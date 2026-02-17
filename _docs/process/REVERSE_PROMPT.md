# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-16
**Task**: A0-P8 Modernize Android Unit Testing

---

## Verification

### Android Unit Testing Article Modernization

- Complete rewrite from 2017 stub (SDK 25, Java 1.8, ApplicationTestCase) to contemporary toolchain (SDK 35, JDK 17, Kotlin 2.1.0, AGP 8.9.0).
- Test subject is the CLMM calculator app with both Kotlin and Rust native implementations.
- `ClmmCalculator.kt` provides pure Kotlin computation with `computeReserves` and `computeLiquidity` functions.
- `MainActivity.kt` uses ClmmCalculator with standard XML layout views.
- Rust `lib.rs` mirrors the Kotlin computation for native deployment.
- Test Dependencies section explains JUnit 4.13.2, AndroidX Test 1.7.0, Robolectric 4.16.1, MockK 1.14.9, Espresso 3.7.0.
- Local Unit Tests section includes `ClmmCalculatorTest.kt` with 8 test methods covering three price regimes, edge cases, and round-trip verification.
- Robolectric Tests section includes `MainActivityTest.kt` with 4 test methods using `ActivityScenario` and `AndroidJUnit4` runner.
- Mocking section demonstrates MockK's `mockkObject` for Kotlin object declarations.
- Instrumented Tests section includes `MainActivityInstrumentedTest.kt` with 2 Espresso test methods.
- NDK Unit Testing section has three subsections.
- Rust Unit Tests subsection shows `#[cfg(test)] mod tests` with 8 test functions using `cargo test`.
- Testing the JNI Boundary subsection documents two approaches: instrumented tests from Kotlin and host JVM tests with host-compiled library.
- GoogleTest for C++ subsection shows CMakeLists.txt integration and adb push/shell workflow.
- Running Tests section provides Gradle task reference table and command-line patterns.
- Code Coverage section covers JaCoCo, Kover, and cargo-llvm-cov.
- Limitations section documents 7 specific constraints.
- MathJax enabled for CLMM reserve formulas in Test Subject section.
- 12 references across 4 categories (Android, Reference, Related Post, Rust).
- All existing content replaced. No content preserved from 2017 draft.

---

## Questions for Human Review

- The test expected values use a delta of 0.01 for floating-point comparisons. Verify that the reserve and liquidity computations produce results within this tolerance by running the CLMM calculator or checking against the WASM widget.
- The `NativeBridgeTest.kt` declares `external fun` methods directly in the test class rather than loading them from `MainActivity`. Verify that the JNI function name convention `Java_com_example_clmm_NativeBridgeTest_calculateReserves` matches the Rust `extern "system"` function names, or adjust the JNI bridge to match.
- The Robolectric tests use `ActivityScenario.launch(MainActivity::class.java)` which requires the XML layout file referenced by `setContentView(R.layout.activity_main)`. The layout XML from the Android FreeBSD article is assumed but not reproduced in this article. Verify that the reader can find it via the cross-reference.
- The host JVM JNI testing approach (`-Djava.library.path=rust/target/debug`) assumes the Rust library compiles for the host with `cargo build`. Verify that the library name (`libclmm.so` on Linux, `libclmm.dylib` on macOS) matches what `System.loadLibrary("clmm")` expects.
- The `app/build.gradle.kts` includes a `buildRustLib` task that runs `cargo ndk`. This task will fail if the Rust toolchain and Android NDK are not configured. For readers who only want to test the Kotlin layer, consider whether the build file should conditionally skip this task.
- Software Versions section has TODO placeholders that need to be filled in on the development machine.
- The article references the Android FreeBSD article via `post_url`. This article must be published before the unit testing article, or the reference must be removed.

---

## Notes

- Next available article number: A92.
- 6 release candidates: A86 "Mission Command Management Style," A87 "Telemeritocracy," A88 "Radioactive Half-Life Demurrage Cryptocurrency Coin," A89 "Cryptotelemeritocracy," A90 "Introduction to Space Studies," A91 "Concentrated Liquidity Market Maker Mathematics."
- 0 stubs.
- 5 pre-release candidates: Android Development on FreeBSD, Android Unit Testing, Claude Code on FreeBSD, Claude Code on OpenBSD, Claude Code Over SSH.
- Publication order dependency: A86 before A87 before A89. A88, A90, and A91 have no dependencies.
- Publication order dependency: FreeBSD Claude Code article before OpenBSD Claude Code article.
- Publication order dependency: Android FreeBSD article and CLMM Mathematics (A91) before Android Unit Testing article.
- SSH article has no publication dependency on other articles.
- A86 publication date: 2026-02-18.
- A88 publication date: 2026-02-17.
- A87 publication date: 2026-02-19.
- A89 publication date: 2026-02-20.
- A90 publication date: 2026-02-21.
- A91 publication date: 2026-02-22.
