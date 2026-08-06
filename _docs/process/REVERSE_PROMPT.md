# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-05
**Task**: A302 equation-density review. Committed and **not pushed**. **No article in this series is
published.**

**66 to 112 display equations, 1143 to 1345 lines.** All three densities are now inside band.

---

## Three Results the Draft Did Not Have

**The aircraft could not have reached its top speed unswept.** Adding the Korn drag-divergence
relation and evaluating it with the streamwise thickness ratios that sweeping itself produces gives
0.765 at 20 degrees of sweep and 0.916 at 40, against a maximum flight Mach number near 0.9. The
X-5 was flying above the drag-rise Mach number of its own unswept setting. **Sweeping was not a
refinement of the performance. It was the performance.** The draft had the mechanism and the trim
consequence but never established that the aircraft needed the mechanism to meet its own numbers.

**One geometric fact produces a performance cost and a safety cost of exactly the same size.**
Induced drag carries the span squared in a denominator through the aspect ratio, and so does the
NACA spin-recovery inertia parameter. Sweeping this wing therefore degrades both by the identical
factor of 2.61. The article had the spin figure already. It did not have the observation that the
drag penalty is numerically the same number for the same reason.

**The gull result now has a number attached.** Giving sweep a control derivative in the same form as
an elevator's returns minus 0.26 per radian at mid sweep against a conventional elevator near minus
0.7, so **sweep is worth roughly a third of an elevator as a pitch effector**. The obstacle to using
it that way is entirely rate. Matching a five degree elevator input inside one short-period time
constant would demand 42 degrees per second against the X-5's 1.33, **a factor of thirty-one**. That
converts the closing rhetorical point into an engineering statement, and it says the gap between the
X-5 and the bird is a rate gap rather than an authority gap, which is a more tractable thing to be
short of.

---

## Where the Equations Went

The two sections that carried none were the ones A301 carries seven and six in, so the pass was
concentrated there and on the claims elsewhere that named a result without showing the relation.
Notable additions include the velocity decomposition normal and spanwise to the leading edge, the
streamwise thickness ratio that a pivoting wing thins as it sweeps, the tapered-panel mean
aerodynamic chord station **with a sensitivity statement on the one assumed quantity in the whole
chain**, the centre-of-gravity range taken as an intersection over the sweep schedule which comes out
empty uncompensated, the pivot-station minimization, a formal quasi-static criterion that evaluates
to 0.81 and is therefore below unity but not comfortably, pivot bearing and pin-shear stresses with a
relation converting bearing clearance into sweep asymmetry, the trim tail load at 4.9 percent of
gross weight, the short-period frequency spread of 1.45 that survives even perfect trim
compensation, the spin recovery criterion and altitude per turn, the calibration matrix condition
number, and the time-varying inertia tensor term that exists only while a morphing wing is actually
moving.

---

## Two Errors in My Own Additions

Independent re-derivation caught both, which is the reason for doing it.

A spanwise velocity component was stated as **0.78 of the free stream**. That is the Mach number, not
the fraction. The fraction is 0.87. Corrected to read as a Mach number.

A sweep-angle error propagation was quoted as **1.3 percent**, which holds only at the low-sweep end.
Across the sweep range it runs to 2.7 percent. Corrected to give the range and say what it depends on.

---

## Verification

318 references with zero undefined and zero orphaned. `_verify.py` at the 0-error 21-warning corpus
baseline. Zero contractions, em-dashes, en-dashes, prose colons, prose semicolons, or prose
parentheticals. Zero doubled words, zero display-math seam defects, zero consecutive-display runs.
No repeated six-word shingle attributable to a duplicated clause, which is the A297 signature.
Isolated build succeeding with **112 rendered display blocks matching 112 source equations** and Part
6 navigation.

---

## What Remains

**Contemporary references are 22.1 percent of dated, below the target range, and I have not padded
them.** That is the primary-reference and publication-review business. The primary base is already
strong at 94 NTRS documents and 33.7 percent of dated references at 1960 or earlier, so A302 does not
have the deficit A301 had.

Word frequency shows `sweep` at 11.73 per thousand body words, which is the article's subject and
unavoidable, `wing` at 8.64, and `aircraft` at 8.23. The last is now inside the sibling range without
any rotation having been applied, which A301 needed.

**Publication order dependency is six deep.** One commit unpushed.

---

## Categories

Still `aerospace history engineering`, still my assumption, now six articles deep. One line of front
matter, reversible with a single edit until the batch publishes.
