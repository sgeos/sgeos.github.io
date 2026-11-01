# Grok harness experience report

> **Navigation**: [Dromon Trial 2](./README.md) | [Process](../README.md)

Opus integrated the three worktrees and ran the one `./_check.sh`. This line read that log. It did not run a second gate. The four P3 files stayed frozen.

## What worked well

- **Fact.** After the operator rebound this line, the rules in the turn contained the current tmp-promotion brief, under The goal and The shares. `set_brief` then survived later engine sessions: each new session opened with the brief this line had last written, including the commit stamp `66bd073`.
- **Fact.** Mail to opus, sol and `@bsechter` returned message ids, and the replies arrived in later turns. The operator approval `m-508caa19acef` named the conditions this line needed: P3 and D2 as written, no `TASKLOG.md` edit, the exclusion list, and the compiler-series note left unapplied.
- **Fact.** The leases worked for the files this line edited. `test_lib` and `lib_readme` were acquired, the edits were made, and both were released. Opus later asked for `lib_readme` and was told it was already free.
- **Fact.** Reading the other worktrees was enough to review P2 without copying it. `python3.13 _lib/blog.py handoff` in the opus worktree, plus the three staged `t_handoff_*` tests, plus `--file=` on `handoff_head_old.md`, `handoff_head_new.md` and `handoff_old.md`, was a real review. Those three snapshots were not the implementer's cases.
- **Fact.** Opus's first P3 review found a real defect with evidence this line did not have. `identifiers` kept only DOI definitions, and the soft-404 pages are hand-written addresses. The fix is in the same four files. The re-review, `m-313768054233`, accepted it after 182 library tests, 96 source tests, and an offline command run on saved pages this line's tests do not use.
- **Fact.** `python3.13 _lib/test_lib.py` and `python3.13 _lib/test_sources.py` run in this worktree. After the fix they reported 182/182 and 96/96.

## What got in the way

- **Fact.** The sessions before the rebound did not have the current brief. The standing brief at the start of this trial said the injected rules were still the phase 2 brief, `.dromon` was not readable, and this line had not inventoried. The operator's mail said the engine kept the rules the session was created with, so the new brief never arrived until a rebound started a fresh session. This line did not invent an inventory in that gap.
- **Fact.** A previous engine session on this line was held because it called `todo_write`. The operator's resume said Dromon does not give this line that tool. This session's tool list still includes `todo_write`, `spawn_subagent`, `web_fetch` and other tools the brief forbids. Calling one ends the turn and holds the line. This session did not call them.
- **Fact.** `python3` in this worktree is 3.9.6. `python3 _lib/test_lib.py` fails at `import tomllib` inside `equations.py`. The suite passes under `python3.13`, which is at `/opt/local/bin/python3.13`. The brief does not name an interpreter.
- **Fact.** `git status` and `git diff` in this worktree print `secret/.gitkeep: Operation not permitted` and `could not open directory 'secret/'`. The command still exits 0. No file under `secret/` was read.
- **Fact.** Opus's note to start P3, `m-0cfc6ea57de8`, arrived after P3 was already implemented and after the review request had been sent. It was late, not lost. The later re-review was the one that carried new information.
- **Fact.** Nothing in the harness listed files that were dirty in more than one worktree. A `git diff --stat` across the three worktrees showed `_lib/README.md` and `_lib/test_lib.py` dirty in all three, and `_posts/2025-11-09-x_planes_orbital_sciences_x34.markdown` and `_posts/2025-12-09-x_planes_invocon_x64.markdown` dirty in both sol and opus, on different lines. Both hunks in each post have to land. Copying either file whole would drop the other escape.
- **Judgement.** Peer status mail spends the autonomous-turn budget. This line's useful waits were for the operator and for opus's review. Turns that only recorded agreement still incremented the counter, which holds the line at 40.

## What I could not see or do

- **Fact.** The brief says `.dromon` is closed to every line. This line did not read it. The brief text that arrived after the rebound was sufficient for the inventory and for P3.
- **Fact.** This line did not commit, push, or run `gh`. The worktree HEAD stayed `66bd073ceef18a124a97ca191a7b11f268ba7395` while the four P3 files were dirty. Reviewers had to lay those files over a clean archive.
- **Fact.** This line did not run `resolve.py --body` against the network, and did not run any script from the main `tmp/`. The only command-level evidence for `--body` on real pages is opus's offline stub, which they described in the acceptance mail.
- **Fact.** This line did not run `_verify.py` or `_check.sh`. Opus is the agreed runner. The corpus result of the merged tree is not visible here yet.
- **Fact.** Lease state was visible only by acquiring a lease, releasing it, or being told. This line did not have a listing of holders.
- **Fact.** A wake was scheduled as `m-3e5ca8ce3840` for 2026-11-01T00:59:54Z, to start P3 if the operator had not written. The operator wrote first, at about 00:00Z, and P3 was implemented, reviewed and integrated before that wake. At 00:52Z `read_mail` of that id said the message was not in the mailbox. It was delivered at 00:59:55Z. The note still said to implement P3. It was not acted on, because the operator had already approved the work and the four files were frozen.
- **Fact.** Every turn reported an "unanswered" count of about 19, while the unread list was the one new message. This line could not tell which historical messages that count referred to, and did not answer phase-2 mail.
- **Fact.** This line has no independent comparison of what the opus and sol engines can do. Their reviews ran tests and offline commands. Their mail did not describe a tool this line was denied and they were granted, apart from the session-resume failure that was specific to this line's kept engine session.

## The gate

- **Fact.** `tmp/worktrees/opus/tmp/promotion/integ/logs/check.txt` records the integrated run. It checked 385 posts with 0 errors and 0 warnings, then `test_lib` 188/188 and `test_sources` 96/96, then a production build it calls ok, then a rendered audit of 552 pages with no findings. The file ends `all checks passed` and `check exit 0`.
- **Fact.** `tmp/worktrees/opus/tmp/promotion/integ/logs/sitediff_integ.txt` ends `18 changed pages, 28 defect blocks fixed, 0 other changes`. Every listed hunk is marked `DEFECT FIX`. The per-file lines add to 18 blocks on 13 article pages and 10 blocks on 5 feeds (`feed.json` 4, `feed.xml` 3, and one each on three category feeds). The feeds repeat article text. The 18 article blocks are the 18 baseline defects. Opus confirmed that reading in `m-972c786a45d5`.
- **Fact.** This line did not run `./_check.sh`.

## Ranked harness suggestions

1. **Judgement.** On resume, install the current brief, or rebind when the line's rules have changed. The problem is that a kept Grok session kept the phase 2 system prompt, `.dromon` was unreadable, and the line could not see the task until an operator rebound it.
2. **Judgement.** Do not offer a tool the line is forbidden to call. The problem is that `todo_write` is in the engine tool list, the brief says calling it holds the line, and the line learns that by being held.
3. **Judgement.** Name the interpreter that can run `_lib/test_lib.py`, or make `python3` that interpreter. The problem is that `python3` is 3.9 and the suite imports `tomllib`, so a green run depends on a path the brief never gives.
4. **Judgement.** Show the integrator which paths are dirty in more than one worktree, and a per-line diff that does not require reconstructing three dirty trees. The problem is that nobody may commit, reviewers overlay files by hand, and a whole-file copy of the two shared posts would drop one of the two escapes.
5. **Judgement.** Add a lease listing, and stop presenting the historical unanswered count as if it were the unread mailbox. The problem is that a line cannot see a holder without taking the lease, and a standing "19 unanswered" does not say which messages are still its job.
6. **Judgement.** Do not charge the autonomous-turn budget for a turn whose only new mail is peer status while the brief says to wait. The problem is that a line waiting on review can be held for answering status notes.
7. **Judgement.** Keep `git status` off `secret/`, or make that denial silent. The problem is that every status in this worktree prints `Operation not permitted` for a directory the task does not use, and the command still exits 0.
