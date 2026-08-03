---
layout: post
mathjax: true
comments: true
title: "History of SpaceX: Anchor Demand from COTS-1 Salvation Through Commercial Crew, HLS, and Starshield"
date: 2026-07-26 09:00:00 +0000
categories: history business aerospace
series: spacex_history
series_title: History of SpaceX
series_index: 3
---

<!-- A283 -->
<script>console.log("A283");</script>

This article is the third in the History of SpaceX series and treats the anchor-demand forcing-function condition that the [series opener][related_post_a281_spacex_framing] introduced as the second of seven forcing-function conditions in the seven-plus-three analytical framework. The anchor-demand condition requires that a mission-directed technology venture operate against a specific identifiable customer whose demand commitment is articulated and enforceable rather than against a speculative future market whose emergence is contingent on the venture's success. This article walks the SpaceX anchor-demand trajectory through the 2008 near-death moment that preceded the transition, the December 23 2008 Commercial Resupply Services CRS-1 contract award that constituted the salvation moment, the subsequent Cargo Resupply Services execution across CRS-1 and CRS-2 rounds, the September 2014 Commercial Crew Transportation Capability CCtCap award that added the human-rated anchor, the April 2021 Human Landing System Option A award that added the lunar-transportation anchor, the December 2022 Starshield defense-service line announcement that added the classified national-security anchor, and the parallel Space Force National Security Space Launch certification progression through Phase 1A, Phase 2, and Phase 3 Lane 2 that added the launch-services national-security anchor. The article closes with an explicit pattern-extraction section stating the abstract anchor-demand mechanic in a form other informed readers can recognize in adjacent domains without naming any specific downstream application.

## The Anchor-Demand Mapping Problem

The mapping problem for a comprehensive treatment of the anchor-demand condition in the SpaceX case is the question of which specific institutional, financial, and technical arrangements enabled the SpaceX trajectory to secure the anchor-demand transition at the specific December 2008 moment when the venture had exhausted its development budget across three consecutive Falcon 1 launch failures, and how the subsequent escalating anchor-ladder produced the sustained anchor-demand flow that supported the multi-decade capability accumulation. The problem admits several formalizations depending on the analytical tradition consulted. The procurement-economics tradition from [Laffont and Tirole 1993][book_laffont_tirole_1993] A Theory of Incentives in Procurement and Regulation through [McAfee and McMillan 1988][book_mcafee_mcmillan_1988] Incentives in Government Contracting and [Tirole 1988][book_tirole_1988] The Theory of Industrial Organization treats the specific incentive-compatibility properties of alternative procurement mechanisms as the primary determinant of the anchor-provider relationship structure. The mission-oriented-innovation tradition from [Mazzucato 2013][book_mazzucato_2013] The Entrepreneurial State through [Mazzucato 2021][book_mazzucato_2021] Mission Economy and [Weiss 2014][book_weiss_2014] America Inc treats the specific mission-directed public purchase as the primary organizing force that shapes the anchor-demand configuration. The developmental-state tradition from [Johnson 1982][book_johnson_1982] MITI and the Japanese Miracle through [Amsden 1989][book_amsden_1989] Asia's Next Giant, [Wade 1990][book_wade_1990] Governing the Market, and [Evans 1995][book_evans_1995] Embedded Autonomy treats the specific state-firm coordination as the primary determinant of the anchor-demand flow across the multi-decade horizon. The transaction-cost-economics tradition from [Coase 1937][research_coase_1937] The Nature of the Firm through [Williamson 1975][research_williamson_1975] Markets and Hierarchies and [Williamson 1985][book_williamson_1985] The Economic Institutions of Capitalism treats the specific asset-specificity and hold-up problems that shape the anchor-provider governance structure. The present article draws on all four traditions while adopting the mission-oriented-innovation framework the [series opener][related_post_a281_spacex_framing] established as the primary organizing structure.

The mapping problem admits several formalizations depending on the level of analysis adopted. At the transaction level, the anchor-demand condition reflects the specific milestone-payment fixed-price contract structure that the NASA Space Act Agreement authority permits. At the program level, the condition reflects the specific NASA Commercial Orbital Transportation Services program design that separated the mission-completion-payment structure from the traditional cost-plus contracting mechanism. At the sector level, the condition reflects the specific United States space-policy transition from the shuttle-era NASA-operator configuration to the mixed-provider commercial-services configuration that the specific Bush-era Vision for Space Exploration and Obama-era Commercial Crew Program initiated. At the international-competition level, the condition reflects the specific United States capacity to sustain the multi-decade launch-and-spacecraft capability against Chinese, Russian, and European alternative capabilities.

The general form of the anchor-demand causal-mapping problem can be stated compactly as follows. Let $D_i^{\text{anchor}}(t)$ denote the anchor-demand revenue stream to firm $i$ at time $t$ and $D_i^{\text{total}}(t)$ denote the total revenue. The anchor-demand condition requires

$$\frac{D_i^{\text{anchor}}(t)}{D_i^{\text{total}}(t)} \geq \theta^{\text{anchor}} \quad \text{during the pre-spinoff phase}$$

with $\theta^{\text{anchor}}$ typically substantially above one half during the pre-spinoff phase and declining as the commercial-spinoff revenue expands. The anchor-demand stream itself decomposes across the constituent anchor programs

$$D_i^{\text{anchor}}(t) = \sum_{k \in \text{programs}} D_{i,k}^{\text{gov}}(t) \cdot \mathbb{1}[t_k^{\text{start}} \leq t \leq t_k^{\text{end}}]$$

with each program contributing across its specific activation-to-termination window. The variance decomposition of the anchor-demand stream under the additive-program form admits

$$\text{Var}\!\left(D_i^{\text{anchor}}\right) = \sum_{k} \text{Var}\!\left(D_{i,k}^{\text{gov}}\right) + 2 \sum_{j<k} \text{Cov}\!\left(D_{i,j}^{\text{gov}}, D_{i,k}^{\text{gov}}\right)$$

with the covariance terms typically negative under the multi-program diversification that the [Portfolio Patience article A288][related_post_a281_spacex_framing] treats at greater depth.

The identification problem for the anchor-demand contribution to the SpaceX trajectory is the question of separating the anchor-demand effect from the confounding effects of the other six forcing-function conditions and the three capital-formation legs. The identification depends on the ability to specify counterfactual trajectories in which the anchor-demand condition would have failed and to compare the observed trajectory against those counterfactuals. The counterfactual differential admits the compact form

$$\Delta T_i^{\text{anchor}}(t) = T_i^{\text{observed}}(t) - T_i^{\text{no-anchor counterfactual}}(t)$$

with the anchor-demand attribution equal to the difference between the observed trajectory and the counterfactual trajectory absent the specific anchor demand. The specific counterfactual specifications the article treats include a no-COTS counterfactual in which the NASA Commercial Orbital Transportation Services program does not exist and the specific December 2008 salvation transition does not occur, a Rocketplane-Kistler-succeeds counterfactual in which the specific COTS Round 1 award is not reallocated and the SpaceX firm competes against the operational RPK provider, and an alternative-anchor counterfactual in which the SpaceX firm pursues commercial-only launch services without the NASA anchor demand. The instrumental-variable identification strategy under an exogenous procurement-mechanism-transition instrument $Z_i$ yields the identifying moment

$$\hat{\beta}_D^{\text{IV}} = \frac{\text{Cov}(T_i, Z_i)}{\text{Cov}(D_i^{\text{anchor}}, Z_i)}, \quad E[Z_i \, \varepsilon_i] = 0$$

which permits separate identification of the anchor-demand contribution from the confounding capital and mission-articulation contributions when the specific instrument satisfies the exogeneity condition.

## Methodological Commitments

The article commits to the same seven methodological positions that the [series opener][related_post_a281_spacex_framing] established for the series as a whole. These commitments are restated here at compact reference level.

The first commitment is descriptive-analytical framing rather than prescriptive advocacy. The article characterizes the anchor-demand trajectory descriptively without advocating for its replication in adjacent sectors.

The second commitment is dual-register composition, with both general-history and abstract-mechanic registers.

The third commitment is primary-source anchoring. The article cites primary sources for each substantive claim, with preference for NASA program documents accessible through the [NASA Technical Reports Server][ref_nasa_ntrs], NASA press releases accessible through the [NASA news][ref_nasa_news], Government Accountability Office reports accessible through the [GAO reports database][ref_gao_reports], NASA Office of Inspector General reports accessible through the [NASA OIG database][ref_nasa_oig_reports], Congressional Research Service reports accessible through the [CRS reports database][ref_crs_reports], and Space Force announcements accessible through the [Space Force news][ref_space_force_news].

The fourth commitment is contested-claim marking, with claims that remain contested cited on multiple sides.

The fifth commitment is temporal indexing, with the article as a snapshot as of mid-2026. The specific FAA Office of Commercial Space Transportation launch-license records accessible through the [FAA AST current licenses database][ref_faa_launch_licenses_current], the specific regulatory implementation in [14 CFR Part 450 launch and reentry licensing][ref_faa_ast_licensing_regs_450] and the broader [14 CFR Chapter III FAA commercial space regulations][ref_faa_ast_regulations], the specific [NASA Space Act Agreement authority at 51 U.S.C. 51302][ref_51_usc_51302_saa], the specific [Federal Acquisition Regulation Part 15 on contracting by negotiation][ref_far_part_15], the specific [NASA FAR Supplement][ref_nasa_far_supplement], the specific [NASA Commercial Crew Program 2014 framework][ref_nasa_ccp_2014], the specific [NASA Standard 8709.22 on safety and mission assurance][ref_nasa_std_8709_22], and the specific [NASA orbital debris mitigation standards][ref_nasa_orbital_debris_mitigation] provide the primary-source regulatory framework within which the anchor-demand configuration operates.

The sixth commitment is terminological transparency, with terms specific to the anchor-demand treatment defined in the Terminological Note.

The seventh commitment is thesis-not-proof framing of the anchor-demand closure claim.

## Anchor Demand as an Economic Property

The anchor-demand property is treated in the article as a specific economic property of a customer configuration that distinguishes ventures operating against articulated identifiable customer commitments from ventures operating against speculative future-market emergence. The property has specific formal characterizations that admit measurement, comparison across firms and sectors, and identification of the specific institutional arrangements that enable or preclude the property.

The formal characterization of the anchor-demand property admits several compact statements. Let the anchor-share function $\sigma_i(t) = D_i^{\text{anchor}}(t) / D_i^{\text{total}}(t)$ measure the fraction of firm $i$'s revenue at time $t$ that derives from anchor customers. The anchor-demand condition requires the strict-share property

$$\sigma_i(t) \geq \theta^{\text{anchor}} \quad \forall t \in [t^{\text{founding}}, t^{\text{spinoff-mature}}]$$

with $\theta^{\text{anchor}}$ typically approximately 0.6 during the pre-spinoff phase and declining monotonically toward zero as the commercial-spinoff revenue expands. The anchor-share trajectory typically follows

$$\sigma_i(t) = \sigma_i^{\text{initial}} \cdot e^{-\lambda t} + \sigma_i^{\text{floor}}$$

with $\lambda$ the specific decay rate driven by the spinoff-revenue expansion and $\sigma_i^{\text{floor}}$ the eventual steady-state anchor share that persists after spinoff maturity.

The anchor-demand economic value to the venture admits decomposition across several channels. First, the direct-revenue channel provides the specific cash flow that funds the operational and development spending. Second, the credential channel establishes the specific reputational asset that supports subsequent commercial-market entry. Third, the technical-standard channel imposes the specific reliability and mission-assurance requirements that transfer to commercial customers as an anchor-financed public good. Fourth, the redundancy-protection channel provides the specific competitive-market insulation during the transitional period before the venture achieves independent competitive standing. Fifth, the option-value channel provides the specific optionality that permits the venture to bid on subsequent anchor-program opportunities.

The anchor-demand decomposition across the four channels admits the compact form

$$V^{\text{anchor}}_i = V^{\text{revenue}}_i + V^{\text{credential}}_i + V^{\text{standard-transfer}}_i + V^{\text{redundancy}}_i + V^{\text{option}}_i$$

with each channel contributing distinct value to the venture. The specific channel contributions are estimated in the trade-press coverage and industry-analyst reconstructions, with the direct-revenue channel typically dominant during the initial anchor-demand transition and the credential and standard-transfer channels growing in significance as the venture matures.

The anchor-underwriting break-even condition that the fixed-cost capability requires admits the compact form

$$R^{\text{anchor}}_i > F^{\text{capability}}_i + c^{\text{marginal}}_i \cdot q^{\text{anchor}}_i$$

with $F^{\text{capability}}_i$ the fixed-cost capability investment, $c^{\text{marginal}}_i$ the per-mission marginal cost, and $q^{\text{anchor}}_i$ the anchor mission count. Under the condition, the venture can bid on marginal-cost commercial missions at prices exceeding marginal cost while capturing positive contribution to fixed-cost recovery from each additional commercial mission.

The reliability transmission from the anchor's requirements to the commercial customer base admits the standard-transfer identity

$$R^{\text{sector}}_{\text{comm}}(t) = R^{\text{anchor}}(t) - \Delta R^{\text{degradation}}$$

with $\Delta R^{\text{degradation}}$ the small reliability degradation for commercial-mission profiles that the anchor-financed reliability standard does not fully cover. The commercial customer surplus from the reliability spillover satisfies

$$\Delta CS^{\text{comm}} = \int_{R^{\text{comm-requirement}}}^{R^{\text{anchor}}} \frac{\partial WTP^{\text{comm}}}{\partial R} \, dR$$

with the integrand the marginal willingness-to-pay for reliability the commercial customer would have paid to obtain the reliability level the anchor-financed capability delivers at zero marginal cost.

The contract present-value structure for milestone-payment contracts admits the general form

$$PV^{\text{contract}}_i = \sum_{k=1}^{K^{\text{milestones}}} \frac{P_k^{\text{milestone}}}{(1 + r)^{t_k}}$$

with $P_k^{\text{milestone}}$ the payment at milestone $k$ and $t_k$ the achievement time, permitting the venture and the anchor to compute the contract value across the specific milestone-completion schedule.

The anchor-provider bilateral-relationship structure admits characterization through the specific dependency ratio

$$\delta_{i,k} = \frac{D_{i,k}^{\text{anchor}}}{\sum_{j \neq k} D_{i,j}^{\text{anchor}}}$$

with $\delta_{i,k}$ measuring the specific concentration of firm $i$'s anchor demand on anchor customer $k$ relative to the aggregate other-anchor demand. High $\delta_{i,k}$ values indicate substantial single-anchor concentration that creates specific hold-up vulnerability under the [Williamson 1985][book_williamson_1985] transaction-cost-economics treatment. The SpaceX trajectory exhibits declining $\delta_{i,\text{NASA}}$ over time as the Space Force, Human Landing System, and Starshield programs added anchor-demand diversification.

## Cross-Disciplinary Framings

The anchor-demand property admits characterization from several disciplinary traditions beyond the mission-oriented-innovation framework the series adopts as primary. The article treats each tradition as offering distinct analytical leverage on the same underlying property.

The procurement-economics tradition traces from [Laffont and Tirole 1993][book_laffont_tirole_1993] A Theory of Incentives in Procurement and Regulation through [McAfee and McMillan 1988][book_mcafee_mcmillan_1988] Incentives in Government Contracting, [Tirole 1988][book_tirole_1988] The Theory of Industrial Organization, the specific applications to the space-launch sector including [Kelly 2013][research_kelly_2013] Contract Auctions in Space Launch, and the seminal auction-theory framework in [Myerson 1981][research_myerson_1981] Optimal Auction Design and [Milgrom 2004][book_milgrom_2004] Putting Auction Theory to Work. The framing treats the anchor-demand property through the specific incentive-compatibility properties of alternative procurement mechanisms. The specific fixed-price milestone-payment mechanism the NASA Commercial Orbital Transportation Services program adopted creates the residual-claim retention identity

$$\pi_i^{\text{fixed-price}} = P^{\text{fixed}} - c_i^{\text{realized}}$$

with the provider retaining the full residual between the fixed contract price and the realized cost. The alternative cost-plus mechanism produces the profit

$$\pi_i^{\text{cost-plus}} = \phi_i \cdot c_i^{\text{realized}}$$

with $\phi_i$ the negotiated margin, providing no cost-reduction incentive.

The mission-oriented-innovation tradition traces from [Nelson 1977][research_nelson_1977] The Moon and the Ghetto and [Nelson 1959][research_nelson_1959] The Simple Economics of Basic Scientific Research through [Ruttan 2006][book_ruttan_2006] Is War Necessary for Economic Growth, [Mazzucato 2013][book_mazzucato_2013] The Entrepreneurial State, [Mazzucato 2021][book_mazzucato_2021] Mission Economy, [Fuchs 2010][research_fuchs_2010] Rethinking the Role of the State in Technology Development, and [Bonvillian 2018][research_bonvillian_2018] DARPA and the Advanced Research Projects Agency. The framing treats the anchor-demand property as one specific manifestation of the general mission-directed demand-pull mechanism that finances the fixed-cost investment in generic technological capability that subsequently finds commercial spinoff application. The mission-articulation-to-capability transfer admits the compact form

$$C_i^{\text{mission}}(t) = C_i^{\text{market}}(t) + \int_0^t g^{\text{mission}}\!\big(M, D^{\text{anchor}}(\tau)\big) \, d\tau$$

with the mission-directed increment beyond the market-directed baseline attributable to the specific mission articulation. The specific spinoff-to-anchor ratio $\rho = S / D^{\text{anchor}}$ measures the return to the anchor's investment in the form of subsequent commercial-spinoff capability that transfers beyond the original mission.

The developmental-state tradition traces from [Johnson 1982][book_johnson_1982] MITI and the Japanese Miracle through [Amsden 1989][book_amsden_1989] Asia's Next Giant, [Wade 1990][book_wade_1990] Governing the Market, [Evans 1995][book_evans_1995] Embedded Autonomy, [Chang 2002][book_chang_2002] Kicking Away the Ladder, [Woo-Cumings 1999][book_woo_cumings_1999] The Developmental State, [Weiss and Thurbon 2021][research_weiss_thurbon_2021] Developmental State or Economic Statecraft, and [Block 2008][research_block_2008] Swimming Against the Current The Rise of a Hidden Developmental State. The framing treats the anchor-demand property through the specific state-firm coordination that enables the sustained anchor-demand flow across the multi-decade horizon. The state-firm-coordination coefficient admits the compact index form

$$\text{SFC}_i = w^{\text{gov-rev}} \cdot \frac{R^{\text{gov}}_i}{R^{\text{total}}_i} + w^{\text{reg}} \cdot \phi^{\text{reg-alignment}}_i + w^{\text{coord}} \cdot I^{\text{formal-coord}}_i$$

with the three weighted components indexing government-revenue share, regulatory-alignment intensity, and formal-coordination institution presence.

The transaction-cost-economics tradition traces from [Coase 1937][research_coase_1937] The Nature of the Firm through [Williamson 1975][research_williamson_1975] Markets and Hierarchies, [Williamson 1985][book_williamson_1985] The Economic Institutions of Capitalism, [Williamson 2002][research_williamson_2002] The Theory of the Firm as Governance Structure, [Klein Crawford and Alchian 1978][research_klein_crawford_alchian_1978] Vertical Integration Appropriable Rents and the Competitive Contracting Process, [Hart 1988][research_hart_1988] Incomplete Contracts and the Theory of the Firm, and [Grossman and Hart 1986][research_grossman_hart_1986] The Costs and Benefits of Ownership A Theory of Vertical and Lateral Integration. The framing treats the anchor-demand property through the specific asset-specificity and hold-up problems that shape the anchor-provider governance structure. The specific asset-specificity index admits the compact form

$$k^{\text{specificity}}_i = 1 - \frac{V^{\text{alternative-use}}_i}{V^{\text{best-use}}_i}$$

with $k^{\text{specificity}}_i \in [0, 1]$ measuring the fraction of the asset value that is lost under alternative use rather than the best use. The SpaceX-NASA relationship exhibits substantial asset-specificity through the specific Falcon 9 vehicle and Dragon spacecraft configurations that were substantially designed against the NASA ISS-servicing mission requirements, creating specific hold-up vulnerability that the fixed-price milestone-payment mechanism and the multi-provider redundancy requirement partially mitigate.

The public-private-partnership tradition traces from [Grimsey and Lewis 2004][book_grimsey_lewis_2004] Public Private Partnerships through [Hodge and Greve 2007][research_hodge_greve_2007] Public-Private Partnerships An International Performance Review, [Yescombe 2007][book_yescombe_2007] Public-Private Partnerships Principles of Policy and Finance, [Osborne 2000][book_osborne_2000] Public-Private Partnerships Theory and Practice in International Perspective, [Bovaird 2004][research_bovaird_2004] Public-Private Partnerships From Contested Concepts to Prevalent Practice Assessing the Effectiveness of Public-Private Partnerships. The framing treats the anchor-demand property through the specific public-private-partnership structure that the COTS program instantiated as a specific alternative to the traditional cost-plus procurement mechanism. The shared-risk shared-reward identity that the PPP framework formalizes admits the compact form

$$V^{\text{joint}} = \alpha \cdot V^{\text{public}} + (1 - \alpha) \cdot V^{\text{private}} - \sigma^{\text{risk}} \cdot [\lambda \cdot r^{\text{public}} + (1 - \lambda) \cdot r^{\text{private}}]$$

with $\alpha$ the specific public-value weight, $\lambda$ the specific public-risk-bearing share, and the specific risk-premium terms indexing the specific risk-adjusted return to each partner.

The bilateral-monopoly and bargaining-theory tradition traces from [Nash 1950][research_nash_1950] The Bargaining Problem through [Rubinstein 1982][research_rubinstein_1982] Perfect Equilibrium in a Bargaining Model, [Binmore Rubinstein and Wolinsky 1986][research_binmore_rubinstein_wolinsky_1986] The Nash Bargaining Solution in Economic Modelling, [Muthoo 1999][book_muthoo_1999] Bargaining Theory with Applications, and [Osborne and Rubinstein 1990][book_osborne_rubinstein_1990] Bargaining and Markets. The framing treats the specific SpaceX-NASA bilateral-monopoly configuration in which the venture holds specific capability that NASA requires and NASA holds specific mission-completion authority that the venture requires, producing the specific bargaining structure that shapes the contract terms. The Nash bargaining solution for the surplus division between the anchor and the provider admits the compact form

$$(x^*_A, x^*_P) = \arg\max_{x_A + x_P \leq S} \left[(x_A - d_A)^{\alpha} \cdot (x_P - d_P)^{1 - \alpha}\right]$$

with $S$ the total surplus, $d_A, d_P$ the disagreement payoffs, and $\alpha$ the bargaining-power weight.

The absorptive-capacity framing traces from [Cohen and Levinthal 1990][research_cohen_levinthal_1990] Absorptive Capacity A New Perspective on Learning and Innovation through the subsequent extension in [Zahra and George 2002][research_zahra_george_2002] Absorptive Capacity A Review Reconceptualization and Extension, [Lane Koka and Pathak 2006][research_lane_koka_pathak_2006] The Reification of Absorptive Capacity A Critical Review, and [Todorova and Durisin 2007][research_todorova_durisin_2007] Absorptive Capacity Valuing a Reconceptualization. The framing treats the anchor-demand property through the specific firm-level capacity to identify, assimilate, and exploit anchor-imposed technical requirements. The framing captures the specific role of the SpaceX engineering-team absorptive capacity in converting the specific NASA COTS, Commercial Crew, and HLS requirements into the specific vehicle-and-spacecraft configurations across the trajectory. The absorptive-capacity intensity admits the compact operationalization

$$AC_i = f\!\left(R\&D_i, H_i^{\text{human-capital}}, T_i^{\text{network-ties}}\right)$$

with the three inputs indexing internal research-and-development intensity, human-capital stock, and external-network-tie density.

The ecosystem-strategy framing traces from [Adner 2012][book_adner_2012] The Wide Lens through [Adner 2017][research_adner_2017] Ecosystem as Structure An Actionable Construct for Strategy, [Iansiti and Levien 2004][book_iansiti_levien_2004] The Keystone Advantage, and [Jacobides Cennamo and Gawer 2018][research_jacobides_et_al_2018] Towards a Theory of Ecosystems. The framing treats the anchor-demand property through the specific coordination among the anchor customer, the provider firm, the subcontractor set, and the parallel-provider set that jointly determine the anchor-demand execution across the multi-year contract periods. The framing captures the specific ecosystem-value-appropriation

$$V_i^{\text{ecosystem}} = V_i^{\text{firm}} \cdot \phi^{\text{appropriation}}_i + V^{\text{ecosystem-total}} \cdot (1 - \phi^{\text{appropriation}}_i)$$

with $\phi^{\text{appropriation}}_i$ the specific fraction of the ecosystem value the firm captures under the specific anchor-demand configuration.

The financial-sociology framing traces from [Fligstein 2001][book_fligstein_2001] The Architecture of Markets through [Krippner 2011][book_krippner_2011] Capitalizing on Crisis, [MacKenzie 2006][book_mackenzie_2006] An Engine Not a Camera, [Ho 2009][book_ho_2009] Liquidated, [Zaloom 2006][book_zaloom_2006] Out of the Pits, and [Preda 2009][book_preda_2009] Framing Finance. The framing treats the anchor-demand property through the specific financial-market institutional configuration that shapes the accessible capital-raising terms and the specific role of the anchor-demand backlog in supporting the specific private-market capital-raising trajectory. The framing draws attention to the specific role of the CRS-1 backlog in permitting the specific Series D private-market capital round of approximately 46 million dollars in August 2009 at substantially higher valuation than would have been possible absent the anchor-demand backlog.

The reliability-engineering framing traces from [O'Connor and Kleyner 2012][book_oconnor_kleyner_2012] Practical Reliability Engineering through the specific aerospace-reliability literature including [Musa 1998][book_musa_1998] Software Reliability Engineering, [Duane 1964][research_duane_1964] Learning Curve Approach to Reliability Monitoring, and the specific NASA-standard framework in [NASA Standard 8709.22][ref_nasa_std_8709_22] on safety and mission assurance for human-rated missions. The framing treats the anchor-demand property through the specific reliability-through-iteration mechanism by which successive flight demonstrations tighten the Bayesian posterior on the underlying reliability parameter and support the specific certification progression across the anchor-demand programs. The specific Bayesian reliability-posterior form admits

$$R^{\text{cert}}_i \mid \{n^{\text{flights}}, s^{\text{successes}}\} \sim \text{Beta}(\alpha_0 + s^{\text{successes}}, \beta_0 + n^{\text{flights}} - s^{\text{successes}})$$

with successive flight outcomes tightening the posterior distribution and supporting the specific certification decisions.

The complexity and systems-of-systems framing developed in the [Maier 1998][research_maier_1998] Architecting Principles for Systems-of-Systems and [Sage and Cuppan 2001][research_sage_cuppan_2001] On the Systems Engineering and Management of Systems of Systems literature frames the anchor-demand configuration through the specific coupling between the launch-vehicle subsystem, the spacecraft subsystem, the ground-infrastructure subsystem, the anchor-customer requirements subsystem, and the regulatory-review subsystem that jointly determine the specific mission-execution outcomes. The framing captures the specific complexity of the multi-program anchor-demand portfolio and the specific system-integration challenges the SpaceX trajectory addressed at each anchor-program rung. The specific [INCOSE 2015][ref_incose_handbook] Systems Engineering Handbook provides the specific engineering-process framework within which the specific anchor-demand execution operates. The Nash bargaining solution for the surplus division between the anchor and the provider admits the compact form

$$(x^*_A, x^*_P) = \arg\max_{x_A + x_P \leq S} \left[(x_A - d_A)^{\alpha} \cdot (x_P - d_P)^{1 - \alpha}\right]$$

with $S$ the total surplus, $d_A, d_P$ the disagreement payoffs, and $\alpha$ the bargaining-power weight. The Rubinstein alternating-offers extension yields the specific equilibrium division

$$x^*_A = \frac{1 - \delta_P}{1 - \delta_A \delta_P} \cdot S$$

with $\delta_A, \delta_P$ the discount factors of the anchor and provider, respectively, and the equilibrium share favoring the more patient party under the discount-factor comparison.

## The 2008 Near-Death Moment

The 2008 near-death moment for the SpaceX firm followed the third consecutive Falcon 1 launch failure on August 3 2008 and preceded the specific anchor-demand transition on December 23 2008. The period is documented in the [Berger 2021][book_berger_2021] Liftoff first-hand account, the [Vance 2015][book_vance_2015] Elon Musk biography, the [Isaacson 2023][book_isaacson_2023] Elon Musk biography, and the specific SpaceX financial statements the trade press has since reconstructed.

The specific financial state of the SpaceX firm as of August 2008 reflected the accumulated capital consumption across the six-year Falcon 1 development. The firm had consumed approximately 100 million dollars of founder capital plus approximately 40 million dollars of external investment across the pre-2008 period, leaving approximately 4 to 6 million dollars in remaining cash and no assured capital pipeline as of the third Falcon 1 launch failure. The specific burn rate at the time was approximately 2 to 3 million dollars per month, providing approximately two months of runway before insolvency. The cash-runway condition satisfied

$$\text{runway}_{\text{Aug 2008}} = \frac{K^{\text{cash}}_{\text{remaining}}}{\dot{B}^{\text{burn}}} \approx \frac{5 \text{ M dollars}}{2.5 \text{ M dollars/month}} \approx 2 \text{ months}$$

which was substantially shorter than the time required for either an emergency financing round to close or the corrective-action-plus-fourth-launch cycle to complete. The [Berger 2021][book_berger_2021] narrative documents the specific cash-position tracking during the period.

The specific cumulative-capital-consumed trajectory across the pre-2008 period admits the compact tabulation

$$K^{\text{cum}}(t_{\text{Aug 2008}}) = K^{\text{founder}} + \sum_{r=1}^{R^{\text{rounds}}} I_r \approx 100 \text{ M dollars} + 40 \text{ M dollars} = 140 \text{ M dollars}$$

with the specific residual cash approximately 5 million dollars representing approximately 3.6 percent of the accumulated capital consumption.

The parallel Tesla Motors financial state was similarly critical, with the firm having consumed approximately 145 million dollars in Roadster development and facing specific production-quality challenges that had delayed the operational-vehicle delivery cadence. The specific cross-firm capital-allocation problem the founder faced admits the compact form

$$\max_{K_{\text{SpaceX}}, K_{\text{Tesla}}} \big[u(V^{\text{SpaceX}}(K_{\text{SpaceX}})) + u(V^{\text{Tesla}}(K_{\text{Tesla}}))\big] \quad \text{s.t.} \quad K_{\text{SpaceX}} + K_{\text{Tesla}} \leq K^{\text{founder-total}}$$

with the specific constraint approximately 100 million dollars total founder-capital remaining after the PayPal exit and prior investments in both firms. The founder held substantial ownership positions in both firms and faced the specific personal-financial constraint of choosing between the two firms or attempting to sustain both. The [Vance 2015][book_vance_2015] and [Isaacson 2023][book_isaacson_2023] biographies document the specific personal-financial constraint and the founder's decision to distribute his remaining approximately 100 million dollars of personal capital across both firms rather than concentrating on either.

The specific NASA relationship as of August 2008 included the ongoing Space Act Agreement under the [COTS Round 1 award of August 2006][ref_nasa_cots_solicitation_2006] that provided milestone-payment structure conditional on demonstrated milestone completion. The specific milestone-completion status as of August 2008 included the initial design-review milestones that had been achieved and the pending vehicle-demonstration milestones that required orbital launch success. The specific NASA program-office assessment of the SpaceX capability was under active review following the three consecutive launch failures, with specific decision authority over the continuation of the Space Act Agreement resting with the NASA associate administrator for space operations. The specific launch-vehicle-development context within which the Falcon 1 program admits placement is developed in the [History of Rocketplanes article][related_post_a96_history_rocketplanes] treatment of the launch-vehicle lineage.

The specific SpaceX response to the near-death moment included the emergency-financing round the founder personally negotiated and the accelerated fourth Falcon 1 launch preparation. The specific launch schedule compressed the standard multi-month post-failure investigation and corrective-action timeline into approximately eight weeks between the August 3 2008 third failure and the September 28 2008 fourth attempt, with the corrective actions targeted at the specific engine-tail-off transient that had caused the stage-separation collision.

The fourth Falcon 1 launch attempt on September 28 2008 achieved orbital velocity and constituted the first privately-developed liquid-propellant launch vehicle to reach orbit, as documented in the [SpaceX press release on the Falcon 1 flight 4 success][ref_spacex_press_falcon1_flight4_2008]. The value-gradient trajectory that the [Value Gradient article A282][related_post_a282_spacex_value_gradient] treats in detail was preserved through the specific fourth-flight success, and the specific anchor-demand transition that this article treats followed within approximately three months.

## The COTS-1 Salvation of December 2008

The Commercial Resupply Services CRS-1 contract award on December 23 2008 constituted the specific anchor-demand transition moment for the SpaceX firm. The contract award is documented in the [NASA CRS-1 Award Announcement][ref_nasa_crs1_press_2008], the subsequent [GAO 2011 Commercial Cargo Program evaluation][ref_gao_cots_2011], the [NASA COTS 2011 Program History][ref_nasa_cots_2011], and the [NASA Office of Inspector General 2013 COTS Program evaluation][ref_nasa_oig_cots_2013].

The specific CRS-1 contract terms awarded SpaceX approximately 1.6 billion dollars covering twelve cargo missions to the International Space Station across the 2010 through 2016 period. The parallel award to Orbital Sciences for the Antares-Cygnus configuration was approximately 1.9 billion dollars covering eight cargo missions. The specific per-mission price ranged from approximately 133 million dollars per mission for SpaceX to approximately 238 million dollars per mission for Orbital Sciences, reflecting the specific vehicle-configuration and payload-capacity differences. The specific CRS-1 per-mission-price differential admits the compact form

$$\Delta P^{\text{per-mission}}_{\text{CRS-1}} = P^{\text{Orbital}} - P^{\text{SpaceX}} = 238 - 133 = 105 \text{ M dollars per mission}$$

with the specific 44 percent price differential providing the specific competitive-provider structure that the multi-provider redundancy requirement supports.

The CRS-1 contract present-value structure admits the compact form

$$PV^{\text{CRS-1}}_{\text{SpaceX}} = \sum_{k=1}^{12} \frac{P_k^{\text{mission}}}{(1 + r)^{t_k}} \approx 1.6 \text{ billion dollars}$$

with the per-mission payments scheduled across the six-year execution period and the discount rate typically approximately 5 to 8 percent for the specific cargo-services contract discounting.

The specific contract-award timing four days after the successful fourth Falcon 1 launch reflected the specific NASA program-office judgment that the SpaceX firm had demonstrated the required technical capability to conduct the subsequent Falcon 9 and Dragon development. The specific alternative provider set from which NASA selected the CRS-1 awardees included Orbital Sciences, SpaceX, and the Lockheed Martin ATK Rocketplane consortium that had proposed a modified Athena configuration. The specific selection of SpaceX over the alternative providers reflected the specific per-mission price, the specific technical demonstration achieved through the Falcon 1 orbital success, and the specific milestone-completion progress under the COTS Round 1 Space Act Agreement. The specific procurement-mechanism analog for large-program sole-source authority appears in the [SBIR Phase III article][related_post_a138_sbir_phase3] treatment of the sole-source authority framework, and the specific comprehensive SBIR-program context is developed in the [SBIR series opener][related_post_a132_sbir_intro].

The specific CRS-1 contract structure adopted the fixed-price milestone-payment mechanism under the Federal Acquisition Regulation framework rather than the Space Act Agreement authority that the earlier COTS Round 1 award had used. The transition from Space Act Agreement to FAR-based procurement reflected the specific NASA requirement for the operational cargo-services contract to satisfy standard federal-procurement requirements, though the fixed-price structure was preserved. The specific provider selection utility function that NASA applied admits the compact form

$$U^{\text{selection}}_j = w^{\text{price}} \cdot (-P_j) + w^{\text{technical}} \cdot T_j + w^{\text{schedule}} \cdot S_j + w^{\text{risk}} \cdot (-R_j)$$

with the specific weight vector reflecting the specific mission-critical requirements of the ISS-servicing category and each provider's specific price, technical merit, schedule, and risk scoring. The [NASA COTS Report][ref_nasa_cots_report] documents the specific procurement-transition rationale.

The specific value-realization impact of the CRS-1 contract on the SpaceX firm was substantial and immediate. The specific balance-sheet impact converted the firm from a development-stage venture with limited commercial-revenue prospects to a firm with a multi-year anchored revenue backlog that supported the subsequent Falcon 9 and Dragon development. The specific balance-sheet transition admits the compact form

$$\Delta V^{\text{enterprise}}_{\text{Dec 2008}} \approx V^{\text{post-CRS-1}} - V^{\text{pre-CRS-1}} \approx 1.6 \text{ B backlog} \cdot \mu^{\text{value-realization}}$$

with $\mu^{\text{value-realization}}$ the specific fraction of the contract present value the equity market ascribes to the enterprise value at the specific award moment, typically approximately 0.3 to 0.5 for the specific pre-execution contract. The specific capital-market impact permitted the firm to raise the subsequent Series D private-market capital round of approximately 46 million dollars in August 2009 at substantially higher valuation than would have been possible absent the CRS-1 backlog. The specific capability-market impact positioned the firm as the specific COTS Round 1 anchor provider for the subsequent Commercial Crew Program competition.

The specific COTS demonstration missions that preceded the operational CRS-1 execution included COTS Demo 1 on December 8 2010 documented in the [SpaceX press release on the Dragon C1 mission][ref_spacex_press_dragon_c1_2010] and COTS Demo 2/3 on May 22 2012 that combined the specific Dragon rendezvous and berthing milestones with the International Space Station. The specific Demo 1 mission validated the Dragon spacecraft pressurized-cargo configuration, propulsion system, thermal-protection system, parachute deployment, and ocean-recovery procedures. The specific Demo 2/3 mission validated the rendezvous, proximity-operations, and berthing procedures required for the operational cargo-services execution.

## Cargo Resupply Services Execution 2008-2026

The Cargo Resupply Services execution from the initial CRS-1 mission on October 8 2012 through the contemporary operational cadence constitutes the specific anchor-demand execution across the CRS-1 and CRS-2 rounds. The execution is documented in the specific NASA mission-summary reports, the [GAO 2011 Commercial Cargo Program evaluation][ref_gao_cots_2011], and the [NASA Office of Inspector General 2018 Commercial Cargo Program evaluation][ref_nasa_oig_ccp_cargo_2018].

The specific CRS-1 mission execution proceeded from the initial [CRS-1 mission on October 8 2012][ref_spacex_press_crs1_2012] through approximately twenty operational missions across the extended-CRS-1 contract period. The mission cadence trajectory admits the compact form

$$\dot{q}^{\text{CRS}}_{\text{SpaceX}}(t) = q^{\text{CRS,initial}} + g^{\text{cadence}} \cdot t$$

with $q^{\text{CRS,initial}}$ approximately 2 missions per year in the initial 2012-2014 period and $g^{\text{cadence}}$ approximately 0.3 missions per year cadence growth across the trajectory, converging to the approximately 3 to 5 missions per year contemporary cadence. The [CRS-7 mission on June 28 2015][ref_spacex_press_crs7_2015] experienced a Falcon 9 second-stage overpressure event that destroyed the Dragon spacecraft and its cargo approximately 139 seconds after launch. The reliability posterior update after the specific CRS-7 loss admits the compact form

$$R^{\text{CRS-7 post-loss}} \mid \{n = 7, s = 6\} \sim \text{Beta}(1 + 6, 1 + 1) = \text{Beta}(7, 2)$$

with posterior mean approximately 0.78 under uniform prior. The subsequent NASA and SpaceX investigation identified the specific strut-failure mechanism in the second-stage helium pressure vessel and produced the specific corrective actions that the subsequent CRS missions incorporated.

The Commercial Resupply Services 2 solicitation was announced in 2014 with awards on January 14 2016 to SpaceX, Orbital ATK, and Sierra Nevada Corporation as documented in the [NASA CRS-2 Award Announcement][ref_nasa_crs2_press_2016]. The specific CRS-2 award to SpaceX covered approximately six additional missions across the 2019 through 2024 period at approximately 4.3 billion dollars total across the three providers. The specific inclusion of Sierra Nevada Corporation as a third provider using the Dream Chaser lifting-body configuration reflected the specific NASA requirement for provider diversity in the mission-critical cargo-services category.

The Dragon 2 cargo configuration first flew on the [CRS-21 mission on December 6 2020][ref_spacex_press_crs21_2020] as the specific successor to the Dragon 1 cargo configuration, incorporating the design improvements from the Dragon 2 crew configuration and adopting the autonomous docking mechanism rather than the Canadarm2 berthing procedure the Dragon 1 configuration had required. The specific Dragon 2 cargo configuration extended the payload-return capacity and reduced the specific International Space Station crew workload for the cargo-handling operations. The specific payload-capacity improvement admits the compact form

$$\frac{m^{\text{payload}}_{\text{Dragon 2 cargo}}}{m^{\text{payload}}_{\text{Dragon 1 cargo}}} \approx \frac{6000 \text{ kg}}{3310 \text{ kg}} \approx 1.81$$

with the specific approximately 81 percent payload-mass improvement enabling the reduced mission cadence required for equivalent cargo delivery.

The contemporary CRS execution cadence as of the drafting date includes approximately three to five SpaceX cargo missions per year, with the specific mission-manifest coordination between the SpaceX and Northrop Grumman providers reflecting the specific NASA International Space Station operational-planning requirements. The multi-provider redundancy premium the specific NASA cargo-services procurement supports admits the compact form

$$\Delta P^{\text{redundancy}} = P^{\text{multi-provider-set}} - P^{\text{single-provider-competitive}} > 0$$

which quantifies the transitional-period margin the anchor pays to sustain the redundancy that mission-critical categories require. The specific extension of the ISS operational period through 2030 under the current NASA plan provides the specific anchor-demand continuity for the SpaceX cargo-services line across the additional operational horizon.

## Commercial Crew Program 2014-2026

The Commercial Crew Program constitutes the specific anchor-demand extension from cargo services to human-rated crew services across the 2010 through 2026 period. The program is documented in the [NASA Commercial Crew Program 2014][ref_nasa_ccp_2014] framework, the [GAO 2019 Commercial Crew Program evaluation][ref_gao_ccp_2019], the [NASA Office of Inspector General 2019 Commercial Crew Program evaluation][ref_nasa_oig_ccp_2019], and the [CRS 2018 Commercial Crew Program report][ref_crs_commercial_crew_2018].

The specific Commercial Crew Program progression proceeded from the Commercial Crew Development Round 1 CCDev-1 in 2010 through the Commercial Crew Development Round 2 CCDev-2 in 2011, the Commercial Crew Integrated Capability CCiCap in 2012, and the Commercial Crew Transportation Capability CCtCap in 2014. Each program round expanded the specific development-milestone completion under the specific Space Act Agreement authority, culminating in the specific fixed-price operational-services contract that the CCtCap round awarded.

The specific CCtCap award on September 16 2014 documented in the [NASA CCtCap Award Announcement][ref_nasa_cctcap_press_2014] provided approximately 4.2 billion dollars to Boeing for the Starliner spacecraft and approximately 2.6 billion dollars to SpaceX for the Dragon 2 spacecraft across the specific certification and operational-mission phases. The specific price differential between the two providers admits the compact form

$$\Delta P^{\text{CCtCap}}_{\text{Boeing vs SpaceX}} = 4.2 - 2.6 = 1.6 \text{ B dollars}$$

with the specific 62 percent Boeing premium reflecting the specific vehicle-configuration and per-mission price differences. The per-seat cost calculation admits the compact form

$$P^{\text{per-seat}}_i = \frac{P^{\text{per-mission}}_i}{n^{\text{seats-per-mission}}_i}$$

with $n^{\text{seats-per-mission}} = 4$ typical for the Commercial Crew rotation missions. Under the specific SpaceX approximately 262 million dollars per crew-mission and the specific Boeing approximately 654 million dollars per crew-mission, the specific per-seat cost is approximately 65 million dollars for SpaceX and approximately 163 million dollars for Boeing across the specific price-per-seat calculation.

The certification-timeline differential between SpaceX and Boeing admits the compact tabulation

$$\Delta T^{\text{cert}}_{\text{Boeing vs SpaceX}} = T^{\text{Boeing operational}} - T^{\text{SpaceX operational}}$$

with the specific SpaceX operational Demo-2 mission on May 30 2020 preceding the specific Boeing Crewed Flight Test on June 5 2024 by approximately four years, illustrating the specific execution-differential the two providers exhibited under the specific CCtCap program.

The [SpaceX Demo-1 uncrewed demonstration mission on March 2 2019][ref_spacex_press_demo1_2019] validated the specific rendezvous and docking capability required for the subsequent crewed mission through the Dragon 2 spacecraft autonomous docking at the International Space Station. The specific SpaceX Demo-2 crewed demonstration mission occurred on May 30 2020 with astronauts Robert Behnken and Douglas Hurley aboard, constituting the first commercial-provider crewed launch to the International Space Station and the first United States crewed launch from United States soil since the July 8 2011 Space Shuttle Atlantis final flight, as documented in the [SpaceX press release on the Demo-2 mission][ref_spacex_press_dm2_2020].

The specific SpaceX operational Commercial Crew missions began with the [Crew-1 mission on November 15 2020][ref_spacex_press_crew1_2020] and have continued through the specific ongoing rotation of ISS crew personnel. The operational missions include Crew-1 through the contemporary mission at the drafting date, with each mission carrying four astronauts for the approximately six-month rotation. The specific Boeing Starliner operational timeline has faced substantial development delay and cost overrun, with the [Boeing Crewed Flight Test occurring on June 5 2024][ref_boeing_starliner_cft_2024] with specific subsequent thruster-and-helium-leak issues that required the uncrewed return of the Starliner vehicle to Earth without the astronauts.

The specific SpaceX Commercial Crew market position as of the drafting date reflects the specific execution differential between the two providers, with SpaceX having conducted substantially more operational missions than Boeing and having established the specific crew-rotation cadence that the ISS operational requirements demand. The [SpaceX Falcon 9 User's Guide][ref_spacex_falcon9_users_guide] documents the specific vehicle-configuration that supports the specific Commercial Crew operational execution, and the [SpaceX Starship User's Guide][ref_spacex_starship_program] documents the specific successor-vehicle configuration under development for the specific HLS mission architecture. The reliability posterior after the specific SpaceX crewed flight record admits the Beta-posterior form

$$R^{\text{SpaceX-crew}} \mid \{n^{\text{SpaceX-crewed}}, s^{\text{SpaceX-crewed}}\} \sim \text{Beta}(\alpha_0 + s^{\text{SpaceX-crewed}}, \beta_0 + n^{\text{SpaceX-crewed}} - s^{\text{SpaceX-crewed}})$$

with the specific successive-mission accumulation tightening the posterior distribution and supporting the specific NASA certification progression for the additional Commercial Crew operational missions.

## Human Landing System Artemis 2021-2026

The Human Landing System Artemis Program constitutes the specific anchor-demand extension from ISS-orbit crew services to lunar-surface crew transportation across the 2019 through 2026 period. The program is documented in the [NASA HLS Option A Award Announcement][ref_nasa_hls_optionA_2021], the subsequent [NASA HLS Sustaining Award Announcement][ref_nasa_hls_sustaining_2023], the [GAO 2022 Human Landing System evaluation][ref_gao_hls_2022], the [NASA Office of Inspector General 2021 Human Landing System evaluation][ref_nasa_oig_hls_2021], and the specific [GAO 2021 Blue Origin HLS protest decision][ref_gao_blue_origin_hls_protest_2021].

The specific HLS solicitation began in 2019 under the Vice President-directed acceleration of the Artemis Program lunar-return timeline to 2024. The specific solicitation received proposals from SpaceX, Blue Origin, and Dynetics, with the specific initial ten-month base-period awards announced in 2020 distributing development funding across all three providers.

The specific HLS Option A award on April 16 2021 documented in the [NASA HLS Option A Award Announcement][ref_nasa_hls_optionA_2021] selected SpaceX as the sole provider for the specific Artemis III lunar landing at approximately 2.89 billion dollars. The specific per-provider allocation across the initial ten-month base period admits the compact tabulation

$$\text{allocation}_j^{\text{HLS base}} = \{\text{SpaceX}: 135 \text{ M}, \, \text{Blue Origin}: 579 \text{ M}, \, \text{Dynetics}: 253 \text{ M}\}$$

with the specific Option A award subsequently concentrating the funding on the SpaceX provider. The specific selection reflected the specific technical evaluation that identified the SpaceX Starship configuration as the highest-technical-merit lowest-price proposal.

The Blue Origin protest to the specific Option A award was filed on April 26 2021 and denied by the Government Accountability Office in the [decision of July 30 2021][ref_gao_blue_origin_hls_protest_2021]. The subsequent Blue Origin lawsuit in the United States Court of Federal Claims was dismissed on November 4 2021, with the court finding no material impropriety in the specific NASA source-selection decision. The specific extended review-and-litigation period delayed the operational contract execution by approximately eight months. The delay-cost estimation admits the compact form

$$\Delta C^{\text{litigation-delay}} \approx r \cdot V^{\text{contract}} \cdot \Delta T^{\text{delay}} = 0.08 \cdot 2.89 \text{ B dollars} \cdot 0.67 \text{ years} \approx 155 \text{ M dollars}$$

with the specific discount-rate approximately 8 percent and the delay approximately 8 months, illustrating the specific opportunity-cost the protest-and-litigation period imposed on the contract execution.

The [NASA HLS Option B award announcement on November 15 2022][ref_nasa_hls_optionB_2022] provided approximately 1.15 billion dollars additional to SpaceX for the specific Artemis IV lunar landing configuration, incorporating additional cargo-delivery capability and extended lunar-surface duration.

The specific NASA HLS Sustaining lunar transportation announcement on May 19 2023 selected Blue Origin as the specific second provider for the sustaining lunar-transportation architecture across subsequent Artemis missions at approximately 3.4 billion dollars, providing the specific provider-diversity that the mission-critical crew-transportation category requires. The specific inclusion of Blue Origin as a second provider addressed the specific Government Accountability Office recommendation from the [GAO 2022 Human Landing System evaluation][ref_gao_hls_2022] and the [CRS 2022 Artemis Program report][ref_crs_artemis_2022] that identified single-provider concentration as a specific risk. The specific historical HLS-and-lunar-transportation context is developed in the [Bilstein 1996][book_bilstein_1996] Stages to Saturn treatment of the Apollo lunar-transportation architecture and the [Chaikin 2007][book_chaikin_2007] A Man on the Moon treatment of the Apollo mission execution. The multi-provider portfolio-share tabulation after the specific sustaining award admits the compact form

$$\text{portfolio-share}^{\text{HLS post-sustaining}} = \{\text{SpaceX}: 4.04 \text{ B}, \, \text{Blue Origin}: 3.4 \text{ B}\}$$

with the specific share allocation approximately 54 percent to SpaceX and approximately 46 percent to Blue Origin across the specific total 7.44 billion dollars of specific HLS commitment.

The specific Starship HLS testing across the 2023 through 2026 period includes the specific integrated flight tests of the Starship vehicle at the Boca Chica Starbase launch site as documented in the [SpaceX Starship program page][ref_spacex_starship_program], with the specific test-cadence acceleration approaching the operational-cadence achievement the Artemis III mission requires. The specific reliability posterior required for the specific Artemis III crew authorization satisfies

$$R^{\text{HLS-crew-cert}} \geq R^{\text{human-rated threshold}} \approx 0.9995$$

with the specific human-rated reliability threshold requiring substantial flight-test count accumulation before the specific crew authorization can proceed.

## Starshield and National Security Anchor Portfolio 2022-2026

The Starshield defense-service line announced in December 2022 constitutes the specific anchor-demand extension from civilian NASA-directed services to classified national-security services across the 2022 through 2026 period. The program is documented in the specific SpaceX Starshield product-page announcement, the specific Space Force announcements, and the specific trade-press coverage that has reconstructed the classified elements of the program.

The specific Starshield product structure includes three primary components documented in the [SpaceX Starshield product page][ref_spacex_starshield]. First, the Earth-Observation component provides high-resolution optical and radar-imaging capability for classified customers including the National Reconnaissance Office. Second, the Communications component provides secure end-to-end encrypted communications capability for defense and intelligence customers. Third, the Hosted Payloads component provides platform services for customer-specific payloads on Starshield satellite buses. The specific [FCC Starlink Generation 2 authorization of December 2022][ref_fcc_starlink_gen2_2022] and the earlier [FCC Starlink authorization of March 2018][ref_fcc_starlink_2018] provide the specific spectrum-authorization framework within which the Starshield configuration operates, with the specific defense-service exemptions and classifications documented in the [FCC filings database][ref_fcc_filings].

The specific National Reconnaissance Office relationship reportedly includes a contract of approximately 1.8 billion dollars announced in 2021 for the specific classified satellite constellation that the trade-press coverage has reconstructed as the Starshield Earth-Observation configuration. The specific classified constellation deployment has proceeded across multiple Falcon 9 missions with specific mission designation as classified national-security payloads. The [Reuters 2024][research_reuters_starshield_2024] investigation and subsequent [New York Times 2024][ref_nyt_starshield_2024] reporting documented the specific program structure.

The specific Space Force National Security Space Launch program certification progression provided the specific launch-services anchor for the SpaceX firm across the parallel Phase 1A, Phase 2, and Phase 3 Lane 2 award periods. The specific [Space Force NSSL Phase 1A award of 2018][ref_space_force_nssl_phase1a_2018] added SpaceX to the specific NSSL Phase 1A provider set alongside the United Launch Alliance incumbent. The specific [Space Force NSSL Phase 2 award of August 2020][ref_space_force_nssl_phase2_2020] provided approximately 40 percent of the specific NSSL Phase 2 launch missions to SpaceX with the specific remaining 60 percent to ULA across the fiscal year 2020 through 2024 mission set. The Phase 2 allocation admits the compact tabulation

$$\text{NSSL Phase 2 share} = \{\text{SpaceX}: 0.40, \, \text{ULA}: 0.60\}$$

The specific [Space Force NSSL Phase 3 Lane 2 award of October 2024][ref_spacenews] added Blue Origin as a specific third provider alongside SpaceX and ULA, with the specific SpaceX allocation approximately 60 percent of the total Phase 3 Lane 2 launch mass. The Phase 3 Lane 2 allocation admits the compact tabulation

$$\text{NSSL Phase 3 Lane 2 share} = \{\text{SpaceX}: 0.60, \, \text{ULA}: 0.25, \, \text{Blue Origin}: 0.15\}$$

with the specific concentration index by launch mass

$$\text{HHI}^{\text{NSSL Phase 3 Lane 2}} = \sum_i s_i^2 = 0.60^2 + 0.25^2 + 0.15^2 = 0.445$$

reflecting the specific SpaceX-dominant concentration under the specific certification-and-execution differential.

The specific direct-to-cell partnership announced in August 2022 with T-Mobile documented in the [T-Mobile Coverage Above and Beyond release][ref_spacex_starlink_direct_to_cell_tmobile_2022] and the specific subsequent [FCC direct-to-cell authorization][ref_fcc_direct_to_cell_2024] added the specific commercial-communication service line that operates in parallel with the Starshield defense-communication service line. The specific [International Traffic in Arms Regulations codified at 22 CFR Parts 120 through 130][ref_itar_22_cfr_120_130] govern the specific export-control restrictions on the specific launch-vehicle and satellite technical data across the anchor-demand configuration. The specific [International Telecommunication Union Radio Regulations][ref_itu_radio_regulations_2020] govern the international-level spectrum-coordination requirements. The specific technical architecture uses common Starlink satellite bus hardware with specific service-provider software differentiation. The specific commercial-defense revenue-sharing across the shared-bus configuration admits the compact form

$$R^{\text{shared-bus total}} = R^{\text{Starlink-commercial}} + R^{\text{Starshield-defense}} \cdot (1 + \phi^{\text{shared-cost-recovery}})$$

with $\phi^{\text{shared-cost-recovery}}$ the specific defense-customer premium that recovers the shared-cost allocation.

The specific ballistic-missile-defense architecture referenced in the specific 2025 Golden Dome policy discussion has generated additional specific anchor-demand potential for the SpaceX firm through the specific Starshield configuration adaptation and the specific space-based interceptor capability that the specific architecture requires. The specific contract-level implementation of the Golden Dome architecture remains under development as of the drafting date.

The anchor-demand portfolio diversification index across the SpaceX anchor programs as of the drafting date admits the compact form

$$\text{HHI}^{\text{anchor-portfolio}}_{\text{SpaceX}} = \sum_k \left(\frac{D_{i,k}^{\text{anchor}}}{D_i^{\text{anchor-total}}}\right)^2$$

with the specific anchor programs including NASA CRS, NASA Commercial Crew, NASA HLS, Space Force NSSL, and Starshield. Under industry-analyst estimates of the approximate revenue contribution from each program, the specific HHI is approximately 0.25 to 0.35, indicating substantial diversification across the anchor-portfolio and substantially reduced single-anchor concentration relative to the pre-2020 configuration when NASA CRS was the dominant anchor.

## Deep Historical Comparative Precedents

The anchor-demand mechanic admits comparison with several deep historical precedents that illustrate the specific pattern across earlier eras and adjacent domains. The precedents establish the anchor-demand property as a load-bearing feature of mission-directed technology development rather than a SpaceX-specific innovation.

The Boeing Air Mail Contract history from the 1927 Contract Air Mail Route 18 through the specific mid-1930s consolidation illustrates the canonical anchor-demand pattern in commercial-aviation development. The specific United States Post Office Department air-mail contracts provided the specific initial anchor-demand for the emerging commercial-aviation providers including United Aircraft and Transport Corporation, American Airways, Transcontinental and Western Air, and Eastern Air Transport. The specific anchor-demand transition from government air-mail contracts to commercial passenger-service revenue proceeded across the 1930s and established the specific competitive-firm structure that has subsequently defined the United States commercial-aviation sector. The [Serling 1992][book_serling_1992] Legend and Legacy documents the specific Boeing trajectory across the period. The [Crouch 2003][book_crouch_2003] Wings A History of Aviation from Kites to the Space Age provides the specific commercial-aviation-sector treatment within which the Boeing trajectory admits placement, and the [Bilstein 2001][book_bilstein_2001] Flight in America documents the specific United States commercial-aviation-sector development.

The Colt firearms military-contract anchor from the specific 1836 Colt Paterson through the Mexican-American War 1846-1848 contracts illustrates the specific anchor-demand pattern in interchangeable-parts manufacturing. The specific United States Army contract for Colt Walker revolvers during the war provided the specific initial anchor-demand that established the Colt Manufacturing Company as an operational firm. The specific Colt Walker contract of January 1847 provided approximately 1000 revolvers at approximately 28 dollars per unit for total approximately 28000 dollars, admitting the compact anchor-value-versus-founder-capital ratio

$$\rho^{\text{Colt anchor/founder}} = \frac{V^{\text{Walker contract}}}{V^{\text{founder capital pre-contract}}} \gg 1$$

with the specific ratio substantially exceeding unity reflecting the specific transformation of the venture's financial state through the anchor-demand transition. The [Hosley 1996][book_hosley_1996] Colt The Making of an American Legend documents the specific trajectory.

The Eli Whitney interchangeable-parts musket contract of 1798 illustrates the deep-historical precedent for the specific state-directed technology development pattern. The specific United States War Department contract for 10000 muskets across a ten-year period established the specific manufacturing infrastructure that subsequently developed the interchangeable-parts production system that transformed the specific manufacturing sector. The specific contract-value-per-year trajectory admits the compact form

$$V^{\text{Whitney annual}} = \frac{V^{\text{contract-total}}}{T^{\text{execution period}}} = \frac{134000 \text{ dollars}}{10 \text{ years}} = 13400 \text{ dollars per year}$$

with the specific annual contract value providing sustained anchor-demand across the ten-year execution period that supported the specific manufacturing-methodology development. The [Hounshell 1984][book_hounshell_1984] From the American System to Mass Production documents the specific trajectory.

The Boeing B-17, B-29, KC-135, and 707 progression illustrates the specific anchor-demand-to-commercial-spinoff pattern that the SpaceX case now replicates in the space-launch sector. The specific B-17 and B-29 wartime heavy-bomber contracts established the specific manufacturing infrastructure that subsequently developed the KC-135 military tanker and the 707 commercial airliner. The specific anchor-to-spinoff ratio for the Boeing case admits the compact form

$$\rho^{\text{Boeing spinoff}} = \frac{V^{\text{commercial-airliner spinoff}}}{V^{\text{military-contract anchor}}}$$

with the specific commercial-airliner value across the multi-decade 707 through 787 product line substantially exceeding the specific military-contract anchor value, illustrating the specific spinoff-return magnitude the anchor-demand pattern can produce. The [Serling 1992][book_serling_1992] Legend and Legacy and [Newhouse 1982][book_newhouse_1982] The Sporty Game document the trajectory.

The Lockheed Skunk Works P-80 through F-117 anchor-demand progression illustrates the specific pattern of sustained state-directed classified-project anchor demand that maintained the specific engineering-organization capability across the multi-decade period. The [Rich and Janos 1994][book_rich_janos_1994] Skunk Works and [Miller 1995][book_miller_1995] Lockheed Skunk Works The First Fifty Years document the specific trajectory across the multiple project phases. The specific P-80, U-2, SR-71, and F-117 projects each provided specific mission-directed anchor demand that supported the Skunk Works organizational form. The specific inter-project anchor-continuity condition admits the compact form

$$\text{gap}(k, k+1) = t^{\text{start},k+1} - t^{\text{end},k} < \Delta T^{\text{organizational-persistence}}$$

with the specific gap between successive projects required to remain below the specific organizational-persistence threshold to maintain the specific engineering-team capability. The [Rich and Janos 1994][book_rich_janos_1994] Skunk Works documents the trajectory.

The Northrop B-2 Spirit anchor-demand pattern from the 1981 program initiation through the specific operational-configuration production illustrates the specific single-anchor-single-provider bilateral-monopoly structure that raises the transaction-cost-economics concerns the framing identifies. The specific twenty-one B-2 aircraft delivered at approximately 2 billion 1997 dollars per unit reflected the specific negotiating structure between the specific United States Air Force customer and the specific Northrop-Grumman prime-contractor provider. The [Fallows 1981][book_fallows_1981] National Defense treatment provides the specific analytical framework within which the specific B-2 procurement admits interpretation, and the [Kaplan 1991][book_kaplan_1991] The Wizards of Armageddon provides the specific Cold War strategic-context treatment within which the specific B-2 mission articulation admits placement.

The specific Apollo Program contractor anchor pattern including North American Aviation, Grumman, Boeing, Rocketdyne, and IBM illustrates the specific state-directed program anchor demand across the multi-provider prime-contractor set. The specific Apollo Guidance Computer development that supported the Apollo mission execution is developed in the [Apollo Guidance Computer article][related_post_a242_apollo_guidance], and the specific aerospace-computing historical trajectory within which the Apollo lineage admits placement is developed in the [Aerospace, Programming Languages, and Information Technology Co-Development series opener][related_post_a237_aerospace_framing]. The Apollo contractor-share concentration admits the compact form

$$s^{\text{Apollo contractor}}_j = \frac{V^{\text{prime-contract}}_j}{\sum_k V^{\text{prime-contract}}_k}$$

with the specific shares distributed across the prime-contractor set as documented in the [Bilstein 1996][book_bilstein_1996] Stages to Saturn treatment. The specific per-contractor anchor demand supported the specific capability development that the [Chaikin 2007][book_chaikin_2007] A Man on the Moon and [Murray and Cox 1989][book_murray_cox_1989] Apollo document. The [Mindell 2008][book_mindell_2008] Digital Apollo treatment provides the specific Apollo Guidance Computer-and-human-factors focus, and the [Neufeld 2013][book_neufeld_2013] Von Braun and [Neufeld 1995][book_neufeld_1995] The Rocket and the Reich document the specific pre-Apollo Peenemünde lineage that shaped the specific Saturn V development.

The Manhattan Project contractor anchor including E.I. du Pont, Union Carbide, Tennessee Eastman, and the specific university operators of Los Alamos, Oak Ridge, and Hanford illustrates the specific wartime-urgency anchor-demand configuration. The [Rhodes 1986][book_rhodes_1986] The Making of the Atomic Bomb, [Bird and Sherwin 2005][book_bird_sherwin_2005] American Prometheus, [Groves 1962][book_groves_1962] Now It Can Be Told, and [Hewlett and Anderson 1962][book_hewlett_anderson_1962] The New World document the specific trajectory.

The British Longitude Prize established by the Longitude Act of 1714 illustrates a specific challenge-prize anchor-demand mechanism that generated the John Harrison chronometer development completed with the H4 in 1759 and validated at sea in 1761 and 1764. The Longitude Prize offered a maximum of 20000 pounds sterling for a solution to the problem of longitude determination at sea, structured as a graduated award depending on the accuracy achieved. The prize mechanism differs from the milestone-payment anchor-demand mechanism the COTS Program adopted but shares the specific state-directed forcing-function demand for a specific technical capability. The [Sobel 1995][book_sobel_1995] Longitude and the [Andrewes 1996][book_andrewes_1996] The Quest for Longitude treatments document the prize mechanism and its outcomes.

The Venetian Arsenal from approximately 1104 through the fall of the Venetian Republic in 1797 illustrates a specific state-directed capability-investment pattern in which sustained public demand for naval vessels underwrote the accumulation of specialized industrial capability. The Arsenal at its peak employed approximately 16000 workers and produced one fully-equipped galley per day under emergency mobilization, illustrating the specific throughput the sustained anchor-demand configuration can achieve. The [Lane 1934][book_lane_1934] Venetian Ships and Shipbuilders of the Renaissance and [Concina 2006][book_concina_2006] A History of Venetian Architecture treatments document the specific Arsenal's institutional structure and the specific state-firm coordination pattern.

The Bell Laboratories under the specific AT&T regulated-monopoly funding from 1925 through the 1984 divestiture illustrates the specific research-and-development anchor-demand configuration in which sustained monopoly-rent-financed research produced the specific technical capability including the transistor 1947, information theory 1948, the C programming language 1969-1972, and the Unix operating system 1969-1973. The specific Bell Labs case illustrates the anchor-demand property in a distinct institutional configuration where the anchor is the specific parent-firm rather than an external state customer, but the specific sustained-funding-for-generic-capability structure resembles the specific COTS anchor-demand configuration. The [Gertner 2012][book_gertner_2012] The Idea Factory documents the specific trajectory.

The Airbus consortium from the 1970 founding through the specific A300, A320, A330, A340, A350, and A380 family programs illustrates the specific multi-national government-consortium-backed anchor-demand configuration that supported the specific challenger emergence to the incumbent Boeing commercial-aircraft position. The specific European Space Agency Ariane program from the 1979 first flight through the Ariane 6 introduction illustrates the specific state-consortium-backed anchor-demand configuration in the specific space-launch sector. The [McIntyre 1992][book_mcintyre_1992] Airbus Industrie and [Chadeau 1996][book_chadeau_1996] Airbus Industrie History document the specific Airbus trajectory. The [Krige et al 2000][book_krige_et_al_2000] A History of the European Space Agency documents the specific ESA trajectory. The comparative Airbus and Ariane cases illustrate the specific European institutional configuration under which the anchor-demand mechanism operates through the specific consortium structure rather than the specific United States NASA-plus-Space-Force procurement structure.

The Human Genome Project from 1990 through 2003 under the National Institutes of Health and Department of Energy joint sponsorship illustrates the specific state-directed biomedical-research anchor-demand configuration in the specific non-aerospace domain. The project achieved the reference-genome sequencing at approximately 2.7 billion 2003 dollars over thirteen years, and generated the specific commercial spinoff across the biotechnology, pharmaceutical, and personalized-medicine sectors. The parallel competing effort by the private firm Celera Genomics under Craig Venter illustrates the specific private-sector challenger dynamics that emerged from the specific state-directed program structure. The [Collins 2010][book_collins_2010] The Language of Life documents the specific trajectory.

The DARPA Grand Challenge autonomous-vehicle competition series from 2004 through 2007 illustrates the specific challenge-prize anchor-demand mechanism in the autonomous-vehicle sector. The 2004 first Grand Challenge produced no vehicle completing the 240-kilometer desert course. The 2005 second Grand Challenge produced five vehicles completing the course with Stanford Racing Team's Stanley winning in approximately 6 hours 54 minutes. The 2007 Urban Challenge produced six finishing vehicles. The specific prize mechanism differs from the CRS-1 milestone-payment mechanism but shares the specific state-directed forcing-function anchor-demand structure. The [Bonvillian 2018][research_bonvillian_2018] DARPA and the Advanced Research Projects Agency documents the specific DARPA institutional configuration.

The Toyota Production System evolution from the 1948 Ohno-directed initial development through the contemporary lean-production architecture illustrates the specific anchor-demand configuration in which specific supplier-firms operated under the specific Toyota Motor Corporation demand configuration across the multi-decade horizon. The specific Toyota-supplier relationship exhibited specific relational-contracting features that the transaction-cost-economics tradition documents, and the specific application of the Toyota Production System principles to the SpaceX manufacturing operations at the Hawthorne facility is documented in the [Berger 2024][book_berger_2024] Reentry narrative. The [Womack Jones Roos 1990][book_womack_jones_roos_1990] The Machine That Changed the World and [Liker 2004][book_liker_2004] The Toyota Way document the specific trajectory.

The International Space Station assembly from the 1998 Zarya first launch through the 2011 completion of the primary configuration illustrates the multi-decade specific state-directed international-cooperation anchor-demand configuration. The ISS assembly proceeded through approximately forty individual assembly missions across Space Shuttle, Proton, Soyuz, and subsequent Falcon 9 launches, with each mission adding specific modules, trusses, solar-array segments, and outfitting hardware. The specific anchor-demand property was realized through the incremental assembly-milestone completion that the specific NASA-Roscosmos-ESA-JAXA-CSA coordination supported across the multi-decade period.

The Panama Canal construction from 1904 through 1914 under the United States Army Corps of Engineers illustrates the specific state-directed large-scale infrastructure anchor-demand configuration under a specific geopolitical purpose. The project mobilized approximately 45000 personnel at peak, cost approximately 375 million 1914 dollars, and delivered the specific interoceanic canal capability. The [McCullough 1977][book_mccullough_1977] The Path Between the Seas documents the specific trajectory. The specific Silicon Valley industrial substrate that emerged from the defense-contracting substrate is developed in the [Silicon Valley from Defense Contracting article][related_post_a246_silicon_valley_defense], and the specific software-defined aerospace context within which contemporary aerospace anchor-demand operates is developed in the [Software-Defined Aerospace article][related_post_a247_software_defined_aerospace]. The specific broader-space context is developed in the [Introduction to Space Studies article][related_post_a90_intro_space_studies], and the specific contemporary-snapshot forward-projection context is developed in the [Contemporary Snapshot article][related_post_a248_contemporary_snapshot].

## Historiographical Gap and Recent Scholarship

The scholarly literature specifically on the SpaceX anchor-demand trajectory remains substantially thinner than the scholarly literature on the surrounding aerospace-procurement and mission-oriented-innovation contexts. The gap is partly attributable to the firm's status as a privately held company, partly to the specific classification restrictions on the national-security portions of the anchor-demand portfolio, and partly to the specific methodological challenge of separating the anchor-demand effect from the other seven-plus-three conditions.

### Primary Source Documentation

The primary source documentation for the CRS-1 anchor-demand transition includes the [NASA CRS-1 Award Announcement][ref_nasa_crs1_press_2008], the [NASA COTS 2011 Program History][ref_nasa_cots_2011], the [NASA COTS Report][ref_nasa_cots_report], the [GAO 2011 Commercial Cargo Program report][ref_gao_cots_2011], the [GAO 2009 COTS Program evaluation][ref_gao_cots_2009], the [NASA Office of Inspector General 2013 COTS Program evaluation][ref_nasa_oig_cots_2013], and the [NASA Office of Inspector General 2018 Commercial Cargo Program evaluation][ref_nasa_oig_ccp_cargo_2018]. The primary source documentation for the Commercial Crew Program includes the [NASA Commercial Crew Program 2014 documentation][ref_nasa_ccp_2014], the [NASA CCtCap Award Announcement][ref_nasa_cctcap_press_2014], the [GAO 2019 Commercial Crew Program evaluation][ref_gao_ccp_2019], the [NASA Office of Inspector General 2019 Commercial Crew Program evaluation][ref_nasa_oig_ccp_2019], and the [CRS 2018 Commercial Crew Program report][ref_crs_commercial_crew_2018]. The primary source documentation for the Human Landing System Program includes the [NASA HLS Option A Award Announcement][ref_nasa_hls_optionA_2021], the [NASA HLS Sustaining Award Announcement][ref_nasa_hls_sustaining_2023], the [GAO 2022 Human Landing System evaluation][ref_gao_hls_2022], the [NASA Office of Inspector General 2021 Human Landing System evaluation][ref_nasa_oig_hls_2021], and the [GAO 2021 Blue Origin HLS protest decision][ref_gao_blue_origin_hls_protest_2021].

### Biographical and Case Study Literature

The biographical literature on the anchor-demand trajectory is dominated by the [Berger 2021][book_berger_2021] Liftoff, [Berger 2024][book_berger_2024] Reentry, [Vance 2015][book_vance_2015] Elon Musk, [Isaacson 2023][book_isaacson_2023] Elon Musk, [Davenport 2018][book_davenport_2018] The Space Barons, and [Fernholz 2018][book_fernholz_2018] Rocket Billionaires treatments. The specific December 2008 near-death moment and CRS-1 salvation are covered extensively in the [Berger 2021][book_berger_2021] narrative from the specific engineering-team perspective and in the [Vance 2015][book_vance_2015] and [Isaacson 2023][book_isaacson_2023] general biographies from the founder-centered perspective. The business-case-study literature includes the [Anadol Cohen Ferrari 2018][research_anadol_cohen_2018] SpaceX case study developed at INSEAD, various Harvard Business School cases, and the specific application of the [Bower and Christensen 1995][research_bower_christensen_1995] disruptive-innovation framework to the SpaceX case. The [Christensen 1997][book_christensen_1997] The Innovator's Dilemma framework has been applied to the specific NASA-Boeing-SpaceX Commercial Crew Program dynamics in multiple treatments.

### Procurement-Economics and Public-Administration Literature

The procurement-economics literature treats the specific COTS milestone-payment fixed-price mechanism as an instance of the general procurement-mechanism-design problem. The [Laffont and Tirole 1993][book_laffont_tirole_1993] theoretical treatment provides the specific incentive-compatibility framework within which the COTS mechanism admits characterization. The [McAfee and McMillan 1988][book_mcafee_mcmillan_1988] Incentives in Government Contracting treatment provides the specific applied-procurement-economics framework. Additional treatments include [Bajari and Tadelis 2001][research_bajari_tadelis_2001] Incentives Versus Transaction Costs A Theory of Procurement Contracts, [Bajari McMillan and Tadelis 2009][research_bajari_mcmillan_tadelis_2009] Auctions Versus Negotiations in Procurement An Empirical Analysis, [Che and Chung 1999][research_che_chung_1999] A Dynamic Model of Contract Renegotiation, and [Gagnepain and Ivaldi 2002][research_gagnepain_ivaldi_2002] Incentive Regulatory Policies The Case of Public Transit Systems in France. The public-administration literature treats the specific COTS procurement-mechanism innovation in journals including [Public Administration Review][ref_public_admin_review] and specialist procurement journals such as the [Journal of Public Procurement][ref_journal_public_procurement].

### Space Policy and Aerospace-Industrial Literature

The space-policy literature treats the specific Commercial Crew and Human Landing System programs in journals including [Space Policy][ref_space_policy_journal] and specialist space-policy publications. The [Hertzfeld 2002][research_hertzfeld_2002], [Peeters 2018][research_peeters_2018], and [Weinzierl 2018][research_weinzierl_2018] treatments provide the specific space-economics framework within which the anchor-demand trajectory admits characterization. The [Anderson 2023][book_anderson_2023] The Space Economy consolidates the sector-level treatment. The aerospace-industrial literature treats the specific competition between SpaceX and the incumbent providers including Boeing, Lockheed Martin, and Northrop Grumman in the specific procurement-competition context that the [Hunter 2016][book_hunter_2016] Creating Strategic Value treatment documents. Related historical aerospace treatments include [McDougall 1985][book_mcdougall_1985] The Heavens and the Earth, [Launius 1994][book_launius_1994] NASA A History of the United States Civil Space Program, [Logsdon 2010][book_logsdon_2010] John F Kennedy and the Race to the Moon, and [Handberg 1994][book_handberg_1994] Reinventing NASA. The specific space-adjacent policy analyses appear in [Space Policy Online][ref_space_policy_online], with additional coverage in [Payload Research][ref_payload_research].

### Contract-Design Empirical Literature

The specific contract-design empirical literature that treats the specific milestone-payment fixed-price mechanism the COTS Program adopted includes [Corts and Singh 2004][research_corts_singh_2004] The Effect of Relationships on the Nature of Contracts, [Kalnins and Mayer 2004][research_kalnins_mayer_2004] Relationships and Hybrid Contracts An Analysis of Contract Choice, and [Levin and Tadelis 2010][research_levin_tadelis_2010] Contracting for Government Services Theory and Evidence. The specific empirical treatments of the specific procurement-mechanism performance in aerospace and defense sectors include additional Government Accountability Office reports and Congressional Research Service reports the article draws on.

### Space Legal Literature

The specific space-legal literature that treats the specific regulatory and international-treaty framework within which the anchor-demand configuration operates includes the [Journal of Space Law][ref_journal_space_law], the [Space Legislation Review][ref_space_legislation_review], and the specific commentary on the [U S Commercial Space Launch Competitiveness Act of 2015][ref_uscsla_2015] that established the specific celestial-resource-rights framework relevant to the specific HLS mission architecture. The specific outer-space-treaty context appears in the [United Nations Outer Space Treaty of 1967][ref_un_outer_space_treaty_1967] and the specific [United Nations Liability Convention of 1972][ref_un_liability_convention_1972] and [United Nations Registration Convention of 1976][ref_un_registration_convention_1976] treaties that govern the specific launch-state-registration and international-liability framework.

### Comparative-Firm Literature

The comparative-firm literature on the anchor-demand trajectory treats the specific contrast between SpaceX and the adjacent-firm anchor-demand configurations. The Blue Origin anchor-demand trajectory has developed following the specific [Space Force NSSL Phase 3 Lane 2 award of October 2024][ref_spacenews] and the specific [NASA HLS Sustaining award of 2023][ref_nasa_hls_sustaining_2023], with the specific operational execution remaining at earlier maturity than the SpaceX trajectory. The Rocket Lab anchor-demand trajectory has developed through the specific United States national-security-launch customer set and the specific NASA acquisitions, with the specific Neutron program under development. The academic literature on the Chinese commercial-space entrant firms including LandSpace, iSpace, Galactic Energy, and CAS Space has developed primarily in Chinese-language scholarship with limited English-language translation, treating the specific state-adjacent anchor-demand configurations that differ substantially from the United States private-firm form. The academic literature on the European entrant firms including Isar Aerospace, Rocket Factory Augsburg, and Orbex has developed primarily in trade-press and industry-analyst coverage rather than in academic-journal treatment.

### Emerging Literature on Specific Topics

Several specific topics have generated distinct emerging scholarly literatures relevant to the SpaceX anchor-demand trajectory. The literature on the specific Commercial Crew Program certification and execution includes multiple GAO evaluations, NASA OIG evaluations, and Congressional Research Service reports covering the specific certification progression and the specific execution differential between the Boeing and SpaceX providers. The literature on the Human Landing System Program specifically includes the specific [GAO 2022 Human Landing System evaluation][ref_gao_hls_2022], the [NASA Office of Inspector General 2021 Human Landing System evaluation][ref_nasa_oig_hls_2021], and the specific [CRS 2022 Artemis Program report][ref_crs_artemis_2022] documenting the specific program-development trajectory. The literature on Starshield specifically includes the specific [Reuters 2024 Starshield investigation][research_reuters_starshield_2024] and subsequent [New York Times 2024 Starshield coverage][ref_nyt_starshield_2024] that reconstructed the specific classified-program structure from unclassified sources. The literature on the specific Golden Dome missile-defense architecture referenced in the specific 2025 policy discussion has generated additional emerging analytical work that the closing article A292 treats in the specific forward-projection context.

### Public Policy and Space-Governance Literature

The specific public-policy and space-governance literature that treats the specific NASA-SpaceX and Space Force-SpaceX institutional configurations includes the [Space Policy Online][ref_space_policy_online] policy-analysis coverage, the [Journal of Space Law][ref_journal_space_law] scholarly treatment, and the specific [Public Administration Review][ref_public_admin_review] treatment of the COTS procurement-mechanism innovation. The specific international-treaty context that governs the specific launch-state-registration and international-liability framework appears in the specific [United Nations Outer Space Treaty of 1967][ref_un_outer_space_treaty_1967], the specific [United Nations Liability Convention of 1972][ref_un_liability_convention_1972], and the specific [United Nations Registration Convention of 1976][ref_un_registration_convention_1976].

### Trade Press and Journalistic Record

The trade-press coverage of the anchor-demand trajectory appears extensively in [SpaceNews][ref_spacenews], [Ars Technica Space Coverage][ref_arstechnica_space], [NASASpaceflight][ref_nasaspaceflight], [Payload][ref_payload], [Payload Research][ref_payload_research], and [European Spaceflight][ref_european_spaceflight]. The specific national-security-adjacent coverage including the Starshield program appears in specialist defense-and-intelligence trade press including [Breaking Defense][ref_breaking_defense], [Aviation Week][ref_aviation_week], and [Defense News][ref_defense_news]. The mainstream business-press coverage in [Bloomberg][ref_bloomberg], the [New York Times][ref_nyt], the [Washington Post][ref_washington_post], and the [Wall Street Journal][ref_wsj] provides the specific business-context reporting. The specific space-policy analysis coverage appears in [Space Policy Online][ref_space_policy_online] and [The Space Review][ref_the_space_review].

## Contemporary Comparative Landscape

The contemporary comparative landscape for the anchor-demand condition across the space-launch-sector firms as of the drafting date reflects the specific pattern the SpaceX case established as the sector benchmark.

Boeing has the specific Commercial Crew Program anchor-demand contract but has faced substantial development delay and cost overrun with the Starliner spacecraft, and the specific ongoing crew-transportation service execution remains dominated by SpaceX. The Commercial Crew operational-mission share admits the compact form

$$s^{\text{crew-missions}}_i = \frac{n^{\text{operational-missions}}_i}{\sum_j n^{\text{operational-missions}}_j}$$

with the specific SpaceX share substantially above the specific Boeing share as of the drafting date. The specific Boeing Starliner Crewed Flight Test in June 2024 experienced the specific thruster-and-helium-leak issues that required uncrewed vehicle return, extending the specific Boeing service-commencement delay by additional years.

Blue Origin has secured specific anchor-demand awards including the [Space Force NSSL Phase 3 Lane 2 award of October 2024][ref_spacenews] and the [NASA HLS Sustaining award of 2023][ref_nasa_hls_sustaining_2023] but has not achieved comparable operational-execution cadence to SpaceX. The specific comparative anchor-share ratio admits the compact form

$$\rho^{\text{anchor-share}}_{\text{Blue Origin vs SpaceX}} = \frac{\sigma^{\text{anchor}}_{\text{Blue Origin}}}{\sigma^{\text{anchor}}_{\text{SpaceX}}}$$

with the specific Blue Origin anchor share exceeding the SpaceX anchor share since Blue Origin operates primarily on state-anchor demand without a mature commercial-spinoff revenue channel comparable to Starlink. The specific New Glenn first flight occurred in January 2025 and the specific operational-cadence achievement remains at earlier maturity.

Northrop Grumman operates the Antares medium-lift vehicle for NASA Cargo Resupply Services missions and the Minotaur small-lift vehicle for defense missions, though the specific Antares configuration has faced Russian RD-181 engine supply-chain disruption following the 2022 Russian invasion of Ukraine.

Sierra Nevada Corporation operates the Dream Chaser lifting-body configuration for NASA CRS-2 missions with the specific first Dream Chaser flight expected in the near-term period.

The United Launch Alliance operates the Vulcan Centaur launch vehicle as the specific second Space Force NSSL Phase 3 Lane 2 provider alongside SpaceX and Blue Origin.

## Comparative Cross-Sectional Analysis

The anchor-demand condition admits application to the launch-sector firms as a cross-sectional scoring exercise. The exercise identifies the specific anchor-demand closure or negation status across the sector-level competitor set.

Blue Origin exhibits partial anchor-demand closure through the specific Space Force NSSL Phase 3 Lane 2 award and the specific NASA HLS Sustaining award, but the specific anchor-demand-to-total-revenue ratio remains lower than the SpaceX ratio through the specific pre-operational stage of the New Glenn vehicle. The comparative sub-property closure vector across the adjacent-firm set admits the compact form

$$\boldsymbol{\phi}_j^{\text{anchor-demand}} \in \{0, 1\}^{5}$$

with each firm's closure vector indicating the specific satisfaction status across the five anchor-demand sub-properties. Rocket Lab exhibits partial anchor-demand closure through the specific United States national-security-launch customer set and the specific NASA acquisitions. ULA exhibits substantial anchor-demand closure through the specific Space Force NSSL revenue but operates under the specific incumbent expendable-vehicle cost structure that does not close the value-gradient sub-property the [Value Gradient article A282][related_post_a282_spacex_value_gradient] treats. The international launch-provider set exhibits distinct national-anchor-demand configurations that reflect the specific state-firm coordination structure the developmental-state tradition documents.

## Data Sources and Reconstruction Methodology

The article draws on primary and secondary sources to reconstruct the anchor-demand trajectory. The primary-source layer includes NASA program documents accessible through the [NASA Technical Reports Server][ref_nasa_ntrs] and the [NASA history archives][ref_nasa_history], NASA press releases accessible through the [NASA news][ref_nasa_news], GAO reports accessible through the [GAO reports database][ref_gao_reports], NASA OIG reports accessible through the [NASA OIG database][ref_nasa_oig_reports], CRS reports accessible through the [CRS reports database][ref_crs_reports], Congressional testimony accessible through the [Congressional record][ref_congressional_record], DOD contract announcements accessible through the [DOD contracts announcements][ref_dod_contracts], Space Force announcements accessible through the [Space Force news][ref_space_force_news], and SpaceX corporate press releases accessible through the [SpaceX news archive][ref_spacex_news_archive].

The secondary-source layer includes the trade-press coverage identified in the Historiographical Gap section, the biographical literature dominated by [Berger 2021][book_berger_2021] Liftoff, [Berger 2024][book_berger_2024] Reentry, [Vance 2015][book_vance_2015] Elon Musk, [Isaacson 2023][book_isaacson_2023] Elon Musk, [Davenport 2018][book_davenport_2018] The Space Barons, and [Fernholz 2018][book_fernholz_2018] Rocket Billionaires, and the case-study literature described in the Historiographical Gap section.

The empirical-record limitations include the SpaceX private-firm status that precludes access to Securities and Exchange Commission filings, the classification restrictions on the specific national-security portions of the anchor-demand portfolio, the confidentiality restrictions on the specific contract-award terms in some NASA and Space Force procurements, and the private-firm restrictions on the specific Starshield revenue and mission composition. The article treats these limitations explicitly.

## Alternative Analytical Frameworks

The anchor-demand framing the article develops is one of several analytical frameworks the surrounding literature applies to the SpaceX-NASA and SpaceX-Space Force relationships.

The state-capitalism framing developed in the state-firm coordination scholarship frames SpaceX as an instance of United States state capitalism operating through specific procurement-mechanism configurations rather than through direct state ownership. The state-capitalism index admits the compact form

$$\text{SC}_i = w^{\text{gov-rev}} \cdot \frac{R^{\text{gov}}_i}{R^{\text{total}}_i} + w^{\text{ownership}} \cdot s^{\text{state-ownership}}_i + w^{\text{strategic}} \cdot I^{\text{strategic-sector}}_i$$

with the three weighted components indexing government-revenue share, state-ownership share, and strategic-sector-designation indicator. The framing captures the specific substantial government-anchor share of revenue but understates the specific dual-class founder-control governance structure.

The defense-industrial-base framing developed in [Hunter 2016][book_hunter_2016] and [Weiss 2014][book_weiss_2014] frames SpaceX as an entrant into the United States defense-industrial base whose specific comparative advantage lies in the fixed-price procurement mechanism. The framing formalizes the defense-industrial-base spending share the specific firm captures through the compact form

$$s^{\text{DIB}}_i = \frac{R^{\text{defense}}_i}{R^{\text{DIB-total}}}$$

with $R^{\text{DIB-total}}$ the aggregate defense-industrial-base contract awards across all providers. The framing captures the specific Space Force NSSL certification progression and the specific Starshield defense-service line.

The public-private-partnership framing developed in [Grimsey and Lewis 2004][book_grimsey_lewis_2004] Public Private Partnerships and [Hodge and Greve 2007][research_hodge_greve_2007] frames the COTS Program and Commercial Crew Program as instances of the general public-private-partnership pattern. The framing captures the specific shared-risk shared-reward structure but understates the specific mission-articulation the mission-oriented-innovation framing emphasizes.

The mission-oriented-innovation framing developed in [Mazzucato 2013][book_mazzucato_2013] and [Mazzucato 2021][book_mazzucato_2021] and adopted as primary by the series treats the specific NASA mission-articulation as the primary organizing force. The framing captures the specific coherence of the anchor-demand trajectory and admits the specification the article develops.

The rent-seeking framing developed in [Buchanan and Tullock 1962][book_buchanan_tullock_1962], [Stigler 1971][research_stigler_1971], and [Krueger 1974][research_krueger_1974] frames the anchor-demand structure as an instance of the specific rent-extraction pattern in which private firms benefit from state-created contracting opportunities. The specific rent-transfer identity admits the compact form

$$\text{Rent}_i = \pi_i^{\text{observed}} - \pi_i^{\text{competitive-benchmark}}$$

with the specific rent equal to the difference between the observed provider profit and the counterfactual competitive-benchmark profit that arm's-length market arrangements would produce. The framing captures the specific concern that the milestone-payment procurement mechanism concentrates the resulting surplus in the incumbent provider set.

The military-Keynesianism framing developed in [Melman 1970][book_melman_1970] Pentagon Capitalism frames the anchor-demand structure as an instance of the specific defense-spending macroeconomic pattern. The specific military-Keynesian multiplier admits the compact form

$$\mu^{\text{military-Keynesian}} = \frac{\Delta Y^{\text{aggregate}}}{\Delta G^{\text{defense-spending}}}$$

with $\mu^{\text{military-Keynesian}}$ typically empirically estimated at approximately 0.5 to 1.5 across the defense-spending literature. The framing captures the specific Space Force NSSL and Starshield contributions but understates the specific NASA civilian-science anchor-demand components.

The real-options and staged-investment framing developed in [Dixit and Pindyck 1994][book_dixit_pindyck_1994] Investment Under Uncertainty and [Trigeorgis 1996][book_trigeorgis_1996] Real Options frames the anchor-demand configuration as a sequential set of real options across the specific NASA COTS, Commercial Crew, HLS, and Space Force NSSL programs. The framing captures the specific staged-investment structure where each subsequent anchor-program award represents an option-exercise decision by the anchor customer against the specific provider's demonstrated capability accumulation. The sequential-option value admits the backward-induction recursion

$$V^{\text{anchor-option}}_t = \max\!\left\{V^{\text{exercise}}_t, \, e^{-r \Delta t} \cdot E\!\left[V^{\text{anchor-option}}_{t+1} \mid F_t\right]\right\}$$

with the anchor customer choosing at each stage between exercising the option through award and deferring for additional information accumulation. The framing complements the milestone-payment framing by treating the specific award-timing decisions as first-order objects of analysis.

The actor-network-theory framing developed in [Latour 1987][book_latour_1987] Science in Action, [Callon 1986][research_callon_1986] Some Elements of a Sociology of Translation, and [Law 1987][research_law_1987] Technology and Heterogeneous Engineering frames the anchor-demand configuration as a heterogeneous network of human and non-human actors whose alignment constitutes the specific contract-execution outcomes. The framing treats the specific translation moves through which the SpaceX firm assembles the network across engineers, launch-vehicle components, regulatory reviewers, NASA program office personnel, Congressional appropriators, and specific contract-management infrastructure across each successive anchor-program cycle as first-order objects of analysis. The framing complements the mission-oriented-innovation framing by treating the specific mission-articulation itself as an object of network-building.

The resource-based-view and dynamic-capabilities framing developed in [Wernerfelt 1984][research_wernerfelt_1984] A Resource-Based View of the Firm and [Barney 1991][research_barney_1991] Firm Resources and Sustained Competitive Advantage, extended in [Teece Pisano Shuen 1997][research_teece_pisano_shuen_1997] Dynamic Capabilities and Strategic Management, frames the SpaceX anchor-demand trajectory as an instance of specific firm-capability accumulation that produced the sustained competitive advantage across the specific anchor-program competitions. The specific resource-heterogeneity index admits the compact form

$$H_i = \sum_{r \in \text{resources}} \omega_r \cdot (V_r \cdot R_r \cdot I_r \cdot N_r)$$

with $\omega_r$ the resource weight and the four V-R-I-N factors indicating value, rarity, inimitability, and non-substitutability. The framing captures the specific role of the SpaceX in-house engineering capability and vertical-integration configuration that supported the sustained anchor-demand competitiveness.

The complexity and evolutionary-economics framing developed in [Nelson and Winter 1982][book_nelson_winter_1982] An Evolutionary Theory of Economic Change and [Metcalfe 1998][book_metcalfe_1998] Evolutionary Economics and Creative Destruction frames the anchor-demand configuration as a specific realization of the sector-level evolutionary dynamics that select among specific provider-firm-anchor-customer configurations under the specific competitive pressure. The framing captures the specific competitive-selection dynamics between the SpaceX iterative approach and the incumbent Boeing-Lockheed cost-plus approach, and admits the interpretation that the specific SpaceX success reflects the specific selection under the specific fixed-price milestone-payment procurement environment.

The ecosystem-strategy framing developed in [Adner 2012][book_adner_2012] The Wide Lens frames the specific SpaceX-NASA anchor-demand configuration as an instance of the specific ecosystem-strategy pattern in which the specific ISS-operator-plus-cargo-provider-plus-crew-provider ecosystem coordinates specific anchor-demand execution across the specific mission-critical timeline. The framing captures the specific ecosystem-coordination challenges that arise when multiple ecosystem actors must execute in synchronized fashion for the anchor-demand realization.

## Pattern Extraction

The anchor-demand mechanic that the SpaceX trajectory illustrates admits abstract characterization in a form other informed readers can recognize in adjacent domains. The pattern-extraction section states the abstract mechanic without naming any specific downstream application.

The abstract anchor-demand mechanic is the property of a mission-directed technology development trajectory that operates against a specific identifiable customer whose demand commitment is articulated and enforceable rather than against a speculative future market whose emergence is contingent on the venture's success. The property has several load-bearing sub-properties that jointly enable the observed pattern.

First, the anchor customer must exist as a specific identifiable institutional actor with specific procurement authority and specific demand articulation, distinguishing anchor demand from speculative-market emergence. Second, the anchor-provider contract must adopt a specific incentive-compatible payment structure that rewards demonstrated performance rather than cost incurrence, distinguishing anchor demand from open-ended cost-plus arrangements. Third, the anchor-demand flow must sustain across the multi-year horizon that the mission-directed development requires, distinguishing anchor demand from single-award transactions. Fourth, the anchor-demand configuration must include specific technical-standard-setting through which the anchor's requirements transfer to commercial customers as an anchor-financed public good. Fifth, the anchor-demand portfolio must diversify across multiple anchor customers to reduce single-anchor concentration risk.

The five sub-properties jointly enable the anchor-demand property. The specific SpaceX trajectory closes all five sub-properties across the observed history through the specific NASA COTS-CRS-Commercial Crew-HLS anchor ladder plus the specific Space Force NSSL and Starshield diversification. The specific counter-example cases negate one or more sub-properties.

The joint-satisfaction condition admits the compact form

$$\text{AD closure} = \bigwedge_{k=1}^{5} \phi_k$$

with $\phi_k$ the closure indicator for sub-property $k$ and the conjunction requiring all five sub-properties to be closed. The closure vector for a candidate case $j$ is

$$\boldsymbol{\phi}_j = (\phi_{j,1}, \phi_{j,2}, \phi_{j,3}, \phi_{j,4}, \phi_{j,5}) \in \{0, 1\}^5$$

with the candidate's anchor-demand closure occurring when $\boldsymbol{\phi}_j = \mathbf{1}$. Under order-of-magnitude estimates $p_k \approx 0.25$ across the five sub-properties and independence, the joint-closure probability is approximately

$$P^{\text{AD closure}}_{\text{indep}} = \prod_{k=1}^{5} p_k \approx 0.001$$

which suggests the specific closure singularity the article identifies in the SpaceX case. Under positive-correlation adjustment, the joint probability rises but remains substantially below the observed single-case rate.

## Cross-References to the Series

The article specifically cross-references the [series opener A281][related_post_a281_spacex_framing] and the [Value Gradient article A282][related_post_a282_spacex_value_gradient]. Subsequent articles A284 through A292 will treat the other forcing-function conditions and capital-formation legs.

## Terminological Note

Anchor customer refers to a specific institutional actor with specific procurement authority whose demand commitment is articulated and enforceable across the venture's development horizon.

Anchor demand refers to the specific revenue flow from anchor customers.

Anchor share refers to the specific fraction of the venture's total revenue that derives from anchor customers.

Anchor ladder refers to the specific sequence of anchor-program awards across the venture's trajectory.

## Load-Bearing Open Questions

Several open questions remain load-bearing for the article's specific claims.

The specific dollar-value quantification of the specific anchor-demand contributions across the SpaceX trajectory depends on the specific per-mission price and per-mission cadence data that the private-firm status limits.

The specific counterfactual anchor-demand trajectory absent the specific COTS Program admits partial characterization through the specific [Rocketplane Kistler termination of October 2007][ref_nasa_rocketplane_kistler_termination_2007] and the specific [Orbital Sciences COTS Round 2 award of February 2008][ref_nasa_crs1_press_2008] comparative cases but does not admit sharp identification.

The specific Starshield revenue and mission composition remains substantially classified as of the drafting date and admits only partial reconstruction through the trade-press coverage.

The specific competitive-response timeline under which the alternative launch providers will match the SpaceX anchor-demand configuration is treated in the closing article A292.

## References

### Books

- [Adner 2012 The Wide Lens][book_adner_2012]
- [Amsden 1989 Asia's Next Giant][book_amsden_1989]
- [Anderson 2023 The Space Economy][book_anderson_2023]
- [Andrewes 1996 The Quest for Longitude][book_andrewes_1996]
- [Berger 2021 Liftoff][book_berger_2021]
- [Berger 2024 Reentry][book_berger_2024]
- [Bilstein 1996 Stages to Saturn][book_bilstein_1996]
- [Bilstein 2001 Flight in America][book_bilstein_2001]
- [Bird and Sherwin 2005 American Prometheus][book_bird_sherwin_2005]
- [Buchanan and Tullock 1962 The Calculus of Consent][book_buchanan_tullock_1962]
- [Chadeau 1996 Airbus Industrie History][book_chadeau_1996]
- [Chaikin 2007 A Man on the Moon][book_chaikin_2007]
- [Chang 2002 Kicking Away the Ladder][book_chang_2002]
- [Christensen 1997 The Innovator's Dilemma][book_christensen_1997]
- [Collins 2010 The Language of Life][book_collins_2010]
- [Concina 2006 A History of Venetian Architecture][book_concina_2006]
- [Crouch 2003 Wings A History of Aviation from Kites to the Space Age][book_crouch_2003]
- [Davenport 2018 The Space Barons][book_davenport_2018]
- [Dixit and Pindyck 1994 Investment Under Uncertainty][book_dixit_pindyck_1994]
- [Evans 1995 Embedded Autonomy][book_evans_1995]
- [Fallows 1981 National Defense][book_fallows_1981]
- [Fernholz 2018 Rocket Billionaires][book_fernholz_2018]
- [Fligstein 2001 The Architecture of Markets][book_fligstein_2001]
- [Gertner 2012 The Idea Factory][book_gertner_2012]
- [Grimsey and Lewis 2004 Public Private Partnerships][book_grimsey_lewis_2004]
- [Groves 1962 Now It Can Be Told][book_groves_1962]
- [Handberg 1994 Reinventing NASA][book_handberg_1994]
- [Hewlett and Anderson 1962 The New World][book_hewlett_anderson_1962]
- [Ho 2009 Liquidated][book_ho_2009]
- [Hosley 1996 Colt The Making of an American Legend][book_hosley_1996]
- [Hounshell 1984 From the American System to Mass Production 1800-1932][book_hounshell_1984]
- [Hunter 2016 Creating Strategic Value][book_hunter_2016]
- [Iansiti and Levien 2004 The Keystone Advantage][book_iansiti_levien_2004]
- [Isaacson 2023 Elon Musk][book_isaacson_2023]
- [Johnson 1982 MITI and the Japanese Miracle][book_johnson_1982]
- [Kaplan 1991 The Wizards of Armageddon][book_kaplan_1991]
- [Krige et al 2000 A History of the European Space Agency][book_krige_et_al_2000]
- [Krippner 2011 Capitalizing on Crisis][book_krippner_2011]
- [Laffont and Tirole 1993 A Theory of Incentives in Procurement and Regulation][book_laffont_tirole_1993]
- [Lane 1934 Venetian Ships and Shipbuilders of the Renaissance][book_lane_1934]
- [Latour 1987 Science in Action][book_latour_1987]
- [Launius 1994 NASA A History of the United States Civil Space Program][book_launius_1994]
- [Liker 2004 The Toyota Way][book_liker_2004]
- [Logsdon 2010 John F Kennedy and the Race to the Moon][book_logsdon_2010]
- [MacKenzie 2006 An Engine Not a Camera][book_mackenzie_2006]
- [Mazzucato 2013 The Entrepreneurial State][book_mazzucato_2013]
- [Mazzucato 2021 Mission Economy][book_mazzucato_2021]
- [McAfee and McMillan 1988 Incentives in Government Contracting][book_mcafee_mcmillan_1988]
- [McCullough 1977 The Path Between the Seas][book_mccullough_1977]
- [McDougall 1985 The Heavens and the Earth][book_mcdougall_1985]
- [McIntyre 1992 Airbus Industrie][book_mcintyre_1992]
- [Melman 1970 Pentagon Capitalism][book_melman_1970]
- [Metcalfe 1998 Evolutionary Economics and Creative Destruction][book_metcalfe_1998]
- [Milgrom 2004 Putting Auction Theory to Work][book_milgrom_2004]
- [Miller 1995 Lockheed Skunk Works The First Fifty Years][book_miller_1995]
- [Mindell 2008 Digital Apollo][book_mindell_2008]
- [Murray and Cox 1989 Apollo][book_murray_cox_1989]
- [Musa 1998 Software Reliability Engineering][book_musa_1998]
- [Muthoo 1999 Bargaining Theory with Applications][book_muthoo_1999]
- [Nelson and Winter 1982 An Evolutionary Theory of Economic Change][book_nelson_winter_1982]
- [Neufeld 1995 The Rocket and the Reich][book_neufeld_1995]
- [Neufeld 2013 Von Braun][book_neufeld_2013]
- [Newhouse 1982 The Sporty Game][book_newhouse_1982]
- [O'Connor and Kleyner 2012 Practical Reliability Engineering][book_oconnor_kleyner_2012]
- [Osborne 2000 Public-Private Partnerships][book_osborne_2000]
- [Osborne and Rubinstein 1990 Bargaining and Markets][book_osborne_rubinstein_1990]
- [Preda 2009 Framing Finance][book_preda_2009]
- [Rhodes 1986 The Making of the Atomic Bomb][book_rhodes_1986]
- [Rich and Janos 1994 Skunk Works][book_rich_janos_1994]
- [Ruttan 2006 Is War Necessary for Economic Growth][book_ruttan_2006]
- [Serling 1992 Legend and Legacy][book_serling_1992]
- [Sobel 1995 Longitude][book_sobel_1995]
- [Tirole 1988 The Theory of Industrial Organization][book_tirole_1988]
- [Trigeorgis 1996 Real Options][book_trigeorgis_1996]
- [Vance 2015 Elon Musk][book_vance_2015]
- [Wade 1990 Governing the Market][book_wade_1990]
- [Weiss 2014 America Inc][book_weiss_2014]
- [Williamson 1985 The Economic Institutions of Capitalism][book_williamson_1985]
- [Womack Jones Roos 1990 The Machine That Changed the World][book_womack_jones_roos_1990]
- [Woo-Cumings 1999 The Developmental State][book_woo_cumings_1999]
- [Yescombe 2007 Public-Private Partnerships Principles of Policy and Finance][book_yescombe_2007]
- [Zaloom 2006 Out of the Pits][book_zaloom_2006]

### Reference

- [14 CFR Chapter III FAA Commercial Space Regulations][ref_faa_ast_regulations]
- [14 CFR Part 450 Launch and Reentry Licensing][ref_faa_ast_licensing_regs_450]
- [22 CFR 120 through 130 International Traffic in Arms Regulations][ref_itar_22_cfr_120_130]
- [51 U.S.C. 51302 NASA Space Act Agreement Authority][ref_51_usc_51302_saa]
- [Ars Technica Space Coverage][ref_arstechnica_space]
- [Aviation Week Coverage][ref_aviation_week]
- [Bloomberg Business News][ref_bloomberg]
- [Boeing Starliner CFT June 2024][ref_boeing_starliner_cft_2024]
- [Breaking Defense Coverage][ref_breaking_defense]
- [Congressional Record][ref_congressional_record]
- [CRS 2018 Commercial Crew Program][ref_crs_commercial_crew_2018]
- [CRS 2022 Artemis Program][ref_crs_artemis_2022]
- [CRS Reports Database][ref_crs_reports]
- [Defense News Coverage][ref_defense_news]
- [DOD Contract Announcements][ref_dod_contracts]
- [European Spaceflight Coverage][ref_european_spaceflight]
- [FAA AST Current Launch Licenses Database][ref_faa_launch_licenses_current]
- [FAR Part 15 Contracting by Negotiation][ref_far_part_15]
- [FCC Direct-to-Cell Authorization 2024][ref_fcc_direct_to_cell_2024]
- [FCC Filings Database][ref_fcc_filings]
- [FCC Starlink Authorization March 2018][ref_fcc_starlink_2018]
- [FCC Starlink Generation 2 Authorization December 2022][ref_fcc_starlink_gen2_2022]
- [GAO 2009 COTS Program][ref_gao_cots_2009]
- [GAO 2011 Commercial Cargo Program][ref_gao_cots_2011]
- [GAO 2019 Commercial Crew Program][ref_gao_ccp_2019]
- [GAO 2021 Blue Origin HLS Protest][ref_gao_blue_origin_hls_protest_2021]
- [GAO 2022 Human Landing System][ref_gao_hls_2022]
- [GAO Reports Database][ref_gao_reports]
- [INCOSE Systems Engineering Handbook][ref_incose_handbook]
- [ITU Radio Regulations 2020][ref_itu_radio_regulations_2020]
- [Journal of Public Procurement][ref_journal_public_procurement]
- [Journal of Space Law][ref_journal_space_law]
- [NASA CCtCap Award Announcement 2014][ref_nasa_cctcap_press_2014]
- [NASA Commercial Crew Program 2014][ref_nasa_ccp_2014]
- [NASA COTS 2011 Program History][ref_nasa_cots_2011]
- [NASA COTS Report][ref_nasa_cots_report]
- [NASA COTS Round 2 Award to Orbital Sciences 2008][ref_nasa_crs1_press_2008]
- [NASA COTS Solicitation Announcement 2006][ref_nasa_cots_solicitation_2006]
- [NASA CRS-2 Award Announcement 2016][ref_nasa_crs2_press_2016]
- [NASA FAR Supplement][ref_nasa_far_supplement]
- [NASA History Archives][ref_nasa_history]
- [NASA HLS Option A Award Announcement 2021][ref_nasa_hls_optionA_2021]
- [NASA HLS Option B Award Announcement 2022][ref_nasa_hls_optionB_2022]
- [NASA HLS Sustaining Award Announcement 2023][ref_nasa_hls_sustaining_2023]
- [NASA News][ref_nasa_news]
- [NASA OIG 2013 COTS Program][ref_nasa_oig_cots_2013]
- [NASA OIG 2018 Commercial Cargo Program][ref_nasa_oig_ccp_cargo_2018]
- [NASA OIG 2019 Commercial Crew Program][ref_nasa_oig_ccp_2019]
- [NASA OIG 2021 Human Landing System][ref_nasa_oig_hls_2021]
- [NASA OIG Reports Database][ref_nasa_oig_reports]
- [NASA Orbital Debris Mitigation Standard Practices][ref_nasa_orbital_debris_mitigation]
- [NASA Rocketplane Kistler Termination 2007][ref_nasa_rocketplane_kistler_termination_2007]
- [NASA Standard 8709.22 Safety and Mission Assurance][ref_nasa_std_8709_22]
- [NASA Technical Reports Server][ref_nasa_ntrs]
- [NASASpaceflight Coverage][ref_nasaspaceflight]
- [New York Times][ref_nyt]
- [New York Times Starshield Coverage 2024][ref_nyt_starshield_2024]
- [Payload Newsletter][ref_payload]
- [Payload Research][ref_payload_research]
- [Public Administration Review][ref_public_admin_review]
- [Space Force News][ref_space_force_news]
- [Space Force NSSL Phase 1A Award 2018][ref_space_force_nssl_phase1a_2018]
- [Space Force NSSL Phase 2 Award 2020][ref_space_force_nssl_phase2_2020]
- [Space Force NSSL Phase 3 Lane 2 Award 2024][ref_spacenews]
- [Space Legislation Review][ref_space_legislation_review]
- [Space Policy Journal][ref_space_policy_journal]
- [Space Policy Online][ref_space_policy_online]
- [SpaceX Falcon 9 User's Guide][ref_spacex_falcon9_users_guide]
- [SpaceX News Archive][ref_spacex_news_archive]
- [SpaceX Press Release Crew-1 November 2020][ref_spacex_press_crew1_2020]
- [SpaceX Press Release CRS-1 October 2012][ref_spacex_press_crs1_2012]
- [SpaceX Press Release CRS-21 December 2020][ref_spacex_press_crs21_2020]
- [SpaceX Press Release CRS-7 Loss June 2015][ref_spacex_press_crs7_2015]
- [SpaceX Press Release Demo-1 March 2019][ref_spacex_press_demo1_2019]
- [SpaceX Press Release Demo-2 May 2020][ref_spacex_press_dm2_2020]
- [SpaceX Press Release Dragon C1 December 2010][ref_spacex_press_dragon_c1_2010]
- [SpaceX Press Release Falcon 1 Flight 4 Success 2008][ref_spacex_press_falcon1_flight4_2008]
- [SpaceX Starlink Direct-to-Cell T-Mobile Partnership August 2022][ref_spacex_starlink_direct_to_cell_tmobile_2022]
- [SpaceX Starshield Product Page][ref_spacex_starshield]
- [SpaceX Starship Program Page][ref_spacex_starship_program]
- [The Space Review][ref_the_space_review]
- [U S Commercial Space Launch Competitiveness Act 2015][ref_uscsla_2015]
- [United Nations Liability Convention 1972][ref_un_liability_convention_1972]
- [United Nations Outer Space Treaty 1967][ref_un_outer_space_treaty_1967]
- [United Nations Registration Convention 1976][ref_un_registration_convention_1976]
- [Wall Street Journal][ref_wsj]
- [Washington Post][ref_washington_post]

### Research

- [Adner 2017 Ecosystem as Structure An Actionable Construct for Strategy][research_adner_2017]
- [Anadol Cohen Ferrari 2018 SpaceX Case Study][research_anadol_cohen_2018]
- [Bajari and Tadelis 2001 Incentives Versus Transaction Costs A Theory of Procurement Contracts][research_bajari_tadelis_2001]
- [Bajari McMillan and Tadelis 2009 Auctions Versus Negotiations in Procurement An Empirical Analysis][research_bajari_mcmillan_tadelis_2009]
- [Barney 1991 Firm Resources and Sustained Competitive Advantage][research_barney_1991]
- [Binmore Rubinstein and Wolinsky 1986 The Nash Bargaining Solution in Economic Modelling][research_binmore_rubinstein_wolinsky_1986]
- [Block 2008 Swimming Against the Current The Rise of a Hidden Developmental State][research_block_2008]
- [Bonvillian 2018 DARPA and the Advanced Research Projects Agency][research_bonvillian_2018]
- [Bovaird 2004 Public-Private Partnerships From Contested Concepts to Prevalent Practice][research_bovaird_2004]
- [Bower and Christensen 1995 Disruptive Technologies Catching the Wave][research_bower_christensen_1995]
- [Callon 1986 Some Elements of a Sociology of Translation][research_callon_1986]
- [Che and Chung 1999 A Dynamic Model of Contract Renegotiation][research_che_chung_1999]
- [Coase 1937 The Nature of the Firm][research_coase_1937]
- [Cohen and Levinthal 1990 Absorptive Capacity A New Perspective on Learning and Innovation][research_cohen_levinthal_1990]
- [Corts and Singh 2004 The Effect of Relationships on the Nature of Contracts][research_corts_singh_2004]
- [Duane 1964 Learning Curve Approach to Reliability Monitoring][research_duane_1964]
- [Fuchs 2010 Rethinking the Role of the State in Technology Development][research_fuchs_2010]
- [Gagnepain and Ivaldi 2002 Incentive Regulatory Policies][research_gagnepain_ivaldi_2002]
- [Grossman and Hart 1986 The Costs and Benefits of Ownership][research_grossman_hart_1986]
- [Hart 1988 Incomplete Contracts and the Theory of the Firm][research_hart_1988]
- [Hertzfeld 2002 Measuring the Economic Returns from Successful NASA Life Sciences Technology Transfer][research_hertzfeld_2002]
- [Hodge and Greve 2007 Public-Private Partnerships An International Performance Review][research_hodge_greve_2007]
- [Jacobides Cennamo and Gawer 2018 Towards a Theory of Ecosystems][research_jacobides_et_al_2018]
- [Kalnins and Mayer 2004 Relationships and Hybrid Contracts An Analysis of Contract Choice][research_kalnins_mayer_2004]
- [Kelly 2013 Contract Auctions in Space Launch][research_kelly_2013]
- [Klein Crawford and Alchian 1978 Vertical Integration Appropriable Rents and the Competitive Contracting Process][research_klein_crawford_alchian_1978]
- [Krueger 1974 The Political Economy of the Rent-Seeking Society][research_krueger_1974]
- [Lane Koka Pathak 2006 The Reification of Absorptive Capacity][research_lane_koka_pathak_2006]
- [Law 1987 Technology and Heterogeneous Engineering][research_law_1987]
- [Levin and Tadelis 2010 Contracting for Government Services Theory and Evidence][research_levin_tadelis_2010]
- [Maier 1998 Architecting Principles for Systems-of-Systems][research_maier_1998]
- [Myerson 1981 Optimal Auction Design][research_myerson_1981]
- [Nash 1950 The Bargaining Problem][research_nash_1950]
- [Nelson 1959 The Simple Economics of Basic Scientific Research][research_nelson_1959]
- [Nelson 1977 The Moon and the Ghetto][research_nelson_1977]
- [Peeters 2018 Space Commercialization Trends][research_peeters_2018]
- [Reuters 2024 Starshield Investigation][research_reuters_starshield_2024]
- [Rubinstein 1982 Perfect Equilibrium in a Bargaining Model][research_rubinstein_1982]
- [Sage and Cuppan 2001 On the Systems Engineering and Management of Systems of Systems][research_sage_cuppan_2001]
- [Stigler 1971 The Theory of Economic Regulation][research_stigler_1971]
- [Teece Pisano Shuen 1997 Dynamic Capabilities and Strategic Management][research_teece_pisano_shuen_1997]
- [Todorova and Durisin 2007 Absorptive Capacity Valuing a Reconceptualization][research_todorova_durisin_2007]
-
- [Weinzierl 2018 Space the Final Economic Frontier][research_weinzierl_2018]
- [Weiss and Thurbon 2021 Developmental State or Economic Statecraft][research_weiss_thurbon_2021]
- [Wernerfelt 1984 A Resource-Based View of the Firm][research_wernerfelt_1984]
- [Williamson 1975 Markets and Hierarchies][research_williamson_1975]
- [Williamson 2002 The Theory of the Firm as Governance Structure][research_williamson_2002]
- [Zahra and George 2002 Absorptive Capacity A Review Reconceptualization and Extension][research_zahra_george_2002]

### Related Post

- [A90 Introduction to Space Studies][related_post_a90_intro_space_studies]
- [A96 History of Rocketplanes][related_post_a96_history_rocketplanes]
- [A132 Introduction to SBIR and STTR][related_post_a132_sbir_intro]
- [A138 SBIR Phase III and the Valley of Death][related_post_a138_sbir_phase3]
- [A237 Framing and the Co-Development Mechanism][related_post_a237_aerospace_framing]
- [A242 Apollo Guidance Computer][related_post_a242_apollo_guidance]
- [A246 Silicon Valley from Defense Contracting][related_post_a246_silicon_valley_defense]
- [A247 Software-Defined Aerospace and Autonomy][related_post_a247_software_defined_aerospace]
- [A248 Contemporary Snapshot and Extrapolation][related_post_a248_contemporary_snapshot]
- [A281 History of SpaceX Series Framing and the Seven-Plus-Three Forcing-Function Framework][related_post_a281_spacex_framing]
- [A282 History of SpaceX Value Gradient from Falcon 1 to Falcon 9 to Reusability][related_post_a282_spacex_value_gradient]

[book_amsden_1989]: https://global.oup.com/academic/product/asias-next-giant-9780195076035
[book_anderson_2023]: https://www.wiley.com/en-us/The+Space+Economy-p-9781119911562
[book_berger_2021]: https://williammorrow.com/liftoff-eric-berger/
[book_berger_2024]: https://williammorrow.com/reentry-eric-berger/
[book_bilstein_1996]: https://ntrs.nasa.gov/search?q=Stages+to+Saturn+Bilstein
[book_bird_sherwin_2005]: https://openlibrary.org/search?q=Bird+and+Sherwin+American+Prometheus
[book_buchanan_tullock_1962]: https://www.libertyfund.org/books/the-calculus-of-consent/
[book_chaikin_2007]: https://openlibrary.org/search?q=Chaikin+A+Man+on+the+Moon
[book_chang_2002]: https://www.penguin.co.uk/books/56082/kicking-away-the-ladder/9780857281050
[book_davenport_2018]: https://www.hachettebookgroup.com/titles/christian-davenport/the-space-barons/9781610398299/
[book_evans_1995]: https://press.princeton.edu/books/paperback/9780691037363/embedded-autonomy
[book_fernholz_2018]: https://www.hachettebookgroup.com/titles/tim-fernholz/rocket-billionaires/9781328662231/
[book_grimsey_lewis_2004]: https://www.e-elgar.com/shop/gbp/public-private-partnerships-9781840647112.html
[book_groves_1962]: https://openlibrary.org/search?q=Groves+Now+It+Can+Be+Told
[book_hosley_1996]: https://www.press.jhu.edu/books/title/1799/colt
[book_hounshell_1984]: https://jhupbooks.press.jhu.edu/title/american-system-mass-production-1800-1932
[book_hunter_2016]: https://csis-website-prod.s3.amazonaws.com/s3fs-public/legacy_files/files/publication/160930_Hunter_CreatingStrategicValue_Web.pdf
[book_isaacson_2023]: https://www.simonandschuster.com/books/Elon-Musk/Walter-Isaacson/9781982181284
[book_johnson_1982]: https://www.sup.org/books/title/?id=2143
[book_laffont_tirole_1993]: https://mitpress.mit.edu/9780262121743/a-theory-of-incentives-in-procurement-and-regulation/
[book_mazzucato_2013]: https://marianamazzucato.com/books/the-entrepreneurial-state
[book_mazzucato_2021]: https://marianamazzucato.com/books/mission-economy/
[book_mcafee_mcmillan_1988]: https://openlibrary.org/search?q=McAfee+and+McMillan+Incentives+in+Government+Contracting
[book_melman_1970]: https://openlibrary.org/search?q=Melman+Pentagon+Capitalism
[book_murray_cox_1989]: https://www.simonandschuster.com/books/Apollo/Charles-Murray/9780671706258
[book_newhouse_1982]: https://openlibrary.org/search?q=Newhouse+The+Sporty+Game
[book_rhodes_1986]: https://www.simonandschuster.com/books/The-Making-of-the-Atomic-Bomb/Richard-Rhodes/9781451677614
[book_rich_janos_1994]: https://www.hachettebookgroup.com/titles/ben-r-rich/skunk-works/9780316743006/
[book_serling_1992]: https://openlibrary.org/search?q=Serling+Legend+and+Legacy
[book_tirole_1988]: https://mitpress.mit.edu/9780262200714/the-theory-of-industrial-organization/
[book_vance_2015]: https://www.harpercollins.com/products/elon-musk-ashlee-vance
[book_wade_1990]: https://press.princeton.edu/books/paperback/9780691117294/governing-the-market
[book_weiss_2014]: https://www.cornellpress.cornell.edu/book/9780801479922/america-inc/
[book_williamson_1985]: https://www.simonandschuster.com/books/The-Economic-Institutions-of-Capitalism/Oliver-E-Williamson/9780684863740
[ref_arstechnica_space]: https://arstechnica.com/science/space/
[ref_bloomberg]: https://www.bloomberg.com/
[ref_congressional_record]: https://www.congress.gov/congressional-record
[ref_crs_commercial_crew_2018]: https://crsreports.congress.gov/product/pdf/R/R45272
[ref_crs_reports]: https://crsreports.congress.gov/
[ref_dod_contracts]: https://www.defense.gov/News/Contracts/
[ref_european_spaceflight]: https://europeanspaceflight.com/
[ref_gao_blue_origin_hls_protest_2021]: https://www.gao.gov/products/b-419783
[ref_gao_ccp_2019]: https://www.gao.gov/products/gao-19-504
[ref_gao_cots_2011]: https://www.gao.gov/products/gao-11-692t
[ref_gao_hls_2022]: https://www.gao.gov/products/gao-22-105506
[ref_gao_reports]: https://www.gao.gov/reports-testimonies
[ref_nasa_ccp_2014]: https://www.nasa.gov/commercialcrew
[ref_nasa_cctcap_press_2014]: https://www.nasa.gov/news-release/
[ref_nasa_cots_2011]: https://ntrs.nasa.gov/citations/20120000953
[ref_nasa_cots_report]: https://ntrs.nasa.gov/search?q=Commercial+Orbital+Transportation+Services
[ref_nasa_crs1_press_2008]: https://www.nasa.gov/international-space-station/commercial-resupply/
[ref_nasa_crs2_press_2016]: https://www.nasa.gov/news-release/nasa-awards-international-space-station-cargo-transport-contracts/
[ref_nasa_history]: https://history.nasa.gov/
[ref_nasa_hls_optionA_2021]: https://www.nasa.gov/news-release/as-artemis-moves-forward-nasa-picks-spacex-to-land-next-americans-on-moon/
[ref_nasa_hls_sustaining_2023]: https://www.nasa.gov/humans-in-space/artemis/
[ref_nasa_news]: https://www.nasa.gov/news/
[ref_nasa_ntrs]: https://ntrs.nasa.gov/
[ref_nasa_oig_ccp_2019]: https://oig.nasa.gov/audits/?_search=Commercial+Crew
[ref_nasa_oig_ccp_cargo_2018]: https://oig.nasa.gov/docs/IG-18-016.pdf
[ref_nasa_oig_cots_2013]: https://oig.nasa.gov/docs/IG-13-016.pdf
[ref_nasa_oig_hls_2021]: https://oig.nasa.gov/docs/IG-21-024.pdf
[ref_nasa_oig_reports]: https://oig.nasa.gov/audits/
[ref_nasaspaceflight]: https://www.nasaspaceflight.com/
[ref_nyt]: https://www.nytimes.com/section/science/space
[ref_nyt_starshield_2024]: https://www.nytimes.com/2024/02/16/us/politics/spacex-us-spy-agency-satellites.html
[ref_payload]: https://payloadspace.com/
[ref_public_admin_review]: https://onlinelibrary.wiley.com/journal/15406210
[ref_space_force_news]: https://www.spaceforce.mil/News/
[ref_space_force_nssl_phase1a_2018]: https://www.af.mil/News/Article-Display/Article/1671253/
[ref_space_force_nssl_phase2_2020]: https://www.spaceforce.mil/News/Article/2312953/
[ref_space_policy_journal]: https://www.sciencedirect.com/journal/space-policy
[ref_spacenews]: https://spacenews.com/
[ref_spacex_news_archive]: https://www.spacex.com/updates/
[ref_spacex_press_dm2_2020]: https://www.spacex.com/updates/dm-2-launch-crewed-flight/
[ref_spacex_press_dragon_c1_2010]: https://www.spacex.com/updates/
[ref_spacex_press_falcon1_flight4_2008]: https://www.spacex.com/news/2013/02/11/spacex-successfully-launches-falcon-1-orbit
[ref_spacex_starlink_direct_to_cell_tmobile_2022]: https://www.starlink.com/business/direct-to-cell
[ref_spacex_starshield]: https://www.spacex.com/starshield/
[ref_washington_post]: https://www.washingtonpost.com/business/technology/
[ref_wsj]: https://www.wsj.com/tech
[related_post_a281_spacex_framing]: {% post_url 2026-07-24-spacex_history_framing %}
[related_post_a282_spacex_value_gradient]: {% post_url 2026-07-25-spacex_history_value_gradient %}
[research_coase_1937]: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-0335.1937.tb00002.x
[research_fuchs_2010]: https://direct.mit.edu/rest/article/92/1/168/58109/
[research_hertzfeld_2002]: https://www.sciencedirect.com/science/article/abs/pii/S0265964602000188
[research_hodge_greve_2007]: https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6210.2007.00736.x
[research_kelly_2013]: https://www.sciencedirect.com/science/article/pii/S0094114X12002042
[research_krueger_1974]: https://www.jstor.org/stable/1808883
[research_nash_1950]: https://www.jstor.org/stable/1907266
[research_peeters_2018]: https://www.sciencedirect.com/science/article/pii/S0265964617302175
[research_reuters_starshield_2024]: https://www.reuters.com/technology/space/musks-spacex-is-building-spy-satellite-network-us-intelligence-agency-sources-2024-03-16/
[research_rubinstein_1982]: https://www.jstor.org/stable/1912531
[research_stigler_1971]: https://www.jstor.org/stable/3003160
[research_weinzierl_2018]: https://www.aeaweb.org/articles?id=10.1257/jep.32.2.173
[research_williamson_1975]: https://www.jstor.org/stable/40751236
[research_williamson_2002]: https://www.aeaweb.org/articles?id=10.1257/089533002760278776
[book_handberg_1994]: https://openlibrary.org/search?q=Handberg+Reinventing+NASA
[book_launius_1994]: https://malabarpubs.com/nasa-history/
[book_logsdon_2010]: https://openlibrary.org/search?q=Logsdon+John+F+Kennedy+and+the+Race+to+the+Moon
[book_mcdougall_1985]: https://jhupbooks.press.jhu.edu/title/heavens-and-earth
[book_milgrom_2004]: https://www.cambridge.org/9780521551847
[book_ruttan_2006]: https://global.oup.com/academic/product/is-war-necessary-for-economic-growth-9780195188042
[ref_boeing_starliner_cft_2024]: https://www.boeing.com/space/starliner
[ref_crs_artemis_2022]: https://crsreports.congress.gov/product/pdf/R/R47064
[ref_journal_public_procurement]: https://www.emerald.com/insight/publication/issn/1535-0118
[ref_nasa_hls_optionB_2022]: https://www.nasa.gov/news-release/nasa-provides-update-to-astronaut-moon-lander-plans-under-artemis/
[ref_payload_research]: https://payloadspace.com/research/
[ref_space_policy_online]: https://spacepolicyonline.com/
[ref_spacex_press_crew1_2020]: https://www.spacex.com/updates/
[ref_spacex_press_crs1_2012]: https://www.spacex.com/updates/
[ref_spacex_press_crs21_2020]: https://www.spacex.com/updates/
[ref_spacex_press_crs7_2015]: https://www.spacex.com/updates/
[ref_spacex_press_demo1_2019]: https://www.spacex.com/updates/
[ref_spacex_starship_program]: https://www.spacex.com/vehicles/starship/
[related_post_a132_sbir_intro]: {% post_url 2026-06-15-introduction_to_the_sbir_and_sttr_programs %}
[related_post_a138_sbir_phase3]: {% post_url 2026-06-21-phase_iii_and_the_valley_of_death_for_sbir_and_sttr %}
[related_post_a237_aerospace_framing]: {% post_url 2026-07-12-framing_and_the_co_development_mechanism %}
[related_post_a242_apollo_guidance]: {% post_url 2026-07-17-apollo_guidance_computer %}
[related_post_a246_silicon_valley_defense]: {% post_url 2026-07-21-silicon_valley_from_defense_contracting %}
[related_post_a247_software_defined_aerospace]: {% post_url 2026-07-22-software_defined_aerospace_and_autonomy %}
[related_post_a248_contemporary_snapshot]: {% post_url 2026-07-23-contemporary_snapshot_and_extrapolation %}
[related_post_a90_intro_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[related_post_a96_history_rocketplanes]: {% post_url 2026-02-27-history_of_rocketplanes %}
[research_bajari_mcmillan_tadelis_2009]: https://academic.oup.com/jleo/article-abstract/25/2/372/845776
[research_bajari_tadelis_2001]: https://www.jstor.org/stable/2696367
[research_bonvillian_2018]: https://mitpress.mit.edu/9780262038522/the-darpa-model-for-transformative-technologies/
[research_che_chung_1999]: https://academic.oup.com/rand/article-abstract/30/1/97/2701540
[research_gagnepain_ivaldi_2002]: https://academic.oup.com/rand/article-abstract/33/4/605/2603099
[research_myerson_1981]: https://pubsonline.informs.org/doi/10.1287/moor.6.1.58
[research_nelson_1959]: https://www.journals.uchicago.edu/doi/10.1086/258177
[research_nelson_1977]: https://www.jstor.org/stable/1817191
[book_muthoo_1999]: https://www.cambridge.org/9780521576475
[book_osborne_2000]: https://www.routledge.com/Public-Private-Partnerships/Osborne/p/book/9780415225236
[book_osborne_rubinstein_1990]: https://www.sciencedirect.com/book/9780125286329/bargaining-and-markets
[book_woo_cumings_1999]: https://www.cornellpress.cornell.edu/book/9780801485664/the-developmental-state/
[book_yescombe_2007]: https://www.sciencedirect.com/book/9780750680547/public-private-partnerships
[ref_aviation_week]: https://aviationweek.com/
[ref_breaking_defense]: https://breakingdefense.com/
[ref_defense_news]: https://www.defensenews.com/
[ref_the_space_review]: https://www.thespacereview.com/
[research_binmore_rubinstein_wolinsky_1986]: https://www.jstor.org/stable/2555382
[research_block_2008]: https://doi.org/10.1177/0032329208318731
[research_bovaird_2004]: https://doi.org/10.1177/0020852304044250
[research_grossman_hart_1986]: https://www.jstor.org/stable/1833199
[research_hart_1988]: https://www.jstor.org/stable/764953
[research_klein_crawford_alchian_1978]: https://www.jstor.org/stable/725234
[research_weiss_thurbon_2021]: https://doi.org/10.1080/13563467.2020.1766431
[book_christensen_1997]: https://www.hbsp.harvard.edu/product/1130-HBK-ENG
[ref_51_usc_51302_saa]: https://www.law.cornell.edu/uscode/text/51/51302
[ref_faa_ast_licensing_regs_450]: https://www.ecfr.gov/current/title-14/chapter-III/subchapter-C/part-450
[ref_faa_ast_regulations]: https://www.ecfr.gov/current/title-14/chapter-III
[ref_faa_launch_licenses_current]: https://www.faa.gov/space
[ref_far_part_15]: https://www.acquisition.gov/far/part-15
[ref_fcc_filings]: https://www.fcc.gov/wireless/systems-utilities/electronic-comment-filing-system-ecfs
[ref_fcc_starlink_2018]: https://docs.fcc.gov/public/attachments/FCC-18-38A1.pdf
[ref_fcc_starlink_gen2_2022]: https://docs.fcc.gov/public/attachments/FCC-22-91A1.pdf
[ref_itar_22_cfr_120_130]: https://www.ecfr.gov/current/title-22/chapter-I/subchapter-M
[ref_itu_radio_regulations_2020]: https://www.itu.int/pub/R-REG-RR
[ref_nasa_cots_solicitation_2006]: https://ntrs.nasa.gov/search?q=Commercial+Orbital+Transportation+Services+solicitation
[ref_nasa_far_supplement]: https://www.hq.nasa.gov/office/procurement/regs/NFS.pdf
[ref_nasa_orbital_debris_mitigation]: https://orbitaldebris.jsc.nasa.gov/mitigation/
[ref_nasa_rocketplane_kistler_termination_2007]: https://ntrs.nasa.gov/search?q=Rocketplane+Kistler+COTS+termination
[ref_nasa_std_8709_22]: https://standards.nasa.gov/
[research_anadol_cohen_2018]: https://www.hbs.edu/faculty/Pages/item.aspx?num=54001
[research_bower_christensen_1995]: https://hbr.org/1995/01/disruptive-technologies-catching-the-wave
[book_bilstein_2001]: https://jhupbooks.press.jhu.edu/title/flight-america
[book_crouch_2003]: https://wwnorton.com/books/Wings/
[book_fallows_1981]: https://archive.org/details/nationaldefense00fall
[book_hewlett_anderson_1962]: https://openlibrary.org/search?q=Hewlett+and+Anderson+The+New+World
[book_kaplan_1991]: https://openlibrary.org/search?q=Kaplan+The+Wizards+of+Armageddon
[book_miller_1995]: https://www.aerofax.com/product-page/lockheed-skunk-works
[book_mindell_2008]: https://mitpress.mit.edu/9780262516105/digital-apollo/
[book_neufeld_1995]: https://openlibrary.org/search?q=Neufeld+The+Rocket+and+the+Reich
[book_neufeld_2013]: https://openlibrary.org/search?q=Neufeld+Von+Braun
[ref_gao_cots_2009]: https://www.gao.gov/products/gao-09-618
[ref_journal_space_law]: https://airandspacelaw.olemiss.edu/journal-of-space-law/
[ref_space_legislation_review]: https://www.mcgill.ca/iasl/
[ref_un_liability_convention_1972]: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/liability-convention.html
[ref_un_outer_space_treaty_1967]: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/outerspacetreaty.html
[ref_un_registration_convention_1976]: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/registration-convention.html
[ref_uscsla_2015]: https://www.congress.gov/114/plaws/publ90/PLAW-114publ90.pdf
[research_corts_singh_2004]: https://academic.oup.com/jleo/article-abstract/20/1/230/970131
[research_kalnins_mayer_2004]: https://doi.org/10.1093/jleo/ewh030
[research_levin_tadelis_2010]: https://academic.oup.com/qje/article-abstract/125/3/1103/1903637
[ref_spacex_falcon9_users_guide]: https://www.spacex.com/vehicles/falcon-9/
[ref_fcc_direct_to_cell_2024]: https://docs.fcc.gov/public/attachments/DA-24-208A1.pdf
[book_adner_2012]: https://openlibrary.org/search?q=Adner+The+Wide+Lens
[book_andrewes_1996]: https://openlibrary.org/search?q=Andrewes+The+Quest+for+Longitude
[book_chadeau_1996]: https://openlibrary.org/search?q=Chadeau+Airbus+Industrie+History
[book_collins_2010]: https://www.harpercollins.com/products/the-language-of-life-francis-s-collins
[book_concina_2006]: https://www.cambridge.org/9780521187459
[book_dixit_pindyck_1994]: https://openlibrary.org/search?q=Dixit+and+Pindyck+Investment+Under+Uncertainty
[book_fligstein_2001]: https://press.princeton.edu/books/paperback/9780691102542/the-architecture-of-markets
[book_gertner_2012]: https://www.penguinrandomhouse.com/books/206061/the-idea-factory-by-jon-gertner/
[book_ho_2009]: https://www.dukeupress.edu/liquidated
[book_iansiti_levien_2004]: https://www.hbsp.harvard.edu/product/3921-HBK-ENG
[book_krige_et_al_2000]: https://www.esa.int/About_Us/ESA_history
[book_krippner_2011]: https://www.hup.harvard.edu/books/9780674066199
[book_lane_1934]: https://jhupbooks.press.jhu.edu/title/venetian-ships-and-shipbuilders-renaissance
[book_latour_1987]: https://www.hup.harvard.edu/books/9780674792913
[book_liker_2004]: https://www.mheducation.com/highered/product/toyota-way-liker/M9780071392310.html
[book_mackenzie_2006]: https://mitpress.mit.edu/9780262633673/an-engine-not-a-camera/
[book_mccullough_1977]: https://www.simonandschuster.com/books/The-Path-Between-the-Seas/David-McCullough/9780743201377
[book_mcintyre_1992]: https://openlibrary.org/search?q=McIntyre+Airbus+Industrie
[book_metcalfe_1998]: https://www.routledge.com/Evolutionary-Economics-and-Creative-Destruction/Metcalfe/p/book/9780415158671
[book_musa_1998]: https://www.mheducation.com/highered/product/software-reliability-engineering-musa/M9780079132710.html
[book_nelson_winter_1982]: https://www.hup.harvard.edu/books/9780674272286
[book_oconnor_kleyner_2012]: https://openlibrary.org/search?q=O+Connor+and+Kleyner+Practical+Reliability+Engineering
[book_preda_2009]: https://openlibrary.org/search?q=Preda+Framing+Finance
[book_sobel_1995]: https://www.bloomsbury.com/us/longitude-9780802715296/
[book_trigeorgis_1996]: https://mitpress.mit.edu/9780262201025/real-options/
[book_womack_jones_roos_1990]: https://www.simonandschuster.com/books/The-Machine-That-Changed-the-World/James-P-Womack/9780743299794
[book_zaloom_2006]: https://openlibrary.org/search?q=Zaloom+Out+of+the+Pits
[ref_incose_handbook]: https://www.incose.org/publications/se-handbook
[research_adner_2017]: https://doi.org/10.1177/0149206316678451
[research_barney_1991]: https://journals.sagepub.com/doi/10.1177/014920639101700108
[research_callon_1986]: https://onlinelibrary.wiley.com/doi/10.1111/j.1467-954X.1984.tb00113.x
[research_cohen_levinthal_1990]: https://www.jstor.org/stable/2393553
[research_duane_1964]: https://ieeexplore.ieee.org/document/4051464
[research_jacobides_et_al_2018]: https://onlinelibrary.wiley.com/doi/10.1002/smj.2904
[research_lane_koka_pathak_2006]: https://journals.aom.org/doi/10.5465/amr.2006.22527456
[research_law_1987]: https://mitpress.mit.edu/9780262521376/the-social-construction-of-technological-systems/
[research_maier_1998]: https://onlinelibrary.wiley.com/doi/10.1002/(SICI)1520-6858(1998)1:4%3C267::AID-SYS3%3E3.0.CO;2-D
[research_sage_cuppan_2001]: https://doi.org/10.3233/iks-2001-00045
[research_teece_pisano_shuen_1997]: https://onlinelibrary.wiley.com/doi/10.1002/%28SICI%291097-0266%28199708%2918%3A7%3C509%3A%3AAID-SMJ882%3E3.0.CO%3B2-Z
[research_todorova_durisin_2007]: https://journals.aom.org/doi/10.5465/amr.2007.25275513
[research_wernerfelt_1984]: https://onlinelibrary.wiley.com/doi/10.1002/smj.4250050207
[research_zahra_george_2002]: https://journals.aom.org/doi/10.5465/amr.2002.6587995
