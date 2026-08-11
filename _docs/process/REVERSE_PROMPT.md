# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-10
**Task**: A330, the Lockheed Martin X-33, drafted. **The draft pass only.** Committed, **not pushed**,
**not published.**

**State after the draft pass: 17,379 lines, 51 display equations, 5,392 reference definitions, 92,916
words**, with all 5,332 master records cited and none left over. Thirty-four of seventy-two drafted,
all still in `_drafts/`.

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

## What the Pass Measured

| | Value |
|---|---|
| Lines | 17,379 |
| Display equations | 51 |
| Reference definitions | 5,392 |
| Words | 92,916 |
| Master records cited | 5,332 of 5,332, none left over |
| Period through 2001 | 2,493, or 46.7 percent |
| Contemporary, 2015 onward | 2,165, or 40.6 percent |

**Both halves are healthy and both were measured after the harvest rather than before**, which is the
rule A328 and A329 earned in opposite directions.

**The citation sweep is clean.** All **616 NTRS fixed identifiers resolved**, **600 of 4,098 sampled
journal DOIs** registered in the Crossref registry with author and year matching and **zero
mismatches**, **160 of 619 sampled DTIC DOIs** likewise, all 7 books and all 19 curated URLs
retrieved, and **zero search-endpoint citations**. **HARD FAILURES: 0.** Sample sizes are stated
rather than hidden, because saying "sampled" without saying how many reads as full coverage.

**Verification.** `verify.py` reports **63 of 63** with **13 agreements between independent routes**,
reaching the rocket equation by integrating the mass flow, the lobe geometry by quadrature and chord
summation, the nozzle area ratio by scanning and against the exact sonic condition, and the weight
inversion by running it forward. `check_any.py` passes. `_verify.py` holds the baseline at **0 errors
and 21 warnings**. `test_lib.py` is **49 of 49**. The isolated build succeeds with all thirty-four
series articles staged as posts.

**Three defects were caught before commit.** A prose parenthetical inside an inline arc-cosine, fixed
by writing the argument as a fraction. A doubled word inside a verbatim citation title, being a
report on an on-board experiment, which is correct English that a case-insensitive checker cannot
accept, **so the record was dropped rather than the checker weakened**, which is the third instance in
three articles. And an inline math span that reflow split across a line, moved into a display of its
own.

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

**A330 has completed the draft pass only.** Thirty-four of seventy-two drafted, **none published**.

The next pass due is the **equation-density review**. Fifty-one equations is low for this series and
I expect that review to find a good deal, particularly around the buckling and bending terms the
identity promotes from background to keystone, **which the article currently names and does not
compute.**
