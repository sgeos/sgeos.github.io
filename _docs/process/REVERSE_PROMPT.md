# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-10
**Task**: A325, the Osprey X-28 Sea Skimmer, drafted. **Draft pass only.** Committed, not pushed.

3,695 lines, 23 display equations, 990 references, 14,380 words.

---

## The Cheapest X-Plane, and the Price Was the Requirement

The Naval Air Development Center asked for an aircraft that could patrol under visual flight rules, be
built in Southeast Asia, be trailered under a thousand pounds, work from canals as little as twenty-five
feet wide, and **cost under five thousand dollars**. **Four of those five are not flight requirements.**

**It is the exact complement of A324.** The X-27 was expensive and never built. This was nearly free and
flew for five weeks on the Delaware River. **And both were bought for the same war**, since the X-26B
was flown over the Mekong Delta made expensive so that it could be silent, while the X-28 was meant for
the same waters made cheap so that there could be many.

---

## The Keystone Is Not Aerodynamic

**The wingspan is twenty-three feet and the canal is twenty-five.** Twelve inches of clearance each side.
The span sets the aspect ratio at 5.454, the aspect ratio sets the induced drag, and the induced drag
sets the endurance, which is the patrol mission's actual product.

**The sharpest result is a collision between two requirements.** The minimum-power speed is 47.2 knots
and the stall speed is 48.0, a ratio of **0.984**, so **the endurance optimum lies below the stall and
cannot be reached**. The trailer limit pushed the stall speed down, the canal pushed the minimum-power
speed down further, and the two crossed.

**The canal cost 23.3 percent of the endurance.** The article prices it and then says the constraint was
still right, because an aircraft that cannot reach the water it patrols has no endurance at all.

**Area per dollar is the only comparison the requirement permits.** Giving each aircraft its own sweep
width, the X-28A returns 20.6 square nautical miles per hour per thousand dollars against a P-3C Orion's
0.18, **a factor of 113, after giving the Orion a twenty-mile radar against a one-mile eyeball.**

**The water was never the problem.** Static thrust exceeds the resistance hump by between 2.75 and 4.59
across every hull the record permits. The real limit is sea state.

---

## Two of My Own Errors, Caught Before Writing

**A sweep-width function had the inequality backwards**, returning more than twice the sighting range and
inflating every coverage figure that used it. Sweep width is the integral of the lateral-range curve and
can never exceed twice the definite range.

**An area-per-dollar comparison gave all three aircraft the same sweep width**, which flattered the
Osprey badly. The conclusion survives a fair comparison. The first version did not deserve to.

**And the climb claim has no room in it.** 2,200 feet per minute is 88.9 percent of the zero-drag ceiling
and needs a propeller efficiency of 0.823. Inverting for drag instead returns 0.0050, a quarter of a
clean sailplane's, so the premise is wrong rather than the arithmetic.

---

## The Designation Finding Is Now Four Deep

X-25, X-26, X-27 and X-28 are **four consecutive designations that did not go to a purpose-built research
aeroplane**, and the X-28A is the clearest case. The Navy did not commission anything. It watched a man
demonstrate his own aeroplane, recognised its own requirements document, and wrote him a cheque.

---

## Verification

**39 independent checks passing, none importing the calculation**, with the minimum-power speed found by
scanning, the endurance by fuel-burn simulation, the static thrust by closing the momentum balance, and
the span ordering as a randomised property.

Reference integrity 990 with zero undefined, zero orphaned and zero duplicate URLs. **Zero
search-endpoint citations.** All 29 hand-curated URLs resolve, 50 of 50 sampled NTRS resolve, 60 of 60
sampled Crossref and 40 of 40 sampled DTIC are registered. `_verify.py` at the 21-warning baseline,
check_any clean, and a 29-article isolated build with all 23 equations rendering.

---

## Awaiting Instruction

**A325 has completed the first of four passes.** The expected next prompt is the equation-density review.

**One thing to weigh before it.** The article carries 23 equations against a series median of 94, which
is the lowest count in the series. That may be a narrow subject or an equation pass waiting to happen,
and I have not pre-judged it.
