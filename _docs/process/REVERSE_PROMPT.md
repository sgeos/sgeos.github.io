# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-10
**Task**: A330 publication review, the fourth and final pass. Committed and **pushed**. **Not
published.**

**Final state: 32,379 lines, 92 display equations, 10,248 reference definitions, 170,821 words**,
with all 10,186 master records cited and none left over. All thirty-four articles remain in
`_drafts/`.

---

## The Contemporary Survey Was Half the Article's Directive and It Was Behind

**Coverage from 2015 onward stood at 2,179 records and 31.3 percent**, having fallen nine points
during the primary pass purely because the period count rose underneath it. **Thirteen clusters held
fewer than twenty-five modern records**, and the worst of them was carrying an argument.

**A harvest took the contemporary half to 5,407 records and 53.1 percent, with 2,845 published from
2022 onward.** The clusters that moved most were the ones the article's own reasoning depends on,
being reusability and launch economics, guidance and powered descent, cryogenic insulation,
manufacturing scale-up, and the buckling literature.

---

## The Strongest Thing This Pass Found Was Hiding in the Article's Own Sensitivity Table

**The buckling section sweeps a knockdown factor and calls it its least certain assumption. That
factor comes from a monograph published in 1968, and replacing it has been an active subject ever
since.** The 1968 values are deliberately conservative lower bounds, and **conservatism in a buckling
allowable is paid directly in structural mass.**

**What that conservatism is worth on this vehicle depends entirely on whether the wall is a sandwich,
and the difference between the two answers is a factor of 38.1.** Moving the knockdown from 0.2 to
0.5 saves **103 pounds** on the composite sandwich, where stiffness is bought with core separation,
and **3,928 pounds on a metal monocoque of the same geometry**, where the thickness is the stiffness.

**That second figure is 5.24 percent of the burnout mass and 52.8 percent of the entire weight growth
that cost the Mach 15 objective.**

**So a sandwich is very nearly insulated from the conservatism of a buckling allowable and a metal
monocoque is not**, which is a second and independent reason the architecture was right and is not
the reason usually given for it. It holds generally rather than at one point, since **a parity
sandwich is lighter than the metal monocoque at every knockdown between one twentieth and one,
tested over twenty thousand values.**

**The uncomfortable corollary is in the article too.** A programme that needed mass, and that cut its
own speed objective because it could not find any, was sizing structure against a factor known to be
conservative. Whether better factors were available in the 1990s is not something the article can
establish, **and the modern literature is evidence that the problem was open rather than that the
answer existed.**

---

## A Second Contemporary Thread, and One Cluster That Is Empty for a Reason

**The aerospike came back through manufacture rather than through aerodynamics.** A plug engine is a
great many small chambers and a contoured ramp, and what made it expensive was building it. Additive
manufacturing removed most of that, which is why the architecture reappeared on small launch vehicles
rather than large ones. **That is a different kind of afterlife from the tank's**, which came back
because the problem was understood better.

**The vehicle's own cluster holds zero contemporary records and the article now says why.** Sixty
records carry the X-33 designation and every one predates 2002. **A cancelled programme stops
generating literature under its own name**, which is the mirror image of A329's finding that a losing
competitor stops generating it the moment it loses.

---

## The Count-Versus-Fraction Trap Caught This Article at Both Ends, in Consecutive Passes

| | After drafting | After the primary pass | After the contemporary pass |
|---|---|---|---|
| Research references cited | 5,318 | 6,958 | 10,186 |
| Period through 2001 | 2,488, 46.8% | 4,018, 57.7% | **4,018, 39.4%** |
| Contemporary 2015 onward | 2,156, 40.5% | **2,179, 31.3%** | 5,407, 53.1% |
| Published 2022 onward | 1,141, 21.5% | 1,145, 16.5% | 2,845, 27.9% |
| Report literature | 1,229, 23.1% | 1,692, 24.3% | **1,692, 16.6%** |

**The primary pass raised the contemporary count by twenty-three and dropped its fraction by nine
points. The contemporary pass left the period count completely unmoved and dropped its fraction by
eighteen.** Nothing was ever removed. **The report literature is the clearest case of all**, holding
at exactly 1,692 records while its share fell from 24.3 percent to 16.6.

The article carries all three columns and says which number moved in each pass.

---

## A Shared-Library Defect the Sweep Exposed

**The citation sweep reported one mismatch and the citation was correct.** The record is a
Chinese-language paper on leakage detection in a composite low-temperature tank, correctly cited,
correctly rendered, and correctly registered.

**The cause is that an anchor stem is only a surname when an author survived ASCII folding.** Where
every author is in a non-Latin script, `refs.anchor_stem` falls back to the title, so the stem
carries no surname at all, **and `citations.verify_doi` was comparing that title fragment against a
registry author who also folds to nothing.** The comparison could never succeed, so every
title-fallback anchor was destined to report a defect.

**The honest treatment is to decline the check rather than to fail it.** `verify_doi` now reports
`author_checked` as false where no registry author survives folding, and the check still bites where
it can run, confirmed against a deliberately bogus surname. `test_lib` has a case and the suite is
**50 of 50**.

---

## One Thing Deliberately Left Alone

**Four records of nanoscale shell mechanics reached the buckling cluster**, using nonlocal elasticity
on nanobeams and nanotubes, which is a different theory from the one the article uses. **They were
left in.** A pattern narrow enough to catch them also catches carbon-nanotube-reinforced ablative
thermal protection material, which is legitimate aerospace work and is on subject. **Four records in
ten thousand one hundred and eighty-six is below the level at which a filter does more good than
harm**, and the widening-has-a-price rule cuts both ways.

---

## What the Review Checked

**Prose style is clean.** Zero em dashes, en dashes, contractions, ellipses and capital emphasis. The
only semicolon, colon and parenthetical in the whole article are the `console.log` debug tag and the
table-of-contents marker, which are the permitted locations. Link text was included as prose in every
scan.

**No acronym appears in authorial prose at all**, checked with word boundaries after the reference set
grew past ten thousand.

**Reference integrity is exact.** 10,248 definitions, zero duplicates, zero undefined uses, zero
orphans, and **zero punctuation defects across 20,434 visible entries.**

**Mathematics.** 92 display equations, each on one source line, zero split equations, zero wrapped
inline spans, zero bold spans crossing a line, an even delimiter count, and balanced braces and
delimiters in every one. `verify.py` reports **110 of 110** with **19 agreements between independent
routes**.

**The citation sweep is clean and this time there are no mismatches at all.** All **764 NTRS fixed
identifiers resolved**, **600 of 8,427 sampled journal DOIs** registry-matched with **zero
mismatches**, **160 of 998 sampled DTIC DOIs** likewise, all 7 books and 19 curated URLs retrieved,
and **zero search-endpoint citations**. **HARD FAILURES: 0.** The single mismatch the previous sweep
reported was the checker defect described above, and it does not recur.

**Structure.** All twelve genre sections present and in order, all three series sections present, and
the Source Base immediately before the Epistemic State.

**Diction.** One phrase sits above the peer median and inside the peer maximum. The two most frequent
content words are **tank at 8.48 per thousand and mass at 6.73**, which are the article's subject and
are left alone.

**The isolated build succeeds at 2.31 megabytes** with all 92 equations rendering as display blocks,
16 sections, 67 subsections, 10 tables, 20,734 list items, zero unfilled markers and zero
link-definition leakage.

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

**A330 is complete through all four passes.** Thirty-four of seventy-two drafted, **none published**.

The next article to draft is **A331, the Orbital Sciences X-34**, editorial date 2025-11-09, series
index 35. **It was cancelled in the same decision as the X-33 and by the same reasoning**, so the
programme-management reading this article treats as a competing account is the one A331 will have to
take seriously. The X-34 flew no powered flights either, but unlike the X-33 it was largely complete
and two airframes survived in storage for years, **which makes it a third kind of never-flew** to set
beside the X-27's absence of demand and the X-30's absence of knowledge.
