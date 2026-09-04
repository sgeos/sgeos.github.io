#!/usr/bin/env python3
"""Verify that a book citation's OpenLibrary work key is the book the article names.

WHY THIS EXISTS. A347 inherited a hand-written `BOOKS` list from A346, which had
inherited it from A345. Ten identifiers were checked against the repository for
the first time and NINE RESOLVED TO UNRELATED WORKS. `Leishman, Principles of
helicopter aerodynamics` pointed at `The 2007-2012 Outlook for Dark Rum in Japan`.
`Prouty, Helicopter performance, stability and control` pointed at a book about
buying apartment buildings. `Stepniewski and Keys, Rotary-wing aerodynamics`
pointed at `Rural modernization`.

WHY EVERY EXISTING CHECK PASSED. The link resolves, so a status check goes green.
The reference block is well formed, so `_verify.py` is satisfied. The rendered
page shows the label the article wrote, so `render.py` sees nothing. A citation
whose TEXT is right and whose TARGET is wrong is invisible to every check that
does not read the target, and this corpus had no check that read the target.

TWO CITATION STYLES LIVE IN THIS CORPUS AND ONLY ONE CAN BE CHECKED THIS WAY. The
generated style labels a book `Author Year`, which carries no title to compare
against and which came from a real lookup in the first place. The hand-written
style labels it `Author, Title`, which is the style that gets typed from memory
and therefore the style that goes wrong. `title_claim` returns None for the
first, and the caller is expected to skip it rather than to guess.

THE WORK JSON ENDPOINT CANNOT BE THE ORACLE, WHICH WAS LEARNED THE EXPENSIVE WAY
ON 2026-09-04. `https://openlibrary.org/works/<key>.json` returns HTTP 500 for
records that plainly exist. `OL17855977W` is Raymer's `Aircraft design, a
conceptual approach` and `OL5220705W` is Wooldridge's `Winged Wonders`, and both
returned `Internal Error` six times out of six while other keys returned 200 every
time. A NONEXISTENT KEY RETURNS 500 AS WELL. That endpoint therefore cannot
separate `this key is wrong` from `this record will not serve`, and the first
version of this module collapsed both into None and reported both as mismatches.
Running the A342 to A346 repair against that measurement would have REWRITTEN
CORRECT CITATIONS, which is the same failure as A348's transient book mismatch and
the same failure as the SSL error that nearly condemned 1,051 citations in A347.
The search index is the oracle instead. It answers numFound 1 with a title and an
author for a real key and numFound 0 for a bogus one, which is the discrimination
this needs, and it carries the AUTHOR, which the work record does not give without
a second request.

A FAILURE IS NEVER A VERDICT. `resolve` returns one of three states and `check`
reports four, so that `could not be determined` can never be read as `wrong`. That
distinction is the whole lesson of `_lib/survey.py` restated for a network oracle.

NETWORK. This reads openlibrary.org and therefore does NOT belong in `_verify.py`,
which is a build gate and runs offline. Run it separately, the way citation and
URL verification are run separately.
"""

import difflib
import json
import re
import time
import urllib.parse
import urllib.request

WORK_URL = re.compile(r"^https://openlibrary\.org/works/(OL\d+W)$")
DEFINITION = re.compile(r"^\[(book_[a-z0-9_]+)\]: (\S+)\s*$", re.M)
LABEL = re.compile(r"^- \[([^\]]+)\]\[(book_[a-z0-9_]+)\]$", re.M)
# An `Author Year` label ends in a four digit year, optionally after `et al`.
GENERATED_STYLE = re.compile(r"\b(1[89]|20)\d{2}\s*$")

USER_AGENT = "sgeos-blog-booklinks/1.0 (+https://sgeos.github.io/)"

#: The three states a lookup can end in. Only FOUND and ABSENT are verdicts.
FOUND, ABSENT, UNKNOWN = "found", "absent", "unknown"

#: The four states a citation can end in. Only WRONG and MISSING are defects.
OK, WRONG, MISSING, UNDETERMINED = "ok", "wrong", "missing", "undetermined"


def citations(text):
    """{anchor: (label, url)} for every book reference defined in an article."""
    labels = {anchor: label for label, anchor in LABEL.findall(text)}
    return {anchor: (labels.get(anchor, ""), url)
            for anchor, url in DEFINITION.findall(text)}


def title_claim(label):
    """The title an `Author, Title` label claims, or None if it claims none.

    A GENERATED `Author Year` LABEL CLAIMS NO TITLE AND MUST NOT BE GUESSED AT.
    Returning the author name here and comparing it to a title would report every
    correct generated citation as a mismatch, which is how the first version of
    this measurement over-reported by a factor of four.
    """
    label = (label or "").strip()
    if not label or GENERATED_STYLE.search(label):
        return None
    if "," not in label:
        return None
    claim = label.split(",", 1)[1].strip()
    return claim or None


def author_claim(label):
    """The surnames an `Author, Title` label leads with, as a list.

    Everything before the first comma, split on `and`, with initials and short
    connecting words dropped. Used to hold a key to BOTH halves of the claim, since
    two different books can carry near enough the same title.
    """
    head = (label or "").split(",", 1)[0]
    return [w for w in head.replace(" and ", " ").split() if len(w) > 2]


def work_key(url):
    """The OpenLibrary work key in a URL, or None if it is not one."""
    m = WORK_URL.match((url or "").strip())
    return m.group(1) if m else None


def resolve(key, opener=urllib.request.urlopen, timeout=40, tries=4):
    """(status, title, authors) for a work key, read from the SEARCH INDEX.

    Returns UNKNOWN rather than raising or guessing when the repository cannot be
    reached, so that a caller can refuse to conclude. A transient failure must not
    become a verdict: see the module docstring for the three occasions this corpus
    has paid for that lesson.
    """
    url = ("https://openlibrary.org/search.json?q="
           + urllib.parse.quote(f'key:"/works/{key}"')
           + "&fields=key,title,author_name&limit=1")
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with opener(req, timeout=timeout) as fh:
                docs = json.load(fh).get("docs") or []
            if not docs:
                return ABSENT, None, []
            return (FOUND, (docs[0].get("title") or "").strip(),
                    list(docs[0].get("author_name") or []))
        except Exception:                                     # noqa: BLE001
            if attempt + 1 < tries:
                time.sleep(1.5 * (attempt + 1))
    return UNKNOWN, None, []


def fetch_title(key, **kw):
    """The repository's title for a work key, or None. Kept for callers that only

    want the title. PREFER `resolve`, because this collapses `absent` and
    `unreachable` into the same None and a caller cannot tell them apart.
    """
    return resolve(key, **kw)[1]


def agrees(claim, title, threshold=0.45):
    """Whether a claimed title and a repository title are the same book.

    A RATIO RATHER THAN EQUALITY, because the corpus writes `Bramwell's helicopter
    dynamics` where the repository writes `Bramwell's Helicopter Dynamics`, and
    writes `Aerodynamics, aeronautics and flight mechanics` against a repository
    record carrying an extra comma. The threshold is set where the observed
    correct pairs and the observed wrong pairs separate cleanly, the worst correct
    pair measuring 0.78 and the best wrong pair 0.40.
    """
    if not claim or not title:
        return False
    a = re.sub(r"[^a-z0-9 ]+", " ", claim.lower())
    b = re.sub(r"[^a-z0-9 ]+", " ", title.lower())
    a, b = " ".join(a.split()), " ".join(b.split())
    if a in b or b in a:
        return True
    return difflib.SequenceMatcher(None, a, b).ratio() >= threshold


def author_agrees(label, authors):
    """Whether a surname the label leads with appears among the repository authors.

    REPORTED AND NOT ENFORCED. The repository writes `E. T. Wooldridge` where the
    article writes `Wooldridge`, writes editors where the article writes authors,
    and sometimes lists nobody at all, so a disagreement here is a thing to read
    rather than a thing to act on.
    """
    blob = " ".join(authors or []).lower()
    words = author_claim(label)
    return any(w.lower() in blob for w in words) if words else False


def check(text, lookup=resolve):
    """[(anchor, claim, title, verdict)] for the checkable citations in an article.

    `verdict` is one of OK, WRONG, MISSING or UNDETERMINED. UNDETERMINED means the
    repository could not be reached and NOTHING IS CONCLUDED, and a caller that
    treats it as a defect has reintroduced the bug this module was rewritten for.

    Citations in the generated `Author Year` style are omitted entirely rather
    than reported as passing, so a caller cannot mistake `not checked` for `checked
    and correct`. That distinction is the whole lesson of `_lib/survey.py`.
    """
    out = []
    for anchor, (label, url) in sorted(citations(text).items()):
        claim = title_claim(label)
        key = work_key(url)
        if claim is None or key is None:
            continue
        status, title, _authors = lookup(key)
        if status == UNKNOWN:
            verdict = UNDETERMINED
        elif status == ABSENT:
            verdict = MISSING
        else:
            verdict = OK if agrees(claim, title) else WRONG
        out.append((anchor, claim, title, verdict))
    return out
