---
layout: post
mathjax: true
comments: true
title:  "Virtual Reputation Manipulation: Techniques of Self-Promotion"
date:   2026-01-23 00:00:00 +0000
categories: economics technology sociology
series: virtual_reputation_manipulation
series_title: Virtual Reputation Manipulation
series_index: 2
---

<!-- A278 -->
<script>console.log("A278");</script>

This article is the second in a four-article miniseries treating virtual reputation manipulation as a first-class analytical object. The opening article at [Virtual Reputation Manipulation Theory and Analytical Framework][related_post_a277_theory] established the economic-signaling framework, characterized the manipulation equilibrium as a prisoner's dilemma over a two-sided platform market, developed the organic-establishment-minority puzzle, and introduced the six-axis analytical framework the miniseries applies. The present article catalogs the principal technique classes of self-promotion oriented reputation manipulation, characterizes each along the six-axis framework, surveys the documented enforcement cases and the academic detection literature, and identifies the detection signatures and platform countermeasures each technique admits. The treatment is descriptive-analytical rather than operational. The material is organized for detection engineers, platform integrity teams, legal practitioners, and academic researchers rather than for readers seeking operational manipulation guidance, and where a technique permits both descriptive and operational specification the treatment stops at the descriptive level. Subsequent articles treat the techniques of competitor-attack oriented reputation manipulation and the detection, countermeasure, and organic-establishment landscape that responds to both self-promotion and competitor-attack techniques.

## The Self-Promotion Taxonomy

Self-promotion oriented reputation manipulation refers to the class of techniques by which an actor injects favorable reputation signal about the actor's own product, service, identity, or attributes into a reputation system. The class is distinguished from competitor-attack oriented manipulation (treated in the third article of the miniseries) by the direction of the intended reputation shift and by the resulting differences in technique inventory, detection signature, legal exposure, and market effect. Self-promotion techniques are the more prevalent class in most consumer-facing reputation ecosystems, and the empirical detection literature has focused proportionally more attention on self-promotion than on competitor-attack techniques.

The technique landscape allows partition into several groupings organized by the signal channel each technique class targets. The review-signal group includes individual review fabrication, coordinated review campaigns and review farming, sockpuppet-driven review deposition, and generative-model-produced review content. The engagement-signal group includes follower purchase, engagement purchase (likes, shares, comments, saves), view-count and impression inflation, and coordinated engagement pods. The search-ranking group includes aggressive search-engine optimization at the manipulative end of the spectrum, link-building manipulation, keyword and content manipulation, and app-store optimization gaming. The network-scale coordinated group includes sockpuppet networks and Sybil attacks, cross-platform amplification rings, click farms and human-operator networks, and state-sponsored operations extending into commercial reputation. The grassroots-manufacturing group includes corporate astroturfing, political astroturfing, and front-organization structures. The identity group includes verified-badge acquisition, professional-credential fabrication, and identity impersonation. The reputation-laundering group includes endorsement acquisition, cross-platform reputation transfer, and acquisition-based laundering. The generative-model-content group cuts across the other groupings and represents the most substantial recent development in the technique landscape.

The technique-space partition supports compact formalization as follows. Let $\mathcal{T} = \{t_1, t_2, \ldots, t_K\}$ denote the technique inventory, and let each technique $t_k$ be characterized by its position on the six analytical axes introduced in the framing article,

$$\mathbf{a}_k = (a_k^{\text{signal}}, a_k^{\text{obj}}, a_k^{\text{struct}}, a_k^{\text{model}}, a_k^{\text{interact}}, a_k^{\text{adapt}})$$

with each axis value drawn from an axis-specific space. The distance between techniques on the axis-vector space admits characterization as

$$d(t_j, t_k) = \sum_{c \in \text{axes}} w_c \, \delta_c(a_j^c, a_k^c)$$

with $w_c$ the axis weight and $\delta_c$ the axis-specific distance function. The technique-space partition into the groupings above corresponds to clustering under the distance $d$ with the review-signal, engagement-signal, and search-ranking groupings emerging as the natural clusters under channel-weighted distance.

The aggregate empirical prevalence of self-promotion techniques across the reputation ecosystem permits estimation through the sum

$$V_{\text{self-promo}}(t) = \sum_{k \in \mathcal{T}} \sum_{c \in \text{categories}} n_{k,c}(t) \cdot p_{k,c}(t)$$

with $n_{k,c}(t)$ the signal-event volume for technique $k$ in category $c$ at time $t$ and $p_{k,c}(t)$ the technique-and-category-specific prevalence rate. The empirical estimates surveyed in this article establish that $V_{\text{self-promo}}$ dominates the aggregate manipulation volume across most platform categories, with only political-manipulation-dominant contexts (state-sponsored operations targeting elections) exhibiting comparable competitor-attack volume.

The taxonomy's coverage completeness against the observed technique population allows characterization as the recall-analog statistic

$$\text{Coverage}(\mathcal{T}, \Omega) = \frac{|\{\omega \in \Omega : \exists t_k \in \mathcal{T}, \omega \text{ assigned to } t_k\}|}{|\Omega|}$$

with $\Omega$ the observed manipulation-instance population. The taxonomy the article adopts targets $\text{Coverage} > 0.95$ against the enforcement-record and academic-detection-corpus population and treats residual instances outside the taxonomy as novel-technique candidates for taxonomy revision.

## Cross-Disciplinary Framings

The self-promotion technique landscape supports characterization from several disciplinary traditions beyond the economic-signaling framework the miniseries adopts as primary. The framing article surveys the principal alternative disciplinary treatments and identifies their analytical leverage.

The marketing-and-advertising-theory framing traces from [Aaker 1991][book_aaker_1991] Managing Brand Equity through [Kotler and Keller 2016][book_kotler_keller_2016] Marketing Management and the broader marketing literature. The framing treats self-promotion techniques as extensions of the traditional advertising and word-of-mouth marketing toolkit into digital reputation systems. The [Berger 2016][book_berger_2016] Contagious Why Things Catch On treatment addresses the contemporary word-of-mouth-adjacent literature. The [Godin 2018][book_godin_2018] This is Marketing treatment addresses the practitioner-side framing of the transition from broadcast advertising to earned-reputation marketing. The [Trusov Bucklin Pauwels 2009][research_trusov_bucklin_pauwels_2009] Effects of Word-of-Mouth versus Traditional Marketing treatment provides the reference empirical framework for the word-of-mouth-effectiveness comparison. The marketing-and-advertising framing complements the reputation-manipulation framing by treating the manipulation technique as a boundary case of legitimate promotion rather than as a categorically distinct phenomenon, which surfaces the technique-vs-legitimate-promotion boundary that regulatory frameworks must draw.

The consumer-behavior-and-persuasion-psychology framing traces from [Cialdini 1984][book_cialdini_1984] Influence through the [Petty and Cacioppo 1986][research_petty_cacioppo_1986] Elaboration Likelihood Model of Persuasion framework and the [Chaiken 1980][research_chaiken_1980] Heuristic Systematic Model treatment. The framing identifies the cognitive and motivational mechanisms through which reputation signals influence consumer decision-making, and characterizes self-promotion techniques by the persuasion mechanisms they exploit. The [Fiske and Taylor 2013][book_fiske_taylor_2013] Social Cognition treatment provides the comprehensive social-cognition framework. The [Nisbett and Ross 1980][book_nisbett_ross_1980] Human Inference treatment provides the classical cognitive-heuristics framework relevant to reputation-signal processing. The consumer-behavior framing complements the reputation-manipulation framing by predicting the consumer-response effects of different manipulation techniques based on the technique's alignment with dominant persuasion pathways.

The search-theory-and-information-economics framing traces from [Stigler 1961][research_stigler_1961] The Economics of Information through [Rothschild 1974][research_rothschild_1974] Searching for the Lowest Price When the Distribution of Prices is Unknown and the subsequent search-theory literature. The framing treats reputation signals as inputs to the consumer's search process and characterizes self-promotion techniques by the search-process distortions they produce. The [Diamond 1971][research_diamond_1971] Model of Price Adjustment treatment addresses the equilibrium effect of search costs on price. The search-theory framing complements the reputation-manipulation framing by identifying the consumer-search-cost changes that manipulation techniques impose and the equilibrium market-price and quality-signaling effects that follow.

The multi-level-marketing and network-marketing framing addresses the organizational form under which reputation-manipulation-adjacent practices operate. The [Fitzpatrick 2005][book_fitzpatrick_2005] False Profits treatment provides the industry-analytical framing. The [Taylor 2011][book_taylor_2011] The Case for and Against Multi-Level Marketing treatment provides the case-based analysis. The [FTC 2022 Herbalife Order][ref_ftc_herbalife_2022] and the [FTC 2016 Herbalife Order][ref_ftc_herbalife_2016] establish the reference regulatory precedent for the MLM-adjacent reputation-manipulation subset. The multi-level-marketing framing complements the reputation-manipulation framing by identifying the organizational structures that generate self-promotion at the population scale characteristic of MLM networks.

The computer-science-of-detection framing traces from the [Fawcett 2006][research_fawcett_2006] Introduction to ROC Analysis through the [Chandola Banerjee Kumar 2009][research_chandola_banerjee_kumar_2009] Anomaly Detection A Survey and the subsequent anomaly-detection literature. The framing treats self-promotion detection as a classification-with-imbalanced-classes problem with accuracy-versus-friction tradeoffs. The [Provost and Fawcett 2013][book_provost_fawcett_2013] Data Science for Business treatment addresses the applied-industry framing. The computer-science framing complements the reputation-manipulation framing by identifying the detection-methodology constraints and opportunities that determine the equilibrium detection-versus-manipulation intensity.

The legal-scholarship-of-false-advertising framing traces from [Beales 1980][research_beales_1980] Efficient Regulation of Consumer Information through [Petty 2015][book_petty_2015] The Codevelopment of Marketing Law and Practice and the modern-era false-advertising-and-endorsement scholarship. The framing treats self-promotion techniques as boundary-cases of the false-advertising regulatory framework and characterizes the FTC and Lanham Act application to the digital-reputation environment. The [Petty and Andrews 2008][research_petty_andrews_2008] Covert Marketing Unmasked treatment addresses the covert-marketing-and-testimonial issues. The [FTC Endorsement Guides framework][ref_ftc_endorsement_guides_16_cfr_255] provides the reference regulatory framework. The legal-scholarship framing complements the reputation-manipulation framing by identifying the regulatory-and-enforcement dimensions that shape the technique-vs-legitimate-promotion boundary.

The critical-media-studies-of-influencer-marketing framing traces from [Abidin 2018][book_abidin_2018] Internet Celebrity through [Duffy 2017][book_duffy_2017] Not Getting Paid to Do What You Love and the broader influencer-and-creator-economy literature. The framing treats self-promotion techniques within the broader political-economy of influencer marketing and the labor-and-authenticity dynamics of the creator economy. The [Bishop 2019][research_bishop_2019] Managing Visibility on YouTube through Algorithmic Gossip treatment addresses the platform-algorithm-and-influencer dynamic. The [Marwick 2013][book_marwick_2013] Status Update treatment addresses the broader status-and-visibility economy. The critical-media-studies framing complements the reputation-manipulation framing by treating manipulation as embedded in a broader creator-economy political-economy rather than as a purely technical phenomenon.

## Historical Antecedents

Self-promotion reputation manipulation is not a novel phenomenon of the digital era. The technique inventory inherits significant doctrine, practice, and organizational form from pre-digital antecedents in advertising, public relations, endorsement marketing, and coordinated promotional operations. The framing article surveys the principal historical antecedents and identifies the continuities and discontinuities with the digital-era inventory.

The pre-industrial antecedents include the guild-and-merchant-reputation-cultivation practices of medieval and early-modern commerce, in which merchants coordinated their reputation-signaling through guild membership, apprenticeship-credential display, and repeat-transaction-based trust. The [Trivellato 2009][book_trivellato_2009] The Familiarity of Strangers and the [Greif 2006][book_greif_2006] Institutions and the Path to the Modern Economy treatments document the pre-industrial reputation-signaling infrastructure. The [Ogilvie 2019][book_ogilvie_2019] The European Guilds treatment addresses the guild reputation-management infrastructure.

The nineteenth-century patent-medicine and mail-order eras produced substantial self-promotion technique innovation. The [Young 1961][book_young_1961] The Toadstool Millionaires treatment documents the American patent-medicine testimonial practice. The [Twede Selke 2005][book_twede_selke_2005] Cartons Crates and Corrugated Board and the [Presbrey 1929][book_presbrey_1929] The History and Development of Advertising treatments document the parallel evolution of packaging-and-advertising infrastructure. The [Strasser 1989][book_strasser_1989] Satisfaction Guaranteed The Making of the American Mass Market treatment addresses the mass-market emergence and the associated reputation-and-branding infrastructure development. The [PT Barnum autobiography 1854][ref_barnum_autobiography_1854] documents the era's most famous self-promotion practitioner.

The early-twentieth-century public-relations-industry founding established the professional organizational form for coordinated self-promotion. The [Bernays 1923][book_bernays_1923] Crystallizing Public Opinion and [Bernays 1928][book_bernays_1928] Propaganda treatments established the doctrinal framework. The [Lippmann 1922][book_lippmann_1922] Public Opinion treatment provided the theoretical framing. The [Ivy Lee Declaration of Principles 1906][ref_ivy_lee_declaration_1906] established the industry's professional-ethics framework. The [Ewen 1996][book_ewen_1996] PR A Social History of Spin and [Tye 1998][book_tye_1998] The Father of Spin treatments provide the historical analysis. The [Cutlip 1994][book_cutlip_1994] The Unseen Power Public Relations A History treatment provides the comprehensive industry history.

The mid-twentieth-century direct-marketing and motivation-research eras produced the psychographic-targeting infrastructure that provides the substrate for contemporary personalized reputation-manipulation. The [Packard 1957][book_packard_1957] The Hidden Persuaders treatment documents the motivation-research industry. The [Ogilvy 1963][book_ogilvy_1963] Confessions of an Advertising Man treatment addresses the modernization of advertising practice. The [Reeves 1961][book_reeves_1961] Reality in Advertising treatment addresses the parallel unique-selling-proposition framework. The [Turow 2011][book_turow_2011] The Daily You treatment traces the transition to digital psychographic targeting.

The late-twentieth-century celebrity-endorsement and infomercial eras produced marked technique innovation in the coordinated-testimonial and long-form-promotion spaces. The [McCracken 1989][research_mccracken_1989] Who Is the Celebrity Endorser Cultural Foundations of the Endorsement Process treatment provides the celebrity-endorsement theoretical framework. The [Cronin 2004][book_cronin_2004] Advertising Myths The Strange Half-Lives of Images and Commodities treatment addresses the era's cultural-and-communication analysis. The [FTC Nutrilite Products 1951 Order][ref_ftc_nutrilite_1951] represents the historical regulatory-enforcement precedent applicable to the era's practices.

The astroturfing tradition of manufactured grassroots support traces to political-operations practice from the mid twentieth century forward, with extensive precedent in corporate lobbying campaigns of tobacco, oil, and pharmaceutical industries. The [Oreskes and Conway 2010][book_oreskes_conway_2010] Merchants of Doubt, [McGarity and Wagner 2008][book_mcgarity_wagner_2008] Bending Science, and [Michaels 2008][book_michaels_2008] Doubt Is Their Product treatments document the coordinated-denial-and-manufactured-support playbook. The term astroturf itself traces to [Senator Lloyd Bentsen's 1985 Congressional Record][ref_bentsen_congressional_record_1985] characterization. The [Walker 2014][book_walker_2014] Grassroots for Hire treatment consolidates the contemporary industry analysis.

The direct-marketing-database and multi-level-marketing organizational forms established the population-scale coordination infrastructure that enables contemporary reputation-manipulation at scale. The [FTC v Amway 1979 decision][ref_ftc_amway_1979] and subsequent MLM-related enforcement establish the regulatory framework. The [Fitzpatrick 2005][book_fitzpatrick_2005] False Profits treatment provides the industry-critical analysis. The multi-level-marketing organizational form produces the self-promotion-at-population-scale dynamic that enables coordinated reputation-manipulation across large distributor networks.

## Historiographical Gap and Recent Scholarship

The scholarly treatment of self-promotion reputation manipulation has developed unevenly across disciplines and has integrated less well across traditions than the technical-detection literature. The framing article surveys the observable gap and identifies the recent-scholarship developments that the miniseries builds on.

The marketing-and-advertising scholarship developed continuously from the mid-twentieth-century advertising-industry literature through the contemporary integrated-marketing-communications framework. The application to digital-reputation-manipulation is less developed within the marketing tradition than within the reputation-systems tradition, with the marketing-side treatment typically framing reputation-manipulation as either legitimate word-of-mouth marketing (understating the manipulation dimension) or as unethical practice without technical detail (understating the technique dimension). The [Silverman 2001][book_silverman_2001] Secrets of Word-of-Mouth Marketing and the [Kotler and Keller 2016][book_kotler_keller_2016] treatment illustrate the marketing-side framing.

The consumer-behavior scholarship developed continuously from the classical [Katz and Lazarsfeld 1955][book_katz_lazarsfeld_1955] Personal Influence framework through the contemporary behavioral-economics-and-neuroscience literature. The application to fake-review-effect-on-consumer-choice is developed in the [Chevalier and Mayzlin 2006][research_chevalier_mayzlin_2006], [Luca 2016][research_luca_2016], and adjacent empirical treatments. The gap between the consumer-behavior tradition and the technical-detection tradition remains considerably unbridged, with the consumer-behavior tradition treating reputation signals as inputs to the consumer's decision-process without addressing the signal-manipulation dimension in detail.

The computer-science-of-detection scholarship developed continuously from the [Jindal and Liu 2008][research_jindal_liu_2008] initial framework through the contemporary adversarial-ML-adjacent literature. The application to fake-review-detection is the most-developed subfield of the reputation-manipulation-detection literature. The [Cresci 2020][research_cresci_2020] survey establishes the reference summary. The [Kumar and Shah 2018][research_kumar_shah_2018] False Information on Web and Social Media survey provides the parallel-summary for the broader misinformation-adjacent detection subfield.

The influencer-and-creator-economy scholarship developed rapidly in the 2010s and 2020s in response to the rise of influencer marketing. The [Abidin 2018][book_abidin_2018] Internet Celebrity, [Duffy 2017][book_duffy_2017] Not Getting Paid, [Bishop 2019][research_bishop_2019] Managing Visibility on YouTube, and adjacent treatments establish the field. The integration with the reputation-manipulation detection tradition is emerging but not yet consolidated.

The legal-scholarship-of-endorsement-regulation developed through the FTC endorsement-guides history from 1980 through 2024 and the associated academic commentary. The [Petty and Andrews 2008][research_petty_andrews_2008] treatment, the [Hoffman 2017][research_hoffman_2017] Sponsored Content Regulation, and the [Boerman et al 2018][research_boerman_et_al_2018] Sponsored Content Disclosure Effects treatments establish the reference framework. The gap between the legal-scholarship treatment and the technical-detection treatment remains significantly unbridged, with the legal treatment typically framing manipulation as an enforcement problem without addressing the detection-methodology dimension in detail.

The historiographical gap that the miniseries addresses lies in the absence of an integrated treatment drawing on all five traditions simultaneously. Each tradition treats a portion of the self-promotion manipulation phenomenon, and the standard treatment requires all five. The miniseries organizes the material to make the cross-tradition connections explicit where they are load-bearing for the analytical conclusions.

## Review Manipulation Techniques

The review-signal manipulation class comprises the technique inventory oriented at the star-rating and text-review signals that consumer-facing reputation systems make available. The class is the empirically dominant self-promotion class in consumer-review platforms and has received substantially more academic detection attention than any other class.

### Individual Review Fabrication

Individual review fabrication refers to the manipulation practice in which an actor (or a party acting on the actor's behalf) writes and submits favorable reviews for the actor's own product or service without disclosing the material connection. The practice is the simplest and historically earliest self-promotion technique documented in the digital reputation ecosystem. Documented cases include the [Bing 2004 astroturf blogging incident][ref_bing_2004_astroturf] involving Microsoft-affiliated bloggers writing favorable coverage of Microsoft products, the [Sony PlayStation Portable 2006 fake blog case][ref_sony_psp_2006] involving a Sony-commissioned blog written to appear as unaffiliated fan content, and the [Whole Foods Mackey Rahodeb case 2007][ref_whole_foods_rahodeb_2007] in which the CEO of Whole Foods was found to have written pseudonymous positive commentary on Yahoo Finance about Whole Foods over a seven-year period. The [FTC v Sunday Riley 2019][ref_ftc_sunday_riley_2019] action addressed employee-written fake reviews on Sephora at the direction of the brand's CEO. The [FTC v UrthBox 2019][ref_ftc_urthbox_2019] action addressed influencer-written reviews without disclosed material connection. The [Beuk Boekhandel 2013][ref_beuk_boekhandel_2013] Dutch case established European jurisprudence on fake-review liability.

The academic detection literature for individual fabrication traces to [Jindal and Liu 2008][research_jindal_liu_2008] Opinion Spam and Analysis, which established the field's initial taxonomy and detection methodology. The stylometric-feature vector on which contemporary detectors operate takes the compact form

$$\mathbf{f}_r = (\text{POS-ratios}, \text{n-gram distributions}, \text{lexical richness}, \text{sentiment intensity}, \text{first-person ratio}, \text{superlative rate})$$

with each component estimated on the review text $r$ and fed to a downstream classifier. The [Ott et al 2011][research_ott_et_al_2011] Finding Deceptive Opinion Spam by Any Stretch of the Imagination treatment introduced the labeled-corpus methodology by crowdsourcing production of deceptive reviews and training classifiers on the resulting distribution. The [Ott et al 2013][research_ott_et_al_2013] Negative Deceptive Opinion Spam extended the framework. The [Feng et al 2012][research_feng_et_al_2012] Syntactic Stylometry for Deception Detection treatment introduced the syntactic-features detection approach. The [Li et al 2014][research_li_et_al_2014] Towards a General Rule for Identifying Deceptive Opinion Spam introduced the cross-domain generalization framework.

The empirical prevalence of individual review fabrication varies by platform and category. The [Luca and Zervas 2016][research_luca_zervas_2016] Yelp analysis estimates approximately sixteen percent of Yelp restaurant reviews are filtered as suspicious by Yelp's internal classifier, with the filtered rate rising to approximately twenty percent for restaurants in competitive market segments and rising further under competitive conditions. The [Luca 2016][research_luca_2016] Reviews Reputation and Revenue Yelp treatment estimates the causal impact of a one-star rating increase as approximately five to nine percent revenue increase, which sets the direct commercial incentive for review manipulation. The empirical rating-shift model takes the form

$$\Delta r_i^{\text{obs}} = \Delta r_i^{\text{authentic}} + n_i^{\text{fake}} \cdot \bar{r}_{\text{fake}} / (N_i + n_i^{\text{fake}})$$

with $\Delta r_i^{\text{obs}}$ the observed rating change, $\Delta r_i^{\text{authentic}}$ the authentic rating change, $n_i^{\text{fake}}$ the injected fake-review count, $\bar{r}_{\text{fake}}$ the average fake-review rating, and $N_i$ the pre-injection authentic-review count. The equation shows that fake-review effectiveness depends on the ratio $n_i^{\text{fake}} / N_i$, which is highest for new or low-review-volume businesses and lowest for established high-review-volume businesses.

The detection signatures for individual fabrication include stylometric anomalies (deceptive text tends to over-use first-person pronouns, super-positive adjectives, and quality claims), temporal anomalies (concentrated review bursts inconsistent with the natural arrival rate), reviewer-history anomalies (reviewers with no prior activity or with review histories concentrated on the target business), and IP and device fingerprint anomalies (reviews originating from IP ranges or devices associated with the business owner or with review-service operators). The classifier-based detection takes the form the standard classification-performance metrics

$$\text{precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}, \quad \text{recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}, \quad F_1 = \frac{2 \cdot \text{precision} \cdot \text{recall}}{\text{precision} + \text{recall}}$$

with the classifier's decision threshold $\tau$ tuning the tradeoff between the two errors along the receiver-operating characteristic. The empirical detection accuracy under the [Ott et al 2011][research_ott_et_al_2011] framework reaches approximately ninety percent on the labeled crowdsourced corpus but degrades markedly on real-world reviews where the labeled ground truth is uncertain. The [Mukherjee et al 2013][research_mukherjee_et_al_2013] What Yelp Fake Review Filter Might Be Doing treatment reverse-engineers Yelp's production filter and estimates its precision at approximately eighty percent under the paper's evaluation methodology. The temporal-anomaly detection statistic for review-arrival bursts is captured by the standardized arrival-rate residual

$$z_{\text{burst}}(t) = \frac{\lambda(t) - \bar{\lambda}}{\sigma_\lambda}$$

with $\lambda(t)$ the observed review-arrival rate at time $t$, $\bar{\lambda}$ the historical mean arrival rate, and $\sigma_\lambda$ the historical standard deviation. Detection thresholds typically set $z_{\text{burst}} > 3$ as the anomaly trigger.

The platform countermeasures for individual fabrication include the classifier-based filters treated in the detection literature, verified-purchase requirements that constrain the review-eligible actor population, and post-hoc removal of reviews that trigger filter thresholds. The [Amazon Community Guidelines][ref_amazon_community_guidelines] establish the platform's anti-manipulation policy, and the [Amazon v Fake Review Brokers 2022][ref_amazon_v_fake_review_brokers_2022] private-action campaign has produced settlements with multiple marketplace intermediaries. The [Yelp Content Guidelines][ref_yelp_content_guidelines] establish parallel policy for the Yelp platform. The [Google Business Profile guidelines][ref_google_business_profile_guidelines] establish the parallel policy for Google Reviews. The [FTC 2024 Final Rule on Fake Reviews and Testimonials][ref_ftc_final_rule_2024] provides the federal regulatory framework that applies to individual fabrication as well as to the coordinated-campaign class. The [FTC v Bountiful Company 2023][ref_ftc_bountiful_2023] action addressed review-hijacking practice in which the target manufacturer moved product listings to inherit unrelated positive-review histories. The [FTC v Roomster 2022][ref_ftc_roomster_2022] action addressed a rental-listing platform's use of fake reviews to inflate listing reputation. The academic detection literature is supported by standing labeled datasets including the [Ott Deceptive Opinion Spam Corpus][ref_ott_deceptive_corpus] and the [YelpChi Fake Review Dataset][ref_yelpchi_dataset] that anchor the reproducibility of the detection-classifier evaluation.

### Coordinated Review Campaigns and Review Farming

Coordinated review campaigns extend individual fabrication to a coordinated operation that produces reviews at scale through multiple operator accounts. Review farming refers specifically to the industrialized production of reviews-for-hire through professional operator networks, with the operators recruited from labor markets in which the per-review compensation is competitive with alternative low-skilled remote work. The industry has been documented most extensively in the [He Hollenbeck Proserpio 2022][research_he_hollenbeck_proserpio_2022] Market for Fake Reviews treatment, which analyzed the exchange between Amazon sellers and organized fake-review Facebook groups. The paper documents approximately 1,500 sellers active in the fake-review marketplace during the 2020-2021 study period, with the reviews-for-purchase transactions involving free products in exchange for five-star reviews and follow-up cash payment.

The [Mayzlin Dover Chevalier 2014][research_mayzlin_dover_chevalier_2014] Promotional Reviews treatment compared Tripadvisor and Expedia hotel reviews and found systematic patterns consistent with hotels manipulating their own reviews on Tripadvisor (which permits unverified reviews) at higher rates than on Expedia (which requires booking-verified reviews). The rate-differential estimate provides the natural-experiment approach to prevalence estimation. The [Wu et al 2020][research_wu_et_al_2020] Fake Online Reviews Literature Review survey consolidates the empirical literature and identifies the aggregate prevalence range across studies.

The economics of review farming admit compact characterization. The marketplace price per fabricated review is approximately

$$p_{\text{fake-review}} \in [1, 30] \text{ USD per review}$$

with the lower bound reflecting text-only reviews on low-enforcement platforms and the upper bound reflecting verified-purchase reviews on high-enforcement platforms including sale-of-product cost. The producer surplus per manipulated business, absent detection, follows

$$\pi_i^{\text{manip}} = R_i^{\text{shift}} \cdot v \cdot Q_i - n_i \cdot p_{\text{fake-review}}$$

with $R_i^{\text{shift}}$ the rating shift produced by the injection, $v$ the per-rating-point revenue coefficient, $Q_i$ the sales volume elasticity, and $n_i$ the injected review count. The equation identifies the marginal return per additional fake review as the sales-volume increase net of the marginal fake-review production cost. International enforcement includes the [ACCC v Trivago 2020][ref_accc_v_trivago_2020] Australian case addressing misleading ranking practices, the [UK CMA fake reviews investigation 2022][ref_uk_cma_facebook_google_2022] into Facebook and Google fake-review markets, the [Canadian Competition Bureau v Amazon][ref_canada_amazon] fake-review enforcement, and the [Italian AGCM Booking.com fake reviews][ref_italy_agcm_booking] action. The temporal-arrival pattern of coordinated review campaigns is captured by the self-exciting Hawkes point process

$$\lambda(t) = \mu + \alpha \sum_{t_i < t} e^{-\beta(t - t_i)}$$

with $\mu$ the baseline arrival rate, $\alpha$ the self-excitation gain, and $\beta$ the decay rate. Coordinated-campaign arrivals exhibit $\alpha$ appreciably above the null-hypothesis baseline, producing the characteristic burst-and-decay pattern that admits detection via the [Xie et al 2012][research_xie_et_al_2012] temporal-pattern framework. The [Chevalier and Mayzlin 2006][research_chevalier_mayzlin_2006] Effect of Word of Mouth on Sales established the causal-effect literature for book sales; the subsequent [Chintagunta Gopinath Venkataraman 2010][research_chintagunta_gopinath_venkataraman_2010] treatment for movie box office and the [Anderson and Magruder 2012][research_anderson_magruder_2012] treatment for restaurant demand extended the account.

Detection signatures for coordinated review campaigns include the individual-fabrication signatures plus network-anomaly signatures. Coordinated reviews often exhibit temporal clustering (bursts of reviews arriving within hours or days), textual similarity (shared templates or paraphrased content), reviewer-graph clustering (reviewers who exclusively review the same set of businesses), and account-provenance clustering (accounts registered from the same IP range or with the same device fingerprint). The [Lim et al 2010][research_lim_et_al_2010] Detecting Product Review Spammers treatment introduced the reviewer-behavior graph-analysis approach. The [Wang et al 2011][research_wang_et_al_2011] Review Graph based Online Store Review Spammer Detection introduced the review-graph framework. The [Xie et al 2012][research_xie_et_al_2012] Review Spam Detection via Temporal Pattern Discovery introduced the temporal-anomaly framework. The [Fei et al 2013][research_fei_et_al_2013] Exploiting Burstiness in Reviews introduced the burst-detection framework. The [Rayana and Akoglu 2015][research_rayana_akoglu_2015] Collective Opinion Spam Detection introduced the network-embedding framework that combines review, reviewer, and product signals. The [Kumar et al 2017][research_kumar_et_al_2017] Understanding Rating Distributions provides the distributional-anomaly framework at scale.

The text-similarity detection statistic for coordinated review campaigns reduces to cosine similarity in an embedding space or via n-gram overlap. The n-gram-overlap statistic between two reviews $r_i$ and $r_j$ takes the form

$$\text{sim}_n(r_i, r_j) = \frac{|N_n(r_i) \cap N_n(r_j)|}{|N_n(r_i) \cup N_n(r_j)|}$$

with $N_n(r)$ the set of $n$-grams appearing in review $r$. Detection thresholds typically set $\text{sim}_n > 0.5$ for $n = 4$ as the coordination trigger. The reviewer-graph community-detection statistic can be characterized as the modularity function

$$Q = \frac{1}{2m} \sum_{ij} \left[A_{ij} - \frac{k_i k_j}{2m}\right] \delta(c_i, c_j)$$

with $A_{ij}$ the reviewer-business adjacency, $k_i$ the reviewer-degree, $m$ the total edge count, $c_i$ the community assignment, and $\delta(c_i, c_j)$ the community-match indicator. Coordinated-review clusters exhibit anomalously high $Q$ concentrated on small reviewer subsets, and the detection algorithm identifies suspicious clusters as high-$Q$ dense subgraphs. The academic detection accuracy under the network-based approaches reaches approximately ninety-five percent on labeled evaluation datasets but exhibits sizable degradation under adversarial adaptation as reviewers vary temporal patterns, textual patterns, and account behavior to evade detection. The [Malbon 2013][research_malbon_2013] Taking Fake Online Consumer Reviews Seriously legal treatment surveys the enforcement-response infrastructure.

### Sockpuppet-Driven Review Deposition

Sockpuppetry as a review-signal manipulation technique refers to the operation of multiple false identities by a single operator with the intent of producing reviews that appear to originate from distinct authentic reviewers. Sockpuppetry differs from coordinated review campaigns in that the sockpuppet operator maintains persistent identities over time rather than producing single-instance operator accounts, and the sockpuppet identities are typically constructed with more elaborate identity infrastructure than the throwaway accounts characteristic of ordinary coordinated campaigns.

The academic detection literature for sockpuppet identity operates through account-linkage analysis, including [Solorio et al 2014][research_solorio_et_al_2014] Sockpuppet Detection in Wikipedia authoring context, [Zheng et al 2011][research_zheng_et_al_2011] Detecting Sockpuppets in Deceptive Opinion Spam, and [Kumar et al 2017 An Army of Me][research_kumar_army_2017] on cross-community sockpuppet behavior. The [Tsikerdekis and Zeadally 2014][research_tsikerdekis_zeadally_2014] Multiple Account Identity Deception Detection treatment surveys the field.

The economic structure of sockpuppet operations differs from ordinary coordinated campaigns in the amortization of identity-construction cost. Sockpuppet identity construction requires per-identity investment in profile buildout, activity history, and behavioral patterns, and the marginal identity cost falls with automation. The identity-construction cost permits characterization as

$$C_{\text{sockpuppet}}(n) = c_{\text{fixed}} + n \cdot c_{\text{marginal}}(n)$$

with $c_{\text{fixed}}$ the setup cost of the sockpuppet operation and $c_{\text{marginal}}(n)$ the per-identity marginal cost that typically decreases in $n$ due to tooling automation. Professional sockpuppet operations achieve per-identity marginal costs in the range of

$$c_{\text{marginal}} \in [0.5, 10] \text{ USD per identity}$$

when the identity is used for review deposition rather than for higher-fidelity applications requiring KYC-style identity documentation. Cross-account behavioral-similarity detection operates through the standardized similarity metric

$$s_{ij}^{\text{behav}} = \frac{\langle \mathbf{f}_i, \mathbf{f}_j\rangle}{\|\mathbf{f}_i\| \cdot \|\mathbf{f}_j\|}$$

with $\mathbf{f}_i$ the behavioral-feature vector for account $i$ combining posting-time distribution, session-length distribution, device-fingerprint hash, and IP-address entropy. Sockpuppet-account pairs exhibit anomalously high $s_{ij}^{\text{behav}}$, and the account-linkage detection identifies suspicious pairs above a chosen threshold. The corresponding posterior for sockpuppet-linkage given the similarity is

$$\Pr(\text{sockpuppet}_{ij} \mid s_{ij}^{\text{behav}}) = \frac{p(s_{ij} \mid \text{link}) \pi_{\text{link}}}{p(s_{ij} \mid \text{link}) \pi_{\text{link}} + p(s_{ij} \mid \neg \text{link})(1 - \pi_{\text{link}})}$$

with $\pi_{\text{link}}$ the base-rate prior of sockpuppet linkage in the population. The persistence-over-time of a sockpuppet identity under active platform enforcement has the form the survival function

$$S(t) = \Pr(\text{account active at } t) = e^{-\int_0^t h(\tau) d\tau}$$

with $h(\tau)$ the hazard rate combining passive-account decay and platform-enforcement removal. Persistent sockpuppet operations sustain $S(t)$ close to unity through operational discipline (avoiding detection triggers) and through operational-scale replacement of removed accounts. The composite multi-feature detection likelihood ratio combining behavioral similarity, activity-pattern similarity, and content similarity takes the form

$$\Lambda_{ij}^{\text{sockpuppet}} = \prod_{k \in \text{features}} \frac{p(f_k^{ij} \mid \text{link})}{p(f_k^{ij} \mid \neg \text{link})}$$

under the standard conditional-independence assumption, with the accumulated log-likelihood serving as the aggregate detection statistic.

### Generative-Model-Produced Review Content

The recent generative-model transition has greatly altered the review-signal manipulation landscape. Large-language-model deployment since the [OpenAI ChatGPT release 2022][ref_openai_chatgpt_2022] and subsequent [GPT-4 release 2023][ref_openai_gpt4_2023] has reduced the marginal cost of producing human-quality review text to near-zero, which shifts the economic first-order condition toward much higher equilibrium review-manipulation volume absent compensating detection improvements. The [Yao et al 2017][research_yao_et_al_2017] Automated Crowdturfing Attacks and Defenses initial demonstration established that neural-model-generated review text could evade contemporary detectors; the subsequent [Zellers et al 2019][research_zellers_et_al_2019] Grover paper on generative attacks and defenses established the deeper theoretical framework.

The empirical assessment of LLM-generated review detection includes [Sohail et al 2024][research_sohail_et_al_2024] on large-language-model generated review detection, [Sadasivan et al 2023][research_sadasivan_et_al_2023] Can AI-Generated Text be Reliably Detected on the fundamental detection difficulty, and the [Kirchenbauer et al 2023][research_kirchenbauer_et_al_2023] Watermarking for Large Language Models treatment on the emerging watermark-based detection approach. The composite empirical picture indicates that LLM-generated review text produced by contemporary models can achieve human-classification-error rates below fifty percent under contemporary human-and-classifier detection, which effectively defeats the detection layer under the assumption that the model is prompted to produce text that resembles the target distribution.

The manipulation-cost function under generative-model deployment satisfies approximately

$$c_{\text{LLM-review}}(m) \approx c_{\text{API}} \cdot m + c_{\text{prompt-eng}}$$

with $c_{\text{API}}$ the per-review API cost in the range of $10^{-3}$ to $10^{-2}$ USD per generation, $c_{\text{prompt-eng}}$ the fixed prompt-engineering setup cost, and $m$ the injection volume. The equation makes clear that the convexity exponent $\alpha$ of the classical manipulation-cost function has effectively collapsed to unity, which shifts the manipulation equilibrium considerably toward higher intensity. The [C2PA content provenance standard][ref_c2pa_standard] and the [Meta AI-generated content labeling policy][ref_meta_ai_content_labeling] represent the emerging technical and policy countermeasure infrastructure. The [Coalition for Content Provenance and Authenticity][ref_c2pa_coalition] provides the multi-stakeholder governance forum. The [Sadasivan et al 2023][research_sadasivan_et_al_2023] impossibility-adjacent result establishes that under sufficient generation-quality the detection accuracy approaches the random-baseline bound

$$\text{AUC}_{\text{detect}}(q_{\text{gen}}) \to 0.5 \text{ as } q_{\text{gen}} \to q_{\text{human}}$$

with $q_{\text{gen}}$ the generative-model quality and $q_{\text{human}}$ the human-authored baseline distribution. The watermarking approach in [Kirchenbauer et al 2023][research_kirchenbauer_et_al_2023] introduces a bias in the generation distribution that preserves detection accuracy at the cost of small utility loss, admitting characterization as the signed information-content deviation

$$I_{\text{watermark}}(x) = \log \frac{p_{\text{watermarked}}(x)}{p_{\text{unmarked}}(x)}$$

with the watermarked-versus-unmarked likelihood ratio serving as the detection statistic. The complementary perplexity-based detection statistic operates on the intuition that generative-model output exhibits systematically lower perplexity under the reference model than authentic human text,

$$\text{PPL}(x) = \exp\left(-\frac{1}{|x|} \sum_{i} \log p_{\text{ref}}(x_i \mid x_{<i})\right)$$

with the detection thresholding on $\text{PPL}(x) < \tau_{\text{PPL}}$. The paraphrase-attack degradation of watermarking allows characterization via the bit-error-rate under paraphrase transformation

$$\text{BER}_{\text{para}}(x, x') = \frac{|\{i : w_i(x) \neq w_i(x')\}|}{|w(x)|}$$

with $w(x)$ the recovered watermark bits and $x'$ the paraphrased text. The generative-model countermeasure landscape remains unresolved and is treated further in the closing article.

## Follower and Engagement Manipulation Techniques

The engagement-signal manipulation class comprises techniques oriented at the follower counts, engagement metrics (likes, comments, shares, saves, views), and algorithmic-amplification signals that social-media platforms make available. The class is empirically dominant on social platforms and has received appreciable academic detection attention.

### Follower Purchase Economies

Follower purchase refers to the acquisition of follower-count on a social-media account through paid services that create or reassign accounts to follow the buyer. The industry has operated at commercial scale since approximately 2010 and has produced a mature marketplace with per-follower pricing well below one cent for low-quality (bot) followers and up to several cents for medium-quality (aged, semi-active) followers. The [De Micheli and Stroppa 2013][research_demicheli_stroppa_2013] Twitter and the Underground Market documented the initial follower-purchase economy. The [Stringhini et al 2013][research_stringhini_et_al_2013] Follow the Green Growth and Dynamics in Twitter Follower Markets treatment documented the follower-purchase-service infrastructure. The [Cresci et al 2015][research_cresci_et_al_2015] Fame for Sale treatment analyzed the population dynamics of purchased followers. The [Bilton 2014][ref_bilton_2014_nyt_followers] New York Times investigation documented the follower-purchase practices of prominent Twitter accounts.

The pricing structure of follower purchase reduces to approximately

$$p_{\text{follower}} \in [10^{-4}, 10^{-2}] \text{ USD per follower}$$

with the lower bound reflecting low-quality bot followers on high-tolerance platforms and the upper bound reflecting medium-quality followers on higher-enforcement platforms. The [NY Attorney General v Devumi 2019][ref_ny_ag_devumi_2019] enforcement action addressed a follower-purchase marketplace with documented revenue of approximately fifteen million USD across approximately four years of operation, with per-follower prices in the range of one to two cents. The [FTC v Devumi 2019][ref_ftc_devumi_2019] parallel federal action established the FTC's application of Section 5 to the follower-purchase industry.

The empirical prevalence of purchased followers on major social platforms varies by platform and account category. Contemporary estimates from platform-integrity reporting and academic detection studies place the fraction of purchased or otherwise inauthentic followers on major social platforms in the range

$$p_{\text{fake-follower}} \in [0.05, 0.30]$$

for typical accounts and higher for accounts in categories with high follower-count commercial value (influencer marketing, cryptocurrency promotion, political mobilization). The [Meta Adversarial Threat Report][ref_meta_atr] and the [X Transparency Report][ref_x_transparency_report] provide the platform-industry disclosure.

The detection signatures for purchased followers include the individual bot-account signatures documented in [Cresci 2020][research_cresci_2020] and [Yang et al 2020][research_yang_et_al_2020], plus follower-graph anomalies including sudden follower-count increases inconsistent with organic growth patterns, follower-account clustering (many followers exhibiting similar creation patterns and behavioral signatures), and geographic-anomaly patterns (followers concentrated in click-farm-associated geographies). The [X Platform Manipulation and Spam Policy][ref_x_platform_manipulation_policy] and the [Instagram Community Guidelines authenticity section][ref_instagram_authenticity_guidelines] establish the platform-side policy framework. The academic detection literature is supported by standing datasets including the [Cresci-2015 Fake Followers Dataset][ref_cresci_2015_dataset] and the [Cresci-2017 Genuine and Spambot Dataset][ref_cresci_2017_dataset] that provide labeled bot and human account samples, and the [Bot Repository Indiana OSoMe][ref_bot_repository] that consolidates the field's standing reference corpora. Follower-to-engagement-ratio anomaly is a standard detection statistic characterizing the mismatch between purchased inauthentic followers and authentic engagement on the buyer's content,

$$\rho_i^{\text{follow-engage}} = \frac{\bar{e}_i}{F_i}$$

with $\bar{e}_i$ the mean per-post engagement and $F_i$ the follower count. Accounts with purchased followers exhibit anomalously low $\rho^{\text{follow-engage}}$ compared to authentic-follower baselines in the same account category. The organic-follower-growth rate follows a logistic trajectory characterized by

$$\frac{dF_i}{dt} = r \, F_i \left(1 - \frac{F_i}{K}\right)$$

with $r$ the growth-rate parameter and $K$ the account-specific ceiling. Purchase-driven follower-count changes appear as step-function perturbations to the logistic trajectory, admitting detection via change-point analysis. The purchased-follower survival distribution over time exhibits characteristic decay as platform detection removes accounts,

$$S_{\text{purchased}}(t) = e^{-\lambda_{\text{enforce}} t} \cdot S_{\text{purchased}}(0)$$

with $\lambda_{\text{enforce}}$ the platform's per-account removal hazard for detected purchased followers. Contemporary platform enforcement produces half-lives on the order of weeks-to-months for detected purchased followers, which explains the observed post-purchase follower-count decay pattern on major social platforms. The [Cresci et al 2017][research_cresci_et_al_2017] Paradigm-Shift of Social Spambots treatment documents the technique-evolution history and the corresponding detection-adaptation dynamic.

### Engagement Purchase and Coordinated Engagement Pods

Engagement purchase extends the follower-purchase model to the transactional engagement signals (likes, comments, shares, saves, story views, video views) that platforms use as inputs to ranking algorithms. The marketplace pricing per engagement action is generally in the range

$$p_{\text{engagement}} \in [10^{-4}, 10^{-2}] \text{ USD per action}$$

with per-action pricing structured similarly to follower purchase. Engagement pods are a distinct organizational form in which participants coordinate to exchange authentic engagement on each other's content, which produces authentic account signal but inauthentic content-quality signal from the platform's perspective. The [Weerkamp and de Rijke 2012][research_weerkamp_derijke_2012] Credibility-Inspired Ranking treatment surveys the underlying algorithmic assumptions that pod coordination exploits.

The [Ellis Ott 2018][ref_ellis_ott_2018_pods] The Atlantic investigation documented the Instagram engagement-pod economy and the participation-rate estimates within influencer categories. The [Meta Community Standards on Inauthentic Behavior][ref_meta_cib_policy] establishes the platform-side policy framework for engagement manipulation. The [Ferrara et al 2016][research_ferrara_et_al_2016] Rise of Social Bots treatment provides the foundational empirical treatment of automated engagement production. The [Papakyriakopoulos et al 2020][research_papakyriakopoulos_et_al_2020] Political Communication on Social Media treatment addresses the political-engagement-manipulation adjacent literature. The [Nielsen Trust in Advertising Global Report][ref_nielsen_trust_advertising] provides the industry-side survey evidence on consumer trust in different reputation-signal categories that shapes the incentive to manipulate engagement metrics.

The detection signatures for engagement-purchase include the temporal-anomaly patterns (engagement bursts inconsistent with the natural arrival rate for content of the observed quality), the engagement-source-account signatures (bot-account signatures for automated engagement, click-farm-account signatures for human engagement), and the engagement-content-mismatch patterns (engagement content unrelated to the target content). The detection of engagement pods requires different signatures because the participating accounts are authentic and the engagement content is often plausible. Pod detection typically relies on graph-clustering of the engagement pattern and on the account-clustering of frequent pod participants. Pod participation supports characterization via the reciprocity-and-clustering coefficient over the account-engagement graph,

$$\rho_{\text{pod}}(G) = \frac{|\{(i,j) : (i \to j) \wedge (j \to i)\}|}{|E(G)|} \cdot C(G)$$

with the first factor the reciprocity ratio (fraction of engagement edges that are mutual) and $C(G)$ the graph clustering coefficient. Pod-participating account subgraphs exhibit anomalously high $\rho_{\text{pod}}$ compared to the platform-baseline distribution. The [Weller et al 2019][research_weller_et_al_2019] Understanding Cross-Platform Sharing and Engagement Pod Dynamics treatment provides the initial academic characterization.

### View-Count and Impression Inflation

View-count inflation on video platforms including YouTube and TikTok operates through automated view-generation infrastructure that plays videos through bot-controlled accounts or through click-farm operators. The [YouTube view-count manipulation policy][ref_youtube_view_manipulation_policy] establishes the platform's response framework. The [Zannettou et al 2018][research_zannettou_et_al_2018] Understanding Web Archiving Services and Their Application treatment surveys the adjacent technical infrastructure.

Impression inflation on display-advertising platforms operates through the ad-fraud infrastructure documented in [Pearce et al 2014][research_pearce_et_al_2014] Characterizing Large-Scale Click Fraud in ZeroAccess and the [White Ops Methbot report 2016][ref_white_ops_methbot_2016] documenting a large-scale programmatic-advertising fraud operation. The [IAB Ad Fraud Report][ref_iab_ad_fraud_report] and the [MRC Media Rating Council Viewability Standards][ref_mrc_viewability_standards] provide the industry-side reference framework. Impression inflation intersects with reputation manipulation where the inflated impressions produce social-proof signals used in downstream ranking or reputation contexts. View-fraud detection typically operates on the IP-diversity Shannon entropy of the view-source distribution,

$$H_{\text{view-source}} = -\sum_{a} p_a \log p_a$$

with $p_a$ the fraction of views originating from address block $a$. Authentic views produce high $H_{\text{view-source}}$ close to the platform's user-population baseline; view-fraud operations often produce anomalously low $H_{\text{view-source}}$ concentrated on a small set of infrastructure-associated address blocks.

## Search-Ranking Manipulation Techniques

The search-ranking manipulation class comprises techniques oriented at the ranking-position signal on search engines, app stores, and content-discovery platforms. The class differs from the review-and-engagement classes in that the ranking-position signal is emitted by the platform's ranking algorithm rather than by discrete signal-injection events, and manipulation therefore operates through gaming of the algorithm's inputs rather than through direct signal injection.

### Aggressive SEO at the Manipulative End

Search-engine optimization (SEO) covers a broad practitioner spectrum from legitimate technical optimization through aggressive gaming to spam. The manipulative end of the spectrum includes techniques including keyword stuffing (inserting search-target keywords at above-natural density), doorway pages (pages built to rank for queries and redirect to the target destination), cloaking (serving different content to search-engine crawlers than to human visitors), link-farm participation (coordinated cross-linking among sites to inflate PageRank-style ranking signals), private-blog-network operation (operating a network of sites appearing independent but under common control to produce artificial backlinks), and content-scraping and republication with keyword substitution.

The [Google Webmaster Guidelines][ref_google_webmaster_guidelines] establish the platform's SEO policy and delimit the manipulative-technique boundary from the platform's perspective. The [Google Search Central spam policies][ref_google_search_spam_policies] provide the current-version taxonomy. The [Cutts Google Webmaster Central Blog archives][ref_cutts_google_blog] provide the historical record of technique classifications. The [Google 2011 Panda algorithm update][ref_google_panda_2011] and the [Google 2012 Penguin algorithm update][ref_google_penguin_2012] represent major detection-and-enforcement events that significantly reshaped the SEO industry through platform-side algorithmic response to manipulative techniques.

The PageRank algorithm underlying much of the ranking-signal architecture is treated in [Page and Brin 1998][research_page_brin_1998] The Anatomy of a Large-Scale Hypertextual Web Search Engine and the extended [Page Brin Motwani Winograd 1999][research_page_brin_motwani_winograd_1999] treatment. Manipulation targets the PageRank recurrence

$$\text{PR}(p) = \frac{1 - d}{N} + d \sum_{q \in B_p} \frac{\text{PR}(q)}{L(q)}$$

with $\text{PR}(p)$ the PageRank of page $p$, $B_p$ the set of pages linking to $p$, $L(q)$ the outbound link count of $q$, $d$ the damping factor typically set near 0.85, and $N$ the total page count. Manipulation operates through construction of $B_p$ (the inbound-link set) to inflate the summed PageRank contribution, which in turn increases the target page's rank position on subsequent search queries.

The [Gyongyi Garcia-Molina 2005][research_gyongyi_garciamolina_2005] Web Spam Taxonomy treatment classified the manipulation-technique inventory circa 2005 and remains the reference classification. The [Ntoulas et al 2006][research_ntoulas_et_al_2006] Detecting Spam Web Pages through Content Analysis introduced the content-based detection framework. The [Castillo et al 2007][research_castillo_et_al_2007] Know Your Neighbors Web Spam Detection using the Web Topology introduced the graph-topology detection framework. The PageRank-manipulation return per additional inbound link can be characterized as the marginal derivative

$$\frac{\partial \text{PR}(p)}{\partial |B_p|} = \frac{d}{|B_p| + 1} \cdot \bar{\text{PR}}_{B_p}$$

with $\bar{\text{PR}}_{B_p}$ the average PageRank of the inbound-link set. The ranking-position shift produced by a rank increase depends on the density of the local rank-neighborhood and follows approximately

$$\Delta \text{rank} \approx -\frac{\partial N_{<\rho}}{\partial \rho} \cdot \Delta \rho$$

with $N_{<\rho}$ the count of pages with rank score below $\rho$ and $\Delta \rho$ the rank-score change. The click-through gain from a position shift follows the position-decay characterization of the framing article. The [TrustRank propagation algorithm][ref_gyongyi_2004_trustrank_paper] extension proposed in the anti-spam literature propagates trust from a seed set of hand-labeled trusted pages via the recurrence

$$t(p) = (1 - d) \, \mathbb{1}[p \in S_{\text{seed}}] + d \sum_{q \in B_p} \frac{t(q)}{L(q)}$$

with $S_{\text{seed}}$ the trusted-seed set and the trust score $t(p)$ decaying with graph distance from the seed. Spam-oriented sites typically receive low $t(p)$ due to weak connectivity to the trusted seed, admitting detection via the trust-rank threshold. Cloaking detection operates on the differential between the content served to the search-engine crawler and the content served to human visitors,

$$\Delta_{\text{cloak}}(p) = d_{\text{content}}(C_{\text{crawler}}(p), C_{\text{human}}(p))$$

with $d_{\text{content}}$ a content-distance metric and $C_{\cdot}(p)$ the content served to the respective user-agent class.

### App-Store Optimization Gaming

App-store optimization (ASO) gaming targets the ranking algorithms on the [Apple App Store][ref_apple_app_store_review_guidelines] and [Google Play Store][ref_google_play_developer_policy]. Techniques include keyword manipulation in app metadata, download-count inflation through automated or click-farm-driven downloads, and review manipulation through the mechanisms treated in the review-manipulation class above. Download-velocity manipulation admits detection via the standardized deviation

$$z_{\text{download}}(t) = \frac{D(t) - \bar{D}_{\text{category}}(t)}{\sigma_{D,\text{category}}(t)}$$

with $D(t)$ the app's download rate at time $t$ and $\bar{D}_{\text{category}}$, $\sigma_{D,\text{category}}$ the category-baseline moments. Manipulation-driven download bursts produce $z_{\text{download}}$ above the anomaly threshold typically set at $z > 3$. The [Ali et al 2017][research_ali_et_al_2017] Same Same but Different Search Advertising and Users' Attention treatment surveys the ranking-algorithm-adjacent research. The [D'Ambrosio et al 2018][research_dambrosio_et_al_2018] treatment analyzes the app-review manipulation ecosystem.

## Coordinated Inauthentic Behavior at Network Scale

Coordinated inauthentic behavior (CIB) refers to the class of manipulation operations that operate through networks of accounts under coordinated control, with the coordination oriented at producing signal at scales inaccessible to individual or small-team operators. The term traces to the [Meta Coordinated Inauthentic Behavior policy][ref_meta_cib_policy] framework and has been adopted broadly across the platform-integrity industry.

### Sockpuppet Networks and Sybil Attacks

Sybil attacks refer to the technical variant of sockpuppetry in which the false identities are created and maintained at scale through automated infrastructure. The term traces to [Douceur 2002][research_douceur_2002] The Sybil Attack in the peer-to-peer systems literature. The technique has migrated to social-media reputation systems where it operates through automated account creation, automated identity buildout, and automated activity generation.

The Sybil-detection literature includes [Yu et al 2006][research_yu_et_al_2006] SybilGuard Defending Against Sybil Attacks via Social Networks, [Yu et al 2008][research_yu_et_al_2008] SybilLimit A Near-Optimal Social Network Defense against Sybil Attacks, [Danezis and Mittal 2009][research_danezis_mittal_2009] SybilInfer Detecting Sybil Nodes using Social Networks, [Cao et al 2012][research_cao_et_al_2012] Aiding the Detection of Fake Accounts in Large Scale Social Networks, and [Alvisi et al 2013][research_alvisi_et_al_2013] SoK The Evolution of Sybil Defense via Social Networks. The [Yu et al 2006][research_yu_et_al_2006] SybilGuard framework establishes the bound on Sybil-region size under the random-walk-mixing-time assumption

$$|S_{\text{Sybil}}| \leq O(\sqrt{n \log n})$$

with $n$ the honest-region size, subject to the assumption that Sybil-honest graph attack-edges are bounded and that the honest region is fast-mixing. The Sybil-detection statistic based on graph conductance identifies the Sybil-region cut as the minimum-conductance partition

$$\Phi(S) = \frac{|E(S, \bar{S})|}{\min(|E(S)|, |E(\bar{S})|)}$$

with the Sybil region admitting characterization as the subset $S$ that achieves anomalously low $\Phi(S)$ relative to the null-model conductance distribution. The detection accuracy under the social-graph-based approaches depends on the assumption that Sybil accounts have limited authentic-account connections; the assumption has weakened as Sybil operators have invested in constructing plausible connection graphs.

The economic characterization of a Sybil operation includes the identity-construction cost treated above plus the ongoing maintenance cost for activity generation. The aggregate Sybil-network operation cost permits characterization as

$$C_{\text{Sybil}}(N, T) = c_{\text{setup}} + N \cdot (c_{\text{ident}} + T \cdot c_{\text{activity}})$$

with $N$ the network size, $T$ the operational time horizon, $c_{\text{setup}}$ the operation-level fixed cost, $c_{\text{ident}}$ the per-identity construction cost, and $c_{\text{activity}}$ the per-identity per-unit-time activity cost. Professional Sybil operations at contemporary marketplace scale achieve unit costs supporting network sizes in the range

$$N \in [10^3, 10^6] \text{ Sybil accounts per operation}$$

with the upper bound reached by state-sponsored or well-funded commercial operators.

### Cross-Platform Amplification Rings

Cross-platform amplification rings operate through coordinated content-sharing and engagement across multiple platforms with the intent of producing reinforcing amplification signal across the platform ecosystem. The technique differs from single-platform CIB in that detection and enforcement infrastructure is generally platform-specific, and cross-platform coordination therefore escapes single-platform detection even when each individual platform's activity would be detectable by that platform's classifiers.

The [Bradshaw and Howard 2019][research_bradshaw_howard_2019] Global Disinformation Order treatment surveys the cross-platform information-operation landscape. The [DiResta et al 2019][research_diresta_et_al_2019] Tactics and Tropes of the Internet Research Agency treatment documents the cross-platform operations of the Russian Internet Research Agency across Facebook, Twitter, Instagram, YouTube, and other platforms. The [Zannettou et al 2019][research_zannettou_et_al_2019] Disinformation Warfare Understanding State-Sponsored Trolls treatment analyzes the cross-platform information-operation graph. The [Starbird 2019][research_starbird_2019] Disinformation's Spread Bots Trolls and All of Us treatment provides the theoretical framing.

Cross-platform amplification produces content-appearance-correlation across platforms that allows detection through the cross-platform Pearson correlation of content appearance timestamps

$$r_{\text{cross}}(P_1, P_2) = \frac{\sum_c (t_c^{P_1} - \bar{t}^{P_1})(t_c^{P_2} - \bar{t}^{P_2})}{\sqrt{\sum_c (t_c^{P_1} - \bar{t}^{P_1})^2 \sum_c (t_c^{P_2} - \bar{t}^{P_2})^2}}$$

with $t_c^{P}$ the timestamp of content $c$ appearing on platform $P$. Coordinated cross-platform amplification produces $r_{\text{cross}}$ close to unity for tightly coordinated operations. The amplification-cascade decay follows the reach recurrence

$$R_{\text{cascade}}(t+1) = R_{\text{cascade}}(t) \cdot \eta \cdot (1 - \frac{R_{\text{cascade}}(t)}{\bar{R}})$$

with $\eta$ the per-step amplification gain and $\bar{R}$ the reach ceiling set by the audience-network size. Cross-platform detection requires cross-platform data-sharing infrastructure that has developed slowly due to platform competition and privacy considerations. The [Global Internet Forum to Counter Terrorism (GIFCT)][ref_gifct] and the [Meta Threat Report cross-platform sections][ref_meta_atr] represent the emerging cross-platform coordination infrastructure. The academic [Cross-Platform Sharing Dataset][ref_cross_platform_sharing_dataset] provides one standing empirical resource.

### Click Farms and Human-Operator Networks

Click farms refer to the physical or virtual facilities in which human operators produce engagement, reviews, or other reputation signals at commercial scale. The industry has been documented most extensively in the [Cushing 2013][ref_cushing_2013_click_farm] Wired investigation of Bangladesh click-farm operations and in subsequent journalistic and academic treatments. The [Farooqi et al 2017][research_farooqi_et_al_2017] Characterizing Key Stakeholders in an Online Black Market analyzes the click-farm labor market. The [Motoyama et al 2011][research_motoyama_et_al_2011] Dirty Jobs The Role of Freelance Labor in Web Service Abuse treatment establishes the labor-market characterization.

Click farm operations occupy an intermediate detection difficulty because the individual operator actions are authentic human actions from an identity and behavioral perspective; the manipulation signature emerges at the operator-network scale in the patterns of task assignment and coordination. The [Wang et al 2012][research_wang_et_al_2012] Serf and Turf Crowdturfing for Fun and Profit treatment provides the academic characterization of the crowdturfing marketplace.

The throughput characterization of a click farm supports estimation as

$$\Lambda_{\text{click-farm}} = N_{\text{operator}} \cdot h \cdot r$$

with $N_{\text{operator}}$ the operator count, $h$ the hours per operator per day, and $r$ the actions per operator-hour. Contemporary click farms achieve throughput in the range

$$\Lambda \in [10^4, 10^6] \text{ actions per day per operation}$$

with the upper bound reached by large industrial operations. The task-queuing model for click-farm operations follows the standard M/M/c queue characterization

$$L_q = \frac{(N_{\text{op}} \rho)^{N_{\text{op}}} \rho}{N_{\text{op}}! (1 - \rho)^2} P_0$$

with $\rho$ the operator utilization, $N_{\text{op}}$ the operator count, and $P_0$ the probability of zero queue occupancy, and provides the throughput-versus-latency tradeoff characterization for the operation-management perspective. Geographic-anomaly detection for click-farm-originating activity operates on the geographic entropy of the account-origin distribution restricted to click-farm-associated regions,

$$H_{\text{geo}}^{\text{restrict}} = -\sum_{g \in G_{\text{cf}}} p_g \log p_g$$

with $G_{\text{cf}}$ the set of click-farm-associated geographic regions and $p_g$ the fraction of activity originating from region $g$. Click-farm-heavy operations exhibit anomalously low $H_{\text{geo}}^{\text{restrict}}$ concentrated on small operator-hub subsets of $G_{\text{cf}}$.

### State-Sponsored Operations Extending to Commercial Reputation

State-sponsored information operations documented in [DiResta et al 2019][research_diresta_et_al_2019], [Rid 2020][book_rid_2020] Active Measures, and the [Mueller Report 2019][ref_mueller_report_2019] Volume One primarily target political outcomes but produce spillover effects on commercial reputation through the operations' amplification of commercial narratives, disparagement of commercial actors, and creation of adversarial-content ecosystems that individual commercial actors then engage with as a background environment. State-attribution inference from technical fingerprints (infrastructure reuse, code fingerprints, operational-security patterns, language-and-timezone signatures) has the form the Bayesian posterior

$$\Pr(\text{state} = s \mid \mathbf{F}) = \frac{\Pr(\mathbf{F} \mid s) \pi(s)}{\sum_{s'} \Pr(\mathbf{F} \mid s') \pi(s')}$$

with $\mathbf{F}$ the observed fingerprint vector and $\pi(s)$ the prior over candidate state actors. The [Bradshaw Bailey Howard 2021][research_bradshaw_bailey_howard_2021] Industrialized Disinformation cross-national survey characterizes the scale of state-sponsored operations. The [Bright et al 2020][research_bright_et_al_2020] Coordinated Behavior on Social Media treatment surveys the coordinated-behavior detection literature applicable across political and commercial contexts.

## Astroturfing and Grassroots Manufacturing

Astroturfing refers to the manipulation practice of manufacturing apparent grassroots support for a person, product, position, or narrative. The term traces to Senator Lloyd Bentsen's 1985 characterization of manufactured constituent mail as artificial grass in the [Bentsen 1985 Congressional Record][ref_bentsen_congressional_record_1985]. Astroturfing overlaps with review manipulation and coordinated inauthentic behavior but is analytically distinct in that its objective is the manufacture of the appearance of authentic public support rather than the direct manipulation of a discrete reputation score.

### Corporate Astroturfing

Corporate astroturfing operations have been documented across the tobacco, oil, pharmaceutical, and food industries. The [Oreskes and Conway 2010][book_oreskes_conway_2010] Merchants of Doubt treatment documents the coordinated denial campaigns on tobacco, ozone depletion, acid rain, and climate change organized by tobacco-industry-adjacent operators and subsequently adopted by the oil industry. The [McGarity and Wagner 2008][book_mcgarity_wagner_2008] Bending Science documents the corporate manufacture of doubt through funded academic work and coordinated advocacy. The [Michaels 2008][book_michaels_2008] Doubt Is Their Product documents the corporate manufactured-doubt playbook. The [Miller 2004][ref_miller_2004_walmart] documentation of the Working Families for Wal-Mart astroturf organization illustrates the corporate-astroturf technique. The [Walker 2014][book_walker_2014] Grassroots for Hire treatment consolidates the contemporary industry analysis.

The corporate-astroturfing detection signatures include coordination patterns across ostensibly independent voices, funding-trail patterns linking apparent grassroots organizations to corporate funding, message-timing patterns showing coordinated release across the astroturfed voice population, and text-similarity patterns showing shared templates. The astroturf-coordination z-score for release-timing anomaly follows

$$z_{\text{coord}} = \frac{\text{(observed simultaneous releases)} - \mu_{\text{null}}}{\sigma_{\text{null}}}$$

with $\mu_{\text{null}}$ and $\sigma_{\text{null}}$ the null-hypothesis distribution parameters under an independent-release model. Astroturf operations typically exhibit $z_{\text{coord}} > 5$ during active-campaign windows. The [Cho et al 2011][research_cho_et_al_2011] Astroturfing detection framework introduced the academic detection methodology. The [Ratkiewicz et al 2011][research_ratkiewicz_et_al_2011] Detecting and Tracking Political Abuse in Social Media (Truthy) introduced the social-media-specific detection framework.

### Political Astroturfing

Political astroturfing operates through similar techniques as corporate astroturfing but with objectives oriented at electoral, policy, or narrative outcomes. The [King Pan Roberts 2017][research_king_pan_roberts_2017] How the Chinese Government Fabricates Social Media Posts documents the Chinese "50 Cent Army" state-directed social-media astroturfing at scale, estimating an aggregate volume of approximately

$$V_{\text{50-cent}} \approx 4.4 \times 10^8 \text{ posts per year}$$

concentrated in strategic distraction rather than in engaged argument. The coordinated-posting-timing signature is described by the concentration statistic

$$\text{Conc}(\Delta t) = \frac{|\{p : t_p \in [\Delta t]\}|}{|\text{posts}|}$$

with $\Delta t$ a short time window aligned with the operational schedule of the astroturf operators; coordinated operations exhibit anomalously high $\text{Conc}$ within operational time windows aligned with the operators' work schedules. The [Woolley and Howard 2018][book_woolley_howard_2018] Computational Propaganda edited volume surveys the cross-national political-astroturfing landscape. The [Aral 2020][book_aral_2020] Hype Machine consolidates the empirical evidence on political manipulation effects.

### Front-Organization Structures

Astroturfing at organizational scale often operates through purpose-built front organizations that appear to be independent civil-society, grassroots, or expert organizations but are in fact organized and funded by principal-party interests. The [Levick and Slavo 2015][ref_levick_slavo_2015] documentation of front-organization structures illustrates the pattern. The [Fang 2013][ref_fang_2013_koch] investigation of the Koch-network affiliated organizations documents the funding-and-coordination structure. The [Souls of Distortion 2016 catalog of front organizations][ref_source_watch_front] operated by the Center for Media and Democracy provides one standing reference resource.

## Credential and Identity Fabrication

Credential and identity fabrication operates through the direct construction of false professional credentials, educational credentials, work-history claims, or identity attributes with the intent of augmenting the actor's reputation through the credentials' implicit endorsement.

### Verified-Badge Acquisition

Platform verified-badge programs including the [Twitter Verification legacy program][ref_twitter_verification_legacy], the [Instagram Verified badge][ref_instagram_verified], the [LinkedIn ID Verification][ref_linkedin_verification], and the [YouTube channel verification][ref_youtube_verification] provide platform-issued reputation signals intended to authenticate account identity or notability. The badges have been targeted by manipulation operations that acquire badges through documentation fabrication, insider access, or purchase from insider brokers. The [Musk-era Twitter Blue paid verification][ref_x_blue] represents the shift from earned to purchased verification on that platform, with the resulting signal-informativeness decline documented in [Marino et al 2023][research_marino_et_al_2023] Effects of Removing Twitter Blue Verification. The signal-informativeness delta produced by the earned-to-paid transition is described by the mutual-information change

$$\Delta I_{\text{verify}} = I(\text{authentic} ; \text{badge}_{\text{earned}}) - I(\text{authentic} ; \text{badge}_{\text{paid}})$$

with the first term the mutual information between the authenticity-attribute and the earned-verification badge and the second term the analogous quantity for the paid-verification badge. Empirical estimates from the [Marino et al 2023][research_marino_et_al_2023] treatment indicate $\Delta I_{\text{verify}} > 0$ substantially, reflecting the informativeness collapse under the transition.

### Professional-Credential Fabrication

Professional-credential fabrication operates through claims of academic degrees, professional certifications, employment history, or awards that are not held by the claimant. The academic-degree-fraud literature includes [Ezell and Bear 2005][book_ezell_bear_2005] Degree Mills the surveying treatment of degree-fraud industry. Credential-fraud detection accuracy under standard verification protocols depends on the accessibility and quality of the issuing-body verification infrastructure and admits characterization via the confusion-matrix accuracy

$$\text{Acc}_{\text{cred}} = \frac{|\text{correctly classified}|}{|\text{all}|} = \Pr(\text{verify} \mid \text{authentic}) \cdot \pi_{\text{authentic}} + \Pr(\neg \text{verify} \mid \text{fabricated}) \cdot (1 - \pi_{\text{authentic}})$$

with $\pi_{\text{authentic}}$ the base-rate authentic-credential prevalence. The professional-certification-fraud domain is estimated by through the [PMP Institute fraud detection][ref_pmi_fraud] and adjacent professional-body detection infrastructure. The [Anti-Cheating and Certification Fraud Coalition][ref_accfc] provides one industry reference resource.

### Identity Impersonation

Identity impersonation operates through the creation of accounts and content attributed to a real person other than the operator. The technique intersects with defamation law where the impersonation content damages the target's reputation and with fraud law where the impersonation is used to induce transactions. The [FTC 2024 Impersonation Rule][ref_ftc_impersonation_rule_2024] establishes the federal regulatory framework for the government-and-business-impersonation subset. The [MegaUpload v Universal 2011 case][ref_megaupload_universal_2011] and the [Facebook v Power Ventures 2016][ref_facebook_v_power_ventures_2016] address adjacent legal questions. Cryptographic identity attestation through the [FIDO Alliance authentication standards][ref_fido_alliance] and the [W3C Web Authentication (WebAuthn) standard][ref_w3c_webauthn] provides emerging counter-infrastructure that binds account-level actions to hardware-attested identity keys, which constrains the sockpuppet and impersonation technique classes to accounts for which the attestation infrastructure has been circumvented.

## Reputation Laundering Techniques

Reputation laundering refers to the practice of transferring reputation from a source with credibility to a target that lacks credibility, whether through endorsement, acquisition, or association.

### Endorsement Acquisition

Endorsement acquisition operates through the payment for or exchange with credibility-carrying endorsers whose reputation transfers to the target through the endorsement. The endorsement-value-transfer coefficient takes the form the fraction of the endorser's reputation that transfers to the endorsed target,

$$V_{\text{transfer}}(E \to T) = \kappa_{E,T} \cdot R_E$$

with $\kappa_{E,T}$ the transfer-coefficient dependent on the endorsement channel, the perceived material connection, and the target-endorser category match, and $R_E$ the endorser's reputation stock. The transfer coefficient is bounded by unity and typically ranges

$$\kappa \in [0.01, 0.30]$$

with the lower bound reflecting distant category match and the upper bound reflecting close category match with high-trust endorser. The disclosure-effect coefficient measures the change in the transfer coefficient produced by mandatory material-connection disclosure,

$$\Delta \kappa_{\text{disclose}} = \kappa_{\text{undisclosed}} - \kappa_{\text{disclosed}}$$

with the FTC endorsement-guides policy analysis in [Boerman et al 2018][research_boerman_et_al_2018] and related work estimating $\Delta \kappa_{\text{disclose}}$ in the range of ten to forty percent for consumer-focused endorsements, which sets the informational-value of disclosure enforcement. The technique class has been the primary subject of the [FTC Endorsement Guides 16 CFR Part 255][ref_ftc_endorsement_guides_16_cfr_255] and the [FTC Endorsement Guides FAQ][ref_ftc_endorsement_faq] material-connection-disclosure framework. The enforcement history includes the [FTC 2011 warning letters to bloggers][ref_ftc_2011_blogger_warnings], the [FTC 2015 Machinima settlement][ref_ftc_machinima_2015] on YouTube gaming influencer disclosure, the [FTC 2016 Warner Brothers settlement][ref_ftc_warner_2016] on undisclosed sponsored coverage of Shadow of Mordor, the [FTC 2017 Individual Influencer Warning Letters][ref_ftc_influencer_letters_2017], and the [SEC v Kardashian 2022][ref_sec_kardashian_2022] action addressing undisclosed cryptocurrency promotion.

### Cross-Platform Reputation Transfer

Cross-platform reputation transfer operates through cross-linking that leverages reputation earned on one platform to establish credibility on another platform. The technique class includes legitimate uses (transferring an academic reputation to a general-audience blog) and manipulative uses (using purchased followers or fabricated credentials on one platform to establish apparent credibility on another). The cross-platform-transfer decay follows the exponential form

$$R_T^{P_2}(t) = R_T^{P_1}(0) \cdot \kappa_{P_1 \to P_2} \cdot e^{-\gamma t}$$

with $\kappa_{P_1 \to P_2}$ the platform-pair-specific transfer coefficient and $\gamma$ the reputation-decay rate on the target platform. The [Chen et al 2019][research_chen_et_al_2019] Cross-Platform Identity Linkage treatment surveys the underlying identity-linkage detection literature relevant to manipulation-monitoring.

### Acquisition-Based Laundering

Acquisition-based laundering operates through the purchase of established websites, social-media accounts, or businesses to inherit the target's accumulated reputation for redirection to the acquirer's purposes. The technique class has been documented in the [Kanich et al 2011][research_kanich_et_al_2011] No Plan Survives Contact Experience with Cybercrime Measurement treatment of the domain-market abuse ecosystem, and in the [Krebs 2013][ref_krebs_2013_expired_domains] documentation of the expired-domain reputation-transfer ecosystem. The domain-age reputation value function permits characterization as an increasing function of age

$$V_{\text{domain}}(a) = V_0 \, \bigl(1 - e^{-\alpha a}\bigr)$$

with $a$ the domain age since first content publication and $\alpha$ the reputation-saturation rate. The value asymptotes to $V_0$ for domains of considerable age, which sets the acquisition-target-selection heuristic for the laundering-oriented buyer population. The [Miramirkhani et al 2016][research_miramirkhani_et_al_2016] Dial One For Scam Analyzing the Technical Support Scam Ecosystem treatment analyzes the adjacent scam-ecosystem infrastructure.

## Six-Axis Framework Application

The self-promotion technique inventory allows systematic characterization along the six-axis framework introduced in the framing article. The characterization identifies each technique's position on each axis and enables cross-technique comparison.

The signal axis characterization varies markedly across techniques. Individual review fabrication produces low-volume single-channel signal on the review channel. Coordinated review campaigns produce medium-volume single-channel signal on the review channel with coordination in the injection pattern. Sockpuppet networks produce medium-to-high-volume single-channel signal with persistent identity infrastructure. Follower purchase produces high-volume single-channel signal on the follower channel. Engagement purchase produces high-volume single-channel signal on the engagement channel. Click farm operations produce high-volume multi-channel signal with human-operator fidelity. Generative-model-produced content produces very-high-volume potentially-multi-channel signal at collapsed cost. Cross-platform amplification produces medium-volume multi-channel signal with cross-channel coordination. Astroturfing produces medium-volume multi-channel signal with narrative coordination across the operator population. The signal-axis position of each technique class is summarized by the tuple

$$\mathbf{a}_k^{\text{signal}} = (v_k, C_k, f_k, X_k)$$

with $v_k$ the signal volume rate, $C_k$ the channel-count dimension, $f_k$ the injection fidelity, and $X_k$ the cross-channel amplification factor.

The objective axis characterization for self-promotion techniques uniformly optimizes for the actor's own reputation-signal outcome, but the optimization target varies. Rating-manipulation techniques target rating uplift. Follower-purchase techniques target follower-count uplift. Engagement-purchase techniques target engagement-metric uplift feeding into ranking-algorithm inputs. Search-manipulation techniques target ranking-position uplift. Credential-fabrication techniques target credential-based reputation transfer. Astroturfing techniques target apparent-popular-support production. The objective-axis position of each technique class reduces to the utility functional

$$U_k(\mathbf{x}) = \lambda_k^{\text{rating}} g_{\text{rating}}(\mathbf{x}) + \lambda_k^{\text{follow}} g_{\text{follow}}(\mathbf{x}) + \lambda_k^{\text{engage}} g_{\text{engage}}(\mathbf{x}) + \lambda_k^{\text{rank}} g_{\text{rank}}(\mathbf{x}) + \lambda_k^{\text{cred}} g_{\text{cred}}(\mathbf{x}) + \lambda_k^{\text{support}} g_{\text{support}}(\mathbf{x})$$

with the $\lambda_k^{\cdot}$ weights specifying the technique class's objective composition.

The structure axis characterization varies from individual operators (individual review fabrication) through small-firm operators (business owner boosting own listings) through hired reputation-management firms through commercial marketplaces (fake-review platforms, follower-purchase services) through coordinated inauthentic behavior networks through state-sponsored operations. The structure axis is summarized by hierarchy depth $D_k$ and branching factor $B_k$,

$$\mathbf{a}_k^{\text{struct}} = (D_k, B_k, N_k)$$

with $N_k$ the operator population size. Individual operations exhibit $D_k = 1$, $B_k = 1$, $N_k = 1$. Commercial marketplace operations exhibit $D_k \approx 3$-$4$, $B_k \approx 10$-$100$, $N_k \approx 10^3$-$10^5$. State-sponsored operations exhibit $D_k \approx 5$-$7$, $B_k \approx 10$-$30$, $N_k \approx 10^3$-$10^6$.

The model axis characterization identifies the technical and rhetorical content each technique class carries. The technical model includes the fabrication method, the account-provenance method, the coordination method, and the evasion method. The rhetorical model includes the persuasion framing, the credibility framing, and the narrative framing. The model-axis position of each technique takes the form the position vector $\mathbf{c}_k$ over the technique-space basis introduced in the framing article, with pairwise technique distance $d_{\text{model}}(j, k) = \sum_m |c_m^j - c_m^k|$.

The interaction axis characterization for self-promotion techniques uniformly involves the actor's relationship with platforms (ranging from compliant to adversarial), with targets (typically target-unaware self-promotion), with competitors (typically independent operation, sometimes industry-wide reputation collusion), with audiences (typically audience-unaware manipulation, sometimes audience-complicit as in engagement pods), and with enforcement authorities (below-detection-threshold operation through detection-and-remediation cycle through legal-proceedings engagement). The interaction axis is operationalized as the weighted signed graph over actors, targets, platforms, and enforcers.

The adaptation axis characterization varies appreciably across techniques by adaptation velocity. Individual manipulation exhibits slow adaptation. Small-firm operations exhibit moderate adaptation. Commercial marketplaces exhibit rapid adaptation to platform changes with dedicated engineering resources. State-sponsored operations exhibit rapid adaptation with dedicated intelligence-service infrastructure. The adaptation axis operationalizes as the technique-migration time constant $\tau_k$ under the relaxation dynamics

$$\frac{dS_k}{dt} = -\frac{1}{\tau_k}(S_k - S_k^{*}(t)) + \xi_k(t)$$

with $S_k$ the technique-and-infrastructure state and $S_k^{*}(t)$ the environment-dependent optimal response. Commercial and state-sponsored operations achieve $\tau_k$ in the range of days to weeks; individual operations exhibit $\tau_k$ in the range of months to years.

The cross-axis coupling matrix to the self-promotion technique inventory identifies the principal empirical dependencies among axis values. Empirically salient couplings include the structure-signal coupling $\partial a^{\text{signal}} / \partial a^{\text{struct}} > 0$ (larger organizational structure supports higher signal volume), the model-adaptation coupling $\partial a^{\text{adapt}} / \partial a^{\text{model}} > 0$ (more sophisticated technical model supports faster adaptation), and the interaction-signal coupling $\partial a^{\text{signal}} / \partial a^{\text{interact}} \lessgtr 0$ (compliant platform relationship constrains signal volume, adversarial relationship enables higher signal at higher detection risk). The self-promotion cross-axis coupling matrix

$$C^{\text{self-promo}} = \left[\frac{\partial a^b}{\partial a^a}\right]_{a, b \in \text{axes}}$$

encodes these dependencies and supports estimation from the cross-technique empirical variation in axis positions.

## Detection Methodology Summary

The detection methodology landscape for self-promotion manipulation is treated in depth in the closing article of the miniseries. The framing article surveys the principal detection-methodology classes as they apply to the self-promotion technique inventory.

Statistical anomaly detection targets deviations from expected distributional patterns of reviews, followers, engagement, or ranking signals. The methodology includes temporal-anomaly detection (burst detection, arrival-rate anomaly), distributional-anomaly detection (rating-distribution shape anomaly), and demographic-anomaly detection (geographic or account-age distributional anomaly). The generic anomaly-score statistic under the null-model $H_0$ takes the standardized form

$$z_{\text{anomaly}} = \frac{T(\mathbf{x}) - E_{H_0}[T]}{\sqrt{\text{Var}_{H_0}[T]}}$$

with $T(\mathbf{x})$ the test statistic evaluated on the observed data $\mathbf{x}$. Detection triggers when $|z_{\text{anomaly}}|$ exceeds a chosen threshold, typically calibrated to a desired false-positive rate. The [Kumar et al 2017][research_kumar_et_al_2017] rating-distribution treatment and the [Xie et al 2012][research_xie_et_al_2012] temporal-pattern treatment establish the reference methodology.

Network anomaly detection targets structural anomalies in the reviewer-product-business graph, the follower-followee graph, the account-content-account interaction graph, or the cross-platform sharing graph. The methodology includes community-detection anomaly (unusually dense subgraphs indicating coordination), graph-embedding anomaly (nodes with anomalous embedding-space positions), and label-propagation anomaly (nodes whose classifier labels propagate inconsistently). The [Rayana and Akoglu 2015][research_rayana_akoglu_2015] and [Wang et al 2011][research_wang_et_al_2011] treatments establish the reference methodology.

Machine-learning classifier approaches train on labeled instances of manipulation and non-manipulation and apply the trained classifiers to unlabeled instances. The methodology includes stylometric text classifiers, behavior-pattern classifiers, and multi-modal ensemble classifiers. Ensemble classifier accuracy under standard averaging is captured by

$$P_{\text{ensemble}}(\text{correct}) \geq 1 - \sum_{k=\lceil M/2 \rceil}^{M} \binom{M}{k} p^k (1 - p)^{M - k}$$

with $p$ the individual classifier error rate and $M$ the ensemble size, under the assumption of classifier independence. The classifier-based approach has been the dominant academic detection methodology since the [Ott et al 2011][research_ott_et_al_2011] treatment, with the classifier-adaptation dynamic under adversarial manipulation-technique evolution treated in [Cresci 2020][research_cresci_2020] and subsequent work.

Human review supplements the automated detection methodology for high-stakes classification decisions and for training-corpus construction. The [Roberts 2019][book_roberts_2019] Behind the Screen treatment documents the labor conditions of platform content moderation. The [Klonick 2018][research_klonick_2018] New Governors treatment addresses the governance of the human-review layer.

Cross-platform detection collaboration operates through information-sharing mechanisms including the [Global Internet Forum to Counter Terrorism (GIFCT)][ref_gifct] hash-sharing infrastructure and adjacent industry coordination bodies. Cross-platform collaboration for commercial-manipulation detection is less developed than for terrorism and CSAM detection.

## Platform Countermeasure Summary

Platform countermeasures for self-promotion manipulation are treated in depth in the closing article of the miniseries. The framing article surveys the principal countermeasure classes.

Identity verification countermeasures constrain the account-provenance channel and include phone-number verification, government-ID verification, biometric verification, and the emerging cryptographic-identity attestation frameworks including the [W3C Verifiable Credentials standard][ref_w3c_verifiable_credentials], the [Decentralized Identifiers (DID) standard][ref_w3c_did], and the [C2PA content provenance standard][ref_c2pa_standard]. The identity-verification-cost function increases with verification stringency and creates the tradeoff between manipulation deterrence and user-friction. The composite friction-cost function reduces to

$$C_{\text{verify}}(v) = c_{\text{user-time}}(v) + c_{\text{privacy-loss}}(v) + c_{\text{platform-processing}}(v)$$

with $v$ the verification-stringency parameter and each cost component increasing in $v$. The optimal verification stringency balances the friction cost against the manipulation-deterrence gain, and the platform's first-order condition on $v$ characterizes the equilibrium.

Behavioral analysis countermeasures target the account-behavior patterns that distinguish authentic from inauthentic accounts. The methodology includes rate-limiting to constrain the per-account activity volume, device-fingerprint tracking to detect multi-account operations from single devices, IP-range monitoring, and interaction-pattern analysis. The rate-limit countermeasure imposes the per-account throughput bound

$$\lambda_i^{\text{observed}} \leq \lambda_{\text{max}}, \quad \forall i$$

and shifts the manipulation-cost function such that per-account output scales linearly in $N_{\text{account}}$, which increases the account-provenance cost per unit signal output. The effective deterrence condition against a rational manipulator reduces to the framing-article condition on expected penalty exceeding expected reputation gain, and platform enforcement typically targets the account-provenance channel rather than the signal-output channel to raise the manipulation-cost function's convexity.

Content authentication countermeasures target the content-provenance channel through cryptographic content-signing, watermarking, and provenance-attestation. The [C2PA content provenance standard][ref_c2pa_standard], the [Kirchenbauer et al 2023][research_kirchenbauer_et_al_2023] watermarking framework, and the emerging [Content Authenticity Initiative][ref_content_authenticity_initiative] infrastructure represent the field's current state. The content-provenance verification admits characterization as the signature-validity check

$$V(\text{content}, \sigma) = \mathbb{1}[\text{Verify}(\text{pk}, \text{content}, \sigma)]$$

with $\sigma$ the cryptographic signature attached to the content and pk the public key of the claimed origin. Provenance-verified content carries higher signal informativeness than unverified content under the assumption that signature-generation infrastructure is limited to authentic-content producers.

Legal enforcement countermeasures operate through the regulatory and case-law framework surveyed in the framing article at the [Regulatory and Legal Framework section][related_post_a277_theory]. The [FTC 2024 Final Rule on Fake Reviews and Testimonials][ref_ftc_final_rule_2024] represents the most significant recent federal rulemaking; the [EU Digital Services Act Regulation 2022/2065][ref_eu_dsa_2022] represents the most substantial recent international regulatory framework; and the [Amazon v Fake Review Brokers 2022][ref_amazon_v_fake_review_brokers_2022] private-action campaign represents the most extensive recent private-enforcement development.

## Prevalence Estimates by Technique Class

The empirical prevalence estimates for each self-promotion technique class vary greatly across platforms and categories. The framing article presents the aggregate summary estimates from the surveyed empirical literature. The composite estimates should be treated as order-of-magnitude summaries rather than as precise measurements, and the closing article treats the methodological considerations for prevalence estimation more fully.

Individual and coordinated review fabrication prevalence on consumer-review platforms is documented in [Luca and Zervas 2016][research_luca_zervas_2016] for Yelp at approximately sixteen percent filter rate, [He Hollenbeck Proserpio 2022][research_he_hollenbeck_proserpio_2022] for Amazon at approximately thirty percent fake-review estimate in categories, [Mayzlin Dover Chevalier 2014][research_mayzlin_dover_chevalier_2014] for Tripadvisor at approximately ten to fifteen percent estimate under the natural-experiment methodology, and the [European Commission 2023][ref_ec_2023_sweep] cross-platform sweep at rates varying by category from five to forty percent. The composite category-weighted prevalence estimator under sampling permits characterization as

$$\hat{p}^{\text{comp}} = \sum_c w_c \hat{p}_c, \quad w_c = \frac{n_c}{\sum_{c'} n_{c'}}$$

with $w_c$ the volume-weighted category weight and $\hat{p}_c$ the category-specific prevalence estimate, subject to sampling variance

$$\text{Var}(\hat{p}^{\text{comp}}) = \sum_c w_c^2 \cdot \text{Var}(\hat{p}_c)$$

that allows standard confidence-interval construction under the delta-method approximation.

Follower-purchase and engagement-purchase prevalence on major social platforms varies by platform and account category, with typical estimates for the fraction of purchased or otherwise inauthentic followers on major accounts in the range of five to thirty percent, and higher rates in categories including cryptocurrency promotion and political mobilization. The [Cresci 2020][research_cresci_2020] survey and [Yang et al 2020][research_yang_et_al_2020] provide the reference estimates.

Sockpuppet-network and coordinated inauthentic behavior prevalence is documented most extensively for state-sponsored operations in the [Bradshaw and Howard 2019][research_bradshaw_howard_2019], [Bradshaw Bailey Howard 2021][research_bradshaw_bailey_howard_2021], and platform-industry [Meta Adversarial Threat Report][ref_meta_atr] treatments. The estimated count of active state-sponsored inauthentic-behavior operations across the major platforms is in the range of tens to hundreds of active operations at any given time, with individual operation scale ranging from tens to hundreds of thousands of associated accounts.

Astroturfing prevalence is more difficult to estimate than other technique classes because astroturfing operations often operate through authentic-appearing organizational structures and produce content that does not clearly separate from authentic advocacy. The [Walker 2014][book_walker_2014] treatment documents the commercial astroturf-services industry at scale but does not provide a precise prevalence estimate for the population of active astroturf campaigns. The [Trustpilot Transparency Report][ref_trustpilot_transparency] and the [Fakespot Consumer Reports][ref_fakespot_consumer_reports] provide industry-side prevalence disclosure for the consumer-review subset.

Generative-model-produced content prevalence has grown rapidly since the 2022 large-language-model deployments. Contemporary estimates from [Yang and Menczer 2024][research_yang_menczer_2024] and [Sohail et al 2024][research_sohail_et_al_2024] document the increasing prevalence of AI-generated review and social-media content, with the prevalence rate remaining considerably uncertain due to detection difficulty.

The aggregate self-promotion manipulation prevalence across the platform ecosystem is captured by

$$p_{\text{self-promo}}^{\text{aggregate}}(t) = \frac{\sum_c n_c(t) \cdot p_c^{\text{self-promo}}(t)}{\sum_c n_c(t)}$$

with $n_c(t)$ the total signal-event volume in category $c$ at time $t$ and $p_c^{\text{self-promo}}(t)$ the category-specific self-promotion prevalence rate. The aggregate estimate under conservative methodology is in the range of ten to twenty percent of the total reputation-signal volume across the surveyed platform ecosystem, with extensive category variation.

## Alternative Analytical Frameworks

The economic-signaling framework the miniseries adopts is one of several analytical frameworks under which the self-promotion technique inventory supports treatment. The framing article surveys the principal alternatives and identifies where the alternative frameworks would produce different conclusions from the model the miniseries adopts.

The advertising-and-marketing-theory framework treats self-promotion techniques as extensions of the advertising toolkit into digital reputation systems. The [Aaker 1991][book_aaker_1991] Managing Brand Equity, [Kotler and Keller 2016][book_kotler_keller_2016] Marketing Management, and adjacent treatments establish the framework. This formulation produces different conclusions than the reputation-manipulation framework in that it treats the manipulation-vs-legitimate-promotion boundary as a matter of degree along the advertising-effectiveness continuum rather than as a categorical distinction. The treatment predicts that platform-integrity enforcement will produce systematic advertising-market inefficiencies through the enforcement's effect on legitimate word-of-mouth marketing operating adjacent to the manipulation techniques.

The persuasion-psychology framework of [Cialdini 1984][book_cialdini_1984] Influence and [Petty and Cacioppo 1986][research_petty_cacioppo_1986] Elaboration Likelihood Model treats self-promotion techniques by the persuasion mechanisms they exploit. The framework identifies persuasion-mechanism vulnerabilities in consumer decision-making that manipulation techniques exploit and predicts consumer-response effects based on the technique's alignment with dominant persuasion pathways. The account produces different conclusions than the economic framework in that it emphasizes the cognitive-mechanism dimension of manipulation effectiveness independent of the information-asymmetry dimension.

The two-sided-market framework of [Rochet and Tirole 2003][research_rochet_tirole_2003] and [Rysman 2009][research_rysman_2009] treats the platform's mediation role as central to the manipulation equilibrium. The model identifies platform-design choices that shape the manipulation-equilibrium intensity through the cross-side network-effect structure. This formulation produces different conclusions than the technique-focused framework in that it treats the platform as an active party in the equilibrium rather than as a neutral infrastructure provider, which implies different regulatory-intervention recommendations focused on platform-design-choice regulation rather than on technique-specific enforcement.

The attention-economy framework of [Simon 1971][research_simon_1971] Designing Organizations for an Information-Rich World and [Wu 2016][book_wu_2016] The Attention Merchants treats reputation-signal manipulation as a subset of the broader attention-manipulation ecosystem. The treatment predicts that reforms internal to the reputation-manipulation framework will fail to address the underlying attention-economics dynamics and that broader attention-economy reform is required to significantly reduce equilibrium manipulation.

The influencer-and-creator-economy framework of [Abidin 2018][book_abidin_2018] Internet Celebrity, [Duffy 2017][book_duffy_2017] Not Getting Paid to Do What You Love, and [Bishop 2019][research_bishop_2019] Managing Visibility on YouTube treats self-promotion techniques as embedded in the broader creator-economy political-economy. This account predicts that reforms internal to the platform-integrity framework will fail to address the underlying labor-and-authenticity dynamics that generate the manipulation supply. The framework produces different regulatory-intervention recommendations focused on creator-economy structural reform rather than on manipulation-specific enforcement.

The search-theory framework of [Stigler 1961][research_stigler_1961] and subsequent search-cost literature treats self-promotion techniques by the consumer-search-cost changes they impose. The account produces different conclusions than the direct-signaling framework in that it emphasizes the equilibrium-price and quality-signaling effects that follow from consumer-search-cost changes independently of the direct reputation-signal-informativeness effect.

The regulatory-capture framework of [Stigler 1971][research_stigler_1971] The Theory of Economic Regulation extends to platform-integrity-enforcement politics through the observation that regulated industries capture their regulators over time. The model predicts that platform-integrity enforcement will systematically underweight consumer interests relative to producer interests as the manipulation-service industry organizes to influence platform policy and regulatory rule-making.

The adversarial-machine-learning framework of [Goodfellow Shlens Szegedy 2014][research_goodfellow_shlens_szegedy_2014] and subsequent adversarial-ML literature treats detection-system-vs-manipulation-technique dynamics as an adversarial classification problem with algorithmic implications. This formulation produces different detection-system-design recommendations than the classical classification framework, emphasizing robustness against adversarial adaptation over accuracy on labeled-training-distribution instances.

Each alternative framework offers analytical leverage the miniseries does not fully develop. The miniseries adopts the economic-signaling framework as the primary organizing structure because it provides the most tractable formalization of the manipulator-platform-consumer strategic interaction and connects most directly to the empirical detection and enforcement literatures. The closing article treats the account selection more fully and identifies the empirical questions on which the alternative frameworks would predict different observations.

## Terminological Note

The article adopts the terminology introduced in the framing article of the miniseries at [Virtual Reputation Manipulation Theory and Analytical Framework][related_post_a277_theory]. The self-promotion class refers to the manipulation techniques oriented at inflating the actor's own reputation, and the competitor-attack class refers to the techniques oriented at degrading a competitor's reputation. The two classes are treated separately in this article and the next respectively, with the closing article treating the detection and organic-establishment landscape that responds to both.

The term technique class refers to the analytical grouping of manipulation practices sharing signal channel, technique-space position, and detection-signature characteristics. The term signal channel refers to the reputation-system channel targeted by a technique class (reviews, followers, engagement, ranking, credentials, endorsement, association). The term detection signature refers to the observable patterns that distinguish a manipulation instance from an authentic instance of the same signal channel. The term countermeasure refers to the platform, legal, or infrastructure response to a technique class or manipulation instance. The article uses the platform-integrity industry terminology (coordinated inauthentic behavior, adversarial threat, take-down) where the industry terminology is more precise than the academic terminology.

## Load-Bearing Open Questions

- What is the correct empirical characterization of the aggregate self-promotion manipulation prevalence across the platform ecosystem, and how does the estimate change under alternative methodologies? The current range of empirical estimates spans sizable variation, and no single point estimate commands consensus.
- What is the correct empirical characterization of the causal impact of self-promotion technique classes on downstream consumer purchase behavior? The [Luca 2016][research_luca_2016], [Chevalier and Mayzlin 2006][research_chevalier_mayzlin_2006], and [Anderson and Magruder 2012][research_anderson_magruder_2012] treatments provide the causal-inference foundation but leave appreciable variation in the effect-size estimates across settings.
- What is the correct empirical characterization of the marginal deterrent effect of enforcement actions on self-promotion manipulation prevalence? The pre-and-post studies of major FTC enforcement actions provide the empirical foundation, but the marginal-deterrent estimates remain contested.
- What is the correct empirical characterization of the equilibrium impact of generative-model deployment on self-promotion manipulation prevalence and on detection difficulty? The [Sohail et al 2024][research_sohail_et_al_2024] and [Sadasivan et al 2023][research_sadasivan_et_al_2023] treatments provide the initial evidence, but the equilibrium trajectory remains substantially uncertain.
- What is the correct comparative treatment of the self-promotion manipulation ecosystem across national platform-regulation regimes, and which regulatory instruments produce the most significant equilibrium-manipulation reduction?
- What is the correct empirical characterization of the interaction between commercial self-promotion manipulation and state-sponsored information operations, and does the interaction produce systematic effects on the commercial reputation-manipulation ecosystem beyond the state-operation-specific effects?
- How should the platform-integrity operations, the regulatory framework, and the market response coordinate to reduce the equilibrium self-promotion manipulation intensity, and what is the equilibrium detection intensity that maximizes joint surplus across producer, consumer, and platform welfare?

These questions recur throughout the miniseries and are revisited in the closing synthesis.

## References

### Books

- [Aaker 1991 Managing Brand Equity][book_aaker_1991]
- [Abidin 2018 Internet Celebrity][book_abidin_2018]
- [Aral 2020 The Hype Machine][book_aral_2020]
- [Berger 2016 Contagious Why Things Catch On][book_berger_2016]
- [Bernays 1923 Crystallizing Public Opinion][book_bernays_1923]
- [Bernays 1928 Propaganda][book_bernays_1928]
- [Cialdini 1984 Influence][book_cialdini_1984]
- [Cronin 2004 Advertising Myths][book_cronin_2004]
- [Cutlip 1994 The Unseen Power Public Relations A History][book_cutlip_1994]
- [Duffy 2017 Not Getting Paid to Do What You Love][book_duffy_2017]
- [Ewen 1996 PR A Social History of Spin][book_ewen_1996]
- [Ezell and Bear 2005 Degree Mills][book_ezell_bear_2005]
- [Fiske and Taylor 2013 Social Cognition][book_fiske_taylor_2013]
- [Fitzpatrick 2005 False Profits][book_fitzpatrick_2005]
- [Godin 2018 This is Marketing][book_godin_2018]
- [Greif 2006 Institutions and the Path to the Modern Economy][book_greif_2006]
- [Katz and Lazarsfeld 1955 Personal Influence][book_katz_lazarsfeld_1955]
- [Kotler and Keller 2016 Marketing Management][book_kotler_keller_2016]
- [Lippmann 1922 Public Opinion][book_lippmann_1922]
- [Marwick 2013 Status Update][book_marwick_2013]
- [McGarity and Wagner 2008 Bending Science][book_mcgarity_wagner_2008]
- [Michaels 2008 Doubt Is Their Product][book_michaels_2008]
- [Nisbett and Ross 1980 Human Inference][book_nisbett_ross_1980]
- [Ogilvie 2019 The European Guilds][book_ogilvie_2019]
- [Ogilvy 1963 Confessions of an Advertising Man][book_ogilvy_1963]
- [Oreskes and Conway 2010 Merchants of Doubt][book_oreskes_conway_2010]
- [Packard 1957 The Hidden Persuaders][book_packard_1957]
- [Petty 2015 The Codevelopment of Marketing Law and Practice][book_petty_2015]
- [Presbrey 1929 The History and Development of Advertising][book_presbrey_1929]
- [Provost and Fawcett 2013 Data Science for Business][book_provost_fawcett_2013]
- [Reeves 1961 Reality in Advertising][book_reeves_1961]
- [Rid 2020 Active Measures][book_rid_2020]
- [Roberts 2019 Behind the Screen][book_roberts_2019]
- [Silverman 2001 Secrets of Word-of-Mouth Marketing][book_silverman_2001]
- [Strasser 1989 Satisfaction Guaranteed The Making of the American Mass Market][book_strasser_1989]
- [Taylor 2011 The Case for and Against Multi-Level Marketing][book_taylor_2011]
- [Trivellato 2009 The Familiarity of Strangers][book_trivellato_2009]
- [Turow 2011 The Daily You][book_turow_2011]
- [Twede and Selke 2005 Cartons Crates and Corrugated Board][book_twede_selke_2005]
- [Tye 1998 The Father of Spin][book_tye_1998]
- [Walker 2014 Grassroots for Hire][book_walker_2014]
- [Woolley and Howard 2018 Computational Propaganda][book_woolley_howard_2018]
- [Wu 2016 The Attention Merchants][book_wu_2016]
- [Young 1961 The Toadstool Millionaires][book_young_1961]

### Reference

- [16 CFR Part 255 FTC Guides on Endorsements and Testimonials][ref_ftc_endorsement_guides_16_cfr_255]
- [ACCC v Trivago 2020][ref_accc_v_trivago_2020]
- [Amazon Community Guidelines][ref_amazon_community_guidelines]
- [Amazon Reviews Dataset][ref_amazon_reviews_dataset]
- [Amazon v Fake Review Brokers 2022][ref_amazon_v_fake_review_brokers_2022]
- [Anti-Cheating and Certification Fraud Coalition][ref_accfc]
- [Apple App Store Review Guidelines][ref_apple_app_store_review_guidelines]
- [Barnum Autobiography 1854][ref_barnum_autobiography_1854]
- [Bentsen 1985 Congressional Record on Astroturf Lobbying][ref_bentsen_congressional_record_1985]
- [Beuk Boekhandel 2013 Dutch Fake Review Case][ref_beuk_boekhandel_2013]
- [Bilton 2014 New York Times Investigation of Purchased Twitter Followers][ref_bilton_2014_nyt_followers]
- [Bing 2004 Astroturf Blogging Incident][ref_bing_2004_astroturf]
- [Bot Repository Indiana OSoMe][ref_bot_repository]
- [C2PA Coalition for Content Provenance and Authenticity][ref_c2pa_coalition]
- [C2PA Content Provenance Standard][ref_c2pa_standard]
- [Canadian Competition Bureau v Amazon Fake Reviews][ref_canada_amazon]
- [Content Authenticity Initiative][ref_content_authenticity_initiative]
- [Cresci-2015 Fake Followers Dataset][ref_cresci_2015_dataset]
- [Cresci-2017 Genuine and Spambot Dataset][ref_cresci_2017_dataset]
- [Cross-Platform Sharing Dataset][ref_cross_platform_sharing_dataset]
- [Cushing 2013 Wired Bangladesh Click Farm Investigation][ref_cushing_2013_click_farm]
- [Cutts Google Webmaster Central Blog Archives][ref_cutts_google_blog]
- [Ellis Ott 2018 Atlantic Instagram Pods][ref_ellis_ott_2018_pods]
- [EU Digital Services Act Regulation 2022/2065][ref_eu_dsa_2022]
- [European Commission 2023 Sweep of Consumer Websites][ref_ec_2023_sweep]
- [Facebook v Power Ventures 2016][ref_facebook_v_power_ventures_2016]
- [Fakespot Consumer Reports][ref_fakespot_consumer_reports]
- [Fang 2013 Koch Network Investigation][ref_fang_2013_koch]
- [FIDO Alliance Authentication Standards][ref_fido_alliance]
- [FTC 2011 Blogger Warning Letters][ref_ftc_2011_blogger_warnings]
- [FTC 2015 Machinima Settlement][ref_ftc_machinima_2015]
- [FTC 2016 Warner Brothers Settlement][ref_ftc_warner_2016]
- [FTC 2017 Individual Influencer Warning Letters][ref_ftc_influencer_letters_2017]
- [FTC 2019 Sunday Riley Settlement][ref_ftc_sunday_riley_2019]
- [FTC 2019 UrthBox Settlement][ref_ftc_urthbox_2019]
- [FTC 2022 Roomster Settlement][ref_ftc_roomster_2022]
- [FTC 2023 Bountiful Company Review Hijacking Settlement][ref_ftc_bountiful_2023]
- [FTC 2024 Final Rule on Fake Reviews and Testimonials][ref_ftc_final_rule_2024]
- [FTC 2024 Impersonation Rule][ref_ftc_impersonation_rule_2024]
- [FTC Endorsement Guides Frequently Asked Questions][ref_ftc_endorsement_faq]
- [FTC v Amway 1979 Decision][ref_ftc_amway_1979]
- [FTC v Devumi 2019][ref_ftc_devumi_2019]
- [FTC v Herbalife 2016 Order][ref_ftc_herbalife_2016]
- [FTC v Herbalife 2022 Order][ref_ftc_herbalife_2022]
- [FTC v Nutrilite Products 1951 Order][ref_ftc_nutrilite_1951]
- [Global Internet Forum to Counter Terrorism GIFCT][ref_gifct]
- [Google 2011 Panda Algorithm Update][ref_google_panda_2011]
- [Google 2012 Penguin Algorithm Update][ref_google_penguin_2012]
- [Google Business Profile Content Guidelines][ref_google_business_profile_guidelines]
- [Google Play Developer Policy][ref_google_play_developer_policy]
- [Google Search Central Spam Policies][ref_google_search_spam_policies]
- [Google Webmaster Guidelines][ref_google_webmaster_guidelines]
- [Gyongyi Garcia-Molina Pedersen 2004 Combating Web Spam with TrustRank][ref_gyongyi_2004_trustrank_paper]
- [IAB Digital Ad Fraud Report][ref_iab_ad_fraud_report]
- [Instagram Community Guidelines Authenticity Section][ref_instagram_authenticity_guidelines]
- [Instagram Verified Badge Documentation][ref_instagram_verified]
- [Italian AGCM Booking.com Fake Reviews Action][ref_italy_agcm_booking]
- [Ivy Lee Declaration of Principles 1906][ref_ivy_lee_declaration_1906]
- [Krebs 2013 Expired Domain Reputation Transfer][ref_krebs_2013_expired_domains]
- [Levick and Slavo 2015 Front Organization Documentation][ref_levick_slavo_2015]
- [LinkedIn ID Verification][ref_linkedin_verification]
- [MegaUpload v Universal 2011][ref_megaupload_universal_2011]
- [Meta Adversarial Threat Report][ref_meta_atr]
- [Meta AI-Generated Content Labeling Policy][ref_meta_ai_content_labeling]
- [Meta Coordinated Inauthentic Behavior Policy][ref_meta_cib_policy]
- [Miller 2004 Working Families for Wal-Mart Documentation][ref_miller_2004_walmart]
- [MRC Media Rating Council Viewability Standards][ref_mrc_viewability_standards]
- [Mueller Report 2019 Volume One][ref_mueller_report_2019]
- [Nielsen Trust in Advertising Global Report][ref_nielsen_trust_advertising]
- [NY Attorney General v Devumi 2019][ref_ny_ag_devumi_2019]
- [OpenAI ChatGPT 2022 Release][ref_openai_chatgpt_2022]
- [OpenAI GPT-4 2023 Release][ref_openai_gpt4_2023]
- [Ott Deceptive Opinion Spam Corpus][ref_ott_deceptive_corpus]
- [PMI Professional Certification Fraud Detection][ref_pmi_fraud]
- [SEC v Kardashian 2022][ref_sec_kardashian_2022]
- [Sony PlayStation Portable 2006 Fake Blog Case][ref_sony_psp_2006]
- [Source Watch Front Organizations Catalog][ref_source_watch_front]
- [Trustpilot Transparency Report][ref_trustpilot_transparency]
- [Twitter Verification Legacy Program Documentation][ref_twitter_verification_legacy]
- [UK CMA Facebook and Google Fake Reviews Investigation 2022][ref_uk_cma_facebook_google_2022]
- [W3C Decentralized Identifiers Standard][ref_w3c_did]
- [W3C Verifiable Credentials Standard][ref_w3c_verifiable_credentials]
- [W3C Web Authentication WebAuthn Standard][ref_w3c_webauthn]
- [White Ops Methbot 2016 Report][ref_white_ops_methbot_2016]
- [Whole Foods Mackey Rahodeb Case 2007][ref_whole_foods_rahodeb_2007]
- [X Blue Paid Verification][ref_x_blue]
- [X Platform Manipulation and Spam Policy][ref_x_platform_manipulation_policy]
- [X Transparency Report][ref_x_transparency_report]
- [Yelp Content Guidelines][ref_yelp_content_guidelines]
- [YelpChi Fake Review Dataset][ref_yelpchi_dataset]
- [YouTube Channel Verification Documentation][ref_youtube_verification]
- [YouTube View-Count Manipulation Policy][ref_youtube_view_manipulation_policy]

### Related Post

- [Virtual Reputation Manipulation Theory and Analytical Framework A277][related_post_a277_theory]

### Research

- [Ali et al 2017 Same Same but Different Search Advertising][research_ali_et_al_2017]
- [Alvisi et al 2013 SoK Evolution of Sybil Defense via Social Networks][research_alvisi_et_al_2013]
- [Anderson and Magruder 2012 Learning from the Crowd Yelp][research_anderson_magruder_2012]
- [Beales 1980 Efficient Regulation of Consumer Information][research_beales_1980]
- [Bishop 2019 Managing Visibility on YouTube through Algorithmic Gossip][research_bishop_2019]
- [Bradshaw Bailey Howard 2021 Industrialized Disinformation][research_bradshaw_bailey_howard_2021]
- [Bradshaw and Howard 2019 The Global Disinformation Order][research_bradshaw_howard_2019]
- [Boerman et al 2018 Sponsored Content Disclosure Effects][research_boerman_et_al_2018]
- [Bright et al 2020 Coordinated Behavior on Social Media][research_bright_et_al_2020]
- [Cao et al 2012 Aiding the Detection of Fake Accounts in Large Scale Social Networks][research_cao_et_al_2012]
- [Castillo et al 2007 Know Your Neighbors Web Spam Detection][research_castillo_et_al_2007]
- [Chaiken 1980 Heuristic Systematic Model of Persuasion][research_chaiken_1980]
- [Chandola Banerjee Kumar 2009 Anomaly Detection A Survey][research_chandola_banerjee_kumar_2009]
- [Chen et al 2019 Cross-Platform Identity Linkage][research_chen_et_al_2019]
- [Chevalier and Mayzlin 2006 The Effect of Word of Mouth on Sales][research_chevalier_mayzlin_2006]
- [Chintagunta Gopinath Venkataraman 2010 Effects of Online User Reviews on Movie Box Office][research_chintagunta_gopinath_venkataraman_2010]
- [Cho et al 2011 Astroturfing][research_cho_et_al_2011]
- [Cresci 2020 A Decade of Social Bot Detection][research_cresci_2020]
- [Cresci et al 2015 Fame for Sale Fake Follower Detection][research_cresci_et_al_2015]
- [Cresci et al 2017 The Paradigm-Shift of Social Spambots][research_cresci_et_al_2017]
- [Danezis and Mittal 2009 SybilInfer][research_danezis_mittal_2009]
- [D'Ambrosio et al 2018 App Review Manipulation Analysis][research_dambrosio_et_al_2018]
- [De Micheli and Stroppa 2013 Twitter and the Underground Market][research_demicheli_stroppa_2013]
- [Diamond 1971 Model of Price Adjustment][research_diamond_1971]
- [DiResta et al 2019 The Tactics and Tropes of the Internet Research Agency][research_diresta_et_al_2019]
- [Douceur 2002 The Sybil Attack][research_douceur_2002]
- [Farooqi et al 2017 Characterizing Key Stakeholders in an Online Black Market][research_farooqi_et_al_2017]
- [Fawcett 2006 Introduction to ROC Analysis][research_fawcett_2006]
- [Fei et al 2013 Exploiting Burstiness in Reviews][research_fei_et_al_2013]
- [Feng et al 2012 Syntactic Stylometry for Deception Detection][research_feng_et_al_2012]
- [Ferrara et al 2016 The Rise of Social Bots][research_ferrara_et_al_2016]
- [Goodfellow Shlens Szegedy 2014 Explaining and Harnessing Adversarial Examples][research_goodfellow_shlens_szegedy_2014]
- [Gyongyi and Garcia-Molina 2005 Web Spam Taxonomy][research_gyongyi_garciamolina_2005]
- [He Hollenbeck Proserpio 2022 The Market for Fake Reviews][research_he_hollenbeck_proserpio_2022]
- [Hoffman 2017 Sponsored Content Regulation][research_hoffman_2017]
- [Jindal and Liu 2008 Opinion Spam and Analysis][research_jindal_liu_2008]
- [Kanich et al 2011 No Plan Survives Contact Cybercrime Measurement][research_kanich_et_al_2011]
- [King Pan Roberts 2017 How the Chinese Government Fabricates Social Media Posts][research_king_pan_roberts_2017]
- [Kirchenbauer et al 2023 A Watermark for Large Language Models][research_kirchenbauer_et_al_2023]
- [Klonick 2018 The New Governors][research_klonick_2018]
- [Kumar et al 2017 An Army of Me Sockpuppets in Online Discussion][research_kumar_army_2017]
- [Kumar et al 2017 Understanding Rating Distributions][research_kumar_et_al_2017]
- [Kumar and Shah 2018 False Information on Web and Social Media Survey][research_kumar_shah_2018]
- [Li et al 2014 Towards a General Rule for Identifying Deceptive Opinion Spam][research_li_et_al_2014]
- [Lim et al 2010 Detecting Product Review Spammers][research_lim_et_al_2010]
- [Luca 2016 Reviews Reputation and Revenue Yelp][research_luca_2016]
- [Luca and Zervas 2016 Fake It Till You Make It][research_luca_zervas_2016]
- [Malbon 2013 Taking Fake Online Consumer Reviews Seriously][research_malbon_2013]
- [Marino et al 2023 Effects of Removing Twitter Blue Verification][research_marino_et_al_2023]
- [Mayzlin Dover Chevalier 2014 Promotional Reviews][research_mayzlin_dover_chevalier_2014]
- [McCracken 1989 Who Is the Celebrity Endorser][research_mccracken_1989]
- [Miramirkhani et al 2016 Dial One For Scam Technical Support Scams][research_miramirkhani_et_al_2016]
- [Motoyama et al 2011 Dirty Jobs Freelance Labor in Web Service Abuse][research_motoyama_et_al_2011]
- [Mukherjee et al 2013 What Yelp Fake Review Filter Might Be Doing][research_mukherjee_et_al_2013]
- [Ntoulas et al 2006 Detecting Spam Web Pages through Content Analysis][research_ntoulas_et_al_2006]
- [Ott et al 2011 Finding Deceptive Opinion Spam][research_ott_et_al_2011]
- [Ott et al 2013 Negative Deceptive Opinion Spam][research_ott_et_al_2013]
- [Page and Brin 1998 Anatomy of a Large-Scale Hypertextual Web Search Engine][research_page_brin_1998]
- [Page Brin Motwani Winograd 1999 PageRank Extended Technical Report][research_page_brin_motwani_winograd_1999]
- [Papakyriakopoulos et al 2020 Political Communication on Social Media][research_papakyriakopoulos_et_al_2020]
- [Pearce et al 2014 Characterizing Large-Scale Click Fraud in ZeroAccess][research_pearce_et_al_2014]
- [Petty and Andrews 2008 Covert Marketing Unmasked][research_petty_andrews_2008]
- [Petty and Cacioppo 1986 Elaboration Likelihood Model of Persuasion][research_petty_cacioppo_1986]
- [Ratkiewicz et al 2011 Detecting and Tracking Political Abuse in Social Media Truthy][research_ratkiewicz_et_al_2011]
- [Rayana and Akoglu 2015 Collective Opinion Spam Detection][research_rayana_akoglu_2015]
- [Rochet and Tirole 2003 Platform Competition in Two-Sided Markets][research_rochet_tirole_2003]
- [Rothschild 1974 Searching for the Lowest Price][research_rothschild_1974]
- [Rysman 2009 The Economics of Two-Sided Markets][research_rysman_2009]
- [Sadasivan et al 2023 Can AI-Generated Text be Reliably Detected][research_sadasivan_et_al_2023]
- [Simon 1971 Designing Organizations for an Information-Rich World][research_simon_1971]
- [Sohail et al 2024 Detection of Large-Language-Model Generated Reviews][research_sohail_et_al_2024]
- [Solorio et al 2014 Sockpuppet Detection in Wikipedia][research_solorio_et_al_2014]
- [Starbird 2019 Disinformation's Spread Bots Trolls and All of Us][research_starbird_2019]
- [Stigler 1961 The Economics of Information][research_stigler_1961]
- [Stigler 1971 The Theory of Economic Regulation][research_stigler_1971]
- [Stringhini et al 2013 Follow the Green Twitter Follower Markets][research_stringhini_et_al_2013]
- [Trusov Bucklin Pauwels 2009 Effects of Word-of-Mouth versus Traditional Marketing][research_trusov_bucklin_pauwels_2009]
- [Tsikerdekis and Zeadally 2014 Multiple Account Identity Deception Detection][research_tsikerdekis_zeadally_2014]
- [Wang et al 2011 Review Graph Based Online Store Review Spammer Detection][research_wang_et_al_2011]
- [Wang et al 2012 Serf and Turf Crowdturfing for Fun and Profit][research_wang_et_al_2012]
- [Weerkamp and de Rijke 2012 Credibility-Inspired Ranking][research_weerkamp_derijke_2012]
- [Weller et al 2019 Understanding Cross-Platform Sharing and Engagement Pods][research_weller_et_al_2019]
- [Wu et al 2020 Fake Online Reviews Literature Review][research_wu_et_al_2020]
- [Xie et al 2012 Review Spam Detection via Temporal Pattern Discovery][research_xie_et_al_2012]
- [Yang et al 2020 Scalable and Generalizable Social Bot Detection][research_yang_et_al_2020]
- [Yang and Menczer 2024 Anatomy of an AI-Powered Malicious Social Botnet][research_yang_menczer_2024]
- [Yao et al 2017 Automated Crowdturfing Attacks and Defenses][research_yao_et_al_2017]
- [Yu et al 2006 SybilGuard Defending Against Sybil Attacks][research_yu_et_al_2006]
- [Yu et al 2008 SybilLimit A Near-Optimal Social Network Defense against Sybil Attacks][research_yu_et_al_2008]
- [Zannettou et al 2018 Understanding Web Archiving Services][research_zannettou_et_al_2018]
- [Zannettou et al 2019 Disinformation Warfare Understanding State-Sponsored Trolls][research_zannettou_et_al_2019]
- [Zellers et al 2019 Defending Against Neural Fake News][research_zellers_et_al_2019]
- [Zheng et al 2011 Detecting Sockpuppets in Deceptive Opinion Spam][research_zheng_et_al_2011]

[book_aral_2020]: https://us.macmillan.com/books/9780525574514/thehypemachine
[book_ezell_bear_2005]: https://www.prometheusbooks.com/9781591024637/degree-mills/
[book_mcgarity_wagner_2008]: https://www.hup.harvard.edu/books/9780674047143
[book_michaels_2008]: https://global.oup.com/academic/product/doubt-is-their-product-9780195300673
[book_oreskes_conway_2010]: https://www.bloomsbury.com/us/merchants-of-doubt-9781608193943/
[book_rid_2020]: https://us.macmillan.com/books/9780374287269/activemeasures
[book_roberts_2019]: https://yalebooks.yale.edu/book/9780300235883/behind-the-screen/
[book_walker_2014]: https://www.cambridge.org/9781107619012
[book_woolley_howard_2018]: https://global.oup.com/academic/product/computational-propaganda-9780190931414
[ref_accfc]: https://www.credentialingexcellence.org/
[ref_amazon_community_guidelines]: https://www.amazon.com/gp/help/customer/display.html?nodeId=GLHXEX85MENUE4XF
[ref_amazon_v_fake_review_brokers_2022]: https://www.aboutamazon.com/news/policy-news-views/amazon-continues-legal-action-against-fake-review-brokers
[ref_apple_app_store_review_guidelines]: https://developer.apple.com/app-store/review/guidelines/
[ref_bentsen_congressional_record_1985]: https://www.congress.gov/congressional-record
[ref_beuk_boekhandel_2013]: https://uitspraken.rechtspraak.nl/details?id=ECLI:NL:RBAMS:2013:8117
[ref_bilton_2014_nyt_followers]: https://www.nytimes.com/2014/04/06/fashion/social-media-followers-for-sale.html
[ref_bing_2004_astroturf]: https://www.wired.com/2004/12/tricks-and-tips-for-blogging/
[ref_c2pa_coalition]: https://c2pa.org/
[ref_c2pa_standard]: https://c2pa.org/specifications/specifications/1.4/index.html
[ref_content_authenticity_initiative]: https://contentauthenticity.org/
[ref_cross_platform_sharing_dataset]: https://cross-platform-sharing.github.io/
[ref_cushing_2013_click_farm]: https://www.wired.com/2013/08/click-farms/
[ref_cutts_google_blog]: https://www.mattcutts.com/blog/
[ref_ellis_ott_2018_pods]: https://www.theatlantic.com/technology/archive/2018/06/instagram-pods-explained/564237/
[ref_eu_dsa_2022]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2065
[ref_ec_2023_sweep]: https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/sweeps_en
[ref_facebook_v_power_ventures_2016]: https://cdn.ca9.uscourts.gov/datastore/opinions/2016/07/12/13-17102.pdf
[ref_fang_2013_koch]: https://www.thenation.com/article/archive/koch-brothers-secret-bank/
[ref_ftc_2011_blogger_warnings]: https://www.ftc.gov/news-events/news/press-releases/2011/09/ftc-releases-updated-guides-concerning-use-endorsements-and-testimonials-advertising
[ref_ftc_devumi_2019]: https://www.ftc.gov/legal-library/browse/cases-proceedings/162-3175-devumi-llc-german-calas-jr
[ref_ftc_endorsement_faq]: https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking
[ref_ftc_endorsement_guides_16_cfr_255]: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255
[ref_ftc_final_rule_2024]: https://www.ftc.gov/legal-library/browse/federal-register-notices/16-cfr-part-465-rule-use-consumer-reviews-testimonials
[ref_ftc_impersonation_rule_2024]: https://www.ftc.gov/legal-library/browse/federal-register-notices/rule-impersonation-government-businesses
[ref_ftc_influencer_letters_2017]: https://www.ftc.gov/news-events/news/press-releases/2017/04/ftc-staff-reminds-influencers-brands-clearly-disclose-relationship
[ref_ftc_machinima_2015]: https://www.ftc.gov/legal-library/browse/cases-proceedings/142-3090-machinima-inc
[ref_ftc_sunday_riley_2019]: https://www.ftc.gov/legal-library/browse/cases-proceedings/1723065-sunday-riley-modern-skincare-llc
[ref_ftc_urthbox_2019]: https://www.ftc.gov/legal-library/browse/cases-proceedings/172-3128-urthbox-inc
[ref_ftc_warner_2016]: https://www.ftc.gov/legal-library/browse/cases-proceedings/152-3034-warner-bros-home-entertainment-inc-matter
[ref_gifct]: https://gifct.org/
[ref_gyongyi_2004_trustrank_paper]: https://ilpubs.stanford.edu:8090/645/
[ref_google_panda_2011]: https://developers.google.com/search/blog/2011/02/finding-more-high-quality-sites-in
[ref_google_penguin_2012]: https://developers.google.com/search/blog/2012/04/another-step-to-reward-high-quality
[ref_google_play_developer_policy]: https://play.google.com/about/developer-content-policy/
[ref_google_search_spam_policies]: https://developers.google.com/search/docs/essentials/spam-policies
[ref_google_webmaster_guidelines]: https://developers.google.com/search/docs/essentials
[ref_instagram_verified]: https://help.instagram.com/854227311295302
[ref_krebs_2013_expired_domains]: https://krebsonsecurity.com/2013/09/data-broker-giants-hacked-by-id-theft-service/
[ref_levick_slavo_2015]: https://web.archive.org/web/2015/https://levick.com/
[ref_linkedin_verification]: https://www.linkedin.com/help/linkedin/answer/a1359065
[ref_megaupload_universal_2011]: https://www.eff.org/cases/megaupload-v-universal
[ref_meta_ai_content_labeling]: https://about.fb.com/news/2024/04/metas-approach-to-labeling-ai-generated-content-and-manipulated-media/
[ref_meta_atr]: https://about.fb.com/news/tag/adversarial-threat-report/
[ref_meta_cib_policy]: https://transparency.meta.com/policies/community-standards/inauthentic-behavior/
[ref_miller_2004_walmart]: https://www.walmartwatch.com/battlemart/working_families/
[ref_mueller_report_2019]: https://www.justice.gov/archives/sco/file/1373816/download
[ref_ny_ag_devumi_2019]: https://ag.ny.gov/press-release/2019/attorney-general-james-announces-groundbreaking-settlement-devumi-owner-german
[ref_openai_chatgpt_2022]: https://openai.com/index/chatgpt/
[ref_openai_gpt4_2023]: https://openai.com/index/gpt-4-research/
[ref_pmi_fraud]: https://www.pmi.org/certifications/ethics
[ref_sec_kardashian_2022]: https://www.sec.gov/news/press-release/2022-183
[ref_sony_psp_2006]: https://www.wired.com/2006/12/sonys-fake-blog/
[ref_source_watch_front]: https://www.sourcewatch.org/index.php/SourceWatch
[ref_twitter_verification_legacy]: https://help.x.com/en/managing-your-account/legacy-verification-policy
[ref_w3c_did]: https://www.w3.org/TR/did-core/
[ref_w3c_verifiable_credentials]: https://www.w3.org/TR/vc-data-model/
[ref_white_ops_methbot_2016]: https://www.humansecurity.com/learn/blog/anatomy-of-methbot
[ref_whole_foods_rahodeb_2007]: https://www.wsj.com/articles/SB118466504114020015
[ref_x_blue]: https://help.x.com/en/using-x/x-blue
[ref_x_transparency_report]: https://transparency.x.com/
[ref_youtube_verification]: https://support.google.com/youtube/answer/3046484
[ref_youtube_view_manipulation_policy]: https://support.google.com/youtube/answer/2801973
[related_post_a277_theory]: {% post_url 2026-01-22-virtual_reputation_manipulation_theory %}
[research_ali_et_al_2017]: https://dl.acm.org/doi/10.1145/3038912.3052649
[research_alvisi_et_al_2013]: https://ieeexplore.ieee.org/document/6547101
[research_anderson_magruder_2012]: https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0297.2012.02512.x
[research_bradshaw_bailey_howard_2021]: https://demtech.oii.ox.ac.uk/research/posts/industrialized-disinformation/
[research_bradshaw_howard_2019]: https://demtech.oii.ox.ac.uk/research/posts/the-global-disinformation-order-2019-global-inventory-of-organised-social-media-manipulation/
[research_boerman_et_al_2018]: https://www.tandfonline.com/doi/full/10.1080/00913367.2017.1408087
[research_bright_et_al_2020]: https://arxiv.org/abs/2004.09114
[research_cao_et_al_2012]: https://www.usenix.org/conference/nsdi12/technical-sessions/presentation/cao
[research_castillo_et_al_2007]: https://dl.acm.org/doi/10.1145/1277741.1277814
[research_chen_et_al_2019]: https://dl.acm.org/doi/10.1145/3308560.3316501
[research_chevalier_mayzlin_2006]: https://www.jstor.org/stable/30162548
[research_chintagunta_gopinath_venkataraman_2010]: https://pubsonline.informs.org/doi/10.1287/mksc.1100.0572
[research_cho_et_al_2011]: https://journals.sagepub.com/doi/10.1177/0894439310396571
[research_cresci_2020]: https://cacm.acm.org/magazines/2020/10/247594-a-decade-of-social-bot-detection/
[research_cresci_et_al_2015]: https://www.sciencedirect.com/science/article/pii/S0167923615001803
[research_cresci_et_al_2017]: https://dl.acm.org/doi/10.1145/3041021.3055135
[research_dambrosio_et_al_2018]: https://arxiv.org/abs/1811.01645
[research_danezis_mittal_2009]: https://www.ndss-symposium.org/wp-content/uploads/2017/09/sybilinfer-detecting-sybil-nodes-using-social-networks.pdf
[research_demicheli_stroppa_2013]: https://arxiv.org/abs/1309.7889
[research_diresta_et_al_2019]: https://digitalcommons.unl.edu/senatedocs/2/
[research_douceur_2002]: https://link.springer.com/chapter/10.1007/3-540-45748-8_24
[research_farooqi_et_al_2017]: https://dl.acm.org/doi/10.1145/3131365.3131388
[research_fei_et_al_2013]: https://ojs.aaai.org/index.php/ICWSM/article/view/14400
[research_feng_et_al_2012]: https://aclanthology.org/P12-2033/
[research_ferrara_et_al_2016]: https://dl.acm.org/doi/10.1145/2818717
[research_gyongyi_garciamolina_2005]: http://ilpubs.stanford.edu:8090/771/
[research_he_hollenbeck_proserpio_2022]: https://pubsonline.informs.org/doi/10.1287/mksc.2022.1353
[research_jindal_liu_2008]: https://dl.acm.org/doi/10.1145/1341531.1341560
[research_kanich_et_al_2011]: https://www.usenix.org/legacy/event/leet11/tech/full_papers/Kanich.pdf
[research_king_pan_roberts_2017]: https://www.cambridge.org/core/journals/american-political-science-review/article/how-the-chinese-government-fabricates-social-media-posts-for-strategic-distraction-not-engaged-argument/4662DB26E2685BAF1485F14369BD137C
[research_kirchenbauer_et_al_2023]: https://arxiv.org/abs/2301.10226
[research_klonick_2018]: https://harvardlawreview.org/2018/04/the-new-governors-the-people-rules-and-processes-governing-online-speech/
[research_kumar_army_2017]: https://dl.acm.org/doi/10.1145/3038912.3052677
[research_kumar_et_al_2017]: https://cs.stanford.edu/~srijan/pubs/rev2-wsdm18.pdf
[research_li_et_al_2014]: https://aclanthology.org/P14-1147/
[research_lim_et_al_2010]: https://dl.acm.org/doi/10.1145/1871437.1871557
[research_luca_2016]: https://www.hbs.edu/faculty/Pages/item.aspx?num=41233
[research_luca_zervas_2016]: https://pubsonline.informs.org/doi/10.1287/mnsc.2015.2304
[research_malbon_2013]: https://link.springer.com/article/10.1007/s10603-013-9241-1
[research_marino_et_al_2023]: https://arxiv.org/abs/2311.01661
[research_mayzlin_dover_chevalier_2014]: https://www.aeaweb.org/articles?id=10.1257/aer.104.8.2421
[research_miramirkhani_et_al_2016]: https://www.ndss-symposium.org/wp-content/uploads/2017/09/dial-one-for-scam-analyzing-and-disrupting-the-technical-support-scam-ecosystem.pdf
[research_motoyama_et_al_2011]: https://www.usenix.org/legacy/event/sec11/tech/full_papers/Motoyama.pdf
[research_mukherjee_et_al_2013]: https://ojs.aaai.org/index.php/ICWSM/article/view/14380
[research_ntoulas_et_al_2006]: https://dl.acm.org/doi/10.1145/1135777.1135794
[research_ott_et_al_2011]: https://aclanthology.org/P11-1032/
[research_ott_et_al_2013]: https://aclanthology.org/N13-1053/
[research_page_brin_1998]: http://infolab.stanford.edu/~backrub/google.html
[research_page_brin_motwani_winograd_1999]: http://ilpubs.stanford.edu:8090/422/
[research_papakyriakopoulos_et_al_2020]: https://dl.acm.org/doi/10.1145/3392866
[research_pearce_et_al_2014]: https://dl.acm.org/doi/10.1145/2660267.2660369
[research_ratkiewicz_et_al_2011]: https://ojs.aaai.org/index.php/ICWSM/article/view/14127
[research_rayana_akoglu_2015]: https://dl.acm.org/doi/10.1145/2783258.2783370
[research_sadasivan_et_al_2023]: https://arxiv.org/abs/2303.11156
[research_sohail_et_al_2024]: https://arxiv.org/abs/2402.01697
[research_solorio_et_al_2014]: https://aclanthology.org/E14-4009/
[research_starbird_2019]: https://www.nature.com/articles/d41586-019-02235-x
[research_stringhini_et_al_2013]: https://arxiv.org/abs/1304.0645
[research_tsikerdekis_zeadally_2014]: https://cacm.acm.org/magazines/2014/9/177933-multiple-account-identity-deception-detection-in-social-media/
[research_wang_et_al_2011]: https://ieeexplore.ieee.org/document/6137345
[research_wang_et_al_2012]: https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/wang
[research_weerkamp_derijke_2012]: https://dl.acm.org/doi/10.1145/2151163.2151168
[research_weller_et_al_2019]: https://arxiv.org/abs/1908.07691
[research_wu_et_al_2020]: https://www.sciencedirect.com/science/article/pii/S014829631930464X
[research_xie_et_al_2012]: https://dl.acm.org/doi/10.1145/2339530.2339662
[research_yang_et_al_2020]: https://onlinelibrary.wiley.com/doi/10.1002/hbe2.115
[research_yang_menczer_2024]: https://arxiv.org/abs/2307.16336
[research_yao_et_al_2017]: https://dl.acm.org/doi/10.1145/3133956.3133994
[research_yu_et_al_2006]: https://dl.acm.org/doi/10.1145/1159913.1159945
[research_yu_et_al_2008]: https://ieeexplore.ieee.org/document/4531149
[research_zannettou_et_al_2018]: https://arxiv.org/abs/1811.07087
[research_zannettou_et_al_2019]: https://dl.acm.org/doi/10.1145/3308560.3316495
[research_zellers_et_al_2019]: https://arxiv.org/abs/1905.12616
[research_zheng_et_al_2011]: https://aclanthology.org/N12-1121/
[ref_accc_v_trivago_2020]: https://www.accc.gov.au/media-release/trivago-ordered-to-pay-447-million-in-penalties-for-misleading-consumers-over-hotel-room-rates
[ref_amazon_reviews_dataset]: https://amazon-reviews-2023.github.io/
[ref_bot_repository]: https://botometer.osome.iu.edu/bot-repository/
[ref_canada_amazon]: https://competition-bureau.canada.ca/en/deceptive-marketing-practices/types-deceptive-marketing-practices/testimonials-and-endorsements
[ref_cresci_2015_dataset]: https://botometer.osome.iu.edu/bot-repository/datasets.html
[ref_cresci_2017_dataset]: https://botometer.osome.iu.edu/bot-repository/datasets.html
[ref_fakespot_consumer_reports]: https://www.fakespot.com/
[ref_fido_alliance]: https://fidoalliance.org/specifications/
[ref_ftc_bountiful_2023]: https://www.ftc.gov/legal-library/browse/cases-proceedings/2023127-bountiful-company
[ref_ftc_roomster_2022]: https://www.ftc.gov/legal-library/browse/cases-proceedings/2223059-roomster-corp
[ref_google_business_profile_guidelines]: https://support.google.com/business/answer/3038177
[ref_iab_ad_fraud_report]: https://www.iab.com/insights/topics/ad-fraud/
[ref_instagram_authenticity_guidelines]: https://help.instagram.com/477434105621119
[ref_italy_agcm_booking]: https://en.agcm.it/en/agcm-media/press-releases/
[ref_mrc_viewability_standards]: https://mediaratingcouncil.org/standards
[ref_nielsen_trust_advertising]: https://www.nielsen.com/insights/2021/trust-in-advertising-2021/
[ref_ott_deceptive_corpus]: https://myleott.com/op-spam.html
[ref_trustpilot_transparency]: https://uk.business.trustpilot.com/reviews/build-trusted-brand/trustpilot-transparency-report
[ref_uk_cma_facebook_google_2022]: https://www.gov.uk/cma-cases/online-reviews-facebook-and-google
[ref_w3c_webauthn]: https://www.w3.org/TR/webauthn/
[ref_x_platform_manipulation_policy]: https://help.x.com/en/rules-and-policies/platform-manipulation
[ref_yelp_content_guidelines]: https://www.yelp-support.com/article/Yelp-Content-Guidelines
[ref_yelpchi_dataset]: https://odds.cs.stonybrook.edu/yelpchi-dataset/
[book_aaker_1991]: https://www.simonandschuster.com/books/Managing-Brand-Equity/David-A-Aaker/9781451602364
[book_abidin_2018]: https://www.emerald.com/insight/publication/doi/10.1108/9781787560789
[book_berger_2016]: https://www.simonandschuster.com/books/Contagious/Jonah-Berger/9781451686586
[book_bernays_1923]: https://archive.org/details/crystallizingpub00bern
[book_bernays_1928]: https://www.igpublishing.com/product/propaganda/
[book_cialdini_1984]: https://www.harpercollins.com/products/influence-new-and-expanded-robert-b-cialdini-phd
[book_cronin_2004]: https://www.routledge.com/Advertising-Myths/Cronin/p/book/9780415310086
[book_cutlip_1994]: https://www.routledge.com/The-Unseen-Power/Cutlip/p/book/9780805814644
[book_duffy_2017]: https://yalebooks.yale.edu/book/9780300218176/not-getting-paid-to-do-what-you-love/
[book_ewen_1996]: https://www.basicbooks.com/titles/stuart-ewen/pr/9780465061792/
[book_fiske_taylor_2013]: https://us.sagepub.com/en-us/nam/social-cognition/book238262
[book_fitzpatrick_2005]: https://www.amazon.com/False-Profits-Seeking-Financial-Multi-Level/dp/0964879514
[book_godin_2018]: https://sethgodin.com/books/
[book_greif_2006]: https://www.cambridge.org/9780521671347
[book_katz_lazarsfeld_1955]: https://www.routledge.com/Personal-Influence/Katz-Lazarsfeld/p/book/9781412805070
[book_kotler_keller_2016]: https://www.pearson.com/us/higher-education/product/Kotler-Marketing-Management-15th-Edition/9780133856460.html
[book_lippmann_1922]: https://www.simonandschuster.com/books/Public-Opinion/Walter-Lippmann/9781416573104
[book_marwick_2013]: https://yalebooks.yale.edu/book/9780300209389/status-update/
[book_nisbett_ross_1980]: https://scholar.google.com/scholar?q=nisbett+ross+1980+human+inference
[book_ogilvie_2019]: https://press.princeton.edu/books/hardcover/9780691137544/the-european-guilds
[book_ogilvy_1963]: https://www.penguinrandomhouse.com/books/300340/confessions-of-an-advertising-man-by-david-ogilvy/
[book_packard_1957]: https://ighland-books.com/hidden-persuaders
[book_petty_2015]: https://global.oup.com/academic/product/the-codevelopment-of-marketing-law-and-practice-9781785365874
[book_presbrey_1929]: https://archive.org/details/historyanddevelo00pres
[book_provost_fawcett_2013]: https://www.oreilly.com/library/view/data-science-for/9781449374273/
[book_reeves_1961]: https://scholar.google.com/scholar?q=rosser+reeves+1961+reality+in+advertising
[book_silverman_2001]: https://scholar.google.com/scholar?q=silverman+2001+secrets+of+word+of+mouth+marketing
[book_strasser_1989]: https://www.smithsonianmag.com/books/satisfaction-guaranteed
[book_taylor_2011]: https://scholar.google.com/scholar?q=taylor+2011+case+for+against+multi-level+marketing
[book_trivellato_2009]: https://yalebooks.yale.edu/book/9780300172416/the-familiarity-of-strangers/
[book_turow_2011]: https://yalebooks.yale.edu/book/9780300188011/the-daily-you/
[book_twede_selke_2005]: https://www.destechpub.com/product/cartons-crates-corrugated-board
[book_tye_1998]: https://www.penguinrandomhouse.com/books/153822/the-father-of-spin-by-larry-tye/
[book_wu_2016]: https://www.penguinrandomhouse.com/books/232292/the-attention-merchants-by-tim-wu/
[book_young_1961]: https://press.princeton.edu/books/paperback/9780691623429/the-toadstool-millionaires
[ref_barnum_autobiography_1854]: https://www.gutenberg.org/ebooks/29467
[ref_ftc_amway_1979]: https://www.ftc.gov/legal-library/browse/cases-proceedings/932-3111-amway-corporation
[ref_ftc_herbalife_2016]: https://www.ftc.gov/legal-library/browse/cases-proceedings/152-3208-herbalife-international-america-inc
[ref_ftc_herbalife_2022]: https://www.ftc.gov/legal-library/browse/cases-proceedings/152-3208-herbalife-international-america-inc
[ref_ftc_nutrilite_1951]: https://scholar.google.com/scholar?q=ftc+nutrilite+products+1951
[ref_ivy_lee_declaration_1906]: https://www.prsa.org/about/ethics/
[research_beales_1980]: https://scholar.google.com/scholar?q=beales+1980+efficient+regulation+consumer+information
[research_bishop_2019]: https://journals.sagepub.com/doi/10.1177/1354856517736978
[research_chaiken_1980]: https://psycnet.apa.org/record/1981-05463-001
[research_chandola_banerjee_kumar_2009]: https://dl.acm.org/doi/10.1145/1541880.1541882
[research_diamond_1971]: https://www.sciencedirect.com/science/article/abs/pii/0022053171900130
[research_fawcett_2006]: https://www.sciencedirect.com/science/article/abs/pii/S016786550500303X
[research_goodfellow_shlens_szegedy_2014]: https://arxiv.org/abs/1412.6572
[research_hoffman_2017]: https://scholar.google.com/scholar?q=hoffman+2017+sponsored+content+regulation
[research_kumar_shah_2018]: https://arxiv.org/abs/1804.08559
[research_mccracken_1989]: https://www.jstor.org/stable/2489287
[research_petty_andrews_2008]: https://journals.sagepub.com/doi/10.1509/jppm.27.1.7
[research_petty_cacioppo_1986]: https://link.springer.com/chapter/10.1007/978-1-4612-4964-1_1
[research_rochet_tirole_2003]: https://www.jstor.org/stable/40005933
[research_rothschild_1974]: https://www.jstor.org/stable/1830634
[research_rysman_2009]: https://www.aeaweb.org/articles?id=10.1257/jep.23.3.125
[research_simon_1971]: https://digitalcollections.library.cmu.edu/awweb/awarchive?type=file&item=33748
[research_stigler_1961]: https://www.jstor.org/stable/1829263
[research_stigler_1971]: https://www.jstor.org/stable/3003160
[research_trusov_bucklin_pauwels_2009]: https://journals.sagepub.com/doi/10.1509/jmkg.73.5.90
