# Style Guide

> **Navigation**: [Writing](./README.md) | [Documentation Root](../README.md)

Prose style and formatting conventions for blog content.

## Tone

Posts are polite, professional, and academic in register. The writing is technical, aimed at developers, researchers, and practitioners solving a problem or thinking through a design space.

## Prose Rules

These rules are enforced both by the global CLAUDE.md and by the publication review pass.

- **No contractions.** Spell out "do not" rather than "don't." Possessives with apostrophe-s such as "Biosphere 2's first mission" are allowed because they are not contractions.
- **No em-dashes.** No en-dashes either. Replace with commas, separate sentences, or restructuring.
- **No prose colons or semicolons.** YAML front matter, timestamps, and the `console.log` debug tag are the only allowed locations.
- **No prose parentheticals.** Mathematical notation parentheses are allowed inside equations and decibel unit annotations. Standard Wikipedia URL disambiguators such as `(spacecraft)` or `(airship)` are allowed as part of URLs.
- **Broken-phrase line structure.** Each phrase or clause on its own line. This affects diffs and review without changing the rendered output.
- **Spell out acronyms on first use.** See [Acronym Handling](./ACRONYM_HANDLING.md) for the rule and the exemption list.

## Code Conventions

- Use triple-backtick markdown fences with a language specifier for all code blocks.
- Show command-line invocations with a `$` prefix followed by actual output.
- Label full file listings with the filename in backticks before the code block, for example `` `Cargo.toml` full listing ``.
- Partial listings should be labelled accordingly, for example `` `src/lib.rs` partial listing ``.

**Legacy note**: Posts before 2026 used Jekyll Liquid tags `{% highlight sh %}...{% endhighlight %}`. New posts use markdown fences exclusively.

## Link Conventions

- Prefer reference-style links over inline links.
- Use lowercase, underscored reference anchors.
- Define all reference URLs at the bottom of the file.
- Use the Jekyll `{% post_url YYYY-MM-DD-post-slug %}` syntax for links to other posts on the blog.

## Reference Style

References in the `## References` section use a categorized format. Each entry is displayed as `[Category, Title][anchor]` where the anchor follows the pattern `category_abbreviated_title`.

- Categories are short labels that group related references. Examples: AI, Claude Code, GitHub, Protocol, Reference, Related Post, Research.
- The category for other posts on the blog is `Related Post` with the `related_post_` anchor prefix.
- The general category for encyclopedic and Wikipedia sources is `Reference` with the `ref_` anchor prefix.
- The category for peer-reviewed papers and primary documents is `Research` with the `research_` anchor prefix.
- References are sorted alphabetically by category, then by title within each category.
- Anchor names use a lowercase abbreviation of the category as a prefix.
- URL definitions at the bottom of the file are sorted alphabetically by anchor name to match.
- The reference index is a first-class deliverable. Every claim, named concept, and external source should have a corresponding entry. There is no limit on the number of references.

Example:

```markdown
## References

- [AI, Effective Context Engineering][ai_context_engineering]
- [Claude Code, Best Practices][cc_best_practices]
- [Reference, Wikipedia Article on Topic X][ref_topic_x]
- [Related Post, Writing Proofs][related_post_writing_proofs]
- [Research, Author 2024 Paper Title][research_author_2024]

[ai_context_engineering]: https://example.com/context
[cc_best_practices]: https://example.com/best-practices
[ref_topic_x]: https://en.wikipedia.org/wiki/Topic_X
[related_post_writing_proofs]: {% post_url 2026-02-10-writing-proofs %}
[research_author_2024]: https://example.com/paper.pdf
```

## Mathematical Content

See [MathJax Conventions](./MATHJAX_CONVENTIONS.md) for math density targets by genre, variable definition patterns, worked example expectations, and numerical sanity checks.

## Filename Slugs

Slugs are lowercase and underscored. They do not begin with English articles such as "a," "an," or "the," following the convention of dropping leading articles when alphabetising titles. The post title in front matter may still begin with an article.

- `apple_tree.markdown` not `an_apple_tree.markdown`
- `half_life_coin.markdown` not `the_half_life_coin.markdown`

## Related Sections

- [Post Structure](./POST_STRUCTURE.md) for front matter, debug markers, and section templates
- [Article Genres](./ARTICLE_GENRES.md) for the three genre framework
- [Acronym Handling](./ACRONYM_HANDLING.md) for the spell-out rule
- [MathJax Conventions](./MATHJAX_CONVENTIONS.md) for math conventions
- [Publication Review](../process/PUBLICATION_REVIEW.md) for the review pass that verifies these rules
