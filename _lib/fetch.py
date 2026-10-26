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
import os
import time
import urllib.error
import urllib.parse
import urllib.request

# A contact address is sent to registries only when the operator opts in through BLOG_CONTACT_EMAIL.
# The default sends none, so no personal address leaves the machine unless someone chooses to send it.
CONTACT = os.environ.get("BLOG_CONTACT_EMAIL", "").strip()
# WIKIMEDIA'S POLICY asks a client to name a way to reach its operator, and a bare
# `blog-research/1.0` drew 429 for four requests in five on 2026-10-26. The blog's own
# address is that way, as `booklinks.py` gives it; no email is ever sent.
UA = {"User-Agent": f"blog-research/1.0 (mailto:{CONTACT})" if CONTACT else
      "blog-research/1.0 (+https://sgeos.github.io/)"}

DEFAULT_TIMEOUT = 45
DEFAULT_TRIES = 4
MIN_INTERVAL = 0.34  # seconds between calls to the same host
# Hosts that throttle harder. Wikipedia answered 429 to pins at 0.34 s on 2026-10-24.
HOST_INTERVAL = {"en.wikipedia.org": 1.0, "www.osti.gov": 1.0, "web.archive.org": 2.5}  # OSTI refused 1,136 of 1,937 at 0.34 s

_last_call = {}


def _host(url):
    return urllib.parse.urlsplit(url).netloc


def _throttle(url):
    h = _host(url)
    now = time.monotonic()
    wait = HOST_INTERVAL.get(h, MIN_INTERVAL) - (now - _last_call.get(h, 0.0))
    if wait > 0:
        time.sleep(wait)
    _last_call[h] = time.monotonic()


def _retry_after(err, attempt):
    """Seconds to wait after a refusal: the server's Retry-After, at most a minute, else backoff."""
    try:
        return min(60, max(1, int(err.headers.get("Retry-After"))))
    except (TypeError, ValueError):
        return 2 ** attempt + 1


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
            time.sleep(_retry_after(e, i))
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


def get_json_status(url, tries=DEFAULT_TRIES, timeout=DEFAULT_TIMEOUT, headers=None):
    """(parsed JSON or None, last HTTP status or None).

    WHY. `get_json` answers None both for a record that does not exist and for a
    server that refused or timed out, and a cache that wrote a `missing` marker on
    every None recorded 115 of 186 OSTI records as absent when the server was
    only throttling. Only a 404 is evidence of absence.
    """
    hdrs = dict(UA)
    if headers:
        hdrs.update(headers)
    status = None
    for i in range(tries):
        _throttle(url)
        try:
            req = urllib.request.Request(url, headers=hdrs)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                status = r.status
                try:
                    return json.loads(r.read()), status
                except ValueError:
                    return None, status
        except urllib.error.HTTPError as e:
            status = e.code
            if e.code == 404:
                return None, 404
            if i < tries - 1:
                time.sleep(_retry_after(e, i))
            continue
        except Exception:
            status = None
        if i < tries - 1:
            time.sleep(2 ** i + 1)
    return None, status


def get_bytes_status(url, tries=DEFAULT_TRIES, timeout=DEFAULT_TIMEOUT, headers=None):
    """(bytes or None, last HTTP status or None), so that only a 404 is read as absence.

    The bytes counterpart of `get_json_status`, for a page cache that must tell an
    archive with no capture, which answers 404, from one that refused.
    """
    import http.client
    hdrs = dict(UA)
    if headers:
        hdrs.update(headers)
    status = None
    for i in range(tries):
        _throttle(url)
        try:
            req = urllib.request.Request(url, headers=hdrs)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                try:
                    return r.read(), r.status
                except http.client.IncompleteRead as e:
                    # AN ARCHIVE CAPTURE REPLAYS THE ORIGINAL `Content-Length`, which need
                    # not match what is served, so every read of it raised. What arrived
                    # holds the page's head, which is what a metadata reader needs.
                    return e.partial, r.status
        except urllib.error.HTTPError as e:
            status = e.code
            if e.code == 404:
                return None, 404
            if i < tries - 1:
                time.sleep(_retry_after(e, i))
            continue
        except Exception:
            status = None
        if i < tries - 1:
            time.sleep(2 ** i + 1)
    return None, status


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
    params = {"query.bibliographic": query, "rows": str(rows)}
    if CONTACT:
        params["mailto"] = CONTACT
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


def crossref_works(dois, **kw):
    """{doi: message} for up to about a hundred DOIs in one request, or None on failure.

    WHY. One request per DOI took hours for the 39,000 identifiers of the
    harvested surveys. Crossref ORs repeated `doi:` filters, so one request
    returns many works. A DOI absent from the reply is absent from the dict,
    and the caller fetches it singly, since a filter can miss a DOI whose case
    or encoding the index normalises differently. A DOI containing a comma
    cannot be filtered and must be fetched singly.
    """
    dois = [d for d in dois if "," not in d]
    if not dois:
        return {}
    params = {"filter": ",".join(f"doi:{d}" for d in dois), "rows": str(len(dois))}
    if CONTACT:
        params["mailto"] = CONTACT
    j = get_json(f"{CROSSREF}?{urllib.parse.urlencode(params)}", **kw)
    if j is None:
        return None
    return {it["DOI"].lower(): it for it in (j.get("message") or {}).get("items") or []}


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


# ---------------------------------------------------------------- OpenAlex

OPENALEX = "https://api.openalex.org/works"


def openalex_search(query, rows=25, filters=None, select=None, field="search", **kw):
    """OpenAlex works matching `query`, or None on failure.

    `field` is `search` for the full-text index, or a filter such as
    `title_and_abstract.search` or `title.search`, which is folded into the
    filter list. NONE, NOT AN EMPTY LIST, ON FAILURE, so a caller can tell a
    query that matched nothing from one that never ran.
    """
    params = {"per-page": str(rows)}
    flt = [filters] if filters else []
    if field == "search":
        params["search"] = query
    else:
        flt.append(f"{field}:{query}")
    if flt:
        params["filter"] = ",".join(flt)
    if select:
        params["select"] = select
    j = get_json(f"{OPENALEX}?{urllib.parse.urlencode(params)}", **kw)
    return None if j is None else (j.get("results") or [])


def openalex_work(doi, **kw):
    """One OpenAlex work by digital object identifier, or None."""
    doi = doi.replace("https://doi.org/", "").strip()
    return get_json(f"{OPENALEX}/doi:{urllib.parse.quote(doi, safe='/()')}", **kw)


def openalex_abstract(work):
    """Plain abstract text rebuilt from OpenAlex's inverted index, or ''.

    OpenAlex stores each word with the positions it occupies. Twenty scratch
    scripts rebuilt the text with the same one-line sort, which is this.
    """
    ii = (work or {}).get("abstract_inverted_index") or {}
    return " ".join(w for _, w in sorted((p, w) for w, ps in ii.items() for p in ps))


def crossref_abstract(msg):
    """Crossref's abstract with its JATS markup removed, or ''."""
    import re
    text = re.sub(r"<[^>]+>", " ", (msg or {}).get("abstract", "") or "")
    return re.sub(r"\s+", " ", text).strip()


def doi_handle(doi, **kw):
    """The Handle System response code for a DOI, 1 when it is registered.

    This asks the registry directly rather than following the publisher's
    landing page, which bot detection often blocks. It says the identifier
    exists, not that it names the work it is cited for.
    """
    doi = doi.replace("https://doi.org/", "").strip()
    j = get_json(f"https://doi.org/api/handles/{urllib.parse.quote(doi, safe='/()')}", **kw)
    return None if j is None else j.get("responseCode")


# ---------------------------------------------------------------- Wikipedia

WIKIPEDIA_API = "https://en.wikipedia.org/w/api.php"


def wikipedia_revision(title, before=None, oldid=None, content=True, **kw):
    """One revision of an English Wikipedia article with its wikitext, or None.

    With `oldid`, that revision. With `before`, an ISO 8601 timestamp, the
    last revision at or before it, which is how a citation is pinned to the
    text that was read. With neither, the current revision. Returns a dict of
    `page_title`, `oldid`, `timestamp` and `content`. Redirects are followed,
    so `page_title` may differ from `title`.
    """
    # WITHOUT `content` only the id and timestamp are asked for, which is all a
    # dated pin needs and a small fraction of the bytes.
    q = {"action": "query", "format": "json", "formatversion": "2", "prop": "revisions",
         "rvprop": "ids|timestamp|content" if content else "ids|timestamp", "rvslots": "main"}
    if oldid:
        q["revids"] = str(oldid)
    else:
        q.update({"titles": title, "redirects": "1", "rvlimit": "1"})
        if before:
            q.update({"rvdir": "older", "rvstart": before})
    j = get_json(f"{WIKIPEDIA_API}?{urllib.parse.urlencode(q)}", **kw)
    pages = ((j or {}).get("query") or {}).get("pages") or []
    if not pages or not pages[0].get("revisions"):
        return None
    rev = pages[0]["revisions"][0]
    return {"page_title": pages[0]["title"], "oldid": rev["revid"], "timestamp": rev["timestamp"],
            "content": rev["slots"]["main"]["content"] if content else None}
