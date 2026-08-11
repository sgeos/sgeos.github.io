# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-10
**Task**: A330 equation-density review, the second of four passes. Committed, **not pushed**, **not
published.**

**51 display equations to 90 across 15 edits**, 17,379 to 17,667 lines and 92,916 to 95,132 words.
References unchanged at 5,392 definitions and all 5,332 master records cited.

---

## The Review Found the Gap the Article Had Dug for Itself

**The draft proved that the membrane model prices conformality at exactly nothing, then asserted
that the real cost lives in bending, buckling, minimum gauge and joints, and computed none of them.**
That assertion is the hinge of the whole article and it was carrying no arithmetic at all. A new
subsection now prices what can be priced and reports what cannot.

**BUCKLING GOVERNS, AND THE ARTICLE REACHES THAT BY INVERSION RATHER THAN BY ESTIMATING A LOAD.**
Setting the buckling thickness equal to the membrane thickness and solving for the compressive line
load gives a threshold of **7.54 kilonewtons per metre**. Thrust alone, ignoring inertia,
aerodynamic bending and every ground-handling case, gives **52.7, which is 7.0 times the
threshold.** The conclusion needs the load to clear a bar, not to be known.

**THE FIRST VERSION OF THAT SECTION WAS WRONG IN THE ARTICLE'S FAVOUR AND THE CORRECTION IS IN THE
TEXT.** Internal pressure stabilises a shell, which I had omitted. Including it raises the effective
knockdown from 0.2 to 0.429 and cuts the ratio of buckling thickness to membrane thickness from 2.64
to **1.80**. **The conclusion survives its own correction**, and at a knockdown of one, meaning a
perfect shell, buckling still asks for 1.635 millimetres against 1.384.

**THE FACESHEETS ARE GOVERNED BY MINIMUM GAUGE, WHICH IS A COST NO STRESS CALCULATION CAN SEE.** A
sandwich splits the membrane load between two sheets, so each needs 0.692 millimetres against a
minimum manufacturable 1.000. **Material is carried that no load calls for, and nothing is
overstressed, so nothing objects.**

---

## A Result That Cuts Against the Architecture

**The sandwich saving is narrower than its reputation and I nearly published a table that overstated
it.** Only the row at the core thickness giving equal stiffness is a like-for-like comparison. There
the sandwich is **1.72 times lighter** with the core at 5.7 percent of the wall. At a thirty
millimetre core it is only **1.13 times lighter** and the core has become **37.9 percent of the wall
mass while carrying no membrane load at all**, and beyond **40.6 millimetres the sandwich weighs more
than the solid wall it replaced.**

**The table now says which row compares equals and which do not**, and names the reasons a real tank
takes the thicker core anyway, being local buckling between cells, damage tolerance, handling and the
insulating value of the core.

**Face wrinkling, the mode a sandwich is normally checked against, has a margin of 1.24 and was not
close.** The tank did not fail in any mode the stress analysis owned.

---

## The Mass Build-Up Does Not Close, and That Is the Finding

**Summing the sandwich wall over the tank's surface gives 1,242.2 kilograms against a built tank of
2,086.5, so the build-up explains 59.5 percent and leaves 844.3 kilograms unaccounted.**

**What is missing is exactly the list the identity pointed at**, being the joints between three major
subassemblies, the longerons, the local reinforcement at every penetration, and the doublers a lobe
junction needs to carry bending into its web. **The membrane model saw none of it. This build-up sees
a little over half of what the membrane model missed, and the remainder is the shape.**

---

## Smaller Relations the Draft Used and Did Not Show

**Where the velocity budget comes from.** Orbital speed at two hundred kilometres is **7,784.3 metres
per second** from the centripetal balance, so the assumed 9,300 implies **1,515.7 metres per second**
of gravity, drag and steering, which is **16.3 percent of the whole budget** rather than a rounding
allowance.

**Why a ratio of thrust coefficients is a ratio of specific impulses.** The draft compared thrust
coefficients and reported the answer as a specific-impulse ratio without showing that the
characteristic velocity cancels for one engine compared against itself. It now shows it.

**Thermal contraction, which is the metal tank's version of the same property.** Over the tank's 8.7
metres the composite moves **4.74 millimetres** and aluminium **54.57**, a ratio of **11.5**. **The
property that makes the composite crack is the property that makes it stay still**, so the metal tank
exchanges an internal problem for an external one rather than solving anything.

Also displayed rather than asserted: the separation criterion and its factor of 5.37, the cost-target
factor of ten, the 35.4 percent industry cost growth, the tanks at 12.27 percent of burnout mass, the
94.2 percent tank fill, the 41.0 percent verdict step, and the required-efficiency inversion.

---

## Attribution, Stated Rather Than Faked

**Four relations in the new section are this article's constructions and it now says so**, being the
web tension, the lobe identity, the inversion for the threshold line load, and the mass build-up.
**None is novel physics and none has a source, because none needs one.** The standard results, being
the critical stress, the knockdown, the pressure-stabilisation term, the sandwich stiffness and the
wrinkling correlation, are named as standard and their literature now sits beside them rather than
several hundred lines away.

**Uncited displayed equations fell from 44 to 41** and the remainder are the steps of derivations
whose opening relation is cited, which is the same disposition A329 reached.

---

## Verification

`verify.py` reports **104 of 104** with **18 agreements between independent routes**. The new work is
checked by routes it did not use, namely the orbital speed against Kepler's period and against the
centripetal identity, the threshold line load by scanning rather than by the closed form, the parity
core thickness put forward through the stiffness relation, and the monotonicity of buckling thickness
in the knockdown as a randomised property over twenty thousand trials.

`check_any.py` passes. `_verify.py` holds the baseline at **0 errors and 21 warnings**. `test_lib.py`
is **49 of 49**. The isolated build succeeds and **all 90 equations render as display blocks**, with
zero split equations, zero wrapped inline spans, zero bold spans crossing a line and an even
delimiter count.

**Three values were absent from the text and are now stated in prose as well as in their displays**,
because LaTeX comma spacing writes 7{,}784.3 and a text check cannot find it. That is the fourth
article in which this has happened.

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

**A330 has completed two of four passes.** Thirty-four of seventy-two drafted, **none published**.

The next pass due is the **primary-reference review**. The equation pass promoted buckling, sandwich
mechanics and minimum gauge from background to keystone, **and that promotion has not yet reached the
reference base**, which is the pattern that has held for eleven consecutive articles.
