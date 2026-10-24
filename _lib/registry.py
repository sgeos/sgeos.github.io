#!/usr/bin/env python3
"""Registry lookups from the command line, replacing the per-article query scripts.

WHY. A375 to A384 carried thirty-seven scripts that opened their own HTTP
connections, against four that imported `fetch`. Each was a few lines, a search
or an abstract lookup, and each re-declared a user agent and a retry loop,
because a module with no command line is more work to use than a one-shot
script is to write. These commands are those scripts, generalised, on top of
`fetch`, so throttling, backoff and the no-email user agent hold everywhere.

INPUTS ARE DATA. Every command that takes queries or identifiers accepts them as
arguments or as `@FILE`, one per line, with `#` starting a comment. A list of
queries kept in an article's `tmp/` directory is then the whole of that
article's part.

A FAILED LOOKUP IS NOT AN EMPTY RESULT. Every command prints `FAILED` for a
request that never returned and exits 1 if any did, because a sweep that
silently skips a query reports a smaller literature rather than an error.

HOSTS. Only api.crossref.org, api.openalex.org and doi.org are contacted.

  python3 _lib/registry.py crossref QUERY... [--rows 5] [--filter F]
  python3 _lib/registry.py openalex QUERY... [--rows 5] [--filter F]
  python3 _lib/registry.py grep-abstracts QUERY REGEX [--rows 25] [--width 200]
  python3 _lib/registry.py abstract DOI...
  python3 _lib/registry.py works DOI... --out FILE.json
  python3 _lib/registry.py type DOI...
"""

import argparse
import json
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fetch  # noqa: E402


def expand(items):
    """Arguments with each `@FILE` replaced by the file's non-comment lines."""
    out = []
    for it in items:
        if it.startswith("@"):
            with open(it[1:], encoding="utf-8") as fh:
                for line in fh:
                    line = line.split("#", 1)[0].strip()
                    if line:
                        out.append(line)
        else:
            out.append(it)
    return out


def bare_doi(s):
    """A DOI without its resolver prefix, lower-cased, trailing full stop removed.

    A trailing full stop makes a different identifier string, which does not
    resolve and defeats any store keyed on the clean form.
    """
    s = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", s.strip(), flags=re.I)
    return s.lower().rstrip(".")


def _year(msg):
    parts = (msg.get("issued", {}) or {}).get("date-parts") or [[None]]
    return (parts[0] or [None])[0]


def cmd_crossref(a):
    failed = 0
    for q in expand(a.query):
        # NOT `fetch.crossref_search`, which returns [] on failure and so cannot
        # tell a query that matched nothing from one that never ran.
        params = {"query.bibliographic": q, "rows": str(a.rows)}
        if a.filter:
            params["filter"] = a.filter
        items = fetch.get_json(f"{fetch.CROSSREF}?{urllib.parse.urlencode(params)}")
        if items is None:
            print(f"FAILED {q}")
            failed += 1
            continue
        print(f"Q: {q}")
        for it in (items.get("message") or {}).get("items") or []:
            fam = ",".join(x.get("family", "") for x in (it.get("author") or [])[:4])
            print(f"   {it.get('DOI')} {_year(it)} {(it.get('title') or [''])[0][:85]}"
                  f" | {(it.get('container-title') or [''])[0][:30]} | {fam} | {it.get('type')}")
    return 1 if failed else 0


def cmd_openalex(a):
    failed = 0
    for q in expand(a.query):
        res = fetch.openalex_search(q, rows=a.rows, filters=a.filter,
                                    select="doi,title,publication_year,authorships,cited_by_count,type")
        if res is None:
            print(f"FAILED {q}")
            failed += 1
            continue
        print(f"Q: {q}")
        for r in res:
            names = [(x.get("author") or {}).get("display_name") or "" for x in r.get("authorships", [])[:4]]
            au = ",".join(n.split()[-1] if n.split() else "" for n in names)
            print(f"   {r.get('doi')} {r.get('publication_year')} {(r.get('title') or '')[:85]}"
                  f" | {au} | cited {r.get('cited_by_count')} | {r.get('type')}")
    return 1 if failed else 0


def cmd_grep_abstracts(a):
    """Abstracts matching QUERY, printed only where REGEX occurs, with context."""
    res = fetch.openalex_search(a.query, rows=a.rows, field="title_and_abstract.search",
                                select="doi,title,publication_year,abstract_inverted_index")
    if res is None:
        print(f"FAILED {a.query}")
        return 1
    rx = re.compile(r".{0,%d}(?:%s).{0,%d}" % (a.width, a.regex, a.width), re.I | re.S)
    hits = 0
    for w in res:
        m = rx.search(fetch.openalex_abstract(w))
        if m:
            hits += 1
            print(f"{w.get('publication_year')} {w.get('doi')} | {(w.get('title') or '')[:90]}\n    {m.group(0)}")
    print(f"{hits} of {len(res)} abstracts match")
    return 0


def abstract_for(doi):
    """(source, title, year, abstract) trying Crossref, then OpenAlex by DOI, then by title.

    THE TITLE FALLBACK CAN FIND A DIFFERENT WORK, so its source names the DOI
    OpenAlex matched and the caller must compare it with the one asked for.
    """
    m = fetch.crossref_work(doi)
    if m is None:
        return None
    title, year = (m.get("title") or [""])[0], _year(m)
    text = fetch.crossref_abstract(m)
    if text:
        return "crossref", title, year, text
    w = fetch.openalex_work(doi)
    text = fetch.openalex_abstract(w)
    if text:
        return "openalex", title, year, text
    if title:
        res = fetch.openalex_search(re.sub(r"[^\w\s]", " ", title)[:150], rows=5,
                                    field="title.search") or []
        for w in res:
            text = fetch.openalex_abstract(w)
            if text:
                return f"openalex title match {w.get('doi')}", title, year, text
    return "none", title, year, ""


def cmd_abstract(a):
    failed = 0
    for d in expand(a.doi):
        got = abstract_for(bare_doi(d))
        if got is None:
            print(f"FAILED {d}")
            failed += 1
            continue
        src, title, year, text = got
        print(f"\n### {d} | {year} | {title} | {src}\n{text[:a.chars] or 'NO ABSTRACT'}")
    return 1 if failed else 0


def cmd_works(a):
    """Crossref metadata, abstract and handle status for a DOI list, saved as JSON."""
    out, failed = {}, 0
    for d in expand(a.doi):
        d = bare_doi(d)
        m = fetch.crossref_work(d)
        handle = fetch.doi_handle(d)
        if m is None:
            failed += 1
            out[d] = {"error": "crossref lookup failed", "handle": handle}
            print(f"FAILED {d} | handle {handle}")
            continue
        out[d] = {"title": (m.get("title") or [""])[0],
                  "container": (m.get("container-title") or [""])[0],
                  "year": _year(m), "type": m.get("type"),
                  "volume": m.get("volume"), "issue": m.get("issue"), "page": m.get("page"),
                  "authors": [x.get("family", x.get("name", "")) for x in m.get("author", [])],
                  "abstract": fetch.crossref_abstract(m), "handle": handle}
        r = out[d]
        print(f"{d} | {r['year']} | {r['title'][:80]} | {','.join(r['authors'][:4])}"
              f" | abstract {len(r['abstract'])} | handle {handle}")
    with open(a.out, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False, sort_keys=True)
    print(f"{len(out)} works, {failed} failed, written to {a.out}")
    return 1 if failed else 0


# OpenAlex types that are not refereed research. Used as a screen, never as
# evidence of review, because OpenAlex types nearly everything `article`.
NOT_RESEARCH = {"editorial", "erratum", "letter", "paratext", "retraction", "peer-review", "other"}


def cmd_type(a):
    failed = 0
    for d in expand(a.doi):
        w = fetch.openalex_work(bare_doi(d))
        if w is None:
            print(f"FAILED {d}")
            failed += 1
            continue
        flag = "  <== NOT RESEARCH" if w.get("type") in NOT_RESEARCH else ""
        flag += "  <== RETRACTED" if w.get("is_retracted") else ""
        print(f"{d} | {w.get('type')} | crossref {w.get('type_crossref')}{flag}")
    return 1 if failed else 0


def main(argv):
    ap = argparse.ArgumentParser(prog="registry.py", description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("crossref", "openalex"):
        p = sub.add_parser(name)
        p.add_argument("query", nargs="+")
        p.add_argument("--rows", type=int, default=5)
        p.add_argument("--filter")
    p = sub.add_parser("grep-abstracts")
    p.add_argument("query")
    p.add_argument("regex")
    p.add_argument("--rows", type=int, default=25)
    p.add_argument("--width", type=int, default=200)
    p = sub.add_parser("abstract")
    p.add_argument("doi", nargs="+")
    p.add_argument("--chars", type=int, default=1600)
    p = sub.add_parser("works")
    p.add_argument("doi", nargs="+")
    p.add_argument("--out", required=True)
    p = sub.add_parser("type")
    p.add_argument("doi", nargs="+")
    a = ap.parse_args(argv[1:])
    if getattr(a, "rows", 1) < 1:
        ap.error("--rows must be positive")
    return {"crossref": cmd_crossref, "openalex": cmd_openalex, "grep-abstracts": cmd_grep_abstracts,
            "abstract": cmd_abstract, "works": cmd_works, "type": cmd_type}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
