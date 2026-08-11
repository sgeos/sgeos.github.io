# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-11
**Task**: Rendered-output auditing, and repairing `lint.py` so it can be run at all.
**Committed and pushed.**

---

## The Corpus Had No Check That Sees What A Reader Sees

`_verify.py` and `_lib/lint.py` both read markdown source, so both can only predict what
kramdown and MathJax will do. **They disagreed with each other and with reality.** Run across
the corpus, lint reported **1,596 defect-severity findings** and the rendered pages carried
**none of them**.

`_lib/render.py` audits built HTML for defects a reader would see, being an unresolved
`[text][anchor]`, an unexpanded marker, unrendered Liquid, raw `$$`, empty or nested-empty list
items, double-escaped entities, and unbalanced MathJax delimiters. It runs in CI immediately
after the build.

**Markup inside `<pre>` and `<code>` is excluded**, because the Jekyll and MathJax tutorial
posts display that syntax as their subject matter. That exclusion is the difference between
zero findings and eleven false ones.

**Current state of the corpus: 462 pages, 167 carrying display math, no findings.**

**I proved the gate can fail rather than assuming it.** Injecting one of each defect class into
a built page produced four findings and exit 1, and restoring the page returned exit 0. A
checker that has never failed is not evidence of a clean corpus.

---

## The Math Check Was Wrong Twice And One Error Masked The Other

This is the part worth carrying forward, because two plausible implementations both produced
false alarms against correct pages.

- **Version one** counted `\[` and `\]` naively. `\\[2mm]` is a LaTeX line break with a spacing
  argument, legal inside `cases`, and it counted as an opening delimiter. One correct page
  reported broken.
- **Version two** excluded any bracket preceded by a backslash. A display block whose last line
  ends in a line break closes as `\\\]`, so the legitimate closing delimiter was discarded. Two
  more correct pages reported broken, **and this version hid the first error**.
- **Version three** is the rule: a bracket is a delimiter exactly when the run of backslashes
  before it has **odd** length. Under it every math-carrying page in the corpus balances.

Had I acted on either of the first two, I would have edited three correct published articles.

---

## `lint.py` Was Unusable Corpus-Wide And Is Now Clean

It had never been run over the corpus. Only `_lib/edits.py` and the tests call it. All 1,596
defect-severity findings were artefacts of two structural assumptions.

- **`references()` splits on a literal `## References` heading.** Two 2016 posts head their link
  block `## Links:`, so the block landed in the body, the reference block came back empty, and
  all 16 of their anchors read as undefined. Every one resolves.
- **Uses were counted in the body only.** The corpus convention puts the visible
  `- [text][anchor]` entry inside the References section, so **1,579 references read as defined
  but never used**.
- **`unfilled-template` scanned raw text.** `\frac{W_{avail}}{c(t)}` contains the literal bytes
  `{c(`, so a published article was flagged for dividing by a function of time.

Anchors are now counted across the whole document, which is what kramdown does, and the
template check strips math first. **Defect-severity findings across the corpus: 1,596 to 0.**

**The 2,025 convention-severity findings were left exactly as they are.** `lint.py` documents
that bold spanning a line break, display math on two lines and duplicate reference URLs were
measured against the corpus and deliberately not promoted to gates because kramdown renders
them correctly. I did not touch that judgement.

---

## Verification

- `python3 _verify.py` **0 errors, 0 warnings**.
- `python3 _lib/test_lib.py` **69 of 69**, up from 63. Six new tests cover the backslash-run
  parity rule, the code-block exclusion, unbalanced display math, the non-standard reference
  heading, the visible-entry-counts-as-a-use rule, and the LaTeX-versus-placeholder distinction.
- `python3 _lib/render.py _site` over a real build: **462 pages, no findings, exit 0**.
- **Gate proven to fail** on four injected defect classes and to pass again on restore.
- `lint.scan` across all 343 files: **0 defect, 2,025 convention**.

---

## Standing Work, Unchanged

**A334, the Boeing X-37**, editorial date 2025-11-12, Part 38 of 72, on your prompt.

**The thirty-seven X-Planes drafts remain unpublished and unauthorised.**
