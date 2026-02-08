# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-07
**Task**: A0-P5 Organize Assets

---

## Verification

### Assets Organized
**Result**: PASS. All loose files removed from `assets/` root. Directory now contains only organized subdirectories: `post_trigonometry/`, `post_adding_images_and_downloads_to_a_github_pages_jekyll_blog/`, `presentations/`, and `wasm/`.

### Posts Patched
**Result**: PASS. Grep confirms zero old-path references remain in any `.markdown`, `.html`, or `.md` file.

---

## Implementation Summary

### Files Moved

| Original Path | New Path |
|---------------|----------|
| `assets/trig_diagrams_001.png` | `assets/post_trigonometry/trig_diagrams_001.png` |
| `assets/trig_diagrams_002.png` | `assets/post_trigonometry/trig_diagrams_002.png` |
| `assets/trig_diagrams_003.png` | `assets/post_trigonometry/trig_diagrams_003.png` |
| `assets/trig_diagrams_004.png` | `assets/post_trigonometry/trig_diagrams_004.png` |
| `assets/trig_diagrams_005.png` | `assets/post_trigonometry/trig_diagrams_005.png` |
| `assets/trig_diagrams_006.png` | `assets/post_trigonometry/trig_diagrams_006.png` |
| `assets/trig_diagrams_007.png` | `assets/post_trigonometry/trig_diagrams_007.png` |
| `assets/image.png` | `assets/post_adding_images_and_downloads_to_a_github_pages_jekyll_blog/image.png` |
| `assets/document.pdf` | `assets/post_adding_images_and_downloads_to_a_github_pages_jekyll_blog/document.pdf` |
| `assets/tokyo_ex_6_sechter.pdf` | `assets/presentations/tokyo_ex_6_sechter.pdf` |

### Posts Patched

| Post | Article | References Updated |
|------|---------|--------------------|
| `_posts/2016-09-03-trigonometry.markdown` | A42 | 7 image references (lines 14, 15, 29, 40, 51, 288, 289) |
| `_posts/2016-08-30-adding_images_and_downloads_to_a_github_pages_jekyll_blog.markdown` | A40 | 4 references: 2 rendered (`image.png`, `document.pdf`) + 2 raw example blocks |

### Unreferenced Files

| File | Notes |
|------|-------|
| `tokyo_ex_6_sechter.pdf` | Presentation slides from Tokyo.ex meetup #6. Committed 2016-09-22. Not referenced by any post. Moved to `assets/presentations/`. |

### Files Also Modified

| File | Changes |
|------|---------|
| `_docs/process/TASKLOG.md` | A0-P5 task state. |
| `_docs/process/REVERSE_PROMPT.md` | This file. |

---

## Questions for Human Pilot

No questions. All objectives from PROMPT.md have been met.

---

## Technical Concerns / Risks

**No blocking concerns.** All file moves used `git mv` to preserve history. Old paths confirmed absent via grep.

**Note on subdirectory naming**: The per-post subdirectory convention (`assets/post_<slug>/`) matches the existing `assets/wasm/post_<slug>/` pattern. The `post_adding_images_and_downloads_to_a_github_pages_jekyll_blog` directory name is long but consistent with the pattern.

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
5. A0 is reserved for non-article work. Twelve prompts completed (A0-P1 through A0-P5, A75-P1 through A75-P3, A76-P1 through A76-P4).
6. All 74 historical posts have article numbers (A1-A74). A75 and A76 are published. Next available: A77.
7. Categories are space-separated, not comma-separated.
8. Read `TASKLOG.md` for current task state.
9. Read `CLAUDE.md` at project root for build commands and quick orientation.
10. Wait for human prompt before proceeding.
