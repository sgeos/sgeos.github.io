# Prompt Staging Area

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is a staging area for complex human-to-AI instructions. The human pilot drafts and refines prompts here before execution.

---

# Current Prompt

## Comments

Read, but unverified:

- Android Development on FreeBSD
- Android Unit Testing
- Authenticating a Phoenix JSON API with Guardian and Ueberauth
- Claude Code on FreeBSD
- Claude Code on OpenBSD
- Claude Code Over SSH
- Getting Started with Solana Using Rust and Pinocchio
- Solana sBPF Assembly Example

## Objectives

Please research the following.
Fold any references in and consider making additions to the "Future Reading" section.

### Revise "Solana sBPF Assembly Example"

Make the following revisions to the "Solana sBPF Assembly Example" draft.
I am certain named constants can be used in sBPF `.s` files.
I am fairly certain a named constant can be defined and commented all on one line.
If a single line delaration and comment is not possible,
the comment can live above the declaration.
Please define, comment, and use named constants for all literals that are not 0, 1, or -1.
Put named constants at the top of the files.

Name constants should be defined something like this:

```
def NAME=value # description
```

Research and use standard naming conventions, including capitalization conventions.

#### Writing the Program

Use a "message length" named constant instead of 12.

```
mov64 r2, 12
```

Use a "success" named constant instead of 0.

```
mov64 r0, 0
```

#### src/log_hello.s ASM

These lines should use named constants "message 0" to "message 3" instead of magic numbers.

```
mov32 r1, 0x6c6c6548
mov32 r1, 0x4273206f
mov32 r1, 0x66204650
mov32 r1, 0x206d6f72
```

Use a "base message length" named constant instead of 17.

```
mov64 r2, 17
```

Use a "message 4" named constant instead of 0x21.

```
mov32 r1, 0x21
```

## Context

Working on backlog posts for next week.
Converting drafts to full posts.

## Constraints

Do not yet assign an article number.

## Success Criteria

- ASM uses named constants, defined with comments at the top of the file.

## Notes

(none)
