# Content Workflow

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

The draft-to-publish pipeline for blog content.

## Workflow Steps

### 1. Create Draft

```sh
./_new_draft.sh my-post-slug
```

This copies `_drafts/template.markdown` to `_drafts/my-post-slug.markdown` and opens it in `$EDITOR`. The template provides the required front matter structure and section scaffolding.

### 2. Write and Preview

```sh
./_preview.sh          # http://localhost:4000/
./_preview.sh 8080     # custom port
```

The preview server renders drafts and future-dated posts. It watches for file changes and rebuilds automatically. The server binds to `0.0.0.0` for access from other devices on the local network.

### 3. Publish

The publish step is a `git mv` from `_drafts/` to `_posts/` with the date prefix from the front matter.

```sh
git mv _drafts/my-post-slug.markdown _posts/YYYY-MM-DD-my-post-slug.markdown
```

**The `_publish.sh` script fails on macOS** because it uses GNU sed flags that BSD sed does not accept. Use `git mv` directly. The script may still work on Linux.

The `git mv` preserves the rename in git history so the file's prior commits remain accessible under the new path.

### 4. Two-Commit Publication Pattern

The publication uses two commits:

1. **Draft commit.** The article in `_drafts/` is staged and committed. This captures the draft state in git history before the move.
2. **Publish commit.** The article is moved to `_posts/` with the date prefix, and the supporting process files are updated (typically `_drafts/draft_summary.md` and `_docs/process/REVERSE_PROMPT.md`). The publish commit is what triggers the deploy after push.

The two-commit pattern is the standard. Never single-commit a publication. The draft state in `_drafts/` is part of the working history and is preserved by the first commit.

For a series whose articles cross-link one another, see [Cross-Linked Series](./CROSS_LINKED_SERIES.md) for the incremental and batch publication patterns.

### 5. Deploy

Pushing to the `master` branch triggers an automatic Jekyll build and deployment via GitHub Pages. The live site is at [sgeos.github.io](https://sgeos.github.io).

The local bundle build is broken on macOS in the current development environment; the deploy build is the authoritative verification. Watch the GitHub Actions log on the push commit to confirm the build completes without `could not find post_url` or other errors.

### 6. Release Announcement

After an article is published and deployed, the AI agent should include a draft release announcement in `REVERSE_PROMPT.md` for the human pilot to review before posting on social media.

The announcement follows this template:

```
New Blog Post: <title>

<hook> <brief summary>

Key takeaways:
- <Key takeaway A>
- <Key takeaway B>
- <Key takeaway C>

You can read the full article here:
<URL>

Let me know your thoughts. I would love to hear about <your topical application of material>!

<#hashtags>
```

**URL format**: `https://sgeos.github.io/<categories>/<date-path>/<slug>.html` where `<categories>` is the categories from front matter joined by `/`, `<date-path>` is `YYYY/MM/DD`, and `<slug>` is the filename stem without the date prefix.

**Hashtags**: Use 5-8 relevant hashtags prefixed with `hashtag#` for LinkedIn compatibility. Choose hashtags that reflect the article's primary topics and target audience.

**Tone**: Professional and inviting. The hook should be a single sentence that frames the problem the article addresses. The summary should be 1-2 sentences explaining what the article covers. The closing invitation should relate to the reader's own work.

## Hidden Drafts

Drafts prefixed with `hidden.` are excluded from version control by `.gitignore`. This allows work-in-progress content that is not ready for commit.

## Multiple Drafts

For a series of cross-linked articles published together, see [Cross-Linked Series](./CROSS_LINKED_SERIES.md). The batch publication pattern stages every article into `_posts/` together so internal `{% post_url %}` tags resolve at once.

## Forward-Dated and Back-Dated Posts

The site sets `future: true` in `_config.yml`. Forward-dated posts render at deploy time and sit at their future date position in chronological listings until the date arrives. Back-dated posts render immediately at their past position. See [Forward-Dated Posts](./FORWARD_DATED_POSTS.md) for the full behaviour.

## Related Sections

- [Cross-Linked Series](./CROSS_LINKED_SERIES.md) for series-level publication patterns
- [Forward-Dated Posts](./FORWARD_DATED_POSTS.md) for the `future: true` configuration
- [Publication Review](./PUBLICATION_REVIEW.md) for the pre-publish review pass
- [Style Verification](./STYLE_VERIFICATION.md) for the verification scripts
- [URL Verification](./URL_VERIFICATION.md) for URL checking
- [Git Strategy](./GIT_STRATEGY.md) for commit conventions
- [Sister Session](./SISTER_SESSION.md) for parallel-session coordination
