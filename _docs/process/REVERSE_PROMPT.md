# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-05-30
**Task**: A111-P2 Publish "Information-Flow Control, A Deep Dive with Keleusma"

---

## Verification

### A111 Published

A111 "Information-Flow Control, A Deep Dive with Keleusma" published at `_posts/2026-05-29-information_flow_control_deep_dive_with_keleusma.markdown` (date `2026-05-29 09:00:00 +0000`, 15 references).

The article already carried the requested `2026-05-29` date, so no content edit was needed. The `git mv` was done manually because `_publish.sh` fails under the macOS BSD `sed`, and the moved file was re-staged so the index carries the correct date.

### Build Verified

The full site builds with no Liquid exceptions. A111's `post_url` links resolve to A109 and A110, and its five Keleusma listings highlight. The article was committed and pushed; the GitHub Actions build deploys it live.

---

## Release Announcement

New Blog Post: Information-Flow Control, A Deep Dive with Keleusma

Most programmers know access control, which decides who may read data. Few know information-flow control, which decides where data may go after it is read. This deep dive covers the theory from Denning's lattice and noninterference through language-based type systems, explains what a first-class language feature catches that taint libraries and newtype wrappers cannot, and shows the mechanics in Keleusma 0.2.0.

Key takeaways:
- A first-class label is a dye, not a fence. It propagates through arithmetic, comparison, and branching, so Keleusma rejects implicit flows that taint libraries miss, and it costs nothing at run time because labels are erased after checking.
- Every release of a secret happens at one auditable operator, declassify, which a reviewer can find by searching for a single keyword.
- The grammar supports label sets and boundary negative labels, the latter stating what a function parameter or data field refuses rather than what a value carries.

You can read the full article here:
https://sgeos.github.io/security/rust/programming/2026/05/29/information_flow_control_deep_dive_with_keleusma.html

#InformationFlowControl #IFC #LanguageSecurity #Keleusma #Noninterference #TypeSystems #Confidentiality

---

## Notes

- Next available article number: A112.
- 0 release candidates.
- 0 new drafts.
- 0 stubs.
- Eight pre-release candidate drafts remain awaiting human verification.
- Published: A79 through A111.
- Blog deploys through GitHub Actions with a lean Jekyll stack; 0 open Dependabot alerts; Keleusma highlighting is live.
