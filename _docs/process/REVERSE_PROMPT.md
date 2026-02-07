# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-07
**Task**: A0-P3 Article Numbering and Process Formalization

---

## Verification

### A0 Convention Documented
**Result**: PASS. COMMUNICATION.md updated: A0 described as "non-article work" in the Ax component table and in the article number description.

### PROMPT.md Commit Rule Corrected
**Result**: PASS. COMMUNICATION.md Forward Prompt Rules and CLAUDE.md Commit Convention sections updated. AI agent must now commit PROMPT.md if the human pilot has modified it.

### Draft Template Updated
**Result**: PASS. `_drafts/template.markdown` now contains `<!-- Axxx -->` placeholder with blank lines before and after.

### POST_STRUCTURE.md Updated
**Result**: PASS. Article Number section updated with explicit blank line requirements and the example now shows content after the comment. Added note about A1-A74 historical numbering and A0 reservation.

### Historical Posts Numbered
**Command**: `python3 add_article_numbers.py`
**Result**: PASS. 74/74 posts updated with article numbers A1-A74.

**Spot checks**:
- A2 (`2016-01-08-hello-world.markdown`): Correct placement and blank lines.
- A55 (`2022-10-03-getting-started-with-playdate.markdown`): Correct placement and blank lines.
- A74 (`2026-01-31-claude_code_getting_started.markdown`): Correct placement and blank lines.

---

## Implementation Summary

### Decisions Documented

| Decision | Location | Summary |
|----------|----------|---------|
| A0 for non-article work | `COMMUNICATION.md` | A0 reserved for documentation, process, and infrastructure |
| PROMPT.md commit rule | `COMMUNICATION.md`, `CLAUDE.md` | AI commits PROMPT.md if human has modified it |

### Files Modified

| File | Changes |
|------|---------|
| `_docs/process/COMMUNICATION.md` | A0 convention, PROMPT.md commit rule corrected |
| `_docs/writing/POST_STRUCTURE.md` | Blank line requirements, historical numbering note |
| `CLAUDE.md` | PROMPT.md commit rule updated |
| `_drafts/template.markdown` | Added `<!-- Axxx -->` placeholder |
| `_posts/*.markdown` (74 files) | Added `<!-- A1 -->` through `<!-- A74 -->` |
| `_docs/process/TASKLOG.md` | A0-P3 task state |
| `_docs/process/REVERSE_PROMPT.md` | This file |

### Article Number Assignment

Posts numbered A1 through A74 in chronological order by filename date prefix. Same-date posts ordered alphabetically by slug. Full mapping:

| Range | Period | Count |
|-------|--------|-------|
| A1-A46 | 2016 | 46 |
| A47-A53 | 2017 | 7 |
| A54 | 2019 | 1 |
| A55-A61 | 2022 | 7 |
| A62-A64 | 2023 | 3 |
| A65 | 2025 | 1 |
| A66-A74 | 2026 | 9 |

**Next available article number: A75.**

---

## Questions for Human Pilot

1. **Drafts numbering?** There are 13 files in `_drafts/` (excluding the template). Should existing drafts receive article numbers now, or should they be numbered when published? If now, numbering would continue from A75.

2. **Same-date ordering?** Posts sharing a publication date (e.g., three posts on 2016-01-08) were ordered alphabetically by slug. If a different ordering is preferred for same-date posts, the numbering can be adjusted.

---

## Technical Concerns / Risks

**Rendering verification**: The article number comments should not affect Jekyll rendering. They are standard HTML comments and will be invisible in the published output. A preview with `./_preview.sh` would confirm no rendering regressions across all 74 posts, but this was not performed to avoid side effects outside the documentation scope.

**Trailing newlines**: The script normalizes each file to end with a single newline. This is standard convention but may produce whitespace-only diffs on posts that previously had different trailing newline patterns.

---

## Intended Next Step

**Awaiting human direction** on:
- Answers to the questions above
- Any adjustments to article numbering
- Next article or documentation task

---

## Session Context

If you are a new AI session reading this file:

1. This is a Jekyll blog project at [sgeos.github.io](https://sgeos.github.io).
2. A documentation knowledge graph exists in `_docs/`. Start at `_docs/README.md`.
3. The project uses scoped conventional commits and Ax-Py-Tz work item coding.
4. `PROMPT.md` is read-only for AI agents. Never modify it. Commit it if the human pilot has changed it.
5. A0 is reserved for non-article work. Three prompts (P1, P2, P3) have been completed.
6. All 74 published posts have article numbers (A1-A74). Next available: A75.
7. Read `TASKLOG.md` for current task state.
8. Read `CLAUDE.md` at project root for build commands and quick orientation.
9. Wait for human prompt before proceeding.
