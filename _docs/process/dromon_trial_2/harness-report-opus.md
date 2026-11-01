# Harness Report, Line opus

> **Navigation**: [Process](../README.md) | [Documentation Root](../../README.md)

This report covers the second Dromon trial on the blog, in which three lines reviewed the main checkout's `tmp/` and promoted what deserved a tracked home. The line `opus` ran Claude Opus 5.5 on Claude Code in the worktree `tmp/worktrees/opus`. It inventoried the article scratch from A297 to A385, implemented P1, P2, D1 and R2, reviewed P3, D2, S1, S2 and R1, integrated all three worktrees and ran the single `./_check.sh`. Each claim is marked **Fact**, **Inference** or **Judgement**. It is written for the people who build the harness.

## 1. What Worked Well

**The standing brief carried the work across compaction.** **Fact.** The session compacted automatically at about 171,000 tokens of context against a threshold of 150,000. The new engine session opened with the brief set by `set_brief`, which named the integration script, the open decision and the next action. The first turn after compaction resumed the integration without re-deriving any review result. **Judgement.** This was the single most valuable harness feature for a long task, because the compaction summary alone does not reliably preserve paths and exact verdicts.

**Mail let three engines from three companies review one another's code.** **Fact.** Every implemented item was reviewed by a line other than its author, and three reviews found real defects that the author then fixed. Sol showed that a single inline math span can break by itself, which my documentation denied. I showed that Sol's Notation row formatter mishandled an underscore after a digit and that Grok's not-found sweep read only DOI references. **Inference.** None of the three defects would have been found by the author alone, because each was found by running the code on a case its author had not chosen.

**Leases worked as intended for the shared files.** **Fact.** I held `test_lib`, `lib_readme` and `blog_py` while editing and released each afterwards. No two lines edited the same shared file at once. The one integration conflict was two adjacent rows in `_lib/README.md` written in separate worktrees, which a lease cannot prevent and a three-way merge resolved.

**The turn and cost counters were visible at every turn.** **Fact.** Each turn opened with the autonomous turn count and the estimated cost against its limit. **Judgement.** This made it straightforward to keep the work inside budget without asking.

**Worktree isolation made integration auditable.** **Fact.** Because each line wrote only its own worktree on a branch from `66bd073`, integration was a three-way `git merge-file` of each changed file against the common base. A check afterwards confirmed that all 761 lines added by any line were present in the merged tree.

## 2. What Got in the Way

**Reviewing another line's code meant reconstructing its tree.** **Fact.** The sandbox denies writes outside my worktree, so running another line's tests in its own worktree failed 13 times with `PermissionError`, since the tests write scratch files beside themselves. I ran every review on a `git archive 66bd073` copy with the other line's changed files overlaid. **Judgement.** This was workable but cost several turns and is easy to get wrong, because an overlay can silently miss an untracked file.

**Mail crossed in flight and repeated itself.** **Fact.** Grok asked me to re-review P3 after I had already accepted it in an earlier message. Sol sent several notes that restated earlier ones, and one turn opened with seven new messages of which four were superseded by a later one. The mailbox reports 104 unanswered messages, most of them notes that need no answer. **Inference.** The unanswered count includes notes, so it does not tell a line what actually awaits it.

**A finding was raised from mis-rendered tool output.** **Fact.** Sol reported doubled backslashes in my documentation. The file contains none, and Sol later withdrew the finding, explaining that it had read JSON-escaped tool output as the file's bytes. **Inference.** An engine that shows tool output escaped can produce false review findings about escaping, which is exactly the subject of this trial's mathematics work.

**Background jobs did not survive session changes.** **Fact.** Long site builds started in the background were lost when the session restarted or compacted, and some background tasks reached their time limit. A first version of my rendered diff tool was quadratic on the feed files and had to be stopped. **Judgement.** The quadratic diff was my defect, but the loss of a running build at compaction was not, and it cost a rebuild of several minutes each time.

**The address `@operator` does not resolve.** **Fact.** Mail to `@operator` failed. The operator must be addressed as `@bsechter`. LINES.md says so, but the failure arrives only after the attempt.

**A correction cannot be threaded to the message it corrects.** **Fact.** Sending a correction with `reply_to` set to my own earlier message to the operator was refused with "a reply to m-1698659dad34 must go from @bsechter to opus". The correction went as a separate message that names the first in its text.

**`wake_after` with a task identifier failed.** **Fact.** One call naming a background task as `task_id` was refused because the identifier did not match a running task. A plain timed wake worked.

**Git commands that touch the index are denied.** **Fact.** During integration, `git restore --source=66bd073 --worktree` failed with `Unable to create '.../.git/worktrees/opus/index.lock': Operation not permitted`. I restored with `git show` redirected into each file instead. **Inference.** The denial follows from the rule that lines may not commit, but it also blocks read-mostly recovery commands that write no commit.

**Sandbox noise obscured real output.** **Fact.** Many commands printed `setpgid` warnings, and `_lib/test_sources.py` produced six network denials for `api.crossref.org` and `api.openalex.org` on every run even though its tests pass offline. Process substitution such as `diff <(...)` and heredocs failed when the working directory was another line's worktree.

## 3. What I Could Not See or Do

**I could not list my own background processes.** **Fact.** `list_processes` reported that it is unsupported for this engine, so after a compaction I could not tell whether a build I had started was still running except by reading its output file.

**I could not see whether another line had read a message before it acted.** **Fact.** `list_sent` shows whether a message was read, but the other lines acted on stale state several times. **Inference.** A line sometimes reads a batch of mail and acts on an older message before reaching the newer one that supersedes it.

**I could not run the deploy gate exactly as written.** **Fact.** `_check.sh` calls `python3`, `bundle` and `ruby` from `PATH`. On this machine `python3` is Python 3.14 while the work used 3.13, and the bundle lives in the main checkout's `vendor/bundle`. I ran the gate with a shim directory ahead of `PATH` and `BUNDLE_PATH` set. **Judgement.** This is a property of the machine rather than the harness, but a line has no way to learn the intended interpreters except by trial.

**I could not commit, which was correct.** **Fact.** All work remains uncommitted in my worktree at `66bd073` for the operator's session to commit. **Judgement.** This boundary was clear and caused no difficulty.

## 4. Ranked Harness Suggestions

1. **Give reviewers a writable copy of another line's tree.** Problem answered: a reviewer cannot run the author's tests in place and must rebuild the tree by hand from an archive and an overlay, which is slow and can omit untracked files. A harness command that materialises another line's worktree as a scratch copy inside the reviewer's own would make every review start from the exact code under review.
2. **Keep background processes across compaction and let a line list them.** Problem answered: builds of several minutes were lost at compaction, and `list_processes` is unsupported, so a line cannot tell what survived.
3. **Count only messages that ask for a reply as unanswered, and mark superseded mail.** Problem answered: 104 unanswered messages, mostly notes, hid the few that needed action, and stale requests were acted on after their answers had been sent.
4. **Resolve `@operator` to the project's operator, or refuse it with the correct address.** Problem answered: the first operator message failed and the fix required reading the rules again.
5. **Silence the `setpgid` warnings and declare expected network denials.** Problem answered: real command output was interleaved with harness noise on almost every call.
6. **Permit index-only Git recovery commands while still refusing commits.** Problem answered: `git restore` was denied during an integration that needed to undo a partial merge, and the workaround rewrote each file by hand.
7. **Report a wrong `task_id` to `wake_after` with the list of valid identifiers.** Problem answered: a refused wake left the line to guess at the identifier format.
