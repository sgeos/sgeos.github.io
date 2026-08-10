# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-10
**Task**: A327 equation-density review, the second of four passes. Committed, **not pushed**.

**State: 5,193 lines, 54 display equations, 1,375 reference definitions, 30,357 words.** Thirty-one
articles drafted, all in `_drafts/`, **none published**.

---

## The Equation Pass

**22 to 54 across 17 edits**, references held at 1,375 and measured before and after.

The audit found the same three categories, **now ten articles running**. The thrust table stated
sixty-eight numbers and showed no substitution. Specific impulse appeared in a column heading and was
never defined. Mach number and the speed of sound were used on every page and never written down. The
inlet section argued quantitatively with no equation at all.

---

## The Best Addition Answers a Question the Draft Raised and Dropped

**The draft asserted that inlet unstart is catastrophic and never said why it is irreversible.**

A fixed-geometry inlet at Mach 20 can **self-start at a contraction of at most 1.657** and can **run at
15,377**, a ratio of **9,279**. The starting limit barely moves across the whole Mach range while the
running limit grows without bound.

**So a hypersonic inlet is started at low speed and must never let go**, because it cannot restart at
speed. That is the clearest single reason the flowpath cannot be treated as a component.

---

## A Bound That Owes Nothing to Any Engine Model

Reaching orbit takes 30.33 megajoules per kilogram of kinetic energy plus 1.90 of potential, or
**32.24 MJ/kg**. Hydrogen carries 119.96. **So the fuel fraction cannot fall below 26.9 percent**
however perfect the engine.

**The integrated ascent gives 45.44 percent, which is 1.69 times the floor.** That is the strongest
available evidence that the integration is not producing a fantasy, because a result below the bound
would have been proof of an error.

**And the other explosive quantity is now stated.** The draft discussed the thermal problem at length
and never mentioned that the structural one grows faster. The total-to-static pressure ratio reaches
**2.245 × 10⁷ at Mach 25**.

---

## The Verifier Caught a Wrong Number in the Article Itself

**The static temperature at 27 km is 223.7 kelvin and the draft wrote 220.6**, which made the
displayed line internally inconsistent, because 220.6 times 13.8 is 3,044 rather than the 3,086 the
line claimed as its own answer.

**An arithmetic line that does not evaluate to its own stated result is the easiest defect to ship and
the hardest to notice**, because both numbers look reasonable in isolation.

---

## Other Additions Worth Noting

**The vehicle-level bridge.** A ten square metre capture at Mach 20 gives 184.9 kilograms per second,
and **an engine developing 1,260 kilonewtons of gross thrust pushes the vehicle with 73**.

**The worked substitution at seven thousand metres per second**, which shows the exhaust leaves only
143.8 metres per second faster than the air arrived.

**The equivalence-ratio trade.** Running at three times stoichiometric nearly quadruples net thrust and
cuts the amplification from eighteen to five and a half, and consumes the same hydrogen the cooling
system needs.

**The ignition margin**, showing 26 to 258 ignition delays fit inside the residence time, which
confirms that mixing rather than chemistry is the limit.

---

## Verification

**98 of 98 independent checks passing, none importing the calculation.** The Kantrowitz contraction is
reached both in closed form and by bisection, the inequality that an inlet can always run at more
contraction than it can start at is tested as a randomised property, and every worked substitution is
re-derived. **All article-facing verified values are confirmed present in the draft.**

`_verify.py` at the 21-warning baseline, check_any clean, reference integrity unchanged at 1,375 with
zero undefined, orphaned or duplicate URLs, **zero constructions above the corpus maximum after
rotating three across three distinct phrasings**, and a 31-article isolated build rendering **all 54
equations across 17 sections and 18 tables**.

---

## Awaiting Instruction

**A327 has completed the draft and equation passes.** The primary-reference and publication passes
remain, each on its own prompt.

**The audit reports 26 displayed equations with no nearby citation**, and this pass promoted the
inlet-starting and orbital-energy subjects that no cluster was ever written for. That is the reference
pass's material.
