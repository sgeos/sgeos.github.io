# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-05-30
**Task**: A111-P1 Draft "Information-Flow Control, A Deep Dive with Keleusma"

---

## Verification

### A111 Researched and Written

A111 "Information-Flow Control, A Deep Dive with Keleusma" drafted at `_drafts/information_flow_control_deep_dive_with_keleusma.markdown`.

**Genre**: Deep dive. Theory of information-flow control, what first-class IFC does that alternatives cannot, and a mechanical section on the Keleusma grammar.
**References**: 15, all linked inline with a References section. Integrity 15/15, zero missing, zero unused.
**Cross-links**: A109 and A110 via post_url.
**Categories**: security rust programming. Date 2026-05-29 (placeholder, set at publication).

### Theory Verified, Examples Tested

The IFC literature was verified by web search before citing: Denning's lattice model (1976) and certification (1977), Goguen and Meseguer on noninterference (1982), Volpano, Smith, and Irvine's type system (1996), the Sabelfeld and Myers survey (2003), Myers and Liskov's decentralized label model and Jif, and Sabelfeld and Sands on declassification (2009).

Every Keleusma listing was run with `keleusma 0.2.0` and the shown output is actual output. Tested scripts live in `tmp/a111/` (gitignored). Confirmed behavior:

- `classify` adds a label; a labelled value reaching a plain parameter is rejected at compile time.
- Labels propagate through arithmetic, comparison, and branching, so an implicit flow (a public value computed on branches selected by a secret) is rejected. This is the article's centerpiece and is the case taint libraries typically miss.
- `declassify` is the single auditable release point.
- Label sets `@{A, B}` and boundary-only negative labels `@!Label` work, the latter with a diagnostic that names the forbidden label.

### Build Verified

Simulating the published state, the site built cleanly: the five Keleusma listings highlight and both post_url links resolve to A109 and A110.

---

## Release Announcement (Pending Publication)

New Blog Post: Information-Flow Control, A Deep Dive with Keleusma

Most programmers know access control, which decides who may read data. Few know information-flow control, which decides where data may go after it is read. This deep dive covers the theory from Denning's lattice and noninterference through language-based type systems, explains what a first-class language feature catches that taint libraries and newtype wrappers cannot, and shows the mechanics in Keleusma 0.2.0.

Key takeaways:
- A first-class label is a dye, not a fence. It propagates through arithmetic, comparison, and branching, so Keleusma rejects implicit flows that taint libraries miss, and it costs nothing at run time because labels are erased after checking.
- Every release of a secret happens at one auditable operator, declassify, which a reviewer can find by searching for a single keyword.
- The grammar supports label sets and boundary negative labels, the latter stating what a function parameter or data field refuses rather than what a value carries.

This draft is awaiting human review. Regenerate the announcement with the live URL at publication time.

---

## Notes

- Next available article number: A112.
- 0 release candidates.
- 1 new draft (A111, awaiting human review).
- 0 stubs.
- Eight pre-release candidate drafts remain awaiting human verification.
- Published: A79 through A110.
- Blog deploys through GitHub Actions with a lean Jekyll stack; 0 open Dependabot alerts; Keleusma highlighting is live.
