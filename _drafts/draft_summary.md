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

### Concentrated Liquidity Market Maker Mathematics — Release Candidate

**File**: `clmm_mathematics.markdown`
**Article**: A91, "Concentrated Liquidity Market Maker Mathematics"
**Topic**: Concentrated liquidity mathematics with interactive Rust WASM calculator widget
**Completion**: ~95%
**Publication Sensibility**: High
**Status**: Release Candidate

Fully rewritten from a JavaScript calculator stub into a researched article.
Serves as a companion to Constant Product AMM Mathematics (A73),
covering the concentrated liquidity extension introduced by Uniswap v3.
Includes virtual and real reserves derivation, the three price regimes,
liquidity computation from deposits, tick mathematics with fee tier table,
capital efficiency, fee accrual, and amplified impermanent loss.
Calculator rewritten from JavaScript to Rust WASM following the A72/A73 pattern.
References A73 and A72 via post_url.
Six references across three categories (Reference, Related Post, Research).

**Remaining Work**:
Human review, URL verification, MathJax rendering check, and WASM compilation before publication.

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

### Introduction to Space Studies — Release Candidate

**File**: `introduction_to_space_studies.markdown`
**Article**: A90, "Introduction to Space Studies"
**Topic**: Space operations history, dual-use aerospace technologies, rocket propulsion, orbital mechanics, and atmospheric flight equations
**Completion**: ~95%
**Publication Sensibility**: High
**Status**: Release Candidate

Fully rewritten from a 61-line stub into a researched article.
Serves as a companion to Introduction to Astronomy (A82),
covering applied spaceflight mathematics rather than observational astronomy.
Includes a brief history of space operations from rocket pioneers through the modern era,
a section on the inherently dual-use nature of aerospace technology,
and comprehensive mathematical treatment of rocket propulsion,
orbital mechanics, and atmospheric flight.
References A82 via post_url.
Eighteen references across three categories (Reference, Related Post, Research).

**Remaining Work**:
Human review, URL verification, and MathJax rendering check before publication.

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

### Telemeritocracy — Release Candidate

**File**: `telemeritocracy.markdown`
**Article**: A87, "Telemeritocracy"
**Topic**: Telemeritocracy as a governance model synthesizing telocracy and meritocracy for engineering teams
**Completion**: ~95%
**Publication Sensibility**: High
**Status**: Release Candidate

Fully researched article proposing telemeritocracy as a governance model.
Defines telocracy through Oakeshott and Hayek, traces meritocracy from Young's satire through modern tech adoption,
synthesizes both into a compound governance principle where authority is assigned based on demonstrated ability to advance a defined purpose.
Examines precedents in Apache, IETF, academic shared governance, and Valve (as failure case).
Discusses engineering team fit, failure modes (Goodhart's Law, Peter Principle, mission drift, authoritarianism risk, informal hierarchy),
and limitations. References the companion Mission Command article (A86) via post_url.
Eleven references across four categories (Book, Reference, Related Post, Research).

**Remaining Work**:
Human review, URL verification, and final proofread before publication. A86 must be published before A87.

### Cryptotelemeritocracy — Release Candidate

**File**: `cryptotelemeritocracy.markdown`
**Article**: A89, "Cryptotelemeritocracy"
**Topic**: Extending telemeritocratic governance with a cryptocratic oversight layer for mission drift prevention
**Completion**: ~95%
**Publication Sensibility**: High
**Status**: Release Candidate

Fully researched article proposing cryptotelemeritocracy as a synthesis of cryptocracy and telemeritocracy (A87).
Addresses the mission drift vulnerability in telemeritocratic governance
by introducing a cryptocratic layer with an anonymous arbitrator elected from a private candidate pool.
Grounds the mission drift problem in organizational theory through Merton, Michels, and Selznick.
Surveys historical precedents for anonymous oversight including Athenian ostracism, Roman tribunes, the Devil's Advocate, Venetian bocche di leone, grand jury secrecy, and inspector general systems.
Defines the cryptocratic layer covering candidate pool composition, arbitrator powers, selection and appointment, recall, communication, incentives, and embedded configurations.
Distinguishes oversight and executive configurations with ombudsman and constitutional guardianship analogs.
Introduces strength classifications along two dimensions of anonymity for the organization and arbitrator.
Addresses telos amendment, mission rigidity, and organizational dissolution upon telos achievement.
Analyzes counter-espionage properties including espionage targeting disruption, espionage-driven mission drift, relationship to existing security mechanisms, and defense in depth.
Discusses eight failure modes and five contexts where the model is inappropriate.
Nineteen references across four categories (Book, Reference, Related Post, Research).

**Remaining Work**:
Human review, URL verification, and final proofread before publication. A87 must be published before A89.

### Cryptotelemeritocracy for Space Exploitation — Release Candidate

**File**: `cryptotelemeritocracy_for_space_exploitation.markdown`
**Article**: A92, "Cryptotelemeritocracy for Space Exploitation"
**Topic**: Applying cryptotelemeritocratic governance to a multigenerational space exploitation enterprise
**Completion**: ~95%
**Publication Sensibility**: High
**Status**: Release Candidate

Fully researched article applying the cryptotelemeritocratic governance model (A89)
to a multigenerational space exploitation enterprise
whose telos spans Mercury colonization through intergalactic expansion.
Introduction foreshadows four-phase compatibility assessment.
Telos structured into 13 objectives across four hierarchical categories:
infrastructure-enabling, energy-scaling, expansion-propagating, and defensive.
Kardashev framing notes governance shift from resource scaling
to civilizational continuity beyond Type III.
Introduces the Birch Planet concept for galaxy-scale energy capture
around a supermassive black hole, with shell gravity equation.
Covers near-term goals including lunar mass driver with orbital vs escape velocity
distinction and deceleration propellant note, Venus aerostat colonies,
Mercury colonization, and Mercury cannibalization as an irreversible
inflection point where governance stability becomes existential.
Venus water sourced from comets, asteroids, and trans-Neptunian objects.
Mercury quantitative claims attributed to MESSENGER mission data.
EROI and exponential growth equations for Dyson Swarm feedback loop.
Presents the corporate structure with corrected spinoff value equations
including $V_{spinoff}$ term and corrected $\Delta V_{share}$ formula.
Reverse conglomerate appreciation through excess pledges.
Spinoff mechanism sheds solved problems, misaligned personnel, and drift pressure.
$\Delta V_{share}$ quantifies focus, $V_{remaining}$ quantifies market opinion.
Cryptotelemeritocracy subordinates shareholder capitalism to telos primacy.
Arbitrator is the only actor not compensated by profit,
champion of the telos not of profit and loss,
preventing profitable stasis short of the telos.
Latency cascade degrades governance from coordinated behavior
to coordinated meaning to propagated narrative.
Governance Coherence Half-Life ($T_{GCH}$) introduced with glottochronology analogy,
punctuated equilibrium critique, and operational 50% divergence definitions.
Intergalactic phase reframed as myth-structure
that may further degrade to rejected superstition.
Analyzes covert seeding during expansion, the spinoff mechanism's relationship
to Michels' iron law of oligarchy, counter-espionage properties in space,
and five space-specific failure modes.
MathJax enabled with multiple equations.
References A89 and A90 via post_url.
Twenty references across four categories (Book, Reference, Related Post, Research).

**Remaining Work**:
Human review, URL verification, and final proofread before publication. A89 must be published before A92.

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

Sixteen files exist in `_drafts/`. One is a template.
Six drafts have been elevated to release candidate status.
No stubs remain.
A80 through A86 have been published.
Writing Proofs (A79) has been published.

The drafts fall into four tiers when assessed for salvageability with contemporary tooling.

**Release Candidates.**
Telemeritocracy (A87),
Radioactive Half-Life Demurrage Cryptocurrency Coin (A88),
Cryptotelemeritocracy (A89),
Introduction to Space Studies (A90),
Concentrated Liquidity Market Maker Mathematics (A91),
and Cryptotelemeritocracy for Space Exploitation (A92) have been fully drafted
and are awaiting human review before publication.
A87 references A86 via post_url (A86 now published). A89 references A87 via post_url.
A92 references A89 and A90 via post_url.
A90 references A82 via post_url. A91 references A73 and A72 via post_url.
Publication order dependency: A87 before A89 before A92.
A88, A90, and A91 have no dependencies.

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
