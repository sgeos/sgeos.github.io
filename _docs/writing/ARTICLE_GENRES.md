# Article Genres

> **Navigation**: [Writing](./README.md) | [Documentation Root](../README.md)

The blog runs three article genres. Identify the genre before drafting, because the section structure, the length norm, and the mathematics density differ by genre.

## The Three Genres

### Subsystem Deep-Dive

Equation-dense engineering articles built on the architectural-keystone pattern. The article identifies a single architectural keystone for its subject and dimensions every dependent component against it. The analog-facilities series at A152 through A160 is the canonical example.

Use the [Subsystem Deep-Dive Structure](./SUBSYSTEM_DEEPDIVE_STRUCTURE.md) and the [MathJax Conventions](./MATHJAX_CONVENTIONS.md) density target for this genre.

### Analytical Essay or Survey

Cited, reasoned articles that map a design space, a history, or a strategy. Headings are chosen for the argument rather than from a fixed template. The BTRON article, the fixed-wing unmanned-aerial-vehicle series, and the patents-and-startup series at A161 through A172 are examples.

Use the [Analytical Essay Structure](./ANALYTICAL_ESSAY_STRUCTURE.md) for this genre. Mathematics appears only where a real quantitative relationship exists.

### Tutorial

Practical how-to posts with a Software Versions section and an Instructions section, scaffolded by `_drafts/template.markdown` and described in [Post Structure](./POST_STRUCTURE.md).

## Universal Conventions

Several conventions apply to all genres without exception.

- The [Style Guide](./STYLE_GUIDE.md) prose rules.
- The front matter fields and the debug markers in [Post Structure](./POST_STRUCTURE.md).
- The reference style and the categorized reference list in the [Style Guide](./STYLE_GUIDE.md).
- The [Acronym Handling](./ACRONYM_HANDLING.md) format.
- The publication review pass in [Publication Review](../process/PUBLICATION_REVIEW.md).

Genre-specific conventions are noted explicitly in their respective documents.

## Length

There is no global length target. An article should be as long as the subject demands.

- Tutorials are typically a few hundred lines plus their code.
- Subsystem deep-dives have run 1,400 to 2,050 lines.
- Analytical essays range from focused four-hundred-line pieces to multi-thousand-line surveys such as BTRON.

Do not pad an essay to deep-dive length or trim a deep-dive to essay length. Match the form to the subject.

## Related Sections

- [Subsystem Deep-Dive Structure](./SUBSYSTEM_DEEPDIVE_STRUCTURE.md)
- [Analytical Essay Structure](./ANALYTICAL_ESSAY_STRUCTURE.md)
- [Post Structure](./POST_STRUCTURE.md) for the tutorial template and universal front matter
- [MathJax Conventions](./MATHJAX_CONVENTIONS.md) for mathematics density by genre
