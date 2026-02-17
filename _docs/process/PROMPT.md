# Prompt Staging Area

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is a staging area for complex human-to-AI instructions. The human pilot drafts and refines prompts here before execution.

---

# Current Prompt

## Comments

Currently reading through the following drafts:
- Android Development on FreeBSD
- Claude Code on FreeBSD

## Objectives

### Draft Claude Code on OpenBSD

Draft a "Getting Started with Claude Code on OpenBSD" article.
It should mirror the "Claude Code on FreeBSD" article.
My understanding is that there is no claude-code package or port for OpenBSD.
Note that by design, OpenBSD is generally hostile to “assume-Linux” software.

**The "Bun" Hurdle:**
Claude Code is built using the Bun runtime.
While Bun has been making progress on BSD compatibility,
it is not yet fully stable on OpenBSD,
which makes running the native Claude Code binary very difficult.

**Workaround:**
Some users have had limited success by installing it via npm (assumes Node.js 18+ installed),
though many of the sandboxing features which rely on Linux-specific kernel features
like namespaces will not work.

Note package installation and port building instructions.
Note setting `USE_BUILTIN_RIPGREP=0` if the CLI is misbehaving on a BSD system,
if this can be verified to be advisable.

Please research this problem and state limitations.
Do not slot for publication, but tentatively use the next publication date slot
for lack of a better alternative.

## Context

Working on backlog posts for next week.
Converting drafts to full posts.

## Constraints

Do not yet assign an article number.

## Success Criteria

- "Getting Started with Claude Code on OpenBSD" article in pre-release candidate state
  ready for verification on OpenBSD.

## Notes

(none)
