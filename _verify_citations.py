#!/usr/bin/env python3
"""Verify that each DOI cited actually resolves to the work it is cited as.

This exists because of a real incident. A 2026-08-02 audit found THIRTEEN
citations whose DOI resolved to an entirely different paper, including one
labelled "Space Traffic Management Priorities" whose DOI returned "Robust
Inference for Consumption-Based Asset Pricing". Every one of them returned
HTTP 200, so a reachability check could never have caught them. An HTTP 200
verifies that something is served, not that it is the cited work.

Network-dependent and therefore deliberately outside the deploy path. Results
are cached, so repeat runs only query DOIs not seen before.

Usage:
    python3 _verify_citations.py              # check everything, using the cache
    python3 _verify_citations.py --limit 40   # bound the number of new lookups
    python3 _verify_citations.py --refresh    # ignore the cache
    python3 _verify_citations.py --quiet

Exit codes: 0 clean, 1 suspected mismatches or unregistered DOIs.
"""

import argparse
import glob
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

CACHE = ".cache/citations.json"
API = "https://api.crossref.org/works/"
# Crossref asks for a contact address so they can reach you about usage.
MAILTO = os.environ.get("CROSSREF_MAILTO", "sgeos@hotmail.com")
UA = f"sgeos.github.io citation check (mailto:{MAILTO})"
PAUSE = 0.4

DEF_RE = re.compile(r"^\[([A-Za-z0-9_-]+)\]:\s*(\S+)", re.M)
DOI_RE = re.compile(r"doi\.org/(10\.\S+)", re.I)

STOP = {
    "the", "a", "an", "of", "and", "or", "in", "on", "for", "to", "with", "at",
    "by", "from", "as", "is", "are", "be", "its", "it", "that", "this", "into",
    "über", "der", "die", "das", "und", "la", "le", "les", "de", "des", "du",
}


def tokens(text):
    return {w for w in re.findall(r"[A-Za-z]{3,}", text.lower()) if w not in STOP}


def load_cache(refresh):
    if refresh or not os.path.exists(CACHE):
        return {}
    try:
        with open(CACHE, encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return {}


def save_cache(cache):
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    with open(CACHE, "w", encoding="utf-8") as fh:
        json.dump(cache, fh, indent=0, sort_keys=True)


def collect():
    """Pair each DOI with the reference-list text that cites it."""
    items = []
    for path in sorted(glob.glob("_posts/*.markdown")) + sorted(glob.glob("_drafts/*.markdown")):
        if os.path.basename(path) == "template.markdown":
            continue
        text = open(path, encoding="utf-8").read()
        defs = {m.group(1): m.group(2) for m in DEF_RE.finditer(text)}
        for anchor, url in defs.items():
            m = DOI_RE.search(url)
            if not m:
                continue
            # Trailing punctuation belongs to the prose, not the DOI, but
            # parentheses can be part of it, so only strip unbalanced ones.
            doi = m.group(1).rstrip(".,;\"'>")
            while doi.endswith(")") and doi.count("(") < doi.count(")"):
                doi = doi[:-1]
            entry = re.search(rf"^-\s*\[([^\]]+)\]\[{re.escape(anchor)}\]\s*$", text, re.M)
            label = entry.group(1) if entry else anchor.replace("_", " ")
            items.append(
                {"post": os.path.basename(path), "anchor": anchor, "doi": doi, "label": label}
            )
    return items


def registration_agency(doi):
    """Ask the DOI system whether the identifier exists at all."""
    url = "https://doi.org/doiRA/" + urllib.parse.quote(doi, safe="/")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            data = json.load(r)
    except Exception:
        return "unresolved"
    if not data:
        return "unresolved"
    entry = data[0]
    if entry.get("RA"):
        return f"registered-with-{entry['RA'].lower().replace(' ', '-')}"
    return "nonexistent"


def lookup(doi):
    url = API + urllib.parse.quote(doi, safe="")
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            msg = json.load(r)["message"]
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {"status": registration_agency(doi)}
        return {"status": f"http-{e.code}"}
    except Exception as e:
        return {"status": f"error-{type(e).__name__}"}
    title = " ".join(msg.get("title") or [])
    authors = [a.get("family", "") for a in (msg.get("author") or [])]
    year = ""
    for key in ("issued", "published-print", "published-online"):
        parts = (msg.get(key) or {}).get("date-parts") or []
        if parts and parts[0] and parts[0][0]:
            year = str(parts[0][0])
            break
    return {"status": "ok", "title": title, "authors": authors, "year": year}


def assess(item, rec):
    """Decide whether the cited label plausibly describes the resolved work."""
    if rec["status"] != "ok":
        return rec["status"], ""
    label_t = tokens(item["label"])
    title_t = tokens(rec["title"])
    if not title_t:
        return "no-title", ""
    overlap = len(label_t & title_t) / len(title_t)
    surname_hit = any(a and a.lower() in item["label"].lower() for a in rec["authors"])
    # A fabricated citation shows near-zero title overlap AND no matching author.
    # Either signal alone is weak: labels abbreviate titles, and some entries
    # omit authors entirely.
    if overlap < 0.20 and not surname_hit:
        return "mismatch", f"resolves to {rec['authors'][:1]} {rec['year']} {rec['title'][:70]!r}"
    if overlap < 0.20:
        return "weak", f"author matches but title does not: {rec['title'][:60]!r}"
    return "ok", ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="cap new network lookups")
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    items = collect()
    cache = load_cache(args.refresh)
    dois = sorted({i["doi"] for i in items})
    todo = [d for d in dois if d not in cache]
    if args.limit:
        todo = todo[: args.limit]

    if not args.quiet:
        print(f"{len(items)} DOI citations, {len(dois)} distinct; {len(todo)} to look up")

    for n, doi in enumerate(todo, 1):
        cache[doi] = lookup(doi)
        if not args.quiet and (n % 25 == 0 or n == len(todo)):
            print(f"  looked up {n}/{len(todo)}")
            save_cache(cache)
        time.sleep(PAUSE)
    save_cache(cache)

    problems = {"mismatch": [], "nonexistent": [], "weak": [], "other": []}
    checked = 0
    for item in items:
        rec = cache.get(item["doi"])
        if not rec:
            continue
        checked += 1
        verdict, detail = assess(item, rec)
        if verdict == "ok":
            continue
        bucket = verdict if verdict in problems else "other"
        problems[bucket].append(f"{item['post']}: [{item['anchor']}] {item['doi']}\n      cited as {item['label'][:72]!r}\n      {detail or verdict}")

    print(f"\nchecked {checked} citations against Crossref")
    for kind in ("mismatch", "nonexistent", "weak", "other"):
        rows = problems[kind]
        if not rows:
            continue
        print(f"\n{kind.upper()} {len(rows)}")
        for r in rows[:25]:
            print(f"    {r}")
        if len(rows) > 25:
            print(f"    ... and {len(rows) - 25} more")

    hard = len(problems["mismatch"]) + len(problems["nonexistent"])
    print(f"\n{hard} hard problem(s), {len(problems['weak'])} weak, {len(problems['other'])} other")
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
