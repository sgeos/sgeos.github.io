# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-06-24
**Task**: Batch publish the sister session's twelve-article patent-and-startup strategy series A161 through A172 across back-dated 2026-05-03 through 2026-05-14

---

## Verification

### Batch Publication Executed

Twelve articles moved from `_drafts/` to `_posts/` with date prefix matching front-matter dates. The article numbers A161 through A172 were already written into each file's debug markers by the sister session, and the publication dates 2026-05-03 through 2026-05-14 were already set in each file's front matter. No content edits applied. The batch fills the open calendar slots immediately before the SAR drone series begins at 2026-05-15.

The twelve articles published as a single batch:

- A161 (2026-05-03): What a Patent Is and Is Not — `_posts/2026-05-03-what_a_patent_is_and_is_not.markdown`
- A162 (2026-05-04): Prior Art and the Foundation of Patentability — `_posts/2026-05-04-prior_art_and_the_foundation_of_patentability.markdown`
- A163 (2026-05-05): What Makes a Patent an Effective Moat — `_posts/2026-05-05-what_makes_a_patent_an_effective_moat.markdown`
- A164 (2026-05-06): Patents, Trade Secrets, and the Disclosure Tradeoff — `_posts/2026-05-06-patents_trade_secrets_and_the_disclosure_tradeoff.markdown`
- A165 (2026-05-07): Patents for the Early Stage Founder — `_posts/2026-05-07-patents_for_the_early_stage_founder.markdown`
- A166 (2026-05-08): Patent Enforcement Reality — `_posts/2026-05-08-patent_enforcement_reality.markdown`
- A167 (2026-05-09): Why Startups Actually Fail — `_posts/2026-05-09-why_startups_actually_fail.markdown`
- A168 (2026-05-10): Funnel of Startup Failure — `_posts/2026-05-10-funnel_of_startup_failure.markdown`
- A169 (2026-05-11): Product Market Fit — `_posts/2026-05-11-product_market_fit.markdown`
- A170 (2026-05-12): Build and Execution Risk — `_posts/2026-05-12-build_and_execution_risk.markdown`
- A171 (2026-05-13): Distribution and Getting Paid — `_posts/2026-05-13-distribution_and_getting_paid.markdown`
- A172 (2026-05-14): What It Takes to Succeed and Where Moats Come From — `_posts/2026-05-14-what_it_takes_to_succeed_and_where_moats_come_from.markdown`

The articles cross-link each other through `{% post_url %}` Liquid tags that reference the dated filenames, so all twelve were moved as a single batch before the build to ensure every link resolves. The cross-link target into A139 at `_posts/2026-06-22-data_rights_and_intellectual_property_for_sbir_and_sttr.markdown` is already published, so that link resolves without action.

### Two-Commit Publication Pattern

The publication follows the established two-commit pattern. The draft commit at `6974a11` staged all twelve drafts in `_drafts/` to capture the draft state in git history. The publish commit moves all twelve from `_drafts/` to `_posts/` with the date prefix and updates the process files. The git rename detection preserves the file history across the move.

### Build Verification

The local bundle build remains broken in this environment; the deploy build runs via the GitHub Actions pipeline after the push. Because the dates 2026-05-03 through 2026-05-14 are back-dated relative to today (2026-06-24), these posts appear at their May positions immediately upon deploy and do not depend on the `future: true` setting that the forward-dated work relies on.

### Status of Process Files

The `_drafts/draft_summary.md` document tracked the analog-facilities series in detail and did not maintain entries for the sister session's parallel series. The summary is left unchanged regarding the sister session's batch; the sister session can extend the summary document with its own entries if it prefers. The current draft_summary.md reflects the analog-facilities series state through A160 as the last update.

### Git Status

`git status` confirms twelve renames from `_drafts/` to `_posts/` in the publish commit with no other content touched, plus the REVERSE_PROMPT.md update in the same commit. The eight long-standing pre-release candidate drafts remain in `_drafts/` awaiting human verification.

---

## Article Number State

The article number space across the blog now reads as follows.

- A1 through A74: legacy published posts predating the modern numbered tracking.
- A75 through A151: published series across 2026-02-06 through 2026-03-14 (the SBIR/STTR series, the BTRON/Keleusma series, the fixed-wing UAV series, the SAR drone series, and standalone articles).
- A152 through A160: analog-facilities series, published 2026-06-28 through 2026-07-06.
- A161 through A172: patent and startup strategy series, published 2026-05-03 through 2026-05-14 in this batch.
- Next available article number: A173.

The analog-facilities series and the patent and startup strategy series are independent. The patent and startup strategy series back-dated dates fall before the analog-facilities series forward-dated dates, so the two series do not collide on date or article number despite being authored in parallel by separate sessions.

---

## Sister Session Coordination

The sister session in the adversarial case intelligence repository drafted and published the patent and startup strategy series under the explicit batch publication prompt that the human pilot relayed. The drafts were ready when delivered, with article numbers and publication dates pre-assigned. The master session executed the batch publication per the prompt. The sister session may have further drafts to deliver; this REVERSE_PROMPT.md will be overwritten on the next task.

---

## Action Items for the Human Pilot

- Verify the GitHub Actions deploy completes without `post_url` resolution errors after the push. The cross-link integrity within the twelve-article series and the cross-link to A139 should all resolve.
- Review the twelve published articles at their permalinks once the deploy completes:
  - https://sgeos.github.io/.../2026/05/03/what_a_patent_is_and_is_not.html through https://sgeos.github.io/.../2026/05/14/what_it_takes_to_succeed_and_where_moats_come_from.html
- The article number space now runs continuously through A172. A173 is the next available.
- Confirm whether the sister session has additional drafts in the pipeline or whether this batch was its terminus.

---

## Notes

- Next available article number: A173.
- 0 release candidates from either the analog-facilities or the patent and startup strategy series.
- 0 stubs.
- Eight long-standing pre-release candidate drafts remain awaiting human verification in `_drafts/`.
- Published through A172 across the combined article number space.
- The patent and startup strategy series spans A161 through A172 across 2026-05-03 through 2026-05-14, organised as a six-article patents arc (A161-A166: what a patent is, prior art, what makes an effective moat, patents versus trade secrets, patents for the early-stage founder, enforcement reality) followed by a six-article startup arc (A167-A172: why startups fail, the funnel of failure, product market fit, build and execution risk, distribution and getting paid, what it takes to succeed and where moats come from).
- The analog-facilities series A152 through A160 remains complete on the forward-dated side at 2026-06-28 through 2026-07-06.
- All scratch is confined to project-local `tmp/` per recorded preference.
- The article drafting guidelines at `tmp/article_drafting_guidelines.md` were captured during A152 through A156 and have since been broadened by the human pilot to cover the other article genres on the blog. The patent and startup strategy series follows the analytical-essay genre rather than the subsystem deep-dive pattern.
- Blog deploys through GitHub Actions with a lean Jekyll stack; `future: true` is enabled in `_config.yml`. The patent and startup strategy series is back-dated and renders without dependence on the future flag.
