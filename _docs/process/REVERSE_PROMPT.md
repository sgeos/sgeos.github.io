## Last Updated

**Date**: 2026-09-05
**Task**: **A350, X-Planes: Boeing X-53 Active Aeroelastic Wing, primary-reference review. The third of
four.** Committed, **not pushed**, since only the publication review pushes. **Not published**, and
publication of the series still not authorised. **Fifty-four of seventy-two drafted.**

---

## The Programme's Own Citation Chain Had Been Read and Not Cited

**The flight test report's bibliography names the papers the programme was built on**, and the draft
used the report's account of those papers without pointing at a single one of them.

**Fourteen were added.** The wind-tunnel programme's summaries and its flutter suppression and model
reduction work. The applications of the concept to an F-16 derivative wing and to the Agile Falcon,
neither of which became the testbed. The flight programme's own plan and its technical and analytical
development. The strain-gauge load calibration and the deflection-based loads estimation. The high
alpha research vehicle that supplied the wings. **And the production support flight control computer**,
which matters because the article calls the research flight control system the first of its kind on an
F/A-18 in a safety-of-flight critical envelope, and the computer it ran on had been built for the fleet
beforehand.

**Every identifier was verified against its repository before assembly**, which is the discipline that
caught a fabricated identifier in A347 and another in A349.

---

## The Primary Count Splits Into Two Kinds and the Article Now Reports Both

**Primaries are 261 of 3,307, or 7.9 percent**, up from 247 of
3,296 at 7.5.

**254 carry a report-server or defence-registry identifier**, which is what
the corpus-wide measure can see.

**7 are journal and conference papers named by hand**, and the measure
cannot see them because an aeronautical society's identifier looks like any other digital object
identifier. **That is the same blind spot A349 hit and reported**, in a milder form, and reporting both
numbers costs nothing and prevents a reader inferring the wrong thing from either.

**Named foundational sources stand at 39.**

---

## The Classical Literature Was Carrying More Than Its Citation Count Suggested

**The sizing section rests on the wartime and early postwar work that settled reversal by adding
stiffness, and that work stood at two reports cited once each.** Two more were added, and the article
now says plainly that this literature is older than the jet engine and was not superseded.

**That matters because it is the article's argument.** The X-53 exists to reopen a question the
classical answer closed, and an article which asserts that while citing the classical answer twice is
asserting rather than showing.

---

## An Anachronism the Prose Read Caught

**The article had the Air Force Research Laboratory sponsoring a programme that ran from 1984.** That
laboratory was formed in 1997, a year after the flight programme began.

**The predecessor is named in the flight test report's own first reference**, being the Flight Dynamics
Laboratory of the Air Force Wright Aeronautical Laboratories. The article now names it and dates the
change, and the correction improves the story rather than merely fixing it, because the sponsor
changing identity between the tunnel programme and the flight programme is part of how long this took.

---

## A Wait-on-Log Matched a Previous Build's Completion Token

**The equation pass replaced `pgrep` with a wait on the build log for `done in`, because the process
wait had matched itself.** This pass found the replacement's own failure mode.

**The wait began before the log was truncated**, matched the previous build's completion line, returned
immediately, and the audit then ran against a `_site` that `make_stub.sh` had just deleted. The audit
reported the directory missing, which is the loud failure and the lucky one.

**A completion token is only evidence if the log is known to be fresh.** That is the third variant in
two articles of the same mistake, after A349's stale audit log and this article's self-matching process
wait. **Truncate or timestamp the log first, then wait on it.**

---

## Verification State

- `python3 _verify.py` reports **0 errors, 0 warnings**.
- `python3 _lib/test_lib.py` reports **104 of 104**.
- `tmp/a350/verify_numbers.py` reports **ALL CHECKS PASS**, with the actuator moments and the dynamic
  pressures recomputed inside the checker rather than compared against the generator.
- Reference integrity: **3,384 defined, 3,384 used, 0 undefined, 0
  orphaned, 0 duplicate URLs**.
- **All seven book links verified on title AND author.** **All seventeen curated http URLs resolve.**
- Prose: no contractions, no dashes, no prose colons outside citation labels, no inline relation, and
  **zero instances of the insertion signature the equation pass added a check for**.
- **7,404 lines, 43,817 words, 27 display equations, 3,384 reference definitions.**
- Survey **3,307 research records across 12 clusters**.
- **The stub-isolated production build succeeded in 837 seconds with no Liquid error**, against a
  checksum taken before it and re-verified after. **The rendered audit reports no findings across 89
  pages.** **Source 27 display equations against 27 real rendered display blocks**, three line-spacing
  directives accounting for the raw count, zero raw dollar pairs, zero unresolved reference brackets,
  page 641,950 bytes. **This build took thirteen times longer than the equation pass's**, on a
  reference block twelve records larger, so build time is not linear in the corpus and a wait must be
  open-ended.

---

## Next

**A350 has one pass remaining, the publication review.**

**Expect it to read the opening against the conclusion first**, which has found a defect in five
consecutive articles. **The specific risk here is that the article has gained three sections since the
conclusion was written**, on the actuator overload arithmetic, on the primary split, and on the
classical literature, and the conclusion mentions none of them.
