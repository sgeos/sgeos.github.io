# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-07
**Task**: A0-P6 Reorganize Assets by Type

---

## Verification

### Assets Organized
**Result**: PASS. All files now follow `assets/$TYPE/post_$SLUG/$FILENAME` pattern. No loose files in `assets/` root.

### Posts Patched
**Result**: PASS. Grep confirms zero old-path references remain.

---

## Implementation Summary

### New Directory Structure

```
assets/
  image/
    post_trigonometry/
      trig_diagrams_001.png through _007.png
    post_adding_images_and_downloads_to_a_github_pages_jekyll_blog/
      image.png
  pdf/
    post_adding_images_and_downloads_to_a_github_pages_jekyll_blog/
      document.pdf
    presentations/
      tokyo_ex_6_sechter.pdf
  wasm/
    post_claude_code_getting_started/
    post_constant_amm_mathematics/
    post_webasm_on_jekyll/
```

### Posts Patched

| Post | Article | References Updated |
|------|---------|--------------------|
| `_posts/2016-09-03-trigonometry.markdown` | A42 | 7 image paths: `assets/post_trigonometry/` to `assets/image/post_trigonometry/` |
| `_posts/2016-08-30-adding_images_and_downloads_to_a_github_pages_jekyll_blog.markdown` | A40 | 2 image refs to `assets/image/post_adding_images.../`, 2 PDF refs to `assets/pdf/post_adding_images.../` |

### Files Also Modified

| File | Changes |
|------|---------|
| `_docs/process/TASKLOG.md` | A0-P6 task state. |
| `_docs/process/REVERSE_PROMPT.md` | This file. |

---

## Questions for Human Pilot

No questions. All objectives from PROMPT.md have been met.

---

## Technical Concerns / Risks

**No blocking concerns.** All moves used `git mv`. Old paths confirmed absent via grep.

---

## Intended Next Step

**Awaiting human direction.**

---

## Session Context

If you are a new AI session reading this file:

1. This is a Jekyll blog project at [sgeos.github.io](https://sgeos.github.io).
2. A documentation knowledge graph exists in `_docs/`. Start at `_docs/README.md`.
3. The project uses scoped conventional commits and Ax-Py-Tz work item coding.
4. `PROMPT.md` is read-only for AI agents. Never modify it. Commit it if the human pilot has changed it.
5. A0 is reserved for non-article work. Thirteen prompts completed (A0-P1 through A0-P6, A75-P1 through A75-P3, A76-P1 through A76-P4).
6. All 74 historical posts have article numbers (A1-A74). A75 and A76 are published. Next available: A77.
7. Categories are space-separated, not comma-separated.
8. Assets follow `assets/$TYPE/post_$SLUG/$FILENAME` convention.
9. Read `TASKLOG.md` for current task state.
10. Read `CLAUDE.md` at project root for build commands and quick orientation.
11. Wait for human prompt before proceeding.
