# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-07-14
**Task**: Draft, review, and publish A224 "Deficiencies of the HTML Hypermedia Model" as a standalone one-off comparative article treating HTML as one hypermedia model among several historical alternatives and cataloguing the properties HTML omits or degrades relative to systems that had established the requirements by the late 1980s. Editorial date 2026-02-17 09:00 UTC, filling the one-day gap between A85 (2026-02-16) and A86 (2026-02-18). Two-commit publication sequence complete; commits pushed to origin/master.

---

## Verification

### Article Body Complete

Standalone one-off comparative article. No series metadata. Treats HTML at the class level as one hypermedia model among six historical alternatives and catalogues where HTML omits or degrades each of the eight properties the historical research programme had established as load-bearing.

- Opening. Names HTML as the model that shipped rather than the richest or most complete, and previews the argument that HTML implements a strict subset of the properties historical hypermedia systems had already addressed.
- Six-system framing. Bush's Memex (conceptual ancestor), Engelbart's NLS (first working implementation), Nelson's Xanadu (transclusion and deep permanent addressing), Apple's HyperCard, Sakamura's BTRON hypermedia model as the Business TRON subsystem of the TRON project (The Real-time Operating system Nucleus), Apple's OpenDoc (native composition).
- What Every Hypermedia Model Must Address. Eight-axis property inventory drawn from the Dexter Hypertext Reference Model: link directionality, link typing, sub-document addressability, transclusion, permanence, versioning, native composition, machine-readable structure.
- Bidirectional Links. HTML one-way vs NLS/Xanadu/BTRON symmetric. Reverse-index staleness bound $N_{\text{stale}} \leq \lambda T$ formalizes why external crawls cannot fully recover the bidirectional property. NLS claim anchored in Engelbart and English 1968 AFIPS FJCC primary implementation report.
- Typed Links. HTML `rel` vocabulary small and inconsistent; RDF and JSON-LD as bolt-on retrofits.
- Sub-Document Addressability. HTML fragment identifiers require authorial decoration; Xanadu tumblers address any span; W3C Web Annotation Model as thin-adoption retrofit.
- Transclusion. HTML has no native transclusion; Xanadu had it as primary composition mechanism.
- Native Document Composition. BTRON typed-part composition, OpenDoc same on Macintosh, OLE surviving instance, PDF opaque-attachment; HTML delegates to templating.
- Permanence and Versioning. URL model resolves whatever server serves; Internet Archive as third-party retrofit; broken-link decay $f_{\text{broken}}(t) = 1 - 2^{-t / T_{1/2}}$ anchored in Klein et al. 2014 PLoS ONE reference-rot measurement; Xanadu permanent addressing at deployment cost; IPFS content-addressable approximation.
- Machine-Readable Structure. HTML mixed structural/presentational/behavioral; NLS trees, Xanadu segments, BTRON typed parts; Semantic Web anchored in Berners-Lee Hendler Lassila 2001 Scientific American as canonical program statement.
- Why HTML Displaced Alternatives. Radical simplicity, HTTP-only deployment, permissiveness enabling growth without central coordination, delegation of typing/versioning/composition to community convention.
- Partial Recoveries. Wiki backlinks, WebMentions and Pingback, static-site generator conventions, JSON-LD for commercial vocabularies, content-addressable storage, Web Components. Each reconstructs a subset of a historical property on top of an inadequate substrate.
- Prior Art in the Comparative Literature. Halasz NoteCards, Meyrowitz Missing Link, Nelson Xanalogical Structure, Nyce and Kahn Memex to Hypertext.
- Conclusion. HTML as minimum-viable subset of a mature research programme. The corrective lets contemporary designers borrow from the historical vocabulary rather than reinvent it under new names.

### Cross-References

Three cross-references to prior corpus posts embedded contextually and formally listed as Related Post entries in the References section.

- A75 Bidirectional Agentic Workflow (in Bidirectional Links, small-scale reconstruction paragraph)
- A76 Markdown as a Specification Language for Agentic Workflows (in Typed Links, corpus-convention paragraph)
- A77 LLM Knowledge Graphs (in Prior Art, contemporary-engineering-problem paragraph)

All three targets predate the 2026-02-17 editorial date and resolve via `post_url` liquid tags.

### Primary References

Nine peer-reviewed primary sources anchor the article's foundational, historical, and empirical claims.

- Berners-Lee, Hendler, Lassila (2001) Scientific American 284, Semantic Web programme canonical statement. DOI resolver returns 200 via Scientific American.
- Bush (1945) Atlantic Monthly 176, Memex conceptual origin. Atlantic direct URL 200.
- Engelbart and English (1968) AFIPS Fall Joint Computer Conference 33, primary NLS implementation report accompanying the Mother of All Demos. ACM DOI redirect returns 403 anti-bot with confirmation via corpus URL-verification pattern for ACM.
- Halasz (1988) Communications of the ACM 31, NoteCards seven-issue catalogue. ACM DOI redirect.
- Halasz and Schwartz (1994) Communications of the ACM 37, Dexter Hypertext Reference Model. ACM DOI redirect.
- Klein, Van de Sompel, Sanderson, Shankar, Balakireva, Zhou, Tobin (2014) PLoS ONE 9, large-scale reference-rot measurement anchoring the broken-link decay equation. DOI resolver returns 200 via PLoS.
- Meyrowitz (1989) Hypertext 89 Proceedings, Missing Link keynote. ACM DOI redirect.
- Nelson (1965) ACM 20th National Conference, original hypertext File Structure paper. ACM DOI redirect.
- Nelson (1999) ACM Computing Surveys 31, Xanalogical Structure restatement against emerging web. ACM DOI redirect.

### Style Verification

Zero em-dashes, en-dashes, contractions, prose semicolons, prose colons in prose, prose parentheticals outside math notation, or certification vocabulary. Debug tags `<!-- A224 -->` and `console.log("A224")` present at lines 10-11. Categories `hypermedia web history`. TRON expanded on first use as The Real-time Operating system Nucleus and BTRON identified as the Business TRON subsystem per corpus acronym-expansion rule.

### Equation Density

Two display equations. Reverse-index staleness bound $N_{\text{stale}} \leq \lambda T$ in the Bidirectional Links section formalizes why external crawls cannot fully recover the bidirectional property of one-way hypermedia. Broken-link decay $f_{\text{broken}}(t) = 1 - 2^{-t / T_{1/2}}$ in the Permanence and Versioning section quantifies the permanence deficiency against multi-year link half-lives measured in the reference-rot literature. Inline math includes $\lambda$, $T$, $N_{\text{stale}}$, $t$, $T_{1/2}$, $f_{\text{broken}}$.

### Reference Density

Twenty-two References-section entries.

- Four `book_` prefix entries: Berners-Lee Weaving the Web, Nelson Computer Lib/Dream Machines, Nelson Literary Machines, Nyce and Kahn Memex to Hypertext.
- Six `ref_` prefix entries: Berners-Lee CERN 1989 proposal, Engelbart 1962 conceptual framework, Sakamura TRON project, W3C Web Annotation Data Model, W3C RDF 1.1 Concepts and Abstract Syntax, WHATWG HTML Living Standard.
- Three `related_post_` prefix entries: A75, A76, A77.
- Nine `research_` prefix entries: Berners-Lee Hendler Lassila 2001, Bush 1945, Engelbart and English 1968, Halasz 1988, Halasz and Schwartz 1994, Klein et al. 2014, Meyrowitz 1989, Nelson 1965, Nelson 1999.

Ordered alphabetically by anchor within each category. Reference-section list order matches the anchor-definition block ordering.

### Collision and Flush Verification

Article number A224 verified unique across `_posts/` and `_drafts/`. Editorial date 2026-02-17 verified empty in both. Adjacent published dates 2026-02-16 (A85 AI Apocalypse Will Be Polite) and 2026-02-18 (A86 Mission Command Management Style) populate the one-day gap boundaries. Article fills the gap without offset or overlap.

Category shadow check: `hypermedia` at first position is specific enough that no shadowing sgeos repository is expected. The article's URL will be `/hypermedia/web/history/2026/02/17/html_hypermedia_deficiencies.html` with no path prefix collision.

### Two-Commit Publication Pattern

Standard two-commit publication.

- Draft commit sequence: 12cd0ec initial draft, b2fd04a two equations added, 45b375c three primary references added, db62c40 publication review with TRON/BTRON expansion and reference block alphabetization.
- Publish commit follows with `git mv` from `_drafts/html_hypermedia_deficiencies.markdown` to `_posts/2026-02-17-html_hypermedia_deficiencies.markdown` plus TASKLOG, draft summary, and REVERSE_PROMPT synchronization.

Commits pushed to origin/master per human pilot instruction.

---

## Article Number State

- Next available article number: A225.
- A224 published as `_posts/2026-02-17-html_hypermedia_deficiencies.markdown` at editorial date 2026-02-17 09:00 UTC.

---

## Action Items for the Human Pilot

- Verify the GitHub Actions deploy completes without errors after the push. The A224 article uses `{% post_url %}` cross-references to A75, A76, and A77, all deployed. The new PDF and EPUB download pipeline from commit db3bc37 will also exercise pandoc and xelatex against the full corpus for the first time; expect the initial run to reveal any posts with math or CJK content that require pandoc-flag adjustments.
- Review the published article at its permalink once the deploy completes at `https://sgeos.github.io/hypermedia/web/history/2026/02/17/html_hypermedia_deficiencies.html`.
- Consider whether the class-level HTML-model critique warrants a follow-up article on a specific historical system in more depth. The later corpus articles at 2026-05-23 (BTRON hypermedia and real-time desktop) and 2026-05-24 (Keleusma as substrate) already provide two such deep dives; A224 supplies the general critique those articles refine.

---

## Notes

- Next available article number: A225.
- 0 release candidates.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification in `_drafts/`.
- Published through A224 across the combined article number space.
- Corpus size 224 posts, editorial dates span 2016 through 2026-07-11.
- Primary-source verification pass performed against Berners-Lee/Hendler/Lassila 2001 Scientific American, Bush 1945 Atlantic Monthly, Engelbart and English 1968 AFIPS FJCC, Halasz 1988 CACM, Halasz and Schwartz 1994 CACM, Klein et al. 2014 PLoS ONE, Meyrowitz 1989 Hypertext Proceedings, Nelson 1965 ACM 20th National Conference, and Nelson 1999 ACM Computing Surveys. Three new primary DOIs verified in publication review pass (Berners-Lee Scientific American 200, Engelbart and English ACM 403 anti-bot matching corpus pattern, Klein PLoS ONE 200).
- Certification barrier compliance verified. Zero certification vocabulary occurrences.
- All scratch confined to project-local `tmp/` per recorded preference.
- Blog deploys through GitHub Actions with a lean Jekyll stack that now includes a post-build pandoc pass generating PDF and EPUB downloads per post from commit db3bc37.
