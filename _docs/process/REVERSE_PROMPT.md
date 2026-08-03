# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-03
**Task**: A291 equation-density expansion pass. 49 display equations added, 26 to 75. Reference-density pass remains.

---

## How the Pass Was Scoped

I measured A290's per-section distribution, which sits at 77 and is at publication-review parity, and matched its shape rather than applying a per-word ratio. The six sections that carry zero equations in every sibling stayed at zero.

| Section | Before | After |
|---|---|---|
| Cross-Disciplinary Framings | 0 | 8 |
| The Commercial Spinoff as an Economic Property | 5 | 7 |
| The Launch-Cadence Coupling | 3 | 5 |
| Vertical Integration and the Internal Transfer Price | 1 | 4 |
| Capital Intensity and the Replenishment Treadmill | 2 | 4 |
| Alternative Analytical Frameworks | 0 | 4 |
| Mapping Problem | 2 | 4 |
| Deep Historical Comparative Precedents | 0 | 3 |
| Remaining narrative and comparison sections | 0 to 2 each | 2 to 3 each |

---

## Six Additions That Carry New Argument

Most of the 49 formalize claims already present. These six change or sharpen something.

1. **Make-or-buy is the wrong test here.** The transaction-cost condition compares internal cost plus governance cost against market price. This case does not turn on that inequality at all. No supplier existed at the required cadence at any price, so the condition is an existence claim rather than a comparison. **The integration would have been correct even had it been more expensive than buying**, which is not the case the literature ordinarily treats.

2. **The spinoff lowers the parent's cost of serving its own external customers.** Spreading fixed cost across more flights drops average cost, so the constellation improves the merchant launch business as a by-product of consuming it. That is the reverse of the resource diversion the diversification literature predicts, and I now treat it as **the strongest single piece of evidence that this is not a diversification**.

3. **Consumer broadband fails the two-sided-market test.** A genuine platform requires each side's utility to rise in the other's participation. For shared-capacity broadband, an additional subscriber weakly *degrades* service. So importing platform pricing conclusions into the broadband business is an error, and only the direct-to-cell service qualifies.

4. **The latency ratio explains the incumbents' non-response.** Low orbit cuts propagation latency by about two orders of magnitude, which moves the service across the threshold where interactive applications become usable. That is a discontinuity in the served application set, not an improvement along an existing dimension — which is why operators optimized for a different design point did not react.

5. **Bring-into-use is a rate requirement, and the option collapses rather than degrades.** The filing's value is an indicator times the protected position, so missing the deadline forfeits it discontinuously. This is the formal core of the spectrum-priority finding and makes it sharper than the prose alone had it.

6. **The treadmill has a favorable side I had not stated.** Uniform replacement fixes the fleet's average age at half a design lifetime, so the constellation is permanently refreshed with current-generation hardware instead of ageing toward obsolescence as a geostationary fleet does. That partially offsets the capital burden the same section describes.

---

## Article Metrics

| Metric | Before | After |
|---|---|---|
| Lines | 796 | 1,013 |
| Words | ~10,203 | ~13,199 |
| **Display equations** | **26** | **75** |
| H2 / H3 sections | 28 / 12 | 28 / 12 |
| Total reference anchors | 173 | 173 |
| Missing / unused / duplicate | 0 / 0 / 0 | 0 / 0 / 0 |
| Duplicate URLs | 0 | 0 |
| Style violations | 0 | 0 |

LaTeX balanced at 32 matched `\left` and `\right` pairs, braces and array environments matched, every macro within the MathJax `tex-mml-chtml` default package set.

---

## Items Requiring Your Attention

1. **Reference-density pass is the remaining item.** 173 anchors against the 190-234 baseline, with books at 46 and research at 39 as the gap.

2. **One equation is an approximation I want flagged.** The coverage-density relation over latitude is a simplified dwell-time expression, correct in form and in its limiting behaviour but not a rigorous derivation of constellation coverage. It is doing illustrative work in explaining why deployment ran high-latitude first, and it should not be read as a design formula.

3. **The publication batch is still four**, A288 through A291, and A288 still carries two of the fabricated citations from the earlier audit.

4. **No build verification is possible** until the batch stages together.

---

## Suggested Next Steps

- Reference-density pass on A291, concentrating on books and research.
- Then A292, the closing article.
- Resolve the citation-integrity remediation before the batch publishes.
- Publish A288 through A291 as a four-article batch.
- Broken-link sweep across live A281, A282, and A283.
- Decide the scope of the "the specific" remediation.
