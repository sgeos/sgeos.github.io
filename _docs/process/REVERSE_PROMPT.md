# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-07-07
**Task**: Draft, verify, and publish A200 "A History of Hardware Description Languages" as a one-off article back-dated to 2026-03-13

---

## Verification

### Article Body Complete

Single-article history of hardware description languages, drafted, publication-reviewed with primary-source verification, and published. The article walks the HDL tradition in one pass across three eras.

- Prehistory and design-complexity forcing function (transistor-count growth per Moore's Law).
- Academic prototypes 1970-1984 (ISPS at Carnegie Mellon under Barbacci, KARL at Kaiserslautern under Hartenstein, ELLA at RSRE UK).
- Commercial standardisation era 1984-2010 (Verilog under Goel, Moorby, and Huang at Automated Integrated Design Systems then Gateway Design Automation 1983-1984, standardised as IEEE 1364 in 1995; VHDL under US Air Force VHSIC contract F33615-83-C-1003 by Intermetrics, Texas Instruments, and IBM in 1983, standardised as IEEE 1076 in 1987; SystemVerilog by Accellera 2002 as IEEE 1800 in 2005; SystemC originated at Synopsys 1999 as IEEE 1666 in 2005; Bluespec by Arvind and Hoe at MIT late 1990s, commercialised by Bluespec Inc. co-founded by Arvind Mithal and Joe Stoy in 2003).
- Embedded-DSL revival 2010-present (Chisel by Asanović's Par Lab team at Berkeley 2012 including Lee and Waterman who also originated RISC-V; SpinalHDL by Papon 2015; Amaranth originally called nMigen by whitequark December 2018, renamed December 2021, succeeding Bourdeauducq's Migen from 2007; MyHDL by Decaluwe 2003; Clash by Baaij at Utrecht and Delft).
- Verification language track (PSL/IEEE 1850, SVA, UVM/IEEE 1800.2).
- High-level synthesis track (behavioural Verilog/VHDL, SystemC HLS via Vivado and Catapult, domain-specific HLS).
- Where the space is going (formal-methods integration, machine-learning-driven design, open-source industrial tooling via Yosys, domain-specific HDLs).

### Two-Commit Publication Pattern

Standard two-commit publication. The draft commit captures the finalised draft in `_drafts/`. The publication commit moves it to `_posts/` with the appropriate date prefix and updates the process files. Git rename detection preserves file history.

### Primary-Source Verification

Publication review included WebSearch verification of load-bearing historical attributions against Wikipedia and project homepages, addressing the lesson from the compilers series that primary-source verification should precede formalisation. Six substantive attribution corrections were applied:

- Verilog: added Chi-Lai Huang as third co-creator; corrected company-name history (Automated Integrated Design Systems renamed to Gateway Design Automation in 1985); corrected development window (late 1983 to early 1984); corrected first-simulator date (1985) and Verilog-XL date (1987); added OVI intermediate step in 1991 preceding IEEE 1364.
- VHDL: distinguished VHSIC program start (1980) from VHDL-specific contract F33615-83-C-1003 (1983); named development team as Intermetrics prime contractor plus Texas Instruments and IBM; added VHDL Analysis and Standardization Group as the IEEE standardisation vehicle in March 1986.
- SystemC: corrected origin to Synopsys 1999 rather than OSCI 2000; added Accellera-OSCI merger December 2011.
- Bluespec: added James Hoe as co-originator of the MIT research with Arvind; named Lennart Augustsson's BH as the Haskell-based initial implementation; correctly attributed Bluespec Inc. co-founding to Arvind Mithal and Joe Stoy of Oxford in June 2003.
- Amaranth: corrected attribution to Catherine "whitequark" beginning December 2018; corrected Amaranth rename to December 2021; distinguished Migen creator Bourdeauducq (2007) from the M-Labs group.
- Chisel: added Par Lab context; named Yunsup Lee and Andrew Waterman as graduate-student co-developers; clarified Rocket Chip as generator that produces RISC-V processor implementations.

### Moore's Law Equation

One display equation added in *Prehistory and the Design-Complexity Forcing Function* formalising Moore's Law as $N(t) = N_0 \cdot 2^{t/T}$ with doubling period $T$ approximately 18-24 months. Mathjax enabled. This is the one load-bearing quantitative claim that the article's design-complexity forcing function argument depends on.

### Style Verification

Zero em-dashes, zero en-dashes, zero contractions, zero prose semicolons outside code blocks and debug tags. Frontmatter uniform with the series conventions: `layout: post`, `mathjax: true`, `comments: true`, `categories: hdl hardware history`. Debug tag `<!-- A200 -->` and `console.log("A200")` in place.

### Status of Process Files

`_docs/process/TASKLOG.md` updated with the A200 publication entry and next-available-article-number advanced to A201. `_drafts/draft_summary.md` extended with an A200 entry at the top. `_docs/process/REVERSE_PROMPT.md` overwritten with this completion report.

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
- A200: history of hardware description languages, published 2026-03-13 (this article).
- Next available article number: A201.

The A200 back-dated date of 2026-03-13 falls in a clear slot between the 2026-03-12 posts (A103 error correction, and the fixed-wing delta wing article) and A102 the 2026-03-14 Keleusma getting started article. No date or article-number collisions.

---

## Action Items for the Human Pilot

- Verify the GitHub Actions deploy completes without errors after the push. The article does not use `{% post_url %}` cross-references, so the deploy is unlikely to fail on that basis.
- Review the published article at its permalink once the deploy completes:
  - `https://sgeos.github.io/hdl/hardware/history/2026/03/13/history_of_hardware_description_languages.html`
- Consider whether to add a Related Post section that cross-references the article from within adjacent history articles.
- If a follow-up HDL article is desired, article number A201 is the next available.

---

## Notes

- Next available article number: A201.
- 0 release candidates from the stream-based compilers series or the hardware description languages article.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification in `_drafts/`.
- Published through A200 across the combined article number space.
- The A200 article is a one-off rather than a series opener. It occupies a single slot at 2026-03-13.
- The article uses aggressive per-phrase line-break rhythm consistent with the recent series style.
- Primary-source verification passes were performed on the six load-bearing historical attributions during publication review, matching the lesson recorded from the compilers series about primary-source verification preceding formalisation.
- All scratch is confined to project-local `tmp/` per recorded preference.
- Blog deploys through GitHub Actions with a lean Jekyll stack. The A200 article is back-dated and renders without dependence on the `future: false` setting.
