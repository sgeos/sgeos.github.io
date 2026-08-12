# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-12
**Task**: A371, the third Keleusma native code generation article. **Publication review complete.**
**Committed AND pushed. NOT published.**

---

## Where It Is

`_drafts/do_proven_bounds_survive_compilation.markdown`, editorial date **2026-08-08**, series
`keleusma_native` index 3. **34,186 lines, 26 display equations, 11,112 reference definitions, 8,331 words
of author prose.**

**The editorial date is back-dated relative to today**, so publishing it would put it live immediately. It
is not published and I have not assumed you want it to be.

---

## The Substantive Gap Was the Survey, and the Numbers Say So Plainly

A369 carries 1,759 research references. A370 carries 1,980. **A371 arrived with 28**, which is a factor of
about sixty-five against your standing instruction that every article in this series serve as a
comprehensive survey of the contemporary literature.

A harvest of **119 queries across fifteen clusters in seven rounds** retrieved 60,091 records. The anchor
gate admitted 11,604 and **11,068 reach the reference list**, beside the 28 hand-selected works, which are
untouched and remain the only ones read. The article says so in its own Source Base and Epistemic State.

**27 of the 28 hand-chosen works were independently returned by the harvest.** That is the best
corroboration of coverage available, because those 28 were chosen before any query ran.

---

## The Largest Defect Was a Venue Filter, and It Took Two Corrections to Find the Bottom

The first rounds requested **journal articles only**, which is the right choice for the aerospace articles
this machinery was built for and the wrong one for computer science. Those rounds returned 19,169 records
and **not one paper from the CerCo project**, which is the research programme the article itself names as
the closest existing work to its own problem.

**Adding conference proceedings more than doubled the corpus and still returned no CerCo paper.** The
reason is that **Springer deposits its Lecture Notes in Computer Science volumes as `book-chapter` rather
than `proceedings-article`**, so an LNCS proceedings paper is typed as a chapter of a book. A third pair of
rounds recovered both papers the article cites by hand.

**No count could have found this.** Each of the first two attempts produced a corpus that was large,
plausible and missing the same thing. It was found only by probing for a named project the survey was known
in advance to require, which is now the method I would use first rather than last.

---

## A Silent Structural Defect in My Own Gate

Every qualified anchor was written as `X(?=.*Q)`, which requires the qualifier to appear **after** the
anchor. `Crafting a Java virtual machine in silicon` was therefore refused, because Java precedes the
phrase. Rewriting every qualifier as a pair of lookaheads evaluated from the start of the title
**recovered 303 records**.

**The cost family was admitted unqualified**, so a Handbook of Army Cost Analysis Terms, a
refuse-derived-fuel cost model and a cost-effectiveness compilation for heart conditions reached the kept
set. The harvest's own notes warned that `resource` cannot be filtered and then **failed to apply the same
reasoning to `cost`, which is worse**, because `cost analysis` and `cost model` are complete phrases in
accounting rather than words merely shared with it.

Tightening it then **collapsed the cost cluster from 52 to 3**, which is the signal that a tightening has
gone too far. Reading the 144 rejects found **four genuine losses**, including `Cost Relation Systems` and
`Closed-Form Upper Bounds in Static Cost Analysis`, each refused by a qualifier that was correct and too
literal, wanting `type system` against `type-theory`.

**A literal space in a multi-word anchor refuses the hyphenated spelling.** That is the **seventh** time in
this corpus that a spelling variant has returned a smaller corpus rather than a wrong one.

---

## Seventeen Homonym Families, Found by Reading Four Samples and Not by Anticipation

`_research/homonyms.py` goes from 41 to 56 noise patterns. **Four independent samples of thirty were read,
each found families the previous had missed, and the last one still found one.** A survey reporting a clean
sample would be reporting that it stopped looking, and the article says that in its Epistemic State.

The families include Stack Overflow the website against the stack overflow condition, circuit timing
signoff against software timing analysis, **three separate senses of just-in-time** being manufacturing,
instructional delivery and commit-time defect prediction, formal semantics in linguistics, the peephole in
critical theory, semantic preservation in natural language generation, the calendar timing anomaly in
finance, Java the island together with pre-stack seismic imaging, static analysis in geotechnical
engineering, the cloud virtual machine, web cache replacement, and software cost estimation.

---

## Two Load-Bearing Citations Were Silently Repointed, and an Off-By-Two Found It

`refs.assign_anchors` builds an anchor stem from first author and year, so **`Necula 2000` names two
different papers**, being the hand-cited translation validation work and a harvested proof-carrying code
abstract. The harvested record took the stem and the merge then replaced the hand entry, so **the prose
citations of Necula 2000 and Pnueli 1998 resolved to the wrong works**.

**This is the exact defect class the article reports having committed four times**, reproduced by my own
tooling in the same sitting. It was found by an off-by-two in the reference count and by no checker. The
hand anchors are now reserved, and the assembler **raises on any collision** instead of merging over it.

Separately, `hand_selected_keys` read the draft, **which is this pipeline's output**. Once a harvest was
assembled it reported 11,094 hand-selected references, treated the whole harvest as already cited, and
emitted a master set of one record.

---

## The Count in My Own Prose Was Wrong by Eight

I wrote that **nine** homonym families were recorded. The store held **seventeen**. That is the same
count-in-my-own-prose defect this article family has now shipped three times, so the count is now derived
from the store, and the assembler **raises if the prose list length disagrees with it**.

Three superlative claims were checked against the numbers that actually landed and corrected. Worst-case
execution time is fourth largest and not second. Real-time certification is largest only among the named
clusters, since the adjacent bucket is larger. And the cost cluster is more than two orders of magnitude
smaller, not roughly two.

---

## The Two Defects Carried Over From the Equation Pass

**The stale identifier count is fixed.** The Epistemic State now says the bibliography was submitted with
27 identifiers of which four were wrong, and that a twenty-eighth was added during editing and resolves,
which describes what happened instead of renumbering the error rate.

**The claim about A370 was wrong and is corrected.** A371 said A370 "resolved 31 of 31". A370's own text
states 35 hand-selected references and 35 resolved. It now reads 35 of 35.

---

## Style and Verification

- `python3 _verify.py` **0 errors, 0 warnings**.
- `python3 _lib/test_lib.py` **75 of 75**.
- `./_check.sh --drafts` **passes end to end**, 506 pages, no findings.
- Reference integrity **11,112 used against 11,112 defined**, zero undefined, zero orphaned, zero duplicate
  definitions, zero malformed list entries.
- **All 28 hand-selected identifiers resolve.** The 403 responses are ACM and the 202 responses are IEEE,
  both documented publisher behaviour, and the single failure was a transient name-resolution error
  confirmed afterwards against the registry, which returned the exact cited title.
- A sample of 12 harvested identifiers resolves.
- Prose clean with zero em dashes, zero en dashes, zero prose parentheticals and zero prose semicolons
  outside mathematics. Two prose colons removed.
- `rather` brought back under the corpus maximum with eight rewrites, **each checked for grammaticality
  rather than substituted mechanically**, which is the lesson A369 paid for.

---

## Outstanding, and One Thing I Did Not Decide for You

**It is committed and pushed, and it is not published**, which is what you asked for.

**Publishing it would put it live immediately**, because 2026-08-08 is in the past. It sits behind A370 in
the series, so publishing would also renumber the two published articles' navigation from "Part 1 of 2" and
"Part 2 of 2" to "of 3". **That is a change to two live pages and I have not made it.**

**The X-Planes work is untouched by this.** A335 remains the last of thirty-nine drafts, all four passes
done, none published, and **A336 is X-39, Reserved but Never Assigned**, a designation anomaly taking the
reduced section order. The handoff at `_docs/process/HANDOFF.md` describes it and should be re-validated
against `git rev-parse HEAD~1` before it is trusted, since this commit moves the head.
