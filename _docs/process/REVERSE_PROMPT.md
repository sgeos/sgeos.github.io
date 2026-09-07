# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

## Last Updated

**Date**: 2026-09-07
**Task**: **A351, X-Planes: Gulfstream X-54, draft pass. The first of four.** Committed and **not
pushed**, which is what the draft pass asks for. **Not published**, and publication of the series
still not authorised. **Fifty-five of seventy-two drafted.**

---

## The Registry Entry Is the Article, and It Was Verified Rather Than Admired

**The X-54A was designated on 5 May 2008 to Gulfstream Aerospace, sponsored by NASA, and the register
states its mission as generating relevant ground sonic boom signatures `in support of NASA and a
regulatory change process`.** It was never built.

**The opening claim was measured against the register rather than asserted.** Of the 510 designations
allocated between August 1998 and November 2025, **exactly one mission statement contains the word
`regulatory`**, and `certification`, `rulemaking` and `policy` appear in none of them. `registry_scan.py`
computes that and `assemble.py` asserts it, because it is the first sentence a reader meets.

**The first version of that opening said `Every other aeroplane in this series was designated to fly`,
which is vague and also false.** The X-6, the X-20, the X-30 and the X-33 all have articles here and
none flew in the form its designation names. **An impression was replaced by a count.**

---

## The Central Computation Is One the Source Set Out and Did Not Perform

**The Quiet Spike flight test report says a ground signature was not attempted because `the stronger
shocks of today's aircraft would overtake the spike's weak shocks within a short distance below the
flight path`.** That is the case for building the X-54, written by the people who would have built it,
two years before the number was allocated.

**`A short distance` is a quantity and weak-shock theory gives it.** Two shocks close at a rate set by
the difference in their strengths, the speed of sound cancels, and the coalescence distance is

    L = separation * 4 gamma / ((gamma + 1) * d(dp)/p)

**At the weakest shock difference in the plausible range it is 1.73 kilometres, and at a typical one
0.35 kilometres, against 13,716 metres of air below the test altitude.** So the shaped signature is
destroyed in the first 12.6 percent of its journey at best and the first 2.5 percent typically.
**The conclusion survives an order of magnitude of uncertainty in the assumption**, which is the only
reason it is worth stating, and geometric spreading would have to lengthen the distance by a factor of
7.9 before it changed. **Both limitations are stated in the article rather than buried.**

**This is the A350 rule applied one article later.** A source that has done the measuring has not
necessarily done the arithmetic.

---

## The Sweep Store Predicted Wrong, and the Prediction Was Written Down First

**The harvest script said the subject is aeronautical, the store is aeronautical, and no family should
need switching off. Thirteen did.**

**Measured with one instrument on both settings.** Fully armed the store dropped 375 records and the
gate then kept 2,485. With thirteen families off it dropped 147 and the gate kept 2,577, so **228
records returned and 92 reached the corpus**. Among the deletions were `Underwater measurements of a
sonic boom`, `Meteorologically Induced Variability of Sonic Boom of a Supersonic Aircraft`, a citation
of the 1976 standard atmosphere, and the whole community-noise exposure-response literature.

**The reason is structural rather than accidental.** Every pattern in the store was earned by a sweep
whose subject was an aeroplane, and this article's subject is a noise. **Community-noise research is
one methodological field in which railways, roads and wind turbines are cases beside aircraft rather
than contaminants of it.**

**Nine tag families were added, taking the store from six tags to fifteen.** `ramjet` is deliberately
left armed because its recorded incident still holds here, and the residual cost of the families left
armed is 28 records, reported rather than filtered away.

### And a Second Pattern Covered a Family That Had Already Been Tagged

**The wind-turbine community-noise literature was still being deleted after the `wind-energy` tag was
applied**, because two separate store entries match that family and only one carried the tag. **That
is precisely the failure `homonyms.TAGS` exists to prevent**, met from a direction the mechanism does
not cover, since a tag switches off one pattern while a contaminant family can be spread across
several. **It was found by measuring the residual, not by reading the store.**

---

## A False Finding Was Caught Before It Shipped

**On the main sweep alone, Mach cutoff measured 17 records against a pool of 2,627 while low-boom
shaping measured 283.** This article was going to report that the mechanism which actually changed the
rule is less studied than the mechanism that did not.

**A supplementary sweep aimed at it returned 87 and the contrast evaporated.** The rewording had moved
it from 24 to 17, so the vocabulary did nothing and the harvest did all of it, and reporting only the
endpoints would have credited the wording with the sweep's result.

**A pool that was not asked returns an absence indistinguishable from one that was.**

---

## Instruments That Failed and Were Fixed

**A `str.replace` matched nothing and reported success.** One of four gate patches silently did not
apply, and the audit sample showed the defect it was supposed to fix still present. **Every
substitution in this article's scripts now asserts its match count**, and `assemble.py` asserts every
slot present before substitution and none left after.

**A new checker compares every prose citation label to the title of the thing it points at.** The
survey's labels are emitted and cannot drift; the body's are typed. **It found one**, a label reading
`Overview of Low-Boom Flight Demonstration Mission and X-59 QueSST Aircraft` over an anchor whose
target is `An Overview of NASA Sonic Boom Flight Research`. Nothing else in this repository would have
seen it.

**One curated DOI was wrong and the identifier check caught it before assembly**, pointing at a paper
on thermals and cloud modelling under a claim about sonic-boom generation theory. **Forty-two curated
identifiers verified, forty-one right.**

**Two checkers were themselves wrong and both failed in the dangerous direction.** The number verifier
cut the article at the survey heading and threw away everything after it, then reported a number
missing that was present. The paragraph-opening check used a negative lookahead that let a decimal
through, so `17.6 years after the number was allocated` opened a paragraph with a numeral unseen.

**And the test written to lock the store fix in place passed for the wrong reason.** Two of its
eleven titles were never deleted by their title at all, having been removed through their venue, so
those assertions would have passed with the fix reverted. **`_lib/test_lib.py` now asserts each title
is armed BEFORE asserting the tag disarms it**, and the venue cases are exercised through
`filter_records` with a venue attached. **A test that cannot fail is not a test**, and this is the same
shape as A348's check that went green without checking anything. Tests are 105 of 105.

**One probe was mis-instrumented.** The indoor-response probe's field wording was narrower than its
plain wording, so it reported a shelf that shrank on restatement. **A rephrasing that loses records is
a worse instrument, not a smaller field**, and the second column must now be a superset of the first.

---

## What the Article Says

**Eleven display equations**, covering the Mach angle, weak-shock propagation speed, the coalescence
length, Whitham's F-function, the equivalent area with its lift term, the pre-steepening pressure, the
N-wave decay exponents, the shock rise time, the sound exposure level and the cutoff Mach number.

**The cutoff Mach number falls out as a temperature ratio and nothing else**, giving 1.153 for the
standard atmosphere above the tropopause and moving by 0.04 for ten kelvin of ground temperature. **So
the technique that actually changed the rule is a forecast rather than a chart.**

**The altitude argument was backwards in the first draft.** It said doubling the distance costs 40.5
percent of the overpressure and called that a weak lever, which is not weak at all. **The lever is
weak because the range is short**, so the article now states that climbing from 45,000 to 50,000 feet
buys 7.6 percent and that halving the boom by climbing alone needs 113,393 feet.

**Two conclusions remain thin and the article says so.** That a shaped nose on an ordinary aeroplane
cannot deliver a shaped ground signature, at 41 records, resting on a primary document and on the
arithmetic above. That the rule is the deliverable and the aeroplane the evidence for it, at 57.

---

## Counts

| Quantity | Value |
|---|---|
| Lines | 6,745 |
| Words | 39,473 |
| Display equations | 11 |
| Reference definitions | 3,159 |
| Research records | 3,072 |
| Report primaries | 318, being 10.4 percent |
| Curated sources | 42, every identifier verified |
| Books | 7, every key resolved on the search index |
| Retrieved across two sweeps | 8,289 |
| Through the subject gate | 3,210 |
| Clusters | 11, residual 57 |

---

## Open Questions for the Pilot

**A324's `book_jenkins` label remains the one live repair**, unchanged from the last report. The key is
correct and the label swallowed the title.

**The OpenLibrary work pages returning Internal Error to a reader** is also unchanged. The seven book
keys in this article were resolved against the search index rather than the work endpoint, which is
what `_lib/booklinks.py` now does.

**Nothing is pushed.** The draft pass commits and does not push, and the next prompt in the rhythm is
the equation-density review.
