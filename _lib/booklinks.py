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

THE MEASURED SCOPE WHEN THIS WAS WRITTEN, on 2026-09-02, was 510 distinct work
keys across 40 files. Of the 215 distinct keys carrying a title-style label, 19
disagreed with the repository, and EVERY ONE WAS IN AN UNPUBLISHED DRAFT. That is
luck rather than process, and it is the reason this module exists.

TWO CITATION STYLES LIVE IN THIS CORPUS AND ONLY ONE CAN BE CHECKED THIS WAY. The
generated style labels a book `Author Year`, which carries no title to compare
against and which came from a real lookup in the first place. The hand-written
style labels it `Author, Title`, which is the style that gets typed from memory
and therefore the style that goes wrong. `title_claim` returns None for the
first, and the caller is expected to skip it rather than to guess.

NETWORK. This reads openlibrary.org and therefore does NOT belong in `_verify.py`,
which is a build gate and runs offline. Run it separately, the way citation and
URL verification are run separately.
"""

import difflib
import json
import re
import urllib.request

WORK_URL = re.compile(r"^https://openlibrary\.org/works/(OL\d+W)$")
DEFINITION = re.compile(r"^\[(book_[a-z0-9_]+)\]: (\S+)\s*$", re.M)
LABEL = re.compile(r"^- \[([^\]]+)\]\[(book_[a-z0-9_]+)\]$", re.M)
# An `Author Year` label ends in a four digit year, optionally after `et al`.
GENERATED_STYLE = re.compile(r"\b(1[89]|20)\d{2}\s*$")


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


def work_key(url):
    """The OpenLibrary work key in a URL, or None if it is not one."""
    m = WORK_URL.match((url or "").strip())
    return m.group(1) if m else None


def fetch_title(key, opener=urllib.request.urlopen, timeout=20):
    """The repository's title for a work key, or None if it does not resolve."""
    try:
        with opener(f"https://openlibrary.org/works/{key}.json", timeout=timeout) as fh:
            return (json.load(fh).get("title") or "").strip() or None
    except Exception:
        return None


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


def check(text, fetch=fetch_title):
    """[(anchor, claim, title, ok)] for the checkable citations in an article.

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
        title = fetch(key)
        out.append((anchor, claim, title, bool(title) and agrees(claim, title)))
    return out
