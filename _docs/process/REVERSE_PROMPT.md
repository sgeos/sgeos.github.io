# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-07-08
**Task**: Research, draft, verify, and publish A203 "Hardware Description Languages, the State of the Practice" as the third article in the HDL thread completing the three-time-frame survey with A200 and A201

---

## Verification

### Article Body Complete

Single-article state-of-the-practice survey, drafted with publication review including primary-source verification against Wikipedia, project home pages, industry press, and the Wilson Research Group functional verification study, and published locally through the two-commit sequence.

- Opening establishes third-time-frame framing (A200 past, A201 future, A203 present) with explicit acknowledgment that market-share data resists precise quantification and is directional rather than exact.
- Industrial mainstream landscape covering the persistent Verilog/VHDL split with regional patterns, SystemVerilog absorption for new design work, SystemC in system-level and high-level synthesis flows, and Bluespec in specialised niches. Wilson Research Group 2024 study data cited for first-silicon success rate (approximately fourteen percent) and verification methodology adoption.
- Vendor toolchain landscape covering AMD Vivado (released 2012 by Xilinx, inherited by AMD after 2022 acquisition), Intel Quartus Prime (with corrected Altera timeline: 2015 Intel acquisition, 2025 Silver Lake 51% majority divestiture), Synopsys Synplify, and Cadence and Siemens EDA complementary tooling.
- Open-source toolchain landscape covering Yosys (started 2012 at Vienna University of Technology by Claire Wolf, name updated from earlier attribution), nextpnr, F4PGA formerly SymbiFlow, and Project IceStorm.
- Embedded-domain-specific-language revival adoption: Chisel with Rocket Chip generator and SiFive (named specifically as founded 2015 by Asanović, Lee, and Waterman from UC Berkeley) and FireSim FPGA-accelerated simulation, Amaranth with LiteX system-on-chip generators, SpinalHDL with VexRiscv soft processor, Clash in Haskell functional-programming research groups, MyHDL in educational contexts.
- Formal verification adoption trajectory citing Wilson Research Group 2024 study for growth from approximately thirty percent to sixty percent over a decade. Industrial platforms JasperGold, VC Formal, Questa Formal. Academic research from Chlipala's MIT Programming Languages and Verification group covering Kami and Koika.
- Additional and emerging languages: Silice by Sylvain Lefebvre at INRIA France with Doom-on-ECP5 demonstration corpus; DFHDL Scala-based multi-abstraction dataflow HDL from DFiantHDL organisation; LiteX and Migen family; PyMTL from Cornell University.
- Domain-specific adoption patterns for automotive/aerospace safety-critical segments, consumer electronics and mobile processor design, RISC-V processor design, academic computer architecture research, and hobbyist/open-source hardware contexts.
- Adoption trajectory closing section synthesising persistent Verilog/VHDL mainstream, gradual SystemVerilog absorption, growing formal verification integration, and maturing open-source toolchain device-family coverage.

### Two-Commit Publication Pattern

Standard two-commit publication. The draft commit captures the finalised draft in `_drafts/`. The publication commit moves it to `_posts/` with the appropriate date prefix and updates the process files. Git rename detection preserves file history.

### Primary-Source Verification

Publication review included WebSearch verification of load-bearing historical and technical attributions. Three corrections applied:

- Intel Altera timeline corrected. The earlier draft said "Intel's two thousand twenty-two Programmable Solutions Group spin-off, which subsequently became Altera Corporation again". Corrected to the full accurate timeline: Intel acquired Altera in 2015 for approximately seventeen billion United States dollars, then divested a fifty-one percent majority stake to Silver Lake Partners in 2025 for approximately eight point seven five billion United States dollars, with Altera returning to its independent Altera Corporation name and Intel retaining a forty-nine percent minority stake.
- SiFive founders named specifically. The earlier draft said "several members of the Berkeley Par Lab team". Corrected to name Krste Asanović, Yunsup Lee, and Andrew Waterman from UC Berkeley in 2015, matching A200's attribution for the same three individuals who originated Chisel and RISC-V.
- Wolf name updated. Yosys was founded under "Clifford Wolf" but the person is now Claire Wolf. Updated both instances in the article to the current name, which is more accurate and respectful.

Verified historical claims: Vivado released by Xilinx in 2012, AMD acquisition of Xilinx completed 14 February 2022 for $49 billion, Yosys started 2012 at Vienna University of Technology as a bachelor's thesis, SiFive founded 2015 by Asanović, Lee, and Waterman from UC Berkeley (RISC-V originated in same team's 2010 summer project), Silice by Sylvain Lefebvre at INRIA France, DFHDL as Scala-based multi-abstraction dataflow HDL, Wilson Research Group 2024 study first-silicon success rate approximately fourteen percent and formal verification growth from approximately thirty percent to sixty percent over a decade.

### Certification Barrier Compliance

Zero occurrences of DO-178C, IEC 61508, tool qualification, certification, certified, airworthiness, or Design Assurance Level in the article body. Only "safety-critical" as a generic descriptor per the memo's allowed usage, appearing in the domain-specific adoption section where automotive and aerospace segments are named as having higher verification methodology adoption. No Keleusma naming in this article because state-of-the-practice framing focuses on actual current adoption and a design-in-progress language does not fit that scope. No von Neumann probe naming.

### Equation Density

Zero display equations. State-of-the-practice survey has no load-bearing quantitative claim that would benefit from formalisation. The three quantitative claims the article does make (approximately eighty-five to ninety percent Verilog/VHDL share, fourteen percent first-silicon success rate, thirty-to-sixty-percent formal verification adoption growth) are directional survey estimates that would gain nothing from symbolic formalisation. The three HDL articles form a consistent set with A200 having one Moore's Law equation as load-bearing forcing function, A201 having zero equations, and A203 having zero equations.

### Style Verification

Zero em-dashes, zero en-dashes, zero contractions, zero prose semicolons outside code blocks and debug tags. Frontmatter uniform with the series conventions: `layout: post`, `mathjax: false`, `comments: true`, `categories: hdl hardware adoption`. Debug tag `<!-- A203 -->` and `console.log("A203")` in place.

### Cross-Article References

Related-post entries for A200 (HDL history) and A201 (HDL design space). A200 and A201 are referenced substantively in the opening and closing sections as the historical and design-space treatments that A203 completes. No compiler-series cross-references because the topic scope focuses on hardware description language adoption rather than compilation. Kami and Koika DOIs match A201 usage.

### Status of Process Files

`_docs/process/TASKLOG.md` updated with the A203 publication entry and next-available-article-number advanced to A204. `_drafts/draft_summary.md` extended with an A203 entry at the top. `_docs/process/REVERSE_PROMPT.md` overwritten with this completion report.

### Git Status

`git status` after the two commits should show a clean working tree ahead of `origin/master` by two commits. The commits are the draft commit `d53251f` and the publication commit that follows.

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
- A201: design space for next-generation HDLs, published 2026-07-07.
- A202: meta-factory prior art and the reproduction loop, published 2026-07-08 at 09:00 UTC.
- A203: hardware description languages the state of the practice, published 2026-07-08 at 12:00 UTC (this article).
- Next available article number: A204.

A203 is the third consecutive current-date publication after A201 and A202. The three HDL articles now form a coherent past/future/present survey.

---

## Action Items for the Human Pilot

- Verify the GitHub Actions deploy completes without errors after the push. The article uses `{% post_url %}` cross-references to A200 and A201 which should resolve given those posts are already deployed.
- Review the published article at its permalink once the deploy completes:
  - `https://sgeos.github.io/hdl/hardware/adoption/2026/07/08/hardware_description_languages_state_of_the_practice.html`
- The three HDL articles A200, A201, A203 now form a coherent past/future/present survey. A follow-up article on any specific adoption thread (specific RISC-V processor design case study, specific verification methodology deep-dive, specific vendor toolchain analysis, or specific device family comparison) could work as A204, or the thread could pause and step away.

---

## Notes

- Next available article number: A204.
- 0 release candidates from the HDL articles or the meta-factory article.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification in `_drafts/`.
- Published through A203 across the combined article number space.
- A201, A202, and A203 form three consecutive current-date publications spanning HDL design space, manufacturing prior art, and HDL state of the practice.
- The article uses aggressive per-phrase line-break rhythm consistent with the recent series style.
- Primary-source verification passes were performed during publication review, matching the lesson recorded from the compilers series about primary-source verification preceding formalisation.
- Keleusma not named in A203 by deliberate editorial choice given the state-of-the-practice framing focuses on actual current adoption.
- All scratch is confined to project-local `tmp/` per recorded preference.
- Blog deploys through GitHub Actions with a lean Jekyll stack. The article renders without dependence on the `future: false` setting because it is dated at current day.
