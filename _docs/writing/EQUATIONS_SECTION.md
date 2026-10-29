# Equations Section

> **Navigation**: [Writing](./README.md) | [Documentation Root](../README.md)

This document defines the Equations section, a generated index of every display equation in an article. Each
equation is listed under its number and classified as standard or bespoke. The section sits immediately before
`## References`.

**Status.** Adopted 2026-10-28. One article, A384, carries the section. Adoption is per article. `_verify.py`
checks only articles that carry the section or a classification file, so every other article is unaffected.

## What the Section Contains

1. A fixed opening that states how many display equations the article has and how many are standard and
   bespoke. These counts are computed when the section is generated, so they cannot go stale.
2. A caution on units, written for the article.
3. One entry for each display equation, in the order the equations appear. Each entry gives
   - the number the equation carries in the body,
   - a title,
   - a one-sentence gloss,
   - optional citations, and
   - the equation, reproduced character for character from the body.
4. A notation key, `### Notation`, that lists the symbols a reader needs.

## Standard and Bespoke

A **standard** equation is an established result formalised without addition, such as the rocket equation or
the synodic period. It usually carries a citation. Its title is set in bold.

A *bespoke* equation is a construction made for the analysis. Examples include a budget assembled from standard
terms, a model that a stated simplifying assumption defines, and a figure of merit the article introduces. Its
title is set in italics and begins with the word Bespoke.

The classification tells the reader where an error is likely to lie. An error in a standard equation is a
transcription error that a textbook can settle. A bespoke equation can be wrong in its construction, and only the
article's own argument supports it. When an equation applies a standard result under an assumption that the
article chose, and the assumption changes the result, classify it as bespoke and name the assumption in the gloss.

## The Body Governs

The section is generated and is never edited by hand. Its equations are copied out of the body on every
regeneration, so the index cannot show an equation that the body no longer contains. Only the human judgement in
the classification file can go stale. That judgement covers the title, the class and the gloss. Each entry
therefore records a digest of the equation it was written for. The check fails when the body equation no longer
matches that digest. The digest is a truncated SHA-256 hash used only to detect change. It has no security role.

## Data

The classification file is `_sources/equations/<article>.toml`. It is named by the article number in the
post's `<!-- Axxx -->` comment, as `_sources/decisions/` files are.

```toml
caution = "Each equation takes the units of the section in which it appears."

[[equation]]
tag = 12
class = "standard"
title = "Tsiolkovsky Rocket Equation"
gloss = "The ratio of initial to final mass grows exponentially with the delta-v."
cite = ["ref_tsiolkovsky_rocket_equation"]
digest = "d9b49d5a54091191"

[[symbol]]
tex = 'I_{\mathrm{sp}}'
meaning = "the specific impulse of a rocket engine"
```

Glosses and meanings are prose and follow the [Style Guide](./STYLE_GUIDE.md). A citation names an anchor that
the body already cites. Its link text is taken from the first place the body cites it, which keeps the label
consistent and leaves the generated References section unchanged. Write `tex` values as TOML literal strings in
single quotes, so that backslashes stay as written.

## Workflow

```sh
python3 _lib/blog.py equations unfold POST --write  # rewrite single-line $$...$$ as $$ blocks
python3 _lib/blog.py equations tag POST --write   # number the body equations \tag{1} to \tag{N}
python3 _lib/blog.py equations skeleton POST      # print a data file to fill in, with digests
python3 _lib/blog.py equations write POST         # generate or regenerate the section
python3 _lib/blog.py equations check POST         # the drift check that _verify.py runs
python3 _lib/blog.py equations stamp POST         # after reviewing a changed equation's entry
```

When an equation is added or removed, run `tag` again to renumber the body, then edit the data file to match.
Entries must be tagged 1 to N in order. When the check reports that an equation changed, review its title, class
and gloss against the new equation, run `stamp`, and then run `write`.

## What the Check Enforces

- Every body equation carries `\tag{n}`, and the tags run 1 to N in order.
- Every body equation has exactly one entry, and every entry has an equation.
- Every body equation is set off by a blank line above and below. Kramdown reads a block that touches the
  text beside it as part of that paragraph and renders it as inline math, where its `\tag` is a MathJax
  error. A373, A381, A382, A383 and A384 carried six such blocks between them, all already rendered inline
  before they were tagged.
- Every entry's digest matches its equation.
- A bespoke title begins with `Bespoke`, and a standard title does not.
- Every cited anchor is cited in the body.
- Every notation symbol appears in at least one equation. This test matches substrings, so it catches a key
  entry for a symbol the article dropped. It cannot prove that the key is complete, and a single-letter symbol
  matches almost any equation.
- The section on disk equals what `write` produces.

## Rendering

The site configures MathJax without automatic numbering, and an explicit `\tag{n}` still renders under that
configuration. The index repeats each tag. This is harmless because no equation carries a `\label`, so no
cross-reference can become ambiguous. Equations inside code fences are displayed syntax, not equations, and are
ignored.

## Known Limits

- Only the two display forms the corpus uses are recognised. One form is a `$$` line that opens a block and a
  second `$$` line that closes it. The other is a whole line `$$...$$`. Tagging requires the block form, and
  `unfold` converts the single-line form to it without changing the equation's text.
- The section adds the equations a second time to the rendered page, which increases page weight on
  equation-dense articles.
- The classification is a judgement and the check cannot verify it. The check only detects when the equation
  under a judgement has changed.

## Related Sections

- [MathJax Conventions](./MATHJAX_CONVENTIONS.md) for display equation conventions
- [Citation Style](./CITATION_STYLE.md) for the generated References section that follows
- [`_lib/README.md`](../../_lib/README.md) for the library command line
