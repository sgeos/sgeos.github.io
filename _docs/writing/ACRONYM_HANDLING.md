# Acronym Handling

> **Navigation**: [Writing](./README.md) | [Documentation Root](../README.md)

Conventions for spelling out and using acronyms in posts.

## The Spell-Out Rule

Spell out every acronym on first use. After first use, subsequent appearances may use the acronym alone.

## Format

Two formats handle most cases.

When the link target is the canonical source for the acronym, embed the spelled-out form in the link text and follow with "or ACRONYM":

```markdown
The [Consultative Committee for Space Data Systems][ref_ccsds]
or CCSDS
publishes...
```

When no link is needed, spell out inline with the same "or ACRONYM" form:

```markdown
The Tracking and Data Relay Satellite System
or TDRSS
provides...
```

Either form establishes the acronym for later use in the article.

## Acronyms That Require Spell-Out

Standards bodies, government agencies, and most program names require spell-out on first use. Representative examples:

- NASA (National Aeronautics and Space Administration)
- ESA (European Space Agency)
- JAXA (Japan Aerospace Exploration Agency)
- IEEE (Institute of Electrical and Electronics Engineers)
- USDA (United States Department of Agriculture)
- FDA (Food and Drug Administration)
- EPA (Environmental Protection Agency)
- WHO (World Health Organization)
- NSF (National Sanitation Foundation, in water and waste contexts)
- ASHRAE (American Society of Heating, Refrigerating, and Air-Conditioning Engineers)
- FCC (Federal Communications Commission)
- ITU (International Telecommunication Union)
- CCSDS (Consultative Committee for Space Data Systems)
- IPC (International Plumbing Code or International Power Cable)
- NEC (National Electrical Code)
- AASHTO (American Association of State Highway and Transportation Officials)
- COSPAR (Committee on Space Research)
- MARPOL (International Convention for the Prevention of Pollution from Ships)
- RCRA (Resource Conservation and Recovery Act)
- CFR (Code of Federal Regulations, typically introduced through the citation it appears in)
- HTV (H-II Transfer Vehicle)

## Acronyms Allowed Without Spell-Out

Model designations and program brand names function as proper nouns and may be used without spell-out. Representative examples from the analog-facilities series:

- BIOS-3
- Biosphere 2
- MELiSSA
- CHAPEA
- HERA
- HI-SEAS
- MDRS, FMARS
- NEEMO
- ICON
- KRUSTY
- DSOC
- MAPLE
- BEAM
- LIFE (Sierra Space LIFE habitat)

These names are widely recognised in the relevant domain. Treat them as proper nouns rather than expanding them inline.

## Acronyms in Math

When an acronym appears as a math symbol, the variable definition prose serves as the spell-out. For example:

```markdown
The photovoltaic conversion efficiency $\eta_{PV}$
follows the panel datasheet.
```

The prose "photovoltaic conversion efficiency" defines PV. Subsequent uses of $\eta_{PV}$ in math do not need additional spell-out.

## Verification

The publication review pass checks acronyms against this rule. See [Publication Review](../process/PUBLICATION_REVIEW.md). A missed spell-out is fixed by expanding the first occurrence, not by inserting an acronym definition list elsewhere.

## Related Sections

- [Style Guide](./STYLE_GUIDE.md) for prose rules
- [Publication Review](../process/PUBLICATION_REVIEW.md) for the verification pass
