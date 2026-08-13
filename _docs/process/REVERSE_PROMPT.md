## Last Updated

**Date**: 2026-08-13
**Task**: **A336, X-Planes, X-39, Reserved but Never Assigned. Publication review complete.**
Committed and **PUSHED**. **Not published.** All four passes are done.

---

## The Pass Reversed the Draft Pass a Second Time, for the Same Reason

**The draft omitted the contemporary-literature survey and gave a reason I still think is correct**, that
a harvested survey of the **aerospace** literature would measure nothing relevant to whether a letter was
written in 1997.

**The conclusion drawn from it was wrong.** This article's subject is not an aircraft. It is what a gap in
an official register means, and **there is a large, current, directly relevant literature on exactly
that**, spread across archival science, infrastructure studies, identifier administration and the logic of
inference from absence. What did not belong was a survey of the wrong field.

**So the survey is now of the right one.** Eight clusters, being archival silence, the argument from
silence, classification systems as infrastructure, identifier assignment and reuse, administering a finite
number space, recordkeeping and the administrative trace, register maintenance, and military nomenclature
practice.

**23,114 raw records, 2,550 through the gate, 2,452 into the reference list** after 98 duplicate
registrations were removed.

**It is kept strictly apart from the evidence.** Not one harvested record is cited in support of any claim
about the X-39, none was read, and **the article would say exactly the same things if the survey were
deleted**. The survey lead, the Source Base and the Epistemic State each say so.

---

## Read This, Because Reading Beat Counting Again

**The gate had a defect that no count would ever have shown, and the audit sample found it.**

The qualifier helper wrote `(?=.*{p})` where `p` contained an alternation. **The alternation escaped the
lookahead**, so `(?=.*standard|standards)(?=.*maintenance|revision)` parsed as `(?=.*standard)` OR
`standards` OR `(?=.*maintenance)` OR `revision`. Every qualified anchor silently became a disjunction of
bare words.

**It failed in both directions at once**, which is why no statistic caught it. Too permissive, admitting
building-information-modelling standards maintenance and hydraulic preventive maintenance on the bare word
`maintenance`. Too narrow, refusing `On the Consolidation of the Internet Domain Name System` because only
the first alternative was anchored. **Correcting it took the military designation cluster from 7 records
to 132.**

**A second sample found four more homonym families**, being the boundary-object concept as it is now used
in education research and design studies, spectrum allocation as a cognitive-radio algorithm rather than a
regulatory act, biological nomenclature, and `sorting things out` as a pun in cell biology. It also found
a spelling variant, **`reuse` failing to match `reusable`**. That is the **eighth** spelling or grouping
defect in this corpus to return a corpus that was wrong rather than empty.

**The article claims a clean corpus nowhere**, and says a third sample is what a fourth would have found.

---

## Two Generator Defects Caught Before They Reached the Article

**`refs.dedupe` returns a pair.** Binding it to one name yields a list of two lists, and the next line
would have emitted a survey of **two** records without raising. It crashed here only by luck of a later
type error. This is the silent form of the defect.

**`refs.clean` was applied to titles and never to author names**, so `Fran&ccedil;ois` reached the link
text undecoded. It happens to render correctly in a browser, which is why nothing downstream complained.

**Both are fixed at source, not patched in the output**, and the assembler now carries the published-file
guard that A371 and A372 have.

---

## What the Structural Review Found

**The Related Post list was wrong against the corpus convention.** It was in series order with bare titles
where every other article in this series sorts alphabetically by the full article title. Rebuilt from the
drafts' own front matter rather than retyped.

**Six Reference entries were misordered**, and after the survey went in, all 2,523 definitions needed
re-sorting within their anchor groups.

**A paragraph-order defect from the primary pass had orphaned the Boeing study**, leaving it stranded
after a concluding paragraph about both contractors.

**Three statements contradicted the new sections** and were reconciled rather than left, being the claim
that the article carries no survey, the claim that the reference base is small, and the reduced-order
paragraph.

---

## Verification

- `python3 _verify.py` **0 errors, 0 warnings** across 300 posts.
- `./_check.sh --drafts` **clean end to end**, 509 pages, no rendered findings.
- Reference integrity **2,523 used against 2,523 defined**, zero undefined, zero orphaned, zero duplicates.
- **2,723 reference list entries, all well formed.** All three visible lists and all three definition
  groups sorted.
- Rendered body carries **zero raw display-math delimiters, zero unresolved reference syntax, zero
  unrendered Liquid and zero empty list items**. Navigation reads **Part 40 of 40**.
- **A random sample of 20 harvested identifiers resolves 20 of 20.** The 403 responses are ACM and
  publisher bot detection, which is documented behaviour.
- Diction **0 constructions above the corpus maximum** against 300 peers. The four words above 5 per
  thousand are `number`, `designation`, `programme` and `aircraft`, **all of them the article's subject**.
  `rather than` sits at 4.02 against a maximum of 4.98 and **was not rewritten mechanically**, which is
  A369's lesson.
- **Final state 5,919 lines, 8 display equations, 2,523 reference definitions, 53,115 words**, of which
  6,724 are author prose.

---

## Outstanding

**It is committed and pushed, and it is not published**, which is what you asked for.

**Publishing it alone would fail the build.** A336 cites thirty-nine siblings through `post_url` and none
of them exists in `_posts/`, so **the set publishes in order or together**. Forty of seventy-two are
drafted and **publication has never been authorised**.

**A337 is the Boeing X-40**, editorial date 2025-11-15, series index 41. A336 used only the designation
facts about the X-40 that its argument required, being the year of allocation and the reassignment from
the Space Maneuver Vehicle to the test bed, so **the vehicle itself is untouched and available**.

**One item is still owed from outside this repository**, being A369's factor-of-roughly-thirty claim,
which rests on the Keleusma decision register.
