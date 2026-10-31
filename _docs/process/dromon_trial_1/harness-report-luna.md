# Harness Experience Report for Luna

## 1. What worked well

**Fact** The operator answered the team plan with clear changes, reassigned A308 and A309 after Grok was held, and took responsibility for merging the worktrees and running one combined gate.

**Fact** Mail between Opus and Luna carried specific review questions and equation tags. I could read the other line's classification file while writing only in my own worktree.

**Fact** I cross-reviewed Opus's A308 file from his worktree. `equations.py check` reported all 105 equations consistent. I initially recommended tags 40 and 41 as bespoke, then agreed with Opus to classify them as standard under the same rule as A307 tag 17: they express general crossover or onset relations without article-chosen inputs. The file owner retained edit authority.

**Inference** The division between file ownership and read-only cross-review allowed independent classification while keeping edits auditable.

## 2. What got in the way

**Fact** The kickoff instructions said two unchecked A306 claims were in ARTICLE_ERRATA.md, but that file had no A306 entry. The operator clarified that the claims were in the gitignored tmp/eq2/FINDINGS.md in the main checkout.

**Fact** The operator reported that Grok could not run because its engine wrote empty hooks-paths and installed-plugins entries into its Dromon home on startup, after which Dromon held the line before the model ran. A removal loop was refused. The operator said this refusal was correct.

**Fact** My first skeleton command used A307 as the argument and failed because the command opens a post path. The command help showed the generic placeholder POST but did not show a concrete file path.

**Fact** The mail tool refused one message because I supplied the identifier of my own outgoing message as `reply_to`. Retrying without `reply_to` delivered the message.

**Fact** At the time of Opus's A307 review, he reported that two earlier review messages from me had not reached his inbox. Sent-message tracking later listed them as delivered. The timing is unavailable, so I cannot distinguish delay from another delivery-state discrepancy.

**Inference** The stale A306 path and the unavailable Grok line delayed agreement on ownership and changed the cross-review assignments.

## 3. What I could not see or do

**Fact** I could read Opus's worktree and could write only in Luna's worktree. I could not access the closed Dromon configuration directories.

**Fact** I learned the reason for Grok's hold from the operator's mail. The line status available to me showed that Grok was held but did not give me the cause.

**Fact** I have had no sandbox denial or file-write refusal in my worktree, and I have no evidence of permanently lost mail. I have not observed a task capability available to Opus but unavailable to Luna.

**Fact** The process-list tool returned no processes and said the daemon cannot identify or stop processes because it cannot read another process's environment. I could not use it to inspect Opus's active gate or background work.

**Inference** A line can assess a teammate's classification from a readable worktree, but cannot independently diagnose a hold when its cause is kept in the operator's environment.

## 4. Ranked harness suggestions

### 1. Keep task artifact paths current

**Judgement** The task brief should name the current path of each referenced finding and say when that path is gitignored. This answers the mismatch between the A306 instruction and ARTICLE_ERRATA.md.

### 2. Add a shared lease for the deploy gate

**Judgement** A declared gate lease should guard the shared build resource. Mail warnings can arrive after a recipient has begun its own run, so they cannot prevent overlapping builds. This answers the concurrency race described in Opus's report and the lack of process visibility from my line.

### 3. Show hold reasons in line status

**Judgement** A held status should include a short cause and the authorized next step when one is available. This answers the inability to plan around a held teammate without waiting for an operator explanation.

### 4. Use a concrete post path in command examples

**Judgement** The equations documentation should show a real invocation such as python3 _lib/equations.py skeleton _posts/YYYY-MM-DD-slug.markdown. This answers the ambiguity of the placeholder POST, which I initially read as an article number.

### 5. Provide a read-only cross-worktree review link

**Judgement** A mail message could attach or link a named file in another line's worktree with read-only access. This answers the need to copy absolute paths into mail before a reviewer can find the classification artifact.

### 6. Explain reply direction in mail validation

**Judgement** The mail tool should state that `reply_to` must identify an incoming message in the current conversation. This answers a rejected outgoing message that had to be retried without a reply identifier.

**Fact** Opus cross-reviewed A307 and identified tag 80 as a textbook short-period approximation. After rereading the brief, I changed tag 4 to bespoke, tag 5 to bespoke as its derived unit conversion, and tag 6 to bespoke. Opus agreed with tag 4, but argued tag 6 should remain standard. I left tag 6 bespoke and reported the unresolved disagreement for the operator. The validator reports all 123 A307 equations consistent, with 72 standard and 51 bespoke. `./_check.sh` passed on the final classification with 384 posts checked, zero errors and warnings, 178/178 and 94/94 library tests, 14 Ruby tests, successful production build and a clean rendered audit of 551 pages.

**Judgement** Tag 4 applies the standard inertial error relation after assigning the full reported circular error probable to gyroscope drift. Tag 5 converts that assumption-based result into different units. Both are bespoke. Tag 6 applies the same relation to the reported growth in total navigator position error. I judge the source does not establish that all growth comes from gyroscope drift, so tag 6 is bespoke. Opus agrees on tag 4 but considers tag 6 standard because its numeric input is reported. I left tag 6 bespoke and reported the remaining disagreement for the operator.
