# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-06
**Task**: A307 primary-reference review, the third of four passes. Committed. **Not pushed.**

---

## Baseline, Which Was Already the Best in the Series

128 primary documents of 208 external, or **61.5 percent**. That is higher than any article this series
has produced, so the deficit was never the share. It was coverage and count.

The instrument that found the real deficit was a **citation-coverage audit by section**, which counted
citations per thousand words the way the equation audit counts equations. It found **fourteen sections
over 200 words at or below four citations per thousand**, and every one of them was a section the
equation pass had either created or expanded.

**That is the third article running in which the equation pass has arrived without its period sources.**
The rule is written down and I still had to rediscover the extent of it by measuring. The harvest was
therefore aimed at the equation pass's topics rather than at the article's original ones.

---

## Result

A supplementary harvest of 33 NTRS, 22 DTIC, and 16 period queries returned 129 new NTRS, 181 new DTIC,
and 151 new period records, taking the master index from 1034 to 1448 entries. **53 primary documents
added across 21 edits.**

References **218 to 271**. Primary sources to **181 of 239 research, 75.7 percent, and 69.3 percent of
external**. Both are the highest in the series by a substantial margin, against A306 at 61.2 percent
before its contemporary additions grew the denominator.

**Coverage is now three thin sections against fourteen**, and all three are synthesis sections that
correctly carry no citations, namely the aircraft-category discussion, the Epistemic State, and the
Conclusion.

---

## The Strongest Finding

**The article's central analytical move had no vocabulary in 1953.**

Identifiability as a property of a system rather than of an estimator was formalised by Aoki in 1966 and
by Staley and Yue in 1970, a decade and more after the programme ended, and the estimation machinery
that would have separated the two error terms is later still. The X-10 was asked to measure a parameter
at a time when the question of whether a parameter is measurable had not yet been posed as a question.

That is the fairest available account of why nobody noticed the observation window was the wrong length,
and it is a better answer than the article previously had, which was silence.

Other threads closed. Circular error probable as a contested statistic rather than a given, including
what a bias does to it, which matters here because a drift rate is a bias and not a noise. The geodetic
literature behind the deflection-of-the-vertical term, together with the gravity-gradiometer aiding that
eventually answered it two decades too late. Inlet and engine airflow matching, whose vocabulary
postdates the X-10's inlet design entirely. Radio propagation and the range-height-angle charts behind
the horizon calculation. What a test range can actually measure, and with it the observation that
**nothing in the accessible record states the Atlantic Missile Range's own tracking error for these
flights**, which bounds how well the X-10's navigation error could have been known at all. The period
ballistic-trajectory theory the cancellation derivation rests on, so that derivation is now shown to be
period material rather than a modern reconstruction. And the redundancy and availability literature
behind the reliability arithmetic.

---

## Verification

271 references with zero undefined, zero orphaned, and zero duplicate URLs. **All 66 fixed identifiers
at 200 and all 180 DOIs Crossref-resolved on title at the 0.85 threshold with zero flagged.** The
article still contains no hand-entered identifier anywhere. All 102 worked values still reproducing.
`_verify.py` at the 0-error 21-warning corpus baseline. Zero contractions, em-dashes, en-dashes, prose
colons, prose semicolons, prose parentheticals, doubled words, duplicate headings, display-math seam
defects, or link texts out of sync. Isolated build succeeding with 122 rendered display blocks and Part
11 navigation.

**Two seam defects found by reading and not by any check.** The error-budget citation insertion split
the finding that the budget does not close from the three readings that resolve it, and the cancellation
insertion left a nine-item citation cluster inside the paragraph carrying the argument. Both repaired by
moving rather than rewriting. Sixth article in which a seam defect survived every automated check.

---

## A Durable Toolchain Repair

The manual correction of a Crossref OCR artefact in an author display had been applied to the master
table directly, and was **silently lost** when the table was regenerated for the supplementary harvest.
It is now in the normaliser and survives regeneration.

The known rule was that reference-text defects belong in the master table rather than in the markdown,
because the markdown is regenerated. The extension is that **a table which is itself regenerated is not
a source of truth either**, and the fix has to live in whatever produces the last artefact in the chain.

---

## State

**1181 lines, 122 display equations, 271 references, 16,090 words.**

Equations and references are inside band. **Lines remain 119 short of the 1300 floor**, reported rather
than padded.

**Contemporary coverage is 55 references, or 23.0 percent of dated**, an absolute count well below the
101 to 155 of A301 through A306. That is the publication review's principal task, and closing it is also
expected to close the line shortfall, which is what happened in A305 and A306.

**Committed, not pushed.** The publication-order dependency is eleven deep. **Categories remain
undecided** at `aerospace history engineering`, now raised twelve times.
