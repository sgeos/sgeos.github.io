# Prompt Staging Area

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is a staging area for complex human-to-AI instructions. The human pilot drafts and refines prompts here before execution.

---

# Current Prompt

## Comments

WASM for A91 built and added to repo.
Please as commit as well as completing the below objectives.

## Objectives

### Modernize Android Development on FreeBSD

The general strategy is to use the FreeBSD Linuxulator
in combination with a command line SDK and NDK development workflow.
The Android emulator is completely out of scope. (State this!)
Assume testing will be done on hardware using a connected device.

The sample application should be a port of the
A91 WASM widget to Android as a single page app.
Mission success if this sample app can be built and tested from FreeBSD.

The development stack is:
- Kotlin for SDK work
- Rust for NDK work
- Whatever happens to be conventional for everything else, like UI files

Sections:
- Post summary (what are we doing and not doint)
- Software Version (just give commands; I will update manually)
- Environment setup.
  - Required ports and other step.
- SDK development.
  - Kotlin app
  - Set up UI
  - Build and run non-interactive app on connected device
- NDK development
  - Rust update code exposed via FFI
  - Build and run interactive app on connected device
- Emulator feasibility
- Conclusion
- Future Reading
- References

Make sure this post is properly researched.

## Context

Working on backlog posts for next week.
Converting drafts to full posts.

## Constraints

Do not yet assign an article number.
Do not slot for publication, despite the manual date update.

## Success Criteria

- Android Development on FreeBSD article in pre-release candidate state
  ready for verification on FreeBSD.
- Sample project itself is portable so I can test on macOS first.

## Notes

(none)
