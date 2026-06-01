# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-06-01
**Task**: A143-P3 Publish "International Analogs to SBIR and STTR" (twelfth article of the SBIR/STTR practitioner-playbook series, the single dedicated international article)

---

## Verification

### A143 Published

A143 "International Analogs to SBIR and STTR" published at `_posts/2026-06-26-international_analogs_to_sbir_and_sttr.markdown` with front-matter date `2026-06-26 09:00:00 +0000`. 20 references across Reference (11), Related Post (6), and Research (3) categories. The twelfth article of the SBIR/STTR practitioner-playbook series and the one dedicated international article, in the business/funding/sbir category. References A132, A134, A138, A140, A142, and A112 via `post_url`.

### Framing

The article steps outside the United States the rest of the series read from, and surveys the analogs other advanced economies have built. One idea organizes it, that every advanced economy faces the same market failure in early-stage high-risk technology and each has built a public instrument to fund the risk reduction private capital will not, so the analogs are different answers to one shared question rather than copies of a single design. The survey is organized around the structural axes along which the answers differ, the instrument used, whether the money is non-dilutive or dilutive, whether selection is challenge-driven or open, and whether the award is staged or paid in one shot.

### Scope Covered

The common problem (market failure, the valley of death, industrial policy); the procurement copies (the United Kingdom Contracts for Innovation, the Netherlands Innovation Impact Challenge, Australia's Business Research and Innovation Initiative, Canada's Innovative Solutions Canada, Japan's reformed SBIR); the European grant programs (Horizon Europe, the European Innovation Council Accelerator, the Eureka network and Eurostars, Germany's Central Innovation Programme); the research-collaboration analog (the STTR dimension and the consortium default abroad); the tax-credit instrument (Canada's Scientific Research and Experimental Development credit); the state as investor (the Israel Innovation Authority, the European blended grant-plus-equity, South Korea's Tech Incubator Program); defense and dual-use (the North Atlantic Treaty Organization's DIANA); the axes of difference with a 13-program comparison table; scale and the UAV case; and Out of Scope.

### Reference and Style Verification

Reference integrity confirmed at 20 of 20 anchors defined and used, zero missing, zero unused, zero duplicate definitions, all cited in the body prose. The eleven Reference Wikipedia URLs and the three Research portals were verified accessible. All foreign-program facts were verified by web search and flagged current-as-of, since these programs change names and structures often, the United Kingdom and Dutch programs both having been renamed recently. Germany's Central Innovation Programme and South Korea's Tech Incubator Program are described in prose because neither has an English Wikipedia article, consistent with the prose-description practice used for the United Kingdom Small Business Research Initiative and Australia's program. Prose style confirmed: no contractions, no em-dashes or en-dashes in the body, and no prose colons or semicolons outside the YAML front matter, the comparison table, and the console.log debug tag, and mathjax is false because the article has no equations. The comparison table is column-consistent at five columns.

### Build Verification

Verified with system Jekyll: the post renders at /business/funding/sbir/2026/06/26/, the A132 and A134 and A138 and A140 and A142 and A112 `post_url` links resolve, all 20 reference links resolve, the comparison table renders, no unresolved link markup remains, and the post appears on the index. The full local bundle build remains broken in this environment; the deploy build runs via the GitHub Actions pipeline after the push.

---

## Release Announcement

New Blog Post: International Analogs to SBIR and STTR

The series has been a United States playbook. This article steps outside the United States to survey the analogs other advanced economies have built, because the problem the programs solve is not peculiarly American.

Key takeaways:
- Every advanced economy faces the same market failure in early-stage high-risk technology, and each funds the risk reduction the market will not, so the American program is one answer among many rather than a unique invention.
- The United Kingdom, the Netherlands, Australia, Canada, and Japan all built challenge-driven, phased, non-dilutive procurement programs on the American pattern, several of them named or modeled after it directly.
- Other countries chose different instruments, the European grant and its blended grant-plus-equity, the Canadian research tax credit, the Israeli royalty-bearing grant, and the South Korean matching investment, which trade the American combination for a different balance of direction, dilution, and reach.
- The research-institution partnering that distinguishes STTR is, abroad, often the default rather than a separate track, so the staircase from feasibility to prototype to market is the durable idea and the rest is national detail.

You can read the full article here:
https://sgeos.github.io/business/funding/sbir/2026/06/26/international_analogs_to_sbir_and_sttr.html

#SBIR #STTR #InnovationPolicy #HorizonEurope #DeepTech #Funding

---

## Action Items for the Human Pilot

- Confirm the 2026-06-26 publication date is as intended. A143 is the twelfth article of the SBIR/STTR series, one day after A142.
- A144 (the worked-campaign capstone reusing the fixed-wing UAV through Phase I, II, and III) is next and closes the planned thirteen-article series.
- The foreign-program facts are unusually time-sensitive and were web-verified at draft. One detail, South Korea's move to add an STTR-style program, rests on recent reporting and is stated as a recent move rather than an established fact.

---

## Notes

- Next available article number: A144.
- 0 release candidates.
- 0 new drafts. A108 through A143 published.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification.
- Published: A79 through A143.
- The SBIR/STTR practitioner-playbook series is underway in the new business/funding/sbir category. Published so far: A132 (orientation), A133 (agency survey), A134 (eligibility and the registration stack), A135 (finding a topic and reading a solicitation), A136 (the Phase I proposal), A137 (Phase II and the commercialization plan), A138 (Phase III and the valley of death), A139 (data rights and intellectual property), A140 (the money), A141 (after the award), A142 (strategy and the portfolio), and A143 (international analogs). Planned A132 through A144; A144 (the worked-campaign capstone) is next and closes the series. United States programs with one international-analogs article; practitioner playbook; balanced across agencies. The fixed-wing-UAV series and its extensions (A112 through A131) remain complete. No internal research cited; public encyclopedic and authoritative sources only.
- All scratch is confined to project-local `tmp/` per recorded preference. A143 process-file deltas were staged in `tmp/a143/` while drafting and have now been applied directly, so those notes are superseded.
- Blog deploys through GitHub Actions with a lean Jekyll stack; 0 open Dependabot alerts; Keleusma highlighting is live.
