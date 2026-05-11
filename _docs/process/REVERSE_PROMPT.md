# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-03-14
**Task**: A107-P1 Draft A107

---

## Verification

### A107 Drafted (Unpublished)

A107 "Getting Started with Keleusma 0.1.1" drafted at `_drafts/keleusma_getting_started.markdown`. Left unpublished per convention.

**Final draft**: 928 lines, 27 references (17 Reference, 1 Related Post, 3 Research, 6 Future Reading).

**Dates set:**
- Front matter date: `2026-03-14 10:31:00 +0000`.
- Software versions date: matching.

**Links verified:**
- One post_url reference: A68 Getting Started with no_std Rust Programming.
- Resolves to file in `_posts/`.
- All 27 reference link usages matched to 27 URL definitions. Zero missing. Zero unused.

**Examples verified:**
- All 8 example scripts from `~/projects/rust/keleusma/examples/scripts/` executed successfully via `keleusma run`.
- Output matched expected values: 24, 7, 100, 40, 169, 11, "hello, Keleusma! 7 plus 2 is 9", 84.

### Process Files Updated

- TASKLOG.md: current task updated to A107-P1, history entry added.
- draft_summary.md: A107 entry added as New Draft with line count and reference count. File count updated to 12.
- REVERSE_PROMPT.md: overwritten with draft verification and freeform commentary.

---

## Release Announcement

Not generated. A107 left unpublished. Release announcement will be generated when A107 is published.

---

## Freeform Commentary

This article is a departure from the aerospace and von Neumann probe content of the A98-A106 articles. It returns to the blog's Rust and embedded programming thread. The cross-reference to A68 "Getting Started with no_std Rust Programming" is appropriate because Keleusma targets the same no_std + alloc embedded environment that A68 introduces.

The article is structured as a practical tutorial rather than a conceptual exploration. Each section introduces a language feature with minimal prose and a complete code example. The examples are drawn directly from the Keleusma repository's example scripts and have been verified against the actual CLI runner. The outputs (24, 7, 100, 40, 169, 11, "hello, Keleusma! 7 plus 2 is 9", 84) match the repository's expected values.

The three-function-kind taxonomy is the most important conceptual contribution of the article. Most programming languages have a single function concept. Keleusma's division into atomic total, non-atomic total, and productive divergent functions directly encodes the verification guarantees into the type system. Each kind has different obligations and different capabilities. This taxonomy is what makes static WCET analysis tractable without requiring the full apparatus of dependent types or interactive theorem provers.

The embedding section is deliberately detailed because embedding is the primary use case for the language. Keleusma is not designed to be used standalone. It is designed to be embedded in Rust host applications that provide domain-specific native functions. The audio natives, the KeleusmaType derive macro, and the hot code swapping interface are all host-facing features that only make sense in the context of a larger application.

One concern is version mismatch. The locally installed CLI reports version 0.1.0, but the Cargo.toml in the repository declares version 0.1.1. The article is titled "Getting Started with Keleusma 0.1.1" per the crates.io release. The human pilot should verify that version 0.1.1 is installed before final publication, or rebuild from source with `cargo install --path keleusma-cli --bin keleusma`.

The reference count of 27 is lower than the probe series articles but appropriate for a getting-started tutorial. The 17 Reference links cover Wikipedia articles for general concepts. The 3 Research links cite the three foundational papers most relevant to Keleusma's design: Turner's total functional programming paper, Rutten's universal coalgebra paper, and Wilhelm et al.'s WCET survey. The 6 Future Reading entries point to the Keleusma documentation directory and the Rust Embedded Book.

---

## Questions for Human Review

- The locally installed `keleusma` CLI reports version 0.1.0. The Cargo.toml declares 0.1.1. The human pilot should rebuild from source (`cargo install --path keleusma-cli --bin keleusma`) to match the article title before publication.
- The article uses a code fence language annotation of plain (no language specified) for Keleusma source code. If a custom syntax highlighter is available or desired, the fences could be annotated with a language identifier.
- The crates.io URL (https://crates.io/crates/keleusma) was not verified via HTTP due to bot detection. The human pilot should confirm the crate page is live.
- The docs.rs URL (https://docs.rs/keleusma) is listed in the Cargo.toml but not referenced in the article. The human pilot may wish to add it.
- Eight pre-release candidate drafts remain awaiting human verification.

---

## Notes

- Next available article number: A108.
- 0 release candidates.
- 1 new draft (A107).
- 0 stubs.
- Eight pre-release candidate drafts remain awaiting human verification.
- Published: A79 through A106.
