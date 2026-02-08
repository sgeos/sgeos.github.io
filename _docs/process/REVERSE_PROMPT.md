# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-08
**Task**: A78-P2 Fold Research into A78 and Revise Old Drafts Review

---

## Verification

### Remaining References Folded into A78
**Result**: PASS. All 8 additional sources from PROMPT.md incorporated into `_drafts/context_engineering.markdown`. References expanded from 20 to 30 across 8 categories. New "Practitioner Strategies" section added. Empirical Evidence expanded from 4 to 6 studies.

### Revised Old Drafts Review
**Result**: PASS. `_drafts/old_drafts.md` rewritten with per-draft sections, contemporary tooling assumptions, and 4-tier publication assessment. Stubs assessed for topicality.

---

## Implementation Summary

### Files Modified

| File | Changes |
|------|---------|
| `_drafts/context_engineering.markdown` | 8 additional sources incorporated. New "Practitioner Strategies" section. Expanded "From Prompt Engineering," Configuration Files, MCP, and Empirical Evidence sections. References: 20 to 30. Future Reading: 5 to 7 entries. |
| `_drafts/old_drafts.md` | Rewritten from tabular format to per-draft sections with contemporary tooling assumptions and 4-tier publication assessment. |
| `_docs/process/PROMPT.md` | Human-updated with A78-P2 instructions. Committed as-is. |
| `_docs/process/TASKLOG.md` | A78-P2 task state. |
| `_docs/process/REVERSE_PROMPT.md` | This file. |

### A78 Changes (P1 to P2)

| Area | P1 | P2 |
|------|----|----|
| References | 20 across 7 categories | 30 across 8 categories |
| Future Reading | 5 entries | 7 entries |
| Empirical studies covered | 4 | 6 |
| Sections | 8 main sections | 9 main sections (added Practitioner Strategies) |
| New sources | N/A | Willison, Karpathy year-in-review, VS Code guide, MCP timeline, arXiv:2510.21413, arXiv:2508.08322, LangChain, HumanLayer, Osmani, Manus |

### Old Drafts Revised Assessment

| Tier | Drafts | Assessment |
|------|--------|------------|
| Tier 1: Publishable with moderate effort | Solana sBPF, statistics | Recent/evergreen, working code/formulas, needs prose |
| Tier 2: Publishable with significant effort | CLMM, half-life coin, space studies, MTG/Rust | Sound foundations, extensive new writing needed |
| Tier 3: Salvageable but niche | Android APK + NDK on FreeBSD | Consolidate into one post, small audience |
| Tier 4: Rewrite or abandon | Android testing, Phoenix/Guardian, astronomy stub, proofs stub | Near-complete rewrites or write from scratch |

---

## Questions for Human Pilot

No questions. All objectives from PROMPT.md have been met.

---

## Technical Concerns / Risks

**URL verification needed.** Reference URLs were gathered by research agents and have not been manually verified. The human pilot should verify all 30 URLs before publication.

**Series cross-references.** A78 uses `{% post_url %}` tags to link to A75, A76, and A77. These should render correctly given the established conventions.

**Overlap with A77.** A78 and A77 share some references and cover related ground. A78 is positioned as a broader survey while A77 focuses specifically on knowledge graphs. The human pilot should verify that the distinction is clear.

**Article length.** A78 has grown substantially with the additional sources. The human pilot should assess whether the length is appropriate or whether any sections should be trimmed.

---

## Intended Next Step

**Awaiting human direction** on:
- Review of the expanded A78 draft
- Whether to polish, revise, or proceed to publication
- Any action on the tiered old drafts assessment

---

## Session Context

If you are a new AI session reading this file:

1. This is a Jekyll blog project at [sgeos.github.io](https://sgeos.github.io).
2. A documentation knowledge graph exists in `_docs/`. Start at `_docs/README.md`.
3. The project uses scoped conventional commits and Ax-Py-Tz work item coding.
4. `PROMPT.md` is read-only for AI agents. Never modify it. Commit it if the human pilot has changed it.
5. A0 is reserved for non-article work. Eighteen prompts completed (A0-P1 through A0-P6, A75-P1 through A75-P3, A76-P1 through A76-P4, A77-P1 through A77-P3, A78-P1 through A78-P2).
6. All 74 historical posts have article numbers (A1-A74). A75, A76, and A77 are published. A78 is drafted. Next available: A79.
7. Categories are space-separated, not comma-separated.
8. Assets follow `assets/$TYPE/post_$SLUG/$FILENAME` convention.
9. Read `TASKLOG.md` for current task state.
10. Read `CLAUDE.md` at project root for build commands and quick orientation.
11. Wait for human prompt before proceeding.
