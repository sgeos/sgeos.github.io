# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-10
**Task**: A324 primary-reference review, the third of four passes. Committed, not pushed, not published.

**References 1,650 to 1,863.** 6,292 to 6,994 lines, 25,265 to 27,738 words, **equations held at 77 and
measured before and after**.

---

## The Numbers, With Both Figures Because Either Alone Misleads

| | Before | After |
|---|---|---|
| Primary count | 963 | **1,176** |
| Primary fraction | 62.2 percent | **66.8 percent** |
| Period count, through 1982 | 718 | **912** |
| Period fraction | 46.4 percent | 51.8 percent |
| Contemporary count, 2015 onward | 595 | **595** |
| Contemporary fraction | 38.4 percent | 33.8 percent |

**The contemporary row is the mirror of the usual warning and it is worth pausing on.** The count did not
move at all. Its fraction fell five points purely because the period base grew underneath it. **Reporting
only the fraction would read as contemporary coverage having been cut, and nothing was cut.** The article
now carries a table giving count and fraction together for all three.

---

## What the Audit Found, Run Before Any Harvesting

Six subjects were thin on primaries, and the pattern in them is the point.

| Subject | Pool | Primary |
|---|---|---|
| energy manoeuvrability | 4 | **0** |
| conical and oblique shocks | 11 | 9 |
| thermal stress | 3 | 3 |
| ram drag and net thrust | 2 | 1 |
| downwash and tail volume | 1 | 1 |
| energy height and climb | 2 | 2 |

**The last four are the equation pass's bill, and the cause was a defect in my selector rather than in
the harvest.** No cluster existed for those subjects when the first two harvests were written, so **every
record about them was being discarded as "no cluster"**. That is the thin-heading rule arriving from the
opposite direction: a heading so thin it did not exist, over a subject the pool partly held.

Six clusters were added and **placed first**, because the cluster matcher returns the first match and a
specific cluster placed after a broad one never sees its own records.

---

## One Widening, and the Homonym It Created in the Same Run

Records such as *Optimum Climb to Height* and *Propulsive efficiency from an energy utilization
standpoint* were being rejected for want of a subject noun my anchor list did not carry, so climb,
takeoff, propulsive and trajectory were admitted.

**That immediately admitted "the propulsive efficiency of single-screw supertankers."** Marine propulsion
shares the entire vocabulary. It is now filtered and recorded in the durable store, along with **energy
height as a term of art in open-channel hydraulics** and **specific energy belonging to batteries**.

**Widening an anchor list has a price, and this time it was paid at the moment of widening rather than
discovered later in the URL sweep.**

---

## Two Subjects Are Genuinely Thin and Are Reported Rather Than Padded

Of 6,518 harvested records, **thirteen carry ram drag, momentum drag or installed performance in their
titles, and seven carry energy height, energy state or minimum time to climb.**

**The subjects are not thin. The headings are.** Ram-drag bookkeeping is settled inside the papers on
inlet additive drag and spillage that the article already cites, because deciding what counts as inlet
drag and what counts as lost thrust is the same accounting question. Energy height is indexed under
trajectory optimisation, and Boyd's own documents were never journal-indexed at all. **The article prints
both counts and says this.**

---

## The Equation Gaps, and Why the Last Step Was Not More Papers

Equations carrying fewer than three citations within reach went **47 of 77, then 36, then 20**.

The first two steps were research references. **The last was not, because the remaining gaps were
textbook identities.** Attaching a period NACA report to $M = V/a$ would raise the count and lower the
scholarship. The standard works were cited at fourteen points instead — Shapiro and Anderson for
compressible flow, Seddon and Goldsmith for intakes, Oates and Mattingly for the thrust equation, Hoerner
and Kuchemann for drag and configuration, Raymer and Nicolai for sizing, Whitford with Stevens and Lewis
for energy manoeuvrability.

The final 20 are numerical evaluations sitting immediately beneath their already-cited defining relation.

---

## Verification

105 numerical checks passing unchanged, with every value still required to appear in the draft.
`_verify.py` at the 21-warning baseline, check_any clean, reference integrity at 1,863 with zero
undefined, zero orphaned and zero duplicate URLs, and a 28-article isolated build with all 77 equations
rendering and 21 intended tables.

**The 213 added references were swept by source type**, since a single check is wrong for three different
kinds of identifier. 40 of 40 NTRS resolve. 60 of 60 sampled Crossref DOIs are registered. 40 of 40
sampled DTIC DOIs are registered, **which is the right check rather than an HTTP request, because those
resolve to a host that refuses automated connections**.

---

## Awaiting Instruction

**A324 has completed three of four passes.** The remaining one is the publication review, which is also
the pass that asks for a push. Nothing is outstanding.
