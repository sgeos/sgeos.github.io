# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-12
**Task**: The three `keleusma_native` research spike articles given a **shared main title with distinct
subtitles**, following A371's word usage pass in the previous commit.
**Committed AND pushed. A369 and A370 are live pages and changed. A371 NOT published.**

---

## Where It Is

`_drafts/do_proven_bounds_survive_compilation.markdown`, editorial date **2026-08-08**, series
`keleusma_native` index 3. **34,193 lines, 26 display equations, 11,112 reference definitions, 7,403 words
of author prose** as `diction.prose` measures it.

**The editorial date is back-dated relative to today**, so publishing it would put it live immediately. It
is not published and I have not assumed you want it to be.

---

## The Shared Title, Which Is the Newest Work

The three articles now read **Keleusma Research Spike** followed by their own subtitle.

- A369, `Blocking Frequency as the Ordering Principle for Instruction-Set Coverage`
- A370, `When an Apparent Design Wart Is a Semantic Boundary`
- A371, `What a Verified Bound Says About the Code That Actually Runs`

**I checked the URL risk before touching anything and it is nil.** `_config.yml` carries no top-level
`permalink:`, the `permalinks:` key belonging to `jekyll-archives`, and none of the three files carries a
`slug:` override. Jekyll's default permalink therefore takes `:title` from the **filename**, so a
front-matter title is URL-neutral and **no `redirects/` entry is needed**. Confirmed afterwards against a
production build, with both live URLs resolving unchanged.

**The comment threads were the risk that mattered more, and they survive.** `_includes/comments.html` sets
`data-mapping="pathname"`, so Giscus keys its GitHub Discussions to the URL path. **Had it been set to
`title`, this change would have orphaned every existing comment thread on two published articles.**

**The link-text convention had to change with the titles.** Related-post entries carried the main title
alone, which under a shared main title would make three different links read identically. They now carry
the subtitle. Three were updated, one in A370 and two in A371.

Two consequences worth your eye. The series navigation now lists two entries both beginning
**Keleusma Research Spike**, distinguished by their Part 1 and Part 2 labels, which reads acceptably but is
repetitive by construction. And **historical TASKLOG entries still name the old titles**, which I left
alone deliberately, since they record what was true when written.

---

## The Word Usage Pass, From the Previous Commit

**`specific` is not a problem here.** It stands at **6 uses for 0.82 per thousand**, well under the limit
and under the corpus median. I checked it first because you named it.

**The measurement had to exclude the harvest or it could not fire at all.** The article carries 331,800 raw
body words against **7,403 words of author prose**, so measuring the raw body would divide every rate by
about forty-five and guarantee silence. `diction.prose` strips link pairs, which is the fix made after A369
found that defect, and it is the only reason this article is measurable.

**Every existing instrument looks at single words, and A369's largest finding was a phrase.** `_verify.py`
watches a fixed forty-seven word class. A369's `and not` reached 2.19 per thousand against a peer maximum
of 1.73 **because an earlier pass had mechanically rewritten `rather than` to clear a single-word limit**,
which is a trade no single-word instrument can see. I added `tmp/a371/phrases.py`, which ranks two- to
four-word constructions against 254 published peers, counting a peer that never uses a phrase as a zero.

**It found 37 constructions at or above the peer maximum, and the real ones were my own boilerplate from
the previous pass.** Six survey subsections opened with `The harvest returned N further contemporary
records in this cluster`, identical but for the number, and four more used `N contemporary records concern
X`. **Ten template sentences now carry a fact about their own cluster instead of restating a count the
reader can already see.** The count fell to 26, and every survivor is subject vocabulary measured against a
corpus of aircraft articles.

**A sense collision on a defined term.** `artefact` is this article's name for $A$, the thing a property was
established about. The Epistemic State also used it in the ordinary measurement sense, saying none of the
four errors "was an artefact of the checking method". It now says false positive.

**Two content redundancies that the word count found and reading had not.** The coverage claim was stated
almost verbatim in both the Source Base and the Epistemic State. And a harvested-list lead I wrote in the
previous pass repeated the hand prose three lines above it, that the theorems are about observable
behaviour.

**`about` remains above the peer maximum and I did not reduce it mechanically.** It sits at 6.08 per
thousand against a peer maximum of 5.28. **42 of its 45 uses are the aboutness sense the thesis is written
in**, being a property established about one artefact and claimed about another, and 3 are the
approximation sense. I classified all 45 rather than asserting the reason. A369's standing lesson is that a
mechanical substitution is not an edit, and trading `about` for a synonym here would move the tic rather
than remove it.

`rather` stands at 28 for 3.78 per thousand. The `three distinct magnitudes` refrain was varied in three of
seven places, in each case where the wording and not the claim was the repetition.

---

## The Corpus-Wide Outliers Are Mostly Not Tics, and One Is

Since you gave `specific` as a recurring example, I ran the corpus-wide check and triaged by collocate,
which is the only thing that separates a topic from a tic.

- **`specific` at 15.07 per thousand is `specific impulse`**, 86 to 99 percent of uses across the rocket
  propellant chemistry articles. It is the term Isp and must not be touched. `_verify.py`'s own comment
  already records this.
- **`key` at 18.26 per thousand is the cryptographic key** in the Solana and SSH articles, `key pair` and
  `key file`. A subject noun.
- **`typically` at 6.88 per thousand in the published search and rescue drone article is a genuine hedge.**
  Its collocates are all verbs, being `typically completes`, `typically budgets` and `typically holds`, so
  it modifies claims rather than naming a thing. **I flagged it and did not touch it**, because it is a
  live published page and outside what you asked for. Say the word if you want it fixed.

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
