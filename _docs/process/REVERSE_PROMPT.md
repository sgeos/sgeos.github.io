# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A369 publication review. Committed **and pushed**. **Not published.** The draft remains in
`_drafts/`.

**111 references to 1,765. 1,268 to 4,789 lines.** 54 display equations held, roughly 25,000 words.

---

## The Survey, and What It Found

A contemporary survey of **1,650 references across fourteen clusters** was added, organised by what each
body of work says about the ordering question rather than by keyword.

**The finding is that the question has become more urgent since it was posed and no more answered.**
Backend bring-up used to be rare, performed by a handful of vendors. RISC-V made custom instruction sets
cheap, WebAssembly made a new target universal, staged lowering multiplied the steps, and accelerators
multiplied the targets. **The occasions for asking have multiplied and the principle is still missing.**

**The extension-identification literature comes closest and misses for a precise reason.** It selects
instructions by measured corpus frequency, which sounds like the same idea, but it selects instructions to
add to a **complete** machine for **speed**, where the objective is a sum. This article selects
instructions to implement next in an **incomplete** compiler for **capability**, where it is a product.
That is the whole difference and it is now stated.

**The sharpest new observation is that compiler fuzzing cannot answer this question at all.** Fuzzing is a
genuine success story and has found very large numbers of real defects. But a fuzzer generates programs
and checks whether the compiler handles them correctly, so **it tests what is implemented**. An
unimplemented instruction is not a bug it can find, because the compiler correctly refuses it. **The most
sophisticated compiler-testing machinery ever built cannot tell an engineer what to implement next.**

**And the blindness generalises.** Testing asks whether what exists is correct. Coverage tooling asks how
much of what exists is exercised. Verification asks whether what exists is sound. **All three presuppose
the artefact.** The question falls in the gap between building a compiler and testing one.

**The one decisive change cuts in the article's favour, and it is an argument the article was not
previously making.** Mining software repositories made corpus measurement ordinary. The twenty-minute
instrument is now the cheap part. **Measuring before ordering was expensive advice in 1978 and is nearly
free in 2026**, which is the strongest case for adopting the recommendation.

Two smaller observations were recorded. **Synthesis reduces implementation cost and leaves the blocking
set untouched**, so it moves the leverage ratio through its denominator only and reorders nothing.
**Machine-generated code is a growing fraction of any corpus**, so the representativeness caveat sharpens
rather than softens.

---

## Four Defects Fixed

**A heading had been glued to the end of a paragraph by an earlier reflow.** `### Seven literatures touch
this problem and none of them answers it` would have shipped as literal `###` text. It was invisible in
the source and detectable only because the heading was missing from a section listing. The reflow function
now keeps link pairs atomic as well as bold spans.

**All 111 reference definitions sat under a single `### Reference` heading** although 109 were `research_`
anchors. Split into Reference, Related Post and Research per the corpus convention.

**The article carried zero related-post links** despite this blog holding a Keleusma corpus. Four
back-references were added. **The important one is A216, Keleusma's Self-Hosting Strategy**, because that
compiler emits bytecode and this article is about lowering bytecode to native code. **That is a direct
sequel relationship the article had not stated.**

And two Source Base figures were wrong on first writing, a query count and a harvest total. Both corrected
against the logs.

---

## Homonyms, Found by Reading

**Every contaminant was found by sampling the clusters and none by anticipating it**, which is the
standing rule and it held again.

A query on binary translation returned forty-five records on **the static dielectric constants of binary
liquid mixtures**. A query on code corpora returned **linguistic** corpora. A query on interpreters
returned the training of **human** interpreters. And a study of **industrial chiller faults** reached the
shortlist through the word `empirical` in a software-engineering venue.

**The lesson is that a weak anchor is worse than no anchor.** `empirical`, `optimization`, `performance`
and `benchmark` were removed from the relevance test in favour of strong computing terms. 3,155 harvested
became 1,678 after filtering and 1,650 after title deduplication.

---

## Verification

120 of the 1,650 harvested identifiers were sampled and **all 120 resolve**. **An epistemic distinction is
now recorded in the article**, that harvested identifiers cannot carry the memory-substitution defect the
article documents, because identifier, title, author and year come from a single record. That is a
structural guarantee and not a verified one, and it is written that way. The foundational 86 were checked
exhaustively and all resolve to the claimed author and year.

`_verify.py`, run against a scratch tree with the draft installed as a post, reports **zero errors and no
style or word-frequency warning for this article**. Prose clean with zero em dashes, en dashes, prose
colons, prose semicolons or parentheticals beyond front matter and the permitted `console.log` tag, zero
unbalanced bold, zero split link pairs, zero glued headings, all 54 display equations on single lines, and
**23 apostrophes audited as possessives with zero contractions**.

**The isolated production build was run over the full 297-post tree, which is what proves the four new
`post_url` tags resolve.** 54 equations render, zero `$$` survivors, 1,791 resolved identifier anchors,
zero unresolved links, zero Liquid errors, 23 sections, 32 subsections, six tables, series navigation
reporting Part 1.

**Counts and fraction are both reported, as the genre document requires.** The base spans 1906 to 2026
with a median of 2022. The contemporary fraction is 94.2 percent and **the foundational count is unchanged
at 111 with 62 predating 2000**. Adding a survey lowers the fraction while leaving the primary count
untouched, so the fraction alone would read as a regression when it is the directive working.

---

## Awaiting Instruction

**The article is complete through all four passes and is committed and pushed. It has not been published**
and remains in `_drafts/`.

**One question is still open.** The `keleusma_native` series navigation reads Part 1 of 1. Whether
siblings are planned would change the series framing but nothing in the current draft.
