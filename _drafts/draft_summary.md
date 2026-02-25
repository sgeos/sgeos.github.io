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

### Human Evolution and the Great Filter — Release Candidate

**File**: `human_evolution_and_the_great_filter.markdown`
**Article**: A95, "Human Evolution and the Great Filter"
**Topic**: Human evolution from LUCA to Homo sapiens through the lens of the Fermi Paradox and the Great Filter
**Completion**: ~95%
**Publication Sensibility**: High
**Status**: Release Candidate

Fully researched article examining whether the evolutionary record on Earth explains the Fermi Paradox.
Traces the complete ancestral lineage of Homo sapiens across 33 stages from the Last Universal Common Ancestor to the present.
Origin of life section covers the fossil record gap, abiogenesis, and panspermia with arguments for and against.
Ancestor table spans seven sub-tables covering pre-eukaryotic life, early eukaryotes, early animals,
vertebrate origins, terrestrial vertebrates, early mammals, primates, and hominins.
Dead ends analysis highlights what did NOT become us at each split,
with detailed treatment of insects, cephalopods, corvids, cetaceans, and elephants.
Extinction events section analyzes the Big Five mass extinctions as both filters and gates,
with compound survival probability expressed in MathJax.
Social animal to technological civilization transition identifies six prerequisites
and uses the Hard Steps probability formalism.
Presents both pre-filter and post-filter arguments before declaring a thesis
that the Great Filter lies predominantly in our past.
Drake Equation, compound survival probability, and Hard Steps probability expressed in MathJax.
References A82 and A90 via post_url.
Sixty-seven references across four categories (Book, Reference, Related Post, Research).

**Remaining Work**:
Human review, MathJax rendering check, and final proofread before publication. A90 must be published before A95.

### History of Rocketplanes — Release Candidate

**File**: `history_of_rocketplanes.markdown`
**Article**: A96, "History of Rocketplanes"
**Topic**: Complete history of rocket-powered aircraft from 1928 to 2024, tracing technology transfer, espionage, and institutional memory
**Completion**: ~95%
**Publication Sensibility**: High
**Status**: Release Candidate

Fully researched article tracing the continuous thread of rocketplane development
from the 1928 Lippisch Ente through the 2024 Dawn Mk-II Aurora.
German pioneers section covers the Ente, Opel RAK.1, Heinkel He 176, and DFS 194.
WWII operational rocketplanes section covers the Me 163 Komet, Bachem Ba 349 Natter,
Yokosuka MXY-7 Ohka, and Bereznyak-Isayev BI-1.
Technology transfer and espionage section covers Operation Paperclip,
Operation Osoaviakhim, and the Silbervogel concept,
tracing how German technology seeded both superpowers.
American X-plane program section covers the Bell X-1 through the Martin X-24B,
including the X-15 hypersonic research program and the cancelled X-20 Dyna-Soar.
Soviet response section covers the MiG-105 Spiral and Buran,
including the BOR-4 reverse-intelligence connection to Dream Chaser.
Space Shuttle section traces technical heritage from X-planes and lifting bodies.
Modern era section covers SpaceShipOne, SpaceShipTwo, Blue Origin New Shepard,
Boeing X-37B, Dream Chaser, and Dawn Mk-II Aurora.
References A90 via post_url.
Fifty references across four categories (Book 4, Reference 41, Related Post 1, Research 4).

**Remaining Work**:
Human review and final proofread before publication. A90 must be published before A96.

### What Does the United States Space Force Do? — Release Candidate

**File**: `what_does_united_states_space_force_do.markdown`
**Article**: A97, "What Does the United States Space Force Do?"
**Topic**: History, justification, and mission portfolio of the United States Space Force
**Completion**: ~95%
**Publication Sensibility**: High
**Status**: Release Candidate

Fully researched article explaining what the United States Space Force does.
History section traces military space from the Army Ballistic Missile Agency
through Air Force Space Command to the 2019 establishment,
with detailed treatment of the Air Force independence precedent
and the substantively identical arguments used against separation in both cases.
Justification section documents fighter pilot culture dominance
using the RAND Corporation study on Air Force officer promotion,
satellite communications deprioritization by the Air Force,
and the emergence of space as a contested warfighting domain.
Mission portfolio section covers ten areas: satellite communications,
Global Positioning System, missile warning, space domain awareness,
launch operations, nuclear command control and communications,
intelligence surveillance and reconnaissance, cyber and electronic warfare,
weather, and offensive and defensive space operations.
Organization section covers the three Field Commands,
delta structure, key installations, Guardian personnel, and budget.
No post_url dependencies on unpublished articles.
Forty-two references across two categories (Reference 31, Research 11).

**Remaining Work**:
Human review and final proofread before publication.

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

Thirteen files exist in `_drafts/`. One is a template.
Three drafts have been elevated to release candidate status.
No stubs remain.
A80 through A94 have been published.
Writing Proofs (A79) has been published.

The drafts fall into four tiers when assessed for salvageability with contemporary tooling.

**Release Candidates.**
Human Evolution and the Great Filter (A95),
History of Rocketplanes (A96),
and What Does the United States Space Force Do? (A97) have been fully drafted
and are awaiting human review before publication.
A95 references A82 and A90 via post_url (both now published).
A96 references A90 via post_url (A90 now published).
A97 has no post_url dependencies.
All publication order dependencies have been resolved.
A95, A96, and A97 have no remaining dependencies.

**Tier 1: Publishable with moderate effort.**
No drafts remain in Tier 1. All publishable drafts have been elevated to release candidate or pre-release candidate status.

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
