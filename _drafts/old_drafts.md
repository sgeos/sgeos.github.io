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

## Draft Status

| Filename | Topic | Completion | Remaining Work | Publication Sensibility |
|----------|-------|------------|----------------|------------------------|
| `building_android_apks_on_freebsd.markdown` | Building Android APKs on FreeBSD using the Linux emulation layer | ~85% | Software Versions block has date and uname fields swapped. Needs prose polish. Nearly identical to the NDK variant and should be consolidated. | Low. Android SDK 25, FreeBSD 11 era (2017). All tooling is severely outdated. |
| `android_ndk_builds_on_freebsd.markdown` | Android NDK builds on FreeBSD using Linux emulation | ~80% | Starts with "TODO: Rework this post." Software Versions formatting issue. Nearly identical to the APK variant. | Low. Same 2017 vintage. NDK r13b is obsolete. Should be merged with the APK draft or abandoned. |
| `android_unit_testing.markdown` | Android unit testing with Gradle, emulators, and CI | ~30% | Placeholder problem description and instructions. Code snippets exist but lack narrative context. Emulator setup is incomplete. | Low. Android Studio 2.2, SDK 25 (2017). Testing frameworks have evolved significantly. |
| `authenticating-a-phoenix-json-api-with-guardian.markdown` | Phoenix/Elixir JSON API authentication with Guardian | ~75% | "Adding Authorization" section is a one-line stub. Article ends abruptly after model and route setup. Broken tests are left as an exercise. | Low. Phoenix 1.1.4, Elixir 1.2.3 (2016). Guardian and Phoenix have had breaking API changes. |
| `statistics.markdown` | Probability and statistics reference with formulas for binomial distributions, confidence intervals, hypothesis testing, and proportions | ~60% | Missing explanatory prose between formulas. Incomplete "Memo" section. No Software Versions. Reads as a formula sheet rather than a tutorial. | Medium. Mathematical content is evergreen. Could be published as a reference with moderate prose additions. |
| `introduction-to-space-studies.markdown` | Orbital parameters, rocket thrust equations, electromagnetic wavelength-frequency relationships | ~30% | Orbital parameter variables are all placeholder ($x$). Needs instructional prose, expanded coverage, and complete variable definitions. | Medium. Physics content is evergreen. Needs significant writing but the mathematical foundation exists. |
| `magic_cards_as_a_model_of_virtual_goods.markdown` | Using Magic the Gathering card anatomy as a model for virtual goods, with Rust data structures | ~20% | Good two-paragraph introduction only. Software Versions, Instructions, and References are all placeholder. Needs card analysis and Rust implementations. | Medium. Concept is interesting and not time-sensitive. Requires substantial new writing. |
| `solana_bpf_asm_example.markdown` | Writing Solana programs using sBPF assembly | ~40% | Placeholder problem description. Missing categories. Has working assembly and build.rs code but needs explanatory prose and testing verification. | Medium-High. Recent (December 2025) and topical. sBPF and Solana are active. Closest to publishable among the technical drafts. |
| `halflife_coin.markdown` | Cryptocurrency protocol design with 100-year half-life decay, RISC-V computing, hierarchical reaping | ~70% | Duplicate sections (Bespoke Reliability and Miner's Incentive appear twice). Categories use comma-separated format (should be space-separated). Missing Software Versions and article number comment. Needs structural polish. | Medium. Speculative protocol design piece. Interesting but niche. |
| `clmm.markdown` | Concentrated Liquidity Market Maker calculator with interactive HTML/JavaScript widget | ~35% | Prose sections are placeholders. Missing categories. Needs CLMM mathematical explanation and DeFi context. | Medium. The interactive calculator widget is functional. Related to the published Constant Product AMM Mathematics article. Needs explanatory content. |
| `introduction-to-astronomy.markdown` | Introduction to astronomy | ~5% | Template only. No content beyond placeholder text. | Low. Nothing to publish. Would need to be written from scratch. |
| `writing-proofs.markdown` | Writing mathematical proofs | ~5% | Template only. No content beyond placeholder text. | Low. Nothing to publish. Would need to be written from scratch. |
| `template.markdown` | Post template for new articles | N/A | This is a template file, not a draft. It provides the standard structure for new posts. | N/A. Not intended for publication. |

## Summary

Thirteen files exist in `_drafts/`. One is a template. Two are empty stubs created from the template.
Of the remaining ten, four date from 2016-2017 and target outdated technology stacks.
The two Android/FreeBSD drafts contain nearly identical content and should be consolidated or abandoned.

The most promising candidates for publication are the Solana sBPF assembly example (recent, topical, partially complete)
and the statistics reference (evergreen mathematical content, substantial formulas already written).
The CLMM calculator has a working interactive widget that pairs well with the published Constant Product AMM article.
The half-life coin draft has the most written content among the newer drafts but is speculative in nature.
