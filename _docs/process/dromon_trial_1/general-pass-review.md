# Review of A385 by the session that ran the general pass

Written by the Claude Code session that ran the A290 to A368 Equations section migration, which is still read-only.
The pilot passed it to the operator on 2026-10-31. It reviews A385 at `df89189`. Its own body follows verbatim.

A385 is still a draft. It is _drafts/dromon_three_models_equations_sections.markdown, titled Access, Legible State and Recomputation in a Three-Model Harness. It has an editorial date of 2026-08-21 and runs to about 8,750 words. TASKLOG records it as through all four passes and not published. The restructure is committed in df89189 and has not been moved to _posts/.

My opinion

The draft is careful and honest, and the core argument is worth publishing. It needs one real fix and some trimming before it goes out.

Strengths

- It keeps facts, inferences and judgements apart, and states how its thesis could fail. It then grades its own verdict down to "partially supported." Few articles about agent trials hold themselves to that.
- The recomputation section is the best part. Two cases carry it:
  - The X-12 Equation 122 finding was right for the wrong reason, and a second line confirmed it without checking.
  - A correct observation was removed because a citation was trusted over a repeated query, and it survived only by accident.

  Both show concretely why agreement is not a check. The tie to the N-version programming literature (Knight and Leveson, Eckhardt and Lee) suits that point.
- It does not overclaim the trial as a test of what caused the original refusal. It says plainly that the trial is not a clean replication, and explains why.

Problems, most important first

1. Many references are in the wrong category. Under "Primary Sources, Non-Peer-Reviewed" it lists papers from peer-reviewed venues:
   - Journal of the ACM: Chandra and Toueg, and Fischer, Lynch and Paterson.
   - Communications of the ACM: Lamport, Lampson, and Ricart and Agrawala.
   - IBM Systems Journal: Fagan.
   - Human Factors: Parasuraman and Manzey.
   - Conference proceedings: NeurIPS (Cemri), NAACL (Röttger) and SOSP (Gray and Cheriton).

   Only the arXiv preprints (Du, Hong and Wu) and the repository page belong there. Hardy's Operating Systems Review note is arguable. My guess is that the peer-review flag was never set when the 21 records were imported. The fix belongs in _sources/, followed by regenerating the section. This error is visible to readers, and the verifier did not catch it.
2. It reads partly as an incident log. Table 4, with pull request numbers, commit hashes and merge times to the minute, and the long account of the operator's mail watcher paging bug, are useful to the people maintaining the harness. They add little to the thesis. The watcher was also the operator's own tool, not part of Dromon. Cutting Table 4 to one paragraph and the watcher account to two or three sentences would remove perhaps 1,000 words and sharpen Finding Two.
3. The equations look added to satisfy the format rather than the argument. Equation 2, the lease invariant, is classed bespoke, yet it is the textbook mutual-exclusion property and cites Gray and Cheriton. I would class it standard. Equation 4 cites Eckhardt and Lee for the joint probability of two correlated misses. I am not confident that paper states the formula in that form, so the citation may claim more than the source supports. That is my inference and I have not checked the paper. Equations 3 and 4 do support the argument about correlated misses. Equations 1 and 2 restate the prose and could be dropped.
4. The date and the events disagree. The post is dated 21 August 2026 but describes events on 30 and 31 October 2026, and its references show an access date of 31 October. That follows the blog's convention of filling date gaps, A384 being 20 August, but a reader will see an article describing events that happen after its own date. If that bothers you, a single sentence noting when the trial took place would settle it.
5. The article names an exception to the "never report the drafting process" rule. That is by your instruction, so it is not a defect. It does make A385 the precedent other articles may cite, so it may be worth recording the exception in the style guide rather than only in the article.

Checks I ran

- No mention of Lightforce or Lightstrike: 0 matches.
- TASKLOG records _verify.py at 0 errors and 0 warnings. I did not run ./_check.sh or a production build myself.
- I did not verify any of the cited sources against their contents.

Recommendation

Fix the reference categories first, then trim Table 4 and the watcher account, then reconsider Equations 1 and 2. After that it is ready to publish.
