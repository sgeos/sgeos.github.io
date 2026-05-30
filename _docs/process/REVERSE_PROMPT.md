# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-05-30
**Task**: A110-P1 Draft "Getting Started with Keleusma 0.2.0"

---

## Verification

### A110 Researched and Written

A110 "Getting Started with Keleusma 0.2.0" drafted at `_drafts/keleusma_0_2_0_getting_started.markdown`.

**Genre**: Tutorial getting-started. Updates the 0.1.1 article (A107) for the 0.2.0 public release.
**References**: 20, all linked inline with a categorized References section. Integrity 20/20, zero missing, zero unused.
**Cross-links**: A107 and A109 via post_url. Links the 40-chapter guide and specific guide chapters for deep dives.
**Categories**: rust embedded programming. Date 2026-05-30 (placeholder, set at publication).

### Every Example Tested

All code was tested against the installed `keleusma 0.2.0`, not assumed from the V0.2.1-WIP repo guide. Tested scripts and the embedding cargo project live in `tmp/a110/` (gitignored). Captured outputs:

- First program, values, text, decisions, repetition, structs, multiheaded with guard, pipeline, traits, newtype refinement, information-flow labels, checked arithmetic all run and produce the outputs shown in the article.
- Verifier rejections are demonstrated as real errors: a refinement that provably fails, an information-flow leak, and a recursive function rejected by the WCMU analysis.
- The `yield` and `loop` examples compile and pass the verifier; the 0.2.0 CLI does not drive their resume protocol, so the article presents them as host-driven and shows the compile step. This is stated honestly.
- The signed-module flow (keygen, compile with signing key, run with verifying key) was run end to end, including the refusal when the key is absent.
- The Rust embedding example was built and run against the crates.io `keleusma 0.2.0` crate and printed `script returned 42`.

### Build Verified

Simulating the published state (the draft copied into `_posts`, built without `--drafts`), the site built cleanly: 17 highlighted `keleusma` blocks plus the `rust` embedding block, and both post_url links resolve to A107 and A109. The temporary copy was removed.

Note: a `--drafts` build of the whole site currently fails, but not because of A110. The eight pre-release-candidate drafts reference each other through post_url and those companions are unpublished, so Jekyll cannot resolve them while they remain drafts. A110's own links resolve.

---

## Release Announcement (Pending Publication)

New Blog Post: Getting Started with Keleusma 0.2.0

Keleusma is a total functional stream-processing language that compiles to bytecode and proves, before a program runs, that every turn finishes within bounded time and bounded memory. Version 0.2.0 is the first public release line, adding cryptographic module signing, information-flow labels, and newtypes with refinement predicates. This article is a practical, fully tested tour: installation, the language, the verifier guarantees, signed modules, and embedding the runtime in a Rust host.

Key takeaways:
- The language omits unbounded loops and recursion by design, and the verifier rejects any program whose time and memory bounds it cannot prove, which the article demonstrates with a rejected recursive function.
- 0.2.0 adds refinement types that reject out-of-range values at compile time, information-flow labels with an auditable declassify gate, and Ed25519-signed modules.
- Keleusma is meant to be embedded. A ten-line Rust host compiles and runs a script through the call-and-resume protocol.

This draft is awaiting human review. Regenerate the announcement with the live URL at publication time.

---

## Notes

- Next available article number: A111.
- 0 release candidates.
- 1 new draft (A110, awaiting human review).
- 0 stubs.
- Eight pre-release candidate drafts remain awaiting human verification.
- Published: A79 through A109.
- Blog deploy now runs through GitHub Actions with a lean Jekyll stack; 0 open Dependabot alerts; Keleusma highlighting is live.
