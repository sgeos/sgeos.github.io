# Process

> **Navigation**: [Documentation Root](../README.md)

Development process, content workflow, and human-AI communication protocol.

## Contents

| Document | Description |
|----------|-------------|
| [Handoff Prompt](./HANDOFF.md) | Self-contained resume prompt written before a planned compaction, with a commit-stamped validity check |
| [Content Workflow](./CONTENT_WORKFLOW.md) | Draft, preview, and publish pipeline with the two-commit pattern |
| [Cross-Linked Series](./CROSS_LINKED_SERIES.md) | Incremental and batch publication patterns for cross-linked series |
| [Forward-Dated Posts](./FORWARD_DATED_POSTS.md) | Behaviour of forward-dated and back-dated posts under `future: true` |
| [Publication Review](./PUBLICATION_REVIEW.md) | Systematic review pass before publication |
| [Research Agent](./RESEARCH_AGENT.md) | Pattern for verifying factual claims with a background agent |
| [URL Verification](./URL_VERIFICATION.md) | URL response-code rules and the catalogue of canonical bot-detected sites |
| [Style Verification](./STYLE_VERIFICATION.md) | Verification scripts for style, references, math, and URLs |
| [Sister Session](./SISTER_SESSION.md) | Coordination when a second session drafts in parallel |
| [Communication](./COMMUNICATION.md) | Bidirectional human-AI communication protocol |
| [Git Strategy](./GIT_STRATEGY.md) | Commit conventions and the two-commit publication pattern |
| [PR Strategy](./PR_STRATEGY.md) | Process for handling incoming pull requests including author investigation |

## Session Working Documents

| Document | Direction | Description |
|----------|-----------|-------------|
| [HANDOFF.md](./HANDOFF.md) | AI to AI | Commit-stamped resume prompt for post-compaction continuity. Not kept current; validated on resume |
| [TASKLOG.md](./TASKLOG.md) | Shared | Current task state and verification log |
| [PROMPT.md](./PROMPT.md) | Human to AI | Staging area for complex instructions |
| [REVERSE_PROMPT.md](./REVERSE_PROMPT.md) | AI to Human | Questions, concerns, and status reports |

## Session Startup Protocol

1. Read [HANDOFF.md](./HANDOFF.md) and run its validity check, comparing its recorded parent commit to `git rev-parse HEAD~1`. Report it as valid, or as invalid-and-stale on a mismatch, per its Validity section. A stale handoff must not be trusted; fall back to the live channels below.
2. Read [TASKLOG.md](./TASKLOG.md) for current task state.
3. Read [REVERSE_PROMPT.md](./REVERSE_PROMPT.md) for last AI communication.
4. Wait for human prompt before proceeding.

## Related Sections

- [Writing](../writing/README.md) for content conventions
- [Architecture](../architecture/README.md) for Jekyll site structure
- [Reference](../reference/README.md) for the common-errors catalogue
