# Task Log

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

Current task state and verification log. This file is the shared source of truth for the active unit of work.

---

## Current Task

**Name**: Refine Article A93 Terminology and Title (A93-P2)
**Status**: Complete
**Started**: 2026-02-18

## Success Criteria

- [x] Article retitled and file renamed.
- [x] "Commercial Engineering" removed as a primary category.
- [x] Content accurately reflects that FMCG products are durable/patchable, not "throwaway."

## Task Breakdown

| ID | Task | Status | Verification |
|----|------|--------|--------------|
| A93-P2-T1 | Retitle article | Complete | Title changed to "FMCG Versus Mission-Critical Engineering." |
| A93-P2-T2 | Shift terminology to FMCG | Complete | "Commercial Software Engineering" replaced with "FMCG Engineering" as primary term. Justification added for why "commercial" is insufficient. FMCG defined as durable product with low-cost patching infrastructure. |
| A93-P2-T3 | Rename file | Complete | `cost_of_failure_spectrum.markdown` renamed to `fmcg_versus_mission_critical_engineering.markdown` via git mv. |
| A93-P2-T4 | Update process files and commit | Complete | TASKLOG, REVERSE_PROMPT, draft summary updated. |

## Notes

- Article A93, "FMCG Versus Mission-Critical Engineering," dated 2026-02-24, categories: management philosophy.
- References A86 (Mission Command) and A87 (Telemeritocracy) via post_url (both published).
- No publication dependencies on unpublished articles.
- Next available article number: A94.
- 6 release candidates: A88, A89, A90, A91, A92, A93.
- 0 stubs.
- Publication order dependency: A89 before A92. A88, A90, A91, and A93 have no dependencies.

## History

| Date | Change |
|------|--------|
| 2026-02-07 | A0: Knowledge graph, communication protocol, CLAUDE.md, git strategy, article numbering (A1-A74), and asset organization established. |
| 2026-02-07 | A75: "Bidirectional Agentic Workflow" drafted and published (2026-02-06 date). |
| 2026-02-07 | A76: "Markdown as a Specification Language for Agentic Workflows" drafted and published (2026-02-08 date). |
| 2026-02-07 | A77: "LLM Knowledge Graphs" drafted and published (2026-02-07 date, 20 references). |
| 2026-02-08 | A78: "The State of Context Engineering in Early 2026" drafted (30 references) and published (2026-02-09 date). Draft summary created. 16 candidate topics added. |
| 2026-02-08 | A79: "Writing Proofs" drafted (15 references). A80: "Probability and Statistics Reference" drafted (9 references). Both elevated to release candidates. |
| 2026-02-08 | A81: "Magic Cards as a Model of Virtual Goods" drafted (9 references). A82: "Introduction to Astronomy" drafted (8 references). |
| 2026-02-08 | A83: "Safe Embedded Functional Control DSL" drafted (12 references, later revised to 16). A84: "LLM Mad Libs Experiment" drafted (10 references). A85: "The AI Apocalypse Will Be Polite" drafted (11 references). |
| 2026-02-09 | A79-A85 elevated to release candidates. A79 published (2026-02-10 date). A80-A85 release announcements generated. A86 and A87 cataloged as stubs. |
| 2026-02-14 | A88-P1: "The Half-Life Coin" researched and rewritten (13 references). Draft summary synced. |
| 2026-02-14 | A88-P2: Renamed to "Radioactive Half-Life Demurrage Cryptocurrency Coin." Five sections revised. Verification Licensing added. RISC Zero reference added (14 total). Filename convention documented. A86/A87 outlines expanded by human. A89 stub added. |
| 2026-02-14 | A86-P1: "Mission Command Management Style" researched and written (14 references). TASKLOG streamlined. |
| 2026-02-14 | A87-P1: "Telemeritocracy" researched and written (11 references). References A86 via post_url. Draft summary synced (13 files, 3 RCs, 1 stub). |
| 2026-02-15 | A89-P1: "Cryptotelemeritocracy" researched and written (15 references). References A87 via post_url. Draft summary synced (13 files, 4 RCs, 0 stubs). |
| 2026-02-15 | A90-P1: "Introduction to Space Studies" researched and written (18 references). References A82 via post_url. Draft summary synced (13 files, 5 RCs, 0 stubs). |
| 2026-02-14 | A89-P2: "Cryptotelemeritocracy" revised from cryptographic to cryptocratic framing (14 references). Three-layer model with candidate pool, arbitrator powers, strength classifications. Draft summary synced. |
| 2026-02-15 | A89-P3: "Cryptotelemeritocracy" expanded with theory additions (19 references). Oversight vs executive configurations, telos amendment, counter-espionage properties section. Draft summary synced. |
| 2026-02-15 | A91-P1: "Concentrated Liquidity Market Maker Mathematics" researched and written (6 references). Calculator rewritten from JS to Rust WASM. Android FreeBSD drafts combined. Draft summary synced (12 files, 6 RCs, 0 stubs). |
| 2026-02-16 | A91-P2: Renamed exported WASM function from `clmm_calculator_init` to `inject_ui`. Human added index.html local testing example and serve instructions. |
| 2026-02-16 | A0-P3: "Android Development on FreeBSD" modernized from 2017 to 2026 toolchain. A91 WASM assets committed. Draft summary synced. |
| 2026-02-16 | A0-P4: "Getting Started with Claude Code on FreeBSD" drafted (12 references). Ports, packages, npm installation. Hello World curses demo. Draft summary synced. |
| 2026-02-16 | A0-P5: "Getting Started with Claude Code on OpenBSD" drafted (12 references). npm-only installation, bash/ripgrep config, Hello World curses demo. Draft summary synced. |
| 2026-02-16 | A0-P6: "Getting Started with Claude Code Over SSH" drafted (10 references). SSH fundamentals, key auth, remote execution via Bash tool, Desktop SSH. Draft summary synced. |
| 2026-02-16 | A0-P7: "Getting Started with Claude Code Over SSH" revised with agent forwarding section (11 references). Security considerations, ProxyJump alternative. Draft summary synced. |
| 2026-02-16 | A0-P8: "Android Unit Testing" modernized from 2017 stub to contemporary AndroidX Test (12 references). CLMM calculator test subject, Kotlin and Rust implementations, NDK testing section. Draft summary synced. |
| 2026-02-16 | A0-P9: "Phoenix JSON API Authentication with Guardian and Ueberauth" modernized from 2016 to contemporary Phoenix 1.7+/Guardian 2.x (11 references). File renamed. Draft summary synced. |
| 2026-02-16 | A0-P10: "Solana sBPF Assembly Example" finished from partial draft. Rewritten with correct sBPF ISA and sbpf toolchain (9 references). Mixed Rust/assembly state documented. File renamed. Draft summary synced. |
| 2026-02-16 | A0-P11: "Getting Started with Solana Using Rust and Pinocchio" drafted (12 references). Mirrors A65 key pegboard with Pinocchio. Mollusk tests, comparison table. Draft summary synced. |
| 2026-02-16 | A0-P12: "Solana sBPF Assembly Example" revised with .rodata section and linked Rust+ASM object file example (11 references). build.rs with Solana SDK Clang. Draft summary synced. |
| 2026-02-16 | A0-P13: "Solana sBPF Assembly Example" revised with .equ named constants in main.s and log_hello.s. All non-0/1/-1 literals replaced. Draft summary synced. |
| 2026-02-17 | A92-P1: "Cryptotelemeritocracy for Space Exploitation" researched and written (13 references). References A89 and A90 via post_url. Draft summary synced (17 files, 7 RCs, 0 stubs). |
| 2026-02-17 | A92-P2: "Cryptotelemeritocracy for Space Exploitation" revised per subsection notes. Birch Planet, Venus water sourcing, MESSENGER attribution, EROI, reverse conglomerate excess pledges, spinoff independence, telos primacy, memetic governance, MathJax equations. 16 references. Draft summary synced. |
| 2026-02-17 | A92-P3: "Cryptotelemeritocracy for Space Exploitation" revised. Introduction foreshadow, telos hierarchy (13 objectives, 4 categories), Kardashev governance shift, mass driver physics, Mercury cannibalization inflection point, corrected spinoff equations, spinoff shedding reframe, Governance Coherence Half-Life. Draft summary synced. |
| 2026-02-17 | A92-P4: "Cryptotelemeritocracy for Space Exploitation" revised. Corrected $\Delta V_{share}$ formula. Arbitrator profit independence. Latency-meaning-narrative cascade. GCH expanded with glottochronology, punctuated equilibrium, operational 50% divergence. Intergalactic phase reframed as myth-structure to superstition. 4 new references (20 total). Draft summary synced. |
| 2026-02-17 | A92-P5: "Cryptotelemeritocracy for Space Exploitation" corrected Birch Planet cross-reference from objective 8 to objective 6. |
| 2026-02-17 | A86-P2: "Mission Command Management Style" published (2026-02-18 date). Draft summary synced (16 files, 6 RCs, 0 stubs). |
| 2026-02-18 | A87-P2: "Telemeritocracy" published (2026-02-19 date). Fixed post_url hyphen/underscore mismatch in A87 and A89. Software versions date updated. Draft summary synced (15 files, 5 RCs, 0 stubs). |
| 2026-02-18 | A93-P1: "The Cost of Failure Spectrum" researched and written (17 references). Date sync convention documented in POST_STRUCTURE.md. Draft summary synced (16 files, 6 RCs, 0 stubs). |
| 2026-02-18 | A93-P2: Retitled to "FMCG Versus Mission-Critical Engineering." Terminology shifted from "commercial software engineering" to "FMCG Engineering" with justification. File renamed. Draft summary synced. |
