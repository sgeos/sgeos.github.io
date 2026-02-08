# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-02-07
**Task**: A0-P4 Fix Header

---

## Verification

### CLAUDE.md Excluded from Jekyll
**Result**: PASS. Added `exclude: [CLAUDE.md]` to `_config.yml`. This prevents Jekyll from processing the file during site generation, removing it from `site.pages` and therefore from the header navigation.

---

## Implementation Summary

### Files Modified

| File | Changes |
|------|---------|
| `_config.yml` | Added `exclude:` list with `CLAUDE.md` entry. |
| `_docs/process/TASKLOG.md` | A0-P4 task state. |
| `_docs/process/REVERSE_PROMPT.md` | This file. |

---

## Speculative Analysis

### Root Cause

GitHub Pages includes the `jekyll-optional-front-matter` plugin by default as part of the `github-pages` gem. This plugin processes `.md` files that lack YAML front matter as Jekyll pages. It extracts a `title` from the first `#` heading in the file.

`CLAUDE.md` begins with `# CLAUDE.md`, so the plugin assigns it `title: "CLAUDE.md"`. The header template (`_includes/header.html`) iterates over `site.pages` and renders a navigation link for every page with a `title`. This causes "CLAUDE.md" to appear in the site header on the live blog.

### Why Preview Differs

The local Jekyll installation (invoked via `_preview.sh`) does not include the `jekyll-optional-front-matter` plugin. Without this plugin, Jekyll treats `.md` files without front matter as static files. They are copied to `_site/` but are not added to the `site.pages` collection. The header template therefore does not render a link for `CLAUDE.md` locally.

### Why README.md Does Not Appear

GitHub Pages also includes the `jekyll-readme-index` plugin, which converts `README.md` into `index.html` at its directory level rather than adding it as a regular page. This likely prevents `README.md` from appearing in the header navigation, even though it also lacks front matter and has a `#` heading.

### Confidence

This analysis is high confidence for the mechanism (exclude directive will prevent processing) and medium confidence for the specific plugin attribution (the behavior is consistent with `jekyll-optional-front-matter` but could involve other GitHub Pages defaults). The human will verify by pushing and checking the live site.

---

## Questions for Human Pilot

No questions. The fix is minimal and the human will verify manually.

---

## Technical Concerns / Risks

**No blocking concerns.** The `exclude` directive is the standard Jekyll mechanism for this purpose. It does not affect Claude Code's ability to read `CLAUDE.md` at runtime.

**Note**: If additional files are added to the project root in the future that should not appear in site navigation (for example, `AGENTS.md`), they should also be added to the `exclude` list.

---

## Intended Next Step

**Awaiting human direction** after manual push and verification.

---

## Session Context

If you are a new AI session reading this file:

1. This is a Jekyll blog project at [sgeos.github.io](https://sgeos.github.io).
2. A documentation knowledge graph exists in `_docs/`. Start at `_docs/README.md`.
3. The project uses scoped conventional commits and Ax-Py-Tz work item coding.
4. `PROMPT.md` is read-only for AI agents. Never modify it. Commit it if the human pilot has changed it.
5. A0 is reserved for non-article work. Eleven prompts completed (A0-P1 through A0-P4, A75-P1 through A75-P3, A76-P1 through A76-P4).
6. All 74 historical posts have article numbers (A1-A74). A75 and A76 are published. Next available: A77.
7. Categories are space-separated, not comma-separated.
8. Read `TASKLOG.md` for current task state.
9. Read `CLAUDE.md` at project root for build commands and quick orientation.
10. Wait for human prompt before proceeding.
