# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-08
**Task**: A84-P1 Rework Draft Notes, Rename Draft Summary

---

## Verification

### Draft Notes Reformatted
**Result**: PASS. `_drafts/llm_mad_libs_experiment.markdown` reformatted from terse experiment notes into proper blog post structure. Assigned A84. No research added per instructions. Added to draft_summary.md as Tier 2 draft.

### Draft Summary Renamed
**Result**: PASS. `_drafts/old_drafts.md` renamed to `_drafts/draft_summary.md` via `git mv`. Title changed from "Old Drafts Review" to "Draft Summary". Opening prose updated.

---

## Implementation Summary

### Files Created/Modified

| File | Changes |
|------|---------|
| `_drafts/llm_mad_libs_experiment.markdown` | Reformatted from terse notes to article structure. Assigned A84. Categories: ai ai-tools. Date: 2026-02-14. Template sections replaced with article prose. Experiment data preserved. |
| `_drafts/old_drafts.md` -> `_drafts/draft_summary.md` | Renamed via git mv. Title changed to "Draft Summary". Opening prose updated. A84 entry added. File count updated to 15. |
| `_docs/process/PROMPT.md` | Human-updated with A84-P1 instructions. Committed as-is. |
| `_docs/process/TASKLOG.md` | A84-P1 task state. |
| `_docs/process/REVERSE_PROMPT.md` | This file. |

### A84 Article Structure

| Section | Content |
|---------|---------|
| Opening | LLMs as blank-fillers, sycophantic compliance, experiment introduction |
| Software Versions | Standard environment block |
| The Experiment | Three-step experiment with separate LLM sessions |
| Step 1 | Session A generates dark Mad Libs template with bracketed placeholders |
| Step 2 | Session B fills template cheerfully under instruction, producing tonally dissonant output |
| Step 3 | Context-aware fill prompt described (output not included, left for future work) |
| Observations | Four observations: compliance, template structure as meaning, instruction-over-pattern, logical fill reveals understanding |
| Implications | Mental model for LLM interaction, prompt engineering consequences |
| Summary | Two fundamental LLM properties demonstrated, users as responsible operators |
| Future Reading | Placeholder |
| References | Placeholder |

### Changes from Original Notes

The original file contained terse bullet points, raw template text, raw Session B output, and a brief prompt suggestion for Step 3. The reformatted article wraps all experiment data in explanatory prose, adds section structure (Experiment, Observations, Implications, Summary), preserves all original template and output text verbatim in fenced code blocks, and frames the experiment as a demonstration of LLM sycophantic compliance and instruction-over-context behavior. The Step 3 output is described but not included (the original notes did not contain it).

---

## Questions for Human Pilot

**Step 3 output.** The original notes describe the Step 3 prompt ("fill in the most logical word") but do not include the resulting output. A future revision could include the actual dark-themed output to complete the three-way comparison. The human pilot may want to run this experiment and paste the result.

**Categories.** The article uses categories "ai ai-tools". The human pilot should confirm these are acceptable. Alternative categories might include "prompt-engineering" or "llm".

---

## Technical Concerns / Risks

**No references.** Per instructions, no research was conducted. The article currently has no external references. Related work on LLM sycophancy, RLHF alignment, and instruction-following behavior should be researched and cited in a future prompt.

**Typo preservation.** The original Session B prompt contained a minor grammatical issue ("Do your best choose words"). This was preserved verbatim in the article as it represents the actual prompt used in the experiment.

---

## Intended Next Step

**Awaiting human direction** on:
- Review of the A84 draft
- Whether to add Step 3 output to the article
- Publication timing for A79, A80, A81, and A82 (all release candidates)
- Any further work

---

## Session Context

If you are a new AI session reading this file:

1. This is a Jekyll blog project at [sgeos.github.io](https://sgeos.github.io).
2. A documentation knowledge graph exists in `_docs/`. Start at `_docs/README.md`.
3. The project uses scoped conventional commits and Ax-Py-Tz work item coding.
4. `PROMPT.md` is read-only for AI agents. Never modify it. Commit it if the human pilot has changed it.
5. A0 is reserved for non-article work. Twenty-six prompts completed (A0-P1 through A0-P7, A75-P1 through A75-P3, A76-P1 through A76-P4, A77-P1 through A77-P3, A78-P1 through A78-P4, A80-P1, A81-P1, A82-P1, A83-P1, A84-P1).
6. All 74 historical posts have article numbers (A1-A74). A75, A76, A77, and A78 are published. A79, A80, A81, and A82 are release candidates. A83 and A84 are drafts. Next available: A85.
7. Categories are space-separated, not comma-separated.
8. Assets follow `assets/$TYPE/post_$SLUG/$FILENAME` convention.
9. Read `TASKLOG.md` for current task state.
10. Read `CLAUDE.md` at project root for build commands and quick orientation.
11. After publication, include a release announcement draft in REVERSE_PROMPT.md. See `CONTENT_WORKFLOW.md` step 5.
12. The draft summary file was renamed from `old_drafts.md` to `draft_summary.md` in A84-P1.
13. Wait for human prompt before proceeding.
