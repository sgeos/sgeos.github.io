# Documentation Strategy

> **Navigation**: [Documentation Root](./README.md)

Meta-documentation describing the conventions governing this knowledge graph.

## Principles

### Atomic Files

Each file covers one concept. This keeps signal-to-noise ratio high and allows AI agents to load only the context they need for a given task.

### Hierarchical Organization

Every section has a `README.md` that serves as a table of contents. High-level files provide orientation. Atomic files provide precision.

### Breadcrumb Navigation

Every file includes an upward navigation link to its parent table of contents and the documentation root. This allows both humans and AI agents to orient themselves quickly.

## Naming Conventions

- File names use `UPPER_SNAKE_CASE` with a `.md` extension.
- Table of contents files are named `README.md`.
- Section directories use `lowercase` names.

## Directory Structure

```
_docs/
├── README.md
├── DOCUMENTATION_STRATEGY.md
├── writing/
│   ├── README.md
│   ├── STYLE_GUIDE.md
│   └── POST_STRUCTURE.md
├── architecture/
│   ├── README.md
│   └── JEKYLL_STRUCTURE.md
├── process/
│   ├── README.md
│   ├── CONTENT_WORKFLOW.md
│   ├── COMMUNICATION.md
│   ├── GIT_STRATEGY.md
│   ├── TASKLOG.md
│   ├── PROMPT.md
│   └── REVERSE_PROMPT.md
└── reference/
    ├── README.md
    └── GLOSSARY.md
```

## AI Agent Navigation

1. Start at `_docs/README.md`.
2. Read the relevant section `README.md` to understand available files.
3. Load atomic files only when needed for the current task.
4. Use upward navigation if disoriented.
5. Do not load all documentation files at once.

## Cross-Reference Conventions

- Use relative markdown links between files. Example: `[Style Guide](../writing/STYLE_GUIDE.md)`.
- Include a "Related Sections" footer in content files where cross-references are useful.
- Navigation breadcrumbs always point upward to the parent table of contents.

## Maintenance

- Add new concepts as atomic files within the appropriate section.
- Split files that exceed approximately 200 lines.
- When removing content, remove it from the parent `README.md` table of contents first.
- Keep this strategy document updated when structural conventions change.

## Version History

| Date | Author | Changes |
|------|--------|---------|
| 2026-02-07 | Claude | Initial creation. Structure adapted from reference project. |
| 2026-02-07 | Claude | Added GIT_STRATEGY.md to directory structure. |
