# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-16
**Task**: A0-P12 Revise Solana sBPF Assembly Example

---

## Verification

### .rodata Section Revision

- Hello World program in `src/main.s` revised to use `.rodata` section.
- String "Hello, sBPF!" declared with `.ascii` directive under a `message:` label.
- `lddw r1, message` loads the 64-bit address of the string into r1.
- Previous stack-based approach (mov32/stxw pattern) replaced entirely.
- Code explanation updated to describe `.rodata`, `.ascii`, and `lddw` instructions.
- Noted that the sbpf assembler supports `.ascii`, `.byte`, `.short`, `.word`, `.int`, `.long`, `.quad` but not `.asciz` or `.string`.

### Linked Rust and Assembly Object File Example

- New subsection "Linking Assembly into a Rust Project with build.rs" added at the end of "Mixed Rust and Assembly Projects."
- Project structure: `src/lib.rs` (Rust entrypoint), `src/log_hello.s` (sBPF assembly), `build.rs`, `Cargo.toml`.
- Assembly function `log_hello` accepts pointer and length arguments, constructs "Hello sBPF from {name}!" on the stack, calls `sol_log_`.
- Callee-saved registers r6-r8 saved on entry and restored before exit.
- 16-byte prefix stored as four little-endian 4-byte words.
- Name bytes copied via a loop using `ldxb`/`stxb` with computed addresses.
- Exclamation mark appended after the name.
- Rust entrypoint uses `#![no_std]`, `#![no_main]`, `extern "C" { fn log_hello(...); }`, passes `b"Rust"`.
- `build.rs` discovers Solana SDK LLVM tools, invokes `clang -target sbf -march=bpfel+solana -c`, archives with `llvm-ar rcs`, emits `cargo:rustc-link-search` and `cargo:rustc-link-lib=static` directives.
- Caveat paragraph clearly states this is a theoretical solution for manual verification.
- Assembly uses Clang syntax with label-based branches.

### References and Prose Updates

- Added `hello-solana-asm` (deanmlittle/hello-solana-asm) as Reference.
- Added `solana-upstream-bpf-template` (solana-developers/solana-upstream-bpf-template) as Reference.
- Total references increased from 9 to 11 across two categories (Reference, Research).
- Opening paragraph updated to mention `.rodata` section and linked object file approach.
- Future Reading updated with hello-solana-asm repository mention.
- Limitation #9 updated to note the `build.rs` theoretical approach alongside sbpf-linker.

---

## Questions for Human Review

- Verify that the sbpf assembler correctly handles the `.rodata` section with `.ascii` directive and `lddw r1, message` address loading. Build and deploy the Hello World program with `sbpf build` and `sbpf deploy`.
- Verify that the `log_hello.s` assembly file assembles correctly with `clang -target sbf -march=bpfel+solana -c`. The Solana SDK's Clang version may differ from upstream LLVM.
- Verify that label-based branches (`jge r8, r7, copy_done` / `ja copy_loop`) work with the Solana SDK's Clang. If not, replace with numeric offsets (`jge r8, r7, +8` / `ja -10`).
- Verify the `build.rs` SDK path `~/.local/share/solana/install/active_release/bin/sdk/sbf/dependencies/platform-tools/llvm/bin`. This assumes the default `solana-install` location.
- Verify that `cargo build-sbf` correctly links the static archive produced by the `build.rs` script. The Solana linker must resolve the `sol_log_` external symbol from the assembly object file.
- Verify that the `extern "C" { fn log_hello(...); }` FFI declaration in the Rust entrypoint matches the assembly function's calling convention for the SBF target.
- Verify that the `custom_panic` handler is required and sufficient for `#![no_std]` programs targeting the Solana runtime via `cargo build-sbf`.
- The `.extern sol_log_` directive in the assembly file declares the syscall as an external symbol. Verify that the Solana linker resolves this during the final linking stage when assembling with Clang rather than the sbpf tool.
- The `Cargo.toml` has no runtime dependencies. Verify that `cargo build-sbf` can produce a valid program binary from a `cdylib` crate with only a raw `entrypoint` function and no `solana-program` dependency.

---

## Notes

- Next available article number: A92.
- 6 release candidates: A86 "Mission Command Management Style," A87 "Telemeritocracy," A88 "Radioactive Half-Life Demurrage Cryptocurrency Coin," A89 "Cryptotelemeritocracy," A90 "Introduction to Space Studies," A91 "Concentrated Liquidity Market Maker Mathematics."
- 0 stubs.
- 8 pre-release candidates: Android Development on FreeBSD, Android Unit Testing, Claude Code on FreeBSD, Claude Code on OpenBSD, Claude Code Over SSH, Phoenix JSON API Authentication with Guardian and Ueberauth, Solana sBPF Assembly Example, Getting Started with Solana Using Rust and Pinocchio.
- Publication order dependency: A86 before A87 before A89. A88, A90, and A91 have no dependencies.
- Publication order dependency: FreeBSD Claude Code article before OpenBSD Claude Code article.
- Publication order dependency: Android FreeBSD article and CLMM Mathematics (A91) before Android Unit Testing article.
- SSH article has no publication dependency on other articles.
- Phoenix Guardian article has no publication dependency on other unpublished articles. References published article A27 via post_url.
- Solana sBPF article has no publication dependency on other unpublished articles.
- Solana Pinocchio article has no publication dependency on other unpublished articles. References published article A65 via post_url.
- A86 publication date: 2026-02-18.
- A88 publication date: 2026-02-17.
- A87 publication date: 2026-02-19.
- A89 publication date: 2026-02-20.
- A90 publication date: 2026-02-21.
- A91 publication date: 2026-02-22.
