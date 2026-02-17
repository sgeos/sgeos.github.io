# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-16
**Task**: A0-P3 Modernize Android Development on FreeBSD

---

## Verification

### Android Development on FreeBSD Article

- Complete rewrite of `_drafts/android_development_on_freebsd.markdown` from 2017 content (FreeBSD 11, SDK 25, NDK r13b) to modern toolchain (FreeBSD 14, SDK 35, NDK r28).
- Development stack: Kotlin for SDK, Rust for NDK via JNI. Fully native Android app with XML layouts. No WebView, no WASM, no HTML.
- Sample app ports the A91 CLMM calculator to Android. Two JNI functions: `calculateReserves` and `calculateLiquidity`.
- SDK phase: Kotlin Activity with EditText inputs and placeholder buttons. Verifies SDK build pipeline on FreeBSD.
- NDK phase: Rust library with `jni` crate. `cargo-ndk` integrated into Gradle build via custom Exec task.
- 10 references across 4 categories (Android, FreeBSD, Related Post, Rust). All URLs verified.
- Emulator feasibility section documents why the Android emulator is unsupported on FreeBSD.
- No article number assigned. Not slotted for publication. Pre-release candidate status.

### A91 WASM Assets

- `assets/wasm/post_clmm_mathematics/` committed (package.json, .d.ts, .js, .wasm, .wasm.d.ts).

---

## Questions for Human Review

- The `post_url` reference to A91 (`2026-02-22-clmm_mathematics`) assumes A91 will be published with that date and slug. Verify this is correct before publishing the Android article.
- The `sdkmanager` command uses `--sdk_root=$ANDROID_HOME`. Some versions require `--sdk_root` while others use the default. Verify on FreeBSD.
- The `brandelf` step may be unnecessary on FreeBSD 14 with the default ELF fallback brand. The article includes it as a safety measure. Test whether SDK tools work without it.
- The `cargo ndk` integration calls NDK's `clang` through the Linuxulator. Verify this works on FreeBSD 14.
- Build configuration uses AGP 8.9.0, Gradle 8.12.1, Kotlin 2.1.0. Verify these versions resolve and build correctly. AGP 9.0.1 and Gradle 9.3.1 are available if an upgrade is preferred.
- Software Versions section has TODO placeholders. Fill in after running commands on FreeBSD.

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
