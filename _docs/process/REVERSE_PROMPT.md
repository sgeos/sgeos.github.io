# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-06-01
**Task**: A142-P3 Publish "Strategy and the Portfolio of SBIR and STTR Awards" (eleventh article of the SBIR/STTR practitioner-playbook series)

---

## Verification

### A142 Published

A142 "Strategy and the Portfolio of SBIR and STTR Awards" published at `_posts/2026-06-25-strategy_and_the_portfolio_of_sbir_and_sttr_awards.markdown` with front-matter date `2026-06-25 09:00:00 +0000`. 20 references across Reference (11), Related Post (6), and Research (3) categories. The eleventh article of the SBIR/STTR practitioner-playbook series, in the business/funding/sbir category. References A134, A135, A137, A138, A140, and A112 via `post_url`.

### Framing

The article steps back from the single award the earlier articles followed to the company that wins them, and asks what the company is using the awards to become. One idea organizes it, that an award is a means and not an end, and that strategy is the discipline of using a portfolio of non-dilutive awards, staged against the risk reduction the whole series has tracked, to build a company that eventually no longer needs them. The central choice that follows is the one between transition and the mill, between treating the awards as a bridge to a self-sustaining business and treating them as the business itself, and almost every other strategic decision is downstream of it.

### Scope Covered

The award is a means (the strategic frame); transition versus the mill (the central choice, the transition partner who pulls a technology across the valley of death, the sole-source Phase III as a positioned-for asset); the portfolio (diversification across agencies, topics, and customers, sequencing, parallel tracks, the proactive pipeline); stacking the capital (state matching funds, the assistance programs); the private-capital bridge (venture capital, angels, seed, equity dilution, the majority-investor eligibility wrinkle, de-risking the technology for investors); the market beyond the government (dual-use, commercialization, the National Science Foundation seed fund); choosing what to pursue (opportunity cost, the distorting award); scale and the UAV case; and Out of Scope.

### Reference and Style Verification

Reference integrity confirmed at 20 of 20 anchors defined and used, zero missing, zero unused, zero duplicate definitions, all cited in the body prose. The eleven Reference Wikipedia URLs and the three Research portals were verified accessible. The transition-partner concepts (prime contractor, program of record, teaming agreement) are described in prose rather than linked, since each candidate Wikipedia URL was a disambiguation page or a redirect to a generic article and citing it would be semantically loose, consistent with the prose-description practice used for the valley of death and march-in rights. Prose style confirmed: no contractions, no em-dashes or en-dashes in the body, and no prose colons or semicolons outside the YAML front matter and the console.log debug tag, and mathjax is false because the article has no equations. The state programs, the assistance funds, and the investor rules are flagged as current-as-of, with the official portal and the Small Business Administration named as authoritative.

### Build Verification

Verified with system Jekyll: the post renders at /business/funding/sbir/2026/06/25/, the A134 and A135 and A137 and A138 and A140 and A112 `post_url` links resolve, all 20 reference links resolve, no unresolved link markup remains, and the post appears on the index. The full local bundle build remains broken in this environment; the deploy build runs via the GitHub Actions pipeline after the push.

---

## Release Announcement

New Blog Post: Strategy and the Portfolio of SBIR and STTR Awards

The earlier articles followed a single award from the decision to pursue it through winning, financing, and closing it out. This article steps back to the company that wins them, and asks the strategic question the others deferred, what the company is using the awards to become.

Key takeaways:
- An award is a means and not an end, and strategy is using a portfolio of non-dilutive awards, staged against demonstrated risk reduction, to build a company that eventually no longer needs them.
- The central choice is transition versus the mill, between treating the awards as a bridge to a self-sustaining business and treating serial award-winning as the business itself, and the company built to transition can always keep winning while the reverse is not true.
- Transition rarely happens alone, so the company cultivates a transition partner, a prime contractor, an integrator, or a program-office customer who pulls the technology across the valley of death, and that cultivation begins early.
- The awards reduce technical risk cheaply, raising a company's value before it raises private money, so the equity it later gives up to venture capital buys more, and a dual-use technology with a market beyond the government is the most durable position of all.

You can read the full article here:
https://sgeos.github.io/business/funding/sbir/2026/06/25/strategy_and_the_portfolio_of_sbir_and_sttr_awards.html

#SBIR #STTR #SmallBusiness #VentureCapital #Commercialization #DualUse #Funding

---

## Action Items for the Human Pilot

- Confirm the 2026-06-25 publication date is as intended. A142 is the eleventh article of the SBIR/STTR series, one day after A141.
- A143 (the international analogs to these programs) is next in the planned thirteen-article series, then A144 (the worked-campaign capstone reusing the fixed-wing UAV) closes it.
- Time-sensitive program facts, the state programs and assistance funds and investor rules, must be re-verified against current rules at each draft.

---

## Notes

- Next available article number: A143.
- 0 release candidates.
- 0 new drafts. A108 through A142 published.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification.
- Published: A79 through A142.
- The SBIR/STTR practitioner-playbook series is underway in the new business/funding/sbir category. Published so far: A132 (orientation), A133 (agency survey), A134 (eligibility and the registration stack), A135 (finding a topic and reading a solicitation), A136 (the Phase I proposal), A137 (Phase II and the commercialization plan), A138 (Phase III and the valley of death), A139 (data rights and intellectual property), A140 (the money), A141 (after the award), and A142 (strategy and the portfolio). Planned A132 through A144; A143 (international analogs) is next, then A144 (the capstone). United States programs with one international-analogs article; practitioner playbook; balanced across agencies. The fixed-wing-UAV series and its extensions (A112 through A131) remain complete. No internal research cited; public encyclopedic and authoritative sources only.
- All scratch is confined to project-local `tmp/` per recorded preference. A142 process-file deltas were staged in `tmp/a142/` while drafting and have now been applied directly, so those notes are superseded.
- Blog deploys through GitHub Actions with a lean Jekyll stack; 0 open Dependabot alerts; Keleusma highlighting is live.
