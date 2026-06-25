# Post Structure

> **Navigation**: [Writing](./README.md) | [Documentation Root](../README.md)

Structural conventions for blog posts, from front matter through references.

## Front Matter

Every post requires YAML front matter with these fields.

```yaml
---
layout: post
mathjax: false
comments: true
title: "Descriptive Post Title"
date: YYYY-MM-DD HH:MM:SS +0000
categories: category-one category-two
---
```

| Field | Required | Notes |
|-------|----------|-------|
| `layout` | Yes | Always `post` |
| `mathjax` | Yes | Set `true` only when the post contains LaTeX math |
| `comments` | Yes | Set `true` to enable Disqus comments |
| `title` | Yes | Quoted, descriptive title |
| `date` | Yes | UTC timezone (`+0000`) |
| `categories` | Yes | Space-separated, lowercase, hyphenated where needed. Do not use commas. |

**Title reminder**: The draft template title reads "Template, Add Category Before You Forget" as a deliberate prompt to set categories before drafting.

## Article Number and Debug Markers

Every post must include two debug markers immediately after the front matter, before any post content. The article number is a monotonically increasing identifier that ties the post to the Ax-Py-Tz work item coding system documented in [Communication](../process/COMMUNICATION.md).

There must be a blank line between the front matter closing `---` and the markers, and a blank line between the markers and the first line of post content.

```markdown
---
layout: post
mathjax: false
comments: true
title: "Post Title"
date: 2026-02-07 00:00:00 +0000
categories: example
---

<!-- A5 -->
<script>console.log("A5");</script>

Post content begins here.
```

- The HTML comment is invisible in the published HTML and serves as a traceability anchor for associating prompts and tasks with the post they support.
- The `<script>` tag logs the article number to the browser console on page load, providing an easy in-browser confirmation of which article is rendering.

The draft template uses the lowercase placeholder `<!-- Axxx -->` and `console.log("Axxx")`. Replace both placeholders with the assigned article number, for example `A161`, before publication. These two markers are the only place colons or quotes appear that the publication style verifier should ignore.

Historical posts are numbered A1 through A74 in chronological order by publication date. A0 is reserved for non-article work.

## Publication Ordering

Article numbers indicate publication order. An effort should be made to avoid publishing multiple posts on the same date. When multiple drafts are ready on the same day, the preferred approach is as follows.

- One post may be published using the previous day's date if nothing was published on that day.
- One post is published for the current day.
- Remaining posts are held as unpublished drafts for future publication.

If two posts are published on the same date despite these measures, they retain their assigned article numbers. Drafts remain unnumbered until a decision is made to polish and publish them. Unpublished drafts may be published tactically, which can result in slightly out-of-order article numbers relative to publication date. This is acceptable.

## Article Length

There is no limit on article length. An article should be as long as the subject demands.

## Section Structure by Genre

The section structure depends on the article's genre. The blog runs three genres:

- **Tutorial.** Practical how-to posts with a Software Versions section and an Instructions section. The standard sections below are the tutorial template.
- **Subsystem deep-dive.** Equation-dense engineering articles built on the architectural-keystone pattern. See [Subsystem Deep-Dive Structure](./SUBSYSTEM_DEEPDIVE_STRUCTURE.md).
- **Analytical essay or survey.** Cited, reasoned articles that map a design space, a history, or a strategy. See [Analytical Essay Structure](./ANALYTICAL_ESSAY_STRUCTURE.md).

Identify the genre before drafting. See [Article Genres](./ARTICLE_GENRES.md) for the framework.

## Standard Sections for Tutorials

Tutorials follow a consistent section order. Not all sections appear in every tutorial.

1. **Opening prose** (no heading). Introductory paragraph describing the problem or topic.
2. **Interactive elements** (optional). Inline HTML, CSS, and JavaScript for embedded widgets or WebAssembly modules.
3. **`## Software Versions`**. Command output showing the environment. Always includes `date -u`, `uname -vm`, and any relevant tool versions.
4. **`## Instructions`**. Primary content with implementation steps, code blocks, and explanations. May use `###` subheadings for distinct steps.
5. **`## References`**. Bullet list of reference-style links. Appears at the end of every post.

### Optional Sections for Tutorials

- `## Conclusion` for summary and takeaways.
- `## Future Reading` for supplementary resources beyond the references list.
- `## From Math to Code` for posts that transition from theory to implementation.

## Software Versions Format

Use shell comment lines (`#`) to group version commands by category for readability. Standard categories are Date, OS and Version, Hardware Information, Shell and Version, and tool-specific sections.

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-01-31 12:10:25 +0000

# OS and Version
$ uname -vm
Darwin Kernel Version 23.6.0: ...

$ sw_vers
ProductName:		macOS
ProductVersion:		14.6.1
BuildVersion:		23G93

# Hardware Information
$ system_profiler SPHardwareDataType | sed -n '8,10p'
      Chip: Apple M1 Max
      Total Number of Cores: 10 (8 performance and 2 efficiency)
      Memory: 32 GB

# Shell and Version
$ echo "${SHELL}"
/bin/bash

$ "${SHELL}" --version | head -n 1
GNU bash, version 3.2.57(1)-release (arm64-apple-darwin23)
```

Include version output for every language, framework, or tool used in the post. Add a comment header for each tool-specific section.

The date output in the Software Versions section must match the front matter `date:` field. When preparing a post for publication, run the `date -u` command, update the Software Versions output with the result, and set the front matter `date:` to the same timestamp. This ensures the recorded environment timestamp and the publication timestamp are consistent.

## Interactive Elements

Posts that embed interactive content follow this pattern.

1. A `<style>` block with scoped CSS classes for the widget.
2. An HTML `<div>` container with a unique element ID.
3. A `<script type="module">` block that imports and initializes the widget. The script's `id` attribute serves as the anchor element that gets replaced.

WebAssembly assets live in `/assets/wasm/<post_slug>/` and are generated by `wasm-bindgen` from Rust source.

## Categories

Categories are lowercase and hyphenated. Common categories include but are not limited to: `ai`, `ai-tools`, `crypto`, `defi`, `development`, `developer-productivity`, `elixir`, `freebsd`, `gamedev`, `macos`, `mobile`, `philosophy`, `rust`, `tutorial`.

## File Naming

- Drafts: `_drafts/<slug>.markdown`
- Published: `_posts/YYYY-MM-DD-<slug>.markdown`
- Hidden drafts (gitignored): `hidden.<slug>.markdown`

The `_publish.sh` script extracts the date from front matter and prepends it to the filename during publication. On macOS the script fails under BSD sed; use `git mv` directly instead. See [Content Workflow](../process/CONTENT_WORKFLOW.md).

Slugs should not begin with English articles such as "a," "an," or "the." This follows the common practice of dropping leading articles when alphabetising titles. The post title in front matter may still begin with an article.

- `apple_tree.markdown` not `an_apple_tree.markdown`
- `half_life_coin.markdown` not `the_half_life_coin.markdown`

## Related Sections

- [Article Genres](./ARTICLE_GENRES.md) for the three genre framework
- [Style Guide](./STYLE_GUIDE.md) for prose rules
- [Subsystem Deep-Dive Structure](./SUBSYSTEM_DEEPDIVE_STRUCTURE.md) for the engineering-article structure
- [Analytical Essay Structure](./ANALYTICAL_ESSAY_STRUCTURE.md) for the essay structure
- [Content Workflow](../process/CONTENT_WORKFLOW.md) for the draft-to-publish flow
