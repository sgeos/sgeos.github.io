#!/usr/bin/env python3
"""Corpus invariant checks. Run in CI before the build, and locally any time.

Every check here exists because the corresponding defect actually shipped. The
2026-08-05 audit found all of them by hand; this script is what stops them
recurring silently. Each check names the incident that motivated it.

Usage:
    python3 _verify.py            # errors and warnings, exits nonzero on error
    python3 _verify.py --strict   # warnings are errors too
    python3 _verify.py --quiet    # only failures

Exit codes: 0 clean, 1 errors found.

Deliberately offline and fast. Citation and URL checking needs the network and
lives in _verify_citations.py, which is not part of the deploy path.
"""

import argparse
import collections
import datetime
import glob
import os
import re
import sys

POSTS = "_posts"
DRAFTS = "_drafts"

ANCHOR = r"[A-Za-z0-9_-]+"
DEF_RE = re.compile(rf"^\[({ANCHOR})\]:\s")
USE_RE = re.compile(rf"\]\[({ANCHOR})\]")
FM_RE = re.compile(r"(?s)\A---\n(.*?)\n---\n")
DATE_RE = re.compile(
    r"^date:\s*(\d{4}-\d{2}-\d{2})[ T](\d{2}:\d{2}:\d{2})\s*([+-]\d{4})?", re.M
)

# GitHub Pages serves sibling project sites at these path prefixes, which shadow
# any post whose FIRST category matches. Such a post builds correctly and then
# 404s on the live site.
SHADOWED = {"keleusma"}

# MathJax accepts these; LaTeX does not, so they break PDF generation. Found on
# 2026-08-05 when the repaired PDF pipeline turned into a de facto math linter.
MATHJAX_ONLY = re.compile(r"\\(bbox|lt|gt|cssId|require|class)\b")

CONTRACTIONS = re.compile(
    r"\b(?:can't|won't|don't|doesn't|didn't|isn't|aren't|wasn't|weren't|hasn't|"
    r"haven't|hadn't|shouldn't|wouldn't|couldn't|it's|that's|there's|we're|"
    r"they're|you're|I'm|we've|they've|you've|I've|we'll|they'll|you'll|I'll)\b",
    re.I,
)

# Content-independent words only. Ratio against the corpus is the WRONG
# discriminator: it surfaces topic vocabulary such as `kotlin` or `raycasting`.
WATCH_WORDS = """specific specifically various comprehensive substantial substantially
particular significant considerable notable essential fundamental crucial
framework configuration mechanism approach aspect factor element component
distinct underlying appropriate relevant robust effective relatively typically
admits compact leverage utilize facilitate encompass underscore
myriad nuanced holistic pivotal seamless intricate paradigm realm landscape""".split()
WORD_RATE_LIMIT = 5.0  # per thousand prose words; a flag, not a verdict


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, check, detail):
        self.errors.append((check, detail))

    def warn(self, check, detail):
        self.warnings.append((check, detail))


def front_matter(text):
    m = FM_RE.match(text)
    return m.group(1) if m else None


def prose_lines(text):
    """Lines eligible for prose checks. Mirrors the extraction in the docs."""
    lines = text.split("\n")
    out = []
    in_fence = in_liquid = False
    math_depth = 0
    seen_fm = False
    in_fm = False
    for i, line in enumerate(lines):
        s = line.strip()
        if i == 0 and s == "---":
            in_fm = True
            continue
        if in_fm:
            if s == "---":
                in_fm = False
                seen_fm = True
            continue
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if re.match(r"^\s*\{%\s*end(highlight|raw)\s*%\}", line):
            in_liquid = False
            continue
        if re.match(r"^\s*\{%\s*(highlight|raw)\b", line):
            in_liquid = True
            continue
        if in_liquid:
            continue
        d = s.count("$$")
        was = math_depth % 2 == 1
        math_depth += d
        if was or d:
            continue
        if not s or s.startswith("#") or s.startswith("<") or s.startswith("|"):
            continue
        if DEF_RE.match(line) or re.match(r"^\s*[-*]\s*\[[^\]]+\]\[", line):
            continue
        if re.match(r"^(?: {4,}|\t)\S", line) and not re.match(r"^\s*(?:[-*+]\s|\d+[.)]\s)", line):
            continue
        out.append((i, line))
    return out


def prose_text(text):
    body = []
    for _, l in prose_lines(text):
        l = re.sub(r"\$[^$\n]+\$|`[^`\n]+`|\{%.*?%\}", " ", l)
        body.append(l)
    return "\n".join(body)


def check_post(path, text, rep):
    name = os.path.basename(path)

    fm = front_matter(text)
    if fm is None:
        rep.error("front-matter", f"{name}: missing or malformed front matter")
        return None

    for key in ("layout", "title", "date"):
        if not re.search(rf"^{key}:", fm, re.M):
            rep.error("front-matter", f"{name}: missing `{key}:`")

    m = DATE_RE.search(fm)
    if not m:
        rep.error("front-matter", f"{name}: unparseable `date:`")
        return None
    d, tm, off = m.group(1), m.group(2), m.group(3) or "+0000"

    # Filename date must equal the front matter date. Four posts disagreed on
    # 2026-08-05; Jekyll uses the front matter, so the filename silently lied
    # about where an article lived and caused a gap-fill into an occupied day.
    if name[:10] != d:
        rep.error("date-filename", f"{name}: filename says {name[:10]}, front matter says {d}")

    # A non-UTC offset makes the front matter date, the filename date, and the
    # URL date three values that can disagree. Nineteen legacy posts carried
    # +0900, which hid two date collisions at URL level for years.
    if off != "+0000":
        rep.error("date-offset", f"{name}: offset {off}, expected +0000")

    cats = re.search(r"^categories:\s*(.*)$", fm, re.M)
    first = None
    if cats:
        raw = cats.group(1).strip()
        if raw.startswith("["):
            parts = [c.strip().strip("\"'") for c in raw.strip("[]").split(",")]
        else:
            parts = raw.split()
        first = parts[0].lower() if parts and parts[0] else None
    if first in SHADOWED:
        rep.error(
            "shadowed-category",
            f"{name}: first category `{first}` is shadowed by a sibling Pages site; the post will 404",
        )

    if not re.search(r"<!--\s*A\d+\s*-->", text):
        rep.warn("debug-tag", f"{name}: no <!-- Axxx --> marker")

    used = set(USE_RE.findall(text))
    defined = [mm.group(1) for mm in re.finditer(rf"^\[({ANCHOR})\]:\s", text, re.M)]
    dset = set(defined)
    for a in sorted(used - dset):
        rep.error("anchor-undefined", f"{name}: [{a}] used but never defined; renders literally")
    for a in sorted(dset - used):
        rep.error("anchor-unused", f"{name}: [{a}] defined but never used")
    dupes = [a for a, n in collections.Counter(defined).items() if n > 1]
    for a in dupes:
        rep.error("anchor-duplicate", f"{name}: [{a}] defined more than once")

    # Definitions sorted within each block. Block-wise, not global: categorised
    # sub-blocks under ### headings must keep their grouping.
    lines = text.split("\n")
    idx = [i for i, l in enumerate(lines) if DEF_RE.match(l)]
    if idx:
        run = [idx[0]]
        runs = []
        for a, b in zip(idx, idx[1:]):
            if all(not lines[j].strip() for j in range(a + 1, b)):
                run.append(b)
            else:
                runs.append(run)
                run = [b]
        runs.append(run)
        for r in runs:
            anchors = [DEF_RE.match(lines[i]).group(1) for i in r]
            if anchors != sorted(anchors):
                rep.error("anchor-order", f"{name}: link definitions not sorted (block at line {r[0]+1})")
                break

    stripped = re.sub(r"(?s)```.*?```", " ", text)
    stripped = re.sub(r"(?s)\{%\s*highlight.*?\{%\s*endhighlight\s*%\}", " ", stripped)
    stripped = re.sub(r"`[^`\n]+`", " ", stripped)
    if stripped.count("$$") % 2:
        rep.error("math-delimiters", f"{name}: odd number of $$ delimiters")
    for env in ("align", "equation", "gather"):
        if re.search(rf"\$\$\s*\n\s*\\begin\{{{env}\}}", text):
            rep.error(
                "math-nesting",
                f"{name}: \\begin{{{env}}} inside $$; use {env}ed. LaTeX rejects the nesting",
            )
    for mm in re.finditer(r"_\{", text):
        i = mm.end() - 1
        depth = 0
        end = None
        for j in range(i, len(text)):
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    end = j + 1
                    break
        # `^{...}` only. A bare `^n` is not a group, and scanning past it for
        # the next brace anywhere in the file produced seven false positives on
        # ordinary summation limits such as `\sum_{i=1}^n`.
        if end and end + 1 < len(text) and text[end] == "^" and text[end + 1] == "{":
            depth = 0
            e2 = None
            for j in range(end + 1, len(text)):
                if text[j] == "{":
                    depth += 1
                elif text[j] == "}":
                    depth -= 1
                    if depth == 0:
                        e2 = j + 1
                        break
            if e2 and e2 < len(text) and text[e2] == "_":
                rep.error("math-double-subscript", f"{name}: double subscript near {text[mm.start():e2+6]!r}")
                break
    mo = MATHJAX_ONLY.search(text)
    if mo:
        rep.warn("math-mathjax-only", f"{name}: {mo.group(0)} is MathJax-only; PDF relies on a shim")

    body = prose_text(text)
    for i, line in prose_lines(text):
        clean = re.sub(r"\$[^$\n]+\$|`[^`\n]+`|\{%.*?%\}|\[[^\]]*\]\[[^\]]*\]", " ", line)
        if "—" in clean or "–" in clean:
            rep.error("style-dash", f"{name}:{i+1}: em or en dash in prose")
            break
    for i, line in prose_lines(text):
        clean = re.sub(r"\$[^$\n]+\$|`[^`\n]+`|\{%.*?%\}|\[[^\]]*\]\[[^\]]*\]", " ", line)
        if CONTRACTIONS.search(clean):
            rep.warn("style-contraction", f"{name}:{i+1}: {CONTRACTIONS.search(clean).group(0)}")
            break

    words = [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'-]*", body)]
    if len(words) >= 400:
        counts = collections.Counter(words)
        for w in WATCH_WORDS:
            n = counts.get(w, 0)
            rate = n * 1000.0 / len(words)
            if n >= 10 and rate >= WORD_RATE_LIMIT:
                rep.warn("word-frequency", f"{name}: `{w}` {n}x = {rate:.1f}/1k (limit {WORD_RATE_LIMIT})")

    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    rep = Report()
    dates = collections.defaultdict(list)
    numbers = collections.defaultdict(list)

    posts = sorted(glob.glob(os.path.join(POSTS, "*.markdown")))
    for p in posts:
        text = open(p, encoding="utf-8").read()
        d = check_post(p, text, rep)
        if d:
            dates[d].append(os.path.basename(p))
        num = re.search(r"<!--\s*(A\d+)\s*-->", text)
        if num:
            numbers[num.group(1)].append(os.path.basename(p))

    # One article per day. Collisions were resolved on 2026-08-05 and are easy
    # to reintroduce by backdating into a day that only looks free.
    for d, files in sorted(dates.items()):
        if len(files) > 1:
            rep.error("date-collision", f"{d}: {', '.join(files)}")

    for n, files in sorted(numbers.items()):
        if len(files) > 1:
            rep.error("article-number", f"{n} used by {len(files)} posts: {', '.join(files)}")

    # Drafts: check what would break on publication, without failing the build.
    for p in sorted(glob.glob(os.path.join(DRAFTS, "*.markdown"))):
        if os.path.basename(p) == "template.markdown":
            continue
        text = open(p, encoding="utf-8").read()
        fm = front_matter(text)
        if not fm:
            continue
        m = DATE_RE.search(fm)
        if m and m.group(1) in dates:
            rep.warn(
                "draft-date-taken",
                f"{os.path.basename(p)}: dated {m.group(1)}, already used by {dates[m.group(1)][0]}",
            )

    if not args.quiet:
        print(f"checked {len(posts)} posts")

    def show(items, label):
        if not items:
            return
        by = collections.defaultdict(list)
        for check, detail in items:
            by[check].append(detail)
        for check in sorted(by):
            print(f"\n{label} [{check}] {len(by[check])}")
            for d in by[check][:12]:
                print(f"    {d}")
            if len(by[check]) > 12:
                print(f"    ... and {len(by[check]) - 12} more")

    show(rep.warnings, "WARN ")
    show(rep.errors, "ERROR")

    failed = rep.errors or (args.strict and rep.warnings)
    print(f"\n{len(rep.errors)} error(s), {len(rep.warnings)} warning(s)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
