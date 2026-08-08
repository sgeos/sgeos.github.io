# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-08
**Task**: A313 primary-reference review, the third of four passes. Committed, **not pushed**, not
published. References rose from **85 to 315**.

---

## The Audit Found a Missing Era, Not a Missing Subject

The pass opened with a coverage audit rather than a selection, per the A310 ordering rule. What it
found was not what I expected.

The draft cited **35 documents from before 1960**, **22 from 2019 onward**, and **three from the whole
of 1960 to 2018** — against 546 pool records in that span.

That shape makes a claim, and the claim is false. It implies the X-16's question was asked in the
1950s, abandoned, and revived recently. **It was worked continuously**, most visibly by the
high-altitude long-endurance programmes of the 1980s and 1990s, which asked exactly Bell's question
with better tools. Condor, Perseus, Pathfinder and their airfoil and sizing literature sit directly
between the two clusters the draft cited.

**The correction is to the article's implicit history rather than to its arithmetic.**

| Era | Before | After |
|---|---|---|
| pre-1960 | 35 | 69 |
| 1960–79 | 3 | 61 |
| 1980–99 | 0 | 56 |
| 2000–18 | 0 | 47 |
| 2019+ | 22 | 57 |

A second harvest aimed at that era, and at one genuinely thin topic — airspeed measurement at low
dynamic pressure, which the equation pass made load-bearing by distinguishing true from equivalent
airspeed — took the pool from 947 to about 1,400 records and the master from 871 to **1,468 entries
with zero anchor drift** on rebuild.

---

## Of 290 Research Citations, 233 Are Primary

**80.3 percent primary and period material**, which is what the pass was asked for. Selection was by
topic *and* era rather than by relevance score, because picking the best-scoring records regardless of
date would have deepened the existing concentration and left the middle empty again.

---

## Three Classes of Selection Defect, All Caught by Reading

This is the part worth recording, because a rule found none of them.

**A substring match.** The pattern `ram` matched inside `fRAMework` and pulled a paper on piezoelectric
morphing wings into the inlet-recovery bucket. Short patterns now carry word boundaries.

**Topical false positives.** `turbojet` and `engine` matched a run of 1960 reports on **nuclear**
turbojet powerplants, which share vocabulary with this subject and nothing else. `fatigue` matched
**crew** fatigue rather than structural fatigue, twice. An exclusion list and a structural-context
requirement now reject 35 matches.

**Records that survived both and were still wrong.** Fifteen dropped by hand before insertion,
including three copies of a mammography paper. Then **three more removed after insertion**, when a
title scan of everything cited found a paper on robust localisation for wireless sensor networks, one
on inductive arrays for unexploded ordnance detection, and one on **charge-coupled device spectra of
stars in globular clusters**. All three had matched on the word *resolution*.

**A title regex is not a substitute for looking**, and the globular clusters paper is the cleanest
illustration of it this series has produced.

---

## What Was Added Beyond Citations

Two new subsections where the material justified one rather than a citation list.

**The buffet boundary is a measured surface and not a number.** Treating it as a constant is a
convenience the article adopts and should not defend. It was being measured in flight at exactly the
time the X-16 was designed, and onset prediction is still an open computational problem, which is why
the single assumed value carries the sensitivity it does.

**The wing is flexible enough that its shape is a variable.** This is now stated as **the largest
unquantifiable risk in the design**. Every aerodynamic estimate in the article assumes a rigid wing at
its drawn shape, no stiffness distribution survives, and whether the difference was small or fatal is
not recoverable.

A third, in the contemporary section, states plainly that the question did not lapse between 1956 and
the present.

---

## Verification

**83 draft-pass and 74 equation-pass re-derivations all still reproducing.** 315 reference definitions,
299 external URLs, zero duplicates, zero orphans. URL sweep: **181 plain 200s, 65 publisher 403s, 2
202s, and 46 DTIC DOIs verified through the Crossref registry** with titles matching the prose.

`_verify.py` at the 0-error 21-warning corpus baseline. Zero style violations. Isolated build passing
with 72 of 72 display blocks rendered, 9 of 9 tables, and Part 17 navigation.

---

## State

**1,016 lines, 72 display equations, 315 references, 10,940 body words.**

**References are now inside the full-aircraft band of 250 to 380.** Lines at 1,016 sit 284 below its
floor and equations at 72 sit 18 below, so **the intermediate-class question narrows to those two
measures** rather than all three.

**Contemporary references at 57 sit below the absolute range this series has held since A301.** That is
expected at this point in the rhythm and closing it is properly the publication review's work, as it
was on A310 and A312.

**Committed, not pushed.** Nothing in the series is published. Categories remain undecided at
`aerospace history engineering`, seventeen articles deep.
