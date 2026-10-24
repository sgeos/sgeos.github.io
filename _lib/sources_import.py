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
versus vs with within without
""".split())


def _case_part(part, force):
    """One hyphen-separated part. Existing capitals and digits are never removed."""
    lead = re.match(r"^[^\w]*", part).group(0)
    rest = part[len(lead):]
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
    later parts are capitalised unless they are minor words."""
    parts = word.split("-")
    return "-".join(_case_part(p, force if i == 0 else False) for i, p in enumerate(parts))


def normalise_title(title):
    """Registry punctuation repaired before casing. A typed spaced hyphen
    separating a subtitle becomes a colon, and a trailing period is dropped,
    since the entry supplies its own. House rules, see CITATION_STYLE.md."""
    title = re.sub(r"\s+-\s+", ": ", title.strip())
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
    g = g.title() if g.isupper() and len(g) > 2 and "." not in g else g
    g = re.sub(r"\.(?=[A-Z])", ". ", g)
    return re.sub(r"\b([A-Z])(?=\s|$)", r"\1.", g)


def _family(f):
    """Family names as printed. A generational suffix takes no comma in the 18th edition."""
    f = sources.clean_text(f)
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
        for f in glob.glob(os.path.join(d, "*.txt")):
            saved[_title_key(os.path.basename(f)[:-4])] = f
    pins = json.load(open(pins_path)) if os.path.exists(pins_path) else {}
    for anchor, title in sorted(links.items()):
        if pins.get(anchor, {}).get("match") in ("exact", "stripped"):
            continue
        f = saved.get(_title_key(title))
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
            if p.get("match") not in ("exact", "stripped"):
                errors.append(f"{a}: no verified Wikipedia pin ({p.get('match')})")
                continue
            # A CONVERTED POST LINKS ITS PIN ALREADY. Re-importing it is how the
            # store is rebuilt and tested, so the link's revision must be the pin's.
            linked = re.search(r"[?&]oldid=(\d+)", target)
            if linked and int(linked.group(1)) != p["oldid"]:
                errors.append(f"{a}: links revision {linked.group(1)} but is pinned to {p['oldid']}")
                continue
            recs[a] = record_from_wikipedia(a, p["page_title"], p["oldid"], p["timestamp"])
            recs[a]["evidence"] = (f"Revision text byte-identical to the copy read for "
                                   f"{decisions['article']}, saved {p['saved_at']}.")
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


def merge(store, drafts, replace=False):
    """(merged, added, unchanged, conflicts). A changed record is a conflict unless `replace`."""
    merged = dict(store)
    added, unchanged, conflicts = [], [], []
    for a, r in sorted(drafts.items()):
        if a not in store:
            added.append(a)
            merged[a] = r
        elif store[a] == r:
            unchanged.append(a)
        else:
            conflicts.append(a)
            if replace:
                merged[a] = r
    return merged, added, unchanged, conflicts


def _diff(old, new):
    keys = sorted(set(old) | set(new))
    return [f"      {k}: {old.get(k)!r} -> {new.get(k)!r}" for k in keys if old.get(k) != new.get(k)]


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
    p = sub.add_parser("import", help="draft records for a post and merge them into the store")
    p.add_argument("post")
    p.add_argument("decisions")
    p.add_argument("--write", action="store_true", help="save the merged store")
    p.add_argument("--replace", action="store_true", help="let a draft replace a differing record")
    p.add_argument("--drafts", help="also save the draft records to this JSON file")
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
                ok = pin.get("match") in ("exact", "stripped")
                bad += not ok
                print(f"  {anchor:34s} {pin.get('match'):13s} {pin.get('oldid', '')} {pin.get('page_title', '')}")
            print(f"{len(pins)} pins, {bad} not verified")
            return 1 if bad else 0
        venues = sources.load_venues()
        store = sources.load_records()
        drafts, new_venues = import_post(a.post, load_decisions(a.decisions), venues)
        if a.drafts:
            with open(a.drafts, "w", encoding="utf-8") as fh:
                json.dump(drafts, fh, indent=1, ensure_ascii=False, sort_keys=True)
        merged, added, unchanged, conflicts = merge(store, drafts, a.replace)
        for anchor in added:
            r = drafts[anchor]
            if r.get("title") and r.get("title") != r.get("title_published"):
                print(f"  NEW {anchor}\n      registry: {r['title_published']}\n      proposed: {r['title']}")
            else:
                print(f"  NEW {anchor}")
        for anchor in conflicts:
            print(f"  CONFLICT {anchor}")
            print("\n".join(_diff(store[anchor], drafts[anchor])))
        for v in new_venues:
            print(f"  NEW VENUE, not established: {v}")
        print(f"{len(drafts)} drafted: {len(added)} new, {len(unchanged)} unchanged, "
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
