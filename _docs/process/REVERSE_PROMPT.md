## Last Updated

**Date**: 2026-09-02
**Task**: **A345 publication review, the fourth and last of four passes.** Committed and **pushed**.
**Not published**, and publication of the series still not authorised.

---

## The First Finding Was Prose Rather Than Coverage

**The primary pass left the article narrating its own drafting history inside the argument.** What the
Data Changed contained the sentences `the draft of this article argued` and `the part the draft of
this article got wrong`.

**A reader has no access to a superseded draft.** The correction was right and the framing made the
reader follow a position the article had already abandoned. **Three passages were rewritten to state
the corrected position directly**, and the one legitimate place for such a note, the Epistemic State,
keeps it.

**Two related repairs.** A section headed `the Scaling Says Which to Trust` had a body whose first
sentence declined to say which, so it was renamed. **The conclusion stated a strong claim in one
paragraph and qualified it in the next**, which reads as a walk-back, so the qualification now travels
with the claim.

---

## The Results Probe Fired for the Sixth Article Running, and This Time Broadening Closed It

**Twelve conclusions were measured against the survey and eleven were thin in the article's own
words.** Then each was restated in the words a publisher would use in a title.

| Result | Article's words | Field's words | After harvest |
|---|---|---|---|
| support interference in a wind tunnel | 4 | 293 | **488** |
| the leading edge as the thing that sets stall angle | 88 | 449 | 452 |
| a remote pilot against compressed time | 10 | 347 | 350 |
| validating a flight control system | 29 | 359 | 366 |
| vertical surface placement and tail volume | 6 | 188 | 188 |
| a common data repository for correlation | 6 | 102 | 148 |
| a cryogenic tunnel as the Reynolds instrument | 8 | 125 | 133 |
| post-departure modes never compared with flight | 4 | 88 | 102 |
| the mass condition of a dynamic model | 12 | 47 | 74 |
| ground-to-flight correlation as a method | 7 | 23 | **51** |
| engine-out on a two versus three engine layout | 23 | 34 | 34 |
| thrust to weight as a scaling invariant | 3 | 5 | 5 |

**Restating the question moved eight of the eleven above forty with no harvesting at all.** The
article's own closing result went **4 to 293**, because the literature says wall interference,
blockage correction and sting correction at least as often as it says support interference. **A
targeted harvest then closed a ninth**, ground-to-flight correlation going 23 to 51.

**THIS IS THE OPPOSITE OF A340 THROUGH A344.** The same probe measured those articles thin and
broadening moved none of them, because they concluded about subjects with genuinely small literatures.
**Here almost every thin measurement was an artefact of vocabulary.**

**The transferable lesson is that a thin measurement is a question and not an answer.** The reflex
that thin means narrow was right nine times of twelve here and wrong three times in A343, which is why
the table carries three columns rather than one.

**Two entries stayed low and neither is a gap.** Engine-out on a two against a three engine layout is
a small real literature at 34. **Thrust to weight being invariant under Froude scaling stands at 5 and
will not move**, because it is dimensional analysis rather than a finding.

---

## I Typed Three Values Into That Table and All Three Were Wrong

**The leading-edge row was written 194 and measures 89. Engine-out was written 68 and measures 23.
Flight-control validation was written 100 and measures 29.** Every one was invented in the direction
of the story being told.

**The table is now emitted by `results_table.py` from the pool**, and the number verifier reproduces
all twelve rows in all three columns against the two pools. **The corpus rule about recomputing rather
than matching was written for statistics carried between passes and applies just as well to a number
typed once.**

---

## State

**A345 is committed and pushed. All four passes complete.** **17,749 lines, 36 display equations,
8,534 reference definitions, 97,843 words**, of which 10,012 are author prose, a dilution factor of
9.8. Editorial date 2025-11-23, series index 49, **full-aircraft class**.

Research 6,114 to **8,466** across the four passes, report primaries 796 to **1,642**, fraction 13.0
to **19.4 percent**. Median publication year 2006, **2,744 records from 2015 or later** at 33.7
percent, **3,293 predating 2000**.

`_verify.py` zero errors and zero warnings, `lint.py` **zero defects and zero conventions**, reference
integrity **8,534 used and defined, zero undefined, orphaned or duplicate**, every stated value
re-derived by a verifier that does not import the computation, **all 17 survey rows agreeing across
three counts and all 12 results rows across three columns**, source and lint display-equation counts
agreeing at 36, **300 of 300 sampled Crossref identifiers registered and 224 of 224 NASA identifiers
resolved** with zero title mismatches, and zero contractions, colons, semicolons, dashes,
parentheticals or caps-emphasis spans in authored prose. **`_lib` tests are 95 of 95.**

**The stub-isolated production build succeeded in 1,940 seconds with no Liquid error, against the exact bytes that were pushed**, the article's checksum having been matched against the stub copy before the build started. **The rendered audit reports no findings across 84 pages.** Source and rendered display-equation counts agree at **36**, with **zero raw dollar pairs leaking** and **zero unresolved reference brackets**. **Two earlier builds were killed and restarted** because the article changed after they began, and a build of superseded bytes verifies nothing about what ships.

**One curated source fails the sweep and resolves by hand.** `cranfieldaerospace.com` returns 200 to a
browser user agent and is refused to the sweep, which is the documented bot-mitigation case rather
than a citation failure.

**Forty-nine of seventy-two drafted, none published, publication never authorised.**

---

## A Documentation Defect Fixed on the Way

**The stub-build recipe in `HANDOFF.md` omitted the `vendor` step and cost this pass two failed
builds.** The copy excludes `vendor`, which holds the installed bundle, and nothing put it back, so
the build fails with `Bundler::GemNotFound` listing every gem. **Setting `BUNDLE_PATH` does not fix
it**, because the stub carries its own `.bundle/config` pinning a relative `vendor/bundle`. The recipe
now says to symlink the real `vendor` into the stub.

---

## Next

**A346**, editorial date 2025-11-24, series index 50. **Nothing is mid-rhythm.**
