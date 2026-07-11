# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-07-11
**Task**: Research, draft, verify, and publish A217-A221 as a five-article back-dated series on rocket propellant chemistry. Editorial dates 2026-02-01 through 2026-02-05. Two-commit batch publication sequence complete. All commits pushed to origin/master per human pilot instruction.

---

## Verification

### Series Structure Complete

Five-article back-dated series with shared main title "Rocket Propellant Chemistry," across all articles. Editorial dates fill the exact open block between `_posts/2026-01-31-claude_code_getting_started.markdown` and `_posts/2026-02-06-bidirectional_agentic_workflow.markdown`, ending flush at 2026-02-05 one day before the dense A75-A151 published block resumes.

- A217 (2026-02-01) Rocket Propellant Chemistry, A Design-Tradeoff Space. 586 lines. Seven display equations establishing series vocabulary: specific impulse definition, effective exhaust velocity, general thrust equation, ideal specific impulse formula through chamber temperature and average molecular weight, characteristic velocity, thrust coefficient, density specific impulse.
- A218 (2026-02-02) Rocket Propellant Chemistry, Solid Propellants. 658 lines. Six display equations: Vieille's law, temperature sensitivity coefficient, density specific impulse, ammonium perchlorate decomposition, aluminum combustion, ammonium dinitramide decomposition. Covers composite (AP-HTPB-Al with representative Shuttle SRB and Ariane 5 formulations), double-base (NC-NG), composite modified double-base, research frontier (ADN, HTPE, alane), grain geometry, tradeoffs, applications, industrial base.
- A219 (2026-02-03) Rocket Propellant Chemistry, Cryogenic Liquid Propellants. 670 lines. Six display equations: hydrolox combustion, oxidizer-to-fuel ratio definition, optimum mixture-ratio stationary condition, methalox combustion, kerolox combustion, ethanol combustion. Covers hydrolox (RS-25, RL10, Vulcain 2 and 2.1, Vinci, LE-9), methalox (Raptor V2, BE-4), kerolox (F-1, Merlin 1D, RD-180, YF-100), V-2 ethanol historical context, ortho-para hydrogen conversion, densified propellants, RP-1 specification, coking constraints, five power cycles, regenerative cooling.
- A220 (2026-02-04) Rocket Propellant Chemistry, Storable and Hypergolic Liquid Propellants. 646 lines. Six display equations: NTO with MMH combustion, NTO with UDMH combustion, hydrazine decomposition step one, hydrazine decomposition step two, HTP decomposition, IRFNA with kerosene combustion. Covers NTO with MMH (R-40, R-4D, OMS), UDMH (YF-20 series, RD-253), and Aerozine 50 (Titan LR87 and LR91, Apollo LM descent and ascent, Apollo SPS, Delta II AJ10-118K); IRFNA with kerosene on Scud A AK-20I and Scud B AK-27P; hydrazine monopropellant with Shell 405 iridium-alumina catalyst; concentrated hydrogen peroxide monopropellant with silver-plated screens; green monopropellants LMP-103S and AF-M315E ASCENT; hypergolic ignition mechanism; toxicity and REACH regulations.
- A221 (2026-02-05) Rocket Propellant Chemistry, Hybrid Propellants. 537 lines. Six display equations: Marxman-Gilbert regression rate law, HTPB butadiene combustion, paraffin combustion, nitrous oxide decomposition, HTPB with nitrous oxide combustion, paraffin with nitrous oxide combustion. Covers classical HTPB fuels, paraffin fuels with melt-layer entrainment mechanism from Karabeyoglu Stanford Space Propulsion Group, nitrous oxide storable hybrids (SpaceShipOne and SpaceShipTwo), metallized hybrids, alternative oxidizers, combustion instability classes. Closes the series with a family recap.

### Chemistry Equation Balance

All thirty-one display equations across the series verified balanced. Chemistry balances verified atom-by-atom across all combustion and decomposition equations. Two mid-review corrections applied: NTO-UDMH combustion equation in A220 (excess oxygen removed to match stated 3.1 to 1 mass ratio), N2O role in A221 (nitrogen correctly identified as inert diluent rather than partial fuel, molecular weight direction corrected).

### Style Verification

Zero em-dashes, en-dashes, contractions, prose semicolons, prose colons, prose parentheticals, certification vocabulary series-wide. Debug tags `<!-- A2xx -->` and `console.log("A2xx")` present in all five articles at lines 10-11. Categories `aerospace propulsion chemistry` uniform.

### Cross-Reference Chain

Twenty `post_url` cross-references across the series, all resolve at batch publication.

- A217 opener forward-references each of A218-A221 by number with descriptive summaries.
- A218-A221 backward-reference A217 for ideal specific impulse formula and other opener vocabulary.
- Family articles cross-reference each other at points where chemistries are shared: LMP-103S bridges A218 and A220, density specific impulse bridges A218 and A219, optimum oxidizer-to-fuel ratio bridges A219 and A220 and A221.
- Chain completeness: A217 → A218 → A219 → A220 → A221 with each next-article pointer correctly named. A221 closes the series with a family recap.

### External URL Verification

Sixteen external references across the series. All verified.

- Sutton and Biblarz Rocket Propulsion Elements ninth edition Wiley: URL 200. Used across all five articles as the standard propulsion reference.
- Sutton History of Liquid Propellant Rocket Engines AIAA 2006: AIAA URL 403 anti-bot pattern with indexed confirmation via Amazon, Google Books, Biblio, and ALA. Used in A219, A220, A221.
- Yang Habiballah Popp Hulka editors Liquid Rocket Thrust Chambers Aspects of Modeling Analysis and Design AIAA 2004: AIAA URL 403 anti-bot pattern with indexed confirmation via Amazon, Biblio, and Skillsoft. Used in A219 and A220.
- Huzel and Huang Modern Engineering for Design of Liquid-Propellant Rocket Engines AIAA 1992: AIAA URL 403 anti-bot pattern with indexed confirmation via ADS, Amazon, Biblio, and ResearchGate. Used in A219 and A220.
- Kubota Propellants and Explosives Thermochemical Aspects of Combustion third edition Wiley-VCH 2015: Wiley Online Books URL 403 anti-bot pattern with indexed confirmation via Amazon, AbeBooks, Wiley-VCH, and Internet Archive. Used in A218.
- Davenas editor Solid Rocket Propulsion Technology Pergamon 1993: ScienceDirect URL 403 anti-bot pattern with indexed confirmation via WorldCat, Blackwell's, and Biblio. Used in A218.
- Kuo and Summerfield editors Fundamentals of Solid-Propellant Combustion AIAA 1984: AIAA URL 403 anti-bot pattern with indexed confirmation via Amazon, AbeBooks, and Google Books. Used in A218.
- Clark Ignition, An Informal History of Liquid Rocket Propellants Rutgers 1972 reprinted 2018: URL 200. Used in A220.
- Chiaverini and Kuo editors Fundamentals of Hybrid Rocket Combustion and Propulsion AIAA 2007: AIAA URL 403 anti-bot pattern with indexed confirmation via Amazon and Cambridge. Used in A221.
- Karabeyoglu Altman Cantwell Combustion of Liquefying Hybrid Propellants Part 1 General Theory Journal of Propulsion and Power 18 2002: AIAA URL 403 anti-bot pattern with indexed confirmation via Stanford PDF, Semantic Scholar, and ResearchGate. Used in A221.
- Marxman and Gilbert Turbulent Boundary Layer Combustion in the Hybrid Rocket Symposium International on Combustion 9 1963: DOI 200. Used in A221.

### Mid-Review Factual Corrections

Substantive corrections applied during publication reviews:

- A218 aluminum oxide phase description clarified for two-phase-flow loss.
- A218 grain formulation percentages verified against Shuttle SRB PBAN specification.
- A218 CMDB missile examples generalized (Trident II D5 and Minuteman III use nitrate ester plasticized polyether variants, not classical CMDB).
- A219 Vulcain 2 and Vulcain 2.1 variants distinguished for Ariane 5 and Ariane 6 respectively.
- A219 hydrolox first-stage Isp ranges corrected to include Vulcain 2 sea-level value ($315$ to $370$ seconds SL, $425$ to $452$ seconds vacuum) with rationale about the RS-25 staged-combustion upper bound and Vulcain 2 gas-generator lower bound.
- A220 Aerojet AJ10-118K moved to Aerozine 50 section from MMH section (confirmed via search that AJ10-118K burns Aerozine 50, not MMH).
- A220 Scud AK oxidizer designations corrected from "AK-27P or AK-27S" to "AK-20I on Scud A and AK-27P on Scud B" (AK-27S did not exist).
- A220 NTO threshold limit value description generalized (specific $3$ ppm figure is historical rather than current).
- A220 NTO-UDMH combustion equation corrected to remove excess oxygen and match stated stoichiometric ratio.
- A221 SpaceShipOne chamber pressure removed from prose (source data conflicts across search results).
- A221 N2O ballast role corrected (nitrogen is inert diluent, not partial fuel).
- A221 Marxman-Gilbert DOI corrected from an incorrect suffix.

### Series Cohesiveness Pass

Series cohesiveness pass verified:

- No article-number collisions with existing published posts or drafts. Debug tags for A217-A221 appear only in the five drafts.
- No editorial-date collisions. Slots 2026-02-01 through 2026-02-05 were empty in `_posts/` prior to batch publication.
- Flush endpoint verified. Series ends at 2026-02-05 one day before the dense A75-A151 published block starts at 2026-02-06 with `bidirectional_agentic_workflow.markdown`.
- Terminology uniform. "Specific impulse", "mixture ratio", "oxidizer-to-fuel ratio", chemical formulas, and engine designations consistent across all five articles.
- Chemical vocabulary chain consistent. HTPB introduced in A218 (as binder), reused in A221 (as neat fuel). ADN introduced in A218, reused in A220 (as LMP-103S component). LMP-103S referenced consistently across A217 opener, A218 introduction, and A220 detailed coverage.
- Shared reference URLs identical across articles (Sutton-Biblarz identical URL across five articles; Sutton History across three; Yang et al. across two; Huzel-Huang across two).
- Anchor prefix convention `ref_` for references and `related_post_` for cross-references uniform across all five articles.

### Two-Commit Publication Pattern

Two-commit batch publication sequence complete.

- Draft commit `2561e2b` captures all five finalised drafts plus draft summary update.
- Publish commit follows with batch `git mv` of all five drafts to `_posts/` plus TASKLOG, draft summary, and REVERSE_PROMPT synchronisation.
- All commits pushed to `origin/master` per human pilot instruction.

---

## Article Number State

- Next available article number: A222.
- A217 through A221 published as five-article back-dated series covering rocket propellant chemistry at editorial dates 2026-02-01 through 2026-02-05.

---

## Action Items for the Human Pilot

- Verify the GitHub Actions deploy completes without errors after the push. The series uses `{% post_url %}` cross-references internally (all resolve at batch publication) and to A90 (Introduction to Space Studies) and A120 (Staged and Boosted Propulsion) which are already deployed.
- Review the published articles at their permalinks once the deploy completes at the following URLs:
  - `https://sgeos.github.io/aerospace/propulsion/chemistry/2026/02/01/rocket_propellant_chemistry_a_design_tradeoff_space.html`
  - `https://sgeos.github.io/aerospace/propulsion/chemistry/2026/02/02/rocket_propellant_chemistry_solid_propellants.html`
  - `https://sgeos.github.io/aerospace/propulsion/chemistry/2026/02/03/rocket_propellant_chemistry_cryogenic_liquid_propellants.html`
  - `https://sgeos.github.io/aerospace/propulsion/chemistry/2026/02/04/rocket_propellant_chemistry_storable_and_hypergolic_liquid_propellants.html`
  - `https://sgeos.github.io/aerospace/propulsion/chemistry/2026/02/05/rocket_propellant_chemistry_hybrid_propellants.html`
- The next available article number is A222. The rocket propellant chemistry taxonomy is now complete in public-facing form covering solid, cryogenic liquid, storable liquid, and hybrid families with a design-tradeoff opener.

---

## Notes

- Next available article number: A222.
- 0 release candidates from the recent series.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification in `_drafts/`.
- Published through A221 across the combined article number space.
- The rocket propellant chemistry series now covers the full chemical propellant taxonomy in public-facing form. The opener article establishes vocabulary (specific impulse, ideal Isp formula, characteristic velocity, thrust coefficient, mixture ratio, density specific impulse), and the four family articles apply the vocabulary to solid, cryogenic liquid, storable liquid, and hybrid combinations. Every article carries chemistry-specific display equations for combustion and decomposition reactions plus family-specific analytical relations.
- Primary-source verification pass was performed across all five articles. Corrections applied during publication reviews are catalogued above.
- Certification barrier compliance verified. Zero occurrences across the series.
- All scratch is confined to project-local `tmp/` per recorded preference.
- Blog deploys through GitHub Actions with a lean Jekyll stack.
