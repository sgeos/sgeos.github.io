# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-16
**Task**: A0-P13 Add Named Constants to Solana sBPF Assembly Example

---

## Verification

### Named Constants in main.s (sbpf tool syntax)

- Two `.equ` constants defined at the top of the file with inline `#` comments.
- `MESSAGE_LEN` = 12, the byte length of "Hello, sBPF!".
- `SUCCESS` = 0, the return code for successful program execution.
- `mov64 r2, MESSAGE_LEN` replaces `mov64 r2, 12`.
- `mov64 r0, SUCCESS` replaces `mov64 r0, 0`.
- Code explanation updated with a new first point describing the `.equ` directive, GAS syntax, and SCREAMING_SNAKE_CASE convention.

### Named Constants in log_hello.s (Clang syntax)

- Fifteen `.equ` constants defined at the top of the file, grouped by purpose with inline comments.
- Return codes: `SUCCESS` = 0.
- Callee-saved register save slots: `SAVE_R6` = -8, `SAVE_R7` = -16, `SAVE_R8` = -24.
- Message prefix words: `MESSAGE_0` = 0x6c6c6548 ("Hell"), `MESSAGE_1` = 0x4273206f ("o sB"), `MESSAGE_2` = 0x66204650 ("PF f"), `MESSAGE_3` = 0x206d6f72 ("rom ").
- Message suffix and length: `MESSAGE_4` = 0x21 ("!"), `BASE_MESSAGE_LEN` = 17.
- Stack buffer layout: `PREFIX_OFFSET` = -88, `PREFIX_OFFSET_4` = -84, `PREFIX_OFFSET_8` = -80, `PREFIX_OFFSET_12` = -76, `NAME_OFFSET` = -72.
- All non-0/1/-1 numeric literals replaced with named constants.
- Memory operands use `[r10+CONSTANT]` form where the assembler evaluates negative constant values.
- Explanation prose updated to describe the constant groups and usage pattern.

---

## Questions for Human Review

- Verify that the sbpf assembler correctly resolves `.equ` constants in immediate operands like `mov64 r2, MESSAGE_LEN`. The sbpf CPI example confirms `.equ` usage, but not with `mov64` specifically.
- Verify that Clang's eBPF assembler correctly resolves `.equ` constants with negative values in memory operands. The form `[r10+SAVE_R6]` where `SAVE_R6 = -8` should evaluate to `[r10-8]`, but this depends on the assembler's expression evaluator. The sbpf tool examples only show positive `.equ` values in memory operands.
- Verify that `.equ` constants defined before `.globl` and the function label are visible within the function body for both the sbpf assembler and Clang. GAS convention places `.equ` definitions before their use, which this code follows.
- The inline comment syntax `.equ NAME, value # comment` follows GAS convention. Verify that both the sbpf assembler and Clang accept `#` comments on `.equ` lines.
- All prior verification questions from A0-P12 remain applicable regarding the linked object file example, `.rodata` usage, and build.rs pipeline.

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
