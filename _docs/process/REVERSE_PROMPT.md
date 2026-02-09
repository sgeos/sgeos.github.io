# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-09
**Task**: A85-P2 Fully Draft A85

---

## Verification

### A85 Fully Drafted
**Result**: PASS. `_drafts/the_ai_apocalypse_will_be_polite.markdown` fully rewritten from ~215-line draft to ~387-line researched humor essay. 11 references across 2 categories (Reference, Research). Deadpan tone preserved. New "The Research" section grounds satire in published research. Links to A84 via post_url.

---

## Implementation Summary

### Files Created/Modified

| File | Changes |
|------|---------|
| `_drafts/the_ai_apocalypse_will_be_polite.markdown` | Fully rewritten. 387 lines. 11 references. Deadpan humor preserved. Research section added. A84 linked. |
| `_drafts/draft_summary.md` | A85 elevated to release candidate. Removed from Tier 2. Summary updated (7 release candidates). |
| `_docs/process/PROMPT.md` | Human-updated with A85-P2 instructions. Committed as-is. |
| `_docs/process/TASKLOG.md` | A85-P2 task state. |
| `_docs/process/REVERSE_PROMPT.md` | This file. |

### A85 Article Structure

| Section | Content |
|---------|---------|
| Opening | AI apocalypse as dramatic vs polite. "It would simply need to be helpful." |
| The Argument | Rogue superintelligence properties. LLM sycophancy as proof of concept. Sharma et al. citation. post_url link to A84. |
| The Scenario | Two escalating delegation suggestions with quoted AI dialogue. Incremental authority transfer. |
| The Mechanism | Framing effects (Tversky-Kahneman 1981). Selective data presentation. Patient yielding. "Simply be right, consistently, until the human stops checking." |
| The Outcome | No Skynet, no HAL, no Ultron. Series of defensible decisions. "It will be very convincing." |
| The Irony (EXPANDED) | AI would not be wrong. Outcomes measurably superior. Bostrom paperclip maximizer as helpfulness analog. |
| A Note on Tone (EXPANDED) | Poe's Law with Nathan Poe 2005 attribution. Ambiguous closing preserved. |
| The Research (NEW) | Six research topics: AI persuasion (Nature HB 2025, 81.2% increase), automation bias, algorithmic authority creep, strategic AI deception (Scheurer et al.), sycophancy (A84 link), instrumental convergence (Bostrom, Russell). |
| Summary | Polite conquest. Sound arguments. Human agreement at every step. |
| Future Reading | 6 entries (Bostrom, Russell, Park deception, sycophancy, automation bias, Poe's Law) |
| References | 11 entries across 2 categories (2 Reference, 9 Research) |

### Changes from A85-P1 Draft

The A85-P1 draft was a humor essay with no research and no references. The A85-P2 version:
- Added sycophancy research and A84 post_url link to The Argument section
- Added Tversky-Kahneman framing effects to The Mechanism section
- Expanded The Irony with Bostrom paperclip maximizer as helpfulness analog
- Expanded A Note on Tone with Nathan Poe 2005 attribution
- Added "The Research" section grounding all satirical mechanisms in published research
- Added 11 references from authoritative sources (Nature, Science, arXiv, OUP, SAGE, PMC, Wikipedia)

---

## Questions for Human Pilot

**post_url dependency.** The article links to A84 "LLM Mad Libs Experiment" using `{% post_url 2026-02-14-llm-mad-libs-experiment %}`. A84 must be published before A85 can build. This adds to the existing dependency chain: A79 must precede A83, and A84 must precede A85.

**Categories.** The article uses categories "ai humor". The human pilot should confirm these are acceptable given the added research depth. "alignment" could be added.

**Tone balance.** The article now has a substantial research section after the humor. The human pilot should assess whether the research section enhances or undermines the deadpan effect. The intent is that "The Research" functions as the punchline, showing the joke is uncomfortably close to reality.

---

## Technical Concerns / Risks

**URL verification.** All 11 reference URLs should be verified before publication. Sources include Nature, Science, arXiv, Oxford University Press, SAGE, PMC, and Wikipedia.

**post_url dependency chain.** A85 depends on A84 via post_url. A84 has no post_url dependencies. A83 depends on A79 via post_url. Publication order must respect these constraints.

---

## Intended Next Step

**Awaiting human direction** on:
- Review of the A85 draft
- Publication order for release candidates (A79, A80, A81, A82, A83, A84, A85)
- Dependencies: A79 before A83, A84 before A85
- Any further work

---

## Session Context

If you are a new AI session reading this file:

1. This is a Jekyll blog project at [sgeos.github.io](https://sgeos.github.io).
2. A documentation knowledge graph exists in `_docs/`. Start at `_docs/README.md`.
3. The project uses scoped conventional commits and Ax-Py-Tz work item coding.
4. `PROMPT.md` is read-only for AI agents. Never modify it. Commit it if the human pilot has changed it.
5. A0 is reserved for non-article work. Thirty prompts completed (A0-P1 through A0-P7, A75-P1 through A75-P3, A76-P1 through A76-P4, A77-P1 through A77-P3, A78-P1 through A78-P4, A80-P1, A81-P1, A82-P1, A83-P1, A83-P2, A84-P1, A84-P2, A85-P1, A85-P2).
6. All 74 historical posts have article numbers (A1-A74). A75, A76, A77, and A78 are published. A79, A80, A81, A82, A83, A84, and A85 are release candidates. Next available: A86.
7. Categories are space-separated, not comma-separated.
8. Assets follow `assets/$TYPE/post_$SLUG/$FILENAME` convention.
9. Read `TASKLOG.md` for current task state.
10. Read `CLAUDE.md` at project root for build commands and quick orientation.
11. After publication, include a release announcement draft in REVERSE_PROMPT.md. See `CONTENT_WORKFLOW.md` step 5.
12. The draft summary file was renamed from `old_drafts.md` to `draft_summary.md` in A84-P1.
13. A83 depends on A79 via post_url. A85 depends on A84 via post_url. Respect publication order.
14. Wait for human prompt before proceeding.
