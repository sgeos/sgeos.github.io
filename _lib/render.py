#!/usr/bin/env python3
"""Audit of BUILT HTML. The only instrument here that sees what a reader sees.

WHY THIS EXISTS. `_verify.py` and `_lib/lint.py` both read markdown source, so both can only
predict what kramdown and MathJax will do. On 2026-08-11 they disagreed with each other and
with reality: lint reported 1,596 defect-severity findings across the corpus and the rendered
pages carried none of them. A source checker cannot settle a rendering question.

WHAT IS CHECKED IS WHAT A READER WOULD SEE, not a house convention. A bold span crossing a
line break is a convention finding because kramdown renders it correctly. A reference that
never resolved is a defect because the page shows `[text][anchor]` in the prose.

THE MATH CHECK IS THE SUBTLE ONE AND TWO WRONG VERSIONS CAME FIRST.

  Version one counted `\\[` and `\\]` naively. `\\\\[2mm]` is a LaTeX line break with a spacing
  argument, legal inside `cases` and `array`, and it was counted as an opening delimiter. That
  reported a correct page as broken.

  Version two excluded any bracket preceded by a backslash. A display block whose last line
  ends in a line break closes as `\\\\\\]`, so the legitimate closing delimiter was discarded.
  That reported two more correct pages as broken AND masked the first error.

  Version three, below, is the correct rule. A run of N backslashes before a bracket is a
  MathJax delimiter exactly when N is ODD, because `\\[` is the delimiter and `\\\\` is a line
  break. Under it, all 167 math-carrying pages in the corpus balance.

CODE BLOCKS ARE EXCLUDED FROM THE MARKUP CHECKS. Articles about Jekyll and about MathJax
legitimately display `{% ... %}` and `$$` as their subject matter.
"""
import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import post  # noqa: E402

# A bracket preceded by an ODD-length run of backslashes is a delimiter. See the module
# docstring; this single rule is the difference between a clean report and three false alarms.
_DELIM_RUN = re.compile(r"(\\+)([\[\]()])")

_HEAD = re.compile(r"<head>.*?</head>", re.S | re.I)
_CODE = re.compile(r"<pre\b.*?</pre>|<code\b.*?</code>", re.S | re.I)

# Each entry is (name, pattern, code_blocks_count). When the third field is False the pattern
# is only applied outside <pre> and <code>, because those legitimately contain markup.
CHECKS = [
    ("unresolved-reference", re.compile(rf"\[[^\]\n<]{{2,90}}\]\[{post.ANCHOR}\]"), False),
    ("unexpanded-marker", re.compile(r"\{\{\s*[A-Za-z_][^}\n]{0,60}\}\}"), False),
    ("unrendered-liquid", re.compile(r"\{%\s*(?!raw\b|endraw\b)[a-z_]+[^%\n]{0,60}%\}"), False),
    ("raw-display-math", re.compile(r"(?<!\\)\$\$"), False),
    # The doubled-list-marker defect that shipped in A332 and A333: a generator emitting its
    # own bullet in front of a line that already had one renders as a nested empty list.
    ("empty-list-item", re.compile(r"<li>\s*</li>"), True),
    ("nested-empty-list", re.compile(r"<li>\s*<ul>"), True),
    ("double-escaped", re.compile(r"&amp;(nbsp|amp|lt|gt|#\d+);"), True),
    ("literal-nbsp-word", re.compile(r"\bandnbsp\b"), True),
]


def delimiter_counts(html):
    """(display_open, display_close, inline_open, inline_close) by backslash-run parity."""
    d_o = d_c = i_o = i_c = 0
    for run, br in _DELIM_RUN.findall(html):
        if len(run) % 2 == 0:
            continue
        if br == "[":
            d_o += 1
        elif br == "]":
            d_c += 1
        elif br == "(":
            i_o += 1
        else:
            i_c += 1
    return d_o, d_c, i_o, i_c


def audit_html(html):
    """Findings for one rendered page, as a list of (check, count, example)."""
    body = _HEAD.sub(" ", html)
    outside = _CODE.sub(" ", body)
    found = []
    for name, pat, in_code in CHECKS:
        target = body if in_code else outside
        hits = pat.findall(target)
        if hits:
            found.append((name, len(hits), str(hits[0])[:120]))
    # Delimiters are counted OUTSIDE code as well. A post about MathJax displays `\\(` and
    # `\\[` as its subject matter, and sample syntax in a code block is never rendered math.
    d_o, d_c, i_o, i_c = delimiter_counts(outside)
    if d_o != d_c:
        found.append(("math-display-unbalanced", abs(d_o - d_c), f"open {d_o} close {d_c}"))
    if i_o != i_c:
        found.append(("math-inline-unbalanced", abs(i_o - i_c), f"open {i_o} close {i_c}"))
    return found


def audit_site(site_dir):
    """Walk a built site. Returns (findings_by_page, pages_scanned, pages_with_math)."""
    findings, pages, with_math = {}, 0, 0
    for root, _dirs, files in os.walk(site_dir):
        for fn in files:
            if not fn.endswith(".html"):
                continue
            path = os.path.join(root, fn)
            try:
                html = open(path, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            pages += 1
            d_o, d_c, _i_o, _i_c = delimiter_counts(_CODE.sub(" ", _HEAD.sub(" ", html)))
            if d_o or d_c:
                with_math += 1
            rows = audit_html(html)
            if rows:
                findings[os.path.relpath(path, site_dir)] = rows
    return findings, pages, with_math


def report(site_dir):
    """Print the audit. Returns the number of pages carrying at least one finding."""
    findings, pages, with_math = audit_site(site_dir)
    totals = collections.Counter()
    for rows in findings.values():
        for name, n, _ex in rows:
            totals[name] += n
    print(f"rendered audit of {site_dir}: {pages:,} pages, {with_math:,} carrying display math")
    if not findings:
        print("  no findings")
        return 0
    for name, n in totals.most_common():
        print(f"  {n:6d}  {name}")
    print()
    for rel, rows in sorted(findings.items(), key=lambda kv: -sum(r[1] for r in kv[1]))[:20]:
        print(f"  {rel}")
        for name, n, ex in rows:
            print(f"      {name:26s} {n:4d}  {ex!r}")
    return len(findings)


def weights(site_dir, top=15):
    """Rendered byte size per page, heaviest first, with the corpus distribution.

    NOTHING MEASURED THIS UNTIL A PAGE REACHED 789 KILOBYTES. A comprehensive survey is a
    deliberate editorial choice and page weight is therefore NOT a defect and NOT gated here.
    It is reported because the two survey articles sit far outside the distribution of the
    other 460 pages, and an author should know that before the pattern repeats.
    """
    rows = []
    for root, _dirs, files in os.walk(site_dir):
        for fn in files:
            if not fn.endswith(".html"):
                continue
            path = os.path.join(root, fn)
            try:
                rows.append((os.path.getsize(path), os.path.relpath(path, site_dir)))
            except OSError:
                continue
    rows.sort(reverse=True)
    return rows[:top], rows


def report_weights(site_dir, top=15):
    heavy, rows = weights(site_dir, top)
    if not rows:
        print(f"no pages under {site_dir}")
        return 0
    sizes = sorted(sz for sz, _ in rows)
    total = sum(sizes)
    median = sizes[len(sizes) // 2]
    print(f"page weight over {len(rows):,} pages: total {total / 1e6:.1f} MB, "
          f"median {median / 1024:.0f} KB")
    print(f"  {'size':>10}  {'x median':>9}  page")
    for sz, rel in heavy:
        print(f"  {sz / 1024:9.0f}K  {sz / median:8.1f}x  {rel[:78]}")
    return 0


if __name__ == "__main__":
    import sys
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    flags = {a for a in sys.argv[1:] if a.startswith("-")}
    site = args[0] if args else "_site"
    if not os.path.isdir(site):
        print(f"no such directory: {site}\n"
              "usage: python3 _lib/render.py <built-site-dir> [--weights]")
        raise SystemExit(2)
    if "--weights" in flags:
        raise SystemExit(report_weights(site))
    raise SystemExit(1 if report(site) else 0)
