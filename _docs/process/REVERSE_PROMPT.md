# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-07
**Task**: A76-P4 Publish A76

---

## Verification

### A76 Published
**Result**: PASS. Draft moved from `_drafts/markdown_as_a_specification_language.markdown` to `_posts/2026-02-08-markdown_as_a_specification_language.markdown` via `_publish.sh`. Date unchanged at `2026-02-08 01:42:16 +0000`.

### post_url Syntax Fixed
**Result**: PASS. Human's `{% post_url 2026-02-06-bidirectional_agentic_workflow.html %}` corrected to `{% post_url 2026-02-06-bidirectional_agentic_workflow %}` (Jekyll expects slug without file extension, per STYLE_GUIDE.md convention).

---

## Implementation Summary

### Files Modified

| File | Changes |
|------|---------|
| `_posts/2026-02-08-markdown_as_a_specification_language.markdown` | Published from `_drafts/`. Fixed `{% post_url %}` syntax (removed `.html` extension). |
| `_docs/process/TASKLOG.md` | A76-P4 task state. |
| `_docs/process/REVERSE_PROMPT.md` | This file. |

---

## Questions for Human Pilot

No questions. A76 is published.

---

## Technical Concerns / Risks

**No blocking concerns.** The `{% post_url %}` tag will resolve to the correct URL at build time. The STYLE_GUIDE.md convention for cross-linking posts is now documented and should prevent hardcoded URLs in future cross-links.

---

## Intended Next Step

**Awaiting human direction** on:
- Whether to push to remote
- Next article or task

---

## Session Context

If you are a new AI session reading this file:

1. This is a Jekyll blog project at [sgeos.github.io](https://sgeos.github.io).
2. A documentation knowledge graph exists in `_docs/`. Start at `_docs/README.md`.
3. The project uses scoped conventional commits and Ax-Py-Tz work item coding.
4. `PROMPT.md` is read-only for AI agents. Never modify it. Commit it if the human pilot has changed it.
5. A0 is reserved for non-article work. Ten prompts completed (A0-P1 through A0-P3, A75-P1 through A75-P3, A76-P1 through A76-P4).
6. All 74 historical posts have article numbers (A1-A74). A75 and A76 are published. Next available: A77.
7. Categories are space-separated, not comma-separated.
8. Read `TASKLOG.md` for current task state.
9. Read `CLAUDE.md` at project root for build commands and quick orientation.
10. Wait for human prompt before proceeding.
