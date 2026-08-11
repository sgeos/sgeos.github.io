# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-10
**Task**: A330 primary-reference review, the third of four passes. Committed, **not pushed**, **not
published.**

**References 5,392 to 7,028 definitions and 5,324 to 6,966 cited research records**, article 17,667
to 22,653 lines and 95,132 to 120,576 words. Display equations unchanged at 90. **All 6,966 master
records cited with none left over.**

---

## The Promotion Rule Fired Harder Than in Any Previous Article

**I audited the twenty-seven subjects the article's equations actually name against the pool, before
harvesting rather than after.** Eighteen were thin on period coverage and **six were at zero**,
including **the rocket equation, the ascent loss budget, minimum gauge, integral tank structure,
cryopumping and the noncircular pressure vessel.**

**None of those is thin because the literature is thin.** They were thin because the first two
harvests asked for tanks, composites, cryogenics and aerospikes, **and before the equation pass the
article had no reason to ask for knockdown factors, face wrinkling, flatwise tension or an ideal
velocity increment.** The harvest that followed used the period's own vocabulary, which is not the
article's, so shell buckling was sought as design criteria for thin-walled circular cylinders and
the bond test as flatwise tensile strength.

**Result: 1,531 more records published through 2001 and 464 more from the report literature.**

---

## Two Finds Worth Naming

**The design monograph the article's own buckling relation comes from is now cited by name.**
Weingarten, Seide and Peterson, 1968, is the agency's design criteria document for the buckling of
thin-walled circular cylinders, and it supplies **both** the knockdown factor the article sweeps and
the pressure-stabilisation term that corrected it. The article was using that practice without
attributing it.

**The literature for the one term the article admits it did not price turns out to be thirty years
older than the X-33.** A 1965 report series on **juncture stress fields in multicellular shell
structures**, running to at least eight volumes and including the buckling analysis of the junction
itself, is exactly the bending-at-the-lobe-junction problem the mass build-up leaves unaccounted, and
a two-hundred-inch multicell tank was pressure tested in 1968. **The knowledge that a lobed tank is
expensive at its junctions was old when the X-33 was designed**, which makes the membrane model's
silence a choice of model rather than an absence of information. That sentence is now in the article.

---

## The Count-Versus-Fraction Trap, in Its Classic Form

| | Before this pass | After |
|---|---|---|
| Research references cited | 5,324 | 6,966 |
| Period through 2001 | 2,488, 46.7% | 4,019, 57.7% |
| Contemporary 2015 onward | 2,162, 40.6% | **2,186, 31.4%** |
| Report literature | 1,231, 23.1% | 1,695, 24.3% |

**The contemporary COUNT rose by twenty-four and the contemporary FRACTION fell by nine points.**
Nothing was removed. The denominator moved. **Reporting only the fraction would have described a
loss that did not occur**, and reporting only the period gain would have concealed that the modern
half is now proportionally thinner. The article states both in a subsection of the Source Base and
says which moved.

---

## Two Subjects Are Genuinely Thin and Are Reported Rather Than Padded

**Minimum gauge as a design driver returns nothing at all in a pool of nearly seven thousand
records**, which is awkward, because the article's own finding is that the facesheets are governed by
it.

**Flatwise tensile testing of a core-to-facing bond returns almost nothing retrievable**, and that is
the more troubling of the two, **because it is the literature of the exact failure that ended the
programme.** The mechanism is well understood and the test is standard, so the absence is more likely
an artefact of what is indexed than a gap in what was done. The article says so.

---

## Three Homonyms, Two of Which I Created by Widening

**Admitting the word multicell to reach the juncture-stress reports also admitted an eleven-volume
fluidized bed boiler programme and a nickel-hydrogen battery common pressure vessel.** Both use the
word exactly as this article does and neither is about a tank. Seventeen records, paid for at the
moment of widening rather than in the sweep.

**A shell is also a quantum field theory object**, and one Casimir self-stress paper on a perfectly
conducting cylindrical shell reached the structures cluster. Found by reading a random sample, not by
anticipation.

**Anticipated and filtered before the harvest ran**: gene knockdown, gauge theory and the railway
gauge, skin wrinkling in dermatology, the chemical and fruit peel, condensation in chemistry and
building physics, and separation in psychology and chemical engineering. **Gene knockdown and gauge
theory would have done real damage**, since the article now uses both words as terms of art.

---

## Two New Clusters, One of Which Is Part of the Failure Chain

**Cryogenic insulation was not a heading and should have been.** The purge gas that cryopumped into
the core exists **because the tank is cold and insulated**, so the insulation system, the purge
cavity and the sealed core are three parts of one arrangement rather than three independent choices.
The article now says that, and adds that a tank sized by volume has a large surface for the
propellant it holds, **so the propellant hardest to contain is also the one with the most surface
through which to boil away.**

**Manufacturing and scale-up is the other**, and it holds ten records, which is the thin subject
above.

---

## An Assertion With No Citation, Which Is What This Pass Is For

**The three documents the article leans on most heavily were cited nowhere.** The tank geometry, the
sandwich construction, the unvented core, the five causes of the failure and the fifteen-minute delay
were all asserted in prose and all taken from the agency's review of the state of the art in liquid
hydrogen cryogenic tank structures and from the failure investigation's own findings.

**It does not matter that every assertion was correct.** An unsourced claim about a document is
indistinguishable from an invented one, and a reference pass that adds sixteen hundred records while
leaving the article's own foundation uncited would have measured the wrong thing. All three are now
cited at the point of use, and the word **unvented** has been restored to the description of the
core, which is the single most important adjective in the failure and had been dropped.

---

## Verification

`verify.py` **104 of 104** with **18 agreements between independent routes**, unchanged, since this
pass added no arithmetic. `check_any.py` passes. `_verify.py` holds the baseline at **0 errors and 21
warnings**. `test_lib.py` is **49 of 49**.

**The reference-entry scan found zero punctuation defects across 13,992 visible entries**, with zero
duplicate definitions, zero undefined uses and zero orphans. **The entity fix from the draft pass is
holding at more than twice the reference count.**

**No acronym appears in authorial prose**, checked with word boundaries after the reference set
nearly doubled, which is the check that must be re-run after every reference pass.

The isolated build succeeds at 1.62 megabytes with **all 90 equations rendering as display blocks**,
9 tables, 14,291 list items, zero unfilled markers and zero link-definition leakage.

**One inconsistency I introduced and then fixed.** The assembler counted the period through 1999,
inherited from A329 whose programme ran to 2002, while this article states its programme ran to early
2001. The rendered count and the sentence beside it disagreed. Both now use 2001.

---

## The Prediction in the Handoff Was Right and It Is Now Measurable

**The handoff said to expect the opposite documentary problem from A329 and to check rather than
assume.** Checking took one query.

**A329 harvested 4,412 records and exactly one carried the X-32 in its title.** The first A330
harvest returned 620 records from the reports server and **62 of them carried the X-33**, before any
harvest aimed at the vehicle. The final pool holds **60 after deduplication**.

**The cause is institutional and it belongs in the closing article.** A defence competitor is
documented by its manufacturer and its customer. A cooperative agreement with a research agency is
documented by an agency that publishes. **The designation is identical in both cases and the
documentary consequence is not.**

---

## An Identity Fell Out That I Did Not Expect, and It Is the Article

**The lobed tank is the shape a lifting body forces, and I set out to price the penalty.** The
penalty is exactly zero, and that is a theorem rather than a coincidence.

Sizing every wall by its membrane tension, the mass per unit enclosed volume of a two-lobe section
involves the retained arc length, the web height and the centre separation. Those satisfy

    arc x radius + web height x separation = 2 x enclosed area

**identically, at every radius and every separation at which the lobes intersect.** So the mass per
unit volume is twice the wall density times the pressure over the allowable, **which is exactly a
cylinder's value, with the geometry gone.**

**A suspiciously clean factor is normally a defect in the checker and this one is not.** The residual
is zero to machine precision, the verifier reproduces it from an area and an arc length obtained by
numerical quadrature rather than from the closed forms, and it survives twenty thousand randomised
geometries.

**What it means is the article's thesis.** A designer who sizes a conformal tank by membrane stress
finds the shape free and is wrong. **The membrane model accounts for 10.6 percent of the mass of the
tank that was actually built.** The other eighty-nine percent is bending at the junctions, buckling,
minimum gauge and joints, **and the record independently reports that the complex joints the lobed
shape demanded are why the composite tank came out heavier than the aluminium tank that replaced
it.** The derivation predicts what the record says.

---

## The Verdict Does Not Depend on the Failure, Which Is the Uncomfortable Part

**Everyone remembers a tank that came apart on 3 November 1999. The arithmetic that killed the
concept needs none of it.**

Take the tank efficiency the programme demonstrated, **26.83 percent of the hydrogen held**, and
apply it to the vehicle the demonstration existed for. At the required propellant fraction the whole
of VentureStar outside its propellant and payload is 195,683 pounds. **The hydrogen tanks alone come
to 80,205 pounds, or 41.0 percent of that entire allowance.** Even allowing them fifteen percent of
it demands a tank **2.73 times better** than the one built and tested.

**Had the tank passed every test it would still weigh what it weighed.** The article says so plainly
and flags the competing programme-management reading as one the record supports at least as well.

---

## Two Published Numbers Were Convertible Into a Weight Report

**The Government Accountability Office records that the speed objective fell from Mach 15 to Mach
13.8 because projected weight exceeded requirements, and says no more.** The rocket equation converts
that sentence. The velocity given up is 408.4 metres per second, and the burnout mass that would have
reached the original objective is **between 9.9 and 12.6 percent lighter across every plausible
effective specific impulse.**

**An independent route agrees.** The two families of published specification disagree about the empty
mass by 12,000 pounds, or 19.0 percent. **Neither table is wrong. They are snapshots of a vehicle
that was getting heavier**, and the inversion uses neither of them.

---

## A Shared-Library Defect That Had Already Shipped Three Times

**Found by reading the reference list, which remains the only method that has ever worked for this
class.**

**Publishers emit titles wrapped in an escaped title tag rather than in a literal one.** The
tag-stripping rule in `refs.clean` never sees those, and the later rule that removes semicolons
mangles the escaped form into visible junk, **which renders as literal entity text in the link
label.**

**It is present in A328 at twenty instances, in A329 at eleven, and was present in A330 at nine.**
`refs.clean` now decodes entities first, `anchor_stem` routes the title fallback through `clean` so
markup cannot occupy the anchor's two-word window, and `test_lib` has a case. **The suite is now 49
of 49.**

**A330 is clean. A328 and A329 still carry it**, because repairing them means re-running their
assemblers, which is outside a draft pass on A330. **Say the word and I will repair both.**

---

## Open Concerns

**The verdict rests on two reported figures**, a tank mass of 4,600 pounds and a capacity of 29,000
gallons. If either is wrong the verdict moves proportionally. **The only defence available is that
the tank capacity, the propellant load and the engine mixture ratio come from three sources that were
never printed together and imply a tank fill of 94.2 percent**, which is what a cryogenic tank
actually carries. That is corroboration and not proof, and the article says so.

**The claim that the aluminium-lithium replacement tank weighed less than the composite one is
secondary-sourced.** It agrees with the derivation, **and a result that agrees with one's own
analysis deserves more scepticism rather than less.** It is flagged at the point of use and again in
the Source Base.

**The failure investigation is thinly represented in retrievable form.** The primary documentation is
largely presentation material and the retrievable copies are scanned images from which no text can be
extracted. The article states the limit rather than writing around it.

---

## Awaiting Instruction

**A330 has completed three of four passes.** Thirty-four of seventy-two drafted, **none published**.

The next and final pass is the **publication review**.
