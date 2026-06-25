# Git Strategy

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

Version control conventions for the blog repository.

## Branch Model

This project uses a single `master` branch. All commits land directly on `master`. There are no feature branches, pull requests, or protected branch rules. This is appropriate for a single-author blog with AI-assisted development.

Pushing to `master` triggers automatic deployment via GitHub Pages.

## Commit Conventions

### Message Format

```
<scope>: <imperative summary>

<optional body explaining why, not what>

[Task: <task-identifier>]

Co-Authored-By: Claude <noreply@anthropic.com>
```

**Summary line**:
- Use imperative mood ("add" not "added", "fix" not "fixes").
- Keep under 72 characters.
- Scope matches the type of change.

**Body** (when needed):
- Explain motivation and context.
- Note any assumptions or limitations.

**Task reference** (when applicable):
- Use the Ax-Py-Tz work item code. See [Communication](./COMMUNICATION.md) for the coding system.

**Co-author**: Include when the AI agent contributed to the changes.

### Scopes

| Scope | Purpose | Example |
|-------|---------|---------|
| `feat` | New blog post or feature | `feat: publish WASM on Jekyll post` |
| `fix` | Corrections to published content or templates | `fix: CSS example block in AMM post` |
| `docs` | Documentation and knowledge graph changes | `docs: add git strategy to knowledge graph` |
| `refactor` | Restructuring without behavior change | `refactor: extract mathjax into include` |
| `chore` | Maintenance tasks | `chore: update dependencies` |
| `draft` | Work-in-progress draft commits | `draft: add WIP drafts` |

### Commit Timing

The AI agent commits once after all tasks in a prompt are complete, including the `REVERSE_PROMPT.md` update. One commit per prompted request is the standard granularity.

Exceptions where multiple commits are appropriate:
- Logically independent changes that should be separable in history.
- The human pilot explicitly requests intermediate commits.
- Publishing an article, which uses the two-commit pattern described below.

### Two-Commit Publication Pattern

Publishing an article uses two commits:

1. **Draft commit** with a `draft:` scope. The article is staged in `_drafts/` and committed. This captures the draft state in git history before the move.
2. **Publish commit** with a `draft:` scope (the move is part of the same drafting workflow). The article moves to `_posts/` with `git mv` and the date prefix, and the supporting process files such as `_drafts/draft_summary.md` and `_docs/process/REVERSE_PROMPT.md` are updated in the same commit. This commit triggers the deploy on push.

The two-commit pattern is the standard. Never single-commit a publication. The draft commit preserves the historical `_drafts/` location of the file for traceability.

See [Content Workflow](./CONTENT_WORKFLOW.md) for the full publication procedure and [Cross-Linked Series](./CROSS_LINKED_SERIES.md) for the batch variant used for tightly cross-linked series.

### Examples

```
docs: add git strategy to knowledge graph

Adapted from reference project. Excludes GitHub issues, PRs, and
feature branches as unnecessary for a single-author blog.

[Task: A0-P2-T1]

Co-Authored-By: Claude <noreply@anthropic.com>
```

```
feat: publish getting started with Claude Code

Co-Authored-By: Claude <noreply@anthropic.com>
```

## Pre-Push Checklist

Before pushing to `master`:

- [ ] Commit messages follow scoped conventional format
- [ ] No secrets or credentials in committed files
- [ ] Drafts prefixed with `hidden.` are not staged
- [ ] `REVERSE_PROMPT.md` and `TASKLOG.md` are updated if AI-assisted work was performed

## Revision History

| Date | Author | Changes |
|------|--------|---------|
| 2026-02-07 | Claude | Initial creation. Adapted from reference project for blog context. |
| 2026-06-25 | Claude | Added two-commit publication pattern section reflecting practice from the analog-facilities series. |
