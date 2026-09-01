## Last Updated

**Date**: 2026-08-31
**Task**: **A342 equation-density review, the second of four passes.** Committed, **not pushed**.
**This commit also carries the draft pass**, which was verified but not separately committed because
you prompted for the second pass while its build was still running. **8 display equations to 20.**
Nothing published and publication still not authorised.

---

## The Guard I Added Yesterday Caught the Same Defect Today

**A341's publication review found a display equation sharing a source line with prose, rendering as
inline math with two sentences run together, and added `math-display-inlined` to `lint.py` because
`render.py` structurally cannot see it.**

**It fired on the very next article.** An edit in this pass put `$$NT = 0 \Longrightarrow FO = 1$$` and
the following sentence on one line. **Caught before the build rather than after it**, which is the
whole difference between a lesson in a comment and a lesson in a test.

---

## Dividing Two Numbers the Draft Had Only Tabulated

**The X-45A and the X-45C carry the same payload fraction to four significant figures.**

$$\frac{680}{5{,}530} = 0.12297 \qquad \frac{2{,}040}{16{,}600} = 0.12289$$

**Their ratio is 0.99940 and the payload was tripled exactly.** The mass exponent in span is 2.977 and
the exponent computed from the payloads instead is 2.976, **which is the same number and is the
explanation.**

**So the near-cubic mass scaling is a held payload fraction and not geometry.** The draft called it a
coincidence of the mission sizing, which was right in direction and wrong to call it a coincidence.
**A scaling exponent that arrives from the mission looks identical in the arithmetic to one that
arrives from the shape and means something entirely different**, which is the warning this series has
recorded before against reading an exponent as a property of the technology. **The correction is
carried into the two aircraft section, the Epistemic State and the conclusion.**

---

## The Coupling the Draft Said It Could Not Evaluate

**The draft said a high-latency link raises interaction time and lowers the fan-out, and left it
there.** Written down, latency enters both halves and does not cancel, because it lengthens the
interaction without lengthening the neglect.

$$FO = \frac{NT + IT_{0} + 2\tau}{IT_{0} + 2\tau + SC}$$

**A satellite round trip costs 21.4 percent of the fan-out on a ten second interaction and a neglect
time three times it, and a quarter-second link costs 3.6 percent.** That is a design consequence
rather than an observation, and it says a supervised combat aircraft wants its operator within line of
sight or its autonomy raised to compensate. **What remains unquantifiable is this aeroplane's actual
latency, which is not published**, and the relation now says exactly what such a figure would buy.

---

## What Else the Pass Added

**Twenty relations from eight, across eleven edits.** The fan-out relation's own derivation, which the
draft asserted and did not derive, being that serving $N$ vehicles takes $N$ interaction times and each
must be served within its neglect time. **The operator's utilisation, which turns out to be the
reciprocal of the fan-out exactly**, so a fully occupied operator is a fan-out of one by definition.
The cost relation the programme's own argument rests on, in which only the crew term responds to
autonomy. The remotely piloted case as a limit, at zero neglect time. The payload fractions and both
exponents. Thrust to weight and the approach thrust fraction, which is the one relation in the
crosswind comparison that does not involve the wing. The approach speed, the wing area from aspect
ratio, the sideslip a crosswind produces, the demand index and the margin as a ratio of ratios. And
the flight rate.

---

## The Promoted-Subjects Rule Fired and Is Recorded Rather Than Closed

**Eleven displayed relations now carry no citation within a paragraph of themselves**, and the pass
promoted the cost-of-a-sortie argument, the operator utilisation relation and the latency coupling.
**That is the expected state after an equation pass**, since the reference base cannot follow a
derivation that did not exist when the pool was built, and closing it is the primary-reference pass's
business.

---

## From the Draft Pass, Since It Is In This Commit

**The keystone is not aerodynamic and its literature is not aeronautical.** One operator flew two
X-45As in coordination in August 2004, and inverting the fan-out relation for that ratio gives neglect
time exactly equal to interaction time, which is the autonomy the vehicle had and which no source
states. **At a fan-out of one an unmanned aeroplane has saved the pilot's life and nothing else.**

**The gate was written with two anchor families before the harvest rather than after**, because A341
twice rejected its own foundational sources for using the vocabulary of the underlying science. **The
supervisory-control cluster holds 399 records an aeronautical gate would have returned none of.**

**Two checks I expected to fail did not.** The X-45C's quoted thrust is admissible against its own
ceiling and yields a lower bound of 16.3 on an unpublished lift to drag ratio, the two figures pinning
each other. **My first attempt at that check omitted the ram term and reached the opposite
conclusion.** And the X-45A, which flew A341's condemned configuration sixty-four times, is not a
counterexample, being better off by 1.28 to 1.98 times across every plausible wing.

**I also cited forward to A343 and A344**, which would have failed the build since this series cites
backward only, and reference integrity caught it first.

---

## State

**A342 is committed and not pushed.** **14,090 lines, 20 display equations, 6,746 reference
definitions, 78,044 words**, of which 8,844 are author prose.

`_verify.py` clean apart from the `date-filename` artefact every draft reports, zero warnings,
`lint.py` **zero defects and zero conventions**, zero contractions, colons, semicolons, dashes,
parentheticals or caps-emphasis spans. Reference integrity zero undefined, zero orphaned, zero
duplicate URLs. **Every stated value re-derived by a verifier sharing no code with the computation**,
with every table row read out of the finished article. 126 of 126 NASA identifiers and 300 of 300
sampled Crossref identifiers resolve with zero title mismatches.

**Forty-six of seventy-two drafted, none published, publication never authorised.**

---

## Next

**The primary-reference review of A342 on your prompt**, which has eleven uncited relations waiting for
it, then the publication review, which is also the pass that pushes.

**Two items remain yours**, being whether `math-display-inlined` should move from `lint.py` to
`_verify.py`, now with a second incident behind it, and the caps defect on the live
`_posts/2026-08-06-native_lowering_coverage.markdown`. **`HANDOFF.md` is several commits stale** and
will self-report as invalid.
