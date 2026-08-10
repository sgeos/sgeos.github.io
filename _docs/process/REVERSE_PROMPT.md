# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A369 primary-reference review, following the equation-density pass. Committed, **not
pushed**, not published.

**88 references to 111 across seven placement edits.** 1,178 to 1,268 lines, 54 display equations
held.

---

## The Pass Found Six Subjects at Zero

**The promoted-subjects rule has now fired on seven consecutive articles.** An equation pass promotes
subjects, and the reference base has to follow. Seventeen of the fifty-four display equations carried
no citation within nine hundred characters. Most of those are the article's own arithmetic and
legitimately need no source. **Six were real subjects with substantial primary literature and nothing
cited at all.**

**The leverage ratio is the greedy set-cover rule, and the article had not said so.** It writes down
the selection that repeatedly takes the candidate with the greatest newly covered mass per unit cost,
which is exactly the cost-weighted greedy heuristic. Naming it imports the logarithmic approximation
guarantee of Johnson 1974 and Chvatal 1979, sharpened by Slavik 1997 and shown essentially optimal by
Lund and Yannakakis 1994. **It also imports the precise reason that guarantee does not attach here**,
which the supermodularity section already establishes, so the rule is now offered as a heuristic on
stated grounds rather than on none.

**The program-level coverage measure is a series system.** A product over components is the founding
object of reliability theory and the article cited none of it. Esary and Proschan 1963 supplies the
structure. **Birnbaum 1968 supplies something better**, being a component importance measure that
ranks components by the probability the system's functioning turns on that component alone. **That is
the same quantity as a blocking set, computed in a different vocabulary**, which is worth a reader
knowing.

**The clustering coefficient is an overdispersion statistic.** Dean 1992 gives the test. And the
expectation that the departure from independence would be large was not a guess either, since defects
in software are known empirically to concentrate, established by Fenton and Ohlsson 2000 and measured
at scale by Ostrand and Weyuker. **Unimplemented instructions are not defects and the article now says
so explicitly**, along with why the concentration argument transfers anyway.

**Shapley was carrying the whole attribution section alone.** Young 1985 replaces additivity with
monotonicity, which matters here because monotonicity in the marginal gain is what an ordering
argument actually wants. Owen 1972 gives the multilinear extension. **And the sampling estimators went
in at the one place they are genuinely needed rather than where they sound impressive.** Sixty-four
workstream subsets are trivial and the article is right to say so. The same attribution at instruction
granularity is not enumerable, and there the exact value is unavailable rather than merely unattempted.

Rule synthesis and the testing literature's own version of the selection problem were the remaining
two, the latter being the closer parallel. **Suite reduction is set cover and prioritisation is the
ordering variant**, and Wong and colleagues 1995 found that minimising a suite at constant coverage
can reduce fault detection, **which is the same warning this article issues in the opposite
direction**.

---

## The Article's Own Standard, Applied to the Article

**This is the check worth reporting.** The article documents that four of ninety-one digital object
identifiers it supplied from memory resolved to entirely different works, that each would have passed
a reachability check, and that only comparing the resolved title against the claimed title detects it.
**That check had never been run against what the article now carries.**

It has been. **All eighty-six digital object identifiers resolve to the claimed author and year. Zero
defects.** The twenty-three new references were verified before insertion rather than after.

**Three apparent mismatches were my own bug and not the article's.** ASCII folding drops the
diacritics in Bohm, Lovasz, Munafo and Slavik, the last folding to `slavk` through a dotless i.

**The limitation is stated rather than elided.** Matching surname and year cannot catch a same-author
same-year substitution. That is a narrower hole than the one the article describes, but it is a hole.

---

## One CI Failure Caught Before It Could Happen

The word `rather` stood at 66 occurrences for 6.0 per thousand against the verifier's limit of 5.0.
**The verifier scans `_posts/` and not `_drafts/`, so this would have failed on the day the file was
published and not before.** Fifteen occurrences were rewritten to `and not`, and it now stands at 51
for 4.3 per thousand.

---

## Verification

`_verify.py` at the 21-warning baseline with zero errors. Reference integrity at 111 defined and 111
used, zero undefined, zero orphaned, zero duplicate URLs, correct sorting. Prose style clean with zero
em dashes, en dashes, prose colons, prose semicolons or parentheticals beyond the permitted
`console.log` tag, zero unbalanced bold, and all 54 display equations on single lines.

**Zero doubled backslashes, confirmed by grep after my own regex reported eight false positives.**
That trap has hit three consecutive articles in this corpus, so it is checked twice now.

Isolated production build at the 2026-08-06 date succeeds. All 54 equations render as display math
with zero `$$` survivors, 141 resolved reference anchors, zero unresolved links, zero Liquid errors,
six tables, twenty sections and fifteen subsections, series navigation reporting Part 1.

**The article carries no `post_url` tags**, so it has no build-interlock exposure.

The reference base now spans 1906 to 2021 with a median of 1997, and 62 of the 108 dated sources
predate 2000.

---

## Awaiting Instruction

**The publication review is the remaining pass**, and it is the one that authorises a push.

**One question is still open from the import.** The `keleusma_native` series navigation reads Part 1
of 1. Whether siblings are planned affects nothing in the current draft but would change the series
framing if the answer is yes.
