# Equation migration status for A306 to A309

Written by the Claude Code session that ran the A290 to A368 Equations section migration and met the original
A306 to A309 problem. The pilot passed it to the operator on 2026-10-31. Reproduced verbatim.

**What happened.** The A290 to A368 equation migration produced validated classification files for 75
articles, A290 to A305 and A310 to A368. A306 to A309 were the only articles in that range left
without one. When the drafting agents tried to write the classification files for those four
articles, an automated safety check in the Claude Code session refused the writes. I then tried to
write the same files myself and was refused too. From that point the check refused every shell
command and every file write in the session, and only reading files still worked.

**What is known.** The refusal came from the session's safety check, not from the repository tooling,
the pre-push hook or the article content validators. The check's own message said it was reacting
to earlier content in the conversation and would keep doing so. It also said not to retry or work
around it. No classification files for A306 to A309 exist. Nothing for those articles was
committed, and no tracked post was changed.

**What is not known.** The check did not name the content that triggered it, and I have not
established which part of the conversation it was. It is therefore not confirmed that anything in
A306 to A309 themselves is the cause. The refusal may simply have built up over a long session and
first fired on these files.

**What was decided.** I did not hand the refused writes to other agents, because that would have been
a way around the refusal rather than an answer to it. A306 to A309 were taken out of scope for the
follow-up goal statement. One related finding about A306 is recorded unverified in
tmp/eq2/FINDINGS.md: the bending moment in Eq 105 appears to be about twice too high.

**Suggested next step.** Try classifying A306 to A309 in a fresh session, one article at a time. If the
refusal happens again on the same articles in a clean context, that points to the articles. If it
does not, that points to the conversation in the earlier session.
