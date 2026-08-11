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

## Next

The X-Planes series is unchanged at **thirty-seven of seventy-two, none published**, with **A334, the Boeing
X-37, next** whenever you want it. Publication of those thirty-seven has still not been authorised and I
have not assumed it from this one.
