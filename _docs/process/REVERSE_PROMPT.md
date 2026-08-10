# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-10
**Task**: A326 publication review, the fourth and final pass. Committed and **pushed**. **Not
published.**

**Final state: 14,071 lines, 69 display equations, 4,180 reference definitions, 77,421 words.** All
thirty articles in the series remain in `_drafts/`.

---

## The Contemporary Survey

**Contemporary coverage 856 to 2,381 references, or 33.0 to 58.0 percent.** A harvest of 78 Crossref
queries under a 2015 filter and 15 NTRS queries took the modern pool from 1,047 to 3,290 and the
article's cited set from 2,594 to 4,117.

**Five survey subsections were added for subjects that were not fields in 1984**, being machine
learning applied to aeroelastic and aerodynamic prediction, morphing structures, digital twins and
structural health monitoring, additive manufacture and topology optimisation, and uncertainty
quantification.

**The last of those bears directly on the article's keystone.** The X-29 handled uncertainty in its
divergence boundary with a margin of 2.667, the flight data then showed the real boundary was lower
than predicted, and the margin absorbed the error. **That margin was doing the work a probability
distribution does now.**

The survey was also reordered so the original grouping stays together and the five new subjects follow
behind a bridging heading, rather than being interleaved.

---

## The Count-Versus-Fraction Trap, Both Ways

**At the primary pass the contemporary count ROSE**, from 850 to 856, while its fraction fell eleven
points because four hundred period sources arrived underneath it.

**At this pass the reverse.** The period count sits unchanged at 1,527 while its fraction falls,
because fifteen hundred contemporary sources arrived underneath that.

**Nothing was removed at any point.** A reader watching only the fractions would have seen two
apparent regressions where there were none, and the Source Base now records both movements.

---

## The Price of the New Clusters, Paid Again

**Digital twins and machine learning are cross-disciplinary methods**, so their literatures are
dominated by civil infrastructure and road vehicles. Reading the assembled draft found fourteen
contaminants, including bridge damage assessment, historical building monitoring, railway digital
twins, tall building aerodynamics and an **automotive occupant restraint system**.

**Two words could not be filtered bare and both were tempting.** "Bridge" is a strain-gauge bridge,
and this aircraft carried eighteen of them at every load station. "Building" is the **building-block
approach** to composite certification, which is a term of art the survey itself cites. Both are now
filtered only in an unambiguous civil-structure context. Thirty-four records were dropped.

---

## Two Defects Found by This Review

**One stale value.** The Epistemic State still carried the pre-correction figure of about 47 degrees
for the critical sweepback, which the equation pass had already replaced with the closed-form 48.013.

**One duplicated block.** The Source Base carried a paragraph twice, because the primary-reference
pass inserted a new heading above text it also kept.

**An article that contradicts itself between sections is worse than one that is merely incomplete**,
and both defects were introduced by earlier passes of this same article rather than by the draft.

---

## Publication Checks

Prose style clean, with **zero em dashes, zero en dashes, zero contractions and zero prose
parentheticals**. The only two semicolons are LaTeX medium spaces inside display equations. **Zero
prose colons**, every colon tracing to a verbatim reference title or the table-of-contents marker.

**Zero acronyms unspelled in authorial prose.** NASA, DARPA and NACA are all spelled out before first
abbreviation, and DATCOM appears only inside verbatim document titles, which are exempt.

**Zero constructions above the corpus maximum.** Only two content words exceed five per thousand,
being `wing` at 6.39 and `aircraft` at 6.22, and **both are the article's own subject nouns and are
left alone**.

---

## Final Verification

88 numerical checks passing unchanged, with all article-facing values confirmed present in the draft.
Reference integrity at 4,180 with zero undefined, zero orphaned and zero duplicate URLs, and **zero
search-endpoint citations**.

**The final set was swept with zero hard failures.** All 378 NTRS identifiers resolve, 240 of 240
sampled journal DOIs are registered and matching against 3,139, 80 of 80 sampled DTIC DOIs are
registered against 602, and all 13 books and 19 curated URLs resolve.

`_verify.py` at the 21-warning baseline, check_any clean, `_lib/test_lib.py` at 45 of 45, equation
citation gaps 32 to 27, and a 30-article isolated build rendering **all 69 equations across 17
sections, 55 subsections and 19 tables** with 97 internal series links resolving.

---

## Awaiting Instruction

**A326 is complete through all four passes.** Thirty of seventy-two drafted, **none published**.

The next article to draft is **A327, the Rockwell X-30 and the National Aero-Space Plane**, editorial
date 2025-11-05, series index 31. **It reverses this article again.** The X-29 was built and flew 242
and 120 sorties. The X-30 was never built at all, and asked a larger question than anything else in
this series.
