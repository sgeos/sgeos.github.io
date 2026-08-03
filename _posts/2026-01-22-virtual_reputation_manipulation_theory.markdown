---
layout: post
mathjax: true
comments: true
title:  "Virtual Reputation Manipulation: Theory and Analytical Framework"
date:   2026-01-22 00:00:00 +0000
categories: economics technology sociology
series: virtual_reputation_manipulation
series_title: Virtual Reputation Manipulation
series_index: 1
---

<!-- A277 -->
<script>console.log("A277");</script>

This article opens a four-article miniseries that treats virtual reputation manipulation as a first-class object of analysis in the contemporary attention economy. The miniseries treats the manipulation of digitally mediated reputation as a prevalent structural condition of participation in most contemporary online enclaves rather than as an aberration from an otherwise trustworthy baseline. This opening article establishes the analytical framework the miniseries applies, characterizes reputation as an economic good with formal properties, formalizes the manipulation equilibrium that emerges from the incentive structure the underlying platforms create, addresses the empirical puzzle that a minority of participants nevertheless achieve organic reputation under manipulation-saturated conditions, introduces the six-axis analytical framework the subsequent articles apply, and surveys the pre-digital historical antecedents that the contemporary manipulation ecosystem inherited from public relations, advertising, and propaganda practice. Subsequent articles treat the techniques of self-promotion oriented reputation manipulation, the techniques of competitor attack oriented reputation manipulation, and the detection, countermeasure, and organic establishment landscape that has emerged in response.

## The Reputation Manipulation Mapping Problem

The mapping problem for a comprehensive treatment of virtual reputation manipulation is the question of which technical, economic, legal, and sociological factors produced the manipulation-saturated equilibrium that characterizes most contemporary online reputation systems, and which factors permit a minority of participants to establish reputation organically despite that equilibrium. The problem admits several formalizations depending on the analytical tradition consulted. The economic tradition from [Akerlof 1970][research_akerlof_1970] on the market for lemons through [Spence 1973][research_spence_1973] on job market signaling, [Klein and Leffler 1981][research_klein_leffler_1981] on brand names as market discipline, [Kreps and Wilson 1982][research_kreps_wilson_1982] on reputation and imperfect information, [Shapiro 1983][research_shapiro_1983] on premiums for high quality products, [Milgrom and Roberts 1986][research_milgrom_roberts_1986] on price and advertising signals, and [Fudenberg and Levine 1992][research_fudenberg_levine_1992] on maintaining a reputation when strategies are imperfectly observed treats reputation as a costly signal transmitted through repeated interactions under information asymmetry. The sociological tradition from [Goffman 1959][book_goffman_1959] The Presentation of Self in Everyday Life through [Bourdieu 1984][book_bourdieu_1984] Distinction, [Coleman 1990][book_coleman_1990] Foundations of Social Theory, [Fukuyama 1995][book_fukuyama_1995] Trust, [Putnam 2000][book_putnam_2000] Bowling Alone, and [Podolny 2005][book_podolny_2005] Status Signals treats reputation as an accumulated social attribute that operates through symbolic capital and network effects. The contemporary treatment to digital reputation systems runs through [Resnick et al 2000][research_resnick_et_al_2000] Reputation Systems, [Dellarocas 2003][research_dellarocas_2003] The Digitization of Word of Mouth, [Bolton Katok Ockenfels 2004][research_bolton_katok_ockenfels_2004] How Effective Are Electronic Reputation Mechanisms, [Ba and Pavlou 2002][research_ba_pavlou_2002] Evidence of the Effect of Trust Building Technology, [Tirole 1996][research_tirole_1996] A Theory of Collective Reputations, [Mailath and Samuelson 2006][book_mailath_samuelson_2006] Repeated Games and Reputations, [Fombrun 1996][book_fombrun_1996] Reputation, and [Origgi 2018][book_origgi_2018] Reputation What It Is and Why It Matters. The present miniseries adopts the economic analytical stance while retaining the sociological tradition's attention to the symbolic and network effects the reputation economy produces.

The mapping problem admits several formalizations depending on the level of analysis adopted. At the level of the individual actor, reputation manipulation shapes patterns of self-presentation, purchase-intent generation, competitive positioning, and audience formation. At the level of the platform, reputation manipulation shapes the design of ranking algorithms, the deployment of detection and enforcement systems, the terms of service, and the two-sided market dynamics between reputation producers and reputation consumers. At the level of the market, reputation manipulation shapes the equilibrium quality of information available to consumers, the survival probabilities of firms competing on reputation, and the returns to authentic quality investment. At the level of the legal-institutional structure, reputation manipulation intersects with consumer protection law, unfair competition doctrine, intermediary liability, and speech regulation. The miniseries treats each level explicitly.

The general form of the causal-mapping problem can be stated compactly as follows. Let $R_i(t)$ denote the observed reputation score of actor $i$ at time $t$, let $q_i(t)$ denote the underlying quality of the good or service the actor offers, and let $m_i(t)$ denote the manipulation intensity the actor deploys. The mapping problem seeks the functional form

$$R_i(t) = F(q_i(t), m_i(t), P_t, D_t, A_t) + \varepsilon_i(t)$$

where $P_t$ denotes the platform architecture and ranking rules at time $t$, $D_t$ denotes the detection and enforcement regime, $A_t$ denotes the audience composition and attention allocation, and $\varepsilon_i(t)$ denotes the unexplained residual. The isolated manipulation contribution to observed reputation can be characterized counterfactually as

$$\Delta R_i^{\text{manip}}(t) = F(q_i(t), m_i(t), P_t, D_t, A_t) - F(q_i(t), 0, P_t, D_t, A_t)$$

with the counterfactual holding underlying quality, platform, detection regime, and audience fixed and setting manipulation intensity to zero. Under an approximately additive decomposition, observed reputation admits the further decomposition

$$R_i(t) = R_i^{q}(t) + R_i^{\text{manip}}(t) + R_i^{\text{platform}}(t) + \varepsilon_i(t)$$

where the first term captures the authentic-quality contribution, the second the manipulation contribution, and the third the platform-architecture contribution independent of the actor's own action. The aggregate manipulation intensity at the market level is the vector sum

$$M(t) = \sum_{i=1}^{N} m_i(t), \quad \bar{m}(t) = M(t)/N$$

with $\bar{m}$ the average per-actor manipulation intensity that indexes the market equilibrium regime. The tractability of the mapping problem depends on the ability to identify the manipulation contribution to $R_i$ separately from the underlying-quality contribution and from the platform and audience effects. The identification problem is considerable because $q_i$ is generally unobservable to the analyst, and the miniseries treats the identification strategies each empirical setting admits.

The mapping problem faces several distinctive methodological challenges beyond those common to industrial-organization analysis. First, the manipulation techniques themselves evolve continuously in response to platform countermeasures, so any technique catalog is a snapshot rather than a stable inventory. Second, the platforms have private information about manipulation prevalence that is not published in scholarly literature and that the platforms have commercial incentives to understate. Third, the actors who manipulate reputations have obvious incentives to conceal both the fact and the technique of manipulation, so the empirical record is skewed toward the manipulation attempts that were detected or disclosed. Fourth, the boundary between manipulation and legitimate promotion is contested and shifts across platforms and legal regimes. Fifth, the reputation economy interpenetrates with the political information environment through overlapping technique and infrastructure, so a treatment focused on commercial reputation cannot cleanly bracket political disinformation. The miniseries treats each challenge explicitly and cites the corrective scholarship as it becomes relevant.

## Methodological Commitments

The miniseries commits explicitly to several methodological positions that shape the analytical treatment across the four articles. These commitments are stated here in the framing article so that the reader can evaluate subsequent claims against the interpretive stance the miniseries adopts.

The first commitment is descriptive-analytical framing rather than operational instruction. The miniseries characterizes documented manipulation techniques for the purpose of analyzing their prevalence, detection signatures, market effects, and legal exposure. The miniseries does not provide operational guidance intended to enable a reader to conduct a manipulation campaign, and where a technique admits both analytical description and operational specification the treatment stops at the analytical description. Detection signatures, platform countermeasures, and enforcement case histories receive treatment proportional to the technique itself so that the material remains useful to detection engineers, platform integrity teams, and legal practitioners rather than to would-be manipulators.

The second commitment is first-class treatment of both self-promotion and competitor-attack manipulation. The miniseries does not treat one class as the default form of manipulation with the other as a variant. The two classes exhibit distinct technique inventories, distinct detection signatures, distinct legal exposures, and distinct market effects, and each receives comparable analytical attention. Article two treats self-promotion techniques. Article three treats competitor-attack techniques. The closing article treats the detection and organic-establishment landscape that responds to both.

The third commitment is the manipulation-as-baseline framing. The miniseries treats reputation manipulation as the empirical default in most contemporary online reputation systems rather than as an aberration from an otherwise trustworthy baseline. The framing rests on the accumulated empirical evidence that fake review prevalence in major consumer platforms exceeds ten percent by conservative estimate and exceeds thirty percent in several categories, that coordinated inauthentic behavior campaigns operate at scale across the major social platforms, that reputation-manipulation service markets have been documented in multiple jurisdictions with public price lists and service catalogs, and that the platforms themselves acknowledge the prevalence in transparency reporting. The empirical base is developed in [Luca and Zervas 2016][research_luca_zervas_2016] Fake It Till You Make It, [Mayzlin Dover Chevalier 2014][research_mayzlin_dover_chevalier_2014] Promotional Reviews, [He Hollenbeck Proserpio 2022][research_he_hollenbeck_proserpio_2022] The Market for Fake Reviews, [Wu et al 2020][research_wu_et_al_2020] Fake Online Reviews, [Ferrara et al 2016][research_ferrara_et_al_2016] The Rise of Social Bots, [Vosoughi Roy Aral 2018][research_vosoughi_roy_aral_2018] The Spread of True and False News Online, and [DiResta et al 2019][research_diresta_et_al_2019] The Tactics and Tropes of the Internet Research Agency, among other primary sources cited across the miniseries.

The fourth commitment is contested-claim marking. The miniseries identifies the claims that remain contested within contemporary scholarship (the precise prevalence rates in each platform category, the causal impact of technique classes on purchase behavior, the effectiveness of detection technologies, the marginal deterrent effect of legal enforcement) and cites the primary sources on each side rather than presenting one position as settled. Where the scholarly literature includes competing estimates, the miniseries reports the range and identifies the methodological basis for the divergence. The prevalence estimator for a random sample of $n$ candidate items is

$$\hat{p}_{\text{manip}} = \frac{1}{n} \sum_{i=1}^{n} \mathbb{1}[y_i = \text{manip}], \quad \text{Var}(\hat{p}_{\text{manip}}) = \frac{\hat{p}_{\text{manip}}(1 - \hat{p}_{\text{manip}})}{n}$$

with $y_i$ the classified item label. Where multiple studies report prevalence estimates for the same phenomenon under differing methodologies, the miniseries adopts the inverse-variance-weighted meta-analytic combined estimate

$$\hat{p}^{\text{meta}} = \frac{\sum_k w_k \hat{p}_k}{\sum_k w_k}, \quad w_k = \frac{1}{\sigma_k^2}$$

with $\sigma_k^2$ the reported variance of the $k$-th study estimate. When study-specific variance is not reported, the miniseries reports the study-specific point estimates with the methodological caveats attached rather than combining them.

The fifth commitment is primary-source anchoring. The miniseries cites primary sources for each substantive claim, with preference for peer-reviewed empirical studies, court filings and judgments, regulatory enforcement documents, and platform transparency reports. Where a claim rests on interpretation of primary data (transaction datasets, review corpora, network graphs, enforcement records), the miniseries cites the dataset and the analytical tradition that reads it in the way the article reports.

The sixth commitment is temporal indexing. The miniseries is a snapshot of the manipulation ecosystem and its scholarly treatment as of the mid 2020s. The technique inventory, prevalence estimates, detection technologies, platform policies, and legal frameworks will continue to evolve. The reader should treat the miniseries as a contemporaneous record of the state of the manipulation ecosystem rather than as a permanent authoritative treatment of the underlying dynamics.

The seventh commitment is terminological transparency. The miniseries uses terms for phenomena and practices that are contested and evolving. The terminology adopted appears in the Terminological Note section below.

## Reputation as an Economic Good

Reputation is treated in the miniseries as an economic good with formal properties that distinguish it from ordinary consumption goods and that shape both the incentive to manipulate and the equilibrium effects of manipulation. Reputation is a credence good in the sense of [Darby and Karni 1973][research_darby_karni_1973] The Free Competition and Optimal Amount of Fraud in that its true value is difficult for the consumer to verify even after consumption. Reputation is a positional good in the sense of [Hirsch 1976][book_hirsch_1976] Social Limits to Growth in that its value depends on relative ranking rather than absolute magnitude. Reputation is a signal in the sense of [Spence 1973][research_spence_1973] in that its function is to convey unobservable underlying attributes through observable proxies whose production cost differs systematically across producer types. Reputation is a form of intangible capital that admits investment, depreciation, and destruction, treated in [Fombrun 1996][book_fombrun_1996] and in the corporate reputation literature that followed.

The formal properties of reputation as an economic good admit compact statement as follows. Let the actor $i$ have an unobservable type $\theta_i \in \Theta$ and let the reputation signal $s_i$ be a function of type, effort, and observation noise,

$$s_i = h(\theta_i, e_i) + \eta_i$$

where $e_i$ denotes reputation-directed effort (which subsumes both authentic quality investment and manipulation investment) and $\eta_i$ denotes idiosyncratic noise in the observation channel. The consumer of the signal forms a posterior about $\theta_i$ via Bayes rule,

$$\Pr(\theta_i = \theta \mid s_i) = \frac{\Pr(s_i \mid \theta_i = \theta) \, \pi(\theta)}{\int_\Theta \Pr(s_i \mid \theta_i = \theta') \, \pi(\theta') \, d\theta'}$$

with prior $\pi$ over types. The posterior determines the consumer's willingness to transact. The consumer's willingness to pay conditional on the observed signal is the posterior-expected utility differential

$$\text{WTP}(s_i) = \int_\Theta u(\theta, q(\theta)) \, \Pr(\theta \mid s_i) \, d\theta - u_{\text{outside}}$$

with $u_{\text{outside}}$ the utility from the outside option. The manipulator's problem is to raise the posterior above the true type-conditional posterior at minimum cost. Manipulation cost typically exhibits convex dependence on manipulation intensity,

$$c(m) = c_0 \, m^{\alpha}, \quad \alpha > 1$$

with $c_0$ a scale parameter and $\alpha$ the convexity exponent that varies by technique class and by the platform's detection intensity.

The information-asymmetry structure was formalized in [Akerlof 1970][research_akerlof_1970] for the used-car market and generalizes to any market in which sellers hold private information about quality and buyers cannot verify quality before purchase. The Akerlof lemons equilibrium characterizes the case where information asymmetry drives high-quality sellers out of the market. In the reputation-mediated variant, the equilibrium separates the market by reputation tier, with high-reputation sellers commanding a premium and low-reputation sellers commanding a discount, and the premium equals the expected quality differential

$$\Delta p = E[q \mid \text{high reputation}] - E[q \mid \text{low reputation}]$$

adjusted for the risk premium associated with the residual uncertainty. Manipulation compresses $\Delta p$ by allowing low-quality sellers to purchase high-reputation status, which reduces the returns to authentic quality investment and shifts the market equilibrium toward the lemons outcome.

The signaling framework of [Spence 1973][research_spence_1973] characterizes the separating equilibrium in which the reputation signal reliably distinguishes types. The single-crossing condition that supports the separating equilibrium is that the marginal cost of producing the signal differs systematically across types,

$$\frac{\partial C(s, \theta_H)}{\partial s} < \frac{\partial C(s, \theta_L)}{\partial s}$$

where $\theta_H$ denotes the high-quality type and $\theta_L$ denotes the low-quality type. Reputation manipulation reduces the marginal cost differential by allowing low-quality types to produce reputation signals at costs comparable to high-quality types, which collapses the separating equilibrium into a pooling equilibrium in which the reputation signal carries no information.

The Klein and Leffler framework in [Klein and Leffler 1981][research_klein_leffler_1981] treats reputation as a bond that firms post against future quality reduction. The bond value equals the present discounted value of the reputation premium the firm captures in future transactions,

$$B = \sum_{t=1}^{\infty} \delta^t \, (p_t^{\text{rep}} - p_t^{\text{no rep}})$$

where $\delta$ is the discount factor and $p_t^{\text{rep}}$ and $p_t^{\text{no rep}}$ denote the price the firm captures with and without the reputation. The firm chooses to maintain quality when the bond value exceeds the one-shot gain from quality reduction. Reputation manipulation collapses the bond value by allowing firms to purchase reputation without investing in quality, which eliminates the bond mechanism and shifts the equilibrium toward quality reduction across the market.

The mechanism-design perspective in [Myerson 1981][research_myerson_1981] Optimal Auction Design and the broader literature developed through [Milgrom 2004][book_milgrom_2004] Putting Auction Theory to Work treats reputation-system architecture as an incentive-compatibility problem in which the platform's design must elicit truthful reputation reporting from actors whose private information cannot be verified directly. The information-design extension in [Kamenica and Gentzkow 2011][research_kamenica_gentzkow_2011] Bayesian Persuasion and the treatment in [Bergemann and Morris 2019][research_bergemann_morris_2019] Information Design generalize the mechanism-design framework to settings where the designer chooses not only the incentive structure but also the information the receiver observes, which captures the platform's control over reputation-signal presentation.

Reputation as an intangible capital stock admits a continuous-time law-of-motion characterization

$$\frac{dR_i}{dt} = -\gamma R_i(t) + \sigma_i^{\text{authentic}}(t) + \sigma_i^{\text{manip}}(t) - \delta_i^{\text{detect}}(t)$$

with $\gamma$ the reputation-decay rate reflecting audience memory attrition, $\sigma_i^{\text{authentic}}$ the authentic-signal inflow from transactions or attribute updates, $\sigma_i^{\text{manip}}$ the manipulation inflow, and $\delta_i^{\text{detect}}$ the detection-triggered reputation loss. The reputation asset value is the present-discounted stream of rents the reputation stock generates,

$$V_R^i = \int_0^{\infty} e^{-rt} \, \pi_i(R_i(t)) \, dt$$

with $r$ the actor's discount rate and $\pi_i(R_i)$ the flow return the reputation stock produces. The steady-state reputation stock under constant inflows and constant detection satisfies

$$R_i^{\text{ss}} = \frac{\sigma_i^{\text{authentic}} + \sigma_i^{\text{manip}} - \delta_i^{\text{detect}}}{\gamma}$$

with the manipulation contribution $\sigma_i^{\text{manip}} - \delta_i^{\text{detect}}$ vanishing when detection perfectly offsets injection and positive when detection lags injection.

## Cross-Disciplinary Framings

The reputation-manipulation phenomenon admits characterization from several disciplinary traditions beyond the economics-of-reputation literature. The miniseries treats each tradition as offering distinct analytical leverage on the same underlying phenomenon while maintaining the economics-of-reputation framework as the primary organizing structure.

The sociological framing traces from [Goffman 1959][book_goffman_1959] The Presentation of Self in Everyday Life and [Goffman 1967][book_goffman_1967] Interaction Ritual through the symbolic-interactionist and impression-management traditions. Reputation is treated as a social accomplishment rather than an economic good, produced through the coordinated performance of identity and status across audiences. The [Bourdieu 1984][book_bourdieu_1984] Distinction framework treats reputation as a component of symbolic capital that can be converted to and from economic, cultural, and social capital, with the conversion rates determined by field-specific rules. The [Coleman 1990][book_coleman_1990] Foundations of Social Theory and [Putnam 2000][book_putnam_2000] Bowling Alone treatments treat reputation as an emergent property of social-network structure that shapes the availability of resources, information, and cooperation. The [Fukuyama 1995][book_fukuyama_1995] Trust extension treats aggregate reputation quality as a determinant of a society's economic capacity. The [Granovetter 1985][research_granovetter_1985] Economic Action and Social Structure and [Uzzi 1997][research_uzzi_1997] Social Structure and Competition treatments trace the embeddedness of economic transactions in social networks and the reputation dynamics that follow. The [Mauss 1925][book_mauss_1925] The Gift and [Douglas 1966][book_douglas_1966] Purity and Danger treatments provide the deep-anthropological framing of reputation as an accumulated symbolic obligation and as a marker of social boundary maintenance. The [Weber 1922][book_weber_1922] Economy and Society treatment provides the classical-sociological framing of authority, legitimacy, and reputation as interrelated forms of social power. The [Elias 1939][book_elias_1939] The Civilizing Process treats reputation and status as shaped by the long-run dynamics of social-differentiation and impulse-regulation processes. The sociological framing complements the economic framing by treating the audience and community structure of reputation reception rather than the incentive structure of reputation production.

The behavioral-economics and cognitive-psychology framing traces from [Tversky and Kahneman 1974][research_tversky_kahneman_1974] Judgment Under Uncertainty through [Kahneman 2011][book_kahneman_2011] Thinking Fast and Slow. The framing identifies systematic cognitive biases that shape consumer response to reputation signals, including availability heuristic (recency-weighted evaluation), representativeness heuristic (stereotype-based evaluation), anchoring (initial-value dependence), and social proof (majority-following behavior). The [Cialdini 1984][book_cialdini_1984] Influence treatment consolidates the persuasion-adjacent biases that manipulation practices exploit, including reciprocity, commitment and consistency, social proof, authority, liking, and scarcity. The [Thaler and Sunstein 2008][book_thaler_sunstein_2008] Nudge extension develops the choice-architecture perspective on how the presentation of reputation signals shapes consumer decision-making even in the absence of manipulation. The [Ariely 2008][book_ariely_2008] Predictably Irrational treatment provides the popular synthesis. The behavioral-economics framing complements the economic framing by treating consumer response to reputation signals as systematically deviating from rational-Bayesian benchmark, which magnifies the effect of manipulation for a given signal-injection intensity.

The computer-science and information-retrieval framing traces from the [Page and Brin 1998][research_page_brin_1998] PageRank algorithm through the reputation-and-trust systems literature. The framing treats reputation as a computed property of the link and interaction graph, with algorithmic ranking functions determining the equilibrium reputation distribution. The [Kleinberg 1999][research_kleinberg_1999] HITS algorithm develops the parallel hub-and-authority framework. The [Watts and Strogatz 1998][research_watts_strogatz_1998] Collective Dynamics of Small-World Networks provides the network-topology framework that shapes reputation propagation. The [Kleinberg 2000][research_kleinberg_2000] Navigation in a Small World treatment provides the search-path framework. The [Adamic and Adar 2003][research_adamic_adar_2003] Friends and Neighbors on the Web treatment provides the link-prediction framework relevant to reputation-signal fabrication detection. The [Golbeck 2008][book_golbeck_2008] Computing with Social Trust consolidates the trust-computation subfield. The computer-science framing complements the economic framing by treating reputation as an artifact of a specific algorithmic architecture rather than as a scalar economic quantity, which surfaces the platform-design choices that shape the manipulation equilibrium.

The legal-scholarship framing traces from the First Amendment tradition through the digital-intermediary-liability tradition. The [Balkin 2018][research_balkin_2018] Free Speech is a Triangle treatment develops the framework of platforms as private governors mediating between users and states. The [Klonick 2018][research_klonick_2018] The New Governors treats the internal governance structure of major platforms. The [Douek 2021][research_douek_2021] Governing Online Speech treats the emerging comparative platform-governance jurisprudence. The [Suzor 2019][book_suzor_2019] Lawless treats the accountability gaps in platform governance. The [Persily 2017][research_persily_2017] Can Democracy Survive the Internet treats the democratic-institution consequences of platform-mediated information environments. The [Solove 2007][book_solove_2007] The Future of Reputation treats the legal implications of digital reputation persistence. The [Nissenbaum 2010][book_nissenbaum_2010] Privacy in Context provides the contextual-integrity framework that has become influential in reputation and privacy law. The legal framing complements the economic framing by treating the constraints on manipulation and the constraints on platform enforcement as products of specific legal-institutional configurations rather than as exogenous constants.

The critical-media-studies framing traces from [Marwick 2013][book_marwick_2013] Status Update through [Marwick and Lewis 2017][research_marwick_lewis_2017] Media Manipulation and Disinformation Online. The framing treats reputation manipulation as embedded in a broader political-economy of digital media in which platform business models, algorithmic amplification, and audience formation combine to produce systematic manipulation-amenable conditions. The [Wardle and Derakhshan 2017][research_wardle_derakhshan_2017] Information Disorder treatment provides the taxonomic framework for misinformation, disinformation, and malinformation that overlaps considerably with the reputation-manipulation taxonomy. The [Roberts 2019][book_roberts_2019] Behind the Screen treats the labor conditions of content moderation that shapes platform-side enforcement capacity. The [Farkas and Schou 2019][book_farkas_schou_2019] Post-Truth Fake News and Democracy treats the epistemological consequences of the manipulation-saturated information environment. The [Zuckerman 2021][book_zuckerman_2021] Mistrust treats the trust erosion produced by manipulation and the potential remedies. The [Aral 2020][book_aral_2020] The Hype Machine consolidates the empirical evidence on social-media effects on political and commercial outcomes. The critical-media-studies framing complements the economic framing by treating the manipulation-saturated equilibrium as a systemic outcome of platform political economy rather than as an aggregation of individual manipulation choices.

The decentralized-systems framing traces from the [Nakamoto 2008][ref_nakamoto_2008_bitcoin] Bitcoin whitepaper through the subsequent Web3 and blockchain-reputation literature. The framing treats reputation as potentially portable across platforms through cryptographic attestation and treats the platform-level manipulation equilibrium as one of several possible architectural equilibria rather than as inherent to digital reputation. The [Buterin 2014][ref_buterin_2014_ethereum] Ethereum whitepaper introduced the smart-contract programmability that supports on-chain reputation systems. The [Weyl Ohlhaver Buterin 2022][research_weyl_ohlhaver_buterin_2022] Decentralized Society treatment proposes the soulbound-token framework for non-transferable on-chain reputation. The empirical assessment in [Zargham and Nabben 2022][research_zargham_nabben_2022] Aligning Intent and Behavior in Web3 tempers the aspirational claims with observed manipulation patterns in decentralized reputation systems. The decentralized-systems framing complements the platform-centric framing by treating the platform's mediating role as historically contingent and identifying alternative architectural configurations that admit different manipulation equilibria.

## The Attention Economy Substrate

Reputation manipulation operates within the attention economy substrate that [Simon 1971][research_simon_1971] Designing Organizations for an Information-Rich World characterized as the defining condition of the contemporary information environment. The Simon insight is that information consumes attention and that attention is the scarce resource in an information-abundant environment. The scholarly treatment developed through [Davenport and Beck 2001][book_davenport_beck_2001] The Attention Economy and reached the popular audience through [Wu 2016][book_wu_2016] The Attention Merchants, [Zuboff 2019][book_zuboff_2019] The Age of Surveillance Capitalism, and [Vaidhyanathan 2018][book_vaidhyanathan_2018] Antisocial Media. The contemporary treatment of attention allocation on platforms runs through [Bucher 2018][book_bucher_2018] If Then, [Gillespie 2018][book_gillespie_2018] Custodians of the Internet, and [Srnicek 2017][book_srnicek_2017] Platform Capitalism.

The formal structure of the attention economy substrate can be characterized as follows. The total attention $A$ available across a platform in a given time interval is bounded above by the population size times the per-user attention budget,

$$A_{\text{total}} = N \cdot \bar{a}$$

with $N$ the active user count and $\bar{a}$ the average attention allocation per user. The allocation of $A_{\text{total}}$ across content, sellers, or reputational entities $i \in \{1, 2, \ldots, K\}$ produces the attention distribution $\{a_i\}_{i=1}^K$ satisfying $\sum_i a_i = A_{\text{total}}$. The empirical distribution of attention across content on major platforms is highly skewed, with the [Zipf 1949][book_zipf_1949] Human Behavior and the Principle of Least Effort framework and the [Pareto 1897][research_pareto_1897] Cours d'Economie Politique framework each providing power-law characterizations. The observed rank-size distribution typically satisfies

$$a_{(r)} \sim r^{-\alpha}, \quad \alpha \in [0.5, 2]$$

with $a_{(r)}$ the attention received by the entity at rank $r$ and $\alpha$ the power-law exponent that varies by platform and content category. The [Adamic and Huberman 2000][research_adamic_huberman_2000] Power-Law Distribution of the World Wide Web and subsequent empirical work document the exponent range. The concentration of attention across the entity set is summarized by the Herfindahl-Hirschman index

$$\text{HHI}_{\text{attention}} = \sum_{i=1}^{K} \left(\frac{a_i}{A_{\text{total}}}\right)^2 \in [1/K, 1]$$

with the lower bound reached under uniform allocation and the upper bound reached under complete concentration on a single entity. An equivalent characterization via the Shannon entropy of the attention distribution is

$$H_{\text{attention}} = -\sum_{i=1}^{K} \frac{a_i}{A_{\text{total}}} \log \frac{a_i}{A_{\text{total}}} \in [0, \log K]$$

with high entropy indicating dispersed attention and low entropy indicating concentrated attention. Major platforms typically exhibit $\text{HHI}_{\text{attention}}$ well above $1/K$ and $H_{\text{attention}}$ well below $\log K$, reflecting the power-law concentration the empirical evidence documents.

The platform mediates the attention allocation through algorithmic ranking. The ranking function

$$\rho_i = g(R_i, e_i, c_i, u_i)$$

maps reputation $R_i$, engagement history $e_i$, content features $c_i$, and user-level personalization features $u_i$ to a ranking score. The attention allocated to entity $i$ is a decreasing function of the entity's rank position

$$a_i = \phi(\text{rank}(\rho_i))$$

with $\phi$ typically exponentially decaying or power-law decaying in rank. The empirical evidence on the rank-attention decay for search results is documented in [Craswell et al 2008][research_craswell_et_al_2008] An Experimental Comparison of Click Position-Bias Models and subsequent work. The click-through decay by rank position observed on major search platforms satisfies approximately

$$\text{CTR}(r) \approx c_0 \cdot r^{-\beta}, \quad \beta \in [1, 2]$$

with $c_0$ the top-position click-through rate. The ranking function creates the incentive to manipulate reputation, since a marginal increase in $R_i$ produces a superlinear increase in attention through the rank position change. The chain-rule expansion of the reputation-to-attention conversion is

$$\frac{\partial a_i}{\partial R_i} = \phi'(\text{rank}(\rho_i)) \cdot \frac{\partial \text{rank}}{\partial \rho_i} \cdot \frac{\partial \rho_i}{\partial R_i}$$

with the first factor typically negative and large in magnitude near the top ranks, the second factor negative and discrete, and the third factor positive and set by the ranking function's reputation weighting. The composite conversion produces the superlinear return-to-reputation that drives the incentive to manipulate.

The two-sided platform structure treated in [Rochet and Tirole 2003][research_rochet_tirole_2003] Platform Competition in Two-Sided Markets and [Rysman 2009][research_rysman_2009] The Economics of Two-Sided Markets shapes the platform's incentive to police manipulation. The platform maximizes joint surplus across both sides of the market, and manipulation degrades the consumer side while benefiting the producer side. The platform's objective admits the composite form

$$W_{\text{platform}}(D, \mathbf{m}) = \psi_C \, \text{CS}(D, \mathbf{m}) + \psi_P \, \text{PS}(D, \mathbf{m}) + \psi_R \, \text{Rev}(D, \mathbf{m}) - C(D)$$

with $\text{CS}$ the consumer surplus, $\text{PS}$ the producer surplus, $\text{Rev}$ the platform revenue net of the surplus terms, $C(D)$ the detection cost, and $\psi_C$, $\psi_P$, $\psi_R$ the platform's marginal valuations. The platform's optimal enforcement intensity balances the loss of consumer trust against the loss of producer participation and against the direct costs of detection and enforcement. The empirical variation in platform enforcement intensity across categories reflects the platform's estimate of the trust-participation tradeoff.

## The Manipulation Equilibrium

The manipulation equilibrium refers to the stable configuration of manipulation prevalence, detection intensity, and market outcomes that emerges from the strategic interaction among producers, consumers, platforms, and enforcement authorities. The equilibrium can be characterized game-theoretically through a repeated interaction model in which each producer chooses a manipulation intensity, the platform chooses a detection intensity, and the consumer forms rational expectations about the manipulation-adjusted signal.

The producer's problem in the single-shot form is to choose manipulation intensity $m_i$ to maximize

$$\pi_i(m_i, m_{-i}) = R_i(m_i, m_{-i}) \cdot v - c(m_i) - L(m_i, D)$$

where $R_i$ is the observed reputation as a function of the actor's own manipulation and the manipulation vector of competitors, $v$ is the per-unit reputation value in terms of expected revenue, $c(m_i)$ is the direct cost of manipulation intensity $m_i$, and $L(m_i, D)$ is the expected loss from detection given the detection intensity $D$. The first-order condition characterizes the interior optimum,

$$\frac{\partial R_i}{\partial m_i} \cdot v = c'(m_i) + \frac{\partial L}{\partial m_i}$$

which sets the marginal reputation benefit equal to the sum of the marginal direct cost and the marginal expected detection loss.

The Nash equilibrium of the symmetric-actor manipulation game is characterized by the fixed-point condition that each actor's chosen manipulation intensity is optimal given the manipulation intensities chosen by all other actors,

$$m_i^* = \arg\max_{m_i} \pi_i(m_i, m_{-i}^*), \quad \forall i$$

with the vector $\mathbf{m}^* = (m_1^*, m_2^*, \ldots)$ satisfying the mutual best-response condition. The equilibrium manipulation intensity is generically positive when the reputation return $v$ is high, the marginal cost of manipulation $c'$ is low, the reputation function $R_i$ is highly sensitive to own manipulation, and the detection intensity $D$ is low. Empirical variation in equilibrium manipulation prevalence across platforms and categories can be interpreted as variation in these four parameters.

The prisoner's dilemma structure of the manipulation game admits a compact characterization. In the two-actor symmetric case with binary manipulation choices $m_i \in \{0, 1\}$, the payoff matrix

$$\begin{array}{c|cc}
 & m_j = 0 & m_j = 1 \\
\hline
m_i = 0 & (\pi_C, \pi_C) & (\pi_L, \pi_H) \\
m_i = 1 & (\pi_H, \pi_L) & (\pi_D, \pi_D)
\end{array}$$

with $\pi_H > \pi_C > \pi_D > \pi_L$ produces a dominant strategy equilibrium of mutual manipulation and a Pareto-inferior payoff pair $(\pi_D, \pi_D)$ relative to the mutual cooperation payoff $(\pi_C, \pi_C)$. The dilemma structure explains the observed universality of manipulation in unregulated reputation markets and the difficulty of unilateral abstention. Under a continuum-of-players extension with symmetric best response, the aggregate manipulation intensity converges to

$$M^* = \sum_{i=1}^{N} m_i^* \to N \cdot \bar{m}^*$$

as $N$ grows, with $\bar{m}^*$ the per-actor equilibrium intensity determined by the first-order condition. The elasticity of equilibrium manipulation with respect to detection intensity satisfies

$$\varepsilon_{m,D} = \frac{\partial \ln \bar{m}^*}{\partial \ln D} < 0$$

with magnitude determined by the convexity of the detection-loss function $L(m, D)$ and the convexity of the direct manipulation cost $c(m)$. High-elasticity regimes indicate that platform detection investment produces significant equilibrium manipulation reduction, and low-elasticity regimes indicate that detection alone is inadequate and additional deterrent instruments are required.

The detection intensity is chosen by the platform to maximize the platform's own objective, which typically weights consumer trust, producer participation, direct enforcement costs, and reputational and regulatory risk. The platform's first-order condition for detection intensity is

$$\frac{\partial \text{Consumer Trust}}{\partial D} \cdot \psi_C - \frac{\partial \text{Producer Participation}}{\partial D} \cdot \psi_P = C'(D)$$

with $\psi_C$ and $\psi_P$ the platform's marginal valuation of consumer trust and producer participation and $C'(D)$ the marginal cost of detection intensity. The equilibrium detection intensity is generically interior when the platform values both sides of the market and the marginal detection cost is convex. Given the detection instrument, the platform's classification of a candidate manipulation signal takes the Bayesian posterior

$$\Pr(m_i = 1 \mid \text{signal}) = \frac{\Pr(\text{signal} \mid m_i = 1) \, \pi(m_i = 1)}{\Pr(\text{signal} \mid m_i = 1) \, \pi(m_i = 1) + \Pr(\text{signal} \mid m_i = 0) \, \pi(m_i = 0)}$$

with the platform triggering enforcement when the posterior exceeds a threshold $\tau$. The classification-threshold choice trades off the true-positive rate against the false-positive rate along the receiver-operating characteristic

$$\text{TPR}(\tau) = 1 - F_1(\tau), \quad \text{FPR}(\tau) = 1 - F_0(\tau)$$

with $F_1$ and $F_0$ the score distributions conditional on manipulation and non-manipulation. The deterrence condition under which a rational actor abstains from manipulation is

$$\Pr(\text{detect}) \cdot \text{Penalty} + c(m) > \frac{\partial R_i}{\partial m_i} \cdot v \cdot m$$

with the left side the expected total cost and the right side the expected reputation gain. The condition binds tightly in high-detection high-penalty regimes and loosens in the opposite regime.

The system reaches a joint equilibrium when the producer's manipulation intensity, the platform's detection intensity, and the consumer's rational expectation are mutually consistent. The joint equilibrium admits multiple stable points depending on the parameter configuration. The high-manipulation equilibrium features high $m^*$, low $D^*$, low consumer trust, and low reputation signal informativeness. The low-manipulation equilibrium features low $m^*$, high $D^*$, high consumer trust, and high reputation signal informativeness. The equilibrium selection depends on historical path dependence, platform design choices, and the exogenous parameters. The equilibrium multiplicity is characteristic of reputation systems and is documented in [Cabral 2012][research_cabral_2012] Reputation on the Internet and related work.

The signal-to-noise ratio of the reputation signal under the manipulation equilibrium is

$$\text{SNR}(\mathbf{m}) = \frac{\text{Var}(h(\theta, e))}{\text{Var}(\eta) + \text{Var}(m \cdot \delta)}$$

where $m \cdot \delta$ represents the manipulation-induced perturbation to the observed signal. The manipulation-induced variance grows with equilibrium manipulation intensity and compresses the informativeness of the reputation signal. After a detected-and-exposed manipulation event at time $t_0$, the consumer trust attached to the affected reputation signal decays and recovers according to

$$T(t \mid \text{exposed at } t_0) = T_{\text{floor}} + (T_0 - T_{\text{floor}}) \cdot \bigl(1 - e^{-\lambda (t - t_0)}\bigr)$$

with $T_0$ the pre-exposure trust level, $T_{\text{floor}}$ the post-exposure trust floor set by the residual reputational damage, and $\lambda$ the recovery rate that varies by the severity of the exposed manipulation and by the audience's tolerance. The recovery-rate empirical estimates run from days for minor infractions on ephemeral platforms to years for major infractions on durable-record platforms.

## The Organic-Establishment Puzzle

The organic-establishment puzzle refers to the empirical observation that a minority of producers achieve genuine, high-value reputation under manipulation-saturated conditions where the manipulation equilibrium would predict that reputation carries no information. The puzzle admits several partial resolutions from the theoretical and empirical literature, and the miniseries treats each while noting that the full resolution remains contested.

The first partial resolution is the credibility-of-costly-signaling account developed in the [Spence 1973][research_spence_1973] tradition. Certain reputation signals remain difficult to manipulate because the signal production requires either substantial time investment, verifiable domain expertise, physical asset commitments, or documented track records that cannot be counterfeited without leaving audit trails. Producers who can produce such uncounterfeitable signals maintain the separating equilibrium in a segment of the market that the manipulation equilibrium leaves untouched. The uncounterfeitable-signal segment admits formal characterization through a modified single-crossing condition that requires the manipulation cost function to diverge in signal magnitude for the low-type actor,

$$\lim_{s \to \infty} \left[\frac{\partial c(s, \theta_L)}{\partial s} - \frac{\partial c(s, \theta_H)}{\partial s}\right] = +\infty$$

which preserves the separating equilibrium even when the standard single-crossing condition collapses under generic manipulation-cost reduction.

The second partial resolution is the audience-selection account. Producers who develop reputation within an audience segment that has invested in detection capability, that reads reputation signals critically, and that punishes detected manipulation heavily can sustain reputation under conditions that would collapse to the manipulation equilibrium in the general market. The audience-selection account admits formal characterization through segmented markets with differing detection intensities and manipulation returns.

The third partial resolution is the reputation-portfolio account developed in the [Tirole 1996][research_tirole_1996] Theory of Collective Reputations framework. Producers who anchor reputation to memberships in collective reputation entities (professional associations, verification programs, certification regimes, editorial imprints, chained-of-custody credentials) inherit the collective's detection and enforcement infrastructure. The collective reputation acts as a partial substitute for the individual reputation signal and shifts the manipulation game to the collective level, where the higher stakes and greater visibility typically sustain a lower manipulation equilibrium. The deviation cost imposed on a member of a collective who is detected manipulating aggregates across the collective's member reputational stakes,

$$C_{\text{deviate}}^{\text{collective}} = \sum_{j \in \text{collective}} \Delta R_j \cdot v_j + P_{\text{expulsion}}$$

with $\Delta R_j$ the reputation loss to member $j$ from the exposed deviation, $v_j$ the member's per-unit reputation value, and $P_{\text{expulsion}}$ the direct cost of expulsion from the collective. The internal-enforcement equilibrium is sustainable when the collective's members can credibly commit to expulsion of detected deviators.

The fourth partial resolution is the temporal-arbitrage account. Producers who invest heavily in reputation during periods of high signal informativeness (before the manipulation equilibrium fully develops in a given platform or category) can convert the accumulated reputation into an asset that persists after the manipulation equilibrium develops. The value of the legacy reputation asset is the present-discounted stream of informative rents accumulated before the equilibrium transitioned,

$$V_{\text{legacy}} = \int_0^{T_{\text{transition}}} R_i(t) \cdot v(t) \cdot I(t) \cdot e^{-rt} \, dt$$

with $I(t)$ the signal informativeness at time $t$ and $T_{\text{transition}}$ the time at which the market transitioned to the manipulation equilibrium. The temporal-arbitrage account explains the observed early-mover advantage in reputation on new platforms and the observed persistence of legacy reputation from pre-digital eras.

The fifth partial resolution is the enforcement-shadow account. Producers who operate under credible external enforcement (regulatory oversight, professional liability, contractual accountability to sophisticated counterparties) face manipulation costs elevated by external enforcement in addition to the platform's internal enforcement. The expected external penalty is the sum across enforcement channels

$$\Pi_{\text{external}}(m) = \sum_{k \in \text{channels}} \Pr(\text{detect}_k \mid m) \cdot L_k$$

with $\Pr(\text{detect}_k \mid m)$ the channel-$k$ detection probability and $L_k$ the channel-$k$ penalty. The enforcement-shadow account explains why certain regulated segments of the reputation market (professional services with liability exposure, publicly traded firms subject to securities disclosure, medical providers subject to malpractice liability) maintain higher signal informativeness than unregulated segments.

The organic-establishment puzzle admits partial quantitative formalization through the mixing weights of the manipulation-equilibrium and separating-equilibrium subpopulations. Let $\phi$ denote the fraction of producers in the separating-equilibrium subpopulation and $1 - \phi$ denote the fraction in the manipulation-equilibrium subpopulation. The consumer's posterior about a randomly encountered producer's type is a mixture

$$\Pr(\theta \mid s) = \phi \cdot \Pr(\theta \mid s, \text{separating}) + (1 - \phi) \cdot \Pr(\theta \mid s, \text{manipulation})$$

with the separating component carrying informative posterior and the manipulation component carrying uninformative posterior. The value of $\phi$ varies across platforms, categories, and time periods, and its estimation is a load-bearing empirical challenge for the miniseries.

The dynamics of $\phi$ over time can be characterized by a replicator equation in which producers switch between the separating-equilibrium and manipulation-equilibrium subpopulations in proportion to the relative payoff differential,

$$\dot{\phi} = \phi (1 - \phi) [\pi_{\text{sep}} - \pi_{\text{manip}}]$$

with $\pi_{\text{sep}}$ and $\pi_{\text{manip}}$ the expected payoffs to the two strategies. The interior fixed points of the replicator dynamics satisfy $\pi_{\text{sep}} = \pi_{\text{manip}}$, and the boundary fixed points at $\phi = 0$ and $\phi = 1$ are stable when the interior payoff comparison points away from the boundary. The local stability of an interior fixed point $\phi^*$ satisfies

$$\left.\frac{d\dot{\phi}}{d\phi}\right|_{\phi = \phi^*} < 0 \iff \phi^* \text{ is asymptotically stable}$$

and the boundary $\phi = 1$ is asymptotically stable when $\pi_{\text{sep}} > \pi_{\text{manip}}$ throughout a neighborhood of $\phi = 1$. The separating-equilibrium subpopulation grows when its expected payoff exceeds the manipulation-equilibrium payoff, which occurs when detection intensity, external enforcement, audience discrimination, or reputation persistence are sufficiently favorable. The manipulation-equilibrium subpopulation grows in the opposite parameter regime. The empirical trajectory of $\phi$ across major consumer platforms since 2000 shows marked category and platform variation and is documented in the platform-specific empirical literature the miniseries cites.

## The Six-Axis Analytical Framework

The miniseries applies a six-axis analytical framework introduced here in the framing article and revisited in the closing article. The framework identifies six dimensions along which any reputation manipulation practice admits characterization. The axes are chosen to permit systematic comparison across techniques, across platforms, and across historical episodes while remaining flexible enough to accommodate the empirical variation. The six axes are the signal axis (form and density of manipulated reputation transmission), the objective axis (what the manipulator optimizes for), the structure axis (organizational form of the manipulation operation), the model axis (doctrinal and technical content of the manipulation), the interaction axis (external relationships with platforms, targets, competitors, and enforcement authorities), and the adaptation axis (response to detection, enforcement, and platform-architecture change). Articles apply each axis to the techniques treated in the period under consideration.

The signal axis characterizes the form and density of information transmission by which each manipulation practice injects manipulated reputation signal into the reputation system. Signal-axis dimensions include channel identity (reviews, ratings, endorsements, engagement metrics, follower counts, recommendation-graph edges), signal volume (single injected signal, coordinated batch, sustained campaign), signal fidelity (crude fabrication detectable by simple filters, sophisticated fabrication matched to authentic distribution, hybrid mixing of authentic and fabricated signal), and cross-channel amplification (single-platform manipulation, cross-platform coordination, external-media amplification). The signal axis is operationalized as an injection-rate flux

$$\sigma_{\text{signal}}(t) = \sum_k n_k(t) \, w_k \, f_k$$

where $n_k$ counts injection events of kind $k$ (review, rating, comment, share, follow, engagement action), $w_k$ is the per-event weight in the ranking function, and $f_k$ is the per-event evasion fidelity against the platform's detection systems. High-fidelity manipulation exhibits $f_k$ close to unity, and low-fidelity manipulation exhibits $f_k$ that produces high detection rates. Cross-generational retention of injected signal follows a decay under platform-detection attenuation

$$R_{\text{inject}}(t) = R_0 \, \prod_{\tau=1}^{t} (1 - d_\tau), \quad d_\tau \in [0, 1]$$

where $d_\tau$ is the fraction of injected signal removed at time $\tau$ by platform enforcement. High-detection platforms exhibit $d_\tau$ closer to unity, and low-detection platforms exhibit $d_\tau$ close to zero. The channel diversity of an actor's signal injection is summarized by the Shannon entropy over the injection-channel distribution

$$H_{\text{channel}}^{i} = -\sum_k p_k^i \log p_k^i, \quad p_k^i = \frac{n_k^i}{\sum_{k'} n_{k'}^i}$$

with $p_k^i$ the fraction of actor $i$'s injection events allocated to channel $k$. High-diversity injection (large $H_{\text{channel}}$) spreads across many channels and complicates single-channel detection, and low-diversity injection concentrates on few channels and admits easier detection.

The objective axis characterizes what each manipulator seeks to optimize. Self-promotion manipulators optimize for the actor's own reputation score, ranking position, purchase-intent generation, and downstream commercial return. Competitor-attack manipulators optimize for the target's reputation degradation, ranking position loss, purchase-intent suppression, and downstream competitive advantage. Astroturf political operators optimize for the perceived popular support of a policy position, candidate, or narrative. State-sponsored operators optimize for foreign-policy objectives including electoral interference, information environment shaping, and adversary destabilization. The objective-axis differences produce downstream technique differences that subsequent articles trace. The objective axis operationalizes as an actor-specific utility functional over reputation-system states $x \in \mathcal{X}$

$$U_{\text{actor}}(x) = \sum_{j=1}^{J} \lambda_j \, g_j(x)$$

where $g_j$ are the actor's constitutive goals and $\lambda_j \geq 0$ are their relative weights. Actor divergence on the objective axis reduces to differences in the $\{\lambda_j, g_j\}$ specifications rather than divergence over instrumental rationality.

The structure axis characterizes the organizational form of the manipulation operation. Individual self-promoters operate at the smallest scale with the simplest organization. Small firm operators (a business owner boosting their own listings) constitute the next tier. Hired reputation-management firms operate at the intermediate scale with employer-employee relationships, task specialization, and client-service contracts. Reputation-manipulation service marketplaces (fake-review platforms, follower-purchase services, engagement-boost services) operate at the platform tier with two-sided market dynamics between manipulators and end-buyers. Coordinated inauthentic behavior networks operate at the campaign tier with central coordination across many operator accounts. State-sponsored operations operate at the largest scale with intelligence-service infrastructure, dedicated funding, and geopolitical objectives. The structure axis admits summary via hierarchy depth and branching factor,

$$D_{\text{struct}} = \text{longest authority path from operator to apex}, \quad B_{\text{struct}} = \text{mean subordinate count per authority node}$$

with individual operators exhibiting minimal $D_{\text{struct}}$ and $B_{\text{struct}}$, and state-sponsored operations exhibiting deep $D_{\text{struct}}$ and moderate $B_{\text{struct}}$ at intermediate tiers.

The model axis characterizes the doctrinal, technical, and rhetorical content each manipulation practice carries. The technical model includes the fabrication method (human-written, template-based, generative-model-produced), the account-provenance method (organic aged accounts, synthetic new accounts, hijacked authentic accounts, purchased authentic accounts), the coordination method (uncoordinated, spreadsheet-coordinated, platform-coordinated, algorithmically coordinated), and the evasion method (rotating IP addresses, timing distribution, behavioral randomization, linguistic variation). The rhetorical model includes the persuasion framing (testimonial, comparative, emotional, expert-authority), the credibility framing (verified purchase claim, verified user claim, identity performance), and the narrative framing (personal story, statistical claim, quality attribute enumeration). The model axis reduces to technique position vectors over a chosen technique-space basis $\{t_1, t_2, \ldots, t_M\}$

$$\mathbf{c}_{\text{practice}} = (c_1, c_2, \ldots, c_M), \quad c_m \in \{-1, 0, +1\}$$

with pairwise technique distance

$$d_{\text{model}}(A, B) = \sum_{m=1}^{M} |c_m^A - c_m^B|$$

measuring model-axis divergence between practices $A$ and $B$. The model-axis differences correspond to distinct detection signatures and distinct enforcement responses.

The interaction axis characterizes external relationships with platforms, targets, competitors, audiences, and enforcement authorities. Interaction-axis dimensions include the platform relationship (compliant use, terms-of-service violation, active concealment, adversarial evasion), the target relationship (target-unaware self-promotion, target-aware self-promotion, target-directed attack, third-party-directed attack), the competitor relationship (independent operation, industry-wide reputation collusion, competitor-attack coordination), the audience relationship (audience-unaware manipulation, audience-aware manipulation, audience-complicit manipulation), and the enforcement relationship (below-detection-threshold operation, detection-and-remediation cycle, escalated-enforcement engagement, legal-proceedings engagement). The interaction axis admits operationalization as a weighted signed graph over actors, targets, platforms, and enforcers,

$$W_{ij}(t) = w_{ij}^{\text{coop}}(t) - w_{ij}^{\text{conflict}}(t), \quad W(t) = [W_{ij}(t)] \in \mathbb{R}^{S \times S}$$

with enforcement-attributable imprint accumulating over time,

$$L_i(t) = \int_0^t \ell_i(\tau) \, d\tau$$

where $\ell_i(\tau)$ counts platform actions, regulatory actions, and legal judgments recorded against actor $i$ at time $\tau$.

The adaptation axis characterizes response to platform-architecture change, detection-technology change, and enforcement change. Adaptation-axis dimensions include technique migration (shifting from a detected technique to an undetected variant), platform migration (shifting from a high-enforcement platform to a low-enforcement platform), attribution obfuscation (shifting from traceable to untraceable operator infrastructure), and legal-form adaptation (shifting from prosecutable forms to protected forms under first-amendment, section-230, or jurisdictional-arbitrage protection). The adaptation axis takes the operational form first-order relaxation toward the actor's response equilibrium under novel platform conditions,

$$\frac{d S_i}{d t} = -\frac{1}{\tau_i}\bigl(S_i(t) - S_i^{*}(t)\bigr) + \xi_i(t)$$

where $S_i$ is the actor's technique-and-infrastructure state, $S_i^{*}(t)$ is the environment-dependent optimal response, $\tau_i$ is the actor's adaptation time constant, and $\xi_i(t)$ is exogenous perturbation. High-adaptation actors (professional manipulation-service firms with dedicated engineering teams) exhibit short $\tau_i$, and low-adaptation actors (individual self-promoters relying on manual technique) exhibit long $\tau_i$.

The six axes are not independent. The account admits a cross-axis coupling matrix

$$C_{\text{coupling}} = \left[\frac{\partial x_a}{\partial x_b}\right]_{a, b \in \{\text{signal, obj, struct, model, interact, adapt}\}}$$

with the off-diagonal entries indexing the sensitivity of axis $a$ to changes in axis $b$. Empirically salient couplings include structure-to-signal (a state-sponsored operator's signal capacity is bounded by the operator's structural scale), model-to-adaptation (a manipulation practice's model determines the ease of technique migration under detection pressure), and interaction-to-signal (an actor's platform relationship constrains the channels through which signal can be injected). The closing article of the miniseries treats the coupling structure empirically.

## Historical Antecedents

The contemporary reputation manipulation ecosystem inherits extensive technique, doctrine, and organizational form from pre-digital antecedents in public relations, advertising, propaganda, and political operations. The framing article characterizes the pre-digital inheritance in this section and defers the detailed treatment to subsequent articles as each technique class is analyzed.

The pre-industrial antecedents trace to the collective-reputation systems of the ancient and medieval world. Roman senatorial reputation operated through a formal ranking system (the cursus honorum) combined with informal reputation cultivation through the patronage-and-clientship network documented in [Wallace-Hadrill 1989][book_wallace_hadrill_1989] Patronage in Ancient Society. Medieval merchant reputation operated through the Champagne fairs and the Mediterranean trading network in which reputation was maintained through the Maghribi trader coalition documented in [Greif 1993][research_greif_1993] Contract Enforceability and Economic Institutions in Early Trade and further developed in [Greif 2006][book_greif_2006] Institutions and the Path to the Modern Economy. The medieval guild system administered collective reputation through membership admission, apprenticeship certification, and expulsion mechanisms documented in [Epstein and Prak 2008][book_epstein_prak_2008] Guilds Innovation and the European Economy. The early-modern commercial-reputation system operated through the correspondent-merchant network documented in [Trivellato 2009][book_trivellato_2009] The Familiarity of Strangers. The pre-industrial reputation systems admit interpretation within the collective-reputation framework of [Tirole 1996][research_tirole_1996] and provide the deep historical precedent for the contemporary platform-mediated reputation architecture.

The early-modern print-culture antecedents trace to the emergence of the newspaper as a reputation-mediating institution. The [Habermas 1962][book_habermas_1962] The Structural Transformation of the Public Sphere provides the theoretical framework for the emergence of the bourgeois public sphere as a reputation-mediating institution. The [Darnton 1982][book_darnton_1982] The Literary Underground of the Old Regime documents the pre-Revolutionary French pamphleteering tradition that combined political and reputational attack. The [Warner 1990][book_warner_1990] The Letters of the Republic treats the American colonial and early-republican print culture that shaped the reputation of political figures. The [Pasley 2001][book_pasley_2001] The Tyranny of Printers treats the partisan-press tradition of the American early republic in which newspapers routinely engaged in reputation manipulation on behalf of political factions. The print-culture antecedents illustrate that the manipulation-saturated information environment predates the digital era by several centuries.

The commercial-testimonial tradition traces to the patent-medicine advertising of the nineteenth century, in which manufacturers of proprietary medicines commissioned testimonials from prominent citizens, from ordinary users, and from fabricated personas. The [Young 1961][book_young_1961] The Toadstool Millionaires documents the American patent-medicine industry and its use of testimonial manipulation. The [Applegate 2012][book_applegate_2012] The Rise of Advertising in the United States traces the broader advertising industry's incorporation of testimonial techniques. The [Presbrey 1929][book_presbrey_1929] The History and Development of Advertising provides the pre-digital antecedent through the early twentieth century. The [Sivulka 1998][book_sivulka_1998] Soap Sex and Cigarettes provides the cultural-history treatment of the industry's development. The [Marchand 1985][book_marchand_1985] Advertising the American Dream treats the interwar advertising industry's construction of consumer identity as a reputation object.

The nineteenth-century yellow-journalism tradition produced organized reputation manipulation at the newspaper-industry scale. The [Campbell 2001][book_campbell_2001] Yellow Journalism documents the Pulitzer and Hearst rivalry that produced the manipulation-oriented mass-circulation newspaper. The [Nasaw 2000][book_nasaw_2000] The Chief provides the definitive biography of William Randolph Hearst and the operational detail of his newspaper empire's reputation-manipulation practices. The yellow-journalism era established many technique templates that later transferred to the twentieth-century advertising and PR industries.

The public-relations tradition of managed reputation traces to the founding of the modern PR industry in the early twentieth century. The [Bernays 1923][book_bernays_1923] Crystallizing Public Opinion and [Bernays 1928][book_bernays_1928] Propaganda established the doctrine of the systematic engineering of consent through media placement, endorsement cultivation, and narrative construction. The [Lee 1925][book_lee_1925] Publicity work and the earlier [Ivy Lee Declaration of Principles 1906][ref_ivy_lee_declaration_1906] established the professional-ethics framing of the PR industry, and the [Byoir 1930][ref_byoir_1930_1955] agency campaigns established the operational form. The [Lippmann 1922][book_lippmann_1922] Public Opinion provided the theoretical framework the PR industry drew on. The critical treatments in [Ewen 1996][book_ewen_1996] PR A Social History of Spin and [Tye 1998][book_tye_1998] The Father of Spin document the industry's development and its manipulation practices from the 1900s through the late twentieth century.

The astroturfing tradition of manufactured grassroots support traces to political-operations practice from the mid twentieth century forward, with sizable precedent in the corporate lobbying campaigns of the tobacco, oil, and pharmaceutical industries. The [McGarity and Wagner 2008][book_mcgarity_wagner_2008] Bending Science documents the corporate manufacture of doubt through funded academic work and coordinated advocacy. The [Oreskes and Conway 2010][book_oreskes_conway_2010] Merchants of Doubt documents the coordinated denial campaigns on tobacco, ozone depletion, acid rain, and climate change. The [Michaels 2008][book_michaels_2008] Doubt Is Their Product documents the corporate manufactured-doubt playbook. The term astroturf itself traces to Senator Lloyd Bentsen's 1985 characterization of manufactured constituent mail as artificial grass in the [Bentsen 1985 Congressional Record][ref_bentsen_congressional_record_1985], and the [Cho et al 2011][research_cho_et_al_2011] Astroturfing framework and the [Walker 2014][book_walker_2014] Grassroots for Hire treatment document the contemporary industry.

The propaganda tradition of state-sponsored reputation manipulation traces to the first world war on both allied and central-powers sides, with appreciable elaboration through the second world war, the cold war, and the contemporary information-operations era. The [Lasswell 1927][book_lasswell_1927] Propaganda Technique in the World War established the analytical framework. The [Ellul 1965][book_ellul_1965] Propaganda The Formation of Men's Attitudes provided the theoretical treatment. The [Herman and Chomsky 1988][book_herman_chomsky_1988] Manufacturing Consent developed the political-economy critique. The contemporary state-sponsored information operations are documented in [Rid 2020][book_rid_2020] Active Measures, [DiResta et al 2019][research_diresta_et_al_2019], and the [Mueller Report 2019][ref_mueller_report_2019] Volume One on Russian interference in the 2016 election.

The direct-marketing tradition of database-driven reputation and preference manipulation traces to the mid twentieth century mail-order and catalog industry and the subsequent development of psychographic marketing. The [Packard 1957][book_packard_1957] The Hidden Persuaders documents the mid-century motivation research industry. The [Turow 2011][book_turow_2011] The Daily You traces the transition to digital psychographic targeting and the contemporary surveillance-advertising economy that provides the substrate for algorithmic reputation manipulation.

The diffusion of a manipulation technique across the operator population follows the general form of the [Bass 1969][research_bass_1969] diffusion model,

$$\frac{dN(t)}{dt} = \bigl(p + q \, \frac{N(t)}{\bar{N}}\bigr) \bigl(\bar{N} - N(t)\bigr)$$

with $N(t)$ the cumulative adopter count at time $t$, $\bar{N}$ the ceiling adopter count, $p$ the innovation coefficient (external influence), and $q$ the imitation coefficient (internal influence). The propaganda reach amplification through cascading exposure follows the compound-growth form

$$R_{\text{reach}}(t) = R_0 \, (1 + \eta)^t$$

with $\eta$ the per-period retransmission gain that combines the audience-network branching factor and the per-message persistence. The empirical treatment of pre-digital propaganda reach traces to [Berelson 1948][research_berelson_1948] and subsequent work; the digital-era treatment appears in [Vosoughi Roy Aral 2018][research_vosoughi_roy_aral_2018] and the platform-integrity literature.

## Historiographical Gap and Recent Scholarship

The scholarly treatment of virtual reputation manipulation has developed unevenly across disciplines, historical periods, and platform categories. The framing article surveys the observable gap in the scholarly literature and identifies the recent-scholarship developments that the miniseries builds on.

The economics-of-reputation literature developed in the 1970s and 1980s under the general information-economics program initiated by [Akerlof 1970][research_akerlof_1970] and [Spence 1973][research_spence_1973], with the reputation-specific extensions in [Klein and Leffler 1981][research_klein_leffler_1981], [Kreps and Wilson 1982][research_kreps_wilson_1982], [Shapiro 1983][research_shapiro_1983], and [Milgrom and Roberts 1986][research_milgrom_roberts_1986]. The extension to digital reputation systems began with [Resnick et al 2000][research_resnick_et_al_2000] and continued through [Dellarocas 2003][research_dellarocas_2003], [Ba and Pavlou 2002][research_ba_pavlou_2002], and [Bolton Katok Ockenfels 2004][research_bolton_katok_ockenfels_2004]. The gap between the theoretical literature and the empirical manipulation-prevalence literature that emerged in the 2010s reflects the historical division between economic-theoretic work grounded in game-theoretic modeling and empirical detection work grounded in machine-learning and network-analytic methodology. The recent [He Hollenbeck Proserpio 2022][research_he_hollenbeck_proserpio_2022] treatment for Amazon reviews and the [Luca and Zervas 2016][research_luca_zervas_2016] treatment for Yelp begin to bridge the two traditions.

The sociological literature on reputation and status developed in parallel to the economics literature but with limited cross-fertilization until the recent embeddedness-and-networks synthesis. The [Podolny 2005][book_podolny_2005] Status Signals treatment marks the substantive integration of the two traditions. The digital-reputation extension in [Marwick 2013][book_marwick_2013] Status Update and [Marwick and boyd 2011][research_marwick_boyd_2011] I Tweet Honestly begins to connect the sociological framing to the empirical platform-specific research.

The critical-media-studies and disinformation-studies literature developed in the 2010s in response to the 2016 US election and the subsequent recognition of state-sponsored information operations. The [Benkler Faris Roberts 2018][book_benkler_faris_roberts_2018] Network Propaganda, [Jamieson 2018][book_jamieson_2018] Cyberwar, [Woolley 2020][book_woolley_2020] The Reality Game, and [Rid 2020][book_rid_2020] Active Measures treatments established the field. The commercial-reputation-manipulation literature has developed largely separately, with limited cross-reference to the political-manipulation literature despite considerable technique overlap. The miniseries treats the two literatures as connected through shared technique, infrastructure, and detection challenges.

The legal-scholarship literature on platform governance and intermediary liability developed in the late 2010s in response to the Section-230 policy debate and the emerging platform-integrity concerns. The [Klonick 2018][research_klonick_2018] New Governors, [Balkin 2018][research_balkin_2018] Free Speech is a Triangle, [Douek 2021][research_douek_2021] Governing Online Speech, and [Suzor 2019][book_suzor_2019] Lawless treatments established the platform-governance subfield. The legal treatment of reputation manipulation as distinct from broader content-moderation questions remains significantly underdeveloped, with [Solove 2007][book_solove_2007] The Future of Reputation the most substantive legal treatment to reputation.

The computer-science literature on manipulation detection developed through the 2010s and accelerated in the 2020s. The [Cresci 2020][research_cresci_2020] Decade of Social Bot Detection surveys the bot-detection subfield. The [Yang et al 2020][research_yang_et_al_2020] Scalable and Generalizable Social Bot Detection treatment extends the model to contemporary bot populations. The [Ott et al 2011][research_ott_et_al_2011] Finding Deceptive Opinion Spam initiated the fake-review-detection subfield, extended in [Mukherjee et al 2013][research_mukherjee_et_al_2013] Yelp Fake Review Filter, [Rayana and Akoglu 2015][research_rayana_akoglu_2015] Collective Opinion Spam Detection, [Kumar et al 2017][research_kumar_et_al_2017] Rating Distributions, and continuing work. The [Grinberg et al 2019][research_grinberg_et_al_2019] Fake News on Twitter treatment provides the network-level empirical assessment of manipulation exposure. The computer-science literature has developed primarily as a detection-methodology tradition with limited integration into the economic and legal frameworks the miniseries adopts.

The historiographical gap that the miniseries seeks to address is the absence of an integrated treatment that draws on all five traditions simultaneously. Each tradition treats a portion of the reputation-manipulation phenomenon: economics treats the incentive structure, sociology treats the audience-and-community structure, critical media studies treats the political-economy structure, law treats the constraint structure, and computer science treats the detection-and-classification methodology. The comprehensive treatment requires all five, and the miniseries organizes the material to make the cross-tradition connections explicit where they are load-bearing for the analytical conclusions.

## Regulatory and Legal Framework

Reputation manipulation intersects with a significant body of statutory, regulatory, and case law that shapes both the manipulation practices themselves and the platform enforcement responses. The framing article surveys the load-bearing legal instruments and defers detailed treatment of the enforcement history to the closing article.

The United States federal framework rests principally on Section 5 of the Federal Trade Commission Act of 1914 at [15 USC 45][ref_ftc_act_15_usc_45] prohibiting unfair or deceptive acts or practices in or affecting commerce. Deceptive endorsement and testimonial practices are addressed through the FTC Endorsement Guides at [16 CFR Part 255][ref_ftc_endorsement_guides_16_cfr_255] establishing disclosure requirements and material-connection standards, together with the [FTC Endorsement Guides FAQ][ref_ftc_endorsement_faq] providing operational interpretation. The Consumer Review Fairness Act of 2016 at [15 USC 45b][ref_consumer_review_fairness_act_2016] prohibits form-contract provisions that restrict consumer review posting. False-advertising claims against manipulated reputation content proceed principally under Section 43(a) of the Lanham Act at [15 USC 1125][ref_lanham_act_15_usc_1125] which creates a private right of action for competitors damaged by false or misleading representations. Intermediary liability for reputation content hosted on platforms is limited by Section 230 of the Communications Decency Act at [47 USC 230][ref_section_230_cda] which immunizes interactive computer service providers from liability for third-party content while permitting good-faith moderation.

The state framework varies. California's Unfair Competition Law at [California Business and Professions Code Section 17200][ref_california_ucl_17200] provides a broad private right of action against unfair, unlawful, or fraudulent business acts. State attorney-general enforcement authorities have brought reputation-manipulation cases under state consumer-protection statutes, and the New York State Attorney General office has been particularly active in this area.

The European framework rests principally on the Unfair Commercial Practices Directive at [Directive 2005/29/EC][ref_eu_ucpd_2005_29_ec] as implemented in member-state law, which prohibits misleading commercial practices including undisclosed paid endorsements and fake reviews. The Digital Services Act at [Regulation 2022/2065][ref_eu_dsa_2022] imposes systemic-risk assessment and mitigation obligations on very large online platforms and search engines. The AI Act at [Regulation 2024/1689][ref_eu_ai_act_2024] regulates deployment of generative-model systems whose output may facilitate reputation manipulation. The [European Commission 2023][ref_ec_2023_sweep] cross-platform sweep of consumer websites documented systematic non-compliance across member states.

The United Kingdom framework includes the [Online Safety Act 2023][ref_uk_online_safety_act_2023] imposing duties of care on user-to-user services and search services, and the [UK CMA fake reviews action][ref_uk_cma_fake_reviews] under the Consumer Protection from Unfair Trading Regulations 2008. The Australian framework rests on the Australian Consumer Law with implementation through the [ACCC fake reviews guidance][ref_accc_fake_reviews_guidance]. The Australian [OAIC Online Privacy Principles][ref_oaic_australian_privacy_principles] address the data-protection dimension of platform manipulation.

Enforcement case law developed through the 2010s and 2020s establishes precedent across several fact patterns. The [FTC v. Cure Encapsulations 2019][ref_ftc_cure_encapsulations_2019] action addressed a supplement manufacturer's payment for fake Amazon reviews. The [NY Attorney General v. Devumi 2019][ref_ny_ag_devumi_2019] action addressed a fake-social-media-follower marketplace and established the first US enforcement action treating fake identities as false endorsements. The [SEC v. Kardashian 2022][ref_sec_kardashian_2022] action addressed undisclosed crypto-asset promotion and established that celebrity endorsement disclosure requirements apply to social-media promotion. The [Amazon v. Fake Review Brokers 2022][ref_amazon_v_fake_review_brokers_2022] private-action campaign has produced settlements with multiple marketplace intermediaries. The [People v. Lifestyle Lift 2013][ref_ny_ag_lifestyle_lift_2013] investigation and settlement established the earliest state-level enforcement action against organized fake-review production. The [GAO 2020 Report on Online Consumer Reviews][ref_gao_2020_online_reviews] provides the consolidated federal audit of the enforcement landscape as of the late 2010s.

Platform-integrity self-regulation runs parallel to the statutory framework. The [Meta Adversarial Threat Report][ref_meta_atr] provides quarterly disclosure of coordinated-inauthentic-behavior enforcement. The [Meta Coordinated Inauthentic Behavior policy][ref_meta_cib_policy] establishes the operational definition of CIB that the platform-integrity industry has adopted. The [Google Search Quality Rater Guidelines][ref_google_srg] establish the taxonomy of manipulated content that the search-quality evaluation framework identifies. The [Amazon Community Guidelines][ref_amazon_community_guidelines] establish the platform's anti-manipulation policy for review content. The [YouTube Community Guidelines Enforcement Report][ref_youtube_transparency_report] and the [Reddit Transparency Report][ref_reddit_transparency_report] provide quantitative disclosure of platform-side enforcement volume. The [TikTok Community Guidelines Enforcement Report][ref_tiktok_transparency_report] provides equivalent disclosure for the TikTok platform.

Empirical study of the manipulation ecosystem draws on several standing datasets. The [Yelp Open Dataset][ref_yelp_open_dataset] provides business, review, and user records suitable for detection research. The [Amazon Reviews Dataset][ref_amazon_reviews_dataset] provides multi-category review corpora used across the fake-review detection literature. The [Botometer database][ref_botometer] provides bot-detection scores for social-media accounts. The [Stanford Internet Observatory data catalog][ref_stanford_internet_observatory] provides datasets and code from the observatory's investigations. The [Twitter Election Integrity dataset archive][ref_twitter_election_integrity] preserves the pre-2023 Twitter releases of state-attributed information-operations content.

The First Amendment constraint on reputation-manipulation regulation runs through the defamation case law from [New York Times v Sullivan 1964][ref_ny_times_sullivan_1964] establishing the actual-malice standard for public-figure defamation, [Gertz v Robert Welch 1974][ref_gertz_v_welch_1974] extending this formulation to private figures, [Milkovich v Lorain Journal 1990][ref_milkovich_v_lorain_1990] distinguishing statements of fact from statements of opinion, and [Snyder v Phelps 2011][ref_snyder_v_phelps_2011] on speech of public concern. The First Amendment framework constrains both the direct regulation of manipulated content and the platform-liability regime that would otherwise incentivize aggressive content moderation.

The Section 230 CDA case law defines the scope of intermediary immunity for platforms hosting manipulated content. The foundational [Zeran v AOL 1997][ref_zeran_v_aol_1997] decision established the broad immunity for third-party content, and [Fair Housing Council v Roommates.com 2008][ref_roommates_2008] carved out the exception for platform-solicited or platform-created content. The [Barnes v Yahoo 2009][ref_barnes_v_yahoo_2009] decision addressed promissory-estoppel exceptions. The [Force v Facebook 2019][ref_force_v_facebook_2019] decision addressed algorithmic-recommendation liability. The recent [Gonzalez v Google 2023][ref_gonzalez_v_google_2023] and [Twitter v Taamneh 2023][ref_twitter_v_taamneh_2023] Supreme Court decisions declined to substantially narrow Section 230 while addressing platform-recommendation liability under the Antiterrorism Act. The [Malwarebytes v Enigma 2020][ref_malwarebytes_v_enigma_2020] cert-denial dissent by Justice Thomas signaled interest in Section-230 revisitation that has not yet materialized. The [FOSTA-SESTA 2018 amendment][ref_fosta_sesta_2018] created the first substantive Section-230 exception, limited to sex-trafficking content.

The international comparative regulation includes the German [Netzwerkdurchsetzungsgesetz NetzDG 2017][ref_germany_netzdg_2017] imposing content-removal obligations on major platforms, the French [Loi Avia 2020][ref_france_loi_avia_2020] largely struck down by the Conseil constitutionnel, the Indian [IT Intermediary Guidelines 2021][ref_india_it_rules_2021] imposing traceability and grievance-officer requirements, the Singapore [Protection from Online Falsehoods and Manipulation Act 2019][ref_singapore_pofma_2019] providing government-directed correction and takedown authority, the Brazilian [Marco Civil da Internet 2014][ref_brazil_marco_civil_2014] establishing the intermediary-liability framework, and the [China Cyberspace Administration deep-synthesis regulations 2023][ref_china_cac_deepfake_2023] regulating generative-model output including manipulation-adjacent applications. The [Bradshaw Bailey Howard 2021][research_bradshaw_bailey_howard_2021] Industrialized Disinformation treatment surveys the cross-national comparative regulatory landscape.

## Contemporary Platform Landscape

The contemporary platform landscape in which reputation manipulation operates admits partition into several major categories that the miniseries treats. The categories differ in their reputation-signal architecture, their detection intensity, their legal exposure, and their manipulation-equilibrium characteristics.

The consumer-review platforms include Amazon, Yelp, Google Reviews, Tripadvisor, and category-specific review sites (Booking.com, OpenTable, Angi, Zocdoc). The dominant signal is the star rating combined with the text review. The manipulation economy has been documented extensively for Amazon in [He Hollenbeck Proserpio 2022][research_he_hollenbeck_proserpio_2022] and [Wu et al 2020][research_wu_et_al_2020], for Yelp in [Luca and Zervas 2016][research_luca_zervas_2016], for Tripadvisor in [Mayzlin Dover Chevalier 2014][research_mayzlin_dover_chevalier_2014], and for Google Reviews in [Feng et al 2021][research_feng_et_al_2021] and subsequent work.

The e-commerce marketplaces include Amazon, eBay, Etsy, Alibaba, and platform-integrated sellers on Instagram and TikTok. The dominant signals are seller ratings, product ratings, and platform-assigned badges (Best Seller, Amazon's Choice, verified badges). The manipulation economy overlaps markedly with the consumer-review economy. Additional manipulation vectors include buy-box manipulation, listing-hijacking, and search-ranking manipulation through keyword-stuffing and inventory positioning.

The social-media engagement platforms include Facebook, Instagram, X (formerly Twitter), TikTok, YouTube, LinkedIn, Reddit, Snapchat, Threads, and Bluesky. The dominant signals are follower counts, engagement metrics (likes, comments, shares, saves), and algorithmic recommendation position. The manipulation economy for follower purchase is documented in [De Micheli and Stroppa 2013][research_demicheli_stroppa_2013], for coordinated inauthentic behavior in [Bradshaw and Howard 2019][research_bradshaw_howard_2019] and the [DFRLab Reports][ref_dfrlab_reports], and for algorithmic amplification manipulation in [Papakyriakopoulos et al 2020][research_papakyriakopoulos_et_al_2020].

The search-engine and content-discovery platforms include Google Search, Bing, DuckDuckGo, Baidu, Yandex, and category-specific discovery (Google Scholar, PubMed, Apple App Store search, Google Play Store search, Amazon search). The dominant signals are ranking position under the platform's ranking function. The manipulation economy runs through search-engine optimization (SEO), reverse-SEO or negative-SEO attacks, and app-store optimization (ASO). The scholarly and industry treatment is documented in [Halavais 2018][book_halavais_2018] Search Engine Society and in the search-engine optimization industry literature.

The professional-network platforms include LinkedIn, ResearchGate, Google Scholar, GitHub, and professional-community-specific platforms. The dominant signals are credential verification, endorsement count, publication citation, and contribution metrics. The manipulation economy runs through credential fabrication, endorsement exchange, citation manipulation, and contribution-metric gaming. The academic-citation manipulation literature is documented in [Van Noorden 2020][research_van_noorden_2020] and the [Retraction Watch database][ref_retraction_watch].

The rating-and-review-service platforms include the platforms that aggregate reputation across other platforms, including Better Business Bureau, Trustpilot, Sitejabber, Consumer Affairs, and Glassdoor. The manipulation dynamics on the aggregator platforms mirror the manipulation dynamics on the underlying platforms with additional layer-specific dynamics around cross-platform brand reputation.

The community-moderation platforms include Reddit, Stack Exchange, Wikipedia, Quora, and category-specific community platforms. The dominant signals are community-assigned moderation status, karma or reputation scores, and edit history. The manipulation economy runs through vote manipulation, sock-puppet posting, edit-war engagement, and moderator co-optation. The Wikipedia case is documented in [Jemielniak 2014][book_jemielniak_2014] Common Knowledge, [Konieczny 2010][research_konieczny_2010], and the [Wikipedia Signpost archives][ref_wikipedia_signpost].

The subscription-and-follower platforms include Substack, Patreon, OnlyFans, YouTube memberships, and Twitch subscriptions. The dominant signals are subscriber counts and revenue proxies. The manipulation economy runs through subscriber purchase, view-count inflation, and coordinated cross-promotion.

The gig-economy and marketplace platforms include Uber, Lyft, DoorDash, Airbnb, TaskRabbit, and Fiverr. The dominant signals are provider ratings, completion rates, and category-specific quality metrics. The manipulation dynamics include provider-side rating manipulation, coordinated cross-rating rings, and consumer-side rating extortion. The empirical treatment is documented in [Athey Castillo Chandar 2019][research_athey_castillo_chandar_2019] and subsequent work.

The scale of the manipulation economy across the landscape admits summary through order-of-magnitude estimates from the industry and regulatory literature. The [FTC 2019 Sunday Riley settlement][ref_ftc_sunday_riley_2019], the [FTC 2020 Fashion Nova settlement][ref_ftc_fashion_nova_2020], the [FTC 2022 Fake Reviews and Endorsements notice of penalty offense][ref_ftc_penalty_offense_2022], and the [FTC 2024 final rule on fake reviews][ref_ftc_final_rule_2024] provide the regulatory documentation. The estimated aggregate annual reputation-manipulation-service market size across major platforms is approximately

$$V_{\text{manip-market}} \sim 10^{9} \text{ to } 10^{10} \text{ USD per year}$$

with the upper bound reflecting the sum of documented service marketplaces plus the estimated volume of internal firm-level manipulation spending. The estimated fake-review prevalence across major consumer platforms varies by category, with the observed range across the platform categories partitioned above satisfying approximately

$$p_{\text{fake}} \in [0.05, 0.40], \quad p_{\text{fake}}^{\text{high-manip category}} > 0.30$$

with the [World Economic Forum 2021][ref_wef_2021_fake_reviews] and [European Commission 2023][ref_ec_2023_sweep] cross-platform sweeps providing category-specific estimates. The aggregate fake-content volume across the reputation ecosystem admits summary as the sum across categories

$$V_{\text{fake}}(t) = \sum_{c \in \text{categories}} n_c(t) \cdot p_c(t)$$

with $n_c(t)$ the total signal-event volume in category $c$ at time $t$ and $p_c(t)$ the category-specific manipulation prevalence. The estimated aggregate ranges from approximately one billion to approximately one hundred billion manipulated signal events per year across the major categories, with the upper bound reflecting generative-model-enabled scale-up documented since 2023 in [Sohail et al 2024][research_sohail_et_al_2024] and subsequent work.

The generative-model impact on the manipulation ecosystem constitutes the most substantial recent development. Large-language-model deployment since the [OpenAI ChatGPT release 2022][ref_openai_chatgpt_2022] and subsequent [GPT-4 release 2023][ref_openai_gpt4_2023], the [Anthropic Claude release][ref_anthropic_claude], and the open-source model releases documented in the [Meta Llama papers][ref_meta_llama] and successors, has produced a step-change reduction in the marginal cost of generating human-quality manipulated content. The empirical assessment in [Yang and Menczer 2024][research_yang_menczer_2024] Anatomy of an AI-Powered Malicious Social Botnet documents the deployment of large-language-model-driven bot accounts across social platforms. The [Goldstein et al 2023][research_goldstein_et_al_2023] Generative Language Models and Automated Influence Operations treatment surveys the emerging threat landscape. The [Sadasivan et al 2023][research_sadasivan_et_al_2023] Can AI-Generated Text be Reliably Detected treatment establishes the detection-difficulty ceiling under contemporary technique. The generative-model transition shifts the manipulation cost function's convexity parameter $\alpha$ appreciably toward unity, which shifts the manipulation-equilibrium first-order condition toward higher equilibrium manipulation intensity absent compensating increases in detection capability. The [Watermarking Large Language Models literature][research_kirchenbauer_et_al_2023] and the [C2PA content provenance standard][ref_c2pa_standard] represent the emerging technical countermeasure infrastructure.

The bot-ecosystem-specific empirical assessment includes [Chu et al 2012][research_chu_et_al_2012] Detecting Automation of Twitter Accounts, [Varol et al 2017][research_varol_et_al_2017] Online Human-Bot Interactions, [Bessi and Ferrara 2016][research_bessi_ferrara_2016] Social Bots Distort the 2016 US Presidential Election Discussion, [Cresci et al 2017][research_cresci_et_al_2017] The Paradigm-Shift of Social Spambots, and [Rauchfleisch and Kaiser 2020][research_rauchfleisch_kaiser_2020] The False Positive Problem of Automatic Bot Detection. The prevalence estimates for bot accounts on major social platforms range from approximately five percent to approximately fifteen percent of active accounts under conservative classifiers and higher under aggressive classifiers, with the divergence reflecting the boundary definition between fully automated accounts, semi-automated accounts, and human-operated accounts with automation assistance.

## Alternative Analytical Frameworks

The economics-and-signaling framework the miniseries adopts is one of several analytical frameworks under which the reputation-manipulation phenomenon has been treated. The framing article surveys the principal alternatives and identifies where the alternative frameworks would produce different conclusions from the treatment the miniseries adopts.

The public-choice framework of [Buchanan and Tullock 1962][book_buchanan_tullock_1962] The Calculus of Consent treats reputation manipulation as an instance of rent-seeking within a political-economy framework in which manipulation is analyzed by the incentives of interest groups to invest resources in reputation-shifting rather than in productive activity. This account produces stronger normative conclusions about the welfare costs of the manipulation equilibrium and predicts regulatory-capture dynamics under which platform enforcement systematically underweights the consumer side.

The information-cascade framework of [Bikhchandani Hirshleifer Welch 1992][research_bikhchandani_hirshleifer_welch_1992] A Theory of Fads Fashion Custom and Cultural Change and the [Banerjee 1992][research_banerjee_1992] Simple Model of Herd Behavior treats reputation manipulation as an intervention in a cascade dynamic in which early signals disproportionately shape later beliefs. The framework predicts that early-stage manipulation produces disproportionate downstream reputation effects and that the manipulation equilibrium exhibits strong path-dependence rather than convergence to a stable configuration. The [Salganik Dodds Watts 2006][research_salganik_dodds_watts_2006] Experimental Study of Inequality and Unpredictability in an Artificial Cultural Market provides the empirical demonstration of cascade dynamics in a controlled reputation-adjacent setting.

The evolutionary-game-theoretic framework of [Maynard Smith 1982][book_maynard_smith_1982] Evolution and the Theory of Games and the [Nowak 2006][book_nowak_2006] Evolutionary Dynamics extension treats the manipulation equilibrium as a stable strategy profile in a repeated interaction over the operator population. The account identifies conditions under which the manipulation strategy is invasion-resistant, replaces the honest strategy under replicator dynamics, and admits or does not admit persistent minority strategies. The model provides an alternative theoretical foundation for the organic-establishment-minority puzzle the miniseries treats.

The complex-systems and network-dynamics framework of [Barabási and Albert 1999][research_barabasi_albert_1999] Emergence of Scaling in Random Networks and the [Newman 2010][book_newman_2010] Networks treatment treats reputation as an emergent property of the interaction graph rather than as a property of individual actors. This formulation predicts that reputation-manipulation effects are shaped by the network topology and that platform-architecture changes to the underlying graph produce reputation-equilibrium changes independent of any manipulation-technique changes. The [Watts 2002][research_watts_2002] A Simple Model of Global Cascades treatment provides the threshold-cascade framework for reputation dynamics.

The critical-political-economy framework of [Fuchs 2014][book_fuchs_2014] Social Media A Critical Introduction and [Fisher and Fuchs 2015][book_fisher_fuchs_2015] Reconsidering Value and Labour in the Digital Age treats reputation manipulation as a symptomatic outcome of the contradictions in the surveillance-capitalist information economy rather than as a phenomenon to be understood in its own terms. The treatment predicts that reforms internal to the platform-integrity framework will fail to address the underlying manipulation dynamic and that structural reform of the platform business model is required.

The regulatory-capture framework of [Stigler 1971][research_stigler_1971] The Theory of Economic Regulation extends to reputation-manipulation enforcement through the observation that regulated industries tend to capture their regulators over time. This account predicts that platform-integrity enforcement will systematically underweight consumer interests relative to producer interests as the manipulation-service industry organizes to influence platform policy. The framework also predicts that state-level regulation will be captured by the platforms it seeks to regulate.

The Bayesian-persuasion framework of [Kamenica and Gentzkow 2011][research_kamenica_gentzkow_2011] treats platform-mediated reputation as an information-design problem in which the platform's ranking function and signal-presentation choices themselves constitute a form of manipulation independent of the individual actor's manipulation choices. The account identifies platform-design choices that maximize the platform's own objective at the expense of consumer welfare and predicts a systematic bias toward reputation-signal presentations that maximize consumer purchase-intent at the expense of accuracy.

Each alternative framework offers analytical leverage the miniseries does not fully develop. The miniseries adopts the economics-and-signaling framework as the primary organizing structure because it provides the most tractable formalization of the manipulator-platform-consumer strategic interaction and because it connects most directly to the empirical detection and enforcement literatures. The closing article treats the treatment selection more fully and identifies the empirical questions on which the alternative frameworks would predict different observations.

## Terminological Note

The miniseries adopts terminological conventions. The term reputation manipulation refers to the deliberate injection of reputation signals into a reputation system that would not have arisen from authentic underlying transactions or attributes. The term astroturfing refers to the manipulation practice of manufacturing apparent grassroots support for a person, product, position, or narrative. The term sockpuppeting refers to the practice of one operator using multiple false identities to inject coordinated signal. The term Sybil attack refers to the technical variant of sockpuppeting in which the false identities are created and maintained at scale through automated infrastructure. The term coordinated inauthentic behavior (abbreviated CIB) refers to the platform-integrity terminology for coordinated manipulation campaigns and traces to Facebook's 2018 policy framework. The term review bombing refers to the coordinated deposit of negative reviews against a target, distinct from the aggregate effect of authentic negative reviews. The term brigading refers to the coordinated deposit of engagement (positive or negative) against a target from an external community. The term reputation laundering refers to the practice of transferring reputation from a source with credibility to a target that lacks credibility, whether through endorsement, acquisition, or association. The term reputation arbitrage refers to the practice of exploiting cross-platform reputation transfer, cross-category reputation transfer, or temporal reputation transfer for commercial gain. The term negative search-engine optimization (abbreviated negative SEO or reverse SEO) refers to the technique class oriented at degrading a target's search-ranking position. The term reputation defense refers to the practice of protecting an authentic reputation against manipulation attacks. The term organic reputation refers to reputation established through the accumulated record of authentic transactions, attributes, or contributions without manipulation. The naming of platforms follows the platform's own current name where possible, with historical names noted where relevant. The miniseries recognizes that manipulation, astroturfing, and inauthentic behavior are contested terms with evolving definitions in academic, regulatory, and platform-industry usage, and no terminological choice fully escapes the interpretive problems the terminology introduces.

## Series Roadmap

The four articles proceed as follows. Each is a comprehensive science-and-history survey rather than an application or tutorial. The full six-axis analytical framework recurs across the articles, and cross-references between them use back-references only so that each article stands alone.

Article one, this article, is the framing.

Article two treats the techniques of self-promotion oriented reputation manipulation. The article organizes the technique inventory by the signal-channel target and by the account-provenance method. Individual review fabrication, coordinated review campaigns, follower purchase, engagement purchase, sockpuppet-driven amplification, generative-model-produced testimonial and endorsement content, search-engine optimization at the aggressive and manipulative end of the spectrum, coordinated cross-platform amplification rings, credential fabrication, and reputation laundering through endorsement acquisition. Documented case studies from the FTC enforcement record, from platform integrity disclosures, and from academic detection studies anchor each technique class. Detection signatures, platform countermeasures, and enforcement case histories accompany each class.

Article three treats the techniques of competitor-attack oriented reputation manipulation. The article organizes the technique inventory by the attack vector and by the target's reputation-system position. Review bombing, brigading, coordinated negative-signal deposit, negative search-engine optimization, defamation campaigns, reporting-system weaponization (mass-report abuse to trigger platform enforcement against the target), Sybil-driven downvoting, complaint-farm services, adversarial content operations targeting the competitor's audience, and cross-platform coordinated negative campaigns. Documented case studies from the FTC enforcement record, from platform integrity disclosures, from defamation-litigation records, and from academic detection studies anchor each technique class. Detection signatures, platform countermeasures, and enforcement case histories accompany each class.

Article four synthesizes the miniseries and treats the detection landscape, the countermeasure landscape, and the organic-establishment minority. The detection landscape includes the statistical detection methods (distributional anomaly detection, temporal anomaly detection, network anomaly detection), the machine-learning detection methods (classifier-based detection, embedding-based detection, generative-adversarial detection), the human-review detection methods, and the cross-platform detection collaboration. The countermeasure landscape includes the platform-integrity operations, the identity-verification systems, the transaction-verification systems, the legal-liability regimes, and the emerging cryptographic-attestation frameworks. The organic-establishment landscape includes the empirical characterization of the producers who maintain organic reputation under manipulation-saturated conditions, the sectors and platforms where organic establishment remains viable, and the strategies documented in the case studies. The article closes with forward projection to the 2030-2050 window under alternative assumptions about generative-model capability, platform-integrity investment, regulatory enforcement, and cross-platform coordination.

## Load-Bearing Open Questions

- What is the correct empirical characterization of aggregate fake-review prevalence across the major consumer-review platforms, and how does the prevalence estimate change under alternative detection methodologies? The [Luca and Zervas 2016][research_luca_zervas_2016] estimate for Yelp, the [He Hollenbeck Proserpio 2022][research_he_hollenbeck_proserpio_2022] estimate for Amazon, and the platform-industry estimates diverge greatly and the divergence remains unresolved.
- What is the correct empirical characterization of the causal impact of manipulation on downstream consumer behavior? The [Ma et al 2013][research_ma_et_al_2013] and [Chevalier and Mayzlin 2006][research_chevalier_mayzlin_2006] estimates and subsequent work provide competing empirical bases.
- What is the correct empirical characterization of the marginal deterrent effect of legal enforcement on manipulation prevalence? The pre-and-post studies of major FTC enforcement actions provide the empirical base, and the treatment remains contested.
- What is the correct empirical characterization of the equilibrium impact of generative-model deployment on manipulation prevalence and detection difficulty? The [Zellers et al 2019][research_zellers_et_al_2019] Grover treatment, the [Sohail et al 2024][research_sohail_et_al_2024] treatment, and subsequent work address the question, and the empirical trajectory since 2023 admits marked uncertainty in extrapolation.
- What is the correct causal characterization of the organic-establishment minority in manipulation-saturated markets, and does the minority persist under sufficiently intense manipulation or eventually collapse into the manipulation equilibrium?
- How should the platform-integrity operations, the regulatory framework, and the market response coordinate to reduce equilibrium manipulation intensity, and what is the equilibrium detection intensity that maximizes joint surplus across producer, consumer, and platform welfare?
- What is the correct comparative treatment of the American manipulation ecosystem against other national manipulation ecosystems in China, Russia, the European Union, India, Brazil, and other major markets, and how do the divergent legal, cultural, and platform-architecture conditions produce divergent equilibria?

These questions recur throughout the miniseries and are revisited in the closing synthesis.

## References

### Books

- [Applegate 2012 The Rise of Advertising in the United States][book_applegate_2012]
- [Aral 2020 The Hype Machine][book_aral_2020]
- [Ariely 2008 Predictably Irrational][book_ariely_2008]
- [Benkler Faris and Roberts 2018 Network Propaganda][book_benkler_faris_roberts_2018]
- [Bernays 1923 Crystallizing Public Opinion][book_bernays_1923]
- [Bernays 1928 Propaganda][book_bernays_1928]
- [Bourdieu 1984 Distinction][book_bourdieu_1984]
- [Buchanan and Tullock 1962 The Calculus of Consent][book_buchanan_tullock_1962]
- [Bucher 2018 If Then][book_bucher_2018]
- [Campbell 2001 Yellow Journalism][book_campbell_2001]
- [Cialdini 1984 Influence][book_cialdini_1984]
- [Coleman 1990 Foundations of Social Theory][book_coleman_1990]
- [Darnton 1982 The Literary Underground of the Old Regime][book_darnton_1982]
- [Davenport and Beck 2001 The Attention Economy][book_davenport_beck_2001]
- [Douglas 1966 Purity and Danger][book_douglas_1966]
- [Elias 1939 The Civilizing Process][book_elias_1939]
- [Ellul 1965 Propaganda The Formation of Men's Attitudes][book_ellul_1965]
- [Epstein and Prak 2008 Guilds Innovation and the European Economy][book_epstein_prak_2008]
- [Ewen 1996 PR A Social History of Spin][book_ewen_1996]
- [Farkas and Schou 2019 Post-Truth Fake News and Democracy][book_farkas_schou_2019]
- [Fisher and Fuchs 2015 Reconsidering Value and Labour in the Digital Age][book_fisher_fuchs_2015]
- [Fombrun 1996 Reputation][book_fombrun_1996]
- [Fuchs 2014 Social Media A Critical Introduction][book_fuchs_2014]
- [Fukuyama 1995 Trust][book_fukuyama_1995]
- [Gillespie 2018 Custodians of the Internet][book_gillespie_2018]
- [Goffman 1959 The Presentation of Self in Everyday Life][book_goffman_1959]
- [Goffman 1967 Interaction Ritual][book_goffman_1967]
- [Golbeck 2008 Computing with Social Trust][book_golbeck_2008]
- [Greif 2006 Institutions and the Path to the Modern Economy][book_greif_2006]
- [Habermas 1962 The Structural Transformation of the Public Sphere][book_habermas_1962]
- [Halavais 2018 Search Engine Society][book_halavais_2018]
- [Herman and Chomsky 1988 Manufacturing Consent][book_herman_chomsky_1988]
- [Hirsch 1976 Social Limits to Growth][book_hirsch_1976]
- [Jamieson 2018 Cyberwar][book_jamieson_2018]
- [Jemielniak 2014 Common Knowledge][book_jemielniak_2014]
- [Kahneman 2011 Thinking Fast and Slow][book_kahneman_2011]
- [Lasswell 1927 Propaganda Technique in the World War][book_lasswell_1927]
- [Lee 1925 Publicity][book_lee_1925]
- [Lippmann 1922 Public Opinion][book_lippmann_1922]
- [Mailath and Samuelson 2006 Repeated Games and Reputations][book_mailath_samuelson_2006]
- [Marchand 1985 Advertising the American Dream][book_marchand_1985]
- [Marwick 2013 Status Update][book_marwick_2013]
- [Mauss 1925 The Gift][book_mauss_1925]
- [Maynard Smith 1982 Evolution and the Theory of Games][book_maynard_smith_1982]
- [McGarity and Wagner 2008 Bending Science][book_mcgarity_wagner_2008]
- [Michaels 2008 Doubt Is Their Product][book_michaels_2008]
- [Milgrom 2004 Putting Auction Theory to Work][book_milgrom_2004]
- [Nasaw 2000 The Chief][book_nasaw_2000]
- [Newman 2010 Networks][book_newman_2010]
- [Nissenbaum 2010 Privacy in Context][book_nissenbaum_2010]
- [Nowak 2006 Evolutionary Dynamics][book_nowak_2006]
- [Oreskes and Conway 2010 Merchants of Doubt][book_oreskes_conway_2010]
- [Origgi 2018 Reputation What It Is and Why It Matters][book_origgi_2018]
- [Packard 1957 The Hidden Persuaders][book_packard_1957]
- [Pasley 2001 The Tyranny of Printers][book_pasley_2001]
- [Podolny 2005 Status Signals][book_podolny_2005]
- [Presbrey 1929 The History and Development of Advertising][book_presbrey_1929]
- [Putnam 2000 Bowling Alone][book_putnam_2000]
- [Rid 2020 Active Measures][book_rid_2020]
- [Roberts 2019 Behind the Screen][book_roberts_2019]
- [Sivulka 1998 Soap Sex and Cigarettes][book_sivulka_1998]
- [Solove 2007 The Future of Reputation][book_solove_2007]
- [Srnicek 2017 Platform Capitalism][book_srnicek_2017]
- [Suzor 2019 Lawless][book_suzor_2019]
- [Thaler and Sunstein 2008 Nudge][book_thaler_sunstein_2008]
- [Trivellato 2009 The Familiarity of Strangers][book_trivellato_2009]
- [Turow 2011 The Daily You][book_turow_2011]
- [Tye 1998 The Father of Spin][book_tye_1998]
- [Vaidhyanathan 2018 Antisocial Media][book_vaidhyanathan_2018]
- [Walker 2014 Grassroots for Hire][book_walker_2014]
- [Wallace-Hadrill 1989 Patronage in Ancient Society][book_wallace_hadrill_1989]
- [Warner 1990 The Letters of the Republic][book_warner_1990]
- [Weber 1922 Economy and Society][book_weber_1922]
- [Woolley 2020 The Reality Game][book_woolley_2020]
- [Wu 2016 The Attention Merchants][book_wu_2016]
- [Young 1961 The Toadstool Millionaires][book_young_1961]
- [Zipf 1949 Human Behavior and the Principle of Least Effort][book_zipf_1949]
- [Zuboff 2019 The Age of Surveillance Capitalism][book_zuboff_2019]
- [Zuckerman 2021 Mistrust][book_zuckerman_2021]

### Reference

- [15 USC 45 Federal Trade Commission Act Section 5][ref_ftc_act_15_usc_45]
- [15 USC 45b Consumer Review Fairness Act 2016][ref_consumer_review_fairness_act_2016]
- [15 USC 1125 Lanham Act Section 43a False Advertising][ref_lanham_act_15_usc_1125]
- [16 CFR Part 255 FTC Guides on Endorsements and Testimonials][ref_ftc_endorsement_guides_16_cfr_255]
- [47 USC 230 Communications Decency Act Section 230][ref_section_230_cda]
- [ACCC Fake Reviews Guidance][ref_accc_fake_reviews_guidance]
- [Amazon Community Guidelines][ref_amazon_community_guidelines]
- [Amazon Reviews Dataset][ref_amazon_reviews_dataset]
- [Amazon v Fake Review Brokers 2022][ref_amazon_v_fake_review_brokers_2022]
- [Anthropic Claude][ref_anthropic_claude]
- [Barnes v Yahoo 2009][ref_barnes_v_yahoo_2009]
- [Bentsen 1985 Congressional Record on Astroturf Lobbying][ref_bentsen_congressional_record_1985]
- [Botometer Bot Detection Database][ref_botometer]
- [Brazil Marco Civil da Internet 2014][ref_brazil_marco_civil_2014]
- [Buterin 2014 Ethereum Whitepaper][ref_buterin_2014_ethereum]
- [Byoir Papers 1930-1955][ref_byoir_1930_1955]
- [C2PA Content Provenance Standard][ref_c2pa_standard]
- [California Business and Professions Code Section 17200 Unfair Competition Law][ref_california_ucl_17200]
- [China Cyberspace Administration Deep Synthesis Regulations 2023][ref_china_cac_deepfake_2023]
- [DFRLab Reports on Coordinated Inauthentic Behavior][ref_dfrlab_reports]
- [EU AI Act Regulation 2024/1689][ref_eu_ai_act_2024]
- [EU Digital Services Act Regulation 2022/2065][ref_eu_dsa_2022]
- [EU Unfair Commercial Practices Directive 2005/29/EC][ref_eu_ucpd_2005_29_ec]
- [European Commission 2023 Sweep of Consumer Websites][ref_ec_2023_sweep]
- [Fair Housing Council v Roommates.com 2008][ref_roommates_2008]
- [Force v Facebook 2019][ref_force_v_facebook_2019]
- [FOSTA-SESTA 2018 Section 230 Amendment][ref_fosta_sesta_2018]
- [France Loi Avia 2020][ref_france_loi_avia_2020]
- [FTC 2019 Sunday Riley Settlement][ref_ftc_sunday_riley_2019]
- [FTC 2020 Fashion Nova Settlement][ref_ftc_fashion_nova_2020]
- [FTC 2022 Fake Reviews and Endorsements Notice of Penalty Offense][ref_ftc_penalty_offense_2022]
- [FTC 2024 Final Rule on Fake Reviews and Testimonials][ref_ftc_final_rule_2024]
- [FTC Endorsement Guides Frequently Asked Questions][ref_ftc_endorsement_faq]
- [FTC v Cure Encapsulations 2019][ref_ftc_cure_encapsulations_2019]
- [GAO 2020 Report on Online Consumer Reviews][ref_gao_2020_online_reviews]
- [Germany Netzwerkdurchsetzungsgesetz NetzDG 2017][ref_germany_netzdg_2017]
- [Gertz v Robert Welch 1974][ref_gertz_v_welch_1974]
- [Gonzalez v Google 2023][ref_gonzalez_v_google_2023]
- [Google Search Quality Rater Guidelines][ref_google_srg]
- [India IT Intermediary Guidelines 2021][ref_india_it_rules_2021]
- [Ivy Lee Declaration of Principles 1906][ref_ivy_lee_declaration_1906]
- [Malwarebytes v Enigma 2020][ref_malwarebytes_v_enigma_2020]
- [Meta Adversarial Threat Report][ref_meta_atr]
- [Meta Coordinated Inauthentic Behavior Policy][ref_meta_cib_policy]
- [Meta Llama][ref_meta_llama]
- [Milkovich v Lorain Journal 1990][ref_milkovich_v_lorain_1990]
- [Mueller Report 2019 Volume One][ref_mueller_report_2019]
- [Nakamoto 2008 Bitcoin Whitepaper][ref_nakamoto_2008_bitcoin]
- [New York Times v Sullivan 1964][ref_ny_times_sullivan_1964]
- [NY Attorney General People v Lifestyle Lift 2013][ref_ny_ag_lifestyle_lift_2013]
- [NY Attorney General v Devumi 2019][ref_ny_ag_devumi_2019]
- [OAIC Australian Privacy Principles][ref_oaic_australian_privacy_principles]
- [OpenAI ChatGPT 2022 Release][ref_openai_chatgpt_2022]
- [OpenAI GPT-4 2023 Release][ref_openai_gpt4_2023]
- [Reddit Transparency Report][ref_reddit_transparency_report]
- [Retraction Watch Database][ref_retraction_watch]
- [SEC v Kardashian 2022][ref_sec_kardashian_2022]
- [Singapore Protection from Online Falsehoods and Manipulation Act 2019][ref_singapore_pofma_2019]
- [Snyder v Phelps 2011][ref_snyder_v_phelps_2011]
- [Stanford Internet Observatory Data Catalog][ref_stanford_internet_observatory]
- [TikTok Community Guidelines Enforcement Report][ref_tiktok_transparency_report]
- [Twitter Election Integrity Dataset Archive][ref_twitter_election_integrity]
- [Twitter v Taamneh 2023][ref_twitter_v_taamneh_2023]
- [UK CMA Fake Reviews Action][ref_uk_cma_fake_reviews]
- [UK Online Safety Act 2023][ref_uk_online_safety_act_2023]
- [Wikipedia Signpost Archives][ref_wikipedia_signpost]
- [World Economic Forum 2021 Report on Fake Reviews][ref_wef_2021_fake_reviews]
- [Yelp Open Dataset][ref_yelp_open_dataset]
- [YouTube Community Guidelines Enforcement Report][ref_youtube_transparency_report]
- [Zeran v AOL 1997][ref_zeran_v_aol_1997]

### Research

- [Adamic and Adar 2003 Friends and Neighbors on the Web][research_adamic_adar_2003]
- [Adamic and Huberman 2000 Power-Law Distribution of the World Wide Web][research_adamic_huberman_2000]
- [Akerlof 1970 The Market for Lemons][research_akerlof_1970]
- [Athey Castillo Chandar 2019 The Allocation of Scarce Attention][research_athey_castillo_chandar_2019]
- [Ba and Pavlou 2002 Evidence of the Effect of Trust Building Technology][research_ba_pavlou_2002]
- [Balkin 2018 Free Speech is a Triangle][research_balkin_2018]
- [Banerjee 1992 A Simple Model of Herd Behavior][research_banerjee_1992]
- [Barabasi and Albert 1999 Emergence of Scaling in Random Networks][research_barabasi_albert_1999]
- [Bass 1969 A New Product Growth Model for Consumer Durables][research_bass_1969]
- [Berelson 1948 Communications and Public Opinion][research_berelson_1948]
- [Bergemann and Morris 2019 Information Design][research_bergemann_morris_2019]
- [Bessi and Ferrara 2016 Social Bots Distort the 2016 US Presidential Election][research_bessi_ferrara_2016]
- [Bikhchandani Hirshleifer Welch 1992 A Theory of Fads Fashion Custom and Cultural Change][research_bikhchandani_hirshleifer_welch_1992]
- [Bolton Katok Ockenfels 2004 How Effective Are Electronic Reputation Mechanisms][research_bolton_katok_ockenfels_2004]
- [Bradshaw Bailey Howard 2021 Industrialized Disinformation][research_bradshaw_bailey_howard_2021]
- [Bradshaw and Howard 2019 The Global Disinformation Order][research_bradshaw_howard_2019]
- [Cabral 2012 Reputation on the Internet][research_cabral_2012]
- [Chevalier and Mayzlin 2006 The Effect of Word of Mouth on Sales][research_chevalier_mayzlin_2006]
- [Cho et al 2011 Astroturfing][research_cho_et_al_2011]
- [Chu et al 2012 Detecting Automation of Twitter Accounts][research_chu_et_al_2012]
- [Craswell et al 2008 An Experimental Comparison of Click Position-Bias Models][research_craswell_et_al_2008]
- [Cresci 2020 A Decade of Social Bot Detection][research_cresci_2020]
- [Cresci et al 2017 The Paradigm-Shift of Social Spambots][research_cresci_et_al_2017]
- [Darby and Karni 1973 Free Competition and Optimal Amount of Fraud][research_darby_karni_1973]
- [Dellarocas 2003 The Digitization of Word of Mouth][research_dellarocas_2003]
- [De Micheli and Stroppa 2013 Twitter and the Underground Market][research_demicheli_stroppa_2013]
- [DiResta et al 2019 The Tactics and Tropes of the Internet Research Agency][research_diresta_et_al_2019]
- [Douek 2021 Governing Online Speech][research_douek_2021]
- [Feng et al 2021 Analyzing Fake Reviews on Google Maps][research_feng_et_al_2021]
- [Ferrara et al 2016 The Rise of Social Bots][research_ferrara_et_al_2016]
- [Fudenberg and Levine 1992 Maintaining a Reputation When Strategies Are Imperfectly Observed][research_fudenberg_levine_1992]
- [Goldstein et al 2023 Generative Language Models and Automated Influence Operations][research_goldstein_et_al_2023]
- [Granovetter 1985 Economic Action and Social Structure][research_granovetter_1985]
- [Greif 1993 Contract Enforceability and Economic Institutions in Early Trade][research_greif_1993]
- [Grinberg et al 2019 Fake News on Twitter During the 2016 US Election][research_grinberg_et_al_2019]
- [He Hollenbeck Proserpio 2022 The Market for Fake Reviews][research_he_hollenbeck_proserpio_2022]
- [Kamenica and Gentzkow 2011 Bayesian Persuasion][research_kamenica_gentzkow_2011]
- [Kirchenbauer et al 2023 A Watermark for Large Language Models][research_kirchenbauer_et_al_2023]
- [Klein and Leffler 1981 The Role of Market Forces in Assuring Contractual Performance][research_klein_leffler_1981]
- [Kleinberg 1999 Authoritative Sources in a Hyperlinked Environment][research_kleinberg_1999]
- [Kleinberg 2000 Navigation in a Small World][research_kleinberg_2000]
- [Klonick 2018 The New Governors][research_klonick_2018]
- [Konieczny 2010 Governance Adhocracy and Wikipedia][research_konieczny_2010]
- [Kreps and Wilson 1982 Reputation and Imperfect Information][research_kreps_wilson_1982]
- [Kumar et al 2017 Understanding Rating Distributions][research_kumar_et_al_2017]
- [Luca and Zervas 2016 Fake It Till You Make It][research_luca_zervas_2016]
- [Ma et al 2013 The Signaling Effect of Online Reviews][research_ma_et_al_2013]
- [Marwick and boyd 2011 I Tweet Honestly I Tweet Passionately][research_marwick_boyd_2011]
- [Marwick and Lewis 2017 Media Manipulation and Disinformation Online][research_marwick_lewis_2017]
- [Mayzlin Dover Chevalier 2014 Promotional Reviews][research_mayzlin_dover_chevalier_2014]
- [Milgrom and Roberts 1986 Price and Advertising Signals of Product Quality][research_milgrom_roberts_1986]
- [Mukherjee et al 2013 What Yelp Fake Review Filter Might Be Doing][research_mukherjee_et_al_2013]
- [Myerson 1981 Optimal Auction Design][research_myerson_1981]
- [Ott et al 2011 Finding Deceptive Opinion Spam by Any Stretch of the Imagination][research_ott_et_al_2011]
- [Page and Brin 1998 The Anatomy of a Large-Scale Hypertextual Web Search Engine][research_page_brin_1998]
- [Papakyriakopoulos et al 2020 Political Communication on Social Media][research_papakyriakopoulos_et_al_2020]
- [Pareto 1897 Cours d'Economie Politique][research_pareto_1897]
- [Persily 2017 Can Democracy Survive the Internet][research_persily_2017]
- [Rauchfleisch and Kaiser 2020 The False Positive Problem of Automatic Bot Detection][research_rauchfleisch_kaiser_2020]
- [Rayana and Akoglu 2015 Collective Opinion Spam Detection][research_rayana_akoglu_2015]
- [Resnick et al 2000 Reputation Systems][research_resnick_et_al_2000]
- [Rochet and Tirole 2003 Platform Competition in Two-Sided Markets][research_rochet_tirole_2003]
- [Rysman 2009 The Economics of Two-Sided Markets][research_rysman_2009]
- [Sadasivan et al 2023 Can AI-Generated Text be Reliably Detected][research_sadasivan_et_al_2023]
- [Salganik Dodds Watts 2006 Experimental Study of Inequality and Unpredictability][research_salganik_dodds_watts_2006]
- [Shapiro 1983 Premiums for High Quality Products][research_shapiro_1983]
- [Simon 1971 Designing Organizations for an Information-Rich World][research_simon_1971]
- [Sohail et al 2024 Detection of Large-Language-Model Generated Reviews][research_sohail_et_al_2024]
- [Spence 1973 Job Market Signaling][research_spence_1973]
- [Stigler 1971 The Theory of Economic Regulation][research_stigler_1971]
- [Tirole 1996 A Theory of Collective Reputations][research_tirole_1996]
- [Tversky and Kahneman 1974 Judgment Under Uncertainty][research_tversky_kahneman_1974]
- [Uzzi 1997 Social Structure and Competition in Interfirm Networks][research_uzzi_1997]
- [Van Noorden 2020 Nature Investigates Citation Manipulation][research_van_noorden_2020]
- [Varol et al 2017 Online Human-Bot Interactions][research_varol_et_al_2017]
- [Vosoughi Roy Aral 2018 The Spread of True and False News Online][research_vosoughi_roy_aral_2018]
- [Wardle and Derakhshan 2017 Information Disorder][research_wardle_derakhshan_2017]
- [Watts 2002 A Simple Model of Global Cascades on Random Networks][research_watts_2002]
- [Watts and Strogatz 1998 Collective Dynamics of Small-World Networks][research_watts_strogatz_1998]
- [Weyl Ohlhaver Buterin 2022 Decentralized Society][research_weyl_ohlhaver_buterin_2022]
- [Wu et al 2020 Fake Online Reviews Literature Review][research_wu_et_al_2020]
- [Yang et al 2020 Scalable and Generalizable Social Bot Detection][research_yang_et_al_2020]
- [Yang and Menczer 2024 Anatomy of an AI-Powered Malicious Social Botnet][research_yang_menczer_2024]
- [Zargham and Nabben 2022 Aligning Intent and Behavior in Web3][research_zargham_nabben_2022]
- [Zellers et al 2019 Defending Against Neural Fake News][research_zellers_et_al_2019]

[book_applegate_2012]: https://global.oup.com/academic/product/the-rise-of-advertising-in-the-united-states-9780810881785
[book_bernays_1923]: https://archive.org/details/crystallizingpub00bern
[book_bernays_1928]: https://www.igpublishing.com/product/propaganda/
[book_bourdieu_1984]: https://www.hup.harvard.edu/books/9780674212770
[book_bucher_2018]: https://global.oup.com/academic/product/if-then-9780190493028
[book_coleman_1990]: https://www.hup.harvard.edu/books/9780674312265
[book_davenport_beck_2001]: https://www.hbsp.harvard.edu/product/1789-HBK-ENG
[book_ellul_1965]: https://www.penguinrandomhouse.com/books/47269/propaganda-by-jacques-ellul/
[book_ewen_1996]: https://www.basicbooks.com/titles/stuart-ewen/pr/9780465061792/
[book_fombrun_1996]: https://www.hbsp.harvard.edu/product/6749-HBK-ENG
[book_fukuyama_1995]: https://www.simonandschuster.com/books/Trust/Francis-Fukuyama/9780684825250
[book_gillespie_2018]: https://yalebooks.yale.edu/book/9780300235029/custodians-of-the-internet/
[book_goffman_1959]: https://www.penguinrandomhouse.com/books/168265/the-presentation-of-self-in-everyday-life-by-erving-goffman/
[book_halavais_2018]: https://www.wiley.com/en-us/Search+Engine+Society%2C+2nd+Edition-p-9781509518906
[book_herman_chomsky_1988]: https://www.penguinrandomhouse.com/books/288363/manufacturing-consent-by-edward-s-herman-and-noam-chomsky/
[book_hirsch_1976]: https://www.hup.harvard.edu/books/9780674812901
[book_jemielniak_2014]: https://www.sup.org/books/title/?id=23054
[book_lasswell_1927]: https://mitpress.mit.edu/9780262620185/propaganda-technique-in-world-war-i/
[book_lee_1925]: https://archive.org/details/publicity00leei
[book_lippmann_1922]: https://www.simonandschuster.com/books/Public-Opinion/Walter-Lippmann/9781416573104
[book_mailath_samuelson_2006]: https://global.oup.com/academic/product/repeated-games-and-reputations-9780195300796
[book_mcgarity_wagner_2008]: https://www.hup.harvard.edu/books/9780674047143
[book_michaels_2008]: https://global.oup.com/academic/product/doubt-is-their-product-9780195300673
[book_oreskes_conway_2010]: https://www.bloomsbury.com/us/merchants-of-doubt-9781608193943/
[book_origgi_2018]: https://press.princeton.edu/books/hardcover/9780691175355/reputation
[book_packard_1957]: https://ighland-books.com/hidden-persuaders
[book_podolny_2005]: https://press.princeton.edu/books/paperback/9780691134253/status-signals
[book_presbrey_1929]: https://archive.org/details/historyanddevelo00pres
[book_putnam_2000]: https://www.simonandschuster.com/books/Bowling-Alone/Robert-D-Putnam/9780743203043
[book_rid_2020]: https://us.macmillan.com/books/9780374287269/activemeasures
[book_srnicek_2017]: https://www.wiley.com/en-us/Platform+Capitalism-p-9781509504879
[book_turow_2011]: https://yalebooks.yale.edu/book/9780300188011/the-daily-you/
[book_tye_1998]: https://www.penguinrandomhouse.com/books/153822/the-father-of-spin-by-larry-tye/
[book_vaidhyanathan_2018]: https://global.oup.com/academic/product/antisocial-media-9780190841164
[book_walker_2014]: https://www.cambridge.org/9781107619012
[book_wu_2016]: https://www.penguinrandomhouse.com/books/232292/the-attention-merchants-by-tim-wu/
[book_young_1961]: https://press.princeton.edu/books/paperback/9780691623429/the-toadstool-millionaires
[book_zipf_1949]: https://archive.org/details/humanbehaviorpri0000zipf
[book_zuboff_2019]: https://www.publicaffairsbooks.com/titles/shoshana-zuboff/the-age-of-surveillance-capitalism/9781610395694/
[ref_accc_fake_reviews_guidance]: https://www.accc.gov.au/business/advertising-and-promotions/online-reviews
[ref_amazon_community_guidelines]: https://www.amazon.com/gp/help/customer/display.html?nodeId=GLHXEX85MENUE4XF
[ref_amazon_reviews_dataset]: https://amazon-reviews-2023.github.io/
[ref_amazon_v_fake_review_brokers_2022]: https://www.aboutamazon.com/news/policy-news-views/amazon-continues-legal-action-against-fake-review-brokers
[ref_bentsen_congressional_record_1985]: https://www.congress.gov/congressional-record
[ref_botometer]: https://botometer.osome.iu.edu/
[ref_byoir_1930_1955]: https://briscoecenter.org/collections/carl-byoir/
[ref_california_ucl_17200]: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=17200
[ref_consumer_review_fairness_act_2016]: https://www.law.cornell.edu/uscode/text/15/45b
[ref_dfrlab_reports]: https://dfrlab.org/
[ref_ec_2023_sweep]: https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/sweeps_en
[ref_eu_ai_act_2024]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689
[ref_eu_dsa_2022]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2065
[ref_eu_ucpd_2005_29_ec]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32005L0029
[ref_ftc_act_15_usc_45]: https://www.law.cornell.edu/uscode/text/15/45
[ref_ftc_cure_encapsulations_2019]: https://www.ftc.gov/legal-library/browse/cases-proceedings/172-3117-cure-encapsulations-inc
[ref_ftc_endorsement_faq]: https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking
[ref_ftc_endorsement_guides_16_cfr_255]: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255
[ref_ftc_fashion_nova_2020]: https://www.ftc.gov/legal-library/browse/cases-proceedings/192-3138-fashion-nova-llc
[ref_ftc_final_rule_2024]: https://www.ftc.gov/legal-library/browse/federal-register-notices/16-cfr-part-465-rule-use-consumer-reviews-testimonials
[ref_ftc_penalty_offense_2022]: https://www.ftc.gov/legal-library/browse/notices-penalty-offenses-concerning-money-making-opportunities-endorsements-reviews-testimonials
[ref_ftc_sunday_riley_2019]: https://www.ftc.gov/legal-library/browse/cases-proceedings/1723065-sunday-riley-modern-skincare-llc
[ref_gao_2020_online_reviews]: https://www.gao.gov/products/gao-20-660
[ref_google_srg]: https://services.google.com/fh/files/misc/hsw-sqrg.pdf
[ref_ivy_lee_declaration_1906]: https://www.prsa.org/about/ethics/
[ref_lanham_act_15_usc_1125]: https://www.law.cornell.edu/uscode/text/15/1125
[ref_meta_atr]: https://about.fb.com/news/tag/adversarial-threat-report/
[ref_meta_cib_policy]: https://transparency.meta.com/policies/community-standards/inauthentic-behavior/
[ref_mueller_report_2019]: https://www.justice.gov/archives/sco/file/1373816/download
[ref_ny_ag_devumi_2019]: https://ag.ny.gov/press-release/2019/attorney-general-james-announces-groundbreaking-settlement-devumi-owner-german
[ref_ny_ag_lifestyle_lift_2013]: https://ag.ny.gov/press-release/2013/ag-schneiderman-announces-agreement-19-companies-cease-writing-fake-online-reviews
[ref_oaic_australian_privacy_principles]: https://www.oaic.gov.au/privacy/australian-privacy-principles
[ref_reddit_transparency_report]: https://www.redditinc.com/policies/transparency-report
[ref_retraction_watch]: https://retractionwatch.com/
[ref_sec_kardashian_2022]: https://www.sec.gov/news/press-release/2022-183
[ref_section_230_cda]: https://www.law.cornell.edu/uscode/text/47/230
[ref_stanford_internet_observatory]: https://cyber.fsi.stanford.edu/io
[ref_tiktok_transparency_report]: https://www.tiktok.com/transparency/en/community-guidelines-enforcement/
[ref_twitter_election_integrity]: https://transparency.twitter.com/en/reports/moderation-research.html
[ref_uk_cma_fake_reviews]: https://www.gov.uk/government/collections/fake-online-reviews-cma-action
[ref_uk_online_safety_act_2023]: https://www.legislation.gov.uk/ukpga/2023/50/contents
[ref_wef_2021_fake_reviews]: https://www.weforum.org/agenda/2021/07/fake-online-reviews-are-a-25-billion-problem/
[ref_wikipedia_signpost]: https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost
[ref_yelp_open_dataset]: https://www.yelp.com/dataset
[ref_youtube_transparency_report]: https://transparencyreport.google.com/youtube-policy/removals
[research_adamic_huberman_2000]: https://firstmonday.org/ojs/index.php/fm/article/view/1298
[research_akerlof_1970]: https://academic.oup.com/qje/article/84/3/488/1896241
[research_athey_castillo_chandar_2019]: https://www.nber.org/papers/w26346
[research_ba_pavlou_2002]: https://www.jstor.org/stable/4132332
[research_bass_1969]: https://pubsonline.informs.org/doi/10.1287/mnsc.15.5.215
[research_berelson_1948]: https://www.jstor.org/stable/2745835
[research_bolton_katok_ockenfels_2004]: https://pubsonline.informs.org/doi/10.1287/mnsc.1030.0199
[research_bradshaw_howard_2019]: https://demtech.oii.ox.ac.uk/research/posts/the-global-disinformation-order-2019-global-inventory-of-organised-social-media-manipulation/
[research_cabral_2012]: https://academic.oup.com/oxrep/article/28/4/730/436538
[research_chevalier_mayzlin_2006]: https://www.jstor.org/stable/30162548
[research_cho_et_al_2011]: https://journals.sagepub.com/doi/10.1177/0894439310396571
[research_craswell_et_al_2008]: https://dl.acm.org/doi/10.1145/1341531.1341545
[research_darby_karni_1973]: https://www.jstor.org/stable/725058
[research_dellarocas_2003]: https://pubsonline.informs.org/doi/10.1287/mnsc.49.10.1407.17308
[research_demicheli_stroppa_2013]: https://arxiv.org/abs/1309.7889
[research_diresta_et_al_2019]: https://digitalcommons.unl.edu/senatedocs/2/
[research_feng_et_al_2021]: https://arxiv.org/abs/2109.05939
[research_ferrara_et_al_2016]: https://dl.acm.org/doi/10.1145/2818717
[research_fudenberg_levine_1992]: https://www.jstor.org/stable/2298058
[research_he_hollenbeck_proserpio_2022]: https://pubsonline.informs.org/doi/10.1287/mksc.2022.1353
[research_klein_leffler_1981]: https://www.jstor.org/stable/1837524
[research_konieczny_2010]: https://journals.sagepub.com/doi/10.1177/1461444809342738
[research_kreps_wilson_1982]: https://www.jstor.org/stable/1912538
[research_luca_zervas_2016]: https://pubsonline.informs.org/doi/10.1287/mnsc.2015.2304
[research_ma_et_al_2013]: https://misq.umn.edu/the-signaling-effect-of-online-reviews.html
[research_mayzlin_dover_chevalier_2014]: https://www.aeaweb.org/articles?id=10.1257/aer.104.8.2421
[research_milgrom_roberts_1986]: https://www.jstor.org/stable/1833272
[research_papakyriakopoulos_et_al_2020]: https://dl.acm.org/doi/10.1145/3392866
[research_pareto_1897]: https://archive.org/details/coursdeconomiep00pare
[research_resnick_et_al_2000]: https://dl.acm.org/doi/10.1145/355112.355122
[research_rochet_tirole_2003]: https://www.jstor.org/stable/40005933
[research_rysman_2009]: https://www.aeaweb.org/articles?id=10.1257/jep.23.3.125
[research_shapiro_1983]: https://academic.oup.com/qje/article/98/4/659/1873941
[research_simon_1971]: https://digitalcollections.library.cmu.edu/awweb/awarchive?type=file&item=33748
[research_sohail_et_al_2024]: https://arxiv.org/abs/2402.01697
[research_spence_1973]: https://academic.oup.com/qje/article/87/3/355/1885359
[research_tirole_1996]: https://academic.oup.com/restud/article/63/1/1/1567526
[research_van_noorden_2020]: https://www.nature.com/articles/d41586-020-02218-3
[research_vosoughi_roy_aral_2018]: https://www.science.org/doi/10.1126/science.aap9559
[research_wu_et_al_2020]: https://www.sciencedirect.com/science/article/pii/S014829631930464X
[research_zellers_et_al_2019]: https://arxiv.org/abs/1905.12616
[book_aral_2020]: https://us.macmillan.com/books/9780525574514/thehypemachine
[book_ariely_2008]: https://www.harpercollins.com/products/predictably-irrational-revised-and-expanded-edition-dan-ariely
[book_benkler_faris_roberts_2018]: https://global.oup.com/academic/product/network-propaganda-9780190923624
[book_buchanan_tullock_1962]: https://oll.libertyfund.org/titles/buchanan-the-calculus-of-consent-logical-foundations-of-constitutional-democracy
[book_campbell_2001]: https://www.abc-clio.com/products/a4152p/
[book_cialdini_1984]: https://www.harpercollins.com/products/influence-new-and-expanded-robert-b-cialdini-phd
[book_darnton_1982]: https://www.hup.harvard.edu/books/9780674536579
[book_douglas_1966]: https://www.routledge.com/Purity-and-Danger-An-Analysis-of-Concepts-of-Pollution-and-Taboo/Douglas/p/book/9780415289955
[book_elias_1939]: https://www.wiley.com/en-us/The+Civilizing+Process%3A+Sociogenetic+and+Psychogenetic+Investigations%2C+Revised+Edition-p-9780631221616
[book_epstein_prak_2008]: https://www.cambridge.org/9780521887175
[book_farkas_schou_2019]: https://www.routledge.com/Post-Truth-Fake-News-and-Democracy-Mapping-the-Politics-of-Falsehood/Farkas-Schou/p/book/9781138336773
[book_fisher_fuchs_2015]: https://link.springer.com/book/10.1057/9781137478573
[book_fuchs_2014]: https://uk.sagepub.com/en-gb/eur/social-media/book282566
[book_goffman_1967]: https://www.penguinrandomhouse.com/books/168266/interaction-ritual-by-erving-goffman/
[book_golbeck_2008]: https://link.springer.com/book/10.1007/978-3-540-92803-0
[book_greif_2006]: https://www.cambridge.org/9780521671347
[book_habermas_1962]: https://mitpress.mit.edu/9780262581080/the-structural-transformation-of-the-public-sphere/
[book_jamieson_2018]: https://global.oup.com/academic/product/cyberwar-9780190058838
[book_kahneman_2011]: https://us.macmillan.com/books/9780374533557/thinkingfastandslow
[book_marchand_1985]: https://www.ucpress.edu/book/9780520050914/advertising-the-american-dream
[book_marwick_2013]: https://yalebooks.yale.edu/book/9780300209389/status-update/
[book_mauss_1925]: https://wwnorton.com/books/9780393320435
[book_maynard_smith_1982]: https://www.cambridge.org/9780521288842
[book_milgrom_2004]: https://www.cambridge.org/9780521536721
[book_nasaw_2000]: https://www.hmhbooks.com/shop/books/The-Chief/9780618154463
[book_newman_2010]: https://global.oup.com/academic/product/networks-9780198805090
[book_nissenbaum_2010]: https://www.sup.org/books/title/?id=8862
[book_nowak_2006]: https://www.hup.harvard.edu/books/9780674023383
[book_pasley_2001]: https://www.upress.virginia.edu/title/2260
[book_roberts_2019]: https://yalebooks.yale.edu/book/9780300235883/behind-the-screen/
[book_sivulka_1998]: https://www.wadsworth.com/marketing_d/course_products/0534506933
[book_solove_2007]: https://yalebooks.yale.edu/book/9780300144222/the-future-of-reputation/
[book_suzor_2019]: https://www.cambridge.org/9781108408271
[book_thaler_sunstein_2008]: https://yalebooks.yale.edu/book/9780300122237/nudge/
[book_trivellato_2009]: https://yalebooks.yale.edu/book/9780300172416/the-familiarity-of-strangers/
[book_wallace_hadrill_1989]: https://www.routledge.com/Patronage-in-Ancient-Society/Wallace-Hadrill/p/book/9780415034418
[book_warner_1990]: https://www.hup.harvard.edu/books/9780674526136
[book_weber_1922]: https://www.ucpress.edu/book/9780520035003/economy-and-society
[book_woolley_2020]: https://www.hachettebookgroup.com/titles/samuel-woolley/the-reality-game/9781541768253/
[book_zuckerman_2021]: https://wwnorton.com/books/9781324002505
[ref_anthropic_claude]: https://www.anthropic.com/claude
[ref_barnes_v_yahoo_2009]: https://cdn.ca9.uscourts.gov/datastore/opinions/2009/06/22/05-36189.pdf
[ref_brazil_marco_civil_2014]: https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm
[ref_buterin_2014_ethereum]: https://ethereum.org/en/whitepaper/
[ref_c2pa_standard]: https://c2pa.org/specifications/specifications/1.4/index.html
[ref_china_cac_deepfake_2023]: https://www.chinalawtranslate.com/en/deep-synthesis/
[ref_force_v_facebook_2019]: https://www.ca2.uscourts.gov/decisions/isysquery/2c50f8ea-4b6f-4c0f-b8ec-92f6c2d80a26/1/doc/18-397_opn.pdf
[ref_fosta_sesta_2018]: https://www.congress.gov/bill/115th-congress/house-bill/1865
[ref_france_loi_avia_2020]: https://www.legifrance.gouv.fr/loda/id/JORFTEXT000042031970/
[ref_germany_netzdg_2017]: https://www.gesetze-im-internet.de/netzdg/
[ref_gertz_v_welch_1974]: https://supreme.justia.com/cases/federal/us/418/323/
[ref_gonzalez_v_google_2023]: https://www.supremecourt.gov/opinions/22pdf/21-1333_6j7a.pdf
[ref_india_it_rules_2021]: https://www.meity.gov.in/content/notification-dated-25th-february-2021-gsr-139e-information-technology-intermediary
[ref_malwarebytes_v_enigma_2020]: https://www.supremecourt.gov/opinions/20pdf/19-1284_869d.pdf
[ref_meta_llama]: https://ai.meta.com/llama/
[ref_milkovich_v_lorain_1990]: https://supreme.justia.com/cases/federal/us/497/1/
[ref_nakamoto_2008_bitcoin]: https://bitcoin.org/bitcoin.pdf
[ref_ny_times_sullivan_1964]: https://supreme.justia.com/cases/federal/us/376/254/
[ref_openai_chatgpt_2022]: https://openai.com/index/chatgpt/
[ref_openai_gpt4_2023]: https://openai.com/index/gpt-4-research/
[ref_roommates_2008]: https://cdn.ca9.uscourts.gov/datastore/opinions/2008/04/03/0456916.pdf
[ref_singapore_pofma_2019]: https://sso.agc.gov.sg/Act/POFMA2019
[ref_snyder_v_phelps_2011]: https://supreme.justia.com/cases/federal/us/562/443/
[ref_twitter_v_taamneh_2023]: https://www.supremecourt.gov/opinions/22pdf/21-1496_d18f.pdf
[ref_zeran_v_aol_1997]: https://law.justia.com/cases/federal/appellate-courts/F3/129/327/565056/
[research_adamic_adar_2003]: https://www.sciencedirect.com/science/article/abs/pii/S0378873303000091
[research_balkin_2018]: https://www.uclawreview.org/2018/12/free-speech-is-a-triangle/
[research_banerjee_1992]: https://academic.oup.com/qje/article-abstract/107/3/797/1873015
[research_barabasi_albert_1999]: https://www.science.org/doi/10.1126/science.286.5439.509
[research_bergemann_morris_2019]: https://www.aeaweb.org/articles?id=10.1257/jel.20181489
[research_bessi_ferrara_2016]: https://firstmonday.org/ojs/index.php/fm/article/view/7090
[research_bikhchandani_hirshleifer_welch_1992]: https://www.jstor.org/stable/2138632
[research_bradshaw_bailey_howard_2021]: https://demtech.oii.ox.ac.uk/research/posts/industrialized-disinformation/
[research_chu_et_al_2012]: https://ieeexplore.ieee.org/document/6280553
[research_cresci_2020]: https://cacm.acm.org/magazines/2020/10/247594-a-decade-of-social-bot-detection/
[research_cresci_et_al_2017]: https://dl.acm.org/doi/10.1145/3041021.3055135
[research_douek_2021]: https://harvardlawreview.org/2021/06/governing-online-speech-from-posts-as-trumps-to-proportionality-and-probability/
[research_goldstein_et_al_2023]: https://arxiv.org/abs/2301.04246
[research_granovetter_1985]: https://www.jstor.org/stable/2780199
[research_greif_1993]: https://www.jstor.org/stable/2117532
[research_grinberg_et_al_2019]: https://www.science.org/doi/10.1126/science.aau2706
[research_kamenica_gentzkow_2011]: https://www.aeaweb.org/articles?id=10.1257/aer.101.6.2590
[research_kirchenbauer_et_al_2023]: https://arxiv.org/abs/2301.10226
[research_kleinberg_1999]: https://dl.acm.org/doi/10.1145/324133.324140
[research_kleinberg_2000]: https://www.nature.com/articles/35022643
[research_klonick_2018]: https://harvardlawreview.org/2018/04/the-new-governors-the-people-rules-and-processes-governing-online-speech/
[research_kumar_et_al_2017]: https://cs.stanford.edu/~srijan/pubs/rev2-wsdm18.pdf
[research_marwick_boyd_2011]: https://journals.sagepub.com/doi/10.1177/1461444810365313
[research_marwick_lewis_2017]: https://datasociety.net/library/media-manipulation-and-disinfo-online/
[research_mukherjee_et_al_2013]: https://ojs.aaai.org/index.php/ICWSM/article/view/14380
[research_myerson_1981]: https://pubsonline.informs.org/doi/10.1287/moor.6.1.58
[research_ott_et_al_2011]: https://aclanthology.org/P11-1032/
[research_page_brin_1998]: http://infolab.stanford.edu/~backrub/google.html
[research_persily_2017]: https://www.journalofdemocracy.org/articles/can-democracy-survive-the-internet/
[research_rauchfleisch_kaiser_2020]: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0241045
[research_rayana_akoglu_2015]: https://dl.acm.org/doi/10.1145/2783258.2783370
[research_sadasivan_et_al_2023]: https://arxiv.org/abs/2303.11156
[research_salganik_dodds_watts_2006]: https://www.science.org/doi/10.1126/science.1121066
[research_stigler_1971]: https://www.jstor.org/stable/3003160
[research_tversky_kahneman_1974]: https://www.science.org/doi/10.1126/science.185.4157.1124
[research_uzzi_1997]: https://www.jstor.org/stable/2393808
[research_varol_et_al_2017]: https://ojs.aaai.org/index.php/ICWSM/article/view/14871
[research_wardle_derakhshan_2017]: https://rm.coe.int/information-disorder-report-november-2017/1680764666
[research_watts_2002]: https://www.pnas.org/doi/10.1073/pnas.082090499
[research_watts_strogatz_1998]: https://www.nature.com/articles/30918
[research_weyl_ohlhaver_buterin_2022]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763
[research_yang_et_al_2020]: https://onlinelibrary.wiley.com/doi/10.1002/hbe2.115
[research_yang_menczer_2024]: https://arxiv.org/abs/2307.16336
[research_zargham_nabben_2022]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4077249
