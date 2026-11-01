# Sol harness experience report

> **Navigation**: [Dromon Trial 2](./README.md) | [Process](../README.md)

## What worked well

- **Fact** The kickoff supplied a precise directory assignment, read-only boundaries, promotion criteria, review requirements and explicit prohibitions on commits, network requests and scratch execution.
- **Fact** Mail tools accepted messages to opus and grok. Sent message identifiers were returned. Both peers subsequently replied and agreed ownership and review assignments.
- **Fact** Sending a coordination blocker to the supplied @operator address returned no operator operator. Sending to the kickoff sender @bsechter succeeded. The operator later confirmed that this is the configured name and that @operator is not an alias.
- **Fact** Grok reported receiving the previous phase brief instead of the current promotion brief. Sol shared a copy of its received task facts as coordination data and notified the kickoff operator. The operator later confirmed that Grok retained a phase 2 session and restarted it with the current brief. Sol did not independently inspect the configuration.
- **Fact** The worktree parent matched the active handoff record at startup.
- **Fact** The brief and scheduled wake tools preserved the inventory paths and next assessment between the first and second turns.

## What got in the way

- **Fact** The initial git status reported an operating-system denial for secret/. The command continued. No secret content was read.
- **Fact** A startup read concatenated historical process records and generated roughly 648,000 output tokens before truncation. Most of the live records were near their beginnings. This was an overly broad command chosen by this line, rather than evidence of a harness failure.
- **Fact** A process-status check using ps was refused with Operation not permitted. The list_processes tool was tried next, but reported that this platform cannot identify or list owned processes because it cannot read process environments. The engine session poll remains available.
- **Fact** Independent review suites launched from the peer worktree encountered permission denials when the existing tests tried to create fixtures under that worktree's tmp directory. The suites reported 170 of 183 and 85 of 96 passing. Sol then copied the tracked test candidate into its own scratch directory. The permitted rerun passed all 183 library tests and all 96 source tests. This restriction is consistent with the supplied write boundary.
- **Fact** Excluding secret with a git pathspec still produced a directory-access warning. The suggested exclusion is therefore not an established workaround.
- **Fact** Sol reported doubled backslashes in peer documentation after misreading JSON-escaped tool output. The peer challenged the finding. A byte-level check established that all relevant runs were single backslashes. Sol withdrew the finding. This was a review error, rather than an established harness defect.
- **Fact** The script inventory initially counted copied repository tooling inside mathrepair/base. The inventory now discloses that scope explicitly. Counts are script copies rather than distinct mechanisms.

## What I could not see or do

- **Fact** The configured permissions prohibit reading .dromon and secret. The supplied brief was sufficient for the work performed so far.
- **Fact** No commit, push, GitHub command, network request, subscription process or daemon was attempted.
- **Fact** No pre-existing scratch script was executed. New sol code under tmp/promotion was executed to inventory files and apply reviewed local edits.
- **Fact** Sol received a second engine-session restart notification before implementation. Its inventory, design notes and mail remained accessible.
- **Fact** Sol was notified that its kept engine session had closed after configuration, instructions, tools or environment changed. Its on-disk brief and scratch command contract were available after restart.
- **Fact** An automatic compaction notification reported about 151,941 context tokens before compaction. The standing brief, source changes, saved verification artifacts and mailbox remained accessible afterwards.
- **Fact** No comparison with the other engines' capabilities has been independently established.
- **Fact** The baseline verifier completed with 385 posts, zero errors and zero warnings.
- **Fact** S1, S2 and R1 were implemented after explicit operator approval. The library suite passed 179 tests and the source suite passed 96. The production build passed. A comparison of all 552 HTML pages against the saved baseline found exactly eight changed pages and ten repaired Notation blocks, with no unexplained hunks. The corpus verifier remained at 385 posts with zero errors and zero warnings. Opus accepted S1 and S2 after independent real-case runs and verified the R1 corpus repair. Its adversarial generator review identified digit-preceded underscores as an unhandled case. Sol corrected the opener and closer rules and added regressions. The updated library suite passed 179 tests, five actual kramdown cases passed and all 5,804 generated Notation rows remained unchanged. The corpus verifier again reported zero errors and zero warnings across 385 posts. Opus accepted the revised R1 after passing all 5,804 corpus symbols and seven adversarial cases through the generator and actual kramdown with zero defects, and checking 254 generated sections for zero drift. Sol independently accepted Opus P1, D1 and R2 with 183 library tests, 96 source tests and an unused saved-site command. The implementation files were frozen and integrated into the Opus worktree. Sol compared the two equation files and found them byte-identical to the accepted versions. Sol inspected the integrated check log. It records 188 library tests, 96 source tests, zero corpus errors and warnings across 385 posts, a successful production build and a rendered audit with no findings across 552 pages, ending in all checks passed and exit zero. Sol independently compared all 552 integrated HTML paths against the baseline and confirmed exactly 13 changed pages, 18 repaired blocks and zero unexplained hunks. The saved evidence is tmp/promotion/render-diff-integrated-sol.json. The integrated feed-aware diff records 18 changed outputs, comprising 13 HTML pages with 18 repaired blocks and five feeds with ten mirrored repairs, with zero other changes. The build still emits Sass deprecation warnings. No commit or deployment was performed.

## Ranked harness suggestions

1. **Judgement** Validate configured operator aliases and instruction versions at kickoff. The problem is that the supplied @operator address failed and a peer reported receiving the old brief.
2. **Judgement** Supply a bounded live-record excerpt at startup. The problem is that historical process files can consume the output budget before their useful current state can be assessed. Preserve the full files as accessible evidence.
3. **Judgement** Provide a documented status command that excludes denied paths. The problem is that ordinary git status touches a denied tracked directory and emits a refusal unrelated to the active task. A pathspec exclusion did not remove the warning in this session.
4. **Judgement** Distinguish transport acceptance from recipient receipt prominently in mail results. The problem is that a returned message identifier establishes sending but does not by itself establish coordination.
