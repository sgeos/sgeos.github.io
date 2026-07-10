# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-07-11
**Task**: Research, draft, verify, and publish A216 "Keleusma's Self-Hosting Strategy" as a public-facing summary adapted from two internal Keleusma documents (`docs/reference/INCREMENTAL_SELF_HOSTING.md` and `docs/roadmap/V0_3_0_SELF_HOSTING.md`). Editorial date 2026-07-11 09:00 UTC. Two-commit publication sequence complete; commits staged locally, not pushed per human pilot instruction.

---

## Verification

### Article Body Complete

Public-facing summary of Keleusma's V0.3.0 self-hosting strategy. The article adapts two internal documents into a form readers outside the project can follow.

- Opening frames the strategy as two-part (backward incremental migration method plus three-stage stream-processor pipeline architecture) and connects to A188-A199 compilers series, A204 self-hosted silicon compiler, and A206 PL theory arc opener.
- What Self-Hosting Means and Why It Matters. Language expressiveness validation, dependency removal, V0.4.0 native-code precondition.
- The Backward Incremental Migration Method. Fowler strangler pattern applied backward, four preconditions (working reference, clean stage boundaries, boundaries bridgeable, backend real risk), moving-seam ASCII diagram with H/T/| notation, adapters as throwaway prototypes, deferral ledger with three-things structure, completion gate with self-application fixed point.
- The Three-Stage Pipeline Architecture. Lexer-parser-codegen decomposition, each stage a Keleusma `loop` function, ASCII diagram, three reasons the shape is recommended (composes with existing model, matches Brinch Hansen prior-art, provides natural test points).
- The Integrated Single-Pass Alternative. Wirth tradition covered (Turbo Pascal 10-30k lines/sec on 4.77 MHz 8088 in 1984, Oberon at millions of lines per second), rationale for why the strategy documents but does not recommend it, migration path if the pipeline turns out to be wrong shape.
- The Bootstrap Fixed Point. Phase A cross-compile, Phase B self-compile, Phase C fixed point, with concrete artifact names kelc.0.kel.bin through kelc.2.kel.bin.
- Constraints on the Surface Language. Three tensions (recursion, Hindley-Milner inference, generics and monomorphization) with resolutions (explicit work-stacks, per-function bounded inference, lazy specialization tables).
- Resolved Design Questions. R3.1 work-stack pattern, R3.4 per-function inference bounds (1024 type vars, 4096 constraints, 16384 body nodes, ~130 KiB transient, ~250 KiB persistent), R3.2 symbol-table substrate, R3.3 byte iteration with three host natives, R3.5 three-layered self-validation with SHA-256 canonicalization, R5.3-informed module-scale compilation with `.kel` and `.def.kel` file naming.
- Open Questions. Cross-module monomorphization mechanism, diagnostic quality regression bound, V0.2 surface adequacy audit.
- Prior Art and Lineage. Strangler pattern (Fowler), self-hosting and bootstrapping tradition, GCC multi-stage bootstrap reproducibility comparison, Brinch Hansen pipeline-of-processes (Prentice-Hall 1985), Wirth Compiler Construction (Addison-Wesley 1996) and Project Oberon (Addison-Wesley 1992/2013), Turbo Pascal 1983-1986 with commercial demonstration, CakeML verified bootstrapping alternative, Thompson Reflections on Trusting Trust (CACM August 1984, 1983 Turing Award lecture), Wheeler Diverse Double-Compiling countermeasure (arxiv 2009). Explicit note that the C-family multi-pass tradition (GCC, Clang, PCC, lcc) is not relevant prior art.
- Lessons from a Contemporary Attempt. Brief-lang partial self-hosting case study observations preserved in five points (frontend achievable while backend is the wall, output capability must be first-class host native, divergent execution models are bootstrap hazard, work-stack idiom independently validated, admit only surface syntax you will actually compile).
- Success Criteria. Nine conditions for V0.3.0 completion including intermediate validations for migration steps 1 and 2, Phase B and Phase C fixed points, regression corpus equivalence, CLI `--self-hosted` flag, and documentation acknowledgment.
- Conclusion. Positions the strategy in the V0.3.0 through V0.5 sequence and points to the internal Keleusma documents and A205 V0.2.2 getting-started article for the subproject scaffold context.

### Two-Commit Publication Pattern

Standard two-commit publication. Draft commit `2feb88c` captures the finalised draft in `_drafts/`. Publish commit follows with the `git mv` to `_posts/2026-07-11-keleusma_self_hosting_strategy.markdown` plus TASKLOG, draft summary, and REVERSE_PROMPT synchronisation. Commits staged locally but not pushed per human pilot instruction.

### Primary-Source Verification

Every claim in the article traces to one of the two source Keleusma documents. Content-verification pass compared the article section by section against the source documents.

- Migration method preconditions all preserved.
- Backward-first porting rationale preserved.
- Moving-seam ASCII diagram identical to source document format.
- Deferral ledger three-things structure preserved.
- Three-stage pipeline decomposition preserved with `compiler/lexer.kel`, `compiler/parser.kel`, `compiler/codegen.kel` file paths.
- Integrated single-pass alternative described accurately with Wirth-tradition attribution and Turbo Pascal benchmark.
- Bootstrap phases with kelc.0 through kelc.2 artifacts preserved.
- Surface-language tensions and resolutions preserved.
- Design question bounds (1024/4096/16384, ~130 KiB, ~250 KiB) accurately preserved.
- Open questions preserved.
- Brief-lang lessons preserved verbatim in substance with the same non-endorsement framing.
- Nine success criteria preserved.

### Prior-Art Attribution Verification

- Brinch Hansen on Pascal Compilers, Prentice-Hall, 1985 verified.
- Wirth, Compiler Construction, Addison-Wesley, 1996 verified.
- Wirth and Gutknecht, Project Oberon, Addison-Wesley 1992 revised 2013 verified.
- Fraser and Hanson, A Retargetable C Compiler, Addison-Wesley, 1995 verified.
- Thompson, Reflections on Trusting Trust, CACM Vol 27 No 8 August 1984, 1983 Turing Award lecture verified against A204 prior citation.
- Wheeler, Diverse Double-Compiling, arxiv 2009 verified against A204 prior citation.
- CakeML verified bootstrapped compiler verified.

### External URL Verification

Fifteen external URLs verified with `curl -I -L`. Fourteen return 200. ACM DL URL for Thompson paper returns 403 for HEAD requests as expected per corpus URL-verification patterns for ACM publications. Confirmed indexed via prior corpus references in A204.

### Publication Review Correction

Internal document URL for INCREMENTAL_SELF_HOSTING.md corrected. The initial draft pointed to `blob/v0.2.2/docs/reference/INCREMENTAL_SELF_HOSTING.md` which returned 404 because the document was added to the Keleusma repository after the v0.2.2 tag. Verified that both source documents exist at HEAD of the main branch. Changed both internal document references to `blob/main/...` which resolves 200 for both files.

### Certification Barrier Compliance

Zero occurrences of DO-178C, IEC 61508, certification, certified, airworthiness, tool qualification, or Design Assurance Level in the article body. The article does not treat certification-adjacent topics and the substitute term "high-assurance embedded control" is not needed for this article's material.

### Keleusma Treatment

Keleusma named directly throughout with the design-in-progress framing preserved. The article makes clear that V0.3.0 is a strategy for realization rather than a shipped result. The V0.4.0 native code generation and V0.5+ Keleusma-in-Keleusma-runtime dependencies are named as downstream goals that depend on V0.3.0.

### Equation Density

Zero display equations. Mathjax false. Two ASCII diagrams provide structural visualization. Approximately fifteen inline code notations for file paths, artifact names, function categories, host natives, and data-structure names. Consistent with A204 self-hosted silicon compiler article which is architectural strategy rather than mathematical formalism.

### Style Verification

Zero em-dashes, zero en-dashes, zero contractions, zero prose semicolons. The one semicolon in the article is inside inline code `[Byte; N]` which is Rust array-length syntax and correctly not a prose semicolon. All colons in the article outside YAML frontmatter are inside Rust module-path inline code (`compiler::intern_bytes`, `compiler::text_from_bytes`, `compiler::text_concat`). Frontmatter uniform with the corpus conventions. Debug tag `<!-- A216 -->` and `console.log("A216")` in place.

### Cross-Article References

Four `post_url` references, all resolve.

- A199 (Streaming Compilers Series Conclusion) for the coalgebraic fixed-point condition that self-hosting satisfies.
- A204 (The Self-Hosted Silicon Compiler) for the software-silicon self-hosting boundary.
- A206 (Developments in Programming Language Theory, A Historical Arc) for the broader intellectual context.
- A205 (Getting Started with Keleusma 0.2.2) for the V0.2.2 subproject scaffold context.

### Status of Process Files

`_docs/process/TASKLOG.md` updated with two A216 history entries (draft and publish) and next-available-article-number advanced to A217. `_drafts/draft_summary.md` updated with A216 Published entry near the top. `_docs/process/REVERSE_PROMPT.md` overwritten with this completion report.

### Git Status

Draft commit `2feb88c` created for the finalised draft plus draft summary synchronisation. Publish commit created for the `git mv` to `_posts/` plus TASKLOG, draft summary, and REVERSE_PROMPT synchronisation. Both commits await push authorisation. `git status` after the two commits should show a clean working tree ahead of `origin/master` by two commits.

---

## Article Number State

- Next available article number: A217.
- A216 published as `_posts/2026-07-11-keleusma_self_hosting_strategy.markdown` at editorial date 2026-07-11 09:00 UTC.

---

## Action Items for the Human Pilot

- Review the two local commits before push authorisation. The two-commit sequence is complete but not pushed.
- Push command when ready: `git push origin master`.
- Verify the GitHub Actions deploy completes without errors after the push. The A216 article uses `{% post_url %}` cross-references to A199 A204 A206 A205 which are all already deployed.
- Review the published article at its permalink once the deploy completes at `https://sgeos.github.io/keleusma/compilers/self-hosting/2026/07/11/keleusma_self_hosting_strategy.html`.
- The article is the public-facing counterpart to two internal Keleusma documents. When those documents move or restructure (post-v0.2.2), the article's `blob/main/...` references may need updating.
- A217 could pick up a fresh Keleusma release, a periodic PL theory current-event survey per the A215 handoff, or a fresh subject.

---

## Notes

- Next available article number: A217.
- 0 release candidates from the recent series.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification in `_drafts/`.
- Published through A216 across the combined article number space.
- The Keleusma corpus now covers the V0.3.0 self-hosting strategy in public-facing form. The internal Keleusma documents (`INCREMENTAL_SELF_HOSTING.md` and `V0_3_0_SELF_HOSTING.md`) remain the authoritative technical specifications; A216 is the summary for readers outside the project.
- Primary-source verification pass was performed section by section against the two source documents. Corrections applied during publication review are catalogued above.
- Certification barrier compliance verified. Zero occurrences across the article.
- All scratch is confined to project-local `tmp/` per recorded preference.
- Blog deploys through GitHub Actions with a lean Jekyll stack.
