# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-07-10
**Task**: Modify A205 in place to cover Keleusma 0.2.2 following the 2026-07-09 tag of Keleusma 0.2.2. Single commit as revise-in-place operation. Push all local work to origin.

---

## Verification

### V0.2.2 Modification Complete

The A205 article was originally published as "Getting Started with Keleusma 0.2.1" at 2026-07-09 12:00 UTC. Keleusma 0.2.2 was tagged 2026-07-09, the day after 0.2.1. Version 0.2.2 is a build-fix and tooling release on the self-hosting-groundwork line rather than a language-surface change. The article was modified in place to cover 0.2.2 rather than creating a new post.

- **File renamed via `git mv`** from `_posts/2026-07-09-keleusma_0_2_1_getting_started.markdown` to `_posts/2026-07-10-keleusma_0_2_2_getting_started.markdown`.
- **Editorial date advanced** from 2026-07-09 12:00 UTC to 2026-07-10 12:00 UTC to reflect the V0.2.2 test date.
- **Title updated** to "Getting Started with Keleusma 0.2.2".
- **Opener rewritten** to characterize V0.2.2 as build-fix and tooling release repairing V0.2.1 regressions on 32-bit and no_std embedded targets and the verify-without-floats feature combination, landing the learning guide as a bilingual mdbook served at `https://sgeos.github.io/keleusma/`, landing the self-hosted-compiler subproject scaffold at `compiler/`, and codifying the release process.
- **Playground introduction paragraph added** to the opener referencing `https://sgeos.github.io/keleusma/playground/` which runs the compiler as WebAssembly.
- **Software Versions section updated** to reflect V0.2.2 test date and installed version.
- **Installation section updated** to note V0.2.2 embedded-build fixes and tighten `keleusma-arena` requirement to 0.3.1.
- **Toward a Self-Hosted Compiler section rewritten** to describe the V0.2.2 scaffold at `compiler/` with the three-stage `loop` pipeline skeleton (lexer, parser, codegen), Rust host driver, and release-by-release implementation plan.
- **Going Deeper section rewritten** to reference the hosted mdbook with bilingual English-Japanese gettext translation and the playground.
- **Conclusion updated** to list V0.2.2 additions alongside V0.2.1 additions plus V0.2.2 fixes.
- **References list updated** with hosted book URLs (all return 200), examples URL pinned to v0.2.2 tag, docs.rs pinned to 0.2.2. Two new reference entries: Hosted Book (mdbook) and Browser-Based Playground.
- **Cross-references in A206 and A215 updated** from `related_post_keleusma_021` to `related_post_keleusma_022` with new target `2026-07-10-keleusma_0_2_2_getting_started`.

### Byte-Identical Verification

Every V0.2.1 code example was re-executed against the installed keleusma 0.2.2 CLI. Each example produced identical stdout to the V0.2.1 baseline, and the strip demonstration confirmed byte-identical compiled bytecode between V0.2.1 and V0.2.2 for the same source (both 2456 bytes for the release build). This confirms V0.2.2 preserves V0.2.1 semantics unchanged, which matches the CHANGELOG claim that no wire-format or bytecode-version change accompanies the release.

### External URL Verification

Every external URL in the reference list verified with `curl -I -L`. Ten URLs, all return 200 including the hosted mdbook root, the playground, and every hosted chapter URL (installing_and_running, big_numbers, information_flow_labels, AUTOMATION_SCRIPTING, SECURITY_POLICY). The examples URL and docs.rs URL are pinned to `v0.2.2` respectively.

### Publication Review Corrections

Three corrections applied during publication review:

1. Playground timing hedged. The opener initially claimed the playground "was made available alongside the 0.2.2 release", which is not verifiable from the Keleusma CHANGELOG. Corrected to "The playground is served alongside the hosted book" which does not overstate the timing.
2. Duplicate playground timing claim removed from Going Deeper section.
3. Incorrect internal link removed. The Toward a Self-Hosted Compiler section contained anchor text "the earlier sections of this article" linked to `kel_guide` (the hosted mdbook URL), which was misleading since the anchor referred to sections within the current article rather than to the hosted book. Removed the link, keeping the anchor text as plain prose.

### Certification Barrier Compliance

Zero occurrences of DO-178C, IEC 61508, certification, certified, airworthiness, tool qualification, or Design Assurance Level in the modified article. High-assurance embedded control terminology preserved where used.

### Style Verification

Zero em-dashes, zero en-dashes, zero contractions, zero prose semicolons. All numeric dates in prose spelled out per corpus convention. Line count 851.

### Cross-Reference Audit

Six `post_url` references in the modified A205 article, zero unresolved. Every used link definition matches a defined link definition, zero mismatches. Cross-references from other posts to A205 all updated:

- A215 references `related_post_keleusma_022` in two places (reference list entry, URL definition).
- A206 references `related_post_keleusma_022` in three places (in-body A205 mention, reference list entry, URL definition).

### Status of Process Files

`_docs/process/TASKLOG.md` updated with the A205 modification history entry. `_drafts/draft_summary.md` updated with the A205 retitled entry and V0.2.2 topic. `_docs/process/REVERSE_PROMPT.md` overwritten with this completion report.

### Git Status After Modification

Single commit pattern for the revise-in-place operation. The modification is not a draft-then-publish sequence and does not warrant the two-commit pattern. The commit includes the file rename with modification, the two cross-reference-updating file modifications in A206 and A215, and the process file synchronisation.

---

## Article Number State

- Next available article number: A216.
- A205 retitled but retains its article number. The debug tag `<!-- A205 -->` and the `console.log("A205")` script tag are unchanged.

---

## Action Items for the Human Pilot

- All local commits pushed to origin as part of this task per user instruction.
- GitHub Actions will build and deploy on push. All editorial dates are in the past so every article renders in the current build.
- After deployment, verify at the following canonical permalinks:
  - The V0.2.2 article at `https://sgeos.github.io/rust/embedded/programming/2026/07/10/keleusma_0_2_2_getting_started.html`
  - The prior V0.2.1 permalink at `https://sgeos.github.io/rust/embedded/programming/2026/07/09/keleusma_0_2_1_getting_started.html` will 404 after deployment; this is expected because the file was renamed.
- The Keleusma corpus now aligns with the 0.2.2 release. No further modification required unless a subsequent Keleusma release warrants coverage.

---

## Notes

- Next available article number: A216.
- A205 was retitled from "Getting Started with Keleusma 0.2.1" to "Getting Started with Keleusma 0.2.2" following the 2026-07-09 tag of Keleusma 0.2.2.
- V0.2.2 is a build-fix and tooling release; the language surface is unchanged from V0.2.1. Every V0.2.1 example produces identical output under V0.2.2 with byte-identical compiled bytecode.
- The hosted mdbook and playground URLs were pinned in the article as canonical references. Both return 200 as of the modification date.
- The Developments in Programming Language Theory series A206 through A215 remains as batch-published. Cross-references from A206 and A215 to A205 updated to the new filename.
- All scratch is confined to project-local `tmp/` per recorded preference.
- Blog deploys through GitHub Actions with a lean Jekyll stack.
