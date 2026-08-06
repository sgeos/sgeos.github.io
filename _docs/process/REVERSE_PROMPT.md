# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-05
**Task**: A304 publication review, the fourth and final pass. Committed and **pushed**. **Not
published.** All eight articles in the series remain in `_drafts/`.

---

## A Duplicated Clause the Equation Pass Left Behind

The article contained this, in consecutive sentences:

> ...which is why the whole subject exists and why **the flame must be anchored rather than left to
> propagate**. **The flame must therefore be anchored by a recirculation zone** rather than propagating
> freely...

The same statement twice. My equation pass inserted the Damköhler paragraph ending in that clause,
immediately before an existing sentence that already said it.

**This is the A297 defect class and every automated check passed it.** The anchor integrity check, the
seam scan, the unbalanced-delimiter scan, `_verify.py`, and the build all saw nothing. It surfaced
only because I was reading `rather than` occurrences for the diction check and two of them turned out
to be the same sentence written twice. That is the third time in this series that a defect of this
kind has been found by a check aimed at something else.

---

## Contemporary Coverage

45 journal articles added from a 40-query Crossref sweep, taking contemporary references from 62 to
**107** and from 28.1 to **40.2 percent of dated references**. The absolute count now matches A302 at
109 and A303 at 105. The percentage is higher because this article carries fewer dated references
overall, and it is above the range the earlier articles settled at, which is deliberate under the
directive.

**Selection was made by DOI directly from the harvest records rather than by transcription**, which is
the rule I adopted after the draft pass hand-constructed nineteen identifiers that resolved to
unrelated papers. All 45 verified with zero flagged at a 0.85 title-similarity threshold, against the
0.5 threshold used previously.

The strongest additions land on the keystone rather than beside it. **Optimal experimental design is a
named modern discipline**, and [Zhong et al 2026] on the goal-oriented Bayesian case, [Attia et al
2025] on robust A-optimal placement, and [Coons and Huan 2025] on expected information gain across
fidelities all formalize exactly the statement this article makes about the X-7, which is that the
value of an observation depends on where it is taken and that the most valuable places are the ones a
cautious programme excludes. The article's central argument now has a live literature standing behind
it rather than one textbook variance relation.

---

## Smaller Defects

**The fuel heating value appeared in an equation and again in prose without ever being defined.** It
is now glossed at first use.

**Liquid hydrogen and kerosene densities were given as subscripts LH2 and RP**, the second of which is
not glossed anywhere in the article and would be opaque to a reader outside propulsion. Both are now
spelled out.

**Three en-dashes entered with contemporary titles.** I corrected them at the master-table level
rather than in the article, so the fix survives the next regeneration of the reference section. One
parenthetical report designation in a title went the same way.

`rather than` measured 41 uses at 4.4 per thousand body words, above A302 at 3.7 and A303 at 2.9.
Fourteen rotations brought it to 30 at 3.03.

---

## Verification

**All 53 worked numerical values re-derived independently, none disagreeing beyond four percent.**

358 references with zero undefined, zero orphaned, and zero duplicate URLs. All 185 meaningful-404
URLs at 200. All 107 DOIs Crossref-resolved on author and title. `_verify.py` at the 0-error
21-warning corpus baseline. Zero contractions, em-dashes, en-dashes, prose colons, prose semicolons,
or prose parentheticals. Zero doubled words, zero display-math seam defects. Bullets and definitions
sorted, acronyms spelled out, genre order conforming. Isolated build succeeding with 94 rendered
display blocks and Part 8 navigation.

**All three densities are inside band**, which is the first article in the series to finish that way
without an overage being argued for.

---

## State

**Pushed.** Nothing in this series is published, and the deploy workflow builds without `--drafts`, so
the push is safe. **The publication-order dependency is eight deep.**

Eight articles are complete of seventy-two. **Categories remain undecided** at
`aerospace history engineering`, still my assumption, eight articles deep and raised repeatedly. A305
is the Aerojet X-8, the Aerobee sounding rocket, where the question is what a designation means when
the vehicle is not an aircraft at all.
