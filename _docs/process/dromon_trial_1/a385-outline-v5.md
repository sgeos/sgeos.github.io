# A385 phase 3 outline, v5

This file is self-contained and supersedes v1 to v4. It is the text to send to the operator.

## Thesis

Luna's wording, which grok also endorses: "This case suggests that reliability depended on three distinct controls: access to a turn, legible coordination state, and independent recomputation. Their failures shaped the work, but model and team judgement also caused errors, and the third line's check came after merge."

Support is assessed separately for each claim. The expected verdict is partially supported, and it is decided after drafting.

## Outline

The pilot's five parts, with the narrative carried by three findings. Each event is told once, and long runs of figures go in tables.

1. **Opening.**

2. **The Problem.**
   - The general pass used eleven agents over 233 articles and 8,122 equations. It produced validated files for A290 to A305 and A310 to A368, so A306 to A309 were the only gap in that range.
   - A306 to A309 hold 483 display equations, 115, 123, 105 and 140, recomputed from the equation data files.
   - Both FINDINGS records are reported, without asserting two separate incidents.
   - The written account of the session that ran the general pass is the source for the refusal. Its own safety check refused the drafting agents' writes for the four articles, then the lead's writes and shell commands, and after that only reads worked. The check said it was reacting to earlier conversation content, and said not to retry or work around it.
   - The trigger is unknown, and it is not established that A306 to A309 caused it.
   - Separately, the A306 agent asked the lead to run its unreviewed script, and the lead declined. The lead also did not hand the refused writes to other agents.
   - The account recorded Eq 105 as unverified. Phase 2 confirmed it and fixed it.

3. **The Thesis.**

4. **The Trial as a Test.**
   - One table of the team and harness, with Op55-pydromon as a fourth agent.
   - The account proposed a test: classify A306 to A309 in a fresh session, one article at a time. A refusal there would point to the articles, and none would point to the earlier conversation.
   - The trial was not an identical replication. It had no refusal of that kind, which is evidence for the conversation explanation but not a clean test.
   - The confounds are a different harness configuration, models from three providers, and Opus taking three articles rather than one.

5. **Finding One, access to a turn.**
   - Grok's eleven holds and nine failure texts, in one table.
   - Op55-pydromon's live repair of each defect a Grok turn exposed, as one chronology.
   - The Opus turns lost to the 1 MiB message limit.
   - Luna's hold.

6. **Finding Two, coordination state.**
   - A plan that gave work to a line that had never answered.
   - Crossed plans and late mail.
   - The operator's failed mail watcher.
   - Reviews of stale revisions, including this outline's own rounds.
   - Dromon hold questions shown under Grok's name, a case of the sender label differing from authorship.
   - The operator's merge, which copied the draft without checking the lease and missed a lease-held Opus edit. The sources are the operator's statement and the opus and luna records.

7. **Finding Three, independent recomputation.**
   - Eq 122, confirmed for the wrong reason.
   - The missed dependents.
   - The unchecked recollection.
   - Grok's third check confirmed the corrected arithmetic after the merge, and luna recomputed it. It audited the result but could not prevent the merged errors.
   - **The sent-mail sequence, told as a failure to keep the sender label apart from authorship.**
     - The unanswered-only list_sent call returned nothing.
     - The unfiltered call listed eleven entries under Grok's name, with bodies Dromon generated as hold questions. The event log explains the sender label, and the operator's finding that Grok wrote and sent none of them is correct and compatible with that view.
     - Grok withdrew its sentence that the sent record was not empty by citing the operator, without re-running list_sent.
     - The later Opus edit dropped the unfiltered-list observation, and luna signed off on that revision.
     - The operator's merge missed the lease-held edit, so the base kept the more accurate text.
     - The article does not say that a first-hand account was withdrawn, or that the operator contradicted a correct claim.

8. **The Work Delivered.** Two tables.

9. **Judging the Thesis.** Claim by claim.

10. **Takeaways.**

11. **Epistemic State.**

12. **Out of Scope, Conclusion, Equations, References.**

## Writing

Each writer drafts in their own `tmp/dromon_trial3/`, and opus assembles under the article lease. If a section is late, opus writes it and its owner reviews it.

| Writer | Sections |
|---|---|
| opus | 1 to 4, 7, 8, 12, and a first draft of 9 |
| grok | 5, and the hold-question takeaway sent to luna |
| luna | 6, 10 and 11 |

## Reviews

Each reviewer recomputes every figure and quotes the line or digest it read.

| Reviewer | Sections |
|---|---|
| luna | 1 to 5, and 8 |
| grok | 7, the tables in 8, and 9 |
| opus | 6, 10 and 11 |

## Passes

Each pass is a separate round after the assembled draft exists. This is the allocation that luna confirmed in m-c8a4410057a0 and grok confirmed in m-cb7ccac8be17.

| Pass | Lead | Reviewer |
|---|---|---|
| Equations | luna | grok |
| References | opus | luna |
| Readiness | opus | luna |
| Diction | grok | opus |

- References use full metadata and stay marked unverified until the operator verifies them.
- The gate runs with python3.13, since the default python3 3.9.6 cannot import tomllib.
- The article lease is released before any merge request.

## Request to the operator

The Op55-pydromon repair chronology, giving each defect, its fix, and the commit or PR.
