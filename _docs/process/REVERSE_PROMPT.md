# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-10
**Task**: A324 publication review, the fourth and final pass. Committed and **pushed**. **Not published.**

**Final state: 9,895 lines, 77 display equations, 2,803 references, 37,006 words.** All twenty-eight
articles in the series remain in `_drafts/`.

---

## The Contemporary Survey

**Contemporary coverage 595 to 1,535 references, or 33.8 to 56.8 percent.** A fourth harvest of 70
Crossref and 8 NTRS queries took the modern pool from 931 to 1,615.

**The survey went from seven subsections to eleven, and each new one answers something the article's own
analysis raised rather than filling a gap in the outline.**

- **Ram drag and high-speed propulsion integration.** This is the keystone's other half and the draft
  survey never reached it. It is live again under supersonic civil transport and variable-cycle engines.
- **Aerothermoelasticity.** The article computes a thermal stress by hand. The modern name for that
  computation is a coupled thermal-structural problem in which the deformation changes the flow doing
  the heating.
- **Derivative and legacy design.** **The one contemporary thread that takes the article's own subject as
  its object of study.** The Lancer kept the F-104's aerofoil and thickness ratio, and pricing that
  inherited constraint is now a research subject.
- **Evaluating an aircraft that was never built.** Surrogate modelling, uncertainty quantification,
  model-based systems engineering. **This is the closest thing to a resolution the article's central
  difficulty has, and it arrived fifty years late.** The article notes that its own analysis is a
  primitive version of the same idea.

---

## The Count-Versus-Fraction Trap Caught This Article From Both Ends

**At the reference pass**, the contemporary count sat unchanged at 595 while its fraction fell, because
the period base was growing underneath it.

**At this pass, the reverse.** The period count sits unchanged at **912** while its fraction falls from
51.8 to 33.8 percent. The primary count **rose**, from 1,176 to 1,188, while its fraction fell from 66.8
to 44.0.

**Neither movement is a fact about coverage. Both are facts about the denominator.** The Source Base now
says this in the article rather than leaving the fractions to be misread as a regression.

---

## Defects Found and Fixed

**The NASA defect recurred for the third consecutive article.** It was used without being spelled out,
including inside link text, which is prose in this corpus. Both occurrences now read National Aeronautics
and Space Administration. **`US gallons` corrected to United States gallons.**

**Two em dashes in table cells**, used as placeholders rather than as prose. Removed anyway, because the
rule is absolute.

**One prose semicolon that I introduced in this very pass**, caught by the checker immediately after the
edit that created it.

**One capitalised emphasis**, `DIFFERENCE`, converted to bold. Emphasis is bold and never capitals.

**Three section headings carried no prose at all** and rendered as a heading immediately followed by a
subheading. Each now has an orienting sentence.

---

## Diction

**Zero constructions above the corpus maximum**, measured against 27 peers. `rather than` sits at 4.61 per
thousand against a peer median of 4.12 and a maximum of 6.78.

**It was left alone deliberately.** The article repeatedly contrasts what was done with what was not, so
the construction is doing real work, and **the A369 lesson is that a mechanical substitution creates a
worse tic than the one it removes**. `mach` at 6.18 per thousand is the article's own subject noun.

---

## Verification

105 numerical checks passing unchanged. Reference integrity at 2,803 with zero undefined, zero orphaned
and zero duplicate URLs. **Zero search-endpoint citations**, the defect A297 left open and which this
article has never had. `_verify.py` at the 21-warning baseline, 45 of 45 library tests, and a 28-article
isolated build with all 77 equations rendering across 18 sections and 45 subsections.

**The 940 references added this pass were swept by source type**: 11 of 11 NTRS resolve, 120 of 120
sampled Crossref DOIs are registered, 1 of 1 DTIC is registered, and all 75 hand-curated URLs resolve.

---

## State

**Pushed to `origin/master`.** The deploy builds without `--drafts`, so the article is not served. Nothing
is outstanding.

---

## Awaiting Instruction

**A324 is complete through all four passes.** Twenty-eight of seventy-two drafted, **none published**.

The next article to draft is **A325, the Osprey X-28 Sea Skimmer**, editorial date 2025-11-03, series
index 29. It is the other side of the X-27: a homebuilt single-seat flying boat that the Navy bought and
actually flew, after a study into patrol aircraft that had to cost under five thousand dollars. **After
three consecutive designations that did not go to research aeroplanes, A325 returns to an aircraft that
existed** and is the fourth consecutive off-the-shelf purchase, which is worth watching for the closing
article.
