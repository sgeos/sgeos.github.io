# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-07
**Task**: A75-P1 Article Publishing Procedures and A75 Draft

---

## Verification

### Same-Date Ordering Policy Documented
**Result**: PASS. Publication Ordering section added to `_docs/writing/POST_STRUCTURE.md` covering the avoid-same-date policy, previous/future day reassignment, and the acceptability of slightly out-of-order article numbers from tactical publication.

### Draft Numbering Clarification
**Result**: PASS. Acknowledged. Existing drafts remain unnumbered. Numbers assigned at publication time.

### Article A75 Drafted
**Result**: PASS. File created at `_drafts/bidirectional_agentic_workflow.markdown`.
- Front matter: layout, mathjax, comments, title, date, categories all set.
- Article comment: `<!-- A75 -->` with blank lines.
- Sections: Opening summary, Software Versions, Instructions (protocol documentation with 8 subsections), workflow diagram, comparison with 6 other approaches, Summary, Future Reading, References.
- References: 20 reference-style links to external sources.

---

## Implementation Summary

### Decisions Documented

| Decision | Location | Summary |
|----------|----------|---------|
| Same-date ordering | `POST_STRUCTURE.md` | Avoid same-date publication. Use adjacent dates. Article numbers indicate publication order. |
| Draft numbering | Acknowledged | Drafts remain unnumbered until publication decision. |

### Files Created

| File | Purpose |
|------|---------|
| `_drafts/bidirectional_agentic_workflow.markdown` | A75 draft article |

### Files Modified

| File | Changes |
|------|---------|
| `_docs/writing/POST_STRUCTURE.md` | Added Publication Ordering section |
| `_docs/process/TASKLOG.md` | A75-P1 task state |
| `_docs/process/REVERSE_PROMPT.md` | This file |

### Article Structure (A75)

The draft covers the bidirectional protocol in a way that can be replicated by others, with a link to the GitHub repository as a reference implementation. The comparison section situates the protocol against six other approaches.

| Section | Content |
|---------|---------|
| Opening | Meta-note that the article was drafted using the protocol it describes |
| Software Versions | macOS 14.6.1, git 2.52.0, Jekyll 4.2.2 |
| The Problem | Stateless agents, lost context, developer as sole state keeper |
| The Bidirectional Protocol | Three-file system: PROMPT.md, REVERSE_PROMPT.md, TASKLOG.md |
| Forward Prompt | Structure, read-only rule, version control benefits |
| Reverse Prompt | Structure, session context section, blocking protocol |
| Task Log | Shared state, verification requirement |
| Session Startup | Three-step protocol |
| Work Item Traceability | Ax-Py-Tz coding system |
| Supporting Infrastructure | Scoped commits, knowledge graph |
| Workflow Diagram | ASCII art showing the full cycle |
| Comparison | Fully autonomous, inline pair programming, spec-driven, breadcrumb, CLAUDE.md/AGENTS.md, bounded autonomy |
| Summary | Middle ground between autonomy and interactivity |
| Future Reading | 5 recommended resources |
| References | 20 reference-style links |

---

## Questions for Human Pilot

1. **Article tone and depth?** The draft is written in the blog's academic, tutorial style. It leans toward explaining the protocol in sufficient detail for a reader to replicate it, with comparisons to provide context. Should the tone be adjusted, or should certain sections be expanded or condensed?

2. **Reference link verification?** The 20 reference URLs were gathered from web research. Some URLs may have changed or become unavailable between research time and publication. A verification pass on the links before publication would be prudent. Should this be done now or deferred to the publication prompt?

3. **Workflow diagram format?** The workflow diagram uses ASCII art, which is consistent with the blog's code-block conventions. An alternative would be an HTML/CSS diagram or an image. Is the ASCII format acceptable?

4. **Publication timing?** The draft date is set to 2026-02-07. Should this be adjusted when the article is ready for publication, or should it retain the draft date?

---

## Technical Concerns / Risks

**Self-referential nature**: The article references the repository it lives in as the "reference implementation." This creates a circular dependency where the article describes a protocol that is documented in the same repository. This is intentional and noted in the opening paragraph, but readers should be aware that the protocol documentation in `_docs/` is the authoritative source and the blog post is an overview.

**URL stability**: Several references point to blog posts and documentation pages that may move or be restructured. The reference-style link format makes future URL updates straightforward since all URLs are defined at the bottom of the file.

**Draft status**: The article is in `_drafts/` and will not appear on the published site until moved to `_posts/` via `_publish.sh`. The draft can be previewed locally with `./_preview.sh`.

---

## Intended Next Step

**Awaiting human direction** on:
- Review of the A75 draft
- Answers to questions above
- Whether to proceed to publication or revise

---

## Session Context

If you are a new AI session reading this file:

1. This is a Jekyll blog project at [sgeos.github.io](https://sgeos.github.io).
2. A documentation knowledge graph exists in `_docs/`. Start at `_docs/README.md`.
3. The project uses scoped conventional commits and Ax-Py-Tz work item coding.
4. `PROMPT.md` is read-only for AI agents. Never modify it. Commit it if the human pilot has changed it.
5. A0 is reserved for non-article work. Four prompts completed (A0-P1 through A0-P3, A75-P1).
6. All 74 published posts have article numbers (A1-A74). Next available: A76.
7. A75 ("Bidirectional Agentic Workflow") is drafted in `_drafts/`.
8. Read `TASKLOG.md` for current task state.
9. Read `CLAUDE.md` at project root for build commands and quick orientation.
10. Wait for human prompt before proceeding.
