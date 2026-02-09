# Task Log

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

Current task state and verification log. This file is the shared source of truth for the active unit of work.

---

## Current Task

**Name**: Rework Draft Notes, Rename Draft Summary (A84-P1)
**Status**: Complete
**Started**: 2026-02-08

## Success Criteria

- [x] Notes reformatted as proper draft article
- [x] old_drafts.md renamed to draft_summary.md with updated title

## Task Breakdown

| ID | Task | Status | Verification |
|----|------|--------|--------------|
| A84-P1-T1 | Reformat LLM Mad Libs notes as article | Complete | `_drafts/llm_mad_libs_experiment.markdown` reformatted from terse notes into proper blog post structure. Assigned A84. Categories: ai ai-tools. Date: 2026-02-14. No research added per instructions. |
| A84-P1-T2 | Rename old_drafts.md to draft_summary.md | Complete | `git mv` used. Title changed from "Old Drafts Review" to "Draft Summary". Opening prose updated. |
| A84-P1-T3 | Add A84 to draft_summary.md | Complete | A84 added to draft_summary.md. Placed in Tier 2. File count updated to 15. |
| A84-P1-T4 | Update TASKLOG.md, REVERSE_PROMPT.md, commit | Complete | This file and REVERSE_PROMPT.md updated. |

## Notes

- A84 assigned to "LLM Mad Libs Experiment". Categories: ai ai-tools. Date: 2026-02-14.
- Human pilot added terse experiment notes to a new draft file. Notes reformatted into article prose without adding research.
- Experiment demonstrates two LLM properties: (1) LLMs are effective blank-fillers via next-token prediction, (2) LLMs are sycophantically compliant and follow instructions even when they conflict with surrounding context.
- Three-step experiment: Session A generates dark Mad Libs template, Session B fills it cheerfully under instruction (producing tonally dissonant output), Step 3 uses a context-aware prompt to reveal the model understands the dark theme.
- Observations cover compliance, template structure as meaning, instruction-over-pattern behavior, and prompt engineering implications.
- No external references consulted. Research deferred to future prompt.
- old_drafts.md renamed to draft_summary.md per PROMPT.md instructions. Title changed to "Draft Summary".
- Placed in Tier 2 (publishable with significant effort) in draft_summary.md.

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
| 2026-02-07 | A77-P1: "LLM Knowledge Graphs" drafted with 20 references. |
| 2026-02-07 | A77-P2: Article number comment updated. DOCUMENTATION_STRATEGY.md inlined. |
| 2026-02-07 | A77-P3: A77 published with 2026-02-07 date. |
| 2026-02-08 | A78-P1: "The State of Context Engineering in Early 2026" drafted. Old drafts reviewed. |
| 2026-02-08 | A78-P2: 8 additional sources folded into A78 (30 references). Old drafts review revised with contemporary tooling assumptions. |
| 2026-02-08 | A78-P3: Release announcement protocol documented. A79 "Writing Proofs" drafted (15 references). Blog branding assessed. 16 candidate topics added. |
| 2026-02-08 | A80-P1: A80 "Probability and Statistics Reference" drafted (9 references). Writing Proofs (A79) and Statistics Reference (A80) elevated to release candidates. |
| 2026-02-08 | A0-P7: About page verified as on brand. Committed with branding analysis in REVERSE_PROMPT.md. |
| 2026-02-08 | A78-P4: A78 published with 2026-02-09 date. Timestamp adjusted to avoid future-dating. |
| 2026-02-08 | A81-P1: A81 "Magic Cards as a Model of Virtual Goods" drafted (9 references). A78 date fix committed. |
| 2026-02-08 | A82-P1: A82 "Introduction to Astronomy" drafted (8 references). Elevated to release candidate. |
| 2026-02-08 | A83-P1: A83 "Safe Embedded Functional Control DSL" reformatted from notes. No research. Added to draft_summary.md Tier 2. |
| 2026-02-08 | A84-P1: A84 "LLM Mad Libs Experiment" reformatted from notes. No research. old_drafts.md renamed to draft_summary.md. |
