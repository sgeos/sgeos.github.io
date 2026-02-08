# Task Log

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

Current task state and verification log. This file is the shared source of truth for the active unit of work.

---

## Current Task

**Name**: Publish A76 (A76-P4)
**Status**: Complete
**Started**: 2026-02-07

## Success Criteria

- [x] A76 is published

## Task Breakdown

| ID | Task | Status | Verification |
|----|------|--------|--------------|
| A76-P4-T1 | Fix post_url syntax and publish | Complete | Removed `.html` extension from `{% post_url %}` tag. Draft moved to `_posts/2026-02-08-markdown_as_a_specification_language.markdown`. |
| A76-P4-T2 | Update TASKLOG.md, REVERSE_PROMPT.md, commit | Complete | This file and REVERSE_PROMPT.md updated. |

## Notes

- Human manually updated STYLE_GUIDE.md with `{% post_url %}` convention for cross-linking posts.
- Human changed `blog_bidirectional` URL definition from hardcoded URL to `{% post_url %}` tag but included `.html` extension. Fixed to match Jekyll syntax (no extension).
- Date not changed per PROMPT.md instructions. Publication date remains `2026-02-08`.

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
