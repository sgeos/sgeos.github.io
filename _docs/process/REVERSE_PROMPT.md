# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-11
**Task**: A370 published and pushed. **It is live.**

`_drafts/two_calling_conventions.markdown` moved to `_posts/2026-08-07-two_calling_conventions.markdown`
at the editorial date 2026-08-07, series `keleusma_native` index 2.

---

## It Went Live Immediately, Because It Is Back-Dated

**This is the one thing worth flagging about the timing.** The editorial date is 2026-08-07 and today is
2026-08-11, so **A370 is back-dated by four days rather than forward-dated**. The site sets `future: false`,
which withholds forward-dated posts until their date arrives. That does not apply here, so the article
appeared on the first build after the push instead of waiting.

The predecessor A369 sits at 2026-08-06, so the two are adjacent and in order.

---

## The Interlock Was Checked In Both Directions First

A `post_url` whose target is absent fails the entire site build, so it was checked before the move and not
after.

- **A370's three targets all resolve**, being the A369 native lowering coverage article and the two Keleusma
  getting-started and self-hosting articles.
- **The only file referencing A370 was `draft_summary.md`**, which is a draft and does not build.

---

## Verification, In The Configuration The Deploy Actually Uses

**The build was run without `--drafts`**, which is what the deploy runs and what the drafting builds were
not. Exit 0.

- **Rendered page**: 0 unfilled markers, 0 unresolved references, **31 matched display-math delimiter
  pairs**, 4,202 links, 4,119 list items, 0 empty list items.
- **Series nav wired both ways**: A369 renders **Part 1 of 2** and links forward, A370 renders **Part 2 of
  2**.
- `python3 _verify.py` **0 errors, 21 warnings**, the unchanged baseline. **A370 appears in no warning now
  that it is checked as a published post rather than a draft**, so `convention` at exactly 5.00 per thousand
  does not trip the limit.
- **Live check after the push**: the article returns **200**, as does the site root.

---

## Final State Of The Article

| Measure | Value |
|---|---|
| Prose words | 11,477 |
| Display equations | 31 |
| Reference definitions | 2,002 |
| Research citations | 1,980, being 35 hand-selected and 1,945 harvested |
| Rendered links | 4,202 |

A370's section was removed from `draft_summary.md`, which tracks drafts only.

---

## Still Open, And Not Acted On

**The `configuration` finding from the word usage pass stands and I have not touched it.** It runs to 201,
154, 94 and 92 uses across four live SpaceX history articles, peaking at 14.9 per thousand, and its
collocations look like an abstract noun serving as a generic sentence subject rather than a term of art.
`substantial` at 29 uses in the hardware description languages article is a vague intensifier. Both are
rewrites of published work and remain your call.

---

## Draft Release Announcement

Per [Content Workflow](./CONTENT_WORKFLOW.md), the announcement is drafted here for your review before it is
posted anywhere. **I have not posted it and will not.**

```
New Blog Post: Two Ways of Doing One Thing: When an Apparent Design Wart Is a Semantic Boundary

Two implementations of one abstraction may be tracking a real boundary, and tidying them into
one can be impossible for reasons that are settled before any code is written. This article is a
public rendition of a private research spike from the Keleusma compiler project, which asked
whether two coroutine calling conventions in the code generation backend could be unified into
one. The material has been retargeted for a general engineering audience and needs no compiler
background.

The thesis is a counting argument. One class of coroutine has two things to report and only one
slot to report them in, so whichever thing the slot is given, the other is lost. The other class
has one thing to report, so a single slot is exactly enough. Count the observable events each
class produces, then count the channels the proposed unification provides. Where the counts
differ the unification is lossy, and no amount of analysis of individual cases will rescue it,
because the loss lives in the interface and not in the instances.

Key takeaways:
- Evidence about instances cannot repair a defect in an interface. Admissibility of a
  unification is a universal claim over a class, so one case refutes it and no quantity of
  confirming cases establishes it.
- The measurement pointed the wrong way while being entirely accurate. Nine of nine observed
  occurrences had the shape that invited the tidy-up, and nine of nine was true. It was a fact
  about the shape of instances offered in answer to a question about how much an interface can
  carry, and those are different questions. Read as a sample, nine successes from nine trials
  is consistent with 28.31 percent of cases failing at 95 percent confidence.
- Assembling a table for publication is a distinct verification activity. Doing so exposed a
  rule shipped one increment earlier that is stricter than the property it enforces, refusing
  ten of twenty-four cases whose tail sequence is provably harmless. No test found it.

The decision the spike informs is narrowed and not made. One option is ruled out on evidence
and two remain genuinely open, which the article reports rather than resolves.

You can read the full article here:
https://sgeos.github.io/engineering/compilers/verification/2026/08/07/two_calling_conventions.html

Let me know your thoughts. I would love to hear about the places in your own systems where two
implementations of one abstraction turned out to be load bearing!

hashtag#compilers hashtag#softwareengineering hashtag#programminglanguages
hashtag#softwarearchitecture hashtag#softwaredesign hashtag#formalmethods
hashtag#systemsprogramming hashtag#codegeneration
```

**Two things I checked rather than assumed.** The article does not claim the decision is made, so the
announcement does not either. The nine-of-nine figure is the article's own, and the 28.31 percent is the
complement of the exact one-sided Clopper and Pearson bound of 0.7169 that the article derives, not a
restatement of the measurement.

---

## Next

The X-Planes series is unchanged at **thirty-seven of seventy-two, none published**, with **A334, the Boeing
X-37, next** whenever you want it. Publication of those thirty-seven has still not been authorised and I
have not assumed it from this one.
