# Task Log

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

Current task state and verification log. This file is the shared source of truth for the active unit of work.

---

## Current Task

**Name**: Revise Solana sBPF Assembly Example (A0-P12)
**Status**: Complete
**Started**: 2026-02-16

## Success Criteria

- [x] ASM uses `.rodata` section with `lddw` address loading.
- [x] Linked object file example with Rust entrypoint passing "Rust" to ASM logging subroutine.
- [x] ASM subroutine logs "Hello sBPF from Rust!" using sol_log_ syscall.
- [x] `build.rs` demonstrates Solana SDK Clang and llvm-ar pipeline.
- [x] New references folded in.

## Task Breakdown

| ID | Task | Status | Verification |
|----|------|--------|--------------|
| A0-P12-T1 | Revise Hello World to use .rodata | Complete | Replaced stack-based string storage with `.rodata` section. `lddw r1, message` loads address. `.ascii` directive stores bytes. Code explanation updated. |
| A0-P12-T2 | Add linked Rust+ASM subsection | Complete | New subsection "Linking Assembly into a Rust Project with build.rs" at end of Mixed Rust and Assembly Projects. log_hello.s with callee-saved register management, byte copy loop, sol_log_ call. Rust entrypoint with extern "C" FFI. build.rs with Solana SDK tool discovery. Cargo.toml. Caveat paragraph. |
| A0-P12-T3 | Update references and prose | Complete | Added hello-solana-asm and solana-upstream-bpf-template references (11 total). Updated opening paragraph, Future Reading, and limitation #9. |
| A0-P12-T4 | Verify reference URLs | Complete | 2 new URLs verified. |
| A0-P12-T5 | Update process files and commit | Complete | TASKLOG, REVERSE_PROMPT, draft summary updated. |

## Notes

- No article number assigned per PROMPT.md directive. Not slotted for publication.
- Linked object file example is a theoretical solution for manual verification.
- Next available article number: A92.
- 6 release candidates: A86, A87, A88, A89, A90, A91.
- 0 stubs.

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
