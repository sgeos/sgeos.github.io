# Dromon Trial 1

> **Navigation**: [Process](../README.md) | [Documentation Root](../../README.md)

The first multi-model trial of the PyDromon harness on this blog, run on 2026-10-30. Three session lines from
three companies were asked to bring A306 to A309 to the Equations section format, to write one harness
experience report each, and to draft A385 about the attempt. Claude Opus 5.5 on Claude Code and GPT-6-Luna on
Codex did the work. Grok 4.7 on Grok Build never ran a turn that reached the task, because its engine writes
empty `hooks-paths` and `installed-plugins` entries into its Dromon home on every start and Dromon then holds
the line.

| File | Description |
|------|-------------|
| [LINES.md](./LINES.md) | The standing brief every line received at the start of each turn |
| [harness-report-opus.md](./harness-report-opus.md) | Experience report of the Opus line |
| [harness-report-luna.md](./harness-report-luna.md) | Experience report of the Luna line |
| [a385-luna.md](./a385-luna.md) | The Luna line's source notes for the A385 draft |
| [notation_A305-A310.md](./notation_A305-A310.md) | The shared notation baseline built from A305 and A310 |

## Outcome

- A306, A308 and A309 were classified by Opus and reviewed by Luna. A307 was classified by Luna and reviewed by
  Opus. 483 equations, 237 standard and 246 bespoke, all consistent, merged by the operator and gated once.
- The disputed A307 Equation 6 was ruled bespoke by the operator, since it allocates the whole reported error
  growth to gyroscope drift, as its neighbours Equations 4, 5 and 7 do.
- Seven article errors were found and left, since equations were out of scope. They are in
  [Article Errata](../ARTICLE_ERRATA.md). The A309 Equation 122 finding was first stated with the wrong reason
  and confirmed by the other line, and the operator's recomputation corrected it.
- The A385 draft is `_drafts/dromon_three_models_equations_sections.markdown`, dated 2026-08-21, unpublished.

## Operator-Side Changes and Failures

- The Grok home `~/.grok/dromon-home` needed its empty entries removed once, its `sandbox.toml` extended to deny
  the blog's `.dromon` paths and the credential directories, and a suggested `read_only` entry for the
  worktree's `.git` file removed, because Grok refuses a file there. A backup is `sandbox.toml.bak-20261030`.
- A loop that would have removed the empty entries before every Grok turn was refused by the permission
  classifier, and was not worked around.
- The operator's mail watcher requested more than the fifty-message limit and failed silently, so a held Luna
  line and the Opus completion report went unseen for about an hour.
