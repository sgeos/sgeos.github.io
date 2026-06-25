# Glossary

> **Navigation**: [Reference](./README.md) | [Documentation Root](../README.md)

Key terms used in the documentation and blog infrastructure.

| Term | Definition |
|------|------------|
| Architectural keystone | The single dominant constraint around which a subsystem deep-dive is structured. Each dependent component is dimensioned against the keystone. Examples include battery storage for an electrical subsystem and the link budget for a communications subsystem. |
| Article genre | One of three article types on the blog: tutorial, subsystem deep-dive, or analytical essay. Each genre has its own section structure and length norm. See [Article Genres](../writing/ARTICLE_GENRES.md). |
| Article number | A monotonically increasing identifier, recorded in an HTML comment and `console.log` debug tag at the top of each post. Forms the basis of the Ax-Py-Tz work item coding system. |
| Back-dated post | A post with a `date:` earlier than the current build time. Renders at deploy time and appears at its past position in chronological listings. Does not depend on `future: true`. |
| Batch publication | The publication pattern where every article of a cross-linked series is moved into `_posts/` together so internal `{% post_url %}` tags resolve at once. Contrasts with incremental publication. |
| Debug markers | The `<!-- AXXX -->` HTML comment and the `<script>console.log("AXXX");</script>` tag immediately after the front matter. They record the article number and provide an in-browser confirmation of which article is rendering. |
| Draft | A work-in-progress post in `_drafts/`. Not published until moved to `_posts/`. |
| Epistemic State | A section in an analytical essay that sorts the article's claims into classes, typically historical fact, structural analysis, and inference, so the reader can evaluate each on appropriate grounds. |
| Forward-dated post | A post with a `date:` later than the current build time. Renders at deploy time under `future: true` and appears at its future date position in chronological listings until the date arrives. |
| Front matter | YAML metadata block at the top of every post, delimited by `---`. |
| Forward prompt | A human-to-AI instruction staged in `PROMPT.md`. |
| Hidden draft | A draft file prefixed with `hidden.` that is excluded from version control by `.gitignore`. |
| Incremental publication | The publication pattern where each article in a series is moved into `_posts/` separately, in cadence. Forward references to later, unpublished articles must be prose only. Contrasts with batch publication. |
| Jekyll | The static site generator used to build the blog from Markdown and Liquid templates. |
| Keystone framing | The structural device used by subsystem deep-dives: identify the architectural keystone, then dimension every dependent component against it. |
| Kramdown | The Markdown parser used by Jekyll. Supports fenced code blocks, tables, and other extensions. |
| Liquid | The template language used by Jekyll for layouts and includes. |
| Master session | The AI session operating in the blog repository that executes git operations, runs the build, and triggers deploys. Contrasts with the sister session. |
| MathJax | JavaScript library for rendering LaTeX mathematical notation in the browser. |
| Publication review | The systematic review pass before publication, triggered by the human pilot's "Please review for publication" prompt. Covers prose style, references, URLs, math, acronyms, and structure. |
| Research agent | A background AI agent launched to verify factual claims, dates, numbers, and URLs in an article before publication. |
| Reverse prompt | An AI-to-human status report written to `REVERSE_PROMPT.md`. |
| Rouge | The syntax highlighting engine used by Jekyll for code blocks. |
| Sister session | A second AI session that drafts content in parallel into the same blog repository, typically in a separate working directory. Does not commit or push directly. The master session handles publication. |
| Slug | The URL-friendly, underscored identifier portion of a post filename. Slugs do not begin with English articles such as "a," "an," or "the." |
| Task log | The shared source of truth for current work state, maintained in `TASKLOG.md`. |
| Two-commit publication | The standard publication pattern: a draft commit that stages the file in `_drafts/`, followed by a publish commit that moves it to `_posts/` and updates process files. |
| WASM | WebAssembly. Binary instruction format used for interactive post content compiled from Rust via `wasm-bindgen`. |
