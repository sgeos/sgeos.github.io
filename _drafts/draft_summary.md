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

### Radioactive Half-Life Demurrage Cryptocurrency Coin — Release Candidate

**File**: `radioactive_half_life_demurrage_cryptocurrency_coin.markdown`
**Article**: A88, "Radioactive Half-Life Demurrage Cryptocurrency Coin"
**Topic**: Cryptocurrency protocol design combining demurrage with proof of useful work and hierarchical reaping
**Completion**: ~95%
**Publication Sensibility**: High
**Status**: Release Candidate

Fully rewritten from informal notes into a researched article.
Explores a thought experiment in cryptocurrency protocol design
that addresses the security budget problem through three mechanisms.
Exponential decay with a 100-year half-life creates a perpetual security subsidy.
Hierarchical reaping distributes the decay cost across three tiers of holders.
Proof of useful work on the RISC-V ISA replaces hash grinding with verifiable computation.
Covers demurrage history (Gesell, Fisher, Freicoin, Chiemgauer),
half-life decay mathematics with MathJax,
whole-coin quantization, the economic loop,
deterministic smart contract binding with salt-parameterized proof of work,
verification licensing, staking and dispute resolution,
protocol specification, and design tradeoffs.
Fourteen references across three categories (Book, Reference, Research).

**Remaining Work**:
Human review, URL verification, and MathJax rendering check before publication.

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

### Mission Command Management Style — Stub

**File**: `mission_command_management_style.markdown`
**Article**: A86, "Mission Command Management Style"
**Topic**: Mission command management style, standard management categories, history, and appropriate use cases
**Completion**: ~10%
**Publication Sensibility**: Medium
**Status**: Stub

Expanded outline with thesis statement, section headers, and bullet points for each section. Covers standard management style quiz critique, mission command definition and principles (Auftragstaktik, commander's intent, decentralized execution), why mission command does not appear on personality quizzes, application to engineering and scientific teams, benefits, risks and failure modes, and when not to use it.

**Remaining Work**:
Draft all prose from the outline. Research management style taxonomies and mission command doctrine. Add categories, Software Versions, and references.

### Telemeritocracy — Stub

**File**: `telemeritocracy.markdown`
**Article**: A87, "Telemeritocracy"
**Topic**: Telocracy, meritocracy, and their synthesis as telemeritocracy
**Completion**: ~10%
**Publication Sensibility**: Medium
**Status**: Stub

Expanded outline with thesis statement, section headers, and bullet points for each section. Defines telocracy and its anti-democratic nature, defines meritocracy, synthesizes telemeritocracy as a governance model with dynamically assigned decision rights based on expertise and performance. Covers history and precedents, benefits, risks and failure modes, and appropriate use cases for scientific and engineering organizations. References the Mission Command article (A86).

**Remaining Work**:
Draft all prose from the outline. Research telocracy and meritocracy concepts. Add categories, Software Versions, and references. A86 should be published before A87 if the reference is via post_url.

### Cryptotelemeritocracy — Stub

**File**: `cryptotelemeritocracy.markdown`
**Article**: A89, "Cryptotelemeritocracy"
**Topic**: Extending telemeritocratic governance with an anonymous telos auditor
**Completion**: ~10%
**Publication Sensibility**: Medium
**Status**: Stub

Expanded outline with thesis statement, section headers, and bullet points for each section. Extends telemeritocracy (A87) by introducing an anonymous auditor empowered to enforce alignment with the organizational telos. Covers auditor mechanics (selection, appointment, powers, anonymity), recall and limits, organizational context, benefits, risks and failure modes, and appropriate use cases. References A87 Telemeritocracy.

**Remaining Work**:
Draft all prose from the outline. Research anonymous governance mechanisms and decentralized oversight systems. Add categories, Software Versions, and references. A87 should be published before A89 if the reference is via post_url.

### Template

**File**: `template.markdown`
**Topic**: Post template for new articles
**Completion**: N/A
**Publication Sensibility**: N/A

This is a template file, not a draft. It provides the standard structure for new posts.

## Summary

Thirteen files exist in `_drafts/`. One is a template.
One draft has been elevated to release candidate status.
Three stubs have article numbers assigned.
A80 through A85 have been published.
Writing Proofs (A79) has been published.

The drafts fall into five tiers when assessed for salvageability with contemporary tooling.

**Release Candidate.**
Radioactive Half-Life Demurrage Cryptocurrency Coin (A88) has been fully drafted
and is awaiting human review before publication.

**Tier 1: Publishable with moderate effort.**
The Solana sBPF assembly example is the most publishable remaining draft.
It is recent, topical, and has working code.

**Tier 2: Publishable with significant effort.**
The CLMM calculator has a functional interactive widget that pairs with the published Constant Product AMM article.
The space studies draft has sound conceptual foundations but requires extensive new writing.

**Tier 3: Salvageable but niche.**
The two Android/FreeBSD drafts should be consolidated into one post and updated to FreeBSD 14 and current Android tooling.
The audience for Android development on FreeBSD is small, making the effort-to-reach ratio unfavorable.

**Tier 4: Rewrite or abandon.**
The Android unit testing and Phoenix/Guardian drafts would require near-complete rewrites to use contemporary frameworks.

**Stubs.**
Mission Command Management Style (A86), Telemeritocracy (A87), and Cryptotelemeritocracy (A89) are expanded outlines with no drafted prose.
A87 references A86. A89 references A87.

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
| CLMM Mathematics and Calculator | crypto defi math | Concentrated liquidity mathematics with interactive widget. Direct sequel to AMM article. | Constant Product AMM Mathematics (A67), CLMM draft |
| Solana sBPF Assembly | crypto development asm | Writing Solana programs at the assembly level. Unique low-level blockchain content. | Solana with Rust and Anchor, sBPF draft |
| Statistics for A/B Testing | math development | Applied statistics for software engineers. Practical extension of the statistics reference. | Probability and Statistics Reference (A80) |
| Orbital Mechanics Primer | math science | Applied physics with MathJax. Evergreen STEM content. | Space studies draft, Trigonometry (A14) |
| Context Engineering Patterns Cookbook | ai ai-tools development | Practical patterns distilled from the survey article. Shorter, actionable format. | Context Engineering (A78), A75-A77 series |
| Evaluating AI-Generated Code | ai development | Metrics and methods for assessing agent output quality. Addresses the evaluation gap identified in A78. | A75-A78 series |
| FreeBSD Jails for Development Environments | freebsd development | Container-like isolation using FreeBSD jails. Updates the FreeBSD systems thread with modern practices. | FreeBSD series (A1-A40 era) |
| Shell Scripting with Modern CLI Tools | sh unix development | fd, ripgrep, jq, fzf as modern replacements for traditional UNIX tools. | Shell scripting series |
| Game AI with Minimax and Alpha-Beta Pruning | gamedev math ai | Classical game AI algorithms with proofs of optimality. Bridges game development and mathematical rigor. | Chess/Go game theory series |
| Playdate Game Physics | gamedev playdate math c | Physics simulation on constrained hardware. Applied mathematics on embedded game platform. | Playdate series, Trigonometry (A14) |
