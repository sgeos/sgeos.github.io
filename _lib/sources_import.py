#!/usr/bin/env python3
"""Draft source records from registry metadata, for review before they enter the database.

WHAT THIS DOES NOT DECIDE. It proposes a record. It does not decide whether a
journal article is a review, whether a publisher has a stake in its subject, or
whether a venue referees full papers, because no registry answers those. The
caller records those decisions on the record or in `_sources/venues.jsonl`, and
`sources.validate` refuses a record whose recorded section the rules do not
reproduce.

HEADLINE CASE IS A PROPOSAL. Registries mostly store titles in sentence case,
and Chicago wants headline case. `headline_case` capitalises what is lower case
and leaves alone anything already carrying a capital or a digit, so it cannot
damage an acronym or a proper noun, but it cannot know that `km` is a unit or
that `up` is an adverb. Every proposed title is reviewed by a person.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sources  # noqa: E402

# Chicago lowercases articles, coordinating conjunctions, `to`, `as`, and
# prepositions regardless of length, except as the first or last word of a
# title or subtitle.
MINOR = set("""
a an the and but for or nor as to
about above across after against along amid among around at before behind below beneath beside
between beyond by down during except from in inside into like near of off on onto out outside over
past per since than through throughout till toward towards under underneath until unto up upon via
versus vs with within without aboard atop despite unlike amidst
""".split())


def _case_part(part, force):
    """One hyphen-separated part. Existing capitals and digits are never removed."""
    lead = re.match(r"^[^\w]*", part).group(0)
    rest = part[len(lead):]
    # A WORD THAT DOES NOT START WITH A LATIN LETTER IS A SYMBOL, such as the α of
    # `α Centauri`, whose capital Α is a different letter that reads as A.
    if rest and not ("a" <= rest[:1].lower() <= "z"):
        return part
    # A LONE LOWER-CASE LETTER OTHER THAN `a` IS A SYMBOL TOO, the q of `Tobin's q`.
    if len(re.sub(r"[^\w]", "", rest)) == 1 and rest[:1].islower() and rest[:1] != "a":
        return part
    bare = re.sub(r"[^\w'\u2019]+$", "", rest)
    # A minor word the registry capitalised, as in "Has A Solid", is lowered.
    # Only the plain capitalised form is touched, so an acronym is never lowered.
    if not force and bare.lower() in MINOR and bare == bare[:1].upper() + bare[1:].lower():
        return lead + rest.lower()
    if not rest or rest[:1].isupper() or re.search(r"[A-Z0-9]", rest):
        return part
    if bare.lower() in MINOR and not force:
        return lead + rest.lower()
    return lead + rest[:1].upper() + rest[1:]


def _case_word(word, force):
    """Chicago 8.161 for compounds. The first part follows the word's position,
    later parts are capitalised unless they are minor words.

    A LATER PART THE REGISTRY CAPITALISED IS KEPT. In `Spin-Off` the second part is
    a particle of the compound, not a preposition, and Chicago capitalises it, so
    lowering a registry capital there would be wrong. A lower-case later part that
    is a minor word stays lower case, as in `Out-of-Pocket`.
    """
    # AN EM DASH JOINS TWO WORDS WITHOUT A SPACE, `technology—A`, so each side is
    # cased as a word of its own. Unlike a colon, a dash does not open a subtitle,
    # so a minor word after it stays lower case, as in `Power—and That's`. Chicago
    # 8.159 forces a capital only first, last and after a colon, so `Technology—a
    # State` is deliberate even where the registry capitalised the article.
    if "\u2014" in word:
        left, right = word.split("\u2014", 1)
        return _case_word(left, force) + "\u2014" + _case_word(right, False)
    parts = word.split("-")
    out = []
    for i, p in enumerate(parts):
        if i and p[:1].isupper():
            out.append(p)
        else:
            out.append(_case_part(p, force if i == 0 else False))
    return "-".join(out)


_TEX_SYMBOLS = {"alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "epsilon": "ε", "lambda": "λ", "mu": "µ",
                "pi": "π", "sigma": "σ", "tau": "τ", "phi": "φ", "omega": "ω", "Delta": "Δ", "Omega": "Ω",
                "sharp": "♯", "pm": "±", "times": "×", "infty": "∞", "leq": "≤", "geq": "≥", "to": "→",
                "rightarrow": "→", "cdot": "·", "ell": "ℓ"}


def tex_to_text(title):
    """A registry title's inline TeX as plain text, `$\\mathbb{Z}_p$` as `Zp`.

    WHY. Forty harvested titles carried TeX, which an entry must escape and a
    reader then sees as markup, and which headline casing corrupted, `\\Mu` for
    `\\mu`. Only a `$...$` span holding TeX is converted, so a price such as
    `$2.6tn` is left alone. Text arguments are kept, Greek and common symbols
    become their characters, subscripts are written inline, `Al2O3`, and a
    superscript keeps a caret unless it is a sign, `SPHINCS+`.
    """
    def convert(m):
        t = m.group(1)
        if not re.search(r"[\\^_{}]", t):
            return m.group(0)
        t = re.sub(r"\\(?:text|hbox|mathrm|mathbb|mathcal|mathit|mathbf|operatorname|textrm)\s*\{([^{}]*)\}", r"\1", t)
        t = re.sub(r"\\([A-Za-z]+)", lambda x: _TEX_SYMBOLS.get(x.group(1), _TEX_SYMBOLS.get(x.group(1).lower(), x.group(1))), t)
        t = re.sub(r"\\[!,;: ]", "", t)
        t = re.sub(r"\\([\[\]])", r"\1", t)
        t = re.sub(r"_\{([^{}]*)\}|_(\w)", lambda x: x.group(1) or x.group(2), t)
        t = re.sub(r"\^\{([^{}]*)\}|\^(\S)", lambda x: (lambda c: c if c in "+-*#♯†" else "^" + c)(x.group(1) or x.group(2)), t)
        return t.replace("{", "").replace("}", "").strip()
    out = re.sub(r"\$\$?([^$]+?)\$\$?", convert, title)
    return re.sub(r"\s+", " ", out).strip()


def normalise_title(title):
    """Registry punctuation repaired before casing. A typed spaced hyphen
    separating a subtitle becomes a colon, and a trailing period is dropped,
    since the entry supplies its own. House rules, see CITATION_STYLE.md."""
    title = tex_to_text(title)
    title = re.sub(r"\s+-\s+", ": ", title.strip())
    # AIAA's SGML entity for a question mark survives in some deposits, as in
    # Edelbaum's `How many impulses/ques/`.
    title = title.replace("/ques/", "?")
    # A trailing footnote mark from the publisher's typesetting is not the title.
    # Marks set as separate superscripts arrive spaced apart, as in Prsa et al.'s
    # `B3 * \u2020`, so each is removed with the space before it.
    title = re.sub(r"(?:\s*[*\u2217\u2020\u2021\u2606\u2605])+$", "", title)
    return re.sub(r"(?<![A-Z])\.$", "", title)


def headline_case(title):
    """A proposed Chicago headline-case title. Review every result."""
    title = normalise_title(title)
    words = title.split(" ")
    if len(words) >= 3 and title.isupper():
        # A word holding a digit is a designation, as in `Resolution B3`, and keeps
        # its capitals. An acronym such as `IAU` cannot be told from a word here and
        # needs a title decision.
        words = [w if re.search(r"\d", w) else w.lower() for w in words]
    out = []
    for i, w in enumerate(words):
        first = i == 0 or words[i - 1].endswith((":", "?", "!", "\u2014"))
        last = i == len(words) - 1 or w.endswith(":")
        out.append(_case_word(w, first or last))
    return " ".join(out)


def _given(g):
    """Given names as printed, with Chicago's spaced initials, as in `A. J.`."""
    g = sources.clean_text(g)
    # A NAME IN CAPITALS IS RECASED word by word, so `JAMES K.` becomes `James K.`;
    # an initial is a single capital and is left alone.
    g = re.sub(r"\b([A-Z])([A-Z]+)\b", lambda m: m.group(1) + m.group(2).lower(), g)
    g = re.sub(r"\.(?=[A-Z])", ". ", g)
    return re.sub(r"\b([A-Z])(?=\s|$)", r"\1.", g)


def _family(f):
    """Family names as printed. A generational suffix takes no comma in the 18th edition."""
    f = sources.clean_text(f)
    # A footnote mark and a typographic apostrophe are typesetting, not the name:
    # `Azuma*` is Azuma, and `O’Brien` is written as the articles write it, `O'Brien`.
    f = re.sub(r"[*\u2217\u2020\u2021,;]+$", "", f).replace("\u2019", "'")
    # A FAMILY NAME IN CAPITALS, `KIM` or `DU`, is recased; a two-letter one too.
    if f.isupper() and len(re.sub(r"[^A-Z]", "", f)) >= 2:
        f = re.sub(r"[A-Z]+", lambda m: m.group(0)[0] + m.group(0)[1:].lower(), f)
    # AIAA deposits an apostrophe as a caret, `O^Neill`, a typesetting code.
    f = f.replace("^", "'")
    return re.sub(r",\s*(Jr\.|Sr\.|II|III|IV)$", r" \1", f)


# AN AFFILIATION DEPOSITED AS AN AUTHOR, `Department of Environmental Engineering,
# Daejeon University`, is not a person and is dropped, as A377's harvested records
# showed at scale. A real organisational author, such as a committee, survives
# unless it carries one of these words.
# The closing check is a lookahead, not \b, because `Inc.` ends in a full stop and a
# word boundary after a full stop at the end of the name never matches.
_AFFILIATION = re.compile(r"\b(Department|Dept\.|University|Universit[äa]t|Faculty|School of|Laborator(y|ies)|"
                          r"Hospital|College|Institute of|Institut|Centre for|Center for|Ph\.D\.|MBA|"
                          r"Inc\.|Ltd\.?|GmbH|S\.A\.|Corporation|Conservatory|Magazine|Academy of)(?!\w)", re.I)
# A BYLINE THAT NAMES NO ONE is no author: the work is then listed under its title.
_NO_ONE = re.compile(r"^(A|Our|Special|From Our|By a) Correspondents?$|^Anonymous$|^Anon\.?$", re.I)


def _authors(people):
    out = []
    has_person = any(p.get("family") for p in people or [])
    for p in people or []:
        name = p.get("name") or ""
        if not p.get("family") and name and _NO_ONE.match(name.strip()):
            continue
        # An affiliation is dropped when people are also named; a record whose only
        # author is an organisation keeps it, unless it is plainly a department.
        if not p.get("family") and name and _AFFILIATION.search(name) and (
                has_person or re.search(r"\bDepartment\b|\bFaculty\b|\bDept\.", name)):
            continue
        if p.get("family"):
            a = {"family": _family(p["family"])}
            if p.get("given"):
                a["given"] = _given(p["given"])
            out.append(a)
        elif p.get("name"):
            out.append({"name": sources.clean_text(p["name"])})
    return out


def _strip_the(container):
    """Chicago drops an initial `The` from a periodical's name, as in *American Naturalist*."""
    return re.sub(r"^The\s+", "", container)


# Every Crossref type the corpus uses, so an import never stops on an unmapped one.
# A reference entry is an encyclopaedia or dictionary entry, so it is marked as
# one and goes to Tertiary Sources under rule 2.
CROSSREF_KIND = {
    "journal-article": "journal-article",
    "proceedings-article": "proceedings-paper",
    "book-chapter": "chapter", "book-part": "chapter", "book-section": "chapter",
    "reference-entry": "chapter",
    "book": "book", "edited-book": "book", "monograph": "book", "reference-book": "book",
    "book-set": "book", "book-series": "book", "proceedings": "book",
    "report": "report", "report-component": "report", "report-series": "report",
    "dissertation": "thesis", "dataset": "dataset", "database": "dataset", "standard": "standard",
    "component": "other", "other": "other", "peer-review": "other", "journal-issue": "other",
    "journal-volume": "other", "journal": "other", "grant": "other",
}


SPRINGER_CS_SERIES = {
    "Lecture Notes in Computer Science", "Lecture Notes in Artificial Intelligence",
    "Lecture Notes in Bioinformatics", "Communications in Computer and Information Science",
    "IFIP Advances in Information and Communication Technology",
    "Lecture Notes of the Institute for Computer Sciences, Social Informatics and Telecommunications Engineering",
    "Lecture Notes in Business Information Processing",
}


def _fallback_year(msg):
    """A year for a record Crossref deposited without an issued date, as for ICSE 2001.

    The meeting's start date is tried, then a year in the container title, which
    for a proceedings usually names its meeting, `ICSE 2001`.
    """
    ev = ((msg.get("event") or {}).get("start") or {}).get("date-parts") or [[None]]
    if (ev[0] or [None])[0]:
        return ev[0][0]
    for t in msg.get("container-title") or []:
        m = re.search(r"\b(19[5-9]\d|20[0-4]\d)\b", t)
        if m:
            return int(m.group(1))
    return None


def record_from_crossref(anchor, msg, cited_doi=None):
    """A draft record from a Crossref `message`. Raises on a type with no mapping.

    THE DOI THE ARTICLE CITES IS KEPT. Crossref answers a request for an alias
    DOI with the record of its primary one, so `10.1109/dac.2006.229229` came back
    as `10.1145/1146909.1147106`. Taking the returned DOI silently changed what the
    article links to, so the cited DOI stays and the primary is kept beside it.
    """
    doi = (cited_doi or msg["DOI"]).lower()
    ctype = msg.get("type")
    # A record with no type at all, as SAGE deposits for some videos, is `other`.
    kind = CROSSREF_KIND.get(ctype) if ctype else "other"
    number = None
    container = sources.clean_text(((msg.get("container-title") or [""]) or [""])[0])
    # EGU General Assembly abstracts are `posted-content` with no meeting name;
    # the DOI carries both the year and the abstract number.
    m = re.match(r"^10\.5194/egusphere-egu(\d\d)-(\d+)$", doi)
    if ctype == "posted-content" and m:
        kind = "abstract"
        number = f"EGU{m.group(1)}-{m.group(2)}"
        container = f"EGU General Assembly 20{m.group(1)}"
    elif ctype == "posted-content":
        kind = "preprint"
        container = sources.clean_text((msg.get("institution") or [{}])[0].get("name", "")) or container
    if not kind:
        raise sources.SourceError(f"{anchor}: Crossref type {ctype!r} has no mapping")
    m = re.match(r"^10\.2514/6\.(\d{4}-\d+)$", doi)
    if m:
        number = f"AIAA {m.group(1)}"
    # THE YEAR OF FIRST PUBLICATION, Crossref's `issued`, which for an article
    # posted online before its issue is the online year. A House rule, chosen over
    # the issue year so that a work's year agrees across the corpus: the harvested
    # survey lists in A369 to A377 and the legacy labels were all written with it,
    # and using the issue year disagreed with them for about one work in twenty.
    issued = (msg.get("issued", {}) or {}).get("date-parts") or [[None]]
    rec = {
        "anchor": anchor,
        "kind": kind,
        "doi": doi,
        **({"doi_primary": msg["DOI"].lower()} if msg["DOI"].lower() != doi else {}),
        "title_published": sources.clean_text((msg.get("title") or [""])[0]),
        "authors": _authors(msg.get("author")),
        "year": (issued[0] or [None])[0] or _fallback_year(msg),
        "publisher": sources.clean_text(msg.get("publisher", "")),
    }
    subtitle = sources.clean_text((msg.get("subtitle") or [""])[0])
    if subtitle and subtitle.lower() not in rec["title_published"].lower():
        rec["title_published"] += ": " + subtitle
    # A TITLE IN ANOTHER LANGUAGE keeps that language's capitalisation, Chicago
    # 11.6, so a German noun keeps its capital and nothing else gains one. Only a
    # registry that states the language is believed; an unstated one is English.
    lang = (msg.get("language") or "en").lower()
    rec["title"] = headline_case(rec["title_published"]) if lang.startswith("en") \
        else normalise_title(rec["title_published"])
    # AN ALL-CAPITALS CONTAINER IS A REGISTRY HABIT, not the journal's name, as
    # with TRANSACTIONS OF THE JAPAN SOCIETY FOR AERONAUTICAL AND SPACE SCIENCES.
    # It is recased as a proposal, and acronyms of five letters or fewer are kept.
    if len(container) > 12 and container.isupper():
        container = " ".join(w if len(w) <= 4 and w.isalpha() and w not in MINOR_UPPER else w.lower()
                             for w in container.split())
        container = headline_case(container)
    if kind == "journal-article":
        rec["container"] = _strip_the(container)
        rec["venue"] = rec["container"]
        for k_src, k_dst in (("volume", "volume"), ("issue", "issue")):
            if msg.get(k_src):
                rec[k_dst] = sources.clean_text(msg[k_src])
        if msg.get("page"):
            rec["pages"] = sources.clean_text(msg["page"])
        elif msg.get("article-number"):
            rec["pages"] = sources.clean_text(msg["article-number"])
        rec.pop("publisher")
        if msg.get("publisher"):
            rec["publisher_registry"] = sources.clean_text(msg["publisher"])
    elif kind == "thesis":
        inst = ((msg.get("institution") or [{}])[0] or {}).get("name") or msg.get("publisher") or ""
        rec["container"] = sources.clean_text(inst)
        rec.pop("publisher", None)
    elif kind in ("dataset", "standard", "other", "report") and not rec.get("publisher"):
        rec.pop("publisher", None)
    elif kind == "book" and not rec["authors"] and msg.get("editor"):
        rec["editors"] = _authors(msg["editor"])
    elif kind in ("proceedings-paper", "chapter", "abstract", "preprint"):
        rec["container"] = container
        if kind == "proceedings-paper":
            rec["venue"] = container
            if msg.get("volume"):
                rec["volume"] = sources.clean_text(msg["volume"])
        if msg.get("editor"):
            rec["editors"] = _authors(msg["editor"])
    if number:
        rec["number"] = number
    if ctype == "reference-entry":
        rec["encyclopaedia"] = True
    # A PAPER IN A SPRINGER COMPUTER-SCIENCE PROCEEDINGS SERIES is typed book-chapter
    # by Crossref. It is a proceedings paper, and its series is the venue, because
    # the series is what Springer's refereeing rule for volume editors governs.
    # Crossref lists the series and the volume title in either order.
    titles = [sources.clean_text(t) for t in (msg.get("container-title") or [])]
    hit = next((t for t in titles if t in SPRINGER_CS_SERIES), None)
    if kind == "chapter" and hit:
        rec["kind"] = "proceedings-paper"
        rec["venue"] = hit
        rec["container"] = next((t for t in titles if t != hit), hit)
    if kind == "chapter" and not rec.get("container"):
        rec["container"] = container or rec.get("publisher", "")
    return rec


def _openalex_person(a):
    """{family, given} from an OpenAlex authorship, preferring the raw `Family, Given` form."""
    raw = (a.get("raw_author_name") or "").strip()
    if "," in raw:
        fam, giv = [x.strip() for x in raw.split(",", 1)]
        return {"family": _family(fam), "given": _given(giv)} if giv else {"family": _family(fam)}
    name = ((a.get("author") or {}).get("display_name") or raw).strip()
    parts = name.split()
    if len(parts) < 2:
        return {"name": sources.clean_text(name)}
    return {"family": _family(parts[-1]), "given": _given(" ".join(parts[:-1]))}


OPENALEX_SOURCE_KIND = {"journal": "journal-article", "conference": "proceedings-paper",
                        "repository": "preprint", "book series": "chapter", "ebook platform": "book"}


def record_from_openalex(anchor, work, doi):
    """A draft record from OpenAlex, for a DOI Crossref does not hold.

    WHY. DataCite registers some DOIs, LIPIcs among them, and DataCite's host is
    outside the hosts this project reads. OpenAlex indexes DataCite works. It
    may merge a paper with its preprint, so the location whose landing page
    carries this DOI is preferred, and the record says where it came from.
    """
    doi = doi.lower()
    locs = work.get("locations") or []
    loc = next((l for l in locs if doi in (l.get("landing_page_url") or "").lower()), None) \
        or work.get("primary_location") or {}
    src = loc.get("source") or {}
    kind = OPENALEX_SOURCE_KIND.get(src.get("type"), "other")
    b = work.get("biblio") or {}
    rec = {"anchor": anchor, "kind": kind, "doi": doi,
           "title_published": sources.clean_text(work.get("title") or ""),
           "authors": [_openalex_person(a) for a in work.get("authorships") or []],
           "year": work.get("publication_year"),
           "note": "Not held by Crossref; metadata from OpenAlex."}
    rec["title"] = headline_case(rec["title_published"])
    name = sources.clean_text(src.get("display_name") or "")
    if kind in ("journal-article", "proceedings-paper", "chapter", "preprint"):
        rec["container"] = _strip_the(name) if kind == "journal-article" else name
        if kind in ("journal-article", "proceedings-paper"):
            rec["venue"] = rec["container"]
    elif name:
        rec["publisher"] = name
    if b.get("volume"):
        rec["volume"] = str(b["volume"])
    if b.get("issue"):
        rec["issue"] = str(b["issue"])
    if b.get("first_page"):
        rec["pages"] = str(b["first_page"]) + (f"-{b['last_page']}" if b.get("last_page") else "")
    return rec


# ------------------------------------------------------------ web sources
#
# WHY. A source with no DOI, no Wikipedia page and no post has no registry record
# this project can read, and the article's legacy label holds only surnames and,
# often, a description in place of the title. Its page is therefore read once and
# the metadata kept as data, `web_metadata` in the decision file. Judgements that
# are about a publisher rather than a page, whether it has a stake, whether its
# site is a periodical, are made once per domain in the decision file's
# `[domain."host"]` tables.

WEB_KIND = {
    "journal-article": "journal-article", "report": "report", "working-paper": "report",
    "government-report": "report", "pdf": "report", "web-article": "web-page", "web-page": "web-page",
    "press-release": "web-page", "speech-or-testimony": "web-page", "dataset": "dataset",
    "standard": "standard", "documentation": "documentation", "book": "book", "chapter": "chapter",
}
DOMAIN_KEYS = {"stake", "primary", "periodical", "container", "publisher", "kind"}
LEGACY_KIND = {"Government": "report", "Data": "dataset", "Research": "report", "Report": "report",
               "Book": "book", "Commentary": "web-page", "Journal": "report", "Primary": "web-page",
               "Reference": "web-page", "Standard": "standard", "Documentation": "documentation"}


def _host_of(url):
    import urllib.parse
    return urllib.parse.urlsplit(url).netloc.lower()


DOMAINS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_sources", "domains.toml")


def load_domains(path=None):
    """The shared domain judgements, `_sources/domains.toml`, made once for every article."""
    import tomllib
    path = path or DOMAINS
    if not os.path.exists(path):
        return {}
    with open(path, "rb") as fh:
        doc = tomllib.load(fh)
    for host, rule in doc.items():
        if not isinstance(rule, dict) or set(rule) - DOMAIN_KEYS - {"why"}:
            raise sources.SourceError(f"{path}: [{host}] takes only {sorted(DOMAIN_KEYS | {'why'})}")
        if not rule.get("why"):
            raise sources.SourceError(f"{path}: [{host}] needs `why`, the reason for the judgement")
    return {h: {k: v for k, v in r.items() if k != "why"} for h, r in doc.items()}


def domain_rule(url, domains):
    """The decision file's rule for a URL's host, trying the host and then without `www.`."""
    h = _host_of(url)
    rule = domains.get(h) or domains.get(h[4:] if h.startswith("www.") else "www." + h) or {}
    extra = set(rule) - DOMAIN_KEYS
    if extra:
        raise sources.SourceError(f"[domain.{h}] unknown keys {sorted(extra)}")
    return rule


def _people_from_label(who):
    """Surnames from a legacy label's author part, and whether the list is complete."""
    who = re.sub(r"\s+\d{4}[a-z]?$", "", who).strip()
    incomplete = bool(re.search(r"\band others\b|\bet al\b", who))
    who = re.sub(r",?\s*(and others|et al\.?)$", "", who)
    names = [x.strip() for x in re.split(r",\s*|\s+and\s+", who) if x.strip()]
    if len(names) == 1 and len(names[0].split()) > 2:
        return [{"name": names[0]}], incomplete
    return [{"family": n} for n in names], incomplete


def record_from_web(anchor, url, meta, label, rule, read_date):
    """A draft record for a web source from its page metadata, or from its label if unread.

    `meta` is one entry of the metadata file, or None. A page that could not be
    read is built from the article's legacy label and its note says so, since
    the label may hold surnames only and a description in place of a title.
    """
    read = meta is not None and meta.get("status") in ("read", "redirected", "partial", "searched") and meta.get("title")
    parts = label.split(", ") if label else []
    if read:
        kind = rule.get("kind") or WEB_KIND.get(meta.get("doc_type"), "web-page")
        title = meta["title"] + (f": {meta['subtitle']}" if meta.get("subtitle") else "")
        authors = []
        for x in meta.get("authors") or []:
            if x.get("family"):
                fam, giv = x["family"], x.get("given") or ""
                # A SUFFIX FILED WITH THE GIVEN NAMES, `James O., Jr.`, belongs to the family name.
                m = re.match(r"^(.*?),?\s+(Jr\.|Sr\.|II|III|IV)$", giv)
                if m:
                    giv, fam = m.group(1), f"{fam} {m.group(2)}"
                authors.append({"family": _family(fam), "given": _given(giv)} if giv else {"family": _family(fam)})
            elif x.get("name"):
                authors.append({"name": sources.clean_text(x["name"])})
        date = (meta.get("date") or "")[:10]
        # A DATE THAT IS NOT ISO, such as a museum's `1863/1877`, keeps its first year;
        # the full form stays in the note.
        if date and not re.match(r"^\d{4}(-\d{2}(-\d{2})?)?$", date):
            first = re.search(r"\d{4}", date)
            meta = dict(meta, notes=((meta.get("notes") or "") + f" Dated {meta.get('date')} on the page.").strip())
            date = first.group(0) if first else ""
        if not date:
            m = re.search(r"\b(\d{4})[a-z]?(?=, )", label or "")
            if m:
                date = m.group(1)
                meta = dict(meta, notes=((meta.get("notes") or "") + " The page shows no date; the year is from "
                                         "the article's label.").strip())
        publisher, container = meta.get("publisher"), meta.get("container")
        number = meta.get("number")
        # NO AUTHOR ON THE PAGE OR IN THE REGISTRY, but the article's label names
        # people, as for RAND's RRA3372-1: the label's surnames are used and noted.
        if not authors and label:
            parts_l = label.split(", ")
            k = next((i for i, x in enumerate(parts_l[1:], 1) if re.search(r"\b\d{4}[a-z]?$", x)), None)
            if k is not None:
                people, _inc = _people_from_label(", ".join(parts_l[1:k + 1]))
                if people and all("family" in p for p in people):
                    authors = people
                    meta = dict(meta, notes=((meta.get("notes") or "") + " The page names no author; the surnames "
                                             "are from the article's label.").strip())
        how = ("Metadata from agreeing search results, the page refusing automated reading"
               if meta.get("status") == "searched" else "Metadata read from the page")
        if meta.get("final_url") and meta.get("final_url") != url:
            how += f" at {meta['final_url']}"
        evidence = f"{how} on {read_date}: {meta.get('evidence') or meta['title']}"
        note = meta.get("notes") or None
    else:
        if not label:
            raise sources.SourceError(f"{anchor}: page unread and no label to build from")
        if len(parts) < 2:
            # A LABEL THAT IS ONLY A TITLE, as some A370 references were written,
            # gives an undated, unattributed entry; code marks are removed.
            parts = ["", label.replace("`", "")]
        k = next((i for i, x in enumerate(parts[1:], 1) if re.search(r"\b\d{4}[a-z]?$", x)), None)
        kind = rule.get("kind") or LEGACY_KIND.get(parts[0], "web-page")
        if k is None:
            # NO YEAR ANYWHERE: the label is `Category, Author, Title`, and the entry
            # takes n.d., which Chicago uses for an undated work.
            authors, incomplete = _people_from_label(parts[1]) if len(parts) > 2 else ([], False)
            title, date = ", ".join(parts[2:] if len(parts) > 2 else parts[1:]), ""
        else:
            authors, incomplete = _people_from_label(", ".join(parts[1:k + 1]))
            title = ", ".join(parts[k + 1:])
            date = re.search(r"(\d{4})[a-z]?$", parts[k]).group(1)
        publisher = container = number = None
        evidence = None
        note = (f"The page could not be read ({(meta or {}).get('status', 'no metadata')}), so this entry is built "
                f"from the article's label{', whose author list is incomplete' if incomplete else ''}; the title "
                f"may be a description.")
    title = sources.clean_text(title)
    # A LABEL'S TITLE WAS WRITTEN BY HAND IN HEADLINE STYLE, code names included,
    # so only a title read from a page is recased.
    rec = {"anchor": anchor, "kind": kind, "url": url, "title_published": title,
           "title": headline_case(title) if read else title,
           "authors": authors, "year": int(date[:4]) if date[:4].isdigit() else None}
    if rule.get("publisher"):
        publisher = rule["publisher"]
    if rule.get("container"):
        container = rule["container"]
    if kind == "web-page":
        if container or publisher:
            rec["container"] = sources.clean_text(container or publisher)
        if date and len(date) >= 4:
            rec["published"] = date
        else:
            rec["accessed"] = read_date
        for flag in ("stake", "primary", "periodical"):
            if rule.get(flag):
                rec[flag] = True
        # AN ORGANISATION'S OWN SITE IS NOT A PERIODICAL, so a host with a stake keeps
        # its name in roman unless its rule says otherwise.
        if meta and meta.get("doc_type") == "web-article" and "periodical" not in rule and not rule.get("stake"):
            rec["periodical"] = True
        if meta and meta.get("doc_type") == "speech-or-testimony" and "primary" not in rule:
            rec["primary"] = True
        # A PRESS RELEASE PROMOTES ITS ISSUER, government and university ones
        # included, which the rules place under Commercial Sources.
        if meta and meta.get("doc_type") == "press-release" and "stake" not in rule:
            rec["stake"] = True
    elif kind in ("journal-article", "chapter"):
        if not container:
            kind = rec["kind"] = "report"
        else:
            rec["container"] = sources.clean_text(container)
            if kind == "journal-article":
                rec["venue"] = rec["container"]
    elif kind == "documentation":
        rec["container"] = sources.clean_text(container or publisher or _host_of(url))
        rec["accessed"] = read_date
    if kind in ("report", "book", "dataset", "standard") and publisher:
        rec["publisher"] = sources.clean_text(publisher)
    if number and kind in ("report", "dataset", "standard"):
        rec["number"] = sources.clean_text(str(number))
    if evidence:
        rec["evidence"] = sources.clean_text(evidence)[:400]
    if note:
        rec["note"] = sources.clean_text(note)[:600]
    if rec["year"] is None:
        rec.pop("year")
    return rec


def openalex_cache_path(cache, doi):
    import os
    return os.path.join(os.path.dirname(cache.rstrip("/")), "openalex", doi.lower().replace("/", "_") + ".json")


def record_from_wikipedia(anchor, page_title, oldid, timestamp):
    """A pinned Wikipedia record. `page_title` is the canonical title the API returned."""
    import urllib.parse
    q = urllib.parse.quote(page_title.replace(" ", "_"), safe="()_,'-")
    return {
        "anchor": anchor,
        "kind": "wikipedia",
        "title_published": page_title,
        "title": headline_case(page_title),
        "year": int(timestamp[:4]),
        "revision": {"oldid": oldid, "timestamp": timestamp},
        "url": f"https://en.wikipedia.org/w/index.php?title={q}&oldid={oldid}",
    }


def record_from_related_post(anchor, post_stem, locators=None):
    rec = {"anchor": anchor, "kind": "related-post", "post": post_stem}
    if locators:
        rec["locators"] = dict(sorted(locators.items()))
    return rec


# ------------------------------------------------------------ post import
#
# WHY. The A384 conversion was three scratch scripts, a Crossref cache filler, a
# Wikipedia pinner and a `build.py` whose second half was human decisions typed
# as Python dictionaries. The mechanism is the same for every article and the
# decisions are data, so the decisions move to a TOML file and the mechanism
# moves here. Rebuilding A384 from its decision file reproduces its 99 stored
# records exactly, which `test_sources.py` checks.
#
# THE DECISION FILE, every key shown.
#
#   article = "A384"                  # names the read copy in Wikipedia evidence
#   crossref_cache = "tmp/a384/crossref"
#   wiki_pins = "tmp/a384/wiki_pins.json"
#
#   [title]                           # corrected display titles, by anchor
#   ref_51_pegasi_b = "51 Pegasi b"
#
#   [note]                            # registry corrections, by anchor
#   research_x = "what was wrong and where the right value came from"
#
#   [synthesis]                       # reviews, with the reason for the judgement
#   research_y = "why this is a review"
#
#   [fix.research_z]                  # field corrections
#   note = "required, where the right value came from"
#   drop = ["volume"]                 # optional, fields to remove
#   set = { pages = "L01706" }        # fields to set
#
# NO DECISION HERE CAN MARK A VENUE PEER-REVIEWED. Venues are judged once, in
# `_sources/venues.jsonl`, from the venue's own statement. A venue the import
# meets for the first time is added as not established, so its papers fall to
# rule 4 until someone reads its policy.

MINOR_UPPER = {w.upper() for w in MINOR} | {"SPACE", "JAPAN", "OF", "THE", "AND"}

DECISION_KEYS = {"article", "crossref_cache", "wiki_pins", "title", "note", "synthesis", "fix",
                 "dated_pins", "web_metadata", "domain", "web_read"}
FIX_KEYS = {"note", "drop", "set"}
NEW_VENUE_BASIS = "Full-paper peer review not established from the venue's own statement; default deny."


def load_decisions(path):
    """A decision file, validated. Raises SourceError on any malformed entry."""
    import tomllib
    with open(path, "rb") as fh:
        doc = tomllib.load(fh)
    extra = set(doc) - DECISION_KEYS
    if extra:
        raise sources.SourceError(f"{path}: unknown keys {sorted(extra)}")
    for k in ("article", "crossref_cache", "wiki_pins"):
        if not isinstance(doc.get(k), str) or not doc[k]:
            raise sources.SourceError(f"{path}: {k} is required")
    if "dated_pins" in doc and not isinstance(doc["dated_pins"], bool):
        raise sources.SourceError(f"{path}: dated_pins is true or false")
    if not (isinstance(doc.get("web_metadata", []), list) and all(isinstance(x, str) for x in doc.get("web_metadata", []))):
        raise sources.SourceError(f"{path}: web_metadata is a list of paths")
    if "web_read" in doc and not re.match(r"^\d{4}-\d{2}-\d{2}$", str(doc["web_read"])):
        raise sources.SourceError(f"{path}: web_read is the ISO date the pages were read")
    for host, rule in doc.get("domain", {}).items():
        if not isinstance(rule, dict) or set(rule) - DOMAIN_KEYS:
            raise sources.SourceError(f"{path}: [domain.{host}] takes only {sorted(DOMAIN_KEYS)}")
    for table in ("title", "note", "synthesis"):
        for a, v in doc.get(table, {}).items():
            if not isinstance(v, str) or not v.strip():
                raise sources.SourceError(f"{path}: [{table}] {a} must be a non-empty string")
    # ONE NOTE PER RECORD. Each of these tables writes `note`, and an anchor in
    # two of them would keep whichever ran last and silently lose the other.
    seen = {}
    for table in ("note", "synthesis", "fix"):
        for a in doc.get(table, {}):
            if a in seen:
                raise sources.SourceError(f"{path}: {a} is in both [{seen[a]}] and [{table}]; "
                                          "write one note")
            seen[a] = table
    for a, f in doc.get("fix", {}).items():
        if set(f) - FIX_KEYS or not isinstance(f.get("note"), str) or not f["note"].strip():
            raise sources.SourceError(f"{path}: [fix.{a}] takes note, drop and set, and needs a note")
        if not isinstance(f.get("drop", []), list) or not isinstance(f.get("set", {}), dict):
            raise sources.SourceError(f"{path}: [fix.{a}] drop is a list and set a table")
        if set(f.get("set", {})) - sources.FIELDS:
            raise sources.SourceError(f"{path}: [fix.{a}] sets unknown fields "
                                      f"{sorted(set(f['set']) - sources.FIELDS)}")
    return doc


def decided_fields(decisions):
    """{anchor: set of fields} that a decision file sets, for amending stored records.

    A DECISION AMENDS THE STORE. A record already stored from another article
    keeps its corrections, but a decision this article's reviewer made about it,
    such as A382's judgement that a review in Progress in Aerospace Sciences is a
    synthesis, must reach the store too, or the decision file would claim a
    decision the database does not hold.
    """
    out = {}
    for a, f in decisions.get("fix", {}).items():
        out.setdefault(a, set()).update(set(f.get("set", {})) | set(f.get("drop", [])) | {"note"})
    for a in decisions.get("title", {}):
        out.setdefault(a, set()).add("title")
    for a in decisions.get("synthesis", {}):
        out.setdefault(a, set()).update({"synthesis", "note"})
    for a in decisions.get("note", {}):
        out.setdefault(a, set()).add("note")
    return out


def link_definitions(text):
    """{anchor: target} for every reference definition in a post."""
    return dict(re.findall(r"^\[([a-z0-9_]+)\]: (\S+.*)$", text, re.M))


def crossref_cache_path(cache, doi):
    import os
    return os.path.join(cache, doi.lower().replace("/", "_") + ".json")


BATCH = 40   # DOIs per Crossref request; 40 took 1.4 s and 80 took 15 s on 2026-10-24


def fetch_crossref(post_path, cache):
    """Cache the raw Crossref record of every DOI a post defines. Returns the misses.

    Raw records are kept so every registry correction can be audited against
    what the registry actually said.
    """
    import json
    import os
    import fetch
    os.makedirs(cache, exist_ok=True)
    text = open(post_path, encoding="utf-8").read()
    dois = sorted({t[len("https://doi.org/"):] for t in link_definitions(text).values()
                   if t.startswith("https://doi.org/")})
    todo = [d for d in dois if not os.path.exists(crossref_cache_path(cache, d))
            and not os.path.exists(openalex_cache_path(cache, d))]

    def save(d, m):
        with open(crossref_cache_path(cache, d), "w", encoding="utf-8") as fh:
            json.dump(m, fh, indent=1, sort_keys=True)

    # BATCHES FIRST, then singles for whatever a batch did not return.
    # A FAILED BATCH IS HALVED, not abandoned, because one identifier the
    # registry rejects, such as one with angle brackets, fails the whole
    # request. A work queue, not recursion; each split halves a chunk, so the
    # queue empties after at most 2 * len(todo) requests.
    single = []
    queue = [todo[i:i + BATCH] for i in range(0, len(todo), BATCH)]
    while queue:
        chunk = queue.pop()
        got = fetch.crossref_works(chunk)
        if got is None:
            if len(chunk) > 1:
                queue += [chunk[:len(chunk) // 2], chunk[len(chunk) // 2:]]
            else:
                single += chunk
            continue
        for d in chunk:
            m = got.get(d.lower())
            if m:
                save(d, m)
            else:
                single.append(d)
    missing = []
    for d in single:
        m = fetch.crossref_work(d)
        if m:
            save(d, m)
            continue
        # NOT IN CROSSREF: the OpenAlex record is cached beside the Crossref ones.
        w = fetch.openalex_work(d)
        if w:
            path = openalex_cache_path(cache, d)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(w, fh, indent=1, sort_keys=True)
        else:
            missing.append(d)
    return dois, missing


def _title_key(t):
    import urllib.parse
    return re.sub(r"[^a-z0-9]", "", urllib.parse.unquote(t).lower())


# A pin is verified when the text read is shown to be the revision pinned: by
# comparing saved wikitext with the revision's (`exact`, or `stripped` when only
# surrounding whitespace differs), or by the revision id a saved rendered page
# carries in its own configuration (`embedded`), which is the id of the very
# revision the reader was served.
VERIFIED_PINS = ("exact", "stripped", "embedded")

_WG_PAGE = re.compile(r'"wgPageName":"((?:[^"\\]|\\.)+)"')
_WG_REV = re.compile(r'"wgRevisionId":(\d+)')


def saved_html_revisions(saved_dirs):
    """{title key: (file, page name, revision id)} for saved rendered Wikipedia pages.

    A380 saved its pages as rendered HTML under hashed names, so the file name
    says nothing and the page's own `wgPageName` and `wgRevisionId` are read.
    A revision id of 0 is a page that did not exist, and is skipped.
    """
    import glob
    import json as _json
    import os
    out = {}
    for d in saved_dirs:
        for f in sorted(glob.glob(os.path.join(d, "*"))):
            if not os.path.isfile(f) or f.endswith((".txt", ".clean", ".json")):
                continue
            head = open(f, encoding="utf-8", errors="replace").read(400_000)
            page, rev = _WG_PAGE.search(head), _WG_REV.search(head)
            if page and rev and int(rev.group(1)) > 0:
                name = _json.loads(f'"{page.group(1)}"')
                out.setdefault(_title_key(name), (f, name, int(rev.group(1))))
    return out


def pin_wikipedia(post_path, saved_dirs, pins_path, at=None):
    """Pin each Wikipedia link in a post to a revision, verified against a saved copy.

    The revision pinned is the last one at or before the saved copy's
    modification time, and its wikitext is compared with the copy. `exact` and
    `stripped` are verified pins. `MISMATCH` means the copy was not taken from
    that revision, and such a pin must not be used as evidence. With `at`, a
    link that has no saved copy is pinned to the revision current at that
    timestamp and marked `unverified`, since nothing shows that text was read.
    Pins already verified are kept, so an interrupted run resumes.
    """
    import datetime
    import glob
    import json
    import os
    import urllib.parse
    import fetch
    text = open(post_path, encoding="utf-8").read()
    links = {a: urllib.parse.unquote(t[len("https://en.wikipedia.org/wiki/"):])
             for a, t in link_definitions(text).items()
             if t.startswith("https://en.wikipedia.org/wiki/")}
    saved = {}
    for d in saved_dirs:
        # THE FIRST DIRECTORY GIVEN WINS. An article's own copies come first and
        # another article's are a fallback, never a replacement.
        for f in sorted(glob.glob(os.path.join(d, "*.txt"))):
            saved.setdefault(_title_key(os.path.basename(f)[:-4]), f)
    html = saved_html_revisions(saved_dirs)
    pins = json.load(open(pins_path)) if os.path.exists(pins_path) else {}
    for anchor, title in sorted(links.items()):
        prev = pins.get(anchor, {})
        if prev.get("match") in VERIFIED_PINS or (at and prev.get("match") == "unverified"
                                                   and prev.get("saved_at") == at):
            continue
        hit = html.get(_title_key(title))
        if hit is None and not saved.get(_title_key(title)):
            # A link through a redirect: the saved page carries the target's name.
            cur = fetch.wikipedia_revision(title)
            hit = html.get(_title_key(cur["page_title"])) if cur else None
        if hit:
            hf, name, revid = hit
            rev = fetch.wikipedia_revision(title, oldid=revid)
            ts = datetime.datetime.fromtimestamp(os.path.getmtime(hf), datetime.timezone.utc)
            ok = rev is not None and _title_key(rev["page_title"]) == _title_key(name)
            pins[anchor] = {"title": title, "page_title": rev["page_title"] if rev else name, "oldid": revid,
                            "timestamp": rev["timestamp"] if rev else None, "saved_file": hf,
                            "saved_at": ts.strftime("%Y-%m-%dT%H:%M:%SZ"),
                            "match": "embedded" if ok else "MISMATCH"}
            continue
        f = saved.get(_title_key(title))
        if not f:
            # A COPY SAVED UNDER A SHORTER NAME, such as `Sphere_of_influence.txt` for
            # `Sphere of influence (astrodynamics)`. A candidate is accepted only if
            # its text is byte-identical to the revision, so a wrong guess cannot pin.
            for key in sorted((k for k in saved if _title_key(title).startswith(k)), key=len, reverse=True):
                cand = saved[key]
                ts_c = datetime.datetime.fromtimestamp(os.path.getmtime(cand), datetime.timezone.utc)
                rev_c = fetch.wikipedia_revision(title, before=ts_c.strftime("%Y-%m-%dT%H:%M:%SZ"))
                if rev_c and rev_c["content"].strip() == open(cand, encoding="utf-8").read().strip():
                    f = cand
                    break
        if f:
            ts = datetime.datetime.fromtimestamp(os.path.getmtime(f), datetime.timezone.utc)
            ts = ts.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif at:
            ts = at
        else:
            pins[anchor] = {"title": title, "match": "no saved copy"}
            continue
        rev = fetch.wikipedia_revision(title, before=ts)
        if rev is None:
            pins[anchor] = {"title": title, "match": "FAILED"}
            continue
        if f:
            mine = open(f, encoding="utf-8").read()
            match = ("exact" if rev["content"] == mine
                     else "stripped" if rev["content"].strip() == mine.strip() else "MISMATCH")
        else:
            match = "unverified"
        pins[anchor] = {"title": title, "page_title": rev["page_title"], "oldid": rev["oldid"],
                        "timestamp": rev["timestamp"], "saved_file": f, "saved_at": ts, "match": match}
        with open(pins_path, "w", encoding="utf-8") as fh:
            json.dump(pins, fh, indent=1, sort_keys=True)
    with open(pins_path, "w", encoding="utf-8") as fh:
        json.dump(pins, fh, indent=1, sort_keys=True)
    return pins


def import_post(post_path, decisions, venues, store=None):
    """Draft records for every source a post defines, with its decisions applied.

    Returns (records, new_venues). Raises SourceError on a link it cannot
    classify, a DOI missing from the cache, or a Wikipedia link with no
    verified pin, rather than importing an incomplete set.
    """
    import json
    text = open(post_path, encoding="utf-8").read()
    pins = json.load(open(decisions["wiki_pins"])) if os.path.exists(decisions["wiki_pins"]) else {}
    web_meta = {}
    # LATER FILES WIN, so a recovery pass listed last replaces a failed first reading,
    # but only where it found something: an unresolved recovery keeps the first.
    for path in decisions.get("web_metadata", []):
        for m in json.load(open(path, encoding="utf-8")):
            if m.get("status") == "unresolved" and m["url"] in web_meta:
                continue
            web_meta[m["url"]] = m
    labels = {anc: lab for lab, anc in LEGACY_ITEM.findall(text)}
    shared_domains = load_domains()
    index = sources.article_index(store, post_path) if store else None
    recs, related, errors = {}, {}, []
    for a, target in sorted(link_definitions(text).items()):
        if target.startswith("https://doi.org/"):
            doi = target[len("https://doi.org/"):].split()[0]
            cr = crossref_cache_path(decisions["crossref_cache"], doi)
            oa = openalex_cache_path(decisions["crossref_cache"], doi)
            try:
                if os.path.exists(cr):
                    recs[a] = record_from_crossref(a, json.load(open(cr)), doi)
                elif os.path.exists(oa):
                    recs[a] = record_from_openalex(a, json.load(open(oa)), doi)
                else:
                    errors.append(f"{a}: {target} in neither registry cache, run fetch-crossref")
            except sources.SourceError as e:
                errors.append(str(e))
            continue
        elif target.startswith("https://en.wikipedia.org/"):
            p = pins.get(a, {})
            # A DATED PIN is the revision current when the article was drafted, used
            # only when no copy of the text read was saved, and only when the
            # decision file says so, since it shows when the page was read but not
            # what it said.
            dated_ok = decisions.get("dated_pins") and p.get("match") == "unverified"
            if p.get("match") not in VERIFIED_PINS and not dated_ok:
                errors.append(f"{a}: no verified Wikipedia pin ({p.get('match')})")
                continue
            # A CONVERTED POST LINKS ITS PIN ALREADY. Re-importing it is how the
            # store is rebuilt and tested, so the link's revision must be the pin's.
            linked = re.search(r"[?&]oldid=(\d+)", target)
            if linked and int(linked.group(1)) != p["oldid"]:
                errors.append(f"{a}: links revision {linked.group(1)} but is pinned to {p['oldid']}")
                continue
            recs[a] = record_from_wikipedia(a, p["page_title"], p["oldid"], p["timestamp"])
            held = re.search(r"tmp/(a\d+)/", p.get("saved_file") or "")
            read_for = held.group(1).upper() if held else decisions["article"]
            recs[a]["evidence"] = {
                "exact": f"Revision text byte-identical to the copy read for {read_for}, "
                         f"saved {p['saved_at']}.",
                "stripped": f"Revision text identical, apart from surrounding whitespace, to the copy read "
                            f"for {read_for}, saved {p['saved_at']}.",
                "embedded": f"Revision id carried by the rendered page saved when {read_for} "
                            f"was researched, {p['saved_at']}.",
                "unverified": f"No copy of the text read for {read_for} was saved. The revision current at "
                              f"{p['saved_at']}, when the article was drafted, so the text read may differ.",
            }[p["match"]]
        elif target.startswith("{% post_url"):
            m = re.match(r"\{% post_url (\S+) %\}(?:#(\S+))?", target)
            related.setdefault(m.group(1), []).append((a, m.group(2)))
        elif target.startswith(("https://", "http://")) and decisions.get("web_read"):
            url = target.split()[0]
            try:
                recs[a] = record_from_web(a, url, web_meta.get(url), labels.get(a, ""),
                                          domain_rule(url, {**shared_domains, **decisions.get("domain", {})}),
                                          decisions["web_read"])
            except sources.SourceError as e:
                # A CONVERTED POST NO LONGER CARRIES ITS LEGACY LABELS, so a page that
                # was built from one is rebuilt from the stored record instead.
                canon = (index or {}).get(a, (None,))[0]
                if canon:
                    recs[a] = dict(store[canon], anchor=a)
                else:
                    errors.append(str(e))
        else:
            errors.append(f"{a}: no importer for {target[:60]}")
    for stem, items in related.items():
        base = [a for a, frag in items if frag is None]
        if len(base) != 1:
            errors.append(f"{stem}: needs exactly one unfragmented anchor, has {base}")
            continue
        recs[base[0]] = record_from_related_post(base[0], stem, {a: f for a, f in items if f})
    for table in ("title", "note", "synthesis", "fix"):
        for a in decisions.get(table, {}):
            if a not in recs:
                errors.append(f"[{table}] {a} names no source in the post")
    if errors:
        raise sources.SourceError(f"{len(errors)} import error(s)\n  " + "\n  ".join(errors))
    # A REGISTRY RECORD WITH NO AUTHORS whose legacy label names people, as for
    # RAND's RRA1658-1, takes the label's surnames, and its note says so.
    for a, r in recs.items():
        if r.get("doi") and not sources.creators(r) and r.get("kind") not in ("wikipedia", "related-post"):
            parts_l = labels.get(a, "").split(", ")
            k = next((i for i, x in enumerate(parts_l[1:], 1) if re.search(r"\b\d{4}[a-z]?$", x)), None)
            if k is not None:
                people, _inc = _people_from_label(", ".join(parts_l[1:k + 1]))
                if people and all("family" in p and p["family"] not in ("Unattributed", "Anonymous")
                                  for p in people):
                    r["authors"] = people
                    r["note"] = "The registry lists no author; the surnames are from the article's label."
    for a, f in decisions.get("fix", {}).items():
        for k in f.get("drop", []):
            recs[a].pop(k, None)
        recs[a].update(f.get("set", {}))
        recs[a]["note"] = f["note"]
    for a, t in decisions.get("title", {}).items():
        recs[a]["title"] = t
    for a, why in decisions.get("synthesis", {}).items():
        recs[a]["synthesis"] = True
        recs[a]["note"] = why
    for a, n in decisions.get("note", {}).items():
        recs[a]["note"] = n
    new_venues = {}
    for r in recs.values():
        v = r.get("venue")
        if v and v not in venues and v not in new_venues:
            new_venues[v] = {"venue": v, "peer_reviewed": False, "checked": False, "basis": NEW_VENUE_BASIS,
                             "class": "proceedings" if r["kind"] == "proceedings-paper" else "journal"}
            if r.get("publisher_registry") or r.get("publisher"):
                new_venues[v]["publisher"] = r.get("publisher_registry") or r["publisher"]
    every = {**venues, **new_venues}
    for r in recs.values():
        r["rule"], r["section"] = sources.classify(r, every)
    return recs, new_venues


def identity(r):
    """What a record IS, independent of its text: a DOI, a page revision, a post, or a URL.

    Two articles that cite the same identity under the same anchor cite one
    source, and the stored record, with its corrections, is the source.
    """
    if r.get("kind") == "related-post":
        return ("post", r.get("post"))
    if r.get("kind") == "wikipedia":
        return ("wikipedia", r.get("title_published"), (r.get("revision") or {}).get("oldid"))
    if r.get("doi"):
        return ("doi", r["doi"].lower())
    return ("url", r.get("url"))


def _renamed(anchor, ident, taken):
    """A canonical anchor for a source whose name the store already uses for another.

    The suffix is a hash of the source's identity, so every article that cites
    the same source under the same clashing name reaches the same record, and
    the first character after the prefix, which picks the shard, is unchanged.
    """
    import hashlib
    h = hashlib.sha1(repr(ident).encode("utf-8")).hexdigest()
    for n in range(6, len(h) + 1):  # bounded by the hash length
        cand = f"{anchor}_{h[:n]}"
        if cand not in taken:
            return cand
    raise sources.SourceError(f"{anchor}: no free canonical name")


def merge(store, drafts, decided=None, amap=None, refresh=False):
    """(merged, added, known, conflicts, extended, amap), merging by source identity.

    A source is matched by what it IS, `identity`, not by its name, so:

    - A KNOWN source, one whose identity is stored under any name, keeps the
      stored record, because a correction made once must survive every later
      import: A382 re-derived Kopp and Lean 2011 from Crossref with placeholder
      pages that A384's record had corrected. If the article names it
      differently, the article's map records its name.
    - This article's DECISIONS about a known source amend it, and a related
      post's new SECTION LOCATORS are added to it.
    - A NEW source takes the article's name, unless the store already uses that
      name for a different source, in which case it is stored under a renamed
      canonical anchor and the article's map points its name there. The article
      text never changes for this.
    - A locator name already bound to another section is a CONFLICT and is not
      written.

    `amap` is the article's existing map, extended and returned.
    """
    merged = dict(store)
    amap = dict(amap or {})
    by_id = {}
    for c, rec in store.items():
        by_id.setdefault(identity(rec), c)
    added, known, conflicts, extended = [], [], [], []
    for a, r in sorted(drafts.items()):
        ident = identity(r)
        c = by_id.get(ident)
        if c is None:
            c = a if a not in merged else _renamed(a, ident, merged)
            merged[c] = dict(r, anchor=c)
            by_id[ident] = c
            added.append(c)
            if c != a:
                amap[a] = c
            continue
        if c != a:
            amap[a] = c
        old = merged[c]
        if r.get("kind") == "related-post":
            loc = dict(old.get("locators", {}))
            clash = [k for k, f in r.get("locators", {}).items() if k in loc and loc[k] != f]
            if clash:
                conflicts.append(a)
                continue
            new_loc = {k: f for k, f in r.get("locators", {}).items() if k not in loc}
            if new_loc:
                merged[c] = dict(old, locators=dict(sorted({**loc, **new_loc}.items())))
                extended.append(c)
                continue
        # REFRESH rebuilds a known record from its registry draft when the importer
        # improves, but only a record with no note, because a note marks a human
        # correction, and a draft never replaces one.
        # Pins and related posts are not registry drafts: a pin's evidence names the
        # copy first verified, and a related post's locators gather across articles.
        if (refresh and not old.get("note") and r.get("kind") not in ("wikipedia", "related-post")
                and r != dict(old, anchor=r.get("anchor"))):
            merged[c] = dict(r, anchor=c)
            extended.append(c)
            continue
        fields = (decided or {}).get(a, set())
        amended = {k: r[k] for k in fields if k in r and old.get(k) != r[k]}
        dropped = [k for k in fields if k not in r and k in old]
        if amended or dropped:
            rec = {k: v for k, v in old.items() if k not in dropped}
            rec.update(amended)
            merged[c] = rec
            extended.append(c)
            continue
        known.append(c)
    return merged, added, known, conflicts, extended, amap


def _diff(old, new):
    keys = sorted(set(old) | set(new))
    return [f"      {k}: {old.get(k)!r} -> {new.get(k)!r}" for k in keys if old.get(k) != new.get(k)]


LEGACY_ITEM = re.compile(r"^- \[(.+)\]\[([a-z0-9_]+)\]$", re.M)


def legacy_labels(text):
    """{anchor: (who-and-year, title)} from a post's pre-conversion reference list.

    The legacy label is `Category, Author Year, Title` for a work and
    `Reference, Title, Wikipedia` for an encyclopaedia article. Those labels were
    checked by hand while the article was drafted, so they are the second
    opinion every registry title and author list is reviewed against.
    """
    out = {}
    for label, a in LEGACY_ITEM.findall(text):
        parts = label.split(", ")
        if parts[0] == "Reference" and parts[-1] == "Wikipedia":
            out[a] = ("", ", ".join(parts[1:-1]))
        else:
            # The author part may hold commas, `Abarbanell, Bushee and Smith Raedy 2003`,
            # so it ends at the first part that ends in a year.
            k = next((i for i, x in enumerate(parts[1:], 1) if re.search(r"\b\d{4}[a-z]?$", x)), None)
            if k is not None and k + 1 < len(parts):
                out[a] = (", ".join(parts[1:k + 1]), ", ".join(parts[k + 1:]))
    return out


def _letters(s):
    return re.sub(r"[^a-z0-9]", "", sources.clean_text(s).lower())


def wikitext_authors(doi, saved_dirs):
    """[(file, [(family, given)])] from citation templates in saved wikitext that name `doi`.

    Wikipedia editors often transcribe a full author list where a registry kept
    only the first author, as for Wieczorek et al. 2006, which Crossref and
    OpenAlex give as one author and the Moon article gives as sixteen. The
    saved copies are the pinned revisions, so the source of a correction is a
    fixed text.
    """
    import glob
    import os
    out = []
    pat = re.compile(r"\{\{\s*[Cc]ite[^{}]*?" + re.escape(doi) + r"[^{}]*\}\}|"
                     r"\{\{\s*[Cc]ite(?:(?!\}\})[^{])*?" + re.escape(doi), re.I | re.S)
    for d in saved_dirs:
        for f in sorted(glob.glob(os.path.join(d, "*.txt"))):
            text = open(f, encoding="utf-8", errors="replace").read()
            for m in pat.finditer(text):
                start = text.rfind("{{", 0, m.start() + 2)
                end = text.find("}}", m.end() - 2)
                tpl = text[start:end if end > 0 else m.end()]
                fams = dict(re.findall(r"\|\s*last(\d*)\s*=\s*([^|}]+)", tpl))
                givs = dict(re.findall(r"\|\s*first(\d*)\s*=\s*([^|}]+)", tpl))
                keys = sorted(fams, key=lambda k: int(k or 1))
                people = [(fams[k].strip(), givs.get(k, "").strip()) for k in keys]
                if people:
                    out.append((f, people))
    return out


def review(text, drafts, store=None, second_opinion=False, saved_dirs=()):
    """[(anchor, [findings])] for each drafted record a person should look at.

    Each finding names a difference from the legacy label, or a field a
    registry commonly gets wrong. A record with no findings still had its title
    recased by `headline_case`, which is a proposal, so the command prints every
    title for reading and marks only the ones that need a decision.
    """
    legacy = legacy_labels(text)
    rows = []
    for a, r in sorted(drafts.items()):
        if r.get("kind") == "related-post":
            continue
        if store and a in store and identity(store[a]) == identity(r):
            continue
        f = []
        who, old_title = legacy.get(a, ("", ""))
        if old_title and _letters(old_title.replace(",", "")) != _letters(r["title"]):
            f.append(f"WORDS DIFFER from the label: {old_title!r}")
        if who:
            m = re.match(r"^(.*?)\s+(\d{4}[a-z]?)$", who)
            if m:
                year = str(r.get("year") or "")
                if not m.group(2).startswith(year) or not year:
                    f.append(f"YEAR {year or 'missing'} against the label's {m.group(2)}")
                label_people = m.group(1)
                if r.get("kind") != "wikipedia" and _letters(sources.cite_label(r)) != _letters(
                        re.sub(r"\bet al\.?", "et al", label_people)):
                    f.append(f"AUTHORS read {sources.cite_label(r)!r}, the label {label_people!r}")
        if r.get("kind") == "journal-article":
            if not r.get("pages"):
                f.append("NO PAGES or article number")
            if not r.get("volume"):
                f.append("NO VOLUME")
        if r.get("kind") in ("book", "report") and not r.get("publisher"):
            f.append("NO PUBLISHER")
        if r.get("kind") != "wikipedia" and not sources.creators(r):
            f.append("NO AUTHORS OR EDITORS")
        if r.get("container") and re.search(r"&[a-z]+;|[<>]|\b\d+(st|nd|rd|th)\b.*\b\d+(st|nd|rd|th)\b", r["container"]):
            f.append(f"CONTAINER looks concatenated or escaped: {r['container'][:80]!r}")
        if second_opinion and r.get("doi") and any(x.startswith(("AUTHORS", "NO AUTHORS")) for x in f):
            import fetch
            w = fetch.openalex_work(r["doi"])
            names = [(x.get("author") or {}).get("display_name") for x in (w or {}).get("authorships", [])]
            f.append(f"OPENALEX authors: {names if w else 'lookup failed'}")
            for wf, people in wikitext_authors(r["doi"], saved_dirs)[:2]:
                f.append(f"WIKITEXT {os.path.basename(wf)} authors: {len(people)}, "
                         f"{'; '.join(', '.join(x for x in p if x) for p in people[:4])}"
                         + (" ..." if len(people) > 4 else ""))
        rows.append((a, r.get("title_published", ""), r.get("title", ""), f))
    return rows


# ------------------------------------------------------------ publishers
#
# WHY. The harvested surveys cite works in thousands of venues, and a venue-by-
# venue reading does not scale. A publisher's own policy that applies to ALL its
# journals, or ALL its proceedings, answers by whom for each of them, which is how
# Elsevier's publishing ethics credited five journals by hand. `publishers.toml`
# records each such policy once, with its scope, and `credit-venues` copies the
# answer into every uncredited venue that publisher's records name, so a venue
# record still carries its own evidence and the rule that validates it is unchanged.

PUBLISHERS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_sources", "publishers.toml")
PUBLISHER_KEYS = {"name", "aliases", "venue_pattern", "journals", "proceedings", "reviewers", "basis", "evidence"}


def load_publishers(path=None):
    import tomllib
    path = path or PUBLISHERS
    if not os.path.exists(path):
        return []
    with open(path, "rb") as fh:
        pubs = tomllib.load(fh).get("publisher", [])
    for p in pubs:
        extra = set(p) - PUBLISHER_KEYS
        if extra or not p.get("name") or not p.get("reviewers") or not p.get("basis"):
            raise sources.SourceError(f"{path}: publisher {p.get('name')!r} needs name, reviewers and basis "
                                      f"and takes only {sorted(PUBLISHER_KEYS)}")
        if not any(e.get("method") == "fetched" for e in p.get("evidence", [])):
            raise sources.SourceError(f"{path}: publisher {p['name']} needs fetched evidence")
        if not (p.get("journals") or p.get("proceedings")):
            raise sources.SourceError(f"{path}: publisher {p['name']} covers neither journals nor proceedings")
    return pubs


def credit_venues(venues, publishers):
    """[(venue, publisher)] credited by a publisher-wide policy, applied to `venues` in place.

    Only a venue not already credited and not a magazine is considered, and
    only when its recorded publisher matches a policy whose scope covers its
    class. A venue's own judgement, such as a review-only journal, is not
    overridden, because a venue with its own evidence keeps it.
    """
    names = {}
    patterns = []
    for p in publishers:
        for n in [p["name"]] + p.get("aliases", []):
            names[n.casefold()] = p
        if p.get("venue_pattern"):
            patterns.append((re.compile(p["venue_pattern"]), p))
    done = []
    for name, v in sorted(venues.items()):
        if v.get("peer_reviewed") or v.get("magazine") or v.get("evidence") or v.get("no_publisher_credit"):
            continue
        # A SOCIETY OR SERIES POLICY matches by venue name, `SIGPLAN` or `Lecture
        # Notes in Computer Science`, and is tried before the publisher's own.
        p = next((pp for rx, pp in patterns if rx.search(name)), None) or names.get((v.get("publisher") or "").casefold())
        if not p or not p.get("proceedings" if v.get("class") == "proceedings" else "journals"):
            continue
        scope = "proceedings" if v.get("class") == "proceedings" else "journals"
        v.update({"peer_reviewed": True, "checked": True, "reviewers": p["reviewers"], "via": p["name"],
                  "basis": f"{p['name']}'s policy for all its {scope}, which covers this venue. {p['basis']}",
                  "evidence": [dict(e) for e in p["evidence"]]})
        done.append((name, p["name"]))
    return done


def main(argv):
    import argparse
    import json
    ap = argparse.ArgumentParser(prog="sources_import.py")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("fetch-crossref", help="cache the Crossref record of every DOI a post defines")
    p.add_argument("post")
    p.add_argument("cache")
    p = sub.add_parser("pin-wiki", help="pin a post's Wikipedia links to verified revisions")
    p.add_argument("post")
    p.add_argument("pins")
    p.add_argument("--saved", action="append", default=[], help="directory of saved wikitext copies")
    p.add_argument("--at", help="pin links with no saved copy to this ISO timestamp, unverified")
    p = sub.add_parser("credit-venues", help="credit uncredited venues from publisher-wide policies")
    p.add_argument("--write", action="store_true")
    p = sub.add_parser("review", help="print drafted titles and flag what needs a decision")
    p.add_argument("post")
    p.add_argument("drafts")
    p.add_argument("--flagged", action="store_true", help="print only records with findings")
    p.add_argument("--second-opinion", action="store_true", help="fetch OpenAlex authors for author findings")
    p.add_argument("--saved", action="append", default=[], help="saved wikitext to search for fuller author lists")
    p = sub.add_parser("import", help="draft records for a post and merge them into the store")
    p.add_argument("post")
    p.add_argument("decisions")
    p.add_argument("--write", action="store_true", help="save the merged store")
    p.add_argument("--drafts", help="also save the draft records to this JSON file")
    p.add_argument("--verbose", action="store_true", help="show how drafts of known records differ")
    p.add_argument("--refresh", action="store_true",
                   help="rebuild known records that carry no note from their registry drafts")
    a = ap.parse_args(argv[1:])
    try:
        if a.cmd == "fetch-crossref":
            dois, missing = fetch_crossref(a.post, a.cache)
            print(f"{len(dois)} DOIs, {len(missing)} missing {missing}")
            return 1 if missing else 0
        if a.cmd == "pin-wiki":
            pins = pin_wikipedia(a.post, a.saved, a.pins, a.at)
            if not pins:
                # A converted post links `/w/index.php?...&oldid=`, which is already a pin.
                print("no unpinned https://en.wikipedia.org/wiki/ links in the post")
            bad = 0
            for anchor, pin in sorted(pins.items()):
                ok = pin.get("match") in VERIFIED_PINS
                bad += not ok
                print(f"  {anchor:34s} {pin.get('match'):13s} {pin.get('oldid', '')} {pin.get('page_title', '')}")
            print(f"{len(pins)} pins, {bad} not verified")
            return 1 if bad else 0
        if a.cmd == "credit-venues":
            venues = sources.load_venues()
            done = credit_venues(venues, load_publishers())
            from collections import Counter
            for pub, n in Counter(p for _v, p in done).most_common():
                print(f"  {n:5d}  {pub}")
            print(f"{len(done)} venues credited by publisher policy")
            if a.write:
                for v in venues.values():
                    sources.validate_venue(v)
                sources.save_venues(venues)
                store = sources.load_records()
                for r in store.values():
                    r["rule"], r["section"] = sources.classify(r, venues)
                sources.save_records(store)
                print("written")
            return 0
        if a.cmd == "review":
            rows = review(open(a.post, encoding="utf-8").read(), json.load(open(a.drafts, encoding="utf-8")),
                          sources.load_records(), a.second_opinion, a.saved)
            flagged = 0
            for anchor, pub, title, findings in rows:
                flagged += bool(findings)
                if findings or not a.flagged:
                    print(f"{anchor}\n    registry: {pub}\n    proposed: {title}")
                    for x in findings:
                        print(f"    ** {x}")
            print(f"{len(rows)} records, {flagged} with findings")
            return 0
        venues = sources.load_venues()
        store = sources.load_records()
        decisions = load_decisions(a.decisions)
        drafts, new_venues = import_post(a.post, decisions, venues, store)
        if a.drafts:
            with open(a.drafts, "w", encoding="utf-8") as fh:
                json.dump(drafts, fh, indent=1, ensure_ascii=False, sort_keys=True)
        merged, added, unchanged, conflicts, extended, amap = merge(
            store, drafts, decided_fields(decisions), sources.load_article_map(a.post), a.refresh)
        every = {**venues, **new_venues}
        for anchor in extended:
            merged[anchor]["rule"], merged[anchor]["section"] = sources.classify(merged[anchor], every)
        back = {}
        for name, canon in amap.items():
            back.setdefault(canon, name)
        draft_of = lambda c: drafts.get(c) or drafts.get(back.get(c, c), {})  # noqa: E731
        renamed = [c for c in added if c in back]
        mapped = sorted(n for n, c in amap.items() if c not in added)
        if a.verbose:
            for anchor in added:
                r = draft_of(anchor)
                if r.get("title") and r.get("title") != r.get("title_published"):
                    print(f"  NEW {anchor}\n      registry: {r['title_published']}\n      proposed: {r['title']}")
                else:
                    print(f"  NEW {anchor}")
            for anchor in unchanged:
                diff = _diff(store[anchor], draft_of(anchor))
                if diff:
                    print(f"  KNOWN {anchor}, stored record kept over this draft:")
                    print("\n".join(diff))
        for anchor in renamed:
            print(f"  RENAMED {back[anchor]} -> {anchor}, the store already uses the name for another source")
        for name in mapped[:40]:
            print(f"  MAPPED {name} -> {amap[name]}, the same source stored under another name")
        if len(mapped) > 40:
            print(f"  ... {len(mapped) - 40} more mapped")
        for anchor in conflicts:
            print(f"  CONFLICT {anchor}, a section locator name already bound to another section")
        for anchor in extended:
            print(f"  EXTENDED {anchor}, new locators or this article's decisions added to the stored record")
        if a.verbose or len(new_venues) <= 40:
            for v in new_venues:
                print(f"  NEW VENUE, not established: {v}")
        print(f"{len(drafts)} drafted: {len(added)} new ({len(renamed)} renamed), {len(unchanged)} known, "
              f"{len(mapped)} mapped, {len(extended)} extended, {len(conflicts)} conflicting, "
              f"{len(new_venues)} new venues")
        if conflicts:
            print("conflicts are not written; resolve each locator name, then rerun")
        if a.write and not conflicts:
            all_venues = {**venues, **new_venues}
            sources.validate(merged, all_venues)
            sources.save_venues(all_venues)
            sources.save_records(merged)
            sources.save_article_map(a.post, amap)
            print("written")
        return 1 if conflicts else 0
    except (sources.SourceError, OSError, ValueError) as e:
        print(f"FAILED: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
