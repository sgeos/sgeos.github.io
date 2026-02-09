# Prompt Staging Area

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is a staging area for complex human-to-AI instructions. The human pilot drafts and refines prompts here before execution.

---

# Current Prompt

## Comments

A83 and A85 intentionally have broken links to unpublished articles.
This will be remedied as articles are published.
I reviewed A83, and it needs some revisions.

## Objectives

### Revise A83

Revise A83 based on the suggestions below the standard prompt sections.

## Context

Adding backlog post candidates.

## Constraints

(no comment)

## Success Criteria

- Post successfully drafted and cataloged.

## Notes

(no comment)

# Suggested Revisions and Clarifications for A83

This document proposes **lightweight, blog-appropriate refinements** to the draft post *“Safe Embedded Functional Control DSL”*.
These suggestions are intentionally scoped to an **informal proposal**, not a formal language specification. The goal is to improve clarity, set correct expectations, and preempt common technical objections without adding deep dives or excessive rigor.

---

## 1. Explicit Threat Model (Clarification, Not Specification)

**Why:**
The post repeatedly emphasizes safety, sandboxing, and capability control, but never states *who is trusted*. Readers with security, PL, or safety backgrounds will implicitly look for this.

**Suggested addition (early in the post):**

> **Threat model.**
> The proposed DSL assumes a trusted host application and an untrusted or semi-trusted script author. The VM, runtime, and host-provided native functions form the trusted computing base. The language and VM aim to prevent script-level code from corrupting host memory, accessing unauthorized resources, or violating determinism guarantees, but do not attempt to defend against malicious or incorrectly implemented host bindings.

This frames safety claims precisely without overpromising.

---

## 2. Bytecode as the Semantic Ground Truth

**Why:**
Formal analysis, WCET reasoning, and proof tooling typically operate on bytecode or a small core IR. The post assumes this implicitly but never states it.

**Suggested addition (Runtime and VM Architecture section):**

> The bytecode operational semantics are the normative definition of program behavior. All surface syntax—including pipelines, pattern matching, and multi-headed functions—is desugared into a small, explicit bytecode instruction set prior to execution and analysis.

This resolves concerns about syntactic sugar without requiring a formal grammar.

---

## 3. Numeric Determinism Acknowledgement

**Why:**
Examples use `f32`, which raises immediate questions for safety-critical readers about IEEE-754 behavior and cross-platform determinism.

**Suggested lightweight clarification:**

> Numeric semantics, including floating-point behavior, must be explicitly specified by the language and runtime. Safety-critical deployments may restrict or replace floating-point arithmetic with deterministic fixed-point representations.

This signals awareness without committing to a design prematurely.

---

## 4. Pipeline Placeholders: Explicit Desugaring Note

**Why:**
Multiple pipeline placeholders can raise questions about cost models and analyzability, even though they are semantically straightforward.

**Suggested addition (Pipelines section):**

> Multiple placeholders are syntactic sugar and are desugared into explicit temporary bindings prior to bytecode generation. Resource usage and execution cost are defined and analyzed at the bytecode level, not the surface syntax level.

This preserves ergonomics while keeping analyzability intact.

---

## 5. Termination and Boundedness Expectations

**Why:**
The post emphasizes bounded resources but never explicitly mentions termination, recursion, or loop constraints.

**Suggested small addition (Bounded Resource Usage):**

> The language design enables termination and resource bounds to be established statically or enforced at runtime. Safety-critical configurations may restrict unbounded recursion or require statically provable execution limits.

This reassures readers without locking in a policy.

---

## 6. “Formally Analyzable” vs. “Formally Verified”

**Why:**
The post is careful, but one explicit sentence would prevent misinterpretation.

**Suggested addition (Formal Analyzability section):**

> The language is designed to be amenable to formal analysis and external proof tools; it does not attempt to be a proof language itself, nor does the runtime perform proofs.

This avoids accidental overclaiming.

---

## 7. Optional: Brief Non-Goals Statement

**Why:**
Clarifying what the language is *not* trying to be helps readers understand the intentional constraints.

**Possible short list:**

> **Non-goals.**
> - Not a general-purpose programming language
> - Not a replacement for Rust or C++
> - Not a real-time scheduler or concurrency runtime
> - Not an actor or message-passing system

Even a short list improves framing.

---

## 8. Reference VM Instruction Set Models to Research

The following virtual machines are worth explicit study as **reference models**, not necessarily as implementations to adopt wholesale.

### SECD / CAM Family (Conceptual Reference)
- **Why relevant:** Designed for functional languages with closures and explicit environments.
- **Fit:** Excellent theoretical foundation for a pure, analyzable, functional control DSL.
- **Caveat:** Requires modernization (explicit frames, fixed-width instructions).

### Lua 5.1 VM (Engineering Reference)
- **Why relevant:** Small, fixed-width instruction set; extremely well-understood embeddable VM.
- **Fit:** Demonstrates how to balance simplicity, performance, and analyzability.
- **Caveat:** Later Lua versions move toward register-based complexity.

### WebAssembly (MVP Subset)
- **Why relevant:** Bytecode is the semantic ground truth; formally specified; capability-oriented.
- **Fit:** Strong model for sandboxing, host integration, and bytecode-level analysis.
- **Caveat:** Instruction set is larger and lower-level than ideal for a control DSL.

### JVM Bytecode (Selective Study)
- **Why relevant:** Decades of bytecode verification and formal reasoning experience.
- **Fit:** Demonstrates how rich source languages can lower into a constrained, analyzable core.
- **Caveat:** Designed for OO and mutable state; not a direct match.

### Lustre / SCADE Intermediate Kernels (Conceptual)
- **Why relevant:** Designed explicitly for WCET and formal verification.
- **Fit:** Illustrates how restricted semantics enable strong guarantees.
- **Caveat:** Synchronous dataflow model is narrower than the proposed DSL.

---

## Overall Guidance

These additions do **not** turn the post into a specification.
They simply:

- Clarify trust boundaries
- Anchor semantics at the bytecode level
- Acknowledge known hard problems without solving them
- Align reader expectations with the language’s stated identity

Together, they make the proposal more robust, more credible, and easier to evaluate by technically sophisticated readers.
