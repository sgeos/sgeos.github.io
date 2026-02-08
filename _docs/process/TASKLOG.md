# Task Log

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

Current task state and verification log. This file is the shared source of truth for the active unit of work.

---

## Current Task

**Name**: Organize Assets (A0-P5)
**Status**: Complete
**Started**: 2026-02-07

## Success Criteria

- [x] `assets` organized
- [x] Relevant posts patched so they do not break

## Task Breakdown

| ID | Task | Status | Verification |
|----|------|--------|--------------|
| A0-P5-T1 | Move trig diagrams and patch post | Complete | 7 PNGs moved to `assets/post_trigonometry/`. 7 references patched in `2016-09-03-trigonometry.markdown`. |
| A0-P5-T2 | Move example assets and patch post | Complete | `image.png` and `document.pdf` moved to `assets/post_adding_images_and_downloads_to_a_github_pages_jekyll_blog/`. 4 references patched (2 rendered + 2 raw example blocks). |
| A0-P5-T3 | Move tokyo_ex presentation | Complete | `tokyo_ex_6_sechter.pdf` moved to `assets/presentations/`. Not referenced by any post. |
| A0-P5-T4 | Update TASKLOG.md, REVERSE_PROMPT.md, commit | Complete | This file and REVERSE_PROMPT.md updated. |

## Notes

- Subdirectory naming follows the `assets/wasm/post_<slug>/` convention already established.
- `tokyo_ex_6_sechter.pdf` has no post reference. Committed 2016-09-22 as standalone presentation slides.
- All old-path references confirmed absent via grep.

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
