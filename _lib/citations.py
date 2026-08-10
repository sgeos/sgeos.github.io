#!/usr/bin/env python3
"""Citation verification. Thirteen `url_check.py` copies and six `verify_urls.py`.

AN HTTP 200 DOES NOT VERIFY A CITATION. It says a document exists at an address,
not that it is the document claimed. The failure mode this module exists to
catch is a REACHABLE IDENTIFIER POINTING AT THE WRONG WORK, which no
reachability check can see. A369 documented four of ninety-one identifiers
supplied from memory resolving to entirely different papers, every one of which
would have passed a link check.

THE DISTINCTION THAT DECIDES WHICH CHECK APPLIES.

  RECALLED identifiers, typed from memory, can be paired with a title they do
  not belong to. They need `verify_doi`, which compares the registry's author
  and year against what the anchor claims.

  RETRIEVED identifiers, taken from a search response, carry identifier and
  metadata from one record, so the substitution failure is not available by
  construction. They need only resolvability, and `sample_resolvable` checks a
  random subset because checking thousands is slow and buys little.

That distinction is a structural guarantee rather than a verified one, and
saying so is part of using it honestly.

BOT DETECTION IS NOT A DEAD LINK. Several publishers return 403 to any
scripted request while being perfectly well indexed. `BOT_DETECTED` lists the
ones this corpus has confirmed, so their responses are reported as inconclusive
instead of as failures.
"""

import collections
import random
import re
import sys
import os
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fetch  # noqa: E402
import refs  # noqa: E402

# Hosts confirmed to refuse scripted requests while being properly indexed.
# Verified by web search at the time each was added; a 403 from these is
# inconclusive, not a failure.
BOT_DETECTED = (
    "researchgate.net", "mdpi.com", "sciencedirect.com", "ssrn.com",
    "academic.oup.com", "phys.org", "crates.io", "npmjs.com", ".mil",
    "tandfonline.com", "springer.com", "wiley.com", "jstor.org",
)

# Endpoints that return 200 for a query matching nothing, so a citation
# pointing at one is unverified even when it responds.
SEARCH_ENDPOINTS = ("openlibrary.org/search", "ntrs.nasa.gov/api/citations/search",
                    "google.com/search", "worldcat.org/search")


def fold(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = (s.replace("ı", "i").replace("ø", "o").replace("đ", "d")
           .replace("ł", "l").replace("ß", "ss").replace("æ", "ae").replace("œ", "oe"))
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def definitions(text):
    """Anchor to URL, from a post's reference block."""
    refs = text.split("## References", 1)[1] if "## References" in text else text
    return dict(re.findall(r"(?m)^\[([A-Za-z0-9_-]+)\]:\s*(\S+)$", refs))


def claimed_from_anchor(anchor):
    """(surname, year) an anchor asserts. Delegates to the single parser."""
    _kind, surname, year = refs.parse_anchor(anchor)
    return surname, year


def verify_doi(anchor, url, year_slack=1):
    """Compare the registry record against what the anchor claims.

    Returns a dict with `status` in ok, mismatch, unresolved, not-a-doi.

    THE FOLDING MATTERS. Naive ASCII stripping turns `Slavík` into `slavk` and
    `Böhm` into `bhm`, which produced three false mismatches in an A369 run and
    read as citation defects until it was fixed.
    """
    if "doi.org" not in url:
        return {"anchor": anchor, "url": url, "status": "not-a-doi"}
    doi = url.split("doi.org/", 1)[1]
    msg = fetch.crossref_work(doi)
    if not msg:
        return {"anchor": anchor, "url": url, "status": "unresolved"}
    title, authors, year, venue = fetch.crossref_fields(msg)
    surname, want_year = claimed_from_anchor(anchor)
    author_ok = (not authors) or (not surname) or any(surname in fold(a) for a in authors)
    year_ok = (want_year is None) or (year is None) or abs(want_year - year) <= year_slack
    return {"anchor": anchor, "url": url, "title": title, "authors": authors,
            "year": year, "venue": venue,
            "status": "ok" if (author_ok and year_ok) else "mismatch",
            "author_ok": author_ok, "year_ok": year_ok}


def verify_all_dois(text, progress=None):
    """Exhaustive registry check of every DOI a post cites."""
    out = []
    defs = definitions(text)
    for i, (anchor, url) in enumerate(sorted(defs.items())):
        r = verify_doi(anchor, url)
        out.append(r)
        if progress:
            progress(i + 1, len(defs), r)
    return out


def sample_resolvable(urls, n=120, seed=20260806):
    """Resolvability of a random subset. For retrieved identifiers.

    Reports what it sampled, because a silent subset reads as full coverage.
    """
    urls = sorted(set(urls))
    rng = random.Random(seed)
    pick = rng.sample(urls, min(n, len(urls)))
    rows = []
    for u in pick:
        host_ok = not any(h in u for h in BOT_DETECTED)
        ok = fetch.resolves(u)
        rows.append({"url": u, "resolves": ok,
                     "status": "ok" if ok else ("inconclusive" if not host_ok else "failed")})
    return {"sampled": len(pick), "of": len(urls), "rows": rows,
            "failed": [r for r in rows if r["status"] == "failed"],
            "inconclusive": [r for r in rows if r["status"] == "inconclusive"]}


def search_endpoint_citations(text):
    """Citations pointing at a search URL, which verify nothing."""
    return {a: u for a, u in definitions(text).items()
            if any(s in u for s in SEARCH_ENDPOINTS)}


def summarise(results):
    c = collections.Counter(r["status"] for r in results)
    return {"total": len(results), **dict(sorted(c.items())),
            "mismatches": [r for r in results if r["status"] == "mismatch"],
            "unresolved": [r for r in results if r["status"] == "unresolved"]}
