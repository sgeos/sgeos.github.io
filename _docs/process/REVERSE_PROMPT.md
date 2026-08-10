# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-10
**Task**: A324 equation-density review, the second of four passes. Committed, not pushed, not published.

**39 display equations to 77 across eighteen edits.** 6,066 to 6,292 lines, 23,720 to 25,265 words.
References held at 1,650 and measured before and after.

---

## What Was Missing, in Three Categories

**Quoted values whose relation was absent.** The density 0.3796, the Mach 2.563, the Reynolds number
3.598 × 10⁷ and the viscosity inside it all appeared as numbers with none of the four relations shown.

**Relations named in prose and never written.** The draft **named the Oswatitsch result by that name**
without stating it. Worse, it displayed specific excess power while never displaying **energy height, of
which specific excess power is the derivative**, so it showed a rate without its quantity.

**Arguments resting on an undisplayed relation.** The climb claim fails because specific excess power is
a ceiling on rate of climb, and **that inequality is the entire argument and was nowhere written**. The
takeoff section said the roll came from integrating the acceleration and showed no integral.

---

## Two Corrections to Numbers Already in the Draft

**The specific excess power peak was computed on a four-point grid.** The draft reported 48,585 feet per
minute at Mach 1.2 and a 23.5 percent shortfall against the claim. A fine scan puts the peak at **49,332
at Mach 1.095, so the shortfall is 21.6 percent**. The article now states the correction and why.

**The verifier did not catch it, and the reason is worth recording.** Its tolerance on that value was
three percent and the error was one and a half. **A tolerance wider than the quantity it is checking is
not a check.** It is now 0.2 percent.

**The Oswatitsch comparison was unfair in the draft's favour.** The equal-strength search ran
unconstrained while the free search was capped at twenty-five degrees of total turning, so the equal pair
appeared to win by exceeding a limit the other obeyed. Under the same cap the free optimum wins by 0.010
points at Mach 2.0 and 0.104 at Mach 2.6, **which confirms the theorem rather than contradicting it**.

---

## The Addition That Matters Most

**Ram drag was absent from the draft entirely**, which is a serious omission in an article asking whether
a turbofan can work at Mach 2.6.

The free stream arrives at 771 metres per second, so the engine must first cancel 20,441 pounds of
momentum, and **45.0 percent of gross thrust is spent on the air's own momentum**. Inverted rather than
asserted, since holding the sea-level rating across the Mach range is not defensible, the rated net
thrust requires an exhaust velocity of 1,714 metres per second against 943 static.

**That is within reach of an afterburning nozzle, but it needs total pressure at the engine face, which
is exactly what the inlet section showed the single cone failing to deliver.** The two halves of the
keystone turn out to be one problem seen from either end, and the draft had not connected them.

---

## A Second Structural Objection, and a Negative Result

**The thermal section argued only half its case.** Losing yield is not all that heating does. A restrained
skin at the Mach 2.6 excursion develops 316 megapascals against 275 of retained yield, **at 115 percent**.
That is an upper bound rather than a prediction, so the relation is inverted: **83 kelvin of
skin-to-substructure differential consumes half the remaining strength**, which is not much for a thin hot
skin over cooler frames.

**And one expectation did not survive being written down.** The far-field downwash gradient goes as one
over aspect ratio, which invites the conclusion that a low-aspect-ratio wing washes its tail harder. **The
lift-curve slope falls with aspect ratio at nearly the same rate**, so the F-104 exceeds the F-5E by eight
percent rather than by the large factor the framing implied. Reported as a negative, and the tail-position
argument now rests on wake geometry, where it belongs.

---

## Verification

**59 to 105 checks, all passing, none importing the calculation.** The thermal stress is reached by
bisecting for the temperature that produces it rather than by evaluating it, the ram result by closing the
momentum balance rather than repeating the formula, and both the downwash flatness and the
turn-rate-against-radius consistency as randomised properties. **All 95 verified values were required to
appear in the draft text and all 95 do.**

`_verify.py` at the 21-warning baseline, check_any clean, 45 of 45 library tests, reference integrity
unchanged at 1,650 with zero undefined and zero orphaned, and a 28-article isolated build with **all 77
equations rendering as display math, zero doubled backslashes and zero unbalanced braces**.

---

## What the Next Pass Inherits

**The reference base must now follow the equations, which is seven articles running.** 47 of the 77
equations carry fewer than three citations within nine hundred characters. The newly promoted subjects at
or near zero are:

- **thermal stress and restrained thermal expansion**
- **ram drag, net thrust and propulsive efficiency**
- **the downwash gradient, tail volume and static margin**
- **energy height and the climb ceiling**
- **the takeoff ground roll**

**Reported as a target list rather than acted on**, since the passes are separate and reference work
belongs to the next prompt.

---

## Awaiting Instruction

**A324 has completed two of four passes.** The expected next prompt is the primary-reference review.
