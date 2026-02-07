# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-07
**Task**: A0-P2 Process Decisions and Clarifications

---

## Verification

### GIT_STRATEGY.md Created
**Result**: PASS. File created at `_docs/process/GIT_STRATEGY.md` with blog-adapted conventions. Excludes GitHub issues, PRs, feature branches, and worktrees from the reference project.

### COMMUNICATION.md Updated
**Result**: PASS. Three changes applied.
1. PROMPT.md read-only rule added to Forward Prompt Rules section.
2. Ax-Py-Tz work item coding system added as new section.
3. Task Completion Protocol updated with commit timing rule (commit after all tasks + reverse prompt).

### POST_STRUCTURE.md Updated
**Result**: PASS. Article Number section added documenting the invisible HTML comment convention (`<!-- A5 -->`).

### Navigation Files Updated
**Result**: PASS.
- `process/README.md`: GIT_STRATEGY.md added to Contents table.
- `DOCUMENTATION_STRATEGY.md`: GIT_STRATEGY.md added to directory structure tree.
- `CLAUDE.md`: Commit Convention section added with summary and PROMPT.md read-only note.

---

## Implementation Summary

### Decisions Documented

| Decision | Location | Summary |
|----------|----------|---------|
| Git strategy | `_docs/process/GIT_STRATEGY.md` | Simple `master` branch workflow. Scoped conventional commits. No PRs or feature branches. |
| Commit convention | `GIT_STRATEGY.md`, `CLAUDE.md` | `<scope>: <imperative summary>` with co-author attribution. |
| Commit timing | `COMMUNICATION.md`, `GIT_STRATEGY.md` | AI commits once after all tasks and reverse prompt are complete. |
| PROMPT.md read-only | `COMMUNICATION.md`, `CLAUDE.md` | AI agent must never modify PROMPT.md. Human pilot owns this file. |
| Ax-Py-Tz coding | `COMMUNICATION.md` | Article-Prompt-Task coding for work item traceability. |
| Article number | `POST_STRUCTURE.md` | Invisible HTML comment with article number after front matter. |

### Files Created

| File | Purpose |
|------|---------|
| `_docs/process/GIT_STRATEGY.md` | Version control conventions adapted for blog |

### Files Modified

| File | Changes |
|------|---------|
| `_docs/process/COMMUNICATION.md` | Added read-only rule, Ax-Py-Tz coding, updated task completion protocol |
| `_docs/writing/POST_STRUCTURE.md` | Added Article Number section |
| `_docs/process/README.md` | Added GIT_STRATEGY.md to contents table |
| `_docs/DOCUMENTATION_STRATEGY.md` | Added GIT_STRATEGY.md to directory tree |
| `CLAUDE.md` | Added Commit Convention section |
| `_docs/process/TASKLOG.md` | Replaced with A0-P2 task state |
| `_docs/process/REVERSE_PROMPT.md` | This file |

---

## Questions for Human Pilot

1. **Article numbering start?** The Ax-Py-Tz system needs a starting article number. Should existing published posts be retroactively numbered (A1 through A74 for the 74 published posts), or should the numbering start fresh from the next post? If starting fresh, what number should the first new article use?

2. **A0 for documentation?** I used A0 to designate documentation-only work that is not associated with a blog article. Is this convention acceptable, or should documentation work use a different designation?

3. **Previous commits?** The first knowledge graph commit (A0-P1) was made before the scoped conventional commit convention was established, so it does not follow the new format. Should that commit be left as-is, or would you like it amended to follow the convention?

---

## Technical Concerns / Risks

**Invisible comment placement**: The article number comment (`<!-- A5 -->`) placed immediately after the front matter `---` will be rendered as an HTML comment in the Jekyll output. This is standard behavior and the comment will not be visible to readers. However, Kramdown may in some edge cases interact unexpectedly with HTML comments at the very top of the Markdown body. If rendering issues arise, the comment could be moved to the end of the file instead.

**Retroactive numbering**: If existing posts are retroactively numbered, that would constitute modifying blog content, which the current prompt's constraints prohibit. This decision should be deferred to a future prompt without the "do not modify blog content" constraint.

---

## Intended Next Step

**Awaiting human direction** on:
- Answers to the questions above
- Any further process refinements
- Next article or documentation task

---

## Session Context

If you are a new AI session reading this file:

1. This is a Jekyll blog project at [sgeos.github.io](https://sgeos.github.io).
2. A documentation knowledge graph exists in `_docs/`. Start at `_docs/README.md`.
3. The project uses scoped conventional commits and Ax-Py-Tz work item coding.
4. `PROMPT.md` is read-only for AI agents. Never modify it.
5. Commit after all tasks and this reverse prompt are updated.
6. A0 designates documentation-only work. Two prompts (P1, P2) have been completed.
7. Read `TASKLOG.md` for current task state.
8. Read `CLAUDE.md` at project root for build commands and quick orientation.
9. Wait for human prompt before proceeding.
