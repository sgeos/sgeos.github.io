# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-06-01
**Task**: A133-P3 Publish "A Survey of the SBIR and STTR Agencies" (second article of the SBIR/STTR practitioner-playbook series)

---

## Verification

### A133 Published

A133 "A Survey of the SBIR and STTR Agencies" published at `_posts/2026-06-16-survey_of_the_sbir_and_sttr_agencies.markdown` with front-matter date `2026-06-16 09:00:00 +0000`. 25 references across Reference (16), Related Post (3), and Research (6) categories. The second article of the SBIR/STTR practitioner-playbook series, in the business/funding/sbir category. References A132, A93, and A112 via `post_url`.

### Framing

The article is the map of the participating agencies, since the first strategic choice an applicant makes is which agency to approach. It is organized on two independent axes, the award vehicle, whether an agency funds the work as a grant or buys it as a procurement contract, and the topic, whether an agency directs the work or accepts open proposals. The agencies populate the corners, the mission agencies on contracts against directed topics toward a government user and the science agencies on grants against open topics toward the market, with the Department of Energy and the smaller agencies filling the corners between.

### Scope Covered

The two axes and where the agencies sit; how many agencies and why the sizes differ; the Department of Defense, the National Institutes of Health, the National Science Foundation, the Department of Energy, and NASA each in turn; the smaller agencies grouped; a comparison table on the vehicle, topic, STTR, Direct to Phase II, relative size, and character; choosing where to apply by mission and by model, with eligibility, cadence, and post-award support as cross-cutting factors; and Out of Scope.

### Balance and Currency

The survey is balanced across the agencies per the series plan, treating the five largest in their own sections and grouping the six smaller ones, and it draws one authoritative portal per major agency as a Research source. All the time-sensitive specifics, the budgets, the cadences, and the component rosters, are stated in general terms and as current-as-of, with the live solicitation named as the authority, the same discipline the series carries throughout because the program changes with reauthorization.

### Reference and Style Verification

Reference integrity confirmed at 25 of 25 anchors defined and used, zero missing, zero unused, zero duplicate definitions, all cited in the body prose. The sixteen Reference Wikipedia URLs (the twelve agencies, DARPA, AFWERX, and the federal-grants and government-procurement articles) and the six Research portals (the Defense SBIR/STTR Innovation Portal, NIH SEED, the Department of Energy SBIR page, the NASA SBIR/STTR page, the NSF America's Seed Fund, and the official sbir.gov portal) were verified accessible. Prose style confirmed: no contractions, no em-dashes or en-dashes in the body, and no prose colons or semicolons, the only semicolon being the console.log debug tag, and mathjax is false because the survey has no equations.

### Build Verification

Verified with system Jekyll: the post renders at /business/funding/sbir/2026/06/16/, the comparison table renders, the A132 and A93 and A112 `post_url` links resolve, all 25 reference links resolve, no unresolved link markup remains, and the post appears on the index. The full local bundle build remains broken in this environment; the deploy build runs via the GitHub Actions pipeline after the push.

---

## Release Announcement

New Blog Post: A Survey of the SBIR and STTR Agencies

The orientation article said the programs are one program run in many houses. This article is the map of those houses, because the first strategic choice an applicant makes is which agency to approach, and that choice turns on matching the work to the agency whose mission and whose model fit it.

Key takeaways:
- The agencies differ on two independent axes, whether they fund research as a grant or buy it as a contract, and whether they direct the topics or accept open proposals, and they populate the corners.
- The Department of Defense and the National Institutes of Health are the giants, the one a contract-and-directed mission agency transitioning work to a military user, the other a grant-and-open science agency funding a company's own health innovation.
- The National Science Foundation is the open door for broad deep technology through its project pitch, the Department of Energy the grant-but-directed home tied to the national labs, and NASA the contract-and-directed home for space and aeronautics.
- Choosing the right house, by the mission the technology serves and the model the agency uses, and accounting for the agency's eligibility rules and its calendar, is the first strategic act of a campaign.

You can read the full article here:
https://sgeos.github.io/business/funding/sbir/2026/06/16/survey_of_the_sbir_and_sttr_agencies.html

#SBIR #STTR #SmallBusiness #Innovation #DoD #NIH #NSF #Funding

---

## Action Items for the Human Pilot

- Confirm the 2026-06-16 publication date is as intended. A133 is the second article of the SBIR/STTR series, one day after A132.
- A134 (eligibility and the registration stack) is next in the planned thirteen-article series.
- Time-sensitive program facts must be re-verified against current law and the policy directive at each draft, since the program changes with reauthorization.

---

## Notes

- Next available article number: A134.
- 0 release candidates.
- 0 new drafts. A108 through A133 published.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification.
- Published: A79 through A133.
- The SBIR/STTR practitioner-playbook series is underway in the new business/funding/sbir category. Published so far: A132 (orientation) and A133 (agency survey). Planned A132 through A144; A134 (eligibility and the registration stack) is next. United States programs with one international-analogs article; practitioner playbook; balanced across agencies. The fixed-wing-UAV series and its extensions (A112 through A131) remain complete. No internal research cited; public encyclopedic and authoritative sources only.
- All scratch is confined to project-local `tmp/` per recorded preference. A133 process-file deltas were staged in `tmp/a133/` while drafting and have now been applied directly, so those notes are superseded.
- Blog deploys through GitHub Actions with a lean Jekyll stack; 0 open Dependabot alerts; Keleusma highlighting is live.
