---
layout: post
mathjax: false
comments: true
title: "Old Drafts Review"
date: 2000-01-01 00:00:00 +0000
categories: meta
---

<!-- Axxx -->

This post reviews the status of old draft posts in this blog's `_drafts/` directory.
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

### Statistics Reference

**File**: `statistics.markdown`
**Topic**: Probability and statistics reference with formulas for binomial distributions, confidence intervals, hypothesis testing, and proportions
**Completion**: ~60%
**Publication Sensibility**: High

Mathematical content is evergreen and requires no tooling updates.
The existing formulas are correct and cover useful ground.
MathJax rendering is already enabled in the front matter.

**Remaining Work**:
Draft explanatory prose between formulas to transform the document from a formula sheet into a tutorial.
Complete the incomplete "Memo" section.
Add a Software Versions block (minimal, since the post is primarily mathematical).
Add introductory and concluding prose.
Add a References section citing standard textbooks.

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

### Magic Cards as a Model of Virtual Goods

**File**: `magic_cards_as_a_model_of_virtual_goods.markdown`
**Topic**: Using Magic the Gathering card anatomy as a model for virtual goods, with Rust data structures
**Completion**: ~20%
**Publication Sensibility**: Medium

The concept is interesting and not time-sensitive.
Rust remains the appropriate language for this topic.
Contemporary Rust (2024 edition) would be used for any new code.

**Remaining Work**:
Draft card anatomy analysis mapping Magic the Gathering card attributes to virtual goods properties.
Implement Rust data structures modeling the card type system.
Replace placeholder Software Versions, Instructions, and References sections.
This draft requires the most new writing relative to what exists.

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

### Introduction to Astronomy

**File**: `introduction-to-astronomy.markdown`
**Topic**: Introduction to astronomy
**Completion**: ~5% (template only)
**Publication Sensibility**: Low

An empty stub with no content beyond placeholder text.
Astronomy is an evergreen and broad topic, but the draft provides no direction or scope.
Publication merit depends entirely on defining a focused angle.
Possible approaches include observational astronomy for beginners, computational astronomy with Python, or astrophotography.
Without a defined scope, the effort to write from scratch is high relative to the publication value.

### Writing Proofs

**File**: `writing-proofs.markdown`
**Topic**: Writing mathematical proofs
**Completion**: ~5% (template only)
**Publication Sensibility**: Low-Medium

An empty stub with no content beyond placeholder text.
Mathematical proof writing is an evergreen STEM education topic with a stable audience.
The topic has higher inherent publication merit than the astronomy stub
because it is more focused and has a clearer target audience (students transitioning from computation to proof-based mathematics).
However, the draft provides no starting material, and the effort is equivalent to writing from scratch.

### Template

**File**: `template.markdown`
**Topic**: Post template for new articles
**Completion**: N/A
**Publication Sensibility**: N/A

This is a template file, not a draft. It provides the standard structure for new posts.

## Summary

Thirteen files exist in `_drafts/`. One is a template. Two are empty stubs created from the template.

The drafts fall into four tiers when assessed for salvageability with contemporary tooling.

**Tier 1: Publishable with moderate effort.**
The Solana sBPF assembly example is the most publishable draft.
It is recent, topical, and has working code.
The statistics reference has correct, evergreen mathematical content that needs prose additions.

**Tier 2: Publishable with significant effort.**
The CLMM calculator has a functional interactive widget that pairs with the published Constant Product AMM article.
The half-life coin draft has substantial written content but needs structural repair.
The space studies and Magic/Rust drafts have sound conceptual foundations but require extensive new writing.

**Tier 3: Salvageable but niche.**
The two Android/FreeBSD drafts should be consolidated into one post and updated to FreeBSD 14 and current Android tooling.
The audience for Android development on FreeBSD is small, making the effort-to-reach ratio unfavorable.

**Tier 4: Rewrite or abandon.**
The Android unit testing and Phoenix/Guardian drafts would require near-complete rewrites to use contemporary frameworks.
The two template stubs (astronomy, proofs) have no existing content.
The proofs stub has higher topicality than the astronomy stub due to its focused audience,
but both would need to be written from scratch.
