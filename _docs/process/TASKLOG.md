# Task Log

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

Current task state and verification log. This file is the shared source of truth for the active unit of work.

---

## Current Task

**Name**: Publish A112 (Fixed-wing LWPLA + fiberglass prototyping)
**Status**: Complete
**Started**: 2026-05-30

## Success Criteria

- [x] A109 "A Verifiable Control Kernel in Keleusma for a Truthful-Machine Architecture" written (companion to A108).
- [x] All code listings verified with keleusma 0.2.1; shown outputs are actual outputs.
- [x] Verified example scripts authored in `tmp/a108/` (gitignored scratch).
- [x] Honest scope sections (kernel only). Resume-driver version difference between 0.2.0 and 0.2.1 documented accurately.
- [x] Reference integrity confirmed (9/9, zero missing, zero unused).
- [x] Publication dependency on A108 recorded.
- [x] Draft summary synced.

## Task Breakdown

| ID | Task | Status | Verification |
|----|------|--------|--------------|
| A109-P1-T1 | Review Keleusma V0.2.0 against the A108 design | Complete | Read CHANGELOG and guide chapters. Asserted fit for the controller and governance kernel, non-fit for neural and prover layers. |
| A109-P1-T2 | Draft and verify example skeletons | Complete | Seven `.kel` files in `tmp/a108/`. Three `fn` examples run (64, 1, 42), two rejected at compile time as intended. The `yield` controller runs under a locally built 0.2.1 (`Int(3)`) and the `loop` controller drives continuously; on 0.2.0 both are verifier-checked via `keleusma compile`. |
| A109-P1-T3 | Write companion article | Complete | Tutorial-genre article with verified listings and outputs, scope sections, 9 references. |
| A109-P1-T4 | Reconcile to 0.2.1 resume driver | Complete | Built keleusma 0.2.1 from working tree, confirmed resume works, updated article and process files from compile-only framing to a real 0.2.1 run while noting 0.2.0 lacks the driver. |

## Notes

- Next available article number: A113.
- 0 release candidates.
- 0 new drafts. A108 through A112 published.
- 0 stubs.
- Eight pre-release candidate drafts remain awaiting human verification.
- A108 is a standalone AI/philosophy article. A109 is its Keleusma implementation companion. The resume driver landed in keleusma 0.2.1 (verified against a working-tree build); the released 0.2.0 lacks it. A109 targets 0.2.1 and documents the 0.2.0 difference.

## History

| Date | Change |
|------|--------|
| 2026-02-07 | A0: Knowledge graph, communication protocol, CLAUDE.md, git strategy, article numbering (A1-A74), and asset organization established. |
| 2026-02-07 | A75: "Bidirectional Agentic Workflow" drafted and published (2026-02-06 date). |
| 2026-02-07 | A76: "Markdown as a Specification Language for Agentic Workflows" drafted and published (2026-02-08 date). |
| 2026-02-07 | A77: "LLM Knowledge Graphs" drafted and published (2026-02-07 date, 20 references). |
| 2026-02-08 | A78: "The State of Context Engineering in Early 2026" drafted (30 references) and published (2026-02-09 date). Draft summary created. 16 candidate topics added. |
| 2026-02-08 | A79: "Writing Proofs" drafted (15 references). A80: "Probability and Statistics Reference" drafted (9 references). Both elevated to release candidates. |
| 2026-02-08 | A81: "Magic Cards as a Model of Virtual Goods" drafted (9 references). A82: "Introduction to Astronomy" drafted (8 references). |
| 2026-02-08 | A83: "Safe Embedded Functional Control DSL" drafted (12 references, later revised to 16). A84: "LLM Mad Libs Experiment" drafted (10 references). A85: "The AI Apocalypse Will Be Polite" drafted (11 references). |
| 2026-02-09 | A79-A85 elevated to release candidates. A79 published (2026-02-10 date). A80-A85 release announcements generated. A86 and A87 cataloged as stubs. |
| 2026-02-14 | A88-P1: "The Half-Life Coin" researched and rewritten (13 references). Draft summary synced. |
| 2026-02-14 | A88-P2: Renamed to "Radioactive Half-Life Demurrage Cryptocurrency Coin." Five sections revised. Verification Licensing added. RISC Zero reference added (14 total). Filename convention documented. A86/A87 outlines expanded by human. A89 stub added. |
| 2026-02-14 | A86-P1: "Mission Command Management Style" researched and written (14 references). TASKLOG streamlined. |
| 2026-02-14 | A87-P1: "Telemeritocracy" researched and written (11 references). References A86 via post_url. Draft summary synced (13 files, 3 RCs, 1 stub). |
| 2026-02-15 | A89-P1: "Cryptotelemeritocracy" researched and written (15 references). References A87 via post_url. Draft summary synced (13 files, 4 RCs, 0 stubs). |
| 2026-02-15 | A90-P1: "Introduction to Space Studies" researched and written (18 references). References A82 via post_url. Draft summary synced (13 files, 5 RCs, 0 stubs). |
| 2026-02-14 | A89-P2: "Cryptotelemeritocracy" revised from cryptographic to cryptocratic framing (14 references). Three-layer model with candidate pool, arbitrator powers, strength classifications. Draft summary synced. |
| 2026-02-15 | A89-P3: "Cryptotelemeritocracy" expanded with theory additions (19 references). Oversight vs executive configurations, telos amendment, counter-espionage properties section. Draft summary synced. |
| 2026-02-15 | A91-P1: "Concentrated Liquidity Market Maker Mathematics" researched and written (6 references). Calculator rewritten from JS to Rust WASM. Android FreeBSD drafts combined. Draft summary synced (12 files, 6 RCs, 0 stubs). |
| 2026-02-16 | A91-P2: Renamed exported WASM function from `clmm_calculator_init` to `inject_ui`. Human added index.html local testing example and serve instructions. |
| 2026-02-16 | A0-P3: "Android Development on FreeBSD" modernized from 2017 to 2026 toolchain. A91 WASM assets committed. Draft summary synced. |
| 2026-02-16 | A0-P4: "Getting Started with Claude Code on FreeBSD" drafted (12 references). Ports, packages, npm installation. Hello World curses demo. Draft summary synced. |
| 2026-02-16 | A0-P5: "Getting Started with Claude Code on OpenBSD" drafted (12 references). npm-only installation, bash/ripgrep config, Hello World curses demo. Draft summary synced. |
| 2026-02-16 | A0-P6: "Getting Started with Claude Code Over SSH" drafted (10 references). SSH fundamentals, key auth, remote execution via Bash tool, Desktop SSH. Draft summary synced. |
| 2026-02-16 | A0-P7: "Getting Started with Claude Code Over SSH" revised with agent forwarding section (11 references). Security considerations, ProxyJump alternative. Draft summary synced. |
| 2026-02-16 | A0-P8: "Android Unit Testing" modernized from 2017 stub to contemporary AndroidX Test (12 references). CLMM calculator test subject, Kotlin and Rust implementations, NDK testing section. Draft summary synced. |
| 2026-02-16 | A0-P9: "Phoenix JSON API Authentication with Guardian and Ueberauth" modernized from 2016 to contemporary Phoenix 1.7+/Guardian 2.x (11 references). File renamed. Draft summary synced. |
| 2026-02-16 | A0-P10: "Solana sBPF Assembly Example" finished from partial draft. Rewritten with correct sBPF ISA and sbpf toolchain (9 references). Mixed Rust/assembly state documented. File renamed. Draft summary synced. |
| 2026-02-16 | A0-P11: "Getting Started with Solana Using Rust and Pinocchio" drafted (12 references). Mirrors A65 key pegboard with Pinocchio. Mollusk tests, comparison table. Draft summary synced. |
| 2026-02-16 | A0-P12: "Solana sBPF Assembly Example" revised with .rodata section and linked Rust+ASM object file example (11 references). build.rs with Solana SDK Clang. Draft summary synced. |
| 2026-02-16 | A0-P13: "Solana sBPF Assembly Example" revised with .equ named constants in main.s and log_hello.s. All non-0/1/-1 literals replaced. Draft summary synced. |
| 2026-02-17 | A92-P1: "Cryptotelemeritocracy for Space Exploitation" researched and written (13 references). References A89 and A90 via post_url. Draft summary synced (17 files, 7 RCs, 0 stubs). |
| 2026-02-17 | A92-P2: "Cryptotelemeritocracy for Space Exploitation" revised per subsection notes. Birch Planet, Venus water sourcing, MESSENGER attribution, EROI, reverse conglomerate excess pledges, spinoff independence, telos primacy, memetic governance, MathJax equations. 16 references. Draft summary synced. |
| 2026-02-17 | A92-P3: "Cryptotelemeritocracy for Space Exploitation" revised. Introduction foreshadow, telos hierarchy (13 objectives, 4 categories), Kardashev governance shift, mass driver physics, Mercury cannibalization inflection point, corrected spinoff equations, spinoff shedding reframe, Governance Coherence Half-Life. Draft summary synced. |
| 2026-02-17 | A92-P4: "Cryptotelemeritocracy for Space Exploitation" revised. Corrected $\Delta V_{share}$ formula. Arbitrator profit independence. Latency-meaning-narrative cascade. GCH expanded with glottochronology, punctuated equilibrium, operational 50% divergence. Intergalactic phase reframed as myth-structure to superstition. 4 new references (20 total). Draft summary synced. |
| 2026-02-17 | A92-P5: "Cryptotelemeritocracy for Space Exploitation" corrected Birch Planet cross-reference from objective 8 to objective 6. |
| 2026-02-17 | A86-P2: "Mission Command Management Style" published (2026-02-18 date). Draft summary synced (16 files, 6 RCs, 0 stubs). |
| 2026-02-18 | A87-P2: "Telemeritocracy" published (2026-02-19 date). Fixed post_url hyphen/underscore mismatch in A87 and A89. Software versions date updated. Draft summary synced (15 files, 5 RCs, 0 stubs). |
| 2026-02-18 | A93-P1: "The Cost of Failure Spectrum" researched and written (17 references). Date sync convention documented in POST_STRUCTURE.md. Draft summary synced (16 files, 6 RCs, 0 stubs). |
| 2026-02-18 | A93-P2: Retitled to "FMCG Versus Mission-Critical Engineering." Terminology shifted from "commercial software engineering" to "FMCG Engineering" with justification. File renamed. Draft summary synced. |
| 2026-02-18 | A93-P3: Retitled to "Fast-Moving Versus Mission-Critical Engineering." FMCG spelled out on first use. Conventional FMCG explained with toilet paper analogy. File renamed. Draft summary synced. |
| 2026-02-18 | A93-P4: All acronyms spelled out on first use. IEC/ISO priming sentence added. RTCA identified for DO-178C. MVP, DORA, IT, MCAS, STAMP spelled out. UI replaced with full phrase. |
| 2026-02-18 | A94-P1: "Long-Form Writing in the Age of Large Language Models" researched and written (60 references). Historical sweep from pre-history through contemporary era with interleaved math and computing milestones. Four historical conclusions with epistemological framing. Draft summary synced (17 files, 7 RCs, 0 stubs). |
| 2026-02-19 | A88-P3: "Radioactive Half-Life Demurrage Cryptocurrency Coin" published (2026-02-19 date). Knowledge graph updated with no-limit writing policies. Draft summary synced (16 files, 6 RCs, 0 stubs). |
| 2026-02-19 | A88-P4: Release announcement for A88 generated and reported in REVERSE_PROMPT.md. |
| 2026-02-19 | A95-P1: "Human Evolution and the Great Filter" researched and written (67 references). References A82 and A90 via post_url. Draft summary synced (17 files, 7 RCs, 0 stubs). |
| 2026-02-19 | A95-P2: Revised. Thesis section renamed to "Weighing the Evidence." Opisthokonta row added for plant split (34 rows, 69 references). Parentheticals inlined throughout. Acronyms spelled out on first use. |
| 2026-02-18 | A96-P1: "History of Rocketplanes" researched and written (50 references). ~30 vehicles from 1928 Lippisch Ente to 2024 Dawn Mk-II Aurora. Technology transfer and espionage narrative. References A90 via post_url. Draft summary synced (18 files, 8 RCs, 0 stubs). |
| 2026-02-19 | A97-P1: "What Does the United States Space Force Do?" researched and written (42 references). History, justification, and ten mission areas. Air Force independence parallel and fighter pilot culture documented. Draft summary synced (19 files, 9 RCs, 0 stubs). |
| 2026-02-19 | A89-P4: "Cryptotelemeritocracy" published (2026-02-20 date). Human corrected date and renamed file. A92 post_url reference corrected to 2026-02-20. Draft summary synced (18 files, 8 RCs, 0 stubs). |
| 2026-02-20 | A90-P2: "Introduction to Space Studies" published (2026-02-21 date). All publication order dependencies resolved. Draft summary synced (17 files, 7 RCs, 0 stubs). |
| 2026-02-22 | A91-P3: "Concentrated Liquidity Market Maker Mathematics" published (2026-02-22 date). Draft summary synced (16 files, 6 RCs, 0 stubs). |
| 2026-02-22 | A92-P6: "Cryptotelemeritocracy for Space Exploitation" published (2026-02-23 date). Draft summary synced (15 files, 5 RCs, 0 stubs). |
| 2026-02-25 | A93-P5, A94-P2: "Fast-Moving Versus Mission-Critical Engineering" published (2026-02-24 date) and "Long-Form Writing in the Age of Large Language Models" published (2026-02-25 date). Dates not updated per prompt instructions. Draft summary synced (13 files, 3 RCs, 0 stubs). |
| 2026-02-26 | A95-P3: "Human Evolution and the Great Filter" published (2026-02-26 date). Draft summary synced (12 files, 2 RCs, 0 stubs). |
| 2026-02-27 | A96-P2: "History of Rocketplanes" published (2026-02-27 date). Draft summary synced (11 files, 1 RC, 0 stubs). |
| 2026-02-27 | A97-P2: "What Does the United States Space Force Do?" published (2026-02-28 date). Draft summary synced (10 files, 0 RCs, 0 stubs). |
| 2026-02-28 | A98-P1: "The Fermi Paradox" researched and written (63 references). References A82, A90, A95 via post_url. Draft summary synced (11 files, 1 RC, 0 stubs). |
| 2026-02-28 | A98-P2: Retitled to "Causality and First-Mover Advantage in Galactic Colonization." File renamed. Incorrect conclusion replaced with causality-based thesis. Intergalactic sterilization and warfare sections added with equations. Conclusion revised. Draft summary synced. |
| 2026-02-28 | A98-P3: Warfare section rewritten with pseudo-realtime observation, offensive hidden information, defensive pseudo-realtime preparations. Colonizing the Light Cone subsection added with sterilize-until-resistance model. Conclusion revised. Draft summary synced. |
| 2026-03-01 | A98-P4: Retitled to "Causality and First-Mover Advantage in Lightcone-Based Competitive Intergalactic Colonization." File renamed. SMBH sterilization engine with Penrose process and Blandford-Znajek equations. Intergalactic topography with cosmic web, filaments, voids, Laniakea. Seven new references (70 total). Draft summary synced. |
| 2026-03-01 | A98-P5: Comprehensive revision per external LLM review. Thesis preview expanded. Carter Hard Step model cited. Oxygen bottleneck softened. False precision reduced. Engineering caveats added. M-dwarf flares, gravitational lensing, heat sinks, beam divergence added. Grabby model dependencies and first-mover assumptions stated. 2d gap as spacetime property. Conclusion revised with synthesis, conditional framing, critique anticipation, stagnation risk. 67 references. Draft summary synced. |
| 2026-03-01 | A98-P6: "Causality and First-Mover Advantage in Lightcone-Based Competitive Intergalactic Colonization" published (2026-03-01 date). Local Group galaxy table added (10 galaxies). Draft summary synced (10 files, 0 RCs, 0 stubs). |
| 2026-03-01 | A99-P1: "Tactical and Strategic Assessment of the Local Galactic Neighborhood" researched and written (82 references). Continuation of A98. Draft summary synced (11 files, 1 RC, 0 stubs). |
| 2026-03-01 | A99-P2, A100-P1: A99 revised with information warfare section (93 references, 2,185 lines). A100 "Roadmap to a Competitive Type III Civilization" researched and written (54 references, 1,832 lines). Draft summary synced (12 files, 2 RCs, 0 stubs). |
| 2026-03-01 | A100-P2, A101-P1: A100 revised with A87/A89/A92 governance conclusions and intergalactic transit engineering section (67 references, 2,232 lines). A101 "The Physics of Intergalactic Force Projection" researched and written (40 references, 1,681 lines). Draft summary synced (13 files, 3 RCs, 0 stubs). |
| 2026-03-02 | A99-P3: A99 revised per external LLM feedback. Assumptions box, capability envelope reframe, energy scaling, asymmetric singularity ratio, dark forest instability derivation, logistic plateau scenarios, civilizational failure modes, ranked strategic priority table, epistemic tone calibrated (96 references, 2,809 lines). Draft summary synced. |
| 2026-03-02 | A99-P4: A99 revised per second round of external LLM feedback. Mathematical formalization (capability scaling equation, instability condition, three growth regimes). Scope constraints (selection pressure bounded, ionization clarified, Sedov-Taylor refined). Consolidated equation block and operational synthesis section added. JavaScript article number printing added to all 110 articles. (96 references, 3,146 lines). Draft summary synced. |
| 2026-03-02 | A99-P5: "Tactical and Strategic Assessment of the Local Galactic Neighborhood" published (2026-03-02 date). M87 jet divergence hardened, radiator ratio corrected. A100/A101 post_url references updated. Draft summary synced (12 files, 2 RCs, 0 stubs). |
| 2026-03-02 | A102-P1: "Von Neumann Probes" researched and written (68 references, 2,011 lines). A99 release announcement regenerated from template. Draft summary synced (13 files, 2 RCs, 0 stubs). |
| 2026-03-03 | A100-P3: "Roadmap to a Competitive Type III Civilization" published (2026-03-03 date). A101/A102 post_url references updated. Draft summary synced (12 files, 1 RC, 0 stubs). |
| 2026-03-04 | A101-P2: "The Physics of Intergalactic Force Projection" revised per external LLM feedback. Probe reliability, detection realism, accretion constraints, symmetric swarm equilibria, galactic geometry, colonization/sterilization distinction, numerical anchors. 75 references (up from 40). 2,622 lines (up from 1,682). A102 post_url updated to 2026-03-04. Draft summary synced. |
| 2026-03-04 | A101-P3: "The Physics of Intergalactic Force Projection" published (2026-03-04 date, 2,856 lines, 105 refs). 30 new references added across 12 topic areas. Draft summary synced. |
| 2026-03-05 | A102-P2: "Von Neumann Probes" revised per 16 external LLM feedback items and published (2026-03-05 date, 2,597 lines, 102 refs). 34 new references added. Future Reading section added (13 entries). Draft summary synced. |
| 2026-03-06 | A103-P1: "The Error Correction Recursion Problem" researched and written (2,164 lines, 75 refs). Left unpublished per human pilot instruction. Draft summary synced. |
| 2026-03-07 | A103-P2: "The Error Correction Recursion Problem" revised per 17 external LLM feedback items. 17 new references integrated from research agent. Draft summary synced. (2,712 lines, 95 refs). |
| 2026-03-08 | A104-P1: "Steampunk and Analog Electronics for Von Neumann Probe Control" researched and written (1,867 lines, 50 refs). Draft summary synced. |
| 2026-03-09 | A104-P2: "Steampunk and Analog Electronics for Von Neumann Probe Control" revised per 11 external LLM feedback items. 28 new references integrated from two research agents. Draft summary synced. (2,784 lines, 78 refs). |
| 2026-03-10 | A105-P1: "Neuromorphic and 3D Printable CPUs for Autonomous Probe Computing" researched and written (3,014 lines, 67 refs). Two research agents deployed. Draft summary synced. |
| 2026-03-11 | A106-P1: "Two-Stage Flying Delta Wing Vehicles for Civil and National Security Applications" researched and written (2,423 lines, 93 refs). Two research agents deployed. Draft summary synced. |
| 2026-03-12 | A103-P3: "The Error Correction Recursion Problem" published (2026-03-12 date, 2,712 lines, 95 refs). A104 and A105 post_url references updated. Draft summary synced. |
| 2026-03-12 | A104/A105/A106 batch publication: "Steampunk and Analog Electronics" (2026-03-08, 2,784 lines, 78 refs), "Neuromorphic and 3D Printable CPUs" (2026-03-10, 3,014 lines, 67 refs), "Two-Stage Flying Delta Wing Vehicles" (2026-03-12, 2,423 lines, 93 refs). Draft summary synced. |
| 2026-03-14 | A107-P1: "Getting Started with Keleusma 0.1.1" researched and written (928 lines, 27 refs). Local repo explored, all examples verified. Draft summary synced. |
| 2026-03-14 | A107-P2: "Getting Started with Keleusma 0.1.1" published (2026-03-14 date). Draft summary synced. |
| 2026-05-30 | A108-P1: "A Speculative Neurosymbolic Blueprint for Truthful, Scientific, and Abstaining Machines" researched and written (963 lines, 56 refs). Exhaustive literature survey with all citations verified. Standalone AI/philosophy article. References A94 and A103 via post_url. Draft summary synced. |
| 2026-05-30 | A109-P1: "A Verifiable Control Kernel in Keleusma for a Truthful-Machine Architecture" written, companion to A108. Reviewed Keleusma V0.2.0 and asserted fit for the control/governance kernel. Seven example scripts authored and verified in tmp/a108 (three run, two rejected at compile time as intended, two pass the verifier). 9 references. References A108 and A107 via post_url; A109 depends on A108 publishing first. Draft summary synced. |
| 2026-05-30 | A109-P2: Keleusma syntax highlighting. Added a Rouge lexer to the Keleusma repo (branch feat-rouge-highlighter, editors/rouge/) and vendored it into the blog at _plugins/keleusma_lexer.rb. Added Gemfile, Gemfile.lock, and a GitHub Actions Pages workflow (.github/workflows/jekyll.yml) so plugins run on deploy; added a .nd CSS rule for information-flow labels. Switched A109 code fences from rust to keleusma. Verified rendering via Kramdown+Rouge. ACTION NEEDED: set the repo Pages source to GitHub Actions for live highlighting. |
| 2026-05-30 | A107 highlighting fix: A107 kept its Keleusma scripts in untagged (unhighlighted) fences and its genuine Rust host code in rust fences. Tagged the 21 Keleusma script blocks as keleusma, left the 10 Rust blocks and the REPL session untouched. |
| 2026-05-30 | Blog highlighter made dual-version. The blog covers both V0.1.1 (A107) and V0.2.0 (A109) Keleusma, so _plugins/keleusma_lexer.rb is now a blog-maintained lexer that recognizes legacy V0.1.x types (i64, f64, String) in addition to the V0.2.x types. It intentionally diverges from the canonical Keleusma-repo lexer, which is left untouched. All seven types render as Keyword.Type. |
| 2026-05-30 | A108-P2, A109-P2: Published A108 "A Speculative Neurosymbolic Blueprint for Truthful, Scientific, and Abstaining Machines" (2026-05-26 date) and A109 "A Verifiable Control Kernel in Keleusma for a Truthful-Machine Architecture" (2026-05-27 date). A109 post_url to A108 reconciled to 2026-05-26. Verified full site build (post_url resolution and Keleusma highlighting confirmed in output). _publish.sh failed under macOS BSD sed (invalid character range in its date regex), so the git mv was done manually. Draft summary synced. |
| 2026-05-30 | Build hardening: replaced the github-pages gem with a lean modern Jekyll stack (jekyll 4, rouge 3.30, jekyll-feed, jekyll-sitemap), regenerated a multi-platform Gemfile.lock, fixed the failing Actions build, and set the Pages source to GitHub Actions. Result: 0 open Dependabot alerts and live Keleusma highlighting on A107 and A109. |
| 2026-05-30 | A110-P1: "Getting Started with Keleusma 0.2.0" researched and written. All listings tested against keleusma 0.2.0; embedding example built and run against the crates.io 0.2.0 crate; verifier rejections demonstrated. Tested scripts and embedding project in tmp/a110 (gitignored). 20 references, inline plus a References section. References A107 and A109 via post_url; links the 40-chapter guide. Draft summary synced. |
| 2026-05-30 | A110-P2: Published A110 "Getting Started with Keleusma 0.2.0" (2026-05-28 date). Verified full site build (post_url to A107/A109 resolve, keleusma and rust fences highlight). Committed and pushed; deployed via the Actions build. Draft summary synced. |
| 2026-05-30 | Software Versions consistency: added an "OS and Version" section (`uname -vm`) to A109 and A110, the recent code-running articles that omitted it. A107 left unchanged (its kernel build date postdates the article, so the current uname would be anachronistic); A108 runs no code. |
| 2026-05-30 | A111-P1: "Information-Flow Control, A Deep Dive with Keleusma" researched and written. IFC theory verified against seven canonical papers; all Keleusma listings tested on 0.2.0 (implicit-flow rejection is the centerpiece). Tested scripts in tmp/a111 (gitignored). 15 references inline plus a References section. References A109 and A110 via post_url. Software Versions includes OS and Version. Draft summary synced. |
| 2026-05-30 | A111-P2: Published A111 "Information-Flow Control, A Deep Dive with Keleusma" (2026-05-29 date). Verified full site build (post_url to A109/A110 resolve, keleusma fences highlight). Committed and pushed; deployed via the Actions build. Draft summary synced. |
| 2026-05-30 | Scratch policy: confined all scratch to project-local tmp/ (recorded as a memory preference); removed stray system /tmp scratch from this session. |
| 2026-05-30 | A112-P1: "Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass" researched and written. Standalone aerospace/fabrication article. Topic researched against verified sources (LW-PLA foaming filament, fiberglass lamination, low-Reynolds-number aerodynamics, square-cube scaling, printed RC airframes). Covers the 1-2 m wingspan sweet spot and a final section on other unmanned vehicles. MathJax enabled. 16 references inline plus a References section. No runnable code, so no OS and Version section. Draft summary synced. |
| 2026-05-30 | A112-P2: Published A112 "Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass" (2026-05-30 date). Standalone article, no post_url cross-links. Verified full site build (renders, MathJax included, on index). Committed and pushed; deployed via the Actions build. Draft summary synced. |
| 2026-05-30 | A112-P3: Revised the published A112 to fold in review gaps. Added a Thermal Caveat (PLA softens ~55-60C, LW-PLA HT and the glass skin as mitigations, plus a layer-anisotropy note), a "Where This Method Fits Among the Alternatives" section (foam board for earliest iteration, molds at volume, continuous-fiber printing), a "When to Glass, and When to Fly It Bare" fidelity-ladder section, and a clarification that chord Reynolds number and airspeed are the real variables with wingspan a proxy mediated by aspect ratio. Added 6 references (22 total). Build verified; committed and pushed. |
| 2026-05-31 | A112-P4: Added a "When to Switch Techniques" section closing the off-ramp gap. States the conditions where fiberglassed LW-PLA stops being appropriate (scale past ~2-3 m, high loads or speed, sustained heat, immersion, production volume) and names the alternatives without detail (built-up spar-and-rib with iron-on film covering, vacuum-bagged composite over foam or in a tool, molded carbon-composite primary structure for large UAVs, molds for volume). Reconciled the "extends both directions" passage to forward-reference it. Added 3 references (25 total). Build verified; committed and pushed. |
| 2026-05-31 | A112-P5: Addressed the remaining gaps. Added a "Stiffness and Flutter" subsection (aeroelasticity, torsional rigidity GJ, no honest flutter plug-and-chug), broadened the thermal caveat to UV and moisture aging, added a turbulator note to the low-Reynolds bound, a square-cube equation block, a "Putting Numbers to It" plug-and-chug section (lift, stall speed, wing loading, WCL, with a worked 1.5 m example), surface-prep and equipment/cost notes in the build method, a "Working Safely with Epoxy and Glass" section, a "Hard Landings and Repair" section (failure modes, reprint vs scarf patch, reseal porous core), and an explicit "Out of Scope" section (propulsion/electronics integration, regulatory thresholds). MathJax equations throughout. Added 7 references (32 total). Build verified; committed and pushed. |
| 2026-05-31 | A112-P6: Added a brief center-of-gravity and control-surfaces note to "Putting Numbers to It" (CG ahead of the aerodynamic center, ~quarter to third of mean aerodynamic chord, control-surface types and rough sizing), self-declaring a full stability-and-control treatment out of scope. Added 2 references (34 total). Build verified; committed and pushed. |
