# Prompt Staging Area

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is a staging area for complex human-to-AI instructions. The human pilot drafts and refines prompts here before execution.

---

# Current Prompt

## Comments

Answers to Reverse Prompt Questions:
1) A74 contained an example DeFi Rust-based WASM widget example.
   Do not worry about it if you did not need it.
2) Modifications made to A91, please review.
   Ran into trouble getting the widget to load. See below.

## Objectives

### Fix A91 Widget Source Code

I added an example `index.html` for local testing,
along with terse instructions on how to serve it.
I ran into the following console error.

```
SyntaxError: Importing binding name 'inject_ui' is not found.
```

Revise widget source code so that it has an `inject_ui()` function.
This is likely the function that builds the UI,
so UI element names will need to match up with the elements
expected by the update logic.

Feel free to refer to previous articles if you need an example.
A72, A73, and A74 all contain example code.

## Context

Working on backlog posts for next week.
Converting drafts to full posts.

## Constraints

(none)

## Success Criteria

- CLMM Mathematics (A91) has fixed example code,
  and is release candidate status.

## Notes

(none)
