# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A314 equation-density review, the second of four passes. Committed, **not pushed**, not
published. Display equations rose from **27 to 47**.

---

## The Pass Found a Ceiling on the Whole Technique

This is the strongest result and it sharpens the article's thesis rather than extending it.

The draft compared the X-17 against an **assumed** reference of 7,000 metres per second at 35
kilometres. The Allen-Eggers closed-form ballistic entry solution lets that be **derived** instead, and
doing so shows two things the draft did not know it had committed to.

**The assumed reference corresponds to a ballistic coefficient of 1,453 kilogrammes per square metre**,
which is a blunt, light body. That is exactly the class of re-entry vehicle the X-17 was built to test.
The draft made that choice without noticing it.

**And the X-17 cannot exceed the heating it produces at its lowest altitude** — 3,241 W/cm² at sea
level, 1,881 at a practical 10 km floor. So:

| Ballistic coefficient, kg/m² | Reference peak, W/cm² | Altitude X-17 needs |
|---|---|---|
| 1,453 | 1,398 | 13.97 km |
| 2,000 | 1,674 | 11.68 km |
| 4,195 | 2,563 | 4.63 km |
| 8,000 | 3,705 | **impossible** |

**Above roughly 2,500 kg/m² at a practical floor, no altitude exists at which the X-17 matches the
heating rate at all.** The heating-rate match is therefore **not a general capability of the vehicle**.
It is conditional on the class of body being simulated, it works for the blunt first-generation
re-entry vehicle, and it would have failed outright for a dense slender one. When re-entry vehicles
later became slender and dense, the technique stopped applying.

---

## Three Further Results

**The vehicle reproduces a point, not a trajectory.** Peak deceleration is Ve² sin γ / (2eH), which
contains **no ballistic coefficient at all**, so every ballistic entry at a given speed and angle pulls
the same 43.7 g. The velocity at peak heating is Ve·e^(−1/6) = 5,925 m/s, also independent of β. **What
β controls is the altitude**, from 31.3 km down to 12.3 across the range — which is the blunt-body
argument stated quantitatively as nineteen kilometres and a factor of twenty in density.

**Ablation is mandatory, not convenient, and one line proves it.** The draft asserted that no passive
material survives. Stefan-Boltzmann gives the temperature a passive surface must reach to reject the
matched flux as **4,127 K**, which exceeds tungsten's melting point at 3,695 and graphite's sublimation
at 3,900. Only hafnium carbide beats it, by 73 kelvin, and it was not a 1956 structural material.

**Radiation is a fourth thing the vehicle could not reproduce, and the draft had it in Out of Scope.**
Shock-layer radiation scales as roughly V^8.5, so the X-17 sees **one part in 110.7** of an
intercontinental re-entry's radiative environment. Unlike the other three failures this one follows from
velocity alone and is unfixable by any choice of altitude. The central partition table gained two rows.

---

## Two Contradictions the Pass Created, and Fixed

Out of Scope still said radiative heating was left aside **after the pass had brought it in**. And Where
the Framing Breaks Down described the reference condition as merely generic when the pass had just
quantified exactly how much weight it carries. Both were corrected rather than left.

---

## What Else Was Added

The rocket equation, giving 63.8 percent propellant in the descending stack at a period solid impulse.
The Damköhler number restating binary scaling as a rate ratio of 16.09, consistent with the 9.25 binary
figure times the velocity ratio. The perfect-gas strong-shock density ceiling of 6 and its standoff
consequence, so **the shock is a different shape in the gas the X-17 did not produce**. The ablation
energy balance with recession of 2.50 mm over the pulse against 10.39 over a re-entry. Thermal
penetration depth, showing the pulse heats **half the depth**, so a material can pass on surface
behaviour and fail on what happens behind it. And the laminar-to-turbulent Stanton scaling, giving a
2.70 penalty at the quoted Reynolds number.

---

## Verification

**56 draft-pass re-derivations still reproducing, plus 44 new ones, zero disagreements.** All
independent of the calculation modules, with the Allen-Eggers peak located on a 5 metre grid against
calc2's 20 metre one so that neither validates the other.

`_verify.py` at the 0-error 21-warning corpus baseline. Zero style violations. Isolated build passing
with 47 of 47 display blocks rendered, 7 of 7 tables, and Part 18 navigation. Equation count measured
before and after, per the A310 lesson.

A section scan flagged eleven sections carrying numbers without equations; **nine remain and all nine
are legitimately narrative**.

---

## State

**607 lines, 47 display equations, 71 references, 6,937 body words.**

**Committed, not pushed.** Nothing in the series is published.

References at 71 are the measure furthest from any band and the reference pass will move that. Lines and
equations remain between the documentation-poor and full-aircraft classes, which is the third
consecutive pass on which **the fourth-class question in `RESEARCH_AIRCRAFT_STRUCTURE.md` has come up**.
It remains yours to settle, as do the categories.
