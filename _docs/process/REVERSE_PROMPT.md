## Last Updated

**Date**: 2026-09-02
**Task**: **Process and tooling pass, taken at pilot discretion. No article content changed.**
**Not published**, and publication of the series still not authorised.

---

## A Resume Channel Contradicted Itself and the Warning Against That Was in the Same Block

**The Current Task block in `TASKLOG.md` stated two different drafted counts on consecutive lines**,
forty-eight and forty-seven, the second left behind by an edit that added the corrected figure without
removing its predecessor. It separately named A342 as the last article with all four passes complete,
when A343 and A344 were both finished and pushed.

**Eleven lines below the contradiction sat a paragraph saying this block has gone self-contradictory
six times and that a resume channel disagreeing with itself is worse than one merely out of date.**
That is the finding rather than an irony. **A warning addressed to a reader does not prevent a defect
introduced by an editor**, because they are not the same audience and the editor need not have read
the paragraph.

**Measured from disk before anything was changed**: 48 drafts carry `series: x_planes`, their indices
run 1 through 48 with no gaps, and 0 are published. Forty-eight was the correct claim.

---

## The Count Was Derivable All Along, So It Is Now Computed

**`_lib/progress.py`** counts the drafts of a series on disk and compares that to what the channels
claim. This is `survey.py`'s rule moved from an article to a process file: **a presence check asking
whether a file still says what it used to say goes green precisely when a number goes stale.**

**Two findings, kept separate because their causes and fixes differ.** `progress-stale` means a pass
did not update the channel. `progress-contradiction` means one edit left its predecessor standing, and
**comparing a single claim against the truth cannot catch that when one of the two claims is correct.**

**Wired into `_verify.py` as a warning rather than an error**, because the defect misdirects a
resuming agent rather than a reader and nothing reaches the built site.

**`HANDOFF.md` is deliberately excluded.** It is a snapshot that goes stale by design between
refreshes and self-reports staleness by a commit comparison, so a count check would fire on it every
time an article is drafted. **That is the permissive-checker failure recorded here the day before.**

---

## My First Pattern Was the Sloppy Kind This Project Keeps Catching

**`\d[\d,]*` for the number absorbed a trailing comma**, so `A297 through A344, drafted with all four
passes` read as a count. It matched **22 spans across `TASKLOG.md`**. Tightened to a real thousands
separator it matches **4**.

**The four surviving matches are why the check is scoped to one block rather than a whole file.** Two
are history entries stating a count that was correct on its own date. **One is `X-19 drafted`**, where
an aircraft designation ends in digits that read as a count, a shape appearing on nearly every history
line of a series covering X-1 through X-76.

**The check was proved to fire before it was trusted.** The contradiction was reintroduced and
`progress-contradiction` confirmed, because a green run after a repair is also exactly what a dead
check looks like.

**`HANDOFF.md` was re-stamped to parent `e5cdaa6` rather than left to go stale**, since its content
remained accurate and staleness would have cost a resuming agent its fallback for nothing.

**Verification**: `_verify.py` **0 errors and 0 warnings** with the new check live, `_lib` tests **94
of 94** from 89, all four claim shapes exercised including the two that must not match, and every
touched file byte-compiles with warnings as errors.

---

## The Sections Below Report A344 and Remain Current, Since No Article Work Has Happened Since

---

## Six of Seven Result-Driven Subjects Measured Thin, and Only One Closed

| claim the article makes | before | after |
|---|---|---|
| an automatic refusal on a detected fault is correct behaviour | 28 | **180** |
| relative rather than absolute positioning as a design choice | 129 | 130 |
| deriving a navigation accuracy requirement from geometry | 9 | 23 |
| fuel volume as the thing that sizes a wing | 4 | 17 |
| which constraint actually sizes a design | 4 | 10 |
| how precisely a manned carrier landing lands | 7 | 9 |
| how well a conceptual estimate matches what gets built | 1 | 3 |

**Each was broadened before being called thin**, which is the discipline three earlier passes failed,
and broadening moved none of them materially.

**Five did not close and three failed the same way.** The queries for which constraint sizes a design
returned 1,139 records and the gate admitted 648, those for estimate against outcome returned 881 and
admitted 371, and those for landing precision returned 680 and admitted 344. **A record the gate
admits is not a record about the subject**, because the gate admits on any anchor while an audit
measures one.

---

## The Article's Two Most Distinctive Claims Belong to a Different Discipline

**Identifying which constraint is active, and comparing a conceptual estimate against the aeroplane
that got built, are design methodology rather than aeronautics.** The aeronautical gate refuses that
literature correctly, and a gate admitting it would be the wrong gate for the rest of the article.

**The refused records for the second include a substantial literature on estimating the weight of a
foetus**, which shares the words and nothing else.

**So those two claims stand on the arithmetic rather than on a survey, and the article says so.** That
is the second article running to find one of its own arguments out of scope for its own gate, after
A343's claim about a requirement standing in for a measurement.

---

## The Instrument Failure Was Given a Guard, and the First Guard Was Wrong

**The same measurement failed three passes running and the third time it was one character.** A344's
audit asked for `arresting gear` with a space while the literature writes `ARRESTING-GEAR CABLE`.

**A diagnostic was built, measured and abandoned.** `separator_risks` flagged every literal space in a
pattern that a hyphen could defeat. Run over this article's twelve audit subjects **it flagged
eleven**, including `span of control`, `probe and drogue` and `sea state`, which no publisher
hyphenates. **A checker that fires on almost everything is the permissive-gate failure wearing
different clothes** and would have trained its reader to ignore it.

**What shipped instead is a builder.** `survey.loose("arresting gear")` returns a pattern that a
hyphen, a space or a run of space cannot defeat. **Making the right thing easy beats warning about the
wrong one**, and the refusal is recorded in the docstring because it is the more useful half.

---

## Counts and Fractions Across Four Stages

**The pool went 4,205, to 6,720, to 7,716, to 9,328.** Report primaries went **684 to 1,217 to 1,364
to 1,502**, at 16.3 percent, then 18.1, then 17.7, then **16.1**. Fitted primaries went **2,352 of
4,205 at 55.9 percent to 5,307 of 9,328 at 56.9**.

**Records from 2015 or later rose 1,696 to 3,608 while their share fell to 40.2 and recovered to
41.4**, and records predating 2000 went 979 to **2,576**. **The median moved back to 2011 and forward
again to 2012**, because the last harvest was aimed at fault management and design methodology, which
are current subjects, while the one before it reached the arresting gear literature of the 1950s.

---

## State

**A344 is committed and pushed. All four passes complete.** **19,382 lines, 24 display equations,
9,392 reference definitions, 103,575 words**, of which 8,130 are author prose. Editorial date
2025-11-22, series index 48, **full-aircraft class**.

`_verify.py` zero errors and zero warnings, `lint.py` **zero defects and zero conventions**, reference
integrity zero undefined, zero orphaned, zero duplicate URLs, all numerical checks passing with every
table parsed out of the finished article, **every survey and probe statistic recomputed from the
reference data**, 300 of 300 sampled Crossref identifiers registered and **111 of 111 NASA identifiers
resolved** with zero title mismatches, zero caps-emphasis spans, and zero contractions, colons,
semicolons, dashes or parentheticals in prose. **`_lib` tests are 89 of 89.**

**The stub-isolated production build succeeded in 5,619 seconds with no Liquid error**, against the
exact bytes that were pushed. **The rendered audit reports no findings across 60 pages.** Source and
rendered display-equation counts agree at **24**, with **zero raw dollar pairs leaking**, which is the
check A341 had to invent because a display equation demoted to inline math is invisible to the audit.
**Zero unresolved reference brackets**, all fourteen sections render in order, and the U.S. Standard
Atmosphere citation that the primary pass recovered resolves on the page.

**Forty-eight of seventy-two drafted, none published, publication never authorised.**

---

## Next

**A345, the Boeing X-48**, editorial date 2025-11-23, series index 49. **It is not a combat aircraft
and an earlier version of this note said the run continued into it.** The X-48 is Boeing's
blended-wing-body subscale demonstrator, flown with NASA and Cranfield. **The run of unmanned combat
aircraft was three articles and ended at A344**, so the supervisory-control and carrier vocabularies
should not be carried into A345 on the strength of that claim. **`gate.ATMOSPHERE` does carry
forward**, because it names the medium rather than the aeroplane.

**Two content decisions remain yours and both are on published posts.**
`_posts/2026-08-06-native_lowering_coverage.markdown` carries two authored caps-emphasis spans at
lines 879 and 1306, and thirteen published posts carry 1,045 shouted citation titles.
