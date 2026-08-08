# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A311 equation-density review, the second of four passes. **Committed, not pushed.** All
fifteen articles in the series remain in `_drafts/`.

---

## The Pass Corrected a Claim This Series Has Been Carrying Since A310

This is the most consequential thing the review did and it deserves to come first, because the error
was inherited rather than introduced.

The draft said, following the previous article, that **position is the third integral of the pilot's
control input** and that a hovering pilot closes a loop around a triple integrator. A310 reached that
by reasoning that position is the double integral of attitude and **attitude is the integral of
whatever the control does**. The second clause is the one that does not survive being written down.

A reaction nozzle produces a moment. A moment produces angular *acceleration*. So attitude is the
**double** integral of control, and composing the two gives

**x(s)/u(s) = g CP / s⁴**

**Position is the fourth integral, not the third.**

**The reconciliation is that the earlier description is the low-frequency case.** Restoring the rate
term gives g CP / (s³(s + D/I)), which behaves as third order below the damping break frequency and
fourth order above it. So **hovering is a third-order problem or a fourth-order one depending on how
much damping the aircraft has**, and an aircraft with neither aerodynamic nor artificial damping is in
the harder case.

**This is not a quibble about counting.** A fourth-order plant demands two derivatives of lead from
the pilot rather than one. That is the clearest available explanation of why the 1972 Ames simulator
work found that **attitude stabilisation gives the best handling qualities for the least control
power** — it does not merely help the pilot, it removes two orders from the plant being closed around.

**The X-14A is the only aircraft in this series that could have demonstrated the distinction**, because
it is the only one whose damping was a dial. The correction is recorded in the Epistemic State as a
correction to the previous article rather than buried.

---

## Four Further Results the Pass Produced

**An optimally flown hover correction splits its time exactly in half.** The stationarity condition
solves to θ\* = ½√(CP·d/g), and substituting back makes the attitude term and the translation term
equal. **Half the time changing attitude and half translating, whatever the control power and whatever
the distance.**

**The wind is a position problem, not an attitude problem**, which is the same conclusion the previous
article reached for the X-13 by a different route on a differently shaped aircraft. A ten metre per
second wind is 5.9 percent of maximum control power as a moment, but it demands a permanent 1.36
degree tilt and costs 11.7 metres of drift in ten seconds uncorrected. **So the disturbance that sizes
the control power is the gust and the manoeuvre, not the steady wind.**

**The overhead compounds, and now it is stated as a product.** Control takes 34.9 to 51.8 percent of
the hover margin, and the disturbance allowance takes two fifths of what that bought. **Only 21 to 31
percent of the margin reaches the pilot as manoeuvring authority.**

**The pitch nozzle must be about forty percent stronger than the roll nozzle** for the same control
power, because the moment arms differ and the X-14 is wider than it is long. And the J85-GE-19 bought
about **590 pounds more lift** than the J85-GE-5, which is what set how much authority the later
experiments could afford to give away — not the digital computer.

---

## Two Defects in the New Spine, Both Caught by Running It

**The closed form for the optimum tilt was simply wrong.** I wrote it as (CP·d/4g)^(1/3), which misses
the numeric optimum by six degrees. The correct form is ½√(CP·d/g), and printing the numeric and the
closed form side by side is what exposed it. Had the numeric alone been reported the article would
have been right by accident and the general relation wrong.

**The diverter section printed a hardcoded constant** where it claimed to sweep the deflection angle,
so its whole table was meaningless. Replaced with the actual component relations.

A pronoun for a generic pilot was also corrected to the neutral form.

---

## Verification

**103 display equations, up from 51 across 22 edits, and nothing trimmed.** All 31 newly introduced
numbers re-derived independently and reproducing, on top of the 45 from the draft pass. `_verify.py`
at the 0-error 21-warning corpus baseline from the repository root. Zero contractions, em-dashes,
en-dashes, prose colons, prose semicolons, prose parentheticals, doubled words, duplicate headings,
unbalanced emphasis markers, lone dollar-delimited lines, or adjacent display-math seams. Genre
section order unchanged and correct.

Isolated build succeeding with **103 rendered display blocks matching the source count exactly**, Part
15 navigation, no unresolved reference links and no surviving Liquid tags.

---

## State

**1088 lines, 103 display equations, 95 references, 15,001 body words.**

**Equations are inside the 90 to 130 band.** Lines at 1088 against a 1300 floor and references at 95
against a 250 floor both still approach from below, which the remaining two passes close.

**Committed, not pushed.** Nothing in this series is published. The publication-order dependency is
fifteen deep, A311 back to A297. **Categories remain undecided** at `aerospace history engineering`,
fifteen articles deep and raised nineteen times.

The next pass is the primary-reference review. The A311 harvest and the combined A310 master hold 2,419
entries, of which 72 are cited, so the material is there.
