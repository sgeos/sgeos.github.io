# Task Log

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

Current task state and verification log. This file is the shared source of truth for the active unit of work.

---

## Current Task

**Name**: Fix Header (A0-P4)
**Status**: Complete
**Started**: 2026-02-07

## Success Criteria

- [x] `CLAUDE.md` no longer linked in header on live blog

## Task Breakdown

| ID | Task | Status | Verification |
|----|------|--------|--------------|
| A0-P4-T1 | Exclude CLAUDE.md from Jekyll | Complete | Added `exclude: [CLAUDE.md]` to `_config.yml`. |
| A0-P4-T2 | Update TASKLOG.md, REVERSE_PROMPT.md, commit | Complete | This file and REVERSE_PROMPT.md updated. |

## Notes

- Root cause: GitHub Pages includes `jekyll-optional-front-matter` plugin by default. This plugin processes `.md` files without YAML front matter as Jekyll pages, extracting the title from the first `#` heading. Local Jekyll does not include this plugin, which explains the preview vs. live divergence.
- The `exclude` directive in `_config.yml` tells Jekyll to skip the file entirely during site generation.
- Human will push and verify manually per PROMPT.md notes.

## History

| Date | Change |
|------|--------|
| 2026-02-07 | A0-P1: Knowledge graph, communication protocol, and CLAUDE.md created. |
| 2026-02-07 | A0-P2: Git strategy, commit convention, Ax-Py-Tz coding, PROMPT.md read-only rule documented. |
| 2026-02-07 | A0-P3: Article numbering formalized. A1-A74 assigned to historical posts. Template updated. |
| 2026-02-07 | A75-P1: Same-date ordering documented. "Bidirectional Agentic Workflow" drafted. |
| 2026-02-07 | A75-P2: A75 draft polished. References categorized and sorted. Reference strategy documented. |
| 2026-02-07 | A75-P3: Software Versions convention updated. A75 published with 2026-02-06 date. |
| 2026-02-07 | A76-P1: "Markdown as a Specification Language for Agentic Workflows" drafted. |
| 2026-02-07 | A76-P2: Code Blocks section added. Supplementary research folded in. Categories convention fixed. |
| 2026-02-07 | A76-P3: Replaced A75 internal code with linked reference to previous article. |
| 2026-02-07 | A76-P4: Fixed post_url syntax. A76 published with 2026-02-08 date. |
| 2026-02-07 | A0-P4: Excluded CLAUDE.md from Jekyll to fix header navigation. |
