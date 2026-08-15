## Last Updated

**Date**: 2026-08-14
**Task**: **A340, "X-Planes: Micro-Craft X-43 Hyper-X", publication review complete.** All four passes
done. Committed and **PUSHED**. **Not published**, and publication of this series has never been
authorised.

---

## The Comprehensiveness Gap Was in the Questions, Not in the Gate

**This article's most transferable finding is not about scramjets.** It is that a stability margin with
an uncertainty larger than itself is indistinguishable from a negative one, and that no single-factor
analysis can see it.

**The survey covered that subject with 235 records out of 11,279.** The first harvest reached the
margin and uncertainty literature only where it happened to sit beside a scramjet query, because every
query I wrote was about hypersonic propulsion. **The gate was working correctly and the questions were
too narrow**, which is a failure mode neither the self-satisfaction test nor the two-sided audit can
detect, since both only examine what the queries returned.

**A supplementary harvest of eighteen queries** on stability margins, uncertainty quantification, model
validation and mishap analysis **raised the pool from 21,376 to 27,748** and margin and control
coverage **from 235 records to 908 across two clusters**, one of them new. **A survey that
under-covers the subject of its own article's conclusion is not comprehensive**, and that is the test
I should have applied before the draft pass rather than at the publication review.

---

## The New Harvest Immediately Proved the Gate's Own Lesson Again

**I admitted the new vocabulary bare and the audit caught it within one run.** `uncertainty
quantification` admitted laser powder bed fusion. `epistemic uncertainty` admitted seismic shear-wave
velocity profiles. `six degree of freedom` admitted a robotic arm.

**Uncertainty methodology belongs to every field that computes**, which makes it exactly as
cross-disciplinary as hydrogen peroxide was in A339 and exactly as unsuitable for bare admission. All
of those terms are now conjunctions against aerospace context.

**The same audit found a homonym I would never have predicted.** **Waverider is also the make of an
oceanographic wave-measuring buoy**, and the gate admitted one deployed during a field experiment in
1980. It was a bare admit because a waverider is an unambiguous hypersonic configuration, and it is not.

---

## One Frame Varied, Three Words Deliberately Left

**"At the Mach N condition" appeared 14 times and now appears 4**, varied across a rotation of Mach
number, flight number and altitude rather than replaced by a single substitute. My first attempt
replaced them all with "on the second flight" and pushed `flight` from 10.79 to 11.31 per thousand,
which traded one tic for another, so I rebalanced.

**`flight` at 10.9 per thousand against a peer maximum of 5.4 was left alone.** Its collocations are
flight conditions, flight test, flight control, flight data, first flight, free flight and powered
flight, which are all legitimate compounds in an article about three flights of a flight research
vehicle.

**`margin` at 3.2 and `uncertainty` at 2.3 are similarly above every peer and are the article's literal
thesis.** Manufacturing variation there would obscure meaning to satisfy an instrument.

**NACA was expanded on first use**, which also let the article note that the body preceding NASA wrote
the 1953 report its derivations rest on.

---

## Verification

**All 44 worked figures were re-derived by a script that does not import the one that produced them**,
with inputs re-typed from the primary sources. All pass.

**All 34 curated non-DOI URLs resolve.** A 30-record sample of harvested DOIs returned 15 HTTP failures
and **all 15 are registered works in Crossref**, which is the pattern A339 documented and the reason
the catalogue now says the registry is the instrument and the landing page is not.

**Structural conformance holds**, with the twelve-section genre order present and in order and the
three series sections in place.

**Prose style scans clean on all five rules with zero caps-emphasis spans.** The 60 display delimiters
balance, no display fails to close on its own line, no inline math carries a pipe, and reference
integrity is exact at 12,584 used and 12,584 defined. `_verify.py` reports 0 errors and 0 warnings
across 301 posts and `./_check.sh --drafts` passes with the rendered audit clean.

---

## Counts and State

**26,249 lines, 30 display equations, 12,584 reference definitions, 141,861 words**, of which
**21,884 are author prose**, a dilution factor of 6.5.

**37 curated sources, all primary or canonical**, 32 from the NASA Technical Reports Server. **12,504
harvested records across fifteen clusters** from a pool of 27,748 at a 45.5 percent admit rate.
That reconciles as 12,504 harvested plus 37 curated plus 43 related-post links equals the 12,584
definitions in the file. **I wrote 12,547 here first, from memory rather than from the artefact**,
and caught it by checking the article's own table against the assembly output.

**This is the largest article in the series by every measure**, against A339's 21,067 lines and 9,831
references, and the length follows from a vehicle with a complete public record and a very large
adjacent literature.

**Forty-four of seventy-two drafted, none published, publication never authorised.** Forty-three of the
forty-four cite a sibling through `post_url` with no target in `_posts/`, so **the set publishes in
order or together**.

---

## One Operational Matter Worth Your Attention

**The deploy gate now takes about two hours.** It was roughly thirty-five minutes before A339. The
corpus carries two drafts above 20,000 lines with more than 22,000 link definitions between them, and
kramdown's link resolution does not scale linearly.

**Nothing is broken and every gate has passed.** But with twenty-eight X-Planes articles still to
write, each of which takes four passes, this is on track to become the dominant cost of the project.
**It may be worth deciding whether every pass needs the full build**, or whether `_verify.py` plus the
static checks suffice between passes with the full gate reserved for the publication review.

---

## What I Did Not Do

**I did not publish**, and I will not without an explicit instruction. The draft is pushed and sitting
in `_drafts/`.

**I did not trim anything to a length or reference target.** The directive is comprehensiveness and
this article earned its size.

---

## Next

**A341, "X-Planes: X-44, One Designation and Two Aircraft"**, editorial date 2025-11-19, series index
45, on your prompt. **The roster title says it is another disputed designation**, so expect the pattern
of A336 through A339 to continue. Nothing is outstanding on A340.
