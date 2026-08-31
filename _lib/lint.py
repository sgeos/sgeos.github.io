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
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import post  # noqa: E402

DEFECT = "defect"
CONVENTION = "convention"

ANCHOR = post.ANCHOR


def _split(text):
    _front, body, refs = post.split(text)
    return body, refs


_strip_code = post.strip_code


def _strip_code_lines(text):
    """Lines with code blanked and numbering preserved. Structure lives in post.py."""
    return post.strip_code_keeping_lines(text).split("\n")


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

    # A DISPLAY EQUATION SHARING A LINE WITH PROSE IS DEMOTED TO INLINE MATH, AND
    # NOTHING ELSE IN THE TOOLCHAIN SEES IT. A341 shipped one into a build: an edit
    # landed `$$...$$` and the next paragraph's opening sentence on the same source
    # line, and kramdown rendered `\(...\)` inside a paragraph with two unrelated
    # sentences run together. `render.py` cannot catch it, because the delimiters
    # balance and the markup resolves; the page is merely wrong. It was found by
    # comparing the source equation count against the rendered one.
    #
    # Measured across the whole corpus before being made a defect: four offending
    # lines in three files, of which three are shell and Makefile syntax inside
    # code blocks, which `strip_code` removes. The corpus is clean.
    for i, line in enumerate(_strip_code_lines(text)):
        if "$$" not in line:
            continue
        if re.match(r"^\$\$.*\$\$$", line):        # a complete display equation
            continue
        if re.match(r"^\$\$[^$]*$", line) or re.match(r"^[^$]*\$\$$", line):
            continue                              # one half of a two-line equation
        if re.match(r"^- \[.*\]\[" + ANCHOR + r"\]$", line):
            continue    # a reference bullet whose LINK TEXT is a title containing math
        out.append((DEFECT, "math-display-inlined",
                    f"line {i+1}: $$ shares a line with prose; renders as INLINE math"))

    # ANCHORS ARE COUNTED ACROSS THE WHOLE FILE, NOT BODY AGAINST REFERENCE BLOCK.
    #
    # The earlier form asked whether an anchor used IN THE BODY was defined IN THE REFERENCE
    # BLOCK, and it was wrong in both directions. Run across the corpus on 2026-08-11 it
    # produced 1,596 defect-severity findings and every one was an artefact.
    #
    #   `references()` splits on a literal `## References` heading. Two 2016 posts head their
    #   link block `## Links:`, so the block landed in the body, the reference block came back
    #   empty, and all 16 of their anchors were reported undefined. Every one resolves, and the
    #   rendered pages carry no literal `[text][anchor]` anywhere.
    #
    #   The corpus convention puts the visible `- [text][anchor]` entry for each reference
    #   INSIDE the References section, which body-only counting cannot see. That reported 1,579
    #   references as defined-but-never-used.
    #
    # Kramdown resolves a reference against the whole document, so this does too.
    used = post.all_used_anchors(text)
    defined_list = re.findall(rf"(?m)^\[({ANCHOR})\]:", _strip_code(text))
    dset = set(defined_list)
    for a in sorted(used - dset):
        out.append((DEFECT, "anchor-undefined", f"[{a}] used but never defined; renders literally"))
    for a in sorted(dset - used):
        out.append((DEFECT, "anchor-unused", f"[{a}] defined but never used"))
    for a, n in collections.Counter(defined_list).items():
        if n > 1:
            out.append((DEFECT, "anchor-duplicate", f"[{a}] defined more than once"))

    # A `{c('...')}` survivor means a generator emitted a template it never
    # filled. A320 froze its cluster citations this way and the reference
    # generator correctly refused to emit; A369 shipped the placeholders into
    # the file because they were inserted from a raw string that was never
    # formatted.
    # MATH IS STRIPPED FIRST. `\frac{W_{avail}}{c(t)}` contains the literal bytes `{c(`, so
    # scanning raw text reported a surviving placeholder against a published article whose
    # only offence was dividing by a function of time.
    for mm in re.finditer(r"\{c\('", post.strip_math(_strip_code(text))):
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
