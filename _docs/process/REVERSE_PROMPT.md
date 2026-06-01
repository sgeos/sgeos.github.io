# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-06-01
**Task**: A134-P3 Publish "SBIR and STTR Eligibility and the Registration Stack" (third article of the SBIR/STTR practitioner-playbook series)

---

## Verification

### A134 Published

A134 "SBIR and STTR Eligibility and the Registration Stack" published at `_posts/2026-06-17-eligibility_and_the_registration_stack_for_sbir_and_sttr.markdown` with front-matter date `2026-06-17 09:00:00 +0000`. 21 references across Reference (13), Related Post (3), and Research (5) categories. The third article of the SBIR/STTR practitioner-playbook series, in the business/funding/sbir category. References A132, A133, and A112 via `post_url`.

### Framing

The article is the gate every applicant passes before it can compete, and it is two gates. Eligibility is a property of the company that is true or false on the day it applies and that the company certifies and re-certifies, and registration is a sequence of federal accounts and identifiers that takes real calendar time to assemble. The practical heart of the article is that second fact, since the registrations take weeks and a company that starts them late will miss a deadline it was otherwise ready to meet.

### Scope Covered

Eligibility (small with affiliation, for-profit, United States, the five-hundred-employee standard, not a socioeconomic set-aside); the ownership rules and the agency-specific investor exception; the principal investigator and the work splits; the performance benchmarks and the duplicate-funding rule; national-security eligibility, the export-control neighbor, and the certification-and-fraud framing; the registration stack in order; why the stack gates the calendar; scale and the small-company case; and Out of Scope.

### Currency and Honesty

The time-sensitive thresholds, the employee standard, the ownership percentages, the investor-exception cap, and the benchmark rates, are stated as current-as-of, with the policy directive, the Small Business Administration size rules, and the live solicitation named as authoritative, since they change with reauthorization. The article also warns that the registrations are free and the government never charges for them, a guard against the third parties that solicit a fee.

### Reference and Style Verification

Reference integrity confirmed at 21 of 21 anchors defined and used, zero missing, zero unused, zero duplicate definitions, all cited in the body prose. The thirteen Reference Wikipedia URLs were verified accessible, and the five Research systems (SAM.gov, Login.gov, the official program portal and company registry, the SBA size-standards page, and the Defense SBIR/STTR Innovation Portal) returned 200. A standalone Unique Entity Identifier article does not exist, so the identifier is described within the System for Award Management treatment, and the thin Login.gov Wikipedia stub was dropped in favor of the actionable live site. Prose style confirmed: no contractions, no em-dashes or en-dashes in the body, and no prose colons or semicolons, the only semicolon being the console.log debug tag, and mathjax is false because the article has no equations.

### Build Verification

Verified with system Jekyll: the post renders at /business/funding/sbir/2026/06/17/, the A132 and A133 and A112 `post_url` links resolve, all 21 reference links resolve, no unresolved link markup remains, and the post appears on the index. The full local bundle build remains broken in this environment; the deploy build runs via the GitHub Actions pipeline after the push.

---

## Release Announcement

New Blog Post: SBIR and STTR Eligibility and the Registration Stack

The agency survey ended on the first strategic choice, which house to knock on. Before a company can knock at all it must pass two gates, eligibility and registration, and this article is about both, the one a property of the company and the other a stack of federal accounts that takes weeks to build.

Key takeaways:
- Eligibility asks whether the company is a genuinely small, American, mostly domestically owned for-profit doing its own research, with a qualifying investigator, a clean enough national-security profile, and a good enough track record if it has one.
- The ownership rules admit an investor exception that some agencies use and some do not, so a company backed by venture or private-equity money may be eligible at one agency and barred at another.
- Eligibility is something the company certifies and re-certifies, so a misstatement is not a clerical slip but exposure under the False Claims Act.
- The registrations take weeks, the validation in the central award system in particular, so they must be started long before a deadline is in view, they are free and the government never charges for them, and a lapsed registration can bar a company that was ready.

You can read the full article here:
https://sgeos.github.io/business/funding/sbir/2026/06/17/eligibility_and_the_registration_stack_for_sbir_and_sttr.html

#SBIR #STTR #SmallBusiness #SAMgov #Eligibility #Registration #Funding

---

## Action Items for the Human Pilot

- Confirm the 2026-06-17 publication date is as intended. A134 is the third article of the SBIR/STTR series, one day after A133.
- A135 (finding a topic and reading a solicitation) is next in the planned thirteen-article series.
- Time-sensitive program facts must be re-verified against current law and the policy directive at each draft, since the program changes with reauthorization.

---

## Notes

- Next available article number: A135.
- 0 release candidates.
- 0 new drafts. A108 through A134 published.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification.
- Published: A79 through A134.
- The SBIR/STTR practitioner-playbook series is underway in the new business/funding/sbir category. Published so far: A132 (orientation), A133 (agency survey), and A134 (eligibility and the registration stack). Planned A132 through A144; A135 (finding a topic and reading a solicitation) is next. United States programs with one international-analogs article; practitioner playbook; balanced across agencies. The fixed-wing-UAV series and its extensions (A112 through A131) remain complete. No internal research cited; public encyclopedic and authoritative sources only.
- All scratch is confined to project-local `tmp/` per recorded preference. A134 process-file deltas were staged in `tmp/a134/` while drafting and have now been applied directly, so those notes are superseded.
- Blog deploys through GitHub Actions with a lean Jekyll stack; 0 open Dependabot alerts; Keleusma highlighting is live.
