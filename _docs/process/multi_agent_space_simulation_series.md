# Multi-Agent Space Simulation Series

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

Plan and standing rulings for the series that reconstructs the thesis of the pilot's lost senior seminar paper on
space simulations, slug `multi_agent_space_simulation`, A386 onward. Planned 2026-11-12 with the pilot. This file is
the series arc on disk. The per-draft status is in [`draft_summary.md`](../../_drafts/draft_summary.md).

## The Arc

| No. | Working title | State | Purpose |
|---|---|---|---|
| A386 | *Multi-Agent Space Simulation: A Reconstructed Thesis* | Drafted, four passes done, economy added, seven publication passes done 2026-11-13, references in the source database, not published | The reconstructed paper. Thesis, what a model is, reviews of four products, soft science fiction conventions with remedies, and a blueprint for a high-fidelity multi-agent predictive simulation, with the equations an implementation needs |
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

Items the A386 hardening passes deferred to this article. A386 now cites sources for lockstep, floating-point
reproducibility, symplectic integration, the cost of a force evaluation and EVE Online's time dilation, so A388 starts
from those and not from nothing:
- **What compression does to the agents.** A386 shows that a shared compression keeps every physical ratio and does not
  compress human decision time, so light-time delay all but disappears at high compression. A388 should work the
  candidate clocks, a fixed low compression, a clock that varies by region, and private subspaces, and say what each
  costs in predictive value.
- **EVE Online's time dilation**, which slows the clock of the server process that hosts an overloaded system, down
  to a floor of 10 percent. A386 cites the developer for it and says only that a world on one clock cannot slow one
  region. Whether a local clock can exist in a continuous solar system under honest light time is the question.
- **A rule for choosing steps** that every machine applies identically. A386 says a fixed-step leapfrog keeps a bounded
  energy error only for a coasting craft, and that close flybys and burns need more.
- **Reversible step control.** A386 cites Hairer and Soderlind 2005 for a step rule that keeps the long-term behaviour
  of a symplectic method. A388 should say whether it suits a craft among moving planets, where energy is not conserved.
- **The cost of the gravity model.** A386 estimates it from a published benchmark, about 0.06 seconds a step for one
  hundred thousand craft feeling thirty bodies, and 6 milliseconds when each craft is bound to a parent body. A388
  should replace the estimate with a measurement, and cost the planning tools, which A386 says may cost more.
- **Sharding by parent body.** A386 proposes the neighbourhood of each body as a shard and light time as the slack
  for agreement between shards. A388 should work the hand-off at the sphere of influence and what compression does to
  the slack.
- **Clocks.** A386 gives each craft a clock at the weak-field rate. A388 should say what the simulation does with it.

### A389, Predictive Value

The three bounds, fidelity, approachability and incentives, the meta of Children of a Dead Earth, EVE Online's agents
as evidence that incentives can be met, the cost of real-life scheduling as a stake, and market demand with its
counter-evidence, Kerbal Space Program 2 and Star Citizen's long alpha.

Items the A386 hardening passes deferred to this article:
- **The mapping literature.** Castronova et al. 2009, Williams 2010 and Barnett et al. 2006 were read in full. Clement
  1982 and Lofgren and Fefferman 2007 were read as abstracts only, and A386 says so. Castronova 2006, *On the Research
  Value of Large Games*, doi 10.1177/1555412006286686, was verified and not cited.
- **Ability average for a station.** The pilot's claim, clarified 2026-11-13, is that participants are average for
  their station, as are the people who hold the real stations. A386 supports it with the Newport record, Green and
  Armstrong 2007 and Armstrong 2001. The primary studies, Green 2002 and Green 2005 in the International Journal of
  Forecasting, were not obtained. A389 should read them.
- **Herman, Frost and Kurz 2009**, *Wargaming for Leaders*, which the pilot read for a class on wargaming. A386 cites
  it from its catalogue record. The pilot has no access to the book for now and ruled on 2026-11-13 to make do. A389
  should cite it properly once the pilot has the book again. The article does not mention the class, and need not.
- **The profession's caution.** Rubel 2006 and Caffrey 2019 say plainly that wargames do not predict. A386 quotes
  both and states the narrower claim. Downes-Martin 2014, on stakeholders who corrupt a game from inside, was found
  and not cited. It is the counterpoint to getting stakeholders to take part.
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
- **The blueprint's principles** are five: omit and never contradict, size fidelity per subsystem, make the physics
  approachable and not soft, make loss last, and be open to checking. The pilot approved the last two, the preference
  for true scale, the preference for the lowest tolerable compression and the crew as the unit that flies a ship, on
  2026-11-13.
- **The mechanism of predictive value**, pilot 2026-11-13. A sufficiently high-fidelity multi-agent simulation should
  have significant predictive value because its agents are subject to the same incentives and constraints as reality.
  That hinges on a scenario close enough to real prospective problems. Competence matters less, since real
  stakeholders are of ordinary ability and make mistakes. The two practical problems are getting the stakeholders who
  would most benefit to take part, and not reflexively waving away unexpected results as unrealistic.
- **Gravity can be optimised**, pilot 2026-11-13. Bodies on ephemerides, craft and small objects bound to parent
  bodies, and shards by parent body. Details such as a flyby's exchange with the parent body need not be modelled.
- **Relativistic time dilation** is what the pilot meant by time dilation. It is nominally relevant to conclusions
  about colonisation, exploration and exploitation.
- **Ability.** Participants in wargames are of average ability for their station, and so are the people who hold the
  real stations simulated. Brilliant people are few, and that matters little, because circumstance and station drive
  a great many decisions. An agent needs only enough competence to do something reasonable, and a competent person of
  less than average ability asks for advice. Pilot, 2026-11-13.
- **Scenarios.** A large part of the thesis is that predictive value is largely a function of being able to formulate
  realistic scenarios that agents are willing to take part in exploring. Pilot, 2026-11-13.
- **Time.** Travel in real time is not a new idea, and the pilot has heard of running the tabletop role-playing game
  Traveller that way. Attending to real life is an alternative to several characters. A long voyage begun before an
  absence is an escape valve, and it models individuals who travel far for private reasons. Relativistic time dilation
  is chiefly a concern of interstellar travel. Pilot, 2026-11-13.
- **The lost sources.** The books the paper drew on are on a shelf the pilot cannot reach, the notes went with the
  paper, and some of the detailed articles it cited are forgotten. The article says so and cites none of them. A
  remark the pilot overheard, such as Traveller run in real time, is stated as overheard and is not cited. Pilot,
  2026-11-13.
- **Voice.** Academic third person and the active voice unless inappropriate. Prefer multi-agent to multiplayer,
  keeping proper names and quoted labels. Length is not an issue. Hardening references and equations is desired.
- **First-hand observation.** The pilot has seen EVE Online's ships slow to rest, and recalls noting that Star
  Citizen's celestial bodies were not subject to celestial mechanics.
- **Nothing is published, pushed or forward-dated** without the pilot's approval.

## Research Material

Gitignored scratch under `tmp/a386/`. `research/ksp_code/`, `research/eve_sc/`, `research/eve_econ/`,
`research/scifi/`, `research/stronger/` and `research/harden/` to `research/harden4/` hold the saved pages and the
research reports, with quotations checked verbatim. `research/harden2/REPORT_A.md` covers wargaming, forecasting and
the full texts of five studies, and `research/harden3/REPORT_B.md` covers the blueprint's engineering claims. Each
folder has a `quotes.tsv` and a checker. The hardening edits are `tmp/a386/fable1.py` to `fable6.py`, each of which
fails unless every replacement matches once, and the draft before them is `tmp/a386/draft_before_fable.markdown`.
`tmp/a386/passive.py` lists passive constructions and first or second person in a post.

## Open Before A386 Publishes

The seven passes the pilot ordered on 2026-11-13 are done: thesis hardening, equation density, reference density,
publication readiness, pathological language usage, the import into the source database and the full URL check. The
editorial date is 2026-11-12, and the front matter carries it.

A reader's pass followed on 2026-11-13 at the pilot's request, so that the article is nominally ready before the
pilot's proofreading. It applied an independent reader's 45 findings on structure and wording, reordered the blueprint
so that Possibility follows The Physical Core, Scenarios follows Predictive Value and the implementation equations come
last, and shortened thesis claims 3 and 5 to the claim with pointers.

1. **The pilot's proofreading, then approval to publish.** Nothing is published, pushed or forward-dated without it.
   Thesis claims 3 and 5 were shortened in the reader's pass, and the removed sentences remain in Possibility and
   Predictive Value. The pilot may restore them to the thesis. The glosses added at first use are the agent's wording,
   and the gloss of soft science fiction, "fiction that puts the story before the physics", needs the pilot's eye.
2. **At publication, rename the article's name map.** `_sources/articles/multi_agent_space_simulation_reconstructed_thesis.json`
   must become `_sources/articles/2026-11-12-multi_agent_space_simulation_reconstructed_thesis.json` in the same commit
   that moves the draft to `_posts/`, or `_verify.py` fails with `sources-drift`. The scratch gate proved both halves.
3. **Design additions awaiting the pilot's word.** The Scenarios subsection, which says that one persistent world is
   one run of one scenario, that worlds can be opened more than once and that a world has a span. It follows from the
   pilot's own statement that predictive value is largely a matter of formulating realistic scenarios.
4. **Two papers cited from abstracts.** Clement 1982 and Lofgren and Fefferman 2007, and the article says so.
5. **One shared record is inconsistent.** `nasa_ideal_rocket_equation`, stored from an earlier article, is filed under
   General Sources, while this article's other NASA Glenn pages are Commercial Sources under the judgement added to
   `_sources/domains.toml` on 2026-11-13. Correcting it means regenerating the published article that cites it.
