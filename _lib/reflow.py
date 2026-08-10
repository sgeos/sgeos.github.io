#!/usr/bin/env python3
"""Paragraph reflow that keeps atomic things atomic.

WHY THIS IS SHARED. Two files in the whole scratch tree carried the bold-atomic
fix and one carried the link-atomic fix, both written in the session that found
the corresponding bug. Every other generator reflowed naively. A fix that lives
in one working directory is not a fix.

WHAT MUST NOT BE SPLIT ACROSS A LINE, and why each rule exists.

  BOLD SPANS. `**a\\nb**` renders correctly in kramdown, so this is a house
  convention rather than a correctness rule, and it is enforced because every
  invariant scan in this corpus counts `**` per line. Splitting one makes the
  scan report a defect that is not there, which trains the reader to ignore it.

  REFERENCE LINK PAIRS. `[text][anchor]` split across a line still renders, but
  the prose checks in _verify.py strip `\\[[^\\]]*\\]\\[[^\\]]*\\]` PER LINE, so a
  split pair is not stripped and its words leak into prose counts.

  DISPLAY EQUATIONS collapse to exactly one line, which is what makes the
  single-line equation scan meaningful.

WHAT THIS DELIBERATELY DOES NOT TOUCH: headings, tables, list items, indented
blocks, HTML lines and link definitions are passed through unchanged. A reflow
that joined a heading onto the paragraph above it shipped in A369 and rendered
as literal `###` text, so `_verify.py` now has a `heading-inline` check and this
module never merges across a blank line.

REFLOW IS OPT-IN PER ARTICLE AND IS NOT A CORPUS NORMALISER. Two wrapping
conventions coexist. A369 wraps at 108 columns with a median line of 103. The
X-Planes drafts are effectively unwrapped, one paragraph per line, with medians
from 59 to 293 and single lines up to 3,006 characters. Running this over an
unwrapped draft rewrites thousands of lines and produces a diff in which no real
change can be found. Use it only on articles authored with it, or as a
deliberate one-time conversion that is its own commit.

It is a fixed point after one pass on every file in the corpus, which is the
property that makes it safe to run repeatedly between edit batches.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import post  # noqa: E402

WIDTH = 108
_SENTINEL = "\x00"

_BOLD = re.compile(r"\*\*.+?\*\*", re.S)
_LINKPAIR = post.LINK_PAIR
_DEF = re.compile(rf"^\[{post.ANCHOR}\]:")


def _passthrough(block):
    s = block.lstrip("\n")
    if not s.strip():
        return True
    return (s.startswith("|") or s.startswith("#") or s.startswith("<")
            or s.startswith("- ") or s.startswith("* ") or s.startswith("    ")
            or s.startswith("\t") or bool(_DEF.match(s)) or "\n|" in s
            or s.lstrip().startswith("```"))


def reflow_paragraph(text, width=WIDTH):
    """Rewrap one paragraph, treating bold spans and link pairs as single tokens."""
    flat = " ".join(text.split("\n"))
    for rx in (_BOLD, _LINKPAIR):
        flat = rx.sub(lambda m: m.group(0).replace(" ", _SENTINEL), flat)
    atoms = [a.replace(_SENTINEL, " ") for a in flat.split()]
    lines, cur = [], ""
    for a in atoms:
        if not cur:
            cur = a
        elif len(cur) + 1 + len(a) <= width:
            cur += " " + a
        else:
            lines.append(cur)
            cur = a
    if cur:
        lines.append(cur)
    return "\n".join(lines)


def reflow_body(body, width=WIDTH):
    """Rewrap prose paragraphs. Blank-line structure is preserved exactly."""
    out = []
    for block in body.split("\n\n"):
        s = block.strip("\n")
        if not s.strip():
            out.append(s)
        elif s.startswith("$$"):
            out.append(re.sub(r"\s+", " ", " ".join(s.split("\n"))).strip())
        elif _passthrough(block):
            out.append(s)
        else:
            out.append(reflow_paragraph(s, width))
    return "\n\n".join(out)


def reflow_post(text, width=WIDTH):
    """Rewrap a whole post, leaving front matter and the reference block alone.

    The reference block is excluded because link definitions are one per line by
    convention and _verify.py checks that they are sorted within each block.
    """
    m = re.match(r"(?s)(\A---\n.*?\n---\n)(.*)", text)
    front, rest = (m.group(1), m.group(2)) if m else ("", text)
    if "\n## References" in rest:
        body, refs = rest.split("\n## References", 1)
        # Rejoin with exactly one blank line. Splitting consumes the separator,
        # so reconstructing it explicitly is what makes this idempotent; the
        # naive version silently deleted one blank line on every run.
        return front + reflow_body(body, width).rstrip("\n") + "\n\n## References" + refs
    return front + reflow_body(rest, width)
