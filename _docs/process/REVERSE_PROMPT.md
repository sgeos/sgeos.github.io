## Last Updated

**Date**: 2026-09-05
**Task**: **A350, X-Planes: Boeing X-53 Active Aeroelastic Wing, equation-density review. The second of
four.** Committed, **not pushed**, since only the publication review pushes. **Not published**, and
publication of the series still not authorised. **Fifty-four of seventy-two drafted.**

---

## The Largest Finding Came Out of a Table the Draft Had Only Tabulated

**The flight test report gives actuator force, horn arm and structural limit in adjacent columns.**
Force times arm is a moment in the same units as the limit printed beside it, and the draft reproduced
all three columns without ever multiplying the first two.

**Multiplying them is alarming.** The aileron actuator delivers 52,400
inch-pounds against a structural limit of 50,000, which it exceeds by 4.8 percent.
**The trailing-edge flap exceeds its own limit by 4.4 percent and the inboard
leading-edge flap's rotary actuator exceeds its negative limit by 38.7 percent.**

**Three of the four wing surfaces carry actuators strong enough to break their own structural limits**,
and only the outboard leading-edge flap cannot.

**That explains the entire flight-test caution regime**, which the draft had reported as a list of
procedures without a reason. The build-up through 25, 50, 75 and 100 percent lateral stick. The
real-time envelope display. The aural disengage tone. The test conductor authorised to terminate a
manoeuvre before the pilot reached a boundary. **The structure was protected by procedure and not by
the actuator**, and the report's remark that the aileron hinge moment dominated the flight test stops
being a complaint and becomes an arithmetic consequence.

---

## The Motivation Is Now a Derivation

**The draft asserted that torsional stiffness is weight and left it there.** Bredt-Batho gives the
torsional rigidity of a thin-walled box as linear in skin thickness, the skin mass per unit span is
linear in the same thickness, so eliminating it leaves stiffness proportional to mass.

**And the reversal dynamic pressure is proportional to stiffness**, so reversal margin is bought
linearly in structural mass, at the corner of the envelope and carried everywhere else in it. **That is
the whole motivation for the programme in one chain.**

---

## Dividing the Two Classical Limits Makes the Stiffness Cancel

**The ratio of reversal to divergence dynamic pressure depends only on the flap's lift and pitching
moment and on where the elastic axis sits.** $K_\theta$ is gone from it entirely.

**So stiffening a wing moves both limits together and changes neither's order.** A designer can push
reversal further out in absolute terms and cannot push it past divergence by that means, which is why
reversal is the limit that gets designed against and divergence is the one that gets checked.

---

## The Time-to-Bank Criteria Were Testing Roll Rate and Not Roll Damping

**With measured roll-mode time constants of order a tenth of a second and criteria written at 50, 90
and 180 degrees of bank, the exponential term in the first-order bank response is negligible** and time
to bank is very nearly angle over rate.

**The slowest measured constant beat its level 1 goal by two thirds again**, and **two of the three fell
below the fast guideline the programme wrote for itself** out of concern about roll-ratchet
pilot-induced oscillation. **A criterion written to catch an aeroplane that rolls too slowly had to be
given a second end**, because this one rolled too readily.

---

## Three Insertion Bugs, All the Same Shape, All Caught

**Each was an addition appended to a line that was already a complete paragraph.** The result was a
full stop followed by a comma, and twice an equation placed before the sentence it depends on.

**A regex for that signature now runs over the assembled article** and reports zero, alongside a check
for lowercase words following a full stop in author prose.

**An inlined relation was also caught, and by the article's own checker rather than by reading.** The
skin mass per unit span had been written inline while the rigidity beside it was displayed, and the
inline-math check that A349 built flagged it.

---

## Verification State

- `python3 _verify.py` reports **0 errors, 0 warnings** across 301 posts.
- `python3 _lib/test_lib.py` reports **104 of 104**.
- `tmp/a350/verify_numbers.py` reports **ALL CHECKS PASS**. **Every actuator figure is recomputed inside
  the checker from the force and the arm** rather than compared against `eqns.json`, so a wrong value in
  the generator cannot validate itself, and the dynamic pressures are recomputed from the atmosphere the
  same way.
- Reference integrity: **3,372 defined, 3,372 used, 0 undefined, 0
  orphaned, 0 duplicate URLs**.
- Prose: no contractions, no dashes, no prose colons outside citation labels, **no inline span carrying
  a relation or a pipe**.
- **7,299 lines, 42,861 words, 27 display equations, 3,372 reference definitions.**
- **The build succeeded in 65 seconds with no Liquid error**, against a checksum taken before it and
  re-verified after. **The rendered audit reports no findings across 89 pages.** **Source 27 display
  equations against 27 real rendered display blocks**, three line-spacing directives accounting for the
  difference in the raw count, zero raw dollar pairs, zero unresolved reference brackets, page 633,451
  bytes.

---

## One Process Note Carried Forward

**Do not wait on `pgrep -f "jekyll build"`.** A shell running that loop has the string in its own
command line, so the loop matches itself and never terminates. Three of them accumulated during the
draft pass while the build had long since finished. **Wait on the build log for `done in` instead**,
which is what this pass did and which worked.

---

## Next

**A350 has two passes remaining**, the primary-reference review and the publication review.

**Report primaries stand at 247 of 3,296, or 7.5 percent**, which
is healthy for this series and needs no rescuing. **The primary pass should look instead at whether the
argument leans anywhere on the survey rather than on a document**, and at the classical literature,
since the reversal charts and the flexible-wing lateral control methods are cited once each and carry
more of the sizing section than that suggests.
