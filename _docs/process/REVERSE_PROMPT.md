# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-16
**Task**: A91-P2 Fix A91 Widget Source Code

---

## Verification

### A91 Widget Fix

- Root cause: the Rust source exported `clmm_calculator_init` but the user's `index.html` imported `inject_ui`.
- Fix: renamed the `#[wasm_bindgen]` function from `clmm_calculator_init` to `inject_ui`.
- Updated in 4 locations: live script tag, Rust function definition, Widget JS Injection Anchor Example, all now consistent with the user's `index.html` example.
- Human additions preserved: `index.html` local testing example and sample serve command.

---

## Questions for Human Review

- None. The fix is a straightforward function rename.

---

## Notes

- Next available article number: A92.
- 6 release candidates: A86 "Mission Command Management Style," A87 "Telemeritocracy," A88 "Radioactive Half-Life Demurrage Cryptocurrency Coin," A89 "Cryptotelemeritocracy," A90 "Introduction to Space Studies," A91 "Concentrated Liquidity Market Maker Mathematics."
- 0 stubs.
- Publication order dependency: A86 before A87 before A89. A88, A90, and A91 have no dependencies.
- A86 publication date: 2026-02-18.
- A88 publication date: 2026-02-17.
- A87 publication date: 2026-02-19.
- A89 publication date: 2026-02-20.
- A90 publication date: 2026-02-21.
- A91 publication date: 2026-02-22.
