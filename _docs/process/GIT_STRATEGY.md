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
