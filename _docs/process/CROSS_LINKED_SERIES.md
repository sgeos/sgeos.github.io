# Cross-Linked Series Publication

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

A series whose articles cross-link one another with `{% post_url %}` Liquid tags has two valid publication patterns. The pattern selected affects the build, the deploy, and the order of commits.

## Incremental Publication

Publish one article per day. Each article may resolve a `{% post_url %}` tag only to articles already in `_posts/`. Forward references to later, unpublished articles must be prose only, with no Liquid tag.

This pattern fits a series authored over time, where each article is finalised and reviewed before the next begins. The analog-facilities series at A152 through A160 used this cadence, with each article published the day after the previous.

Workflow per article:
- Draft and review the article.
- Stage and commit in `_drafts/`.
- Move to `_posts/` with `git mv` and commit.
- Push to deploy through GitHub Actions.

The next article in the series may now reference this one via `{% post_url %}` because the target file exists in `_posts/`.

## Batch Publication

Stage every article of the series into `_posts/` together, at which point all internal `{% post_url %}` tags resolve at once, including forward references between articles in the series.

This pattern fits a tightly cross-linked set authored in advance, where forward references are unavoidable. The patents-and-startup series at A161 through A172 used this batch pattern.

Workflow for the batch:
- Confirm article numbers, dates, and slugs across the full batch.
- Verify cross-link integrity: every `{% post_url YYYY-MM-DD-slug %}` references a destination that will exist after the move.
- Stage all drafts to track them. Commit as `_drafts/`.
- Move all files to `_posts/` in a single batch with `git mv`. Commit and push.

Stage the whole series before the deploy build, not one article at a time, or the build fails on the unresolved forward tags. A drafts-only preview likewise fails on the unresolved tags until the batch is staged, which is expected.

## Choosing the Pattern

| Pattern | Use when |
|---------|----------|
| Incremental | Series authored over time; review cycle between articles; no forward cross-references at publication time |
| Batch | Series authored in advance; cross-links span the full series; back-dated to fill a calendar gap |

Both patterns produce identical deployed content. The choice is operational, not editorial.

## Build Verification

Both patterns require the GitHub Actions deploy build to resolve every `{% post_url %}` tag. A `could not find post_url` error in the build log indicates a typo in a slug or a forward reference that should have been prose-only under the incremental pattern.

The local bundle build is broken on macOS per project memory. The deploy build is the authoritative verification. Watch the GitHub Actions log on the push commit to confirm the build completes without `post_url` errors.

## Related Sections

- [Content Workflow](./CONTENT_WORKFLOW.md) for the per-article publication flow
- [Forward-Dated Posts](./FORWARD_DATED_POSTS.md) for the `future: true` configuration that lets future-dated posts deploy immediately
- [Git Strategy](./GIT_STRATEGY.md) for commit conventions
