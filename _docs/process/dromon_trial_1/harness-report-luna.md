# Luna harness experience report

## 1. What worked well

- **Fact** The isolated Luna worktree kept the article edits in my branch while I could read Opus's worktree for an independent review.
- **Fact** The lease tool let me acquire and release `a308` and `a309` before and after editing those articles.
- **Fact** Mail allowed the operator to approve the work split and the two A306 choices before edits began. It also let us exchange equation inputs and review results.
- **Fact** The equation tooling regenerated the tags and Equations sections, and `equations.py check` reported 105 consistent equations for A308 and 140 for A309 after the edits.

## 2. What got in the way

- **Fact** Scheduled wake notes were delivered later than their due times. One note due at 04:17:48 UTC arrived at 04:17:49 UTC, while earlier notes arrived minutes after their due times. The delay made a wake useful as a reminder, but not as a precise deadline.
- **Fact** The session was automatically compacted and later resumed in a new engine process. The standing brief and repository notes helped restore the task state, but mail and worktree state still had to be checked against the current checkout.
- **Inference** Mail replies arriving across turns made it difficult to know at a glance whether a review or gate was complete. A concise status message naming the reviewed files, lease state, and gate state reduced that ambiguity.
- **Fact, reported by Opus** Opus reported that a tool result for an approximately one megabyte post exceeded Dromon's one MiB message limit, and that two Edit calls failed with `Tool permission request failed: AbortError: Stream closed`. Opus used line-scoped Python replacement for the equation edit. I did not reproduce those failures myself.

## 3. What I could not see or do

- **Fact** I could read other worktrees but was instructed to write only in Luna's worktree. The shared lease state coordinated access to shared resources, while each worktree contained separate edits until the operator integrated them.
- **Fact** The `.dromon` directory was denied by the filesystem policy. I could not inspect its internal state and used the mailbox and lease tools for coordination.
- **Fact** I could not commit, push, use GitHub CLI, or run network fetches under the task rules. The operator owns integration and outward-facing changes.
- **Inference** The worktree model supports parallel editing, but cross-worktree review depends on explicit messages because local Git status does not show another line's uncommitted changes.

## 4. Ranked harness suggestions

1. **Judgement** Provide a compact shared task status for active line, lease holder, review state, and gate state. This would answer the coordination problem created by replies spread across turns and separate worktrees.
2. **Judgement** Enforce or surface a reliable output-size limit before sending tool results to the engine. This would answer the reported one MiB failure and help avoid losing a turn to an oversized file read.
3. **Judgement** Make editor-tool stream failures retryable or provide a clear fallback path. This would answer Opus's reported `AbortError` failures without requiring a custom script for a narrow edit.
4. **Judgement** Show scheduled wake delivery latency and distinguish a reminder from a deadline. This would answer the mismatch between due time and actual note delivery.
5. **Judgement** Preserve a short, automatically refreshed resume summary across compaction and engine restarts. This would answer the repeated need to reconstruct active work from mail, Git state, and process files.
