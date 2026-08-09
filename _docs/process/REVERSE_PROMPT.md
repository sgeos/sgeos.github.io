# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A320 primary-reference review, the third of four passes.
**Committed, not pushed.** Not published.

**References 871 to 2,283. Primary citations from 44.0 to 68.7 percent.** Period sources dated 1975 or
earlier rose from 243 to 983. **2,887 lines, 70 display equations, 16,898 words.** Equations were
measured before and after and did not move.

---

## The Audit Ran First, and It Bit Harder Than in Any Previous Article

**All ten subjects the equation pass promoted were thin. Four were at zero records.**

- the standard atmosphere and scale height — **zero**
- the ballistic coefficient as a design parameter — **zero**
- weight estimation and mass fractions — **zero**
- the speed of sound and the atmospheric temperature profile — **zero**

Three more sat at one or two. **The draft harvest could not have known those relations would come to
exist**, which is exactly why the audit belongs after the equation pass and not before it. A second
harvest of 56 NTRS, 12 DTIC and 14 Crossref queries took the master from 1,834 to 3,055 records and
every one of them now has a base.

---

## The Keystone Itself Was Thin, Which Is Worse

**Crossrange, the subject of the entire article, had eight records in the pool.**

The draft harvest used the period terms of art and they were correct as far as they went. Eight is not a
base for an article that derives the relation, inverts it on a requirement, and inverts it again on a
measurement.

Probing with the era's own wider vocabulary — **roll modulation, lift modulation, maneuvering range,
boost-glide range** — took it to twenty-one and surfaced two papers that should have been there from the
start. **Roll modulation for maximum re-entry lateral range**, from 1965, is the keystone relation by
name. And a 1963 study of **lateral-range and hypersonic lift-to-drag-ratio requirements** states this
article's own argument in its title.

**The pattern was too narrow, not the archive. That is now the third article running.**

---

## Nine New Homonym Families, and One Is Internal to the Discipline

**Nine, which is the most any article in this series has produced, and every one was found by probing or
by reading rather than by anticipation.** Four came out of probing the clusters and five more out of
reading what the URL sweep printed, which is reported further down.

**Ballistic means three different things in this very corpus, and the Defense Technical Information
Center hosts all three, so the venue cannot separate them.** The entry-trajectory sense is the one
wanted. A **ballistic range** is a gun that fires models into still air to study hypersonic flow, which
is a legitimate technique and is **deliberately not filtered**. And **terminal ballistics** means
warheads, fusing, penetration and armour vulnerability. The filter removes exactly five records and I
checked every one of them for over-reach.

**Easy glide is a stage of crystal plasticity**, so a paper on dislocation tangles in aluminium answered
a pattern written for gliding range.

**Lifting equipment is hoists and cranes**, which arrived through "vacuum lifting equipment".

**Host range is microbiology**, and it put a paper on Pseudomonas aeruginosa plasmids into the article's
most important cluster. The keystone now carries its own negative pattern covering ballistic range,
speed range, ramjet and host range, because in that cluster the word range was doing four other jobs.

---

## A Real Technical Gap Was Found in the Unused Pool and Closed

Reading the 582 unused primary records turned up something the article had genuinely got wrong by
omission. **It applies a convective heating correlation and never said why radiation is neglected.**

Shock-layer radiation becomes a significant part of the heat load only above roughly ten kilometres per
second, which is lunar or interplanetary return. PRIME entered at 7.7, so the omission is correct. **But
correct-and-unstated is not the standard**, and the article now says so, with its own twenty-record
cluster and the explicit note that at Apollo's entry speed the correlation used here would not do.

---

## One Tooling Defect Fixed

Authorless records fall back to the first four words of their title for display text. Titles that carry
their own year then produced **"U.S. Standard Atmosphere, 1962 1962"**, which is a doubled word in body
prose, and the style check was right to reject it. `gen_master.py` now suppresses a year that the title
fragment already ends with.

---

## Checks

**Both verifiers still pass unchanged**, at 114 and 104 checks. Nothing in this pass touched a number.

**`_verify.py` at the 21-warning baseline.** `check_any.py` clean across all 24 articles after the
display fix.

**A 24-article isolated build succeeds with all 70 equations rendering as display math.**

**The external sweep covered 2,286 links and confirmed 1,655 of 1,655 DOIs registered in the Crossref
registry, with zero unregistered.** An HTTP 200 does not verify a citation, which is why the DOI half
is checked against the registry rather than against a status code.

**Reading what that sweep printed caught twenty-one wrong-field citations that nothing else would have
found**, and five more homonym families with them. **Reentry in agriculture is the interval before
workers may re-enter a treated field.** Entry in space physics is solar protons entering the
magnetosphere. Thermal resistance, inactivation and injury belong to food microbiology, where recovery
of an organism is also a term of art. **Speed of sound belongs to solutions and acoustics, a homonym
this pass created for itself by adding that query.** And Guidance for Authors is journal front matter
that Crossref indexes as a work, which is not a homonym at all but a record-type defect. The rejection
list is now 416 entries.

---

## What Is Deliberately Still Thin

**Entry guidance sits at about 30 percent primary.** That is not a gap so much as the shape of the
subject. Period entry guidance is a small literature and the modern predictor-corrector work is large,
and the contemporary survey the publication review will expand is supposed to cite the latter heavily.
**I have left it rather than padding the period side to move a ratio.**

Three topics the audit still flags as thin — the ballistic coefficient, the Allen and Eggers solution,
and heating correlations by name — are **artefacts of the audit's own narrow patterns** rather than real
gaps. The audit matches author names and exact phrases; the clusters that actually serve those passages
hold 5, 93 and 19 records respectively.

---

## State

**A320 primary-reference pass complete. Committed, not pushed, not published.**

**Awaiting the publication-review prompt.** The contemporary survey is the remaining large piece, and on
current counts it will need to move contemporary coverage up substantially from 550 of 2,252.

**Still open and unchanged.** The fourth genre class, now nine consecutive articles. The A305 length
offer.
