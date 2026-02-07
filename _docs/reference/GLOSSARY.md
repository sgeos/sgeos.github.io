# Glossary

> **Navigation**: [Reference](./README.md) | [Documentation Root](../README.md)

Key terms used in the documentation and blog infrastructure.

| Term | Definition |
|------|------------|
| Draft | A work-in-progress post in `_drafts/`. Not published until moved to `_posts/`. |
| Front matter | YAML metadata block at the top of every post, delimited by `---`. |
| Hidden draft | A draft file prefixed with `hidden.` that is excluded from version control by `.gitignore`. |
| Jekyll | The static site generator used to build the blog from Markdown and Liquid templates. |
| Kramdown | The Markdown parser used by Jekyll. Supports fenced code blocks, tables, and other extensions. |
| Liquid | The template language used by Jekyll for layouts and includes. |
| MathJax | JavaScript library for rendering LaTeX mathematical notation in the browser. |
| Rouge | The syntax highlighting engine used by Jekyll for code blocks. |
| Slug | The URL-friendly, hyphenated identifier portion of a post filename (e.g., `getting-started-with-claude-code`). |
| WASM | WebAssembly. Binary instruction format used for interactive post content compiled from Rust via `wasm-bindgen`. |
| Forward prompt | A human-to-AI instruction staged in `PROMPT.md`. |
| Reverse prompt | An AI-to-human status report written to `REVERSE_PROMPT.md`. |
| Task log | The shared source of truth for current work state, maintained in `TASKLOG.md`. |
