# AGENTS.md

Guidance for AI coding assistants other than Claude Code, such as Codex or Grok Build.

## Authoritative source

The project context, conventions and per-session protocol live in
[`CLAUDE.md`](./CLAUDE.md). Despite the name, its content is agent agnostic. Read it before
making any non-trivial change.

## Reading order

1. [`CLAUDE.md`](./CLAUDE.md).
2. [`_docs/process/HANDOFF.md`](./_docs/process/HANDOFF.md), the resume prompt and its
   validity check.
3. [`_docs/process/TASKLOG.md`](./_docs/process/TASKLOG.md), the task state.
4. [`_docs/process/REVERSE_PROMPT.md`](./_docs/process/REVERSE_PROMPT.md), the last report.
5. [`_docs/README.md`](./_docs/README.md), the documentation index.

## Flagged up front

- **Commit once per prompt,** with a scoped conventional commit.
- **Ask before outward-facing actions,** such as pushing, which deploys the site,
  changing settings, or publishing a draft.
- **Scratch directories.** Use `tmp/` for transient files. Its contents are ignored. Never
  commit anything under `secret/` or `.codex/`, and never copy `secret/` into tracked files.
- **Run `./_check.sh` before pushing,** since a push to `master` deploys.
- **Changing a published post's date or categories moves its URL** and needs a redirect.
