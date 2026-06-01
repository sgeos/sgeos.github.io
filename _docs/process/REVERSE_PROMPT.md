# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-05-31
**Task**: A129-P3 Publish "An Aerobatic Maneuver Reference Catalog for Fixed-Wing UAVs" (fourth extension, reference companion to A128)

---

## Verification

### A129 Published

A129 "An Aerobatic Maneuver Reference Catalog for Fixed-Wing UAVs" published at `_posts/2026-06-12-aerobatic_maneuver_reference_catalog_for_fixed_wing_uavs.markdown` with front-matter date `2026-06-12 09:00:00 +0000`. 32 references across Book (1), Reference (26), and Related Post (5) categories, and a 79-row catalog. Standalone aerospace reference article and the fourth extension beyond the core fixed-wing-UAV arc, the reference companion to the A128 model. References A120, A123, A125, A127, and A128 via `post_url`.

### Framing

The article turns the costed-trajectory model of A128 into a reference, a catalog of the named and recognized maneuvers each classified by what it does to the energy state, the load it demands, and how high in the speed range it survives. It is written for the unmanned case, so a maneuver is a selectable object with a known cost and footprint rather than a learned skill, and the honesty of the catalog rests on a clear division between the sourced definitions and the original classification.

### Scope Covered

A 79-row alphabetical catalog with a stable family-prefixed identifier per maneuver across twelve families, the lines, turns, rolls, loops and eights, partial loops and combinations, stall turns, tailslides, spins, post-stall and supermaneuvers, three-dimensional and prop-hang figures, basic fighter maneuvers, and composite or display figures. The columns are the identifier, the maneuver, the family, the spatiotemporal path, the energy-height behavior, the peak load class, and the regime ceiling with flags. The prose covers how to read the table, why the thermal cost is folded into the regime column, provenance and limitations, the maneuvers without a closed form, the parametric families, the alternate names, using the catalog, and a worked reading of one row into numbers.

### The Honesty Division

The existence and definition of each maneuver are sourced to the established catalogs, the Aresti system, the world air sports federation, the International Aerobatic Club, and the basic-fighter-maneuver repertoire, linked to their own descriptions where one exists. The classification of each maneuver in the cost model, the energy-height behavior, the peak load class, and the regime ceiling, is forward-declared as an original and qualitative synthesis to be checked rather than as measured data, with three stated limitations, that the values are classes and not certified numbers, that the catalog lists named base figures and notes the parametric families rather than enumerating the combinatorial Aresti space, and that the post-stall figures carry a no-closed-form flag rather than a fabricated load.

### Reference and Style Verification

Reference integrity confirmed at 32 of 32 anchors defined and used, zero missing and zero unused, alphabetized within each category. The catalog has 79 data rows with all family-prefixed identifiers unique. The completeness pass added three Reference anchors (Aerobatics, Spiral Dive, and Three-Dimensional Flying), all verified HTTP 200 on 2026-05-31. The Book source (Vinh, on Google Books) was verified accessible. Lazy eight, knife-edge flight, and the yo-yo maneuvers have no standalone article and are cited to the catalog standards rather than linked. Prose style confirmed: no contractions, no em-dashes or en-dashes in the body, and no prose colons or semicolons, the only semicolon being the console.log debug tag.

### Build Verification

Verified with system Jekyll: the post renders at /aerospace/engineering/uav/2026/06/12/, the catalog table renders with 80 rows including the header, the A120 and A123 and A125 and A127 and A128 `post_url` links resolve, all three new reference links resolve to real hrefs, no unresolved link markup remains, and the post appears on the index. The full local bundle build remains broken in this environment; the deploy build runs via the GitHub Actions pipeline after the push.

---

## Release Announcement

New Blog Post: An Aerobatic Maneuver Reference Catalog for Fixed-Wing UAVs

The previous article built a model that prices an aerobatic maneuver as a costed trajectory. This one is the reference companion, a catalog of seventy-nine named and recognized maneuvers, each classified by what it does to the energy state, the load it demands, and how high in the speed range it survives, written for the people who command unmanned aircraft rather than for the human pilot.

Key takeaways:
- Each row is one maneuver with a stable identifier, sorted alphabetically, classified by its spatiotemporal path, its energy-height behavior, its peak load, and its regime ceiling.
- The maneuver definitions are borrowed from the established catalogs while the classification in the cost model is an original synthesis offered to be checked rather than trusted, and the thermal cost is folded into the regime ceiling because the sport repertoire is uniformly subsonic.
- The post-stall figures, the spins and snaps and the cobra and the three-dimensional prop-hang set, carry a no-closed-form flag and a section on what can still be said about them, an honesty the model demanded.
- The purpose is the one that runs through the whole extension set, to let an unmanned aircraft treat a maneuver as a selectable object with a known cost and footprint, chosen against a budget rather than against the limits of a person who is no longer aboard.

You can read the full article here:
https://sgeos.github.io/aerospace/engineering/uav/2026/06/12/aerobatic_maneuver_reference_catalog_for_fixed_wing_uavs.html

#UAV #FixedWing #Aerospace #Aerobatics #Aresti #ReferenceCatalog #EnergyManeuverability

---

## Action Items for the Human Pilot

- Confirm the 2026-06-12 publication date is as intended. A129 is the fourth extension beyond the core arc and the reference companion to A128, one day after it.
- The catalog lists 79 named and recognized base figures rather than the combinatorial Aresti space. If a larger table is wanted, it can be widened by enumerating parametric rows explicitly, the point rolls by count, the multi-turn spins, and the rolls on lines by count, which the "Parametric Families" section currently describes rather than enumerates.
- Optionally request the Aresti figure symbols and a per-family iconography, which are the one improvement that cannot be added in text and would require image assets.
- Possible further unflagged extensions, if desired later, are payload and mission systems, and the regulatory and operations layer.

---

## Notes

- Next available article number: A130.
- 0 release candidates.
- 0 new drafts. A108 through A129 published.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification.
- Published: A79 through A129.
- The core fixed-wing-UAV arc is complete (A112, A114, A116, A118, A120, A121, A122, A123, A124, A125); A126 (communications), A127 (structures and the flight envelope), A128 (aerobatics as costed trajectories, the synthesis capstone), and A129 (an aerobatic maneuver reference catalog, the reference companion to A128) are the first four extensions beyond it. No internal research cited; public encyclopedic and authoritative sources only.
- All scratch is confined to project-local `tmp/` per recorded preference. A129 process-file deltas were staged in `tmp/a129/` while drafting and have now been applied directly, so those notes are superseded.
- Blog deploys through GitHub Actions with a lean Jekyll stack; 0 open Dependabot alerts; Keleusma highlighting is live.
