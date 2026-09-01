## Last Updated

**Date**: 2026-08-31
**Task**: **A342 primary-reference review, the third of four passes.** Committed, **not pushed**.
Nothing published and publication still not authorised.

---

## The Keystone's Own Vocabulary Measured Three Records

**Neglect time and interaction time are the two quantities the fan-out relation is built from, and the
pool the first two passes built held three papers using those words.** That is the sharpest gap this
series has found underneath an article's own keystone.

**A targeted harvest closed three of six gaps decisively and improved the rest.**

| subject | before | after |
|---|---|---|
| latency and delay in remote control | 18 | 210 |
| approach, landing and the low-speed end | 25 | 158 |
| aircraft mass fractions and the sizing loop | 6 | 100 |
| manpower and the economics of operating aircraft | 24 | 48 |
| neglect time and interaction time | 3 | 47 |
| scaling laws across aircraft size | 1 | 11 |

**The audit was written in the field's vocabulary from the outset this time**, which is the correction
A341's primary pass had to make halfway through after reporting its own comparison baseline at eleven
records where the pool held 204.

---

## The Definition of Primary Had to Fit a Subject Spanning Two Fields

**A NASA report is primary for the aerodynamics and an ACM conference paper is primary for the fan-out
relation**, and a definition admitting only the first would have reported this article's keystone
literature as entirely secondary.

**Report primaries went from 359 to 914, or 5.4 percent to 9.7.** On the fitted definition, which adds
the AIAA, SAE, ACM and IEEE venues, primary sources went from **3,438 of 6,671 at 51.5 percent to 5,130
of 9,444 at 54.3**. **The ACM count went from 47 to 92**, which is small and is the venue the keystone
was published in.

**Both numbers reported, because the count-versus-fraction trap fired again.** Records from 2015 or
later rose from 3,487 to **4,452** in count while falling from 56.4 percent to **50.9** in share, and
records predating 2000 went from 942 to **1,798**.

---

## A Defect the Corpus Had Already Recorded, and I Did Not Carry It Forward

**The gate refused `Validating Human-Robot Interaction Schemes in Multitasking Environments`, which is
where neglect tolerance is measured rather than assumed, because the publisher sets `Human-Robot` with
an en dash.**

**A334 recorded exactly this**, on a nickel-hydrogen battery paper whose depositor used U+2010, and
said the normalising step should be copied forward. **It was not copied forward into A342.**

**So the fix went into the library rather than into the article's script.** `_lib/gate.py` now
normalises typographic dashes and quotes for every gate, with a regression test covering six dash code
points and checking that an off-subject title is still refused. **Re-running the original harvest
through the normalising gate admitted 23 records that were being refused on the shape of a dash
alone.** A per-article fix had already failed once and the library is where it stops failing.

---

## The Second Rejection Is Not a Defect and Is More Interesting

**`Remote Manipulative Control with Transmission Delay`, published in 1963, uses none of the modern
terms for its own subject.** It predates `latency`, `teleoperation` and `supervisory control` as terms
of art. **A gate written in a field's current vocabulary cannot reach that field's origin**, and the
only remedy is to know the document exists and fetch it by identifier.

**That paper turned out to matter more than I expected.** Sheridan and Ferrell measured the operator's
completion time growing with transmission delay in 1963, and four years later named the response to
it, which was to stop transmitting movements and start transmitting intentions. **Supervisory control
was invented as an answer to latency**, and the X-45A is an aeroplane built on that answer. The
article now says so, thirty-nine years of lineage in two citations.

---

## Twelve Foundational Primaries, Each Cited Beside Its Relation

Olsen and Wood on fan-out. Crandall and others on neglect tolerance measured. Steinfeld and others on
the common metrics framework. Whetten and Goodrich, twice, on the switch cost and the multi-operator
case. Crandall and Cummings on performance metrics. Cummings and colleagues four times on operator
capacity, controller capacity, scheduling strategy and decentralised control, **all of it about
aircraft specifically and all of it within eight years of the demonstration**. And Sheridan and
Ferrell twice, in 1963 and 1967.

---

## Three Subjects Remain Thin and Each for a Different Reason

**Scaling laws across aircraft size return eleven**, because the square-cube argument is a textbook
subject rather than a journal one, and it is cited to books.

**Neglect and interaction time return forty-seven**, because those exact terms belong to a small
sub-community while the concepts are covered elsewhere in the survey, under operator workload at 246
and fan-out at 220. **The thinness is in the vocabulary and not in the coverage**, which is a
distinction worth making rather than harvesting against.

**Manpower and crew cost return forty-eight**, because much of the analysis that would answer it is
defence work not published where a bibliographic sweep reaches. **Same limit this article already
records for its datalink cluster.**

---

## State

**A342 is committed and not pushed.** **Three of four passes complete.** 20 display equations held and
measured before and after, **9,519 reference definitions**, and the supervisory-control cluster grew
from 399 records to 1,062.

`_verify.py` clean apart from the `date-filename` artefact, zero warnings, `lint.py` **zero defects and
zero conventions**, zero style violations. Reference integrity zero undefined, zero orphaned, zero
duplicate URLs. **Every cluster row and the survey total check against the data the article ships
with.** `_lib` tests 82 of 82 after the new one.

**One caps-emphasis span was introduced by me in this pass and removed**, which is the third time
across A341 and A342 that I have reintroduced the class the 2026-08-14 audit cleared.

**Forty-six of seventy-two drafted, none published, publication never authorised.**

---

## Next

**The publication review of A342 on your prompt**, which is also the pass that pushes.

**Two items remain yours**, being whether `math-display-inlined` should move from `lint.py` to
`_verify.py`, now with two incidents behind it, and the caps defect on the live
`_posts/2026-08-06-native_lowering_coverage.markdown`. **`HANDOFF.md` is several commits stale.**
