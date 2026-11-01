# Joint Promotion Plan

> **Navigation**: [Dromon Trial 2](./README.md) | [Process](../README.md)

The plan the three lines agreed and sent to the operator as `m-207f70d9ca1e`, verbatim, followed by the approval `m-f993b843cd08`.

```text
Joint promotion plan, agreed by opus, sol and grok. The inventories are tmp/worktrees/opus/tmp/promotion/inventory-opus.md, tmp/worktrees/sol/tmp/promotion/inventory-sol.md and tmp/worktrees/grok/tmp/promotion/inventory-grok.md. The merged plan is tmp/worktrees/opus/tmp/promotion/plan-draft.md. Most of tmp/ is Covered or Leave. Grok's share yields no promotion of its own, because the A1 to A296 conversion is finished and already in the library.

LIVE DEFECT FOUND. A production build of 66bd073 shows emphasis tags inside inline maths in 18 blocks on 13 published pages. Kramdown pairs an underscore or asterisk across two $...$ spans. On the X-43 page, for example, the source line renders as "$\dot{m}<em>{0}$, the captured air mass flow, with $\dot{m}</em>{e}$". Sol confirmed the count independently.
- 10 of the blocks, on 8 pages, are generated Notation entries. The tracked equations.py render emits them, and equations.py check passes them. The pages are X-24, X-34, X-35, X-43, X-64, X-66, distressed acquisitions and native lowering coverage.
- 8 blocks, on 7 pages, are body prose. The pages are framing, X-21, X-34, X-37, X-49, X-64 and mass drivers.
- That the reader sees broken maths there is an inference from MathJax 3 delimiter matching. I have not checked it in a browser.

ITEMS, given as implementer then reviewer.
P1, opus then sol. render.py gains a math-emphasis check, with tests from the a362 kramdown probe cases. It reports only until R1 and R2 land, then gates. Evidence is three detectors, emrisk with 7 copies, astrisk with 6 and mathrot with 7, plus sol's mathrepair/fixmath.py. A source-side lint predictor was dropped, because it flags 104 pairs against 18 real defects.
D1, opus then sol. MATHJAX_CONVENTIONS.md records the measured kramdown underscore and asterisk rule and the escape. It also records the code and front matter boundaries any repair must respect, learned when fixmath.py once altered a shell command.
P2, opus then grok. New _lib/handoff.py with a blog.py handoff command, which checks HANDOFF.md's recorded parent commit against HEAD or HEAD~1. Evidence is 7 copies of handoff_check.py. Grok reviews against the spent handoff snapshots in its share.
P3 and D2, grok then opus. resolve.py gains a classifier for a page served with status 200 whose body says not found. URL_VERIFICATION.md records the case. Evidence is 6 copies of urlcheck.py, and the lesson is today recorded only in one drafting note.
S1, sol then opus. equations preview POST DATA [--show] validates a candidate classification in memory. Evidence is three byte-identical validate.py files.
S2, sol then opus. equations audit BEFORE AFTER guards a migration so that only layout and tags may change. Evidence is 2 auditors. Its future use is the first generated Equations section on a new article. It can be dropped if you judge that speculative.
P4, an undeclared-symbol report, is held for noise.

NEEDS YOUR EXPLICIT APPROVAL, because these change published posts.
R1, sol then opus. equations.py render escapes underscores and asterisks inside the inline maths of Notation entries only. The 8 affected Equations sections are regenerated in the same change, so that equations check never sees a mismatch.
R2, opus then sol. Hand-escape the 8 body-prose blocks on 7 pages.
For both, a build diff before and after must show rendered changes only in the defect blocks. No URL, category or date changes. Should either carry an erratum or TASKLOG row?

GATES. No item changes what _verify.py reports. Sol's baseline is 385 posts, 0 errors and 0 warnings. Leases: test_lib, lib_readme, blog_py and docs, as each file needs. One writer per file, and sol is the only writer of equations.py.

Grok asks that tmp/dromon_trial4, site_after, wt_before_site, .claude and __pycache__ stay outside the promotion set, since no share names them.

We start implementing P1, D1, P2, P3, D2, S1 and S2 on your reply, or after an hour with none. R1 and R2 wait for your explicit yes in either case.
```

## Approval

```text
Operator approval of the joint promotion plan m-207f70d9ca1e. All of it is approved, with these conditions.
1. P1, D1, P2, P3 with D2, S1 and S2 are approved as written. S2 stays, kept small, and its documentation must say it is a layout guard and not proof of equivalence.
2. R1 and R2 are approved explicitly, yes. Conditions. (a) Build the site before and after, and diff the rendered pages. Every changed hunk must be one of the 18 defect blocks, and you report the diff summary with page and block counts. (b) No URL, category, date or prose change, only the escapes. (c) P1 gates in render.py only in the same change set as R1 and R2, and _check.sh must pass with it gating. (d) P1 must not fire on the 37 single-dollar blocks such as $18.5 Bn. Include one as a negative test.
3. No erratum, because no claim changes. The operator writes the TASKLOG row and REVERSE_PROMPT at integration, so do not edit TASKLOG.md. The docs lease then covers the section README files only.
4. Grok is right. tmp/dromon_trial4, site_after, wt_before_site, .claude and __pycache__ stay outside the set.
5. Leave compiler_series_scrubbing_and_errata.md unapplied, as Grok judged.
6. Every reviewer runs the tests and the command itself on a case the implementer did not use, and reports what it ran.
When all items are reviewed, one line runs ./_check.sh in its worktree, after merging the others work there or after I say which worktree, and each line writes its experience report. Report finished items to @bsechter.
```
