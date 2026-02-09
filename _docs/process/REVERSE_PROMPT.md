# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-08
**Task**: A83-P1 Rework Draft Notes

---

## Verification

### Draft Notes Reformatted
**Result**: PASS. `_drafts/safe_embedded_functional_control_dsl.markdown` reformatted from raw specification notes into proper blog post structure. Assigned A83. No research added per instructions. Added to old_drafts.md as Tier 2 draft.

---

## Implementation Summary

### Files Created/Modified

| File | Changes |
|------|---------|
| `_drafts/safe_embedded_functional_control_dsl.markdown` | Reformatted from specification notes to article structure. Assigned A83. Categories: dsl embedded development safety. Date: 2026-02-13. Template sections replaced with article prose. Code examples preserved. |
| `_drafts/old_drafts.md` | A83 added with Tier 2 assessment. File count updated to 14. |
| `_docs/process/PROMPT.md` | Human-updated with A83-P1 instructions. Committed as-is. |
| `_docs/process/TASKLOG.md` | A83-P1 task state. |
| `_docs/process/REVERSE_PROMPT.md` | This file. |

### A83 Article Structure

| Section | Content |
|---------|---------|
| Opening | Safety-critical embedded systems motivation, DSL proposal, provable and certifiable (not a proof language), draft status |
| Software Versions | Standard environment block |
| Design Goals | Seven goals: maximum safety, formal analyzability, embeddability, hot-updatable logic, functional syntax, concurrency-safe design, performance |
| Language Features | Eight features: pure functions, pipelines with @ placeholder, exhaustive pattern matching, multi-headed functions, ADTs, strong type system with effect annotations, hot update mechanism, concurrency semantics |
| Runtime and VM Architecture | Four subsections: stack-based VM, memory model, host integration, formal guarantees |
| Example | SensorEvent ADT with temperature/pressure handlers demonstrating pipelines and host-bound effects |
| Design Tradeoffs | Expressiveness traded for predictability and safety, host/script boundary rationale |
| Summary | Recap and future work outline (formal semantics, reference implementation, certification) |
| Future Reading | Placeholder for future development |
| References | Placeholder for future research |

### Changes from Original Notes

The original file contained raw specification notes with numbered bullet lists, horizontal rules as section dividers, and template placeholder sections (Problem description, Instructions, echo "Code here."). The reformatted article replaces all placeholder sections with article prose, converts bullet lists into flowing paragraphs, adds a Software Versions block, and restructures the specification sections as article headings. All technical content from the original notes is preserved. No content was added beyond reformatting.

---

## Questions for Human Pilot

**Categories.** The article uses categories "dsl embedded development safety". The human pilot should confirm these are acceptable. Alternative categories might include "rust" (given the Rust host target) or "aerospace".

**Completion estimate.** The draft is assessed at ~25% completion. The specification structure is sound but lacks research, references, related work comparison, and expanded prose. The human pilot should confirm whether this assessment is reasonable.

---

## Technical Concerns / Risks

**No references.** Per instructions, no research was conducted. The article currently has no external references. Related work (Lua, Erlang, SCADE, Lustre, Ivory, Copilot) should be researched and cited in a future prompt.

**Certification claims.** The article states the language is "designed to be provable and certifiable." Certification pathways (DO-178C, MISRA, IEC 61508) should be researched and discussed when the article is fleshed out.

---

## Intended Next Step

**Awaiting human direction** on:
- Review of the A83 draft structure
- Whether to proceed with research and expansion of A83 in a future prompt
- Publication timing for A79, A80, A81, and A82 (all release candidates)
- Any further work

---

## Session Context

If you are a new AI session reading this file:

1. This is a Jekyll blog project at [sgeos.github.io](https://sgeos.github.io).
2. A documentation knowledge graph exists in `_docs/`. Start at `_docs/README.md`.
3. The project uses scoped conventional commits and Ax-Py-Tz work item coding.
4. `PROMPT.md` is read-only for AI agents. Never modify it. Commit it if the human pilot has changed it.
5. A0 is reserved for non-article work. Twenty-five prompts completed (A0-P1 through A0-P7, A75-P1 through A75-P3, A76-P1 through A76-P4, A77-P1 through A77-P3, A78-P1 through A78-P4, A80-P1, A81-P1, A82-P1, A83-P1).
6. All 74 historical posts have article numbers (A1-A74). A75, A76, A77, and A78 are published. A79, A80, A81, and A82 are release candidates. A83 is a draft. Next available: A84.
7. Categories are space-separated, not comma-separated.
8. Assets follow `assets/$TYPE/post_$SLUG/$FILENAME` convention.
9. Read `TASKLOG.md` for current task state.
10. Read `CLAUDE.md` at project root for build commands and quick orientation.
11. After publication, include a release announcement draft in REVERSE_PROMPT.md. See `CONTENT_WORKFLOW.md` step 5.
12. Wait for human prompt before proceeding.
