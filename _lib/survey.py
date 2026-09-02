#!/usr/bin/env python3
"""Recompute the statistics an article states about its own reference survey.

WHY THIS IS A MODULE AND NOT A SCRIPT IN A SCRATCH DIRECTORY. A342's publication
review found the paragraph interpreting the survey stale in ALL SIX of its
statistics, while every mechanical part of the same survey was correct. The
primary pass had regenerated the cluster rows and the total with a script and
left the hand-written prose about them alone, and the Source Base four hundred
lines further down stated the corrected values, so the article contradicted
itself and every automated check passed.

IT PASSED BECAUSE THE CHECK WAS A PRESENCE CHECK. The article's number verifier
confirmed the figure with `present("1,771 records", ...)`, which asks whether the
article still says what it used to say. That goes green PRECISELY WHEN A NUMBER
GOES STALE, since a stale number is by definition still present.

The repair was a checker that extracts each stated statistic and recomputes it
from the reference data. It found six defects on its first run. It was written in
a gitignored scratch directory, which means the next article inherits the lesson
and not the instrument, so the general half lives here.

WHAT CANNOT BE GATED CORPUS-WIDE. A median publication year and a period share
cannot be derived from the article, only from the reference set, and that set is
build scratch rather than a committed artefact. `_verify.py` therefore gates the
one thing the article does carry, which is that a cluster row's stated count
matches the citations on that row. Everything else needs this module and the
article's own data.
"""

import collections
import re
import statistics

ROW = re.compile(r"^\*\*([\d,]+) records\.\*\*(.*)$", re.M)
HEADING = re.compile(r"^### (.+)$")
CITE = re.compile(r"\]\[([a-z][a-z0-9_]*)\]")

_UNITS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
          "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
          "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
          "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19}
_TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
         "seventy": 70, "eighty": 80, "ninety": 90}


def words_to_int(phrase):
    """`Two thousand two hundred and eighty` to 2280, or None if it is not a number.

    A SPELLED-OUT NUMBER IS STILL A NUMBER. The prose style spells small numbers
    out, so a checker that only reads digits silently skips exactly the claims a
    careful author took the trouble to write in words. A342 stated its pre-2000
    record count that way and the first version of the checker reported it as a
    parse failure, which is one step from reporting it as passing.
    """
    total = current = 0
    seen = False
    for token in re.split(r"[\s-]+", (phrase or "").strip().lower()):
        if token in ("and", ""):
            continue
        if token in _UNITS:
            current += _UNITS[token]
        elif token in _TENS:
            current += _TENS[token]
        elif token == "hundred":
            current = (current or 1) * 100
        elif token == "thousand":
            total += (current or 1) * 1000
            current = 0
        else:
            return None
        seen = True
    return total + current if seen else None


def stated_rows(text):
    """{cluster heading: (stated count, citations actually present)} from the article."""
    out, heading = {}, None
    for line in text.split("\n"):
        m = HEADING.match(line)
        if m:
            heading = m.group(1).strip()
            continue
        m = ROW.match(line)
        if m and heading is not None:
            out[heading] = (int(m.group(1).replace(",", "")),
                            len(CITE.findall(m.group(2))))
    return out


def cluster_counts(meta):
    """{cluster: records} from the reference metadata, research records only."""
    return collections.Counter(m["cluster"] for m in meta.values()
                               if m.get("kind") == "research")


def period_stats(meta, recent_from=2015, old_before=2000):
    """Median year and the period counts, with SHARES BESIDE COUNTS.

    THE COUNT AND THE FRACTION MOVE IN OPPOSITE DIRECTIONS AND BOTH ARE TRUE.
    Every reference pass in this series has enlarged the recent literature in
    count while shrinking it in share, because the pass adds older primaries
    faster than recent ones. Reporting either alone misrepresents the corpus, so
    this returns both and the caller is expected to state both.
    """
    years = [int(m["year"]) for m in meta.values()
             if m.get("kind") == "research" and str(m.get("year") or "").isdigit()]
    if not years:
        return {"dated": 0, "median": None, "recent": 0, "recent_pct": None, "old": 0}
    recent = sum(1 for y in years if y >= recent_from)
    return {"dated": len(years),
            "median": int(statistics.median(years)),
            "recent": recent,
            "recent_pct": round(100.0 * recent / len(years), 1),
            "old": sum(1 for y in years if y < old_before)}


def primary_stats(meta, definitions, prefixes):
    """Counts and shares for a definition of primary FITTED TO THE SUBJECT.

    A342's subject spans aeronautics and human-robot interaction, so a NASA
    report is primary for one half and an ACM conference paper for the other. A
    definition admitting only the report literature would have reported that
    article's keystone as entirely secondary. `prefixes` is therefore supplied by
    the caller rather than fixed here.
    """
    res = [a for a, m in meta.items() if m.get("kind") == "research"]
    if not res:
        return {"total": 0, "primary": 0, "primary_pct": None}
    hit = sum(1 for a in res if any(definitions[a].startswith(p) or p in definitions[a]
                                    for p in prefixes))
    return {"total": len(res), "primary": hit,
            "primary_pct": round(100.0 * hit / len(res), 1)}


def loose(term):
    r"""A multi-word term as a regex that a hyphen or a run of space cannot defeat.

    THE SAME MEASUREMENT FAILED THREE PASSES RUNNING and the third time it was one
    character. A344's audit asked for `arresting gear` with a space while the
    literature writes `ARRESTING-GEAR CABLE`, and the subject measured 4 records
    where the pool held 12, and 40 where it held 72, with nothing harvested
    between those readings. `gate.py` normalises typographic dashes so no subject
    GATE fails on the shape of a dash, but an audit pattern is not a gate and
    normalises nothing.

    A DIAGNOSTIC WAS BUILT FIRST, MEASURED, AND ABANDONED, and the refusal is the
    useful part. `separator_risks` flagged every literal space in a pattern that a
    hyphen could defeat. Run over this article's twelve audit subjects it flagged
    eleven, including `span of control`, `probe and drogue` and `sea state`, which
    no publisher hyphenates. A checker that fires on almost everything is the
    permissive-gate failure wearing different clothes, and it would have trained
    its reader to ignore it. Making the right thing easy beats warning about the
    wrong one, so what remains is a builder.

        loose("arresting gear")  ->  arresting[-\s]+gear

    Use it for compound technical nouns. Leave ordinary prepositional phrases
    alone, since `span of control` gains nothing from it.
    """
    parts = [re.escape(p) for p in (term or "").split()]
    return r"[-\s]+".join(parts)


def check(claims):
    """Compare (label, stated, actual) triples. Returns (failures, report lines).

    Stated values may be integers, digit strings with separators, or spelled-out
    numbers, because all three occur in the prose.
    """
    lines, bad = [], 0
    for label, stated, actual in claims:
        value = stated
        if isinstance(stated, str):
            cleaned = stated.replace(",", "").strip()
            value = (int(cleaned) if re.fullmatch(r"-?\d+", cleaned)
                     else float(cleaned) if re.fullmatch(r"-?\d*\.\d+", cleaned)
                     else words_to_int(stated))
        ok = value is not None and value == actual
        if not ok:
            bad += 1
        lines.append(f"  {'ok ' if ok else 'BAD'} {label}: article {stated}, data {actual}")
    return bad, lines
