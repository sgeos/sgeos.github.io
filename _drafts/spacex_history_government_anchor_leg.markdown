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

The procurement-mechanism-design tradition traces from [Laffont and Tirole 1993][book_laffont_tirole_1993] and [McAfee and McMillan 1988][book_mcafee_mcmillan_1988] through [Myerson 1981][research_myerson_1981] Optimal Auction Design, [Milgrom 2004][book_milgrom_2004] Putting Auction Theory to Work, [Bajari and Tadelis 2001][research_bajari_tadelis_2001] Incentives Versus Transaction Costs, [Bajari McMillan and Tadelis 2009][research_bajari_mcmillan_tadelis_2009], [Levin and Tadelis 2010][research_levin_tadelis_2010] Contracting for Government Services, [Corts and Singh 2004][research_corts_singh_2004], [Kalnins and Mayer 2004][research_kalnins_mayer_2004], [Che and Chung 1999][research_che_chung_1999], and [Gagnepain and Ivaldi 2002][research_gagnepain_ivaldi_2002]. The framing supplies the specific central result that the specific optimal incentive power falls as the specific project uncertainty rises, because a specific fixed-price instrument applied to a specific poorly specified requirement produces a specific risk premium exceeding the specific efficiency gain. The specific result is directly contrary to the specific policy lesson usually drawn from the specific COTS case, and the article treats the specific tension rather than suppressing it.

The transaction-cost tradition traces from [Coase 1937][research_coase_1937] through [Williamson 1971][research_williamson_1971], [Williamson 1975][research_williamson_1975], [Williamson 1985][book_williamson_1985], [Williamson 2002][research_williamson_2002], [Klein Crawford and Alchian 1978][research_klein_crawford_alchian_1978], [Monteverde and Teece 1982][research_monteverde_teece_1982], [Masten 1984][research_masten_1984], [Grossman and Hart 1986][research_grossman_hart_1986], [Hart and Moore 1990][research_hart_moore_1990], and [Lafontaine and Slade 2007][research_lafontaine_slade_2007]. The framing treats the specific bilateral-monopoly hazard that arises once a specific provider has invested in a specific asset specific to a specific single customer, and it predicts the specific holdup the specific fixed-price instrument would otherwise invite. The specific hazard index admits the compact form

$$h = \frac{V^{\text{asset in intended use}} - V^{\text{asset in next-best use}}}{V^{\text{asset in intended use}}}$$

with the specific hazard rising in the specific asset specificity. The specific SpaceX case exhibits a specific low value of the specific index relative to a specific typical defense programme, because the specific launch vehicle the specific government funding helped develop had specific commercial uses the specific government did not control. The specific low specificity is the specific structural reason the specific arrangement did not produce the specific holdup the framing would otherwise predict, and it connects the capital-formation leg directly to the generality-forcing condition the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats.

The entrepreneurial-finance tradition traces from [Sahlman 1990][research_sahlman_1990] through [Gompers 1995][research_gompers_1995] Optimal Investment Monitoring and the Staging of Venture Capital, [Lerner 1994][research_lerner_1994_syndication], [Kaplan and Stromberg 2003][research_kaplan_stromberg_2003], [Kaplan and Stromberg 2004][research_kaplan_stromberg_2004], [Gompers and Lerner 2001][book_gompers_lerner_2001], [Metrick and Yasuda 2011][book_metrick_yasuda_2011], and [Lerner 2009][book_lerner_2009] Boulevard of Broken Dreams. The framing treats the specific milestone structure as a specific staged financing and supplies the specific observation that the specific instrument replicates substantially the specific monitoring function a specific venture investor performs, while dispensing with the specific equity claim that ordinarily compensates the specific investor for performing it. The specific government-programme evaluation literature in [Lerner 1996][research_lerner_1996_government_program] and [Kortum and Lerner 2000][research_kortum_lerner_2000] supplies the specific empirical apparatus for assessing whether the specific public capital displaced or complemented the specific private capital.

The public-economics tradition traces from [Nelson 1959][research_nelson_1959] The Simple Economics of Basic Scientific Research and [Arrow 1962][research_arrow_1962] Economic Welfare and the Allocation of Resources for Invention through [Griliches 1979][research_griliches_1979], [Griliches and Lichtenberg 1984][research_griliches_lichtenberg_1984], [Romer 1990][research_romer_1990], and [Aghion and Howitt 1992][research_aghion_howitt_1992]. The framing supplies the specific rationale for the specific public expenditure, resting on the specific gap between the specific private and the specific social return that a specific appropriability failure creates. The specific gap admits the compact form

$$\Delta = r^{\text{social}} - r^{\text{private}} > 0$$

with the specific public intervention warranted where the specific gap is large and the specific private investment consequently below the specific socially optimal level.

The public-private-partnership tradition traces from [Grimsey and Lewis 2004][book_grimsey_lewis_2004] Public Private Partnerships, [Osborne 2000][book_osborne_2000], [Yescombe 2007][book_yescombe_2007], [Hodge and Greve 2007][research_hodge_greve_2007], [Bovaird 2004][research_bovaird_2004], and [Vining and Weimer 2005][research_vining_weimer_2005]. The framing situates the specific instrument within the specific broader family of specific hybrid arrangements and supplies the specific comparative record against which the specific COTS outcome should be assessed, which is substantially less favorable than the specific COTS advocacy literature suggests.

The mission-oriented and developmental-state tradition traces from [Mazzucato 2013][book_mazzucato_2013] The Entrepreneurial State, [Mazzucato 2021][book_mazzucato_2021] Mission Economy, [Ruttan 2006][book_ruttan_2006] Is War Necessary for Economic Growth, [Weiss 2014][book_weiss_2014] America Inc, [Hartley 2017][book_hartley_2017] The Economics of Arms, [Block 2008][research_block_2008], [Weiss and Thurbon 2021][research_weiss_thurbon_2021], [Johnson 1982][book_johnson_1982], [Amsden 1989][book_amsden_1989], [Wade 1990][book_wade_1990], and [Evans 1995][book_evans_1995] Embedded Autonomy. The framing treats the specific arrangement as a specific instance of specific state-directed development operating through specific procurement rather than through specific ownership or specific directed credit, and it supplies the specific comparative frame within which the specific United States instrument differs from the specific East Asian instruments principally in its specific indirection.

The defense-industrial and rent-seeking tradition traces from [Melman 1970][book_melman_1970] Pentagon Capitalism, [Fallows 1981][book_fallows_1981] National Defense, [Hunter 2016][book_hunter_2016] Creating Strategic Value, [Kaplan 1991][book_kaplan_1991] The Wizards of Armageddon, [Buchanan and Tullock 1962][book_buchanan_tullock_1962], [Stigler 1971][research_stigler_1971], and [Krueger 1974][research_krueger_1974]. The framing treats the specific arrangement as a specific transfer to a specific concentrated private interest and supplies the specific skeptical reading the article treats in the Alternative Analytical Frameworks section.

The innovation-policy and programme-evaluation tradition traces from [Bonvillian 2018][research_bonvillian_2018] on the specific DARPA institutional model, the specific [Heilmeier Catechism][ref_heilmeier_catechism] as the specific programme-selection instrument, [Freeman 1987][book_freeman_1987], [Lundvall 1992][book_lundvall_1992], [Nelson 1993][book_nelson_1993], and [Mowery and Rosenberg 1998][book_mowery_rosenberg_1998]. The framing supplies the specific comparative set of specific public instruments against which the specific Space Act Agreement should be located.

## The Space Act Agreement Instrument

The specific legal instrument under which the specific COTS development capital was extended deserves treatment before the specific history, because substantially every distinctive feature of the specific arrangement follows from it and because the specific commentary routinely describes the specific arrangement as a contract when it was not one.

The specific [National Aeronautics and Space Act][ref_nasa_act_1958] confers on the specific agency an authority to enter into specific agreements other than specific contracts, specific grants, and specific cooperative agreements, codified at the specific [51 USC 20113 provisions][ref_51_usc_20113] and described in the specific [NASA partnerships and Space Act Agreements guidance][ref_nasa_partnerships]. The specific authority is the specific civil-agency analogue of the specific other-transaction authority that the specific defense agencies hold and that the specific [Department of Defense other-transactions resources][ref_dod_other_transactions] describe.

The specific consequence of proceeding under the specific authority rather than under the specific [Federal Acquisition Regulation][ref_far_part_15] is that substantially the entire specific regulatory apparatus governing specific federal procurement does not apply. The specific cost-accounting standards do not apply. The specific certified cost-or-pricing-data requirements do not apply. The specific specific contract-type framework that the specific [Federal Acquisition Regulation Part 16][ref_far_part_16] establishes does not apply. The specific intellectual-property allocation is negotiated rather than prescribed, which the specific [Data Rights and Intellectual Property article A164][related_post_a164_patents_trade_secrets] treats in the specific adjacent context. The specific bid-protest jurisdiction is substantially narrower.

The specific consequences cut in both directions and the article states both. The specific absence of the specific cost-accounting apparatus is what permitted a specific provider without a specific government-compliant accounting system to participate at all, which is the specific barrier that excludes substantially every specific venture-stage firm from specific traditional defense procurement. The specific same absence removes the specific visibility into the specific provider's costs that the specific apparatus exists to supply, so that the specific agency purchasing under the specific instrument cannot determine whether the specific price it pays bears any specific relation to the specific cost incurred.

The specific instrument's specific defining operational feature is that it is a specific agreement rather than a specific procurement, so that the specific agency is not purchasing a specific deliverable but is contributing to a specific jointly pursued objective. The specific distinction admits the compact statement

$$\text{procurement} \; : \; \text{agency receives title to a deliverable} \qquad \text{against} \qquad \text{agreement} \; : \; \text{agency receives a demonstrated capability in the market}$$

with the specific second producing no specific asset the specific agency owns. The specific structure is the specific reason the specific capability the specific funding produced remained available for the specific commercial and specific defense applications that the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] documents, rather than becoming a specific government asset subject to specific government disposition.

## COTS Round One 2006 through 2008

The specific Commercial Orbital Transportation Services programme was announced in the specific January 2006 period and the specific round-one awards were made in the specific August 2006 period. The specific record appears in the specific [NASA commercial space documentation][ref_nasa_cots_solicitation_2006] and the specific [NASA COTS programme literature][ref_nasa_cots_report].

The specific round-one awards went to two providers. The specific SpaceX award was approximately 278 million dollars against a specific milestone schedule covering the specific Falcon 9 launch vehicle and the specific Dragon spacecraft. The specific Rocketplane Kistler award was approximately 207 million dollars against a specific milestone schedule covering the specific K-1 vehicle. The specific figures are reported in the specific programme documentation and are among the specific few quantities in this series that are directly documented rather than reconstructed.

The specific structural features of the specific round-one awards that bear on the capital-formation question are four. The specific awards were milestone-based rather than cost-reimbursed. The specific awards required a specific private cost share. The specific awards conveyed no specific equity and no specific governance rights. The specific awards were terminable at the specific agency's discretion upon a specific milestone failure without a specific termination-for-convenience settlement of the specific kind a specific Federal Acquisition Regulation contract would require.

The specific fourth feature is the specific one that makes the specific instrument work and is the specific one most often omitted from the specific summaries. A specific agency that must pay a specific settlement to discontinue a specific failing programme faces a specific option value in continuation that a specific agency facing no specific settlement does not. The specific difference admits the compact statement

$$V^{\text{continue}} - V^{\text{terminate}} = \left[ \text{expected completion value} \right] - \left[ - S \right] \qquad \text{with} \qquad S = 0 \text{ under the agreement}$$

with the specific settlement term vanishing under the specific instrument, which lowers the specific threshold at which the specific agency will in fact terminate. The specific Rocketplane Kistler case demonstrates the specific mechanism operating.

## The Rocketplane Kistler Termination

The specific Rocketplane Kistler agreement was terminated in the specific 2007 period after the specific provider failed to satisfy a specific financing milestone requiring it to raise a specific private capital sum. The specific termination is recorded in the specific [NASA news releases][ref_nasa_news] and treated in the specific programme evaluations at the specific [GAO 2009 COTS evaluation][ref_gao_cots_2009] and the specific [NASA Office of Inspector General 2013 COTS evaluation][ref_nasa_oig_cots_2013].

The specific case is analytically important for three reasons that the specific commentary generally reduces to one.

The specific first and most frequently noted is that the specific instrument permitted a specific rapid termination. The specific agency recovered the specific unobligated balance and re-competed the specific position, awarding it to a specific second provider in the specific 2008 period. A specific comparable failure under a specific cost-plus development contract would have produced a specific extended termination process and a specific settlement.

The specific second and more analytically interesting is that the specific failed milestone was a specific financing milestone rather than a specific technical one. The specific instrument conditioned the specific public capital on the specific provider's ability to raise the specific private capital, which makes the specific public channel and the specific private channel complements rather than substitutes by explicit design. The specific structure admits the compact statement

$$m_j \text{ released} \iff \left[ \text{technical milestone } j \text{ achieved} \right] \wedge \left[ K^{\text{private}} \geq \alpha K^{\text{gov}} \right]$$

with the specific conjunction required. The specific design uses the specific private capital market as a specific external validator of the specific provider's prospects, which economizes on the specific agency's own assessment capability. The specific mechanism is the specific same one the specific SBIR programme employs through its specific Phase II commercialization requirements, which the [Money Behind an SBIR or STTR Award article A140][related_post_a140_sbir_money] treats.

The specific third is that the specific case supplies the specific counterfactual observation the identification problem requires. A specific competitor holding a specific substantially similar award at a specific substantially similar stage attempted the specific private-capital path and failed to complete it. The specific observation does not establish that the specific SpaceX private raise would have failed, and it does establish that the specific private path was not freely available to a specific similarly situated firm in the specific same period.

## COTS Milestone Mechanics and the Non-Dilutive Property

The specific analytical core of this article is the specific observation that the specific COTS payments functioned as development capital and carried no specific claim on the specific firm. The specific section states the specific claim precisely and then states what it does not establish.

The specific SpaceX COTS award grew through specific amendments to approximately 396 million dollars across the specific agreement period. The specific capital was received across the specific 2006 through 2012 interval, which spans the specific period the [series opener][related_post_a281_spacex_framing] identifies as the specific near-death moment and the specific period in which the specific firm's specific private valuation was at its lowest.

The specific non-dilutive property admits the compact comparison. The specific approximately 396 million dollars received through the specific channel, had it instead been raised as equity at the specific valuations prevailing across the specific interval, would have required surrendering a specific fraction

$$\delta^{\text{avoided}} = \frac{K^{\text{COTS}}}{V + K^{\text{COTS}}}$$

that is substantial at the specific contemporaneous valuations and that would have compounded against every specific subsequent round. The specific compounding is the specific feature that makes the specific timing decisive. A specific dilution avoided early is a specific dilution avoided in every specific later round, because the specific founder share entering each specific subsequent round is higher than it would otherwise have been. The specific cumulative effect admits the compact form

$$e^{\text{founder}}_N = \left[ e_0 - \delta^{\text{avoided}} \right] \prod_{n=1}^{N} \left( 1 - \delta_n \right) \qquad \text{against} \qquad e_0 \prod_{n=1}^{N} \left( 1 - \delta_n \right)$$

with the specific difference persisting across the specific entire subsequent financing sequence rather than being confined to the specific round it displaced. The specific connection to the [Governance article A287][related_post_a287_spacex_governance] is direct, because the specific control condition that article analyzes depends on the specific founder's specific residual share, and the specific government channel raised the specific share available at every specific subsequent stage.

The specific claim the article does not make deserves equal prominence. The specific analysis does not establish that the specific government capital was necessary, because the specific counterfactual in which the specific firm raised the specific same amount privately at a specific worse price is not obviously infeasible. The specific analysis does not establish that the specific government capital was efficiently deployed, because the specific counterfactual social return on the specific same appropriation directed elsewhere is not estimated. The specific analysis establishes the specific narrower proposition that the specific capital arrived on specific terms substantially more favorable than the specific alternatives available at the specific time, and that the specific favorable terms compounded.

## The Commercial Resupply Services Transition

The specific transition from the specific development agreement to the specific services contract occurred in the specific December 2008 period with the specific award of the specific Commercial Resupply Services contracts, recorded in the specific [NASA news releases][ref_nasa_news] and treated at length in the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand].

The specific transition changes the specific instrument's character in a way the capital-formation analysis must register. The specific CRS contracts were procurement contracts rather than agreements, and the specific payments were for specific delivered services rather than against specific development milestones. The specific channel therefore ceased to be a specific capital-formation channel and became a specific revenue channel at the specific moment of the specific transition.

The specific analytical consequence is that the specific government-anchor capital-formation leg has a specific bounded duration. The specific leg operated across the specific 2006 through approximately 2012 interval, and thereafter the specific government relationship supplied revenue rather than capital. The specific bounded duration admits the compact statement

$$K^{\text{gov}}(t) \approx \text{constant} \qquad \text{for} \qquad t > t^{\text{transition}}$$

with the specific cumulative government development capital reaching a specific plateau while the specific government revenue continued to grow. The specific distinction matters because the specific commentary that describes the specific firm as government-funded conflates a specific bounded historical capital contribution with a specific continuing commercial relationship, and the specific two have specific different implications for substantially every question the series treats.

The specific subsequent [CRS-2 award][ref_nasa_crs2_press_2016] of the specific 2016 period extended the specific services relationship without reopening the specific capital-formation channel.

## Commercial Crew and the Fixed-Price Competition

The specific Commercial Crew progression partially reopened the specific capital-formation channel for a specific second capability. The specific programme proceeded through the specific Commercial Crew Development awards of the specific 2010 and 2011 periods, the specific Commercial Crew Integrated Capability awards of the specific 2012 period, and the specific Commercial Crew Transportation Capability awards of the specific September 2014 period. The specific record appears in the specific [NASA Commercial Crew Program documentation][ref_nasa_ccp_documents], the specific [certification record][ref_nasa_ccp_certification], and the specific evaluations at the specific [GAO 2014 Commercial Crew evaluation][ref_gao_2014_commercial_crew], the specific [GAO 2019 evaluation][ref_gao_ccp_2019], the specific [GAO 2020 evaluation][ref_gao_2020_commercial_crew], the specific evaluations in the specific [NASA Office of Inspector General reports database][ref_nasa_oig_reports], and the specific [Congressional Research Service Commercial Crew report][ref_crs_commercial_crew].

The specific early phases were conducted under specific Space Act Agreements and the specific final phase under a specific Federal Acquisition Regulation contract, which reflects a specific deliberate progression from a specific development instrument to a specific procurement instrument as the specific requirement became specifiable. The specific progression is the specific practical answer to the specific mechanism-design result that the specific optimal incentive power falls with the specific uncertainty, because it applies the specific high-powered instrument at the specific stage where the specific provider knows more than the specific agency and the specific specified instrument at the specific stage where the specific requirement is stable.

The specific CCtCap awards were approximately 4.2 billion dollars to one specific provider and approximately 2.6 billion dollars to the specific second. The specific award structure is a specific fixed-price arrangement with specific milestone payments, so the specific incentive-power parameter sits near unity.

## The Boeing Comparison and Risk Transfer

The specific comparison between the specific two Commercial Crew providers constitutes the specific clearest available natural experiment in the specific procurement literature, because the specific two providers executed a specific substantially identical requirement under a specific substantially identical instrument across a specific identical period.

The specific outcome differed substantially. The specific one provider achieved the specific crewed demonstration flight in the specific May 2020 period. The specific other encountered a specific sequence of specific development difficulties including a specific uncrewed flight-test anomaly in the specific December 2019 period, a specific repeat uncrewed flight in the specific 2022 period, and specific propulsion difficulties during the specific crewed flight test of the specific June 2024 period.

The specific capital-formation significance is not the specific schedule difference but the specific cost incidence. Under the specific fixed-price instrument the specific overrun was borne by the specific provider and recorded as a specific charge against its specific earnings, rather than being reimbursed. The specific reported cumulative charges are substantial and are documented in the specific provider's specific public filings accessible through the specific [Securities and Exchange Commission EDGAR][ref_sec_edgar] system and summarized in the specific [Boeing press releases][ref_boeing_press]. The specific transfer admits the compact statement

$$L^{\text{public}} = (1 - b) \cdot \left( C^{\text{actual}} - C^{\text{estimated}} \right)^{+} \approx 0 \qquad \text{at} \qquad b \approx 1$$

with the specific public exposure approaching zero. The specific comparison against the specific cost-plus counterfactual that the article treats below is the specific substantive demonstration that the specific instrument accomplished the specific risk transfer it was designed to accomplish.

The specific qualification the article records is that the specific risk transfer is only credible where the specific provider can in fact absorb the specific loss. A specific fixed-price instrument imposed on a specific provider without the specific balance sheet to absorb a specific overrun does not transfer the specific risk. It converts it into a specific completion risk borne by the specific agency in a specific different form, which is the specific failure mode the specific defense-procurement literature documents extensively and which the specific Rocketplane Kistler case illustrates in the specific development setting.

## National Security Space Launch Certification

The specific defense channel operated on a specific different principle from the specific civil channel and deserves separate treatment. The specific National Security Space Launch programme, formerly the specific Evolved Expendable Launch Vehicle programme, purchases specific launch services rather than funding specific development, and the specific channel therefore supplied substantially revenue rather than capital across most of its specific history. The specific record appears in the specific [Space Force National Security Space Launch][ref_space_force_nssl] framework documentation, the specific [Phase 1A award record][ref_space_force_nssl_phase1a_2018], the specific [Phase 2 award record][ref_space_force_nssl_phase2_2020], the specific [Phase 3 Lane 2 coverage][ref_spacenews_nssl_phase3], the specific [GAO 2023 National Security Space Launch evaluation][ref_gao_nssl_2023], and the specific [Space Force news][ref_space_force_news] and [Department of Defense contract announcements][ref_dod_contracts].

The specific capital-formation content of the specific defense channel lies in a specific different place. The specific certification process itself is a specific substantial fixed investment that the specific provider must make and that the specific programme partially funds, and the specific certification once obtained is a specific durable asset that raises the specific provider's value independently of any specific specific mission awarded. The specific certification therefore functions as a specific capital contribution in kind rather than in cash, admitting the compact statement

$$\Delta V^{\text{certification}} = \sum_{t} \frac{p^{\text{award}}(t) \cdot \pi^{\text{margin}}}{(1+\rho)^t} \; - \; C^{\text{certification}}$$

with the specific certification's value equal to the specific discounted expected award stream it makes accessible net of the specific investment required to obtain it.

The specific Phase 2 award of the specific 2020 period allocated the specific mission set between two providers on a specific announced split, and the specific Phase 3 structure of the specific 2024 period established a specific two-lane arrangement admitting a specific broader provider set into the specific less demanding lane. The specific progression from a specific single-provider arrangement through a specific duopoly to a specific multi-provider structure across the specific two decades is the specific competitive outcome the specific programme reforms were intended to produce.

## The Litigation and Entry Path

The specific entry path into the specific defense channel is not adequately described as a specific certification process, because the specific entry was contested and the specific contest was resolved partly through specific litigation.

The specific provider filed suit against the specific Air Force in the specific 2014 period challenging a specific sole-source block award to the specific incumbent. The specific matter was resolved by a specific settlement in the specific 2015 period, and the specific certification followed later that specific year. The specific bid-protest and specific claims apparatus that the specific [GAO bid-protest function][ref_gao_bid_protest] and the specific [United States Court of Federal Claims][ref_uscfc] administer is the specific institutional channel through which the specific contest proceeded.

The specific capital-formation significance is that the specific entry into the specific channel required a specific investment in specific legal and specific political action distinct from the specific technical investment, and that the specific investment was available to a specific firm holding a specific patient private capital base and would not have been available to a specific firm dependent on specific near-term contract revenue. The specific observation connects the specific three capital-formation legs, because the specific patient private leg that the Patient-Private Capital-Formation Leg article A290 will treat financed the specific contest that opened the specific government channel.

## Starshield and the Classified Anchor

The specific Starshield business that the specific [SpaceX Starshield documentation][ref_spacex_starshield] describes at the specific unclassified level and that the specific [Reuters 2024 investigation][research_reuters_starshield_2024] and the specific [New York Times 2024 coverage][ref_nyt_starshield_2024] reconstructed represents a specific further stage of the specific government relationship in which the specific government is purchasing a specific capability the specific firm developed substantially on its own account.

The specific direction of the specific capital flow has therefore reversed relative to the specific COTS period. In the specific earlier period the specific government supplied capital to build a specific capability that did not exist. In the specific later period the specific firm supplied a specific capability built with specific commercial capital and the specific government purchased access to it. The specific reversal admits the compact statement

$$\text{sign}\!\left( \frac{\partial K^{\text{firm}}}{\partial \, \text{government relationship}} \right) \; : \; + \text{ in the development period}, \; - \text{ in the current period}$$

with the specific firm now investing ahead of the specific government requirement rather than the reverse. The specific reversal is the specific completion of the specific capital-formation leg and the specific reason the article treats the specific leg as historically bounded.

## SBIR Phase III Sole-Source Authority as Structural Analogue

The specific Small Business Innovation Research programme supplies the specific closest statutory analogue to the specific structural pattern the specific COTS-to-CRS sequence exhibits, and the specific analogy is instructive precisely because the specific statutory mechanism is explicit where the specific COTS mechanism was not.

The specific programme operates under the specific [statutory authority at 15 USC 638][ref_sbir_statute_15usc638] and the specific [Small Business Administration policy directive][ref_sba_sbir_policy_directive] documented through the specific [SBIR programme portal][ref_sbir_gov]. The specific programme is treated comprehensively in the [Introduction to the SBIR and STTR Programs article A132][related_post_a132_sbir_intro], and the specific Phase III mechanism in the [Phase III and the Valley of Death article A138][related_post_a138_sbir_phase3], with the specific funding mechanics in the [Money Behind an SBIR or STTR Award article A140][related_post_a140_sbir_money].

The specific Phase III authority permits a specific agency to award a specific follow-on contract deriving from specific earlier programme work without a specific further competition, and without a specific dollar limit. The specific authority is the specific statutory recognition of a specific structural fact, namely that a specific development award creates a specific provider who is thereafter uniquely positioned, and that requiring a specific fresh competition at the specific follow-on stage would either produce a specific foregone conclusion or would transfer the specific benefit of the specific development investment to a specific competitor who did not make it.

The specific structural pattern admits the compact statement

$$\text{development award} \longrightarrow \text{capability} \longrightarrow \text{position} \longrightarrow \text{follow-on award}$$

with the specific chain operating whether or not a specific statute names it. The specific COTS-to-CRS sequence was formally competed and the specific SBIR Phase III sequence is formally exempt from competition, and the specific two nonetheless produce a specific substantially similar outcome, because the specific competition at the specific follow-on stage is conducted among providers whose specific relative positions the specific prior development stage established.

The specific analytical value of the specific analogy is that it identifies what a specific government-anchor capital-formation leg actually transfers. It does not principally transfer money. It transfers position, and the specific money is the specific mechanism by which the specific position is created. A specific venture evaluating the specific leg should therefore assess the specific follow-on position the specific development award would establish rather than the specific development award's specific magnitude, which is the specific assessment the specific SBIR practitioner literature the specific series treats makes explicitly.

## The Cost-Plus Counterfactual

The specific counterfactual against which the specific instrument should be assessed is not a specific absence of government funding but the specific alternative instrument the specific same agency employed contemporaneously for a specific comparable objective.

The specific Constellation programme and the specific Space Launch System that the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats as generality-forcing negation cases were procured under specific cost-reimbursement arrangements with specific incentive-power parameters near zero. The specific record appears in the specific [NASA Constellation Program documentation][ref_nasa_constellation], the specific [NASA Space Launch System program documentation][ref_nasa_sls_program], the specific [NASA Authorization Act of 2010][ref_nasa_auth_2010], the specific [NASA Office of Inspector General 2022 Artemis management evaluation][ref_nasa_oig_artemis_2022], and the specific [Congressional Research Service 2022 Artemis Program report][ref_crs_artemis_2022].

The specific comparison admits statement along three dimensions. The specific cost incidence differs, with the specific overrun borne publicly under the specific cost-plus instrument and privately under the specific fixed-price instrument. The specific asset disposition differs, with the specific cost-plus instrument producing a specific vehicle the specific agency directs and the specific agreement producing a specific capability in the specific market. The specific termination cost differs, with the specific cost-plus programme carrying a specific constituency and a specific settlement exposure that the specific agreement does not.

The specific comparison is nonetheless confounded in a specific way the specific advocacy literature generally omits. The specific two instruments were applied to specific different requirements. The specific cost-plus programmes pursued a specific crewed beyond-low-Earth-orbit capability with no specific commercial market, and the specific fixed-price instruments pursued a specific low-Earth-orbit logistics capability with a specific plausible commercial market. The specific mechanism-design result that the specific optimal incentive power falls with the specific uncertainty and rises with the specific specifiability implies that the specific instrument choice may have been appropriate in both specific cases. The specific article records the specific confound rather than reporting the specific comparison as a specific clean demonstration.

The specific cost comparison the specific agency itself published estimated that a specific traditional cost-plus development of the specific launch vehicle would have cost several times the specific amount actually expended. The specific estimate is a specific model output produced using a specific parametric cost model calibrated on specific historical programmes, and it is treated in this article as a specific contested reconstruction rather than as a specific measurement. The specific direction of the specific estimate is consistent with the specific broader procurement literature and the specific magnitude is not independently verifiable.

## Deep Historical Comparative Precedents

The government-anchor capital-formation mechanic admits comparison with specific deep historical precedents in which a specific state supplied specific development capital to a specific private party on specific terms other than ownership.

The specific armory and specific interchangeable-parts precedent that the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats supplies the specific earliest systematic American instance. The specific War Department advanced specific funds against specific delivery schedules to specific private contractors including the specific Whitney and specific Colt enterprises, and the specific advances functioned as specific working capital that the specific contemporary capital markets would not have supplied. The [Hounshell 1984][book_hounshell_1984] From the American System to Mass Production and [Hosley 1996][book_hosley_1996] Colt treatments document the specific arrangements.

The specific air-mail contracts of the specific 1920s and 1930s supply the specific closest transportation-sector analogue. The specific Post Office Department contracts supplied a specific revenue floor against which specific private capital could be raised, and the specific subsequent commercial passenger business was built on the specific capability the specific mail contracts sustained. The [Serling 1992][book_serling_1992] Legend and Legacy, [Bilstein 2001][book_bilstein_2001] Flight in America, and [Crouch 2003][book_crouch_2003] Wings treatments document the specific trajectory. The specific structural difference from the specific COTS case is that the specific mail contracts supplied revenue against a specific delivered service from the outset rather than capital against specific development milestones, which places them nearer the specific CRS stage than the specific COTS stage.

The specific wartime production financing of the specific 1940s supplies the specific largest historical instance of specific public capital supplied to specific private producers without specific equity. The specific arrangements comprised specific government-owned contractor-operated facilities, specific advance payments, and specific accelerated amortization, and they produced a specific private industrial capability at a specific public cost with a specific negotiated post-war disposition. The [Hounshell 1984][book_hounshell_1984], [Rhodes 1986][book_rhodes_1986] The Making of the Atomic Bomb, [Groves 1962][book_groves_1962] Now It Can Be Told, and [Hewlett and Anderson 1962][book_hewlett_anderson_1962] The New World treatments document specific portions of the specific arrangement. The specific disposition question that the specific post-war period confronted is the specific same question the specific Space Act Agreement resolves in advance by conveying no specific asset.

The specific integrated-circuit procurement of the specific 1960s supplies the specific instance in which a specific government purchase at a specific price no specific commercial buyer would pay carried a specific industry through the specific interval before a specific commercial market existed. The [Berlin 2005][book_berlin_2005] The Man Behind the Microchip, [Malone 2014][book_malone_2014] The Intel Trinity, [Lecuyer 2006][book_lecuyer_2006] Making Silicon Valley, [Riordan Hoddeson and Kolb 2015][book_riordan_hoddeson_kolb_2015] Tunnel Visions, [Mindell 2008][book_mindell_2008] Digital Apollo, and the specific retrospectives in [Noyce 1976][research_noyce_1976] and [Kilby 1976][research_kilby_1976] document the specific trajectory, and the [Silicon Valley from Defense Contracting article A246][related_post_a246_silicon_valley_defense] treats the specific regional consequence. The specific case is a specific demand-side rather than a specific capital-side instance, which the article notes because the specific two are conflated as frequently in the specific historical literature as in the specific contemporary commentary.

The specific ARPANET and the specific DARPA institutional model supply the specific instance of a specific public funder operating through a specific programme-manager structure with a specific explicit selection discipline. The [Abbate 1999][book_abbate_1999] Inventing the Internet and [Norberg and O'Neill 1996][book_norberg_oneill_1996] Transforming Computer Technology treatments document the specific programme, [Bonvillian 2018][research_bonvillian_2018] documents the specific institutional model, and the specific [Heilmeier Catechism][ref_heilmeier_catechism] states the specific selection instrument. The specific model differs from the specific COTS instrument in that it funds specific research rather than specific capability demonstration and conveys no specific expectation of a specific follow-on procurement.

The specific X-33 and specific reusable-launch-vehicle programmes of the specific 1990s supply the specific negation case within the specific same agency and the specific same domain. The specific programme proceeded under a specific cooperative agreement with a specific cost share, pursued a specific technically ambitious single-vehicle demonstration, and was terminated in the specific 2001 period without producing a specific flying article. The specific record is accessible through the specific [NASA X-33 and reusable launch vehicle literature][ref_ntrs_x33] and the specific [NASA history archives][ref_nasa_history]. The specific case shares the specific cost-share structure with the specific COTS instrument and differs in that the specific milestone schedule was tied to a specific single integrated demonstration rather than to a specific sequence of independently valuable increments, which is the specific decomposability property the [Decomposability article A285][related_post_a285_spacex_decomposability] treats. The specific comparison establishes that the specific instrument alone is insufficient and that the specific milestone decomposition is doing substantial work.

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

### Critical and Skeptical Literature

A specific critical literature reads the specific arrangement as a specific transfer to a specific concentrated private interest rather than as a specific efficient procurement innovation. The specific position draws on [Melman 1970][book_melman_1970] Pentagon Capitalism, [Fallows 1981][book_fallows_1981] National Defense, [Buchanan and Tullock 1962][book_buchanan_tullock_1962] The Calculus of Consent, [Stigler 1971][research_stigler_1971] The Theory of Economic Regulation, [Krueger 1974][research_krueger_1974] The Political Economy of the Rent-Seeking Society, and [Hunter 2016][book_hunter_2016] Creating Strategic Value. The specific concern that the specific instrument's specific reduced oversight is a specific feature for the specific provider and a specific defect for the specific public is well founded and the article does not resolve it. The specific concern that the specific resulting position is now substantially unchallengeable is treated in the Contemporary Comparative Landscape section.

### Trade Press and Journalistic Record

The specific programme record reaches the public substantially through [SpaceNews][ref_spacenews], [Ars Technica space coverage][ref_arstechnica_space], [NASASpaceflight][ref_nasaspaceflight], [Payload][ref_payload], [Payload Research][ref_payload_research], [The Space Review][ref_the_space_review], and [Space Policy Online][ref_space_policy_online], with the specific defense-adjacent coverage in [Breaking Defense][ref_breaking_defense], [Aviation Week][ref_aviation_week], and [Defense News][ref_defense_news], and the specific business coverage in [Bloomberg][ref_bloomberg], the [New York Times][ref_nyt], the [Wall Street Journal][ref_wsj], and the [Washington Post][ref_washington_post]. The specific peer-reviewed sector treatment appears in [Space Policy][ref_space_policy_journal], the [AIAA Journal of Spacecraft and Rockets][ref_aiaa_jsr], and the [Journal of Space Law][ref_journal_space_law], with the specific procurement-specific treatment in the [Journal of Public Procurement][ref_journal_public_procurement] and the [Public Administration Review][ref_public_admin_review].

## Contemporary Comparative Landscape

The contemporary landscape for the government-anchor capital-formation leg differs from the landscape for the forcing-function conditions, because the specific leg is available to any specific provider the specific agency selects and is therefore a specific policy variable rather than a specific firm attribute.

The specific instrument has been extended substantially since the specific COTS period. The specific Human Landing System awards that the specific [NASA Human Landing System program documentation][ref_nasa_hls_program], the specific [Option A award][ref_nasa_hls_option_a_2021], and the specific [sustaining award][ref_nasa_hls_sustainable_2023] record employ a specific comparable milestone structure at a specific substantially larger scale, and the specific evaluations at the specific [NASA Office of Inspector General 2021 HLS evaluation][ref_nasa_oig_hls_2021] and the specific [GAO 2022 HLS evaluation][ref_gao_hls_2022] apply the specific same analytical apparatus. The specific commercial low-Earth-orbit destinations programme and the specific commercial lunar payload arrangements extend it further. The specific broader agency posture appears in the specific [NASA commercial space documentation][ref_nasa_commercial_space].

Blue Origin has received specific awards under the specific extended instrument including the specific sustaining lunar-lander award and the specific National Security Space Launch Phase 3 allocation, and its specific position illustrates a specific structural point. The specific instrument supplies specific capital to a specific provider that in that specific case did not require it, because the specific single-funder configuration the [Governance article A287][related_post_a287_spacex_governance] treats already supplied the specific development capital. The specific award therefore functions for that specific provider substantially as a specific validation and a specific revenue commitment rather than as a specific capital-formation channel. The specific record appears in the specific [Blue Origin press releases][ref_blue_origin_press].

Rocket Lab and the specific smaller entrant set receive specific awards under the specific instrument at a specific scale where the specific capital-formation function is substantially operative, which is the specific population for which the specific instrument was designed. The specific record appears in the specific [Rocket Lab press releases][ref_rocket_lab_press]. The specific United Launch Alliance operates substantially outside the specific development-capital channel and within the specific services channel, documented through the specific [United Launch Alliance news][ref_ula_press].

The specific comparative-national picture is that specific other jurisdictions have adopted specific variants of the specific instrument. The specific European arrangements documented through the specific [Arianespace record][ref_arianespace], the specific Japanese arrangements through the specific [JAXA press releases][ref_jaxa_press], the specific Indian arrangements through the specific [ISRO press releases][ref_isro_press], and the specific Chinese arrangements through the specific [China National Space Administration][ref_chinese_space_program] and the specific [China sector reporting][ref_china_commercial_space] exhibit specific different balances between specific public ownership and specific private provision.

The specific concern the critical literature raises deserves statement in this specific section rather than only in the specific literature survey. The specific instrument that opened the specific market to a specific new entrant in the specific 2006 period now operates in a specific market where that specific entrant holds a specific dominant position, and a specific instrument that lowers the specific barrier to a specific challenger also lowers the specific barrier to a specific incumbent extending its specific position. The specific policy question of whether the specific instrument should now be applied differently is outside the specific article's scope and is not outside the specific reader's legitimate interest.

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

The specific reconstruction methodology proceeds by taking the specific documented award and milestone record as the specific spine and using the specific secondary sources only for the specific private-side quantities the specific public record does not contain.

The specific empirical-record limitations are correspondingly narrower than elsewhere in the series and comprise the following. The specific provider's specific actual development costs are not public, so the specific relation between the specific milestone payments and the specific costs they defrayed is unknown. The specific private cost-share amounts are reported in aggregate rather than in detail. The specific classified portions of the specific defense relationship are not documented. The specific counterfactual cost estimates the specific agency published are model outputs whose specific calibration is not independently verifiable. The specific consequence is that the article can state with confidence what the specific government supplied and cannot state with confidence what it bought.

## Alternative Analytical Frameworks

The government-anchor capital-formation framing the article develops is one of several analytical frameworks the surrounding literature applies.

The rent-seeking framing developed in [Buchanan and Tullock 1962][book_buchanan_tullock_1962], [Stigler 1971][research_stigler_1971], and [Krueger 1974][research_krueger_1974] treats the specific arrangement as a specific transfer obtained through specific political action rather than as a specific efficient instrument. The framing draws support from the specific litigation and specific advocacy the entry section documents, and it generates the specific prediction that the specific returns should correlate with the specific political access rather than with the specific technical performance. The specific prediction is checkable in principle against the specific commercial revenue share that the [Value Capture article A284][related_post_a284_spacex_value_capture] documents, and the specific evidence runs against the specific strong form while supporting the specific weaker claim that the specific early-period access mattered.

The capture framing developed in [Stigler 1971][research_stigler_1971] and the specific regulated-industry treatments in [Kahn 1988][book_kahn_1988] and [Sharkey 1982][book_sharkey_1982] treats the specific agency as having been captured by the specific provider it created. The framing generates the specific prediction that the specific subsequent instrument design should favor the specific incumbent, and the specific two-lane Phase 3 structure and the specific dual-provider lunar-lander arrangement are evidence against the specific prediction rather than for it.

The developmental-state framing developed in [Johnson 1982][book_johnson_1982], [Amsden 1989][book_amsden_1989], [Wade 1990][book_wade_1990], [Evans 1995][book_evans_1995], [Block 2008][research_block_2008], and [Weiss and Thurbon 2021][research_weiss_thurbon_2021] treats the specific arrangement as a specific instance of a specific hidden industrial policy operating through specific procurement. The framing supplies the specific most useful comparative frame and the specific most direct challenge to the specific self-description of the specific participants, who generally present the specific arrangement as a specific market mechanism rather than as a specific industrial policy.

The transaction-cost framing developed in [Williamson 1985][book_williamson_1985] and [Bajari and Tadelis 2001][research_bajari_tadelis_2001] treats the specific instrument choice as a specific efficient response to the specific contracting hazards the specific requirement presented, and it predicts that the specific instrument should have been chosen wherever the specific requirement was ill specified and the specific asset specificity low. The framing supplies the specific most complete positive account of why the specific instrument was appropriate here and why it would not be appropriate for a specific requirement with a specific higher asset specificity.

The real-options framing developed in [Dixit and Pindyck 1994][book_dixit_pindyck_1994] and [Trigeorgis 1996][book_trigeorgis_1996] treats the specific milestone structure as a specific option strip held by the specific agency and supplies the specific formal account of the specific termination behavior the Rocketplane Kistler case exhibits.

The public-choice and budgetary framing treats the specific instrument as attractive to the specific agency principally because it produces a specific visible result within a specific appropriation cycle, and it predicts that the specific instrument will be selected for its specific budgetary properties irrespective of its specific efficiency properties. The framing supplies the specific explanation for the specific instrument's specific rapid extension to specific programmes whose specific characteristics differ substantially from those the specific original application suited.

The evolutionary framing developed in [Nelson and Winter 1982][book_nelson_winter_1982] and [Metcalfe 1998][book_metcalfe_1998] supplies the specific caution that the specific single observed success is a specific poor basis for the specific policy generalization the specific advocacy literature draws, and that the specific relevant population includes the specific programmes that received the specific same instrument and failed.

## Pattern Extraction

The government-anchor capital-formation pattern that the SpaceX case exhibits admits the following abstract statement without naming any specific downstream application. A mission-directed technology venture achieves the government-anchor capital-formation closure when a specific state customer supplies development capital against demonstrated technical milestones, on terms that convey no claim on the venture's residual or its control, at the stage when private capital would be most expensive, and in a structure that establishes a position from which follow-on revenue can be earned.

The abstract mechanic requires joint satisfaction of five sub-properties, admitting the compact conjunctive form

$$\Phi^{\text{gov-anchor}} = \prod_{k=1}^{5} \phi_k, \qquad \phi_k \in \{0,1\}$$

First, the capital must be non-dilutive, conveying no equity and no governance rights. Capital that conveys either is private capital wearing a public label.

Second, the capital must arrive at the development stage rather than at the operational stage. Capital arriving after the capability exists is revenue, and it performs a different function.

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
- [Amsden 1989 Asia's Next Giant][book_amsden_1989]
- [Berlin 2005 The Man Behind the Microchip][book_berlin_2005]
- [Bilstein 2001 Flight in America][book_bilstein_2001]
- [Buchanan and Tullock 1962 The Calculus of Consent][book_buchanan_tullock_1962]
- [Crouch 2003 Wings A History of Aviation from Kites to the Space Age][book_crouch_2003]
- [Dixit and Pindyck 1994 Investment Under Uncertainty][book_dixit_pindyck_1994]
- [Evans 1995 Embedded Autonomy][book_evans_1995]
- [Fallows 1981 National Defense][book_fallows_1981]
- [Freeman 1987 Technology Policy and Economic Performance][book_freeman_1987]
- [Gompers and Lerner 2001 The Money of Invention][book_gompers_lerner_2001]
- [Grimsey and Lewis 2004 Public Private Partnerships][book_grimsey_lewis_2004]
- [Groves 1962 Now It Can Be Told][book_groves_1962]
- [Hartley 2017 The Economics of Arms][book_hartley_2017]
- [Hewlett and Anderson 1962 The New World][book_hewlett_anderson_1962]
- [Hosley 1996 Colt The Making of an American Legend][book_hosley_1996]
- [Hounshell 1984 From the American System to Mass Production][book_hounshell_1984]
- [Hunter 2016 Creating Strategic Value][book_hunter_2016]
- [Johnson 1982 MITI and the Japanese Miracle][book_johnson_1982]
- [Kahn 1988 The Economics of Regulation][book_kahn_1988]
- [Kaplan 1991 The Wizards of Armageddon][book_kaplan_1991]
- [Krige et al 2000 A History of the European Space Agency][book_krige_et_al_2000]
- [Laffont and Tirole 1993 A Theory of Incentives in Procurement and Regulation][book_laffont_tirole_1993]
- [Lecuyer 2006 Making Silicon Valley][book_lecuyer_2006]
- [Lerner 2009 Boulevard of Broken Dreams][book_lerner_2009]
- [Lundvall 1992 National Systems of Innovation][book_lundvall_1992]
- [Malone 2014 The Intel Trinity][book_malone_2014]
- [Mazzucato 2013 The Entrepreneurial State][book_mazzucato_2013]
- [Mazzucato 2021 Mission Economy][book_mazzucato_2021]
- [McAfee and McMillan 1988 Incentives in Government Contracting][book_mcafee_mcmillan_1988]
- [Melman 1970 Pentagon Capitalism][book_melman_1970]
- [Metcalfe 1998 Evolutionary Economics and Creative Destruction][book_metcalfe_1998]
- [Metrick and Yasuda 2011 Venture Capital and the Finance of Innovation][book_metrick_yasuda_2011]
- [Milgrom 2004 Putting Auction Theory to Work][book_milgrom_2004]
- [Mindell 2008 Digital Apollo][book_mindell_2008]
- [Mowery and Rosenberg 1998 Paths of Innovation][book_mowery_rosenberg_1998]
- [Nelson 1993 National Innovation Systems][book_nelson_1993]
- [Nelson and Winter 1982 An Evolutionary Theory of Economic Change][book_nelson_winter_1982]
- [Norberg and O'Neill 1996 Transforming Computer Technology][book_norberg_oneill_1996]
- [Osborne 2000 Public-Private Partnerships][book_osborne_2000]
- [Rhodes 1986 The Making of the Atomic Bomb][book_rhodes_1986]
- [Riordan Hoddeson and Kolb 2015 Tunnel Visions][book_riordan_hoddeson_kolb_2015]
- [Ruttan 2006 Is War Necessary for Economic Growth][book_ruttan_2006]
- [Serling 1992 Legend and Legacy][book_serling_1992]
- [Sharkey 1982 The Theory of Natural Monopoly][book_sharkey_1982]
- [Trigeorgis 1996 Real Options][book_trigeorgis_1996]
- [Wade 1990 Governing the Market][book_wade_1990]
- [Weiss 2014 America Inc][book_weiss_2014]
- [Williamson 1985 The Economic Institutions of Capitalism][book_williamson_1985]
- [Yescombe 2007 Public-Private Partnerships Principles of Policy and Finance][book_yescombe_2007]

### Reference

- [AIAA Journal of Spacecraft and Rockets][ref_aiaa_jsr]
- [Arianespace][ref_arianespace]
- [Ars Technica Space Coverage][ref_arstechnica_space]
- [Aviation Week][ref_aviation_week]
- [Bloomberg][ref_bloomberg]
- [Blue Origin Press Releases][ref_blue_origin_press]
- [Boeing Press Releases][ref_boeing_press]
- [Breaking Defense][ref_breaking_defense]
- [China Commercial Space Sector Coverage][ref_china_commercial_space]
- [China National Space Administration][ref_chinese_space_program]
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
- [Federal Acquisition Regulation Part 15 Contracting by Negotiation][ref_far_part_15]
- [Federal Acquisition Regulation Part 16 Types of Contracts][ref_far_part_16]
- [Federal Procurement Data System][ref_fpds]
- [GAO 2009 COTS Programme Evaluation][ref_gao_cots_2009]
- [GAO 2011 Commercial Cargo Programme Evaluation][ref_gao_cots_2011]
- [GAO 2014 Commercial Crew Programme Evaluation][ref_gao_2014_commercial_crew]
- [GAO 2019 Commercial Crew Program Evaluation][ref_gao_ccp_2019]
- [GAO 2020 Commercial Crew Programme Evaluation][ref_gao_2020_commercial_crew]
- [GAO 2022 Human Landing System Evaluation][ref_gao_hls_2022]
- [GAO 2023 National Security Space Launch Evaluation][ref_gao_nssl_2023]
- [GAO Bid Protest Function][ref_gao_bid_protest]
- [GAO Reports and Testimonies Database][ref_gao_reports]
- [House Science Space and Technology Committee Hearing Record][ref_house_science_committee_hearings]
- [ISRO Press Releases][ref_isro_press]
- [ITAR 22 CFR 120 through 130][ref_itar_22_cfr_120_130]
- [JAXA Press Releases][ref_jaxa_press]
- [Journal of Public Procurement][ref_journal_public_procurement]
- [Journal of Space Law][ref_journal_space_law]
- [NASA Authorization Act of 2010][ref_nasa_auth_2010]
- [NASA Commercial Crew Certification Record][ref_nasa_ccp_certification]
- [NASA Commercial Crew Program Documentation][ref_nasa_ccp_documents]
- [NASA COTS Programme Literature][ref_nasa_cots_report]
- [NASA Commercial Space Documentation][ref_nasa_commercial_space]
- [NASA Constellation Program Documentation][ref_nasa_constellation]
- [NASA Commercial Space Documentation][ref_nasa_cots_solicitation_2006]
- [NASA CRS-2 Award Announcement January 2016][ref_nasa_crs2_press_2016]
- [NASA FAR Supplement][ref_nasa_far_supplement]
- [NASA History Archives][ref_nasa_history]
- [NASA HLS Option A Award April 16 2021][ref_nasa_hls_option_a_2021]
- [NASA HLS Sustaining Lander Award 2023][ref_nasa_hls_sustainable_2023]
- [NASA Human Landing System Program Documentation][ref_nasa_hls_program]
- [NASA News Releases][ref_nasa_news]
- [NASA Office of Inspector General 2013 COTS Evaluation][ref_nasa_oig_cots_2013]
- [NASA Office of Inspector General 2018 Commercial Cargo Evaluation][ref_nasa_oig_ccp_cargo_2018]
- [NASA Office of Inspector General 2021 Human Landing System Evaluation][ref_nasa_oig_hls_2021]
- [NASA Office of Inspector General 2022 Artemis Management Evaluation][ref_nasa_oig_artemis_2022]
- [NASA Office of Inspector General Reports Database][ref_nasa_oig_reports]
- [NASA Partnerships and Space Act Agreements][ref_nasa_partnerships]
- [NASA Space Launch System Program Documentation][ref_nasa_sls_program]
- [NASA X-33 and Reusable Launch Vehicle Literature][ref_ntrs_x33]
- [NASASpaceflight][ref_nasaspaceflight]
- [National Aeronautics and Space Act of 1958][ref_nasa_act_1958]
- [New York Times 2024 Starshield Coverage][ref_nyt_starshield_2024]
- [New York Times Space Coverage][ref_nyt]
- [OMB Circulars][ref_omb_circular_a11]
- [Payload][ref_payload]
- [Payload Research][ref_payload_research]
- [Public Administration Review][ref_public_admin_review]
- [Rocket Lab Press Releases][ref_rocket_lab_press]
- [SBIR and STTR Programme Portal][ref_sbir_gov]
- [SBIR and STTR Statutory Authority 15 USC 638][ref_sbir_statute_15usc638]
- [SEC EDGAR Company Search][ref_sec_edgar]
- [Small Business Administration SBIR Policy Directive][ref_sba_sbir_policy_directive]
- [Space Act Agreement Authority 51 USC 20113][ref_51_usc_20113]
- [Space Force National Security Space Launch][ref_space_force_nssl]
- [Space Force News][ref_space_force_news]
- [Space Force NSSL Phase 1A Award 2018][ref_space_force_nssl_phase1a_2018]
- [Space Force NSSL Phase 2 Award 2020][ref_space_force_nssl_phase2_2020]
- [Space Policy Journal][ref_space_policy_journal]
- [Space Policy Online][ref_space_policy_online]
- [SpaceNews][ref_spacenews]
- [SpaceNews National Security Space Launch Phase 3 Coverage][ref_spacenews_nssl_phase3]
- [SpaceX Starshield Documentation][ref_spacex_starshield]
- [The Space Review][ref_the_space_review]
- [United Launch Alliance News][ref_ula_press]
- [United States Commercial Space Launch Competitiveness Act of 2015][ref_uscsla_2015]
- [United States Court of Federal Claims][ref_uscfc]
- [USAspending Federal Award Data][ref_usaspending]
- [Wall Street Journal Technology Coverage][ref_wsj]
- [Washington Post Technology Coverage][ref_washington_post]

### Research

- [Aghion and Howitt 1992 A Model of Growth Through Creative Destruction][research_aghion_howitt_1992]
- [Arrow 1962 Economic Welfare and the Allocation of Resources for Invention][research_arrow_1962]
- [Bajari and Tadelis 2001 Incentives Versus Transaction Costs A Theory of Procurement Contracts][research_bajari_tadelis_2001]
- [Bajari McMillan and Tadelis 2009 Auctions Versus Negotiations in Procurement][research_bajari_mcmillan_tadelis_2009]
- [Block 2008 Swimming Against the Current The Rise of a Hidden Developmental State][research_block_2008]
- [Bonvillian 2018 DARPA and the Advanced Research Projects Agency Model][research_bonvillian_2018]
- [Bovaird 2004 Public-Private Partnerships From Contested Concepts to Prevalent Practice][research_bovaird_2004]
- [Che and Chung 1999 Contractual Remedies to the Holdup Problem][research_che_chung_1999]
- [Coase 1937 The Nature of the Firm][research_coase_1937]
- [Corts and Singh 2004 The Effect of Repeated Interaction on Contract Choice][research_corts_singh_2004]
- [Gagnepain and Ivaldi 2002 Incentive Regulatory Policies][research_gagnepain_ivaldi_2002]
- [Gompers 1995 Optimal Investment Monitoring and the Staging of Venture Capital][research_gompers_1995]
- [Griliches 1979 Issues in Assessing the Contribution of Research and Development to Productivity Growth][research_griliches_1979]
- [Griliches and Lichtenberg 1984 R and D and Productivity Growth at the Industry Level][research_griliches_lichtenberg_1984]
- [Grossman and Hart 1986 The Costs and Benefits of Ownership][research_grossman_hart_1986]
- [Hall and Lerner 2010 The Financing of R and D and Innovation][research_hall_lerner_2010]
- [Hart and Moore 1990 Property Rights and the Nature of the Firm][research_hart_moore_1990]
- [Hodge and Greve 2007 Public-Private Partnerships An International Performance Review][research_hodge_greve_2007]
- [Kalnins and Mayer 2004 Relationships and Hybrid Contracts][research_kalnins_mayer_2004]
- [Kaplan and Stromberg 2003 Financial Contracting Theory Meets the Real World][research_kaplan_stromberg_2003]
- [Kaplan and Stromberg 2004 Characteristics Contracts and Actions][research_kaplan_stromberg_2004]
- [Kilby 1976 Invention of the Integrated Circuit][research_kilby_1976]
- [Klein Crawford and Alchian 1978 Vertical Integration Appropriable Rents and the Competitive Contracting Process][research_klein_crawford_alchian_1978]
- [Kortum and Lerner 2000 Assessing the Contribution of Venture Capital to Innovation][research_kortum_lerner_2000]
- [Krueger 1974 The Political Economy of the Rent-Seeking Society][research_krueger_1974]
- [Lafontaine and Slade 2007 Vertical Integration and Firm Boundaries][research_lafontaine_slade_2007]
- [Lerner 1994 The Syndication of Venture Capital Investments][research_lerner_1994_syndication]
- [Lerner 1996 The Government as Venture Capitalist][research_lerner_1996_government_program]
- [Levin and Tadelis 2010 Contracting for Government Services Theory and Evidence][research_levin_tadelis_2010]
- [Masten 1984 The Organization of Production][research_masten_1984]
- [Monteverde and Teece 1982 Supplier Switching Costs and Vertical Integration][research_monteverde_teece_1982]
- [Myerson 1981 Optimal Auction Design][research_myerson_1981]
- [Nelson 1959 The Simple Economics of Basic Scientific Research][research_nelson_1959]
- [Noyce 1976 Microelectronics][research_noyce_1976]
- [Reuters 2024 Starshield Investigation][research_reuters_starshield_2024]
- [Romer 1990 Endogenous Technological Change][research_romer_1990]
- [Sahlman 1990 The Structure and Governance of Venture-Capital Organizations][research_sahlman_1990]
- [Stigler 1971 The Theory of Economic Regulation][research_stigler_1971]
- [Vining and Weimer 2005 Establishing Public-Private Partnership Contracts][research_vining_weimer_2005]
- [Weiss and Thurbon 2021 Developmental State or Economic Statecraft][research_weiss_thurbon_2021]
- [Williamson 1971 The Vertical Integration of Production][research_williamson_1971]
- [Williamson 1975 Markets and Hierarchies][research_williamson_1975]
- [Williamson 2002 The Theory of the Firm as Governance Structure][research_williamson_2002]

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
[book_amsden_1989]: https://global.oup.com/academic/product/asias-next-giant-9780195076035
[book_berlin_2005]: https://global.oup.com/academic/product/the-man-behind-the-microchip-9780195311990
[book_bilstein_2001]: https://jhupbooks.press.jhu.edu/title/flight-america
[book_buchanan_tullock_1962]: https://www.libertyfund.org/books/the-calculus-of-consent/
[book_crouch_2003]: https://wwnorton.com/books/Wings/
[book_dixit_pindyck_1994]: https://press.princeton.edu/books/hardcover/9780691034102/investment-under-uncertainty
[book_evans_1995]: https://press.princeton.edu/books/paperback/9780691037363/embedded-autonomy
[book_fallows_1981]: https://archive.org/details/nationaldefense00fall
[book_freeman_1987]: https://www.taylorfrancis.com/books/mono/10.4324/9781315014647/technology-policy-economic-performance-christopher-freeman
[book_gompers_lerner_2001]: https://www.hbsp.harvard.edu/product/2434-HBK-ENG
[book_grimsey_lewis_2004]: https://www.e-elgar.com/shop/gbp/public-private-partnerships-9781840647112.html
[book_groves_1962]: https://openlibrary.org/search?q=Groves+Now+It+Can+Be+Told
[book_hartley_2017]: https://www.taylorfrancis.com/books/mono/10.4324/9781315617831/economics-arms-keith-hartley
[book_hewlett_anderson_1962]: https://openlibrary.org/search?q=Hewlett+Anderson+New+World+Manhattan+Project
[book_hosley_1996]: https://www.press.jhu.edu/books/title/1799/colt
[book_hounshell_1984]: https://jhupbooks.press.jhu.edu/title/american-system-mass-production-1800-1932
[book_hunter_2016]: https://csis-website-prod.s3.amazonaws.com/s3fs-public/legacy_files/files/publication/160930_Hunter_CreatingStrategicValue_Web.pdf
[book_johnson_1982]: https://www.sup.org/books/title/?id=2143
[book_kahn_1988]: https://mitpress.mit.edu/9780262610520/the-economics-of-regulation/
[book_kaplan_1991]: https://openlibrary.org/search?q=Kaplan+The+Wizards+of+Armageddon
[book_krige_et_al_2000]: https://www.esa.int/About_Us/ESA_history
[book_laffont_tirole_1993]: https://mitpress.mit.edu/9780262121743/a-theory-of-incentives-in-procurement-and-regulation/
[book_lecuyer_2006]: https://mitpress.mit.edu/9780262622110/making-silicon-valley/
[book_lerner_2009]: https://press.princeton.edu/books/hardcover/9780691142197/boulevard-of-broken-dreams
[book_lundvall_1992]: https://www.taylorfrancis.com/books/edit/10.4324/9781315199665/national-systems-innovation-bengt-ke-lundvall
[book_malone_2014]: https://openlibrary.org/search?q=Malone+The+Intel+Trinity
[book_mazzucato_2013]: https://marianamazzucato.com/books/the-entrepreneurial-state
[book_mazzucato_2021]: https://marianamazzucato.com/books/mission-economy/
[book_mcafee_mcmillan_1988]: https://openlibrary.org/search?q=McAfee+McMillan+Incentives+in+Government+Contracting
[book_melman_1970]: https://openlibrary.org/search?q=Melman+Pentagon+Capitalism
[book_metcalfe_1998]: https://www.routledge.com/Evolutionary-Economics-and-Creative-Destruction/Metcalfe/p/book/9780415158671
[book_metrick_yasuda_2011]: https://openlibrary.org/search?q=Metrick+Yasuda+Venture+Capital+Finance+of+Innovation
[book_milgrom_2004]: https://www.cambridge.org/9780521551847
[book_mindell_2008]: https://mitpress.mit.edu/9780262516105/digital-apollo/
[book_mowery_rosenberg_1998]: https://openlibrary.org/search?q=Mowery+Rosenberg+Paths+of+Innovation
[book_nelson_1993]: https://global.oup.com/academic/product/national-innovation-systems-9780195076172
[book_nelson_winter_1982]: https://www.hup.harvard.edu/books/9780674272286
[book_norberg_oneill_1996]: https://jhupbooks.press.jhu.edu/title/transforming-computer-technology
[book_osborne_2000]: https://www.routledge.com/Public-Private-Partnerships/Osborne/p/book/9780415225236
[book_rhodes_1986]: https://www.simonandschuster.com/books/The-Making-of-the-Atomic-Bomb/Richard-Rhodes/9781451677614
[book_riordan_hoddeson_kolb_2015]: https://openlibrary.org/search?q=Riordan+Hoddeson+Kolb+Tunnel+Visions
[book_ruttan_2006]: https://global.oup.com/academic/product/is-war-necessary-for-economic-growth-9780195188042
[book_serling_1992]: https://openlibrary.org/search?q=Serling+Legend+and+Legacy+Boeing
[book_sharkey_1982]: https://www.cambridge.org/9780521271943
[book_trigeorgis_1996]: https://mitpress.mit.edu/9780262201025/real-options/
[book_wade_1990]: https://press.princeton.edu/books/paperback/9780691117294/governing-the-market
[book_weiss_2014]: https://www.cornellpress.cornell.edu/book/9780801479922/america-inc/
[book_williamson_1985]: https://www.simonandschuster.com/books/The-Economic-Institutions-of-Capitalism/Oliver-E-Williamson/9780684863740
[book_yescombe_2007]: https://www.sciencedirect.com/book/9780750680547/public-private-partnerships
[ref_51_usc_20113]: https://www.law.cornell.edu/uscode/text/51/20113
[ref_aiaa_jsr]: https://arc.aiaa.org/journal/jsr
[ref_arianespace]: https://www.arianespace.com/
[ref_arstechnica_space]: https://arstechnica.com/science/space/
[ref_aviation_week]: https://aviationweek.com/
[ref_bloomberg]: https://www.bloomberg.com/
[ref_blue_origin_press]: https://www.blueorigin.com/news/
[ref_boeing_press]: https://boeing.mediaroom.com/
[ref_breaking_defense]: https://breakingdefense.com/
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
[ref_far_part_15]: https://www.acquisition.gov/far/part-15
[ref_far_part_16]: https://www.acquisition.gov/far/part-16
[ref_fpds]: https://www.fpds.gov/
[ref_gao_2014_commercial_crew]: https://www.gao.gov/products/gao-14-593
[ref_gao_2020_commercial_crew]: https://www.gao.gov/products/gao-20-121
[ref_gao_bid_protest]: https://www.gao.gov/legal/bid-protests
[ref_gao_ccp_2019]: https://www.gao.gov/products/gao-19-504
[ref_gao_cots_2009]: https://www.gao.gov/products/gao-09-618
[ref_gao_cots_2011]: https://www.gao.gov/products/gao-11-692t
[ref_gao_hls_2022]: https://www.gao.gov/products/gao-22-105506
[ref_gao_nssl_2023]: https://www.gao.gov/products/gao-23-105815
[ref_gao_reports]: https://www.gao.gov/reports-testimonies
[ref_heilmeier_catechism]: https://www.darpa.mil/about-us/heilmeier-catechism
[ref_house_science_committee_hearings]: https://science.house.gov/
[ref_isro_press]: https://www.isro.gov.in/
[ref_itar_22_cfr_120_130]: https://www.ecfr.gov/current/title-22/chapter-I/subchapter-M
[ref_jaxa_press]: https://global.jaxa.jp/press/
[ref_journal_public_procurement]: https://www.emerald.com/insight/publication/issn/1535-0118
[ref_journal_space_law]: https://law.olemiss.edu/
[ref_nasa_act_1958]: https://history.nasa.gov/spaceact.html
[ref_nasa_auth_2010]: https://www.congress.gov/111/plaws/publ267/PLAW-111publ267.pdf
[ref_nasa_ccp_certification]: https://www.nasa.gov/commercialcrew
[ref_nasa_ccp_documents]: https://www.nasa.gov/commercialcrew/
[ref_nasa_commercial_space]: https://www.nasa.gov/commercial-space/
[ref_nasa_constellation]: https://ntrs.nasa.gov/search?q=Constellation
[ref_nasa_cots_report]: https://ntrs.nasa.gov/search?q=Commercial%20Orbital%20Transportation%20Services
[ref_nasa_cots_solicitation_2006]: https://www.nasa.gov/humans-in-space/commercial-space/
[ref_nasa_crs2_press_2016]: https://www.nasa.gov/news-release/nasa-awards-international-space-station-cargo-transport-contracts/
[ref_nasa_far_supplement]: https://www.hq.nasa.gov/office/procurement/regs/NFS.pdf
[ref_nasa_history]: https://history.nasa.gov/
[ref_nasa_hls_option_a_2021]: https://www.nasa.gov/press-release/as-artemis-moves-forward-nasa-picks-spacex-to-land-next-americans-on-moon/
[ref_nasa_hls_program]: https://www.nasa.gov/humans-in-space/human-landing-system/
[ref_nasa_hls_sustainable_2023]: https://www.nasa.gov/press-release/nasa-selects-blue-origin-as-second-artemis-lunar-lander-provider/
[ref_nasa_news]: https://www.nasa.gov/news/
[ref_nasa_oig_artemis_2022]: https://oig.nasa.gov/docs/IG-22-003.pdf
[ref_nasa_oig_ccp_cargo_2018]: https://oig.nasa.gov/docs/IG-18-016.pdf
[ref_nasa_oig_cots_2013]: https://oig.nasa.gov/docs/IG-13-016.pdf
[ref_nasa_oig_hls_2021]: https://oig.nasa.gov/docs/IG-21-024.pdf
[ref_nasa_oig_reports]: https://oig.nasa.gov/
[ref_nasa_partnerships]: https://www.nasa.gov/partnerships/
[ref_nasa_sls_program]: https://www.nasa.gov/humans-in-space/space-launch-system/
[ref_nasaspaceflight]: https://www.nasaspaceflight.com/
[ref_ntrs_x33]: https://ntrs.nasa.gov/search?q=X-33%20reusable%20launch%20vehicle
[ref_nyt]: https://www.nytimes.com/section/science/space
[ref_nyt_starshield_2024]: https://www.nytimes.com/2024/02/16/us/politics/spacex-us-spy-agency-satellites.html
[ref_omb_circular_a11]: https://www.whitehouse.gov/omb/information-for-agencies/circulars/
[ref_payload]: https://payloadspace.com/
[ref_payload_research]: https://payloadspace.com/research/
[ref_public_admin_review]: https://onlinelibrary.wiley.com/journal/15406210
[ref_rocket_lab_press]: https://www.rocketlabusa.com/updates/
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
[ref_spacex_starshield]: https://www.spacex.com/starshield/
[ref_the_space_review]: https://www.thespacereview.com/
[ref_ula_press]: https://www.ulalaunch.com/about/news
[ref_usaspending]: https://www.usaspending.gov/
[ref_uscfc]: https://www.uscfc.uscourts.gov/
[ref_uscsla_2015]: https://www.congress.gov/114/plaws/publ90/PLAW-114publ90.pdf
[ref_washington_post]: https://www.washingtonpost.com/business/technology/
[ref_wsj]: https://www.wsj.com/tech
[research_aghion_howitt_1992]: https://www.jstor.org/stable/2951599
[research_arrow_1962]: https://www.nber.org/system/files/chapters/c2144/c2144.pdf
[research_bajari_mcmillan_tadelis_2009]: https://academic.oup.com/jleo/article-abstract/25/2/372/845776
[research_bajari_tadelis_2001]: https://www.jstor.org/stable/2696367
[research_block_2008]: https://journals.sagepub.com/doi/10.1177/0032329207312349
[research_bonvillian_2018]: https://mitpress.mit.edu/9780262038522/the-darpa-model-for-transformative-technologies/
[research_bovaird_2004]: https://onlinelibrary.wiley.com/doi/10.1111/j.1467-9299.2004.00405.x
[research_che_chung_1999]: https://academic.oup.com/rand/article-abstract/30/1/97/2701540
[research_coase_1937]: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-0335.1937.tb00002.x
[research_corts_singh_2004]: https://academic.oup.com/jleo/article-abstract/20/1/230/970131
[research_gagnepain_ivaldi_2002]: https://academic.oup.com/rand/article-abstract/33/4/605/2603099
[research_gompers_1995]: https://www.jstor.org/stable/2329227
[research_griliches_1979]: https://www.jstor.org/stable/3003318
[research_griliches_lichtenberg_1984]: https://www.nber.org/system/files/chapters/c10054/c10054.pdf
[research_grossman_hart_1986]: https://www.jstor.org/stable/1833199
[research_hall_lerner_2010]: https://www.sciencedirect.com/science/article/pii/S0169721810010142
[research_hart_moore_1990]: https://www.jstor.org/stable/2937861
[research_hodge_greve_2007]: https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6210.2007.00736.x
[research_kalnins_mayer_2004]: https://pubsonline.informs.org/doi/10.1287/mnsc.1040.0223
[research_kaplan_stromberg_2003]: https://academic.oup.com/restud/article-abstract/70/2/281/1571073
[research_kaplan_stromberg_2004]: https://academic.oup.com/rfs/article-abstract/17/1/1/1601330
[research_kilby_1976]: https://ieeexplore.ieee.org/document/1454570
[research_klein_crawford_alchian_1978]: https://www.jstor.org/stable/725234
[research_kortum_lerner_2000]: https://www.rand.org/pubs/reprints/RP924.html
[research_krueger_1974]: https://www.jstor.org/stable/1808883
[research_lafontaine_slade_2007]: https://www.aeaweb.org/articles?id=10.1257/jel.45.3.629
[research_lerner_1994_syndication]: https://www.jstor.org/stable/3665602
[research_lerner_1996_government_program]: https://www.nber.org/papers/w5753
[research_levin_tadelis_2010]: https://academic.oup.com/qje/article-abstract/125/3/1103/1903637
[research_masten_1984]: https://www.jstor.org/stable/725228
[research_monteverde_teece_1982]: https://www.jstor.org/stable/3003400
[research_myerson_1981]: https://pubsonline.informs.org/doi/10.1287/moor.6.1.58
[research_nelson_1959]: https://www.journals.uchicago.edu/doi/10.1086/258177
[research_noyce_1976]: https://ieeexplore.ieee.org/document/1454572
[research_reuters_starshield_2024]: https://www.reuters.com/technology/space/musks-spacex-is-building-spy-satellite-network-us-intelligence-agency-sources-2024-03-16/
[research_romer_1990]: https://www.journals.uchicago.edu/doi/10.1086/261725
[research_sahlman_1990]: https://www.sciencedirect.com/science/article/pii/0304405X9090065E
[research_stigler_1971]: https://www.jstor.org/stable/3003160
[research_vining_weimer_2005]: https://link.springer.com/journal/11115
[research_weiss_thurbon_2021]: https://journals.sagepub.com/doi/10.1177/0032329220950247
[research_williamson_1971]: https://www.jstor.org/stable/1815199
[research_williamson_1975]: https://www.jstor.org/stable/40751236
[research_williamson_2002]: https://www.aeaweb.org/articles?id=10.1257/089533002760278776
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
