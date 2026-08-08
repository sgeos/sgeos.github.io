# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A315 drafted, the Hiller X-18. The first of four passes. Committed, **not pushed**, not
published. All nineteen articles in the series remain in `_drafts/`.

---

## The Keystone Is Slipstream Immersion, and It Is Geometric

A tilt-wing points its wing at the sky, which means pointing it away from the oncoming air. A wing at
ninety degrees to the flow is stalled. **The configuration works only where the propeller slipstream
keeps the flow attached**, and the immersed fraction is set by propeller diameter against span, which is
frozen when the aircraft is drawn.

Two sixteen-foot propellers on a 47.92-foot span give:

| Station | Immersed span |
|---|---|
| At the disc | 66.8 percent |
| Just behind, representative | 56.8 percent |
| Fully contracted | 47.2 percent |

**About 43 percent of the span is never immersed.** At a 15-degree stall angle the outer panel is
stalled for **83.3 percent of the conversion**. That is geometric rather than aerodynamic, and no
section design removes it, because the wing is pointed away from the air by construction.

**What the slipstream buys is genuinely large.** At an 82.1 lb/ft² disc loading the part-developed
slipstream dynamic pressure corresponds to an equivalent airspeed of **117 knots while the aircraft is
standing still**. The immersed wing never stops flying. The un-immersed wing never starts.

---

## The Engine-Out Claim Was Checked and Is Arithmetic, Not Caution

Sources say the turboprops were not cross-linked and that losing one meant losing the aircraft. That is
a checkable statement. Losing one propeller in hover gives a **268 kN m rolling moment**, and:

| Freestream | Aileron authority |
|---|---|
| 0 m/s | 0.00 percent |
| 10 m/s | 0.46 percent |
| 30 m/s | 4.12 percent |

**Cross-shafting is not a refinement. It is the only fix**, and its absence is the aircraft's defining
deficiency.

The final flight follows from the same relation. **A few percent of thrust asymmetry exhausts the roll
control during conversion** — 3.04 percent at 30 m/s at ten thousand feet. A propeller pitch control
failure is not a small disturbance, so the departure was the expected outcome rather than bad luck.

**And there is a bitter detail.** Converting at ten thousand feet rather than near the ground cost about
**26 percent of the available roll authority**, because authority scales with density. The altitude was
chosen for safety, to give room to recover. It made the departure more likely and the outcome more
survivable, and the programme got the survivable half.

---

## A Strong Internal Validation

Momentum theory gives **7,883 ideal shaft horsepower** for hover against an installed 11,700, implying a
figure of merit of **0.674**. That is an entirely ordinary propeller value, and it is the best available
check that the published weight, propeller diameter and engine power describe one consistent aircraft.

---

## Series Threads

**The tail turbojet fitted purely for pitch makes this the third vertical take-off aircraft in the
series to carry a separate thrust-based control system**, after the X-13 and X-14, for the same reason
each time: aerodynamic control scales with dynamic pressure and vanishes, while thrust does not. The
crossover here is 58.6 knots.

**The one-directory question was live and was decided explicitly.** The X-18 shares the VTOL control
problem with the X-13 and X-14 and shares nothing else, since a tilt-wing lifts with a wing in a
slipstream rather than a deflected jet. Rather than import a pool built for a different aircraft, the
harvest **asked the shared questions directly**. That obtains the common literature without the A309
defect, and costs a few duplicate queries.

**Both harvest-design lessons were applied from the start** rather than as later corrections — the
middle era present per A313, and a 1960 cutoff on the early sweep per A314.

---

## An Error Caught by Reading Output, Not by a Check

An elevator effectiveness of 0.02 per radian produced a pitch-jet crossover of **454 knots**, which is
absurd for an aircraft of this class. The correct order is about 1.2 per radian, giving 58.6 knots.
**No automated check would have caught it** — the arithmetic was correct and the coefficient was wrong.
It is recorded in the Epistemic State.

---

## Verification

**62 independent re-derivations, zero disagreements** after one rounding correction, using a trapezoidal
atmosphere so the calculation module cannot validate itself.

66 reference definitions, 48 external URLs, zero duplicates or orphans. 27 plain 200s, 7 publisher 403s,
14 DTIC DOIs registry-verified. **A 404 was found and fixed**, since the XC-142 encyclopaedia title was
wrong. A read of all 36 cited titles found no off-topic citation.

`_verify.py` at the 0-error 21-warning corpus baseline. Zero style violations. Isolated build passing
with 21 of 21 display blocks rendered, 4 of 4 tables, and Part 19 navigation — with **both** navigation
clauses repointed, after the A314 copy left one at the previous part number.

---

## State

**386 lines, 21 display equations, 66 references, 3,982 body words.**

This is a shorter draft than A313 or A314 produced, and the reason is favourable rather than not.
**Unlike those two, this subject's configuration has a real primary literature** even though the
individual airframe does not, which is the inverse of their situation. The pool is rich and the
reference pass has a great deal to work with.

**Committed, not pushed**, per the series rhythm for a draft pass.

Nineteen articles complete of seventy-two. **The publication-order dependency is nineteen deep.**
Categories remain undecided, and the fourth-class question in `RESEARCH_AIRCRAFT_STRUCTURE.md` is open
across two completed articles.

A316 is the next entry on the roster; check `HANDOFF.md` before starting.
