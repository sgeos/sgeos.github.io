# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-18
**Task**: A93-P1 Document Date Sync and Draft Cost of Failure Spectrum

---

## Verification

### Date Sync Convention

- Added paragraph to `_docs/writing/POST_STRUCTURE.md` in the Software Versions Format section.
- Convention: the `date -u` output in Software Versions must match the front matter `date:` field. Run `date -u`, update Software Versions output, and set front matter date to the same timestamp before publication.

### Article A93

- "The Cost of Failure Spectrum" drafted at `_drafts/cost_of_failure_spectrum.markdown`.
- 718 lines, 17 references across 5 categories (Book, Reference, Related Post, Research).
- Date: 2026-02-24. Categories: management philosophy.
- Conventional terminology: "commercial software engineering" (Sommerville, academic) for the user's "FMCG Engineering" concept. "Lean product development" (Ries, practitioner) acknowledged as a related framework.
- Core insight framed as cost of failure spectrum: whether a poor quality MVP has positive or negative value determines the engineering mode.
- Sections: Opening prose, Software Versions, The Dichotomy, Why "Cost of Failure" Not "Speed vs Quality", Established Frameworks, The Hybrid Pattern, Mindset Mismatch, Conclusion, Future Reading, References.
- References A86 (Mission Command) and A87 (Telemeritocracy) via post_url (both published).
- No publication dependencies on unpublished articles.

### URL Verification

- 17 URLs verified. Wikipedia pages all confirmed indexed.
- Sommerville book Wikipedia URL returned 404 (no dedicated page exists). Replaced with Ian Sommerville (software engineer) author page.
- MIT Press (Leveson) and Gartner (Bimodal) returned 403 (bot detection, consistent with known academic publisher patterns).
- All other URLs returned 200 or 302 (redirect, normal).

### Draft Summary

- Updated: 16 files, 6 RCs, 0 stubs.
- A93 entry added with full description.

---

## Questions for Human Review

- The Sommerville reference now links to the author's Wikipedia page rather than a dedicated book page (which does not exist). Verify this is acceptable, or suggest an alternative URL such as the publisher's page or Goodreads.
- Review the article's treatment of "commercial software engineering" as the conventional term. The user's original framing as "FMCG Engineering" has no established equivalent. Sommerville's critical systems taxonomy is the closest academic framework.

---

## Notes

- Next available article number: A94.
- 6 release candidates: A88 "Radioactive Half-Life Demurrage Cryptocurrency Coin," A89 "Cryptotelemeritocracy," A90 "Introduction to Space Studies," A91 "Concentrated Liquidity Market Maker Mathematics," A92 "Cryptotelemeritocracy for Space Exploitation," A93 "The Cost of Failure Spectrum."
- 0 stubs.
- 8 pre-release candidates: Android Development on FreeBSD, Android Unit Testing, Claude Code on FreeBSD, Claude Code on OpenBSD, Claude Code Over SSH, Phoenix JSON API Authentication with Guardian and Ueberauth, Solana sBPF Assembly Example, Getting Started with Solana Using Rust and Pinocchio.
- Publication order dependency: A89 before A92. A88, A90, A91, and A93 have no dependencies.
- Publication order dependency: FreeBSD Claude Code article before OpenBSD Claude Code article.
- Publication order dependency: Android FreeBSD article and CLMM Mathematics (A91) before Android Unit Testing article.
