# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-10
**Task**: A326 equation-density review, the second of four passes. Committed, **not pushed**.

**State: 8,028 lines, 69 display equations, 2,207 reference definitions, 46,399 words.** Thirty
articles drafted, all in `_drafts/`, **none published**.

---

## The Equation Pass

**29 to 69 across 23 edits**, references held at 2,207 and measured before and after.

The audit found the same three categories the last two articles did. **Quoted values with no relation
behind them**, the Vehicle table stating thirty-two numbers and displaying nothing while the
lift-curve slopes and lift-to-drag figures appeared from nowhere. **Relations used throughout and
defined nowhere**, being dynamic pressure, equivalent airspeed, the pitching moment derivative, the
drag polar and the induced drag factor. **And whole sections arguing quantitatively with no equation
at all**, the worst being the vehicle description and the instrumentation section.

---

## The Two Additions That Are More Than Bookkeeping

**The closed form of the untailored root**, which the draft never displayed although the entire sweep
argument rests on it. It splits the reciprocal boundary into a torsion term that is always positive
and a bending term **whose sign is the sign of the sweep**, which is the forward-sweep problem in one
line. It agrees with the eigenvalue solver **to one part in a billion at every sweep angle tested**,
and it gives the critical sweepback in closed form as **48.013 degrees**.

**That corrects a value the draft stated.** The draft said sweepback beyond about 47 degrees removes
the boundary, which came from an integer scan.

**The doubling time from rest.** A disturbance released with zero pitch rate follows cosh rather than
a pure exponential, so it doubles in arcosh(2) over lambda rather than ln(2) over lambda. **The ratio
is 1.900**, large enough to read as a real discrepancy if the two are confused. The article uses the
exponential figure throughout, which is the conservative one.

---

## A Closed Form Written and Then Deleted

**The candidate for the Southwell sensitivity was 1/(1 - r_max)**, which is clean and gives 1.600 at
the aircraft's own reach. The simulation gives 1.389, stable to three figures across a factor of ten
in noise.

**They disagree because they are not the same quantity.** The closed form is the amplification of the
twist at the topmost data point; the reported figure is the sensitivity of an eight-point
least-squares slope. **A clean form that lands near a measured number is not an explanation of it**,
so the article reports the simulated value and says it was simulated.

---

## One Finding Fell Out of the New Equations

**The sustained load factor at Mach 0.9 at sea level is 10.66 against an 8 g structural design
limit**, so the airframe rather than the engine is what binds low down. It follows from the
thrust-to-weight ratio exceeding unity at the manoeuvre design weight, which the Vehicle section now
computes.

**The keystone sensitivity is also derived rather than asserted.** Writing the inversion as
q_D = q r/(r - 1) gives an elasticity of -1.667 at r = 1.6, so a one percent error in the published
ratio is a 1.67 percent error in the boundary, and the two-significant-figure rounding costs 5.2
percent.

---

## Two Verifier Defects, Both Silent

**`require_in_text` appends to the failure list**, so calling it after `report` meant anything it
found was never printed, and it returns True when nothing is missing, so the guard around it was
inverted as well. **Together those made a silent check look like a passing one.**

**The coarse determinant scan quantises its root to the grid step**, producing apparent disagreements
with the closed form of up to 0.31 percent that were entirely the grid. A tolerance loose enough to
absorb that would have been looser than the quantity it was checking, so the scan now brackets and
then bisects.

The verifier now separates two kinds of check. `chk` records a value the article states so
`require_in_text` can insist it appears, while agreements between two computed routes use a separate
helper, because the article deliberately withholds the model's absolute divergence pressures and
demanding they appear would require printing numbers it has argued are meaningless.

---

## Verification

**88 of 88 independent checks passing, none importing the calculation.** The amplification derivation
is tested as a randomised property over the moment balance, the critical sweepback is reached both in
closed form and by bisection on the determinant scan, the cosh doubling is confirmed by Runge-Kutta
integration, and the sustained load factor is found by scanning for where thrust equals drag.
**All article-facing verified values are confirmed present in the draft.**

`_verify.py` at the 21-warning baseline, check_any clean, `_lib/test_lib.py` at 45 of 45, reference
integrity unchanged at 2,207 with zero undefined, zero orphaned, zero duplicate URLs and zero
search-endpoint citations, zero constructions above the corpus maximum after rotating two more across
two distinct phrasings, and a 30-article isolated build rendering **all 69 equations as display math
across 17 sections and 18 tables**.

**The citation sweep from the draft pass stands**, since the reference set did not change. 1,767 DOIs
registry-verified at zero unresolved, all 378 NTRS identifiers resolving, and all books and curated
URLs resolving.

---

## Awaiting Instruction

**A326 has completed the draft and equation passes.** The primary-reference and publication passes
remain, each on its own prompt.

**The audit now reports 49 displayed equations with no nearby citation**, which is the ninth
consecutive article in which an equation pass promotes subjects the reference base has to follow.
That is the reference pass's material.
