---
layout: post
mathjax: true
comments: true
title:  "History of SpaceX: The Government-Anchor Capital-Formation Leg and Non-Dilutive Development Finance"
date:   2026-08-01 09:00:00 +0000
categories: history business aerospace
series: spacex_history
series_title: History of SpaceX
series_index: 9
---

<!-- A289 -->
<script>console.log("A289");</script>

This article is the ninth in the History of SpaceX series and the first of three treating the capital-formation legs that the [series opener][related_post_a281_spacex_framing] introduced alongside the seven forcing-function conditions. The government-anchor leg is distinguished from the anchor-demand condition that the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] treats by a distinction the article develops throughout. Anchor demand concerns the existence of a specific identifiable customer who will buy a specific output. The government-anchor capital-formation leg concerns the specific mechanism by which the specific government relationship supplied capital to build the specific capability before any specific output existed, and supplied it without taking equity, without taking votes, and without imposing the specific covenants that private development capital of comparable magnitude would have carried. The article walks the specific Space Act Agreement instrument under which the specific development funding was extended, the specific Commercial Orbital Transportation Services round-one awards of August 2006 and the specific Rocketplane Kistler termination of 2007 that demonstrates the specific instrument operating as designed, the specific milestone-payment mechanics and the specific non-dilutive property that constitutes the analytical core of the article, the specific Commercial Resupply Services transition of December 2008, the specific Commercial Crew progression from the specific 2010 Commercial Crew Development awards through the specific September 16 2014 Commercial Crew Transportation Capability awards, the specific Boeing comparison that demonstrates the specific risk transfer a specific fixed-price instrument accomplishes, the specific National Security Space Launch certification progression across the specific 2018 Phase 1A, the specific 2020 Phase 2, and the specific 2024 Phase 3 Lane 2 awards, and the specific Starshield classified anchor. The article treats the specific Small Business Innovation Research Phase III sole-source authority that the [Phase III and the Valley of Death article A138][related_post_a138_sbir_phase3] develops as the specific closest statutory analogue to the specific structural pattern under which a specific development award produces a specific provider who subsequently receives a specific services contract. The article contrasts the specific instrument against the specific cost-plus counterfactual that the specific Constellation and specific Space Launch System programmes realized. The article closes with an explicit pattern-extraction section stating the abstract government-anchor capital-formation mechanic in a form other informed readers can recognize in adjacent domains without naming any specific downstream application.

## The Government-Anchor Capital-Formation Mapping Problem

The mapping problem for a comprehensive treatment of the government-anchor capital-formation leg in the SpaceX case is the question of how much capital the specific government relationship supplied, on what specific terms, at what specific stages, and what specific alternative terms the specific venture would have faced had the specific capital been raised privately instead.

The problem is distinct from the anchor-demand problem in a way that deserves statement at the outset, because the specific two are routinely conflated in the specific commentary. A specific customer who purchases a specific delivered service supplies revenue. A specific customer who pays against specific development milestones before any specific service exists supplies capital. The specific distinction admits the compact statement

$$\text{revenue} \; : \; p \cdot q \quad \text{with} \quad q > 0 \qquad \text{against} \qquad \text{development capital} \; : \; \sum_j m_j \quad \text{with} \quad q = 0$$

with the specific first requiring a specific delivered quantity and the specific second requiring only a specific demonstrated milestone. The specific COTS awards belong to the specific second category and the specific Commercial Resupply Services contracts to the specific first, and the specific transition between them is the specific event the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] treats.

The problem admits several formalizations depending on the analytical tradition consulted. The procurement-mechanism-design tradition from [Laffont and Tirole 1993][book_laffont_tirole_1993] A Theory of Incentives in Procurement and Regulation and [McAfee and McMillan 1988][book_mcafee_mcmillan_1988] Incentives in Government Contracting treats the specific instrument as a point on the specific continuum between a specific cost-reimbursement and a specific fixed-price arrangement, indexed by the specific power of the specific incentive scheme. The transaction-cost tradition from [Williamson 1975][research_williamson_1975] and [Williamson 1985][book_williamson_1985] treats the specific instrument as a specific governance structure selected to economize on the specific contracting hazards a specific novel and specific asset-specific development presents. The entrepreneurial-finance tradition from [Sahlman 1990][research_sahlman_1990] and [Gompers 1995][research_gompers_1995] treats the specific milestone structure as a specific staged financing whose specific tranches are released against specific verified progress. The public-finance and innovation-policy tradition from [Arrow 1962][research_arrow_1962] and [Nelson 1959][research_nelson_1959] treats the specific arrangement as a specific public response to a specific underinvestment arising from the specific appropriability failure a specific novel capability exhibits. The present article draws on all four traditions while adopting the mission-oriented-innovation framework the [series opener][related_post_a281_spacex_framing] established as primary.

The general form of the capital-formation problem can be stated compactly. Let $K^{\text{gov}}(t)$, $K^{\text{equity}}(t)$, and $K^{\text{debt}}(t)$ denote the specific cumulative capital supplied through each specific channel. The specific total admits the identity

$$K^{\text{total}}(t) = K^{\text{gov}}(t) + K^{\text{equity}}(t) + K^{\text{debt}}(t)$$

and the specific question the leg poses is what fraction the specific first term contributed at each specific stage and what the specific venture would have paid for the specific same amount through the specific other channels.

The specific defining property of the specific government channel is that it carries no specific claim on the specific residual and no specific claim on the specific control. The specific property admits the compact statement

$$\frac{\partial e^{\text{founder}}}{\partial K^{\text{gov}}} = 0 \qquad \text{and} \qquad \frac{\partial v^{\text{founder}}}{\partial K^{\text{gov}}} = 0$$

against the specific corresponding derivatives for the specific equity channel, which are strictly negative for the specific first and weakly negative for the specific second under the specific arrangements the [Governance article A287][related_post_a287_spacex_governance] documents. The specific property is the specific reason the article treats the specific channel as a specific distinct leg rather than as a specific variety of customer revenue, and it is the specific reason the specific three legs are analytically separable rather than substitutable.

The specific identification problem is the specific counterfactual. The specific counterfactual differential admits the compact form

$$\Delta V^{\text{gov-anchor}}_i(t) = V^{\text{observed}}_i(t) - V^{\text{private-capital counterfactual}}_i(t)$$

with the specific attribution equal to the difference between the specific observed trajectory and the specific counterfactual in which the specific development capital was raised privately on the specific terms available at the specific time. The specific counterfactual is unusually tractable relative to those of the preceding articles, because the specific terms available privately in the specific 2006 through 2008 period are partially documented through the specific rounds the Patient-Private Capital-Formation Leg article A290 will treat, and because the specific Rocketplane Kistler case supplies a specific observation of what happened to a specific competitor that attempted the specific private path.

## Methodological Commitments

The article commits to the same seven methodological positions the [series opener][related_post_a281_spacex_framing] established, restated at compact reference level.

The first commitment is descriptive-analytical framing rather than prescriptive advocacy. The commitment is strained here because the specific COTS instrument has become a specific policy exemplar cited in support of specific procurement reforms across specific unrelated domains, and the specific literature advocating its extension is substantially larger than the specific literature evaluating it.

The second commitment is dual-register composition with both general-history and abstract-mechanic registers.

The third commitment is primary-source anchoring. The specific documentary position for this specific article is the strongest in the series, because the specific government party to every specific transaction is subject to specific disclosure obligations the specific private party is not. The article cites the specific [National Aeronautics and Space Act][ref_nasa_act_1958], the specific [Space Act Agreement authority at 51 USC 20113][ref_51_usc_20113], the specific [NASA partnerships and Space Act Agreements guidance][ref_nasa_partnerships], the specific [NASA Federal Acquisition Regulation Supplement][ref_nasa_far_supplement], the specific [Federal Acquisition Regulation Part 15][ref_far_part_15] and [Part 16][ref_far_part_16] provisions governing negotiated procurement and contract types, the specific [NASA commercial space documentation][ref_nasa_cots_solicitation_2006], the specific [NASA COTS programme literature][ref_nasa_cots_report], the specific [CRS-2 award announcement][ref_nasa_crs2_press_2016], the specific [NASA news releases][ref_nasa_news] carrying the specific award and termination announcements, the specific [Commercial Crew Program documentation][ref_nasa_ccp_documents] and [certification record][ref_nasa_ccp_certification], the specific [Space Force National Security Space Launch][ref_space_force_nssl] framework with the specific [Phase 1A][ref_space_force_nssl_phase1a_2018], [Phase 2][ref_space_force_nssl_phase2_2020], and [Phase 3 Lane 2][ref_spacenews_nssl_phase3] awards, the specific [Department of Defense contract announcements][ref_dod_contracts], the specific [Federal Procurement Data System][ref_fpds] and [USAspending][ref_usaspending] records, and the specific oversight record in the specific [GAO reports database][ref_gao_reports] and the specific [NASA Office of Inspector General reports database][ref_nasa_oig_reports].

The fourth commitment is contested-claim marking, with specific attention to the specific counterfactual development-cost estimates that the specific NASA analyses produced and that the article treats as model outputs rather than as measurements.

The fifth commitment is temporal indexing as a mid-2026 snapshot.

The sixth commitment is terminological transparency with the Terminological Note section below, with specific attention to the specific distinction between a specific Space Act Agreement and a specific Federal Acquisition Regulation contract, which are legally distinct instruments that the specific commentary routinely conflates.

The seventh commitment is thesis-not-proof framing of the capital-formation closure claim.

## Government Anchor Capital as an Economic Property

The government-anchor capital-formation property is treated as a specific economic property of the specific financing channel that distinguishes ventures able to fund a specific capability development from a specific customer relationship from ventures that must fund it from the specific capital markets.

The specific property has three components. The specific first is magnitude, concerning how much capital the specific channel supplied. The specific second is timing, concerning whether the specific capital arrived at the specific stages when the specific alternatives were most expensive. The specific third is terms, concerning what the specific capital cost in claims surrendered.

The specific cost-of-capital comparison across the specific channels admits the compact form

$$r^{\text{gov}} \ll r^{\text{equity}} \qquad \text{with} \qquad r^{\text{gov}} = \text{value of concessions granted per dollar received}$$

with the specific government channel carrying a specific cost that is not zero but that is denominated in specific non-financial concessions comprising specific reporting obligations, specific audit exposure, specific mission-assurance requirements, specific export-control compliance under the specific [ITAR provisions][ref_itar_22_cfr_120_130], and a specific degree of programmatic direction. The specific concessions are real and the article does not treat the specific channel as free capital. The specific claim is the weaker and more defensible one that the specific concessions are cheaper than the specific equity dilution the specific alternative would have required.

The specific dilution avoided admits direct computation in principle. Let $K^{\text{gov}}$ denote the specific government development capital and let $V$ denote the specific firm valuation at the specific time it was received. The specific equity that would have been surrendered to raise the specific same amount privately is

$$\delta^{\text{avoided}} = \frac{K^{\text{gov}}}{V + K^{\text{gov}}}$$

evaluated at the specific contemporaneous valuation. The specific expression is large when the specific capital is received at a specific low valuation, which is precisely when a specific development-stage venture receives it. The specific timing property therefore compounds the specific terms property rather than merely accompanying it.

The specific milestone structure admits treatment as a specific option strip. The specific paying party holds at each specific milestone the specific right to discontinue, and the specific value of the specific arrangement to the specific paying party is

$$V^{\text{payer}} = \sum_{j} \pi_j \cdot \left[ B_j - m_j \right] \qquad \text{with} \qquad \pi_j = \prod_{k < j} P\!\left( \text{milestone } k \text{ achieved} \right)$$

with the specific expected outlay conditional on the specific programme surviving to each specific stage. The specific structure caps the specific payer's exposure at the specific milestones actually achieved, which is the specific property that distinguishes it from a specific cost-reimbursement arrangement in which the specific payer bears the specific overrun.

The specific incentive-power parameter that the [Laffont and Tirole 1993][book_laffont_tirole_1993] apparatus defines admits the compact form

$$b = 1 - \frac{\partial \, \text{payment}}{\partial \, \text{cost}}$$

taking the specific value zero for a specific pure cost-reimbursement arrangement in which every specific additional dollar of cost is reimbursed, and the specific value unity for a specific pure fixed-price arrangement in which the specific payment is invariant to the specific cost. The specific COTS and specific Commercial Crew instruments sit at or near $b = 1$, and the specific Constellation and specific Space Launch System instruments sit near $b = 0$. The specific parameter is the specific single most useful summary of the specific difference between the specific two procurement regimes the article compares.

The specific risk allocation follows directly from the specific incentive power. The specific overrun borne by the specific provider is

$$L^{\text{provider}} = b \cdot \left( C^{\text{actual}} - C^{\text{estimated}} \right)^{+}$$

with the specific provider bearing the specific entire overrun at $b = 1$ and none at $b = 0$. The specific transfer is the specific mechanism by which the specific fixed-price instrument converts a specific public cost risk into a specific private one, and the specific Boeing comparison the article develops is the specific clearest available demonstration of the specific transfer operating.

The specific cost-share requirement that the specific COTS instrument imposed admits the compact statement

$$K^{\text{private}} \geq \alpha \cdot K^{\text{gov}}$$

with the specific provider required to supply a specific matching contribution. The specific requirement is what converts the specific instrument from a specific subsidy into a specific co-investment, and it is the specific requirement whose specific failure terminated the specific Rocketplane Kistler agreement.

## Cross-Disciplinary Framings

The government-anchor capital-formation property admits characterization from several disciplinary traditions beyond the mission-oriented-innovation framework the series adopts as primary.

The procurement-mechanism-design tradition traces from [Laffont and Tirole 1993][book_laffont_tirole_1993] and [McAfee and McMillan 1988][book_mcafee_mcmillan_1988] through [Myerson 1981][research_myerson_1981] Optimal Auction Design, [Milgrom 2004][book_milgrom_2004] Putting Auction Theory to Work, [Bajari and Tadelis 2001][research_bajari_tadelis_2001] Incentives Versus Transaction Costs, [Bajari McMillan and Tadelis 2009][research_bajari_mcmillan_tadelis_2009], [Levin and Tadelis 2010][research_levin_tadelis_2010] Contracting for Government Services, [Corts and Singh 2004][research_corts_singh_2004], [Kalnins and Mayer 2004][research_kalnins_mayer_2004], [Che and Chung 1999][research_che_chung_1999], and [Gagnepain and Ivaldi 2002][research_gagnepain_ivaldi_2002]. The framing supplies the specific central result that the specific optimal incentive power falls as the specific project uncertainty rises, because a specific fixed-price instrument applied to a specific poorly specified requirement produces a specific risk premium exceeding the specific efficiency gain. The specific result admits the compact form

$$b^{\ast} = \arg\max_b \left[ \Delta^{\text{effort}}(b) - \tfrac{\gamma}{2} b^2 \sigma^2_{\text{cost}} \right] \qquad \text{with} \qquad \frac{\partial b^{\ast}}{\partial \sigma^2_{\text{cost}}} < 0$$

with the specific optimal incentive power trading the specific effort gain a specific high-powered scheme induces against the specific risk premium the specific provider demands for bearing the specific cost variance. The specific result is directly contrary to the specific policy lesson usually drawn from the specific COTS case, and the article treats the specific tension rather than suppressing it.

The transaction-cost tradition traces from [Coase 1937][research_coase_1937] through [Williamson 1971][research_williamson_1971], [Williamson 1975][research_williamson_1975], [Williamson 1985][book_williamson_1985], [Williamson 2002][research_williamson_2002], [Klein Crawford and Alchian 1978][research_klein_crawford_alchian_1978], [Monteverde and Teece 1982][research_monteverde_teece_1982], [Masten 1984][research_masten_1984], [Grossman and Hart 1986][research_grossman_hart_1986], [Hart and Moore 1990][research_hart_moore_1990], and [Lafontaine and Slade 2007][research_lafontaine_slade_2007]. The framing treats the specific bilateral-monopoly hazard that arises once a specific provider has invested in a specific asset specific to a specific single customer, and it predicts the specific holdup the specific fixed-price instrument would otherwise invite. The specific hazard index admits the compact form

$$h = \frac{V^{\text{asset in intended use}} - V^{\text{asset in next-best use}}}{V^{\text{asset in intended use}}}$$

with the specific hazard rising in the specific asset specificity. The specific SpaceX case exhibits a specific low value of the specific index relative to a specific typical defense programme, because the specific launch vehicle the specific government funding helped develop had specific commercial uses the specific government did not control. The specific low specificity is the specific structural reason the specific arrangement did not produce the specific holdup the framing would otherwise predict. The specific governance-choice rule the tradition supplies admits the compact form

$$\text{instrument} = \begin{cases} \text{market or agreement} & h < \bar{h} \\ \text{hierarchy or cost-reimbursement} & h \geq \bar{h} \end{cases}$$

with the specific threshold determined by the specific contracting hazard the specific asset specificity generates. The specific case sits below the specific threshold, and the specific connection to the generality-forcing condition the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats is direct, because that condition is precisely the condition that keeps $h$ low.

The entrepreneurial-finance tradition traces from [Sahlman 1990][research_sahlman_1990] through [Gompers 1995][research_gompers_1995] Optimal Investment Monitoring and the Staging of Venture Capital, [Lerner 1994][research_lerner_1994_syndication], [Kaplan and Stromberg 2003][research_kaplan_stromberg_2003], [Kaplan and Stromberg 2004][research_kaplan_stromberg_2004], [Gompers and Lerner 2001][book_gompers_lerner_2001], [Metrick and Yasuda 2011][book_metrick_yasuda_2011], and [Lerner 2009][book_lerner_2009] Boulevard of Broken Dreams. The framing treats the specific milestone structure as a specific staged financing and supplies the specific observation that the specific instrument replicates substantially the specific monitoring function a specific venture investor performs, while dispensing with the specific equity claim that ordinarily compensates the specific investor for performing it. The specific asymmetry admits the compact statement

$$\underbrace{\text{monitoring} + \text{staging}}_{\text{both channels}} \; + \; \underbrace{\text{equity claim}}_{\text{private only}} \; \longrightarrow \; \text{cost to venture}$$

with the specific government channel supplying the specific first bracket and omitting the specific second. The specific omission is the specific whole of the non-dilutive property expressed in the specific vocabulary of the specific tradition. The specific government-programme evaluation literature in [Lerner 1996][research_lerner_1996_government_program] and [Kortum and Lerner 2000][research_kortum_lerner_2000] supplies the specific empirical apparatus for assessing whether the specific public capital displaced or complemented the specific private capital.

The public-economics tradition traces from [Nelson 1959][research_nelson_1959] The Simple Economics of Basic Scientific Research and [Arrow 1962][research_arrow_1962] Economic Welfare and the Allocation of Resources for Invention through [Griliches 1979][research_griliches_1979], [Griliches and Lichtenberg 1984][research_griliches_lichtenberg_1984], [Romer 1990][research_romer_1990], and [Aghion and Howitt 1992][research_aghion_howitt_1992]. The framing supplies the specific rationale for the specific public expenditure, resting on the specific gap between the specific private and the specific social return that a specific appropriability failure creates. The specific gap admits the compact form

$$\Delta = r^{\text{social}} - r^{\text{private}} > 0$$

with the specific public intervention warranted where the specific gap is large and the specific private investment consequently below the specific socially optimal level. The specific optimal subsidy under the specific framing satisfies

$$s^{\ast} = \frac{r^{\text{social}} - r^{\text{private}}}{r^{\text{social}}}$$

giving the specific fraction of the specific investment the specific public should bear. The specific expression is the specific formal answer to the specific question of how large a specific cost share the specific instrument should require, and the specific COTS requirement was set by negotiation rather than by any specific such calculation.

The public-private-partnership tradition traces from [Grimsey and Lewis 2004][book_grimsey_lewis_2004] Public Private Partnerships, [Osborne 2000][book_osborne_2000], [Yescombe 2007][book_yescombe_2007], [Hodge and Greve 2007][research_hodge_greve_2007], [Bovaird 2004][research_bovaird_2004], and [Vining and Weimer 2005][research_vining_weimer_2005]. The framing situates the specific instrument within the specific broader family of specific hybrid arrangements and supplies the specific comparative record against which the specific COTS outcome should be assessed, which is substantially less favorable than the specific COTS advocacy literature suggests. The specific risk-allocation principle the tradition states is that each specific risk should be borne by the specific party best able to manage it, admitting the compact form

$$\text{assign risk } k \text{ to } \arg\min_{i} \; c_i(k)$$

with $c_i(k)$ the specific cost to the specific party $i$ of bearing the specific risk $k$. The specific principle recommends assigning the specific technical-execution risk to the specific provider and the specific requirement-definition risk to the specific agency, which is substantially the specific allocation the specific COTS instrument achieved and substantially not the specific allocation a specific fixed-price instrument on an agency-specified requirement achieves.

The mission-oriented and developmental-state tradition traces from [Mazzucato 2013][book_mazzucato_2013] The Entrepreneurial State, [Mazzucato 2021][book_mazzucato_2021] Mission Economy, [Ruttan 2006][book_ruttan_2006] Is War Necessary for Economic Growth, [Weiss 2014][book_weiss_2014] America Inc, [Hartley 2017][book_hartley_2017] The Economics of Arms, [Block 2008][research_block_2008], [Weiss and Thurbon 2021][research_weiss_thurbon_2021], [Johnson 1982][book_johnson_1982], [Amsden 1989][book_amsden_1989], [Wade 1990][book_wade_1990], and [Evans 1995][book_evans_1995] Embedded Autonomy. The framing treats the specific arrangement as a specific instance of specific state-directed development operating through specific procurement rather than through specific ownership or specific directed credit, and it supplies the specific comparative frame within which the specific United States instrument differs from the specific East Asian instruments principally in its specific indirection. The specific instrument set admits compact enumeration by the specific channel through which the specific state acts

$$\mathcal{I} = \left\{ \text{ownership}, \; \text{directed credit}, \; \text{tariff}, \; \text{subsidy}, \; \text{procurement} \right\}$$

with the specific United States arrangement operating substantially through the specific last element alone while the specific East Asian arrangements operated across several. The specific narrowness of the specific channel is what permits the specific arrangement to be described domestically as a specific market mechanism rather than as a specific industrial policy.

The defense-industrial and rent-seeking tradition traces from [Melman 1970][book_melman_1970] Pentagon Capitalism, [Fallows 1981][book_fallows_1981] National Defense, [Hunter 2016][book_hunter_2016] Creating Strategic Value, [Kaplan 1991][book_kaplan_1991] The Wizards of Armageddon, [Buchanan and Tullock 1962][book_buchanan_tullock_1962], [Stigler 1971][research_stigler_1971], and [Krueger 1974][research_krueger_1974]. The framing treats the specific arrangement as a specific transfer to a specific concentrated private interest and supplies the specific skeptical reading the article treats in the Alternative Analytical Frameworks section. The specific concentration the specific framing tracks admits the compact form

$$H^{\text{provider}} = \sum_j s_j^2 \qquad \text{with} \qquad s_j = \frac{\text{awards to provider } j}{\text{total awards}}$$

with the specific index falling across the specific 2006 through 2015 period as the specific entrant took share from the specific incumbent, and rising thereafter as the specific entrant consolidated. The specific non-monotonicity is the specific quantitative form of the specific policy question the article raises in the Contemporary Comparative Landscape section.

The innovation-policy and programme-evaluation tradition traces from [Bonvillian 2018][research_bonvillian_2018] on the specific DARPA institutional model, the specific [Heilmeier Catechism][ref_heilmeier_catechism] as the specific programme-selection instrument, [Freeman 1987][book_freeman_1987], [Lundvall 1992][book_lundvall_1992], [Nelson 1993][book_nelson_1993], and [Mowery and Rosenberg 1998][book_mowery_rosenberg_1998]. The specific selection discipline the specific tradition supplies admits statement as a specific screening condition applied before any specific award

$$\text{fund} \iff \left[ \text{objective specifiable} \right] \wedge \left[ \text{current practice inadequate} \right] \wedge \left[ \text{success testable} \right] \wedge \left[ \text{consequence material} \right]$$

with the specific conjunction required. The framing supplies the specific comparative set of specific public instruments against which the specific Space Act Agreement should be located.

The systems-engineering tradition traces from [Blanchard and Fabrycky 2011][book_blanchard_fabrycky_2011] Systems Engineering and Analysis and [Buede 2009][book_buede_2009] The Engineering Design of Systems through [Suh 2001][book_suh_2001] Axiomatic Design, [Maier 1998][research_maier_1998] Architecting Principles for Systems-of-Systems, [Sage and Cuppan 2001][research_sage_cuppan_2001], the specific [INCOSE Systems Engineering Handbook][ref_incose_handbook], and the specific [NASA Systems Engineering Handbook][ref_nasa_se_handbook]. The framing supplies the specific apparatus for the specific question the milestone decomposition poses, which is how a specific development is partitioned into specific increments that are separately verifiable. The specific partition problem is a specific systems-architecture problem before it is a specific contracting problem, and the specific X-33 comparison the article develops turns entirely on it.

The organizational-learning tradition traces from [March and Simon 1958][book_march_simon_1958] Organizations and [Cyert and March 1963][book_cyert_march_1963] A Behavioral Theory of the Firm through [Argyris and Schon 1978][book_argyris_schon_1978] Organizational Learning, [Levitt and March 1988][research_levitt_march_1988], [Huber 1991][research_huber_1991], [March 1991][research_march_1991], [Nonaka 1994][research_nonaka_1994], [Nonaka and Takeuchi 1995][book_nonaka_takeuchi_1995] The Knowledge-Creating Company, [Senge 1990][book_senge_1990] The Fifth Discipline, [Cohen and Levinthal 1990][research_cohen_levinthal_1990], [Kogut and Zander 1992][research_kogut_zander_1992], [Grant 1996][research_grant_1996], [Argote and Ingram 2000][research_argote_ingram_2000], and [Argote and Miron-Spektor 2011][research_argote_miron_spektor_2011]. The framing applies to the specific agency rather than to the specific provider and supplies the specific account of how a specific programme office accumulates the specific evaluative capability the preceding section identifies as the specific binding constraint.

The learning-curve tradition traces from [Wright 1936][research_wright_1936] Factors Affecting the Cost of Airplanes through [Alchian 1963][research_alchian_1963] Reliability of Progress Curves, [Rapping 1965][research_rapping_1965], [Argote and Epple 1990][research_argote_epple_1990], [Argote 1999][book_argote_1999] Organizational Learning, [Adler and Clark 1991][research_adler_clark_1991], [Lieberman 1984][research_lieberman_1984], and [Dutton and Thomas 1984][research_dutton_thomas_1984]. The framing bears on the specific counterfactual cost estimate the article treats as contested, because the specific parametric models the specific estimate employs are calibrated on a specific historical experience base whose specific learning rates may not transfer to a specific different production organization. The specific transfer question admits the compact statement

$$b^{\text{historical}} \stackrel{?}{=} b^{\text{provider}}$$

with the specific estimate assuming equality and the specific case being one in which the specific production organization differed substantially from the specific calibration sample.

The institutional-economics tradition traces from [North 1990][book_north_1990] Institutions Institutional Change and Economic Performance through [Ostrom 1990][book_ostrom_1990] Governing the Commons, [Greif 2006][book_grief_2006] Institutions and the Path to the Modern Economy, and [Acemoglu and Robinson 2012][book_acemoglu_robinson_2012] Why Nations Fail. The framing situates the specific instrument as one specific rule within a specific broader institutional configuration and supplies the specific caution that a specific rule transplanted without its specific supporting institutions does not reproduce its specific effects.

The reliability and mission-assurance tradition traces from [Perrow 1984][book_perrow_1984] Normal Accidents through [Vaughan 1996][book_vaughan_1996] The Challenger Launch Decision, [Weick and Sutcliffe 2007][book_weick_sutcliffe_2007] Managing the Unexpected, [O'Connor and Kleyner 2012][book_oconnor_kleyner_2012] Practical Reliability Engineering, [Musa 1998][book_musa_1998] Software Reliability Engineering, [Duane 1964][research_duane_1964], and the specific [NASA reliability and mission-assurance standards][ref_nasa_std_8709_22]. The framing supplies the specific content of the specific mission-assurance concessions the economic-property section identifies as part of the specific cost of the specific channel, and the specific [Columbia Accident Investigation Board report][ref_caib_report_2003] and [Rogers Commission report][ref_rogers_commission_1986] supply the specific institutional history from which the specific requirements derive.

The industrial-organization tradition traces from [Bain 1968][book_bain_1968] Industrial Organization through [Scherer and Ross 1990][book_scherer_ross_1990] Industrial Market Structure and Economic Performance, [Tirole 1988][book_tirole_1988] The Theory of Industrial Organization, [Porter 1980][book_porter_1980] Competitive Strategy, [Porter 1985][book_porter_1985] Competitive Advantage, [Baumol 1977][research_baumol_1977], [Kahn 1988][book_kahn_1988] The Economics of Regulation, and [Sharkey 1982][book_sharkey_1982] The Theory of Natural Monopoly. The framing supplies the specific apparatus for the specific concentration question the article raises in its specific closing sections, and the specific antitrust treatments in [Bork 1978][book_bork_1978], [Posner 2001][book_posner_2001], [Hovenkamp 2005][book_hovenkamp_2005], and [Khan 2017][research_khan_2017] supply the specific normative frame.

The economic-history tradition traces from [Landes 1969][book_landes_1969] The Unbound Prometheus, [Rosenberg 1976][book_rosenberg_1976] Perspectives on Technology, [Rosenberg 1982][book_rosenberg_1982] Inside the Black Box, [Mowery and Rosenberg 1998][book_mowery_rosenberg_1998] Paths of Innovation, [Chandler 1962][book_chandler_1962] Strategy and Structure, [Chandler 1977][book_chandler_1977] The Visible Hand, [Chandler 1990][book_chandler_1990] Scale and Scope, and [Hughes 1983][book_hughes_1983] Networks of Power. The framing supplies the specific long-run comparative record within which the specific arrangement is a specific recent instance of a specific recurring relationship between a specific state and a specific private producer.

## The Space Act Agreement Instrument

The specific legal instrument under which the specific COTS development capital was extended deserves treatment before the specific history, because substantially every distinctive feature of the specific arrangement follows from it and because the specific commentary routinely describes the specific arrangement as a contract when it was not one.

The specific [National Aeronautics and Space Act][ref_nasa_act_1958] confers on the specific agency an authority to enter into specific agreements other than specific contracts, specific grants, and specific cooperative agreements, codified at the specific [51 USC 20113 provisions][ref_51_usc_20113] and described in the specific [NASA partnerships and Space Act Agreements guidance][ref_nasa_partnerships]. The specific authority is the specific civil-agency analogue of the specific other-transaction authority that the specific defense agencies hold at the specific [10 USC 2371b provisions][ref_10_usc_2371b] and that the specific [Department of Defense other-transactions resources][ref_dod_other_transactions] describe. The specific related commercial-space authority appears at the specific [51 USC 51302 provisions][ref_51_usc_51302_saa], and the specific agency's specific internal programme-management framework at the specific [NASA programme and project management requirements][ref_nasa_npr_7120_5f].

The specific consequence of proceeding under the specific authority rather than under the specific [Federal Acquisition Regulation][ref_far_part_15] is that substantially the entire specific regulatory apparatus governing specific federal procurement does not apply. The specific cost-accounting standards do not apply. The specific certified cost-or-pricing-data requirements do not apply. The specific contract-type framework that the specific [Federal Acquisition Regulation Part 16][ref_far_part_16] establishes does not apply, nor do the specific commercial-item procedures at [Part 12][ref_far_part_12] or the specific research-and-development contracting provisions at [Part 35][ref_far_part_35]. The specific intellectual-property allocation is negotiated rather than prescribed, which the specific [Data Rights and Intellectual Property article A164][related_post_a164_patents_trade_secrets] treats in the specific adjacent context. The specific bid-protest jurisdiction is substantially narrower. The specific international framework within which the specific resulting launches operate is unaffected by the specific instrument choice and comprises the specific [United Nations Outer Space Treaty of 1967][ref_un_outer_space_treaty_1967], the specific [Liability Convention of 1972][ref_un_liability_convention_1972], and the specific [Registration Convention of 1976][ref_un_registration_convention_1976], with the specific scholarly treatment in the specific [Journal of Space Law][ref_journal_space_law].

The specific regulatory burden removed admits compact statement as the specific difference in the specific compliance cost a specific provider must bear

$$C^{\text{compliance}}_{\text{FAR}} - C^{\text{compliance}}_{\text{agreement}} > 0$$

with the specific difference constituting a specific fixed entry cost that scales poorly with the specific provider's size. The specific consequences cut in both directions and the article states both. The specific absence of the specific cost-accounting apparatus is what permitted a specific provider without a specific government-compliant accounting system to participate at all, which is the specific barrier that excludes substantially every specific venture-stage firm from specific traditional defense procurement. The specific same absence removes the specific visibility into the specific provider's costs that the specific apparatus exists to supply, so that the specific agency purchasing under the specific instrument cannot determine whether the specific price it pays bears any specific relation to the specific cost incurred.

The specific instrument's specific defining operational feature is that it is a specific agreement rather than a specific procurement, so that the specific agency is not purchasing a specific deliverable but is contributing to a specific jointly pursued objective. The specific distinction admits the compact statement

$$\text{procurement} \; : \; \text{agency receives title to a deliverable} \qquad \text{against} \qquad \text{agreement} \; : \; \text{agency receives a demonstrated capability in the market}$$

with the specific second producing no specific asset the specific agency owns. The specific residual-claim structure admits the compact statement

$$\text{title}^{\text{agency}} = \varnothing \qquad \text{while} \qquad \text{capability}^{\text{market}} > 0$$

with the specific agency holding no specific asset and the specific market gaining a specific capability. The specific structure is the specific reason the specific capability the specific funding produced remained available for the specific commercial and specific defense applications that the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] documents, rather than becoming a specific government asset subject to specific government disposition.

## COTS Round One 2006 through 2008

The specific Commercial Orbital Transportation Services programme was announced in the specific January 2006 period and the specific round-one awards were made in the specific August 2006 period. The specific record appears in the specific [NASA commercial space documentation][ref_nasa_cots_solicitation_2006] and the specific [NASA COTS programme literature][ref_nasa_cots_report].

The specific round-one awards went to two providers. The specific SpaceX award was approximately 278 million dollars against a specific milestone schedule covering the specific Falcon 9 launch vehicle and the specific Dragon spacecraft. The specific Rocketplane Kistler award was approximately 207 million dollars against a specific milestone schedule covering the specific K-1 vehicle. The specific two-provider structure was itself a specific design choice with a specific analytical rationale. The specific probability that at least one specific provider succeeds under specific independent execution risk is

$$P(\text{at least one succeeds}) = 1 - \prod_{j} \left( 1 - p_j \right)$$

which exceeds the specific single-provider probability at a specific cost equal to the specific sum of the specific awards. The specific structure is the specific same parallel-track logic the [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] treats, applied by the specific payer across specific providers rather than by a specific venture across specific lines. The specific figures are reported in the specific [NASA COTS programme history of 2011][ref_nasa_cots_2011] and the specific [NASA COTS programme literature][ref_nasa_cots_report], and are among the specific few quantities in this series that are directly documented rather than reconstructed.

The specific structural features of the specific round-one awards that bear on the capital-formation question are four. The specific awards were milestone-based rather than cost-reimbursed. The specific awards required a specific private cost share. The specific awards conveyed no specific equity and no specific governance rights. The specific awards were terminable at the specific agency's discretion upon a specific milestone failure without a specific termination-for-convenience settlement of the specific kind a specific Federal Acquisition Regulation contract would require.

The specific four features admit compact statement as the specific instrument's specific parameter vector

$$\left( b, \; \alpha, \; \Delta e, \; S \right) = \left( 1, \; \alpha > 0, \; 0, \; 0 \right)$$

comprising the specific unit incentive power, the specific positive cost share, the specific zero dilution, and the specific zero termination settlement. The specific fourth feature is the specific one that makes the specific instrument work and is the specific one most often omitted from the specific summaries. A specific agency that must pay a specific settlement to discontinue a specific failing programme faces a specific option value in continuation that a specific agency facing no specific settlement does not. The specific difference admits the compact statement

$$V^{\text{continue}} - V^{\text{terminate}} = \left[ \text{expected completion value} \right] - \left[ - S \right] \qquad \text{with} \qquad S = 0 \text{ under the agreement}$$

with the specific settlement term vanishing under the specific instrument, which lowers the specific threshold at which the specific agency will in fact terminate. The specific Rocketplane Kistler case demonstrates the specific mechanism operating.

## The Rocketplane Kistler Termination

The specific Rocketplane Kistler agreement was terminated in the specific 2007 period after the specific provider failed to satisfy a specific financing milestone requiring it to raise a specific private capital sum. The specific termination is recorded in the specific [NASA news releases][ref_nasa_news] and treated in the specific programme evaluations at the specific [GAO 2009 COTS evaluation][ref_gao_cots_2009] and the specific [NASA Office of Inspector General 2013 COTS evaluation][ref_nasa_oig_cots_2013].

The specific case is analytically important for three reasons that the specific commentary generally reduces to one.

The specific first and most frequently noted is that the specific instrument permitted a specific rapid termination. The specific agency recovered the specific unobligated balance and re-competed the specific position, awarding it to a specific second provider in the specific 2008 period as the specific [NASA news releases][ref_nasa_news] record. The specific recovery admits the compact statement

$$R^{\text{agency}} = K^{\text{obligated}} - K^{\text{disbursed}} \qquad \text{against} \qquad R^{\text{agency}} = -S \quad \text{under a cost-plus termination}$$

with the specific agency recovering the specific unobligated balance under the specific agreement and paying a specific settlement under the specific contract. A specific comparable failure under a specific cost-plus development contract would have produced a specific extended termination process and a specific settlement.

The specific second and more analytically interesting is that the specific failed milestone was a specific financing milestone rather than a specific technical one. The specific instrument conditioned the specific public capital on the specific provider's ability to raise the specific private capital, which makes the specific public channel and the specific private channel complements rather than substitutes by explicit design. The specific structure admits the compact statement

$$m_j \text{ released} \iff \left[ \text{technical milestone } j \text{ achieved} \right] \wedge \left[ K^{\text{private}} \geq \alpha K^{\text{gov}} \right]$$

with the specific conjunction required. The specific design uses the specific private capital market as a specific external validator of the specific provider's prospects, which economizes on the specific agency's own assessment capability. The specific mechanism is the specific same one the specific SBIR programme employs through its specific Phase II commercialization requirements, which the [Money Behind an SBIR or STTR Award article A140][related_post_a140_sbir_money] treats.

The specific third is that the specific case supplies the specific counterfactual observation the identification problem requires. A specific competitor holding a specific substantially similar award at a specific substantially similar stage attempted the specific private-capital path and failed to complete it. The specific inferential value of the specific observation admits careful statement. Let $A$ denote the specific event that a specific similarly situated firm can complete a specific private raise. The specific observation establishes

$$P(A) < 1 \qquad \text{and not} \qquad P(A \mid \text{SpaceX}) = 0$$

with the specific single failure bounding the specific probability away from certainty without identifying it for any specific other firm. The specific observation does not establish that the specific SpaceX private raise would have failed, and it does establish that the specific private path was not freely available to a specific similarly situated firm in the specific same period.

## COTS Milestone Mechanics and the Non-Dilutive Property

The specific analytical core of this article is the specific observation that the specific COTS payments functioned as development capital and carried no specific claim on the specific firm. The specific section states the specific claim precisely and then states what it does not establish.

The specific SpaceX COTS award grew through specific amendments to approximately 396 million dollars across the specific agreement period. The specific capital was received across the specific 2006 through 2012 interval, which spans the specific period the [series opener][related_post_a281_spacex_framing] identifies as the specific near-death moment and the specific period in which the specific firm's specific private valuation was at its lowest. The specific coincidence is the specific whole of the timing argument, because the specific dilution a specific dollar of capital costs is inversely proportional to the specific valuation at which it is raised

$$\frac{\partial \delta}{\partial V} < 0 \qquad \text{so that} \qquad \delta \Big|_{V \text{ low}} \gg \delta \Big|_{V \text{ high}}$$

with the specific capital arriving precisely when the specific alternative was most expensive.

The specific non-dilutive property admits the compact comparison. The specific approximately 396 million dollars received through the specific channel, had it instead been raised as equity at the specific valuations prevailing across the specific interval, would have required surrendering a specific fraction

$$\delta^{\text{avoided}} = \frac{K^{\text{COTS}}}{V + K^{\text{COTS}}}$$

that is substantial at the specific contemporaneous valuations and that would have compounded against every specific subsequent round. The specific compounding is the specific feature that makes the specific timing decisive. A specific dilution avoided early is a specific dilution avoided in every specific later round, because the specific founder share entering each specific subsequent round is higher than it would otherwise have been. The specific cumulative effect admits the compact form

$$e^{\text{founder}}_N = \left[ e_0 - \delta^{\text{avoided}} \right] \prod_{n=1}^{N} \left( 1 - \delta_n \right) \qquad \text{against} \qquad e_0 \prod_{n=1}^{N} \left( 1 - \delta_n \right)$$

with the specific difference persisting across the specific entire subsequent financing sequence rather than being confined to the specific round it displaced. The specific connection to the [Governance article A287][related_post_a287_spacex_governance] is direct, because the specific control condition that article analyzes depends on the specific founder's specific residual share, and the specific government channel raised the specific share available at every specific subsequent stage.

The specific claim the article does not make deserves equal prominence. The specific analysis does not establish that the specific government capital was necessary, because the specific counterfactual in which the specific firm raised the specific same amount privately at a specific worse price is not obviously infeasible. The specific analysis does not establish that the specific government capital was efficiently deployed, because the specific counterfactual social return on the specific same appropriation directed elsewhere is not estimated. The specific three propositions admit compact separation

$$\underbrace{\text{terms were favorable}}_{\text{established}} \; \not\Rightarrow \; \underbrace{\text{capital was necessary}}_{\text{not established}} \; \not\Rightarrow \; \underbrace{\text{expenditure was efficient}}_{\text{not established}}$$

with only the specific first supported by the specific evidence the article assembles. The specific analysis establishes the specific narrower proposition that the specific capital arrived on specific terms substantially more favorable than the specific alternatives available at the specific time, and that the specific favorable terms compounded.

## The Commercial Resupply Services Transition

The specific transition from the specific development agreement to the specific services contract occurred in the specific December 2008 period with the specific award of the specific Commercial Resupply Services contracts, recorded in the specific [NASA news releases][ref_nasa_news] and treated at length in the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand].

The specific transition changes the specific instrument's character in a way the capital-formation analysis must register. The specific CRS contracts were procurement contracts rather than agreements, and the specific payments were for specific delivered services rather than against specific development milestones. The specific channel therefore ceased to be a specific capital-formation channel and became a specific revenue channel at the specific moment of the specific transition.

The specific analytical consequence is that the specific government-anchor capital-formation leg has a specific bounded duration. The specific leg operated across the specific 2006 through approximately 2012 interval, and thereafter the specific government relationship supplied revenue rather than capital. The specific bounded duration admits the compact statement

$$K^{\text{gov}}(t) \approx \text{constant} \qquad \text{for} \qquad t > t^{\text{transition}}$$

with the specific cumulative government development capital reaching a specific plateau while the specific government revenue continued to grow. The specific two quantities the specific commentary conflates admit compact separation

$$\frac{K^{\text{gov}}}{K^{\text{total}}} \Bigg|_{\text{cumulative, development era}} \qquad \text{against} \qquad \frac{R^{\text{gov}}(t)}{R^{\text{total}}(t)} \Bigg|_{\text{current}}$$

with the specific first a specific historical capital share that is fixed and the specific second a specific current revenue share that has declined as the specific commercial lines grew. The specific distinction matters because the specific commentary that describes the specific firm as government-funded conflates a specific bounded historical capital contribution with a specific continuing commercial relationship, and the specific two have specific different implications for substantially every question the series treats.

The specific subsequent [CRS-2 award][ref_nasa_crs2_press_2016] of the specific 2016 period extended the specific services relationship without reopening the specific capital-formation channel. The specific execution record across the specific two contracts is documented in the specific [NASA Commercial Resupply Services programme overview][ref_nasa_crs_program_overview] and in the specific SpaceX press record covering the specific [Dragon C1 demonstration of 2010][ref_spacex_press_dragon_c1_2010], the specific [CRS-1 mission of 2012][ref_spacex_press_crs1_2012], the specific [CRS-7 loss of 2015][ref_spacex_press_crs7_2015], and the specific [CRS-21 mission of 2020][ref_spacex_press_crs21_2020].

## Commercial Crew and the Fixed-Price Competition

The specific Commercial Crew progression partially reopened the specific capital-formation channel for a specific second capability. The specific programme proceeded through the specific Commercial Crew Development awards of the specific 2010 and 2011 periods, the specific Commercial Crew Integrated Capability awards of the specific 2012 period, and the specific Commercial Crew Transportation Capability awards of the specific September 2014 period. The specific record appears in the specific [NASA Commercial Crew Program documentation][ref_nasa_ccp_documents], the specific [certification record][ref_nasa_ccp_certification], and the specific evaluations at the specific [GAO 2014 Commercial Crew evaluation][ref_gao_2014_commercial_crew], the specific [GAO 2019 evaluation][ref_gao_ccp_2019], the specific [GAO 2020 evaluation][ref_gao_2020_commercial_crew], the specific evaluations in the specific [NASA Office of Inspector General reports database][ref_nasa_oig_reports], and the specific [Congressional Research Service Commercial Crew report][ref_crs_commercial_crew].

The specific early phases were conducted under specific Space Act Agreements and the specific final phase under a specific Federal Acquisition Regulation contract, which reflects a specific deliberate progression from a specific development instrument to a specific procurement instrument as the specific requirement became specifiable. The specific progression is the specific practical answer to the specific mechanism-design result that the specific optimal incentive power falls with the specific uncertainty. The specific staged instrument choice admits the compact statement

$$b^{\ast}(t) = b^{\ast}\!\left( \sigma^2_{\text{cost}}(t) \right) \qquad \text{with} \qquad \sigma^2_{\text{cost}}(t) \text{ declining in } t$$

with the specific instrument tightening as the specific requirement becomes specifiable. The specific arrangement applies the specific high-powered instrument at the specific stage where the specific provider knows more than the specific agency and the specific specified instrument at the specific stage where the specific requirement is stable.

The specific CCtCap awards were approximately 4.2 billion dollars to one specific provider and approximately 2.6 billion dollars to the specific second, recorded in the specific [NASA Commercial Crew certification record][ref_nasa_ccp_certification]. The specific award structure is a specific fixed-price arrangement with specific milestone payments, so the specific incentive-power parameter sits near unity. The specific dual-award structure preserved the specific parallel-track property at the specific operational stage, and the specific price differential between the specific two awards admits the compact expression

$$\frac{P^{\text{high}} - P^{\text{low}}}{P^{\text{low}}} \approx 0.6$$

which the specific agency accepted in exchange for the specific redundancy the specific second provider supplied. The specific subsequent execution record establishes that the specific redundancy was not decorative.

## The Boeing Comparison and Risk Transfer

The specific comparison between the specific two Commercial Crew providers constitutes the specific clearest available natural experiment in the specific procurement literature, because the specific two providers executed a specific substantially identical requirement under a specific substantially identical instrument across a specific identical period.

The specific outcome differed substantially. The specific one provider achieved the specific uncrewed demonstration flight of the specific [Demo-1 mission in March 2019][ref_spacex_press_demo1_2019], the specific crewed demonstration flight of the specific [Demo-2 mission in May 2020][ref_spacex_press_dm2_2020], and the specific first operational rotation of the specific [Crew-1 mission in November 2020][ref_spacex_press_crew1_2020]. The specific other encountered a specific sequence of specific development difficulties including a specific uncrewed flight-test anomaly in the specific December 2019 period, a specific repeat uncrewed flight in the specific 2022 period, and specific propulsion difficulties during the specific crewed flight test of the specific June 2024 period that the specific [Boeing Starliner programme record][ref_boeing_starliner_cft_2024] documents.

The specific capital-formation significance is not the specific schedule difference but the specific cost incidence. Under the specific fixed-price instrument the specific overrun was borne by the specific provider and recorded as a specific charge against its specific earnings, rather than being reimbursed. The specific reported cumulative charges are substantial and are documented in the specific provider's specific public filings accessible through the specific [Securities and Exchange Commission EDGAR][ref_sec_edgar] system and summarized in the specific [Boeing press releases][ref_boeing_press]. The specific transfer admits the compact statement

$$L^{\text{public}} = (1 - b) \cdot \left( C^{\text{actual}} - C^{\text{estimated}} \right)^{+} \approx 0 \qquad \text{at} \qquad b \approx 1$$

with the specific public exposure approaching zero. The specific incidence comparison across the specific two instrument classes admits the compact tabulation

$$\left( L^{\text{public}}, \; L^{\text{provider}} \right) = \begin{cases} \left( 0, \; \Delta C \right) & \text{fixed price} \\ \left( \Delta C, \; 0 \right) & \text{cost reimbursement} \end{cases}$$

with the specific overrun falling entirely on one specific party or the specific other. The specific comparison against the specific cost-plus counterfactual that the article treats below is the specific substantive demonstration that the specific instrument accomplished the specific risk transfer it was designed to accomplish.

The specific qualification the article records is that the specific risk transfer is only credible where the specific provider can in fact absorb the specific loss. A specific fixed-price instrument imposed on a specific provider without the specific balance sheet to absorb a specific overrun does not transfer the specific risk. It converts it into a specific completion risk borne by the specific agency in a specific different form. The specific credibility condition admits the compact statement

$$\text{risk transferred} \iff \Delta C \leq W^{\text{provider}}$$

with $W^{\text{provider}}$ the specific provider's specific capacity to absorb the specific loss, and with the specific transfer failing whenever the specific overrun exceeds it. The specific condition is the specific failure mode the specific defense-procurement literature documents extensively and which the specific Rocketplane Kistler case illustrates in the specific development setting.

## National Security Space Launch Certification

The specific defense channel operated on a specific different principle from the specific civil channel and deserves separate treatment. The specific National Security Space Launch programme, formerly the specific Evolved Expendable Launch Vehicle programme, purchases specific launch services rather than funding specific development, and the specific channel therefore supplied substantially revenue rather than capital across most of its specific history. The specific record appears in the specific [Space Force National Security Space Launch][ref_space_force_nssl] framework documentation, the specific [Phase 1A award record][ref_space_force_nssl_phase1a_2018], the specific [Phase 2 award record][ref_space_force_nssl_phase2_2020], the specific [Phase 3 Lane 2 coverage][ref_spacenews_nssl_phase3], the specific [GAO 2023 National Security Space Launch evaluation][ref_gao_nssl_2023], and the specific [Space Force news][ref_space_force_news] and [Department of Defense contract announcements][ref_dod_contracts].

The specific launch infrastructure on which the specific certified missions depend is itself partly a specific government asset made available on specific negotiated terms, comprising the specific [Kennedy Space Center Launch Complex 39A arrangement][ref_ksc_lc39a_lease], the specific [Vandenberg environmental record][ref_vandenberg_slc4e_ea], and in the specific earliest period the specific [Kwajalein Atoll range documentation][ref_kwajalein_atoll_documentation]. The specific licensing regime under which the specific operations proceed is the specific [FAA commercial space transportation regulations][ref_faa_ast_regulations] and the specific [Part 450 licensing requirements][ref_faa_ast_licensing_regs_450], with the specific current authorizations recorded in the specific [FAA current launch licenses][ref_faa_launch_licenses_current]. The specific capital-formation content of the specific defense channel lies in a specific different place. The specific certification process itself is a specific substantial fixed investment that the specific provider must make and that the specific programme partially funds, and the specific certification once obtained is a specific durable asset that raises the specific provider's value independently of any specific specific mission awarded. The specific certification therefore functions as a specific capital contribution in kind rather than in cash, admitting the compact statement

$$\Delta V^{\text{certification}} = \sum_{t} \frac{p^{\text{award}}(t) \cdot \pi^{\text{margin}}}{(1+\rho)^t} \; - \; C^{\text{certification}}$$

with the specific certification's value equal to the specific discounted expected award stream it makes accessible net of the specific investment required to obtain it. The specific certification therefore behaves as a specific barrier whose specific height is symmetric in construction and asymmetric in effect, admitting the compact statement

$$C^{\text{certification}} \text{ identical across entrants} \qquad \text{while} \qquad \frac{C^{\text{certification}}}{R^{\text{existing}}} \text{ differs by orders of magnitude}$$

with the specific fixed cost trivial for a specific incumbent holding a specific large existing revenue base and prohibitive for a specific entrant holding none.

The specific Phase 2 award of the specific 2020 period allocated the specific mission set between two providers on a specific announced split, and the specific Phase 3 structure of the specific 2024 period established a specific two-lane arrangement admitting a specific broader provider set into the specific less demanding lane. The specific progression admits compact statement through the specific provider count admitted to the specific competed mission set

$$n^{\text{providers}} \; : \; 1 \longrightarrow 2 \longrightarrow 3+$$

across the specific pre-2015, specific Phase 2, and specific Phase 3 periods respectively. The specific progression from a specific single-provider arrangement through a specific duopoly to a specific multi-provider structure across the specific two decades is the specific competitive outcome the specific programme reforms were intended to produce.

## The Litigation and Entry Path

The specific entry path into the specific defense channel is not adequately described as a specific certification process, because the specific entry was contested and the specific contest was resolved partly through specific litigation.

The specific provider filed suit against the specific Air Force in the specific 2014 period challenging a specific sole-source block award to the specific incumbent. The specific matter was resolved by a specific settlement in the specific 2015 period, and the specific certification followed later that specific year. The specific bid-protest and specific claims apparatus that the specific [GAO bid-protest function][ref_gao_bid_protest] and the specific [United States Court of Federal Claims][ref_uscfc] administer is the specific institutional channel through which the specific contest proceeded. The specific decision to pursue it admits the compact statement

$$\text{litigate} \iff p^{\text{prevail}} \cdot V^{\text{channel access}} > C^{\text{legal}} + C^{\text{relationship}}$$

with the specific second cost term capturing the specific damage a specific contest inflicts on a specific ongoing customer relationship, which is the specific term that deters substantially every specific incumbent supplier from bringing one.

The specific capital-formation significance is that the specific entry into the specific channel required a specific investment in specific legal and specific political action distinct from the specific technical investment, and that the specific investment was available to a specific firm holding a specific patient private capital base and would not have been available to a specific firm dependent on specific near-term contract revenue. The specific dependency admits the compact statement

$$K^{\text{gov}} \; \text{accessible} \; \Leftarrow \; \text{legal contest} \; \Leftarrow \; K^{\text{private, patient}}$$

with the specific government channel's specific accessibility conditioned on a specific prior private expenditure. The specific observation connects the specific three capital-formation legs, because the specific patient private leg that the Patient-Private Capital-Formation Leg article A290 will treat financed the specific contest that opened the specific government channel.

## Starshield and the Classified Anchor

The specific Starshield business that the specific [SpaceX Starshield documentation][ref_spacex_starshield] describes at the specific unclassified level and that the specific [Reuters 2024 investigation][research_reuters_starshield_2024] and the specific [New York Times 2024 coverage][ref_nyt_starshield_2024] reconstructed represents a specific further stage of the specific government relationship in which the specific government is purchasing a specific capability the specific firm developed substantially on its own account.

The specific direction of the specific capital flow has therefore reversed relative to the specific COTS period. In the specific earlier period the specific government supplied capital to build a specific capability that did not exist. In the specific later period the specific firm supplied a specific capability built with specific commercial capital and the specific government purchased access to it. The specific reversal admits the compact statement

$$\text{sign}\!\left( \frac{\partial K^{\text{firm}}}{\partial \, \text{government relationship}} \right) \; : \; + \text{ in the development period}, \; - \text{ in the current period}$$

with the specific firm now investing ahead of the specific government requirement rather than the reverse. The specific reversal admits the compact statement as a specific change in the specific temporal ordering

$$t^{\text{gov capital}} < t^{\text{capability}} \qquad \text{becomes} \qquad t^{\text{capability}} < t^{\text{gov purchase}}$$

with the specific ordering inverted between the specific two eras. The specific reversal is the specific completion of the specific capital-formation leg and the specific reason the article treats the specific leg as historically bounded.

## SBIR Phase III Sole-Source Authority as Structural Analogue

The specific Small Business Innovation Research programme supplies the specific closest statutory analogue to the specific structural pattern the specific COTS-to-CRS sequence exhibits, and the specific analogy is instructive precisely because the specific statutory mechanism is explicit where the specific COTS mechanism was not.

The specific programme operates under the specific [statutory authority at 15 USC 638][ref_sbir_statute_15usc638] and the specific [Small Business Administration policy directive][ref_sba_sbir_policy_directive] documented through the specific [SBIR programme portal][ref_sbir_gov]. The specific programme is treated comprehensively in the [Introduction to the SBIR and STTR Programs article A132][related_post_a132_sbir_intro], and the specific Phase III mechanism in the [Phase III and the Valley of Death article A138][related_post_a138_sbir_phase3], with the specific funding mechanics in the [Money Behind an SBIR or STTR Award article A140][related_post_a140_sbir_money].

The specific Phase III authority permits a specific agency to award a specific follow-on contract deriving from specific earlier programme work without a specific further competition, and without a specific dollar limit. The specific authority is the specific statutory recognition of a specific structural fact, namely that a specific development award creates a specific provider who is thereafter uniquely positioned, and that requiring a specific fresh competition at the specific follow-on stage would either produce a specific foregone conclusion or would transfer the specific benefit of the specific development investment to a specific competitor who did not make it.

The specific structural pattern admits the compact statement

$$\text{development award} \longrightarrow \text{capability} \longrightarrow \text{position} \longrightarrow \text{follow-on award}$$

with the specific chain operating whether or not a specific statute names it. The specific competitive consequence admits the compact statement

$$P\!\left( \text{win follow-on} \mid \text{received development award} \right) \gg P\!\left( \text{win follow-on} \right)$$

with the specific conditional probability substantially exceeding the specific unconditional one irrespective of whether the specific follow-on is formally competed. The specific COTS-to-CRS sequence was formally competed and the specific SBIR Phase III sequence is formally exempt from competition, and the specific two nonetheless produce a specific substantially similar outcome, because the specific competition at the specific follow-on stage is conducted among providers whose specific relative positions the specific prior development stage established.

The specific analytical value of the specific analogy is that it identifies what a specific government-anchor capital-formation leg actually transfers. It does not principally transfer money. It transfers position, and the specific money is the specific mechanism by which the specific position is created. A specific venture evaluating the specific leg should therefore assess the specific follow-on position the specific development award would establish rather than the specific development award's specific magnitude, The specific valuation the specific assessment requires admits the compact form

$$V^{\text{award}} = \underbrace{K^{\text{development}}}_{\text{visible}} + \underbrace{P\!\left( \text{follow-on} \right) \cdot V^{\text{follow-on position}}}_{\text{usually dominant}}$$

with the specific second term ordinarily exceeding the specific first by a specific substantial multiple. This is the specific assessment the specific SBIR practitioner literature the specific series treats makes explicitly.

## The Agency-Side Capability Requirement

The article to this point has treated the specific instrument as though its specific properties inhered in the specific document. They do not. Every specific property the preceding sections attribute to the specific instrument requires a specific agency capable of exercising it, and the specific capability is neither automatic nor evenly distributed. The specific section states the requirement because the specific advocacy literature that recommends extending the specific instrument to specific other domains substantially omits it.

The specific instrument requires the specific agency to perform four functions that a specific cost-reimbursement arrangement does not require. The specific agency must specify a specific milestone that is verifiable without access to the specific provider's specific cost records. The specific agency must verify the specific milestone when the specific provider claims it. The specific agency must decline to pay when the specific milestone is not met. And the specific agency must terminate when the specific pattern of failures warrants it, against the specific institutional pressure that every specific programme generates in favor of continuation.

The specific fourth function is the specific one that fails most often. The specific termination decision admits the compact statement

$$\text{terminate} \iff E\!\left[ V^{\text{completion}} \mid \mathcal{F}_t \right] < \sum_{j > J(t)} m_j + C^{\text{political}}$$

with $C^{\text{political}}$ the specific institutional cost the specific deciding official bears personally and the specific benefit accruing diffusely. The specific asymmetry between a specific concentrated cost and a specific diffuse benefit is the specific standard public-choice account of why specific programmes persist, and the specific Space Act Agreement reduces the specific first term in the specific inequality without touching the specific second.

The specific capability the specific functions jointly require is what the specific developmental-state literature terms embedded autonomy. The specific concept that [Evans 1995][book_evans_1995] Embedded Autonomy develops requires a specific agency close enough to the specific industry to evaluate a specific technical claim and distant enough from it to decline one. The specific two requirements pull against each other, and the specific balance admits the compact statement

$$\Sigma^{\text{agency}} = \min\left\{ \text{technical proximity}, \; \text{institutional distance} \right\}$$

with the specific capability governed by whichever specific element is weaker rather than by their specific sum. A specific agency with specific deep technical knowledge and specific close industry ties evaluates well and cannot refuse. A specific agency with specific strong independence and specific thin technical knowledge refuses arbitrarily. The specific comparative literature in [Johnson 1982][book_johnson_1982] MITI and the Japanese Miracle, [Amsden 1989][book_amsden_1989] Asia's Next Giant, [Wade 1990][book_wade_1990] Governing the Market, [Woo-Cumings 1999][book_woo_cumings_1999] The Developmental State, and [Chang 2002][book_chang_2002] Kicking Away the Ladder documents the specific institutional arrangements under which specific other states have attempted the specific balance.

The specific agency-side literature on the specific particular agency is unusually candid and is worth citing directly rather than through the specific procurement abstraction. The treatments in [McCurdy 1994][book_mccurdy_1994] Inside NASA, [Handberg 1994][book_handberg_1994] Reinventing NASA, [Launius 1994][book_launius_1994] NASA A History of the United States Civil Space Program, [McDougall 1985][book_mcdougall_1985] The Heavens and the Earth, [Hargrove 1994][book_hargrove_1994] Prisoners of Myth, [Selznick 1949][book_selznick_1949] TVA and the Grass Roots, and [Klerkx 2004][book_klerkx_2004] Lost in Space document the specific organizational culture and the specific goal-displacement hazard within which the specific programme office operated. The specific programme-office model the specific [DARPA institutional treatment][research_bonvillian_2018] describes and the specific [Heilmeier Catechism][ref_heilmeier_catechism] states supplies the specific comparative benchmark for a specific agency-side selection capability.

The specific personnel dimension is the specific one the specific documentary record covers least well and the specific participant accounts cover best. The specific programme required a specific small number of specific individuals willing to accept a specific personal career risk in exchange for a specific institutional outcome, which is a specific resource no specific appropriation creates. The specific accounts in [Berger 2021][book_berger_2021] Liftoff, [Berger 2024][book_berger_2024] Reentry, [Davenport 2018][book_davenport_2018] The Space Barons, and [Fernholz 2018][book_fernholz_2018] Rocket Billionaires document the specific individuals on both sides of the specific transaction.

The specific implication for the specific policy question is direct and is the specific reason the section exists. A specific jurisdiction that adopts the specific instrument without the specific agency-side capability obtains the specific reduced oversight without the specific compensating selection discipline, which is strictly worse than the specific arrangement it replaced. The specific instrument is not a specific substitute for a specific capable agency. It is a specific tool that a specific capable agency can use and that a specific incapable one should not.

## The Cost-Plus Counterfactual

The specific counterfactual against which the specific instrument should be assessed is not a specific absence of government funding but the specific alternative instrument the specific same agency employed contemporaneously for a specific comparable objective.

The specific Constellation programme and the specific Space Launch System that the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats as generality-forcing negation cases were procured under specific cost-reimbursement arrangements with specific incentive-power parameters near zero. The specific record appears in the specific [NASA Constellation Program documentation][ref_nasa_constellation], the specific [NASA Space Launch System program documentation][ref_nasa_sls_program], the specific [NASA Authorization Act of 2010][ref_nasa_auth_2010], the specific [NASA Office of Inspector General 2022 Artemis management evaluation][ref_nasa_oig_artemis_2022], and the specific [Congressional Research Service 2022 Artemis Program report][ref_crs_artemis_2022].

The specific comparison admits compact statement through the specific instrument parameter vector the COTS section introduces, evaluated for the specific two classes

$$\left( b, \; \alpha, \; \Delta e, \; S \right)^{\text{agreement}} = (1, \alpha, 0, 0) \qquad \text{against} \qquad \left( b, \; \alpha, \; \Delta e, \; S \right)^{\text{cost-plus}} \approx (0, 0, 0, S > 0)$$

with the specific two classes differing on three of the specific four parameters. The specific comparison admits statement along three dimensions. The specific cost incidence differs, with the specific overrun borne publicly under the specific cost-plus instrument and privately under the specific fixed-price instrument. The specific asset disposition differs, with the specific cost-plus instrument producing a specific vehicle the specific agency directs and the specific agreement producing a specific capability in the specific market. The specific termination cost differs, with the specific cost-plus programme carrying a specific constituency and a specific settlement exposure that the specific agreement does not.

The specific comparison is nonetheless confounded in a specific way the specific advocacy literature generally omits. The specific two instruments were applied to specific different requirements. The specific cost-plus programmes pursued a specific crewed beyond-low-Earth-orbit capability with no specific commercial market, and the specific fixed-price instruments pursued a specific low-Earth-orbit logistics capability with a specific plausible commercial market. The specific confound admits the compact statement that the specific observed comparison estimates

$$\left[ \text{outcome}^{\text{agreement}} - \text{outcome}^{\text{cost-plus}} \right] = \underbrace{\Delta^{\text{instrument}}}_{\text{sought}} + \underbrace{\Delta^{\text{requirement}}}_{\text{confound}}$$

with the specific second term unidentified. The specific mechanism-design result that the specific optimal incentive power falls with the specific uncertainty and rises with the specific specifiability implies that the specific instrument choice may have been appropriate in both specific cases. The specific article records the specific confound rather than reporting the specific comparison as a specific clean demonstration.

The specific cost comparison the specific agency itself published estimated that a specific traditional cost-plus development of the specific launch vehicle would have cost several times the specific amount actually expended. The specific estimate is a specific model output produced using a specific parametric cost model calibrated on specific historical programmes, and it is treated in this article as a specific contested reconstruction rather than as a specific measurement. The specific estimate's specific construction admits the compact statement

$$\hat{C}^{\text{counterfactual}} = f\!\left( \text{mass}, \; \text{complexity}, \; \text{heritage}; \; \hat{\beta}^{\text{historical}} \right)$$

with the specific parameters calibrated on a specific historical programme set drawn substantially from the specific cost-plus regime whose specific costs the specific estimate is being used to criticize. The specific circularity is not fatal and is not nothing. The specific direction of the specific estimate is consistent with the specific broader procurement literature and the specific magnitude is not independently verifiable.

## Deep Historical Comparative Precedents

The government-anchor capital-formation mechanic admits comparison with specific deep historical precedents in which a specific state supplied specific development capital to a specific private party on specific terms other than ownership.

The specific armory and specific interchangeable-parts precedent that the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats supplies the specific earliest systematic American instance. The specific War Department advanced specific funds against specific delivery schedules to specific private contractors including the specific Whitney and specific Colt enterprises, and the specific advances functioned as specific working capital that the specific contemporary capital markets would not have supplied. The [Hounshell 1984][book_hounshell_1984] From the American System to Mass Production and [Hosley 1996][book_hosley_1996] Colt treatments document the specific arrangements. The specific advance admits the compact characterization as a specific negative working-capital position supplied by the specific customer

$$\text{WC}^{\text{contractor}} = \text{receivables} + \text{inventory} - \text{advances} < 0$$

with the specific customer financing the specific production cycle. The specific structure is the specific oldest form the government-anchor capital-formation leg takes and it remains the specific most common.

The specific air-mail contracts of the specific 1920s and 1930s supply the specific closest transportation-sector analogue. The specific Post Office Department contracts supplied a specific revenue floor against which specific private capital could be raised, and the specific subsequent commercial passenger business was built on the specific capability the specific mail contracts sustained. The [Serling 1992][book_serling_1992] Legend and Legacy, [Bilstein 2001][book_bilstein_2001] Flight in America, and [Crouch 2003][book_crouch_2003] Wings treatments document the specific trajectory. The specific structural difference from the specific COTS case is that the specific mail contracts supplied revenue against a specific delivered service from the outset rather than capital against specific development milestones, which places them nearer the specific CRS stage than the specific COTS stage.

The specific wartime production financing of the specific 1940s supplies the specific largest historical instance of specific public capital supplied to specific private producers without specific equity. The specific arrangements comprised specific government-owned contractor-operated facilities, specific advance payments, and specific accelerated amortization, and they produced a specific private industrial capability at a specific public cost with a specific negotiated post-war disposition. The [Hounshell 1984][book_hounshell_1984], [Rhodes 1986][book_rhodes_1986] The Making of the Atomic Bomb, [Groves 1962][book_groves_1962] Now It Can Be Told, and [Hewlett and Anderson 1962][book_hewlett_anderson_1962] The New World treatments document specific portions of the specific arrangement. The specific arrangements admit compact classification by where the specific title rested

$$\left\{ \text{government-owned government-operated}, \; \text{government-owned contractor-operated}, \; \text{contractor-owned} \right\}$$

with the specific middle form dominating and with the specific post-war disposition of the specific government-owned assets constituting a specific distinct policy episode. The specific disposition question that the specific post-war period confronted is the specific same question the specific Space Act Agreement resolves in advance by conveying no specific asset.

The specific integrated-circuit procurement of the specific 1960s supplies the specific instance in which a specific government purchase at a specific price no specific commercial buyer would pay carried a specific industry through the specific interval before a specific commercial market existed. The [Berlin 2005][book_berlin_2005] The Man Behind the Microchip, [Malone 2014][book_malone_2014] The Intel Trinity, [Lecuyer 2006][book_lecuyer_2006] Making Silicon Valley, [Riordan Hoddeson and Kolb 2015][book_riordan_hoddeson_kolb_2015] Tunnel Visions, [Mindell 2008][book_mindell_2008] Digital Apollo, and the specific retrospectives in [Noyce 1976][research_noyce_1976] and [Kilby 1976][research_kilby_1976] document the specific trajectory, and the [Silicon Valley from Defense Contracting article A246][related_post_a246_silicon_valley_defense] treats the specific regional consequence. The specific case is a specific demand-side rather than a specific capital-side instance, which the article notes because the specific two are conflated as frequently in the specific historical literature as in the specific contemporary commentary.

The specific ARPANET and the specific DARPA institutional model supply the specific instance of a specific public funder operating through a specific programme-manager structure with a specific explicit selection discipline. The [Abbate 1999][book_abbate_1999] Inventing the Internet and [Norberg and O'Neill 1996][book_norberg_oneill_1996] Transforming Computer Technology treatments document the specific programme, [Bonvillian 2018][research_bonvillian_2018] documents the specific institutional model, and the specific [Heilmeier Catechism][ref_heilmeier_catechism] states the specific selection instrument. The specific model differs from the specific COTS instrument in that it funds specific research rather than specific capability demonstration and conveys no specific expectation of a specific follow-on procurement.

The specific X-33 and specific reusable-launch-vehicle programmes of the specific 1990s supply the specific negation case within the specific same agency and the specific same domain. The specific programme proceeded under a specific cooperative agreement with a specific cost share, pursued a specific technically ambitious single-vehicle demonstration, and was terminated in the specific 2001 period without producing a specific flying article. The specific record is accessible through the specific [NASA X-33 and reusable launch vehicle literature][ref_ntrs_x33] and the specific [NASA history archives][ref_nasa_history]. The specific case shares the specific cost-share structure with the specific COTS instrument and differs in that the specific milestone schedule was tied to a specific single integrated demonstration rather than to a specific sequence of independently valuable increments, which is the specific decomposability property the [Decomposability article A285][related_post_a285_spacex_decomposability] treats. The specific difference admits the compact statement through the specific milestone count

$$\left| \{ m_j \} \right|^{\text{X-33}} \approx 1 \qquad \text{against} \qquad \left| \{ m_j \} \right|^{\text{COTS}} \gg 1$$

with the specific single integrated demonstration supplying neither the specific payer's intermediate option to discontinue nor the specific provider's intermediate validation. The specific comparison establishes that the specific instrument alone is insufficient and that the specific milestone decomposition is doing substantial work.

The specific transcontinental-railroad land grants and the specific associated federal bond issues of the specific 1860s supply the specific instance in which a specific state supplied capital on specific terms that conveyed a specific asset rather than an equity claim, and in which the specific subsequent disposition of the specific asset became the specific dominant political question. The specific parallel to the specific Space Act Agreement's specific conveyance of no asset is instructive, because the specific agreement resolves in advance the specific question the specific land grants left open. The specific broader institutional treatments in [Chandler 1977][book_chandler_1977] The Visible Hand and [Fligstein 2001][book_fligstein_2001] The Architecture of Markets situate the specific arrangement within the specific development of the specific American corporate form.

The specific Apollo contractor set supplies the specific instance in which a specific state programme funded a specific private industrial capability at a specific scale and under a specific cost-reimbursement instrument, producing a specific capability that substantially did not survive the specific programme. The specific treatments in [Bilstein 1996][book_bilstein_1996] Stages to Saturn, [Murray and Cox 1989][book_murray_cox_1989] Apollo, [Chaikin 2007][book_chaikin_2007] A Man on the Moon, [Kranz 2000][book_kranz_2000] Failure Is Not an Option, [Logsdon 1970][book_logsdon_1970] The Decision to Go to the Moon, [Logsdon 2010][book_logsdon_2010] John F Kennedy and the Race to the Moon, [Kraemer 2006][book_kraemer_2006] Rocketdyne, and [Mindell 2008][book_mindell_2008] Digital Apollo document the specific arrangement. The specific contrast with the specific COTS instrument is the specific clearest available within the specific same agency, because the specific two instruments funded specific comparable capability development sixty years apart and produced specific opposite dispositions of the specific resulting capability.

The specific Skunk Works and specific classified-programme arrangements documented in [Rich and Janos 1994][book_rich_janos_1994] Skunk Works and [Miller 1995][book_miller_1995] Lockheed Skunk Works supply the specific instance in which the specific reduced oversight the specific Space Act Agreement provides was obtained instead through specific classification. The specific comparison establishes that the specific oversight reduction is separable from the specific instrument and can be achieved by specific several institutional routes, each with specific different accountability consequences.

The specific European and specific Japanese launch programmes documented through the specific [Arianespace record][ref_arianespace], the specific [JAXA press releases][ref_jaxa_press], and the [Krige et al 2000][book_krige_et_al_2000] A History of the European Space Agency supply the specific comparative institutional arrangements, in which the specific public capital is supplied through specific national and specific consortium structures with specific equity or specific quasi-equity positions rather than through specific non-dilutive milestone payments. The specific comparison is the specific most direct available test of whether the specific non-dilutive property matters, and the specific European record of specific slower cost reduction is consistent with the specific proposition without establishing it.

## Historiographical Gap and Recent Scholarship

The scholarly literature on the specific COTS instrument is substantial in volume and unusual in character. Substantially the largest portion of it is advocacy, produced by specific participants or specific institutional beneficiaries and directed at extending the specific instrument to specific other domains. The specific evaluative literature is thinner and is concentrated in the specific oversight bodies rather than in the specific academic journals.

### Primary Source Documentation

The specific primary record comprises the specific statutory and regulatory materials at the specific [National Aeronautics and Space Act][ref_nasa_act_1958], the specific [Space Act Agreement authority][ref_51_usc_20113], the specific [NASA partnerships guidance][ref_nasa_partnerships], the specific [NASA Federal Acquisition Regulation Supplement][ref_nasa_far_supplement], the specific [Federal Acquisition Regulation Part 15][ref_far_part_15] and [Part 16][ref_far_part_16], the specific [Commercial Space Launch Act][ref_csla_1984] and its specific [2004 amendments][ref_csla_amendments_2004], and the specific [Commercial Space Launch Competitiveness Act of 2015][ref_uscsla_2015]. The specific programme record comprises the specific COTS, Commercial Crew, and Commercial Resupply materials identified above. The specific expenditure record is accessible through the specific [Federal Procurement Data System][ref_fpds] and the specific [USAspending][ref_usaspending] systems, and the specific budget-formulation framework through the specific [OMB circulars][ref_omb_circular_a11].

### Oversight and Programme-Evaluation Literature

The specific evaluative record is dominated by the specific oversight bodies. The specific principal documents comprise the specific [GAO 2009 COTS evaluation][ref_gao_cots_2009], the specific [GAO 2011 commercial cargo evaluation][ref_gao_cots_2011], the specific [NASA Office of Inspector General 2013 COTS evaluation][ref_nasa_oig_cots_2013], the specific [NASA Office of Inspector General 2018 commercial cargo evaluation][ref_nasa_oig_ccp_cargo_2018], the specific [GAO 2014][ref_gao_2014_commercial_crew], [2019][ref_gao_ccp_2019], and [2020][ref_gao_2020_commercial_crew] Commercial Crew evaluations, the specific [GAO 2023 National Security Space Launch evaluation][ref_gao_nssl_2023], and the specific Congressional Research Service reports at the specific [Commercial Crew report][ref_crs_commercial_crew], the specific [2018 Commercial Crew report][ref_crs_commercial_crew_2018], and the specific [2022 Artemis report][ref_crs_artemis_2022], with the specific broader collection at the specific [CRS reports database][ref_crs_reports] and the specific [Congressional record][ref_congressional_record] and [House Science Committee hearing record][ref_house_science_committee_hearings].

### Procurement-Economics Literature

The specific theoretical literature is surveyed in the Cross-Disciplinary Framings section. The specific principal works are [Laffont and Tirole 1993][book_laffont_tirole_1993], [McAfee and McMillan 1988][book_mcafee_mcmillan_1988], [Myerson 1981][research_myerson_1981], [Milgrom 2004][book_milgrom_2004], [Bajari and Tadelis 2001][research_bajari_tadelis_2001], [Bajari McMillan and Tadelis 2009][research_bajari_mcmillan_tadelis_2009], [Levin and Tadelis 2010][research_levin_tadelis_2010], [Corts and Singh 2004][research_corts_singh_2004], [Kalnins and Mayer 2004][research_kalnins_mayer_2004], [Che and Chung 1999][research_che_chung_1999], and [Gagnepain and Ivaldi 2002][research_gagnepain_ivaldi_2002]. The specific gap the literature exhibits with respect to the present case is that its specific empirical base is drawn overwhelmingly from specific construction and specific routine-services procurement, where the specific requirement is specifiable and the specific provider population is large. The specific applicability of the specific findings to a specific first-of-kind development with a specific provider population of two is not established.

### Public-Private-Partnership and Innovation-Policy Literature

The specific literature comprising [Grimsey and Lewis 2004][book_grimsey_lewis_2004], [Osborne 2000][book_osborne_2000], [Yescombe 2007][book_yescombe_2007], [Hodge and Greve 2007][research_hodge_greve_2007], [Bovaird 2004][research_bovaird_2004], and [Vining and Weimer 2005][research_vining_weimer_2005] supplies the specific comparative record for specific hybrid arrangements, and the specific innovation-policy literature comprising [Nelson 1959][research_nelson_1959], [Arrow 1962][research_arrow_1962], [Lerner 1996][research_lerner_1996_government_program], [Kortum and Lerner 2000][research_kortum_lerner_2000], [Hall and Lerner 2010][research_hall_lerner_2010], [Bonvillian 2018][research_bonvillian_2018], [Mazzucato 2013][book_mazzucato_2013], and [Mazzucato 2021][book_mazzucato_2021] supplies the specific rationale and evaluation apparatus. The specific finding the specific partnership literature reports, that specific outcomes are substantially more variable than the specific advocacy predicts, is the specific principal caution the article carries into its specific assessment.

### Small Business Innovation Research Literature

The specific SBIR literature supplies the specific closest statutory analogue and is developed at length in the specific series that the [Introduction to the SBIR and STTR Programs article A132][related_post_a132_sbir_intro], the [Phase III and the Valley of Death article A138][related_post_a138_sbir_phase3], and the [Money Behind an SBIR or STTR Award article A140][related_post_a140_sbir_money] represent. The specific statutory and administrative materials are the specific [statute at 15 USC 638][ref_sbir_statute_15usc638], the specific [Small Business Administration policy directive][ref_sba_sbir_policy_directive], and the specific [programme portal][ref_sbir_gov].

### Agency-Side and Public-Administration Literature

The specific literature on the specific purchasing agency is substantial and is systematically underused in the specific procurement-economics treatments, which model the specific agency as a specific unitary rational actor. The specific principal works are [McCurdy 1994][book_mccurdy_1994] Inside NASA, [Handberg 1994][book_handberg_1994] Reinventing NASA, [Launius 1994][book_launius_1994], [Launius 2004][book_launius_2004] Frontiers of Space Exploration, [McDougall 1985][book_mcdougall_1985] The Heavens and the Earth, [Logsdon 1970][book_logsdon_1970], [Logsdon 2010][book_logsdon_2010], [Klerkx 2004][book_klerkx_2004] Lost in Space, [Selznick 1949][book_selznick_1949], and [Hargrove 1994][book_hargrove_1994] Prisoners of Myth. The specific organizational-culture strand in [Kunda 1992][book_kunda_1992] Engineering Culture and the specific professions strand in [Abbott 1988][book_abbott_1988] The System of Professions and [Larson 1977][book_larson_1977] The Rise of Professionalism supply the specific account of how a specific technical workforce inside a specific agency forms and defends a specific jurisdiction, which bears directly on the specific agency's specific willingness to cede a specific development to a specific outside provider.

### Institutional and Comparative-Political-Economy Literature

The specific comparative literature comprising [Johnson 1982][book_johnson_1982], [Amsden 1989][book_amsden_1989], [Wade 1990][book_wade_1990], [Evans 1995][book_evans_1995], [Woo-Cumings 1999][book_woo_cumings_1999], [Chang 2002][book_chang_2002], [Block 2008][research_block_2008], and [Weiss and Thurbon 2021][research_weiss_thurbon_2021] supplies the specific state-capacity apparatus, and the specific institutional-economics strand in [North 1990][book_north_1990], [Ostrom 1990][book_ostrom_1990], [Greif 2006][book_grief_2006], and [Acemoglu and Robinson 2012][book_acemoglu_robinson_2012] supplies the specific account of why a specific rule transplanted without its specific supporting institutions fails. The specific innovation-systems strand in [Freeman 1987][book_freeman_1987], [Lundvall 1992][book_lundvall_1992], [Nelson 1993][book_nelson_1993], [Mowery and Rosenberg 1998][book_mowery_rosenberg_1998], [Perez 2002][book_perez_2002] Technological Revolutions and Financial Capital, and [Schumpeter 1942][book_schumpeter_1942] Capitalism Socialism and Democracy supplies the specific macro framing.

### Systems-Engineering and Reliability Literature

The specific literature comprising [Blanchard and Fabrycky 2011][book_blanchard_fabrycky_2011], [Buede 2009][book_buede_2009], [Suh 2001][book_suh_2001], [Maier 1998][research_maier_1998], [Sage and Cuppan 2001][research_sage_cuppan_2001], the specific [INCOSE Systems Engineering Handbook][ref_incose_handbook], and the specific [NASA Systems Engineering Handbook][ref_nasa_se_handbook] supplies the specific milestone-decomposition apparatus. The specific reliability strand comprising [Perrow 1984][book_perrow_1984], [Vaughan 1996][book_vaughan_1996], [Weick and Sutcliffe 2007][book_weick_sutcliffe_2007], [O'Connor and Kleyner 2012][book_oconnor_kleyner_2012], [Musa 1998][book_musa_1998], and [Duane 1964][research_duane_1964], together with the specific [Rogers Commission report][ref_rogers_commission_1986] and the specific [Columbia Accident Investigation Board report][ref_caib_report_2003], supplies the specific institutional history from which the specific mission-assurance requirements derive.

### Methodological Literature

The specific case-study methodology literature comprising [Yin 2014][book_yin_2014] Case Study Research and Applications and [Creswell 2014][book_creswell_2014] Research Design supplies the specific inferential standards. The specific selection problem for this specific article is that the specific instrument's specific successes are documented in specific detail by specific participants and its specific failures are documented thinly, so that the specific readily available evidence is systematically favorable. The specific evolutionary and failure treatments in [Nelson and Winter 1982][book_nelson_winter_1982], [Metcalfe 1998][book_metcalfe_1998], [Ormerod 2005][book_ormerod_2005] Why Most Things Fail, [Kauffman 1993][book_kauffman_1993], and [Beinhocker 2006][book_beinhocker_2006] The Origin of Wealth supply the specific base-rate framing. The specific working-paper record through which the specific procurement-economics frontier circulates is accessible at the specific [National Bureau of Economic Research][ref_nber] and the specific [Social Science Research Network][ref_ssrn].

### Critical and Skeptical Literature

A specific critical literature reads the specific arrangement as a specific transfer to a specific concentrated private interest rather than as a specific efficient procurement innovation. The specific position draws on [Melman 1970][book_melman_1970] Pentagon Capitalism, [Fallows 1981][book_fallows_1981] National Defense, [Buchanan and Tullock 1962][book_buchanan_tullock_1962] The Calculus of Consent, [Stigler 1971][research_stigler_1971] The Theory of Economic Regulation, [Krueger 1974][research_krueger_1974] The Political Economy of the Rent-Seeking Society, and [Hunter 2016][book_hunter_2016] Creating Strategic Value. The specific concern that the specific instrument's specific reduced oversight is a specific feature for the specific provider and a specific defect for the specific public is well founded and the article does not resolve it. The specific concern that the specific resulting position is now substantially unchallengeable is treated in the Contemporary Comparative Landscape section.

### Trade Press and Journalistic Record

The specific programme record reaches the public substantially through [SpaceNews][ref_spacenews], [Ars Technica space coverage][ref_arstechnica_space], [NASASpaceflight][ref_nasaspaceflight], [Payload][ref_payload], [Payload Research][ref_payload_research], [The Space Review][ref_the_space_review], and [Space Policy Online][ref_space_policy_online], with the specific defense-adjacent coverage in [Breaking Defense][ref_breaking_defense], [Aviation Week][ref_aviation_week], and [Defense News][ref_defense_news], and the specific business coverage in [Bloomberg][ref_bloomberg], the [New York Times][ref_nyt], the [Wall Street Journal][ref_wsj], and the [Washington Post][ref_washington_post]. The specific peer-reviewed sector treatment appears in [Space Policy][ref_space_policy_journal], the [AIAA Journal of Spacecraft and Rockets][ref_aiaa_jsr], and the [Journal of Space Law][ref_journal_space_law], with the specific procurement-specific treatment in the [Journal of Public Procurement][ref_journal_public_procurement] and the [Public Administration Review][ref_public_admin_review].

## Contemporary Comparative Landscape

The contemporary landscape for the government-anchor capital-formation leg differs from the landscape for the forcing-function conditions, because the specific leg is available to any specific provider the specific agency selects and is therefore a specific policy variable rather than a specific firm attribute.

The specific instrument has been extended substantially since the specific COTS period. The specific Human Landing System awards that the specific [NASA Human Landing System program documentation][ref_nasa_hls_program], the specific [HLS solicitation][ref_nasa_hls_solicitation], the specific [Option A award][ref_nasa_hls_option_a_2021], the specific [Option B award][ref_nasa_hls_option_b_2022], and the specific [sustaining award][ref_nasa_hls_sustainable_2023] record employ a specific comparable milestone structure at a specific substantially larger scale, and the specific protest and litigation record at the specific [GAO 2021 protest decision][ref_gao_hls_bid_protest_2021] and the specific [United States Court of Federal Claims][ref_uscfc] record documents the specific contest the specific larger scale invited, and the specific evaluations at the specific [NASA Office of Inspector General 2021 HLS evaluation][ref_nasa_oig_hls_2021] and the specific [GAO 2022 HLS evaluation][ref_gao_hls_2022] apply the specific same analytical apparatus. The specific commercial low-Earth-orbit destinations programme and the specific commercial lunar payload arrangements extend it further. The specific broader agency posture appears in the specific [NASA commercial space documentation][ref_nasa_commercial_space].

Blue Origin has received specific awards under the specific extended instrument including the specific sustaining lunar-lander award and the specific National Security Space Launch Phase 3 allocation, and its specific position illustrates a specific structural point. The specific instrument supplies specific capital to a specific provider that in that specific case did not require it, because the specific single-funder configuration the [Governance article A287][related_post_a287_spacex_governance] treats already supplied the specific development capital. The specific distinction admits the compact statement through the specific marginal effect of the specific award on the specific provider's specific capital constraint

$$\frac{\partial \, \text{capability}}{\partial K^{\text{gov}}} \approx 0 \quad \text{where the constraint does not bind} \qquad \text{against} \qquad \gg 0 \quad \text{where it does}$$

with the specific instrument performing its specific capital-formation function only for a specific provider whose specific capital constraint binds. The specific award therefore functions for that specific provider substantially as a specific validation and a specific revenue commitment rather than as a specific capital-formation channel. The specific record appears in the specific [Blue Origin press releases][ref_blue_origin_press].

Rocket Lab and the specific smaller entrant set receive specific awards under the specific instrument at a specific scale where the specific capital-formation function is substantially operative, which is the specific population for which the specific instrument was designed. The specific record appears in the specific [Rocket Lab press releases][ref_rocket_lab_press]. The specific United Launch Alliance operates substantially outside the specific development-capital channel and within the specific services channel, documented through the specific [United Launch Alliance news][ref_ula_press].

The specific broader defense-industrial context within which the specific instrument now operates is treated in [Hunter 2016][book_hunter_2016] Creating Strategic Value, [Hartley 2017][book_hartley_2017] The Economics of Arms, [Melman 1970][book_melman_1970] Pentagon Capitalism, and [Fallows 1981][book_fallows_1981] National Defense, and the specific incumbent portfolios against which the specific entrant competes are documented through the specific [Boeing press releases][ref_boeing_press], the specific [Boeing historical archives][ref_boeing_historical_archives], and the specific [Northrop Grumman press releases][ref_northrop_grumman_press]. The specific aerospace-industry comparative record in [Serling 1992][book_serling_1992] Legend and Legacy, [Newhouse 1982][book_newhouse_1982] The Sporty Game, [Newhouse 2007][book_newhouse_2007] Boeing versus Airbus, and [Lawrence 2016][book_lawrence_2016] Airbus versus Boeing supplies the specific longer arc within which the specific present contest sits.

The specific comparative-national picture is that specific other jurisdictions have adopted specific variants of the specific instrument. The specific European arrangements documented through the specific [Arianespace record][ref_arianespace], the specific Japanese arrangements through the specific [JAXA press releases][ref_jaxa_press], the specific Indian arrangements through the specific [ISRO press releases][ref_isro_press], and the specific Chinese arrangements through the specific [China National Space Administration][ref_chinese_space_program] and the specific [China sector reporting][ref_china_commercial_space] exhibit specific different balances between specific public ownership and specific private provision.

The specific concern the critical literature raises deserves statement in this specific section rather than only in the specific literature survey. The specific instrument that opened the specific market to a specific new entrant in the specific 2006 period now operates in a specific market where that specific entrant holds a specific dominant position, and a specific instrument that lowers the specific barrier to a specific challenger also lowers the specific barrier to a specific incumbent extending its specific position. The specific asymmetry admits the compact statement

$$\frac{\partial \, \text{share}}{\partial \, \text{instrument availability}} > 0 \quad \text{for the entrant at } t_0 \qquad \text{and} \qquad > 0 \quad \text{for the same firm as incumbent at } t_1$$

with the specific same policy producing the specific opposite competitive effect at the specific two dates. The specific policy question of whether the specific instrument should now be applied differently is outside the specific article's scope and is not outside the specific reader's legitimate interest.

## Comparative Cross-Sectional Analysis

The government-anchor capital-formation leg admits application to the specific provider set as a specific cross-sectional scoring exercise across the specific five sub-properties the pattern-extraction section states. The specific closure vector admits the compact form

$$\boldsymbol{\phi}_j^{\text{gov-anchor}} \in \{0,1\}^{5}$$

with each specific provider's specific vector indicating the specific satisfaction status across the specific non-dilutive-terms, specific development-stage-timing, specific milestone-decomposition, specific private-cost-share, and specific follow-on-position sub-properties.

SpaceX exhibits specific closure on all five. Blue Origin exhibits specific closure on the specific non-dilutive-terms and specific follow-on-position sub-properties and specific non-closure on the specific development-stage-timing sub-property, because the specific awards arrived after the specific capability was substantially funded. Rocketplane Kistler exhibited specific closure on the specific non-dilutive-terms, specific timing, and specific milestone-decomposition sub-properties and specific non-closure on the specific private-cost-share sub-property, which is what terminated it. The specific X-33 programme exhibited specific non-closure on the specific milestone-decomposition sub-property. The specific cost-plus programmes exhibit specific non-closure on substantially all five.

The specific cross-sectional pattern indicates that the specific milestone-decomposition and the specific private-cost-share sub-properties are the specific two on which the specific negation cases fail, and that neither is a property of the specific funding magnitude. The specific finding admits the compact statement

$$P\!\left( \text{success} \mid K^{\text{gov}} \right) \approx P\!\left( \text{success} \right) \qquad \text{while} \qquad P\!\left( \text{success} \mid \text{decomposed milestones} \wedge \text{cost share} \right) \gg P\!\left( \text{success} \right)$$

with the specific structure of the specific instrument carrying substantially more information than the specific amount disbursed. The specific finding is the specific most directly actionable conclusion in the article, and it is the specific conclusion the specific COTS advocacy literature least frequently states, because the specific advocacy is generally directed at securing the specific appropriation rather than at specifying the specific instrument.

## Data Sources and Reconstruction Methodology

The article draws on specific primary and specific secondary sources, and its specific evidentiary position is the strongest of any article in the series.

The specific primary-source layer comprises the specific statutory, regulatory, programme, and oversight materials identified in the Historiographical Gap section. The specific award amounts, the specific milestone structures, the specific termination actions, and the specific competitive outcomes are directly documented by the specific government party. The specific asymmetry with the preceding articles is substantial and arises from a specific structural fact rather than from a specific research effort, namely that the specific government party to each specific transaction is subject to specific disclosure obligations the specific private party is not.

The specific secondary-source layer comprises the specific trade-press and specific evaluative literature identified above.

The specific reconstruction methodology proceeds by taking the specific documented award and milestone record as the specific spine and using the specific secondary sources only for the specific private-side quantities the specific public record does not contain. The specific supporting technical and programme literature is accessible through the specific [NASA Technical Reports Server][ref_nasa_ntrs], and the specific provider's specific own announcements through the specific [SpaceX news archive][ref_spacex_news_archive] and the specific [SpaceX corporate site][ref_spacex_company].

The specific empirical-record limitations are correspondingly narrower than elsewhere in the series and comprise the following. The specific provider's specific actual development costs are not public, so the specific relation between the specific milestone payments and the specific costs they defrayed is unknown. The specific private cost-share amounts are reported in aggregate rather than in detail. The specific classified portions of the specific defense relationship are not documented. The specific counterfactual cost estimates the specific agency published are model outputs whose specific calibration is not independently verifiable. The specific consequence is that the article can state with confidence what the specific government supplied and cannot state with confidence what it bought.

## Alternative Analytical Frameworks

The government-anchor capital-formation framing the article develops is one of several analytical frameworks the surrounding literature applies.

The rent-seeking framing developed in [Buchanan and Tullock 1962][book_buchanan_tullock_1962], [Stigler 1971][research_stigler_1971], and [Krueger 1974][research_krueger_1974] treats the specific arrangement as a specific transfer obtained through specific political action rather than as a specific efficient instrument. The framing draws support from the specific litigation and specific advocacy the entry section documents, and it generates the specific prediction that the specific returns should correlate with the specific political access rather than with the specific technical performance. The specific prediction is checkable in principle against the specific commercial revenue share that the [Value Capture article A284][related_post_a284_spacex_value_capture] documents, The specific rent the framing posits admits the compact form

$$\text{Rent} = \pi^{\text{observed}} - \pi^{\text{competitive benchmark}} \qquad \text{with} \qquad \frac{\partial \text{Rent}}{\partial \, \text{political effort}} > 0$$

under the specific framing's prediction. The specific evidence runs against the specific strong form while supporting the specific weaker claim that the specific early-period access mattered.

The capture framing developed in [Stigler 1971][research_stigler_1971] and the specific regulated-industry treatments in [Kahn 1988][book_kahn_1988] and [Sharkey 1982][book_sharkey_1982] treats the specific agency as having been captured by the specific provider it created. The framing generates the specific prediction that the specific subsequent instrument design should favor the specific incumbent, admitting the compact form

$$\frac{\partial \, \text{eligibility threshold}}{\partial \, \text{incumbent preference}} > 0$$

with the specific agency progressively narrowing the specific admissible provider set. The specific two-lane Phase 3 structure and the specific dual-provider lunar-lander arrangement are evidence against the specific prediction rather than for it.

The developmental-state framing developed in [Johnson 1982][book_johnson_1982], [Amsden 1989][book_amsden_1989], [Wade 1990][book_wade_1990], [Evans 1995][book_evans_1995], [Block 2008][research_block_2008], and [Weiss and Thurbon 2021][research_weiss_thurbon_2021] treats the specific arrangement as a specific instance of a specific hidden industrial policy operating through specific procurement. The specific state capacity the framing treats as decisive admits the compact form

$$\Sigma^{\text{state}} = f\!\left( \text{technical competence}, \; \text{insulation from capture}, \; \text{embeddedness in the sector} \right)$$

with the specific third element requiring enough proximity to the specific industry to select well and the specific second requiring enough distance not to be captured while doing so. The framing supplies the specific most useful comparative frame and the specific most direct challenge to the specific self-description of the specific participants, who generally present the specific arrangement as a specific market mechanism rather than as a specific industrial policy.

The transaction-cost framing developed in [Williamson 1985][book_williamson_1985] and [Bajari and Tadelis 2001][research_bajari_tadelis_2001] treats the specific instrument choice as a specific efficient response to the specific contracting hazards the specific requirement presented, and it predicts that the specific instrument should have been chosen wherever the specific requirement was ill specified and the specific asset specificity low. The specific selection rule admits the compact form

$$\text{agreement} \iff \left[ h < \bar{h} \right] \wedge \left[ \text{requirement ill specified} \right] \wedge \left[ \text{provider can bear } \Delta C \right]$$

with the specific conjunction required. The framing supplies the specific most complete positive account of why the specific instrument was appropriate here and why it would not be appropriate for a specific requirement with a specific higher asset specificity.

The real-options framing developed in [Dixit and Pindyck 1994][book_dixit_pindyck_1994] and [Trigeorgis 1996][book_trigeorgis_1996] treats the specific milestone structure as a specific option strip held by the specific agency. The specific valuation admits the compact form

$$V^{\text{agency}} = \sum_j \pi_j \cdot \max\left\{ B_j - m_j, \; 0 \right\}$$

with the specific agency discontinuing at the specific first milestone where the specific expected benefit falls below the specific payment, which is the specific formal account of the specific termination behavior the Rocketplane Kistler case exhibits.

The public-choice and budgetary framing treats the specific instrument as attractive to the specific agency principally because it produces a specific visible result within a specific appropriation cycle, and it predicts that the specific instrument will be selected for its specific budgetary properties irrespective of its specific efficiency properties. The specific budgetary preference admits the compact form

$$U^{\text{agency}} = w^{\text{outcome}} \cdot V^{\text{programme}} + w^{\text{visibility}} \cdot V^{\text{result within appropriation cycle}}$$

with the specific second term entering the specific agency's objective and not the specific social objective. The framing supplies the specific explanation for the specific instrument's specific rapid extension to specific programmes whose specific characteristics differ substantially from those the specific original application suited.

The evolutionary framing developed in [Nelson and Winter 1982][book_nelson_winter_1982] and [Metcalfe 1998][book_metcalfe_1998] supplies the specific caution that the specific single observed success is a specific poor basis for the specific policy generalization the specific advocacy literature draws, and that the specific relevant population includes the specific programmes that received the specific same instrument and failed. The specific behavioral framing developed in [Kahneman and Tversky 1979][research_kahneman_tversky_1979], [Tversky and Kahneman 1992][research_tversky_kahneman_1992], [Kahneman 2011][book_kahneman_2011] Thinking Fast and Slow, [Simon 1957][book_simon_1957] Administrative Behavior, [Staw 1976][research_staw_1976], [Ross and Staw 1993][research_ross_staw_1993], and [Weick 1979][book_weick_1979] The Social Psychology of Organizing treats the specific agency's specific termination decision as a specific judgment subject to the specific escalation hazard, and it predicts that the specific programmes hardest to terminate are those in which the specific deciding officials made the specific original selection. The framing supplies the specific behavioral complement to the specific public-choice account of the specific same failure.

The specific state-capacity framing developed in [Evans 1995][book_evans_1995], [Johnson 1982][book_johnson_1982], [Amsden 1989][book_amsden_1989], [Wade 1990][book_wade_1990], and [Woo-Cumings 1999][book_woo_cumings_1999] treats the specific outcome as attributable to the specific agency's specific evaluative capability rather than to the specific instrument, and it generates the specific prediction that the specific same instrument applied by a specific less capable agency produces specific worse outcomes. The specific prediction is the specific most policy-relevant claim in the article and is the specific one the specific single case cannot test.

The specific institutional-transplant framing developed in [North 1990][book_north_1990], [Greif 2006][book_grief_2006], and [Acemoglu and Robinson 2012][book_acemoglu_robinson_2012] treats the specific instrument as a specific rule whose specific effects depend on the specific surrounding institutional configuration, and it supplies the specific formal reason the specific advocacy for extending the specific instrument to specific other jurisdictions should be discounted.

The specific systems-architecture framing developed in [Simon 1962][research_simon_1962] The Architecture of Complexity, [Maier 1998][research_maier_1998], and [Suh 2001][book_suh_2001] treats the specific milestone decomposition rather than the specific payment structure as the specific operative variable, and it is the specific framing under which the specific X-33 comparison carries the specific most weight.

The specific correction admits the compact statement

$$\hat{P}\!\left( \text{success} \mid \text{instrument} \right) = \frac{n^{\text{success}}}{n^{\text{success}} + n^{\text{failure}}}$$

with the specific denominator understated whenever the specific evaluation counts only the specific programmes that completed.

## Pattern Extraction

The government-anchor capital-formation pattern that the SpaceX case exhibits admits the following abstract statement without naming any specific downstream application. A mission-directed technology venture achieves the government-anchor capital-formation closure when a specific state customer supplies development capital against demonstrated technical milestones, on terms that convey no claim on the venture's residual or its control, at the stage when private capital would be most expensive, and in a structure that establishes a position from which follow-on revenue can be earned.

The abstract mechanic requires joint satisfaction of five sub-properties, admitting the compact conjunctive form

$$\Phi^{\text{gov-anchor}} = \prod_{k=1}^{5} \phi_k, \qquad \phi_k \in \{0,1\}$$

First, the capital must be non-dilutive, conveying no equity and no governance rights. Capital that conveys either is private capital wearing a public label.

Second, the capital must arrive at the development stage rather than at the operational stage, satisfying

$$t^{\text{award}} < t^{\text{capability}}$$

Capital arriving after the capability exists is revenue, and it performs a different function.

Third, the milestone schedule must decompose the development into increments that are independently verifiable. A milestone schedule tied to a single integrated demonstration supplies neither the payer's option to discontinue nor the provider's intermediate validation, which is the failure the X-33 comparison isolates.

Fourth, the arrangement must require a private cost share, which uses the private capital market as an external validator and makes the two channels complements rather than substitutes.

Fifth, the arrangement must establish a follow-on position. The capital is the mechanism and the position is the transfer. A venture that receives the development capital and does not thereby become the natural provider of the follow-on service has received a subsidy rather than a capital-formation leg.

The specific mechanic admits a specific diagnostic procedure stated as an ordered test vector

$$\tau = \left( \Delta e = \Delta v = 0, \;\; t^{\text{award}} < t^{\text{capability}}, \;\; \left| \{ m_j \} \right| \gg 1, \;\; K^{\text{private}} \geq \alpha K^{\text{gov}}, \;\; \exists \text{ follow-on position} \right)$$

with the specific third and fifth components the ones a specific candidate case most often fails.

The mechanic carries costs the statement should not conceal. The reduced oversight that makes the instrument accessible to a venture-stage provider is the same reduced oversight that prevents the paying public from determining what it bought. The follow-on position the instrument creates is a position against which subsequent competition is structurally disadvantaged, so an instrument justified as opening a market predictably concentrates it. And the instrument's availability is a policy choice made by parties the venture does not control, which makes this leg the least reproducible of the three the series treats.

## Cross-References to the Series

The article back-references the [series opener][related_post_a281_spacex_framing] for the seven-plus-three framework and the pre-COTS prologue. The article back-references the [Value Gradient article A282][related_post_a282_spacex_value_gradient] for the vehicle progression the development capital funded. The article back-references the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] for the demand-side treatment from which this article's capital-side treatment is deliberately distinguished. The article back-references the [Value Capture article A284][related_post_a284_spacex_value_capture] for the commercial revenue against which the government share should be assessed. The article back-references the [Decomposability article A285][related_post_a285_spacex_decomposability] for the rung structure that the milestone decomposition mirrors. The article back-references the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] for the low asset specificity that prevented the holdup the transaction-cost framing would otherwise predict, and for the cost-plus negation cases. The article back-references the [Governance article A287][related_post_a287_spacex_governance] for the control condition that the avoided dilution preserved. The article back-references the [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] for the portfolio across which the capital was allocated.

The article forward-references the Patient-Private Capital-Formation Leg article A290, which treats the private channel that this article's cost-share requirement made complementary, and the Category-Dominating Commercial Spinoff article A291, which treats the third leg. The closing article A292 synthesizes across the framework.

The article cross-references the existing published corpus including the [Introduction to the SBIR and STTR Programs article A132][related_post_a132_sbir_intro], the [Phase III and the Valley of Death article A138][related_post_a138_sbir_phase3], the [Money Behind an SBIR or STTR Award article A140][related_post_a140_sbir_money], the [Patents Trade Secrets and the Disclosure Tradeoff article A164][related_post_a164_patents_trade_secrets], the [Introduction to Space Studies article A90][related_post_a90_intro_space_studies], the [History of Rocketplanes article A96][related_post_a96_history_rocketplanes], the [What Does the United States Space Force Do article A97][related_post_a97_us_space_force], the [Framing and the Co-Development Mechanism article A237][related_post_a237_aerospace_framing], the [Silicon Valley from Defense Contracting article A246][related_post_a246_silicon_valley_defense], the [Software-Defined Aerospace article A247][related_post_a247_software_defined_aerospace], and the [Contemporary Snapshot article A248][related_post_a248_contemporary_snapshot].

## Terminological Note

The article adopts specific terminology consistent with the federal procurement conventions and marks the places where the popular usage diverges. The term "Space Act Agreement" refers to an instrument entered under the agency's other-transaction authority, which is legally distinct from a contract and is not governed by the Federal Acquisition Regulation. The term "contract" is reserved for instruments governed by that regulation, so that the COTS instruments were agreements and the CRS and CCtCap instruments were contracts. The term "non-dilutive" refers to capital conveying no claim on the residual and no claim on control, and it does not imply the capital is costless. The term "incentive power" refers to the fraction of a marginal cost increase borne by the provider, taking the value unity under a pure fixed-price arrangement. The term "milestone payment" refers to a disbursement conditioned on a verified technical or financial event rather than on elapsed time or incurred cost. The term "capital-formation leg" refers to a channel through which the venture obtained the capital to build a capability, and is distinguished throughout from a demand channel through which it obtained revenue for delivering one.

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
- [Vining and Weimer 2005 Establishing Public-Private Partnership Contracts][research_vining_weimer_2005]
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
[book_acemoglu_robinson_2012]: https://openlibrary.org/search?q=Acemoglu+Robinson+Why+Nations+Fail
[book_amsden_1989]: https://global.oup.com/academic/product/asias-next-giant-9780195076035
[book_argote_1999]: https://openlibrary.org/search?q=Argote+Organizational+Learning+Creating+Retaining+Transferring+Knowledge
[book_argyris_schon_1978]: https://www.pearson.com/en-us/subject-catalog/p/organizational-learning-a-theory-of-action-perspective/P200000005949
[book_bain_1968]: https://openlibrary.org/search?q=Bain+Industrial+Organization+1968
[book_beinhocker_2006]: https://www.hbsp.harvard.edu/product/5062-HBK-ENG
[book_berger_2021]: https://www.harpercollins.com/products/liftoff-eric-berger
[book_berger_2024]: https://openlibrary.org/search?q=Berger+Reentry+SpaceX
[book_berlin_2005]: https://global.oup.com/academic/product/the-man-behind-the-microchip-9780195311990
[book_bilstein_1996]: https://openlibrary.org/search?q=Bilstein+Stages+to+Saturn
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
[book_dixit_pindyck_1994]: https://press.princeton.edu/books/hardcover/9780691034102/investment-under-uncertainty
[book_evans_1995]: https://press.princeton.edu/books/paperback/9780691037363/embedded-autonomy
[book_fallows_1981]: https://archive.org/details/nationaldefense00fall
[book_fernholz_2018]: https://www.hachettebookgroup.com/titles/tim-fernholz/rocket-billionaires/9781328662231/
[book_fligstein_2001]: https://press.princeton.edu/books/paperback/9780691102542/the-architecture-of-markets
[book_freeman_1987]: https://www.taylorfrancis.com/books/mono/10.4324/9781315014647/technology-policy-economic-performance-christopher-freeman
[book_gompers_lerner_2001]: https://www.hbsp.harvard.edu/product/2434-HBK-ENG
[book_grief_2006]: https://www.cambridge.org/9780521671347
[book_grimsey_lewis_2004]: https://www.e-elgar.com/shop/gbp/public-private-partnerships-9781840647112.html
[book_groves_1962]: https://openlibrary.org/search?q=Groves+Now+It+Can+Be+Told
[book_handberg_1994]: https://openlibrary.org/search?q=Handberg+Reinventing+NASA
[book_hargrove_1994]: https://openlibrary.org/search?q=Hargrove+Prisoners+of+Myth
[book_hartley_2017]: https://www.taylorfrancis.com/books/mono/10.4324/9781315617831/economics-arms-keith-hartley
[book_hewlett_anderson_1962]: https://openlibrary.org/search?q=Hewlett+Anderson+New+World+Manhattan+Project
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
[book_lundvall_1992]: https://www.taylorfrancis.com/books/edit/10.4324/9781315199665/national-systems-innovation-bengt-ke-lundvall
[book_malone_2014]: https://openlibrary.org/search?q=Malone+The+Intel+Trinity
[book_march_simon_1958]: https://www.wiley.com/en-us/Organizations%2C+2nd+Edition-p-9780631186311
[book_mazzucato_2013]: https://marianamazzucato.com/books/the-entrepreneurial-state
[book_mazzucato_2021]: https://marianamazzucato.com/books/mission-economy/
[book_mcafee_mcmillan_1988]: https://openlibrary.org/search?q=McAfee+McMillan+Incentives+in+Government+Contracting
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
[book_oconnor_kleyner_2012]: https://openlibrary.org/search?q=O%27Connor+Kleyner+Practical+Reliability+Engineering
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
[book_serling_1992]: https://openlibrary.org/search?q=Serling+Legend+and+Legacy+Boeing
[book_sharkey_1982]: https://www.cambridge.org/9780521271943
[book_simon_1957]: https://www.simonandschuster.com/books/Administrative-Behavior-4th-Edition/Herbert-A-Simon/9781439136218
[book_suh_2001]: https://global.oup.com/academic/product/axiomatic-design-9780195134667
[book_tirole_1988]: https://mitpress.mit.edu/9780262200714/the-theory-of-industrial-organization/
[book_trigeorgis_1996]: https://mitpress.mit.edu/9780262201025/real-options/
[book_vaughan_1996]: https://press.uchicago.edu/ucp/books/book/chicago/C/bo22781921.html
[book_wade_1990]: https://press.princeton.edu/books/paperback/9780691117294/governing-the-market
[book_weick_1979]: https://www.mheducation.com/highered/product/social-psychology-organizing-weick/M9780075548089.html
[book_weick_sutcliffe_2007]: https://openlibrary.org/search?q=Weick+Sutcliffe+Managing+the+Unexpected
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
[ref_faa_launch_licenses_current]: https://www.faa.gov/space/licenses
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
[ref_journal_space_law]: https://law.olemiss.edu/
[ref_ksc_lc39a_lease]: https://www.nasa.gov/kennedy/
[ref_kwajalein_atoll_documentation]: https://www.army.mil/usakwajalein
[ref_nasa_act_1958]: https://history.nasa.gov/spaceact.html
[ref_nasa_auth_2010]: https://www.congress.gov/111/plaws/publ267/PLAW-111publ267.pdf
[ref_nasa_ccp_certification]: https://www.nasa.gov/commercialcrew
[ref_nasa_ccp_documents]: https://www.nasa.gov/commercialcrew/
[ref_nasa_commercial_space]: https://www.nasa.gov/commercial-space/
[ref_nasa_constellation]: https://ntrs.nasa.gov/search?q=Constellation
[ref_nasa_cots_2011]: https://ntrs.nasa.gov/citations/20120000953
[ref_nasa_cots_report]: https://ntrs.nasa.gov/search?q=Commercial%20Orbital%20Transportation%20Services
[ref_nasa_cots_solicitation_2006]: https://www.nasa.gov/humans-in-space/commercial-space/
[ref_nasa_crs2_press_2016]: https://www.nasa.gov/news-release/nasa-awards-international-space-station-cargo-transport-contracts/
[ref_nasa_crs_program_overview]: https://www.nasa.gov/commercial-resupply/
[ref_nasa_far_supplement]: https://www.hq.nasa.gov/office/procurement/regs/NFS.pdf
[ref_nasa_history]: https://history.nasa.gov/
[ref_nasa_hls_option_a_2021]: https://www.nasa.gov/press-release/as-artemis-moves-forward-nasa-picks-spacex-to-land-next-americans-on-moon/
[ref_nasa_hls_option_b_2022]: https://www.nasa.gov/press-release/nasa-awards-spacex-second-contract-option-for-artemis-moon-landing/
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
[ref_nasa_oig_reports]: https://oig.nasa.gov/
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
[research_alchian_1963]: https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1963.tb00723.x
[research_argote_epple_1990]: https://www.science.org/doi/10.1126/science.247.4945.920
[research_argote_ingram_2000]: https://www.sciencedirect.com/science/article/abs/pii/S0749597800928930
[research_argote_miron_spektor_2011]: https://pubsonline.informs.org/doi/10.1287/orsc.1100.0621
[research_arrow_1962]: https://www.nber.org/system/files/chapters/c2144/c2144.pdf
[research_bajari_mcmillan_tadelis_2009]: https://academic.oup.com/jleo/article-abstract/25/2/372/845776
[research_bajari_tadelis_2001]: https://www.jstor.org/stable/2696367
[research_baumol_1977]: https://www.jstor.org/stable/1807012
[research_block_2008]: https://journals.sagepub.com/doi/10.1177/0032329207312349
[research_bonvillian_2018]: https://mitpress.mit.edu/9780262038522/the-darpa-model-for-transformative-technologies/
[research_bovaird_2004]: https://onlinelibrary.wiley.com/doi/10.1111/j.1467-9299.2004.00405.x
[research_che_chung_1999]: https://academic.oup.com/rand/article-abstract/30/1/97/2701540
[research_coase_1937]: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-0335.1937.tb00002.x
[research_cohen_levinthal_1990]: https://www.jstor.org/stable/2393553
[research_corts_singh_2004]: https://academic.oup.com/jleo/article-abstract/20/1/230/970131
[research_duane_1964]: https://ieeexplore.ieee.org/document/4051464
[research_dutton_thomas_1984]: https://journals.aom.org/doi/10.5465/amr.1984.4277938
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
[research_kalnins_mayer_2004]: https://pubsonline.informs.org/doi/10.1287/mnsc.1040.0223
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
[research_ross_staw_1993]: https://journals.aom.org/doi/10.5465/256640
[research_sage_cuppan_2001]: https://link.springer.com/journal/11213
[research_sahlman_1990]: https://www.sciencedirect.com/science/article/pii/0304405X9090065E
[research_simon_1962]: https://www.jstor.org/stable/985254
[research_staw_1976]: https://www.sciencedirect.com/science/article/abs/pii/003050737690005X
[research_stigler_1971]: https://www.jstor.org/stable/3003160
[research_tversky_kahneman_1992]: https://link.springer.com/article/10.1007/BF00122574
[research_vining_weimer_2005]: https://link.springer.com/journal/11115
[research_weiss_thurbon_2021]: https://journals.sagepub.com/doi/10.1177/0032329220950247
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
