## Last Updated

**Date**: 2026-09-01
**Task**: **A344 equation-density review, the second of four passes.** Committed, **not pushed**.
Nothing published and publication still not authorised.

---

## Ten Display Equations to Twenty-Three, and the Pass Settled a Question the Draft Left Open

**The draft printed two readings of the arrested landing and said the record does not choose.** Working
the relations through closes it, and the argument is dimensional rather than documentary.

**A stopping distance measured aboard a ship is a deck distance**, so it must pair with a speed
relative to that deck. Pairing a deck distance with an airspeed mixes two reference frames, which is
what the draft's first row did.

**The aeroplane's own wing then says which figure the quoted 145 knots is.** Reading it as a stalling
speed demands

$$C_{L,\max} = \frac{2 (W/S)}{\rho V^{2}} = 0.617$$

**which is too low even for a tailless planform.** Reading it as an approach airspeed gives 1.14 times
the stall at a maximum lift coefficient of 0.8, which is an ordinary carrier approach margin. **So the
engagement was slower than 145 knots and the deceleration is nearer 1.8 g than 2.7.**

**Both rows are still printed**, because the wind over the deck that day is not recorded and an
argument that fixes a reading is weaker than a document that states one. **Three places in the article
that said the question was open now say it is settled by argument**, being the framing section, the
epistemic state and the analysis.

---

## The Guard Fired for the Fourth Consecutive Article

**`math-display-inlined` caught one defect and it was mine again.** A replacement ending in a display
equation left the paragraph's remaining prose on the same source line. **A341 shipped this into a
build, A342 was caught by the workbench, A343 by the gate, and A344 by the gate.** Source pairs and
complete-line equations now agree at 23.

**A rounding defect was also caught.** The descent rate at three degrees and 145 knots was written 769
where the computation gives 768.4977, which rounds to 768. **That is the second article running in
which a table I wrote failed to round from its own arithmetic.**

**And the verifier broke itself by growing.** The arrestment table was matched by a regular expression
that became ambiguous when the equation pass added a hook-load table beginning with the same `| 145
kn |`. **A pattern that was unambiguous when written stopped being so when the article grew**, and it
now keys on words only the arrestment rows carry.

---

## What Was Added

**The relation the keystone rests on and never showed.** Differential positioning is now written out,
with the range equation carrying a satellite clock offset and ionospheric and tropospheric delays, and
the between-receiver difference cancelling the clock error exactly and the atmosphere very nearly.
**What is left is the vector between the two receivers**, which is the quantity the deck problem needs.

**The descent rate**, which the structure section named and did not compute. It is the approach speed
and the glide slope multiplied, giving 636 to 1,024 feet per minute, against two to three hundred for
an airliner. **A carrier undercarriage is a different component with the same name.**

**The hook load**, which the prose asserted and did not compute, at 339 to 496 kilonewtons applied at
a single point at the tail. **The deck runs 36.8 metres under the aeroplane while it stops.**

**The fuel volume argument for the wing**, which the draft named as a candidate and left untested. The
published range costs between 3,706 and 4,625 kilograms at plausible lift to drag ratios, **which is a
large volume to put in a wing this aeroplane has and a fuselage it barely has.** The test is not
conclusive because a published range figure may be a radius.

**Also the wing loading where it is first used rather than eighty lines later, the time to rest, the
wind over deck relation, the two ratios between the aircraft, the prediction ratio and the six percent
disagreement between sources.**

---

## The Promoted-Subjects Rule Fired

**Seventeen of twenty-three equation paragraphs carry no citation in their window.** Most are
arithmetic on cited values and legitimately need none. **The differential positioning relation is
cited to a standard text and the sizing relations to the design texts**, which were the ones that
needed it. **The remaining gap is the arresting gear as a machine**, whose deceleration this article
computes and whose literature it does not yet carry. Recorded rather than closed, per precedent, since
the reference base is the third pass's work.

---

## State

**A344 is committed and not pushed. Two of four passes complete.** **9,081 lines, 23 display
equations, 4,269 reference definitions, 49,841 words**, of which 6,686 are author prose. **References
held at 4,269 and measured before and after**, since an equation pass adds no sources.

`_verify.py` zero errors and zero warnings, `lint.py` **zero defects and zero conventions**, reference
integrity zero undefined, zero orphaned, zero duplicate URLs, **all numerical checks passing** with
every table row parsed out of the finished article, every cluster row checked by `_lib/survey.py`,
zero caps-emphasis spans on the corrected instrument, and zero contractions, colons, semicolons,
dashes or parentheticals in prose.

**Forty-eight of seventy-two drafted, none published, publication never authorised.**

---

## Next

**The primary-reference review of A344 on your prompt**, which is the third of four passes. **The
arresting gear and the satellite navigation literature are the two subjects the equation pass
promoted** and the audit should expect both to be thin.

**Two content decisions remain yours and both are on published posts.**
`_posts/2026-08-06-native_lowering_coverage.markdown` carries two authored caps-emphasis spans at
lines 879 and 1306, and thirteen published posts carry 1,045 shouted citation titles.
