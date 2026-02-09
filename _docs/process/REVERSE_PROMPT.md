# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-08
**Task**: A82-P1 Draft Introduction to Astronomy

---

## Verification

### Introduction to Astronomy Drafted
**Result**: PASS. `_drafts/introduction-to-astronomy.markdown` rewritten from a 32-line empty stub to a full 925-line article. Assigned A82. 8 references from official sources (NASA, ESA, IAU, OpenStax, Hubble). Research incorporated covering solar system bodies, moon counts, asteroid belt data, and galactic structure.

---

## Implementation Summary

### Files Created/Modified

| File | Changes |
|------|---------|
| `_drafts/introduction-to-astronomy.markdown` | Rewritten from empty stub to full A82 draft. 925 lines. 8 references. Covers solar system from Sun outward, galactic and intergalactic features, qualitative concepts, and 8 mathematical formulas with MathJax. |
| `_drafts/old_drafts.md` | Introduction to Astronomy elevated to release candidate. Removed from Tier 4. Summary updated (4 release candidates). |
| `_docs/process/PROMPT.md` | Human-updated with A82-P1 instructions. Committed as-is. |
| `_docs/process/TASKLOG.md` | A82-P1 task state. |
| `_docs/process/REVERSE_PROMPT.md` | This file. |

### A82 Article Structure

| Section | Content |
|---------|---------|
| Opening | Astronomy as oldest natural science, Sun-outward pedagogical approach, article scope |
| Software Versions | Standard environment block |
| The Sun | Main-sequence G2V star, composition, core temperature, luminosity, solar wind, sunspots and solar cycle |
| Mercury | Smallest planet, extreme temperature range, 3:2 spin-orbit resonance, cratered surface, no moons |
| Venus | Retrograde rotation, runaway greenhouse, atmospheric pressure, sulfuric acid clouds, no moons |
| Earth | Liquid water, magnetosphere, plate tectonics, Moon (formation, tidal locking, recession) |
| Mars | Iron oxide surface, Olympus Mons, Valles Marineris, polar ice caps, Phobos and Deimos |
| Asteroid Belt | 1.1 million+ catalogued, Ceres (dwarf planet), Vesta, Pallas, Hygiea with mass/diameter data |
| Jupiter | Gas giant, Great Red Spot, magnetosphere, 95+ moons, Galilean moons (Io, Europa, Ganymede, Callisto) |
| Saturn | Ring system, lowest density, hexagonal polar vortex, 270+ moons, Titan (atmosphere/methane lakes), Enceladus (subsurface ocean) |
| Uranus | Axial tilt 98 degrees, ice giant, 13 rings, 28 moons, 5 major moons (Miranda, Ariel, Umbriel, Titania, Oberon) |
| Neptune | Strongest winds, Great Dark Spot, 16 moons, Triton (retrograde orbit, nitrogen geysers) |
| Kuiper Belt | 30-50 AU, Pluto and Charon (binary system), Eris, Makemake, Haumea |
| Oort Cloud | 2,000-100,000 AU, hypothesized spherical shell, long-period comets, estimated trillions of objects |
| Galactic Features | Milky Way (barred spiral, 100-400 billion stars), nebulae (4 types), star clusters (open/globular), black holes (stellar/supermassive) |
| Intergalactic Features | Galaxy types (spiral/elliptical/irregular), Local Group (54+ galaxies), clusters, superclusters, observable universe (93 billion light-years, 200 billion+ galaxies) |
| Broad Qualitative Concepts | Electromagnetic spectrum, H-R diagram, stellar evolution (main sequence through remnants), cosmic distance ladder, light as a time machine |
| Mathematical Formulas | Kepler's 3 laws, Newton's gravitation, inverse square law, Stefan-Boltzmann, Wien's displacement, Doppler/redshift, parallax, apparent/absolute magnitude |
| Summary | Recap of scope covered, astronomy as an active and evolving science |
| Future Reading | 5 entries (NASA Solar System, OpenStax Astronomy 2e, ESA Space Science, IAU MPC, Hubble Site) |
| References | 8 entries across 1 category (Reference), all from official sources |

### Scope Relative to Space Studies Draft

The Introduction to Space Studies draft (`introduction-to-space-studies.markdown`) was read for context and kept separate. The astronomy article covers a qualitative survey of celestial bodies and introductory astronomy formulas (Kepler, gravitation, luminosity, redshift, parallax, magnitude). The space studies draft covers orbital parameters and engineering formulas (thrust equation, wavelength-frequency relationship). There is no significant content overlap.

---

## Questions for Human Pilot

**Moon counts.** Planet moon counts are approximate and based on available data. Jupiter has 95+ confirmed moons, Saturn 140+, Uranus 28, and Neptune 16. These numbers change as new moons are discovered. The human pilot should verify these are acceptable approximate values.

**Mathematical formula selection.** The eight formulas selected (Kepler's laws, Newton's gravitation, inverse square law, Stefan-Boltzmann, Wien's law, Doppler/redshift, parallax, magnitude) represent a standard introductory astronomy curriculum. If additional formulas are desired (for example, escape velocity, Roche limit, or Schwarzschild radius), they can be added.

---

## Technical Concerns / Risks

**URL verification.** All 8 reference URLs point to official institutional sources (NASA, ESA, IAU, OpenStax, Hubble). The human pilot should verify all URLs before publication.

**MathJax rendering.** The article uses extensive MathJax for 8 formula sections. Local rendering verification is recommended before publication, particularly for multi-line equations and subscript/superscript nesting.

**Categories.** The article uses categories "space astronomy science". The human pilot should confirm these are acceptable.

---

## Intended Next Step

**Awaiting human direction** on:
- Review of the A82 draft
- Whether additional formulas or topics should be added
- Publication timing for A79, A80, A81, and A82 (all release candidates)
- Any further work

---

## Session Context

If you are a new AI session reading this file:

1. This is a Jekyll blog project at [sgeos.github.io](https://sgeos.github.io).
2. A documentation knowledge graph exists in `_docs/`. Start at `_docs/README.md`.
3. The project uses scoped conventional commits and Ax-Py-Tz work item coding.
4. `PROMPT.md` is read-only for AI agents. Never modify it. Commit it if the human pilot has changed it.
5. A0 is reserved for non-article work. Twenty-four prompts completed (A0-P1 through A0-P7, A75-P1 through A75-P3, A76-P1 through A76-P4, A77-P1 through A77-P3, A78-P1 through A78-P4, A80-P1, A81-P1, A82-P1).
6. All 74 historical posts have article numbers (A1-A74). A75, A76, A77, and A78 are published. A79, A80, A81, and A82 are drafted (release candidates). Next available: A83.
7. Categories are space-separated, not comma-separated.
8. Assets follow `assets/$TYPE/post_$SLUG/$FILENAME` convention.
9. Read `TASKLOG.md` for current task state.
10. Read `CLAUDE.md` at project root for build commands and quick orientation.
11. After publication, include a release announcement draft in REVERSE_PROMPT.md. See `CONTENT_WORKFLOW.md` step 5.
12. Wait for human prompt before proceeding.
