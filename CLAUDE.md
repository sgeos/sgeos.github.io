# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Jekyll-based static blog deployed to GitHub Pages at [sgeos.github.io](https://sgeos.github.io). The repository is the source for the live site. Pushing to `master` triggers automatic Jekyll builds and deployment via GitHub Pages.

## Common Commands

**Preview locally (published and future-dated posts; drafts off by default):**
```sh
./_preview.sh            # serves at http://localhost:4000/
./_preview.sh 8080       # custom port
DRAFTS=1 ./_preview.sh   # include drafts (aborts if a draft has an unresolved post_url)
FUTURE=0 ./_preview.sh   # hide forward-dated posts, matching the live site
```

Drafts are off by default because `--drafts` builds the `_drafts/` directory, and
release-candidate drafts that cross-reference one another with `post_url` tags pointing at
unpublished filenames make that build fail. Use `DRAFTS=1` only once those references resolve.

**Build the way CI does when verifying.** `bundle install` works; the bundle was never broken,
merely never installed. `JEKYLL_ENV=production bundle exec jekyll build --baseurl ""` reproduces
the deploy closely, including `jekyll-archives`. Do not verify against a Gemfile-free build with
plugins stripped; it reports hundreds of phantom broken links and hides real ones. See
[`_docs/process/CROSS_LINKED_SERIES.md`](_docs/process/CROSS_LINKED_SERIES.md).

**The preview does not match the live site for forward-dated posts by default.** `_preview.sh`
passes `--future`, so it renders posts dated ahead of today. The site sets `future: false`, so
those same posts are excluded from the real build and return 404 until their dates arrive. A
clean default preview is therefore not evidence that a forward-dated cross-reference is safe.
Run `FUTURE=0 ./_preview.sh` to match production. See
[`_docs/process/FORWARD_DATED_POSTS.md`](_docs/process/FORWARD_DATED_POSTS.md).

**Verify corpus invariants (runs in CI before every build):**
```sh
python3 _verify.py           # errors and warnings; exits nonzero on error
python3 _verify.py --strict  # treat warnings as errors too
```

Checks date collisions, filename versus front matter dates, UTC offsets, reference integrity,
link-definition ordering, duplicate article numbers, shadowed first categories, math validity,
prose style, and word-frequency outliers. Every check exists because that defect actually
shipped. Citation and URL verification needs the network and lives separately.

**Create a new draft:**
```sh
./_new_draft.sh my-post-slug   # creates _drafts/my-post-slug.markdown from template
```

**Publish a draft (moves from `_drafts/` to `_posts/` with date prefix from front matter):**
```sh
./_publish.sh _drafts/my-post-slug.markdown
```

The publish script extracts the `date:` field from YAML front matter, stages the file with `git add`, then uses `git mv` to rename it into `_posts/YYYY-MM-DD-my-post-slug.markdown`. It does not commit automatically.

## Content Authoring

Posts use Markdown with YAML front matter. The template at `_drafts/template.markdown` defines the required structure:

```yaml
---
layout: post
mathjax: false
comments: true
title:  "Post Title"
date:   2026-01-01 00:00:00 +0000
categories:
---
```

- Set `mathjax: true` to enable LaTeX math rendering. Inline math uses `$...$` or `\(...\)`.
- Set `comments: true` to enable Giscus comments on the post. Giscus stores comments as GitHub Discussions in this repository.
- Series metadata: set `series: <slug>`, `series_title: <human title>`, and `series_index: <N>` on each post in a series. The post layout auto-generates a compact context header near the top ("Part N of M in Series Title") and a full table-of-contents nav at the bottom with previous and next links. Posts sharing the same `series:` slug are grouped and sorted by `series_index:`.
- Automatic table of contents. A TOC injects at the top of the article on posts with four or more H2/H3 headings and at least 800 words. Suppress per post with `toc: false` in front matter. Take manual control by placing `* Contents \n {:toc}` in the post markdown; kramdown generates a TOC in that location and the auto-injector defers.
- Published post filenames follow the pattern `_posts/YYYY-MM-DD-slug.markdown`.
- Drafts prefixed with `hidden.` are gitignored and will not be committed.
- Do not use `keleusma` as the first category. The `sgeos/keleusma` repository serves its own GitHub Pages site at `https://sgeos.github.io/keleusma/` which shadows any URL under that path prefix. Jekyll's default permalink places the first category first in the URL, so any post with `categories: keleusma ...` returns 404 despite building correctly. Place a more general category first, such as `compilers`, `operating-systems`, or `programming-languages`. See [`_docs/writing/POST_STRUCTURE.md`](_docs/writing/POST_STRUCTURE.md) for the full explanation and additional shadowed-path guidance.
- **Every category appears in the post URL, not only the first.** Jekyll's default permalink is `/:categories/:year/:month/:day/:title.html` and `:categories` is the whole list joined. **Renaming or removing a category anywhere in the list moves the post and 404s its old address.** This bit on 2026-08-11: renaming `c++` to `cpp`, in fourth and third position respectively, broke two live 2022 URLs after a change believed to be URL-neutral because the category was not first. Any category change to a published post therefore needs a `redirects/` entry. See below.
- **Two categories that slugify to the same string destroy an archive page.** `c` and `c++` both slugify to `c`, so `jekyll-archives` wrote `/categories/c/index.html` twice, one archive silently overwrote the other, and `/categories/cpp/` returned 404 on the live site. The build reports only a `Conflict` line among the Sass deprecations. `_verify.py` now fails on this as `category-slug-collision`, because catching it before the category ships avoids the URL move that fixing it later requires. Avoid punctuation in category names, since `c++`, `c#` and `.net` all slugify to something shorter and collision-prone.

## Architecture

- **Layouts** (`_layouts/`): Three templates. `default.html` is the base. `post.html` extends default and adds schema.org metadata, MathJax include, and Giscus comments. `page.html` is for static pages.
- **Includes** (`_includes/`): Reusable partials for head, header, footer, MathJax loading, Giscus comments integration, and social icons.
- **Styles** (`_sass/`, `css/main.scss`): Sass-based styling with separate files for base typography, layout, and syntax highlighting.
- **WASM modules** (`assets/wasm/`): Some posts embed interactive WebAssembly calculators. Each module directory contains `.js`, `.wasm`, `.d.ts`, and `package.json` files generated by wasm-bindgen from Rust source.
- **Redirects** (`redirects/`): Static redirect pages that keep a retired URL working. Each file carries an explicit `permalink` pinning it to the OLD address, a canonical link and a meta refresh to the new one, and `sitemap: false` so it stays out of the sitemap. There is no redirect plugin and adding one would change the deploy path, so this is the mechanism. **Add an entry whenever a published post's URL changes**, which in practice means whenever its categories or date change.

## Configuration

`_config.yml` uses Kramdown for Markdown processing and Rouge for syntax highlighting. The `excerpt_separator` is set to empty string as a workaround for a Jekyll tag-closing bug. Changes to `_config.yml` require restarting the Jekyll server.

## Documentation

A knowledge graph is maintained in `_docs/`. Start at [`_docs/README.md`](_docs/README.md) for navigation.

| Section | Path | Description |
|---------|------|-------------|
| Writing | [`_docs/writing/`](_docs/writing/README.md) | Prose style, post structure, and content conventions |
| Architecture | [`_docs/architecture/`](_docs/architecture/README.md) | Jekyll site structure, layouts, and asset integration |
| Process | [`_docs/process/`](_docs/process/README.md) | Content workflow, communication protocol, and task tracking |
| Reference | [`_docs/reference/`](_docs/reference/README.md) | Glossary and supplementary reference material |

## Commit Convention

Use scoped conventional commits: `<scope>: <imperative summary>`. Common scopes: `feat`, `fix`, `docs`, `refactor`, `chore`, `draft`. Include `Co-Authored-By: Claude <noreply@anthropic.com>` when AI-assisted. See [`_docs/process/GIT_STRATEGY.md`](_docs/process/GIT_STRATEGY.md) for full details.

The AI agent commits once after all tasks in a prompt are complete, including the `REVERSE_PROMPT.md` update. `PROMPT.md` is read-only for the AI agent but must be included in the commit if the human pilot has modified it.

## Session Startup Protocol

1. Read [`_docs/process/HANDOFF.md`](_docs/process/HANDOFF.md) and run its validity check, comparing its recorded parent commit to `git rev-parse HEAD~1`. Report it as valid, or as invalid-and-stale on a mismatch, per its Validity section. A stale handoff must not be trusted.
2. Read [`_docs/process/TASKLOG.md`](_docs/process/TASKLOG.md) for current task state.
3. Read [`_docs/process/REVERSE_PROMPT.md`](_docs/process/REVERSE_PROMPT.md) for last AI communication.
4. Wait for human prompt before proceeding.

## Compact Instructions

When compacting this conversation, automatically or via `/compact`, preserve the following so a post-compaction turn resumes without loss. Prefer pointers to the on-disk source of truth over prose, since those files are authoritative and current while the summary is a convenience.

- **The handoff prompt** [`_docs/process/HANDOFF.md`](_docs/process/HANDOFF.md), the self-contained imperative resume prompt. It is overwritten before a planned compaction and stamped with the commit it describes. On resume, validate it by comparing its recorded parent commit to `git rev-parse HEAD~1`, and report it invalid-and-stale on a mismatch rather than trusting it.
- **The resume channels**, plus the instruction to re-read them fresh after compaction: [`_docs/process/REVERSE_PROMPT.md`](_docs/process/REVERSE_PROMPT.md) for the latest AI-to-human report, [`_docs/process/TASKLOG.md`](_docs/process/TASKLOG.md) for current task state and the history table, and [`_drafts/draft_summary.md`](_drafts/draft_summary.md) for per-draft status.
- **The active article and its stage.** Which article number is in progress, which of the four passes it has completed, and its editorial date. Do not re-derive what the process files already record.
- **Git position.** Branch, head commit, whether anything is unpushed, and any uncommitted work with its verification status.
- **In-flight verification.** Any running build, URL sweep, or background job, and what its result gates.
- **The governing rules that are easy to lose**: the `post_url` build-failure interlock and the back-reference-only convention, the two-commit publication pattern, build verification in a Gemfile-free scratch copy before any publishing push, the prose style rules, that density conventions are absolute counts rather than ratios, that an HTTP 200 does not verify a citation, and that irreversible or outward-facing actions need confirmation.

After compaction, before acting, validate `HANDOFF.md` and re-read the resume channels. They and the git state are the true resume anchors.
