# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-07-09
**Task**: Research, draft, verify, and publish A205 "Getting Started with Keleusma 0.2.1" as the third article in the Keleusma getting-started series with A107 (0.1.1) and A110 (0.2.0). Editorial date 2026-07-09 12:00 UTC. Two-commit publication sequence complete; commits staged locally, not pushed per human pilot instruction.

---

## Verification

### Article Body Complete

Practical walkthrough of the material additions in the Keleusma 0.2.1 release tagged 2026-07-08, aligned with the pattern established by A107 and A110.

- Opening frames the article as a companion to A107 and A110 and connects the 0.2.2 development-cycle self-hosted-compiler groundwork to A199 and A204.
- Software Versions section captures actual host details from the executing environment.
- Installation section preserves the source-checkout pattern from A110 with updated dependency version pins.
- Boolean, Bitwise, and Shift Operators section introduces the letter-prefixed bitwise family (`band`/`bor`/`bxor`/`bnot`), the assembly-mnemonic shifts (`lsl`/`asl`/`lsr`/`asr`), and the two boolean subfamilies with eager (`and`/`or`/`xor`/`not`) and short-circuit (`andalso`/`orelse`) semantics. Three runnable examples with computed outputs.
- General Const Generics section covers the `const` keyword introduction, turbofish call syntax, admissible arithmetic expressions in const arguments (`+`/`-`/`*` excluding division and modulo to preserve totality), and the monomorphization-substitution property that preserves the static bounds.
- Executable Scripts section covers the shebang line convention and shell-orchestrator use pattern.
- Script Arguments section covers `shell::arg` returning `Option<Text>`, `shell::arg_count`, the `--` terminator, and the companion `shell::run_full` native returning `(Word, Text, Text)`.
- Debug Assertions section covers the `assert` statement with optional message, `VmError::AssertionFailed` at debug builds, and compile-out under release builds. Explicit hedge on CLI vs library capability: the CLI prints the raw `VmError` while source-span resolution happens in a host program consuming `Vm::fault_source_location()`.
- Partial Operation Handling section covers checked arithmetic (`ok`/`overflow`/`underflow`/`zero_divisor`), array indexing (`invalid_index`), refinement-newtype construction (`invalid_newtype`), discriminant-to-enum (`ok`/`payload_discriminant`/`invalid_discriminant`), and fallible native calls (`error(code)`). Runnable example demonstrates `safe_div`, `saturate_add_byte`, and the `saturate_max` keyword.
- Strippable Debug Metadata section demonstrates `keleusma compile --debug` and `keleusma strip` with a byte-identical verification via `cmp`, scoped to same source.
- Deployment Policy section covers the strict-mode signing and encryption operator-configured trust-store model with three activation paths (`KELEUSMA_TRUSTED_KEYS_DIR`, `/etc/keleusma/trusted_keys`, `KELEUSMA_REQUIRE_SIGNED=1`) and symmetric strict-encryption configuration through `KELEUSMA_DECRYPTION_KEYS_DIR` and `KELEUSMA_REQUIRE_ENCRYPTED`.
- Under the Hood section summarises three internal changes: flat-byte composite runtime representation with 32-byte `Value` slot down from 40, typed operand-stack pass modelled after the JVM and WebAssembly verifiers, and trait-method resolution on generic structs and enums.
- Toward a Self-Hosted Compiler section stamps the 0.2.2 development cycle's self-hosted-compiler groundwork theme and cross-references A199 for the software case and A204 for the silicon case.
- Going Deeper section indexes the guide chapters relevant to the article's topics.
- Conclusion frames 0.2.1 as consolidation, preserving the central definitive-bound promise.

### Two-Commit Publication Pattern

Standard two-commit publication. Draft commit `20dce1b` captures the finalised draft in `_drafts/`. Publish commit follows with the `git mv` to `_posts/` plus the process file updates. Git rename detection preserves file history. Commits staged locally but not pushed per human pilot instruction.

### Primary-Source Verification

Every claim about Keleusma 0.2.1 additions traces directly to the shipped `CHANGELOG.md` in the `v0.2.1` tag worktree at `tmp/keleusma-021/`. Every code listing was executed against an installed `keleusma 0.2.1` CLI built from that worktree. Every reported output is the actual output produced by the interpreter. Two publication-review hedges applied.

- Assert-failure demonstration hedge. The CHANGELOG documents `Vm::fault_source_location()` for host programs. The command-line frontend does not expose it and prints the raw `VmError` alone. Article notes both facts and points the reader to the library application-programming-interface for span resolution.
- Strip byte-identical claim hedge. The CHANGELOG claim that a stripped debug build is byte-identical to a release build holds for source without the `assert` statement, since `assert` emits opcodes only under debug builds. Article uses a source without `assert` for the strip demonstration and scopes the byte-identical claim to "of the same source".

### External URL Verification

Every external URL verified with `curl -I -L`. Hosted mdBook site at `sgeos.github.io/keleusma/` returned 404 across every candidate chapter URL. All guide references switched to `github.com/sgeos/keleusma/blob/v0.2.1/docs/guide/...` which all resolve `200`. Examples URL switched to `github.com/sgeos/keleusma/tree/v0.2.1/examples/scripts`. Docs.rs URL pinned to `/keleusma/0.2.1`. Pinning to the tag provides stability against future guide reorganisation and preserves the reader's ability to see documentation matching the release the article discusses.

### Certification Barrier Compliance

Zero occurrences of DO-178C, IEC 61508, tool qualification, certification, certified, airworthiness, or Design Assurance Level in the article body. The article does not treat certification-adjacent topics and the substitute term "high-assurance embedded control" is not needed. Keleusma is named directly throughout with design-in-progress framing preserved via the standard phrasing.

### Keleusma Treatment

Named directly throughout. Design-in-progress framing preserved in the Toward a Self-Hosted Compiler section: the Keleusma standardization effort sits on the software side of the self-hosting boundary and is described as a candidate example of a compact-toolchain language design that a self-hosting compiler could reasonably compile itself with. No overreach on hardware-target capability.

### Equation Density

Zero display equations. `mathjax: false`. One inline mathematical expression `x * 2^k` appears in the shift-operator section as a compact expression of the multiplicative interpretation of `asl`. Consistent with A107 and A110 disposition and with the recent zero-equations disposition of A201, A202, A203, and A204.

### Style Verification

Zero em-dashes, zero en-dashes, zero contractions, zero prose semicolons outside code blocks and debug tags. Frontmatter uniform with the getting-started series conventions: `layout: post`, `mathjax: false`, `comments: true`, `categories: rust embedded programming`. Debug tag `<!-- A205 -->` and `console.log("A205")` in place.

### Cross-Article References

Related-post entries for A107 (Getting Started with Keleusma 0.1.1), A110 (Getting Started with Keleusma 0.2.0), A109 (A Verifiable Control Kernel in Keleusma), A111 (Information-Flow Control, A Deep Dive with Keleusma), A199 (Streaming Compilers Series Conclusion), and A204 (The Self-Hosted Silicon Compiler). Every `post_url` target verified against the `_posts/` directory. A199 is cited substantively in the Toward a Self-Hosted Compiler section for the coalgebraic fixed-point endpoint. A204 is cited substantively for the silicon-boundary case of the self-hosting concept.

### Status of Process Files

`_docs/process/TASKLOG.md` updated with two A205 history entries and next-available-article-number advanced to A206. `_drafts/draft_summary.md` updated with an A205 Published entry near the top. `_docs/process/REVERSE_PROMPT.md` overwritten with this completion report.

### Git Status

Draft commit `20dce1b` created for the finalised draft with draft summary synchronisation. Publish commit created for the `git mv` to `_posts/` plus TASKLOG, draft summary, and REVERSE_PROMPT synchronisation. Both commits await push authorisation. `git status` after the two commits should show a clean working tree ahead of `origin/master` by two commits.

---

## Article Number State

- A1 through A74: legacy published posts predating the modern numbered tracking.
- A75 through A151: published series across 2026-02-06 through 2026-03-14.
- A152 through A160: analog-facilities series, published 2026-06-28 through 2026-07-06.
- A161 through A172: patent and startup strategy series, published 2026-05-03 through 2026-05-14.
- A173 through A187: two-dimensional projection in games series, published 2026-04-18 through 2026-05-02.
- A188 through A199: stream-based compilers series, published 2026-04-06 through 2026-04-17.
- A200: history of hardware description languages, published 2026-03-13.
- A201: design space for next-generation HDLs, published 2026-07-07.
- A202: meta-factory prior art and the reproduction loop, published 2026-07-08 at 09:00 UTC.
- A203: hardware description languages the state of the practice, published 2026-07-08 at 12:00 UTC.
- A204: the self-hosted silicon compiler, published 2026-07-09 at 09:00 UTC.
- A205: getting started with Keleusma 0.2.1, published 2026-07-09 at 12:00 UTC (this article).
- Next available article number: A206.

A205 is the third article in the Keleusma getting-started series with A107 and A110, aligned with the 0.2.1 release tagged 2026-07-08.

---

## Action Items for the Human Pilot

- Review the two local commits before push authorisation. The two-commit sequence is complete but not pushed.
- Push command when ready: `git push origin master`.
- Verify the GitHub Actions deploy completes without errors after the push. The article uses `{% post_url %}` cross-references to A107, A110, A109 (verifiable control kernel), A111 (information-flow control deep dive), A199, and A204, which should all resolve since those posts are already deployed.
- Review the published article at its permalink once the deploy completes at `https://sgeos.github.io/rust/embedded/programming/2026/07/09/keleusma_0_2_1_getting_started.html`.
- Consider removing the `tmp/keleusma-021/` worktree after the article is deployed: `git -C /Users/bsechter/projects/rust/keleusma worktree remove /Users/bsechter/projects/blog/tmp/keleusma-021`. The worktree was used for the CLI-verification pass and is no longer required.

---

## Notes

- Next available article number: A206.
- 0 release candidates from the HDL articles.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification in `_drafts/`.
- Published through A205 across the combined article number space, though A204 and A205 commits are local only pending push authorisation.
- The Keleusma getting-started thread now spans three release lines: A107 (0.1.1), A110 (0.2.0), and A205 (0.2.1).
- Every code listing in A205 was verified against the installed `keleusma 0.2.1` binary. Software Versions, installation confirmation, and every runnable example produce the outputs recorded verbatim in the article.
- Primary-source verification passes were performed during publication review, matching the lesson recorded from the compilers series about primary-source verification preceding formalisation. External URLs verified with `curl -I -L`; hosted mdBook site was 404 so all guide references switched to the `v0.2.1` tag on GitHub for stability.
- The V0.2.1 shipped `CHANGELOG.md` is the authoritative source for every claim about the release. All V0.2.1 material additions are covered in the article except two host-facing capabilities that do not surface in a CLI walkthrough. First, the breakpoint runtime mechanism is a host application-programming-interface. Second, the whole-segment shared-data marshalling is a host application-programming-interface. Both are noted in the CHANGELOG for readers who consult it.
- Keleusma named directly with design-in-progress framing per the pattern established across the recent Keleusma articles.
- All scratch is confined to project-local `tmp/` per recorded preference.
- Blog deploys through GitHub Actions with a lean Jekyll stack.
