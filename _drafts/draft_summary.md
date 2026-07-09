---
layout: post
mathjax: false
comments: true
title: "Draft Summary"
date: 2000-01-01 00:00:00 +0000
categories: meta
---

<!-- Axxx -->

This post reviews the status of draft posts in this blog's `_drafts/` directory.
Each draft is assessed for topic, completion status, remaining work, and publication sensibility.
Assessments assume that contemporary tooling will be used if salvaged
and that appropriate ecosystem standard choices will replace any tooling that has fallen out of favor.
Missing sections and prose will need to be drafted.
Stubs and largely incomplete drafts are assessed for topicality and publication merit.

## Draft Status

### Getting Started with Keleusma 0.2.1 (A205) — Published

**File**: `_posts/2026-07-09-keleusma_0_2_1_getting_started.markdown`

**Topic**: Third article in the Keleusma getting-started series with A107 (0.1.1) and A110 (0.2.0). Practical walkthrough of the material additions in the 0.2.1 release tagged 2026-07-08. Sections cover: software versions and installation; the boolean/bitwise/shift operator families (`band`/`bor`/`bxor`/`bnot`, `lsl`/`asl`/`lsr`/`asr`, eager `and`/`or`/`xor`/`not` and short-circuit `andalso`/`orelse`); general const generics superseding the earlier `Multiword<N, F>` special case; executable shebang scripts and the script argument vector via `shell::arg` and `shell::arg_count`; debug `assert` statements with strippable debug-record backing; partial-operation handling for checked arithmetic and array indexing and refinement-newtype construction; strippable debug metadata via `keleusma compile --debug` and `keleusma strip`; operator-configured strict-mode deployment policy for signed and encrypted bytecode; and an Under the Hood section covering the flat-byte composite runtime representation, the typed operand-stack verifier pass, and trait-method resolution on generic structs. Closer sketches the 0.2.2 development cycle's self-hosted-compiler groundwork and cross-references the streaming compilers series conclusion (A199) and the self-hosted silicon compiler article (A204).

**Article Number**: A205
**Completion**: 100%
**Publication Sensibility**: High (companion to A107 and A110 aligned with the recently tagged 0.2.1 release, every code listing verified against an installed 0.2.1 CLI)
**Status**: Published 2026-07-09 at 12:00 UTC. 724 lines, mathjax false, zero display equations. All code listings executed against an installed `keleusma 0.2.1` and outputs recorded verbatim. Cross-references A107, A110, A109 (verifiable control kernel), A111 (information-flow control deep dive), A199 (streaming compilers conclusion), and A204 (self-hosted silicon compiler). Categories `rust embedded programming`. External URLs pinned to the `v0.2.1` tag. Two-commit publication pattern; commits local pending push authorisation.

### The Self-Hosted Silicon Compiler (A204) — Published

**File**: `_posts/2026-07-09-self_hosted_silicon_compiler.markdown`

**Topic**: Fifth article completing the five-article HDL and manufacturing thread with A200 (history), A201 (design space), A202 (meta-factory), and A203 (state of the practice). Addresses the specific integration point between the computational and manufacturing halves of the reproduction loop identified in A201 and A202. Sections cover: definition of self-hosting for silicon compilation (narrow silicon compiler translation, strong vs weak self-hosting forms, dependency reduction and reproduction-loop rationales); software bootstrap precedent citing A199 fixed-point condition, Ken Thompson's 1984 Turing Award lecture Reflections on Trusting Trust published in CACM Vol 27 No 8 August 1984, and David A. Wheeler's 2009 Diverse Double-Compilation countermeasure; Gabriel Somlo's Trustworthy Free Libre Linux-Capable Self-Hosting sixty-four-bit RISC-V Computer at Carnegie Mellon University Software Engineering Institute as strongest existing demonstration with Rocket Chip RISC-V core on LiteX system-on-chip on Lattice ECP5 field-programmable-gate-array with Yosys and Project Trellis and nextpnr toolchain running Fedora Linux; silicon boundary distinguishing what current self-hosting reaches versus what remains below the fabrication boundary; research directions toward compact self-hosting toolchains including Silice minimal grammar by Sylvain Lefebvre at INRIA and Keleusma design-in-progress software-target example and on-fabric compilation acceleration and bootstrap procedure design; applications in trust-adjacent computing citing Wheeler DDC use case and educational contexts and long-term autonomy contexts and reproducible-builds hardware distribution; meta-factory connection tying computational self-hosting to A202's mechanical prior art including brief mention of three additional required system components (materials refinery, kinematic fabricator, meta-cognitive orchestration). Two publication-review hedges applied: Yosys source size softened from specific one-hundred-thousand-lines figure to on-the-order-of-several-hundred-thousand-lines directional claim, and Somlo/DDC connection softened to note Somlo references DDC as related mitigation rather than as integrated bootstrap component.

**Article Number**: A204
**Completion**: 100%
**Publication Sensibility**: High (closes the five-article HDL and manufacturing thread with the specific integration point that ties the computational and manufacturing halves of the reproduction loop, grounded in Somlo's substantial existing work rather than speculation)
**Status**: Published 2026-07-09 (editorial date, tomorrow). 1805 lines, mathjax false, zero display equations. Historical and technical claims verified against primary sources including Thompson CACM 1984, Wheeler arxiv 2010, Somlo CMU SEI project pages, and Wikipedia bootstrapping compilers article. Keleusma named directly with design-in-progress framing. Von Neumann probe named once with explicit decline to develop interstellar case. Categories `hdl hardware self-hosting`.

### Hardware Description Languages, the State of the Practice (A203) — Published

**File**: `_posts/2026-07-08-hardware_description_languages_state_of_the_practice.markdown`

**Topic**: Third article in the HDL thread completing the three-time-frame survey with A200 (history) and A201 (design space). State-of-the-practice framing covering industrial mainstream landscape (Verilog/VHDL split with regional patterns, SystemVerilog absorption for new work, SystemC in system-level modelling, Bluespec in specialised niches), vendor toolchain landscape (AMD Vivado post-2022 Xilinx acquisition, Intel Quartus with 2015 Altera acquisition and 2025 Silver Lake divestiture, Synopsys Synplify, Cadence, Siemens EDA), open-source toolchain landscape (Yosys started 2012 at Vienna University of Technology by Claire Wolf, nextpnr, F4PGA formerly SymbiFlow, Project IceStorm), embedded-DSL revival adoption (Chisel with Rocket Chip generator and SiFive founded 2015 by Asanović/Lee/Waterman from UC Berkeley and FireSim FPGA-accelerated simulation, Amaranth with LiteX system-on-chip generators, SpinalHDL with VexRiscv soft processor, Clash in Haskell research groups, MyHDL in educational contexts), formal verification adoption citing Wilson Research Group 2024 study for growth from approximately thirty percent to sixty percent over a decade and industrial platforms JasperGold VC Formal Questa Formal alongside academic Kami and Koika from Chlipala's MIT PLV group, additional and emerging languages (Silice by Sylvain Lefebvre at INRIA France with Doom-on-ECP5 demonstration, DFHDL Scala-based multi-abstraction dataflow HDL, LiteX Migen family, PyMTL from Cornell), domain-specific adoption patterns for automotive/aerospace safety-critical segments and consumer/mobile and RISC-V processor design and academic computer architecture and hobbyist/open-source contexts, closing adoption trajectory synthesising the persistent Verilog/VHDL mainstream with gradual SystemVerilog absorption plus growing formal verification integration plus maturing open-source toolchain device-family coverage. Wilson Research Group 2024 first-silicon success rate figure (approximately fourteen percent) cited as evidence of design-complexity forcing function. Keleusma not named because state-of-the-practice framing does not include design-in-progress language.

**Article Number**: A203
**Completion**: 100%
**Publication Sensibility**: High (completes the three-time-frame HDL survey started with A200 and A201, brings distinct current-adoption content and Wilson Research Group 2024 verification study data that A200 and A201 did not cover)
**Status**: Published 2026-07-08 at 12:00 UTC to sequence after A202 which was 09:00 UTC on the same date. 1763 lines, mathjax false, zero display equations. Three publication-review corrections applied: Intel-Altera timeline; SiFive founders named; Wolf name updated to current Claire Wolf. Categories `hdl hardware adoption`.

### The Meta-Factory, Prior Art and the Reproduction Loop (A202) — Published

**File**: `_posts/2026-07-08-meta_factory_prior_art_and_the_reproduction_loop.markdown`

**Topic**: Companion article to A201 covering the physical-reproduction side of the reproduction loop that A201's self-hosted synthesis toolchains occupy on the computational side. Historical prior-art survey across four traditions: von Neumann's Universal Constructor from Theory of Self-Reproducing Automata edited by Arthur W. Burks and published posthumously by University of Illinois Press in 1966; the 1980 NASA studies including von Tiesenhausen and Darbro TM-78304 at Marshall Space Flight Center in July 1980 and the NASA-ASEE Summer Study proceedings published as CP-2255 edited by Freitas and Gilbreath in November 1982 with the 150-page self-replicating lunar factory chapter proposing a 20-year development program; Freitas and Merkle's 2004 Kinematic Self-Replicating Machines from Landes Bioscience with its 137-dimensional design-space taxonomy funded by Zyvex; RepRap project by Adrian Bowyer at University of Bath from 23 March 2005 with first self-print 13 September 2006 and Darwin first-generation printer at London Science Museum; industrial digital-twin meta-factories exemplified by Hyundai Motor Group Innovation Center Singapore on NVIDIA Omniverse platform. Closing section synthesises with A201 recording that both computational and mechanical sides of the reproduction loop have established prior art, with remaining engineering work being integration rather than invention. Keleusma named briefly with design-in-progress framing and explicit note that meta-factory prior art does not depend on any specific programming language. Von Neumann probe named once with explicit decline to develop the interstellar case. High-assurance embedded control substituted for scrubbed certification-adjacent framing.

**Article Number**: A202
**Completion**: 100%
**Publication Sensibility**: High (companion to A201 grounded in substantial engineering literature rather than speculation, extends the HDL-and-reproduction thread to the manufacturing side of the loop)
**Status**: Published 2026-07-08 (back-dated by one day for tomorrow's scheduled publication). 1465 lines, mathjax false, zero display equations. Historical attributions verified against Wikipedia, NASA NTRS, molecularassembler.com, RepRap project pages, and NVIDIA press releases. Two hedges applied during publication review. Categories `manufacturing self-replication history`.

### The Design Space for Next-Generation Hardware Description Languages (A201) — Published

**File**: `_posts/2026-07-07-design_space_next_generation_hardware_description_languages.markdown`

**Topic**: Companion to A200 covering the design space for next-generation hardware description languages. Four pain points in current industrial HDL flows (pipeline timing verification, clock-domain crossing, area budget verification, deadlock and livelock verification). Treatment of what the embedded-DSL revival languages (Chisel, SpinalHDL, Amaranth, Clash) address and what they leave open. Four further design levers drawn from adjacent programming-language traditions: static WCET analysis with Keleusma as software-target example, totality and productivity as type-system properties with Kami and Koika at MIT as formal-verification-integrated HDL demonstrations, coroutine primitives for clock-domain crossing, and static memory footprint analysis. Self-hosted synthesis toolchains treatment via Yosys, nextpnr, and F4PGA formerly SymbiFlow as production-adjacent open-source flow. Closer on cross-domain description languages composing hardware description with system-level requirements (SysML v2), multi-domain physical modelling (Modelica), and constructive geometry (OpenSCAD, CadQuery). Keleusma named directly, treated as design-in-progress example implementing software-target analogs of three of the four design levers. Von Neumann probe named once as speculative literature, article declines to develop the case. High-assurance embedded control terminology substituted for scrubbed certification-adjacent framing. Zero display equations because the design-space survey does not have load-bearing quantitative claims.

**Article Number**: A201
**Completion**: 100%
**Publication Sensibility**: High (companion to A200 grounded in the same lineage, extending A200's historical treatment into current-decade design-space analysis)
**Status**: Published 2026-07-07. 1585 lines, mathjax false, 24 references including inline citations to Kami, Koika, F4PGA, Yosys, nextpnr, SysML v2, Modelica, and CDC pragmatic-formal-verification work. Historical and technical claims verified against primary sources including MIT CSAIL PLV project page, PLDI 2020 paper, OMG press release, and open-source project documentation. Categories `hdl hardware design`.

### A History of Hardware Description Languages (A200) — Published

**File**: `_posts/2026-03-13-history_of_hardware_description_languages.markdown`

**Topic**: One-off history of hardware description languages across five decades. Three-era organisation: academic prototypes 1970-1984 (ISPS at Carnegie Mellon under Barbacci, KARL at Kaiserslautern under Hartenstein, ELLA at RSRE UK); commercial standardisation era 1984-2010 (Verilog developed by Goel, Moorby, and Huang at Automated Integrated Design Systems/Gateway 1983-1984 and standardised as IEEE 1364 in 1995; VHDL developed by Intermetrics, Texas Instruments, and IBM under US Air Force VHSIC contract 1983 and standardised as IEEE 1076 in 1987; SystemVerilog by Accellera 2002 as IEEE 1800 in 2005; SystemC originated at Synopsys 1999 and standardised as IEEE 1666 in 2005; Bluespec by Arvind and Hoe at MIT late 1990s, commercialised by Bluespec Inc. co-founded by Arvind Mithal and Joe Stoy in 2003); and embedded-DSL revival 2010-present (Chisel by Asanović's Par Lab team at Berkeley 2012 including Lee and Waterman who also originated RISC-V; SpinalHDL by Papon 2015; Amaranth originally called nMigen by whitequark December 2018, renamed December 2021, succeeding Bourdeauducq's Migen from 2007; MyHDL by Decaluwe 2003; Clash by Baaij at Utrecht and Delft). Verification language track (PSL/IEEE 1850, SVA, UVM/IEEE 1800.2) and high-level synthesis track (behavioural Verilog/VHDL, SystemC HLS via Vivado and Catapult, domain-specific HLS). Closes with observations on formal-methods integration, machine-learning-driven design synthesis, open-source industrial tooling via Yosys, and domain-specific hardware description as the emerging next wave. One display equation formalising Moore's Law $N(t) = N_0 \cdot 2^{t/T}$ as the design-complexity forcing function that repeats at each historical wave.

**Article Number**: A200
**Completion**: 100%
**Publication Sensibility**: High (comprehensive one-article treatment of the HDL space, covering the full lineage from academic prototypes through modern embedded-DSL revival with primary-source-verified attributions)
**Status**: Published 2026-03-13 (back-dated). 1903 lines, one display equation, mathjax enabled. Six substantive attribution corrections applied during publication review after WebSearch verification against Wikipedia and project homepages. Categories `hdl hardware history`.

### Stream-Based Compilers series (A188-A199) — Published

**Files**:
- `_posts/2026-04-06-compilation_as_streaming_discipline.markdown` (A188)
- `_posts/2026-04-07-wirth_single_pass_line.markdown` (A189)
- `_posts/2026-04-08-turbo_pascal_closed_source_demonstration.markdown` (A190)
- `_posts/2026-04-09-brinch_hansen_pipeline_of_processes.markdown` (A191)
- `_posts/2026-04-10-block_structured_single_pass_validation.markdown` (A192)
- `_posts/2026-04-11-coalgebraic_productivity_stream_processor_analogy.markdown` (A193)
- `_posts/2026-04-12-fixup_tables_forward_jump_problem.markdown` (A194)
- `_posts/2026-04-13-declare_before_use_forward_declarations.markdown` (A195)
- `_posts/2026-04-14-symbol_tables_scope_popping_bounded_memory.markdown` (A196)
- `_posts/2026-04-15-integrated_single_pass_versus_decomposed_pipeline.markdown` (A197)
- `_posts/2026-04-16-when_multi_pass_wins.markdown` (A198)
- `_posts/2026-04-17-stream_processor_as_compiler_and_compiler_as_stream_processor.markdown` (A199)

**Topic**: Twelve-article series on the stream-processor compilation discipline. Covers the historical demonstrations (Wirth's PL/0 through Oberon line, Turbo Pascal as the closed-source commercial demonstration, Brinch Hansen's pipeline-of-processes architecture and SuperPascal self-hosting), the mathematical foundation (block-structured control flow with the WebAssembly single-pass validator per Haas et al. PLDI 2017 and Watt's Isabelle mechanisation; coalgebraic productivity per Rutten's universal-coalgebra treatment and stream calculus, with the Endrullis decidability result, the Abel-Pientka copattern framework, and Turner's total functional programming), the engineering techniques (fixup tables with the forward-jump problem, declare-before-use ordering with forward declarations for mutual recursion, scoped symbol tables with the scope-popping discipline), the architectural synthesis (integrated single-pass versus decomposed pipeline compared head-to-head with Keleusma V0.3.0 as modern worked example; when multi-pass wins covering whole-program optimisation, Hindley-Milner unification, type-class resolution, and metaprogramming), and the series closer (the compiler as stream processor and the stream processor as compiler, with the Keleusma five-stage compilation pipeline formalised as function composition and its compositional working-memory bound derived from the WCMU analysis). Historical claims flagged with epistemic markers throughout, especially A190 Turbo Pascal treatment where the compiler internals were never released as open source. Keleusma treatment consistently frames V0.3.0 self-hosting as design-in-progress rather than shipped result. MathJax enabled throughout.

**Article Numbers**: A188 through A199 (twelve articles)
**Completion**: 100%
**Publication Sensibility**: High (comprehensive treatment of the stream-processor compilation discipline as a distinct architectural tradition, with rigorous mathematical foundation from coalgebraic productivity theory, engineering technique specifications, and modern realisation via Keleusma's pipeline)
**Status**: Published 2026-04-06 through 2026-04-17 (back-dated, landing flush with the two-dimensional projection in games series at 2026-04-18). Total ~14,273 lines and ~90 display equations across twelve articles. Historical trio A189-A191, theory pair A192-A193, techniques trio A194-A196, synthesis pair A197-A198, opener A188 and closer A199.

### Two-Dimensional Projection in Games series (A173-A187) — Published

**Files**:
- `_posts/2026-04-18-two_dimensional_projection_as_a_coordinate_mapping_problem.markdown` (A173)
- `_posts/2026-04-19-top_down_projection_without_height.markdown` (A174)
- `_posts/2026-04-20-top_down_with_decoupled_vertical_axis.markdown` (A175)
- `_posts/2026-04-21-side_scrolling_without_depth.markdown` (A176)
- `_posts/2026-04-22-side_scrolling_with_parallax_layers.markdown` (A177)
- `_posts/2026-04-23-belt_scroll_side_scrolling_with_explicit_depth.markdown` (A178)
- `_posts/2026-04-24-oblique_projection_and_quarter_view.markdown` (A179)
- `_posts/2026-04-25-axonometric_projection_isometric_dimetric_trimetric.markdown` (A180)
- `_posts/2026-04-26-mode_7_and_affine_ground_plane.markdown` (A181)
- `_posts/2026-04-27-sprite_scaling_pseudo_three_dimensional.markdown` (A182)
- `_posts/2026-04-28-raycasting_two_dimensional_map_rendered_as_three_dimensions.markdown` (A183)
- `_posts/2026-04-29-stylised_and_hybrid_projections_inconsistent_frame.markdown` (A184)
- `_posts/2026-04-30-draw_order_y_sort_z_sort_and_painters_algorithm.markdown` (A185)
- `_posts/2026-05-01-picking_and_hit_testing_in_pseudo_three_dimensional_projections.markdown` (A186)
- `_posts/2026-05-02-camera_as_linear_operator_affine_and_projective_synthesis.markdown` (A187)

**Topic**: Fifteen-article series on two-dimensional projection in games, covering the math of translating internal world coordinates (2D, pseudo-3D with layer-based depth, and 3D) to screen space, and translating screen-space input back into world space. Organised into six clusters: A173 opener (Two-Dimensional Projection as a Coordinate Mapping Problem framing the forward map and inverse map duality, the math-versus-delivery distinction, and the series roadmap); A174-A178 Cartesian cluster (top-down without height as the floor case, decoupled vertical axis with shadow drop, side-scrolling without depth, side-scrolling with parallax layers, belt-scroll with explicit depth); A179-A180 oblique-and-axonometric cluster (oblique cabinet/cavalier projection with quarter view, axonometric with isometric/dimetric/trimetric variants); A181-A184 affine-and-projective cluster (Mode 7 per-scanline affine ground plane, sprite scaling pseudo-three-dimensional including Battle Clash and Metal Combat, raycasting with fisheye correction, stylised hybrid projections with the Mother lineage and Limbo/Inside stylised post-processing); A185-A186 cross-cutters (draw order with Painter's Algorithm and Y-sort/Z-sort/hybrid sort criteria, picking and hit testing with condition number bounds and the canonical sprite-scale-and-rotate light-gun hit test); A187 synthesis closer (the camera as linear operator showing the PVM pipeline and recovering each previous projection mode as a restricted case of the modern graphics-processing-unit pipeline). Each article carries the standard projection-mode template (Brief History, Forward Map, Inverse Map, Worked Example, Variations Within the Mode, Delivery Mechanisms, Where the Framing Breaks Down, Canon, Out of Scope, Conclusion, References), with appropriate variations for the opener, cross-cutters, and synthesis closer. The y-down depth-into-screen convention is established in A174 and carried throughout the series. MathJax enabled throughout.

**Article Numbers**: A173 through A187 (fifteen articles)
**Completion**: 100%
**Publication Sensibility**: High (a comprehensive series treating every major two-dimensional projection mode in commercial games, with cross-cutting articles on draw order and picking and a synthesis closer that ties the series to the modern projective pipeline)
**Status**: Published 2026-04-18 through 2026-05-02 (back-dated, landing flush with the patent and startup strategy series at 2026-05-03). Total ~14,640 lines, ~343 display equations, ~1,144 inline expressions, ~106 unique references across the fifteen articles. Forward references in prose to be converted to {% post_url %} Liquid tags in a follow-up pass.

### Venus Cloudtop Buoyant Analog — Published

**File**: `_posts/2026-07-06-venus_cloudtop_buoyant_analog.markdown`
**Topic**: Eighth and final per-subsystem deep-dive in the analog-facilities category following A152 through A159, closing the series at the most conspicuous gap A152 identified (the buoyant cloudtop habitat for Venus). Uses the framing that the buoyancy condition is the architectural keystone, with envelope volume, internal atmosphere mass, structural mass, operating altitude band, and subsystem mass budget all dimensioned against the density differential between the internal Earth breathing-mix atmosphere and the external Venus CO2 atmosphere. Derives buoyancy from first principles with worked example at ~6,320 kg total mass for four-crew habitat requiring ~10,500 m^3 envelope at 55 km altitude. References Landis 2003 Colonization of Venus paper and NASA Langley HAVOC 2014-2015 concept. Includes a dedicated synthesis section walking each of the seven prior subsystem articles and explaining how its architectural keystone adapts to the Venus cloudtop context (electricity benefits from 1.92x Earth solar irradiance, water faces sulfuric acid clouds requiring high-closure recovery, communications inherits link budget with cloud attenuation and super-rotation considerations, food benefits from abundant CO2 and high PAR, habitat envelope shifts from pressure containment to acid and UV durability, waste loses several disposition pathways and must rely on incineration and biological processing, transportation gains zero-velocity horizontal travel via super-rotation but loses surface access). Covers terrestrial stratospheric platforms (World View Stratollite, dormant Loon, Sceye, LTA Research Pathfinder, Goodyear Wingfoot) as closest available proxies, no-buoyancy architectures (Venus surface, orbit, flyby), terrestrial-only cheats, keystone-breakdown cases, and a major Series Synthesis section reviewing all eight architectural keystones across the analog-facilities series. MathJax enabled.
**Article Number**: A160
**Completion**: 100%
**Publication Sensibility**: High (closes the analog-facilities series as the planned terminus per the dirigible-last request, addresses the explicit gap from A152)
**Status**: Published 2026-07-06 (20 references; ~1,411 lines; mathjax true with 15 display equations and 28 inline expressions; series terminus)

### Garbage and Transportation for Off-Grid Space Colonization Analogs — Published

**File**: `_posts/2026-07-05-garbage_and_transportation_for_off_grid_space_colonization_analogs.markdown`
**Topic**: Seventh per-subsystem deep-dive in the analog-facilities category following A152 through A158, the penultimate article before the A160 Venus cloudtop closer. Treats transportation as the primary subject with garbage logistics as a specific use case. Uses the framing that the cargo throughput rate is the architectural keystone, with vehicle fleet sizing, route infrastructure, energy budget, and endpoint storage all dimensioned against the throughput. Derives throughput from first principles with worked 50 kg/day example, vehicle fleet sizing with worked utilisation example, rolling resistance and aerodynamic drag equations, gravitational work, energy budget for surface vehicle with 54 kWh worked example, the Tsiolkovsky rocket equation with propellant mass fraction derivation and 0.94 worked example. Walks dependent components covering vehicles (wheeled, tracked, planetary rover including corrected Apollo LRV cruise 13 km/h and 18 km/h record with Apollo 17 traverse 35.9 km, Mars rovers, NASA LTVS Lunar Outpost/Lunar Dawn/Astrolab), routes (paved, graded earth, marked, fixed-rail, no-route), energy supply (chemical, battery, hydrogen, solar), loading and unloading, endpoint storage, crew movement, garbage and bulk solid waste transport with pickup frequency equation. Transportation modes summary with comparative analysis. Covers no-transportation architectures (point-of-use disposition, drop-shipment, self-propelled cargo), terrestrial-only cheats (public road network, commercial freight, refuelling), space-only options (orbital manoeuvre, suborbital hopping, lunar/Mars surface rovers, sample return, electromagnetic launch). Closes on three cases where the keystone framing breaks down (zero-throughput closed colony, surge regime, catastrophic failure). Generalisation section walks residential homestead, remote research station with Antarctic traverse, disaster relief, mining/oilfield camp, maritime vessel under IMO, and forward operating base. MathJax enabled.
**Article Number**: A159
**Completion**: 100%
**Publication Sensibility**: High for the space-themed cluster (seventh per-subsystem article continues the deep-dive cadence under A152's nine-subsystem roadmap, penultimate to the A160 Venus cloudtop closer)
**Status**: Published 2026-07-05 (18 references; ~1,404 lines; mathjax true with 19 display equations and 26 inline expressions)

### Waste and Sewage Management for Off-Grid Space Colonization Analogs — Published

**File**: `_posts/2026-07-04-waste_and_sewage_management_for_off_grid_space_colonization_analogs.markdown`
**Topic**: Sixth per-subsystem deep-dive in the analog-facilities category following A152 through A157. Treats the waste subsystem under the framing that the waste mass balance is the architectural keystone, with stream classification, treatment train selection, storage capacity, regulatory compliance, and disposition pathway all dimensioned against the per-crew per-day waste production rate. Distinguishes itself from A154 by treating the broader waste universe (solid waste, food packaging, hazardous waste, atmospheric trace contaminants, regulated streams) beyond the water-recovery overlap. Derives mass balance from first principles with worked example for a four-crew habitat producing approximately twenty kilograms per day total waste, storage volume of 5.4 cubic metres at fifty percent closure across six-month disposition cadence, and disposition mass flux. Walks dependent components covering stream classification (urine, faeces, food preparation waste, packaging, hazardous, atmospheric), collection subsystem with vacuum-flow toilet, treatment train (vapour compression distillation, composting, anaerobic digestion, incineration with corrected 5 to 10 percent ash residue, plasma pyrolysis, mechanical compactor with compaction ratio equation and Heat Melt Compactor reference), storage, disposition pathways (destructive reentry, return-to-Earth, incineration, regolith burial, vacuum venting under planetary protection, biological processing, recycling), hazardous waste handling under RCRA, and atmospheric waste handling. Treatment technologies section covers carbon dioxide removal through lithium hydroxide canister with stoichiometric mass ratio derivation, regenerable amine swing-bed Carbon Dioxide Removal Assembly, Sabatier reactor with reaction equation, Bosch reactor with reaction equation, trace contaminant control, particulate filtration, and composting/anaerobic digestion. Covers no-treatment architectures (storage-only with linear storage scaling equation, dump-and-forget, vacuum-vent), terrestrial-only cheats (municipal sewer, curbside trash, hazardous waste transporter), and space-only options (destructive reentry, regolith burial citing 96 Apollo lunar waste bags, vacuum venting under COSPAR, in-situ resource recovery). Closes on three cases where the keystone framing breaks down (short-duration mission, upset event surge, heavily regulated waste regime). Generalisation section walks residential homestead, remote research station with Madrid Protocol coverage, disaster relief, maritime vessel with MARPOL coverage, and forward operating base. MathJax enabled.
**Article Number**: A158
**Completion**: 100%
**Publication Sensibility**: High for the space-themed cluster (sixth per-subsystem article continues the deep-dive cadence under A152's nine-subsystem roadmap, while doubling as a general off-grid waste and sewage management guide for terrestrial use cases)
**Status**: Published 2026-07-04 (18 references; ~1,505 lines; mathjax true with 15 display equations and 21 inline expressions)

### Habitat and Physical Operations for Off-Grid Space Colonization Analogs — Published

**File**: `_posts/2026-07-03-habitat_and_physical_operations_for_off_grid_space_colonization_analogs.markdown`
**Topic**: Fifth per-subsystem deep-dive in the analog-facilities category following A152, A153, A154, A155, and A156. Treats the habitat layer under the framing that the habitable pressure envelope is the architectural keystone, with structural mass, airlock cycling, thermal boundary, radiation shielding, micrometeoroid shielding, and interface penetrations all dimensioned against the envelope. Derives habitable volume sizing, differential pressure across the envelope, cylindrical and spherical pressure vessel stress equations, required wall thickness with safety factor and worked example at 8.7 mm for a 4-metre radius aluminium habitat, structural mass equation, thermal heat loss equation with worked 3.2 kW for a Mars surface habitat, airlock gas loss with the corrected ISS Quest 4.2 m^3 crewlock and 0.4 to 1.4 kg per cycle figure, and radiation shielding attenuation. Walks dependent components in order of dependency covering pressure envelope material (rigid aluminium, inflatable BEAM and Sierra Space LIFE, 3D-printed ICON Vulcan and Olympus, subterranean, rammed-earth and regolith), interior layout with NASA HIDH per-crew volume guidance, airlocks and EVA staging including suit-port architecture, thermal control with corrected ISS 70 kW EATCS radiator capacity, radiation shielding with corrected Mars 230 mSv/year unshielded and lunar 380 to 500 mSv/year solar minimum dose figures, micrometeoroid and orbital debris Whipple shield, and interface penetrations. Covers no-pressure-envelope architectures (open-air shelter, underwater habitat, subterranean cave), terrestrial-only cheats (breathable atmosphere, natural radiation shielding, conventional building codes), space-only options (lunar lava tube habitats with Marius Hills and Mare Tranquillitatis pits, regolith burial including Mars Ice Home concept, orbital free-flying habitats including Lunar Gateway and commercial LEO destinations, inflatable surface habitats). Closes on three cases where the keystone framing breaks down (near-zero pressure differential terrestrial, external-pressure-dominated underwater, distributed-village multi-module). Generalisation section walks submarine, Antarctic winter-over, off-grid residential, disaster relief, maritime vessel, and forward operating base. MathJax enabled.
**Article Number**: A157
**Completion**: 100%
**Publication Sensibility**: High for the space-themed cluster (fifth per-subsystem article continues the deep-dive cadence under A152's nine-subsystem roadmap, while doubling as a general off-grid habitat construction and operations guide for terrestrial use cases)
**Status**: Published 2026-07-03 (25 references; ~1,568 lines; mathjax true with 21 display equations and 27 inline expressions)

### Food Production and Closed Ecological Systems for Off-Grid Space Colonization Analogs — Published

**File**: `_posts/2026-07-02-food_production_and_closed_ecological_systems_for_off_grid_space_colonization_analogs.markdown`
**Topic**: Fourth per-subsystem deep-dive in the analog-facilities category following A152, A153, A154, and A155, designed to function as a general off-grid food production guide with space-colonization as contextual flavour. Treats the food production layer under the framing that the caloric yield per square metre per day is the architectural keystone, with the cultivation area following from the daily caloric demand and the achievable yield, and the lighting power, water demand, carbon dioxide flux, nutrient supply, and harvest and storage capacity all dimensioned against the cultivation area. Derives cultivation area sizing from first principles with worked example at 120 m^2 for four crew at 3000 kcal/day on a wheat-and-soybean mix at 150 kcal per square metre per day yield. Walks the dependent components in order of dependency covering cultivation systems (soil, hydroponic, aeroponic, vertical controlled environment), lighting (natural sun, artificial LED, hybrid), climate control with CO2 enrichment, nutrient supply, harvest and storage, and waste recycling through composting, anaerobic digestion, and microbial bioreactor processing. Includes production strategies covering intensive staple horticulture, fresh produce cultivation, aquaculture and aquaponics, single-cell protein from Spirulina and Chlorella, and insect protein with feed conversion ratio comparison. Treats closed ecological system biology through BIOS-3, Biosphere 2 at approximately 80 percent caloric closure across 2000 m^2 cropping area, Yuegong-365 at approximately 80 percent food self-sufficiency, the MELiSSA C1 through C5 compartment architecture with C4a algal and C4b higher-plant split, and the NASA Controlled Ecological Life Support System Biomass Production Chamber at Kennedy Space Center. Includes no-production architectures (ISS-style shelf-stable ration import, hybrid partial production with NASA Veggie and Advanced Plant Habitat, short-duration), terrestrial-only cheats (grocery resupply, local farms, wild harvest), and space-only options (reduced Mars top-of-atmosphere flux further attenuated by atmospheric dust at the surface, lunar peaks of eternal light, lunar equatorial 14-day night, microgravity considerations through Veggie and APH, regolith and in-situ resources). Closes on three cases where the keystone framing breaks down (short-duration mission, crop failure contingency, crew dietary preference). Generalisation section walks residential homestead, remote research station, disaster relief, maritime vessel, and forward operating base. MathJax enabled.
**Article Number**: A156
**Completion**: 100%
**Publication Sensibility**: High for the space-themed cluster (fourth per-subsystem article continues the deep-dive cadence under A152's nine-subsystem roadmap, while doubling as a general off-grid food production guide for terrestrial use cases)
**Status**: Published 2026-07-02 (13 references; ~1,641 lines; mathjax true with 15 display equations and 19 inline expressions)

Fourth per-subsystem deep-dive article following A153, A154, and A155, treating the food production subsystem under the caloric-yield-as-keystone framing.

Sections covered include
opening as fourth subsystem deep-dive citing food as the longest-cycle closed-loop subsystem per A152;
generalisation framing to any off-grid food production system context;
The Caloric Yield Keystone (yield-demand mismatch, closure ratio applied symmetrically from water article);
Sizing From First Principles (cultivation area equation A_crop = N_crew × E_cal × σ / Y with worked example 120 m^2 for four-crew habitat at 3000 kcal/day at 150 kcal per square metre per day yield, daily light integral DLI = PPFD × t_photoperiod, lighting power equation P_light, water demand V_water_food = A_crop × ET_crop with 600 L/day worked example, closure ratio C_food = E_cal,produced / E_cal,consumed, makeup caloric demand equation, photosynthesis stoichiometric reaction 6 CO2 + 6 H2O to glucose plus 6 O2, mass balance equations for CO2 consumption and O2 production at 1.5 kg CO2 and 1 kg O2 per kg dry biomass);
Dependent Components in Order of Dependency (cultivation systems with hydroponic variants, lighting with photosynthetic efficiency η_photo = E_biomass / E_PAR ranging 0.5 to 3 percent field for higher plants with theoretical maxima 4.6 percent C3 and 6 percent C4 and 8 to 10 percent cyanobacteria, climate control with CO2 enrichment, nutrient supply, harvest and storage, waste recycling);
Production Strategies (intensive staple horticulture, fresh produce, aquaculture, single-cell protein, insect protein with feed conversion ratio equation);
Closed Ecological System Biology (BIOS-3 with substantial food closure varying by run, Biosphere 2 with 80 percent caloric closure, Yuegong-365 with 80 percent food self-sufficiency, MELiSSA C1-C5 architecture with C4a algal and C4b higher-plant split, NASA CELSS Biomass Production Chamber);
No-Production Architectures (shelf-stable ration, hybrid partial production, short-duration);
Terrestrial-Only Cheats (grocery resupply, local farm cooperation, wild harvest);
Space-Only Options (Mars top-of-atmosphere 43 percent reduction further attenuated by surface dust, lunar peaks of eternal light, lunar equatorial 14-day night, microgravity considerations, regolith and in-situ resources);
Where the Keystone Framing Breaks Down (short-duration mission, crop failure contingency, crew dietary preference);
Generalisation Beyond the Space Analog Context;
Out of Scope (crop physiology and breeding, soil chemistry and microbiology, aquaculture engineering, pest and pathogen management, food safety and nutrition, spaceflight crew nutrition research);
Conclusion.

Research agent verified
the NASA exploration crew caloric demand of 2000 to 3000 kcal per day with additional 500 kcal on EVA days per JSC-67378,
the wheat, potato, soybean, lettuce, Spirulina, Chlorella, and mealworm caloric densities and protein content,
the photosynthetically active radiation 400 to 700 nanometre wavelength range and the photosynthetic efficiency ranges including 0.5 to 3 percent for higher plants under field conditions with theoretical maxima 4.6 percent C3 and 6 percent C4 and 8 to 10 percent for cyanobacteria,
the daily light integral 12 to 17 mol/m^2/day for leafy greens and 20 to 30 mol/m^2/day for fruiting crops,
the LED grow light efficacy 2.5 to 3.5 micromoles per joule,
the Mars top-of-atmosphere solar flux at approximately 43 percent of Earth further attenuated by atmospheric dust at the surface,
the lunar solar constant at 1361 W/m^2 at 1 AU,
the Biosphere 2 Mission 1 80 percent caloric closure on 2000 m^2 cropping area across the 2-year 8-crew mission,
the BIOS-3 approximately 95 percent atmospheric closure with food closure varying by run,
the Yuegong-365 approximately 98 percent overall system closure with full water and oxygen recycling and approximately 80 percent food self-sufficiency,
the MELiSSA C1 anoxic thermophilic, C2 photoheterotrophic, C3 nitrifying, C4a photoautotrophic algal with Limnospira indica or Spirulina, C4b higher-plant, and C5 crew compartment architecture,
the NASA Veggie deployed April 2014 with crops including red romaine lettuce, zinnia, Mizuna, Russian kale, pak choi, dragoon lettuce, and tomato,
the NASA Advanced Plant Habitat deployed 2017 with Arabidopsis, dwarf wheat, and chile peppers in 2021,
the NASA Controlled Ecological Life Support System Biomass Production Chamber operated 1988 onward for over 1200 days at Kennedy Space Center,
the MELiSSA Pilot Plant inaugurated 4 June 2009 at UAB with the Claude Chipaux Laboratory active in 2025-2026,
the hydroponic, aeroponic, controlled environment agriculture, aquaponic, single-cell protein, and edible insect production strategies,
the USDA Organic 7 CFR Part 205, the FDA Food Code 2022 10th edition, and the FAO/WHO Codex Alimentarius,
and the CO2 enrichment 800 to 1200 ppm versus ambient 425 ppm with C3 yield uplift 40 to 100 percent and C4 yield uplift 10 to 25 percent.

Critical factual corrections applied include
the Biosphere 2 caloric closure corrected from 50 percent to approximately 80 percent across the 2000 square metre cropping area;
the Yuegong-365 food self-sufficiency clarified to 80 percent with the 98 percent figure framed as overall system closure including water and oxygen;
the BIOS-3 food closure softened from a specific 50-60 percent range to substantial food closure varying by run with the 95 percent atmospheric closure cited;
the MELiSSA C4 compartment split into C4a photoautotrophic algal (Limnospira indica or Spirulina) and C4b higher-plant per current ESA definitions;
the Mars solar irradiance qualifier clarified that the 43 percent figure is top-of-atmosphere with further attenuation by atmospheric dust at the surface;
the photosynthetic efficiency refined to 0.5 to 3 percent for higher plants under field conditions with theoretical maxima 4.6 percent C3 and 6 percent C4 and 8 to 10 percent only for cyanobacteria;
the LED efficacy range adjusted to 2.5 to 3.5 micromoles per joule (the upper end was already accurate);
URL replacements for the NASA Advanced Plant Habitat page (relocated to NASA Growing Plants in Space) and the NASA Veggie page (relocated to the Wikipedia Vegetable Production System article).

References:
12 references across Reference (9) and Related Post (4) categories.
All inline-linked per project style.
A152, A153, A154, and A155 cited via post_url as the parent and sibling articles.

### Communications and the Link Budget for Off-Grid Space Colonization Analogs — Published

**File**: `_posts/2026-07-01-communications_and_the_link_budget_for_off_grid_space_colonization_analogs.markdown`
**Topic**: Third per-subsystem deep-dive in the analog-facilities category following A152, A153, and A154, designed to function as a general off-grid communications system guide with space-colonization as contextual flavour. Treats the communications layer of the off-grid analog under the framing that the link budget is the architectural keystone, with antenna aperture, transmit power, modulation, forward error correction strength, and operating frequency all dimensioned against the required signal-to-noise margin. Derives the link budget from first principles with the Friis equation, free-space path loss, Shannon-Hartley capacity bound, parabolic antenna gain, beamwidth, Johnson-Nyquist thermal noise floor, Doppler shift, and link margin equations. Walks the dependent components in order of dependency covering antennas, transmitters and power amplifiers, receivers and low-noise amplifiers, modems and forward error correction, networking layer with IEEE 802.3 and 802.11 references, and power supply and cooling. Includes a latency, bandwidth, and protocol considerations section with delay-tolerant networking and bundle protocol. Includes no-radio-frequency architectures covering free-space optical and physical data transport (sneakernet). Includes terrestrial-only cheats and space-only options covering NASA Deep Space Network, ESA Estrack, Mars Relay Network (updated after MAVEN mission conclusion June 2026), lunar relay constellation through LunaNet and ESA Moonlight, and deep-space optical communications. Closes on three cases where the keystone framing breaks down covering solar conjunction blackout (with January 2026 most recent and early 2028 next), entry-descent-landing plasma sheath, and deep outer solar system extreme-distance regime. Includes generalisation beyond space analog covering residential cabin, remote research station, disaster relief, maritime vessel, and forward operating base use cases. MathJax enabled.
**Article Number**: A155
**Completion**: 100%
**Publication Sensibility**: High for the space-themed cluster (third per-subsystem article continues the deep-dive cadence under A152's nine-subsystem roadmap, while doubling as a general off-grid communications system guide for terrestrial use cases)
**Status**: Published 2026-07-01 (28 references; ~1,544 lines; mathjax true with 16 display equations and 27 inline expressions)

Third per-subsystem deep-dive article following A153 and A154, treating the communications subsystem of the off-grid analog under the link-budget-as-keystone framing.
Sections covered include
opening as third subsystem deep-dive identifying communications as the umbilical that connects the operational island to surrounding institutional context;
generalisation framing to any off-grid communications system context;
The Link Budget Keystone (closure problem analogous to electrical generation-load and water supply-demand mismatch);
Link Budget From First Principles (Friis equation in linear and dB form, free-space path loss with the 32.45 constant for km and MHz, parabolic antenna gain, beamwidth, Johnson-Nyquist thermal noise, Shannon-Hartley capacity bound, link margin definition, worked example for 12 GHz Ku-band geostationary uplink yielding 11 dB margin);
Dependent Components in Order of Dependency (antennas including parabolic, omnidirectional, phased array, horn; transmitters and power amplifiers with 10 to 40 percent solid-state efficiency; receivers and low-noise amplifiers with 0.8 to 1.5 dB noise figure; modems and forward error correction with BPSK at 9 dB through higher-order QAM, LDPC and turbo codes; networking layer under IEEE 802.3 Ethernet and IEEE 802.11 wireless including 802.11s mesh; power supply and cooling);
Latency, Bandwidth, and Protocol Considerations (Mars 3 to 22 minute and lunar 1.3 second light-time delay, TCP degradation under multi-minute delay, Delay-Tolerant Networking and Bundle Protocol substitution, Mars relay UHF data rates, direct-to-Earth X-band, DSOC optical demonstrator);
No-Radio-Frequency Architectures (free-space optical with terrestrial 1 to 10 Gbps over 1 km, NASA LCRD geostationary optical relay, physical data transport sneakernet);
Terrestrial-Only Cheats (broadband Internet, cellular, low Earth orbit constellations including Starlink, OneWeb, and Iridium);
Space-Only Options (NASA Deep Space Network at Goldstone, Madrid, Canberra with 70-metre and 34-metre antennas, ESA Estrack at New Norcia, Cebreros, Malarguee, Mars Relay Network with MRO, Mars Odyssey, Mars Express, ExoMars Trace Gas Orbiter after MAVEN mission conclusion June 2026, lunar relay through LunaNet and ESA Moonlight, deep-space optical communications including DSOC primary mission concluded September 2025);
Where the Keystone Framing Breaks Down (solar conjunction blackout with X-band 5 degree and Ka-band 2 to 3 degree thresholds, most recent January 2026 with next early 2028; entry-descent-landing plasma sheath; deep outer solar system Voyager regime at 160 bps from 24 billion km);
Generalisation Beyond the Space Analog Context (residential off-grid cabin, remote research station with Antarctic Starlink shift since 2022, disaster relief, maritime vessel with antenna gimbal compensation, military forward operating base);
Out of Scope (modulation and coding theory, network protocols and security, antenna engineering and EMC, spectrum allocation and regulatory compliance, quantum communications, software-defined radio architecture);
Conclusion.

Research agent verified
the Friis equation linear and dB forms,
the free-space path loss 32.45 constant for km and MHz,
the Shannon-Hartley capacity bound,
the parabolic antenna gain with aperture efficiency 0.55 to 0.70 for well-designed dishes,
the parabolic 3 dB beamwidth approximately 70 lambda over D in degrees,
the Johnson-Nyquist thermal noise N = k T B with Boltzmann constant 1.380649 times 10 to the minus 23 J/K,
the Doppler shift Delta f over f = v over c non-relativistic limit,
the NASA Deep Space Network three sites at Goldstone, Madrid, and Canberra with one 70-metre and multiple 34-metre antennas each with Madrid adding DSS-53 February 2022,
the ESA Estrack network with three deep-space 35-metre antennas and the upcoming DSA-4 at New Norcia inaugurated October 2025,
the Mars Relay Network active orbiters MRO, Mars Odyssey, Mars Express, and ExoMars Trace Gas Orbiter after MAVEN mission conclusion 3 June 2026,
the NASA Laser Communications Relay Demonstration launch 7 December 2021 with 1.244 Gbps capability and first ILLUMA-T link 5 December 2023,
the Psyche DSOC launch 13 October 2023 with first light 14 November 2023, 267 Mbps from 16 million km in December 2023, distance record from 494 million km on 3 December 2024, primary mission concluded 2 September 2025 with possible 2026 reactivation,
the Starlink 2026 figures of approximately 10,000 active satellites with 25 to 50 ms latency and 100 to 400 Mbps download,
the Iridium 66 active satellites in 6 polar planes with Iridium NEXT completed January 2019,
the Globalstar 25 second-generation satellites with announced 54-satellite expansion and Amazon acquisition agreement April 2026,
the TDRSS three generations with planned phaseout in favour of commercial relay providers,
the HF radio 3 to 30 MHz ionospheric skywave,
the VHF 30 to 300 MHz and UHF 300 MHz to 3 GHz ITU allocations,
the IEEE 802.11s mesh and the Meshtastic-style overlays on LoRa rather than LoRa itself as mesh,
the FCC Part 95 personal radio services covering FRS, GMRS, MURS, and CB,
the CCSDS Space Packet Protocol, CFDP, Proximity-1, and Space Link Extension standards,
the IEEE 802.11ax Wi-Fi 6 published February 2021, 802.11ax 6 GHz extension Wi-Fi 6E, and 802.11be Wi-Fi 7 published September 2024,
the ITU-R Radio Regulations 2024 edition entered force 1 January 2025 after WRC-23,
the CCSDS FEC codes including concatenated convolutional plus Reed-Solomon, turbo, LDPC AR4JA family, and BCH plus LDPC via DVB-S2 with polar codes used in 5G but not in current CCSDS standard suites,
the terrestrial free-space optical 500 m typical year-round availability with multi-kilometre under favourable weather,
and the Mars solar conjunction January 2026 most recent with next opposition February 2027 and next superior conjunction approximately early 2028.

Critical factual corrections applied:
MAVEN removed from active Mars relay list with the mission conclusion announced 3 June 2026 explicitly noted;
the DSOC primary mission framed as concluded September 2025 with the November 2023 first link at 267 Mbps from 16 million km, the December 2024 distance record from 494 million km, and the possible reactivation under consideration following the May 2026 Mars flyby;
the solar conjunction blackout specification expanded with X-band Sun-Earth-Probe angle below approximately five degrees and Ka-band below approximately two to three degrees;
the Mars solar conjunction schedule corrected with the most recent January 2026 and next early 2028 rather than late 2026 to early 2027;
the polar codes removed from CCSDS-standard list with LDPC and concatenated turbo codes substituted;
URL replacements for the NASA Deep Space Network page (relocated to Wikipedia), the LCRD page (Wikipedia), the LunaNet page (Wikipedia), the FCC root (Wikipedia), and the Space Telecommunications Radio System (Software-Defined Radio Wikipedia) along with the IETF RFC 9171 page for the Bundle Protocol.

References:
28 references across Reference (25) and Related Post (3) categories.
All inline-linked per project style.
A152, A153, and A154 cited via post_url as the parent and sibling articles.

### Water Systems and Life Support Recovery for Off-Grid Space Colonization Analogs — Published

**File**: `_posts/2026-06-30-water_systems_and_life_support_recovery_for_off_grid_space_colonization_analogs.markdown`
**Topic**: Second per-subsystem deep-dive in the analog-facilities category following A152 and A153, designed to function as a general off-grid water system guide with space-colonization as contextual flavour. Treats the water layer of the off-grid analog under the dual-keystone framing that the storage tank is the architectural keystone for any off-grid water system and the recovery loop is the closed-system extension that determines long-duration sustainability. Derives storage sizing from first principles with worked examples at 8400 L (terrestrial) and 250 to 420 L (spaceflight regime) scales. Walks the dependent components in order of dependency covering water sources (rainwater harvesting, well extraction, atmospheric water generation, closed-loop recovery), treatment train (sedimentation, filtration, disinfection, polishing), storage materials and geometry, distribution network with hydrostatic pressure and pump power equations, and heating and pressure management. Includes a recovery loop and closure ratio section with worked makeup water demand calculation across mission durations. Includes a treatment technologies in detail section covering reverse osmosis with flux equation, distillation with thermodynamic minimum and multi-stage architectures, ultraviolet disinfection with Chick-Watson kinetics and adenovirus virus caveat, chemical disinfection, activated carbon, and ion exchange. Includes no-recovery architectures section, terrestrial-only cheats section, and space-only options covering lunar polar water ice via LCROSS, Mars subsurface ice via SHARAD, Mars atmospheric water vapor via WAVAR concept, and asteroid and comet volatiles. Closes on three cases where the keystone framing breaks down (sub-day mission duration, trace-water outer solar system, in-situ resource abundance regime). Includes generalisation beyond space analog covering residential cabin, remote research station, disaster relief, maritime vessel, and forward operating base use cases. MathJax enabled.
**Article Number**: A154
**Completion**: 100%
**Publication Sensibility**: High for the space-themed cluster (second per-subsystem article continues the deep-dive cadence under A152's nine-subsystem roadmap, while doubling as a general off-grid water system guide for terrestrial use cases)
**Status**: Published 2026-06-30 (15 references; ~1,690 lines; mathjax true with 11 display equations and 36 inline expressions)

Second per-subsystem deep-dive article following A153, treating the water subsystem of the off-grid analog under the dual-keystone framing where the storage tank is the primary architectural keystone analogous to the battery bank in A153 and the recovery loop is the closed-system extension that determines long-duration sustainability.
Sections covered include
opening as second subsystem deep-dive citing water as the highest-leverage subsystem per A152;
generalisation framing to any off-grid water system context;
The Storage and Recovery Keystone (supply-demand mismatch and closed-system architecture);
Storage Sizing From First Principles (V_storage equation, two worked examples at 8400 L terrestrial and 250 to 420 L spaceflight scales, daily demand decomposition by stream, closure ratio C and makeup water demand equation, makeup water worked example at 95 percent versus zero percent closure);
Dependent Components in Order of Dependency (water sources including rainwater harvesting with the corrected 1.0 L/m2/mm gross conversion and 0.8 to 0.9 effective after runoff coefficient, well extraction with pump power equation, atmospheric water generation, recovery; treatment train through sedimentation, filtration, disinfection with Chick-Watson kinetics, polishing under NSF Standard 61, 53, EPA SDWA, WHO Guidelines; storage materials and geometry; distribution network with hydrostatic pressure equation; heating and pressure management);
The Recovery Loop and Closure Ratio (greywater, blackwater with jurisdiction-dependent kitchen sink classification, atmospheric humidity, urine stream with ISS UPA vapor compression distillation and BPA);
Treatment Technologies in Detail (reverse osmosis with flux equation and corrected energy ranges, distillation with thermodynamic minimum 0.63 kWh/L latent heat and corrected multi-stage values, ultraviolet disinfection with adenovirus caveat, chemical disinfection, activated carbon, ion exchange);
No-Recovery Architectures (single-pass, continuous resupply, hybrid partial recovery);
Terrestrial-Only Cheats (municipal connection, trucked-in delivery, cogeneration);
Space-Only Options (lunar polar water ice via LCROSS October 2009 with Lunar Reconnaissance Orbiter follow-up, Mars subsurface ice via SHARAD with Phoenix lander 2008 confirmation, Mars atmospheric water vapor via WAVAR sorbent regeneration concept from Bruckner at University of Washington, asteroid and comet volatiles);
Where the Keystone Framing Breaks Down (sub-day mission, trace-water outer solar system, in-situ resource abundance);
Generalisation Beyond the Space Analog Context (residential cabin, remote research station, disaster relief, maritime vessel, forward operating base);
Out of Scope (treatment-train engineering, bioregenerative life support biology, pharmaceutical residues, trace organic contaminants, microbial control in distribution, in-situ resource utilisation engineering);
Conclusion.

Research agent verified
the ISS Water Recovery System 98 percent closure after Brine Processor Assembly addition with the 20 June 2023 milestone date,
the ISS Urine Processor Assembly 75 to 87 percent urine water recovery via rotating vapor compression distillation,
the NASA JSC-63414 SWEGs Revision A November 2023 potable water standard,
the Biosphere 2 Mission One water cycle through condensation collection and constructed wetlands,
the BIOS-3 ten crewed closures from 1972 with 180-day longest run and 85 percent water recycling,
the MELiSSA Pilot Plant at the Universitat Autonoma de Barcelona Claude Chipaux Laboratory with five compartments C1 through C5 active in 2025-2026,
the Yuegong-365 mission 10 May 2017 to 15 May 2018 with 98.2 percent overall system closure,
the rainwater harvesting conversion factor 1.0 L per square metre per millimetre gross with 0.8 to 0.9 effective after runoff coefficient,
the atmospheric water generator specific energy 0.25 to 0.5 kWh per litre at moderate humidity,
the kitchen sink jurisdiction-dependent classification with California and Hawaii treating as blackwater versus IPC and UPC excluding from greywater,
the reverse osmosis energy 2.5 to 4 kWh per cubic metre seawater and 0.5 to 1.5 kWh per cubic metre brackish,
the ultraviolet 30 to 40 mJ/cm2 dose for 4-log bacteria and protozoa with adenovirus requiring greater than 100 mJ/cm2,
the ultrafiltration 0.01 to 0.1 micrometre pore size and 0.1 to 0.5 kWh per cubic metre energy,
the distillation thermodynamic minimum 0.63 kWh per litre latent heat with practical small stills at 1 to 2 kWh per litre and multi-stage flash at 18 to 28 kWh per cubic metre,
the NSF/ANSI 61-2025, NSF/ANSI 53-2023, and NSF/ANSI 55-2024 current revisions,
the EPA Safe Drinking Water Act 40 CFR Part 141 National Primary Drinking Water Regulations,
the WHO Guidelines for Drinking-Water Quality fourth edition with third addendum 18 June 2026,
the ASHRAE Standard 188-2021 Legionellosis Risk Management,
the 2024 International Plumbing Code current edition,
the LCROSS impactor mission 9 October 2009 confirming water ice in Cabeus crater,
the Mars Reconnaissance Orbiter SHARAD radar instrument mapping mid-latitude buried ice including Utopia Planitia and Deuteronilus Mensae,
the Phoenix lander 2008 direct observation of subsurface ice,
the WAVAR concept from Adam Bruckner at the University of Washington for Type 3A zeolite molecular sieve cycled adsorption from Martian wind-driven airflow,
and the Mars atmosphere approximately 0.03 percent water vapor average by volume with significant seasonal variation.

Critical factual corrections applied:
the rainwater conversion corrected from 0.9 L/m2/mm to 1.0 L/m2/mm gross with 0.8 to 0.9 effective after runoff coefficient;
the ISS daily water use refined from 4 to 6 L/crew/day to 3 to 5 L/crew/day for drinking and food preparation;
the single-stage distillation energy corrected from 2 to 4 kWh per litre to the thermodynamic minimum 0.63 kWh per litre latent heat with practical small stills at 1 to 2 kWh per litre;
the multi-stage distillation energy refined to 18 to 28 kWh per cubic metre for multi-stage flash and 4 to 7 kWh thermal plus 1.5 to 2 kWh electrical per cubic metre for multi-effect distillation;
the WHO Guidelines for Drinking-Water Quality updated to fourth edition incorporating first, second, and third addenda through June 2026;
the kitchen sink classification softened with jurisdiction-dependent qualifier covering California, Hawaii blackwater treatment versus IPC and UPC exclusion from greywater;
the ultraviolet dose specification expanded with the adenovirus 100 mJ/cm2 caveat for virus inactivation;
the SHARAD acronym spelled out as Shallow Radar on first use.

References:
15 references across Reference (13) and Related Post (2) categories.
All inline-linked per project style.
A152 (Simulating Space Colonization on Earth Using Off-Grid Facilities) and A153 (Electricity and Energy Storage for Off-Grid Space Colonization Analogs) cited via post_url as the parent and sibling articles.

### Electricity and Energy Storage for Off-Grid Space Colonization Analogs — Published

**File**: `_posts/2026-06-29-electricity_and_energy_storage_for_off_grid_space_colonization_analogs.markdown`
**Topic**: First per-subsystem deep-dive in the analog-facilities category following A152, designed to function as a general off-grid electrical-system guide with space-colonization as contextual flavour. Treats the electricity layer of the off-grid analog under the framing that battery storage is the architectural keystone, with every dependent component dimensioned against the battery bank. Derives battery sizing from first principles with worked examples and the round-trip efficiency cascade. Walks the dependent components in order of dependency covering generation capacity with photovoltaic temperature derating, charge controllers, inverters and power conditioning, generator backup with the fuel consumption equation, load shedding strategy, and conductor sizing with the voltage drop equation. Includes a no-battery alternatives section covering continuous baseload fission through Kilopower and Fission Surface Power, geothermal, thermal storage, mechanical storage, and hydrogen production. Includes a terrestrial-only cheats section enumerating grid-tied operation, trucked-in diesel resupply, and cogeneration. Includes a space-only options section covering lunar peaks of eternal light, Mars solar at reduced irradiance, space-based solar power, orbital reflectors and the Znamya experiments, and the statite architecture. Includes a generalisation-beyond-space-analog section covering off-grid cabin, remote research station, disaster relief, maritime vessel, and forward operating base use cases. Closes on three cases where the keystone framing breaks down covering the lunar equatorial fourteen-day night, the Mars dust storm season, and the outer-planet solar weakness. MathJax enabled with ten display equations and twenty inline expressions.
**Article Number**: A153
**Completion**: 100%
**Publication Sensibility**: High for the space-themed cluster (first per-subsystem article opens the deep-dive cadence under A152's nine-subsystem roadmap, while doubling as a general off-grid electrical-system guide for terrestrial use cases)
**Status**: Published 2026-06-29 (16 references; ~1,508 lines; mathjax true with 10 display equations and 20 inline expressions)

First per-subsystem deep-dive article following A152, treating the electricity subsystem of the off-grid analog under the battery-as-keystone framing.
Sections covered include
opening as deep-dive of the highest-leverage subsystem;
The Battery Storage Keystone (decoupling intermittent generation from continuous load, three failure modes for the no-storage architecture);
Battery Sizing From First Principles (E_usable equation, E_nameplate equation with depth of discharge and round-trip efficiency factors, two worked examples at 33 kWh and 1300 kWh scales, chemistry comparison covering LiFePO4, NMC, lead-acid, and vanadium redox flow);
Dependent Components in Order of Dependency (generation capacity with A_PV equation and worked example, charge controllers under NEC 690 and IEC 62548, inverters under UL 1741, generator backup with propane consumption worked example, load shedding strategy with three-tier prioritisation);
No-Battery Architectures (Kilopower KRUSTY with the corrected 28-hour 1 kWe design point demonstration, Fission Surface Power 100 kW class target after August 2025 acceleration, geothermal, thermal storage, mechanical storage, hydrogen production);
Terrestrial-Only Cheats (grid-tied operation, trucked-in fuel resupply, cogeneration with adjacent facility);
Space-Only Options (lunar peaks of eternal light with Shackleton rim Points A and B at 81 and 82 percent illumination and 94 percent maximum, Mars solar at 43 percent of Earth irradiance with InSight dust failure precedent, Space-Based Solar Power with Caltech MAPLE 2023 demonstrator and ESA Solaris programme, orbital reflectors with the Znamya experiments, statite architecture from McInnes 1989 and Forward 1993);
Where the Keystone Framing Breaks Down (lunar equatorial 14-day night, Mars dust storm season, outer-planet solar weakness);
Out of Scope (battery management system engineering, power-electronics circuit design, grid-forming and islanding behaviour, nuclear safety and licensing, space-based solar power economics, energy storage chemistry research);
Conclusion.

Research agent verified
the ISS battery replacement campaign (Ni-H2 to Li-ion, 2017 to 2021, 48 to 24 unit consolidation),
the lithium iron phosphate cycle life and energy density ranges,
the lead-acid and vanadium redox flow battery ranges,
the photovoltaic efficiency ranges across mono- and multi-crystalline silicon, thin film, and triple-junction tandem cells,
the Mars and lunar solar irradiance values,
the McMurdo Ross Island Wind Energy Project specifications,
the Kilopower KRUSTY 28-hour full-power test on 20 March 2018 with 5.5 kW thermal yielding 1 kW electric design point,
the Fission Surface Power programme acceleration to 100 kW class in August 2025,
the MMRTG 125 W beginning of life electrical output from approximately 2 kW thermal,
the Plutonium-238 production restart in 2013 with the 1.5 kg per year target slipped to 2026,
the Peter Glaser 1968 Science paper with the 1973 patent,
the Caltech SSPP MAPLE demonstrator January 2023 launch with June 2023 ground reception below 0.1 microwatt as proof of concept,
the ESA Solaris programme November 2022 Ministerial Council approval with the 2025 full programme decision,
the JAXA mid-2030s commercial SSPS target rather than 2050,
the China space solar power station 2028 LEO demonstrator and 2050 commercial GEO target,
the Znamya 2 February 1993 deployment and Znamya 2.5 February 1999 failure,
the Forward and McInnes statite concept dates (McInnes 1989, Forward 1993),
the Krafft Ehricke Soletta 1978 concept with the Lunetta variant,
the Peaks of Eternal Light at Shackleton crater rim Points A and B with 81 and 82 percent illumination,
the NEC Article 690 and Article 706 photovoltaic and energy storage system coverage,
and the UL 1741 distributed energy resource inverter standard.

Critical factual corrections applied:
the Kilopower KRUSTY description corrected from "1 kW electric output" to "1 kW electric design point demonstrated through 28-hour full-power test producing 5.5 kW thermal";
the Fission Surface Power 40 kW target updated to 100 kW class after the August 2025 NASA acceleration;
the statite attribution corrected from Forward 1991 to McInnes 1989 and Forward 1993;
the Soletta concept date refined from "the 1970s" to "1978" with the Lunetta variant added;
the Caltech MAPLE ground reception detail added that detected power was below one tenth of a microwatt as proof of concept;
the Space-Based Solar Power efficiency caveat expanded to acknowledge theoretical 45 percent ceilings under optimised components;
the IX team description expanded to identify Intuitive Machines and X-energy;
the JAXA acronym spelled out as Japan Aerospace Exploration Agency on first use;
the Peak of Eternal Light section expanded with specific Shackleton Point A and Point B illumination figures and 94 percent maximum;
URL corrections for the NASA Fission Surface Power page (relocated to Wikipedia), the NASA Artemis Base Camp page (replaced with the Peak of Eternal Light Wikipedia article), the Caltech MAPLE landing page (replaced with the Caltech mission-end press release), and the UL 1741 services URL (replaced with the UL Standards Shop product detail page).

References:
14 references across Reference (13) and Related Post (1) categories.
All inline-linked per project style.
A152 (Simulating Space Colonization on Earth Using Off-Grid Facilities) cited via post_url as the parent survey article.

### Simulating Space Colonization on Earth Using Off-Grid Facilities — Published

**File**: `_posts/2026-06-28-simulating_space_colonization_on_earth_using_off_grid_facilities.markdown`
**Topic**: Survey introduction to the off-grid terrestrial analog for space colonization, framed as an iteration engine for the actual space mission. Treats the analog as a problem in its own right rather than a recreational exercise. Establishes a simulation honesty model on four axes (closure, isolation, duration, environmental fidelity), with closure formalised as a quantitative ratio. Surveys the major prior attempts grouped by category (Antarctic stations, closed ecological system experiments, Mars surface analogs, underwater analogs, buoyant and atmospheric platform analogs covering Landis Venus cloudtop and HAVOC), presents a comparison matrix, and walks through site selection criteria with United States and international site catalogues. Defines a nine-subsystem facility stack (electricity and energy storage, electronic operations and computing, communications, food production, potable water, sewage and human waste, physical operations and habitat, garbage and waste disposal, transportation and roads), with light-time delay and Mars synodic period quantified. Introduces the bootstrap and expansion regime distinction with the synodic resupply cadence. Opens the analog-facilities category for subsequent per-subsystem and per-topic articles. Cross-links A82-derived space studies cluster. MathJax enabled.
**Article Number**: A152
**Completion**: 100%
**Publication Sensibility**: High for the space-themed cluster (opens a problem space that subsequent articles can treat in depth)
**Status**: Published 2026-06-28 (57 references; ~2,047 lines; mathjax true)

Survey-style aerospace and engineering article on terrestrial off-grid analog facilities for space colonization simulation.
Sections covered include
opening framing as iteration engine for the real mission;
The Simulation Honesty Problem (closure, isolation, duration, environmental fidelity axes, with closure formalised as C = 1 minus m_ext over m_tot and worked examples for ISS WRS at C ~ 0.98 and Biosphere 2 food at C ~ 0.5);
Survey of Prior Attempts grouped by category covering Antarctic stations (McMurdo, Amundsen-Scott, Concordia), closed ecological system experiments (BIOS-3, Biosphere 2, Yuegong-1, MELiSSA), Mars surface analogs (MDRS, FMARS, HI-SEAS, HERA, CHAPEA, Mars-500), underwater analogs (NEEMO at Aquarius), and buoyant and atmospheric platform analogs (Landis Venus cloudtop and HAVOC framing with density ratio derivation, plus the World View, Loon, and Sceye stratospheric platforms identified as the closest available terrestrial proxies);
Comparison matrix of thirteen prior attempts on site, operator, longest crewed run, closure score, isolation score, and operating year span;
Site Selection (five criteria) with United States catalogue (Mojave, Great Basin, Sonoran, Mauna Loa/Kea, Brooks Range) and international catalogue (Atacama, Devon Island, Pilbara, Iceland and Lanzarote PANGAEA, Antarctic continent, Tibetan Plateau, Pamirs);
The Facility-System Stack (nine subsystems: electricity and energy storage, electronic operations and computing, communications with light-time delay quantified by tau = d/c yielding 3 to 22 minutes for Mars and 1.3 seconds for the Moon, food production, potable water, sewage and human waste, physical operations and habitat, garbage and waste disposal, transportation and roads);
Bootstrap and Expansion (the operational-regime distinction with the Mars synodic period ~780 days fixing the resupply cadence);
Out of Scope (per-subsystem engineering, crew behaviour, closed ecological system biology, pressure suit and EVA, radiation, reduced gravity, programme cost, regulatory and treaty, governance of the simulated colony);
Conclusion.

Research agent verified
the Biosphere 2 mission dates (September 1991 to September 1993, March to September 1994) and the management transfer chain (Columbia 1995 to 2003, University of Arizona 2007 research and 2011 ownership),
the MDRS opening year (2001) and Mars Society operation,
the FMARS inauguration July 2000,
the HI-SEAS operator transfer to International MoonBase Alliance in 2018 with HI-SEAS IV running 366 days in 2015 and 2016,
the HERA 45-day mission length and JSC location,
the CHAPEA Mission 1 dates (June 2023 to July 2024, 378 days) with ICON-printed Mars Dune Alpha habitat,
the Concordia operator as IPEV and PNRA with ESA as scientific participant,
the Mars-500 dates (June 2010 to November 2011) and IBMP Moscow,
the BIOS-3 construction begun 1965 and operational from 1972,
the Yuegong-365 mission (May 2017 to May 2018, 370 days),
the McMurdo establishment date and population variation,
the Amundsen-Scott winter-over population around 40 to 50,
the Aquarius depth (~18 metres), FIU ownership transition (2013 operational, 2014 full), and NEEMO 23 in 2019 as last mission,
the MELiSSA initiation in 1989 with the Pilot Plant at UAB,
the PANGAEA training sites (Lanzarote, Dolomites, Ries Crater),
the Iceland Apollo training dates (1965, 1967) with Artemis II training in 2024,
the ISS Water Recovery System 98 percent recovery via Brine Processor Assembly addition,
and the McMurdo Ross Island Wind Energy Project with three Enercon E33 turbines.

Critical factual corrections applied:
the BIOS-3 dates clarified to construction begun 1965 and operational from 1972;
the Biosphere 2 management chain corrected to Columbia 1995 to 2003, U Arizona research 2007 and full ownership 2011;
the HI-SEAS operator corrected to International MoonBase Alliance since 2018;
the Aquarius depth corrected from approximately 20 metres to approximately 18 metres (60 feet);
the FIU ownership transition split into 2013 operational and 2014 full ownership;
the NEEMO last announced mission corrected to 2019 from 2017;
the ISS Water Recovery System characterised by Brine Processor Assembly addition rather than UPA upgrade;
the PANGAEA training site catalogue expanded to Lanzarote, Dolomites, and Ries Crater with Iceland repositioned as Apollo and Artemis training rather than PANGAEA;
URL replacements for NASA pages reorganised after 2024, the NSF United States Antarctic Program URL migrated to usap.gov, and the Wikipedia URL for Aquarius and Institute of Biophysics articles using current canonical paths.

References:
57 references across Reference (55) and Related Post (2) categories.
All inline-linked per project style.
A90 (introduction to space studies) and A92 (cryptotelemeritocracy for space exploitation) cited via post_url as the prior space-themed cluster articles.
Venus cloudtop subsection cites the Landis 2003 Colonization of Venus paper via NTRS, the NASA Langley High Altitude Venus Operational Concept via Wikipedia, and the World View Stratollite, Loon, and Sceye stratospheric platform programmes as terrestrial proxies.

### Maintenance and Lifecycle Management for SAR Drone Programs — Published

**File**: `_posts/2026-05-21-maintenance_and_lifecycle_management_for_search_and_rescue_drone_programs.markdown`
**Topic**: Seventh and final article in the SAR drone series after A145 (physics), A146 (buyer's framework), A147 (R&D), A148 (geographic setting), A149 (operator training), and A150 (sensor and payload selection with embedded data management). Series terminus. Treats the maintenance and lifecycle management as the second principal cost driver after the operator training programme. Five-layer maintenance stack covering airframe, battery lifecycle, payload calibration, firmware and software, and ground support equipment. Pre-flight and post-flight inspection, scheduled periodic maintenance, mishap repair. Battery cycle counting, state of health monitoring, storage protocols, transport regulations (UN 38.3, IATA DGR, 49 CFR Part 173), disposal and recycling. Payload calibration covering thermal radiometric, lidar boresight, multispectral spectral, gimbal alignment. Firmware and software lifecycle including vendor update cadence and ground station OS lifecycle. Spare parts strategy. Five-year total cost of ownership scorecard table by programme tier with maintenance fraction. End-of-life disposition covering lithium battery recycling, e-waste, and ITAR-controlled sensor disposition. Series synthesis closing the seven-article series.
**Article Number**: A151
**Completion**: 100%
**Publication Sensibility**: High for the buyer audience (closes the series with the operating-cost picture)
**Status**: Published 2026-05-21 (25 references; 3,022 lines)

Standalone aerospace and engineering analytical article on maintenance and lifecycle management for SAR drone programmes.
Sections covered include
opening as series terminus;
Why Maintenance Drives the Multi-Year Cost (consumables, scheduled service, unscheduled service);
The Maintenance Stack Taxonomy (five-layer scorecard table);
Airframe Maintenance (pre-flight and post-flight inspection per Part 107.49, scheduled periodic maintenance with three categories, mishap and field-failure repair with 5 to 10 percent of platform cost per year baseline);
Battery Lifecycle Management (cycle counting against 200 to 500 cycle thresholds, state of health monitoring with 80 percent capacity retirement criterion, storage protocols at 40 to 60 percent state of charge, transport under UN 38.3 and IATA DGR and 49 CFR Part 173, disposal through Call2Recycle and dedicated industrial recyclers);
Payload Maintenance and Calibration (thermal radiometric annual at USD 500 to USD 2000 per cycle, lidar boresight after assembly or major repair, multispectral via reference panels, gimbal mechanical alignment);
Firmware and Software Lifecycle (vendor update cadence with DJI and Skydio security trust centers, ground station OS lifecycle with Windows 10 EOL October 2025);
Spare Parts Strategy (critical spare inventory ratios, vendor parts catalogues, cannibalisation for legacy fleets);
Total Cost of Ownership (five-year scorecard table mapping to A146 tiers with 15 to 25 percent maintenance fraction);
End-of-Life Disposition (lithium battery recycling, airframe and avionics e-waste, ITAR-controlled sensor disposition through DDTC);
A Worked SAR Drone Programme Walk-Through (seven-step walk-through of a constructed Tier 2 mid-sized regional county SAR programme through the buyer's framework, geographic filter, platform selection, sensor selection with data management, operator training, maintenance programme, and integrated operating cycle);
Series Synthesis (seven-domain decision space recapitulation, entry-point matrix mapping reader question to starting article, sequential reading roadmap by reader role covering programme manager, operator pool builder, IT and compliance officer, and R&D lead);
Out of Scope (operator maintenance training, airworthiness certification for non-Part 107 platforms, cybersecurity incident response, maritime SAR specific maintenance, international logistics, plus a Topics Deferred at the Series Terminus subsection enumerating nine deferred topics that the series did not draft including lease versus buy financial analysis, insurance and underwriter requirements, detection algorithm ecosystem, vendor consolidation and supply chain risk, operator labour and human resources strategy, legal and regulatory counsel relationship, inter-agency coordination, multi-platform mixed-fleet management, and metrics and outcomes measurement);
Conclusion (series terminus).

Research agent verified
the DJI Care Enterprise and DJI Maintenance Program tier structures,
the DJI Intelligent Flight Battery cycle definition where one cycle equals 75 percent of rated capacity consumed,
the Skydio Care Enterprise availability for X10 with the explicit exclusion of X10D Blue UAS variant,
the WingtraCARE and Total Maintenance Plan service tiers,
the UN 38.3 Revision 8 with Amendment 1,
the IATA Dangerous Goods Regulations 67th Edition effective 1 January 2026 with the new 30 percent state of charge limit for UN 3480 and UN 3481 shipments,
the 49 CFR 173.185 lithium cells and batteries regulation,
the PHMSA Lithium Battery Guide for Shippers,
the IEC 62133-2 portable sealed secondary lithium cell safety standard,
the ANSI National Accreditation Board and A2LA accreditation pathway,
the FAA Part 107.49 preflight inspection requirement,
the FAA Public Aircraft Operations guidance through AC 00-1.1B,
the FAA AC 107-2A current revision,
the ASTM F2909 Continued Airworthiness specification,
the 14 CFR Part 43 applicability limitation to Category 4 operations,
the Call2Recycle network with the explicit damaged battery limitation,
and
the Microsoft Windows 10 end of standard support on 14 October 2025 with ESU through 13 October 2026.

Critical factual corrections applied:
the "DJI Enterprise Care" naming corrected to "DJI Care Enterprise";
the DJI Intelligent Flight Battery cycle definition clarified to 75 percent of rated capacity consumed rather than full discharge;
the IATA DGR 67th Edition January 2026 30 percent state of charge limit added for lithium battery shipment;
the Call2Recycle limitation clarified that the network does not accept damaged, swollen, leaking, or recalled batteries with the local hazardous waste facility cited as the disposal pathway for the crashed platform battery;
the NIST traceability framed as industry best practice rather than NIST mandate;
the ANSI National Accreditation Board and A2LA cited as the accreditation pathway for ISO IEC 17025 calibration laboratories;
the Microsoft Windows 10 EOL date specified as 14 October 2025 with the ESU programme available through 13 October 2026;
URL corrections for the DJI Battery Maintenance Guide specific support article, the DJI Care service portal, the DJI Care Refresh specific URL, and the 49 CFR 173.185 specific section URL.

References:
25 references across Reference (19) and Related Post (6) categories.
All inline-linked per project style.
A145 (physics), A146 (buyer's framework), A147 (R&D), A148 (geographic setting), A149 (operator training), and A150 (sensors and data) cited via post_url.

**Remaining Work**:
None. Published. Series terminus.

### Sensor and Payload Selection for Search and Rescue Drones — Published

**File**: `_posts/2026-05-20-sensor_and_payload_selection_for_search_and_rescue_drones.markdown`
**Topic**: Sixth article in the SAR drone series after A145 (physics), A146 (buyer's framework), A147 (R&D), A148 (geographic setting), and A149 (operator training). Treats the sensor payload as the principal mission-capability decision the programme manager makes after the airframe and the operator training. Six sensor categories (thermal imaging, electro-optical visible, lidar, multispectral and hyperspectral, audio payloads, specialised). Per-class physics, performance metrics, resolution tiers, vendor landscape. Payload integration covering mass, power, data bandwidth, gimbal mount, and MISB metadata. Sensor data management and chain of custody covering data volume, storage architecture, evidentiary chain of custody, records retention and FOIA, state drone surveillance laws, federal procurement and Blue UAS, cybersecurity controls, vendor data handling policies, and calibration records as evidentiary support. Sensor mix by mission profile scorecard table. Sensor budget by programme tier table mapping to A146 tiers.
**Article Number**: A150
**Completion**: 100%
**Publication Sensibility**: High for the buyer audience (complements A146 as the sensor-and-data investment companion)
**Status**: Published 2026-05-20 (81 references; 4,364 lines)

Standalone aerospace and engineering analytical article on sensor and payload selection for SAR drone programmes.
Sections covered include
opening as sixth in the SAR drone series;
Why the Sensor Frames the Mission (sensor defines detection envelope, airframe defines coverage);
The Sensor Stack Taxonomy (six categories with detection physics, typical range, per-sensor cost tier table);
Thermal Imaging (uncooled LWIR vs cooled MWIR, NETD, four resolution tiers from entry through frontier, radiometric vs non-radiometric, vendor landscape);
Electro-Optical Visible Imaging (sensor format, resolution, stabilisation, low-light and starlight imaging);
Lidar (range, point density, return modes, georegistration via RTK and PPK, vendor landscape);
Multispectral and Hyperspectral Imaging (wildfire SWIR application, water rescue, ground anomaly detection);
Audio Sensors and Acoustic Payloads (loudspeaker payloads, acoustic detection research phase);
Payload Integration (mass and endurance trade, power budget, data bandwidth, gimbal mount standards including DJI Skyport and ASTM F38, MISB KLV and STANAG 4609 metadata);
Sensor Data Management and Chain of Custody (data volume by sensor class with concrete per-hour figures, storage architecture across onboard, ground station, and cloud classes, chain of custody for evidentiary use with KLV metadata, cryptographic hash integrity, calibration record linkage, records retention and FOIA implications including IACP body-worn camera framework adaptation, state drone surveillance laws with NCSL tracker and representative state statutes from Florida, Texas, Illinois, California, and Nevada, federal procurement restrictions with American Security Drone Act and Blue UAS framework, cybersecurity controls covering NIST 800-53, NIST 800-171, CMMC, and FedRAMP, vendor data handling policies for DJI FlightHub 2, Skydio Cloud, Parrot Cloud, Wingtra Cloud, DroneDeploy, Pix4D, Esri Site Scan, and Esri ArcGIS, calibration records and evidentiary support under the Daubert standard with ISO IEC 17025 and NIST traceability);
Sensor Mix by Mission Profile (eight-profile scorecard table from night land search through underwater);
Sensor Budget by Program Tier (five-tier scorecard table mapping to A146 tiers);
Out of Scope (sensor-specific operator training, maintenance and lifecycle management, machine learning detection algorithms, export control regime, specialised sensors, underwater payloads, international regulatory regimes);
Conclusion.

Research agent verified
the FLIR Boson Plus and Boson core distinction (NETD 20 mK vs 50 mK),
the Hadron 640R modular pairing,
the Tau 2 pixel pitch and ITAR classification,
the Workswell WIRIS Pro 640x512 and WIRIS Security 800x600 split,
the Sierra-Olympia naming where Vinden is uncooled LWIR and Ventus is cooled MWIR,
the DJI Zenmuse L2 five-return survey lidar performance,
the DJI Zenmuse V1 thermal-and-loudspeaker payload at 127 dB and 500 metres,
the LightWare microLiDAR altimeter line,
the Ouster-Velodyne merger,
the YellowScan and Riegl survey-grade configurations,
the MicaSense AgEagle ownership and Altum-PT thermal-multispectral configuration,
the Cubert ULTRIS snapshot hyperspectral line,
the MISB ST 0601 KLV and STANAG 4609 motion imagery interoperability framework,
the ASTM F38 subcommittee structure and the ISO 21895 categorisation standard,
the MIL-STD-704 aircraft and MIL-STD-1275 ground vehicle power standards,
and
the DroneAudioset benchmark for distress-signal detection research.

Critical factual corrections applied:
the "Brigade Electronics drone loudspeaker line" claim removed since Brigade has no public drone loudspeaker product, replaced with the DJI Zenmuse V1 integrated payload and the Sky Speaker-I aftermarket payload from Yangda;
the "SkyShout purpose-built drone loudspeaker payloads" claim removed since the SkyShout manufacturer attribution could not be verified, replaced with the Sky Speaker-I from Yangda;
the Carnegie Mellon whistle detection attribution softened to "CMU Robotics Institute AirLab work on SAR-oriented aerial robotics" with the DroneAudioset benchmark cited as the specific distress-signal research anchor;
the "12 volt and 28 volt drone payload power bus standards" claim reframed since the drone industry has not adopted either MIL-STD-704 or MIL-STD-1275 as a universal payload bus, with both standards now cited as relevant aviation power standards rather than drone standards;
the "ASTM Committee F38 universal payload mount standard" claim reframed since F38 has not standardised a universal payload mount, with the DJI SkyPort and X-Port through the DJI Payload SDK cited as the dominant Enterprise mount and fixed-wing platforms noted as vendor-specific custom mounts;
URL corrections for FLIR Boson Plus and Hadron 640R (oem.flir.com pages),
the Workswell WIRIS Pro page,
the Freefly MoVI XL store page,
the YellowScan compare-products page,
the Sierra-Olympia airborne cameras page,
the DJI Payload SDK developer portal,
the Sony Starvis Framos overview page.

Second research agent pass commissioned for the sensor data management section. Verified NIST SP 800-86 publication, ISO IEC 27037 and the 27041, 27042, 27043 family, ASTM E2916, SWGDE Best Practices for Drone Forensics document 21-F-002, CJIS Security Policy version 6.0, 28 CFR Part 23 applicability, American Security Drone Act incorporation in FY 2024 NDAA Sections 1821-1833, NDAA Section 848 of FY 2020 prohibition, Blue UAS framework with the December 2025 list transition from DIU to DCMA, Florida Statute 934.50, California Civil Code Section 1708.8 as amended by AB 856, Texas Government Code Chapter 423, Illinois 725 ILCS 167, FOIA Exemption 7(C), NIST SP 800-53 Release 5.2.0, NIST SP 800-171 Rev 3, CMMC final procurement rule effective 10 November 2025 with DoD-contract scope, FedRAMP, DJI FlightHub 2 data residency, DJI Local Data Mode, Skydio Cloud US AWS regions, Parrot Cloud EU residency, Daubert v. Merrell Dow, ISO IEC 17025 calibration laboratory accreditation, and NIST traceability for radiometric thermal calibration via the Low Background Infrared facility.

Critical factual corrections applied in the second pass:
the thermal radiometric per-hour data volume range extended from "500 megabytes to 2 gigabytes" to "500 megabytes to 5 gigabytes" to capture continuous radiometric video capture;
the lidar per-hour data volume range extended from "5 to 30 gigabytes" to "5 to 50 gigabytes" to capture higher-point-rate frontier survey-grade systems;
the example Tier 2 weekly thermal data volume adjusted to "5 to 50 gigabytes per week" reflecting the wider range;
the CMMC clarification added that the certification applies primarily to Department of Defense contracts rather than the non-Department of Defense federal grants that the SAR programme more commonly operates under;
the Blue UAS attribution clarified as "Defense Innovation Unit Blue UAS framework" with the December 2025 list transition to the Defense Contract Management Agency noted;
the California citation refined to "California Civil Code Section 1708.8 as amended by AB 856";
URL corrections for the American Security Drone Act FAR final rule, the Blue UAS framework page at diu.mil/blue-uas/framework, the SWGDE drone forensics document, the California Civil Code Section 1708.8 specific URL.

References:
81 references across Reference (76) and Related Post (5) categories.
All inline-linked per project style.
A145 (physics), A146 (buyer's framework), A147 (R&D), A148 (geographic setting), and A149 (operator training) cited via post_url.

**Remaining Work**:
None. Published.

### Operator Training and Certification for a Search and Rescue Drone Program — Published

**File**: `_posts/2026-05-19-operator_training_and_certification_for_search_and_rescue_drone_programs.markdown`
**Topic**: Fifth article in the SAR drone series after A145 (physics), A146 (buyer's framework), A147 (R&D), and A148 (geographic setting). Disaggregates the operator training cost that A146 mentioned in passing into a five-layer training stack (FAA Part 107, manufacturer training, SAR operational training, NIMS and ICS, specialised operations). Per-layer cost and timeline. Recurrency requirements. Crew roles and training pathways. Operator pool construction. Training budget by program tier.
**Article Number**: A149
**Completion**: 100%
**Publication Sensibility**: High for the buyer audience (complements A146 as the operator-investment companion)
**Status**: Published 2026-05-19 (56 references; 2,059 lines)

Standalone aerospace and engineering analytical article on operator training and certification for SAR drone programmes.
Sections covered include
opening as fifth in the SAR drone series;
Why Training Dominates the Cost (personnel scaling, currency accumulation, turnover replacement);
The Five Layers of the Training Stack (overview);
Layer 1, the Regulatory Minimum (FAA Part 107 certificate, ALC-451 recurrent course, waivers and exemptions, Public Aircraft Operations pathway);
Layer 2, Manufacturer Training (DJI Enterprise Learning Center, Skydio Academy, Parrot Certified Training Program, AeroVironment training, Quantum Systems, Wingtra);
Layer 3, SAR Operational Training (DRONERESPONDERS UNITE, TEEX UAS programmes, NASAR SARTech series, NDSU/NPUASTS, Sinclair, Embry-Riddle);
Layer 4, NIMS and ICS Integration (IS-100, IS-200, IS-700, IS-800, ICS-300, ICS-400, NWCG alignment);
Layer 5, Specialised Operations (night, OOP with ASTM F3322, BVLOS, wildfire NWCG taskbooks);
Recurrency and Currency Maintenance (per-layer recurrency, flight-hour requirements);
Crew Roles and Training Pathways (Visual Observer, Sensor Operator, Remote Pilot in Command, Search Team Coordinator, UAS Team Leader with role-cost scorecard table);
Building the Operator Pool (selection, volunteer vs paid, retention, multi-platform qualification);
Training Budget by Program Size (scorecard table mapping to A146's five tiers);
Out of Scope (sensor selection training, maintenance technician training, state-by-state variation, international frameworks);
Conclusion.

Research agent verified
the FAA Part 107 and ACS materials,
the FEMA Independent Study and ICS course catalogue,
the NWCG Next Generation Position Task Book pathway,
the SAR-specific training providers,
the manufacturer training portals,
and the NIST Standard Test Methods adoption pathway.
Critical factual corrections applied:
the non-existent "NIMS UAS Group Supervisor" position renamed to "UAS Team Leader" with reference to the actual NWCG UASM position and FEMA NIMS-509 sUAS team typing,
the non-existent NWCG "UASGS" and "RPM" positions replaced with the actual NWCG UASP, UASM, and UASL positions,
the "NIST-licensed evaluator" claim for TEEX corrected to "NIST-aligned evaluator" with reference to ASTM Committee E54.09 and the Airborne Public Safety Association as the credentialing bodies,
and URL corrections for ICS-300/400 (separate catalogue URLs), Embry-Riddle (bachelor's programme), Sinclair (UAS center), AeroVironment (Puma product page since training is contract-bundled), Parrot (certified training programme), NDSU/NPUASTS (test site), TEEX (sUAS-specific programme), and Wingtra (extended services).

References:
56 references across Reference (52) and Related Post (4) categories.
All inline-linked per project style.
A145 (physics), A146 (buyer's framework), A147 (R&D), and A148 (geographic setting) cited via post_url.

**Remaining Work**:
None. Published.

### Search and Rescue Drone Fleets by Geographic Setting — Published

**File**: `_posts/2026-05-18-search_and_rescue_drone_fleets_by_geographic_setting.markdown`
**Topic**: Fourth article in the SAR drone series after A145 (physics and economics), A146 (buyer's framework), and A147 (R&D companion). Treats the urban-to-frontier geographic axis as an independent fleet-selection filter alongside A146's mission-profile filter. Four operational levels (Densely Urban, Suburban or Small Urban, Rural, Frontier and Remote) mapped to federal classifications (RUCC, RUCA, CDC NCHS, FAR). Per-level platform mix, fleet sizing, airspace and regulatory posture, funding map, and crew complement. Parallel-operations patterns (single-aircraft serial, single-class parallel, cross-class parallel, multi-aircraft swarms, manned-unmanned teaming). Reading-order table for the four articles in the series.
**Article Number**: A148
**Completion**: 100%
**Publication Sensibility**: High for the buyer audience (complements A146)
**Status**: Published 2026-05-18 (51 references; 1,694 lines)

Standalone aerospace and engineering analytical article on the geographic-setting filter for SAR drone fleet selection.
Sections covered include
opening as fourth in the SAR drone series;
Why Setting Matters Beyond Mission Profile (six structural axes: airspace classification, operations over people, beyond visual line of sight, range and communications, crew complement, funding landscape);
The Federal Geographic Classifications (USDA RUCC, RUCA, CDC NCHS, USDA FAR);
The Four Operational Levels (with mapping table to the federal classifications);
Level 1, Densely Urban (multicopter-dominated fleet, LAANC routine, OOP routine, UASI funding);
Level 2, Suburban or Small Urban (balanced multicopter and hybrid fleet);
Level 3, Rural (fixed-wing or hybrid essential, Class G airspace, SHSP funding);
Level 4, Frontier and Remote (long-endurance fixed-wing essential, Class G, Section 44807 exemptions, federal frontier-operating agency budgets);
Parallel Operations Patterns (single-aircraft serial, single-class parallel, cross-class parallel, multi-aircraft swarms, manned-unmanned teaming);
Airspace and Regulatory Posture by Level (scorecard table);
Funding by Level (UASI, SHSP, THSGP, AFG, federal frontier agency budgets, USDA Rural Development);
Crew Complement by Level (scorecard table);
The Quartet Reading Order (table mapping audience to entry article);
Out of Scope (international classifications, detailed airspace charting, specific operational tactics, state-by-state regulatory variation);
Conclusion.

Research agent verified
the federal classification system URLs,
the FAA airspace and LAANC URLs,
the Part 107 Operations Over People rule and ASTM F3322 standard,
the UASI and HSGP funding programmes,
the federal frontier-operating agency UAS programmes,
and the parallel-operations multi-drone management platforms.
URL corrections applied for CDC NCHS, B4UFLY, USFS UAS, USFWS UAS, Iridium for UAV markets, Starlink business, NPS aviation search and rescue, USDA Rural Development community facilities, and the UAS Facility Maps canonical ArcGIS-hosted location.

References:
51 references across Reference (48) and Related Post (3) categories.
All inline-linked per project style.
A145 (physics and economics), A146 (buyer's framework), and A147 (R&D companion) cited via post_url as the prior articles in the SAR drone series.

### Research and Development for Search and Rescue Drones — Published

**File**: `_posts/2026-05-17-research_and_development_for_search_and_rescue_drones.markdown`
**Topic**: Third article in the SAR drone series after A145 (physics and economics) and A146 (buyer's framework). Treats the research and development side for the smaller audience of academic SAR research groups, federal labs, public-safety agencies with engineering staff, SBIR awardees, and the supporting contractor base. Build-versus-buy frame, federal R&D funding sources, university and federal lab partnerships, the SDK and simulator landscape, custom payload development, regulatory pathways for experimental aircraft, intellectual property in federally funded research, and the technology transition through the valley of death.
**Article Number**: A147
**Completion**: 100%
**Publication Sensibility**: High for the R&D audience; not for the general SAR buyer audience
**Status**: Published 2026-05-17 (101 references; 2,015 lines)

Standalone aerospace, engineering, and program-management analytical article.
Sections covered include
opening as third in the SAR drone series;
The Build-Versus-Buy Frame (three options: build, modify, buy with operational properties that move the program between tiers);
When to Build, When to Modify, When to Buy (custom flight envelope, custom sensor integration, novel autonomous behaviour, multi-aircraft coordination, custom communications);
Federal R&D Funding for SAR Drones (DHS S&T including LRBAA and SBIR and FRRG, SBIR/STTR, NIST PSCR, NIST Standard Test Methods, NASA UAS-NAS, NSF CPS and SCC, DOE national labs including Sandia ORNL INL PNNL, DARPA OFFSET and SubT);
University and Federal Lab Partnerships (the seven FAA UAS Test Sites with the corrected chronology of six in December 2013 plus UAF in early 2014, Raspet, NREC, MIT Lincoln Lab, JHU/APL, NPS CRUSER);
The SDK and Simulator Landscape (DJI Mobile/Onboard/Payload SDKs, Skydio Extend, Parrot Olympe and Open Flight Control, PX4, ArduPilot, ROS 2, PX4 SITL/HITL, AirSim with the full discontinued-and-continued-by-IAMAI lineage, Gazebo, NVIDIA Isaac Sim, MathWorks UAV Toolbox);
Custom Payload Development (Pixhawk/Holybro/mRo autopilot hardware, FLIR Boson Plus and Workswell and Sierra Olympia thermal payloads, LightWare LiDAR, Raspberry Pi and NVIDIA Jetson companion computers, NDAA-compliant component sourcing);
Regulatory Pathways for Experimental Aircraft (Part 107, Section 44807, COA, Special Airworthiness Certificate, Type Certification, Part 108 NPRM);
Intellectual Property in Federally Funded Research (Bayh-Dole, SBIR uniform 20-year data rights regime under May 2019 SBA Policy Directive and DFARS Final Rule January 2025, Stevenson-Wydler and CRADAs, DFARS 252.227-7013/-7014, STTR pre-award allocation);
Technology Transition from Prototype to Operational Use (valley of death, SBIR Phase III sole-source, DHS T2C and CAP, FAA Type Certification, NIST Standard Test Methods as gates, operator demonstrations through DRONERESPONDERS UNITE);
Out of Scope (detailed engineering of custom platforms covered in A112 through A131, international R&D, counter-UAS, manned aircraft integration, commercial-only development);
Conclusion.

Research agent verified
the underlying SDK and platform URLs,
the federal funding programmes,
the university lab and FAA test site URLs,
the regulatory pathway URLs,
and the intellectual property regime documents.
Critical factual corrections applied:
the SBIR data rights regime corrected to the uniform 20-year window under the May 2019 SBA Policy Directive (the pre-2019 4-years-plus-12 regime no longer applies),
the FAA UAS Test Site chronology corrected to six designated December 2013 plus UAF early 2014,
the Nevada UAS Test Site updated to the UNR Nevada Autonomous programme (March 2022 transition),
the University of Maryland UAS Test Site updated to UROC (October 2022 rebrand),
the Naval Postgraduate School lab corrected from the non-existent CAVR to the actual CRUSER,
the AirSim lineage corrected to acknowledge the July 2022 archive, the December 2023 Project AirSim discontinuation, and the IAMAI Simulations continuation,
and the DHS transition vehicles updated from the older Transition to Practice programme to the current Technology Transfer and Commercialization Program plus the Commercialization Accelerator Program.

References:
101 references across Reference (92) and Related Post (9) categories.
All inline-linked per project style.
A145 (physics and economics) and A146 (buyer's framework) cited via post_url as the prior articles in the SAR drone series.
A112 (prototyping), A132 (SBIR intro), A138 (Phase III), A139 (data rights), A141 (after the award), A142 (strategy), and A144 (worked campaign) cited via post_url as the prior SBIR and fixed-wing UAV series articles.

### A Buyer's Decision Framework for Search and Rescue Drones — Published

**File**: `_posts/2026-05-16-buyers_decision_framework_for_search_and_rescue_drones.markdown`
**Topic**: Practitioner buyer's decision framework for US-based search and rescue drone procurement in 2026, the actionable companion to A145. Three-branch decision tree on funding source, mission profile, and budget tier. Five budget tiers including a Tier 0 proof-of-concept tier for organizations beginning a program. Worked five-year total cost of ownership. Federal funding source map. Crew complement and Incident Command System integration. Insurance and liability. Buying timeline.
**Article Number**: A146
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-16 (60 references; 1,755 lines)

Standalone aerospace and engineering analytical article on UAV procurement for SAR.
Sections covered include
opening framing as companion to A145;
Branch One, the Funding Source (FAR 52.240-1 effective 22 December 2025, ADSA 2023, NDAA Section 1709 of FY 2025, FCC Covered List actions on DJI and Autel, DCMA Blue UAS list since 3 December 2025, JAG restriction on drone procurement);
Branch Two, the Mission Profile (wilderness, urban, water rescue, alpine, disaster response, payload essentials);
Branch Three, the Budget Tier:
  Tier 0, Evaluation and Proficiency ($300 to $1,500 acquisition; proof-of-concept-through-production framing universal to any new capability; DJI Mini 4 Pro, Autel Nano Plus, BetaFPV Cetus Pro; SDK and simulator references including DJI Mobile SDK, Parrot Olympe, PX4, ArduPilot, AirSim, Gazebo);
  Tier 1, Volunteer ($3,000 to $15,000);
  Tier 2, Small Professional ($15,000 to $60,000);
  Tier 3, Medium Professional ($60,000 to $250,000);
  Tier 4, Large Program or Federal Agency ($250,000 to $2 million plus);
a Worked Five-Year Total Cost of Ownership (Tier 3 example, approximately $430,000 over five years against $200,000 acquisition);
Funding Sources (HSGP with UASI consolidated into SHSP in FY 2025, AFG admissible for drones, SAFER personnel-only, JAG restricted, Operation Stonegarden);
Crew Complement and Incident Command Integration;
Insurance and Liability (FTCA, sovereign immunity, commercial insurance);
the Buying Timeline (6 to 18 months from decision to operational capability);
Out of Scope;
Conclusion.

Research agent verified
the FAR 52.240-1 effective date and citation,
the ADSA 2023 enactment as part of FY 2024 NDAA,
the corrected attribution of Section 1709 to FY 2025 NDAA,
the DCMA Blue UAS list transfer of 3 December 2025,
the JAG restriction on drone procurement per Bureau of Justice Assistance guidance,
the UASI consolidation into SHSP in FY 2025,
the SAFER personnel-only scope,
current 2026 prices for representative platforms,
and the structural gap that no NDAA-compliant prosumer thermal multicopter sells under $10,000 in the US market.
The article incorporates these findings as factual corrections rather than as commentary.

References:
60 references across Reference (58) and Related Post (2) categories.
All inline-linked per project style.
A145 (physics and economics companion) cited via post_url.
A134 (payload and mission systems) cited via post_url.
Forward reference to a future A147 (drone development companion) is plain prose without a post_url tag, to be upgraded after A147 publishes.

### Fixed-Wing, Multicopter, and Hybrid Drones for Search and Rescue, Physics and Economics — Published

**File**: `_posts/2026-05-15-fixed_wing_multicopter_and_hybrid_drones_for_search_and_rescue.markdown`
**Topic**: Comparative analysis of the three drone platform classes (fixed-wing, multicopter, hybrid VTOL) for search and rescue, covering the underlying physics, capital outlay, upkeep costs, and personnel training. The first of a two-part series, with the buyer's decision framework to follow as A146.
**Article Number**: A145
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-15 (57 references; 1,824 lines)

Standalone aerospace and engineering analytical article on UAVs in search and rescue.
Sections covered include
opening problem framing;
the three platform classes (fixed-wing, multicopter, hybrid VTOL with examples);
the physics of fixed-wing flight (lift, drag, lift-to-drag ratio, Reynolds number and the low-Reynolds-number regime, the electric Breguet endurance equation);
the physics of multicopter flight (Rankine and Froude actuator disk theory, hover power, disk loading, figure of merit, forward-flight power minimum, battery endurance);
the physics of hybrid VTOL aircraft (tail-sitter, quad-plane and convertiplane, tilt-rotor and tilt-wing, the cruise efficiency penalty);
performance implications for search and rescue with a scorecard table;
the four-phase SAR use case sequence (wide-area search, target investigation, intervention, sustained coverage);
capital outlay with a price-range table covering multicopter, hybrid VTOL, and fixed-wing classes;
upkeep costs with a per-platform annual cost table covering batteries, propellers, motors, airframe inspection, sensor calibration, ground station, spectrum, insurance, and incident repair;
personnel training (FAA Part 107, manufacturer training, search-and-rescue specific training, recurrency) with a training cost table;
the hybrid compromise with a scorecard table;
Out of Scope (defers detailed regulatory compliance, sensor technology in depth, weather minima and operational envelopes, mission-system architecture, and specific procurement guidance);
conclusion.

MathJax used throughout the physics sections.

Cross-links via post_url to the existing series:
A114 (runway sizing), A116 (launch and recovery), A123 (propulsion and power sizing), A125 (electric energy systems and endurance budget), A134 (payload and mission systems), A135 (regulatory and operations layer), A144 (worked SBIR campaign).

References:
57 references across Reference (50) and Related Post (7) categories.
All inline-linked per project style.
A parallel research agent verified physics references (Wikipedia momentum theory, drag equation, Reynolds number, Breguet, figure of merit, disk loading), platform references (current URLs for ScanEagle, Skylark, Skydio X10, Penguin C as Edge Autonomy), regulatory references (eCFR Part 107 as primary source, FAA public safety page, EASA), training references (DJI Academy, Skydio Academy, AOPA), and SAR-specific references (DRONERESPONDERS, NASAR).
Vendor URLs returning 403 to curl are documented bot-detection patterns, valid for human readers.
No internal research cited.

### A Worked SBIR and STTR Campaign for a Fixed-Wing UAV — Published

**File**: `_posts/2026-06-27-worked_sbir_and_sttr_campaign_for_a_fixed_wing_uav.markdown`
**Topic**: A single constructed company, the running fixed-wing unmanned aircraft firm, followed through a whole SBIR and STTR campaign from feasibility to prototype to market, synthesizing the entire series; the thirteenth and final article of the SBIR/STTR practitioner-playbook series, the worked-campaign capstone.
**Article Number**: A144
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-27 (19 references)

Standalone article and the thirteenth and final article of the SBIR/STTR practitioner-playbook series, the worked-campaign capstone that closes it.
Framed on the organizing idea of the whole series, that the programs supply non-dilutive capital in stages against demonstrated risk reduction, a staircase from feasibility to prototype to market, walked once in full by one company that uses each award to buy the next rung.
Sections covered include
the company and the airframe (the dual-use fixed-wing unmanned aircraft of the running case);
deciding to pursue (orientation and the agency choice);
getting ready (eligibility and registration, the STTR route chosen);
finding the topic and winning Phase I (the feasibility proposal);
Phase II and the prototype (the commercialization plan, the research partner performing its share under the STTR split);
the money, the rights, and the compliance (the indirect rate and the cash gap, the Phase-I-to-Phase-II funding gap, data-rights marking and the company-and-partner intellectual-property allocation, reporting and audits);
the valley of death and Phase III (the transition partner and the sole-source follow-on);
the strategy over time (the portfolio, the state match, the private-capital bridge, the international option);
where it could go wrong (the same campaign in reverse as a catalog of the failures the series warned against);
and an Out of Scope section.
The company is explicitly a constructed illustration rather than a real firm.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links every prior article of the series via post_url (A132 the introduction, A133 the agencies, A134 eligibility, A135 the topic and solicitation, A136 Phase I, A137 Phase II, A138 Phase III, A139 data rights, A140 the money, A141 after the award, A142 strategy, and A143 international analogs) plus A112 (the running-case unmanned aircraft).
19 references across Reference (4), Related Post (13), and Research (2) categories.
With A144 the SBIR/STTR practitioner-playbook series is complete, all thirteen of thirteen articles published.

### International Analogs to SBIR and STTR — Published

**File**: `_posts/2026-06-26-international_analogs_to_sbir_and_sttr.markdown`
**Topic**: A survey of the foreign equivalents to the United States SBIR and STTR programs, organized by the structural axes along which they differ (procurement versus grant versus tax credit versus equity; non-dilutive versus dilutive; challenge-driven versus open; phased versus single-shot); the twelfth article and the single dedicated international article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A143
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-26 (20 references)

Standalone article and the twelfth of the SBIR/STTR practitioner-playbook series, the one dedicated international article.
Framed on the idea that every advanced economy faces the same market failure in early-stage high-risk technology and each has built a public instrument to fund the risk reduction private capital will not, so the analogs are different answers to one shared question rather than copies of a single design.
Sections covered include
the common problem (the market failure, the valley of death, industrial policy);
the procurement copies (the United Kingdom Contracts for Innovation, formerly the Small Business Research Initiative; the Netherlands SBIR, now the Innovation Impact Challenge; Australia's Business Research and Innovation Initiative; Canada's Innovative Solutions Canada; Japan's 2021-reformed SBIR under the Cabinet Office);
the European grant programs (Horizon Europe, the European Innovation Council Accelerator, the Eureka network and Eurostars, Germany's Central Innovation Programme for the Mittelstand);
the research-collaboration analog (the STTR dimension, the consortium model as the default abroad, South Korea's move to add an STTR-style program);
the tax-credit instrument (Canada's Scientific Research and Experimental Development credit);
the state as investor (the Israel Innovation Authority's royalty-bearing grants, the European Accelerator's blended grant-plus-equity, South Korea's Tech Incubator Program for Startups);
defense and dual-use (the North Atlantic Treaty Organization's DIANA);
the axes of difference (a 13-program comparison table and where the United States program sits);
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
All foreign-program facts were verified by web search and flagged current-as-of, with each country's own program authority named as the only reliable source.
Cross-links A132 (the introduction), A134 (eligibility and the STTR distinction), A138 (the valley of death), A140 (the money, non-dilutive), A142 (strategy and the portfolio), and A112 (the running-case company) via post_url; the worked-campaign capstone is referenced in prose pending A144.
20 references across Reference (11), Related Post (6), and Research (3) categories.

### Strategy and the Portfolio of SBIR and STTR Awards — Published

**File**: `_posts/2026-06-25-strategy_and_the_portfolio_of_sbir_and_sttr_awards.markdown`
**Topic**: The strategic view above the single award, the portfolio, transition versus the mill, stacking non-dilutive capital, the private-capital bridge, dual-use markets, and the discipline of choosing what to pursue; the eleventh article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A142
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-25 (20 references)

Standalone article and the eleventh of the SBIR/STTR practitioner-playbook series.
Framed on the idea that an award is a means and not an end, and that strategy is the discipline of using a portfolio of non-dilutive awards, staged against the risk reduction the whole series has tracked, to build a company that eventually no longer needs them, with the central choice between transition and the mill.
Sections covered include
the award is a means (the strategic frame);
transition versus the mill (the central choice, the transition partner who pulls a technology across the valley of death, the sole-source Phase III as a positioned-for asset);
the portfolio (diversification across agencies, topics, and customers, sequencing, parallel tracks, the proactive pipeline);
stacking the capital (state matching funds, the assistance programs, layering non-dilutive sources);
the private-capital bridge (venture capital, angels, seed, equity dilution, the majority-investor eligibility wrinkle, de-risking the technology for investors);
the market beyond the government (dual-use, commercialization, the National Science Foundation seed fund);
choosing what to pursue (opportunity cost, the distorting award);
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A134 (eligibility and the investor exception), A135 (the topic and solicitation), A137 (the commercialization plan), A138 (the valley of death), A140 (the money), and A112 (the running-case company) via post_url; the international-analogs article is referenced in prose pending A143.
20 references across Reference (11), Related Post (6), and Research (3) categories.

### After the Award, Compliance and Reporting for SBIR and STTR — Published

**File**: `_posts/2026-06-24-after_the_award_for_sbir_and_sttr.markdown`
**Topic**: The continuing obligations of holding an award, performing the work, reporting, invoicing, surviving audits, staying in good standing, and closing out, the second half of the campaign where past performance is built or destroyed; the tenth article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A141
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-24 (19 references)

Standalone article and the tenth of the SBIR/STTR practitioner-playbook series.
Framed on the idea that an award is a binding agreement with continuing duties and that winning is the start of an obligation rather than the end of an effort.
Sections covered include
winning is the start (the award binds, contract or grant);
performing and who to talk to (milestones and deliverables, the contracting officer versus the technical point of contact, formal modifications, no-cost extensions, termination, subcontractor and partner management);
reporting (technical progress and final reports, the commercialization report that feeds the benchmarks, the late-report consequences);
invoicing and getting paid (the payment systems, the lag);
audits and the settling of rates (the Defense Contract Audit Agency, the incurred-cost true-up, the single audit, the audit trail and records retention);
compliance and integrity (the certifications, the False Claims Act, debarment, the defense cybersecurity obligation);
closing out;
continuing standing (registrations, accounting, benchmarks, past performance);
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A134 (eligibility), A136 (the Phase I proposal), A139 (data rights), A140 (the money), and A112 (the running-case company) via post_url; the strategy article is referenced in prose pending A142.
19 references across Reference (11), Related Post (5), and Research (3) categories.

### The Money Behind an SBIR or STTR Award — Published

**File**: `_posts/2026-06-23-money_behind_an_sbir_or_sttr_award.markdown`
**Topic**: The cost proposal, direct and indirect costs, the indirect rate, compliant accounting, and the cash flow that decide whether a company that won an award can survive it; the ninth article of the SBIR/STTR practitioner-playbook series, the one with arithmetic.
**Article Number**: A140
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-23 (18 references)

Standalone article and the ninth of the SBIR/STTR practitioner-playbook series, the one with arithmetic.
Framed on the idea that the award is a fixed pot and the company must justify it in a compliant budget, account for it in a way the government accepts, and finance the gap between spending it and being paid.
Sections covered include
the cost proposal (justify every dollar, fit the cap, match the work plan, evaluated for reasonableness, the agency budget format);
direct and indirect costs (the fringe, overhead, and general-and-administrative pools, equipment title);
the indirect rate (rate equals the indirect pool over an allocation base, the loaded-cost chain, provisional versus negotiated rates, the true-up risk);
fee and the two contract types (cost-reimbursement with a fee, fixed-price, grants without fee, no cost share);
compliant accounting (segregation, timekeeping, the Defense Contract Audit Agency, proportionate standards);
allowable and unallowable costs (the cost principles);
cash flow, the quiet killer (the lag and the gap, burn rate and runway, outside financing and the line of credit and factoring);
a note on assistance funds;
common money mistakes;
scale and the UAV case;
and an Out of Scope section.
mathjax true, with the indirect-rate and loaded-cost relations, the one article in the series with arithmetic.
No runnable code, so no Software Versions section.
Cross-links A136 (the Phase I proposal), A137 (Phase II), A138 (Phase III), and A112 (the running-case company) via post_url; the compliance and strategy articles are referenced in prose pending A141 and A142.
18 references across Reference (11), Related Post (4), and Research (3) categories.

### Data Rights and Intellectual Property in SBIR and STTR — Published

**File**: `_posts/2026-06-22-data_rights_and_intellectual_property_for_sbir_and_sttr.markdown`
**Topic**: The intellectual property a company keeps under the programs, patents under Bayh-Dole and the special SBIR data rights, the crown jewel that the non-dilutive funding was meant to build and that marking preserves; the eighth article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A139
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-22 (16 references)

Standalone article and the eighth of the SBIR/STTR practitioner-playbook series, its crown-jewel article.
Framed on the idea that the government funds the work but the company keeps the inventions and the technical data, so the program is non-dilutive in intellectual property as well as equity, and the retained ownership is the asset the funding was meant to build, kept only by guarding it.
Sections covered include
two bodies of rights (patents versus data rights, and the STTR allocation with the research institution);
patent rights under Bayh-Dole (the company elects title, the election clock, march-in rights, the United-States-manufacturing preference);
SBIR data rights (the protected license, the protection period historically four years and since lengthened, background versus foreground);
marking is the act that preserves the rights (unmarked data risks unlimited rights, markings must conform, assertions can be challenged);
the categories of rights (unlimited, government-purpose, limited and restricted, the special SBIR category);
what the government keeps and what the company keeps;
threats to the crown jewel (subcontracts, omissions, expiry, over-delivery, mixed funding, open-source code);
how the rights create value (the sole-source position, the asset in a sale);
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A132 (orientation), A134 (eligibility), A136 (the Phase I proposal), A138 (Phase III), and A112 (the running-case company) via post_url; the money, compliance, and strategy articles are referenced in prose pending A140, A141, and A142.
16 references across Reference (9), Related Post (5), and Research (2) categories.

### Phase III and the Valley of Death for SBIR and STTR — Published

**File**: `_posts/2026-06-21-phase_iii_and_the_valley_of_death_for_sbir_and_sttr.markdown`
**Topic**: Phase III, the commercialization step that carries no SBIR funds, and the valley of death between a funded prototype and a self-sustaining product or fielded program, with the sole-source authority and the data rights as the tools for crossing it; the seventh article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A138
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-21 (19 references)

Standalone article and the seventh of the SBIR/STTR practitioner-playbook series.
Framed on the idea that Phase III is a destination rather than an award, since it carries no program money, so the company must cross the valley of death from a funded prototype to a self-sustaining product or fielded program on other money.
Sections covered include
what Phase III is (no set-aside money, no dollar or time limit, the high technology-readiness rungs, the concrete funding sources, not strictly sequential);
the sole-source authority (the broad, non-expiring procurement lever, permission to buy and not a commitment);
the valley of death (the gap and why technologies die in it);
crossing by government transition (the program of record, the transition partner, the budget line, the acquisition pull, the prime-contractor path and its risk, the CRADA and the readiness program);
crossing by the market (the product, the customers, the venture capital, the Food and Drug Administration path, SBIR as an investor credential);
why Phase III is the point (the benchmarks measure it, the mill is the failure to reach it);
common ways to fall in;
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A132 (orientation), A134 (eligibility), A137 (Phase II), and A112 (the running-case company) via post_url; the data-rights, money, and strategy articles are referenced in prose pending A139, A140, and A142.
19 references across Reference (11), Related Post (4), and Research (4) categories.

### Phase II and the Commercialization Plan for SBIR and STTR — Published

**File**: `_posts/2026-06-20-phase_ii_and_the_commercialization_plan_for_sbir_and_sttr.markdown`
**Topic**: The Phase II development award and the commercialization plan that becomes a first-class scored deliverable, the step where a funded research result becomes a business or remains a research result; the sixth article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A137
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-20 (20 references)

Standalone article and the sixth of the SBIR/STTR practitioner-playbook series.
Framed on the idea that Phase II is the step where the program stops asking whether the idea can work and starts asking whether it can become a product, so the money grows by an order of magnitude, the work turns from feasibility to development, and the commercialization plan becomes a scored deliverable.
Sections covered include
what Phase II builds (a prototype, the middle technology-readiness rungs, the base-and-option structure, the intellectual property);
the gate from Phase I (the sequence, the funding gap, Direct to Phase II, selection is not award);
the Phase II proposal (the shift of weight to commercialization, the work-split limit);
the commercialization plan as a deliverable (a business plan, the market analysis, the value proposition, the competition, the go-to-market strategy, product-market fit, documented commitments such as a memorandum of understanding, and the reporting that feeds the eligibility benchmarks);
transition versus market commercialization (the two agency cultures);
extending Phase II and bridging toward Phase III (the enhancement, the sequential Phase II, the commercialization readiness program);
the funding gap and cash flow;
common ways to lose Phase II;
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A132 (orientation), A133 (agency survey), A134 (eligibility), A136 (the Phase I proposal), and A112 (the running-case company) via post_url; Phase III and the money article are referenced in prose pending A138 and A140.
20 references across Reference (11), Related Post (5), and Research (4) categories.

### Writing the Phase I SBIR and STTR Proposal — Published

**File**: `_posts/2026-06-19-writing_the_phase_i_proposal_for_sbir_and_sttr.markdown`
**Topic**: Writing the Phase I proposal as an argument that the company can retire an idea's feasibility risk, written to the evaluation criteria, by a credible team, with a commercial promise; the proposal-craft core of the SBIR/STTR practitioner-playbook series.
**Article Number**: A136
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-19 (20 references)

Standalone article and the fifth of the SBIR/STTR practitioner-playbook series, its proposal-craft core.
Framed on the idea that a Phase I proposal is an argument that the company can retire the feasibility risk of an idea, written to the published evaluation criteria, by a believable team, with a commercial promise.
Sections covered include
what Phase I actually asks (feasibility and proof of concept, not a product, the overpromise as the classic failure, the technology-readiness staircase);
the volumes and their shape (the technical and cost volumes telling the same story, the project summary and public abstract, the proprietary markings, the page-limit boundary);
the sections of the technical volume;
the three things a reviewer scores (technical merit, qualifications, commercialization potential);
writing the innovation (the feasibility question, the technical risk to retire, plain technical writing);
the work plan (the work breakdown, milestones, deliverables, risk and mitigation, fitting the envelope, and setting up Phase II with go-or-no-go criteria);
the team and the past performance (the principal investigator and the work-split limits, the STTR partner);
the commercialization story (scored even in Phase I, dual-use, the customer letter);
writing to the reviewer (peer review at science agencies, government technical evaluation at directed agencies, clarity for a busy reader, the internal red-team review);
review, debrief, and resubmission (most proposals lose, the debrief is the prize, resubmit);
common ways to lose;
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A132 (orientation), A134 (eligibility), A135 (solicitation), and A112 (the running-case company) via post_url; Phase II is referenced in prose pending A137.
20 references across Reference (12), Related Post (4), and Research (4) categories.

### Finding a Topic and Reading an SBIR or STTR Solicitation — Published

**File**: `_posts/2026-06-18-finding_a_topic_and_reading_a_solicitation_for_sbir_and_sttr.markdown`
**Topic**: Finding the topic or funding opportunity that matches a company's capability and reading the solicitation precisely, the bridge between eligibility and the proposal; the fourth article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A135
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-18 (16 references)

Standalone article and the fourth of the SBIR/STTR practitioner-playbook series.
Framed on the two tasks of the stage, finding the opportunity (a matching topic at a directed agency, fit within a broad area at an open one) and reading the solicitation as the contract for the competition.
Sections covered include
two kinds of looking;
where the opportunities live (the cross-agency portal, the agency systems, the calendar);
the anatomy of a solicitation, including tracking its amendments;
reading a topic (the objective, deliverables, target technology readiness level, the dual-use expectation, the keywords, and the customer-pull letters to begin lining up);
the pre-release window and talking to the agency (the directed-agency topic-author contact and the blackout versus the open-agency program-officer culture);
is it a fit and is it winnable (past-award intelligence from the searchable awards record, and the teaming and STTR-partner commitment);
reading for compliance (the cheapest loss, with the cost ceiling and period scoping the work);
writing to the evaluation criteria;
the open-agency path (the NSF project pitch, the NIH institute and funding opportunity);
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A132 (orientation), A133 (agency survey), A134 (eligibility), and A112 (the running-case company) via post_url.
16 references across Reference (8), Related Post (4), and Research (4) categories.

### SBIR and STTR Eligibility and the Registration Stack — Published

**File**: `_posts/2026-06-17-eligibility_and_the_registration_stack_for_sbir_and_sttr.markdown`
**Topic**: The two gates an applicant clears before any SBIR or STTR proposal, eligibility (what the company must be) and registration (getting it into the federal systems), with the registrations' lead time gating the calendar; the third article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A134
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-17 (21 references)

Standalone article and the third of the SBIR/STTR practitioner-playbook series.
Framed on the two gates before a proposal, eligibility as a property of the company true or false on the day it applies, and registration as a multi-week sequence of accounts and identifiers whose lead time gates the calendar.
Sections covered include
eligibility, what the company must be (small with affiliation, for-profit, United States, the five-hundred-employee standard versus the industry-code standards, not a socioeconomic set-aside);
the ownership rules and the investor exception (more than half owned by United States individuals or small businesses, the venture, private-equity, and hedge-fund majority-ownership exception that is agency-specific);
the principal investigator and the work (the SBIR primary-employment requirement, the STTR flexibility, the work splits, the United States place of performance);
the performance benchmarks and the duplicate-funding and essentially-equivalent-work rule;
national-security eligibility (the 2026 screening), the export-control neighbor, and the certification-and-fraud framing (False Claims Act exposure);
the registration stack in order (Login.gov, the System for Award Management with the unique entity identifier and CAGE code, the program company registry and its control identifier, the agency portal);
why the stack gates the calendar (validation can take weeks, annual renewal, the registration-is-free warning);
scale and the small-company case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A132 (orientation), A133 (agency survey), and A112 (the running-case company) via post_url.
21 references across Reference (13), Related Post (3), and Research (5, the live federal systems) categories.

### A Survey of the SBIR and STTR Agencies — Published

**File**: `_posts/2026-06-16-survey_of_the_sbir_and_sttr_agencies.markdown`
**Topic**: A survey of the eleven SBIR and five STTR agencies for the practitioner choosing where to apply, organized on two axes (grant versus contract, directed versus open topics); the second article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A133
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-16 (25 references)

Standalone article and the second of the SBIR/STTR practitioner-playbook series, in the business/funding/sbir category.
Organized on two independent axes, the award vehicle (grant or cooperative agreement versus procurement contract) and the topic (directed versus open), with the agencies populating the corners.
Sections covered include
the two axes and where the agencies sit;
how many agencies and why the sizes differ (eleven SBIR, five STTR, the set-aside making budget proportional to extramural research);
the Department of Defense (contract, directed, the components and the Defense SBIR/STTR Innovation Portal, transition, dual-use, the national-security screening);
the National Institutes of Health (grant, open, standing receipt dates);
the National Science Foundation (grant, broad, America's Seed Fund, the required project pitch);
the Department of Energy (grant but directed, the national-lab STTR fit);
NASA (contract, directed, transition to a NASA mission);
the smaller agencies (Agriculture, Homeland Security, Commerce with NOAA and NIST, Education, Transportation, Environmental Protection);
a comparison table (vehicle, topics, STTR, Direct to Phase II, relative size, character);
choosing where to apply (match by mission and by model, eligibility varying by agency, the cadence as a selection factor, differing post-award support);
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Balanced across agencies per the series plan, with all time-sensitive specifics flagged as current-as-of.
Cross-links A132 (the orientation), A93 (mission-critical engineering, the Department of Defense culture), and A112 (the UAV as a dual-use example) via post_url.
25 references across Reference (16), Related Post (3), and Research (6, one authoritative portal per major agency) categories.

### An Introduction to the SBIR and STTR Programs — Published

**File**: `_posts/2026-06-15-introduction_to_the_sbir_and_sttr_programs.markdown`
**Topic**: Orientation to the United States SBIR and STTR programs, framed on non-dilutive capital staged against demonstrated risk reduction mapped to the technology readiness level; the first article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A132
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-15 (18 references)

Standalone article and the first of a new series, the SBIR/STTR practitioner playbook, in a new category cluster (business/funding/sbir, permalink /business/funding/sbir/).
The master variable is non-dilutive capital staged against demonstrated reduction of risk, the three-phase staircase mapped to the technology readiness level.
Sections covered include
a program that runs on reauthorization (the 2025 lapse and the 2026 reauthorization through fiscal year 2031);
the core idea (non-dilutive, mission-pulled, the set-aside, the scale of over four billion dollars a year across roughly four thousand awards, America's Seed Fund);
the three phases (Phase I feasibility, Phase II development, Phase III commercialization with no SBIR funds and sole-source authority) with the technology-readiness-level mapping and the multi-year timeline;
SBIR versus STTR (the research-institution partner and the work splits);
who can compete (the eligibility gate and the 2026 national-security screening);
why the money is worth the trouble (non-dilutive, data rights, the valley of death);
what the programs are not (the grant-versus-contract distinction, not free money, not a substitute for a customer);
the series ahead;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Explicitly United States, with the international analogs deferred to a later article, and all time-sensitive figures flagged as current-as-of with the live solicitation and the SBA policy directive named as authoritative.
Cross-links A93 (mission-critical engineering), A112 (prototyping the UAV, the running case), and A131 (the risk-based regulatory framing) via post_url.
18 references across Reference (12), Related Post (3), and Research (3) categories.

### The Regulatory and Operations Layer for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-14-regulatory_and_operations_layer_for_fixed_wing_uavs.markdown`
**Topic**: The regulatory and operations layer above the engineering of a fixed-wing UAV, framed jurisdiction-neutrally on the principle that the authorization to operate is granted in proportion to demonstrated risk control, with kinetic energy as the physical proxy for harm; the sixth and final flagged extension.
**Article Number**: A131
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-14 (41 references)

Standalone aerospace article and the sixth and final flagged extension beyond the core fixed-wing-UAV arc, the layer above the engineering, with which the series and its extensions are now complete.
The master variable is the authorization to operate, granted in proportion to the risk an operation poses and the control the operator can demonstrate, with the impact kinetic energy E_k = (1/2) m v^2 as the physical proxy for harm tying the regulatory categories to the mass and speed the series worked in.
Explicitly jurisdiction-neutral, framed on the International Civil Aviation Organization and the Chicago Convention with the FAA, the European Union Aviation Safety Agency, the UK Civil Aviation Authority, the Civil Aviation Safety Authority, Transport Canada, and the Civil Aviation Administration of China named as examples, the thresholds presented as patterns that differ by state and change over time.
Sections covered include
regulation is jurisdictional;
authorization proportionate to risk (the open, specific, and certified pattern, ground risk and air risk, the specific operations risk assessment);
kinetic energy as the measure of harm;
the axes of risk (mass, line of sight, over people, altitude, airspace);
registration, identification, and competency with the autonomy-and-responsibility tension;
airworthiness and the certified end;
integrating with other traffic (segregated versus integrated, unmanned traffic management and U-space, detect and avoid, command-and-control reliability);
the operations layer (concept of operations, crew, pre-flight planning, maintenance, training, the safety management system, just culture, independent accident investigation);
contingency and containment (defined procedures, the geofence, flight termination, and command-link security as a regulatory concern);
adjacent regimes (spectrum and the telecommunication union, export control, privacy and data protection, property rights, insurance, and noise);
the boundary with space (the suborbital handoff to space law, the Outer Space Treaty, the Kármán line as a convention);
scale and the UAV case;
and an Out of Scope section.
MathJax for the kinetic-energy relation.
No runnable code, so no Software Versions section.
The pilot's instruction that not everyone is in the USA is honored throughout, the article naming authorities from several continents, framing the specifics as patterns that vary and change, directing the reader to the governing authority, and drawing its three Research sources from the international bodies (the International Civil Aviation Organization, the European Union Aviation Safety Agency, and the Joint Authorities for Rulemaking on Unmanned Systems for the risk assessment).
References A112, A125, A126, A127, and A130 via post_url.
41 references across Reference (33), Related Post (5), and Research (3) categories.

### Payload and Mission Systems for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-13-payload_and_mission_systems_for_fixed_wing_uavs.markdown`
**Topic**: The payload and mission system of a fixed-wing UAV, framed on the payload fraction and the share of the mass, power, volume, data, and energy budget that reaches the payload, including suborbital spaceplane payload delivery with payload-owned circularization.
**Article Number**: A130
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-13 (45 references)

Standalone aerospace article and the fifth extension beyond the core fixed-wing-UAV arc.
The master variable is the payload fraction and, more broadly, the share of the budgets the series tracked that reaches the payload rather than carrying it, the payload being the point and the platform the overhead.
Sections covered include
the payload fraction (size, weight, power, and cost);
a taxonomy of payloads (electro-optical and infrared, synthetic-aperture radar, signals intelligence, lidar, multispectral and hyperspectral, communications relay, delivery and agricultural, the loitering-munition effector, scientific);
integrating the payload with the platform (mass and center of gravity, power as hotel load with the peak-versus-average note, data with onboard storage and compression, heat, volume, vibration and isolation);
pointing and stabilization with the geolocation and target-location-error chain;
the mission system (tasking, edge versus downlink processing, sensor fusion, autonomy);
the payload sizes the aircraft with the aperture-sets-resolution physics (angular resolution and ground sample distance tying SWaP to standoff performance);
releasing and dropping payloads;
suborbital spaceplane payload delivery (the reusable carrier delivers an accurate release state near apogee and the payload owns circularization, Dv = v_circ - v_h);
scale and the UAV case (modular bays and interface standards, the loitering munition as payload-is-the-aircraft);
a worked example (a 20 percent payload fraction on the 25 kg aircraft, and the ~7.8 km/s circular speed at a 200 km apogee with the honest delta-v split);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
The pilot's explicit inclusion, suborbital spaceplane payload delivery where orbital circularization around apogee is the payload's responsibility, is covered in its own section, with the orbital mechanics after release held out of scope except for the handoff delta-v.
References A120, A121, A125, A126, A127, and A128 via post_url.
45 references across Reference (37), Related Post (6), and Research (2) categories.

### An Aerobatic Maneuver Reference Catalog for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-12-aerobatic_maneuver_reference_catalog_for_fixed_wing_uavs.markdown`
**Topic**: A reference catalog of 79 named aerobatic maneuvers, each classified in the A128 costed-trajectory model, alphabetical with stable family-prefixed IDs; the reference companion to A128.
**Article Number**: A129
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-12 (32 references; 79 catalog rows)

Standalone aerospace reference article and the fourth extension beyond the core fixed-wing-UAV arc, the reference companion to the A128 model.
Written for the UAV operator and the autonomy, not the human pilot.
A 79-row alphabetical catalog with a stable family-prefixed identifier per maneuver across twelve families (lines, turns, rolls, loops and eights, partial loops and combinations, stall turns, tailslides, spins, post-stall and supermaneuvers, three-dimensional and prop-hang figures, basic fighter maneuvers, composite or display).
Columns are the identifier, the maneuver, the family, the spatiotemporal path, the energy-height behavior, the peak load class, and the regime ceiling with flags.
Maneuver definitions are cited to the Aresti catalog, the world air sports federation, the International Aerobatic Club, the basic-fighter-maneuver repertoire, and Wikipedia where an article exists.
The cost classification is forward-declared as an original, qualitative synthesis with three stated limitations, since no catalog tabulates the energy-height behavior, the load class, and the regime ceiling per maneuver.
Sections covered include
how to read the table;
why the thermal cost is folded into the regime column;
provenance and limitations;
the catalog;
maneuvers without a closed form (spins, snaps, the cobra, the Kulbit, the Herbst maneuver, the gyroscopic tumbles, and the three-dimensional and prop-hang figures, with what can still be said);
parametric families;
alternate names;
using the catalog;
reading a row in numbers (the break turn read into the corner-speed and load figures of the structures and model articles);
Out of Scope;
and a conclusion.
MathJax enabled for the model symbols.
No runnable code, so no Software Versions section.
The honesty of the catalog rests on a clear division, the maneuver definitions sourced to the established catalogs and the cost classification offered as an original synthesis to be checked rather than as measured data.
References A120, A123, A125, A127, and A128 via post_url.
32 references across Book (1), Reference (26), and Related Post (5) categories.

### Aerobatics as Costed Trajectories for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-11-aerobatics_as_costed_trajectories_for_fixed_wing_uavs.markdown`
**Topic**: UAV aerobatics treated as commanded spatiotemporal trajectories priced in energetic, structural, and thermal cost across the subsonic, supersonic, and hypersonic regimes, with a hypothetical spaceplane reentry case; the synthesis capstone of the extension set.
**Article Number**: A128
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-11 (42 references)

Standalone aerospace article and the third extension beyond the core fixed-wing-UAV arc (after A126 communications and A127 structures), the synthesis capstone of the extension set.
Written for the UAV operator and the autonomy and explicitly not for the human pilot, treating a maneuver as a commanded spatiotemporal trajectory rather than a learned skill.
The master variable is the energy state and the specific excess power Ps = V(T - D)/W = dh_e/dt, with every maneuver a transaction in potential, kinetic, and propulsive energy and three costs (energetic, structural, thermal) whose dominant term migrates with the speed regime.
Sections covered include
a maneuver as a trajectory;
the energy state and specific excess power (energy height h_e = h + V^2/2g, energy-maneuverability theory);
the three costs and the control-authority-and-bandwidth feasibility gate;
the kinematic primitives and the maneuverability (doghouse) diagram with its lift, structural, and sustained bounds;
a scored catalogue table of ten maneuvers (path, peak load, energy-height behavior, highest surviving regime, with the post-stall spin and cobra flagged as no-closed-form);
the footprint in space and time (airspace volume, time, wind drift, deconfliction);
the subsonic regime (figure flying, the no-human-ceiling advantage, negative-g and outside figures);
the transonic and supersonic regimes (wave drag, Ps collapse, Mach tuck, the shrinking catalogue);
the hypersonic regime (stagnation heating dominant, bank-angle modulation and S-turns, boost-glide and HGV referents);
spaceplane maneuvering during reentry (the corridor, bank reversals and angle of attack, the Shuttle's forty-degree alpha and cross-range, control authority migrating from RCS to surfaces per A122);
spaceplane maneuvering after the thermal wall (terminal-area energy management, tying A124 and A125);
scale and the UAV case (favorable structural scaling, the loitering-munition terminal maneuver, the energy and powertrain-thermal bounds);
a worked example on the 25 kg series aircraft (level turn radius and rate, the corner turn, a loop sized by the energy-height trade, a Mach-five thermal note);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout, honest where no closed form exists.
No runnable code, so no Software Versions section.
The term aerobatics is extended to commanded maneuvering, with an explicit lampshade that figure flying does not survive the hypersonic and reentry regimes.
References A120, A122, A123, A124, A125, and A127 via post_url.
42 references across Book (1), Reference (33), Related Post (6), and Research (2) categories.

### Structures and the Flight Envelope for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-10-structures_and_the_flight_envelope_for_fixed_wing_uavs.markdown`
**Topic**: The airframe structure and the flight envelope of a fixed-wing UAV, framed on the load factor and the load-versus-speed (V-n) diagram, the boundary the whole series operates inside; the second extension beyond the core arc.
**Article Number**: A127
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-10 (42 references)

Standalone aerospace article and the second extension beyond the core fixed-wing-UAV arc (after A126 communications).
The master variable is the load factor n = L/W and the load-versus-speed diagram, the flight envelope bounded by the stall parabola, the structural limit-load line, and the maximum-speed line, with the structure sized to its corners.
Sections covered include
the flight envelope;
the corner and the maneuvering speed;
limit load and ultimate load (the 1.5 factor of safety);
categories and the width of the envelope (normal, utility, aerobatic);
the gust envelope (sharp-edged and derived gust, the light-UAV gust sensitivity);
loads beyond the flight envelope (launch, recovery, touchdown through the undercarriage, taxi and handling, tying A116 and A124);
how the structure carries the load (bending, shear, torsion, asymmetric and combined cases, spar/rib/longeron, monocoque and stressed skin, tying A112);
material, stress, buckling, and the margin of safety (specific strength and modulus, the before-yield instability of thin panels, strength versus stiffness);
fatigue and the life of the structure (the stress-life curve, safe-life, fail-safe, damage-tolerant);
aeroelasticity and the flutter boundary (divergence, control reversal, flutter as a dynamic-pressure wall, tying A112 and A123);
the aerobatic envelope (the widest symmetric diagram, negative-g structure, and the UAV no-pilot point tying loitering munitions, with the maneuver art and physiology out of scope);
the envelope is not fixed (density altitude, the A120 thermal wall, composite knockdown, fatigue, autopilot envelope protection tying A123/A125);
proving the structure (the static ultimate-load test, flutter clearance by ground vibration test and stepped envelope expansion, and the fatigue test article);
scale and the UAV case (square-cube structural fraction, composite and printed structures, attritable design);
a worked example on the 25 kg series aircraft (stall speed about 18 m/s, corner speed about 38 m/s, limit and ultimate loads, a gust increment that rivals the maneuver limit);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
The pilot's pre-draft question, whether aerobatics belongs, is answered in the article by covering aerobatics as the envelope's widest symmetric case.
References A112, A116, A120, A123, and A124 via post_url.
42 references across Book (1), Reference (33), Related Post (5), and Research (3) categories.

### Communications and the Command-and-Control Data Link for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-09-communications_and_the_command_and_control_data_link_for_fixed_wing_uavs.markdown`
**Topic**: The command-and-control data link of a fixed-wing UAV, framed on the link budget (received power versus noise) with latency as the companion constraint; the first extension beyond the core arc.
**Article Number**: A126
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-09 (34 references)

Standalone aerospace article and the first extension beyond the core fixed-wing-UAV arc (which closed with the A125 capstone).
The master variable is the link budget, P_rx = P_tx + gains - free-space path loss, with the signal-to-noise margin setting range and the Shannon limit bounding data rate, and latency as the companion constraint that decides what can be controlled over the link.
Sections covered include
the link budget (Friis, free-space path loss, SNR, Shannon, Fresnel, ISM bands, the frequency range-versus-rate trade, near-ground multipath and the two-ray ground reflection, the regulatory cap on effective radiated power);
the radio horizon;
the moving aircraft (airframe shadowing, radiation-pattern nulls and polarization, antenna diversity, a tracking ground antenna);
the three streams (command uplink, telemetry downlink, payload downlink with codec compression latency);
radio control with a handheld transmitter (2.4 GHz FHSS, ExpressLRS, CRSF/SBUS handoff, the control-link packet rate, FPV, failsafe, the manual path);
computer-controlled transmission (MAVLink, SiK/RFD900 telemetry radios, the ground control station, companion computer over cellular, intent versus stick inputs, coexisting with the handheld link);
beyond line of sight (relay, cellular, SATCOM via Iridium);
latency and why the fast loops are aboard (tying A123 and A125);
security and jamming (J/S ratio, spread spectrum, AES encryption, spoofing, directional antenna);
lost link (the preset failsafe, geofence, tying A116 and A125);
scale and the UAV case (the radios as part of the A121 hotel load);
a worked example (a 100 mW 2.4 GHz link closing 10 km with a 12 dB margin, a ~48 km radio horizon, kbps command versus Mbps video, LOS versus SATCOM latency);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
The pilot's explicit requirement, RC control via both a consumer handheld controller and a computer-controlled transmitter, is covered in its own two sections framed as the coexisting manual and autonomous paths.
References A116, A121, and A125 via post_url.
34 references across Reference (28), Related Post (3), and Research (3) categories.

### Guidance, Navigation, and Automatic Landing for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-08-guidance_navigation_and_automatic_landing_for_fixed_wing_uavs.markdown`
**Topic**: The outer-loop autonomy of a fixed-wing UAV, framed on the feedback loop that drives the error between the navigation estimate and the guidance command to zero; the capstone of the set.
**Article Number**: A125
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-08 (29 references; 333 lines)

Standalone aerospace article and the tenth and capstone entry in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion, A121 electric energy systems, A122 stability and control, A123 dynamic stability and control, A124 landing gear and touchdown, A125 guidance, navigation, and automatic landing).
Takes up the outer loop A123 set up.
The master variable is the feedback loop that drives the error between the commanded state (guidance) and the estimated state (navigation) to zero, nested by bandwidth, with the automatic landing as the tightest loop.
Sections covered include
the nested loops (inner attitude, outer guidance, mission, bandwidth separation, digital sample rates and latency);
navigation (GNSS, INS/IMU, dead reckoning, Kalman fusion, air data, RTK, initialization, GNSS-denied vision);
guidance (waypoints, cross-track error, the look-ahead path-following law);
wind and the ground track (crab, the wind triangle, the small-UAV case);
closing the loop with energy (the total energy control system as the real-time version of the series' energy budget);
the approach and automatic landing (glideslope, flare, RTK/radar-altimeter/vision, touchdown dispersion tied to the runway width) with the automatic-takeoff bookend;
when the loop breaks (GNSS loss, lost link, geofence, return-to-launch, redundancy, flight termination);
scale and the UAV case (Pixhawk-class boards, ArduPilot/PX4, the autonomy spectrum);
a worked example (loop bandwidth separation, the cross-track law, the navigation error budget, the glideslope dispersion);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
References A114, A116, A123, and A124 via post_url, and the conclusion ties the whole ten-article set together.
29 references across Reference, Related Post, and Research categories.
333 lines.

### Landing Gear and the Physics of Touchdown for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-07-landing_gear_and_the_physics_of_touchdown_for_fixed_wing_uavs.markdown`
**Topic**: Landing gear and the surface interfaces of a fixed-wing UAV, framed on the touchdown energy absorbed over a stroke, complementing the runway and recovery articles.
**Article Number**: A124
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-07 (23 references; 320 lines)

Standalone aerospace article and the ninth in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion, A121 electric energy systems, A122 stability and control, A123 dynamic stability and control, A124 landing gear and touchdown).
The master variable is the touchdown energy absorbed over a stroke, n = v^2/(2 g0 d), the energy-and-stroke idea of the recovery article applied to the final surface interface.
Sections covered include
the touchdown energy and the stroke;
wheels and landing gear (retractable versus fixed, tricycle and conventional layout, the oleo strut as gas spring and oil damper, recoil damping and bounce, frangible and sacrificial gear, spin-up and side gear loads, the gear-up fallback);
skids (sacrificial skids, friction stroke, skis and tundra tires by surface);
water landings (floatplane, flying boat, planing and the step, ditching, porpoising);
drogue and main parachutes (the drogue-before-main staging, with the residual touchdown energy taken by an airbag or crush);
deliberate impact (intentional lithospheric and hydrospheric intersection, crushable crashworthy structure for expendable vehicles);
energy bleeding before touchdown (spoilers, forward slip, S-turns, flare, with the honest distinction that true aerobraking is an orbital maneuver while a boost-glide or ramjet or scramjet vehicle does thermally limited atmospheric deceleration);
scale and the UAV case;
a worked example (sink-rate, parachute, and deliberate-impact loads set by the stroke);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
Complements rather than duplicates the launch-and-recovery article.
References A114, A116, A120, and A122 via post_url.
23 references across Reference, Related Post, and Research categories.
320 lines.

### Dynamic Stability and Control for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-06-dynamic_stability_and_control_for_fixed_wing_uavs.markdown`
**Topic**: Dynamic stability and control of a fixed-wing UAV, framed on the damping and frequency of the aircraft's natural modes, the dynamic sequel that completes the stability-and-control arc begun by the static-stability article.
**Article Number**: A123
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-06 (22 references; 316 lines)

Standalone aerospace article and the eighth in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion, A121 electric energy systems, A122 stability and control, A123 dynamic stability and control).
Takes up the dynamic question A122 deferred.
The master variable is the damping and frequency of the natural modes, with the aircraft modeled as a damped harmonic oscillator where static stability is the spring, inertia the mass, and aerodynamic rate forces the damping.
Sections covered include
the spring, the mass, and the damping (with a small-disturbance about-trim caveat);
the longitudinal modes (short-period, phugoid);
the lateral-directional modes (roll subsidence, spiral, Dutch roll, with the spiral-versus-Dutch-roll trade tied to A122's dihedral-versus-weathercock balance);
damping, frequency, and handling qualities (settling time, Cooper-Harper, flying-qualities levels);
gusts and ride quality (turbulence excitation and the small-UAV gust sensitivity);
stability augmentation (yaw damper, pitch damper, rate feedback from an IMU, the SAS inner loop, augmentation limits and pilot-induced oscillation, and the SAS-versus-CAS distinction);
fly-by-wire and relaxed static stability;
scale and the UAV case (faster modes, autopilot and actuator bandwidth);
a worked example (Dutch-roll damping from 0.05 to 0.4 with a yaw damper, and a phugoid period);
and an Out of Scope section that defers derivative estimation and the equations of motion, control-law synthesis, sensors and state estimation, structural and aeroelastic dynamics, departure and spin, and the outer-loop guidance, navigation, and automatic landing.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
References A112, A114, and A122 via post_url.
22 references across Reference, Related Post, and Research categories.
316 lines.

### Stability, Control, and Configuration for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-05-stability_control_and_configuration_for_fixed_wing_uavs.markdown`
**Topic**: Stability, control, and configuration of a fixed-wing UAV, framed on the balance of moments about the center of gravity with the static margin as the master proxy for the stability-versus-maneuverability trade.
**Article Number**: A122
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-05 (46 references; 409 lines)

Standalone aerospace article and the seventh in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion, A121 electric energy systems, A122 stability and control).
Takes up the full stability-and-control treatment A112 deferred.
The master variable is the moment balance about the center of gravity, with the static margin K_n = (x_np - x_cg)/MAC as the proxy for the stability-versus-maneuverability trade.
Sections covered include
the moment balance and the static margin (with the center-of-gravity range across the loading envelope);
lateral and directional static stability (fin weathercock stability and dihedral);
airfoils, camber, and invertibility;
configuration archetypes (conventional empennage, canard, tandem, tailless flying wing with sweep, washout, and reflex);
control surfaces by placement and name (elevator, aileron, rudder, elevon, ruddervator, stabilator, flaperon) with adverse yaw;
high-lift and spoiler devices;
control authority and dynamic pressure, running from aerodynamic surfaces through differential thrust and thrust vectoring to a reaction control system (spaceplane RCS and cold-gas thrusters, tied to A120's boost-glide arc, with an honest low-altitude caveat);
the wing tradeoff (aspect ratio versus wing loading, speed versus glide, planform);
the trim-drag energy cost;
a worked example (static margin and tail volume coefficient, with a flying-wing reflex contrast);
and an Out of Scope section that defers the dynamic-stability modes, control-law design, RCS detailed design, and the translational orbital problem (orbital mechanics, the orbital maneuver, and stationkeeping, affirmed as legitimate for spacecraft that reach orbit).
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
References A112, A114, and A118 via post_url.
46 references across Reference, Related Post, and Research categories.
409 lines.

### Electric Energy Systems and the Endurance Budget for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-04-electric_energy_systems_and_endurance_budget_for_fixed_wing_uavs.markdown`
**Topic**: The electric energy economy of a fixed-wing UAV, framed as a state-of-charge energy-flow budget (supply minus demand, buffered by storage), the flow counterpart to A120's stock budget.
**Article Number**: A121
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-04 (29 references; 381 lines)

Standalone aerospace article and the sixth in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion, A121 electric energy systems).
Fills the solar, fuel-cell, hybrid, and battery-management items A118 deferred.
The master variable is the energy-flow budget, the power balance dE/dt = P_in - P_out and its integral over the harvest cycle, contrasted explicitly with A120's one-time energy stock (stock versus flow).
Sections covered include
the energy-flow budget;
the demand side and the hotel load (flight power versus a fixed non-propulsive floor);
storage as the buffer (specific energy, depth of discharge, round-trip efficiency, cold derating, the specific-energy-versus-specific-power tradeoff, the battery wall, supercapacitor for peaks);
harvesting from the sun (output = efficiency times area times irradiance, the daily account, MPPT named);
the scale gate for solar perpetual flight (square-cube, Pathfinder/Helios/Zephyr/Solar Impulse);
harvesting from hydrogen (PEM fuel cell, Ion Tiger, Phantom Eye);
hybrid systems (series and parallel);
harvesting from the air (thermal and dynamic soaring);
the perpetual-flight closure (daily harvest at least daily demand, night energy within usable storage, cycle-life bounding the campaign);
a worked example on the 25 kg series aircraft;
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
The thesis is that sustained flight is a balance of powers rather than a quantity of energy, and indefinite flight is the cycle closing on itself, which the large light high-flying solar aircraft achieves and the small one does not.
References A112, A118, and A120 via post_url.
29 references across Reference, Related Post, and Research categories.
381 lines.

### Staged and Boosted Propulsion for Small Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-03-staged_and_boosted_propulsion_for_fixed_wing_uavs.markdown`
**Topic**: Staged and boosted propulsion for a ~2m fixed-wing UAV, framed around the post-boost mission energy budget (potential plus kinetic plus stored propulsive energy).
**Article Number**: A120
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-03 (40 references; 472 lines)

Standalone aerospace article and the fifth in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion).
Reopens the high-speed families A118 ruled out of regime by adding a boost stage, and is framed throughout as the management of the post-boost mission energy budget.
The boost deposits potential and kinetic energy (Tsiolkovsky rocket equation, specific impulse, one versus two stage), to which stored propulsive energy is added, and the kinetic share sets the stagnation temperature and therefore the airframe material.
Sections covered include
the mission energy budget with the energy height h_e = h + V^2/2g;
the boost stage;
the thermal wall (stagnation temperature versus Mach, aerodynamic heating, altitude and duration relief);
airframe materials by regime (LW-PLA subsonic, aluminum/composite transonic, titanium/steel supersonic with the SR-71 anchor, superalloy/refractory/CMC/carbon-carbon/UHTC/active-cooling/ablative hypersonic with the X-43 and X-51 anchors);
airframe archetypes for spending the budget (vertical-fighter banking it as altitude with the Bachem Natter anchor, maneuverable descending spending it on lift with lifting-body/waverider/HGV/MaRV members, and conventional holding it level on propulsion);
boost-glide with range (L/D)(h + V^2/2g);
boost-sustainer (RATO and the cruise-missile boost-turbojet);
boost-ramjet (integral rocket-ramjet, GQM-163 Coyote, Mach 2-4 titanium airframe);
boost-scramjet (X-43, X-51, hypersonic materials, research-grade honesty);
boost-throttleable-rocket;
one stage versus two;
a worked example on a 2 m vehicle (propellant fraction and stagnation temperature to Mach 2 and Mach 5, with the Mach-5 energy height of about 147 km);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
The thesis is that the ~2m scale forbids none of these configurations, since material and budget, not size, set how far up the speed ladder a prototype can be carried.
References A112, A114, A116, and A118 via post_url.
40 references across Reference, Related Post, and Research categories.
472 lines.

### Propulsion and Power Sizing for Small Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-02-propulsion_and_power_sizing_for_fixed_wing_uavs.markdown`
**Topic**: Sizing the propulsion and power system of a small fixed-wing UAV, worked outward from the power-required master variable.
**Article Number**: A118
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-02 (36 references; 445 lines)

Standalone aerospace article and the fourth in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion).
Establishes the power-required master variable, where power is thrust times speed and thrust in level flight is drag, so the power to fly is the weight times the speed divided by the lift-to-drag ratio, and works through
the drag polar and lift-to-drag ratio;
propellers and efficiency via momentum theory, static thrust, and advance ratio, including the electric ducted fan;
the thrust-to-weight and launch and climb case that usually sizes the powertrain, tying back to A114 and A116;
electric propulsion (battery specific energy, brushless motor, the endurance equation, and the battery wall);
combustion propulsion (two-stroke and Wankel, brake-specific fuel consumption, heavy fuel, range and endurance);
altitude and available power (the density-altitude lapse of engine power and propeller thrust);
endurance and range with reserves (endurance at the minimum-power speed, range at the best lift-to-drag speed for a propeller aircraft);
a brief solar, hybrid, and fuel-cell note;
jets and regimes beyond the propeller (turbojet and turbofan in scope; ramjet, scramjet, throttleable rocket, and rocket boost-glide named and declared out of regime);
a worked example on the 25 kg series aircraft;
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
Real-UAV anchors RQ-7 Shadow (Wankel), ScanEagle (heavy-fuel piston), and RQ-20 Puma (electric).
References A112, A114, and A116 via post_url.
36 references across Reference, Related Post, and Research categories.
445 lines.

### Three Audiences for an Operating System — Published

**File**: `_posts/2026-05-22-three_audiences_for_an_operating_system.markdown`
**Topic**: Prequel to the BTRON-hypermedia trilogy. Names the operator-as-end-user category as a distinct third audience for an operating system, alongside the consumer and the developer. Sets up the question that A113, A115, and A117 then answer.
**Article Number**: A119
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-22 (61 references; 1,364 lines)

Standalone category-framing article and the prequel to the BTRON-hypermedia trilogy (A113, A115, A117).
Sections covered include
Opening on who an operating system serves;
The Three Audiences (consumer, developer, operator with role definitions and the load-bearing authority concept);
The Consumer Answer (Apple HIG, Windows UX Guidelines, GNOME HIG, KDE HIG, Material Design);
The Developer Answer (Unix philosophy, Emacs, Vim, Visual Studio Code, Git, Cargo, npm, pip);
The Operator (the unfilled category);
A Short History of Operator-Facing Computing (Sketchpad, NLS, MOCR, Alto, Macintosh, BTRON, HyperCard, OpenDoc, GNOME Bonobo, SCADA, PLCs, ARINC 661, ISA-101, NUREG-0700, IEC 62366, ISO 9241, ASM Consortium);
Why the Consumer Answer Fails the Operator (five structural failure modes);
Why the Developer Answer Also Fails (four structural failure modes);
The Operator Population Today (aerospace, medical, industrial, defense and intelligence, legal and regulatory, financial markets);
A Scorecard of Audience Requirements (10-row table across consumer, developer, operator);
The Gap That Remains;
Out of Scope (defers the substantive solution, the language substrate, and the worked vertical to the trilogy);
Conclusion.

References:
61 references across Reference (58) and Related Post (3) categories.
All inline-linked per project style.
A113, A115, and A117 cited via post_url as the deferred follow-ups.
No internal research cited.
A research agent verified the operator-specific references (ISA-101, ASM Consortium, IEC 62366, ISO 9241, NUREG-0700, ARINC 661, glass cockpit, SCADA, HITL, ergonomics, alarm fatigue) and the audience-contrast sources (Apple HIG, Windows UX, GNOME HIG, KDE HIG, Unix philosophy).

### Launch and Recovery Systems for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-01-launch_and_recovery_systems_for_fixed_wing_uavs.markdown`
**Topic**: Runway-independent launch and recovery for fixed-wing UAVs, worked outward from the energy-and-stroke master variable.
**Article Number**: A116
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-01 (26 references; 478 lines)

Standalone aerospace article and the runway-independent companion to A114.
Establishes the energy-and-stroke master variable, where launch must add and recovery must remove a kinetic energy fixed by mass and flying speed and the g-load rises as the stroke shrinks, and works through
launch by catapult (bungee, pneumatic, hydraulic, rail), winch and aerotow, booster, and zero-length launch;
recovery by net and cable (Skyhook), arrested landing, parachute and airbag, belly skid, and high-alpha braking (deep stall, cobra braking as a routine procedure, and perched landing);
wind and environment;
the acceleration limit;
failure and abort modes, with the fail-safe principle and a flight-termination or controlled-ditch option;
matching launch to recovery with real-UAV anchors (ScanEagle, RQ-7 Shadow, RQ-21 Blackjack);
airframe implications;
a worked numeric example;
and a fully declared Out of Scope.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
References A114 (Runway Sizing for Fixed-Wing UAVs) and A112 (Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass) via post_url.
26 references across Reference, Related Post, and Research categories.
478 lines.

### Human Spaceflight Ground Systems as an Illustrative Vertical for a Hypermedia Desktop — Published

**File**: `_posts/2026-05-25-human_spaceflight_ground_systems_as_illustrative_vertical.markdown`
**Topic**: Vertical-specific follow-up to A113 and A115. Walks through human spaceflight ground systems in the Apollo lineage, lampshaded as an illustrative example vertical with explicit extrapolation guidance to modern crewed launch and on-orbit operations. Includes a Day-in-the-Launch-Operator's-Workflow walkthrough and six verified Keleusma code samples for the load-bearing claims.
**Article Number**: A117
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-25 (40 references; 1,944 lines)

Sections covered include
The Apollo Reference (MOCR, RTCC on IBM System/360 Model 75, LCC and Firing Rooms, MSFN, NASCOM, Flight and Mission Rules, simulators, recovery, the flight directors and Apollo 13);
Extrapolation to Modern Requirements (CCSDS, Commercial Crew Program, ISS Multilateral Coordination, Artemis and Human Landing System, FAA Part 450, NPR 7150.2 and NASA-STD-8719.13 and NPR 8705.2, ITAR);
The Hypermedia Object Model in Launch Operations (six commitments with Apollo-to-hypermedia mapping table);
Engineering Commitments in Launch Operations (five commitments with five Keleusma code samples and a mapping table);
The Ten-Layer Architectural Sketch in Launch Operations (full table inheriting A115 verdicts and clarifying each layer's launch role);
A Day in the Launch Operator's Workflow (eleven scenes from pre-launch shift report through post-flight review);
Trust and Provenance;
Certification and Regulatory Posture;
Why This Vertical Is a Good Illustration (and where it is hard);
Risks and Open Questions;
Out of Scope (link store schema, certification path, contractor selection deferred to future posts);
Conclusion.

Six verified Keleusma code samples in `tmp/a117/`:
01_countdown_sequencer.kel (loop main compiles to 260 bytes);
02_telemetry_alarm.kel (Proprietary -> displayable bucket, returns 1);
03_abort_decision.kel (Sensitive -> typed outcome, returns 2);
04_abort_decision_reject.kel (same without declassify, compile-time reject);
05_mission_rules.kel (const data registry, returns 300);
06_signed_flight_rules.kel (signed entry function compiles to 232 bytes).

References:
40 references across Reference (37), Related Post (2), and Research (1) categories.
All inline-linked per project style.
A113 and A115 cited via post_url.
Apollo-era and contemporary primary sources verified by a parallel research agent.
No internal Keleusma research cited.

### Keleusma as a Substrate for a Real-Time Hypermedia Desktop — Published

**File**: `_posts/2026-05-24-keleusma_as_substrate_for_real_time_hypermedia_desktop.markdown`
**Topic**: Follow-up to A113. Maps Keleusma V0.2.0 capabilities and the public V0.5+ roadmap onto A113's six structural commitments of the hypermedia object model, the five engineering commitments for real-time hypermedia composition, and the ten-layer architectural sketch. Vertical-agnostic by design; the vertical-specific treatment is deferred to a separate follow-up.
**Article Number**: A115
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-24 (45 references; 1,701 lines)

Analytical follow-up to A113. Sections covered include
What Keleusma Provides at Version 0.2.0;
The Six Structural Commitments of the Hypermedia Object Model;
The Five Engineering Commitments for Real-Time Hypermedia;
Mapping the Ten-Layer Architectural Sketch (ten verdicts: two strong fits, five partial fits, three mismatches);
What Keleusma Uniquely Provides (verified totality, verified WCET/WCMU, language-level IFC);
What Keleusma Does Not Provide (mature ecosystem, general-purpose breadth, authoring tooling);
The Asymmetry and Its Implication;
The Roadmap Path (V0.3.0 self-hosted compiler through V0.5.x interval-graph refinement);
What Would Need to Be Built;
Risks and Open Questions;
Out of Scope (vertical choice, detailed link store design, certification path all deferred to separate posts);
Conclusion.

Five illustrative Keleusma code samples verified against the installed keleusma 0.2.0 CLI:
01_typed_part.kel (Citation struct, runs and returns 42);
02_handler_loop.kel (loop main with yield, compiles to 228-byte bytecode);
03_ifc_sanitiser.kel (classify/declassify sanitiser pattern, runs and returns 200);
04_ifc_reject.kel (same without declassify, verifier rejects at compile time);
05_preallocated.kel (const data block, runs and returns 20).

All examples in `tmp/a115/`.

References:
45 references across Reference (38), Related Post (5), and Research (1) categories.
Inline citations throughout per project style.
A113, A107, A109, A110, A111 cited via post_url.
No internal Keleusma research material cited; only public Keleusma artefacts (README, crates.io, docs.rs, GitHub).

**Remaining Work**:
Human review of analytical claims and the Keleusma-to-BTRON mapping.
Confirm publication date and assign final timestamp.
Update memory once published.

### Runway Sizing for Fixed-Wing UAVs — Published

**File**: `_posts/2026-05-31-runway_sizing_for_fixed_wing_uavs.markdown`
**Topic**: Sizing runways for small and medium fixed-wing UAVs, worked outward from the master speed variable.
**Article Number**: A114
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-31 (28 references; 548 lines)

Standalone aerospace article.
Establishes the squared-speed master variable, where stall and liftoff speed are set by wing loading, air density, and the maximum lift coefficient, and works outward through explicit square-cube size-scaling;
the level ground roll;
paved versus dirt surfaces;
inclined and ski-jump runways;
wind, crosswind, and landing-gear ground handling;
orientation with an Earth-rotation dismissal;
density altitude;
obstacle clearance, margins, and an in-scope abort and stopping-margin note;
the landing roll and ground effect;
width and the lateral dimension (touchdown dispersion and guidance lateral error);
full-runway versus single-phase operation anchored to real UAVs (ScanEagle, RQ-7 Shadow, MQ-9 Reaper);
planform and airframe implications (conventional, delta, flying wing);
a worked numeric example;
and lighting, reflectors, and markings (optional versus required).
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
References A112 (Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass) via post_url.
28 references across Reference, Related Post, and Research categories.
548 lines.

### BTRON, Hypermedia, and the Real-Time Desktop — Published

**File**: `_posts/2026-05-23-btron_hypermedia_and_real_time_desktop.markdown`
**Topic**: Historical and analytical treatment of the BTRON proposition, the asymmetry between successful real-time operating systems and failed hypermedia desktops, a contemporary diagnosis of the market gap, and a concrete architectural sketch for a 2026 successor.
**Article Number**: A113
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-23 (149 references; 4,166 lines)

Standalone operating-systems history and philosophy article.
Surveys the BTRON proposition under the TRON Project (Sakamura, 1984),
why BTRON failed (Super 301 trade dispute listed in April 1989 and withdrawn the following month after USTR site visit, hardware program collapse, ecosystem shortfall, conceptual depth tax, vendor entrenchment),
the histories of relevant real-time operating systems (VRTX 1981, pSOS ~1982, VxWorks 1987, QNX 1980 in the Ottawa area of Canada, QNX Photon, Green Hills INTEGRITY, FreeRTOS, Zephyr, RTEMS, NuttX, μITRON, T-Kernel, seL4, Genode, Redox OS),
the histories of hypermedia systems (Memex, NLS in 1968 funded by ARPA/NASA/USAF, Project Xanadu, Smalltalk, NoteCards developed at Xerox PARC starting 1984 by Trigg/Halasz/Moran, HyperCard 1987-2004, OLE 2 in the 1992-1993 window, Cairo, OpenDoc framework 1994 and CyberDog 1996, Bonobo, KParts, Lotus/HCL Notes ~42M peak seats with ~140M cumulative licenses, SharePoint, World Wide Web with the Berners-Lee 1989 CERN proposal, Roam, Logseq, Obsidian, Notion, Coda, Jupyter, Observable, Solid, Beaker last released December 2020, Automerge, Yjs, ActivityPub),
the six structural commitments of the hypermedia object model,
where the model wins on merit and where it is clearly the wrong fit,
the real-time-plus-hypermedia special case,
who is served by the mass-market file-and-application model,
who would benefit from a real-time hypermedia desktop,
the web browser as substrate analysis,
a super-browser as modern realization,
why the gap persists (four-component diagnosis),
and viable entry strategies (vertical-first, internal-program, acquisition-path, sponsored-standards).
References A93 (Fast-Moving Versus Mission-Critical Engineering) and A86 (Mission Command Management Style) via post_url.
76 references across 4 categories (Book, Reference, Related Post, Research).
2,219 lines.

**Research Pass (2026-05-31)**:
Four parallel research agents verified factual claims across TRON Project history,
real-time operating systems history, hypermedia systems history,
and contemporary tools / regulated-industry incumbents / standards.
Corrections applied:
ITRON deployment softened from "several billion per year" to "cumulative billions";
Super 301 chronology refined (listed April 1989, withdrawn May 1989);
Real Object / Virtual Object pairing introduced for BTRON's hypermedia model;
TRON character code Unicode comparison added with concrete dates (Cho Kanji 1999 ~180K characters vs Unicode 4.1 in 2005);
RTOS first-generation date range corrected from "1970s-early 1980s" to "early 1980s";
QNX origin location corrected from "Ottawa" to "Ottawa area of Canada" with University of Waterloo founder attribution;
QNX Photon deprecation since 2014 disclosed;
QNX vehicle deployment updated to "more than 275 million" with BlackBerry press release citation;
FreeRTOS "most widely deployed" softened to "among the most widely deployed";
FreeRTOS AWS 2017 transaction reframed as stewardship transfer with AWS blog citation;
seL4 superlative softened to "most extensive functional-correctness proof of a general-purpose OS kernel";
Redox OS alpha status disclosed;
NLS funding expanded to ARPA/NASA/USAF;
NoteCards authorship attributed (Trigg, Halasz, Moran);
HyperCard "several million users" softened to "millions";
OLE 2 release window clarified (1992-1993);
OpenDoc shipping clarified (framework 1994, CyberDog 1996);
Lotus Notes seat counts corrected from "hundreds of millions" to ~42M active / ~140M cumulative;
SharePoint primitives clarified (files and lists);
Beaker reframed from "dormant" to "discontinued after December 2020";
ARP4754B successor noted.
URL fixes:
ref_cho_kanji (Wikipedia 404, replaced with chokanji.com);
ref_super_301 (replaced with Section 301 stable URL);
ref_vrtx (replaced with Versatile_Real-Time_Executive);
ref_qnx_neutrino (replaced with qnx.software);
ref_qnx_photon (replaced with QNX_Photon Wikipedia entry).
New references added with inline citations:
ARP4754A; TRON character encoding;
IEEE Milestone for TRON RTOS family;
USTR 25 May 1989 statement;
Mars Pathfinder priority inversion engineering note;
BlackBerry QNX 275M vehicles press release;
Amazon FreeRTOS launch blog post;
seL4 SOSP 2009 paper;
Engelbart and English 1968 AFIPS paper;
Halasz 1988 NoteCards retrospective in CACM;
Berners-Lee 1989 CERN proposal;
Kleppmann and colleagues local-first essay (Onward 2019).
URL verification:
all new URLs return HTTP 200 except ACM Digital Library and chokanji.com which return 403 to curl due to bot detection but are valid human-accessible URLs.

**Expansion Pass (2026-05-31)**:
Four additional parallel research agents covered alternative research operating systems (Plan 9, Inferno, Self, Oberon, JX),
the artificial intelligence and large language model angle (retrieval-augmented generation, Model Context Protocol, structured output, Coalition for Content Provenance and Authenticity, agent provenance research),
architectural building blocks for a 2026 hypermedia operating system (Automerge, Yjs, Loro, InterPlanetary File System, Iroh, Hypercore, seL4, Genode, Capsicum, Cap'n Proto, WebAssembly Component Model, Servo, Chromium Embedded Framework, WebKit, ProseMirror, TipTap, Lexical, JetBrains Meta Programming System, CodeMirror, Skia, Cairo Graphics, HarfBuzz, FreeType),
and regulated-industry incumbents (DOORS, Polarion, Windchill, ENOVIA, Vault, Gotham, Foundry, Relativity, iManage).
Seven new sections added:
"Other Radical Unifications" (Plan 9, Inferno, Self/Morphic, Oberon, JX as alternative unification approaches);
"Performance and Latency Engineering for Composed Documents" (bounded handler execution time, deadline propagation, preallocated resources, spatial and temporal isolation, admission control);
"The Artificial Intelligence Synergy" (RAG, MCP, structured output, C2PA, regulatory provenance requirements, PROV-AGENT, HyperAgents workshop);
"How the Incumbents Compare" (comparison table across the nine incumbents on typed parts, typed links, in-place composition, provenance, and local-first persistence);
"Coexistence with the File and Application World" (file system bridges, import handlers, lossy export, gradual adoption);
"A Concrete Architectural Sketch" (ten layers from verified microkernel through user-facing shell, naming production-quality open-source components for each);
"Out of Scope" (explicit declaration of seven topics deferred to follow-up articles).
56 new authoritative sources added with inline citations.
Reference count rose from 76 to 132 across Book (2), Reference (108), Related Post (2), and Research (20) categories.
Line count rose from 2,219 to 3,408.

**Completion Pass (2026-05-31)**:
Three additional parallel research agents covered Lifestreams (Gelernter and Freeman, Yale, mid-1990s),
Sutherland's Sketchpad (1963) and Alan Kay's Dynabook (1968-1972),
and the contemporary Tools for Thought movement (Matuschak, Nielsen, Appleton, Bret Victor, Rheingold, Future of Coding, Hyperlink Academy).
Seven new sections and inline additions added:
Sketchpad paragraph in hypermedia history;
Dynabook paragraph in hypermedia history;
Lifestreams paragraph in hypermedia history;
Tools for Thought paragraph in hypermedia history (with cultural framing);
"A Day in the Workflow, an Aerospace Requirements Example" between Architectural Sketch and Conclusion;
"Epistemic State of the Argument" between Workflow and Conclusion (distinguishing factual, structural, and strategic claims);
"Reader's Next Steps" after Out of Scope (TRON Forum, seL4 community, Genode community, local-first community, Solid working group, HyperAgents workshop, Tools for Thought community);
"Glossary" after Reader's Next Steps (defined-terms section for 12 key concepts including capability-based security, compound document, conflict-free replicated data type, content-addressable storage, handler, hypermedia object model, link store, microkernel, provenance, real-time operating system, separation kernel, transclusion, typed link, typed part).
17 new authoritative sources added with inline citations:
Mirror Worlds (Gelernter 1991 Oxford);
Tools for Thought (Rheingold 1985 MIT Press);
Lifestreams CHI 1996 paper;
Lifestreams SIGMOD 1996 paper;
Lifestreams Yale project page;
Sutherland's Sketchpad Cambridge-hosted thesis;
Sketchpad Wikipedia;
Kay and Goldberg Personal Dynamic Media 1977;
Dynabook Wikipedia;
Matuschak and Nielsen 2019 ttft essay;
Matuschak personal site;
Evergreen Notes;
Maggie Appleton personal site;
Appleton Garden History essay;
Bret Victor Magic Ink essay;
Future of Coding;
Hyperlink Academy.
Reference count rose from 132 to 149.
Line count rose from 3,408 to 4,166.
All anchors verified used and defined; style scan clean.
URL verification: all HTTP 200 except documented OUP 202 (project memory) and ACM DL 403 (bot detection, valid for human readers).

**Remaining Work**:
Human review of the four completion-pass additions (Lifestreams, Sketchpad/Dynabook, Tools for Thought, user journey walkthrough, epistemic state, next steps, glossary).
Confirm publication date and assign final timestamp.
Update Software Versions section if any is desired (currently omitted to match A98-class analytical-article convention).
Update memory once published.

### Solana sBPF Assembly Example — Pre-Release Candidate

**File**: `solana_sbpf_assembly_example.markdown`
**Topic**: Writing Solana programs using sBPF assembly with the sbpf standalone toolchain
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

Completely rewritten from a partial draft with x86 assembly and clang build.rs
to use the correct sBPF instruction set and the sbpf standalone toolchain.
Covers the sBPF virtual machine, registers and memory layout, instruction set overview,
toolchain installation, project creation, a Hello World program using `.rodata` section,
`lddw` address loading, and `.equ` named constants for all non-trivial literals.
Building and deploying with sbpf tool,
and the current state of mixed Rust and assembly projects.
Three experimental paths for mixed projects documented (nightly inline asm, sbpf-linker, build.rs).
Includes a theoretical linked Rust and assembly example
using the Solana SDK's Clang and llvm-ar in a `build.rs` script.
The Rust entrypoint passes a string to an sBPF assembly logging subroutine via C FFI.
Both assembly files use `.equ` named constants with inline comments.
Nine limitations documented.
Eleven references across two categories (Reference, Research).
No article number assigned. Not slotted for publication.

**Remaining Work**:
Human verification by building and deploying the Hello World program with the sbpf tool.
Verify the linked Rust and assembly example compiles with cargo build-sbf.
Fill in Software Versions TODO placeholders.
Verify assembly code executes correctly on a local test validator.
Assign article number and publication date when ready.

### Android Development on FreeBSD — Pre-Release Candidate

**File**: `android_development_on_freebsd.markdown`
**Topic**: Android SDK and NDK development on FreeBSD using Kotlin, Rust, and the Linuxulator
**Completion**: ~90%
**Publication Sensibility**: Medium
**Status**: Pre-Release Candidate

Completely rewritten from 2017 content (FreeBSD 11, SDK 25, NDK r13b)
to modern toolchain (FreeBSD 14, SDK 35, NDK r28).
Covers Linuxulator setup with Rocky Linux 9 base,
Android SDK and NDK installation via sdkmanager,
ADB setup with native FreeBSD port,
Kotlin SDK development with standard XML layouts,
Rust NDK development with JNI integration via cargo-ndk,
and emulator feasibility discussion.
Sample app is a native Android port of the CLMM calculator (A91)
with Kotlin UI and Rust math exposed through JNI.
No article number assigned. Not slotted for publication.
Ten references across four categories (Android, FreeBSD, Related Post, Rust).

**Remaining Work**:
Human verification on FreeBSD hardware.
Fill in Software Versions TODO placeholders.
Test build pipeline on FreeBSD 14 with Linuxulator.
Assign article number and publication date when ready.

### Android Unit Testing — Pre-Release Candidate

**File**: `android_unit_testing.markdown`
**Topic**: Android unit testing across Kotlin, Robolectric, instrumented, and NDK layers
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

Completely rewritten from 2017 content (SDK 25, Java 1.8, ApplicationTestCase)
to modern toolchain (SDK 35, JDK 17, Kotlin 2.1.0, AGP 8.9.0).
Test subject is the CLMM calculator app with both Kotlin and Rust native implementations.
Covers test dependencies (JUnit 4, AndroidX Test, Robolectric, MockK, Espresso),
local unit tests with pure logic and Robolectric Activity tests,
mocking with MockK object declarations,
instrumented tests with Espresso,
and NDK unit testing with Rust cargo test, JNI boundary testing, and GoogleTest for C++.
Running Tests section provides Gradle task table. Code Coverage section covers JaCoCo, Kover, and cargo-llvm-cov.
Seven limitations documented. MathJax enabled for CLMM reserve formulas.
References Android FreeBSD article and CLMM Mathematics (A91) via post_url.
No article number assigned. Not slotted for publication.
Twelve references across four categories (Android, Reference, Related Post, Rust).

**Remaining Work**:
Human verification of test code against actual Android project.
Fill in Software Versions TODO placeholders.
Verify floating-point test expected values against CLMM calculator.
Verify JNI function name conventions for NativeBridgeTest.
Assign article number and publication date when ready.
Android FreeBSD article and CLMM Mathematics (A91) must be published first.

### Authenticating a Phoenix JSON API with Guardian and Ueberauth — Pre-Release Candidate

**File**: `phoenix_json_api_authentication_with_guardian.markdown`
**Topic**: Phoenix/Elixir JSON API authentication with Guardian JWT and Ueberauth identity strategy
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

Completely rewritten from 2016 content (Phoenix 1.1.4, Elixir 1.2.3, Guardian ~0.10.0, Comeonin ~2.1)
to modern toolchain (Phoenix 1.7+, Guardian ~> 2.3, bcrypt_elixir ~> 3.0, Ueberauth ~> 0.10).
MemoApi example application with user registration, JWT-based login, and protected memo CRUD.
Uses context modules, Guardian implementation module pattern, plug pipeline, and error handler.
Ueberauth identity strategy integration with callback pattern example.
Testing the API section with curl commands and expected JSON responses.
Seven limitations documented.
References published article A27 "A Shell Script for Working with Phoenix JSON APIs" via post_url.
No article number assigned. Not slotted for publication.
Eleven references across four categories (Elixir, Phoenix, Reference, Related Post).

**Remaining Work**:
Human verification by building and running the MemoApi project.
Fill in Software Versions TODO placeholders.
Verify Guardian secret key generation command.
Verify Ueberauth identity strategy plug compatibility.
Assign article number and publication date when ready.

### Getting Started with Claude Code on FreeBSD — Pre-Release Candidate

**File**: `claude_code_getting_started_on_freebsd.markdown`
**Topic**: Installing and configuring Claude Code on FreeBSD
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

New article covering Claude Code installation on FreeBSD via the misc/claude-code port, binary packages, and npm.
Documents shebang fix, ripgrep configuration, and a Hello World exercise
that generates a curses-based system dashboard using only FreeBSD base system tools.
Limitations section documents unsupported platform status and known issues.
References the companion Getting Started with Claude Code post (A74) via post_url.
Twelve references across four categories (Claude, FreeBSD, GitHub, Related Post).
No article number assigned. Not slotted for publication.

**Remaining Work**:
Human verification on FreeBSD hardware.
Fill in Software Versions output.
Test the Hello World prompt on FreeBSD.
Verify shebang fix and ripgrep configuration.
Assign article number and publication date when ready.

### Getting Started with Claude Code Over SSH — Pre-Release Candidate

**File**: `claude_code_getting_started_over_ssh.markdown`
**Topic**: Using Claude Code locally to work on remote machines over SSH
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

New article covering the use of Claude Code on a local workstation
to execute commands on remote machines via SSH.
Introduces SSH fundamentals for readers unfamiliar with the protocol.
Walks through Ed25519 key generation, public key copying, SSH agent setup,
host configuration, and verification.
Documents remote execution patterns using Claude Code's Bash tool
including single commands, multi-command chains, and scp file transfer.
Covers timeout configuration for long-running remote operations.
Detailed agent forwarding section covers mechanism, configuration,
verification, Claude Code usage, security considerations,
and ProxyJump as a safer alternative for untrusted intermediate hosts.
Briefly discusses Claude Code Desktop SSH as an alternative
that requires Claude Code on the remote machine.
Hello World section demonstrates end-to-end remote workflow
with OS detection, C code generation, scp transfer, and remote compilation.
References companion Getting Started posts for macOS (A74), FreeBSD, and OpenBSD via post_url.
Eleven references across three categories (Claude, Reference, Related Post).
No article number assigned. Not slotted for publication.

**Remaining Work**:
Human verification with an actual remote SSH target.
Fill in Software Versions output.
Test the Hello World prompt against a remote machine.
Verify agent forwarding with `ssh -A myserver "ssh-add -l"`.
Verify timeout configuration format.
Assign article number and publication date when ready.

### Getting Started with Claude Code on OpenBSD — Pre-Release Candidate

**File**: `claude_code_getting_started_on_openbsd.markdown`
**Topic**: Installing and configuring Claude Code on OpenBSD
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

New article covering Claude Code installation on OpenBSD via npm,
the only viable installation path on the platform.
No port or package exists for Claude Code on OpenBSD.
Documents bash installation and `/bin/bash` symlink requirement,
ripgrep configuration via `USE_BUILTIN_RIPGREP` setting,
and a critical warning against running the native installer or `claude install`
which downloads an incompatible Linux binary and breaks npm installations.
Hello World exercise generates a curses-based system dashboard using only OpenBSD base system tools.
Limitations section is more extensive than the FreeBSD article
due to the absence of a dedicated port and the removal of the Linux compatibility layer.
References the companion Getting Started with Claude Code post (A74)
and the FreeBSD article via post_url.
Twelve references across four categories (Claude, GitHub, OpenBSD, Related Post).
No article number assigned. Not slotted for publication.

**Remaining Work**:
Human verification on OpenBSD hardware.
Fill in Software Versions output.
Test the Hello World prompt on OpenBSD.
Verify bash symlink and ripgrep configuration.
Verify that `doas pkg_add node` installs a supported Node.js version (18-24).
Assign article number and publication date when ready.

### Getting Started with Solana Using Rust and Pinocchio — Pre-Release Candidate

**File**: `solana_with_rust_and_pinocchio_getting_started.markdown`
**Topic**: Building a Solana program with Pinocchio zero-dependency library, mirroring the Anchor companion article (A65)
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

New article mirroring A65 "Getting Started with Solana Using Rust and Anchor"
but using the Pinocchio zero-dependency library instead of Anchor.
Same key pegboard toy contract that stores a public key and encrypted private key on-chain.
Covers Pinocchio project setup, manual account validation, raw byte parsing,
PDA creation via CPI to System Program, Mollusk test harness,
building with cargo build-sbf, and deployment to local test validator.
Comparison table with Anchor implementation (A65).
Nine limitations documented.
References published article A65 via post_url.
No article number assigned. Not slotted for publication.
Twelve references across three categories (Reference, Related Post, Research).

**Remaining Work**:
Human verification by building and deploying the program with cargo build-sbf.
Fill in Software Versions TODO placeholders.
Run Mollusk tests against compiled BPF binary.
Verify Pinocchio crate versions are current.
Assign article number and publication date when ready.

### Template

**File**: `template.markdown`
**Topic**: Post template for new articles
**Completion**: N/A
**Publication Sensibility**: N/A

This is a template file, not a draft. It provides the standard structure for new posts.

## Summary

Ten files exist in `_drafts/`. One is a template.
No release candidates remain.
No new drafts remain.
No stubs remain.
A79 through A144 have been published.

**Tier 1: Publishable with moderate effort.**
No drafts remain in Tier 1.
A126 (communications and the command-and-control data link), A127 (structures and the flight envelope), A128 (aerobatics as costed trajectories, the synthesis capstone of the extension set), A129 (an aerobatic maneuver reference catalog, the reference companion to A128), A130 (payload and mission systems), and A131 (the regulatory and operations layer) are the six extensions beyond the core fixed-wing-UAV arc; the series and its extensions are now complete, with no further extensions flagged.
A132 through A144 are the SBIR/STTR practitioner playbook, a complete thirteen-article series in the new business/funding/sbir category covering the United States SBIR and STTR programs from orientation, agency survey, eligibility and registration, finding a topic and reading a solicitation, the Phase I proposal, Phase II and the commercialization plan, Phase III and the valley of death, data rights and intellectual property, the money, after the award, strategy, and international analogs through a worked-campaign capstone that reuses the fixed-wing UAV; the series is now complete, all thirteen of thirteen articles published.

The drafts fall into four tiers when assessed for salvageability with contemporary tooling.

**Pre-Release Candidates.**
Android Development on FreeBSD has been fully rewritten with modern tooling
and is awaiting verification on FreeBSD hardware before publication.
Android Unit Testing has been fully rewritten with contemporary AndroidX Test, Robolectric, MockK,
and NDK testing coverage and is awaiting verification against an actual Android project.
Getting Started with Claude Code on FreeBSD covers installation via ports, packages, and npm
and is awaiting verification on FreeBSD hardware before publication.
Getting Started with Claude Code on OpenBSD covers npm-only installation with bash and ripgrep configuration
and is awaiting verification on OpenBSD hardware before publication.
Getting Started with Claude Code Over SSH covers using Claude Code locally to work on remote machines via SSH
and is awaiting verification with a remote SSH target.
Authenticating a Phoenix JSON API with Guardian and Ueberauth has been fully rewritten
from 2016 Phoenix 1.1/Guardian 0.10 to modern Phoenix 1.7+/Guardian 2.x
and is awaiting verification by building and running the MemoApi project.
Solana sBPF Assembly Example has been fully rewritten from a partial draft with x86 assembly
to use the correct sBPF ISA and the sbpf standalone toolchain,
revised with `.rodata` section usage and a theoretical linked Rust and assembly example,
and is awaiting verification by building and deploying with the sbpf tool.
Getting Started with Solana Using Rust and Pinocchio mirrors the Anchor companion article (A65)
using the Pinocchio zero-dependency library
and is awaiting verification by building and running Mollusk tests.

**No stubs remain.**
All article-numbered drafts have been elevated to release candidate status.

## Candidate Future Post Topics

The following table lists on-brand post ideas organized by thematic cluster.
Topics are selected to align with the blog's established strengths in systems programming, applied mathematics, unconventional toolchains, and AI-assisted development.

| Topic | Categories | Rationale | Builds On |
|-------|------------|-----------|-----------|
| Formal Verification with TLA+ | math development | Formal methods for distributed protocol design. Bridges the mathematical rigor thread with systems engineering. | Writing Proofs (A79), Radioactive Half-Life Demurrage Cryptocurrency Coin (A88) |
| Lean 4 and Automated Theorem Proving | math ai development | Interactive theorem prover with growing LLM integration. Connects proofs, AI, and software verification. | Writing Proofs (A79) |
| Property-Based Testing in Rust | rust development | QuickCheck-style testing as lightweight formal methods. Practical bridge between proofs and everyday engineering. | no_std Rust series, AMM Mathematics (A67) |
| RISC-V Assembly Getting Started | asm embedded development | Emerging instruction set architecture for embedded and open hardware. Natural extension of ARM and x86 assembly posts. | ASM Playdate Development, UNIX ARM Assembler |
| Rust on RISC-V Microcontrollers | rust embedded no_std | no_std Rust on RISC-V hardware. Combines two active threads in the blog. | no_std Rust series, Radioactive Half-Life Demurrage Cryptocurrency Coin (A88) |
| WebAssembly Component Model | rust wasm development | WASI and the component model as the next step beyond basic WASM. | WASM on Jekyll (A73) |
| ~~CLMM Mathematics and Calculator~~ | ~~crypto defi math~~ | ~~Concentrated liquidity mathematics with interactive widget. Direct sequel to AMM article.~~ | ~~Covered by Concentrated Liquidity Market Maker Mathematics (A91)~~ |
| ~~Solana sBPF Assembly~~ | ~~crypto development asm~~ | ~~Writing Solana programs at the assembly level. Unique low-level blockchain content.~~ | ~~Covered by Solana sBPF Assembly Example draft~~ |
| Statistics for A/B Testing | math development | Applied statistics for software engineers. Practical extension of the statistics reference. | Probability and Statistics Reference (A80) |
| ~~Orbital Mechanics Primer~~ | ~~math science~~ | ~~Applied physics with MathJax. Evergreen STEM content.~~ | ~~Covered by Introduction to Space Studies (A90)~~ |
| Context Engineering Patterns Cookbook | ai ai-tools development | Practical patterns distilled from the survey article. Shorter, actionable format. | Context Engineering (A78), A75-A77 series |
| Evaluating AI-Generated Code | ai development | Metrics and methods for assessing agent output quality. Addresses the evaluation gap identified in A78. | A75-A78 series |
| FreeBSD Jails for Development Environments | freebsd development | Container-like isolation using FreeBSD jails. Updates the FreeBSD systems thread with modern practices. | FreeBSD series (A1-A40 era) |
| Shell Scripting with Modern CLI Tools | sh unix development | fd, ripgrep, jq, fzf as modern replacements for traditional UNIX tools. | Shell scripting series |
| Game AI with Minimax and Alpha-Beta Pruning | gamedev math ai | Classical game AI algorithms with proofs of optimality. Bridges game development and mathematical rigor. | Chess/Go game theory series |
| Playdate Game Physics | gamedev playdate math c | Physics simulation on constrained hardware. Applied mathematics on embedded game platform. | Playdate series, Trigonometry (A14) |
| Observable Signatures of Competitive Civilizations | science philosophy | Unselected A101 candidate. What observational evidence would distinguish competitive expansion from natural astrophysical processes. Connects Dyson sphere searches and SETI to the competitive framework. | A98, A99, A100, A101 |
| The Survival Bottleneck Engineering Roadmap | science philosophy | Unselected A101 candidate. Detailed engineering requirements for the Type 0 to Type I transition. Covered adequately in A100 but could be expanded with specific technology roadmaps and quantitative risk reduction strategies. | A100 |
| Self-Replicating Technology Engineering | science philosophy | Unselected A101 candidate. Detailed engineering analysis of self-replicating machines and spacecraft. Von Neumann universal constructor, error correction, gray goo risk quantification. Implementation-focused rather than strategic. | A100, A101 |
| Governance Coherence Deep Dive | science philosophy | Unselected A101 candidate. Full treatment of governance coherence half-life, myth-structure transition, and institutional degradation at cosmic scales. A92 already covers this but the competitive context from A98-A101 would add depth. | A87, A89, A92, A100 |
| Economics of Competitive Expansion | science philosophy | Unselected A101 candidate. Resource allocation, opportunity costs, and economic optimization under competitive expansion imperatives. Interesting but secondary to physical feasibility questions. | A98, A100 |
| First Contact Protocols Under Competitive Assumptions | science philosophy | Unselected A101 candidate. Decision-theoretic analysis of first contact under the competitive framework. Premature without knowing whether force projection is physically feasible, which A101 now addresses. | A98, A99, A101 |
