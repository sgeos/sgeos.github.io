# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-06-26
**Task**: Draft, finalise, and batch-publish the fifteen-article two-dimensional projection in games series (A173 through A187) across back-dated 2026-04-18 through 2026-05-02

---

## Verification

### Series Body Complete

Fifteen articles drafted, reviewed, and published. The series treats two-dimensional projection in games organised into six clusters that walk from the simplest top-down view through the projective synthesis closer.

- A173 opener (2026-04-18): Two-Dimensional Projection as a Coordinate Mapping Problem.
- A174 through A178 Cartesian cluster (2026-04-19 through 2026-04-23): top-down without height, decoupled vertical axis with shadow drop, side-scrolling without depth, side-scrolling with parallax layers, belt-scroll with explicit depth and the Y-sort intro.
- A179 and A180 oblique-and-axonometric cluster (2026-04-24 and 2026-04-25): oblique projection with cabinet and cavalier variants, axonometric with isometric/dimetric/trimetric variants.
- A181 through A184 affine-and-projective cluster (2026-04-26 through 2026-04-29): Mode 7 affine ground plane, sprite scaling pseudo-three-dimensional, raycasting with fisheye correction, stylised hybrid projections.
- A185 and A186 cross-cutters (2026-04-30 and 2026-05-01): draw order with Y-sort/Z-sort/painter's algorithm, picking and hit testing with the Battle Clash and Metal Combat sprite-scale-and-rotate canonical case.
- A187 synthesis closer (2026-05-02): the camera as linear operator, with each previous mode recovered as a restricted case of the PVM pipeline.

### Two-Commit Publication Pattern

The publication follows the established two-commit pattern. The draft commit captures all fifteen drafts in `_drafts/` to record the draft state in git history. The publication commit moves all fifteen from `_drafts/` to `_posts/` with the appropriate date prefix and updates the process files. Git rename detection preserves the file history across the moves.

### Build Verification

The local bundle build remains broken in this environment; the deploy build runs via the GitHub Actions pipeline after the push. Because the dates 2026-04-18 through 2026-05-02 are back-dated relative to today (2026-06-26), the posts appear at their April-May positions immediately upon deploy and do not depend on the `future: true` setting that the forward-dated work relies on.

### Style and Cohesiveness Verification

All fifteen articles pass the style consistency checks: zero em-dashes, zero en-dashes, zero contractions, zero prose colons, zero prose parentheticals (besides the debug script tag).

Frontmatter is uniform across the series: `layout: post`, `mathjax: true`, `comments: true`, `categories: games graphics projection`.

Section structures follow the established projection-mode template (Brief History, Forward Map, Inverse Map, Worked Example, Variations Within the Mode, Delivery Mechanisms, Where the Framing Breaks Down, Canon, Out of Scope, Conclusion, References) for the projection-mode articles, with appropriate variations for the opener (A173), the cross-cutters (A185, A186), and the synthesis closer (A187). A178 includes additional Y-Sort Criterion and Pick Disambiguation sections as previews of the cross-cutters. A183 includes a dedicated Fisheye Correction section.

Forward-reference accuracy was verified across the series. Every "next article in the cluster/series" claim in conclusions correctly identifies the subsequent article by content. Cluster references in A187's synthesis closer match the article's actual subject matter.

Shared canonical game attribution was verified consistent across the series. Battle Clash (A173, A182, A186), Mother / EarthBound Beginnings (A173, A174, A184), Adventure (A173, A174), Pac-Man (A173, A174), and others all use consistent dates and credits.

The y-down depth-into-screen convention is established in A174 and referenced consistently in subsequent articles (A176 through A187 all reference back to the convention).

Two URL inconsistencies were found during the cohesiveness pass and resolved: `ref_donkey_kong` normalised to `Donkey_Kong_(arcade_game)` across A173 and A176; `ref_streets_of_rage` normalised to `Streets_of_Rage_(video_game)` across A173 and A178.

### Series Numerical Totals

- Total lines: ~14,640 across the fifteen articles.
- Total display equations: ~343.
- Total inline expressions: ~1,144.
- Total references: ~106 unique across the series. Twenty-two references appear in multiple articles with consistent URLs.

### Status of Process Files

`_docs/process/TASKLOG.md` updated with publication entries for A173 through A187 and the next-available-article-number entry corrected from the stale A145 claim to A188. `_drafts/draft_summary.md` extended with a series entry covering all fifteen articles. `_docs/process/REVERSE_PROMPT.md` overwritten with this completion report. The stale A145 claim in the previous TASKLOG predated the projection series, the analog-facilities series (A152-A160), and the patent and startup strategy series (A161-A172); the corrected A188 reflects the next available number across all three published series.

### Git Status

`git status` confirms fifteen renames from `_drafts/` to `_posts/` in the publication commit, plus the three process-file updates (TASKLOG.md, draft_summary.md, REVERSE_PROMPT.md). No other content touched.

---

## Article Number State

The article number space across the blog now reads as follows.

- A1 through A74: legacy published posts predating the modern numbered tracking.
- A75 through A151: published series across 2026-02-06 through 2026-03-14 (the BTRON/Keleusma series, the fixed-wing UAV series, the SAR drone series, and standalone articles).
- A152 through A160: analog-facilities series, published 2026-06-28 through 2026-07-06.
- A161 through A172: patent and startup strategy series, published 2026-05-03 through 2026-05-14.
- A173 through A187: two-dimensional projection in games series, published 2026-04-18 through 2026-05-02 (this batch).
- Next available article number: A188.

The two-dimensional projection in games series back-dated dates fall before the patent series start at 2026-05-03 and well before the analog-facilities series forward-dated dates, so the three series do not collide on date or article number.

---

## Action Items for the Human Pilot

- Verify the GitHub Actions deploy completes without `post_url` resolution errors after the push. The series articles use prose forward references rather than `{% post_url %}` Liquid tags; a follow-up pass to convert the prose references to Liquid tags would tighten the cross-linking but is not required for build success.
- Review the fifteen published articles at their permalinks once the deploy completes:
  - `https://sgeos.github.io/.../2026/04/18/two_dimensional_projection_as_a_coordinate_mapping_problem.html` through `https://sgeos.github.io/.../2026/05/02/camera_as_linear_operator_affine_and_projective_synthesis.html`
- The article number space now runs continuously through A187 across the combined article number space. A188 is the next available.

---

## Notes

- Next available article number: A188.
- 0 release candidates from the two-dimensional projection in games series, the analog-facilities series, or the patent and startup strategy series.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification in `_drafts/`.
- Published through A187 across the combined article number space.
- The two-dimensional projection in games series spans A173 through A187 across 2026-04-18 through 2026-05-02, organised as a six-cluster walk: opener, Cartesian cluster, oblique-and-axonometric cluster, affine-and-projective cluster, cross-cutters, synthesis closer. The series fills the calendar slot immediately before the patent and startup strategy series (A161-A172) at 2026-05-03 through 2026-05-14.
- The analog-facilities series A152 through A160 remains complete on the forward-dated side at 2026-06-28 through 2026-07-06.
- All scratch is confined to project-local `tmp/` per recorded preference.
- The post-drafting `{% post_url %}` conversion pass is deferred as a polish item. The series articles use prose forward references like "the next article in the cluster" and "the cross-cutting picking article later in the series" rather than Liquid tags. Build correctness is unaffected because the references are prose rather than broken Liquid syntax.
- Blog deploys through GitHub Actions with a lean Jekyll stack; `future: true` is enabled in `_config.yml`. The two-dimensional projection in games series is back-dated and renders without dependence on the future flag.
