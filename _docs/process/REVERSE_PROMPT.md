# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-05-30
**Task**: A109-P1 Draft A109 (Keleusma control-kernel companion to A108)

---

## Verification

### A109 Written and Examples Verified

A109 "A Verifiable Control Kernel in Keleusma for a Truthful-Machine Architecture" drafted at `_drafts/verifiable_control_kernel_in_keleusma.markdown`.

**Genre**: Tutorial. Companion to A108. Implements the deterministic control-and-governance kernel of the truthful-machine blueprint in Keleusma V0.2.0.
**References**: 9 (1 Crate, 1 GitHub, 1 Guide, 4 Reference, 2 Related Post). Integrity 9/9, zero missing, zero unused.
**Cross-links**: A108 and A107 via post_url.
**Categories**: ai rust programming.

### Method and Evidence

I first reviewed Keleusma V0.2.0 in `/Users/bsechter/projects/rust/keleusma` (workspace at 0.2.1, the 0.2.0 line tagged, CHANGELOG and guide chapters read). The review concluded that Keleusma is a strong fit for the control and governance kernel of the A108 design and a deliberate non-fit for the neural and formal-prover layers.

I then drafted seven example scripts in `tmp/a108/` (gitignored scratch) and verified each with `keleusma 0.2.0`:

- `01_typed_claims.kel` runs and prints `64`.
- `01b_typed_claims_reject.kel` is rejected at compile time (refinement provably fails for `Confidence(150)`).
- `02_route.kel` runs and prints `1`.
- `03_fact_gate.kel` runs and prints `42`.
- `03b_fact_gate_leak.kel` is rejected at compile time (information-flow type error on `Word@Unverified`).
- `04_controller_tick.kel` (yield) and `05_controller_loop.kel` (loop) pass the verifier via `keleusma compile`.

Every output quoted in the article is the actual captured output.

### Honest Limitation Found and Documented

The installed 0.2.0 CLI runner does not yet drive the yield/loop resume protocol, and `shell::exit` is not available in it. The guide documents a tick-counter driver that this build does not implement. The article therefore shows the `yield` and `loop` controllers via `keleusma compile`, which proves they lex, type-check, and pass the bounded-execution verifier, and states plainly that driving them to completion requires the embedding host rather than the stock CLI. This was surfaced rather than hidden.

### Scope Discipline

Per the subject matter, the article is explicit that it implements the kernel only. The proposer, critics, retrieval, calibrator, and formal prover are out of scope and unbuildable in Keleusma, and the article says so. Nothing claims a working truthful machine.

### Publication Dependency (action needed before publishing)

A109 links to A108 via `post_url`. A108 must be published first. The A108 `post_url` target date embedded in A109 is `2026-05-30`; if A108 is published on a different date, update the `related_post_truthful_machine` reference in A109 to match. Until A108 is published, `_preview.sh` and `jekyll build` will fail to resolve the A108 link.

### Process Files Updated

- TASKLOG.md: current task A109-P1, history entry added, next available advanced to A110.
- draft_summary.md: A109 entry added, counts updated to 13 files and 2 new drafts, dependency recorded.
- REVERSE_PROMPT.md: overwritten with this summary.

---

## Notes

- Next available article number: A110.
- 0 release candidates.
- 2 new drafts (A108 and A109, awaiting human review). A109 depends on A108 publishing first.
- 0 stubs.
- Eight pre-release candidate drafts remain awaiting human verification.
- Published: A79 through A107.
- Verified Keleusma example scripts live in `tmp/a108/` (gitignored, not committed).
