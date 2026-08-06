# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-06
**Task**: A307, the North American X-10, drafted, verified, and committed. **Not pushed**, per the
rhythm. Three review passes remain.

---

## The Keystone Is Time, Which Is New for This Series

Every previous vehicle answered a question that could be asked in minutes. The Navaho mission is
**2.87 hours**, and the error that decides whether a self-contained navigator works grows with elapsed
time rather than with distance, speed, or geometry.

Inverting the reported 800 metre accuracy requirement gives a gyroscope drift specification of
**0.0025 degrees per hour**. Inverting the reported achieved drift of 1.6 kilometres per hour gives
**0.0144**. The shortfall of **5.74** reproduces independently by propagating the achieved drift to
full range, which is a consistency check rather than a second measurement, and the article says so.

---

## The Central Result

Schuler tuning makes accelerometer error **bounded** at 1274 metres and gyroscope error **secular**.
The two are equal at **47.8 minutes**. The X-10's supersonic leg is **27.6 minutes**, so the vehicle
built to prove a gyroscope specification flew where gyroscopes were not the dominant error.

Being the smaller term is a nuisance. Being an inseparable term is fatal, and that is the actual
situation. The two error signatures are **97.4 percent correlated** over an X-10 leg, a variance
inflation of **19.7**, against **exact orthogonality over one Schuler period**, which the article
proves by direct integration. A window sweep puts the optimum at **exactly 84.4 minutes**.

**The corollary inverts ordinary testing intuition.** Flying the same thousand kilometres subsonically
takes 62.8 minutes, crosses the threshold, and is more than ten times more informative about the drift
rate. Speed was the enemy of the measurement.

---

## Results the Sources Do Not State

- The reported ranges **cannot be reconciled with the reported weights** under any cruise condition.
  The mass ratio of 1.640 is data rather than assumption and yields 275 kilometres at maximum Mach,
  while the reported figures demand subsonic lift-to-drag ratios of 12.6 to 28.4 against a realistic
  ceiling near 7 for aspect ratio 1.87.
- The **radio horizon is 482 kilometres**, less than half the navigation leg.
- The **aluminium recovery-temperature frontier is Mach 2.27** and the demonstrated maximum was 2.05.
- The **vertical channel is unstable**, doubling every 6.6 minutes, 18.1 e-foldings over a mission.
- **Deflection of the vertical alone consumes 77 percent** of the accuracy requirement, and it is the
  one term no instrument improvement addresses.
- The **break-even inlet recovery to sustain Mach 2.05 is 0.622**, which resolves the free-flight
  duct anomaly as a model-scale artefact using the vehicle's own demonstrated speed as evidence.

**The error budget does not close.** The quadrature sum exceeds the reported stellar-inertial accuracy
by a factor of 3.3, and the deflection term alone exceeds it. Three readings are offered and none
adopted. The one I find most likely, and least often stated, is that the demonstration was flown down
a surveyed range rather than over the target country.

---

## The Source Base, Which Produced a Controlled Negative

**The vehicle is indexed under its project number.** Queries on X-10 and Navaho return nothing usable.
`MX-770` returns the two primary aerodynamic documents immediately. This extends the archive rule from
choosing the right archive to choosing the right name within one.

**The DTIC route that worked for the X-9 fails here, and fails cleanly.** `MX-776` returns the RASCAL
weapon system report. The identical query form on `MX-770` returns nothing about the Navaho at all.
Same archive, same route, same query shape, adjacent project numbers, opposite results. **The negative
result is therefore about the record and not about the method**, which is a stronger statement than
this series has previously been able to make about a source gap.

Three documents in the accessible record concern the actual hardware. The article is possible because
the topical record is enormous even though the vehicle-specific record is three items.

---

## Verification

**All 102 worked values re-derived independently with no corrections required.** That is the second
article running to pass first numeric verification clean, and the only procedural difference remains
that the numbers were computed in a scratch script before the prose was written.

213 references with zero undefined, zero orphaned, and zero duplicate URLs. **All 132 DOIs
Crossref-resolved on title at the 0.85 threshold with zero flagged, and there are no hand-entered
identifiers anywhere.** 56 of 66 fixed identifiers at 200, the ten failures being the unpublished
series back-references, which is expected and correct. `_verify.py` at the 0-error 21-warning corpus
baseline. Zero contractions, em-dashes, en-dashes, prose colons, prose semicolons, or prose
parentheticals. Zero doubled words, zero display-math seam defects, zero duplicate headings, zero link
texts out of sync. Isolated build succeeding with 84 rendered display blocks, Part 11 navigation, and
all ten back-references resolving.

---

## Two Things I Got Wrong and Corrected

**A factual claim, caught by checking rather than by any tool.** The draft said the X-10 was the second
of three articles whose designation came from an administrative reorganisation. A305 and A306 record
the X-8 as RTV-A-1 and the X-9 as RTV-A-4, and the X-10 was RTV-A-5. All three. The corrected claim is
stronger and now carries the aircraft-category section, because three exceptions with one common origin
are a pattern where three with separate origins would not be.

**Three anchors invented during composition**, all caught by the reference generator before any pass
ran. The ordering rule of resolving the index from metadata first is working, but invention at
composition time is a separate and still-live defect class, and I am recording it rather than treating
the catch as a clean result.

---

## Final State

**943 lines, 84 display equations, 213 references, 14,346 words.**

All three densities are under band, at 943 against a 1300 floor, 84 against 90, and 213 against 250.
This is deliberate and is the A306 approach, but it is further below than A306's draft was, which
finished at 1228, 88, and 239. The three remaining passes have more to close here than they did there.
Nothing was padded to narrow the gap and the shortfall is reported rather than disguised.

---

## State

**Committed, not pushed.** The rhythm pushes on the publication review. **The publication-order
dependency is now eleven deep**, A307 back to A297, all through `post_url`.

Eleven articles complete of seventy-two. **Categories remain undecided** at `aerospace history
engineering`, eleven articles deep and now raised ten times. It fixes 72 URLs permanently at
publication and stays reversible with one edit until the first article publishes.

**A305 is still 40 percent over the line ceiling** and the cut I offered has not been taken up. The
offer stands and I will not act on it unprompted.
