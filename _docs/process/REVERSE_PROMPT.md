# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-08
**Task**: A80-P1 Draft Statistics Reference Post, Update Old Drafts

---

## Verification

### Statistics Reference Post Drafted
**Result**: PASS. `_drafts/statistics.markdown` rewritten from a 207-line formula sheet to a complete reference article. Assigned A80. 9 references across 4 categories (Book, Reference, Tool). Research incorporated covering probability distributions, hypothesis testing, confidence intervals, and sample size determination. MathJax corrected throughout.

### Old Drafts Updated for Release Candidates
**Result**: PASS. Writing Proofs (A79) and Statistics Reference (A80) marked as release candidates in `old_drafts.md`. Summary tier structure updated to reflect the new status.

---

## Implementation Summary

### Files Created/Modified

| File | Changes |
|------|---------|
| `_drafts/statistics.markdown` | Rewritten from formula sheet to full A80 draft. 9 references. Covers distributions, hypothesis testing, confidence intervals, sample size. MathJax corrected. |
| `_drafts/old_drafts.md` | Writing Proofs and Statistics Reference sections updated to "Release Candidate" status. Summary tiers updated. |
| `_docs/process/PROMPT.md` | Human-updated with A80-P1 instructions. Committed as-is. |
| `_docs/process/TASKLOG.md` | A80-P1 task state. |
| `_docs/process/REVERSE_PROMPT.md` | This file. |

### A80 Article Structure

| Section | Content |
|---------|---------|
| Opening | What statistics is, why it matters to engineers, post scope as a reference |
| Software Versions | Standard environment block |
| Notation | Symbol table for all notation used in the article |
| Probability Distributions | Binomial PMF, Normal PDF, Poisson PMF with mean/variance |
| Normal Approximation | Approximation conditions, continuity correction table |
| Descriptive Statistics | Sample mean, sample and population variance, standard deviation |
| Law of Total Probability | Two-partition form, rearrangements |
| Bayes' Theorem | Standard form, expanded denominator, applications |
| Central Limit Theorem | CLT statement, standard error, rule of thumb |
| Hypothesis Testing | Framework, type errors, Z-test, t-test, proportion test, general form |
| Confidence Intervals | General form, mean (known/unknown variance), variance, proportion, difference of means, difference of proportions, pooled proportion |
| Sample Size Determination | For proportion (worst-case), for mean |
| Summary | When methods apply, their assumptions and limitations |
| Future Reading | 5 entries (NIST, Seeing Theory, Wasserman, Bruce, Ross) |
| References | 9 entries across 4 categories (Book, Reference, Tool) |

### Changes from Original Draft

| Aspect | Original | A80 |
|--------|----------|-----|
| Length | ~207 lines | ~547 lines |
| Prose | None (formula sheet only) | Explanatory prose for every section |
| Title | "Statistics" | "Probability and Statistics Reference" |
| Article number | None | A80 |
| Notation | Undefined | Formal notation table |
| Distributions | Binomial only | Binomial, Normal, Poisson |
| Bayes' Theorem | Absent | Full section with expanded form |
| CLT | Absent | Full section with standard error |
| t-test | Absent | Full section |
| CI for mean | Absent | Known and unknown variance forms |
| Sample size | Absent | For proportion and mean |
| Continuity correction | Inline align block (broken rendering) | Markdown table |
| MathJax | Broken (spurious `\\`, `\mp` errors) | Corrected throughout |
| References | None | 9 across 4 categories |

---

## Questions for Human Pilot

No questions. All objectives from PROMPT.md have been met.

---

## Technical Concerns / Risks

**MathJax rendering.** A80 uses MathJax extensively with both inline and display math. The human pilot should preview locally to verify rendering, particularly the continuity correction table, the chi-squared confidence interval notation, and the pooled standard error formula.

**URL verification.** Reference URLs were gathered by research agent and have not been manually verified. The human pilot should verify all 9 URLs before publication.

**Scope assessment.** A80 covers introductory undergraduate probability and statistics. The human pilot should assess whether the scope is appropriate or whether any sections should be added, trimmed, or expanded. Potential additions at this level include correlation/regression, chi-squared goodness-of-fit test, and ANOVA, but these would increase the article length significantly.

---

## Intended Next Step

**Awaiting human direction** on:
- Review of the A80 draft
- Whether to polish, revise, or proceed to publication for A79 and A80
- Publication timing for A78 (noted as ready in previous PROMPT.md comments)
- Any action on the candidate future post topics in old_drafts.md

---

## Session Context

If you are a new AI session reading this file:

1. This is a Jekyll blog project at [sgeos.github.io](https://sgeos.github.io).
2. A documentation knowledge graph exists in `_docs/`. Start at `_docs/README.md`.
3. The project uses scoped conventional commits and Ax-Py-Tz work item coding.
4. `PROMPT.md` is read-only for AI agents. Never modify it. Commit it if the human pilot has changed it.
5. A0 is reserved for non-article work. Twenty prompts completed (A0-P1 through A0-P6, A75-P1 through A75-P3, A76-P1 through A76-P4, A77-P1 through A77-P3, A78-P1 through A78-P3, A80-P1).
6. All 74 historical posts have article numbers (A1-A74). A75, A76, and A77 are published. A78, A79, and A80 are drafted. Next available: A81.
7. Categories are space-separated, not comma-separated.
8. Assets follow `assets/$TYPE/post_$SLUG/$FILENAME` convention.
9. Read `TASKLOG.md` for current task state.
10. Read `CLAUDE.md` at project root for build commands and quick orientation.
11. After publication, include a release announcement draft in REVERSE_PROMPT.md. See `CONTENT_WORKFLOW.md` step 5.
12. Wait for human prompt before proceeding.
