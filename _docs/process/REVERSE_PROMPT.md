# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-02
**Task**: A290 equation-density expansion pass. 41 display equations added, 30 to 71, bringing the absolute count into the 60-72 series band. Reference-density pass remains.

---

## How the Pass Was Scoped

I measured the per-section equation distribution of A289, which sits at 73 and is at publication-review parity, and matched its shape rather than applying a uniform per-word ratio. The series holds absolute counts, so a ratio would have overshot.

The six sections that carry zero equations in every sibling stayed at zero. Those are Methodological Commitments, Historiographical Gap, Data Sources, Cross-References, Terminological Note, and Load-Bearing Open Questions.

| Section | Before | After |
|---|---|---|
| Cross-Disciplinary Framings | 2 | 8 |
| Fund-Life Constraint | 3 | 6 |
| Patient Private Capital as an Economic Property | 5 | 7 |
| Tender-Offer Mechanism | 2 | 5 |
| Mapping Problem | 2 | 4 |
| Alternative Analytical Frameworks | 0 | 4 |
| Deep Historical Comparative Precedents | 0 | 3 |
| Contemporary Comparative Landscape | 0 | 2 |
| Remaining narrative and negation sections | 1 to 2 each | 2 to 3 each |

---

## Five Additions That Carry New Argument

These are not restatements of adjacent prose. Each changes or sharpens a claim, and they are the ones worth your eye.

1. **The binding clock is not the fund life.** Formalizing the three channels separately gives a minimum over the contractual term and the fundraise cycle, and the fundraise cycle wins at three to four years against ten. The channel that actually binds is the one the partnership agreement does not mention. That upgrades the article's complaint about the commentary from a simplification to a substantive error.

2. **The minimum governs, not the average.** The draft argued the investor base broadened toward longer-lived vehicles and computed a weighted average. The weighted average is the wrong statistic. A single holder reaching its term generates a realization demand regardless of everyone else's horizon, so the binding quantity is the minimum remaining term across the base. **This is the addition I think matters most**, because it explains why the tender mechanism is necessary rather than merely convenient. Broadening the base does not relieve the pressure, since adding a perpetual holder leaves the minimum unchanged.

3. **The duration condition is a clock, not a threshold.** Remaining vehicle life declines at unit rate while the required holding period does not, so a fund that comfortably satisfied the condition at entry violates it later with no change in the venture, the investor's view, or the schedule.

4. **The carry is discounted, not merely deferred.** Present-valuing it shows a general partner can rationally prefer an earlier realization at a lower valuation whenever valuation growth trails the discount rate. Conviction does not touch that.

5. **The mechanism is not a hedge.** The state-dependence identity sets the availability indicator equal to the indicator of improving prospects. A hedge pays in the adverse state. This is unavailable in it. That states the limitation you flagged as formally as it can be stated.

---

## Article Metrics

| Metric | Before | After |
|---|---|---|
| Lines | 770 | 950 |
| Words | ~11,668 | ~15,277 |
| Display equations | 30 | **71** |
| H2 / H3 sections | 27 / 10 | 27 / 10 |
| Total reference anchors | 157 | 157 |
| Missing / unused / duplicate anchors | 0 / 0 / 0 | 0 / 0 / 0 |
| Duplicate URLs | 0 | 0 |
| Em-dash / en-dash / paren / contraction / colon / semicolon | 0 | 0 |

LaTeX balanced at 64 matched `\left` and `\right` pairs with balanced braces. Every macro used was checked against the MathJax `tex-mml-chtml` default package set, which is what this site loads. Nothing requires a package the site does not have.

---

## Items Requiring Your Attention

1. **Reference-density pass is the remaining item on A290.** 157 anchors against the 190-234 baseline. Books at 54 and research at 31 are the series lows and are where the gap sits.

2. **New prose was written at ordinary phrasing density.** Per your direction the "the specific" question waits for its own pass, so I did not add to the problem while working inside the article. New passages therefore read slightly cleaner than their surroundings. The remediation pass will normalize both, so this should not need separate handling.

3. **Two process-file defects found and repaired.** The TASKLOG History table had a duplicated header and five byte-identical duplicate rows covering A287 through A290. Removed. The A288 and A289 history entries recorded pre-publication-review counts as final metrics, understating them at 260 and 203 anchors against the actual 349 and 341. Corrected to agree with `draft_summary.md` and with the files themselves.

4. **No build verification was run and none is possible yet.** A290 back-references A288 and A289 by `post_url` and both are unpublished, so any build fails by construction until the batch stages together. This is the documented interlock, not a defect. Build verification belongs at publication.

5. **The publication batch is still three.** A288, A289, and A290 publish together or in strict order. A288 has zero missing `post_url` targets, so the batch is publishable in that order once A290 reaches parity.

---

## Suggested Next Steps

- Run the reference-density pass on A290, concentrating on books and research where the gap is widest.
- Then A291 Category-Dominating Commercial Spinoff at editorial date 2026-08-03 09:00 UTC. A290 forward-references it as the retained-earnings channel that ultimately displaces the need for the patient-private leg.
- Publish A288, A289, and A290 as a batch once all three are at parity, which clears the sequencing constraint in one step.
- Schedule the broken-link sweep across A281, A282, and A283, which remain live with dead reference URLs.
- Decide the scope of the "the specific" remediation. The three unpublished drafts are the cheap containment; the seven live articles are the larger call.
