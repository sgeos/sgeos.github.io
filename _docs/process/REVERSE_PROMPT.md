# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-07
**Task**: Knowledge Graph and Communication Protocol Setup

---

## Verification

### Knowledge Graph Structure
**Command**: `find _docs -name "*.md" | sort`
**Expected Result**: 13 markdown files across 4 sections (writing, architecture, process, reference) plus root README and DOCUMENTATION_STRATEGY.

### File List

```
_docs/DOCUMENTATION_STRATEGY.md
_docs/README.md
_docs/architecture/JEKYLL_STRUCTURE.md
_docs/architecture/README.md
_docs/process/COMMUNICATION.md
_docs/process/CONTENT_WORKFLOW.md
_docs/process/PROMPT.md
_docs/process/README.md
_docs/process/REVERSE_PROMPT.md
_docs/process/TASKLOG.md
_docs/reference/GLOSSARY.md
_docs/reference/README.md
_docs/writing/POST_STRUCTURE.md
_docs/writing/README.md
_docs/writing/STYLE_GUIDE.md
```

### CLAUDE.md Updated
**Result**: Added Documentation section with navigation table and Session Startup Protocol.

---

## Implementation Summary

### Knowledge Graph Created

Adapted the reference project's documentation structure to fit a simple blog project. The reference project (Cordial Cantina) has 11 documentation sections covering a complex Elixir/Rust trading application. This blog project uses 4 sections appropriate to its scope.

| Section | Files | Purpose |
|---------|-------|---------|
| writing | 3 | Style guide and post structure conventions |
| architecture | 2 | Jekyll layout hierarchy and asset organization |
| process | 6 | Workflow, communication protocol, task tracking |
| reference | 2 | Glossary of key terms |

### Bidirectional Communication Protocol

Replicated the three-document communication model from the reference project.

- `PROMPT.md` (human to AI) was already present and retained as-is.
- `REVERSE_PROMPT.md` (AI to human) was present but contained content from the reference project. Overwritten with content appropriate to this blog project.
- `TASKLOG.md` (shared) created as the renamed equivalent of the reference project's `MILESTONE.md`.
- `COMMUNICATION.md` documents the full protocol including forward prompts, reverse prompts, task completion, and blocking procedures.

---

## MILESTONE.md Naming Recommendation

The reference project uses `MILESTONE.md` as the current sprint source of truth. The name "milestone" implies a fixed endpoint in a release-oriented development cycle. Based on how the file actually functions, it is a task log that tracks individual work items, their statuses, and verification results within a current unit of work.

**Recommended name: `TASKLOG.md`**

Rationale: The file logs tasks and their completion states. "Task log" describes the file's actual function rather than implying a release management artifact. This name is more accurate for a blog project that does not follow versioned release cycles, and it also better reflects the file's use in the reference project.

This project uses `TASKLOG.md`. The reference project may benefit from the same rename, but that decision is left to the human pilot per the constraint against modifying the reference project.

---

## Questions for Human Pilot

1. **Git strategy documentation?** The reference project includes `GIT_STRATEGY.md` documenting branch naming, commit conventions, and linear history policy. This blog project currently uses a simple `master` branch workflow. Should a git strategy document be added, or is the current workflow sufficiently simple that it does not warrant formal documentation?

2. **Work item coding system?** The reference project uses a hierarchical work item coding system (Vw-Mx-Py-Tz). This blog does not have versioned releases or phased milestones. Should a simplified task identification scheme be adopted, or should tasks be identified by descriptive names only?

3. **Commit convention for documentation changes?** The reference project uses scoped conventional commits (e.g., `docs: add knowledge graph`). Should this blog adopt a similar commit convention, or continue with the current free-form commit messages?

4. **PROMPT.md content?** The existing `PROMPT.md` contains the instructions that were just executed. Should the file be updated to reflect a "completed" state, or should the current prompt content be preserved as-is for the commit history?

---

## Technical Concerns / Risks

**Jekyll underscore prefix**: Directories prefixed with `_` are excluded from the Jekyll build output by default. The `_docs/` directory will not appear on the published site, which is the intended behavior for internal documentation.

**REVERSE_PROMPT.md overwrite**: The previous content in `REVERSE_PROMPT.md` contained status information from the Cordial Cantina reference project, not from this blog. This content appeared to be a copy-paste artifact rather than meaningful state for this project. It has been replaced.

---

## Intended Next Step

**Awaiting human direction** on:
- Answers to the questions above
- Whether to commit the current state
- Any adjustments to the knowledge graph structure or content

---

## Session Context

If you are a new AI session reading this file:

1. This is a Jekyll blog project at [sgeos.github.io](https://sgeos.github.io).
2. A documentation knowledge graph was created in `_docs/` on 2026-02-07.
3. The knowledge graph is intentionally lightweight, matching the project's scope.
4. Start at `_docs/README.md` for navigation.
5. Read `TASKLOG.md` for current task state.
6. Read `CLAUDE.md` at project root for build commands and quick orientation.
7. Wait for human prompt before proceeding.
