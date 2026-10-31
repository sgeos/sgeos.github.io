# Harness experience report, line grok

Grok 4.7 on Grok Build, worktree `tmp/worktrees/grok`, branch `dromon/grok`. This report covers what this line could see on the turn after phase 2 had already been merged at `9ff3d6c`. Claims are marked **Fact**, **Inference**, or **Judgement**.

## 1. What worked well

**Fact.** On this turn `search_tool` returned the Dromon mail tools and `use_tool` called them. The mailbox opened, messages could be read, and `line_status` reported the line running rather than held, at commit `9ff3d6c4686aa413468f09245138900ecb554e99`, with Luna and Opus idle on the same commit and no leases held.

**Fact.** The operator's task message named the commit range `b5256b0..9ff3d6c`, the three posts, and the equations to recompute. `git diff` of that range is 26 lines across the X-9, X-11, and X-12 posts. Reading those posts by line range, and searching them, was enough. The posts did not have to be loaded whole.

**Fact.** The shell could run Python on the inputs printed in the articles. The recomputation did not need network access, a deploy gate, or a write to a post.

**Fact.** The other worktrees were readable. Luna's notes and Opus's draft of A385 were on disk at the same commit, so this line could see what the article already claims about Grok without asking either line to resend it.

**Judgement.** A task that names commits, paths, and equation numbers is what made an independent check possible for a line that had missed the editing. The check did not depend on trusting the other lines' figures, which is the property phase 1 had shown was needed.

## 2. What got in the way

**Fact.** This line did not take part in phase 1 or phase 2. Both are merged. The operator's message `m-5efc213dabb0` says the line was held all day on Dromon defects. The operator's message `m-34b532c78ead` says the immediately previous turn was held only because Dromon refused `list_dir`, that the refusal is a known defect, and that everything else on that turn passed.

**Fact.** The standing instructions for this line say that Dromon refuses Grok's `search_tool` meta-tool and that, until a fix, the line cannot read mail. They also say a call to any tool outside a short allow-list ends the turn and holds the line, and they name `list_dir` as one to avoid. On the turn that wrote the first version of this report `search_tool` worked. This line did not call `list_dir`.

**Fact.** That same turn was held before its mail left. The operator's message `m-04a26aaf03ca` says Dromon accepts `use_tool` only with an inline `tool_input`, and that the `tool_input_file` form was refused, so none of the four messages was sent. The same message says scratch files belong under this worktree's `tmp/` and not under `/tmp`. The drafts had been written under `/tmp`. This later turn sends them with an inline `tool_input`.

**Fact.** The operator's message `m-63d91d57b69a` says a later turn was held by a harness defect. Grok sends `get_command_or_subagent_output` with ACP kind `other`, and Dromon allows only `execute` for it. The turn had started `python3.13 _verify.py` in the Opus worktree and then called that tool to wait. The command was terminated. Until a fix is merged and the daemon restarted, this line must run every command in the foreground and must not call `get_command_or_subagent_output` or `kill_command_or_subagent`.

**Inference.** The previous hold happened because the model followed the general tool list, which still offers `list_dir`, rather than the side instruction that Dromon refuses it. A refused call is not reported back as a tool error the model can correct. It ends the turn.

**Fact.** The operator's message `m-3dc701bb75f0` settles this from the event log. All eleven questions recorded with sender grok, from `q-983f30f8aa66` at 2026-10-30T22:52Z to `q-956960e9e9d7` at 2026-10-31T07:13Z, are Dromon's own hold questions. Dromon raises them under the held line's name. This line asked none of them, and no sent mail of this line's was lost. The empty sent record before 07:13Z is correct, because this line had sent nothing until then. The first `list_sent` used `unanswered_only` and returned nothing for the further reason that the operator had already answered the hold questions.

**Fact.** `read_mail` on each question identifier returns a body this line did not write. Each begins "Dromon held line grok, which had a turn fail and sent no operator mail during it." Each offers only the choice `resume`. The sender field says the question is from grok. There are eleven identifiers and nine distinct failure texts. Two texts were raised twice. The texts are a home directory holding hook and plugin entries, a sandbox profile that does not deny `.dromon`, the engine closing its connection, a project `.claude` directory the line would load, a home `.grok` directory that would load another harness, `search_tool` used when the line was not given it, the driver for `grok-4.7` refusing the model `grok-4.6`, a tool-call kind of `other` that does not agree with `list_dir`, and `use_tool` used when the line was not given it.

**Fact.** `line_status` does not say who wrote a question. Retained session transcripts contain no call that invokes `ask_operator`. The earlier inference, that this line asked those questions, is withdrawn. The operator's reading of the event log is the source for the fact that Dromon raised them.

**Fact.** Peer mail still in the mailbox is the phase 1 plan. Opus asked this line to review A309. Luna proposed a split. Both messages predate the merge. Acting on them would have repeated finished work.

**Fact.** The injected instructions forbid `todo_write`, subagents, `web_fetch`, `gh`, commit, and push for this line, on pain of a hold. This line did not call them. The other lines' reports describe running the deploy gate and editing posts. This line was told not to edit posts, so that difference was not exercised on the assigned task.

**Judgement.** The costly failure was not the arithmetic. It was that the line could not say it was held, so the other two planned as if a third worker might still appear, and then had to replan without it.

## 3. What I could not see or do

**Fact.** This line cannot read `.dromon/`. The account of empty hook-path and plugin entries, of four edits to the Grok Dromon home, of a corrupted sandbox profile, and of a refused removal loop is the operator's account as A385 already records it. This line did not observe those events.

**Fact.** This line has no transcript of its own held turns. It knows the last hold was `list_dir` only because the operator said so.

**Fact.** `secret/` in the worktree is not readable. Nothing in the assigned task is there.

**Fact.** The eleven hold questions are recorded under this line's name and are addressed to the operator, not to Opus or Luna. They are Dromon's questions. The line still has no sent message to either peer from either phase.

**Judgement.** A line that is the subject of the failure is the worst witness to the failure's cause. The article is right to attribute the early holds to the operator's report rather than to anything Grok measured.

## 4. Ranked harness suggestions

1. **A refused tool call should return an error to the model, not hold the line.** Problem it answers: one call to `list_dir`, which the general tool list still offers, ended a turn and held the line. A later turn was held the same way for `use_tool` with `tool_input_file`, a form the tool schema still offers. A third turn was held because `get_command_or_subagent_output` is sent with ACP kind `other`, which Dromon does not allow. The model cannot learn the defect inside the turn that hits it.

2. **Give a hold question a sender distinct from the line.** Problem it answers: Dromon raises hold questions under the held line's name, so they appear in `list_sent` as if the line had asked them. This line mistook them for its own mail. The operator stated this suggestion in `m-3dc701bb75f0`. `line_status` also does not mention them.

3. **Do not offer a tool the harness will refuse.** Problem it answers: the Grok line is told, in two places, both that `list_dir` exists and that calling it holds the line. The shell command `ls` works. The tool list should say that, and should not present `list_dir` as callable.

4. **Do not assign a silent line a share of the work.** Problem it answers: phase 1 gave this line an article and two reviews while it could not answer mail. A line that has not sent a message should appear in the plan as absent, not as a pending reviewer.

5. **Put the question text in the operator's reply, or say that the reply answers a harness hold.** Problem it answers: the mailbox showed the single word resume, and the question text was visible only by opening the question identifier. The line first treated those replies as answers to questions it had asked.

6. **Let a released line comment on a draft that says it never ran, before that sentence is treated as final.** Problem it answers: A385, as merged, says the Grok model never ran and took no part in either phase. That was true through the merge. It is false as a statement about the line after release, and only this line is in a position to add the limit.
