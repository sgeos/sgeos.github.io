# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-07-16
**Task**: Draft, review, and publish A225-A236 as the twelve-article back-dated series "Industrialization Waves and Geopolitical Positioning" walking successive industrialization waves chronologically from British first-mover industrialization through the contemporary snapshot. Shared main title with per-article subtitles. Editorial dates 2026-03-15 through 2026-03-26 filling exactly the twelve-day gap between A107 Keleusma Getting Started and A206 Programming Language Theory arc opener. Two-commit batch-publication pattern complete; commits pushed to origin/master.

---

## Verification

### Series Complete

Twelve-article back-dated series. Shared main title "Industrialization Waves and Geopolitical Positioning" with per-article subtitle in "Main: Sub" format.

- A225 (index 1, 2026-03-15): Framing and the Preindustrial World. Opener establishing primary-structural rather than sufficient thesis, six-axis framework, Malthusian and organic-economy ceilings, fiscal-military capacity, and preindustrial political map circa 1750.
- A226 (index 2, 2026-03-16): First-Mover Britain. Coal endowment, colonial capital, Napoleonic-era fiscal-military state, textile mechanization, iron-and-steam complex, Pax Britannica, two-power naval standard, sterling reserve decay.
- A227 (index 3, 2026-03-17): Continental European Followers. Gerschenkron paradigmatic case, universal banking, Belgium, France, Germany, Netherlands, Switzerland, Scandinavia, Austria-Hungary, Italy, Iberia, Baumol convergence hypothesis with half-life.
- A228 (index 4, 2026-03-18): American Ascent. Continental internal market, immigration-driven scale, protectionist tariff policy, managerial capitalism, natural-resource abundance, externalized wartime disruption, dollar reserve rise, manufacturing-employment decline.
- A229 (index 5, 2026-03-19): Meiji Japan. First non-Western industrialization from preindustrial baseline, Tokugawa baseline, Perry shock, institutional response, zaibatsu conglomerates, universal conscription and education, imperial expansion, 1945 catastrophe.
- A230 (index 6, 2026-03-20): Soviet Forced Industrialization. Tsarist baseline, 1928 Stalinist turn, First Five-Year Plan, collectivization catastrophe, Great Patriotic War, Cold War buildup, stagnation and structural weakness, 1991 institutional collapse.
- A231 (index 7, 2026-03-21): Postwar Japan and West Germany. Paired case under American occupation and security guarantee, Marshall Plan, Wirtschaftswunder, Japanese economic miracle, alliance-locked geopolitics, contemporary rearmament.
- A232 (index 8, 2026-03-22): East Asian Tigers. South Korea, Taiwan, Singapore, Hong Kong. Developmental-state template extension of Japanese postwar model under Cold War subsidy, land reform, export discipline, financial repression, Young-Krugman debate, 1997 crisis.
- A233 (index 9, 2026-03-23): China's Rise. Post-1978 reform arc, Deng-era liberalization, 2001 WTO accession as hinge point, state-capitalism model, 2008 crisis stimulus, Xi Jinping era, Belt and Road Initiative, systemic-rival positioning.
- A234 (index 10, 2026-03-24): India and the Late Arrivals. Post-1991 Indian liberalization, service-sector-driven growth, Vietnam Đổi Mới, Bangladesh garment sector, Indonesia post-1998 recovery, middle-income trap question.
- A235 (index 11, 2026-03-25): The Non-Industrializers and Edge Cases. Middle Eastern oil states, post-Soviet Russia, Sub-Saharan Africa, Latin America outside industrial cluster, Central Asia, Iran, North Korea, Israel-Palestine. Framework limits explicit.
- A236 (index 12, 2026-03-26): Contemporary Snapshot and Extrapolation. Closer with contemporary configuration as of 2026, forward extrapolation across 2026-2050 window, competing extrapolation strategies from Kotkin, Sachs, Perez, Smil, and Zeihan as illustrative alternatives, load-bearing open questions.

### Equation Density

Fifty-two display equations across twelve articles. A225 opener heaviest at nine equations establishing the framework. Case articles A226 through A234 carry three to five equations each anchoring case-specific mechanisms. A235 edge-case article and A236 closer carry three each with appropriate lightness for their synthesis roles.

Cross-case comparability: Gerschenkron growth-rate premium formalized for Britain (implicit), Germany (approximately two percentage points), Japan (3.6 percent per year), Korea (3.1 percent per year), China (5.2 percent per year), Vietnam (6.3 percent per year), and India (2.7 percent per year), enabling explicit cross-case comparison of catch-up performance intensity.

### Reference Density

One hundred seventy total references across twelve articles. A225 opener carries twenty-nine references including ten primary research papers. Case articles A226 through A234 carry eleven to nineteen references each. A236 closer carries twelve references anchored to books for the named extrapolation-strategy analysts. All twelve articles have refs_defined == refs_used with no dangling anchors or uncited definitions.

Primary research anchor examples: Broadberry-Guan-Li on Great Divergence, North-Weingast on constitutional commitment, Karaman-Pamuk on European fiscal capacity, Klein et al. on reference rot, Naumenko on Ukrainian famine, Cheremukhin-Golosov-Guriev-Tsyvinski on Stalin counterfactual, Song-Storesletten-Zilibotti on Chinese growth, Horn-Reinhart-Trebesch on Chinese overseas lending, Autor-Dorn-Hanson on China Syndrome, Sachs-Warner on resource curse, Ross on oil and democracy, Nunn on African slave trades.

### Style Verification

Zero em-dashes, en-dashes, contractions, prose colons, prose semicolons, prose parentheticals outside math notation, or certification vocabulary across all twelve articles. Debug tags `<!-- Axxx -->` and `console.log("Axxx")` present in all twelve at consistent positions. Categories `history economics geopolitics` uniform. Series metadata `industrialization_waves` slug with `Industrialization Waves and Geopolitical Positioning` title and indices one through twelve. Front-matter titles use "Main: Sub" format placing shared main title before per-article subtitle.

### Collision and Flush Verification

Article numbers A225 through A236 verified unique across `_posts/` and `_drafts/`. Editorial dates 2026-03-15 through 2026-03-26 verified empty in both directories prior to publication. Adjacent published dates 2026-03-14 (A107 Keleusma Getting Started) and 2026-03-27 (A206 Programming Language Theory arc opener) populate the twelve-day gap boundaries. Series fills the gap exactly without offset or overlap. Next available article number after publication is A237.

Category shadow check: `history` at first position was previously verified during A222 and A223 publication reviews to have no shadowing `sgeos/history` GitHub Pages project.

### Two-Commit Publication Pattern

Standard two-commit batch publication.

- Draft-stage commits: A225-A236 individual drafts, per-article equation-density and reference-density review passes, per-article publication reviews, series-wide consistency pass with title standardization to Main: Sub format.
- Publish commit follows with `git mv` batch moving all twelve drafts to `_posts/` with editorial-date prefixes plus TASKLOG, draft summary, and REVERSE_PROMPT synchronization.

Commits pushed to origin/master per human pilot instruction.

---

## Article Number State

- Next available article number: A237.
- A225-A236 published as twelve-article batch across editorial dates 2026-03-15 through 2026-03-26.

---

## Action Items for the Human Pilot

- Verify the GitHub Actions deploy completes without errors after the push. The series uses `{% post_url %}` cross-references extensively across all twelve articles plus references outside the series to A97 and A98 which are already deployed.
- Review the published series at the permalinks once the deploy completes. Base URL pattern is `https://sgeos.github.io/history/economics/geopolitics/2026/03/DD/SLUG.html` per each article's date and slug.
- Consider whether the series roadmap in A225 should be updated to reflect the specifically published subtitles, since some may have shifted during drafting. Current opener text was written before the subtitles were finalized to Main: Sub format.
- Consider whether follow-up articles on specific extrapolation strategies (Kotkin demographic-projection depth, Perez technological-long-wave depth, Smil energy-transition depth) would be productive future work. The A236 closer positions such follow-ups as consequences of the series framework rather than as freestanding preferences.

---

## Notes

- Next available article number: A237.
- 0 release candidates.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification in `_drafts/`.
- Published through A236 across the combined article number space.
- Corpus size 236 posts, editorial dates span 2016 through 2026-07-11.
- Series comprises the largest single back-dated batch publication in the corpus after the Programming Language Theory arc (A206-A215, ten articles) and the Rocket Propellant Chemistry series (A217-A221, five articles). At twelve articles it exceeds both.
- Total series length approximately 2,300 lines across twelve articles, averaging 190 lines per article with the opener at 356 lines and shorter synthesis and edge-case articles around 140-160 lines.
- Certification barrier compliance verified. Zero certification vocabulary occurrences series-wide.
- All scratch confined to project-local `tmp/` per recorded preference.
- Blog deploys through GitHub Actions with the post-build pandoc PDF/EPUB generation pipeline from commit db3bc37 exercised against the full corpus.
