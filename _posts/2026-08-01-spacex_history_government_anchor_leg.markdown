---
layout: post
mathjax: true
comments: true
title: "History of SpaceX: The Government-Anchor Capital-Formation Leg and Non-Dilutive Development Finance"
date: 2026-08-01 09:00:00 +0000
categories: history business aerospace
series: spacex_history
series_title: History of SpaceX
series_index: 9
---

<!-- A289 -->
<script>console.log("A289");</script>

This article is the ninth in the History of SpaceX series and the first of three treating the capital-formation legs that the [series opener][related_post_a281_spacex_framing] introduced alongside the seven forcing-function conditions. The government-anchor leg is distinguished from the anchor-demand condition that the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] treats by a distinction the article develops throughout. Anchor demand concerns the existence of an identifiable customer who will buy an output. The government-anchor capital-formation leg concerns the mechanism by which the government relationship supplied capital to build the capability before any output existed, and supplied it without taking equity, without taking votes, and without imposing the covenants that private development capital of comparable magnitude would have carried. The article walks the Space Act Agreement instrument under which the development funding was extended, the Commercial Orbital Transportation Services round-one awards of August 2006 and the Rocketplane Kistler termination of 2007 that demonstrates the instrument operating as designed, the milestone-payment mechanics and the non-dilutive property that constitutes the analytical core of the article, the Commercial Resupply Services transition of December 2008, the Commercial Crew progression from the 2010 Commercial Crew Development awards through the September 16 2014 Commercial Crew Transportation Capability awards, the Boeing comparison that demonstrates the risk transfer a fixed-price instrument accomplishes, the National Security Space Launch certification progression across the 2018 Phase 1A, the 2020 Phase 2, and the 2024 Phase 3 Lane 2 awards, and the Starshield classified anchor. The article treats the Small Business Innovation Research Phase III sole-source authority that the [Phase III and the Valley of Death article A138][related_post_a138_sbir_phase3] develops as the closest statutory analogue to the structural pattern under which a development award produces a provider who subsequently receives a services contract. The article contrasts the instrument against the cost-plus counterfactual that the Constellation and Space Launch System programmes realized. The article closes with an explicit pattern-extraction section stating the abstract government-anchor capital-formation mechanic in a form other informed readers can recognize in adjacent domains without naming any downstream application.

## The Government-Anchor Capital-Formation Mapping Problem

The mapping problem for a comprehensive treatment of the government-anchor capital-formation leg in the SpaceX case is the question of how much capital the government relationship supplied, on what terms, at what stages, and what alternative terms the venture would have faced had the capital been raised privately instead.

The problem is distinct from the anchor-demand problem in a way that deserves statement at the outset, because the two are routinely conflated in the commentary. A customer who purchases a delivered service provides revenue. A customer who pays against development milestones before any service exists offers capital. The distinction can be stated as

$$\text{revenue} \; : \; p \cdot q \quad \text{with} \quad q > 0 \qquad \text{against} \qquad \text{development capital} \; : \; \sum_j m_j \quad \text{with} \quad q = 0$$

with the first requiring a delivered quantity and the second requiring only a demonstrated milestone. The COTS awards belong to the second category and the Commercial Resupply Services contracts to the first, and the transition between them is the event the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] treats.

The problem admits several formalizations depending on the analytical tradition consulted. The procurement-mechanism-design tradition from [Laffont and Tirole 1993][book_laffont_tirole_1993] A Theory of Incentives in Procurement and Regulation and [McAfee and McMillan 1988][book_mcafee_mcmillan_1988] Incentives in Government Contracting treats the instrument as a point on the continuum between a cost-reimbursement and a fixed-price arrangement, indexed by the specific power of the incentive scheme. The transaction-cost tradition from [Williamson 1975][research_williamson_1975] and [Williamson 1985][book_williamson_1985] treats the instrument as a governance structure selected to economize on the contracting hazards a novel and asset-development presents. The entrepreneurial-finance tradition from [Sahlman 1990][research_sahlman_1990] and [Gompers 1995][research_gompers_1995] treats the milestone structure as a staged financing whose tranches are released against verified progress. The public-finance and innovation-policy tradition from [Arrow 1962][research_arrow_1962] and [Nelson 1959][research_nelson_1959] treats the arrangement as a public response to an underinvestment arising from the appropriability failure a novel capability exhibits. The present article draws on all four traditions while adopting the mission-oriented-innovation framework the [series opener][related_post_a281_spacex_framing] established as primary.

The general form of the capital-formation problem can be stated compactly. Let $K^{\text{gov}}(t)$, $K^{\text{equity}}(t)$, and $K^{\text{debt}}(t)$ denote the cumulative capital supplied through each channel. The total admits the identity

$$K^{\text{total}}(t) = K^{\text{gov}}(t) + K^{\text{equity}}(t) + K^{\text{debt}}(t)$$

and the question the leg poses is what fraction the first term contributed at each stage and what the venture would have paid for the same amount through the other channels.

The defining property of the government channel is that it carries no claim on the residual and no claim on the control. The property may be stated compactly

$$\frac{\partial e^{\text{founder}}}{\partial K^{\text{gov}}} = 0 \qquad \text{and} \qquad \frac{\partial v^{\text{founder}}}{\partial K^{\text{gov}}} = 0$$

against the corresponding derivatives for the equity channel, which are strictly negative for the first and weakly negative for the second under the arrangements the [Governance article A287][related_post_a287_spacex_governance] documents. The property is the reason the article treats the channel as a distinct leg rather than as a variety of customer revenue, and it is the reason the three legs are analytically separable rather than substitutable.

The identification problem is the counterfactual. The counterfactual differential takes the form

$$\Delta V^{\text{gov-anchor}}_i(t) = V^{\text{observed}}_i(t) - V^{\text{private-capital counterfactual}}_i(t)$$

with the attribution equal to the difference between the observed trajectory and the counterfactual in which the development capital was raised privately on the terms available at the time. The counterfactual is unusually tractable relative to those of the preceding articles, because the terms available privately in the 2006 through 2008 period are partially documented through the rounds the Patient-Private Capital-Formation Leg article A290 will treat, and because the Rocketplane Kistler case gives an observation of what happened to a competitor that attempted the private path.

## Methodological Commitments

The article commits to the same seven methodological positions the [series opener][related_post_a281_spacex_framing] established, restated at compact reference level.

The first commitment is descriptive-analytical framing rather than prescriptive advocacy. The commitment is strained here because the COTS instrument has become a policy exemplar cited in support of procurement reforms across unrelated domains, and the literature advocating its extension is substantially larger than the literature evaluating it.

The second commitment is dual-register composition with both general-history and abstract-mechanic registers.

The third commitment is primary-source anchoring. The documentary position for this article is the strongest in the series, because the government party to every transaction is subject to disclosure obligations the private party is not. The article cites the [National Aeronautics and Space Act][ref_nasa_act_1958], the [Space Act Agreement authority at 51 USC 20113][ref_51_usc_20113], the [NASA partnerships and Space Act Agreements guidance][ref_nasa_partnerships], the [NASA Federal Acquisition Regulation Supplement][ref_nasa_far_supplement], the [Federal Acquisition Regulation Part 15][ref_far_part_15] and [Part 16][ref_far_part_16] provisions governing negotiated procurement and contract types, the [NASA commercial space documentation][ref_nasa_cots_solicitation_2006], the [NASA COTS programme literature][ref_nasa_cots_report], the [CRS-2 award announcement][ref_nasa_crs2_press_2016], the [NASA news releases][ref_nasa_news] carrying the award and termination announcements, the [Commercial Crew Program documentation][ref_nasa_ccp_documents] and [certification record][ref_nasa_ccp_certification], the [Space Force National Security Space Launch][ref_space_force_nssl] framework with the [Phase 1A][ref_space_force_nssl_phase1a_2018], [Phase 2][ref_space_force_nssl_phase2_2020], and [Phase 3 Lane 2][ref_spacenews_nssl_phase3] awards, the [Department of Defense contract announcements][ref_dod_contracts], the [Federal Procurement Data System][ref_fpds] and [USAspending][ref_usaspending] records, and the oversight record in the [GAO reports database][ref_gao_reports] and the [NASA Office of Inspector General reports database][ref_nasa_oig_reports].

The fourth commitment is contested-claim marking, with attention to the counterfactual development-cost estimates that the NASA analyses produced and that the article treats as model outputs rather than as measurements.

The fifth commitment is temporal indexing as a mid-2026 snapshot.

The sixth commitment is terminological transparency with the Terminological Note section below, with attention to the distinction between a Space Act Agreement and a Federal Acquisition Regulation contract, which are legally distinct instruments that the commentary routinely conflates.

The seventh commitment is thesis-not-proof framing of the capital-formation closure claim.

## Government Anchor Capital as an Economic Property

The government-anchor capital-formation property is treated as an economic property of the financing channel that distinguishes ventures able to fund a capability development from a customer relationship from ventures that must fund it from the capital markets.

The property has three components. The first is magnitude, concerning how much capital the channel supplied. The second is timing, concerning whether the capital arrived at the stages when the alternatives were most expensive. The third is terms, concerning what the capital cost in claims surrendered.

The cost-of-capital comparison across the channels can be written as

$$r^{\text{gov}} \ll r^{\text{equity}} \qquad \text{with} \qquad r^{\text{gov}} = \text{value of concessions granted per dollar received}$$

with the government channel carrying a cost that is not zero but that is denominated in non-financial concessions comprising reporting obligations, audit exposure, mission-assurance requirements, export-control compliance under the [ITAR provisions][ref_itar_22_cfr_120_130], and a degree of programmatic direction. The concessions are real and the article does not treat the channel as free capital. The claim is the weaker and more defensible one that the concessions are cheaper than the equity dilution the alternative would have required.

The dilution avoided admits direct computation in principle. Let $K^{\text{gov}}$ denote the government development capital and let $V$ denote the firm valuation at the time it was received. The equity that would have been surrendered to raise the same amount privately is

$$\delta^{\text{avoided}} = \frac{K^{\text{gov}}}{V + K^{\text{gov}}}$$

evaluated at the contemporaneous valuation. The expression is large when the capital is received at a low valuation, which is precisely when a development-stage venture receives it. The timing property therefore compounds the terms property rather than merely accompanying it.

The milestone structure admits treatment as an option strip. The paying party holds at each milestone the right to discontinue, and the value of the arrangement to the paying party is

$$V^{\text{payer}} = \sum_{j} \pi_j \cdot \left[ B_j - m_j \right] \qquad \text{with} \qquad \pi_j = \prod_{k < j} P\!\left( \text{milestone } k \text{ achieved} \right)$$

with the expected outlay conditional on the programme surviving to each stage. The structure caps the payer's exposure at the milestones actually achieved, which is the property that distinguishes it from a cost-reimbursement arrangement in which the payer bears the overrun.

The incentive-power parameter that the [Laffont and Tirole 1993][book_laffont_tirole_1993] apparatus defines has the form

$$b = 1 - \frac{\partial \, \text{payment}}{\partial \, \text{cost}}$$

taking the value zero for a pure cost-reimbursement arrangement in which every additional dollar of cost is reimbursed, and the value unity for a pure fixed-price arrangement in which the payment is invariant to the cost. The COTS and Commercial Crew instruments sit at or near $b = 1$, and the Constellation and Space Launch System instruments sit near $b = 0$. The parameter is the single most useful summary of the difference between the two procurement regimes the article compares.

The risk allocation follows directly from the incentive power. The overrun borne by the provider is

$$L^{\text{provider}} = b \cdot \left( C^{\text{actual}} - C^{\text{estimated}} \right)^{+}$$

with the provider bearing the entire overrun at $b = 1$ and none at $b = 0$. The transfer is the mechanism by which the fixed-price instrument converts a public cost risk into a private one, and the Boeing comparison the article develops is the clearest available demonstration of the transfer operating.

The cost-share requirement that the COTS instrument imposed is stated compactly as

$$K^{\text{private}} \geq \alpha \cdot K^{\text{gov}}$$

with the provider required to supply a matching contribution. The requirement is what converts the instrument from a subsidy into a co-investment, and it is the requirement whose failure terminated the Rocketplane Kistler agreement.

## Cross-Disciplinary Framings

The government-anchor capital-formation property can be characterized from several disciplinary traditions beyond the mission-oriented-innovation framework the series adopts as primary.

The procurement-mechanism-design tradition traces from [Laffont and Tirole 1993][book_laffont_tirole_1993] and [McAfee and McMillan 1988][book_mcafee_mcmillan_1988] through [Myerson 1981][research_myerson_1981] Optimal Auction Design, [Milgrom 2004][book_milgrom_2004] Putting Auction Theory to Work, [Bajari and Tadelis 2001][research_bajari_tadelis_2001] Incentives Versus Transaction Costs, [Bajari McMillan and Tadelis 2009][research_bajari_mcmillan_tadelis_2009], [Levin and Tadelis 2010][research_levin_tadelis_2010] Contracting for Government Services, [Corts and Singh 2004][research_corts_singh_2004], [Kalnins and Mayer 2004][research_kalnins_mayer_2004], [Che and Chung 1999][research_che_chung_1999], and [Gagnepain and Ivaldi 2002][research_gagnepain_ivaldi_2002]. The framing yields the central result that the optimal incentive power falls as the project uncertainty rises, because a fixed-price instrument applied to a poorly specified requirement produces a risk premium exceeding the efficiency gain. The result may be written

$$b^{\ast} = \arg\max_b \left[ \Delta^{\text{effort}}(b) - \tfrac{\gamma}{2} b^2 \sigma^2_{\text{cost}} \right] \qquad \text{with} \qquad \frac{\partial b^{\ast}}{\partial \sigma^2_{\text{cost}}} < 0$$

with the optimal incentive power trading the effort gain a high-powered scheme induces against the risk premium the provider demands for bearing the cost variance. The result is directly contrary to the policy lesson usually drawn from the COTS case, and the article treats the tension rather than suppressing it.

The transaction-cost tradition traces from [Coase 1937][research_coase_1937] through [Williamson 1971][research_williamson_1971], [Williamson 1975][research_williamson_1975], [Williamson 1985][book_williamson_1985], [Williamson 2002][research_williamson_2002], [Klein Crawford and Alchian 1978][research_klein_crawford_alchian_1978], [Monteverde and Teece 1982][research_monteverde_teece_1982], [Masten 1984][research_masten_1984], [Grossman and Hart 1986][research_grossman_hart_1986], [Hart and Moore 1990][research_hart_moore_1990], and [Lafontaine and Slade 2007][research_lafontaine_slade_2007]. The framing treats the bilateral-monopoly hazard that arises once a provider has invested in an asset to a single customer, and it predicts the holdup the fixed-price instrument would otherwise invite. The hazard index admits the compact form

$$h = \frac{V^{\text{asset in intended use}} - V^{\text{asset in next-best use}}}{V^{\text{asset in intended use}}}$$

with the hazard rising in the asset specificity. The SpaceX case exhibits a low value of the index relative to a typical defense programme, because the launch vehicle the government funding helped develop had commercial uses the government did not control. The low specificity is the structural reason the arrangement did not produce the holdup the framing would otherwise predict. The governance-choice rule the tradition contributes takes the form

$$\text{instrument} = \begin{cases} \text{market or agreement} & h < \bar{h} \\ \text{hierarchy or cost-reimbursement} & h \geq \bar{h} \end{cases}$$

with the threshold determined by the contracting hazard the asset specificity generates. The case sits below the threshold, and the connection to the generality-forcing condition the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats is direct, because that condition is precisely the condition that keeps $h$ low.

The entrepreneurial-finance tradition traces from [Sahlman 1990][research_sahlman_1990] through [Gompers 1995][research_gompers_1995] Optimal Investment Monitoring and the Staging of Venture Capital, [Lerner 1994][research_lerner_1994_syndication], [Kaplan and Stromberg 2003][research_kaplan_stromberg_2003], [Kaplan and Stromberg 2004][research_kaplan_stromberg_2004], [Gompers and Lerner 2001][book_gompers_lerner_2001], [Metrick and Yasuda 2011][book_metrick_yasuda_2011], and [Lerner 2009][book_lerner_2009] Boulevard of Broken Dreams. The framing treats the milestone structure as a staged financing and gives the observation that the instrument replicates substantially the monitoring function a venture investor performs, while dispensing with the equity claim that ordinarily compensates the investor for performing it. The asymmetry admits the compact statement

$$\underbrace{\text{monitoring} + \text{staging}}_{\text{both channels}} \; + \; \underbrace{\text{equity claim}}_{\text{private only}} \; \longrightarrow \; \text{cost to venture}$$

with the government channel supplying the first bracket and omitting the second. The omission is the whole of the non-dilutive property expressed in the vocabulary of the tradition. The government-programme evaluation literature in [Lerner 1996][research_lerner_1996_government_program] and [Kortum and Lerner 2000][research_kortum_lerner_2000] supplies the empirical apparatus for assessing whether the public capital displaced or complemented the private capital.

The public-economics tradition traces from [Nelson 1959][research_nelson_1959] The Simple Economics of Basic Scientific Research and [Arrow 1962][research_arrow_1962] Economic Welfare and the Allocation of Resources for Invention through [Griliches 1979][research_griliches_1979], [Griliches and Lichtenberg 1984][research_griliches_lichtenberg_1984], [Romer 1990][research_romer_1990], and [Aghion and Howitt 1992][research_aghion_howitt_1992]. The framing yields the rationale for the public expenditure, resting on the gap between the private and the social return that an appropriability failure creates. The gap can be written as

$$\Delta = r^{\text{social}} - r^{\text{private}} > 0$$

with the public intervention warranted where the gap is large and the private investment consequently below the socially optimal level. The optimal subsidy under the framing satisfies

$$s^{\ast} = \frac{r^{\text{social}} - r^{\text{private}}}{r^{\text{social}}}$$

giving the fraction of the investment the public should bear. The expression is the formal answer to the question of how large a cost share the instrument should require, and the COTS requirement was set by negotiation rather than by any such calculation.

The public-private-partnership tradition traces from [Grimsey and Lewis 2004][book_grimsey_lewis_2004] Public Private Partnerships, [Osborne 2000][book_osborne_2000], [Yescombe 2007][book_yescombe_2007], [Hodge and Greve 2007][research_hodge_greve_2007], [Bovaird 2004][research_bovaird_2004]. The framing situates the instrument within the broader family of hybrid arrangements and contributes the comparative record against which the COTS outcome should be assessed, which is substantially less favorable than the COTS advocacy literature suggests. The risk-allocation principle the tradition states is that each risk should be borne by the party best able to manage it, admitting the compact form

$$\text{assign risk } k \text{ to } \arg\min_{i} \; c_i(k)$$

with $c_i(k)$ the cost to the party $i$ of bearing the risk $k$. The principle recommends assigning the technical-execution risk to the provider and the requirement-definition risk to the agency, which is substantially the allocation the COTS instrument achieved and substantially not the allocation a fixed-price instrument on an agency-specified requirement achieves.

The mission-oriented and developmental-state tradition traces from [Mazzucato 2013][book_mazzucato_2013] The Entrepreneurial State, [Mazzucato 2021][book_mazzucato_2021] Mission Economy, [Ruttan 2006][book_ruttan_2006] Is War Necessary for Economic Growth, [Weiss 2014][book_weiss_2014] America Inc, [Hartley 2017][book_hartley_2017] The Economics of Arms, [Block 2008][research_block_2008], [Weiss and Thurbon 2021][research_weiss_thurbon_2021], [Johnson 1982][book_johnson_1982], [Amsden 1989][book_amsden_1989], [Wade 1990][book_wade_1990], and [Evans 1995][book_evans_1995] Embedded Autonomy. The framing treats the arrangement as an instance of state-directed development operating through procurement rather than through ownership or directed credit, and it provides the comparative frame within which the United States instrument differs from the East Asian instruments principally in its indirection. The instrument set admits compact enumeration by the channel through which the state acts

$$\mathcal{I} = \left\{ \text{ownership}, \; \text{directed credit}, \; \text{tariff}, \; \text{subsidy}, \; \text{procurement} \right\}$$

with the United States arrangement operating substantially through the last element alone while the East Asian arrangements operated across several. The narrowness of the channel is what permits the arrangement to be described domestically as a market mechanism rather than as an industrial policy.

The defense-industrial and rent-seeking tradition traces from [Melman 1970][book_melman_1970] Pentagon Capitalism, [Fallows 1981][book_fallows_1981] National Defense, [Hunter 2016][book_hunter_2016] Creating Strategic Value, [Kaplan 1991][book_kaplan_1991] The Wizards of Armageddon, [Buchanan and Tullock 1962][book_buchanan_tullock_1962], [Stigler 1971][research_stigler_1971], and [Krueger 1974][research_krueger_1974]. The framing treats the arrangement as a transfer to a concentrated private interest and supplies the skeptical reading the article treats in the Alternative Analytical Frameworks section. The concentration the framing tracks has the form

$$H^{\text{provider}} = \sum_j s_j^2 \qquad \text{with} \qquad s_j = \frac{\text{awards to provider } j}{\text{total awards}}$$

with the index falling across the 2006 through 2015 period as the entrant took share from the incumbent, and rising thereafter as the entrant consolidated. The non-monotonicity is the quantitative form of the policy question the article raises in the Contemporary Comparative Landscape section.

The innovation-policy and programme-evaluation tradition traces from [Bonvillian 2018][research_bonvillian_2018] on the DARPA institutional model, the [Heilmeier Catechism][ref_heilmeier_catechism] as the programme-selection instrument, [Freeman 1987][book_freeman_1987], [Lundvall 1992][book_lundvall_1992], [Nelson 1993][book_nelson_1993], and [Mowery and Rosenberg 1998][book_mowery_rosenberg_1998]. The selection discipline the tradition offers can be stated as a screening condition applied before any award

$$\text{fund} \iff \left[ \text{objective specifiable} \right] \wedge \left[ \text{current practice inadequate} \right] \wedge \left[ \text{success testable} \right] \wedge \left[ \text{consequence material} \right]$$

with the conjunction required. The framing gives the comparative set of public instruments against which the Space Act Agreement should be located.

The systems-engineering tradition traces from [Blanchard and Fabrycky 2011][book_blanchard_fabrycky_2011] Systems Engineering and Analysis and [Buede 2009][book_buede_2009] The Engineering Design of Systems through [Suh 2001][book_suh_2001] Axiomatic Design, [Maier 1998][research_maier_1998] Architecting Principles for Systems-of-Systems, [Sage and Cuppan 2001][research_sage_cuppan_2001], the [INCOSE Systems Engineering Handbook][ref_incose_handbook], and the [NASA Systems Engineering Handbook][ref_nasa_se_handbook]. The framing yields the apparatus for the question the milestone decomposition poses, which is how a development is partitioned into increments that are separately verifiable. The partition problem is a systems-architecture problem before it is a contracting problem, and the X-33 comparison the article develops turns entirely on it.

The organizational-learning tradition traces from [March and Simon 1958][book_march_simon_1958] Organizations and [Cyert and March 1963][book_cyert_march_1963] A Behavioral Theory of the Firm through [Argyris and Schon 1978][book_argyris_schon_1978] Organizational Learning, [Levitt and March 1988][research_levitt_march_1988], [Huber 1991][research_huber_1991], [March 1991][research_march_1991], [Nonaka 1994][research_nonaka_1994], [Nonaka and Takeuchi 1995][book_nonaka_takeuchi_1995] The Knowledge-Creating Company, [Senge 1990][book_senge_1990] The Fifth Discipline, [Cohen and Levinthal 1990][research_cohen_levinthal_1990], [Kogut and Zander 1992][research_kogut_zander_1992], [Grant 1996][research_grant_1996], [Argote and Ingram 2000][research_argote_ingram_2000], and [Argote and Miron-Spektor 2011][research_argote_miron_spektor_2011]. The framing applies to the agency rather than to the provider and provides the account of how a programme office accumulates the evaluative capability the preceding section identifies as the binding constraint.

The learning-curve tradition traces from [Wright 1936][research_wright_1936] Factors Affecting the Cost of Airplanes through [Alchian 1963][research_alchian_1963] Reliability of Progress Curves, [Rapping 1965][research_rapping_1965], [Argote and Epple 1990][research_argote_epple_1990], [Argote 1999][book_argote_1999] Organizational Learning, [Adler and Clark 1991][research_adler_clark_1991], [Lieberman 1984][research_lieberman_1984], and [Dutton and Thomas 1984][research_dutton_thomas_1984]. The framing bears on the counterfactual cost estimate the article treats as contested, because the parametric models the estimate employs are calibrated on a historical experience base whose learning rates may not transfer to a different production organization. The transfer question can be stated as

$$b^{\text{historical}} \stackrel{?}{=} b^{\text{provider}}$$

with the estimate assuming equality and the case being one in which the production organization differed substantially from the calibration sample.

The institutional-economics tradition traces from [North 1990][book_north_1990] Institutions Institutional Change and Economic Performance through [Ostrom 1990][book_ostrom_1990] Governing the Commons, [Greif 2006][book_grief_2006] Institutions and the Path to the Modern Economy, and [Acemoglu and Robinson 2012][book_acemoglu_robinson_2012] Why Nations Fail. The framing situates the instrument as one rule within a broader institutional configuration and offers the caution that a rule transplanted without its supporting institutions does not reproduce its effects.

The reliability and mission-assurance tradition traces from [Perrow 1984][book_perrow_1984] Normal Accidents through [Vaughan 1996][book_vaughan_1996] The Challenger Launch Decision, [Weick and Sutcliffe 2007][book_weick_sutcliffe_2007] Managing the Unexpected, [O'Connor and Kleyner 2012][book_oconnor_kleyner_2012] Practical Reliability Engineering, [Musa 1998][book_musa_1998] Software Reliability Engineering, [Duane 1964][research_duane_1964], and the [NASA reliability and mission-assurance standards][ref_nasa_std_8709_22]. The framing contributes the content of the mission-assurance concessions the economic-property section identifies as part of the cost of the channel, and the [Columbia Accident Investigation Board report][ref_caib_report_2003] and [Rogers Commission report][ref_rogers_commission_1986] supply the institutional history from which the requirements derive.

The industrial-organization tradition traces from [Bain 1968][book_bain_1968] Industrial Organization through [Scherer and Ross 1990][book_scherer_ross_1990] Industrial Market Structure and Economic Performance, [Tirole 1988][book_tirole_1988] The Theory of Industrial Organization, [Porter 1980][book_porter_1980] Competitive Strategy, [Porter 1985][book_porter_1985] Competitive Advantage, [Baumol 1977][research_baumol_1977], [Kahn 1988][book_kahn_1988] The Economics of Regulation, and [Sharkey 1982][book_sharkey_1982] The Theory of Natural Monopoly. The framing gives the apparatus for the concentration question the article raises in its closing sections, and the antitrust treatments in [Bork 1978][book_bork_1978], [Posner 2001][book_posner_2001], [Hovenkamp 2005][book_hovenkamp_2005], and [Khan 2017][research_khan_2017] supply the normative frame.

The economic-history tradition traces from [Landes 1969][book_landes_1969] The Unbound Prometheus, [Rosenberg 1976][book_rosenberg_1976] Perspectives on Technology, [Rosenberg 1982][book_rosenberg_1982] Inside the Black Box, [Mowery and Rosenberg 1998][book_mowery_rosenberg_1998] Paths of Innovation, [Chandler 1962][book_chandler_1962] Strategy and Structure, [Chandler 1977][book_chandler_1977] The Visible Hand, [Chandler 1990][book_chandler_1990] Scale and Scope, and [Hughes 1983][book_hughes_1983] Networks of Power. The framing provides the long-run comparative record within which the arrangement is a recent instance of a recurring relationship between a state and a private producer.

## The Space Act Agreement Instrument

The legal instrument under which the COTS development capital was extended deserves treatment before the history, because substantially every distinctive feature of the arrangement follows from it and because the commentary routinely describes the arrangement as a contract when it was not one.

The [National Aeronautics and Space Act][ref_nasa_act_1958] confers on the agency an authority to enter into agreements other than contracts, grants, and cooperative agreements, codified at the [51 USC 20113 provisions][ref_51_usc_20113] and described in the [NASA partnerships and Space Act Agreements guidance][ref_nasa_partnerships]. The authority is the civil-agency analogue of the other-transaction authority that the defense agencies hold at the [10 USC 2371b provisions][ref_10_usc_2371b] and that the [Department of Defense other-transactions resources][ref_dod_other_transactions] describe. The related commercial-space authority appears at the [51 USC 51302 provisions][ref_51_usc_51302_saa], and the agency's internal programme-management framework at the [NASA programme and project management requirements][ref_nasa_npr_7120_5f].

The consequence of proceeding under the authority rather than under the [Federal Acquisition Regulation][ref_far_part_15] is that substantially the entire regulatory apparatus governing specific federal procurement does not apply. The cost-accounting standards do not apply. The certified cost-or-pricing-data requirements do not apply. The contract-type framework that the [Federal Acquisition Regulation Part 16][ref_far_part_16] establishes does not apply, nor do the commercial-item procedures at [Part 12][ref_far_part_12] or the research-and-development contracting provisions at [Part 35][ref_far_part_35]. The intellectual-property allocation is negotiated rather than prescribed, which the [Data Rights and Intellectual Property article A164][related_post_a164_patents_trade_secrets] treats in the adjacent context. The bid-protest jurisdiction is substantially narrower. The international framework within which the resulting launches operate is unaffected by the instrument choice and comprises the [United Nations Outer Space Treaty of 1967][ref_un_outer_space_treaty_1967], the [Liability Convention of 1972][ref_un_liability_convention_1972], and the [Registration Convention of 1976][ref_un_registration_convention_1976], with the scholarly treatment in the [Journal of Space Law][ref_journal_space_law].

The regulatory burden removed admits compact statement as the difference in the compliance cost a provider must bear

$$C^{\text{compliance}}_{\text{FAR}} - C^{\text{compliance}}_{\text{agreement}} > 0$$

with the difference constituting a fixed entry cost that scales poorly with the provider's size. The consequences cut in both directions and the article states both. The absence of the cost-accounting apparatus is what permitted a provider without a government-compliant accounting system to participate at all, which is the barrier that excludes substantially every venture-stage firm from traditional defense procurement. The same absence removes the visibility into the provider's costs that the apparatus exists to supply, so that the agency purchasing under the instrument cannot determine whether the price it pays bears any relation to the cost incurred.

The instrument's defining operational feature is that it is an agreement rather than a procurement, so that the agency is not purchasing a deliverable but is contributing to a jointly pursued objective. The distinction may be stated compactly

$$\text{procurement} \; : \; \text{agency receives title to a deliverable} \qquad \text{against} \qquad \text{agreement} \; : \; \text{agency receives a demonstrated capability in the market}$$

with the second producing no asset the agency owns. The residual-claim structure is stated compactly as

$$\text{title}^{\text{agency}} = \varnothing \qquad \text{while} \qquad \text{capability}^{\text{market}} > 0$$

with the agency holding no asset and the market gaining a capability. The structure is the reason the capability the funding produced remained available for the commercial and defense applications that the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] documents, rather than becoming a government asset subject to government disposition.

## COTS Round One 2006 through 2008

The Commercial Orbital Transportation Services programme was announced in the January 2006 period and the round-one awards were made in the August 2006 period. The record appears in the [NASA commercial space documentation][ref_nasa_cots_solicitation_2006] and the [NASA COTS programme literature][ref_nasa_cots_report].

The round-one awards went to two providers. The SpaceX award was approximately 278 million dollars against a milestone schedule covering the Falcon 9 launch vehicle and the Dragon spacecraft. The Rocketplane Kistler award was approximately 207 million dollars against a milestone schedule covering the K-1 vehicle. The two-provider structure was itself a design choice with an analytical rationale. The probability that at least one provider succeeds under independent execution risk is

$$P(\text{at least one succeeds}) = 1 - \prod_{j} \left( 1 - p_j \right)$$

which exceeds the single-provider probability at a cost equal to the sum of the awards. The structure is the same parallel-track logic the [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] treats, applied by the payer across providers rather than by a venture across lines. The figures are reported in the [NASA COTS programme history of 2011][ref_nasa_cots_2011] and the [NASA COTS programme literature][ref_nasa_cots_report], and are among the few quantities in this series that are directly documented rather than reconstructed.

The structural features of the round-one awards that bear on the capital-formation question are four. The awards were milestone-based rather than cost-reimbursed. The awards required a private cost share. The awards conveyed no equity and no governance rights. The awards were terminable at the agency's discretion upon a milestone failure without a termination-for-convenience settlement of the kind a Federal Acquisition Regulation contract would require.

The four features admit compact statement as the instrument's parameter vector

$$\left( b, \; \alpha, \; \Delta e, \; S \right) = \left( 1, \; \alpha > 0, \; 0, \; 0 \right)$$

comprising the unit incentive power, the positive cost share, the zero dilution, and the zero termination settlement. The fourth feature is the one that makes the instrument work and is the one most often omitted from the summaries. An agency that must pay a settlement to discontinue a failing programme faces an option value in continuation that an agency facing no settlement does not. The difference admits the compact statement

$$V^{\text{continue}} - V^{\text{terminate}} = \left[ \text{expected completion value} \right] - \left[ - S \right] \qquad \text{with} \qquad S = 0 \text{ under the agreement}$$

with the settlement term vanishing under the instrument, which lowers the threshold at which the agency will in fact terminate. The Rocketplane Kistler case demonstrates the mechanism operating.

## The Rocketplane Kistler Termination

The Rocketplane Kistler agreement was terminated in the 2007 period after the provider failed to satisfy a financing milestone requiring it to raise a private capital sum. The termination is recorded in the [NASA news releases][ref_nasa_news] and treated in the programme evaluations at the [GAO 2009 COTS evaluation][ref_gao_cots_2009] and the [NASA Office of Inspector General 2013 COTS evaluation][ref_nasa_oig_cots_2013].

The case is analytically important for three reasons that the commentary generally reduces to one.

The first and most frequently noted is that the instrument permitted a rapid termination. The agency recovered the unobligated balance and re-competed the position, awarding it to a second provider in the 2008 period as the [NASA news releases][ref_nasa_news] record. The recovery can be stated as

$$R^{\text{agency}} = K^{\text{obligated}} - K^{\text{disbursed}} \qquad \text{against} \qquad R^{\text{agency}} = -S \quad \text{under a cost-plus termination}$$

with the agency recovering the unobligated balance under the agreement and paying a settlement under the contract. A comparable failure under a cost-plus development contract would have produced an extended termination process and a settlement.

The second and more analytically interesting is that the failed milestone was a financing milestone rather than a technical one. The instrument conditioned the public capital on the provider's ability to raise the private capital, which makes the public channel and the private channel complements rather than substitutes by explicit design. The structure may be stated compactly

$$m_j \text{ released} \iff \left[ \text{technical milestone } j \text{ achieved} \right] \wedge \left[ K^{\text{private}} \geq \alpha K^{\text{gov}} \right]$$

with the conjunction required. The design uses the private capital market as an external validator of the provider's prospects, which economizes on the agency's own assessment capability. The mechanism is the same one the SBIR programme employs through its Phase II commercialization requirements, which the [Money Behind an SBIR or STTR Award article A140][related_post_a140_sbir_money] treats.

The third is that the case offers the counterfactual observation the identification problem requires. A competitor holding a substantially similar award at a substantially similar stage attempted the private-capital path and failed to complete it. The inferential value of the observation admits careful statement. Let $A$ denote the event that a similarly situated firm can complete a private raise. The observation establishes

$$P(A) < 1 \qquad \text{and not} \qquad P(A \mid \text{SpaceX}) = 0$$

with the single failure bounding the probability away from certainty without identifying it for any other firm. The observation does not establish that the SpaceX private raise would have failed, and it does establish that the private path was not freely available to a similarly situated firm in the same period.

## COTS Milestone Mechanics and the Non-Dilutive Property

The analytical core of this article is the observation that the COTS payments functioned as development capital and carried no claim on the firm. The section states the claim precisely and then states what it does not establish.

The SpaceX COTS award grew through amendments to approximately 396 million dollars across the agreement period. The capital was received across the 2006 through 2012 interval, which spans the period the [series opener][related_post_a281_spacex_framing] identifies as the near-death moment and the period in which the firm's private valuation was at its lowest. The coincidence is the whole of the timing argument, because the dilution a dollar of capital costs is inversely proportional to the valuation at which it is raised

$$\frac{\partial \delta}{\partial V} < 0 \qquad \text{so that} \qquad \delta \Big|_{V \text{ low}} \gg \delta \Big|_{V \text{ high}}$$

with the capital arriving precisely when the alternative was most expensive.

The non-dilutive property admits the compact comparison. The approximately 396 million dollars received through the channel, had it instead been raised as equity at the valuations prevailing across the interval, would have required surrendering a fraction

$$\delta^{\text{avoided}} = \frac{K^{\text{COTS}}}{V + K^{\text{COTS}}}$$

that is substantial at the contemporaneous valuations and that would have compounded against every subsequent round. The compounding is the feature that makes the timing decisive. A dilution avoided early is a dilution avoided in every later round, because the founder share entering each subsequent round is higher than it would otherwise have been. The cumulative effect may be written

$$e^{\text{founder}}_N = \left[ e_0 - \delta^{\text{avoided}} \right] \prod_{n=1}^{N} \left( 1 - \delta_n \right) \qquad \text{against} \qquad e_0 \prod_{n=1}^{N} \left( 1 - \delta_n \right)$$

with the difference persisting across the entire subsequent financing sequence rather than being confined to the round it displaced. The connection to the [Governance article A287][related_post_a287_spacex_governance] is direct, because the control condition that article analyzes depends on the founder's residual share, and the government channel raised the share available at every subsequent stage.

The claim the article does not make deserves equal prominence. The analysis does not establish that the government capital was necessary, because the counterfactual in which the firm raised the same amount privately at a worse price is not obviously infeasible. The analysis does not establish that the government capital was efficiently deployed, because the counterfactual social return on the same appropriation directed elsewhere is not estimated. The three propositions admit compact separation

$$\underbrace{\text{terms were favorable}}_{\text{established}} \; \not\Rightarrow \; \underbrace{\text{capital was necessary}}_{\text{not established}} \; \not\Rightarrow \; \underbrace{\text{expenditure was efficient}}_{\text{not established}}$$

with only the first supported by the evidence the article assembles. The analysis establishes the narrower proposition that the capital arrived on terms substantially more favorable than the alternatives available at the time, and that the favorable terms compounded.

## The Commercial Resupply Services Transition

The transition from the development agreement to the services contract occurred in the December 2008 period with the award of the Commercial Resupply Services contracts, recorded in the [NASA news releases][ref_nasa_news] and treated at length in the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand].

The transition changes the instrument's character in a way the capital-formation analysis must register. The CRS contracts were procurement contracts rather than agreements, and the payments were for delivered services rather than against development milestones. The channel therefore ceased to be a capital-formation channel and became a revenue channel at the moment of the transition.

The analytical consequence is that the government-anchor capital-formation leg has a bounded duration. The leg operated across the 2006 through approximately 2012 interval, and thereafter the government relationship supplied revenue rather than capital. The bounded duration is stated compactly as

$$K^{\text{gov}}(t) \approx \text{constant} \qquad \text{for} \qquad t > t^{\text{transition}}$$

with the cumulative government development capital reaching a plateau while the government revenue continued to grow. The two quantities the commentary conflates admit compact separation

$$\frac{K^{\text{gov}}}{K^{\text{total}}} \Bigg|_{\text{cumulative, development era}} \qquad \text{against} \qquad \frac{R^{\text{gov}}(t)}{R^{\text{total}}(t)} \Bigg|_{\text{current}}$$

with the first a historical capital share that is fixed and the second a current revenue share that has declined as the commercial lines grew. The distinction matters because the commentary that describes the firm as government-funded conflates a bounded historical capital contribution with a continuing commercial relationship, and the two have different implications for substantially every question the series treats.

The subsequent [CRS-2 award][ref_nasa_crs2_press_2016] of the 2016 period extended the services relationship without reopening the capital-formation channel. The execution record across the two contracts is documented in the [NASA Commercial Resupply Services programme overview][ref_nasa_crs_program_overview] and in the SpaceX press record covering the [Dragon C1 demonstration of 2010][ref_spacex_press_dragon_c1_2010], the [CRS-1 mission of 2012][ref_spacex_press_crs1_2012], the [CRS-7 loss of 2015][ref_spacex_press_crs7_2015], and the [CRS-21 mission of 2020][ref_spacex_press_crs21_2020].

## Commercial Crew and the Fixed-Price Competition

The Commercial Crew progression partially reopened the capital-formation channel for a second capability. The programme proceeded through the Commercial Crew Development awards of the 2010 and 2011 periods, the Commercial Crew Integrated Capability awards of the 2012 period, and the Commercial Crew Transportation Capability awards of the September 2014 period. The record appears in the [NASA Commercial Crew Program documentation][ref_nasa_ccp_documents], the [certification record][ref_nasa_ccp_certification], and the evaluations at the [GAO 2014 Commercial Crew evaluation][ref_gao_2014_commercial_crew], the [GAO 2019 evaluation][ref_gao_ccp_2019], the [GAO 2020 evaluation][ref_gao_2020_commercial_crew], the evaluations in the [NASA Office of Inspector General reports database][ref_nasa_oig_reports], and the [Congressional Research Service Commercial Crew report][ref_crs_commercial_crew].

The early phases were conducted under Space Act Agreements and the final phase under a Federal Acquisition Regulation contract, which reflects a deliberate progression from a development instrument to a procurement instrument as the requirement became specifiable. The progression is the practical answer to the mechanism-design result that the optimal incentive power falls with the uncertainty. The staged instrument choice admits the compact statement

$$b^{\ast}(t) = b^{\ast}\!\left( \sigma^2_{\text{cost}}(t) \right) \qquad \text{with} \qquad \sigma^2_{\text{cost}}(t) \text{ declining in } t$$

with the instrument tightening as the requirement becomes specifiable. The arrangement applies the high-powered instrument at the stage where the provider knows more than the agency and the specified instrument at the stage where the requirement is stable.

The CCtCap awards were approximately 4.2 billion dollars to one provider and approximately 2.6 billion dollars to the second, recorded in the [NASA Commercial Crew certification record][ref_nasa_ccp_certification]. The award structure is a fixed-price arrangement with milestone payments, so the incentive-power parameter sits near unity. The dual-award structure preserved the parallel-track property at the operational stage, and the price differential between the two awards admits the compact expression

$$\frac{P^{\text{high}} - P^{\text{low}}}{P^{\text{low}}} \approx 0.6$$

which the agency accepted in exchange for the redundancy the second provider supplied. The subsequent execution record establishes that the redundancy was not decorative.

## The Boeing Comparison and Risk Transfer

The comparison between the two Commercial Crew providers constitutes the clearest available natural experiment in the procurement literature, because the two providers executed a substantially identical requirement under a substantially identical instrument across an identical period.

The outcome differed substantially. The one provider achieved the uncrewed demonstration flight of the [Demo-1 mission in March 2019][ref_spacex_press_demo1_2019], the crewed demonstration flight of the [Demo-2 mission in May 2020][ref_spacex_press_dm2_2020], and the first operational rotation of the [Crew-1 mission in November 2020][ref_spacex_press_crew1_2020]. The other encountered a sequence of development difficulties including an uncrewed flight-test anomaly in the December 2019 period, a repeat uncrewed flight in the 2022 period, and propulsion difficulties during the crewed flight test of the June 2024 period that the [Boeing Starliner programme record][ref_boeing_starliner_cft_2024] documents.

The capital-formation significance is not the schedule difference but the cost incidence. Under the fixed-price instrument the overrun was borne by the provider and recorded as a charge against its earnings, rather than being reimbursed. The reported cumulative charges are substantial and are documented in the provider's public filings accessible through the [Securities and Exchange Commission EDGAR][ref_sec_edgar] system and summarized in the [Boeing press releases][ref_boeing_press]. The transfer can be stated as

$$L^{\text{public}} = (1 - b) \cdot \left( C^{\text{actual}} - C^{\text{estimated}} \right)^{+} \approx 0 \qquad \text{at} \qquad b \approx 1$$

with the public exposure approaching zero. The incidence comparison across the two instrument classes admits the compact tabulation

$$\left( L^{\text{public}}, \; L^{\text{provider}} \right) = \begin{cases} \left( 0, \; \Delta C \right) & \text{fixed price} \\ \left( \Delta C, \; 0 \right) & \text{cost reimbursement} \end{cases}$$

with the overrun falling entirely on one party or the other. The comparison against the cost-plus counterfactual that the article treats below is the substantive demonstration that the instrument accomplished the risk transfer it was designed to accomplish.

The qualification the article records is that the risk transfer is only credible where the provider can in fact absorb the loss. A fixed-price instrument imposed on a provider without the balance sheet to absorb an overrun does not transfer the risk. It converts it into a completion risk borne by the agency in a different form. The credibility condition may be stated compactly

$$\text{risk transferred} \iff \Delta C \leq W^{\text{provider}}$$

with $W^{\text{provider}}$ the provider's capacity to absorb the loss, and with the transfer failing whenever the overrun exceeds it. The condition is the failure mode the defense-procurement literature documents extensively and which the Rocketplane Kistler case illustrates in the development setting.

## National Security Space Launch Certification

The defense channel operated on a different principle from the civil channel and deserves separate treatment. The National Security Space Launch programme, formerly the Evolved Expendable Launch Vehicle programme, purchases specific launch services rather than funding development, and the channel therefore supplied substantially revenue rather than capital across most of its history. The record appears in the [Space Force National Security Space Launch][ref_space_force_nssl] framework documentation, the [Phase 1A award record][ref_space_force_nssl_phase1a_2018], the [Phase 2 award record][ref_space_force_nssl_phase2_2020], the [Phase 3 Lane 2 coverage][ref_spacenews_nssl_phase3], the [GAO 2023 National Security Space Launch evaluation][ref_gao_nssl_2023], and the [Space Force news][ref_space_force_news] and [Department of Defense contract announcements][ref_dod_contracts].

The launch infrastructure on which the certified missions depend is itself partly a government asset made available on negotiated terms, comprising the [Kennedy Space Center Launch Complex 39A arrangement][ref_ksc_lc39a_lease], the [Vandenberg environmental record][ref_vandenberg_slc4e_ea], and in the earliest period the [Kwajalein Atoll range documentation][ref_kwajalein_atoll_documentation]. The licensing regime under which the operations proceed is the [FAA commercial space transportation regulations][ref_faa_ast_regulations] and the [Part 450 licensing requirements][ref_faa_ast_licensing_regs_450], with the current authorizations recorded in the [FAA current launch licenses][ref_faa_launch_licenses_current]. The capital-formation content of the defense channel lies in a different place. The certification process itself is a substantial fixed investment that the provider must make and that the programme partially funds, and the certification once obtained is a durable asset that raises the provider's value independently of any mission awarded. The certification therefore functions as a capital contribution in kind rather than in cash, admitting the compact statement

$$\Delta V^{\text{certification}} = \sum_{t} \frac{p^{\text{award}}(t) \cdot \pi^{\text{margin}}}{(1+\rho)^t} \; - \; C^{\text{certification}}$$

with the certification's value equal to the discounted expected award stream it makes accessible net of the investment required to obtain it. The certification therefore behaves as a barrier whose height is symmetric in construction and asymmetric in effect, admitting the compact statement

$$C^{\text{certification}} \text{ identical across entrants} \qquad \text{while} \qquad \frac{C^{\text{certification}}}{R^{\text{existing}}} \text{ differs by orders of magnitude}$$

with the fixed cost trivial for an incumbent holding a large existing revenue base and prohibitive for an entrant holding none.

The Phase 2 award of the 2020 period allocated the mission set between two providers on an announced split, and the Phase 3 structure of the 2024 period established a two-lane arrangement admitting a broader provider set into the less demanding lane. The progression can be stated compactly through the provider count admitted to the competed mission set

$$n^{\text{providers}} \; : \; 1 \longrightarrow 2 \longrightarrow 3+$$

across the pre-2015, Phase 2, and Phase 3 periods respectively. The progression from a single-provider arrangement through a duopoly to a multi-provider structure across the two decades is the competitive outcome the programme reforms were intended to produce.

## The Litigation and Entry Path

The entry path into the defense channel is not adequately described as a certification process, because the entry was contested and the contest was resolved partly through litigation.

The provider filed suit against the Air Force in the 2014 period challenging a sole-source block award to the incumbent. The matter was resolved by a settlement in the 2015 period, and the certification followed later that year. The bid-protest and claims apparatus that the [GAO bid-protest function][ref_gao_bid_protest] and the [United States Court of Federal Claims][ref_uscfc] administer is the institutional channel through which the contest proceeded. The decision to pursue it is stated compactly as

$$\text{litigate} \iff p^{\text{prevail}} \cdot V^{\text{channel access}} > C^{\text{legal}} + C^{\text{relationship}}$$

with the second cost term capturing the damage a contest inflicts on an ongoing customer relationship, which is the term that deters substantially every incumbent supplier from bringing one.

The capital-formation significance is that the entry into the channel required an investment in legal and political action distinct from the technical investment, and that the investment was available to a firm holding a patient private capital base and would not have been available to a firm dependent on near-term contract revenue. The dependency admits the compact statement

$$K^{\text{gov}} \; \text{accessible} \; \Leftarrow \; \text{legal contest} \; \Leftarrow \; K^{\text{private, patient}}$$

with the government channel's accessibility conditioned on a prior private expenditure. The observation connects the three capital-formation legs, because the patient private leg that the Patient-Private Capital-Formation Leg article A290 will treat financed the contest that opened the government channel.

## Starshield and the Classified Anchor

The Starshield business that the [SpaceX Starshield documentation][ref_spacex_starshield] describes at the unclassified level and that the [Reuters 2024 investigation][research_reuters_starshield_2024] and the [New York Times 2024 coverage][ref_nyt_starshield_2024] reconstructed represents a further stage of the government relationship in which the government is purchasing a capability the firm developed substantially on its own account.

The direction of the capital flow has therefore reversed relative to the COTS period. In the earlier period the government supplied capital to build a capability that did not exist. In the later period the firm supplied a capability built with commercial capital and the government purchased access to it. The reversal can be stated as

$$\text{sign}\!\left( \frac{\partial K^{\text{firm}}}{\partial \, \text{government relationship}} \right) \; : \; + \text{ in the development period}, \; - \text{ in the current period}$$

with the firm now investing ahead of the government requirement rather than the reverse. The reversal admits the compact statement as a change in the temporal ordering

$$t^{\text{gov capital}} < t^{\text{capability}} \qquad \text{becomes} \qquad t^{\text{capability}} < t^{\text{gov purchase}}$$

with the ordering inverted between the two eras. The reversal is the completion of the capital-formation leg and the reason the article treats the leg as historically bounded.

## SBIR Phase III Sole-Source Authority as Structural Analogue

The Small Business Innovation Research programme yields the closest statutory analogue to the structural pattern the COTS-to-CRS sequence exhibits, and the analogy is instructive precisely because the statutory mechanism is explicit where the COTS mechanism was not.

The programme operates under the [statutory authority at 15 USC 638][ref_sbir_statute_15usc638] and the [Small Business Administration policy directive][ref_sba_sbir_policy_directive] documented through the [SBIR programme portal][ref_sbir_gov]. The programme is treated comprehensively in the [Introduction to the SBIR and STTR Programs article A132][related_post_a132_sbir_intro], and the Phase III mechanism in the [Phase III and the Valley of Death article A138][related_post_a138_sbir_phase3], with the funding mechanics in the [Money Behind an SBIR or STTR Award article A140][related_post_a140_sbir_money].

The Phase III authority permits an agency to award a follow-on contract deriving from earlier programme work without a further competition, and without a dollar limit. The authority is the statutory recognition of a structural fact, namely that a development award creates a provider who is thereafter uniquely positioned, and that requiring a fresh competition at the follow-on stage would either produce a foregone conclusion or would transfer the benefit of the development investment to a competitor who did not make it.

The structural pattern may be stated compactly

$$\text{development award} \longrightarrow \text{capability} \longrightarrow \text{position} \longrightarrow \text{follow-on award}$$

with the chain operating whether or not a statute names it. The competitive consequence is stated compactly as

$$P\!\left( \text{win follow-on} \mid \text{received development award} \right) \gg P\!\left( \text{win follow-on} \right)$$

with the conditional probability substantially exceeding the unconditional one irrespective of whether the follow-on is formally competed. The COTS-to-CRS sequence was formally competed and the SBIR Phase III sequence is formally exempt from competition, and the two nonetheless produce a substantially similar outcome, because the competition at the follow-on stage is conducted among providers whose relative positions the prior development stage established.

The analytical value of the analogy is that it identifies what a government-anchor capital-formation leg actually transfers. It does not principally transfer money. It transfers position, and the money is the mechanism by which the position is created. A venture evaluating the leg should therefore assess the follow-on position the development award would establish rather than the development award's magnitude, The valuation the assessment requires admits the compact form

$$V^{\text{award}} = \underbrace{K^{\text{development}}}_{\text{visible}} + \underbrace{P\!\left( \text{follow-on} \right) \cdot V^{\text{follow-on position}}}_{\text{usually dominant}}$$

with the second term ordinarily exceeding the first by a substantial multiple. This is the assessment the SBIR practitioner literature the series treats makes explicitly.

## The Agency-Side Capability Requirement

The article to this point has treated the instrument as though its properties inhered in the document. They do not. Every property the preceding sections attribute to the instrument requires an agency capable of exercising it, and the capability is neither automatic nor evenly distributed. The section states the requirement because the advocacy literature that recommends extending the instrument to other domains substantially omits it.

The instrument requires the agency to perform four functions that a cost-reimbursement arrangement does not require. The agency must specify a milestone that is verifiable without access to the provider's cost records. The agency must verify the milestone when the provider claims it. The agency must decline to pay when the milestone is not met. And the agency must terminate when the pattern of failures warrants it, against the institutional pressure that every programme generates in favor of continuation.

The fourth function is the one that fails most often. The termination decision admits the compact statement

$$\text{terminate} \iff E\!\left[ V^{\text{completion}} \mid \mathcal{F}_t \right] < \sum_{j > J(t)} m_j + C^{\text{political}}$$

with $C^{\text{political}}$ the institutional cost the deciding official bears personally and the benefit accruing diffusely. The asymmetry between a concentrated cost and a diffuse benefit is the standard public-choice account of why programmes persist, and the Space Act Agreement reduces the first term in the inequality without touching the second.

The capability the functions jointly require is what the developmental-state literature terms embedded autonomy. The concept that [Evans 1995][book_evans_1995] Embedded Autonomy develops requires an agency close enough to the industry to evaluate a technical claim and distant enough from it to decline one. The two requirements pull against each other, and the balance can be stated as

$$\Sigma^{\text{agency}} = \min\left\{ \text{technical proximity}, \; \text{institutional distance} \right\}$$

with the capability governed by whichever specific element is weaker rather than by their sum. An agency with deep technical knowledge and close industry ties evaluates well and cannot refuse. An agency with strong independence and thin technical knowledge refuses arbitrarily. The comparative literature in [Johnson 1982][book_johnson_1982] MITI and the Japanese Miracle, [Amsden 1989][book_amsden_1989] Asia's Next Giant, [Wade 1990][book_wade_1990] Governing the Market, [Woo-Cumings 1999][book_woo_cumings_1999] The Developmental State, and [Chang 2002][book_chang_2002] Kicking Away the Ladder documents the institutional arrangements under which other states have attempted the balance.

The agency-side literature on the particular agency is unusually candid and is worth citing directly rather than through the procurement abstraction. The treatments in [McCurdy 1994][book_mccurdy_1994] Inside NASA, [Handberg 1994][book_handberg_1994] Reinventing NASA, [Launius 1994][book_launius_1994] NASA A History of the United States Civil Space Program, [McDougall 1985][book_mcdougall_1985] The Heavens and the Earth, [Hargrove 1994][book_hargrove_1994] Prisoners of Myth, [Selznick 1949][book_selznick_1949] TVA and the Grass Roots, and [Klerkx 2004][book_klerkx_2004] Lost in Space document the organizational culture and the goal-displacement hazard within which the programme office operated. The programme-office model the [DARPA institutional treatment][research_bonvillian_2018] describes and the [Heilmeier Catechism][ref_heilmeier_catechism] states contributes the comparative benchmark for an agency-side selection capability.

The personnel dimension is the one the documentary record covers least well and the participant accounts cover best. The programme required a small number of individuals willing to accept a personal career risk in exchange for an institutional outcome, which is a resource no appropriation creates. The accounts in [Berger 2021][book_berger_2021] Liftoff, [Berger 2024][book_berger_2024] Reentry, [Davenport 2018][book_davenport_2018] The Space Barons, and [Fernholz 2018][book_fernholz_2018] Rocket Billionaires document the individuals on both sides of the transaction.

The implication for the policy question is direct and is the reason the section exists. A jurisdiction that adopts the instrument without the agency-side capability obtains the reduced oversight without the compensating selection discipline, which is strictly worse than the arrangement it replaced. The instrument is not a substitute for a capable agency. It is a tool that a capable agency can use and that an incapable one should not.

## The Cost-Plus Counterfactual

The counterfactual against which the instrument should be assessed is not an absence of government funding but the alternative instrument the same agency employed contemporaneously for a comparable objective.

The Constellation programme and the Space Launch System that the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats as generality-forcing negation cases were procured under cost-reimbursement arrangements with incentive-power parameters near zero. The record appears in the [NASA Constellation Program documentation][ref_nasa_constellation], the [NASA Space Launch System program documentation][ref_nasa_sls_program], the [NASA Authorization Act of 2010][ref_nasa_auth_2010], the [NASA Office of Inspector General 2022 Artemis management evaluation][ref_nasa_oig_artemis_2022], and the [Congressional Research Service 2022 Artemis Program report][ref_crs_artemis_2022].

The comparison is stated compactly through the instrument parameter vector the COTS section introduces, evaluated for the two classes

$$\left( b, \; \alpha, \; \Delta e, \; S \right)^{\text{agreement}} = (1, \alpha, 0, 0) \qquad \text{against} \qquad \left( b, \; \alpha, \; \Delta e, \; S \right)^{\text{cost-plus}} \approx (0, 0, 0, S > 0)$$

with the two classes differing on three of the four parameters. The comparison admits statement along three dimensions. The cost incidence differs, with the overrun borne publicly under the cost-plus instrument and privately under the fixed-price instrument. The asset disposition differs, with the cost-plus instrument producing a vehicle the agency directs and the agreement producing a capability in the market. The termination cost differs, with the cost-plus programme carrying a constituency and a settlement exposure that the agreement does not.

The comparison is nonetheless confounded in a way the advocacy literature generally omits. The two instruments were applied to different requirements. The cost-plus programmes pursued a crewed beyond-low-Earth-orbit capability with no commercial market, and the fixed-price instruments pursued a low-Earth-orbit logistics capability with a plausible commercial market. The confound admits the compact statement that the observed comparison estimates

$$\left[ \text{outcome}^{\text{agreement}} - \text{outcome}^{\text{cost-plus}} \right] = \underbrace{\Delta^{\text{instrument}}}_{\text{sought}} + \underbrace{\Delta^{\text{requirement}}}_{\text{confound}}$$

with the second term unidentified. The mechanism-design result that the optimal incentive power falls with the uncertainty and rises with the specifiability implies that the instrument choice may have been appropriate in both cases. The article records the confound rather than reporting the comparison as a clean demonstration.

The cost comparison the agency itself published estimated that a traditional cost-plus development of the launch vehicle would have cost several times the amount actually expended. The estimate is a model output produced using a parametric cost model calibrated on historical programmes, and it is treated in this article as a contested reconstruction rather than as a measurement. The estimate's construction may be stated compactly

$$\hat{C}^{\text{counterfactual}} = f\!\left( \text{mass}, \; \text{complexity}, \; \text{heritage}; \; \hat{\beta}^{\text{historical}} \right)$$

with the parameters calibrated on a historical programme set drawn substantially from the cost-plus regime whose costs the estimate is being used to criticize. The circularity is not fatal and is not nothing. The direction of the estimate is consistent with the broader procurement literature and the magnitude is not independently verifiable.

## Deep Historical Comparative Precedents

The government-anchor capital-formation mechanic invites comparison with deep historical precedents in which a state supplied development capital to a private party on terms other than ownership.

The armory and interchangeable-parts precedent that the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats supplies the earliest systematic American instance. The War Department advanced funds against delivery schedules to private contractors including the Whitney and Colt enterprises, and the advances functioned as working capital that the contemporary capital markets would not have supplied. The [Hounshell 1984][book_hounshell_1984] From the American System to Mass Production and [Hosley 1996][book_hosley_1996] Colt treatments document the arrangements. The advance admits the compact characterization as a negative working-capital position supplied by the customer

$$\text{WC}^{\text{contractor}} = \text{receivables} + \text{inventory} - \text{advances} < 0$$

with the customer financing the production cycle. The structure is the oldest form the government-anchor capital-formation leg takes and it remains the most common.

The air-mail contracts of the 1920s and 1930s supply the closest transportation-sector analogue. The Post Office Department contracts supplied a revenue floor against which private capital could be raised, and the subsequent commercial passenger business was built on the capability the mail contracts sustained. The [Serling 1992][book_serling_1992] Legend and Legacy, [Bilstein 2001][book_bilstein_2001] Flight in America, and [Crouch 2003][book_crouch_2003] Wings treatments document the trajectory. The structural difference from the COTS case is that the mail contracts supplied revenue against a delivered service from the outset rather than capital against development milestones, which places them nearer the CRS stage than the COTS stage.

The wartime production financing of the 1940s supplies the largest historical instance of public capital supplied to private producers without equity. The arrangements comprised government-owned contractor-operated facilities, advance payments, and accelerated amortization, and they produced a private industrial capability at a public cost with a negotiated post-war disposition. The [Hounshell 1984][book_hounshell_1984], [Rhodes 1986][book_rhodes_1986] The Making of the Atomic Bomb, [Groves 1962][book_groves_1962] Now It Can Be Told, and [Hewlett and Anderson 1962][book_hewlett_anderson_1962] The New World treatments document portions of the arrangement. The arrangements admit compact classification by where the title rested

$$\left\{ \text{government-owned government-operated}, \; \text{government-owned contractor-operated}, \; \text{contractor-owned} \right\}$$

with the middle form dominating and with the post-war disposition of the government-owned assets constituting a distinct policy episode. The disposition question that the post-war period confronted is the same question the Space Act Agreement resolves in advance by conveying no asset.

The integrated-circuit procurement of the 1960s supplies the instance in which a government purchase at a price no commercial buyer would pay carried an industry through the interval before a commercial market existed. The [Berlin 2005][book_berlin_2005] The Man Behind the Microchip, [Malone 2014][book_malone_2014] The Intel Trinity, [Lecuyer 2006][book_lecuyer_2006] Making Silicon Valley, [Riordan Hoddeson and Kolb 2015][book_riordan_hoddeson_kolb_2015] Tunnel Visions, [Mindell 2008][book_mindell_2008] Digital Apollo, and the retrospectives in [Noyce 1976][research_noyce_1976] and [Kilby 1976][research_kilby_1976] document the trajectory, and the [Silicon Valley from Defense Contracting article A246][related_post_a246_silicon_valley_defense] treats the regional consequence. The case is a demand-side rather than a capital-side instance, which the article notes because the two are conflated as frequently in the historical literature as in the contemporary commentary.

The ARPANET and the DARPA institutional model supply the instance of a public funder operating through a programme-manager structure with an explicit selection discipline. The [Abbate 1999][book_abbate_1999] Inventing the Internet and [Norberg and O'Neill 1996][book_norberg_oneill_1996] Transforming Computer Technology treatments document the programme, [Bonvillian 2018][research_bonvillian_2018] documents the institutional model, and the [Heilmeier Catechism][ref_heilmeier_catechism] states the selection instrument. The model differs from the COTS instrument in that it funds specific research rather than capability demonstration and conveys no expectation of a follow-on procurement.

The X-33 and reusable-launch-vehicle programmes of the 1990s supply the negation case within the same agency and the same domain. The programme proceeded under a cooperative agreement with a cost share, pursued a technically ambitious single-vehicle demonstration, and was terminated in the 2001 period without producing a flying article. The record is accessible through the [NASA X-33 and reusable launch vehicle literature][ref_ntrs_x33] and the [NASA history archives][ref_nasa_history]. The case shares the cost-share structure with the COTS instrument and differs in that the milestone schedule was tied to a single integrated demonstration rather than to a sequence of independently valuable increments, which is the decomposability property the [Decomposability article A285][related_post_a285_spacex_decomposability] treats. The difference admits the compact statement through the milestone count

$$\left| \{ m_j \} \right|^{\text{X-33}} \approx 1 \qquad \text{against} \qquad \left| \{ m_j \} \right|^{\text{COTS}} \gg 1$$

with the single integrated demonstration supplying neither the payer's intermediate option to discontinue nor the provider's intermediate validation. The comparison establishes that the instrument alone is insufficient and that the milestone decomposition is doing substantial work.

The transcontinental-railroad land grants and the associated federal bond issues of the 1860s supply the instance in which a state supplied capital on terms that conveyed an asset rather than an equity claim, and in which the subsequent disposition of the asset became the dominant political question. The parallel to the Space Act Agreement's conveyance of no asset is instructive, because the agreement resolves in advance the question the land grants left open. The broader institutional treatments in [Chandler 1977][book_chandler_1977] The Visible Hand and [Fligstein 2001][book_fligstein_2001] The Architecture of Markets situate the arrangement within the development of the American corporate form.

The Apollo contractor set provides the instance in which a state programme funded a private industrial capability at a scale and under a cost-reimbursement instrument, producing a capability that substantially did not survive the programme. The treatments in [Bilstein 1996][book_bilstein_1996] Stages to Saturn, [Murray and Cox 1989][book_murray_cox_1989] Apollo, [Chaikin 2007][book_chaikin_2007] A Man on the Moon, [Kranz 2000][book_kranz_2000] Failure Is Not an Option, [Logsdon 1970][book_logsdon_1970] The Decision to Go to the Moon, [Logsdon 2010][book_logsdon_2010] John F Kennedy and the Race to the Moon, [Kraemer 2006][book_kraemer_2006] Rocketdyne, and [Mindell 2008][book_mindell_2008] Digital Apollo document the arrangement. The contrast with the COTS instrument is the clearest available within the same agency, because the two instruments funded comparable capability development sixty years apart and produced opposite dispositions of the resulting capability.

The Skunk Works and classified-programme arrangements documented in [Rich and Janos 1994][book_rich_janos_1994] Skunk Works and [Miller 1995][book_miller_1995] Lockheed Skunk Works supply the instance in which the reduced oversight the Space Act Agreement provides was obtained instead through classification. The comparison establishes that the oversight reduction is separable from the instrument and can be achieved by several institutional routes, each with different accountability consequences.

The European and Japanese launch programmes documented through the [Arianespace record][ref_arianespace], the [JAXA press releases][ref_jaxa_press], and the [Krige et al 2000][book_krige_et_al_2000] A History of the European Space Agency supply the comparative institutional arrangements, in which the public capital is supplied through national and consortium structures with equity or quasi-equity positions rather than through non-dilutive milestone payments. The comparison is the most direct available test of whether the non-dilutive property matters, and the European record of slower cost reduction is consistent with the proposition without establishing it.

## Historiographical Gap and Recent Scholarship

The scholarly literature on the COTS instrument is substantial in volume and unusual in character. Substantially the largest portion of it is advocacy, produced by participants or institutional beneficiaries and directed at extending the instrument to other domains. The evaluative literature is thinner and is concentrated in the oversight bodies rather than in the academic journals.

### Primary Source Documentation

The primary record comprises the statutory and regulatory materials at the [National Aeronautics and Space Act][ref_nasa_act_1958], the [Space Act Agreement authority][ref_51_usc_20113], the [NASA partnerships guidance][ref_nasa_partnerships], the [NASA Federal Acquisition Regulation Supplement][ref_nasa_far_supplement], the [Federal Acquisition Regulation Part 15][ref_far_part_15] and [Part 16][ref_far_part_16], the [Commercial Space Launch Act][ref_csla_1984] and its [2004 amendments][ref_csla_amendments_2004], and the [Commercial Space Launch Competitiveness Act of 2015][ref_uscsla_2015]. The programme record comprises the COTS, Commercial Crew, and Commercial Resupply materials identified above. The expenditure record is accessible through the [Federal Procurement Data System][ref_fpds] and the [USAspending][ref_usaspending] systems, and the budget-formulation framework through the [OMB circulars][ref_omb_circular_a11].

### Oversight and Programme-Evaluation Literature

The evaluative record is dominated by the oversight bodies. The principal documents comprise the [GAO 2009 COTS evaluation][ref_gao_cots_2009], the [GAO 2011 commercial cargo evaluation][ref_gao_cots_2011], the [NASA Office of Inspector General 2013 COTS evaluation][ref_nasa_oig_cots_2013], the [NASA Office of Inspector General 2018 commercial cargo evaluation][ref_nasa_oig_ccp_cargo_2018], the [GAO 2014][ref_gao_2014_commercial_crew], [2019][ref_gao_ccp_2019], and [2020][ref_gao_2020_commercial_crew] Commercial Crew evaluations, the [GAO 2023 National Security Space Launch evaluation][ref_gao_nssl_2023], and the Congressional Research Service reports at the [Commercial Crew report][ref_crs_commercial_crew], the [2018 Commercial Crew report][ref_crs_commercial_crew_2018], and the [2022 Artemis report][ref_crs_artemis_2022], with the broader collection at the [CRS reports database][ref_crs_reports] and the [Congressional record][ref_congressional_record] and [House Science Committee hearing record][ref_house_science_committee_hearings].

### Procurement-Economics Literature

The theoretical literature is surveyed in the Cross-Disciplinary Framings section. The principal works are [Laffont and Tirole 1993][book_laffont_tirole_1993], [McAfee and McMillan 1988][book_mcafee_mcmillan_1988], [Myerson 1981][research_myerson_1981], [Milgrom 2004][book_milgrom_2004], [Bajari and Tadelis 2001][research_bajari_tadelis_2001], [Bajari McMillan and Tadelis 2009][research_bajari_mcmillan_tadelis_2009], [Levin and Tadelis 2010][research_levin_tadelis_2010], [Corts and Singh 2004][research_corts_singh_2004], [Kalnins and Mayer 2004][research_kalnins_mayer_2004], [Che and Chung 1999][research_che_chung_1999], and [Gagnepain and Ivaldi 2002][research_gagnepain_ivaldi_2002]. The gap the literature exhibits with respect to the present case is that its empirical base is drawn overwhelmingly from construction and routine-services procurement, where the requirement is specifiable and the provider population is large. The applicability of the findings to a first-of-kind development with a provider population of two is not established.

### Public-Private-Partnership and Innovation-Policy Literature

The literature comprising [Grimsey and Lewis 2004][book_grimsey_lewis_2004], [Osborne 2000][book_osborne_2000], [Yescombe 2007][book_yescombe_2007], [Hodge and Greve 2007][research_hodge_greve_2007], [Bovaird 2004][research_bovaird_2004] supplies the comparative record for hybrid arrangements, and the innovation-policy literature comprising [Nelson 1959][research_nelson_1959], [Arrow 1962][research_arrow_1962], [Lerner 1996][research_lerner_1996_government_program], [Kortum and Lerner 2000][research_kortum_lerner_2000], [Hall and Lerner 2010][research_hall_lerner_2010], [Bonvillian 2018][research_bonvillian_2018], [Mazzucato 2013][book_mazzucato_2013], and [Mazzucato 2021][book_mazzucato_2021] supplies the rationale and evaluation apparatus. The finding the partnership literature reports, that outcomes are substantially more variable than the advocacy predicts, is the principal caution the article carries into its assessment.

### Small Business Innovation Research Literature

The SBIR literature gives the closest statutory analogue and is developed at length in the series that the [Introduction to the SBIR and STTR Programs article A132][related_post_a132_sbir_intro], the [Phase III and the Valley of Death article A138][related_post_a138_sbir_phase3], and the [Money Behind an SBIR or STTR Award article A140][related_post_a140_sbir_money] represent. The statutory and administrative materials are the [statute at 15 USC 638][ref_sbir_statute_15usc638], the [Small Business Administration policy directive][ref_sba_sbir_policy_directive], and the [programme portal][ref_sbir_gov].

### Agency-Side and Public-Administration Literature

The literature on the purchasing agency is substantial and is systematically underused in the procurement-economics treatments, which model the agency as a unitary rational actor. The principal works are [McCurdy 1994][book_mccurdy_1994] Inside NASA, [Handberg 1994][book_handberg_1994] Reinventing NASA, [Launius 1994][book_launius_1994], [Launius 2004][book_launius_2004] Frontiers of Space Exploration, [McDougall 1985][book_mcdougall_1985] The Heavens and the Earth, [Logsdon 1970][book_logsdon_1970], [Logsdon 2010][book_logsdon_2010], [Klerkx 2004][book_klerkx_2004] Lost in Space, [Selznick 1949][book_selznick_1949], and [Hargrove 1994][book_hargrove_1994] Prisoners of Myth. The organizational-culture strand in [Kunda 1992][book_kunda_1992] Engineering Culture and the professions strand in [Abbott 1988][book_abbott_1988] The System of Professions and [Larson 1977][book_larson_1977] The Rise of Professionalism supply the account of how a technical workforce inside an agency forms and defends a jurisdiction, which bears directly on the agency's willingness to cede a development to an outside provider.

### Institutional and Comparative-Political-Economy Literature

The comparative literature comprising [Johnson 1982][book_johnson_1982], [Amsden 1989][book_amsden_1989], [Wade 1990][book_wade_1990], [Evans 1995][book_evans_1995], [Woo-Cumings 1999][book_woo_cumings_1999], [Chang 2002][book_chang_2002], [Block 2008][research_block_2008], and [Weiss and Thurbon 2021][research_weiss_thurbon_2021] supplies the state-capacity apparatus, and the institutional-economics strand in [North 1990][book_north_1990], [Ostrom 1990][book_ostrom_1990], [Greif 2006][book_grief_2006], and [Acemoglu and Robinson 2012][book_acemoglu_robinson_2012] supplies the account of why a rule transplanted without its supporting institutions fails. The innovation-systems strand in [Freeman 1987][book_freeman_1987], [Lundvall 1992][book_lundvall_1992], [Nelson 1993][book_nelson_1993], [Mowery and Rosenberg 1998][book_mowery_rosenberg_1998], [Perez 2002][book_perez_2002] Technological Revolutions and Financial Capital, and [Schumpeter 1942][book_schumpeter_1942] Capitalism Socialism and Democracy supplies the macro framing.

### Systems-Engineering and Reliability Literature

The literature comprising [Blanchard and Fabrycky 2011][book_blanchard_fabrycky_2011], [Buede 2009][book_buede_2009], [Suh 2001][book_suh_2001], [Maier 1998][research_maier_1998], [Sage and Cuppan 2001][research_sage_cuppan_2001], the [INCOSE Systems Engineering Handbook][ref_incose_handbook], and the [NASA Systems Engineering Handbook][ref_nasa_se_handbook] supplies the milestone-decomposition apparatus. The reliability strand comprising [Perrow 1984][book_perrow_1984], [Vaughan 1996][book_vaughan_1996], [Weick and Sutcliffe 2007][book_weick_sutcliffe_2007], [O'Connor and Kleyner 2012][book_oconnor_kleyner_2012], [Musa 1998][book_musa_1998], and [Duane 1964][research_duane_1964], together with the [Rogers Commission report][ref_rogers_commission_1986] and the [Columbia Accident Investigation Board report][ref_caib_report_2003], supplies the institutional history from which the mission-assurance requirements derive.

### Methodological Literature

The case-study methodology literature comprising [Yin 2014][book_yin_2014] Case Study Research and Applications and [Creswell 2014][book_creswell_2014] Research Design supplies the inferential standards. The selection problem for this article is that the instrument's successes are documented in detail by participants and its failures are documented thinly, so that the readily available evidence is systematically favorable. The evolutionary and failure treatments in [Nelson and Winter 1982][book_nelson_winter_1982], [Metcalfe 1998][book_metcalfe_1998], [Ormerod 2005][book_ormerod_2005] Why Most Things Fail, [Kauffman 1993][book_kauffman_1993], and [Beinhocker 2006][book_beinhocker_2006] The Origin of Wealth supply the base-rate framing. The working-paper record through which the procurement-economics frontier circulates is accessible at the [National Bureau of Economic Research][ref_nber] and the [Social Science Research Network][ref_ssrn].

### Critical and Skeptical Literature

A critical literature reads the arrangement as a transfer to a concentrated private interest rather than as an efficient procurement innovation. The position draws on [Melman 1970][book_melman_1970] Pentagon Capitalism, [Fallows 1981][book_fallows_1981] National Defense, [Buchanan and Tullock 1962][book_buchanan_tullock_1962] The Calculus of Consent, [Stigler 1971][research_stigler_1971] The Theory of Economic Regulation, [Krueger 1974][research_krueger_1974] The Political Economy of the Rent-Seeking Society, and [Hunter 2016][book_hunter_2016] Creating Strategic Value. The concern that the instrument's reduced oversight is a feature for the provider and a defect for the public is well founded and the article does not resolve it. The concern that the resulting position is now substantially unchallengeable is treated in the Contemporary Comparative Landscape section.

### Trade Press and Journalistic Record

The programme record reaches the public substantially through [SpaceNews][ref_spacenews], [Ars Technica space coverage][ref_arstechnica_space], [NASASpaceflight][ref_nasaspaceflight], [Payload][ref_payload], [Payload Research][ref_payload_research], [The Space Review][ref_the_space_review], and [Space Policy Online][ref_space_policy_online], with the defense-adjacent coverage in [Breaking Defense][ref_breaking_defense], [Aviation Week][ref_aviation_week], and [Defense News][ref_defense_news], and the business coverage in [Bloomberg][ref_bloomberg], the [New York Times][ref_nyt], the [Wall Street Journal][ref_wsj], and the [Washington Post][ref_washington_post]. The peer-reviewed sector treatment appears in [Space Policy][ref_space_policy_journal], the [AIAA Journal of Spacecraft and Rockets][ref_aiaa_jsr], and the [Journal of Space Law][ref_journal_space_law], with the procurement-treatment in the [Journal of Public Procurement][ref_journal_public_procurement] and the [Public Administration Review][ref_public_admin_review].

## Contemporary Comparative Landscape

The contemporary landscape for the government-anchor capital-formation leg differs from the landscape for the forcing-function conditions, because the leg is available to any provider the agency selects and is therefore a policy variable rather than a firm attribute.

The instrument has been extended substantially since the COTS period. The Human Landing System awards that the [NASA Human Landing System program documentation][ref_nasa_hls_program], the [HLS solicitation][ref_nasa_hls_solicitation], the [Option A award][ref_nasa_hls_option_a_2021], the [Option B award][ref_nasa_hls_option_b_2022], and the [sustaining award][ref_nasa_hls_sustainable_2023] record employ a comparable milestone structure at a substantially larger scale, and the protest and litigation record at the [GAO 2021 protest decision][ref_gao_hls_bid_protest_2021] and the [United States Court of Federal Claims][ref_uscfc] record documents the contest the larger scale invited, and the evaluations at the [NASA Office of Inspector General 2021 HLS evaluation][ref_nasa_oig_hls_2021] and the [GAO 2022 HLS evaluation][ref_gao_hls_2022] apply the same analytical apparatus. The commercial low-Earth-orbit destinations programme and the commercial lunar payload arrangements extend it further. The broader agency posture appears in the [NASA commercial space documentation][ref_nasa_commercial_space].

Blue Origin has received awards under the extended instrument including the sustaining lunar-lander award and the National Security Space Launch Phase 3 allocation, and its position illustrates a structural point. The instrument offers capital to a provider that in that case did not require it, because the single-funder configuration the [Governance article A287][related_post_a287_spacex_governance] treats already supplied the development capital. The distinction admits the compact statement through the marginal effect of the award on the provider's capital constraint

$$\frac{\partial \, \text{capability}}{\partial K^{\text{gov}}} \approx 0 \quad \text{where the constraint does not bind} \qquad \text{against} \qquad \gg 0 \quad \text{where it does}$$

with the instrument performing its capital-formation function only for a provider whose capital constraint binds. The award therefore functions for that provider substantially as a validation and a revenue commitment rather than as a capital-formation channel. The record appears in the [Blue Origin press releases][ref_blue_origin_press].

Rocket Lab and the smaller entrant set receive awards under the instrument at a scale where the capital-formation function is substantially operative, which is the population for which the instrument was designed. The record appears in the [Rocket Lab press releases][ref_rocket_lab_press]. The United Launch Alliance operates substantially outside the development-capital channel and within the services channel, documented through the [United Launch Alliance news][ref_ula_press].

The broader defense-industrial context within which the instrument now operates is treated in [Hunter 2016][book_hunter_2016] Creating Strategic Value, [Hartley 2017][book_hartley_2017] The Economics of Arms, [Melman 1970][book_melman_1970] Pentagon Capitalism, and [Fallows 1981][book_fallows_1981] National Defense, and the incumbent portfolios against which the entrant competes are documented through the [Boeing press releases][ref_boeing_press], the [Boeing historical archives][ref_boeing_historical_archives], and the [Northrop Grumman press releases][ref_northrop_grumman_press]. The aerospace-industry comparative record in [Serling 1992][book_serling_1992] Legend and Legacy, [Newhouse 1982][book_newhouse_1982] The Sporty Game, [Newhouse 2007][book_newhouse_2007] Boeing versus Airbus, and [Lawrence 2016][book_lawrence_2016] Airbus versus Boeing supplies the longer arc within which the present contest sits.

The comparative-national picture is that other jurisdictions have adopted variants of the instrument. The European arrangements documented through the [Arianespace record][ref_arianespace], the Japanese arrangements through the [JAXA press releases][ref_jaxa_press], the Indian arrangements through the [ISRO press releases][ref_isro_press], and the Chinese arrangements through the [China National Space Administration][ref_chinese_space_program] and the [China sector reporting][ref_china_commercial_space] exhibit different balances between public ownership and private provision.

The concern the critical literature raises deserves statement in this section rather than only in the literature survey. The instrument that opened the market to a new entrant in the 2006 period now operates in a market where that entrant holds a dominant position, and an instrument that lowers the barrier to a challenger also lowers the barrier to an incumbent extending its position. The asymmetry is stated compactly as

$$\frac{\partial \, \text{share}}{\partial \, \text{instrument availability}} > 0 \quad \text{for the entrant at } t_0 \qquad \text{and} \qquad > 0 \quad \text{for the same firm as incumbent at } t_1$$

with the same policy producing the opposite competitive effect at the two dates. The policy question of whether the instrument should now be applied differently is outside the article's scope and is not outside the reader's legitimate interest.

## Comparative Cross-Sectional Analysis

The government-anchor capital-formation leg applies to the provider set as a cross-sectional scoring exercise across the five sub-properties the pattern-extraction section states. The closure vector takes the form

$$\boldsymbol{\phi}_j^{\text{gov-anchor}} \in \{0,1\}^{5}$$

with each provider's vector indicating the satisfaction status across the non-dilutive-terms, development-stage-timing, milestone-decomposition, private-cost-share, and follow-on-position sub-properties.

SpaceX exhibits closure on all five. Blue Origin exhibits closure on the non-dilutive-terms and follow-on-position sub-properties and non-closure on the development-stage-timing sub-property, because the awards arrived after the capability was substantially funded. Rocketplane Kistler exhibited closure on the non-dilutive-terms, timing, and milestone-decomposition sub-properties and non-closure on the private-cost-share sub-property, which is what terminated it. The X-33 programme exhibited non-closure on the milestone-decomposition sub-property. The cost-plus programmes exhibit non-closure on substantially all five.

The cross-sectional pattern indicates that the milestone-decomposition and the private-cost-share sub-properties are the two on which the negation cases fail, and that neither is a property of the funding magnitude. The finding admits the compact statement

$$P\!\left( \text{success} \mid K^{\text{gov}} \right) \approx P\!\left( \text{success} \right) \qquad \text{while} \qquad P\!\left( \text{success} \mid \text{decomposed milestones} \wedge \text{cost share} \right) \gg P\!\left( \text{success} \right)$$

with the structure of the instrument carrying substantially more information than the amount disbursed. The finding is the most directly actionable conclusion in the article, and it is the conclusion the COTS advocacy literature least frequently states, because the advocacy is generally directed at securing the appropriation rather than at specifying the instrument.

## Data Sources and Reconstruction Methodology

The article draws on primary and secondary sources, and its evidentiary position is the strongest of any article in the series.

The primary-source layer comprises the statutory, regulatory, programme, and oversight materials identified in the Historiographical Gap section. The award amounts, the milestone structures, the termination actions, and the competitive outcomes are directly documented by the government party. The asymmetry with the preceding articles is substantial and arises from a structural fact rather than from a research effort, namely that the government party to each transaction is subject to disclosure obligations the private party is not.

The secondary-source layer comprises the trade-press and evaluative literature identified above.

The reconstruction methodology proceeds by taking the documented award and milestone record as the spine and using the secondary sources only for the private-side quantities the public record does not contain. The supporting technical and programme literature is accessible through the [NASA Technical Reports Server][ref_nasa_ntrs], and the provider's own announcements through the [SpaceX news archive][ref_spacex_news_archive] and the [SpaceX corporate site][ref_spacex_company].

The empirical-record limitations are correspondingly narrower than elsewhere in the series and comprise the following. The provider's actual development costs are not public, so the relation between the milestone payments and the costs they defrayed is unknown. The private cost-share amounts are reported in aggregate rather than in detail. The classified portions of the defense relationship are not documented. The counterfactual cost estimates the agency published are model outputs whose calibration is not independently verifiable. The consequence is that the article can state with confidence what the government supplied and cannot state with confidence what it bought.

## Alternative Analytical Frameworks

The government-anchor capital-formation framing the article develops is one of several analytical frameworks the surrounding literature applies.

The rent-seeking framing developed in [Buchanan and Tullock 1962][book_buchanan_tullock_1962], [Stigler 1971][research_stigler_1971], and [Krueger 1974][research_krueger_1974] treats the arrangement as a transfer obtained through political action rather than as an efficient instrument. The framing draws support from the litigation and advocacy the entry section documents, and it generates the prediction that the returns should correlate with the political access rather than with the technical performance. The prediction is checkable in principle against the commercial revenue share that the [Value Capture article A284][related_post_a284_spacex_value_capture] documents, The rent the framing posits can be written as

$$\text{Rent} = \pi^{\text{observed}} - \pi^{\text{competitive benchmark}} \qquad \text{with} \qquad \frac{\partial \text{Rent}}{\partial \, \text{political effort}} > 0$$

under the framing's prediction. The evidence runs against the strong form while supporting the weaker claim that the early-period access mattered.

The capture framing developed in [Stigler 1971][research_stigler_1971] and the regulated-industry treatments in [Kahn 1988][book_kahn_1988] and [Sharkey 1982][book_sharkey_1982] treats the agency as having been captured by the provider it created. The framing generates the prediction that the subsequent instrument design should favor the incumbent, admitting the compact form

$$\frac{\partial \, \text{eligibility threshold}}{\partial \, \text{incumbent preference}} > 0$$

with the agency progressively narrowing the admissible provider set. The two-lane Phase 3 structure and the dual-provider lunar-lander arrangement are evidence against the prediction rather than for it.

The developmental-state framing developed in [Johnson 1982][book_johnson_1982], [Amsden 1989][book_amsden_1989], [Wade 1990][book_wade_1990], [Evans 1995][book_evans_1995], [Block 2008][research_block_2008], and [Weiss and Thurbon 2021][research_weiss_thurbon_2021] treats the arrangement as an instance of a hidden industrial policy operating through procurement. The state capacity the framing treats as decisive has the form

$$\Sigma^{\text{state}} = f\!\left( \text{technical competence}, \; \text{insulation from capture}, \; \text{embeddedness in the sector} \right)$$

with the third element requiring enough proximity to the industry to select well and the second requiring enough distance not to be captured while doing so. The framing yields the most useful comparative frame and the most direct challenge to the self-description of the participants, who generally present the arrangement as a market mechanism rather than as an industrial policy.

The transaction-cost framing developed in [Williamson 1985][book_williamson_1985] and [Bajari and Tadelis 2001][research_bajari_tadelis_2001] treats the instrument choice as an efficient response to the contracting hazards the requirement presented, and it predicts that the instrument should have been chosen wherever the requirement was ill specified and the asset specificity low. The selection rule may be written

$$\text{agreement} \iff \left[ h < \bar{h} \right] \wedge \left[ \text{requirement ill specified} \right] \wedge \left[ \text{provider can bear } \Delta C \right]$$

with the conjunction required. The framing contributes the most complete positive account of why the instrument was appropriate here and why it would not be appropriate for a requirement with a higher asset specificity.

The real-options framing developed in [Dixit and Pindyck 1994][book_dixit_pindyck_1994] and [Trigeorgis 1996][book_trigeorgis_1996] treats the milestone structure as an option strip held by the agency. The valuation admits the compact form

$$V^{\text{agency}} = \sum_j \pi_j \cdot \max\left\{ B_j - m_j, \; 0 \right\}$$

with the agency discontinuing at the first milestone where the expected benefit falls below the payment, which is the formal account of the termination behavior the Rocketplane Kistler case exhibits.

The public-choice and budgetary framing treats the instrument as attractive to the agency principally because it produces a visible result within an appropriation cycle, and it predicts that the instrument will be selected for its budgetary properties irrespective of its efficiency properties. The budgetary preference takes the form

$$U^{\text{agency}} = w^{\text{outcome}} \cdot V^{\text{programme}} + w^{\text{visibility}} \cdot V^{\text{result within appropriation cycle}}$$

with the second term entering the agency's objective and not the social objective. The framing gives the explanation for the instrument's rapid extension to programmes whose characteristics differ substantially from those the original application suited.

The evolutionary framing developed in [Nelson and Winter 1982][book_nelson_winter_1982] and [Metcalfe 1998][book_metcalfe_1998] supplies the caution that the single observed success is a poor basis for the policy generalization the advocacy literature draws, and that the relevant population includes the programmes that received the same instrument and failed. The behavioral framing developed in [Kahneman and Tversky 1979][research_kahneman_tversky_1979], [Tversky and Kahneman 1992][research_tversky_kahneman_1992], [Kahneman 2011][book_kahneman_2011] Thinking Fast and Slow, [Simon 1957][book_simon_1957] Administrative Behavior, [Staw 1976][research_staw_1976], [Ross and Staw 1993][research_ross_staw_1993], and [Weick 1979][book_weick_1979] The Social Psychology of Organizing treats the agency's termination decision as a judgment subject to the escalation hazard, and it predicts that the programmes hardest to terminate are those in which the deciding officials made the original selection. The framing provides the behavioral complement to the public-choice account of the same failure.

The state-capacity framing developed in [Evans 1995][book_evans_1995], [Johnson 1982][book_johnson_1982], [Amsden 1989][book_amsden_1989], [Wade 1990][book_wade_1990], and [Woo-Cumings 1999][book_woo_cumings_1999] treats the outcome as attributable to the agency's evaluative capability rather than to the instrument, and it generates the prediction that the same instrument applied by a less capable agency produces worse outcomes. The prediction is the most policy-relevant claim in the article and is the one the single case cannot test.

The institutional-transplant framing developed in [North 1990][book_north_1990], [Greif 2006][book_grief_2006], and [Acemoglu and Robinson 2012][book_acemoglu_robinson_2012] treats the instrument as a rule whose effects depend on the surrounding institutional configuration, and it offers the formal reason the advocacy for extending the instrument to other jurisdictions should be discounted.

The systems-architecture framing developed in [Simon 1962][research_simon_1962] The Architecture of Complexity, [Maier 1998][research_maier_1998], and [Suh 2001][book_suh_2001] treats the milestone decomposition rather than the payment structure as the operative variable, and it is the framing under which the X-33 comparison carries the most weight.

The correction can be stated as

$$\hat{P}\!\left( \text{success} \mid \text{instrument} \right) = \frac{n^{\text{success}}}{n^{\text{success}} + n^{\text{failure}}}$$

with the denominator understated whenever the evaluation counts only the programmes that completed.

## Pattern Extraction

The government-anchor capital-formation pattern that the SpaceX case exhibits admits the following abstract statement without naming any downstream application. A mission-directed technology venture achieves the government-anchor capital-formation closure when a state customer yields development capital against demonstrated technical milestones, on terms that convey no claim on the venture's residual or its control, at the stage when private capital would be most expensive, and in a structure that establishes a position from which follow-on revenue can be earned.

The abstract mechanic requires joint satisfaction of five sub-properties, admitting the compact conjunctive form

$$\Phi^{\text{gov-anchor}} = \prod_{k=1}^{5} \phi_k, \qquad \phi_k \in \{0,1\}$$

First, the capital must be non-dilutive, conveying no equity and no governance rights. Capital that conveys either is private capital wearing a public label.

Second, the capital must arrive at the development stage rather than at the operational stage, satisfying

$$t^{\text{award}} < t^{\text{capability}}$$

Capital arriving after the capability exists is revenue, and it performs a different function.

Third, the milestone schedule must decompose the development into increments that are independently verifiable. A milestone schedule tied to a single integrated demonstration contributes neither the payer's option to discontinue nor the provider's intermediate validation, which is the failure the X-33 comparison isolates.

Fourth, the arrangement must require a private cost share, which uses the private capital market as an external validator and makes the two channels complements rather than substitutes.

Fifth, the arrangement must establish a follow-on position. The capital is the mechanism and the position is the transfer. A venture that receives the development capital and does not thereby become the natural provider of the follow-on service has received a subsidy rather than a capital-formation leg.

The mechanic admits a diagnostic procedure stated as an ordered test vector

$$\tau = \left( \Delta e = \Delta v = 0, \;\; t^{\text{award}} < t^{\text{capability}}, \;\; \left| \{ m_j \} \right| \gg 1, \;\; K^{\text{private}} \geq \alpha K^{\text{gov}}, \;\; \exists \text{ follow-on position} \right)$$

with the third and fifth components the ones a candidate case most often fails.

The mechanic carries costs the statement should not conceal. The reduced oversight that makes the instrument accessible to a venture-stage provider is the same reduced oversight that prevents the paying public from determining what it bought. The follow-on position the instrument creates is a position against which subsequent competition is structurally disadvantaged, so an instrument justified as opening a market predictably concentrates it. And the instrument's availability is a policy choice made by parties the venture does not control, which makes this leg the least reproducible of the three the series treats.

## Cross-References to the Series

The article back-references the [series opener][related_post_a281_spacex_framing] for the seven-plus-three framework and the pre-COTS prologue. The article back-references the [Value Gradient article A282][related_post_a282_spacex_value_gradient] for the vehicle progression the development capital funded. The article back-references the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] for the demand-side treatment from which this article's capital-side treatment is deliberately distinguished. The article back-references the [Value Capture article A284][related_post_a284_spacex_value_capture] for the commercial revenue against which the government share should be assessed. The article back-references the [Decomposability article A285][related_post_a285_spacex_decomposability] for the rung structure that the milestone decomposition mirrors. The article back-references the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] for the low asset specificity that prevented the holdup the transaction-cost framing would otherwise predict, and for the cost-plus negation cases. The article back-references the [Governance article A287][related_post_a287_spacex_governance] for the control condition that the avoided dilution preserved. The article back-references the [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] for the portfolio across which the capital was allocated.

The article forward-references the Patient-Private Capital-Formation Leg article A290, which treats the private channel that this article's cost-share requirement made complementary, and the Category-Dominating Commercial Spinoff article A291, which treats the third leg. The closing article A292 synthesizes across the framework.

The article cross-references the existing published corpus including the [Introduction to the SBIR and STTR Programs article A132][related_post_a132_sbir_intro], the [Phase III and the Valley of Death article A138][related_post_a138_sbir_phase3], the [Money Behind an SBIR or STTR Award article A140][related_post_a140_sbir_money], the [Patents Trade Secrets and the Disclosure Tradeoff article A164][related_post_a164_patents_trade_secrets], the [Introduction to Space Studies article A90][related_post_a90_intro_space_studies], the [History of Rocketplanes article A96][related_post_a96_history_rocketplanes], the [What Does the United States Space Force Do article A97][related_post_a97_us_space_force], the [Framing and the Co-Development Mechanism article A237][related_post_a237_aerospace_framing], the [Silicon Valley from Defense Contracting article A246][related_post_a246_silicon_valley_defense], the [Software-Defined Aerospace article A247][related_post_a247_software_defined_aerospace], and the [Contemporary Snapshot article A248][related_post_a248_contemporary_snapshot].

## Terminological Note

The article adopts terminology consistent with the federal procurement conventions and marks the places where the popular usage diverges. The term "Space Act Agreement" refers to an instrument entered under the agency's other-transaction authority, which is legally distinct from a contract and is not governed by the Federal Acquisition Regulation. The term "contract" is reserved for instruments governed by that regulation, so that the COTS instruments were agreements and the CRS and CCtCap instruments were contracts. The term "non-dilutive" refers to capital conveying no claim on the residual and no claim on control, and it does not imply the capital is costless. The term "incentive power" refers to the fraction of a marginal cost increase borne by the provider, taking the value unity under a pure fixed-price arrangement. The term "milestone payment" refers to a disbursement conditioned on a verified technical or financial event rather than on elapsed time or incurred cost. The term "capital-formation leg" refers to a channel through which the venture obtained the capital to build a capability, and is distinguished throughout from a demand channel through which it obtained revenue for delivering one.

## Load-Bearing Open Questions

The article closes with the load-bearing open questions the treatment leaves unresolved. First, the counterfactual in which the development capital was raised privately is not resolved, and the Rocketplane Kistler observation constrains it without settling it. Second, the provider's actual development costs are not public, so the relation between what the government paid and what the development cost is unknown, and every efficiency claim about the instrument depends on that unknown relation. Third, the agency's published counterfactual cost estimates are model outputs whose calibration cannot be independently checked, and they are the single most frequently cited quantity in the advocacy literature. Fourth, the mechanism-design result that optimal incentive power falls with uncertainty is in direct tension with the policy lesson usually drawn from this case, and the article records the tension without resolving it. Fifth, the comparison against the cost-plus programmes is confounded by the different requirements the two instrument classes addressed. Sixth, whether an instrument that opened the market to a challenger should continue to be applied unchanged now that the challenger holds a dominant position is a policy question the article raises and does not answer.

## References

### Books

- [Abbate 1999 Inventing the Internet][book_abbate_1999]
- [Abbott 1988 The System of Professions][book_abbott_1988]
- [Acemoglu and Robinson 2012 Why Nations Fail][book_acemoglu_robinson_2012]
- [Amsden 1989 Asia's Next Giant][book_amsden_1989]
- [Argote 1999 Organizational Learning][book_argote_1999]
- [Argyris and Schon 1978 Organizational Learning][book_argyris_schon_1978]
- [Bain 1968 Industrial Organization][book_bain_1968]
- [Beinhocker 2006 The Origin of Wealth][book_beinhocker_2006]
- [Berger 2021 Liftoff][book_berger_2021]
- [Berger 2024 Reentry][book_berger_2024]
- [Berlin 2005 The Man Behind the Microchip][book_berlin_2005]
- [Bilstein 1996 Stages to Saturn][book_bilstein_1996]
- [Bilstein 2001 Flight in America][book_bilstein_2001]
- [Blanchard and Fabrycky 2011 Systems Engineering and Analysis][book_blanchard_fabrycky_2011]
- [Bork 1978 The Antitrust Paradox][book_bork_1978]
- [Buchanan and Tullock 1962 The Calculus of Consent][book_buchanan_tullock_1962]
- [Buede 2009 The Engineering Design of Systems Models and Methods][book_buede_2009]
- [Chaikin 2007 A Man on the Moon][book_chaikin_2007]
- [Chandler 1962 Strategy and Structure][book_chandler_1962]
- [Chandler 1977 The Visible Hand][book_chandler_1977]
- [Chandler 1990 Scale and Scope][book_chandler_1990]
- [Chang 2002 Kicking Away the Ladder][book_chang_2002]
- [Creswell 2014 Research Design][book_creswell_2014]
- [Crouch 2003 Wings A History of Aviation from Kites to the Space Age][book_crouch_2003]
- [Cyert and March 1963 A Behavioral Theory of the Firm][book_cyert_march_1963]
- [Davenport 2018 The Space Barons][book_davenport_2018]
- [Dixit and Pindyck 1994 Investment Under Uncertainty][book_dixit_pindyck_1994]
- [Evans 1995 Embedded Autonomy][book_evans_1995]
- [Fallows 1981 National Defense][book_fallows_1981]
- [Fernholz 2018 Rocket Billionaires][book_fernholz_2018]
- [Fligstein 2001 The Architecture of Markets][book_fligstein_2001]
- [Freeman 1987 Technology Policy and Economic Performance][book_freeman_1987]
- [Gompers and Lerner 2001 The Money of Invention][book_gompers_lerner_2001]
- [Greif 2006 Institutions and the Path to the Modern Economy][book_grief_2006]
- [Grimsey and Lewis 2004 Public Private Partnerships][book_grimsey_lewis_2004]
- [Groves 1962 Now It Can Be Told][book_groves_1962]
- [Handberg 1994 Reinventing NASA][book_handberg_1994]
- [Hargrove 1994 Prisoners of Myth][book_hargrove_1994]
- [Hartley 2017 The Economics of Arms][book_hartley_2017]
- [Hewlett and Anderson 1962 The New World][book_hewlett_anderson_1962]
- [Hosley 1996 Colt The Making of an American Legend][book_hosley_1996]
- [Hounshell 1984 From the American System to Mass Production][book_hounshell_1984]
- [Hovenkamp 2005 The Antitrust Enterprise][book_hovenkamp_2005]
- [Hughes 1983 Networks of Power][book_hughes_1983]
- [Hunter 2016 Creating Strategic Value][book_hunter_2016]
- [Johnson 1982 MITI and the Japanese Miracle][book_johnson_1982]
- [Kahn 1988 The Economics of Regulation][book_kahn_1988]
- [Kahneman 2011 Thinking Fast and Slow][book_kahneman_2011]
- [Kaplan 1991 The Wizards of Armageddon][book_kaplan_1991]
- [Kauffman 1993 The Origins of Order][book_kauffman_1993]
- [Klerkx 2004 Lost in Space][book_klerkx_2004]
- [Kraemer 2006 Rocketdyne Powering Humans into Space][book_kraemer_2006]
- [Kranz 2000 Failure Is Not an Option][book_kranz_2000]
- [Krige et al 2000 A History of the European Space Agency][book_krige_et_al_2000]
- [Kunda 1992 Engineering Culture][book_kunda_1992]
- [Laffont and Tirole 1993 A Theory of Incentives in Procurement and Regulation][book_laffont_tirole_1993]
- [Landes 1969 The Unbound Prometheus][book_landes_1969]
- [Larson 1977 The Rise of Professionalism][book_larson_1977]
- [Launius 1994 NASA A History of the United States Civil Space Program][book_launius_1994]
- [Launius 2004 Frontiers of Space Exploration][book_launius_2004]
- [Lawrence 2016 Airbus versus Boeing][book_lawrence_2016]
- [Lecuyer 2006 Making Silicon Valley][book_lecuyer_2006]
- [Lerner 2009 Boulevard of Broken Dreams][book_lerner_2009]
- [Logsdon 1970 The Decision to Go to the Moon][book_logsdon_1970]
- [Logsdon 2010 John F Kennedy and the Race to the Moon][book_logsdon_2010]
- [Lundvall 1992 National Systems of Innovation][book_lundvall_1992]
- [Malone 2014 The Intel Trinity][book_malone_2014]
- [March and Simon 1958 Organizations][book_march_simon_1958]
- [Mazzucato 2013 The Entrepreneurial State][book_mazzucato_2013]
- [Mazzucato 2021 Mission Economy][book_mazzucato_2021]
- [McAfee and McMillan 1988 Incentives in Government Contracting][book_mcafee_mcmillan_1988]
- [McCurdy 1994 Inside NASA][book_mccurdy_1994]
- [McDougall 1985 The Heavens and the Earth][book_mcdougall_1985]
- [Melman 1970 Pentagon Capitalism][book_melman_1970]
- [Metcalfe 1998 Evolutionary Economics and Creative Destruction][book_metcalfe_1998]
- [Metrick and Yasuda 2011 Venture Capital and the Finance of Innovation][book_metrick_yasuda_2011]
- [Milgrom 2004 Putting Auction Theory to Work][book_milgrom_2004]
- [Miller 1995 Lockheed Skunk Works The First Fifty Years][book_miller_1995]
- [Mindell 2008 Digital Apollo][book_mindell_2008]
- [Mowery and Rosenberg 1998 Paths of Innovation][book_mowery_rosenberg_1998]
- [Murray and Cox 1989 Apollo][book_murray_cox_1989]
- [Musa 1998 Software Reliability Engineering][book_musa_1998]
- [Nelson 1993 National Innovation Systems][book_nelson_1993]
- [Nelson and Winter 1982 An Evolutionary Theory of Economic Change][book_nelson_winter_1982]
- [Newhouse 1982 The Sporty Game][book_newhouse_1982]
- [Newhouse 2007 Boeing versus Airbus][book_newhouse_2007]
- [Nonaka and Takeuchi 1995 The Knowledge-Creating Company][book_nonaka_takeuchi_1995]
- [Norberg and O'Neill 1996 Transforming Computer Technology][book_norberg_oneill_1996]
- [North 1990 Institutions Institutional Change and Economic Performance][book_north_1990]
- [O'Connor and Kleyner 2012 Practical Reliability Engineering][book_oconnor_kleyner_2012]
- [Ormerod 2005 Why Most Things Fail][book_ormerod_2005]
- [Osborne 2000 Public-Private Partnerships][book_osborne_2000]
- [Ostrom 1990 Governing the Commons][book_ostrom_1990]
- [Perez 2002 Technological Revolutions and Financial Capital][book_perez_2002]
- [Perrow 1984 Normal Accidents][book_perrow_1984]
- [Porter 1980 Competitive Strategy][book_porter_1980]
- [Porter 1985 Competitive Advantage][book_porter_1985]
- [Posner 2001 Antitrust Law][book_posner_2001]
- [Rhodes 1986 The Making of the Atomic Bomb][book_rhodes_1986]
- [Rich and Janos 1994 Skunk Works][book_rich_janos_1994]
- [Riordan Hoddeson and Kolb 2015 Tunnel Visions][book_riordan_hoddeson_kolb_2015]
- [Rosenberg 1976 Perspectives on Technology][book_rosenberg_1976]
- [Rosenberg 1982 Inside the Black Box][book_rosenberg_1982]
- [Ruttan 2006 Is War Necessary for Economic Growth][book_ruttan_2006]
- [Scherer and Ross 1990 Industrial Market Structure and Economic Performance][book_scherer_ross_1990]
- [Schumpeter 1942 Capitalism Socialism and Democracy][book_schumpeter_1942]
- [Selznick 1949 TVA and the Grass Roots][book_selznick_1949]
- [Senge 1990 The Fifth Discipline][book_senge_1990]
- [Serling 1992 Legend and Legacy][book_serling_1992]
- [Sharkey 1982 The Theory of Natural Monopoly][book_sharkey_1982]
- [Simon 1957 Administrative Behavior][book_simon_1957]
- [Suh 2001 Axiomatic Design Advances and Applications][book_suh_2001]
- [Tirole 1988 The Theory of Industrial Organization][book_tirole_1988]
- [Trigeorgis 1996 Real Options][book_trigeorgis_1996]
- [Vaughan 1996 The Challenger Launch Decision][book_vaughan_1996]
- [Wade 1990 Governing the Market][book_wade_1990]
- [Weick 1979 The Social Psychology of Organizing][book_weick_1979]
- [Weick and Sutcliffe 2007 Managing the Unexpected][book_weick_sutcliffe_2007]
- [Weiss 2014 America Inc][book_weiss_2014]
- [Williamson 1985 The Economic Institutions of Capitalism][book_williamson_1985]
- [Woo-Cumings 1999 The Developmental State][book_woo_cumings_1999]
- [Yescombe 2007 Public-Private Partnerships Principles of Policy and Finance][book_yescombe_2007]
- [Yin 2014 Case Study Research and Applications][book_yin_2014]

### Reference

- [AIAA Journal of Spacecraft and Rockets][ref_aiaa_jsr]
- [Arianespace][ref_arianespace]
- [Ars Technica Space Coverage][ref_arstechnica_space]
- [Aviation Week][ref_aviation_week]
- [Bloomberg][ref_bloomberg]
- [Blue Origin Press Releases][ref_blue_origin_press]
- [Boeing Historical Archives][ref_boeing_historical_archives]
- [Boeing Press Releases][ref_boeing_press]
- [Boeing Starliner Programme Record][ref_boeing_starliner_cft_2024]
- [Breaking Defense][ref_breaking_defense]
- [China Commercial Space Sector Coverage][ref_china_commercial_space]
- [China National Space Administration][ref_chinese_space_program]
- [Columbia Accident Investigation Board Report 2003][ref_caib_report_2003]
- [Commercial Space Authority 51 USC 51302][ref_51_usc_51302_saa]
- [Commercial Space Launch Act][ref_csla_1984]
- [Commercial Space Launch Amendments Act of 2004][ref_csla_amendments_2004]
- [Congressional Record][ref_congressional_record]
- [Congressional Research Service Commercial Crew Report][ref_crs_commercial_crew]
- [Congressional Research Service Reports Database][ref_crs_reports]
- [CRS 2018 Commercial Crew Programme Report][ref_crs_commercial_crew_2018]
- [CRS 2022 Artemis Program Report][ref_crs_artemis_2022]
- [DARPA Heilmeier Catechism][ref_heilmeier_catechism]
- [Defense News][ref_defense_news]
- [Department of Defense Contract Announcements][ref_dod_contracts]
- [Department of Defense Other Transactions Resources][ref_dod_other_transactions]
- [DOD Other Transaction Authority 10 USC 2371b][ref_10_usc_2371b]
- [FAA 14 CFR Part 450 Launch and Reentry Licensing Requirements][ref_faa_ast_licensing_regs_450]
- [FAA Commercial Space Transportation Regulations 14 CFR Chapter III][ref_faa_ast_regulations]
- [FAA Current Launch Licenses][ref_faa_launch_licenses_current]
- [Federal Acquisition Regulation Part 12 Acquisition of Commercial Products][ref_far_part_12]
- [Federal Acquisition Regulation Part 15 Contracting by Negotiation][ref_far_part_15]
- [Federal Acquisition Regulation Part 16 Types of Contracts][ref_far_part_16]
- [Federal Acquisition Regulation Part 35 Research and Development Contracting][ref_far_part_35]
- [Federal Procurement Data System][ref_fpds]
- [GAO 2009 COTS Programme Evaluation][ref_gao_cots_2009]
- [GAO 2011 Commercial Cargo Programme Evaluation][ref_gao_cots_2011]
- [GAO 2014 Commercial Crew Programme Evaluation][ref_gao_2014_commercial_crew]
- [GAO 2019 Commercial Crew Program Evaluation][ref_gao_ccp_2019]
- [GAO 2020 Commercial Crew Programme Evaluation][ref_gao_2020_commercial_crew]
- [GAO 2021 Human Landing System Protest Decision][ref_gao_hls_bid_protest_2021]
- [GAO 2022 Human Landing System Evaluation][ref_gao_hls_2022]
- [GAO 2023 National Security Space Launch Evaluation][ref_gao_nssl_2023]
- [GAO Bid Protest Function][ref_gao_bid_protest]
- [GAO Reports and Testimonies Database][ref_gao_reports]
- [House Science Space and Technology Committee Hearing Record][ref_house_science_committee_hearings]
- [INCOSE Systems Engineering Handbook][ref_incose_handbook]
- [ISRO Press Releases][ref_isro_press]
- [ITAR 22 CFR 120 through 130][ref_itar_22_cfr_120_130]
- [JAXA Press Releases][ref_jaxa_press]
- [Journal of Public Procurement][ref_journal_public_procurement]
- [Journal of Space Law][ref_journal_space_law]
- [Kennedy Space Center Launch Complex 39A Arrangement][ref_ksc_lc39a_lease]
- [Kwajalein Atoll Range Documentation][ref_kwajalein_atoll_documentation]
- [NASA Authorization Act of 2010][ref_nasa_auth_2010]
- [NASA Commercial Crew Certification Record][ref_nasa_ccp_certification]
- [NASA Commercial Crew Program Documentation][ref_nasa_ccp_documents]
- [NASA Commercial Resupply Services Programme Overview][ref_nasa_crs_program_overview]
- [NASA Commercial Space Documentation][ref_nasa_commercial_space]
- [NASA Commercial Space Documentation][ref_nasa_cots_solicitation_2006]
- [NASA Constellation Program Documentation][ref_nasa_constellation]
- [NASA COTS Programme History 2011][ref_nasa_cots_2011]
- [NASA COTS Programme Literature][ref_nasa_cots_report]
- [NASA CRS-2 Award Announcement January 2016][ref_nasa_crs2_press_2016]
- [NASA FAR Supplement][ref_nasa_far_supplement]
- [NASA History Archives][ref_nasa_history]
- [NASA HLS Option A Award April 16 2021][ref_nasa_hls_option_a_2021]
- [NASA HLS Option B Award November 15 2022][ref_nasa_hls_option_b_2022]
- [NASA HLS Sustaining Lander Award 2023][ref_nasa_hls_sustainable_2023]
- [NASA Human Landing System Program Documentation][ref_nasa_hls_program]
- [NASA Human Landing System Solicitation][ref_nasa_hls_solicitation]
- [NASA News Releases][ref_nasa_news]
- [NASA NPR 7120.5 Programme and Project Management Requirements][ref_nasa_npr_7120_5f]
- [NASA Office of Inspector General 2013 COTS Evaluation][ref_nasa_oig_cots_2013]
- [NASA Office of Inspector General 2018 Commercial Cargo Evaluation][ref_nasa_oig_ccp_cargo_2018]
- [NASA Office of Inspector General 2021 Human Landing System Evaluation][ref_nasa_oig_hls_2021]
- [NASA Office of Inspector General 2022 Artemis Management Evaluation][ref_nasa_oig_artemis_2022]
- [NASA Office of Inspector General Reports Database][ref_nasa_oig_reports]
- [NASA Partnerships and Space Act Agreements][ref_nasa_partnerships]
- [NASA Space Launch System Program Documentation][ref_nasa_sls_program]
- [NASA Systems Engineering Handbook][ref_nasa_se_handbook]
- [NASA Technical Reports Server][ref_nasa_ntrs]
- [NASA Technical Standards System][ref_nasa_std_8709_22]
- [NASA X-33 and Reusable Launch Vehicle Literature][ref_ntrs_x33]
- [NASASpaceflight][ref_nasaspaceflight]
- [National Aeronautics and Space Act of 1958][ref_nasa_act_1958]
- [National Bureau of Economic Research][ref_nber]
- [New York Times 2024 Starshield Coverage][ref_nyt_starshield_2024]
- [New York Times Space Coverage][ref_nyt]
- [Northrop Grumman Press Releases][ref_northrop_grumman_press]
- [OMB Circulars][ref_omb_circular_a11]
- [Payload][ref_payload]
- [Payload Research][ref_payload_research]
- [Public Administration Review][ref_public_admin_review]
- [Rocket Lab Press Releases][ref_rocket_lab_press]
- [Rogers Commission Report 1986][ref_rogers_commission_1986]
- [SBIR and STTR Programme Portal][ref_sbir_gov]
- [SBIR and STTR Statutory Authority 15 USC 638][ref_sbir_statute_15usc638]
- [SEC EDGAR Company Search][ref_sec_edgar]
- [Small Business Administration SBIR Policy Directive][ref_sba_sbir_policy_directive]
- [Social Science Research Network][ref_ssrn]
- [Space Act Agreement Authority 51 USC 20113][ref_51_usc_20113]
- [Space Force National Security Space Launch][ref_space_force_nssl]
- [Space Force News][ref_space_force_news]
- [Space Force NSSL Phase 1A Award 2018][ref_space_force_nssl_phase1a_2018]
- [Space Force NSSL Phase 2 Award 2020][ref_space_force_nssl_phase2_2020]
- [Space Policy Journal][ref_space_policy_journal]
- [Space Policy Online][ref_space_policy_online]
- [SpaceNews][ref_spacenews]
- [SpaceNews National Security Space Launch Phase 3 Coverage][ref_spacenews_nssl_phase3]
- [SpaceX Corporate Site][ref_spacex_company]
- [SpaceX Crew-1 Operational Rotation 2020][ref_spacex_press_crew1_2020]
- [SpaceX CRS-1 Mission 2012][ref_spacex_press_crs1_2012]
- [SpaceX CRS-21 Mission 2020][ref_spacex_press_crs21_2020]
- [SpaceX CRS-7 Mission Loss 2015][ref_spacex_press_crs7_2015]
- [SpaceX Demo-1 Uncrewed Demonstration 2019][ref_spacex_press_demo1_2019]
- [SpaceX Demo-2 Crewed Demonstration 2020][ref_spacex_press_dm2_2020]
- [SpaceX Dragon C1 Demonstration 2010][ref_spacex_press_dragon_c1_2010]
- [SpaceX News Archive][ref_spacex_news_archive]
- [SpaceX Starshield Documentation][ref_spacex_starshield]
- [The Space Review][ref_the_space_review]
- [United Launch Alliance News][ref_ula_press]
- [United Nations Liability Convention of 1972][ref_un_liability_convention_1972]
- [United Nations Outer Space Treaty of 1967][ref_un_outer_space_treaty_1967]
- [United Nations Registration Convention of 1976][ref_un_registration_convention_1976]
- [United States Commercial Space Launch Competitiveness Act of 2015][ref_uscsla_2015]
- [United States Court of Federal Claims][ref_uscfc]
- [USAspending Federal Award Data][ref_usaspending]
- [Vandenberg Environmental Record][ref_vandenberg_slc4e_ea]
- [Wall Street Journal Technology Coverage][ref_wsj]
- [Washington Post Technology Coverage][ref_washington_post]

### Research

- [Adler and Clark 1991 Behind the Learning Curve][research_adler_clark_1991]
- [Aghion and Howitt 1992 A Model of Growth Through Creative Destruction][research_aghion_howitt_1992]
- [Alchian 1963 Reliability of Progress Curves in Airframe Production][research_alchian_1963]
- [Argote and Epple 1990 Learning Curves in Manufacturing][research_argote_epple_1990]
- [Argote and Ingram 2000 Knowledge Transfer A Basis for Competitive Advantage in Firms][research_argote_ingram_2000]
- [Argote and Miron-Spektor 2011 Organizational Learning From Experience to Knowledge][research_argote_miron_spektor_2011]
- [Arrow 1962 Economic Welfare and the Allocation of Resources for Invention][research_arrow_1962]
- [Bajari and Tadelis 2001 Incentives Versus Transaction Costs A Theory of Procurement Contracts][research_bajari_tadelis_2001]
- [Bajari McMillan and Tadelis 2009 Auctions Versus Negotiations in Procurement][research_bajari_mcmillan_tadelis_2009]
- [Baumol 1977 On the Proper Cost Tests for Natural Monopoly in a Multiproduct Industry][research_baumol_1977]
- [Block 2008 Swimming Against the Current The Rise of a Hidden Developmental State][research_block_2008]
- [Bonvillian 2018 DARPA and the Advanced Research Projects Agency Model][research_bonvillian_2018]
- [Bovaird 2004 Public-Private Partnerships From Contested Concepts to Prevalent Practice][research_bovaird_2004]
- [Che and Chung 1999 Contractual Remedies to the Holdup Problem][research_che_chung_1999]
- [Coase 1937 The Nature of the Firm][research_coase_1937]
- [Cohen and Levinthal 1990 Absorptive Capacity A New Perspective on Learning and Innovation][research_cohen_levinthal_1990]
- [Corts and Singh 2004 The Effect of Repeated Interaction on Contract Choice][research_corts_singh_2004]
- [Duane 1964 Learning Curve Approach to Reliability Monitoring][research_duane_1964]
- [Dutton and Thomas 1984 Treating Progress Functions as a Managerial Opportunity][research_dutton_thomas_1984]
- [Gagnepain and Ivaldi 2002 Incentive Regulatory Policies][research_gagnepain_ivaldi_2002]
- [Gompers 1995 Optimal Investment Monitoring and the Staging of Venture Capital][research_gompers_1995]
- [Grant 1996 Toward a Knowledge-Based Theory of the Firm][research_grant_1996]
- [Griliches 1979 Issues in Assessing the Contribution of Research and Development to Productivity Growth][research_griliches_1979]
- [Griliches and Lichtenberg 1984 R and D and Productivity Growth at the Industry Level][research_griliches_lichtenberg_1984]
- [Grossman and Hart 1986 The Costs and Benefits of Ownership][research_grossman_hart_1986]
- [Hall and Lerner 2010 The Financing of R and D and Innovation][research_hall_lerner_2010]
- [Hart and Moore 1990 Property Rights and the Nature of the Firm][research_hart_moore_1990]
- [Hodge and Greve 2007 Public-Private Partnerships An International Performance Review][research_hodge_greve_2007]
- [Huber 1991 Organizational Learning The Contributing Processes][research_huber_1991]
- [Kahneman and Tversky 1979 Prospect Theory][research_kahneman_tversky_1979]
- [Kalnins and Mayer 2004 Relationships and Hybrid Contracts][research_kalnins_mayer_2004]
- [Kaplan and Stromberg 2003 Financial Contracting Theory Meets the Real World][research_kaplan_stromberg_2003]
- [Kaplan and Stromberg 2004 Characteristics Contracts and Actions][research_kaplan_stromberg_2004]
- [Khan 2017 Amazon's Antitrust Paradox][research_khan_2017]
- [Kilby 1976 Invention of the Integrated Circuit][research_kilby_1976]
- [Klein Crawford and Alchian 1978 Vertical Integration Appropriable Rents and the Competitive Contracting Process][research_klein_crawford_alchian_1978]
- [Kogut and Zander 1992 Knowledge of the Firm Combinative Capabilities and the Replication of Technology][research_kogut_zander_1992]
- [Kortum and Lerner 2000 Assessing the Contribution of Venture Capital to Innovation][research_kortum_lerner_2000]
- [Krueger 1974 The Political Economy of the Rent-Seeking Society][research_krueger_1974]
- [Lafontaine and Slade 2007 Vertical Integration and Firm Boundaries][research_lafontaine_slade_2007]
- [Lerner 1994 The Syndication of Venture Capital Investments][research_lerner_1994_syndication]
- [Lerner 1996 The Government as Venture Capitalist][research_lerner_1996_government_program]
- [Levin and Tadelis 2010 Contracting for Government Services Theory and Evidence][research_levin_tadelis_2010]
- [Levitt and March 1988 Organizational Learning][research_levitt_march_1988]
- [Lieberman 1984 The Learning Curve and Pricing in the Chemical Processing Industries][research_lieberman_1984]
- [Maier 1998 Architecting Principles for Systems-of-Systems][research_maier_1998]
- [March 1991 Exploration and Exploitation in Organizational Learning][research_march_1991]
- [Masten 1984 The Organization of Production][research_masten_1984]
- [Monteverde and Teece 1982 Supplier Switching Costs and Vertical Integration][research_monteverde_teece_1982]
- [Myerson 1981 Optimal Auction Design][research_myerson_1981]
- [Nelson 1959 The Simple Economics of Basic Scientific Research][research_nelson_1959]
- [Nonaka 1994 A Dynamic Theory of Organizational Knowledge Creation][research_nonaka_1994]
- [Noyce 1976 Microelectronics][research_noyce_1976]
- [Rapping 1965 Learning and World War II Production Functions][research_rapping_1965]
- [Reuters 2024 Starshield Investigation][research_reuters_starshield_2024]
- [Romer 1990 Endogenous Technological Change][research_romer_1990]
- [Ross and Staw 1993 Organizational Escalation and Exit][research_ross_staw_1993]
- [Sage and Cuppan 2001 On the Systems Engineering and Management of Systems of Systems][research_sage_cuppan_2001]
- [Sahlman 1990 The Structure and Governance of Venture-Capital Organizations][research_sahlman_1990]
- [Simon 1962 The Architecture of Complexity][research_simon_1962]
- [Staw 1976 Knee-Deep in the Big Muddy][research_staw_1976]
- [Stigler 1971 The Theory of Economic Regulation][research_stigler_1971]
- [Tversky and Kahneman 1992 Advances in Prospect Theory][research_tversky_kahneman_1992]
-
- [Weiss and Thurbon 2021 Developmental State or Economic Statecraft][research_weiss_thurbon_2021]
- [Williamson 1971 The Vertical Integration of Production][research_williamson_1971]
- [Williamson 1975 Markets and Hierarchies][research_williamson_1975]
- [Williamson 2002 The Theory of the Firm as Governance Structure][research_williamson_2002]
- [Wright 1936 Factors Affecting the Cost of Airplanes][research_wright_1936]

### Related Post

- [A90 Introduction to Space Studies][related_post_a90_intro_space_studies]
- [A96 History of Rocketplanes][related_post_a96_history_rocketplanes]
- [A97 What Does the United States Space Force Do][related_post_a97_us_space_force]
- [A132 Introduction to the SBIR and STTR Programs][related_post_a132_sbir_intro]
- [A138 Phase III and the Valley of Death for SBIR and STTR][related_post_a138_sbir_phase3]
- [A140 Money Behind an SBIR or STTR Award][related_post_a140_sbir_money]
- [A164 Patents Trade Secrets and the Disclosure Tradeoff][related_post_a164_patents_trade_secrets]
- [A237 Framing and the Co-Development Mechanism][related_post_a237_aerospace_framing]
- [A246 Silicon Valley from Defense Contracting][related_post_a246_silicon_valley_defense]
- [A247 Software-Defined Aerospace and Autonomy][related_post_a247_software_defined_aerospace]
- [A248 Contemporary Snapshot and Extrapolation][related_post_a248_contemporary_snapshot]
- [A281 History of SpaceX Series Framing and the Seven-Plus-Three Forcing-Function Framework][related_post_a281_spacex_framing]
- [A282 History of SpaceX Value Gradient from Falcon 1 to Falcon 9 to Reusability][related_post_a282_spacex_value_gradient]
- [A283 History of SpaceX Anchor Demand from COTS-1 Salvation Through Commercial Crew, HLS, and Starshield][related_post_a283_spacex_anchor_demand]
- [A284 History of SpaceX Value Capture from Launch-Service Pricing and Vertical Integration into Starlink][related_post_a284_spacex_value_capture]
- [A285 History of SpaceX Decomposability of Falcon, Dragon, Heavy, and Starship as Independently Valuable Rungs][related_post_a285_spacex_decomposability]
- [A286 History of SpaceX Generality-Forcing from Mars Requirements as a Cross-Domain Capability Substrate][related_post_a286_spacex_generality_forcing]
- [A287 History of SpaceX Governance That Resists Capital Capture Across Thirty-Plus Funding Rounds][related_post_a287_spacex_governance]
- [A288 History of SpaceX Portfolio Patience and the Internalization of Tail Risk][related_post_a288_spacex_portfolio_patience]

[book_abbate_1999]: https://mitpress.mit.edu/9780262511155/inventing-the-internet/
[book_abbott_1988]: https://openlibrary.org/search?q=Abbott+The+System+of+Professions
[book_acemoglu_robinson_2012]: https://openlibrary.org/search?q=Acemoglu+and+Robinson+Why+Nations+Fail
[book_amsden_1989]: https://global.oup.com/academic/product/asias-next-giant-9780195076035
[book_argote_1999]: https://openlibrary.org/search?q=Argote+Organizational+Learning+Creating+Retaining+Transferring+Knowledge
[book_argyris_schon_1978]: https://www.pearson.com/en-us/subject-catalog/p/organizational-learning-a-theory-of-action-perspective/P200000005949
[book_bain_1968]: https://openlibrary.org/search?q=Bain+Industrial+Organization+1968
[book_beinhocker_2006]: https://www.hbsp.harvard.edu/product/5062-HBK-ENG
[book_berger_2021]: https://www.harpercollins.com/products/liftoff-eric-berger
[book_berger_2024]: https://openlibrary.org/search?q=Berger+Reentry+SpaceX
[book_berlin_2005]: https://global.oup.com/academic/product/the-man-behind-the-microchip-9780195311990
[book_bilstein_1996]: https://ntrs.nasa.gov/search?q=Stages+to+Saturn+Bilstein
[book_bilstein_2001]: https://jhupbooks.press.jhu.edu/title/flight-america
[book_blanchard_fabrycky_2011]: https://www.pearson.com/en-us/subject-catalog/p/systems-engineering-and-analysis/P200000003302
[book_bork_1978]: https://www.hup.harvard.edu/books/9780674032545
[book_buchanan_tullock_1962]: https://www.libertyfund.org/books/the-calculus-of-consent/
[book_buede_2009]: https://openlibrary.org/search?q=Buede+Engineering+Design+of+Systems+Models+and+Methods
[book_chaikin_2007]: https://openlibrary.org/search?q=Chaikin+A+Man+on+the+Moon
[book_chandler_1962]: https://mitpress.mit.edu/9780262530095/strategy-and-structure/
[book_chandler_1977]: https://www.hup.harvard.edu/books/9780674940529
[book_chandler_1990]: https://openlibrary.org/search?q=Chandler+Scale+and+Scope
[book_chang_2002]: https://www.penguin.co.uk/books/56082/kicking-away-the-ladder/9780857281050
[book_creswell_2014]: https://us.sagepub.com/en-us/nam/research-design/book255675
[book_crouch_2003]: https://wwnorton.com/books/Wings/
[book_cyert_march_1963]: https://openlibrary.org/search?q=Cyert+March+Behavioral+Theory+Firm
[book_davenport_2018]: https://www.hachettebookgroup.com/titles/christian-davenport/the-space-barons/9781610398299/
[book_dixit_pindyck_1994]: https://openlibrary.org/search?q=Dixit+and+Pindyck+Investment+Under+Uncertainty
[book_evans_1995]: https://press.princeton.edu/books/paperback/9780691037363/embedded-autonomy
[book_fallows_1981]: https://archive.org/details/nationaldefense00fall
[book_fernholz_2018]: https://www.hachettebookgroup.com/titles/tim-fernholz/rocket-billionaires/9781328662231/
[book_fligstein_2001]: https://press.princeton.edu/books/paperback/9780691102542/the-architecture-of-markets
[book_freeman_1987]: https://openlibrary.org/search?q=Freeman+Technology+Policy+and+Economic+Performance
[book_gompers_lerner_2001]: https://www.hbsp.harvard.edu/product/2434-HBK-ENG
[book_grief_2006]: https://www.cambridge.org/9780521671347
[book_grimsey_lewis_2004]: https://www.e-elgar.com/shop/gbp/public-private-partnerships-9781840647112.html
[book_groves_1962]: https://openlibrary.org/search?q=Groves+Now+It+Can+Be+Told
[book_handberg_1994]: https://openlibrary.org/search?q=Handberg+Reinventing+NASA
[book_hargrove_1994]: https://openlibrary.org/search?q=Hargrove+Prisoners+of+Myth
[book_hartley_2017]: https://openlibrary.org/search?q=Hartley+The+Economics+of+Arms
[book_hewlett_anderson_1962]: https://openlibrary.org/search?q=Hewlett+and+Anderson+The+New+World
[book_hosley_1996]: https://www.press.jhu.edu/books/title/1799/colt
[book_hounshell_1984]: https://jhupbooks.press.jhu.edu/title/american-system-mass-production-1800-1932
[book_hovenkamp_2005]: https://openlibrary.org/search?q=Hovenkamp+The+Antitrust+Enterprise
[book_hughes_1983]: https://jhupbooks.press.jhu.edu/title/networks-power
[book_hunter_2016]: https://csis-website-prod.s3.amazonaws.com/s3fs-public/legacy_files/files/publication/160930_Hunter_CreatingStrategicValue_Web.pdf
[book_johnson_1982]: https://www.sup.org/books/title/?id=2143
[book_kahn_1988]: https://mitpress.mit.edu/9780262610520/the-economics-of-regulation/
[book_kahneman_2011]: https://us.macmillan.com/books/9780374533557/thinkingfastandslow
[book_kaplan_1991]: https://openlibrary.org/search?q=Kaplan+The+Wizards+of+Armageddon
[book_kauffman_1993]: https://global.oup.com/academic/product/the-origins-of-order-9780195079517
[book_klerkx_2004]: https://us.macmillan.com/books/9780375421501/lostinspace
[book_kraemer_2006]: https://openlibrary.org/search?q=Kraemer+Rocketdyne+Powering+Humans+into+Space
[book_kranz_2000]: https://www.simonandschuster.com/books/Failure-Is-Not-an-Option/Gene-Kranz/9781439148815
[book_krige_et_al_2000]: https://www.esa.int/About_Us/ESA_history
[book_kunda_1992]: https://openlibrary.org/search?q=Kunda+Engineering+Culture
[book_laffont_tirole_1993]: https://mitpress.mit.edu/9780262121743/a-theory-of-incentives-in-procurement-and-regulation/
[book_landes_1969]: https://www.cambridge.org/9780521094184
[book_larson_1977]: https://www.ucpress.edu/book/9780520039070/the-rise-of-professionalism
[book_launius_1994]: https://openlibrary.org/search?q=Launius+NASA+History+United+States+Civil+Space+Program
[book_launius_2004]: https://global.oup.com/academic/product/frontiers-of-space-exploration-9780313325243
[book_lawrence_2016]: https://www.routledge.com/Airbus-vs-Boeing/Lawrence/p/book/9781138287884
[book_lecuyer_2006]: https://mitpress.mit.edu/9780262622110/making-silicon-valley/
[book_lerner_2009]: https://press.princeton.edu/books/hardcover/9780691142197/boulevard-of-broken-dreams
[book_logsdon_1970]: https://mitpress.mit.edu/9780262620109/the-decision-to-go-to-the-moon/
[book_logsdon_2010]: https://openlibrary.org/search?q=Logsdon+John+F+Kennedy+and+the+Race+to+the+Moon
[book_lundvall_1992]: https://openlibrary.org/search?q=Lundvall+National+Systems+of+Innovation
[book_malone_2014]: https://openlibrary.org/search?q=Malone+The+Intel+Trinity
[book_march_simon_1958]: https://www.wiley.com/en-us/Organizations%2C+2nd+Edition-p-9780631186311
[book_mazzucato_2013]: https://marianamazzucato.com/books/the-entrepreneurial-state
[book_mazzucato_2021]: https://marianamazzucato.com/books/mission-economy/
[book_mcafee_mcmillan_1988]: https://openlibrary.org/search?q=McAfee+and+McMillan+Incentives+in+Government+Contracting
[book_mccurdy_1994]: https://jhupbooks.press.jhu.edu/title/inside-nasa
[book_mcdougall_1985]: https://jhupbooks.press.jhu.edu/title/heavens-and-earth
[book_melman_1970]: https://openlibrary.org/search?q=Melman+Pentagon+Capitalism
[book_metcalfe_1998]: https://www.routledge.com/Evolutionary-Economics-and-Creative-Destruction/Metcalfe/p/book/9780415158671
[book_metrick_yasuda_2011]: https://openlibrary.org/search?q=Metrick+Yasuda+Venture+Capital+Finance+of+Innovation
[book_milgrom_2004]: https://www.cambridge.org/9780521551847
[book_miller_1995]: https://openlibrary.org/search?q=Miller+Lockheed+Skunk+Works+First+Fifty+Years
[book_mindell_2008]: https://mitpress.mit.edu/9780262516105/digital-apollo/
[book_mowery_rosenberg_1998]: https://openlibrary.org/search?q=Mowery+Rosenberg+Paths+of+Innovation
[book_murray_cox_1989]: https://www.simonandschuster.com/books/Apollo/Charles-Murray/9780671706258
[book_musa_1998]: https://openlibrary.org/search?q=Musa+Software+Reliability+Engineering
[book_nelson_1993]: https://global.oup.com/academic/product/national-innovation-systems-9780195076172
[book_nelson_winter_1982]: https://www.hup.harvard.edu/books/9780674272286
[book_newhouse_1982]: https://openlibrary.org/search?q=Newhouse+The+Sporty+Game
[book_newhouse_2007]: https://us.macmillan.com/books/9781400079131/boeingversusairbus
[book_nonaka_takeuchi_1995]: https://global.oup.com/academic/product/the-knowledge-creating-company-9780195092691
[book_norberg_oneill_1996]: https://jhupbooks.press.jhu.edu/title/transforming-computer-technology
[book_north_1990]: https://www.cambridge.org/9780521397346
[book_oconnor_kleyner_2012]: https://openlibrary.org/search?q=O+Connor+and+Kleyner+Practical+Reliability+Engineering
[book_ormerod_2005]: https://us.macmillan.com/books/9780375421099/whymostthingsfail
[book_osborne_2000]: https://www.routledge.com/Public-Private-Partnerships/Osborne/p/book/9780415225236
[book_ostrom_1990]: https://www.cambridge.org/9780521405997
[book_perez_2002]: https://openlibrary.org/search?q=Perez+Technological+Revolutions+and+Financial+Capital
[book_perrow_1984]: https://press.princeton.edu/books/paperback/9780691004129/normal-accidents
[book_porter_1980]: https://www.simonandschuster.com/books/Competitive-Strategy/Michael-E-Porter/9780684841489
[book_porter_1985]: https://www.simonandschuster.com/books/Competitive-Advantage/Michael-E-Porter/9780684841465
[book_posner_2001]: https://openlibrary.org/search?q=Posner+Antitrust+Law
[book_rhodes_1986]: https://www.simonandschuster.com/books/The-Making-of-the-Atomic-Bomb/Richard-Rhodes/9781451677614
[book_rich_janos_1994]: https://www.hachettebookgroup.com/titles/ben-r-rich/skunk-works/9780316743006/
[book_riordan_hoddeson_kolb_2015]: https://openlibrary.org/search?q=Riordan+Hoddeson+Kolb+Tunnel+Visions
[book_rosenberg_1976]: https://www.cambridge.org/9780521290111
[book_rosenberg_1982]: https://www.cambridge.org/9780521273671
[book_ruttan_2006]: https://global.oup.com/academic/product/is-war-necessary-for-economic-growth-9780195188042
[book_scherer_ross_1990]: https://openlibrary.org/search?q=Scherer+Ross+Industrial+Market+Structure
[book_schumpeter_1942]: https://www.harpercollins.com/products/capitalism-socialism-and-democracy-joseph-a-schumpeter
[book_selznick_1949]: https://www.ucpress.edu/book/9780520000384/tva-and-the-grass-roots
[book_senge_1990]: https://www.penguinrandomhouse.com/books/163984/the-fifth-discipline-by-peter-m-senge/
[book_serling_1992]: https://openlibrary.org/search?q=Serling+Legend+and+Legacy
[book_sharkey_1982]: https://www.cambridge.org/9780521271943
[book_simon_1957]: https://www.simonandschuster.com/books/Administrative-Behavior-4th-Edition/Herbert-A-Simon/9781439136218
[book_suh_2001]: https://global.oup.com/academic/product/axiomatic-design-9780195134667
[book_tirole_1988]: https://mitpress.mit.edu/9780262200714/the-theory-of-industrial-organization/
[book_trigeorgis_1996]: https://mitpress.mit.edu/9780262201025/real-options/
[book_vaughan_1996]: https://press.uchicago.edu/ucp/books/book/chicago/C/bo22781921.html
[book_wade_1990]: https://press.princeton.edu/books/paperback/9780691117294/governing-the-market
[book_weick_1979]: https://www.mheducation.com/highered/product/social-psychology-organizing-weick/M9780075548089.html
[book_weick_sutcliffe_2007]: https://openlibrary.org/search?q=Weick+and+Sutcliffe+Managing+the+Unexpected
[book_weiss_2014]: https://www.cornellpress.cornell.edu/book/9780801479922/america-inc/
[book_williamson_1985]: https://www.simonandschuster.com/books/The-Economic-Institutions-of-Capitalism/Oliver-E-Williamson/9780684863740
[book_woo_cumings_1999]: https://www.cornellpress.cornell.edu/book/9780801485664/the-developmental-state/
[book_yescombe_2007]: https://www.sciencedirect.com/book/9780750680547/public-private-partnerships
[book_yin_2014]: https://us.sagepub.com/en-us/nam/case-study-research-and-applications/book250150
[ref_10_usc_2371b]: https://www.law.cornell.edu/uscode/text/10/2371b
[ref_51_usc_20113]: https://www.law.cornell.edu/uscode/text/51/20113
[ref_51_usc_51302_saa]: https://www.law.cornell.edu/uscode/text/51/51302
[ref_aiaa_jsr]: https://arc.aiaa.org/journal/jsr
[ref_arianespace]: https://www.arianespace.com/
[ref_arstechnica_space]: https://arstechnica.com/science/space/
[ref_aviation_week]: https://aviationweek.com/
[ref_bloomberg]: https://www.bloomberg.com/
[ref_blue_origin_press]: https://www.blueorigin.com/news/
[ref_boeing_historical_archives]: https://www.boeing.com/history/
[ref_boeing_press]: https://boeing.mediaroom.com/
[ref_boeing_starliner_cft_2024]: https://www.boeing.com/space/starliner
[ref_breaking_defense]: https://breakingdefense.com/
[ref_caib_report_2003]: https://www.govinfo.gov/app/details/GPO-CAIB
[ref_china_commercial_space]: https://spacenews.com/topic/china/
[ref_chinese_space_program]: https://www.cnsa.gov.cn/english/
[ref_congressional_record]: https://www.congress.gov/congressional-record
[ref_crs_artemis_2022]: https://crsreports.congress.gov/product/pdf/R/R47064
[ref_crs_commercial_crew]: https://crsreports.congress.gov/product/pdf/R/R44708
[ref_crs_commercial_crew_2018]: https://crsreports.congress.gov/product/pdf/R/R45272
[ref_crs_reports]: https://crsreports.congress.gov/
[ref_csla_1984]: https://www.law.cornell.edu/uscode/text/51/subtitle-V/chapter-509
[ref_csla_amendments_2004]: https://www.congress.gov/108/plaws/publ492/PLAW-108publ492.pdf
[ref_defense_news]: https://www.defensenews.com/
[ref_dod_contracts]: https://www.defense.gov/News/Contracts/
[ref_dod_other_transactions]: https://aida.mitre.org/ota/
[ref_faa_ast_licensing_regs_450]: https://www.ecfr.gov/current/title-14/chapter-III/subchapter-C/part-450
[ref_faa_ast_regulations]: https://www.ecfr.gov/current/title-14/chapter-III
[ref_faa_launch_licenses_current]: https://www.faa.gov/space
[ref_far_part_12]: https://www.acquisition.gov/far/part-12
[ref_far_part_15]: https://www.acquisition.gov/far/part-15
[ref_far_part_16]: https://www.acquisition.gov/far/part-16
[ref_far_part_35]: https://www.acquisition.gov/far/part-35
[ref_fpds]: https://www.fpds.gov/
[ref_gao_2014_commercial_crew]: https://www.gao.gov/products/gao-14-593
[ref_gao_2020_commercial_crew]: https://www.gao.gov/products/gao-20-121
[ref_gao_bid_protest]: https://www.gao.gov/legal/bid-protests
[ref_gao_ccp_2019]: https://www.gao.gov/products/gao-19-504
[ref_gao_cots_2009]: https://www.gao.gov/products/gao-09-618
[ref_gao_cots_2011]: https://www.gao.gov/products/gao-11-692t
[ref_gao_hls_2022]: https://www.gao.gov/products/gao-22-105506
[ref_gao_hls_bid_protest_2021]: https://www.gao.gov/products/b-419783
[ref_gao_nssl_2023]: https://www.gao.gov/products/gao-23-105815
[ref_gao_reports]: https://www.gao.gov/reports-testimonies
[ref_heilmeier_catechism]: https://www.darpa.mil/about-us/heilmeier-catechism
[ref_house_science_committee_hearings]: https://science.house.gov/
[ref_incose_handbook]: https://www.incose.org/products-and-publications/se-handbook
[ref_isro_press]: https://www.isro.gov.in/
[ref_itar_22_cfr_120_130]: https://www.ecfr.gov/current/title-22/chapter-I/subchapter-M
[ref_jaxa_press]: https://global.jaxa.jp/press/
[ref_journal_public_procurement]: https://www.emerald.com/insight/publication/issn/1535-0118
[ref_journal_space_law]: https://airandspacelaw.olemiss.edu/journal-of-space-law/
[ref_ksc_lc39a_lease]: https://www.nasa.gov/kennedy/
[ref_kwajalein_atoll_documentation]: https://www.army.mil/usakwajalein
[ref_nasa_act_1958]: https://history.nasa.gov/spaceact.html
[ref_nasa_auth_2010]: https://www.congress.gov/111/plaws/publ267/PLAW-111publ267.pdf
[ref_nasa_ccp_certification]: https://www.nasa.gov/humans-in-space/commercial-space/
[ref_nasa_ccp_documents]: https://www.nasa.gov/commercialcrew/
[ref_nasa_commercial_space]: https://www.nasa.gov/commercial-space/
[ref_nasa_constellation]: https://www.nasa.gov/history/history-publications-and-resources/nasa-history-series/
[ref_nasa_cots_2011]: https://ntrs.nasa.gov/citations/20120000953
[ref_nasa_cots_report]: https://ntrs.nasa.gov/search?q=Commercial+Orbital+Transportation+Services
[ref_nasa_cots_solicitation_2006]: https://ntrs.nasa.gov/search?q=Commercial+Orbital+Transportation+Services+solicitation
[ref_nasa_crs2_press_2016]: https://www.nasa.gov/news-release/nasa-awards-international-space-station-cargo-transport-contracts/
[ref_nasa_crs_program_overview]: https://www.nasa.gov/commercial-resupply/
[ref_nasa_far_supplement]: https://www.hq.nasa.gov/office/procurement/regs/NFS.pdf
[ref_nasa_history]: https://history.nasa.gov/
[ref_nasa_hls_option_a_2021]: https://www.nasa.gov/humans-in-space/artemis/
[ref_nasa_hls_option_b_2022]: https://www.nasa.gov/mission/artemis-iii/
[ref_nasa_hls_program]: https://www.nasa.gov/humans-in-space/human-landing-system/
[ref_nasa_hls_solicitation]: https://sam.gov/opp/human-landing-system/
[ref_nasa_hls_sustainable_2023]: https://www.nasa.gov/press-release/nasa-selects-blue-origin-as-second-artemis-lunar-lander-provider/
[ref_nasa_news]: https://www.nasa.gov/news/
[ref_nasa_npr_7120_5f]: https://nodis3.gsfc.nasa.gov/npg_img/N_PR_7120_005F_/N_PR_7120_005F_.pdf
[ref_nasa_ntrs]: https://ntrs.nasa.gov/
[ref_nasa_oig_artemis_2022]: https://oig.nasa.gov/docs/IG-22-003.pdf
[ref_nasa_oig_ccp_cargo_2018]: https://oig.nasa.gov/docs/IG-18-016.pdf
[ref_nasa_oig_cots_2013]: https://oig.nasa.gov/docs/IG-13-016.pdf
[ref_nasa_oig_hls_2021]: https://oig.nasa.gov/docs/IG-21-024.pdf
[ref_nasa_oig_reports]: https://oig.nasa.gov/audits/
[ref_nasa_partnerships]: https://www.nasa.gov/partnerships/
[ref_nasa_se_handbook]: https://www.nasa.gov/reference/systems-engineering-handbook/
[ref_nasa_sls_program]: https://www.nasa.gov/humans-in-space/space-launch-system/
[ref_nasa_std_8709_22]: https://standards.nasa.gov/
[ref_nasaspaceflight]: https://www.nasaspaceflight.com/
[ref_nber]: https://www.nber.org/
[ref_northrop_grumman_press]: https://news.northropgrumman.com/
[ref_ntrs_x33]: https://ntrs.nasa.gov/search?q=X-33%20reusable%20launch%20vehicle
[ref_nyt]: https://www.nytimes.com/section/science/space
[ref_nyt_starshield_2024]: https://www.nytimes.com/2024/02/16/us/politics/spacex-us-spy-agency-satellites.html
[ref_omb_circular_a11]: https://www.whitehouse.gov/omb/information-for-agencies/circulars/
[ref_payload]: https://payloadspace.com/
[ref_payload_research]: https://payloadspace.com/research/
[ref_public_admin_review]: https://onlinelibrary.wiley.com/journal/15406210
[ref_rocket_lab_press]: https://www.rocketlabusa.com/updates/
[ref_rogers_commission_1986]: https://history.nasa.gov/rogersrep/genindex.htm
[ref_sba_sbir_policy_directive]: https://www.sbir.gov/about
[ref_sbir_gov]: https://www.sbir.gov/
[ref_sbir_statute_15usc638]: https://www.law.cornell.edu/uscode/text/15/638
[ref_sec_edgar]: https://www.sec.gov/edgar/searchedgar/companysearch
[ref_space_force_news]: https://www.spaceforce.mil/News/
[ref_space_force_nssl]: https://www.spaceforce.mil/News/Fact-Sheets
[ref_space_force_nssl_phase1a_2018]: https://www.af.mil/News/Article-Display/Article/1671253/
[ref_space_force_nssl_phase2_2020]: https://www.spaceforce.mil/News/Article/2312953/
[ref_space_policy_journal]: https://www.sciencedirect.com/journal/space-policy
[ref_space_policy_online]: https://spacepolicyonline.com/
[ref_spacenews]: https://spacenews.com/
[ref_spacenews_nssl_phase3]: https://spacenews.com/?s=NSSL+Phase+3
[ref_spacex_company]: https://www.spacex.com/
[ref_spacex_news_archive]: https://www.spacex.com/updates/
[ref_spacex_press_crew1_2020]: https://www.spacex.com/updates/
[ref_spacex_press_crs1_2012]: https://www.spacex.com/updates/
[ref_spacex_press_crs21_2020]: https://www.spacex.com/updates/
[ref_spacex_press_crs7_2015]: https://www.spacex.com/updates/
[ref_spacex_press_demo1_2019]: https://www.spacex.com/updates/
[ref_spacex_press_dm2_2020]: https://www.spacex.com/updates/dm-2-launch-crewed-flight/
[ref_spacex_press_dragon_c1_2010]: https://www.spacex.com/updates/
[ref_spacex_starshield]: https://www.spacex.com/starshield/
[ref_ssrn]: https://www.ssrn.com/
[ref_the_space_review]: https://www.thespacereview.com/
[ref_ula_press]: https://www.ulalaunch.com/about/news
[ref_un_liability_convention_1972]: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/liability-convention.html
[ref_un_outer_space_treaty_1967]: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/outerspacetreaty.html
[ref_un_registration_convention_1976]: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/registration-convention.html
[ref_usaspending]: https://www.usaspending.gov/
[ref_uscfc]: https://www.uscfc.uscourts.gov/
[ref_uscsla_2015]: https://www.congress.gov/114/plaws/publ90/PLAW-114publ90.pdf
[ref_vandenberg_slc4e_ea]: https://www.faa.gov/space/environmental
[ref_washington_post]: https://www.washingtonpost.com/business/technology/
[ref_wsj]: https://www.wsj.com/tech
[research_adler_clark_1991]: https://pubsonline.informs.org/doi/10.1287/mnsc.37.3.267
[research_aghion_howitt_1992]: https://www.jstor.org/stable/2951599
[research_alchian_1963]: https://doi.org/10.2307/1909166
[research_argote_epple_1990]: https://www.science.org/doi/10.1126/science.247.4945.920
[research_argote_ingram_2000]: https://www.sciencedirect.com/science/article/abs/pii/S0749597800928930
[research_argote_miron_spektor_2011]: https://pubsonline.informs.org/doi/10.1287/orsc.1100.0621
[research_arrow_1962]: https://www.nber.org/system/files/chapters/c2144/c2144.pdf
[research_bajari_mcmillan_tadelis_2009]: https://academic.oup.com/jleo/article-abstract/25/2/372/845776
[research_bajari_tadelis_2001]: https://www.jstor.org/stable/2696367
[research_baumol_1977]: https://www.jstor.org/stable/1807012
[research_block_2008]: https://doi.org/10.1177/0032329208318731
[research_bonvillian_2018]: https://mitpress.mit.edu/9780262038522/the-darpa-model-for-transformative-technologies/
[research_bovaird_2004]: https://doi.org/10.1177/0020852304044250
[research_che_chung_1999]: https://academic.oup.com/rand/article-abstract/30/1/97/2701540
[research_coase_1937]: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-0335.1937.tb00002.x
[research_cohen_levinthal_1990]: https://www.jstor.org/stable/2393553
[research_corts_singh_2004]: https://academic.oup.com/jleo/article-abstract/20/1/230/970131
[research_duane_1964]: https://ieeexplore.ieee.org/document/4051464
[research_dutton_thomas_1984]: https://doi.org/10.2307/258437
[research_gagnepain_ivaldi_2002]: https://academic.oup.com/rand/article-abstract/33/4/605/2603099
[research_gompers_1995]: https://www.jstor.org/stable/2329227
[research_grant_1996]: https://onlinelibrary.wiley.com/doi/10.1002/smj.4250171110
[research_griliches_1979]: https://www.jstor.org/stable/3003318
[research_griliches_lichtenberg_1984]: https://www.nber.org/system/files/chapters/c10054/c10054.pdf
[research_grossman_hart_1986]: https://www.jstor.org/stable/1833199
[research_hall_lerner_2010]: https://www.sciencedirect.com/science/article/pii/S0169721810010142
[research_hart_moore_1990]: https://www.jstor.org/stable/2937861
[research_hodge_greve_2007]: https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6210.2007.00736.x
[research_huber_1991]: https://pubsonline.informs.org/doi/10.1287/orsc.2.1.88
[research_kahneman_tversky_1979]: https://www.jstor.org/stable/1914185
[research_kalnins_mayer_2004]: https://doi.org/10.1093/jleo/ewh030
[research_kaplan_stromberg_2003]: https://academic.oup.com/restud/article-abstract/70/2/281/1571073
[research_kaplan_stromberg_2004]: https://academic.oup.com/rfs/article-abstract/17/1/1/1601330
[research_khan_2017]: https://www.yalelawjournal.org/note/amazons-antitrust-paradox
[research_kilby_1976]: https://ieeexplore.ieee.org/document/1454570
[research_klein_crawford_alchian_1978]: https://www.jstor.org/stable/725234
[research_kogut_zander_1992]: https://pubsonline.informs.org/doi/10.1287/orsc.3.3.383
[research_kortum_lerner_2000]: https://www.rand.org/pubs/reprints/RP924.html
[research_krueger_1974]: https://www.jstor.org/stable/1808883
[research_lafontaine_slade_2007]: https://www.aeaweb.org/articles?id=10.1257/jel.45.3.629
[research_lerner_1994_syndication]: https://www.jstor.org/stable/3665602
[research_lerner_1996_government_program]: https://www.nber.org/papers/w5753
[research_levin_tadelis_2010]: https://academic.oup.com/qje/article-abstract/125/3/1103/1903637
[research_levitt_march_1988]: https://www.annualreviews.org/doi/10.1146/annurev.so.14.080188.001535
[research_lieberman_1984]: https://www.jstor.org/stable/2555589
[research_maier_1998]: https://onlinelibrary.wiley.com/doi/10.1002/(SICI)1520-6858(1998)1:4%3C267::AID-SYS3%3E3.0.CO;2-D
[research_march_1991]: https://pubsonline.informs.org/doi/10.1287/orsc.2.1.71
[research_masten_1984]: https://www.jstor.org/stable/725228
[research_monteverde_teece_1982]: https://www.jstor.org/stable/3003400
[research_myerson_1981]: https://pubsonline.informs.org/doi/10.1287/moor.6.1.58
[research_nelson_1959]: https://www.journals.uchicago.edu/doi/10.1086/258177
[research_nonaka_1994]: https://pubsonline.informs.org/doi/10.1287/orsc.5.1.14
[research_noyce_1976]: https://ieeexplore.ieee.org/document/1454572
[research_rapping_1965]: https://www.jstor.org/stable/1928223
[research_reuters_starshield_2024]: https://www.reuters.com/technology/space/musks-spacex-is-building-spy-satellite-network-us-intelligence-agency-sources-2024-03-16/
[research_romer_1990]: https://www.journals.uchicago.edu/doi/10.1086/261725
[research_ross_staw_1993]: https://doi.org/10.2307/256756
[research_sage_cuppan_2001]: https://doi.org/10.3233/iks-2001-00045
[research_sahlman_1990]: https://www.sciencedirect.com/science/article/pii/0304405X9090065E
[research_simon_1962]: https://www.jstor.org/stable/985254
[research_staw_1976]: https://www.sciencedirect.com/science/article/abs/pii/003050737690005X
[research_stigler_1971]: https://www.jstor.org/stable/3003160
[research_tversky_kahneman_1992]: https://link.springer.com/article/10.1007/BF00122574
[research_weiss_thurbon_2021]: https://doi.org/10.1080/13563467.2020.1766431
[research_williamson_1971]: https://www.jstor.org/stable/1815199
[research_williamson_1975]: https://www.jstor.org/stable/40751236
[research_williamson_2002]: https://www.aeaweb.org/articles?id=10.1257/089533002760278776
[research_wright_1936]: https://arc.aiaa.org/doi/10.2514/8.155
[related_post_a90_intro_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[related_post_a96_history_rocketplanes]: {% post_url 2026-02-27-history_of_rocketplanes %}
[related_post_a97_us_space_force]: {% post_url 2026-02-28-what_does_united_states_space_force_do %}
[related_post_a132_sbir_intro]: {% post_url 2026-06-15-introduction_to_the_sbir_and_sttr_programs %}
[related_post_a138_sbir_phase3]: {% post_url 2026-06-21-phase_iii_and_the_valley_of_death_for_sbir_and_sttr %}
[related_post_a140_sbir_money]: {% post_url 2026-06-23-money_behind_an_sbir_or_sttr_award %}
[related_post_a164_patents_trade_secrets]: {% post_url 2026-05-06-patents_trade_secrets_and_the_disclosure_tradeoff %}
[related_post_a237_aerospace_framing]: {% post_url 2026-07-12-framing_and_the_co_development_mechanism %}
[related_post_a246_silicon_valley_defense]: {% post_url 2026-07-21-silicon_valley_from_defense_contracting %}
[related_post_a247_software_defined_aerospace]: {% post_url 2026-07-22-software_defined_aerospace_and_autonomy %}
[related_post_a248_contemporary_snapshot]: {% post_url 2026-07-23-contemporary_snapshot_and_extrapolation %}
[related_post_a281_spacex_framing]: {% post_url 2026-07-24-spacex_history_framing %}
[related_post_a282_spacex_value_gradient]: {% post_url 2026-07-25-spacex_history_value_gradient %}
[related_post_a283_spacex_anchor_demand]: {% post_url 2026-07-26-spacex_history_anchor_demand %}
[related_post_a284_spacex_value_capture]: {% post_url 2026-07-27-spacex_history_value_capture %}
[related_post_a285_spacex_decomposability]: {% post_url 2026-07-28-spacex_history_decomposability %}
[related_post_a286_spacex_generality_forcing]: {% post_url 2026-07-29-spacex_history_generality_forcing %}
[related_post_a287_spacex_governance]: {% post_url 2026-07-30-spacex_history_governance %}
[related_post_a288_spacex_portfolio_patience]: {% post_url 2026-07-31-spacex_history_portfolio_patience %}
