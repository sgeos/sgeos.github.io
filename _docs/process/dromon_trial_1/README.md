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
| [harness-report-grok.md](./harness-report-grok.md) | Experience report of the Grok line, written after it was admitted |
| [a385-grok.md](./a385-grok.md) | The Grok line's source notes for the A385 draft |
| [a385-luna.md](./a385-luna.md) | The Luna line's source notes for the A385 draft |
| [notation_A305-A310.md](./notation_A305-A310.md) | The shared notation baseline built from A305 and A310 |

## Outcome

- A306, A308 and A309 were classified by Opus and reviewed by Luna. A307 was classified by Luna and reviewed by
  Opus. 483 equations, 237 standard and 246 bespoke, all consistent, merged by the operator and gated once.
- The disputed A307 Equation 6 was ruled bespoke by the operator, since it allocates the whole reported error
  growth to gyroscope drift, as its neighbours Equations 4, 5 and 7 do.
- Seven article errors were found and left, since equations were out of scope. Phase 2 fixed them and removed
  them from [Article Errata](../ARTICLE_ERRATA.md). The A309 Equation 122 finding was first stated with the wrong reason
  and confirmed by the other line, and the operator's recomputation corrected it.
- The A385 draft is `_drafts/dromon_three_models_equations_sections.markdown`, dated 2026-08-21, unpublished.
- Phase 1 was merged at `c8e5bd6` and deployed at `b5256b0`.

## Phase 2, 2026-10-31

- **Grok again.** After the daemon was restarted onto PyDromon `c020579`, which admits Grok's empty home records, and
  two leftovers of the operator's own tests were removed, Grok's model ran its first turns. Dromon then refused Grok's
  `search_tool` meta-tool, through which Grok reaches every MCP tool, Dromon's mail included. The defect was reported
  to the PyDromon session, which is fixing it on `fix/grok-tools`. Grok stayed held for the whole phase.
- **The seven errors are fixed.** Opus fixed A306, reviewed by Luna. Luna fixed A308 and A309, reviewed by Opus. Each
  review recomputed every value, and it found two stale dependents, A308's "fifty-three kilogrammes" and A309's
  18,220 kg, which Luna then fixed. Luna also relabelled A309 Eqs 76 and 77, which used `m_1` for the mass after
  jettison. The operator approved both A306 choices before any edit.
- **The Opus engine died twice** on the 1 MiB message limit of Dromon's Claude reader while editing the 2.6 MB A306
  post. The likely trigger is the Edit tool's result, which carries the whole original file. Large posts were then
  edited through the shell. PyDromon has queued a fix that raises the limit.
- **A385 records phase 2** in "The Second Phase", reviewed and signed off by Luna.

## Grok Admitted, 2026-10-31

Grok joined after four more PyDromon fixes, each found from a live Grok turn and reported to the `Op55-pydromon`
session, which owns that checkout. Each fix was merged there before the blog daemon was restarted onto it.

| PyDromon | Defect |
|---|---|
| PR 97, `4a0c95d` | `search_tool` and `use_tool` refused, so a Grok line could not reach Dromon's mail |
| PR 99, `bcd04d0` | Dromon never requested the line's model, so Grok ran `grok-4.6` and the turn was refused |
| PR 101, `f60e91d` | Grok calls named only in `_meta["x.ai/tool"]`, so every Grok tool call was refused |
| PR 102, pending | `list_dir` reports kind `other`, and a refused file-backed `use_tool` named the wrong cause |

The operator also gave the line `Read`, `Grep` and `Glob`, and told it to avoid `list_dir` and to pass `use_tool`
arguments inline. Grok then recomputed every phase 2 value from the articles' own inputs, independently, and found no
discrepancy, wrote its report, and sent notes for A385, which Opus added and Luna reviewed. The eleven questions recorded
under Grok's name were Dromon's own hold questions, which the event log shows. Grok asked none of them.

## Operator-Side Changes and Failures

- The Grok home `~/.grok/dromon-home` needed its empty entries removed once, its `sandbox.toml` extended to deny
  the blog's `.dromon` paths and the credential directories, and a suggested `read_only` entry for the
  worktree's `.git` file removed, because Grok refuses a file there. A backup is `sandbox.toml.bak-20261030`.
- A loop that would have removed the empty entries before every Grok turn was refused by the permission
  classifier, and was not worked around.
- The operator's mail watcher requested more than the fifty-message limit and failed silently, so a held Luna
  line and the Opus completion report went unseen for about an hour.
