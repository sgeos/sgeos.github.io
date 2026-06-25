# Subsystem Deep-Dive Structure

> **Navigation**: [Writing](./README.md) | [Documentation Root](../README.md)

Section structure for the subsystem deep-dive genre. The pattern was established in A153 through A156 and held across A152 through A160. See [Article Genres](./ARTICLE_GENRES.md) for genre identification.

## The Architectural Keystone Framing

Each subsystem deep-dive identifies a single architectural keystone around which every other component is dimensioned. The framing is the article's analytical spine. The "no-X architectures," "terrestrial-only cheats," "space-only options," and "where the framing breaks down" sections each acknowledge limits to the framing without abandoning it.

Examples from the analog-facilities series:

| Article | Subsystem | Keystone |
|---------|-----------|----------|
| A153 | Electricity | battery storage |
| A154 | Water | storage tank with recovery loop |
| A155 | Communications | link budget |
| A156 | Food | caloric yield per square metre per day |
| A157 | Habitat | pressure envelope |
| A158 | Waste | waste mass balance |
| A159 | Transportation | cargo throughput rate |
| A160 | Venus cloudtop | buoyancy condition |

The keystone framing applies cleanly when the subject admits a single dominant constraint. When several constraints compete on equal terms, prefer the analytical essay genre instead.

## Section Order

1. Opening paragraph naming the subsystem and cross-linking the prior articles in the series.
2. Framing paragraph naming the architectural keystone.
3. Generalisation paragraph identifying the non-space use cases the article also serves.
4. Constraint paragraph naming the dominant architecture the article targets.
5. `## The X Keystone` section explaining why the keystone is central.
6. `## Sizing From First Principles` section with the core equations and worked examples.
7. `## Dependent Components in Order of Dependency` section with one subsection per component.
8. `## No-X Architectures` section listing alternatives that bypass the keystone.
9. `## Terrestrial-Only Cheats` section enumerating the ways the analog can cheat.
10. `## Space-Only Options` section listing options the actual mission has that the analog cannot reproduce.
11. `## Where the Keystone Framing Breaks Down` section listing three cases where the framing fails.
12. `## Generalisation Beyond the Space Analog Context` section with five representative terrestrial use cases.
13. `## Out of Scope` section enumerating deferred topics.
14. `## Conclusion` section summarising the architecture and acknowledging dual role.
15. `## References` section with the sorted reference list and link definitions.

## Generalisation Section

The Generalisation section walks five representative non-space use cases. The canonical set from the analog-facilities series is residential cabin or homestead, remote research station, disaster relief installation, maritime vessel, and military forward operating base. Adapt the set to the subject when these do not apply.

## Sizing Section

The Sizing section derives the keystone equation from first principles, defines each symbol in prose immediately before the equation, and presents a worked numerical example with a concrete result. Verify the worked example by independent numerical sanity check before publication. See the Numerical Sanity Checks section of [MathJax Conventions](./MATHJAX_CONVENTIONS.md).

## Length Norm

Subsystem deep-dives in the analog-facilities series have run 1,400 to 2,050 lines. The Dependent Components section is the longest, typically 400 to 600 lines. Each worked example consumes roughly 30 to 50 lines including the equation derivation, the worked numerical example, and the dependent-component implications.

## Related Sections

- [Article Genres](./ARTICLE_GENRES.md) for the genre framework
- [MathJax Conventions](./MATHJAX_CONVENTIONS.md) for math density targets
- [Style Guide](./STYLE_GUIDE.md) for prose rules
- [Publication Review](../process/PUBLICATION_REVIEW.md) for the review pass
