# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-06-01
**Task**: A132-P3 Publish "An Introduction to the SBIR and STTR Programs" (first article of the SBIR/STTR practitioner-playbook series)

---

## Verification

### A132 Published

A132 "An Introduction to the SBIR and STTR Programs" published at `_posts/2026-06-15-introduction_to_the_sbir_and_sttr_programs.markdown` with front-matter date `2026-06-15 09:00:00 +0000`. 18 references across Reference (12), Related Post (3), and Research (3) categories. The first article of a new series, the SBIR/STTR practitioner playbook, in a new category cluster (business/funding/sbir). References A93, A112, and A131 via `post_url`.

### Framing

The article opens the new series on the largest United States source of early-stage non-dilutive research funding for small companies, organized around one idea, that the programs are non-dilutive capital staged against demonstrated reduction of risk, a three-step staircase that carries an idea from a feasibility study through a funded prototype to a transition into a product, mapped to the technology readiness level. It is written as a practitioner playbook, and it carries a front caution that these are United States federal programs whose figures and rules change with each reauthorization, so the numbers are current-as-of and the authoritative source is the live solicitation and the current policy directive.

### Scope Covered

A program that runs on reauthorization (the 2025 lapse and the 2026 reauthorization through fiscal year 2031); the core idea (non-dilutive, mission-pulled, the set-aside, the scale of more than four billion dollars a year, America's Seed Fund); the three phases with the technology-readiness-level mapping and the multi-year timeline; SBIR versus STTR; who can compete, with the 2026 national-security screening; the grant-versus-contract distinction; why the money is worth the trouble; what the programs are not; the series ahead; and Out of Scope.

### Time-Sensitivity and Verification of Program Facts

Because the programs are governed by periodic reauthorization, the time-sensitive facts were verified by web search on 2026-06-01: the programs lapsed when their authority expired on 2025-09-30 and were reauthorized in 2026 through fiscal year 2031, and the scale is over four billion dollars a year across roughly four thousand awards. The dollar figures, the set-aside percentages, and the work splits are stated as current-as-of, with the live solicitation and the Small Business Administration policy directive named as authoritative. Every article in this series must re-verify these against current law at draft time.

### Reference and Style Verification

Reference integrity confirmed at 18 of 18 anchors defined and used, zero missing, zero unused, zero duplicate definitions, all cited in the body prose. The Bayh-Dole en-dash title is percent-encoded. The official program portal and the NSF America's Seed Fund page returned HTTP 200, and the Congressional Research Service overview on congress.gov returns the documented government-site 403 to curl and is a valid human-accessible page. Prose style confirmed: no contractions, no em-dashes or en-dashes in the body, and no prose colons or semicolons, the only semicolon being the console.log debug tag, and mathjax is false because the orientation article has no equations.

### Build Verification

Verified with system Jekyll: the post renders at the new /business/funding/sbir/2026/06/15/ permalink for the new series, the A93 and A112 and A131 `post_url` links resolve, all 18 reference links resolve, no unresolved link markup remains, and the post appears on the index. The full local bundle build remains broken in this environment; the deploy build runs via the GitHub Actions pipeline after the push.

---

## Release Announcement

New Blog Post: An Introduction to the SBIR and STTR Programs

The previous series designed a fixed-wing unmanned aircraft from the airframe outward. This new series is about a different layer entirely, the one that pays for the work and carries it to a fielded product, and it opens on the largest source of early-stage non-dilutive research funding for small companies in the United States, the Small Business Innovation Research and Small Business Technology Transfer programs.

Key takeaways:
- The programs are non-dilutive capital staged against demonstrated reduction of risk, a three-step staircase from a feasibility study through a funded prototype to a transition into a product, mapped to the technology readiness level.
- They are creatures of statute that run on periodic reauthorization, and they lapsed as recently as the end of the last fiscal year before being reauthorized through 2031, so the numbers change and must be checked against the current solicitation.
- The money is non-dilutive and mission-pulled, taking no equity and funding work an agency needs, which is why it is often the bridge across the valley of death between a research result and a product.
- This is a practitioner series, and the articles that follow walk the path from surveying the agencies through eligibility, the proposal, the phases, the data rights, the money, and the strategy, to a capstone that funds the aircraft of the previous series.

You can read the full article here:
https://sgeos.github.io/business/funding/sbir/2026/06/15/introduction_to_the_sbir_and_sttr_programs.html

#SBIR #STTR #SmallBusiness #Innovation #NonDilutive #RandD #GovTech #Funding

---

## Action Items for the Human Pilot

- Confirm the 2026-06-15 publication date is as intended. A132 is the first article of the new SBIR/STTR series, one day after the final fixed-wing-UAV article.
- The series is planned as thirteen articles, A132 through A144: orientation (this one), agency survey, eligibility and registration, topic and solicitation, the Phase I proposal, Phase II and the commercialization plan, Phase III and the valley of death, data rights, the money, after the award, strategy, international analogs, and a worked-campaign capstone. A133 (the agency survey) is next.
- Time-sensitive program facts must be re-verified against current law and the policy directive at each draft, since the program changes with reauthorization.

---

## Notes

- Next available article number: A133.
- 0 release candidates.
- 0 new drafts. A108 through A132 published.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification.
- Published: A79 through A132.
- The fixed-wing-UAV series and its extensions are complete (A112, A114, A116, A118, A120, A121, A122, A123, A124, A125 plus A126 through A131). A132 opens a new series, the SBIR/STTR practitioner playbook, in the new business/funding/sbir category, planned as A132 through A144. United States programs with one international-analogs article; practitioner playbook; balanced across agencies. No internal research cited; public encyclopedic and authoritative sources only.
- All scratch is confined to project-local `tmp/` per recorded preference. A132 process-file deltas were staged in `tmp/a132/` while drafting and have now been applied directly, so those notes are superseded.
- Blog deploys through GitHub Actions with a lean Jekyll stack; 0 open Dependabot alerts; Keleusma highlighting is live.
