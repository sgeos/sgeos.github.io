---
layout: post
mathjax: false
comments: true
title: "Draft Summary"
date: 2000-01-01 00:00:00 +0000
categories: meta
---

<!-- Axxx -->

This post reviews the status of draft posts in this blog's `_drafts/` directory.
Each draft is assessed for topic, completion status, remaining work, and publication sensibility.
Assessments assume that contemporary tooling will be used if salvaged
and that appropriate ecosystem standard choices will replace any tooling that has fallen out of favor.
Missing sections and prose will need to be drafted.
Stubs and largely incomplete drafts are assessed for topicality and publication merit.

## Draft Status

### Research and Development for Search and Rescue Drones — New Draft

**File**: `_drafts/research_and_development_for_search_and_rescue_drones.markdown`
**Topic**: Third article in the SAR drone series after A145 (physics and economics) and A146 (buyer's framework). Treats the research and development side for the smaller audience of academic SAR research groups, federal labs, public-safety agencies with engineering staff, SBIR awardees, and the supporting contractor base. Build-versus-buy frame, federal R&D funding sources, university and federal lab partnerships, the SDK and simulator landscape, custom payload development, regulatory pathways for experimental aircraft, intellectual property in federally funded research, and the technology transition through the valley of death.
**Article Number**: A147
**Completion**: 100%
**Publication Sensibility**: High for the R&D audience; not for the general SAR buyer audience
**Status**: New Draft (101 references; 2,015 lines)

Standalone aerospace, engineering, and program-management analytical article.
Sections covered include
opening as third in the SAR drone series;
The Build-Versus-Buy Frame (three options: build, modify, buy with operational properties that move the program between tiers);
When to Build, When to Modify, When to Buy (custom flight envelope, custom sensor integration, novel autonomous behaviour, multi-aircraft coordination, custom communications);
Federal R&D Funding for SAR Drones (DHS S&T including LRBAA and SBIR and FRRG, SBIR/STTR, NIST PSCR, NIST Standard Test Methods, NASA UAS-NAS, NSF CPS and SCC, DOE national labs including Sandia ORNL INL PNNL, DARPA OFFSET and SubT);
University and Federal Lab Partnerships (the seven FAA UAS Test Sites with the corrected chronology of six in December 2013 plus UAF in early 2014, Raspet, NREC, MIT Lincoln Lab, JHU/APL, NPS CRUSER);
The SDK and Simulator Landscape (DJI Mobile/Onboard/Payload SDKs, Skydio Extend, Parrot Olympe and Open Flight Control, PX4, ArduPilot, ROS 2, PX4 SITL/HITL, AirSim with the full discontinued-and-continued-by-IAMAI lineage, Gazebo, NVIDIA Isaac Sim, MathWorks UAV Toolbox);
Custom Payload Development (Pixhawk/Holybro/mRo autopilot hardware, FLIR Boson Plus and Workswell and Sierra Olympia thermal payloads, LightWare LiDAR, Raspberry Pi and NVIDIA Jetson companion computers, NDAA-compliant component sourcing);
Regulatory Pathways for Experimental Aircraft (Part 107, Section 44807, COA, Special Airworthiness Certificate, Type Certification, Part 108 NPRM);
Intellectual Property in Federally Funded Research (Bayh-Dole, SBIR uniform 20-year data rights regime under May 2019 SBA Policy Directive and DFARS Final Rule January 2025, Stevenson-Wydler and CRADAs, DFARS 252.227-7013/-7014, STTR pre-award allocation);
Technology Transition from Prototype to Operational Use (valley of death, SBIR Phase III sole-source, DHS T2C and CAP, FAA Type Certification, NIST Standard Test Methods as gates, operator demonstrations through DRONERESPONDERS UNITE);
Out of Scope (detailed engineering of custom platforms covered in A112 through A131, international R&D, counter-UAS, manned aircraft integration, commercial-only development);
Conclusion.

Research agent verified
the underlying SDK and platform URLs,
the federal funding programmes,
the university lab and FAA test site URLs,
the regulatory pathway URLs,
and the intellectual property regime documents.
Critical factual corrections applied:
the SBIR data rights regime corrected to the uniform 20-year window under the May 2019 SBA Policy Directive (the pre-2019 4-years-plus-12 regime no longer applies),
the FAA UAS Test Site chronology corrected to six designated December 2013 plus UAF early 2014,
the Nevada UAS Test Site updated to the UNR Nevada Autonomous programme (March 2022 transition),
the University of Maryland UAS Test Site updated to UROC (October 2022 rebrand),
the Naval Postgraduate School lab corrected from the non-existent CAVR to the actual CRUSER,
the AirSim lineage corrected to acknowledge the July 2022 archive, the December 2023 Project AirSim discontinuation, and the IAMAI Simulations continuation,
and the DHS transition vehicles updated from the older Transition to Practice programme to the current Technology Transfer and Commercialization Program plus the Commercialization Accelerator Program.

References:
101 references across Reference (92) and Related Post (9) categories.
All inline-linked per project style.
A145 (physics and economics) and A146 (buyer's framework) cited via post_url as the prior articles in the SAR drone series.
A112 (prototyping), A132 (SBIR intro), A138 (Phase III), A139 (data rights), A141 (after the award), A142 (strategy), and A144 (worked campaign) cited via post_url as the prior SBIR and fixed-wing UAV series articles.

**Remaining Work**:
Human review of build-versus-buy claims and the transition pathway.
Confirm publication date.

### A Buyer's Decision Framework for Search and Rescue Drones — Published

**File**: `_posts/2026-05-16-buyers_decision_framework_for_search_and_rescue_drones.markdown`
**Topic**: Practitioner buyer's decision framework for US-based search and rescue drone procurement in 2026, the actionable companion to A145. Three-branch decision tree on funding source, mission profile, and budget tier. Five budget tiers including a Tier 0 proof-of-concept tier for organizations beginning a program. Worked five-year total cost of ownership. Federal funding source map. Crew complement and Incident Command System integration. Insurance and liability. Buying timeline.
**Article Number**: A146
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-16 (60 references; 1,755 lines)

Standalone aerospace and engineering analytical article on UAV procurement for SAR.
Sections covered include
opening framing as companion to A145;
Branch One, the Funding Source (FAR 52.240-1 effective 22 December 2025, ADSA 2023, NDAA Section 1709 of FY 2025, FCC Covered List actions on DJI and Autel, DCMA Blue UAS list since 3 December 2025, JAG restriction on drone procurement);
Branch Two, the Mission Profile (wilderness, urban, water rescue, alpine, disaster response, payload essentials);
Branch Three, the Budget Tier:
  Tier 0, Evaluation and Proficiency ($300 to $1,500 acquisition; proof-of-concept-through-production framing universal to any new capability; DJI Mini 4 Pro, Autel Nano Plus, BetaFPV Cetus Pro; SDK and simulator references including DJI Mobile SDK, Parrot Olympe, PX4, ArduPilot, AirSim, Gazebo);
  Tier 1, Volunteer ($3,000 to $15,000);
  Tier 2, Small Professional ($15,000 to $60,000);
  Tier 3, Medium Professional ($60,000 to $250,000);
  Tier 4, Large Program or Federal Agency ($250,000 to $2 million plus);
a Worked Five-Year Total Cost of Ownership (Tier 3 example, approximately $430,000 over five years against $200,000 acquisition);
Funding Sources (HSGP with UASI consolidated into SHSP in FY 2025, AFG admissible for drones, SAFER personnel-only, JAG restricted, Operation Stonegarden);
Crew Complement and Incident Command Integration;
Insurance and Liability (FTCA, sovereign immunity, commercial insurance);
the Buying Timeline (6 to 18 months from decision to operational capability);
Out of Scope;
Conclusion.

Research agent verified
the FAR 52.240-1 effective date and citation,
the ADSA 2023 enactment as part of FY 2024 NDAA,
the corrected attribution of Section 1709 to FY 2025 NDAA,
the DCMA Blue UAS list transfer of 3 December 2025,
the JAG restriction on drone procurement per Bureau of Justice Assistance guidance,
the UASI consolidation into SHSP in FY 2025,
the SAFER personnel-only scope,
current 2026 prices for representative platforms,
and the structural gap that no NDAA-compliant prosumer thermal multicopter sells under $10,000 in the US market.
The article incorporates these findings as factual corrections rather than as commentary.

References:
60 references across Reference (58) and Related Post (2) categories.
All inline-linked per project style.
A145 (physics and economics companion) cited via post_url.
A134 (payload and mission systems) cited via post_url.
Forward reference to a future A147 (drone development companion) is plain prose without a post_url tag, to be upgraded after A147 publishes.

### Fixed-Wing, Multicopter, and Hybrid Drones for Search and Rescue, Physics and Economics — Published

**File**: `_posts/2026-05-15-fixed_wing_multicopter_and_hybrid_drones_for_search_and_rescue.markdown`
**Topic**: Comparative analysis of the three drone platform classes (fixed-wing, multicopter, hybrid VTOL) for search and rescue, covering the underlying physics, capital outlay, upkeep costs, and personnel training. The first of a two-part series, with the buyer's decision framework to follow as A146.
**Article Number**: A145
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-15 (57 references; 1,824 lines)

Standalone aerospace and engineering analytical article on UAVs in search and rescue.
Sections covered include
opening problem framing;
the three platform classes (fixed-wing, multicopter, hybrid VTOL with examples);
the physics of fixed-wing flight (lift, drag, lift-to-drag ratio, Reynolds number and the low-Reynolds-number regime, the electric Breguet endurance equation);
the physics of multicopter flight (Rankine and Froude actuator disk theory, hover power, disk loading, figure of merit, forward-flight power minimum, battery endurance);
the physics of hybrid VTOL aircraft (tail-sitter, quad-plane and convertiplane, tilt-rotor and tilt-wing, the cruise efficiency penalty);
performance implications for search and rescue with a scorecard table;
the four-phase SAR use case sequence (wide-area search, target investigation, intervention, sustained coverage);
capital outlay with a price-range table covering multicopter, hybrid VTOL, and fixed-wing classes;
upkeep costs with a per-platform annual cost table covering batteries, propellers, motors, airframe inspection, sensor calibration, ground station, spectrum, insurance, and incident repair;
personnel training (FAA Part 107, manufacturer training, search-and-rescue specific training, recurrency) with a training cost table;
the hybrid compromise with a scorecard table;
Out of Scope (defers detailed regulatory compliance, sensor technology in depth, weather minima and operational envelopes, mission-system architecture, and specific procurement guidance);
conclusion.

MathJax used throughout the physics sections.

Cross-links via post_url to the existing series:
A114 (runway sizing), A116 (launch and recovery), A123 (propulsion and power sizing), A125 (electric energy systems and endurance budget), A134 (payload and mission systems), A135 (regulatory and operations layer), A144 (worked SBIR campaign).

References:
57 references across Reference (50) and Related Post (7) categories.
All inline-linked per project style.
A parallel research agent verified physics references (Wikipedia momentum theory, drag equation, Reynolds number, Breguet, figure of merit, disk loading), platform references (current URLs for ScanEagle, Skylark, Skydio X10, Penguin C as Edge Autonomy), regulatory references (eCFR Part 107 as primary source, FAA public safety page, EASA), training references (DJI Academy, Skydio Academy, AOPA), and SAR-specific references (DRONERESPONDERS, NASAR).
Vendor URLs returning 403 to curl are documented bot-detection patterns, valid for human readers.
No internal research cited.

### A Worked SBIR and STTR Campaign for a Fixed-Wing UAV — Published

**File**: `_posts/2026-06-27-worked_sbir_and_sttr_campaign_for_a_fixed_wing_uav.markdown`
**Topic**: A single constructed company, the running fixed-wing unmanned aircraft firm, followed through a whole SBIR and STTR campaign from feasibility to prototype to market, synthesizing the entire series; the thirteenth and final article of the SBIR/STTR practitioner-playbook series, the worked-campaign capstone.
**Article Number**: A144
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-27 (19 references)

Standalone article and the thirteenth and final article of the SBIR/STTR practitioner-playbook series, the worked-campaign capstone that closes it.
Framed on the organizing idea of the whole series, that the programs supply non-dilutive capital in stages against demonstrated risk reduction, a staircase from feasibility to prototype to market, walked once in full by one company that uses each award to buy the next rung.
Sections covered include
the company and the airframe (the dual-use fixed-wing unmanned aircraft of the running case);
deciding to pursue (orientation and the agency choice);
getting ready (eligibility and registration, the STTR route chosen);
finding the topic and winning Phase I (the feasibility proposal);
Phase II and the prototype (the commercialization plan, the research partner performing its share under the STTR split);
the money, the rights, and the compliance (the indirect rate and the cash gap, the Phase-I-to-Phase-II funding gap, data-rights marking and the company-and-partner intellectual-property allocation, reporting and audits);
the valley of death and Phase III (the transition partner and the sole-source follow-on);
the strategy over time (the portfolio, the state match, the private-capital bridge, the international option);
where it could go wrong (the same campaign in reverse as a catalog of the failures the series warned against);
and an Out of Scope section.
The company is explicitly a constructed illustration rather than a real firm.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links every prior article of the series via post_url (A132 the introduction, A133 the agencies, A134 eligibility, A135 the topic and solicitation, A136 Phase I, A137 Phase II, A138 Phase III, A139 data rights, A140 the money, A141 after the award, A142 strategy, and A143 international analogs) plus A112 (the running-case unmanned aircraft).
19 references across Reference (4), Related Post (13), and Research (2) categories.
With A144 the SBIR/STTR practitioner-playbook series is complete, all thirteen of thirteen articles published.

### International Analogs to SBIR and STTR — Published

**File**: `_posts/2026-06-26-international_analogs_to_sbir_and_sttr.markdown`
**Topic**: A survey of the foreign equivalents to the United States SBIR and STTR programs, organized by the structural axes along which they differ (procurement versus grant versus tax credit versus equity; non-dilutive versus dilutive; challenge-driven versus open; phased versus single-shot); the twelfth article and the single dedicated international article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A143
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-26 (20 references)

Standalone article and the twelfth of the SBIR/STTR practitioner-playbook series, the one dedicated international article.
Framed on the idea that every advanced economy faces the same market failure in early-stage high-risk technology and each has built a public instrument to fund the risk reduction private capital will not, so the analogs are different answers to one shared question rather than copies of a single design.
Sections covered include
the common problem (the market failure, the valley of death, industrial policy);
the procurement copies (the United Kingdom Contracts for Innovation, formerly the Small Business Research Initiative; the Netherlands SBIR, now the Innovation Impact Challenge; Australia's Business Research and Innovation Initiative; Canada's Innovative Solutions Canada; Japan's 2021-reformed SBIR under the Cabinet Office);
the European grant programs (Horizon Europe, the European Innovation Council Accelerator, the Eureka network and Eurostars, Germany's Central Innovation Programme for the Mittelstand);
the research-collaboration analog (the STTR dimension, the consortium model as the default abroad, South Korea's move to add an STTR-style program);
the tax-credit instrument (Canada's Scientific Research and Experimental Development credit);
the state as investor (the Israel Innovation Authority's royalty-bearing grants, the European Accelerator's blended grant-plus-equity, South Korea's Tech Incubator Program for Startups);
defense and dual-use (the North Atlantic Treaty Organization's DIANA);
the axes of difference (a 13-program comparison table and where the United States program sits);
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
All foreign-program facts were verified by web search and flagged current-as-of, with each country's own program authority named as the only reliable source.
Cross-links A132 (the introduction), A134 (eligibility and the STTR distinction), A138 (the valley of death), A140 (the money, non-dilutive), A142 (strategy and the portfolio), and A112 (the running-case company) via post_url; the worked-campaign capstone is referenced in prose pending A144.
20 references across Reference (11), Related Post (6), and Research (3) categories.

### Strategy and the Portfolio of SBIR and STTR Awards — Published

**File**: `_posts/2026-06-25-strategy_and_the_portfolio_of_sbir_and_sttr_awards.markdown`
**Topic**: The strategic view above the single award, the portfolio, transition versus the mill, stacking non-dilutive capital, the private-capital bridge, dual-use markets, and the discipline of choosing what to pursue; the eleventh article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A142
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-25 (20 references)

Standalone article and the eleventh of the SBIR/STTR practitioner-playbook series.
Framed on the idea that an award is a means and not an end, and that strategy is the discipline of using a portfolio of non-dilutive awards, staged against the risk reduction the whole series has tracked, to build a company that eventually no longer needs them, with the central choice between transition and the mill.
Sections covered include
the award is a means (the strategic frame);
transition versus the mill (the central choice, the transition partner who pulls a technology across the valley of death, the sole-source Phase III as a positioned-for asset);
the portfolio (diversification across agencies, topics, and customers, sequencing, parallel tracks, the proactive pipeline);
stacking the capital (state matching funds, the assistance programs, layering non-dilutive sources);
the private-capital bridge (venture capital, angels, seed, equity dilution, the majority-investor eligibility wrinkle, de-risking the technology for investors);
the market beyond the government (dual-use, commercialization, the National Science Foundation seed fund);
choosing what to pursue (opportunity cost, the distorting award);
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A134 (eligibility and the investor exception), A135 (the topic and solicitation), A137 (the commercialization plan), A138 (the valley of death), A140 (the money), and A112 (the running-case company) via post_url; the international-analogs article is referenced in prose pending A143.
20 references across Reference (11), Related Post (6), and Research (3) categories.

### After the Award, Compliance and Reporting for SBIR and STTR — Published

**File**: `_posts/2026-06-24-after_the_award_for_sbir_and_sttr.markdown`
**Topic**: The continuing obligations of holding an award, performing the work, reporting, invoicing, surviving audits, staying in good standing, and closing out, the second half of the campaign where past performance is built or destroyed; the tenth article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A141
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-24 (19 references)

Standalone article and the tenth of the SBIR/STTR practitioner-playbook series.
Framed on the idea that an award is a binding agreement with continuing duties and that winning is the start of an obligation rather than the end of an effort.
Sections covered include
winning is the start (the award binds, contract or grant);
performing and who to talk to (milestones and deliverables, the contracting officer versus the technical point of contact, formal modifications, no-cost extensions, termination, subcontractor and partner management);
reporting (technical progress and final reports, the commercialization report that feeds the benchmarks, the late-report consequences);
invoicing and getting paid (the payment systems, the lag);
audits and the settling of rates (the Defense Contract Audit Agency, the incurred-cost true-up, the single audit, the audit trail and records retention);
compliance and integrity (the certifications, the False Claims Act, debarment, the defense cybersecurity obligation);
closing out;
continuing standing (registrations, accounting, benchmarks, past performance);
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A134 (eligibility), A136 (the Phase I proposal), A139 (data rights), A140 (the money), and A112 (the running-case company) via post_url; the strategy article is referenced in prose pending A142.
19 references across Reference (11), Related Post (5), and Research (3) categories.

### The Money Behind an SBIR or STTR Award — Published

**File**: `_posts/2026-06-23-money_behind_an_sbir_or_sttr_award.markdown`
**Topic**: The cost proposal, direct and indirect costs, the indirect rate, compliant accounting, and the cash flow that decide whether a company that won an award can survive it; the ninth article of the SBIR/STTR practitioner-playbook series, the one with arithmetic.
**Article Number**: A140
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-23 (18 references)

Standalone article and the ninth of the SBIR/STTR practitioner-playbook series, the one with arithmetic.
Framed on the idea that the award is a fixed pot and the company must justify it in a compliant budget, account for it in a way the government accepts, and finance the gap between spending it and being paid.
Sections covered include
the cost proposal (justify every dollar, fit the cap, match the work plan, evaluated for reasonableness, the agency budget format);
direct and indirect costs (the fringe, overhead, and general-and-administrative pools, equipment title);
the indirect rate (rate equals the indirect pool over an allocation base, the loaded-cost chain, provisional versus negotiated rates, the true-up risk);
fee and the two contract types (cost-reimbursement with a fee, fixed-price, grants without fee, no cost share);
compliant accounting (segregation, timekeeping, the Defense Contract Audit Agency, proportionate standards);
allowable and unallowable costs (the cost principles);
cash flow, the quiet killer (the lag and the gap, burn rate and runway, outside financing and the line of credit and factoring);
a note on assistance funds;
common money mistakes;
scale and the UAV case;
and an Out of Scope section.
mathjax true, with the indirect-rate and loaded-cost relations, the one article in the series with arithmetic.
No runnable code, so no Software Versions section.
Cross-links A136 (the Phase I proposal), A137 (Phase II), A138 (Phase III), and A112 (the running-case company) via post_url; the compliance and strategy articles are referenced in prose pending A141 and A142.
18 references across Reference (11), Related Post (4), and Research (3) categories.

### Data Rights and Intellectual Property in SBIR and STTR — Published

**File**: `_posts/2026-06-22-data_rights_and_intellectual_property_for_sbir_and_sttr.markdown`
**Topic**: The intellectual property a company keeps under the programs, patents under Bayh-Dole and the special SBIR data rights, the crown jewel that the non-dilutive funding was meant to build and that marking preserves; the eighth article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A139
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-22 (16 references)

Standalone article and the eighth of the SBIR/STTR practitioner-playbook series, its crown-jewel article.
Framed on the idea that the government funds the work but the company keeps the inventions and the technical data, so the program is non-dilutive in intellectual property as well as equity, and the retained ownership is the asset the funding was meant to build, kept only by guarding it.
Sections covered include
two bodies of rights (patents versus data rights, and the STTR allocation with the research institution);
patent rights under Bayh-Dole (the company elects title, the election clock, march-in rights, the United-States-manufacturing preference);
SBIR data rights (the protected license, the protection period historically four years and since lengthened, background versus foreground);
marking is the act that preserves the rights (unmarked data risks unlimited rights, markings must conform, assertions can be challenged);
the categories of rights (unlimited, government-purpose, limited and restricted, the special SBIR category);
what the government keeps and what the company keeps;
threats to the crown jewel (subcontracts, omissions, expiry, over-delivery, mixed funding, open-source code);
how the rights create value (the sole-source position, the asset in a sale);
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A132 (orientation), A134 (eligibility), A136 (the Phase I proposal), A138 (Phase III), and A112 (the running-case company) via post_url; the money, compliance, and strategy articles are referenced in prose pending A140, A141, and A142.
16 references across Reference (9), Related Post (5), and Research (2) categories.

### Phase III and the Valley of Death for SBIR and STTR — Published

**File**: `_posts/2026-06-21-phase_iii_and_the_valley_of_death_for_sbir_and_sttr.markdown`
**Topic**: Phase III, the commercialization step that carries no SBIR funds, and the valley of death between a funded prototype and a self-sustaining product or fielded program, with the sole-source authority and the data rights as the tools for crossing it; the seventh article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A138
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-21 (19 references)

Standalone article and the seventh of the SBIR/STTR practitioner-playbook series.
Framed on the idea that Phase III is a destination rather than an award, since it carries no program money, so the company must cross the valley of death from a funded prototype to a self-sustaining product or fielded program on other money.
Sections covered include
what Phase III is (no set-aside money, no dollar or time limit, the high technology-readiness rungs, the concrete funding sources, not strictly sequential);
the sole-source authority (the broad, non-expiring procurement lever, permission to buy and not a commitment);
the valley of death (the gap and why technologies die in it);
crossing by government transition (the program of record, the transition partner, the budget line, the acquisition pull, the prime-contractor path and its risk, the CRADA and the readiness program);
crossing by the market (the product, the customers, the venture capital, the Food and Drug Administration path, SBIR as an investor credential);
why Phase III is the point (the benchmarks measure it, the mill is the failure to reach it);
common ways to fall in;
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A132 (orientation), A134 (eligibility), A137 (Phase II), and A112 (the running-case company) via post_url; the data-rights, money, and strategy articles are referenced in prose pending A139, A140, and A142.
19 references across Reference (11), Related Post (4), and Research (4) categories.

### Phase II and the Commercialization Plan for SBIR and STTR — Published

**File**: `_posts/2026-06-20-phase_ii_and_the_commercialization_plan_for_sbir_and_sttr.markdown`
**Topic**: The Phase II development award and the commercialization plan that becomes a first-class scored deliverable, the step where a funded research result becomes a business or remains a research result; the sixth article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A137
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-20 (20 references)

Standalone article and the sixth of the SBIR/STTR practitioner-playbook series.
Framed on the idea that Phase II is the step where the program stops asking whether the idea can work and starts asking whether it can become a product, so the money grows by an order of magnitude, the work turns from feasibility to development, and the commercialization plan becomes a scored deliverable.
Sections covered include
what Phase II builds (a prototype, the middle technology-readiness rungs, the base-and-option structure, the intellectual property);
the gate from Phase I (the sequence, the funding gap, Direct to Phase II, selection is not award);
the Phase II proposal (the shift of weight to commercialization, the work-split limit);
the commercialization plan as a deliverable (a business plan, the market analysis, the value proposition, the competition, the go-to-market strategy, product-market fit, documented commitments such as a memorandum of understanding, and the reporting that feeds the eligibility benchmarks);
transition versus market commercialization (the two agency cultures);
extending Phase II and bridging toward Phase III (the enhancement, the sequential Phase II, the commercialization readiness program);
the funding gap and cash flow;
common ways to lose Phase II;
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A132 (orientation), A133 (agency survey), A134 (eligibility), A136 (the Phase I proposal), and A112 (the running-case company) via post_url; Phase III and the money article are referenced in prose pending A138 and A140.
20 references across Reference (11), Related Post (5), and Research (4) categories.

### Writing the Phase I SBIR and STTR Proposal — Published

**File**: `_posts/2026-06-19-writing_the_phase_i_proposal_for_sbir_and_sttr.markdown`
**Topic**: Writing the Phase I proposal as an argument that the company can retire an idea's feasibility risk, written to the evaluation criteria, by a credible team, with a commercial promise; the proposal-craft core of the SBIR/STTR practitioner-playbook series.
**Article Number**: A136
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-19 (20 references)

Standalone article and the fifth of the SBIR/STTR practitioner-playbook series, its proposal-craft core.
Framed on the idea that a Phase I proposal is an argument that the company can retire the feasibility risk of an idea, written to the published evaluation criteria, by a believable team, with a commercial promise.
Sections covered include
what Phase I actually asks (feasibility and proof of concept, not a product, the overpromise as the classic failure, the technology-readiness staircase);
the volumes and their shape (the technical and cost volumes telling the same story, the project summary and public abstract, the proprietary markings, the page-limit boundary);
the sections of the technical volume;
the three things a reviewer scores (technical merit, qualifications, commercialization potential);
writing the innovation (the feasibility question, the technical risk to retire, plain technical writing);
the work plan (the work breakdown, milestones, deliverables, risk and mitigation, fitting the envelope, and setting up Phase II with go-or-no-go criteria);
the team and the past performance (the principal investigator and the work-split limits, the STTR partner);
the commercialization story (scored even in Phase I, dual-use, the customer letter);
writing to the reviewer (peer review at science agencies, government technical evaluation at directed agencies, clarity for a busy reader, the internal red-team review);
review, debrief, and resubmission (most proposals lose, the debrief is the prize, resubmit);
common ways to lose;
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A132 (orientation), A134 (eligibility), A135 (solicitation), and A112 (the running-case company) via post_url; Phase II is referenced in prose pending A137.
20 references across Reference (12), Related Post (4), and Research (4) categories.

### Finding a Topic and Reading an SBIR or STTR Solicitation — Published

**File**: `_posts/2026-06-18-finding_a_topic_and_reading_a_solicitation_for_sbir_and_sttr.markdown`
**Topic**: Finding the topic or funding opportunity that matches a company's capability and reading the solicitation precisely, the bridge between eligibility and the proposal; the fourth article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A135
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-18 (16 references)

Standalone article and the fourth of the SBIR/STTR practitioner-playbook series.
Framed on the two tasks of the stage, finding the opportunity (a matching topic at a directed agency, fit within a broad area at an open one) and reading the solicitation as the contract for the competition.
Sections covered include
two kinds of looking;
where the opportunities live (the cross-agency portal, the agency systems, the calendar);
the anatomy of a solicitation, including tracking its amendments;
reading a topic (the objective, deliverables, target technology readiness level, the dual-use expectation, the keywords, and the customer-pull letters to begin lining up);
the pre-release window and talking to the agency (the directed-agency topic-author contact and the blackout versus the open-agency program-officer culture);
is it a fit and is it winnable (past-award intelligence from the searchable awards record, and the teaming and STTR-partner commitment);
reading for compliance (the cheapest loss, with the cost ceiling and period scoping the work);
writing to the evaluation criteria;
the open-agency path (the NSF project pitch, the NIH institute and funding opportunity);
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A132 (orientation), A133 (agency survey), A134 (eligibility), and A112 (the running-case company) via post_url.
16 references across Reference (8), Related Post (4), and Research (4) categories.

### SBIR and STTR Eligibility and the Registration Stack — Published

**File**: `_posts/2026-06-17-eligibility_and_the_registration_stack_for_sbir_and_sttr.markdown`
**Topic**: The two gates an applicant clears before any SBIR or STTR proposal, eligibility (what the company must be) and registration (getting it into the federal systems), with the registrations' lead time gating the calendar; the third article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A134
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-17 (21 references)

Standalone article and the third of the SBIR/STTR practitioner-playbook series.
Framed on the two gates before a proposal, eligibility as a property of the company true or false on the day it applies, and registration as a multi-week sequence of accounts and identifiers whose lead time gates the calendar.
Sections covered include
eligibility, what the company must be (small with affiliation, for-profit, United States, the five-hundred-employee standard versus the industry-code standards, not a socioeconomic set-aside);
the ownership rules and the investor exception (more than half owned by United States individuals or small businesses, the venture, private-equity, and hedge-fund majority-ownership exception that is agency-specific);
the principal investigator and the work (the SBIR primary-employment requirement, the STTR flexibility, the work splits, the United States place of performance);
the performance benchmarks and the duplicate-funding and essentially-equivalent-work rule;
national-security eligibility (the 2026 screening), the export-control neighbor, and the certification-and-fraud framing (False Claims Act exposure);
the registration stack in order (Login.gov, the System for Award Management with the unique entity identifier and CAGE code, the program company registry and its control identifier, the agency portal);
why the stack gates the calendar (validation can take weeks, annual renewal, the registration-is-free warning);
scale and the small-company case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A132 (orientation), A133 (agency survey), and A112 (the running-case company) via post_url.
21 references across Reference (13), Related Post (3), and Research (5, the live federal systems) categories.

### A Survey of the SBIR and STTR Agencies — Published

**File**: `_posts/2026-06-16-survey_of_the_sbir_and_sttr_agencies.markdown`
**Topic**: A survey of the eleven SBIR and five STTR agencies for the practitioner choosing where to apply, organized on two axes (grant versus contract, directed versus open topics); the second article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A133
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-16 (25 references)

Standalone article and the second of the SBIR/STTR practitioner-playbook series, in the business/funding/sbir category.
Organized on two independent axes, the award vehicle (grant or cooperative agreement versus procurement contract) and the topic (directed versus open), with the agencies populating the corners.
Sections covered include
the two axes and where the agencies sit;
how many agencies and why the sizes differ (eleven SBIR, five STTR, the set-aside making budget proportional to extramural research);
the Department of Defense (contract, directed, the components and the Defense SBIR/STTR Innovation Portal, transition, dual-use, the national-security screening);
the National Institutes of Health (grant, open, standing receipt dates);
the National Science Foundation (grant, broad, America's Seed Fund, the required project pitch);
the Department of Energy (grant but directed, the national-lab STTR fit);
NASA (contract, directed, transition to a NASA mission);
the smaller agencies (Agriculture, Homeland Security, Commerce with NOAA and NIST, Education, Transportation, Environmental Protection);
a comparison table (vehicle, topics, STTR, Direct to Phase II, relative size, character);
choosing where to apply (match by mission and by model, eligibility varying by agency, the cadence as a selection factor, differing post-award support);
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Balanced across agencies per the series plan, with all time-sensitive specifics flagged as current-as-of.
Cross-links A132 (the orientation), A93 (mission-critical engineering, the Department of Defense culture), and A112 (the UAV as a dual-use example) via post_url.
25 references across Reference (16), Related Post (3), and Research (6, one authoritative portal per major agency) categories.

### An Introduction to the SBIR and STTR Programs — Published

**File**: `_posts/2026-06-15-introduction_to_the_sbir_and_sttr_programs.markdown`
**Topic**: Orientation to the United States SBIR and STTR programs, framed on non-dilutive capital staged against demonstrated risk reduction mapped to the technology readiness level; the first article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A132
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-15 (18 references)

Standalone article and the first of a new series, the SBIR/STTR practitioner playbook, in a new category cluster (business/funding/sbir, permalink /business/funding/sbir/).
The master variable is non-dilutive capital staged against demonstrated reduction of risk, the three-phase staircase mapped to the technology readiness level.
Sections covered include
a program that runs on reauthorization (the 2025 lapse and the 2026 reauthorization through fiscal year 2031);
the core idea (non-dilutive, mission-pulled, the set-aside, the scale of over four billion dollars a year across roughly four thousand awards, America's Seed Fund);
the three phases (Phase I feasibility, Phase II development, Phase III commercialization with no SBIR funds and sole-source authority) with the technology-readiness-level mapping and the multi-year timeline;
SBIR versus STTR (the research-institution partner and the work splits);
who can compete (the eligibility gate and the 2026 national-security screening);
why the money is worth the trouble (non-dilutive, data rights, the valley of death);
what the programs are not (the grant-versus-contract distinction, not free money, not a substitute for a customer);
the series ahead;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Explicitly United States, with the international analogs deferred to a later article, and all time-sensitive figures flagged as current-as-of with the live solicitation and the SBA policy directive named as authoritative.
Cross-links A93 (mission-critical engineering), A112 (prototyping the UAV, the running case), and A131 (the risk-based regulatory framing) via post_url.
18 references across Reference (12), Related Post (3), and Research (3) categories.

### The Regulatory and Operations Layer for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-14-regulatory_and_operations_layer_for_fixed_wing_uavs.markdown`
**Topic**: The regulatory and operations layer above the engineering of a fixed-wing UAV, framed jurisdiction-neutrally on the principle that the authorization to operate is granted in proportion to demonstrated risk control, with kinetic energy as the physical proxy for harm; the sixth and final flagged extension.
**Article Number**: A131
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-14 (41 references)

Standalone aerospace article and the sixth and final flagged extension beyond the core fixed-wing-UAV arc, the layer above the engineering, with which the series and its extensions are now complete.
The master variable is the authorization to operate, granted in proportion to the risk an operation poses and the control the operator can demonstrate, with the impact kinetic energy E_k = (1/2) m v^2 as the physical proxy for harm tying the regulatory categories to the mass and speed the series worked in.
Explicitly jurisdiction-neutral, framed on the International Civil Aviation Organization and the Chicago Convention with the FAA, the European Union Aviation Safety Agency, the UK Civil Aviation Authority, the Civil Aviation Safety Authority, Transport Canada, and the Civil Aviation Administration of China named as examples, the thresholds presented as patterns that differ by state and change over time.
Sections covered include
regulation is jurisdictional;
authorization proportionate to risk (the open, specific, and certified pattern, ground risk and air risk, the specific operations risk assessment);
kinetic energy as the measure of harm;
the axes of risk (mass, line of sight, over people, altitude, airspace);
registration, identification, and competency with the autonomy-and-responsibility tension;
airworthiness and the certified end;
integrating with other traffic (segregated versus integrated, unmanned traffic management and U-space, detect and avoid, command-and-control reliability);
the operations layer (concept of operations, crew, pre-flight planning, maintenance, training, the safety management system, just culture, independent accident investigation);
contingency and containment (defined procedures, the geofence, flight termination, and command-link security as a regulatory concern);
adjacent regimes (spectrum and the telecommunication union, export control, privacy and data protection, property rights, insurance, and noise);
the boundary with space (the suborbital handoff to space law, the Outer Space Treaty, the Kármán line as a convention);
scale and the UAV case;
and an Out of Scope section.
MathJax for the kinetic-energy relation.
No runnable code, so no Software Versions section.
The pilot's instruction that not everyone is in the USA is honored throughout, the article naming authorities from several continents, framing the specifics as patterns that vary and change, directing the reader to the governing authority, and drawing its three Research sources from the international bodies (the International Civil Aviation Organization, the European Union Aviation Safety Agency, and the Joint Authorities for Rulemaking on Unmanned Systems for the risk assessment).
References A112, A125, A126, A127, and A130 via post_url.
41 references across Reference (33), Related Post (5), and Research (3) categories.

### Payload and Mission Systems for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-13-payload_and_mission_systems_for_fixed_wing_uavs.markdown`
**Topic**: The payload and mission system of a fixed-wing UAV, framed on the payload fraction and the share of the mass, power, volume, data, and energy budget that reaches the payload, including suborbital spaceplane payload delivery with payload-owned circularization.
**Article Number**: A130
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-13 (45 references)

Standalone aerospace article and the fifth extension beyond the core fixed-wing-UAV arc.
The master variable is the payload fraction and, more broadly, the share of the budgets the series tracked that reaches the payload rather than carrying it, the payload being the point and the platform the overhead.
Sections covered include
the payload fraction (size, weight, power, and cost);
a taxonomy of payloads (electro-optical and infrared, synthetic-aperture radar, signals intelligence, lidar, multispectral and hyperspectral, communications relay, delivery and agricultural, the loitering-munition effector, scientific);
integrating the payload with the platform (mass and center of gravity, power as hotel load with the peak-versus-average note, data with onboard storage and compression, heat, volume, vibration and isolation);
pointing and stabilization with the geolocation and target-location-error chain;
the mission system (tasking, edge versus downlink processing, sensor fusion, autonomy);
the payload sizes the aircraft with the aperture-sets-resolution physics (angular resolution and ground sample distance tying SWaP to standoff performance);
releasing and dropping payloads;
suborbital spaceplane payload delivery (the reusable carrier delivers an accurate release state near apogee and the payload owns circularization, Dv = v_circ - v_h);
scale and the UAV case (modular bays and interface standards, the loitering munition as payload-is-the-aircraft);
a worked example (a 20 percent payload fraction on the 25 kg aircraft, and the ~7.8 km/s circular speed at a 200 km apogee with the honest delta-v split);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
The pilot's explicit inclusion, suborbital spaceplane payload delivery where orbital circularization around apogee is the payload's responsibility, is covered in its own section, with the orbital mechanics after release held out of scope except for the handoff delta-v.
References A120, A121, A125, A126, A127, and A128 via post_url.
45 references across Reference (37), Related Post (6), and Research (2) categories.

### An Aerobatic Maneuver Reference Catalog for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-12-aerobatic_maneuver_reference_catalog_for_fixed_wing_uavs.markdown`
**Topic**: A reference catalog of 79 named aerobatic maneuvers, each classified in the A128 costed-trajectory model, alphabetical with stable family-prefixed IDs; the reference companion to A128.
**Article Number**: A129
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-12 (32 references; 79 catalog rows)

Standalone aerospace reference article and the fourth extension beyond the core fixed-wing-UAV arc, the reference companion to the A128 model.
Written for the UAV operator and the autonomy, not the human pilot.
A 79-row alphabetical catalog with a stable family-prefixed identifier per maneuver across twelve families (lines, turns, rolls, loops and eights, partial loops and combinations, stall turns, tailslides, spins, post-stall and supermaneuvers, three-dimensional and prop-hang figures, basic fighter maneuvers, composite or display).
Columns are the identifier, the maneuver, the family, the spatiotemporal path, the energy-height behavior, the peak load class, and the regime ceiling with flags.
Maneuver definitions are cited to the Aresti catalog, the world air sports federation, the International Aerobatic Club, the basic-fighter-maneuver repertoire, and Wikipedia where an article exists.
The cost classification is forward-declared as an original, qualitative synthesis with three stated limitations, since no catalog tabulates the energy-height behavior, the load class, and the regime ceiling per maneuver.
Sections covered include
how to read the table;
why the thermal cost is folded into the regime column;
provenance and limitations;
the catalog;
maneuvers without a closed form (spins, snaps, the cobra, the Kulbit, the Herbst maneuver, the gyroscopic tumbles, and the three-dimensional and prop-hang figures, with what can still be said);
parametric families;
alternate names;
using the catalog;
reading a row in numbers (the break turn read into the corner-speed and load figures of the structures and model articles);
Out of Scope;
and a conclusion.
MathJax enabled for the model symbols.
No runnable code, so no Software Versions section.
The honesty of the catalog rests on a clear division, the maneuver definitions sourced to the established catalogs and the cost classification offered as an original synthesis to be checked rather than as measured data.
References A120, A123, A125, A127, and A128 via post_url.
32 references across Book (1), Reference (26), and Related Post (5) categories.

### Aerobatics as Costed Trajectories for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-11-aerobatics_as_costed_trajectories_for_fixed_wing_uavs.markdown`
**Topic**: UAV aerobatics treated as commanded spatiotemporal trajectories priced in energetic, structural, and thermal cost across the subsonic, supersonic, and hypersonic regimes, with a hypothetical spaceplane reentry case; the synthesis capstone of the extension set.
**Article Number**: A128
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-11 (42 references)

Standalone aerospace article and the third extension beyond the core fixed-wing-UAV arc (after A126 communications and A127 structures), the synthesis capstone of the extension set.
Written for the UAV operator and the autonomy and explicitly not for the human pilot, treating a maneuver as a commanded spatiotemporal trajectory rather than a learned skill.
The master variable is the energy state and the specific excess power Ps = V(T - D)/W = dh_e/dt, with every maneuver a transaction in potential, kinetic, and propulsive energy and three costs (energetic, structural, thermal) whose dominant term migrates with the speed regime.
Sections covered include
a maneuver as a trajectory;
the energy state and specific excess power (energy height h_e = h + V^2/2g, energy-maneuverability theory);
the three costs and the control-authority-and-bandwidth feasibility gate;
the kinematic primitives and the maneuverability (doghouse) diagram with its lift, structural, and sustained bounds;
a scored catalogue table of ten maneuvers (path, peak load, energy-height behavior, highest surviving regime, with the post-stall spin and cobra flagged as no-closed-form);
the footprint in space and time (airspace volume, time, wind drift, deconfliction);
the subsonic regime (figure flying, the no-human-ceiling advantage, negative-g and outside figures);
the transonic and supersonic regimes (wave drag, Ps collapse, Mach tuck, the shrinking catalogue);
the hypersonic regime (stagnation heating dominant, bank-angle modulation and S-turns, boost-glide and HGV referents);
spaceplane maneuvering during reentry (the corridor, bank reversals and angle of attack, the Shuttle's forty-degree alpha and cross-range, control authority migrating from RCS to surfaces per A122);
spaceplane maneuvering after the thermal wall (terminal-area energy management, tying A124 and A125);
scale and the UAV case (favorable structural scaling, the loitering-munition terminal maneuver, the energy and powertrain-thermal bounds);
a worked example on the 25 kg series aircraft (level turn radius and rate, the corner turn, a loop sized by the energy-height trade, a Mach-five thermal note);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout, honest where no closed form exists.
No runnable code, so no Software Versions section.
The term aerobatics is extended to commanded maneuvering, with an explicit lampshade that figure flying does not survive the hypersonic and reentry regimes.
References A120, A122, A123, A124, A125, and A127 via post_url.
42 references across Book (1), Reference (33), Related Post (6), and Research (2) categories.

### Structures and the Flight Envelope for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-10-structures_and_the_flight_envelope_for_fixed_wing_uavs.markdown`
**Topic**: The airframe structure and the flight envelope of a fixed-wing UAV, framed on the load factor and the load-versus-speed (V-n) diagram, the boundary the whole series operates inside; the second extension beyond the core arc.
**Article Number**: A127
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-10 (42 references)

Standalone aerospace article and the second extension beyond the core fixed-wing-UAV arc (after A126 communications).
The master variable is the load factor n = L/W and the load-versus-speed diagram, the flight envelope bounded by the stall parabola, the structural limit-load line, and the maximum-speed line, with the structure sized to its corners.
Sections covered include
the flight envelope;
the corner and the maneuvering speed;
limit load and ultimate load (the 1.5 factor of safety);
categories and the width of the envelope (normal, utility, aerobatic);
the gust envelope (sharp-edged and derived gust, the light-UAV gust sensitivity);
loads beyond the flight envelope (launch, recovery, touchdown through the undercarriage, taxi and handling, tying A116 and A124);
how the structure carries the load (bending, shear, torsion, asymmetric and combined cases, spar/rib/longeron, monocoque and stressed skin, tying A112);
material, stress, buckling, and the margin of safety (specific strength and modulus, the before-yield instability of thin panels, strength versus stiffness);
fatigue and the life of the structure (the stress-life curve, safe-life, fail-safe, damage-tolerant);
aeroelasticity and the flutter boundary (divergence, control reversal, flutter as a dynamic-pressure wall, tying A112 and A123);
the aerobatic envelope (the widest symmetric diagram, negative-g structure, and the UAV no-pilot point tying loitering munitions, with the maneuver art and physiology out of scope);
the envelope is not fixed (density altitude, the A120 thermal wall, composite knockdown, fatigue, autopilot envelope protection tying A123/A125);
proving the structure (the static ultimate-load test, flutter clearance by ground vibration test and stepped envelope expansion, and the fatigue test article);
scale and the UAV case (square-cube structural fraction, composite and printed structures, attritable design);
a worked example on the 25 kg series aircraft (stall speed about 18 m/s, corner speed about 38 m/s, limit and ultimate loads, a gust increment that rivals the maneuver limit);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
The pilot's pre-draft question, whether aerobatics belongs, is answered in the article by covering aerobatics as the envelope's widest symmetric case.
References A112, A116, A120, A123, and A124 via post_url.
42 references across Book (1), Reference (33), Related Post (5), and Research (3) categories.

### Communications and the Command-and-Control Data Link for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-09-communications_and_the_command_and_control_data_link_for_fixed_wing_uavs.markdown`
**Topic**: The command-and-control data link of a fixed-wing UAV, framed on the link budget (received power versus noise) with latency as the companion constraint; the first extension beyond the core arc.
**Article Number**: A126
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-09 (34 references)

Standalone aerospace article and the first extension beyond the core fixed-wing-UAV arc (which closed with the A125 capstone).
The master variable is the link budget, P_rx = P_tx + gains - free-space path loss, with the signal-to-noise margin setting range and the Shannon limit bounding data rate, and latency as the companion constraint that decides what can be controlled over the link.
Sections covered include
the link budget (Friis, free-space path loss, SNR, Shannon, Fresnel, ISM bands, the frequency range-versus-rate trade, near-ground multipath and the two-ray ground reflection, the regulatory cap on effective radiated power);
the radio horizon;
the moving aircraft (airframe shadowing, radiation-pattern nulls and polarization, antenna diversity, a tracking ground antenna);
the three streams (command uplink, telemetry downlink, payload downlink with codec compression latency);
radio control with a handheld transmitter (2.4 GHz FHSS, ExpressLRS, CRSF/SBUS handoff, the control-link packet rate, FPV, failsafe, the manual path);
computer-controlled transmission (MAVLink, SiK/RFD900 telemetry radios, the ground control station, companion computer over cellular, intent versus stick inputs, coexisting with the handheld link);
beyond line of sight (relay, cellular, SATCOM via Iridium);
latency and why the fast loops are aboard (tying A123 and A125);
security and jamming (J/S ratio, spread spectrum, AES encryption, spoofing, directional antenna);
lost link (the preset failsafe, geofence, tying A116 and A125);
scale and the UAV case (the radios as part of the A121 hotel load);
a worked example (a 100 mW 2.4 GHz link closing 10 km with a 12 dB margin, a ~48 km radio horizon, kbps command versus Mbps video, LOS versus SATCOM latency);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
The pilot's explicit requirement, RC control via both a consumer handheld controller and a computer-controlled transmitter, is covered in its own two sections framed as the coexisting manual and autonomous paths.
References A116, A121, and A125 via post_url.
34 references across Reference (28), Related Post (3), and Research (3) categories.

### Guidance, Navigation, and Automatic Landing for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-08-guidance_navigation_and_automatic_landing_for_fixed_wing_uavs.markdown`
**Topic**: The outer-loop autonomy of a fixed-wing UAV, framed on the feedback loop that drives the error between the navigation estimate and the guidance command to zero; the capstone of the set.
**Article Number**: A125
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-08 (29 references; 333 lines)

Standalone aerospace article and the tenth and capstone entry in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion, A121 electric energy systems, A122 stability and control, A123 dynamic stability and control, A124 landing gear and touchdown, A125 guidance, navigation, and automatic landing).
Takes up the outer loop A123 set up.
The master variable is the feedback loop that drives the error between the commanded state (guidance) and the estimated state (navigation) to zero, nested by bandwidth, with the automatic landing as the tightest loop.
Sections covered include
the nested loops (inner attitude, outer guidance, mission, bandwidth separation, digital sample rates and latency);
navigation (GNSS, INS/IMU, dead reckoning, Kalman fusion, air data, RTK, initialization, GNSS-denied vision);
guidance (waypoints, cross-track error, the look-ahead path-following law);
wind and the ground track (crab, the wind triangle, the small-UAV case);
closing the loop with energy (the total energy control system as the real-time version of the series' energy budget);
the approach and automatic landing (glideslope, flare, RTK/radar-altimeter/vision, touchdown dispersion tied to the runway width) with the automatic-takeoff bookend;
when the loop breaks (GNSS loss, lost link, geofence, return-to-launch, redundancy, flight termination);
scale and the UAV case (Pixhawk-class boards, ArduPilot/PX4, the autonomy spectrum);
a worked example (loop bandwidth separation, the cross-track law, the navigation error budget, the glideslope dispersion);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
References A114, A116, A123, and A124 via post_url, and the conclusion ties the whole ten-article set together.
29 references across Reference, Related Post, and Research categories.
333 lines.

### Landing Gear and the Physics of Touchdown for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-07-landing_gear_and_the_physics_of_touchdown_for_fixed_wing_uavs.markdown`
**Topic**: Landing gear and the surface interfaces of a fixed-wing UAV, framed on the touchdown energy absorbed over a stroke, complementing the runway and recovery articles.
**Article Number**: A124
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-07 (23 references; 320 lines)

Standalone aerospace article and the ninth in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion, A121 electric energy systems, A122 stability and control, A123 dynamic stability and control, A124 landing gear and touchdown).
The master variable is the touchdown energy absorbed over a stroke, n = v^2/(2 g0 d), the energy-and-stroke idea of the recovery article applied to the final surface interface.
Sections covered include
the touchdown energy and the stroke;
wheels and landing gear (retractable versus fixed, tricycle and conventional layout, the oleo strut as gas spring and oil damper, recoil damping and bounce, frangible and sacrificial gear, spin-up and side gear loads, the gear-up fallback);
skids (sacrificial skids, friction stroke, skis and tundra tires by surface);
water landings (floatplane, flying boat, planing and the step, ditching, porpoising);
drogue and main parachutes (the drogue-before-main staging, with the residual touchdown energy taken by an airbag or crush);
deliberate impact (intentional lithospheric and hydrospheric intersection, crushable crashworthy structure for expendable vehicles);
energy bleeding before touchdown (spoilers, forward slip, S-turns, flare, with the honest distinction that true aerobraking is an orbital maneuver while a boost-glide or ramjet or scramjet vehicle does thermally limited atmospheric deceleration);
scale and the UAV case;
a worked example (sink-rate, parachute, and deliberate-impact loads set by the stroke);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
Complements rather than duplicates the launch-and-recovery article.
References A114, A116, A120, and A122 via post_url.
23 references across Reference, Related Post, and Research categories.
320 lines.

### Dynamic Stability and Control for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-06-dynamic_stability_and_control_for_fixed_wing_uavs.markdown`
**Topic**: Dynamic stability and control of a fixed-wing UAV, framed on the damping and frequency of the aircraft's natural modes, the dynamic sequel that completes the stability-and-control arc begun by the static-stability article.
**Article Number**: A123
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-06 (22 references; 316 lines)

Standalone aerospace article and the eighth in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion, A121 electric energy systems, A122 stability and control, A123 dynamic stability and control).
Takes up the dynamic question A122 deferred.
The master variable is the damping and frequency of the natural modes, with the aircraft modeled as a damped harmonic oscillator where static stability is the spring, inertia the mass, and aerodynamic rate forces the damping.
Sections covered include
the spring, the mass, and the damping (with a small-disturbance about-trim caveat);
the longitudinal modes (short-period, phugoid);
the lateral-directional modes (roll subsidence, spiral, Dutch roll, with the spiral-versus-Dutch-roll trade tied to A122's dihedral-versus-weathercock balance);
damping, frequency, and handling qualities (settling time, Cooper-Harper, flying-qualities levels);
gusts and ride quality (turbulence excitation and the small-UAV gust sensitivity);
stability augmentation (yaw damper, pitch damper, rate feedback from an IMU, the SAS inner loop, augmentation limits and pilot-induced oscillation, and the SAS-versus-CAS distinction);
fly-by-wire and relaxed static stability;
scale and the UAV case (faster modes, autopilot and actuator bandwidth);
a worked example (Dutch-roll damping from 0.05 to 0.4 with a yaw damper, and a phugoid period);
and an Out of Scope section that defers derivative estimation and the equations of motion, control-law synthesis, sensors and state estimation, structural and aeroelastic dynamics, departure and spin, and the outer-loop guidance, navigation, and automatic landing.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
References A112, A114, and A122 via post_url.
22 references across Reference, Related Post, and Research categories.
316 lines.

### Stability, Control, and Configuration for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-05-stability_control_and_configuration_for_fixed_wing_uavs.markdown`
**Topic**: Stability, control, and configuration of a fixed-wing UAV, framed on the balance of moments about the center of gravity with the static margin as the master proxy for the stability-versus-maneuverability trade.
**Article Number**: A122
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-05 (46 references; 409 lines)

Standalone aerospace article and the seventh in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion, A121 electric energy systems, A122 stability and control).
Takes up the full stability-and-control treatment A112 deferred.
The master variable is the moment balance about the center of gravity, with the static margin K_n = (x_np - x_cg)/MAC as the proxy for the stability-versus-maneuverability trade.
Sections covered include
the moment balance and the static margin (with the center-of-gravity range across the loading envelope);
lateral and directional static stability (fin weathercock stability and dihedral);
airfoils, camber, and invertibility;
configuration archetypes (conventional empennage, canard, tandem, tailless flying wing with sweep, washout, and reflex);
control surfaces by placement and name (elevator, aileron, rudder, elevon, ruddervator, stabilator, flaperon) with adverse yaw;
high-lift and spoiler devices;
control authority and dynamic pressure, running from aerodynamic surfaces through differential thrust and thrust vectoring to a reaction control system (spaceplane RCS and cold-gas thrusters, tied to A120's boost-glide arc, with an honest low-altitude caveat);
the wing tradeoff (aspect ratio versus wing loading, speed versus glide, planform);
the trim-drag energy cost;
a worked example (static margin and tail volume coefficient, with a flying-wing reflex contrast);
and an Out of Scope section that defers the dynamic-stability modes, control-law design, RCS detailed design, and the translational orbital problem (orbital mechanics, the orbital maneuver, and stationkeeping, affirmed as legitimate for spacecraft that reach orbit).
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
References A112, A114, and A118 via post_url.
46 references across Reference, Related Post, and Research categories.
409 lines.

### Electric Energy Systems and the Endurance Budget for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-04-electric_energy_systems_and_endurance_budget_for_fixed_wing_uavs.markdown`
**Topic**: The electric energy economy of a fixed-wing UAV, framed as a state-of-charge energy-flow budget (supply minus demand, buffered by storage), the flow counterpart to A120's stock budget.
**Article Number**: A121
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-04 (29 references; 381 lines)

Standalone aerospace article and the sixth in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion, A121 electric energy systems).
Fills the solar, fuel-cell, hybrid, and battery-management items A118 deferred.
The master variable is the energy-flow budget, the power balance dE/dt = P_in - P_out and its integral over the harvest cycle, contrasted explicitly with A120's one-time energy stock (stock versus flow).
Sections covered include
the energy-flow budget;
the demand side and the hotel load (flight power versus a fixed non-propulsive floor);
storage as the buffer (specific energy, depth of discharge, round-trip efficiency, cold derating, the specific-energy-versus-specific-power tradeoff, the battery wall, supercapacitor for peaks);
harvesting from the sun (output = efficiency times area times irradiance, the daily account, MPPT named);
the scale gate for solar perpetual flight (square-cube, Pathfinder/Helios/Zephyr/Solar Impulse);
harvesting from hydrogen (PEM fuel cell, Ion Tiger, Phantom Eye);
hybrid systems (series and parallel);
harvesting from the air (thermal and dynamic soaring);
the perpetual-flight closure (daily harvest at least daily demand, night energy within usable storage, cycle-life bounding the campaign);
a worked example on the 25 kg series aircraft;
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
The thesis is that sustained flight is a balance of powers rather than a quantity of energy, and indefinite flight is the cycle closing on itself, which the large light high-flying solar aircraft achieves and the small one does not.
References A112, A118, and A120 via post_url.
29 references across Reference, Related Post, and Research categories.
381 lines.

### Staged and Boosted Propulsion for Small Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-03-staged_and_boosted_propulsion_for_fixed_wing_uavs.markdown`
**Topic**: Staged and boosted propulsion for a ~2m fixed-wing UAV, framed around the post-boost mission energy budget (potential plus kinetic plus stored propulsive energy).
**Article Number**: A120
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-03 (40 references; 472 lines)

Standalone aerospace article and the fifth in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion).
Reopens the high-speed families A118 ruled out of regime by adding a boost stage, and is framed throughout as the management of the post-boost mission energy budget.
The boost deposits potential and kinetic energy (Tsiolkovsky rocket equation, specific impulse, one versus two stage), to which stored propulsive energy is added, and the kinetic share sets the stagnation temperature and therefore the airframe material.
Sections covered include
the mission energy budget with the energy height h_e = h + V^2/2g;
the boost stage;
the thermal wall (stagnation temperature versus Mach, aerodynamic heating, altitude and duration relief);
airframe materials by regime (LW-PLA subsonic, aluminum/composite transonic, titanium/steel supersonic with the SR-71 anchor, superalloy/refractory/CMC/carbon-carbon/UHTC/active-cooling/ablative hypersonic with the X-43 and X-51 anchors);
airframe archetypes for spending the budget (vertical-fighter banking it as altitude with the Bachem Natter anchor, maneuverable descending spending it on lift with lifting-body/waverider/HGV/MaRV members, and conventional holding it level on propulsion);
boost-glide with range (L/D)(h + V^2/2g);
boost-sustainer (RATO and the cruise-missile boost-turbojet);
boost-ramjet (integral rocket-ramjet, GQM-163 Coyote, Mach 2-4 titanium airframe);
boost-scramjet (X-43, X-51, hypersonic materials, research-grade honesty);
boost-throttleable-rocket;
one stage versus two;
a worked example on a 2 m vehicle (propellant fraction and stagnation temperature to Mach 2 and Mach 5, with the Mach-5 energy height of about 147 km);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
The thesis is that the ~2m scale forbids none of these configurations, since material and budget, not size, set how far up the speed ladder a prototype can be carried.
References A112, A114, A116, and A118 via post_url.
40 references across Reference, Related Post, and Research categories.
472 lines.

### Propulsion and Power Sizing for Small Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-02-propulsion_and_power_sizing_for_fixed_wing_uavs.markdown`
**Topic**: Sizing the propulsion and power system of a small fixed-wing UAV, worked outward from the power-required master variable.
**Article Number**: A118
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-02 (36 references; 445 lines)

Standalone aerospace article and the fourth in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion).
Establishes the power-required master variable, where power is thrust times speed and thrust in level flight is drag, so the power to fly is the weight times the speed divided by the lift-to-drag ratio, and works through
the drag polar and lift-to-drag ratio;
propellers and efficiency via momentum theory, static thrust, and advance ratio, including the electric ducted fan;
the thrust-to-weight and launch and climb case that usually sizes the powertrain, tying back to A114 and A116;
electric propulsion (battery specific energy, brushless motor, the endurance equation, and the battery wall);
combustion propulsion (two-stroke and Wankel, brake-specific fuel consumption, heavy fuel, range and endurance);
altitude and available power (the density-altitude lapse of engine power and propeller thrust);
endurance and range with reserves (endurance at the minimum-power speed, range at the best lift-to-drag speed for a propeller aircraft);
a brief solar, hybrid, and fuel-cell note;
jets and regimes beyond the propeller (turbojet and turbofan in scope; ramjet, scramjet, throttleable rocket, and rocket boost-glide named and declared out of regime);
a worked example on the 25 kg series aircraft;
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
Real-UAV anchors RQ-7 Shadow (Wankel), ScanEagle (heavy-fuel piston), and RQ-20 Puma (electric).
References A112, A114, and A116 via post_url.
36 references across Reference, Related Post, and Research categories.
445 lines.

### Three Audiences for an Operating System — Published

**File**: `_posts/2026-05-22-three_audiences_for_an_operating_system.markdown`
**Topic**: Prequel to the BTRON-hypermedia trilogy. Names the operator-as-end-user category as a distinct third audience for an operating system, alongside the consumer and the developer. Sets up the question that A113, A115, and A117 then answer.
**Article Number**: A119
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-22 (61 references; 1,364 lines)

Standalone category-framing article and the prequel to the BTRON-hypermedia trilogy (A113, A115, A117).
Sections covered include
Opening on who an operating system serves;
The Three Audiences (consumer, developer, operator with role definitions and the load-bearing authority concept);
The Consumer Answer (Apple HIG, Windows UX Guidelines, GNOME HIG, KDE HIG, Material Design);
The Developer Answer (Unix philosophy, Emacs, Vim, Visual Studio Code, Git, Cargo, npm, pip);
The Operator (the unfilled category);
A Short History of Operator-Facing Computing (Sketchpad, NLS, MOCR, Alto, Macintosh, BTRON, HyperCard, OpenDoc, GNOME Bonobo, SCADA, PLCs, ARINC 661, ISA-101, NUREG-0700, IEC 62366, ISO 9241, ASM Consortium);
Why the Consumer Answer Fails the Operator (five structural failure modes);
Why the Developer Answer Also Fails (four structural failure modes);
The Operator Population Today (aerospace, medical, industrial, defense and intelligence, legal and regulatory, financial markets);
A Scorecard of Audience Requirements (10-row table across consumer, developer, operator);
The Gap That Remains;
Out of Scope (defers the substantive solution, the language substrate, and the worked vertical to the trilogy);
Conclusion.

References:
61 references across Reference (58) and Related Post (3) categories.
All inline-linked per project style.
A113, A115, and A117 cited via post_url as the deferred follow-ups.
No internal research cited.
A research agent verified the operator-specific references (ISA-101, ASM Consortium, IEC 62366, ISO 9241, NUREG-0700, ARINC 661, glass cockpit, SCADA, HITL, ergonomics, alarm fatigue) and the audience-contrast sources (Apple HIG, Windows UX, GNOME HIG, KDE HIG, Unix philosophy).

### Launch and Recovery Systems for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-01-launch_and_recovery_systems_for_fixed_wing_uavs.markdown`
**Topic**: Runway-independent launch and recovery for fixed-wing UAVs, worked outward from the energy-and-stroke master variable.
**Article Number**: A116
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-01 (26 references; 478 lines)

Standalone aerospace article and the runway-independent companion to A114.
Establishes the energy-and-stroke master variable, where launch must add and recovery must remove a kinetic energy fixed by mass and flying speed and the g-load rises as the stroke shrinks, and works through
launch by catapult (bungee, pneumatic, hydraulic, rail), winch and aerotow, booster, and zero-length launch;
recovery by net and cable (Skyhook), arrested landing, parachute and airbag, belly skid, and high-alpha braking (deep stall, cobra braking as a routine procedure, and perched landing);
wind and environment;
the acceleration limit;
failure and abort modes, with the fail-safe principle and a flight-termination or controlled-ditch option;
matching launch to recovery with real-UAV anchors (ScanEagle, RQ-7 Shadow, RQ-21 Blackjack);
airframe implications;
a worked numeric example;
and a fully declared Out of Scope.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
References A114 (Runway Sizing for Fixed-Wing UAVs) and A112 (Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass) via post_url.
26 references across Reference, Related Post, and Research categories.
478 lines.

### Human Spaceflight Ground Systems as an Illustrative Vertical for a Hypermedia Desktop — Published

**File**: `_posts/2026-05-25-human_spaceflight_ground_systems_as_illustrative_vertical.markdown`
**Topic**: Vertical-specific follow-up to A113 and A115. Walks through human spaceflight ground systems in the Apollo lineage, lampshaded as an illustrative example vertical with explicit extrapolation guidance to modern crewed launch and on-orbit operations. Includes a Day-in-the-Launch-Operator's-Workflow walkthrough and six verified Keleusma code samples for the load-bearing claims.
**Article Number**: A117
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-25 (40 references; 1,944 lines)

Sections covered include
The Apollo Reference (MOCR, RTCC on IBM System/360 Model 75, LCC and Firing Rooms, MSFN, NASCOM, Flight and Mission Rules, simulators, recovery, the flight directors and Apollo 13);
Extrapolation to Modern Requirements (CCSDS, Commercial Crew Program, ISS Multilateral Coordination, Artemis and Human Landing System, FAA Part 450, NPR 7150.2 and NASA-STD-8719.13 and NPR 8705.2, ITAR);
The Hypermedia Object Model in Launch Operations (six commitments with Apollo-to-hypermedia mapping table);
Engineering Commitments in Launch Operations (five commitments with five Keleusma code samples and a mapping table);
The Ten-Layer Architectural Sketch in Launch Operations (full table inheriting A115 verdicts and clarifying each layer's launch role);
A Day in the Launch Operator's Workflow (eleven scenes from pre-launch shift report through post-flight review);
Trust and Provenance;
Certification and Regulatory Posture;
Why This Vertical Is a Good Illustration (and where it is hard);
Risks and Open Questions;
Out of Scope (link store schema, certification path, contractor selection deferred to future posts);
Conclusion.

Six verified Keleusma code samples in `tmp/a117/`:
01_countdown_sequencer.kel (loop main compiles to 260 bytes);
02_telemetry_alarm.kel (Proprietary -> displayable bucket, returns 1);
03_abort_decision.kel (Sensitive -> typed outcome, returns 2);
04_abort_decision_reject.kel (same without declassify, compile-time reject);
05_mission_rules.kel (const data registry, returns 300);
06_signed_flight_rules.kel (signed entry function compiles to 232 bytes).

References:
40 references across Reference (37), Related Post (2), and Research (1) categories.
All inline-linked per project style.
A113 and A115 cited via post_url.
Apollo-era and contemporary primary sources verified by a parallel research agent.
No internal Keleusma research cited.

### Keleusma as a Substrate for a Real-Time Hypermedia Desktop — Published

**File**: `_posts/2026-05-24-keleusma_as_substrate_for_real_time_hypermedia_desktop.markdown`
**Topic**: Follow-up to A113. Maps Keleusma V0.2.0 capabilities and the public V0.5+ roadmap onto A113's six structural commitments of the hypermedia object model, the five engineering commitments for real-time hypermedia composition, and the ten-layer architectural sketch. Vertical-agnostic by design; the vertical-specific treatment is deferred to a separate follow-up.
**Article Number**: A115
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-24 (45 references; 1,701 lines)

Analytical follow-up to A113. Sections covered include
What Keleusma Provides at Version 0.2.0;
The Six Structural Commitments of the Hypermedia Object Model;
The Five Engineering Commitments for Real-Time Hypermedia;
Mapping the Ten-Layer Architectural Sketch (ten verdicts: two strong fits, five partial fits, three mismatches);
What Keleusma Uniquely Provides (verified totality, verified WCET/WCMU, language-level IFC);
What Keleusma Does Not Provide (mature ecosystem, general-purpose breadth, authoring tooling);
The Asymmetry and Its Implication;
The Roadmap Path (V0.3.0 self-hosted compiler through V0.5.x interval-graph refinement);
What Would Need to Be Built;
Risks and Open Questions;
Out of Scope (vertical choice, detailed link store design, certification path all deferred to separate posts);
Conclusion.

Five illustrative Keleusma code samples verified against the installed keleusma 0.2.0 CLI:
01_typed_part.kel (Citation struct, runs and returns 42);
02_handler_loop.kel (loop main with yield, compiles to 228-byte bytecode);
03_ifc_sanitiser.kel (classify/declassify sanitiser pattern, runs and returns 200);
04_ifc_reject.kel (same without declassify, verifier rejects at compile time);
05_preallocated.kel (const data block, runs and returns 20).

All examples in `tmp/a115/`.

References:
45 references across Reference (38), Related Post (5), and Research (1) categories.
Inline citations throughout per project style.
A113, A107, A109, A110, A111 cited via post_url.
No internal Keleusma research material cited; only public Keleusma artefacts (README, crates.io, docs.rs, GitHub).

**Remaining Work**:
Human review of analytical claims and the Keleusma-to-BTRON mapping.
Confirm publication date and assign final timestamp.
Update memory once published.

### Runway Sizing for Fixed-Wing UAVs — Published

**File**: `_posts/2026-05-31-runway_sizing_for_fixed_wing_uavs.markdown`
**Topic**: Sizing runways for small and medium fixed-wing UAVs, worked outward from the master speed variable.
**Article Number**: A114
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-31 (28 references; 548 lines)

Standalone aerospace article.
Establishes the squared-speed master variable, where stall and liftoff speed are set by wing loading, air density, and the maximum lift coefficient, and works outward through explicit square-cube size-scaling;
the level ground roll;
paved versus dirt surfaces;
inclined and ski-jump runways;
wind, crosswind, and landing-gear ground handling;
orientation with an Earth-rotation dismissal;
density altitude;
obstacle clearance, margins, and an in-scope abort and stopping-margin note;
the landing roll and ground effect;
width and the lateral dimension (touchdown dispersion and guidance lateral error);
full-runway versus single-phase operation anchored to real UAVs (ScanEagle, RQ-7 Shadow, MQ-9 Reaper);
planform and airframe implications (conventional, delta, flying wing);
a worked numeric example;
and lighting, reflectors, and markings (optional versus required).
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
References A112 (Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass) via post_url.
28 references across Reference, Related Post, and Research categories.
548 lines.

### BTRON, Hypermedia, and the Real-Time Desktop — Published

**File**: `_posts/2026-05-23-btron_hypermedia_and_real_time_desktop.markdown`
**Topic**: Historical and analytical treatment of the BTRON proposition, the asymmetry between successful real-time operating systems and failed hypermedia desktops, a contemporary diagnosis of the market gap, and a concrete architectural sketch for a 2026 successor.
**Article Number**: A113
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-23 (149 references; 4,166 lines)

Standalone operating-systems history and philosophy article.
Surveys the BTRON proposition under the TRON Project (Sakamura, 1984),
why BTRON failed (Super 301 trade dispute listed in April 1989 and withdrawn the following month after USTR site visit, hardware program collapse, ecosystem shortfall, conceptual depth tax, vendor entrenchment),
the histories of relevant real-time operating systems (VRTX 1981, pSOS ~1982, VxWorks 1987, QNX 1980 in the Ottawa area of Canada, QNX Photon, Green Hills INTEGRITY, FreeRTOS, Zephyr, RTEMS, NuttX, μITRON, T-Kernel, seL4, Genode, Redox OS),
the histories of hypermedia systems (Memex, NLS in 1968 funded by ARPA/NASA/USAF, Project Xanadu, Smalltalk, NoteCards developed at Xerox PARC starting 1984 by Trigg/Halasz/Moran, HyperCard 1987-2004, OLE 2 in the 1992-1993 window, Cairo, OpenDoc framework 1994 and CyberDog 1996, Bonobo, KParts, Lotus/HCL Notes ~42M peak seats with ~140M cumulative licenses, SharePoint, World Wide Web with the Berners-Lee 1989 CERN proposal, Roam, Logseq, Obsidian, Notion, Coda, Jupyter, Observable, Solid, Beaker last released December 2020, Automerge, Yjs, ActivityPub),
the six structural commitments of the hypermedia object model,
where the model wins on merit and where it is clearly the wrong fit,
the real-time-plus-hypermedia special case,
who is served by the mass-market file-and-application model,
who would benefit from a real-time hypermedia desktop,
the web browser as substrate analysis,
a super-browser as modern realization,
why the gap persists (four-component diagnosis),
and viable entry strategies (vertical-first, internal-program, acquisition-path, sponsored-standards).
References A93 (Fast-Moving Versus Mission-Critical Engineering) and A86 (Mission Command Management Style) via post_url.
76 references across 4 categories (Book, Reference, Related Post, Research).
2,219 lines.

**Research Pass (2026-05-31)**:
Four parallel research agents verified factual claims across TRON Project history,
real-time operating systems history, hypermedia systems history,
and contemporary tools / regulated-industry incumbents / standards.
Corrections applied:
ITRON deployment softened from "several billion per year" to "cumulative billions";
Super 301 chronology refined (listed April 1989, withdrawn May 1989);
Real Object / Virtual Object pairing introduced for BTRON's hypermedia model;
TRON character code Unicode comparison added with concrete dates (Cho Kanji 1999 ~180K characters vs Unicode 4.1 in 2005);
RTOS first-generation date range corrected from "1970s-early 1980s" to "early 1980s";
QNX origin location corrected from "Ottawa" to "Ottawa area of Canada" with University of Waterloo founder attribution;
QNX Photon deprecation since 2014 disclosed;
QNX vehicle deployment updated to "more than 275 million" with BlackBerry press release citation;
FreeRTOS "most widely deployed" softened to "among the most widely deployed";
FreeRTOS AWS 2017 transaction reframed as stewardship transfer with AWS blog citation;
seL4 superlative softened to "most extensive functional-correctness proof of a general-purpose OS kernel";
Redox OS alpha status disclosed;
NLS funding expanded to ARPA/NASA/USAF;
NoteCards authorship attributed (Trigg, Halasz, Moran);
HyperCard "several million users" softened to "millions";
OLE 2 release window clarified (1992-1993);
OpenDoc shipping clarified (framework 1994, CyberDog 1996);
Lotus Notes seat counts corrected from "hundreds of millions" to ~42M active / ~140M cumulative;
SharePoint primitives clarified (files and lists);
Beaker reframed from "dormant" to "discontinued after December 2020";
ARP4754B successor noted.
URL fixes:
ref_cho_kanji (Wikipedia 404, replaced with chokanji.com);
ref_super_301 (replaced with Section 301 stable URL);
ref_vrtx (replaced with Versatile_Real-Time_Executive);
ref_qnx_neutrino (replaced with qnx.software);
ref_qnx_photon (replaced with QNX_Photon Wikipedia entry).
New references added with inline citations:
ARP4754A; TRON character encoding;
IEEE Milestone for TRON RTOS family;
USTR 25 May 1989 statement;
Mars Pathfinder priority inversion engineering note;
BlackBerry QNX 275M vehicles press release;
Amazon FreeRTOS launch blog post;
seL4 SOSP 2009 paper;
Engelbart and English 1968 AFIPS paper;
Halasz 1988 NoteCards retrospective in CACM;
Berners-Lee 1989 CERN proposal;
Kleppmann and colleagues local-first essay (Onward 2019).
URL verification:
all new URLs return HTTP 200 except ACM Digital Library and chokanji.com which return 403 to curl due to bot detection but are valid human-accessible URLs.

**Expansion Pass (2026-05-31)**:
Four additional parallel research agents covered alternative research operating systems (Plan 9, Inferno, Self, Oberon, JX),
the artificial intelligence and large language model angle (retrieval-augmented generation, Model Context Protocol, structured output, Coalition for Content Provenance and Authenticity, agent provenance research),
architectural building blocks for a 2026 hypermedia operating system (Automerge, Yjs, Loro, InterPlanetary File System, Iroh, Hypercore, seL4, Genode, Capsicum, Cap'n Proto, WebAssembly Component Model, Servo, Chromium Embedded Framework, WebKit, ProseMirror, TipTap, Lexical, JetBrains Meta Programming System, CodeMirror, Skia, Cairo Graphics, HarfBuzz, FreeType),
and regulated-industry incumbents (DOORS, Polarion, Windchill, ENOVIA, Vault, Gotham, Foundry, Relativity, iManage).
Seven new sections added:
"Other Radical Unifications" (Plan 9, Inferno, Self/Morphic, Oberon, JX as alternative unification approaches);
"Performance and Latency Engineering for Composed Documents" (bounded handler execution time, deadline propagation, preallocated resources, spatial and temporal isolation, admission control);
"The Artificial Intelligence Synergy" (RAG, MCP, structured output, C2PA, regulatory provenance requirements, PROV-AGENT, HyperAgents workshop);
"How the Incumbents Compare" (comparison table across the nine incumbents on typed parts, typed links, in-place composition, provenance, and local-first persistence);
"Coexistence with the File and Application World" (file system bridges, import handlers, lossy export, gradual adoption);
"A Concrete Architectural Sketch" (ten layers from verified microkernel through user-facing shell, naming production-quality open-source components for each);
"Out of Scope" (explicit declaration of seven topics deferred to follow-up articles).
56 new authoritative sources added with inline citations.
Reference count rose from 76 to 132 across Book (2), Reference (108), Related Post (2), and Research (20) categories.
Line count rose from 2,219 to 3,408.

**Completion Pass (2026-05-31)**:
Three additional parallel research agents covered Lifestreams (Gelernter and Freeman, Yale, mid-1990s),
Sutherland's Sketchpad (1963) and Alan Kay's Dynabook (1968-1972),
and the contemporary Tools for Thought movement (Matuschak, Nielsen, Appleton, Bret Victor, Rheingold, Future of Coding, Hyperlink Academy).
Seven new sections and inline additions added:
Sketchpad paragraph in hypermedia history;
Dynabook paragraph in hypermedia history;
Lifestreams paragraph in hypermedia history;
Tools for Thought paragraph in hypermedia history (with cultural framing);
"A Day in the Workflow, an Aerospace Requirements Example" between Architectural Sketch and Conclusion;
"Epistemic State of the Argument" between Workflow and Conclusion (distinguishing factual, structural, and strategic claims);
"Reader's Next Steps" after Out of Scope (TRON Forum, seL4 community, Genode community, local-first community, Solid working group, HyperAgents workshop, Tools for Thought community);
"Glossary" after Reader's Next Steps (defined-terms section for 12 key concepts including capability-based security, compound document, conflict-free replicated data type, content-addressable storage, handler, hypermedia object model, link store, microkernel, provenance, real-time operating system, separation kernel, transclusion, typed link, typed part).
17 new authoritative sources added with inline citations:
Mirror Worlds (Gelernter 1991 Oxford);
Tools for Thought (Rheingold 1985 MIT Press);
Lifestreams CHI 1996 paper;
Lifestreams SIGMOD 1996 paper;
Lifestreams Yale project page;
Sutherland's Sketchpad Cambridge-hosted thesis;
Sketchpad Wikipedia;
Kay and Goldberg Personal Dynamic Media 1977;
Dynabook Wikipedia;
Matuschak and Nielsen 2019 ttft essay;
Matuschak personal site;
Evergreen Notes;
Maggie Appleton personal site;
Appleton Garden History essay;
Bret Victor Magic Ink essay;
Future of Coding;
Hyperlink Academy.
Reference count rose from 132 to 149.
Line count rose from 3,408 to 4,166.
All anchors verified used and defined; style scan clean.
URL verification: all HTTP 200 except documented OUP 202 (project memory) and ACM DL 403 (bot detection, valid for human readers).

**Remaining Work**:
Human review of the four completion-pass additions (Lifestreams, Sketchpad/Dynabook, Tools for Thought, user journey walkthrough, epistemic state, next steps, glossary).
Confirm publication date and assign final timestamp.
Update Software Versions section if any is desired (currently omitted to match A98-class analytical-article convention).
Update memory once published.

### Solana sBPF Assembly Example — Pre-Release Candidate

**File**: `solana_sbpf_assembly_example.markdown`
**Topic**: Writing Solana programs using sBPF assembly with the sbpf standalone toolchain
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

Completely rewritten from a partial draft with x86 assembly and clang build.rs
to use the correct sBPF instruction set and the sbpf standalone toolchain.
Covers the sBPF virtual machine, registers and memory layout, instruction set overview,
toolchain installation, project creation, a Hello World program using `.rodata` section,
`lddw` address loading, and `.equ` named constants for all non-trivial literals.
Building and deploying with sbpf tool,
and the current state of mixed Rust and assembly projects.
Three experimental paths for mixed projects documented (nightly inline asm, sbpf-linker, build.rs).
Includes a theoretical linked Rust and assembly example
using the Solana SDK's Clang and llvm-ar in a `build.rs` script.
The Rust entrypoint passes a string to an sBPF assembly logging subroutine via C FFI.
Both assembly files use `.equ` named constants with inline comments.
Nine limitations documented.
Eleven references across two categories (Reference, Research).
No article number assigned. Not slotted for publication.

**Remaining Work**:
Human verification by building and deploying the Hello World program with the sbpf tool.
Verify the linked Rust and assembly example compiles with cargo build-sbf.
Fill in Software Versions TODO placeholders.
Verify assembly code executes correctly on a local test validator.
Assign article number and publication date when ready.

### Android Development on FreeBSD — Pre-Release Candidate

**File**: `android_development_on_freebsd.markdown`
**Topic**: Android SDK and NDK development on FreeBSD using Kotlin, Rust, and the Linuxulator
**Completion**: ~90%
**Publication Sensibility**: Medium
**Status**: Pre-Release Candidate

Completely rewritten from 2017 content (FreeBSD 11, SDK 25, NDK r13b)
to modern toolchain (FreeBSD 14, SDK 35, NDK r28).
Covers Linuxulator setup with Rocky Linux 9 base,
Android SDK and NDK installation via sdkmanager,
ADB setup with native FreeBSD port,
Kotlin SDK development with standard XML layouts,
Rust NDK development with JNI integration via cargo-ndk,
and emulator feasibility discussion.
Sample app is a native Android port of the CLMM calculator (A91)
with Kotlin UI and Rust math exposed through JNI.
No article number assigned. Not slotted for publication.
Ten references across four categories (Android, FreeBSD, Related Post, Rust).

**Remaining Work**:
Human verification on FreeBSD hardware.
Fill in Software Versions TODO placeholders.
Test build pipeline on FreeBSD 14 with Linuxulator.
Assign article number and publication date when ready.

### Android Unit Testing — Pre-Release Candidate

**File**: `android_unit_testing.markdown`
**Topic**: Android unit testing across Kotlin, Robolectric, instrumented, and NDK layers
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

Completely rewritten from 2017 content (SDK 25, Java 1.8, ApplicationTestCase)
to modern toolchain (SDK 35, JDK 17, Kotlin 2.1.0, AGP 8.9.0).
Test subject is the CLMM calculator app with both Kotlin and Rust native implementations.
Covers test dependencies (JUnit 4, AndroidX Test, Robolectric, MockK, Espresso),
local unit tests with pure logic and Robolectric Activity tests,
mocking with MockK object declarations,
instrumented tests with Espresso,
and NDK unit testing with Rust cargo test, JNI boundary testing, and GoogleTest for C++.
Running Tests section provides Gradle task table. Code Coverage section covers JaCoCo, Kover, and cargo-llvm-cov.
Seven limitations documented. MathJax enabled for CLMM reserve formulas.
References Android FreeBSD article and CLMM Mathematics (A91) via post_url.
No article number assigned. Not slotted for publication.
Twelve references across four categories (Android, Reference, Related Post, Rust).

**Remaining Work**:
Human verification of test code against actual Android project.
Fill in Software Versions TODO placeholders.
Verify floating-point test expected values against CLMM calculator.
Verify JNI function name conventions for NativeBridgeTest.
Assign article number and publication date when ready.
Android FreeBSD article and CLMM Mathematics (A91) must be published first.

### Authenticating a Phoenix JSON API with Guardian and Ueberauth — Pre-Release Candidate

**File**: `phoenix_json_api_authentication_with_guardian.markdown`
**Topic**: Phoenix/Elixir JSON API authentication with Guardian JWT and Ueberauth identity strategy
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

Completely rewritten from 2016 content (Phoenix 1.1.4, Elixir 1.2.3, Guardian ~0.10.0, Comeonin ~2.1)
to modern toolchain (Phoenix 1.7+, Guardian ~> 2.3, bcrypt_elixir ~> 3.0, Ueberauth ~> 0.10).
MemoApi example application with user registration, JWT-based login, and protected memo CRUD.
Uses context modules, Guardian implementation module pattern, plug pipeline, and error handler.
Ueberauth identity strategy integration with callback pattern example.
Testing the API section with curl commands and expected JSON responses.
Seven limitations documented.
References published article A27 "A Shell Script for Working with Phoenix JSON APIs" via post_url.
No article number assigned. Not slotted for publication.
Eleven references across four categories (Elixir, Phoenix, Reference, Related Post).

**Remaining Work**:
Human verification by building and running the MemoApi project.
Fill in Software Versions TODO placeholders.
Verify Guardian secret key generation command.
Verify Ueberauth identity strategy plug compatibility.
Assign article number and publication date when ready.

### Getting Started with Claude Code on FreeBSD — Pre-Release Candidate

**File**: `claude_code_getting_started_on_freebsd.markdown`
**Topic**: Installing and configuring Claude Code on FreeBSD
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

New article covering Claude Code installation on FreeBSD via the misc/claude-code port, binary packages, and npm.
Documents shebang fix, ripgrep configuration, and a Hello World exercise
that generates a curses-based system dashboard using only FreeBSD base system tools.
Limitations section documents unsupported platform status and known issues.
References the companion Getting Started with Claude Code post (A74) via post_url.
Twelve references across four categories (Claude, FreeBSD, GitHub, Related Post).
No article number assigned. Not slotted for publication.

**Remaining Work**:
Human verification on FreeBSD hardware.
Fill in Software Versions output.
Test the Hello World prompt on FreeBSD.
Verify shebang fix and ripgrep configuration.
Assign article number and publication date when ready.

### Getting Started with Claude Code Over SSH — Pre-Release Candidate

**File**: `claude_code_getting_started_over_ssh.markdown`
**Topic**: Using Claude Code locally to work on remote machines over SSH
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

New article covering the use of Claude Code on a local workstation
to execute commands on remote machines via SSH.
Introduces SSH fundamentals for readers unfamiliar with the protocol.
Walks through Ed25519 key generation, public key copying, SSH agent setup,
host configuration, and verification.
Documents remote execution patterns using Claude Code's Bash tool
including single commands, multi-command chains, and scp file transfer.
Covers timeout configuration for long-running remote operations.
Detailed agent forwarding section covers mechanism, configuration,
verification, Claude Code usage, security considerations,
and ProxyJump as a safer alternative for untrusted intermediate hosts.
Briefly discusses Claude Code Desktop SSH as an alternative
that requires Claude Code on the remote machine.
Hello World section demonstrates end-to-end remote workflow
with OS detection, C code generation, scp transfer, and remote compilation.
References companion Getting Started posts for macOS (A74), FreeBSD, and OpenBSD via post_url.
Eleven references across three categories (Claude, Reference, Related Post).
No article number assigned. Not slotted for publication.

**Remaining Work**:
Human verification with an actual remote SSH target.
Fill in Software Versions output.
Test the Hello World prompt against a remote machine.
Verify agent forwarding with `ssh -A myserver "ssh-add -l"`.
Verify timeout configuration format.
Assign article number and publication date when ready.

### Getting Started with Claude Code on OpenBSD — Pre-Release Candidate

**File**: `claude_code_getting_started_on_openbsd.markdown`
**Topic**: Installing and configuring Claude Code on OpenBSD
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

New article covering Claude Code installation on OpenBSD via npm,
the only viable installation path on the platform.
No port or package exists for Claude Code on OpenBSD.
Documents bash installation and `/bin/bash` symlink requirement,
ripgrep configuration via `USE_BUILTIN_RIPGREP` setting,
and a critical warning against running the native installer or `claude install`
which downloads an incompatible Linux binary and breaks npm installations.
Hello World exercise generates a curses-based system dashboard using only OpenBSD base system tools.
Limitations section is more extensive than the FreeBSD article
due to the absence of a dedicated port and the removal of the Linux compatibility layer.
References the companion Getting Started with Claude Code post (A74)
and the FreeBSD article via post_url.
Twelve references across four categories (Claude, GitHub, OpenBSD, Related Post).
No article number assigned. Not slotted for publication.

**Remaining Work**:
Human verification on OpenBSD hardware.
Fill in Software Versions output.
Test the Hello World prompt on OpenBSD.
Verify bash symlink and ripgrep configuration.
Verify that `doas pkg_add node` installs a supported Node.js version (18-24).
Assign article number and publication date when ready.

### Getting Started with Solana Using Rust and Pinocchio — Pre-Release Candidate

**File**: `solana_with_rust_and_pinocchio_getting_started.markdown`
**Topic**: Building a Solana program with Pinocchio zero-dependency library, mirroring the Anchor companion article (A65)
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

New article mirroring A65 "Getting Started with Solana Using Rust and Anchor"
but using the Pinocchio zero-dependency library instead of Anchor.
Same key pegboard toy contract that stores a public key and encrypted private key on-chain.
Covers Pinocchio project setup, manual account validation, raw byte parsing,
PDA creation via CPI to System Program, Mollusk test harness,
building with cargo build-sbf, and deployment to local test validator.
Comparison table with Anchor implementation (A65).
Nine limitations documented.
References published article A65 via post_url.
No article number assigned. Not slotted for publication.
Twelve references across three categories (Reference, Related Post, Research).

**Remaining Work**:
Human verification by building and deploying the program with cargo build-sbf.
Fill in Software Versions TODO placeholders.
Run Mollusk tests against compiled BPF binary.
Verify Pinocchio crate versions are current.
Assign article number and publication date when ready.

### Template

**File**: `template.markdown`
**Topic**: Post template for new articles
**Completion**: N/A
**Publication Sensibility**: N/A

This is a template file, not a draft. It provides the standard structure for new posts.

## Summary

Ten files exist in `_drafts/`. One is a template.
No release candidates remain.
No new drafts remain.
No stubs remain.
A79 through A144 have been published.

**Tier 1: Publishable with moderate effort.**
No drafts remain in Tier 1.
A126 (communications and the command-and-control data link), A127 (structures and the flight envelope), A128 (aerobatics as costed trajectories, the synthesis capstone of the extension set), A129 (an aerobatic maneuver reference catalog, the reference companion to A128), A130 (payload and mission systems), and A131 (the regulatory and operations layer) are the six extensions beyond the core fixed-wing-UAV arc; the series and its extensions are now complete, with no further extensions flagged.
A132 through A144 are the SBIR/STTR practitioner playbook, a complete thirteen-article series in the new business/funding/sbir category covering the United States SBIR and STTR programs from orientation, agency survey, eligibility and registration, finding a topic and reading a solicitation, the Phase I proposal, Phase II and the commercialization plan, Phase III and the valley of death, data rights and intellectual property, the money, after the award, strategy, and international analogs through a worked-campaign capstone that reuses the fixed-wing UAV; the series is now complete, all thirteen of thirteen articles published.

The drafts fall into four tiers when assessed for salvageability with contemporary tooling.

**Pre-Release Candidates.**
Android Development on FreeBSD has been fully rewritten with modern tooling
and is awaiting verification on FreeBSD hardware before publication.
Android Unit Testing has been fully rewritten with contemporary AndroidX Test, Robolectric, MockK,
and NDK testing coverage and is awaiting verification against an actual Android project.
Getting Started with Claude Code on FreeBSD covers installation via ports, packages, and npm
and is awaiting verification on FreeBSD hardware before publication.
Getting Started with Claude Code on OpenBSD covers npm-only installation with bash and ripgrep configuration
and is awaiting verification on OpenBSD hardware before publication.
Getting Started with Claude Code Over SSH covers using Claude Code locally to work on remote machines via SSH
and is awaiting verification with a remote SSH target.
Authenticating a Phoenix JSON API with Guardian and Ueberauth has been fully rewritten
from 2016 Phoenix 1.1/Guardian 0.10 to modern Phoenix 1.7+/Guardian 2.x
and is awaiting verification by building and running the MemoApi project.
Solana sBPF Assembly Example has been fully rewritten from a partial draft with x86 assembly
to use the correct sBPF ISA and the sbpf standalone toolchain,
revised with `.rodata` section usage and a theoretical linked Rust and assembly example,
and is awaiting verification by building and deploying with the sbpf tool.
Getting Started with Solana Using Rust and Pinocchio mirrors the Anchor companion article (A65)
using the Pinocchio zero-dependency library
and is awaiting verification by building and running Mollusk tests.

**No stubs remain.**
All article-numbered drafts have been elevated to release candidate status.

## Candidate Future Post Topics

The following table lists on-brand post ideas organized by thematic cluster.
Topics are selected to align with the blog's established strengths in systems programming, applied mathematics, unconventional toolchains, and AI-assisted development.

| Topic | Categories | Rationale | Builds On |
|-------|------------|-----------|-----------|
| Formal Verification with TLA+ | math development | Formal methods for distributed protocol design. Bridges the mathematical rigor thread with systems engineering. | Writing Proofs (A79), Radioactive Half-Life Demurrage Cryptocurrency Coin (A88) |
| Lean 4 and Automated Theorem Proving | math ai development | Interactive theorem prover with growing LLM integration. Connects proofs, AI, and software verification. | Writing Proofs (A79) |
| Property-Based Testing in Rust | rust development | QuickCheck-style testing as lightweight formal methods. Practical bridge between proofs and everyday engineering. | no_std Rust series, AMM Mathematics (A67) |
| RISC-V Assembly Getting Started | asm embedded development | Emerging instruction set architecture for embedded and open hardware. Natural extension of ARM and x86 assembly posts. | ASM Playdate Development, UNIX ARM Assembler |
| Rust on RISC-V Microcontrollers | rust embedded no_std | no_std Rust on RISC-V hardware. Combines two active threads in the blog. | no_std Rust series, Radioactive Half-Life Demurrage Cryptocurrency Coin (A88) |
| WebAssembly Component Model | rust wasm development | WASI and the component model as the next step beyond basic WASM. | WASM on Jekyll (A73) |
| ~~CLMM Mathematics and Calculator~~ | ~~crypto defi math~~ | ~~Concentrated liquidity mathematics with interactive widget. Direct sequel to AMM article.~~ | ~~Covered by Concentrated Liquidity Market Maker Mathematics (A91)~~ |
| ~~Solana sBPF Assembly~~ | ~~crypto development asm~~ | ~~Writing Solana programs at the assembly level. Unique low-level blockchain content.~~ | ~~Covered by Solana sBPF Assembly Example draft~~ |
| Statistics for A/B Testing | math development | Applied statistics for software engineers. Practical extension of the statistics reference. | Probability and Statistics Reference (A80) |
| ~~Orbital Mechanics Primer~~ | ~~math science~~ | ~~Applied physics with MathJax. Evergreen STEM content.~~ | ~~Covered by Introduction to Space Studies (A90)~~ |
| Context Engineering Patterns Cookbook | ai ai-tools development | Practical patterns distilled from the survey article. Shorter, actionable format. | Context Engineering (A78), A75-A77 series |
| Evaluating AI-Generated Code | ai development | Metrics and methods for assessing agent output quality. Addresses the evaluation gap identified in A78. | A75-A78 series |
| FreeBSD Jails for Development Environments | freebsd development | Container-like isolation using FreeBSD jails. Updates the FreeBSD systems thread with modern practices. | FreeBSD series (A1-A40 era) |
| Shell Scripting with Modern CLI Tools | sh unix development | fd, ripgrep, jq, fzf as modern replacements for traditional UNIX tools. | Shell scripting series |
| Game AI with Minimax and Alpha-Beta Pruning | gamedev math ai | Classical game AI algorithms with proofs of optimality. Bridges game development and mathematical rigor. | Chess/Go game theory series |
| Playdate Game Physics | gamedev playdate math c | Physics simulation on constrained hardware. Applied mathematics on embedded game platform. | Playdate series, Trigonometry (A14) |
| Observable Signatures of Competitive Civilizations | science philosophy | Unselected A101 candidate. What observational evidence would distinguish competitive expansion from natural astrophysical processes. Connects Dyson sphere searches and SETI to the competitive framework. | A98, A99, A100, A101 |
| The Survival Bottleneck Engineering Roadmap | science philosophy | Unselected A101 candidate. Detailed engineering requirements for the Type 0 to Type I transition. Covered adequately in A100 but could be expanded with specific technology roadmaps and quantitative risk reduction strategies. | A100 |
| Self-Replicating Technology Engineering | science philosophy | Unselected A101 candidate. Detailed engineering analysis of self-replicating machines and spacecraft. Von Neumann universal constructor, error correction, gray goo risk quantification. Implementation-focused rather than strategic. | A100, A101 |
| Governance Coherence Deep Dive | science philosophy | Unselected A101 candidate. Full treatment of governance coherence half-life, myth-structure transition, and institutional degradation at cosmic scales. A92 already covers this but the competitive context from A98-A101 would add depth. | A87, A89, A92, A100 |
| Economics of Competitive Expansion | science philosophy | Unselected A101 candidate. Resource allocation, opportunity costs, and economic optimization under competitive expansion imperatives. Interesting but secondary to physical feasibility questions. | A98, A100 |
| First Contact Protocols Under Competitive Assumptions | science philosophy | Unselected A101 candidate. Decision-theoretic analysis of first contact under the competitive framework. Premature without knowing whether force projection is physically feasible, which A101 now addresses. | A98, A99, A101 |
