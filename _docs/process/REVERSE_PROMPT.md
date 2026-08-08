# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A313 equation-density review, the second of four passes. Committed, **not pushed**, not
published. Display equations rose from **20 to 72**.

---

## The Pass Corrected the Article's Physics, Not Only Its Density

This is the important part and it is a **directional** error rather than a numerical one.

The draft's headline result is that three aeroplanes designed against one requirement all need a
turbojet to beat proportionality in thin air, at a solved lapse exponent near 0.9378. The draft
attributed that to **compressor Reynolds number degradation**.

**That attribution is backwards.** Degradation makes a compressor perform *worse* in thin air, which
pushes the exponent *above* one. It cannot be what allows thrust to beat proportionality.

The mechanism that does is **ram recovery**. Sea level static thrust is quoted at Mach zero, so the
inlet sees ambient static pressure. At altitude the aeroplane must fly faster to hold its lift
coefficient, and at the design condition it is doing Mach 0.685, so the inlet sees

$$p_t/p = (1 + 0.2 \times 0.685^2)^{3.5} = 1.3685$$

which gives an effective exponent of **0.8889**.

**Ram alone over-explains the observed 0.9378.** The realised benefit is 56.0 percent of ideal, so
**44 percent is consumed by losses elsewhere in the engine** — and *that* is where Reynolds
degradation belongs. Blade Reynolds number falls 11.58 times, from 6.16 × 10⁵ to 5.32 × 10⁴, which is
below the roughly 2 × 10⁵ threshold where stage efficiency degrades measurably.

**The two mechanisms act in opposite directions and the observed exponent is what survives their
difference.** The draft said none of that. The correction is stated in the text rather than silently
applied, and the forward reference and the Epistemic State entry were both repointed.

**Tenth consecutive article in which writing a relation down caught a claim carried as an assertion.**

---

## A Second Result Reconciles an Apparent Contradiction

The draft concluded thrust binds and the corner never does. That sits awkwardly beside the U-2's
reputation for having only a few knots between stall and buffet, and a reader would be right to notice.

**Both are true, and the difference is which airspeed is quoted.** A pilot's instrument reads close to
equivalent airspeed, which is true airspeed scaled by the square root of the density ratio.

| Altitude, ft | Band, kt TAS | Band, kt EAS |
|---|---|---|
| 40,000 | 276.4 | 137.1 |
| 62,000 | 169.2 | 49.5 |
| 69,500 | 118.1 | 28.8 |
| 71,832 | 100.3 | 23.1 |

**The instrument band closes 2.15 times faster than the physical one.** So the corner does not set the
ceiling, and it entirely sets the difficulty of flying the cruise. The folk account and the arithmetic
are both right, about different things.

---

## An Assertion Became a Computation

The draft said ambient pressure falls below the vapour pressure of water at body temperature "above
roughly sixty-three thousand feet" and showed no relation for it. The Antoine equation gives 46.95
millimetres of mercury at 37 degrees Celsius, and the atmosphere puts that at **62,829 feet**, which is
**90.4 percent of the design altitude**. The aeroplane therefore cruises entirely above the Armstrong
limit. The assertion was right and is now backed.

---

## Two Defects in My Own Additions

**The narrowing claim was wrong on first writing.** I said the instrument band narrows "almost six
times faster" than the physical one. That conflated the equivalent-airspeed band's own narrowing factor
of 5.935 with its rate *relative* to true airspeed, which is 2.15. Corrected.

**The diffraction figure used the wrong aperture.** It computed with 0.30 metres while calling it twelve
inches, which is 0.3048. The correct value is 2.201 microradians rather than 2.237. Corrected.

Both were caught by the independent re-derivation rather than by reading.

---

## What Else Was Added

The relations the prose already relied on but did not show. The lift and drag equations. The derivative
condition defining the polar optimum, and with it the proof that **minimum drag is altitude-independent
by cancellation** rather than by assertion. Specific excess power with the ceiling as its zero. The
closed form for corner density, which shows it is **linear in wing loading exactly as the thrust ceiling
is**, which is why the two move together. The gust derivation showing one power of speed cancelling. The
aspect-ratio benefit as the square root of two. Breguet from the fuel-flow differential. The
single-engine counterfactual as a ratio of weight to thrust.

---

## Coverage and Verification

A section scan flagged **ten** sections carrying numbers with no equation. **Six remain**, and all six
are legitimately narrative — the opening, two historical-context sections, the flight record, the Source
Base, and the Epistemic State, where relations belong at the point of derivation rather than at
recapitulation.

**83 original re-derivations still reproducing, plus 74 new ones**, zero disagreements. All independent
of the calculation modules, using a trapezoidal integration of the hydrostatic equation so that a
mistake cannot validate itself.

`_verify.py` at the 0-error 21-warning corpus baseline. Zero style violations. Isolated build passing
with **72 of 72 display blocks rendered**, 9 of 9 tables, and Part 17 navigation. Equation count was
measured before and after every batch, per the A310 lesson.

---

## State

**758 lines, 72 display equations, 85 references, 8,731 body words.**

**Committed, not pushed.** Nothing in the series is published.

**The class question from the draft pass stands and has narrowed.** Equations at 72 are 18 below the
full-aircraft floor of 90 and far above the documentation-poor ceiling of 15. References at 85 are the
measure still furthest from any band, and the reference pass will move that. I have not invented a
fourth class in `RESEARCH_AIRCRAFT_STRUCTURE.md` and will not without your instruction.

Categories remain undecided at `aerospace history engineering`, seventeen articles deep.
