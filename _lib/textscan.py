#!/usr/bin/env python3
"""Searching saved source text, replacing the per-article `ctx.py` and `clean.py`.

WHY. A381 to A384 each carried a byte-identical seven-line `ctx.py` and A381 to
A383 a six-line `clean.py`. Small enough to retype, and that is why they were
retyped, four and three times.

  python3 _lib/textscan.py ctx FILE REGEX [--width 150] [--max 4]
  python3 _lib/textscan.py strip-wikitext IN OUT

`ctx` prints each case-insensitive match with its surroundings and line breaks
flattened, which is what checking a claim against a saved source needs and
what `grep` does badly across wrapped lines.

`strip-wikitext` removes `<ref>` elements and citation templates, so a search
for a fact finds the article's sentence rather than a reference title. The
template loop is bounded at eight passes, enough for the nesting depth seen in
practice, and anything nested deeper is left in place, not mangled.
"""

import argparse
import re
import sys

TEMPLATE_PASSES = 8


def context(text, pattern, width=150, limit=4):
    """Up to `limit` snippets around case-insensitive matches of `pattern`."""
    if width < 0 or limit < 1:
        raise ValueError("width must be non-negative and limit positive")
    out = []
    for m in re.finditer(pattern, text, re.I):
        if len(out) >= limit:
            break
        out.append(text[max(0, m.start() - width):m.end() + width].replace("\n", " "))
    return out


def strip_wikitext(s):
    """Wikitext with references and citation templates removed."""
    s = re.sub(r"<ref[^>/]*/>", "", s)
    s = re.sub(r"<ref[^>]*>.*?</ref>", "", s, flags=re.S)
    for _ in range(TEMPLATE_PASSES):
        s, n = re.subn(r"\{\{[Cc]ite[^{}]*\}\}|\{\{[Ss]fn[^{}]*\}\}", "", s)
        if not n:
            break
    return s


def main(argv):
    ap = argparse.ArgumentParser(prog="textscan.py")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("ctx")
    p.add_argument("file")
    p.add_argument("regex")
    p.add_argument("--width", type=int, default=150)
    p.add_argument("--max", type=int, default=4)
    p = sub.add_parser("strip-wikitext")
    p.add_argument("src")
    p.add_argument("dst")
    a = ap.parse_args(argv[1:])
    if a.cmd == "ctx":
        text = open(a.file, encoding="utf-8", errors="replace").read()
        hits = context(text, a.regex, a.width, a.max)
        for h in hits:
            print(f"  ...{h}...")
        return 0 if hits else 1
    src = open(a.src, encoding="utf-8", errors="replace").read()
    with open(a.dst, "w", encoding="utf-8") as fh:
        fh.write(strip_wikitext(src))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
