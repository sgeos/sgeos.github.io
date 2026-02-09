# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-08
**Task**: A83-P2 Fully Draft A83

---

## Verification

### A83 Fully Drafted
**Result**: PASS. `_drafts/safe_embedded_functional_control_dsl.markdown` fully rewritten from ~260-line design notes to ~584-line researched article. 12 references across 2 categories (Reference, Research). Research incorporated covering embeddable scripting languages, synchronous dataflow, effect systems, hot code reloading, capability-based security, and formal verification.

---

## Implementation Summary

### Files Created/Modified

| File | Changes |
|------|---------|
| `_drafts/safe_embedded_functional_control_dsl.markdown` | Fully rewritten. 584 lines. 12 references. Elixir-inspired, Rust-embeddable, mission-critical framing. Links to A79. |
| `_drafts/draft_summary.md` | A83 elevated to release candidate. Removed from Tier 2. Summary updated (5 release candidates). |
| `_docs/process/PROMPT.md` | Human-updated with A83-P2 instructions. Committed as-is. |
| `_docs/process/TASKLOG.md` | A83-P2 task state. |
| `_docs/process/REVERSE_PROMPT.md` | This file. |

### A83 Article Structure

| Section | Content |
|---------|---------|
| Opening | Embeddable scripting landscape (Lua, Rhai, mruby), mission-critical gap, DSL proposal, Elixir inspiration, Rust embedding, A79 tie-in, informal proposal framing |
| Software Versions | Standard environment block |
| Why Existing Embeddable Languages Fall Short | Lua (dynamic typing, global vars, GC pauses), Rhai (no static types, no effect tracking), mruby (complexity, limitations from constraining full language) |
| Design Inspiration | Elixir/BEAM (syntax, pipelines, hot reload, fault tolerance), Gleam (static types on BEAM), Roc (platform architecture, I/O control), Koka (algebraic effects) |
| Design Goals | 7 goals: safety, formal analyzability, embeddability, hot updates, functional syntax, concurrency safety, bounded resources |
| Language Features | 8 features with code examples: pure functions, pipelines with @, exhaustive pattern matching, multi-headed functions with guards, ADTs (Result, SensorEvent), static typing with effect annotations (! io), hot update code_change callback, concurrency semantics |
| Runtime and VM Architecture | Stack-based VM, arena-based memory (no GC), capability-based host integration (WASI model), formal guarantees |
| Use Cases | Plugin systems, game programming, robotics scripting |
| Related Work | Lustre/SCADE (synchronous dataflow, DO-178C), Ivory/Copilot (Haskell EDSLs, NASA, code generation vs runtime embedding) |
| Design Tradeoffs | Expressiveness vs safety, host/script boundary, SCADE/Lustre philosophy |
| Summary | Recap, A79 link, future work |
| Future Reading | 6 entries (Rhai, Elixir, Gleam, Roc, Koka, Copilot) |
| References | 12 entries across 2 categories (11 Reference, 1 Research) |

### Changes from A83-P1 Draft

Major rewrite. The A83-P1 draft was a reformatted version of design notes with no research and no references. The A83-P2 version:
- Reframed from aerospace-specific to general mission-critical scripting (plugins, games, robotics)
- Added "Why Existing Languages Fall Short" section comparing Lua, Rhai, mruby
- Added "Design Inspiration" section covering Elixir, Gleam, Roc, Koka
- Expanded code examples (factorial with guards, ADT declarations, effect annotations, code_change callback)
- Added "Use Cases" section with three concrete applications
- Added "Related Work" section comparing Lustre/SCADE and Ivory/Copilot
- Added 12 references from official sources
- Added post_url links to A79 "Writing Proofs"
- Replaced "Performance Considerations" goal with "Bounded Resource Usage" (more precise)
- Added arena-based memory model (no GC) and capability-based security (WASI model)

---

## Questions for Human Pilot

**A79 post_url link.** The article links to A79 "Writing Proofs" using `{% post_url 2026-02-09-writing-proofs %}`. This assumes A79 will be published before A83. If A79 is not yet published when A83 goes live, the link will fail. The human pilot should ensure A79 is published first or remove the links.

**Categories.** The article uses categories "dsl embedded development safety". The human pilot should confirm these are acceptable.

**Elixir inspiration depth.** The article describes Elixir as the primary syntactic inspiration but the proposed DSL diverges significantly (static typing, no actor model, no OTP). The human pilot should confirm that the level of Elixir attribution is appropriate.

---

## Technical Concerns / Risks

**URL verification.** All 12 reference URLs should be verified before publication. Most point to official project sites and documentation.

**post_url dependency.** Two `post_url` links reference A79. A79 must be published (moved to `_posts/`) before A83 can build successfully.

---

## Intended Next Step

**Awaiting human direction** on:
- Review of the A83 draft
- Publication order (A79 must precede A83 due to post_url dependency)
- Publication timing for A79, A80, A81, A82, and A83 (all release candidates)
- Any further work

---

## Session Context

If you are a new AI session reading this file:

1. This is a Jekyll blog project at [sgeos.github.io](https://sgeos.github.io).
2. A documentation knowledge graph exists in `_docs/`. Start at `_docs/README.md`.
3. The project uses scoped conventional commits and Ax-Py-Tz work item coding.
4. `PROMPT.md` is read-only for AI agents. Never modify it. Commit it if the human pilot has changed it.
5. A0 is reserved for non-article work. Twenty-eight prompts completed (A0-P1 through A0-P7, A75-P1 through A75-P3, A76-P1 through A76-P4, A77-P1 through A77-P3, A78-P1 through A78-P4, A80-P1, A81-P1, A82-P1, A83-P1, A83-P2, A84-P1, A85-P1).
6. All 74 historical posts have article numbers (A1-A74). A75, A76, A77, and A78 are published. A79, A80, A81, A82, and A83 are release candidates. A84 and A85 are drafts. Next available: A86.
7. Categories are space-separated, not comma-separated.
8. Assets follow `assets/$TYPE/post_$SLUG/$FILENAME` convention.
9. Read `TASKLOG.md` for current task state.
10. Read `CLAUDE.md` at project root for build commands and quick orientation.
11. After publication, include a release announcement draft in REVERSE_PROMPT.md. See `CONTENT_WORKFLOW.md` step 5.
12. The draft summary file was renamed from `old_drafts.md` to `draft_summary.md` in A84-P1.
13. A83 depends on A79 via post_url. A79 must be published before A83.
14. Wait for human prompt before proceeding.
