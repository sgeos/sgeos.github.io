---
layout: post
mathjax: true
comments: true
title: "History of SpaceX: Decomposability of Falcon, Dragon, Heavy, and Starship as Independently Valuable Rungs"
date: 2026-07-29 09:00:00 +0000
categories: history business aerospace
series: spacex_history
series_title: History of SpaceX
series_index: 5
---

<!-- A285 -->
<script>console.log("A285");</script>

This article is the fifth in the History of SpaceX series and treats the decomposability forcing-function condition that the [series opener][related_post_a281_spacex_framing] introduced as the fourth of seven forcing-function conditions in the seven-plus-three analytical framework. The decomposability condition requires that a mission-directed technology venture organize its development trajectory as a ladder of independently valuable rungs rather than as a single all-or-nothing terminal capability, so that each intermediate configuration produces revenue, capability, and organizational learning that support the subsequent rung. The article walks the SpaceX vehicle ladder through the Falcon 1 small-lift vehicle across the 2002 through 2009 development and operational period, the Falcon 9 medium-lift vehicle across the 2005 through drafting-date development and operational period spanning the v1.0, v1.1, Full Thrust, and Block 5 configurations, the Dragon 1 cargo spacecraft across the 2006 through 2020 development and operational period, the Falcon Heavy heavy-lift vehicle across the 2011 through drafting-date development and operational period, the Dragon 2 crew and cargo spacecraft across the 2014 through drafting-date development and operational period, the Starship and Super Heavy super-heavy-lift architecture across the 2016 through drafting-date development and testing period, the Merlin engine family across the 1A, 1B, 1C, 1C+, 1D, 1D+, and Vacuum variants, the Raptor engine family across the Raptor 1, Raptor 2, and Raptor 3 variants, and the Cape Canaveral SLC-40, Kennedy Space Center LC-39A, Vandenberg SLC-4E, and Boca Chica Starbase launch-site progression. The article contrasts the SpaceX decomposability pattern against three canonical negation cases including the Superconducting Super Collider single-configuration cancellation on October 21 1993 documented in the [Riordan Hoddeson Kolb 2015][book_riordan_hoddeson_kolb_2015] Tunnel Visions treatment, the Iridium single-arrangement bankruptcy filing on August 13 1999 following the March 12 1999 revenue shortfall documented in the [Bloomberg][ref_bloomberg] business coverage and the [Fine 1998][book_fine_1998] Clockspeed treatment of the vertical-integration case, and the International Thermonuclear Experimental Reactor single-structure multi-decade construction documented in the [ITER Organization][ref_iter_organization] program-status reports. The article draws on the primary-source aerospace-history literature including [Bilstein 1980][book_bilstein_1980] Stages to Saturn, [Bilstein 2001][book_bilstein_2001] Flight in America, [Chaikin 1994][book_chaikin_1994] A Man on the Moon, [Ezell and Ezell 1978][book_ezell_ezell_1978] The Partnership A History of the Apollo-Soyuz Test Project, [Heppenheimer 1999][book_heppenheimer_1999] The Space Shuttle Decision, [Launius 2004][book_launius_2004] Frontiers of Space Exploration, [Logsdon 1970][book_logsdon_1970] The Decision to Go to the Moon, [McCurdy 1994][book_mccurdy_1994] Inside NASA, [Kranz 2000][book_kranz_2000] Failure Is Not an Option, [Serling 1992][book_serling_1992] Legend and Legacy on the Boeing history, and [Newhouse 1982][book_newhouse_1982] The Sporty Game on the aerospace-industry competitive dynamics, in addition to the SpaceX-focused treatments in [Berger 2021][book_berger_2021] Liftoff, [Berger 2024][book_berger_2024] Reentry, [Vance 2015][book_vance_2015] Elon Musk, [Isaacson 2023][book_isaacson_2023] Elon Musk, [Fernholz 2018][book_fernholz_2018] Rocket Billionaires, and [Davenport 2018][book_davenport_2018] The Space Barons. The mission-oriented-innovation and public-innovation-strategy scholarly context draws on [Mazzucato 2013][book_mazzucato_2013] The Entrepreneurial State, [Mazzucato 2021][book_mazzucato_2021] Mission Economy, [Ruttan 2006][book_ruttan_2006] Is War Necessary for Economic Growth, [Weiss 2014][book_weiss_2014] America Inc, [Mowery and Rosenberg 1998][book_mowery_rosenberg_1998] Paths of Innovation, [Nelson 1993][book_nelson_1993] National Innovation Systems, and [Klepper 2016][book_klepper_2016] Experimental Capitalism. The article closes with an explicit pattern-extraction section stating the abstract decomposability mechanic in a form other informed readers can recognize in adjacent domains without naming any downstream application.

## The Decomposability Mapping Problem

The mapping problem for a comprehensive treatment of the decomposability condition in the SpaceX case is the question of which vehicle-family and subsystem-family decomposition enabled the SpaceX trajectory to sustain a multi-decade capability accumulation through a sequence of independently valuable rungs rather than through a single all-or-nothing terminal-capability program, and how the rung-by-rung revenue, capability, and organizational-learning realization at each intermediate configuration supported the subsequent rung development. The problem permits several formalizations depending on the analytical tradition consulted. The systems-engineering tradition from [Simon 1962][research_simon_1962] The Architecture of Complexity through [Alexander 1964][book_alexander_1964] Notes on the Synthesis of Form, [Baldwin and Clark 2000][book_baldwin_clark_2000] Design Rules The Power of Modularity, and the [INCOSE Systems Engineering Handbook][ref_incose_handbook] treats the decomposability property as the hierarchical-decomposition and modular-architecture configuration that enables the independent-development-and-integration of the constituent subsystems. The staged-development tradition from [Boehm 1988][research_boehm_1988] A Spiral Model of Software Development and Enhancement and the incremental-and-iterative-development literature treats the decomposability property as the staged-capability-realization configuration that enables the risk-managed development across the multi-year horizon. The technology-adoption tradition from [Rogers 1962][book_rogers_1962] Diffusion of Innovations through [Moore 1991][book_moore_1991] Crossing the Chasm treats the decomposability property as the market-segment-progression configuration that enables the market-development across the multi-decade adoption horizon. The real-options tradition from [Trigeorgis 1996][book_trigeorgis_1996] Real Options through [Dixit and Pindyck 1994][book_dixit_pindyck_1994] Investment Under Uncertainty treats the decomposability property as the option-value-generation configuration that enables the staged-investment across the multi-year uncertain horizon. The present article draws on all four traditions while adopting the mission-oriented-innovation framework the [series opener][related_post_a281_spacex_framing] established as the primary organizing structure.

The mapping problem admits several formalizations depending on the level of analysis adopted. At the subsystem level, the decomposability condition reflects the engine, structure, avionics, and propellant-system modularity that enables the independent-development-and-integration of the constituent subsystems. At the vehicle level, the condition reflects the vehicle-family decomposition into small-lift, medium-lift, heavy-lift, and super-heavy-lift configurations that enables the incremental capability progression. At the mission level, the condition reflects the mission-class decomposition into cargo, crew, national-security, geostationary-transfer, and interplanetary configurations that enables the incremental market progression. At the program level, the condition reflects the staged-development configuration that enables the risk-managed multi-decade capability accumulation across the vehicle and mission decomposition.

The general form of the decomposability causal-mapping problem can be stated compactly as follows. Let $R_i(t) = \{r_1, r_2, \ldots, r_N\}$ denote the set of rungs the venture $i$ has completed by time $t$, with each rung $r_n$ representing an independently valuable configuration that produces revenue, capability, and organizational-learning value. The decomposability condition requires

$$\forall r_n \in R_i(t) : V^{\text{rung}}(r_n) > V^{\text{development-cost}}(r_n)$$

with each rung's independent value exceeding its own development cost so that each rung is individually justifiable rather than justifiable only in terms of the terminal-capability value.

The rung-value decomposition can be written as

$$V^{\text{rung}}(r_n) = V^{\text{revenue}}(r_n) + V^{\text{capability}}(r_n) + V^{\text{learning}}(r_n) + V^{\text{option}}(r_n)$$

with each channel contributing distinct value at each rung. The revenue channel captures the commercial-and-government-contract revenue the rung generates. The capability channel captures the engineering-and-manufacturing capability the rung accumulates. The learning channel captures the organizational-and-technical learning the rung produces. The option channel captures the real-option value the rung creates for subsequent rung development.

The cumulative-capability accumulation across the rung sequence has the form

$$K_i(t) = K_i(0) + \sum_{n=1}^{N(t)} \Delta K(r_n)$$

with $\Delta K(r_n)$ the incremental capability the rung $r_n$ contributes. The SpaceX case exhibits substantial $\Delta K$ values across the Falcon 1, Falcon 9, Dragon, Falcon Heavy, and Starship rungs, with each rung contributing engine, structure, avionics, and operations capability.

The rung-to-rung capability-transfer efficiency may be written

$$\eta^{\text{transfer}}_{n \to n+1} = \frac{K^{\text{shared}}_{n \to n+1}}{K^{\text{total}}_{n}}$$

with the SpaceX case exhibiting substantial $\eta^{\text{transfer}}$ values across the rung boundaries reflecting the extensive subsystem-and-organizational-learning transfer.

The identification problem for the decomposability contribution to the SpaceX trajectory is the question of separating the decomposability effect from the confounding effects of the other six forcing-function conditions and the three capital-formation legs. The counterfactual differential takes the compact form

$$\Delta V_i^{\text{decomposability}}(t) = V_i^{\text{observed}}(t) - V_i^{\text{single-configuration counterfactual}}(t)$$

with the decomposability attribution equal to the difference between the observed cumulative value and the counterfactual cumulative value under the single-configuration scenario. The counterfactual specifications the article treats include a Falcon-1-only counterfactual in which the SpaceX firm terminates development at the small-lift configuration, a Falcon-9-only counterfactual in which the SpaceX firm terminates development at the medium-lift arrangement, and a direct-to-Starship counterfactual in which the SpaceX firm attempts the super-heavy-lift development without the intermediate Falcon 1, Falcon 9, Dragon, and Falcon Heavy rung progression.

The rung-transition survival function takes the form

$$S(t) = \exp\!\left(-\int_0^t \lambda^{\text{failure}}(r_n(s)) \, ds\right)$$

with $\lambda^{\text{failure}}(r_n)$ the hazard rate for the rung $r_n$ that depends on the technical, financial, and market conditions at each rung. The single-configuration all-or-nothing arrangement corresponds to the limit $S(t) \to 0$ under the catastrophic-failure scenario.

The rung-value expectation across the rung sequence can be written as

$$E[V^{\text{total}}] = \sum_{n=1}^{N} P(r_n \text{ completed}) \cdot V^{\text{rung}}(r_n) \cdot \prod_{k<n} P(r_k \text{ completed})$$

with the product term reflecting the conditional-dependency structure across the rung sequence.

The decomposability-advantage decomposition has the form

$$V^{\text{decomposability-advantage}} = E[V^{\text{decomposed}}] - E[V^{\text{single-configuration}}] - C^{\text{coordination}}$$

with $C^{\text{coordination}}$ the coordination cost across the rung sequence.

## Methodological Commitments

The article commits to the same seven methodological positions that the [series opener][related_post_a281_spacex_framing] established for the series as a whole. These commitments are restated here at compact reference level.

The first commitment is descriptive-analytical framing rather than prescriptive advocacy.

The second commitment is dual-register composition with both general-history and abstract-mechanic registers.

The third commitment is primary-source anchoring. The article cites primary sources for each substantive claim with preference for [NASA Technical Reports Server][ref_nasa_ntrs] documents, [FAA AST current licenses database][ref_faa_ast] records, [FCC filings database][ref_fcc_filings] records including the Starlink authorizations, [SpaceX news archive][ref_spacex_news_archive] press releases, the [SpaceX Falcon 9 User's Guide][ref_spacex_booster_reuse_stats], the [SpaceX Falcon Heavy User's Guide][ref_spacex_falcon_heavy_users_guide], the [SpaceX Starship User's Guide][ref_spacex_starship_users_guide], the [NASA COTS Space Act Agreement August 18 2006][ref_nasa_cots_saa_2006], the [NASA CCtCap Contract September 16 2014][ref_nasa_cctcap_2014], the [NASA HLS Option A Award April 16 2021][ref_nasa_hls_option_a_2021], the [NASA HLS Option B Award November 15 2022][ref_nasa_hls_option_b_2022], the [GAO 2014 Commercial Crew Transportation Report][ref_gao_2014_commercial_crew], the [GAO 2021 NASA Human Landing System Program Report][ref_gao_hls_bid_protest_2021], the [NASA Office of the Inspector General Reports][ref_nasa_oig_reports] on the SpaceX-related programs, and secondary sources including [Berger 2021][book_berger_2021] Liftoff and [Berger 2024][book_berger_2024] Reentry. The article additionally draws on the trade-press coverage in [SpaceNews][ref_spacenews], [Ars Technica Space][ref_arstechnica_space], [NASASpaceflight][ref_nasaspaceflight], [Payload][ref_payload], [Payload Research][ref_payload_research], [Aviation Week][ref_aviation_week], [Defense News][ref_defense_news], [Breaking Defense][ref_breaking_defense], [Space Policy Online][ref_space_policy_online], [The Space Review][ref_the_space_review], and [European Spaceflight][ref_european_spaceflight].

The fourth commitment is contested-claim marking, with attention to the Starship development-cost and reusability-cadence estimates that the private-firm status renders substantially reconstructive rather than directly documented.

The fifth commitment is temporal indexing as a mid-2026 snapshot. The broader institutional-context documents relevant to the decomposability configuration include the [NASA Space Act Agreements Guide][ref_nasa_saa_guide], the [ITAR 22 CFR 120 through 130][ref_itar_22_cfr_120_130], the [ITU Radio Regulations 2020][ref_itu_radio_regulations_2020], the [Space Force National Security Space Launch][ref_space_force_nssl] framework, the [FAA Office of Commercial Space Transportation][ref_faa_ast] licensing regime, the [Commercial Space Launch Act 1984][ref_csla_1984], the [Commercial Space Launch Amendments Act 2004][ref_csla_amendments_2004], and the [United States Commercial Space Launch Competitiveness Act 2015][ref_uscsla_2015].

The sixth commitment is terminological transparency with the Terminological Note section below.

The seventh commitment is thesis-not-proof framing of the decomposability closure claim.

## Decomposability as an Economic Property

The decomposability property is treated in the article as an economic and organizational property of a firm's development trajectory that distinguishes ventures organized as a ladder of independently valuable rungs from ventures organized as a single all-or-nothing terminal-capability program. The property has formal characterizations that admit measurement, comparison across firms and sectors, and identification of the organizational and technical arrangements that enable or preclude the property.

The formal characterization of the decomposability property permits several compact statements. Let $R_i(t)$ denote the set of rungs completed by firm $i$ at time $t$, and let $V^{\text{rung}}(r_n)$ denote the independent value the rung $r_n$ generates. The decomposability condition requires

$$V^{\text{rung}}(r_n) \geq V^{\text{threshold}} \quad \forall r_n \in R_i(t)$$

with $V^{\text{threshold}}$ the threshold above which each rung is individually justifiable rather than justifiable only through the terminal-capability value. The SpaceX case exhibits substantial $V^{\text{rung}}$ values across the Falcon 1, Falcon 9, Dragon, Falcon Heavy, and Starship rungs, with each rung realizing revenue, capability, and learning value that exceeded its own development cost.

The rung-independent-viability test may be written

$$V^{\text{rung}}(r_n) - I^{\text{development}}(r_n) - I^{\text{shared-infrastructure attribution}}(r_n) > 0$$

with the shared-infrastructure-attribution term reflecting the overhead-allocation across the rung sequence. The test result is satisfied for the Falcon 9, Dragon 1, Dragon 2, and Falcon Heavy rungs under the reasonable overhead-allocation assumptions.

The rung-progression dynamics admit the compact form

$$\text{Prob}(r_{n+1} \mid r_n) = g(V^{\text{rung}}(r_n), K^{\text{accumulated}}(r_1, \ldots, r_n), \Pi^{\text{external}}(t))$$

with the conditional probability of transitioning to the subsequent rung determined by the value realized at the current rung, the accumulated capability across the completed rungs, and the external factors including market conditions and capital availability. The SpaceX case exhibits high transition probabilities across the Falcon 1 to Falcon 9 to Falcon Heavy to Starship progression, with each rung transition supported by the accumulated capability and the realized rung value.

The rung-transition-time distribution admits the compact form

$$T^{\text{transition}}_{n \to n+1} \sim \text{LogNormal}(\mu^{\text{transition}}_n, \sigma^{\text{transition}}_n)$$

with the log-normal parameters reflecting the technological, financial, and market conditions at the transition period.

The decomposition-quality index takes the form

$$D_i = \frac{1}{N} \sum_{n=1}^{N} \frac{V^{\text{rung}}(r_n)}{V^{\text{development-cost}}(r_n)}$$

with $D_i$ exceeding unity indicating that the rung decomposition enables individually justifiable rung development across the rung sequence. The SpaceX case exhibits $D_i$ values substantially exceeding unity, reflecting the rung-by-rung revenue realization from the Falcon 9 commercial-launch and NASA-cargo revenue, the Falcon Heavy commercial-launch and defense-launch revenue, and the Dragon crew-and-cargo NASA revenue.

The modularity index can be written as

$$M_i = \frac{\sum_{s \in \text{subsystems}} \omega_s \cdot \phi^{\text{reuse}}_{s}}{\sum_{s \in \text{subsystems}} \omega_s}$$

with $\phi^{\text{reuse}}_{s}$ the fraction of the subsystem $s$ that is reused across multiple rungs and $\omega_s$ the weight indicating the subsystem's contribution to the overall vehicle configuration. The SpaceX case exhibits high $M_i$ values reflecting the Merlin engine reuse across the Falcon 1, Falcon 9, and Falcon Heavy vehicles, the Dragon 1 to Dragon 2 subsystem reuse, and the structural and avionics reuse across the vehicle family.

The subsystem-interface-count has the form

$$N^{\text{interfaces}}_i = \binom{n^{\text{subsystems}}}{2} \cdot \phi^{\text{connected}}_{i}$$

with $\phi^{\text{connected}}_{i}$ the fraction of subsystem-pairs that share the direct interface. The SpaceX case exhibits substantial subsystem-interface-count reduction relative to the analog aerospace-industry baseline reflecting the integrated-architecture configuration.

The staged-investment option value may be written

$$V^{\text{option}}(r_{n+1}) = \max(0, V^{\text{expected}}(r_{n+1}) - I(r_{n+1}))$$

with $V^{\text{expected}}(r_{n+1})$ the expected value of the subsequent rung conditional on the current rung completion and $I(r_{n+1})$ the investment cost of the subsequent rung. The real-options valuation permits the extended form

$$V^{\text{total}}(r_n) = V^{\text{current}}(r_n) + \max(0, V^{\text{option-to-continue}}(r_n) - I^{\text{option-exercise}}(r_n))$$

with the option-to-continue value depending on the technological, market, and capital-market conditions at the decision point.

The Bellman-recursion form of the staged-investment value permits the concise form

$$V^{\ast}(r_n) = \max\!\left\{V^{\text{stop}}(r_n), \; V^{\text{continue}}(r_n) - I(r_{n+1}) + \delta \cdot E[V^{\ast}(r_{n+1})]\right\}$$

with $\delta$ the discount factor and the $\max$ operator reflecting the option-to-continue-or-stop at each rung.

The capability-accumulation trajectory admits the compact continuous-time form

$$\dot K_i(t) = \eta \cdot I^{\text{development}}(t) + \mu \cdot L(t) \cdot K_i(t) - \delta \cdot K_i(t)$$

with $\eta$ the investment-to-capability conversion coefficient, $\mu$ the learning coefficient, $L(t)$ the learning intensity, and $\delta$ the capability-depreciation rate.

The rung-sequence completion probability under the decomposed configuration takes the form

$$P^{\text{decomposed}}(\text{complete } r_N) = \prod_{n=1}^{N} p_n^{\text{rung-success}} \geq P^{\text{single-configuration}}(\text{complete})$$

with the rung-by-rung success probabilities $p_n^{\text{rung-success}}$ typically substantially exceeding the single-configuration success probability under the same-technology-risk assumption.

The option-value under the Black-Scholes-Merton framework can be written as

$$V^{\text{option}} = V^{\text{expected}} \cdot \Phi(d_1) - I \cdot e^{-r T} \cdot \Phi(d_2)$$

with $\Phi$ the standard-normal cumulative distribution function, $d_1$ and $d_2$ the standardized drift-and-volatility parameters, $r$ the risk-free rate, and $T$ the time-to-decision.

## Cross-Disciplinary Framings

The decomposability property draws characterization from several disciplinary traditions beyond the mission-oriented-innovation framework the series adopts as primary.

The systems-architecture tradition traces from [Simon 1962][research_simon_1962] The Architecture of Complexity through [Alexander 1964][book_alexander_1964] Notes on the Synthesis of Form, [Baldwin and Clark 2000][book_baldwin_clark_2000] Design Rules The Power of Modularity, [Ulrich 1995][research_ulrich_1995] The Role of Product Architecture in the Manufacturing Firm, [Sanchez and Mahoney 1996][research_sanchez_mahoney_1996] Modularity Flexibility and Knowledge Management in Product and Organization Design, [Sosa Eppinger Rowles 2003][research_sosa_eppinger_rowles_2003] Identifying Modular and Integrative Systems and their Impact on Design Team Interactions, [MacCormack Baldwin Rusnak 2012][research_maccormack_baldwin_rusnak_2012] Exploring the Duality between Product and Organizational Architectures, [Fixson 2005][research_fixson_2005] Product Architecture Assessment A Tool to Link Product Manufacturing Supply Chain and Service Decisions, [Baldwin and Woodard 2009][research_baldwin_woodard_2009] The Architecture of Platforms A Unified View, [Suh 2001][book_suh_2001] Axiomatic Design, [Ethiraj and Levinthal 2004][research_ethiraj_levinthal_2004] Modularity and Innovation in Complex Systems, [Rivkin and Siggelkow 2003][research_rivkin_siggelkow_2003] Balancing Search and Stability Interdependencies Among Elements of Organizational Design, [Kauffman 1993][book_kauffman_1993] The Origins of Order, and [Sanchez 1995][research_sanchez_1995] Strategic Flexibility in Product Competition. The framing treats the decomposability property through the hierarchical-decomposition and modular-architecture configuration that enables the independent-development-and-integration of the constituent subsystems. The SpaceX vehicle-family decomposition into small-lift, medium-lift, heavy-lift, and super-heavy-lift configurations reflects the hierarchical-decomposition principles that support the rung-by-rung capability progression. The modular-architecture index has the form

$$MA_i = \frac{\sum_{s} c^{\text{internal}}_{s}}{\sum_{s,t} c^{\text{internal}}_{s} + c^{\text{external}}_{s,t}}$$

with $c^{\text{internal}}_{s}$ the intra-subsystem coupling and $c^{\text{external}}_{s,t}$ the inter-subsystem coupling that jointly determine the modular-architecture strength.

The Simon nearly-decomposable hierarchical-system decomposition may be written

$$T^{\text{system-dynamics}} = T^{\text{intra-module-dynamics}} \oplus T^{\text{inter-module-dynamics}}$$

with the nearly-decomposable configuration admitting the approximate separation of the intra-module and inter-module dynamics on the different time-scales.

The staged-development tradition traces from [Boehm 1988][research_boehm_1988] A Spiral Model of Software Development and Enhancement through the incremental-and-iterative-development literature including [Beck 1999][book_beck_1999] Extreme Programming Explained, [Schwaber 2004][book_schwaber_2004] Agile Project Management with Scrum, [Boehm and Turner 2003][book_boehm_turner_2003] Balancing Agility and Discipline, [Poppendieck and Poppendieck 2003][book_poppendieck_2003] Lean Software Development, and the NASA staged-development frameworks documented in the [NASA Systems Engineering Handbook][ref_nasa_se_handbook] and the [NASA Program and Project Life Cycle Requirements NPR 7120.5F][ref_nasa_npr_7120_5f]. The framing treats the decomposability property through the staged-capability-realization configuration that enables the risk-managed development across the multi-year horizon. The SpaceX Falcon 9 progression through the v1.0, v1.1, Full Thrust, and Block 5 configurations reflects the staged-development principles that support the incremental capability improvement across the ten-year development horizon. The staged-development risk-reduction identity yields the compact form

$$R^{\text{residual}}_n = R^{\text{initial}} \cdot \prod_{k=1}^{n} (1 - \Delta R_k^{\text{resolution}})$$

with $\Delta R_k^{\text{resolution}}$ the risk-resolution fraction realized at the rung $k$ so that the residual risk decreases geometrically across the rung sequence.

The technology-adoption tradition traces from [Rogers 1962][book_rogers_1962] Diffusion of Innovations through [Moore 1991][book_moore_1991] Crossing the Chasm, [Christensen 1997][book_christensen_1997] The Innovator's Dilemma, [Christensen and Raynor 2003][book_christensen_raynor_2003] The Innovator's Solution, [Utterback 1994][book_utterback_1994] Mastering the Dynamics of Innovation, [Foster 1986][book_foster_1986] Innovation The Attackers Advantage, [Bower and Christensen 1995][research_bower_christensen_1995] Disruptive Technologies Catching the Wave, [Klepper 1996][research_klepper_1996] Entry Exit Growth and Innovation over the Product Life Cycle, [Klepper 2010][research_klepper_2010] The Origin and Growth of Industry Clusters, [Adner 2012][book_adner_2012] The Wide Lens, [Adner and Kapoor 2010][research_adner_kapoor_2010] Value Creation in Innovation Ecosystems, and [Anderson 2023][book_anderson_2023] The Space Economy. The framing treats the decomposability property through the market-segment-progression configuration that enables the market-development across the multi-decade adoption horizon. The SpaceX mission-class progression through the cargo, crew, national-security, geostationary-transfer, and interplanetary configurations reflects the market-segment-progression principles that support the incremental market development. The Bass diffusion equation takes the form

$$\frac{dN(t)}{dt} = \left[p + q \cdot \frac{N(t)}{m}\right] \cdot [m - N(t)]$$

with $p$ the innovation coefficient, $q$ the imitation coefficient, $m$ the market potential, and $N(t)$ the cumulative adoption by time $t$.

The real-options tradition traces from [Trigeorgis 1996][book_trigeorgis_1996] Real Options through [Dixit and Pindyck 1994][book_dixit_pindyck_1994] Investment Under Uncertainty, [Myers 1977][research_myers_1977] Determinants of Corporate Borrowing, [Black and Scholes 1973][research_black_scholes_1973] The Pricing of Options and Corporate Liabilities, [Merton 1973][research_merton_1973] Theory of Rational Option Pricing, [McDonald and Siegel 1986][research_mcdonald_siegel_1986] The Value of Waiting to Invest, and [Copeland and Antikarov 2001][book_copeland_antikarov_2001] Real Options A Practitioners Guide. The framing treats the decomposability property through the option-value-generation configuration that enables the staged-investment across the multi-year uncertain horizon. The SpaceX Falcon 1 to Falcon 9 transition and Falcon 9 to Falcon Heavy transition reflect the option-exercise decisions supported by the capability accumulation and market development at each intermediate rung. The compound-option valuation across the rung sequence admits the compact recursive form

$$V^{\text{compound}}(r_n) = \max\!\left(0, V^{\text{underlying}}(r_n) + V^{\text{compound}}(r_{n+1}) - I(r_{n+1})\right)$$

with the compound-option value at rung $n$ depending recursively on the option value at rung $n+1$.

The dynamic-capabilities tradition traces from [Teece Pisano Shuen 1997][research_teece_pisano_shuen_1997] Dynamic Capabilities and Strategic Management through [Eisenhardt and Martin 2000][research_eisenhardt_martin_2000] Dynamic Capabilities What Are They, [Pisano 2015][research_pisano_2015] You Need an Innovation Strategy, [Teece 2007][research_teece_2007] Explicating Dynamic Capabilities The Nature and Microfoundations of Sustainable Enterprise Performance, [Helfat and Peteraf 2003][research_helfat_peteraf_2003] The Dynamic Resource-Based View, [Winter 2003][research_winter_2003] Understanding Dynamic Capabilities, [Barney 1991][research_barney_1991] Firm Resources and Sustained Competitive Advantage, [Wernerfelt 1984][research_wernerfelt_1984] A Resource-Based View of the Firm, [Peteraf 1993][research_peteraf_1993] The Cornerstones of Competitive Advantage, [Penrose 1959][book_penrose_1959] The Theory of the Growth of the Firm, [Nelson and Winter 1982][book_nelson_winter_1982] An Evolutionary Theory of Economic Change, [Chandler 1962][book_chandler_1962] Strategy and Structure, [Chandler 1977][book_chandler_1977] The Visible Hand, and [Chandler 1990][book_chandler_1990] Scale and Scope. The framing treats the decomposability property through the capability-reconfiguration dynamics that enable the rung-by-rung capability progression. The SpaceX engineering, manufacturing, and operations capability reconfiguration across the Falcon 1, Falcon 9, Dragon, Falcon Heavy, and Starship rungs reflects the dynamic-capabilities principles that support the multi-decade capability accumulation. The dynamic-capabilities decomposition can be written as

$$DC_i = \alpha^{\text{sense}} \cdot S_i + \alpha^{\text{seize}} \cdot Z_i + \alpha^{\text{reconfigure}} \cdot R_i$$

with the sense, seize, and reconfigure components each weighted by the coefficients that reflect the configuration of the dynamic-capabilities arrangement.

The absorptive-capacity tradition traces from [Cohen and Levinthal 1990][research_cohen_levinthal_1990] Absorptive Capacity A New Perspective on Learning and Innovation through [Zahra and George 2002][research_zahra_george_2002] Absorptive Capacity A Review Reconceptualization and Extension, [Lane Koka Pathak 2006][research_lane_koka_pathak_2006] The Reification of Absorptive Capacity, [Todorova and Durisin 2007][research_todorova_durisin_2007] Absorptive Capacity Valuing a Reconceptualization, [Volberda Foss Lyles 2010][research_volberda_foss_lyles_2010] Absorbing the Concept of Absorptive Capacity, and [Zahra 2015][research_zahra_2015] Corporate Entrepreneurship as Knowledge Creation and Conversion. The framing treats the decomposability property through the organizational-learning dynamics that enable the capability-transfer across the rung sequence. The SpaceX Merlin engine learning transferred across the Falcon 1, Falcon 9, and Falcon Heavy configurations, the Dragon 1 spacecraft learning transferred to the Dragon 2 arrangement, and the Falcon reusability learning transferred to the Starship recovery development each reflect the absorptive-capacity principles. The absorptive-capacity index has the form

$$AC_i = \phi\!\left(K_i^{\text{prior}}, D_i^{\text{diversity}}, I_i^{\text{research-intensity}}\right)$$

with the prior-knowledge stock, the knowledge-diversity, and the research-intensity jointly determining the absorptive-capacity level.

The organizational-learning tradition traces from [Argote 1999][book_argote_1999] Organizational Learning through [Argote and Miron-Spektor 2011][research_argote_miron_spektor_2011] Organizational Learning From Experience to Knowledge, [Levitt and March 1988][research_levitt_march_1988] Organizational Learning, [March 1991][research_march_1991] Exploration and Exploitation in Organizational Learning, [Nonaka 1994][research_nonaka_1994] A Dynamic Theory of Organizational Knowledge Creation, [Nonaka and Takeuchi 1995][book_nonaka_takeuchi_1995] The Knowledge-Creating Company, [Argyris and Schon 1978][book_argyris_schon_1978] Organizational Learning A Theory of Action Perspective, [Senge 1990][book_senge_1990] The Fifth Discipline, [Argote and Ingram 2000][research_argote_ingram_2000] Knowledge Transfer A Basis for Competitive Advantage in Firms, [Kogut and Zander 1992][research_kogut_zander_1992] Knowledge of the Firm Combinative Capabilities and the Replication of Technology, [Grant 1996][research_grant_1996] Toward a Knowledge-Based Theory of the Firm, and [Wright 1936][research_wright_1936] Factors Affecting the Cost of Airplanes. The framing treats the decomposability property through the learning-curve dynamics that enable the cost-and-capability improvement across the rung sequence. The SpaceX Falcon 9 launch-cadence progression from the 2013 initial operational cadence through the 2024 approximately-140-launch-per-year cadence reflects the learning-curve dynamics that support the decomposability configuration. The Wright learning-curve equation admits the compact power-law form

$$C(n) = C(1) \cdot n^{-b}, \quad b = -\frac{\log_2 \rho^{\text{learning}}}{1}$$

with $\rho^{\text{learning}}$ the learning rate at cumulative production $n$ and $C(1)$ the first-unit cost.

The lean-manufacturing tradition traces from [Womack Jones Roos 1990][book_womack_jones_roos_1990] The Machine That Changed the World through [Liker 2004][book_liker_2004] The Toyota Way, [Ohno 1988][book_ohno_1988] Toyota Production System, [Womack and Jones 2003][book_womack_jones_2003] Lean Thinking, [Shingo 1989][book_shingo_1989] A Study of the Toyota Production System, [Fine 1998][book_fine_1998] Clockspeed Winning Industry Control in the Age of Temporary Advantage, [Hounshell 1984][book_hounshell_1984] From the American System to Mass Production, [Meyer and Lehnerd 1997][book_meyer_lehnerd_1997] The Power of Product Platforms, [Sanderson and Uzumeri 1997][book_sanderson_uzumeri_1997] Managing Product Families, and [Robertson and Ulrich 1998][research_robertson_ulrich_1998] Planning for Product Platforms. The framing treats the decomposability property through the production-flexibility and product-family-decomposition principles that enable the efficient-manufacturing across the rung sequence. The SpaceX vertical-manufacturing configuration at the Hawthorne facility reflects the lean-manufacturing principles adapted to the launch-vehicle production arrangement. The takt-time identity may be written

$$T^{\text{takt}} = \frac{T^{\text{available}}}{D^{\text{demand}}}$$

with $T^{\text{available}}$ the available production time and $D^{\text{demand}}$ the demand rate that jointly determine the target-cycle-time per unit.

## The Falcon 1 Small-Lift Vehicle 2002 through 2009

The Falcon 1 small-lift vehicle constitutes the first rung of the SpaceX vehicle-family decomposition. The Falcon 1 development period spans the March 14 2002 SpaceX founding through the July 14 2009 fifth and final Falcon 1 launch, a seven-year period that encompasses the initial engine-development, structure-development, avionics-development, and launch-operations-development that established the engineering-and-manufacturing capability base for the subsequent Falcon 9 development. The Falcon 1 development period is comprehensively documented in [Berger 2021][book_berger_2021] Liftoff, [Vance 2015][book_vance_2015] Elon Musk The Falcon 1 Launch Vehicle Demonstration Flights Status and Future Plans Falcon Launch Vehicles An Overview, [Isaacson 2023][book_isaacson_2023] Elon Musk, the historical [SpaceX press releases][ref_spacex_news_archive] archived across the 2002 through 2009 period, and the archived [Kwajalein Atoll USAKA Historical Documentation][ref_kwajalein_atoll_documentation] on the Omelek Island launch operations.

The Falcon 1 vehicle configuration comprises the two-stage kerosene-and-liquid-oxygen arrangement with the Merlin 1A first-stage engine and the Kestrel second-stage engine. The vehicle mass allows the brief statement of approximately 30,000 kilograms at liftoff with the approximately 670-kilogram payload capability to low-Earth orbit. The Falcon 1 vehicle first-stage propellant mass is approximately 25,000 kilograms with the Merlin 1A thrust of approximately 340,000 newtons at sea level. The vehicle configuration is documented in the archived Falcon 1 User's Guide as reconstructed in the [SpaceX news archive][ref_spacex_news_archive] and the technical treatment in [Sutton and Biblarz 2010][book_sutton_biblarz_2010] Rocket Propulsion Elements, [Humble Henry Larson 1995][book_humble_henry_larson_1995] Space Propulsion Analysis and Design, [Turner 2008][book_turner_2008] Rocket and Spacecraft Propulsion, and [Wertz and Larson 1999][book_wertz_larson_1999] Space Mission Analysis and Design.

The Tsiolkovsky rocket equation takes the compact form

$$\Delta v = v_e \cdot \ln\!\left(\frac{m_0}{m_f}\right) = I_{sp} \cdot g_0 \cdot \ln\!\left(\frac{m_0}{m_f}\right)$$

with $v_e$ the effective exhaust velocity, $I_{sp}$ the specific impulse, $g_0$ the standard gravitational acceleration, $m_0$ the initial mass, and $m_f$ the final mass. The Falcon 1 configuration allows approximately $\Delta v \approx 9,000$ meters per second summed across the first and second stages.

The specific thrust-to-weight ratio at liftoff takes the form

$$TWR = \frac{F^{\text{thrust}}}{m_0 \cdot g_0}$$

with the Falcon 1 liftoff TWR of approximately 1.16 reflecting the mission-marginal thrust-to-weight configuration.

The payload-fraction identity can be written as

$$\pi^{\text{payload}} = \frac{m^{\text{payload}}}{m_0} = \prod_{i=1}^{n^{\text{stages}}} \left(\frac{m_f^{(i)}}{m_0^{(i)}}\right)$$

with the Falcon 1 payload fraction of approximately 0.022 reflecting the two-stage configuration.

The Falcon 1 launch sequence comprises five launches across the March 24 2006 through July 14 2009 period, documented in the [SpaceX news archive][ref_spacex_news_archive] press releases and the [Berger 2021][book_berger_2021] Liftoff historical treatment. The launches are the Flight 1 on March 24 2006 that failed at approximately 25 seconds due to a fuel-line leak, the Flight 2 on March 21 2007 that reached orbit but experienced roll-instability that precluded orbital-insertion, the Flight 3 on August 3 2008 that failed at approximately two minutes due to recontact between the separating first stage and the second stage, the Flight 4 on September 28 2008 that successfully reached orbit as the first privately-developed orbital-class launch vehicle, and the Flight 5 on July 14 2009 that successfully deployed the RazakSAT satellite as the first commercial Falcon 1 mission.

The Falcon 1 launch-success rate across the five-flight sample has the form

$$p^{\text{success}}_{F1} = \frac{n^{\text{successes}}}{n^{\text{attempts}}} = \frac{2}{5} = 0.40$$

with the Bayesian posterior success-rate estimate substantially higher given the late-flight learning-curve pattern and the successful concluding flights.

The Falcon 1 rung-value analysis has the concise statement of the approximately 100 million dollar investment across the 2002 through 2009 development-and-operational period against the approximately 15 million dollars in launch-service revenue realized from the RazakSAT commercial mission and the various sub-orbital and demonstration missions. The rung-value gap between the approximately 100 million dollar investment and the approximately 15 million dollar revenue realization reflects the capability-and-learning value the Falcon 1 rung produced independent of the direct revenue. The capability-and-learning value manifests in the Merlin engine base configuration that transferred to the Merlin 1C and Merlin 1D arrangements for the Falcon 9 vehicle, the vehicle-integration and launch-operations capability that transferred to the Falcon 9 launch operations, and the organizational learning that transferred to the Falcon 9 program management.

The capability-transfer efficiency from the Falcon 1 rung to the Falcon 9 rung may be written

$$\eta^{\text{transfer}}_{F1 \to F9} = \frac{\Delta K^{\text{Falcon 9}}_{\text{from-Falcon 1}}}{K^{\text{Falcon 1}}_{\text{total}}}$$

with $\eta^{\text{transfer}}$ substantially exceeding zero reflecting the substantial subsystem, engineering, and organizational-learning transfer across the rung boundary.

The rung-value ratio for the Falcon 1 rung admits the compact form

$$\rho^{\text{Falcon 1}} = \frac{V^{\text{revenue}}_{F1} + V^{\text{capability-transfer}}_{F1 \to F9}}{I^{\text{development}}_{F1}}$$

with the $\rho^{\text{Falcon 1}}$ substantially exceeding unity when the capability-transfer value is properly attributed to the Falcon 1 rung.

## The Falcon 9 Medium-Lift Vehicle 2005 through Drafting Date

The Falcon 9 medium-lift vehicle constitutes the second rung of the SpaceX vehicle-family decomposition and the primary revenue-generating rung across the contemporary period. The Falcon 9 development period spans the 2005 initial concept-definition through the June 4 2010 first flight and the subsequent v1.0, v1.1, Full Thrust, and Block 5 configuration progression across the 2010 through drafting-date period. The Falcon 9 development is documented in [Berger 2024][book_berger_2024] Reentry, the [SpaceX Falcon 9 User's Guide][ref_spacex_booster_reuse_stats], the [NASA COTS Space Act Agreement August 18 2006][ref_nasa_cots_saa_2006] and the derivative CRS-1 contract, the [Anadol Cohen Ferrari 2018][ref_hbs_spacex_case] SpaceX Case Study, and the contemporary trade-press coverage in [SpaceNews][ref_spacenews], [Ars Technica Space][ref_arstechnica_space], and [NASASpaceflight][ref_nasaspaceflight].

The Falcon 9 v1.0 configuration comprises the two-stage kerosene-and-liquid-oxygen arrangement with the nine Merlin 1C first-stage engines and the single Merlin 1C Vacuum second-stage engine. The vehicle mass permits the concise statement of approximately 335,000 kilograms at liftoff with the approximately 10,450-kilogram payload capability to low-Earth orbit. The Falcon 9 v1.0 first-stage propellant mass is approximately 245,000 kilograms with the nine-Merlin-1C thrust of approximately 4.94 million newtons at sea level. The Falcon 9 v1.0 launch sequence comprises the five flights across the June 4 2010 through March 1 2013 period with the configuration retiring in favor of the v1.1 arrangement.

The Falcon 9 v1.1 configuration comprises the stretched two-stage arrangement with the nine Merlin 1D first-stage engines in the octaweb structure and the single Merlin 1D Vacuum second-stage engine. The vehicle mass yields the compact statement of approximately 505,000 kilograms at liftoff with the approximately 13,150-kilogram payload capability to low-Earth orbit. The Falcon 9 v1.1 first flight occurred on September 29 2013.

The Falcon 9 v1.0 to v1.1 mass-fraction improvement takes the form

$$\pi^{\text{improvement}}_{v1.0 \to v1.1} = \frac{\pi^{\text{payload}}_{v1.1}}{\pi^{\text{payload}}_{v1.0}} \approx 1.26$$

reflecting the approximately 26 percent payload-fraction improvement from the v1.0 to v1.1 configuration transition supported by the Merlin 1C to Merlin 1D engine transition.

The Falcon 9 Full Thrust configuration comprises the December 22 2015 debut arrangement with the first successful first-stage landing on the Landing Zone 1 at Cape Canaveral. The vehicle mass allows the brief statement of approximately 549,000 kilograms at liftoff with the approximately 22,800-kilogram payload capability to low-Earth orbit in the expendable configuration or approximately 15,600 kilograms in the reusable arrangement.

The reusability-payload-penalty can be written as

$$\Delta m^{\text{payload}}_{\text{reuse}} = m^{\text{payload}}_{\text{expendable}} - m^{\text{payload}}_{\text{reusable}} \approx 7,200 \text{ kg}$$

reflecting the approximately 32 percent payload-penalty for the first-stage-recovery configuration relative to the expendable arrangement.

The Falcon 9 Block 5 configuration comprises the May 11 2018 debut arrangement with the design-for-reuse enhancements that support the rapid-turnaround reusability. The Block 5 configuration achieved the ten-flight reusability threshold on the approximately-30-flight per-booster limit and the approximately-140-launch per-year annual cadence by the drafting date. The Block 5 reusability trajectory is documented in the [FAA AST current licenses database][ref_faa_ast], the [SpaceX news archive][ref_spacex_news_archive] press releases, the contemporary [Payload Research][ref_payload_research] launch-cadence analysis, and the [SpaceX Booster Reuse Statistics][ref_spacex_booster_reuse_stats] operational records.

The Falcon 9 launch-cadence progression admits the compact fitted form

$$N^{\text{launches}}(t) = N_0 \cdot e^{g \cdot (t - t_0)}$$

with $g$ the growth rate approximately 0.35 per year across the 2013 through 2024 operational period. The reusability-cost-reduction identity has the form

$$C^{\text{amortized}}(k) = \frac{C^{\text{manufacture}} + k \cdot C^{\text{refurbishment}}}{k+1}$$

with $k$ the number of reflights per booster so that the amortized cost per launch decreases with the reuse-count. The Falcon 9 Block 5 configuration supports approximately $k \approx 20$ reflights per booster with the amortized-cost of approximately 15 million dollars per launch against the approximately 60 million dollar manufacturing cost.

The block-progression capability index may be written

$$K^{\text{block}}_n = K^{\text{block}}_{n-1} \cdot (1 + \Delta^{\text{improvement}}_n)$$

with the block-by-block capability improvement $\Delta^{\text{improvement}}_n$ approximately 0.15 across the v1.0 to v1.1 to Full Thrust to Block 5 progression.

The Falcon 9 rung-value analysis takes the compact statement of the approximately 400 million dollar development investment through the 2010 first flight against the approximately 5 billion dollars in cumulative launch-service revenue across the 2010 through drafting-date operational period. The rung-value ratio of approximately 12.5 substantially exceeds unity, reflecting the commercial-viability of the Falcon 9 rung as an independently justifiable configuration. The commercial-viability assessment draws on the [Wall Street Journal][ref_wsj] and the [Bloomberg][ref_bloomberg] business coverage, and the NASA COTS Phase 1 and COTS Phase 2 procurement records in the [NASA COTS Final Report 2014][ref_nasa_cots_final_report_2014].

The Falcon 9 launch-service-price trajectory has the concise form

$$P^{\text{launch}}(t) = P_0 \cdot e^{-\beta^{\text{learning}} \cdot t}$$

with $\beta^{\text{learning}}$ the price-decay rate reflecting the learning-and-reusability cost-reduction across the operational period.

## The Dragon 1 Cargo Spacecraft 2006 through 2020

The Dragon 1 cargo spacecraft constitutes the third rung of the SpaceX vehicle-family decomposition and the first spacecraft development within the SpaceX portfolio. The Dragon 1 development period spans the 2006 initial concept-definition following the August 18 2006 [COTS Space Act Agreement award][ref_nasa_cots_saa_2006] through the December 8 2010 first flight and the subsequent Cargo Resupply Services operational period across the October 8 2012 through April 7 2020 final Dragon 1 mission. The Dragon 1 development is comprehensively documented in the [NASA COTS Final Report 2014][ref_nasa_cots_final_report_2014] and the [NASA CRS Program Overview][ref_nasa_crs_program_overview].

The Dragon 1 vehicle configuration comprises the pressurized-and-unpressurized cargo spacecraft arrangement with the approximately 6,000-kilogram launch mass and the approximately 3,310-kilogram pressurized-cargo capability. The Dragon 1 configuration is documented in the NASA CRS program documentation and the SpaceX press releases in the [SpaceX news archive][ref_spacex_news_archive].

The Dragon 1 cargo-delivery efficiency takes the form

$$\eta^{\text{cargo}}_{D1} = \frac{m^{\text{cargo}}_{\text{delivered}}}{m^{\text{launch}}_{D1}}$$

with the Dragon 1 cargo-delivery efficiency of approximately 0.55 reflecting the efficient mass-utilization of the spacecraft configuration.

The Dragon 1 rung-value analysis admits the compact statement of the approximately 300 million dollar development investment against the approximately 3.04 billion dollars in Cargo Resupply Services revenue across the 2008 through 2020 CRS-1 contract-execution period as the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] treats. The rung-value ratio of approximately 10 substantially exceeds unity, reflecting the commercial-viability of the Dragon 1 rung as an independently justifiable configuration.

The Dragon 1 mission-value identity can be written as

$$V^{\text{mission}}_{D1}(n) = P^{\text{price-per-mission}} \cdot n^{\text{missions}} + V^{\text{capability-transfer}}_{D1 \to D2}$$

with the capability-transfer value to the Dragon 2 configuration substantially augmenting the direct-mission-revenue value.

## The Falcon Heavy Heavy-Lift Vehicle 2011 through Drafting Date

The Falcon Heavy heavy-lift vehicle constitutes the fourth rung of the SpaceX vehicle-family decomposition and the heavy-lift capability expansion. The Falcon Heavy development period spans the April 5 2011 initial announcement through the February 6 2018 first flight and the subsequent operational period across the 2018 through drafting-date period. The Falcon Heavy program is documented in the [SpaceX Falcon Heavy User's Guide][ref_spacex_falcon_heavy_users_guide], the historical [SpaceX Falcon Heavy Press Release April 5 2011][ref_spacex_press_falcon_heavy_2011] announcement, the [SpaceX news archive][ref_spacex_news_archive] launch press releases, the [Space Force Falcon Heavy Certification Documentation][ref_space_force_nssl], the [Wall Street Journal][ref_wsj] coverage of the Arabsat-6A commercial mission, and the contemporary [SpaceNews][ref_spacenews], [NASASpaceflight][ref_nasaspaceflight], and [Aviation Week][ref_aviation_week] coverage.

The Falcon Heavy vehicle configuration comprises the three-Falcon-9-core arrangement with the twenty-seven Merlin 1D first-stage engines and the single Merlin 1D Vacuum second-stage engine. The vehicle mass permits the concise statement of approximately 1,420,000 kilograms at liftoff with the approximately 63,800-kilogram payload capability to low-Earth orbit in the expendable configuration.

The Falcon Heavy total-thrust identity has the form

$$F^{\text{FH}}_{\text{total}} = 3 \cdot F^{\text{F9-core}}_{\text{thrust}} = 3 \cdot 9 \cdot F^{\text{Merlin 1D}}_{\text{sea-level}}$$

with the approximately 22.8 million newtons total liftoff thrust reflecting the 27-engine parallel-staging configuration.

The parallel-staging payload-capability enhancement may be written

$$m^{\text{payload}}_{\text{FH}} = k^{\text{parallel-staging}} \cdot m^{\text{payload}}_{\text{F9}}$$

with $k^{\text{parallel-staging}} \approx 2.8$ reflecting the payload-capability enhancement from the three-core configuration relative to the single-core Falcon 9 baseline.

The Falcon Heavy launch sequence comprises the eleven launches across the February 6 2018 through drafting-date period, documented in the [SpaceX news archive][ref_spacex_news_archive] press releases. The launches include the inaugural Tesla-Roadster demonstration on February 6 2018, the Arabsat-6A commercial mission on April 11 2019, the STP-2 defense mission on June 25 2019, the USSF-44 defense mission on November 1 2022, the Psyche NASA mission on October 13 2023, and the subsequent commercial and defense missions.

The Falcon Heavy annual-cadence yields the compact form

$$\bar N^{\text{FH-per-year}} = \frac{n^{\text{total-flights}}_{FH}}{\Delta t^{\text{operational}}_{FH}} \approx \frac{11}{7.5} \approx 1.5$$

reflecting the approximately 1.5-launch-per-year operational cadence substantially below the Falcon 9 approximately 140-launch-per-year cadence due to the narrow heavy-lift-mission subset.

The Falcon Heavy rung-value analysis allows the brief statement of the approximately 500 million dollar development investment against the approximately 1 billion dollars in cumulative launch-service revenue across the 2018 through drafting-date operational period. The rung-value ratio of approximately 2 exceeds unity, reflecting the commercial-viability of the Falcon Heavy rung despite the lower launch cadence compared to the Falcon 9.

## The Dragon 2 Crew and Cargo Spacecraft 2014 through Drafting Date

The Dragon 2 crew and cargo spacecraft constitutes the fifth rung of the SpaceX vehicle-family decomposition and the human-spaceflight capability. The Dragon 2 development period spans the September 16 2014 [Commercial Crew Transportation Capability contract award][ref_nasa_cctcap_2014] through the March 2 2019 Demo-1 uncrewed flight, the May 30 2019 Demo-2 crewed flight, and the subsequent operational period across the 2020 through drafting-date period. The Dragon 2 program is documented in the [GAO 2014 Commercial Crew Transportation Report][ref_gao_2014_commercial_crew], the [GAO 2020 Commercial Crew Progress Report][ref_gao_2020_commercial_crew], the [NASA Commercial Crew Program Documents][ref_nasa_ccp_documents], the [Congressional Research Service Commercial Crew Reports][ref_crs_commercial_crew], the [NASA Commercial Crew Certification Documentation][ref_nasa_cots_saa_2006], the [House Committee on Science Space and Technology Hearings on Commercial Crew][ref_house_science_committee_hearings], and the [SpaceX news archive][ref_spacex_news_archive] launch press releases.

The Dragon 2 vehicle configuration comprises the pressurized crew spacecraft arrangement with the approximately 12,500-kilogram launch mass and the approximately four-crew capability supplemented by the approximately 3,300-kilogram cargo capability. The Dragon 2 configuration supports both the crew and cargo missions under the CRS-2 cargo-and-crew arrangement.

The crew-loss-of-mission probability takes the form

$$P^{\text{LOM}}_{D2} = 1 - \prod_{i \in \text{critical-events}} P^{\text{success}}_i$$

with the target loss-of-mission probability of less than 1 in 500 as the NASA Commercial Crew Program specification. The loss-of-crew probability can be written as

$$P^{\text{LOC}}_{D2} = P^{\text{LOM}}_{D2} \cdot P^{\text{catastrophic-given-mission-loss}}_{D2}$$

with the launch-abort-system reliability substantially reducing the loss-of-crew probability below the loss-of-mission probability.

The Dragon 2 rung-value analysis takes the compact statement of the approximately 3 billion dollar development investment as the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] treats against the approximately 3.5 billion dollars in Commercial Crew Transportation Capability revenue plus the approximately 3 billion dollars in CRS-2 cargo revenue across the 2019 through drafting-date operational period. The rung-value ratio of approximately 2 exceeds unity, reflecting the commercial-viability of the Dragon 2 rung as an independently justifiable configuration. The safety-and-reliability analysis draws on the [Musa 1998][book_musa_1998] Software Reliability Engineering framework, the [OConnor and Kleyner 2012][book_oconnor_kleyner_2012] Practical Reliability Engineering treatment, and the [NASA Systems Engineering Handbook][ref_nasa_se_handbook].

## The Starship and Super Heavy Super-Heavy-Lift Architecture 2016 through Drafting Date

The Starship and Super Heavy super-heavy-lift architecture constitutes the sixth rung of the SpaceX vehicle-family decomposition and the super-heavy-lift capability that supports the Mars-transportation, Human Landing System, and Starlink deployment applications. The Starship development period spans the September 27 2016 initial Interplanetary Transport System announcement documented in the [Musk 2017 IAC Making Humans a Multi-Planetary Species][research_musk_2017_iac] through the 2019 Starhopper testing, the April 20 2023 first integrated flight test, the October 13 2024 first successful booster catch, and the subsequent test-and-development period across the 2024 through drafting-date period. The Starship program is documented in the [SpaceX Starship User's Guide][ref_spacex_starship_users_guide], the [FAA Starship Environmental Assessment][ref_faa_starship_pea] and the [FAA Starship Programmatic Environmental Assessment][ref_faa_starship_pea], the [NASA HLS Option A Award April 16 2021][ref_nasa_hls_option_a_2021], the [NASA HLS Option B Award November 15 2022][ref_nasa_hls_option_b_2022], the [Musk 2018 IAC Making Life Multi-Planetary][research_musk_2018_iac], the [Musk 2024 Starship Update][research_musk_2024_starship_update], the [SpaceX news archive][ref_spacex_news_archive] test-flight press releases, the [Blue Origin Complaint Blue Origin Federation LLC v United States 2021][ref_blue_origin_hls_complaint], the [GAO Decision Blue Origin Federation LLC B-419783 2021][ref_gao_hls_bid_protest_2021], the [NASA HLS Sustainable Lunar Development Contract May 19 2023][ref_nasa_hls_sustainable_2023], and the contemporary trade-press coverage in [SpaceNews][ref_spacenews], [Ars Technica Space][ref_arstechnica_space], [NASASpaceflight][ref_nasaspaceflight], [Payload][ref_payload], [European Spaceflight][ref_european_spaceflight], the [New York Times][ref_nyt], and the [Washington Post][ref_washington_post].

The Starship vehicle configuration comprises the two-stage methane-and-liquid-oxygen arrangement with the 33 Raptor 2 first-stage engines and the six Raptor 2 second-stage engines including the three sea-level and three vacuum structures. The vehicle mass has the concise statement of approximately 5,000,000 kilograms at liftoff with the approximately 100,000-kilogram to 150,000-kilogram payload capability to low-Earth orbit in the reusable configuration.

The Starship total-thrust identity has the form

$$F^{\text{SS}}_{\text{total}} = 33 \cdot F^{\text{Raptor 2}}_{\text{sea-level}} \approx 74.4 \times 10^6 \text{ N}$$

reflecting the 33-engine Super Heavy first-stage configuration.

The full-flow-staged-combustion cycle chamber-pressure identity may be written

$$P^{\text{chamber}}_{\text{FFSC}} = P^{\text{oxidizer-turbopump}}_{\text{outlet}} = P^{\text{fuel-turbopump}}_{\text{outlet}}$$

with the Raptor 2 chamber pressure of approximately 300 bar substantially exceeding the gas-generator Merlin chamber pressure of approximately 100 bar reflecting the cycle-efficiency advantage of the full-flow-staged-combustion configuration.

The in-space-refueling mass-multiplication identity admits the compact form

$$m^{\text{destination}}_{\text{payload}} = m^{\text{LEO}}_{\text{payload}} \cdot e^{-\Delta v^{\text{destination}} / (I_{sp} \cdot g_0)} \cdot k^{\text{refuel}}$$

with $k^{\text{refuel}}$ the refueling-multiplier that the in-space-refueling capability provides for the interplanetary-mission payload delivery.

The full-reusability cost-per-kilogram-to-orbit projection takes the form

$$C^{\text{per-kg}}_{\text{full-reuse}} = \frac{C^{\text{propellant}} + C^{\text{operations}} + C^{\text{amortized-hardware}}}{m^{\text{payload}}}$$

with the projected approximately 100 dollar per kilogram cost under the full-reusability operational-cadence configuration substantially below the approximately 3,000 dollar per kilogram Falcon 9 reusable-mode baseline.

The Starship test sequence comprises the test flights across the April 20 2023 through drafting-date period, documented in the [FAA AST current licenses database][ref_faa_ast] records and the SpaceX press releases in the [SpaceX news archive][ref_spacex_news_archive]. The test flights include the IFT-1 on April 20 2023 that experienced multiple engine failures and the range-safety termination, the IFT-2 on November 18 2023 that achieved stage-separation but experienced the range-safety termination of both stages, the IFT-3 on March 14 2024 that achieved orbital-velocity but experienced the reentry break-up, the IFT-4 on June 6 2024 that achieved successful booster-splashdown and successful Starship-splashdown, the IFT-5 on October 13 2024 that achieved the first successful booster catch at Mechazilla, the subsequent IFT-6 through IFT-10 flights that expanded the test envelope, and the 2025-2026 operational flights that began the Starlink deployment and NASA HLS integration testing.

The test-flight-cadence progression can be written as

$$N^{\text{test-flights}}(t) = \sum_{k=1}^{n^{\text{completed}}} \mathbb{1}[t^{\text{flight}}_k \leq t]$$

with the IFT-flight indicator function summing to approximately 10 by the drafting date.

The test-flight-milestone-achievement progression has the form

$$M^{\text{milestones}}(n) = \{m : m \text{ achieved by flight } n\}$$

with the milestone set expanding across the IFT-1 through IFT-10 progression from the engine-ignition milestone through the stage-separation, orbital-velocity, successful-splashdown, booster-catch, and in-space-refueling-demonstration milestones.

The Starship rung-value analysis permits the concise statement of the approximately 5 billion dollar cumulative development investment through the drafting date against the approximately 4.05 billion dollars in NASA HLS Option A and Option B revenue that supports the Starship-derived HLS lander development. The rung-value ratio depends on the realized Starship operational applications including the commercial launch-service, the NASA HLS lunar-landing, the Starlink v2.0 deployment, and the interplanetary applications that admit substantial uncertainty at the drafting date.

The Starship expected-value decomposition may be written

$$E[V^{\text{Starship}}] = \sum_{a \in \text{applications}} P(a) \cdot V(a) \cdot \eta^{\text{Starship-share}}(a)$$

with the expected-value summing across the application-set weighted by the application-realization probability, the application-value, and the Starship-share of the application market.

## The Merlin Engine Family Progression

The Merlin engine family constitutes the propulsion-system rung within the SpaceX subsystem decomposition. The Merlin engine family development is documented in the technical treatments in The Falcon 1 Launch Vehicle Demonstration Flights Status and Future Plans, [Sutton and Biblarz 2010][book_sutton_biblarz_2010] Rocket Propulsion Elements, the [Musk 2017 IAC][research_musk_2017_iac] and [Musk 2018 IAC][research_musk_2018_iac] Starship treatments that reference the Merlin heritage, and the historical SpaceX press releases documenting the Merlin engine progression across the 2003 through drafting-date period. The Merlin 1A initial configuration produced approximately 340,000 newtons of thrust at sea level and served the Falcon 1 vehicle across the 2006 through 2008 period. The Merlin 1B intermediate configuration was developed but not flown. The Merlin 1C configuration produced approximately 420,000 newtons of thrust at sea level and served the Falcon 1 Flight 4 and Flight 5 missions and the Falcon 9 v1.0 vehicle. The Merlin 1C+ configuration provided the enhanced-thrust variant. The Merlin 1D configuration produced approximately 654,000 newtons of thrust at sea level and served the Falcon 9 v1.1, Full Thrust, and Block 5 arrangements and the Falcon Heavy vehicle. The Merlin 1D+ configuration provided the further-enhanced-thrust variant. The Merlin 1D Vacuum configuration produced approximately 934,000 newtons of thrust in vacuum and served the Falcon 9 and Falcon Heavy second stage.

The Merlin engine reuse across the Falcon 1, Falcon 9, and Falcon Heavy vehicles reflects the subsystem-level decomposability that supported the vehicle-family capability accumulation. The engine-level modularity index yields the compact statement of approximately 0.85 reflecting the high engine-reuse fraction across the vehicle family.

The Merlin thrust-progression admits the compact factor-form

$$\frac{F^{\text{Merlin 1D}}_{\text{sea-level}}}{F^{\text{Merlin 1A}}_{\text{sea-level}}} \approx \frac{654}{340} \approx 1.92$$

reflecting the approximately doubling of engine thrust across the Merlin family progression.

The Merlin specific-impulse progression allows the brief form

$$I_{sp}^{\text{Merlin 1D, sea level}} \approx 282 \text{ s}, \quad I_{sp}^{\text{Merlin 1D Vacuum}} \approx 348 \text{ s}$$

with the vacuum-configuration substantially exceeding the sea-level-arrangement specific impulse.

The Merlin engine-cost-reduction across the production-quantity admits the compact learning-curve form

$$C^{\text{Merlin}}(n) = C^{\text{Merlin}}(1) \cdot n^{-b^{\text{Merlin}}}$$

with $b^{\text{Merlin}} \approx 0.32$ reflecting the approximately 80 percent learning rate across the approximately 1,500-unit cumulative production through the drafting date.

## The Raptor Engine Family Progression

The Raptor engine family constitutes the super-heavy-lift propulsion-system rung within the SpaceX subsystem decomposition. The Raptor engine family development is documented in the [Musk 2017 IAC][research_musk_2017_iac] and [Musk 2018 IAC][research_musk_2018_iac] Starship treatments that specify the Raptor engine performance targets, the [Musk 2024 Starship Update][research_musk_2024_starship_update] Raptor 3 specifications, the technical treatment in [Sutton and Biblarz 2010][book_sutton_biblarz_2010] Rocket Propulsion Elements on the full-flow-staged-combustion cycle, the [Huzel and Huang 1992][book_huzel_huang_1992] Modern Engineering for Design of Liquid Propellant Rocket Engines, and the historical [Soviet RD-270 engine documentation][ref_rd270_documentation] as the precedent for the full-flow-staged-combustion cycle. The Raptor 1 initial configuration produced approximately 1,850,000 newtons of thrust at sea level using the full-flow staged-combustion cycle with the methane-and-liquid-oxygen propellant. The Raptor 2 configuration produced approximately 2,300,000 newtons of thrust at sea level and served the IFT-1 through IFT-10 Starship test flights. The Raptor 3 configuration produced approximately 2,750,000 newtons of thrust at sea level in the development-and-testing phase across the 2024 through drafting-date period.

The Raptor engine development represents the step-change from the kerosene-and-liquid-oxygen Merlin engine family to the methane-and-liquid-oxygen Raptor engine family that supports the Mars-transportation and in-space refueling applications. The engine-cycle progression from the gas-generator Merlin configuration to the full-flow staged-combustion Raptor arrangement reflects the technological-capability step that the Starship vehicle structure required.

The Raptor specific-impulse takes the compact statement

$$I_{sp}^{\text{Raptor 2, sea level}} \approx 327 \text{ s}, \quad I_{sp}^{\text{Raptor Vacuum}} \approx 380 \text{ s}$$

with the vacuum-configuration approaching the theoretical maximum for the methane-and-liquid-oxygen propellant arrangement.

The engine-cycle efficiency progression from the gas-generator to the full-flow-staged-combustion takes the form

$$\eta^{\text{cycle}}_{\text{FFSC}} > \eta^{\text{cycle}}_{\text{gas-generator}}$$

with the full-flow-staged-combustion cycle recovering the turbine exhaust into the combustion chamber rather than dumping the turbine exhaust overboard as the gas-generator cycle does.

The Raptor thrust-progression across the Raptor 1, Raptor 2, and Raptor 3 configurations can be written as

$$F^{\text{Raptor 3}}_{\text{sea-level}} = F^{\text{Raptor 1}}_{\text{sea-level}} \cdot \prod_{n=1}^{2} (1 + \Delta^{\text{Raptor}}_n)$$

with the approximately 50 percent thrust increase across the three-configuration progression.

## The Launch Site Progression

The launch site progression across the Kwajalein Omelek Island, Cape Canaveral SLC-40, Kennedy Space Center LC-39A, Vandenberg SLC-4E, and Boca Chica Starbase sites constitutes the launch-infrastructure rung within the SpaceX operations decomposition. The launch-site progression is documented in the [FAA AST current licenses database][ref_faa_ast], the [KSC LC-39A Lease Agreement][ref_ksc_lc39a_lease] between NASA and SpaceX, the [Vandenberg SLC-4E Environmental Assessment][ref_vandenberg_slc4e_ea], the [Boca Chica Starbase Environmental Assessment][ref_faa_starship_pea], and the historical treatment in [Benson and Faherty 1978][book_benson_faherty_1978] Moonport A History of Apollo Launch Facilities and Operations.

The Kwajalein Omelek Island site supported the Falcon 1 launches across the 2006 through 2009 period. The Cape Canaveral SLC-40 site supported the Falcon 9 launches from the June 4 2010 first flight through the September 1 2016 AMOS-6 pre-launch anomaly and the subsequent post-repair operational period. The Kennedy Space Center LC-39A site supported the Falcon 9 launches from the February 19 2017 first flight following the SLC-40 anomaly repair and the Falcon Heavy launches from the February 6 2018 first flight. The Vandenberg SLC-4E site supported the Falcon 9 polar-orbit launches from the September 29 2013 first flight. The Boca Chica Starbase site supports the Starship testing from the 2019 Starhopper testing through the drafting-date operational testing.

The launch-site decomposition reflects the mission-class specialization across the low-inclination LEO, polar LEO, geostationary-transfer, and super-heavy-lift configurations. The launch-site modularity supports the mission-flexibility that the SpaceX operations require.

The launch-site utilization identity has the form

$$U^{\text{site}}_i = \frac{N^{\text{launches}}_i}{N^{\text{maximum-cadence}}_i}$$

with the LC-39A utilization approaching approximately 0.8 across the 2024 through drafting-date period reflecting the approximately 40-launch-per-year cadence against the approximately 50-launch-per-year theoretical maximum.

The azimuth-constraint identity for the orbital-inclination may be written

$$\cos(i^{\text{inclination}}) = \cos(\phi^{\text{latitude}}) \cdot \sin(A^{\text{azimuth}})$$

with $\phi^{\text{latitude}}$ the launch-site latitude and $A^{\text{azimuth}}$ the launch azimuth that jointly determine the reachable orbital-inclination range from the launch site.

## Deep Historical Comparative Precedents

The decomposability pattern the SpaceX case exhibits admits comparative analysis against the historical precedent set of firms and programs that have or have not organized their development trajectories as ladders of independently valuable rungs.

The Boeing commercial-aircraft-family case permits the decomposability treatment. The Boeing 707 through Boeing 777 through Boeing 787 product-family progression across the 1958 through drafting-date period exhibits the rung-by-rung capability progression that the SpaceX vehicle family echoes. The 707 introduction in 1958 established the narrow-body jet-airliner configuration. The 727 introduction in 1963 extended the narrow-body configuration to the tri-jet short-to-medium-haul market. The 737 introduction in 1967 extended the narrow-body configuration to the short-haul twin-jet market and continues in production as the 737 MAX at the drafting date. The 747 introduction in 1969 established the wide-body quad-jet long-haul market. The 757 and 767 introductions in the 1980s established the medium-body twin-jet configurations. The 777 introduction in 1994 established the large-body twin-jet configuration. The 787 introduction in 2011 established the composite-fuselage long-haul configuration. The Boeing case is comprehensively documented in [Serling 1992][book_serling_1992] Legend and Legacy, [Newhouse 1982][book_newhouse_1982] The Sporty Game, and the [Boeing Historical Archives][ref_boeing_historical_archives]. The Boeing case illustrates the decomposability configuration at the commercial-aircraft-family scale.

The IBM System/360 through Z Series computer-family case allows the decomposability treatment. The System/360 introduction on April 7 1964 established the compatible-computer-family architecture that admitted the incremental upgrade across the System/360 through System/370 through System/390 through zSeries through Z Series configurations. The IBM case is comprehensively documented in [Pugh 1995][book_pugh_1995] Building IBM, [Pugh Johnson Palmer 1991][book_pugh_johnson_palmer_1991] IBM's 360 and Early 370 Systems, and the [IBM Archives][ref_ibm_archives]. The IBM case illustrates the decomposability configuration at the compatible-computer-architecture scale.

The Ford Motor Company product-family case supports the decomposability treatment. The Model T introduction in 1908 established the mass-market automobile configuration. The V-8 engine introduction in 1932 established the enhanced-performance engine configuration. The Falcon introduction in 1960 established the compact configuration. The Mustang introduction on April 17 1964 established the pony-car configuration. The F-series-truck continuation across the 1948 through drafting-date period established the commercial-truck configuration. The Ford case is comprehensively documented in [Ford and Crowther 1922][book_ford_crowther_1922] My Life and Work, [Nevins 1954][book_nevins_1954] Ford The Times The Man The Company, and [Hounshell 1984][book_hounshell_1984] From the American System to Mass Production. The Ford case illustrates the decomposability configuration at the automotive-product-family scale.

The Bell Telephone Laboratories technology-progression case admits the decomposability treatment. The point-contact transistor introduction on December 23 1947 by [Bardeen and Brattain 1948][research_bardeen_brattain_1948] The Transistor A Semi-Conductor Triode established the solid-state amplification configuration. The junction-transistor development in 1951 by [Shockley 1949][research_shockley_1949] The Theory of p-n Junctions in Semiconductors established the manufacturable transistor configuration. The integrated-circuit development in the 1958 through 1961 period by [Kilby 1976][research_kilby_1976] Invention of the Integrated Circuit and [Noyce 1976][research_noyce_1976] Microelectronics established the monolithic integrated-circuit configuration that supported the large-scale integration and very-large-scale integration progression. The Bell Labs case is comprehensively documented in [Gertner 2012][book_gertner_2012] The Idea Factory, [Riordan and Hoddeson 1997][book_riordan_hoddeson_1997] Crystal Fire, and [Wu 2010][book_wu_2010] The Master Switch. The Bell Labs case illustrates the decomposability configuration at the technology-progression scale that transferred substantially outside the parent-firm boundary as the [Value Capture article A284][related_post_a284_spacex_value_capture] treats.

The Titan launch-vehicle-family case permits the decomposability treatment. The Titan I through Titan II through Titan III through Titan IV progression across the 1959 through 2005 period exhibits the rung-by-rung capability progression from the liquid-fuel intercontinental-ballistic-missile configuration through the storable-propellant arrangement through the solid-rocket-motor-augmented structure through the expanded heavy-lift setup. The Titan case is documented in [Stumpf 2000][book_stumpf_2000] Titan II A History of a Cold War Missile Program and [Green and Lomask 1970][book_green_lomask_1970] Vanguard A History. The Titan case illustrates the decomposability configuration at the launch-vehicle-family scale within the government-directed development arrangement.

The Douglas commercial-aircraft-family case allows the decomposability treatment. The DC-3 introduction in 1936 established the medium-range airliner configuration. The DC-4 introduction in 1942 established the four-engine long-range configuration. The DC-6 and DC-7 introductions in the 1946 through 1953 period established the piston-engine long-range configurations. The DC-8 introduction in 1958 established the jet-airliner configuration. The DC-9 introduction in 1965 established the twin-jet configuration. The DC-10 introduction in 1971 established the wide-body tri-jet configuration. The MD-11 introduction in 1990 established the extended-range tri-jet configuration. The Douglas case is comprehensively documented in [Francillon 1979][book_francillon_1979] McDonnell Douglas Aircraft Since 1920 and [Serling 1992][book_serling_1992] Legend and Legacy. The Douglas case illustrates the decomposability configuration at the commercial-aircraft-family scale.

The Airbus commercial-aircraft-family case supports the decomposability treatment. The A300 introduction in 1972 established the twin-aisle twin-jet configuration. The A310 introduction in 1982 established the extended-range twin-jet configuration. The A320 introduction in 1987 established the fly-by-wire narrow-body configuration. The A330 and A340 introductions in the 1992 through 1993 period established the medium-range twin-jet and long-range quad-jet configurations. The A380 introduction in 2007 established the double-deck super-heavy configuration. The A350 introduction in 2015 established the composite-fuselage extended-range configuration. The Airbus case is comprehensively documented in [McIntyre 1992][book_mcintyre_1992] The Airbus Story and [Lawrence 2016][book_lawrence_2016] Airbus vs Boeing.

The single-configuration failure cases admit contrasting treatment. The Superconducting Super Collider case exhibited the all-or-nothing terminal-capability configuration that produced the catastrophic cancellation on October 21 1993 following the approximately 2 billion dollars in committed expenditure. The SSC case is comprehensively documented in [Riordan Hoddeson Kolb 2015][book_riordan_hoddeson_kolb_2015] Tunnel Visions. The Iridium case exhibited the all-or-nothing constellation-deployment configuration that produced the bankruptcy filing on August 13 1999 following the approximately 5 billion dollars in committed expenditure. The Iridium case is documented in the business-press coverage. The Boeing 2707 supersonic-transport case exhibited the all-or-nothing configuration that produced the cancellation on March 24 1971 following the approximately 200 million dollars in federal expenditure documented in [Horwitch 1982][book_horwitch_1982] Clipped Wings The American SST Conflict. The Constellation program case exhibited the all-or-nothing lunar-exploration configuration that produced the cancellation in the 2010 policy transition following the approximately 10 billion dollars in committed NASA expenditure documented in the [NASA Constellation Program Documentation][ref_nasa_constellation]. The International Thermonuclear Experimental Reactor case exhibits the ongoing all-or-nothing multi-decade construction configuration with the first-plasma target repeatedly postponed and the budget substantially exceeding the original commitment. The Concorde supersonic-transport case exhibited the all-or-nothing configuration that produced the commercial failure and the 2003 service termination despite the completed development documented in [Owen 2001][book_owen_2001] Concorde and the Americans and [Trubshaw 2000][book_trubshaw_2000] Concorde The Inside Story.

## Historiographical Gap and Recent Scholarship

The SpaceX decomposability treatment reveals substantial historiographical gaps in the existing scholarship that the present article partially addresses. The gap analysis proceeds across several dimensions.

### Identified Gaps in the Existing Scholarship

The first gap is the absence of comprehensive rung-by-rung value quantification for the SpaceX vehicle family. The existing scholarship including [Anadol Cohen Ferrari 2018][ref_hbs_spacex_case] SpaceX Case Study, [Weinzierl 2018][research_weinzierl_2018] Space the Final Economic Frontier, and [Fuchs 2010][research_fuchs_2010] Rethinking the Role of the State in Technology Development provides the qualitative treatment of the SpaceX vehicle-family progression but does not attempt the rung-by-rung quantitative decomposition of the revenue, capability, and learning value that the decomposability framework requires. The quantitative-decomposition gap partly reflects the private-firm status that precludes the direct financial disclosure and partly reflects the analytical-framework immaturity in the mission-oriented-innovation literature.

The second gap is the absence of comparative modularity metrics between the SpaceX vehicle family and the legacy-contractor vehicle families. The modular-architecture-metric literature including [MacCormack Baldwin Rusnak 2012][research_maccormack_baldwin_rusnak_2012] Exploring the Duality between Product and Organizational Architectures, [Sosa Eppinger Rowles 2003][research_sosa_eppinger_rowles_2003] Identifying Modular and Integrative Systems, and [Fixson 2005][research_fixson_2005] Product Architecture Assessment develops the quantitative-modularity-metric frameworks but does not systematically apply them to the launch-vehicle-family comparison across the SpaceX, ULA, Blue Origin, Rocket Lab, and legacy-contractor configurations.

The third gap is the absence of counterfactual-analytical treatment of the single-configuration-alternative SpaceX trajectories. The counterfactual-analytical treatment requires the speculative-reconstruction of the alternative-development trajectories under the Falcon-1-only, Falcon-9-only, or direct-to-Starship counterfactual specifications that the present article treats but that the existing scholarship does not systematically address.

The fourth gap is the absence of the staged-development-cost-and-schedule reconstruction across the SpaceX vehicle family. The existing scholarship provides the point-estimate treatments but does not develop the comprehensive cost-and-schedule dataset across the rung sequence that the real-options-analytical treatment requires.

### Commercial Space and Mission-Oriented Innovation Literature

The emerging literature partly addresses the gaps. The literature on the commercial-space-industry evolution including [Anderson 2023][book_anderson_2023] The Space Economy, [Davenport 2018][book_davenport_2018] The Space Barons, and [Fernholz 2018][book_fernholz_2018] Rocket Billionaires provides the comprehensive coverage of the commercial-space-industry evolution across the 2000 through drafting-date period. The literature on the mission-oriented-innovation strategy including [Mazzucato 2013][book_mazzucato_2013] The Entrepreneurial State, [Mazzucato 2021][book_mazzucato_2021] Mission Economy, and [Ruttan 2006][book_ruttan_2006] Is War Necessary for Economic Growth provides the analytical framework for the mission-oriented-innovation strategy treatment.

### Case-Study and Teaching Literature

The business-school case-study literature including the [Harvard Business School SpaceX Case][ref_hbs_spacex_case], the [Stanford Graduate School of Business SpaceX Case][ref_stanford_spacex_case], and the [Wharton SpaceX Case][ref_wharton_spacex_case] provides the qualitative treatment of the SpaceX development trajectory across the business-school teaching case format.

### Public Administration and Procurement Literature

The public-administration and public-policy literature that treats the NASA program-management approach and the commercial-partnership evolution includes the coverage in the [Public Administration Review][ref_public_admin_review] and the [Space Policy Journal][ref_space_policy_journal] scholarly treatments. The scholarship provides the analytical treatment of the institutional configuration within which the SpaceX decomposability arrangement operates.

### Space Law and Policy Literature

The space-policy literature including the coverage in the [Journal of Space Law][ref_journal_space_law] and the [Space Policy Online][ref_space_policy_online] policy-analysis coverage provides the analytical treatment of the regulatory and institutional context within which the SpaceX decomposability configuration operates.

## Contemporary Comparative Landscape

The contemporary launch-service-and-spacecraft-industry landscape provides the comparative context within which the SpaceX decomposability configuration admits characterization. The comparative treatment proceeds across the commercial-launch-service, commercial-spacecraft, and defense-launch-service segments.

The Blue Origin commercial-launch-service and commercial-spacecraft configuration constitutes the principal contemporary competitor to the SpaceX arrangement across the human-spaceflight, national-security-launch, and lunar-lander segments. The Blue Origin vehicle-family progression from the New Shepard sub-orbital-launch configuration through the New Glenn heavy-lift orbital-launch arrangement through the BE-4 engine development through the Blue Moon lunar-lander development exhibits the attempted-decomposability structure with the weaker execution than the SpaceX setup. The New Shepard first flight in the April 29 2015 period established the sub-orbital tourism configuration. The New Glenn first flight in the January 16 2025 period established the orbital-launch configuration approximately 14 years after the Blue Origin founding on September 8 2000 compared to the approximately 8-year Falcon 9 development period. The Blue Origin case is comprehensively documented in [Davenport 2018][book_davenport_2018] The Space Barons, [Fernholz 2018][book_fernholz_2018] Rocket Billionaires, and the [Blue Origin Press Releases][ref_blue_origin_press].

The Rocket Lab commercial-launch-service configuration constitutes the small-lift competitor to the SpaceX arrangement and exhibits the decomposability structure at the smaller scale. The Rocket Lab vehicle-family progression from the Electron small-lift-vehicle configuration through the Neutron medium-lift-vehicle development through the Photon spacecraft-platform arrangement exhibits the rung-by-rung capability progression at the approximately 100-fold smaller payload-capability scale. The Electron first flight on May 25 2017 established the small-lift dedicated-launch configuration. The Neutron development targets the mid-2020s first-flight. The Rocket Lab case is documented in the [Rocket Lab press releases][ref_rocket_lab_press] and the [SpaceNews][ref_spacenews] contemporary coverage.

The United Launch Alliance commercial-launch-service configuration constitutes the legacy-contractor case that exhibits the transition-based rather than the rung-based development arrangement. The ULA transition from the Atlas V through the Vulcan Centaur exhibits the single-configuration transition rather than the overlapping rung progression that the SpaceX arrangement exhibits. The Atlas V retirement approaches with the Vulcan Centaur first flight on January 8 2024. The ULA case is documented in the [ULA press releases][ref_ula_press] and the NSSL contract records.

The Relativity Space commercial-launch-service configuration exhibits the all-or-nothing 3D-printing-bet arrangement with the Terran 1 small-lift-vehicle first flight on March 22 2023 followed by the Terran R medium-lift-vehicle pivot. The Terran 1 program cancellation following the single flight illustrates the single-configuration failure mode that the decomposability arrangement avoids.

The Firefly Aerospace commercial-launch-service configuration exhibits the Alpha small-lift-vehicle through the Beta and medium-lift-vehicle development. The Firefly Alpha first successful orbital-flight on October 1 2022 established the small-lift capability.

The ArianeGroup commercial-launch-service configuration constitutes the European staged-evolution case with the Ariane 4 through Ariane 5 through Ariane 6 progression across the 1988 through drafting-date period exhibiting the slow-progression arrangement that produced the competitive-disadvantage relative to the SpaceX structure. The Ariane 6 first flight on July 9 2024 established the new-generation European launch capability. The ArianeGroup case is documented in the [ArianeGroup press releases][ref_arianegroup_press] and the [European Spaceflight][ref_european_spaceflight] contemporary coverage.

The Roscosmos launch-service configuration constitutes the Russian legacy-continuation case with the Soyuz launch-vehicle continuation from the 1966 first flight through the drafting-date operational continuation, and the Angara launch-vehicle protracted development from the 1992 initial concept through the December 23 2014 first flight and the limited operational cadence. The Roscosmos case illustrates the single-configuration continuation arrangement.

The China Aerospace Science and Technology Corporation configuration constitutes the Chinese state-directed arrangement with the Long March family evolution from the Long March 1 through Long March 5, Long March 6, Long March 7, and Long March 8 structures exhibiting the state-directed decomposability setup. The Long March family is documented in the [Chinese space program documentation][ref_chinese_space_program] and the contemporary trade-press coverage.

The Indian Space Research Organisation configuration constitutes the Indian state-directed arrangement with the PSLV through GSLV through LVM3 progression exhibiting the state-directed decomposability structure at the medium-lift scale. The ISRO case is documented in the [ISRO press releases][ref_isro_press].

The Japanese Aerospace Exploration Agency configuration constitutes the Japanese state-directed arrangement with the H-II through H-IIA through H-IIB through H3 progression exhibiting the state-directed decomposability structure. The JAXA case is documented in the [JAXA press releases][ref_jaxa_press].

The Northrop Grumman Antares commercial-launch-service configuration exhibits the joint-venture arrangement with the Antares 100 through Antares 200 through Antares 300 progression across the 2013 through drafting-date period. The Antares family is documented in the [Northrop Grumman press releases][ref_northrop_grumman_press].

The Sierra Space Dream Chaser commercial-spacecraft configuration exhibits the single-arrangement cargo-spacecraft development following the CRS-2 contract award. The Dream Chaser first orbital-flight targets the mid-2020s period.

The Boeing Starliner commercial-crew-spacecraft configuration exhibits the single-arrangement crew-spacecraft development that has produced the extended-development period with the Crewed Flight Test on June 5 2024 followed by the uncrewed-return decision due to the propulsion-and-life-support anomalies. The Starliner case illustrates the single-configuration failure mode that produced the commercial-viability question at the drafting date. The Starliner case is documented in the [Boeing press releases][ref_boeing_press] and the [NASA Commercial Crew Program Documents][ref_nasa_ccp_documents].

## Comparative Cross-Sectional Analysis

The decomposability-configuration comparative cross-sectional analysis proceeds across the contemporary launch-service-provider set with the attention to the rung-count, rung-value-realization, subsystem-modularity, and transition-time metrics.

The rung-count comparison permits the following approximate summary. The SpaceX configuration exhibits the approximately six-rung ladder across the Falcon 1, Falcon 9, Dragon 1, Falcon Heavy, Dragon 2, and Starship arrangements plus the approximately three-rung engine ladder across the Merlin, Kestrel, and Raptor structures plus the approximately four-rung launch-site ladder across the Kwajalein, SLC-40, LC-39A, SLC-4E, and Boca Chica setups. The total rung-count of approximately thirteen substantially exceeds the rung-counts of the contemporary competitors.

The Blue Origin configuration exhibits the approximately three-rung ladder across the New Shepard, New Glenn, and Blue Moon arrangements with the weaker rung-value-realization at each rung. The Rocket Lab configuration exhibits the approximately three-rung ladder across the Electron, Neutron, and Photon arrangements at the smaller scale. The ULA configuration exhibits the approximately two-rung ladder across the Atlas V and Vulcan Centaur arrangements with the transition rather than rung-progression structure. The ArianeGroup configuration exhibits the approximately three-rung ladder across the Ariane 4, Ariane 5, and Ariane 6 arrangements with the extended transition periods.

The rung-value-realization comparison allows the following approximate summary. The SpaceX Falcon 9 rung realized approximately 5 billion dollars in cumulative launch-service revenue across the 2010 through drafting-date period. The SpaceX Falcon Heavy rung realized approximately 1 billion dollars in cumulative launch-service revenue. The SpaceX Dragon 1 rung realized approximately 3 billion dollars in cumulative CRS-1 revenue. The SpaceX Dragon 2 rung realized approximately 6 billion dollars in cumulative CCtCap and CRS-2 revenue. The SpaceX Starship rung has realized approximately 4 billion dollars in NASA HLS revenue at the drafting date. The rung-value totals substantially exceed the rung-value totals for the contemporary competitors.

The subsystem-modularity comparison supports the following approximate summary. The SpaceX Merlin engine family is reused across the Falcon 9 and Falcon Heavy configurations. The SpaceX Dragon 1 to Dragon 2 subsystem reuse supports the spacecraft-family capability accumulation. The SpaceX structural, avionics, and operations reuse across the vehicle family supports the high modularity index. The competitor configurations exhibit lower modularity indices reflecting the reduced reuse across the vehicle families.

The transition-time comparison admits the following approximate summary. The SpaceX Falcon 1 to Falcon 9 transition spanned approximately two years from the 2008 fourth Falcon 1 flight to the 2010 first Falcon 9 flight. The SpaceX Falcon 9 to Falcon Heavy transition spanned approximately eight years from the 2010 first Falcon 9 flight to the 2018 first Falcon Heavy flight. The SpaceX Dragon 1 to Dragon 2 transition spanned approximately nine years from the 2010 first Dragon 1 flight to the 2019 first Dragon 2 crewed flight. The SpaceX Falcon 9 to Starship transition spans approximately 15 years and continues at the drafting date. The transition times substantially undercut the competitor transition times reflecting the rapid-development configuration.

The cost-per-kilogram-to-orbit comparison permits the following approximate summary. The SpaceX Falcon 9 reusable-configuration cost per kilogram to low-Earth orbit is approximately 2,700 dollars. The SpaceX Falcon Heavy expendable-configuration cost per kilogram is approximately 1,500 dollars. The SpaceX Starship projected fully-reusable-configuration cost per kilogram is approximately 100 dollars. The ULA Atlas V cost per kilogram is approximately 6,500 dollars. The ArianeGroup Ariane 5 cost per kilogram is approximately 9,000 dollars. The Roscosmos Soyuz cost per kilogram is approximately 5,000 dollars. The cost-per-kilogram comparison illustrates the competitive-advantage the SpaceX decomposability configuration produces.

The launch-cadence comparison allows the following approximate summary. The SpaceX Falcon 9 approximately 140-launch-per-year cadence in 2024 substantially exceeds the competitor annual cadences. The ULA approximately 5-launch-per-year cadence, the ArianeGroup approximately 5-launch-per-year cadence, the Roscosmos approximately 15-launch-per-year cadence, and the China Aerospace Science and Technology Corporation approximately 60-launch-per-year cadence collectively fall substantially below the SpaceX cadence.

## Data Sources and Reconstruction Methodology

The data-sources-and-reconstruction methodology treats the quantitative data underlying the rung-value analysis, the subsystem-modularity analysis, and the competitive-comparative analysis. The methodology proceeds across the primary-source, secondary-source, and reconstruction categories.

The primary-source category includes the SpaceX press releases in the [SpaceX news archive][ref_spacex_news_archive], the NASA program documentation including the [NASA COTS Final Report 2014][ref_nasa_cots_final_report_2014] and the [NASA HLS Option A Award April 16 2021][ref_nasa_hls_option_a_2021], the [FAA AST current licenses database][ref_faa_ast], the [FCC filings database][ref_fcc_filings] records including the Starlink authorizations, the [GAO reports][ref_gao_2014_commercial_crew] on the SpaceX-related programs, and the [Musk 2017 IAC][research_musk_2017_iac], [Musk 2018 IAC][research_musk_2018_iac], and [Musk 2024 Starship Update][research_musk_2024_starship_update] technical papers.

The secondary-source category includes the [Berger 2021][book_berger_2021] Liftoff and [Berger 2024][book_berger_2024] Reentry historical treatments, the [Vance 2015][book_vance_2015] and [Isaacson 2023][book_isaacson_2023] biographical treatments, the [Anderson 2023][book_anderson_2023] The Space Economy consolidation, and the [Anadol Cohen Ferrari 2018][ref_hbs_spacex_case] SpaceX Case Study business-school treatment.

The trade-press-source category includes the [SpaceNews][ref_spacenews], [Ars Technica Space][ref_arstechnica_space], [NASASpaceflight][ref_nasaspaceflight], [Payload][ref_payload], [Payload Research][ref_payload_research], [Aviation Week][ref_aviation_week], [Defense News][ref_defense_news], [Breaking Defense][ref_breaking_defense], [Space Policy Online][ref_space_policy_online], [The Space Review][ref_the_space_review], [European Spaceflight][ref_european_spaceflight], [Bloomberg][ref_bloomberg], [Wall Street Journal][ref_wsj], [New York Times][ref_nyt], and [Washington Post][ref_washington_post] coverage.

The reconstruction methodology treats the unavailable primary-source data through the triangulation across the multiple secondary sources. The SpaceX development cost estimates rely on the triangulation across the Musk statements in the IAC papers, the trade-press estimates in the Payload Research and SpaceNews coverage, and the analytical treatments in the Anadol Cohen Ferrari case study. The launch-cadence data rely on the FAA license records, the SpaceX press releases, and the trade-press launch-tracking coverage. The contract-value data rely on the NASA press releases, the GAO reports, and the Federal Procurement Data System records.

The data-limitation acknowledgment identifies the reconstructions as substantially reconstructive rather than directly documented for the SpaceX private-firm financial data, the competitor private-firm financial data, and the classified defense-contract data. The reconstructions carry substantial uncertainty and should be interpreted as approximate estimates rather than precise values.

The methodological triangulation approach follows the mixed-methods framework in [Creswell 2014][book_creswell_2014] Research Design Qualitative Quantitative and Mixed Methods Approaches and the case-study methodology in [Yin 2014][book_yin_2014] Case Study Research Design and Methods.

## Alternative Analytical Frameworks

The decomposability property supports alternative analytical treatment beyond the mission-oriented-innovation primary framework the series adopts. The alternative treatments include the real-options-analytical framing, the complexity-and-systems-of-systems framing, the actor-network-theory framing, the ecosystem-strategy framing, the political-economy framing, the public-choice-and-rent-seeking framing, and the behavioral-firm-theory framing.

The real-options-analytical framing extends the real-options treatment in the Cross-Disciplinary Framings section. The staged-investment configuration admits the compound-option treatment in which each rung's option-to-continue value depends recursively on the option value at each subsequent rung. The compound-option valuation has the concise form

$$V^{\text{compound}}_n = f\!\left(V^{\text{rung}}_n, V^{\text{compound}}_{n+1}, I_{n+1}, \sigma^{\text{market}}_{n+1}, \sigma^{\text{technical}}_{n+1}, r^{\text{discount}}\right)$$

with the inputs indexing the current-rung value, the subsequent-rung compound-option value, the subsequent-rung investment cost, the market-uncertainty volatility, the technical-uncertainty volatility, and the discount rate. The SpaceX case permits the compound-option treatment across the Falcon 1 to Falcon 9 to Falcon Heavy to Starship rung sequence.

The complexity-and-systems-of-systems framing treats the SpaceX vehicle-family and subsystem-family configuration through the complexity-theory and systems-of-systems-engineering treatments in [Maier 1998][research_maier_1998] Architecting Principles for Systems-of-Systems, [Sage and Cuppan 2001][research_sage_cuppan_2001] On the Systems Engineering and Management of Systems of Systems, [DeLaurentis and Callaway 2004][research_delaurentis_callaway_2004] A System-of-Systems Perspective for Public Policy Decisions, and [Kauffman 1993][book_kauffman_1993] The Origins of Order. The framing captures the hierarchical-complexity configuration in which the vehicle family, subsystem family, and operational-infrastructure jointly constitute the system-of-systems arrangement. The complexity-index takes the form

$$C_i = \sum_{s \in \text{subsystems}} \omega_s \cdot k_s^{\text{connectivity}}$$

with $k_s^{\text{connectivity}}$ the subsystem-connectivity degree.

The actor-network-theory framing treats the SpaceX decomposability configuration through the network-of-actors treatment in [Latour 1987][book_latour_1987] Science in Action, [Callon 1986][research_callon_1986] Some Elements of a Sociology of Translation, [Law 1987][research_law_1987] Technology and Heterogeneous Engineering, and [Bijker 1995][book_bijker_1995] Of Bicycles Bakelites and Bulbs. The framing treats the SpaceX vehicle-family, engine-family, and launch-infrastructure decomposition as the heterogeneous network of human and non-human actors whose alignment supports the decomposability configuration. The actor-network-strength index can be written as

$$ANS_i = \sum_{a \in \text{actors}} \omega_a \cdot \phi^{\text{alignment}}_{i,a}$$

with $\phi^{\text{alignment}}_{i,a}$ the actor-network-alignment fraction for actor $a$ in firm $i$.

The ecosystem-strategy framing treats the SpaceX decomposability configuration through the ecosystem-level orchestration in [Adner 2012][book_adner_2012] The Wide Lens, [Adner 2017][research_adner_2017] Ecosystem as Structure An Actionable Construct for Strategy, [Adner and Kapoor 2010][research_adner_kapoor_2010] Value Creation in Innovation Ecosystems, [Iansiti and Levien 2004][book_iansiti_levien_2004] The Keystone Advantage, and [Jacobides Cennamo and Gawer 2018][research_jacobides_et_al_2018] Towards a Theory of Ecosystems. The framing treats the SpaceX vehicle-family decomposition as the ecosystem-level orchestration configuration in which the SpaceX firm coordinates the launch-service, spacecraft, propulsion, and operations segments to jointly support the decomposability outcome. The ecosystem-orchestration index has the form

$$EO_i = \sum_{s \in \text{segments}} \omega_s \cdot \phi^{\text{coordinated}}_{i,s}$$

with $\phi^{\text{coordinated}}_{i,s}$ the segment-coordination strength.

The political-economy framing treats the SpaceX decomposability configuration through the critical political-economy treatment in [Foster and McChesney 2011][book_foster_mcchesney_2011] The Endless Crisis, [Krippner 2011][book_krippner_2011] Capitalizing on Crisis, and [Zuboff 2019][book_zuboff_2019] The Age of Surveillance Capitalism. The framing treats the SpaceX vehicle-family decomposition through the state-market interpenetration and the privatization-of-space-infrastructure dynamics that the decomposability configuration enables.

The public-choice and rent-seeking framing treats the SpaceX decomposability configuration through the public-choice-theory and rent-seeking-theory treatments in [Buchanan and Tullock 1962][book_buchanan_tullock_1962] The Calculus of Consent, [Stigler 1971][research_stigler_1971] The Theory of Economic Regulation, and [Krueger 1974][research_krueger_1974] The Political Economy of the Rent-Seeking Society. The framing treats the SpaceX vehicle-family decomposition and government-anchor procurement configuration through the rent-seeking-dynamics analysis of the NASA COTS, CCtCap, HLS, and Space Force NSSL contract-award mechanisms.

The behavioral-firm-theory framing treats the SpaceX decomposability configuration through the behavioral-firm-theory treatment in [Cyert and March 1963][book_cyert_march_1963] A Behavioral Theory of the Firm and [Simon 1957][book_simon_1957] Administrative Behavior. The framing treats the SpaceX firm-level decomposability decisions through the bounded-rationality and organizational-slack dynamics that the behavioral-firm-theory treatment identifies.

The evolutionary-economics framing treats the SpaceX decomposability configuration through the evolutionary-economics treatment in [Nelson and Winter 1982][book_nelson_winter_1982] An Evolutionary Theory of Economic Change and [Metcalfe 1998][book_metcalfe_1998] Evolutionary Economics and Creative Destruction. The framing treats the SpaceX vehicle-family evolution as the evolutionary-selection process in which the rung configurations that survive the market-and-technical selection constitute the incremental capability progression.

The institutional-economics framing treats the SpaceX decomposability configuration through the institutional-economics treatment in [North 1990][book_north_1990] Institutions Institutional Change and Economic Performance, [Ostrom 1990][book_ostrom_1990] Governing the Commons, and [Acemoglu and Robinson 2012][book_acemoglu_robinson_2012] Why Nations Fail. The framing treats the SpaceX decomposability configuration through the formal and informal institutional arrangements that shape the contracts, transactions, and organizational forms that support the rung-by-rung development.

The financial-sociology framing treats the SpaceX decomposability configuration through the financial-sociology treatment in [Fligstein 2001][book_fligstein_2001] The Architecture of Markets, [MacKenzie 2006][book_mackenzie_2006] An Engine Not a Camera, and [Ho 2009][book_ho_2009] Liquidated. The framing treats the SpaceX capital-formation configuration through the financial-market institutional arrangement that shapes the rung-by-rung capital-raising trajectory.

## Pattern Extraction

The decomposability pattern that the SpaceX case exhibits allows the following abstract statement without naming any downstream application. A mission-directed technology venture achieves the decomposability closure when the venture's development trajectory supports organization as a ladder of independently valuable rungs rather than as a single all-or-nothing terminal-capability program, with each intermediate configuration producing revenue, capability, and organizational-learning value that support the subsequent rung development.

The abstract decomposability mechanic requires joint satisfaction of five sub-properties. First, the rung sequence admits identification of the intermediate configurations that possess independent value. Second, each rung's value exceeds its own development cost so that the rung is individually justifiable rather than justifiable only through the terminal-capability value. Third, the rung-to-rung capability accumulation supports the subsequent-rung development. Fourth, the subsystem-level modularity supports the reuse across the rung sequence. Fifth, the staged-development configuration provides the real-option value that supports the risk-managed multi-decade capability accumulation.

The abstract decomposability closure admits the compact identity form

$$D^{\text{closure}} = \mathbb{1}\!\left[\prod_{k=1}^{5} \mathbb{1}[s_k \text{ satisfied}] = 1\right]$$

with the closure indicator equal to unity when all five sub-properties are jointly satisfied and zero when any sub-property fails.

The absence of the decomposability configuration produces the single-arrangement failure mode that the Superconducting Super Collider, the Iridium, and the International Thermonuclear Experimental Reactor cases illustrate. The single-configuration failure mode manifests through the all-or-nothing terminal-capability commitment that produces the catastrophic-failure risk when the terminal-capability program experiences the technical, budgetary, or political disruption that precludes the completion.

## Cross-References to the Series

The article back-references the [series opener][related_post_a281_spacex_framing] for the seven-plus-three framework introduction and the SpaceX founding narrative and 2002 through 2008 pre-COTS period. The article back-references the [Value Gradient article A282][related_post_a282_spacex_value_gradient] for the Falcon 1 through Falcon 9 to reusability progression and the Iridium single-bet failure contrast. The article back-references the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] for the COTS-1 salvation and the escalating anchor sequence through Cargo Resupply Services, Commercial Crew, HLS, and Starshield. The article back-references the [Value Capture article A284][related_post_a284_spacex_value_capture] for the launch-service pricing evolution and the vertical-integration into Starlink.

The article cross-references the existing published corpus including the [History of Rocketplanes article A96][related_post_a96_history_rocketplanes] for the technical rocketry history that provides the technical-context background, the [Introduction to Space Studies article A90][related_post_a90_intro_space_studies] for the broader space-context, the [What Does the United States Space Force Do article A97][related_post_a97_us_space_force] for the defense-customer context, the [Framing and the Co-Development Mechanism article A237][related_post_a237_aerospace_framing] for the aerospace-computing co-development framework, the [Space Shuttle Software as Engineering Landmark article A244][related_post_a244_space_shuttle_software] for the software-reliability engineering context, the [Silicon Valley from Defense Contracting article A246][related_post_a246_silicon_valley_defense] for the defense-anchor procurement pattern, the [Software-Defined Aerospace and Autonomy article A247][related_post_a247_software_defined_aerospace] for the software-defined vehicle context, and the [Contemporary Snapshot and Extrapolation article A248][related_post_a248_contemporary_snapshot] for the aerospace-industry-state coverage.

## Terminological Note

The article adopts terminology consistent with the aerospace-industry conventions. The term "small-lift" refers to launch vehicles with less than approximately 2,000 kilograms payload capability to low-Earth orbit. The term "medium-lift" refers to launch vehicles with approximately 2,000 to 20,000 kilograms payload capability. The term "heavy-lift" refers to launch vehicles with approximately 20,000 to 50,000 kilograms payload capability. The term "super-heavy-lift" refers to launch vehicles with greater than approximately 50,000 kilograms payload capability. The term "rung" refers to an intermediate configuration in the vehicle-family or subsystem-family decomposition that possesses independent value. The term "decomposability" refers to the property of the development trajectory that permits organization as a ladder of independently valuable rungs.

## Load-Bearing Open Questions

The article closes with the load-bearing open questions that the decomposability treatment leaves unresolved. First, the quantitative estimation of the rung-by-rung value realization requires substantially more primary-source documentation than the private-firm status permits. Second, the counterfactual analysis of the single-configuration alternatives requires the speculative reconstruction of the alternative-development trajectories. Third, the transferability of the decomposability pattern to the non-launch-vehicle applications allows substantial uncertainty. Fourth, the long-term sustainability of the decomposability configuration under the Starship-transition scenario supports substantial uncertainty pending the Starship operational validation.

## References

### Books

- [Acemoglu and Robinson 2012 Why Nations Fail][book_acemoglu_robinson_2012]
- [Adner 2012 The Wide Lens][book_adner_2012]
- [Alexander 1964 Notes on the Synthesis of Form][book_alexander_1964]
- [Anderson 2023 The Space Economy][book_anderson_2023]
- [Argote 1999 Organizational Learning][book_argote_1999]
- [Argyris and Schon 1978 Organizational Learning A Theory of Action Perspective][book_argyris_schon_1978]
- [Baldwin and Clark 2000 Design Rules The Power of Modularity][book_baldwin_clark_2000]
- [Beck 1999 Extreme Programming Explained][book_beck_1999]
- [Benson and Faherty 1978 Moonport A History of Apollo Launch Facilities and Operations][book_benson_faherty_1978]
- [Berger 2021 Liftoff][book_berger_2021]
- [Berger 2024 Reentry][book_berger_2024]
- [Bijker 1995 Of Bicycles Bakelites and Bulbs][book_bijker_1995]
- [Bilstein 1980 Stages to Saturn][book_bilstein_1980]
- [Bilstein 2001 Flight in America][book_bilstein_2001]
- [Boehm and Turner 2003 Balancing Agility and Discipline][book_boehm_turner_2003]
- [Buchanan and Tullock 1962 The Calculus of Consent][book_buchanan_tullock_1962]
- [Chaikin 1994 A Man on the Moon][book_chaikin_1994]
- [Chandler 1962 Strategy and Structure][book_chandler_1962]
- [Chandler 1977 The Visible Hand][book_chandler_1977]
- [Chandler 1990 Scale and Scope][book_chandler_1990]
- [Christensen 1997 The Innovator's Dilemma][book_christensen_1997]
- [Christensen and Raynor 2003 The Innovator's Solution][book_christensen_raynor_2003]
- [Copeland and Antikarov 2001 Real Options A Practitioners Guide][book_copeland_antikarov_2001]
- [Creswell 2014 Research Design Qualitative Quantitative and Mixed Methods Approaches][book_creswell_2014]
- [Cyert and March 1963 A Behavioral Theory of the Firm][book_cyert_march_1963]
- [Davenport 2018 The Space Barons][book_davenport_2018]
- [Dixit and Pindyck 1994 Investment Under Uncertainty][book_dixit_pindyck_1994]
- [Ezell and Ezell 1978 The Partnership A History of the Apollo-Soyuz Test Project][book_ezell_ezell_1978]
- [Fernholz 2018 Rocket Billionaires][book_fernholz_2018]
- [Fine 1998 Clockspeed Winning Industry Control in the Age of Temporary Advantage][book_fine_1998]
- [Fligstein 2001 The Architecture of Markets][book_fligstein_2001]
- [Ford and Crowther 1922 My Life and Work][book_ford_crowther_1922]
- [Foster 1986 Innovation The Attackers Advantage][book_foster_1986]
- [Foster and McChesney 2011 The Endless Crisis][book_foster_mcchesney_2011]
- [Francillon 1979 McDonnell Douglas Aircraft Since 1920][book_francillon_1979]
- [Gertner 2012 The Idea Factory][book_gertner_2012]
- [Green and Lomask 1970 Vanguard A History][book_green_lomask_1970]
- [Heppenheimer 1999 The Space Shuttle Decision][book_heppenheimer_1999]
- [Ho 2009 Liquidated][book_ho_2009]
- [Horwitch 1982 Clipped Wings The American SST Conflict][book_horwitch_1982]
- [Hounshell 1984 From the American System to Mass Production][book_hounshell_1984]
- [Humble Henry Larson 1995 Space Propulsion Analysis and Design][book_humble_henry_larson_1995]
- [Huzel and Huang 1992 Modern Engineering for Design of Liquid Propellant Rocket Engines][book_huzel_huang_1992]
- [Iansiti and Levien 2004 The Keystone Advantage][book_iansiti_levien_2004]
- [Isaacson 2023 Elon Musk][book_isaacson_2023]
- [Kauffman 1993 The Origins of Order][book_kauffman_1993]
- [Klepper 2016 Experimental Capitalism][book_klepper_2016]
- [Kranz 2000 Failure Is Not an Option][book_kranz_2000]
- [Krippner 2011 Capitalizing on Crisis][book_krippner_2011]
- [Latour 1987 Science in Action][book_latour_1987]
- [Launius 2004 Frontiers of Space Exploration][book_launius_2004]
- [Lawrence 2016 Airbus vs Boeing][book_lawrence_2016]
- [Liker 2004 The Toyota Way][book_liker_2004]
- [Logsdon 1970 The Decision to Go to the Moon][book_logsdon_1970]
- [MacKenzie 2006 An Engine Not a Camera][book_mackenzie_2006]
- [Mazzucato 2013 The Entrepreneurial State][book_mazzucato_2013]
- [Mazzucato 2021 Mission Economy][book_mazzucato_2021]
- [McCurdy 1994 Inside NASA][book_mccurdy_1994]
- [McIntyre 1992 The Airbus Story][book_mcintyre_1992]
- [Metcalfe 1998 Evolutionary Economics and Creative Destruction][book_metcalfe_1998]
- [Meyer and Lehnerd 1997 The Power of Product Platforms][book_meyer_lehnerd_1997]
- [Moore 1991 Crossing the Chasm][book_moore_1991]
- [Mowery and Rosenberg 1998 Paths of Innovation][book_mowery_rosenberg_1998]
- [Musa 1998 Software Reliability Engineering][book_musa_1998]
- [Nelson 1993 National Innovation Systems][book_nelson_1993]
- [Nelson and Winter 1982 An Evolutionary Theory of Economic Change][book_nelson_winter_1982]
- [Nevins 1954 Ford The Times The Man The Company][book_nevins_1954]
- [Newhouse 1982 The Sporty Game][book_newhouse_1982]
- [Nonaka and Takeuchi 1995 The Knowledge-Creating Company][book_nonaka_takeuchi_1995]
- [North 1990 Institutions Institutional Change and Economic Performance][book_north_1990]
- [O'Connor and Kleyner 2012 Practical Reliability Engineering][book_oconnor_kleyner_2012]
- [Ohno 1988 Toyota Production System][book_ohno_1988]
- [Ostrom 1990 Governing the Commons][book_ostrom_1990]
- [Owen 2001 Concorde and the Americans][book_owen_2001]
- [Penrose 1959 The Theory of the Growth of the Firm][book_penrose_1959]
- [Poppendieck and Poppendieck 2003 Lean Software Development][book_poppendieck_2003]
- [Pugh 1995 Building IBM][book_pugh_1995]
- [Pugh Johnson Palmer 1991 IBM's 360 and Early 370 Systems][book_pugh_johnson_palmer_1991]
- [Riordan and Hoddeson 1997 Crystal Fire][book_riordan_hoddeson_1997]
- [Riordan Hoddeson Kolb 2015 Tunnel Visions][book_riordan_hoddeson_kolb_2015]
- [Rogers 1962 Diffusion of Innovations][book_rogers_1962]
- [Ruttan 2006 Is War Necessary for Economic Growth][book_ruttan_2006]
- [Sanderson and Uzumeri 1997 Managing Product Families][book_sanderson_uzumeri_1997]
- [Schwaber 2004 Agile Project Management with Scrum][book_schwaber_2004]
- [Senge 1990 The Fifth Discipline][book_senge_1990]
- [Serling 1992 Legend and Legacy][book_serling_1992]
- [Shingo 1989 A Study of the Toyota Production System][book_shingo_1989]
- [Simon 1957 Administrative Behavior][book_simon_1957]
- [Stumpf 2000 Titan II A History of a Cold War Missile Program][book_stumpf_2000]
- [Suh 2001 Axiomatic Design][book_suh_2001]
- [Sutton and Biblarz 2010 Rocket Propulsion Elements][book_sutton_biblarz_2010]
- [Trigeorgis 1996 Real Options][book_trigeorgis_1996]
- [Trubshaw 2000 Concorde The Inside Story][book_trubshaw_2000]
- [Turner 2008 Rocket and Spacecraft Propulsion][book_turner_2008]
- [Utterback 1994 Mastering the Dynamics of Innovation][book_utterback_1994]
- [Vance 2015 Elon Musk][book_vance_2015]
- [Weiss 2014 America Inc][book_weiss_2014]
- [Wertz and Larson 1999 Space Mission Analysis and Design][book_wertz_larson_1999]
- [Womack and Jones 2003 Lean Thinking][book_womack_jones_2003]
- [Womack Jones Roos 1990 The Machine That Changed the World][book_womack_jones_roos_1990]
- [Wu 2010 The Master Switch][book_wu_2010]
- [Yin 2014 Case Study Research Design and Methods][book_yin_2014]
- [Zuboff 2019 The Age of Surveillance Capitalism][book_zuboff_2019]

### Reference

- [ArianeGroup Press Releases][ref_arianegroup_press]
- [Ars Technica Space Coverage][ref_arstechnica_space]
- [Aviation Week Coverage][ref_aviation_week]
- [Bloomberg Business News][ref_bloomberg]
- [Blue Origin Complaint Blue Origin Federation LLC v United States 2021][ref_blue_origin_hls_complaint]
- [Blue Origin Press Releases][ref_blue_origin_press]
- [Boeing Historical Archives][ref_boeing_historical_archives]
- [Boeing Press Releases][ref_boeing_press]
- [Breaking Defense Coverage][ref_breaking_defense]
- [Chinese Space Program Documentation][ref_chinese_space_program]
- [Commercial Space Launch Act 1984][ref_csla_1984]
- [Commercial Space Launch Amendments Act 2004][ref_csla_amendments_2004]
- [Congressional Research Service Commercial Crew Reports][ref_crs_commercial_crew]
- [Defense News Coverage][ref_defense_news]
- [European Spaceflight Coverage][ref_european_spaceflight]
- [FAA AST Current Launch Licenses Database][ref_faa_ast]
- [FAA Starship Environmental Assessment][ref_faa_starship_pea]
- [FCC Filings Database][ref_fcc_filings]
- [GAO 2014 Commercial Crew Transportation Report][ref_gao_2014_commercial_crew]
- [GAO 2020 Commercial Crew Progress Report][ref_gao_2020_commercial_crew]
- [GAO 2021 NASA Human Landing System Program Report][ref_gao_hls_bid_protest_2021]
- [Harvard Business School SpaceX Case][ref_hbs_spacex_case]
- [House Committee on Science Space and Technology Hearings on Commercial Crew][ref_house_science_committee_hearings]
- [IBM Archives][ref_ibm_archives]
- [INCOSE Systems Engineering Handbook][ref_incose_handbook]
- [Indian Space Research Organisation Press Releases][ref_isro_press]
- [ITAR 22 CFR 120 through 130][ref_itar_22_cfr_120_130]
- [ITER Organization][ref_iter_organization]
- [ITU Radio Regulations 2020][ref_itu_radio_regulations_2020]
- [Japanese Aerospace Exploration Agency Press Releases][ref_jaxa_press]
- [Journal of Space Law][ref_journal_space_law]
- [KSC LC-39A Lease Agreement][ref_ksc_lc39a_lease]
- [Kwajalein Atoll USAKA Historical Documentation][ref_kwajalein_atoll_documentation]
- [NASA CCtCap Contract September 16 2014][ref_nasa_cctcap_2014]
- [NASA Commercial Crew Certification Documentation][ref_nasa_cots_saa_2006]
- [NASA Commercial Crew Program Documents][ref_nasa_ccp_documents]
- [NASA Constellation Program Documentation][ref_nasa_constellation]
- [NASA COTS Final Report 2014][ref_nasa_cots_final_report_2014]
- [NASA CRS Program Overview][ref_nasa_crs_program_overview]
- [NASA HLS Option A Award April 16 2021][ref_nasa_hls_option_a_2021]
- [NASA HLS Option B Award November 15 2022][ref_nasa_hls_option_b_2022]
- [NASA HLS Sustainable Lunar Development Contract May 19 2023][ref_nasa_hls_sustainable_2023]
- [NASA Office of the Inspector General Reports][ref_nasa_oig_reports]
- [NASA Program and Project Life Cycle Requirements NPR 7120.5F][ref_nasa_npr_7120_5f]
- [NASA Space Act Agreements Guide][ref_nasa_saa_guide]
- [NASA Systems Engineering Handbook][ref_nasa_se_handbook]
- [NASA Technical Reports Server][ref_nasa_ntrs]
- [NASASpaceflight Coverage][ref_nasaspaceflight]
- [New York Times][ref_nyt]
- [Northrop Grumman Press Releases][ref_northrop_grumman_press]
- [Payload Newsletter][ref_payload]
- [Payload Research][ref_payload_research]
- [Public Administration Review][ref_public_admin_review]
- [Rocket Lab Press Releases][ref_rocket_lab_press]
- [Soviet RD-270 Engine Documentation][ref_rd270_documentation]
- [Space Force National Security Space Launch][ref_space_force_nssl]
- [Space Policy Journal][ref_space_policy_journal]
- [Space Policy Online][ref_space_policy_online]
- [SpaceNews][ref_spacenews]
- [SpaceX Booster Reuse Statistics][ref_spacex_booster_reuse_stats]
- [SpaceX Falcon Heavy Press Release April 5 2011][ref_spacex_press_falcon_heavy_2011]
- [SpaceX Falcon Heavy User's Guide][ref_spacex_falcon_heavy_users_guide]
- [SpaceX News Archive][ref_spacex_news_archive]
- [SpaceX Starship User's Guide][ref_spacex_starship_users_guide]
- [Stanford Graduate School of Business SpaceX Case][ref_stanford_spacex_case]
- [The Space Review][ref_the_space_review]
- [United Launch Alliance Press Releases][ref_ula_press]
- [United States Commercial Space Launch Competitiveness Act 2015][ref_uscsla_2015]
- [Vandenberg SLC-4E Environmental Assessment][ref_vandenberg_slc4e_ea]
- [Wall Street Journal][ref_wsj]
- [Washington Post][ref_washington_post]
- [Wharton SpaceX Case][ref_wharton_spacex_case]

### Research

- [Adner 2017 Ecosystem as Structure An Actionable Construct for Strategy][research_adner_2017]
- [Adner and Kapoor 2010 Value Creation in Innovation Ecosystems][research_adner_kapoor_2010]
- [Argote and Ingram 2000 Knowledge Transfer A Basis for Competitive Advantage in Firms][research_argote_ingram_2000]
- [Argote and Miron-Spektor 2011 Organizational Learning From Experience to Knowledge][research_argote_miron_spektor_2011]
- [Baldwin and Woodard 2009 The Architecture of Platforms A Unified View][research_baldwin_woodard_2009]
- [Bardeen and Brattain 1948 The Transistor A Semi-Conductor Triode][research_bardeen_brattain_1948]
- [Barney 1991 Firm Resources and Sustained Competitive Advantage][research_barney_1991]
-
- [Black and Scholes 1973 The Pricing of Options and Corporate Liabilities][research_black_scholes_1973]
- [Boehm 1988 A Spiral Model of Software Development and Enhancement][research_boehm_1988]
- [Bower and Christensen 1995 Disruptive Technologies Catching the Wave][research_bower_christensen_1995]
- [Callon 1986 Some Elements of a Sociology of Translation][research_callon_1986]
- [Cohen and Levinthal 1990 Absorptive Capacity A New Perspective on Learning and Innovation][research_cohen_levinthal_1990]
- [DeLaurentis and Callaway 2004 A System-of-Systems Perspective for Public Policy Decisions][research_delaurentis_callaway_2004]
- [Eisenhardt and Martin 2000 Dynamic Capabilities What Are They][research_eisenhardt_martin_2000]
- [Ethiraj and Levinthal 2004 Modularity and Innovation in Complex Systems][research_ethiraj_levinthal_2004]
- [Fixson 2005 Product Architecture Assessment A Tool to Link Product Manufacturing Supply Chain and Service Decisions][research_fixson_2005]
- [Fuchs 2010 Rethinking the Role of the State in Technology Development][research_fuchs_2010]
- [Grant 1996 Toward a Knowledge-Based Theory of the Firm][research_grant_1996]
- [Helfat and Peteraf 2003 The Dynamic Resource-Based View][research_helfat_peteraf_2003]
- [Jacobides Cennamo and Gawer 2018 Towards a Theory of Ecosystems][research_jacobides_et_al_2018]
- [Kilby 1976 Invention of the Integrated Circuit][research_kilby_1976]
-
- [Klepper 1996 Entry Exit Growth and Innovation over the Product Life Cycle][research_klepper_1996]
- [Klepper 2010 The Origin and Growth of Industry Clusters][research_klepper_2010]
- [Kogut and Zander 1992 Knowledge of the Firm Combinative Capabilities and the Replication of Technology][research_kogut_zander_1992]
- [Krueger 1974 The Political Economy of the Rent-Seeking Society][research_krueger_1974]
- [Lane Koka Pathak 2006 The Reification of Absorptive Capacity][research_lane_koka_pathak_2006]
- [Law 1987 Technology and Heterogeneous Engineering][research_law_1987]
- [Levitt and March 1988 Organizational Learning][research_levitt_march_1988]
- [MacCormack Baldwin Rusnak 2012 Exploring the Duality between Product and Organizational Architectures][research_maccormack_baldwin_rusnak_2012]
- [Maier 1998 Architecting Principles for Systems-of-Systems][research_maier_1998]
- [March 1991 Exploration and Exploitation in Organizational Learning][research_march_1991]
- [McDonald and Siegel 1986 The Value of Waiting to Invest][research_mcdonald_siegel_1986]
- [Merton 1973 Theory of Rational Option Pricing][research_merton_1973]
- [Musk 2017 IAC Making Humans a Multi-Planetary Species][research_musk_2017_iac]
- [Musk 2018 IAC Making Life Multi-Planetary][research_musk_2018_iac]
- [Musk 2024 Starship Update][research_musk_2024_starship_update]
- [Myers 1977 Determinants of Corporate Borrowing][research_myers_1977]
- [Nonaka 1994 A Dynamic Theory of Organizational Knowledge Creation][research_nonaka_1994]
- [Noyce 1976 Microelectronics][research_noyce_1976]
- [Peteraf 1993 The Cornerstones of Competitive Advantage][research_peteraf_1993]
- [Pisano 2015 You Need an Innovation Strategy][research_pisano_2015]
- [Rivkin and Siggelkow 2003 Balancing Search and Stability Interdependencies Among Elements of Organizational Design][research_rivkin_siggelkow_2003]
- [Robertson and Ulrich 1998 Planning for Product Platforms][research_robertson_ulrich_1998]
- [Sage and Cuppan 2001 On the Systems Engineering and Management of Systems of Systems][research_sage_cuppan_2001]
- [Sanchez 1995 Strategic Flexibility in Product Competition][research_sanchez_1995]
- [Sanchez and Mahoney 1996 Modularity Flexibility and Knowledge Management in Product and Organization Design][research_sanchez_mahoney_1996]
- [Shockley 1949 The Theory of p-n Junctions in Semiconductors][research_shockley_1949]
- [Simon 1962 The Architecture of Complexity][research_simon_1962]
- [Sosa Eppinger Rowles 2003 Identifying Modular and Integrative Systems and their Impact on Design Team Interactions][research_sosa_eppinger_rowles_2003]
- [Stigler 1971 The Theory of Economic Regulation][research_stigler_1971]
- [Teece 2007 Explicating Dynamic Capabilities The Nature and Microfoundations of Sustainable Enterprise Performance][research_teece_2007]
- [Teece Pisano Shuen 1997 Dynamic Capabilities and Strategic Management][research_teece_pisano_shuen_1997]
- [Todorova and Durisin 2007 Absorptive Capacity Valuing a Reconceptualization][research_todorova_durisin_2007]
- [Ulrich 1995 The Role of Product Architecture in the Manufacturing Firm][research_ulrich_1995]
- [Volberda Foss Lyles 2010 Absorbing the Concept of Absorptive Capacity][research_volberda_foss_lyles_2010]
- [Weinzierl 2018 Space the Final Economic Frontier][research_weinzierl_2018]
- [Wernerfelt 1984 A Resource-Based View of the Firm][research_wernerfelt_1984]
- [Winter 2003 Understanding Dynamic Capabilities][research_winter_2003]
- [Wright 1936 Factors Affecting the Cost of Airplanes][research_wright_1936]
- [Zahra 2015 Corporate Entrepreneurship as Knowledge Creation and Conversion][research_zahra_2015]
- [Zahra and George 2002 Absorptive Capacity A Review Reconceptualization and Extension][research_zahra_george_2002]

### Related Post

- [A90 Introduction to Space Studies][related_post_a90_intro_space_studies]
- [A96 History of Rocketplanes][related_post_a96_history_rocketplanes]
- [A97 What Does the United States Space Force Do][related_post_a97_us_space_force]
- [A237 Framing and the Co-Development Mechanism][related_post_a237_aerospace_framing]
- [A244 Space Shuttle Software as Engineering Landmark][related_post_a244_space_shuttle_software]
- [A246 Silicon Valley from Defense Contracting][related_post_a246_silicon_valley_defense]
- [A247 Software-Defined Aerospace and Autonomy][related_post_a247_software_defined_aerospace]
- [A248 Contemporary Snapshot and Extrapolation][related_post_a248_contemporary_snapshot]
- [A281 History of SpaceX Series Framing and the Seven-Plus-Three Forcing-Function Framework][related_post_a281_spacex_framing]
- [A282 History of SpaceX Value Gradient from Falcon 1 to Falcon 9 to Reusability][related_post_a282_spacex_value_gradient]
- [A283 History of SpaceX Anchor Demand from COTS-1 Salvation Through Commercial Crew, HLS, and Starshield][related_post_a283_spacex_anchor_demand]
- [A284 History of SpaceX Value Capture from Launch-Service Pricing and Vertical Integration into Starlink][related_post_a284_spacex_value_capture]

[book_acemoglu_robinson_2012]: https://openlibrary.org/search?q=Acemoglu+and+Robinson+Why+Nations+Fail
[book_adner_2012]: https://openlibrary.org/search?q=Adner+The+Wide+Lens
[book_alexander_1964]: https://www.hup.harvard.edu/books/9780674627512
[book_anderson_2023]: https://www.wiley.com/en-us/The+Space+Economy-p-9781119911562
[book_argote_1999]: https://openlibrary.org/search?q=Argote+Organizational+Learning+Creating+Retaining+Transferring+Knowledge
[book_argyris_schon_1978]: https://www.pearson.com/en-us/subject-catalog/p/organizational-learning-a-theory-of-action-perspective/P200000005949
[book_baldwin_clark_2000]: https://mitpress.mit.edu/9780262024662/design-rules/
[book_beck_1999]: https://www.oreilly.com/library/view/extreme-programming-explained/9780321278654/
[book_benson_faherty_1978]: https://ntrs.nasa.gov/search?q=Moonport+History+of+Apollo+Launch+Facilities
[book_berger_2021]: https://williammorrow.com/liftoff-eric-berger/
[book_berger_2024]: https://williammorrow.com/reentry-eric-berger/
[book_bijker_1995]: https://mitpress.mit.edu/9780262522274/of-bicycles-bakelites-and-bulbs/
[book_bilstein_1980]: https://ntrs.nasa.gov/search?q=Stages+to+Saturn
[book_bilstein_2001]: https://jhupbooks.press.jhu.edu/title/flight-america
[book_boehm_turner_2003]: https://www.pearson.com/en-us/subject-catalog/p/balancing-agility-and-discipline-a-guide-for-the-perplexed/P200000009253
[book_buchanan_tullock_1962]: https://www.libertyfund.org/books/the-calculus-of-consent/
[book_chaikin_1994]: https://www.penguinrandomhouse.com/books/74211/a-man-on-the-moon-by-andrew-chaikin/
[book_chandler_1962]: https://mitpress.mit.edu/9780262530095/strategy-and-structure/
[book_chandler_1977]: https://www.hup.harvard.edu/books/9780674940529
[book_chandler_1990]: https://openlibrary.org/search?q=Chandler+Scale+and+Scope
[book_christensen_1997]: https://www.hbsp.harvard.edu/product/1130-HBK-ENG
[book_christensen_raynor_2003]: https://www.hbsp.harvard.edu/product/3595-HBK-ENG
[book_copeland_antikarov_2001]: https://openlibrary.org/search?q=Copeland+and+Antikarov+Real+Options+A+Practitioners+Guide
[book_creswell_2014]: https://us.sagepub.com/en-us/nam/research-design/book255675
[book_cyert_march_1963]: https://openlibrary.org/search?q=Cyert+March+Behavioral+Theory+Firm
[book_davenport_2018]: https://www.hachettebookgroup.com/titles/christian-davenport/the-space-barons/9781610398299/
[book_dixit_pindyck_1994]: https://openlibrary.org/search?q=Dixit+and+Pindyck+Investment+Under+Uncertainty
[book_ezell_ezell_1978]: https://ntrs.nasa.gov/search?q=On+Mars+Exploration+of+the+Red+Planet
[book_fernholz_2018]: https://www.hachettebookgroup.com/titles/tim-fernholz/rocket-billionaires/9781328662231/
[book_fine_1998]: https://www.hachettebookgroup.com/titles/charles-h-fine/clockspeed/9780738201535/
[book_fligstein_2001]: https://press.princeton.edu/books/paperback/9780691102542/the-architecture-of-markets
[book_ford_crowther_1922]: https://openlibrary.org/search?q=Ford+My+Life+and+Work
[book_foster_1986]: https://openlibrary.org/search?q=Foster+Innovation+Attackers+Advantage
[book_foster_mcchesney_2011]: https://monthlyreview.org/product/endless_crisis/
[book_francillon_1979]: https://openlibrary.org/search?q=Francillon+McDonnell+Douglas+Aircraft+Since+1920
[book_gertner_2012]: https://www.penguinrandomhouse.com/books/206061/the-idea-factory-by-jon-gertner/
[book_green_lomask_1970]: https://ntrs.nasa.gov/search?q=Vanguard+a+History
[book_heppenheimer_1999]: https://www.si.edu/object/space-shuttle-decision%3Anmah_1197080
[book_ho_2009]: https://www.dukeupress.edu/liquidated
[book_horwitch_1982]: https://mitpress.mit.edu/9780262580620/clipped-wings/
[book_hounshell_1984]: https://jhupbooks.press.jhu.edu/title/american-system-mass-production-1800-1932
[book_humble_henry_larson_1995]: https://www.mheducation.com/highered/product/space-propulsion-analysis-design-humble-henry/M9780070313200.html
[book_huzel_huang_1992]: https://arc.aiaa.org/doi/book/10.2514/4.866197
[book_iansiti_levien_2004]: https://www.hbsp.harvard.edu/product/5219-HBK-ENG
[book_isaacson_2023]: https://www.simonandschuster.com/books/Elon-Musk/Walter-Isaacson/9781982181284
[book_kauffman_1993]: https://global.oup.com/academic/product/the-origins-of-order-9780195079517
[book_klepper_2016]: https://press.princeton.edu/books/hardcover/9780691169620/experimental-capitalism
[book_kranz_2000]: https://www.simonandschuster.com/books/Failure-Is-Not-an-Option/Gene-Kranz/9781439148815
[book_krippner_2011]: https://www.hup.harvard.edu/books/9780674066199
[book_latour_1987]: https://www.hup.harvard.edu/books/9780674792913
[book_launius_2004]: https://global.oup.com/academic/product/frontiers-of-space-exploration-9780313325243
[book_lawrence_2016]: https://www.routledge.com/Airbus-vs-Boeing/Lawrence/p/book/9781138287884
[book_liker_2004]: https://www.mheducation.com/highered/product/toyota-way-liker/M9780071392310.html
[book_logsdon_1970]: https://mitpress.mit.edu/9780262620109/the-decision-to-go-to-the-moon/
[book_mackenzie_2006]: https://mitpress.mit.edu/9780262633673/an-engine-not-a-camera/
[book_mazzucato_2013]: https://marianamazzucato.com/books/the-entrepreneurial-state
[book_mazzucato_2021]: https://marianamazzucato.com/books/mission-economy/
[book_mccurdy_1994]: https://jhupbooks.press.jhu.edu/title/inside-nasa
[book_mcintyre_1992]: https://openlibrary.org/search?q=McIntyre+Airbus+Industrie
[book_metcalfe_1998]: https://www.routledge.com/Evolutionary-Economics-and-Creative-Destruction/Metcalfe/p/book/9780415158671
[book_meyer_lehnerd_1997]: https://www.simonandschuster.com/books/The-Power-of-Product-Platforms/Marc-H-Meyer/9780684825809
[book_moore_1991]: https://www.harpercollins.com/products/crossing-the-chasm-geoffrey-a-moore
[book_mowery_rosenberg_1998]: https://www.cambridge.org/9780521645126
[book_musa_1998]: https://openlibrary.org/search?q=Musa+Software+Reliability+Engineering
[book_nelson_1993]: https://global.oup.com/academic/product/national-innovation-systems-9780195076172
[book_nelson_winter_1982]: https://www.hup.harvard.edu/books/9780674272286
[book_nevins_1954]: https://openlibrary.org/search?q=Nevins+Ford+The+Times+The+Man+The+Company
[book_newhouse_1982]: https://openlibrary.org/search?q=Newhouse+The+Sporty+Game
[book_nonaka_takeuchi_1995]: https://global.oup.com/academic/product/the-knowledge-creating-company-9780195092691
[book_north_1990]: https://www.cambridge.org/9780521397346
[book_oconnor_kleyner_2012]: https://openlibrary.org/search?q=O+Connor+and+Kleyner+Practical+Reliability+Engineering
[book_ohno_1988]: https://openlibrary.org/search?q=Ohno+Toyota+Production+System
[book_ostrom_1990]: https://www.cambridge.org/9780521405997
[book_owen_2001]: https://www.airlifepublishing.com/book/concorde-and-the-americans
[book_penrose_1959]: https://global.oup.com/academic/product/the-theory-of-the-growth-of-the-firm-9780199573844
[book_poppendieck_2003]: https://www.pearson.com/en-us/subject-catalog/p/lean-software-development-an-agile-toolkit/P200000009336
[book_pugh_1995]: https://mitpress.mit.edu/9780262161473/building-ibm/
[book_pugh_johnson_palmer_1991]: https://mitpress.mit.edu/9780262161237/ibms-360-and-early-370-systems/
[book_riordan_hoddeson_1997]: https://wwnorton.com/books/Crystal-Fire/
[book_riordan_hoddeson_kolb_2015]: https://openlibrary.org/search?q=Riordan+Hoddeson+Kolb+Tunnel+Visions
[book_rogers_1962]: https://www.simonandschuster.com/books/Diffusion-of-Innovations-5th-Edition/Everett-M-Rogers/9780743258234
[book_ruttan_2006]: https://global.oup.com/academic/product/is-war-necessary-for-economic-growth-9780195188042
[book_sanderson_uzumeri_1997]: https://openlibrary.org/search?q=Sanderson+and+Uzumeri+Managing+Product+Families
[book_schwaber_2004]: https://www.microsoftpressstore.com/store/agile-project-management-with-scrum-9780735619937
[book_senge_1990]: https://www.penguinrandomhouse.com/books/163984/the-fifth-discipline-by-peter-m-senge/
[book_serling_1992]: https://openlibrary.org/search?q=Serling+Legend+and+Legacy
[book_shingo_1989]: https://openlibrary.org/search?q=Shingo+A+Study+of+the+Toyota+Production+System
[book_simon_1957]: https://www.simonandschuster.com/books/Administrative-Behavior-4th-Edition/Herbert-A-Simon/9781439136218
[book_stumpf_2000]: https://uapress.arkansas.edu/9781557286017/titan-ii/
[book_suh_2001]: https://global.oup.com/academic/product/axiomatic-design-9780195134667
[book_sutton_biblarz_2010]: https://www.wiley.com/en-us/Rocket+Propulsion+Elements%2C+9th+Edition-p-9781118753651
[book_trigeorgis_1996]: https://mitpress.mit.edu/9780262201025/real-options/
[book_trubshaw_2000]: https://openlibrary.org/search?q=Trubshaw+Concorde+Inside+Story
[book_turner_2008]: https://link.springer.com/book/10.1007/978-3-540-69203-4
[book_utterback_1994]: https://www.hbsp.harvard.edu/product/4855-HBK-ENG
[book_vance_2015]: https://www.harpercollins.com/products/elon-musk-ashlee-vance
[book_weiss_2014]: https://www.cornellpress.cornell.edu/book/9780801479922/america-inc/
[book_wertz_larson_1999]: https://link.springer.com/book/9780792359012
[book_womack_jones_2003]: https://www.simonandschuster.com/books/Lean-Thinking/James-P-Womack/9780743249270
[book_womack_jones_roos_1990]: https://www.simonandschuster.com/books/The-Machine-That-Changed-the-World/James-P-Womack/9780743299794
[book_wu_2010]: https://openlibrary.org/search?q=Wu+The+Master+Switch
[book_yin_2014]: https://us.sagepub.com/en-us/nam/case-study-research-and-applications/book250150
[book_zuboff_2019]: https://www.hachettebookgroup.com/titles/shoshana-zuboff/the-age-of-surveillance-capitalism/9781610395694/
[ref_arianegroup_press]: https://www.arianegroup.com/en/news/press-releases/
[ref_arstechnica_space]: https://arstechnica.com/science/space/
[ref_aviation_week]: https://aviationweek.com/
[ref_bloomberg]: https://www.bloomberg.com/
[ref_blue_origin_hls_complaint]: https://www.uscfc.uscourts.gov/
[ref_blue_origin_press]: https://www.blueorigin.com/news/
[ref_boeing_historical_archives]: https://www.boeing.com/history/
[ref_boeing_press]: https://boeing.mediaroom.com/
[ref_breaking_defense]: https://breakingdefense.com/
[ref_chinese_space_program]: https://www.cnsa.gov.cn/english/
[ref_crs_commercial_crew]: https://crsreports.congress.gov/product/pdf/R/R44708
[ref_csla_1984]: https://www.law.cornell.edu/uscode/text/51/subtitle-V/chapter-509
[ref_csla_amendments_2004]: https://www.congress.gov/108/plaws/publ492/PLAW-108publ492.pdf
[ref_defense_news]: https://www.defensenews.com/
[ref_european_spaceflight]: https://europeanspaceflight.com/
[ref_faa_ast]: https://www.faa.gov/space
[ref_faa_starship_pea]: https://www.faa.gov/space/stakeholder_engagement/spacex_starship
[ref_fcc_filings]: https://www.fcc.gov/wireless/systems-utilities/electronic-comment-filing-system-ecfs
[ref_gao_2014_commercial_crew]: https://www.gao.gov/products/gao-14-593
[ref_gao_2020_commercial_crew]: https://www.gao.gov/products/gao-20-121
[ref_gao_hls_bid_protest_2021]: https://www.gao.gov/products/b-419783
[ref_hbs_spacex_case]: https://www.hbs.edu/faculty/Pages/item.aspx?num=54001
[ref_house_science_committee_hearings]: https://science.house.gov/
[ref_ibm_archives]: https://www.ibm.com/history/
[ref_incose_handbook]: https://www.incose.org/products-and-publications/se-handbook
[ref_isro_press]: https://www.isro.gov.in/
[ref_itar_22_cfr_120_130]: https://www.ecfr.gov/current/title-22/chapter-I/subchapter-M
[ref_iter_organization]: https://www.iter.org/
[ref_itu_radio_regulations_2020]: https://www.itu.int/pub/R-REG-RR
[ref_jaxa_press]: https://global.jaxa.jp/press/
[ref_journal_space_law]: https://airandspacelaw.olemiss.edu/journal-of-space-law/
[ref_ksc_lc39a_lease]: https://www.nasa.gov/kennedy/
[ref_kwajalein_atoll_documentation]: https://www.army.mil/usakwajalein
[ref_nasa_ccp_documents]: https://www.nasa.gov/commercialcrew/
[ref_nasa_cctcap_2014]: https://www.nasa.gov/press/2014/september/nasa-chooses-american-companies-to-transport-us-astronauts-to-international/
[ref_nasa_constellation]: https://www.nasa.gov/history/history-publications-and-resources/nasa-history-series/
[ref_nasa_cots_final_report_2014]: https://ntrs.nasa.gov/search?q=Commercial+Orbital+Transportation+Services+final+report
[ref_nasa_cots_saa_2006]: https://www.nasa.gov/humans-in-space/commercial-space/
[ref_nasa_crs_program_overview]: https://www.nasa.gov/commercial-resupply/
[ref_nasa_hls_option_a_2021]: https://www.nasa.gov/humans-in-space/artemis/
[ref_nasa_hls_option_b_2022]: https://www.nasa.gov/mission/artemis-iii/
[ref_nasa_hls_sustainable_2023]: https://www.nasa.gov/press-release/nasa-selects-blue-origin-as-second-artemis-lunar-lander-provider/
[ref_nasa_npr_7120_5f]: https://nodis3.gsfc.nasa.gov/npg_img/N_PR_7120_005F_/N_PR_7120_005F_.pdf
[ref_nasa_ntrs]: https://ntrs.nasa.gov/
[ref_nasa_oig_reports]: https://oig.nasa.gov/audits/
[ref_nasa_saa_guide]: https://ntrs.nasa.gov/search?q=Space+Act+Agreement
[ref_nasa_se_handbook]: https://www.nasa.gov/reference/systems-engineering-handbook/
[ref_nasaspaceflight]: https://www.nasaspaceflight.com/
[ref_northrop_grumman_press]: https://news.northropgrumman.com/
[ref_nyt]: https://www.nytimes.com/section/science/space
[ref_payload]: https://payloadspace.com/
[ref_payload_research]: https://payloadspace.com/research/
[ref_public_admin_review]: https://onlinelibrary.wiley.com/journal/15406210
[ref_rd270_documentation]: https://www.energomash.ru/
[ref_rocket_lab_press]: https://www.rocketlabusa.com/updates/
[ref_space_force_nssl]: https://www.spaceforce.mil/News/Fact-Sheets
[ref_space_policy_journal]: https://www.sciencedirect.com/journal/space-policy
[ref_space_policy_online]: https://spacepolicyonline.com/
[ref_spacenews]: https://spacenews.com/
[ref_spacex_booster_reuse_stats]: https://www.spacex.com/vehicles/falcon-9/
[ref_spacex_falcon_heavy_users_guide]: https://www.spacex.com/vehicles/falcon-heavy/
[ref_spacex_news_archive]: https://www.spacex.com/updates/
[ref_spacex_press_falcon_heavy_2011]: https://www.spacex.com/updates/
[ref_spacex_starship_users_guide]: https://www.spacex.com/vehicles/starship/
[ref_stanford_spacex_case]: https://www.gsb.stanford.edu/faculty-research/case-studies
[ref_the_space_review]: https://www.thespacereview.com/
[ref_ula_press]: https://www.ulalaunch.com/about/news
[ref_uscsla_2015]: https://www.congress.gov/114/plaws/publ90/PLAW-114publ90.pdf
[ref_vandenberg_slc4e_ea]: https://www.faa.gov/space/environmental
[ref_washington_post]: https://www.washingtonpost.com/business/technology/
[ref_wharton_spacex_case]: https://knowledge.wharton.upenn.edu/
[ref_wsj]: https://www.wsj.com/tech
[related_post_a237_aerospace_framing]: {% post_url 2026-07-13-framing_and_the_co_development_mechanism %}
[related_post_a244_space_shuttle_software]: {% post_url 2026-07-20-space_shuttle_software_as_engineering_landmark %}
[related_post_a246_silicon_valley_defense]: {% post_url 2026-07-22-silicon_valley_from_defense_contracting %}
[related_post_a247_software_defined_aerospace]: {% post_url 2026-07-23-software_defined_aerospace_and_autonomy %}
[related_post_a248_contemporary_snapshot]: {% post_url 2026-07-24-contemporary_snapshot_and_extrapolation %}
[related_post_a281_spacex_framing]: {% post_url 2026-07-25-spacex_history_framing %}
[related_post_a282_spacex_value_gradient]: {% post_url 2026-07-26-spacex_history_value_gradient %}
[related_post_a283_spacex_anchor_demand]: {% post_url 2026-07-27-spacex_history_anchor_demand %}
[related_post_a284_spacex_value_capture]: {% post_url 2026-07-28-spacex_history_value_capture %}
[related_post_a90_intro_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[related_post_a96_history_rocketplanes]: {% post_url 2026-02-27-history_of_rocketplanes %}
[related_post_a97_us_space_force]: {% post_url 2026-02-28-what_does_united_states_space_force_do %}
[research_adner_2017]: https://doi.org/10.1177/0149206316678451
[research_adner_kapoor_2010]: https://onlinelibrary.wiley.com/doi/10.1002/smj.821
[research_argote_ingram_2000]: https://www.sciencedirect.com/science/article/abs/pii/S0749597800928930
[research_argote_miron_spektor_2011]: https://pubsonline.informs.org/doi/10.1287/orsc.1100.0621
[research_baldwin_woodard_2009]: https://www.hbs.edu/faculty/Pages/item.aspx?num=32196
[research_bardeen_brattain_1948]: https://journals.aps.org/pr/abstract/10.1103/PhysRev.74.230
[research_barney_1991]: https://journals.sagepub.com/doi/10.1177/014920639101700108
[research_black_scholes_1973]: https://www.jstor.org/stable/1831029
[research_boehm_1988]: https://ieeexplore.ieee.org/document/59
[research_bower_christensen_1995]: https://hbr.org/1995/01/disruptive-technologies-catching-the-wave
[research_callon_1986]: https://onlinelibrary.wiley.com/doi/10.1111/j.1467-954X.1984.tb00113.x
[research_cohen_levinthal_1990]: https://www.jstor.org/stable/2393553
[research_delaurentis_callaway_2004]: https://asmedigitalcollection.asme.org/computingengineering/article/4/4/408/462891
[research_eisenhardt_martin_2000]: https://onlinelibrary.wiley.com/doi/10.1002/1097-0266%28200010/11%2921%3A10/11%3C1105%3A%3AAID-SMJ133%3E3.0.CO%3B2-E
[research_ethiraj_levinthal_2004]: https://pubsonline.informs.org/doi/10.1287/mnsc.1030.0145
[research_fixson_2005]: https://www.sciencedirect.com/science/article/abs/pii/S0272696304000816
[research_fuchs_2010]: https://direct.mit.edu/rest/article/92/1/168/58109/
[research_grant_1996]: https://onlinelibrary.wiley.com/doi/10.1002/smj.4250171110
[research_helfat_peteraf_2003]: https://onlinelibrary.wiley.com/doi/10.1002/smj.332
[research_jacobides_et_al_2018]: https://onlinelibrary.wiley.com/doi/10.1002/smj.2904
[research_kilby_1976]: https://ieeexplore.ieee.org/document/1454570
[research_klepper_1996]: https://www.jstor.org/stable/2118211
[research_klepper_2010]: https://academic.oup.com/icc/article/19/1/135/731929
[research_kogut_zander_1992]: https://pubsonline.informs.org/doi/10.1287/orsc.3.3.383
[research_krueger_1974]: https://www.jstor.org/stable/1808883
[research_lane_koka_pathak_2006]: https://journals.aom.org/doi/10.5465/amr.2006.22527456
[research_law_1987]: https://www.jstor.org/stable/687075
[research_levitt_march_1988]: https://www.annualreviews.org/doi/10.1146/annurev.so.14.080188.001535
[research_maccormack_baldwin_rusnak_2012]: https://doi.org/10.1016/j.respol.2012.04.011
[research_maier_1998]: https://onlinelibrary.wiley.com/doi/10.1002/(SICI)1520-6858(1998)1:4%3C267::AID-SYS3%3E3.0.CO;2-D
[research_march_1991]: https://pubsonline.informs.org/doi/10.1287/orsc.2.1.71
[research_mcdonald_siegel_1986]: https://academic.oup.com/qje/article-abstract/101/4/707/1885353
[research_merton_1973]: https://www.jstor.org/stable/3003143
[research_musk_2017_iac]: https://www.liebertpub.com/doi/10.1089/space.2017.29009.emu
[research_musk_2018_iac]: https://www.spacex.com/updates/
[research_musk_2024_starship_update]: https://www.spacex.com/updates/
[research_myers_1977]: https://www.sciencedirect.com/science/article/abs/pii/0304405X77900150
[research_nonaka_1994]: https://pubsonline.informs.org/doi/10.1287/orsc.5.1.14
[research_noyce_1976]: https://ieeexplore.ieee.org/document/1454572
[research_peteraf_1993]: https://onlinelibrary.wiley.com/doi/10.1002/smj.4250140303
[research_pisano_2015]: https://hbr.org/2015/06/you-need-an-innovation-strategy
[research_rivkin_siggelkow_2003]: https://doi.org/10.1287/mnsc.49.3.290.12740
[research_robertson_ulrich_1998]: https://sloanreview.mit.edu/article/planning-for-product-platforms/
[research_sage_cuppan_2001]: https://doi.org/10.3233/iks-2001-00045
[research_sanchez_1995]: https://onlinelibrary.wiley.com/doi/10.1002/smj.4250160921
[research_sanchez_mahoney_1996]: https://onlinelibrary.wiley.com/doi/10.1002/smj.4250171107
[research_shockley_1949]: https://onlinelibrary.wiley.com/doi/10.1002/j.1538-7305.1949.tb03645.x
[research_simon_1962]: https://www.jstor.org/stable/985254
[research_sosa_eppinger_rowles_2003]: https://doi.org/10.1115/1.1564074
[research_stigler_1971]: https://www.jstor.org/stable/3003160
[research_teece_2007]: https://onlinelibrary.wiley.com/doi/10.1002/smj.640
[research_teece_pisano_shuen_1997]: https://onlinelibrary.wiley.com/doi/10.1002/%28SICI%291097-0266%28199708%2918%3A7%3C509%3A%3AAID-SMJ882%3E3.0.CO%3B2-Z
[research_todorova_durisin_2007]: https://journals.aom.org/doi/10.5465/amr.2007.25275513
[research_ulrich_1995]: https://www.sciencedirect.com/science/article/abs/pii/0048733394000513
[research_volberda_foss_lyles_2010]: https://pubsonline.informs.org/doi/10.1287/orsc.1090.0503
[research_weinzierl_2018]: https://www.aeaweb.org/articles?id=10.1257/jep.32.2.173
[research_wernerfelt_1984]: https://onlinelibrary.wiley.com/doi/10.1002/smj.4250050207
[research_winter_2003]: https://onlinelibrary.wiley.com/doi/10.1002/smj.318
[research_wright_1936]: https://arc.aiaa.org/doi/10.2514/8.155
[research_zahra_2015]: https://doi.org/10.1007/s11187-015-9650-4
[research_zahra_george_2002]: https://journals.aom.org/doi/10.5465/amr.2002.6587995
