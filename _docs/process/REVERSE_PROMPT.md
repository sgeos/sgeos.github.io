# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-03
**Task**: A291 publication-review expansion pass. Article is at parity. Anchors 232 to 326, equations 75 to 78, H2 28 to 29, H3 12 to 19.

---

## The Revision That Matters

**The new H2 corrects a claim the article had been making since the first draft.**

The mapping problem said the spinoff leg "terminates the capital-formation problem rather than managing it," on the ground that retained earnings carry neither a milestone requirement nor a dilution. That is too strong and I have said so in the article rather than quietly softening it.

Retained earnings carry no *financial* claim. They carry an **operational** one, and it is not smaller than what it replaced. A subscriber base is a continuing service obligation. A carrier partnership is a contractual obligation to a counterparty holding spectrum the venture does not own. A national authorization is a political obligation to a regulator who can withdraw it. **None of these parties supplied capital, none holds equity, and none appears anywhere in the capital-formation accounting the series has built across three articles.**

The governance point is the sharp one. A287 establishes a control configuration designed so that an investor wanting to redirect the firm must assemble votes it cannot get. That defence is exact against the party it was built against and **absent against every party the third leg creates**, because their leverage does not run through equity at all. A telecom regulator, a carrier declining renewal, or a migrating subscriber base each constrains the firm without holding a share. The dual-class structure the series treats as protecting the mission from capital is no protection whatever here.

I also formalized that the leg's net contribution need not be monotone in the spinoff's scale, and marked that I cannot say whether the turning point has been passed, since both the mission burn and the obligation cost are unpublished.

---

## A Pattern the Series Has Now Hit Three Times

I stated this as a pattern in the article rather than as a third isolated finding.

- **A288**: a portfolio that appears to distribute risk concentrates it on a shared vehicle family.
- **A290**: sub-properties that appear to fail independently fail together under adverse states.
- **A291**: a leg that appears to remove a constraint substitutes a different one.

In all three the framework's own decomposition understates the coupling between the conditions it separates, and the coupling only becomes visible under conditions the observed history does not contain. **I have directed A292 to treat this as a general property of the seven-plus-three framework rather than as three coincidences.** That is probably the most useful thing this pass produced for the closing article.

---

## Survey Expansion

Eleven new cross-disciplinary traditions, five historical precedent cases, seven Historiographical Gap subsections, five analytical framings, expanded contemporary landscape.

The Ostrom commons-governance addition is worth noting because it reframes rather than repeats. Applying the design principles asks whether an orbital-allocation regime *could* work rather than restating that the externality exists. The answer is pessimistic, mainly because the resource boundary is poorly defined and the appropriators are sovereign states rather than a community.

---

## Article Metrics

| Metric | Before | After |
|---|---|---|
| Lines | 1,137 | 1,425 |
| Words | ~14,839 | ~18,955 |
| Display equations | 75 | 78 |
| H2 / H3 | 28 / 12 | 29 / 19 |
| Book references | 46 | 101 |
| Primary reference URLs | 127 | 127 |
| Research references | 39 | 78 |
| **Total reference anchors** | **232** | **326** |
| Missing / unused / duplicate | 0 / 0 / 0 | 0 / 0 / 0 |
| Duplicate URLs | 0 | 0 |
| Style violations | 0 | 0 |

At parity with A290 at 331 anchors. All four reference blocks alphabetical, LaTeX balanced, all macros within the MathJax default set.

---

## Citation Handling

1. **The nineteen anchors identified as fabricated or unregistered in the 2026-08-02 audit were blacklisted from the selection set before drafting**, and the script asserted none had crept in.

2. **Every candidate DOI was checked against Crossref and `doi.org` before use.** One anchor was excluded because its registered metadata names a different book than the citation claims.

3. **Twenty dead links were caught and repaired.** This was the first full sweep of A291's book and research URLs, since the earlier passes covered only the primary-reference anchors. Twelve were older publisher variants my harvest had pulled from the corpus in preference to the repaired Open Library links the sibling drafts already carry, and were fixed by adopting the sibling version. One had no repaired version and got a verified Open Library search URL. Six further inherited publisher pages were repaired the same way. Two research links were repointed at verified DOI targets.

4. **One repair corrected a conflated citation, and the same conflation is live.** The anchor `research_adilov_et_al_2018` claimed the title "An Economic Analysis of Earth Orbit Pollution" with a 2018 date. That paper is **2014**. The 2018 paper by the same authors has a different title entirely. A291 now uses `research_adilov_et_al_2014` pointing at the verified 2014 DOI. **The conflation exists in the published A284 and in the A288 and A289 drafts** and is logged with the other citation debt. It is milder than the thirteen outright mismatches but the same class of error.

5. **A290 is unaffected.** I checked, since it shares several of those anchors. It already carries the repaired URLs, so my earlier "zero 404s" report on it stands.

6. **One verification I could not complete.** After the sweeps, `openlibrary.org` began refusing connections at host level, including to its own root and to a URL that had returned 200 earlier in this same session. That is the documented rate-limiting behaviour rather than evidence of rot, and the substituted URLs are the same ones the sibling drafts already use, but I did not get a clean final re-verification of them and am not going to claim one.

---

## Items Requiring Your Attention

1. **A291 is at parity.** The four-article batch A288 through A291 is ready for authorization.

2. **A288 still carries two fabricated citations**, and the five published articles still carry eleven. That decision is still open and I would resolve it before the batch ships.

3. **Open Library search URLs now stand in for a growing share of book references.** They are stable but weaker than edition pages. This is accumulating across the series and is worth a dedicated pass at some point.

4. **No build verification is possible** until the batch stages together.

---

## Suggested Next Steps

- A292, the closing article. It should pick up the three-instance coupling pattern above and test it across all ten conditions.
- Resolve the citation-integrity remediation.
- Publish A288 through A291 as a four-article batch.
- Broken-link sweep across live A281, A282, and A283.
- Decide the scope of the "the specific" remediation.
