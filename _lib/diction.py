#!/usr/bin/env python3
"""Pathological word and phrase usage, measured against the author's own corpus.

THIS MODULE EXISTS BECAUSE ITS PREDECESSOR WAS LOST. A `diction.py` was written
for A320 and copied into A321, A322 and A323. A369 never received a copy, and
the analysis was redone by hand, rediscovering the same prose-stripping rules
and the same phrase list while missing the acronym check the original had. Four
copies and then silence is the exact pattern this library was built to end.

The original was written because an article reached 46.2 uses of `specific` per
thousand words while passing style review with prose reported clean.

WHY _verify.py CANNOT DO THIS. Its `prose_text` strips math, code and Liquid but
NOT `[text][anchor]` pairs, so reference link text counts as prose. In a survey
article that is fatal: A369 carries 1,650 harvested titles, which inflate the
denominator from 11,830 author words to 27,178 and dilute every rate by well
over half. This module strips citation link text, which is what makes the
measurement about the author rather than about the bibliography.

WHY A FIXED THRESHOLD IS THE WRONG DISCRIMINATOR. The original flagged anything
above 5.0 per thousand, which cannot distinguish a tic from a subject noun:
`instruction` at 5.4 per thousand in a compiler article is what the article is
about. `baseline` compares against peer articles instead, so a construction is
flagged when it is unusual FOR THIS AUTHOR. Domain nouns score near-infinite
ratios against unrelated peers and are therefore reported separately and
ignored, which is a limitation stated rather than hidden.
"""

import collections
import glob as _glob
import os
import re
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import post  # noqa: E402

# Constructions worth watching. The first group came from the A320 tool, the
# rest were found in A369 by comparing against peers.
PHRASES = [
    "rather than", "and not", "instead of", "which is the", "which is",
    "it is worth", "worth noting", "worth stating", "worth showing",
    "which is why", "that is why", "in other words", "it is important",
    "the fact that", "is not a", "and it is", "this article",
    "the second is", "in which the", "is the same", "it is the",
]

STOP = set("""the a an and or but of to in on at for with by from as is are was were be been
being it its this that these those which who whom whose what when where how why not no nor
so than then there here their they them he she his her we us our you your i me my if all
any both each few more most other some such only own same too very can will just should now
into over under again further once about above below between through during before after
because while against among within without upon per also may might must shall would could
one two three four five six seven eight nine ten""".split())


def prose(text):
    """Author prose only. Citation link text, math, code and tables removed.

    Order matters. Link pairs go first, because a title containing a dollar sign
    or a pipe would otherwise be partly eaten by the later rules and leave debris.
    """
    body = post.body(text)
    p = post.LINK_PAIR.sub(" ", body)
    p = re.sub(rf"(?m)^\[{post.ANCHOR}\]:.*$", " ", p)
    p = post.strip_code(p)
    p = re.sub(r"(?s)\$\$.*?\$\$", " ", p)
    p = re.sub(r"(?<!\$)\$(?!\$)[^$\n]+\$(?!\$)", " ", p)
    p = re.sub(r"`[^`\n]+`", " ", p)
    p = re.sub(r"<[^>]+>", " ", p)
    p = re.sub(r"(?m)^\|.*$", " ", p)
    return p


def words(text):
    return re.findall(r"[A-Za-z][A-Za-z'-]+", prose(text))


def rates(text, patterns=PHRASES):
    """Occurrences per thousand author words, for each pattern."""
    p = prose(text)
    n = len(re.findall(r"[A-Za-z][A-Za-z'-]+", p)) or 1
    out = {}
    for ph in patterns:
        # A hyphenated technical compound is a domain term, not a style tic.
        # `application-specific` and `target-specific` are not the overuse of
        # `specific` this check hunts, and counting them inflates the signal
        # that matters. Word boundaries alone match inside compounds, because a
        # hyphen IS a boundary, so the neighbours are excluded explicitly.
        k = len(re.findall(r"(?<![\w-])" + re.escape(ph) + r"(?![\w-])", p, re.I))
        out[ph] = (k, 1000.0 * k / n)
    return out, n


def baseline(paths, patterns=PHRASES):
    """Median and maximum rate for each pattern across peer articles.

    A peer set of one is not a baseline. Callers should pass the articles
    written in the same voice, which for this corpus means the same series.
    """
    acc = collections.defaultdict(list)
    used = 0
    for p in paths:
        try:
            t = open(p, encoding="utf-8").read()
        except OSError:
            continue
        used += 1
        r, _ = rates(t, patterns)
        for ph, (_, per_k) in r.items():
            acc[ph].append(per_k)
    return {ph: {"median": statistics.median(v), "max": max(v), "n": len(v)}
            for ph, v in acc.items() if v}, used


def compare(text, peer_paths, patterns=PHRASES):
    """Rows of (pattern, count, rate, median, max, verdict), worst first.

    `over-max` is the finding that matters. It means the construction is used
    more heavily than in ANY article the author has written, which is evidence
    of a tic rather than of subject matter.
    """
    base, npeers = baseline(peer_paths, patterns)
    mine, n = rates(text, patterns)
    rows = []
    for ph, (k, per_k) in mine.items():
        b = base.get(ph)
        if not b:
            rows.append((ph, k, per_k, None, None, "no-baseline"))
            continue
        verdict = ("over-max" if per_k > b["max"] else
                   "over-median" if per_k > b["median"] else "ok")
        rows.append((ph, k, per_k, b["median"], b["max"], verdict))
    order = {"over-max": 0, "over-median": 1, "no-baseline": 2, "ok": 3}
    rows.sort(key=lambda r: (order[r[5]], -(r[2] or 0)))
    return rows, n, npeers


def overused_words(text, limit=5.0, min_count=10):
    """Content-independent words above a rate. The original tool's check.

    Retained because it needs no peer set, which makes it usable on the first
    article of a new series when `compare` has nothing to compare against.
    """
    w = [x.lower() for x in words(text)]
    n = len(w) or 1
    out = []
    for word, k in collections.Counter(w).items():
        if word in STOP or len(word) < 4 or k < min_count:
            continue
        per_k = 1000.0 * k / n
        if per_k >= limit:
            out.append((per_k, k, word))
    return sorted(out, reverse=True)


def repeated_ngrams(text, size=3, min_count=6):
    w = [x.lower() for x in words(text)]
    c = collections.Counter(" ".join(w[i:i + size]) for i in range(len(w) - size))
    return [(k, g) for g, k in c.most_common() if k >= min_count]


def acronyms(text, exempt=()):
    """First use of each acronym, and whether it looks spelled out nearby.

    The check the hand-rolled A369 analysis omitted entirely. Heuristic by
    nature: it looks for the initials appearing as word starts within a window,
    so it reports candidates for reading rather than verdicts.
    """
    p = prose(text)
    ex = {x.upper() for x in exempt}
    seen = {}
    for m in re.finditer(r"\b([A-Z]{2,6})\b", p):
        a = m.group(1)
        if a in ex or a in seen:
            continue
        seen[a] = m.start()
    out = []
    for a, pos in sorted(seen.items(), key=lambda kv: kv[1]):
        window = p[max(0, pos - 260):pos + 260]
        pat = r"\b" + r"[a-z]*\s+".join(list(a)) + r"[a-z]*"
        out.append((a, pos, re.search(pat, window, re.I) is not None))
    return out


def report(path, peer_glob=None, patterns=PHRASES):
    """One-shot human report. Peers default to siblings in the same directory."""
    text = open(path, encoding="utf-8").read()
    peers = [p for p in _glob.glob(peer_glob or os.path.join(os.path.dirname(path) or ".", "*.markdown"))
             if os.path.abspath(p) != os.path.abspath(path)]
    rows, n, npeers = compare(text, peers, patterns)
    print(f"{os.path.basename(path)}: {n} author prose words, {npeers} peers")
    print(f"  {'construction':18s} {'n':>4s} {'rate':>6s} {'median':>7s} {'max':>6s}  verdict")
    for ph, k, per_k, med, mx, verdict in rows:
        if verdict == "ok":
            continue
        ms = f"{med:7.2f}" if med is not None else "      -"
        xs = f"{mx:6.2f}" if mx is not None else "     -"
        print(f"  {ph:18s} {k:4d} {per_k:6.2f} {ms} {xs}  {verdict}")
    flagged = [r for r in rows if r[5] == "over-max"]
    print(f"  {len(flagged)} construction(s) above the corpus maximum")
    return rows
