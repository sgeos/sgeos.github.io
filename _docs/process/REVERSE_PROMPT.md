# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-12
**Task**: A371, the third Keleusma native code generation article, copied in from the Keleusma
repository, brought to corpus standards and retargeted for a general audience.
**Committed. NOT pushed and NOT published.**

---

## Where It Is

`_drafts/do_proven_bounds_survive_compilation.markdown`, editorial date **2026-08-08**, series
`keleusma_native` index 3. **702 lines, 16 display equations, 43 reference definitions, 6,233 words.**

**The editorial date is back-dated relative to today**, so publishing it would put it live immediately.
It is not published and I have not assumed you want it to be.

---

## The Largest Defect Was a Duplicated Survey

**The contemporary-literature section appeared twice.** The second pass re-covered worst-case execution
time analysis, stack bound analysis, the AbsInt tools, verified compilation, translation validation and
proof-carrying code, all of which the first pass had already covered under better headings. **Forty-nine
lines removed**, with nothing lost that the surviving pass does not say.

---

## The Article Claimed No Compiler Background Was Required and Did Not Deliver It

The source said in its second paragraph that **no compiler background is required**, and then used
bytecode, machine code, optimising compilers, stack frames, register allocation, spilling, `alloca`,
calling conventions and memory-to-register promotion without introducing any of them.

**Either the claim or the article had to change**, and since the retarget you asked for wants the claim
to be true, the article changed.

- **A new `## What You Need to Know to Read This` section** carries the five ideas the argument actually
  needs, in plain language, each one earning its place because a later section depends on it.
- **The opening leads with the general problem** and three analogies that involve no compilers at all,
  being a staging-environment performance budget, a circuit-simulated power draw and a scale-model safety
  margin, before naming a compiler.
- **A `## The Uncomfortable Answer` section** states early that verifying the compiler is not enough,
  which was buried in the source and is the point most likely to surprise a reader.
- **The jargon-dense passages now name things in words first.** The eBPF section explains what eBPF is.
  The reefing of terms like `stream entry point`, `chunk` and `lowering` is gone.

**The mathematics is untouched**, because the genre wants it and a general technical reader can follow a
relation whose symbols are named in prose immediately before it.

---

## Two Count Errors in My Own New Prose

**This is precisely the defect A370 shipped and I reproduced it twice in one sitting.**

- The orientation section promised **six ideas** and gave five.
- The summary promised **two findings** where the article has three, and the same paragraph then
  referred to "the third result".

**Both were found by reading the draft rather than by any checker**, which is the standing lesson.

---

## A Figure in the Lede Was Supported Nowhere

The source opened by saying the measurement takes **nine seconds**, and that number appeared in no other
section of the article. **A number in a lede that the body does not carry is unverifiable by a reader.**

It is now stated in the Source Base beside the rest of the instrument description, and the Epistemic
State marks it as **the author's report rather than an independently timed figure**, with the note that
nothing in the argument depends on it.

---

## A Corpus-Wide Checker Artefact, Found Here and Fixed

Of the 27 research identifiers, **26 matched their cited titles exactly and one read as a defect that was
not one.**

**Crossref deposits a title and its subtitle as separate fields.** `CakeML: a verified implementation of
ML` is stored as the title `CakeML` alone, so a label citing the paper the way everybody cites it
overlapped the registry title by **0.17** and would have been reported.

**`_verify_citations.py` now folds the subtitle into the comparison.** This is the same shape as the
`no-title` artefact that accounted for 14,979 of 15,159 weak findings before it was fixed, which is to
say **the checker was comparing against less than the registry actually holds.** Cached records still
carry the old title and will correct themselves as the cache refreshes.

**I did not change `refs.display` or `fetch.crossref_fields`**, which build reader-facing link text, since
adding subtitles there would rewrite labels across the whole corpus for no benefit.

---

## Style and Verification

Twenty-one prose colons, ten prose semicolons and two em dashes removed. Link definitions and all five
visible reference lists sorted. `rather than` reduced from above the corpus maximum.

- `python3 _verify.py` **0 errors, 0 warnings**.
- `python3 _lib/test_lib.py` **75 of 75**.
- `./_check.sh --drafts` **passes end to end**, 506 pages, no findings.
- **All 27 research identifiers resolve**, none registry-only.
- **All 14 curated URLs resolve**, the single 403 being `iso.org`, a documented bot-mitigation case.
- Reference integrity clean, 43 used against 43 defined, none undefined or orphaned.
- Section order conforms to the analytical-essay genre.

---

## Outstanding, and Two Things I Did Not Decide for You

**It is committed and not pushed.** You did not ask for a push and this is not a publication review, so I
left it local. Say the word and it goes up.

**Publishing it would put it live immediately**, because 2026-08-08 is in the past. It sits behind A370
in the series, so publishing would also renumber the two published articles' navigation from "Part 1 of
2" and "Part 2 of 2" to "of 3". **That is a change to two live pages and I have not made it.**

**The X-Planes work is untouched by this.** A335 remains the last of thirty-nine drafts, all four passes
done, none published, and **A336 is X-39, Reserved but Never Assigned**, which is a designation anomaly
taking the reduced section order. The handoff at `_docs/process/HANDOFF.md` is current and validates.
