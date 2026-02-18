# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-18
**Task**: A87-P2 Publish Telemeritocracy

---

## Verification

### Publication

- A87, "Telemeritocracy," published to `_posts/2026-02-19-telemeritocracy.markdown`.
- Date: 2026-02-19. Categories: management philosophy.
- Software versions date updated from `2026-02-14 23:42:34 +0000` to `2026-02-18 15:58:18 +0000`.
- Fixed post_url reference mismatch: `mission-command-management-style` (hyphens) changed to `mission_command_management_style` (underscores) in A87 (4 occurrences) and A89 (1 occurrence). The published A86 file uses underscores, and Jekyll's `post_url` tag requires an exact slug match.
- Draft summary updated: 15 files, 5 RCs, 0 stubs.
- A89 (Cryptotelemeritocracy) dependency on A87 is now satisfied.

---

## Release Announcement

New Blog Post: Telemeritocracy

Mission command tells you how to delegate. But who should hold authority in the first place, and on what basis? This article proposes an answer.

Telemeritocracy is a governance model that synthesizes telocracy and meritocracy. Authority is assigned to those who have demonstrated the ability to advance the organization's defined purpose. The model is not new in practice, but the explicit synthesis reveals structural properties that neither telocracy nor meritocracy exhibits alone.

Key takeaways:
- Telemeritocracy grounds authority in demonstrated ability to advance a defined purpose, distinguishing it from both generic meritocracy and purpose-blind credentialism.
- Historical precedents in Apache, IETF, and academic shared governance show the model works at scale, while Valve's flat structure illustrates what happens when merit is decoupled from purpose.
- Five failure modes, from Goodhart's Law gaming to informal hierarchy formation, define the boundaries where the model breaks down and where additional governance mechanisms are needed.

You can read the full article here:
https://sgeos.github.io/management/philosophy/2026/02/19/telemeritocracy.html

Let me know your thoughts. I would love to hear about how your organization balances purpose and competence when assigning authority!

#Telemeritocracy #Governance #Leadership #Management #Engineering #Meritocracy #OrganizationalDesign

---

## Questions for Human Review

- Verify the post_url fix. The published A86 filename uses underscores (`mission_command_management_style`), so all `post_url` references must also use underscores. Four occurrences in A87 and one in A89 were corrected. A92 does not reference A86 directly.

---

## Notes

- Next available article number: A93.
- 5 release candidates: A88 "Radioactive Half-Life Demurrage Cryptocurrency Coin," A89 "Cryptotelemeritocracy," A90 "Introduction to Space Studies," A91 "Concentrated Liquidity Market Maker Mathematics," A92 "Cryptotelemeritocracy for Space Exploitation."
- 0 stubs.
- 8 pre-release candidates: Android Development on FreeBSD, Android Unit Testing, Claude Code on FreeBSD, Claude Code on OpenBSD, Claude Code Over SSH, Phoenix JSON API Authentication with Guardian and Ueberauth, Solana sBPF Assembly Example, Getting Started with Solana Using Rust and Pinocchio.
- Publication order dependency: A89 before A92. A88, A90, and A91 have no dependencies.
- Publication order dependency: FreeBSD Claude Code article before OpenBSD Claude Code article.
- Publication order dependency: Android FreeBSD article and CLMM Mathematics (A91) before Android Unit Testing article.
- A88 publication date: 2026-02-17.
- A89 publication date: 2026-02-20.
- A90 publication date: 2026-02-21.
- A91 publication date: 2026-02-22.
- A92 publication date: 2026-02-23.
