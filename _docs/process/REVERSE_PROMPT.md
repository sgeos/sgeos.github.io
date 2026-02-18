# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-18
**Task**: A93-P2 Refine Article A93 Terminology and Title

---

## Verification

### Title and Filename

- Title changed from "The Cost of Failure Spectrum" to "FMCG Versus Mission-Critical Engineering."
- File renamed from `cost_of_failure_spectrum.markdown` to `fmcg_versus_mission_critical_engineering.markdown` via git mv.

### Terminology Shift

- "FMCG Engineering" (Fast-Moving Consumer Goods Engineering) is now the primary term throughout the article.
- "Commercial software engineering" is retained as a near-equivalent academic term in the FMCG Engineering subsection, with explicit justification for why it is insufficient. The dichotomy applies to hobbyist projects, volunteer efforts, and open-source software where "commercial" implications do not fit.
- FMCG Engineering defined as a mode where the product is durable but the infrastructure allows for low-cost patching, meaning a poor quality MVP still yields positive value through feedback.
- All 18 occurrences of "commercial" as an engineering mode label replaced with "FMCG" throughout the article body, conclusion, and future reading sections.
- Two correct uses of "commercial" retained: "commercial airliners" (aviation term) and the justification paragraph explaining why "commercial software engineering" is insufficient.

### Draft Summary

- Updated: title, filename, topic description, and summary section reflect new FMCG terminology.

---

## Questions for Human Review

- The article now uses "FMCG Engineering" consistently as the primary term. Review the justification paragraph in the FMCG Engineering subsection for accuracy and tone.
- The Sommerville reference still links to the author's Wikipedia page (no dedicated book page exists). This was noted in A93-P1 and remains unchanged.

---

## Notes

- Next available article number: A94.
- 6 release candidates: A88 "Radioactive Half-Life Demurrage Cryptocurrency Coin," A89 "Cryptotelemeritocracy," A90 "Introduction to Space Studies," A91 "Concentrated Liquidity Market Maker Mathematics," A92 "Cryptotelemeritocracy for Space Exploitation," A93 "FMCG Versus Mission-Critical Engineering."
- 0 stubs.
- 8 pre-release candidates: Android Development on FreeBSD, Android Unit Testing, Claude Code on FreeBSD, Claude Code on OpenBSD, Claude Code Over SSH, Phoenix JSON API Authentication with Guardian and Ueberauth, Solana sBPF Assembly Example, Getting Started with Solana Using Rust and Pinocchio.
- Publication order dependency: A89 before A92. A88, A90, A91, and A93 have no dependencies.
