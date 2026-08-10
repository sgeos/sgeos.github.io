# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A369 published and pushed live.

`_posts/2026-08-06-native_lowering_coverage.markdown`. 4,787 lines, 54 display equations, 1,765
references, roughly 24,900 words.

---

## What Happened

**The draft needed no commit.** The working tree was already clean and nothing was unpushed, since the
word-usage pass had committed and pushed it. That is stated rather than passed over, because the
instruction assumed there was pending work and there was not.

`_publish.sh` moved the file into `_posts/` and staged the rename. **No content changed at publication.**

**The editorial date of 2026-08-06 is three days in the past**, so the article went live immediately on
push and did not depend on `future: true`. The production build was therefore run **without** `--future`,
which is the configuration the live site actually uses and the only build that proves the point. The
article renders.

**The date slot was free.** The surrounding posts run 2026-08-01 through 2026-08-05 from the History of
SpaceX series, so this fills the day immediately after that series ends.

---

## Verification After the Move

`_verify.py` reports **zero errors and the unchanged 21-warning baseline**, so the article contributed no
new warning, and it is clean under `--strict` as well.

The production build succeeds in 11.4 seconds. The article renders at its live URL with **54 equations,
1,791 resolved identifier anchors, zero unresolved references, zero literal Liquid and zero Liquid
exceptions**, 23 sections, 32 subsections, six tables, and series navigation reporting Part 1.

**It appears on the home page, in `feed.xml` and in `sitemap.xml`.**

All twelve internal links were resolved against the built output. **All four `post_url` back-references
point at pages that exist**, the important one being A216, Keleusma's Self-Hosting Strategy.

**Two link targets are absent, and the absence is pre-existing and site-wide.** The post layout emits
`.pdf` and `.epub` download links for every article, and the built site contains two PDF files and no
EPUB files across 297 posts. The published A216 emits the identical pair. **This was checked rather than
assumed**, since a missing link on a newly published article is exactly the kind of thing that looks like
a regression.

The A369 entry was removed from `_drafts/draft_summary.md`, which tracks `_drafts/` contents only. Thirty
three draft sections remain.

---

## Still Open

**Two questions carry over and neither blocked publication.**

The `keleusma_native` series navigation reads Part 1 of 1. Whether siblings are planned would change the
series framing but nothing in the published article.

And `prose_text` in `_verify.py` does not strip `[text][anchor]` pairs, so harvested reference titles
count as prose and dilute the word-frequency check in the reference-heavy regime. **A369 is now a
published instance of that dilution**, at 11,800 words of author prose against 27,178 words as the
verifier counts them. The fix is a corpus-wide behaviour change affecting 297 posts and remains your call.

The next X-Planes article is A324, the Lockheed X-27, editorial date 2025-11-02. Next available article
number is A370.
