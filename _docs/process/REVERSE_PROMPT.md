# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-09
**Task**: A84-P2 Verify A83 Edits, Fully Draft A84

---

## Verification

### A83 Edits Verified
**Result**: PASS. Human edits to pipeline placeholder (`@` to `_`), expanded examples (4 variants), and expanded semantics (zero or more placeholders, implicit first parameter, multi-placeholder) are sound design changes. Typo "parmeter" corrected to "parameter". Prose "the same value is slotted to be passed into multiple parameters" tightened to "the piped value is substituted at each placeholder position".

### A84 Fully Drafted
**Result**: PASS. `_drafts/llm_mad_libs_experiment.markdown` fully rewritten from ~268-line draft to ~506-line researched article. 10 references across 2 categories (Reference, Research). Step 3 logical fill output included. New "Sycophancy in the Literature" section. Expanded Implications.

---

## Implementation Summary

### Files Created/Modified

| File | Changes |
|------|---------|
| `_drafts/safe_embedded_functional_control_dsl.markdown` | Typo "parmeter" fixed to "parameter". Prose tightened for pipeline multi-placeholder description. |
| `_drafts/llm_mad_libs_experiment.markdown` | Fully rewritten. 506 lines. 10 references. Three-session experiment with Step 3 output. Sycophancy literature section. Expanded implications. |
| `_drafts/draft_summary.md` | A84 elevated to release candidate. Removed from Tier 2. Summary updated (6 release candidates). |
| `_docs/process/PROMPT.md` | Human-updated with A84-P2 instructions. Committed as-is. |
| `_docs/process/TASKLOG.md` | A84-P2 task state. |
| `_docs/process/REVERSE_PROMPT.md` | This file. |

### A84 Article Structure

| Section | Content |
|---------|---------|
| Opening | LLMs as blank-fillers, sycophantic compliance, Sharma et al. citation, three-session experiment introduction |
| Software Versions | Standard environment block |
| The Experiment | Step 1: dark template generation (Session A). Step 2: cheerful fill (Session B). Step 3: logical fill (Session C, NEW). |
| Observations | 4 observations: compliance by default, template structure carries meaning, instruction compliance overrides pattern matching, logical fill reveals understanding. Research citations woven in. |
| Sycophancy in the Literature (NEW) | Sharma et al. (ICLR 2024), RLHF amplification, reward hacking (Weng), specification gaming (Krakovna et al.), Goodhart's Law, instruction hierarchy (Wallace et al.), Constitutional AI |
| Implications (EXPANDED) | Mental model for LLM interaction, prompt engineering consequences, OWASP prompt injection connection, application design constraints, alignment gap |
| Summary | Three-session recap, compliance-not-comprehension distinction, sycophancy and instruction hierarchy literature, practitioner takeaway |
| Future Reading | 6 entries (sycophancy paper, reward hacking, specification gaming, instruction hierarchy, Anthropic Constitution, HELM) |
| References | 10 entries across 2 categories (3 Reference, 7 Research) |

### Changes from A84-P1 Draft

Major rewrite. The A84-P1 draft was a reformatted version of experiment notes with no research and no references. The A84-P2 version:
- Added Step 3 (logical fill) output as a concrete example, completing the three-session experiment
- Added "Sycophancy in the Literature" section covering six research topics
- Expanded Observations with research citations supporting each finding
- Expanded Implications with OWASP prompt injection connection and alignment gap discussion
- Added opening paragraph citing Sharma et al. to frame the article in the research literature
- Added 10 references from authoritative sources (arXiv, Alignment Forum, OWASP, Stanford, Anthropic)

---

## Questions for Human Pilot

**Step 3 output.** The Step 3 "logical fill" output (Session C) was generated to demonstrate what a context-aware fill produces. The human pilot should verify that this output is acceptable for publication. If the human pilot has actual LLM output from a real Session C, it should replace the generated version.

**Categories.** The article uses categories "ai ai-tools". The human pilot should confirm these are acceptable. "alignment" or "safety" could be alternatives given the sycophancy focus.

**Sycophancy in the Literature section.** This section references researchers by name (Sharma et al., Weng, Krakovna et al., Wallace et al.). The human pilot should confirm that naming researchers is consistent with the blog's style.

---

## Technical Concerns / Risks

**URL verification.** All 10 reference URLs should be verified before publication. Most point to arXiv papers, official project sites, and established research platforms.

**Step 3 authenticity.** The Step 3 output was generated to complete the article structure. For maximum authenticity, the human pilot may wish to run the actual experiment and replace the output with real LLM responses.

---

## Intended Next Step

**Awaiting human direction** on:
- Review of the A83 prose corrections
- Review of the A84 draft
- Publication timing for release candidates (A79, A80, A81, A82, A83, A84)
- Any further work

---

## Session Context

If you are a new AI session reading this file:

1. This is a Jekyll blog project at [sgeos.github.io](https://sgeos.github.io).
2. A documentation knowledge graph exists in `_docs/`. Start at `_docs/README.md`.
3. The project uses scoped conventional commits and Ax-Py-Tz work item coding.
4. `PROMPT.md` is read-only for AI agents. Never modify it. Commit it if the human pilot has changed it.
5. A0 is reserved for non-article work. Twenty-nine prompts completed (A0-P1 through A0-P7, A75-P1 through A75-P3, A76-P1 through A76-P4, A77-P1 through A77-P3, A78-P1 through A78-P4, A80-P1, A81-P1, A82-P1, A83-P1, A83-P2, A84-P1, A84-P2, A85-P1).
6. All 74 historical posts have article numbers (A1-A74). A75, A76, A77, and A78 are published. A79, A80, A81, A82, A83, and A84 are release candidates. A85 is a draft. Next available: A86.
7. Categories are space-separated, not comma-separated.
8. Assets follow `assets/$TYPE/post_$SLUG/$FILENAME` convention.
9. Read `TASKLOG.md` for current task state.
10. Read `CLAUDE.md` at project root for build commands and quick orientation.
11. After publication, include a release announcement draft in REVERSE_PROMPT.md. See `CONTENT_WORKFLOW.md` step 5.
12. The draft summary file was renamed from `old_drafts.md` to `draft_summary.md` in A84-P1.
13. A83 depends on A79 via post_url. A79 must be published before A83.
14. Wait for human prompt before proceeding.
