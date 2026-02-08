# Task Log

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

Current task state and verification log. This file is the shared source of truth for the active unit of work.

---

## Current Task

**Name**: Reorganize Assets by Type (A0-P6)
**Status**: Complete
**Started**: 2026-02-07

## Success Criteria

- [x] `assets` organized as `assets/$TYPE/post_$POST_TITLE/$FILENAME`
- [x] Relevant posts patched so they do not break

## Task Breakdown

| ID | Task | Status | Verification |
|----|------|--------|--------------|
| A0-P6-T1 | Reorganize assets by type then post slug | Complete | All files moved to `assets/$TYPE/post_$SLUG/` pattern. Posts patched. No old paths remain. |
| A0-P6-T2 | Update TASKLOG.md, REVERSE_PROMPT.md, commit | Complete | This file and REVERSE_PROMPT.md updated. |

## Notes

- Restructures A0-P5 organization from `assets/post_$SLUG/` to `assets/$TYPE/post_$SLUG/`.
- Image files go under `assets/image/`, PDF files under `assets/pdf/`, WASM files already under `assets/wasm/`.
- The `adding_images` post now has assets split across two type directories (image and pdf).

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
| 2026-02-07 | A0-P5: Organized assets into post-specific subdirectories. Patched 2 posts. |
| 2026-02-07 | A0-P6: Reorganized assets by type then post slug. Patched 2 posts. |
