# Sister Session Coordination

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

How to operate when a second AI session is drafting content in parallel into the same repository.

## Context

A sister session is another AI session, typically with its own working directory or repository scope, that drafts blog content into the same `_drafts/` directory as the master session. The sister session can produce articles in its own series without conflicting with the master session's work, as long as both sessions follow the coordination rules below.

The patents-and-startup series at A161 through A172 was authored by a sister session in an adversarial case intelligence repository and published in batch by the master session.

## Master Session Role

The session operating in the blog repository is the master session. The master session executes git operations, runs the local build (when available), and triggers deploys through push. The sister session writes drafts but does not commit or push directly.

## Coordination Rules

### Draft Territory

- Sister session drafts appear in `_drafts/` as untracked files. The master session does not stage, edit, or commit them until the sister session signals readiness through the human pilot.
- The master session does not modify sister session drafts unless explicitly directed.
- The sister session may extend `_drafts/draft_summary.md` with its own entries, or maintain its own summary document. The master session's draft summary tracks the master session's own series.

### Article Numbers

- Sister session article numbers are deferred until publication. The master session reserves its forward range and leaves a buffer for the sister.
- When the sister session delivers a batch for publication, the human pilot relays the article number and date assignments. The master session does not assign numbers to sister session drafts on its own initiative.
- If both sessions need to assign numbers concurrently, the human pilot adjudicates.

### Dates

- The sister session typically uses back-dated articles to fill calendar gaps without colliding with the master session's forward-dated work.
- Date collisions are avoided by convention: the master session announces its forward-dated range, and the sister session selects dates outside that range.

### Repository Scope

- The master session does not enter the sister session's working repository.
- The master session does not touch the secret keleusma research repository at `/Users/bsechter/projects/rust/keleusma/secret/` per the recorded preference.

## Batch Publication Flow

When the sister session signals a batch ready for publication, the human pilot relays a prompt with the explicit file-to-date mapping and the article numbers. The master session executes the batch under [Cross-Linked Series](./CROSS_LINKED_SERIES.md) batch publication pattern:

1. Stage all sister session drafts in `_drafts/` to track them.
2. Commit the drafts in `_drafts/` location as one commit (preserves draft state in git history).
3. Move all drafts to `_posts/` with date prefixes in a single batch through `git mv`.
4. Commit the publication move and update [REVERSE_PROMPT.md](./REVERSE_PROMPT.md).
5. Push to deploy.

No content edits during the batch. The sister session is responsible for the article content; the master session is responsible for the publication mechanics.

## Status Tracking

[REVERSE_PROMPT.md](./REVERSE_PROMPT.md) records the master session's actions including any sister session batch publication. A "Sister Session Coordination" section in the reverse prompt documents which drafts are present, which have been published, and the article number range reserved for the sister session.

## Concurrency Model

Both sessions can operate at the same wall-clock time without interfering, as long as:

- The master session's commits remain on the master branch and push to origin.
- The sister session does not commit or push directly.
- Untracked draft files appear in `_drafts/` from the sister session and the master session ignores them until publication is requested.

This is a cooperative model. No automated conflict detection guards against violations. The conventions above are the convention.

## Related Sections

- [Cross-Linked Series](./CROSS_LINKED_SERIES.md) for the batch publication pattern
- [Git Strategy](./GIT_STRATEGY.md) for commit conventions
- [Reverse Prompt](./REVERSE_PROMPT.md) for status reporting
