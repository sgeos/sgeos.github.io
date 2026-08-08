# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A316 drafted, the first of four passes. Committed, **not pushed**, per the rhythm. **Not
published.** All twenty articles in the series remain in `_drafts/`.

---

## The Handoff Was Right and the Keystone Does Not Transfer

You warned me not to assume the X-18's keystone carried over, and it does not. **A tilt-wing must keep
its wing flying at absurd angles, so slipstream immersion is everything. A tilt-propeller never rotates
its wing at all.**

What is astonishing about the X-19 instead is the size of its wings. **154.6 square feet carrying 13,660
pounds, a wing loading of 88.4 pounds per square foot in an aircraft required to land vertically.** The
wing alone stalls at 136.5 knots, so it cannot carry the aircraft at any speed below that.

**The keystone is the propeller normal force**, meaning the force a propeller develops at right angles to
its own axis in oblique flow. Curtiss-Wright called it the radial lift force and sized the wing around
it. Its literature is Ribner's wartime work on propellers in yaw, which is **aerodynamic stability
literature from 1943 to 1945, eighteen years older than the aircraft**. A pool imported from A315 would
not have contained a line of it, which settled the one-directory question on its own.

---

## The Wide Blade Is Demanded Twice

The best result in the article. The X-19's propellers had famously wide blades and the usual explanation
is radial lift.

The 400-knot cruise caps the helical tip Mach number, which caps the rotational tip speed at **644.2 feet
per second, or 946 revolutions per minute**. Hovering at that tip speed then requires a solidity of 0.211
and a blade chord of **17.2 inches on a 13-foot propeller**, against about 7 inches for a conventional
one. **That calculation never mentions radial lift.** The wide blade is forced by two requirements that
were going to be imposed anyway, and the radial lift force arrives with it.

Feeding the chord back through Ribner's fin analogy fixes the one free parameter, the in-plane momentum
fraction, at **0.283 from geometry rather than by assumption.**

---

## A Result That Cuts Against the Article's Own Thesis

I want to flag this rather than bury it, because it is the finding I did not expect.

The propellers do supply **29.8 percent of the lift slope in cruise**, and without the radial lift force
the X-19 would have needed about **225 square feet at 61 pounds per square foot**, an ordinary transport
wing loading. Two independent routes to that number, one ignoring drag entirely and one from the fully
trimmed corridor, **agree to 3.5 percent**.

**But the conversion corridor is continuous with the effect switched off.** Higher speeds, narrower
bands, still continuous. So the radial lift force is **not** what made the X-19 possible. It made the
wing smaller. The article says so plainly in a section titled for it, because the opposite claim was the
one the configuration was sold on.

---

## The Cure and the Cause of Death Were the Same Component

The X-18's fatal deficiency was two engines with no interconnection. The X-19 had the interconnection,
and losing both propellers on one side is an upset of **1.67 times full roll control**, so the
cross-shaft was not a refinement. **The cross-shaft is also the gearbox that destroyed the aircraft.**

Two further control findings. The tandem layout supplies for nothing the pitch control that the X-18
needed a turbojet to obtain, at 35.9 degrees per second squared. **Yaw is an order of magnitude short**
at 1.99 degrees per second squared, which is a candidate explanation for the recorded control system
problems rather than an answer, since differential nacelle tilt is not excluded.

---

## Two Defects Found by Reading, Not by Checking

**The corridor was circular and returned nonsense.** The first formulation solved the vertical
equilibrium equation for thrust and then tested the same equation, which is satisfied identically at any
speed. It reported **0.6 knots at every nacelle angle below 60 degrees**. Nothing flagged it. Eliminating
thrust between the two equations instead gives a residual that is well scaled everywhere.

**The isolated build script arrived one stub short.** The copy carried eighteen predecessors and A316
needs nineteen, so the `post_url` to A315 had no target and **the entire build failed**. That is the
interlock behaving exactly as designed, and it is the copied-script defect in its purest form. I also
found and fixed the two-clause navigation check, both clauses, per the A314 lesson.

**One model inconsistency fixed rather than carried.** A figure of merit of 0.70 and a propeller
efficiency of 0.80 were being used for what the momentum model treats as one quantity. The corridor is
now reported across both.

---

## What This Article Cannot Do

**There is no flight data from the regime the aircraft was built for.** Fifty flights, four hours, and
**no transition was ever attempted**. Comparison With Ground Prediction therefore reports the absence
rather than a comparison, and every cruise number in the article is a prediction with no X-19
measurement against it. The only confirmation belongs to the X-100, which transitioned once in 1960.

I also state where my own model stops deserving belief. The in-plane momentum picture is defensible to
about 60 degrees of disc incidence, and **five of the ten corridor rows sit outside that**, reaching 89.5
degrees at the hover end.

---

## Verification

**107 independent re-derivations, zero disagreements**, from a verifier that integrates the atmosphere by
trapezoidal rule where the model uses the analytic layer solution and uses closed forms where the model
bisects. All 102 quoted values confirmed present in the text.

79 references, 60 external URLs, zero duplicates or orphans. URL sweep at 38 plain 200s, 10 publisher
403s, and **3 DTIC DOIs verified through the Crossref registry** with matching titles. `_verify.py` at
the 0-error 21-warning corpus baseline with no new warnings. Zero style violations. Isolated build
passing with 33 of 33 display blocks rendering as display rather than inline, 2 of 2 tables, and Part 20
navigation.

---

## State

**Committed, not pushed**, which is the draft pass. **514 lines, 33 display equations, 79 references,
6,601 words.**

Twenty of seventy-two articles. The publication-order dependency is now **twenty deep** and every
cross-reference points backward.

**The fourth genre class is still the open decision and A316 does not settle it.** At 514 lines and 33
equations this is a draft-pass state rather than a final one, so it is not yet evidence either way. The
three remaining passes are yours to prompt.
