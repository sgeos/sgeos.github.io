# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-06-01
**Task**: A140-P3 Publish "The Money Behind an SBIR or STTR Award" (ninth article of the SBIR/STTR practitioner-playbook series)

---

## Verification

### A140 Published

A140 "The Money Behind an SBIR or STTR Award" published at `_posts/2026-06-23-money_behind_an_sbir_or_sttr_award.markdown` with front-matter date `2026-06-23 09:00:00 +0000`. 18 references across Reference (11), Related Post (4), and Research (3) categories. The ninth article of the SBIR/STTR practitioner-playbook series, the one with arithmetic, in the business/funding/sbir category. References A136, A137, A138, and A112 via `post_url`.

### Framing

The article is about the three things that decide whether an award is worth having, the cost proposal that fits the work into the dollars, the indirect rate that decides how much of the award actually reaches the work, and the cash flow that determines whether a company that won an award can survive it. One idea organizes it, that the award is a fixed pot and the company must justify it in a compliant budget, account for it in a way the government will accept, and finance the gap between spending it and being paid. It is the one article in the series with arithmetic, because the indirect rate is a number and it matters.

### Scope Covered

The cost proposal; direct and indirect costs and the pools; the indirect rate with its rate-equals-pool-over-base relation and its loaded-cost chain, the provisional-versus-negotiated distinction, and the true-up risk; fee and the two contract types and the absence of a cost-share requirement; compliant accounting and the audit standard; allowable and unallowable costs; cash flow with the line of credit and factoring as bridges; the assistance funds; common money mistakes; scale and the UAV case; and Out of Scope.

### Reference and Style Verification

Reference integrity confirmed at 18 of 18 anchors defined and used, zero missing, zero unused, zero duplicate definitions, all cited in the body prose. The eleven Reference Wikipedia URLs and the three Research systems were verified accessible. Prose style confirmed: no contractions, no em-dashes or en-dashes in the body, and no prose colons or semicolons outside the display-math blocks and the console.log debug tag, and mathjax is true because the indirect-rate and loaded-cost relations are quantitative. The fee limit, the rate mechanics, and the cost principles are stated as illustrative and current-as-of, with the cost regulations and the agency instructions named as authoritative, and the loaded-cost chain is flagged as illustrative since its application depends on the company's accounting structure.

### Build Verification

Verified with system Jekyll: the post renders at /business/funding/sbir/2026/06/23/, MathJax is included, the A136 and A137 and A138 and A112 `post_url` links resolve, all 18 reference links resolve, no unresolved link markup remains, and the post appears on the index. The full local bundle build remains broken in this environment; the deploy build runs via the GitHub Actions pipeline after the push.

---

## Release Announcement

New Blog Post: The Money Behind an SBIR or STTR Award

The earlier articles wrote the technical proposal and described the rights the company keeps, and they kept deferring the money. This article is the money, the three things that decide whether an award is worth having.

Key takeaways:
- The award is a fixed pot, and the company must justify it in a compliant budget, account for it in a way the government will accept, and finance the gap between spending it and being paid.
- The indirect rate, the pool of overhead divided by a base, decides how much of a fixed award funds the work and how much covers the company, so a rate set too high prices the company out and one set too low starves it.
- A compliant accounting system that segregates direct from indirect costs and survives an audit is a prerequisite for the cost-reimbursement awards, not an afterthought, and is real early work for a startup.
- Cash flow is the quiet killer, since payment lags the work and a gap falls between phases, so a company can hold a two-million-dollar award and still miss a payroll unless it plans the cash and finances the receivable.

You can read the full article here:
https://sgeos.github.io/business/funding/sbir/2026/06/23/money_behind_an_sbir_or_sttr_award.html

#SBIR #STTR #SmallBusiness #IndirectRate #Accounting #CashFlow #Funding

---

## Action Items for the Human Pilot

- Confirm the 2026-06-23 publication date is as intended. A140 is the ninth article of the SBIR/STTR series, one day after A139.
- A141 (after the award, the compliance, reporting, and audits) is next in the planned thirteen-article series.
- Time-sensitive program facts, the fee limits and rate mechanics and cost principles, must be re-verified against current rules at each draft.

---

## Notes

- Next available article number: A141.
- 0 release candidates.
- 0 new drafts. A108 through A140 published.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification.
- Published: A79 through A140.
- The SBIR/STTR practitioner-playbook series is underway in the new business/funding/sbir category. Published so far: A132 (orientation), A133 (agency survey), A134 (eligibility and the registration stack), A135 (finding a topic and reading a solicitation), A136 (the Phase I proposal), A137 (Phase II and the commercialization plan), A138 (Phase III and the valley of death), A139 (data rights and intellectual property), and A140 (the money). Planned A132 through A144; A141 (after the award) is next. United States programs with one international-analogs article; practitioner playbook; balanced across agencies. The fixed-wing-UAV series and its extensions (A112 through A131) remain complete. No internal research cited; public encyclopedic and authoritative sources only.
- All scratch is confined to project-local `tmp/` per recorded preference. A140 process-file deltas were staged in `tmp/a140/` while drafting and have now been applied directly, so those notes are superseded.
- Blog deploys through GitHub Actions with a lean Jekyll stack; 0 open Dependabot alerts; Keleusma highlighting is live.
