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

## Mathematical Content

- Set `mathjax: true` in front matter when a post contains mathematical notation.
- Use `$...$` for inline math and `$$...$$` for display math.
- Notation follows standard LaTeX conventions.
