# Prompt Staging Area

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is a staging area for complex human-to-AI instructions. The human pilot drafts and refines prompts here before execution.

---

# Current Prompt

## Comments

Currently reading:

- Getting Started with Solana Using Rust and Pinocchio

Read, but unverified:

- Android Development on FreeBSD
- Android Unit Testing
- Authenticating a Phoenix JSON API with Guardian and Ueberauth
- Claude Code on FreeBSD
- Claude Code on OpenBSD
- Claude Code Over SSH
- Solana sBPF Assembly Example

## Objectives

Please research the following.
Fold any references in and consider making additions to the "Future Reading" section.

### Revise "Solana sBPF Assembly Example"

Make the following revisions to the "Solana sBPF Assembly Example" draft.

#### Use .rodata Section

Please revise the ASM to use a `.rodata` section or equivalent for the string literal.
It should be possible to use an instruction to load the address before calling the logging routine.

#### Linked Object Files

My goal when writing this article was to produce a public example of linking sBPF object files.
The Rust code should contain the entry point, and the `.s` files should contain library functions.
If this should work in principle, please attempt to draft a solution that I can manually verify.

In this case, put the logging logic in an ASM file, and the entrypoint in the Rust code.
The Rust code should pass the string "Rust" to the ASM logging routine.
The logging code should print "Hello sBPF from {}!" where `{}` is the passed in string.

My understanding is that the `build.rs` approach just simplifies linking the object files.
This should be the last subsection or paragraph in "Mixed Rust and Assembly Projects" sections.

## Context

Working on backlog posts for next week.
Converting drafts to full posts.

## Constraints

Do not yet assign an article number.

## Success Criteria

- ASM uses `.rodata` section or equivalent.
- Unless complete infeasible, there should be a linked object file example for me to manually verify.
  - Rust entrypoint passes "Rust" to ASM logging subroutine.
  - ASM subroutine logs "Hello sBPF from {}!" where `{}` is the passed in string.
  - `build.rs` demonstrates how to make all of this "just work" using standard commands.

## Notes

(none)
