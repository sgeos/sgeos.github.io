# Publication Review

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

The systematic review pass that any article undergoes before publication. The human pilot triggers it with the prompt "Please review for publication, and make suitable changes." The cue requests both the review and the fixes in the same response.

## Scope

The review covers prose style, reference integrity, URL response, mathematical content, acronym handling, and structural conformance to the article's genre. Apply fixes immediately. Report all changes made.

## Checks

### Prose Style

Verify against the [Style Guide](../writing/STYLE_GUIDE.md):

- No contractions.
- No em-dashes, no en-dashes.
- No prose colons or semicolons. The YAML front matter, timestamps, and the `console.log` debug tag are the only allowed locations.
- No prose parentheticals. Math notation parentheses are allowed in equations and decibel unit annotations.
- Broken-phrase line structure preserved.

Run the style verification script from [Style Verification](./STYLE_VERIFICATION.md) to confirm zero counts for em-dashes, en-dashes, and contractions.

### Diction and Repetition

The checks above are punctuation checks. They do not detect an overused word, and for a long time
nothing else did either, which is how one article reached 46.2 uses of `specific` per thousand
words while passing this review with prose style reported clean.

Run the word-frequency section of the verification script. Investigate any content-independent
word above roughly 5 uses per thousand, and any formulaic phrase repeating more than a handful of
times. Then apply judgment, because the count alone does not decide:

- **Legitimate.** The word is the article's subject or a technical term. `specific impulse` in a
  propellant article, `context` in an article about context windows, `sort key` in an article
  about draw order. Leave these alone and say why in the review report.
- **Filler.** Removing the word does not change the claim. Delete it.
- **Formulaic.** The word carries meaning but one phrasing repeats. Vary across a rotation rather
  than substituting a single replacement formula.

See the Diction and Repetition section of the [Style Guide](../writing/STYLE_GUIDE.md) for the
rules and for why this check exists.

### Acronym Spell-Out on First Use

Verify against [Acronym Handling](../writing/ACRONYM_HANDLING.md). Trace every multi-letter acronym to its first body occurrence and confirm the spell-out is present. Model designations and program brand names are exempt.

### Reference Integrity

- Every `[Category, Title][anchor]` link in the references list has a corresponding `[anchor]: URL` definition.
- The references list is sorted alphabetically by category, then by title within each category.
- The link definitions at the bottom of the file are sorted alphabetically by anchor name.
- No `[anchor]` is used in the body without a definition.
- No definition is unused.

The script in [Style Verification](./STYLE_VERIFICATION.md) reports missing and unused anchors and confirms the definitions are sorted.

### URL Response

Spot-check every URL with curl. See [URL Verification](./URL_VERIFICATION.md) for the procedure and the catalogue of known 403 responses on canonical sites. 404 responses require URL replacement before publication. 403 responses are acceptable only on documented bot-detected canonical sources.

### Numerical Sanity

For articles with mathematics, re-derive each worked example independently from the stated input values. See the Numerical Sanity Checks section of [MathJax Conventions](../writing/MATHJAX_CONVENTIONS.md).

### Structural Conformance

Confirm the article follows the section order for its genre:

- [Subsystem Deep-Dive Structure](../writing/SUBSYSTEM_DEEPDIVE_STRUCTURE.md) for that genre.
- [Analytical Essay Structure](../writing/ANALYTICAL_ESSAY_STRUCTURE.md) for that genre.
- [Post Structure](../writing/POST_STRUCTURE.md) for tutorials.

## The "Does the Article Include MathJax?" Prompt

The human pilot uses the recurring prompt "Does the article include MathJax? It seems like it could and probably should."

For a math-bearing article, this is the cue to add more equations even when MathJax is already enabled. Preempt by including ample math from the start.

For an article whose genre genuinely carries no math, the correct response is to confirm that and explain why, rather than to manufacture equations. See [MathJax Conventions](../writing/MATHJAX_CONVENTIONS.md) for density guidance by genre.

## Reporting

After the review, list each issue found and each fix applied. Do not leave the human pilot to discover unstated changes by diffing.

## Related Sections

- [Style Verification](./STYLE_VERIFICATION.md) for the verification scripts
- [URL Verification](./URL_VERIFICATION.md) for the URL-check procedure
- [Style Guide](../writing/STYLE_GUIDE.md) for the prose rules
- [MathJax Conventions](../writing/MATHJAX_CONVENTIONS.md) for math review
- [Acronym Handling](../writing/ACRONYM_HANDLING.md) for the spell-out rule
