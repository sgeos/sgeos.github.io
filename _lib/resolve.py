#!/usr/bin/env python3
"""Does a cited identifier RESOLVE, and if not, is that the citation's fault or the web's.

RELATIONSHIP TO `_verify_citations.py`. That script asks whether a DOI resolves to THE WORK IT
IS CITED AS, by comparing registry metadata against the citation text. It is the stronger
check and it is the one that catches a wrong identifier. This module asks the weaker and
different question of whether the identifier RESOLVES AT ALL from here, which catches a dead
landing page, a publisher that has dropped the record, and a transcription fault in whatever
pipeline wrote the file. Both are useful and neither subsumes the other.

WHY THIS EXISTS AS SHARED CODE. It was written three times as a throwaway script, most
recently as `tmp/a370/sweep.py`, and each rewrite had to rediscover the same two facts.

  AN HTTP FAILURE IS USUALLY NOT A CITATION FAILURE. Publishers run bot mitigation. IEEE
  answers 202, several others answer 403, and a Defense Technical Information Center deposit
  refuses the connection outright. On a 250-record sample of A370, 22 identifiers, being 8.8
  percent, failed by HTTP and every one was registered and correct. Treating those as broken
  citations would have condemned one reference in eleven.

  THE FALLBACK MUST BE A DIFFERENT ROUTE, NOT A RETRY. Asking the registry whether the record
  exists is independent evidence. Asking the publisher again is the same failing request.

AN HTTP 200 DOES NOT VERIFY A CITATION. It says an identifier exists. Use
`_verify_citations.py` for the question of whether it is the right one.
"""
import json
import os
import random
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import post  # noqa: E402

# 202 is IEEE's bot-mitigation answer and 403 is the same behaviour elsewhere. Both mean the
# request reached a server that chose not to serve a robot, which is not evidence about the
# identifier. 401 and 418 appear for the same reason.
ACCEPTED = frozenset({200, 202, 301, 302, 303, 307, 308, 401, 403, 418})

DOI_IN_URL = re.compile(r"doi\.org/(10\.[^\s>\"']+)", re.I)
DEF_LINE = re.compile(rf"^\[({post.ANCHOR})\]:\s*(\S+)\s*$", re.M)

UA = {"User-Agent": "Mozilla/5.0 (compatible) sgeos.github.io link check"}
CROSSREF = "https://api.crossref.org/works/"
DATACITE = "https://api.datacite.org/dois/"


def identifiers(text):
    """{anchor: url} for every reference definition whose URL carries a DOI."""
    out = {}
    for anchor, url in DEF_LINE.findall(text):
        if DOI_IN_URL.search(url):
            out[anchor] = url
    return out


def _head(url, timeout=25):
    req = urllib.request.Request(url, headers=UA, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return f"ERR {type(e).__name__}"


def _registry_has(doi, timeout=25, datacite=True):
    """Ask the issuing registry directly. A DIFFERENT ROUTE, not a retry of the same request.

    LIPIcs and some others deposit with DataCite, so a Crossref lookup returns nothing for a
    perfectly valid identifier. That artefact was mistaken for a bad citation once already.
    """
    quoted = urllib.parse.quote(doi, safe="")
    for base, ok in ((CROSSREF, lambda d: d.get("status") == "ok"),
                     (DATACITE, lambda d: "data" in d)):
        if base is DATACITE and not datacite:
            continue
        try:
            req = urllib.request.Request(base + quoted,
                                         headers={**UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                if ok(json.load(r)):
                    return True
        except Exception:
            continue
    return False


def check(url, timeout=25):
    """(resolved, route, status). `route` is 'http' or 'registry' or '' when unresolved."""
    status = _head(url, timeout)
    if isinstance(status, int) and status in ACCEPTED:
        return True, "http", status
    m = DOI_IN_URL.search(url)
    if m and _registry_has(m.group(1), timeout):
        return True, "registry", status
    return False, "", status


def sweep(text, sample=0, seed=None, timeout=25, on_result=None):
    """Check the identifiers in one post. `sample` of 0 checks all of them.

    `seed` is required when sampling, so a reviewer can reproduce exactly which records were
    checked. An unseeded sample is not a reproducible measurement.
    """
    found = identifiers(text)
    anchors = sorted(found)
    if sample and sample < len(anchors):
        if seed is None:
            raise ValueError("sampling needs a seed so the sample is reproducible")
        anchors = random.Random(seed).sample(anchors, sample)
    rows = []
    for a in anchors:
        resolved, route, status = check(found[a], timeout)
        rows.append({"anchor": a, "url": found[a], "resolved": resolved,
                     "route": route, "status": status})
        if on_result:
            on_result(rows[-1])
    return rows


def summarise(rows):
    """Counts a report can print without recomputing them."""
    total = len(rows)
    http = sum(1 for r in rows if r["route"] == "http")
    registry = sum(1 for r in rows if r["route"] == "registry")
    failed = [r for r in rows if not r["resolved"]]
    return {
        "total": total,
        "resolved": total - len(failed),
        "via_http": http,
        "via_registry": registry,
        # The figure worth reporting to a reader: how often clicking a reference fails even
        # though the citation is correct.
        "registry_only_fraction": (registry / total) if total else 0.0,
        "failed": failed,
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python3 _lib/resolve.py <post.markdown> [sample] [seed]")
        raise SystemExit(2)
    path = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    sd = int(sys.argv[3]) if len(sys.argv) > 3 else 20260811
    body = open(path, encoding="utf-8").read()

    def show(row):
        if not row["resolved"]:
            print(f"  FAIL {row['status']!s:>10}  {row['anchor']}  {row['url']}")
        elif row["route"] == "registry":
            print(f"  registry-only ({row['status']})  {row['anchor']}  {row['url']}")

    rows = sweep(body, sample=n, seed=sd, on_result=show)
    s = summarise(rows)
    print(f"{os.path.basename(path)}: {s['resolved']}/{s['total']} resolved, "
          f"{s['via_registry']} registry-only ({s['registry_only_fraction'] * 100:.1f} percent)")
    print("AN HTTP 200 DOES NOT VERIFY A CITATION. It says the identifier exists, not that it "
          "is the right one. Use _verify_citations.py for that.")
    raise SystemExit(1 if s["failed"] else 0)
