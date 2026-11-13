# Multi-Agent Space Simulation Series

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

Plan and standing rulings for the series that reconstructs the thesis of the pilot's lost senior seminar paper on
space simulations, slug `multi_agent_space_simulation`, A386 onward. Planned 2026-11-12 with the pilot. This file is
the series arc on disk. The per-draft status is in [`draft_summary.md`](../../_drafts/draft_summary.md).

## The Arc

| No. | Working title | State | Purpose |
|---|---|---|---|
| A386 | *Multi-Agent Space Simulation: A Reconstructed Thesis* | Drafted, four passes done, economy added, not published | The reconstructed paper. Thesis, what a model is, reviews of four products, soft science fiction conventions with remedies, and a blueprint for a high-fidelity multi-agent predictive simulation, with the equations an implementation needs |
| A387 | *Since 2021: Research Harnesses and Agent Operators* | Planned | Dates and reviews work after the paper, and tests A386's third claim, that no such simulation is known |
| A388 | *Why It Is Hard: Time, Fuel, Fidelity and Determinism* | Planned | Works the hard problems A386 only names |
| A389 | *Predictive Value* | Planned | Predictive value under three bounds, and market demand tied to educating the public |
| A390 | *A Textbook Sandbox: Keleusma Agents Flying KSP* | Held until the demonstrator exists | The technology demonstrator, stated as a hypothesis to test |

### A387, Since 2021

- KSPDG from MIT Lincoln Laboratory, multi-agent orbital pursuit and evasion in Kerbal Space Program through kRPC,
  with Gym and PettingZoo interfaces, repository created 2022-11-29, and the AIAA Capture the Satellite challenge. The
  AIAA page refused scripted requests with a 403, so it must be checked by search.
- BSK-RL on Basilisk from the University of Colorado's AVS Lab, repository created 2023-06-08. Its own paper is still
  to be found. arXiv 2511.12792, which the admin session attributed to it, is by Hady et al., 2025-11-16, and whether
  it uses BSK-RL is unchecked.
- Language models as spacecraft operators in KSP, all by Carrasco, Rodriguez-Fernandez, Linares and colleagues:
  arXiv 2404.00413 (2024-03-30), 2408.08676 (2024-08-16), 2501.07802 (2025-01-14) and 2505.19896 (2025-05-26).
- Kerbal Space Program 2 and its studio's closure, and Star Citizen's server meshing from Alpha 4.0.
- Candidates to date and test against the third claim: Principia with the multiplayer modifications, Orbiter's
  multiplayer projects, Space Engineers, Elite Dangerous and any newer KSP successor. Whether any pair meets two of
  the three conditions decides whether the post narrows the thesis.

### A388, Why It Is Hard

Shared time and subspaces, the shared clock and its compression, several characters per agent, resolution of events
from committed orders, scheduling across time zones, the rarity of encounters under honest delta-v budgets, accuracy
against accessibility, and deterministic lockstep with fixed-point or fixed-order arithmetic.

### A389, Predictive Value

The three bounds, fidelity, approachability and incentives, the meta of Children of a Dead Earth, EVE Online's agents
as evidence that incentives can be met, the cost of real-life scheduling as a stake, and market demand with its
counter-evidence, Kerbal Space Program 2 and Star Citizen's long alpha.

### A390, the Demonstrator

Keleusma stream processors controlling simulated craft in KSP through kRPC, paired with an MCP server, aiming at a
documented textbook sandbox model. That Keleusma's bounded worst-case time and host-driven stepping suit deterministic
fixed-step agents is a hypothesis for the demonstrator to test, not a finding.

## Standing Rulings

- **The paper is lost.** Present its thesis as a reconstruction from memory. Never invent its title, year, sources,
  figures or wording, and never quote it. Ask the pilot for any detail.
- **Disclosure.** Say "an undergraduate space studies programme". Do not name the university or the course. The
  series may say that the pilot kept meticulous notes and lost them with the paper to a hardware failure, and give the
  pilot's view that undergraduate classes prioritise grading, display of knowledge and verification of academic
  honesty above the quality of the written material.
- **Terms.** Agents, never players. Simulations, never games, except in quotations and titles.
- **Attribution.** The whole series is the author's position. Say so once per article. Mark sourced facts by citation
  and inferences by name, and sort them in the Epistemic State section.
- **Sources.** Public sources and first principles only, with space agency sources wherever one exists. The paper
  cited the Children of a Dead Earth developer blog, and so does A386. The paper also drew on purchased modelling
  texts whose titles the pilot no longer recalls. They are not cited.
- **No reverse engineering** of any product is involved or planned, and the series does not describe one.
- **Products are reviewed as of today**, with the review date stated.
- **Developers are generally competent.** A product reflects product-market fit and its own product thesis. Where it
  falls short of the series' standard, it pursued a different thesis and achieved it, or failed in the attempt.
- **Soft science fiction conventions** are identified and corrected whether they come from the reviewed simulations
  or from other media, each with a remedy that becomes a design rule.
- **The blueprint** is a real-time multi-agent simulation built on the method of Children of a Dead Earth. It takes a
  method, not a product.
- **EVE Online's economy.** Science fantasy in its parts, the best known multi-agent supply chain as a system. Its poor
  models interlock so comprehensively that the whole has predictive value, and its commodity market is its one strong,
  accurate model. Its wrong models have the right fidelity for driving interaction, which the blueprint must match
  while also being true.
- **Nothing is published, pushed or forward-dated** without the pilot's approval.

## Research Material

Gitignored scratch under `tmp/a386/`. `research/ksp_code/`, `research/eve_sc/`, `research/eve_econ/` and `research/scifi/` hold the saved
pages and the research reports, with quotations checked verbatim by `tmp/a386/quotecheck.py`.

## Open Before A386 Publishes

1. **The hardening pass with Fable 5.2**, which the pilot plans next.
2. **Import into the source database.** The References section is hand-written and must be generated from
   `_sources/` through a decision file in `_sources/decisions/A386.toml`.
3. **A full URL check.** A bulk check was refused by the permission classifier on 2026-11-13 and was not worked
   around. Most links were fetched successfully during research.
4. **Glasstone 1964** is cited through an archive.org item labelled with the 1957 edition. A better locator is wanted.
5. **The front matter date** is a placeholder, set to the publication time at publication.
