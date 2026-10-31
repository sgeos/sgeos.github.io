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

$$
\mathbf{a}_k = (a_k^{\text{signal}}, a_k^{\text{obj}}, a_k^{\text{struct}}, a_k^{\text{model}}, a_k^{\text{interact}}, a_k^{\text{adapt}})
\tag{1}
$$

with each axis value drawn from an axis-specific space. The distance between techniques on the axis-vector space admits characterization as

$$
d(t_j, t_k) = \sum_{c \in \text{axes}} w_c \, \delta_c(a_j^c, a_k^c)
\tag{2}
$$

with $w_c$ the axis weight and $\delta_c$ the axis-specific distance function. The technique-space partition into the groupings above corresponds to clustering under the distance $d$ with the review-signal, engagement-signal, and search-ranking groupings emerging as the natural clusters under channel-weighted distance.

The aggregate empirical prevalence of self-promotion techniques across the reputation ecosystem permits estimation through the sum

$$
V_{\text{self-promo}}(t) = \sum_{k \in \mathcal{T}} \sum_{c \in \text{categories}} n_{k,c}(t) \cdot p_{k,c}(t)
\tag{3}
$$

with $n_{k,c}(t)$ the signal-event volume for technique $k$ in category $c$ at time $t$ and $p_{k,c}(t)$ the technique-and-category-specific prevalence rate. The empirical estimates surveyed in this article establish that $V_{\text{self-promo}}$ dominates the aggregate manipulation volume across most platform categories, with only political-manipulation-dominant contexts (state-sponsored operations targeting elections) exhibiting comparable competitor-attack volume.

The taxonomy's coverage completeness against the observed technique population allows characterization as the recall-analog statistic

$$
\text{Coverage}(\mathcal{T}, \Omega) = \frac{|\{\omega \in \Omega : \exists t_k \in \mathcal{T}, \omega \text{ assigned to } t_k\}|}{|\Omega|}
\tag{4}
$$

with $\Omega$ the observed manipulation-instance population. The taxonomy the article adopts targets $\text{Coverage} > 0.95$ against the enforcement-record and academic-detection-corpus population and treats residual instances outside the taxonomy as novel-technique candidates for taxonomy revision.

## Cross-Disciplinary Framings

The self-promotion technique landscape supports characterization from several disciplinary traditions beyond the economic-signaling framework the miniseries adopts as primary. The framing article surveys the principal alternative disciplinary treatments and identifies their analytical leverage.

The marketing-and-advertising-theory framing traces from [Aaker 1991][book_aaker_1991] Managing Brand Equity through [Kotler and Keller 2016][book_kotler_keller_2016] Marketing Management and the broader marketing literature. The framing treats self-promotion techniques as extensions of the traditional advertising and word-of-mouth marketing toolkit into digital reputation systems. The [Berger 2016][book_berger_2016] Contagious Why Things Catch On treatment addresses the contemporary word-of-mouth-adjacent literature. The [Godin 2018][book_godin_2018] This is Marketing treatment addresses the practitioner-side framing of the transition from broadcast advertising to earned-reputation marketing. The [Trusov et al. 2009][research_trusov_bucklin_pauwels_2009] Effects of Word-of-Mouth versus Traditional Marketing treatment provides the reference empirical framework for the word-of-mouth-effectiveness comparison. The marketing-and-advertising framing complements the reputation-manipulation framing by treating the manipulation technique as a boundary case of legitimate promotion rather than as a categorically distinct phenomenon, which surfaces the technique-vs-legitimate-promotion boundary that regulatory frameworks must draw.

The consumer-behavior-and-persuasion-psychology framing traces from [Cialdini 1984][book_cialdini_1984] Influence through the [Petty and Cacioppo 1986][research_petty_cacioppo_1986] Elaboration Likelihood Model of Persuasion framework and the [Chaiken 1980][research_chaiken_1980] Heuristic Systematic Model treatment. The framing identifies the cognitive and motivational mechanisms through which reputation signals influence consumer decision-making, and characterizes self-promotion techniques by the persuasion mechanisms they exploit. The [Fiske and Taylor 2013][book_fiske_taylor_2013] Social Cognition treatment provides the comprehensive social-cognition framework. The [Nisbett and Ross 1980][book_nisbett_ross_1980] Human Inference treatment provides the classical cognitive-heuristics framework relevant to reputation-signal processing. The consumer-behavior framing complements the reputation-manipulation framing by predicting the consumer-response effects of different manipulation techniques based on the technique's alignment with dominant persuasion pathways.

The search-theory-and-information-economics framing traces from [Stigler 1961][research_stigler_1961] The Economics of Information through [Rothschild 1974][research_rothschild_1974] Searching for the Lowest Price When the Distribution of Prices is Unknown and the subsequent search-theory literature. The framing treats reputation signals as inputs to the consumer's search process and characterizes self-promotion techniques by the search-process distortions they produce. The [Diamond 1971][research_diamond_1971] Model of Price Adjustment treatment addresses the equilibrium effect of search costs on price. The search-theory framing complements the reputation-manipulation framing by identifying the consumer-search-cost changes that manipulation techniques impose and the equilibrium market-price and quality-signaling effects that follow.

The multi-level-marketing and network-marketing framing addresses the organizational form under which reputation-manipulation-adjacent practices operate. The [Fitzpatrick 2005][book_fitzpatrick_2005] False Profits treatment provides the industry-analytical framing. The [Taylor 2011][book_taylor_2011] The Case for and Against Multi-Level Marketing treatment provides the case-based analysis. The [FTC 2022 Herbalife Order][ref_ftc_herbalife_2022] and the [FTC 2016 Herbalife Order][ref_ftc_herbalife_2016] establish the reference regulatory precedent for the MLM-adjacent reputation-manipulation subset. The multi-level-marketing framing complements the reputation-manipulation framing by identifying the organizational structures that generate self-promotion at the population scale characteristic of MLM networks.

The computer-science-of-detection framing traces from the [Fawcett 2006][research_fawcett_2006] Introduction to ROC Analysis through the [Chandola et al. 2009][research_chandola_banerjee_kumar_2009] Anomaly Detection A Survey and the subsequent anomaly-detection literature. The framing treats self-promotion detection as a classification-with-imbalanced-classes problem with accuracy-versus-friction tradeoffs. The [Provost and Fawcett 2013][book_provost_fawcett_2013] Data Science for Business treatment addresses the applied-industry framing. The computer-science framing complements the reputation-manipulation framing by identifying the detection-methodology constraints and opportunities that determine the equilibrium detection-versus-manipulation intensity.

The legal-scholarship-of-false-advertising framing traces from [Beales et al. 1981][research_beales_1980] Efficient Regulation of Consumer Information through [Petty 2015][book_petty_2015] The Codevelopment of Marketing Law and Practice and the modern-era false-advertising-and-endorsement scholarship. The framing treats self-promotion techniques as boundary-cases of the false-advertising regulatory framework and characterizes the FTC and Lanham Act application to the digital-reputation environment. The [Petty and Andrews 2008][research_petty_andrews_2008] Covert Marketing Unmasked treatment addresses the covert-marketing-and-testimonial issues. The [FTC Endorsement Guides framework][ref_ftc_endorsement_guides_16_cfr_255] provides the reference regulatory framework. The legal-scholarship framing complements the reputation-manipulation framing by identifying the regulatory-and-enforcement dimensions that shape the technique-vs-legitimate-promotion boundary.

The critical-media-studies-of-influencer-marketing framing traces from [Abidin 2018][book_abidin_2018] Internet Celebrity through [Duffy 2017][book_duffy_2017] Not Getting Paid to Do What You Love and the broader influencer-and-creator-economy literature. The framing treats self-promotion techniques within the broader political-economy of influencer marketing and the labor-and-authenticity dynamics of the creator economy. The [Bishop 2018][research_bishop_2019] Managing Visibility on YouTube through Algorithmic Gossip treatment addresses the platform-algorithm-and-influencer dynamic. The [Marwick 2013][book_marwick_2013] Status Update treatment addresses the broader status-and-visibility economy. The critical-media-studies framing complements the reputation-manipulation framing by treating manipulation as embedded in a broader creator-economy political-economy rather than as a purely technical phenomenon.

## Historical Antecedents

Self-promotion reputation manipulation is not a novel phenomenon of the digital era. The technique inventory inherits significant doctrine, practice, and organizational form from pre-digital antecedents in advertising, public relations, endorsement marketing, and coordinated promotional operations. The framing article surveys the principal historical antecedents and identifies the continuities and discontinuities with the digital-era inventory.

The pre-industrial antecedents include the guild-and-merchant-reputation-cultivation practices of medieval and early-modern commerce, in which merchants coordinated their reputation-signaling through guild membership, apprenticeship-credential display, and repeat-transaction-based trust. The [Trivellato 2009][book_trivellato_2009] The Familiarity of Strangers and the [Greif 2006][book_greif_2006] Institutions and the Path to the Modern Economy treatments document the pre-industrial reputation-signaling infrastructure. The [Ogilvie 2019][book_ogilvie_2019] The European Guilds treatment addresses the guild reputation-management infrastructure.

The nineteenth-century patent-medicine and mail-order eras produced substantial self-promotion technique innovation. The [Young 1961][book_young_1961] The Toadstool Millionaires treatment documents the American patent-medicine testimonial practice. The [Twede and Selke 2005][book_twede_selke_2005] Cartons Crates and Corrugated Board and the [Presbrey 1929][book_presbrey_1929] The History and Development of Advertising treatments document the parallel evolution of packaging-and-advertising infrastructure. The [Strasser 1989][book_strasser_1989] Satisfaction Guaranteed The Making of the American Mass Market treatment addresses the mass-market emergence and the associated reputation-and-branding infrastructure development. The [PT Barnum autobiography 1854][ref_barnum_autobiography_1854] documents the era's most famous self-promotion practitioner.

The early-twentieth-century public-relations-industry founding established the professional organizational form for coordinated self-promotion. The [Bernays 1923][book_bernays_1923] Crystallizing Public Opinion and [Bernays 1928][book_bernays_1928] Propaganda treatments established the doctrinal framework. The [Lippmann 1922][book_lippmann_1922] Public Opinion treatment provided the theoretical framing. The [PRSA Code of Ethics 1906][ref_ivy_lee_declaration_1906] established the industry's professional-ethics framework. The [Ewen 1996][book_ewen_1996] PR A Social History of Spin and [Tye 1998][book_tye_1998] The Father of Spin treatments provide the historical analysis. The [Cutlip 1994][book_cutlip_1994] The Unseen Power Public Relations A History treatment provides the comprehensive industry history.

The mid-twentieth-century direct-marketing and motivation-research eras produced the psychographic-targeting infrastructure that provides the substrate for contemporary personalized reputation-manipulation. The [Packard 1957][book_packard_1957] The Hidden Persuaders treatment documents the motivation-research industry. The [Ogilvy 1963][book_ogilvy_1963] Confessions of an Advertising Man treatment addresses the modernization of advertising practice. The [Reeves 1961][book_reeves_1961] Reality in Advertising treatment addresses the parallel unique-selling-proposition framework. The [Turow 2011][book_turow_2011] The Daily You treatment traces the transition to digital psychographic targeting.

The late-twentieth-century celebrity-endorsement and infomercial eras produced marked technique innovation in the coordinated-testimonial and long-form-promotion spaces. The [McCracken 1989][research_mccracken_1989] Who Is the Celebrity Endorser Cultural Foundations of the Endorsement Process treatment provides the celebrity-endorsement theoretical framework. The [Cronin 2004][book_cronin_2004] Advertising Myths The Strange Half-Lives of Images and Commodities treatment addresses the era's cultural-and-communication analysis. The [FTC Nutrilite Products 1951 Order][ref_ftc_nutrilite_1951] represents the historical regulatory-enforcement precedent applicable to the era's practices.

The astroturfing tradition of manufactured grassroots support traces to political-operations practice from the mid twentieth century forward, with extensive precedent in corporate lobbying campaigns of tobacco, oil, and pharmaceutical industries. The [Oreskes and Conway 2010][book_oreskes_conway_2010] Merchants of Doubt, [McGarity and Wagner 2008][book_mcgarity_wagner_2008] Bending Science, and [Michaels 2008][book_michaels_2008] Doubt Is Their Product treatments document the coordinated-denial-and-manufactured-support playbook. The term astroturf itself traces to [Senator Lloyd Bentsen's 1985 Congressional Record][ref_bentsen_congressional_record_1985] characterization. The [Walker 2014][book_walker_2014] Grassroots for Hire treatment consolidates the contemporary industry analysis.

The direct-marketing-database and multi-level-marketing organizational forms established the population-scale coordination infrastructure that enables contemporary reputation-manipulation at scale. The [FTC v Amway 1979 decision][ref_ftc_amway_1979] and subsequent MLM-related enforcement establish the regulatory framework. The [Fitzpatrick 2005][book_fitzpatrick_2005] False Profits treatment provides the industry-critical analysis. The multi-level-marketing organizational form produces the self-promotion-at-population-scale dynamic that enables coordinated reputation-manipulation across large distributor networks.

## Historiographical Gap and Recent Scholarship

The scholarly treatment of self-promotion reputation manipulation has developed unevenly across disciplines and has integrated less well across traditions than the technical-detection literature. The framing article surveys the observable gap and identifies the recent-scholarship developments that the miniseries builds on.

The marketing-and-advertising scholarship developed continuously from the mid-twentieth-century advertising-industry literature through the contemporary integrated-marketing-communications framework. The application to digital-reputation-manipulation is less developed within the marketing tradition than within the reputation-systems tradition, with the marketing-side treatment typically framing reputation-manipulation as either legitimate word-of-mouth marketing (understating the manipulation dimension) or as unethical practice without technical detail (understating the technique dimension). The [Silverman 2001][book_silverman_2001] Secrets of Word-of-Mouth Marketing and the [Kotler and Keller 2016][book_kotler_keller_2016] treatment illustrate the marketing-side framing.

The consumer-behavior scholarship developed continuously from the classical [Katz and Lazarsfeld 1955][book_katz_lazarsfeld_1955] Personal Influence framework through the contemporary behavioral-economics-and-neuroscience literature. The application to fake-review-effect-on-consumer-choice is developed in the [Chevalier and Mayzlin 2006][research_chevalier_mayzlin_2006], [Luca 2016][research_luca_2016], and adjacent empirical treatments. The gap between the consumer-behavior tradition and the technical-detection tradition remains considerably unbridged, with the consumer-behavior tradition treating reputation signals as inputs to the consumer's decision-process without addressing the signal-manipulation dimension in detail.

The computer-science-of-detection scholarship developed continuously from the [Jindal and Liu 2008][research_jindal_liu_2008] initial framework through the contemporary adversarial-ML-adjacent literature. The application to fake-review-detection is the most-developed subfield of the reputation-manipulation-detection literature. The [Cresci 2020][research_cresci_2020] survey establishes the reference summary. The [Kumar and Shah 2018][research_kumar_shah_2018] False Information on Web and Social Media survey provides the parallel-summary for the broader misinformation-adjacent detection subfield.

The influencer-and-creator-economy scholarship developed rapidly in the 2010s and 2020s in response to the rise of influencer marketing. The [Abidin 2018][book_abidin_2018] Internet Celebrity, [Duffy 2017][book_duffy_2017] Not Getting Paid, [Bishop 2018][research_bishop_2019] Managing Visibility on YouTube, and adjacent treatments establish the field. The integration with the reputation-manipulation detection tradition is emerging but not yet consolidated.

The legal-scholarship-of-endorsement-regulation developed through the FTC endorsement-guides history from 1980 through 2024 and the associated academic commentary. The [Petty and Andrews 2008][research_petty_andrews_2008] treatment, the [Hoffman 2017][research_hoffman_2017] Sponsored Content Regulation, and the [Boerman 2018][research_boerman_et_al_2018] Sponsored Content Disclosure Effects treatments establish the reference framework. The gap between the legal-scholarship treatment and the technical-detection treatment remains significantly unbridged, with the legal treatment typically framing manipulation as an enforcement problem without addressing the detection-methodology dimension in detail.

The historiographical gap that the miniseries addresses lies in the absence of an integrated treatment drawing on all five traditions simultaneously. Each tradition treats a portion of the self-promotion manipulation phenomenon, and the standard treatment requires all five. The miniseries organizes the material to make the cross-tradition connections explicit where they are load-bearing for the analytical conclusions.

## Review Manipulation Techniques

The review-signal manipulation class comprises the technique inventory oriented at the star-rating and text-review signals that consumer-facing reputation systems make available. The class is the empirically dominant self-promotion class in consumer-review platforms and has received substantially more academic detection attention than any other class.

### Individual Review Fabrication

Individual review fabrication refers to the manipulation practice in which an actor (or a party acting on the actor's behalf) writes and submits favorable reviews for the actor's own product or service without disclosing the material connection. The practice is the simplest and historically earliest self-promotion technique documented in the digital reputation ecosystem. Documented cases include the [Bing 2004 astroturf blogging incident][ref_bing_2004_astroturf] involving Microsoft-affiliated bloggers writing favorable coverage of Microsoft products, the [Sony PlayStation Portable 2006 fake blog case][ref_sony_psp_2006] involving a Sony-commissioned blog written to appear as unaffiliated fan content, and the [Whole Foods Mackey Rahodeb 2007][ref_whole_foods_rahodeb_2007] in which the CEO of Whole Foods was found to have written pseudonymous positive commentary on Yahoo Finance about Whole Foods over a seven-year period. The [FTC v Sunday Riley 2019][ref_ftc_sunday_riley_2019] action addressed employee-written fake reviews on Sephora at the direction of the brand's CEO. The [FTC v UrthBox 2019][ref_ftc_urthbox_2019] action addressed influencer-written reviews without disclosed material connection. The [Beuk Boekhandel 2013][ref_beuk_boekhandel_2013] Dutch case established European jurisprudence on fake-review liability.

The academic detection literature for individual fabrication traces to [Jindal and Liu 2008][research_jindal_liu_2008] Opinion Spam and Analysis, which established the field's initial taxonomy and detection methodology. The stylometric-feature vector on which contemporary detectors operate takes the compact form

$$
\mathbf{f}_r = (\text{POS-ratios}, \text{n-gram distributions}, \text{lexical richness}, \text{sentiment intensity}, \text{first-person ratio}, \text{superlative rate})
\tag{5}
$$

with each component estimated on the review text $r$ and fed to a downstream classifier. The [Ott et al. 2011][research_ott_et_al_2011] Finding Deceptive Opinion Spam by Any Stretch of the Imagination treatment introduced the labeled-corpus methodology by crowdsourcing production of deceptive reviews and training classifiers on the resulting distribution. The [Ott et al. 2013][research_ott_et_al_2013] Negative Deceptive Opinion Spam extended the framework. The [Feng 2012][research_feng_et_al_2012] Syntactic Stylometry for Deception Detection treatment introduced the syntactic-features detection approach. The [Li et al. 2014][research_li_et_al_2014] Towards a General Rule for Identifying Deceptive Opinion Spam introduced the cross-domain generalization framework.

The empirical prevalence of individual review fabrication varies by platform and category. The [Luca and Zervas 2016][research_luca_zervas_2016] Yelp analysis estimates approximately sixteen percent of Yelp restaurant reviews are filtered as suspicious by Yelp's internal classifier, with the filtered rate rising to approximately twenty percent for restaurants in competitive market segments and rising further under competitive conditions. The [Luca 2016][research_luca_2016] Reviews Reputation and Revenue Yelp treatment estimates the causal impact of a one-star rating increase as approximately five to nine percent revenue increase, which sets the direct commercial incentive for review manipulation. The empirical rating-shift model takes the form

$$
\Delta r_i^{\text{obs}} = \Delta r_i^{\text{authentic}} + n_i^{\text{fake}} \cdot (\bar{r}_{\text{fake}} - \bar{r}_{\text{pre}}) / (N_i + n_i^{\text{fake}})
\tag{6}
$$

with $\Delta r_i^{\text{obs}}$ the observed rating change, $\Delta r_i^{\text{authentic}}$ the authentic rating change, $n_i^{\text{fake}}$ the injected fake-review count, $\bar{r}\_{\text{fake}}$ the average fake-review rating, $\bar{r}\_{\text{pre}}$ the pre-injection average rating, and $N_i$ the pre-injection authentic-review count. The equation shows that fake-review effectiveness depends on the ratio $n_i^{\text{fake}} / N_i$, which is highest for new or low-review-volume businesses and lowest for established high-review-volume businesses.

The detection signatures for individual fabrication include stylometric anomalies (deceptive text tends to over-use first-person pronouns, super-positive adjectives, and quality claims), temporal anomalies (concentrated review bursts inconsistent with the natural arrival rate), reviewer-history anomalies (reviewers with no prior activity or with review histories concentrated on the target business), and IP and device fingerprint anomalies (reviews originating from IP ranges or devices associated with the business owner or with review-service operators). The classifier-based detection takes the form the standard classification-performance metrics

$$
\text{precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}, \quad \text{recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}, \quad F_1 = \frac{2 \cdot \text{precision} \cdot \text{recall}}{\text{precision} + \text{recall}}
\tag{7}
$$

with the classifier's decision threshold $\tau$ tuning the tradeoff between the two errors along the receiver-operating characteristic. The empirical detection accuracy under the [Ott et al. 2011][research_ott_et_al_2011] framework reaches approximately ninety percent on the labeled crowdsourced corpus but degrades markedly on real-world reviews where the labeled ground truth is uncertain. The [Mukherjee 2013][research_mukherjee_et_al_2013] What Yelp Fake Review Filter Might Be Doing treatment reverse-engineers Yelp's production filter and estimates its precision at approximately eighty percent under the paper's evaluation methodology. The temporal-anomaly detection statistic for review-arrival bursts is captured by the standardized arrival-rate residual

$$
z_{\text{burst}}(t) = \frac{\lambda(t) - \bar{\lambda}}{\sigma_\lambda}
\tag{8}
$$

with $\lambda(t)$ the observed review-arrival rate at time $t$, $\bar{\lambda}$ the historical mean arrival rate, and $\sigma_\lambda$ the historical standard deviation. Detection thresholds typically set $z_{\text{burst}} > 3$ as the anomaly trigger.

The platform countermeasures for individual fabrication include the classifier-based filters treated in the detection literature, verified-purchase requirements that constrain the review-eligible actor population, and post-hoc removal of reviews that trigger filter thresholds. The [Amazon Community Guidelines][ref_amazon_community_guidelines] establish the platform's anti-manipulation policy, and the [Amazon v Fake Review 2022][ref_amazon_v_fake_review_brokers_2022] private-action campaign has produced settlements with multiple marketplace intermediaries. The [Yelp Content Guidelines][ref_yelp_content_guidelines] establish parallel policy for the Yelp platform. The [Google Business Profile guidelines][ref_google_business_profile_guidelines] establish the parallel policy for Google Reviews. The [FTC 2024 Final Rule on Fake Reviews and Testimonials][ref_ftc_final_rule_2024] provides the federal regulatory framework that applies to individual fabrication as well as to the coordinated-campaign class. The [FTC v Bountiful Company 2023][ref_ftc_bountiful_2023] action addressed review-hijacking practice in which the target manufacturer moved product listings to inherit unrelated positive-review histories. The [FTC v Roomster 2022][ref_ftc_roomster_2022] action addressed a rental-listing platform's use of fake reviews to inflate listing reputation. The academic detection literature is supported by standing labeled datasets including the [Ott Deceptive Opinion Spam Corpus][ref_ott_deceptive_corpus] and the [YelpChi Fake Review Dataset][ref_yelpchi_dataset] that anchor the reproducibility of the detection-classifier evaluation.

### Coordinated Review Campaigns and Review Farming

Coordinated review campaigns extend individual fabrication to a coordinated operation that produces reviews at scale through multiple operator accounts. Review farming refers specifically to the industrialized production of reviews-for-hire through professional operator networks, with the operators recruited from labor markets in which the per-review compensation is competitive with alternative low-skilled remote work. The industry has been documented most extensively in the [He et al. 2022][research_he_hollenbeck_proserpio_2022] Market for Fake Reviews treatment, which analyzed the exchange between Amazon sellers and organized fake-review Facebook groups. The paper documents approximately 1,500 sellers active in the fake-review marketplace during the 2020-2021 study period, with the reviews-for-purchase transactions involving free products in exchange for five-star reviews and follow-up cash payment.

The [Mayzlin et al. 2014][research_mayzlin_dover_chevalier_2014] Promotional Reviews treatment compared Tripadvisor and Expedia hotel reviews and found systematic patterns consistent with hotels manipulating their own reviews on Tripadvisor (which permits unverified reviews) at higher rates than on Expedia (which requires booking-verified reviews). The rate-differential estimate provides the natural-experiment approach to prevalence estimation. The [Wu et al. 2020][research_wu_et_al_2020] Fake Online Reviews Literature Review survey consolidates the empirical literature and identifies the aggregate prevalence range across studies.

The economics of review farming admit compact characterization. The marketplace price per fabricated review is approximately

$$
p_{\text{fake-review}} \in [1, 30] \text{ USD per review}
\tag{9}
$$

with the lower bound reflecting text-only reviews on low-enforcement platforms and the upper bound reflecting verified-purchase reviews on high-enforcement platforms including sale-of-product cost. The producer surplus per manipulated business, absent detection, follows

$$
\pi_i^{\text{manip}} = R_i^{\text{shift}} \cdot v \cdot Q_i - n_i \cdot p_{\text{fake-review}}
\tag{10}
$$

with $R_i^{\text{shift}}$ the rating shift produced by the injection, $v$ the per-rating-point revenue coefficient, $Q_i$ the sales volume elasticity, and $n_i$ the injected review count. The equation identifies the marginal return per additional fake review as the sales-volume increase net of the marginal fake-review production cost. International enforcement includes the [ACCC v Trivago 2020][ref_accc_v_trivago_2020] Australian case addressing misleading ranking practices, the [UK CMA fake reviews investigation 2022][ref_uk_cma_facebook_google_2022] into Facebook and Google fake-review markets, the [Canadian Competition Bureau v Amazon][ref_canada_amazon] fake-review enforcement, and the [Italian AGCM Booking.com fake reviews][ref_italy_agcm_booking] action. The temporal-arrival pattern of coordinated review campaigns is captured by the self-exciting Hawkes point process

$$
\lambda(t) = \mu + \alpha \sum_{t_i < t} e^{-\beta(t - t_i)}
\tag{11}
$$

with $\mu$ the baseline arrival rate, $\alpha$ the self-excitation gain, and $\beta$ the decay rate. Coordinated-campaign arrivals exhibit $\alpha$ appreciably above the null-hypothesis baseline, producing the characteristic burst-and-decay pattern that admits detection via the [Xie et al. 2012][research_xie_et_al_2012] temporal-pattern framework. The [Chevalier and Mayzlin 2006][research_chevalier_mayzlin_2006] Effect of Word of Mouth on Sales established the causal-effect literature for book sales; the subsequent [Chintagunta et al. 2010][research_chintagunta_gopinath_venkataraman_2010] treatment for movie box office and the [Anderson and Magruder 2012][research_anderson_magruder_2012] treatment for restaurant demand extended the account.

Detection signatures for coordinated review campaigns include the individual-fabrication signatures plus network-anomaly signatures. Coordinated reviews often exhibit temporal clustering (bursts of reviews arriving within hours or days), textual similarity (shared templates or paraphrased content), reviewer-graph clustering (reviewers who exclusively review the same set of businesses), and account-provenance clustering (accounts registered from the same IP range or with the same device fingerprint). The [Lim et al. 2010][research_lim_et_al_2010] Detecting Product Review Spammers treatment introduced the reviewer-behavior graph-analysis approach. The [Wang et al. 2011][research_wang_et_al_2011] Review Graph based Online Store Review Spammer Detection introduced the review-graph framework. The [Xie et al. 2012][research_xie_et_al_2012] Review Spam Detection via Temporal Pattern Discovery introduced the temporal-anomaly framework. The [Fei et al. 2013][research_fei_et_al_2013] Exploiting Burstiness in Reviews introduced the burst-detection framework. The [Rayana and Akoglu 2015][research_rayana_akoglu_2015] Collective Opinion Spam Detection introduced the network-embedding framework that combines review, reviewer, and product signals. The [Kumar 2017][research_kumar_et_al_2017] Understanding Rating Distributions provides the distributional-anomaly framework at scale.

The text-similarity detection statistic for coordinated review campaigns reduces to cosine similarity in an embedding space or via n-gram overlap. The n-gram-overlap statistic between two reviews $r_i$ and $r_j$ takes the form

$$
\text{sim}_n(r_i, r_j) = \frac{|N_n(r_i) \cap N_n(r_j)|}{|N_n(r_i) \cup N_n(r_j)|}
\tag{12}
$$

with $N_n(r)$ the set of $n$-grams appearing in review $r$. Detection thresholds typically set $\text{sim}\_n > 0.5$ for $n = 4$ as the coordination trigger. The reviewer-graph community-detection statistic can be characterized as the modularity function

$$
Q = \frac{1}{2m} \sum_{ij} \left[A_{ij} - \frac{k_i k_j}{2m}\right] \delta(c_i, c_j)
\tag{13}
$$

with $A_{ij}$ the reviewer-business adjacency, $k_i$ the reviewer-degree, $m$ the total edge count, $c_i$ the community assignment, and $\delta(c_i, c_j)$ the community-match indicator. Coordinated-review clusters exhibit anomalously high $Q$ concentrated on small reviewer subsets, and the detection algorithm identifies suspicious clusters as high-$Q$ dense subgraphs. The academic detection accuracy under the network-based approaches reaches approximately ninety-five percent on labeled evaluation datasets but exhibits sizable degradation under adversarial adaptation as reviewers vary temporal patterns, textual patterns, and account behavior to evade detection. The [Malbon 2013][research_malbon_2013] Taking Fake Online Consumer Reviews Seriously legal treatment surveys the enforcement-response infrastructure.

### Sockpuppet-Driven Review Deposition

Sockpuppetry as a review-signal manipulation technique refers to the operation of multiple false identities by a single operator with the intent of producing reviews that appear to originate from distinct authentic reviewers. Sockpuppetry differs from coordinated review campaigns in that the sockpuppet operator maintains persistent identities over time rather than producing single-instance operator accounts, and the sockpuppet identities are typically constructed with more elaborate identity infrastructure than the throwaway accounts characteristic of ordinary coordinated campaigns.

The academic detection literature for sockpuppet identity operates through account-linkage analysis, including [Solorio et al. 2014][research_solorio_et_al_2014] Sockpuppet Detection in Wikipedia authoring context, [Zheng 2011][research_zheng_et_al_2011] Detecting Sockpuppets in Deceptive Opinion Spam, and [Kumar et al 2017 An Army of Me][research_kumar_army_2017] on cross-community sockpuppet behavior. The [Tsikerdekis and Zeadally 2014][research_tsikerdekis_zeadally_2014] Multiple Account Identity Deception Detection treatment surveys the field.

The economic structure of sockpuppet operations differs from ordinary coordinated campaigns in the amortization of identity-construction cost. Sockpuppet identity construction requires per-identity investment in profile buildout, activity history, and behavioral patterns, and the marginal identity cost falls with automation. The identity-construction cost permits characterization as

$$
C_{\text{sockpuppet}}(n) = c_{\text{fixed}} + n \cdot c_{\text{marginal}}(n)
\tag{14}
$$

with $c_{\text{fixed}}$ the setup cost of the sockpuppet operation and $c_{\text{marginal}}(n)$ the per-identity marginal cost that typically decreases in $n$ due to tooling automation. Professional sockpuppet operations achieve per-identity marginal costs in the range of

$$
c_{\text{marginal}} \in [0.5, 10] \text{ USD per identity}
\tag{15}
$$

when the identity is used for review deposition rather than for higher-fidelity applications requiring KYC-style identity documentation. Cross-account behavioral-similarity detection operates through the standardized similarity metric

$$
s_{ij}^{\text{behav}} = \frac{\langle \mathbf{f}_i, \mathbf{f}_j\rangle}{\|\mathbf{f}_i\| \cdot \|\mathbf{f}_j\|}
\tag{16}
$$

with $\mathbf{f}\_i$ the behavioral-feature vector for account $i$ combining posting-time distribution, session-length distribution, device-fingerprint hash, and IP-address entropy. Sockpuppet-account pairs exhibit anomalously high $s_{ij}^{\text{behav}}$, and the account-linkage detection identifies suspicious pairs above a chosen threshold. The corresponding posterior for sockpuppet-linkage given the similarity is

$$
\Pr(\text{sockpuppet}_{ij} \mid s_{ij}^{\text{behav}}) = \frac{p(s_{ij} \mid \text{link}) \pi_{\text{link}}}{p(s_{ij} \mid \text{link}) \pi_{\text{link}} + p(s_{ij} \mid \neg \text{link})(1 - \pi_{\text{link}})}
\tag{17}
$$

with $\pi_{\text{link}}$ the base-rate prior of sockpuppet linkage in the population. The persistence-over-time of a sockpuppet identity under active platform enforcement has the form the survival function

$$
S(t) = \Pr(\text{account active at } t) = e^{-\int_0^t h(\tau) d\tau}
\tag{18}
$$

with $h(\tau)$ the hazard rate combining passive-account decay and platform-enforcement removal. Persistent sockpuppet operations sustain $S(t)$ close to unity through operational discipline (avoiding detection triggers) and through operational-scale replacement of removed accounts. The composite multi-feature detection likelihood ratio combining behavioral similarity, activity-pattern similarity, and content similarity takes the form

$$
\Lambda_{ij}^{\text{sockpuppet}} = \prod_{k \in \text{features}} \frac{p(f_k^{ij} \mid \text{link})}{p(f_k^{ij} \mid \neg \text{link})}
\tag{19}
$$

under the standard conditional-independence assumption, with the accumulated log-likelihood serving as the aggregate detection statistic.

### Generative-Model-Produced Review Content

The recent generative-model transition has greatly altered the review-signal manipulation landscape. Large-language-model deployment since the [OpenAI ChatGPT release 2022][ref_openai_chatgpt_2022] and subsequent [GPT-4 release 2023][ref_openai_gpt4_2023] has reduced the marginal cost of producing human-quality review text to near-zero, which shifts the economic first-order condition toward much higher equilibrium review-manipulation volume absent compensating detection improvements. The [Yao et al. 2017][research_yao_et_al_2017] Automated Crowdturfing Attacks and Defenses initial demonstration established that neural-model-generated review text could evade contemporary detectors; the subsequent [Zellers et al. 2019][research_zellers_et_al_2019] Grover paper on generative attacks and defenses established the deeper theoretical framework.

The empirical assessment of LLM-generated review detection includes [Sohail 2024][research_sohail_et_al_2024] on large-language-model generated review detection, [Sadasivan et al. 2023][research_sadasivan_et_al_2023] Can AI-Generated Text be Reliably Detected on the fundamental detection difficulty, and the [Kirchenbauer et al. 2023][research_kirchenbauer_et_al_2023] Watermarking for Large Language Models treatment on the emerging watermark-based detection approach. The composite empirical picture indicates that LLM-generated review text produced by contemporary models can achieve human-classification-error rates below fifty percent under contemporary human-and-classifier detection, which effectively defeats the detection layer under the assumption that the model is prompted to produce text that resembles the target distribution.

The manipulation-cost function under generative-model deployment satisfies approximately

$$
c_{\text{LLM-review}}(m) \approx c_{\text{API}} \cdot m + c_{\text{prompt-eng}}
\tag{20}
$$

with $c_{\text{API}}$ the per-review API cost in the range of $10^{-3}$ to $10^{-2}$ USD per generation, $c_{\text{prompt-eng}}$ the fixed prompt-engineering setup cost, and $m$ the injection volume. The equation makes clear that the convexity exponent $\alpha$ of the classical manipulation-cost function has effectively collapsed to unity, which shifts the manipulation equilibrium considerably toward higher intensity. The [C2PA content provenance standard][ref_c2pa_standard] and the [Meta AI-generated content labeling policy][ref_meta_ai_content_labeling] represent the emerging technical and policy countermeasure infrastructure. The [Coalition for Content Provenance and Authenticity][ref_c2pa_coalition] provides the multi-stakeholder governance forum. The [Sadasivan et al. 2023][research_sadasivan_et_al_2023] impossibility-adjacent result establishes that under sufficient generation-quality the detection accuracy approaches the random-baseline bound

$$
\text{AUC}_{\text{detect}}(q_{\text{gen}}) \to 0.5 \text{ as } q_{\text{gen}} \to q_{\text{human}}
\tag{21}
$$

with $q_{\text{gen}}$ the generative-model quality and $q_{\text{human}}$ the human-authored baseline distribution. The watermarking approach in [Kirchenbauer et al. 2023][research_kirchenbauer_et_al_2023] introduces a bias in the generation distribution that preserves detection accuracy at the cost of small utility loss, admitting characterization as the signed information-content deviation

$$
I_{\text{watermark}}(x) = \log \frac{p_{\text{watermarked}}(x)}{p_{\text{unmarked}}(x)}
\tag{22}
$$

with the watermarked-versus-unmarked likelihood ratio serving as the detection statistic. The complementary perplexity-based detection statistic operates on the intuition that generative-model output exhibits systematically lower perplexity under the reference model than authentic human text,

$$
\text{PPL}(x) = \exp\left(-\frac{1}{|x|} \sum_{i} \log p_{\text{ref}}(x_i \mid x_{<i})\right)
\tag{23}
$$

with the detection thresholding on $\text{PPL}(x) < \tau_{\text{PPL}}$. The paraphrase-attack degradation of watermarking allows characterization via the bit-error-rate under paraphrase transformation

$$
\text{BER}_{\text{para}}(x, x') = \frac{|\{i : w_i(x) \neq w_i(x')\}|}{|w(x)|}
\tag{24}
$$

with $w(x)$ the recovered watermark bits and $x'$ the paraphrased text. The generative-model countermeasure landscape remains unresolved and is treated further in the closing article.

## Follower and Engagement Manipulation Techniques

The engagement-signal manipulation class comprises techniques oriented at the follower counts, engagement metrics (likes, comments, shares, saves, views), and algorithmic-amplification signals that social-media platforms make available. The class is empirically dominant on social platforms and has received appreciable academic detection attention.

### Follower Purchase Economies

Follower purchase refers to the acquisition of follower-count on a social-media account through paid services that create or reassign accounts to follow the buyer. The industry has operated at commercial scale since approximately 2010 and has produced a mature marketplace with per-follower pricing well below one cent for low-quality (bot) followers and up to several cents for medium-quality (aged, semi-active) followers. The [De Micheli and Stroppa 2013][research_demicheli_stroppa_2013] Twitter and the Underground Market documented the initial follower-purchase economy. The [Stringhini et al. 2013][research_stringhini_et_al_2013] Follow the Green Growth and Dynamics in Twitter Follower Markets treatment documented the follower-purchase-service infrastructure. The [Cresci et al. 2015][research_cresci_et_al_2015] Fame for Sale treatment analyzed the population dynamics of purchased followers. The [Bilton 2014][ref_bilton_2014_nyt_followers] New York Times investigation documented the follower-purchase practices of prominent Twitter accounts.

The pricing structure of follower purchase reduces to approximately

$$
p_{\text{follower}} \in [10^{-4}, 10^{-2}] \text{ USD per follower}
\tag{25}
$$

with the lower bound reflecting low-quality bot followers on high-tolerance platforms and the upper bound reflecting medium-quality followers on higher-enforcement platforms. The [NY Attorney General v 2019][ref_ny_ag_devumi_2019] enforcement action addressed a follower-purchase marketplace with documented revenue of approximately fifteen million USD across approximately four years of operation, with per-follower prices in the range of one to two cents. The [FTC v Devumi 2019][ref_ftc_devumi_2019] parallel federal action established the FTC's application of Section 5 to the follower-purchase industry.

The empirical prevalence of purchased followers on major social platforms varies by platform and account category. Contemporary estimates from platform-integrity reporting and academic detection studies place the fraction of purchased or otherwise inauthentic followers on major social platforms in the range

$$
p_{\text{fake-follower}} \in [0.05, 0.30]
\tag{26}
$$

for typical accounts and higher for accounts in categories with high follower-count commercial value (influencer marketing, cryptocurrency promotion, political mobilization). The [Meta Adversarial Threat Report][ref_meta_atr] and the [X Transparency Report][ref_x_transparency_report] provide the platform-industry disclosure.

The detection signatures for purchased followers include the individual bot-account signatures documented in [Cresci 2020][research_cresci_2020] and [Yang et al. 2019][research_yang_et_al_2020], plus follower-graph anomalies including sudden follower-count increases inconsistent with organic growth patterns, follower-account clustering (many followers exhibiting similar creation patterns and behavioral signatures), and geographic-anomaly patterns (followers concentrated in click-farm-associated geographies). The [X Platform Manipulation and Spam Policy][ref_x_platform_manipulation_policy] and the [Instagram Community Guidelines authenticity section][ref_instagram_authenticity_guidelines] establish the platform-side policy framework. The academic detection literature is supported by standing datasets including the [Cresci-2015 Fake Followers Dataset][ref_cresci_2015_dataset] and the [Cresci-2017 Genuine and Spambot Dataset][ref_cresci_2017_dataset] that provide labeled bot and human account samples, and the [Bot Repository Indiana OSoMe][ref_bot_repository] that consolidates the field's standing reference corpora. Follower-to-engagement-ratio anomaly is a standard detection statistic characterizing the mismatch between purchased inauthentic followers and authentic engagement on the buyer's content,

$$
\rho_i^{\text{follow-engage}} = \frac{\bar{e}_i}{F_i}
\tag{27}
$$

with $\bar{e}\_i$ the mean per-post engagement and $F_i$ the follower count. Accounts with purchased followers exhibit anomalously low $\rho^{\text{follow-engage}}$ compared to authentic-follower baselines in the same account category. The organic-follower-growth rate follows a logistic trajectory characterized by

$$
\frac{dF_i}{dt} = r \, F_i \left(1 - \frac{F_i}{K}\right)
\tag{28}
$$

with $r$ the growth-rate parameter and $K$ the account-specific ceiling. Purchase-driven follower-count changes appear as step-function perturbations to the logistic trajectory, admitting detection via change-point analysis. The purchased-follower survival distribution over time exhibits characteristic decay as platform detection removes accounts,

$$
S_{\text{purchased}}(t) = e^{-\lambda_{\text{enforce}} t} \cdot S_{\text{purchased}}(0)
\tag{29}
$$

with $\lambda_{\text{enforce}}$ the platform's per-account removal hazard for detected purchased followers. Contemporary platform enforcement produces half-lives on the order of weeks-to-months for detected purchased followers, which explains the observed post-purchase follower-count decay pattern on major social platforms. The [Cresci et al. 2017][research_cresci_et_al_2017] Paradigm-Shift of Social Spambots treatment documents the technique-evolution history and the corresponding detection-adaptation dynamic.

### Engagement Purchase and Coordinated Engagement Pods

Engagement purchase extends the follower-purchase model to the transactional engagement signals (likes, comments, shares, saves, story views, video views) that platforms use as inputs to ranking algorithms. The marketplace pricing per engagement action is generally in the range

$$
p_{\text{engagement}} \in [10^{-4}, 10^{-2}] \text{ USD per action}
\tag{30}
$$

with per-action pricing structured similarly to follower purchase. Engagement pods are a distinct organizational form in which participants coordinate to exchange authentic engagement on each other's content, which produces authentic account signal but inauthentic content-quality signal from the platform's perspective. The [Weerkamp and de Rijke 2012][research_weerkamp_derijke_2012] Credibility-Inspired Ranking treatment surveys the underlying algorithmic assumptions that pod coordination exploits.

The [Ellis Ott 2018][ref_ellis_ott_2018_pods] The Atlantic investigation documented the Instagram engagement-pod economy and the participation-rate estimates within influencer categories. The [Meta Community Standards on Inauthentic Behavior][ref_meta_cib_policy] establishes the platform-side policy framework for engagement manipulation. The [Ferrara et al. 2016][research_ferrara_et_al_2016] Rise of Social Bots treatment provides the foundational empirical treatment of automated engagement production. The [Papakyriakopoulos et al. 2020][research_papakyriakopoulos_et_al_2020] Political Communication on Social Media treatment addresses the political-engagement-manipulation adjacent literature. The [Nielsen Trust in Advertising Global Report][ref_nielsen_trust_advertising] provides the industry-side survey evidence on consumer trust in different reputation-signal categories that shapes the incentive to manipulate engagement metrics.

The detection signatures for engagement-purchase include the temporal-anomaly patterns (engagement bursts inconsistent with the natural arrival rate for content of the observed quality), the engagement-source-account signatures (bot-account signatures for automated engagement, click-farm-account signatures for human engagement), and the engagement-content-mismatch patterns (engagement content unrelated to the target content). The detection of engagement pods requires different signatures because the participating accounts are authentic and the engagement content is often plausible. Pod detection typically relies on graph-clustering of the engagement pattern and on the account-clustering of frequent pod participants. Pod participation supports characterization via the reciprocity-and-clustering coefficient over the account-engagement graph,

$$
\rho_{\text{pod}}(G) = \frac{|\{(i,j) : (i \to j) \wedge (j \to i)\}|}{|E(G)|} \cdot C(G)
\tag{31}
$$

with the first factor the reciprocity ratio (fraction of engagement edges that are mutual) and $C(G)$ the graph clustering coefficient. Pod-participating account subgraphs exhibit anomalously high $\rho_{\text{pod}}$ compared to the platform-baseline distribution. The [Weller 2019][research_weller_et_al_2019] Understanding Cross-Platform Sharing and Engagement Pod Dynamics treatment provides the initial academic characterization.

### View-Count and Impression Inflation

View-count inflation on video platforms including YouTube and TikTok operates through automated view-generation infrastructure that plays videos through bot-controlled accounts or through click-farm operators. The [YouTube view-count manipulation policy][ref_youtube_view_manipulation_policy] establishes the platform's response framework. The [Zannettou et al. 2018][research_zannettou_et_al_2018] Understanding Web Archiving Services and Their Application treatment surveys the adjacent technical infrastructure.

Impression inflation on display-advertising platforms operates through the ad-fraud infrastructure documented in [Pearce et al. 2014][research_pearce_et_al_2014] Characterizing Large-Scale Click Fraud in ZeroAccess and the [White Ops Methbot report 2016][ref_white_ops_methbot_2016] documenting a large-scale programmatic-advertising fraud operation. The [IAB Ad Fraud Report][ref_iab_ad_fraud_report] and the [MRC Media Rating Council Viewability Standards][ref_mrc_viewability_standards] provide the industry-side reference framework. Impression inflation intersects with reputation manipulation where the inflated impressions produce social-proof signals used in downstream ranking or reputation contexts. View-fraud detection typically operates on the IP-diversity Shannon entropy of the view-source distribution,

$$
H_{\text{view-source}} = -\sum_{a} p_a \log p_a
\tag{32}
$$

with $p_a$ the fraction of views originating from address block $a$. Authentic views produce high $H_{\text{view-source}}$ close to the platform's user-population baseline; view-fraud operations often produce anomalously low $H_{\text{view-source}}$ concentrated on a small set of infrastructure-associated address blocks.

## Search-Ranking Manipulation Techniques

The search-ranking manipulation class comprises techniques oriented at the ranking-position signal on search engines, app stores, and content-discovery platforms. The class differs from the review-and-engagement classes in that the ranking-position signal is emitted by the platform's ranking algorithm rather than by discrete signal-injection events, and manipulation therefore operates through gaming of the algorithm's inputs rather than through direct signal injection.

### Aggressive SEO at the Manipulative End

Search-engine optimization (SEO) covers a broad practitioner spectrum from legitimate technical optimization through aggressive gaming to spam. The manipulative end of the spectrum includes techniques including keyword stuffing (inserting search-target keywords at above-natural density), doorway pages (pages built to rank for queries and redirect to the target destination), cloaking (serving different content to search-engine crawlers than to human visitors), link-farm participation (coordinated cross-linking among sites to inflate PageRank-style ranking signals), private-blog-network operation (operating a network of sites appearing independent but under common control to produce artificial backlinks), and content-scraping and republication with keyword substitution.

The [Google Webmaster Guidelines][ref_google_webmaster_guidelines] establish the platform's SEO policy and delimit the manipulative-technique boundary from the platform's perspective. The [Google Search Central spam policies][ref_google_search_spam_policies] provide the current-version taxonomy. The [Cutts Google Webmaster Central Blog archives][ref_cutts_google_blog] provide the historical record of technique classifications. The [Google 2011 Panda algorithm update][ref_google_panda_2011] and the [Google 2012 Penguin algorithm update][ref_google_penguin_2012] represent major detection-and-enforcement events that significantly reshaped the SEO industry through platform-side algorithmic response to manipulative techniques.

The PageRank algorithm underlying much of the ranking-signal architecture is treated in [Brin and Page 1998][research_page_brin_1998] The Anatomy of a Large-Scale Hypertextual Web Search Engine and the extended [Page Brin Motwani Winograd 1999][research_page_brin_motwani_winograd_1999] treatment. Manipulation targets the PageRank recurrence

$$
\text{PR}(p) = \frac{1 - d}{N} + d \sum_{q \in B_p} \frac{\text{PR}(q)}{L(q)}
\tag{33}
$$

with $\text{PR}(p)$ the PageRank of page $p$, $B_p$ the set of pages linking to $p$, $L(q)$ the outbound link count of $q$, $d$ the damping factor typically set near 0.85, and $N$ the total page count. Manipulation operates through construction of $B_p$ (the inbound-link set) to inflate the summed PageRank contribution, which in turn increases the target page's rank position on subsequent search queries.

The [Gyongyi and Garcia-Molina 2005][research_gyongyi_garciamolina_2005] Web Spam Taxonomy treatment classified the manipulation-technique inventory circa 2005 and remains the reference classification. The [Ntoulas et al. 2006][research_ntoulas_et_al_2006] Detecting Spam Web Pages through Content Analysis introduced the content-based detection framework. The [Castillo et al. 2007][research_castillo_et_al_2007] Know Your Neighbors Web Spam Detection using the Web Topology introduced the graph-topology detection framework. The PageRank-manipulation return per additional inbound link can be characterized as the marginal derivative

$$
\frac{\partial \text{PR}(p)}{\partial |B_p|} \approx d \cdot \overline{\text{PR}/L}_{B_p}
\tag{34}
$$

with $\overline{\text{PR}/L}\_{B_p}$ the average of $\text{PR}(q)/L(q)$ over the inbound-link set. The ranking-position shift produced by a rank increase depends on the density of the local rank-neighborhood and follows approximately

$$
\Delta \text{rank} \approx -\frac{\partial N_{<\rho}}{\partial \rho} \cdot \Delta \rho
\tag{35}
$$

with $N_{<\rho}$ the count of pages with rank score below $\rho$ and $\Delta \rho$ the rank-score change. The click-through gain from a position shift follows the position-decay characterization of the framing article. The [TrustRank propagation algorithm][ref_gyongyi_2004_trustrank_paper] extension proposed in the anti-spam literature propagates trust from a seed set of hand-labeled trusted pages via the recurrence

$$
t(p) = (1 - d) \, \mathbb{1}[p \in S_{\text{seed}}] + d \sum_{q \in B_p} \frac{t(q)}{L(q)}
\tag{36}
$$

with $S_{\text{seed}}$ the trusted-seed set and the trust score $t(p)$ decaying with graph distance from the seed. Spam-oriented sites typically receive low $t(p)$ due to weak connectivity to the trusted seed, admitting detection via the trust-rank threshold. Cloaking detection operates on the differential between the content served to the search-engine crawler and the content served to human visitors,

$$
\Delta_{\text{cloak}}(p) = d_{\text{content}}(C_{\text{crawler}}(p), C_{\text{human}}(p))
\tag{37}
$$

with $d_{\text{content}}$ a content-distance metric and $C_{\cdot}(p)$ the content served to the respective user-agent class.

### App-Store Optimization Gaming

App-store optimization (ASO) gaming targets the ranking algorithms on the [Apple App Store][ref_apple_app_store_review_guidelines] and [Google Play Store][ref_google_play_developer_policy]. Techniques include keyword manipulation in app metadata, download-count inflation through automated or click-farm-driven downloads, and review manipulation through the mechanisms treated in the review-manipulation class above. Download-velocity manipulation admits detection via the standardized deviation

$$
z_{\text{download}}(t) = \frac{D(t) - \bar{D}_{\text{category}}(t)}{\sigma_{D,\text{category}}(t)}
\tag{38}
$$

with $D(t)$ the app's download rate at time $t$ and $\bar{D}\_{\text{category}}$, $\sigma_{D,\text{category}}$ the category-baseline moments. Manipulation-driven download bursts produce $z_{\text{download}}$ above the anomaly threshold typically set at $z > 3$. The [Ali 2017][research_ali_et_al_2017] Same Same but Different Search Advertising and Users' Attention treatment surveys the ranking-algorithm-adjacent research. The [D'Ambrosio 2018][research_dambrosio_et_al_2018] treatment analyzes the app-review manipulation ecosystem.

## Coordinated Inauthentic Behavior at Network Scale

Coordinated inauthentic behavior (CIB) refers to the class of manipulation operations that operate through networks of accounts under coordinated control, with the coordination oriented at producing signal at scales inaccessible to individual or small-team operators. The term traces to the [Meta Coordinated Inauthentic Behavior policy][ref_meta_cib_policy] framework and has been adopted broadly across the platform-integrity industry.

### Sockpuppet Networks and Sybil Attacks

Sybil attacks refer to the technical variant of sockpuppetry in which the false identities are created and maintained at scale through automated infrastructure. The term traces to [Douceur 2002][research_douceur_2002] The Sybil Attack in the peer-to-peer systems literature. The technique has migrated to social-media reputation systems where it operates through automated account creation, automated identity buildout, and automated activity generation.

The Sybil-detection literature includes [Yu et al. 2006][research_yu_et_al_2006] SybilGuard Defending Against Sybil Attacks via Social Networks, [Yu et al. 2008][research_yu_et_al_2008] SybilLimit A Near-Optimal Social Network Defense against Sybil Attacks, [Danezis and Mittal 2009][research_danezis_mittal_2009] SybilInfer Detecting Sybil Nodes using Social Networks, [Cao et al. 2012][research_cao_et_al_2012] Aiding the Detection of Fake Accounts in Large Scale Social Networks, and [Alvisi et al. 2013][research_alvisi_et_al_2013] SoK The Evolution of Sybil Defense via Social Networks. The [Yu et al. 2006][research_yu_et_al_2006] SybilGuard framework establishes the bound on Sybil-region size under the random-walk-mixing-time assumption

$$
|S_{\text{Sybil}}| \leq O(\sqrt{n \log n})
\tag{39}
$$

with $n$ the honest-region size, subject to the assumption that Sybil-honest graph attack-edges are bounded and that the honest region is fast-mixing. The Sybil-detection statistic based on graph conductance identifies the Sybil-region cut as the minimum-conductance partition

$$
\Phi(S) = \frac{|E(S, \bar{S})|}{\min(|E(S)|, |E(\bar{S})|)}
\tag{40}
$$

with the Sybil region admitting characterization as the subset $S$ that achieves anomalously low $\Phi(S)$ relative to the null-model conductance distribution. The detection accuracy under the social-graph-based approaches depends on the assumption that Sybil accounts have limited authentic-account connections; the assumption has weakened as Sybil operators have invested in constructing plausible connection graphs.

The economic characterization of a Sybil operation includes the identity-construction cost treated above plus the ongoing maintenance cost for activity generation. The aggregate Sybil-network operation cost permits characterization as

$$
C_{\text{Sybil}}(N, T) = c_{\text{setup}} + N \cdot (c_{\text{ident}} + T \cdot c_{\text{activity}})
\tag{41}
$$

with $N$ the network size, $T$ the operational time horizon, $c_{\text{setup}}$ the operation-level fixed cost, $c_{\text{ident}}$ the per-identity construction cost, and $c_{\text{activity}}$ the per-identity per-unit-time activity cost. Professional Sybil operations at contemporary marketplace scale achieve unit costs supporting network sizes in the range

$$
N \in [10^3, 10^6] \text{ Sybil accounts per operation}
\tag{42}
$$

with the upper bound reached by state-sponsored or well-funded commercial operators.

### Cross-Platform Amplification Rings

Cross-platform amplification rings operate through coordinated content-sharing and engagement across multiple platforms with the intent of producing reinforcing amplification signal across the platform ecosystem. The technique differs from single-platform CIB in that detection and enforcement infrastructure is generally platform-specific, and cross-platform coordination therefore escapes single-platform detection even when each individual platform's activity would be detectable by that platform's classifiers.

The [Bradshaw and Howard 2019][research_bradshaw_howard_2019] Global Disinformation Order treatment surveys the cross-platform information-operation landscape. The [DiResta et al. 2019][research_diresta_et_al_2019] Tactics and Tropes of the Internet Research Agency treatment documents the cross-platform operations of the Russian Internet Research Agency across Facebook, Twitter, Instagram, YouTube, and other platforms. The [Zannettou et al. 2019][research_zannettou_et_al_2019] Disinformation Warfare Understanding State-Sponsored Trolls treatment analyzes the cross-platform information-operation graph. The [Starbird 2019][research_starbird_2019] Disinformation's Spread Bots Trolls and All of Us treatment provides the theoretical framing.

Cross-platform amplification produces content-appearance-correlation across platforms that allows detection through the cross-platform Pearson correlation of content appearance timestamps

$$
r_{\text{cross}}(P_1, P_2) = \frac{\sum_c (t_c^{P_1} - \bar{t}^{P_1})(t_c^{P_2} - \bar{t}^{P_2})}{\sqrt{\sum_c (t_c^{P_1} - \bar{t}^{P_1})^2 \sum_c (t_c^{P_2} - \bar{t}^{P_2})^2}}
\tag{43}
$$

with $t_c^{P}$ the timestamp of content $c$ appearing on platform $P$. Coordinated cross-platform amplification produces $r_{\text{cross}}$ close to unity for tightly coordinated operations. The amplification-cascade decay follows the reach recurrence

$$
R_{\text{cascade}}(t+1) = R_{\text{cascade}}(t) \cdot \eta \cdot (1 - \frac{R_{\text{cascade}}(t)}{\bar{R}})
\tag{44}
$$

with $\eta$ the per-step amplification gain and $\bar{R}$ the reach ceiling set by the audience-network size. Cross-platform detection requires cross-platform data-sharing infrastructure that has developed slowly due to platform competition and privacy considerations. The [Global Internet Forum to Counter Terrorism (GIFCT)][ref_gifct] and the [Meta Threat Report cross-platform sections][ref_meta_atr] represent the emerging cross-platform coordination infrastructure. The academic [Cross-Platform Sharing Dataset][ref_cross_platform_sharing_dataset] provides one standing empirical resource.

### Click Farms and Human-Operator Networks

Click farms refer to the physical or virtual facilities in which human operators produce engagement, reviews, or other reputation signals at commercial scale. The industry has been documented most extensively in the [Cushing 2013][ref_cushing_2013_click_farm] Wired investigation of Bangladesh click-farm operations and in subsequent journalistic and academic treatments. The [Farooqi 2017][research_farooqi_et_al_2017] Characterizing Key Stakeholders in an Online Black Market analyzes the click-farm labor market. The [Motoyama 2011][research_motoyama_et_al_2011] Dirty Jobs The Role of Freelance Labor in Web Service Abuse treatment establishes the labor-market characterization.

Click farm operations occupy an intermediate detection difficulty because the individual operator actions are authentic human actions from an identity and behavioral perspective; the manipulation signature emerges at the operator-network scale in the patterns of task assignment and coordination. The [Wang 2012][research_wang_et_al_2012] Serf and Turf Crowdturfing for Fun and Profit treatment provides the academic characterization of the crowdturfing marketplace.

The throughput characterization of a click farm supports estimation as

$$
\Lambda_{\text{click-farm}} = N_{\text{operator}} \cdot h \cdot r
\tag{45}
$$

with $N_{\text{operator}}$ the operator count, $h$ the hours per operator per day, and $r$ the actions per operator-hour. Contemporary click farms achieve throughput in the range

$$
\Lambda \in [10^4, 10^6] \text{ actions per day per operation}
\tag{46}
$$

with the upper bound reached by large industrial operations. The task-queuing model for click-farm operations follows the standard M/M/c queue characterization

$$
L_q = \frac{(N_{\text{op}} \rho)^{N_{\text{op}}} \rho}{N_{\text{op}}! (1 - \rho)^2} P_0
\tag{47}
$$

with $\rho$ the operator utilization, $N_{\text{op}}$ the operator count, and $P_0$ the probability of zero queue occupancy, and provides the throughput-versus-latency tradeoff characterization for the operation-management perspective. Geographic-anomaly detection for click-farm-originating activity operates on the geographic entropy of the account-origin distribution restricted to click-farm-associated regions,

$$
H_{\text{geo}}^{\text{restrict}} = -\sum_{g \in G_{\text{cf}}} p_g \log p_g
\tag{48}
$$

with $G_{\text{cf}}$ the set of click-farm-associated geographic regions and $p_g$ the fraction of activity originating from region $g$. Click-farm-heavy operations exhibit anomalously low $H_{\text{geo}}^{\text{restrict}}$ concentrated on small operator-hub subsets of $G_{\text{cf}}$.

### State-Sponsored Operations Extending to Commercial Reputation

State-sponsored information operations documented in [DiResta et al. 2019][research_diresta_et_al_2019], [Rid 2020][book_rid_2020] Active Measures, and the [Mueller Report 2019][ref_mueller_report_2019] Volume One primarily target political outcomes but produce spillover effects on commercial reputation through the operations' amplification of commercial narratives, disparagement of commercial actors, and creation of adversarial-content ecosystems that individual commercial actors then engage with as a background environment. State-attribution inference from technical fingerprints (infrastructure reuse, code fingerprints, operational-security patterns, language-and-timezone signatures) has the form the Bayesian posterior

$$
\Pr(\text{state} = s \mid \mathbf{F}) = \frac{\Pr(\mathbf{F} \mid s) \pi(s)}{\sum_{s'} \Pr(\mathbf{F} \mid s') \pi(s')}
\tag{49}
$$

with $\mathbf{F}$ the observed fingerprint vector and $\pi(s)$ the prior over candidate state actors. The [Bradshaw et al. 2021][research_bradshaw_bailey_howard_2021] Industrialized Disinformation cross-national survey characterizes the scale of state-sponsored operations. The [Bright 2020][research_bright_et_al_2020] Coordinated Behavior on Social Media treatment surveys the coordinated-behavior detection literature applicable across political and commercial contexts.

## Astroturfing and Grassroots Manufacturing

Astroturfing refers to the manipulation practice of manufacturing apparent grassroots support for a person, product, position, or narrative. The term traces to Senator Lloyd Bentsen's 1985 characterization of manufactured constituent mail as artificial grass in the [Bentsen 1985 Congressional Record][ref_bentsen_congressional_record_1985]. Astroturfing overlaps with review manipulation and coordinated inauthentic behavior but is analytically distinct in that its objective is the manufacture of the appearance of authentic public support rather than the direct manipulation of a discrete reputation score.

### Corporate Astroturfing

Corporate astroturfing operations have been documented across the tobacco, oil, pharmaceutical, and food industries. The [Oreskes and Conway 2010][book_oreskes_conway_2010] Merchants of Doubt treatment documents the coordinated denial campaigns on tobacco, ozone depletion, acid rain, and climate change organized by tobacco-industry-adjacent operators and subsequently adopted by the oil industry. The [McGarity and Wagner 2008][book_mcgarity_wagner_2008] Bending Science documents the corporate manufacture of doubt through funded academic work and coordinated advocacy. The [Michaels 2008][book_michaels_2008] Doubt Is Their Product documents the corporate manufactured-doubt playbook. The [Miller 2004][ref_miller_2004_walmart] documentation of the Working Families for Wal-Mart astroturf organization illustrates the corporate-astroturf technique. The [Walker 2014][book_walker_2014] Grassroots for Hire treatment consolidates the contemporary industry analysis.

The corporate-astroturfing detection signatures include coordination patterns across ostensibly independent voices, funding-trail patterns linking apparent grassroots organizations to corporate funding, message-timing patterns showing coordinated release across the astroturfed voice population, and text-similarity patterns showing shared templates. The astroturf-coordination z-score for release-timing anomaly follows

$$
z_{\text{coord}} = \frac{\text{(observed simultaneous releases)} - \mu_{\text{null}}}{\sigma_{\text{null}}}
\tag{50}
$$

with $\mu_{\text{null}}$ and $\sigma_{\text{null}}$ the null-hypothesis distribution parameters under an independent-release model. Astroturf operations typically exhibit $z_{\text{coord}} > 5$ during active-campaign windows. The [Cho et al. 2011][research_cho_et_al_2011] Astroturfing detection framework introduced the academic detection methodology. The [Ratkiewicz et al. 2011][research_ratkiewicz_et_al_2011] Detecting and Tracking Political Abuse in Social Media (Truthy) introduced the social-media-specific detection framework.

### Political Astroturfing

Political astroturfing operates through similar techniques as corporate astroturfing but with objectives oriented at electoral, policy, or narrative outcomes. The [King et al. 2017][research_king_pan_roberts_2017] How the Chinese Government Fabricates Social Media Posts documents the Chinese "50 Cent Army" state-directed social-media astroturfing at scale, estimating an aggregate volume of approximately

$$
V_{\text{50-cent}} \approx 4.4 \times 10^8 \text{ posts per year}
\tag{51}
$$

concentrated in strategic distraction rather than in engaged argument. The coordinated-posting-timing signature is described by the concentration statistic

$$
\text{Conc}(\Delta t) = \frac{|\{p : t_p \in [\Delta t]\}|}{|\text{posts}|}
\tag{52}
$$

with $\Delta t$ a short time window aligned with the operational schedule of the astroturf operators; coordinated operations exhibit anomalously high $\text{Conc}$ within operational time windows aligned with the operators' work schedules. The [Woolley and Howard 2018][book_woolley_howard_2018] Computational Propaganda edited volume surveys the cross-national political-astroturfing landscape. The [Aral 2020][book_aral_2020] Hype Machine consolidates the empirical evidence on political manipulation effects.

### Front-Organization Structures

Astroturfing at organizational scale often operates through purpose-built front organizations that appear to be independent civil-society, grassroots, or expert organizations but are in fact organized and funded by principal-party interests. The [Levick and Slavo 2015][ref_levick_slavo_2015] documentation of front-organization structures illustrates the pattern. The [Fang 2013][ref_fang_2013_koch] investigation of the Koch-network affiliated organizations documents the funding-and-coordination structure. The [Souls of Distortion 2016 catalog of front organizations][ref_source_watch_front] operated by the Center for Media and Democracy provides one standing reference resource.

## Credential and Identity Fabrication

Credential and identity fabrication operates through the direct construction of false professional credentials, educational credentials, work-history claims, or identity attributes with the intent of augmenting the actor's reputation through the credentials' implicit endorsement.

### Verified-Badge Acquisition

Platform verified-badge programs including the [Twitter Verification legacy program][ref_twitter_verification_legacy], the [Instagram Verified badge][ref_instagram_verified], the [LinkedIn ID Verification][ref_linkedin_verification], and the [YouTube channel verification][ref_youtube_verification] provide platform-issued reputation signals intended to authenticate account identity or notability. The badges have been targeted by manipulation operations that acquire badges through documentation fabrication, insider access, or purchase from insider brokers. The [Musk-era Twitter Blue paid verification][ref_x_blue] represents the shift from earned to purchased verification on that platform, with the resulting signal-informativeness decline documented in [Marino 2023][research_marino_et_al_2023] Effects of Removing Twitter Blue Verification. The signal-informativeness delta produced by the earned-to-paid transition is described by the mutual-information change

$$
\Delta I_{\text{verify}} = I(\text{authentic} ; \text{badge}_{\text{earned}}) - I(\text{authentic} ; \text{badge}_{\text{paid}})
\tag{53}
$$

with the first term the mutual information between the authenticity-attribute and the earned-verification badge and the second term the analogous quantity for the paid-verification badge. Empirical estimates from the [Marino 2023][research_marino_et_al_2023] treatment indicate $\Delta I_{\text{verify}} > 0$ substantially, reflecting the informativeness collapse under the transition.

### Professional-Credential Fabrication

Professional-credential fabrication operates through claims of academic degrees, professional certifications, employment history, or awards that are not held by the claimant. The academic-degree-fraud literature includes [Ezell and Bear 2005][book_ezell_bear_2005] Degree Mills the surveying treatment of degree-fraud industry. Credential-fraud detection accuracy under standard verification protocols depends on the accessibility and quality of the issuing-body verification infrastructure and admits characterization via the confusion-matrix accuracy

$$
\text{Acc}_{\text{cred}} = \frac{|\text{correctly classified}|}{|\text{all}|} = \Pr(\text{verify} \mid \text{authentic}) \cdot \pi_{\text{authentic}} + \Pr(\neg \text{verify} \mid \text{fabricated}) \cdot (1 - \pi_{\text{authentic}})
\tag{54}
$$

with $\pi_{\text{authentic}}$ the base-rate authentic-credential prevalence. The professional-certification-fraud domain is estimated by through the [PMP Institute fraud detection][ref_pmi_fraud] and adjacent professional-body detection infrastructure. The [Anti-Cheating and Certification Fraud Coalition][ref_accfc] provides one industry reference resource.

### Identity Impersonation

Identity impersonation operates through the creation of accounts and content attributed to a real person other than the operator. The technique intersects with defamation law where the impersonation content damages the target's reputation and with fraud law where the impersonation is used to induce transactions. The [FTC 2024 Impersonation Rule][ref_ftc_impersonation_rule_2024] establishes the federal regulatory framework for the government-and-business-impersonation subset. The [MegaUpload v Universal 2011 case][ref_megaupload_universal_2011] and the [Facebook v Power Ventures 2016][ref_facebook_v_power_ventures_2016] address adjacent legal questions. Cryptographic identity attestation through the [FIDO Alliance authentication standards][ref_fido_alliance] and the [W3C Web Authentication (WebAuthn) standard][ref_w3c_webauthn] provides emerging counter-infrastructure that binds account-level actions to hardware-attested identity keys, which constrains the sockpuppet and impersonation technique classes to accounts for which the attestation infrastructure has been circumvented.

## Reputation Laundering Techniques

Reputation laundering refers to the practice of transferring reputation from a source with credibility to a target that lacks credibility, whether through endorsement, acquisition, or association.

### Endorsement Acquisition

Endorsement acquisition operates through the payment for or exchange with credibility-carrying endorsers whose reputation transfers to the target through the endorsement. The endorsement-value-transfer coefficient takes the form the fraction of the endorser's reputation that transfers to the endorsed target,

$$
V_{\text{transfer}}(E \to T) = \kappa_{E,T} \cdot R_E
\tag{55}
$$

with $\kappa_{E,T}$ the transfer-coefficient dependent on the endorsement channel, the perceived material connection, and the target-endorser category match, and $R_E$ the endorser's reputation stock. The transfer coefficient is bounded by unity and typically ranges

$$
\kappa \in [0.01, 0.30]
\tag{56}
$$

with the lower bound reflecting distant category match and the upper bound reflecting close category match with high-trust endorser. The disclosure-effect coefficient measures the change in the transfer coefficient produced by mandatory material-connection disclosure,

$$
\Delta \kappa_{\text{disclose}} = \kappa_{\text{undisclosed}} - \kappa_{\text{disclosed}}
\tag{57}
$$

with the FTC endorsement-guides policy analysis in [Boerman 2018][research_boerman_et_al_2018] and related work estimating $\Delta \kappa_{\text{disclose}}$ in the range of ten to forty percent for consumer-focused endorsements, which sets the informational-value of disclosure enforcement. The technique class has been the primary subject of the [FTC Endorsement Guides 16 CFR Part 255][ref_ftc_endorsement_guides_16_cfr_255] and the [FTC Endorsement Guides FAQ][ref_ftc_endorsement_faq] material-connection-disclosure framework. The enforcement history includes the [FTC 2011 warning letters to bloggers][ref_ftc_2011_blogger_warnings], the [FTC 2015 Machinima settlement][ref_ftc_machinima_2015] on YouTube gaming influencer disclosure, the [FTC 2016 Warner Brothers settlement][ref_ftc_warner_2016] on undisclosed sponsored coverage of Shadow of Mordor, the [FTC 2017 Individual Influencer Warning Letters][ref_ftc_influencer_letters_2017], and the [SEC v Kardashian 2022][ref_sec_kardashian_2022] action addressing undisclosed cryptocurrency promotion.

### Cross-Platform Reputation Transfer

Cross-platform reputation transfer operates through cross-linking that leverages reputation earned on one platform to establish credibility on another platform. The technique class includes legitimate uses (transferring an academic reputation to a general-audience blog) and manipulative uses (using purchased followers or fabricated credentials on one platform to establish apparent credibility on another). The cross-platform-transfer decay follows the exponential form

$$
R_T^{P_2}(t) = R_T^{P_1}(0) \cdot \kappa_{P_1 \to P_2} \cdot e^{-\gamma t}
\tag{58}
$$

with $\kappa_{P_1 \to P_2}$ the platform-pair-specific transfer coefficient and $\gamma$ the reputation-decay rate on the target platform. The [Chen 2019][research_chen_et_al_2019] Cross-Platform Identity Linkage treatment surveys the underlying identity-linkage detection literature relevant to manipulation-monitoring.

### Acquisition-Based Laundering

Acquisition-based laundering operates through the purchase of established websites, social-media accounts, or businesses to inherit the target's accumulated reputation for redirection to the acquirer's purposes. The technique class has been documented in the [Kanich 2011][research_kanich_et_al_2011] No Plan Survives Contact Experience with Cybercrime Measurement treatment of the domain-market abuse ecosystem, and in the [Krebs 2013][ref_krebs_2013_expired_domains] documentation of the expired-domain reputation-transfer ecosystem. The domain-age reputation value function permits characterization as an increasing function of age

$$
V_{\text{domain}}(a) = V_0 \, \bigl(1 - e^{-\alpha a}\bigr)
\tag{59}
$$

with $a$ the domain age since first content publication and $\alpha$ the reputation-saturation rate. The value asymptotes to $V_0$ for domains of considerable age, which sets the acquisition-target-selection heuristic for the laundering-oriented buyer population. The [Miramirkhani et al. 2017][research_miramirkhani_et_al_2016] Dial One For Scam Analyzing the Technical Support Scam Ecosystem treatment analyzes the adjacent scam-ecosystem infrastructure.

## Six-Axis Framework Application

The self-promotion technique inventory allows systematic characterization along the six-axis framework introduced in the framing article. The characterization identifies each technique's position on each axis and enables cross-technique comparison.

The signal axis characterization varies markedly across techniques. Individual review fabrication produces low-volume single-channel signal on the review channel. Coordinated review campaigns produce medium-volume single-channel signal on the review channel with coordination in the injection pattern. Sockpuppet networks produce medium-to-high-volume single-channel signal with persistent identity infrastructure. Follower purchase produces high-volume single-channel signal on the follower channel. Engagement purchase produces high-volume single-channel signal on the engagement channel. Click farm operations produce high-volume multi-channel signal with human-operator fidelity. Generative-model-produced content produces very-high-volume potentially-multi-channel signal at collapsed cost. Cross-platform amplification produces medium-volume multi-channel signal with cross-channel coordination. Astroturfing produces medium-volume multi-channel signal with narrative coordination across the operator population. The signal-axis position of each technique class is summarized by the tuple

$$
\mathbf{a}_k^{\text{signal}} = (v_k, C_k, f_k, X_k)
\tag{60}
$$

with $v_k$ the signal volume rate, $C_k$ the channel-count dimension, $f_k$ the injection fidelity, and $X_k$ the cross-channel amplification factor.

The objective axis characterization for self-promotion techniques uniformly optimizes for the actor's own reputation-signal outcome, but the optimization target varies. Rating-manipulation techniques target rating uplift. Follower-purchase techniques target follower-count uplift. Engagement-purchase techniques target engagement-metric uplift feeding into ranking-algorithm inputs. Search-manipulation techniques target ranking-position uplift. Credential-fabrication techniques target credential-based reputation transfer. Astroturfing techniques target apparent-popular-support production. The objective-axis position of each technique class reduces to the utility functional

$$
U_k(\mathbf{x}) = \lambda_k^{\text{rating}} g_{\text{rating}}(\mathbf{x}) + \lambda_k^{\text{follow}} g_{\text{follow}}(\mathbf{x}) + \lambda_k^{\text{engage}} g_{\text{engage}}(\mathbf{x}) + \lambda_k^{\text{rank}} g_{\text{rank}}(\mathbf{x}) + \lambda_k^{\text{cred}} g_{\text{cred}}(\mathbf{x}) + \lambda_k^{\text{support}} g_{\text{support}}(\mathbf{x})
\tag{61}
$$

with the $\lambda_k^{\cdot}$ weights specifying the technique class's objective composition.

The structure axis characterization varies from individual operators (individual review fabrication) through small-firm operators (business owner boosting own listings) through hired reputation-management firms through commercial marketplaces (fake-review platforms, follower-purchase services) through coordinated inauthentic behavior networks through state-sponsored operations. The structure axis is summarized by hierarchy depth $D_k$ and branching factor $B_k$,

$$
\mathbf{a}_k^{\text{struct}} = (D_k, B_k, N_k)
\tag{62}
$$

with $N_k$ the operator population size. Individual operations exhibit $D_k = 1$, $B_k = 1$, $N_k = 1$. Commercial marketplace operations exhibit $D_k \approx 3$-$4$, $B_k \approx 10$-$100$, $N_k \approx 10^3$-$10^5$. State-sponsored operations exhibit $D_k \approx 5$-$7$, $B_k \approx 10$-$30$, $N_k \approx 10^3$-$10^6$.

The model axis characterization identifies the technical and rhetorical content each technique class carries. The technical model includes the fabrication method, the account-provenance method, the coordination method, and the evasion method. The rhetorical model includes the persuasion framing, the credibility framing, and the narrative framing. The model-axis position of each technique takes the form the position vector $\mathbf{c}\_k$ over the technique-space basis introduced in the framing article, with pairwise technique distance $d_{\text{model}}(j, k) = \sum_m \lvert c_m^j - c_m^k \rvert$.

The interaction axis characterization for self-promotion techniques uniformly involves the actor's relationship with platforms (ranging from compliant to adversarial), with targets (typically target-unaware self-promotion), with competitors (typically independent operation, sometimes industry-wide reputation collusion), with audiences (typically audience-unaware manipulation, sometimes audience-complicit as in engagement pods), and with enforcement authorities (below-detection-threshold operation through detection-and-remediation cycle through legal-proceedings engagement). The interaction axis is operationalized as the weighted signed graph over actors, targets, platforms, and enforcers.

The adaptation axis characterization varies appreciably across techniques by adaptation velocity. Individual manipulation exhibits slow adaptation. Small-firm operations exhibit moderate adaptation. Commercial marketplaces exhibit rapid adaptation to platform changes with dedicated engineering resources. State-sponsored operations exhibit rapid adaptation with dedicated intelligence-service infrastructure. The adaptation axis operationalizes as the technique-migration time constant $\tau_k$ under the relaxation dynamics

$$
\frac{dS_k}{dt} = -\frac{1}{\tau_k}(S_k - S_k^{*}(t)) + \xi_k(t)
\tag{63}
$$

with $S_k$ the technique-and-infrastructure state and $S_k^{\*}(t)$ the environment-dependent optimal response. Commercial and state-sponsored operations achieve $\tau_k$ in the range of days to weeks; individual operations exhibit $\tau_k$ in the range of months to years.

The cross-axis coupling matrix to the self-promotion technique inventory identifies the principal empirical dependencies among axis values. Empirically salient couplings include the structure-signal coupling $\partial a^{\text{signal}} / \partial a^{\text{struct}} > 0$ (larger organizational structure supports higher signal volume), the model-adaptation coupling $\partial a^{\text{adapt}} / \partial a^{\text{model}} > 0$ (more sophisticated technical model supports faster adaptation), and the interaction-signal coupling $\partial a^{\text{signal}} / \partial a^{\text{interact}} \lessgtr 0$ (compliant platform relationship constrains signal volume, adversarial relationship enables higher signal at higher detection risk). The self-promotion cross-axis coupling matrix

$$
C^{\text{self-promo}} = \left[\frac{\partial a^b}{\partial a^a}\right]_{a, b \in \text{axes}}
\tag{64}
$$

encodes these dependencies and supports estimation from the cross-technique empirical variation in axis positions.

## Detection Methodology Summary

The detection methodology landscape for self-promotion manipulation is treated in depth in the closing article of the miniseries. The framing article surveys the principal detection-methodology classes as they apply to the self-promotion technique inventory.

Statistical anomaly detection targets deviations from expected distributional patterns of reviews, followers, engagement, or ranking signals. The methodology includes temporal-anomaly detection (burst detection, arrival-rate anomaly), distributional-anomaly detection (rating-distribution shape anomaly), and demographic-anomaly detection (geographic or account-age distributional anomaly). The generic anomaly-score statistic under the null-model $H_0$ takes the standardized form

$$
z_{\text{anomaly}} = \frac{T(\mathbf{x}) - E_{H_0}[T]}{\sqrt{\text{Var}_{H_0}[T]}}
\tag{65}
$$

with $T(\mathbf{x})$ the test statistic evaluated on the observed data $\mathbf{x}$. Detection triggers when $\lvert z_{\text{anomaly}} \rvert$ exceeds a chosen threshold, typically calibrated to a desired false-positive rate. The [Kumar 2017][research_kumar_et_al_2017] rating-distribution treatment and the [Xie et al. 2012][research_xie_et_al_2012] temporal-pattern treatment establish the reference methodology.

Network anomaly detection targets structural anomalies in the reviewer-product-business graph, the follower-followee graph, the account-content-account interaction graph, or the cross-platform sharing graph. The methodology includes community-detection anomaly (unusually dense subgraphs indicating coordination), graph-embedding anomaly (nodes with anomalous embedding-space positions), and label-propagation anomaly (nodes whose classifier labels propagate inconsistently). The [Rayana and Akoglu 2015][research_rayana_akoglu_2015] and [Wang et al. 2011][research_wang_et_al_2011] treatments establish the reference methodology.

Machine-learning classifier approaches train on labeled instances of manipulation and non-manipulation and apply the trained classifiers to unlabeled instances. The methodology includes stylometric text classifiers, behavior-pattern classifiers, and multi-modal ensemble classifiers. Ensemble classifier accuracy under standard averaging is captured by

$$
P_{\text{ensemble}}(\text{correct}) \geq 1 - \sum_{k=\lceil M/2 \rceil}^{M} \binom{M}{k} p^k (1 - p)^{M - k}
\tag{66}
$$

with $p$ the individual classifier error rate and $M$ the ensemble size, under the assumption of classifier independence. The classifier-based approach has been the dominant academic detection methodology since the [Ott et al. 2011][research_ott_et_al_2011] treatment, with the classifier-adaptation dynamic under adversarial manipulation-technique evolution treated in [Cresci 2020][research_cresci_2020] and subsequent work.

Human review supplements the automated detection methodology for high-stakes classification decisions and for training-corpus construction. The [Roberts 2019][book_roberts_2019] Behind the Screen treatment documents the labor conditions of platform content moderation. The [Klonick 2018][research_klonick_2018] New Governors treatment addresses the governance of the human-review layer.

Cross-platform detection collaboration operates through information-sharing mechanisms including the [Global Internet Forum to Counter Terrorism (GIFCT)][ref_gifct] hash-sharing infrastructure and adjacent industry coordination bodies. Cross-platform collaboration for commercial-manipulation detection is less developed than for terrorism and CSAM detection.

## Platform Countermeasure Summary

Platform countermeasures for self-promotion manipulation are treated in depth in the closing article of the miniseries. The framing article surveys the principal countermeasure classes.

Identity verification countermeasures constrain the account-provenance channel and include phone-number verification, government-ID verification, biometric verification, and the emerging cryptographic-identity attestation frameworks including the [W3C Verifiable Credentials standard][ref_w3c_verifiable_credentials], the [Decentralized Identifiers (DID) standard][ref_w3c_did], and the [C2PA content provenance standard][ref_c2pa_standard]. The identity-verification-cost function increases with verification stringency and creates the tradeoff between manipulation deterrence and user-friction. The composite friction-cost function reduces to

$$
C_{\text{verify}}(v) = c_{\text{user-time}}(v) + c_{\text{privacy-loss}}(v) + c_{\text{platform-processing}}(v)
\tag{67}
$$

with $v$ the verification-stringency parameter and each cost component increasing in $v$. The optimal verification stringency balances the friction cost against the manipulation-deterrence gain, and the platform's first-order condition on $v$ characterizes the equilibrium.

Behavioral analysis countermeasures target the account-behavior patterns that distinguish authentic from inauthentic accounts. The methodology includes rate-limiting to constrain the per-account activity volume, device-fingerprint tracking to detect multi-account operations from single devices, IP-range monitoring, and interaction-pattern analysis. The rate-limit countermeasure imposes the per-account throughput bound

$$
\lambda_i^{\text{observed}} \leq \lambda_{\text{max}}, \quad \forall i
\tag{68}
$$

and shifts the manipulation-cost function such that per-account output scales linearly in $N_{\text{account}}$, which increases the account-provenance cost per unit signal output. The effective deterrence condition against a rational manipulator reduces to the framing-article condition on expected penalty exceeding expected reputation gain, and platform enforcement typically targets the account-provenance channel rather than the signal-output channel to raise the manipulation-cost function's convexity.

Content authentication countermeasures target the content-provenance channel through cryptographic content-signing, watermarking, and provenance-attestation. The [C2PA content provenance standard][ref_c2pa_standard], the [Kirchenbauer et al. 2023][research_kirchenbauer_et_al_2023] watermarking framework, and the emerging [Content Authenticity Initiative][ref_content_authenticity_initiative] infrastructure represent the field's current state. The content-provenance verification admits characterization as the signature-validity check

$$
V(\text{content}, \sigma) = \mathbb{1}[\text{Verify}(\text{pk}, \text{content}, \sigma)]
\tag{69}
$$

with $\sigma$ the cryptographic signature attached to the content and pk the public key of the claimed origin. Provenance-verified content carries higher signal informativeness than unverified content under the assumption that signature-generation infrastructure is limited to authentic-content producers.

Legal enforcement countermeasures operate through the regulatory and case-law framework surveyed in the framing article at the [Regulatory and Legal Framework section][related_post_a277_theory]. The [FTC 2024 Final Rule on Fake Reviews and Testimonials][ref_ftc_final_rule_2024] represents the most significant recent federal rulemaking; the [EU Digital Services Act Regulation 2022/2065][ref_eu_dsa_2022] represents the most substantial recent international regulatory framework; and the [Amazon v Fake Review 2022][ref_amazon_v_fake_review_brokers_2022] private-action campaign represents the most extensive recent private-enforcement development.

## Prevalence Estimates by Technique Class

The empirical prevalence estimates for each self-promotion technique class vary greatly across platforms and categories. The framing article presents the aggregate summary estimates from the surveyed empirical literature. The composite estimates should be treated as order-of-magnitude summaries rather than as precise measurements, and the closing article treats the methodological considerations for prevalence estimation more fully.

Individual and coordinated review fabrication prevalence on consumer-review platforms is documented in [Luca and Zervas 2016][research_luca_zervas_2016] for Yelp at approximately sixteen percent filter rate, [He et al. 2022][research_he_hollenbeck_proserpio_2022] for Amazon at approximately thirty percent fake-review estimate in categories, [Mayzlin et al. 2014][research_mayzlin_dover_chevalier_2014] for Tripadvisor at approximately ten to fifteen percent estimate under the natural-experiment methodology, and the [European Commission 2023][ref_ec_2023_sweep] cross-platform sweep at rates varying by category from five to forty percent. The composite category-weighted prevalence estimator under sampling permits characterization as

$$
\hat{p}^{\text{comp}} = \sum_c w_c \hat{p}_c, \quad w_c = \frac{n_c}{\sum_{c'} n_{c'}}
\tag{70}
$$

with $w_c$ the volume-weighted category weight and $\hat{p}\_c$ the category-specific prevalence estimate, subject to sampling variance

$$
\text{Var}(\hat{p}^{\text{comp}}) = \sum_c w_c^2 \cdot \text{Var}(\hat{p}_c)
\tag{71}
$$

that allows standard confidence-interval construction under the delta-method approximation.

Follower-purchase and engagement-purchase prevalence on major social platforms varies by platform and account category, with typical estimates for the fraction of purchased or otherwise inauthentic followers on major accounts in the range of five to thirty percent, and higher rates in categories including cryptocurrency promotion and political mobilization. The [Cresci 2020][research_cresci_2020] survey and [Yang et al. 2019][research_yang_et_al_2020] provide the reference estimates.

Sockpuppet-network and coordinated inauthentic behavior prevalence is documented most extensively for state-sponsored operations in the [Bradshaw and Howard 2019][research_bradshaw_howard_2019], [Bradshaw et al. 2021][research_bradshaw_bailey_howard_2021], and platform-industry [Meta Adversarial Threat Report][ref_meta_atr] treatments. The estimated count of active state-sponsored inauthentic-behavior operations across the major platforms is in the range of tens to hundreds of active operations at any given time, with individual operation scale ranging from tens to hundreds of thousands of associated accounts.

Astroturfing prevalence is more difficult to estimate than other technique classes because astroturfing operations often operate through authentic-appearing organizational structures and produce content that does not clearly separate from authentic advocacy. The [Walker 2014][book_walker_2014] treatment documents the commercial astroturf-services industry at scale but does not provide a precise prevalence estimate for the population of active astroturf campaigns. The [Trustpilot Transparency Report][ref_trustpilot_transparency] and the [Fakespot Consumer Reports][ref_fakespot_consumer_reports] provide industry-side prevalence disclosure for the consumer-review subset.

Generative-model-produced content prevalence has grown rapidly since the 2022 large-language-model deployments. Contemporary estimates from [Yang and Menczer 2023][research_yang_menczer_2024] and [Sohail 2024][research_sohail_et_al_2024] document the increasing prevalence of AI-generated review and social-media content, with the prevalence rate remaining considerably uncertain due to detection difficulty.

The aggregate self-promotion manipulation prevalence across the platform ecosystem is captured by

$$
p_{\text{self-promo}}^{\text{aggregate}}(t) = \frac{\sum_c n_c(t) \cdot p_c^{\text{self-promo}}(t)}{\sum_c n_c(t)}
\tag{72}
$$

with $n_c(t)$ the total signal-event volume in category $c$ at time $t$ and $p_c^{\text{self-promo}}(t)$ the category-specific self-promotion prevalence rate. The aggregate estimate under conservative methodology is in the range of ten to twenty percent of the total reputation-signal volume across the surveyed platform ecosystem, with extensive category variation.

## Alternative Analytical Frameworks

The economic-signaling framework the miniseries adopts is one of several analytical frameworks under which the self-promotion technique inventory supports treatment. The framing article surveys the principal alternatives and identifies where the alternative frameworks would produce different conclusions from the model the miniseries adopts.

The advertising-and-marketing-theory framework treats self-promotion techniques as extensions of the advertising toolkit into digital reputation systems. The [Aaker 1991][book_aaker_1991] Managing Brand Equity, [Kotler and Keller 2016][book_kotler_keller_2016] Marketing Management, and adjacent treatments establish the framework. This formulation produces different conclusions than the reputation-manipulation framework in that it treats the manipulation-vs-legitimate-promotion boundary as a matter of degree along the advertising-effectiveness continuum rather than as a categorical distinction. The treatment predicts that platform-integrity enforcement will produce systematic advertising-market inefficiencies through the enforcement's effect on legitimate word-of-mouth marketing operating adjacent to the manipulation techniques.

The persuasion-psychology framework of [Cialdini 1984][book_cialdini_1984] Influence and [Petty and Cacioppo 1986][research_petty_cacioppo_1986] Elaboration Likelihood Model treats self-promotion techniques by the persuasion mechanisms they exploit. The framework identifies persuasion-mechanism vulnerabilities in consumer decision-making that manipulation techniques exploit and predicts consumer-response effects based on the technique's alignment with dominant persuasion pathways. The account produces different conclusions than the economic framework in that it emphasizes the cognitive-mechanism dimension of manipulation effectiveness independent of the information-asymmetry dimension.

The two-sided-market framework of [Rochet and Tirole 2003][research_rochet_tirole_2003] and [Rysman 2009][research_rysman_2009] treats the platform's mediation role as central to the manipulation equilibrium. The model identifies platform-design choices that shape the manipulation-equilibrium intensity through the cross-side network-effect structure. This formulation produces different conclusions than the technique-focused framework in that it treats the platform as an active party in the equilibrium rather than as a neutral infrastructure provider, which implies different regulatory-intervention recommendations focused on platform-design-choice regulation rather than on technique-specific enforcement.

The attention-economy framework of [Simon 1971][research_simon_1971] Designing Organizations for an Information-Rich World and [Wu 2016][book_wu_2016] The Attention Merchants treats reputation-signal manipulation as a subset of the broader attention-manipulation ecosystem. The treatment predicts that reforms internal to the reputation-manipulation framework will fail to address the underlying attention-economics dynamics and that broader attention-economy reform is required to significantly reduce equilibrium manipulation.

The influencer-and-creator-economy framework of [Abidin 2018][book_abidin_2018] Internet Celebrity, [Duffy 2017][book_duffy_2017] Not Getting Paid to Do What You Love, and [Bishop 2018][research_bishop_2019] Managing Visibility on YouTube treats self-promotion techniques as embedded in the broader creator-economy political-economy. This account predicts that reforms internal to the platform-integrity framework will fail to address the underlying labor-and-authenticity dynamics that generate the manipulation supply. The framework produces different regulatory-intervention recommendations focused on creator-economy structural reform rather than on manipulation-specific enforcement.

The search-theory framework of [Stigler 1961][research_stigler_1961] and subsequent search-cost literature treats self-promotion techniques by the consumer-search-cost changes they impose. The account produces different conclusions than the direct-signaling framework in that it emphasizes the equilibrium-price and quality-signaling effects that follow from consumer-search-cost changes independently of the direct reputation-signal-informativeness effect.

The regulatory-capture framework of [Stigler 1971][research_stigler_1971] The Theory of Economic Regulation extends to platform-integrity-enforcement politics through the observation that regulated industries capture their regulators over time. The model predicts that platform-integrity enforcement will systematically underweight consumer interests relative to producer interests as the manipulation-service industry organizes to influence platform policy and regulatory rule-making.

The adversarial-machine-learning framework of [Goodfellow et al. 2014][research_goodfellow_shlens_szegedy_2014] and subsequent adversarial-ML literature treats detection-system-vs-manipulation-technique dynamics as an adversarial classification problem with algorithmic implications. This formulation produces different detection-system-design recommendations than the classical classification framework, emphasizing robustness against adversarial adaptation over accuracy on labeled-training-distribution instances.

Each alternative framework offers analytical leverage the miniseries does not fully develop. The miniseries adopts the economic-signaling framework as the primary organizing structure because it provides the most tractable formalization of the manipulator-platform-consumer strategic interaction and connects most directly to the empirical detection and enforcement literatures. The closing article treats the account selection more fully and identifies the empirical questions on which the alternative frameworks would predict different observations.

## Terminological Note

The article adopts the terminology introduced in the framing article of the miniseries at [Virtual Reputation Manipulation Theory and Analytical Framework][related_post_a277_theory]. The self-promotion class refers to the manipulation techniques oriented at inflating the actor's own reputation, and the competitor-attack class refers to the techniques oriented at degrading a competitor's reputation. The two classes are treated separately in this article and the next respectively, with the closing article treating the detection and organic-establishment landscape that responds to both.

The term technique class refers to the analytical grouping of manipulation practices sharing signal channel, technique-space position, and detection-signature characteristics. The term signal channel refers to the reputation-system channel targeted by a technique class (reviews, followers, engagement, ranking, credentials, endorsement, association). The term detection signature refers to the observable patterns that distinguish a manipulation instance from an authentic instance of the same signal channel. The term countermeasure refers to the platform, legal, or infrastructure response to a technique class or manipulation instance. The article uses the platform-integrity industry terminology (coordinated inauthentic behavior, adversarial threat, take-down) where the industry terminology is more precise than the academic terminology.

## Load-Bearing Open Questions

- What is the correct empirical characterization of the aggregate self-promotion manipulation prevalence across the platform ecosystem, and how does the estimate change under alternative methodologies? The current range of empirical estimates spans sizable variation, and no single point estimate commands consensus.
- What is the correct empirical characterization of the causal impact of self-promotion technique classes on downstream consumer purchase behavior? The [Luca 2016][research_luca_2016], [Chevalier and Mayzlin 2006][research_chevalier_mayzlin_2006], and [Anderson and Magruder 2012][research_anderson_magruder_2012] treatments provide the causal-inference foundation but leave appreciable variation in the effect-size estimates across settings.
- What is the correct empirical characterization of the marginal deterrent effect of enforcement actions on self-promotion manipulation prevalence? The pre-and-post studies of major FTC enforcement actions provide the empirical foundation, but the marginal-deterrent estimates remain contested.
- What is the correct empirical characterization of the equilibrium impact of generative-model deployment on self-promotion manipulation prevalence and on detection difficulty? The [Sohail 2024][research_sohail_et_al_2024] and [Sadasivan et al. 2023][research_sadasivan_et_al_2023] treatments provide the initial evidence, but the equilibrium trajectory remains substantially uncertain.
- What is the correct comparative treatment of the self-promotion manipulation ecosystem across national platform-regulation regimes, and which regulatory instruments produce the most significant equilibrium-manipulation reduction?
- What is the correct empirical characterization of the interaction between commercial self-promotion manipulation and state-sponsored information operations, and does the interaction produce systematic effects on the commercial reputation-manipulation ecosystem beyond the state-operation-specific effects?
- How should the platform-integrity operations, the regulatory framework, and the market response coordinate to reduce the equilibrium self-promotion manipulation intensity, and what is the equilibrium detection intensity that maximizes joint surplus across producer, consumer, and platform welfare?

These questions recur throughout the miniseries and are revisited in the closing synthesis.

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 72 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 72, 36 are established and 36 are bespoke.
Prices are in United States dollars per unit named in each range, rates are per unit time on the platform in question, and most other quantities are dimensionless scores or abstract axis values, while several letters are reused, with $\alpha$ a self-excitation gain in the Hawkes process and a saturation rate in the domain value, $\rho$ an operator utilisation in the queue and a rank score elsewhere, and $\kappa$ a transfer coefficient rather than an agreement statistic.

*Equation 1, Bespoke Six-Axis Technique Vector.*
The article characterises each self-promotion technique by its positions on the six analytical axes of the framing article.

$$
\mathbf{a}_k = (a_k^{\text{signal}}, a_k^{\text{obj}}, a_k^{\text{struct}}, a_k^{\text{model}}, a_k^{\text{interact}}, a_k^{\text{adapt}})
\tag{1}
$$

*Equation 2, Bespoke Weighted Technique Distance.*
The article defines the distance between techniques as a weighted sum of axis-specific distances, with weights it leaves to the analyst.

$$
d(t_j, t_k) = \sum_{c \in \text{axes}} w_c \, \delta_c(a_j^c, a_k^c)
\tag{2}
$$

**Equation 3, Aggregate Self-Promotion Volume.**
The aggregate volume is the sum over techniques and categories of signal-event volume times the prevalence rate.

$$
V_{\text{self-promo}}(t) = \sum_{k \in \mathcal{T}} \sum_{c \in \text{categories}} n_{k,c}(t) \cdot p_{k,c}(t)
\tag{3}
$$

*Equation 4, Bespoke Taxonomy Coverage.*
The article defines coverage as the fraction of observed manipulation instances that the taxonomy assigns to some technique, a recall analogue.

$$
\text{Coverage}(\mathcal{T}, \Omega) = \frac{|\{\omega \in \Omega : \exists t_k \in \mathcal{T}, \omega \text{ assigned to } t_k\}|}{|\Omega|}
\tag{4}
$$

*Equation 5, Bespoke Stylometric Feature Vector.*
The article lists the stylometric components that a contemporary fake-review detector takes as input for a review.

$$
\mathbf{f}_r = (\text{POS-ratios}, \text{n-gram distributions}, \text{lexical richness}, \text{sentiment intensity}, \text{first-person ratio}, \text{superlative rate})
\tag{5}
$$

*Equation 6, Bespoke Rating-Shift Model.*
The article writes the observed rating change as the authentic change plus the gap between the injected fake reviews' average rating and the prior average, weighted by their share of all reviews.

$$
\Delta r_i^{\text{obs}} = \Delta r_i^{\text{authentic}} + n_i^{\text{fake}} \cdot (\bar{r}_{\text{fake}} - \bar{r}_{\text{pre}}) / (N_i + n_i^{\text{fake}})
\tag{6}
$$

**Equation 7, Precision, Recall and F1 Score.**
Precision is the fraction of flagged items that are manipulated, recall is the fraction of manipulated items that are flagged, and the F1 score is their harmonic mean.

$$
\text{precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}, \quad \text{recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}, \quad F_1 = \frac{2 \cdot \text{precision} \cdot \text{recall}}{\text{precision} + \text{recall}}
\tag{7}
$$

**Equation 8, Standardised Arrival-Rate Residual.**
The burst statistic is the observed review-arrival rate less its historical mean, divided by its historical standard deviation.

$$
z_{\text{burst}}(t) = \frac{\lambda(t) - \bar{\lambda}}{\sigma_\lambda}
\tag{8}
$$

*Equation 9, Bespoke Price Range of a Fabricated Review.*
The article states a marketplace price of 1 to 30 United States dollars per fabricated review.

$$
p_{\text{fake-review}} \in [1, 30] \text{ USD per review}
\tag{9}
$$

*Equation 10, Bespoke Producer Surplus From Review Manipulation.*
The article writes the surplus as the rating shift times a revenue coefficient times a sales volume term, less the purchase cost of the injected reviews.

$$
\pi_i^{\text{manip}} = R_i^{\text{shift}} \cdot v \cdot Q_i - n_i \cdot p_{\text{fake-review}}
\tag{10}
$$

**Equation 11, Hawkes Self-Exciting Point Process.**
The arrival intensity is a baseline rate plus an exponentially decaying contribution from each earlier arrival, the Hawkes process with an exponential kernel.

$$
\lambda(t) = \mu + \alpha \sum_{t_i < t} e^{-\beta(t - t_i)}
\tag{11}
$$

**Equation 12, Jaccard Similarity of N-Gram Sets.**
The overlap of two reviews is the size of the intersection of their n-gram sets divided by the size of the union.

$$
\text{sim}_n(r_i, r_j) = \frac{|N_n(r_i) \cap N_n(r_j)|}{|N_n(r_i) \cup N_n(r_j)|}
\tag{12}
$$

**Equation 13, Newman Modularity.**
Modularity compares the edges within communities with the number expected under a degree-preserving random graph.

$$
Q = \frac{1}{2m} \sum_{ij} \left[A_{ij} - \frac{k_i k_j}{2m}\right] \delta(c_i, c_j)
\tag{13}
$$

*Equation 14, Bespoke Sockpuppet Construction Cost.*
The article writes the cost of a sockpuppet operation as a fixed setup cost plus the number of identities times a marginal cost that falls with scale.

$$
C_{\text{sockpuppet}}(n) = c_{\text{fixed}} + n \cdot c_{\text{marginal}}(n)
\tag{14}
$$

*Equation 15, Bespoke Marginal Identity Cost Range.*
The article states a marginal cost of 0.5 to 10 United States dollars per sockpuppet identity used for review deposition.

$$
c_{\text{marginal}} \in [0.5, 10] \text{ USD per identity}
\tag{15}
$$

**Equation 16, Cosine Similarity of Behavioural Features.**
The similarity of two accounts is the inner product of their behavioural feature vectors divided by the product of the vector norms.

$$
s_{ij}^{\text{behav}} = \frac{\langle \mathbf{f}_i, \mathbf{f}_j\rangle}{\|\mathbf{f}_i\| \cdot \|\mathbf{f}_j\|}
\tag{16}
$$

**Equation 17, Bayesian Posterior of Sockpuppet Linkage.**
Bayes rule for a binary hypothesis gives the posterior probability that two accounts are linked given their behavioural similarity.

$$
\Pr(\text{sockpuppet}_{ij} \mid s_{ij}^{\text{behav}}) = \frac{p(s_{ij} \mid \text{link}) \pi_{\text{link}}}{p(s_{ij} \mid \text{link}) \pi_{\text{link}} + p(s_{ij} \mid \neg \text{link})(1 - \pi_{\text{link}})}
\tag{17}
$$

**Equation 18, Survival Function From a Hazard Rate.**
The probability that an account remains active at a given time is the exponential of the negative integrated hazard.

$$
S(t) = \Pr(\text{account active at } t) = e^{-\int_0^t h(\tau) d\tau}
\tag{18}
$$

**Equation 19, Naive Bayes Likelihood Ratio.**
Under conditional independence of the features, the joint likelihood ratio for linkage is the product of the per-feature likelihood ratios.

$$
\Lambda_{ij}^{\text{sockpuppet}} = \prod_{k \in \text{features}} \frac{p(f_k^{ij} \mid \text{link})}{p(f_k^{ij} \mid \neg \text{link})}
\tag{19}
$$

*Equation 20, Bespoke Linear Cost of Generated Reviews.*
The article approximates the cost of generated reviews as a per-review interface cost times volume plus a fixed prompt-engineering cost, which removes the convexity of the classical cost function.

$$
c_{\text{LLM-review}}(m) \approx c_{\text{API}} \cdot m + c_{\text{prompt-eng}}
\tag{20}
$$

**Equation 21, Detection Accuracy Approaching Chance.**
As the quality of generated text approaches that of human text, the area under the curve of any detector approaches one half, the result the article attributes to Sadasivan and colleagues.
[Sadasivan et al. 2023][research_sadasivan_et_al_2023]

$$
\text{AUC}_{\text{detect}}(q_{\text{gen}}) \to 0.5 \text{ as } q_{\text{gen}} \to q_{\text{human}}
\tag{21}
$$

**Equation 22, Log-Likelihood Ratio for Watermark Detection.**
The information content of a text is the logarithm of the ratio of its likelihood under the watermarked distribution to its likelihood under the unmarked distribution.

$$
I_{\text{watermark}}(x) = \log \frac{p_{\text{watermarked}}(x)}{p_{\text{unmarked}}(x)}
\tag{22}
$$

**Equation 23, Perplexity Under a Reference Model.**
Perplexity is the exponential of the negative mean log probability of each token given the tokens before it.

$$
\text{PPL}(x) = \exp\left(-\frac{1}{|x|} \sum_{i} \log p_{\text{ref}}(x_i \mid x_{<i})\right)
\tag{23}
$$

**Equation 24, Bit-Error Rate Under Paraphrase.**
The bit-error rate is the fraction of recovered watermark bits that differ between the original and the paraphrased text.

$$
\text{BER}_{\text{para}}(x, x') = \frac{|\{i : w_i(x) \neq w_i(x')\}|}{|w(x)|}
\tag{24}
$$

*Equation 25, Bespoke Price Range of a Purchased Follower.*
The article states a price of $10^{-4}$ to $10^{-2}$ United States dollars per purchased follower.

$$
p_{\text{follower}} \in [10^{-4}, 10^{-2}] \text{ USD per follower}
\tag{25}
$$

*Equation 26, Bespoke Fake-Follower Fraction Range.*
The article summarises the fraction of purchased or inauthentic followers on typical accounts as 5 to 30 per cent.

$$
p_{\text{fake-follower}} \in [0.05, 0.30]
\tag{26}
$$

**Equation 27, Engagement-to-Follower Ratio.**
The engagement rate of an account is the mean engagement per post divided by the follower count.

$$
\rho_i^{\text{follow-engage}} = \frac{\bar{e}_i}{F_i}
\tag{27}
$$

**Equation 28, Logistic Growth of Organic Followers.**
The logistic equation describes follower growth that is proportional to the current count and slows as the count approaches an account-specific ceiling.

$$
\frac{dF_i}{dt} = r \, F_i \left(1 - \frac{F_i}{K}\right)
\tag{28}
$$

*Equation 29, Bespoke Constant-Hazard Survival of Purchased Followers.*
The article assumes a constant removal hazard, so that purchased followers decay exponentially from their initial count.

$$
S_{\text{purchased}}(t) = e^{-\lambda_{\text{enforce}} t} \cdot S_{\text{purchased}}(0)
\tag{29}
$$

*Equation 30, Bespoke Price Range of an Engagement Action.*
The article states a price of $10^{-4}$ to $10^{-2}$ United States dollars per purchased engagement action.

$$
p_{\text{engagement}} \in [10^{-4}, 10^{-2}] \text{ USD per action}
\tag{30}
$$

*Equation 31, Bespoke Pod Participation Statistic.*
The article multiplies the reciprocity ratio of the engagement graph by its clustering coefficient to score engagement-pod participation.

$$
\rho_{\text{pod}}(G) = \frac{|\{(i,j) : (i \to j) \wedge (j \to i)\}|}{|E(G)|} \cdot C(G)
\tag{31}
$$

**Equation 32, Shannon Entropy of View Sources.**
The diversity of view sources is the Shannon entropy of the fractions of views from each address block.

$$
H_{\text{view-source}} = -\sum_{a} p_a \log p_a
\tag{32}
$$

**Equation 33, PageRank Recurrence.**
The PageRank of a page is a teleportation term plus the damped sum of the PageRank of each linking page divided by its outbound link count.
[Brin and Page 1998][research_page_brin_1998]
[Page Brin Motwani Winograd 1999][research_page_brin_motwani_winograd_1999]

$$
\text{PR}(p) = \frac{1 - d}{N} + d \sum_{q \in B_p} \frac{\text{PR}(q)}{L(q)}
\tag{33}
$$

*Equation 34, Bespoke Marginal PageRank Return per Inbound Link.*
The article approximates the gain from one more inbound link as the damping factor times the average over the inbound set of each page's PageRank divided by its outbound link count.

$$
\frac{\partial \text{PR}(p)}{\partial |B_p|} \approx d \cdot \overline{\text{PR}/L}_{B_p}
\tag{34}
$$

*Equation 35, Bespoke First-Order Rank-Position Shift.*
The article approximates the change in rank position as the local density of pages in rank score times the change in score.

$$
\Delta \text{rank} \approx -\frac{\partial N_{<\rho}}{\partial \rho} \cdot \Delta \rho
\tag{35}
$$

**Equation 36, TrustRank Recurrence.**
Trust propagates from a hand-labelled seed set through the link graph by a damped recurrence of the same form as PageRank.
[TrustRank propagation algorithm][ref_gyongyi_2004_trustrank_paper]

$$
t(p) = (1 - d) \, \mathbb{1}[p \in S_{\text{seed}}] + d \sum_{q \in B_p} \frac{t(q)}{L(q)}
\tag{36}
$$

*Equation 37, Bespoke Cloaking Differential.*
The article measures cloaking as a content distance between the pages served to a crawler and to a human visitor.

$$
\Delta_{\text{cloak}}(p) = d_{\text{content}}(C_{\text{crawler}}(p), C_{\text{human}}(p))
\tag{37}
$$

**Equation 38, Standardised Download-Rate Deviation.**
The statistic is the download rate of an app less the category mean, divided by the category standard deviation.

$$
z_{\text{download}}(t) = \frac{D(t) - \bar{D}_{\text{category}}(t)}{\sigma_{D,\text{category}}(t)}
\tag{38}
$$

**Equation 39, SybilGuard Bound on the Sybil Region.**
Under fast mixing of the honest region and a bounded number of attack edges, the SybilGuard protocol bounds the number of Sybil identities it accepts.
[Yu et al. 2006][research_yu_et_al_2006]

$$
|S_{\text{Sybil}}| \leq O(\sqrt{n \log n})
\tag{39}
$$

**Equation 40, Graph Conductance of a Cut.**
Conductance is the number of edges crossing a cut divided by the smaller of the edge counts on either side.

$$
\Phi(S) = \frac{|E(S, \bar{S})|}{\min(|E(S)|, |E(\bar{S})|)}
\tag{40}
$$

*Equation 41, Bespoke Sybil Operation Cost.*
The article writes the cost of a Sybil network as a setup cost plus, for each identity, a construction cost and an activity cost accrued over the operating horizon.

$$
C_{\text{Sybil}}(N, T) = c_{\text{setup}} + N \cdot (c_{\text{ident}} + T \cdot c_{\text{activity}})
\tag{41}
$$

*Equation 42, Bespoke Sybil Network Size Range.*
The article states a network size of $10^3$ to $10^6$ accounts per operation.

$$
N \in [10^3, 10^6] \text{ Sybil accounts per operation}
\tag{42}
$$

**Equation 43, Pearson Correlation of Appearance Timestamps.**
The cross-platform statistic is the Pearson correlation between the timestamps at which the same content appears on two platforms.

$$
r_{\text{cross}}(P_1, P_2) = \frac{\sum_c (t_c^{P_1} - \bar{t}^{P_1})(t_c^{P_2} - \bar{t}^{P_2})}{\sqrt{\sum_c (t_c^{P_1} - \bar{t}^{P_1})^2 \sum_c (t_c^{P_2} - \bar{t}^{P_2})^2}}
\tag{43}
$$

*Equation 44, Bespoke Logistic Amplification Cascade.*
The article models reach as a discrete recurrence with a per-step gain that is throttled as reach approaches a ceiling set by audience size.

$$
R_{\text{cascade}}(t+1) = R_{\text{cascade}}(t) \cdot \eta \cdot (1 - \frac{R_{\text{cascade}}(t)}{\bar{R}})
\tag{44}
$$

*Equation 45, Bespoke Click-Farm Throughput.*
The article estimates throughput as the operator count times hours per operator per day times actions per operator hour.

$$
\Lambda_{\text{click-farm}} = N_{\text{operator}} \cdot h \cdot r
\tag{45}
$$

*Equation 46, Bespoke Click-Farm Throughput Range.*
The article states a throughput of $10^4$ to $10^6$ actions per day per operation.

$$
\Lambda \in [10^4, 10^6] \text{ actions per day per operation}
\tag{46}
$$

**Equation 47, Mean Queue Length of an M/M/c Queue.**
The expected number of tasks waiting in a multi-server queue with Poisson arrivals and exponential service follows the Erlang formula in the utilisation and the probability of an empty system.

$$
L_q = \frac{(N_{\text{op}} \rho)^{N_{\text{op}}} \rho}{N_{\text{op}}! (1 - \rho)^2} P_0
\tag{47}
$$

**Equation 48, Restricted Geographic Entropy.**
The geographic diversity of activity is the Shannon entropy of the fractions of activity originating from each click-farm-associated region.

$$
H_{\text{geo}}^{\text{restrict}} = -\sum_{g \in G_{\text{cf}}} p_g \log p_g
\tag{48}
$$

**Equation 49, Bayesian Posterior Over State Attribution.**
Bayes rule over a discrete set of candidate state actors gives the posterior attribution given an observed fingerprint vector.

$$
\Pr(\text{state} = s \mid \mathbf{F}) = \frac{\Pr(\mathbf{F} \mid s) \pi(s)}{\sum_{s'} \Pr(\mathbf{F} \mid s') \pi(s')}
\tag{49}
$$

**Equation 50, Coordination Z-Score.**
The statistic is the observed count of simultaneous releases less its expectation under independent release, divided by the null standard deviation.

$$
z_{\text{coord}} = \frac{\text{(observed simultaneous releases)} - \mu_{\text{null}}}{\sigma_{\text{null}}}
\tag{50}
$$

**Equation 51, Annual Volume of 50 Cent Army Posts.**
King, Pan and Roberts estimate that state-directed fabrication produces roughly $4.4 \times 10^8$ social media posts per year.
[King et al. 2017][research_king_pan_roberts_2017]

$$
V_{\text{50-cent}} \approx 4.4 \times 10^8 \text{ posts per year}
\tag{51}
$$

*Equation 52, Bespoke Posting-Time Concentration.*
The article defines concentration as the fraction of posts falling within a short window aligned with the operators' work schedule.

$$
\text{Conc}(\Delta t) = \frac{|\{p : t_p \in [\Delta t]\}|}{|\text{posts}|}
\tag{52}
$$

*Equation 53, Bespoke Verification Informativeness Change.*
The article measures the effect of paid verification as the mutual information between authenticity and an earned badge less that for a paid badge.

$$
\Delta I_{\text{verify}} = I(\text{authentic} ; \text{badge}_{\text{earned}}) - I(\text{authentic} ; \text{badge}_{\text{paid}})
\tag{53}
$$

**Equation 54, Classification Accuracy Under a Base Rate.**
Accuracy is the fraction correctly classified, which equals the true-positive rate weighted by the base rate of authentic credentials plus the true-negative rate weighted by its complement.

$$
\text{Acc}_{\text{cred}} = \frac{|\text{correctly classified}|}{|\text{all}|} = \Pr(\text{verify} \mid \text{authentic}) \cdot \pi_{\text{authentic}} + \Pr(\neg \text{verify} \mid \text{fabricated}) \cdot (1 - \pi_{\text{authentic}})
\tag{54}
$$

*Equation 55, Bespoke Endorsement Value Transfer.*
The article assumes that an endorsement transfers a fixed fraction of the endorser's reputation stock to the target.

$$
V_{\text{transfer}}(E \to T) = \kappa_{E,T} \cdot R_E
\tag{55}
$$

*Equation 56, Bespoke Transfer Coefficient Range.*
The article states that the transfer coefficient typically lies between 0.01 and 0.30.

$$
\kappa \in [0.01, 0.30]
\tag{56}
$$

*Equation 57, Bespoke Disclosure Effect on Transfer.*
The article defines the disclosure effect as the transfer coefficient without disclosure less the coefficient with it.
[Boerman 2018][research_boerman_et_al_2018]

$$
\Delta \kappa_{\text{disclose}} = \kappa_{\text{undisclosed}} - \kappa_{\text{disclosed}}
\tag{57}
$$

*Equation 58, Bespoke Exponential Cross-Platform Transfer Decay.*
The article assumes that transferred reputation starts at a fraction of its value on the origin platform and decays exponentially on the target platform.

$$
R_T^{P_2}(t) = R_T^{P_1}(0) \cdot \kappa_{P_1 \to P_2} \cdot e^{-\gamma t}
\tag{58}
$$

*Equation 59, Bespoke Saturating Domain-Age Value.*
The article assumes that the reputation value of a domain rises toward a ceiling as one minus a decaying exponential in its age.

$$
V_{\text{domain}}(a) = V_0 \, \bigl(1 - e^{-\alpha a}\bigr)
\tag{59}
$$

*Equation 60, Bespoke Signal-Axis Tuple.*
The article places each technique class on the signal axis by its volume rate, channel count, injection fidelity and cross-channel amplification.

$$
\mathbf{a}_k^{\text{signal}} = (v_k, C_k, f_k, X_k)
\tag{60}
$$

*Equation 61, Bespoke Objective-Axis Utility.*
The article writes the objective of each technique class as a weighted sum of six goal functions for rating, following, engagement, rank, credentials and apparent support.

$$
U_k(\mathbf{x}) = \lambda_k^{\text{rating}} g_{\text{rating}}(\mathbf{x}) + \lambda_k^{\text{follow}} g_{\text{follow}}(\mathbf{x}) + \lambda_k^{\text{engage}} g_{\text{engage}}(\mathbf{x}) + \lambda_k^{\text{rank}} g_{\text{rank}}(\mathbf{x}) + \lambda_k^{\text{cred}} g_{\text{cred}}(\mathbf{x}) + \lambda_k^{\text{support}} g_{\text{support}}(\mathbf{x})
\tag{61}
$$

*Equation 62, Bespoke Structure-Axis Tuple.*
The article places each technique class on the structure axis by hierarchy depth, branching factor and operator population.

$$
\mathbf{a}_k^{\text{struct}} = (D_k, B_k, N_k)
\tag{62}
$$

*Equation 63, Bespoke First-Order Adaptation Dynamics.*
The article assumes that a technique's state relaxes toward its environment-dependent optimum with a single migration time constant, perturbed by exogenous noise.

$$
\frac{dS_k}{dt} = -\frac{1}{\tau_k}(S_k - S_k^{*}(t)) + \xi_k(t)
\tag{63}
$$

*Equation 64, Bespoke Self-Promotion Coupling Matrix.*
The article defines a matrix of partial derivatives between axis positions to encode the cross-axis dependencies of self-promotion.

$$
C^{\text{self-promo}} = \left[\frac{\partial a^b}{\partial a^a}\right]_{a, b \in \text{axes}}
\tag{64}
$$

**Equation 65, Generic Standardised Anomaly Score.**
The anomaly score is a test statistic less its expectation under the null model, divided by its null standard deviation.

$$
z_{\text{anomaly}} = \frac{T(\mathbf{x}) - E_{H_0}[T]}{\sqrt{\text{Var}_{H_0}[T]}}
\tag{65}
$$

**Equation 66, Majority-Vote Ensemble Accuracy.**
For independent classifiers with a common error rate, the probability that a majority vote is correct is one less the binomial probability that at least half err.

$$
P_{\text{ensemble}}(\text{correct}) \geq 1 - \sum_{k=\lceil M/2 \rceil}^{M} \binom{M}{k} p^k (1 - p)^{M - k}
\tag{66}
$$

*Equation 67, Bespoke Verification Friction Cost.*
The article assembles the friction of identity verification as the sum of user time, privacy loss and platform processing costs, each rising with stringency.

$$
C_{\text{verify}}(v) = c_{\text{user-time}}(v) + c_{\text{privacy-loss}}(v) + c_{\text{platform-processing}}(v)
\tag{67}
$$

**Equation 68, Per-Account Rate Limit.**
A rate limit bounds the observed activity rate of every account by a platform maximum.

$$
\lambda_i^{\text{observed}} \leq \lambda_{\text{max}}, \quad \forall i
\tag{68}
$$

**Equation 69, Signature Validity Indicator.**
Provenance verification is the indicator that the signature attached to the content verifies under the public key of the claimed origin.

$$
V(\text{content}, \sigma) = \mathbb{1}[\text{Verify}(\text{pk}, \text{content}, \sigma)]
\tag{69}
$$

**Equation 70, Volume-Weighted Composite Prevalence.**
The composite estimate is the mean of category estimates weighted by each category's share of volume.

$$
\hat{p}^{\text{comp}} = \sum_c w_c \hat{p}_c, \quad w_c = \frac{n_c}{\sum_{c'} n_{c'}}
\tag{70}
$$

**Equation 71, Variance of the Composite Prevalence.**
For independent category estimates with fixed weights, the variance of the composite is the sum of squared weights times the category variances.

$$
\text{Var}(\hat{p}^{\text{comp}}) = \sum_c w_c^2 \cdot \text{Var}(\hat{p}_c)
\tag{71}
$$

**Equation 72, Volume-Weighted Aggregate Self-Promotion Prevalence.**
The aggregate prevalence is the category prevalence rates weighted by signal-event volume and divided by total volume.

$$
p_{\text{self-promo}}^{\text{aggregate}}(t) = \frac{\sum_c n_c(t) \cdot p_c^{\text{self-promo}}(t)}{\sum_c n_c(t)}
\tag{72}
$$

### Notation

- $\mathbf{a}_k$, the six-axis position vector of technique $k$
- $w_c$, the weight of axis $c$ in the technique distance, and separately the volume weight of category $c$ in the composite prevalence
- $n_{k,c}(t)$, the signal-event volume for technique $k$ in category $c$
- $p_{k,c}(t)$, the prevalence rate for technique $k$ in category $c$
- $\Omega$, the observed population of manipulation instances
- $\Delta r_i^{\text{obs}}$, the observed rating change
- $n_i^{\text{fake}}$, the injected fake-review count
- $N_i$, the pre-injection authentic-review count
- $\lambda(t)$, the observed review-arrival rate, or the Hawkes intensity
- $\mu$, the baseline arrival rate of the Hawkes process
- $\beta$, the decay rate of the Hawkes kernel
- $R_i^{\text{shift}}$, the rating shift produced by the injection
- $v$, the per-rating-point revenue coefficient
- $N_n(r_i)$, the set of $n$-grams appearing in review $r_i$
- $A_{ij}$, the reviewer-business adjacency
- $k_i$, the degree of reviewer $i$
- $m$, the total edge count in the modularity, and the injection volume in the generated-review cost
- $c_{\text{marginal}}$, the per-identity marginal cost of a sockpuppet
- $\pi_{\text{link}}$, the base-rate prior of sockpuppet linkage
- $h(\tau)$, the hazard rate of account removal
- $q_{\text{gen}}$, the quality of the generative model
- $F_i$, the follower count of account $i$
- $\bar{e}_i$, the mean per-post engagement
- $K$, the account-specific follower ceiling
- $\lambda_{\text{enforce}}$, the per-account removal hazard for purchased followers
- $C(G)$, the clustering coefficient of the engagement graph
- $p_a$, the fraction of views from address block $a$
- $\text{PR}(p)$, the PageRank of page $p$
- $d$, the damping factor, typically near 0.85
- $B_p$, the set of pages linking to page $p$
- $L(q)$, the outbound link count of page $q$
- $t(p)$, the TrustRank trust score of page $p$
- $\Phi(S)$, the conductance of the cut around node set $S$
- $\rho$, the operator utilisation in the queue, and the rank score in the rank-shift approximation
- $N_{\text{op}}$, the click-farm operator count in the queue model
- $P_0$, the probability of an empty queue
- $\kappa_{E,T}$, the fraction of endorser reputation transferred to the target
- $\gamma$, the reputation decay rate on the target platform
- $V_0$, the asymptotic reputation value of a domain
- $\tau_k$, the technique-migration time constant
- $p$, the error rate of an individual classifier in the ensemble, and a page in the PageRank recurrence
- $M$, the ensemble size
- $\hat{p}^{\text{comp}}$, the composite category-weighted prevalence estimate

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- Alvisi, L., A. Clement, A. Epasto, S. Lattanzi, and A. Panconesi. 2013. "SoK: The Evolution of Sybil Defense via Social Networks." In *2013 IEEE Symposium on Security and Privacy*. IEEE. [https://doi.org/10.1109/sp.2013.33][research_alvisi_et_al_2013]
- Brin, Sergey, and Lawrence Page. 1998. "The Anatomy of a Large-Scale Hypertextual Web Search Engine." *Computer Networks and ISDN Systems* 30 (1–7): 107–17. [https://doi.org/10.1016/s0169-7552(98)00110-x][research_page_brin_1998]
- Chandola, Varun, Arindam Banerjee, and Vipin Kumar. 2009. "Anomaly Detection: A Survey." *ACM Computing Surveys* 41 (3): 1–58. [https://doi.org/10.1145/1541880.1541882][research_chandola_banerjee_kumar_2009]
- Cho, Charles H., Martin L. Martens, Hakkyun Kim, and Michelle Rodrigue. 2011. "Astroturfing Global Warming: It Isn’t Always Greener on the Other Side of the Fence." *Journal of Business Ethics* 104 (4): 571–87. [https://doi.org/10.1007/s10551-011-0950-6][research_cho_et_al_2011]
- Cresci, Stefano, Roberto Di Pietro, Marinella Petrocchi, Angelo Spognardi, and Maurizio Tesconi. 2015. "Fame for Sale: Efficient Detection of Fake Twitter Followers." *Decision Support Systems* 80: 56–71. [https://doi.org/10.1016/j.dss.2015.09.003][research_cresci_et_al_2015]
- Diamond, Peter A. 1971. "A Model of Price Adjustment." *Journal of Economic Theory* 3 (2): 156–68. [https://doi.org/10.1016/0022-0531(71)90013-5][research_diamond_1971]
- Douceur, John R. 2002. "The Sybil Attack." In *Peer-to-Peer Systems*. Springer Berlin Heidelberg. [https://doi.org/10.1007/3-540-45748-8\_24][research_douceur_2002]
- Fawcett, Tom. 2006. "An Introduction to ROC Analysis." *Pattern Recognition Letters* 27 (8): 861–74. [https://doi.org/10.1016/j.patrec.2005.10.010][research_fawcett_2006]
- Malbon, Justin. 2013. "Taking Fake Online Consumer Reviews Seriously." *Journal of Consumer Policy* 36 (2): 139–57. [https://doi.org/10.1007/s10603-012-9216-7][research_malbon_2013]
- Papakyriakopoulos, Orestis, Juan Carlos Medina Serrano, and Simon Hegelich. 2020. "Political Communication on Social Media: A Tale of Hyperactive Users and Bias in Recommender Systems." *Online Social Networks and Media* 15: 100058. [https://doi.org/10.1016/j.osnem.2019.100058][research_papakyriakopoulos_et_al_2020]
- Starbird, Kate. 2019. "Disinformation’s Spread: Bots, Trolls and All of Us." *Nature* 571 (7766): 449–449. [https://doi.org/10.1038/d41586-019-02235-x][research_starbird_2019]
- Tsikerdekis, Michail, and Sherali Zeadally. 2014. "Multiple Account Identity Deception Detection in Social Media Using Nonverbal Behavior." *IEEE Transactions on Information Forensics and Security* 9 (8): 1311–21. [https://doi.org/10.1109/tifs.2014.2332820][research_tsikerdekis_zeadally_2014]
- Wang, Guan, Sihong Xie, Bing Liu, and Philip S. Yu. 2011. "Review Graph Based Online Store Review Spammer Detection." In *2011 IEEE 11th International Conference on Data Mining*. IEEE. [https://doi.org/10.1109/icdm.2011.124][research_wang_et_al_2011]
- Weerkamp, Wouter, and Maarten de Rijke. 2012. "Credibility-Inspired Ranking for Blog Post Retrieval." *Information Retrieval* 15 (3–4): 243–77. [https://doi.org/10.1007/s10791-011-9182-8][research_weerkamp_derijke_2012]
- Wu, Yuanyuan, Eric W. T. Ngai, Pengkun Wu, and Chong Wu. 2020. "Fake Online Reviews: Literature Review, Synthesis, and Directions for Future Research." *Decision Support Systems* 132: 113280. [https://doi.org/10.1016/j.dss.2020.113280][research_wu_et_al_2020]
- Yang, Kai-Cheng, Onur Varol, Clayton A. Davis, Emilio Ferrara, Alessandro Flammini, and Filippo Menczer. 2019. "Arming the Public with Artificial Intelligence to Counter Social Bots." *Human Behavior and Emerging Technologies* 1 (1): 48–61. [https://doi.org/10.1002/hbe2.115][research_yang_et_al_2020]
- Yu, Haifeng, Phillip B. Gibbons, Michael Kaminsky, and Feng Xiao. 2008. "SybilLimit: A near-Optimal Social Network Defense against Sybil Attacks." In *2008 IEEE Symposium on Security and Privacy (sp 2008)*. IEEE. [https://doi.org/10.1109/sp.2008.13][research_yu_et_al_2008]

### Primary Sources, Non-Peer-Reviewed

- "16 CFR Part 255 FTC Guides on Endorsements and Testimonials." n.d. Accessed October 25, 2026. [https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255][ref_ftc_endorsement_guides_16_cfr_255]
- Ali. 2017. *Same Same but Different Search Advertising*. [https://scholar.google.com/scholar?q=Same+Same+but+Different+Search+Advertising+Ali+2017][research_ali_et_al_2017]
- Anderson, Michael, and Jeremy Magruder. 2012. "Learning from the Crowd: Regression Discontinuity Estimates of the Effects of an Online Review Database." *Economic Journal* 122 (563): 957–89. [https://doi.org/10.1111/j.1468-0297.2012.02512.x][research_anderson_magruder_2012]
- Beales, Howard, Richard Craswell, and Steven C. Salop. 1981. "The Efficient Regulation of Consumer Information." *Journal of Law and Economics* 24 (3): 491–539. [https://doi.org/10.1086/466997][research_beales_1980]
- Bentsen. 1985. "Congressional Record." Accessed October 25, 2026. [https://www.congress.gov/congressional-record][ref_bentsen_congressional_record_1985]
- Bishop, Sophie. 2018. "Anxiety, Panic and Self-Optimization: Inequalities and the YouTube Algorithm." *Convergence: The International Journal of Research into New Media Technologies* 24 (1): 69–84. [https://doi.org/10.1177/1354856517736978][research_bishop_2019]
- Bright. 2020. *Coordinated Behavior on Social Media*. [https://scholar.google.com/scholar?q=Coordinated+Behavior+on+Social+Media+Bright+2020][research_bright_et_al_2020]
- *C2PA Coalition for Content Provenance and Authenticity*. n.d. [https://c2pa.org/][ref_c2pa_coalition]
- *C2PA Content Provenance Standard*. n.d. [https://c2pa.org/specifications/specifications/1.4/index.html][ref_c2pa_standard]
- Cao, Qiang, Michael Sirivianos, Xiaowei Yang, and Tiago Pregueiro. 2012. "Aiding the Detection of Fake Accounts in Large Scale Social Online Services." In *9th USENIX Symposium on Networked Systems Design and Implementation (NSDI 12)*. [https://www.usenix.org/conference/nsdi12/technical-sessions/presentation/cao][research_cao_et_al_2012]
- Castillo, Carlos, Debora Donato, Aristides Gionis, Vanessa Murdock, and Fabrizio Silvestri. 2007. "Know Your Neighbors: Web Spam Detection Using the Web Topology." In *Proceedings of the 30th annual international ACM SIGIR conference on Research and development in information retrieval*. ACM. [https://doi.org/10.1145/1277741.1277814][research_castillo_et_al_2007]
- Chen. 2019. *Cross-Platform Identity Linkage*. [https://scholar.google.com/scholar?q=Cross-Platform+Identity+Linkage+Chen+2019][research_chen_et_al_2019]
- Chevalier, Judith A., and Dina Mayzlin. 2006. "The Effect of Word of Mouth on Sales: Online Book Reviews." *Journal of Marketing Research* 43 (3): 345–54. [https://doi.org/10.1509/jmkr.43.3.345][research_chevalier_mayzlin_2006]
- Chintagunta, Pradeep K., Shyam Gopinath, and Sriram Venkataraman. 2010. "The Effects of Online User Reviews on Movie Box Office Performance: Accounting for Sequential Rollout and Aggregation across Local Markets." *Marketing Science* 29 (5): 944–57. [https://doi.org/10.1287/mksc.1100.0572][research_chintagunta_gopinath_venkataraman_2010]
- Cresci, Stefano. 2020. "A Decade of Social Bot Detection." *Communications of the ACM* 63 (10): 72–83. [https://doi.org/10.1145/3409116][research_cresci_2020]
- Cresci, Stefano, Roberto Di Pietro, Marinella Petrocchi, Angelo Spognardi, and Maurizio Tesconi. 2017. "The Paradigm-Shift of Social Spambots: Evidence, Theories, and Tools for the Arms Race." In *Proceedings of the 26th International Conference on World Wide Web Companion - WWW '17 Companion*. ACM Press. [https://doi.org/10.1145/3041021.3055135][research_cresci_et_al_2017]
- D'Ambrosio. 2018. *App Review Manipulation Analysis*. [https://scholar.google.com/scholar?q=App+Review+Manipulation+Analysis+D%27Ambrosio+2018][research_dambrosio_et_al_2018]
- De Micheli and Stroppa. 2013. *Twitter and the Underground Market*. [https://scholar.google.com/scholar?q=Twitter+and+the+Underground+Market+De+Micheli+Stroppa+2013][research_demicheli_stroppa_2013]
- "EU Digital Services Act Regulation 2022/." 2065. [https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2065][ref_eu_dsa_2022]
- European Commission. 2023. "Sweep of Consumer Websites." [https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/sweeps\_en][ref_ec_2023_sweep]
- "Facebook v Power Ventures." 2016. [https://cdn.ca9.uscourts.gov/datastore/opinions/2016/07/12/13-17102.pdf][ref_facebook_v_power_ventures_2016]
- Farooqi. 2017. *Characterizing Key Stakeholders in an Online Black Market*. [https://scholar.google.com/scholar?q=Characterizing+Key+Stakeholders+in+an+Online+Black+Market+Farooqi+2017][research_farooqi_et_al_2017]
- Fei, Geli, Arjun Mukherjee, Bing Liu, Meichun Hsu, Malu Castellanos, and Riddhiman Ghosh. 2013. "Exploiting Burstiness in Reviews for Review Spammer Detection." *Proceedings of the International AAAI Conference on Web and Social Media* 7 (1): 175–84. [https://doi.org/10.1609/icwsm.v7i1.14400][research_fei_et_al_2013]
- Feng. 2012. *Syntactic Stylometry for Deception Detection*. [https://scholar.google.com/scholar?q=Syntactic+Stylometry+for+Deception+Detection+Feng+2012][research_feng_et_al_2012]
- Ferrara, Emilio, Onur Varol, Clayton Davis, Filippo Menczer, and Alessandro Flammini. 2016. "The Rise of Social Bots." *Communications of the ACM* 59 (7): 96–104. [https://doi.org/10.1145/2818717][research_ferrara_et_al_2016]
- FTC. 2011. "Blogger Warning Letters." [https://www.ftc.gov/news-events/news/press-releases/2011/09/ftc-releases-updated-guides-concerning-use-endorsements-and-testimonials-advertising][ref_ftc_2011_blogger_warnings]
- FTC. 2015. "Machinima Settlement." [https://www.ftc.gov/legal-library/browse/cases-proceedings/142-3090-machinima-inc][ref_ftc_machinima_2015]
- FTC. 2016. "Warner Brothers Settlement." [https://www.ftc.gov/legal-library/browse/cases-proceedings/152-3034-warner-bros-home-entertainment-inc-matter][ref_ftc_warner_2016]
- FTC. 2017. "Individual Influencer Warning Letters." [https://www.ftc.gov/news-events/news/press-releases/2017/04/ftc-staff-reminds-influencers-brands-clearly-disclose-relationship][ref_ftc_influencer_letters_2017]
- FTC. 2019a. "Sunday Riley Settlement." [https://www.ftc.gov/legal-library/browse/cases-proceedings/1723065-sunday-riley-modern-skincare-llc][ref_ftc_sunday_riley_2019]
- FTC. 2019b. "UrthBox Settlement." [https://www.ftc.gov/legal-library/browse/cases-proceedings/172-3128-urthbox-inc][ref_ftc_urthbox_2019]
- FTC. 2022. "Roomster Settlement." [https://www.ftc.gov/legal-library/browse/cases-proceedings/2223059-roomster-corp][ref_ftc_roomster_2022]
- FTC. 2023. "Bountiful Company Review Hijacking Settlement." [https://www.ftc.gov/legal-library/browse/cases-proceedings/2023127-bountiful-company][ref_ftc_bountiful_2023]
- FTC. 2024a. "Final Rule on Fake Reviews and Testimonials." [https://www.ftc.gov/legal-library/browse/federal-register-notices/16-cfr-part-465-rule-use-consumer-reviews-testimonials][ref_ftc_final_rule_2024]
- FTC. 2024b. "Impersonation Rule." [https://www.ftc.gov/legal-library/browse/federal-register-notices/rule-impersonation-government-businesses][ref_ftc_impersonation_rule_2024]
- FTC v Amway. 1979. "Decision." [https://www.ftc.gov/legal-library/browse/cases-proceedings/932-3111-amway-corporation][ref_ftc_amway_1979]
- "FTC v Devumi." 2019. [https://www.ftc.gov/legal-library/browse/cases-proceedings/162-3175-devumi-llc-german-calas-jr][ref_ftc_devumi_2019]
- FTC v Herbalife. 2016. "Order." [https://www.ftc.gov/legal-library/browse/cases-proceedings/152-3208-herbalife-international-america-inc][ref_ftc_herbalife_2016]
- FTC v Herbalife. 2022. "Order." [https://www.ftc.gov/legal-library/browse/cases-proceedings/152-3208-herbalife-international-america-inc][ref_ftc_herbalife_2022]
- "FTC's Endorsement Guides: What People Are Asking." 2017. Federal Trade Commission, September 7. [https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking][ref_ftc_endorsement_faq]
- Goodfellow, Ian J., Jonathon Shlens, and Christian Szegedy. 2014. "Explaining and Harnessing Adversarial Examples." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1412.6572][research_goodfellow_shlens_szegedy_2014]
- He, Sherry, Brett Hollenbeck, and Davide Proserpio. 2022. "The Market for Fake Reviews." *Marketing Science* 41 (5): 896–921. [https://doi.org/10.1287/mksc.2022.1353][research_he_hollenbeck_proserpio_2022]
- Jindal, Nitin, and Bing Liu. 2008. "Opinion Spam and Analysis." In *Proceedings of the international conference on Web search and web data mining - WSDM '08*. ACM Press. [https://doi.org/10.1145/1341531.1341560][research_jindal_liu_2008]
- King, Gary, Jennifer Pan, and Margaret E. Roberts. 2017. "How the Chinese Government Fabricates Social Media Posts for Strategic Distraction, Not Engaged Argument." *American Political Science Review* 111 (3): 484–501. [https://doi.org/10.1017/s0003055417000144][research_king_pan_roberts_2017]
- Kirchenbauer, John, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, and Tom Goldstein. 2023. "A Watermark for Large Language Models." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2301.10226][research_kirchenbauer_et_al_2023]
- Kumar, Srijan, Justin Cheng, Jure Leskovec, and V. S. Subrahmanian. 2017. "An Army of Me: Sockpuppets in Online Discussion Communities." In *Proceedings of the 26th International Conference on World Wide Web*. International World Wide Web Conferences Steering Committee. [https://doi.org/10.1145/3038912.3052677][research_kumar_army_2017]
- Kumar, Srijan, and Neil Shah. 2018. "False Information on Web and Social Media: A Survey." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1804.08559][research_kumar_shah_2018]
- Li, Jiwei, Myle Ott, Claire Cardie, and Eduard Hovy. 2014. "Towards a General Rule for Identifying Deceptive Opinion Spam." In *Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*. Association for Computational Linguistics. [https://doi.org/10.3115/v1/p14-1147][research_li_et_al_2014]
- Lim, Ee-Peng, Viet-An Nguyen, Nitin Jindal, Bing Liu, and Hady Wirawan Lauw. 2010. "Detecting Product Review Spammers Using Rating Behaviors." In *Proceedings of the 19th ACM international conference on Information and knowledge management*. ACM. [https://doi.org/10.1145/1871437.1871557][research_lim_et_al_2010]
- Luca, Michael, and Georgios Zervas. 2016. "Fake It till You Make It: Reputation, Competition, and Yelp Review Fraud." *Management Science* 62 (12): 3412–27. [https://doi.org/10.1287/mnsc.2015.2304][research_luca_zervas_2016]
- Marino. 2023. *Effects of Removing Twitter Blue Verification*. [https://scholar.google.com/scholar?q=Effects+of+Removing+Twitter+Blue+Verification+Marino+2023][research_marino_et_al_2023]
- Mayzlin, Dina, Yaniv Dover, and Judith Chevalier. 2014. "Promotional Reviews: An Empirical Investigation of Online Review Manipulation." *American Economic Review* 104 (8): 2421–55. [https://doi.org/10.1257/aer.104.8.2421][research_mayzlin_dover_chevalier_2014]
- McCracken, Grant. 1989. "Who Is the Celebrity Endorser? Cultural Foundations of the Endorsement Process." *Journal of Consumer Research* 16 (3): 310. [https://doi.org/10.1086/209217][research_mccracken_1989]
- Miramirkhani, Najmeh, Oleksii Starov, and Nick Nikiforakis. 2017. "Dial One for Scam: A Large-Scale Analysis of Technical Support Scams." In *Proceedings 2017 Network and Distributed System Security Symposium*. Internet Society. [https://doi.org/10.14722/ndss.2017.23163][research_miramirkhani_et_al_2016]
- Mukherjee. 2013. *What Yelp Fake Review Filter Might Be Doing*. [https://scholar.google.com/scholar?q=What+Yelp+Fake+Review+Filter+Might+Be+Doing+Mukherjee+2013][research_mukherjee_et_al_2013]
- Ntoulas, Alexandros, Marc Najork, Mark Manasse, and Dennis Fetterly. 2006. "Detecting Spam Web Pages through Content Analysis." In *Proceedings of the 15th international conference on World Wide Web*. ACM. [https://doi.org/10.1145/1135777.1135794][research_ntoulas_et_al_2006]
- Ott, Myle, Claire Cardie, and Jeffrey T. Hancock. 2013. "Negative Deceptive Opinion Spam." In *Proceedings of the 2013 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*. [https://aclanthology.org/N13-1053/][research_ott_et_al_2013]
- Ott, Myle, Yejin Choi, Claire Cardie, and Jeffrey T. Hancock. 2011. "Finding Deceptive Opinion Spam by Any Stretch of the Imagination." In *Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies*. [https://aclanthology.org/P11-1032/][research_ott_et_al_2011]
- Pearce, Paul, Vacha Dave, Chris Grier, et al. 2014. "Characterizing Large-Scale Click Fraud in ZeroAccess." In *Proceedings of the 2014 ACM SIGSAC Conference on Computer and Communications Security*. ACM. [https://doi.org/10.1145/2660267.2660369][research_pearce_et_al_2014]
- Petty, Ross D., and J. Craig Andrews. 2008. "Covert Marketing Unmasked: A Legal and Regulatory Guide for Practices That Mask Marketing Messages." *Journal of Public Policy & Marketing* 27 (1): 7–18. [https://doi.org/10.1509/jppm.27.1.7][research_petty_andrews_2008]
- Petty, Richard E., and John T. Cacioppo. 1986. "The Elaboration Likelihood Model of Persuasion." In *Communication and Persuasion*. Springer New York. [https://doi.org/10.1007/978-1-4612-4964-1\_1][research_petty_cacioppo_1986]
- Ratkiewicz, Jacob, Michael Conover, Mark Meiss, Bruno Goncalves, Alessandro Flammini, and Filippo Menczer. 2011. "Detecting and Tracking Political Abuse in Social Media." *Proceedings of the International AAAI Conference on Web and Social Media* 5 (1): 297–304. [https://doi.org/10.1609/icwsm.v5i1.14127][research_ratkiewicz_et_al_2011]
- Rayana, Shebuti, and Leman Akoglu. 2015. "Collective Opinion Spam Detection: Bridging Review Networks and Metadata." In *Proceedings of the 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*. ACM. [https://doi.org/10.1145/2783258.2783370][research_rayana_akoglu_2015]
- Rochet, Jean-Charles, and Jean Tirole. 2003. "Platform Competition in Two-Sided Markets." *Journal of the European Economic Association* 1 (4): 990–1029. [https://doi.org/10.1162/154247603322493212][research_rochet_tirole_2003]
- Rothschild, Michael. 1974. "Searching for the Lowest Price When the Distribution of Prices Is Unknown." *Journal of Political Economy* 82 (4): 689–711. [https://doi.org/10.1086/260229][research_rothschild_1974]
- Rysman, Marc. 2009. "The Economics of Two-Sided Markets." *Journal of Economic Perspectives* 23 (3): 125–43. [https://doi.org/10.1257/jep.23.3.125][research_rysman_2009]
- Sadasivan, Vinu Sankar, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, and Soheil Feizi. 2023. "Can AI-Generated Text Be Reliably Detected?" Preprint, arXiv. [https://doi.org/10.48550/arxiv.2303.11156][research_sadasivan_et_al_2023]
- "SEC v Kardashian." 2022. [https://www.sec.gov/news/press-release/2022-183][ref_sec_kardashian_2022]
- Sohail. 2024. *Detection of Large-Language-Model Generated Reviews*. [https://scholar.google.com/scholar?q=Detection+of+Large-Language-Model+Generated+Reviews+Sohail+2024][research_sohail_et_al_2024]
- Solorio, Thamar, Ragib Hasan, and Mainul Mizan. 2014. "Sockpuppet Detection in Wikipedia: A Corpus of Real-World Deceptive Writing for Linking Identities." In *Proceedings of the Language Resources and Evaluation Conference*. European Language Resources Association (ELRA). [https://doi.org/10.63317/4ea8cv4zth8s][research_solorio_et_al_2014]
- Stigler, George J. 1961. "The Economics of Information." *Journal of Political Economy* 69 (3): 213–25. [https://doi.org/10.1086/258464][research_stigler_1961]
- Stigler, George J. 1971. "The Theory of Economic Regulation." *Bell Journal of Economics and Management Science* 2 (1): 3. [https://doi.org/10.2307/3003160][research_stigler_1971]
- Stringhini, Gianluca, Gang Wang, Manuel Egele, et al. 2013. "Follow the Green: Growth and Dynamics in Twitter Follower Markets." In *Proceedings of the 2013 conference on Internet measurement conference*. ACM. [https://doi.org/10.1145/2504730.2504731][research_stringhini_et_al_2013]
- Trusov, Michael, Randolph E. Bucklin, and Koen Pauwels. 2009. "Effects of Word-of-Mouth versus Traditional Marketing: Findings from an Internet Social Networking Site." *Journal of Marketing* 73 (5): 90–102. [https://doi.org/10.1509/jmkg.73.5.90][research_trusov_bucklin_pauwels_2009]
- *W3C Decentralized Identifiers Standard*. n.d. [https://www.w3.org/TR/did-core/][ref_w3c_did]
- *W3C Verifiable Credentials Standard*. n.d. [https://www.w3.org/TR/vc-data-model/][ref_w3c_verifiable_credentials]
- *W3C Web Authentication WebAuthn Standard*. n.d. [https://www.w3.org/TR/webauthn/][ref_w3c_webauthn]
- Weller. 2019. *Understanding Cross-Platform Sharing and Engagement Pods*. [https://scholar.google.com/scholar?q=Understanding+Cross-Platform+Sharing+and+Engagement+Pods+Weller+2019][research_weller_et_al_2019]
- Xie, Sihong, Guan Wang, Shuyang Lin, and Philip S. Yu. 2012. "Review Spam Detection via Temporal Pattern Discovery." In *Proceedings of the 18th ACM SIGKDD international conference on Knowledge discovery and data mining*. ACM. [https://doi.org/10.1145/2339530.2339662][research_xie_et_al_2012]
- Yang, Kai-Cheng, and Filippo Menczer. 2023. "Anatomy of an AI-Powered Malicious Social Botnet." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2307.16336][research_yang_menczer_2024]
- Yao, Yuanshun, Bimal Viswanath, Jenna Cryan, Haitao Zheng, and Ben Y. Zhao. 2017. "Automated Crowdturfing Attacks and Defenses in Online Review Systems." In *Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security*. ACM. [https://doi.org/10.1145/3133956.3133990][research_yao_et_al_2017]
- Yu, Haifeng, Michael Kaminsky, Phillip B. Gibbons, and Abraham Flaxman. 2006. "SybilGuard: Defending against Sybil Attacks via Social Networks." In *Proceedings of the 2006 conference on Applications, technologies, architectures, and protocols for computer communications*. ACM. [https://doi.org/10.1145/1159913.1159945][research_yu_et_al_2006]
- Zannettou, Savvas, Jeremy Blackburn, Emiliano De Cristofaro, Michael Sirivianos, and Gianluca Stringhini. 2018. "Understanding Web Archiving Services and Their (Mis)Use on Social Media." *Proceedings of the International AAAI Conference on Web and Social Media* 12 (1). [https://doi.org/10.1609/icwsm.v12i1.15018][research_zannettou_et_al_2018]
- Zannettou, Savvas, Tristan Caulfield, Emiliano De Cristofaro, Michael Sirivianos, Gianluca Stringhini, and Jeremy Blackburn. 2019. "Disinformation Warfare: Understanding State-Sponsored Trolls on Twitter and Their Influence on the Web." In *Companion Proceedings of The 2019 World Wide Web Conference*. ACM. [https://doi.org/10.1145/3308560.3316495][research_zannettou_et_al_2019]
- Zellers, Rowan, Ari Holtzman, Hannah Rashkin, et al. 2019. "Defending against Neural Fake News." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1905.12616][research_zellers_et_al_2019]

### Secondary Sources

- Aaker, David A. 1991. *Managing Brand Equity: Capitalizing on the Value of a Brand Name*. Free Press. [https://www.simonandschuster.com/books/Managing-Brand-Equity/David-A-Aaker/9781451602364][book_aaker_1991]
- Abidin, Crystal. 2018. *Internet Celebrity: Understanding Fame Online*. Emerald Publishing Limited. [https://www.emerald.com/insight/publication/doi/10.1108/9781787560789][book_abidin_2018]
- Aral, Sinan. 2020. *The Hype Machine: How Social Media Disrupts Our Elections, Our Economy, and Our Health—and How We Must Adapt*. Currency. [https://us.macmillan.com/books/9780525574514/thehypemachine][book_aral_2020]
- Barnum Autobiography. 1854. *The Project Gutenberg Works of Joseph Lincoln: An Index by Joseph Crosby Lincoln*. [https://www.gutenberg.org/ebooks/29467][ref_barnum_autobiography_1854]
- Berger, Jonah. 2016. *Contagious: Why Things Catch On*. Simon & Schuster. [https://www.simonandschuster.com/books/Contagious/Jonah-Berger/9781451686586][book_berger_2016]
- Bernays, Edward L. 1923. *Crystallizing Public Opinion*. Boni and Liveright. [https://archive.org/details/crystallizingpub00bern][book_bernays_1923]
- Bernays, Edward L. 1928. *Propaganda*. H. Liveright. [https://www.igpublishing.com/product/propaganda/][book_bernays_1928]
- Cialdini, Robert B. 1984. *Influence: How and Why People Agree to Things*. Morrow. [https://www.harpercollins.com/products/influence-new-and-expanded-robert-b-cialdini-phd][book_cialdini_1984]
- Cronin, Anne. 2004. *Advertising Myths: The Strange Half-Lives of Images and Commodities (International Library of Sociology)*. Routledge. [https://www.routledge.com/Advertising-Myths/Cronin/p/book/9780415310086][book_cronin_2004]
- Cutlip, Scott M. 1994. *The Unseen Power: Public Relations, a History*. Erlbaum Associates. [https://www.routledge.com/The-Unseen-Power/Cutlip/p/book/9780805814644][book_cutlip_1994]
- Duffy, Brooke Erin. 2017. *(Not) Getting Paid to Do What You Love: Gender, Social Media, and Aspirational Work*. Yale University Press. [https://yalebooks.yale.edu/book/9780300218176/not-getting-paid-to-do-what-you-love/][book_duffy_2017]
- Ewen. 1996. *PR A Social History of Spin*. [https://www.basicbooks.com/titles/stuart-ewen/pr/9780465061792/][book_ewen_1996]
- Ezell, Allen, and Bear. 2005. *Degree Mills: The Billion-Dollar Industry That Has Sold over a Million Fake Diplomas*. Prometheus Books. [https://www.prometheusbooks.com/9781591024637/degree-mills/][book_ezell_bear_2005]
- Fiske, Susan T., and Shelley E. Taylor. 2013. *Social Cognition: From Brains to Culture*. SAGE Publications, Limited. [https://us.sagepub.com/en-us/nam/social-cognition/book238262][book_fiske_taylor_2013]
- Fitzpatrick, Robert L. 2005. *False Profits: Seeking Spiritual Deliverance in Pyramid Schemes & Mulit-Level Marketing*. Fitzpatrick Management Inc. [https://www.amazon.com/False-Profits-Seeking-Financial-Multi-Level/dp/0964879514][book_fitzpatrick_2005]
- Godin, Seth. 2018. *This Is Marketing*. Portfolio/Penguin. [https://sethgodin.com/books/][book_godin_2018]
- Greif, Avner. 2006. *Institutions and Trade during the Late Medieval Commercial Revolution*. Cambridge University Press. [https://www.cambridge.org/9780521671347][book_greif_2006]
- Katz, Elihu, and Paul Lazarsfeld. 1955. *Personal Influence: The Part Played by People in the Flow of Mass Communications*. Free Press. [https://www.routledge.com/Personal-Influence/Katz-Lazarsfeld/p/book/9781412805070][book_katz_lazarsfeld_1955]
- Kotler, Philip, and Kevin Lane Keller. 2016. *Marketing Management*. Pearson. [https://www.pearson.com/us/higher-education/product/Kotler-Marketing-Management-15th-Edition/9780133856460.html][book_kotler_keller_2016]
- Lippmann, Walter. 1922. *Public Opinion*. George Allen & Unwin Ltd. [https://www.simonandschuster.com/books/Public-Opinion/Walter-Lippmann/9781416573104][book_lippmann_1922]
- Marwick, Alice E. 2013. *Status Update: Celebrity, Publicity, and Branding in the Social Media Age*. Yale University Press. [https://yalebooks.yale.edu/book/9780300209389/status-update/][book_marwick_2013]
- McGarity, Thomas O., and Wagner. 2008. *Bending Science: How Special Interests Corrupt Public Health Research*. Harvard University Press. [https://www.hup.harvard.edu/books/9780674047143][book_mcgarity_wagner_2008]
- Michaels. 2008. *Doubt Is Their Product: How Industry's Assault on Science Threatens Your Health*. Oxford University Press, USA. [https://global.oup.com/academic/product/doubt-is-their-product-9780195300673][book_michaels_2008]
- Nisbett, Richard E., and Ross. 1980. *Human Inference: Strategies and Shortcomings of Social Judgment*. Prentice-Hall. [https://openlibrary.org/works/OL2467050W][book_nisbett_ross_1980]
- Ogilvie, Sheilagh. 2019. *The European Guilds: An Economic Analysis*. Princeton University Press. [https://press.princeton.edu/books/hardcover/9780691137544/the-european-guilds][book_ogilvie_2019]
- Ogilvy, David. 1963. *Confessions of an Advertising Man*. dell publishing co. [https://www.penguinrandomhouse.com/books/300340/confessions-of-an-advertising-man-by-david-ogilvy/][book_ogilvy_1963]
- Oreskes, Naomi, and Conway. 2010. *Merchants of Doubt: How a Handful of Scientists Obscured the Truth on Issues from Tobacco Smoke to Global Warming*. Bloomsbury Publishing Plc. [https://www.bloomsbury.com/us/merchants-of-doubt-9781608193943/][book_oreskes_conway_2010]
- Packard, Vance. 1957. *The Hidden Persuaders*. Longmans, Green. [https://ighland-books.com/hidden-persuaders][book_packard_1957]
- Petty. 2015. *The Codevelopment of Marketing Law and Practice*. [https://global.oup.com/academic/product/the-codevelopment-of-marketing-law-and-practice-9781785365874][book_petty_2015]
- Presbrey, Frank. 1929. *The History and Development of Advertising*. Doubleday. [https://archive.org/details/historyanddevelo00pres][book_presbrey_1929]
- Provost, Foster, and Tom Fawcett. 2013. *Data Science for Business: What You Need to Know about Data Mining and Data-Analytic Thinking*. O'Reilly Media, Incorporated. [https://www.oreilly.com/library/view/data-science-for/9781449374273/][book_provost_fawcett_2013]
- Reeves, Rosser. 1961. *Reality in Advertising*. Knopf. [https://openlibrary.org/works/OL6576145W][book_reeves_1961]
- Rid, Thomas. 2020. *Active Measures*. [https://us.macmillan.com/books/9780374287269/activemeasures][book_rid_2020]
- Roberts, Sarah T. 2019. *Behind the Screen: Content Moderation in the Shadows of Social Media*. Yale University Press. [https://yalebooks.yale.edu/book/9780300235883/behind-the-screen/][book_roberts_2019]
- Silverman, George. 2001. *The Secrets of Word-Of-Mouth Marketing: How to Trigger Exponential Sales through Runaway Word of Mouth*. Amacom Books. [https://openlibrary.org/works/OL8508962W][book_silverman_2001]
- Strasser. 1989. *Satisfaction Guaranteed The Making of the American Mass Market*. [https://www.smithsonianmag.com/books/satisfaction-guaranteed][book_strasser_1989]
- Taylor. 2011. *The Case for and Against Multi-Level Marketing*. [https://scholar.google.com/scholar?q=taylor+2011+case+for+against+multi-level+marketing][book_taylor_2011]
- Trivellato, Francesca. 2009. *The Familiarity of Strangers: The Sephardic Diaspora, Livorno, and Cross-Cultural Trade in the Early Modern Period*. Yale University Press. [https://yalebooks.yale.edu/book/9780300172416/the-familiarity-of-strangers/][book_trivellato_2009]
- Turow, Joseph. 2011. *The Daily You: How the New Advertising Industry Is Defining Your Identity and Your Worth*. Yale University Press. [https://yalebooks.yale.edu/book/9780300188011/the-daily-you/][book_turow_2011]
- Twede and Selke. 2005. *Cartons Crates and Corrugated Board*. [https://www.destechpub.com/product/cartons-crates-corrugated-board][book_twede_selke_2005]
- Tye, Larry. 1998. *The Father of Spin: Edward L. Bernays & the Birth of Public Relations*. Crown Publishers. [https://www.penguinrandomhouse.com/books/153822/the-father-of-spin-by-larry-tye/][book_tye_1998]
- Walker, Edward T. 2014. *Grassroots for Hire: Public Affairs Consultants in American Democracy*. Cambridge University Press. [https://www.cambridge.org/9781107619012][book_walker_2014]
- Woolley, Samuel C., and Philip N. Howard. 2018. *Computational Propaganda: Political Parties, Politicians, and Political Manipulation on Social Media*. Oxford University Press, Incorporated. [https://global.oup.com/academic/product/computational-propaganda-9780190931414][book_woolley_howard_2018]
- Wu, Tim. 2016. *The Attention Merchants: The Epic Scramble to Get inside Our Heads*. Knopf. [https://www.penguinrandomhouse.com/books/232292/the-attention-merchants-by-tim-wu/][book_wu_2016]
- Young, James Harvey. 1961. *The Toadstool Millionaires*. Princeton, New jersey, Princeton University Press. [https://press.princeton.edu/books/paperback/9780691623429/the-toadstool-millionaires][book_young_1961]

### Commercial Sources

- "ACCC v Trivago." 2020. [https://www.accc.gov.au/media-release/trivago-ordered-to-pay-447-million-in-penalties-for-misleading-consumers-over-hotel-room-rates][ref_accc_v_trivago_2020]
- "Amazon v Fake Review Brokers." 2022. [https://www.aboutamazon.com/news/policy-news-views/amazon-continues-legal-action-against-fake-review-brokers][ref_amazon_v_fake_review_brokers_2022]
- "Global Internet Forum to Counter Terrorism GIFCT." n.d. Accessed October 25, 2026. [https://gifct.org/][ref_gifct]
- Google. 2011. "Panda Algorithm Update." [https://developers.google.com/search/blog/2011/02/finding-more-high-quality-sites-in][ref_google_panda_2011]
- Google. 2012. "Penguin Algorithm Update." [https://developers.google.com/search/blog/2012/04/another-step-to-reward-high-quality][ref_google_penguin_2012]
- "Google Search Central Spam Policies." n.d. Accessed October 25, 2026. [https://developers.google.com/search/docs/essentials/spam-policies][ref_google_search_spam_policies]
- "Google Webmaster Guidelines." n.d. Accessed October 25, 2026. [https://developers.google.com/search/docs/essentials][ref_google_webmaster_guidelines]
- "Guidelines for Representing Your Business on Google." n.d. Accessed October 25, 2026. [https://support.google.com/business/answer/3038177][ref_google_business_profile_guidelines]
- "Instagram Community Guidelines Authenticity Section." n.d. Accessed October 25, 2026. [https://help.instagram.com/477434105621119][ref_instagram_authenticity_guidelines]
- "Instagram Verified Badge Documentation." n.d. Accessed October 25, 2026. [https://help.instagram.com/854227311295302][ref_instagram_verified]
- "MegaUpload v Universal." 2011. [https://www.eff.org/cases/megaupload-v-universal][ref_megaupload_universal_2011]
- "Meta Adversarial Threat Report." n.d. Accessed October 25, 2026. [https://about.fb.com/news/tag/adversarial-threat-report/][ref_meta_atr]
- "Meta Coordinated Inauthentic Behavior Policy." n.d. Accessed October 25, 2026. [https://transparency.meta.com/policies/community-standards/inauthentic-behavior/][ref_meta_cib_policy]
- "NY Attorney General v Devumi." 2019. [https://ag.ny.gov/press-release/2019/attorney-general-james-announces-groundbreaking-settlement-devumi-owner-german][ref_ny_ag_devumi_2019]
- OpenAI ChatGPT. 2022. "Introducing ChatGPT." Accessed October 25, 2026. [https://openai.com/index/chatgpt/][ref_openai_chatgpt_2022]
- OpenAI GPT-4. 2023. "GPT-4." Accessed October 25, 2026. [https://openai.com/index/gpt-4-research/][ref_openai_gpt4_2023]
- "Our Approach to Labeling AI-Generated Content and Manipulated Media." 2024. Meta Newsroom, April 5. [https://about.fb.com/news/2024/04/metas-approach-to-labeling-ai-generated-content-and-manipulated-media/][ref_meta_ai_content_labeling]
- "Twitter Verification Legacy Program Documentation." n.d. Accessed October 25, 2026. [https://help.x.com/en/managing-your-account/legacy-verification-policy][ref_twitter_verification_legacy]
- "Verification Badges on Channels: YouTube Help." n.d. Accessed October 25, 2026. [https://support.google.com/youtube/answer/3046484][ref_youtube_verification]
- "X Blue Paid Verification." n.d. Accessed October 25, 2026. [https://help.x.com/en/using-x/x-blue][ref_x_blue]
- "X Platform Manipulation and Spam Policy." n.d. Accessed October 25, 2026. [https://help.x.com/en/rules-and-policies/platform-manipulation][ref_x_platform_manipulation_policy]
- "YouTube View-Count Manipulation Policy." n.d. Accessed October 25, 2026. [https://support.google.com/youtube/answer/2801973][ref_youtube_view_manipulation_policy]

### General Sources

- "Amazon Community Guidelines." n.d. Accessed October 25, 2026. [https://www.amazon.com/gp/help/customer/display.html?nodeId=GLHXEX85MENUE4XF][ref_amazon_community_guidelines]
- "Amazon Reviews Dataset." n.d. Accessed October 25, 2026. [https://amazon-reviews-2023.github.io/][ref_amazon_reviews_dataset]
- "Anti-Cheating and Certification Fraud Coalition." n.d. Accessed October 25, 2026. [https://www.credentialingexcellence.org/][ref_accfc]
- Apple Inc. n.d. "App Review Guidelines." Apple Developer. Accessed October 25, 2026. [https://developer.apple.com/app-store/review/guidelines/][ref_apple_app_store_review_guidelines]
- Beuk Boekhandel. 2013. "Dutch Fake Review Case." [https://uitspraken.rechtspraak.nl/details?id=ECLI:NL:RBAMS:2013:8117][ref_beuk_boekhandel_2013]
- Bilton. 2014. "New York Times Investigation of Purchased Twitter Followers." [https://www.nytimes.com/2014/04/06/fashion/social-media-followers-for-sale.html][ref_bilton_2014_nyt_followers]
- Bing. 2004. "Astroturf Blogging Incident." [https://www.wired.com/2004/12/tricks-and-tips-for-blogging/][ref_bing_2004_astroturf]
- Boerman. 2018. "Sponsored Content Disclosure Effects." [https://www.tandfonline.com/doi/full/10.1080/00913367.2017.1408087][research_boerman_et_al_2018]
- "Bot Repository Indiana OSoMe." n.d. Accessed October 25, 2026. [https://botometer.osome.iu.edu/bot-repository/][ref_bot_repository]
- Bradshaw, Bailey, and Howard. 2021. "DemTech \| Industrialized Disinformation: 2020 Global Inventory of Organized Social Media Manipulation." Accessed October 25, 2026. [https://demtech.oii.ox.ac.uk/research/posts/industrialized-disinformation/][research_bradshaw_bailey_howard_2021]
- Bradshaw and Howard. 2019. "DemTech \| the Global Disinformation Order: 2019 Global Inventory of Organised Social Media Manipulation." Accessed October 25, 2026. [https://demtech.oii.ox.ac.uk/research/posts/the-global-disinformation-order-2019-global-inventory-of-organised-social-media-manipulation/][research_bradshaw_howard_2019]
- "Canadian Competition Bureau v Amazon Fake Reviews." n.d. Accessed October 25, 2026. [https://competition-bureau.canada.ca/en/deceptive-marketing-practices/types-deceptive-marketing-practices/testimonials-and-endorsements][ref_canada_amazon]
- Chaiken. 1980. "Heuristic Systematic Model of Persuasion." [https://psycnet.apa.org/record/1981-05463-001][research_chaiken_1980]
- "Content Authenticity Initiative." n.d. Accessed October 25, 2026. [https://contentauthenticity.org/][ref_content_authenticity_initiative]
- "Cresci-2017 Genuine and Spambot Dataset." n.d. Accessed October 25, 2026. [https://botometer.osome.iu.edu/bot-repository/datasets.html][ref_cresci_2015_dataset]
- "Cross-Platform Sharing Dataset." n.d. Accessed October 25, 2026. [https://cross-platform-sharing.github.io/][ref_cross_platform_sharing_dataset]
- Cushing. 2013. "Wired Bangladesh Click Farm Investigation." [https://www.wired.com/2013/08/click-farms/][ref_cushing_2013_click_farm]
- "Cutts Google Webmaster Central Blog Archives." n.d. Accessed October 25, 2026. [https://www.mattcutts.com/blog/][ref_cutts_google_blog]
- Danezis and Mittal. 2009. "SybilInfer." [https://www.ndss-symposium.org/wp-content/uploads/2017/09/sybilinfer-detecting-sybil-nodes-using-social-networks.pdf][research_danezis_mittal_2009]
- "Deceptive Opinion Spam Corpus Myle Ott." n.d. Myle Ott. Accessed October 25, 2026. [https://myleott.com/op-spam.html][ref_ott_deceptive_corpus]
- "Developer Policy Center." n.d. Accessed October 25, 2026. [https://play.google.com/about/developer-content-policy/][ref_google_play_developer_policy]
- DiResta, Renee, Kris Shaffer, Becky Ruppel, et al. 2019. "The Tactics & Tropes of the Internet Research Agency." DigitalCommons@University of Nebraska - Lincoln. Accessed October 25, 2026. [https://digitalcommons.unl.edu/senatedocs/2/][research_diresta_et_al_2019]
- Ellis Ott. 2018. "Atlantic Instagram Pods." [https://www.theatlantic.com/technology/archive/2018/06/instagram-pods-explained/564237/][ref_ellis_ott_2018_pods]
- "Fakespot Consumer Reports." n.d. Accessed October 25, 2026. [https://www.fakespot.com/][ref_fakespot_consumer_reports]
- Fang. 2013. "Koch Network Investigation." [https://www.thenation.com/article/archive/koch-brothers-secret-bank/][ref_fang_2013_koch]
- "FIDO User Authentication Specifications." 2018. *FIDO Alliance*, November 14. [https://fidoalliance.org/specifications/][ref_fido_alliance]
- FTC v Nutrilite Products. 1951. "Order." [https://scholar.google.com/scholar?q=ftc+nutrilite+products+1951][ref_ftc_nutrilite_1951]
- Gyongyi and Garcia-Molina. 2005. "Web Spam Taxonomy." [http://ilpubs.stanford.edu:8090/771/][research_gyongyi_garciamolina_2005]
- Gyongyi Garcia-Molina Pedersen. 2004. "Combating Web Spam with TrustRank." [https://ilpubs.stanford.edu:8090/645/][ref_gyongyi_2004_trustrank_paper]
- Hoffman. 2017. "Sponsored Content Regulation." [https://scholar.google.com/scholar?q=hoffman+2017+sponsored+content+regulation][research_hoffman_2017]
- "IAB Digital Ad Fraud Report." n.d. Accessed October 25, 2026. [https://www.iab.com/insights/topics/ad-fraud/][ref_iab_ad_fraud_report]
- "Italian AGCM Booking.com Fake Reviews Action." n.d. Accessed October 25, 2026. [https://en.agcm.it/en/agcm-media/press-releases/][ref_italy_agcm_booking]
- Kanich. 2011. "No Plan Survives Contact Cybercrime Measurement." [https://www.usenix.org/legacy/event/leet11/tech/full\_papers/Kanich.pdf][research_kanich_et_al_2011]
- Klonick. 2018. "The New Governors." [https://harvardlawreview.org/2018/04/the-new-governors-the-people-rules-and-processes-governing-online-speech/][research_klonick_2018]
- Krebs. 2013. "Expired Domain Reputation Transfer." [https://krebsonsecurity.com/2013/09/data-broker-giants-hacked-by-id-theft-service/][ref_krebs_2013_expired_domains]
- Kumar. 2017. "Understanding Rating Distributions." [https://cs.stanford.edu/~srijan/pubs/rev2-wsdm18.pdf][research_kumar_et_al_2017]
- Levick and Slavo. 2015. "Front Organization Documentation." [https://web.archive.org/web/2015/https://levick.com/][ref_levick_slavo_2015]
- "LinkedIn ID Verification." n.d. Accessed October 25, 2026. [https://www.linkedin.com/help/linkedin/answer/a1359065][ref_linkedin_verification]
- Luca. 2016. "Reviews Reputation and Revenue Yelp." [https://www.hbs.edu/faculty/Pages/item.aspx?num=41233][research_luca_2016]
- Miller. 2004. "Working Families for Wal-Mart Documentation." [https://www.walmartwatch.com/battlemart/working\_families/][ref_miller_2004_walmart]
- Motoyama. 2011. "Dirty Jobs Freelance Labor in Web Service Abuse." [https://www.usenix.org/legacy/event/sec11/tech/full\_papers/Motoyama.pdf][research_motoyama_et_al_2011]
- "MRC Media Rating Council Viewability Standards." n.d. Accessed October 25, 2026. [https://mediaratingcouncil.org/standards][ref_mrc_viewability_standards]
- Mueller Report. 2019. "Volume One." [https://www.justice.gov/archives/sco/file/1373816/download][ref_mueller_report_2019]
- "Nielsen Trust in Advertising Global Report." n.d. Accessed October 25, 2026. [https://www.nielsen.com/insights/2021/trust-in-advertising-2021/][ref_nielsen_trust_advertising]
- Page Brin Motwani Winograd. 1999. "PageRank Extended Technical Report." [http://ilpubs.stanford.edu:8090/422/][research_page_brin_motwani_winograd_1999]
- "PMI Professional Certification Fraud Detection." n.d. Accessed October 25, 2026. [https://www.pmi.org/certifications/ethics][ref_pmi_fraud]
- "PRSA Code of Ethics." 1906. www. Accessed October 25, 2026. [https://www.prsa.org/about/ethics/][ref_ivy_lee_declaration_1906]
- Simon. 1971. "Designing Organizations for an Information-Rich World." [https://digitalcollections.library.cmu.edu/awweb/awarchive?type=file&item=33748][research_simon_1971]
- Sony PlayStation Portable. 2006. "Fake Blog Case." [https://www.wired.com/2006/12/sonys-fake-blog/][ref_sony_psp_2006]
- "Source Watch Front Organizations Catalog." n.d. Accessed October 25, 2026. [https://www.sourcewatch.org/index.php/SourceWatch][ref_source_watch_front]
- "Trustpilot Transparency Report." n.d. Accessed October 25, 2026. [https://uk.business.trustpilot.com/reviews/build-trusted-brand/trustpilot-transparency-report][ref_trustpilot_transparency]
- UK, CMA, Facebook, et al. 2022. "\[Title not identified\]." Accessed October 25, 2026. [https://www.gov.uk/cma-cases/online-reviews-facebook-and-google][ref_uk_cma_facebook_google_2022]
- Wang. 2012. "Serf and Turf Crowdturfing for Fun and Profit." [https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/wang][research_wang_et_al_2012]
- White Ops Methbot. 2016. "Report." [https://www.humansecurity.com/learn/blog/anatomy-of-methbot][ref_white_ops_methbot_2016]
- "Whole Foods Mackey Rahodeb Case." 2007. [https://www.wsj.com/articles/SB118466504114020015][ref_whole_foods_rahodeb_2007]
- "X Transparency Report." n.d. Accessed October 25, 2026. [https://transparency.x.com/][ref_x_transparency_report]
- "Yelp Content Guidelines." n.d. Accessed October 25, 2026. [https://www.yelp-support.com/article/Yelp-Content-Guidelines][ref_yelp_content_guidelines]
- "YelpCHI Dataset – ODDS." n.d. Accessed October 25, 2026. [https://odds.cs.stonybrook.edu/yelpchi-dataset/][ref_yelpchi_dataset]
- Zheng. 2011. "Detecting Sockpuppets in Deceptive Opinion Spam." [https://aclanthology.org/N12-1121/][research_zheng_et_al_2011]

### Related Posts

- Sechter, Brendan. 2026. "Virtual Reputation Manipulation: Theory and Analytical Framework." *Brendan A R Sechter's Development Blog*, January 22. [https://sgeos.github.io/economics/technology/sociology/2026/01/22/virtual\_reputation\_manipulation\_theory.html][related_post_a277_theory]

[book_aaker_1991]: https://www.simonandschuster.com/books/Managing-Brand-Equity/David-A-Aaker/9781451602364
[book_abidin_2018]: https://www.emerald.com/insight/publication/doi/10.1108/9781787560789
[book_aral_2020]: https://us.macmillan.com/books/9780525574514/thehypemachine
[book_berger_2016]: https://www.simonandschuster.com/books/Contagious/Jonah-Berger/9781451686586
[book_bernays_1923]: https://archive.org/details/crystallizingpub00bern
[book_bernays_1928]: https://www.igpublishing.com/product/propaganda/
[book_cialdini_1984]: https://www.harpercollins.com/products/influence-new-and-expanded-robert-b-cialdini-phd
[book_cronin_2004]: https://www.routledge.com/Advertising-Myths/Cronin/p/book/9780415310086
[book_cutlip_1994]: https://www.routledge.com/The-Unseen-Power/Cutlip/p/book/9780805814644
[book_duffy_2017]: https://yalebooks.yale.edu/book/9780300218176/not-getting-paid-to-do-what-you-love/
[book_ewen_1996]: https://www.basicbooks.com/titles/stuart-ewen/pr/9780465061792/
[book_ezell_bear_2005]: https://www.prometheusbooks.com/9781591024637/degree-mills/
[book_fiske_taylor_2013]: https://us.sagepub.com/en-us/nam/social-cognition/book238262
[book_fitzpatrick_2005]: https://www.amazon.com/False-Profits-Seeking-Financial-Multi-Level/dp/0964879514
[book_godin_2018]: https://sethgodin.com/books/
[book_greif_2006]: https://www.cambridge.org/9780521671347
[book_katz_lazarsfeld_1955]: https://www.routledge.com/Personal-Influence/Katz-Lazarsfeld/p/book/9781412805070
[book_kotler_keller_2016]: https://www.pearson.com/us/higher-education/product/Kotler-Marketing-Management-15th-Edition/9780133856460.html
[book_lippmann_1922]: https://www.simonandschuster.com/books/Public-Opinion/Walter-Lippmann/9781416573104
[book_marwick_2013]: https://yalebooks.yale.edu/book/9780300209389/status-update/
[book_mcgarity_wagner_2008]: https://www.hup.harvard.edu/books/9780674047143
[book_michaels_2008]: https://global.oup.com/academic/product/doubt-is-their-product-9780195300673
[book_nisbett_ross_1980]: https://openlibrary.org/works/OL2467050W
[book_ogilvie_2019]: https://press.princeton.edu/books/hardcover/9780691137544/the-european-guilds
[book_ogilvy_1963]: https://www.penguinrandomhouse.com/books/300340/confessions-of-an-advertising-man-by-david-ogilvy/
[book_oreskes_conway_2010]: https://www.bloomsbury.com/us/merchants-of-doubt-9781608193943/
[book_packard_1957]: https://ighland-books.com/hidden-persuaders
[book_petty_2015]: https://global.oup.com/academic/product/the-codevelopment-of-marketing-law-and-practice-9781785365874
[book_presbrey_1929]: https://archive.org/details/historyanddevelo00pres
[book_provost_fawcett_2013]: https://www.oreilly.com/library/view/data-science-for/9781449374273/
[book_reeves_1961]: https://openlibrary.org/works/OL6576145W
[book_rid_2020]: https://us.macmillan.com/books/9780374287269/activemeasures
[book_roberts_2019]: https://yalebooks.yale.edu/book/9780300235883/behind-the-screen/
[book_silverman_2001]: https://openlibrary.org/works/OL8508962W
[book_strasser_1989]: https://www.smithsonianmag.com/books/satisfaction-guaranteed
[book_taylor_2011]: https://scholar.google.com/scholar?q=taylor+2011+case+for+against+multi-level+marketing
[book_trivellato_2009]: https://yalebooks.yale.edu/book/9780300172416/the-familiarity-of-strangers/
[book_turow_2011]: https://yalebooks.yale.edu/book/9780300188011/the-daily-you/
[book_twede_selke_2005]: https://www.destechpub.com/product/cartons-crates-corrugated-board
[book_tye_1998]: https://www.penguinrandomhouse.com/books/153822/the-father-of-spin-by-larry-tye/
[book_walker_2014]: https://www.cambridge.org/9781107619012
[book_woolley_howard_2018]: https://global.oup.com/academic/product/computational-propaganda-9780190931414
[book_wu_2016]: https://www.penguinrandomhouse.com/books/232292/the-attention-merchants-by-tim-wu/
[book_young_1961]: https://press.princeton.edu/books/paperback/9780691623429/the-toadstool-millionaires
[ref_accc_v_trivago_2020]: https://www.accc.gov.au/media-release/trivago-ordered-to-pay-447-million-in-penalties-for-misleading-consumers-over-hotel-room-rates
[ref_accfc]: https://www.credentialingexcellence.org/
[ref_amazon_community_guidelines]: https://www.amazon.com/gp/help/customer/display.html?nodeId=GLHXEX85MENUE4XF
[ref_amazon_reviews_dataset]: https://amazon-reviews-2023.github.io/
[ref_amazon_v_fake_review_brokers_2022]: https://www.aboutamazon.com/news/policy-news-views/amazon-continues-legal-action-against-fake-review-brokers
[ref_apple_app_store_review_guidelines]: https://developer.apple.com/app-store/review/guidelines/
[ref_barnum_autobiography_1854]: https://www.gutenberg.org/ebooks/29467
[ref_bentsen_congressional_record_1985]: https://www.congress.gov/congressional-record
[ref_beuk_boekhandel_2013]: https://uitspraken.rechtspraak.nl/details?id=ECLI:NL:RBAMS:2013:8117
[ref_bilton_2014_nyt_followers]: https://www.nytimes.com/2014/04/06/fashion/social-media-followers-for-sale.html
[ref_bing_2004_astroturf]: https://www.wired.com/2004/12/tricks-and-tips-for-blogging/
[ref_bot_repository]: https://botometer.osome.iu.edu/bot-repository/
[ref_c2pa_coalition]: https://c2pa.org/
[ref_c2pa_standard]: https://c2pa.org/specifications/specifications/1.4/index.html
[ref_canada_amazon]: https://competition-bureau.canada.ca/en/deceptive-marketing-practices/types-deceptive-marketing-practices/testimonials-and-endorsements
[ref_content_authenticity_initiative]: https://contentauthenticity.org/
[ref_cresci_2015_dataset]: https://botometer.osome.iu.edu/bot-repository/datasets.html
[ref_cresci_2017_dataset]: https://botometer.osome.iu.edu/bot-repository/datasets.html
[ref_cross_platform_sharing_dataset]: https://cross-platform-sharing.github.io/
[ref_cushing_2013_click_farm]: https://www.wired.com/2013/08/click-farms/
[ref_cutts_google_blog]: https://www.mattcutts.com/blog/
[ref_ec_2023_sweep]: https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/sweeps_en
[ref_ellis_ott_2018_pods]: https://www.theatlantic.com/technology/archive/2018/06/instagram-pods-explained/564237/
[ref_eu_dsa_2022]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2065
[ref_facebook_v_power_ventures_2016]: https://cdn.ca9.uscourts.gov/datastore/opinions/2016/07/12/13-17102.pdf
[ref_fakespot_consumer_reports]: https://www.fakespot.com/
[ref_fang_2013_koch]: https://www.thenation.com/article/archive/koch-brothers-secret-bank/
[ref_fido_alliance]: https://fidoalliance.org/specifications/
[ref_ftc_2011_blogger_warnings]: https://www.ftc.gov/news-events/news/press-releases/2011/09/ftc-releases-updated-guides-concerning-use-endorsements-and-testimonials-advertising
[ref_ftc_amway_1979]: https://www.ftc.gov/legal-library/browse/cases-proceedings/932-3111-amway-corporation
[ref_ftc_bountiful_2023]: https://www.ftc.gov/legal-library/browse/cases-proceedings/2023127-bountiful-company
[ref_ftc_devumi_2019]: https://www.ftc.gov/legal-library/browse/cases-proceedings/162-3175-devumi-llc-german-calas-jr
[ref_ftc_endorsement_faq]: https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking
[ref_ftc_endorsement_guides_16_cfr_255]: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255
[ref_ftc_final_rule_2024]: https://www.ftc.gov/legal-library/browse/federal-register-notices/16-cfr-part-465-rule-use-consumer-reviews-testimonials
[ref_ftc_herbalife_2016]: https://www.ftc.gov/legal-library/browse/cases-proceedings/152-3208-herbalife-international-america-inc
[ref_ftc_herbalife_2022]: https://www.ftc.gov/legal-library/browse/cases-proceedings/152-3208-herbalife-international-america-inc
[ref_ftc_impersonation_rule_2024]: https://www.ftc.gov/legal-library/browse/federal-register-notices/rule-impersonation-government-businesses
[ref_ftc_influencer_letters_2017]: https://www.ftc.gov/news-events/news/press-releases/2017/04/ftc-staff-reminds-influencers-brands-clearly-disclose-relationship
[ref_ftc_machinima_2015]: https://www.ftc.gov/legal-library/browse/cases-proceedings/142-3090-machinima-inc
[ref_ftc_nutrilite_1951]: https://scholar.google.com/scholar?q=ftc+nutrilite+products+1951
[ref_ftc_roomster_2022]: https://www.ftc.gov/legal-library/browse/cases-proceedings/2223059-roomster-corp
[ref_ftc_sunday_riley_2019]: https://www.ftc.gov/legal-library/browse/cases-proceedings/1723065-sunday-riley-modern-skincare-llc
[ref_ftc_urthbox_2019]: https://www.ftc.gov/legal-library/browse/cases-proceedings/172-3128-urthbox-inc
[ref_ftc_warner_2016]: https://www.ftc.gov/legal-library/browse/cases-proceedings/152-3034-warner-bros-home-entertainment-inc-matter
[ref_gifct]: https://gifct.org/
[ref_google_business_profile_guidelines]: https://support.google.com/business/answer/3038177
[ref_google_panda_2011]: https://developers.google.com/search/blog/2011/02/finding-more-high-quality-sites-in
[ref_google_penguin_2012]: https://developers.google.com/search/blog/2012/04/another-step-to-reward-high-quality
[ref_google_play_developer_policy]: https://play.google.com/about/developer-content-policy/
[ref_google_search_spam_policies]: https://developers.google.com/search/docs/essentials/spam-policies
[ref_google_webmaster_guidelines]: https://developers.google.com/search/docs/essentials
[ref_gyongyi_2004_trustrank_paper]: https://ilpubs.stanford.edu:8090/645/
[ref_iab_ad_fraud_report]: https://www.iab.com/insights/topics/ad-fraud/
[ref_instagram_authenticity_guidelines]: https://help.instagram.com/477434105621119
[ref_instagram_verified]: https://help.instagram.com/854227311295302
[ref_italy_agcm_booking]: https://en.agcm.it/en/agcm-media/press-releases/
[ref_ivy_lee_declaration_1906]: https://www.prsa.org/about/ethics/
[ref_krebs_2013_expired_domains]: https://krebsonsecurity.com/2013/09/data-broker-giants-hacked-by-id-theft-service/
[ref_levick_slavo_2015]: https://web.archive.org/web/2015/https://levick.com/
[ref_linkedin_verification]: https://www.linkedin.com/help/linkedin/answer/a1359065
[ref_megaupload_universal_2011]: https://www.eff.org/cases/megaupload-v-universal
[ref_meta_ai_content_labeling]: https://about.fb.com/news/2024/04/metas-approach-to-labeling-ai-generated-content-and-manipulated-media/
[ref_meta_atr]: https://about.fb.com/news/tag/adversarial-threat-report/
[ref_meta_cib_policy]: https://transparency.meta.com/policies/community-standards/inauthentic-behavior/
[ref_miller_2004_walmart]: https://www.walmartwatch.com/battlemart/working_families/
[ref_mrc_viewability_standards]: https://mediaratingcouncil.org/standards
[ref_mueller_report_2019]: https://www.justice.gov/archives/sco/file/1373816/download
[ref_nielsen_trust_advertising]: https://www.nielsen.com/insights/2021/trust-in-advertising-2021/
[ref_ny_ag_devumi_2019]: https://ag.ny.gov/press-release/2019/attorney-general-james-announces-groundbreaking-settlement-devumi-owner-german
[ref_openai_chatgpt_2022]: https://openai.com/index/chatgpt/
[ref_openai_gpt4_2023]: https://openai.com/index/gpt-4-research/
[ref_ott_deceptive_corpus]: https://myleott.com/op-spam.html
[ref_pmi_fraud]: https://www.pmi.org/certifications/ethics
[ref_sec_kardashian_2022]: https://www.sec.gov/news/press-release/2022-183
[ref_sony_psp_2006]: https://www.wired.com/2006/12/sonys-fake-blog/
[ref_source_watch_front]: https://www.sourcewatch.org/index.php/SourceWatch
[ref_trustpilot_transparency]: https://uk.business.trustpilot.com/reviews/build-trusted-brand/trustpilot-transparency-report
[ref_twitter_verification_legacy]: https://help.x.com/en/managing-your-account/legacy-verification-policy
[ref_uk_cma_facebook_google_2022]: https://www.gov.uk/cma-cases/online-reviews-facebook-and-google
[ref_w3c_did]: https://www.w3.org/TR/did-core/
[ref_w3c_verifiable_credentials]: https://www.w3.org/TR/vc-data-model/
[ref_w3c_webauthn]: https://www.w3.org/TR/webauthn/
[ref_white_ops_methbot_2016]: https://www.humansecurity.com/learn/blog/anatomy-of-methbot
[ref_whole_foods_rahodeb_2007]: https://www.wsj.com/articles/SB118466504114020015
[ref_x_blue]: https://help.x.com/en/using-x/x-blue
[ref_x_platform_manipulation_policy]: https://help.x.com/en/rules-and-policies/platform-manipulation
[ref_x_transparency_report]: https://transparency.x.com/
[ref_yelp_content_guidelines]: https://www.yelp-support.com/article/Yelp-Content-Guidelines
[ref_yelpchi_dataset]: https://odds.cs.stonybrook.edu/yelpchi-dataset/
[ref_youtube_verification]: https://support.google.com/youtube/answer/3046484
[ref_youtube_view_manipulation_policy]: https://support.google.com/youtube/answer/2801973
[related_post_a277_theory]: {% post_url 2026-01-22-virtual_reputation_manipulation_theory %}
[research_ali_et_al_2017]: https://scholar.google.com/scholar?q=Same+Same+but+Different+Search+Advertising+Ali+2017
[research_alvisi_et_al_2013]: https://doi.org/10.1109/sp.2013.33
[research_anderson_magruder_2012]: https://doi.org/10.1111/j.1468-0297.2012.02512.x
[research_beales_1980]: https://doi.org/10.1086/466997
[research_bishop_2019]: https://doi.org/10.1177/1354856517736978
[research_boerman_et_al_2018]: https://www.tandfonline.com/doi/full/10.1080/00913367.2017.1408087
[research_bradshaw_bailey_howard_2021]: https://demtech.oii.ox.ac.uk/research/posts/industrialized-disinformation/
[research_bradshaw_howard_2019]: https://demtech.oii.ox.ac.uk/research/posts/the-global-disinformation-order-2019-global-inventory-of-organised-social-media-manipulation/
[research_bright_et_al_2020]: https://scholar.google.com/scholar?q=Coordinated+Behavior+on+Social+Media+Bright+2020
[research_cao_et_al_2012]: https://www.usenix.org/conference/nsdi12/technical-sessions/presentation/cao
[research_castillo_et_al_2007]: https://doi.org/10.1145/1277741.1277814
[research_chaiken_1980]: https://psycnet.apa.org/record/1981-05463-001
[research_chandola_banerjee_kumar_2009]: https://doi.org/10.1145/1541880.1541882
[research_chen_et_al_2019]: https://scholar.google.com/scholar?q=Cross-Platform+Identity+Linkage+Chen+2019
[research_chevalier_mayzlin_2006]: https://doi.org/10.1509/jmkr.43.3.345
[research_chintagunta_gopinath_venkataraman_2010]: https://doi.org/10.1287/mksc.1100.0572
[research_cho_et_al_2011]: https://doi.org/10.1007/s10551-011-0950-6
[research_cresci_2020]: https://doi.org/10.1145/3409116
[research_cresci_et_al_2015]: https://doi.org/10.1016/j.dss.2015.09.003
[research_cresci_et_al_2017]: https://doi.org/10.1145/3041021.3055135
[research_dambrosio_et_al_2018]: https://scholar.google.com/scholar?q=App+Review+Manipulation+Analysis+D%27Ambrosio+2018
[research_danezis_mittal_2009]: https://www.ndss-symposium.org/wp-content/uploads/2017/09/sybilinfer-detecting-sybil-nodes-using-social-networks.pdf
[research_demicheli_stroppa_2013]: https://scholar.google.com/scholar?q=Twitter+and+the+Underground+Market+De+Micheli+Stroppa+2013
[research_diamond_1971]: https://doi.org/10.1016/0022-0531(71)90013-5
[research_diresta_et_al_2019]: https://digitalcommons.unl.edu/senatedocs/2/
[research_douceur_2002]: https://doi.org/10.1007/3-540-45748-8_24
[research_farooqi_et_al_2017]: https://scholar.google.com/scholar?q=Characterizing+Key+Stakeholders+in+an+Online+Black+Market+Farooqi+2017
[research_fawcett_2006]: https://doi.org/10.1016/j.patrec.2005.10.010
[research_fei_et_al_2013]: https://doi.org/10.1609/icwsm.v7i1.14400
[research_feng_et_al_2012]: https://scholar.google.com/scholar?q=Syntactic+Stylometry+for+Deception+Detection+Feng+2012
[research_ferrara_et_al_2016]: https://doi.org/10.1145/2818717
[research_goodfellow_shlens_szegedy_2014]: https://doi.org/10.48550/arxiv.1412.6572
[research_gyongyi_garciamolina_2005]: http://ilpubs.stanford.edu:8090/771/
[research_he_hollenbeck_proserpio_2022]: https://doi.org/10.1287/mksc.2022.1353
[research_hoffman_2017]: https://scholar.google.com/scholar?q=hoffman+2017+sponsored+content+regulation
[research_jindal_liu_2008]: https://doi.org/10.1145/1341531.1341560
[research_kanich_et_al_2011]: https://www.usenix.org/legacy/event/leet11/tech/full_papers/Kanich.pdf
[research_king_pan_roberts_2017]: https://doi.org/10.1017/s0003055417000144
[research_kirchenbauer_et_al_2023]: https://doi.org/10.48550/arxiv.2301.10226
[research_klonick_2018]: https://harvardlawreview.org/2018/04/the-new-governors-the-people-rules-and-processes-governing-online-speech/
[research_kumar_army_2017]: https://doi.org/10.1145/3038912.3052677
[research_kumar_et_al_2017]: https://cs.stanford.edu/~srijan/pubs/rev2-wsdm18.pdf
[research_kumar_shah_2018]: https://doi.org/10.48550/arxiv.1804.08559
[research_li_et_al_2014]: https://doi.org/10.3115/v1/p14-1147
[research_lim_et_al_2010]: https://doi.org/10.1145/1871437.1871557
[research_luca_2016]: https://www.hbs.edu/faculty/Pages/item.aspx?num=41233
[research_luca_zervas_2016]: https://doi.org/10.1287/mnsc.2015.2304
[research_malbon_2013]: https://doi.org/10.1007/s10603-012-9216-7
[research_marino_et_al_2023]: https://scholar.google.com/scholar?q=Effects+of+Removing+Twitter+Blue+Verification+Marino+2023
[research_mayzlin_dover_chevalier_2014]: https://doi.org/10.1257/aer.104.8.2421
[research_mccracken_1989]: https://doi.org/10.1086/209217
[research_miramirkhani_et_al_2016]: https://doi.org/10.14722/ndss.2017.23163
[research_motoyama_et_al_2011]: https://www.usenix.org/legacy/event/sec11/tech/full_papers/Motoyama.pdf
[research_mukherjee_et_al_2013]: https://scholar.google.com/scholar?q=What+Yelp+Fake+Review+Filter+Might+Be+Doing+Mukherjee+2013
[research_ntoulas_et_al_2006]: https://doi.org/10.1145/1135777.1135794
[research_ott_et_al_2011]: https://aclanthology.org/P11-1032/
[research_ott_et_al_2013]: https://aclanthology.org/N13-1053/
[research_page_brin_1998]: https://doi.org/10.1016/s0169-7552(98)00110-x
[research_page_brin_motwani_winograd_1999]: http://ilpubs.stanford.edu:8090/422/
[research_papakyriakopoulos_et_al_2020]: https://doi.org/10.1016/j.osnem.2019.100058
[research_pearce_et_al_2014]: https://doi.org/10.1145/2660267.2660369
[research_petty_andrews_2008]: https://doi.org/10.1509/jppm.27.1.7
[research_petty_cacioppo_1986]: https://doi.org/10.1007/978-1-4612-4964-1_1
[research_ratkiewicz_et_al_2011]: https://doi.org/10.1609/icwsm.v5i1.14127
[research_rayana_akoglu_2015]: https://doi.org/10.1145/2783258.2783370
[research_rochet_tirole_2003]: https://doi.org/10.1162/154247603322493212
[research_rothschild_1974]: https://doi.org/10.1086/260229
[research_rysman_2009]: https://doi.org/10.1257/jep.23.3.125
[research_sadasivan_et_al_2023]: https://doi.org/10.48550/arxiv.2303.11156
[research_simon_1971]: https://digitalcollections.library.cmu.edu/awweb/awarchive?type=file&item=33748
[research_sohail_et_al_2024]: https://scholar.google.com/scholar?q=Detection+of+Large-Language-Model+Generated+Reviews+Sohail+2024
[research_solorio_et_al_2014]: https://doi.org/10.63317/4ea8cv4zth8s
[research_starbird_2019]: https://doi.org/10.1038/d41586-019-02235-x
[research_stigler_1961]: https://doi.org/10.1086/258464
[research_stigler_1971]: https://doi.org/10.2307/3003160
[research_stringhini_et_al_2013]: https://doi.org/10.1145/2504730.2504731
[research_trusov_bucklin_pauwels_2009]: https://doi.org/10.1509/jmkg.73.5.90
[research_tsikerdekis_zeadally_2014]: https://doi.org/10.1109/tifs.2014.2332820
[research_wang_et_al_2011]: https://doi.org/10.1109/icdm.2011.124
[research_wang_et_al_2012]: https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/wang
[research_weerkamp_derijke_2012]: https://doi.org/10.1007/s10791-011-9182-8
[research_weller_et_al_2019]: https://scholar.google.com/scholar?q=Understanding+Cross-Platform+Sharing+and+Engagement+Pods+Weller+2019
[research_wu_et_al_2020]: https://doi.org/10.1016/j.dss.2020.113280
[research_xie_et_al_2012]: https://doi.org/10.1145/2339530.2339662
[research_yang_et_al_2020]: https://doi.org/10.1002/hbe2.115
[research_yang_menczer_2024]: https://doi.org/10.48550/arxiv.2307.16336
[research_yao_et_al_2017]: https://doi.org/10.1145/3133956.3133990
[research_yu_et_al_2006]: https://doi.org/10.1145/1159913.1159945
[research_yu_et_al_2008]: https://doi.org/10.1109/sp.2008.13
[research_zannettou_et_al_2018]: https://doi.org/10.1609/icwsm.v12i1.15018
[research_zannettou_et_al_2019]: https://doi.org/10.1145/3308560.3316495
[research_zellers_et_al_2019]: https://doi.org/10.48550/arxiv.1905.12616
[research_zheng_et_al_2011]: https://aclanthology.org/N12-1121/
