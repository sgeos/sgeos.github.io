# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-07
**Task**: A77-P3 Publish LLM Knowledge Graphs Post

---

## Verification

### Article Published
**Result**: PASS. `_drafts/llm_knowledge_graphs.markdown` published to `_posts/2026-02-07-llm_knowledge_graphs.markdown` via `_publish.sh`.

---

## Implementation Summary

### Files Modified

| File | Changes |
|------|---------|
| `_posts/2026-02-07-llm_knowledge_graphs.markdown` | Published from `_drafts/`. Includes human edits: date changed to 2026-02-07, bold label added before DOCUMENTATION_STRATEGY.md code block. |
| `_docs/process/PROMPT.md` | Human-updated with A77-P3 instructions. Committed as-is. |
| `_docs/process/TASKLOG.md` | A77-P3 task state. |
| `_docs/process/REVERSE_PROMPT.md` | This file. |

---

## Questions for Human Pilot

No questions. All objectives from PROMPT.md have been met.

---

## Technical Concerns / Risks

No concerns. Standard publication workflow.

---

## Intended Next Step

**Awaiting human direction** on next task. A77 is published. Next available article number is A78.

---

## Session Context

If you are a new AI session reading this file:

1. This is a Jekyll blog project at [sgeos.github.io](https://sgeos.github.io).
2. A documentation knowledge graph exists in `_docs/`. Start at `_docs/README.md`.
3. The project uses scoped conventional commits and Ax-Py-Tz work item coding.
4. `PROMPT.md` is read-only for AI agents. Never modify it. Commit it if the human pilot has changed it.
5. A0 is reserved for non-article work. Sixteen prompts completed (A0-P1 through A0-P6, A75-P1 through A75-P3, A76-P1 through A76-P4, A77-P1 through A77-P3).
6. All 74 historical posts have article numbers (A1-A74). A75, A76, and A77 are published. Next available: A78.
7. Categories are space-separated, not comma-separated.
8. Assets follow `assets/$TYPE/post_$SLUG/$FILENAME` convention.
9. Read `TASKLOG.md` for current task state.
10. Read `CLAUDE.md` at project root for build commands and quick orientation.
11. Wait for human prompt before proceeding.
