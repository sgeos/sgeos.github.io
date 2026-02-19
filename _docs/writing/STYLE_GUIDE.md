# Style Guide

> **Navigation**: [Writing](./README.md) | [Documentation Root](../README.md)

Prose style and formatting conventions for blog content.

## Tone

Posts are polite, professional, and academic in register. The writing is technical and tutorial-oriented, aimed at developers solving practical problems.

## Prose Rules

- Avoid contractions. Write "do not" instead of "don't."
- Spell out acronyms on first use. Example: "Automated Market Makers (AMMs)."
- Avoid parentheticals, em-dashes, en-dashes, colons, and semicolons in prose where possible.
- Use precise technical terminology. Prefer clarity over brevity.

## Code Conventions

- Use triple-backtick markdown fences with a language specifier for all code blocks.
- Show command-line invocations with a `$` prefix followed by actual output.
- Label full file listings with the filename in backticks before the code block. Example: `` `Cargo.toml` full listing ``.
- Partial listings should be labeled accordingly. Example: `` `src/lib.rs` partial listing ``.

**Legacy note**: Posts before 2026 used Jekyll Liquid tags (`{% highlight sh %}...{% endhighlight %}`). New posts should use markdown fences exclusively.

## Link Conventions

- Prefer reference-style links over inline links.
- Use lowercase, underscored reference anchors.
- Define all reference URLs at the bottom of the file.
- Use Jekyll `{% post_url YYYY-MM-DD-post-slug %}` syntax for links to other posts on the blog.

### Reference Categorization

References in the `## References` section use a categorized format. Each entry is displayed as `[Category, Title][anchor]` where the anchor follows the pattern `category_abbreviated_title`.

- Categories are short labels that group related references. Examples: AI, Claude Code, GitHub, Protocol, Research.
- The category for other posts on the blog is `Related Post`.
- References are sorted alphabetically by category, then by title within each category.
- Anchor names use a lowercase abbreviation of the category as a prefix. Examples: `ai_`, `cc_`, `github_`, `protocol_`, `research_`.
- URL definitions at the bottom of the file are sorted alphabetically by anchor name to match.
- There is no limit on the number of references in an article. The reference index is a first-class deliverable and may be more valuable than the article itself. Every claim, named concept, and external source mentioned in the article should have a corresponding reference entry.

Example:

```markdown
## References

- [AI, Effective Context Engineering][ai_context_engineering]
- [Claude Code, Best Practices][cc_best_practices]
- [GitHub, Reference Implementation][github_blog_repo]
- [Related Post, Writing Proofs][related_post_writing_proofs]

[ai_context_engineering]: https://example.com/context
[cc_best_practices]: https://example.com/best-practices
[github_blog_repo]: https://github.com/user/repo
[related_post_writing_proofs]: {% post_url 2026-02-10-writing-proofs %}
```

## Mathematical Content

- Set `mathjax: true` in front matter when a post contains mathematical notation.
- Use `$...$` for inline math and `$$...$$` for display math.
- Notation follows standard LaTeX conventions.
