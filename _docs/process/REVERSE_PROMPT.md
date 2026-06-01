# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-06-01
**Task**: A141-P3 Publish "After the Award, Compliance and Reporting for SBIR and STTR" (tenth article of the SBIR/STTR practitioner-playbook series)

---

## Verification

### A141 Published

A141 "After the Award, Compliance and Reporting for SBIR and STTR" published at `_posts/2026-06-24-after_the_award_for_sbir_and_sttr.markdown` with front-matter date `2026-06-24 09:00:00 +0000`. 19 references across Reference (11), Related Post (5), and Research (3) categories. The tenth article of the SBIR/STTR practitioner-playbook series, in the business/funding/sbir category. References A134, A136, A139, A140, and A112 via `post_url`.

### Framing

The article is about the second half of the campaign, the part that begins after the win. The earlier articles wrote the proposal and won the award. This article frames the award as a binding agreement with continuing duties, so that winning is the start of an obligation rather than the end of an effort. One idea organizes it, that past performance is built or destroyed during performance, and that the company that reports, invoices, survives audits, and closes out cleanly earns the standing that makes the next award possible.

### Scope Covered

Winning is the start (the award binds, contract or grant); performing and who to talk to (milestones and deliverables, the contracting officer versus the technical point of contact, formal modifications, no-cost extensions, termination for default and for convenience, subcontractor and partner management); reporting (technical progress and final reports, the commercialization report that feeds the benchmarks, the late-report consequences); invoicing and getting paid (the payment systems, the lag); audits and the settling of rates (the Defense Contract Audit Agency, the incurred-cost true-up, the single audit, the audit trail and records retention); compliance and integrity (the certifications, the False Claims Act, debarment, the defense cybersecurity obligation); closing out; continuing standing; scale and the UAV case; and Out of Scope.

### Reference and Style Verification

Reference integrity confirmed at 19 of 19 anchors defined and used, zero missing, zero unused, zero duplicate definitions, all cited in the body prose. The eleven Reference Wikipedia URLs and the three Research systems were verified accessible. Prose style confirmed: no contractions, no em-dashes or en-dashes in the body, and no prose colons or semicolons outside the YAML front matter and the console.log debug tag, and mathjax is false because the article has no equations. All time-sensitive specifics (reporting cadences, audit thresholds, retention periods, the cybersecurity-certification requirement) are flagged as current-as-of, with the award terms and the agency instructions named as authoritative.

### Build Verification

Verified with system Jekyll: the post renders at /business/funding/sbir/2026/06/24/, the A134 and A136 and A139 and A140 and A112 `post_url` links resolve, all 19 reference links resolve, no unresolved link markup remains, and the post appears on the index. The full local bundle build remains broken in this environment; the deploy build runs via the GitHub Actions pipeline after the push.

---

## Release Announcement

New Blog Post: After the Award, Compliance and Reporting for SBIR and STTR

The earlier articles wrote the proposal and won the award. This article is the second half of the campaign, the part that begins after the win, where past performance is built or destroyed.

Key takeaways:
- An award is a binding agreement with continuing duties, so winning is the start of an obligation rather than the end of an effort.
- Two people govern the relationship, the contracting officer who owns the agreement and the technical point of contact who owns the work, and knowing which one to ask for what avoids costly mistakes.
- Reporting is not paperwork, the technical and commercialization reports feed the benchmarks that decide future eligibility, and late reports carry real consequences.
- The company that reports, invoices, survives audits, and closes out cleanly earns the standing that makes the next award possible.

You can read the full article here:
https://sgeos.github.io/business/funding/sbir/2026/06/24/after_the_award_for_sbir_and_sttr.html

#SBIR #STTR #SmallBusiness #Compliance #Auditing #PastPerformance #Funding

---

## Action Items for the Human Pilot

- Confirm the 2026-06-24 publication date is as intended. A141 is the tenth article of the SBIR/STTR series, one day after A140.
- A142 (strategy, the portfolio, transition versus the mill, state and matching funds, the venture bridge) is next in the planned thirteen-article series, then A143 (international analogs) and A144 (the worked-campaign capstone) close it.
- Time-sensitive program facts, the reporting cadences and audit thresholds and the cybersecurity-certification requirement, must be re-verified against current rules at each draft.

---

## Notes

- Next available article number: A142.
- 0 release candidates.
- 0 new drafts. A108 through A141 published.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification.
- Published: A79 through A141.
- The SBIR/STTR practitioner-playbook series is underway in the new business/funding/sbir category. Published so far: A132 (orientation), A133 (agency survey), A134 (eligibility and the registration stack), A135 (finding a topic and reading a solicitation), A136 (the Phase I proposal), A137 (Phase II and the commercialization plan), A138 (Phase III and the valley of death), A139 (data rights and intellectual property), A140 (the money), and A141 (after the award, compliance and reporting). Planned A132 through A144; A142 (strategy) is next, then A143 (international analogs) and A144 (the capstone). United States programs with one international-analogs article; practitioner playbook; balanced across agencies. The fixed-wing-UAV series and its extensions (A112 through A131) remain complete. No internal research cited; public encyclopedic and authoritative sources only.
- All scratch is confined to project-local `tmp/` per recorded preference. A141 process-file deltas were staged in `tmp/a141/` while drafting and have now been applied directly, so those notes are superseded.
- Blog deploys through GitHub Actions with a lean Jekyll stack; 0 open Dependabot alerts; Keleusma highlighting is live.
