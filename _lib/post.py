#!/usr/bin/env python3
"""What a post is made of. The one place that knows the document's shape.

WHY THIS MODULE EXISTS, AND THE IRONY OF NEEDING IT. An audit of this library
found seven independent splits on `"## References"` across four modules, nine
hard-codings of the anchor character class across six, two separate `ANCHOR`
constants, and a byte-identical `fold` in two files. That is the same defect the
library was written to remove, reproduced inside it within a day.

The lesson generalises past this repository. Extracting shared mechanism does
not, by itself, stop shared mechanism reappearing. Each module here was written
knowing the others existed, and each still re-derived the document structure
because doing so was two lines and importing felt heavier. Duplication is the
default outcome of local convenience, so it has to be checked for deliberately
rather than assumed absent.

DEPENDENCY DIRECTION. This module imports nothing from the library. Everything
else may import it. That keeps the graph acyclic and means a change to document
structure lands in exactly one file.
"""

import re

# The anchor character class, defined once. `_verify.py` carries its own copy
# because it must run standalone on a bare runner with no import path set up,
# and that duplication is deliberate and documented in both places.
ANCHOR = r"[A-Za-z0-9_-]+"

FRONT_MATTER = re.compile(r"(?s)\A---\n(.*?)\n---\n")
DEF_LINE = re.compile(rf"(?m)^\[({ANCHOR})\]:\s*(\S.*)$")
USE = re.compile(rf"\]\[({ANCHOR})\]")
LINK_PAIR = re.compile(rf"\[[^\]\n]+\]\[{ANCHOR}\]")
DISPLAY_EQ = re.compile(r"(?m)^\$\$.*\$\$$")
HEADING = re.compile(r"(?m)^(#{2,3} .+)$")

REFERENCES_HEADING = "## References"


def split(text):
    """(front_matter, body, references) with the heading kept on the references.

    The body excludes front matter and everything from `## References` onward.
    A post with no reference block yields an empty string for it rather than
    raising, because drafts legitimately reach the equation pass without one.
    """
    m = FRONT_MATTER.match(text)
    front, rest = (m.group(0), text[m.end():]) if m else ("", text)
    if REFERENCES_HEADING in rest:
        body, refs = rest.split(REFERENCES_HEADING, 1)
        return front, body, REFERENCES_HEADING + refs
    return front, rest, ""


def body(text):
    return split(text)[1]


def references(text):
    return split(text)[2]


def strip_code(text):
    """Remove fenced code, Liquid highlight blocks and inline code."""
    t = re.sub(r"(?s)```.*?```", " ", text)
    t = re.sub(r"(?s)\{%\s*highlight.*?\{%\s*endhighlight\s*%\}", " ", t)
    return re.sub(r"`[^`\n]+`", " ", t)


def definitions(text):
    """{anchor: url} from the reference block."""
    return {a: u.strip() for a, u in DEF_LINE.findall(references(text) or text)}


def used_anchors(text):
    return set(USE.findall(body(text)))


def equations(text):
    """Display equations, as source lines."""
    return DISPLAY_EQ.findall(body(text))


def sections(text):
    """(heading, content) pairs over the body, including the untitled opening."""
    parts = HEADING.split(body(text))
    out = [("(opening)", parts[0])]
    for i in range(1, len(parts), 2):
        out.append((parts[i].strip(), parts[i + 1] if i + 1 < len(parts) else ""))
    return out
