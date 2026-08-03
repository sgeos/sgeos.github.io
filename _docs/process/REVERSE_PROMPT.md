# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-03
**Task**: A291 primary-reference expansion pass. 59 primary reference URLs added, 68 to 127. Total anchors 173 to 232.

---

## How the Audit Found the Gaps

I measured primary-reference density per section. Seven carried **no primary sources at all**:

- The Category-Dominating Spinoff Mapping Problem
- The Commercial Spinoff as an Economic Property
- Cross-Disciplinary Framings
- Capital Intensity and the Replenishment Treadmill
- Comparative Cross-Sectional Analysis
- Data Sources and Reconstruction Methodology
- Alternative Analytical Frameworks

Every added URL came from the verified sibling corpus and was rechecked by HTTP request before use.

---

## Two Placements That Changed the Argument

Most of the 59 attach sources to claims already made. These two altered what the article says.

**1. The short satellite lifetime is partly a compliance cost, not purely a commercial choice.** Placing the orbital-debris mitigation regime behind the design decision made the connection visible. A low-orbit constellation satisfies post-mission disposal expectations most cheaply by operating where drag performs the disposal without a dedicated manoeuvre.

That has an uncomfortable consequence for the article's own structure. **The replenishment treadmill I treat as the spinoff's principal structural liability is in part the price of the mitigation practice I credit the operator for.** The two sections were making opposing points about the same design decision without acknowledging each other. They now do.

**2. The insurance market does not solve the congestion externality.** I placed the Liability Convention, the federal indemnification regime, and the commercial underwriting market behind the externality section, expecting them to qualify the common-pool claim. They do not. Each instrument responds to a **realized loss** rather than to an **increment in risk**, so none of them prices the marginal congestion an additional satellite imposes. The externality survives the existence of an active risk-transfer market, which is a stronger version of the claim than the section previously made.

---

## Article Metrics

| Metric | Before | After |
|---|---|---|
| Lines | 1,013 | 1,137 |
| Words | ~13,199 | ~14,839 |
| Display equations | 75 | 75 |
| Book references | 46 | 46 |
| **Primary reference URLs** | **68** | **127** |
| Research references | 39 | 39 |
| Related-post cross-references | 20 | 20 |
| **Total reference anchors** | **173** | **232** |
| Missing / unused / duplicate | 0 / 0 / 0 | 0 / 0 / 0 |
| Duplicate URLs | 0 | 0 |
| Style violations | 0 | 0 |

Primary references at 127 are comparable to A289 at 130 and A290 at 134. All three reference blocks verified alphabetical.

---

## Items Requiring Your Attention

1. **Books at 46 and research at 39 are the remaining gap.** A288 carries 116 and 110, A290 carries 106 and 72. You asked specifically for primary references, so this is deliberate rather than an oversight, and it is the target for the publication-review pass.

2. **Three dead inherited URLs were dropped rather than replaced.** The Journal of Space Law, the NASA technical standard for orbital debris, and the McGill space-law publication list all 404. None was load-bearing, and guessing at replacements is how the fabricated citations in the published articles got there. Dropping was the safer call.

3. **Two Starship anchors shared a URL** and were consolidated.

4. **URL sweep.** All 127 primary URLs checked. **Zero 404s.** 106 confirmed 200; the other 21 are documented bot-detection, paywall, or rate-limit hosts. I extended `URL_VERIFICATION.md` with eight new ones observed here, including the Federal Communications Commission and the Financial Accounting Standards Board.

5. **The publication batch is still four**, and A288 still carries two fabricated citations from the earlier audit.

---

## Suggested Next Steps

- Publication-review pass on A291, targeting books and research where the gap now sits.
- Then A292, the closing article.
- Resolve the citation-integrity remediation before the batch publishes.
- Publish A288 through A291 as a four-article batch.
- Broken-link sweep across live A281, A282, and A283.
- Decide the scope of the "the specific" remediation.
