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
    # AN EM DASH JOINS TWO WORDS WITHOUT A SPACE, `technology—A`, and what follows
    # it opens a new phrase, so each side is cased as a word and the right side
    # as a first word.
    if "\u2014" in word:
        left, right = word.split("\u2014", 1)
        return _case_word(left, force) + "\u2014" + _case_word(right, True)
    parts = word.split("-")
    out = []
    for i, p in enumerate(parts):
        if i and p[:1].isupper():
            out.append(p)
        else:
            out.append(_case_part(p, force if i == 0 else False))
    return "-".join(out)


def normalise_title(title):
    """Registry punctuation repaired before casing. A typed spaced hyphen
    separating a subtitle becomes a colon, and a trailing period is dropped,
    since the entry supplies its own. House rules, see CITATION_STYLE.md."""
    title = re.sub(r"\s+-\s+", ": ", title.strip())
    # AIAA's SGML entity for a question mark survives in some deposits, as in
    # Edelbaum's `How many impulses/ques/`.
    title = title.replace("/ques/", "?")
    # A trailing footnote mark from the publisher's typesetting is not the title.
    title = re.sub(r"[*\u2217\u2020\u2021]+$", "", title)
    return re.sub(r"(?<![A-Z])\.$", "", title)


def headline_case(title):
    """A proposed Chicago headline-case title. Review every result."""
    title = normalise_title(title)
    words = title.split(" ")
    if len(words) >= 3 and title.isupper():
        words = title.lower().split(" ")
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
    # AIAA deposits an apostrophe as a caret, `O^Neill`, a typesetting code.
    f = f.replace("^", "'")
    f = f.title() if f.isupper() and len(f) > 3 else f
    return re.sub(r",\s*(Jr\.|Sr\.|II|III|IV)$", r" \1", f)


def _authors(people):
    out = []
    for p in people or []:
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


CROSSREF_KIND = {
    "journal-article": "journal-article",
    "proceedings-article": "proceedings-paper",
    "book-chapter": "chapter",
    "book": "book",
    "edited-book": "book",
    "monograph": "book",
    "report": "report",
}


def record_from_crossref(anchor, msg):
    """A draft record from a Crossref `message`. Raises on a type with no mapping."""
    doi = msg["DOI"].lower()
    ctype = msg.get("type")
    kind = CROSSREF_KIND.get(ctype)
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
    issued = (msg.get("issued", {}) or {}).get("date-parts") or [[None]]
    rec = {
        "anchor": anchor,
        "kind": kind,
        "doi": doi,
        "title_published": sources.clean_text((msg.get("title") or [""])[0]),
        "authors": _authors(msg.get("author")),
        "year": (issued[0] or [None])[0],
        "publisher": sources.clean_text(msg.get("publisher", "")),
    }
    subtitle = sources.clean_text((msg.get("subtitle") or [""])[0])
    if subtitle and subtitle.lower() not in rec["title_published"].lower():
        rec["title_published"] += ": " + subtitle
    rec["title"] = headline_case(rec["title_published"])
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
    return rec


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

DECISION_KEYS = {"article", "crossref_cache", "wiki_pins", "title", "note", "synthesis", "fix"}
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
    missing = []
    for d in dois:
        path = crossref_cache_path(cache, d)
        if os.path.exists(path):
            continue
        m = fetch.crossref_work(d)
        if not m:
            missing.append(d)
            continue
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(m, fh, indent=1, sort_keys=True)
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
        if pins.get(anchor, {}).get("match") in VERIFIED_PINS:
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


def import_post(post_path, decisions, venues):
    """Draft records for every source a post defines, with its decisions applied.

    Returns (records, new_venues). Raises SourceError on a link it cannot
    classify, a DOI missing from the cache, or a Wikipedia link with no
    verified pin, rather than importing an incomplete set.
    """
    import json
    text = open(post_path, encoding="utf-8").read()
    pins = json.load(open(decisions["wiki_pins"]))
    recs, related, errors = {}, {}, []
    for a, target in sorted(link_definitions(text).items()):
        if target.startswith("https://doi.org/"):
            try:
                msg = json.load(open(crossref_cache_path(decisions["crossref_cache"],
                                                         target[len("https://doi.org/"):])))
            except FileNotFoundError:
                errors.append(f"{a}: {target} not in the Crossref cache, run fetch-crossref")
                continue
            recs[a] = record_from_crossref(a, msg)
        elif target.startswith("https://en.wikipedia.org/"):
            p = pins.get(a, {})
            if p.get("match") not in VERIFIED_PINS:
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
            }[p["match"]]
        elif target.startswith("{% post_url"):
            m = re.match(r"\{% post_url (\S+) %\}(?:#(\S+))?", target)
            related.setdefault(m.group(1), []).append((a, m.group(2)))
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
            new_venues[v] = {"venue": v, "peer_reviewed": False, "checked": False, "basis": NEW_VENUE_BASIS}
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


def merge(store, drafts, replace=False, decided=None):
    """(merged, added, known, conflicts, extended).

    A NEW anchor is added. A KNOWN anchor, the same identity already stored, keeps
    the stored record, because a correction made once must survive every later
    import of the same source: A382 re-derived Kopp and Lean 2011 from Crossref with
    its placeholder pages, which A384's record had already corrected. A related
    post's section locators are the exception, since articles cite different
    sections of one post, so new locators are added to the stored record, and a
    locator name already bound to another section is a conflict. The SAME anchor
    with a DIFFERENT identity is a conflict, never written without `replace`.
    """
    merged = dict(store)
    added, known, conflicts, extended = [], [], [], []
    for a, r in sorted(drafts.items()):
        if a not in store:
            added.append(a)
            merged[a] = r
            continue
        old = store[a]
        if identity(old) != identity(r):
            conflicts.append(a)
            if replace:
                merged[a] = r
            continue
        if r.get("kind") == "related-post":
            loc = dict(old.get("locators", {}))
            clash = [k for k, f in r.get("locators", {}).items() if k in loc and loc[k] != f]
            if clash:
                conflicts.append(a)
                continue
            new_loc = {k: f for k, f in r.get("locators", {}).items() if k not in loc}
            if new_loc:
                merged[a] = dict(old, locators=dict(sorted({**loc, **new_loc}.items())))
                extended.append(a)
                continue
        fields = (decided or {}).get(a, set())
        amended = {k: r[k] for k in fields if k in r and old.get(k) != r[k]}
        dropped = [k for k in fields if k not in r and k in old]
        if amended or dropped:
            rec = {k: v for k, v in old.items() if k not in dropped}
            rec.update(amended)
            merged[a] = rec
            extended.append(a)
            continue
        known.append(a)
    return merged, added, known, conflicts, extended


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
    p.add_argument("--replace", action="store_true", help="let a draft replace a differing record")
    p.add_argument("--drafts", help="also save the draft records to this JSON file")
    p.add_argument("--verbose", action="store_true", help="show how drafts of known records differ")
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
        drafts, new_venues = import_post(a.post, decisions, venues)
        if a.drafts:
            with open(a.drafts, "w", encoding="utf-8") as fh:
                json.dump(drafts, fh, indent=1, ensure_ascii=False, sort_keys=True)
        merged, added, unchanged, conflicts, extended = merge(store, drafts, a.replace,
                                                              decided_fields(decisions))
        every = {**venues, **new_venues}
        for anchor in extended:
            merged[anchor]["rule"], merged[anchor]["section"] = sources.classify(merged[anchor], every)
        for anchor in added:
            r = drafts[anchor]
            if r.get("title") and r.get("title") != r.get("title_published"):
                print(f"  NEW {anchor}\n      registry: {r['title_published']}\n      proposed: {r['title']}")
            else:
                print(f"  NEW {anchor}")
        for anchor in conflicts:
            print(f"  CONFLICT {anchor}, a different source under a stored anchor")
            print("\n".join(_diff(store[anchor], drafts[anchor])))
        for anchor in extended:
            print(f"  EXTENDED {anchor}, new locators or this article's decisions added to the stored record")
        for anchor in unchanged:
            diff = _diff(store[anchor], drafts[anchor])
            if diff and a.verbose:
                print(f"  KNOWN {anchor}, stored record kept over this draft:")
                print("\n".join(diff))
        for v in new_venues:
            print(f"  NEW VENUE, not established: {v}")
        print(f"{len(drafts)} drafted: {len(added)} new, {len(unchanged)} known, {len(extended)} extended, "
              f"{len(conflicts)} conflicting, {len(new_venues)} new venues")
        if conflicts and not a.replace:
            print("conflicts are not written; decide each, then rerun with --replace")
        if a.write:
            all_venues = {**venues, **new_venues}
            sources.validate(merged, all_venues)
            sources.save_venues(all_venues)
            sources.save_records(merged)
            print("written")
        return 1 if conflicts and not a.replace else 0
    except (sources.SourceError, OSError, ValueError) as e:
        print(f"FAILED: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
