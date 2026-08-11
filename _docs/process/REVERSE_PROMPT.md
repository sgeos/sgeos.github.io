# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-11
**Task**: A333 primary-reference review, the third of four passes. **Committed, not pushed.** **Not
published.**

**References 3,467 to 5,063 definitions and 3,352 to 4,948 cited**, with all 4,948 master records cited
and none left over. The article moved from 11,229 to 16,068 lines and from 60,869 to 85,923 words.
**Equations unchanged at 28.**

---

## Both Counts Rose and the Fractions Moved Apart

| | After drafting | After this pass |
|---|---|---|
| Cited records | 3,352 | **4,948** |
| Period count, through 2001 | 1,566 | **2,422** |
| Period fraction | 46.7 percent | **48.9 percent** |
| Contemporary count, 2015 onward | 1,567 | **2,214** |
| Contemporary fraction | 46.7 percent | **44.7 percent** |

**The period base grew by 856 records and gained 2.2 points of share. The contemporary base grew by 647
and lost 2.0.** Nothing was removed from either. **The denominator moved**, which is the whole reason
this series prints the count beside the fraction.

---

## The Promotion Rule, Sixteenth Article Running

| Newly promoted subject | Before | After |
|---|---|---|
| **Phase margin and delay margin** | **0** | **142** |
| **Specific fuel consumption and engine performance** | **0** | **161** |
| Munk moment and slender-body theory | 1 | 111 |
| Turn performance and corner speed | 4 | 10 |

**Phase margin at zero was the worst instance this series has produced**, because it carried the
article's headline result. The correction was vocabulary. The article says delay budget; the control
literature says **gain and phase margin, time delay margin and robustness**, and the aeronautical half
says **equivalent time delay and pilot-induced oscillation criteria**.

**Turn performance stays thin at 10 and is reported as thin rather than padded.** It is peripheral to
the article, occupying one subsection.

---

## The Two Keystone Documents, Hunted by Name and Found

The draft derived the Munk moment and cited nobody for it. **It now rests on the two papers that
established it.**

- **Munk 1924**, the aerodynamic forces on airship hulls, which is the potential-flow result.
- **Allen and Perkins 1951**, a study of effects of viscosity on flow over slender inclined bodies of
  revolution, which is the correction that makes it usable at real angles of attack.

**The relation this article displays is older than aeronautical stability and control as a
discipline**, and the article now says so with the sources beside it.

---

## Three Defects in My Own Search, and All Three Fail Silently

**This pass exposed more tooling faults than any before it, and the common property is that none of
them produces a wrong answer. All three produce a smaller one**, which reads as a thin literature
rather than as a bug, and that is exactly why they survive passes.

**The anchor gate rejected the article's oldest primary source outright.** The 1951 title contains no
aircraft, no aerodynamics and no design, because it is a paper about **viscosity, flow, slender bodies
and revolution**. A gate built from vehicle vocabulary refused the single best source for the relation
the article displays. **The gate now admits the vocabulary of the physics as well as that of the
machine**, and selection went from 4,772 kept to 5,050 on that change alone.

**A plural boundary refused Munk's paper.** It is titled the aerodynamic forces on airship **hulls**,
and a pattern written for `hull` declined it. **This is the third time in this project that a plural
has done exactly this**, after `installation effects` in A332 and the historical `Diffusers` and `area
rules`.

**A spelling variant halved a cluster.** British manoeuvrability and American maneuverability are
different strings and my pattern matched neither reliably.

---

## A Fourth Fault, Which Is a Sequencing Trap Rather Than a Pattern

**Widening the anchor gate after the reports-server detail pass leaves the newly admitted records
without metadata, so they never reach the master set at all.** The 1951 paper passed selection, showed
as kept, and was still absent from the article, because the detail pass had already cached only the
records that passed the older gate.

**Nothing reported an error.** The record was simply not there. **Re-run the detail pass after any
change to the anchor gate or the cluster patterns**, which is now the rule, and it recovered eight
records here including the one that mattered.

---

## Verification

- `python3 tmp/a333/verify.py` **99 of 99**, unchanged, since this pass added no arithmetic.
- `python3 _verify.py` **0 errors, 21 warnings**, from the repository root.
- `python3 tmp/errata/check_any.py` **0 failures, 0 warnings**.
- **All 4,948 master records cited, none left over.**
- **Reference scan clean across 10,076 visible entries**, zero punctuation defects, zero duplicate,
  undefined or orphaned definitions.
- **80 of 80 sampled DOIs verify against the Crossref registry** with none declining the author check,
  and **326 of 326 NTRS identifiers resolve.**
- **Isolated 37-article build exit 0**, page 1.17 MB, **28 open and 28 close display-math delimiters**,
  zero unexpanded markers, zero nested empty lists, zero blockquotes.

---

## Next

**A333 pass four**, the publication review, on your prompt. **It also asks for a push.** Contemporary
coverage stands at 2,214 records and 44.7 percent, so I expect that pass to be prose, a contemporary
harvest for the thin clusters, the full sweep and the final structural check.
