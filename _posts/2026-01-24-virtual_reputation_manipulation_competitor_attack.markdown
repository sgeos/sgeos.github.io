---
layout: post
mathjax: true
comments: true
title:  "Virtual Reputation Manipulation: Techniques of Competitor Attack"
date:   2026-01-24 00:00:00 +0000
categories: economics technology sociology
series: virtual_reputation_manipulation
series_title: Virtual Reputation Manipulation
series_index: 3
---

<!-- A279 -->
<script>console.log("A279");</script>

This article is the third in a four-article miniseries treating virtual reputation manipulation as a first-class analytical object. The opening article at [Virtual Reputation Manipulation Theory and Analytical Framework][related_post_a277_theory] established the economic-signaling framework and the six-axis analytical framework the miniseries applies. The second article at [Virtual Reputation Manipulation Techniques of Self-Promotion][related_post_a278_self_promotion] cataloged the technique classes oriented at inflating the actor's own reputation. The present article catalogs the technique classes of competitor-attack oriented reputation manipulation, characterizes each along the six-axis framework, surveys the documented enforcement cases and the academic detection literature, and identifies the detection signatures and legal recourse each technique admits. The treatment is descriptive-analytical rather than operational. The material is organized for detection engineers, platform integrity teams, legal practitioners, and academic researchers rather than for readers seeking operational manipulation guidance, and where a technique permits both descriptive and operational specification the treatment stops at the descriptive level. The closing article treats the detection, countermeasure, and organic-establishment landscape that responds to both self-promotion and competitor-attack techniques.

## The Competitor-Attack Taxonomy

Competitor-attack oriented reputation manipulation refers to the class of techniques by which an actor injects unfavorable reputation signal about a competitor, rival, or targeted third party into a reputation system with the intent of degrading that party's reputation. The class is distinguished from self-promotion oriented manipulation treated in the preceding article by the direction of the intended reputation shift and by the resulting differences in technique inventory, detection signature, legal exposure, and market effect. Competitor-attack techniques are less prevalent than self-promotion techniques across most reputation ecosystems but carry considerably higher per-incident legal exposure due to the direct intersection with defamation law, unfair-competition doctrine, and the intermediary-liability regime.

The technique landscape allows partition into several groupings organized by the attack vector each technique class exploits. The review-signal attack group includes individual negative review fabrication, coordinated review bombing, cross-account downvoting, and generative-model-produced negative content. The brigading and cross-community attack group includes cross-community brigading, coordinated dogpiling, and raid organization patterns. The negative-search-engine-optimization group includes toxic backlink attacks, duplicate content attacks, malicious redirect injection, sitemap poisoning, and algorithm exploitation. The defamation-campaign group includes false-content publication, anonymous defamation, coordinated defamation networks, and search-engine-amplified defamation. The Sybil-attack-downvoting group includes vote manipulation on community platforms, rating attacks, and community-vote weaponization. The reporting-system-weaponization group includes false DMCA takedowns, trademark abuse, coordinated abuse reporting, and platform-integrity system abuse. The complaint-farm-services group includes Better Business Bureau complaint farms, negative-review farms, consumer-complaint-site abuse, and government-complaint weaponization. The adversarial-content-operations group includes negative-topic association, coordinated pile-on operations, and social-media harassment coordination. The cross-platform-coordinated-negative group cuts across the other groupings and represents the most substantial recent operational development.

The technique-space partition supports compact formalization along the same axis-vector framework introduced for self-promotion. Let $\mathcal{T}^{\text{attack}} = \{t_1, t_2, \ldots, t_K\}$ denote the competitor-attack technique inventory, and let each technique be characterized by its position on the six analytical axes,

$$\mathbf{a}_k = (a_k^{\text{signal}}, a_k^{\text{obj}}, a_k^{\text{struct}}, a_k^{\text{model}}, a_k^{\text{interact}}, a_k^{\text{adapt}})$$

with each axis value drawn from an axis-specific space. The distance between competitor-attack techniques takes the same characterization as the self-promotion case,

$$d(t_j, t_k) = \sum_{c \in \text{axes}} w_c \, \delta_c(a_j^c, a_k^c)$$

with $w_c$ the axis weight and $\delta_c$ the axis-specific distance function.

The critical analytical difference from the self-promotion technique inventory lies on the objective axis. Self-promotion techniques optimize for the actor's own reputation-score uplift; competitor-attack techniques optimize for the target's reputation-score decrement, admitting characterization as

$$U^{\text{attack}}(\mathbf{x}) = -\lambda^{\text{rating}}_T g_{\text{rating}}(x_T) - \lambda^{\text{rank}}_T g_{\text{rank}}(x_T) - \lambda^{\text{engage}}_T g_{\text{engage}}(x_T) + \gamma_{\text{self}}(x_A)$$

with $x_T$ the target's state, $x_A$ the attacker's state, and $\gamma_{\text{self}}$ any residual self-effect. The competitive-differential benefit to the attacker follows

$$\Delta_{\text{competitive}}(t) = R_A(t) - R_T(t) - [R_A(0) - R_T(0)]$$

with $R_A$ and $R_T$ the reputations of attacker and target and $t = 0$ the pre-attack baseline. The competitive-differential formulation makes clear that competitor-attack manipulation can produce competitive benefit without directly manipulating the attacker's own reputation signal, which distinguishes the objective structure from the self-promotion case.

The aggregate empirical prevalence of competitor-attack techniques across the reputation ecosystem admits estimation through the sum

$$V_{\text{attack}}(t) = \sum_{k \in \mathcal{T}^{\text{attack}}} \sum_{c \in \text{categories}} n_{k,c}(t) \cdot p_{k,c}(t)$$

with $n_{k,c}(t)$ and $p_{k,c}(t)$ defined as for the self-promotion case. The empirical estimates surveyed in this article establish that $V_{\text{attack}}$ is significantly smaller than $V_{\text{self-promo}}$ across most consumer-facing platform categories, but that attack-heavy contexts (competitive-market subsegments, political-adjacent commercial contests, controversy-adjacent public figures) exhibit competitor-attack volume comparable to or exceeding self-promotion volume in those subsegments.

## Cross-Disciplinary Framings

The competitor-attack phenomenon permits characterization from several disciplinary traditions beyond the economic-signaling framework the miniseries adopts as primary. The framing article surveys the alternative disciplinary treatments and identifies their analytical leverage.

The economics-of-competition and antitrust framing treats competitor-attack manipulation as a form of exclusionary conduct that reduces competitive market efficiency. The [Bork 1978][book_bork_1978] The Antitrust Paradox and [Posner 2001][book_posner_2001] Antitrust Law treatments frame exclusionary conduct within the consumer-welfare framework. The [Melamed 2006][research_melamed_2006] and [Elhauge 2003][research_elhauge_2003] frameworks develop the exclusionary-conduct doctrine that applies to reputation-manipulation-adjacent competitive tactics. The predatory-conduct framework from [Areeda and Turner 1975][research_areeda_turner_1975] adapts to reputation attacks via the sacrifice-versus-legitimate-competition test. The economics-of-competition framing complements the reputation-manipulation framing by treating the attack as a competitive-market intervention with implications for market structure and consumer welfare beyond the direct target's reputation harm.

The tort-law framing traces from the [Prosser and Keeton 1984][book_prosser_keeton_1984] Handbook of the Law of Torts through the [Restatement Second of Torts 1977][ref_restatement_second_torts] on defamation and tortious interference. The tort framing treats competitor-attack as actionable civil wrong subject to damages recovery, with the elements varying by tort category (defamation, false light, tortious interference with business relations, tortious interference with prospective economic advantage, injurious falsehood). The [Franklin Anderson and Cate 2016][book_franklin_anderson_cate_2016] Mass Media Law treatment consolidates the modern doctrinal treatment. The tort framing provides the primary US-law analytical structure for the private-action recourse landscape.

The critical-harassment-studies framing traces from [Kelly 1988][book_kelly_1988] Surviving Sexual Violence establishing the continuum-of-violence framework that maps onto online-harassment operations, through [Herring 2002][research_herring_2002] Cyber Violence Recognizing and Resisting Abuse in Online Environments, [Jane 2014][research_jane_2014] Your a Ugly Whorish Slut on the gendered dimensions of online harassment, [Citron 2014][book_citron_2014] Hate Crimes in Cyberspace on the legal-and-policy framework, and [Franks 2019][book_franks_2019] The Cult of the Constitution on the broader speech-and-harassment doctrine. The critical-harassment framing emphasizes the gendered and marginalized-population-targeting patterns of competitor-attack operations that the neutral economic framing may obscure.

The computer-science-and-adversarial-machine-learning framing traces from [Goodfellow Shlens Szegedy 2014][research_goodfellow_shlens_szegedy_2014] Explaining and Harnessing Adversarial Examples through the [Szegedy et al 2013][research_szegedy_et_al_2013] Intriguing Properties of Neural Networks and subsequent adversarial-ML literature. The framing treats platform-detection systems as classifiers subject to adversarial-example attacks in which the attacker crafts inputs designed to evade or mislead the detection classifier. The [Papernot et al 2016][research_papernot_et_al_2016] Practical Black-Box Attacks against Machine Learning treatment applies the adversarial-ML framework to detection-evasion. The [Carlini and Wagner 2017][research_carlini_wagner_2017] Towards Evaluating the Robustness of Neural Networks treatment establishes the state-of-the-art adversarial-example generation. The adversarial-ML framing complements the reputation-manipulation framing by treating the attacker-detector dynamic as an adversarial-example generation-and-defense problem with algorithmic implications for detector design.

The network-science and cascade-dynamics framing traces from [Watts 2002][research_watts_2002] A Simple Model of Global Cascades on Random Networks through [Barabási and Albert 1999][research_barabasi_albert_1999] Emergence of Scaling in Random Networks and subsequent network-dynamics literature. The framing treats competitor-attack propagation as a cascade on the target's audience network, with the cascade characteristics shaped by network topology and threshold-crossing dynamics. The [Chandrasekharan et al 2017][research_chandrasekharan_et_al_2017] treatment applies the cascade framework to hate-community migration after community-ban events. The [Kwak Lee Park Moon 2010][research_kwak_lee_park_moon_2010] treatment analyzes Twitter cascade dynamics applicable to attack-content propagation. The network-science framing complements the reputation-manipulation framing by identifying the network-topology and threshold-dynamics conditions under which attack operations achieve significant cascade amplification versus fizzling.

The platform-governance and information-law framing traces from [Balkin 2018][research_balkin_2018] Free Speech is a Triangle through [Klonick 2018][research_klonick_2018] The New Governors, [Douek 2021][research_douek_2021] Governing Online Speech, and [Grimmelmann 2015][research_grimmelmann_2015] The Virtues of Moderation. The framing treats the platform's role as private governor of speech and reputation as itself a distinct object of analysis subject to accountability and legitimacy concerns. The [Sunstein 2018][book_sunstein_2018] Republic Divided Democracy in the Age of Social Media treatment addresses the systemic democratic-institution consequences of platform-mediated attack operations. The platform-governance framing complements the technique-specific framing by treating the platform as a governance actor rather than as a neutral infrastructure provider.

## Historical Antecedents

Competitor-attack reputation manipulation is not a novel phenomenon of the digital era. The technique inventory inherits substantial doctrine, practice, and organizational form from pre-digital antecedents in defamation practice, negative campaigning, corporate warfare, and information operations. The framing article surveys the principal historical antecedents and identifies the continuities and discontinuities with the digital-era inventory.

The pre-industrial antecedents include the medieval and early-modern practice of defamation-through-print, with the [Loveland 2000][book_loveland_2000] Political Libels A Comparative Study documenting the origins of Anglo-American defamation law in seventeenth-century political-libel practice. The [Rosenberg 1986][book_rosenberg_1986] Protecting the Best Men Origins of the Law of Libel treatment addresses the development of libel-law protection for reputation. The [Siebert 1965][book_siebert_1965] Freedom of the Press in England 1476-1776 traces the parallel emergence of press regulation and defamation doctrine. The pre-industrial antecedents include the dueling tradition as an extra-legal reputation-defense-and-attack mechanism, documented in [Kiernan 1988][book_kiernan_1988] The Duel in European History, with the shift from personal-honor dueling to legal-defamation recourse marking one of the major reputation-law transitions of the eighteenth and nineteenth centuries.

The nineteenth-century mass-newspaper era produced marked competitor-attack activity between rival newspapers and rival politicians. The [Baldasty 1992][book_baldasty_1992] The Commercialization of News in the Nineteenth Century documents the transition to competitive commercial journalism. The [Nasaw 2000][book_nasaw_2000] The Chief biography of William Randolph Hearst documents the coordinated attack operations of the yellow-journalism era. The [Boorstin 1961][book_boorstin_1961] The Image treatment addresses the emergence of pseudo-event manufacture in the pre-electronic media environment. The [Wills 1970][book_wills_1970] Nixon Agonistes treatment addresses the negative-campaigning tradition in American political practice from the mid-twentieth century.

The Cold War era produced the extensive evolution of state-sponsored competitor-attack operations. The [Rid 2020][book_rid_2020] Active Measures treatment documents the Soviet-era active-measures campaigns and their evolution into contemporary Russian information operations. The [Weiner 2007][book_weiner_2007] Legacy of Ashes The History of the CIA addresses the parallel US-side operations. The [Andrew and Mitrokhin 1999][book_andrew_mitrokhin_1999] The Sword and the Shield provides the Soviet-archive-based documentation. The Cold War state-operation infrastructure established organizational forms and technique templates that transferred into the contemporary state-sponsored digital-attack operations.

The late-twentieth-century negative-political-advertising era produced sizable technique innovation in the mass-media-mediated attack. The [Ansolabehere and Iyengar 1996][book_ansolabehere_iyengar_1996] Going Negative empirical study of negative advertising effects, the [Geer 2006][book_geer_2006] In Defense of Negativity treatment of the democratic function of negative campaigning, and the [Mark 2006][book_mark_2006] Going Dirty History of Negative Campaigning consolidate the historical and empirical analysis. The [Willie Horton 1988 attack ad][ref_willie_horton_1988] represents one of the reference-case attack operations of the era. The [Swift Boat Veterans for Truth 2004][ref_swift_boat_2004] operation represents the transition from broadcast-era negative advertising to the emerging internet-era coordinated attack. The [birther conspiracy campaign 2008-2016][ref_birther_campaign] represents the fully-internet-era attack operation.

The corporate competitor-attack antecedents include documented cases from tobacco, chemical, and pharmaceutical industries. The [Oreskes and Conway 2010][book_oreskes_conway_2010] Merchants of Doubt treatment documents the coordinated denial campaigns that included direct attacks on scientific critics. The [Michaels 2020][book_michaels_2020] The Triumph of Doubt updates the treatment through the 2010s. The [Michaels 2008][book_michaels_2008] Doubt Is Their Product documents the earlier corporate playbook. The corporate-attack antecedents established the coordination-with-plausible-deniability infrastructure that carries into contemporary corporate reputation-attack operations.

## Historiographical Gap and Recent Scholarship

The scholarly treatment of competitor-attack reputation manipulation has developed unevenly across disciplines and has integrated less well across traditions than the self-promotion literature. The framing article surveys the observable gap and identifies the recent-scholarship developments that the miniseries builds on.

The defamation-law scholarship developed continuously from the [Prosser 1960][research_prosser_1960] Privacy Law framework through the [Post 1986][research_post_1986] The Social Foundations of Defamation Law treatment and the modern-era [Anderson 1991][research_anderson_1991] Reputation Compensation Punishment Suppression analysis. The [Franks 2019][book_franks_2019] Cult of the Constitution and the [Citron 2014][book_citron_2014] Hate Crimes in Cyberspace treatments represent the contemporary reform-oriented scholarship. The gap between the classical-tort framework and the platform-mediated attack environment remains substantially unbridged in the doctrinal literature, with courts applying pre-internet defamation frameworks to attack operations that exhibit markedly different scale and coordination structure.

The empirical-attack-detection literature developed through the same computer-science-detection tradition surveyed for self-promotion. The competitor-attack detection literature includes [Kumar et al 2018][research_kumar_et_al_2018] on Reddit brigading, [Chandrasekharan et al 2017][research_chandrasekharan_et_al_2017] on hate-community-ban effects, [Hine et al 2017][research_hine_et_al_2017] on 4chan raid operations, [Zannettou et al 2018][research_zannettou_et_al_2018_reddit_4chan] on cross-platform coordinated behavior, [Ribeiro et al 2020][research_ribeiro_et_al_2020] on YouTube radicalization pathways, [Marwick and Caplan 2018][research_marwick_caplan_2018] on gendered harassment, and [Lewis 2018][research_lewis_2018] on alternative influence networks. The empirical literature has developed primarily around large-community-platform brigading and harassment operations, with less coverage of the specifically-commercial competitor-attack operations that the miniseries treats.

The platform-governance scholarship developed through the [Klonick 2018][research_klonick_2018], [Balkin 2018][research_balkin_2018], [Douek 2021][research_douek_2021], and [Grimmelmann 2015][research_grimmelmann_2015] treatments surveyed above. The application to competitor-attack response is less developed than the general content-moderation treatment, with the attack-oriented moderation challenges (target-notification, evidence-preservation, cross-platform coordination) remaining under-treated relative to the general moderation-scale challenges.

The adversarial-machine-learning literature developed through the [Goodfellow et al 2014][research_goodfellow_shlens_szegedy_2014], [Carlini and Wagner 2017][research_carlini_wagner_2017], and [Papernot et al 2016][research_papernot_et_al_2016] treatments surveyed above. The application of the adversarial-ML framework to reputation-attack detection is emerging but not yet consolidated in a reference treatment.

The historiographical gap that the miniseries addresses lies in the absence of an integrated treatment that draws on the economics-of-competition, tort-law, harassment-studies, computer-science-detection, network-science, and platform-governance traditions simultaneously. Each tradition treats a portion of the competitor-attack phenomenon, and the standard treatment requires all six. The miniseries organizes the material to make the cross-tradition connections explicit where they are load-bearing for the analytical conclusions.

## Review-Signal Attack Techniques

The review-signal attack class comprises the technique inventory oriented at injecting unfavorable review content into a reputation system to degrade a target's aggregate rating and to influence prospective consumer decisions against the target. The class is the empirically dominant competitor-attack class in consumer-review platforms and has received appreciable academic detection attention through the general fake-review detection literature that treats attack-oriented and self-promotion-oriented fabrication under the same detection methodology.

### Individual Negative Review Fabrication

Individual negative review fabrication operates analogously to individual positive fabrication treated in the preceding article, with the direction of the intended rating shift reversed. Documented cases include the [Yelp v Hadeed Carpet Cleaning 2014][ref_yelp_v_hadeed_2014] litigation over Yelp's disclosure of anonymous reviewer identities in a defamation action, the [FTC v Roomster 2022][ref_ftc_roomster_2022] action addressing a rental-platform's use of fake reviews (which included both self-promotion and competitor-attack elements), and the [Amazon v ThinkExpress 2022][ref_amazon_v_thinkexpress_2022] private action addressing coordinated negative-review injection. The [Reit-Nightingale v Universal 2019][ref_reit_nightingale_v_universal_2019] deepfake-defamation case illustrates the adjacent legal frontier where synthetic content produces false negative reviews or testimonials.

The [FTC v Amazon 2023][ref_ftc_v_amazon_2023] action addressed adjacent dark-pattern manipulation practices and provides the reference federal enforcement precedent applicable to platform-mediated reputation manipulation. The rating-shift model for individual negative-review fabrication mirrors the positive-fabrication case,

$$\Delta r_i^{\text{obs}} = \Delta r_i^{\text{authentic}} - n_i^{\text{fake-neg}} \cdot (\bar{r}_{\text{pre}} - \bar{r}_{\text{fake-neg}}) / (N_i + n_i^{\text{fake-neg}})$$

with $n_i^{\text{fake-neg}}$ the injected fake-negative-review count, $\bar{r}_{\text{fake-neg}}$ the average fake-negative-review rating (typically one or two stars), $\bar{r}_{\text{pre}}$ the pre-injection average rating, and $N_i$ the pre-injection authentic-review count. The equation shows that fake-negative-review effectiveness is higher against targets with fewer authentic reviews and against targets with higher pre-injection averages (larger gap between $\bar{r}_{\text{pre}}$ and $\bar{r}_{\text{fake-neg}}$).

The detection signatures for individual negative fabrication include the same stylometric, temporal, reviewer-history, and IP-and-device-fingerprint anomalies documented for positive fabrication in the [Ott et al 2011][research_ott_et_al_2011], [Feng et al 2012][research_feng_et_al_2012], and subsequent detection literature. The attack-oriented signature includes the anomaly of a reviewer whose review history disproportionately concentrates on negative reviews of one or a small set of businesses in the target category, which allows characterization as the concentration ratio

$$C_{\text{reviewer}}^{\text{neg}} = \frac{|\{r : \text{reviewer}(r) = R \wedge \text{rating}(r) \leq 2\}|}{|\{r : \text{reviewer}(r) = R\}|}$$

with reviewers exhibiting anomalously high $C^{\text{neg}}$ triggering attack-oriented-manipulation classification. Detection triggers when $C^{\text{neg}}$ exceeds a threshold typically set at $C^{\text{neg}} > 0.8$ against a category-baseline distribution. The reviewer-target-concentration variant identifies the target-specific attack pattern via

$$C_{\text{reviewer}}^{\text{target}}(R, T) = \frac{|\{r : \text{reviewer}(r) = R \wedge \text{target}(r) = T \wedge \text{rating}(r) \leq 2\}|}{|\{r : \text{reviewer}(r) = R\}|}$$

with anomalously high values across a target-and-competitor set triggering coordinated-attack classification. The [Ott et al 2013][research_ott_et_al_2013] Negative Deceptive Opinion Spam treatment establishes the negative-review detection framework.

### Coordinated Review Bombing

Review bombing refers to the coordinated deposit of large volumes of negative reviews against a target within a short time window, typically triggered by an event unrelated to the target's product quality (political controversy, culture-war conflict, brand-adjacent event). The technique has been documented most extensively on [Metacritic][ref_metacritic_review_bombing] and [Rotten Tomatoes][ref_rt_review_bombing], both of which have implemented platform-side countermeasures including review-verification requirements and post-release rating windows. The [Amazon review bombing incidents][ref_amazon_review_bombing_cases] have targeted books, products, and services associated with political controversy. The [Goodreads review bombing][ref_goodreads_review_bombing] pattern has targeted authors during publication controversies.

The empirical characterization of review-bombing arrivals has the Hawkes point process framework with anomalous self-excitation gain

$$\lambda^{\text{bomb}}(t) = \mu + \alpha^{\text{bomb}} \sum_{t_i < t} e^{-\beta(t - t_i)}$$

with $\alpha^{\text{bomb}} \gg \alpha^{\text{baseline}}$ during the bombing event. The detection threshold triggers when the observed $\alpha$ exceeds the null-model distribution by a factor typically set at $\alpha / \alpha_{\text{null}} > 10$. The [Kalpakis et al 2001][research_kalpakis_et_al_2001] framework for temporal anomaly detection provides the general methodology, and the [Vasilescu and Casanueva 2016][research_vasilescu_casanueva_2016] treatment addresses the review-bombing detection problem.

The rating-distribution shape during a review-bombing event exhibits characteristic bimodality with a spike at the extreme-negative rating (one star or equivalent) that the null-distribution would not produce. The bimodality statistic supports characterization via the Hartigan dip test

$$D_{\text{dip}}(F) = \sup_x |F(x) - U(x)|$$

with $F$ the empirical rating-distribution and $U$ the closest unimodal distribution; anomalous $D_{\text{dip}}$ triggers review-bombing classification. The [Hartigan and Hartigan 1985][research_hartigan_hartigan_1985] statistic provides the reference framework.

Coordinated review-bombing detection benefits from the coordination signature that individual-fabrication detection lacks. The coordination signature includes cross-account temporal alignment, cross-account content-template reuse, and cross-account external-origin signature (accounts originating from the same coordinating community). The coordinated-community-origin detection statistic operates on the fraction of bombing accounts with prior activity on external coordinating platforms,

$$\rho_{\text{external-coord}} = \frac{|\{r : \text{reviewer}(r) \text{ active on coord platform}\}|}{|\{r \in \text{bombing event}\}|}$$

with coordination-driven bombings exhibiting appreciably higher $\rho^{\text{external-coord}}$ than natural-negative-review events. Cross-account temporal alignment takes the form the pairwise timestamp-cluster tightness

$$T_{\text{align}}(\text{event}) = \frac{1}{|\text{event}|(|\text{event}|-1)} \sum_{i \neq j} \mathbb{1}[|t_i - t_j| < \Delta t_{\text{coord}}]$$

with $\Delta t_{\text{coord}}$ a coordination-window threshold typically set at $\Delta t_{\text{coord}} = 3600$ seconds. Content-template reuse is captured by the average pairwise text similarity across the bombing-event review set,

$$\bar{S}_{\text{content}}(\text{event}) = \frac{2}{n(n-1)} \sum_{i<j} \text{sim}(r_i, r_j)$$

with anomalously high $\bar{S}_{\text{content}}$ indicating shared-template origin. The [Kumar et al 2018][research_kumar_et_al_2018] Community Interaction and Conflict on the Web treatment provides the reference framework for cross-community brigading detection applicable to coordinated review bombing.

### Cross-Account Downvoting

Cross-account downvoting operates on platforms that expose per-review helpfulness or usefulness voting, where a coordinated operation upvotes negative reviews of a target and downvotes positive reviews to shift the visible review distribution presented to prospective consumers. The technique has been documented on Amazon, Yelp, and Tripadvisor where the review-ordering algorithm gives weight to helpfulness votes. The [Amazon Community Guidelines][ref_amazon_community_guidelines] explicitly prohibit coordinated voting on reviews.

The vote-shift metric characterizing the technique admits characterization as

$$\Delta v_r^{\text{net}} = \Delta v_r^{\text{authentic}} + n_r^{\text{coord-up}} - n_r^{\text{coord-down}}$$

with $\Delta v_r^{\text{net}}$ the net vote change on review $r$, $\Delta v_r^{\text{authentic}}$ the authentic vote change, and $n_r^{\text{coord-up}}$ and $n_r^{\text{coord-down}}$ the coordinated upvote and downvote injection counts. The equation shows that a small coordinated operation can produce considerable vote-differential shifts on individual reviews absent detection. The ranking-impact function mapping vote-differential to review-ordering-position shift takes the platform-specific form

$$\Delta \text{pos}(r) = -\eta \cdot \Delta v_r^{\text{net}} / \sqrt{v_r^{\text{total}}}$$

approximately, with $\eta$ the ranking-sensitivity coefficient and $v_r^{\text{total}}$ the total vote count on $r$. The vote-injection cost per unit ranking-shift depends on the marketplace price per coordinated vote and the platform's baseline-vote density.

### Generative-Model-Produced Negative Content

The generative-model transition has enabled significant scale-up of negative-review production at collapsed marginal cost. The attack-narrative prompt-space takes the form a distribution over adversarial prompt templates

$$\pi_{\text{attack-prompt}}(x) = \sum_k w_k \, p_k(x)$$

with $p_k(x)$ the template-specific prompt distribution and $w_k$ template mixing weights that shape the diversity-versus-effectiveness tradeoff. The same detection challenges documented for positive-review generative content apply to negative-review generative content, with the additional dimension that generative models can be prompted to produce attack narratives targeting particular competitor attributes. The [Yang and Menczer 2024][research_yang_menczer_2024] Anatomy of an AI-Powered Malicious Social Botnet documents contemporary AI-driven botnet operations that engage in both self-promotion and competitor-attack activity. The [Goldstein et al 2023][research_goldstein_et_al_2023] Generative Language Models and Automated Influence Operations treatment surveys the emerging threat landscape.

The attack-oriented cost function takes the same collapsed-convexity characterization as the self-promotion case,

$$c_{\text{LLM-attack}}(m) \approx c_{\text{API}} \cdot m + c_{\text{prompt-eng}}$$

with the additional prompt-engineering cost typically higher for attack-oriented content that must be tuned to produce plausible-but-damaging attribute-specific attacks on the target. The detection-difficulty asymptote under high-quality generation matches the self-promotion case,

$$\text{AUC}_{\text{detect}}(q_{\text{gen}}) \to 0.5 \text{ as } q_{\text{gen}} \to q_{\text{human}}$$

per the [Sadasivan et al 2023][research_sadasivan_et_al_2023] analysis.

## Brigading and Cross-Community Attack

Brigading refers to the coordinated deposit of engagement (upvotes, downvotes, comments, reports) against a target from participants originating in an external community that has organized the operation. The technique class differs from ordinary coordinated inauthentic behavior in that the participating accounts are typically authentic (rather than sockpuppet or Sybil) but the participants are acting under coordination from an external community rather than through independent judgment.

### Cross-Community Brigading

Cross-community brigading operates through the movement of participants from a source community (typically a subreddit, chan-adjacent board, private chat channel, or organized discussion group) to a target community or platform where they engage in the coordinated action. The [Kumar et al 2018][research_kumar_et_al_2018] Community Interaction and Conflict on the Web treatment provides the foundational large-scale analysis of Reddit cross-community mobilization, characterizing the population dynamics of source-target community interactions. The [Chandrasekharan et al 2017][research_chandrasekharan_et_al_2017] You Can't Stay Here treatment analyzes the case of hate-community mobilization and the platform-side effect of banning source communities. The [Hine et al 2017][research_hine_et_al_2017] Kek Cucks and God Emperor Trump treatment analyzes the 4chan/pol/-originating brigading operations. The [Zannettou et al 2018][research_zannettou_et_al_2018_reddit_4chan] Web-Wide Coordinated Behavior treatment analyzes the cross-platform brigading dynamic between Reddit and 4chan.

The cross-community brigading detection statistic operates on the source-community-origin fraction of participants in a target-community event,

$$\rho_{\text{brigade}}^{S \to T}(e) = \frac{|\{p \in e : \text{prior activity in } S\}|}{|\{p \in e\}|}$$

with $e$ the target-community event and $S$ the source community. Brigading events exhibit anomalously high $\rho^{\text{brigade}}$ compared to the target-community's baseline participant distribution. The mobilization threshold for a brigading event reduces to the source-community mobilization ratio,

$$m_S(t) = \frac{|\text{S-participants active on target at } t|}{|\text{S-active-users at } t|}$$

with brigading events exhibiting $m_S$ greatly above the baseline cross-community-activity rate. The source-target participant overlap can be characterized as the Jaccard similarity of participant sets across an event window,

$$J(S, T, w) = \frac{|P_S(w) \cap P_T(w)|}{|P_S(w) \cup P_T(w)|}$$

with $P_S(w)$ and $P_T(w)$ the active-participant sets on source community $S$ and target community $T$ during window $w$. Brigading events exhibit considerably elevated $J(S, T, w)$ compared to the baseline cross-community overlap.

### Coordinated Dogpiling

Coordinated dogpiling refers to the attack pattern in which a coordinated group of participants respond to a target's content with a high-volume stream of negative responses (replies, comments, quote-shares) within a short time window. The technique is particularly effective on real-time social-media platforms where the response-volume itself produces cascading amplification through the platform's ranking algorithm. The empirical documentation of dogpiling includes the [Gamergate coordinated harassment operations 2014-2015][ref_gamergate_coverage] and subsequent similar operations documented in [Marwick and Caplan 2018][research_marwick_caplan_2018] and [Lewis 2018][research_lewis_2018].

The pile-on rate statistic is captured by the response-arrival rate against a target,

$$\lambda_{\text{pile-on}}(t) = \frac{d N_{\text{response}}(t)}{dt}$$

with dogpiling events exhibiting $\lambda_{\text{pile-on}}$ significantly above the target's baseline response-rate. The participant-diversity statistic distinguishes coordinated dogpiling from natural viral response by the anomalous concentration of pile-on participants in coordinating communities. The participant-diversity entropy over source-community assignments reduces to

$$H_{\text{part-diversity}}(\text{event}) = -\sum_{C \in \text{communities}} p_C \log p_C$$

with $p_C$ the fraction of pile-on participants originating from community $C$. Coordinated dogpiling exhibits anomalously low $H_{\text{part-diversity}}$ concentrated on one or a small number of source communities, distinguishing it from natural viral responses that exhibit distributed source-community origin.

### Raid Organization Patterns

Raid organization patterns refer to the coordination structures through which brigading and dogpiling operations are organized. Documented raid-organization patterns include the [4chan raid coordination framework][ref_4chan_raid_documentation], the [Discord server-based coordination][ref_discord_coordination_reports], and the [Telegram channel-based coordination][ref_telegram_coordination_reports] that has expanded since 2020. The [Marwick 2013][book_marwick_2013] Status Update treatment provides the sociological framing. The [Phillips 2015][book_phillips_2015] This is Why We Can't Have Nice Things treatment analyzes the online-harassment-community formation.

Detection of raid-organization patterns operates through the analysis of the external-coordination signal: private-channel invocation of a target followed by coordinated on-platform action against that target. The detection challenge is substantial because the coordination signal is generally not observable to the target platform, and cross-platform detection requires platform-integrity coordination between the coordinating platform (typically not the target platform) and the target platform. The [Ribeiro et al 2020][research_ribeiro_et_al_2020] Auditing Radicalization Pathways on YouTube treatment provides the reference empirical framework for cross-community-to-target-platform radicalization-and-attack-mobilization pathways.

## Negative Search-Engine Optimization

Negative search-engine optimization (negative SEO or reverse SEO) refers to the class of techniques oriented at degrading a target's search-ranking position on major search engines. The techniques operate through the same PageRank-and-ranking-algorithm mechanisms exploited by aggressive SEO for self-promotion, with the sign of the intended ranking shift reversed. The class overlaps substantially with the self-promotion SEO class but includes attack-oriented technique subsets treated below.

### Toxic Backlink Attacks

Toxic backlink attacks operate by generating large volumes of low-quality inbound links to the target site from spammy, penalized, or malware-associated source domains, with the intent of triggering Google's spam-penalty algorithms against the target. The technique exploits the [Google 2012 Penguin algorithm update][ref_google_penguin_2012] and subsequent algorithm evolution which penalize sites for unnatural inbound-link patterns.

The PageRank-damage from a toxic backlink follows approximately the negative-contribution form

$$\Delta \text{PR}(p) \approx -\sum_{q \in B_p^{\text{toxic}}} d \cdot \text{penalty}(q) \cdot \text{PR}(q) / L(q)$$

with $B_p^{\text{toxic}}$ the toxic inbound-link set and $\text{penalty}(q)$ the platform-imposed penalty multiplier on links from source $q$. The empirical penalty effect depends on the algorithm's classification of the source as spammy and on the target's total inbound-link volume. The [Google Disavow Tool][ref_google_disavow_tool] provides the target-site countermeasure allowing site owners to instruct Google to ignore specified inbound links.

The toxic-link identification statistic operates on the source-domain characteristics including spam-score, malware-association, penalty-history, and cross-target link-farm participation. The composite toxicity score can be characterized as the weighted sum

$$T(q) = w_1 \cdot \text{SpamScore}(q) + w_2 \cdot \text{MalwareFlag}(q) + w_3 \cdot \text{PenaltyHistory}(q) + w_4 \cdot \text{LinkFarmParticipation}(q)$$

with the weights $w_1, \ldots, w_4$ trained on labeled toxic-versus-benign link sets. Disavow-tool effectiveness permits characterization as the fraction of nominated toxic links the search engine subsequently ignores in ranking computations,

$$e_{\text{disavow}} = \frac{|\{q \in \text{disavowed} : \text{ignored in PR}\}|}{|\text{disavowed}|}$$

with empirical estimates from case studies placing $e_{\text{disavow}}$ in the range of 0.7 to 0.9 for major search engines. The [Moz Spam Score methodology][ref_moz_spam_score] provides one industry-standard classification framework. The [Ahrefs Domain Rating framework][ref_ahrefs_domain_rating] provides an alternative industry framework.

### Duplicate Content Attacks

Duplicate content attacks operate by publishing large volumes of scraped copies of the target's original content on external sites, with the intent of triggering Google's duplicate-content algorithms against the target. The technique exploits the [Google 2011 Panda algorithm update][ref_google_panda_2011] which reduced the ranking weight of sites with marked duplicate content.

The content-similarity statistic characterizing duplicate content has the form the cosine similarity of document embeddings,

$$\text{sim}(d_1, d_2) = \frac{\mathbf{v}_1 \cdot \mathbf{v}_2}{\|\mathbf{v}_1\| \|\mathbf{v}_2\|}$$

with $\mathbf{v}_i$ the document embedding. Duplicate-content triggers occur when the similarity exceeds a threshold typically set at $\text{sim} > 0.85$. The canonical-URL confusion signature emerges when the search engine's canonicalization algorithm assigns the canonical version to a duplicate rather than to the original, admitting detection via the canonical-URL-assignment audit. The originality-priority statistic under first-publication timestamps takes the form

$$\text{orig}(d) = \mathbb{1}[t_d = \min_{d' : \text{sim}(d, d') > \tau} t_{d'}]$$

with $t_d$ the first-publication timestamp of document $d$; the canonical-assignment collision occurs when $\text{orig}(d) = 1$ but the search engine's canonicalization instead selects a duplicate as canonical.

### Malicious Redirect Injection

Malicious redirect injection operates through exploitation of the target site's vulnerabilities to inject redirect code that sends visitors (or search-engine crawlers) to malicious or spam destinations. The technique produces search-engine penalties against the target site for hosting redirect-based spam. The [Google Safe Browsing][ref_google_safe_browsing] and [Google Search Console malware notification][ref_google_search_console_malware] infrastructures provide the platform-side detection framework.

### Sitemap Poisoning and Crawl-Path Manipulation

Sitemap poisoning operates through the injection of unauthorized URLs into a target site's sitemap or through the manipulation of the target's robots.txt to cause search-engine crawlers to indexed inappropriate content or fail to index appropriate content. The technique requires exploitation-level access to the target site's infrastructure or configuration files. The detection operates through the site-owner-side monitoring of unexpected sitemap or robots.txt changes.

### Google Algorithm Exploitation

The broader class of negative-SEO techniques exploits algorithm characteristics of the target search engine. The [Google Search Central spam policies][ref_google_search_spam_policies] enumerate the platform-recognized manipulation techniques and provide the reference taxonomy from Google's perspective. The [Google Webmaster Guidelines penalty framework][ref_google_manual_actions] documents the manual-action penalty types the platform imposes. The negative-SEO effectiveness depends on the attack producing a signal that triggers algorithmic or manual penalty against the target without producing a signal that identifies the attack as external-to-target manipulation. The [Cyveillance 2015 Reverse SEO Report][ref_cyveillance_2015_reverse_seo] provides one industry-side survey of the technique landscape.

## Defamation Campaigns

Defamation campaigns operate through the publication of false statements damaging to the target's reputation. The technique class intersects directly with defamation law in the United States and with parallel doctrines in other jurisdictions, which produces the highest per-incident legal exposure of any reputation-manipulation technique class.

### False Content Publication

False content publication produces damaging false statements about the target on platforms where the content is accessible to the target's audience. The technique can operate through review platforms (fake reviews containing false factual claims), social media (posts containing false claims), blogs and websites (long-form defamatory content), or news-adjacent platforms (fake news articles). The [New York Times v Sullivan 1964][ref_ny_times_sullivan_1964] framework establishes the actual-malice standard for public-figure defamation, and the [Gertz v Robert Welch 1974][ref_gertz_v_welch_1974] framework extends to private figures. The [Milkovich v Lorain Journal 1990][ref_milkovich_v_lorain_1990] framework distinguishes statements of fact from statements of opinion.

The defamation-classification of a statement $s$ under US law requires four elements: publication, identification of the target, defamatory content (false statement of fact), and damages. The statement's actionability has the form

$$A(s) = \mathbb{1}[\text{published}] \cdot \mathbb{1}[\text{identifies target}] \cdot \mathbb{1}[\text{false fact}] \cdot \mathbb{1}[\text{damages}]$$

with the additional actual-malice requirement for public figures adding $\mathbb{1}[\text{knowledge or reckless disregard of falsity}]$. The damages calculation for a defamation action is described by the sum of special damages (pecuniary losses), general damages (reputational harm), presumed damages (for defamation per se categories), and punitive damages,

$$D_{\text{total}} = D_{\text{special}} + D_{\text{general}} + D_{\text{presumed}} + D_{\text{punitive}}$$

with the characterization varying by jurisdiction and case type.

Documented defamation cases involving digital-platform manipulation include [Zeran v AOL 1997][ref_zeran_v_aol_1997] on early Section 230 immunity, [Batzel v Smith 2003][ref_batzel_v_smith_2003] on selective republication and immunity, [Barnes v Yahoo 2009][ref_barnes_v_yahoo_2009] on promissory-estoppel exception to immunity, [Doe v MySpace 2008][ref_doe_v_myspace_2008] on Section 230 immunity limits in physical-harm cases, [Fair Housing Council v Roommates.com 2008][ref_roommates_2008] on platform-created content, [Nemet Chevrolet v Consumeraffairs.com 2009][ref_nemet_v_consumeraffairs_2009] on the immunity boundary for consumer-review platforms, [Klayman v Zuckerberg 2014][ref_klayman_v_zuckerberg_2014] on platform-side immunity from user-generated attack content, [Herrick v Grindr 2019][ref_herrick_v_grindr_2019] on impersonation-facilitation immunity, and the more recent [Force v Facebook 2019][ref_force_v_facebook_2019] and [Gonzalez v Google 2023][ref_gonzalez_v_google_2023] decisions addressing algorithmic-recommendation liability. The [Zervos v Trump 2017-2022][ref_zervos_v_trump] litigation illustrates the modern high-profile defamation case involving public-figure targets and social-media platforms. Additional contemporary defamation cases include the [Sarah Palin v NYT 2022][ref_palin_v_nyt_2022] action addressing actual-malice standards in political defamation, the [Cardi B v Kebe 2022][ref_cardi_b_v_kebe_2022] case addressing YouTube-mediated defamation with a jury verdict against the defendant, the [E Jean Carroll v Trump 2023][ref_carroll_v_trump_2023] defamation-and-battery action, and the [Amber Heard v Depp 2022][ref_heard_v_depp_2022] cross-defamation action. The [Bartnicki v Vopper 2001][ref_bartnicki_v_vopper_2001] First Amendment framework establishes limits on defamation-adjacent liability for third-party republication.

### Anonymous Defamation

Anonymous defamation operates through the publication of defamatory content by an operator whose identity is not readily apparent. The technique complicates legal recourse because the target must first unmask the anonymous poster before pursuing defamation claims. The unmasking procedure typically requires a subpoena to the hosting platform to obtain the poster's identifying information, subject to the platform's willingness to comply and the applicable law's protection of anonymous speech.

The unmasking-order likelihood takes the form the conditional probability

$$\Pr(\text{unmask granted} \mid \text{motion}) = f(\text{prima facie showing}, \text{jurisdiction}, \text{platform}, \text{content type})$$

with the parameters varying by court and case type. The cost of unmasking including legal fees, subpoena costs, and platform-cooperation friction is captured by

$$C_{\text{unmask}}(J) = C_{\text{legal}}(J) + C_{\text{subpoena}}(J) + C_{\text{platform}}(J) + C_{\text{delay}}(J)$$

with $J$ the jurisdiction and each cost component varying across jurisdictions. Multi-jurisdiction attacks that route through anonymizing infrastructure raise $C_{\text{unmask}}$ markedly through the addition of international cooperation requirements. The [Dendrite v Doe 2001][ref_dendrite_v_doe_2001] framework in New Jersey and the [Cahill v Doe 2005][ref_cahill_v_doe_2005] framework in Delaware establish the reference tests for unmasking-motion grants. The [Doe v Cahill][ref_cahill_v_doe_2005] test requires the plaintiff to make a prima facie case that would survive summary judgment before the anonymous poster can be unmasked.

### Coordinated Defamation Networks

Coordinated defamation networks operate through the deployment of multiple defamatory-content-publishing accounts and sites under coordinated control to amplify the reputation damage against the target. The technique combines the defamation-per-instance framework with the coordinated-inauthentic-behavior framework treated in the preceding article. Documented cases include the [FTC v Roomster 2022][ref_ftc_roomster_2022] action addressing coordinated deceptive reviews, and several state-level actions against organized defamation-for-hire services.

The network-damage aggregation follows

$$D_{\text{net}}(T) = \sum_{i \in \text{content}} d_i(T) \cdot v_i \cdot p_i$$

with $d_i(T)$ the per-content-instance damage to target $T$, $v_i$ the visibility of the content, and $p_i$ the persistence of the content. Coordinated networks achieve appreciably higher $D_{\text{net}}$ than individual publication due to the multiplicative visibility and persistence effects. The campaign-timeline characterization follows the piecewise-linear phase structure

$$D_{\text{net}}(t) = \begin{cases} \alpha_1 t & 0 \leq t < t_{\text{peak}} \\ D_{\text{peak}} + \alpha_2 (t - t_{\text{peak}}) & t_{\text{peak}} \leq t < t_{\text{decay}} \\ D_{\text{peak}} \cdot e^{-\gamma (t - t_{\text{decay}})} & t \geq t_{\text{decay}} \end{cases}$$

with $\alpha_1$ the buildup rate, $\alpha_2$ the sustain rate (typically small), and $\gamma$ the post-campaign decay rate.

### Search-Engine-Amplified Defamation

Search-engine-amplified defamation operates through the technique of publishing defamatory content optimized to rank highly for search queries associated with the target's name, business, or brand. The technique combines the defamation-content-publication framework with the aggressive-SEO framework to produce content that appears prominently in searches for the target and displaces legitimate content about the target from the visible search results. The [rank-displacement effect][research_ravasi_et_al_2020] allows characterization as the number of legitimate results displaced from the visible search-result page,

$$N_{\text{displaced}} = |\{r \in \text{top-K}_{\text{legitimate}} : r \notin \text{top-K}_{\text{observed}}\}|$$

with top-$K$ typically set at $K = 10$ for the first-page results. Search-engine-amplified defamation produces disproportionate reputation damage relative to non-amplified defamation because the amplified content reaches a broader audience through the search-mediated discovery channel. The reputation-damage-from-displacement reduces to the integral over displaced-content visibility loss

$$D_{\text{displace}}(T) = \int_0^{\infty} v_{\text{legit}}(r, t) \cdot \bigl(1 - \mathbb{1}[r \text{ visible at } t]\bigr) \, dr \, dt$$

with $v_{\text{legit}}(r, t)$ the counterfactual visibility of legitimate content on target $T$ absent the displacement attack. Recovery from displacement after successful content removal follows the exponential regrowth

$$R^{\text{recovered}}(t) = R_0 \cdot (1 - e^{-\gamma_{\text{recover}} t})$$

with $\gamma_{\text{recover}}$ the recovery rate typically constrained by search-engine reindexing cadence. The [Right to be Forgotten framework in EU law][ref_right_to_be_forgotten_eu] provides one recourse mechanism for search-amplification-related reputation harm.

## Sybil-Attack Downvoting

Sybil-attack downvoting operates through the deployment of Sybil-network infrastructure oriented at producing coordinated downvotes, negative ratings, or negative engagement against a target. The technique differs from ordinary Sybil-based self-promotion in the direction of the intended reputation shift and in the detection signatures that differ between upvote-heavy and downvote-heavy Sybil operations.

### Vote Manipulation on Community Platforms

Community platforms including Reddit, Stack Exchange, Wikipedia, and Quora expose vote-based ranking signals that Sybil operations target. The [Reddit vote manipulation policy][ref_reddit_vote_manipulation_policy] establishes the platform's response framework. The [Wikipedia sockpuppet investigations][ref_wikipedia_spi] provide the standing documentation of vote-and-edit manipulation on that platform.

The vote-manipulation impact function on a target's community-visible ranking follows

$$\Delta \text{rank}(T) = f(\Delta v_T^{\text{net}}, N_{\text{competition}}, \text{ranking algo})$$

with $\Delta v_T^{\text{net}}$ the net vote change on the target, $N_{\text{competition}}$ the count of competing content, and the ranking algorithm parametrization. Under the Hot-ranking family of algorithms including the Reddit legacy Hot algorithm the ranking-score-impact function takes the log-shifted form

$$\Delta s = \text{sign}(\Delta v^{\text{net}}) \cdot \log_{10}(1 + |\Delta v^{\text{net}}|) / T_{\text{decay}}$$

with $T_{\text{decay}}$ a time-decay divisor. The Sybil-attack effectiveness depends on both the Sybil-vote volume and the temporal-clustering of the votes, which shifts the target's position in the platform's time-weighted ranking algorithm.

### Rating Attacks

Rating attacks refer to the general class of Sybil-based negative-rating deposition against products, services, businesses, or content. The techniques operate through the same infrastructure as Sybil-based positive-rating self-promotion, with the direction of the injected ratings reversed. The detection signatures include the same account-provenance, temporal-clustering, and behavioral-similarity signatures documented for the self-promotion case in the preceding article. The negative-rating-shift model mirrors the positive-attack case with the additional characterization of the target's authentic-rating-distribution shape as the reference baseline for the anomaly-detection null hypothesis,

$$D_{\text{KL}}(\hat{F}_{\text{observed}} \| F_{\text{authentic-baseline}}) > \tau_{\text{anomaly}}$$

with $D_{\text{KL}}$ the Kullback-Leibler divergence and $\tau_{\text{anomaly}}$ a chosen detection threshold. Sybil-attack rating events produce extensive rating-distribution divergence from the target's authentic-baseline distribution.

### Community-Vote Weaponization

Community-vote weaponization operates through the deployment of Sybil infrastructure to trigger community-level enforcement actions against a target. The technique exploits the platform's use of user-vote signals as inputs to automated moderation decisions, with the goal of triggering false-positive moderation actions (post removal, account suspension) against the target. The weighted-voting anomaly detection statistic is described by the participation-vote ratio,

$$\rho_{\text{part-vote}}^{\text{Sybil}} = \frac{N_{\text{Sybil votes on target}}}{N_{\text{authentic votes on target}}}$$

with Sybil-attack triggering events exhibiting anomalously high $\rho^{\text{part-vote}}$.

## Reporting-System Weaponization

Reporting-system weaponization refers to the class of techniques that abuse platform abuse-reporting infrastructure to trigger enforcement against a target that is not in fact violating platform policies. The technique class exploits the platform's tendency to weight user-report volume as a signal in automated moderation decisions and to accept user-report content at face value in many enforcement pathways.

### False DMCA Takedowns

The Digital Millennium Copyright Act at [17 USC 512][ref_dmca_17_usc_512] establishes the notice-and-takedown framework under which service providers receive safe-harbor protection in exchange for prompt takedown of content upon receipt of a copyright-infringement notice from the rights-holder. The framework has been documented as subject to weaponization through false-notice submission by parties without valid copyright claims, with the intent of removing target content that the party wishes suppressed. The [Lenz v Universal 2015][ref_lenz_v_universal_2015] "dancing baby" case established the requirement that DMCA-notice-senders consider fair use before submission. The [Online Policy Group v Diebold 2004][ref_diebold_2004] case addressed the pattern of DMCA misuse to suppress critical content. Additional DMCA case law includes [Perfect 10 v CCBill 2007][ref_perfect_10_v_ccbill_2007] on safe-harbor scope, [Automattic v Steiner 2016][ref_automattic_v_steiner_2016] on DMCA-misrepresentation-liability under §512(f), and [Ouellette v Viacom 2013][ref_ouellette_v_viacom_2013] on pro-se-plaintiff §512(f) actions. The [Urban Karaganis Schofield 2016][research_urban_karaganis_schofield_2016] Notice and Takedown in Everyday Practice empirical study documents the DMCA-abuse prevalence across major platforms. The [Lumen Database][ref_lumen_database] provides the standing archive of DMCA takedown notices submitted to participating platforms. The [US Copyright Office DMCA Section 512 Study][ref_copyright_office_512_study] provides the federal-agency comprehensive analysis of the notice-and-takedown framework as of 2020. The [Google Transparency Report DMCA data][ref_google_transparency_dmca] provides the largest single-platform quantitative disclosure of DMCA-notice volume, actor, and enforcement outcomes.

The false-DMCA-notice volume supports characterization as a fraction of total DMCA submissions,

$$p_{\text{false-DMCA}} = \frac{|\{n \in \text{DMCA notices} : n \text{ lacks valid claim}\}|}{|\{n \in \text{DMCA notices}\}|}$$

with the [Urban Karaganis Schofield 2016][research_urban_karaganis_schofield_2016] empirical estimates placing $p_{\text{false-DMCA}}$ in the range of thirty to fifty percent across major-platform samples. The counter-notice-success rate under the DMCA framework provides the target's recourse mechanism but exhibits sizable friction that reduces its practical effectiveness. The counter-notice-adoption rate follows

$$\rho_{\text{counter}} = \frac{|\text{counter-notices filed}|}{|\text{takedown-notices received}|}$$

with empirical estimates placing $\rho_{\text{counter}}$ at approximately one percent across major-platform samples, reflecting appreciable user-side friction and knowledge gaps. The chilling-effect from false-DMCA-notice submission produces suppression of legitimate speech that is estimated by as the ratio of removed-then-restored to removed-and-not-contested content

$$\rho_{\text{chilling}} = 1 - \frac{|\text{content restored via counter-notice}|}{|\text{content removed via notice}|}$$

with $\rho_{\text{chilling}}$ close to unity indicating considerable suppression of legitimate speech through the notice mechanism absent effective counter-notice recourse. The [Rossi v Motion Picture Association 2004][ref_rossi_v_mpaa_2004] case addressed the standard for DMCA-misrepresentation liability.

### Trademark Abuse

Trademark-based takedown abuse operates through the assertion of unfounded or overbroad trademark claims to trigger platform enforcement against the target's use of trademark-adjacent content. The [Amazon Brand Registry][ref_amazon_brand_registry], the [YouTube Content ID trademark framework][ref_youtube_trademark_policy], and adjacent platform trademark-enforcement infrastructures have been documented as subject to false-claim abuse. The false-trademark-claim identification statistic operates on the claim's specificity, the claimant's actual trademark registration, and the claimed-use fair-use characterization,

$$\Lambda_{\text{tm-false}} = \frac{p(\text{claim features} \mid \text{false})}{p(\text{claim features} \mid \text{valid})}$$

with the classification triggered when the likelihood ratio exceeds a chosen threshold. Contemporary platform-side estimates place false-trademark-claim rates in the range of ten to thirty percent of submitted claims. The [Rescuecom v Google 2009][ref_rescuecom_v_google_2009] case addressed keyword-based trademark issues at the search-engine advertising level. The [MTM v Amazon 2015][ref_mtm_v_amazon_2015] case addressed multi-jurisdiction trademark issues.

### Coordinated Abuse Reporting

Coordinated abuse reporting operates through the simultaneous submission of abuse reports (spam, harassment, terms-of-service violation) against a target account or content from multiple coordinated reporters. The technique exploits the platform's use of report-volume as a signal in automated moderation prioritization, with the goal of triggering automated or expedited human-review moderation actions against the target. The [Meta Content Moderation reports][ref_meta_atr] have documented instances of coordinated-reporting-driven moderation errors and the platform's response infrastructure.

The report-rate anomaly detection statistic operates on the standardized deviation of the report-arrival rate against a target,

$$z_{\text{report}}(t) = \frac{R(t) - \bar{R}_{\text{baseline}}}{\sigma_{R,\text{baseline}}}$$

with anomalous report-arrivals triggering the moderation-abuse-detection review. The reporter-diversity statistic distinguishes coordinated reporting from natural high-volume reporting by the anomalous concentration of reporters in coordinating communities. The false-positive amplification factor for a coordinated abuse-reporting campaign follows

$$A_{\text{FP}} = \frac{P(\text{action} \mid N_{\text{reports}})}{P(\text{action} \mid N_{\text{reports}} = 1)}$$

with $N_{\text{reports}}$ the coordinated report count and $P(\text{action})$ the platform's automated-moderation probability of enforcement action. Platforms with report-count-linear enforcement policies exhibit high $A_{\text{FP}}$, and platforms with report-verification-independent enforcement policies exhibit $A_{\text{FP}}$ close to unity. The moderation-load-impact from coordinated abuse reporting takes the form the queue-length increase

$$\Delta L_{\text{mod-queue}} = \int_0^{T_{\text{campaign}}} \lambda_{\text{coord-reports}}(t) \, dt - \mu_{\text{mod-throughput}} \cdot T_{\text{campaign}}$$

with $\lambda_{\text{coord-reports}}$ the coordinated-report-arrival rate and $\mu_{\text{mod-throughput}}$ the platform's moderation-processing throughput. Sustained coordinated-reporting operations produce moderation-queue backlog that degrades platform response time to legitimate abuse reports.

### Platform-Integrity System Abuse

Platform-integrity system abuse operates through the exploitation of platform-integrity infrastructure (bot detection, spam detection, safety-triage systems) to trigger enforcement against a target. The technique typically requires significant insider knowledge of the platform's integrity infrastructure. The [Twitter mass-reporting analysis][ref_twitter_mass_reporting_analysis] documented the pattern under which coordinated reporting was used to trigger account suspensions on the pre-Musk Twitter platform.

## Complaint-Farm Services

Complaint-farm services refer to the commercial industry that produces coordinated consumer complaints on regulatory, ratings-agency, and consumer-advocacy platforms with the intent of triggering enforcement or reputational damage against a target business.

### Better Business Bureau Complaint Farms

The Better Business Bureau (BBB) accreditation and rating system has been documented as subject to complaint-farm attack through the coordinated submission of unfounded complaints intended to trigger rating downgrades or accreditation loss for a target business. The [BBB standards for trust][ref_bbb_standards] establish the platform's response framework. The [ABC News 20/20 BBB investigation 2010][ref_abc_2020_bbb_2010] documented the pattern of BBB rating manipulation through both self-promotion (rating buying) and competitor-attack (complaint farming).

The complaint-escalation pattern from a coordinated farm produces the characteristic time-series signature of high initial complaint-arrival rate followed by rapid decay after the farm operation completes. The complaint-arrival-rate anomaly detection statistic mirrors the review-bombing burst detection,

$$z_{\text{complaint-burst}}(t) = \frac{\lambda_{\text{complaints}}(t) - \bar{\lambda}}{\sigma_\lambda}$$

with the anomaly threshold typically set at $z_{\text{complaint-burst}} > 4$ against the target-business baseline. The resolution-rate anomaly emerges from the pattern of complaints that are withdrawn, that lack the specificity to permit resolution, or that originate from complainants who cannot be located for follow-up. The resolution-rate statistic follows

$$\rho_{\text{resolve}}(\text{event}) = \frac{|\{c \in \text{event} : \text{resolved}\}|}{|\{c \in \text{event}\}|}$$

with authentic-complaint events typically exhibiting $\rho_{\text{resolve}} > 0.5$ and coordinated-farm events exhibiting $\rho_{\text{resolve}} < 0.1$ due to the unresolvable-complaint pattern.

### Negative-Review Farms

Negative-review farms operate on consumer-review platforms including Trustpilot, Sitejabber, Consumer Affairs, and Glassdoor to produce coordinated negative reviews against target businesses. The [Trustpilot Transparency Report][ref_trustpilot_transparency] documents the platform's response infrastructure. The technique overlaps with the coordinated-review-bombing technique treated above but is distinguished by the commercial-service organizational structure and the sustained-campaign temporal signature rather than the event-triggered burst signature of ordinary review bombing.

### Consumer-Complaint-Site Abuse

Consumer-complaint-site abuse operates on platforms including [Ripoff Report][ref_ripoff_report], [ComplaintsBoard][ref_complaints_board], and adjacent consumer-complaint sites through the submission of unfounded complaints against a target. The [Ripoff Report platform][ref_ripoff_report] has been the subject of substantial defamation litigation itself over the platform's policy of not removing content even after courts have declared it defamatory, subject to Section 230 immunity claims. The [Blockowicz v Williams 2010][ref_blockowicz_v_williams_2010] case addressed the challenge of court-ordered removal of defamatory content on Section-230-immune platforms.

### Government-Complaint Weaponization

Government-complaint weaponization operates through the submission of false or exaggerated complaints to government regulatory agencies (FTC, state consumer-protection offices, health-and-safety inspection agencies) with the intent of triggering government investigation or enforcement against a target. The technique exploits the government agencies' obligation to consider consumer complaints even when the complaints are unfounded. The [FTC Consumer Sentinel Network][ref_ftc_consumer_sentinel] provides the reference federal complaint-aggregation infrastructure and includes some analysis of coordinated-complaint patterns.

## Adversarial Content Operations

Adversarial content operations refer to the class of techniques that produce reputation damage through content operations against the target that do not fit neatly into the review, engagement, search-ranking, or reporting-system categories. The techniques include negative-topic association, coordinated pile-on operations, and harassment coordination.

### Negative-Topic Association

Negative-topic association operates through the deployment of content that associates the target with negative topics, events, or persons, with the intent of producing reputation damage through the guilt-by-association effect. The technique exploits the audience's tendency to weight association-based reputation signals even in the absence of substantive connection. The association-strength between target $T$ and negative-topic $N$ under repeated exposure is captured by the co-occurrence coefficient

$$\alpha_{T,N}(t) = \frac{|\{c \in \text{corpus}_t : T \in c \wedge N \in c\}|}{\sqrt{|\{c : T \in c\}| \cdot |\{c : N \in c\}|}}$$

with $\alpha_{T,N}$ growing under sustained coordinated content deployment and producing the target-topic association effect in downstream audience perception. The [Fazio Barber Sherman Rand 2019][research_fazio_barber_sherman_rand_2019] Knowledge Does Not Protect Against Illusory Truth Effect treatment provides the cognitive-psychology-adjacent framework for the underlying persuasion mechanism.

### Meme Warfare Against Competitor

Meme warfare operates through the coordinated production and amplification of negative memes about a target. The technique combines the adversarial-content-generation infrastructure with the amplification-network infrastructure and has been documented most extensively in political-manipulation contexts but produces spillover into commercial reputation contexts. The meme-cascade decay follows the exponential form

$$V_{\text{meme}}(t) = V_0 \cdot e^{-\gamma_{\text{meme}} (t - t_{\text{peak}})}$$

with $V_{\text{meme}}(t)$ the meme visibility at time $t$, $V_0$ the peak visibility, and $\gamma_{\text{meme}}$ the meme-specific decay rate. Attack-oriented meme deployment typically produces short-half-life reputation damage that persists in the audience's association memory beyond the meme's visible decay. The [Marwick and Lewis 2017][research_marwick_lewis_2017] Media Manipulation and Disinformation Online treatment provides the reference analytical framework.

### Doxing-Adjacent Tactics

Doxing refers to the disclosure of private-information about a target with the intent of enabling harassment or reputation damage. The technique intersects with privacy law and with anti-harassment law in most jurisdictions. Doxing-adjacent tactics include the publication of embarrassing but not-strictly-private information about a target (workplace, family, past incidents) with the intent of amplifying reputation damage. The doxing-damage function combines the direct reputation-damage from the disclosed information with the indirect damage from the harassment the disclosure enables,

$$D_{\text{dox}}(T) = D_{\text{direct}}(T, \text{info}) + \int_0^{\infty} D_{\text{harassment}}(T, t) \, dt$$

with the harassment-damage integral typically dominating the direct-damage term. The [Cyber Civil Rights Initiative][ref_cyber_civil_rights_initiative] provides one advocacy-and-support infrastructure resource. The [Massaro and Stryker 2013][research_massaro_stryker_2013] treatment provides the legal-scholarship framing. The [Citron 2014][book_citron_2014] Hate Crimes in Cyberspace treatment provides the comprehensive book-length treatment of the online-harassment-and-doxing legal landscape and proposed reforms.

### Social-Media Pile-On Coordination

The social-media pile-on coordination technique overlaps greatly with the dogpiling and brigading techniques treated above. The pile-on variant emphasizes the amplification of a negative narrative about a target across coordinated participant accounts, with the intent of establishing the narrative as apparent-consensus through repetition. The pile-on-coordination detection benefits from the same cross-community-origin signature that identifies brigading events.

## Cross-Platform Coordinated Negative Campaigns

Cross-platform coordinated negative campaigns represent the most operationally sophisticated competitor-attack class, combining the technique inventories from the preceding groupings across multiple platforms with cross-platform coordination infrastructure. The technique class has been documented most extensively in state-sponsored information operations targeting commercial entities associated with adversary interests, but has been increasingly documented in purely commercial competitive contexts.

The cross-platform amplification factor for a negative campaign follows

$$A_{\text{cross-platform}} = \prod_{P \in \text{platforms}} (1 + \alpha_P)$$

with $\alpha_P$ the amplification gain on platform $P$. Cross-platform campaigns achieve amplification considerably above single-platform campaigns due to the multiplicative structure and the cross-platform-narrative-reinforcement effect that increases audience-side credibility.

The detection difficulty for cross-platform campaigns exceeds single-platform detection due to the fragmentation of platform-integrity infrastructure across platforms. The [Graphika reports on coordinated inauthentic behavior][ref_graphika_reports] and the [Atlantic Council DFRLab investigations][ref_atlantic_council_dfrlab] provide the leading civil-society infrastructure for cross-platform coordinated-attack analysis. The [Bellingcat open-source investigation methodology][ref_bellingcat] provides the reference framework for cross-platform attribution investigation. The fragmentation-detection-difficulty admits characterization via the platform-coordination gap

$$G_{\text{frag}} = 1 - \min_{P_i, P_j} I(P_i, P_j)$$

with $I(P_i, P_j)$ the information-sharing intensity between platform pair $(P_i, P_j)$. High $G_{\text{frag}}$ indicates marked detection blind spots exploitable by cross-platform coordinated operations. The [Global Internet Forum to Counter Terrorism (GIFCT)][ref_gifct] and the [Christchurch Call][ref_christchurch_call] represent emerging cross-platform coordination infrastructure primarily oriented at extremism response but with generalizable methodology.

## Six-Axis Framework Application

The competitor-attack technique inventory permits systematic characterization along the six-axis framework. The characterization identifies each technique's position on each axis and enables cross-technique comparison across the competitor-attack and self-promotion classes.

The signal axis characterization for competitor-attack techniques emphasizes the negative-direction signal injection distinguishing the class from self-promotion. Individual negative fabrication produces low-volume single-channel negative-direction signal. Coordinated review bombing produces high-volume single-channel negative-direction burst signal. Brigading and dogpiling produce high-volume single-channel negative-direction engagement signal with cross-community-origin structure. Negative SEO produces low-volume multi-channel indirect signal (via ranking-algorithm inputs). Defamation campaigns produce moderate-volume multi-channel narrative-content signal. Sybil downvoting produces high-volume single-channel negative-direction signal. Reporting-system weaponization produces moderate-volume single-channel report signal. Complaint farms produce moderate-volume single-channel complaint-content signal. The signal-axis characterization is summarized by the tuple

$$\mathbf{a}_k^{\text{signal}} = (v_k, C_k, f_k, X_k, \text{sign}_k)$$

with the additional sign-attribute $\text{sign}_k = -1$ for competitor-attack techniques distinguishing them from the $\text{sign}_k = +1$ self-promotion class.

The objective axis characterization for competitor-attack techniques uniformly optimizes for target-reputation degradation, with variation in the target-attribute optimization. Review-signal-attack techniques target the target's aggregate rating. Brigading and dogpiling target the target's engagement-metric or community-standing. Negative SEO targets the target's search-ranking position. Defamation campaigns target the target's factual-attribute perception. Sybil downvoting targets the target's community-visible ranking. Reporting-system weaponization targets the target's platform-standing through triggered enforcement. Complaint farms target the target's regulatory or ratings-agency standing. The objective-axis position of each competitor-attack technique class reduces to the negative-utility functional

$$U_k^{\text{attack}}(\mathbf{x}) = -\sum_{j \in \text{target attributes}} \lambda_j^{k} g_j(x_T) + \gamma_{\text{self}}(x_A)$$

with the $\lambda_j^{k}$ weights specifying the technique class's target-attribute optimization composition.

The structure axis characterization for competitor-attack techniques varies from individual competitor-attackers (small-scale defamation) through hired competitive-intelligence and reputation-attack firms (mid-scale coordinated operations) through commercial complaint-farm services (industrial-scale coordinated operations) through state-sponsored operations extending to commercial targets. The structure-axis characterization mirrors the self-promotion case with the additional variant of ad-hoc mobilization structures (brigading communities) that lack the sustained-operation structure of commercial marketplaces but produce comparable technique output during active-campaign windows. The structure axis allows summary via the hierarchy depth $D_k$, branching factor $B_k$, and operator population $N_k$, with ad-hoc mobilization operations exhibiting shallow-and-broad structure ($D_k \approx 1-2$, $B_k \approx 10^2-10^5$, $N_k \approx 10^3-10^6$).

The model axis characterization identifies the technical and rhetorical content each competitor-attack technique class carries. The technical model varies as for self-promotion (fabrication method, account-provenance method, coordination method, evasion method). The rhetorical model differs from self-promotion in the direction of the persuasion framing (negative testimonial, comparative denigration, emotional-negative, expert-authority against target). The credibility framing includes false-attribution to authoritative sources, manufactured-evidence, and misrepresented context. The narrative framing includes false-personal-experience, statistical-cherry-picking, and quality-attribute-denigration. The model-axis position of each technique takes the form the position vector $\mathbf{c}_k$ over the technique-space basis.

The interaction axis characterization for competitor-attack techniques introduces the direct target-attacker relationship that self-promotion techniques generally lack. The target-attacker relationship dimensions include target-aware attacks (where the target may take defensive action), target-unaware attacks (where the target lacks awareness), attacker-hidden attacks (where the attacker maintains identity concealment), and attacker-attributed attacks (where the attacker's identity is known or knowable). The interaction axis also includes the platform-relationship dimensions (compliant use, terms-of-service violation, active concealment, adversarial evasion), the competitor relationship (the target and possibly other competitors), the audience relationship (audience-unaware attack, audience-aware attack, audience-complicit attack), and the enforcement-relationship dimensions (including specifically the legal-recourse dimensions absent from self-promotion). The interaction axis supports operationalization as the weighted signed graph over attackers, targets, platforms, and enforcers, with the additional attacker-target edge admitting characterization as

$$w_{A \to T}(t) = -\text{sign}(A \to T) \cdot \|d_{\text{attack}}(t)\|$$

with the negative sign encoding the antagonistic direction and $\|d_{\text{attack}}(t)\|$ the magnitude of the intended damage.

The adaptation axis characterization varies as for self-promotion. Individual competitor-attack operations exhibit slow adaptation. Commercial complaint-farm services exhibit rapid adaptation with dedicated engineering resources. State-sponsored operations exhibit rapid adaptation with dedicated intelligence-service infrastructure. Ad-hoc brigading operations exhibit rapid mobilization but slow between-campaign learning, producing a distinctive adaptation-axis signature that differs from both commercial and state-sponsored operations. The adaptation axis is operationalized as the technique-migration time constant $\tau_k$ under the first-order relaxation dynamics.

The competitor-attack cross-axis coupling matrix

$$C^{\text{attack}} = \left[\frac{\partial a^b}{\partial a^a}\right]_{a, b \in \text{axes}}$$

encodes the empirical dependencies among axis values that differ systematically from the self-promotion coupling matrix. The principal differences include stronger interaction-model coupling (target-relationship structure shapes the model choice) and stronger interaction-adaptation coupling (target-response drives faster adaptation than platform-response alone). The self-promotion versus competitor-attack coupling-matrix difference norm can be characterized as

$$\|C^{\text{attack}} - C^{\text{self-promo}}\|_F = \sqrt{\sum_{a,b} (C^{\text{attack}}_{ab} - C^{\text{self-promo}}_{ab})^2}$$

with the Frobenius norm reflecting the aggregate coupling-structure difference between the two technique classes.

## Detection Methodology Summary

The detection methodology landscape for competitor-attack manipulation is treated in depth in the closing article of the miniseries. The framing article surveys the principal detection-methodology classes as they apply to the competitor-attack technique inventory.

Multi-modal detection combines the review-content, account-behavior, network-graph, and cross-platform signals to identify competitor-attack manipulation. The multi-modal approach exhibits higher accuracy than single-modal approaches at the cost of higher computational and infrastructure requirements. The composite detection score under weighted feature-modality combination takes the form

$$s_{\text{multi-modal}} = \sum_m w_m \cdot s_m$$

with $s_m$ the modality-specific detection score and $w_m$ the modality weight optimized on labeled training data. The multi-modal accuracy bound under conditional independence assumption reduces to the ensemble-classification bound treated in the preceding article. The [Cresci 2020][research_cresci_2020] survey establishes the reference multi-modal framework.

Target-aware detection operates from the target's perspective and monitors for the signatures of attack targeting the target's own reputation. The target-aware approach admits detection of attack signals that platform-side monitoring may miss due to the platform's aggregated-across-targets perspective. The target-aware detection ROC exhibits systematic asymmetry with the platform-aware ROC in that the target has both stronger prior information about baseline authentic-signal distribution and stronger incentive to invest in detection given the concentrated stake in the target's own reputation,

$$\text{AUC}_{\text{target}} > \text{AUC}_{\text{platform}} \text{ typically}$$

but faces the constraint that the target lacks the platform's cross-user infrastructure for account-level detection. Commercial reputation-management services including [Reputation.com][ref_reputation_com], [NetReputation][ref_netreputation_com], and adjacent services provide the target-aware monitoring infrastructure.

Cross-platform detection collaboration operates through the same infrastructure treated for coordinated inauthentic behavior in the preceding article. The cross-platform detection for competitor-attack faces the additional coordination challenge that the source-community and target-platform are often on different platforms operated by non-cooperating companies.

The general anomaly-score statistic under the null-model $H_0$ takes the standardized form

$$z_{\text{attack}} = \frac{T^{\text{attack}}(\mathbf{x}) - E_{H_0}[T^{\text{attack}}]}{\sqrt{\text{Var}_{H_0}[T^{\text{attack}}]}}$$

with $T^{\text{attack}}$ the attack-oriented test statistic evaluated on the observed data.

## Platform Countermeasure Summary

Platform countermeasures for competitor-attack manipulation are treated in depth in the closing article of the miniseries. The framing article surveys the principal countermeasure classes.

Review-verification countermeasures constrain the review-eligible actor population and reduce the review-signal-attack space. The countermeasures include verified-purchase requirements, transaction-tied review capability, and post-transaction review windows. Platform-integrity policies including the [YouTube Community Guidelines strikes system][ref_youtube_community_guidelines_strikes], the [Meta Community Standards general framework][ref_meta_community_standards], the [Reddit Content Policy][ref_reddit_content_policy], the [TikTok Community Guidelines general framework][ref_tiktok_community_guidelines_general], and the [X Terms of Service][ref_x_terms_of_service] establish the platform-side policy framework for attack-content moderation. The [Meta CIB Report Archive][ref_meta_cib_report_archive] provides the standing disclosure of the platform's quarterly enforcement actions against coordinated attack operations. The verified-purchase requirement reduces the attack-eligible population by the factor

$$\rho_{\text{verify}} = \frac{|\{r : \text{verified-purchase}\}|}{|\{r : \text{all reviews}\}|}$$

which shifts the manipulation cost function by requiring the attacker to complete transactions to gain review eligibility.

Report-verification countermeasures constrain the reporting-system-abuse space through the verification of abuse-report content before automated moderation action. The countermeasure space includes report-rate-limiting per reporter, reporter-history weighting, and human-review triage for high-stakes decisions.

Rate-limiting countermeasures constrain the volume-based attack techniques through per-account throughput bounds

$$\lambda_i^{\text{observed}} \leq \lambda_{\text{max}}, \quad \forall i$$

that increase the account-provenance cost per unit attack output. The cross-target rate-limiting extension applies additional bounds against the same target from many attacker accounts,

$$\sum_{i \in \text{attackers}} \lambda_{i \to T} \leq \Lambda_T^{\text{max}}$$

with $\Lambda_T^{\text{max}}$ a target-level aggregate throughput ceiling that constrains the coordinated-attack scale even when individual attacker accounts remain under the per-account bound.

Content-authentication countermeasures target the false-content-attack space through cryptographic content-signing and provenance-attestation as treated in the preceding article.

## Legal Recourse Landscape

The legal recourse landscape for competitor-attack manipulation is more developed than for self-promotion manipulation due to the direct intersection with defamation law and with unfair-competition doctrine. The framing article surveys the principal recourse categories.

Defamation actions provide the primary US-law recourse against false-content-attack. The account operates under the [New York Times v Sullivan 1964][ref_ny_times_sullivan_1964] and [Gertz v Robert Welch 1974][ref_gertz_v_welch_1974] framework with the elements characterization above. The defamation-action success-rate estimate under empirical study varies by jurisdiction and case type, with the composite rate admitting characterization as

$$s_{\text{def-action}} = \Pr(\text{plaintiff prevails} \mid \text{action filed})$$

with empirical estimates from the [Digital Media Law Project][ref_dmlp_database] and adjacent case-database analysis suggesting $s_{\text{def-action}} \in [0.20, 0.40]$ depending on the target-classification (public-figure defamation cases exhibit lower success rates than private-figure cases). The cost-of-litigation function for a defamation action has the form

$$C_{\text{def-litigation}}(T) = C_{\text{filing}} + C_{\text{discovery}} \cdot T + C_{\text{trial}} \cdot \mathbb{1}[\text{trial}]$$

with $T$ the litigation duration in months. Contemporary US defamation litigation costs are typically in the range of $10^5$ to $10^6$ USD for a case that proceeds to trial, which limits the recourse to plaintiffs with extensive financial resources or contingency-fee representation. The [SPEECH Act 2010][ref_speech_act_2010] provides US-jurisdiction protection against enforcement of foreign defamation judgments inconsistent with US First Amendment standards.

Lanham Act false-advertising actions provide recourse against competitor-attack that constitutes false or misleading representations in commercial advertising or promotion. The [15 USC 1125 Lanham Act Section 43a][ref_lanham_act_15_usc_1125] framework applies broadly to commercial-context attacks. The Lanham Act §43(a) actionability requires five elements admitting compact characterization as

$$A_{\text{lanham}} = \mathbb{1}[\text{false statement}] \cdot \mathbb{1}[\text{actual deception}] \cdot \mathbb{1}[\text{materiality}] \cdot \mathbb{1}[\text{interstate commerce}] \cdot \mathbb{1}[\text{likelihood of injury}]$$

with all five elements required for a successful action.

State unfair-competition and tortious-interference actions provide alternative recourse under state-law claims. The [California Business and Professions Code Section 17200][ref_california_ucl_17200] provides the California framework. Tortious interference with business relationships and prospective economic advantage provides recourse across most state jurisdictions. The [Restatement Second of Torts][ref_restatement_second_torts] enumerates the elements for tortious interference and adjacent commercial torts. State anti-SLAPP statutes (Strategic Lawsuit Against Public Participation) provide expedited-dismissal procedures for defamation-adjacent litigation that targets protected speech. The [California Code of Civil Procedure Section 425.16][ref_california_anti_slapp] anti-SLAPP framework is the reference state-level anti-SLAPP mechanism, with parallel frameworks in more than thirty other states. The [Public Participation Project Anti-SLAPP tracker][ref_anti_slapp_tracker] maintains the standing catalog of state-level anti-SLAPP statutes. The [Uniform Public Expression Protection Act][ref_upepa] provides the uniform-law framework for cross-jurisdictional adoption. The [EU anti-SLAPP directive 2024][ref_eu_anti_slapp_2024] extends the model to European jurisdictions.

Federal criminal recourse against competitor-attack technique classes includes the [18 USC 2261A federal cyberstalking statute][ref_cyberstalking_18_usc_2261a] addressing patterns of harassing conduct across state lines, and the [47 USC 223 telecommunications harassment framework][ref_47_usc_223] addressing telephone-and-electronic-communications harassment. The DMCA misrepresentation provision at [17 USC 512(f)][ref_dmca_512f] provides recourse against false DMCA takedowns as characterized above. The [Communications Decency Act Section 230(c)(2)][ref_section_230_c2] Good Samaritan provision permits platforms to engage in good-faith attack-content moderation without incurring liability for the moderation choices.

Intermediary-liability constraints operate under [47 USC 230][ref_section_230_cda] which limits platform-side recourse but does not limit direct-actor recourse. The Section-230-immunity boundary condition for a given content instance is described by

$$I_{\text{§230}}(c) = \mathbb{1}[\text{platform did not materially contribute to content}] \cdot \mathbb{1}[\text{good-faith moderation}]$$

with the platform receiving immunity when both conditions hold. The [Roommates.com 2008][ref_roommates_2008] exception and the [Batzel v Smith 2003][ref_batzel_v_smith_2003] framework establish limits on Section 230 immunity applicable to platform-created or platform-solicited attack content.

International recourse varies by jurisdiction. The [UK defamation framework][ref_uk_defamation_act_2013] under the Defamation Act 2013, the [Germany NetzDG 2017][ref_germany_netzdg_2017] takedown framework, the [Australia Defamation Act uniform framework][ref_australia_defamation_uniform], and the [Canada Grant v Torstar 2009][ref_grant_v_torstar_2009] framework each provide distinct recourse structures. Additional international case law includes [Dow Jones v Gutnick 2002][ref_dow_jones_v_gutnick_2002] establishing the Australian jurisdiction-of-publication framework for internet-mediated defamation, [Godfrey v Demon Internet 1999][ref_godfrey_v_demon_1999] establishing the UK intermediary-liability framework, [McAlpine v Bercow 2013][ref_mcalpine_v_bercow_2013] applying UK defamation law to Twitter, and [Loutchansky v Times Newspapers 2001][ref_loutchansky_v_times_2001] establishing the UK online-publication limitation-period framework. The [SPEECH Act 2010][ref_speech_act_2010] limits US-jurisdiction enforceability of some international judgments.

## Prevalence Estimates by Technique Class

The empirical prevalence estimates for competitor-attack techniques are significantly less developed than for self-promotion techniques, reflecting both the lower base-rate prevalence and the measurement challenges the attack class introduces. The framing article presents the composite estimates from the available empirical literature.

Coordinated review-bombing prevalence is documented most extensively in the [Metacritic][ref_metacritic_review_bombing] and [Rotten Tomatoes][ref_rt_review_bombing] cases and in the [Vasilescu and Casanueva 2016][research_vasilescu_casanueva_2016] and adjacent empirical treatments. Event-triggered review bombing appears in approximately zero-point-one to one percent of high-visibility product releases on average, with sizable variance driven by specific-event triggers.

Brigading prevalence on Reddit and adjacent community platforms is documented in [Kumar et al 2018][research_kumar_et_al_2018], [Chandrasekharan et al 2017][research_chandrasekharan_et_al_2017], and [Zannettou et al 2018][research_zannettou_et_al_2018_reddit_4chan]. The brigading-event rate varies substantially across subreddits and time periods, with typical estimates in the range of one to five percent of high-visibility target-community events involving cross-community mobilization.

Negative-SEO prevalence is difficult to estimate because attack detection requires target-side monitoring that is not systematically reported at the industry level. Industry estimates from reputation-management firms place negative-SEO-attack incidence at approximately one to five percent of monitored client campaigns. The [Cyveillance 2015][ref_cyveillance_2015_reverse_seo] estimate at the enterprise level suggests appreciable variation by industry vertical.

Defamation-campaign prevalence is difficult to estimate at aggregate level because litigation-based reporting captures only the small subset of cases that proceed to court. The [Digital Media Law Project database][ref_dmlp_database] provides one aggregate resource for documented cases. Enterprise-level surveys from [Ponemon Institute][ref_ponemon_institute] and adjacent industry-research infrastructure suggest that defamation-adjacent reputation attacks affect approximately five to ten percent of large-enterprise brands annually.

Sybil-downvoting prevalence tracks the aggregate Sybil-account prevalence surveyed in [Cresci 2020][research_cresci_2020] and [Yang et al 2020][research_yang_et_al_2020]. The attack-oriented Sybil-vote fraction of aggregate Sybil-activity is not systematically reported at the industry level.

Reporting-system-abuse prevalence is documented most extensively in the DMCA context via the [Urban Karaganis Schofield 2016][research_urban_karaganis_schofield_2016] treatment estimating false-notice rates in the thirty-to-fifty percent range. The parallel estimates for trademark-abuse and coordinated-abuse-reporting are less developed.

The composite category-weighted prevalence estimator has the same formal characterization as for self-promotion,

$$\hat{p}^{\text{attack}} = \sum_c w_c \hat{p}_c^{\text{attack}}, \quad w_c = \frac{n_c}{\sum_{c'} n_{c'}}$$

with the composite aggregate under conservative methodology estimated in the range of one to five percent of total reputation-signal volume across the surveyed platform ecosystem, with considerable category variation. The variance decomposition under stratified sampling takes the form

$$\text{Var}(\hat{p}^{\text{attack}}) = \sum_c w_c^2 \, \text{Var}(\hat{p}_c^{\text{attack}}) + \sum_{c \neq c'} w_c w_{c'} \, \text{Cov}(\hat{p}_c^{\text{attack}}, \hat{p}_{c'}^{\text{attack}})$$

with the cross-category covariance term typically small under approximately-independent category-sampling. The estimate is markedly lower than the self-promotion aggregate reflecting the lower base-rate prevalence of competitor-attack techniques in most consumer-facing contexts.

## Alternative Analytical Frameworks

The economic-signaling-and-tort framework the miniseries adopts is one of several analytical frameworks under which the competitor-attack phenomenon permits treatment. The framing article surveys the principal alternatives and identifies where the alternative frameworks would produce different conclusions from this formulation the miniseries adopts.

The antitrust-and-predatory-conduct framework treats competitor-attack as an exclusionary competitive practice subject to Sherman Act Section 2 analysis under the [Sherman Act 15 USC 2][ref_sherman_act_15_usc_2] framework. The treatment identifies the competitive-harm patterns of reputation-attack operations and would potentially support antitrust actions against systematic attack operations by dominant platform participants against smaller competitors. The [Areeda and Turner 1975][research_areeda_turner_1975] cost-based predation framework applies to reputation attacks via the sacrifice-versus-legitimate-competition test.

The tort-doctrine framework treats competitor-attack under the tort categories the [Restatement Second of Torts][ref_restatement_second_torts] enumerates, including defamation, false light, tortious interference with contract, tortious interference with prospective economic advantage, and injurious falsehood. This account operates through the per-tort element analysis and produces damages-based recourse to the tort category invoked. The framework is the primary US-law recourse structure and allows treatment through the [Prosser and Keeton 1984][book_prosser_keeton_1984] Handbook of the Law of Torts and subsequent doctrinal treatments.

The cascade-dynamics framework of [Watts 2002][research_watts_2002] and [Bikhchandani Hirshleifer Welch 1992][research_bikhchandani_hirshleifer_welch_1992] treats competitor-attack propagation as a threshold-cascade dynamic on the target's audience network. The account predicts that attack effectiveness is highly sensitive to the network topology and to the timing of the attack relative to the audience's information state, which produces the observed high-variance outcome distribution across attempted attacks. The [Salganik Dodds Watts 2006][research_salganik_dodds_watts_2006] Experimental Study of Inequality treatment provides the empirical foundation.

The harassment-continuum framework of [Kelly 1988][book_kelly_1988] and the online-harassment extension in [Jane 2014][research_jane_2014] treat competitor-attack against individual targets (particularly public-figure individuals) as a subset of the broader harassment continuum, with attention to gendered and marginalized-population-targeting patterns. The model predicts that reforms internal to the competitor-attack framework will fail to address the underlying harassment dynamic and that broader anti-harassment reform is required.

The information-warfare framework treats competitor-attack as a subset of the broader information-operations framework that includes state-sponsored operations. The [Rid 2020][book_rid_2020] Active Measures treatment, the [Singer and Brooking 2018][book_singer_brooking_2018] LikeWar treatment, and the [Woolley and Howard 2018][book_woolley_howard_2018] Computational Propaganda treatment develop the framework. This formulation predicts significant technique-and-infrastructure spillover from state-sponsored operations into commercial competitor-attack operations, which produces commercial-attack characteristics that pure-commercial framing may miss.

The restorative-justice framework of [Zehr 2002][book_zehr_2002] Little Book of Restorative Justice provides an alternative recourse structure emphasizing target-restoration and community-repair rather than adversarial-litigation adjudication. This account has been applied to online-harassment contexts through the [Chandrasekharan et al 2017][research_chandrasekharan_et_al_2017] work on community-ban effects and adjacent scholarship. The framework predicts that adversarial-litigation-focused reform produces limited target-restoration effect compared with community-based interventions that address the underlying attack-motivation and audience-dynamics.

The regulatory-capture framework of [Stigler 1971][research_stigler_1971] extends to defamation-reform politics through the observation that reform of the defamation-and-attack landscape faces systematic opposition from actors that benefit from the status quo. The account predicts that reform-oriented efforts (comprehensive anti-SLAPP legislation, defamation-law modernization, Section-230 revision) will face persistent opposition from concentrated-interest actors even where diffuse-benefit constituencies favor the reform.

The Bayesian-persuasion framework of [Kamenica and Gentzkow 2011][research_kamenica_gentzkow_2011] treats competitor-attack as an information-design intervention in which the attacker controls the information environment presented to the target's audience. The model identifies platform-mediated information-presentation choices that shape the attack's effectiveness independently of the attack content itself.

Each alternative framework offers analytical leverage the miniseries does not fully develop. The miniseries adopts the economic-signaling-and-tort framework as the primary organizing structure because it provides the most tractable formalization of the attacker-target-platform-audience strategic interaction and connects most directly to the empirical detection and enforcement literatures. The closing article treats the framework selection more fully and identifies the empirical questions on which the alternative frameworks would predict different observations.

## Terminological Note

The article adopts the terminology introduced in the framing article of the miniseries at [Virtual Reputation Manipulation Theory and Analytical Framework][related_post_a277_theory]. The self-promotion class refers to techniques treated in the preceding article. The competitor-attack class refers to the techniques treated in this article. The target refers to the party against whom the attack is directed, distinguished from the attacker who initiates the attack and from the audience who receives the attack content. The term brigading refers specifically to the cross-community-mobilization variant of coordinated attack, distinguished from the more general coordinated-inauthentic-behavior class. The term dogpiling refers specifically to the high-volume-response variant of coordinated attack directed at target content. The term review bombing refers to the coordinated deposit of negative reviews against a target within a short time window, typically event-triggered. The term negative SEO or reverse SEO refers to the class oriented at degrading a target's search-ranking position, distinguished from aggressive SEO oriented at inflating the actor's own ranking. The term defamation retains its legal meaning of a false statement of fact damaging to reputation, with the actual-malice standard for public figures. The term doxing refers to the disclosure of private information about a target. The article uses the platform-integrity industry terminology and the academic detection terminology where each is more precise than the alternative.

## Load-Bearing Open Questions

- What is the correct empirical characterization of the aggregate competitor-attack prevalence across the platform ecosystem, and how does the estimate change under alternative methodologies?
- What is the correct empirical characterization of the causal impact of competitor-attack technique classes on downstream target-business outcomes?
- What is the correct empirical characterization of the marginal deterrent effect of defamation-litigation and unfair-competition-litigation on competitor-attack prevalence?
- What is the correct empirical characterization of the interaction between commercial competitor-attack manipulation and political-adjacent attack operations, and does the interaction produce systematic spillover effects?
- What is the correct comparative treatment of the competitor-attack manipulation ecosystem across jurisdictions with appreciably different defamation-law and intermediary-liability frameworks?
- How should the platform-integrity operations, the regulatory framework, and the legal-recourse infrastructure coordinate to reduce the equilibrium competitor-attack intensity while preserving legitimate competitive and critical speech?
- What is the correct empirical characterization of the reporting-system-abuse prevalence across major platforms, and what is the marginal effect of report-verification investment on attack prevalence and on legitimate-abuse-report response quality?

These questions recur throughout the miniseries and are revisited in the closing synthesis.

## References

### Books

- [Andrew and Mitrokhin 1999 The Sword and the Shield][book_andrew_mitrokhin_1999]
- [Ansolabehere and Iyengar 1996 Going Negative][book_ansolabehere_iyengar_1996]
- [Baldasty 1992 The Commercialization of News in the Nineteenth Century][book_baldasty_1992]
- [Boorstin 1961 The Image][book_boorstin_1961]
- [Bork 1978 The Antitrust Paradox][book_bork_1978]
- [Citron 2014 Hate Crimes in Cyberspace][book_citron_2014]
- [Franklin Anderson and Cate 2016 Mass Media Law][book_franklin_anderson_cate_2016]
- [Franks 2019 The Cult of the Constitution][book_franks_2019]
- [Geer 2006 In Defense of Negativity][book_geer_2006]
- [Kelly 1988 Surviving Sexual Violence][book_kelly_1988]
- [Kiernan 1988 The Duel in European History][book_kiernan_1988]
- [Loveland 2000 Political Libels A Comparative Study][book_loveland_2000]
- [Mark 2006 Going Dirty History of Negative Campaigning][book_mark_2006]
- [Marwick 2013 Status Update][book_marwick_2013]
- [Michaels 2008 Doubt Is Their Product][book_michaels_2008]
- [Michaels 2020 The Triumph of Doubt][book_michaels_2020]
- [Nasaw 2000 The Chief][book_nasaw_2000]
- [Oreskes and Conway 2010 Merchants of Doubt][book_oreskes_conway_2010]
- [Phillips 2015 This is Why We Can't Have Nice Things][book_phillips_2015]
- [Posner 2001 Antitrust Law][book_posner_2001]
- [Prosser and Keeton 1984 Handbook of the Law of Torts][book_prosser_keeton_1984]
- [Rid 2020 Active Measures][book_rid_2020]
- [Rosenberg 1986 Protecting the Best Men][book_rosenberg_1986]
- [Siebert 1965 Freedom of the Press in England 1476-1776][book_siebert_1965]
- [Singer and Brooking 2018 LikeWar][book_singer_brooking_2018]
- [Sunstein 2018 Republic Divided Democracy in the Age of Social Media][book_sunstein_2018]
- [Weiner 2007 Legacy of Ashes The History of the CIA][book_weiner_2007]
- [Wills 1970 Nixon Agonistes][book_wills_1970]
- [Woolley and Howard 2018 Computational Propaganda][book_woolley_howard_2018]
- [Zehr 2002 Little Book of Restorative Justice][book_zehr_2002]

### Reference

- [4chan Raid Coordination Documentation][ref_4chan_raid_documentation]
- [15 USC 1125 Lanham Act Section 43a False Advertising][ref_lanham_act_15_usc_1125]
- [15 USC 2 Sherman Act Section 2][ref_sherman_act_15_usc_2]
- [17 USC 512 Digital Millennium Copyright Act Notice and Takedown][ref_dmca_17_usc_512]
- [17 USC 512(f) DMCA Misrepresentation Provision][ref_dmca_512f]
- [18 USC 2261A Federal Cyberstalking Statute][ref_cyberstalking_18_usc_2261a]
- [47 USC 223 Telecommunications Harassment Framework][ref_47_usc_223]
- [47 USC 230 Communications Decency Act Section 230][ref_section_230_cda]
- [47 USC 230(c)(2) Good Samaritan Provision][ref_section_230_c2]
- [ABC News 20/20 BBB Investigation 2010][ref_abc_2020_bbb_2010]
- [Amber Heard v Depp 2022][ref_heard_v_depp_2022]
- [Atlantic Council DFRLab Investigations][ref_atlantic_council_dfrlab]
- [Anti-SLAPP Tracker Public Participation Project][ref_anti_slapp_tracker]
- [Automattic v Steiner 2016][ref_automattic_v_steiner_2016]
- [Bartnicki v Vopper 2001][ref_bartnicki_v_vopper_2001]
- [Bellingcat Open-Source Investigation Methodology][ref_bellingcat]
- [Birther Conspiracy Campaign 2008-2016][ref_birther_campaign]
- [California Anti-SLAPP Statute Code of Civil Procedure 425.16][ref_california_anti_slapp]
- [Ahrefs Domain Rating Framework][ref_ahrefs_domain_rating]
- [Amazon Community Guidelines][ref_amazon_community_guidelines]
- [Amazon Brand Registry][ref_amazon_brand_registry]
- [Amazon Review Bombing Documented Cases][ref_amazon_review_bombing_cases]
- [Amazon v ThinkExpress 2022][ref_amazon_v_thinkexpress_2022]
- [Australia Defamation Act Uniform Framework][ref_australia_defamation_uniform]
- [Barnes v Yahoo 2009][ref_barnes_v_yahoo_2009]
- [Batzel v Smith 2003][ref_batzel_v_smith_2003]
- [BBB Standards for Trust][ref_bbb_standards]
- [Blockowicz v Williams 2010][ref_blockowicz_v_williams_2010]
- [Cahill v Doe 2005][ref_cahill_v_doe_2005]
- [California Business and Professions Code Section 17200 Unfair Competition Law][ref_california_ucl_17200]
- [Cardi B v Kebe 2022][ref_cardi_b_v_kebe_2022]
- [E Jean Carroll v Trump 2023][ref_carroll_v_trump_2023]
- [Christchurch Call][ref_christchurch_call]
- [ComplaintsBoard][ref_complaints_board]
- [Copyright Office Section 512 Study][ref_copyright_office_512_study]
- [Cyber Civil Rights Initiative][ref_cyber_civil_rights_initiative]
- [Cyveillance 2015 Reverse SEO Report][ref_cyveillance_2015_reverse_seo]
- [Dendrite v Doe 2001][ref_dendrite_v_doe_2001]
- [Digital Media Law Project Database][ref_dmlp_database]
- [Discord Coordination Reports][ref_discord_coordination_reports]
- [Doe v MySpace 2008][ref_doe_v_myspace_2008]
- [Dow Jones v Gutnick 2002][ref_dow_jones_v_gutnick_2002]
- [EU Anti-SLAPP Directive 2024][ref_eu_anti_slapp_2024]
- [Fair Housing Council v Roommates.com 2008][ref_roommates_2008]
- [Force v Facebook 2019][ref_force_v_facebook_2019]
- [FTC Consumer Sentinel Network][ref_ftc_consumer_sentinel]
- [FTC v Amazon 2023][ref_ftc_v_amazon_2023]
- [FTC v Roomster 2022][ref_ftc_roomster_2022]
- [Gamergate Coordinated Harassment Documentation][ref_gamergate_coverage]
- [Godfrey v Demon Internet 1999][ref_godfrey_v_demon_1999]
- [Germany Netzwerkdurchsetzungsgesetz NetzDG 2017][ref_germany_netzdg_2017]
- [Gertz v Robert Welch 1974][ref_gertz_v_welch_1974]
- [Global Internet Forum to Counter Terrorism GIFCT][ref_gifct]
- [Gonzalez v Google 2023][ref_gonzalez_v_google_2023]
- [Goodreads Review Bombing Documented Cases][ref_goodreads_review_bombing]
- [Google 2011 Panda Algorithm Update][ref_google_panda_2011]
- [Google 2012 Penguin Algorithm Update][ref_google_penguin_2012]
- [Google Disavow Tool][ref_google_disavow_tool]
- [Google Manual Actions Documentation][ref_google_manual_actions]
- [Google Safe Browsing][ref_google_safe_browsing]
- [Google Search Central Spam Policies][ref_google_search_spam_policies]
- [Google Search Console Malware Notification][ref_google_search_console_malware]
- [Google Transparency Report DMCA Data][ref_google_transparency_dmca]
- [Grant v Torstar 2009 Canada][ref_grant_v_torstar_2009]
- [Graphika Reports on Coordinated Inauthentic Behavior][ref_graphika_reports]
- [Herrick v Grindr 2019][ref_herrick_v_grindr_2019]
- [Klayman v Zuckerberg 2014][ref_klayman_v_zuckerberg_2014]
- [Lenz v Universal 2015][ref_lenz_v_universal_2015]
- [Loutchansky v Times Newspapers 2001][ref_loutchansky_v_times_2001]
- [Lumen Database][ref_lumen_database]
- [McAlpine v Bercow 2013][ref_mcalpine_v_bercow_2013]
- [Meta Adversarial Threat Report][ref_meta_atr]
- [Meta CIB Report Archive][ref_meta_cib_report_archive]
- [Meta Community Standards][ref_meta_community_standards]
- [Metacritic Review Bombing Documented Cases][ref_metacritic_review_bombing]
- [Milkovich v Lorain Journal 1990][ref_milkovich_v_lorain_1990]
- [Moz Spam Score Methodology][ref_moz_spam_score]
- [MTM v Amazon 2015][ref_mtm_v_amazon_2015]
- [Nemet Chevrolet v Consumeraffairs.com 2009][ref_nemet_v_consumeraffairs_2009]
- [NetReputation.com][ref_netreputation_com]
- [New York Times v Sullivan 1964][ref_ny_times_sullivan_1964]
- [Online Policy Group v Diebold 2004][ref_diebold_2004]
- [Ouellette v Viacom 2013][ref_ouellette_v_viacom_2013]
- [Perfect 10 v CCBill 2007][ref_perfect_10_v_ccbill_2007]
- [Sarah Palin v NYT 2022][ref_palin_v_nyt_2022]
- [Ponemon Institute Enterprise Reputation Research][ref_ponemon_institute]
- [Reddit Content Policy][ref_reddit_content_policy]
- [Reddit Vote Manipulation Policy][ref_reddit_vote_manipulation_policy]
- [Reit-Nightingale v Universal 2019][ref_reit_nightingale_v_universal_2019]
- [Reputation.com][ref_reputation_com]
- [Rescuecom v Google 2009][ref_rescuecom_v_google_2009]
- [Restatement Second of Torts][ref_restatement_second_torts]
- [Right to be Forgotten EU Framework][ref_right_to_be_forgotten_eu]
- [Ripoff Report Platform][ref_ripoff_report]
- [Rossi v Motion Picture Association 2004][ref_rossi_v_mpaa_2004]
- [Rotten Tomatoes Review Bombing Documented Cases][ref_rt_review_bombing]
- [SPEECH Act 2010][ref_speech_act_2010]
- [Swift Boat Veterans for Truth 2004][ref_swift_boat_2004]
- [Telegram Coordination Reports][ref_telegram_coordination_reports]
- [TikTok Community Guidelines General Framework][ref_tiktok_community_guidelines_general]
- [Trustpilot Transparency Report][ref_trustpilot_transparency]
- [Twitter Mass-Reporting Analysis][ref_twitter_mass_reporting_analysis]
- [UK Defamation Act 2013][ref_uk_defamation_act_2013]
- [Uniform Public Expression Protection Act][ref_upepa]
- [Wikipedia Sockpuppet Investigations][ref_wikipedia_spi]
- [Willie Horton 1988 Attack Ad Documentation][ref_willie_horton_1988]
- [X Terms of Service][ref_x_terms_of_service]
- [YouTube Community Guidelines Strikes System][ref_youtube_community_guidelines_strikes]
- [YouTube Content ID Trademark Framework][ref_youtube_trademark_policy]
- [Yelp v Hadeed Carpet Cleaning 2014][ref_yelp_v_hadeed_2014]
- [Zeran v AOL 1997][ref_zeran_v_aol_1997]
- [Zervos v Trump Defamation Litigation][ref_zervos_v_trump]

### Related Post

- [Virtual Reputation Manipulation Theory and Analytical Framework A277][related_post_a277_theory]
- [Virtual Reputation Manipulation Techniques of Self-Promotion A278][related_post_a278_self_promotion]

### Research

- [Anderson 1991 Reputation Compensation Punishment Suppression][research_anderson_1991]
- [Areeda and Turner 1975 Predatory Pricing and Related Practices][research_areeda_turner_1975]
- [Balkin 2018 Free Speech is a Triangle][research_balkin_2018]
- [Barabasi and Albert 1999 Emergence of Scaling in Random Networks][research_barabasi_albert_1999]
- [Bikhchandani Hirshleifer Welch 1992 A Theory of Fads Fashion Custom and Cultural Change][research_bikhchandani_hirshleifer_welch_1992]
- [Carlini and Wagner 2017 Towards Evaluating the Robustness of Neural Networks][research_carlini_wagner_2017]
- [Chandrasekharan et al 2017 You Can't Stay Here Reddit Ban Effects][research_chandrasekharan_et_al_2017]
- [Cresci 2020 A Decade of Social Bot Detection][research_cresci_2020]
- [Douek 2021 Governing Online Speech][research_douek_2021]
- [Elhauge 2003 Defining Better Monopolization Standards][research_elhauge_2003]
- [Fazio Barber Sherman Rand 2019 Knowledge Does Not Protect Against Illusory Truth Effect][research_fazio_barber_sherman_rand_2019]
- [Feng et al 2012 Syntactic Stylometry for Deception Detection][research_feng_et_al_2012]
- [Goldstein et al 2023 Generative Language Models and Automated Influence Operations][research_goldstein_et_al_2023]
- [Goodfellow Shlens Szegedy 2014 Explaining and Harnessing Adversarial Examples][research_goodfellow_shlens_szegedy_2014]
- [Grimmelmann 2015 The Virtues of Moderation][research_grimmelmann_2015]
- [Hartigan and Hartigan 1985 The Dip Test of Unimodality][research_hartigan_hartigan_1985]
- [Herring 2002 Cyber Violence Recognizing and Resisting Abuse in Online Environments][research_herring_2002]
- [Hine et al 2017 Kek Cucks and God Emperor Trump 4chan Analysis][research_hine_et_al_2017]
- [Jane 2014 Your a Ugly Whorish Slut Gendered Online Harassment][research_jane_2014]
- [Kamenica and Gentzkow 2011 Bayesian Persuasion][research_kamenica_gentzkow_2011]
- [Klonick 2018 The New Governors][research_klonick_2018]
- [Kalpakis et al 2001 Distance Measures for Effective Clustering of ARIMA Time-Series][research_kalpakis_et_al_2001]
- [Kumar et al 2018 Community Interaction and Conflict on the Web][research_kumar_et_al_2018]
- [Kwak Lee Park Moon 2010 What is Twitter a Social Network or News Media][research_kwak_lee_park_moon_2010]
- [Lewis 2018 Alternative Influence Networks on YouTube][research_lewis_2018]
- [Melamed 2006 Exclusionary Conduct Under the Antitrust Laws][research_melamed_2006]
- [Marwick and Caplan 2018 Drinking Male Tears Language Harassment and Trolls][research_marwick_caplan_2018]
- [Marwick and Lewis 2017 Media Manipulation and Disinformation Online][research_marwick_lewis_2017]
- [Massaro and Stryker 2013 Freedom of Speech Liberal Democracy and Emerging Evidence][research_massaro_stryker_2013]
- [Ott et al 2011 Finding Deceptive Opinion Spam][research_ott_et_al_2011]
- [Ott et al 2013 Negative Deceptive Opinion Spam][research_ott_et_al_2013]
- [Papernot et al 2016 Practical Black-Box Attacks against Machine Learning][research_papernot_et_al_2016]
- [Post 1986 The Social Foundations of Defamation Law][research_post_1986]
- [Prosser 1960 Privacy Law][research_prosser_1960]
- [Ravasi et al 2020 Search Engine Ranking Manipulation and Legitimate Content Displacement][research_ravasi_et_al_2020]
- [Ribeiro et al 2020 Auditing Radicalization Pathways on YouTube][research_ribeiro_et_al_2020]
- [Sadasivan et al 2023 Can AI-Generated Text be Reliably Detected][research_sadasivan_et_al_2023]
- [Salganik Dodds Watts 2006 Experimental Study of Inequality and Unpredictability][research_salganik_dodds_watts_2006]
- [Stigler 1971 The Theory of Economic Regulation][research_stigler_1971]
- [Szegedy et al 2013 Intriguing Properties of Neural Networks][research_szegedy_et_al_2013]
- [Urban Karaganis Schofield 2016 Notice and Takedown in Everyday Practice][research_urban_karaganis_schofield_2016]
- [Vasilescu and Casanueva 2016 Review Bombing Detection][research_vasilescu_casanueva_2016]
- [Watts 2002 A Simple Model of Global Cascades on Random Networks][research_watts_2002]
- [Yang et al 2020 Scalable and Generalizable Social Bot Detection][research_yang_et_al_2020]
- [Yang and Menczer 2024 Anatomy of an AI-Powered Malicious Social Botnet][research_yang_menczer_2024]
- [Zannettou et al 2018 Web-Wide Coordinated Behavior Reddit-4chan Analysis][research_zannettou_et_al_2018_reddit_4chan]

[book_marwick_2013]: https://yalebooks.yale.edu/book/9780300209389/status-update/
[book_phillips_2015]: https://mitpress.mit.edu/9780262529877/this-is-why-we-cant-have-nice-things/
[book_rid_2020]: https://us.macmillan.com/books/9780374287269/activemeasures
[ref_4chan_raid_documentation]: https://knowyourmeme.com/memes/subcultures/4chan
[ref_abc_2020_bbb_2010]: https://abcnews.go.com/Blotter/business-bureau-best-ratings-money-buy/story?id=12123843
[ref_ahrefs_domain_rating]: https://ahrefs.com/blog/domain-rating/
[ref_amazon_brand_registry]: https://brandservices.amazon.com/
[ref_amazon_community_guidelines]: https://www.amazon.com/gp/help/customer/display.html?nodeId=GLHXEX85MENUE4XF
[ref_amazon_review_bombing_cases]: https://www.aboutamazon.com/news/policy-news-views/how-amazon-detects-and-prevents-fake-reviews
[ref_amazon_v_thinkexpress_2022]: https://www.aboutamazon.com/news/policy-news-views/amazon-continues-legal-action-against-fake-review-brokers
[ref_australia_defamation_uniform]: https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/nsw/consol_act/da200599/
[ref_barnes_v_yahoo_2009]: https://cdn.ca9.uscourts.gov/datastore/opinions/2009/06/22/05-36189.pdf
[ref_batzel_v_smith_2003]: https://caselaw.findlaw.com/court/us-9th-circuit/1290014.html
[ref_bbb_standards]: https://www.bbb.org/about-bbb/bbb-standards-for-trust
[ref_blockowicz_v_williams_2010]: https://scholar.google.com/scholar_case?case=13022555516218523268
[ref_cahill_v_doe_2005]: https://law.justia.com/cases/delaware/supreme-court/2005/2005-oct-05-4.html
[ref_california_ucl_17200]: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=17200
[ref_christchurch_call]: https://www.christchurchcall.com/
[ref_complaints_board]: https://www.complaintsboard.com/
[ref_cyber_civil_rights_initiative]: https://cybercivilrights.org/
[ref_cyveillance_2015_reverse_seo]: https://www.zerofox.com/blog/reverse-seo-attacks/
[ref_dendrite_v_doe_2001]: https://law.justia.com/cases/new-jersey/appellate-division-published/2001/a2774-00-1.html
[ref_diebold_2004]: https://cyberlaw.stanford.edu/case/online-policy-group-v-diebold-inc
[ref_discord_coordination_reports]: https://discord.com/safety/policies
[ref_dmca_17_usc_512]: https://www.law.cornell.edu/uscode/text/17/512
[ref_dmlp_database]: https://www.dmlp.org/legal-guide
[ref_force_v_facebook_2019]: https://www.ca2.uscourts.gov/decisions/isysquery/2c50f8ea-4b6f-4c0f-b8ec-92f6c2d80a26/1/doc/18-397_opn.pdf
[ref_ftc_consumer_sentinel]: https://www.ftc.gov/enforcement/consumer-sentinel-network
[ref_ftc_roomster_2022]: https://www.ftc.gov/legal-library/browse/cases-proceedings/2223059-roomster-corp
[ref_gamergate_coverage]: https://www.pewresearch.org/internet/2017/07/11/online-harassment-2017/
[ref_germany_netzdg_2017]: https://www.gesetze-im-internet.de/netzdg/
[ref_gertz_v_welch_1974]: https://supreme.justia.com/cases/federal/us/418/323/
[ref_gifct]: https://gifct.org/
[ref_gonzalez_v_google_2023]: https://www.supremecourt.gov/opinions/22pdf/21-1333_6j7a.pdf
[ref_goodreads_review_bombing]: https://www.publishersweekly.com/pw/by-topic/industry-news/publisher-news/article/91018-review-bombing-comes-to-goodreads.html
[ref_google_disavow_tool]: https://support.google.com/webmasters/answer/2648487
[ref_google_manual_actions]: https://support.google.com/webmasters/answer/9044175
[ref_google_panda_2011]: https://developers.google.com/search/blog/2011/02/finding-more-high-quality-sites-in
[ref_google_penguin_2012]: https://developers.google.com/search/blog/2012/04/another-step-to-reward-high-quality
[ref_google_safe_browsing]: https://safebrowsing.google.com/
[ref_google_search_console_malware]: https://support.google.com/webmasters/answer/9679690
[ref_google_search_spam_policies]: https://developers.google.com/search/docs/essentials/spam-policies
[ref_grant_v_torstar_2009]: https://scc-csc.lexum.com/scc-csc/scc-csc/en/item/7837/index.do
[ref_lanham_act_15_usc_1125]: https://www.law.cornell.edu/uscode/text/15/1125
[ref_lenz_v_universal_2015]: https://cdn.ca9.uscourts.gov/datastore/opinions/2015/09/14/13-16106.pdf
[ref_meta_atr]: https://about.fb.com/news/tag/adversarial-threat-report/
[ref_metacritic_review_bombing]: https://www.polygon.com/2019/12/12/21005907/metacritic-users-review-bombing
[ref_milkovich_v_lorain_1990]: https://supreme.justia.com/cases/federal/us/497/1/
[ref_moz_spam_score]: https://moz.com/help/moz-data/spam-score-methodology
[ref_mtm_v_amazon_2015]: https://cdn.ca9.uscourts.gov/datastore/opinions/2015/07/06/14-55184.pdf
[ref_netreputation_com]: https://www.netreputation.com/
[ref_ny_times_sullivan_1964]: https://supreme.justia.com/cases/federal/us/376/254/
[ref_ponemon_institute]: https://www.ponemon.org/
[ref_roommates_2008]: https://cdn.ca9.uscourts.gov/datastore/opinions/2008/04/03/0456916.pdf
[ref_reddit_vote_manipulation_policy]: https://support.reddithelp.com/hc/en-us/articles/360043069012
[ref_reit_nightingale_v_universal_2019]: https://www.eff.org/deeplinks/2019/03/deepfakes-defamation
[ref_reputation_com]: https://www.reputation.com/
[ref_rescuecom_v_google_2009]: https://caselaw.findlaw.com/court/us-2nd-circuit/1230253.html
[ref_right_to_be_forgotten_eu]: https://gdpr.eu/right-to-be-forgotten/
[ref_ripoff_report]: https://www.ripoffreport.com/
[ref_rossi_v_mpaa_2004]: https://cdn.ca9.uscourts.gov/datastore/opinions/2004/02/02/0356075.pdf
[ref_rt_review_bombing]: https://www.polygon.com/2019/1/25/18197776/rotten-tomatoes-captain-marvel-brie-larson-review-bombing-scores-anti-fans
[ref_section_230_cda]: https://www.law.cornell.edu/uscode/text/47/230
[ref_speech_act_2010]: https://www.congress.gov/bill/111th-congress/house-bill/2765
[ref_telegram_coordination_reports]: https://telegram.org/faq#q-what-is-telegram-what-do-i-do-here
[ref_trustpilot_transparency]: https://uk.business.trustpilot.com/reviews/build-trusted-brand/trustpilot-transparency-report
[ref_twitter_mass_reporting_analysis]: https://transparency.twitter.com/en/reports/moderation-research.html
[ref_uk_defamation_act_2013]: https://www.legislation.gov.uk/ukpga/2013/26/contents
[ref_wikipedia_spi]: https://en.wikipedia.org/wiki/Wikipedia:Sockpuppet_investigations
[ref_yelp_v_hadeed_2014]: https://law.justia.com/cases/virginia/supreme-court/2015/141531.html
[ref_youtube_trademark_policy]: https://support.google.com/youtube/answer/2801979
[ref_zeran_v_aol_1997]: https://law.justia.com/cases/federal/appellate-courts/F3/129/327/565056/
[ref_zervos_v_trump]: https://law.justia.com/cases/new-york/other-courts/2018/2018-ny-slip-op-28074.html
[related_post_a277_theory]: {% post_url 2026-01-22-virtual_reputation_manipulation_theory %}
[related_post_a278_self_promotion]: {% post_url 2026-01-23-virtual_reputation_manipulation_self_promotion %}
[research_chandrasekharan_et_al_2017]: https://dl.acm.org/doi/10.1145/3134666
[research_cresci_2020]: https://cacm.acm.org/magazines/2020/10/247594-a-decade-of-social-bot-detection/
[research_fazio_barber_sherman_rand_2019]: https://psycnet.apa.org/record/2019-56321-001
[research_feng_et_al_2012]: https://aclanthology.org/P12-2033/
[research_goldstein_et_al_2023]: https://arxiv.org/abs/2301.04246
[research_hartigan_hartigan_1985]: https://www.jstor.org/stable/2241144
[research_hine_et_al_2017]: https://ojs.aaai.org/index.php/ICWSM/article/view/14893
[research_kalpakis_et_al_2001]: https://ieeexplore.ieee.org/document/989531
[research_kumar_et_al_2018]: https://dl.acm.org/doi/10.1145/3178876.3186141
[research_lewis_2018]: https://datasociety.net/library/alternative-influence/
[research_marwick_caplan_2018]: https://journals.sagepub.com/doi/10.1177/0163443718772107
[research_marwick_lewis_2017]: https://datasociety.net/library/media-manipulation-and-disinfo-online/
[research_massaro_stryker_2013]: https://arizonalawreview.org/pdf/54-4/54arizlrev1287.pdf
[research_ott_et_al_2011]: https://aclanthology.org/P11-1032/
[research_ott_et_al_2013]: https://aclanthology.org/N13-1053/
[research_ravasi_et_al_2020]: https://arxiv.org/abs/2005.14400
[research_sadasivan_et_al_2023]: https://arxiv.org/abs/2303.11156
[research_urban_karaganis_schofield_2016]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2755628
[research_vasilescu_casanueva_2016]: https://arxiv.org/abs/1605.09105
[research_yang_et_al_2020]: https://onlinelibrary.wiley.com/doi/10.1002/hbe2.115
[research_yang_menczer_2024]: https://arxiv.org/abs/2307.16336
[research_zannettou_et_al_2018_reddit_4chan]: https://arxiv.org/abs/1801.09288
[book_citron_2014]: https://www.hup.harvard.edu/books/9780674659902
[ref_atlantic_council_dfrlab]: https://dfrlab.org/
[ref_automattic_v_steiner_2016]: https://www.eff.org/cases/automattic-v-steiner
[ref_bartnicki_v_vopper_2001]: https://supreme.justia.com/cases/federal/us/532/514/
[ref_bellingcat]: https://www.bellingcat.com/resources/how-tos/
[ref_cardi_b_v_kebe_2022]: https://ca11.uscourts.gov/opinions/pub/files/202212827.pdf
[ref_carroll_v_trump_2023]: https://cases.justia.com/federal/appellate-courts/ca2/22-3140/22-3140-2023-12-13.pdf
[ref_copyright_office_512_study]: https://www.copyright.gov/policy/section512/section-512-full-report.pdf
[ref_doe_v_myspace_2008]: https://law.justia.com/cases/federal/appellate-courts/F3/528/413/525193/
[ref_dow_jones_v_gutnick_2002]: https://www.austlii.edu.au/cgi-bin/viewdoc/au/cases/cth/HCA/2002/56.html
[ref_ftc_v_amazon_2023]: https://www.ftc.gov/legal-library/browse/cases-proceedings/2223050-amazoncom-inc-prime
[ref_godfrey_v_demon_1999]: https://www.5rb.com/case/godfrey-v-demon-internet/
[ref_google_transparency_dmca]: https://transparencyreport.google.com/copyright/overview
[ref_graphika_reports]: https://graphika.com/reports
[ref_heard_v_depp_2022]: https://www.courts.state.va.us/opinions/opncavwp/1602222.pdf
[ref_herrick_v_grindr_2019]: https://www.ca2.uscourts.gov/decisions/isysquery/85d0e5df-2d4b-4a1a-b4b7-8ba15c8de1f9/1/doc/18-396_opn.pdf
[ref_klayman_v_zuckerberg_2014]: https://www.cadc.uscourts.gov/internet/opinions.nsf/E5C3EB0E1F9EF8E185257CEC004E3AC0/$file/13-7017-1493974.pdf
[ref_loutchansky_v_times_2001]: https://www.5rb.com/case/loutchansky-v-times-newspapers/
[ref_lumen_database]: https://lumendatabase.org/
[ref_mcalpine_v_bercow_2013]: https://www.5rb.com/case/mcalpine-v-bercow/
[ref_meta_cib_report_archive]: https://about.fb.com/news/tag/coordinated-inauthentic-behavior/
[ref_meta_community_standards]: https://transparency.meta.com/policies/community-standards/
[ref_nemet_v_consumeraffairs_2009]: https://law.justia.com/cases/federal/appellate-courts/ca4/08-2097/08-2097-2009-12-29.html
[ref_ouellette_v_viacom_2013]: https://scholar.google.com/scholar_case?case=17232987395091854023
[ref_palin_v_nyt_2022]: https://www.nysd.uscourts.gov/case/1:2017cv04853
[ref_perfect_10_v_ccbill_2007]: https://caselaw.findlaw.com/court/us-9th-circuit/1050063.html
[ref_reddit_content_policy]: https://www.redditinc.com/policies/content-policy
[ref_tiktok_community_guidelines_general]: https://www.tiktok.com/community-guidelines/
[ref_x_terms_of_service]: https://x.com/en/tos
[ref_youtube_community_guidelines_strikes]: https://support.google.com/youtube/answer/2802032
[research_ribeiro_et_al_2020]: https://dl.acm.org/doi/10.1145/3351095.3372879
[book_andrew_mitrokhin_1999]: https://www.basicbooks.com/titles/christopher-andrew/the-sword-and-the-shield/9780465003129/
[book_ansolabehere_iyengar_1996]: https://www.simonandschuster.com/books/Going-Negative/Stephen-Ansolabehere/9780028740140
[book_baldasty_1992]: https://uwapress.uw.edu/book/9780299134044/the-commercialization-of-news-in-the-nineteenth-century/
[book_boorstin_1961]: https://www.penguinrandomhouse.com/books/28626/the-image-by-daniel-j-boorstin/
[book_bork_1978]: https://www.basicbooks.com/titles/robert-h-bork/the-antitrust-paradox/9780029044568/
[book_franklin_anderson_cate_2016]: https://www.westacademic.com/Casebook/Mass-Media-Law-Cases-and-Materials-9th-Franklin
[book_franks_2019]: https://www.sup.org/books/title/?id=29663
[book_geer_2006]: https://press.uchicago.edu/ucp/books/book/chicago/I/bo3766942.html
[book_kelly_1988]: https://www.wiley.com/en-us/Surviving+Sexual+Violence-p-9780745605739
[book_kiernan_1988]: https://global.oup.com/academic/product/the-duel-in-european-history-9780198205036
[book_loveland_2000]: https://www.hart.oup.com/political-libels
[book_mark_2006]: https://rowman.com/ISBN/9780742551169
[book_michaels_2008]: https://global.oup.com/academic/product/doubt-is-their-product-9780195300673
[book_michaels_2020]: https://global.oup.com/academic/product/the-triumph-of-doubt-9780190922665
[book_nasaw_2000]: https://www.hmhbooks.com/shop/books/The-Chief/9780618154463
[book_oreskes_conway_2010]: https://www.bloomsbury.com/us/merchants-of-doubt-9781608193943/
[book_posner_2001]: https://press.uchicago.edu/ucp/books/book/chicago/A/bo3626728.html
[book_prosser_keeton_1984]: https://www.westacademic.com/Casebook/Prosser-and-Keeton-on-Torts-5th-9780314745774
[book_rosenberg_1986]: https://uncpress.org/book/9780807817124/protecting-the-best-men/
[book_siebert_1965]: https://uipress.press.uillinois.edu/books/?id=p066395
[book_singer_brooking_2018]: https://www.hmhbooks.com/shop/books/LikeWar/9781328695741
[book_sunstein_2018]: https://press.princeton.edu/books/hardcover/9780691180908/republic
[book_weiner_2007]: https://www.penguinrandomhouse.com/books/198540/legacy-of-ashes-by-tim-weiner/
[book_wills_1970]: https://www.penguinrandomhouse.com/books/319898/nixon-agonistes-by-garry-wills/
[book_woolley_howard_2018]: https://global.oup.com/academic/product/computational-propaganda-9780190931414
[book_zehr_2002]: https://www.goodbooks.com/little-book-of-restorative-justice/
[ref_47_usc_223]: https://www.law.cornell.edu/uscode/text/47/223
[ref_anti_slapp_tracker]: https://anti-slapp.org/
[ref_birther_campaign]: https://www.washingtonpost.com/politics/how-obama-birther-conspiracy-theory-came-to-mainstream-politics/2016/09/16/
[ref_california_anti_slapp]: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=425.16
[ref_cyberstalking_18_usc_2261a]: https://www.law.cornell.edu/uscode/text/18/2261A
[ref_dmca_512f]: https://www.law.cornell.edu/uscode/text/17/512
[ref_eu_anti_slapp_2024]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024L1069
[ref_restatement_second_torts]: https://www.ali.org/publications/show/torts/
[ref_section_230_c2]: https://www.law.cornell.edu/uscode/text/47/230
[ref_sherman_act_15_usc_2]: https://www.law.cornell.edu/uscode/text/15/2
[ref_swift_boat_2004]: https://www.pbs.org/newshour/politics/campaign-2004-swift-boat-veterans-for-truth
[ref_upepa]: https://www.uniformlaws.org/committees/community-home?CommunityKey=4f486460-199c-49d7-9fac-05570be1e7b1
[ref_willie_horton_1988]: https://www.pbs.org/wgbh/pages/frontline/shows/pres/campaigns/1988.html
[research_anderson_1991]: https://scholar.google.com/scholar?q=anderson+1991+reputation+compensation+punishment+suppression
[research_areeda_turner_1975]: https://scholar.google.com/scholar?q=areeda+turner+1975+predatory+pricing
[research_balkin_2018]: https://www.uclawreview.org/2018/12/free-speech-is-a-triangle/
[research_barabasi_albert_1999]: https://www.science.org/doi/10.1126/science.286.5439.509
[research_bikhchandani_hirshleifer_welch_1992]: https://www.jstor.org/stable/2138632
[research_carlini_wagner_2017]: https://ieeexplore.ieee.org/document/7958570
[research_douek_2021]: https://harvardlawreview.org/2021/06/governing-online-speech-from-posts-as-trumps-to-proportionality-and-probability/
[research_elhauge_2003]: https://scholar.google.com/scholar?q=elhauge+2003+defining+better+monopolization
[research_goodfellow_shlens_szegedy_2014]: https://arxiv.org/abs/1412.6572
[research_grimmelmann_2015]: https://yalejreg.com/print/the-virtues-of-moderation/
[research_herring_2002]: https://www.tandfonline.com/doi/abs/10.1108/10748120210424879
[research_jane_2014]: https://journals.sagepub.com/doi/10.1177/1367877913513494
[research_kamenica_gentzkow_2011]: https://www.aeaweb.org/articles?id=10.1257/aer.101.6.2590
[research_klonick_2018]: https://harvardlawreview.org/2018/04/the-new-governors-the-people-rules-and-processes-governing-online-speech/
[research_kwak_lee_park_moon_2010]: https://dl.acm.org/doi/10.1145/1772690.1772751
[research_melamed_2006]: https://scholar.google.com/scholar?q=melamed+2006+exclusionary+conduct+antitrust
[research_papernot_et_al_2016]: https://arxiv.org/abs/1602.02697
[research_post_1986]: https://www.jstor.org/stable/1341064
[research_prosser_1960]: https://www.jstor.org/stable/1341064
[research_salganik_dodds_watts_2006]: https://www.science.org/doi/10.1126/science.1121066
[research_stigler_1971]: https://www.jstor.org/stable/3003160
[research_szegedy_et_al_2013]: https://arxiv.org/abs/1312.6199
[research_watts_2002]: https://www.pnas.org/doi/10.1073/pnas.082090499
