# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-09
**Task**: A83-P3 Revise A83

---

## Verification

### A83 Revised
**Result**: PASS. `_drafts/safe_embedded_functional_control_dsl.markdown` revised with all 8 human-suggested refinements. Article grew from 591 to 688 lines. References grew from 12 to 16 (4 new VM architecture references). All additions match the article's existing prose style and are scoped as lightweight, blog-appropriate refinements.

---

## Implementation Summary

### Files Created/Modified

| File | Changes |
|------|---------|
| `_drafts/safe_embedded_functional_control_dsl.markdown` | 8 revisions applied. 688 lines (was 591). 16 references (was 12). |
| `_drafts/draft_summary.md` | A83 entry updated to reflect revisions and 16 references. |
| `_docs/process/PROMPT.md` | Human-updated with A83-P3 instructions. Committed as-is. |
| `_docs/process/TASKLOG.md` | A83-P3 task state. |
| `_docs/process/REVERSE_PROMPT.md` | This file. |

### Revisions Applied

| # | Revision | Location | Content |
|---|----------|----------|---------|
| 1 | Explicit Threat Model | After introduction, before Software Versions | Trusted host, untrusted script author, trusted computing base defined. Does not defend against malicious host bindings. |
| 2 | Bytecode as Semantic Ground Truth | VM Design subsection | Bytecode operational semantics are the normative definition. All surface syntax desugared prior to execution and analysis. |
| 3 | Numeric Determinism | After Type System subsection | Floating-point behavior must be explicitly specified. Safety-critical deployments may use fixed-point. |
| 4 | Pipeline Desugaring | Pipelines subsection | Multiple placeholders desugared into explicit temporary bindings. Cost analysis at bytecode level. |
| 5 | Termination and Boundedness | Bounded Resource Usage design goal | Termination bounds established statically or enforced at runtime. May restrict unbounded recursion. |
| 6 | Formally Analyzable vs Verified | Safety and Formal Guarantees subsection | Amenable to formal analysis and external proof tools. Not a proof language. Runtime does not perform proofs. |
| 7 | Non-Goals | New subsection after Design Goals | Not a general-purpose language, not a Rust/C++ replacement, not a scheduler, not an actor system. |
| 8 | Reference VM Architectures | New subsection in Related Work | SECD machine (theoretical foundation), Lua 5.1 VM (engineering reference), WebAssembly (formal bytecode spec), JVM (bytecode verification). |

### New References Added

| Reference | URL |
|-----------|-----|
| JVM Specification | https://docs.oracle.com/javase/specs/jvms/se21/html/index.html |
| The Implementation of Lua 5.0 | https://www.lua.org/doc/jucs05.pdf |
| SECD Machine | https://en.wikipedia.org/wiki/SECD_machine |
| WebAssembly Core Specification | https://webassembly.github.io/spec/core/ |

---

## Questions for Human Pilot

**Threat model placement.** The threat model paragraph was placed at the end of the introduction, before Software Versions. An alternative placement would be as a subsection under Design Goals. The current position ensures readers encounter it early.

**Non-goals as subsection.** Non-Goals was placed as a subsection (###) under Design Goals (##). This keeps it associated with the design goals section while distinguishing it from the seven positive goals. An alternative would be a separate top-level section.

**VM architecture depth.** The Reference VM Architectures subsection provides brief descriptions of each VM family. The human may want to expand these with more specific technical details or reduce them to a sentence each.

**Lustre/SCADE in VM architectures.** The human's suggestions included Lustre/SCADE intermediate kernels as a fifth VM reference model. Since Lustre/SCADE is already discussed in detail in the Related Work section immediately above the new Reference VM Architectures subsection, a redundant entry was not added. The human may want to add a cross-reference.

---

## Technical Concerns / Risks

**URL verification.** The 4 new reference URLs should be verified before publication. The JVM Specification URL targets SE 21. The Lua implementation paper URL targets the JUCS 2005 publication. The SECD Machine URL is a Wikipedia article. The WebAssembly Core Specification URL targets the official W3C spec.

**post_url dependency.** A83 still contains `%{ post_url 2026-02-09-writing-proofs %}` which depends on A79 being published first. This is an existing dependency from A83-P2.

**Broken post_url syntax.** The post_url tags in A83 use `%{` instead of `{%`. This appears to be intentional to prevent build errors while A79 is unpublished, as noted in the human's comment that "A83 and A85 intentionally have broken links to unpublished articles."

---

## Intended Next Step

**Awaiting human direction** on:
- Review of the A83 revisions
- Publication order for release candidates (A79, A80, A81, A82, A83, A84, A85)
- Dependencies: A79 before A83, A84 before A85
- Any further work

---

## Session Context

If you are a new AI session reading this file:

1. This is a Jekyll blog project at [sgeos.github.io](https://sgeos.github.io).
2. A documentation knowledge graph exists in `_docs/`. Start at `_docs/README.md`.
3. The project uses scoped conventional commits and Ax-Py-Tz work item coding.
4. `PROMPT.md` is read-only for AI agents. Never modify it. Commit it if the human pilot has changed it.
5. A0 is reserved for non-article work. Thirty-one prompts completed (A0-P1 through A0-P7, A75-P1 through A75-P3, A76-P1 through A76-P4, A77-P1 through A77-P3, A78-P1 through A78-P4, A80-P1, A81-P1, A82-P1, A83-P1, A83-P2, A83-P3, A84-P1, A84-P2, A85-P1, A85-P2).
6. All 74 historical posts have article numbers (A1-A74). A75, A76, A77, and A78 are published. A79, A80, A81, A82, A83, A84, and A85 are release candidates. Next available: A86.
7. Categories are space-separated, not comma-separated.
8. Assets follow `assets/$TYPE/post_$SLUG/$FILENAME` convention.
9. Read `TASKLOG.md` for current task state.
10. Read `CLAUDE.md` at project root for build commands and quick orientation.
11. After publication, include a release announcement draft in REVERSE_PROMPT.md. See `CONTENT_WORKFLOW.md` step 5.
12. The draft summary file was renamed from `old_drafts.md` to `draft_summary.md` in A84-P1.
13. A83 depends on A79 via post_url. A85 depends on A84 via post_url. Respect publication order.
14. Wait for human prompt before proceeding.
