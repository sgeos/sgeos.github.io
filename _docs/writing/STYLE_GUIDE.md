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

## Diction and Repetition

The rules above constrain punctuation. These constrain word choice, which is where the
corpus has actually gone wrong.

- **Do not calibrate density against recent siblings.** When drafting article N of a series, the
  preceding articles are context for continuity of argument, cross-reference, and terminology.
  They are not a target to match for prose texture. Write each article at ordinary density.
- **Delete the empty intensifier.** If removing an adjective does not change the claim, it was
  not doing work. `the specific mechanism` almost always means `the mechanism`. The same applies
  to `substantial`, `significant`, and `comprehensive` used as generic emphasis rather than as a
  measured quantity.
- **Vary formulaic phrasing.** A sentence pattern that introduces equations, closes citations, or
  opens paragraphs should not repeat verbatim across an article. Where a phrase is genuinely
  needed many times, rotate among several forms rather than substituting one fixed formula for
  another, which only moves the problem.
- **Preserve the word when it carries meaning.** `specific impulse` is a technical term.
  `any specific case` is a real quantifier claim, weaker than `any case`. `X rather than the
  general Y` is a real contrast. Never strip a word from an article whose subject is that word,
  such as `context` in an article about context windows.

### Why this section exists

Between 2026-01 and 2026-07 the word `specific` escalated to 46.2 uses per thousand words in the
worst article, against a natural corpus rate near 1.7, and one series used `specifically` as an
adjective, producing ungrammatical prose such as "the specifically Gulf oil states". None of it
was caused by an instruction. It was self-imitation drift, an agent calibrating to its own prior
output, and it survived every context reset because nothing in the review pass could see it. The
publication review verified punctuation and reported prose style clean on the worst offenders.

The measurement method and the remediation history are in the 2026-08-05 entry of
[TASKLOG](../process/TASKLOG.md).

### How to measure it

`_verify.py` flags any watched word above 5.0 uses per thousand author prose words. **A rate alone
cannot tell a term of art from a tic**, and acting on the rate alone would delete `specific impulse`
from five rocketry articles. The discriminator is the neighbouring words.

```sh
python3 _lib/diction.py collocate specific _posts/<file>.markdown   # evidence for one word
python3 _lib/diction.py outliers  _drafts/<file>.markdown           # words above the peer maximum
python3 _lib/diction.py tics      _drafts/<file>.markdown           # the enumerated tic class
python3 _lib/diction.py report    _drafts/<file>.markdown           # multi-word constructions
```

**Direction depends on part of speech and getting it backwards inverts the answer.** A noun forms its
compound with the word BEFORE it, so `configuration` is judged by `capability configuration`. An
adjective forms it with the word AFTER, so `specific` is judged by `specific impulse`. `collocate`
prints both directions for this reason. Reading only one direction once produced a recommendation to
rewrite four published articles that did not need it.

**A word above the peer maximum is usually the subject rather than a tic.** No peer article wrote
about coroutines, so `suspension` exceeds every peer and means nothing. The `tics` mode exists because
the tic class has to be enumerated in advance. A relative check discovers subjects, not tics.

**Signatures worth knowing.**

| Observation | Reading |
|---|---|
| One collocate accounts for most uses, as `specific impulse` at 86 percent | Term of art. Exempt it |
| Many different content-word modifiers, as `capability configuration` and `vehicle configuration` | Term of art used across distinct referents. Exempt it |
| Neighbours are determiners and verbs, as `a substantial` and `achieved substantial` | Vague quantifier. Fix it |
| The word is the article's own subject and the bare uses have a named antecedent | Ordinary anaphora. Exempt it |

**A warning is not a verdict and must be resolved either way.** `_verify_exemptions.yml` records every
false positive with a measured reason, because an unactioned warning becomes noise and noise is how
the original `specific` problem stayed invisible for months. Warnings carry their top collocate inline
so they can be triaged without rerunning anything.


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
- [Article Genres](./ARTICLE_GENRES.md) for the genre framework
- [Acronym Handling](./ACRONYM_HANDLING.md) for the spell-out rule
- [MathJax Conventions](./MATHJAX_CONVENTIONS.md) for math conventions
- [Publication Review](../process/PUBLICATION_REVIEW.md) for the review pass that verifies these rules
