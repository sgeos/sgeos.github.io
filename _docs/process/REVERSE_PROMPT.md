## Last Updated

**Date**: 2026-09-03
**Task**: **A348, X-Planes: Boeing X-51 Waverider, draft pass. The first of four.** Committed and
**not pushed**, since the draft pass does not push. **Not published**, and publication of the series
still not authorised. **Fifty-two of seventy-two drafted.**

---

## The First Article to Switch Sweep-Store Patterns Off, and It Nearly Was Not

**A346 recorded `ramjet` as a contaminant. A347 recorded `hypersonics` and `missiles`.** Both entries
carried a written warning that they must not be reused in the articles where those families are the
subject, and A347's named the X-15, X-30 and X-43 explicitly.

**A348 is the X-51. Those three patterns would have deleted 3,408 records, being 48.1 percent of
everything harvested**, including scramjet combustor flameholding, ramjet to scramjet mode
transition, waverider aerodynamics and inlet unstart prediction. That is not contamination. That is
the article.

**A warning addressed to a reader is not a mechanism**, which is this repository's oldest lesson and
it arrived again one article after the warning was written. `NOISE_PATTERNS` entries may now carry a
tag, `homonyms.TAGS` lists them, and `noise_hit` and `filter_records` take an `allow` list.

**An unknown tag raises rather than being ignored.** The quiet failure this prevents is an article
believing it has switched a filter off while its own subject is still being deleted, whose symptom
would be a thin survey with no explanation. Two regression tests cover both directions and the
library is **100 of 100**.

**Only tagged patterns can be switched off**, and every other pattern stayed armed, because
turbomachinery and atmospheric chemistry are contaminants here too.

---

## The Article

**The X-51A flew four times. On the flight that worked, the engine under test supplied under eight
percent of the vehicle's kinetic energy.** A 26 second rocket supplied 92.3 percent; the scramjet
supplied 7.7 across 210 seconds, taking 8.08 times as long to do a twelfth as much.

**A340 left a claim unfinished and this article tests it.** That article recorded that eleven seconds
on hydrogen has not demonstrated a propulsion system, because the thermal problem at length is a
different problem. **It was right, and the reason is arithmetic.**

**The X-51A flew 19.1 times longer than the X-43 at 6.67 times the lower heating rate, so it absorbed
2.86 times the heat load.** A short flight is a heat capacity problem. A long one is a heat transfer
problem, because the structure reaches equilibrium.

**The fuel does two jobs and they compete.** 270 pounds of JP-7 was the energy supply and the entire
heat sink aboard, and its heat sink capacity is 5.4 to 8.1 percent of the energy it releases.

**None of the three failures was combustion.** A thermal seal that had to take three quarters of an
inch of engine growth, an inlet unstart with a failed transition from ethylene to JP-7, and a fin
latch. **The discipline's exotic component works and its ordinary components did not.**

---

## The A347 Instrument Caught Six Errors in A348

**`_lib/booklinks.py` found six of eight book identifiers wrong in this article's first list.** The
two that were right are the two carried forward from A347's verified set.

**A hand-typed OpenLibrary key is wrong almost every time and a verified one stays right**, which is
an argument for the instrument rather than for care. Written one article ago, paid for immediately.

---

## Two Bugs of the Same Class, One in My Own Diagnostic

**A347's `\bcompressor\b` could not match `COMPRESSORS`.** While auditing A348 I wrote a probe for
civil-engineering contamination containing a bare `urban`, which matched inside **dist·urban·ce** and
reported 48 hypersonic flight-control papers as contaminants. **The probe was the defect.**

**Both are the A345 near-miss class**, where `\bX-?48\b` could not match `X-48B`. It has now appeared
three times, twice in patterns written to implement the lesson.

---

## Verification State

- `python3 _verify.py` reports **0 errors, 0 warnings**.
- `python3 _lib/test_lib.py` reports **100 of 100**, up from 98.
- `tmp/a348/verify_numbers.py` reports **ALL CHECKS PASS**, 38 recomputed claims, all present in the
  prose, 17 cluster rows matching their own citations, cluster table matching sections.
- Reference integrity: **5,441 defined, 5,441 used, 0 undefined, 0 orphaned, 0 duplicate URLs**.
- Book links **8 checked, 0 mismatched**. All eight foundational NTRS identifiers resolve.
- Prose: no contractions, no dashes, no prose colons, one semicolon and it is the `console.log` tag.
- **11,353 lines, 61,688 words, 10,451 author prose words, 19 display equations, none inlined.**
- Sweep store **121 patterns**, three of them tagged.

---

## Next

**The A348 equation-density review**, the second of four passes. **19 display equations is low** and
the pass has obvious targets: the oblique shock relation solved for this vehicle's conditions, the
Kantrowitz starting limit, the isolator pressure rise, one-dimensional scramjet cycle relations,
stream thrust and specific impulse, the Rayleigh line for heat addition in a duct, and the
Sutton-Graves heat flux correlation the article currently uses only as a proportionality.

**The book-identifier repair for A342 through A346 remains outstanding and still needs your
decision.**
