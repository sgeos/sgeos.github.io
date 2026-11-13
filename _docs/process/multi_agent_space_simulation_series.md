# Multi-Agent Space Simulation Series

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

Plan and standing rulings for the series that reconstructs the thesis of the pilot's lost senior seminar paper on
space simulations, slug `multi_agent_space_simulation`, A386 onward. Planned 2026-11-12 with the pilot. This file is
the series arc on disk. The per-draft status is in [`draft_summary.md`](../../_drafts/draft_summary.md).

## The Arc

| No. | Working title | State | Purpose |
|---|---|---|---|
| A386 | *Multi-Agent Space Simulation: A Reconstructed Thesis* | Drafted, four passes done, economy added, hardened 2026-11-13, not published | The reconstructed paper. Thesis, what a model is, reviews of four products, soft science fiction conventions with remedies, and a blueprint for a high-fidelity multi-agent predictive simulation, with the equations an implementation needs |
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

Items the A386 hardening pass deferred to this article:
- **What compression does to the agents.** A386 shows that a shared compression keeps every physical ratio and does not
  compress human decision time, so light-time delay all but disappears at high compression. A388 should work the
  candidate clocks, a fixed low compression, a clock that varies by region, and private subspaces, and say what each
  costs in predictive value.
- **EVE Online's time dilation**, which slows the clock of one loaded system. It works there because systems are
  discrete rooms. Whether a local clock can exist in a continuous solar system under honest light time is the question.
  It needs a developer source, since A386 does not cite one.
- **A rule for choosing steps** that every machine applies identically. A386 says a fixed-step leapfrog keeps a bounded
  energy error only for a coasting craft, and that close flybys and burns need more.
- **Sources for lockstep and floating-point reproducibility**, which A386 states without citation. Candidates to verify
  are Bettner and Terrano 2001 on lockstep in Age of Empires and Goldberg 1991 on floating-point arithmetic.
- **The cost of the gravity model.** A386 estimates three million inverse-square evaluations a step for one hundred
  thousand craft and thirty bodies, about a tenth of a second on one core. A388 should replace the estimate with a
  measurement.

### A389, Predictive Value

The three bounds, fidelity, approachability and incentives, the meta of Children of a Dead Earth, EVE Online's agents
as evidence that incentives can be met, the cost of real-life scheduling as a stake, and market demand with its
counter-evidence, Kerbal Space Program 2 and Star Citizen's long alpha.

Items the A386 hardening pass deferred to this article:
- **The mapping literature read in full.** A386 cites Castronova et al. 2009, Lofgren and Fefferman 2007 and Williams
  2010 from their abstracts only. A389 should read them, with Castronova 2006, *On the Research Value of Large Games*,
  doi 10.1177/1555412006286686, which was verified and not cited.
- **Selection.** A386 names the limit that agents are volunteers with leisure while the actors of real near-term space
  are states, firms and crews under law and mortal risk. A389 should say what follows from it.
- **Whether a flight model teaches.** A386 infers, from Barnett et al. 2006 and Clement 1982, that flying for years
  under a model that contradicts inertia practises a misconception. No study of a simulation's effect on its agents'
  physics was found. A389 should look for one.
- **The two objections to market demand** that A386 states and does not answer: that the audiences of the soft products
  may be paying for the conveniences honest physics removes, and that Kerbal Space Program 2 closed before it tested
  demand.

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
- **Dated mechanics.** EVE Online's mechanics change. Date each figure by its source. An outdated figure still
  describes how agents played at the time, and it need not invalidate a conclusion.
- **Star Citizen** broadly aspires to a higher-fidelity version of EVE Online's soft science fiction thesis, with its
  own spin. It achieved product-market fit in alpha, which is irregular. Its pledges are not purchases, but the terms
  make them binding. Its mismanagement is the author's judgement, set against the reading that perpetual alpha is
  the business model working.
- **Kerbal Space Program 2** is the one known attempt at many agents on the textbook core in a product for the public.
  Its publisher announced multiplayer and no source records it delivered. Its mismanagement is the author's judgement.
  What the record shows is that the attempt failed in execution before it could test demand.
- **The blueprint's principles**, as of the hardening pass, are five: omit and never contradict, size fidelity per
  subsystem, make the physics approachable and not soft, make loss last, and be open to checking. The last two were
  added by the hardening pass from the article's own third bound and its openness argument, and they await the pilot's
  confirmation.
- **Nothing is published, pushed or forward-dated** without the pilot's approval.

## Research Material

Gitignored scratch under `tmp/a386/`. `research/ksp_code/`, `research/eve_sc/`, `research/eve_econ/`,
`research/scifi/`, `research/stronger/` and `research/harden/` hold the saved pages and the research reports, with
quotations checked verbatim by `tmp/a386/quotecheck.py`. The hardening pass's edits are `tmp/a386/fable1.py` and
`tmp/a386/fable2.py`, and the draft as it stood before them is `tmp/a386/draft_before_fable.markdown`.

## Open Before A386 Publishes

1. **The pilot's rulings on the hardening pass**, done 2026-11-13 with Fable 5.2 and an independent adversarial
   review. They are listed in `REVERSE_PROMPT.md`. In brief: whether the two added principles and the stated
   preferences for true scale and low compression stand, whether "time dilation" meant the clock's compression,
   whether the pilot can attest at first hand that EVE Online's ships slow to rest and that Star Citizen's planets
   do not orbit, whether the passages in the pilot's own voice stay as they are, and whether an article of 18,894
   words should be split.
2. **Import into the source database.** The References section is hand-written and must be generated from
   `_sources/` through a decision file in `_sources/decisions/A386.toml`.
3. **A full URL check.** A bulk check was refused by the permission classifier on 2026-11-13 and was not worked
   around. Most links were fetched successfully during research.
4. **The papers cited from abstracts.** Barnett et al. 2006, Clement 1982, Castronova et al. 2009, Lofgren and
   Fefferman 2007 and Williams 2010 were read only as abstracts, and the article says so. Reading them in full
   would let the article drop that caveat.
5. **The front matter date** is a placeholder, set to the publication time at publication.
