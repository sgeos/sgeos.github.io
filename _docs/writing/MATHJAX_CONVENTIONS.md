# MathJax Conventions

> **Navigation**: [Writing](./README.md) | [Documentation Root](../README.md)

Conventions for mathematical content in posts. MathJax renders LaTeX notation in the browser when `mathjax: true` is set in the front matter.

## Enabling MathJax

Set `mathjax: true` in the front matter whenever any mathematical notation appears in the body. The `post.html` layout reads this flag and conditionally loads MathJax through `_includes/mathjax.html`. Leave the flag `false` when the post carries no math, to avoid the client-side load cost.

## Inline and Display Math

- Inline math uses `$...$` delimiters.
- Display math uses `$$...$$` delimiters, either on a single line or in block form with the delimiters on separate lines.
- Within math expressions, follow standard LaTeX conventions for symbols, subscripts, superscripts, fractions, and Greek letters.

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
