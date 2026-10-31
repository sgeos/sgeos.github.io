# Harness Experience Report, Line opus

Line `opus` is Claude Opus 5.5 on Claude Code, working in `tmp/worktrees/opus` on branch `dromon/opus` from `c1b3b8a`. The report covers the trial from its kickoff at about 22:52 UTC on 2026-10-30 to the gate run at about 23:15 UTC. Each claim is marked **Fact**, **Inference** or **Judgement**.

## Outcome in Brief

- **Fact.** The line classified and applied A306 with 115 equations, 60 standard and 55 bespoke, A308 with 105 equations, 47 standard and 58 bespoke, and A309 with 140 equations, 58 standard and 82 bespoke. For each article `equations.py check` reported every equation consistent and `_verify.py` reported 0 errors and 0 warnings.
- **Fact.** A308 was originally grok's article. It came to this line by the operator's reply m-7d72c0efa79b, because grok could not run.
- **Fact.** luna reviewed eight A306 entries and agreed with all of them. luna proposed one title change, to Equation 54, which the line adopted because the body never names Küchemann.
- **Fact.** No line in the trial could commit, push or use `gh`. Integration is the operator's.
- **Fact.** The line's `./_check.sh` run, without `--drafts`, finished with exit 0: `_verify.py` at 0 errors and 0 warnings, library tests passing, the build ok, and a rendered audit of 551 pages with no findings. Most of the run's time went to the production build.
- **Fact.** luna reviewed all three of this line's articles. The only open dispute, A308 Eqs 40 and 41, was settled as standard by a rule shared with luna's A307 Eq 17. One argument for standard is this line's unverified recollection of the inflatable-beam literature.
- **Fact.** The A385 draft is at `_drafts/dromon_three_models_equations_sections.markdown`. `_verify.py` reports it clean.

## 1. What Worked Well

- **Fact.** The tooling did what `EQUATIONS_SECTION.md` describes. Each article went through `separate.py`, `unfold`, `tag`, `write` and `check` on the first attempt, with no tags or generated sections edited by hand.
- **Fact.** A309 Equation 17 is a display that spans two source lines. `unfold` and `tag` handled it correctly, against this line's prediction that they might not.
- **Fact.** The validator in the main checkout, `tmp/eq3/validate.py`, caught nothing in the three files on the first run. **Inference.** Writing the TOML directly as text, as the brief requires, kept TOML escaping from becoming a source of errors.
- **Fact.** Leases worked as described. `acquire_lease` returned an expiry, and the line held `a306`, `a309` and `a308` in turn and released each one.
- **Fact.** Line-to-line mail let opus and luna agree a plan in a few exchanges, before any tracked file was written.
- **Fact.** One review exchange produced a real correction, and luna independently confirmed two of this line's arithmetic findings in A306.
- **Fact.** The standing brief led the first turn after automatic compaction, so the line resumed without re-deriving its task. **Judgement.** It was the most useful single harness feature in this trial.
- **Fact.** A308 Equation 7 is byte-identical to A309 Equation 1, and the two digests match. The line gave both entries the same title. **Judgement.** Content digests make consistency across articles checkable for free.

## 2. What Got in the Way

- **Fact, reported by the operator.** grok could not run two turns in a row. On every start Grok writes empty hooks-paths and installed-plugins entries into its Dromon home, and Dromon refuses any turn while those entries exist. A removal loop that would have bypassed the guard was refused, and the pilot is deciding what happens next.
- **Fact.** The plan had to be rebuilt for two lines after it was sent. The A309 review request this line sent grok, m-015d2a7b010a, still shows as "waiting", meaning not delivered.
- **Fact.** The task brief in `.dromon/LINES.md` said two unchecked A306 claims were in `_docs/process/ARTICLE_ERRATA.md`. They were not there. Both opus and luna found the discrepancy independently. The operator then confirmed that the claims live in the main checkout's `tmp/eq2/FINDINGS.md`. **Judgement.** An inaccurate pointer in a brief costs every line the same search, so here it cost twice.
- **Fact.** The operator's approval was sent at about 23:01. `line_status` showed it as pending well before this line's mailbox delivered it, and it arrived only at the start of the next turn. **Inference.** Mail is delivered at turn boundaries, so a line that keeps working inside a long turn acts on stale instructions until the turn ends.
- **Fact.** The context reached about 223,500 tokens before automatic compaction ran, against a threshold of 150,000. **Inference.** Compaction is checked only at turn start, so one long turn can overrun the threshold by half again.
- **Fact.** The scripts named in the brief, `tmp/eq2/apply.sh`, `separate.py` and `validate.py` and `tmp/eq3/validate.py`, are gitignored. They exist only in the main checkout, so this line ran them by absolute path from its worktree. `apply.sh` changes to its own repository root, so it cannot be used as written against a worktree.
- **Fact.** When this line wrote its A307 review, two of luna's messages had not reached its mailbox. One asked for that review and one answered the A308 dispute. This line read luna's answer in luna's notes file in luna's worktree before the mail arrived. luna's sent-message tracking later showed both as delivered. **Inference.** Delivery to the mailbox happens at the recipient's turn boundary, so a long turn on the receiving side looks like lost mail from inside it.
- **Fact.** This line's explicit answer on A307 Eqs 4 and 6, m-80ec3c937468, shows "delivered" but never "read" in `list_sent`, while later mails to luna show "read". luna then disputed the A385 draft's account of this line's position, because it had not seen that message. **Inference.** The mailbox gives a recipient no prompt about a delivered message it skipped. The sender's "delivered, not read" was the only clue.
- **Fact.** The lines agreed to announce a `./_check.sh` run by mail before starting it. This line announced its second run, m-8b372974f3c3, and started it. The announcement stayed "waiting", undelivered, and luna started its own gate at about the same time without having seen it. This line stopped its run when luna's mail arrived. **Judgement.** Mail cannot give mutual exclusion when delivery waits for a turn boundary. A declared `gate` lease would. **Fact.** No such lease exists. `acquire_lease gate` returned "the project declares no lease 'gate'. Declared leases: a306, a307, a308, a309, article".
- **Fact.** luna's first planning mail and this line's crossed, carrying different splits. It cost one extra exchange.
- **Fact.** This line's A307 review answered luna's question on Eqs 4 and 6 only with a closing "I agree with every other entry", which did not answer it. The line answered explicitly in a later message. **Judgement.** That was this line's error, not the harness's.
- **Fact, reported by the operator in m-56389db9e072.** This line's A309 Equation 122 finding gave the wrong reason. It took the semi-major axis of the ballistic arc, `a_bal`, as the SCORE orbit's. With the orbit's 7205.5 km from Equation 43 the bracket gives about -7.5 kJ/kg, -7.48 by the operator's figures and -7.50 with R_e = 6371 km by this line's, so the stated 7.5 has the right size and the wrong sign, because the subtraction is reversed. On the figure this line cited, the bracket would have been positive, so its reasoning did not support its conclusion. luna confirmed the finding and did not catch the figure. **Judgement.** That was this line's error, and a second line's agreement was not verification. The operator's recomputation found it.
- **Fact.** The context reached about 162,800 tokens before the second automatic compaction, again over the 150,000 threshold.
- **Fact.** `pgrep` was denied in the sandbox ("Cannot get process list"), so the line tracked the background gate by reading its log.
- **Fact.** Reading one X-Planes post by line offset exceeded the read tool's token limit, because its literature lines run to tens of kilobytes. An `awk` extraction of the display equations worked.
- **Fact.** Two read_mail calls in the first session used message identifiers that did not exist and returned errors. Listing mail first avoided the problem afterwards.

## 3. What I Could Not See or Do

- **Fact.** The line could not commit, push or open pull requests. By design, it reports the worktree HEAD and the gate result instead.
- **Fact.** The line could not read `.dromon/`, so it could not see grok's failure for itself. Everything it knows about that failure comes from the operator's mail.
- **Fact.** `line_status` reports that on this platform the daemon cannot identify which processes belong to a line, so it neither lists nor stops them.
- **Fact.** The engine sandbox lists the shared `.git` directory as a write root. `line_status` reports `shared_git_directory_write_allowed: false` and denies specific descendants. **Inference.** The two layers describe the same boundary differently, and a line reading only one of them could misjudge what it may do. The line did not test the boundary.
- **Fact.** The line cannot see the other lines' turns, costs or holds except through mail and the operator. It learned grok was held from mail, not from any status call.
- **Fact.** A call to `line_status` with both `detail` and `lists` returned a truncated result that recommended dropping `lists`. A later call with `lists` alone was also truncated, returned no list at all, and again recommended dropping `lists`. So `lists` returned nothing in practice. At that point luna had not touched its worktree for about half an hour and had three unread messages from this line, and the line could not tell whether luna was running, idle or held. **Fact, reported later by the operator in m-9c5afc27c587.** luna was held. The `kill_all` stop policy could not read the process table, because `ps` did not answer within 10 seconds, so Dromon refused the turn and raised an operator question. The operator's mail watcher, which requested more than the 50-message limit, failed silently. That question and this line's report m-cf74ea43ac58 went unseen for roughly an hour. **Judgement.** A hold reason visible to the other lines, as luna's report also suggests, would have turned an hour of guessing into one status call.

## 4. Ranked Harness Suggestions

1. **Fix the Grok startup interaction, or report it to the other lines.** Problem: a third of the team was idle, and its share fell on the others without the harness telling them. A line whose turns are refused should be visible as held, with a reason, in the other lines' status.
2. **Deliver operator mail inside a running turn, or let a line poll for it.** Problem: the approval sat pending while this line kept working on assumptions it could not confirm.
3. **Check the compaction threshold during a turn as well as at its start.** Problem: context ran half again past the threshold before compaction, which raises cost and the risk of losing detail.
4. **Check pointers in task briefs against the repository before the trial starts.** Problem: the errata pointer was wrong, and two lines spent the same search finding that out.
5. **Make the main checkout's gitignored tooling available to worktrees, or say in the brief that it must be run by absolute path.** Problem: `apply.sh` cannot run against a worktree as written, and the scripts are absent from every worktree.
6. **Let a project declare a lease for a machine-wide action such as the deploy gate, and say so in the brief.** Problem: the agreed mail protocol for taking turns on `./_check.sh` failed the first time an announcement waited at a turn boundary, and two production builds started at once.
7. **Flag delivered but unopened messages to their recipient at turn start.** Problem: one unopened answer turned a classification question into a dispute over what a line had said.
8. **Report the same write boundary in the engine sandbox and in `line_status`.** Problem: two descriptions of one boundary invite a wrong reading.
