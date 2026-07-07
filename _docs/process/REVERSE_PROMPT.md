# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-07-07
**Task**: Research, draft, verify, and publish A201 "The Design Space for Next-Generation Hardware Description Languages" as a companion article to A200

---

## Verification

### Article Body Complete

Single-article companion to A200, drafted with publication review including primary-source verification against Wikipedia, project home pages, and academic literature, and published.

- Opening framed as design-space survey rather than prediction of a specific successor language, grounded in A200's observation that each historical wave responded to a specific abstraction gap.
- Pain points in current industrial HDL flows (pipeline timing verification, clock-domain crossing, area budget verification, deadlock and livelock verification).
- What the embedded-DSL revival languages address (generator-based design, workflow integration, type-system expressiveness) and what they leave open (timing, CDC, area, deadlock still require external verification).
- Four further design levers drawn from adjacent programming-language traditions. Static WCET analysis with Keleusma as software-target example implementing WCET analysis at module load. Totality and productivity as type-system properties formalised through Rutten's universal-coalgebra treatment and subsequent stream-calculus work, with Kami and Koika at MIT as Coq-based formal-verification-integrated HDL demonstrations. Coroutine primitives for CDC with typed yield and resume in Keleusma as software-target analog. Static memory footprint analysis via Keleusma's WCMU discipline as software-target analog.
- Self-hosted synthesis toolchains treatment via Yosys, nextpnr, and F4PGA formerly SymbiFlow as production-adjacent open-source flow.
- Cross-domain description languages closer composing hardware description with SysML v2 for system-level requirements, Modelica for multi-domain physical modelling, and OpenSCAD and CadQuery for constructive geometry.

### Two-Commit Publication Pattern

Standard two-commit publication. The draft commit captures the finalised draft in `_drafts/`. The publication commit moves it to `_posts/` with the appropriate date prefix and updates the process files. Git rename detection preserves file history.

### Primary-Source Verification

Publication review included WebSearch verification of load-bearing technical and historical attributions, matching the lesson from the compilers series that primary-source verification should precede formalisation. Two minor hedges applied during review:

- Rutten attribution refined to acknowledge that productivity was developed in his 2005 stream-calculus work and subsequent Endrullis et al. results rather than the 2000 universal-coalgebra paper alone.
- F4PGA device family claim softened from named subfamilies to family-level ("selected Lattice and Xilinx 7-Series device families") because subfamily-specific claims were general knowledge but not directly verified against search results.

Verified technical claims include Kami MIT CSAIL origin and Coq-based nature, Koika PLDI 2020 provenance and Bluespec-inspired design, Yosys and nextpnr as F4PGA components, F4PGA formerly SymbiFlow, SysML v2 beta approved by OMG July 2023, Modelica Association non-profit status, OpenModelica open-source implementation status, and CDC pragmatic-formal-verification methodology from 2024.

### Certification Barrier Compliance

Zero occurrences of DO-178C, IEC 61508, tool qualification, certification, certified, airworthiness, or Design Assurance Level in the article body. "High-assurance embedded control" is the substitute term for the scrubbed "certification-adjacent embedded control" used near Keleusma naming, matching the compilers-series scrubbed terminology exactly. Von Neumann probe named once, contextualised as "occasionally discussed in the interstellar-mission speculative literature", article explicitly declines to develop the interstellar case because practical applications are substantially closer to present-day engineering.

### Keleusma Treatment

Named directly per user instruction throughout the article. Function categories (`fn`, `yield`, `loop`) attributed correctly to Keleusma's public vocabulary. WCET, WCMU, and coroutine primitives named as Keleusma features implementing software-target analogs of three of the four design levers. Design-in-progress framing preserved at each mention. Zero certification-adjacent framing near Keleusma name.

### Equation Density

Zero display equations. Design-space survey does not have load-bearing quantitative claims. Reviewed candidates (four-lever composition, area-budget decidability, coalgebraic productivity callback from A193) all rejected as decorative annotations of prose claims that were complete without formalisation. The mathjax flag is set to false accordingly.

### Style Verification

Zero em-dashes, zero en-dashes, zero contractions, zero prose semicolons outside code blocks and debug tags. Frontmatter uniform with the series conventions: `layout: post`, `mathjax: false`, `comments: true`, `categories: hdl hardware design`. Debug tag `<!-- A201 -->` and `console.log("A201")` in place.

### Cross-Article References

Related-post entries for A188 (streaming discipline opener), A193 (coalgebraic productivity), and A200 (HDL history). Rutten and Turner DOIs match compiler-series citations. Wilhelm WCET DOI matches A188 citation. Kami, Koika, F4PGA, SysML v2, Modelica, and CDC verification references are new to this article.

### Status of Process Files

`_docs/process/TASKLOG.md` updated with the A201 publication entry and next-available-article-number advanced to A202. `_drafts/draft_summary.md` extended with an A201 entry at the top. `_docs/process/REVERSE_PROMPT.md` overwritten with this completion report.

### Git Status

`git status` confirms one rename from `_drafts/` to `_posts/` in the publication commit, plus the three process-file updates. No other content touched.

---

## Article Number State

The article number space across the blog now reads as follows.

- A1 through A74: legacy published posts predating the modern numbered tracking.
- A75 through A151: published series across 2026-02-06 through 2026-03-14.
- A152 through A160: analog-facilities series, published 2026-06-28 through 2026-07-06.
- A161 through A172: patent and startup strategy series, published 2026-05-03 through 2026-05-14.
- A173 through A187: two-dimensional projection in games series, published 2026-04-18 through 2026-05-02.
- A188 through A199: stream-based compilers series, published 2026-04-06 through 2026-04-17.
- A200: history of hardware description languages, published 2026-03-13.
- A201: design space for next-generation HDLs, published 2026-07-07 (this article).
- Next available article number: A202.

A201 is the first article to publish at today's actual date rather than a back-dated slot. The article is contemporary rather than filling a historical gap.

---

## Action Items for the Human Pilot

- Verify the GitHub Actions deploy completes without errors after the push. The article uses `{% post_url %}` cross-references to A188, A193, and A200 which should resolve given those posts are already deployed.
- Review the published article at its permalink once the deploy completes:
  - `https://sgeos.github.io/hdl/hardware/design/2026/07/07/design_space_next_generation_hardware_description_languages.html`
- If a follow-up article on any specific design lever (WCET at hardware level, coroutine CDC, formal-methods integration with existing HDLs, or self-hosted silicon compilers as a specific research direction) is desired, article number A202 is the next available.

---

## Notes

- Next available article number: A202.
- 0 release candidates from the HDL articles or the stream-based compilers series.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification in `_drafts/`.
- Published through A201 across the combined article number space.
- A201 is the first article published at today's actual date rather than a back-dated slot.
- The article uses aggressive per-phrase line-break rhythm consistent with the recent series style.
- Primary-source verification passes were performed during publication review, matching the lesson recorded from the compilers series about primary-source verification preceding formalisation.
- Keleusma is named directly per user instruction, with design-in-progress framing preserved and certification-adjacent framing scrubbed.
- All scratch is confined to project-local `tmp/` per recorded preference.
- Blog deploys through GitHub Actions with a lean Jekyll stack. The article renders without dependence on the `future: false` setting because it is dated at today's actual date.
