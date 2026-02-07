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

```sh
./_publish.sh _drafts/my-post-slug.markdown
```

The publish script performs these steps in order.

1. Extracts the `date:` field from the YAML front matter.
2. Stages the draft file with `git add`.
3. Moves the file to `_posts/YYYY-MM-DD-my-post-slug.markdown` using `git mv`.

The script does not create a git commit. The author commits manually after verifying the move.

### 4. Deploy

Pushing to the `master` branch triggers an automatic Jekyll build and deployment via GitHub Pages. The live site is at [sgeos.github.io](https://sgeos.github.io).

## Hidden Drafts

Drafts prefixed with `hidden.` are excluded from version control by `.gitignore`. This allows work-in-progress content that is not ready for commit.

## Multiple Drafts

The publish script accepts multiple file arguments for batch publication.

```sh
./_publish.sh _drafts/post-one.markdown _drafts/post-two.markdown
```
