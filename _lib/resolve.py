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

WITH `--body`, every http(s) reference definition is read, not only the DOI ones.
The not-found pages are hand-written publisher and agency addresses and carry no
DOI, so a DOI-only sweep never sees them. A not-found page served under status
200 does not count as resolution. A DOI the registry holds still resolves, by
the registry route. Without the option the sweep stays DOI-only and does not
read bodies. A NOT-FOUND-BODY row is a page to read, not a verdict.
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


def identifiers(text, all_urls=False):
    """{anchor: url} for reference definitions.

    The default keeps a definition whose URL carries a DOI. That is whether an
    identifier resolves. `all_urls` keeps every http(s) definition instead.
    `--body` needs the wider set. The not-found pages are hand-written publisher
    and agency addresses, and a DOI landing is not one of them. A `mailto:` link
    is neither.
    """
    out = {}
    for anchor, url in DEF_LINE.findall(text):
        if all_urls:
            if url.startswith(("http://", "https://")):
                out[anchor] = url
        elif DOI_IN_URL.search(url):
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


# urlcheck.py in A364 and A365 reads the first 4000 characters of a successful
# response. A page-level phrase matches anywhere in that opening. A bare
# "not found" matches only a short title, h1 or first line. The scratch
# alternation also matches ordinary prose, and the A362 copy of the same family
# had already flagged real pages with an unbounded proxy.
_OPENING = 4000
_PAGE_PHRASE = re.compile(r"page not found|404 not found", re.I)
_TITLE = re.compile(r"<(title|h1)\b[^>]*>(.*?)</\1>", re.I | re.S)
_TAG = re.compile(r"<[^>]+>")
_SOFT_TITLE = frozenset({
    "not found",
    "404",
    "404 not found",
    "404 error",
    "page not found",
    "under maintenance",
})


def _plain(fragment):
    return re.sub(r"\s+", " ", _TAG.sub(" ", fragment)).strip()


def _soft_heading(inner):
    """A short title or first line that is the page's own not-found notice."""
    low = _plain(inner).lower()
    if not low or len(low) > 80:
        return False
    if "page not found" in low or "404 not found" in low or "under maintenance" in low:
        return True
    head = re.split(r"\s+[|–—-]\s+", low, maxsplit=1)[0].strip()
    if head in _SOFT_TITLE:
        return True
    return low.startswith("404 ") and "not found" in low


def not_found_body(text):
    """True when the opening of a successful response is a not-found page.

    Empty input is not that page. A sentence that merely contains the words
    "not found" is not that page either.
    """
    if not text:
        return False
    head = text[:_OPENING]
    if _PAGE_PHRASE.search(head):
        return True
    if any(_soft_heading(m.group(2)) for m in _TITLE.finditer(head)):
        return True
    first = next((ln.strip() for ln in head.splitlines() if ln.strip()), "")
    return _soft_heading(first)


def decide(status, opening, registered):
    """(resolved, route) from a status, an optional body and a registry answer.

    `opening` is None when the body was not read. It is consulted only for a
    200. A not-found page is not HTTP resolution. A DOI the registry holds
    still resolves, by the registry route.
    """
    soft = opening is not None and status == 200 and not_found_body(opening)
    if isinstance(status, int) and status in ACCEPTED and not soft:
        return True, "http"
    if registered:
        return True, "registry"
    return False, ""


def _get_opening(url, timeout=25):
    """The first 4000 characters of a GET that returned 200, else None.

    None leaves the HEAD result standing. A transport failure is not evidence
    that the page is missing, and a GET that answers with some other status is
    not the case this check classifies.
    """
    req = urllib.request.Request(url, headers=UA, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            if r.status != 200:
                return None
            return r.read(_OPENING).decode("utf-8", "replace")
    except Exception:
        return None


def check(url, timeout=25, *, read_body=False):
    """(resolved, route, status). `route` is 'http' or 'registry' or '' when unresolved.

    `read_body` GETs the opening of an HTTP 200 and applies `not_found_body`.
    The default leaves the status check unchanged.
    """
    status = _head(url, timeout)
    opening = _get_opening(url, timeout) if read_body and status == 200 else None
    soft = opening is not None and not_found_body(opening)
    registered = False
    if not (isinstance(status, int) and status in ACCEPTED and not soft):
        m = DOI_IN_URL.search(url)
        if m:
            registered = _registry_has(m.group(1), timeout)
    resolved, route = decide(status, opening, registered)
    return resolved, route, status


def sweep(text, sample=0, seed=None, timeout=25, on_result=None, read_body=False):
    """Check the identifiers in one post. `sample` of 0 checks all of them.

    `seed` is required when sampling, so a reviewer can reproduce exactly which records were
    checked. An unseeded sample is not a reproducible measurement. `read_body` widens the
    selection from DOI definitions to every http(s) reference definition.
    """
    found = identifiers(text, all_urls=read_body)
    anchors = sorted(found)
    if sample and sample < len(anchors):
        if seed is None:
            raise ValueError("sampling needs a seed so the sample is reproducible")
        anchors = random.Random(seed).sample(anchors, sample)
    rows = []
    for a in anchors:
        resolved, route, status = check(found[a], timeout, read_body=read_body)
        row = {"anchor": a, "url": found[a], "resolved": resolved,
               "route": route, "status": status}
        # A 200 is in ACCEPTED, so the only way it fails the HTTP route after a
        # body was requested is that the opening was a not-found page.
        if read_body and status == 200 and route != "http":
            row["body"] = "not-found"
        rows.append(row)
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


def _usage():
    print("usage: python3 _lib/resolve.py <post.markdown> [sample] [seed] [--body]")
    print("  default  DOI-bearing reference definitions only, status check")
    print("  --body   every http(s) reference definition; GET the opening of each HTTP 200")
    print("           and reject a not-found page. A NOT-FOUND-BODY row is a page to read,")
    print("           not a verdict that the citation is wrong.")


def main(argv):
    """Status check of DOI definitions. `--body` also reads hand-written http(s) URLs."""
    args = [a for a in argv[1:] if a != "--body"]
    read_body = "--body" in argv[1:]
    if any(a in ("-h", "--help") for a in argv[1:]):
        _usage()
        return 0
    if not args:
        _usage()
        return 2
    path = args[0]
    n = int(args[1]) if len(args) > 1 else 0
    sd = int(args[2]) if len(args) > 2 else 20260811
    body = open(path, encoding="utf-8").read()

    def show(row):
        if row.get("body") == "not-found" and not row["resolved"]:
            print(f"  NOT-FOUND-BODY {row['status']!s:>6}  {row['anchor']}  {row['url']}")
        elif row.get("body") == "not-found":
            print(f"  not-found body, registry-only ({row['status']})  "
                  f"{row['anchor']}  {row['url']}")
        elif not row["resolved"]:
            print(f"  FAIL {row['status']!s:>10}  {row['anchor']}  {row['url']}")
        elif row["route"] == "registry":
            print(f"  registry-only ({row['status']})  {row['anchor']}  {row['url']}")

    rows = sweep(body, sample=n, seed=sd, read_body=read_body, on_result=show)
    s = summarise(rows)
    print(f"{os.path.basename(path)}: {s['resolved']}/{s['total']} resolved, "
          f"{s['via_registry']} registry-only ({s['registry_only_fraction'] * 100:.1f} percent)")
    print("AN HTTP 200 DOES NOT VERIFY A CITATION. It says the identifier exists, not that it "
          "is the right one. Use _verify_citations.py for that.")
    if read_body:
        print("A 200 WHOSE BODY IS A NOT-FOUND PAGE IS NOT RESOLUTION. --body read every "
              "http(s) reference, not only DOIs. A NOT-FOUND-BODY row is a page to read, "
              "not a verdict.")
    return 1 if s["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
