# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-11
**Task**: A370 correction, acting on `tmp/A370_correction_instructions.md`. **A live article was edited,
committed and pushed.**

---

## Both Defects Are Repaired, And The Second One Was Mine

**The widened-return option was published under-costed**, exactly as the instructions state. I verified the
argument before acting on it rather than transcribing it.

A coroutine resumes at the point it suspended. Under the callback convention that is free because the
function never returned. Under a return convention the call has ended and nothing survives, which costs
nothing for the divergent form, since the reset instruction clears every local and the next iteration
starts from the top, and **is fatal for the terminating form**, because the next call must resume mid-body
and a function entered at its entry point cannot do that. So the interface is a **triple** carrying a
continuation, not a pair carrying a tag, and the continuation implies a frame allocation whose lifetime
spans host execution, which is the property the option was credited with preserving.

**The option count was my error and it shipped.** The published text said two options remained and then set
out three. Traced through git, the pre-publication text at `8a53aa3` read "**Remaining, and genuinely
open:**" with no count. **My pathological-word-usage pass at `21e34c2` replaced that colon-led label with a
full sentence and invented a count the list never had.** Removing a prose colon introduced a factual error
into an article that was two commits from going live, and no check I ran afterwards could see it.

---

## I Found A Third Thing The Instructions Did Not Ask For

**The correction contradicted another section of the same article, and fixing only the passages listed
would have shipped that contradiction.**

The Contemporary Literature said the convergence of C#, F# and Kotlin on a tagged return is "the strongest
available evidence for the widened-return option this article identifies". After the correction that
sentence argues for the under-costed form.

**Read carefully, the literature is evidence for the correction.** Not one of those systems returns a bare
tagged value. Each pairs the tag with a state object that survives the call, the state machine in C# and F#
and the continuation in Kotlin, precisely because a coroutine that suspends more than once must resume
mid-body. **They converged on the triple and the article read them as converging on the pair.** That is now
in the text, and it makes the correction better evidenced than the original claim was.

This is the failure mode A333 hit, where a withdrawn claim survived in two other sections.

---

## What Changed

| Location | Change |
|---|---|
| The third option | Added the reentrancy argument, the triple interface, and the frame it implies |
| Cost model | $C_{\mathrm{one}} = (c_{\mathrm{tag}} + c_{\mathrm{frame}}) N$, with $c_{\mathrm{frame}} = 0$ only at most one suspension per call, and the crossover moved down |
| The 95.83 percent | Now says explicitly it must not be read as the fraction for which a pair suffices |
| Options list | The frame property is preserved only for at most one suspension per call |
| Options count | Two to three |
| The Contemporary Literature | Reconciled with the correction, as above |
| Epistemic State | Both corrections recorded, including that the corpus could not have exposed the first and that the second came from a later editing pass |

**No new reference was needed.** `llvm.coro.id.retcon` is cited through the existing
`ref_llvm_coroutines` anchor.

---

## What Did Not Change, As Instructed And As Verified

The pigeonhole argument, the semantic-boundary finding, the recommendation, every measurement figure, and
the citation set. **The correction makes the alternative less attractive, so the recommendation stands a
fortiori.**

---

## Verification

- `python3 _verify.py` **0 errors, 0 warnings**.
- `python3 _lib/render.py _site` over a full build: **462 pages, no findings, exit 0**. This is the first
  correction to run through the rendered auditor.
- **32 display-math blocks, balanced in source and in the rendered page.**
- `lint.scan` on the article: **0 defect-severity findings**.
- The `llvm.coro.id.retcon` citation renders as inline code inside a resolved link.
- **Prose scan clean.** The one colon the scan reports is Keleusma syntax inside a fenced code block.

---

## Standing Work, Unchanged

**A334, the Boeing X-37**, on your prompt. **The thirty-seven X-Planes drafts remain unpublished and
unauthorised.**
