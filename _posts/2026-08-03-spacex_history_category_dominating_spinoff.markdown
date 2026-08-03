---
layout: post
mathjax: true
comments: true
title: "History of SpaceX: The Category-Dominating Commercial Spinoff and the Internalization of Anchor Demand"
date: 2026-08-03 09:00:00 +0000
categories: history business aerospace
series: spacex_history
series_title: History of SpaceX
series_index: 11
---

<!-- A291 -->
<script>console.log("A291");</script>

This article is the eleventh in the History of SpaceX series and the third and last treating the capital-formation legs that the [series opener][related_post_a281_spacex_framing] introduced. The category-dominating commercial spinoff concerns the business the venture built on top of its own capability, and the article's organizing claim is that the spinoff is not a diversification into an adjacent market but the internalization of an anchor customer. Where the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] treats a government customer buying launches, this article treats the venture becoming the customer it had previously needed someone else to be. The decisive economic property is not that the spinoff grew large. It is that the spinoff consumes the parent's output at marginal cost while every competitor attempting the same business must pay a market price the parent sets. The article walks the January 2015 announcement and the capacity argument that motivated it, the deployment sequence from the first operational batch of May 2019 through the service beta of 2020 and the commercial rollout of 2021, the vertical integration and the internal transfer price that the whole arrangement turns upon, the coupling between constellation deployment and launch cadence, the subscriber and revenue trajectory across the 2020 through drafting-date period, the direct-to-cell extension beginning with the carrier partnership announced in 2022, the capital intensity and the replenishment obligation that a short-lifetime constellation imposes, and the regulatory position across the Federal Communications Commission, the International Telecommunication Union, and the national regulators whose authorizations the service requires. The article contrasts the configuration against the Iridium and Globalstar precedents, in which comparable constellations were built without a captive launch capability, and against the OneWeb and Kuiper cases, in which competitors attempted the business while buying launch at market. The article closes with an explicit pattern-extraction section stating the abstract commercial-spinoff mechanic in a form other informed readers can recognize in adjacent domains.

## The Category-Dominating Spinoff Mapping Problem

The mapping problem for a comprehensive treatment of the commercial-spinoff leg is the question of what the spinoff business actually is in economic terms, what it consumed from the parent, what it returned, and by what date the return exceeded the parent's requirement for external capital.

The last element is the capital-formation question and it is the reason the spinoff belongs in this series rather than in a treatment of the satellite communications industry. The two preceding legs, which the [Government-Anchor Capital-Formation Leg article A289][related_post_a289_spacex_government_anchor_leg] and the [Patient-Private Capital-Formation Leg article A290][related_post_a290_spacex_patient_private_leg] develop, both supply capital from outside the firm on terms that constrain it. The government leg supplies capital against milestones and carries a requirement. The private leg provides capital against equity and carries a dilution. Retained earnings carry neither. The spinoff leg is therefore the only one of the three that terminates the capital-formation problem rather than managing it, and the analytically interesting question is what conditions a spinoff must satisfy to reach that scale.

The ordinary account treats the constellation as a diversification, on the reasoning that a launch company entered the telecommunications business. That account is not false and it is not an explanation, because it offers no reason why a launch company should have any advantage in telecommunications, and absent such an advantage the diversification would destroy value for the reasons the corporate-diversification literature the [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] surveys documents at length.

The general form of the problem can be stated compactly. Let $q^{\text{internal}}$ denote the launch capacity the spinoff consumes and $q^{\text{external}}$ the capacity sold to third parties. The parent's total output satisfies

$$q^{\text{total}} = q^{\text{internal}} + q^{\text{external}}$$

with the ordinary treatment of a launch business considering only the second term. The article's position is that the first term became the larger one and that the transition is the central event in the firm's commercial history. The transition admits statement as a share crossing one half

$$s(t) = \frac{q^{\text{internal}}(t)}{q^{\text{total}}(t)} \qquad \text{with} \qquad \frac{ds}{dt} > 0 \;\; \text{and} \;\; s(t) > \tfrac{1}{2} \;\; \text{after some date}$$

with the date at which the majority of the firm's own launches served its own constellation being the point at which the launch business ceased to be primarily a merchant business. The quantity is reconstructible from public launch manifests and is one of the few claims in this article that does not depend on unpublished financial data. The manifest record is traceable through the [Federal Aviation Administration Office of Commercial Space Transportation][ref_faa_ast] licensing file and its [licensing regulations][ref_faa_ast_regulations], with the sector compilations at [Space Capital][ref_space_capital] and [BryceTech][ref_bryce_tech] and the programme history at [NASA history][ref_nasa_history]. The scholarly outlets in which such reconstructions are published are surveyed at [SSRN][ref_ssrn].

The relation among the three capital-formation legs admits compact statement as a decomposition of the external requirement

$$K^{\text{external}}(t) = B(t) - K^{\text{government}}(t) - R^{\text{retained}}(t)$$

with the government term the subject of the [Government-Anchor Capital-Formation Leg article A289][related_post_a289_spacex_government_anchor_leg], the residual met by the private leg the [Patient-Private Capital-Formation Leg article A290][related_post_a290_spacex_patient_private_leg] describes, and the third term the subject of this article. The three legs are therefore not parallel alternatives but terms in a single budget identity, and the sequence in which they arrived is the sequence in which each became available.

The identification problem is the counterfactual, and it admits the compact form

$$\Delta V^{\text{spinoff}}(t) = V^{\text{observed}}(t) - V^{\text{no spinoff counterfactual}}(t)$$

with the attribution equal to the difference between the observed trajectory and the counterfactual in which the same launch capability existed and no constellation was built. The counterfactual is partially observable, because contemporaneous ventures attempted the constellation without the launch capability and the sector gives their outcomes.

## Methodological Commitments

The article commits to the same seven methodological positions the [series opener][related_post_a281_spacex_framing] established, restated at compact reference level.

The first commitment is descriptive-analytical framing rather than prescriptive advocacy.

The second commitment is dual-register composition with both general-history and abstract-mechanic registers.

The third commitment is primary-source anchoring. The documentary position for this article is stronger than that of the two preceding capital-formation articles on regulatory matters and comparably weak on financial ones. The regulatory record is public and extensive, comprising the [Federal Communications Commission authorizations][ref_fcc_starlink_2018] and the [second-generation authorization][ref_fcc_starlink_gen2_2022], the [direct-to-cell authorization][ref_fcc_direct_to_cell_2024], the general [Commission filing system][ref_fcc_filings], the [International Telecommunication Union Radio Regulations][ref_itu_radio_regulations_2020], and the [Federal Aviation Administration Office of Commercial Space Transportation][ref_faa_ast] licensing record. The service and vehicle record is published at [Starlink][ref_spacex_starlink], the [Starlink technology description][ref_starlink_technology], the [SpaceX corporate record][ref_spacex_company], the [SpaceX news archive][ref_spacex_news_archive], and the [Falcon 9 vehicle page][ref_spacex_falcon9_vehicle]. The financial record is substantially absent, because the firm is private and the spinoff has never been separately reported.

The fourth commitment is contested-claim marking. Every subscriber count, revenue figure, satellite production rate, and launch cost in this article is a reconstructive estimate.

The fifth commitment is temporal indexing as a mid-2026 snapshot.

The sixth commitment is terminological transparency with the Terminological Note section below.

The seventh commitment is thesis-not-proof framing of the capital-formation closure claim.

## The Commercial Spinoff as an Economic Property

The category-dominating commercial spinoff is treated as an economic property of the relationship between a capability and a business built upon it, distinguishing ventures whose spinoff consumes the parent's output at internal cost from ventures whose adjacent business must transact at market.

The property is a property of the vertical relationship rather than of the spinoff's market position, and the article's central analytical move is to state it that way. A large spinoff purchasing its inputs at market prices is a diversification and is subject to every objection the diversification literature raises. A spinoff purchasing its inputs at marginal cost from a parent with idle capacity is something else, and the difference is the whole subject of this article.

The cost position can be stated compactly. Let $c^{\text{marginal}}$ denote the parent's marginal cost of supplying one launch and let $p^{\text{market}}$ denote the price a third party pays. The spinoff's launch cost and a competitor's launch cost stand in the relation

$$c^{\text{spinoff}} = c^{\text{marginal}} \qquad \text{against} \qquad c^{\text{competitor}} = p^{\text{market}} \geq c^{\text{marginal}} + m$$

with $m$ the parent's margin on external sales. The competitor's disadvantage per launch is therefore at least the parent's entire margin, and it is incurred on every launch of a deployment campaign requiring many of them.

The aggregate effect over a deployment campaign of $N$ launches takes the form

$$\Delta C = N \cdot m$$

with the disadvantage scaling linearly in the campaign size. A constellation is precisely the application in which $N$ is large, which is the structural reason the advantage matters here and would not matter for a business requiring a single launch.

The condition a competitor must satisfy to remain viable against the gap can be written as

$$\Pi^{\text{competitor}} > 0 \iff \left( \text{ARPU} - c^{\text{operating}} \right) \cdot n^{\text{sub}} \; > \; C^{\text{deployment}} + N \cdot m$$

with the final term the disadvantage the integrated operator does not bear. A competitor must therefore either serve more subscribers, charge more, or operate more cheaply than the integrated operator merely to reach the same margin, and it must do so while holding an identical satellite technology and an identical spectrum position. The article's position is that no contemporaneous competitor has demonstrated any of the three.

The capacity argument that motivates the arrangement can be stated as a utilization condition. A launch capability has a fixed cost of maintaining production and operations that is incurred whether or not vehicles fly. Let $\bar{q}$ denote the capacity the fixed cost sustains and $q^{\text{external}}$ the external demand. Where

$$q^{\text{external}} < \bar{q}$$

the residual capacity is idle and its marginal cost of use is low. The spinoff converts that residual into a revenue stream, and the arrangement is best understood as the monetization of a by-product rather than as an entry into a new market.

The effect on the parent's own cost structure follows directly, because a fixed cost spread across more flights falls per flight. The average cost has the form

$$\bar{c}(q) = \frac{F}{q} + c^{\text{marginal}} \qquad \text{with} \qquad \frac{d\bar{c}}{dq} < 0$$

with $F$ the fixed cost of maintaining production and operations. The fixed component includes the launch-site tenancies documented in the [Kennedy Space Center Launch Complex 39A lease][ref_ksc_lc39a_lease] and the [Vandenberg Space Launch Complex 4E environmental record][ref_vandenberg_slc4e_ea], together with the range and licensing obligations the [Office of Commercial Space Transportation regulations][ref_faa_ast_regulations] and the [Part 450 licensing rule][ref_faa_ast_licensing_regs_450] impose, all of which are incurred whether or not a given vehicle flies. The spinoff therefore lowers the cost at which the parent can serve its external customers as a by-product of serving itself, which is the reverse of the resource-diversion the diversification literature predicts and which the article regards as the strongest single piece of evidence that the arrangement is not a diversification.

The capital-formation function is stated as a crossover condition. Let $R(t)$ denote the spinoff's free cash contribution and $B(t)$ the parent's mission-directed burn. The external capital requirement is

$$K^{\text{external}}(t) = \max \left\{ 0, \; B(t) - R(t) \right\}$$

and the leg closes the capital-formation problem at the date $t^{\ast}$ satisfying

$$R(t^{\ast}) \geq B(t^{\ast})$$

after which external capital becomes optional. The article's position is that the date is the single most consequential unobserved quantity in the series, because every governance and financing arrangement the preceding articles describe exists to bridge the interval before it.

## Cross-Disciplinary Framings

The commercial-spinoff property admits characterization from several disciplinary traditions beyond the mission-oriented-innovation framework the series adopts as primary.

The vertical-integration tradition traces from [Coase 1937][research_coase_1937] The Nature of the Firm through [Williamson 1971][research_williamson_1971], [Williamson 1985][book_williamson_1985] The Economic Institutions of Capitalism, [Klein Crawford and Alchian 1978][research_klein_crawford_alchian_1978], [Monteverde and Teece 1982][research_monteverde_teece_1982], and [Grossman and Hart 1986][research_grossman_hart_1986]. The framing provides the account of when a firm should make rather than buy, and its contribution here is to identify the condition the case satisfies. The ordinary condition compares costs and may be written

$$\text{make} \iff c^{\text{internal}} + g < p^{\text{market}}$$

with $g$ the governance cost of operating the activity inside the firm. The present case does not turn on that inequality. The constellation requires a launch cadence no external supplier could commit to at any price the programme could bear, so the relevant condition is

$$\text{make} \iff \nexists \; \text{supplier with} \; \dot{q}^{\text{available}} \geq \dot{q}^{\text{required}}$$

with the make decision following from supply unavailability rather than from a cost comparison. The distinction matters because it means the integration would have been correct even had it been more expensive than buying, which is not the case the transaction-cost literature ordinarily treats.

The appropriability tradition traces from [Teece 1986][research_teece_1986] Profiting from Technological Innovation. The framing is the most directly applicable of any in this survey. It holds that an innovator captures value only where it controls the complementary assets an innovation requires, and it identifies launch capacity as precisely such an asset for a constellation business. The captured share admits the compact form

$$\sigma^{\text{innovator}} = \sigma\!\left( \text{control of complementary assets}, \; \text{strength of the appropriability regime} \right)$$

with the value accruing to the holder of the scarce complement where the innovation itself is imitable. Satellite manufacture is imitable and launch capacity at the required cadence was not, which is the framing's explanation for where the value settled. The [Value Capture article A284][related_post_a284_spacex_value_capture] develops the general point and this article offers the sharpest instance of it in the series.

The network-effects and standards tradition traces from [Katz and Shapiro 1985][research_katz_shapiro_1985] Network Externalities Competition and Compatibility, [Farrell and Saloner 1985][research_farrell_saloner_1985], [Arthur 1989][research_arthur_1989] Competing Technologies Increasing Returns and Lock-In, and [David 1985][research_david_1985] Clio and the Economics of QWERTY. The framing gives the account of why a constellation business exhibits increasing returns, because coverage completeness is a step function of satellite count. The value relation takes the form

$$V(S) \ll \frac{S}{S^{\ast}} \cdot V(S^{\ast}) \qquad \text{for} \qquad S < S^{\ast}$$

with $S^{\ast}$ the count at which continuous coverage is attained. The convexity below the threshold is what makes the business unfinanceable against its own early revenue and is the point at which this article's subject connects to the two preceding capital-formation legs.

The two-sided-market and platform tradition traces from [Rochet and Tirole 2003][research_rochet_tirole_2003] and [Rochet and Tirole 2006][research_rochet_tirole_2006] through [Rysman 2009][research_rysman_2009], [Parker and Van Alstyne 2005][research_parker_vanalstyne_2005], [Evans 2003][research_evans_2003], [Boudreau 2010][research_boudreau_2010], [Hagiu and Wright 2015][research_hagiu_wright_2015], [Gawer 2014][research_gawer_2014], [Gawer and Cusumano 2014][research_gawer_cusumano_2014], [Jacobides Cennamo and Gawer 2018][research_jacobides_et_al_2018], with the book-length treatments at [Cusumano and Gawer 2002][book_cusumano_gawer_2002], [Iansiti and Levien 2004][book_iansiti_levien_2004], and [Van Alstyne Parker and Choudary 2016][book_vanalstyne_parker_choudary_2016]. The framing applies partially and the article marks the limit. A genuinely two-sided market exhibits a cross-side externality, admitting the compact condition

$$\frac{\partial u^{A}}{\partial n^{B}} > 0 \qquad \text{and} \qquad \frac{\partial u^{B}}{\partial n^{A}} > 0$$

with the utility of each side rising in the participation of the other. The direct-to-cell extension satisfies the condition, because it serves subscribers through carriers and the value to each rises with the other. The consumer broadband service does not, because a subscriber's service quality is weakly decreasing in the number of other subscribers sharing a cell. The broadband business is therefore an ordinary subscription business with a satellite delivery mechanism, and importing platform conclusions into it is an error the commentary makes routinely.

The regulated-industry and natural-monopoly tradition traces from [Sharkey 1982][book_sharkey_1982] The Theory of Natural Monopoly through [Kahn 1988][book_kahn_1988] The Economics of Regulation, [Stigler 1971][research_stigler_1971] The Theory of Economic Regulation, [Krueger 1974][research_krueger_1974], [Bain 1968][book_bain_1968], [Scherer and Ross 1990][book_scherer_ross_1990], and [Tirole 1988][book_tirole_1988]. The framing yields the account of what a finite orbital and spectral resource implies. Natural monopoly in the technical sense requires cost subadditivity, admitting the compact condition

$$C\!\left( \textstyle\sum_i y_i \right) < \sum_i C(y_i)$$

for the relevant output vectors, meaning a single operator serves the market more cheaply than several. The condition plausibly holds for a constellation, because coverage must be complete regardless of subscriber count and duplicating it duplicates the entire fixed cost. The tradition is therefore the one most likely to generate the regulatory response the article's closing questions anticipate, and the article notes that the subadditivity argument is stronger here than in most industries where it is asserted.

The competition-policy tradition traces from [Bork 1978][book_bork_1978] The Antitrust Paradox through [Posner 2001][book_posner_2001], [Hovenkamp 2005][book_hovenkamp_2005], and [Khan 2017][research_khan_2017] Amazon's Antitrust Paradox. The [Khan 2017][research_khan_2017] treatment is directly relevant because it concerns a vertically integrated firm that competes with the parties who depend on its infrastructure, which is the exact structure this article describes once external launch customers and the constellation compete for the same capacity. The foreclosure incentive admits the compact statement

$$\frac{\partial \Pi^{\text{consolidated}}}{\partial q^{\text{external to a rival constellation}}} = m - \frac{\partial \Pi^{\text{constellation}}}{\partial \left( \text{rival capability} \right)}$$

with the sign ambiguous and turning on whether the margin from selling a launch exceeds the downstream harm from enabling a competitor. The article notes that the firm has in fact sold launch capacity to a rival constellation programme, which is evidence that the first term has so far dominated, and that the observation cuts against the strongest form of the foreclosure concern.

The technology-cycle tradition traces from [Abernathy and Clark 1985][research_abernathy_clark_1985] through [Anderson and Tushman 1990][research_anderson_tushman_1990], [Henderson and Clark 1990][research_henderson_clark_1990] Architectural Innovation, [Bower and Christensen 1995][research_bower_christensen_1995], [Christensen and Rosenbloom 1995][research_christensen_rosenbloom_1995], [Utterback 1994][book_utterback_1994], [Christensen 1997][book_christensen_1997], [Christensen and Raynor 2003][book_christensen_raynor_2003], and [Bresnahan and Trajtenberg 1995][research_bresnahan_trajtenberg_1995] General Purpose Technologies. The framing treats the constellation as a discontinuity in the delivery of connectivity rather than as an improvement in satellite communications. The relevant performance comparison can be written as

$$\ell^{\text{LEO}} \approx \frac{h^{\text{LEO}}}{h^{\text{GEO}}} \cdot \ell^{\text{GEO}} \qquad \text{with} \qquad \frac{h^{\text{LEO}}}{h^{\text{GEO}}} \sim 10^{-2}$$

with $\ell$ the propagation latency and $h$ the orbital altitude. The two-order reduction moves the service across the threshold at which interactive applications become usable, which is a discontinuity in the served application set rather than an improvement along an existing performance dimension. That is the reading which best explains why the incumbent geostationary operators, whose assets were optimized for a different point in the design space, did not respond.

The capability tradition traces from [Penrose 1959][book_penrose_1959] The Theory of the Growth of the Firm through [Teece Pisano and Shuen 1997][research_teece_pisano_shuen_1997], [Wernerfelt 1984][research_wernerfelt_1984], [Barney 1991][research_barney_1991], [Nelson and Winter 1982][book_nelson_winter_1982], and [Metcalfe 1998][book_metcalfe_1998]. The framing contributes the account of the spinoff as an application of surplus capability, which is the reading closest to the article's own.

The telecommunications-history tradition traces from [Wu 2010][book_wu_2010] The Master Switch, [Temin and Galambos 1987][book_temin_galambos_1987] The Fall of the Bell System, [Levin 2010][book_levin_2010], [Sobel 1995][book_sobel_1995], [Nye 1990][book_nye_1990] Electrifying America, and [Hughes 1983][book_hughes_1983] Networks of Power. The framing yields the base rates and is the tradition that most consistently predicts a regulatory intervention following the attainment of a dominant position in a communications infrastructure. The institutional apparatus through which such an intervention would be argued is at the [European Corporate Governance Institute][ref_ecgi], the [Harvard Law School Forum on Corporate Governance][ref_harvard_corpgov_forum], the [Council of Institutional Investors][ref_cii], and the [Organisation for Economic Co-operation and Development corporate-governance principles][ref_oecd_corporate_governance], with the listing and index regimes at the [New York Stock Exchange Listed Company Manual][ref_nyse_listed_company_manual], the [Nasdaq listing rules][ref_nasdaq_listing_rules], [FTSE Russell][ref_ftse_russell], and [S and P Dow Jones Indices][ref_spdji]. None of it reaches a firm that never lists, which is the observation the [Governance article A287][related_post_a287_spacex_governance] develops and which this article notes applies with equal force to a communications infrastructure of this scale.

The public-administration and procurement tradition surveyed at [Public Administration Review][ref_public_admin_review] and the [Journal of Public Procurement][ref_journal_public_procurement] supplies the account of how a government buyer relates to a supplier that has become dominant in a commercial category, and the macroeconomic context in which the buildout occurred is documented at the [National Bureau of Economic Research][ref_nber] and the [Conference Board][ref_conference_board].

The dynamic-capabilities tradition traces from [Teece Pisano and Shuen 1997][research_teece_pisano_shuen_1997] through [Teece 2007][research_teece_2007], [Teece 2018][research_teece_2018], [Eisenhardt and Martin 2000][research_eisenhardt_martin_2000], [Helfat and Peteraf 2003][research_helfat_peteraf_2003], [Winter 2003][research_winter_2003], [Peteraf 1993][research_peteraf_1993], and [Grant 1996][research_grant_1996], with the absorptive-capacity and knowledge lines at [Cohen and Levinthal 1990][research_cohen_levinthal_1990] and [Kogut and Zander 1992][research_kogut_zander_1992] and the exploration and exploitation framing at [March 1991][research_march_1991] and [Levitt and March 1988][research_levitt_march_1988]. The tradition's contribution here is to identify the spinoff as an application of a capability rather than an acquisition of one, which is the distinction that separates it from a conglomerate entry and which the diversification objection elides.

The innovation-systems and endogenous-growth tradition traces from [Arrow 1962][research_arrow_1962] and [Nelson 1959][research_nelson_1959] through [Romer 1990][research_romer_1990], [Griliches 1979][research_griliches_1979], [Dosi 1988][research_dosi_1988], [Pavitt 1984][research_pavitt_1984], [Freeman and Soete 1997][research_freeman_soete_1997], and [Bonvillian 2018][research_bonvillian_2018], with the book-length treatments at [Nelson 1993][book_nelson_1993], [Mowery and Rosenberg 1998][book_mowery_rosenberg_1998], [Ruttan 2006][book_ruttan_2006], and [Lipsey Carlaw and Bekar 2005][book_lipsey_carlaw_bekar_2005] Economic Transformations. The tradition provides the general-purpose-technology framing under which cheap access to orbit is an input to activities not yet identified, which is the strongest form of the case for the arrangement and the one least susceptible to measurement.

The contract-and-procurement tradition traces from [Bajari and Tadelis 2001][research_bajari_tadelis_2001] through [Levin and Tadelis 2010][research_levin_tadelis_2010], [Lafontaine and Slade 2007][research_lafontaine_slade_2007] Vertical Integration and Firm Boundaries, [Corts and Singh 2004][research_corts_singh_2004], and [Gagnepain and Ivaldi 2002][research_gagnepain_ivaldi_2002], with the regulatory-contracting treatment at [Laffont and Tirole 1993][book_laffont_tirole_1993]. The [Lafontaine and Slade 2007][research_lafontaine_slade_2007] survey is the most directly useful, because it collects the empirical evidence on when integration improves outcomes and finds the evidence considerably more favorable to integration than the theoretical literature's caution suggests.

The organizational-reliability tradition traces from [Perrow 1984][book_perrow_1984] Normal Accidents through [Vaughan 1996][book_vaughan_1996] The Challenger Launch Decision, [Weick 1979][book_weick_1979], [Weick and Sutcliffe 2007][book_weick_sutcliffe_2007], [Selznick 1949][book_selznick_1949], and [Mindell 2008][book_mindell_2008]. The tradition bears on the replenishment treadmill in a way the financial treatment does not, because a production and launch tempo sustained indefinitely is an organizational condition rather than a capital one, and the tradition's central finding is that sustained high tempo erodes the margins that absorb error.

The commons and institutional tradition traces from [Ostrom 1990][book_ostrom_1990] Governing the Commons through [North 1990][book_north_1990] and [Acemoglu and Robinson 2012][book_acemoglu_robinson_2012], with the historical instances at [Grief 2006][book_grief_2006], [Lane 1934][book_lane_1934], and [de Vries and van der Woude 1997][book_devries_vanderwoude_1997]. The [Ostrom 1990][book_ostrom_1990] treatment matters because it establishes that unpriced common-pool resources are not invariably destroyed and that the conditions under which local governance succeeds are identifiable, which reframes the orbital-congestion question from a prediction of catastrophe into a question about whether those conditions obtain.

The science-and-technology-studies tradition traces from [Bijker Hughes and Pinch 1987][book_bijker_hughes_pinch_1987] through [Bijker 1995][book_bijker_1995], [Latour 1987][book_latour_1987], [MacKenzie 1990][book_mackenzie_1990] Inventing Accuracy, [Hughes 1983][book_hughes_1983], and [Nye 1998][book_nye_1998]. The tradition offers the account of how a technical system and its user expectations are co-constructed, which is relevant because the service category this article calls category-dominating did not exist as a consumer expectation before the system that serves it.

The financial-sociology tradition traces from [MacKenzie 2006][book_mackenzie_2006] An Engine Not a Camera through [Ho 2009][book_ho_2009], [Preda 2009][book_preda_2009], [Zaloom 2006][book_zaloom_2006], [Krippner 2011][book_krippner_2011], [Fligstein 2001][book_fligstein_2001] The Architecture of Markets, and [Berle and Means 1932][book_berle_means_1932]. The tradition treats the categories through which a business is valued as institutionally produced, which bears directly on this article's observation that the reported segmentation of a private firm is an accounting choice rather than an economic fact.

The corporate-control tradition traces from [Manne 1965][research_manne_1965] through [Grossman and Hart 1988][research_grossman_hart_1988], [Harris and Raviv 1988][research_harris_raviv_1988], [DeAngelo and DeAngelo 1985][research_deangelo_deangelo_1985], [Fama and Jensen 1983][research_fama_jensen_1983], [Jensen 1986][research_jensen_1986], [Shleifer and Vishny 1997][research_shleifer_vishny_1997], [Bebchuk Kraakman and Triantis 2000][research_bebchuk_kraakman_triantis_2000], [Bebchuk and Kastiel 2017][research_bebchuk_kastiel_2017], [Gompers Ishii and Metrick 2003][research_gompers_ishii_metrick_2003], [La Porta Lopez-de-Silanes Shleifer and Vishny 1998][research_laporta_et_al_1998], [Hart and Moore 1990][research_hart_moore_1990], [Hart 1988][research_hart_1988], and [Williamson 2002][research_williamson_2002], with the book-length treatments at [Hansmann 1996][book_hansmann_1996], [Easterbrook and Fischel 1991][book_easterbrook_fischel_1991], and [Roe 1994][book_roe_1994]. The tradition is the one the new Constraint the Spinoff Installs section draws upon, and its relevant limitation is that it theorizes control exercised through ownership and has comparatively little to say about control exercised through a service or licensing relationship.

The developmental-state tradition traces from [Johnson 1982][book_johnson_1982] MITI and the Japanese Miracle through [Amsden 1989][book_amsden_1989], [Wade 1990][book_wade_1990], [Evans 1995][book_evans_1995], [Chang 2002][book_chang_2002], and [Woo-Cumings 1999][book_woo_cumings_1999], and the project-finance apparatus at [Grimsey and Lewis 2004][book_grimsey_lewis_2004] and [Yescombe 2007][book_yescombe_2007] supplies the contemporary institutional form for infrastructure whose construction period exceeds its financiers' horizon.

The market-design tradition traces from [Myerson 1981][research_myerson_1981] through [Milgrom 2004][book_milgrom_2004] and [McAfee and McMillan 1988][book_mcafee_mcmillan_1988], and it bears on the spectrum-coordination regime rather than on the tender arrangement the preceding article treats, because an administration allocating priority among filings is conducting an assignment without prices.

The space-economics tradition traces from [Weinzierl 2018][research_weinzierl_2018] Space the Final Economic Frontier through [Hertzfeld 2002][research_hertzfeld_2002], [Adilov Alexander and Cunningham 2014][research_adilov_et_al_2014], [Weeden and Chow 2012][research_weeden_chow_2012], and [Zimmerman 2011][research_zimmerman_2011], with the policy histories at [Launius 2004][book_launius_2004], [McCurdy 1994][book_mccurdy_1994], [Logsdon 1970][book_logsdon_1970], [Handberg 1994][book_handberg_1994], [McDougall 1985][book_mcdougall_1985], and [Heppenheimer 1999][book_heppenheimer_1999].

## The January 2015 Announcement and the Capacity Argument

The constellation programme was announced in January 2015 at the event recorded in the [SpaceX Seattle announcement][ref_spacex_seattle_announcement_2015], and the announcement coincided with the financing round the [Patient-Private Capital-Formation Leg article A290][related_post_a290_spacex_patient_private_leg] treats. The coincidence is not incidental. The round supplied capital against a business line that did not yet exist, and the announcement supplied the business line against which the capital was raised.

The stated rationale at announcement was that the revenue required to fund the mission the [series opener][related_post_a281_spacex_framing] describes exceeded any plausible revenue from launch services alone. The claim is checkable in order of magnitude. The global commercial launch market at the time supported a total addressable revenue substantially below the programme cost of a Mars transportation system, whereas the global telecommunications market exceeded it by orders of magnitude. The comparison can be stated as

$$\text{TAM}^{\text{launch}} \ll B^{\text{mission}} \ll \text{TAM}^{\text{telecom}}$$

with the middle quantity being the mission burn the spinoff was intended to fund. The reasoning does not establish that the venture could capture any particular share of the larger market, and the article marks the distinction between the size of a market and the accessibility of it. The share the argument actually requires has the form

$$\sigma^{\text{required}} = \frac{B^{\text{mission}}}{\text{TAM}^{\text{telecom}} \cdot \mu}$$

with $\mu$ the achievable margin. The quantity is small, which is what makes the argument survivable, and it is not zero, which is what makes it an argument rather than an assertion. The mission against which the burn is defined is documented in the architecture statements at the [2017 International Astronautical Congress presentation][ref_musk_iac_2017], the [SpaceX Starship programme][ref_spacex_starship_program], and the agency reference architectures at the [NASA Mars programme][ref_nasa_mars_program], the [NASA Mars science record][ref_nasa_science_mars], and the [Design Reference Architecture 5.0][ref_nasa_dra_5_0]. The article's position is that a rationale of this form is checkable only in order of magnitude and that it was treated at the time as more precise than it was.

The capacity argument is the second and less frequently stated rationale, and the article regards it as the stronger of the two. By 2015 the vehicle programme the [Value Gradient article A282][related_post_a282_spacex_value_gradient] traces had produced a launch capability whose production and operations infrastructure was sized above the external demand available to it. A constellation is the application that consumes launch capacity in the largest quantity available anywhere, and it was the application most naturally matched to the surplus the firm held. The matching condition may be stated compactly

$$\arg\max_{a \in \mathcal{A}} \; \left[ \text{capacity consumed by application } a \right] \quad \text{subject to} \quad \text{capability already held}$$

with the constellation the maximizer over the application set the firm could reach. The formulation makes the decision look less like market entry and more like an allocation problem, which is the reading the article adopts.

## The Deployment Sequence from 2019 to 2021

The first operational batch reached orbit in May 2019 as recorded in the [first operational batch release][ref_spacex_press_starlink_v0_9_2019], following the two prototype spacecraft of 2018 recorded in the [prototype release][ref_spacex_press_tintin_2018]. Service beta began in 2020 as recorded in the [service beta release][ref_spacex_press_beta_2020], and commercial availability broadened through 2021. The consolidated programme record is at [Starlink][ref_spacex_starlink] and the technical description at the [Starlink technology page][ref_starlink_technology].

The deployment exhibits the step-function property the network-effects framing predicts. A constellation in low Earth orbit contributes continuous service to a given latitude band only once enough orbital planes are populated to guarantee that a satellite is always in view. Below that threshold the service is intermittent and substantially unsellable. The coverage condition may be written

$$\text{continuous service at latitude } \lambda \iff n^{\text{planes}}(\lambda) \geq n^{\text{minimum}}(\lambda)$$

with the revenue from a partially deployed constellation being not a proportional fraction of the complete one but approximately zero until the threshold is crossed. The revenue relation is therefore a step rather than a ramp, admitting the compact form

$$R(S) = \begin{cases} \approx 0 & S < S^{\ast} \\ R^{\text{full}} \cdot \left( S / S^{\ast} \right)^{\gamma} & S \geq S^{\ast} \end{cases}$$

with $\gamma$ governing how capacity growth beyond the coverage threshold converts into further revenue. The property is the structural reason a constellation cannot be built incrementally against revenue and must be financed ahead of any income whatever, which is what connects this article to the two preceding capital-formation legs.

The threshold property also explains the deployment sequence's geographic order. A satellite in a circular orbit at inclination $i$ spends time over latitudes in proportion to the geometry, and the dwell density peaks near the turning latitudes, admitting the approximate relation

$$\text{coverage density}(\lambda) \; \propto \; \frac{1}{\sqrt{\sin^2 i - \sin^2 \lambda}} \qquad \text{for} \qquad |\lambda| < i$$

with the density rising toward $|\lambda| \to i$ and vanishing beyond it. Coverage was therefore established first at the latitudes the inclination favored and extended subsequently, so that revenue began at high northern latitudes where terrestrial broadband was poorest and the competing alternatives weakest. The commercial sequence follows from orbital geometry rather than from a market-selection decision.

## Vertical Integration and the Internal Transfer Price

The internal transfer price is the quantity on which every financial claim about the spinoff depends, and it is unobservable.

The parent supplies launch services to the spinoff and the spinoff provides revenue to the consolidated entity. The price at which the internal transaction is recorded determines how the consolidated profit is attributed between the two, and it determines nothing about the consolidated profit itself. The identity admits the compact form

$$\Pi^{\text{consolidated}} = \Pi^{\text{launch}}\!\left( p^{\text{transfer}} \right) + \Pi^{\text{constellation}}\!\left( p^{\text{transfer}} \right) \qquad \text{with} \qquad \frac{\partial \Pi^{\text{consolidated}}}{\partial p^{\text{transfer}}} = 0$$

with the transfer price redistributing profit between the segments and leaving the total unchanged. The redistribution is exact and is stated compactly as

$$\frac{\partial \Pi^{\text{launch}}}{\partial p^{\text{transfer}}} = q^{\text{internal}} = - \frac{\partial \Pi^{\text{constellation}}}{\partial p^{\text{transfer}}}$$

with the two derivatives equal in magnitude and opposite in sign. The consequence is that any externally reported claim about the profitability of either segment separately is a claim about an accounting choice rather than about an economic fact, and the article declines to make such claims. The point is not peculiar to this firm. Segment reporting for a listed issuer operates under the management-approach standard at [Financial Accounting Standards Board Topic 280][ref_fasb_asc280] and the disclosure regime at [Regulation S-K][ref_sec_regulation_sk], under which reported segments follow the internal reporting structure rather than any economically defined boundary. A private firm publishes nothing at all, so the ambiguity that a listed issuer at least discloses the basis for is here entirely unresolved.

The observation has a sharper implication for the competitive analysis. A competitor evaluating entry compares its own launch cost against the price it observes the parent charging external customers. That price is not the cost the spinoff bears. The competitor's inference error takes the form

$$\hat{c}^{\text{parent}}_{\text{competitor}} = p^{\text{market}} \; > \; c^{\text{marginal}} = c^{\text{parent}}_{\text{actual}}$$

with the observable price exceeding the unobservable cost by the full margin. The competitor therefore systematically overestimates the parent's constellation cost, which means an entry decision that looks marginal on the competitor's information may be clearly unprofitable on the parent's. The [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] identifies the same transfer price as the single most consequential unobserved quantity from the portfolio side. The two articles converge on the same missing number from different directions.

The vertical structure also creates the conflict the competition-policy tradition identifies. The parent sells launch services to firms that compete with its own constellation, and the capacity it allocates internally is capacity unavailable to them. The allocation operates under a binding constraint admitting the compact form

$$q^{\text{internal}} + q^{\text{external}} \leq \bar{q} \qquad \text{with} \qquad \bar{q} \; \text{finite at any date}$$

with every internal launch displacing an external one whenever the constraint binds. The arrangement is documented in the general [SpaceX corporate record][ref_spacex_company] and no public allocation rule exists, which means the question of whether the constraint has bound and how it was resolved is unanswerable from outside the firm. The corporate-law instruments through which such a conflict would ordinarily be tested are the fiduciary provisions of the [Delaware General Corporation Law][ref_dgcl] as interpreted by the [Delaware Court of Chancery][ref_delaware_chancery], or the equivalent provisions of the [Texas Business Organizations Code][ref_texas_boc] following the reincorporation the [Governance article A287][related_post_a287_spacex_governance] treats. A launch customer harmed by an allocation decision is a counterparty rather than a shareholder, so none of those instruments is available to it, and the [Securities and Exchange Commission investor education service][ref_sec_investor_gov] describes a disclosure regime that does not apply.

## The Launch-Cadence Coupling

The constellation and the launch business are coupled through cadence in a manner that is mutually reinforcing and that the article treats as the mechanical core of the case.

A constellation of $S$ satellites deployed in batches of $b$ per launch requires

$$N^{\text{launches}} = \left\lceil \frac{S}{b} \right\rceil$$

launches for initial deployment, and a satellite operational lifetime of $L$ years imposes a steady-state replenishment requirement of

$$\dot{N}^{\text{replenish}} = \frac{S}{b \cdot L}$$

launches per year thereafter. For a constellation of several thousand satellites at a lifetime of roughly five years, the replenishment requirement alone exceeds the entire global commercial launch cadence of the period preceding the programme, admitting the compact comparison

$$\dot{N}^{\text{replenish}} \; > \; \dot{N}^{\text{global commercial, pre-programme}}$$

with the steady-state obligation of a single constellation exceeding what the entire world launch industry had previously demonstrated. The comparison establishes that the capability had to be created rather than procured and is the quantitative form of the supply-unavailability condition the vertical-integration framing states. The vehicle set through which the cadence was delivered is documented at the [Falcon 9 vehicle page][ref_spacex_falcon9_vehicle], the [Falcon Heavy vehicle page][ref_spacex_falcon_heavy_vehicle] and its [first flight record][ref_spacex_press_falcon_heavy_2018], and the [Starship programme page][ref_spacex_starship_program], with the site environmental approvals at the [Starship programmatic environmental assessment][ref_faa_starship_pea]. Systems-engineering practice for programmes of this class is documented in the [NASA programme management requirements][ref_nasa_npr_7120_5f] and the [International Council on Systems Engineering handbook][ref_incose_handbook], and the technical literature appears in the [Journal of Spacecraft and Rockets][ref_aiaa_jsr] and the [Journal of Propulsion and Power][ref_aiaa_jpp].

The coupling runs in both directions and that is what makes it consequential. The constellation offers the launch business with a demand stream large enough to justify the cadence, and the cadence drives the reuse experience that the [Decomposability article A285][related_post_a285_spacex_decomposability] and the [Value Gradient article A282][related_post_a282_spacex_value_gradient] identify as the source of cost reduction. The learning relationship admits the conventional form

$$c_n = c_1 \cdot n^{-\beta}$$

with $c_n$ the cost at cumulative flight $n$ and $\beta$ the learning exponent. The constellation increases $n$ faster than external demand could, which lowers $c_n$, which lowers the constellation's own cost, which improves the economics that justify further deployment. The loop admits statement as a fixed point in the deployment rate

$$\dot{N}^{\ast} = \Psi\!\left( c\big( \dot{N}^{\ast} \big) \right) \qquad \text{with} \qquad \Psi' < 0 \;\; \text{and} \;\; c' < 0$$

with the composition increasing, so that the system admits a self-reinforcing equilibrium at high cadence and low cost rather than converging to the industry's prior operating point. The structure is the mechanical core of the case and it is what the ordinary account of a launch company entering telecommunications entirely omits. The reuse record is at the [Falcon 9 vehicle page][ref_spacex_falcon9_vehicle] and the milestone sequence at the [first booster landing][ref_spacex_press_falcon9_first_landing_2015], the [first reflight][ref_spacex_press_ses10_2017], and the [Block 5 introduction][ref_spacex_press_block5_bangabandhu_2018].

The self-reinforcing structure is the strongest available argument that the spinoff was not a diversification. A diversification consumes the parent's resources. This arrangement improved the parent's core economics as a direct consequence of consuming its output.

## Service Rollout and the Subscriber Trajectory

The subscriber trajectory is reconstructed from company statements and trade-press reporting at [SpaceNews][ref_spacenews], [Ars Technica space coverage][ref_arstechnica_space], [Payload][ref_payload], [Payload Research][ref_payload_research], and [The Space Review][ref_the_space_review], and every figure carries the reconstruction caveat the Data Sources section states.

The reported trajectory rises from the beta of 2020 through successive announced milestones across the 2021 to 2025 period into the millions of subscribers, with the service available across a majority of national markets by the drafting date. The revenue relation can be written as

$$R^{\text{consumer}}(t) = n^{\text{sub}}(t) \cdot \text{ARPU} + R^{\text{hardware}}(t)$$

with the hardware term historically negative or near zero, because terminals were supplied below manufacturing cost as a subscriber-acquisition expense. The negative hardware margin is a conventional subscription-business structure and is the reason early revenue figures understate the eventual contribution.

The segment composition matters more than the aggregate. Consumer broadband carries the lowest revenue per unit of capacity, while maritime, aviation, enterprise, and government services carry substantially higher figures for the same bandwidth. The blended figure admits the form

$$\text{ARPU}^{\text{blended}} = \sum_j w_j \cdot \text{ARPU}_j \qquad \text{with} \qquad \frac{d}{dt} w^{\text{high-value}} > 0$$

with the mix shifting toward the higher-value segments across the period. The shift is not merely a revenue preference but a capacity-allocation necessity, because a satellite's bandwidth over a given cell is finite and admits the compact constraint

$$\sum_{j} n_j \cdot b_j \; \leq \; B^{\text{cell}}$$

with $b_j$ the bandwidth a subscriber of class $j$ consumes. A consumer subscriber in a congested cell therefore displaces capacity that a maritime or enterprise subscriber would pay several times more to obtain, which means the mix shift is what a capacity-constrained operator does under any reasonable pricing rule. The defense line the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] treats and the [Starshield record][ref_spacex_starshield] documents is the extreme case of the same shift.

## Direct-to-Cell and the Carrier Partnerships

The direct-to-cell extension is analytically distinct from the broadband service and the article treats it separately.

The service was announced through a carrier partnership in 2022 and developed through subsequent carrier agreements and regulatory authorizations, with the service description at [Starlink direct-to-cell][ref_starlink_direct_to_cell] and the authorization record at the [Federal Communications Commission direct-to-cell proceeding][ref_fcc_direct_to_cell_2024].

The arrangement differs from the broadband business in three respects the article regards as material. The first is that it uses terrestrial mobile spectrum licensed to the carrier rather than spectrum licensed to the satellite operator, which makes the carrier relationship a legal necessity rather than a distribution convenience. The second is that it requires no customer equipment whatever, which removes the terminal cost that constrains broadband subscriber acquisition. The third is that it is genuinely two-sided in the sense the platform tradition describes, because the value to a carrier rises with coverage and the value to a subscriber rises with carrier participation.

The spectrum arrangement admits the compact statement

$$\text{service} = f\!\left( \text{satellite capability}, \; \text{carrier spectrum rights} \right)$$

with neither input substitutable for the other. The consequence is that the direct-to-cell business is the one part of the spinoff in which the venture does not hold the complementary asset, and the appropriability tradition predicts that value will be divided by relative bargaining power rather than captured. The division admits the compact bargaining form

$$\sigma^{\text{operator}} = \sigma\!\left( u^{\text{operator}}, \; u^{\text{carrier}} \right) \qquad \text{with} \qquad u^{\text{carrier}} \; \text{rising in the number of competing operators}$$

with the carrier's disagreement payoff improving as alternative satellite partners appear. The operator's share is therefore highest while it is the only viable partner and falls as the category develops, which is the reverse of the trajectory the broadband business exhibits. The article regards this as the most significant structural qualification to the category-dominance claim.

The offsetting advantage is that the addressable population is not limited by terminal ownership, admitting the compact contrast

$$M^{\text{direct-to-cell}} = n^{\text{handsets in coverage}} \qquad \text{against} \qquad M^{\text{broadband}} = n^{\text{terminals sold}}$$

with the first quantity larger than the second by several orders of magnitude and requiring no subscriber-acquisition hardware subsidy. The two effects run in opposite directions and the article does not claim to know which dominates.

## The Revenue Trajectory and the Mission-Funding Crossover

The revenue trajectory is the quantity the capital-formation argument requires and it is the least well documented quantity in the article.

Reported figures across the 2020 through drafting-date period rise from negligible to a scale exceeding the launch business, with the sector analyses at [Space Capital][ref_space_capital], [BryceTech][ref_bryce_tech], and [Payload Research][ref_payload_research] supplying the reconstructions and the business press at [Bloomberg][ref_bloomberg], the [New York Times][ref_nyt], and the [Wall Street Journal][ref_wsj] supplying the reported company statements.

The crossover condition the economic-property section states requires comparing revenue against mission burn, and neither quantity is published. The article's position is therefore explicitly conditional. If the reported revenue figures are approximately correct and if the mission burn is of the order the programme's public scale suggests, then the crossover falls somewhere in the middle of the decade and the capital-formation problem is substantially closed. The crossover date is the solution of an equation neither of whose sides is published, admitting the compact form

$$t^{\ast} = \inf \left\{ t \; : \; R^{\text{free}}(t) \geq B(t) \right\}$$

with the infimum taken over dates at which the condition first holds and continues to hold. The article states the conditional rather than asserting the conclusion, and the Load-Bearing Open Questions section records the crossover date as the series' principal unresolved empirical question.

The distinction between revenue and free cash contribution deserves emphasis, because the replenishment obligation the next section describes consumes a substantial and continuing fraction of gross revenue. The relevant quantity is

$$R^{\text{free}}(t) = R^{\text{gross}}(t) - C^{\text{operating}}(t) - C^{\text{replenishment}}(t)$$

with the third term structural rather than discretionary. The distinction from a business whose marginal cost is near zero admits the compact contrast

$$\frac{\partial C^{\text{replenishment}}}{\partial S} > 0 \qquad \text{against} \qquad \frac{\partial C^{\text{marginal}}}{\partial n^{\text{user}}} \approx 0$$

with the first structure obliging continuing capital expenditure proportional to the deployed asset base and the second not. A constellation business cannot reduce replenishment spending without shrinking, which distinguishes it from a software business at comparable revenue and which the commentary comparing the two routinely omits.

## Capital Intensity and the Replenishment Treadmill

The constellation imposes a permanent capital obligation that has no analogue in the launch business, and the article treats it as the principal structural liability of the spinoff.

Satellites in low Earth orbit experience atmospheric drag and deorbit within a period substantially shorter than conventional geostationary spacecraft lifetimes. The design choice is deliberate and is what the orbital-debris regime the regulatory section describes effectively requires, but it converts the constellation from a capital asset into a consumable. The steady-state obligation has the form

$$C^{\text{replenishment}} = \frac{S}{L} \cdot \left( c^{\text{satellite}} + \frac{c^{\text{launch}}}{b} \right)$$

with the whole quantity recurring annually and indefinitely. The design choice is not purely commercial. The mitigation regime documented at the [NASA Orbital Debris Program Office][ref_nasa_orbital_debris], the [standard practices][ref_nasa_orbital_debris_mitigation], and the [Inter-Agency Space Debris Coordination Committee guidelines][ref_iadc_guidelines] establishes post-mission disposal expectations that a low-orbit constellation satisfies most cheaply by operating at an altitude where drag performs the disposal without a dedicated manoeuvre. The regulatory obligation and the short lifetime are therefore the same design decision viewed from two directions, and the financial burden this section describes is in part the cost of compliance.

The obligation is the reason satellite production rate rather than launch rate became the binding constraint on the programme, admitting the compact statement

$$\dot{S}^{\text{production required}} = \frac{S}{L} \qquad \text{with} \qquad \dot{S}^{\text{production}} < b \cdot \dot{N}^{\text{launch capacity}}$$

with the production term the smaller of the two and therefore governing. The relation is the reason the venture built satellite manufacturing at a scale without precedent in the sector, and it inverts the sector's historical constraint, in which launch availability governed and spacecraft were produced individually.

The manufacturing achievement deserves statement in its own terms. Producing spacecraft at a rate measured in units per day rather than units per year is a discontinuity in the industry's production practice, and it follows the same learning relationship the launch business exhibits. The steady state the treadmill implies also fixes the fleet's average age, admitting the compact result

$$\bar{a} = \frac{L}{2} \qquad \text{in steady state with uniform replacement}$$

with the deployed constellation permanently averaging half a design lifetime. The property is favorable and is rarely stated, because it means the operational fleet is continuously refreshed with current-generation hardware rather than ageing toward obsolescence as a conventional geostationary fleet does. The [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats the design commonality that makes the rate attainable.

The treadmill also gives the strongest argument against the natural-monopoly reading of the position. An incumbent whose asset base must be entirely replaced every few years cannot rest on it, and a competitor entering later deploys a newer generation against an incumbent carrying a partially obsolete fleet. The advantage can be stated as

$$\text{incumbency advantage} \; \sim \; \frac{L}{T^{\text{competitor deployment}}}$$

with the advantage small where the replacement interval is short relative to the time a competitor requires to deploy. The article regards this as a genuine limit on the durability of the position and as the feature most likely to be underweighted by both advocates and critics.

## The Regulatory Position Across the Commission the Union and National Regulators

The regulatory position is the second structural constraint and it operates on a resource the venture cannot manufacture.

The domestic authorization record comprises the [initial authorization][ref_fcc_starlink_2018], the [second-generation authorization][ref_fcc_starlink_gen2_2022], the [direct-to-cell proceeding][ref_fcc_direct_to_cell_2024], and the general [filing system][ref_fcc_filings]. The international coordination operates through the [International Telecommunication Union Radio Regulations][ref_itu_radio_regulations_2020], under which spectrum and orbital-slot rights are coordinated among administrations rather than allocated by any single authority. Launch licensing runs through the [Federal Aviation Administration Office of Commercial Space Transportation][ref_faa_ast] under the [Commercial Space Launch Act][ref_csla_1984], its [amendments][ref_csla_amendments_2004], the [current provisions][ref_uscsla_2015], the [Part 450 licensing rule][ref_faa_ast_licensing_regs_450], the general [licensing regulations][ref_faa_ast_regulations], and the [financial responsibility and indemnification regime][ref_faa_financial_responsibility]. The agency's own authorities derive from [Title 51 Section 20113][ref_51_usc_20113], and export control over the spacecraft themselves operates through the [International Traffic in Arms Regulations][ref_itar_22_cfr_120_130], which is the reason a constellation operator's manufacturing footprint is less internationally distributable than its market. The treaty framework comprises the [Outer Space Treaty][ref_un_outer_space_treaty_1967], the [Liability Convention][ref_un_liability_convention_1972], and the [Registration Convention][ref_un_registration_convention_1976], under which the launching state bears international responsibility for national activities.

Service in any national market requires that market's own authorization, which makes the regulatory position a per-country matter rather than a single approval. The addressable market may be written

$$M^{\text{addressable}}(t) = \sum_{k \in \mathcal{J}(t)} M_k \qquad \text{with} \qquad \mathcal{J}(t) = \left\{ k : \text{authorization granted in jurisdiction } k \right\}$$

with the index set growing by administrative decision rather than by commercial effort. The consequence is that the addressable market is not the world but the union of jurisdictions that have granted access, and the difference is substantial and politically contingent.

The structure also creates a distinct category of risk that the sector's financial commentary treats poorly. An authorization is revocable, and the revenue attaching to a jurisdiction is therefore conditional, admitting the compact statement

$$\mathbb{E}\left[ R_k \right] = R_k \cdot P\!\left( \text{authorization retained} \right)$$

with the second factor a political rather than an operational quantity. The article notes that the largest single risk to the revenue base described here may be diplomatic rather than technical or competitive.

## Spectrum Priority as the Scarce Asset

The scarce asset in the constellation business is not orbital volume and is not capital. It is spectrum priority.

The coordination regime the [Radio Regulations][ref_itu_radio_regulations_2020] establishes operates on a first-filed basis subject to bring-into-use deadlines, so that an operator filing earlier and deploying on schedule obtains a protected position against later entrants, who must demonstrate non-interference with the incumbent. The priority relation may be stated compactly

$$\text{priority}_i > \text{priority}_j \iff t^{\text{filing}}_i < t^{\text{filing}}_j \; \wedge \; \text{bring-into-use satisfied}$$

with the second conjunct being the reason deployment speed carries a regulatory value independent of its commercial value. A constellation deployed quickly converts a filing into a protected right, and a constellation deployed slowly forfeits it.

The deadline imposes a rate requirement rather than a quantity requirement, admitting the compact condition

$$\dot{S}^{\text{deployed}} \; \geq \; \frac{S^{\text{filed}}}{T^{\text{bring-into-use}} - t^{\text{start}}}$$

with failure to satisfy it forfeiting the filed position in whole or in part. The domestic implementation of the milestone regime appears in the [initial authorization][ref_fcc_starlink_2018] and the [second-generation authorization][ref_fcc_starlink_gen2_2022], and the statutory basis for the licensing of the launches required to satisfy it runs through the [Commercial Space Launch Act][ref_csla_1984], its [subsequent amendments][ref_csla_amendments_2004], the [current commercial space launch provisions][ref_uscsla_2015], and the [Part 450 licensing rule][ref_faa_ast_licensing_regs_450]. A venture holding captive launch capacity controls the numerator's feasibility directly. A venture buying launch at market controls neither the rate nor the schedule, because its supplier allocates capacity across a manifest the venture does not set.

The observation reframes the launch-cadence coupling. The cadence was not merely an economic advantage. It was the mechanism by which a regulatory option was exercised before it expired, and the option's value is stated compactly as

$$W^{\text{filing}} = \mathbf{1}\left[ \text{bring-into-use satisfied} \right] \cdot V^{\text{protected position}}$$

with the value collapsing to zero on failure rather than degrading gracefully. The article regards this as the single most underappreciated element of the case and as the point at which the capital-formation story and the regulatory story become the same story.

## Orbital Shells and the Congestion Externality

The constellation imposes costs on other operators and on future entrants that it does not bear, and the article states the externality plainly rather than treating it as a critics' talking point.

The debris and conjunction regime is documented at the [NASA Orbital Debris Program Office][ref_nasa_orbital_debris], the [orbital debris mitigation standard practices][ref_nasa_orbital_debris_mitigation], and the [Inter-Agency Space Debris Coordination Committee guidelines][ref_iadc_guidelines], with the economic treatments at [Adilov Alexander and Cunningham 2014][research_adilov_et_al_2014] and [Weeden and Chow 2012][research_weeden_chow_2012]. The externality admits the compact statement

$$\frac{\partial \, \text{collision risk}_j}{\partial \, S_i} > 0 \qquad \text{with the cost borne by } j \neq i$$

with each operator's deployment raising every other operator's risk and no mechanism pricing the increment. The conjunction rate between resident objects scales approximately with the square of the population in a shell, admitting the compact relation

$$\dot{n}^{\text{conjunction}} \; \propto \; \frac{S_{\text{shell}}^{2}}{V_{\text{shell}}}$$

with the quadratic term the reason an increment to an already-populated shell is more costly than the same increment to an empty one. The divergence between the private and social optimum follows directly

$$S^{\text{private}} : \; \frac{\partial \Pi_i}{\partial S_i} = 0 \qquad \text{against} \qquad S^{\text{social}} : \; \frac{\partial}{\partial S_i}\left[ \Pi_i + \sum_{j \neq i} \Pi_j \right] = 0$$

with the private optimum exceeding the social one by the uninternalized external term. The structure is a standard common-pool problem and the literature the regulated-industry tradition gives predicts under-provision of mitigation absent an allocation regime. The instruments that exist are liability and insurance rather than allocation. International responsibility runs through the [Liability Convention][ref_un_liability_convention_1972], domestic financial responsibility through the [Federal Aviation Administration indemnification regime][ref_faa_financial_responsibility], and the commercial risk-transfer market through the underwriters documented at [Aon space insurance][ref_aon_space_insurance] and the [Lloyd's market][ref_lloyds_market]. The article notes that none of these instruments prices the marginal congestion an additional satellite imposes, because each responds to a realized loss rather than to an increment in risk, so the externality survives the existence of an active insurance market.

The article notes in fairness that the short design lifetime and active deorbit capability the constellation employs are substantially better mitigation practice than the geostationary and medium-orbit precedents exhibited, and that the aggregate risk nonetheless rises because the object count rises faster than the per-object risk falls. Both statements are true and the commentary generally asserts only one of them.

## The Iridium and Globalstar Precedents

The two 1990s constellation programmes supply the precedents in which the same business was attempted without a captive launch capability, and the [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] and the [Patient-Private Capital-Formation Leg article A290][related_post_a290_spacex_patient_private_leg] treat the capital-structure dimension of the first.

The relevant contrast for this article is the cost position rather than the financing. Both programmes purchased launch at market prices from external providers, and both therefore incurred the full disadvantage the economic-property section states, on a campaign requiring dozens of launches. The disadvantage they bore admits the compact application of the economic-property result

$$\Delta C^{\text{1990s programmes}} = N \cdot m \qquad \text{with} \qquad N \sim 10^{1} \; \text{to} \; 10^{2}$$

with the full external margin incurred across every launch of the deployment. The record is at the [Iridium corporate archive][ref_iridium_press_archive_1998], the [Chapter 11 filing][ref_iridium_chapter_11_1999] lodged with the [Securities and Exchange Commission EDGAR][ref_sec_edgar] system, and the case treatments at [Finkelstein and Sanford 2000][research_finkelstein_sanford_2000] and [Zimmerman 2011][research_zimmerman_2011].

The second and less frequently noted contrast concerns the market rather than the cost. Both programmes targeted voice telephony against a terrestrial cellular buildout that expanded faster than either anticipated, so that the addressable market contracted during deployment. The failure mode admits the compact statement as a race between deployment and market erosion

$$\frac{d M^{\text{addressable}}}{dt} < 0 \qquad \text{while} \qquad S < S^{\ast}$$

with the market contracting during the very interval in which the threshold property guarantees no revenue. The combination is close to unsurvivable and it is the sharper reading of those failures than the capital-structure account alone yields. The present case targeted broadband against a terrestrial buildout whose rural economics have not improved comparably, and the article marks this as a favorable contingency rather than as a strategic insight, because nothing in the 2015 decision demonstrates foresight about terrestrial deployment economics.

## The OneWeb and Kuiper Comparisons

The two contemporary competitors supply the cleanest available test of the article's central claim, because both attempted the same business in the same period under different vertical arrangements.

OneWeb purchased launch services externally and its trajectory is documented at the [OneWeb corporate record][ref_oneweb] and the [Eutelsat corporate record][ref_eutelsat_oneweb], with the insolvency administered through the [United States bankruptcy court system][ref_uscourts_bankruptcy] under the [Chapter 11][ref_bankruptcy_code_ch11] provisions. The programme faced the full external launch cost, faced a deployment deadline set by its own spectrum filings, and depended on a capital supplier whose withdrawal proved terminal. The three failures were not independent, admitting the compact statement

$$\left[ \text{no captive launch} \right] \Rightarrow \left[ \text{deadline uncontrolled} \right] \Rightarrow \left[ \text{capital requirement uncertain} \right] \Rightarrow \left[ \text{supplier withdrawal} \right]$$

with each condition raising the probability of the next. The [Patient-Private Capital-Formation Leg article A290][related_post_a290_spacex_patient_private_leg] treats the same case as a financing failure and this article treats it as a supply failure, and the two readings are compatible because the supply position is what made the financing requirement unbounded.

The Amazon programme contributes the comparison the article regards as most informative, because the sponsor's capital position removes the financing constraint entirely and isolates the launch-supply variable. A programme financed from a balance sheet of that scale cannot fail for want of capital, so its outcome tests the launch-supply proposition specifically. The programme has contracted launch capacity from multiple providers including, notably, the parent firm this article treats, and the sector record is at [SpaceNews][ref_spacenews], [Ars Technica space coverage][ref_arstechnica_space], and [Space Policy Online][ref_space_policy_online].

The comparison admits the compact statement as a controlled contrast

$$\left\{ \text{capital} \right\} \; \text{held approximately constant}, \qquad \left\{ \text{captive launch} \right\} \; \text{varied}$$

with the outcome difference attributable to the varied factor to the extent the other factors are genuinely comparable. The design is the closest the sector offers to holding the financing constraint fixed, admitting the compact statement

$$\left. \frac{\partial \, \text{outcome}}{\partial \, \text{captive launch}} \right|_{\text{capital held high}}$$

as the estimand the comparison identifies. The article marks the limits of the inference. The programmes began at different dates, hold different spectrum priorities, and pursue partially different market segments, so the contrast is suggestive rather than clean.

## The Constraint the Spinoff Installs

The mapping-problem section states that the spinoff leg terminates the capital-formation problem rather than managing it, on the ground that retained earnings carry neither a milestone requirement nor a dilution. That statement is too strong, and correcting it is the most consequential revision this review makes.

Retained earnings carry no financial claim. They carry an operational one, and the operational claim is not smaller than the financial claim it replaced. A subscriber base is a continuing service obligation. A carrier partnership is a contractual obligation with a counterparty holding an asset the venture does not own. A national authorization is a political obligation to a regulator with the power to withdraw it. None of these parties supplied capital and none holds equity, so none of them appears anywhere in the capital-formation accounting the series has developed across the three legs.

The correct statement of the leg's contribution nets the spinoff's own claims against its gross generation, admitting the compact form

$$R^{\text{available to mission}} = R^{\text{gross}} - C^{\text{operating}} - C^{\text{replenishment}} - C^{\text{regulatory and service obligations}}$$

with the final term rising in the size of the subscriber base and the number of jurisdictions served. The term is not merely financial. It consumes decision capacity at the level of the firm, which is the resource the [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] identifies as binding before capital does, drawing on the managerial-services limit that [Penrose 1959][book_penrose_1959] states and that [March and Simon 1958][book_march_simon_1958], [Cyert and March 1963][book_cyert_march_1963], and [Simon 1957][book_simon_1957] develop.

The consequence is that the leg's net contribution need not be monotone in the spinoff's scale. There exists in principle a scale beyond which the marginal subscriber consumes more mission-relevant capacity than the marginal revenue funds, admitting the compact stationarity condition

$$\frac{\partial R^{\text{available to mission}}}{\partial n^{\text{sub}}} = 0 \qquad \text{at some} \qquad n^{\text{sub}} = n^{\dagger}$$

with the article unable to say whether $n^{\dagger}$ has been passed, or whether it lies far beyond any attainable scale, because both the mission burn and the obligation cost are unpublished. The article states the possibility because the ordinary account treats the relationship as monotone by assumption and never examines it.

The sharper point concerns governance rather than arithmetic. The [Governance article A287][related_post_a287_spacex_governance] establishes a control configuration designed to resist capital capture, in which an investor seeking to redirect the firm must assemble votes it cannot obtain. That defence is exact against the party it was designed against and is entirely absent against the parties this section identifies. The asymmetry can be stated as

$$\text{defence} = f\!\left( \text{votes required} \right) \qquad \text{but} \qquad \frac{\partial \, \text{leverage}^{\text{regulator, carrier, subscriber}}}{\partial \, \text{votes held}} = 0$$

with the leverage of these parties independent of any equity position. A telecommunications regulator withdrawing an authorization, a carrier declining to renew a spectrum arrangement, or a subscriber base migrating to a competitor each constrains the firm without holding a single share. The dual-class structure the series treats as the mechanism protecting the mission from capital is therefore no protection whatever against the constituencies the third leg creates.

The observation completes a pattern the series has now encountered three times, and the article states it as a pattern rather than as a third isolated finding. The [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] found that a portfolio which appears to distribute risk concentrates it on a shared vehicle family. The [Patient-Private Capital-Formation Leg article A290][related_post_a290_spacex_patient_private_leg] found that sub-properties which appear to fail independently fail together under adverse states. The present article finds that a leg which appears to remove a constraint substitutes a different one. In all three cases the framework's own decomposition understates the coupling between the conditions it separates, and the coupling becomes visible only under conditions the observed history does not contain. The closing article A292 should treat this as a general property of the seven-plus-three framework rather than as three coincidences.

The evidentiary position of this section is weak in the same way the A290 adverse-state treatment is weak. No instance is observable in which a regulatory or service obligation visibly constrained a mission-directed decision at this firm. The section reasons from the structure of the obligations rather than from any observed event, and its claims are conditional predictions. The article notes that the direct-to-cell arrangement and the per-jurisdiction authorization structure are the two channels through which such a constraint would first become visible, and that both are recent enough that an absence of observed constraint carries little information.

## Deep Historical Comparative Precedents

The category-dominating spinoff mechanic admits comparison with historical precedents in which a firm built a business on top of a capability developed for another purpose.

The Standard Oil consolidation supplies the precedent for retained-earnings financing displacing external capital markets entirely, documented in [Chernow 2004][book_chernow_2004] Titan and [Nevins 1954][book_nevins_1954], with the primary record at the [Supreme Court decision of 1911][ref_standard_oil_1911]. The relevant parallel is the vertical control of transport, because the firm's position rested substantially on rail and pipeline arrangements that competitors could not obtain on comparable terms. The structural identity with the present case may be stated compactly

$$c^{\text{integrated}}_{\text{transport}} = c^{\text{marginal}} \qquad \text{against} \qquad c^{\text{rival}}_{\text{transport}} = p^{\text{posted}} - r$$

with $r$ the rebate a rival could not obtain, which is the same relation this article states with launch substituted for rail. The article notes that the historical case resolved through dissolution rather than through competitive erosion, which is the base rate the competition-policy tradition applies.

The Bell System supplies the precedent for a communications infrastructure attaining a dominant position and the regulatory settlement that followed, documented in [Temin and Galambos 1987][book_temin_galambos_1987], [Wu 2010][book_wu_2010], [Levin 2010][book_levin_2010], and [Sobel 1995][book_sobel_1995], with the primary record at the [consent decree of 1956][ref_att_consent_decree_1956] and the [divestiture of 1984][ref_att_divestiture_1984]. The case yields the base rate that the telecommunications-history tradition applies, and the article's reading is that the settlement terms in both instances turned on the treatment of the vertical relationship rather than on market share as such. The regulated bargain is stated compactly as

$$\Pi^{\text{permitted}} = \bar{r} \cdot K^{\text{rate base}} \qquad \text{subject to} \qquad \text{universal-service obligation}$$

with a permitted return on invested capital exchanged for a coverage obligation. The form is one of the available outcomes for the present case and the article notes that a firm whose asset base must be continuously replaced would find a rate-base regime unusually favorable, since the rate base would never depreciate away.

The electrification build-outs supply the precedent for a capital-intensive network whose value depends on coverage completeness, documented in [Hughes 1983][book_hughes_1983] and [Nye 1990][book_nye_1990]. The threshold property the deployment section describes is the same property those systems exhibited, admitting the compact statement of the coverage economics

$$\frac{C^{\text{network}}}{n^{\text{user}}} \; \text{decreasing in} \; n^{\text{user}} \qquad \text{with} \qquad C^{\text{network}} \; \text{largely independent of} \; n^{\text{user}}$$

with the fixed coverage cost incurred before any user is served. The historical resolution was a regulated monopoly with a universal-service obligation, which is one of the available outcomes for the present case.

The railroad and canal financings supply the precedent for infrastructure whose construction period exceeded its financiers' horizon, documented in [Chandler 1977][book_chandler_1977] The Visible Hand and [Chandler 1990][book_chandler_1990] Scale and Scope, with the general treatments at [Landes 1969][book_landes_1969], [North 1990][book_north_1990], and [Perez 2002][book_perez_2002] Technological Revolutions and Financial Capital. The [Perez 2002][book_perez_2002] periodization is the most directly applicable, because it treats the availability of capital for a technology class as a function of the installation and deployment cycle rather than as a constant.

The medieval and early-modern partnership forms supply the deepest precedent for a capital arrangement terminating with a single undertaking rather than persisting, documented in [Lane 1934][book_lane_1934], [Grief 2006][book_grief_2006] Institutions and the Path to the Modern Economy, [de Vries and van der Woude 1997][book_devries_vanderwoude_1997], [Steensgaard 1974][book_steensgaard_1974], [Stern 2011][book_stern_2011], and [Robins 2006][book_robins_2006]. The relevance to this article is narrower than to its predecessor and concerns the chartered company's combination of a commercial monopoly with a delegated public function, which is the historical arrangement closest to an operator holding an effectively exclusive position in a communications infrastructure across many jurisdictions.

The aircraft industry provides the sectoral precedent for a privately financed development programme at a scale exceeding the sponsoring firm's capacity to absorb failure, documented in [Newhouse 1982][book_newhouse_1982] The Sporty Game, [Newhouse 2007][book_newhouse_2007], [Serling 1992][book_serling_1992], [Bilstein 1996][book_bilstein_1996], and [Neufeld 1995][book_neufeld_1995]. The relevant finding is that such programmes were repeatedly sustained by government orders rather than by commercial demand alone, which is the same conjunction the series treats and which suggests the pattern is sectoral rather than singular.

The corporate research laboratory offers the precedent for patience obtained through monopoly rents rather than through a commercial spinoff, documented in [Gertner 2012][book_gertner_2012] The Idea Factory, [Hiltzik 1999][book_hiltzik_1999] Dealers of Lightning, [Kearns and Nadler 1992][book_kearns_nadler_1992], [Mowery and Rosenberg 1998][book_mowery_rosenberg_1998], and [Ruttan 2006][book_ruttan_2006]. The arrangement produced long horizons with no external claim at all and dissolved when the rents did, which is the precedent most directly relevant to the new Constraint the Spinoff Installs section, because it is a case in which the commercial base that funded the research eventually constrained it.

The postwar East Asian industrial financings supply the case in which the duration problem was solved by policy rather than by instrument, documented in [Johnson 1982][book_johnson_1982], [Amsden 1989][book_amsden_1989], [Wade 1990][book_wade_1990], [Evans 1995][book_evans_1995], [Chang 2002][book_chang_2002], [Woo-Cumings 1999][book_woo_cumings_1999], and the institutional treatments at [North 1990][book_north_1990] and [Acemoglu and Robinson 2012][book_acemoglu_robinson_2012]. The comparison is the closest available to the Chinese state programmes the contemporary landscape describes.

The modern project-finance apparatus documented at [Grimsey and Lewis 2004][book_grimsey_lewis_2004] and [Yescombe 2007][book_yescombe_2007] supplies the contemporary institutional answer to infrastructure whose construction period exceeds its financiers' horizon, through a special-purpose vehicle matched to a contracted revenue stream. The form is unavailable to a constellation before deployment for the reason the threshold property states, since the structure presupposes a contracted revenue stream and a pre-threshold constellation has none.

The computing industry gives the precedent for a firm that supplied a platform while competing with the parties depending on it, documented at the [IBM archives][ref_ibm_archives] with the analytical treatments at [Cusumano and Gawer 2002][book_cusumano_gawer_2002] and [Iansiti and Levien 2004][book_iansiti_levien_2004]. The pattern is the one the competition-policy tradition treats and it is the closest structural analogue to the launch-allocation conflict this article identifies.

## Historiographical Gap and Recent Scholarship

The scholarly literature bearing on the commercial-spinoff leg is developed on the sector and on the platform economics separately and is substantially absent on their conjunction, which is the gap this article addresses.

### Primary Source Documentation

The regulatory record is the strongest primary layer available to any article in this series and comprises the [Federal Communications Commission authorizations][ref_fcc_starlink_2018], the [second-generation authorization][ref_fcc_starlink_gen2_2022], the [direct-to-cell proceeding][ref_fcc_direct_to_cell_2024], the [Commission filing system][ref_fcc_filings], the [International Telecommunication Union Radio Regulations][ref_itu_radio_regulations_2020], the [Federal Aviation Administration Office of Commercial Space Transportation][ref_faa_ast] record, and the treaty instruments at the [Outer Space Treaty][ref_un_outer_space_treaty_1967], the [Liability Convention][ref_un_liability_convention_1972], and the [Registration Convention][ref_un_registration_convention_1976]. The debris regime is at the [NASA Orbital Debris Program Office][ref_nasa_orbital_debris], the [standard practices][ref_nasa_orbital_debris_mitigation], and the [Inter-Agency Space Debris Coordination Committee guidelines][ref_iadc_guidelines]. The company record is at [Starlink][ref_spacex_starlink], the [technology page][ref_starlink_technology], [direct-to-cell][ref_starlink_direct_to_cell], the [SpaceX corporate record][ref_spacex_company], and the [news archive][ref_spacex_news_archive]. Government contracting is traceable through [USAspending][ref_usaspending], the [Federal Procurement Data System][ref_fpds], and the [Department of Defense contract announcements][ref_dod_contracts].

### Platform and Network-Economics Literature

The literature is surveyed in the Cross-Disciplinary Framings section and its principal works are [Katz and Shapiro 1985][research_katz_shapiro_1985], [Farrell and Saloner 1985][research_farrell_saloner_1985], [Arthur 1989][research_arthur_1989], [David 1985][research_david_1985], [Rochet and Tirole 2003][research_rochet_tirole_2003], [Rochet and Tirole 2006][research_rochet_tirole_2006], [Rysman 2009][research_rysman_2009], [Parker and Van Alstyne 2005][research_parker_vanalstyne_2005], [Evans 2003][research_evans_2003], [Boudreau 2010][research_boudreau_2010], [Hagiu and Wright 2015][research_hagiu_wright_2015], [Gawer 2014][research_gawer_2014], [Gawer and Cusumano 2014][research_gawer_cusumano_2014], and [Jacobides Cennamo and Gawer 2018][research_jacobides_et_al_2018]. The gap with respect to the present case is that the literature developed on digital platforms whose marginal cost of serving an additional participant is near zero, and a constellation's marginal cost is not, so conclusions about pricing and market structure transfer only with qualification.

### Vertical Integration and Appropriability Literature

The principal works are [Coase 1937][research_coase_1937], [Williamson 1971][research_williamson_1971], [Williamson 1985][book_williamson_1985], [Klein Crawford and Alchian 1978][research_klein_crawford_alchian_1978], [Monteverde and Teece 1982][research_monteverde_teece_1982], [Grossman and Hart 1986][research_grossman_hart_1986], and [Teece 1986][research_teece_1986]. The gap is empirical rather than theoretical. The literature predicts that an integrated firm will favor its own downstream business, and testing the prediction here requires the internal transfer price and the capacity-allocation rule, neither of which is observable.

### Regulation and Competition-Policy Literature

The principal works are [Sharkey 1982][book_sharkey_1982], [Kahn 1988][book_kahn_1988], [Stigler 1971][research_stigler_1971], [Krueger 1974][research_krueger_1974], [Bain 1968][book_bain_1968], [Scherer and Ross 1990][book_scherer_ross_1990], [Tirole 1988][book_tirole_1988], [Bork 1978][book_bork_1978], [Posner 2001][book_posner_2001], [Hovenkamp 2005][book_hovenkamp_2005], and [Khan 2017][research_khan_2017]. The gap is that the sector's competition analysis has been conducted almost entirely at the launch-services level and almost not at all at the connectivity level, where the concentration is greater and the entry barrier is regulatory rather than technical.

### Sector and Policy Literature

The principal works are [Weinzierl 2018][research_weinzierl_2018], [Hertzfeld 2002][research_hertzfeld_2002], [Adilov Alexander and Cunningham 2014][research_adilov_et_al_2014], [Weeden and Chow 2012][research_weeden_chow_2012], and [Zimmerman 2011][research_zimmerman_2011], with the policy histories at [Launius 2004][book_launius_2004], [McCurdy 1994][book_mccurdy_1994], [Logsdon 1970][book_logsdon_1970], [Handberg 1994][book_handberg_1994], [McDougall 1985][book_mcdougall_1985], and [Heppenheimer 1999][book_heppenheimer_1999]. The literature treats the sector as a government-programme domain and has not substantially absorbed the transition to a commercially financed one.

### Capability and Organization Literature

The literature bearing on the spinoff as an application of existing capability comprises [Penrose 1959][book_penrose_1959], [March and Simon 1958][book_march_simon_1958], [Cyert and March 1963][book_cyert_march_1963], [Simon 1957][book_simon_1957], [Nelson and Winter 1982][book_nelson_winter_1982], [Teece Pisano and Shuen 1997][research_teece_pisano_shuen_1997], [Teece 2007][research_teece_2007], [Teece 2018][research_teece_2018], [Eisenhardt and Martin 2000][research_eisenhardt_martin_2000], [Helfat and Peteraf 2003][research_helfat_peteraf_2003], [Winter 2003][research_winter_2003], [Peteraf 1993][research_peteraf_1993], [Grant 1996][research_grant_1996], [Cohen and Levinthal 1990][research_cohen_levinthal_1990], [Kogut and Zander 1992][research_kogut_zander_1992], [March 1991][research_march_1991], and [Levitt and March 1988][research_levitt_march_1988]. The gap is that the literature theorizes capability application within a market and has little to say about a case where the firm creates the downstream market it then applies the capability to.

### Contract Theory and Empirical Integration Literature

The literature comprises [Coase 1937][research_coase_1937], [Williamson 1971][research_williamson_1971], [Williamson 1985][book_williamson_1985], [Williamson 2002][research_williamson_2002], [Klein Crawford and Alchian 1978][research_klein_crawford_alchian_1978], [Monteverde and Teece 1982][research_monteverde_teece_1982], [Grossman and Hart 1986][research_grossman_hart_1986], [Hart and Moore 1990][research_hart_moore_1990], [Hart 1988][research_hart_1988], with the empirical surveys at [Lafontaine and Slade 2007][research_lafontaine_slade_2007], [Bajari and Tadelis 2001][research_bajari_tadelis_2001], [Levin and Tadelis 2010][research_levin_tadelis_2010], [Corts and Singh 2004][research_corts_singh_2004], and [Gagnepain and Ivaldi 2002][research_gagnepain_ivaldi_2002]. The gap is that the empirical literature studies integration decisions with observable transfer prices and this case contributes none.

### Corporate Control and Ownership Literature

The literature comprises [Manne 1965][research_manne_1965], [Grossman and Hart 1988][research_grossman_hart_1988], [Harris and Raviv 1988][research_harris_raviv_1988], [DeAngelo and DeAngelo 1985][research_deangelo_deangelo_1985], [Fama and Jensen 1983][research_fama_jensen_1983], [Jensen 1986][research_jensen_1986], [Shleifer and Vishny 1997][research_shleifer_vishny_1997], [Bebchuk Kraakman and Triantis 2000][research_bebchuk_kraakman_triantis_2000], [Bebchuk and Kastiel 2017][research_bebchuk_kastiel_2017], [Gompers Ishii and Metrick 2003][research_gompers_ishii_metrick_2003], [La Porta Lopez-de-Silanes Shleifer and Vishny 1998][research_laporta_et_al_1998], [Hansmann 1996][book_hansmann_1996], [Easterbrook and Fischel 1991][book_easterbrook_fischel_1991], [Roe 1994][book_roe_1994], [Berle and Means 1932][book_berle_means_1932], and [Fligstein 2001][book_fligstein_2001]. The gap the new Constraint the Spinoff Installs section identifies is that this literature theorizes control exercised through ownership and has almost nothing to say about control exercised by a regulator, a licensing counterparty, or a subscriber base, none of which holds equity and each of which constrains the firm.

### Innovation Systems and Growth Literature

The literature comprises [Arrow 1962][research_arrow_1962], [Nelson 1959][research_nelson_1959], [Romer 1990][research_romer_1990], [Griliches 1979][research_griliches_1979], [Dosi 1988][research_dosi_1988], [Pavitt 1984][research_pavitt_1984], [Freeman and Soete 1997][research_freeman_soete_1997], [Bonvillian 2018][research_bonvillian_2018], [Nelson 1993][book_nelson_1993], [Mowery and Rosenberg 1998][book_mowery_rosenberg_1998], [Ruttan 2006][book_ruttan_2006], [Lipsey Carlaw and Bekar 2005][book_lipsey_carlaw_bekar_2005], and [Beinhocker 2006][book_beinhocker_2006]. The gap is that the general-purpose-technology framing predicts downstream effects that are by construction not yet observable, so the strongest form of the case for the arrangement is also the least testable.

### Reliability and Organizational Safety Literature

The literature comprises [Perrow 1984][book_perrow_1984], [Vaughan 1996][book_vaughan_1996], [Weick 1979][book_weick_1979], [Weick and Sutcliffe 2007][book_weick_sutcliffe_2007], [Selznick 1949][book_selznick_1949], [Mindell 2008][book_mindell_2008], and [MacKenzie 1990][book_mackenzie_1990]. The gap is that the sector's reliability literature was developed for low-tempo high-consequence programmes and the replenishment treadmill describes a high-tempo regime for which the accumulated findings may not transfer.

### Commons and Institutional Governance Literature

The literature comprises [Ostrom 1990][book_ostrom_1990], [North 1990][book_north_1990], [Acemoglu and Robinson 2012][book_acemoglu_robinson_2012], and the historical instances at [Grief 2006][book_grief_2006], [Lane 1934][book_lane_1934], and [de Vries and van der Woude 1997][book_devries_vanderwoude_1997]. The [Ostrom 1990][book_ostrom_1990] design principles supply the most useful available checklist for whether an orbital-allocation regime could work, and the article notes that the orbital case satisfies few of them, principally because the resource boundary is poorly defined and the appropriator community is not a community in any meaningful sense.

### Science and Technology Studies Literature

The literature comprises [Bijker Hughes and Pinch 1987][book_bijker_hughes_pinch_1987], [Bijker 1995][book_bijker_1995], [Latour 1987][book_latour_1987], [MacKenzie 1990][book_mackenzie_1990], [Hughes 1983][book_hughes_1983], [Nye 1990][book_nye_1990], and [Nye 1998][book_nye_1998], with the financial-sociology line at [MacKenzie 2006][book_mackenzie_2006], [Ho 2009][book_ho_2009], [Preda 2009][book_preda_2009], [Zaloom 2006][book_zaloom_2006], and [Krippner 2011][book_krippner_2011]. The gap is that the sector has attracted comparatively little constructivist attention relative to its cultural prominence.

### Critical and Skeptical Literature

A critical literature reads the arrangement as the private appropriation of a global commons and as the concentration of communications infrastructure in a single unaccountable firm, drawing on [Srnicek 2017][book_srnicek_2017] Platform Capitalism, [Zuboff 2019][book_zuboff_2019], [Krippner 2011][book_krippner_2011], [Wu 2010][book_wu_2010], and [Khan 2017][research_khan_2017]. The orbital-commons form of the concern is the strongest, because the resource is genuinely finite, genuinely shared, and genuinely unpriced. The article regards the concern as well founded and does not resolve it.

### Case-Study and Biographical Literature

The narrative record is at [Berger 2021][book_berger_2021] Liftoff, [Berger 2024][book_berger_2024] Reentry, [Vance 2015][book_vance_2015], [Isaacson 2023][book_isaacson_2023], [Davenport 2018][book_davenport_2018], and [Fernholz 2018][book_fernholz_2018], and it yields substantially the entire account of the internal decision to proceed with the programme.

### Trade Press and Journalistic Record

Substantially every quantitative claim in this article rests on the reconstruction appearing in [SpaceNews][ref_spacenews], [Ars Technica space coverage][ref_arstechnica_space], [Payload][ref_payload], [Payload Research][ref_payload_research], [The Space Review][ref_the_space_review], [NASASpaceflight][ref_nasaspaceflight], [Space Policy Online][ref_space_policy_online], [European Spaceflight][ref_european_spaceflight], [Aviation Week][ref_aviation_week], [Breaking Defense][ref_breaking_defense], [Defense News][ref_defense_news], [Bloomberg][ref_bloomberg], the [New York Times][ref_nyt], and the [Wall Street Journal][ref_wsj], with the sector analyses at [Space Capital][ref_space_capital], [BryceTech][ref_bryce_tech], and [PitchBook][ref_pitchbook].

## Contemporary Comparative Landscape

The contemporary landscape for the commercial-spinoff leg is the emptiest of the three capital-formation legs, because the conditions the pattern requires are jointly satisfied almost nowhere.

The European position operates through [Arianespace][ref_arianespace] and [ArianeGroup][ref_arianegroup_press] under a governmental-shareholder arrangement, with a constellation programme pursued at the union level rather than by a commercial operator, and the entrant record at [European Spaceflight][ref_european_spaceflight]. The configuration cannot produce the arrangement this article describes, because the launch provider and the constellation operator are separate institutions with separate budgets, so the internal transaction occurs at a negotiated price rather than at marginal cost. The condition the arrangement requires admits the compact statement

$$\text{common residual claimant over both stages} \iff \text{transfer at } c^{\text{marginal}} \text{ is incentive-compatible}$$

with separate budgets destroying the incentive compatibility irrespective of any policy intention, because each institution is assessed on its own result.

The Chinese position documented at [China commercial space][ref_china_commercial_space] pursues constellation programmes with state financing and domestic launch capacity, which satisfies the captive-launch condition through common state ownership rather than through common corporate ownership. The article regards this as the closest structural analogue currently in existence and notes that it achieves the coupling by a different institutional route.

The Indian and Japanese positions at [ISRO][ref_isro_press] and [JAXA][ref_jaxa_press] hold launch capability without a commercial constellation of comparable scale, and the broader Chinese programme record is at [China's space programme][ref_chinese_space_program]. The crewed-spaceflight and station lines that other commercial operators pursue are documented at the [Polaris programme][ref_polaris_program], the [NASA International Space Station record][ref_nasa_iss], and the general [NASA news record][ref_nasa_news], and the large-scale international scientific collaboration at the [ITER Organization][ref_iter_organization] supplies the contrasting institutional form in which no commercial spinoff is contemplated at all.

The scarcity of the configuration can be stated as

$$\left| \left\{ \text{entities holding captive launch at constellation cadence} \right\} \right| \; \sim \; 2$$

counting the present case and the Chinese state programmes, and the article notes that this is the smallest comparison set of any condition treated in the series. The pattern the closing section states is therefore extracted from close to a single observation, and the reader should weight it accordingly.

Among commercial entrants, [Rocket Lab][ref_rocket_lab_press] holds launch capability at a vehicle scale below constellation deployment economics while developing a larger vehicle, [Blue Origin][ref_blue_origin_press] holds a launch programme under the single-funder arrangement the [Governance article A287][related_post_a287_spacex_governance] treats and is affiliated with the constellation competitor this article discusses, and [United Launch Alliance][ref_ula_press] with its parents at [Boeing][ref_boeing_press] and [Northrop Grumman][ref_northrop_grumman_press] operates as a launch provider without a downstream service business. The [Space Force National Security Space Launch programme][ref_space_force_nssl] record documents the government-customer side of the same set.

The scarcity of the configuration is best appreciated against the historical alternatives rather than against contemporary entrants alone. The regulated-monopoly form the [Bell System][ref_att_consent_decree_1956] settlement produced, the state-directed form the East Asian financings employed, and the foundation-ownership form the [Governance article A287][related_post_a287_spacex_governance] treats each solved the duration problem by a route unavailable to a commercially financed venture in a common-law jurisdiction. The arrangement this article describes is therefore not the general solution to a general problem but a particular solution available under a narrow conjunction of conditions, which is the qualification the closing article should carry into any forward projection.

## Comparative Cross-Sectional Analysis

The commercial-spinoff leg admits application to the venture set as a cross-sectional scoring exercise across the five sub-properties the pattern-extraction section states. The closure vector admits the compact form

$$\boldsymbol{\phi}_j^{\text{spinoff}} \in \{0,1\}^{5}$$

with each venture's vector indicating satisfaction across the captive-input, surplus-capacity, threshold-market, regulatory-priority, and reinvestment-scale sub-properties.

The scoring assembles into a matrix whose rows are the ventures and whose columns are the sub-properties in the order the pattern-extraction section states

$$\begin{array}{lccccc}
 & \phi_1 & \phi_2 & \phi_3 & \phi_4 & \phi_5 \\
\text{SpaceX} & 1 & 1 & 1 & 1 & 1 \\
\text{Iridium} & 0 & 0 & 1 & 1 & 0 \\
\text{OneWeb} & 0 & 0 & 1 & 0 & 0 \\
\text{Amazon programme} & 0 & 0 & 1 & \ast & 1 \\
\text{Chinese state programmes} & 1 & \ast & 1 & \ast & \ast
\end{array}$$

with $\ast$ marking a cell the available record does not establish. The underlying deployment and financing data are reconstructed from [Space Capital][ref_space_capital], [BryceTech][ref_bryce_tech], [Payload Research][ref_payload_research], and [PitchBook][ref_pitchbook], and the corporate comparators whose balance-sheet positions the reinvestment-scale column reflects are documented at [Alphabet investor relations][ref_alphabet_ir], [Meta investor relations][ref_meta_ir], and the [Berkshire Hathaway shareholder letters][ref_berkshire]. SpaceX exhibits closure on all five. Iridium exhibited non-closure on captive input and surplus capacity, closure on threshold market and regulatory priority, and non-closure on reinvestment scale. OneWeb exhibited the same pattern with an additional failure on regulatory priority following its deployment interruption. The Amazon programme exhibits non-closure on captive input, closure on reinvestment scale by virtue of its sponsor, and an unresolved position on regulatory priority. The Chinese state programmes exhibit closure on captive input through common ownership and an unresolved position on the remainder.

The cross-sectional pattern indicates that the captive-input sub-property is the one that discriminates most sharply, and the correlation with the outcome may be stated compactly

$$\operatorname{corr}_j\!\left( \phi_{j,1}^{\text{captive input}}, \; \text{completion} \right) \gg \operatorname{corr}_j\!\left( \phi_{j,5}^{\text{reinvestment scale}}, \; \text{completion} \right)$$

with the availability of captive launch capacity carrying more information than the sponsor's capital scale. The finding is the article's central empirical claim and it is the reason the article treats the Amazon comparison as the informative one, since that case holds capital scale high and captive input absent.

## Data Sources and Reconstruction Methodology

The article draws on primary and secondary sources with a pronounced asymmetry between the regulatory and financial layers.

The primary-source layer on regulatory matters is complete and authoritative. Authorizations, filings, coordination records, and licensing decisions are public and were consulted directly through the [Commission filing system][ref_fcc_filings], the [Radio Regulations][ref_itu_radio_regulations_2020], and the [Office of Commercial Space Transportation][ref_faa_ast] record. Congressional deliberation on the statutory framework is at the [Congressional Record][ref_congressional_record] and the [House Science Committee hearing record][ref_house_science_committee_hearings]. The teaching-case reconstructions at the [Stanford Graduate School of Business case collection][ref_stanford_spacex_case], the [Harvard Business School case collection][ref_hbs_spacex_case], and the [Wharton knowledge repository][ref_wharton_spacex_case] supply secondary reconstructions assembled from the same public record and were used as cross-checks rather than as sources.

The primary-source layer on financial matters is substantially absent. The firm is private, the spinoff has never been separately reported, and no segment disclosure exists. The reconstruction methodology therefore takes the regulatory record as the spine for anything concerning satellite counts, authorizations, and deployment dates, and relies on trade-press reconstruction for everything concerning subscribers, revenue, and cost.

The empirical-record limitations comprise the following. The internal transfer price is unknown and determines the attribution of profit between the segments. The capacity-allocation rule between internal and external launch demand is unknown. Satellite unit cost is unknown. Mission burn is unknown, which makes the crossover date unknown. Subscriber and revenue figures are company statements repeated by the press rather than audited disclosures. The consequence is that the article's structural claims are substantially better supported than its quantitative ones, and the reader should treat the numbers as illustrative of a pattern rather than as measurements.

## Alternative Analytical Frameworks

The commercial-spinoff framing the article develops is one of several the surrounding literature applies.

The diversification framing treats the constellation as an entry into an unrelated market and predicts value destruction on the evidence the corporate-diversification literature contributes. The article's response is that the framing misidentifies the relationship, and the distinction is stated compactly as

$$\text{related} \iff \frac{\partial c^{\text{segment } A}}{\partial q^{\text{segment } B}} \neq 0$$

with genuine relatedness requiring that one segment's activity alter the other's cost. The businesses here share the input rather than merely the owner, so the derivative is nonzero and negative. The framing's prediction would apply to a constellation operator purchasing launch at market, for whom the derivative is zero.

The platform framing treats the constellation as a two-sided market and imports the pricing and market-structure conclusions of the platform literature. The article accepts the framing for the direct-to-cell service and rejects it for consumer broadband, on the ground that the latter has one side and a positive marginal cost. The rejection admits the compact test

$$\frac{\partial u^{\text{subscriber}}}{\partial n^{\text{subscriber}}} \leq 0 \quad \text{for shared-capacity broadband}$$

with additional subscribers degrading rather than improving the service, which is the opposite of the network externality the platform conclusions presuppose.

The natural-monopoly framing treats the position as a durable dominance arising from scale economies and a finite resource, and it generates the regulatory prescriptions the regulated-industry tradition supplies. The article's response is stated compactly as a contrast in the durability of the underlying asset

$$T^{\text{asset life, conventional utility}} \sim 10^{1} \; \text{to} \; 10^{2} \; \text{years} \qquad \text{against} \qquad L \sim 5 \; \text{years}$$

with the conventional natural monopoly resting on an asset base that outlives any plausible entrant response and this one resting on an asset base that does not. The finite resource here is spectrum priority rather than infrastructure, and priority is a legal position that an administration can in principle revisit.

The commons framing treats the orbital environment as a shared resource being appropriated without compensation and generates the strongest available critique. The article accepts the framing's factual premise. The allocation the framing would require admits the compact statement as a corrective price

$$p^{\text{orbital}}_i = \sum_{j \neq i} \frac{\partial \Pi_j}{\partial S_i}$$

with each operator charged the marginal external cost it imposes on the others. No such instrument exists in any jurisdiction. The framing therefore argues for an allocation regime rather than against any particular operator, and the article notes that the first operator to reach scale in an unpriced commons is the one an eventual regime would most constrain, which gives the incumbent an interest in the regime's design that is worth stating explicitly. The forums in which such a regime would be negotiated are the [International Telecommunication Union][ref_itu_radio_regulations_2020] process, the treaty framework at the [Outer Space Treaty][ref_un_outer_space_treaty_1967] and the [Registration Convention][ref_un_registration_convention_1976], and the domestic rulemaking record at the [Commission filing system][ref_fcc_filings].

The comparative-institutional framing asks whether the arrangement is a feature of United States law and industrial structure specifically. The [United Kingdom Companies Act 2006][ref_uk_companies_act_2006] pre-emption regime and the corporate-governance expectations at the [Organisation for Economic Co-operation and Development][ref_oecd_corporate_governance] would each constrain the financing sequence that produced the capability, and the flexible contracting authorities at the [Department of Defense other-transaction guidance][ref_dod_other_transactions] have no direct analogue in most jurisdictions. The configuration is therefore less portable than its abstract statement suggests, which the [Government-Anchor Capital-Formation Leg article A289][related_post_a289_spacex_government_anchor_leg] develops for the procurement side.

The industrial-policy framing treats the outcome as the return on the government investment the [Government-Anchor Capital-Formation Leg article A289][related_post_a289_spacex_government_anchor_leg] documents, and it generates the claim that the public has an equity-like interest in the result that the non-dilutive instrument failed to secure. The article regards the framing as analytically serious and notes that it is a claim about what the instrument should have been rather than about what it was.

The capability framing developed in [Penrose 1959][book_penrose_1959], [Teece Pisano and Shuen 1997][research_teece_pisano_shuen_1997], [Teece 2007][research_teece_2007], [Eisenhardt and Martin 2000][research_eisenhardt_martin_2000], [Helfat and Peteraf 2003][research_helfat_peteraf_2003], and [Winter 2003][research_winter_2003] treats the spinoff as the application of a capability the firm already possessed rather than as an entry into a market it did not understand. Under the framing the interesting question is not why the firm entered but why no other holder of comparable capability did, and the answer the article provides is that no other holder had surplus capacity at the required cadence.

The contract-and-boundaries framing developed in [Lafontaine and Slade 2007][research_lafontaine_slade_2007], [Bajari and Tadelis 2001][research_bajari_tadelis_2001], [Levin and Tadelis 2010][research_levin_tadelis_2010], and [Corts and Singh 2004][research_corts_singh_2004] asks whether the observed integration is consistent with the empirical regularities the literature has established. It is, and unusually strongly, because the activity exhibits high asset specificity, high measurement difficulty, and high coordination requirements, which are the three conditions the empirical literature most consistently associates with integration.

The corporate-control framing developed in [Manne 1965][research_manne_1965], [Grossman and Hart 1988][research_grossman_hart_1988], [Harris and Raviv 1988][research_harris_raviv_1988], [Fama and Jensen 1983][research_fama_jensen_1983], [Shleifer and Vishny 1997][research_shleifer_vishny_1997], [Hansmann 1996][book_hansmann_1996], and [Easterbrook and Fischel 1991][book_easterbrook_fischel_1991] treats the arrangement as an ownership question and asks which class of party should hold residual control. The new Constraint the Spinoff Installs section develops the framing's principal limitation for this case, which is that the parties acquiring leverage over the firm through the spinoff acquire it without ownership and are therefore invisible to the framing entirely.

The reliability framing developed in [Perrow 1984][book_perrow_1984], [Vaughan 1996][book_vaughan_1996], [Weick and Sutcliffe 2007][book_weick_sutcliffe_2007], and [Mindell 2008][book_mindell_2008] treats the replenishment treadmill as an organizational condition rather than a financial one and generates the prediction that sustained high tempo erodes the margins that absorb error. The prediction is testable against the programme's own anomaly record and the article does not attempt the test, which is a gap a subsequent treatment could close.

The commons-governance framing developed in [Ostrom 1990][book_ostrom_1990], [North 1990][book_north_1990], and [Acemoglu and Robinson 2012][book_acemoglu_robinson_2012] asks whether an orbital-allocation regime could work rather than whether one is needed. Applying the design principles yields a pessimistic answer, principally because the resource boundary is poorly defined and the appropriators are sovereign states rather than a community, and the article regards this as a more useful contribution than a further restatement that the externality exists.

The evolutionary framing developed in [Nelson and Winter 1982][book_nelson_winter_1982], [Metcalfe 1998][book_metcalfe_1998], and [Klepper 1996][research_klepper_1996] supplies the selection caution, which applies with particular force here because the spinoff is observed only in the case that succeeded and the contemporaneous attempts that failed are the comparison set the article uses to argue for the mechanism.

## Pattern Extraction

The category-dominating commercial spinoff pattern that the SpaceX case exhibits admits the following abstract statement without naming any downstream application. A mission-directed technology venture achieves the commercial-spinoff closure when it builds a downstream business that consumes its own principal output at marginal cost, in a market whose value depends on a deployment threshold the venture's own capacity allows it to reach faster than any competitor, and at a scale whose retained earnings exceed the mission burn.

The abstract mechanic requires joint satisfaction of five sub-properties, admitting the compact conjunctive form

$$\Phi^{\text{spinoff}} = \prod_{k=1}^{5} \phi_k, \qquad \phi_k \in \{0,1\}$$

First, the spinoff must consume an input the parent produces, so that its cost position is the parent's marginal cost rather than any market price. A spinoff purchasing at market is a diversification and is subject to every objection the diversification literature raises.

Second, the parent must hold surplus capacity in that input, so that the consumption monetizes an idle resource rather than displacing a more valuable external sale.

Third, the downstream market must exhibit a deployment threshold, so that speed of deployment converts into a durable position rather than into a merely earlier revenue start.

Fourth, the position must be protected by a priority rule the venture can satisfy and competitors cannot, which in this instance is regulatory rather than technical.

Fifth, the resulting earnings must reach the scale of the mission burn, since a profitable spinoff below that scale improves the financial position without closing the capital-formation problem.

The mechanic admits a diagnostic procedure stated as an ordered test vector

$$\tau = \left( \text{input captive}, \;\; q^{\text{external}} < \bar{q}, \;\; \text{threshold market}, \;\; \text{priority attainable}, \;\; R \geq B \right)$$

with the first component the one a candidate case will usually fail and the fifth the one an assessment will usually assert without evidence.

The mechanic carries a limitation the statement should not conceal. The arrangement converts a capital asset into a consumable, because the downstream business imposes a permanent replenishment obligation that scales with its own size. The limitation admits the compact statement

$$\text{durability} \; \sim \; \frac{L}{T^{\text{competitor deployment}}} \qquad \text{rather than} \qquad \text{durability} \to \infty$$

with the ratio small wherever the replacement interval is short. The venture does not obtain an annuity. It obtains a business that must rebuild itself continuously and whose dominance lasts precisely as long as it continues to do so faster than anyone else.

A second limitation is stated in the Constraint the Spinoff Installs section and belongs in the abstract statement rather than only in the analysis. The fifth sub-property requires that retained earnings reach the scale of the mission burn, and it is written as though the spinoff's contribution were its gross generation. It is not. A spinoff at mission-funding scale is also an operating business with service obligations, counterparty commitments, and regulatory dependencies in every jurisdiction it serves, and those obligations consume the same decision capacity the mission requires. The closure the pattern describes is therefore a substitution of constraints rather than a removal of one, and a candidate case should be assessed on the net rather than on the gross.

## Cross-References to the Series

The article back-references the [series opener][related_post_a281_spacex_framing] for the seven-plus-three framework and the mission burn the spinoff is intended to fund. The article back-references the [Value Gradient article A282][related_post_a282_spacex_value_gradient] for the vehicle progression whose surplus capacity the spinoff consumes. The article back-references the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] for the external anchor customer the spinoff internalizes. The article back-references the [Value Capture article A284][related_post_a284_spacex_value_capture] for the complementary-asset argument this article offers the sharpest instance of. The article back-references the [Decomposability article A285][related_post_a285_spacex_decomposability] for the reuse progression the cadence coupling accelerates. The article back-references the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] for the design commonality that makes the satellite production rate attainable. The article back-references the [Governance article A287][related_post_a287_spacex_governance] for the control configuration that permitted the programme to be undertaken over the objection external shareholders would likely have raised. The article back-references the [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] for the line structure the spinoff occupies and for the transfer price both articles identify as the critical unobserved quantity. The article back-references the [Government-Anchor Capital-Formation Leg article A289][related_post_a289_spacex_government_anchor_leg] for the non-dilutive channel that financed the capability the spinoff exploits. The article back-references the [Patient-Private Capital-Formation Leg article A290][related_post_a290_spacex_patient_private_leg] for the January 2015 round raised against the business this article describes.

The article forward-references the closing article A292, which synthesizes across the framework and treats the singular-conjunction thesis.

The article cross-references the existing published corpus including the [Why Startups Actually Fail article A167][related_post_a167_startup_failure], the [What a Patent Is and Is Not article A161][related_post_a161_patent_intro], the [Patents Trade Secrets and the Disclosure Tradeoff article A164][related_post_a164_patents_trade_secrets], the [Money Behind an SBIR or STTR Award article A140][related_post_a140_sbir_money], the [Introduction to Space Studies article A90][related_post_a90_intro_space_studies], the [History of Rocketplanes article A96][related_post_a96_history_rocketplanes], the [What Does the United States Space Force Do article A97][related_post_a97_us_space_force], the [Framing and the Co-Development Mechanism article A237][related_post_a237_aerospace_framing], the [Silicon Valley from Defense Contracting article A246][related_post_a246_silicon_valley_defense], and the [Contemporary Snapshot article A248][related_post_a248_contemporary_snapshot].

## Terminological Note

The article adopts terminology consistent with the satellite communications and industrial-organization conventions and marks the places popular usage diverges. The term "spinoff" refers throughout to a business line built within the firm on an existing capability, and not to a corporate separation, which is the ordinary financial meaning and which the [Governance article A287][related_post_a287_spacex_governance] treats as an open question for this business specifically. The term "constellation" refers to a coordinated set of satellites operated as a single system, and is distinguished from a "fleet", which carries no coordination implication. The term "captive input" refers to an input supplied by a commonly owned party at internal cost, and is distinguished from a "secured supply", which refers to a contracted external supply at a market price. The term "category-dominating" refers to a position holding the majority of a defined service category by the relevant volume measure, and the article marks that the category definition is contestable and that the position looks different if the category is defined as satellite broadband, as rural broadband, or as connectivity generally. The term "replenishment" refers to the ongoing replacement of satellites reaching end of life, and is distinguished from "expansion", which refers to growth in the deployed count.

## Load-Bearing Open Questions

The article closes with the load-bearing open questions the treatment leaves unresolved. First, the internal transfer price is unknown, and it determines whether the launch business or the constellation business is the profitable one in any reported segmentation. Second, the capacity-allocation rule between internal and external launch demand is unknown, and it is the quantity a competition authority would need first. Third, the mission-funding crossover date is unknown, and it is the single most consequential unresolved quantity in the series, because every arrangement the preceding articles describe exists to bridge the interval before it. Fourth, whether the regulatory priority the constellation holds is durable against a coordinated administrative response is untested. Fifth, whether the replenishment treadmill limits the position's durability as the article argues or is offset by production learning faster than obsolescence is an empirical question the available data cannot settle. Sixth, the direct-to-cell business depends on a complementary asset the venture does not own, and the division of value between the operator and the carriers is unresolved. Seventh, whether the orbital-congestion externality will be addressed by an allocation regime, by liability, or not at all is a policy question whose resolution would materially alter the economics this article describes.

## References

### Books

- [Acemoglu and Robinson 2012 Why Nations Fail][book_acemoglu_robinson_2012]
- [Amsden 1989 Asia's Next Giant][book_amsden_1989]
- [Bain 1968 Industrial Organization][book_bain_1968]
- [Beinhocker 2006 The Origin of Wealth][book_beinhocker_2006]
- [Berger 2021 Liftoff][book_berger_2021]
- [Berger 2024 Reentry][book_berger_2024]
- [Berle and Means 1932 The Modern Corporation and Private Property][book_berle_means_1932]
- [Bijker 1995 Of Bicycles Bakelites and Bulbs][book_bijker_1995]
- [Bijker Hughes Pinch 1987 The Social Construction of Technological Systems][book_bijker_hughes_pinch_1987]
- [Bilstein 1996 Stages to Saturn][book_bilstein_1996]
- [Bork 1978 The Antitrust Paradox][book_bork_1978]
- [Chandler 1977 The Visible Hand][book_chandler_1977]
- [Chandler 1990 Scale and Scope][book_chandler_1990]
- [Chang 2002 Kicking Away the Ladder][book_chang_2002]
- [Chernow 2004 Titan][book_chernow_2004]
- [Christensen 1997 The Innovator's Dilemma][book_christensen_1997]
- [Christensen and Raynor 2003 The Innovator's Solution][book_christensen_raynor_2003]
- [Cusumano and Gawer 2002 Platform Leadership][book_cusumano_gawer_2002]
- [Cyert and March 1963 A Behavioral Theory of the Firm][book_cyert_march_1963]
- [Davenport 2018 The Space Barons][book_davenport_2018]
- [de Vries and van der Woude 1997 The First Modern Economy][book_devries_vanderwoude_1997]
- [Easterbrook and Fischel 1991 The Economic Structure of Corporate Law][book_easterbrook_fischel_1991]
- [Evans 1995 Embedded Autonomy][book_evans_1995]
- [Fernholz 2018 Rocket Billionaires][book_fernholz_2018]
- [Fligstein 2001 The Architecture of Markets][book_fligstein_2001]
- [Gertner 2012 The Idea Factory][book_gertner_2012]
- [Grief 2006 Institutions and the Path to the Modern Economy][book_grief_2006]
- [Grimsey and Lewis 2004 Public Private Partnerships][book_grimsey_lewis_2004]
- [Handberg 1994 Reinventing NASA][book_handberg_1994]
- [Hansmann 1996 The Ownership of Enterprise][book_hansmann_1996]
- [Heppenheimer 1999 The Space Shuttle Decision][book_heppenheimer_1999]
- [Hiltzik 1999 Dealers of Lightning][book_hiltzik_1999]
- [Ho 2009 Liquidated][book_ho_2009]
- [Hovenkamp 2005 The Antitrust Enterprise][book_hovenkamp_2005]
- [Hughes 1983 Networks of Power][book_hughes_1983]
- [Iansiti and Levien 2004 The Keystone Advantage][book_iansiti_levien_2004]
- [Isaacson 2023 Elon Musk][book_isaacson_2023]
- [Johnson 1982 MITI and the Japanese Miracle][book_johnson_1982]
- [Kahn 1988 The Economics of Regulation][book_kahn_1988]
- [Kearns and Nadler 1992 Prophets in the Dark][book_kearns_nadler_1992]
- [Krippner 2011 Capitalizing on Crisis][book_krippner_2011]
- [Laffont and Tirole 1993 A Theory of Incentives in Procurement and Regulation][book_laffont_tirole_1993]
- [Landes 1969 The Unbound Prometheus][book_landes_1969]
- [Lane 1934 Venetian Ships and Shipbuilders of the Renaissance][book_lane_1934]
- [Latour 1987 Science in Action][book_latour_1987]
- [Launius 2004 Frontiers of Space Exploration][book_launius_2004]
- [Levin 2010 The Wires That Bind][book_levin_2010]
- [Lipsey Carlaw and Bekar 2005 Economic Transformations General Purpose Technologies and Long-Term Economic Growth][book_lipsey_carlaw_bekar_2005]
- [Logsdon 1970 The Decision to Go to the Moon][book_logsdon_1970]
- [MacKenzie 1990 Inventing Accuracy][book_mackenzie_1990]
- [MacKenzie 2006 An Engine Not a Camera][book_mackenzie_2006]
- [March and Simon 1958 Organizations][book_march_simon_1958]
- [McAfee and McMillan 1988 Incentives in Government Contracting][book_mcafee_mcmillan_1988]
- [McCurdy 1994 Inside NASA][book_mccurdy_1994]
- [McDougall 1985 The Heavens and the Earth][book_mcdougall_1985]
- [Metcalfe 1998 Evolutionary Economics and Creative Destruction][book_metcalfe_1998]
- [Milgrom 2004 Putting Auction Theory to Work][book_milgrom_2004]
- [Mindell 2008 Digital Apollo][book_mindell_2008]
- [Mowery and Rosenberg 1998 Paths of Innovation][book_mowery_rosenberg_1998]
- [Nelson 1993 National Innovation Systems][book_nelson_1993]
- [Nelson and Winter 1982 An Evolutionary Theory of Economic Change][book_nelson_winter_1982]
- [Neufeld 1995 The Rocket and the Reich][book_neufeld_1995]
- [Nevins 1954 Ford The Times The Man The Company][book_nevins_1954]
- [Newhouse 1982 The Sporty Game][book_newhouse_1982]
- [Newhouse 2007 Boeing versus Airbus][book_newhouse_2007]
- [North 1990 Institutions Institutional Change and Economic Performance][book_north_1990]
- [Nye 1990 Electrifying America][book_nye_1990]
- [Nye 1998 Consuming Power][book_nye_1998]
- [Ostrom 1990 Governing the Commons][book_ostrom_1990]
- [Penrose 1959 The Theory of the Growth of the Firm][book_penrose_1959]
- [Perez 2002 Technological Revolutions and Financial Capital][book_perez_2002]
- [Perrow 1984 Normal Accidents][book_perrow_1984]
- [Posner 2001 Antitrust Law][book_posner_2001]
- [Preda 2009 Framing Finance][book_preda_2009]
- [Robins 2006 The Corporation That Changed the World][book_robins_2006]
- [Roe 1994 Strong Managers Weak Owners][book_roe_1994]
- [Ruttan 2006 Is War Necessary for Economic Growth][book_ruttan_2006]
- [Scherer and Ross 1990 Industrial Market Structure and Economic Performance][book_scherer_ross_1990]
- [Selznick 1949 TVA and the Grass Roots][book_selznick_1949]
- [Serling 1992 Legend and Legacy][book_serling_1992]
- [Sharkey 1982 The Theory of Natural Monopoly][book_sharkey_1982]
- [Simon 1957 Administrative Behavior][book_simon_1957]
- [Sobel 1995 Longitude][book_sobel_1995]
- [Srnicek 2017 Platform Capitalism][book_srnicek_2017]
- [Steensgaard 1974 The Asian Trade Revolution of the Seventeenth Century][book_steensgaard_1974]
- [Stern 2011 The Company-State][book_stern_2011]
- [Temin and Galambos 1987 The Fall of the Bell System][book_temin_galambos_1987]
- [Tirole 1988 The Theory of Industrial Organization][book_tirole_1988]
- [Utterback 1994 Mastering the Dynamics of Innovation][book_utterback_1994]
- [Van Alstyne Parker Choudary 2016 Platform Revolution][book_vanalstyne_parker_choudary_2016]
- [Vance 2015 Elon Musk Tesla SpaceX and the Quest for a Fantastic Future][book_vance_2015]
- [Vaughan 1996 The Challenger Launch Decision][book_vaughan_1996]
- [Wade 1990 Governing the Market][book_wade_1990]
- [Weick 1979 The Social Psychology of Organizing][book_weick_1979]
- [Weick and Sutcliffe 2007 Managing the Unexpected][book_weick_sutcliffe_2007]
- [Williamson 1985 The Economic Institutions of Capitalism][book_williamson_1985]
- [Woo-Cumings 1999 The Developmental State][book_woo_cumings_1999]
- [Wu 2010 The Master Switch][book_wu_2010]
- [Yescombe 2007 Public-Private Partnerships Principles of Policy and Finance][book_yescombe_2007]
- [Zaloom 2006 Out of the Pits][book_zaloom_2006]
- [Zuboff 2019 The Age of Surveillance Capitalism][book_zuboff_2019]

### Reference

- [14 CFR Chapter III FAA Commercial Space Regulations][ref_faa_ast_regulations]
- [14 CFR Part 450 Launch and Reentry Licensing][ref_faa_ast_licensing_regs_450]
- [1956 AT&T Consent Decree][ref_att_consent_decree_1956]
- [1984 AT&T Divestiture Modification of Final Judgment][ref_att_divestiture_1984]
- [22 CFR 120 through 130 International Traffic in Arms Regulations][ref_itar_22_cfr_120_130]
- [51 U.S.C. Chapter 509 Commercial Space Launch Act 1984][ref_csla_1984]
- [AIAA Journal of Propulsion and Power][ref_aiaa_jpp]
- [AIAA Journal of Spacecraft and Rockets][ref_aiaa_jsr]
- [Alphabet Investor Relations][ref_alphabet_ir]
- [Aon Space and Aviation Risk Brokerage][ref_aon_space_insurance]
- [ArianeGroup Press Releases][ref_arianegroup_press]
- [Arianespace][ref_arianespace]
- [Ars Technica Space Coverage][ref_arstechnica_space]
- [Aviation Week Coverage][ref_aviation_week]
- [Berkshire Hathaway Shareholder Materials][ref_berkshire]
- [Bloomberg Business News][ref_bloomberg]
- [Blue Origin Press Releases][ref_blue_origin_press]
- [Boeing Press Releases][ref_boeing_press]
- [Breaking Defense Coverage][ref_breaking_defense]
- [BryceTech Sector Reports][ref_bryce_tech]
- [China Commercial Space Industry Analysis][ref_china_commercial_space]
- [Chinese Space Program Documentation][ref_chinese_space_program]
- [Commercial Space Launch Amendments Act 2004][ref_csla_amendments_2004]
- [Congressional Record][ref_congressional_record]
- [Council of Institutional Investors][ref_cii]
- [Defense News Coverage][ref_defense_news]
- [Delaware Court of Chancery][ref_delaware_chancery]
- [Delaware General Corporation Law Title 8 Chapter 1][ref_dgcl]
- [Department of Defense Other Transaction Guidance][ref_dod_other_transactions]
- [DOD Contract Announcements][ref_dod_contracts]
- [European Corporate Governance Institute][ref_ecgi]
- [European Spaceflight Coverage][ref_european_spaceflight]
- [Eutelsat Corporate Record][ref_eutelsat_oneweb]
- [FAA Financial Responsibility Requirements 14 CFR Part 440][ref_faa_financial_responsibility]
- [FAA Office of Commercial Space Transportation][ref_faa_ast]
- [FAA Starship Programmatic Environmental Assessment][ref_faa_starship_pea]
- [FCC Direct-to-Cell Authorization 2024][ref_fcc_direct_to_cell_2024]
- [FCC Filings Database][ref_fcc_filings]
- [FCC Starlink Authorization March 2018][ref_fcc_starlink_2018]
- [FCC Starlink Generation 2 Authorization December 2022][ref_fcc_starlink_gen2_2022]
- [Federal Procurement Data System][ref_fpds]
- [Financial Accounting Standards Board][ref_fasb_asc280]
- [FTSE Russell][ref_ftse_russell]
- [Harvard Business School SpaceX Case][ref_hbs_spacex_case]
- [Harvard Law School Forum on Corporate Governance][ref_harvard_corpgov_forum]
- [House Committee on Science Space and Technology Hearings on Commercial Crew][ref_house_science_committee_hearings]
- [IBM Archives][ref_ibm_archives]
- [INCOSE 2015 Systems Engineering Handbook][ref_incose_handbook]
- [Indian Space Research Organisation Press Releases][ref_isro_press]
- [Inter-Agency Space Debris Coordination Committee][ref_iadc_guidelines]
- [Iridium Chapter 11 Bankruptcy Filing 1999][ref_iridium_chapter_11_1999]
- [Iridium World Communications Press Release Archive 1998][ref_iridium_press_archive_1998]
- [ITER Organization][ref_iter_organization]
- [ITU Radio Regulations 2020][ref_itu_radio_regulations_2020]
- [Japanese Aerospace Exploration Agency Press Releases][ref_jaxa_press]
- [Journal of Public Procurement][ref_journal_public_procurement]
- [KSC LC-39A Lease Agreement][ref_ksc_lc39a_lease]
- [Lloyd's of London Market][ref_lloyds_market]
- [Meta Investor Relations][ref_meta_ir]
- [Musk 2017 International Astronautical Congress Making Life Multi-Planetary][ref_musk_iac_2017]
- [NASA Design Reference Architecture 5.0 for Mars][ref_nasa_dra_5_0]
- [NASA History Archives][ref_nasa_history]
- [NASA International Space Station Documentation][ref_nasa_iss]
- [NASA Mars Exploration Program][ref_nasa_mars_program]
- [NASA Mars Science Documentation][ref_nasa_science_mars]
- [NASA News][ref_nasa_news]
- [NASA Orbital Debris Mitigation Standard Practices][ref_nasa_orbital_debris_mitigation]
- [NASA Orbital Debris Program Office][ref_nasa_orbital_debris]
- [NASA Program and Project Life Cycle Requirements NPR 7120.5F][ref_nasa_npr_7120_5f]
- [NASASpaceflight Coverage][ref_nasaspaceflight]
- [Nasdaq Listing Rules][ref_nasdaq_listing_rules]
- [National Bureau of Economic Research][ref_nber]
- [New York Times][ref_nyt]
- [Northrop Grumman Press Releases][ref_northrop_grumman_press]
- [NYSE Listed Company Manual][ref_nyse_listed_company_manual]
- [OECD Principles of Corporate Governance][ref_oecd_corporate_governance]
- [OneWeb Corporate Record][ref_oneweb]
- [Payload Newsletter][ref_payload]
- [Payload Research][ref_payload_research]
- [PitchBook Transaction Data][ref_pitchbook]
- [Polaris Program][ref_polaris_program]
- [Public Administration Review][ref_public_admin_review]
- [Rocket Lab Press Releases][ref_rocket_lab_press]
- [S&P Dow Jones Indices][ref_spdji]
- [SEC EDGAR Company Search][ref_sec_edgar]
- [SEC Investor Education Materials][ref_sec_investor_gov]
- [SEC Regulation S-K Disclosure Requirements][ref_sec_regulation_sk]
- [Social Science Research Network][ref_ssrn]
- [Space Act Agreement Authority 51 USC 20113][ref_51_usc_20113]
- [Space Capital Quarterly Reports][ref_space_capital]
- [Space Force National Security Space Launch][ref_space_force_nssl]
- [Space Policy Online][ref_space_policy_online]
- [SpaceNews][ref_spacenews]
- [SpaceX Better Than Nothing Beta Press October 2020][ref_spacex_press_beta_2020]
- [SpaceX Corporate Site][ref_spacex_company]
- [SpaceX Falcon 9 Vehicle Documentation][ref_spacex_falcon9_vehicle]
- [SpaceX Falcon Heavy Vehicle Documentation][ref_spacex_falcon_heavy_vehicle]
- [SpaceX News Archive][ref_spacex_news_archive]
- [SpaceX Press Release Block 5 Bangabandhu-1 May 2018][ref_spacex_press_block5_bangabandhu_2018]
- [SpaceX Press Release Falcon 9 First Landing December 2015][ref_spacex_press_falcon9_first_landing_2015]
- [SpaceX Press Release Falcon Heavy First Flight February 2018][ref_spacex_press_falcon_heavy_2018]
- [SpaceX Press Release SES-10 First Refly March 2017][ref_spacex_press_ses10_2017]
- [SpaceX Press Release Starlink First 60 Operational Satellites May 2019][ref_spacex_press_starlink_v0_9_2019]
- [SpaceX Press Release Tintin A and B February 2018][ref_spacex_press_tintin_2018]
- [SpaceX Seattle Facility Announcement January 2015][ref_spacex_seattle_announcement_2015]
- [SpaceX Starlink Program Page][ref_spacex_starlink]
- [SpaceX Starshield Product Page][ref_spacex_starshield]
- [SpaceX Starship Program Page][ref_spacex_starship_program]
- [Standard Oil Dissolution Supreme Court Decision 1911][ref_standard_oil_1911]
- [Stanford Graduate School of Business SpaceX Case][ref_stanford_spacex_case]
- [Starlink Direct to Cell][ref_starlink_direct_to_cell]
- [Starlink Technology][ref_starlink_technology]
- [Texas Business Organizations Code][ref_texas_boc]
- [The Conference Board][ref_conference_board]
- [The Space Review][ref_the_space_review]
- [U S Commercial Space Launch Competitiveness Act 2015][ref_uscsla_2015]
- [United Kingdom Companies Act 2006][ref_uk_companies_act_2006]
- [United Launch Alliance Press Releases][ref_ula_press]
- [United Nations Liability Convention 1972][ref_un_liability_convention_1972]
- [United Nations Outer Space Treaty 1967][ref_un_outer_space_treaty_1967]
- [United Nations Registration Convention 1976][ref_un_registration_convention_1976]
- [United States Bankruptcy Code Chapter 11][ref_bankruptcy_code_ch11]
- [United States Bankruptcy Courts][ref_uscourts_bankruptcy]
- [USAspending Federal Award Data][ref_usaspending]
- [Vandenberg SLC-4E Environmental Assessment][ref_vandenberg_slc4e_ea]
- [Wall Street Journal][ref_wsj]
- [Wharton SpaceX Case][ref_wharton_spacex_case]

### Research

- [Abernathy and Clark 1985 Innovation Mapping the Winds of Creative Destruction][research_abernathy_clark_1985]
- [Adilov Alexander and Cunningham 2014 An Economic Analysis of Earth Orbit Pollution][research_adilov_et_al_2014]
- [Anderson and Tushman 1990 Technological Discontinuities and Dominant Designs][research_anderson_tushman_1990]
- [Arrow 1962 Economic Welfare and the Allocation of Resources for Invention][research_arrow_1962]
- [Arthur 1989 Competing Technologies Increasing Returns and Lock-In by Historical Events][research_arthur_1989]
- [Bajari and Tadelis 2001 Incentives Versus Transaction Costs A Theory of Procurement Contracts][research_bajari_tadelis_2001]
- [Barney 1991 Firm Resources and Sustained Competitive Advantage][research_barney_1991]
- [Bebchuk and Kastiel 2017 The Untenable Case for Perpetual Dual-Class Stock][research_bebchuk_kastiel_2017]
- [Bebchuk Kraakman and Triantis 2000 Stock Pyramids Cross-Ownership and Dual Class Equity][research_bebchuk_kraakman_triantis_2000]
- [Bonvillian 2018 DARPA and the Advanced Research Projects Agency][research_bonvillian_2018]
- [Boudreau 2010 Open Platform Strategies and Innovation][research_boudreau_2010]
- [Bower and Christensen 1995 Disruptive Technologies Catching the Wave][research_bower_christensen_1995]
- [Bresnahan and Trajtenberg 1995 General Purpose Technologies Engines of Growth][research_bresnahan_trajtenberg_1995]
- [Christensen and Rosenbloom 1995 Explaining the Attackers Advantage][research_christensen_rosenbloom_1995]
- [Coase 1937 The Nature of the Firm][research_coase_1937]
- [Cohen and Levinthal 1990 Absorptive Capacity A New Perspective on Learning and Innovation][research_cohen_levinthal_1990]
- [Corts and Singh 2004 The Effect of Relationships on the Nature of Contracts][research_corts_singh_2004]
- [David 1985 Clio and the Economics of QWERTY][research_david_1985]
- [DeAngelo and DeAngelo 1985 Managerial Ownership of Voting Rights][research_deangelo_deangelo_1985]
- [Dosi 1988 Sources Procedures and Microeconomic Effects of Innovation][research_dosi_1988]
- [Eisenhardt and Martin 2000 Dynamic Capabilities What Are They][research_eisenhardt_martin_2000]
- [Evans 2003 The Antitrust Economics of Multi-Sided Platform Markets][research_evans_2003]
- [Fama and Jensen 1983 Separation of Ownership and Control][research_fama_jensen_1983]
- [Farrell and Saloner 1985 Standardization Compatibility and Innovation][research_farrell_saloner_1985]
- [Finkelstein and Sanford 2000 Learning from Corporate Mistakes Iridium][research_finkelstein_sanford_2000]
- [Freeman and Soete 1997 The Economics of Industrial Innovation][research_freeman_soete_1997]
- [Gagnepain and Ivaldi 2002 Incentive Regulatory Policies][research_gagnepain_ivaldi_2002]
- [Gawer 2014 Bridging Differing Perspectives on Technological Platforms][research_gawer_2014]
- [Gawer and Cusumano 2014 Industry Platforms and Ecosystem Innovation][research_gawer_cusumano_2014]
- [Gompers Ishii and Metrick 2003 Corporate Governance and Equity Prices][research_gompers_ishii_metrick_2003]
- [Grant 1996 Toward a Knowledge-Based Theory of the Firm][research_grant_1996]
- [Griliches 1979 Issues in Assessing the Contribution of R and D to Productivity Growth][research_griliches_1979]
- [Grossman and Hart 1986 The Costs and Benefits of Ownership][research_grossman_hart_1986]
- [Grossman and Hart 1988 One Share-One Vote and the Market for Corporate Control][research_grossman_hart_1988]
- [Hagiu and Wright 2015 Multi-Sided Platforms][research_hagiu_wright_2015]
- [Harris and Raviv 1988 Corporate Governance Voting Rights and Majority Rules][research_harris_raviv_1988]
- [Hart 1988 Incomplete Contracts and the Theory of the Firm][research_hart_1988]
- [Hart and Moore 1990 Property Rights and the Nature of the Firm][research_hart_moore_1990]
- [Helfat and Peteraf 2003 The Dynamic Resource-Based View][research_helfat_peteraf_2003]
- [Henderson and Clark 1990 Architectural Innovation The Reconfiguration of Existing Product Technologies][research_henderson_clark_1990]
- [Hertzfeld 2002 Measuring the Economic Returns from Successful NASA Life Sciences Technology Transfer][research_hertzfeld_2002]
- [Jacobides Cennamo and Gawer 2018 Towards a Theory of Ecosystems][research_jacobides_et_al_2018]
- [Jensen 1986 Agency Costs of Free Cash Flow Corporate Finance and Takeovers][research_jensen_1986]
- [Katz and Shapiro 1985 Network Externalities Competition and Compatibility][research_katz_shapiro_1985]
- [Khan 2017 Amazon's Antitrust Paradox][research_khan_2017]
- [Klein Crawford and Alchian 1978 Vertical Integration Appropriable Rents and the Competitive Contracting Process][research_klein_crawford_alchian_1978]
- [Klepper 1996 Entry Exit Growth and Innovation over the Product Life Cycle][research_klepper_1996]
- [Kogut and Zander 1992 Knowledge of the Firm Combinative Capabilities and the Replication of Technology][research_kogut_zander_1992]
- [Krueger 1974 The Political Economy of the Rent-Seeking Society][research_krueger_1974]
- [La Porta Lopez-de-Silanes Shleifer and Vishny 1998 Law and Finance][research_laporta_et_al_1998]
- [Lafontaine and Slade 2007 Vertical Integration and Firm Boundaries The Evidence][research_lafontaine_slade_2007]
- [Levin and Tadelis 2010 Contracting for Government Services Theory and Evidence][research_levin_tadelis_2010]
- [Levitt and March 1988 Organizational Learning][research_levitt_march_1988]
- [Manne 1965 Mergers and the Market for Corporate Control][research_manne_1965]
- [March 1991 Exploration and Exploitation in Organizational Learning][research_march_1991]
- [Monteverde and Teece 1982 Supplier Switching Costs and Vertical Integration in the Automobile Industry][research_monteverde_teece_1982]
- [Myerson 1981 Optimal Auction Design][research_myerson_1981]
- [Nelson 1959 The Simple Economics of Basic Scientific Research][research_nelson_1959]
- [Parker and Van Alstyne 2005 Two-Sided Network Effects A Theory of Information Product Design][research_parker_vanalstyne_2005]
- [Pavitt 1984 Sectoral Patterns of Technical Change][research_pavitt_1984]
- [Peteraf 1993 The Cornerstones of Competitive Advantage][research_peteraf_1993]
- [Rochet and Tirole 2003 Platform Competition in Two-Sided Markets][research_rochet_tirole_2003]
- [Rochet and Tirole 2006 Two-Sided Markets A Progress Report][research_rochet_tirole_2006]
- [Romer 1990 Endogenous Technological Change][research_romer_1990]
- [Rysman 2009 The Economics of Two-Sided Markets][research_rysman_2009]
- [Shleifer and Vishny 1997 A Survey of Corporate Governance][research_shleifer_vishny_1997]
- [Stigler 1971 The Theory of Economic Regulation][research_stigler_1971]
- [Teece 1986 Profiting from Technological Innovation][research_teece_1986]
- [Teece 2007 Explicating Dynamic Capabilities The Nature and Microfoundations of Sustainable Enterprise Performance][research_teece_2007]
- [Teece 2018 Profiting from Innovation in the Digital Economy][research_teece_2018]
- [Teece Pisano Shuen 1997 Dynamic Capabilities and Strategic Management][research_teece_pisano_shuen_1997]
- [Weeden and Chow 2012 Taking a Common-Pool Resources Approach to Space Sustainability][research_weeden_chow_2012]
- [Weinzierl 2018 Space the Final Economic Frontier][research_weinzierl_2018]
- [Wernerfelt 1984 A Resource-Based View of the Firm][research_wernerfelt_1984]
- [Williamson 1971 The Vertical Integration of Production Market Failure Considerations][research_williamson_1971]
- [Williamson 2002 The Theory of the Firm as Governance Structure][research_williamson_2002]
- [Winter 2003 Understanding Dynamic Capabilities][research_winter_2003]
- [Zimmerman 2011 Economics of Satellite Communications][research_zimmerman_2011]

### Related Post

- [A90 Introduction to Space Studies][related_post_a90_intro_space_studies]
- [A96 History of Rocketplanes][related_post_a96_history_rocketplanes]
- [A97 What Does the United States Space Force Do][related_post_a97_us_space_force]
- [A140 Money Behind an SBIR or STTR Award][related_post_a140_sbir_money]
- [A161 What a Patent Is and Is Not][related_post_a161_patent_intro]
- [A164 Patents Trade Secrets and the Disclosure Tradeoff][related_post_a164_patents_trade_secrets]
- [A167 Why Startups Actually Fail][related_post_a167_startup_failure]
- [A237 Framing and the Co-Development Mechanism][related_post_a237_aerospace_framing]
- [A246 Silicon Valley from Defense Contracting][related_post_a246_silicon_valley_defense]
- [A248 Contemporary Snapshot and Extrapolation][related_post_a248_contemporary_snapshot]
- [A281 History of SpaceX Series Framing and the Seven-Plus-Three Forcing-Function Framework][related_post_a281_spacex_framing]
- [A282 History of SpaceX Value Gradient from Falcon 1 to Falcon 9 to Reusability][related_post_a282_spacex_value_gradient]
- [A283 History of SpaceX Anchor Demand from COTS-1 Salvation Through Commercial Crew, HLS, and Starshield][related_post_a283_spacex_anchor_demand]
- [A284 History of SpaceX Value Capture from Launch-Service Pricing and Vertical Integration into Starlink][related_post_a284_spacex_value_capture]
- [A285 History of SpaceX Decomposability of Falcon, Dragon, Heavy, and Starship as Independently Valuable Rungs][related_post_a285_spacex_decomposability]
- [A286 History of SpaceX Generality-Forcing from Mars Requirements as a Cross-Domain Capability Substrate][related_post_a286_spacex_generality_forcing]
- [A287 History of SpaceX Governance That Resists Capital Capture Across Thirty-Plus Funding Rounds][related_post_a287_spacex_governance]
- [A288 History of SpaceX Portfolio Patience and the Internalization of Tail Risk][related_post_a288_spacex_portfolio_patience]
- [A289 History of SpaceX The Government-Anchor Capital-Formation Leg and Non-Dilutive Development Finance][related_post_a289_spacex_government_anchor_leg]
- [A290 History of SpaceX The Patient-Private Capital-Formation Leg and the Manufacture of Patience][related_post_a290_spacex_patient_private_leg]

[book_acemoglu_robinson_2012]: https://openlibrary.org/search?q=Acemoglu+and+Robinson+Why+Nations+Fail
[book_amsden_1989]: https://global.oup.com/academic/product/asias-next-giant-9780195076035
[book_bain_1968]: https://openlibrary.org/search?q=Bain+Industrial+Organization+1968
[book_beinhocker_2006]: https://www.hbsp.harvard.edu/product/5062-HBK-ENG
[book_berger_2021]: https://williammorrow.com/liftoff-eric-berger/
[book_berger_2024]: https://williammorrow.com/reentry-eric-berger/
[book_berle_means_1932]: https://www.routledge.com/The-Modern-Corporation-and-Private-Property/Berle-Means/p/book/9780887388873
[book_bijker_1995]: https://mitpress.mit.edu/9780262522274/of-bicycles-bakelites-and-bulbs/
[book_bijker_hughes_pinch_1987]: https://mitpress.mit.edu/9780262521376/the-social-construction-of-technological-systems/
[book_bilstein_1996]: https://ntrs.nasa.gov/search?q=Stages+to+Saturn+Bilstein
[book_bork_1978]: https://www.hup.harvard.edu/books/9780674032545
[book_chandler_1977]: https://www.hup.harvard.edu/books/9780674940529
[book_chandler_1990]: https://openlibrary.org/search?q=Chandler+Scale+and+Scope
[book_chang_2002]: https://www.penguin.co.uk/books/56082/kicking-away-the-ladder/9780857281050
[book_chernow_2004]: https://openlibrary.org/search?q=Chernow+Titan
[book_christensen_1997]: https://www.hbsp.harvard.edu/product/1130-HBK-ENG
[book_christensen_raynor_2003]: https://www.hbsp.harvard.edu/product/3595-HBK-ENG
[book_cusumano_gawer_2002]: https://www.hbsp.harvard.edu/product/6155-HBK-ENG
[book_cyert_march_1963]: https://openlibrary.org/search?q=Cyert+March+Behavioral+Theory+Firm
[book_davenport_2018]: https://www.hachettebookgroup.com/titles/christian-davenport/the-space-barons/9781610398299/
[book_devries_vanderwoude_1997]: https://www.cambridge.org/9780521578257
[book_easterbrook_fischel_1991]: https://www.hup.harvard.edu/books/9780674235397
[book_evans_1995]: https://press.princeton.edu/books/paperback/9780691037363/embedded-autonomy
[book_fernholz_2018]: https://www.hachettebookgroup.com/titles/tim-fernholz/rocket-billionaires/9781328662231/
[book_fligstein_2001]: https://press.princeton.edu/books/paperback/9780691102542/the-architecture-of-markets
[book_gertner_2012]: https://www.penguinrandomhouse.com/books/206061/the-idea-factory-by-jon-gertner/
[book_grief_2006]: https://www.cambridge.org/9780521671347
[book_grimsey_lewis_2004]: https://www.e-elgar.com/shop/gbp/public-private-partnerships-9781840647112.html
[book_handberg_1994]: https://openlibrary.org/search?q=Handberg+Reinventing+NASA
[book_hansmann_1996]: https://www.hup.harvard.edu/books/9780674001718
[book_heppenheimer_1999]: https://www.si.edu/object/space-shuttle-decision%3Anmah_1197080
[book_hiltzik_1999]: https://openlibrary.org/search?q=Hiltzik+Dealers+of+Lightning
[book_ho_2009]: https://www.dukeupress.edu/liquidated
[book_hovenkamp_2005]: https://openlibrary.org/search?q=Hovenkamp+The+Antitrust+Enterprise
[book_hughes_1983]: https://jhupbooks.press.jhu.edu/title/networks-power
[book_iansiti_levien_2004]: https://www.hbsp.harvard.edu/product/5219-HBK-ENG
[book_isaacson_2023]: https://www.simonandschuster.com/books/Elon-Musk/Walter-Isaacson/9781982181284
[book_johnson_1982]: https://www.sup.org/books/title/?id=2143
[book_kahn_1988]: https://mitpress.mit.edu/9780262610520/the-economics-of-regulation/
[book_kearns_nadler_1992]: https://openlibrary.org/search?q=Kearns+Nadler+Prophets+Dark
[book_krippner_2011]: https://www.hup.harvard.edu/books/9780674066199
[book_laffont_tirole_1993]: https://mitpress.mit.edu/9780262121743/a-theory-of-incentives-in-procurement-and-regulation/
[book_landes_1969]: https://www.cambridge.org/9780521094184
[book_lane_1934]: https://jhupbooks.press.jhu.edu/title/venetian-ships-and-shipbuilders-renaissance
[book_latour_1987]: https://www.hup.harvard.edu/books/9780674792913
[book_launius_2004]: https://global.oup.com/academic/product/frontiers-of-space-exploration-9780313325243
[book_levin_2010]: https://openlibrary.org/search?q=Levin+Wires+That+Bind
[book_lipsey_carlaw_bekar_2005]: https://global.oup.com/academic/product/economic-transformations-9780199290895
[book_logsdon_1970]: https://mitpress.mit.edu/9780262620109/the-decision-to-go-to-the-moon/
[book_mackenzie_1990]: https://mitpress.mit.edu/9780262631471/inventing-accuracy/
[book_mackenzie_2006]: https://mitpress.mit.edu/9780262633673/an-engine-not-a-camera/
[book_march_simon_1958]: https://www.wiley.com/en-us/Organizations%2C+2nd+Edition-p-9780631186311
[book_mcafee_mcmillan_1988]: https://openlibrary.org/search?q=McAfee+and+McMillan+Incentives+in+Government+Contracting
[book_mccurdy_1994]: https://jhupbooks.press.jhu.edu/title/inside-nasa
[book_mcdougall_1985]: https://jhupbooks.press.jhu.edu/title/heavens-and-earth
[book_metcalfe_1998]: https://www.routledge.com/Evolutionary-Economics-and-Creative-Destruction/Metcalfe/p/book/9780415158671
[book_milgrom_2004]: https://www.cambridge.org/9780521551847
[book_mindell_2008]: https://mitpress.mit.edu/9780262516105/digital-apollo/
[book_mowery_rosenberg_1998]: https://www.cambridge.org/9780521645126
[book_nelson_1993]: https://global.oup.com/academic/product/national-innovation-systems-9780195076172
[book_nelson_winter_1982]: https://www.hup.harvard.edu/books/9780674272286
[book_neufeld_1995]: https://openlibrary.org/search?q=Neufeld+The+Rocket+and+the+Reich
[book_nevins_1954]: https://openlibrary.org/search?q=Nevins+Ford+The+Times+The+Man+The+Company
[book_newhouse_1982]: https://openlibrary.org/search?q=Newhouse+The+Sporty+Game
[book_newhouse_2007]: https://us.macmillan.com/books/9781400079131/boeingversusairbus
[book_north_1990]: https://www.cambridge.org/9780521397346
[book_nye_1990]: https://mitpress.mit.edu/9780262640305/electrifying-america/
[book_nye_1998]: https://mitpress.mit.edu/9780262640503/consuming-power/
[book_ostrom_1990]: https://www.cambridge.org/9780521405997
[book_penrose_1959]: https://global.oup.com/academic/product/the-theory-of-the-growth-of-the-firm-9780199573844
[book_perez_2002]: https://www.edwardelgar.com/shop/gbp/technological-revolutions-and-financial-capital-9781843763314.html
[book_perrow_1984]: https://press.princeton.edu/books/paperback/9780691004129/normal-accidents
[book_posner_2001]: https://openlibrary.org/search?q=Posner+Antitrust+Law
[book_preda_2009]: https://openlibrary.org/search?q=Preda+Framing+Finance
[book_robins_2006]: https://www.pluto.co.uk/9780745325248/the-corporation-that-changed-the-world/
[book_roe_1994]: https://press.princeton.edu/books/paperback/9780691026312/strong-managers-weak-owners
[book_ruttan_2006]: https://global.oup.com/academic/product/is-war-necessary-for-economic-growth-9780195188042
[book_scherer_ross_1990]: https://openlibrary.org/search?q=Scherer+Ross+Industrial+Market+Structure
[book_selznick_1949]: https://www.ucpress.edu/book/9780520000384/tva-and-the-grass-roots
[book_serling_1992]: https://openlibrary.org/search?q=Serling+Legend+and+Legacy
[book_sharkey_1982]: https://www.cambridge.org/9780521271943
[book_simon_1957]: https://www.simonandschuster.com/books/Administrative-Behavior-4th-Edition/Herbert-A-Simon/9781439136218
[book_sobel_1995]: https://www.bloomsbury.com/us/longitude-9780802715296/
[book_srnicek_2017]: https://www.wiley.com/en-us/Platform+Capitalism-p-9781509504879
[book_steensgaard_1974]: https://openlibrary.org/search?q=Steensgaard+The+Asian+Trade+Revolution+of+the+Seventeenth+Century
[book_stern_2011]: https://global.oup.com/academic/product/the-company-state-9780195393736
[book_temin_galambos_1987]: https://openlibrary.org/search?q=Temin+Galambos+Fall+Bell+System
[book_tirole_1988]: https://mitpress.mit.edu/9780262200714/the-theory-of-industrial-organization/
[book_utterback_1994]: https://www.hbsp.harvard.edu/product/4855-HBK-ENG
[book_vanalstyne_parker_choudary_2016]: https://wwnorton.com/books/Platform-Revolution/
[book_vance_2015]: https://www.harpercollins.com/products/elon-musk-ashlee-vance
[book_vaughan_1996]: https://press.uchicago.edu/ucp/books/book/chicago/C/bo22781921.html
[book_wade_1990]: https://press.princeton.edu/books/paperback/9780691117294/governing-the-market
[book_weick_1979]: https://www.mheducation.com/highered/product/social-psychology-organizing-weick/M9780075548089.html
[book_weick_sutcliffe_2007]: https://openlibrary.org/search?q=Weick+and+Sutcliffe+Managing+the+Unexpected
[book_williamson_1985]: https://www.simonandschuster.com/books/The-Economic-Institutions-of-Capitalism/Oliver-E-Williamson/9780684863740
[book_woo_cumings_1999]: https://www.cornellpress.cornell.edu/book/9780801485664/the-developmental-state/
[book_wu_2010]: https://openlibrary.org/search?q=Wu+The+Master+Switch
[book_yescombe_2007]: https://www.sciencedirect.com/book/9780750680547/public-private-partnerships
[book_zaloom_2006]: https://openlibrary.org/search?q=Zaloom+Out+of+the+Pits
[book_zuboff_2019]: https://www.hachettebookgroup.com/titles/shoshana-zuboff/the-age-of-surveillance-capitalism/9781610395694/
[ref_51_usc_20113]: https://www.law.cornell.edu/uscode/text/51/20113
[ref_aiaa_jpp]: https://arc.aiaa.org/journal/jpp
[ref_aiaa_jsr]: https://arc.aiaa.org/journal/jsr
[ref_alphabet_ir]: https://abc.xyz/investor/
[ref_aon_space_insurance]: https://www.aon.com/
[ref_arianegroup_press]: https://www.arianegroup.com/en/news/press-releases/
[ref_arianespace]: https://www.arianespace.com/
[ref_arstechnica_space]: https://arstechnica.com/science/space/
[ref_att_consent_decree_1956]: https://www.corp.att.com/history/nethistory/consent-decree.html
[ref_att_divestiture_1984]: https://www.corp.att.com/history/nethistory/divestiture.html
[ref_aviation_week]: https://aviationweek.com/
[ref_bankruptcy_code_ch11]: https://www.law.cornell.edu/uscode/text/11/chapter-11
[ref_berkshire]: https://www.berkshirehathaway.com/
[ref_bloomberg]: https://www.bloomberg.com/
[ref_blue_origin_press]: https://www.blueorigin.com/news/
[ref_boeing_press]: https://boeing.mediaroom.com/
[ref_breaking_defense]: https://breakingdefense.com/
[ref_bryce_tech]: https://brycetech.com/reports
[ref_china_commercial_space]: https://spacenews.com/topic/china/
[ref_chinese_space_program]: https://www.cnsa.gov.cn/english/
[ref_cii]: https://www.cii.org/
[ref_conference_board]: https://www.conference-board.org/
[ref_congressional_record]: https://www.congress.gov/congressional-record
[ref_csla_1984]: https://www.law.cornell.edu/uscode/text/51/subtitle-V/chapter-509
[ref_csla_amendments_2004]: https://www.congress.gov/108/plaws/publ492/PLAW-108publ492.pdf
[ref_defense_news]: https://www.defensenews.com/
[ref_delaware_chancery]: https://courts.delaware.gov/chancery/
[ref_dgcl]: https://delcode.delaware.gov/title8/c001/
[ref_dod_contracts]: https://www.defense.gov/News/Contracts/
[ref_dod_other_transactions]: https://aida.mitre.org/ota/
[ref_ecgi]: https://www.ecgi.global/
[ref_european_spaceflight]: https://europeanspaceflight.com/
[ref_eutelsat_oneweb]: https://www.eutelsat.com/
[ref_faa_ast]: https://www.faa.gov/space
[ref_faa_ast_licensing_regs_450]: https://www.ecfr.gov/current/title-14/chapter-III/subchapter-C/part-450
[ref_faa_ast_regulations]: https://www.ecfr.gov/current/title-14/chapter-III
[ref_faa_financial_responsibility]: https://www.ecfr.gov/current/title-14/part-440
[ref_faa_starship_pea]: https://www.faa.gov/space/stakeholder_engagement/spacex_starship
[ref_fasb_asc280]: https://www.fasb.org/
[ref_fcc_direct_to_cell_2024]: https://docs.fcc.gov/public/attachments/DA-24-208A1.pdf
[ref_fcc_filings]: https://www.fcc.gov/wireless/systems-utilities/electronic-comment-filing-system-ecfs
[ref_fcc_starlink_2018]: https://docs.fcc.gov/public/attachments/FCC-18-38A1.pdf
[ref_fcc_starlink_gen2_2022]: https://docs.fcc.gov/public/attachments/FCC-22-91A1.pdf
[ref_fpds]: https://www.fpds.gov/
[ref_ftse_russell]: https://www.lseg.com/en/ftse-russell
[ref_harvard_corpgov_forum]: https://corpgov.law.harvard.edu/
[ref_hbs_spacex_case]: https://www.hbs.edu/faculty/Pages/item.aspx?num=54001
[ref_house_science_committee_hearings]: https://science.house.gov/
[ref_iadc_guidelines]: https://www.iadc-home.org/
[ref_ibm_archives]: https://www.ibm.com/history/
[ref_incose_handbook]: https://www.incose.org/products-and-publications/se-handbook
[ref_iridium_chapter_11_1999]: https://www.sec.gov/Archives/edgar/data/1029074/0000912057-99-034228.txt
[ref_iridium_press_archive_1998]: https://www.iridium.com/
[ref_isro_press]: https://www.isro.gov.in/
[ref_itar_22_cfr_120_130]: https://www.ecfr.gov/current/title-22/chapter-I/subchapter-M
[ref_iter_organization]: https://www.iter.org/
[ref_itu_radio_regulations_2020]: https://www.itu.int/pub/R-REG-RR
[ref_jaxa_press]: https://global.jaxa.jp/press/
[ref_journal_public_procurement]: https://www.emerald.com/insight/publication/issn/1535-0118
[ref_ksc_lc39a_lease]: https://www.nasa.gov/kennedy/
[ref_lloyds_market]: https://www.lloyds.com/
[ref_meta_ir]: https://investor.atmeta.com/
[ref_musk_iac_2017]: https://arc.aiaa.org/doi/10.1089/space.2018.29013.emu
[ref_nasa_dra_5_0]: https://ntrs.nasa.gov/citations/20090012109
[ref_nasa_history]: https://history.nasa.gov/
[ref_nasa_iss]: https://www.nasa.gov/international-space-station/
[ref_nasa_mars_program]: https://mars.nasa.gov/
[ref_nasa_news]: https://www.nasa.gov/news/
[ref_nasa_npr_7120_5f]: https://nodis3.gsfc.nasa.gov/npg_img/N_PR_7120_005F_/N_PR_7120_005F_.pdf
[ref_nasa_orbital_debris]: https://orbitaldebris.jsc.nasa.gov/
[ref_nasa_orbital_debris_mitigation]: https://orbitaldebris.jsc.nasa.gov/mitigation/
[ref_nasa_science_mars]: https://science.nasa.gov/mars/
[ref_nasaspaceflight]: https://www.nasaspaceflight.com/
[ref_nasdaq_listing_rules]: https://listingcenter.nasdaq.com/rulebook/nasdaq/rules
[ref_nber]: https://www.nber.org/
[ref_northrop_grumman_press]: https://news.northropgrumman.com/
[ref_nyse_listed_company_manual]: https://nyseguide.srorules.com/listed-company-manual
[ref_nyt]: https://www.nytimes.com/section/science/space
[ref_oecd_corporate_governance]: https://www.oecd.org/corporate/principles-corporate-governance/
[ref_oneweb]: https://oneweb.net/
[ref_payload]: https://payloadspace.com/
[ref_payload_research]: https://payloadspace.com/research/
[ref_pitchbook]: https://pitchbook.com/
[ref_polaris_program]: https://polarisprogram.com/
[ref_public_admin_review]: https://onlinelibrary.wiley.com/journal/15406210
[ref_rocket_lab_press]: https://www.rocketlabusa.com/updates/
[ref_sec_edgar]: https://www.sec.gov/edgar/searchedgar/companysearch
[ref_sec_investor_gov]: https://www.investor.gov/
[ref_sec_regulation_sk]: https://www.ecfr.gov/current/title-17/part-229
[ref_space_capital]: https://www.spacecapital.com/
[ref_space_force_nssl]: https://www.spaceforce.mil/News/Fact-Sheets
[ref_space_policy_online]: https://spacepolicyonline.com/
[ref_spacenews]: https://spacenews.com/
[ref_spacex_company]: https://www.spacex.com/
[ref_spacex_falcon9_vehicle]: https://www.spacex.com/vehicles/falcon-9/
[ref_spacex_falcon_heavy_vehicle]: https://www.spacex.com/vehicles/falcon-heavy/
[ref_spacex_news_archive]: https://www.spacex.com/updates/
[ref_spacex_press_beta_2020]: https://www.spacex.com/updates/
[ref_spacex_press_block5_bangabandhu_2018]: https://www.spacex.com/updates/
[ref_spacex_press_falcon9_first_landing_2015]: https://www.spacex.com/news/2015/12/22/orbcomm-2-mission-successful-first-landing-orbital-rocket
[ref_spacex_press_falcon_heavy_2018]: https://www.spacex.com/news/2018/02/06/successful-first-flight-falcon-heavy
[ref_spacex_press_ses10_2017]: https://www.spacex.com/news/2017/03/30/spacex-successfully-launches-first-reused-rocket
[ref_spacex_press_starlink_v0_9_2019]: https://www.spacex.com/updates/
[ref_spacex_press_tintin_2018]: https://www.spacex.com/updates/
[ref_spacex_seattle_announcement_2015]: https://www.spacex.com/updates/
[ref_spacex_starlink]: https://www.starlink.com/
[ref_spacex_starshield]: https://www.spacex.com/starshield/
[ref_spacex_starship_program]: https://www.spacex.com/vehicles/starship/
[ref_spdji]: https://www.spglobal.com/spdji/en/
[ref_ssrn]: https://www.ssrn.com/
[ref_standard_oil_1911]: https://supreme.justia.com/cases/federal/us/221/1/
[ref_stanford_spacex_case]: https://www.gsb.stanford.edu/faculty-research/case-studies
[ref_starlink_direct_to_cell]: https://www.starlink.com/business/direct-to-cell
[ref_starlink_technology]: https://www.starlink.com/technology
[ref_texas_boc]: https://statutes.capitol.texas.gov/Docs/BO/htm/BO.21.htm
[ref_the_space_review]: https://www.thespacereview.com/
[ref_uk_companies_act_2006]: https://www.legislation.gov.uk/ukpga/2006/46/contents
[ref_ula_press]: https://www.ulalaunch.com/about/news
[ref_un_liability_convention_1972]: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/liability-convention.html
[ref_un_outer_space_treaty_1967]: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/outerspacetreaty.html
[ref_un_registration_convention_1976]: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/registration-convention.html
[ref_usaspending]: https://www.usaspending.gov/
[ref_uscourts_bankruptcy]: https://www.uscourts.gov/court-programs/bankruptcy
[ref_uscsla_2015]: https://www.congress.gov/114/plaws/publ90/PLAW-114publ90.pdf
[ref_vandenberg_slc4e_ea]: https://www.faa.gov/space/environmental
[ref_wharton_spacex_case]: https://knowledge.wharton.upenn.edu/
[ref_wsj]: https://www.wsj.com/tech
[related_post_a140_sbir_money]: {% post_url 2026-06-23-money_behind_an_sbir_or_sttr_award %}
[related_post_a161_patent_intro]: {% post_url 2026-05-03-what_a_patent_is_and_is_not %}
[related_post_a164_patents_trade_secrets]: {% post_url 2026-05-06-patents_trade_secrets_and_the_disclosure_tradeoff %}
[related_post_a167_startup_failure]: {% post_url 2026-05-09-why_startups_actually_fail %}
[related_post_a237_aerospace_framing]: {% post_url 2026-07-12-framing_and_the_co_development_mechanism %}
[related_post_a246_silicon_valley_defense]: {% post_url 2026-07-21-silicon_valley_from_defense_contracting %}
[related_post_a248_contemporary_snapshot]: {% post_url 2026-07-23-contemporary_snapshot_and_extrapolation %}
[related_post_a281_spacex_framing]: {% post_url 2026-07-24-spacex_history_framing %}
[related_post_a282_spacex_value_gradient]: {% post_url 2026-07-25-spacex_history_value_gradient %}
[related_post_a283_spacex_anchor_demand]: {% post_url 2026-07-26-spacex_history_anchor_demand %}
[related_post_a284_spacex_value_capture]: {% post_url 2026-07-27-spacex_history_value_capture %}
[related_post_a285_spacex_decomposability]: {% post_url 2026-07-28-spacex_history_decomposability %}
[related_post_a286_spacex_generality_forcing]: {% post_url 2026-07-29-spacex_history_generality_forcing %}
[related_post_a287_spacex_governance]: {% post_url 2026-07-30-spacex_history_governance %}
[related_post_a288_spacex_portfolio_patience]: {% post_url 2026-07-31-spacex_history_portfolio_patience %}
[related_post_a289_spacex_government_anchor_leg]: {% post_url 2026-08-01-spacex_history_government_anchor_leg %}
[related_post_a290_spacex_patient_private_leg]: {% post_url 2026-08-02-spacex_history_patient_private_leg %}
[related_post_a90_intro_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[related_post_a96_history_rocketplanes]: {% post_url 2026-02-27-history_of_rocketplanes %}
[related_post_a97_us_space_force]: {% post_url 2026-02-28-what_does_united_states_space_force_do %}
[research_abernathy_clark_1985]: https://www.sciencedirect.com/science/article/abs/pii/0048733385900217
[research_adilov_et_al_2014]: https://doi.org/10.1007/s10640-013-9758-4
[research_anderson_tushman_1990]: https://www.jstor.org/stable/2393511
[research_arrow_1962]: https://www.jstor.org/stable/2295952
[research_arthur_1989]: https://www.jstor.org/stable/2234208
[research_bajari_tadelis_2001]: https://www.jstor.org/stable/2696367
[research_barney_1991]: https://journals.sagepub.com/doi/10.1177/014920639101700108
[research_bebchuk_kastiel_2017]: https://www.virginialawreview.org/articles/untenable-case-perpetual-dual-class-stock/
[research_bebchuk_kraakman_triantis_2000]: https://www.nber.org/chapters/c9013
[research_bonvillian_2018]: https://mitpress.mit.edu/9780262038522/the-darpa-model-for-transformative-technologies/
[research_boudreau_2010]: https://pubsonline.informs.org/doi/10.1287/mnsc.1100.1215
[research_bower_christensen_1995]: https://hbr.org/1995/01/disruptive-technologies-catching-the-wave
[research_bresnahan_trajtenberg_1995]: https://www.sciencedirect.com/science/article/abs/pii/030440769401598T
[research_christensen_rosenbloom_1995]: https://www.sciencedirect.com/science/article/abs/pii/004873339400794D
[research_coase_1937]: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-0335.1937.tb00002.x
[research_cohen_levinthal_1990]: https://www.jstor.org/stable/2393553
[research_corts_singh_2004]: https://academic.oup.com/jleo/article-abstract/20/1/230/970131
[research_david_1985]: https://www.jstor.org/stable/1805621
[research_deangelo_deangelo_1985]: https://www.sciencedirect.com/science/article/abs/pii/0304405X85900436
[research_dosi_1988]: https://www.jstor.org/stable/2726526
[research_eisenhardt_martin_2000]: https://onlinelibrary.wiley.com/doi/10.1002/1097-0266%28200010/11%2921%3A10/11%3C1105%3A%3AAID-SMJ133%3E3.0.CO%3B2-E
[research_evans_2003]: https://academic.oup.com/yjolt/article/20/1/325/2379723
[research_fama_jensen_1983]: https://www.jstor.org/stable/725104
[research_farrell_saloner_1985]: https://www.jstor.org/stable/2555277
[research_finkelstein_sanford_2000]: https://doi.org/10.1016/S0090-2616(00)00020-6
[research_freeman_soete_1997]: https://mitpress.mit.edu/9780262561136/the-economics-of-industrial-innovation/
[research_gagnepain_ivaldi_2002]: https://academic.oup.com/rand/article-abstract/33/4/605/2603099
[research_gawer_2014]: https://www.sciencedirect.com/science/article/abs/pii/S0048733314001292
[research_gawer_cusumano_2014]: https://onlinelibrary.wiley.com/doi/10.1111/jpim.12105
[research_gompers_ishii_metrick_2003]: https://academic.oup.com/qje/article/118/1/107/1917017
[research_grant_1996]: https://onlinelibrary.wiley.com/doi/10.1002/smj.4250171110
[research_griliches_1979]: https://www.jstor.org/stable/3003318
[research_grossman_hart_1986]: https://www.jstor.org/stable/1833199
[research_grossman_hart_1988]: https://www.sciencedirect.com/science/article/abs/pii/0304405X88900443
[research_hagiu_wright_2015]: https://www.sciencedirect.com/science/article/pii/S0167718715000156
[research_harris_raviv_1988]: https://www.sciencedirect.com/science/article/abs/pii/0304405X88900455
[research_hart_1988]: https://www.jstor.org/stable/764953
[research_hart_moore_1990]: https://www.jstor.org/stable/2937861
[research_helfat_peteraf_2003]: https://onlinelibrary.wiley.com/doi/10.1002/smj.332
[research_henderson_clark_1990]: https://www.jstor.org/stable/2393549
[research_hertzfeld_2002]: https://www.sciencedirect.com/science/article/abs/pii/S0265964602000188
[research_jacobides_et_al_2018]: https://onlinelibrary.wiley.com/doi/10.1002/smj.2904
[research_jensen_1986]: https://www.jstor.org/stable/1818789
[research_katz_shapiro_1985]: https://www.jstor.org/stable/1814809
[research_khan_2017]: https://www.yalelawjournal.org/note/amazons-antitrust-paradox
[research_klein_crawford_alchian_1978]: https://www.jstor.org/stable/725234
[research_klepper_1996]: https://www.jstor.org/stable/2118234
[research_kogut_zander_1992]: https://pubsonline.informs.org/doi/10.1287/orsc.3.3.383
[research_krueger_1974]: https://www.jstor.org/stable/1808883
[research_lafontaine_slade_2007]: https://www.aeaweb.org/articles?id=10.1257/jel.45.3.629
[research_laporta_et_al_1998]: https://www.journals.uchicago.edu/doi/10.1086/250042
[research_levin_tadelis_2010]: https://academic.oup.com/qje/article-abstract/125/3/1103/1903637
[research_levitt_march_1988]: https://www.annualreviews.org/doi/10.1146/annurev.so.14.080188.001535
[research_manne_1965]: https://www.journals.uchicago.edu/doi/10.1086/259036
[research_march_1991]: https://pubsonline.informs.org/doi/10.1287/orsc.2.1.71
[research_monteverde_teece_1982]: https://www.jstor.org/stable/3003400
[research_myerson_1981]: https://pubsonline.informs.org/doi/10.1287/moor.6.1.58
[research_nelson_1959]: https://www.journals.uchicago.edu/doi/10.1086/258177
[research_parker_vanalstyne_2005]: https://pubsonline.informs.org/doi/10.1287/mnsc.1050.0400
[research_pavitt_1984]: https://www.sciencedirect.com/science/article/abs/pii/0048733384900215
[research_peteraf_1993]: https://onlinelibrary.wiley.com/doi/10.1002/smj.4250140303
[research_rochet_tirole_2003]: https://www.jstor.org/stable/40007911
[research_rochet_tirole_2006]: https://onlinelibrary.wiley.com/doi/10.1111/j.1756-2171.2006.tb00036.x
[research_romer_1990]: https://www.journals.uchicago.edu/doi/10.1086/261725
[research_rysman_2009]: https://www.aeaweb.org/articles?id=10.1257/jep.23.3.125
[research_shleifer_vishny_1997]: https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1997.tb04820.x
[research_stigler_1971]: https://www.jstor.org/stable/3003160
[research_teece_1986]: https://www.sciencedirect.com/science/article/abs/pii/0048733386900272
[research_teece_2007]: https://onlinelibrary.wiley.com/doi/10.1002/smj.640
[research_teece_2018]: https://www.sciencedirect.com/science/article/pii/S0048733317301993
[research_teece_pisano_shuen_1997]: https://onlinelibrary.wiley.com/doi/10.1002/%28SICI%291097-0266%28199708%2918%3A7%3C509%3A%3AAID-SMJ882%3E3.0.CO%3B2-Z
[research_weeden_chow_2012]: https://www.sciencedirect.com/science/article/abs/pii/S0265964612000513
[research_weinzierl_2018]: https://www.aeaweb.org/articles?id=10.1257/jep.32.2.173
[research_wernerfelt_1984]: https://onlinelibrary.wiley.com/doi/10.1002/smj.4250050207
[research_williamson_1971]: https://www.jstor.org/stable/1815199
[research_williamson_2002]: https://www.aeaweb.org/articles?id=10.1257/089533002760278776
[research_winter_2003]: https://onlinelibrary.wiley.com/doi/10.1002/smj.318
[research_zimmerman_2011]: https://openlibrary.org/search?q=Zimmerman+Economics+Satellite+Communications
