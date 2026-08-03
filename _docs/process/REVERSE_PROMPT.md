# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-04
**Task**: Imported the handoff-prompt protocol from `keleusma` and adapted it to this project. This completes the durable handoff process you deferred on 2026-08-02 until the series was finished.

---

## What the Protocol Actually Is

The idea worth importing is one design decision, and it is counterintuitive.

**The handoff is deliberately not kept current.** Every other channel here is maintained — `TASKLOG.md` incrementally, `REVERSE_PROMPT.md` overwritten each task. `HANDOFF.md` is the opposite: a snapshot stamped with the commit it describes.

That is what makes it safe. A resuming agent compares the recorded parent commit to `git rev-parse HEAD~1`:

- **Match** — the handoff commit is still the tip, nothing landed after it, so the handoff describes the live state. Trust it.
- **Mismatch** — something landed after. The handoff is stale **by construction**, says so itself, and the agent falls back to the live channels instead.

A handoff kept perpetually "current" cannot do this. It would look authoritative while quietly describing a state that no longer exists, which is precisely the failure a post-compaction agent cannot detect from the inside.

---

## What I Adapted

The source is written for a Rust compiler project with a release gate, feature branches, and a byte-identical differential oracle. I substituted this project's equivalents rather than importing the shape wholesale.

| Source | Here |
|---|---|
| `docs/process/` | `_docs/process/` |
| Three resume channels including a design journal | Two channels plus `_drafts/draft_summary.md` |
| `scripts/release-gate.sh`, differential oracle | Build check, anchor integrity, style discipline, URL sweeps, DOI registry checks |
| Branch hierarchy, no-ff merges | `master`, two-commit publication pattern |
| Boundary counts pinned by a test | Density conventions as absolute counts |

**One addition the source does not have.** I added a **Writing a New Handoff** section. Without it the protocol is a one-off document that decays the moment the state moves; with it, the format perpetuates itself and the next agent knows to set the parent commit from `HEAD` rather than carrying forward a remembered value.

---

## Where It Is Wired

- **`_docs/process/HANDOFF.md`** — the protocol, stamped with parent commit `7c2c97b`.
- **`CLAUDE.md`** — session startup now validates the handoff first; a new **Compact Instructions** section lists what to preserve on compaction, adapted to this project's channels and governing rules.
- **`_docs/process/README.md`** — indexed and added to the session working documents table and startup protocol.
- **`_docs/process/COMMUNICATION.md`** — described as a channel, with the not-kept-current property stated explicitly so nobody "helpfully" maintains it.

---

## What the First Handoff Says

I stamped it with the real current state rather than leaving a template, so it is immediately usable.

It records that the series is complete and **no work is in flight**, and explicitly tells a resuming agent not to resume drafting or re-verifying it. It then carries forward the four open observations, seven method rules earned during the series, and six governing constraints.

The method rules are the part I would not want lost. They include that an HTTP 200 does not verify a citation, that a source which cannot be confirmed should be dropped rather than guessed at, that a script's blast radius should be checked before running it over the corpus, and that counts should be verified on things you did not intend to change. Each of those was learned from an actual failure in this series, two of them my own.

---

## Verification

The validity check passes against the committed state: the handoff's recorded parent matches `HEAD~1`.

---

## Items Requiring Your Attention

1. **The ephemeral handoff at `tmp/spacex_series_post_compaction_handoff.md` is now superseded.** It remains untracked and gitignored. Delete it whenever you like; I left it alone since it costs nothing.
2. **Two carried-forward defects are recorded in the handoff, not fixed**: the `future:` config-versus-documentation contradiction, and `_publish.sh` failing under BSD sed. Both are your call.

---

## Suggested Next Steps

- Nothing is pending. The series is published and the handoff protocol is in place.
- When you next plan a compaction, ask for a handoff and I will overwrite `HANDOFF.md` per its own instructions.
