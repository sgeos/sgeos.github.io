# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-05-31
**Task**: A119-P1 Publish "Three Audiences for an Operating System"

---

## Verification

### A119 Published

A119 "Three Audiences for an Operating System" published at `_posts/2026-05-22-three_audiences_for_an_operating_system.markdown` with front-matter date `2026-05-22 09:00:00 +0000`. 1,364 lines. 61 references across Reference (58) and Related Post (3) categories.

### Backdating and Series Order

The article is dated 2026-05-22 per the human pilot's explicit instruction, slotting one day before A113 (2026-05-23). The series now reads as a four-part progression in publication date order: A119 (category) → A113 (design space) → A115 (substrate) → A117 (illustrative vertical). Article number A119 is preserved per POST_STRUCTURE.md's policy that out-of-order article numbering relative to publication date is acceptable.

### Function in the Series

A119 establishes the operator-as-end-user category as distinct from the consumer and the developer. It does not propose a solution. The Out of Scope section explicitly defers the substantive design to A113, the language substrate to A115, and the worked vertical example to A117. The trilogy is the substantive answer; A119 is the prequel that names the question.

### Research

A focused research agent verified the operator-specific standards (ISA-101, ASM Consortium, IEC 62366, ISO 9241, NUREG-0700, ARINC 661), the HCI canon (Norman, Shneiderman, Engelbart, Sutherland, Kay), operator-domain examples (SCADA, ERAM, glass cockpit, control room, human-in-the-loop, alarm fatigue), and the audience-contrast sources (Apple HIG, Microsoft Windows UX Guidelines, Unix philosophy, GNOME HIG, KDE HIG). Three URLs that returned 404 (All-Source Analysis System, Mission Management Center, NUREG-0700 attempted Wikipedia entries) were dropped from the article and the prose reworked to use only verifiable sources. NUREG-0700's nrc.gov page returns 000 to curl due to Cloudflare bot protection, documented in project memory as expected for several .gov sites; the URL is correct and works in browsers.

### Build Verification

Local Jekyll build remains broken in this environment (gem environment issue, documented in earlier history entries). Build verification depends on the GitHub Actions deployment pipeline after the push.

---

## Release Announcement

New Blog Post: Three Audiences for an Operating System

An operating system serves people. The shipping operating systems of 2026 serve two audiences well, namely the consumer and the developer, and a third audience poorly or not at all. This article identifies the three audiences, sketches what each requires, and observes that the operator-as-end-user has not had a contemporary general-purpose operating system designed for the role. The article does not propose a solution; that is the work of the BTRON-hypermedia trilogy A113, A115, and A117 that follow this one in publication date order.

Key takeaways:
- The consumer audience is served correctly by the file-and-application mass-market answer. The developer audience is served correctly by the Unix-derived developer-workstation answer. The operator audience is served by industry-specific systems that do not share a general-purpose operating system layer.
- The operator's load-bearing concept is written external authority. A flight controller, a radiologist, a power dispatcher, an air traffic controller, a chemical plant operator, an intelligence analyst, a legal reviewer, and a financial trading floor all operate under written procedures, rules, and certifications. The system's job is to make the admissible action easy and the inadmissible action either impossible or audited.
- The consumer answer fails the operator on five structural axes: the application owns the file, the interface is optimised for casual use, latency is best-effort, provenance is bolted on, and the trust model is per-user-account rather than per-information-part.
- The developer answer fails the operator on four structural axes: the tools are oriented toward authoring rather than operation, the trust model is per-source-commit rather than per-information-part, the latency model is best-effort, and the display is tuned to source code rather than to typed information.
- The operator population is in the millions, spans aerospace, medical, industrial, defense, intelligence, legal, regulatory, and financial markets, and has a combined budget in the tens of billions of US dollars annually. The category is real, the gap is real, and the engineering components to fill it all exist.

You can read the full article here:
https://sgeos.github.io/operating-systems/philosophy/hci/2026/05/22/three_audiences_for_an_operating_system.html

#OperatingSystems #BTRON #Hypermedia #HCI #ISA101 #IEC62366 #ARINC661 #NUREG0700 #ASMConsortium

---

## Notes

- Next available article numbers: A118 (reserved for the other session) and A120.
- 0 release candidates.
- 0 new drafts. A79 through A117 plus A119 published.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification.
- Published: A79 through A117 plus A119.
- The BTRON-hypermedia four-part series is now complete: A119 (category) → A113 (design space) → A115 (substrate) → A117 (vertical example). Each article cites the others via post_url. The detailed link store design, the certification path, the contractor selection, and other deferred topics remain available as future posts.
- All scratch is confined to project-local `tmp/` per recorded preference.
- Blog deploys through GitHub Actions with a lean Jekyll stack; 0 open Dependabot alerts; Keleusma highlighting is live.
