# MathJax Conventions

> **Navigation**: [Writing](./README.md) | [Documentation Root](../README.md)

Conventions for mathematical content in posts. MathJax renders LaTeX notation in the browser when `mathjax: true` is set in the front matter.

## Enabling MathJax

Set `mathjax: true` in the front matter whenever any mathematical notation appears in the body. The `post.html` layout reads this flag and conditionally loads MathJax through `_includes/mathjax.html`. Leave the flag `false` when the post carries no math, to avoid the client-side load cost.

## Inline and Display Math

- Inline math uses `$...$` delimiters.
- Display math uses `$$...$$` delimiters, either on a single line or in block form with the delimiters on separate lines.
- Within math expressions, follow standard LaTeX conventions for symbols, subscripts, superscripts, fractions, and Greek letters.

## Underscores and Asterisks in Inline Math

**Kramdown does not recognise single-dollar math.** It passes `$...$` through to the page for MathJax to typeset in the browser, and before that it reads the underscores and asterisks inside the span as Markdown emphasis. Two spans in one paragraph or list item can therefore be joined by an `<em>` tag that opens in the first and closes in the second. MathJax matches delimiters within a single run of text and the tag breaks the run, so the reader sees raw LaTeX followed by stray italics.

The rule was measured by probing kramdown directly during A362 for the underscore and A363 for the asterisk.

- An underscore opens emphasis unless the character before it is a letter, so it opens after a digit or a brace, as in `x^2_i` or `\dot{m}_{0}`. It closes when the character after it is not a letter or digit, as in `_{` or `_\`.
- An underscore between two letters, as in `V_j` or `u_e`, neither opens nor closes. A digit before the underscore does not protect it.
- Bare asterisks inside inline math pair by count within the paragraph, so `$I^{*}$` and `$S^{*}$` in one sentence render as `$I^{<em>}$ ... $S^{</em>}$`.
- Bracing a subscript does not help, because `}_` is an opening position and `_{` a closing one.
- An escaped `\_` or `\*` is inert. Kramdown consumes the backslash and MathJax receives the plain character, so escaping costs nothing in the rendered math.
- Display math in `$$` blocks is converted by kramdown itself and is not affected.

**Escape the underscore or asterisk** whenever a paragraph or list item carries more than one of them inside inline math, whether in one span or in several. A single span can break on its own, since `$\dot{m}_{a} + \dot{m}_{b}$` renders as `$\dot{m}<em>{a} + \dot{m}</em>{b}$`. A lone subscript is safe until a second one is added nearby, which is how most occurrences arose. The defect is easy to write in a sentence of the form "$X_{a}$, the first quantity, with $X_{b}$ the second", which is also the shape of a generated Notation entry.

**A repair that edits inline math must respect two boundaries.** It must skip posts that do not set `mathjax: true`, because MathJax never loads there and the character has no mathematical meaning, and it must mask fenced and inline code, because a shell command such as `GRANT ALL PRIVILEGES ON ${DB_NAME}.*` reads as an inline span to a naive dollar pattern. An early automatic repair escaped the asterisk in exactly that command in a 2016 post, and a comparison of builds before and after caught it.

`_lib/render.py` reports this defect as `math-emphasis` on the built site, which is the only place it can be seen reliably. A source predictor using the rule above flagged 104 pairs where the rendered pages carried 18, so the rendered check is authoritative. It skips a block holding an odd number of dollar signs, because a literal dollar in a reference title such as `$18.5 Bn` followed by an italic journal name is correct text.

## Variable Definitions

Define each symbol in prose immediately before its first display equation. State the variable name, its meaning, and its units. Then state the equation. Then explain the result.

This pattern lets the reader read the prose linearly without needing to look up symbols from a separate definition list.

## Worked Examples

Each major derived equation should be followed by a worked numerical example with concrete inputs and a stated result. The worked example anchors the abstract equation to a concrete magnitude the reader can reason about. Use realistic values from the article's context rather than artificial round numbers.

## Density Targets by Genre

| Genre | Display equations | Inline expressions |
|-------|---------|----------------|
| Subsystem deep-dive | approximately 10 to 16 | approximately 19 to 36 |
| Analytical essay | as the argument requires, often zero | sparse |
| Tutorial | as the topic requires | sparse |

The subsystem deep-dive targets are descriptive, not prescriptive. They reflect the actual density of A152 through A160. An article that genuinely needs more math should carry more. Do not pad math to hit a target. Do not strip math to stay under a target.

For genres that carry no math, the correct response to the human pilot's recurring "Does the article include MathJax?" prompt is to confirm briefly and explain why, rather than to manufacture equations. See [Publication Review](../process/PUBLICATION_REVIEW.md).

## Numerical Sanity Checks

Before publishing any article with math:

- Re-derive each worked example independently from the stated input values.
- Verify unit consistency throughout each derivation, for example μmol versus mol or dBm versus dBW.
- Cross-check ratios and stoichiometry against the molecular masses.
- Check that decibel conversions assume the right reference power.
- Verify constant values against the SI definition, for example the Boltzmann constant at 1.380649e-23 J/K.
- Round consistently. Match the precision of the input values rather than the precision of the calculator output.

A failed sanity check is fixed by correcting the article, not by leaving the published number incorrect. The worked example is part of the article's argument.

## Common Numerical Errors

See [Common Errors](../reference/COMMON_ERRORS.md) for a catalogue of recurring numerical errors observed during the analog-facilities series, including unit confusion, missing factors of two, and order-of-magnitude transcription errors.

## Related Sections

- [Style Guide](./STYLE_GUIDE.md) for prose rules
- [Subsystem Deep-Dive Structure](./SUBSYSTEM_DEEPDIVE_STRUCTURE.md) for the equation-bearing sizing section
- [Publication Review](../process/PUBLICATION_REVIEW.md) for the verification pass
- [Common Errors](../reference/COMMON_ERRORS.md) for fact and unit traps
