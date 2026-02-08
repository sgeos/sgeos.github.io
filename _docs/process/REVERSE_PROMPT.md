# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-07
**Task**: A77-P2 Polish LLM Knowledge Graphs Post

---

## Verification

### Article Number Comment Updated
**Result**: PASS. Changed `<!-- Axxx -->` to `<!-- A77 -->` on line 10 of `_drafts/llm_knowledge_graphs.markdown`.

### DOCUMENTATION_STRATEGY.md Inlined
**Result**: PASS. Full file body inlined in a quadruple-backtick markdown code block in the "A Worked Example" section (lines 179-259). Surrounding prose introduces the file and notes that readers should adapt the strategy for their own project.

---

## Implementation Summary

### Files Modified

| File | Changes |
|------|---------|
| `_drafts/llm_knowledge_graphs.markdown` | Article number comment set to A77. Full `DOCUMENTATION_STRATEGY.md` body inlined in code block with surrounding prose. |
| `_docs/process/TASKLOG.md` | A77-P2 task state. |
| `_docs/process/REVERSE_PROMPT.md` | This file. |

### Inline Placement

The `DOCUMENTATION_STRATEGY.md` content was inserted in the "A Worked Example" section, immediately after the sentence that references the file (line 173). The insertion includes:

1. Three lines of transitional prose noting that readers should adapt the strategy for their own project.
2. The full file body in a quadruple-backtick fenced code block with `markdown` language annotation.
3. A one-line transition ("Three structural principles from this strategy merit closer examination.") bridging into the existing principle-by-principle discussion.

Quadruple backticks were used because `DOCUMENTATION_STRATEGY.md` itself contains a triple-backtick code block for the directory structure.

---

## Questions for Human Pilot

No questions. All objectives from PROMPT.md have been met.

---

## Technical Concerns / Risks

**Nested code block rendering.** The quadruple-backtick fence should correctly contain the triple-backtick directory structure block in Kramdown. This is standard CommonMark behavior, but the human pilot should verify rendering in local preview before publication.

---

## Intended Next Step

**Awaiting human direction** on:
- Further polish or revision of the A77 draft
- Whether to proceed to publication

---

## Session Context

If you are a new AI session reading this file:

1. This is a Jekyll blog project at [sgeos.github.io](https://sgeos.github.io).
2. A documentation knowledge graph exists in `_docs/`. Start at `_docs/README.md`.
3. The project uses scoped conventional commits and Ax-Py-Tz work item coding.
4. `PROMPT.md` is read-only for AI agents. Never modify it. Commit it if the human pilot has changed it.
5. A0 is reserved for non-article work. Fifteen prompts completed (A0-P1 through A0-P6, A75-P1 through A75-P3, A76-P1 through A76-P4, A77-P1 through A77-P2).
6. All 74 historical posts have article numbers (A1-A74). A75 and A76 are published. A77 is in draft. Next available: A78.
7. Categories are space-separated, not comma-separated.
8. Assets follow `assets/$TYPE/post_$SLUG/$FILENAME` convention.
9. Read `TASKLOG.md` for current task state.
10. Read `CLAUDE.md` at project root for build commands and quick orientation.
11. Wait for human prompt before proceeding.
