# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-05
**Task**: Infrastructure audit, download-pipeline repair, and the follow-up rectifications. All
complete, deployed, and verified live. One editorial item remains for you.

---

## Resolved

**PDF downloads, the significant one.** Every post links a `.pdf` that has never existed. Cause was
a missing `lmodern` package, which pandoc's default LaTeX template loads. Added it. Separately,
`_downloads.rb` now **exits nonzero on systemic failure**, meaning a format produced zero outputs
across all posts. That is the reason this shipped undetected: the script only warned, so CI stayed
green through roughly 293 dead links. Individual failures still only warn, so one bad post cannot
block a deploy.

**EPUB paths.** `_downloads.rb` reconstructed each permalink from the source **filename** date;
Jekyll derives it from the front matter date. Nineteen posts diverge, so their EPUB landed where no
HTML exists. It now **discovers the emitted HTML by globbing the built site**, which removes date
arithmetic from the problem entirely. Verified: 293 of 294 posts resolve to exactly one HTML file,
the exception being the forward-dated article legitimately absent from the build.

**A latent trap I did not expect to find.** `_config.yml` set no `timezone:`, so permalinks
depended on the build machine. The `2026-03-06 01:14 +0000` post builds as `/03/06/` on the UTC
runner and `/03/05/` in Pacific time. **A local URL check was not evidence about production.**
Pinned `timezone: UTC`, which the runner already uses, so no live URL changes. Verified by
comparing a local build against the live sitemap: **291 local pages, 291 live, zero differences.**

**Reference integrity, now clean corpus-wide.** Added the missing `[rust_book]` definition to the
2025-12-17 Solana post, which had been rendering literally as `[The Rust Programming
Language][rust_book]` on the live site. The four orphan definitions in 2016 posts were initially
removed and, per your instruction, subsequently restored and cited instead. Zero undefined, zero
unused.

**Dependency.** `json` 2.19.7 to 2.21.2, clearing the Dependabot advisory. The lockfile diff is
that one line.

**Documentation.** Recorded that the scratch build strips `jekyll-archives` and skips
`_downloads.rb`, so category, tag, and download links appear broken in it. A crawl reported 740
broken targets on that basis alone, all fine in production. I nearly reported those to you as real.

---

## Everything Below Was Subsequently Rectified

The four items that had needed your judgment are done, per your instruction. The orphan links were
restored and cited rather than deleted, the 171 unsorted definition blocks were sorted block-wise
so categorised sub-blocks survive, and the four filename dates were corrected to match their front
matter. `tmp/` was left alone as intentionally gitignored.

**One editorial item remains, and only you can decide it.** A224 was backdated to 2026-02-17 to
fill what that day's log called the gap between A85 at 02-16 and A86 at 02-18. That reasoning
trusted A86's misleading filename. A86's real date is 02-17, so the gap never existed and
2026-02-17 now visibly carries two articles. The genuine remaining gap in that window is
**2026-03-07**. Moving A224 would change a published URL.

## Original Judgment Items, For The Record

**1. A post is six days from where its filename says.**
`_posts/2026-03-12-error_correction_recursion_problem.markdown` carries `date: 2026-03-06`. Jekyll
uses the front matter, so it is live at **2026-03-06**, not 03-12. Given how deliberately you place
articles into calendar gaps, this looks like a real editorial slip rather than a rounding artifact.
Three others differ by one day and are probably harmless: `single-file-elixir-programs` (2016),
`mission_command_management_style`, and `telemeritocracy`. **I changed none of them**, because
which date is correct is a content decision, and changing the front matter would change a live URL.

**2. 171 of 294 posts have unsorted link-definition blocks.**
The style guide requires alphabetical sorting by anchor and the verification script checks it, so
they technically fail. Sorting them means touching 171 files for **zero rendering change**. I did
not do it. Worth it only if you want the check to run clean.

**3. I deleted four unused link definitions.**
`elixir-syslog`, `unix-case-insensitive`, `ion-dtn-users`, `postgresql-install`, all in 2016 posts.
They were invisible in the rendered output. An unused definition can mean the author meant to cite
something and never linked it, so if you would rather have kept them as leads, revert that part.

**4. The `json` bump is untested locally.**
The local bundle is broken by the gem-environment issue, so `bundle lock` resolved cleanly but I
could not run a build against it. **CI is the first real test.** Watch the next deploy.

---

## What I Audited and Found Healthy

All top-level pages, feeds, sitemap, robots, favicon, manifest, and the Pagefind index return 200.
Zero broken internal links, zero missing asset references. No duplicate article numbers, no front
matter defects, complete debug-tag coverage across 294 posts. MathJax flags correct, with all six
apparent unrendered-math cases proving to be shell variables, Makefile syntax, or a currency
figure. Category and tag archives live, including `/categories/keleusma/`, which does not hit the
shadowed-path trap. `draft_summary.md` in sync with all eight drafts. Next article number A295
matches the highest present. No build artifacts tracked. The four unresolved draft `post_url` tags
are the documented, expected interlock condition.

Housekeeping, not a defect: `tmp/` holds roughly fifty scratch files from earlier sessions. It is
gitignored. I left it alone rather than delete work you may still want.

---

## State

Branch `master`, tree clean, everything pushed and deployed.

**The download pipeline is fully repaired and verified live**: `pdf=293 epub=293 skipped=1
failed=0`, from an initial 293 PDF failures and 19 misplaced EPUBs. A 28-post sample spanning 2016
to 2026 returns 200 for both formats. Six deploys were needed because LaTeX aborts at the FIRST
error in a document, so each fix exposed the next defect. Do not read a flat failure count as a
stalled fix; check whether the ERROR TEXT changed.

Six of the ten root causes were latent defects in the CORPUS, not tooling: `align` nested in
display delimiters, two double subscripts, two under-declared array column specs, MathJax-only
macros, and an opening `$` followed by a space. All are invalid LaTeX that MathJax renders
leniently and that the delimiter-balance check cannot see. The PDF pipeline is the only process
here that parses the mathematics strictly, so treat it as a math linter and keep it green.

Corpus-wide: zero undefined anchors, zero unused definitions, zero unsorted definition blocks, zero
filename-versus-front-matter date mismatches, zero broken internal links, zero missing assets.
