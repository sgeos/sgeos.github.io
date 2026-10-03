# Work Durability

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

How to keep a long turn's work when the turn does not survive to deliver it.

**The root cause is that the response channel is not storage.** Text an agent emits to the human is
delivered only if the turn completes. A turn can fail to complete for several unrelated reasons, and
in every one of them the visible output is lost while any file written during the turn survives. The
lesson is not to work faster or in smaller pieces for their own sake. It is that **the deliverable
should be on disk before the turn ends, because a turn is not a transaction and nothing rolls back
except what was never written down.**

This file is the durability companion to [Verification Traps](./VERIFICATION_TRAPS.md), whose root
cause is asserting a property instead of measuring it. These are different failures. A verification
trap ships a wrong claim. A durability failure ships nothing at all.

---

## A turn can end before it delivers, and the ways are unrelated

Any of these ends a turn with its visible output discarded.

| Cause | Warning | Recoverable by retry |
|---|---|---|
| A safeguard flags the turn | None | Sometimes, and not by repeating the same request |
| Context is exhausted | Some | Yes, after compaction |
| The human interrupts | None | Yes |
| A network or service error | None | Usually |
| A tool error late in a long turn | None | Depends on the tool |

**None of them is predictable from inside the turn**, so none of them can be planned around by
judging whether this particular turn is at risk. The habit has to be unconditional.

---

## The response channel is not storage

**What happened.** A research pass for A365 ran fourteen minutes, fetched seven budget justification
books, queried the federal award record, resolved an engine through the cruise missile that shares
it, and identified the article's keystone. The turn was flagged by a safeguard at the moment the
research finished and drafting was about to begin. **No draft existed. Not a line of article prose.**

The data survived, because every document had been fetched to a file and every instrument written to
a file. **The findings did not survive, because they had only ever been said.**

**The check.** Before a turn ends, ask what a fresh session with this repository and no conversation
would be unable to reconstruct. That is the part that is only in the channel.

**The habit.** Write the deliverable to disk as it is produced, not when it is finished.

---

## Data on disk is not findings on disk

**This is the part that is easy to get wrong while believing the work is safe.** An instrument that
reproduces a number does not reproduce the reading of that number. The A365 pass had, on disk:

- seven budget books, and a scanner that extracted every entry from them
- a diff showing six distinct versions of one programme description
- an award record with five awards and their full contract data

and it had, only in the conversation:

- that the six versions collapse to **one concept change**, datable to an eleven-month window
- that one contract description **independently corroborates** that change and freezes the original
  concept in the government's own words
- that four books running name the **binding unknown**, which is the article's keystone
- that three register counts in the resume prompt were **wrong**, and what the right ones are

**The second list is the research. The first is its raw material.** A new session reading the first
list would have to redo the second, and would not know that the resume prompt it was trusting
contained three wrong numbers.

**The check.** A research pass is not finished when the data is fetched. It is finished when a file
on disk states what the data means.

**The habit.** Keep a findings file in the working directory and append to it as findings arrive. It
costs a few lines per finding and it is the only artefact that survives everything.

---

## Write long prose to a file, not to the channel

The series already composes articles as numbered body files assembled by a script. That convention
was adopted for assembly mechanics, so that every section boundary is computed on one string in one
pass. **It has a second and larger benefit that was not the original reason: a section written to a
file is delivered whether or not the turn completes.**

**The habit.** Compose each section straight to `tmp/<article>/body_NN.md` and assemble at the end.
Keep the agent's own narration to what it did, not to a restatement of the content. A turn that
writes ten files and says four sentences loses four sentences when it dies. A turn that says
everything and writes nothing loses everything.

---

## Checkpoint a long turn on findings, not on a clock

A pass that will run many minutes should write to disk at every point where it learns something it
could not cheaply relearn. The trigger is **a finding**, not elapsed time, because a turn that
fetched ten documents and concluded nothing has lost little, while a turn that fetched one document
and overturned a premise has lost a great deal.

Findings worth an immediate line in the file:

- a number in a resume prompt, handoff or earlier article that turns out to be wrong
- an instrument that reported confidently and wrongly, and why
- a source that could not be retrieved, so it is not silently retried forever
- a reading that required several sources to reach
- a refusal, so a later sweep does not re-admit the same homonym

---

## When a subject is sensitive-sounding, route the substance through files

Some legitimate subjects read as sensitive in prose while being unremarkable in their own technical
register. A publicly designated research aircraft is a matter of public record, its budget line is
published by the Department, and its award record is open. **The engineering is still better written
as symbol definitions and displayed relations than as discursive prose**, which is also the genre's
own register and not a concession.

**The habit.** Put the engineering in the equations and the symbol table. Put the prose in files.
Keep the narration procedural. This is good practice for the article regardless, and it removes the
turn's dependence on a long passage surviving the channel.

---

## A second incident, on a pass nobody would have called sensitive

**What happened.** A377's pathological word usage pass was stopped by a safeguard twice. The
article is about where to apply perfume. The pass itself is arithmetic, being word and phrase
counts measured against the published corpus, and the article's subject has nothing in common
with the defence-adjacent research pass recorded above.

**What was lost, and what was not.** Nothing of the work. Every edit had been applied to the
article by a script before either turn narrated anything, so both turns lost only their
narration, and the pass resumed from the file.

**What the two incidents have in common, which is not the subject.** In both cases the turn was
about to emit a long passage into the channel. A365's was a research narrative. A377's was a
diction report, which is by construction a list of dozens of fragments of the author's own prose
with their surrounding clauses, stripped of the context that makes them ordinary. **A diction
pass is therefore among the most exposed passes in the workflow**, which is not obvious in
advance, and that is the reason this entry exists.

**The habit, which is the one already stated here.** Route the substance through files. Keep the
narration procedural and short. Apply edits with a script before describing them. For a diction
pass, write the measurement tables and the per-word judgements to a findings file under
`tmp/<article>/` and report the counts and the decisions instead of the fragments.

**What this is not.** It is not a reason to skip the pass, which found and fixed three formulas
in A377. It is not a reason to shorten the article. And it is not evidence that the article's
subject is the cause, because the first incident's subject was unrelated and the second
incident's article had already passed the same safeguard throughout the four passes before it.

---

## What this does not change

**None of this is a reason to shorten the work.** The standing directive is that these articles have
no length limit and no reference limit, and durability is a question of where output goes rather than
how much of it there is. A twelve-section article written to twelve files is exactly as long as one
written to the channel, and it survives.

**Nor is it a reason to commit prematurely.** Files under `tmp/` are gitignored and that is correct;
they survive a lost turn, a compaction and a new session. They do not survive someone clearing
`tmp/`, so a findings file is a working artefact and not an archive. Anything that needs to outlive
the working directory belongs in the article, in the process files, or in a commit.

---

## Related Sections

- [Verification Traps](./VERIFICATION_TRAPS.md) for the companion failure mode, asserting instead of measuring
- [Handoff Prompt](./HANDOFF.md) for the resume prompt a planned compaction writes
- [Communication](./COMMUNICATION.md) for the human-facing channels and what belongs in each
- [Content Workflow](./CONTENT_WORKFLOW.md) for the draft and publish pipeline
