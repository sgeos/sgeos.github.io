# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-07
**Task**: A76-P1 Draft A76 Article

---

## Verification

### Research Completed
**Result**: PASS. Three research agents deployed in parallel covering the "English as programming language" discourse, markdown as specification language patterns, and structured prompting format comparisons. Agents hit rate limits but gathered substantial data before cutoff. Key sources identified include Karpathy's 2023 tweet, Huang's 2024 and 2025 statements, Welsh's CACM article, the LessWrong analysis, GitHub's spec-driven development blog posts, Thoughtworks industry analysis, Anthropic's context engineering and Agent Skills, and an arxiv study on prompt formatting impact.

### Article Drafted
**Result**: PASS. File created at `_drafts/markdown_as_a_specification_language.markdown`. The article contains 10 content sections, a Conclusion, Future Reading with 5 entries, and References with 16 categorized entries across 7 categories.

---

## Implementation Summary

### Article Structure (A76)

| Section | Content |
|---------|---------|
| Opening | Challenges "English is the new programming language" claim. Argues for structured markdown in the developer's native language. |
| Software Versions | macOS 14.6.1, git implied, Jekyll implied, Claude Code 2.1.37 |
| The Claim | History of the idea from Perlis through Karpathy, Huang, Welsh. |
| The Problem with Unstructured English | LessWrong's six properties analysis. Practical ambiguity example. Vibe coding pattern. |
| Markdown as the Middle Ground | Structural primitives (headers, lists, code blocks, tables). De facto standard for AI config files. |
| Spec-Driven Development | GitHub Spec Kit four-phase workflow. Thoughtworks, Red Hat, JetBrains adoption. Living document philosophy. |
| The Native Language Advantage | Markdown structure is language-agnostic. Non-English developers benefit. Bilingual specification pattern. |
| Format Comparison | Table comparing Plain English, Markdown, YAML/JSON, DSLs. Empirical research on format impact. |
| Pros and Cons | 7 advantages, 4 limitations. |
| Context Engineering | Context rot, progressive disclosure, CLAUDE.md approach, Anthropic Agent Skills. |
| Conclusion | "The specification language for agentic workflows is structured markdown in the developer's native language." |
| Future Reading | 5 entries covering GitHub SDD, Osmani spec guide, prompt formatting research, LessWrong analysis, Anthropic context engineering. |
| References | 16 categorized entries across AI, Claude Code, GitHub, Industry, Protocol, Research. |

### Files Created

| File | Purpose |
|------|---------|
| `_drafts/markdown_as_a_specification_language.markdown` | A76 draft article |

### Files Modified

| File | Changes |
|------|---------|
| `_docs/process/TASKLOG.md` | A76-P1 task state. |
| `_docs/process/REVERSE_PROMPT.md` | This file. |

---

## Questions for Human Pilot

1. **Article scope and depth.** The article covers the topic from historical context through practical comparison to ecosystem adoption. It is longer than A75. Should any sections be expanded, condensed, or removed?

2. **Vibe coding attribution.** The article attributes the term "vibe coding" to Andrej Karpathy in February 2025. This attribution comes from research agent results. If the exact date or context is incorrect, it should be verified before publication.

3. **Format comparison data.** The article cites a study showing 40% performance variation and 18% improvement with markdown formatting. These figures come from an arxiv paper (2411.10541). The paper should be verified for accuracy of these specific numbers before publication.

4. **Native language angle.** The article makes a case for non-English developers using markdown with their native language. This is a distinctive argument not commonly made in the "English as programming language" discourse. Is this angle appropriate for the blog's audience, or should it be condensed?

5. **Software Versions placeholder.** The date and versions in the Software Versions section are carried over from A75. These should be updated with fresh command output before publication.

---

## Technical Concerns / Risks

**Research agent rate limits.** All three research agents hit rate limits before completing their full research scope. The article was drafted from partial results. Some sources may be missing or underrepresented. A supplementary research pass before publication would strengthen the reference list.

**URL verification not performed.** The 16 reference URLs were gathered from research agent web search results and have not been independently verified for reachability.

---

## Intended Next Step

**Awaiting human direction** on:
- Review of the A76 draft
- Answers to questions above
- Whether to proceed to polishing, publication, or revision

---

## Session Context

If you are a new AI session reading this file:

1. This is a Jekyll blog project at [sgeos.github.io](https://sgeos.github.io).
2. A documentation knowledge graph exists in `_docs/`. Start at `_docs/README.md`.
3. The project uses scoped conventional commits and Ax-Py-Tz work item coding.
4. `PROMPT.md` is read-only for AI agents. Never modify it. Commit it if the human pilot has changed it.
5. A0 is reserved for non-article work. Seven prompts completed (A0-P1 through A0-P3, A75-P1 through A75-P3, A76-P1).
6. All 74 historical posts have article numbers (A1-A74). A75 is published. A76 is drafted. Next available: A77.
7. Read `TASKLOG.md` for current task state.
8. Read `CLAUDE.md` at project root for build commands and quick orientation.
9. Wait for human prompt before proceeding.
