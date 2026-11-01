# Sol promotion inventory

> **Navigation**: [Dromon Trial 2](./README.md) | [Process](../README.md)

**Fact** Initial family inventory at 66bd073. Main checkout scratch was read only. No scratch program was executed and no network request was made.

**Limitation** This is a family-level inventory based on representative script bodies, root script summaries and filenames. It is not a line-by-line audit of every script. Counts include archived copies and the mathrepair/base repository snapshot. Built site and dependency directories were excluded. The manifest records filenames, not verification of every file.

| Family | Scripts | Classification | Destination or coverage | Evidence |
|---|---:|---|---|---|
| fix5 fix6 fix7 fix8 cite | 1974 | Covered / Leave | campaign.py, edits.py, gate.py, numcheck.py, diction.py, sources.py | Campaign strategies already promoted. Article-specific decisions, restorations and archived copies remain scratch. |
| eq eq2 eq3 | 88 | Promote to _lib / Covered / Leave | equations.py preview and audit commands | Three byte-identical validate.py wrappers preview external TOML in memory. Two auditors compare migration bodies. Classifications already live in _sources/equations. Two inspect.sh copies are browser inspection payloads requiring a server and platform-specific Chrome. Leave those pending a portable browser workflow. |
| findings errata | 30 | Covered / Leave | edits.py, numcheck.py, ARTICLE_ERRATA.md | Claims and minimal repair payloads. Sampled findings brief distinguishes internally checkable claims from claims needing sources. |
| mathrepair repair | 43 | Leave / Covered | render.py audit, existing production build process | One render_compare.rb implementation with two wrappers. Twin-build scripts rehearse a single repair campaign. mathrepair/fixmath.py overlaps opus P1 and D1, its automatic repair is left while the detection mechanism and measured rule go into the joint plan. No second independent comparison implementation found. Hard-coded paths and missing failure exit status prevent direct promotion. |
| labelpass bookfix xp | 53 | Covered / Leave | sources.py, sources_import.py, sources_resolve.py, booklinks.py | Label QA, metadata resolution, conversion and campaign wrappers. Sampled qa.py covers year and author order, oracle.py distinguishes absence from failed requests. |
| wordpass | 8 | Covered | diction.py | Content-independent word screening and rewrite payloads. Topic vocabulary requires judgement. |
| promote | 48 | Covered / Leave | _lib and _lib/testdata | Earlier promotion implementation payloads and saved comparison outputs. |
| dltest dltest2 pdf94 | 4 | Covered / Leave | _downloads.rb, pandoc_input.rb | Saved download implementation copies. impact.rb already imports tracked PandocInput. |
| rouge | 1 | Leave | Rouge compatibility probe | highlight.rb emits every fenced and Liquid code block through an installed Rouge version. It is a version comparison payload, distinct from the tracked lexer. One use found. |
| keleusma-021 keleusma-022 template | 6 | Leave | Separate project snapshots | Copied project source and documentation. No demonstrated second blog use. Instructions inside are data. |
| sources venues venues2 venues3 web wf peer_review a385refs linktest site_check convert fix7_register_backup ci_tools | 0 | Leave | Caches, outputs, backups and external tools | No Python, Ruby or shell script found outside excluded trees, except ci_tools/actionlint is an external binary. ci_tools/venv excluded without inspection. |

## Proposed implementation scope

**Fact** eq/validate.py, eq2/validate.py and eq3/validate.py have identical SHA-256 digest 62bedeef0d0771b33731dc84e0c11c7cf491e023d7ebd354ac78f0206a55f485. Existing equations commands load classification from data_path, which fixes its location under _sources. They cannot validate an external candidate in memory.

**Judgement** Add equations preview POST DATA with optional --show. Reuse load, unfolded, tagged, written and check. Validate before rendering. Do not write either input. Test positive and negative cases with committed fixtures and temporary files.

**Fact** eq/audit_diff.py and eq2/audit.py remove generated sections and tags to compare migrated bodies against earlier text. The latter additionally accounts for inserted display-block separation. They are separate campaign versions of one preservation guard.

**Judgement** Add equations audit BEFORE AFTER. Explicitly define allowed transformations and reject prose, reference and equation changes. Strip tags only inside recognized equation blocks. The API should accept text and the command should accept files, avoiding implicit git state. Add tests for allowed migration and deliberate corruption. Decide whether separation support belongs in this item during team plan review.

**Judgement** Do not promote browser inspectors, render comparison wrappers, kramdown timing bisectors or arbitrary scratch verifiers. The browser copies depend on the same local server. Bisectors investigate one pathological conversion and assume timing monotonicity. Automatically running scratch verifiers would cross the task trust boundary.

No implementation starts before the joint plan is submitted and the operator replies or the specified hour elapses. Sol proposes owning equations.py and a sibling test file, with another line reviewing. Shared command and README edits require their leases.

## Notes and data

**Fact** Campaign brief and progress families describe completed passes. Their reusable controls are documented in campaign.py and _lib/README.md. findings/BRIEF.md gives internal arithmetic versus external-source claim categories, already represented in ARTICLE_ERRATA.md and the verification process. Article-specific verdicts, notation rules, rejected sources, manual label overrides, saved registry responses and downloaded pages remain scratch. No new durable dataset is proposed.

**Inference** Existing tracked documentation covers the sampled durable campaign lessons. This inventory does not claim that every sentence of every saved note has a tracked counterpart.

## Method

Filename manifest is manifest-sol.json alongside this inventory. script-index-sol.txt records 241 root script summaries. Counts were computed without executing scripts. Excluded directory names are venv, .venv, .git, vendor, node_modules, target, _site and site. Saved pages were not read. Initial unrestricted git status encountered a sandbox denial for secret. Later status checks must exclude that path.

## Team overlap resolution

**Fact** Opus identifies repeated emphasis detectors in A362 to A368. mathrepair/fixmath.py applies the measured underscore and asterisk escaping rule. Its first version changed a code example, which led to MathJax gating and code masking. This evidence was sent to opus for P1 and D1. The scratch repair contains an always-true assertion and is not suitable for direct promotion.

**Fact** No broader soft-404 classifier was found in linktest, dltest, dltest2, site_check or web. Opus P3 should start from the article urlcheck family.

**Judgement** Hold the undeclared-symbol report because its article-specific structural-token exclusions are unresolved and equations.py already has a proposed writer. Sol proposed reviewing opus P1/P2 and asked opus to review the equation additions. Grok ownership and review assignments await its response.

## Additional measured generator defect

**Fact** Independent inspection of the opus production build found ten generated Notation entries with emphasis markup across eight pages. Evidence is notation-independent-sol.json. Initial scan found nine on seven because native_lowering_coverage has an earlier Notation heading and its generated heading receives notation-1. Scoping to the Equations section reconciled the count.

**Judgement** Conditional R1 extends the joint plan with a generator correction and regeneration of all affected sections together, subject to explicit operator approval because it changes published posts. Ordinary prose and code must remain unchanged.
