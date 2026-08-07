# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-07
**Task**: A308 primary-reference review, the third of four passes. Committed. **Not pushed.**

---

## Baseline

79 primary of 149 external, or **53.0 percent**, which is below A307's 61.5 baseline, and only 11 NTRS
records cited. That last figure was the tell. An article whose keystone is shell stability should not be
drawing eleven documents from the aerospace archive, and the supplementary sweep confirmed it.

The citation-coverage audit found **eleven sections over 180 words at or below four citations per
thousand**, and every one was a section the equation pass created or expanded. **Fourth article running.**

---

## Result

A supplementary harvest of 43 NTRS, 20 DTIC, and 18 period queries returned 158, 171, and 172 new
records, taking the master index from 845 to 1289 entries with zero duplicate URLs. **74 primary
documents added across 22 edits.**

References **160 to 234**. Primary sources to **153 of 212 research, 72.2 percent, and 68.6 percent of
external** — the highest in the series, against A307's 69.3 percent peak.

Coverage is now **four thin sections against eleven**, and three of the four are synthesis sections that
correctly carry no citations.

---

## The Best Find

**The measurement the article's keystone section describes was actually made, and the article did not
know it.** [Miller and Gerus 1966] reports the bending strength of a large thin-walled
pressure-stabilised cylinder, which is precisely the relation the equation pass derived, tested on
hardware of the right size. I had derived $M = \pi p r^{3} / 2$, computed with it, and drawn the
article's central conclusion from it, without knowing the period had measured the same thing directly.

The second find explains a choice the article had only described. **Peterson 1960 correlates measured
buckling strength of pressurised cylinders against the pressure parameter**, which is the empirical form
the design offices actually used, and Babcock and Sechler in 1962 and 1963 measure how much of the
classical strength an initial imperfection removes. That is why the allowable is a knockdown factor
rather than a theory.

---

## What Else Closed

**Ground-wind induced oscillation on the pad**, which the article had omitted entirely. A slender vehicle
in a steady wind sheds vortices and can be driven into resonance, and for a pressure-stabilised vehicle
the pressure resisting it is the standing five pounds rather than the flight sixty. The period devoted a
whole meeting to the problem.

Sonic fatigue as a named discipline with its own test methods and statistical machinery. Cryogenic
pressurisation, autogenous systems, and pre-launch conditioning. The period trajectory and staging
machinery the range table rests on. And the reentry deceleration result, which **Scherberg and Rubin
computed in 1953, four years before the X-11 flew**, so the article's use of it is period practice rather
than hindsight.

---

## A Defect I Introduced and Repaired Inside the Pass

The additions drove the leading citation construction to **39.1 percent**, against a house norm of 20 to
27, because I did not vary the construction while writing. Fifty-four rotations brought it to **18.8
percent** with the top actual construction at 3.2 percent.

The rule says to vary while writing rather than afterwards, and it is the third time this session that a
rule has held while followed and failed the moment it was skipped.

---

## Verification

234 references with zero undefined, zero orphaned, and zero duplicate URLs. **All 23 fixed identifiers at
200 and all 192 DOIs Crossref-resolved on title at the 0.85 threshold with zero flagged**, and this
article contains no hand-entered identifier anywhere. All 78 worked values still reproducing.
`_verify.py` at the 0-error 21-warning corpus baseline. Zero contractions, em-dashes, en-dashes, prose
colons, prose semicolons, prose parentheticals, doubled words, duplicate headings, or display-math seam
defects. Isolated build succeeding with 92 rendered display blocks, Part 12 navigation, no unresolved
reference links and no surviving Liquid tags.

---

## State, and a Warning About the Last Pass

**940 lines, 92 display equations, 234 references, 12,447 words.**

Equations are inside band. References remain 16 short of the 250 floor, which the publication review will
close comfortably since it added 96 to A307.

**The line count is the problem.** At 940 against a 1300 floor the gap is 360 lines, and that is larger
than any article in this series has carried into a publication review. A307 entered its final pass at
1181 and finished at 1329, a gain of 148. A gain of that size here would finish at about 1090, which is
short of band.

The contemporary work therefore has to be substantially larger than usual, and the threads this pass
opened are the ones to aim it at, namely shell stability under combined loading and modern knockdown
methods, ground-wind and buffet loads, sonic fatigue and acoustic environments, cryogenic tank
pressurisation and boil-off, and reentry body dynamics. If it still finishes short I will report the
shortfall rather than pad, per the standing rule.

**Committed, not pushed.** The publication-order dependency is twelve deep. **Categories remain
undecided** at `aerospace history engineering`, twelve articles deep and raised fifteen times.
