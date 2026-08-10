# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A369 pathological word-usage pass. Committed and pushed. **Not published.**

**57 edits.** 4,789 to 4,787 lines, 54 display equations and 1,765 references held.

---

## The Method Was the Finding

**Constructions were measured against twenty-seven peer drafts in the same voice, not against fixed
thresholds.** A fixed threshold cannot tell a subject noun from a tic. `instruction` at 5.41 per thousand
looks alarming until one notices it is what the article is about.

**Five constructions exceeded the maximum of the entire corpus.**

| construction | A369 before | peer median | peer max |
|---|---|---|---|
| `and not` | 2.19 | 0.36 | 1.73 |
| `worth` | 1.77 | 1.05 | 1.61 |
| `the second is` | 0.59 | 0.06 | 0.19 |
| `in which the` | 0.59 | 0.17 | 0.50 |
| `outright` | 0.17 | 0.00 | 0.14 |

All five are now inside range, and nothing sits above the corpus maximum.

---

## The Worst One Was Self-Inflicted

**The primary-reference pass created it.** That pass found `rather` at 6.0 per thousand against the
verifier's limit of 5.0 and mechanically rewrote fifteen instances of `rather than` to `and not`. The
count came down and the limit was cleared. **What actually happened is that one tic was traded for
another**, and the replacement was pushed past every article in the corpus.

**A mechanical substitution is not an edit.** The 57 replacements here are varied deliberately, and the
load is spread across `instead of`, `never`, comma-not and outright restructuring, **each of which now
sits below the corpus maximum instead of one absorbing all of it**.

`worth` was cut from 22 occurrences to 3, because it is mostly announcement. A sentence saying that a
point is worth stating says less than the point does. `rather than` fell from 60 to 42, from 5.05 to 3.55
per thousand, now below the peer median of 4.00.

**The word named in the prompt was not a problem here.** `specific` stands at 0.68 per thousand against a
peer median of 0.99 and a maximum of 1.91, and `specifically` appears twice.

---

## A Separate Finding, and It Concerns the Verifier

**`prose_text` in `_verify.py` strips math, code and Liquid but not `[text][anchor]` link pairs.**

The consequence is that the 1,650 harvested paper titles count as prose. They inflate the denominator
from 11,800 words to 27,178 and **dilute the word-frequency check into insensitivity**. That is why CI
reported nothing while two constructions sat above the corpus maximum.

**In the reference-heavy regime established at A318, this check is much weaker than it looks.** The
analysis here was therefore run twice, once as the verifier sees the file and once over author prose
only, and only the second was informative.

**This is a real gap in the tooling and I have not changed `_verify.py`**, since that is a corpus-wide
behaviour change affecting 297 posts and is the pilot's call. The two candidate fixes are stripping link
pairs in `prose_text`, which makes the check sensitive again but shifts every existing rate, or leaving
it and treating the prose-only measurement as a manual step in the publication pass.

---

## Verification

`_verify.py` reports zero errors and no style or word-frequency warning for this article. Prose clean
with zero em dashes, en dashes, prose colons, prose semicolons or parentheticals beyond front matter and
the permitted `console.log` tag, zero unbalanced bold, zero split link pairs, zero glued headings, all 54
display equations on single lines, and **24 apostrophes programmatically confirmed to be possessives with
zero contractions**.

Isolated production build over the full 297-post tree succeeds, with 54 equations rendering, 1,791
resolved identifier anchors, zero unresolved links and zero Liquid errors.

---

## Awaiting Instruction

**The article is complete through four passes plus this one, committed and pushed. It has not been
published** and remains in `_drafts/`.

**Two questions are open.** Whether siblings in the `keleusma_native` series are planned, since navigation
reads Part 1 of 1. And whether `_verify.py` should strip link pairs from `prose_text`, which would restore
the word-frequency check in the reference-heavy regime at the cost of shifting every recorded rate.
