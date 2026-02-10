# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-09
**Task**: A79-P1 Publish A79, Catalog Stubs

---

## Verification

### A79 Published
**Result**: PASS. `_drafts/writing-proofs.markdown` moved to `_posts/2026-02-10-writing-proofs.markdown`. Human-adjusted date preserved. A83 post_url links corrected (syntax and date).

### Stub Drafts Cataloged
**Result**: PASS. A86 "Mission Command Management Style" and A87 "Telemeritocracy" assigned article numbers. `new_draft.markdown` identified as template copy. All entries added to draft_summary.md.

### A83 Links Fixed
**Result**: PASS. Two post_url references updated from `%{ post_url 2026-02-09-writing-proofs %}` to `{% post_url 2026-02-10-writing-proofs %}`.

---

## Release Announcement Draft

### Writing Proofs (A79)

**Published**: 2026-02-10
**URL**: https://sgeos.github.io/math/development/ai/2026/02/10/writing-proofs.html
**Categories**: math development ai

A survey of mathematical proof techniques and their applications to software verification and formal methods. Covers five proof techniques (direct proof, proof by contradiction, contrapositive, induction, and constructive proof) with worked examples. Extends into software verification with Hoare logic, the Curry-Howard correspondence, TLA+, CompCert, Lean 4, and seL4. Concludes with agentic formal verification covering AlphaProof, Hilbert, APOLLO, and Safe. Fifteen references across five categories.

---

## Implementation Summary

### Files Created/Modified

| File | Changes |
|------|---------|
| `_posts/2026-02-10-writing-proofs.markdown` | Published from `_drafts/`. Human-adjusted date 2026-02-10. |
| `_drafts/safe_embedded_functional_control_dsl.markdown` | Two post_url links fixed: syntax and date updated for A79. |
| `_drafts/mission_command_management_style.markdown` | Article number assigned: A86. |
| `_drafts/telemeritocracy.markdown` | Article number assigned: A87. |
| `_drafts/draft_summary.md` | A79 removed from RCs. A86, A87, new_draft entries added. Summary updated. |
| `_docs/process/PROMPT.md` | Human-updated with A79-P1 instructions. Committed as-is. |
| `_docs/process/TASKLOG.md` | A79-P1 task state. |
| `_docs/process/REVERSE_PROMPT.md` | This file. |

### Stub Drafts Cataloged

| Article | Title | File | Status |
|---------|-------|------|--------|
| A86 | Mission Command Management Style | `mission_command_management_style.markdown` | Stub (~5%). Management style categories, mission command doctrine. |
| A87 | Telemeritocracy | `telemeritocracy.markdown` | Stub (~5%). Telocracy, meritocracy, telemeritocracy. References A86. |
| N/A | Template Copy | `new_draft.markdown` | Leftover template copy from stub creation workflow. |

---

## Questions for Human Pilot

**new_draft.markdown.** This file appears to be a leftover copy of the template from creating the other two stubs. It has no unique content. The human pilot may want to delete it or keep it as a working file for future stub creation.

**A87 references A86.** The telemeritocracy stub notes "Reference mission command article." If this becomes a post_url link, A86 must be published before A87. This potential dependency has been noted in draft_summary.md.

**Release announcement URL.** The URL `https://sgeos.github.io/math/development/ai/2026/02/10/writing-proofs.html` is inferred from Jekyll's default permalink structure and the article's categories. The human pilot should verify after deployment.

---

## Technical Concerns / Risks

**A83 post_url now live.** The A83 post_url links to A79 have been restored to valid `{% post_url %}` syntax. If A83 is built as a draft (via `_preview.sh`), the post_url will now resolve correctly. If A79 were somehow removed, the build would fail.

**A85 post_url still broken.** A85 still contains intentionally broken `%{ post_url 2026-02-14-llm-mad-libs-experiment %}` links. These must be fixed when A84 is published.

**Remaining dependency.** A84 must be published before A85. The A79-before-A83 dependency is now resolved.

---

## Intended Next Step

**Awaiting human direction** on:
- Verification that A79 deployed correctly to GitHub Pages
- Review of remaining release candidates (A80, A81, A82, A83, A84, A85)
- Publication order: A84 before A85 (remaining dependency)
- Whether to delete `new_draft.markdown`
- Any further work

---

## Session Context

If you are a new AI session reading this file:

1. This is a Jekyll blog project at [sgeos.github.io](https://sgeos.github.io).
2. A documentation knowledge graph exists in `_docs/`. Start at `_docs/README.md`.
3. The project uses scoped conventional commits and Ax-Py-Tz work item coding.
4. `PROMPT.md` is read-only for AI agents. Never modify it. Commit it if the human pilot has changed it.
5. A0 is reserved for non-article work. Thirty-two prompts completed (A0-P1 through A0-P7, A75-P1 through A75-P3, A76-P1 through A76-P4, A77-P1 through A77-P3, A78-P1 through A78-P4, A79-P1, A80-P1, A81-P1, A82-P1, A83-P1, A83-P2, A83-P3, A84-P1, A84-P2, A85-P1, A85-P2).
6. All 74 historical posts have article numbers (A1-A74). A75, A76, A77, A78, and A79 are published. A80, A81, A82, A83, A84, and A85 are release candidates. A86 and A87 are stubs. Next available: A88.
7. Categories are space-separated, not comma-separated.
8. Assets follow `assets/$TYPE/post_$SLUG/$FILENAME` convention.
9. Read `TASKLOG.md` for current task state.
10. Read `CLAUDE.md` at project root for build commands and quick orientation.
11. After publication, include a release announcement draft in REVERSE_PROMPT.md. See `CONTENT_WORKFLOW.md` step 5.
12. The draft summary file was renamed from `old_drafts.md` to `draft_summary.md` in A84-P1.
13. A85 depends on A84 via post_url. A87 may depend on A86. Respect publication order.
14. Wait for human prompt before proceeding.
