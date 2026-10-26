#!/usr/bin/env python3
"""Resolve legacy reference links that are not DOIs to registry records.

WHY. Articles A200 to A296 link the page a reader can open, a publisher's book
page, a JSTOR stable URL, an arXiv abstract, a proceedings site or a search,
rather than a DOI, and about nine thousand such links are too many to read one
page at a time. Most carry an identifier a registry answers for, a DOI in the
path, a JSTOR number, an Elsevier PII, an arXiv number or an ISBN, and most of
the rest name a work a registry can find by its title. This module finds that
record and decides whether it is the work the article meant.

TRUST. A registry record is believed only when it AGREES WITH THE LABEL the
article was written with, which was checked by hand when the article was
drafted. `agrees` states the test. A record found by search must agree on the
title, the first author and the year. A record named by an identifier in the
link itself must agree on the title, or on the first author and the year,
because the link is what the article cited. A record that disagrees is not
used, and the entry falls back to the page or the label, as before.

Every answer is cached raw, one file per identifier or query under the shared
cache, so each value an entry shows can be audited against what the registry
said. Only an HTTP 404 is recorded as absence.
"""

import hashlib
import json
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sources  # noqa: E402

# ------------------------------------------------------------ identifiers in links

# A SICI DOI, Wiley's `10.1002/(SICI)1097-0266(199708)18:7<509::AID-SMJ882>3.0.CO;2-Z`,
# holds angle brackets and semicolons, so the DOI runs to the end of the path.
_DOI_IN = re.compile(r"(10\.\d{4,9}/[^\s?#&]+)")
# Path segments a publisher appends after the DOI, `/abstract`, `/full`, `/pdf`.
_DOI_TAIL = re.compile(r"(?:/(?:abstract|full|pdf|epdf|meta|summary|html|references|figures|fulltext|"
                       r"pdfplus|suppl_file|issue-toc|abs|citedby))+$|\.pdf$", re.I)


def _isbn_ok(digits):
    """Whether a run of ten or thirteen characters is a valid ISBN by its check digit."""
    if len(digits) == 13 and digits.isdigit() and digits[:3] in ("978", "979"):
        s = sum(int(c) * (1 if i % 2 == 0 else 3) for i, c in enumerate(digits[:12]))
        return (10 - s % 10) % 10 == int(digits[12])
    if len(digits) == 10 and digits[:9].isdigit() and (digits[9].isdigit() or digits[9] in "Xx"):
        s = sum(int(c) * (10 - i) for i, c in enumerate(digits[:9]))
        s += 10 if digits[9] in "Xx" else int(digits[9])
        return s % 11 == 0
    return False


def url_identifier(url):
    """(kind, value) for the registry identifier a link's URL carries, or None.

    Kinds are `doi`, `pii` (an Elsevier publisher item, resolved to its DOI by
    Crossref), `arxiv` and `isbn`. A JSTOR stable number is JSTOR's DOI,
    `10.2307/N`, and a Nature article's path is its DOI suffix. An ISBN is taken
    only when its check digit holds, so an article number is not read as one.
    """
    u = urllib.parse.unquote(url.split("#")[0])
    m = re.search(r"arxiv\.org/(?:abs|pdf)/((?:\d{4}\.\d{4,5})|(?:[a-z\-]+(?:\.[A-Z]{2})?/\d{7}))(?:v\d+)?", u)
    if m:
        return "arxiv", m.group(1)
    m = re.search(r"jstor\.org/stable/(?:pdf/)?(\d+)(?:\.pdf)?/?$", u)
    if m:
        return "doi", f"10.2307/{m.group(1)}"
    # NBER WORKING PAPERS, SSRN PAPERS AND eLIFE ARTICLES carry their DOI suffix in
    # the path, `nber.org/papers/w1234` being `10.3386/w1234`.
    m = re.search(r"nber\.org/(?:papers|system/files/working_papers)/(w\d+)", u)
    if m:
        return "doi", f"10.3386/{m.group(1)}"
    m = re.search(r"ssrn\.com/(?:sol3/papers\.cfm\?abstract_id=|abstract=)(\d+)", u)
    if m:
        return "doi", f"10.2139/ssrn.{m.group(1)}"
    m = re.search(r"elifesciences\.org/articles/(\d+)", u)
    if m:
        return "doi", f"10.7554/elife.{m.group(1)}"
    m = re.search(r"nature\.com/articles/([A-Za-z0-9_.\-]*[0-9][A-Za-z0-9_.\-]*)/?$", u)
    if m:
        return "doi", f"10.1038/{m.group(1)}"
    m = re.search(r"sciencedirect\.com/science/article/(?:abs/)?pii/([0-9A-Z]{16,17})", u) or \
        re.search(r"cell\.com/.*/(?:fulltext|abstract|pdf)/(S[0-9X\-()]{16,24})", u)
    if m:
        pii = re.sub(r"[^0-9A-Z]", "", m.group(1))
        # AN OLD ELSEVIER PII, sixteen characters and no leading S, spells its DOI:
        # ISSN, two-digit year, item and check character, `0004370289900774` being
        # `10.1016/0004-3702(89)90077-4`. Crossref does not index these by PII.
        m2 = re.fullmatch(r"(\d{4})(\d{3}[\dX])(\d\d)(\d{5})([\dX])", pii)
        if m2:
            return "doi", f"10.1016/{m2.group(1)}-{m2.group(2)}({m2.group(3)}){m2.group(4)}-{m2.group(5)}".lower()
        return "pii", pii
    m = _DOI_IN.search(u)
    if m:
        doi = _DOI_TAIL.sub("", m.group(1).rstrip(".,;)/"))
        return "doi", doi.lower()
    for m in re.finditer(r"(?<![0-9])(97[89][0-9]{10}|[0-9]{9}[0-9Xx])(?![0-9])", u.replace("-", "")):
        if _isbn_ok(m.group(1)):
            return "isbn", m.group(1).upper()
    return None


# ------------------------------------------------------------ labels

_YEAR = re.compile(r"(?:^|[\s,(])((?:1[5-9]|20)\d\d)[a-z]?(?=$|[\s,)])")
_GIVEN = re.compile(r"^(?:[A-Z][a-zà-öø-ÿ'’\-]+\.?|[A-Z]\.(?:-?[A-Z]\.)*|[A-Z]{1,2})"
                    r"(?:\s+(?:[A-Z][a-zà-öø-ÿ'’\-]+\.?|[A-Z]\.(?:-?[A-Z]\.)*|[A-Z]))*$")
_FAMILY = re.compile(r"^(?:(?:de|del|della|der|van|von|da|di|du|le|la|ten|ter|St\.|Mc|O')\s?)*"
                     r"[A-Z][A-Za-zà-öø-ÿ'’\-]+(?:\s+[A-Z][A-Za-zà-öø-ÿ'’\-]+)?(?:\s+(?:Jr\.|Sr\.|II|III|IV))?$")
_EDITORS = re.compile(r"\s*\((?:editor|editors|eds?\.?)\)\s*$|^(?:editor|editors|eds?\.?)$", re.I)
_SUFFIXES = {"Jr.", "Jr", "Sr.", "Sr", "II", "III", "IV"}
_TITLE_START = {"The", "A", "An", "On", "In", "From", "Toward", "Towards", "How", "Why", "What", "When"}


def _given_like(x):
    x = _EDITORS.sub("", x).strip()
    return bool(x) and len(x.split()) <= 4 and x.split()[0] not in _TITLE_START and bool(_GIVEN.match(x))


def _family_like(x):
    return bool(x) and len(x.split()) <= 3 and x.split()[0] not in _TITLE_START and bool(_FAMILY.match(x))


def _full_form_people(parts):
    """(people, editors, the parts after them) for `Family, Given[, and Family, Given]`.

    The A200 to A236 labels are written in a bibliography's own order, `Curry,
    Haskell B. and Feys, Robert, Combinatory Logic, North-Holland, 1958`, so a
    name is a family part followed by a given part, and further names follow
    `and` or a comma before a later `and`. Returns ([], False, parts) when the
    label does not open that way.
    """
    people, editors, i = [], False, 0
    while i + 1 < len(parts):                       # bound: each pass consumes two parts
        fam = re.sub(r"^and\s+", "", parts[i]).strip()
        giv = parts[i + 1]
        nxt = None
        m = re.match(r"^(.*?)\s+and\s+(.+)$", giv)
        if m:
            giv, nxt = m.group(1), m.group(2)
        if not (_family_like(fam) and _given_like(giv)):
            break
        if _EDITORS.search(giv):
            editors = True
        people.append({"family": fam, "given": _EDITORS.sub("", giv).strip()})
        i += 2
        if i < len(parts) and parts[i] in _SUFFIXES:
            people[-1]["family"] += " " + parts[i].rstrip(".") + ("." if parts[i].startswith(("Jr", "Sr")) else "")
            i += 1
        if i < len(parts) and _EDITORS.match(parts[i]):
            editors = True
            i += 1
        if nxt is not None:
            parts = parts[:i] + [nxt] + parts[i:]
            continue
        # A LONGER LIST puts its `and` before the last name only, so the window
        # reaches four names ahead.
        # AN `and` COUNTS ONLY WHEN A NAME FOLLOWS IT, so `Convergence, and Welfare,
        # What the Long-run Data Show` in Baumol's title is not a list of authors.
        def names_follow(j):
            p = parts[j]
            if p.startswith("and "):
                return j + 1 < len(parts) and _family_like(p[4:]) and _given_like(parts[j + 1])
            m = re.match(r"^(.*?)\s+and\s+(.+)$", p)
            return bool(m) and _given_like(m.group(1)) and _family_like(m.group(2)) and \
                j + 1 < len(parts) and _given_like(parts[j + 1])
        later_and = any(names_follow(j) for j in range(i, min(i + 8, len(parts))))
        if i < len(parts) and parts[i].startswith("and "):
            continue
        if not (later_and and i + 1 < len(parts) and _family_like(parts[i]) and _given_like(parts[i + 1])):
            break
    return people, editors, parts[i:]


# THE OLD LISTS' SECTION NAMES that open a label, beside the categories the importer
# already maps to kinds.
CATEGORY_PREFIXES = {"Future Reading", "Related Post", "Wikipedia", "Industry", "Tool", "Material", "Protocol"}

# PREFIXES WHOSE LABELS NAME PEOPLE. A `ref_` or `data_` label describes a page or a
# record, `Commercial Space Launch Amendments Act 2004`, and its words are no surnames.
PEOPLE_PREFIXES = ("research_", "book_", "paper_", "thesis_", "commentary_", "survey_")


def parse_label(label, anchor=None):
    """{people, editors, year, title, venue, form} from a legacy label in any form.

    `people` is a list of {family, given?}; a family part only, for the
    `Who Year Title` forms, which name surnames. `form` is `full` for the
    bibliography form, `short` for `Who Year [Title]`, and `none` for a
    description, which names no people. Nothing here is trusted on its own; it
    is what a registry record is compared with.
    """
    import sources_import as si
    label = re.sub(r"\s+", " ", (label or "").replace("`", "")).strip()
    out = {"people": [], "editors": False, "year": None, "title": "", "venue": "", "form": "none"}
    if not label:
        return out
    parts = label.split(", ")
    # A CATEGORY BEFORE THE LABEL, `Reference, Mars Ice Home Concept` or `Future Reading,
    # The Hypersonic Revolution`, names the old list's section, not the work.
    if len(parts) >= 2 and (parts[0] in si.LEGACY_KIND or parts[0] in CATEGORY_PREFIXES):
        parts = parts[1:]
        label = ", ".join(parts)
    people, editors, rest = _full_form_people(parts)
    if people and rest:
        year = None
        if rest and re.fullmatch(r"(?:1[5-9]|20)\d\d[a-z]?", rest[-1]):
            year = int(rest[-1][:4])
            rest = rest[:-1]
        # THE LAST PART BEFORE THE YEAR is the publisher or the venue, `MIT Press`
        # or `Annals of Mathematics 33`, when there is more than a title.
        venue = rest.pop() if len(rest) > 1 else ""
        # AN EDITION NOTE, `ninth edition`, is not part of the title.
        rest = [x for x in rest if not re.search(r"\bedition$", x, re.I)]
        out.update(people=people, editors=editors, year=year, title=", ".join(rest), venue=venue, form="full")
        return out
    # TITLE, SURNAMES, YEAR, the A100 to A199 `Future Reading` form, `Computing: A Concise
    # History, Campbell-Kelly, 2012`, with a venue in brackets after the title,
    # `Are Self-Replicating Machines Feasible? (JBIS), Ellery, 2017`.
    if len(parts) >= 3 and re.fullmatch(r"(?:1[5-9]|20)\d\d[a-z]?", parts[-1]) and \
            re.fullmatch(r"[A-Z][\w'’\-]+(?:\s+(?:and|et al\.?)(?:\s+[A-Z][\w'’\-]+)?)*", parts[-2]):
        who = parts[-2]
        fams, inc = si._people_from_label(who)
        title = ", ".join(parts[:-2])
        vm = re.search(r"\s*\(([^)]+)\)$", title)
        venue = vm.group(1) if vm else ""
        title = title[:vm.start()] if vm else title
        out.update(people=[p for p in fams if p.get("family")], year=int(parts[-1][:4]), title=title,
                   venue=venue, form="short", incomplete=inc)
        return out
    who, year, title = si.split_label(label)
    if year:
        fams, out["incomplete"] = si._people_from_label(who)
        describes = anchor is not None and not anchor.startswith(PEOPLE_PREFIXES)
        if describes and not title and not re.search(r"\band\b|\bet al\b", who) and len(who.split()) > 1:
            # A DESCRIPTION WITH A YEAR, `FCC Starlink Authorization March 2018`.
            out.update(year=year, title=who, form="short")
            return out
        # SURNAMES WITHOUT COMMAS OR `and`, `Bruner Goodnow Austin`, are one name each.
        bare = re.sub(r",?\s*(and others|et al\.?)$", "", who).strip()
        if len(fams) == 1 and fams[0].get("name") and not si._ORG.search(bare) and not describes and \
                all(w[:1].isupper() for w in bare.split()):
            fams = [{"family": w} for w in bare.split()]
        # A TITLE IN PLACE OF A NAME, `Falcon 9 User's Guide 2020`, names no people;
        # a label that is only `Boehm 1981` names its author.
        if who and not re.search(r"\d", who) and (not title or si._label_names_people(who, title)):
            out["people"] = [p for p in fams if p.get("family")]
        out.update(year=year, title=title, form="short")
        return out
    out["title"] = label
    return out


def search_label(label, anchor):
    """`parse_label`, with a title taken from the anchor when the label gives none.

    WHY. The A237 to A260 labels are `Boehm 1981`, an author and a year, but their
    anchors often spell the title, `book_boehm_software_engineering_economics`.
    The anchor's words, less the prefix, the authors' names and the year, are a
    title HINT: enough to search by and to compare a registry title with, and
    never printed, since an anchor's words are not the title's own spelling.
    """
    lab = parse_label(label, anchor)
    if lab["title"] or not lab["people"] or not lab["year"]:
        return lab
    fams = {_fold(w) for p in lab["people"] for w in (p.get("family") or "").split()}
    words = [w for w in anchor.split("_")[1:] if not re.fullmatch(r"\d{4}[a-z]?", w)
             and _fold(w) not in fams and w not in ("et", "al", "and", "thesis", "paper", "book")]
    if len(words) >= 2:
        lab = dict(lab, title=" ".join(words), hinted=True)
    return lab


TITLE_FIRST_ITEM = re.compile(r"^- \[\*([^\]]+)\*\]\[([a-z0-9_]+)\], (.+)$", re.M)


def title_first_labels(text):
    """{anchor: label} for items written title first, rewritten in the bibliography form.

    A201 to A204 write `- [*Kinematic Self-Replicating Machines*][anchor], Robert A.
    Freitas Jr. and Ralph C. Merkle, Landes Bioscience, 2004`, names in reading
    order and `edited by` for editors. The label returned is `Freitas Jr., Robert
    A. and Merkle, Ralph C., Kinematic Self-Replicating Machines, Landes
    Bioscience, 2004`, which `parse_label` reads.
    """
    import sources_import as si
    out = {}
    for title, anchor, rest in TITLE_FIRST_ITEM.findall(text):
        parts = [x.strip() for x in rest.split(", ")]
        ym = re.search(r"((?:1[5-9]|20)\d\d)$", parts[-1]) if parts else None
        if not ym:
            continue
        year, parts = ym.group(1), parts[:-1]
        # THE LAST PART IS THE PUBLISHER unless it names people, `Niklaus Wirth and Jürg
        # Gutknecht` before A194's `revised edition 2013`.
        # Names are joined by `and` or carry an initial; `Landes Bioscience` does neither.
        def names_people(x):
            chunks = re.split(r"\s+and\s+", re.sub(r"^edited by\s+", "", x))
            looks = all(re.fullmatch(r"[A-ZÀ-Þ][\w'’\-]+(?:\s+(?:[A-ZÀ-Þ][\w.'’\-]*|de|van|von|der))+", c)
                        and not _PUBLISHER_WORDS.search(c) for c in chunks)
            return looks and (len(chunks) > 1 or bool(re.search(r"\b[A-Z]\.", x)))
        venue = parts.pop() if parts and not names_people(parts[-1]) else ""
        people, editors = [], False
        for chunk in parts:
            if re.search(r"\d", chunk) or si._ORG.search(chunk):
                # A SERIES AND NUMBER, `NASA Conference Publication 2255`, is not a name.
                venue = venue or chunk
                continue
            if chunk.startswith("edited by "):
                if people:              # the authors are named; an editor of their book is not one
                    continue
                editors, chunk = True, chunk[len("edited by "):]
            for name in re.split(r"\s+and\s+", chunk):
                p = si._person(name)
                if p and p.get("family"):
                    people.append(p)
        if not people:
            continue
        names = " and ".join(f"{p['family']}, {p['given']}" if p.get("given") else p["family"] for p in people)
        out[anchor] = (f"{names}{' (editors)' if editors else ''}, {title}"
                       f"{', ' + venue if venue else ''}, {year}")
    return out


# ------------------------------------------------------------ agreement


def _key(s):
    s = sources.clean_text(s or "").lower().replace("&", " and ")
    s = re.sub(r"^(the|a|an)\s+", "", s)
    return re.sub(r"[^a-z0-9]", "", s)


def _words(s):
    s = sources.clean_text(s or "").lower().replace("&", " and ")
    return [w for w in re.findall(r"[a-z0-9]+", s) if w not in ("the", "a", "an", "and", "of")]


def title_agrees(label_title, title):
    """Whether a label's title names the same work as a registry title.

    Equal ignoring case, punctuation and a leading article; or the label is the
    main title, the registry adding a subtitle; or the label is a short title,
    every word of it in the registry's opening words in order. A label writes a
    colon as a comma, so commas are ignored.
    """
    a, b = _key(label_title), _key(title)
    if not a or not b:
        return False
    if a == b or b.startswith(a) and len(a) >= 12:
        return True
    # A REGISTRY TITLE WITHOUT THE SUBTITLE the label gives, `Why Nations Fail` for
    # the label's `Why Nations Fail, The Origins of Power, Prosperity, and Poverty`.
    if a.startswith(b) and len(b) >= 12 and len(_words(title)) >= 2:
        return True
    main = _key(re.split(r"[:?.]\s", sources.clean_text(title), maxsplit=1)[0])
    if a == main:
        return True
    la, lb = _words(label_title), _words(title)
    return len(la) >= 2 and lb[:len(la) + 3] and all(w in lb[:len(la) + 3] for w in la) \
        and len(la) >= 0.5 * len(lb[:len(la) + 3])


def _fold(x):
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFKD", (x or "").lower()) if c.isalpha())


def people_agree(label_people, families):
    """Whether the label's first family name is among the record's first three."""
    if not label_people:
        return False
    first = _fold(label_people[0].get("family") or label_people[0].get("name") or "")
    return bool(first) and any(first == _fold(f) or _fold(f).endswith(first) and len(first) > 3
                               for f in families[:3])


def _authors_say_it(lab, families):
    """Whether a record's authors confirm a label that gives no title: same first, and its second too."""
    fams = [_fold(p.get("family") or "") for p in lab["people"]]
    rec = [_fold(f) for f in families if f]
    if lab["title"] and not lab.get("hinted"):
        return True
    if not rec or rec[0] != fams[0] and not (len(fams[0]) > 3 and rec[0].endswith(fams[0])):
        return False
    if len(fams) >= 2 and not lab.get("incomplete"):
        return fams[1] in rec
    return True


def _org_like(name):
    """Whether a label's one name is written as an organisation's, `OpenAI`, `DeepMind`, `NASA`."""
    import sources_import as si
    return bool(re.search(r"[a-z][A-Z]|^[A-Z]{2,}$", name) or si._ORG.search(name))


def agrees(lab, title, families, year, by_identifier, slack=1):
    """(ok, why) for whether a registry record is the work a parsed label names.

    `by_identifier` is True when the link itself names the record, so the label
    may lack a title, as the `Boehm 1981` labels do. A registry's year may be the
    online year or a later edition's, hence `slack`.
    """
    t_ok = bool(lab["title"]) and title_agrees(lab["title"], title)
    p_ok = people_agree(lab["people"], families) if lab["people"] else None
    y_ok = None if not (lab["year"] and year) else abs(int(lab["year"]) - int(year)) <= slack
    if by_identifier:
        if t_ok and p_ok is not False:
            return True, "title and authors agree"
        if t_ok and not lab["people"]:
            return True, "title agrees"
        # WITHOUT A TITLE the authors must say it: the record's first author is the
        # label's, and a label naming two or more people in full names a second the
        # record also names. `Bubeck Eldan and Lee 2017` once took Bubeck and Eldan's
        # 2015 paper, and `Bellemare Dabney Munos 2017` a 2018 paper Bellemare was third on.
        if p_ok and y_ok and _authors_say_it(lab, families):
            return True, "first author and year agree"
        if t_ok and y_ok:
            return True, "title and year agree"
        # A LABEL NAMING AN ORGANISATION, `OpenAI 2019`, for a paper its staff wrote
        # cannot agree on the author, and gives no title; the link's own identifier
        # and the exact year are then the evidence, and the reason says so.
        if not lab["title"] and lab["year"] and year and int(lab["year"]) == int(year) and \
                len(lab["people"]) == 1 and p_ok is False and _org_like(lab["people"][0].get("family") or ""):
            return True, "only the year agrees, the label naming an organisation"
        return False, f"disagrees: title {t_ok}, author {p_ok}, year {y_ok}"
    if t_ok and p_ok and y_ok is not False:
        return True, "title, first author and year agree"
    if t_ok and not lab["people"] and y_ok and len(_key(lab["title"])) >= 12:
        return True, "title and year agree"
    return False, f"disagrees: title {t_ok}, author {p_ok}, year {y_ok}"


# ------------------------------------------------------------ caches


def _safe(x):
    return re.sub(r"[^A-Za-z0-9._\-]", "_", x)


def cache_path(cache, server, ident):
    return os.path.join(cache, server, _safe(ident.lower() if server != "isbn" else ident) + ".json")


def query_path(cache, engine, query):
    h = hashlib.sha1(query.encode("utf-8")).hexdigest()[:16]
    return os.path.join(cache, "search", engine, h + ".json")


def page_path(cache, url):
    h = hashlib.sha1(url.encode("utf-8")).hexdigest()[:20]
    return os.path.join(cache, "pages", h + ".json")


def _load(path):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    return None


def _save(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1, sort_keys=True, ensure_ascii=False)
    os.replace(tmp, path)


def _settled(path):
    return any(os.path.exists(path + m) for m in ("", ".missing", ".unreadable"))


# ------------------------------------------------------------ fetchers
#
# Each takes a list in the order to fetch, skips what is cached or settled, and
# returns (fetched, missing, failed). A refusal or a timeout caches nothing, so
# a rerun asks again.


def fetch_pii(piis, cache):
    """Resolve Elsevier PIIs to DOIs through Crossref's `alternative-id` filter.

    One PII a request: two in one filter answered with an unparseable reply on
    2026-10-25. The answer cached is the matching Crossref message itself, so the
    DOI's record needs no second request.
    """
    import fetch
    got = miss = failed = 0
    for pii in dict.fromkeys(piis):                   # bound: one request a PII
        path = cache_path(cache, "pii", pii)
        if _settled(path):
            continue
        j, status = fetch.get_json_status(f"{fetch.CROSSREF}?filter=alternative-id:{pii}&rows=2")
        items = ((j or {}).get("message") or {}).get("items")
        if items is None:
            failed += 1
            continue
        hits = [it for it in items if pii in [re.sub(r"[^0-9A-Z]", "", x) for x in it.get("alternative-id", [])]]
        if len(hits) == 1:
            _save(path, hits[0])
            got += 1
        else:
            open(path + ".missing", "w").close()
            miss += 1
    return got, miss, failed


def arxiv_doi(ident):
    return f"10.48550/arXiv.{ident}"


def fetch_datacite(dois, cache):
    """Cache DataCite's attributes for DOIs Crossref does not hold, arXiv's among them.

    WHY. arXiv's own interface answered `Rate exceeded` to the first request on
    2026-10-25, and arXiv registers its DOIs with DataCite, which answers singly.
    """
    import fetch
    got = miss = failed = 0
    for doi in dict.fromkeys(dois):                   # bound: one request a DOI
        path = cache_path(cache, "datacite", doi)
        if _settled(path):
            continue
        j, status = fetch.get_json_status(f"https://api.datacite.org/dois/{urllib.parse.quote(doi, safe='/')}")
        if j and (j.get("data") or {}).get("attributes"):
            _save(path, j["data"]["attributes"])
            got += 1
        elif status == 404:
            open(path + ".missing", "w").close()
            miss += 1
        else:
            failed += 1
    return got, miss, failed


def fetch_isbn(isbns, cache):
    """Cache Open Library's edition for each ISBN, with the key of its work.

    The work itself is then fetched by `fetch-reports openlibrary`, which
    collects its editions and authors, so a book found by ISBN and one linked to
    Open Library are built the same way.
    """
    import fetch
    got = miss = failed = 0
    for isbn in dict.fromkeys(isbns):                 # bound: one request an ISBN
        path = cache_path(cache, "isbn", isbn)
        if _settled(path):
            continue
        j, status = fetch.get_json_status(f"https://openlibrary.org/isbn/{isbn}.json")
        if j and j.get("works"):
            _save(path, j)
            got += 1
        elif status == 404 or (j is not None and not j.get("works")):
            open(path + ".missing", "w").close()
            miss += 1
        else:
            failed += 1
    return got, miss, failed


def book_query(lab, main=False):
    """The Open Library search for a label: its title and first surname.

    `main` asks by the main title alone, the part before a subtitle the label
    writes after a comma, since a search for `The Rise and Fall of the Great
    Powers, Economic Change and Military Conflict from 1500 to 2000` found nothing.
    """
    fam = (lab["people"][0].get("family") or "") if lab["people"] else ""
    title = lab["title"].split(", ")[0] if main else lab["title"]
    return {"title": title, "author": fam}


def work_query(lab):
    """The Crossref bibliographic query for a label: title, first surname, year."""
    fam = (lab["people"][0].get("family") or "") if lab["people"] else ""
    return " ".join(x for x in (lab["title"], fam, str(lab["year"] or "")) if x)


def fetch_book_searches(labs, cache):
    """Search Open Library for each label's book, caching the raw answer by query."""
    import fetch
    got = failed = 0
    queries = []
    for lab in labs:
        queries.append(book_query(lab))
        if ", " in lab["title"]:
            res = _load(query_path(cache, "openlibrary", json.dumps(book_query(lab), sort_keys=True)))
            if res is not None and not book_candidate(lab, cache)[0]:
                queries.append(book_query(lab, True))
    for q in queries:                                  # bound: two requests a label
        key = json.dumps(q, sort_keys=True)
        path = query_path(cache, "openlibrary", key)
        if os.path.exists(path):
            continue
        params = {k: v for k, v in q.items() if v}
        params.update(limit="8", fields="key,title,subtitle,author_name,first_publish_year,edition_count")
        j = fetch.get_json(f"https://openlibrary.org/search.json?{urllib.parse.urlencode(params)}")
        if j is None:
            failed += 1
            continue
        _save(path, {"query": q, "docs": j.get("docs") or []})
        got += 1
    return got, 0, failed


def fetch_work_searches(labs, cache):
    """Search Crossref for each label's work, caching the raw answer by query."""
    import fetch
    got = failed = 0
    for lab in labs:                                   # bound: one request a label
        q = work_query(lab)
        path = query_path(cache, "crossref", q)
        if os.path.exists(path):
            continue
        params = {"query.bibliographic": q, "rows": "5"}
        j = fetch.get_json(f"{fetch.CROSSREF}?{urllib.parse.urlencode(params)}")
        if j is None:
            failed += 1
            continue
        _save(path, {"query": q, "items": (j.get("message") or {}).get("items") or []})
        got += 1
    return got, 0, failed


# Hosts whose pages state their own bibliographic metadata in `citation_*` tags
# and are read live. Every other page is read from its Internet Archive capture
# nearest the article's date, which is also nearer what the author read.
# OpenReview is not among them: its pages and its API both answered with a browser
# challenge on 2026-10-25, which this project does not answer, so its captures are read.
LIVE_HOSTS = ("papers.nips.cc", "proceedings.neurips.cc", "proceedings.mlr.press", "jmlr.org", "www.jmlr.org",
              "aclanthology.org", "ojs.aaai.org", "www.ijcai.org", "ijcai.org",
              "openaccess.thecvf.com", "www.jair.org", "jair.org", "www.usenix.org")


def fetch_pages(urls, cache, dates):
    """Cache each page's own head metadata, live for `LIVE_HOSTS`, else from its capture.

    `dates` maps a URL to the YYYYMMDD the article was dated, which picks the
    capture. The Wayback Machine answers a timestamp with its nearest capture,
    and the capture's own timestamp is recorded. Bot challenges are not answered:
    a page that serves one is recorded as unread.
    """
    import fetch
    import sources_import as si
    got = miss = failed = streak = 0
    for url in dict.fromkeys(urls):                   # bound: one request a URL
        path = page_path(cache, url)
        if _settled(path):
            continue
        host = urllib.parse.urlsplit(url).netloc.lower()
        live = host in LIVE_HOSTS
        src = url if live else f"https://web.archive.org/web/{dates.get(url, '2026')}id_/{url}"
        item = re.match(r"https?://(?:www\.)?archive\.org/details/([^/?#]+)", url)
        if item:
            # AN INTERNET ARCHIVE ITEM states its own metadata; the Wayback Machine does
            # not replay archive.org, answering 403. An empty answer is no such item.
            j, status = fetch.get_json_status(f"https://archive.org/metadata/{item.group(1)}", tries=2)
            if j is None:
                failed += 1
                continue
            md = j.get("metadata") or {}
            if not md:
                open(path + ".missing", "w").close()
                miss += 1
                continue
            who = md.get("creator") or []
            who = [who] if isinstance(who, str) else who
            date = str(md.get("date") or md.get("year") or "")
            dm = re.search(r"(\d{4})(?:-(\d\d))?(?:-(\d\d))?", date)
            _save(path, {"url": url, "read_from": f"https://archive.org/metadata/{item.group(1)}", "live": True,
                         "status": "read", "meta": {
                             "title": sources.clean_text(md["title"] if isinstance(md.get("title"), str)
                                                         else (md.get("title") or [""])[0]) or None,
                             "authors": [p for p in (si._person(w) for w in who[:12]) if p],
                             "container": None, "publisher": (md.get("publisher") if isinstance(
                                 md.get("publisher"), str) else None),
                             "date": "-".join(g for g in dm.groups() if g) if dm else None, "doi": None,
                             "conference": None, "journal": None, "volume": None, "og_type": "book"
                             if md.get("mediatype") == "texts" else None, "pages": None}})
            got += 1
            continue
        # ONE TRY: a refusal is asked again by the next run, and retrying a capture the
        # archive will not replay cost two requests and a backoff for every one.
        body, status = fetch.get_bytes_status(src, tries=1 if not live else 2, timeout=30)
        if body is None:
            # NO CAPTURE AT ALL is a 404 from the archive, absence; anything else is retried.
            if status == 404:
                open(path + ".missing", "w").close()
                miss += 1
            else:
                # A 403 IS NOT SETTLED: the archive gives it both for a site excluded from it
                # and to a client it is throttling. A run of failures pauses the reader.
                failed += 1
                streak += status is None
                if streak >= 5:
                    import time
                    time.sleep(120)
                    streak = 0
            continue
        streak = 0
        if body[:2] == b"\x1f\x8b":
            # AAAI'S PAGES ARRIVE COMPRESSED whether or not compression was asked for.
            # A TRUNCATED CAPTURE is decompressed as far as it goes; its head is what matters.
            import zlib
            try:
                body = zlib.decompressobj(16 + zlib.MAX_WBITS).decompress(body)
            except zlib.error:
                pass
        row = {"url": url, "read_from": src, "live": live}
        if body[:5] == b"%PDF-":
            row.update(status="pdf")
        else:
            try:
                text = body.decode("utf-8")
            except UnicodeDecodeError:
                text = body.decode("cp1252", "replace")
            if re.search(r"anubis_challenge|cf-chl-|Just a moment\.\.\.|Making sure you.re not a bot|Verifying your browser|"
                         r"ChallengeRequiredError", text):
                row.update(status="challenge")
            else:
                md = si.page_metadata(text)
                # IEEE STATES ITS DOI in the page's own document metadata, a script
                # object, not in a meta tag.
                m = re.search(r'"doi":"(10\.\d{4,9}/[^"]+)"', text) if "ieeexplore" in host else None
                if m and not md.get("doi"):
                    md["doi"] = m.group(1)
                row.update(status="read", meta=md)
        _save(path, row)
        got += 1
    return got, miss, failed


# ------------------------------------------------------------ records


def record_from_datacite(anchor, attrs, doi):
    """A preprint record from DataCite attributes, as arXiv registers its DOIs."""
    import sources_import as si
    people = []
    for c in attrs.get("creators") or []:
        # A CREATOR WITH NO LETTERS, `:` beside OpenAI's staff, is no one; an
        # organisation, `Adaptive Agent Team`, keeps its name whole.
        if not re.search(r"\w", c.get("name") or c.get("familyName") or ""):
            continue
        if c.get("nameType") == "Organizational":
            people.append({"name": sources.clean_text(c.get("name") or "")})
        elif c.get("familyName"):
            people.append({"family": c["familyName"], "given": c.get("givenName") or ""})
        elif c.get("name"):
            people.append(si._person(c["name"]) or {"name": c["name"]})
    title = sources.clean_text(((attrs.get("titles") or [{}])[0]).get("title", ""))
    # AN arXiv DOI is a preprint whatever type its record states.
    kind = "preprint" if (attrs.get("types") or {}).get("resourceTypeGeneral") == "Preprint" or \
        doi.lower().startswith("10.48550/arxiv.") else "other"
    rec = {"anchor": anchor, "kind": kind, "doi": doi.lower(), "title_published": title,
           "title": si.headline_case(title), "authors": si._authors(people),
           "year": attrs.get("publicationYear")}
    if kind == "preprint":
        rec["container"] = sources.clean_text(attrs.get("publisher") or "arXiv")
    elif attrs.get("publisher"):
        rec["publisher"] = sources.clean_text(attrs["publisher"])
    return rec


def _crossref_families(msg):
    return [a.get("family", "") for a in (msg.get("author") or msg.get("editor") or []) if a.get("family")]


def _crossref_year(msg):
    import fetch
    return fetch.crossref_fields(msg)[2]


def _ol_families(names):
    import sources_import as si
    out = []
    for n in names or []:
        p = si._person(n) or {}
        out.append(p.get("family") or p.get("name") or "")
    return out


def is_search(url):
    """Whether a link is a search, which names no document."""
    return bool(re.search(r"scholar\.google\.|/search(?:\.jsp)?\?|[?&](?:q|query)=", url))


def book_candidate(lab, cache):
    """(search result, why) for the first cached Open Library result agreeing with the label."""
    res = _load(query_path(cache, "openlibrary", json.dumps(book_query(lab), sort_keys=True))) or {}
    if ", " in lab["title"]:
        more = _load(query_path(cache, "openlibrary", json.dumps(book_query(lab, True), sort_keys=True)))
        res = {"docs": (res.get("docs") or []) + ((more or {}).get("docs") or [])}
    for doc in (res or {}).get("docs", []):           # bound: sixteen results, two searches
        fpy = doc.get("first_publish_year")
        # A BOOK'S FIRST EDITION cannot postdate the year the article cites it by;
        # a later edition may well be the one cited, so no lower bound.
        y_ok = fpy is None or lab["year"] is None or fpy <= lab["year"] + 1
        if not lab["people"]:
            # A LABEL NAMING NO ONE matches on its title alone, so the title must be long
            # enough to identify a book and the book must be old enough: A267's
            # `Frame of Government 1682 Pennsylvania` once matched a 2000 novel titled
            # `Pennsylvania`.
            y_ok = fpy is not None and lab["year"] is not None and fpy <= lab["year"] + 1 and \
                len(_key(lab["title"])) >= 12
        ok, why = agrees(lab, doc.get("title") or "", _ol_families(doc.get("author_name")), lab["year"], False,
                         slack=1000)
        if ok and y_ok and doc.get("key"):
            return doc, why
    return None, "no search result agrees"


def registry_record(anchor, url, label, cache, crossref_cache, fuller=None):
    """(record or None, how) for a non-DOI link from the caches, if one agrees with the label.

    Tries, in order, the identifier the URL carries, then a search by the
    label's title. Returns (None, why) when nothing agrees, and the caller builds
    the entry from the page or the label instead.
    """
    import sources_import as si
    lab = search_label(label, anchor)
    ident = url_identifier(url)
    tried = []
    if ident:
        kind, value = ident
        if kind == "pii":
            msg = _load(cache_path(cache, "pii", value))
            if msg:
                ok, why = agrees(lab, (msg.get("title") or [""])[0], _crossref_families(msg), _crossref_year(msg), True)
                if ok:
                    rec = si.record_from_crossref(anchor, msg, msg["DOI"])
                    return rec, f"the DOI Crossref gives for the Elsevier item {value} the article linked, {why}"
                tried.append(f"PII {value}: {why}")
        elif kind == "doi":
            msg = _load(si.crossref_cache_path(crossref_cache, value))
            if msg:
                ok, why = agrees(lab, (msg.get("title") or [""])[0], _crossref_families(msg), _crossref_year(msg), True)
                if ok:
                    return si.record_from_crossref(anchor, msg, value), f"the DOI {value} the linked URL carries, {why}"
                tried.append(f"DOI {value}: {why}")
            else:
                d = _load(cache_path(cache, "datacite", value))
                if d:
                    fams = [c.get("familyName") or "" for c in d.get("creators") or []]
                    ok, why = agrees(lab, ((d.get("titles") or [{}])[0]).get("title", ""), fams,
                                     d.get("publicationYear"), True)
                    if ok:
                        return record_from_datacite(anchor, d, value), f"DataCite's record of {value}, {why}"
                    tried.append(f"DataCite {value}: {why}")
        elif kind == "arxiv":
            doi = arxiv_doi(value)
            d = _load(cache_path(cache, "datacite", doi))
            if d:
                fams = [c.get("familyName") or "" for c in d.get("creators") or []]
                ok, why = agrees(lab, ((d.get("titles") or [{}])[0]).get("title", ""), fams,
                                 d.get("publicationYear"), True, slack=2)
                if ok:
                    return record_from_datacite(anchor, d, doi), f"DataCite's record of arXiv {value}, {why}"
                tried.append(f"arXiv {value}: {why}")
        elif kind == "isbn":
            ed = _load(cache_path(cache, "isbn", value))
            work = (((ed or {}).get("works") or [{}])[0]).get("key", "").lstrip("/")
            w = _load(si.report_cache_path(cache, "openlibrary", work)) if work else None
            if w:
                ok, why = agrees(lab, w.get("title") or "", _ol_families(w.get("_author_names")),
                                 lab["year"], True)
                if ok:
                    rec = _book_record(anchor, w, work, lab, url)
                    return rec, f"Open Library's {work} for the ISBN {value} the linked URL carries, {why}"
                tried.append(f"ISBN {value}: {why}")
    page = _load(page_path(cache, url))
    if proceedings_index_url(url) and not ((page or {}).get("meta") or {}).get("title"):
        # A PROCEEDINGS LINK THAT SERVES NO PAPER is matched in its proceedings' index.
        paper, why = proceedings_match(url, lab, cache)
        if paper:
            rec = record_from_proceedings(anchor, paper, lab)
            how = (f"the link serves no paper, so the paper is {why}" if paper["url"] != url else why)
            return rec, how
        tried.append(f"proceedings index: {why}")
    pdoi = ((page or {}).get("meta") or {}).get("doi")
    if pdoi:
        pdoi = pdoi.lower().replace("https://doi.org/", "")
        msg = _load(si.crossref_cache_path(crossref_cache, pdoi))
        if msg:
            ok, why = agrees(lab, (msg.get("title") or [""])[0], _crossref_families(msg), _crossref_year(msg), True)
            if ok:
                return si.record_from_crossref(anchor, msg, pdoi), f"the DOI {pdoi} the page itself states, {why}"
            tried.append(f"page DOI {pdoi}: {why}")
    # A DESCRIPTION, a `ref_` label such as `NASA Commercial Crew Program 2014`, is not
    # searched by title: it once matched a 2015 book chapter on the programme.
    if lab["title"] and (anchor.startswith(PEOPLE_PREFIXES) or lab["form"] == "full"):
        doc, why = book_candidate(lab, cache)
        if doc:
            work = doc["key"].lstrip("/")
            w = _load(si.report_cache_path(cache, "openlibrary", work))
            if w:
                # A SEARCH LINK, or a Wikipedia article standing in for the book, names
                # no copy of the work, so the entry links the work found.
                at = f"https://openlibrary.org/{work}" if is_search(url) or "wikipedia.org/" in url else url
                return _book_record(anchor, w, work, lab, at), f"Open Library's {work}, found by title, {why}"
        res = _load(query_path(cache, "crossref", work_query(lab)))
        for msg in (res or {}).get("items", [])[:5]:
            ok, why = agrees(lab, (msg.get("title") or [""])[0], _crossref_families(msg), _crossref_year(msg), False)
            if ok and msg.get("type") not in ("component", "peer-review", "grant"):
                return si.record_from_crossref(anchor, msg, msg["DOI"]), \
                    f"Crossref's {msg['DOI']}, found by title, {why}"
    full = search_label(fuller, anchor) if fuller else lab
    # ONLY WHEN THE LINK'S OWN PAGE CANNOT BE READ: the page is the version the
    # article linked, a proceedings paper before its preprint.
    if not lab["title"] and len(full["people"]) >= 2 and full["year"] and not page_meta(cache, url, label):
        # AUTHORS AND A YEAR ONLY: the one arXiv record by exactly those authors.
        attrs, why = author_match(full, cache)
        if attrs:
            return record_from_datacite(anchor, attrs, attrs["doi"]), f"DataCite's {attrs['doi']}, {why}"
        tried.append(why)
    return None, "; ".join(tried) or "no registry record agrees"


def _book_record(anchor, w, work, lab, url):
    """A book from a cached Open Library work, at the article's own link."""
    import sources_import as si
    who = ", ".join(p.get("family", "") for p in lab["people"]) if lab["people"] else None
    rec = si.record_from_openlibrary(anchor, w, work, lab["year"], who)
    # THE ARTICLE'S LINK IS KEPT, so its reader still reaches the page the author
    # gave, and two articles that link the same page cite one source.
    rec["url"] = url
    # GIVEN NAMES FROM A FULL LABEL, `Church, Alonzo`, where Open Library kept only
    # the surnames the label supplied.
    full = {_fold(p["family"]): p for p in lab["people"] if p.get("given")}
    rec["authors"] = [dict(a, given=full[_fold(a["family"])]["given"])
                      if a.get("family") and not a.get("given") and _fold(a["family"]) in full else a
                      for a in rec.get("authors", [])]
    # A CONTRIBUTOR THE LABEL DOES NOT NAME, an audiobook's narrator such as Dennis
    # Holland beside Kuhn, is not an author, unless the label's list is incomplete.
    fams = {_fold(p.get("family") or "") for p in lab["people"]}
    if fams and not lab.get("incomplete") and len(rec.get("authors", [])) > len(fams):
        kept = [a for a in rec["authors"] if _fold(a.get("family") or a.get("name") or "") in fams]
        if kept:
            rec["authors"] = kept
    if lab["editors"] and not rec.get("editors"):
        rec["editors"], rec["authors"] = rec.pop("authors"), []
    return rec


# ------------------------------------------------------------ planning


def plan(posts, cache, crossref_cache):
    """{task: [items]} of what remains to fetch for the posts' non-DOI links."""
    import sources_import as si
    todo = {"crossref_dois": [], "pii": [], "datacite": [], "isbn": [], "openlibrary_works": [],
            "book_search": [], "work_search": [], "pages": {}, "proceedings": {}, "book_docs": {},
            "author_search": []}
    for post in posts:
        text = open(post, encoding="utf-8").read()
        date = re.search(r"^date:\s*(\d{4})-(\d\d)-(\d\d)", text, re.M)
        stamp = "".join(date.groups()) if date else "2026"
        labels, fuller = article_labels(text)
        for a, target in si.link_definitions(text).items():
            url = target.split()[0]
            lab = search_label(labels.get(a, ""), a)
            if url.startswith("https://en.wikipedia.org/") and lab["people"] and lab["year"] and lab["title"]:
                # A WIKIPEDIA LINK STANDING IN FOR THE WORK ITS LABEL NAMES is sought by title.
                todo["book_search"].append(lab)
                doc, _why = book_candidate(lab, cache)
                if doc:
                    todo["openlibrary_works"].append(doc["key"].lstrip("/"))
                    todo["book_docs"][doc["key"].lstrip("/")] = doc
                todo["work_search"].append(lab)
                continue
            rep = si._report_ident(url)
            if rep and rep[0] == "openlibrary" and lab["title"] and lab["year"]:
                # A LINKED WORK THAT DISAGREES WITH ITS LABEL is sought again by title.
                w = _load(si.report_cache_path(cache, "openlibrary", rep[1]))
                if w and not title_agrees(lab["title"], w.get("title") or ""):
                    todo["book_search"].append(lab)
                    doc, _why = book_candidate(lab, cache)
                    if doc:
                        todo["openlibrary_works"].append(doc["key"].lstrip("/"))
                        todo["book_docs"][doc["key"].lstrip("/")] = doc
                continue
            if not url.startswith("http") or url.startswith(("https://doi.org/", "https://en.wikipedia.org/")) \
                    or rep:
                continue
            ident = url_identifier(url)
            rec = None
            if ident:
                kind, value = ident
                if kind == "doi":
                    todo["crossref_dois"].append(value)
                    if os.path.exists(si.crossref_cache_path(crossref_cache, value) + ".missing"):
                        todo["datacite"].append(value)
                elif kind == "pii":
                    todo["pii"].append(value)
                elif kind == "arxiv":
                    todo["datacite"].append(arxiv_doi(value))
                elif kind == "isbn":
                    todo["isbn"].append(value)
                    ed = _load(cache_path(cache, "isbn", value))
                    work = (((ed or {}).get("works") or [{}])[0]).get("key", "").lstrip("/")
                    if work:
                        todo["openlibrary_works"].append(work)
                rec, _why = registry_record(a, url, labels.get(a, ""), cache, crossref_cache)
            if rec is None and lab["title"] and lab["year"]:
                if a.startswith("book_") or lab["form"] == "full" and not re.search(r"\d", lab["venue"]):
                    todo["book_search"].append(lab)
                    doc, _why = book_candidate(lab, cache)
                    if doc:
                        todo["openlibrary_works"].append(doc["key"].lstrip("/"))
                        todo["book_docs"][doc["key"].lstrip("/")] = doc
                if not a.startswith("book_") or lab["form"] == "full":
                    todo["work_search"].append(lab)
                rec, _why = registry_record(a, url, labels.get(a, ""), cache, crossref_cache)
            pi = proceedings_index_url(url, lab["year"])
            if pi:
                todo["proceedings"][pi[0]] = pi[1]
                if pi[0].startswith("neurips_") and lab["year"]:
                    todo["proceedings"][f"neurips_{lab['year'] - 1}"] = \
                        f"https://papers.nips.cc/paper_files/paper/{lab['year'] - 1}"
            if rec is None and not lab["title"]:
                full = search_label(fuller.get(a, labels.get(a, "")), a)
                if len(full["people"]) >= 2 and full["year"] and not full.get("incomplete"):
                    todo["author_search"].append(full)
                    rec, _why = registry_record(a, url, labels.get(a, ""), cache, crossref_cache, fuller.get(a))
            if rec is None:
                todo["pages"][url] = stamp
                page = _load(page_path(cache, url))
                pdoi = ((page or {}).get("meta") or {}).get("doi")
                if pdoi:
                    todo["crossref_dois"].append(pdoi.lower().replace("https://doi.org/", ""))
    return todo


STEPS = ("crossref", "pii", "datacite", "isbn", "works", "book-search", "work-search", "pages", "proceedings",
         "author-search")


def run_step(step, posts, cache, crossref_cache, shard=(0, 1)):
    """Fetch what one step of `plan` still lacks. Returns its (fetched, missing, failed).

    The steps depend on one another, an ISBN's work on its edition, a search on
    the identifiers that failed to agree, so they are run in `STEPS` order and
    the plan is recomputed from the caches before each. Crossref is asked by one
    process at a time, as its public pool requires.
    """
    import sources_import as si
    todo = plan(posts, cache, crossref_cache)
    k, n = shard
    if step == "crossref":
        path = os.path.join(cache, "resolve_dois.txt")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(dict.fromkeys(todo["crossref_dois"])) + "\n")
        _dois, missing = si.fetch_crossref("@" + path, crossref_cache)
        return len(todo["crossref_dois"]), len(missing), 0
    if step == "pii":
        return fetch_pii(todo["pii"], cache)
    if step == "datacite":
        return fetch_datacite(todo["datacite"], cache)
    if step == "isbn":
        return fetch_isbn(todo["isbn"][k::n], cache)
    if step == "works":
        works = sorted(set(w for w in todo["openlibrary_works"] if w))[k::n]
        light = fetch_works_light(works, cache, todo["book_docs"])
        rest = [w for w in works if w not in todo["book_docs"]]
        full = si.fetch_reports(rest, cache, "openlibrary")
        return light[0] + full[0], light[1] + full[1], light[2] + full[2]
    if step == "book-search":
        return fetch_book_searches(todo["book_search"][k::n], cache)
    if step == "work-search":
        return fetch_work_searches(todo["work_search"], cache)
    if step == "author-search":
        return fetch_author_searches(todo["author_search"], cache)
    if step == "proceedings":
        return fetch_proceedings_indexes(todo["proceedings"], cache)
    if step == "pages":
        urls = sorted(todo["pages"])[k::n]
        return fetch_pages(urls, cache, todo["pages"])
    raise ValueError(step)


def main(argv):
    import argparse
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plan", help="count what remains to fetch for the posts' non-DOI links")
    p.add_argument("posts", nargs="+")
    p.add_argument("--cache", default="tmp/sources")
    p.add_argument("--crossref-cache", default="tmp/sources/crossref")
    p = sub.add_parser("fetch", help="run one resolution step for the posts")
    p.add_argument("step", choices=STEPS)
    p.add_argument("posts", nargs="+")
    p.add_argument("--cache", default="tmp/sources")
    p.add_argument("--crossref-cache", default="tmp/sources/crossref")
    p.add_argument("--shard", default="0/1", help="k/n, this process's share, for the steps on other hosts")
    p = sub.add_parser("normalise", help="make legacy posts readable to the converter, in place")
    p.add_argument("posts", nargs="+")
    p = sub.add_parser("explain", help="print how each non-DOI link of a post resolves")
    p.add_argument("post")
    p.add_argument("--cache", default="tmp/sources")
    p.add_argument("--crossref-cache", default="tmp/sources/crossref")
    a = ap.parse_args(argv)
    if a.cmd == "plan":
        todo = plan(a.posts, a.cache, a.crossref_cache)
        for k, v in todo.items():
            print(f"{k}: {len(set(map(str, v)) if not isinstance(v, dict) else v)}")
        return 0
    if a.cmd == "normalise":
        paths, slugs = post_paths()
        for path in a.posts:
            text = open(path, encoding="utf-8").read()
            new, notes = normalise_legacy(text, paths, slugs)
            if new != text:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(new)
            print(f"{path}: {len(notes)} change(s)")
        return 0
    if a.cmd == "fetch":
        k, n = (int(x) for x in a.shard.split("/"))
        got, miss, failed = run_step(a.step, a.posts, a.cache, a.crossref_cache, (k, n))
        print(f"{a.step}: {got} fetched, {miss} missing, {failed} refused or timed out")
        return 0
    import sources_import as si
    text = open(a.post, encoding="utf-8").read()
    labels, fuller = article_labels(text)
    for anc, target in sorted(si.link_definitions(text).items()):
        url = target.split()[0]
        if not url.startswith("http") or url.startswith(("https://doi.org/", "https://en.wikipedia.org/")):
            continue
        rec, how = registry_record(anc, url, labels.get(anc, ""), a.cache, a.crossref_cache, fuller.get(anc))
        if rec:
            print(f"REG {anc}: {how}")
            continue
        meta = page_meta(a.cache, url, labels.get(anc, ""))
        print(f"PAGE {anc}: {meta['title'][:80]!r}" if meta else f"-- {anc}: {how}")
    return 0



# ------------------------------------------------------------ pages and labels

_GENERIC = {"case", "study", "report", "page", "history", "overview", "home", "official", "site", "website",
            "program", "programme", "news", "press", "release", "data", "database", "series", "book", "paper",
            "primary", "text", "document", "documents", "archive", "guide", "handbook", "in", "on", "to", "for"}
_JUNK_TITLE = re.compile(r"^(page not found|404|not found|access denied|just a moment|wayback machine|"
                         r"attention required|error|forbidden|home|index|untitled|redirect|object moved|"
                         r"301 moved|302 found|sign in|log ?in|subscribe)\b", re.I)
_JUNK_AUTHOR = re.compile(r"staff|editor|admin|team|desk|newsroom|@|https?:|www\.|\.com\b|press office|"
                          r"communications|webmaster|contributor", re.I)


def page_meta(cache, url, label):
    """A web-metadata entry, the form `record_from_web` reads, from a cached page, or None.

    A capture is distrusted when its title is a site's name, an error page, or
    shares no word with a label that has a title, which is what a capture
    redirected to a home page shows. An author that is the site itself, or a
    desk or a staff line, is not an author.
    """
    import sources_import as si
    row = _load(page_path(cache, url))
    if not row or row.get("status") != "read":
        return None
    md = dict(row.get("meta") or {})
    host = re.sub(r"^www\.", "", urllib.parse.urlsplit(url).netloc.lower())
    title = si._site_free_title(md.get("title"), host, md.get("container"))
    # A CATALOGUE'S OWN WORDS around a title, HathiTrust's `Catalog Record:` and a
    # library's `[electronic resource]`, are not the title.
    title = re.sub(r"^Catalog Record:\s*|\s*\[electronic resource\]", "", title or "").strip() or None
    site = md.get("container") or ""
    if not title or _JUNK_TITLE.match(title) or _key(title) in (_key(site), _key(host.split(".")[0])):
        return None
    lab = parse_label(label)
    # A TITLE THAT SHARES ONLY A GENERIC WORD with the label's is another page: the
    # case `Montes Calcados` for the label `SpaceX Case Study` shares only `case`.
    content = [w for w in _words(lab["title"]) if w not in _GENERIC]
    if lab["title"] and not title_agrees(lab["title"], title) and content and \
            len(set(content) & set(_words(title))) < max(1, len(content) / 2):
        return None
    if page_names_another(md, title, lab):
        return None
    authors = []
    for p in md.get("authors") or []:
        name = p.get("name") or f"{p.get('given', '')} {p.get('family', '')}"
        if _JUNK_AUTHOR.search(name) or _key(name) in (_key(site), _key(md.get("publisher") or ""), _key(host)):
            continue
        if p.get("name") and len(p["name"].split()) == 1:
            continue
        authors.append(p)
    gov = re.search(r"\.(gov|mil|edu)$", host)
    doc_type = ("book" if md.get("og_type") == "book" else
                "proceedings-paper" if md.get("conference") else
                "journal-article" if md.get("journal") else
                "web-article" if md.get("og_type") == "article" and not gov else "web-page")
    date = md.get("date")
    if date and not (re.match(r"^\d{4}", date) and 1400 <= int(date[:4]) <= 2100):
        date = None
    # A PAGE DATED LONG AFTER THE WORK it reproduces, the National Archives' 2021 page
    # for the Emancipation Proclamation of 1863, gives the page's date, not the work's;
    # the year the article cites is the work's.
    if date and lab["year"] and int(date[:4]) > lab["year"] + 2:
        date = None
    # A BOOK SCANNED FROM A LATER PRINTING carries that printing's year; the year the
    # article cites it by is the edition it was written from.
    if doc_type == "book" and lab["year"] and date and abs(int(date[:4]) - lab["year"]) > 1:
        date = None
    where = "the page" if row.get("live") else "the Internet Archive capture"
    stamp = re.search(r"/web/(\d{8})", row.get("read_from") or "")
    return {"url": url, "status": "read", "final_url": None, "doc_type": doc_type, "title": title,
            "subtitle": None, "authors": authors, "publisher": md.get("publisher"),
            "container": md.get("conference") or md.get("journal") or site or None,
            "date": date, "modified": None, "number": None, "doi": md.get("doi"),
            "volume": md.get("volume"), "pages": md.get("pages"),
            "evidence": title[:150],
            "notes": f"Read from {where}{' nearest ' + stamp.group(1) if stamp else ''}, its own head tags only."}


_SUBTITLE_START = re.compile(r"^(The|A|An|On|How|Why|What|Its|Their|Essays|Studies|Reflections|Lessons|Notes|"
                             r"Origins|From|Toward|Towards|Aspects|Theory|Principles|History|Foundations)\b")
_PUBLISHER_WORDS = re.compile(r"Press|University|Wiley|Springer|Elsevier|Routledge|Norton|Penguin|Random House|"
                              r"Knopf|Basic Books|Harper|Macmillan|Addison|Prentice|McGraw|North-Holland|"
                              r"O'Reilly|AIAA|Academic|Books|Publishing|Publishers|Verlag|Crown|Viking|Scribner|"
                              r"Little, Brown|Simon|Doubleday|Bantam|Free Press|Belknap|Pantheon|Vintage|Holt", re.I)


# THE VENUES A200 TO A236 LABELS ABBREVIATE, written out as Chicago wants a journal's
# or a proceedings' name. Only a label-built entry needs this; a registry gives the name.
VENUE_NAMES = {
    "CACM": "Communications of the ACM", "JACM": "Journal of the ACM",
    "POPL": "Proceedings of the ACM Symposium on Principles of Programming Languages",
    "ICFP": "Proceedings of the ACM SIGPLAN International Conference on Functional Programming",
    "PLDI": "Proceedings of the ACM SIGPLAN Conference on Programming Language Design and Implementation",
    "LICS": "Proceedings of the IEEE Symposium on Logic in Computer Science",
    "ESOP": "European Symposium on Programming", "CADE": "International Conference on Automated Deduction",
    "PLPV": "Workshop on Programming Languages Meets Program Verification",
    "TYPES": "International Conference on Types for Proofs and Programs",
    "HOPL-III": "Proceedings of the Third ACM SIGPLAN Conference on History of Programming Languages",
    "ACM SIGPLAN HOPL-II": "Proceedings of the Second ACM SIGPLAN Conference on History of Programming Languages",
}
# A LABEL'S REMARK in the venue's place, `reprinted 2018` or `personal essay`, names no venue.
_REMARK = re.compile(r"^(revised|reprinted|unpublished|personal|lecture|copenhagen|marktoberdorf)\b|\blecture$", re.I)


def record_from_label(anchor, url, label, rule, read_date, why):
    """A draft record from a label written as a bibliography entry, or None for other forms.

    The A200 to A236 labels name every author with given names, the title, the
    publisher or the journal and its volume, and the year, so an unread page
    still yields a full entry. A label writes a subtitle's colon as a comma; the
    comma before a part that opens a subtitle is read as the colon.
    """
    lab = parse_label(label, anchor)
    if lab["form"] != "full" or not lab["title"] or not lab["year"]:
        return None
    parts = lab["title"].split(", ")
    title = parts[0] + "".join((": " if i == 1 and _SUBTITLE_START.match(p) else ", ") + p
                               for i, p in enumerate(parts[1:], 1))
    venue = lab["venue"]
    remark = ""
    if _REMARK.search(venue):
        remark, venue = venue, ""
    report = bool(re.search(r"Technical (Report|Note)|\bMemo\b|Research Report", venue))
    jm = None if report else re.match(r"^(.*?\D)\s+(\d+)$", venue)
    if jm and jm.group(1) in VENUE_NAMES:
        venue = f"{VENUE_NAMES[jm.group(1)]} {jm.group(2)}"
        jm = re.match(r"^(.*?\D)\s+(\d+)$", venue)
    elif re.sub(r"\s+\d{4}$", "", venue) in VENUE_NAMES:
        venue = VENUE_NAMES[re.sub(r"\s+\d{4}$", "", venue)]
    people = [dict(p) for p in lab["people"]]
    rec = {"anchor": anchor, "url": url, "title_published": title, "title": title, "year": lab["year"]}
    if rule.get("kind"):
        rec["kind"] = rule["kind"]
    elif report:
        rec["kind"] = "report"
    elif anchor.startswith("book_") or (venue and _PUBLISHER_WORDS.search(venue) and not jm):
        rec["kind"] = "book"
    elif jm and not anchor.startswith("book_"):
        rec["kind"] = "journal-article"
    elif venue and not anchor.startswith(("book_", "ref_")):
        rec["kind"] = "proceedings-paper"
    else:
        rec["kind"] = "report"
    if lab["editors"]:
        rec["editors"], rec["authors"] = people, []
    else:
        rec["authors"] = people
    if rec["kind"] == "journal-article":
        rec["container"] = rec["venue"] = jm.group(1).strip()
        rec["volume"] = jm.group(2)
    elif rec["kind"] == "proceedings-paper":
        rec["container"] = rec["venue"] = venue
    elif venue:
        rec["publisher"] = rule.get("publisher") or venue
    elif rule.get("publisher"):
        rec["publisher"] = rule["publisher"]
    rec["note"] = (f"{why}, so this entry is built from the article's label, which names its authors in full; "
                   f"the title's punctuation is the label's." + (f" The label adds `{remark}`." if remark else ""))
    return rec


def check_openlibrary_link(anchor, url, work, label, cache, rule, read_date):
    """A replacement record when a linked Open Library work is not the book the label names, else None.

    WHY. Ten hand-written work keys in A345 to A347 were checked once and nine
    named unrelated books, `Leishman, Principles of helicopter aerodynamics`
    pointing at a market report on dark rum (see `booklinks.py`). A record built
    from the wrong work would print the wrong book under the right label. The
    label is the claim, so the work must agree with it on the title, or on the
    first author where the label gives no title. The right work is then sought
    by title, and failing that the entry is built from the label.
    """
    import sources_import as si
    lab = parse_label(label, anchor)
    t = work.get("title") or ""
    fams = _ol_families(work.get("_author_names"))
    if lab["title"]:
        bad = not title_agrees(lab["title"], t)
    else:
        bad = bool(lab["people"]) and not people_agree(lab["people"], fams)
    if not bad:
        return None
    said = f"The article linked Open Library's {t!r} at {url}, which is not the work its label names"
    doc, why = book_candidate(lab, cache) if lab["title"] else (None, "")
    if doc:
        key = doc["key"].lstrip("/")
        w = _load(si.report_cache_path(cache, "openlibrary", key))
        if w:
            rec = _book_record(anchor, w, key, lab, f"https://openlibrary.org/{key}")
            rec["note"] = f"{said}; the work is Open Library's {key}, found by title, {why}."
            return rec
    rule = dict(rule, kind="book")
    rec = record_from_label(anchor, url, label, rule, read_date, said)
    if rec is None:
        rec = si.record_from_web(anchor, url, {"status": "wrong record"}, label, rule, read_date)
        rec["note"] = f"{said}, so this entry is built from the label; the title may be a description."
    return rec


UNIDENTIFIED = "[Title not identified]"


def record_without_title(anchor, url, label, read_date, why):
    """A record for a label naming authors and a year but no title, the title marked unidentified.

    WHY. Some A237 to A248 labels, `Hopkins Alonso Adcock 1965`, name a work no
    registry or search could find, and the link they give is dead. The entry keeps
    what the article claims, its authors and year, and says plainly that the title
    is not known, rather than printing a surname as a title or inventing one.
    """
    lab = parse_label(label, anchor)
    rec = {"anchor": anchor, "kind": "report", "url": url, "title_published": UNIDENTIFIED,
           "title": UNIDENTIFIED, "authors": [dict(p) for p in lab["people"]],
           "note": f"{why}, and no registry record agreeing with the label was found, so the entry gives the "
                   f"label's authors and year and marks the title as not identified."}
    if lab["year"]:
        rec["year"] = lab["year"]
    if not lab["people"]:
        rec["title"] = rec["title_published"] = lab["title"] or label or UNIDENTIFIED
    return rec


# ------------------------------------------------------------ proceedings indexes
#
# WHY. 95 of the 200 NeurIPS links and 24 of the 162 PMLR links in A250 to A265
# did not serve a paper on 2026-10-25, and several carry hashes no paper has, so
# the link itself is wrong. Their labels, `Boyan and Moore 1995`, give authors and
# a year but no title. Each proceedings publishes an index of every paper with
# its authors, NeurIPS by year and PMLR by volume, so a dead link is matched to
# the one paper in that index by exactly the label's authors.


def proceedings_index_url(url, year=None):
    """(key, index URL) for the proceedings index a NeurIPS or PMLR link belongs to, or None."""
    m = re.search(r"proceedings\.mlr\.press/(v\d+)/", url)
    if m:
        return f"pmlr_{m.group(1)}", f"https://proceedings.mlr.press/{m.group(1)}/"
    m = re.search(r"(?:papers\.nips\.cc|proceedings\.neurips\.cc)/paper(?:_files/paper)?/(\d{4})/", url)
    y = int(m.group(1)) if m else year
    if m or ("nips.cc" in url or "neurips.cc" in url) and y:
        return f"neurips_{y}", f"https://papers.nips.cc/paper_files/paper/{y}"
    return None


def parse_proceedings_index(key, text):
    """[{title, authors, url, container}] from a NeurIPS or PMLR index page."""
    import html
    out = []
    if key.startswith("neurips_"):
        for href, title, who in re.findall(r'<a title="paper title" href="([^"]+)">([^<]+)</a>\s*'
                                           r'<span class="paper-authors">([^<]*)</span>', text):
            out.append({"title": html.unescape(title).strip(), "authors": html.unescape(who).split(", "),
                        "url": "https://papers.nips.cc" + href,
                        "container": "Advances in Neural Information Processing Systems"})
    else:
        for block in text.split('<div class="paper">')[1:]:
            t = re.search(r'<p class="title">(.*?)</p>', block, re.S)
            w = re.search(r'<span class="authors">(.*?)</span>', block, re.S)
            c = re.search(r'<span class="info"><i>(.*?)</i>', block, re.S)
            u = re.search(r'<a href="(https?://proceedings\.mlr\.press/[^"]+\.html)">abs</a>', block)
            if t and w and u:
                who = html.unescape(re.sub(r"<[^>]+>", "", w.group(1))).replace("\xa0", " ")
                out.append({"title": html.unescape(re.sub(r"\s+", " ", t.group(1))).strip(),
                            "authors": [x.strip() for x in who.split(",") if x.strip()],
                            "url": u.group(1).replace("http://", "https://"),
                            "container": html.unescape(c.group(1)).strip() if c else "Proceedings of Machine Learning Research"})
    return out


def fetch_proceedings_indexes(keys_urls, cache):
    """Cache each proceedings index, parsed, one file per year or volume."""
    import fetch
    got = miss = failed = 0
    for key, url in dict(keys_urls).items():           # bound: one request an index
        path = cache_path(cache, "proceedings", key)
        if _settled(path):
            continue
        body, status = fetch.get_bytes_status(url, tries=2)
        if body is None:
            if status == 404:
                open(path + ".missing", "w").close()
                miss += 1
            else:
                failed += 1
            continue
        _save(path, {"url": url, "papers": parse_proceedings_index(key, body.decode("utf-8", "replace"))})
        got += 1
    return got, miss, failed


def proceedings_match(url, lab, cache):
    """(paper, why) for the one paper in the link's proceedings index by exactly the label's authors.

    The label's year and the year before are both searched for NeurIPS, whose
    index files a volume under the year of the conference, published the next
    year. A label with `et al` matches on its first author only, so it must be
    unique among the papers of that index by that first author.
    """
    import sources_import as si
    if not lab["people"] or not lab["year"]:
        return None, "the label names no authors and year"
    fams = [_fold(p.get("family") or "") for p in lab["people"]]
    keys = []
    first = proceedings_index_url(url, lab["year"])
    if first:
        keys.append(first[0])
        if first[0].startswith("neurips_"):
            keys = [f"neurips_{lab['year']}", f"neurips_{lab['year'] - 1}"]
    hits = []
    for key in dict.fromkeys(keys):
        idx = _load(cache_path(cache, "proceedings", key))
        for paper in (idx or {}).get("papers", []):
            pf = [_fold((si._person(n) or {}).get("family", "")) for n in paper["authors"]]
            if not pf or pf[0] != fams[0]:
                continue
            exact = len(fams) > 1 and len(pf) == len(fams) and all(f in pf for f in fams)
            if exact or (len(fams) == 1 and (lab.get("incomplete") or len(pf) <= 2)):
                hits.append(dict(paper, index=key))
    if lab["title"]:
        hits = [h for h in hits if title_agrees(lab["title"], h["title"])] or hits
    if len(hits) == 1:
        return hits[0], f"the one paper in {hits[0]['index'].replace('_', ' ')} by the label's authors"
    return None, f"{len(hits)} papers in the index match the label's authors"


def record_from_proceedings(anchor, paper, lab):
    """A proceedings paper from a parsed index entry."""
    import sources_import as si
    people = [p for p in (si._person(n) for n in paper["authors"]) if p]
    title = sources.clean_text(paper["title"])
    rec = {"anchor": anchor, "kind": "proceedings-paper", "url": paper["url"], "title_published": title,
           "title": si.headline_case(title), "authors": si._authors(people), "year": lab["year"],
           "container": paper["container"], "venue": paper["container"]}
    if paper["index"].startswith("neurips_") and paper["index"] != f"neurips_{lab['year']}":
        rec["note"] = (f"NeurIPS files the paper under {paper['index'][8:]}, the year of the conference; "
                       f"{lab['year']} is the year the article cites it by.")
    return rec


def wrong_link(url, label, anchor, cache, crossref_cache):
    """What a link's own identifier names, (title, first author), when it is plainly another work, else None.

    WHY. A250 to A265 link arXiv numbers and DOIs that name unrelated papers:
    `Barreto et al 2019` links a paper on moduli stabilisation in string theory.
    A record that disagrees with the label on both the title and the authors is
    another work, so the entry must not send its reader there. A record that
    disagrees only on the year is not called wrong.
    """
    import sources_import as si
    lab = search_label(label, anchor)
    ident = url_identifier(url)
    if not lab["people"]:
        return None
    page = _load(page_path(cache, url))
    md = (page or {}).get("meta") or {}
    if (page or {}).get("status") == "read" and md.get("title") and page_names_another(md, md["title"], lab):
        who = md["authors"][0]
        return sources.clean_text(md["title"]), who.get("family") or who.get("name")
    if not ident:
        return None
    kind, value = ident
    title, fams = None, []
    if kind == "arxiv" or kind == "doi" and not os.path.exists(si.crossref_cache_path(crossref_cache, value)):
        d = _load(cache_path(cache, "datacite", arxiv_doi(value) if kind == "arxiv" else value))
        if d:
            title = ((d.get("titles") or [{}])[0]).get("title", "")
            fams = [c.get("familyName") or c.get("name") or "" for c in d.get("creators") or []]
    elif kind == "doi":
        msg = _load(si.crossref_cache_path(crossref_cache, value))
        title, fams = (msg.get("title") or [""])[0], _crossref_families(msg)
    elif kind == "pii":
        msg = _load(cache_path(cache, "pii", value))
        if msg:
            title, fams = (msg.get("title") or [""])[0], _crossref_families(msg)
    if title is None:
        return None
    t_ok = bool(lab["title"]) and title_agrees(lab["title"], title)
    if t_ok or people_agree(lab["people"], fams) or not fams:
        return None
    return sources.clean_text(title), fams[0]


def search_url(lab, book=False):
    """A search for a work by its label, for an entry whose own link is wrong or names no document."""
    q = urllib.parse.quote_plus(" ".join(x for x in [lab["title"] if not lab.get("hinted") else "",
                                                     " ".join(p.get("family", "") for p in lab["people"][:3]),
                                                     str(lab["year"] or "")] if x))
    return f"https://openlibrary.org/search?q={q}" if book else f"https://scholar.google.com/scholar?q={q}"


def fetch_works_light(works, cache, docs, by_key=False):
    """Cache a work found by search with one request, its editions, beside the search's own fields.

    WHY. `fetch-reports openlibrary` asks for a work, its editions and each author,
    four requests a book, and Open Library answered slowly at that volume. A search
    result already gives the title and the authors' full names, so for a work found
    by search only the editions, which carry the publishers, are asked for. The
    file has the shape `record_from_openlibrary` reads.
    """
    import fetch
    import sources_import as si
    got = miss = failed = 0
    for w in works:                                    # bound: two requests a work
        path = si.report_cache_path(cache, "openlibrary", w)
        if any(os.path.exists(path + m) for m in ("", ".missing", ".unreadable")):
            continue
        if w not in docs and by_key:
            # A WORK FOUND BY ISBN has no search result yet; the search index gives
            # its title and authors' names by its key in one request.
            q = urllib.parse.urlencode({"q": f"key:/{w}", "fields": "key,title,subtitle,author_name"})
            j = fetch.get_json(f"https://openlibrary.org/search.json?{q}")
            hit = [d for d in (j or {}).get("docs") or [] if d.get("key") == "/" + w]
            if hit:
                docs[w] = hit[0]
        if w not in docs:
            continue
        j, status = fetch.get_json_status(f"https://openlibrary.org/{w}/editions.json?limit=50")
        if j is None and status != 404:
            failed += 1
            continue
        doc = docs[w]
        _save(path, {"key": "/" + w, "title": doc.get("title"), "subtitle": doc.get("subtitle"),
                     "_author_names": doc.get("author_name") or [], "_editions": (j or {}).get("entries") or [],
                     "_via": "search result and editions"})
        got += 1
    return got, miss, failed


def article_labels(text):
    """({anchor: label}, {anchor: fuller label}) for a legacy article, every source it names.

    The reference list's items come first, those written title first rewritten in
    the bibliography form. A source cited only in the prose, as A262's `Gallup
    1970`, takes the prose's label. Where the prose names more authors than the
    list, `Engstrom et al 2020` against all seven, the prose's label is the fuller
    one, which a search by authors and an entry built from a label use.
    """
    import sources_import as si
    # LIQUID IN A LABEL, `{% raw %}[Ion-dtn-users]{% endraw %}` in A16, kept brackets from
    # being read as a link; it is markup, not the title, and escaped it breaks the build.
    unliquid = lambda x: re.sub(r"\{%-?\s*(?:raw|endraw)\s*-?%\}", "", x)  # noqa: E731
    labels = {anc: unliquid(lab) for lab, anc in si.LEGACY_ITEM.findall(text)}
    for anc, lab in title_first_labels(text).items():
        labels.setdefault(anc, unliquid(lab))
    fuller = {}
    for lab, anc in sources.USE_RE.findall(text.split("\n## References\n")[0]):
        lab = lab.replace("*", "").replace("\n", " ")
        labels.setdefault(anc, lab)
        n = len(parse_label(lab, anc)["people"])
        if n > len(parse_label(fuller.get(anc, labels[anc]), anc)["people"]):
            fuller[anc] = lab
    return labels, fuller


def author_query(lab):
    """The DataCite search for an arXiv record by every family the label names and its year."""
    fams = [p["family"] for p in lab["people"] if p.get("family")][:5]
    q = " AND ".join(f'creators.familyName:"{f}"' for f in fams)
    return f"{q} AND publicationYear:[{lab['year'] - 1} TO {lab['year']}]"


def fetch_author_searches(labs, cache):
    """Search DataCite's arXiv records by a label's authors and year, caching each raw answer."""
    import fetch
    got = failed = 0
    for lab in labs:                                   # bound: one request a label
        q = author_query(lab)
        path = query_path(cache, "datacite", q)
        if os.path.exists(path):
            continue
        params = {"query": q, "client-id": "arxiv.content", "page[size]": "25"}
        j = fetch.get_json(f"https://api.datacite.org/dois?{urllib.parse.urlencode(params)}")
        if j is None:
            failed += 1
            continue
        _save(path, {"query": q, "data": [x.get("attributes") for x in j.get("data") or []]})
        got += 1
    return got, 0, failed


def author_match(lab, cache):
    """(DataCite attributes, why) for the one arXiv record by exactly the label's authors, or None.

    Only a label naming two or more people is searched this way, and the record
    must name the same first author and the same set of authors, so that a paper
    by a team with a frequent co-author is not taken for another.
    """
    fams = [_fold(p.get("family") or "") for p in lab["people"]]
    if len(fams) < 2 or lab.get("incomplete"):
        return None, "the label does not name every author"
    res = _load(query_path(cache, "datacite", author_query(lab)))
    hits = []
    for a in (res or {}).get("data", []):
        cf = [_fold(c.get("familyName") or c.get("name") or "") for c in a.get("creators") or []]
        if cf and cf[0] == fams[0] and sorted(cf) == sorted(fams):
            hits.append(a)
    if len(hits) == 1:
        return hits[0], "the one arXiv record by exactly the label's authors in its year"
    return None, f"{len(hits)} arXiv records by exactly the label's authors"


def page_names_another(md, title, lab):
    """Whether a page's own metadata names a different work from the label's.

    WHY. A240 to A267 link pages whose metadata is plainly another paper:
    `Forrester 1948` links an MIT repository record of a 2016 thesis on PhoQ-PhoP
    kinetics, and `Alon et al 2013` a NeurIPS paper on firing-rate predictions. A
    label with no title gave nothing to compare, so the page's authors are
    compared: a page naming authors, none of them the label's first, and no
    agreeing title, is another work.
    """
    import sources_import as si
    if not lab["people"]:
        return False
    fams = [(p.get("family") or p.get("name") or "") for p in md.get("authors") or []]
    if not fams:
        return False
    if lab["title"] and title_agrees(lab["title"], title or ""):
        return False
    return not people_agree(lab["people"], fams)


# ------------------------------------------------------------ legacy posts


def post_paths(posts_dir="_posts"):
    """({site path: post stem}, {slug: [stems]}) for every post, for links to this blog by URL."""
    import glob
    paths, slugs = {}, {}
    for f in glob.glob(os.path.join(posts_dir, "*.markdown")):            # bound: one post a file
        text = open(f, encoding="utf-8").read()
        m = re.search(r"(?m)^categories:\s*(.*)$", text)
        cats = m.group(1).split() if m else []
        stem = os.path.basename(f)[:-9]
        paths["/" + "/".join(cats + [stem[:4], stem[5:7], stem[8:10], stem[11:] + ".html"])] = stem
        slugs.setdefault(stem[11:], []).append(stem)
    return paths, slugs


def normalise_legacy(text, paths=None, slugs=None):
    """(text, [changes]) with a legacy post made readable to the converter. Nothing a reader sees changes.

    - `## References:` and `## Links:` become `## References`.
    - An inline list item, `- [Title](URL)`, becomes a reference-style link.
    - An anchor with hyphens or capitals, `android-asm-github`, is lower-cased with underscores
      in its definition and every use; kramdown matches names without regard to case.
    - A link to this blog's own post by URL becomes `post_url`, matched by the post's path or,
      where the URL's date differs by the time zone, by a slug only one post has.
    """
    notes = []
    text, n = re.subn(r"(?m)^## (?:References|Links):\s*$", "## References", text)
    if n:
        notes.append("heading")
    # A DEFINITION'S SPACING, `[name]:    URL` aligned by hand, is one space, as the
    # converter reads definitions and as kramdown renders either.
    text, n = re.subn(r"(?m)^(\[[^\]]+\]:)[ \t]{2,}(\S)", r"\1 \2", text)
    if n:
        notes.append(f"spacing x{n}")
    m = re.search(r"(?m)^## References\s*$", text)
    if m:
        head, refs = text[:m.end()], text[m.end():]
        defs = []

        def item(mm):
            label, url = mm.group(1), mm.group(2)
            slug = "ref_" + re.sub(r"_+", "_", re.sub(r"[^a-z0-9]+", "_", label.lower())).strip("_")[:50]
            defs.append(f"[{slug}]: {url}")
            return f"- [{label}][{slug}]"
        refs2 = re.sub(r"(?m)^- \[([^\]]+)\]\((https?://[^)\s]+)\)\s*$", item, refs)
        if defs:
            refs2 = refs2.rstrip("\n") + "\n\n" + "\n".join(defs) + "\n"
            notes.append(f"{len(defs)} inline items")
        text = head + refs2
    defs = re.findall(r"(?m)^\[([^\]]+)\]:[ \t]*\S", text)
    taken = set(defs)
    for a in defs:                                     # bound: one pass a definition
        if re.fullmatch(r"[a-z0-9_]+", a):
            continue
        new = re.sub(r"_+", "_", re.sub(r"[^a-z0-9]+", "_", a.lower())).strip("_")
        while new in taken:                            # bound: each pass lengthens the name
            new += "_x"
        taken.add(new)
        text = re.sub(r"(?mi)^\[" + re.escape(a) + r"\]:", f"[{new}]:", text)
        text = re.sub(r"(?i)\]\[" + re.escape(a) + r"\]", f"][{new}]", text)
        notes.append(f"{a} -> {new}")
    if paths is not None:
        def own(mm):
            path, frag = mm.group(2), mm.group(3) or ""
            stem = paths.get(path)
            cand = (slugs or {}).get(path.rsplit("/", 1)[-1][:-5], [])
            if not stem and len(cand) == 1:
                stem = cand[0]
            if not stem:
                return mm.group(0)
            notes.append(f"{path} -> post_url {stem}")
            return f"{mm.group(1)} {{% post_url {stem} %}}{frag}"
        text = re.sub(r"(?m)^(\[[a-z0-9_]+\]:)[ \t]+(?:https?://sgeos\.github\.io)?(/[^\s#]+\.html)(#\S+)?[ \t]*$",
                      own, text)
    return text, notes


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
