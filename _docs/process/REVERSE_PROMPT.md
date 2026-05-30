# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-05-30
**Task**: A110-P2 Publish "Getting Started with Keleusma 0.2.0"

---

## Verification

### A110 Published

A110 "Getting Started with Keleusma 0.2.0" published at `_posts/2026-05-28-keleusma_0_2_0_getting_started.markdown` (date `2026-05-28 09:00:00 +0000`, 20 references).

The front-matter date and the Software Versions timestamp were set to the requested `2026-05-28`. The `git mv` was done manually because `_publish.sh` fails under the macOS BSD `sed`, and the moved file's edited content was re-staged so the index carries the correct date.

### Build Verified

The full site builds with no Liquid exceptions. A110's `post_url` links resolve to A107 and A109, and its Keleusma and Rust code blocks highlight. The article was committed and pushed; the GitHub Actions build deploys it live.

---

## Release Announcement

New Blog Post: Getting Started with Keleusma 0.2.0

Keleusma is a total functional stream-processing language that compiles to bytecode and proves, before a program runs, that every turn finishes within bounded time and bounded memory. Version 0.2.0 is the first public release line, adding cryptographic module signing, information-flow labels, and newtypes with refinement predicates. This article is a practical, fully tested tour: installation, the language, the verifier guarantees, signed modules, and embedding the runtime in a Rust host.

Key takeaways:
- The language omits unbounded loops and recursion by design, and the verifier rejects any program whose time and memory bounds it cannot prove, demonstrated with a rejected recursive function.
- 0.2.0 adds refinement types that reject out-of-range values at compile time, information-flow labels with an auditable declassify gate, and Ed25519-signed modules.
- Keleusma is meant to be embedded. A short Rust host compiles and runs a script through the call-and-resume protocol.

You can read the full article here:
https://sgeos.github.io/rust/embedded/programming/2026/05/28/keleusma_0_2_0_getting_started.html

#Keleusma #Rust #EmbeddedSystems #ProgrammingLanguages #Bytecode #WCET #TotalFunctional #InfoFlowControl

---

## Notes

- Next available article number: A111.
- 0 release candidates.
- 0 new drafts.
- 0 stubs.
- Eight pre-release candidate drafts remain awaiting human verification.
- Published: A79 through A110.
- Blog deploys through GitHub Actions with a lean Jekyll stack; 0 open Dependabot alerts; Keleusma highlighting is live.
