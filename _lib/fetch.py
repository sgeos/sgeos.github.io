#!/usr/bin/env python3
"""One HTTP client for literature sweeps, replacing ninety hand-rolled copies.

WHY. A survey of the scratch tooling found 90 files defining their own retry
loop and 121 defining their own User-Agent, against 0 files carrying the
doubled-backslash guard. The mechanism was copied everywhere and the lessons
nowhere. This module is the mechanism, so the next fix has one place to land.

The dominant convention across the copies was `def get(url, tries=4)` returning
parsed JSON or None, and that convention is preserved deliberately so migrating
a script is a rename rather than a rewrite.

RETURNING NONE RATHER THAN RAISING is the existing convention and is kept, but
it is a real hazard: a caller that forgets to test the result silently harvests
nothing and reports success. `get_json_strict` raises instead, and sweep code
that cannot tolerate a silent empty result should use it.

POLITENESS IS NOT OPTIONAL. Crossref gives faster and more reliable service to
requests carrying a contact address, and NTRS and OSTI will throttle a client
that hammers them. MIN_INTERVAL enforces a floor between calls to one host.
"""

import json
import time
import urllib.error
import urllib.parse
import urllib.request

CONTACT = "sgeos@hotmail.com"
UA = {"User-Agent": f"blog-research/1.0 (mailto:{CONTACT})"}

DEFAULT_TIMEOUT = 45
DEFAULT_TRIES = 4
MIN_INTERVAL = 0.34  # seconds between calls to the same host

_last_call = {}


def _host(url):
    return urllib.parse.urlsplit(url).netloc


def _throttle(url):
    h = _host(url)
    now = time.monotonic()
    wait = MIN_INTERVAL - (now - _last_call.get(h, 0.0))
    if wait > 0:
        time.sleep(wait)
    _last_call[h] = time.monotonic()


def get_bytes(url, tries=DEFAULT_TRIES, timeout=DEFAULT_TIMEOUT, headers=None):
    """Raw fetch with exponential backoff. Returns bytes, or None if all tries fail.

    A 404 is not retried, because it will not become a 200. Everything else is,
    including the 403s that bot-detecting hosts return intermittently.
    """
    hdrs = dict(UA)
    if headers:
        hdrs.update(headers)
    for i in range(tries):
        _throttle(url)
        try:
            req = urllib.request.Request(url, headers=hdrs)
            return urllib.request.urlopen(req, timeout=timeout).read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if i == tries - 1:
                return None
            time.sleep(2 ** i + 1)
        except Exception:
            if i == tries - 1:
                return None
            time.sleep(2 ** i + 1)
    return None


def get_json(url, **kw):
    """Parsed JSON, or None. The convention the existing scripts already use."""
    raw = get_bytes(url, **kw)
    if raw is None:
        return None
    try:
        return json.loads(raw)
    except ValueError:
        return None


def get_json_strict(url, **kw):
    """Parsed JSON, raising on failure, for callers that must not silently no-op."""
    out = get_json(url, **kw)
    if out is None:
        raise RuntimeError(f"fetch failed: {url}")
    return out


def resolves(url, **kw):
    """Whether a URL fetches at all. NOT evidence that a citation is correct.

    An HTTP 200 says a document exists at an address. It says nothing about
    whether it is the document claimed. Use crossref_work and compare the
    resolved title and authors for that.
    """
    return get_bytes(url, **kw) is not None


# ---------------------------------------------------------------- Crossref

CROSSREF = "https://api.crossref.org/works"


def crossref_search(query, rows=50, filters=None, **kw):
    """Bibliographic search. Returns the item list, possibly empty."""
    params = {"query.bibliographic": query, "rows": str(rows), "mailto": CONTACT}
    if filters:
        params["filter"] = filters
    j = get_json(f"{CROSSREF}?{urllib.parse.urlencode(params)}", **kw)
    return ((j or {}).get("message", {}) or {}).get("items", []) or []


def crossref_work(doi, **kw):
    """One work by digital object identifier, or None.

    Do NOT append a `select` parameter to this endpoint. It returns HTTP 400,
    which cost a full verification run that reported 120 of 120 identifiers
    unresolved when every one of them was fine.
    """
    doi = doi.replace("https://doi.org/", "").strip()
    j = get_json(f"{CROSSREF}/{urllib.parse.quote(doi)}", **kw)
    return (j or {}).get("message")


def crossref_fields(msg):
    """Normalised (title, authors, year, venue) from a Crossref message."""
    if not msg:
        return "", [], None, ""
    title = (msg.get("title") or [""])[0]
    authors = [a.get("family", "") for a in (msg.get("author") or []) if a.get("family")]
    parts = (msg.get("issued", {}) or {}).get("date-parts") or [[None]]
    year = (parts[0] or [None])[0]
    venue = ((msg.get("container-title") or [""]) or [""])[0]
    return title, authors, year, venue


# ---------------------------------------------------------------- NTRS

NTRS_SEARCH = "https://ntrs.nasa.gov/api/citations/search"
NTRS_DETAIL = "https://ntrs.nasa.gov/api/citations"


# **THE PAGE SIZE IS TEN AND THE SERVER WILL NOT BUDGE, BUT THE OFFSET WORKS AND THE
# SPELLING MATTERS.** Passing `page` as a JSON object, which this module did from A317
# until A360, gets the size clamped to ten AND THE OFFSET SILENTLY IGNORED, so every
# request returns the same first ten records however deep you ask. Passing `page[size]`
# and `page[from]` as separate query parameters is honoured. A360 measured the query
# `plug nozzle` at 242 matching records, of which the old call returned 10 and the new one
# returns all 242 with no duplicates. **Every literature sweep in this corpus has been
# taking the top ten of each reports-server query and leaving the rest**, which is why the
# reports fraction has been the recurring complaint of every primary-reference pass.
NTRS_PAGE = 10          # the server's hard page size, measured rather than documented


def ntrs_search(query, rows=25, **kw):
    """NASA Technical Reports Server search, paginated to `rows`.

    Returns up to `rows` records, walking the server's ten-record pages. It returns
    NEITHER AUTHORS NOR YEAR, which is why `ntrs_detail` exists and why link text built
    from search results alone produced labels such as "Tests of the".

    **THE LOOP IS BOUNDED BY `rows` AND BY A REPEATED PAGE.** A server that ignored the
    offset would return the same page for ever, which is exactly the defect this function
    was written to fix, so an offset that yields nothing new stops the walk rather than
    spinning.
    """
    out, seen = [], set()
    for frm in range(0, max(rows, 1), NTRS_PAGE):        # bound: rows / 10 requests
        url = (f"{NTRS_SEARCH}?q={urllib.parse.quote(query)}"
               f"&page%5Bsize%5D={NTRS_PAGE}&page%5Bfrom%5D={frm}")
        j = get_json(url, **kw)
        page = (j or {}).get("results", []) or []
        fresh = [r for r in page if r.get("id") not in seen]
        if not fresh:
            break
        for r in fresh:
            seen.add(r.get("id"))
            out.append(r)
            if len(out) >= rows:
                return out
    return out


def ntrs_total(query, **kw):
    """How many records the reports server says it holds for a query.

    **THE SERVER REPORTS ITS OWN TOTAL AND NOTHING WAS READING IT.** That number is what
    turns a sweep's coverage from a guess into a measurement, because it says how much of
    each question was left on the server.
    """
    url = (f"{NTRS_SEARCH}?q={urllib.parse.quote(query)}"
           f"&page%5Bsize%5D=1&page%5Bfrom%5D=0")
    j = get_json(url, **kw)
    return int(((j or {}).get("stats") or {}).get("total") or 0)


def ntrs_detail(record_id, **kw):
    """Authors, year and title for one NTRS record."""
    j = get_json(f"{NTRS_DETAIL}/{urllib.parse.quote(str(record_id))}", **kw)
    if not j:
        return {}
    authors = [a.get("meta", {}).get("author", {}).get("name", "") or a.get("name", "")
               for a in (j.get("authorAffiliations") or [])]
    pubs = j.get("publications") or [{}]
    date = (pubs[0] or {}).get("publicationDate") or ""
    return {"title": j.get("title", ""),
            "authors": [a for a in authors if a],
            "year": date[:4] if date[:4].isdigit() else "",
            "url": f"https://ntrs.nasa.gov/citations/{record_id}"}


# ---------------------------------------------------------------- other sources

def dtic_search(query, rows=50, **kw):
    """Defense Technical Information Center reports, reachable through Crossref."""
    return crossref_search(query, rows=rows, filters="prefix:10.21236", **kw)


def osti_search(query, rows=50, **kw):
    """Department of Energy technical reports."""
    params = {"q": query, "rows": str(rows)}
    j = get_json(f"https://www.osti.gov/api/v1/records?{urllib.parse.urlencode(params)}", **kw)
    return j if isinstance(j, list) else []


def openlibrary_search(query, limit=20, **kw):
    """Books.

    The search endpoint returns HTTP 200 for any query including one that
    matches nothing, so a citation pointing at a SEARCH URL is unverified even
    when it responds. Resolve to a work or edition identifier before citing.
    """
    params = {"q": query, "limit": str(limit)}
    j = get_json(f"https://openlibrary.org/search.json?{urllib.parse.urlencode(params)}", **kw)
    return (j or {}).get("docs", []) or []
