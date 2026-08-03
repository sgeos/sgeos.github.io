# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-02
**Task**: A290 publication-review expansion pass. Article is at parity. **The pass also uncovered a citation-integrity defect affecting five published articles that needs your decision.**

---

## Read This First

A Crossref and `doi.org` audit of every DOI-bearing citation in the History of SpaceX corpus found **thirteen citations whose stated title and target document do not correspond**, plus five DOIs that are not registered at all.

**Every one of these URLs returns HTTP 200.** The link sweeps run at each prior publication passed all of them, including mine. A status check confirms a URL resolves. It does not confirm the document is the work the citation names.

| Anchor | Claimed | Actually resolves to | Where |
|---|---|---|---|
| research_alchian_1963 | Alchian 1963 Reliability of Progress Curves in Airframe Production | "Leverage and the Cost of Capital", Solomon | **A282 live** |
| research_sanchez_1993 | Sanchez 1993 Strategic Flexibility Firm Organization | "Strategic resources", Black and Boal 2007 | **A282 live** |
| research_munir_phillips_2005 | Munir and Phillips 2005 The Birth of the Kodak Moment | "The Integration Journey", Yu et al | **A284 live** |
| research_pisano_teece_2007 | Pisano and Teece 2007 How to Capture Value from Innovation | "From the Editor", Vogel 2005 | **A284 live** |
| research_bergstresser_2020 | Bergstresser 2020 Space Traffic Management Priorities | "Robust Inference for Consumption-Based Asset Pricing", Kleibergen and Zhan | **A284 live** |
| research_kilmichael_musk_2003 | Kilmichael Musk 2003 Falcon Launch Vehicles An Overview | "Control of Wing Rock Motion", Xin and Balakrishnan | **A285 live** |
| research_zahra_2015 | Zahra 2015 Corporate Entrepreneurship as Knowledge Creation | "Proposing Social Resources as the Fundamental Catalyst", Tocher et al | **A285 live** |
| research_bjelde_et_al_2007 | Bjelde et al 2007 Falcon 1 Demonstration Flights | "Space Hardware Cost Improvement Curve Update", Mackenzie and Parlanti | **A286 live** |
| research_dutton_thomas_1984 | Dutton and Thomas 1984 Treating Progress Functions | "Self-Fulfilling Prophecy as a Management Tool", Eden | **A286 live** |
| research_suarez_utterback_1995 | Suarez and Utterback 1995 Dominant Designs | "Japanese spinoffs", Ito 1995 | **A286 live** |
| research_kalnins_mayer_2004 | Kalnins and Mayer 2004 Relationships and Hybrid Contracts | "Focusing Firm Evolution", Williams and Mitchell | **A287 live** |
| research_maccormack_baldwin_rusnak_2012 | MacCormack Baldwin and Rusnak 2012 | "CEO Overconfidence and Innovation", Galasso and Simcoe | A288 draft |
| research_villalonga_2004 | Villalonga 2004 Does Diversification Cause the Discount | "Convertible Bond Design", Korkeamaki and Moore | A288 draft |

Five more DOIs are unregistered, meaning `doi.org` returns no redirect and the identifier was constructed: `research_block_2008`, `research_weiss_thurbon_2021`, `research_ross_staw_1993`, `book_logsdon_2010`, and `book_lundvall_1992` whose DOI resolves to an unrelated book called "Gales".

**What I did.** All six that would have entered A290 were removed before this commit, including `research_ross_staw_1993`, which was already in the draft from the original drafting session. **A290 is clean.** I extended `_docs/process/URL_VERIFICATION.md` with a section on why a 200 does not verify a citation and the two registry commands that catch this.

**What I did not do.** I have not touched the published articles. Removing citations from five live posts is your call, not mine. The affected passages will need rewriting or re-sourcing rather than a find-and-replace, since in most cases the claim is fine and only the reference is wrong.

I would treat this as higher priority than publishing the A288 to A290 batch. A288 carries two of them and would ship them into a sixth live article.

---

## The Publication Review Itself

**New H2: The Adverse-State Financing Regime.** The article had established that the mechanism supplies patience in good states and none in bad ones, and then never said what happens in the bad state. The new section says.

A venture whose prospects deteriorate does not stop raising. It raises on down rounds, senior liquidation preferences, participating preferred, full-ratchet anti-dilution, pay-to-play, and venture debt. Every one of those moves the supplying claim toward a fixed prioritized position. **So the claim-type sub-property is not a property of equity as an instrument. It is a state-contingent property of the equity a venture can issue**, and it degrades exactly where it would carry the most value.

That forces a correction to the article's own framework. The pattern extraction states five sub-properties and writes them as a product, which assumes independent failure. They are not independent. An adverse state withdraws the realization path, degrades the claim type, and concentrates the holder base simultaneously. **Three of five fail on one common cause**, so the product overstates joint survival and is a diagnostic checklist rather than a probability model. I updated the Pattern Extraction and the open questions to carry this rather than leaving it buried in the new section.

This is the financing analogue of the A288 finding that four of five portfolio lines share a vehicle family. In both cases an arrangement that looks like it distributes risk turns out to concentrate it, and in both cases the concentration is invisible in the observed history. I have directed A292 to examine whether the correlation is general across all ten conditions.

The section is marked as weakly evidenced, because no adverse-state round is observable in this case and the reasoning is from the documented instrument set rather than from any transaction.

**Survey expansion.** Seven new cross-disciplinary traditions, five historical precedent cases including the Venetian and Genoese partnership forms and East Asian state-directed industrial finance, five Historiographical Gap subsections, five analytical framings.

---

## Article Metrics

| Metric | Before | After |
|---|---|---|
| Lines | 1,167 | 1,439 |
| Words | ~18,734 | ~23,301 |
| Display equations | 74 | 77 |
| H2 / H3 | 27 / 11 | 28 / 16 |
| Book references | 54 | 106 |
| Primary reference URLs | 134 | 134 |
| Research references | 31 | 72 |
| **Total reference anchors** | **238** | **331** |
| Missing / unused / duplicate | 0 / 0 / 0 | 0 / 0 / 0 |
| Duplicate URLs | 0 | 0 |
| Style violations | 0 | 0 |

LaTeX balanced at 68 matched pairs, braces and array environments matched, all macros within the MathJax default package set. Full sweep of all 178 book and research URLs returned **zero 404 responses**; every non-200 is documented publisher bot-detection or rate-limiting.

---

## Items Requiring Your Attention

1. **The citation-integrity defect above.** Needs a decision before the batch publishes.
2. **Consolidated two Zubrin anchors** that pointed at the same publisher page for The Case for Mars.
3. **A290 is at parity** and the three-article batch is otherwise ready for authorization.
4. **Still no build verification and still none possible** until the batch stages together.

---

## Suggested Next Steps

- Decide how to handle the fabricated citations in A282, A284, A285, A286, and A287, and fix the two in A288 before it publishes.
- Consider a corpus-wide DOI audit beyond this series, since nothing about the failure is specific to these articles.
- Then A291 Category-Dominating Commercial Spinoff at editorial date 2026-08-03 09:00 UTC.
- Publish A288, A289, and A290 as a batch.
- Broken-link sweep across live A281, A282, and A283.
- Decide the scope of the "the specific" remediation.
