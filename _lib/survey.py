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

ROW = re.compile(r"^\*\*([\d,]+) (?:records?|works?)\.\*\*(.*)$", re.M)  # `record` for a one-record row
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

    IT NOW SPLITS ON HYPHENS AS WELL AS SPACES, and the reason is that the corpus
    NORMALISES intraword hyphens away before matching. `gate.flatten_separators`
    turns `Hyper-X` into `Hyper X`, so a probe written as `hyper-?x` matches
    nothing at all, silently, and reports the subject as absent.

    THAT FAILURE HAS NOW HAPPENED FOUR TIMES AND TWICE IN PATTERNS WRITTEN TO
    IMPLEMENT THE LESSON. A345's audit could not match `X-48B` with `\bX-?48\b`.
    A347's sweep-store entry could not match `COMPRESSORS` with `\bcompressor\b`.
    A348's contamination probe matched `urban` inside `disturbance`, and its
    Hyper-X probe reported 2 records where there were 16. **Every one was a
    diagnostic reporting the data as wrong when the diagnostic was wrong**, which
    is the dangerous direction, because it argues for work that is not needed and
    hides work that is.

        loose("arresting gear")  ->  arresting[-\s]+gear
        loose("Hyper-X")         ->  Hyper[-\s]+X

    Use it for compound technical nouns and for hyphenated names. Leave ordinary
    prepositional phrases alone, since `span of control` gains nothing from it.
    """
    parts = [re.escape(p) for p in re.split(r"[\s-]+", (term or "").strip()) if p]
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


# ------------------------------------------------------------ year statistics
#
# WHY. Until conversion to generated references, a median year and a period
# share could not be derived from the article, only from build scratch. A
# converted article's References now carry each work's year from the source
# database, which can differ from the year the harvest recorded, since the
# database takes Crossref's first-publication year. So an article can come to
# contradict its own reference list, and these claims are recomputed after every
# conversion. The survey is the article's `research_` definitions, which is how
# the X-Planes articles define it, and a cluster is the works its rows cite.

_NUM = r"(\d[\d,]*)"
MEDIAN = re.compile(r"median (?:publication )?year (?:of the dated records )?is (\d{4})")
DATED = re.compile(r"Of the " + _NUM + r" (?:dated records|records that carry a year|dated works|dated titles)")
PERIOD = re.compile(_NUM + r"(?: of them)?(?:, (?:or|being) ([\d.]+) percent,)? (?:were published|are dated|date from|"
                    r"were dated|appeared)"
                    r"(?: in)? (?:before (\d{4})|(\d{4}) or earlier|(\d{4}) or later)")
_BEING = re.compile(r"^[^.]*?being ([\d.]+) percent")


def stated_year_claims(text):
    """[(scope, kind, values, line number)] for each year statistic the prose states.

    `scope` is the cluster heading when the claim sits under a heading that has a
    cluster row, else `survey`. `values` are (count, percent or None, year) for a
    period claim, (count,) for a dated count and (year,) for a median.
    """
    body = text.split("\n## References\n")[0]
    rows = stated_rows(body)
    out, heading = [], None
    for i, line in enumerate(body.split("\n"), 1):
        m = HEADING.match(line)
        if m:
            heading = m.group(1).strip()
            continue
        if line.startswith("- [") or ROW.match(line):
            continue
        in_cluster = heading in rows
        for mm in MEDIAN.finditer(line):
            near = line[max(0, mm.start() - 40):mm.end()]
            # `that cluster's median` points at another cluster named earlier, as A308's
            # does, so only `the`, `this` or `its` ties a median to its own section.
            local = re.search(r"(?<!that )cluster'?s? median|its median", near, re.I)
            if re.search(r"that cluster'?s? median", near, re.I):
                continue
            # ONLY AN UNAMBIGUOUS SCOPE IS CHECKED. A survey median must share its line
            # with the survey or its dated records, since a bare `The median publication
            # year is 1975` under a cluster heading describes the cluster, as in A329,
            # and a survey paragraph can sit under a cluster heading, as in A320.
            survey_line = bool(re.search(r"\bsurvey\b|dated records", line))
            if local and in_cluster and not survey_line:
                sc = heading
            elif survey_line and not local:
                sc = "survey"
            else:
                continue
            out.append((sc, "median", (int(mm.group(1)),), i, mm.group(0)))
        # A PERIOD CLAIM COUNTS ONLY BESIDE A DATED COUNT, so a count of some subset,
        # such as titles naming a designation, is not read as the whole survey's.
        d = DATED.search(line)
        of_dated = re.search(r"median publication year of the dated records", line)
        if not d and not of_dated:
            continue
        if d:
            out.append(("survey", "dated", (int(d.group(1).replace(",", "")),), i, d.group(0)))
        for mm in PERIOD.finditer(line, d.end() if d else of_dated.end()):
            n, pct, before, upto, after = mm.groups()
            span = mm.group(0)
            if pct is None:
                b2 = _BEING.match(line[mm.end():])
                if b2 and not PERIOD.search(line[mm.end():mm.end() + b2.end()]):
                    pct, span = b2.group(1), line[mm.start():mm.end() + b2.end()]
            kind, y = (("before", before) if before else ("upto", upto) if upto else ("after", after))
            # THE PERCENT KEEPS ITS WRITTEN FORM, `45` or `44.8`, so it is recomputed and
            # rewritten at the precision the article states.
            out.append(("survey", kind, (int(n.replace(",", "")), pct, int(y)), i, span))
    return out


def cluster_members(text):
    """{cluster heading: anchors its rows cite}."""
    body = text.split("\n## References\n")[0]
    out, heading = {}, None
    for line in body.split("\n"):
        m = HEADING.match(line)
        if m:
            heading = m.group(1).strip()
            continue
        r = ROW.match(line)
        if r and heading:
            out.setdefault(heading, []).extend(CITE.findall(r.group(2)))
    return out


def year_check(text, year_of):
    """Recompute each stated year claim with `year_of(anchor) -> int or None`.

    Returns [(line, scope, kind, stated, recomputed)] for every claim, so a
    caller can print the agreements and fail on the rest.
    """
    defs = re.findall(r"(?m)^\[(research_[a-z0-9_]+)\]: ", text)
    members = cluster_members(text)
    results = []
    for scope, kind, vals, line, span in stated_year_claims(text):
        anchors = sorted(set(members.get(scope, []))) if scope != "survey" else sorted(set(defs))
        years = [y for y in (year_of(a) for a in anchors) if y]
        if not years:
            continue
        if kind == "median":
            got = (int(statistics.median(years)),)
        elif kind == "dated":
            got = (len(years),)
        else:
            n, pct, y = vals
            hit = sum(1 for x in years if (x < y if kind == "before" else x <= y if kind == "upto" else x >= y))
            places = len(pct.split(".")[1]) if pct and "." in pct else 0
            share = round(100.0 * hit / len(years), places)
            got = (hit, (f"{share:.{places}f}") if pct is not None else None, y)
        results.append((line, scope, kind, vals, got, span))
    return results


def year_edits(results):
    """[(old, new)] text replacements that make each disagreeing claim state its data.

    Only the numbers inside the matched span change, so the sentence around them
    is untouched and each edit is auditable against its claim.
    """
    out = []
    for line, scope, kind, stated, got, span in results:
        if stated == got:
            continue
        new = span
        if kind == "median":
            new = span.replace(str(stated[0]), str(got[0]), 1)
        elif kind == "dated":
            new = span.replace(f"{stated[0]:,}", f"{got[0]:,}", 1)
        else:
            new = span.replace(f"{stated[0]:,}", f"{got[0]:,}", 1)
            if stated[1] is not None:
                new = new.replace(f"{stated[1]} percent", f"{got[1]} percent", 1)
        if new != span:
            out.append((span, new))
    return out


def main(argv):
    """`survey.py years POST...` recomputes each stated year statistic from the source database."""
    import sys as _sys
    import os as _os
    _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
    import sources
    if len(argv) < 3 or argv[1] != "years":
        print("usage: survey.py years POST... [--edits FILE.toml]")
        return 2
    records = sources.load_records()
    bad = 0
    paths = [x for i, x in enumerate(argv[2:], 2) if not x.startswith("--") and argv[i - 1] != "--edits"]
    for path in paths:
        text = open(path, encoding="utf-8").read()
        index = sources.article_index(records, path)

        def year_of(a):
            hit = index.get(a)
            r = records.get(hit[0]) if hit else None
            return (r.get("original_year") or r.get("year")) if r else None
        res = year_check(text, year_of)
        wrong = [x for x in res if x[3] != x[4]]
        bad += len(wrong)
        print(f"{path}: {len(res)} year claims, {len(wrong)} disagree")
        for line, scope, kind, stated, got, _span in wrong:
            print(f"  line {line} {scope} {kind}: article {stated}, data {got}")
        if "--edits" in argv:
            # A TOML EDIT FILE for `_lib/edits.py`, written beside the post's name.
            out = argv[argv.index("--edits") + 1]
            with open(out, "w", encoding="utf-8") as fh:
                fh.write("# Year statistics recomputed from the source database by `survey.py years`.\n")
                for old, new in year_edits(res):
                    fh.write(f"\n[[edit]]\nold = \'\'\'{old}\'\'\'\nnew = \'\'\'{new}\'\'\'\n")
    return 1 if bad else 0


if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
