---
layout: post
mathjax: true
comments: true
title:  "History of SpaceX: The Category-Dominating Commercial Spinoff and the Internalization of Anchor Demand"
date:   2026-08-03 09:00:00 +0000
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

The last element is the capital-formation question and it is the reason the spinoff belongs in this series rather than in a treatment of the satellite communications industry. The two preceding legs, which the [Government-Anchor Capital-Formation Leg article A289][related_post_a289_spacex_government_anchor_leg] and the [Patient-Private Capital-Formation Leg article A290][related_post_a290_spacex_patient_private_leg] develop, both supply capital from outside the firm on terms that constrain it. The government leg supplies capital against milestones and carries a requirement. The private leg supplies capital against equity and carries a dilution. Retained earnings carry neither. The spinoff leg is therefore the only one of the three that terminates the capital-formation problem rather than managing it, and the analytically interesting question is what conditions a spinoff must satisfy to reach that scale.

The ordinary account treats the constellation as a diversification, on the reasoning that a launch company entered the telecommunications business. That account is not false and it is not an explanation, because it supplies no reason why a launch company should have any advantage in telecommunications, and absent such an advantage the diversification would destroy value for the reasons the corporate-diversification literature the [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] surveys documents at length.

The general form of the problem can be stated compactly. Let $q^{\text{internal}}$ denote the launch capacity the spinoff consumes and $q^{\text{external}}$ the capacity sold to third parties. The parent's total output satisfies

$$q^{\text{total}} = q^{\text{internal}} + q^{\text{external}}$$

with the ordinary treatment of a launch business considering only the second term. The article's position is that the first term became the larger one and that the transition is the central event in the firm's commercial history. The transition admits statement as a share crossing one half

$$s(t) = \frac{q^{\text{internal}}(t)}{q^{\text{total}}(t)} \qquad \text{with} \qquad \frac{ds}{dt} > 0 \;\; \text{and} \;\; s(t) > \tfrac{1}{2} \;\; \text{after some date}$$

with the date at which the majority of the firm's own launches served its own constellation being the point at which the launch business ceased to be primarily a merchant business. The quantity is reconstructible from public launch manifests and is one of the few claims in this article that does not depend on unpublished financial data.

The relation among the three capital-formation legs admits compact statement as a decomposition of the external requirement

$$K^{\text{external}}(t) = B(t) - K^{\text{government}}(t) - R^{\text{retained}}(t)$$

with the government term the subject of the [Government-Anchor Capital-Formation Leg article A289][related_post_a289_spacex_government_anchor_leg], the residual met by the private leg the [Patient-Private Capital-Formation Leg article A290][related_post_a290_spacex_patient_private_leg] describes, and the third term the subject of this article. The three legs are therefore not parallel alternatives but terms in a single budget identity, and the sequence in which they arrived is the sequence in which each became available.

The identification problem is the counterfactual, and it admits the compact form

$$\Delta V^{\text{spinoff}}(t) = V^{\text{observed}}(t) - V^{\text{no spinoff counterfactual}}(t)$$

with the attribution equal to the difference between the observed trajectory and the counterfactual in which the same launch capability existed and no constellation was built. The counterfactual is partially observable, because contemporaneous ventures attempted the constellation without the launch capability and the sector supplies their outcomes.

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

The cost position admits compact statement. Let $c^{\text{marginal}}$ denote the parent's marginal cost of supplying one launch and let $p^{\text{market}}$ denote the price a third party pays. The spinoff's launch cost and a competitor's launch cost stand in the relation

$$c^{\text{spinoff}} = c^{\text{marginal}} \qquad \text{against} \qquad c^{\text{competitor}} = p^{\text{market}} \geq c^{\text{marginal}} + m$$

with $m$ the parent's margin on external sales. The competitor's disadvantage per launch is therefore at least the parent's entire margin, and it is incurred on every launch of a deployment campaign requiring many of them.

The aggregate effect over a deployment campaign of $N$ launches admits the compact form

$$\Delta C = N \cdot m$$

with the disadvantage scaling linearly in the campaign size. A constellation is precisely the application in which $N$ is large, which is the structural reason the advantage matters here and would not matter for a business requiring a single launch.

The condition a competitor must satisfy to remain viable against the gap admits the compact form

$$\Pi^{\text{competitor}} > 0 \iff \left( \text{ARPU} - c^{\text{operating}} \right) \cdot n^{\text{sub}} \; > \; C^{\text{deployment}} + N \cdot m$$

with the final term the disadvantage the integrated operator does not bear. A competitor must therefore either serve more subscribers, charge more, or operate more cheaply than the integrated operator merely to reach the same margin, and it must do so while holding an identical satellite technology and an identical spectrum position. The article's position is that no contemporaneous competitor has demonstrated any of the three.

The capacity argument that motivates the arrangement admits statement as a utilization condition. A launch capability has a fixed cost of maintaining production and operations that is incurred whether or not vehicles fly. Let $\bar{q}$ denote the capacity the fixed cost sustains and $q^{\text{external}}$ the external demand. Where

$$q^{\text{external}} < \bar{q}$$

the residual capacity is idle and its marginal cost of use is low. The spinoff converts that residual into a revenue stream, and the arrangement is best understood as the monetization of a by-product rather than as an entry into a new market.

The effect on the parent's own cost structure follows directly, because a fixed cost spread across more flights falls per flight. The average cost admits the compact form

$$\bar{c}(q) = \frac{F}{q} + c^{\text{marginal}} \qquad \text{with} \qquad \frac{d\bar{c}}{dq} < 0$$

with $F$ the fixed cost of maintaining production and operations. The spinoff therefore lowers the cost at which the parent can serve its external customers as a by-product of serving itself, which is the reverse of the resource-diversion the diversification literature predicts and which the article regards as the strongest single piece of evidence that the arrangement is not a diversification.

The capital-formation function admits statement as a crossover condition. Let $R(t)$ denote the spinoff's free cash contribution and $B(t)$ the parent's mission-directed burn. The external capital requirement is

$$K^{\text{external}}(t) = \max \left\{ 0, \; B(t) - R(t) \right\}$$

and the leg closes the capital-formation problem at the date $t^{\ast}$ satisfying

$$R(t^{\ast}) \geq B(t^{\ast})$$

after which external capital becomes optional. The article's position is that the date is the single most consequential unobserved quantity in the series, because every governance and financing arrangement the preceding articles describe exists to bridge the interval before it.

## Cross-Disciplinary Framings

The commercial-spinoff property admits characterization from several disciplinary traditions beyond the mission-oriented-innovation framework the series adopts as primary.

The vertical-integration tradition traces from [Coase 1937][research_coase_1937] The Nature of the Firm through [Williamson 1971][research_williamson_1971], [Williamson 1985][book_williamson_1985] The Economic Institutions of Capitalism, [Klein Crawford and Alchian 1978][research_klein_crawford_alchian_1978], [Monteverde and Teece 1982][research_monteverde_teece_1982], and [Grossman and Hart 1986][research_grossman_hart_1986]. The framing supplies the account of when a firm should make rather than buy, and its contribution here is to identify the specific condition the case satisfies. The ordinary condition compares costs and admits the compact form

$$\text{make} \iff c^{\text{internal}} + g < p^{\text{market}}$$

with $g$ the governance cost of operating the activity inside the firm. The present case does not turn on that inequality. The constellation requires a launch cadence no external supplier could commit to at any price the programme could bear, so the relevant condition is

$$\text{make} \iff \nexists \; \text{supplier with} \; \dot{q}^{\text{available}} \geq \dot{q}^{\text{required}}$$

with the make decision following from supply unavailability rather than from a cost comparison. The distinction matters because it means the integration would have been correct even had it been more expensive than buying, which is not the case the transaction-cost literature ordinarily treats.

The appropriability tradition traces from [Teece 1986][research_teece_1986] Profiting from Technological Innovation. The framing is the most directly applicable of any in this survey. It holds that an innovator captures value only where it controls the complementary assets an innovation requires, and it identifies launch capacity as precisely such an asset for a constellation business. The captured share admits the compact form

$$\sigma^{\text{innovator}} = \sigma\!\left( \text{control of complementary assets}, \; \text{strength of the appropriability regime} \right)$$

with the value accruing to the holder of the scarce complement where the innovation itself is imitable. Satellite manufacture is imitable and launch capacity at the required cadence was not, which is the framing's explanation for where the value settled. The [Value Capture article A284][related_post_a284_spacex_value_capture] develops the general point and this article supplies the sharpest instance of it in the series.

The network-effects and standards tradition traces from [Katz and Shapiro 1985][research_katz_shapiro_1985] Network Externalities Competition and Compatibility, [Farrell and Saloner 1985][research_farrell_saloner_1985], [Arthur 1989][research_arthur_1989] Competing Technologies Increasing Returns and Lock-In, and [David 1985][research_david_1985] Clio and the Economics of QWERTY. The framing supplies the account of why a constellation business exhibits increasing returns, because coverage completeness is a step function of satellite count. The value relation admits the compact form

$$V(S) \ll \frac{S}{S^{\ast}} \cdot V(S^{\ast}) \qquad \text{for} \qquad S < S^{\ast}$$

with $S^{\ast}$ the count at which continuous coverage is attained. The convexity below the threshold is what makes the business unfinanceable against its own early revenue and is the point at which this article's subject connects to the two preceding capital-formation legs.

The two-sided-market and platform tradition traces from [Rochet and Tirole 2003][research_rochet_tirole_2003] and [Rochet and Tirole 2006][research_rochet_tirole_2006] through [Rysman 2009][research_rysman_2009], [Parker and Van Alstyne 2005][research_parker_vanalstyne_2005], [Evans 2003][research_evans_2003], [Boudreau 2010][research_boudreau_2010], [Hagiu and Wright 2015][research_hagiu_wright_2015], [Gawer 2014][research_gawer_2014], [Gawer and Cusumano 2014][research_gawer_cusumano_2014], [Jacobides Cennamo and Gawer 2018][research_jacobides_et_al_2018], with the book-length treatments at [Cusumano and Gawer 2002][book_cusumano_gawer_2002], [Iansiti and Levien 2004][book_iansiti_levien_2004], and [Van Alstyne Parker and Choudary 2016][book_vanalstyne_parker_choudary_2016]. The framing applies partially and the article marks the limit. A genuinely two-sided market exhibits a cross-side externality, admitting the compact condition

$$\frac{\partial u^{A}}{\partial n^{B}} > 0 \qquad \text{and} \qquad \frac{\partial u^{B}}{\partial n^{A}} > 0$$

with the utility of each side rising in the participation of the other. The direct-to-cell extension satisfies the condition, because it serves subscribers through carriers and the value to each rises with the other. The consumer broadband service does not, because a subscriber's service quality is weakly decreasing in the number of other subscribers sharing a cell. The broadband business is therefore an ordinary subscription business with a satellite delivery mechanism, and importing platform conclusions into it is an error the commentary makes routinely.

The regulated-industry and natural-monopoly tradition traces from [Sharkey 1982][book_sharkey_1982] The Theory of Natural Monopoly through [Kahn 1988][book_kahn_1988] The Economics of Regulation, [Stigler 1971][research_stigler_1971] The Theory of Economic Regulation, [Krueger 1974][research_krueger_1974], [Bain 1968][book_bain_1968], [Scherer and Ross 1990][book_scherer_ross_1990], and [Tirole 1988][book_tirole_1988]. The framing supplies the account of what a finite orbital and spectral resource implies. Natural monopoly in the technical sense requires cost subadditivity, admitting the compact condition

$$C\!\left( \textstyle\sum_i y_i \right) < \sum_i C(y_i)$$

for the relevant output vectors, meaning a single operator serves the market more cheaply than several. The condition plausibly holds for a constellation, because coverage must be complete regardless of subscriber count and duplicating it duplicates the entire fixed cost. The tradition is therefore the one most likely to generate the regulatory response the article's closing questions anticipate, and the article notes that the subadditivity argument is stronger here than in most industries where it is asserted.

The competition-policy tradition traces from [Bork 1978][book_bork_1978] The Antitrust Paradox through [Posner 2001][book_posner_2001], [Hovenkamp 2005][book_hovenkamp_2005], and [Khan 2017][research_khan_2017] Amazon's Antitrust Paradox. The [Khan 2017][research_khan_2017] treatment is directly relevant because it concerns a vertically integrated firm that competes with the parties who depend on its infrastructure, which is the exact structure this article describes once external launch customers and the constellation compete for the same capacity. The foreclosure incentive admits the compact statement

$$\frac{\partial \Pi^{\text{consolidated}}}{\partial q^{\text{external to a rival constellation}}} = m - \frac{\partial \Pi^{\text{constellation}}}{\partial \left( \text{rival capability} \right)}$$

with the sign ambiguous and turning on whether the margin from selling a launch exceeds the downstream harm from enabling a competitor. The article notes that the firm has in fact sold launch capacity to a rival constellation programme, which is evidence that the first term has so far dominated, and that the observation cuts against the strongest form of the foreclosure concern.

The technology-cycle tradition traces from [Abernathy and Clark 1985][research_abernathy_clark_1985] through [Anderson and Tushman 1990][research_anderson_tushman_1990], [Henderson and Clark 1990][research_henderson_clark_1990] Architectural Innovation, [Bower and Christensen 1995][research_bower_christensen_1995], [Christensen and Rosenbloom 1995][research_christensen_rosenbloom_1995], [Utterback 1994][book_utterback_1994], [Christensen 1997][book_christensen_1997], [Christensen and Raynor 2003][book_christensen_raynor_2003], and [Bresnahan and Trajtenberg 1995][research_bresnahan_trajtenberg_1995] General Purpose Technologies. The framing treats the constellation as a discontinuity in the delivery of connectivity rather than as an improvement in satellite communications. The relevant performance comparison admits the compact form

$$\ell^{\text{LEO}} \approx \frac{h^{\text{LEO}}}{h^{\text{GEO}}} \cdot \ell^{\text{GEO}} \qquad \text{with} \qquad \frac{h^{\text{LEO}}}{h^{\text{GEO}}} \sim 10^{-2}$$

with $\ell$ the propagation latency and $h$ the orbital altitude. The two-order reduction moves the service across the threshold at which interactive applications become usable, which is a discontinuity in the served application set rather than an improvement along an existing performance dimension. That is the reading which best explains why the incumbent geostationary operators, whose assets were optimized for a different point in the design space, did not respond.

The capability tradition traces from [Penrose 1959][book_penrose_1959] The Theory of the Growth of the Firm through [Teece Pisano and Shuen 1997][research_teece_pisano_shuen_1997], [Wernerfelt 1984][research_wernerfelt_1984], [Barney 1991][research_barney_1991], [Nelson and Winter 1982][book_nelson_winter_1982], and [Metcalfe 1998][book_metcalfe_1998]. The framing supplies the account of the spinoff as an application of surplus capability, which is the reading closest to the article's own.

The telecommunications-history tradition traces from [Wu 2010][book_wu_2010] The Master Switch, [Temin and Galambos 1987][book_temin_galambos_1987] The Fall of the Bell System, [Levin 2010][book_levin_2010], [Sobel 1995][book_sobel_1995], [Nye 1990][book_nye_1990] Electrifying America, and [Hughes 1983][book_hughes_1983] Networks of Power. The framing supplies the base rates and is the tradition that most consistently predicts a regulatory intervention following the attainment of a dominant position in a communications infrastructure.

The space-economics tradition traces from [Weinzierl 2018][research_weinzierl_2018] Space the Final Economic Frontier through [Hertzfeld 2002][research_hertzfeld_2002], [Adilov Alexander and Cunningham 2018][research_adilov_et_al_2018], [Weeden and Chow 2012][research_weeden_chow_2012], and [Zimmerman 2011][research_zimmerman_2011], with the policy histories at [Launius 2004][book_launius_2004], [McCurdy 1994][book_mccurdy_1994], [Logsdon 1970][book_logsdon_1970], [Handberg 1994][book_handberg_1994], [McDougall 1985][book_mcdougall_1985], and [Heppenheimer 1999][book_heppenheimer_1999].

## The January 2015 Announcement and the Capacity Argument

The constellation programme was announced in January 2015 at the event recorded in the [SpaceX Seattle announcement][ref_spacex_seattle_announcement_2015], and the announcement coincided with the financing round the [Patient-Private Capital-Formation Leg article A290][related_post_a290_spacex_patient_private_leg] treats. The coincidence is not incidental. The round supplied capital against a business line that did not yet exist, and the announcement supplied the business line against which the capital was raised.

The stated rationale at announcement was that the revenue required to fund the mission the [series opener][related_post_a281_spacex_framing] describes exceeded any plausible revenue from launch services alone. The claim is checkable in order of magnitude. The global commercial launch market at the time supported a total addressable revenue substantially below the programme cost of a Mars transportation system, whereas the global telecommunications market exceeded it by orders of magnitude. The comparison admits the compact statement

$$\text{TAM}^{\text{launch}} \ll B^{\text{mission}} \ll \text{TAM}^{\text{telecom}}$$

with the middle quantity being the mission burn the spinoff was intended to fund. The reasoning does not establish that the venture could capture any particular share of the larger market, and the article marks the distinction between the size of a market and the accessibility of it. The share the argument actually requires admits the compact form

$$\sigma^{\text{required}} = \frac{B^{\text{mission}}}{\text{TAM}^{\text{telecom}} \cdot \mu}$$

with $\mu$ the achievable margin. The quantity is small, which is what makes the argument survivable, and it is not zero, which is what makes it an argument rather than an assertion. The article's position is that a rationale of this form is checkable only in order of magnitude and that it was treated at the time as more precise than it was.

The capacity argument is the second and less frequently stated rationale, and the article regards it as the stronger of the two. By 2015 the vehicle programme the [Value Gradient article A282][related_post_a282_spacex_value_gradient] traces had produced a launch capability whose production and operations infrastructure was sized above the external demand available to it. A constellation is the application that consumes launch capacity in the largest quantity available anywhere, and it was the application most naturally matched to the specific surplus the firm held. The matching condition admits the compact statement

$$\arg\max_{a \in \mathcal{A}} \; \left[ \text{capacity consumed by application } a \right] \quad \text{subject to} \quad \text{capability already held}$$

with the constellation the maximizer over the application set the firm could reach. The formulation makes the decision look less like market entry and more like an allocation problem, which is the reading the article adopts.

## The Deployment Sequence from 2019 to 2021

The first operational batch reached orbit in May 2019 as recorded in the [first operational batch release][ref_spacex_press_starlink_v0_9_2019], following the two prototype spacecraft of 2018 recorded in the [prototype release][ref_spacex_press_tintin_2018]. Service beta began in 2020 as recorded in the [service beta release][ref_spacex_press_beta_2020], and commercial availability broadened through 2021. The consolidated programme record is at [Starlink][ref_spacex_starlink] and the technical description at the [Starlink technology page][ref_starlink_technology].

The deployment exhibits the step-function property the network-effects framing predicts. A constellation in low Earth orbit supplies continuous service to a given latitude band only once enough orbital planes are populated to guarantee that a satellite is always in view. Below that threshold the service is intermittent and substantially unsellable. The coverage condition admits the compact form

$$\text{continuous service at latitude } \lambda \iff n^{\text{planes}}(\lambda) \geq n^{\text{minimum}}(\lambda)$$

with the revenue from a partially deployed constellation being not a proportional fraction of the complete one but approximately zero until the threshold is crossed. The revenue relation is therefore a step rather than a ramp, admitting the compact form

$$R(S) = \begin{cases} \approx 0 & S < S^{\ast} \\ R^{\text{full}} \cdot \left( S / S^{\ast} \right)^{\gamma} & S \geq S^{\ast} \end{cases}$$

with $\gamma$ governing how capacity growth beyond the coverage threshold converts into further revenue. The property is the structural reason a constellation cannot be built incrementally against revenue and must be financed ahead of any income whatever, which is what connects this article to the two preceding capital-formation legs.

The threshold property also explains the deployment sequence's geographic order. A satellite in a circular orbit at inclination $i$ spends time over latitudes in proportion to the geometry, and the dwell density peaks near the turning latitudes, admitting the approximate relation

$$\text{coverage density}(\lambda) \; \propto \; \frac{1}{\sqrt{\sin^2 i - \sin^2 \lambda}} \qquad \text{for} \qquad |\lambda| < i$$

with the density rising toward $|\lambda| \to i$ and vanishing beyond it. Coverage was therefore established first at the latitudes the inclination favored and extended subsequently, so that revenue began at high northern latitudes where terrestrial broadband was poorest and the competing alternatives weakest. The commercial sequence follows from orbital geometry rather than from a market-selection decision.

## Vertical Integration and the Internal Transfer Price

The internal transfer price is the quantity on which every financial claim about the spinoff depends, and it is unobservable.

The parent supplies launch services to the spinoff and the spinoff supplies revenue to the consolidated entity. The price at which the internal transaction is recorded determines how the consolidated profit is attributed between the two, and it determines nothing about the consolidated profit itself. The identity admits the compact form

$$\Pi^{\text{consolidated}} = \Pi^{\text{launch}}\!\left( p^{\text{transfer}} \right) + \Pi^{\text{constellation}}\!\left( p^{\text{transfer}} \right) \qquad \text{with} \qquad \frac{\partial \Pi^{\text{consolidated}}}{\partial p^{\text{transfer}}} = 0$$

with the transfer price redistributing profit between the segments and leaving the total unchanged. The redistribution is exact and admits the compact statement

$$\frac{\partial \Pi^{\text{launch}}}{\partial p^{\text{transfer}}} = q^{\text{internal}} = - \frac{\partial \Pi^{\text{constellation}}}{\partial p^{\text{transfer}}}$$

with the two derivatives equal in magnitude and opposite in sign. The consequence is that any externally reported claim about the profitability of either segment separately is a claim about an accounting choice rather than about an economic fact, and the article declines to make such claims.

The observation has a sharper implication for the competitive analysis. A competitor evaluating entry compares its own launch cost against the price it observes the parent charging external customers. That price is not the cost the spinoff bears. The competitor's inference error admits the compact form

$$\hat{c}^{\text{parent}}_{\text{competitor}} = p^{\text{market}} \; > \; c^{\text{marginal}} = c^{\text{parent}}_{\text{actual}}$$

with the observable price exceeding the unobservable cost by the full margin. The competitor therefore systematically overestimates the parent's constellation cost, which means an entry decision that looks marginal on the competitor's information may be clearly unprofitable on the parent's. The [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] identifies the same transfer price as the single most consequential unobserved quantity from the portfolio side. The two articles converge on the same missing number from different directions.

The vertical structure also creates the conflict the competition-policy tradition identifies. The parent sells launch services to firms that compete with its own constellation, and the capacity it allocates internally is capacity unavailable to them. The allocation operates under a binding constraint admitting the compact form

$$q^{\text{internal}} + q^{\text{external}} \leq \bar{q} \qquad \text{with} \qquad \bar{q} \; \text{finite at any date}$$

with every internal launch displacing an external one whenever the constraint binds. The arrangement is documented in the general [SpaceX corporate record][ref_spacex_company] and no public allocation rule exists, which means the question of whether the constraint has bound and how it was resolved is unanswerable from outside the firm.

## The Launch-Cadence Coupling

The constellation and the launch business are coupled through cadence in a manner that is mutually reinforcing and that the article treats as the mechanical core of the case.

A constellation of $S$ satellites deployed in batches of $b$ per launch requires

$$N^{\text{launches}} = \left\lceil \frac{S}{b} \right\rceil$$

launches for initial deployment, and a satellite operational lifetime of $L$ years imposes a steady-state replenishment requirement of

$$\dot{N}^{\text{replenish}} = \frac{S}{b \cdot L}$$

launches per year thereafter. For a constellation of several thousand satellites at a lifetime of roughly five years, the replenishment requirement alone exceeds the entire global commercial launch cadence of the period preceding the programme, admitting the compact comparison

$$\dot{N}^{\text{replenish}} \; > \; \dot{N}^{\text{global commercial, pre-programme}}$$

with the steady-state obligation of a single constellation exceeding what the entire world launch industry had previously demonstrated. The comparison establishes that the capability had to be created rather than procured and is the quantitative form of the supply-unavailability condition the vertical-integration framing states.

The coupling runs in both directions and that is what makes it consequential. The constellation supplies the launch business with a demand stream large enough to justify the cadence, and the cadence drives the reuse experience that the [Decomposability article A285][related_post_a285_spacex_decomposability] and the [Value Gradient article A282][related_post_a282_spacex_value_gradient] identify as the source of cost reduction. The learning relationship admits the conventional form

$$c_n = c_1 \cdot n^{-\beta}$$

with $c_n$ the cost at cumulative flight $n$ and $\beta$ the learning exponent. The constellation increases $n$ faster than external demand could, which lowers $c_n$, which lowers the constellation's own cost, which improves the economics that justify further deployment. The loop admits statement as a fixed point in the deployment rate

$$\dot{N}^{\ast} = \Psi\!\left( c\big( \dot{N}^{\ast} \big) \right) \qquad \text{with} \qquad \Psi' < 0 \;\; \text{and} \;\; c' < 0$$

with the composition increasing, so that the system admits a self-reinforcing equilibrium at high cadence and low cost rather than converging to the industry's prior operating point. The structure is the mechanical core of the case and it is what the ordinary account of a launch company entering telecommunications entirely omits. The reuse record is at the [Falcon 9 vehicle page][ref_spacex_falcon9_vehicle] and the milestone sequence at the [first booster landing][ref_spacex_press_falcon9_first_landing_2015], the [first reflight][ref_spacex_press_ses10_2017], and the [Block 5 introduction][ref_spacex_press_block5_bangabandhu_2018].

The self-reinforcing structure is the strongest available argument that the spinoff was not a diversification. A diversification consumes the parent's resources. This arrangement improved the parent's core economics as a direct consequence of consuming its output.

## Service Rollout and the Subscriber Trajectory

The subscriber trajectory is reconstructed from company statements and trade-press reporting at [SpaceNews][ref_spacenews], [Ars Technica space coverage][ref_arstechnica_space], [Payload][ref_payload], [Payload Research][ref_payload_research], and [The Space Review][ref_the_space_review], and every figure carries the reconstruction caveat the Data Sources section states.

The reported trajectory rises from the beta of 2020 through successive announced milestones across the 2021 to 2025 period into the millions of subscribers, with the service available across a majority of national markets by the drafting date. The revenue relation admits the compact form

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

Satellites in low Earth orbit experience atmospheric drag and deorbit within a period substantially shorter than conventional geostationary spacecraft lifetimes. The design choice is deliberate and is what the orbital-debris regime the regulatory section describes effectively requires, but it converts the constellation from a capital asset into a consumable. The steady-state obligation admits the compact form

$$C^{\text{replenishment}} = \frac{S}{L} \cdot \left( c^{\text{satellite}} + \frac{c^{\text{launch}}}{b} \right)$$

with the whole quantity recurring annually and indefinitely. The obligation is the reason satellite production rate rather than launch rate became the binding constraint on the programme, admitting the compact statement

$$\dot{S}^{\text{production required}} = \frac{S}{L} \qquad \text{with} \qquad \dot{S}^{\text{production}} < b \cdot \dot{N}^{\text{launch capacity}}$$

with the production term the smaller of the two and therefore governing. The relation is the reason the venture built satellite manufacturing at a scale without precedent in the sector, and it inverts the sector's historical constraint, in which launch availability governed and spacecraft were produced individually.

The manufacturing achievement deserves statement in its own terms. Producing spacecraft at a rate measured in units per day rather than units per year is a discontinuity in the industry's production practice, and it follows the same learning relationship the launch business exhibits. The steady state the treadmill implies also fixes the fleet's average age, admitting the compact result

$$\bar{a} = \frac{L}{2} \qquad \text{in steady state with uniform replacement}$$

with the deployed constellation permanently averaging half a design lifetime. The property is favorable and is rarely stated, because it means the operational fleet is continuously refreshed with current-generation hardware rather than ageing toward obsolescence as a conventional geostationary fleet does. The [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats the design commonality that makes the rate attainable.

The treadmill also supplies the strongest argument against the natural-monopoly reading of the position. An incumbent whose asset base must be entirely replaced every few years cannot rest on it, and a competitor entering later deploys a newer generation against an incumbent carrying a partially obsolete fleet. The advantage admits the compact statement

$$\text{incumbency advantage} \; \sim \; \frac{L}{T^{\text{competitor deployment}}}$$

with the advantage small where the replacement interval is short relative to the time a competitor requires to deploy. The article regards this as a genuine limit on the durability of the position and as the feature most likely to be underweighted by both advocates and critics.

## The Regulatory Position Across the Commission the Union and National Regulators

The regulatory position is the second structural constraint and it operates on a resource the venture cannot manufacture.

The domestic authorization record comprises the [initial authorization][ref_fcc_starlink_2018], the [second-generation authorization][ref_fcc_starlink_gen2_2022], the [direct-to-cell proceeding][ref_fcc_direct_to_cell_2024], and the general [filing system][ref_fcc_filings]. The international coordination operates through the [International Telecommunication Union Radio Regulations][ref_itu_radio_regulations_2020], under which spectrum and orbital-slot rights are coordinated among administrations rather than allocated by any single authority. Launch licensing runs through the [Federal Aviation Administration Office of Commercial Space Transportation][ref_faa_ast]. The treaty framework comprises the [Outer Space Treaty][ref_un_outer_space_treaty_1967], the [Liability Convention][ref_un_liability_convention_1972], and the [Registration Convention][ref_un_registration_convention_1976], under which the launching state bears international responsibility for national activities.

Service in any national market requires that market's own authorization, which makes the regulatory position a per-country matter rather than a single approval. The addressable market admits the compact form

$$M^{\text{addressable}}(t) = \sum_{k \in \mathcal{J}(t)} M_k \qquad \text{with} \qquad \mathcal{J}(t) = \left\{ k : \text{authorization granted in jurisdiction } k \right\}$$

with the index set growing by administrative decision rather than by commercial effort. The consequence is that the addressable market is not the world but the union of jurisdictions that have granted access, and the difference is substantial and politically contingent.

The structure also creates a distinct category of risk that the sector's financial commentary treats poorly. An authorization is revocable, and the revenue attaching to a jurisdiction is therefore conditional, admitting the compact statement

$$\mathbb{E}\left[ R_k \right] = R_k \cdot P\!\left( \text{authorization retained} \right)$$

with the second factor a political rather than an operational quantity. The article notes that the largest single risk to the revenue base described here may be diplomatic rather than technical or competitive.

## Spectrum Priority as the Scarce Asset

The scarce asset in the constellation business is not orbital volume and is not capital. It is spectrum priority.

The coordination regime the [Radio Regulations][ref_itu_radio_regulations_2020] establishes operates on a first-filed basis subject to bring-into-use deadlines, so that an operator filing earlier and deploying on schedule obtains a protected position against later entrants, who must demonstrate non-interference with the incumbent. The priority relation admits the compact statement

$$\text{priority}_i > \text{priority}_j \iff t^{\text{filing}}_i < t^{\text{filing}}_j \; \wedge \; \text{bring-into-use satisfied}$$

with the second conjunct being the reason deployment speed carries a regulatory value independent of its commercial value. A constellation deployed quickly converts a filing into a protected right, and a constellation deployed slowly forfeits it.

The deadline imposes a rate requirement rather than a quantity requirement, admitting the compact condition

$$\dot{S}^{\text{deployed}} \; \geq \; \frac{S^{\text{filed}}}{T^{\text{bring-into-use}} - t^{\text{start}}}$$

with failure to satisfy it forfeiting the filed position in whole or in part. A venture holding captive launch capacity controls the numerator's feasibility directly. A venture buying launch at market controls neither the rate nor the schedule, because its supplier allocates capacity across a manifest the venture does not set.

The observation reframes the launch-cadence coupling. The cadence was not merely an economic advantage. It was the mechanism by which a regulatory option was exercised before it expired, and the option's value admits the compact statement

$$W^{\text{filing}} = \mathbf{1}\left[ \text{bring-into-use satisfied} \right] \cdot V^{\text{protected position}}$$

with the value collapsing to zero on failure rather than degrading gracefully. The article regards this as the single most underappreciated element of the case and as the point at which the capital-formation story and the regulatory story become the same story.

## Orbital Shells and the Congestion Externality

The constellation imposes costs on other operators and on future entrants that it does not bear, and the article states the externality plainly rather than treating it as a critics' talking point.

The debris and conjunction regime is documented at the [NASA Orbital Debris Program Office][ref_nasa_orbital_debris], the [orbital debris mitigation standard practices][ref_nasa_orbital_debris_mitigation], and the [Inter-Agency Space Debris Coordination Committee guidelines][ref_iadc_guidelines], with the economic treatments at [Adilov Alexander and Cunningham 2018][research_adilov_et_al_2018] and [Weeden and Chow 2012][research_weeden_chow_2012]. The externality admits the compact statement

$$\frac{\partial \, \text{collision risk}_j}{\partial \, S_i} > 0 \qquad \text{with the cost borne by } j \neq i$$

with each operator's deployment raising every other operator's risk and no mechanism pricing the increment. The conjunction rate between resident objects scales approximately with the square of the population in a shell, admitting the compact relation

$$\dot{n}^{\text{conjunction}} \; \propto \; \frac{S_{\text{shell}}^{2}}{V_{\text{shell}}}$$

with the quadratic term the reason an increment to an already-populated shell is more costly than the same increment to an empty one. The divergence between the private and social optimum follows directly

$$S^{\text{private}} : \; \frac{\partial \Pi_i}{\partial S_i} = 0 \qquad \text{against} \qquad S^{\text{social}} : \; \frac{\partial}{\partial S_i}\left[ \Pi_i + \sum_{j \neq i} \Pi_j \right] = 0$$

with the private optimum exceeding the social one by the uninternalized external term. The structure is a standard common-pool problem and the literature the regulated-industry tradition supplies predicts under-provision of mitigation absent an allocation regime.

The article notes in fairness that the short design lifetime and active deorbit capability the constellation employs are substantially better mitigation practice than the geostationary and medium-orbit precedents exhibited, and that the aggregate risk nonetheless rises because the object count rises faster than the per-object risk falls. Both statements are true and the commentary generally asserts only one of them.

## The Iridium and Globalstar Precedents

The two 1990s constellation programmes supply the precedents in which the same business was attempted without a captive launch capability, and the [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] and the [Patient-Private Capital-Formation Leg article A290][related_post_a290_spacex_patient_private_leg] treat the capital-structure dimension of the first.

The relevant contrast for this article is the cost position rather than the financing. Both programmes purchased launch at market prices from external providers, and both therefore incurred the full disadvantage the economic-property section states, on a campaign requiring dozens of launches. The disadvantage they bore admits the compact application of the economic-property result

$$\Delta C^{\text{1990s programmes}} = N \cdot m \qquad \text{with} \qquad N \sim 10^{1} \; \text{to} \; 10^{2}$$

with the full external margin incurred across every launch of the deployment. The record is at the [Iridium corporate archive][ref_iridium_press_archive_1998], the [Chapter 11 filing][ref_iridium_chapter_11_1999] lodged with the [Securities and Exchange Commission EDGAR][ref_sec_edgar] system, and the case treatments at [Finkelstein and Sanford 2000][research_finkelstein_sanford_2000] and [Zimmerman 2011][research_zimmerman_2011].

The second and less frequently noted contrast concerns the market rather than the cost. Both programmes targeted voice telephony against a terrestrial cellular buildout that expanded faster than either anticipated, so that the addressable market contracted during deployment. The failure mode admits the compact statement as a race between deployment and market erosion

$$\frac{d M^{\text{addressable}}}{dt} < 0 \qquad \text{while} \qquad S < S^{\ast}$$

with the market contracting during the very interval in which the threshold property guarantees no revenue. The combination is close to unsurvivable and it is the sharper reading of those failures than the capital-structure account alone supplies. The present case targeted broadband against a terrestrial buildout whose rural economics have not improved comparably, and the article marks this as a favorable contingency rather than as a strategic insight, because nothing in the 2015 decision demonstrates foresight about terrestrial deployment economics.

## The OneWeb and Kuiper Comparisons

The two contemporary competitors supply the cleanest available test of the article's central claim, because both attempted the same business in the same period under different vertical arrangements.

OneWeb purchased launch services externally and its trajectory is documented at the [OneWeb corporate record][ref_oneweb] and the [Eutelsat corporate record][ref_eutelsat_oneweb], with the insolvency administered through the [United States bankruptcy court system][ref_uscourts_bankruptcy] under the [Chapter 11][ref_bankruptcy_code_ch11] provisions. The programme faced the full external launch cost, faced a deployment deadline set by its own spectrum filings, and depended on a capital supplier whose withdrawal proved terminal. The three failures were not independent, admitting the compact statement

$$\left[ \text{no captive launch} \right] \Rightarrow \left[ \text{deadline uncontrolled} \right] \Rightarrow \left[ \text{capital requirement uncertain} \right] \Rightarrow \left[ \text{supplier withdrawal} \right]$$

with each condition raising the probability of the next. The [Patient-Private Capital-Formation Leg article A290][related_post_a290_spacex_patient_private_leg] treats the same case as a financing failure and this article treats it as a supply failure, and the two readings are compatible because the supply position is what made the financing requirement unbounded.

The Amazon programme supplies the comparison the article regards as most informative, because the sponsor's capital position removes the financing constraint entirely and isolates the launch-supply variable. A programme financed from a balance sheet of that scale cannot fail for want of capital, so its outcome tests the launch-supply proposition specifically. The programme has contracted launch capacity from multiple providers including, notably, the parent firm this article treats, and the sector record is at [SpaceNews][ref_spacenews], [Ars Technica space coverage][ref_arstechnica_space], and [Space Policy Online][ref_space_policy_online].

The comparison admits the compact statement as a controlled contrast

$$\left\{ \text{capital} \right\} \; \text{held approximately constant}, \qquad \left\{ \text{captive launch} \right\} \; \text{varied}$$

with the outcome difference attributable to the varied factor to the extent the other factors are genuinely comparable. The design is the closest the sector offers to holding the financing constraint fixed, admitting the compact statement

$$\left. \frac{\partial \, \text{outcome}}{\partial \, \text{captive launch}} \right|_{\text{capital held high}}$$

as the estimand the comparison identifies. The article marks the limits of the inference. The programmes began at different dates, hold different spectrum priorities, and pursue partially different market segments, so the contrast is suggestive rather than clean.

## Deep Historical Comparative Precedents

The category-dominating spinoff mechanic admits comparison with historical precedents in which a firm built a business on top of a capability developed for another purpose.

The Standard Oil consolidation supplies the precedent for retained-earnings financing displacing external capital markets entirely, documented in [Chernow 2004][book_chernow_2004] Titan and [Nevins 1954][book_nevins_1954], with the primary record at the [Supreme Court decision of 1911][ref_standard_oil_1911]. The relevant parallel is the vertical control of transport, because the firm's position rested substantially on rail and pipeline arrangements that competitors could not obtain on comparable terms. The structural identity with the present case admits the compact statement

$$c^{\text{integrated}}_{\text{transport}} = c^{\text{marginal}} \qquad \text{against} \qquad c^{\text{rival}}_{\text{transport}} = p^{\text{posted}} - r$$

with $r$ the rebate a rival could not obtain, which is the same relation this article states with launch substituted for rail. The article notes that the historical case resolved through dissolution rather than through competitive erosion, which is the base rate the competition-policy tradition applies.

The Bell System supplies the precedent for a communications infrastructure attaining a dominant position and the regulatory settlement that followed, documented in [Temin and Galambos 1987][book_temin_galambos_1987], [Wu 2010][book_wu_2010], [Levin 2010][book_levin_2010], and [Sobel 1995][book_sobel_1995], with the primary record at the [consent decree of 1956][ref_att_consent_decree_1956] and the [divestiture of 1984][ref_att_divestiture_1984]. The case supplies the base rate that the telecommunications-history tradition applies, and the article's reading is that the settlement terms in both instances turned on the treatment of the vertical relationship rather than on market share as such. The regulated bargain admits the compact statement

$$\Pi^{\text{permitted}} = \bar{r} \cdot K^{\text{rate base}} \qquad \text{subject to} \qquad \text{universal-service obligation}$$

with a permitted return on invested capital exchanged for a coverage obligation. The form is one of the available outcomes for the present case and the article notes that a firm whose asset base must be continuously replaced would find a rate-base regime unusually favorable, since the rate base would never depreciate away.

The electrification build-outs supply the precedent for a capital-intensive network whose value depends on coverage completeness, documented in [Hughes 1983][book_hughes_1983] and [Nye 1990][book_nye_1990]. The threshold property the deployment section describes is the same property those systems exhibited, admitting the compact statement of the coverage economics

$$\frac{C^{\text{network}}}{n^{\text{user}}} \; \text{decreasing in} \; n^{\text{user}} \qquad \text{with} \qquad C^{\text{network}} \; \text{largely independent of} \; n^{\text{user}}$$

with the fixed coverage cost incurred before any user is served. The historical resolution was a regulated monopoly with a universal-service obligation, which is one of the available outcomes for the present case.

The railroad and canal financings supply the precedent for infrastructure whose construction period exceeded its financiers' horizon, documented in [Chandler 1977][book_chandler_1977] The Visible Hand and [Chandler 1990][book_chandler_1990] Scale and Scope, with the general treatments at [Landes 1969][book_landes_1969], [North 1990][book_north_1990], and [Perez 2002][book_perez_2002] Technological Revolutions and Financial Capital. The [Perez 2002][book_perez_2002] periodization is the most directly applicable, because it treats the availability of capital for a technology class as a function of the installation and deployment cycle rather than as a constant.

The computing industry supplies the precedent for a firm that supplied a platform while competing with the parties depending on it, documented at the [IBM archives][ref_ibm_archives] with the analytical treatments at [Cusumano and Gawer 2002][book_cusumano_gawer_2002] and [Iansiti and Levien 2004][book_iansiti_levien_2004]. The pattern is the one the competition-policy tradition treats and it is the closest structural analogue to the launch-allocation conflict this article identifies.

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

The principal works are [Weinzierl 2018][research_weinzierl_2018], [Hertzfeld 2002][research_hertzfeld_2002], [Adilov Alexander and Cunningham 2018][research_adilov_et_al_2018], [Weeden and Chow 2012][research_weeden_chow_2012], and [Zimmerman 2011][research_zimmerman_2011], with the policy histories at [Launius 2004][book_launius_2004], [McCurdy 1994][book_mccurdy_1994], [Logsdon 1970][book_logsdon_1970], [Handberg 1994][book_handberg_1994], [McDougall 1985][book_mcdougall_1985], and [Heppenheimer 1999][book_heppenheimer_1999]. The literature treats the sector as a government-programme domain and has not substantially absorbed the transition to a commercially financed one.

### Critical and Skeptical Literature

A critical literature reads the arrangement as the private appropriation of a global commons and as the concentration of communications infrastructure in a single unaccountable firm, drawing on [Srnicek 2017][book_srnicek_2017] Platform Capitalism, [Zuboff 2019][book_zuboff_2019], [Krippner 2011][book_krippner_2011], [Wu 2010][book_wu_2010], and [Khan 2017][research_khan_2017]. The orbital-commons form of the concern is the strongest, because the resource is genuinely finite, genuinely shared, and genuinely unpriced. The article regards the concern as well founded and does not resolve it.

### Case-Study and Biographical Literature

The narrative record is at [Berger 2021][book_berger_2021] Liftoff, [Berger 2024][book_berger_2024] Reentry, [Vance 2015][book_vance_2015], [Isaacson 2023][book_isaacson_2023], [Davenport 2018][book_davenport_2018], and [Fernholz 2018][book_fernholz_2018], and it supplies substantially the entire account of the internal decision to proceed with the programme.

### Trade Press and Journalistic Record

Substantially every quantitative claim in this article rests on the reconstruction appearing in [SpaceNews][ref_spacenews], [Ars Technica space coverage][ref_arstechnica_space], [Payload][ref_payload], [Payload Research][ref_payload_research], [The Space Review][ref_the_space_review], [NASASpaceflight][ref_nasaspaceflight], [Space Policy Online][ref_space_policy_online], [European Spaceflight][ref_european_spaceflight], [Aviation Week][ref_aviation_week], [Breaking Defense][ref_breaking_defense], [Defense News][ref_defense_news], [Bloomberg][ref_bloomberg], the [New York Times][ref_nyt], and the [Wall Street Journal][ref_wsj], with the sector analyses at [Space Capital][ref_space_capital], [BryceTech][ref_bryce_tech], and [PitchBook][ref_pitchbook].

## Contemporary Comparative Landscape

The contemporary landscape for the commercial-spinoff leg is the emptiest of the three capital-formation legs, because the conditions the pattern requires are jointly satisfied almost nowhere.

The European position operates through [Arianespace][ref_arianespace] and [ArianeGroup][ref_arianegroup_press] under a governmental-shareholder arrangement, with a constellation programme pursued at the union level rather than by a commercial operator, and the entrant record at [European Spaceflight][ref_european_spaceflight]. The configuration cannot produce the arrangement this article describes, because the launch provider and the constellation operator are separate institutions with separate budgets, so the internal transaction occurs at a negotiated price rather than at marginal cost. The condition the arrangement requires admits the compact statement

$$\text{common residual claimant over both stages} \iff \text{transfer at } c^{\text{marginal}} \text{ is incentive-compatible}$$

with separate budgets destroying the incentive compatibility irrespective of any policy intention, because each institution is assessed on its own result.

The Chinese position documented at [China commercial space][ref_china_commercial_space] pursues constellation programmes with state financing and domestic launch capacity, which satisfies the captive-launch condition through common state ownership rather than through common corporate ownership. The article regards this as the closest structural analogue currently in existence and notes that it achieves the coupling by a different institutional route.

The Indian and Japanese positions at [ISRO][ref_isro_press] and [JAXA][ref_jaxa_press] hold launch capability without a commercial constellation of comparable scale.

The scarcity of the configuration admits the compact statement

$$\left| \left\{ \text{entities holding captive launch at constellation cadence} \right\} \right| \; \sim \; 2$$

counting the present case and the Chinese state programmes, and the article notes that this is the smallest comparison set of any condition treated in the series. The pattern the closing section states is therefore extracted from close to a single observation, and the reader should weight it accordingly.

Among commercial entrants, [Rocket Lab][ref_rocket_lab_press] holds launch capability at a vehicle scale below constellation deployment economics while developing a larger vehicle, [Blue Origin][ref_blue_origin_press] holds a launch programme under the single-funder arrangement the [Governance article A287][related_post_a287_spacex_governance] treats and is affiliated with the constellation competitor this article discusses, and [United Launch Alliance][ref_ula_press] with its parents at [Boeing][ref_boeing_press] and [Northrop Grumman][ref_northrop_grumman_press] operates as a launch provider without a downstream service business. The [Space Force National Security Space Launch programme][ref_space_force_nssl] record documents the government-customer side of the same set.

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

with $\ast$ marking a cell the available record does not establish. SpaceX exhibits closure on all five. Iridium exhibited non-closure on captive input and surplus capacity, closure on threshold market and regulatory priority, and non-closure on reinvestment scale. OneWeb exhibited the same pattern with an additional failure on regulatory priority following its deployment interruption. The Amazon programme exhibits non-closure on captive input, closure on reinvestment scale by virtue of its sponsor, and an unresolved position on regulatory priority. The Chinese state programmes exhibit closure on captive input through common ownership and an unresolved position on the remainder.

The cross-sectional pattern indicates that the captive-input sub-property is the one that discriminates most sharply, and the correlation with the outcome admits the compact statement

$$\operatorname{corr}_j\!\left( \phi_{j,1}^{\text{captive input}}, \; \text{completion} \right) \gg \operatorname{corr}_j\!\left( \phi_{j,5}^{\text{reinvestment scale}}, \; \text{completion} \right)$$

with the availability of captive launch capacity carrying more information than the sponsor's capital scale. The finding is the article's central empirical claim and it is the reason the article treats the Amazon comparison as the informative one, since that case holds capital scale high and captive input absent.

## Data Sources and Reconstruction Methodology

The article draws on primary and secondary sources with a pronounced asymmetry between the regulatory and financial layers.

The primary-source layer on regulatory matters is complete and authoritative. Authorizations, filings, coordination records, and licensing decisions are public and were consulted directly.

The primary-source layer on financial matters is substantially absent. The firm is private, the spinoff has never been separately reported, and no segment disclosure exists. The reconstruction methodology therefore takes the regulatory record as the spine for anything concerning satellite counts, authorizations, and deployment dates, and relies on trade-press reconstruction for everything concerning subscribers, revenue, and cost.

The empirical-record limitations comprise the following. The internal transfer price is unknown and determines the attribution of profit between the segments. The capacity-allocation rule between internal and external launch demand is unknown. Satellite unit cost is unknown. Mission burn is unknown, which makes the crossover date unknown. Subscriber and revenue figures are company statements repeated by the press rather than audited disclosures. The consequence is that the article's structural claims are substantially better supported than its quantitative ones, and the reader should treat the numbers as illustrative of a pattern rather than as measurements.

## Alternative Analytical Frameworks

The commercial-spinoff framing the article develops is one of several the surrounding literature applies.

The diversification framing treats the constellation as an entry into an unrelated market and predicts value destruction on the evidence the corporate-diversification literature supplies. The article's response is that the framing misidentifies the relationship, and the distinction admits the compact statement

$$\text{related} \iff \frac{\partial c^{\text{segment } A}}{\partial q^{\text{segment } B}} \neq 0$$

with genuine relatedness requiring that one segment's activity alter the other's cost. The businesses here share the input rather than merely the owner, so the derivative is nonzero and negative. The framing's prediction would apply to a constellation operator purchasing launch at market, for whom the derivative is zero.

The platform framing treats the constellation as a two-sided market and imports the pricing and market-structure conclusions of the platform literature. The article accepts the framing for the direct-to-cell service and rejects it for consumer broadband, on the ground that the latter has one side and a positive marginal cost. The rejection admits the compact test

$$\frac{\partial u^{\text{subscriber}}}{\partial n^{\text{subscriber}}} \leq 0 \quad \text{for shared-capacity broadband}$$

with additional subscribers degrading rather than improving the service, which is the opposite of the network externality the platform conclusions presuppose.

The natural-monopoly framing treats the position as a durable dominance arising from scale economies and a finite resource, and it generates the regulatory prescriptions the regulated-industry tradition supplies. The article's response admits compact statement as a contrast in the durability of the underlying asset

$$T^{\text{asset life, conventional utility}} \sim 10^{1} \; \text{to} \; 10^{2} \; \text{years} \qquad \text{against} \qquad L \sim 5 \; \text{years}$$

with the conventional natural monopoly resting on an asset base that outlives any plausible entrant response and this one resting on an asset base that does not. The finite resource here is spectrum priority rather than infrastructure, and priority is a legal position that an administration can in principle revisit.

The commons framing treats the orbital environment as a shared resource being appropriated without compensation and generates the strongest available critique. The article accepts the framing's factual premise. The allocation the framing would require admits the compact statement as a corrective price

$$p^{\text{orbital}}_i = \sum_{j \neq i} \frac{\partial \Pi_j}{\partial S_i}$$

with each operator charged the marginal external cost it imposes on the others. No such instrument exists in any jurisdiction. The framing therefore argues for an allocation regime rather than against any particular operator, and the article notes that the first operator to reach scale in an unpriced commons is the one an eventual regime would most constrain, which gives the incumbent an interest in the regime's design that is worth stating explicitly.

The industrial-policy framing treats the outcome as the return on the government investment the [Government-Anchor Capital-Formation Leg article A289][related_post_a289_spacex_government_anchor_leg] documents, and it generates the claim that the public has an equity-like interest in the result that the non-dilutive instrument failed to secure. The article regards the framing as analytically serious and notes that it is a claim about what the instrument should have been rather than about what it was.

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

## Cross-References to the Series

The article back-references the [series opener][related_post_a281_spacex_framing] for the seven-plus-three framework and the mission burn the spinoff is intended to fund. The article back-references the [Value Gradient article A282][related_post_a282_spacex_value_gradient] for the vehicle progression whose surplus capacity the spinoff consumes. The article back-references the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] for the external anchor customer the spinoff internalizes. The article back-references the [Value Capture article A284][related_post_a284_spacex_value_capture] for the complementary-asset argument this article supplies the sharpest instance of. The article back-references the [Decomposability article A285][related_post_a285_spacex_decomposability] for the reuse progression the cadence coupling accelerates. The article back-references the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] for the design commonality that makes the satellite production rate attainable. The article back-references the [Governance article A287][related_post_a287_spacex_governance] for the control configuration that permitted the programme to be undertaken over the objection external shareholders would likely have raised. The article back-references the [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] for the line structure the spinoff occupies and for the transfer price both articles identify as the critical unobserved quantity. The article back-references the [Government-Anchor Capital-Formation Leg article A289][related_post_a289_spacex_government_anchor_leg] for the non-dilutive channel that financed the capability the spinoff exploits. The article back-references the [Patient-Private Capital-Formation Leg article A290][related_post_a290_spacex_patient_private_leg] for the January 2015 round raised against the business this article describes.

The article forward-references the closing article A292, which synthesizes across the framework and treats the singular-conjunction thesis.

The article cross-references the existing published corpus including the [Why Startups Actually Fail article A167][related_post_a167_startup_failure], the [What a Patent Is and Is Not article A161][related_post_a161_patent_intro], the [Patents Trade Secrets and the Disclosure Tradeoff article A164][related_post_a164_patents_trade_secrets], the [Money Behind an SBIR or STTR Award article A140][related_post_a140_sbir_money], the [Introduction to Space Studies article A90][related_post_a90_intro_space_studies], the [History of Rocketplanes article A96][related_post_a96_history_rocketplanes], the [What Does the United States Space Force Do article A97][related_post_a97_us_space_force], the [Framing and the Co-Development Mechanism article A237][related_post_a237_aerospace_framing], the [Silicon Valley from Defense Contracting article A246][related_post_a246_silicon_valley_defense], and the [Contemporary Snapshot article A248][related_post_a248_contemporary_snapshot].

## Terminological Note

The article adopts terminology consistent with the satellite communications and industrial-organization conventions and marks the places popular usage diverges. The term "spinoff" refers throughout to a business line built within the firm on an existing capability, and not to a corporate separation, which is the ordinary financial meaning and which the [Governance article A287][related_post_a287_spacex_governance] treats as an open question for this business specifically. The term "constellation" refers to a coordinated set of satellites operated as a single system, and is distinguished from a "fleet", which carries no coordination implication. The term "captive input" refers to an input supplied by a commonly owned party at internal cost, and is distinguished from a "secured supply", which refers to a contracted external supply at a market price. The term "category-dominating" refers to a position holding the majority of a defined service category by the relevant volume measure, and the article marks that the category definition is contestable and that the position looks different if the category is defined as satellite broadband, as rural broadband, or as connectivity generally. The term "replenishment" refers to the ongoing replacement of satellites reaching end of life, and is distinguished from "expansion", which refers to growth in the deployed count.

## Load-Bearing Open Questions

The article closes with the load-bearing open questions the treatment leaves unresolved. First, the internal transfer price is unknown, and it determines whether the launch business or the constellation business is the profitable one in any reported segmentation. Second, the capacity-allocation rule between internal and external launch demand is unknown, and it is the quantity a competition authority would need first. Third, the mission-funding crossover date is unknown, and it is the single most consequential unresolved quantity in the series, because every arrangement the preceding articles describe exists to bridge the interval before it. Fourth, whether the regulatory priority the constellation holds is durable against a coordinated administrative response is untested. Fifth, whether the replenishment treadmill limits the position's durability as the article argues or is offset by production learning faster than obsolescence is an empirical question the available data cannot settle. Sixth, the direct-to-cell business depends on a complementary asset the venture does not own, and the division of value between the operator and the carriers is unresolved. Seventh, whether the orbital-congestion externality will be addressed by an allocation regime, by liability, or not at all is a policy question whose resolution would materially alter the economics this article describes.

## References

### Books

- [Bain 1968 Industrial Organization][book_bain_1968]
- [Berger 2021 Liftoff][book_berger_2021]
- [Berger 2024 Reentry][book_berger_2024]
- [Bork 1978 The Antitrust Paradox][book_bork_1978]
- [Chandler 1977 The Visible Hand][book_chandler_1977]
- [Chandler 1990 Scale and Scope][book_chandler_1990]
- [Chernow 2004 Titan][book_chernow_2004]
- [Christensen 1997 The Innovator's Dilemma][book_christensen_1997]
- [Christensen and Raynor 2003 The Innovator's Solution][book_christensen_raynor_2003]
- [Cusumano and Gawer 2002 Platform Leadership][book_cusumano_gawer_2002]
- [Davenport 2018 The Space Barons][book_davenport_2018]
- [Fernholz 2018 Rocket Billionaires][book_fernholz_2018]
- [Handberg 1994 Reinventing NASA][book_handberg_1994]
- [Heppenheimer 1999 The Space Shuttle Decision][book_heppenheimer_1999]
- [Hovenkamp 2005 The Antitrust Enterprise][book_hovenkamp_2005]
- [Hughes 1983 Networks of Power][book_hughes_1983]
- [Iansiti and Levien 2004 The Keystone Advantage][book_iansiti_levien_2004]
- [Isaacson 2023 Elon Musk][book_isaacson_2023]
- [Kahn 1988 The Economics of Regulation][book_kahn_1988]
- [Krippner 2011 Capitalizing on Crisis][book_krippner_2011]
- [Landes 1969 The Unbound Prometheus][book_landes_1969]
- [Launius 2004 Frontiers of Space Exploration][book_launius_2004]
- [Levin 2010 The Wires That Bind][book_levin_2010]
- [Logsdon 1970 The Decision to Go to the Moon][book_logsdon_1970]
- [McCurdy 1994 Inside NASA][book_mccurdy_1994]
- [McDougall 1985 The Heavens and the Earth][book_mcdougall_1985]
- [Metcalfe 1998 Evolutionary Economics and Creative Destruction][book_metcalfe_1998]
- [Nelson and Winter 1982 An Evolutionary Theory of Economic Change][book_nelson_winter_1982]
- [Nevins 1954 Ford The Times The Man The Company][book_nevins_1954]
- [North 1990 Institutions Institutional Change and Economic Performance][book_north_1990]
- [Nye 1990 Electrifying America][book_nye_1990]
- [Penrose 1959 The Theory of the Growth of the Firm][book_penrose_1959]
- [Perez 2002 Technological Revolutions and Financial Capital][book_perez_2002]
- [Posner 2001 Antitrust Law][book_posner_2001]
- [Scherer and Ross 1990 Industrial Market Structure and Economic Performance][book_scherer_ross_1990]
- [Sharkey 1982 The Theory of Natural Monopoly][book_sharkey_1982]
- [Sobel 1995 Longitude][book_sobel_1995]
- [Srnicek 2017 Platform Capitalism][book_srnicek_2017]
- [Temin and Galambos 1987 The Fall of the Bell System][book_temin_galambos_1987]
- [Tirole 1988 The Theory of Industrial Organization][book_tirole_1988]
- [Utterback 1994 Mastering the Dynamics of Innovation][book_utterback_1994]
- [Van Alstyne Parker Choudary 2016 Platform Revolution][book_vanalstyne_parker_choudary_2016]
- [Vance 2015 Elon Musk Tesla SpaceX and the Quest for a Fantastic Future][book_vance_2015]
- [Williamson 1985 The Economic Institutions of Capitalism][book_williamson_1985]
- [Wu 2010 The Master Switch][book_wu_2010]
- [Zuboff 2019 The Age of Surveillance Capitalism][book_zuboff_2019]

### Reference

- [1956 AT&T Consent Decree][ref_att_consent_decree_1956]
- [1984 AT&T Divestiture Modification of Final Judgment][ref_att_divestiture_1984]
- [ArianeGroup Press Releases][ref_arianegroup_press]
- [Arianespace][ref_arianespace]
- [Ars Technica Space Coverage][ref_arstechnica_space]
- [Aviation Week Coverage][ref_aviation_week]
- [Bloomberg Business News][ref_bloomberg]
- [Blue Origin Press Releases][ref_blue_origin_press]
- [Boeing Press Releases][ref_boeing_press]
- [Breaking Defense Coverage][ref_breaking_defense]
- [BryceTech Sector Reports][ref_bryce_tech]
- [China Commercial Space Industry Analysis][ref_china_commercial_space]
- [Defense News Coverage][ref_defense_news]
- [DOD Contract Announcements][ref_dod_contracts]
- [European Spaceflight Coverage][ref_european_spaceflight]
- [Eutelsat Corporate Record][ref_eutelsat_oneweb]
- [FAA Office of Commercial Space Transportation][ref_faa_ast]
- [FCC Direct-to-Cell Authorization 2024][ref_fcc_direct_to_cell_2024]
- [FCC Filings Database][ref_fcc_filings]
- [FCC Starlink Authorization March 2018][ref_fcc_starlink_2018]
- [FCC Starlink Generation 2 Authorization December 2022][ref_fcc_starlink_gen2_2022]
- [Federal Procurement Data System][ref_fpds]
- [IBM Archives][ref_ibm_archives]
- [Indian Space Research Organisation Press Releases][ref_isro_press]
- [Inter-Agency Space Debris Coordination Committee][ref_iadc_guidelines]
- [Iridium Chapter 11 Bankruptcy Filing 1999][ref_iridium_chapter_11_1999]
- [Iridium World Communications Press Release Archive 1998][ref_iridium_press_archive_1998]
- [ITU Radio Regulations 2020][ref_itu_radio_regulations_2020]
- [Japanese Aerospace Exploration Agency Press Releases][ref_jaxa_press]
- [NASA Orbital Debris Mitigation Standard Practices][ref_nasa_orbital_debris_mitigation]
- [NASA Orbital Debris Program Office][ref_nasa_orbital_debris]
- [NASASpaceflight Coverage][ref_nasaspaceflight]
- [New York Times][ref_nyt]
- [Northrop Grumman Press Releases][ref_northrop_grumman_press]
- [OneWeb Corporate Record][ref_oneweb]
- [Payload Newsletter][ref_payload]
- [Payload Research][ref_payload_research]
- [PitchBook Transaction Data][ref_pitchbook]
- [Rocket Lab Press Releases][ref_rocket_lab_press]
- [SEC EDGAR Company Search][ref_sec_edgar]
- [Space Capital Quarterly Reports][ref_space_capital]
- [Space Force National Security Space Launch][ref_space_force_nssl]
- [Space Policy Online][ref_space_policy_online]
- [SpaceNews][ref_spacenews]
- [SpaceX Better Than Nothing Beta Press October 2020][ref_spacex_press_beta_2020]
- [SpaceX Corporate Site][ref_spacex_company]
- [SpaceX Falcon 9 Vehicle Documentation][ref_spacex_falcon9_vehicle]
- [SpaceX News Archive][ref_spacex_news_archive]
- [SpaceX Press Release Block 5 Bangabandhu-1 May 2018][ref_spacex_press_block5_bangabandhu_2018]
- [SpaceX Press Release Falcon 9 First Landing December 2015][ref_spacex_press_falcon9_first_landing_2015]
- [SpaceX Press Release SES-10 First Refly March 2017][ref_spacex_press_ses10_2017]
- [SpaceX Press Release Starlink First 60 Operational Satellites May 2019][ref_spacex_press_starlink_v0_9_2019]
- [SpaceX Press Release Tintin A and B February 2018][ref_spacex_press_tintin_2018]
- [SpaceX Seattle Facility Announcement January 2015][ref_spacex_seattle_announcement_2015]
- [SpaceX Starlink Program Page][ref_spacex_starlink]
- [SpaceX Starshield Product Page][ref_spacex_starshield]
- [Standard Oil Dissolution Supreme Court Decision 1911][ref_standard_oil_1911]
- [Starlink Direct to Cell][ref_starlink_direct_to_cell]
- [Starlink Technology][ref_starlink_technology]
- [The Space Review][ref_the_space_review]
- [United Launch Alliance Press Releases][ref_ula_press]
- [United Nations Liability Convention 1972][ref_un_liability_convention_1972]
- [United Nations Outer Space Treaty 1967][ref_un_outer_space_treaty_1967]
- [United Nations Registration Convention 1976][ref_un_registration_convention_1976]
- [United States Bankruptcy Code Chapter 11][ref_bankruptcy_code_ch11]
- [United States Bankruptcy Courts][ref_uscourts_bankruptcy]
- [USAspending Federal Award Data][ref_usaspending]
- [Wall Street Journal][ref_wsj]

### Research

- [Abernathy and Clark 1985 Innovation Mapping the Winds of Creative Destruction][research_abernathy_clark_1985]
- [Adilov Alexander Cunningham 2018 An Economic Analysis of Earth Orbit Pollution][research_adilov_et_al_2018]
- [Anderson and Tushman 1990 Technological Discontinuities and Dominant Designs][research_anderson_tushman_1990]
- [Arthur 1989 Competing Technologies Increasing Returns and Lock-In by Historical Events][research_arthur_1989]
- [Barney 1991 Firm Resources and Sustained Competitive Advantage][research_barney_1991]
- [Boudreau 2010 Open Platform Strategies and Innovation][research_boudreau_2010]
- [Bower and Christensen 1995 Disruptive Technologies Catching the Wave][research_bower_christensen_1995]
- [Bresnahan and Trajtenberg 1995 General Purpose Technologies Engines of Growth][research_bresnahan_trajtenberg_1995]
- [Christensen and Rosenbloom 1995 Explaining the Attackers Advantage][research_christensen_rosenbloom_1995]
- [Coase 1937 The Nature of the Firm][research_coase_1937]
- [David 1985 Clio and the Economics of QWERTY][research_david_1985]
- [Evans 2003 The Antitrust Economics of Multi-Sided Platform Markets][research_evans_2003]
- [Farrell and Saloner 1985 Standardization Compatibility and Innovation][research_farrell_saloner_1985]
- [Finkelstein and Sanford 2000 Learning from Corporate Mistakes Iridium][research_finkelstein_sanford_2000]
- [Gawer 2014 Bridging Differing Perspectives on Technological Platforms][research_gawer_2014]
- [Gawer and Cusumano 2014 Industry Platforms and Ecosystem Innovation][research_gawer_cusumano_2014]
- [Grossman and Hart 1986 The Costs and Benefits of Ownership][research_grossman_hart_1986]
- [Hagiu and Wright 2015 Multi-Sided Platforms][research_hagiu_wright_2015]
- [Henderson and Clark 1990 Architectural Innovation The Reconfiguration of Existing Product Technologies][research_henderson_clark_1990]
- [Hertzfeld 2002 Measuring the Economic Returns from Successful NASA Life Sciences Technology Transfer][research_hertzfeld_2002]
- [Jacobides Cennamo and Gawer 2018 Towards a Theory of Ecosystems][research_jacobides_et_al_2018]
- [Katz and Shapiro 1985 Network Externalities Competition and Compatibility][research_katz_shapiro_1985]
- [Khan 2017 Amazon's Antitrust Paradox][research_khan_2017]
- [Klein Crawford and Alchian 1978 Vertical Integration Appropriable Rents and the Competitive Contracting Process][research_klein_crawford_alchian_1978]
- [Klepper 1996 Entry Exit Growth and Innovation over the Product Life Cycle][research_klepper_1996]
- [Krueger 1974 The Political Economy of the Rent-Seeking Society][research_krueger_1974]
- [Monteverde and Teece 1982 Supplier Switching Costs and Vertical Integration in the Automobile Industry][research_monteverde_teece_1982]
- [Parker and Van Alstyne 2005 Two-Sided Network Effects A Theory of Information Product Design][research_parker_vanalstyne_2005]
- [Rochet and Tirole 2003 Platform Competition in Two-Sided Markets][research_rochet_tirole_2003]
- [Rochet and Tirole 2006 Two-Sided Markets A Progress Report][research_rochet_tirole_2006]
- [Rysman 2009 The Economics of Two-Sided Markets][research_rysman_2009]
- [Stigler 1971 The Theory of Economic Regulation][research_stigler_1971]
- [Teece 1986 Profiting from Technological Innovation][research_teece_1986]
- [Teece Pisano Shuen 1997 Dynamic Capabilities and Strategic Management][research_teece_pisano_shuen_1997]
- [Weeden and Chow 2012 Taking a Common-Pool Resources Approach to Space Sustainability][research_weeden_chow_2012]
- [Weinzierl 2018 Space the Final Economic Frontier][research_weinzierl_2018]
- [Wernerfelt 1984 A Resource-Based View of the Firm][research_wernerfelt_1984]
- [Williamson 1971 The Vertical Integration of Production Market Failure Considerations][research_williamson_1971]
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

[book_bain_1968]: https://openlibrary.org/search?q=Bain+Industrial+Organization+1968
[book_berger_2021]: https://williammorrow.com/liftoff-eric-berger/
[book_berger_2024]: https://williammorrow.com/reentry-eric-berger/
[book_bork_1978]: https://www.hup.harvard.edu/books/9780674032545
[book_chandler_1977]: https://www.hup.harvard.edu/books/9780674940529
[book_chandler_1990]: https://www.hup.harvard.edu/books/9780674789944
[book_chernow_2004]: https://www.penguinrandomhouse.com/books/98060/titan-by-ron-chernow/
[book_christensen_1997]: https://www.hbsp.harvard.edu/product/1130-HBK-ENG
[book_christensen_raynor_2003]: https://www.hbsp.harvard.edu/product/3595-HBK-ENG
[book_cusumano_gawer_2002]: https://www.hbsp.harvard.edu/product/6155-HBK-ENG
[book_davenport_2018]: https://www.hachettebookgroup.com/titles/christian-davenport/the-space-barons/9781610398299/
[book_fernholz_2018]: https://www.hachettebookgroup.com/titles/tim-fernholz/rocket-billionaires/9781328662231/
[book_handberg_1994]: https://www.abc-clio.com/9780275949242/
[book_heppenheimer_1999]: https://www.si.edu/object/space-shuttle-decision%3Anmah_1197080
[book_hovenkamp_2005]: https://www.hup.harvard.edu/books/9780674025819
[book_hughes_1983]: https://jhupbooks.press.jhu.edu/title/networks-power
[book_iansiti_levien_2004]: https://www.hbsp.harvard.edu/product/5219-HBK-ENG
[book_isaacson_2023]: https://www.simonandschuster.com/books/Elon-Musk/Walter-Isaacson/9781982181284
[book_kahn_1988]: https://mitpress.mit.edu/9780262610520/the-economics-of-regulation/
[book_krippner_2011]: https://www.hup.harvard.edu/books/9780674066199
[book_landes_1969]: https://www.cambridge.org/9780521094184
[book_launius_2004]: https://global.oup.com/academic/product/frontiers-of-space-exploration-9780313325243
[book_levin_2010]: https://openlibrary.org/search?q=Levin+Wires+That+Bind
[book_logsdon_1970]: https://mitpress.mit.edu/9780262620109/the-decision-to-go-to-the-moon/
[book_mccurdy_1994]: https://jhupbooks.press.jhu.edu/title/inside-nasa
[book_mcdougall_1985]: https://jhupbooks.press.jhu.edu/title/heavens-and-earth
[book_metcalfe_1998]: https://www.routledge.com/Evolutionary-Economics-and-Creative-Destruction/Metcalfe/p/book/9780415158671
[book_nelson_winter_1982]: https://www.hup.harvard.edu/books/9780674272286
[book_nevins_1954]: https://openlibrary.org/search?q=Nevins+Ford+The+Times+The+Man+The+Company
[book_north_1990]: https://www.cambridge.org/9780521397346
[book_nye_1990]: https://mitpress.mit.edu/9780262640305/electrifying-america/
[book_penrose_1959]: https://global.oup.com/academic/product/the-theory-of-the-growth-of-the-firm-9780199573844
[book_perez_2002]: https://www.edwardelgar.com/shop/gbp/technological-revolutions-and-financial-capital-9781843763314.html
[book_posner_2001]: https://press.uchicago.edu/ucp/books/book/chicago/A/bo3627998.html
[book_scherer_ross_1990]: https://openlibrary.org/search?q=Scherer+Ross+Industrial+Market+Structure
[book_sharkey_1982]: https://www.cambridge.org/9780521271943
[book_sobel_1995]: https://www.bloomsbury.com/us/longitude-9780802715296/
[book_srnicek_2017]: https://www.wiley.com/en-us/Platform+Capitalism-p-9781509504879
[book_temin_galambos_1987]: https://openlibrary.org/search?q=Temin+Galambos+Fall+Bell+System
[book_tirole_1988]: https://mitpress.mit.edu/9780262200714/the-theory-of-industrial-organization/
[book_utterback_1994]: https://www.hbsp.harvard.edu/product/4855-HBK-ENG
[book_vanalstyne_parker_choudary_2016]: https://wwnorton.com/books/Platform-Revolution/
[book_vance_2015]: https://www.harpercollins.com/products/elon-musk-ashlee-vance
[book_williamson_1985]: https://www.simonandschuster.com/books/The-Economic-Institutions-of-Capitalism/Oliver-E-Williamson/9780684863740
[book_wu_2010]: https://www.penguinrandomhouse.com/books/181430/the-master-switch-by-tim-wu/
[book_zuboff_2019]: https://www.hachettebookgroup.com/titles/shoshana-zuboff/the-age-of-surveillance-capitalism/9781610395694/
[ref_arianegroup_press]: https://www.arianegroup.com/en/news/press-releases/
[ref_arianespace]: https://www.arianespace.com/
[ref_arstechnica_space]: https://arstechnica.com/science/space/
[ref_att_consent_decree_1956]: https://www.corp.att.com/history/nethistory/consent-decree.html
[ref_att_divestiture_1984]: https://www.corp.att.com/history/nethistory/divestiture.html
[ref_aviation_week]: https://aviationweek.com/
[ref_bankruptcy_code_ch11]: https://www.law.cornell.edu/uscode/text/11/chapter-11
[ref_bloomberg]: https://www.bloomberg.com/
[ref_blue_origin_press]: https://www.blueorigin.com/news/
[ref_boeing_press]: https://boeing.mediaroom.com/
[ref_breaking_defense]: https://breakingdefense.com/
[ref_bryce_tech]: https://brycetech.com/reports
[ref_china_commercial_space]: https://spacenews.com/topic/china/
[ref_defense_news]: https://www.defensenews.com/
[ref_dod_contracts]: https://www.defense.gov/News/Contracts/
[ref_european_spaceflight]: https://europeanspaceflight.com/
[ref_eutelsat_oneweb]: https://www.eutelsat.com/
[ref_faa_ast]: https://www.faa.gov/space
[ref_fcc_direct_to_cell_2024]: https://docs.fcc.gov/public/attachments/DA-24-208A1.pdf
[ref_fcc_filings]: https://www.fcc.gov/wireless/systems-utilities/electronic-comment-filing-system-ecfs
[ref_fcc_starlink_2018]: https://docs.fcc.gov/public/attachments/FCC-18-38A1.pdf
[ref_fcc_starlink_gen2_2022]: https://docs.fcc.gov/public/attachments/FCC-22-91A1.pdf
[ref_fpds]: https://www.fpds.gov/
[ref_iadc_guidelines]: https://www.iadc-home.org/
[ref_ibm_archives]: https://www.ibm.com/history/
[ref_iridium_chapter_11_1999]: https://www.sec.gov/Archives/edgar/data/1029074/0000912057-99-034228.txt
[ref_iridium_press_archive_1998]: https://www.iridium.com/
[ref_isro_press]: https://www.isro.gov.in/
[ref_itu_radio_regulations_2020]: https://www.itu.int/pub/R-REG-RR
[ref_jaxa_press]: https://global.jaxa.jp/press/
[ref_nasa_orbital_debris]: https://orbitaldebris.jsc.nasa.gov/
[ref_nasa_orbital_debris_mitigation]: https://orbitaldebris.jsc.nasa.gov/mitigation/
[ref_nasaspaceflight]: https://www.nasaspaceflight.com/
[ref_northrop_grumman_press]: https://news.northropgrumman.com/
[ref_nyt]: https://www.nytimes.com/section/science/space
[ref_oneweb]: https://oneweb.net/
[ref_payload]: https://payloadspace.com/
[ref_payload_research]: https://payloadspace.com/research/
[ref_pitchbook]: https://pitchbook.com/
[ref_rocket_lab_press]: https://www.rocketlabusa.com/updates/
[ref_sec_edgar]: https://www.sec.gov/edgar/searchedgar/companysearch
[ref_space_capital]: https://www.spacecapital.com/
[ref_space_force_nssl]: https://www.spaceforce.mil/News/Fact-Sheets
[ref_space_policy_online]: https://spacepolicyonline.com/
[ref_spacenews]: https://spacenews.com/
[ref_spacex_company]: https://www.spacex.com/
[ref_spacex_falcon9_vehicle]: https://www.spacex.com/vehicles/falcon-9/
[ref_spacex_news_archive]: https://www.spacex.com/updates/
[ref_spacex_press_beta_2020]: https://www.spacex.com/updates/
[ref_spacex_press_block5_bangabandhu_2018]: https://www.spacex.com/updates/
[ref_spacex_press_falcon9_first_landing_2015]: https://www.spacex.com/news/2015/12/22/orbcomm-2-mission-successful-first-landing-orbital-rocket
[ref_spacex_press_ses10_2017]: https://www.spacex.com/news/2017/03/30/spacex-successfully-launches-first-reused-rocket
[ref_spacex_press_starlink_v0_9_2019]: https://www.spacex.com/updates/
[ref_spacex_press_tintin_2018]: https://www.spacex.com/updates/
[ref_spacex_seattle_announcement_2015]: https://www.spacex.com/updates/
[ref_spacex_starlink]: https://www.starlink.com/
[ref_spacex_starshield]: https://www.spacex.com/starshield/
[ref_standard_oil_1911]: https://supreme.justia.com/cases/federal/us/221/1/
[ref_starlink_direct_to_cell]: https://www.starlink.com/business/direct-to-cell
[ref_starlink_technology]: https://www.starlink.com/technology
[ref_the_space_review]: https://www.thespacereview.com/
[ref_ula_press]: https://www.ulalaunch.com/about/news
[ref_un_liability_convention_1972]: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/liability-convention.html
[ref_un_outer_space_treaty_1967]: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/outerspacetreaty.html
[ref_un_registration_convention_1976]: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/registration-convention.html
[ref_usaspending]: https://www.usaspending.gov/
[ref_uscourts_bankruptcy]: https://www.uscourts.gov/court-programs/bankruptcy
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
[research_adilov_et_al_2018]: https://www.sciencedirect.com/science/article/abs/pii/S0921800917305591
[research_anderson_tushman_1990]: https://www.jstor.org/stable/2393511
[research_arthur_1989]: https://www.jstor.org/stable/2234208
[research_barney_1991]: https://journals.sagepub.com/doi/10.1177/014920639101700108
[research_boudreau_2010]: https://pubsonline.informs.org/doi/10.1287/mnsc.1100.1215
[research_bower_christensen_1995]: https://hbr.org/1995/01/disruptive-technologies-catching-the-wave
[research_bresnahan_trajtenberg_1995]: https://www.sciencedirect.com/science/article/abs/pii/030440769401598T
[research_christensen_rosenbloom_1995]: https://www.sciencedirect.com/science/article/abs/pii/004873339400794D
[research_coase_1937]: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-0335.1937.tb00002.x
[research_david_1985]: https://www.jstor.org/stable/1805621
[research_evans_2003]: https://academic.oup.com/yjolt/article/20/1/325/2379723
[research_farrell_saloner_1985]: https://www.jstor.org/stable/2555277
[research_finkelstein_sanford_2000]: https://sloanreview.mit.edu/article/learning-from-corporate-mistakes-the-rise-and-fall-of-iridium/
[research_gawer_2014]: https://www.sciencedirect.com/science/article/abs/pii/S0048733314001292
[research_gawer_cusumano_2014]: https://onlinelibrary.wiley.com/doi/10.1111/jpim.12105
[research_grossman_hart_1986]: https://www.jstor.org/stable/1833199
[research_hagiu_wright_2015]: https://www.sciencedirect.com/science/article/pii/S0167718715000156
[research_henderson_clark_1990]: https://www.jstor.org/stable/2393549
[research_hertzfeld_2002]: https://www.sciencedirect.com/science/article/abs/pii/S0265964602000188
[research_jacobides_et_al_2018]: https://onlinelibrary.wiley.com/doi/10.1002/smj.2904
[research_katz_shapiro_1985]: https://www.jstor.org/stable/1814809
[research_khan_2017]: https://www.yalelawjournal.org/note/amazons-antitrust-paradox
[research_klein_crawford_alchian_1978]: https://www.jstor.org/stable/725234
[research_klepper_1996]: https://www.jstor.org/stable/2118234
[research_krueger_1974]: https://www.jstor.org/stable/1808883
[research_monteverde_teece_1982]: https://www.jstor.org/stable/3003400
[research_parker_vanalstyne_2005]: https://pubsonline.informs.org/doi/10.1287/mnsc.1050.0400
[research_rochet_tirole_2003]: https://www.jstor.org/stable/40007911
[research_rochet_tirole_2006]: https://onlinelibrary.wiley.com/doi/10.1111/j.1756-2171.2006.tb00036.x
[research_rysman_2009]: https://www.aeaweb.org/articles?id=10.1257/jep.23.3.125
[research_stigler_1971]: https://www.jstor.org/stable/3003160
[research_teece_1986]: https://www.sciencedirect.com/science/article/abs/pii/0048733386900272
[research_teece_pisano_shuen_1997]: https://onlinelibrary.wiley.com/doi/10.1002/%28SICI%291097-0266%28199708%2918%3A7%3C509%3A%3AAID-SMJ882%3E3.0.CO%3B2-Z
[research_weeden_chow_2012]: https://www.sciencedirect.com/science/article/abs/pii/S0265964612000513
[research_weinzierl_2018]: https://www.aeaweb.org/articles?id=10.1257/jep.32.2.173
[research_wernerfelt_1984]: https://onlinelibrary.wiley.com/doi/10.1002/smj.4250050207
[research_williamson_1971]: https://www.jstor.org/stable/1815199
[research_zimmerman_2011]: https://openlibrary.org/search?q=Zimmerman+Economics+Satellite+Communications
