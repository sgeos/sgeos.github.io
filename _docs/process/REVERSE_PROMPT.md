# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-07-20
**Task**: Batch publication of the sixteen-article Machines That Learn From Experience series (A250 through A265) at editorial dates 2025-12-18 through 2026-01-02. Two-commit batch publication pattern per Cross-Linked Series doc. First commit stages all 16 drafts in `_drafts/`. Second commit moves all 16 files to `_posts/` with date prefixes and syncs process files. Series predated the git commit as a pre-NDA contemporaneous record of state-of-the-art literature review.

---

## Series Overview

Sixteen-article comprehensive survey of adaptive, reinforcement, and experiential learning artificial intelligence together with the neuroscience and psychology of learning from which the field has borrowed extensively and to which it contributes reciprocally.

Article inventory by series index and editorial date:

| Index | Article | Date | Slug |
|-------|---------|------|------|
| 1 | A250 Framing | 2025-12-18 | framing |
| 2 | A251 Bandits and Online Learning | 2025-12-19 | bandits_and_online_learning |
| 3 | A252 Reinforcement Learning Foundations | 2025-12-20 | reinforcement_learning_foundations |
| 4 | A253 Deep Reinforcement Learning | 2025-12-21 | deep_reinforcement_learning |
| 5 | A254 Exploration Intrinsic Motivation and Curiosity | 2025-12-22 | exploration_intrinsic_motivation_and_curiosity |
| 6 | A255 Hierarchical Reinforcement Learning | 2025-12-23 | hierarchical_reinforcement_learning |
| 7 | A256 World Models and Predictive Model-Based Adaptation | 2025-12-24 | world_models_and_predictive_model_based_adaptation |
| 8 | A257 Offline and Batch Reinforcement Learning | 2025-12-25 | offline_and_batch_reinforcement_learning |
| 9 | A258 Meta-Learning and Online Adaptation | 2025-12-26 | meta_learning_and_online_adaptation |
| 10 | A259 Continual and Lifelong Learning | 2025-12-27 | continual_and_lifelong_learning |
| 11 | A260 Learning From Demonstration Preference and Other Agents | 2025-12-28 | learning_from_demonstration_preference_and_other_agents |
| 12 | A261 Evolutionary and Open-Ended Adaptation | 2025-12-29 | evolutionary_and_open_ended_adaptation |
| 13 | A262 Embodied Cognition and Developmental Learning | 2025-12-30 | embodied_cognition_and_developmental_learning |
| 14 | A263 NeuroAI What Neuroscience and Machine Learning Took From Each Other | 2025-12-31 | neuroai |
| 15 | A264 From Conditioning to Computation the Psychology of Learning | 2026-01-01 | psychology_of_learning |
| 16 | A265 The Established Public Baseline and the Open Questions | 2026-01-02 | established_public_baseline_and_open_questions |

Editorial-date range fills the sixteen-day gap between `_posts/2025-12-17-solana_with_rust_and_anchor_getting_started.markdown` and `_posts/2026-01-14-metagaming_framework_for_life_strategy.markdown`.

---

## Verification

### Series-Wide Metrics

- Total lines: 12,375 across all 16 articles.
- Total display equations: 690.
- Total primary research references: 1,594.
- Total book references: 162.
- Total related-post cross-references: monotonic. Article N back-references all N-1 prior series articles.

### Cross-Reference Integrity

Cross-references use `post_url` liquid tags. All 15 forward references from within the series resolve to the specific date-prefixed filenames created in this batch publication. Cross-reference structure is back-reference-only, so article N cites articles 1 through N-1 but does not forward-reference article N+1 through 16. A265 as the closer cites all 15 prior articles.

### Anchor Integrity

All 16 articles report zero missing and zero unused reference anchors per Python `re` scan of `][anchor]` citation forms against `^[anchor]:` URL definition forms.

### Style Discipline

All 16 articles report zero em-dashes, zero en-dashes, zero non-possessive contractions, zero prose colons or semicolons outside math notation and reference-list formatting. Certification vocabulary absent. Debug tags `<!-- Axxx -->` and `<script>console.log("Axxx");</script>` present in every article.

### Front-Matter Uniformity

All 16 articles carry `layout: post`, `mathjax: true`, `comments: true`, `categories: artificial-intelligence machine-learning neuroscience`, `series: machines_that_learn_from_experience`, `series_title: Machines That Learn From Experience`, and monotonic `series_index` from 1 through 16.

### Six-Axis Framework Consistency

A250 opener defines the six analytical axes (signal, objective, structure, model, interaction, adaptation). A265 closer recapitulates the same six axes in the "Six-Axis Framework Revisited" section, records the specific series articles that treat each axis, and identifies the specific settled-versus-open partition per axis. The synthesis satisfies A250's specific promise that the closer would "map the whole field onto this framework."

### Four-Pass Workflow

All 16 articles completed the four-pass workflow before batch staging:
1. Initial draft
2. Equation density review
3. Reference density review (primary references)
4. Publication review

---

## Publication Pattern

Two-commit batch publication per `_docs/process/CROSS_LINKED_SERIES.md`:

1. **Draft commit**: Stage all 16 drafts in `_drafts/` and commit. Captures the drafting endpoint in git history before the move to `_posts/`. Commit hash `d1bb03f`.
2. **Publish commit**: Move all 16 files to `_posts/` with date prefixes using `git mv` (the `_publish.sh` script fails under BSD sed on macOS, per corpus history, so `git mv` is used directly). Sync `_docs/process/REVERSE_PROMPT.md` and `_docs/process/TASKLOG.md` in the same commit. This commit triggers the deploy on push.

The batch pattern is required by the series's cross-link topology. Every article in A251 through A265 references at least one earlier article via `post_url`, and A265 references all 15 prior articles. Incremental publication would require each `post_url` to resolve at the time of that article's push, which the back-reference-only structure permits, but the batch pattern is operationally simpler for a sixteen-article corpus authored in advance and provides a single deploy event for the entire series.

---

## Pre-NDA Documentary Context

The series was authored, reviewed, and published as a contemporaneous record of the state of the art in adaptive, reinforcement, and experiential learning artificial intelligence at the closing of the mid-2020s editorial window. The publication commit establishes the specific pre-disclosure timestamp of the record. All 1,594 primary references resolve to publicly available URLs (arXiv, Nature, Science, MLR, NeurIPS, JAIR, ACM, university-hosted PDFs, publisher pages). No proprietary or NDA-covered material appears in the corpus. The corpus documents the specific settled public baseline of the field, distinguishable by inspection from any subsequent disclosure a future non-disclosure agreement might introduce.

---

## Article Number State

- Next available article number: A266.
- A250 through A265 published as sixteen-article batch on 2026-07-20 at editorial dates 2025-12-18 through 2026-01-02.
- All corpus articles through A265 either published or drafted with no gaps in article numbering.

---

## Action Items for the Human Pilot

- Verify the GitHub Actions deploy completes without errors after the push. The build must resolve every `{% post_url %}` tag across the 15 forward references within the series.
- Review the published articles at their permalinks once the deploy completes. Under Jekyll defaults with categories `artificial-intelligence machine-learning neuroscience`, URLs will be of the form `https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/YYYY/MM/DD/<slug>.html`.
- Because the editorial dates 2025-12-18 through 2026-01-02 are all in the past, the articles become visible immediately upon deploy under either `future: true` or `future: false` configuration.
- The `draft_summary.md` was not synced in this commit given the volume of changes. Consider a follow-up `docs:` commit to add the batch entry.

---

## Notes

- Sixteen articles published as sixteen-article batch (2025-12-18 through 2026-01-02 editorial dates).
- Corpus size 265 posts after this publication.
- All scratch confined to project-local `tmp/` per recorded preference.
- Blog deploys through GitHub Actions with the post-build pandoc PDF/EPUB generation pipeline.
- The specific two-commit batch pattern followed the procedure documented in `_docs/process/CROSS_LINKED_SERIES.md` under Batch Publication.
