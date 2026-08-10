# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-10
**Task**: A326 draft pass, the first of four. Committed, **not pushed**, per the rhythm.

**State: 7,784 lines, 29 display equations, 2,208 reference definitions, 44,545 words.** Thirty
articles drafted, all in `_drafts/`, **none published**.

---

## The Run of Four Ends, and the Method Reverses With It

**The X-29 is the first purpose-built research aeroplane in this series since the X-24.** The four
before it were an off-the-shelf autogyro, an off-the-shelf sailplane, a fighter never built, and a
five-thousand-dollar homebuilt flying boat.

**That changes how the article had to be researched.** A324 and A325 both returned nothing from the
Technical Reports Server under the vehicle's own name and had to harvest the physics instead. This
subject returns a great deal, and **378 of the cited references are recalled by fixed document
identifier**, including the two primary reports that carry most of the article's numbers.

---

## The Keystone

**Two published figures connect through a relation neither was derived from.** The primary record gives
the wing's predicted elastic-to-rigid lift-curve-slope ratio as about 1.6, and separately gives the
design dynamic pressure as 1,700 pounds per square foot. The single-degree-of-freedom divergence model
makes that ratio exactly one over one minus the pressure ratio, so the two together fix **a divergence
dynamic pressure of 4,533 pounds per square foot that nobody published**, with no assumption about the
wing's stiffness, geometry or material.

**The margin is 2.667 in dynamic pressure and only 1.633 in equivalent airspeed**, and the second is
the number a pilot experiences.

**The design point checks against itself.** It is quoted twice, as a pressure and as a Mach number at
an altitude, and recomputing one from the other agrees to 0.24 percent.

---

## Defects Found by Writing the Relation Down

**One of them printed free energy.** The two-mode divergence eigenvalue has an identically zero
quadratic coefficient, so the characteristic equation is linear. Trusting floating point to notice sent
the solver down the quadratic branch, which **returned 5.7 times ten to the twenty-first pounds per
square foot**. An absolute tolerance cannot catch a residue that is sixteen orders below the terms that
produced it and still enormous, so the test had to be made relative to the magnitude of what cancelled.

**The bend-twist coupling sign was backwards**, reporting that tailoring lowered the divergence
boundary, which is the reverse of the point of the technology.

**The trim analysis conflated the surface's own lift coefficient with the wing-referenced increment**,
inflating the trim load by a factor of five and driving the drag comparison above nine hundred.

**The transonic comparison was made at equal leading-edge sweep when the source's claim is at equal
shock sweep**, and those two questions give opposite answers.

---

## What the Analysis Established

**The model reproduces a result it was not fitted to.** Sweepback beyond about 47 degrees removes the
divergence boundary entirely, which is the classical result, recovered from an independent determinant
scan.

**The required tailoring survives its own assumptions.** Reaching the observed margin needs a
non-dimensional coupling of 0.627 against a hard bound of 1.0, and that stays between 0.61 and 0.79
across a factor of more than five in the assumed stiffness ratio.

**The Southwell method was applied to flight data for the first time on this aircraft.** The report
calls the estimate highly sensitive without saying how sensitive. It is about 1.4 times the twist
measurement error at the aircraft's own reach.

**A control-law requirement fixed a structural boundary.** The canard's divergence boundary was set by
the pitch-loop stiffness required for control stability, which is the article's argument for treating
structure and control as one system.

**Instability measured in frames rather than probability.** About 100 milliseconds to double at Mach 0.9
at sea level, four frames at 40 hertz, of which sampling consumes 37.5. Isolating a failed channel in
three frames spends 75 percent of a doubling time.

---

## Verification

**42 of 42 independent checks passing**, the verifier reaching every value by a different route than
the calculation, namely bisection, a determinant scan, a non-linear fit, Runge-Kutta integration and
enumeration. **One of the article's own literals was wrong and the verifier caught it.**

`_verify.py` at the 21-warning baseline, check_any clean, zero constructions above the corpus maximum
after rotating four across four distinct phrasings, and a 30-article isolated build rendering all 29
equations across 17 sections with 97 internal series links resolving.

**The citation sweep was still running when this was written and its result is not yet recorded.**

---

## Awaiting Instruction

**A326 has completed the draft pass only.** The equation, primary-reference and publication passes
remain, each on its own prompt.

**29 display equations is low against a corpus median of 94**, and the audit already names sixteen
sections that state numbers with no displayed relation behind them. The equation pass has plenty to
work with.
