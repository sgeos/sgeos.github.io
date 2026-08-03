# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-02
**Task**: A290 equation-density review for remaining candidates. 3 further display equations added, 71 to 74. Reference-density pass remains.

---

## How the Review Was Conducted

The expansion pass had already brought A290 from 30 to 71. This review tested whether that pass was exhaustive rather than assuming it.

I scanned every prose paragraph for quantitative or structural language with no display equation within four lines. That returned seven paragraphs. Five sit in sections that carry zero equations in every sibling, namely Methodological Commitments, Historiographical Gap, Data Sources, Cross-References, and Terminological Note. Those were correctly left alone. The remaining two were already well covered by adjacent math.

A mechanical scan is weak evidence on its own, so I then read for load-bearing claims the scan would not catch. That found three worth formalizing.

---

## The Three Additions

**1. The January 2015 round does not reconcile.** The article reported approximately one billion dollars for approximately ten percent, and separately reported an approximately twelve billion dollar valuation. The arithmetic gives ten billion post-money and nine billion pre-money.

I did **not** reconcile the gap, because the record does not support reconciling it. The reported figure may be pre-money or post-money, the round may have carried a secondary component that does not dilute, or the percentage may be loose enough to absorb the difference. The article now states the discrepancy and says which of those it cannot distinguish. **This is the kind of thing worth your eye**, because it is a genuine internal inconsistency in the reconstructed figures rather than a presentational matter, and I have surfaced it rather than smoothing it.

**2. The tender interval was reported but never used.** The article calls the mechanism semi-annual throughout and never does anything with the frequency. It bounds the wait from an arbitrary date to the next occasion at six months, which is roughly five percent of the ten-year term. That bound is what licenses treating the mechanism as continuously available rather than episodic.

The counterfactual sharpens it. A triennial tender would leave a residual mismatch of the same order as the harvest period and would not resolve the constraint at all. So the frequency and not merely the existence of the mechanism is load-bearing, which the article had not said.

**3. The closure matrix now shows its own gaps.** The cross-sectional scoring was prose. It is now a matrix with two distinct markers, one for cells the configuration renders inapplicable and one for cells the record does not establish. Neither is imputed.

Making it explicit surfaced something the prose concealed. The two failed cases, Iridium and OneWeb, carry the most missing cells. That is exactly the pattern a survivorship problem produces, and the section now says so.

---

## Article Metrics

| Metric | After expansion | After review |
|---|---|---|
| Lines | 950 | 975 |
| Words | ~15,277 | ~15,771 |
| Display equations | 71 | **74** |
| Total reference anchors | 157 | 157 |
| Missing / unused / duplicate anchors | 0 / 0 / 0 | 0 / 0 / 0 |
| Em-dash / en-dash / paren / contraction / colon / semicolon | 0 | 0 |

LaTeX balanced with matched `\left` and `\right` pairs, balanced braces, and matched `array` environments. All macros within the MathJax `tex-mml-chtml` default package set.

---

## Items Requiring Your Attention

1. **74 is above the nominal 60-72 band.** I judged this acceptable because A288 sits at 75, so the observed series range accommodates it, and because each addition carries argument rather than padding. Say the word if you would rather hold the nominal ceiling and I will drop the weakest of the three, which is the closure matrix.

2. **The 2015 round figures do not reconcile.** See addition one above. The article now says so plainly. If you know which reading is correct, that is a one-line fix and would tighten the section.

3. **Reference-density pass is the only remaining item on A290.** 157 anchors against the 190-234 baseline, with books at 54 and research at 31 as the series lows.

4. **Still no build verification, and still none possible.** A290's `post_url` references to unpublished A288 and A289 fail any build by construction. Documented interlock, not a defect.

---

## Suggested Next Steps

- Run the reference-density pass on A290, concentrating on books and research.
- Then A291 Category-Dominating Commercial Spinoff at editorial date 2026-08-03 09:00 UTC.
- Publish A288, A289, and A290 as a batch once all three are at parity.
- Schedule the broken-link sweep across live A281, A282, and A283.
- Decide the scope of the "the specific" remediation. Three unpublished drafts is the cheap containment; the seven live articles are the larger call.
