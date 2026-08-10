# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-10
**Task**: A327 publication review, the fourth and final pass. Committed and **pushed**. **Not
published.**

**Final state: 10,596 lines, 54 display equations, 3,118 reference definitions, 58,563 words.** All
thirty-one articles in the series remain in `_drafts/`.

---

## The Contemporary Survey

**Contemporary coverage 753 to 1,784 references, or 37.1 to 58.9 percent.** A deliberate harvest of 60
Crossref queries under a 2015 filter and 10 NTRS queries took the modern pool from 1,089 to 2,701 and
the master from 2,028 to 3,062 records, **every one of which is now cited**.

**Seven survey subsections were added for subjects that were not fields in 1993**, being
detonation-based propulsion, precooled engines, machine learning applied to hypersonic prediction,
uncertainty quantification, additive manufacture of cooled structures, aerothermoelasticity, and the
economics of reusable launch.

---

## The Most Important Development Is Not Aerodynamic

**Reusable rocket first stages lowered the cost of access to space substantially, without
air-breathing.** That was the X-30's entire justification.

**The argument was answered by a different technology, and the physics the X-30 could not settle is
exactly where it was left.** That seemed worth saying plainly in the survey, because it is the reason
the question has not been reopened rather than any technical verdict on it.

**Two of the new subjects bear directly on the article's own arithmetic.** Detonation approaches
constant-volume heat release and so extracts more work from the same chemical energy, which attacks
precisely the difficulty that the fuel is a small perturbation on a very large stream. And uncertainty
quantification is the discipline that answers the twenty-fold amplification, since **a twenty-fold
amplification is not an argument against computing but an argument for computing the amplification.**

---

## The Count-Versus-Fraction Trap, Both Ways

**At the primary pass the primary count rose** from 940 to 1,304 while its fraction fell from 71.3 to
64.3 percent.

**At this pass the reverse.** The period count sits essentially unchanged at 1,103 while its fraction
falls, because a further thousand contemporary sources arrived underneath it.

**Nothing was removed at any point**, and the Source Base records both movements.

---

## Publication Checks

Prose style clean, with **zero em dashes, zero en dashes, zero contractions, zero prose parentheticals,
zero prose colons and zero prose semicolons** in the body. Every colon found traces to YAML front
matter.

**No acronyms appear in authorial prose at all.** The only all-capital tokens are the unit symbols MW
and MJ, and NASA appears solely inside verbatim citation titles, which are exempt.

**Zero constructions above the corpus maximum.**

---

## Final Verification

98 numerical checks passing unchanged, with all article-facing values confirmed present in the draft.
`_lib/test_lib.py` at 46 of 46. Reference integrity at 3,118 with zero undefined, orphaned or
duplicate URLs, and **zero search-endpoint citations**.

**The final set was swept with zero hard failures**, including all 435 NTRS identifiers, 240 of 240
sampled journal DOIs against 2,305, 80 of 80 sampled DTIC DOIs against 324, and all books and curated
URLs.

`_verify.py` at the 21-warning baseline, check_any clean, and a 31-article isolated build rendering
**all 54 equations across 17 sections, 55 subsections and 19 tables**.

---

## Awaiting Instruction

**A327 is complete through all four passes.** Thirty-one of seventy-two drafted, **none published**.

The next article to draft is **A328, the Rockwell-MBB X-31**, editorial date 2025-11-06, series index
32. **It inverts this one again.** The X-31 was built, two were flown, and it answered its question in
the most direct way available, by flying manoeuvres no conventional aircraft could perform and then
being flown against conventional aircraft to see whether that mattered.
