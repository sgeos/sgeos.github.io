## Last Updated

**Date**: 2026-09-04
**Task**: **A350, X-Planes: Boeing X-53 Active Aeroelastic Wing, draft pass. The first of four.**
Committed, **not pushed**, since only the publication review pushes. **Not published**, and publication
of the series still not authorised. **Fifty-four of seventy-two drafted.**

---

## The Aeroplane Never Reached the Condition It Was Named For

**The X-53 is a production F/A-18 with its wing stiffening deliberately removed.** Boeing's Phantom
Works built covers that returned the wing to its preproduction torsional stiffness, undoing the two
roll modifications the contractor had added when full-scale development flight tests showed degraded
transonic and supersonic roll performance.

**Aileron reversal is the keystone.** A trailing-edge surface twists a flexible wing against itself,
its rolling moment falls with dynamic pressure, and at reversal it changes sign. **The classical answer
is torsional stiffness and torsional stiffness is weight**, and the design charts for choosing it were
published before the war ended. **A leading-edge surface twists the wing the other way**, so the
flexibility that destroys one amplifies the other.

**Two of the programme's four host requirements did not survive.** The external stores provision was
deleted outright. **The requirement to fly beyond trailing-edge control reversal was deleted after
early flight tests showed it could not be met.**

**No reversal was observed.** The aileron rolling moment approached zero and stayed there without
changing sign, and the report's own hypothesis is that the surfaces were themselves flexible enough to
relieve the hinge moment they were applying to the wing.

**And the two test points at the highest dynamic pressures were never flown.** Mach 1.3 at 15,000 feet
and Mach 1.2 at 10,000 feet were outside the aeroplane's performance envelope. **Computed here from the
standard atmosphere, those are about 1,413 and 1,467 pounds per square foot, and they are the only two
above 1,400**, which is where the programme's own four-region figure draws reversal. **The report
attributes the shortfall to drag from the research instrumentation itself**, naming the external
deflection targets, the wiring, the pressure instrumentation and the camera pods.

---

## The Clearest Shortfall Is in the Region the Concept Is Aimed At

**Time-to-bank met the level 1 goal at the subsonic region I and supersonic region II test points.**
**At the subsonic region III test point it failed to meet even the level 2 requirement.**

**Region III is where the trailing edge has gone to zero and the leading edge carries the whole roll**,
which is precisely the regime a deliberately flexible wing exists to exploit.

**The demonstration is nonetheless real.** Roll rates within 15 to 20 percent of a production F/A-18
were obtained by active control of wing flexibility alone, **without the differential rolling
horizontal tail the production aeroplane uses for the job at these conditions.**

---

## Three Defects the Prose Read Caught

**A derivation error.** The stated reversal dynamic pressure dropped a term the article's own moment
balance produces. The full expression is now given, then the textbook reduction, **with the article
saying which one it uses and why**.

**An invented quantity.** The article had said the instrumentation added several hundred pounds. **No
source states any such figure.** Removed, and the article now says the record does not give it.

**A misattribution.** The performance shortfall had been attributed to weight, and the report
attributes it to drag. Corrected.

---

## A Broken Curated URL Cost a Build

**`ref_harv` pointed at a Wikipedia title carrying an agency prefix that returns 404.** The curated URL
sweep caught it while the production build was running.

**The build was killed rather than allowed to finish on a file that was about to change**, which is
A347's rule and the second consecutive article in which it has been enforced rather than rediscovered.

---

## The Sweep Store Needed No Tag, Which Is the Opposite of the Previous Article

**It removed 419 records of 6,127 and reading a sample found the
drops correct.** A349 had to switch seven patterns off across three tagged families, because its
subject was confusable names and the store is aeronautical. **This subject is a wing, and the store was
built by articles about wings.**

**Two adjacent families were checked closely.** The wind turbine blade is an aeroelastic structure and
the family stays armed, its drops being wind speed forecasting rather than blade aeroelasticity.
Rotorcraft aeroelasticity is not filtered at all and about 99 records carry it,
many of them tiltrotor wing work that belongs here.

---

## The Keystone Literature Is the Smallest Cluster and That Is the Finding

**22 records of 3,296, or 0.67 percent, are about
control reversal itself.** A probe found it at 32, so a second sweep was run in every vocabulary the
field has used across eighty years, 2,485 fresh records were gated to 565, and
the probe moved to 43.

**It is still the smallest cluster.** Reversal was solved in the 1940s by adding stiffness and the
answer held, so the literature closed. **A literature closes when a problem stops being open**, and
this article is about an attempt to reopen one that did not reach the condition.

---

## A Wait Loop Matched Itself and Never Terminated

**`after_build.sh` waits on `pgrep -f "jekyll build"`, and a shell running that loop has the string
`jekyll build` in its own command line.** So the loop matched itself, three of them accumulated, and
each waited for the others for ever while the build had long since finished.

**The build log said `done in 168.107 seconds` while `pgrep` still reported a match.** The audit was
run directly instead, and the lingering shells were killed.

**This is the same shape as A349's stale audit log**, where the audit raced the build and reported the
previous run's numbers. **The wait condition in that script is not trustworthy and the build log is**,
so read the log rather than the process table.

---

## Verification State

- `python3 _verify.py` reports **0 errors, 0 warnings**.
- `python3 _lib/test_lib.py` reports **104 of 104**.
- `tmp/a350/verify_numbers.py` reports **ALL CHECKS PASS**, with the dynamic pressures recomputed inside
  the checker from the atmosphere rather than compared against `analysis.json`.
- Reference integrity: **3,372 defined, 3,372 used, 0 undefined, 0
  orphaned, 0 duplicate URLs**.
- **All 25 foundational report identifiers verified against the report server before
  assembly**, and all six book links verified on title AND author.
- **All seventeen curated http URLs resolve**, after the one that did not was corrected.
- Prose: no contractions, no dashes, no prose colons outside citation labels, no inline span carrying a
  relation or a pipe.
- **7,223 lines, 41,819 words, 11 display equations, 3,372 reference definitions.**
- Survey **3,296 research records across 12 clusters**, report primaries 247 at 7.5 percent.
- **The stub-isolated production build succeeded in 168 seconds with no Liquid error**, against a
  checksum taken before it and re-verified after. **The rendered audit reports no findings across 89
  pages.** **Source 11 display equations against 11 rendered display blocks**, zero raw dollar pairs,
  zero unresolved reference brackets, page 625,332 bytes.

---

## Next

**A350 has three passes remaining**, the equation-density review, the primary-reference review and the
publication review, in that order and each on its own prompt.

**The equation pass has a great deal to work with.** The article displays eleven relations and the
report supplies far more that the prose currently states in words, among them the roll-mode time
constant against its level 1 and level 2 limits, the hinge-moment limits against the actuator
capabilities, the four-region boundaries as dynamic pressures, and the weight-against-stiffness trade
that is the whole motivation.
