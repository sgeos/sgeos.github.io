# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-16
**Task**: A0-P10 Finish Drafting Solana sBPF Assembly Example

---

## Verification

### Solana sBPF Assembly Example Article

- Complete rewrite from partial draft with x86 assembly (`lea`, `ret`, `%rax`) and `clang -target bpf` build.rs to correct sBPF instruction set and the `sbpf` standalone toolchain.
- File renamed from `solana_bpf_asm_example.markdown` to `solana_sbpf_assembly_example.markdown` via `git mv`.
- Title: "Solana sBPF Assembly Example."
- Front matter: `mathjax: false`, categories `solana assembly`, date `2026-03-01 00:01:00 +0000`.
- Background section covers the sBPF virtual machine as Solana's fork of eBPF, key differences from upstream eBPF, the rBPF Rust implementation, and the `sbf-solana-solana` target triple.
- Registers and Memory subsection with 11-register table (r0-r10 with purposes) and 4-region memory layout table (code, stack, heap, input with base addresses).
- Instruction Set subsection with categorized table covering data movement, wide immediate, memory load/store, arithmetic, bitwise, jumps, branches, function calls, and program exit.
- Instructions section walks through `cargo install sbpf`, `sbpf init`, project structure, Hello World program, `sbpf build`, deployment to local test validator, and `sbpf deploy`.
- Hello World program stores "Hello, sBPF!" on the stack in three 4-byte words using `mov32` and `stxw`, invokes `sol_log_` syscall with pointer and length, exits with return code 0.
- Mixed Rust and Assembly Projects subsection documents the current state: no stable workflow exists. Three experimental paths covered: nightly inline assembly with `asm_experimental_arch`, separate compilation with `sbpf-linker` (proven for C/Nim/Python but untested for Rust), and the `build.rs` approach (analogous to `cc` crate but undocumented for SBF target). Entrypoint conflict between Rust `entrypoint!` macro and hand-written assembly entrypoint documented.
- 9 limitations documented including no signed division, 4KB stack frame limit, 64-frame call depth, CPI depth of 4, bounds-checked memory, no random/network/time access, compute unit budget, determinism requirement, and no stable mixed Rust/assembly workflow.
- 9 references across 2 categories (Reference, Research).
- No article number assigned. Not slotted for publication. `<!-- Axxx -->` placeholder used.

---

## Questions for Human Review

- Software Versions section has TODO placeholders that need to be filled in on the development machine after installing `sbpf` and running the project.
- Verify that `cargo install sbpf` is the correct installation command and that the tool is available on crates.io. The GitHub repository is `blueshift-gg/sbpf`.
- Verify that `sbpf init hello_sbpf` creates the expected project structure with `src/main.s`, `deploy/`, and `Cargo.toml`.
- Verify that the Hello World assembly program assembles, deploys, and logs "Hello, sBPF!" on a local test validator. The little-endian encoding of "Hell" as `0x6c6c6548`, "o, s" as `0x73202c6f`, and "BPF!" as `0x21465042` should be verified.
- Verify that `sol_log_` is the correct syscall name for the sbpf assembler. Some documentation uses `sol_log_` with a trailing underscore and some without.
- Verify that `solana program invoke <PROGRAM_ID>` is the correct command for invoking a deployed program from the CLI.
- The Mixed Rust and Assembly Projects subsection states that `sbpf-linker` has been demonstrated with clana (C), nimlana (Nim), and pylana (Python). Verify these project names are correct.
- The article states the default compute unit budget is 200,000 per instruction. The standard Solana budget is 200,000 per transaction (not per instruction). Verify the correct framing.
- Verify that the `no-entrypoint` Cargo feature is the correct mechanism for suppressing the Rust entrypoint macro in mixed projects.

---

## Notes

- Next available article number: A92.
- 6 release candidates: A86 "Mission Command Management Style," A87 "Telemeritocracy," A88 "Radioactive Half-Life Demurrage Cryptocurrency Coin," A89 "Cryptotelemeritocracy," A90 "Introduction to Space Studies," A91 "Concentrated Liquidity Market Maker Mathematics."
- 0 stubs.
- 7 pre-release candidates: Android Development on FreeBSD, Android Unit Testing, Claude Code on FreeBSD, Claude Code on OpenBSD, Claude Code Over SSH, Phoenix JSON API Authentication with Guardian and Ueberauth, Solana sBPF Assembly Example.
- Publication order dependency: A86 before A87 before A89. A88, A90, and A91 have no dependencies.
- Publication order dependency: FreeBSD Claude Code article before OpenBSD Claude Code article.
- Publication order dependency: Android FreeBSD article and CLMM Mathematics (A91) before Android Unit Testing article.
- SSH article has no publication dependency on other articles.
- Phoenix Guardian article has no publication dependency on other unpublished articles. References published article A27 via post_url.
- Solana sBPF article has no publication dependency on other unpublished articles.
- A86 publication date: 2026-02-18.
- A88 publication date: 2026-02-17.
- A87 publication date: 2026-02-19.
- A89 publication date: 2026-02-20.
- A90 publication date: 2026-02-21.
- A91 publication date: 2026-02-22.
