#!/usr/bin/env python3
"""Invariant scan for a post in progress, run between edit batches.

RELATIONSHIP TO _verify.py. That script is the gate: it runs in CI and on
pre-push, it covers the whole corpus, and every check in it is an error the
corpus is already clean of. This module is the workbench: it runs on one file
mid-edit and reports house conventions as well as defects, including several
that are deliberately NOT in _verify.py because the corpus violates them
harmlessly.

The distinction is load-bearing. Promoting a convention to a corpus gate was
measured and rejected during this work:

  bold spanning a line break   7.7% of posts   kramdown renders it correctly
  display math on two lines   24.2% of posts   kramdown renders it correctly
  duplicate reference URL     19.5% of posts   often legitimate

Those three are reported here as CONVENTION findings and are not errors
anywhere. Only findings marked DEFECT are things that actually break.
"""

import collections
import re

DEFECT = "defect"
CONVENTION = "convention"

ANCHOR = r"[A-Za-z0-9_-]+"


def _split(text):
    m = re.match(r"(?s)(\A---\n.*?\n---\n)(.*)", text)
    rest = m.group(2) if m else text
    if "\n## References" in rest:
        body, refs = rest.split("\n## References", 1)
        return body, refs
    return rest, ""


def _strip_code(text):
    t = re.sub(r"(?s)```.*?```", " ", text)
    t = re.sub(r"(?s)\{%\s*highlight.*?\{%\s*endhighlight\s*%\}", " ", t)
    return re.sub(r"`[^`\n]+`", " ", t)


def scan(text):
    """Return a list of (severity, check, detail)."""
    out = []
    body, refs = _split(text)
    stripped = _strip_code(text)
    lines = text.split("\n")

    # ---- DEFECTS. These break rendering or the build.
    for mm in re.finditer(r"\S ##+ [A-Za-z]", stripped):
        out.append((DEFECT, "heading-inline",
                    f"heading glued to prose near {mm.group(0)!r}; renders as literal text"))
    for mm in re.finditer(r"\\\\[,;:!]", stripped):
        out.append((DEFECT, "math-doubled-backslash",
                    f"{mm.group(0)!r}; MathJax reads it as a line break"))
    if stripped.count("$$") % 2:
        out.append((DEFECT, "math-delimiters", "odd number of $$ delimiters"))

    used = set(re.findall(rf"\]\[({ANCHOR})\]", body))
    defined = re.findall(rf"(?m)^\[({ANCHOR})\]:", refs)
    dset = set(defined)
    for a in sorted(used - dset):
        out.append((DEFECT, "anchor-undefined", f"[{a}] used but never defined; renders literally"))
    for a in sorted(dset - used):
        out.append((DEFECT, "anchor-unused", f"[{a}] defined but never used"))
    for a, n in collections.Counter(defined).items():
        if n > 1:
            out.append((DEFECT, "anchor-duplicate", f"[{a}] defined more than once"))

    # A `{c('...')}` survivor means a generator emitted a template it never
    # filled. A320 froze its cluster citations this way and the reference
    # generator correctly refused to emit; A369 shipped the placeholders into
    # the file because they were inserted from a raw string that was never
    # formatted.
    for mm in re.finditer(r"\{c\(", text):
        out.append((DEFECT, "unfilled-template", "a {c('...')} placeholder survived into the file"))
        break

    # ---- CONVENTIONS. Measured against the corpus and deliberately not gates.
    for i, line in enumerate(lines):
        cl = re.sub(r"`[^`\n]+`|\$[^$\n]+\$", " ", line)
        if cl.count("**") % 2:
            out.append((CONVENTION, "bold-span", f"line {i+1}: bold span crosses a line break"))
    for i, line in enumerate(lines):
        if line.count("[") != line.count("]"):
            out.append((CONVENTION, "split-link", f"line {i+1}: link pair split across lines"))
    n = len(re.findall(r"(?m)^\$\$(?!.*\$\$$).*$", body))
    if n:
        out.append((CONVENTION, "math-multiline", f"{n} display equations span several source lines"))
    urls = collections.Counter(u.strip() for u in re.findall(rf"(?m)^\[{ANCHOR}\]:\s*(\S.*)$", refs))
    for u, c in urls.items():
        if c > 1:
            out.append((CONVENTION, "duplicate-url", f"{c} anchors resolve to {u[:70]}"))
    return out


def summary(text):
    """Counts by severity and check, for a one-line progress report."""
    rows = scan(text)
    by = collections.Counter((sev, chk) for sev, chk, _ in rows)
    return {"defects": sum(v for (s, _), v in by.items() if s == DEFECT),
            "conventions": sum(v for (s, _), v in by.items() if s == CONVENTION),
            "by_check": {f"{s}/{c}": v for (s, c), v in sorted(by.items())}}


def assert_clean(text, allow_conventions=True):
    """Raise if the text carries defects. Used as a guard by edits.apply."""
    rows = [r for r in scan(text) if r[0] == DEFECT or not allow_conventions]
    if rows:
        detail = "; ".join(f"{c}: {d}" for _, c, d in rows[:6])
        raise ValueError(f"{len(rows)} invariant failure(s): {detail}")
    return True


def stats(text):
    """Descriptive counts. Reported, never targeted, per the genre document."""
    body, refs = _split(text)
    return {"lines": len(text.split("\n")),
            "words": len(body.split()),
            "equations": len(re.findall(r"(?m)^\$\$.*\$\$$", body)),
            "citations": len(re.findall(rf"\]\[{ANCHOR}\]", body)),
            "references": len(re.findall(rf"(?m)^\[{ANCHOR}\]:", refs))}
