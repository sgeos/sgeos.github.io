# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-11
**Task**: A333 publication review, the fourth and final pass. Committed and **pushed**. **Not
published.**

**Final state: 20,991 lines, 28 display equations, 6,696 reference definitions, 111,381 words**, with
all 6,581 master records cited and none left over. **All thirty-seven articles remain in `_drafts/`.**

---

## The Contemporary Survey

Coverage stood at 2,214 records and 44.7 percent, with ten clusters under forty modern records and two
of them carrying arguments. **A harvest took it to 3,766 and 57.2 percent, with 1,623 published from
2022 onward.**

**The worst gap was the keystone.** Scaling and similitude held **ten** modern records while the
article claims that dynamically scaled subscale flight testing went from a specialist technique to a
routine one. **A claim about the present needs the present literature behind it**, and it now has 46.

**The most useful find is that the article's Reynolds penalty has a modern name and a large
literature.** What the period called scale effects the present calls **low Reynolds number
aerodynamics**, a field that grew because small unmanned aircraft made the regime commercially
important. That cluster went from 38 modern records to 259.

**And the placement is worth stating.** At 8.81 million on the mean chord the X-36 sits **above** the
range where that literature concentrates, **so the penalty this article computes is real and the model
is not in the difficult part of the curve.** That is a better answer than either dismissing the penalty
or being frightened of it.

---

## The Count-Versus-Fraction Trap, in Its Classic Form

| | Draft | Primary pass | Publication pass |
|---|---|---|---|
| Cited records | 3,352 | 4,948 | **6,581** |
| Period count | 1,566 | 2,422 | **2,461** |
| Period fraction | 46.7 | 48.9 | **37.4 percent** |
| Contemporary count | 1,567 | 2,214 | **3,766** |
| Contemporary fraction | 46.7 | 44.7 | **57.2 percent** |

**The primary pass raised the period count by 856 and its share by 2.2 points. This pass raised the
period count again, by 39, while its fraction fell 11.5 points.** Nothing was removed at any stage.
**The period base never shrank; the contemporary survey grew faster**, which is the directive working.
All three columns are in the article rather than the last one.

---

## Two Stale Claims the Pass Caught, and One Was Mine Twice

**The equation pass withdrew the claim that the split ailerons were margin rather than necessity,
because the drag increment that decides it is unpublished and the answer flips inside its bracket.
That withdrawal did not reach two other places in the article.** The Epistemic State still asserted it
as close to a deduction, and the Conclusion still carried it as a subordinate clause. **Both are now
corrected to say that public information does not settle it**, while keeping the structural claim that
does not depend on the increment.

**My first correction then broke a different rule.** I wrote that the claim "was claimed in an earlier
form of this article and is withdrawn", which is **drafting history leaking into the article**, a
sentence referring to a revision the reader never saw. **Rewritten to keep the epistemic content and
drop the revision history.**

---

## Diction

**`rather than` stood at 46 occurrences and a rate of 6.95 against a corpus maximum of 6.78.** Reduced
to 35 by varying ten of them. **Zero constructions now exceed the corpus maximum.**

---

## Verification

Every reading below was taken from the repository root, because `_verify.py` resolves its paths
relative to the working directory.

- `python3 _verify.py` **0 errors, 21 warnings**, the baseline.
- `python3 tmp/errata/check_any.py` **0 failures, 0 warnings.** Twelve genre sections and three series
  sections in order, with the Source Base immediately before Epistemic State.
- `python3 _lib/test_lib.py` **54 of 54**.
- `python3 tmp/a333/verify.py` **99 of 99** by an independent verifier that does not import the
  calculation.
- **Prose style clean**: zero em dashes, en dashes, minus signs, contractions, prose colons, curly
  quotes and capitals used for emphasis. **The only semicolon and parentheses in the article are the
  debug tag.**
- **Reference scan clean across 13,342 visible entries**, zero punctuation defects of any kind in link
  text, **zero duplicate, undefined or orphaned definitions**, zero blockquotes.
- **Acronym check re-run after the reference growth.** The authorial spell-out sits at character 5,285
  against a first citation occurrence at 50,837.
- **Sweep clean with zero hard failures**: **650 of 650 sampled DOIs verify against the Crossref
  registry** with 12 honestly declining the author check, **333 of 333 NTRS identifiers resolve**, and
  **79 of 79 curated URLs return OK.**
- **Isolated 37-article build exit 0**, page 1.51 MB, **28 open and 28 close display-math delimiters
  matching the equation count exactly**, zero unexpanded markers, zero nested empty lists, zero
  blockquotes and zero entity junk.
- **Confirmed after pushing** that the article returns 404 while the site root returns 200, which is
  correct because nothing in the series is published.

---

## What Stays Thin and Is Reported Rather Than Padded

**Turn performance holds seven modern records** after a harvest aimed at it. It occupies one
subsection, it is peripheral to the argument, and padding it would be worse than reporting it.

**The vehicle's own cluster holds five records and no modern ones**, which is the fourth instance in
four consecutive articles and the fourth distinct reason. The X-33 and X-34 were cancelled, the X-35
won and never had a trace at all, **and the X-36 ran to completion and produced a technique rather than
a vehicle**, so its contribution is filed under the names of its methods. **Four vehicles, four
reasons, one shape**, and that belongs in the closing article.

---

## Next

**A334, the Boeing X-37**, editorial date 2025-11-12, Part 38 of 72, on your prompt.

**Publication has still never been authorised and the `post_url` interlock is now thirty-seven deep**,
so these articles publish in order or together.
