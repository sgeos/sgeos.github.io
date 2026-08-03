# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-02
**Task**: A290 primary-reference expansion pass. 81 primary reference URLs added, 53 to 134. Total anchors 157 to 238. Both above the series baselines.

---

## How the Audit Found the Gaps

I measured primary-reference density per section rather than eyeballing it. Six sections carried **no primary sources at all**:

- Patient Private Capital as an Economic Property
- Cross-Disciplinary Framings
- The January 2015 Google and Fidelity Round
- Dilution Management and Control Preservation
- Deep Historical Comparative Precedents
- Alternative Analytical Frameworks

Every added URL came from the verified sibling corpus rather than being invented, and every one was rechecked by HTTP request before use.

---

## Three Passages That Are Argument, Not Citation

The pass added prose in three places rather than only hanging citations on existing sentences.

**1. The constraint is documentary.** A paragraph in the economic-property section walks the actual apparatus — the Delaware partnership and corporation statutes, the Chancery interpretations of what a partnership agreement may waive, the Advisers Act as amended by Dodd-Frank. The point is that every element of the fund-life constraint sits in a statute, an agreement, or a market convention, and none of it is a property of capital. **That is the article's central claim stated at the level of the record**, which it had asserted but never grounded.

**2. Patience and opacity are the same mechanism.** A comparable transfer in a listed issuer produces a Schedule 13D filing and becomes public. In this arrangement it produces nothing beyond a Form D notice. So the identity and size of incoming buyers are unavailable to any outside party, **including to the selling holders**. The critical literature already in the article treats this as the central objection; the article now concedes it is correct on the facts while disputing that it argues against describing the mechanism accurately.

**3. The finding is jurisdiction-bound.** United Kingdom pre-emption rights constrain the issuance sequence, German codetermination and two-tier boards alter the control calculus, and the European Union Shareholder Rights Directive imposes engagement duties with no United States analogue. A reader applying the pattern outside the United States should expect the control-preservation sub-property to fail for reasons unrelated to financing. The abstract statement concealed this.

A new **Comparative Contemporary Configurations** subsection marks the boundary between the fund-life problem this article treats and the control-allocation problem the commentary conflates with it, covering the OpenAI charter and restructuring, the Anthropic long-term benefit trust, and the listed founder-control comparators.

---

## Article Metrics

| Metric | Before | After |
|---|---|---|
| Lines | 975 | 1,167 |
| Words | ~15,771 | ~18,734 |
| Display equations | 74 | 74 |
| H2 / H3 sections | 27 / 10 | 27 / 11 |
| Book references | 54 | 54 |
| **Primary reference URLs** | **53** | **134** |
| Research references | 31 | 31 |
| Related-post cross-references | 19 | 19 |
| **Total reference anchors** | **157** | **238** |
| Missing / unused / duplicate anchors | 0 / 0 / 0 | 0 / 0 / 0 |
| Duplicate URLs | 0 | 0 |
| Style violations | 0 | 0 |

Primary references at 134 now exceed A289 at 130, the previous series high.

---

## Items Requiring Your Attention

1. **Books at 54 and research at 31 are still the series lows.** A288 carries 116 and 110, A289 carries 123 and 69. You asked specifically for primary references and that is what I did, so this is a deliberate remaining gap rather than an oversight. It is the natural target for the publication-review pass.

2. **Three dead NASA URLs were inherited and repaired.** The Space Act Agreements guide, the CRS-1 award release, and the COTS agreement page all 404. I replaced them with verified NASA programme pages rather than guessing at moved slugs, per the rule that guessing is how fabricated citations enter. The replacements are less specific than what they replace, which is a real if minor loss of citation precision.

3. **One duplicate URL consolidated.** Two Bloomberg anchors shared a host, so the Iridium citation now uses the existing general anchor.

4. **URL sweep results.** All 134 primary URLs checked. 118 confirmed 200. The other 16 are every one a documented bot-detection, paywall, or rate-limit case, not a dead link. I extended `_docs/process/URL_VERIFICATION.md` with the fourteen 403 hosts this series has surfaced and added a new table for 202, 401, 429, and connection-reset responses that are not failures. `blueorigin.com` returns 429 persistently rather than transiently, which is worth knowing before someone concludes it is broken.

5. **Still no build verification and still none possible.** A290's `post_url` references to unpublished A288 and A289 fail any build by construction.

---

## Suggested Next Steps

- Publication-review pass on A290, targeting books and research where the gap now sits.
- Then A291 Category-Dominating Commercial Spinoff at editorial date 2026-08-03 09:00 UTC.
- Publish A288, A289, and A290 as a batch once all three are at parity.
- Schedule the broken-link sweep across live A281, A282, and A283. The three dead NASA URLs repaired here are almost certainly still live in those articles.
- Decide the scope of the "the specific" remediation.
