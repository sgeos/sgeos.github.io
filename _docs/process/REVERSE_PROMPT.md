# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-12
**Task**: A335, the Scaled Composites X-38. **Publication review complete. All four passes done.**
**Committed and PUSHED. NOT published.**

---

## A Factual Error in a Constant Changed a Result

**The X-24A's length had been set equal to the X-38 atmospheric test vehicle's 24.5 feet, which is a
different aircraft**, and its mass was low by three hundred kilograms. Corrected to **24 feet and 11,447
pounds**, the scaling exponent falls from **4.207 to 3.507** and the geometric-similarity factor from
1.276 to **1.120**.

**The conclusion survives**, because the argument uses only the sign, that mass grew faster than the
cube of length, and the contrast with the X-37's **1.924** still straddles 3. **A caveat now records
that the exponent rests on two published figures for a vehicle retired in 1971 and is sensitive to
both.**

**Nothing had caught it because both figures were plausible and both produced a plausible answer.** The
independent verifier had been handed the same two constants, and **a verifier that shares an input with
the thing it checks does not check that input.** It now derives the X-24A figures by converting from
the imperial values the sources actually quote. **A new entry in the traps document records the whole
shape of it.**

**The consolation is that independence still paid.** The verifier failed loudly the moment the
production module changed, rather than following it silently.

---

## Two Style Defects, Both Shared With A334

**`DLR` was used without a spell-out**, which the acronym rule forbids on first use.

**The generated reference-count block used capitals for emphasis** where the corpus rule requires bold.
That text came from the assembler, and **A334 carries the identical violation**, so both assemblers were
corrected and **A334 was rebuilt**. It is an unpublished draft and leaving a known violation in it would
have been knowingly shipping one.

---

## Everything Else Was Clean

- **Prose style clean on every check.** No em dashes, en dashes, prose colons, prose semicolons,
  parentheticals or contractions, and after the fix no capitals used for emphasis.
- **All 18 curated URLs resolve**, checked individually per the trap A334 established. None returned 404
  this time.
- **No drafting-history leaks.** The Source Base was written to state findings rather than to narrate
  passes, which is the correction A334 needed and this article did not.
- **Section order conforms to the research-aircraft genre** without exception.
- **Contemporary coverage is 49.6 percent** of dated records with **19.9 percent** dated 2020 or later,
  which satisfies the comprehensive-survey directive.

---

## Verification

- `python3 _verify.py` **0 errors, 0 warnings**.
- `python3 tmp/a335/verify.py` **46 of 46**.
- `./_check.sh --drafts` **passes end to end**, no findings.
- **3,816 reference entries scanned** for stray punctuation, all clean.
- **Reference integrity clean**, 1,936 used against 1,936 defined, none undefined or orphaned.
- Identifier sweep, seeded sample of 200: **200 of 200 resolved**, 22 through the issuing registry.

---

## Final State

**6,733 lines, 24 display equations, 1,936 reference definitions, 36,570 words**, with all **1,768
research records cited and none left over**, plus 112 reference works.

Period half **871**, contemporary **883**, technical reports **478 at 27.0 percent**, which is the
highest report share this series has measured and is what a decelerator subject should produce.

---

## Outstanding

**Nothing blocking.** The tree is clean and everything is pushed.

**A335 IS NOT PUBLISHED and publication of the thirty-nine X-Planes drafts has never been authorised.**
The article remains in `_drafts/`, the deploy workflow builds without `--drafts`, and the
publication-order dependency is now **thirty-nine deep**.

**A336 is X-39, Reserved but Never Assigned**, editorial date 2025-11-14, Part 40 of 72. **It is a
designation anomaly**, and the genre document prescribes the reduced six-section order for one, with
the caveat that A320 was written at full length because the X-23 actually flew and returned a
measurement. **The test is whether a vehicle existed and produced data, not whether the designation is
disputed.** For a number that was reserved and never assigned, the short class is the honest default.
