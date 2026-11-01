# Operator Report

> **Navigation**: [Dromon Trial 2](./README.md) | [Process](../README.md)

This report covers the second Dromon trial on the blog from the operator's side. The operator session is Claude
Opus 5.5 on Claude Code, named `Op55-blog`. It wrote the brief and the project file, started and supervised the
daemon, answered every hold, approved the plan, verified the integrated work and committed it. The daemon ran
PyDromon `main` at `f5f8da1` from 2026-10-31 23:36Z. Each claim is marked **Fact**, **Inference** or
**Judgement**. It is written for the people who build the harness.

## 1. What Worked Well

**The team found a live defect that eight months of scratch had worked around.** **Fact.** The inventory turned
up three private detectors for kramdown emphasis inside inline mathematics, copied through A362 to A368 and never
promoted. Measuring them on a production build found 18 defect blocks on 13 published pages, 10 of them written by
the tracked Equations generator. **Judgement.** A promotion review that only moved code would have missed this.
The lines measured before proposing, which is what the brief asked for.

**Review by a different engine found real defects in all three lines' work.** **Fact.** Opus found that Grok's
not-found classifier never reached the hand-written URLs it was promoted for, and that Sol's generator escape
missed an underscore after a digit. Sol found that Opus's documentation denied a case that kramdown does break. Each
author fixed the defect, and each reviewer re-ran its own case. **Inference.** The brief's rule that a reviewer runs
the code on a case the implementer did not choose produced these findings. Agreement alone would not have.

**One line shared the brief with a line that had not received it.** **Fact.** When Grok reported the old brief, Sol
wrote a copy of its own brief to its worktree, labelled it coordination data without operator authority, and told
Grok and the operator. **Judgement.** That is the correct handling of authority across lines, and it kept Grok from
inventing a task.

**Rebinding gave the operator a way to reset a session.** **Fact.** `dromon rebind` drops the engine session, and
`settings` then reported `session = new`. Grok's next turn carried the current brief.

**Integration was auditable.** **Fact.** Every line wrote only its own worktree from `66bd073` and none committed.
The operator applied the integrated diff to the main checkout and confirmed that each of the 13 changed posts is
byte-identical to `66bd073` once backslashes are removed. The operator's own `./_check.sh` repeated the line's
result.

## 2. What Got in the Way

**A resumed Grok session kept the rules it was created with.** **Fact.** The Grok line opened this trial with the
phase 2 brief. Dromon resumes the stored session `01a190cf-b536-7cb3-8c05-68b365a161af` through `session/load` and
passes the current instructions in `_meta.rules`. Grok's `system_prompt.txt` for that session was rewritten when the
turn began, and it still held the phase 2 text. `settings grok` showed `keep_session = off` and the session
identifier as read only. **Inference.** Grok applies `_meta.rules` only at `session/new`. If so, the phase 3 brief
also never reached Grok as rules, only through mail. **Fact.** `dromon rebind grok` to the same model and strategy was
refused as a no-op. The workaround was to hibernate the line, rebind it to `flexible`, rebind it back to
`subscription` and awaken it.

**`@operator` does not resolve.** **Fact.** Sol and Grok each failed to mail `@operator` with `no operator
operator`, and both fell back to replying to the kickoff. The briefs of earlier trials told lines to use
`@operator`. **Fact**, from the PyDromon implementation line. An operator address is resolved by its identifier in
`model.py` `_require_party`, which refuses an identifier that is not registered, and that check dates from
2026-10-24, before PR 114. **Inference.** `@operator` resolves only in a project whose operator is named
`operator`, and here the operator is `bsechter`, so it has never resolved on this blog.

**The `kill_all` stop policy holds a line on one slow `ps`.** **Fact.** Sol was held three times, each with the
turn not started because `ps did not answer within 10 seconds`. The daemon log holds 13 such lines across both
trials. From the operator's shell the same command, `ps -ww -U 501 -o pid=,ppid=,pgid=,args=`, took 0.04 seconds
at rest. A probe that timed it every two seconds measured 9.5, 13.6 and 15.4 seconds between 00:12Z and 00:15Z on
2026-11-01, while another project's parallel Rust test builds and a Jekyll build held the processor. **Inference.**
The cause is host load against a fixed ten-second timeout with a single attempt. Each hold is a turn failure that
waits for an operator answer.

**The engine offers tools the line may not call.** **Fact.** Grok's fresh session called `todo_write` and was held.
The tool list had been in the phase 2 brief, and the operator dropped it from the new one. **Judgement.** The fault
here is shared. The operator removed a rule the engine still needed. The harness offered the tool and taught the
line its boundary by holding it.

**The operator mailbox carries history that does not need answering.** **Fact.** It held 93 messages at kickoff, 13
unread and 45 counted unanswered, from earlier phases. Two phase 3 notes from Opus were still unread. **Fact.** The
operator's watcher compared the mailbox's total count, a fix from the last trial. It caught every message this
trial.

**A retired line cannot be removed.** **Fact.** The `luna` line was removed from the project file, and
`dromon status` still lists it as idle, because lines persist in the event log. No command retires a line.

**A message the operator sent could not be read back.** **Fact.** `dromon read m-f993b843cd08`, the operator's own
approval, returned nothing, since `read` opens the operator's mailbox and the message went to lines. The operator
recovered the text from its own session.

## 3. What I Could Not See or Do

**The operator could not see whether a line's background job was running.** **Fact.** Opus ended a turn while its
`./_check.sh` ran in the background. All three lines showed idle, so the operator's watcher exited as if the work had
stopped. The operator found the gate only through the process table, and waited on its process identifier.
**Inference.** A line's status that counted a running background task would have shown this.

**The operator could not see why a hold happened beyond its one line.** **Fact.** The hold for `ps` named the
timeout and nothing about load. The operator had to write a probe to learn the cause.

## 4. Ranked Harness Suggestions

1. **Refresh a resumed session's rules, or start a new session when they change.** Problem answered. A Grok line ran
   on a brief two phases old, and the only reset was a double rebind under hibernation. A changed instruction hash
   could force `session/new`, or `rebind` could accept a same-model rebind as an explicit session reset.
2. **Retry the process listing with a longer timeout before holding a `kill_all` line.** Problem answered. On a
   loaded shared host `ps` took 9.5 to 15.4 seconds, and Sol was held three times for a condition that passed in
   seconds. A retry with backoff, and a hold message that reports the measured time, would make the hold rare and
   legible.
3. **Resolve `@operator` to the project's operator, or refuse it naming the right address.** Problem answered. Two
   lines lost their first operator message.
4. **Show running background tasks in `dromon status`.** Problem answered. A line that ended its turn with a gate
   running looked idle, and the operator's watcher stopped.
5. **Withhold the tools a line is not given from the engine's tool list.** Problem answered. Grok learnt its tool
   boundary by being held.
6. **Let the operator retire a line and read its own sent mail.** Problem answered. A retired line stays in status,
   and an approval could not be read back from the harness.
7. **Separate notes from requests in the unanswered count.** Problem answered. Every line and the operator saw a
   standing count of historical notes that hid what needed action.
