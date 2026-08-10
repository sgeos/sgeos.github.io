# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-10
**Task**: A327 primary-reference review, the third of four passes. Committed, **not pushed**.

**State: 7,408 lines, 54 display equations, 2,084 reference definitions, 41,972 words.** Thirty-one
articles drafted, all in `_drafts/`, **none published**.

---

## What Moved

**References 1,375 to 2,084 defined and 1,345 to 2,054 cited.** Equations held at 54, measured before
and after. **Primary sources 940 to 1,304**, and the period count 798 to 1,102.

**The primary fraction fell while the primary count rose by a third**, from 71.3 to 64.3 percent,
because the same pass also cited seven hundred contemporary sources that had been harvested and left
unused. Nothing was removed, and the Source Base states both numbers.

---

## Two Causes, and Only One of Them Was Supply

**The first was supply, and the audit said so unambiguously.** For nine of the ten subjects the
equation pass promoted, the cited count equalled the pool count exactly, and **three stood at zero**.
Energy requirements to orbit went from 0 to 4, mass capture 0 to 2, stagnation pressure and structural
load 0 to 8, normal shock and pressure recovery 1 to 16, equivalence ratio 1 to 37, Reynolds and
transition criteria 3 to 53, ignition delay and kinetics 4 to 52, and inlet starting 9 to 50.

**The second was selection, and it was mine.** **Two hundred and forty-nine harvested records were
sitting uncited**, because the article carried a marker for the period half of several clusters and
none for the modern half, and one cluster had no marker at all.

**That is not a research finding. It is a bookkeeping error**, and it is recorded because an article
that harvests a record and then never cites it has done the work and thrown it away. **Every one of
the 2,028 master records is now cited.**

---

## A Library Defect, Found by the Corpus Checker

**A Springer title containing inline LaTeX reached link text.** Truncated for display it left **a
single unbalanced `$$`, which opens a MathJax display block and swallows the rest of the page.**

`refs.clean` stripped HTML, ampersands, brackets and braces, and **not dollars or LaTeX commands**. It
now strips both, and `_lib/test_lib.py` gained a regression test.

**The test was initially appended to the end of that file and never ran.** Discovery is a module-level
loop over `globals()`, so anything defined after it is invisible, and the suite reported 45 of 45 and
looked healthy. **A test that is never collected is worse than no test, because it reads as coverage.**
Moved above the loop, the suite is at **46 of 46**.

---

## Reported Rather Than Padded

**Mass capture returns two records from five targeted queries.** The quantity is discussed **inside**
the inlet literature, which this article cites 268 times, rather than under a heading of its own.

**And one homonym was not predicted.** The energy-to-orbit vocabulary collides with **oceanographic
and meteorological energy budgets**, and eleven of sixteen matching records were internal waves in the
South China Sea, stratospheric budgets and surface energy balance. The anchor gate rejected every one,
which is the gate working.

---

## Verification

98 numerical checks passing unchanged, with all article-facing values confirmed present in the draft.
`_lib/test_lib.py` at 46 of 46. Reference integrity at 2,084 with zero undefined, orphaned or
duplicate URLs, and **zero search-endpoint citations**.

**The full set was swept with zero hard failures**, including all 435 NTRS identifiers, 240 of 240
sampled journal DOIs, 80 of 80 sampled DTIC DOIs, and all books and curated URLs.

`_verify.py` at the 21-warning baseline, check_any clean, zero constructions above the corpus maximum,
equation citation gaps 26 to 20, and a 31-article isolated build rendering all 54 equations across 17
sections and 19 tables.

---

## Awaiting Instruction

**A327 has completed the draft, equation and primary-reference passes.** The publication review
remains.

**Contemporary coverage stands at 753 references and 37.1 percent**, against a standing directive that
these articles serve as a comprehensive survey of the current literature. The contemporary pool was
extended during this pass only as a side effect of citing what was already harvested, so there is
material for a deliberate contemporary harvest.
