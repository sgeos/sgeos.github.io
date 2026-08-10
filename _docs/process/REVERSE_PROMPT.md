# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A369 equation-density review, following the standards and retarget pass. Committed, **not
pushed**, not published.

**47 display equations to 54 across six edits.** 1,135 to 1,178 lines, 88 references unchanged.

---

## The Equation Pass, and Why It Added Only Seven

**The genre rule is different here and it constrained the pass.** The analytical essay genre states
that essays carry equations **only where a real quantitative relationship exists**, and that token
equations belong to a different genre. **Nothing was added for density.** Every addition is a relation
the prose already named or relied on without showing.

**Submodularity was named as the false theorem the article corrects and never written down**, so a
reader could not see that the whole force of the error is a **reversed inequality**. Both forms now
sit side by side. **And the greedy guarantee it would have bought was invoked by name and never
stated**, which is precisely what let the error pass; it is now given at 0.632, with the note that
supermodularity admits no such bound.

**Three quoted figures are now derived rather than asserted.** The sixty-four corpus passes as two to
the sixth over the workstream powerset. The rule of three from the binomial, the three being the
logarithm of twenty at 2.996. And Amdahl's bound, with the parallel made explicit, since an
instruction that blocks nothing is a term with fraction zero and no quality of implementation raises
it.

**The dispersion claim is now bounded, and the bound turned out to be the best addition.** With 9,318
missing instances over 496 units, **maximal dispersion would block every unit**, giving a gap equal to
the full instruction coverage of 0.8731. The observed 328 blocked units and gap of 0.5344 therefore
sit well inside that extreme, **which is the same fact the clustering coefficient of 5.51 reports by a
completely different route.** The article now has two independent ways of seeing its own result.

Jensen's inequality was used and called a convexity shortcut without being named.

---

## Verification

**13 to 24 checks.** The rule of three is checked against the **exact binomial** rather than quoted.
Amdahl is verified as a **limit** rather than asserted. **The dispersion upper bound is tested as a
property over 20,000 random corpora**, alongside the existing property test that unit coverage can
never exceed instruction coverage.

Prose style clean, all 54 equations on single lines, zero duplicates, zero doubled backslashes.
Isolated build at the 2026-08-06 date with all 54 rendering and zero unresolved links.

**The body was reflowed again after the edits**, since the new anchors had to be rewrapped to the
file's 108-character wrapping. That is now a standing step for this article.

---

## What the Retarget Did Not Do

**It did not simplify the analysis, which is the article's value.** The formal apparatus, the seven
literature traditions, the confidence bounds and the threats to validity are all intact. What changed
is that a reader who has never written a compiler can now get in.

---

## The Opening

**The file led with a single 700-word abstract that named seven literature traditions before it said
what had happened.** It now opens with the two numbers that carry the whole argument.

**A compiler was 87 percent finished. It could not compile two thirds of the programs it was for.**

Both are correct. The first counts instructions, the second counts whole programs, and the gap exists
because **a program needs every instruction it uses, not most of them.** Then the falsified
recommendation, and the instrument that took twenty minutes to build and two seconds to run.

A short section now explains what a compiler backend is and why an ordering question exists at all.
**The seven traditions became a table**, with the point that none of them answers the question stated
once rather than buried in a list.

**Four on-ramps were added ahead of the formal passages.** The most useful is that **a sum forgives a
missing term and a product forgives nothing**, which is the entire reason the two coverage measures
diverge and was previously left for the reader to infer from the notation.

---

## Three Genre Sections the File Arrived Without

**Epistemic State**, sorting the claims into measured, derived, assumed, corrected-during-writing and
not-established. **It names corpus representativeness as the weakest link** and says that a reader who
doubts it should read the ordering as established for the present consumer rather than the eventual
one. It also records that the article's own conclusion about operand type recovery was too broad, since
the capability was later needed by a different workstream at 18 compilation units.

**Out of Scope** and **Conclusion**, neither of which existed.

---

## One Real Defect, and One Convention Clash

**The article said it reported three errors in one place while the abstract and a later paragraph both
said four.** Fixed to four, with a note that the fourth is described inside the description of the
third, which is the point of that section.

**The whole body was reflowed.** The source used one unwrapped line per paragraph, up to 3,690
characters, and the prose I added was hard-wrapped, which produced **thirty lines with bold spanning a
break**. The corpus invariant is that **bold never spans a line break**, which every other article
satisfies either by not wrapping at all or by wrapping around it. The body now wraps at 108 characters
with bold kept atomic.

---

## Verification

**A 13-check independent verifier** recomputing the article's arithmetic from its stated inputs. It
includes **a property test over 20,000 random corpora that unit coverage can never exceed instruction
coverage**, which is what the product form forbids, and a check that the withdrawn citation-defect
rate really was the more alarming of the two.

All arithmetic confirmed: 64,116 of 73,434 at 0.8731, 168 of 496 at 0.3387, a gap of 0.5344, a
workstream ratio of 9.54, a clustering coefficient of 5.51, and a defect rate of 5.5 percent over 91
candidates.

**Prose style clean.** Zero em dashes, en dashes, prose colons, prose semicolons or parentheticals
beyond the permitted `console.log` tag, zero unbalanced bold, all 47 equations on single lines, zero
doubled backslashes.

**Build.** Isolated build at the 2026-08-06 date, all 47 equations rendering, six tables, 20 sections
and 16 subsections, zero Liquid errors, zero unresolved links, series navigation reporting Part 1.

---

## A Note on the Article Itself

**It documents its own author's formal recommendation being falsified by a two-second measurement, and
then documents four errors made while writing it, observing that all four ran toward a more striking
result and that the fourth was committed inside the paragraph warning against the first three.**

That is unusual and it is the most valuable thing in the article. **The retarget was written to make
that reachable, not to soften it.**

---

## State

**Committed, not pushed, not published.** Not a publication-review pass, so the push rule does not
apply.

**One question remains**, being whether siblings in the `keleusma_native` series are planned, since
the navigation reads Part 1 of 1.

The X-Planes series is untouched at twenty-seven articles complete and pushed. **The next X-Planes
article is A324, the Lockheed X-27.**
