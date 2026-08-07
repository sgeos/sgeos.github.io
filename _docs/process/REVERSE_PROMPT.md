# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-07
**Task**: A308 equation-density review, the second of four passes. Committed. **Not pushed.**

---

## Baseline and Result

54 display equations across 8697 body words, 6.2 per thousand. **38 added across 18 edits**, taking the
article from 678 lines and 54 equations to **854 and 92**, which is inside the 90 to 130 band. The
structural audit found no orphaned or duplicate subsections, and no zero-equation subsection over 180
words remains against two at baseline.

---

## The Pass Corrected the Draft's Own Claim

The draft wrote the staging-gain relation down and then asserted, without evaluating it, that the gain
was modest. Evaluating it gives **1044 metres per second for a three-tonne jettison, or twelve percent
of the whole ideal velocity.**

The intuition was wrong for a reason worth keeping. **The benefit of staging depends on the ratio of
jettisoned mass to burnout mass, not to gross mass.** Three tonnes of engine against a burnout mass of
5395 kilogrammes is an enormous fraction even though it is under three percent of the vehicle at
lift-off. So the one-and-a-half stage arrangement captures most of the value of staging rather than
giving it up, and the balloon tank is what makes the burnout mass small enough for that to be true. The
two decisions reinforce each other instead of trading against each other, which is the opposite of what
the draft said, and the section was rewritten.

**This is the second time in this article that writing a relation down caught a claim the prose was
carrying on assertion.** It is now the standing argument for the equation pass existing at all.

---

## The Pass Also Explained the Article's Headline Number

The five pounds per square inch of standing nitrogen is the vehicle's most quotable fact and the draft
reported it without accounting for it. Inverting the buckling relation for the pressure that produces
an equal axial tension gives

**2.58 pounds per square inch at the governing heavy gauge**, so the reported five-pound specification
carries a margin of 1.94 on the calculation. A specification at roughly twice the computed requirement
is what a designer writes when the requirement rests on a knockdown factor he does not trust, which is
exactly the situation the article describes two sections earlier.

---

## Other Relations Now Shown

Euler column buckling of the whole vehicle at 121 times the empty weight, which rules out the global
mode and establishes that local shell buckling is the failure. The fixed hoop-to-axial ratio of two,
which is why a tank splits lengthwise. Tank volume and propellant split, with the finding that **52.6
kilogrammes of nitrogen holds up 5395 kilogrammes of steel, a ratio of 103 to one**. The acoustic
environment at 153 decibels and 883 pascals at thirty metres. The pogo coupling condition against a
53 hertz solid-bar mode. The Allen and Eggers result that peak reentry deceleration is independent of
ballistic coefficient, giving **64 g for the reentry body against 3.44 for the booster that launched
it**. Boil-off at seven and a half percent of the oxygen load per hour. Maximum dynamic pressure of
9736 pascals, which is **two percent of the internal tank pressure** and is the clearest statement of
where this structure's loads come from. The aerodynamic bending moment at three percent of the
pressure-stabilised capacity. The proof and burst factor chain. The tank figure of merit at under seven
kilogrammes per tonne of propellant. The four-to-one experimental scatter in shell buckling with the
design factor sitting at the eleventh percentile of the observed band.

**And the orbital comparison, which is the best single addition.** Circular orbital speed at two hundred
kilometres is 7788 metres per second against the 7193 an intercontinental trajectory needs, a difference
of 595 or seven percent of the ideal velocity. **An intercontinental ballistic missile is already
ninety-two percent of the way to orbit.** That is why every early space programme was built on a
ballistic missile and none on a cruise missile, and it is the deepest reason the Atlas outlived the
Navaho by six decades.

---

## Verification

All 42 new worked values re-derived independently, with **one correction**. The pressure fluctuation at
153 decibels was first written as roughly six hundred pascals and is 883. The relation was rewritten to
compute it from intensity directly rather than from the rounded sound pressure level, which removes the
rounding sensitivity that produced the discrepancy.

All 78 previously verified values still reproducing. Zero duplicate headings, zero display-math seam
defects, zero lone dollar-delimited lines, zero paragraph-repeated citations. Zero contractions,
em-dashes, en-dashes, prose colons, prose semicolons, or prose parentheticals. 92 rendered display
blocks confirmed in the built HTML against 92 in the source, with Part 12 navigation, no unresolved
reference links and no surviving Liquid tags. `_verify.py` at the 0-error 21-warning corpus baseline.

---

## State

**854 lines, 92 display equations, 160 references, 11,180 words.**

Equations are inside band. **Lines remain 446 short of the 1300 floor and references 90 short of the
250 floor**, and that gap is larger than it was at the same point in A307, which stood at 1111 lines
and 218 references after its equation pass. The two remaining passes have correspondingly more to do
here, and the primary harvest should be aimed at what this pass opened, namely shell stability under
combined loading, acoustic and vibration environments, cryogenic boil-off and loading, reentry body
dynamics, and the launch-vehicle transition.

**Committed, not pushed.** The publication-order dependency is twelve deep. **Categories remain
undecided** at `aerospace history engineering`, twelve articles deep and raised fourteen times.
