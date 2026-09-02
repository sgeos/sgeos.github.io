#!/usr/bin/env python3
"""Recompute what a process file states about how far a series is drafted.

WHY THIS EXISTS. The Current Task block in `TASKLOG.md` states how many articles
of the active series are drafted. On 2026-09-02 it stated TWO DIFFERENT COUNTS ON
CONSECUTIVE LINES, forty-eight and forty-seven, the second left behind by an
incremental edit that added the first without removing it. The block's own prose,
eleven lines below the contradiction, says it has gone self-contradictory six
times for exactly that reason and that a resume channel disagreeing with itself is
worse than one merely out of date. That made this the seventh, and the prose
warning about it did not prevent it, because a warning addressed to a reader is
not a check.

THE COUNT IS DERIVABLE, SO IT IS DERIVED. `survey.py` records the same principle
for an article's own reference statistics: a presence check asking whether a file
still says what it used to say GOES GREEN PRECISELY WHEN A NUMBER GOES STALE. The
number of drafted articles in a series is a count of files on disk, so nothing
here matches a remembered string. It counts the drafts and compares.

WHY A CONTRADICTION IS REPORTED SEPARATELY FROM A MISMATCH. They have different
causes and different fixes. A mismatch means the file was not updated in the pass
that added an article. A contradiction means one edit added a claim and left its
predecessor standing, which is the failure actually observed, and which no amount
of comparing a single claim to the truth would catch when one of the two claims is
correct.

WHY `HANDOFF.md` IS NOT CHECKED. It is DELIBERATELY a snapshot that goes stale
between refreshes, and it self-reports staleness by comparing its recorded parent
commit to `git rev-parse HEAD~1`. Checking its count would fire on every article
drafted between refreshes, which is the permissive-checker failure recorded in
`REVERSE_PROMPT.md` on 2026-09-01: a checker that fires on almost everything
trains its reader to ignore it. The channels checked here are the ones the process
requires to be rewritten after every pass.

WHAT IS NOT DERIVABLE AND SO IS NOT CHECKED. The series total, being seventy-two,
is a plan rather than a measurement, and the class or subject of the next article
cannot be derived from file names at all. A handoff asserting that the next
aircraft is a combat aeroplane when it is a research demonstrator is exactly the
kind of error this cannot see, and that error was made on 2026-09-01.
"""

import re

# `Forty-eight of seventy-two drafted`, `48 of 72 articles drafted`, `48 drafted`.
# The trailing `drafted` is REQUIRED and is what keeps this off two neighbouring
# constructions that are not this claim: `series x_planes index 48 of 72`, which
# states a position rather than a count, and `all forty-eight X-Planes drafts
# remain in _drafts/`, which is a frozen history entry describing the past.
# A DIGIT GROUP MUST NOT ABSORB A TRAILING COMMA. Written as `\d[\d,]*` this
# read `A297 through A344, drafted with all four passes` as the number `344,`
# followed by `drafted`, and matched twenty-one such fragments in the history
# section alone. A thousands separator is always followed by three digits.
_NUM = r"\d{1,3}(?:,\d{3})*"
_WORD = r"[A-Za-z]+(?:-[A-Za-z]+)?"

STATED = re.compile(
    rf"\b({_WORD}|{_NUM})"
    rf"(?:\s+of\s+(?:{_WORD}|{_NUM}))?"
    r"(?:\s+articles)?\s+drafted\b",
    re.I,
)

FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)

# A LITERAL QUOTED AS AN EXAMPLE IS NOT A CLAIM. Documenting this checker inside a
# channel it reads means writing its own trigger shapes down, and the section of
# REVERSE_PROMPT.md explaining why `X-19 drafted` matches DID match, on the first
# run after it was written. `_lib/render.py` excludes `<pre>` and `<code>` for the
# same reason, because articles about a syntax display that syntax as their
# subject. Code spans are blanked to spaces rather than deleted so that a span
# INSIDE a word, as in `draft`X`ed`, cannot fuse its neighbours into a token
# neither contains. Blanking does not separate a number from a following word,
# since the pattern joins them with `\s+`, and that is deliberate: a code span
# between a count and the word `drafted` is still that claim.
CODE = re.compile(r"```.*?```|``[^`]*``|`[^`\n]*`", re.S)


def strip_code(text):
    """Fenced blocks and inline code spans blanked, leaving everything else."""
    return CODE.sub(lambda m: " " * len(m.group(0)), text or "")


def _to_int(token, words_to_int):
    token = token.strip()
    if re.fullmatch(r"\d[\d,]*", token):
        return int(token.replace(",", ""))
    return words_to_int(token)


def drafted(files, series):
    """How many of `files` are drafts belonging to `series`.

    `files` is an iterable of `(name, text)` so that a caller may pass synthetic
    text. The template carries no `series:` line and so is excluded by the same
    rule that excludes every unrelated draft, rather than by name.
    """
    n = 0
    for _, text in files:
        m = FM.match(text or "")
        if not m:
            continue
        if re.search(rf"^series:\s*{re.escape(series)}\s*$", m.group(1), re.M):
            n += 1
    return n


def indices(files, series):
    """The `series_index` values present, as a sorted list, for gap reporting."""
    out = []
    for _, text in files:
        m = FM.match(text or "")
        if not m:
            continue
        if not re.search(rf"^series:\s*{re.escape(series)}\s*$", m.group(1), re.M):
            continue
        mi = re.search(r"^series_index:\s*(\d+)\s*$", m.group(1), re.M)
        if mi:
            out.append(int(mi.group(1)))
    return sorted(out)


def section(text, heading):
    """The body under a `## heading`, up to the next `## `, or the whole text.

    TASKLOG.md is APPEND-ONLY BELOW `## History`, and those entries state counts
    that were correct on the day they were written. Scanning the whole file would
    report every one of them as contradicting today's measurement, so a caller
    checking that file passes the block that the process requires to be current.

    MEASURED, BECAUSE A SCOPE RULE ASSERTED IS NOT A SCOPE RULE JUSTIFIED. Over
    the whole of TASKLOG.md on 2026-09-02 the claim pattern matched four spans
    outside the current block. Two are history entries stating a count correct on
    its own date. **The other is `X-19 drafted`**, where the designation of the
    aircraft ends in digits that read as a count, and in a series covering X-1
    through X-76 that shape recurs on almost every history line.
    """
    m = re.search(rf"^##\s+{re.escape(heading)}\s*$(.*?)(?=^##\s|\Z)",
                  text or "", re.M | re.S)
    return m.group(1) if m else None


def stated_counts(text, words_to_int):
    """Every drafted-count claim in `text`, as a list of `(int, matched text)`.

    A token that does not parse as a number is DROPPED RATHER THAN REPORTED. The
    construction `the article being drafted` is prose, not a claim, and a checker
    that reported it would fire on ordinary writing.
    """
    out = []
    for m in STATED.finditer(strip_code(text)):
        n = _to_int(m.group(1), words_to_int)
        if n is not None:
            out.append((n, m.group(0)))
    return out


def check(files, series, channels, words_to_int):
    """Findings as `(check, detail)`, empty when every channel agrees with disk.

    `channels` is an iterable of `(label, text)` already narrowed to the part of
    each file that is required to be current.
    """
    actual = drafted(files, series)
    found = []
    for label, text in channels:
        claims = stated_counts(text, words_to_int)
        distinct = sorted({n for n, _ in claims})
        if len(distinct) > 1:
            quoted = ", ".join(sorted({repr(s) for _, s in claims}))
            found.append((
                "progress-contradiction",
                f"{label} states {len(distinct)} different drafted counts "
                f"({', '.join(str(d) for d in distinct)}): {quoted}. "
                f"{actual} drafts of series {series} are on disk."))
        elif distinct and distinct[0] != actual:
            found.append((
                "progress-stale",
                f"{label} states {distinct[0]} drafted, but {actual} drafts of "
                f"series {series} are on disk."))
    return found
