# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-12
**Task**: A371, the third Keleusma native code generation article. **Equation-density review complete**,
following the standards and retarget pass in the previous commit.
**Committed. NOT pushed and NOT published.**

---

## Where It Is

`_drafts/do_proven_bounds_survive_compilation.markdown`, editorial date **2026-08-08**, series
`keleusma_native` index 3. **758 lines, 26 display equations, 44 reference definitions, 6,693 words.**

**The editorial date is back-dated relative to today**, so publishing it would put it live immediately.
It is not published and I have not assumed you want it to be.

---

## Sixteen to Twenty-Six Equations, and the Best One the Article Already Had in Prose

**The article's thesis was a schema stated only in words.** It is that proving a property of one artefact
does not license claiming it of a transformed one, and writing that down once in the opening lets the
**conclusion close the loop by giving the three available shapes as three schemas**, being fix a contract,
recompute from the artefact, and transfer. **Nobody deploys the third.** That is the article's
recommendation and it now has a form rather than only a sentence.

**The pair arithmetic turns a phrase into a number.** The article called its zero-inversion result
"barely a test at all" without showing why. With ties removed the strictly ordered pairs are
$\binom{9}{2} - \binom{7}{2} = 15$, so **the sample makes 41.7 percent of the comparisons it appears
to**. The claim was right and unquantified.

Also added: the summation that carries the per-instruction premise to the aggregate conclusion, which the
article stated in prose and never displayed, with the observation that **$\alpha$ and $\kappa$ are the
same number reached from two directions**. The memory bound in the bytes the article actually quotes. The
CerCo inversion as two directions side by side. The optimiser's deletion beside the emission.

**Two of seven audited gaps closed, and the five that remain should stay open.** They are survey prose
about other people's work plus one restatement, where the numbers are publication years. Manufacturing
relations for them would be padding.

---

## Reading the Twenty-Six Found a Collision, and a Rule This Article Had Escaped

**$A$ was both the artefact in the schema and the allocation count in Result 1.** The allocation counts
are now written out as $\mathrm{allocs}$, and a short notation note states which symbols are general and
which are specific, namely that $\mathcal{R}$ is the particular kind of property and $\mathcal{C}$ the
particular kind of transformation.

**Three display equations spanned two source lines.** The corpus rule is one line, because the style
checker validates per line, and **this article was hand-authored and never passed through `reflow`**,
which is what enforces that rule for the generated articles. Worth remembering for any future article
that arrives from outside the pipeline.

---

## One Citation Added, and a Note on Why Not More

**`citation_gaps` rose from 10 to 18 and most of that should be ignored for this genre.** The metric
assumes an article whose relations come from a literature, and here most of them are the author's own
derivations about the author's own compiler. **Citing anyone for those would be manufacturing.**

The one genuinely borrowed relation left uncited was **Kendall's rank correlation**, whose numerator the
inversion count is. It is cited now.

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
- `./_check.sh --drafts` **passes end to end**, no findings.
- **All 28 research identifiers resolve**, none registry-only.
- **All 14 curated URLs resolve**, the single 403 being `iso.org`, a documented bot-mitigation case.
- Reference integrity clean, 44 used against 44 defined, none undefined or orphaned.
- Section order conforms to the analytical-essay genre.
- All 26 equations read for brace balance, delimiter closure, bare pipes and doubled backslashes.

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
