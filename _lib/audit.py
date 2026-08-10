#!/usr/bin/env python3
"""Coverage audits run between passes. Thirteen `ref_audit.py`, eight `eqn_scan.py`.

THE PROMOTED-SUBJECTS RULE IS THE STRONGEST RECURRING FINDING IN THIS CORPUS AND
IT HAS FIRED ON SEVEN CONSECUTIVE ARTICLES. An equation pass promotes subjects,
and the reference base has to follow, because the harvest that preceded the
draft could not know which derivations would come to exist. In A317 the audit
found five thin topics and they were exactly the five the equation pass had
promoted, one at zero. In A319 all nine promoted subjects were thin and four
were at zero. In A369 six subjects sat at zero, including the greedy set-cover
guarantee the article argued against without citing.

RUN `citation_gaps` AFTER EVERY EQUATION PASS, BEFORE SELECTING SOURCES.

`equation_gaps` is the mirror check. The genre rule is that if the prose names a
result, relies on a relation, or quotes a value some relation produced, then the
relation must be displayed. A section carrying numeric literals and no equations
is the candidate that rule is looking for.

PRIMARY IS DEFINED, NOT LEFT VAGUE. A primary source is an original research
report or paper contemporary with the work. A recent review of a subject is a
fine citation and is not primary. `primary_fraction` reports the COUNT as well
as the fraction, because adding a contemporary survey lowers the fraction while
leaving the count untouched, and reporting only the fraction reads as a
regression when it is the comprehensiveness directive working.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import refs  # noqa: E402

ANCHOR = r"[A-Za-z0-9_-]+"


def _body(text):
    return text.split("## References")[0]


def sections(text):
    """(heading, content) pairs, including the untitled opening."""
    body = _body(text)
    parts = re.split(r"(?m)^(#{2,3} .+)$", body)
    out = [("(opening)", parts[0])]
    for i in range(1, len(parts), 2):
        out.append((parts[i].strip(), parts[i + 1] if i + 1 < len(parts) else ""))
    return out


def equation_gaps(text, min_words=200):
    """Sections carrying numbers but no displayed relation.

    Reports rather than judges. A section quoting a single date is not a defect,
    which is why the numeric literals are shown for reading.
    """
    out = []
    for head, content in sections(text):
        w = len(content.split())
        if w < min_words:
            continue
        eqs = len(re.findall(r"(?m)^\$\$.*\$\$$", content))
        nums = re.findall(r"(?<![\w.])\d[\d,]*\.?\d*(?![\w])", content)
        if eqs == 0 and len(nums) >= 4:
            out.append({"section": head, "words": w, "equations": eqs,
                        "numeric_literals": len(nums), "examples": nums[:8]})
    return out


def citation_gaps(text, window=900):
    """Displayed equations with no citation within `window` characters.

    A gap is a candidate, not a verdict. Much of an article's arithmetic is its
    own and needs no source. The value is that the list is short enough to read.
    """
    body = _body(text)
    out = []
    for m in re.finditer(r"(?m)^\$\$.*\$\$$", body):
        ctx = body[max(0, m.start() - window):m.end() + window]
        if re.search(rf"\]\[(?:research|ref|book)_{ANCHOR}\]", ctx):
            continue
        h = body.rfind("\n#", 0, m.start())
        head = body[h:body.find("\n", h + 1)].strip() if h > 0 else "(opening)"
        out.append({"section": head, "equation": m.group(0)[:90]})
    return out


def section_citation_density(text, thin_words=250, thin_cites=1):
    """Per-section citation counts, flagging substantial and thinly sourced ones."""
    rows = []
    for head, content in sections(text):
        w = len(content.split())
        cites = re.findall(rf"\]\[({ANCHOR})\]", content)
        rows.append({"section": head, "words": w, "citations": len(cites),
                     "distinct": len(set(cites)),
                     "thin": w > thin_words and len(cites) <= thin_cites})
    return rows


def year_of(anchor):
    """Delegates to refs.parse_anchor, the single anchor parser."""
    return refs.parse_anchor(anchor)[2]


def primary_fraction(text, cutoff):
    """Count AND fraction of references at or before `cutoff`.

    `cutoff` is the article's own contemporary boundary and must be supplied.
    There is no sensible default, because primary for a 1958 aircraft and
    primary for a 2024 compiler are different years.
    """
    block = text.split("## References", 1)[1] if "## References" in text else ""
    anchors = re.findall(rf"(?m)^\[({ANCHOR})\]:", block)
    years = [(a, year_of(a)) for a in anchors]
    dated = [(a, y) for a, y in years if y]
    primary = [a for a, y in dated if y <= cutoff]
    return {"references": len(anchors), "dated": len(dated),
            "primary_count": len(primary), "cutoff": cutoff,
            "primary_fraction": (len(primary) / len(dated)) if dated else 0.0,
            "undated": [a for a, y in years if not y]}


def period_histogram(text, bands=((0, 1979), (1980, 1999), (2000, 2014), (2015, 2100))):
    block = text.split("## References", 1)[1] if "## References" in text else ""
    years = [year_of(a) for a in re.findall(rf"(?m)^\[({ANCHOR})\]:", block)]
    years = [y for y in years if y]
    out = []
    for lo, hi in bands:
        n = sum(1 for y in years if lo <= y <= hi)
        out.append({"from": lo, "to": hi, "count": n,
                    "share": (n / len(years)) if years else 0.0})
    return out


def report(path, cutoff=None):
    text = open(path, encoding="utf-8").read()
    eg = equation_gaps(text)
    cg = citation_gaps(text)
    thin = [r for r in section_citation_density(text) if r["thin"]]
    print(f"{path}")
    print(f"  sections naming numbers with no displayed relation : {len(eg)}")
    for r in eg[:8]:
        print(f"      {r['section'][:64]}  ({r['numeric_literals']} literals)")
    print(f"  displayed equations with no nearby citation        : {len(cg)}")
    for r in cg[:8]:
        print(f"      {r['section'][:52]}  {r['equation'][:44]}")
    print(f"  substantial sections cited once or not at all      : {len(thin)}")
    for r in thin[:8]:
        print(f"      {r['section'][:64]}  ({r['words']} words, {r['citations']} cites)")
    if cutoff:
        pf = primary_fraction(text, cutoff)
        print(f"  primary at or before {cutoff}: {pf['primary_count']} of {pf['dated']} "
              f"= {pf['primary_fraction']*100:.1f}%  (count and fraction both reported)")
    return {"equation_gaps": eg, "citation_gaps": cg, "thin_sections": thin}
