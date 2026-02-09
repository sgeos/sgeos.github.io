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

### Solana sBPF Assembly Example

**File**: `solana_bpf_asm_example.markdown`
**Topic**: Writing Solana programs using sBPF assembly
**Completion**: ~40%
**Publication Sensibility**: High

The most publishable draft.
The topic is recent (December 2025), and the sBPF instruction set and Solana runtime remain actively developed.
Working assembly source and a `build.rs` build script are present.
Contemporary tooling (Solana CLI 2.x, Agave validator) would be used for Software Versions.

**Remaining Work**:
Replace placeholder problem description with explanatory prose covering the sBPF instruction set, Solana's runtime model, and why assembly-level programming is useful.
Add categories (space-separated).
Verify that the assembly code and build script compile and deploy against the current Solana toolchain.
Draft a complete Instructions section.
Add a References section.

### Statistics Reference — Release Candidate

**File**: `statistics.markdown`
**Article**: A80, "Probability and Statistics Reference"
**Topic**: Probability and statistics reference covering distributions, hypothesis testing, confidence intervals, and sample size determination
**Completion**: ~95%
**Publication Sensibility**: High
**Status**: Release Candidate

Rewritten from a formula sheet into a complete reference article.
Explanatory prose added for every section.
Notation table, Software Versions block, summary, future reading, and references are all present.
MathJax corrected throughout.
Nine references across four categories (Book, Reference, Tool).
Additional topics added beyond the original draft: Normal PDF, Poisson distribution, Bayes' theorem, Central Limit Theorem, t-test, confidence intervals for means, and sample size determination.

**Remaining Work**:
Human review and local MathJax rendering verification before publication.

### CLMM Calculator

**File**: `clmm.markdown`
**Topic**: Concentrated Liquidity Market Maker calculator with interactive HTML/JavaScript widget
**Completion**: ~35%
**Publication Sensibility**: Medium-High

The interactive calculator widget is functional and pairs naturally with the published Constant Product AMM Mathematics article (A67).
Concentrated liquidity remains the dominant market maker design in decentralized finance.
The JavaScript implementation requires no framework migration.

**Remaining Work**:
Draft the CLMM mathematical explanation covering tick spacing, price ranges, and liquidity concentration.
Provide DeFi context explaining how concentrated liquidity differs from constant product designs.
Add categories (space-separated).
Replace placeholder prose sections with complete narrative.
Add a Software Versions block.
Add a References section citing the Uniswap v3 whitepaper and related literature.

### Half-Life Coin

**File**: `halflife_coin.markdown`
**Topic**: Cryptocurrency protocol design with 100-year half-life decay, RISC-V computing, hierarchical reaping
**Completion**: ~70%
**Publication Sensibility**: Medium

A speculative protocol design piece with substantial written content.
The topic is niche but intellectually interesting.
No specific tooling dependencies exist since the post is a design document.

**Remaining Work**:
Remove duplicate sections (Bespoke Reliability and Miner's Incentive each appear twice).
Fix categories to use space-separated format.
Add Software Versions block and article number comment.
Draft missing transitions and polish existing prose.
Assess whether the speculative nature warrants framing as a thought experiment rather than a proposal.

### Introduction to Space Studies

**File**: `introduction-to-space-studies.markdown`
**Topic**: Orbital parameters, rocket thrust equations, electromagnetic wavelength-frequency relationships
**Completion**: ~30%
**Publication Sensibility**: Medium

Physics content is evergreen and requires no tooling updates.
The mathematical foundation for orbital mechanics and electromagnetic theory exists in the draft.
MathJax rendering is already enabled.

**Remaining Work**:
Replace all placeholder variables (currently $x$ throughout) with correct physical variable definitions.
Draft instructional prose explaining each equation set and its physical significance.
Expand coverage to provide a coherent introduction rather than isolated formula groups.
Add a Software Versions block and a References section.

### Magic Cards as a Model of Virtual Goods — Release Candidate

**File**: `magic_cards_as_a_model_of_virtual_goods.markdown`
**Article**: A81, "Magic Cards as a Model of Virtual Goods"
**Topic**: Magic card anatomy as a physical data structure and model for virtual goods economics
**Completion**: ~95%
**Publication Sensibility**: High
**Status**: Release Candidate

Rewritten from a stub into a full article.
Covers card anatomy (name, mana cost, art, type line, set symbol, rules text, power/toughness, collector information, flavor text),
virtual goods economics (near-zero marginal cost, R&D cost structure, designed scarcity, chase vs bulk, RMT),
and analysis (cards as APIs, printing as distribution platform, rarity as dual-purpose tool, value asymmetry).
Links to A66 "Metagaming as a Framework for Real-Life Strategy" as a companion article.
Nine references across five categories (Blog, Book, Industry, Reference, Tool).
Rust data structures were removed from scope in favor of the economics focus.

**Remaining Work**:
Human review and URL verification before publication.

### Building Android APKs on FreeBSD

**File**: `building_android_apks_on_freebsd.markdown`
**Topic**: Building Android APKs on FreeBSD using the Linux emulation layer
**Completion**: ~85%
**Publication Sensibility**: Low-Medium

The original draft targets Android SDK 25 and FreeBSD 11 (2017).
If salvaged, contemporary tooling would be Android SDK 35+ and FreeBSD 14.
The Linux emulation layer approach remains valid on FreeBSD and is still documented in the FreeBSD Handbook.
However, the audience for Android development on FreeBSD is small.
Nearly identical to the NDK variant and should be consolidated into a single post if pursued.

**Remaining Work**:
Consolidate with the NDK variant into a single post.
Update all SDK and NDK version references to contemporary releases.
Fix the Software Versions block (date and uname fields are swapped).
Verify that the Linux emulation approach still works with current Android build tools.
Polish prose.

### Android NDK Builds on FreeBSD

**File**: `android_ndk_builds_on_freebsd.markdown`
**Topic**: Android NDK builds on FreeBSD using Linux emulation
**Completion**: ~80%
**Publication Sensibility**: Low-Medium

Same assessment as the APK variant.
Starts with "TODO: Rework this post."
Should be merged with the APK draft into a single consolidated article covering both SDK and NDK workflows on FreeBSD 14.

**Remaining Work**:
Merge content into the APK variant (or vice versa).
Update NDK references from r13b to current NDK r27+.
Fix Software Versions formatting.
Draft unified narrative covering both build workflows.

### Android Unit Testing

**File**: `android_unit_testing.markdown`
**Topic**: Android unit testing with Gradle, emulators, and CI
**Completion**: ~30%
**Publication Sensibility**: Low

The original targets Android Studio 2.2 and SDK 25 (2017).
Android testing has evolved significantly.
Contemporary tooling would use AndroidX Test, Jetpack Compose testing, and Android Studio current.
The existing code snippets would need near-complete replacement.

**Remaining Work**:
Rewrite around contemporary AndroidX Test and Compose UI testing frameworks.
Replace placeholder problem description and instructions with complete prose.
Update emulator setup to use current Android Emulator and device profiles.
The scope of rewriting approaches writing from scratch.

### Authenticating a Phoenix JSON API with Guardian

**File**: `authenticating-a-phoenix-json-api-with-guardian.markdown`
**Topic**: Phoenix/Elixir JSON API authentication with Guardian
**Completion**: ~75%
**Publication Sensibility**: Low

The original targets Phoenix 1.1.4 and Elixir 1.2.3 (2016).
Both Phoenix and Guardian have had multiple breaking API changes since then.
Contemporary tooling would use Phoenix 1.7+, Elixir 1.17+, and Guardian 2.x.
Phoenix 1.7 introduced verified routes and a significantly different project structure.
The existing code would need substantial rewriting to match current conventions.

**Remaining Work**:
Rewrite all Phoenix and Guardian code for Phoenix 1.7+ and Guardian 2.x.
Complete the stub "Adding Authorization" section.
Fix broken tests rather than leaving them as exercises.
Update project structure to reflect current `mix phx.new` output.
The rewrite effort is significant given the cumulative breaking changes.

### Introduction to Astronomy — Release Candidate

**File**: `introduction-to-astronomy.markdown`
**Article**: A82, "Introduction to Astronomy"
**Topic**: Introduction to astronomy covering the solar system, galactic and intergalactic features, qualitative concepts, and mathematical formulas
**Completion**: ~95%
**Publication Sensibility**: High
**Status**: Release Candidate

Rewritten from an empty stub into a full article.
Starts at the Sun and works outward through the solar system,
covering all eight planets with their notable moons,
the asteroid belt with notable asteroids (Ceres, Vesta, Pallas, Hygiea),
the Kuiper Belt (Pluto, Charon, Eris, Makemake, Haumea), and the Oort Cloud.
Extends to galactic features (Milky Way, nebulae, star clusters, black holes)
and intergalactic features (galaxy types, Local Group, clusters, superclusters, observable universe).
Surveys broad qualitative concepts (electromagnetic spectrum, Hertzsprung-Russell diagram, stellar evolution, cosmic distance ladder, light as a time machine).
Collects eight mathematical formulas with MathJax (Kepler's laws, Newton's gravitation, inverse square law, Stefan-Boltzmann, Wien's law, Doppler effect and redshift, parallax, magnitude system).
Eight references from official sources (NASA, ESA, IAU, OpenStax, Hubble).

**Remaining Work**:
Human review, URL verification, and local MathJax rendering check before publication.

### Writing Proofs — Release Candidate

**File**: `writing-proofs.markdown`
**Article**: A79, "Writing Proofs"
**Topic**: Mathematical proof techniques, software verification, and formal verification in the age of agentic workflows
**Completion**: ~95%
**Publication Sensibility**: High
**Status**: Release Candidate

Rewritten from an empty stub into a full article.
Covers five proof techniques (direct, contradiction, contrapositive, induction, constructive) with worked examples.
Extends into software verification (Hoare logic, Curry-Howard, TLA+, CompCert, Lean 4, seL4)
and agentic formal verification (AlphaProof, Hilbert, APOLLO, Safe).
Fifteen references across five categories (Blog, Book, Industry, Research, Tool).

**Remaining Work**:
Human review, URL verification, and local MathJax rendering check before publication.

### Safe Embedded Functional Control DSL

**File**: `safe_embedded_functional_control_dsl.markdown`
**Article**: A83, "Safe Embedded Functional Control DSL"
**Topic**: Draft specification for a safe, provable, hot-updatable functional DSL for aerospace drone control logic
**Completion**: ~25%
**Publication Sensibility**: Medium

A draft specification proposing a functional DSL for safety-critical embedded control.
Covers seven design goals (safety, formal analyzability, embeddability, hot updates, functional syntax, concurrency safety, performance),
eight language features (pure functions, pipelines, pattern matching, multi-headed functions, ADTs, type system, hot updates, concurrency semantics),
and runtime architecture (stack-based VM, memory model, host integration, formal guarantees).
Includes an illustrative sensor event example.
No external research has been incorporated yet.
The article captures design notes for future development.

**Remaining Work**:
Research related work (Lua, Erlang, SCADE, Lustre, other embedded DSLs).
Add references.
Flesh out formal semantics.
Evaluate against real control system requirements.
Consider certification pathways (DO-178C, MISRA).

### LLM Mad Libs Experiment

**File**: `llm_mad_libs_experiment.markdown`
**Article**: A84, "LLM Mad Libs Experiment"
**Topic**: Mad Libs experiment demonstrating LLM sycophantic compliance and instruction-over-context behavior
**Completion**: ~30%
**Publication Sensibility**: Medium-High

A draft article describing a multi-session Mad Libs experiment.
Session A generates a dark-themed template with bracketed placeholders.
Session B fills in the template with cheerful words under instruction, producing tonally dissonant output.
A third prompt variant asks for context-aware fills, revealing that the LLM understands the dark theme but overrides it when instructed.
Observations cover sycophantic compliance, template structure as meaning carrier, instruction-over-pattern behavior, and implications for prompt engineering.
No external research has been incorporated yet.

**Remaining Work**:
Research related work on LLM sycophancy, instruction following, and alignment.
Add references.
Include the Step 3 output (logical fill) as a concrete example.
Expand the Implications section.

### Template

**File**: `template.markdown`
**Topic**: Post template for new articles
**Completion**: N/A
**Publication Sensibility**: N/A

This is a template file, not a draft. It provides the standard structure for new posts.

## Summary

Fifteen files exist in `_drafts/`. One is a template.
Four drafts have been elevated to release candidate status.

The drafts fall into four tiers when assessed for salvageability with contemporary tooling.

**Release Candidates.**
Writing Proofs (A79), the Probability and Statistics Reference (A80),
Magic Cards as a Model of Virtual Goods (A81),
and Introduction to Astronomy (A82)
have been fully drafted and are awaiting human review before publication.

**Tier 1: Publishable with moderate effort.**
The Solana sBPF assembly example is the most publishable remaining draft.
It is recent, topical, and has working code.

**Tier 2: Publishable with significant effort.**
The LLM Mad Libs Experiment (A84) has a complete experiment narrative but needs research, references, and a Step 3 output example.
The Safe Embedded Functional Control DSL (A83) has a coherent specification structure but needs research, references, and expanded content.
The CLMM calculator has a functional interactive widget that pairs with the published Constant Product AMM article.
The half-life coin draft has substantial written content but needs structural repair.
The space studies draft has sound conceptual foundations but requires extensive new writing.

**Tier 3: Salvageable but niche.**
The two Android/FreeBSD drafts should be consolidated into one post and updated to FreeBSD 14 and current Android tooling.
The audience for Android development on FreeBSD is small, making the effort-to-reach ratio unfavorable.

**Tier 4: Rewrite or abandon.**
The Android unit testing and Phoenix/Guardian drafts would require near-complete rewrites to use contemporary frameworks.

## Candidate Future Post Topics

The following table lists on-brand post ideas organized by thematic cluster.
Topics are selected to align with the blog's established strengths in systems programming, applied mathematics, unconventional toolchains, and AI-assisted development.

| Topic | Categories | Rationale | Builds On |
|-------|------------|-----------|-----------|
| Formal Verification with TLA+ | math development | Formal methods for distributed protocol design. Bridges the mathematical rigor thread with systems engineering. | Writing Proofs (A79), half-life coin draft |
| Lean 4 and Automated Theorem Proving | math ai development | Interactive theorem prover with growing LLM integration. Connects proofs, AI, and software verification. | Writing Proofs (A79) |
| Property-Based Testing in Rust | rust development | QuickCheck-style testing as lightweight formal methods. Practical bridge between proofs and everyday engineering. | no_std Rust series, AMM Mathematics (A67) |
| RISC-V Assembly Getting Started | asm embedded development | Emerging instruction set architecture for embedded and open hardware. Natural extension of ARM and x86 assembly posts. | ASM Playdate Development, UNIX ARM Assembler |
| Rust on RISC-V Microcontrollers | rust embedded no_std | no_std Rust on RISC-V hardware. Combines two active threads in the blog. | no_std Rust series, half-life coin draft |
| WebAssembly Component Model | rust wasm development | WASI and the component model as the next step beyond basic WASM. | WASM on Jekyll (A73) |
| CLMM Mathematics and Calculator | crypto defi math | Concentrated liquidity mathematics with interactive widget. Direct sequel to AMM article. | Constant Product AMM Mathematics (A67), CLMM draft |
| Solana sBPF Assembly | crypto development asm | Writing Solana programs at the assembly level. Unique low-level blockchain content. | Solana with Rust and Anchor, sBPF draft |
| Statistics for A/B Testing | math development | Applied statistics for software engineers. Practical extension of the statistics draft. | Statistics draft |
| Orbital Mechanics Primer | math science | Applied physics with MathJax. Evergreen STEM content. | Space studies draft, Trigonometry (A14) |
| Context Engineering Patterns Cookbook | ai ai-tools development | Practical patterns distilled from the survey article. Shorter, actionable format. | Context Engineering (A78), A75-A77 series |
| Evaluating AI-Generated Code | ai development | Metrics and methods for assessing agent output quality. Addresses the evaluation gap identified in A78. | A75-A78 series |
| FreeBSD Jails for Development Environments | freebsd development | Container-like isolation using FreeBSD jails. Updates the FreeBSD systems thread with modern practices. | FreeBSD series (A1-A40 era) |
| Shell Scripting with Modern CLI Tools | sh unix development | fd, ripgrep, jq, fzf as modern replacements for traditional UNIX tools. | Shell scripting series |
| Game AI with Minimax and Alpha-Beta Pruning | gamedev math ai | Classical game AI algorithms with proofs of optimality. Bridges game development and mathematical rigor. | Chess/Go game theory series |
| Playdate Game Physics | gamedev playdate math c | Physics simulation on constrained hardware. Applied mathematics on embedded game platform. | Playdate series, Trigonometry (A14) |
