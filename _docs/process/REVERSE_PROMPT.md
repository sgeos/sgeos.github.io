# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A314 primary-reference review, the third of four passes. Committed, **not pushed**, not
published. References rose from **71 to 277**.

---

## The Audit Found a Supply Problem, Not a Selection Problem

This is a different defect from the one A313's audit found, and worth distinguishing.

**The pool held only twenty records from before 1960, for a vehicle that flew in 1956 and 1957.** The
first harvest's period sweep used a 1985 cutoff, and 1960s and 1970s material crowded out the
contemporaneous literature entirely. A second sweep with a **1960 cutoff** took pre-1960 supply from 20
to **157**.

**The documents the X-17's own engineers would have been reading are the most valuable primary material
this article can have, and they had to be asked for specifically.** A313's lesson was that a harvest
must ask for the middle era. This one is that it must also ask for the *earliest* era with a cutoff
tight enough to isolate it. The two are related and neither implies the other.

Two thin topics were filled at the same time. Refractory materials and radiative cooling stood at six
records, which the equation pass had made load-bearing by arguing that ablation is mandatory through a
Stefan-Boltzmann test on every refractory material there is, and re-entry vehicle dynamics stood at
seven.

**Of 252 research references, 214 or 84.9 percent are primary and period material.** Era distribution
is 33, 94, 43, 44, and 38 across the five bands.

---

## Sixteen Rejected by Reading, in a New Vocabulary

The failure mode is the one A313 recorded, arriving in different words.

| Search term | What it returned |
|---|---|
| refractory | furnace fillers; mullitization of alumina raw material; **silicon carbide power converters**; near-infrared reflectance of **rocks** for asteroid science |
| high temperature air | a pneumatic **air motor** |
| chemical kinetics | oxidation of **n-butane**; chemiluminescence in propane-butane flames |
| heat flux | **microchannel heat sinks** for electronics cooling |

The refractory bucket was rewritten to require a materials term **and** a protection, structural, or
property context, and each rejection carries a recorded reason.

**An asymmetry worth noting.** A second automated relevance scan run after insertion flagged seven more
citations. **All seven were false positives of the scan's own keyword list** — a ceramic-heated tunnel,
high-emissivity coatings, expansion-tube shot-to-shot variation, and others squarely on subject. The
reading step catches real defects. The automated step generates noise in both directions and is useful
only as a prompt to look.

---

## Where the Citations Went

Thirteen insertion points, each supporting a specific claim rather than listing. The facilities
discussion now says plainly that **every ground facility is a partial simulation too**, which is worth
establishing before criticising the X-17 for being one. The high-temperature air properties are named as
**the single largest supporting literature the article rests on**, because every quantity in the heating
calculation depends on them and none is constant. And the re-entry dynamics literature is tied to the
observation that **a vehicle which tips over and fires has an attitude error at ignition by
construction**.

---

## Verification

**56 draft-pass and 44 equation-pass re-derivations all still reproducing**, zero disagreements. 277
reference definitions, 260 external URLs, zero duplicates or orphans. URL sweep: 152 plain 200s, 61
publisher 403s, 4 202s, 1 302, and **42 DTIC DOIs verified through the Crossref registry** with matching
titles.

`_verify.py` at the 0-error 21-warning corpus baseline. Zero style violations. Isolated build passing
with 47 of 47 display blocks rendered, 7 of 7 tables, and Part 18 navigation.

---

## State

**835 lines, 47 display equations, 277 references, 8,301 body words.**

**References are inside the full-aircraft band of 250 to 380.** Lines sit 465 below its floor and
equations 43 below, so the intermediate-class question stands on those two measures exactly as it did
for A313.

**Contemporary references at 38 of 252, or 15.1 percent, are low by series standards.** That is expected
at this point in the rhythm and closing it is the publication review's work, as it was on A310, A312 and
A313.

**Committed, not pushed.** Nothing in the series is published. Categories remain undecided, and the
fourth-class question is now open across two articles and four passes.
