---
layout: post
mathjax: true
comments: true
title: "History of SpaceX: Portfolio Patience and the Internalization of Tail Risk"
date: 2026-08-01 09:00:00 +0000
categories: history business aerospace
series: spacex_history
series_title: History of SpaceX
series_index: 8
---

<!-- A288 -->
<script>console.log("A288");</script>

This article is the eighth in the History of SpaceX series and treats the portfolio-patience forcing-function condition that the [series opener][related_post_a281_spacex_framing] introduced as the seventh and final forcing-function condition in the seven-plus-three analytical framework. The portfolio-patience condition requires that a mission-directed technology venture hold several revenue-bearing lines whose failure modes are imperfectly correlated, so that no single adverse outcome terminates the venture, and that the venture sustain each line across the interval before it returns anything. The condition is distinguished from ordinary corporate diversification by two features that the article develops at length. The lines are generated from a single capability base and not assembled by acquisition, and the quantity being diversified is not the variance of the return but the probability that the venture ceases to exist before the mission is reached. The article walks the SpaceX portfolio composition through the launch-service line, the spacecraft line comprising Dragon 1 and Dragon 2, the constellation line comprising Starlink, the defense-services line comprising Starshield and the national-security launch business, and the next-generation vehicle line comprising Starship and Super Heavy. The article treats the cross-subsidization flows among the lines and the internal capital market through which they are directed, and it treats the correlation structure that determines whether the portfolio in fact reduces the ruin probability or merely appears to. The article engages at length with the strongest objection the finance literature raises, namely the conglomerate discount that [Lang and Stulz 1994][research_lang_stulz_1994] and [Berger and Ofek 1995][research_berger_ofek_1995] document and that [Scharfstein and Stein 2000][research_scharfstein_stein_2000] The Dark Side of Internal Capital Markets explains, under which internalized diversification destroys value because investors can diversify more cheaply themselves. The article contrasts the SpaceX configuration against the Iridium single-bet failure of 1999, the Superconducting Super Collider cancellation of 1993, and the contemporary single-bet failures at OneWeb and Virgin Orbit. The article closes with an explicit pattern-extraction section stating the abstract portfolio-patience mechanic in a form other informed readers can recognize in adjacent domains without naming any downstream application.

## The Portfolio-Patience Mapping Problem

The mapping problem for a comprehensive treatment of the portfolio-patience condition in the SpaceX case is the question of which lines the firm has held simultaneously, what correlation structure their returns exhibit, what transfers have flowed among them, and whether the resulting configuration in fact reduced the probability of termination relative to the counterfactual in which the firm pursued the mission through a single line.

The problem permits several formalizations. The portfolio-selection tradition from [Markowitz 1952][research_markowitz_1952] Portfolio Selection and [Markowitz 1959][book_markowitz_1959] through [Sharpe 1964][research_sharpe_1964] Capital Asset Prices and [Lintner 1965][research_lintner_1965] treats the problem as a mean-variance optimization over an asset set, and it offers the formal apparatus the article adapts. The corporate-diversification tradition from [Lewellen 1971][research_lewellen_1971] A Pure Financial Rationale for the Conglomerate Merger through [Amihud and Lev 1981][research_amihud_lev_1981] Risk Reduction as a Managerial Motive, [Lang and Stulz 1994][research_lang_stulz_1994], [Berger and Ofek 1995][research_berger_ofek_1995] Diversification's Effect on Firm Value, [Montgomery 1994][research_montgomery_1994] Corporate Diversification, [Rajan et al. 2000][research_rajan_servaes_zingales_2000] The Cost of Diversity, and [Villalonga 2000][research_villalonga_2004] treats the problem as one of whether the firm should diversify at all, and it returns a substantially negative answer that the article must confront, not evade. The internal-capital-markets tradition from [Gertner et al. 1994][research_gertner_scharfstein_stein_1994] Internal versus External Capital Markets, [Stein 1997][research_stein_1997] Internal Capital Markets and the Competition for Corporate Resources, and [Scharfstein and Stein 2000][research_scharfstein_stein_2000] treats the allocation mechanism among the lines. The real-options tradition from [Myers 1977][research_myers_1977] through [Dixit and Pindyck 1994][book_dixit_pindyck_1994] and [Trigeorgis 1996][book_trigeorgis_1996] treats the portfolio as a collection of options and not as a collection of cash-flow streams. The present article draws on all four traditions while adopting the mission-oriented-innovation framework the [series opener][related_post_a281_spacex_framing] established as primary.

The general form of the problem can be stated compactly. Let $\mathcal{L} = \{1, \ldots, L\}$ index the lines and let $R_\ell(t)$ denote the return of the line $\ell$ at time $t$. The portfolio return may be written

$$
R^{\text{portfolio}}(t) = \sum_{\ell \in \mathcal{L}} w_\ell(t) \, R_\ell(t) \qquad \text{with} \qquad \sum_{\ell} w_\ell(t) = 1
\tag{1}
$$

and the portfolio variance admits the standard form

$$
\sigma^2_{\text{portfolio}} = \sum_{\ell} \sum_{m} w_\ell w_m \, \rho_{\ell m} \, \sigma_\ell \sigma_m
\tag{2}
$$

with $\rho_{\ell m}$ the correlation between the lines $\ell$ and $m$. The variance falls below the weighted average of the line variances whenever the correlations are less than unity, which is the elementary result on which the entire condition rests and which is also the result whose applicability to this case is least obvious.

The quantity the condition actually concerns is not the variance. A mission-directed venture is not indifferent between a distribution with a given variance and a distribution with the same variance shifted so that a portion of its mass lies below the point at which the venture ceases to operate. The relevant object is the ruin probability

$$
P^{\text{ruin}}(T) = P\!\left( \exists \, t \leq T \; : \; C(t) \leq 0 \right)
\tag{3}
$$

with $C(t)$ the cash position and the event being the first passage below zero. The distinction between variance reduction and ruin-probability reduction is the analytical hinge of this article, because the two objectives recommend different portfolios and because substantially the entire corporate-diversification literature evaluates the former.

The relationship between the portfolio composition and the ruin probability takes the compact statement that for a portfolio of lines with independent failure events,

$$
P^{\text{ruin}}_{\text{portfolio}} \approx \prod_{\ell \in \mathcal{L}} P^{\text{failure}}_\ell \qquad \text{against} \qquad P^{\text{ruin}}_{\text{single bet}} = P^{\text{failure}}_1
\tag{4}
$$

with the product falling rapidly in the line count when the failures are independent and collapsing to the single-bet expression when they are perfectly correlated. The general object the analysis requires is therefore the full correlation matrix

$$
\boldsymbol{\rho} = \left[ \rho_{\ell m} \right]_{\ell, m \in \mathcal{L}}
\tag{5}
$$

, not any summary of it, because the ruin probability depends on the joint distribution of the adverse events and not on their marginal probabilities. The empirical question for the SpaceX case is where between the two extremes the realized correlation structure lies, and the answer the article develops is that it lies substantially closer to the correlated extreme than the line count alone would suggest, because the lines share a launch vehicle.

The identification problem is that the counterfactual is unobservable in the same way it was for the governance condition. The counterfactual differential has the concise form

$$
\Delta V^{\text{portfolio}}_i(t) = V^{\text{observed}}_i(t) - V^{\text{single-line counterfactual}}_i(t)
\tag{6}
$$

with the attribution equal to the difference between the observed trajectory and the counterfactual in which the firm pursued the mission through a single line. The counterfactual specifications the article treats include a launch-services-only counterfactual, a constellation-only counterfactual of the kind the Iridium case realizes, and a Starship-only counterfactual in which the firm forgoes the revenue-bearing lines entirely.

## Methodological Commitments

The article commits to the same seven methodological positions the [series opener][related_post_a281_spacex_framing] established. These are restated at compact reference level with attention to the ways the portfolio material strains them.

The first commitment is descriptive-analytical framing, not prescriptive advocacy.

The second commitment is dual-register composition with both general-history and abstract-mechanic registers.

The third commitment is primary-source anchoring. The article cites primary sources with preference for the [SpaceX news archive][ref_spacex_news_archive], the [SpaceX Falcon 9 vehicle documentation][ref_spacex_falcon9_vehicle], the [SpaceX Falcon Heavy vehicle documentation][ref_spacex_falcon_heavy_vehicle], the [SpaceX Starship vehicle documentation][ref_spacex_starship_vehicle], the [Starlink service documentation][ref_spacex_starlink], the [SpaceX Starshield documentation][ref_spacex_starshield], the [FAA current launch licenses][ref_faa_ast], the [FCC Starlink authorizations][ref_fcc_starlink_2018] and [FCC Starlink Gen2 authorizations][ref_fcc_starlink_gen2_2022], the [NASA Commercial Crew Program documentation][ref_nasa_ccp_documents], the [NASA Human Landing System program documentation][ref_nasa_hls_program], and the [Space Force National Security Space Launch][ref_space_force_nssl] framework and the [Space Force news][ref_space_force_news], the [Department of Defense contract announcements][ref_dod_contracts], the [NASA Commercial Resupply Services program overview][ref_nasa_crs_program_overview], the [Securities and Exchange Commission EDGAR][ref_sec_edgar] system, and the [United States Bankruptcy Code Chapter 11][ref_bankruptcy_code_ch11] provisions under which the negation cases were resolved. The article draws on secondary sources including [Berger 2021][book_berger_2021] Liftoff, [Berger 2024][book_berger_2024] Reentry, [Vance 2015][book_vance_2015] Elon Musk, [Isaacson 2023][book_isaacson_2023] Elon Musk, [Davenport 2018][book_davenport_2018] The Space Barons, and [Fernholz 2018][book_fernholz_2018] Rocket Billionaires.

The fourth commitment is contested-claim marking. The commitment binds heavily here. The per-line revenue figures, the margins, and above all the internal transfer prices at which one line charges another are not disclosed. The transfer price is the single most important unobserved quantity in this article, because substantially every claim about cross-subsidization depends on it.

The fifth commitment is temporal indexing as a mid-2026 snapshot.

The sixth commitment is terminological transparency with the Terminological Note section below, with attention to the distinction between decomposability and portfolio patience that the [Decomposability article A285][related_post_a285_spacex_decomposability] and the present article respectively treat.

The seventh commitment is thesis-not-proof framing of the portfolio-patience closure claim.

## Portfolio Patience as an Economic Property

The portfolio-patience property is treated as an economic property of a firm's line composition and capital-allocation practice that distinguishes ventures able to survive an adverse outcome in any single line from ventures whose continued existence is contingent on a single outcome.

The property has two components that the name joins and that are analytically separable. The portfolio component concerns the composition of the line set at an instant. The patience component concerns the willingness to sustain a line across the interval before it returns anything. A venture can hold a diversified portfolio without patience, in which case it terminates each line at the first adverse signal and holds a portfolio of short-lived undertakings. A venture can exhibit patience without a portfolio, in which case it is the single-bet configuration the negation cases illustrate. The condition requires both.

The patience component permits formalization through the horizon over which the venture evaluates a line. Let $\tau_\ell$ denote the interval the venture will sustain the line $\ell$ before requiring a positive return, and let $\tau^{\ast}\_\ell$ denote the interval the line in fact requires. The patience condition is

$$
\tau_\ell \geq \tau^{\ast}_\ell \qquad \forall \ell \in \mathcal{L}
\tag{7}
$$

and the condition fails for a venture whose evaluation horizon is set by an external party with a shorter horizon. The patience allows equivalent expression as a discount rate and not as a horizon, through the correspondence

$$
\tau_\ell \; \longleftrightarrow \; \rho_\ell \qquad \text{with} \qquad \frac{\partial \tau_\ell}{\partial \rho_\ell} < 0
\tag{8}
$$

with a lower discount rate and a longer tolerated horizon being two descriptions of the same underlying parameter. The formulation is useful because it connects the patience component directly to the horizon divergence between controller and investor that the [Governance article A287][related_post_a287_spacex_governance] formalizes. The connection to the [Governance article A287][related_post_a287_spacex_governance] is direct and is the reason the two conditions are adjacent in the framework. The governance configuration is what permits $\tau_\ell$ to be set by the controller, not by the capital market, and without it the patience component cannot be satisfied whatever the portfolio composition.

The portfolio component supports formalization through the effective line count. A portfolio of $L$ lines with pairwise correlation $\rho$ behaves for variance purposes like a portfolio of

$$
L^{\text{effective}} = \frac{L}{1 + (L-1)\rho}
\tag{9}
$$

independent lines, which equals $L$ when $\rho = 0$ and collapses to unity when $\rho = 1$ irrespective of the nominal count. The expression is the reason a nominal portfolio of five lines may supply substantially less protection than the count suggests, and it is the quantity the article attempts to estimate for the SpaceX case.

The asymmetry between variance and ruin deserves formal statement. Under a standard mean-variance objective the venture maximizes

$$
U = E\!\left[ R^{\text{portfolio}} \right] - \tfrac{\gamma}{2} \sigma^2_{\text{portfolio}}
\tag{10}
$$

and under a survival objective it maximizes

$$
U^{\text{survival}} = P\!\left( \text{reach } M \right) = 1 - P^{\text{ruin}}(T^{\text{mission}})
\tag{11}
$$

with the two objectives coinciding only under restrictive distributional assumptions. The survival objective is indifferent to upside variance entirely and is concerned exclusively with the left tail, which recommends a portfolio weighted toward lines whose returns are positive in the states where the other lines fail and not toward lines with high expected returns.

The cross-subsidization flow admits the compact definition

$$
f_{\ell \to m}(t) = \text{capital directed from line } \ell \text{ to line } m \text{ at } t
\tag{12}
$$

with the net position of the line $\ell$ given by

$$
n_\ell(t) = \sum_{m} f_{m \to \ell}(t) - \sum_{m} f_{\ell \to m}(t)
\tag{13}
$$

and a line exhibiting persistently negative $n_\ell$ constituting a source and a line exhibiting persistently positive $n_\ell$ constituting a sink. The mission-directed configuration is characterized by the pattern in which the revenue-bearing lines are sources and the mission-critical line is the dominant sink.

The capability-base identity distinguishes the configuration from a conglomerate. Let $K_\ell$ denote the capability set the line $\ell$ requires. The configuration is a generated portfolio when

$$
\bigcap_{\ell \in \mathcal{L}} K_\ell \neq \varnothing \qquad \text{and} \qquad \left| \bigcap_{\ell} K_\ell \right| \big/ \left| \bigcup_{\ell} K_\ell \right| \gg 0
\tag{14}
$$

with a substantial fraction of the total capability shared across every line, and it is an assembled portfolio when the intersection is empty. The distinction is the whole of the response to the conglomerate-discount objection, and the quantity in the second expression is the one the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] establishes is large for this case.

## Cross-Disciplinary Framings

The portfolio-patience property admits characterization from several disciplinary traditions beyond the mission-oriented-innovation framework the series adopts as primary.

The portfolio-selection tradition traces from [Markowitz 1952][research_markowitz_1952] and [Markowitz 1959][book_markowitz_1959] Portfolio Selection through [Sharpe 1964][research_sharpe_1964] and [Lintner 1965][research_lintner_1965]. The framing provides the mean-variance apparatus and gives equally the reason that apparatus is a poor fit for the case. The efficiency criterion the tradition offers takes the form

$$
S = \frac{E\!\left[R^{\text{portfolio}}\right] - r_f}{\sigma_{\text{portfolio}}}
\tag{15}
$$

with the ratio maximized along the efficient frontier. The criterion is the one the article argues is inapplicable, because a venture that reaches its mission with a low ratio has succeeded and one that fails to reach it with a high ratio has not. The theory assumes an investor who can hold a fractional position in every asset and who is compensated only for non-diversifiable risk. A mission-directed venture holds an indivisible position in an undertaking it cannot sell, and the risk it most needs to reduce is precisely the idiosyncratic risk the theory says the market does not compensate.

The corporate-diversification tradition traces from [Lewellen 1971][research_lewellen_1971] through [Amihud and Lev 1981][research_amihud_lev_1981], [Lang and Stulz 1994][research_lang_stulz_1994] Tobin's q Corporate Diversification and Firm Performance, [Berger and Ofek 1995][research_berger_ofek_1995], [Montgomery 1994][research_montgomery_1994], [Rajan et al. 2000][research_rajan_servaes_zingales_2000], and [Villalonga 2000][research_villalonga_2004] Does Diversification Cause the Diversification Discount. The framing returns the finding that diversified firms trade at a discount to the sum of their parts, and it gives the two standard explanations comprising the investor's ability to diversify more cheaply and the misallocation internal capital markets produce. The excess-value measure the tradition constructs can be written as

$$
EV = \ln\!\left( \frac{V^{\text{observed}}}{\sum_\ell m_\ell \cdot A_\ell} \right)
\tag{16}
$$

with $m_\ell$ an industry median valuation multiple and $A_\ell$ an accounting base for the segment, and with the measure reported as significantly negative across the diversified samples. The framing constitutes the principal objection to the portfolio-patience condition, and the article treats it in a dedicated section, not in passing.

The internal-capital-markets tradition traces from [Gertner et al. 1994][research_gertner_scharfstein_stein_1994], [Stein 1997][research_stein_1997], and [Scharfstein and Stein 2000][research_scharfstein_stein_2000]. The framing yields both the case for internal allocation, resting on the headquarters ability to engage in winner-picking with information an external market lacks, and the case against it, resting on the rent-seeking by division managers that the dark-side treatment documents. The allocation quality has the form

$$
Q^{\text{allocation}} = \operatorname{corr}\!\left( \Delta k_\ell, \; q_\ell \right)
\tag{17}
$$

with $\Delta k_\ell$ the capital directed to the line and $q_\ell$ the investment opportunity of the line, and with an efficient internal market exhibiting a positive correlation and a socialistic one exhibiting a correlation near zero.

The real-options tradition traces from [Myers 1977][research_myers_1977] through [Black and Scholes 1973][research_black_scholes_1973], [Merton 1973][research_merton_1973], [McDonald and Siegel 1986][research_mcdonald_siegel_1986], [Kogut and Kulatilaka 1994][research_kogut_kulatilaka_1994], [Dixit and Pindyck 1994][book_dixit_pindyck_1994], [Trigeorgis 1996][book_trigeorgis_1996], and [Copeland and Antikarov 2001][book_copeland_antikarov_2001]. The framing treats each line as an option and the portfolio as an option portfolio, and it contributes the important observation that a portfolio of options is worth more than an option on a portfolio. The inequality may be written

$$
\sum_{\ell} E\!\left[ \max(V_\ell - K_\ell, 0) \right] \geq E\!\left[ \max\!\left( \sum_\ell V_\ell - \sum_\ell K_\ell, 0 \right) \right]
\tag{18}
$$

with the separately exercisable options dominating the bundled one. The result is the formal statement of why holding the lines as distinguishable undertakings that can be independently continued or abandoned is worth more than holding them as a single indivisible programme, and it connects the portfolio-patience condition directly to the decomposability condition the [Decomposability article A285][related_post_a285_spacex_decomposability] treats.

The ruin-theory and survival-analysis tradition yields the apparatus the article argues is the correct one. The tradition treats the first-passage problem for a capital process and evaluates a configuration by the probability that the process reaches an absorbing barrier before a horizon. The classical result the tradition provides bounds the ruin probability exponentially in the initial capital

$$
P^{\text{ruin}}(\infty) \leq e^{-\Lambda \, C(0)}
\tag{19}
$$

with $\Lambda$ an adjustment coefficient increasing in the safety loading of the revenue process over the claim process. The form makes explicit that an increase in the sustained revenue margin reduces the ruin probability exponentially and not linearly, which is the reason a modest recurring revenue line is worth substantially more to a venture facing a ruin barrier than its magnitude suggests. The framing is standard in the insurance and reliability literatures that [O'Connor and Kleyner 2012][book_oconnor_kleyner_2012] Practical Reliability Engineering represents, and it is substantially absent from the corporate-diversification literature, which is the reason that literature and the present article reach different conclusions from the same evidence.

The corporate-strategy tradition traces from [Chandler 1962][book_chandler_1962] Strategy and Structure, [Chandler 1977][book_chandler_1977] The Visible Hand, and [Chandler 1990][book_chandler_1990] Scale and Scope through [Penrose 1959][book_penrose_1959] The Theory of the Growth of the Firm, [Porter 1980][book_porter_1980] Competitive Strategy, [Porter 1985][book_porter_1985] Competitive Advantage, and the diversification-strategy strand that [Montgomery 1994][research_montgomery_1994] surveys. The [Penrose 1959][book_penrose_1959] treatment contributes the most useful antecedent, because it explains firm growth through the redeployment of underused resources into adjacent activities. The mechanism admits the compact statement through a slack measure

$$
\Sigma(t) = \sum_{k \in K} \left[ \bar{u}_k - u_k(t) \right]^{+}
\tag{20}
$$

with $\bar{u}\_k$ the capacity of the capability $k$ and $u_k(t)$ its utilization, and with a positive slack constituting the resource from which a new line can be generated at a marginal, not a full cost. The expression is the formal statement of why the lines were generated and not acquired, and it is the quantity that distinguishes this growth path from an acquisitive one.

The platform and ecosystem tradition traces from [Meyer and Lehnerd 1997][book_meyer_lehnerd_1997] The Power of Product Platforms, [Sanderson and Uzumeri 1997][book_sanderson_uzumeri_1997] Managing Product Families, [Robertson and Ulrich 1998][research_robertson_ulrich_1998], [Baldwin and Clark 2000][book_baldwin_clark_2000] Design Rules, [Gawer and Cusumano 2002][book_cusumano_gawer_2002] Platform Leadership, [Iansiti and Levien 2004][book_iansiti_levien_2004] The Keystone Advantage, [Adner 2012][book_adner_2012] The Wide Lens, [Adner 2021][book_adner_2021] Winning the Right Game, [Adner and Kapoor 2009][research_adner_kapoor_2010], and [Jacobides et al. 2018][research_jacobides_et_al_2018]. The framing treats the shared capability base as a platform from which the lines derive. The platform leverage permits the concise form

$$
\Lambda^{\text{platform}} = \frac{\sum_{\ell} V_\ell}{C^{\text{shared base}}}
\tag{21}
$$

with the leverage rising in the line count for a fixed base cost. The expression supplies the vocabulary in which the generated-versus-assembled distinction is naturally expressed, because an assembled portfolio has no shared base in the denominator and therefore no leverage of the kind the expression measures.

The supply-chain and clockspeed tradition traces from [Fine 1998][book_fine_1998] Clockspeed and [Cusumano 2010][book_cusumano_2010] Staying Power. The framing offers the observation that the rate at which an industry's architecture changes determines how long a position remains defensible. The decay takes the form

$$
A_\ell(t) = A_\ell(0) \, e^{-\kappa_\ell t}
\tag{22}
$$

with $\kappa_\ell$ the clockspeed of the line's industry and with the advantage decaying faster in the faster-moving segment. The portfolio therefore mixes lines with different decay constants, and a portfolio weighted toward high-$\kappa$ lines requires a higher rate of replenishment to hold its position than one weighted toward low-$\kappa$ lines.

The organizational-ecology and failure tradition traces from [Ormerod 2005][book_ormerod_2005] Why Most Things Fail, [Kauffman 1993][book_kauffman_1993] The Origins of Order, [Beinhocker 2006][book_beinhocker_2006] The Origin of Wealth, [Nelson and Winter 1982][book_nelson_winter_1982] An Evolutionary Theory of Economic Change, and [Metcalfe 1998][book_metcalfe_1998] Evolutionary Economics and Creative Destruction. The framing gives the base rates against which any claim about the reduction of a failure probability should be assessed, and the base rates are unfavorable to ventures of substantially every description. The venture-failure literature that the [Why Startups Actually Fail article A167][related_post_a167_startup_failure] surveys provides the proximate-cause distribution against which the single-bet failure mode should be located.

The agency and free-cash-flow tradition traces from [Berle and Means 1932][book_berle_means_1932] The Modern Corporation and Private Property through [Jensen and Meckling 1976][research_jensen_meckling_1976], [Fama and Jensen 1983][research_fama_jensen_1983], [Jensen 1986][research_jensen_1986] Agency Costs of Free Cash Flow, [Shleifer and Vishny 1997][research_shleifer_vishny_1997], [Hart 1995][book_hart_1995] Firms Contracts and Financial Structure, and [Tirole 2006][book_tirole_2006] The Theory of Corporate Finance. The framing yields the sharpest available statement of what the configuration risks, because [Jensen 1986][research_jensen_1986] identifies diversification as the canonical use to which a manager directs a free cash flow that ought to be returned to the claimants. The prediction can be written as

$$
\frac{\partial \, \text{diversification}}{\partial \, \text{free cash flow}} > 0 \qquad \text{under the agency reading}
\tag{23}
$$

with the relation observed empirically across diversified firms. The SpaceX pattern in which a matured line funds an immature one is observationally identical to the pattern the framing predicts, and the two readings are distinguished only by whether the receiving line is judged worth funding, which is the question at issue, not an independent test. The governance apparatus that would ordinarily discipline the behavior is deliberately disabled in this case, as the [Governance article A287][related_post_a287_spacex_governance] documents.

The learning-curve and experience tradition traces from [Wright 1936][research_wright_1936] Factors Affecting the Cost of Airplanes through [Alchian 1963][research_alchian_1963] Reliability of Progress Curves, [Rapping 1965][research_rapping_1965], [Argote and Epple 1990][research_argote_epple_1990] Learning Curves in Manufacturing, [Argote 1999][book_argote_1999] Organizational Learning, [Adler and Clark 1991][research_adler_clark_1991], [Lieberman 1984][research_lieberman_1984], and [Dutton and Thomas 1984][research_dutton_thomas_1984]. The framing bears on the portfolio question through a mechanism the diversification literature omits entirely. A shared production capability accumulates experience from every line simultaneously, so that the learning rate on the shared element scales with the total volume and not with any single line's volume. The effect has the form

$$
c^{\text{shared}}_n = c^{\text{shared}}_1 \left( \sum_{\ell} n_\ell \right)^{-b}
\tag{24}
$$

with the cumulative volume summed across the lines. The expression is a positive interaction among the lines that a portfolio of standalone firms cannot reproduce, and it is a value source the conglomerate-discount literature does not measure because the conglomerates it studied shared no production base.

The modularity and architecture tradition traces from [Simon 1962][research_simon_1962] The Architecture of Complexity through [Ulrich 1995][research_ulrich_1995], [Sanchez and Mahoney 1996][research_sanchez_mahoney_1996], [Baldwin and Woodard 2009][research_baldwin_woodard_2009], [Fixson 2004][research_fixson_2005], [Novak and Eppinger 2001][research_novak_eppinger_2001], [Sosa et al. 2003][research_sosa_eppinger_rowles_2003], [Ethiraj and Levinthal 2004][research_ethiraj_levinthal_2004], [Rivkin and Siggelkow 2003][research_rivkin_siggelkow_2003], and [MacCormack et al. 2012][research_maccormack_baldwin_rusnak_2012]. The framing contributes the structural condition under which a shared base can support multiple lines without the lines interfering with one another, namely that the interfaces be specified and stable. A shared base with unstable interfaces couples the lines, not serving them, which converts the claimed diversification into an additional correlation channel.

The diffusion and dominant-design tradition traces from [Rogers 1962][book_rogers_1962] Diffusion of Innovations through [Utterback 1994][book_utterback_1994] Mastering the Dynamics of Innovation, [Abernathy and Clark 1985][research_abernathy_clark_1985], [Anderson and Tushman 1990][research_anderson_tushman_1990], [Suárez and Utterback 1995][research_suarez_utterback_1995], and [Murmann and Frenken 2006][research_murmann_frenken_2006]. The framing offers the account of the rate at which a line's market matures, which determines the interval across which the patience component must operate for that line.

The reliability and organizational-safety tradition traces from [Perrow 1984][book_perrow_1984] Normal Accidents through [Vaughan 1996][book_vaughan_1996] The Challenger Launch Decision, [Weick and Sutcliffe 2007][book_weick_sutcliffe_2007] Managing the Unexpected, [Musa 1998][book_musa_1998] Software Reliability Engineering, and [Duane 1964][research_duane_1964]. The framing provides the apparatus for the vehicle-reliability common factor that dominates the correlation structure, and its central claim that tightly coupled systems produce accidents as a normal consequence and not as an aberration bears directly on whether the shared-vehicle exposure can be engineered away or must be absorbed.

## The Portfolio Composition at the Drafting Date

The portfolio at the drafting date comprises five lines that the article treats in turn. The enumeration is an analytical choice, not a reported organizational structure, because the firm does not publish a segment breakdown, and a different partition would be defensible. A listed issuer would be required to report operating segments under the disclosure regime that the [Regulation S-K][ref_sec_regulation_sk] provisions and the [Financial Accounting Standards Board][ref_fasb_asc280] segment standard establish, and the absence of that obligation is a direct consequence of the unlisted configuration the [Governance article A287][related_post_a287_spacex_governance] treats.

The launch-service line sells delivery to orbit to external customers. The spacecraft line sells cargo and crew transport to the International Space Station and to private customers. The constellation line sells broadband connectivity to consumer, enterprise, maritime, aviation, and government subscribers. The defense-services line sells classified satellite capability and national-security launch to United States government customers. The next-generation vehicle line comprises the Starship and Super Heavy development and returns substantially nothing at the drafting date.

The line set exhibits a structural feature that the analysis must foreground. Four of the five lines depend on a single launch vehicle family, and the fifth is a launch vehicle. The dependency structure can be stated as

$$
K^{\text{Falcon}} \in K_\ell \qquad \text{for} \qquad \ell \in \{\text{launch}, \text{spacecraft}, \text{constellation}, \text{defense}\}
\tag{25}
$$

with the Falcon capability appearing in the capability set of every revenue-bearing line. The consequence is that a Falcon 9 grounding event propagates to substantially the entire revenue base simultaneously, and the portfolio therefore gives substantially no protection against the single most likely catastrophic operational event. The observation is the principal qualification the article places on the portfolio-patience claim for this case, and the article states it before the favorable material and not after it.

The offsetting consideration is that the correlation structure differs by risk category. The portfolio yields substantially no protection against a vehicle-reliability event and substantially considerable protection against a demand event, a regulatory event, a competitive event, or a customer-budgetary event. The decomposition may be written

$$
\rho_{\ell m} = \sum_{c \in \mathcal{C}} \omega_c \, \rho^{(c)}_{\ell m}
\tag{26}
$$

with the total correlation a weighted sum across risk categories $c$, and with $\rho^{(\text{vehicle})}\_{\ell m} \approx 1$ while $\rho^{(\text{demand})}\_{\ell m}$ is substantially below unity across the pairs. The portfolio is therefore correctly described as diversified with respect to demand-side risk and undiversified with respect to supply-side risk. The correct summary statistic is accordingly a vector, not a scalar

$$
\boldsymbol{L}^{\text{effective}} = \left( L^{\text{eff}}_{\text{vehicle}}, \; L^{\text{eff}}_{\text{demand}}, \; L^{\text{eff}}_{\text{regulatory}}, \; L^{\text{eff}}_{\text{key-person}} \right)
\tag{27}
$$

with the components differing by an order of magnitude across the categories. Reporting a single number for a portfolio of this structure discards the information that matters most.

## The Launch-Service Line

The launch-service line is the oldest revenue-bearing line and the one from which the others were generated. The line sells delivery to orbit under the commercial terms the [SpaceX Falcon 9 vehicle documentation][ref_spacex_falcon9_vehicle] and the [SpaceX Falcon Heavy vehicle documentation][ref_spacex_falcon_heavy_vehicle] describe, and the mission record is reconstructible from the [FAA current launch licenses][ref_faa_ast], the [FAA Office of Commercial Space Transportation][ref_faa_ast] records, and the [SpaceX news archive][ref_spacex_news_archive]. The milestones that established the line's cost position include the [first orbital-class booster landing of December 2015][ref_spacex_press_falcon9_first_landing_2015], the [first reflight of a recovered booster in March 2017][ref_spacex_press_ses10_2017], the [Block 5 introduction of May 2018][ref_spacex_press_block5_bangabandhu_2018], and the [first Falcon Heavy flight of February 2018][ref_spacex_press_falcon_heavy_2018].

The line's role in the portfolio is distinctive. It is the line that generates the capability the other lines consume, and it is therefore the line whose failure would be least survivable. The line is also the one whose external revenue has grown most slowly relative to the others across the recent period, because an increasing fraction of the launch capacity is consumed internally by the constellation line. The internal consumption fraction yields the compact form

$$
\iota(t) = \frac{n^{\text{internal launches}}(t)}{n^{\text{total launches}}(t)}
\tag{28}
$$

with the fraction rising substantially across the 2019 through drafting-date period as the constellation deployment accelerated. The rise means that the launch-service line has been progressively converted from an external revenue line into an internal input supplier, which is a transformation the portfolio analysis must register because an internal input supplier does not diversify anything. The diversifying contribution of the line accordingly scales with its external fraction and not with its total activity, admitting the compact form

$$
w^{\text{effective}}_{\text{launch}} = \left( 1 - \iota(t) \right) \cdot w_{\text{launch}}(t)
\tag{29}
$$

with the effective portfolio weight falling as the internal consumption rises even while the line's physical activity grows. The distinction between activity and diversifying contribution is one the published commentary on this firm routinely elides.

The value-gradient progression by which the line reached its present cost position is treated in the [Value Gradient article A282][related_post_a282_spacex_value_gradient], and the pricing evolution is treated in the [Value Capture article A284][related_post_a284_spacex_value_capture].

## The Spacecraft Line

The spacecraft line comprises the Dragon 1 cargo configuration operating across the 2010 through 2020 period and the Dragon 2 arrangement operating in crew and cargo variants from the 2019 period forward. The line is documented in the [NASA Commercial Crew Program documentation][ref_nasa_ccp_documents], the [NASA Commercial Resupply Services program overview][ref_nasa_crs_program_overview], the [CRS-2 award announcement of January 2016][ref_nasa_crs2_press_2016], and the award announcements published through the [NASA news releases][ref_nasa_news], and treated at length in the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand]. The programme-evaluation record appears in the [GAO 2019 Commercial Crew Program evaluation][ref_gao_ccp_2019], the [NASA Office of Inspector General 2019 Commercial Crew evaluation][ref_nasa_oig_ccp_2019], the [NASA Office of Inspector General 2018 Commercial Cargo evaluation][ref_nasa_oig_ccp_cargo_2018], and the [Congressional Research Service Commercial Crew report][ref_crs_commercial_crew].

The line occupies a distinctive position in the portfolio because its revenue derives substantially from a single customer under a small number of contracts. The concentration allows the brief statement through a Herfindahl index over the customer set

$$
H_\ell = \sum_{j} s_{j\ell}^2
\tag{30}
$$

with $s_{j\ell}$ the revenue share of the customer $j$ in the line $\ell$, and with the spacecraft line exhibiting an index approaching unity. A line with a customer Herfindahl near unity contributes limited diversification benefit irrespective of its revenue magnitude, because the line fails whenever the single customer's budget or programmatic priorities change.

The offsetting feature is that the single customer is a government agency operating under a multi-year appropriation with a statutory mission, which makes the customer's demand substantially less correlated with the commercial cycle than a commercial customer's would be. The spacecraft line therefore contributes specific counter-cyclical, not uncorrelated variance, which is the more valuable of the two under a survival objective. The ordering takes the compact statement that for a line added to a portfolio,

$$
\left. \frac{\partial P^{\text{ruin}}}{\partial w_\ell} \right|_{\rho_\ell < 0} < \left. \frac{\partial P^{\text{ruin}}}{\partial w_\ell} \right|_{\rho_\ell = 0} < \left. \frac{\partial P^{\text{ruin}}}{\partial w_\ell} \right|_{\rho_\ell > 0}
\tag{31}
$$

with a negatively correlated line reducing the ruin probability more than an uncorrelated line of the same mean and variance. The result is standard and is worth stating because the portfolio discussion in the trade press treats line count as the operative variable and correlation sign as a detail.

## The Constellation Line

The constellation line comprising Starlink is the dominant revenue line at the drafting date and is treated at length in the [Value Capture article A284][related_post_a284_spacex_value_capture]. The service is documented in the [Starlink service documentation][ref_spacex_starlink] and the constellation parameters in the [FCC Starlink authorization of 2018][ref_fcc_starlink_2018] and the [FCC Starlink Gen2 authorization of 2022][ref_fcc_starlink_gen2_2022]. The deployment milestones comprise the [Seattle announcement of January 2015][ref_spacex_seattle_announcement_2015], the [first operational batch of May 2019][ref_spacex_press_starlink_v0_9_2019], the [service beta of 2020][ref_spacex_press_beta_2020], and the [direct-to-cell partnership announced in 2022][ref_spacex_starlink_direct_to_cell_tmobile_2022].

The line transformed the portfolio's character. Before the line reached scale the firm held a portfolio of project-based lines whose revenue was lumpy, contract-dependent, and concentrated in a small customer set. The constellation line supplies a subscription revenue stream with different statistical properties entirely. The difference has the concise statement through the revenue autocorrelation

$$
\phi_\ell = \operatorname{corr}\!\left( r_\ell(t), \; r_\ell(t-1) \right)
\tag{32}
$$

with the project-based lines exhibiting a low autocorrelation and the subscription line exhibiting an autocorrelation near unity. A high-autocorrelation revenue stream is substantially more valuable under a survival objective than a low-autocorrelation stream of the same mean and variance, because the ruin event depends on the path and not on the distribution at a horizon.

The line nonetheless exhibited the same all-or-nothing deployment structure that the Iridium negation case illustrates, and the structure deserves statement because it is the respect in which the line most resembles the failure. A constellation returns substantially nothing until a minimum deployed count supports a continuous service footprint, admitting the compact form

$$
r^{\text{constellation}}(t) = \begin{cases} 0 & N^{\text{deployed}}(t) < N^{\text{minimum}} \\ g\!\left( N^{\text{deployed}}(t) \right) & \text{otherwise} \end{cases}
\tag{33}
$$

with a discontinuity at the threshold. The difference between this case and the Iridium case is not the shape of the function but the source of the capital sustaining the venture across the interval in which the function returns zero.

The line also introduced a new risk category that the prior portfolio did not carry. The constellation is exposed to an orbital-environment risk that the [NASA Orbital Debris Program Office][ref_nasa_orbital_debris] documents and that the literature in [Kessler and Cour-Palais 1978][research_kessler_courpalais_1978], [Weeden and Chow 2012][research_weeden_chow_2012], [Adilov 2018][research_adilov_et_al_2018], and [Walker 2020][research_walker_et_al_2020] treats, to a spectrum-regulatory risk operating under the [ITU Radio Regulations][ref_itu_radio_regulations_2020] and the [FCC filing system][ref_fcc_filings], to a debris-mitigation compliance risk under the [NASA Orbital Debris Program Office][ref_nasa_orbital_debris] standard practices and the [Inter-Agency Space Debris Coordination Committee guidelines][ref_iadc_guidelines], and to a terrestrial-competition risk from fiber and mobile networks. None of the three risks bears on any other line, which is the sense in which the line genuinely diversifies.

## The Defense-Services Line

The defense-services line comprises the Starshield business that the [SpaceX Starshield documentation][ref_spacex_starshield] describes at the unclassified level, together with the national-security launch business operating under the [Space Force National Security Space Launch][ref_space_force_nssl] framework and the certification progression the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] documents. The reported contract values reach the public record through the [Reuters 2024 investigation][research_reuters_starshield_2024] and the [New York Times 2024 coverage][ref_nyt_starshield_2024], and the comparative provider assessment appears in the [GAO 2023 National Security Space Launch evaluation][ref_gao_nssl_2023]. The certification progression is documented in the [Phase 1A award of 2018][ref_space_force_nssl_phase1a_2018], the [Phase 2 award of 2020][ref_space_force_nssl_phase2_2020], the [Phase 3 Lane 2 coverage of October 2024][ref_spacenews_nssl_phase3], with the contract announcements appearing through the [Department of Defense contract announcements][ref_dod_contracts] and the [Space Force news][ref_space_force_news].

The line's portfolio contribution is that its demand is generated by a process substantially disconnected from the commercial demand generating the other lines. A defense budget responds to a threat environment and an appropriations politics, and a commercial satellite budget responds to a capital-market condition and an end-market demand. The correlation between the two drivers is low and has historically been negative across portions of the cycle. The decomposition takes the form

$$
r_{\text{defense}}(t) = \beta_{\text{threat}} \, X^{\text{threat}}(t) + \beta_{\text{approp}} \, X^{\text{appropriation}}(t) + \varepsilon(t)
\tag{34}
$$

with neither driver appearing in the commercial lines' revenue equations. The structural independence of the driver set, not any observed sample correlation is what supports the diversification claim for this line, because a sample correlation estimated over a short period is uninformative and a structural argument is not.

The line carries an offsetting concentration. The customer set is a small number of United States government entities, and the line is therefore exposed to a single-jurisdiction political risk that no other line carries to the same degree. The line also imposes organizational-conflict-of-interest and security constraints that propagate into the other lines, so that the line's presence in the portfolio is not costless to the others. The net contribution therefore can be written as

$$
\Delta_{\text{defense}} = \underbrace{\delta^{\text{diversification}}}_{> 0} - \underbrace{c^{\text{constraint spillover}}}_{> 0}
\tag{35}
$$

with the sign of the net contribution an empirical question the available record does not settle.

## The Next-Generation Vehicle Line

The Starship and Super Heavy line is the sink in the cross-subsidization structure and the line whose presence the portfolio-patience condition is principally intended to permit. The vehicle is documented in the [SpaceX Starship vehicle documentation][ref_spacex_starship_vehicle] and with the first integrated flight test of April 2023 recorded in the [SpaceX news archive][ref_spacex_news_archive], and treated at length in the [Decomposability article A285][related_post_a285_spacex_decomposability] and the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing]. The lunar-lander milestones are documented in the [NASA HLS Option A award][ref_nasa_hls_option_a_2021] and the [NASA HLS Option B award][ref_nasa_hls_option_b_2022], and the programme evaluation in the [NASA Office of Inspector General 2021 HLS evaluation][ref_nasa_oig_hls_2021] and the [GAO 2022 HLS evaluation][ref_gao_hls_2022].

The line returns substantially nothing at the drafting date beyond the Human Landing System contract milestones that the [NASA Human Landing System program documentation][ref_nasa_hls_program] describes. The line consumes a substantial fraction of the firm's capital expenditure and a substantial fraction of its engineering attention. Under a standard capital-budgeting evaluation applied at substantially any point across the 2016 through drafting-date period, the line would have been terminated. The evaluation may be stated compactly

$$
\text{NPV}_{\text{Starship}}(t) = \sum_{s > t} \frac{E\!\left[ \text{CF}(s) \right]}{(1+\rho)^{s-t}} - K(t) < 0 \qquad \text{for } \rho = \rho^{\text{investor}}
\tag{36}
$$

with the expression negative at any discount rate a diversified investor would apply and turning positive only at a substantially lower rate or under an option valuation that treats the programme as a claim on a future capability rather than as a cash-flow stream.

The fact that it was not terminated is the observable to which the portfolio-patience claim reduces. The patience condition stated in the economic-property section requires

$$
\tau_{\text{Starship}} \geq \tau^{\ast}_{\text{Starship}}
\tag{37}
$$

and the left side is set by the controller under the governance configuration the [Governance article A287][related_post_a287_spacex_governance] treats, while the right side is set by the engineering difficulty of the programme. The observed behavior is consistent with a left side substantially exceeding any horizon an external capital provider would impose. The option reading provides the complementary valuation

$$
V^{\text{Starship}} = \sum_{a \in A} p(a) \cdot \left[ V^{\text{application}}(a) - K^{\text{residual}}(a) \right]^{+}
\tag{38}
$$

with the value accruing from the application set the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] documents rather than from any single projected cash-flow stream. The article treats the sustained funding as the central evidence for the condition in this case.

## Cross-Subsidization and the Internal Capital Market

The cross-subsidization structure is the mechanism by which the portfolio serves the mission rather than merely coexisting with it. The structure is also the least observable feature of the case, because the transfers are internal and the transfer prices are not published.

The historical sequence of the flows permits reconstruction at a qualitative level. Across the 2006 through 2012 period the state-anchored spacecraft development that the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] treats supplied the capital that sustained the launch-vehicle development. Across the 2013 through 2019 period the launch-service line supplied the capital that sustained the reusability development and the early constellation development. Across the 2020 through drafting-date period the constellation line has supplied the dominant share of the capital sustaining the next-generation vehicle development. The sequence exhibits a consistent pattern in which the line that has most recently matured funds the line that is next to mature.

The pattern admits the compact statement as an ordered relation over the lines

$$
f_{\ell \to m} > 0 \quad \text{predominantly for} \quad \text{maturity}(\ell) > \text{maturity}(m)
\tag{39}
$$

with the capital flowing consistently from the more mature to the less mature line. The maturity ordering that governs the flows permits the concise statement through a line lifecycle position

$$
\mu_\ell(t) = \frac{\text{cumulative revenue}_\ell(t)}{\text{cumulative investment}_\ell(t)}
\tag{40}
$$

with a line exhibiting $\mu_\ell < 1$ constituting a net consumer and one exhibiting $\mu_\ell > 1$ a net contributor, and with the observed flow running consistently from the higher to the lower ratio. The structure is an internal analogue of the staged financing that [Gompers 1995][research_gompers_1995] documents in the venture-capital setting, with the difference that the staging decision is made by a party who holds the entire portfolio rather than by a party who holds a fractional position in each undertaking.

The transfer-price problem deserves explicit statement because it determines what the reported figures mean. When the launch-service line delivers a constellation satellite, the price at which the transaction is recorded is an internal accounting choice. A high transfer price attributes the value to the launch line and makes the constellation line appear less profitable. A low transfer price does the reverse. The consequence is stated compactly as

$$
\pi_{\text{launch}} + \pi_{\text{constellation}} = \text{invariant} \qquad \text{while} \qquad \frac{\partial \pi_{\text{launch}}}{\partial p^{\text{transfer}}} > 0 > \frac{\partial \pi_{\text{constellation}}}{\partial p^{\text{transfer}}}
\tag{41}
$$

with the total invariant to the transfer price and the split entirely determined by it. Every published estimate of the per-line profitability of this firm rests on an assumed transfer price that the estimator has chosen, and the reader should treat the line-level figures accordingly.

The internal allocation quality is the question the internal-capital-markets literature poses. The favorable reading is the winner-picking account that [Stein 1997][research_stein_1997] develops, under which a headquarters with superior information directs capital better than an external market could. The unfavorable reading is the dark-side account that [Scharfstein and Stein 2000][research_scharfstein_stein_2000] develops, under which division managers extract rents and the allocation becomes socialistic. The SpaceX configuration exhibits a feature that bears on which reading applies, namely that the allocation is directed by a party with an overriding preference over the outcome rather than by a party balancing divisional claims. The configuration is therefore substantially immune to the socialistic failure the dark-side account describes and substantially exposed to a different failure in which the allocation reflects the controller's commitment rather than the investment opportunity. The allocation-quality correlation the Cross-Disciplinary Framings section defines would be measured against the mission rather than against the return. The substitution yields the compact statement

$$
Q^{\text{mission}} = \operatorname{corr}\!\left( \Delta k_\ell, \; \frac{\partial P(\text{reach } M)}{\partial k_\ell} \right) \qquad \text{against} \qquad Q^{\text{return}} = \operatorname{corr}\!\left( \Delta k_\ell, \; q_\ell \right)
\tag{42}
$$

with the observed allocation scoring well on the first measure by construction and indeterminately on the second. The circularity is unavoidable and the article states it rather than presenting the first measure as an independent validation.

## The Correlation Structure and Tail-Risk Mitigation

The question the article must answer is whether the portfolio in fact reduces the ruin probability. The answer requires the correlation structure rather than the line count.

The dominant common factor is the launch vehicle. A Falcon 9 loss-of-mission event triggers a grounding pending an investigation, and the grounding halts the launch-service revenue, the spacecraft missions, the constellation deployment, and the national-security launches simultaneously. The event does not halt the constellation subscription revenue from the already-deployed satellites, which is the single most important qualification in the opposite direction, because it means the constellation line contributes a revenue stream that survives the common-mode event.

The structure therefore allows a compact characterization. Let $S$ denote the event of an extended vehicle grounding. The surviving revenue fraction is

$$
\theta = \frac{r^{\text{constellation subscription}}}{r^{\text{total}}} \qquad \text{conditional on } S
\tag{43}
$$

with the fraction having risen from substantially zero before the 2020 period to a substantial value at the drafting date. The rise is the most consequential change in the firm's risk profile across its history, and it is attributable to the constellation line's subscription character rather than to the line count. Applying the effective-line-count expression from the economic-property section to the realized correlation structure gives

$$
L^{\text{effective}} \Big|_{\text{vehicle risk}} \approx 1 \qquad \text{against} \qquad L^{\text{effective}} \Big|_{\text{demand risk}} \approx 3 \text{ to } 4
\tag{44}
$$

against a nominal count of five, with the two figures bracketing the true protection the portfolio offers. The practice of reporting a single effective count for a portfolio facing heterogeneous risk categories is therefore misleading in both directions depending on which category dominates the realized event.

The runway under the adverse event has the form

$$
\Theta^{\text{stress}} = \frac{C(t)}{\dot{C}^{\text{burn}} - \theta \cdot r^{\text{total}}}
\tag{45}
$$

with the denominator the net burn under the grounding scenario and with the runway becoming unbounded when the surviving revenue exceeds the burn. The transition from a bounded to an unbounded stressed runway is the discrete event that the portfolio-patience condition is designed to produce, and it is the event that distinguishes the configuration at the drafting date from the arrangement in the 2008 period that the [series opener][related_post_a281_spacex_framing] treats.

The portfolio is not the only instrument available for managing the tail, and the article would be incomplete without stating the alternatives. The launch-insurance market that the [Lloyd's market][ref_lloyds_market] and the specialist brokers including [Aon][ref_aon_space_insurance] intermediate transfers a portion of the per-mission risk to an external party for a premium. The United States regulatory regime requires a financial-responsibility demonstration under the [FAA financial responsibility requirements][ref_faa_financial_responsibility], and the international liability framework operates under the [Liability Convention 1972][ref_un_liability_convention_1972], the [Outer Space Treaty 1967][ref_un_outer_space_treaty_1967], and the [Registration Convention 1976][ref_un_registration_convention_1976].

The instruments are complements to the portfolio rather than substitutes for it, and the reason is analytically important. Insurance transfers a per-mission loss whose magnitude is bounded by the insured value. It does not transfer the consequential loss that an extended grounding imposes on the dependent lines, and it does not transfer the loss of a development programme. The coverage gap can be stated as

$$
L^{\text{uninsured}} = L^{\text{total}} - L^{\text{insured}} = L^{\text{consequential}} + L^{\text{programme}}
\tag{46}
$$

with the two uninsured components being precisely the ones that determine whether the venture reaches the mission. The portfolio addresses the residual the insurance market does not price, which is the reason a fully insured single-line venture remains a single-bet configuration.

The second common factor is the regulatory environment, which affects the launch cadence through the [FAA Part 450 licensing][ref_faa_ast_licensing_regs_450] regime and the [FAA Starship environmental review][ref_faa_starship_ea], and affects the constellation through the spectrum process. The two regulatory channels are institutionally distinct and the correlation between them is low, which is a favorable feature.

The third common factor is the controller. Every line depends on a single individual to a degree that the [Governance article A287][related_post_a287_spacex_governance] documents, and the dependency is perfectly correlated across the lines by construction. The portfolio gives substantially no protection against a key-person event, and a key-person event is precisely the event the governance configuration makes most consequential. The interaction allows the brief statement. Let $\phi_6$ and $\phi_7$ denote the governance and portfolio-patience closures. The framework treats the joint closure as a product of independent indicators, and the key-person channel establishes that

$$
P\!\left( \text{survive} \mid \phi_6 = 1, \phi_7 = 1 \right) < P\!\left( \text{survive} \mid \phi_6 = 1 \right) \cdot P\!\left( \text{survive} \mid \phi_7 = 1 \right) \big/ P\!\left( \text{survive} \right)
\tag{47}
$$

so that the two conditions are not independent in the direction the framework's product form assumes. The two conditions therefore interact adversely in a respect the framework does not otherwise surface, and the article states the interaction rather than treating the conditions as independently satisfiable.

## The Attention-Allocation Constraint

The analysis to this point has treated capital as the scarce resource the portfolio allocates. Capital is divisible, transferable, and fungible across the lines. The resources that are not divisible deserve separate treatment, because they bind before capital does and because the portfolio-patience literature substantially ignores them.

The binding constraint that [Penrose 1959][book_penrose_1959] identifies is not capital but the managerial services available to plan and direct an expansion. The constraint is generated internally, cannot be purchased at short notice, and grows only through the experience of the existing organization. The consequence is a maximum rate of expansion independent of the capital available, which the literature terms the Penrose effect. The constraint may be written

$$
\frac{dL}{dt} \leq \gamma \cdot M(t) \qquad \text{with} \qquad \dot{M}(t) = h\!\left( M(t), \; \text{experience} \right)
\tag{48}
$$

with the rate of line addition bounded by the available managerial capacity rather than by the capital position. A venture holding substantial capital and insufficient managerial capacity cannot convert the former into the latter by spending it.

The attention constraint operates at the level of the controller with particular force in this case. The bounded-rationality tradition from [Simon 1957][book_simon_1957] Administrative Behavior through [March and Simon 1958][book_march_simon_1958] Organizations, [Cyert and March 1963][book_cyert_march_1963] A Behavioral Theory of the Firm, and [Weick 1979][book_weick_1979] The Social Psychology of Organizing treats attention as a scarce resource allocated across a problem set, and it predicts that an increase in the line count reduces the attention available to each. The allocation takes the compact form

$$
\sum_{\ell \in \mathcal{L}} a_\ell(t) \leq \bar{A} \qquad \text{with} \qquad \frac{\partial \, \text{progress}_\ell}{\partial a_\ell} > 0
\tag{49}
$$

with the total attention bounded and the progress on each line increasing in its share. The consequence is the cost the pattern-extraction section states, namely that the portfolio purchases its survival benefit at the price of a slower rate of progress on each line.

The constraint is sharper for a configuration in which the same individual holds the control the [Governance article A287][related_post_a287_spacex_governance] documents. A governance arrangement that concentrates the decision authority also concentrates the attention bottleneck, because the decisions the arrangement reserves to the controller cannot be delegated without dissolving the arrangement. The two conditions therefore interact adversely along a second channel distinct from the key-person channel the correlation section identifies. The first channel concerns what happens if the controller is lost. The second concerns what happens while the controller is present and the line count grows.

The offsetting mechanism is the organizational-learning process that [Levitt and March 1988][research_levitt_march_1988], [Huber 1991][research_huber_1991], [March 1991][research_march_1991], [Argyris and Schon 1978][book_argyris_schon_1978] Organizational Learning, [Nonaka and Takeuchi 1995][book_nonaka_takeuchi_1995] The Knowledge-Creating Company, [Nonaka 1994][research_nonaka_1994], and [Senge and Senge 1990][book_senge_1990] The Fifth Discipline develop, under which an organization converts individual attention into routines that operate without it. The conversion rate determines whether the attention constraint binds permanently or transiently. The knowledge-transfer literature comprising [Kogut and Zander 1992][research_kogut_zander_1992], [Grant 1996][research_grant_1996], [Argote and Ingram 2000][research_argote_ingram_2000], and [Argote and Miron-Spektor 2011][research_argote_miron_spektor_2011] supplies the mechanism, and the absorptive-capacity literature comprising [Cohen and Levinthal 1990][research_cohen_levinthal_1990], [Zahra and George 2002][research_zahra_george_2002], [Todorova and Durisin 2007][research_todorova_durisin_2007], [Lane et al. 2006][research_lane_koka_pathak_2006], and [Volberda et al. 2010][research_volberda_foss_lyles_2010] supplies the conditions under which a line absorbs what another line has learned.

The empirical signature that would distinguish a binding attention constraint from a non-binding one is a negative relation between the line count and the rate of progress per line. The relation is not directly observable for this case, because the per-line progress is not measured and the line count has grown monotonically alongside substantially every other quantity. The article therefore records the constraint as a theoretically grounded cost rather than as a measured one.

## The Conglomerate-Discount Objection

The finance literature's settled position is that corporate diversification destroys value. The position is supported by a substantial empirical record, and the article treats it as the principal objection to the portfolio-patience condition rather than as a complication to be noted and set aside.

The empirical finding is that diversified firms trade at a discount to the imputed value of their segments valued as standalone entities. The discount takes the form

$$
D = \frac{V^{\text{diversified}}}{\sum_{\ell} V^{\text{standalone}}_\ell} - 1 < 0
\tag{50}
$$

with [Lang and Stulz 1994][research_lang_stulz_1994] and [Berger and Ofek 1995][research_berger_ofek_1995] establishing the result and [Rajan et al. 2000][research_rajan_servaes_zingales_2000] and [Scharfstein and Stein 2000][research_scharfstein_stein_2000] supplying the mechanisms.

The literature offers three explanations. The first is that an investor can diversify at substantially zero cost by holding a portfolio of standalone firms, so that a firm which diversifies on the investor's behalf yields nothing the investor could not obtain and destroys the option to hold the segments in different proportions. The second is that the internal capital market misallocates, transferring capital from high-opportunity to low-opportunity segments through the rent-seeking the dark-side account describes. The third is that the diversification decision reflects a managerial motive of the kind [Amihud and Lev 1981][research_amihud_lev_1981] identify, in which managers reduce firm-risk to protect their own undiversified human capital at the shareholders' expense.

The article's response has three parts, and the first two are concessions.

The first concession is that the second and third explanations apply to the case with force. The internal allocation is directed by a party with an overriding preference, and a misallocation relative to the return-maximizing benchmark is not merely possible but is the declared intent of the arrangement. The managerial-motive explanation applies with unusual directness, because the controller's human capital and reputation are undiversifiably bound to the venture.

The second concession is that [Villalonga 2000][research_villalonga_2004] and the subsequent literature establish that a portion of the measured discount is a selection artifact rather than a causal effect, so that the magnitude of the true effect is smaller than the early estimates suggested. The concession cuts in the article's favor and the article notes it as a weakening of the objection rather than as a refutation.

The substantive response concerns the first explanation, which is the load-bearing one. The claim that an investor can replicate the diversification at lower cost requires that the segments be separately investable and that the investor's objective be the one the firm is diversifying against. Neither holds here.

The segments are not separately investable, because they are generated from a shared capability base rather than assembled, and a standalone constellation firm without a captive launch capability is a different entity with a different cost structure. The imputed standalone valuation the discount measure requires is therefore not defined for this case in the way it is defined for a conglomerate assembled by acquisition. The breakdown may be stated compactly

$$
V^{\text{standalone}}_\ell \neq V_\ell \Big|_{\text{within portfolio}} \qquad \text{because} \qquad c_\ell^{\text{standalone}} > c_\ell \Big|_{\text{shared base}}
\tag{51}
$$

with the standalone cost strictly higher for every line that consumes the shared capability. The measure's denominator is therefore not merely mismeasured but undefined, because the entity it prices does not exist and would have different economics if it did. The generated-versus-assembled distinction the economic-property section formalizes is precisely the distinction the discount literature's method assumes away.

The objective differs more fundamentally. The investor diversifies to reduce the variance of a return on a position the investor can exit. The venture diversifies to reduce the probability that it ceases to exist before reaching an objective the investor does not share and cannot purchase separately. The two are not the same operation performed by different parties. The distinction is stated compactly as

$$
\text{investor solves} \; \min_w \sigma^2(w) \quad \text{s.t.} \; E[R] \geq \bar{R} \qquad \text{venture solves} \; \min_w P^{\text{ruin}}(w, T^{\text{mission}})
\tag{52}
$$

with the two programmes yielding different optima. An investor holding a fractional position in a mission-directed venture and a portfolio of other assets has diversified the investor's exposure and has done nothing whatever to the venture's ruin probability. The asymmetry has the concise statement

$$
\frac{\partial \sigma^2_{\text{investor}}}{\partial \text{diversification}} < 0 \qquad \text{while} \qquad \frac{\partial P^{\text{ruin}}_{\text{venture}}}{\partial \text{investor diversification}} = 0
\tag{53}
$$

with the investor's action affecting the investor's exposure and leaving the venture's survival probability exactly unchanged. The quantity on the right is the one that determines whether the mission is reached.

The conclusion the article draws is not that the discount literature is wrong. It is that the literature measures a different thing, and that a firm whose objective is the survival to a non-tradeable goal is outside the population over which the finding was estimated. The reader who rejects the mission objective as a legitimate corporate purpose will reject the response along with it, and the article notes that the disagreement is about the objective rather than about the finance.

## The Iridium Counter-Example

The Iridium programme constitutes the canonical portfolio-patience negation case in the space sector, and it is the case the [Value Gradient article A282][related_post_a282_spacex_value_gradient] and the [Decomposability article A285][related_post_a285_spacex_decomposability] treat from different angles. The case is documented in [Finkelstein and Sanford 2000][research_finkelstein_sanford_2000] Learning from Corporate Mistakes and in the satellite-economics treatment in [Zimmerman 2011][research_zimmerman_2011]. The primary record comprises the [Iridium Chapter 11 filing of 1999][ref_iridium_chapter_11_1999] lodged with the [Securities and Exchange Commission EDGAR][ref_sec_edgar] system, the [Iridium press archive][ref_iridium_press_archive_1998], and the contemporaneous [Bloomberg coverage][ref_bloomberg]. The proceeding was conducted under the [United States Bankruptcy Code Chapter 11][ref_bankruptcy_code_ch11] provisions that the [United States Courts bankruptcy resources][ref_uscourts_bankruptcy] describe.

The configuration deployed a low-Earth-orbit constellation of approximately 66 operational satellites supporting a handheld voice-telephony service, at a total investment reported at approximately 5 billion dollars across the development period. The service commenced in the November 1998 period. The Chapter 11 filing followed in the August 1999 period, approximately nine months later, and the assets were subsequently acquired for a figure reported at approximately 25 million dollars.

The case is a portfolio-patience negation in a precise sense. The venture held a single line. The line required substantially the entire capital before it returned anything, because a constellation contributes no service until a sufficient fraction of it is deployed. The configuration therefore exhibited an all-or-nothing payoff structure in which the venture had no revenue-bearing position to fall back on when the subscriber uptake proved slower and the terrestrial-cellular substitute proved faster than the business case assumed.

The structure admits the compact statement. The venture's survival required

$$
r^{\text{subscriber}}(t) > \dot{C}^{\text{debt service}} \qquad \text{from} \qquad t = t^{\text{service commencement}}
\tag{54}
$$

with substantially no tolerance for a shortfall, because the capital structure carried a debt service that commenced on a schedule independent of the subscriber ramp. The configuration had a single line, a single customer segment, a single technology, and a fixed obligation. Each feature individually is survivable and the conjunction is not. The coverage ratio that governs the outcome can be written as

$$
\Xi(t) = \frac{r^{\text{subscriber}}(t)}{\dot{C}^{\text{debt service}}}
\tag{55}
$$

with the venture surviving while $\Xi > 1$ and entering the default process otherwise. The ratio depends on a subscriber ramp with a substantial forecast variance in the numerator and a contractually fixed quantity in the denominator, which is the structural feature that converts a forecast error into a terminal event.

The comparison to the Starlink line is instructive precisely because the two undertakings are superficially similar. Both deploy a large low-Earth-orbit constellation supporting a consumer communications service requiring a substantial deployment before returning anything. The differences are that the Starlink deployment was funded from an internal source rather than from a fixed-obligation external one, that the deploying firm held a revenue-bearing launch business throughout, that the deployment cost per satellite was reduced by the captive launch capability, and that the service addressed a market segment the terrestrial alternative does not serve rather than one it serves better. The first two differences are portfolio-patience differences and the second two are not, which the article notes so that the case is not read as establishing more than it does. The decomposition of the outcome difference can be stated as

$$
\Delta^{\text{outcome}} = \underbrace{\Delta^{\text{funding source}} + \Delta^{\text{concurrent revenue}}}_{\text{portfolio-patience}} + \underbrace{\Delta^{\text{deployment cost}} + \Delta^{\text{market segment}}}_{\text{not portfolio-patience}}
\tag{56}
$$

with the article claiming only the first bracket. A reading that attributes the entire outcome difference to the portfolio structure overstates what the comparison supports.

## The Superconducting Super Collider Counter-Example

The Superconducting Super Collider constitutes the negation case in the publicly funded research setting. The programme was authorized in the late 1980s, sited in the Waxahachie Texas location, and cancelled by the Congress in the October 1993 period after a reported expenditure of approximately 2 billion dollars and after a substantial fraction of the tunnel had been bored. The programme was administered through the [Department of Energy Office of Science][ref_doe_office_of_science], and the oversight record appears in the [Government Accountability Office reports database][ref_gao_reports], the [Congressional record][ref_congressional_record], and the [House Science Committee hearing record][ref_house_science_committee_hearings].

The case is a portfolio-patience negation in the same structural sense as the Iridium case and in a different institutional setting. The programme was a single indivisible undertaking that would return its scientific value only upon completion and that returned substantially nothing at any intermediate stage. The programme therefore faced an annual appropriation decision in which the decision maker compared a continuing cost against a benefit that remained entirely prospective, and the comparison is one a single-line configuration loses whenever the appropriator's horizon is shorter than the programme's.

The structure permits the concise form. The probability that the programme survives to completion is

$$
P\!\left( \text{completion} \right) = \prod_{y=1}^{Y} P\!\left( \text{appropriation continues in year } y \right)
\tag{57}
$$

with the product taken across the full construction period and with each annual factor below unity. The product falls rapidly in the year count for any per-year probability meaningfully below unity, which is the formal statement of why a long single-line programme dependent on a repeated external decision is structurally fragile irrespective of its merit. The value structure that produces the fragility has the form

$$
V^{\text{SSC}}(f) = \begin{cases} 0 & f < 1 \\ V^{\text{complete}} & f = 1 \end{cases}
\tag{58}
$$

with $f$ the fraction of the construction completed and with substantially no value realized at any intermediate fraction. The comparison to the Constellation Program cancellation that the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats is direct, and the two cases share the structure.

The lesson the article draws is that portfolio patience is not exclusively a private-sector instrument. A publicly funded programme that generates intermediate deliverables of independent value faces a different annual decision from one that does not, and the difference is the same decomposability-plus-portfolio structure the private case exhibits.

## Contemporary Single-Bet Failures

The contemporary record gives further instances that postdate the canonical cases and that occurred under market conditions substantially similar to the present.

The OneWeb constellation programme filed for Chapter 11 protection in the March 2020 period with a portion of its planned constellation deployed. The configuration exhibited the Iridium structure updated to the contemporary market, comprising a single constellation line requiring a substantial deployment before returning, funded from an external source, and held by a venture with no other revenue-bearing business. The proximate trigger was a funding withdrawal rather than a demand shortfall, which establishes that the single-line configuration is fragile to a capital-supply event as well as to a demand event. The programme was subsequently acquired and continued under different ownership, and the successor operations are documented through the [OneWeb corporate record][ref_oneweb] and the [Eutelsat corporate record][ref_eutelsat_oneweb].

The Virgin Orbit launch programme ceased operations and filed for Chapter 11 protection in the April 2023 period following a launch failure in the January 2023 period. The configuration held a single vehicle serving a single market segment, and the single failure was therefore sufficient to terminate the venture. The case is the clearest available contemporary demonstration that a single-vehicle configuration converts an ordinary operational event into a terminal one. The proceeding was conducted in the [United States Bankruptcy Court for the District of Delaware][ref_virgin_orbit_court].

The earlier record includes the Beal Aerospace closure of the 2000 period, the Rocketplane Kistler termination of its NASA agreement in the 2007 period recorded in the [NASA news releases][ref_nasa_news] that the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] treats, the Sea Launch bankruptcy of the 2009 period, and the Teledesic constellation suspension of the 2002 period. Each case exhibits a single-line configuration, and the pattern across them is sufficiently consistent that the base rate for the arrangement in this sector is the relevant prior against which the SpaceX outcome should be read.

The aggregate statement may be written

$$
\hat{P}\!\left( \text{survival} \mid \text{single line} \right) \ll \hat{P}\!\left( \text{survival} \mid \text{portfolio} \right)
\tag{59}
$$

with the inequality supported by the sector record and with the important caveat that the comparison is confounded, because the ventures that assembled portfolios were disproportionately the ventures that had survived long enough to assemble them. The confounding yields the compact statement. Let $A$ denote the event that a venture assembled a portfolio and $S$ the event that it survived to a horizon. The observed association satisfies

$$
P(S \mid A) > P(S) \qquad \text{with} \qquad P(A \mid S^{\text{early}}) > P(A)
\tag{60}
$$

so that the ventures observed with portfolios are disproportionately those that had already survived the early period in which most failures occur. The direction of the confounding inflates the apparent benefit, and the article states it rather than reporting the raw comparison.

## Deep Historical Comparative Precedents

The portfolio-patience mechanic supports comparison with deep historical precedents that establish the property as a recurring feature of undertakings requiring sustained investment across horizons longer than any single revenue source supports.

The chartered-company form supplies the earliest systematic instance. The Dutch and English East India Companies held portfolios of voyages, trading posts, and commodity lines whose individual outcomes were substantially independent, and the portfolio structure was the mechanism by which a single lost vessel did not terminate the enterprise. The treatments in [Steensgaard 1974][book_steensgaard_1974] The Asian Trade Revolution of the Seventeenth Century, [Stern 2011][book_stern_2011] The Company-State, and [Robins 2006][book_robins_2006] The Corporation That Changed the World document the arrangements. The voyage portfolio admits the same treatment the article applies throughout, with the ruin probability for a venture financing $n$ simultaneous voyages each carrying an independent loss probability $q$ satisfying

$$
P^{\text{ruin}} = q^{\, n} \qquad \text{against} \qquad P^{\text{ruin}} = q \quad \text{for the single-voyage partnership}
\tag{61}
$$

with the improvement geometric in the voyage count. The move from the single-voyage partnership to the permanent joint-stock company with a continuing portfolio is the institutional innovation on which the form rests, and it is the same innovation the present condition describes.

The Venetian Arsenal and the broader Venetian maritime economy supply a parallel instance in which risk was distributed across vessels and voyages through partial ownership and early insurance arrangements. The [Lane 1934][book_lane_1934] Venetian Ships and Shipbuilders of the Renaissance and [Concina 2006][book_concina_2006] treatments document the structures. The arrangement diversified across ventures rather than within a firm, which makes it the historical antecedent of the venture-capital form rather than of the configuration this article treats.

The Manhattan Project supplies the purest historical instance of a portfolio held under irreducible technical uncertainty. The programme pursued gaseous diffusion, electromagnetic separation, and plutonium production simultaneously, at a cost far exceeding that of selecting one, precisely because no party could determine in advance which route would succeed. The treatments in [Rhodes 1986][book_rhodes_1986] The Making of the Atomic Bomb, [Groves 1962][book_groves_1962] Now It Can Be Told, [Hewlett and Anderson 1962][book_hewlett_anderson_1962] The New World, and [Bird and Sherwin 2005][book_bird_sherwin_2005] American Prometheus document the decision. The structure allows the brief statement that for independent routes each with success probability $p_r$,

$$
P(\text{at least one succeeds}) = 1 - \prod_{r} \left( 1 - p_r \right)
\tag{62}
$$

with the parallel pursuit purchasing a higher joint success probability at a cost equal to the sum of the route costs. The case is the cleanest available demonstration that a portfolio is rational under uncertainty about which approach works even when it is manifestly wasteful under any single realized history, and it is the structure the engineering-development portion of the SpaceX portfolio most resembles.

The Standard Oil trajectory provides the instance of a portfolio assembled across the stages of a single value chain rather than across unrelated markets, documented in [Chernow 2004][book_chernow_2004] Titan. The configuration held refining, transport, distribution, and by-product lines whose common exposure was the crude price and whose idiosyncratic exposures differed. The antitrust response documented in [Bork 1978][book_bork_1978], [Posner 2001][book_posner_2001], and [Hovenkamp 2005][book_hovenkamp_2005] establishes the hazard that a successful vertically generated portfolio attracts, which is a consideration the SpaceX configuration will encounter as the constellation position consolidates.

The Lockheed Skunk Works trajectory documented in [Rich and Janos 1994][book_rich_janos_1994] Skunk Works and [Miller 1995][book_miller_1995] Lockheed Skunk Works supplies the instance in which the portfolio was held at the level of the parent firm while the development organization pursued a single project at a time. The arrangement separates the portfolio function from the development function, and it is the organizational alternative to holding both in a single unit. The comparison is instructive because it establishes that the portfolio need not be held at the same level as the mission, provided the level holding it is willing to fund the level pursuing it.

The Concorde and United States supersonic transport programmes supply the single-bet negation in the commercial-aviation setting, documented in [Owen 1997][book_owen_1997] Concorde, [Owen 2001][book_owen_2001] Concorde and the Americans, [Trubshaw 2000][book_trubshaw_2000] Concorde The Inside Story, and [Horwitch 1982][book_horwitch_1982] Clipped Wings. The configurations committed to a single vehicle addressing a single route structure, and neither held an adjacent line whose revenue could have sustained the programme through the period in which the economics deteriorated.

The Bell System supplies the instance in which a portfolio of regulated revenue lines sustained a research programme with a horizon no single line would have supported. The treatments in [Gertner 2012][book_gertner_2012] The Idea Factory, [Temin and Galambos 1987][book_temin_galambos_1987] The Fall of the Bell System, [Wu 2010][book_wu_2010] The Master Switch, and [Levin 2010][book_levin_2010] The Wires That Bind document the arrangement. The case is the closest twentieth-century analogue to the cross-subsidization structure this article describes, with the difference that the subsidy flowed from a regulated monopoly rent rather than from a competitively earned surplus, and with the consequence that the arrangement terminated when the regulatory settlement changed rather than when the research programme concluded.

The IBM System/360 programme offers the instance of a firm sustaining a development whose cost approached its annual revenue, funded from a portfolio of existing product lines that the new architecture was intended to replace. The [Pugh et al. 1991][book_pugh_johnson_palmer_1991] and [Pugh 1995][book_pugh_1995] treatments document the programme and the [IBM archives][ref_ibm_archives] hold the institutional record. The structure in which the incumbent lines fund their own replacement is precisely the structure the Falcon-funds-Starship relationship exhibits, and the IBM case is the best-documented historical instance of a firm executing it successfully.

The Boeing progression from the military contracts through the commercial airliner business that the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats gives the instance in which a military line and a commercial line were held simultaneously with imperfectly correlated demand. The [Serling 1992][book_serling_1992] Legend and Legacy, [Newhouse 1982][book_newhouse_1982] The Sporty Game, and [Newhouse 2007][book_newhouse_2007] Boeing versus Airbus treatments document the arrangement across the full period, and [Lawrence 2016][book_lawrence_2016] Airbus versus Boeing supplies the comparative treatment. The pattern in which a defense line stabilizes a commercial cycle and a commercial line stabilizes a defense cycle is the same pattern the SpaceX defense-services line exhibits.

The Ford and Toyota manufacturing trajectories supply the instance in which a single product line sustained across a long horizon was subsequently displaced by a configuration holding multiple lines with shared production capability. The [Ford et al. 1922][book_ford_crowther_1922], [Nevins 1954][book_nevins_1954], [Ohno 1988][book_ohno_1988], [Shingō 1989][book_shingo_1989], [Womack et al. 1990][book_womack_jones_roos_1990], [Womack and Jones 2003][book_womack_jones_2003], and [Liker 2004][book_liker_2004] treatments document the progression. The relevant feature is that the shared production capability is what made the multiple lines affordable, which is the generated-portfolio structure in a manufacturing setting.

The conglomerate wave of the mid-twentieth century yields the negative precedent that the discount literature was written to explain. The configurations assembled unrelated lines by acquisition on the explicit rationale of risk reduction, and the subsequent record was sufficiently poor that the form was substantially abandoned. The treatments in [Chandler 1962][book_chandler_1962], [Chandler 1977][book_chandler_1977], [Chandler 1990][book_chandler_1990], [Fligstein 2001][book_fligstein_2001] The Architecture of Markets, and [Montgomery 1994][research_montgomery_1994] document the episode. The precedent set permits summary through the pair of indicators the article's central distinction defines

$$
\chi = \left( \mathbb{1}\!\left[ L > 1 \right], \; \mathbb{1}\!\left[ \textstyle\bigcap_\ell K_\ell \neq \varnothing \right] \right)
\tag{63}
$$

with the chartered companies, the Bell System, the IBM programme, and the Boeing progression occupying the $(1,1)$ cell, the mid-century conglomerates occupying the $(1,0)$ cell, and the single-bet negation cases occupying the $(0, \cdot)$ cell. The historical record contains substantially more $(1,0)$ cases than $(1,1)$ cases, and the $(1,0)$ record is poor. The case is the reason the article's central distinction between a generated and an assembled portfolio must do real work rather than serve as a rhetorical convenience, because the conglomerate wave is exactly what the portfolio-patience condition would license if the distinction were dropped.

## Historiographical Gap and Recent Scholarship

The scholarly literature bearing on the portfolio-patience condition is unusual within this series in that it is abundant rather than thin, and the difficulty is that substantially all of it was written to answer a different question. The corporate-diversification literature is mature, well identified, and largely settled, and it evaluates an objective the case does not hold.

### Primary Source Documentation

The primary-source documentation comprises the [SpaceX news archive][ref_spacex_news_archive], the vehicle documentation at [Falcon 9][ref_spacex_falcon9_vehicle], [Falcon Heavy][ref_spacex_falcon_heavy_vehicle], and [Starship][ref_spacex_starship_vehicle], the [Starlink service documentation][ref_spacex_starlink], the [SpaceX Starshield documentation][ref_spacex_starshield], the [SpaceX corporate site][ref_spacex_company], the [FAA current launch licenses][ref_faa_ast] and [FAA Part 450 licensing regulations][ref_faa_ast_licensing_regs_450], the [FAA Starship environmental review][ref_faa_starship_ea], the [FCC Starlink authorization of 2018][ref_fcc_starlink_2018], the [FCC Starlink Gen2 authorization of 2022][ref_fcc_starlink_gen2_2022], the [FCC direct-to-cell authorization of 2024][ref_fcc_direct_to_cell_2024], the [FCC filing system][ref_fcc_filings], the [NASA Commercial Crew Program documentation][ref_nasa_ccp_documents], the [NASA Human Landing System program documentation][ref_nasa_hls_program], the [Space Force National Security Space Launch][ref_space_force_nssl] framework, the [GAO 2023 National Security Space Launch evaluation][ref_gao_nssl_2023], the [ITU Radio Regulations][ref_itu_radio_regulations_2020], the [Securities and Exchange Commission EDGAR][ref_sec_edgar] system and the [Form D exempt-offering notices][ref_sec_form_d], the [Regulation S-K][ref_sec_regulation_sk] disclosure requirements, the [United States Bankruptcy Code Chapter 11][ref_bankruptcy_code_ch11] provisions, and the [FAA financial responsibility requirements][ref_faa_financial_responsibility].

### Portfolio and Diversification Literature

The literature is surveyed above in the Cross-Disciplinary Framings and Conglomerate-Discount sections. The principal works are [Markowitz 1952][research_markowitz_1952], [Markowitz 1959][book_markowitz_1959], [Sharpe 1964][research_sharpe_1964], [Lintner 1965][research_lintner_1965], [Lewellen 1971][research_lewellen_1971], [Amihud and Lev 1981][research_amihud_lev_1981], [Lang and Stulz 1994][research_lang_stulz_1994], [Montgomery 1994][research_montgomery_1994], [Berger and Ofek 1995][research_berger_ofek_1995], [Rajan et al. 2000][research_rajan_servaes_zingales_2000], and [Villalonga 2000][research_villalonga_2004]. The gap with respect to the present case is that the literature's dependent variable is a market valuation, which requires a listed firm, and the case is unlisted. The literature's method is therefore inapplicable to the case in a mechanical sense before any question about its conceptual applicability arises.

### Internal Capital Markets Literature

The literature comprises [Gertner et al. 1994][research_gertner_scharfstein_stein_1994], [Stein 1997][research_stein_1997], and [Scharfstein and Stein 2000][research_scharfstein_stein_2000]. The literature is the most directly applicable body of work to the cross-subsidization structure, and its central finding that internal allocation is subject to political distortion is one the article accepts. The unexplored question the literature leaves is what happens when the allocator holds an objective other than the return, which is precisely the configuration here and is substantially absent from the published treatments.

### Real-Options and Sequential-Investment Literature

The literature comprising [Myers 1977][research_myers_1977], [Black and Scholes 1973][research_black_scholes_1973], [Merton 1973][research_merton_1973], [McDonald and Siegel 1986][research_mcdonald_siegel_1986], [Kogut and Kulatilaka 1994][research_kogut_kulatilaka_1994], [Dixit and Pindyck 1994][book_dixit_pindyck_1994], [Trigeorgis 1996][book_trigeorgis_1996], and [Copeland and Antikarov 2001][book_copeland_antikarov_2001] supplies the apparatus for valuing the portfolio as a collection of separately exercisable options. The entrepreneurial-finance treatments in [Sahlman 1990][research_sahlman_1990], [Gompers 1995][research_gompers_1995], [Kaplan and Stromberg 2003][research_kaplan_stromberg_2003], [Kaplan and StrÖMberg 2004][research_kaplan_stromberg_2004], [Lerner 1994][research_lerner_1994_syndication], [Gompers and Lerner 2001][book_gompers_lerner_2001], [Metrick and Yasuda 2011][book_metrick_yasuda_2011], and [Lerner 2009][book_lerner_2009] supply the external analogue in which the portfolio is held across firms by a fund rather than within a firm by a venture.

### Space-Sector Economics and Failure Literature

The sector literature comprising [Hertzfeld 2002][research_hertzfeld_2002], [Peeters 2018][research_peeters_2018], [Weinzierl 2018][research_weinzierl_2018], [Anderson 2023][book_anderson_2023] The Space Economy, and [Zimmerman 2011][research_zimmerman_2011] supplies the sector framing. The failure record is documented in [Finkelstein and Sanford 2000][research_finkelstein_sanford_2000] for the Iridium case and in [Klerkx 2004][book_klerkx_2004] Lost in Space and [Handberg 1994][book_handberg_1994] Reinventing NASA for the institutional context. The trade-press record identified below carries substantially the entire contemporary failure record, because the ventures concerned were private and their filings are sparse.

The peer-reviewed sector literature appears in [Space Policy][ref_space_policy_journal], the [AIAA Journal of Spacecraft and Rockets][ref_aiaa_jsr], the [Journal of Space Safety Engineering][ref_jsse_journal], and the [Journal of Space Law][ref_journal_space_law], with the policy-analysis coverage in [Space Policy Online][ref_space_policy_online]. The sector market-sizing and investment-flow data on which the line-magnitude estimates depend are published by analyst firms including [BryceTech][ref_bryce_tech] and [Space Capital][ref_space_capital], and the figures are secondary reconstructions rather than reported accounts. The business case-study treatments appear in the [Anadol et al. 2018][research_anadol_cohen_2018] Harvard Business School treatment, the [Stanford Graduate School of Business case collection][ref_stanford_spacex_case], and the [Wharton knowledge repository][ref_wharton_spacex_case].

### Comparative and Adjacent Literature

The comparative literature on mission-directed and public-purpose organizations comprising [Mazzucato 2013][book_mazzucato_2013], [Mazzucato 2021][book_mazzucato_2021], [Ruttan 2006][book_ruttan_2006], [Weiss 2014][book_weiss_2014], [Hartley 2017][book_hartley_2017], and [Bonvillian 2018][research_bonvillian_2018] treats the institutional arrangements under which long-horizon programmes are sustained without a commercial portfolio. The innovation-systems literature comprising [Freeman 1987][book_freeman_1987], [Lundvall 1992][book_lundvall_1992], [Nelson 1993][book_nelson_1993], [Mowery and Rosenberg 1998][book_mowery_rosenberg_1998], [Perez 2002][book_perez_2002], and [Schumpeter 1942][book_schumpeter_1942] supplies the macro framing.

### Corporate-Governance and Agency Literature

The agency literature bears on the configuration through the free-cash-flow channel rather than through the control channel the [Governance article A287][related_post_a287_spacex_governance] treats. The principal works are [Berle and Means 1932][book_berle_means_1932], [Jensen and Meckling 1976][research_jensen_meckling_1976], [Fama and Jensen 1983][research_fama_jensen_1983], [Jensen 1986][research_jensen_1986], [Shleifer and Vishny 1997][research_shleifer_vishny_1997], [Grossman and Hart 1987][research_grossman_hart_1988], [Harris and Raviv 1988][research_harris_raviv_1988], [Hart 1995][book_hart_1995], [Tirole 2006][book_tirole_2006], [Easterbrook and Fischel 1991][book_easterbrook_fischel_1991], [Roe 1994][book_roe_1994], and [La Porta et al. 1998][research_laporta_et_al_1998]. The empirical dual-class record in [DeAngelo and DeAngelo 1985][research_deangelo_deangelo_1985], [Gompers et al. 2003][research_gompers_ishii_metrick_2003], [Gompers et al. 2009][research_gompers_ishii_metrick_2010], [Bebchuk et al. 1999][research_bebchuk_kraakman_triantis_2000], and [Bebchuk and Kastiel 2017][research_bebchuk_kastiel_2017] establishes the conditions under which the discipline the framing relies on is absent. The gap the literature exhibits is that it evaluates the allocation against a return benchmark and contributes no treatment of an allocator holding a different objective.

### Learning and Capability-Accumulation Literature

The literature comprising [Wright 1936][research_wright_1936], [Alchian 1963][research_alchian_1963], [Rapping 1965][research_rapping_1965], [Argote and Epple 1990][research_argote_epple_1990], [Argote 1999][book_argote_1999], [Adler and Clark 1991][research_adler_clark_1991], [Lieberman 1984][research_lieberman_1984], and [Dutton and Thomas 1984][research_dutton_thomas_1984] supplies the mechanism by which the shared base accumulates experience from every line jointly. The knowledge and absorptive-capacity strand comprising [Cohen and Levinthal 1990][research_cohen_levinthal_1990], [Kogut and Zander 1992][research_kogut_zander_1992], [Grant 1996][research_grant_1996], [Argote and Ingram 2000][research_argote_ingram_2000], [Zahra and George 2002][research_zahra_george_2002], [Todorova and Durisin 2007][research_todorova_durisin_2007], [Lane et al. 2006][research_lane_koka_pathak_2006], [Volberda et al. 2010][research_volberda_foss_lyles_2010], and [Argote and Miron-Spektor 2011][research_argote_miron_spektor_2011] supplies the conditions under which the transfer occurs. The modularity strand comprising [Simon 1962][research_simon_1962], [Ulrich 1995][research_ulrich_1995], [Sanchez and Mahoney 1996][research_sanchez_mahoney_1996], [Baldwin and Woodard 2009][research_baldwin_woodard_2009], [Fixson 2004][research_fixson_2005], [Novak and Eppinger 2001][research_novak_eppinger_2001], [Sosa et al. 2003][research_sosa_eppinger_rowles_2003], [Ethiraj and Levinthal 2004][research_ethiraj_levinthal_2004], [Rivkin and Siggelkow 2003][research_rivkin_siggelkow_2003], and [MacCormack et al. 2012][research_maccormack_baldwin_rusnak_2012] supplies the interface conditions under which a shared base serves rather than couples the lines.

### Critical and Skeptical Literature

A critical literature reads the configuration as a concentration of infrastructural control rather than as a prudent risk management. The position appears in [Srnicek 2017][book_srnicek_2017] Platform Capitalism, [Zuboff 2019][book_zuboff_2019] The Age of Surveillance Capitalism, [Foster and McChesney 2011][book_foster_mcchesney_2011] The Endless Crisis, [Melman 1970][book_melman_1970] Pentagon Capitalism, and [Wu 2010][book_wu_2010] The Master Switch, with the antitrust apparatus in [Bork 1978][book_bork_1978], [Posner 2001][book_posner_2001], [Hovenkamp 2005][book_hovenkamp_2005], and [Khan 2017][research_khan_2017] Amazon's Antitrust Paradox, and the regulated-industry treatments in [Kahn 1988][book_kahn_1988] The Economics of Regulation and [Sharkey 1982][book_sharkey_1982] The Theory of Natural Monopoly. The concern the literature raises is that a generated portfolio spanning launch, connectivity, and defense services concentrates a set of capabilities whose separation a society might have reason to prefer, and that the efficiency argument the article develops is silent on that question. The article regards the concern as well founded and does not resolve it.

### Methodological Literature

The case-study methodology literature comprising [Yin 2014][book_yin_2014] and [Creswell and Creswell 2014][book_creswell_2014] supplies the inferential standards. The selection problem is unusually acute for this condition, because the portfolio is observable only for ventures that survived long enough to build one. The evolutionary and failure treatments in [Nelson and Winter 1982][book_nelson_winter_1982], [Metcalfe 1998][book_metcalfe_1998], [Ormerod 2005][book_ormerod_2005], [Kauffman 1993][book_kauffman_1993], and [Beinhocker 2006][book_beinhocker_2006] supply the base-rate framing. The working-paper record in which the corporate-finance frontier circulates ahead of journal publication is accessible through the [National Bureau of Economic Research][ref_nber], the [Social Science Research Network][ref_ssrn], and the [European Corporate Governance Institute][ref_ecgi], with the doctrinal commentary in the [Harvard Law School Forum on Corporate Governance][ref_harvard_corpgov_forum] and the [Columbia Law School Blue Sky Blog][ref_columbia_blue_sky].

### Trade Press and Journalistic Record

The per-line revenue and contract-value figures on which substantially every quantitative claim in this article rests reach the public through [SpaceNews][ref_spacenews], [Ars Technica space coverage][ref_arstechnica_space], [NASASpaceflight][ref_nasaspaceflight], [Payload][ref_payload], [Payload Research][ref_payload_research], [European Spaceflight][ref_european_spaceflight], and [The Space Review][ref_the_space_review], with defense-adjacent coverage in [Breaking Defense][ref_breaking_defense], [Aviation Week][ref_aviation_week], and [Defense News][ref_defense_news], and business coverage in [Bloomberg][ref_bloomberg], the [New York Times][ref_nyt], the [Wall Street Journal][ref_wsj], and the [Washington Post][ref_washington_post].

## Contemporary Comparative Landscape

The contemporary landscape exhibits a range of portfolio configurations across the sector.

Blue Origin holds a portfolio comprising a suborbital tourism line, an orbital launch line, an engine-supply line selling the BE-4 to an external customer, and a lunar-lander line. The configuration is a generated portfolio in the sense this article defines, and the engine-supply line is a genuinely uncorrelated revenue source. The distinguishing feature is that the portfolio is not required to fund the mission, because the single-funder configuration the [Governance article A287][related_post_a287_spacex_governance] treats supplies the capital directly. The consequence is that the portfolio serves a capability-development purpose rather than a survival purpose. The record is available through the [Blue Origin press releases][ref_blue_origin_press].

Rocket Lab holds a portfolio comprising a small-launch line, a spacecraft-manufacturing line, and a components line, and the components line provides external customers including competitors. The configuration is the closest sector analogue to the structure this article describes, and it was assembled substantially by acquisition rather than generated, which places it on the opposite side of the article's central distinction. The record is available through the [Rocket Lab press releases][ref_rocket_lab_press].

The United Launch Alliance holds a single line serving a concentrated customer set, and its survival is assured by its parent structure rather than by its portfolio. The parent firms hold broad portfolios of their own, documented through the [Boeing press releases][ref_boeing_press] and the [Northrop Grumman press releases][ref_northrop_grumman_press], which is the reason a joint venture of diversified parents faces a different survival question from a standalone venture. The record is available through the [United Launch Alliance news][ref_ula_press].

The European, Japanese, Indian, and Chinese configurations documented through the [Arianespace][ref_arianespace], [JAXA][ref_jaxa_press], [ISRO][ref_isro_press], and [China National Space Administration][ref_chinese_space_program] records and the [China sector reporting][ref_china_commercial_space] exhibit state-programme structures in which the survival question is answered by the appropriation rather than by the portfolio. The configurations are therefore not comparable on the dimension this article measures. The comparison that is available concerns the patience component alone, and the ordering across the organizational forms is

$$
\tau^{\text{state programme}} > \tau^{\text{founder-controlled private}} > \tau^{\text{venture-backed private}} > \tau^{\text{listed}}
\tag{64}
$$

with the state programmes scoring well on the patience component and poorly on the portfolio component, and the listed commercial firms scoring in the reverse.

The incumbent aerospace primes supply the opposite configuration, in which a very broad portfolio assembled across decades coexists with substantially no mission of the kind this series treats. The portfolios are documented through the [Boeing press releases][ref_boeing_press], the [Boeing historical archives][ref_boeing_historical_archives], and the [Northrop Grumman press releases][ref_northrop_grumman_press], and the defense-industrial context appears in [Hunter 2016][book_hunter_2016] Creating Strategic Value and [Hartley 2017][book_hartley_2017] The Economics of Arms. The configurations satisfy the multiplicity and imperfect-correlation sub-properties comfortably and satisfy the patience and mission-directed-allocation sub-properties not at all, which places them at the opposite corner of the space from the single-bet negation cases and equally far from the closure.

The pattern the landscape exhibits is that a portfolio and a patient capital source are substitutes rather than complements for the survival purpose. A venture with an assured capital source does not require a portfolio to survive, and a venture with a portfolio does not require an assured capital source. The substitution may be stated compactly

$$
P^{\text{ruin}} = f\!\left( \min\left\{ L^{\text{effective}}, \; \Theta^{\text{assured capital}} \right\} \right)
\tag{65}
$$

with the ruin probability governed by whichever specific protection is stronger rather than by their sum. The SpaceX configuration holds both, which is the reason it is treated in the series as a closed conjunction rather than as a minimal example.

## Comparative Cross-Sectional Analysis

The portfolio-patience condition allows application to the organization set as a cross-sectional scoring exercise across the five sub-properties the pattern-extraction section states. The closure vector takes the compact form

$$
\boldsymbol{\phi}_j^{\text{portfolio-patience}} \in \{0,1\}^{5}
\tag{66}
$$

with each organization's vector indicating the satisfaction status across the multiplicity, generation, imperfect-correlation, patience, and mission-directed-allocation sub-properties.

SpaceX exhibits closure on all five, with the important qualification that the imperfect-correlation sub-property closes only with respect to demand-side risk and fails with respect to the shared-vehicle and key-person common factors. The qualification is material enough that the article records the closure as partial rather than complete on that sub-property.

Blue Origin exhibits closure on the multiplicity, generation, and patience sub-properties, and the mission-directed-allocation sub-property closes trivially because the allocator is the funder. Rocket Lab exhibits closure on the multiplicity and imperfect-correlation sub-properties and non-closure on the generation sub-property. The United Launch Alliance exhibits non-closure on substantially all five. The state programmes exhibit closure on the patience sub-property alone. The single-bet negation cases exhibit non-closure on the multiplicity sub-property by construction, which is what makes them the negation cases.

The cross-sectional pattern indicates that the multiplicity sub-property is the easiest to satisfy and the generation sub-property the hardest, and that the two are substantially uncorrelated across the set. The correlation is stated compactly as

$$
\operatorname{corr}_j\!\left( \phi_{j,1}^{\text{multiplicity}}, \; \phi_{j,2}^{\text{generation}} \right) \approx 0
\tag{67}
$$

with the presence of multiple lines carrying substantially no information about whether they were generated from a shared base or assembled. The finding matters because the conglomerate literature establishes that the assembled configuration destroys value, so that a venture satisfying the multiplicity sub-property alone has adopted the arrangement the evidence disfavors.

## Data Sources and Reconstruction Methodology

The article draws on primary and secondary sources to reconstruct the portfolio trajectory, and the evidentiary position is comparable to that of the [Governance article A287][related_post_a287_spacex_governance] rather than to that of the technical articles earlier in the series.

The primary-source layer comprises the regulatory, contractual, and corporate materials identified in the Historiographical Gap section. The regulatory materials are complete and authoritative for the matters they cover, which comprise the constellation parameters, the launch licensing, and the spectrum assignments. They cover substantially nothing about the finances.

The secondary-source layer comprises the trade-press and analyst reconstructions identified above.

The reconstruction methodology for the portfolio claims proceeds by triangulating the launch manifest, which is well documented through the [FAA current launch licenses][ref_faa_ast] and the [FAA Office of Commercial Space Transportation][ref_faa_ast] records, against the reported contract values appearing in the [Department of Defense contract announcements][ref_dod_contracts] and the NASA award announcements, and against the reported subscriber counts and the sector estimates that [BryceTech][ref_bryce_tech] and [Space Capital][ref_space_capital] publish. The method produces a defensible ordering of the line magnitudes and a poorly determined estimate of their absolute values.

The empirical-record limitations are severe and comprise the following. The firm publishes no segment reporting. The internal transfer prices are unknown and are the single most consequential unobserved quantity, because the per-line profitability is entirely determined by them. The capital expenditure allocation across the lines is unknown. The Starshield revenue and mission composition are classified. The consequence is that the article's qualitative claims about the portfolio structure are substantially better supported than its quantitative claims about the magnitudes, and the reader should weight them accordingly.

## Alternative Analytical Frameworks

The portfolio-patience framing the article develops is one of several analytical frameworks the surrounding literature applies to the configuration.

The corporate-diversification framing developed in [Lang and Stulz 1994][research_lang_stulz_1994], [Berger and Ofek 1995][research_berger_ofek_1995], and [Villalonga 2000][research_villalonga_2004] is the principal alternative and treats the configuration as a value-destroying diversification. The framing is treated at length in its own section rather than dismissed here.

The vertical-integration framing developed in [Coase 1937][research_coase_1937], [Williamson 1975][research_williamson_1975], [Williamson 1985][book_williamson_1985], [Klein et al. 1978][research_klein_crawford_alchian_1978], [Monteverde and Teece 1982][research_monteverde_teece_1982], [Grossman and Hart 1986][research_grossman_hart_1986], [Hart and Moore 1990][research_hart_moore_1990], and [Lafontaine and Slade 2007][research_lafontaine_slade_2007] treats the configuration not as a portfolio at all but as a vertically integrated production chain in which the launch line is an input supplier to the constellation line. The framing is a serious competitor to the portfolio reading, because the launch-to-constellation relationship is genuinely vertical. The double-marginalization gain takes the form

$$
\Delta^{\text{integration}} = \left( p^{\text{market}}_{\text{launch}} - c^{\text{marginal}}_{\text{launch}} \right) \cdot q^{\text{internal}}
\tag{68}
$$

with the gain equal to the eliminated upstream margin applied across the internally consumed quantity, and with the magnitude for this case substantial because the internal quantity is large. The framing predicts that the arrangement's value derives from the elimination of a double-marginalization and a holdup hazard rather than from any risk reduction. The two readings are not mutually exclusive and the article's claim is that the portfolio reading adds something the vertical reading omits, namely the survival of the subscription revenue under the vehicle-grounding scenario.

The resource-based and dynamic-capabilities framing developed in [Penrose 1959][book_penrose_1959], [Wernerfelt 1984][research_wernerfelt_1984], [Barney 1991][research_barney_1991], [Peteraf 1993][research_peteraf_1993], [Teece et al. 1997][research_teece_pisano_shuen_1997], [Eisenhardt and Martin 2000][research_eisenhardt_martin_2000], [Helfat and Peteraf 2003][research_helfat_peteraf_2003], [Winter 2003][research_winter_2003], and [Teece 2007][research_teece_2007] treats the lines as redeployments of an underused resource base. The resource-quality criterion the tradition yields can be written as

$$
\Pi_\ell = V_\ell \cdot R_\ell \cdot I_\ell \cdot N_\ell
\tag{69}
$$

with the four factors indexing value, rarity, inimitability, and non-substitutability, and with a shared resource scoring on the criterion contributing to every line simultaneously. The [Penrose 1959][book_penrose_1959] mechanism is the closest available account of how the lines came to exist, and the framing contributes the best explanation of the generation process while supplying substantially nothing about the risk structure.

The platform framing developed in [Meyer and Lehnerd 1997][book_meyer_lehnerd_1997], [Baldwin and Clark 2000][book_baldwin_clark_2000], [Gawer and Cusumano 2002][book_cusumano_gawer_2002], [Iansiti and Levien 2004][book_iansiti_levien_2004], [Adner 2012][book_adner_2012], [Adner 2021][book_adner_2021], [Gawer and Cusumano 2013][research_gawer_cusumano_2014], and [Jacobides et al. 2018][research_jacobides_et_al_2018] treats the shared capability base as a platform and the lines as applications built on it. The platform account and the generated-portfolio account are related by the compact correspondence

$$
\text{platform} \longleftrightarrow \bigcap_\ell K_\ell \qquad \text{applications} \longleftrightarrow \mathcal{L}
\tag{70}
$$

with the shared capability intersection playing the role the platform literature assigns to the platform and the line set playing the role it assigns to the applications. The framing is substantially equivalent to the generated-portfolio account in different vocabulary.

The real-options framing developed in [Dixit and Pindyck 1994][book_dixit_pindyck_1994] and [Trigeorgis 1996][book_trigeorgis_1996] treats the lines as separately exercisable options and offers the formal statement that a portfolio of options exceeds an option on a portfolio. The framing connects the condition to the decomposability condition and gives the most rigorous available account of why the line structure matters independently of the risk correlation.

The behavioral framing developed in [Kahneman and Tversky 1979][research_kahneman_tversky_1979], [Tversky and Kahneman 1992][research_tversky_kahneman_1992], [Kahneman 2011][book_kahneman_2011], [Staw 1976][research_staw_1976], and [Ross and Staw 1993][research_ross_staw_1993] supplies the skeptical reading under which the patience the condition praises is an escalation of commitment that the absence of an external check permits. The framing generates a testable prediction that the continuation decision is insensitive to the arriving evidence

$$
\frac{\partial P\!\left( \text{continue} \right)}{\partial \, \text{signal}} \approx 0 \qquad \text{under escalation} \qquad \text{against} \qquad < 0 \quad \text{under rational updating}
\tag{71}
$$

with the two readings distinguishable in principle by observing whether the resource commitment responds to the programme's setbacks. The prediction is not distinguishable from the favorable reading using the evidence available while the programme remains incomplete, because the observed setbacks have been followed by the continued commitment under both readings.

The evolutionary and selection framing developed in [Nelson and Winter 1982][book_nelson_winter_1982], [Metcalfe 1998][book_metcalfe_1998], [Klepper 1996][research_klepper_1996], and [Klepper 2010][research_klepper_2010] supplies the caution that the observed configuration is a survivor and that the portfolio may be a consequence of survival rather than a cause of it. The caution is stronger for this condition than for any other in the framework, because the causal direction is genuinely ambiguous. The identification failure has the concise statement

$$
\text{Cov}\!\left( \text{portfolio}, \; \text{survival} \right) = \underbrace{\beta_1}_{\text{portfolio causes survival}} + \underbrace{\beta_2}_{\text{survival permits portfolio}}
\tag{72}
$$

with the observed covariance equal to the sum and with no available instrument separating the two terms. A venture survives long enough to build a portfolio, and a portfolio helps a venture survive, and the observational record cannot separate them.

The agency and free-cash-flow framing developed in [Jensen 1986][research_jensen_1986], [Jensen and Meckling 1976][research_jensen_meckling_1976], [Fama and Jensen 1983][research_fama_jensen_1983], and [Shleifer and Vishny 1997][research_shleifer_vishny_1997] treats the cross-subsidization not as a portfolio mechanism but as the canonical misuse of a free cash flow that ought to be returned to the claimants. The framing is the most direct challenge to the article's reading of the Starlink-funds-Starship relationship, and the two readings are observationally identical. The framing is not answered by the evidence and is answered only by the prior one holds about whether the receiving line is worth funding.

The modularity and architecture framing developed in [Simon 1962][research_simon_1962], [Ulrich 1995][research_ulrich_1995], [Sanchez and Mahoney 1996][research_sanchez_mahoney_1996], and [Baldwin and Woodard 2009][research_baldwin_woodard_2009] treats the question as one of interface design rather than of risk. The framing predicts that the shared base delivers its benefit only where the interfaces between the base and the lines are stable, and that an unstable interface converts the shared base from a source of leverage into a source of correlated failure. The framing yields a concrete design criterion the risk framing does not.

The learning and absorptive-capacity framing developed in [Wright 1936][research_wright_1936], [Argote and Epple 1990][research_argote_epple_1990], [Cohen and Levinthal 1990][research_cohen_levinthal_1990], and [Argote and Ingram 2000][research_argote_ingram_2000] treats the portfolio's value as arising from the joint experience accumulation on the shared element rather than from any risk reduction. The framing provides a value source that is measurable in principle and that the diversification literature does not consider, and it predicts that the benefit rises with the number of lines exercising the shared element rather than with the number of lines as such.

The reliability and normal-accidents framing developed in [Perrow 1984][book_perrow_1984], [Vaughan 1996][book_vaughan_1996], and [Weick and Sutcliffe 2007][book_weick_sutcliffe_2007] treats the shared-vehicle common factor as an irreducible property of a tightly coupled system rather than as an engineering deficiency to be corrected. The framing implies that the correlated exposure the article documents cannot be designed away and must instead be absorbed, which supports the article's emphasis on the surviving subscription revenue rather than on any prospective reliability improvement.

The actor-network framing developed in [Latour 1987][book_latour_1987], [Callon 1984][research_callon_1986], and [Law 1987][research_law_1987] treats the lines as heterogeneous assemblages whose boundaries are analytical impositions rather than natural facts, and it offers the useful caution that the five-line partition this article adopts is a choice for which the firm's own internal organization may supply no warrant.

## Pattern Extraction

The portfolio-patience pattern that the SpaceX case exhibits supports the following abstract statement without naming any downstream application. A mission-directed technology venture achieves the portfolio-patience closure when it holds several revenue-bearing lines generated from a shared capability base, whose adverse outcomes are imperfectly correlated, each of which it will sustain across the interval that line requires, with the capital directed among them according to the mission rather than according to the return.

The abstract mechanic requires joint satisfaction of five sub-properties, admitting the compact conjunctive form

$$
\Phi^{\text{portfolio-patience}} = \prod_{k=1}^{5} \phi_k, \qquad \phi_k \in \{0,1\}
\tag{73}
$$

First, the venture must hold more than one revenue-bearing line, so that no single adverse outcome is terminal.

Second, the lines must be generated from a shared capability base rather than assembled by acquisition. This is the sub-property that distinguishes the configuration from the conglomerate the finance literature disfavors, and it is the hardest of the five to satisfy.

Third, the adverse outcomes must be imperfectly correlated, and the correlation must be evaluated per risk category rather than in aggregate. A portfolio may be well diversified against a demand event and entirely undiversified against a supply event, and reporting only the aggregate correlation conceals the distinction.

Fourth, the venture must sustain each line across the interval that line requires, which requires that the evaluation horizon be set internally rather than by an external capital provider. This sub-property is a governance property and cannot be satisfied by any portfolio composition.

Fifth, the capital must be directed among the lines according to the mission. A venture allocating according to the return holds a portfolio and is not pursuing a mission with it.

The mechanic admits a diagnostic procedure stated as an ordered test vector

$$
\tau = \left( L > 1, \;\; \left| \bigcap_\ell K_\ell \right| \gg 0, \;\; \rho^{(c)}_{\ell m} < 1 \; \forall c, \;\; \tau_\ell \geq \tau^{\ast}_\ell, \;\; f_{\ell \to m} \text{ tracks mission} \right)
\tag{74}
$$

with the second and third components the ones a candidate case will usually fail and the first the one it will usually pass.

The mechanic carries two costs the statement should not conceal. The first is that the lines compete for a finite engineering attention, so that the portfolio purchases its survival benefit with a slower rate of progress on each line than a single-line configuration would achieve. The second is that the mission-directed allocation is by construction not the return-maximizing allocation, so that the configuration is worth less to an investor who does not hold the mission than the same assets would be worth separately. The trade can be stated as

$$
\frac{\partial P^{\text{ruin}}}{\partial L} < 0 \qquad \text{while} \qquad \frac{\partial \, \text{rate of progress per line}}{\partial L} < 0
\tag{75}
$$

with both derivatives negative, so that the line count that minimizes the ruin probability is not the line count that maximizes the rate at which any single line advances. The condition is therefore not a free improvement. It is a purchase of a reduced ruin probability at a price paid in speed and investor value.

## Cross-References to the Series

The article back-references the [series opener][related_post_a281_spacex_framing] for the seven-plus-three framework and for the 2008 near-death period against which the present risk profile should be compared. The article back-references the [Value Gradient article A282][related_post_a282_spacex_value_gradient] for the launch-vehicle progression that generated the capability base. The article back-references the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] for the state-anchored spacecraft line and the defense-services line. The article back-references the [Value Capture article A284][related_post_a284_spacex_value_capture] for the constellation line and the pricing structure. The article back-references the [Decomposability article A285][related_post_a285_spacex_decomposability] for the rung structure the present article distinguishes from the portfolio structure. The article back-references the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] for the shared capability base without which the portfolio would be assembled rather than generated. The article back-references the [Governance article A287][related_post_a287_spacex_governance] for the control configuration that permits the evaluation horizon to be set internally, which the fourth sub-property requires.

The article forward-references the remaining articles. The Government-Anchor Capital-Formation Leg article A289, the Patient-Private Capital-Formation Leg article A290, and the Category-Dominating Commercial Spinoff article A291 treat the three financing channels that supplied the capital the portfolio allocates. The closing article A292 synthesizes across the framework.

The article cross-references the existing published corpus including the [Introduction to Space Studies article A90][related_post_a90_intro_space_studies], the [History of Rocketplanes article A96][related_post_a96_history_rocketplanes], the [What Does the United States Space Force Do article A97][related_post_a97_us_space_force], the [Framing and the Co-Development Mechanism article A237][related_post_a237_aerospace_framing], the [Silicon Valley from Defense Contracting article A246][related_post_a246_silicon_valley_defense], the [Software-Defined Aerospace article A247][related_post_a247_software_defined_aerospace], the [Contemporary Snapshot article A248][related_post_a248_contemporary_snapshot], and the [Why Startups Actually Fail article A167][related_post_a167_startup_failure].

## Terminological Note

The article adopts terminology consistent with the finance and strategy conventions and departs from them where necessary. The term "line" refers to a revenue-bearing business activity, and it is used in preference to "segment" because the latter carries a reporting connotation that would misleadingly suggest the firm publishes one. The term "generated portfolio" refers to a line set produced by redeploying a shared capability base, and "assembled portfolio" refers to a line set acquired. The term "patience" refers to the length of the interval across which a line will be sustained without a positive return, and it is a property of the evaluating party rather than of the line. The term "ruin" refers to the event in which the venture's capital position reaches the level at which it ceases to operate, and it is distinguished from a negative return of any magnitude that leaves the venture operating. The term "cross-subsidization" refers to a directed transfer of capital from a line to another, and it carries no pejorative connotation in this article.

## Load-Bearing Open Questions

The article closes with the load-bearing open questions the treatment leaves unresolved. First, the causal direction between the portfolio and the survival is genuinely ambiguous, and the observational record cannot separate the hypothesis that the portfolio produced the survival from the hypothesis that the survival permitted the portfolio. Second, the internal transfer prices are unknown, which means that substantially every per-line quantitative claim in this article rests on an assumption the article cannot verify. Third, the shared-vehicle common factor means the portfolio contributes substantially no protection against the most likely catastrophic operational event, and the article does not resolve how much the surviving subscription revenue offsets that exposure. Fourth, the key-person common factor is perfectly correlated across the lines and interacts adversely with the governance condition, and the framework does not otherwise surface the interaction. Fifth, the conglomerate-discount objection is answered by an argument about the objective rather than by evidence, and a reader who does not accept the mission as a legitimate corporate objective will find the answer unpersuasive. Sixth, the patience the article documents is not distinguishable from an escalation of commitment using the evidence available while the Starship programme remains incomplete.

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 75 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 75, 18 are established and 57 are bespoke.
Returns, weights, correlations and probabilities are dimensionless, runways are measured in time, and flows, costs and values carry whatever currency unit a section uses, while most equations state the structure of an argument and are not evaluated with data.

**Equation 1, Portfolio Return.**
The portfolio return is the weighted sum of the line returns, with weights that sum to one.
[Markowitz 1952][research_markowitz_1952]

$$
R^{\text{portfolio}}(t) = \sum_{\ell \in \mathcal{L}} w_\ell(t) \, R_\ell(t) \qquad \text{with} \qquad \sum_{\ell} w_\ell(t) = 1
\tag{1}
$$

**Equation 2, Portfolio Variance.**
The portfolio variance is the double sum over pairs of lines of the two weights, the correlation and the two standard deviations.
[Markowitz 1952][research_markowitz_1952]

$$
\sigma^2_{\text{portfolio}} = \sum_{\ell} \sum_{m} w_\ell w_m \, \rho_{\ell m} \, \sigma_\ell \sigma_m
\tag{2}
$$

**Equation 3, Finite-Horizon Ruin Probability.**
The ruin probability is the probability that the cash position first falls to zero or below at some time before the horizon.

$$
P^{\text{ruin}}(T) = P\!\left( \exists \, t \leq T \; : \; C(t) \leq 0 \right)
\tag{3}
$$

*Equation 4, Bespoke Ruin Probability of Independent Lines.*
Ruin of the portfolio is approximated as the product of the line failure probabilities, which assumes that failures are independent and that any one surviving line averts ruin.

$$
P^{\text{ruin}}_{\text{portfolio}} \approx \prod_{\ell \in \mathcal{L}} P^{\text{failure}}_\ell \qquad \text{against} \qquad P^{\text{ruin}}_{\text{single bet}} = P^{\text{failure}}_1
\tag{4}
$$

**Equation 5, Correlation Matrix of the Lines.**
The correlation matrix collects the pairwise correlations between every two lines of the portfolio.

$$
\boldsymbol{\rho} = \left[ \rho_{\ell m} \right]_{\ell, m \in \mathcal{L}}
\tag{5}
$$

*Equation 6, Bespoke Single-Line Counterfactual Differential.*
The portfolio contribution is defined as the observed value less the value under a counterfactual in which the firm pursued the mission through a single line.

$$
\Delta V^{\text{portfolio}}_i(t) = V^{\text{observed}}_i(t) - V^{\text{single-line counterfactual}}_i(t)
\tag{6}
$$

*Equation 7, Bespoke Patience Condition.*
The condition requires the interval the venture will sustain each line without a positive return to be at least the interval that line in fact requires.

$$
\tau_\ell \geq \tau^{\ast}_\ell \qquad \forall \ell \in \mathcal{L}
\tag{7}
$$

*Equation 8, Bespoke Correspondence of Patience and Discount Rate.*
The article treats the tolerated horizon and the discount rate of a line as two descriptions of one parameter, with the horizon falling as the rate rises.

$$
\tau_\ell \; \longleftrightarrow \; \rho_\ell \qquad \text{with} \qquad \frac{\partial \tau_\ell}{\partial \rho_\ell} < 0
\tag{8}
$$

**Equation 9, Effective Number of Equally Correlated Lines.**
For equally weighted lines of equal variance and common pairwise correlation, the portfolio variance equals that of this many independent lines, from the nominal count at zero correlation down to one at perfect correlation.

$$
L^{\text{effective}} = \frac{L}{1 + (L-1)\rho}
\tag{9}
$$

**Equation 10, Mean-Variance Utility.**
The mean-variance objective is the expected portfolio return less half a risk-aversion coefficient times the portfolio variance.

$$
U = E\!\left[ R^{\text{portfolio}} \right] - \tfrac{\gamma}{2} \sigma^2_{\text{portfolio}}
\tag{10}
$$

*Equation 11, Bespoke Survival Objective.*
The venture is taken to maximise the probability of reaching the mission, which equals one minus the ruin probability at the mission horizon.

$$
U^{\text{survival}} = P\!\left( \text{reach } M \right) = 1 - P^{\text{ruin}}(T^{\text{mission}})
\tag{11}
$$

*Equation 12, Bespoke Cross-Subsidisation Flow.*
The flow is defined as the capital directed from one line to another at a given time.

$$
f_{\ell \to m}(t) = \text{capital directed from line } \ell \text{ to line } m \text{ at } t
\tag{12}
$$

*Equation 13, Bespoke Net Capital Position of a Line.*
The net position of a line is the capital it receives from other lines less the capital it sends to them, so that a persistently negative value marks a source and a positive one a sink.

$$
n_\ell(t) = \sum_{m} f_{m \to \ell}(t) - \sum_{m} f_{\ell \to m}(t)
\tag{13}
$$

*Equation 14, Bespoke Generated Portfolio Condition.*
A portfolio is classed as generated when the capability shared by every line is non-empty and forms a substantial fraction of all the capability the lines require.

$$
\bigcap_{\ell \in \mathcal{L}} K_\ell \neq \varnothing \qquad \text{and} \qquad \left| \bigcap_{\ell} K_\ell \right| \big/ \left| \bigcup_{\ell} K_\ell \right| \gg 0
\tag{14}
$$

**Equation 15, Sharpe Ratio.**
The Sharpe ratio is the expected portfolio return in excess of the risk-free rate divided by the portfolio standard deviation.
[Sharpe 1964][research_sharpe_1964]

$$
S = \frac{E\!\left[R^{\text{portfolio}}\right] - r_f}{\sigma_{\text{portfolio}}}
\tag{15}
$$

**Equation 16, Berger and Ofek Excess Value.**
Excess value is the natural logarithm of the observed firm value divided by the imputed value of its segments, each an industry median multiple times an accounting base.
[Berger and Ofek 1995][research_berger_ofek_1995]

$$
EV = \ln\!\left( \frac{V^{\text{observed}}}{\sum_\ell m_\ell \cdot A_\ell} \right)
\tag{16}
$$

*Equation 17, Bespoke Allocation Quality.*
Allocation quality is defined as the correlation across lines between the capital directed to a line and its investment opportunity.

$$
Q^{\text{allocation}} = \operatorname{corr}\!\left( \Delta k_\ell, \; q_\ell \right)
\tag{17}
$$

**Equation 18, Portfolio of Options Dominates an Option on a Portfolio.**
The expected sum of separate call payoffs is at least the expected payoff of a single call on the summed values and strike prices, because the positive part of a sum never exceeds the sum of positive parts.
[Merton 1973][research_merton_1973]

$$
\sum_{\ell} E\!\left[ \max(V_\ell - K_\ell, 0) \right] \geq E\!\left[ \max\!\left( \sum_\ell V_\ell - \sum_\ell K_\ell, 0 \right) \right]
\tag{18}
$$

**Equation 19, Lundberg Bound on Ultimate Ruin.**
The classical ruin-theory bound limits the probability of ultimate ruin to an exponential in the initial capital with the adjustment coefficient as rate.

$$
P^{\text{ruin}}(\infty) \leq e^{-\Lambda \, C(0)}
\tag{19}
$$

*Equation 20, Bespoke Penrose Slack Measure.*
Slack is defined as the sum over capabilities of the positive part of capacity less utilisation, a formalisation the article gives of the underused resources in the Penrose account.
[Penrose 1959][book_penrose_1959]

$$
\Sigma(t) = \sum_{k \in K} \left[ \bar{u}_k - u_k(t) \right]^{+}
\tag{20}
$$

*Equation 21, Bespoke Platform Leverage.*
Platform leverage is defined as the summed value of the lines divided by the cost of the shared capability base.

$$
\Lambda^{\text{platform}} = \frac{\sum_{\ell} V_\ell}{C^{\text{shared base}}}
\tag{21}
$$

*Equation 22, Bespoke Exponential Decay of Advantage.*
The advantage of a line is modelled as decaying exponentially at the clockspeed of its industry, a functional form the article assumes for the clockspeed argument.

$$
A_\ell(t) = A_\ell(0) \, e^{-\kappa_\ell t}
\tag{22}
$$

**Equation 23, Free Cash Flow Prediction of Diversification.**
The agency theory of free cash flow predicts that diversification rises with the free cash flow available to managers.
[Jensen 1986][research_jensen_1986]

$$
\frac{\partial \, \text{diversification}}{\partial \, \text{free cash flow}} > 0 \qquad \text{under the agency reading}
\tag{23}
$$

*Equation 24, Bespoke Learning Curve on Pooled Volume.*
The learning curve is applied to the shared production element with cumulative volume summed across all lines, which assumes that experience pools across the lines.
[Wright 1936][research_wright_1936]

$$
c^{\text{shared}}_n = c^{\text{shared}}_1 \left( \sum_{\ell} n_\ell \right)^{-b}
\tag{24}
$$

*Equation 25, Bespoke Falcon Dependency of the Revenue Lines.*
The statement places the Falcon capability in the capability set of each of the four revenue lines other than next-generation development.

$$
K^{\text{Falcon}} \in K_\ell \qquad \text{for} \qquad \ell \in \{\text{launch}, \text{spacecraft}, \text{constellation}, \text{defense}\}
\tag{25}
$$

*Equation 26, Bespoke Correlation Decomposition by Risk Category.*
The correlation between two lines is modelled as a weighted sum of category-specific correlations, an additive decomposition the article assumes.

$$
\rho_{\ell m} = \sum_{c \in \mathcal{C}} \omega_c \, \rho^{(c)}_{\ell m}
\tag{26}
$$

*Equation 27, Bespoke Effective Line Count Vector.*
The effective line count is reported as a vector with one component for each risk category rather than as a single number.

$$
\boldsymbol{L}^{\text{effective}} = \left( L^{\text{eff}}_{\text{vehicle}}, \; L^{\text{eff}}_{\text{demand}}, \; L^{\text{eff}}_{\text{regulatory}}, \; L^{\text{eff}}_{\text{key-person}} \right)
\tag{27}
$$

*Equation 28, Bespoke Internal Consumption Fraction.*
The fraction the article defines divides the launches consumed internally by the total launches.

$$
\iota(t) = \frac{n^{\text{internal launches}}(t)}{n^{\text{total launches}}(t)}
\tag{28}
$$

*Equation 29, Bespoke Effective Weight of the Launch Line.*
The diversifying weight of the launch line is taken as its portfolio weight times its external fraction, on the premise that internal supply diversifies nothing.

$$
w^{\text{effective}}_{\text{launch}} = \left( 1 - \iota(t) \right) \cdot w_{\text{launch}}(t)
\tag{29}
$$

**Equation 30, Herfindahl Index of Customer Concentration.**
The Herfindahl index of a line is the sum of the squared revenue shares of its customers.

$$
H_\ell = \sum_{j} s_{j\ell}^2
\tag{30}
$$

**Equation 31, Ruin Sensitivity Ordered by Correlation Sign.**
Adding weight to a line lowers the ruin probability most when the line is negatively correlated with the rest, less when uncorrelated and least when positively correlated.

$$
\left. \frac{\partial P^{\text{ruin}}}{\partial w_\ell} \right|_{\rho_\ell < 0} < \left. \frac{\partial P^{\text{ruin}}}{\partial w_\ell} \right|_{\rho_\ell = 0} < \left. \frac{\partial P^{\text{ruin}}}{\partial w_\ell} \right|_{\rho_\ell > 0}
\tag{31}
$$

**Equation 32, First-Order Autocorrelation of Revenue.**
The first-order autocorrelation is the correlation between the revenue of a line in one period and its revenue in the previous period.

$$
\phi_\ell = \operatorname{corr}\!\left( r_\ell(t), \; r_\ell(t-1) \right)
\tag{32}
$$

*Equation 33, Bespoke Threshold Revenue of a Constellation.*
Constellation revenue is modelled as zero below a minimum deployed count and as a function of the deployed count above it.

$$
r^{\text{constellation}}(t) = \begin{cases} 0 & N^{\text{deployed}}(t) < N^{\text{minimum}} \\ g\!\left( N^{\text{deployed}}(t) \right) & \text{otherwise} \end{cases}
\tag{33}
$$

*Equation 34, Bespoke Defence Revenue Drivers.*
Defence revenue is modelled as linear in a threat driver and an appropriation driver plus an error term, neither driver appearing in the commercial lines.

$$
r_{\text{defense}}(t) = \beta_{\text{threat}} \, X^{\text{threat}}(t) + \beta_{\text{approp}} \, X^{\text{appropriation}}(t) + \varepsilon(t)
\tag{34}
$$

*Equation 35, Bespoke Net Contribution of the Defence Line.*
The net contribution of the defence line is a positive diversification term less a positive constraint-spillover cost, with a sign the article leaves open.

$$
\Delta_{\text{defense}} = \underbrace{\delta^{\text{diversification}}}_{> 0} - \underbrace{c^{\text{constraint spillover}}}_{> 0}
\tag{35}
$$

*Equation 36, Bespoke Negative Net Present Value of Starship.*
The net present value of Starship at the investor discount rate is asserted to be negative at any time across the period, a judgement the article makes rather than computes.

$$
\text{NPV}_{\text{Starship}}(t) = \sum_{s > t} \frac{E\!\left[ \text{CF}(s) \right]}{(1+\rho)^{s-t}} - K(t) < 0 \qquad \text{for } \rho = \rho^{\text{investor}}
\tag{36}
$$

*Equation 37, Bespoke Patience Condition for Starship.*
The patience condition is applied to Starship, requiring the horizon the controller tolerates to be at least the horizon the programme requires.

$$
\tau_{\text{Starship}} \geq \tau^{\ast}_{\text{Starship}}
\tag{37}
$$

*Equation 38, Bespoke Option Value of Starship.*
The value of Starship is constructed as a probability-weighted sum over applications of the positive part of application value net of residual investment.

$$
V^{\text{Starship}} = \sum_{a \in A} p(a) \cdot \left[ V^{\text{application}}(a) - K^{\text{residual}}(a) \right]^{+}
\tag{38}
$$

*Equation 39, Bespoke Maturity Ordering of Capital Flows.*
The statement records that positive flows run predominantly from more mature to less mature lines.

$$
f_{\ell \to m} > 0 \quad \text{predominantly for} \quad \text{maturity}(\ell) > \text{maturity}(m)
\tag{39}
$$

*Equation 40, Bespoke Lifecycle Position of a Line.*
The lifecycle position the article defines divides the cumulative revenue of a line by its cumulative investment.

$$
\mu_\ell(t) = \frac{\text{cumulative revenue}_\ell(t)}{\text{cumulative investment}_\ell(t)}
\tag{40}
$$

**Equation 41, Invariance of Total Profit to the Transfer Price.**
The combined profit of the launch and constellation lines is unchanged by the internal transfer price, which only moves profit from one line to the other.

$$
\pi_{\text{launch}} + \pi_{\text{constellation}} = \text{invariant} \qquad \text{while} \qquad \frac{\partial \pi_{\text{launch}}}{\partial p^{\text{transfer}}} > 0 > \frac{\partial \pi_{\text{constellation}}}{\partial p^{\text{transfer}}}
\tag{41}
$$

*Equation 42, Bespoke Mission and Return Allocation Quality.*
Allocation quality measured against the marginal contribution to reaching the mission is set against quality measured against investment opportunity.

$$
Q^{\text{mission}} = \operatorname{corr}\!\left( \Delta k_\ell, \; \frac{\partial P(\text{reach } M)}{\partial k_\ell} \right) \qquad \text{against} \qquad Q^{\text{return}} = \operatorname{corr}\!\left( \Delta k_\ell, \; q_\ell \right)
\tag{42}
$$

*Equation 43, Bespoke Surviving Revenue Fraction under Grounding.*
The fraction the article defines is the share of total revenue from constellation subscriptions that continues during an extended vehicle grounding.

$$
\theta = \frac{r^{\text{constellation subscription}}}{r^{\text{total}}} \qquad \text{conditional on } S
\tag{43}
$$

*Equation 44, Bespoke Effective Line Counts by Risk Category.*
The effective line count is about one for vehicle risk and three to four for demand risk, values the article estimates from its reading of the correlation structure.

$$
L^{\text{effective}} \Big|_{\text{vehicle risk}} \approx 1 \qquad \text{against} \qquad L^{\text{effective}} \Big|_{\text{demand risk}} \approx 3 \text{ to } 4
\tag{44}
$$

*Equation 45, Bespoke Stressed Runway.*
The runway under a grounding is the cash position divided by the burn rate less the surviving revenue, and it becomes unbounded once that revenue exceeds the burn.

$$
\Theta^{\text{stress}} = \frac{C(t)}{\dot{C}^{\text{burn}} - \theta \cdot r^{\text{total}}}
\tag{45}
$$

*Equation 46, Bespoke Uninsured Loss.*
The uninsured loss is the total loss less the insured loss, which the article equates with the consequential loss plus the loss of a development programme.

$$
L^{\text{uninsured}} = L^{\text{total}} - L^{\text{insured}} = L^{\text{consequential}} + L^{\text{programme}}
\tag{46}
$$

*Equation 47, Bespoke Adverse Interaction of Governance and Portfolio Closures.*
The inequality states that the survival probability given both closures falls below what independence of the two closures would imply, through the key-person channel.

$$
P\!\left( \text{survive} \mid \phi_6 = 1, \phi_7 = 1 \right) < P\!\left( \text{survive} \mid \phi_6 = 1 \right) \cdot P\!\left( \text{survive} \mid \phi_7 = 1 \right) \big/ P\!\left( \text{survive} \right)
\tag{47}
$$

*Equation 48, Bespoke Penrose Growth Constraint.*
The rate of line addition is bounded by a multiple of managerial capacity, which grows with experience, a formalisation the article gives of the Penrose effect.
[Penrose 1959][book_penrose_1959]

$$
\frac{dL}{dt} \leq \gamma \cdot M(t) \qquad \text{with} \qquad \dot{M}(t) = h\!\left( M(t), \; \text{experience} \right)
\tag{48}
$$

*Equation 49, Bespoke Attention Budget.*
Attention across lines is bounded by a fixed total, with progress on each line increasing in the attention it receives.

$$
\sum_{\ell \in \mathcal{L}} a_\ell(t) \leq \bar{A} \qquad \text{with} \qquad \frac{\partial \, \text{progress}_\ell}{\partial a_\ell} > 0
\tag{49}
$$

**Equation 50, Diversification Discount.**
The discount is the value of the diversified firm divided by the summed standalone values of its segments less one, found negative in the diversified samples.
[Lang and Stulz 1994][research_lang_stulz_1994]
[Berger and Ofek 1995][research_berger_ofek_1995]

$$
D = \frac{V^{\text{diversified}}}{\sum_{\ell} V^{\text{standalone}}_\ell} - 1 < 0
\tag{50}
$$

*Equation 51, Bespoke Undefined Standalone Valuation.*
The standalone value of a line differs from its value within the portfolio because the standalone cost exceeds the cost on the shared base.

$$
V^{\text{standalone}}_\ell \neq V_\ell \Big|_{\text{within portfolio}} \qquad \text{because} \qquad c_\ell^{\text{standalone}} > c_\ell \Big|_{\text{shared base}}
\tag{51}
$$

*Equation 52, Bespoke Investor and Venture Optimisation Problems.*
The investor is modelled as minimising variance subject to a return floor and the venture as minimising the ruin probability at the mission horizon.

$$
\text{investor solves} \; \min_w \sigma^2(w) \quad \text{s.t.} \; E[R] \geq \bar{R} \qquad \text{venture solves} \; \min_w P^{\text{ruin}}(w, T^{\text{mission}})
\tag{52}
$$

*Equation 53, Bespoke Asymmetry of Investor Diversification.*
The statement holds that investor diversification lowers the investor variance and leaves the ruin probability of the venture unchanged.

$$
\frac{\partial \sigma^2_{\text{investor}}}{\partial \text{diversification}} < 0 \qquad \text{while} \qquad \frac{\partial P^{\text{ruin}}_{\text{venture}}}{\partial \text{investor diversification}} = 0
\tag{53}
$$

*Equation 54, Bespoke Iridium Survival Condition.*
Survival is taken to require subscriber revenue above the debt-service rate from the commencement of service onward.

$$
r^{\text{subscriber}}(t) > \dot{C}^{\text{debt service}} \qquad \text{from} \qquad t = t^{\text{service commencement}}
\tag{54}
$$

*Equation 55, Bespoke Iridium Revenue Coverage Ratio.*
The coverage ratio divides subscriber revenue by the debt-service rate, a variant of the debt-service coverage ratio that uses revenue in place of operating income.

$$
\Xi(t) = \frac{r^{\text{subscriber}}(t)}{\dot{C}^{\text{debt service}}}
\tag{55}
$$

*Equation 56, Bespoke Decomposition of the Iridium Outcome Difference.*
The outcome difference between the constellation line and Iridium is split into two portfolio-patience terms and two other terms, of which the article claims only the first pair.

$$
\Delta^{\text{outcome}} = \underbrace{\Delta^{\text{funding source}} + \Delta^{\text{concurrent revenue}}}_{\text{portfolio-patience}} + \underbrace{\Delta^{\text{deployment cost}} + \Delta^{\text{market segment}}}_{\text{not portfolio-patience}}
\tag{56}
$$

*Equation 57, Bespoke Annual Appropriation Survival Product.*
The survival of the Superconducting Super Collider is expressed through a product over construction years of the probability that the appropriation continues, which assumes the years are independent.

$$
P\!\left( \text{completion} \right) = \prod_{y=1}^{Y} P\!\left( \text{appropriation continues in year } y \right)
\tag{57}
$$

*Equation 58, Bespoke All-or-Nothing Value of the Collider.*
The value of the Superconducting Super Collider is modelled as zero at any completed fraction below one and as the complete value only at completion.

$$
V^{\text{SSC}}(f) = \begin{cases} 0 & f < 1 \\ V^{\text{complete}} & f = 1 \end{cases}
\tag{58}
$$

*Equation 59, Bespoke Estimated Survival Comparison.*
The estimated survival probability of single-line ventures is asserted to be far below that of portfolio ventures, a comparison the article reads from the sector record.

$$
\hat{P}\!\left( \text{survival} \mid \text{single line} \right) \ll \hat{P}\!\left( \text{survival} \mid \text{portfolio} \right)
\tag{59}
$$

*Equation 60, Bespoke Survivorship Confounding.*
Assembling a portfolio is positively associated with survival and is itself more likely among ventures that survived the early period, which inflates the apparent benefit.

$$
P(S \mid A) > P(S) \qquad \text{with} \qquad P(A \mid S^{\text{early}}) > P(A)
\tag{60}
$$

**Equation 61, Ruin of Independent Voyages.**
With independent voyages each lost with the same probability, ruin requires every voyage to be lost, so its probability is the loss probability raised to the voyage count.

$$
P^{\text{ruin}} = q^{\, n} \qquad \text{against} \qquad P^{\text{ruin}} = q \quad \text{for the single-voyage partnership}
\tag{61}
$$

**Equation 62, Probability That at Least One Route Succeeds.**
For independent routes the probability that at least one succeeds is one minus the product of the failure probabilities.

$$
P(\text{at least one succeeds}) = 1 - \prod_{r} \left( 1 - p_r \right)
\tag{62}
$$

*Equation 63, Bespoke Precedent Classification Pair.*
The pair of indicators for multiple lines and a shared capability base classifies the historical precedents into cells, a classification the article constructs.

$$
\chi = \left( \mathbb{1}\!\left[ L > 1 \right], \; \mathbb{1}\!\left[ \textstyle\bigcap_\ell K_\ell \neq \varnothing \right] \right)
\tag{63}
$$

*Equation 64, Bespoke Ordering of Patience by Organisational Form.*
Patience is ordered from state programmes through founder-controlled and venture-backed private firms to listed firms, a ranking the article asserts.

$$
\tau^{\text{state programme}} > \tau^{\text{founder-controlled private}} > \tau^{\text{venture-backed private}} > \tau^{\text{listed}}
\tag{64}
$$

*Equation 65, Bespoke Substitution of Portfolio and Assured Capital.*
The ruin probability is posited to depend on the stronger of the effective line count and the assured-capital runway rather than on their sum.

$$
P^{\text{ruin}} = f\!\left( \min\left\{ L^{\text{effective}}, \; \Theta^{\text{assured capital}} \right\} \right)
\tag{65}
$$

*Equation 66, Bespoke Portfolio-Patience Closure Vector.*
Each organisation receives a binary vector over the five portfolio-patience sub-properties that the pattern-extraction section states.

$$
\boldsymbol{\phi}_j^{\text{portfolio-patience}} \in \{0,1\}^{5}
\tag{66}
$$

*Equation 67, Bespoke Correlation of Multiplicity and Generation.*
The statement records the article's finding that the multiplicity and generation indicators are nearly uncorrelated across its scored set.

$$
\operatorname{corr}_j\!\left( \phi_{j,1}^{\text{multiplicity}}, \; \phi_{j,2}^{\text{generation}} \right) \approx 0
\tag{67}
$$

*Equation 68, Bespoke Gain from Vertical Integration.*
The integration gain is approximated as the upstream launch margin over marginal cost times the internally consumed quantity, which omits any change in downstream price.

$$
\Delta^{\text{integration}} = \left( p^{\text{market}}_{\text{launch}} - c^{\text{marginal}}_{\text{launch}} \right) \cdot q^{\text{internal}}
\tag{68}
$$

*Equation 69, Bespoke Multiplicative Resource-Quality Criterion.*
The resource criterion is written as the product of value, rarity, inimitability and non-substitutability, a multiplicative form the article chose for the four resource-based criteria.
[Barney 1991][research_barney_1991]

$$
\Pi_\ell = V_\ell \cdot R_\ell \cdot I_\ell \cdot N_\ell
\tag{69}
$$

*Equation 70, Bespoke Platform Correspondence.*
The correspondence maps the platform to the capability shared by every line and the applications to the line set.

$$
\text{platform} \longleftrightarrow \bigcap_\ell K_\ell \qquad \text{applications} \longleftrightarrow \mathcal{L}
\tag{70}
$$

*Equation 71, Bespoke Escalation Test.*
Escalation predicts that continuation is insensitive to arriving evidence, whereas rational updating predicts that continuation falls with adverse evidence.

$$
\frac{\partial P\!\left( \text{continue} \right)}{\partial \, \text{signal}} \approx 0 \qquad \text{under escalation} \qquad \text{against} \qquad < 0 \quad \text{under rational updating}
\tag{71}
$$

*Equation 72, Bespoke Two-Direction Covariance Decomposition.*
The covariance of portfolio and survival is split into a term for portfolio causing survival and a term for survival permitting portfolio, which the record cannot separate.

$$
\text{Cov}\!\left( \text{portfolio}, \; \text{survival} \right) = \underbrace{\beta_1}_{\text{portfolio causes survival}} + \underbrace{\beta_2}_{\text{survival permits portfolio}}
\tag{72}
$$

*Equation 73, Bespoke Portfolio-Patience Conjunctive Closure.*
Closure is the product of five binary sub-property indicators, so that it obtains only when every indicator is one.

$$
\Phi^{\text{portfolio-patience}} = \prod_{k=1}^{5} \phi_k, \qquad \phi_k \in \{0,1\}
\tag{73}
$$

*Equation 74, Bespoke Portfolio-Patience Test Vector.*
The test vector collects the five diagnostic conditions, from more than one line to flows that track the mission.

$$
\tau = \left( L > 1, \;\; \left| \bigcap_\ell K_\ell \right| \gg 0, \;\; \rho^{(c)}_{\ell m} < 1 \; \forall c, \;\; \tau_\ell \geq \tau^{\ast}_\ell, \;\; f_{\ell \to m} \text{ tracks mission} \right)
\tag{74}
$$

*Equation 75, Bespoke Trade between Survival and Progress.*
Adding lines lowers the ruin probability and also lowers the rate of progress on each line, so the two objectives call for different line counts.

$$
\frac{\partial P^{\text{ruin}}}{\partial L} < 0 \qquad \text{while} \qquad \frac{\partial \, \text{rate of progress per line}}{\partial L} < 0
\tag{75}
$$

### Notation

- $\mathcal{L}$, the set of revenue-bearing lines
- $w_\ell$, the portfolio weight of the line $\ell$
- $R_\ell(t)$, the return of the line $\ell$ at time $t$
- $\rho_{\ell m}$, the correlation between the lines $\ell$ and $m$
- $\sigma_\ell$, the standard deviation of the return of the line $\ell$
- $P^{\text{ruin}}$, the probability that the cash position falls to zero before the horizon
- $C(t)$, the cash position of the venture
- $\tau_\ell$, the interval the venture will sustain the line $\ell$ before requiring a positive return
- $\tau^{\ast}_\ell$, the interval the line $\ell$ in fact requires
- $\rho_\ell$, the discount rate applied to the line $\ell$
- $L^{\text{effective}}$, the effective number of independent lines
- $\gamma$, the risk-aversion coefficient in the mean-variance objective
- $f_{\ell \to m}$, the capital directed from the line $\ell$ to the line $m$
- $n_\ell(t)$, the net capital position of the line $\ell$
- $K_\ell$, the capability set the line $\ell$ requires
- $r_f$, the risk-free rate
- $m_\ell$, an industry median valuation multiple for the segment $\ell$
- $A_\ell$, an accounting base for the segment $\ell$, and in the clockspeed equation the advantage of the line
- $\Lambda$, the adjustment coefficient of ruin theory
- $\kappa_\ell$, the clockspeed of the industry of the line $\ell$
- $b$, the learning exponent of the progress function
- $\iota(t)$, the fraction of launches consumed internally
- $H_\ell$, the Herfindahl index of customer concentration in the line $\ell$
- $\phi_\ell$, the first-order autocorrelation of the revenue of the line $\ell$
- $\mu_\ell(t)$, the cumulative revenue of the line $\ell$ divided by its cumulative investment
- $\theta$, the fraction of revenue that survives an extended vehicle grounding
- $\Theta^{\text{stress}}$, the runway under a grounding
- $\Xi(t)$, the ratio of subscriber revenue to the debt-service rate
- $q$, the loss probability of a single voyage
- $p_r$, the success probability of the route $r$
- $\boldsymbol{\phi}_j$, the binary closure vector of the organisation $j$ over five sub-properties
- $\Phi^{\text{portfolio-patience}}$, the conjunctive closure, the product of the five sub-property indicators

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- Abernathy, William J., and Kim B. Clark. 1985. "Innovation: Mapping the Winds of Creative Destruction." *Research Policy* 14 (1): 3–22. [https://doi.org/10.1016/0048-7333(85)90021-6][research_abernathy_clark_1985]
- Adner, Ron, and Rahul Kapoor. 2009. "Value Creation in Innovation Ecosystems: How the Structure of Technological Interdependence Affects Firm Performance in New Technology Generations." *Strategic Management Journal* 31 (3): 306–33. [https://doi.org/10.1002/smj.821][research_adner_kapoor_2010]
- Argote, Linda, and Paul Ingram. 2000. "Knowledge Transfer: A Basis for Competitive Advantage in Firms." *Organizational Behavior and Human Decision Processes* 82 (1): 150–69. [https://doi.org/10.1006/obhd.2000.2893][research_argote_ingram_2000]
- Berger, Philip G., and Eli Ofek. 1995. "Diversification's Effect on Firm Value." *Journal of Financial Economics* 37 (1): 39–65. [https://doi.org/10.1016/0304-405x(94)00798-6][research_berger_ofek_1995]
- Coase, R. H. 1937. "The Nature of the Firm." *Economica* 4 (16): 386–405. [https://doi.org/10.1111/j.1468-0335.1937.tb00002.x][research_coase_1937]
- DeAngelo, Harry, and Linda DeAngelo. 1985. "Managerial Ownership of Voting Rights." *Journal of Financial Economics* 14 (1): 33–69. [https://doi.org/10.1016/0304-405x(85)90043-1][research_deangelo_deangelo_1985]
- Duane, J. T. 1964. "Learning Curve Approach to Reliability Monitoring." *IEEE Transactions on Aerospace* 2 (2): 563–66. [https://doi.org/10.1109/ta.1964.4319640][research_duane_1964]
- Eisenhardt, Kathleen M., and Jeffrey A. Martin. 2000. "Dynamic Capabilities: What Are They?" *Strategic Management Journal* 21 (10–11): 1105–21. [https://doi.org/10.1002/1097-0266(200010/11)21:10/11\<1105::aid-smj133\>3.0.co;2-e][research_eisenhardt_martin_2000]
- Finkelstein, Sydney, and Shade H. Sanford. 2000. "Learning from Corporate Mistakes:." *Organizational Dynamics* 29 (2): 138–48. [https://doi.org/10.1016/s0090-2616(00)00020-6][research_finkelstein_sanford_2000]
- Fixson, Sebastian K. 2004. "Product Architecture Assessment: A Tool to Link Product, Process, and Supply Chain Design Decisions." *Journal of Operations Management* 23 (3–4): 345–69. [https://doi.org/10.1016/j.jom.2004.08.006][research_fixson_2005]
- Gawer, Annabelle, and Michael A. Cusumano. 2013. "Industry Platforms and Ecosystem Innovation." *Journal of Product Innovation Management* 31 (3): 417–33. [https://doi.org/10.1111/jpim.12105][research_gawer_cusumano_2014]
- Grant, Robert M. 1996. "Toward a Knowledge-Based Theory of the Firm." *Strategic Management Journal* 17 (S2): 109–22. [https://doi.org/10.1002/smj.4250171110][research_grant_1996]
- Helfat, Constance E., and Margaret A. Peteraf. 2003. "The Dynamic Resource-Based View: Capability Lifecycles." *Strategic Management Journal* 24 (10): 997–1010. [https://doi.org/10.1002/smj.332][research_helfat_peteraf_2003]
- Hertzfeld, Henry R. 2002. "Measuring the Economic Returns from Successful NASA Life Sciences Technology Transfers." *Journal of Technology Transfer* 27 (4): 311–20. [https://doi.org/10.1023/a:1020207506064][research_hertzfeld_2002]
- Jacobides, Michael G., Carmelo Cennamo, and Annabelle Gawer. 2018. "Towards a Theory of Ecosystems." *Strategic Management Journal* 39 (8): 2255–76. [https://doi.org/10.1002/smj.2904][research_jacobides_et_al_2018]
- Jensen, Michael C., and William H. Meckling. 1976. "Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure." *Journal of Financial Economics* 3 (4): 305–60. [https://doi.org/10.1016/0304-405x(76)90026-x][research_jensen_meckling_1976]
- Kessler, Donald J., and Burton G. Cour-Palais. 1978. "Collision Frequency of Artificial Satellites: The Creation of a Debris Belt." *Journal of Geophysical Research: Space Physics* 83 (A6): 2637–46. [https://doi.org/10.1029/ja083ia06p02637][research_kessler_courpalais_1978]
- Klepper, Steven. 2010. "The Origin and Growth of Industry Clusters: The Making of Silicon Valley and Detroit." *Journal of Urban Economics* 67 (1): 15–32. [https://doi.org/10.1016/j.jue.2009.09.004][research_klepper_2010]
- Lerner, Joshua. 1994. "The Syndication of Venture Capital Investments." *Financial Management* 23 (3): 16. [https://doi.org/10.2307/3665618][research_lerner_1994_syndication]
- Lieberman, Marvin B. 1984. "The Learning Curve and Pricing in the Chemical Processing Industries." *RAND Journal of Economics* 15 (2): 213. [https://doi.org/10.2307/2555676][research_lieberman_1984]
- MacCormack, Alan, Carliss Baldwin, and John Rusnak. 2012. "Exploring the Duality between Product and Organizational Architectures: A Test of the “Mirroring” Hypothesis." *Research Policy* 41 (8): 1309–24. [https://doi.org/10.1016/j.respol.2012.04.011][research_maccormack_baldwin_rusnak_2012]
- Murmann, Johann Peter, and Koen Frenken. 2006. "Toward a Systematic Framework for Research on Dominant Designs, Technological Innovations, and Industrial Change." *Research Policy* 35 (7): 925–52. [https://doi.org/10.1016/j.respol.2006.04.011][research_murmann_frenken_2006]
- Myers, Stewart C. 1977. "Determinants of Corporate Borrowing." *Journal of Financial Economics* 5 (2): 147–75. [https://doi.org/10.1016/0304-405x(77)90015-0][research_myers_1977]
- Peteraf, Margaret A. 1993. "The Cornerstones of Competitive Advantage: A Resource-Based View." *Strategic Management Journal* 14 (3): 179–91. [https://doi.org/10.1002/smj.4250140303][research_peteraf_1993]
- Sahlman, William A. 1990. "The Structure and Governance of Venture-Capital Organizations." *Journal of Financial Economics* 27 (2): 473–521. [https://doi.org/10.1016/0304-405x(90)90065-8][research_sahlman_1990]
- Sanchez, Ron, and Joseph T. Mahoney. 1996. "Modularity, Flexibility, and Knowledge Management in Product and Organization Design." *Strategic Management Journal* 17 (S2): 63–76. [https://doi.org/10.1002/smj.4250171107][research_sanchez_mahoney_1996]
- Staw, Barry M. 1976. "Knee-Deep in the Big Muddy: A Study of Escalating Commitment to a Chosen Course of Action." *Organizational Behavior and Human Performance* 16 (1): 27–44. [https://doi.org/10.1016/0030-5073(76)90005-2][research_staw_1976]
- Suárez, Fernando F., and James M. Utterback. 1995. "Dominant Designs and the Survival of Firms." *Strategic Management Journal* 16 (6): 415–30. [https://doi.org/10.1002/smj.4250160602][research_suarez_utterback_1995]
- Teece, David J. 2007. "Explicating Dynamic Capabilities: The Nature and Microfoundations of (Sustainable) Enterprise Performance." *Strategic Management Journal* 28 (13): 1319–50. [https://doi.org/10.1002/smj.640][research_teece_2007]
- Teece, David J., Gary Pisano, and Amy Shuen. 1997. "Dynamic Capabilities and Strategic Management." *Strategic Management Journal* 18 (7): 509–33. [https://doi.org/10.1002/(sici)1097-0266(199708)18:7\<509::aid-smj882\>3.0.co;2-z][research_teece_pisano_shuen_1997]
- Tversky, Amos, and Daniel Kahneman. 1992. "Advances in Prospect Theory: Cumulative Representation of Uncertainty." *Journal of Risk and Uncertainty* 5 (4): 297–323. [https://doi.org/10.1007/bf00122574][research_tversky_kahneman_1992]
- Ulrich, Karl. 1995. "The Role of Product Architecture in the Manufacturing Firm." *Research Policy* 24 (3): 419–40. [https://doi.org/10.1016/0048-7333(94)00775-3][research_ulrich_1995]
- Weeden, Brian C., and Tiffany Chow. 2012. "Taking a Common-Pool Resources Approach to Space Sustainability: A Framework and Potential Policies." *Space Policy* 28 (3): 166–72. [https://doi.org/10.1016/j.spacepol.2012.06.004][research_weeden_chow_2012]
- Wernerfelt, Birger. 1984. "A Resource-Based View of the Firm." *Strategic Management Journal* 5 (2): 171–80. [https://doi.org/10.1002/smj.4250050207][research_wernerfelt_1984]
- Winter, Sidney G. 2003. "Understanding Dynamic Capabilities." *Strategic Management Journal* 24 (10): 991–95. [https://doi.org/10.1002/smj.318][research_winter_2003]
- Wright, T. P. 1936. "Factors Affecting the Cost of Airplanes." *Journal of the Aeronautical Sciences* 3 (4): 122–28. [https://doi.org/10.2514/8.155][research_wright_1936]

### Primary Sources, Non-Peer-Reviewed

- "11 U.S. Code Chapter 11: REORGANIZATION." n.d. LII / Legal Information Institute. Accessed October 25, 2026. [https://www.law.cornell.edu/uscode/text/11/chapter-11][ref_bankruptcy_code_ch11]
- "14 CFR Part 450 -- Launch and Reentry License Requirements." n.d. Accessed October 25, 2026. [https://www.ecfr.gov/current/title-14/chapter-III/subchapter-C/part-450][ref_faa_ast_licensing_regs_450]
- Adler, Paul S., and Kim B. Clark. 1991. "Behind the Learning Curve: A Sketch of the Learning Process." *Management Science* 37 (3): 267–81. [https://doi.org/10.1287/mnsc.37.3.267][research_adler_clark_1991]
- Alchian, Armen. 1963. "Reliability of Progress Curves in Airframe Production." *Econometrica* 31 (4): 679. [https://doi.org/10.2307/1909166][research_alchian_1963]
- Amihud, Yakov, and Baruch Lev. 1981. "Risk Reduction as a Managerial Motive for Conglomerate Mergers." *Bell Journal of Economics* 12 (2): 605. [https://doi.org/10.2307/3003575][research_amihud_lev_1981]
- Anderson, Philip, and Michael L. Tushman. 1990. "Technological Discontinuities and Dominant Designs: A Cyclical Model of Technological Change." *Administrative Science Quarterly* 35 (4): 604. [https://doi.org/10.2307/2393511][research_anderson_tushman_1990]
- Argote, Linda, and Dennis Epple. 1990. "Learning Curves in Manufacturing." *Science* 247 (4945): 920–24. [https://doi.org/10.1126/science.247.4945.920][research_argote_epple_1990]
- Argote, Linda, and Ella Miron-Spektor. 2011. "Organizational Learning: From Experience to Knowledge." *Organization Science* 22 (5): 1123–37. [https://doi.org/10.1287/orsc.1100.0621][research_argote_miron_spektor_2011]
- Baldwin, Carliss Y., and C. Jason Woodard. 2009. "The Architecture of Platforms: A Unified View." In *Platforms, Markets and Innovation*. Edward Elgar Publishing. [https://doi.org/10.4337/9781849803311.00008][research_baldwin_woodard_2009]
- Barney, Jay. 1991. "Firm Resources and Sustained Competitive Advantage." *Journal of Management* 17 (1): 99–120. [https://doi.org/10.1177/014920639101700108][research_barney_1991]
- Bebchuk, Lucian A., and Kobi Kastiel. 2017. "The Untenable Case for Perpetual Dual-Class Stock." Preprint, . [https://doi.org/10.2139/ssrn.2954630][research_bebchuk_kastiel_2017]
- Bebchuk, Lucian, Reinier Kraakman, and George Triantis. 1999. *Stock Pyramids, Cross-Ownership, and the Dual Class Equity: The Creation and Agency Costs of Seperating Control from Cash Flow Rights*. National Bureau of Economic Research. [https://doi.org/10.3386/w6951][research_bebchuk_kraakman_triantis_2000]
- Beinhocker. 2006. *The Origin of Wealth*. Harvard Business Publishing. [https://www.hbsp.harvard.edu/product/5062-HBK-ENG][book_beinhocker_2006]
- Black, Fischer, and Myron Scholes. 1973. "The Pricing of Options and Corporate Liabilities." *Journal of Political Economy* 81 (3): 637–54. [https://doi.org/10.1086/260062][research_black_scholes_1973]
- Callon, Michel. 1984. "Some Elements of a Sociology of Translation: Domestication of the Scallops and the Fishermen of St Brieuc Bay." *Sociological Review* 32 (1\_suppl): 196–233. [https://doi.org/10.1111/j.1467-954x.1984.tb00113.x][research_callon_1986]
- Cohen, Wesley M., and Daniel A. Levinthal. 1990. "Absorptive Capacity: A New Perspective on Learning and Innovation." *Administrative Science Quarterly* 35 (1): 128. [https://doi.org/10.2307/2393553][research_cohen_levinthal_1990]
- "Commercial Space Transportation \| Federal Aviation AdministrationLockUnited States Department of Transportation." n.d. Accessed October 25, 2026. [https://www.faa.gov/space][ref_faa_ast]
- "Congressional Record." n.d. Accessed October 25, 2026. [https://www.congress.gov/congressional-record][ref_congressional_record]
- *Congressional Research Service Commercial Crew Report*. n.d. Congressional Research Service. [https://crsreports.congress.gov/product/pdf/R/R44708][ref_crs_commercial_crew]
- Dutton, John M., and Annie Thomas. 1984. "Treating Progress Functions as a Managerial Opportunity." *Academy of Management Review* 9 (2): 235. [https://doi.org/10.2307/258437][research_dutton_thomas_1984]
- Ethiraj, Sendil K., and Daniel Levinthal. 2004. "Modularity and Innovation in Complex Systems." *Management Science* 50 (2): 159–73. [https://doi.org/10.1287/mnsc.1030.0145][research_ethiraj_levinthal_2004]
- "FAA Financial Responsibility Requirements 14 CFR Part 440." n.d. Accessed October 25, 2026. [https://www.ecfr.gov/current/title-14/part-440][ref_faa_financial_responsibility]
- "FAA Starship Programmatic Environmental Assessment." n.d. Accessed October 25, 2026. [https://www.faa.gov/space/stakeholder\_engagement/spacex\_starship][ref_faa_starship_ea]
- Fama, Eugene F., and Michael C. Jensen. 1983. "Separation of Ownership and Control." *Journal of Law and Economics* 26 (2): 301–25. [https://doi.org/10.1086/467037][research_fama_jensen_1983]
- "FCC Direct-to-Cell Authorization." 2024. [https://docs.fcc.gov/public/attachments/DA-24-208A1.pdf][ref_fcc_direct_to_cell_2024]
- "FCC Starlink Authorization March." 2018. [https://docs.fcc.gov/public/attachments/FCC-18-38A1.pdf][ref_fcc_starlink_2018]
- "FCC Starlink Generation 2 Authorization December." 2022. [https://docs.fcc.gov/public/attachments/FCC-22-91A1.pdf][ref_fcc_starlink_gen2_2022]
- GAO. 2019. "Commercial Crew Program Evaluation." [https://www.gao.gov/products/gao-19-504][ref_gao_ccp_2019]
- GAO. 2022. "Human Landing System Evaluation." [https://www.gao.gov/products/gao-22-105506][ref_gao_hls_2022]
- GAO. 2023. "National Security Space Launch Evaluation." [https://www.gao.gov/products/gao-23-105815][ref_gao_nssl_2023]
- "GAO Reports and Testimonies Database." n.d. Accessed October 25, 2026. [https://www.gao.gov/reports-testimonies][ref_gao_reports]
- Gertner, Robert, David Scharfstein, and Jeremy Stein. 1994. *Internal versus External Capital Markets*. National Bureau of Economic Research. [https://doi.org/10.3386/w4776][research_gertner_scharfstein_stein_1994]
- Gompers, Paul A. 1995. "Optimal Investment, Monitoring, and the Staging of Venture Capital." *Journal of Finance* 50 (5): 1461–89. [https://doi.org/10.1111/j.1540-6261.1995.tb05185.x][research_gompers_1995]
- Gompers, P., J. Ishii, and A. Metrick. 2003. "Corporate Governance and Equity Prices." *Quarterly Journal of Economics* 118 (1): 107–56. [https://doi.org/10.1162/00335530360535162][research_gompers_ishii_metrick_2003]
- Gompers, Paul A., Joy Ishii, and Andrew Metrick. 2009. "Extreme Governance: An Analysis of Dual-Class Firms in the United States." *Review of Financial Studies* 23 (3): 1051–88. [https://doi.org/10.1093/rfs/hhp024][research_gompers_ishii_metrick_2010]
- Grossman, Sanford J., and Oliver D. Hart. 1986. "The Costs and Benefits of Ownership: A Theory of Vertical and Lateral Integration." *Journal of Political Economy* 94 (4): 691–719. [https://doi.org/10.1086/261404][research_grossman_hart_1986]
- Grossman, Sanford, and Oliver Hart. 1987. *One Share/One Vote and the Market for Corporate Control*. National Bureau of Economic Research. [https://doi.org/10.3386/w2347][research_grossman_hart_1988]
- Hart, Oliver, and John Moore. 1990. "Property Rights and the Nature of the Firm." *Journal of Political Economy* 98 (6): 1119–58. [https://doi.org/10.1086/261729][research_hart_moore_1990]
- "House Committee on Science Space & Tech." n.d. House Committee on Science Space & Tech - Republicans. Accessed October 25, 2026. [https://science.house.gov/][ref_house_science_committee_hearings]
- Huber, George P. 1991. "Organizational Learning: The Contributing Processes and the Literatures." *Organization Science* 2 (1): 88–115. [https://doi.org/10.1287/orsc.2.1.88][research_huber_1991]
- "Iridium Chapter 11 Bankruptcy Filing." 1999. [https://www.sec.gov/Archives/edgar/data/1029074/0000912057-99-034228.txt][ref_iridium_chapter_11_1999]
- Kahneman, Daniel, and Amos Tversky. 1979. "Prospect Theory: An Analysis of Decision under Risk." *Econometrica* 47 (2): 263. [https://doi.org/10.2307/1914185][research_kahneman_tversky_1979]
- Kaplan, Steven N., and Per Stromberg. 2003. "Financial Contracting Theory Meets the Real World: An Empirical Analysis of Venture Capital Contracts." *Review of Economic Studies* 70 (2): 281–315. [https://doi.org/10.1111/1467-937x.00245][research_kaplan_stromberg_2003]
- Kaplan, Steven N., and Per StrÖMberg. 2004. "Characteristics, Contracts, and Actions: Evidence from Venture Capitalist Analyses." *Journal of Finance* 59 (5): 2177–2210. [https://doi.org/10.1111/j.1540-6261.2004.00696.x][research_kaplan_stromberg_2004]
- Klein, Benjamin, Robert G. Crawford, and Armen A. Alchian. 1978. "Vertical Integration, Appropriable Rents, and the Competitive Contracting Process." *Journal of Law and Economics* 21 (2): 297–326. [https://doi.org/10.1086/466922][research_klein_crawford_alchian_1978]
- Kogut, Bruce, and Nalin Kulatilaka. 1994. "Operating Flexibility, Global Manufacturing, and the Option Value of a Multinational Network." *Management Science* 40 (1): 123–39. [https://doi.org/10.1287/mnsc.40.1.123][research_kogut_kulatilaka_1994]
- Kogut, Bruce, and Udo Zander. 1992. "Knowledge of the Firm, Combinative Capabilities, and the Replication of Technology." *Organization Science* 3 (3): 383–97. [https://doi.org/10.1287/orsc.3.3.383][research_kogut_zander_1992]
- La Porta, Rafael, Florencio Lopez-de-Silanes, Andrei Shleifer, and Robert W. Vishny. 1998. "Law and Finance." *Journal of Political Economy* 106 (6): 1113–55. [https://doi.org/10.1086/250042][research_laporta_et_al_1998]
- Lafontaine, Francine, and Margaret Slade. 2007. "Vertical Integration and Firm Boundaries: The Evidence." *Journal of Economic Literature* 45 (3): 629–85. [https://doi.org/10.1257/jel.45.3.629][research_lafontaine_slade_2007]
- Lane, Peter J., Balaji R. Koka, and Seemantini Pathak. 2006. "The Reification of Absorptive Capacity: A Critical Review and Rejuvenation of the Construct." *Academy of Management Review* 31 (4): 833–63. [https://doi.org/10.5465/amr.2006.22527456][research_lane_koka_pathak_2006]
- Lang, Larry H. P., and René M. Stulz. 1994. "Tobin's q, Corporate Diversification, and Firm Performance." *Journal of Political Economy* 102 (6): 1248–80. [https://doi.org/10.1086/261970][research_lang_stulz_1994]
- Levitt, Barbara, and James G. March. 1988. "Organizational Learning." *Annual Review of Sociology* 14 (1): 319–38. [https://doi.org/10.1146/annurev.so.14.080188.001535][research_levitt_march_1988]
- Lewellen, Wilbur G. 1971. "A Pure Financial Rationale for the Conglomerate Merger." *Journal of Finance* 26 (2): 521–37. [https://doi.org/10.1111/j.1540-6261.1971.tb00912.x][research_lewellen_1971]
- "Liability Convention." 1972. Accessed October 25, 2026. [https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/liability-convention.html][ref_un_liability_convention_1972]
- Lintner, John. 1965. "The Valuation of Risk Assets and the Selection of Risky Investments in Stock Portfolios and Capital Budgets." *Review of Economics and Statistics* 47 (1): 13. [https://doi.org/10.2307/1924119][research_lintner_1965]
- March, James G. 1991. "Exploration and Exploitation in Organizational Learning." *Organization Science* 2 (1): 71–87. [https://doi.org/10.1287/orsc.2.1.71][research_march_1991]
- Markowitz, Harry. 1952. "Portfolio Selection." *Journal of Finance* 7 (1): 77. [https://doi.org/10.2307/2975974][research_markowitz_1952]
- McDonald, Robert, and Daniel Siegel. 1986. "The Value of Waiting to Invest." *Quarterly Journal of Economics* 101 (4): 707. [https://doi.org/10.2307/1884175][research_mcdonald_siegel_1986]
- Merton, Robert C. 1973. "Theory of Rational Option Pricing." *Bell Journal of Economics and Management Science* 4 (1): 141. [https://doi.org/10.2307/3003143][research_merton_1973]
- Monteverde, Kirk, and David J. Teece. 1982. "Supplier Switching Costs and Vertical Integration in the Automobile Industry." *Bell Journal of Economics* 13 (1): 206. [https://doi.org/10.2307/3003441][research_monteverde_teece_1982]
- Montgomery, Cynthia A. 1994. "Corporate Diversification." *Journal of Economic Perspectives* 8 (3): 163–78. [https://doi.org/10.1257/jep.8.3.163][research_montgomery_1994]
- NASA Office of Inspector General. 2018. *Commercial Cargo Evaluation*. NASA Office of Inspector General. [https://oig.nasa.gov/docs/IG-18-016.pdf][ref_nasa_oig_ccp_cargo_2018]
- NASA Office of Inspector General. 2019. *Commercial Crew Evaluation*. NASA Office of Inspector General. [https://oig.nasa.gov/audits/?\_search=Commercial+Crew][ref_nasa_oig_ccp_2019]
- NASA Office of Inspector General. 2021. *Human Landing System Evaluation*. NASA Office of Inspector General. [https://oig.nasa.gov/docs/IG-21-024.pdf][ref_nasa_oig_hls_2021]
- Nonaka, Ikujiro. 1994. "A Dynamic Theory of Organizational Knowledge Creation." *Organization Science* 5 (1): 14–37. [https://doi.org/10.1287/orsc.5.1.14][research_nonaka_1994]
- Novak, Sharon, and Steven D. Eppinger. 2001. "Sourcing by Design: Product Complexity and the Supply Chain." *Management Science* 47 (1): 189–204. [https://doi.org/10.1287/mnsc.47.1.189.10662][research_novak_eppinger_2001]
- "Outer Space Treaty." 1967. Accessed October 25, 2026. [https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/outerspacetreaty.html][ref_un_outer_space_treaty_1967]
- Peeters, Walter. 2018. "Toward a Definition of New Space? The Entrepreneurial Perspective." *New Space* 6 (3): 187–90. [https://doi.org/10.1089/space.2017.0039][research_peeters_2018]
- *Radio Regulations*. n.d. [https://www.itu.int/pub/R-REG-RR][ref_itu_radio_regulations_2020]
- Rajan, Raghuram, Henri Servaes, and Luigi Zingales. 2000. "The Cost of Diversity: The Diversification Discount and Inefficient Investment." *Journal of Finance* 55 (1): 35–80. [https://doi.org/10.1111/0022-1082.00200][research_rajan_servaes_zingales_2000]
- Rapping, Leonard. 1965. "Learning and World War II Production Functions." *Review of Economics and Statistics* 47 (1): 81. [https://doi.org/10.2307/1924126][research_rapping_1965]
- "Registration Convention." 1976. Accessed October 25, 2026. [https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/registration-convention.html][ref_un_registration_convention_1976]
- Rivkin, Jan W., and Nicolaj Siggelkow. 2003. "Balancing Search and Stability: Interdependencies among Elements of Organizational Design." *Management Science* 49 (3): 290–311. [https://doi.org/10.1287/mnsc.49.3.290.12740][research_rivkin_siggelkow_2003]
- Robertson, David, and Karl Ulrich. 1998. "Planning for Product Platforms." *MIT Sloan Management Review*. [https://sloanreview.mit.edu/article/planning-for-product-platforms/][research_robertson_ulrich_1998]
- Ross, J., and B. M. Staw. 1993. "Organizational Escalation and Exit: Lessons from the Shoreham Nuclear Power Plant." *Academy of Management Journal* 36 (4): 701–32. [https://doi.org/10.2307/256756][research_ross_staw_1993]
- Scharfstein, David S., and Jeremy C. Stein. 2000. "The Dark Side of Internal Capital Markets: Divisional Rent-Seeking and Inefficient Investment." *Journal of Finance* 55 (6): 2537–64. [https://doi.org/10.1111/0022-1082.00299][research_scharfstein_stein_2000]
- "SEC EDGAR Company Search." n.d. Accessed October 25, 2026. [https://www.sec.gov/edgar/searchedgar/companysearch][ref_sec_edgar]
- "SEC Form D Exempt Offering Notices." n.d. Accessed October 25, 2026. [https://www.sec.gov/answers/formd.htm][ref_sec_form_d]
- "SEC Regulation S-K Disclosure Requirements." n.d. Accessed October 25, 2026. [https://www.ecfr.gov/current/title-17/part-229][ref_sec_regulation_sk]
- Sharpe, William F. 1964. "Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk." *Journal of Finance* 19 (3): 425–42. [https://doi.org/10.1111/j.1540-6261.1964.tb02865.x][research_sharpe_1964]
- Shleifer, Andrei, and Robert W. Vishny. 1997. "A Survey of Corporate Governance." *Journal of Finance* 52 (2): 737–83. [https://doi.org/10.1111/j.1540-6261.1997.tb04820.x][research_shleifer_vishny_1997]
- Sosa, Manuel E., Steven D. Eppinger, and Craig M. Rowles. 2003. "Identifying Modular and Integrative Systems and Their Impact on Design Team Interactions." *Journal of Mechanical Design* 125 (2): 240–52. [https://doi.org/10.1115/1.1564074][research_sosa_eppinger_rowles_2003]
- Stein, Jeremy C. 1997. "Internal Capital Markets and the Competition for Corporate Resources." *Journal of Finance* 52 (1): 111–33. [https://doi.org/10.1111/j.1540-6261.1997.tb03810.x][research_stein_1997]
- Todorova, Gergana, and Boris Durisin. 2007. "Absorptive Capacity: Valuing a Reconceptualization." *Academy of Management Review* 32 (3): 774–86. [https://doi.org/10.5465/amr.2007.25275513][research_todorova_durisin_2007]
- "United States Bankruptcy Courts." n.d. Accessed October 25, 2026. [https://www.uscourts.gov/court-programs/bankruptcy][ref_uscourts_bankruptcy]
- Villalonga, Belen. 2000. "Does Diversification Cause the 'Diversification Discount'?" Preprint, . [https://doi.org/10.2139/ssrn.227828][research_villalonga_2004]
- Volberda, Henk W., Nicolai J. Foss, and Marjorie A. Lyles. 2010. "PERSPECTIVE—Absorbing the Concept of Absorptive Capacity: How to Realize Its Potential in the Organization Field." *Organization Science* 21 (4): 931–51. [https://doi.org/10.1287/orsc.1090.0503][research_volberda_foss_lyles_2010]
- Weinzierl, Matthew. 2018. "Space, the Final Economic Frontier." *Journal of Economic Perspectives* 32 (2): 173–92. [https://doi.org/10.1257/jep.32.2.173][research_weinzierl_2018]
- Zahra, Shaker A., and Gerard George. 2002. "Absorptive Capacity: A Review, Reconceptualization, and Extension." *Academy of Management Review* 27 (2): 185. [https://doi.org/10.5465/amr.2002.6587995][research_zahra_george_2002]

### Secondary Sources

- Adner, Ron. 2012. *The Wide Lens: A New Strategy for Innovation*. Portfolio/Penguin. [https://openlibrary.org/works/OL16191407W][book_adner_2012]
- Adner, Ron. 2021. *Winning the Right Game: How to Disrupt, Defend, and Deliver in a Changing World*. The MIT Press. [https://mitpress.mit.edu/9780262046114/winning-the-right-game/][book_adner_2021]
- Anderson. 2023. *The Space Economy*. [https://www.wiley.com/en-us/The+Space+Economy-p-9781119911562][book_anderson_2023]
- Argote, Linda. 1999. *Organizational Learning: Creating, Retaining, and Transferring Knowledge*. Kluwer Academic. [https://openlibrary.org/works/OL2002798W][book_argote_1999]
- Argyris, Chris, and David A. Schon. 1978. *Organizational Learning*. Addison-Wesley Pub. Co. [https://www.pearson.com/en-us/subject-catalog/p/organizational-learning-a-theory-of-action-perspective/P200000005949][book_argyris_schon_1978]
- Baldwin, Carliss Y., and Kim B. Clark. 2000. *Design Rules: The Power of Modularity*. MIT Press. [https://mitpress.mit.edu/9780262024662/design-rules/][book_baldwin_clark_2000]
- Berger, Eric. 2021. *Liftoff: Elon Musk and the Desperate Early Days That Launched SpaceX*. HarperCollins Publishers Limited. [https://www.harpercollins.com/products/liftoff-eric-berger][book_berger_2021]
- Berger, Eric. 2024. *Reentry: SpaceX, Elon Musk, and the Reusable Rockets That Launched a Second Space Age*. BenBella Books, Inc. [https://openlibrary.org/works/OL37529642W][book_berger_2024]
- Berle, Adolf Augustus, and Means. 1932. *The Modern Corporation and Private Property*. Macmillan. [https://www.routledge.com/The-Modern-Corporation-and-Private-Property/Berle-Means/p/book/9780887388873][book_berle_means_1932]
- Bird, Kai, and Martin J. Sherwin. 2005. *American Prometheus: The Triumph and Tragedy of J. Robert Oppenheimer*. A.A. Knopf. [https://openlibrary.org/works/OL1905682W][book_bird_sherwin_2005]
- Bork, Robert H. 1978. *The Antitrust Paradox: A Policy at War with Itself*. Basic Books. [https://www.hup.harvard.edu/books/9780674032545][book_bork_1978]
- Chandler. 1962. *Strategy and Structure: Chapters in the History of the Industrial Enterprise*. M.I.T. Press. [https://mitpress.mit.edu/9780262530095/strategy-and-structure/][book_chandler_1962]
- Chandler. 1977. *The Visible Hand: The Managerial Revolution in American Business*. Belknap Press. [https://www.hup.harvard.edu/books/9780674940529][book_chandler_1977]
- Chandler, A. D. 1990. *Scale and Scope*. Harvard U.P. [https://openlibrary.org/works/OL11391139W][book_chandler_1990]
- Chernow. 2004. *Titan The Life of John D Rockefeller Sr*. [https://openlibrary.org/search?q=Chernow+Titan][book_chernow_2004]
- Concina, Ennio. 2006. *A History of Venetian Architecture*. Cambridge University Press. [https://www.cambridge.org/9780521187459][book_concina_2006]
- Copeland and Antikarov. 2001. *Real Options A Practitioner's Guide*. [https://openlibrary.org/search?q=Copeland+and+Antikarov+Real+Options+A+Practitioners+Guide][book_copeland_antikarov_2001]
- Creswell, John W., and J. David Creswell. 2014. *Research Design: Qualitative, Quantitative and Mixed Methods Approaches*. SAGE Publications. [https://us.sagepub.com/en-us/nam/research-design/book255675][book_creswell_2014]
- Cusumano, Michael A. 2010. *Staying Power: Six Enduring Principles for Managing Strategy and Innovation in an Uncertain World (Lessons from Microsoft, Apple, Intel, Google, Toyota and More)*. Oxford University Press. [https://global.oup.com/academic/product/staying-power-9780199678501][book_cusumano_2010]
- Cyert, Richard Michael, and James G. March. 1963. *A Behavioral Theory of the Firm*. Prentice-Hall. [https://openlibrary.org/works/OL2859173W][book_cyert_march_1963]
- Davenport, Christian. 2018. *The Space Barons: Elon Musk, Jeff Bezos, and the Quest to Colonize the Cosmos*. PublicAffairs. [https://www.hachettebookgroup.com/titles/christian-davenport/the-space-barons/9781610398299/][book_davenport_2018]
- Dixit, Avinash K., and Pindyck. 1994. *Investment under Uncertainty*. Princeton University Press. [https://openlibrary.org/works/OL2979477W][book_dixit_pindyck_1994]
- Easterbrook, Frank, and Daniel R. Fischel. 1991. *Economic Structure of Corporate Law*. Harvard University Press. [https://www.hup.harvard.edu/books/9780674235397][book_easterbrook_fischel_1991]
- Fernholz, Tim. 2018. *Rocket Billionaires: Elon Musk, Jeff Bezos, and the New Space Race*. Houghton Mifflin Harcourt Publishing Company. [https://www.hachettebookgroup.com/titles/tim-fernholz/rocket-billionaires/9781328662231/][book_fernholz_2018]
- Fine, Charles H. 1998. *Clockspeed: Winning Industry Control in the Age of Temporary Advantage*. Perseus Books. [https://www.hachettebookgroup.com/titles/charles-h-fine/clockspeed/9780738201535/][book_fine_1998]
- Fligstein, Neil. 2001. *The Architecture of Markets: An Economic Sociology of Twenty-First-Century Capitalist Societies*. Princeton University Press. [https://press.princeton.edu/books/paperback/9780691102542/the-architecture-of-markets][book_fligstein_2001]
- Ford, Henry, Henry Ford, Samuel Crowther, Henry Ford, Henry, Crowther, Samuel Ford, and Henry Henry Ford. 1922. *My Life and Work*. Doubleday Page & Company. [https://openlibrary.org/works/OL4418043W][book_ford_crowther_1922]
- Foster, John Bellamy, and Robert W. McChesney. 2011. *The Endless Crisis: How Monopoly-Finance Capital Produces Stagnation and Upheaval from the USA to China*. Monthly Review Press. [https://monthlyreview.org/product/endless\_crisis/][book_foster_mcchesney_2011]
- Freeman, Christopher. 1987. *Technology, Policy, and Economic Performance: Lessons from Japan*. Pinter Publishers. [https://openlibrary.org/works/OL2642736W][book_freeman_1987]
- Gawer, Annabelle, and Michael A. Cusumano. 2002. *Platform Leadership: How Intel, Microsoft, and Cisco Drive Industry Innovation*. Harvard Business School Press. [https://www.hbsp.harvard.edu/product/6155-HBK-ENG][book_cusumano_gawer_2002]
- Gertner. 2012. *The Idea Factory*. [https://www.penguinrandomhouse.com/books/206061/the-idea-factory-by-jon-gertner/][book_gertner_2012]
- Gompers, Paul A., and Lerner. 2001. *The Money of Invention: How Venture Capital Creates New Wealth*. Harvard Business School Press. [https://www.hbsp.harvard.edu/product/2434-HBK-ENG][book_gompers_lerner_2001]
- Groves, Leslie R. 1962. *Now It Can Be Told: The Story of the Manhattan Project*. Harper. [https://openlibrary.org/works/OL5912728W][book_groves_1962]
- Handberg. 1994. *Reinventing NASA*. [https://openlibrary.org/search?q=Handberg+Reinventing+NASA][book_handberg_1994]
- Hart, Oliver D. 1995. *Firms, Contracts, and Financial Structure*. Clarendon Press. [https://global.oup.com/academic/product/firms-contracts-and-financial-structure-9780198288817][book_hart_1995]
- Hartley. 2017. *The Economics of Arms*. [https://openlibrary.org/search?q=Hartley+The+Economics+of+Arms][book_hartley_2017]
- Hewlett, R. G., and Anderson. 1962. *The New World, 1939/1946*. Pennsylvania State U.P. [https://openlibrary.org/works/OL12854869W][book_hewlett_anderson_1962]
- Horwitch. 1982. *Clipped Wings The American SST Conflict*. [https://mitpress.mit.edu/9780262580620/clipped-wings/][book_horwitch_1982]
- Hovenkamp, Herbert. 2005. *The Antitrust Enterprise: Principle and Execution*. Harvard University Press. [https://openlibrary.org/works/OL3464674W][book_hovenkamp_2005]
- Hunter. 2016. *Creating Strategic Value*. [https://csis-website-prod.s3.amazonaws.com/s3fs-public/legacy\_files/files/publication/160930\_Hunter\_CreatingStrategicValue\_Web.pdf][book_hunter_2016]
- Iansiti, Marco, and Roy Levien. 2004. *The Keystone Advantage: What the New Dynamics of Business Ecosystems Mean for Strategy, Innovation, and Sustainability*. Harvard Business School Press. [https://www.hbsp.harvard.edu/product/3921-HBK-ENG][book_iansiti_levien_2004]
- Isaacson, Walter. 2023. *Elon Musk*. Simon & Schuster. [https://www.simonandschuster.com/books/Elon-Musk/Walter-Isaacson/9781982181284][book_isaacson_2023]
- Kahn, Alfred E. 1988. *The Economics of Regulation: Principles and Institutions*. MIT Press. [https://mitpress.mit.edu/9780262610520/the-economics-of-regulation/][book_kahn_1988]
- Kahneman, Daniel. 2011. *Thinking, Fast and Slow*. Penguin Books, Limited. [https://us.macmillan.com/books/9780374533557/thinkingfastandslow][book_kahneman_2011]
- Kauffman, Stuart A. 1993. *The Origins of Order: Self-Organization and Selection in Evolution*. Oxford University Press. [https://global.oup.com/academic/product/the-origins-of-order-9780195079517][book_kauffman_1993]
- Klerkx, Greg. 2004. *Lost in Space*. Secker & Warburg. [https://us.macmillan.com/books/9780375421501/lostinspace][book_klerkx_2004]
- Lane, Frederic Chapin. 1934. *Venetian Ships and Shipbuilders of the Renaissance*. The Johns Hopkins Press. [https://jhupbooks.press.jhu.edu/title/venetian-ships-and-shipbuilders-renaissance][book_lane_1934]
- Latour, Bruno. 1987. *Science in Action: How to Follow Scientists and Engineers through Society*. Harvard University Press. [https://www.hup.harvard.edu/books/9780674792913][book_latour_1987]
- Lawrence. 2016. *Airbus versus Boeing*. [https://www.routledge.com/Airbus-vs-Boeing/Lawrence/p/book/9781138287884][book_lawrence_2016]
- Lerner, Joshua. 2009. *Boulevard of Broken Dreams: Why Public Efforts to Boost Entrepreneurship and Venture Capital Have Failed and What to Do about It*. Princeton University Press. [https://press.princeton.edu/books/hardcover/9780691142197/boulevard-of-broken-dreams][book_lerner_2009]
- Levin. 2010. *The Wires That Bind*. [https://openlibrary.org/search?q=Levin+Wires+That+Bind][book_levin_2010]
- Liker, Jeffrey K. 2004. *The Toyota Way: 14 Management Principles from the World's Greatest Manufacturer*. McGraw-Hill. [https://www.mheducation.com/highered/product/toyota-way-liker/M9780071392310.html][book_liker_2004]
- Lundvall, Bengt-Ake. 1992. *National Systems of Innovation: Towards a Theory of Innovation and Interactive Learning*. Pinter Publishers. [https://openlibrary.org/works/OL9010144W][book_lundvall_1992]
- March, James G., and Simon. 1958. *Organizations*. Wiley. [https://www.wiley.com/en-us/Organizations%2C+2nd+Edition-p-9780631186311][book_march_simon_1958]
- Markowitz, Harry Max. 1959. *Portfolio Selection: Efficient Diversification of Investments (Cowles Foundation Monograph: No. 16)*. Yale University Press. [https://yalebooks.yale.edu/book/9780300013726/portfolio-selection/][book_markowitz_1959]
- Mazzucato, Mariana. 2013. *The Entrepreneurial State: Debunking Public vs. Private Sector Myths*. Anthem Press. [https://marianamazzucato.com/books/the-entrepreneurial-state][book_mazzucato_2013]
- Mazzucato, Mariana. 2021. *Mission Economy: A Moonshot Guide to Changing Capitalism*. Penguin Books, Limited. [https://marianamazzucato.com/books/mission-economy/][book_mazzucato_2021]
- Melman, Seymour. 1970. *Pentagon Capitalism: The Management of the New Imperialism*. McGraw-Hill. [https://openlibrary.org/works/OL1299274W][book_melman_1970]
- Metcalfe, J. Stanley. 1998. *Evolutionary Economics and Creative Destruction*. Taylor & Francis Group. [https://www.routledge.com/Evolutionary-Economics-and-Creative-Destruction/Metcalfe/p/book/9780415158671][book_metcalfe_1998]
- Metrick, Andrew, and Yasuda. 2011. *Venture Capital and the Finance of Innovation*. Wiley. [https://openlibrary.org/works/OL3690888W][book_metrick_yasuda_2011]
- Meyer, Marc H., and Lehnerd. 1997. *The Power of Product Platforms: Building Value and Cost Leadership*. Free Press. [https://www.simonandschuster.com/books/The-Power-of-Product-Platforms/Marc-H-Meyer/9780684825809][book_meyer_lehnerd_1997]
- Miller. 1995. *Lockheed's Skunk Works: The First Fifty Years*. Aerofax. [https://openlibrary.org/works/OL7006663W][book_miller_1995]
- Mowery, David C., and Nathan Rosenberg. 1998. *Paths of Innovation: Technological Change in 20th-Century America*. Cambridge University Press. [https://openlibrary.org/works/OL21370782W][book_mowery_rosenberg_1998]
- Musa, John D. 1998. *Software Reliability Engineering*. Osborne/McGraw-Hill. [https://openlibrary.org/works/OL4781285W][book_musa_1998]
- Nelson, Richard R. 1993. *National Innovation Systems: A Comparative Analysis*. Oxford University Press, Incorporated. [https://global.oup.com/academic/product/national-innovation-systems-9780195076172][book_nelson_1993]
- Nelson, Richard R., and Winter. 1982. *An Evolutionary Theory of Economic Change*. Belknap Press of Harvard University Press. [https://www.hup.harvard.edu/books/9780674272286][book_nelson_winter_1982]
- Nevins. 1954. *Ford The Times The Man The Company*. [https://openlibrary.org/search?q=Nevins+Ford+The+Times+The+Man+The+Company][book_nevins_1954]
- Newhouse, John. 1982. *The Sporty Game*. Knopf. [https://openlibrary.org/works/OL2625941W][book_newhouse_1982]
- Newhouse, John. 2007. *Boeing versus Airbus*. Knopf Doubleday Publishing Group. [https://us.macmillan.com/books/9781400079131/boeingversusairbus][book_newhouse_2007]
- Nonaka, Ikujirō, and Takeuchi. 1995. *The Knowledge-Creating Company: How Japanese Companies Create the Dynamics of Innovation*. Oxford University Press. [https://global.oup.com/academic/product/the-knowledge-creating-company-9780195092691][book_nonaka_takeuchi_1995]
- O'Connor, Patrick D. T., and Kleyner. 2012. *Practical Reliability Engineering*. Wiley. [https://openlibrary.org/works/OL3744715W][book_oconnor_kleyner_2012]
- Ohno, Taiichi. 1988. *Toyota Production System: Beyond Large-Scale Production*. Productivity Press. [https://openlibrary.org/works/OL8681881W][book_ohno_1988]
- Ormerod, Paul. 2005. *Why Most Things Fail: Evolution, Extinction and Economics*. Faber & Faber, Incorporated. [https://us.macmillan.com/books/9780375421099/whymostthingsfail][book_ormerod_2005]
- Owen. 1997. *Concorde The Story of a Supersonic Pioneer*. [https://openlibrary.org/search?q=Owen+Concorde+Story+of+a+Supersonic+Pioneer][book_owen_1997]
- Owen, Kenneth. 2001. *Concorde and the Americans*. Smithsonian Institution Press. [https://openlibrary.org/works/OL3341689W][book_owen_2001]
- Penrose, Edith Tilton. 1959. *The Theory of the Growth of the Firm*. Oxford University Press. [https://global.oup.com/academic/product/the-theory-of-the-growth-of-the-firm-9780199573844][book_penrose_1959]
- Perez, Carlota. 2002. *Technological Revolutions and Financial Capital: The Dynamics of Bubbles and Golden Ages*. Edward Elgar Publishing. [https://openlibrary.org/works/OL224128W][book_perez_2002]
- Perrow, Charles. 1984. *Normal Accidents: Living with High-Risk Technologies*. Basic Books. [https://press.princeton.edu/books/paperback/9780691004129/normal-accidents][book_perrow_1984]
- Porter, Michael E. 1980. *Competitive Strategy: Techniques for Analyzing Industries and Competitors*. Free Press. [https://www.simonandschuster.com/books/Competitive-Strategy/Michael-E-Porter/9780684841489][book_porter_1980]
- Porter, Michael E. 1985. *Competitive Advantage: Creating and Sustaining Superior Performance*. Free Press. [https://www.simonandschuster.com/books/Competitive-Advantage/Michael-E-Porter/9780684841465][book_porter_1985]
- Posner, Richard A. 2001. *Antitrust Law: An Economic Perspective*. University of Chicago Press. [https://openlibrary.org/works/OL1924317W][book_posner_2001]
- Pugh, Emerson W. 1995. *Building IBM: Shaping an Industry and Its Technology*. MIT Press. [https://mitpress.mit.edu/9780262161473/building-ibm/][book_pugh_1995]
- Pugh, Emerson W., Johnson, and Palmer. 1991. *IBM's 360 and Early 370 Systems*. MIT Press. [https://mitpress.mit.edu/9780262161237/ibms-360-and-early-370-systems/][book_pugh_johnson_palmer_1991]
- Rhodes, Richard. 1986. *The Making of the Atomic Bomb*. Simon & Schuster. [https://www.simonandschuster.com/books/The-Making-of-the-Atomic-Bomb/Richard-Rhodes/9781451677614][book_rhodes_1986]
- Rich, Ben R., and Leo Janos. 1994. *Skunk Works: A Personal Memoir of My Years at Lockheed*. Hachette Book Group. [https://www.hachettebookgroup.com/titles/ben-r-rich/skunk-works/9780316743006/][book_rich_janos_1994]
- Robins, Nick. 2006. *The Corporation That Changed the World: How the East India Company Shaped the Modern Multinational*. Pluto Press. [https://openlibrary.org/works/OL2083415W][book_robins_2006]
- Roe, Mark J. 1994. *Strong Managers, Weak Owners: The Political Roots of American Corporate Finance*. Princeton University Press. [https://press.princeton.edu/books/paperback/9780691026312/strong-managers-weak-owners][book_roe_1994]
- Rogers, Everett M. 1962. *Diffusion of Innovations, 5th Edition*. Free Press. [https://www.simonandschuster.com/books/Diffusion-of-Innovations-5th-Edition/Everett-M-Rogers/9780743258234][book_rogers_1962]
- Ruttan, Vernon W. 2006. *Is War Necessary for Economic Growth?: Military Procurement and Technology Development*. Oxford University Press. [https://global.oup.com/academic/product/is-war-necessary-for-economic-growth-9780195188042][book_ruttan_2006]
- Sanderson and Uzumeri. 1997. *Managing Product Families*. McGraw-Hill Publishing Co. [https://openlibrary.org/works/OL33995941W][book_sanderson_uzumeri_1997]
- Schumpeter, Joseph Alois. 1942. *Capitalism, Socialism and Democracy*. Harper. [https://www.harpercollins.com/products/capitalism-socialism-and-democracy-joseph-a-schumpeter][book_schumpeter_1942]
- Senge, Peter, and Peter M. Senge. 1990. *The Fifth Discipline: The Art and Practice of the Learning Organization*. Doubleday/Currency. [https://www.penguinrandomhouse.com/books/163984/the-fifth-discipline-by-peter-m-senge/][book_senge_1990]
- Serling, Robert J. 1992. *Legend and Legacy: The Story of Boeing and Its People*. St. Martin's Press. [https://openlibrary.org/works/OL2769360W][book_serling_1992]
- Sharkey, William W. 1982. *The Theory of Natural Monopoly*. Cambridge University Press. [https://www.cambridge.org/9780521271943][book_sharkey_1982]
- Shingō, Shigeo. 1989. *A Study of the Toyota Production System from an Industrial Engineering Viewpoint*. Productivity Press. [https://openlibrary.org/works/OL4111563W][book_shingo_1989]
- Simon, Herbert Alexander. 1957. *Administrative Behavior: A Study of Decision-Making Processes in Administrative Organization*. Macmillan. [https://www.simonandschuster.com/books/Administrative-Behavior-4th-Edition/Herbert-A-Simon/9781439136218][book_simon_1957]
- Srnicek, Nick. 2017. *Platform Capitalism*. Polity Press. [https://www.wiley.com/en-us/Platform+Capitalism-p-9781509504879][book_srnicek_2017]
- Steensgaard, Niels. 1974. *Asian Trade Revolution of the Seventeenth Century*. University of Chicago Press. [https://openlibrary.org/works/OL7009029W][book_steensgaard_1974]
- Stern, Philip J. 2011. *The Company-State: Corporate Sovereignty and the Early Modern Foundation of the British Empire in India*. Oxford University Press. [https://global.oup.com/academic/product/the-company-state-9780195393736][book_stern_2011]
- Temin, Peter, and Galambos. 1987. *The Fall of the Bell System: A Study in Prices and Politics*. Cambridge University Press. [https://openlibrary.org/works/OL4797079W][book_temin_galambos_1987]
- Tirole, Jean. 2006. *The Theory of Corporate Finance*. Princeton University Press. [https://press.princeton.edu/books/hardcover/9780691125565/the-theory-of-corporate-finance][book_tirole_2006]
- Trigeorgis, Lenos. 1996. *Real Options: Managerial Flexibility and Strategy in Resource Allocation*. MIT Press. [https://mitpress.mit.edu/9780262201025/real-options/][book_trigeorgis_1996]
- Trubshaw. 2000. *Concorde The Inside Story*. [https://openlibrary.org/search?q=Trubshaw+Concorde+Inside+Story][book_trubshaw_2000]
- Utterback, James M. 1994. *Mastering the Dynamics of Innovation: How Companies Can Seize Opportunities in the Face of Technological Change*. Harvard Business School Press. [https://www.hbsp.harvard.edu/product/4855-HBK-ENG][book_utterback_1994]
- Vance, Ashlee. 2015. *Elon Musk: Tesla, SpaceX, and the Quest for a Fantastic Future*. HarperCollins Publishers. [https://www.harpercollins.com/products/elon-musk-ashlee-vance][book_vance_2015]
- Vaughan, Diane. 1996. *The Challenger Launch Decision: Risky Technology, Culture, and Deviance at NASA*. University of Chicago Press. [https://press.uchicago.edu/ucp/books/book/chicago/C/bo22781921.html][book_vaughan_1996]
- Weick, Karl E. 1979. *Social Psychology of Organizing*. McGraw-Hill Humanities/Social Sciences/Languages. [https://www.mheducation.com/highered/product/social-psychology-organizing-weick/M9780075548089.html][book_weick_1979]
- Weick, Karl E., and Kathleen M. Sutcliffe. 2007. *Managing the Unexpected*. John Wiley & Sons, Ltd. [https://openlibrary.org/works/OL3749104W][book_weick_sutcliffe_2007]
- Weiss, Linda. 2014. *America Inc.?: Innovation and Enterprise in the National Security State*. Cornell University Press. [https://www.cornellpress.cornell.edu/book/9780801479922/america-inc/][book_weiss_2014]
- Williamson, Oliver E. 1985. *The Economic Institutions of Capitalism: Firms, Markets, Relational Contracting*. The Free Press. [https://www.simonandschuster.com/books/The-Economic-Institutions-of-Capitalism/Oliver-E-Williamson/9780684863740][book_williamson_1985]
- Womack, James P., and Jones. 2003. *Lean Thinking: Banish Waste and Create Wealth in Your Corporation*. Free Press. [https://www.simonandschuster.com/books/Lean-Thinking/James-P-Womack/9780743249270][book_womack_jones_2003]
- Womack, James P., Daniel T. Jones, and Daniel Roos. 1990. *The Machine That Changed the World: The Story of Lean Production-- Toyota's Secret Weapon in the Global Car Wars That Is Now Revolutionizing World Industry*. Free Press. [https://www.simonandschuster.com/books/The-Machine-That-Changed-the-World/James-P-Womack/9780743299794][book_womack_jones_roos_1990]
- Wu, Tim. 2010. *The Master Switch: The Rise and Fall of Information Empires*. Alfred A. Knopf. [https://openlibrary.org/works/OL15118227W][book_wu_2010]
- Yin. 2014. *Case Study Research and Applications*. [https://us.sagepub.com/en-us/nam/case-study-research-and-applications/book250150][book_yin_2014]
- Zuboff, Shoshana. 2019. *The Age of Surveillance Capitalism: The Fight for a Human Future at the New Frontier of Power*. Profile Books Ltd. [https://www.hachettebookgroup.com/titles/shoshana-zuboff/the-age-of-surveillance-capitalism/9781610395694/][book_zuboff_2019]

### Commercial Sources

- "Aon Space and Aviation Risk Brokerage." n.d. Accessed October 25, 2026. [https://www.aon.com/][ref_aon_space_insurance]
- "ARES \| Orbital Debris Program Office." n.d. Accessed October 25, 2026. [https://orbitaldebris.jsc.nasa.gov/][ref_nasa_orbital_debris]
- "Arianespace." n.d. Accessed October 25, 2026. [https://www.arianespace.com/][ref_arianespace]
- "Artemis III." 2022. NASA. Accessed October 25, 2026. [https://www.nasa.gov/mission/artemis-iii/][ref_nasa_hls_option_b_2022]
- "Blue Origin Press Releases." n.d. Accessed October 25, 2026. [https://www.blueorigin.com/news/][ref_blue_origin_press]
- "Boeing Historical Archives." n.d. Accessed October 25, 2026. [https://www.boeing.com/history/][ref_boeing_historical_archives]
- "Boeing Press Releases." n.d. Accessed October 25, 2026. [https://boeing.mediaroom.com/][ref_boeing_press]
- "BryceTech Sector Reports." n.d. Accessed October 25, 2026. [https://brycetech.com/reports][ref_bryce_tech]
- "Chinese Space Program Documentation." n.d. Accessed October 25, 2026. [https://www.cnsa.gov.cn/english/][ref_chinese_space_program]
- "Commercial Crew Program." n.d. NASA. Accessed October 25, 2026. [https://www.nasa.gov/commercialcrew/][ref_nasa_ccp_documents]
- "Commercial Resupply Missions." n.d. NASA. Accessed October 25, 2026. [https://www.nasa.gov/commercial-resupply/][ref_nasa_crs_program_overview]
- "DOD Contract Announcements." n.d. Accessed October 25, 2026. [https://www.defense.gov/News/Contracts/][ref_dod_contracts]
- "Eutelsat Corporate Record." n.d. Accessed October 25, 2026. [https://www.eutelsat.com/][ref_eutelsat_oneweb]
- "FCC Filings Database." n.d. Accessed October 25, 2026. [https://www.fcc.gov/wireless/systems-utilities/electronic-comment-filing-system-ecfs][ref_fcc_filings]
- "Homepage: Lloyd's." n.d. Accessed October 25, 2026. [https://www.lloyds.com/][ref_lloyds_market]
- "Human Landing System." n.d. NASA. Accessed October 25, 2026. [https://www.nasa.gov/humans-in-space/human-landing-system/][ref_nasa_hls_program]
- "IBM Archives." n.d. Accessed October 25, 2026. [https://www.ibm.com/history/][ref_ibm_archives]
- "Indian Space Research Organisation Press Releases." n.d. Accessed October 25, 2026. [https://www.isro.gov.in/][ref_isro_press]
- "Iridium Corporate News Archive." n.d. Accessed October 25, 2026. [https://www.iridium.com/][ref_iridium_press_archive_1998]
- "Japanese Aerospace Exploration Agency Press Releases." n.d. Accessed October 25, 2026. [https://global.jaxa.jp/press/][ref_jaxa_press]
- "Moon to Mars." 2021. NASA. Accessed October 25, 2026. [https://www.nasa.gov/humans-in-space/artemis/][ref_nasa_hls_option_a_2021]
- "NASA Awards International Space Station Cargo Transport Contracts." 2016. NASA. Accessed October 25, 2026. [https://www.nasa.gov/news-release/nasa-awards-international-space-station-cargo-transport-contracts/][ref_nasa_crs2_press_2016]
- "NASA News." 2022. NASA, December 7. [https://www.nasa.gov/news/][ref_nasa_news]
- "News U.S. Air Force Logo." n.d. Accessed October 25, 2026. [https://www.spaceforce.mil/News/][ref_space_force_news]
- "News \| Rocket Lab." n.d. Rocket Lab. Accessed October 25, 2026. [https://www.rocketlabusa.com/updates/][ref_rocket_lab_press]
- "Northrop Grumman Press Releases." n.d. Accessed October 25, 2026. [https://news.northropgrumman.com/][ref_northrop_grumman_press]
- "OneWeb Corporate Record." n.d. Accessed October 25, 2026. [https://oneweb.net/][ref_oneweb]
- "Space Capital Quarterly Reports." n.d. Accessed October 25, 2026. [https://www.spacecapital.com/][ref_space_capital]
- "Space Force National Security Space Launch." n.d. Accessed October 25, 2026. [https://www.spaceforce.mil/News/Fact-Sheets][ref_space_force_nssl]
- "Space Force NSSL Phase 1A Award." 2018. [https://www.af.mil/News/Article-Display/Article/1671253/][ref_space_force_nssl_phase1a_2018]
- "Space Force NSSL Phase 2 Award." 2020. [https://www.spaceforce.mil/News/Article/2312953/][ref_space_force_nssl_phase2_2020]
- "SpaceX Better Than Nothing Beta Press October." 2020. [https://www.spacex.com/updates/][ref_spacex_press_beta_2020]
- "SpaceX Corporate Site." n.d. Accessed October 25, 2026. [https://www.spacex.com/][ref_spacex_company]
- "SpaceX Direct-to-Cell Partnership Announcement." 2022. [https://www.starlink.com/business/direct-to-cell][ref_spacex_starlink_direct_to_cell_tmobile_2022]
- "SpaceX Falcon 9 Vehicle Documentation." n.d. Accessed October 25, 2026. [https://www.spacex.com/vehicles/falcon-9/][ref_spacex_falcon9_vehicle]
- "SpaceX Falcon Heavy Vehicle Documentation." n.d. Accessed October 25, 2026. [https://www.spacex.com/vehicles/falcon-heavy/][ref_spacex_falcon_heavy_vehicle]
- "SpaceX News Archive." n.d. Accessed October 25, 2026. [https://www.spacex.com/updates/][ref_spacex_news_archive]
- "SpaceX Press Release Block 5 Bangabandhu-1 May." 2018. [https://www.spacex.com/updates/][ref_spacex_press_block5_bangabandhu_2018]
- "SpaceX Press Release Falcon 9 First Landing December." 2015. [https://www.spacex.com/news/2015/12/22/orbcomm-2-mission-successful-first-landing-orbital-rocket][ref_spacex_press_falcon9_first_landing_2015]
- "SpaceX Press Release Falcon Heavy First Flight February." 2018. [https://www.spacex.com/news/2018/02/06/successful-first-flight-falcon-heavy][ref_spacex_press_falcon_heavy_2018]
- "SpaceX Press Release SES-10 First Refly March." 2017. [https://www.spacex.com/news/2017/03/30/spacex-successfully-launches-first-reused-rocket][ref_spacex_press_ses10_2017]
- "SpaceX Press Release Starlink First 60 Operational Satellites May." 2019. [https://www.spacex.com/updates/][ref_spacex_press_starlink_v0_9_2019]
- "SpaceX Seattle Facility Announcement January." 2015. [https://www.spacex.com/updates/][ref_spacex_seattle_announcement_2015]
- "SpaceX Starlink Program Page." n.d. Accessed October 25, 2026. [https://www.starlink.com/][ref_spacex_starlink]
- "SpaceX Starshield Product Page." n.d. Accessed October 25, 2026. [https://www.spacex.com/starshield/][ref_spacex_starshield]
- "SpaceX Starship Program Page." n.d. Accessed October 25, 2026. [https://www.spacex.com/vehicles/starship/][ref_spacex_starship_vehicle]
- "United Launch Alliance Press Releases." n.d. Accessed October 25, 2026. [https://www.ulalaunch.com/about/news][ref_ula_press]
- Walker. 2020. "Impact of Satellite Constellations on Optical Astronomy." [https://noirlab.edu/public/products/techdocs/techdoc003/][research_walker_et_al_2020]

### General Sources

- Adilov. 2018. "An Economic Analysis of Earth Orbit Pollution." [https://www.sciencedirect.com/science/article/abs/pii/S0921800917305591][research_adilov_et_al_2018]
- "AIAA Journal of Spacecraft and Rockets." n.d. Accessed October 25, 2026. [https://arc.aiaa.org/journal/jsr][ref_aiaa_jsr]
- Anadol, Cohen, and Ferrari. 2018. "SpaceX Case Study." [https://www.hbs.edu/faculty/Pages/item.aspx?num=54001][research_anadol_cohen_2018]
- "Ars Technica Space Coverage." n.d. Accessed October 25, 2026. [https://arstechnica.com/science/space/][ref_arstechnica_space]
- "Aviation Week Coverage." n.d. Accessed October 25, 2026. [https://aviationweek.com/][ref_aviation_week]
- "Bloomberg Business News." n.d. Accessed October 25, 2026. [https://www.bloomberg.com/][ref_bloomberg]
- Bonvillian. 2018. "DARPA and the Advanced Research Projects Agency." [https://mitpress.mit.edu/9780262038522/the-darpa-model-for-transformative-technologies/][research_bonvillian_2018]
- "Breaking Defense Coverage." n.d. Accessed October 25, 2026. [https://breakingdefense.com/][ref_breaking_defense]
- "China Commercial Space Industry Analysis." n.d. Accessed October 25, 2026. [https://spacenews.com/topic/china/][ref_china_commercial_space]
- "Columbia Law School Blue Sky Blog." n.d. Accessed October 25, 2026. [https://clsbluesky.law.columbia.edu/][ref_columbia_blue_sky]
- "Defense News Coverage." n.d. Accessed October 25, 2026. [https://www.defensenews.com/][ref_defense_news]
- "Department of Energy Office of Science." n.d. Accessed October 25, 2026. [https://science.osti.gov/][ref_doe_office_of_science]
- "District of Delaware \| United States Bankruptcy Court." n.d. Accessed October 25, 2026. [https://www.deb.uscourts.gov/][ref_virgin_orbit_court]
- "European Corporate Governance Institute." n.d. Accessed October 25, 2026. [https://www.ecgi.global/][ref_ecgi]
- "European Spaceflight Homepage." n.d. *European Spaceflight*. Accessed October 25, 2026. [https://europeanspaceflight.com/][ref_european_spaceflight]
- "Financial Accounting Standards Board." n.d. Accessed October 25, 2026. [https://www.fasb.org/][ref_fasb_asc280]
- Harris and Raviv. 1988. "Corporate Governance Voting Rights and Majority Rules." [https://www.sciencedirect.com/science/article/abs/pii/0304405X88900455][research_harris_raviv_1988]
- "Harvard Law School Forum on Corporate Governance." n.d. Accessed October 25, 2026. [https://corpgov.law.harvard.edu/][ref_harvard_corpgov_forum]
- "Inter-Agency Space Debris Coordination Committee." n.d. Accessed October 25, 2026. [https://www.iadc-home.org/][ref_iadc_guidelines]
- Jensen. 1986. "Agency Costs of Free Cash Flow Corporate Finance and Takeovers." [https://www.jstor.org/stable/1818789][research_jensen_1986]
- "Journal of Space Law." n.d. Center for Air and Space Law. Accessed October 25, 2026. [https://airandspacelaw.olemiss.edu/journal-of-space-law/][ref_journal_space_law]
- "Journal of Space Safety Engineering." n.d. Accessed October 25, 2026. [https://www.sciencedirect.com/journal/journal-of-space-safety-engineering][ref_jsse_journal]
- Khan. 2017. "Amazon’s Antitrust Paradox." *Yale Law Journal*, January 31. [https://www.yalelawjournal.org/note/amazons-antitrust-paradox][research_khan_2017]
- Klepper. 1996. "Entry Exit Growth and Innovation over the Product Life Cycle." [https://www.jstor.org/stable/2118211][research_klepper_1996]
- Law. 1987. "Technology and Heterogeneous Engineering." [https://mitpress.mit.edu/9780262521376/the-social-construction-of-technological-systems/][research_law_1987]
- "NASASpaceflight Coverage." n.d. Accessed October 25, 2026. [https://www.nasaspaceflight.com/][ref_nasaspaceflight]
- "National Bureau of Economic Research." n.d. NBER. Accessed October 25, 2026. [https://www.nber.org/][ref_nber]
- "New York Times." n.d. Accessed October 25, 2026. [https://www.nytimes.com/section/science/space][ref_nyt]
- New York Times. 2024. "Starshield Coverage." [https://www.nytimes.com/2024/02/16/us/politics/spacex-us-spy-agency-satellites.html][ref_nyt_starshield_2024]
- "Payload Newsletter." n.d. Accessed October 25, 2026. [https://payloadspace.com/][ref_payload]
- "Research Newsletter." n.d. *Payload*. Accessed October 25, 2026. [https://payloadspace.com/research/][ref_payload_research]
- Reuters. 2024. "Starshield Investigation." [https://www.reuters.com/technology/space/musks-spacex-is-building-spy-satellite-network-us-intelligence-agency-sources-2024-03-16/][research_reuters_starshield_2024]
- Simon. 1962. "The Architecture of Complexity." [https://www.jstor.org/stable/985254][research_simon_1962]
- "Social Science Research Network." n.d. Accessed October 25, 2026. [https://www.ssrn.com/][ref_ssrn]
- "Space Policy Journal." n.d. Accessed October 25, 2026. [https://www.sciencedirect.com/journal/space-policy][ref_space_policy_journal]
- "Space Policy Online." n.d. Accessed October 25, 2026. [https://spacepolicyonline.com/][ref_space_policy_online]
- "The Space Review: Essays and Commentary about the Final Frontier." n.d. Accessed October 25, 2026. [https://www.thespacereview.com/][ref_the_space_review]
- "SpaceNews." n.d. Accessed October 25, 2026. [https://spacenews.com/][ref_spacenews]
- "SpaceNews National Security Space Launch Phase 3 Coverage." n.d. Accessed October 25, 2026. [https://spacenews.com/?s=NSSL+Phase+3][ref_spacenews_nssl_phase3]
- "Stanford Graduate School of Business SpaceX Case." n.d. Accessed October 25, 2026. [https://www.gsb.stanford.edu/faculty-research/case-studies][ref_stanford_spacex_case]
- "Wall Street Journal." n.d. Accessed October 25, 2026. [https://www.wsj.com/tech][ref_wsj]
- "Washington Post Technology Coverage." n.d. Accessed October 25, 2026. [https://www.washingtonpost.com/business/technology/][ref_washington_post]
- "Wharton SpaceX Case." n.d. Accessed October 25, 2026. [https://knowledge.wharton.upenn.edu/][ref_wharton_spacex_case]
- Williamson. 1975. "Markets and Hierarchies." [https://www.jstor.org/stable/40751236][research_williamson_1975]
- Zimmerman. 2011. "Economics of Satellite Communications." [https://openlibrary.org/search?q=Zimmerman+Economics+Satellite+Communications][research_zimmerman_2011]

### Related Posts

- Sechter, Brendan. 2026. "Introduction to Space Studies." *Brendan A R Sechter's Development Blog*, February 21. [https://sgeos.github.io/space/math/2026/02/21/introduction\_to\_space\_studies.html][related_post_a90_intro_space_studies]
- Sechter, Brendan. 2026. "History of Rocketplanes." *Brendan A R Sechter's Development Blog*, February 27. [https://sgeos.github.io/space/history/2026/02/27/history\_of\_rocketplanes.html][related_post_a96_history_rocketplanes]
- Sechter, Brendan. 2026. "What Does the United States Space Force Do?" *Brendan A R Sechter's Development Blog*, February 28. [https://sgeos.github.io/space/military/2026/02/28/what\_does\_united\_states\_space\_force\_do.html][related_post_a97_us_space_force]
- Sechter, Brendan. 2026. "Why Startups Actually Fail." *Brendan A R Sechter's Development Blog*, May 9. [https://sgeos.github.io/business/strategy/startups/2026/05/09/why\_startups\_actually\_fail.html][related_post_a167_startup_failure]
- Sechter, Brendan. 2026. "Aerospace, Programming Languages, and Information Technology Co-Development: Framing and the Co-Development Mechanism." *Brendan A R Sechter's Development Blog*, July 13. [https://sgeos.github.io/history/technology/aerospace/2026/07/13/framing\_and\_the\_co\_development\_mechanism.html][related_post_a237_aerospace_framing]
- Sechter, Brendan. 2026. "Aerospace, Programming Languages, and Information Technology Co-Development: Silicon Valley from Defense Contracting." *Brendan A R Sechter's Development Blog*, July 22. [https://sgeos.github.io/history/technology/aerospace/2026/07/22/silicon\_valley\_from\_defense\_contracting.html][related_post_a246_silicon_valley_defense]
- Sechter, Brendan. 2026. "Aerospace, Programming Languages, and Information Technology Co-Development: Software-Defined Aerospace and Autonomy." *Brendan A R Sechter's Development Blog*, July 23. [https://sgeos.github.io/history/technology/aerospace/2026/07/23/software\_defined\_aerospace\_and\_autonomy.html][related_post_a247_software_defined_aerospace]
- Sechter, Brendan. 2026. "Aerospace, Programming Languages, and Information Technology Co-Development: Contemporary Snapshot and Extrapolation." *Brendan A R Sechter's Development Blog*, July 24. [https://sgeos.github.io/history/technology/aerospace/2026/07/24/contemporary\_snapshot\_and\_extrapolation.html][related_post_a248_contemporary_snapshot]
- Sechter, Brendan. 2026. "History of SpaceX: Series Framing and the Seven-Plus-Three Forcing-Function Framework." *Brendan A R Sechter's Development Blog*, July 25. [https://sgeos.github.io/history/business/aerospace/2026/07/25/spacex\_history\_framing.html][related_post_a281_spacex_framing]
- Sechter, Brendan. 2026. "History of SpaceX: Value Gradient from Falcon 1 to Falcon 9 to Reusability." *Brendan A R Sechter's Development Blog*, July 26. [https://sgeos.github.io/history/business/aerospace/2026/07/26/spacex\_history\_value\_gradient.html][related_post_a282_spacex_value_gradient]
- Sechter, Brendan. 2026. "History of SpaceX: Anchor Demand from COTS-1 Salvation Through Commercial Crew, HLS, and Starshield." *Brendan A R Sechter's Development Blog*, July 27. [https://sgeos.github.io/history/business/aerospace/2026/07/27/spacex\_history\_anchor\_demand.html][related_post_a283_spacex_anchor_demand]
- Sechter, Brendan. 2026. "History of SpaceX: Value Capture from Launch-Service Pricing and Vertical Integration into Starlink." *Brendan A R Sechter's Development Blog*, July 28. [https://sgeos.github.io/history/business/aerospace/2026/07/28/spacex\_history\_value\_capture.html][related_post_a284_spacex_value_capture]
- Sechter, Brendan. 2026. "History of SpaceX: Decomposability of Falcon, Dragon, Heavy, and Starship as Independently Valuable Rungs." *Brendan A R Sechter's Development Blog*, July 29. [https://sgeos.github.io/history/business/aerospace/2026/07/29/spacex\_history\_decomposability.html][related_post_a285_spacex_decomposability]
- Sechter, Brendan. 2026. "History of SpaceX: Generality-Forcing from Mars Requirements as a Cross-Domain Capability Substrate." *Brendan A R Sechter's Development Blog*, July 30. [https://sgeos.github.io/history/business/aerospace/2026/07/30/spacex\_history\_generality\_forcing.html][related_post_a286_spacex_generality_forcing]
- Sechter, Brendan. 2026. "History of SpaceX: Governance That Resists Capital Capture Across Thirty-Plus Funding Rounds." *Brendan A R Sechter's Development Blog*, July 31. [https://sgeos.github.io/history/business/aerospace/2026/07/31/spacex\_history\_governance.html][related_post_a287_spacex_governance]

[book_adner_2012]: https://openlibrary.org/works/OL16191407W
[book_adner_2021]: https://mitpress.mit.edu/9780262046114/winning-the-right-game/
[book_anderson_2023]: https://www.wiley.com/en-us/The+Space+Economy-p-9781119911562
[book_argote_1999]: https://openlibrary.org/works/OL2002798W
[book_argyris_schon_1978]: https://www.pearson.com/en-us/subject-catalog/p/organizational-learning-a-theory-of-action-perspective/P200000005949
[book_baldwin_clark_2000]: https://mitpress.mit.edu/9780262024662/design-rules/
[book_beinhocker_2006]: https://www.hbsp.harvard.edu/product/5062-HBK-ENG
[book_berger_2021]: https://www.harpercollins.com/products/liftoff-eric-berger
[book_berger_2024]: https://openlibrary.org/works/OL37529642W
[book_berle_means_1932]: https://www.routledge.com/The-Modern-Corporation-and-Private-Property/Berle-Means/p/book/9780887388873
[book_bird_sherwin_2005]: https://openlibrary.org/works/OL1905682W
[book_bork_1978]: https://www.hup.harvard.edu/books/9780674032545
[book_chandler_1962]: https://mitpress.mit.edu/9780262530095/strategy-and-structure/
[book_chandler_1977]: https://www.hup.harvard.edu/books/9780674940529
[book_chandler_1990]: https://openlibrary.org/works/OL11391139W
[book_chernow_2004]: https://openlibrary.org/search?q=Chernow+Titan
[book_concina_2006]: https://www.cambridge.org/9780521187459
[book_copeland_antikarov_2001]: https://openlibrary.org/search?q=Copeland+and+Antikarov+Real+Options+A+Practitioners+Guide
[book_creswell_2014]: https://us.sagepub.com/en-us/nam/research-design/book255675
[book_cusumano_2010]: https://global.oup.com/academic/product/staying-power-9780199678501
[book_cusumano_gawer_2002]: https://www.hbsp.harvard.edu/product/6155-HBK-ENG
[book_cyert_march_1963]: https://openlibrary.org/works/OL2859173W
[book_davenport_2018]: https://www.hachettebookgroup.com/titles/christian-davenport/the-space-barons/9781610398299/
[book_dixit_pindyck_1994]: https://openlibrary.org/works/OL2979477W
[book_easterbrook_fischel_1991]: https://www.hup.harvard.edu/books/9780674235397
[book_fernholz_2018]: https://www.hachettebookgroup.com/titles/tim-fernholz/rocket-billionaires/9781328662231/
[book_fine_1998]: https://www.hachettebookgroup.com/titles/charles-h-fine/clockspeed/9780738201535/
[book_fligstein_2001]: https://press.princeton.edu/books/paperback/9780691102542/the-architecture-of-markets
[book_ford_crowther_1922]: https://openlibrary.org/works/OL4418043W
[book_foster_mcchesney_2011]: https://monthlyreview.org/product/endless_crisis/
[book_freeman_1987]: https://openlibrary.org/works/OL2642736W
[book_gertner_2012]: https://www.penguinrandomhouse.com/books/206061/the-idea-factory-by-jon-gertner/
[book_gompers_lerner_2001]: https://www.hbsp.harvard.edu/product/2434-HBK-ENG
[book_groves_1962]: https://openlibrary.org/works/OL5912728W
[book_handberg_1994]: https://openlibrary.org/search?q=Handberg+Reinventing+NASA
[book_hart_1995]: https://global.oup.com/academic/product/firms-contracts-and-financial-structure-9780198288817
[book_hartley_2017]: https://openlibrary.org/search?q=Hartley+The+Economics+of+Arms
[book_hewlett_anderson_1962]: https://openlibrary.org/works/OL12854869W
[book_horwitch_1982]: https://mitpress.mit.edu/9780262580620/clipped-wings/
[book_hovenkamp_2005]: https://openlibrary.org/works/OL3464674W
[book_hunter_2016]: https://csis-website-prod.s3.amazonaws.com/s3fs-public/legacy_files/files/publication/160930_Hunter_CreatingStrategicValue_Web.pdf
[book_iansiti_levien_2004]: https://www.hbsp.harvard.edu/product/3921-HBK-ENG
[book_isaacson_2023]: https://www.simonandschuster.com/books/Elon-Musk/Walter-Isaacson/9781982181284
[book_kahn_1988]: https://mitpress.mit.edu/9780262610520/the-economics-of-regulation/
[book_kahneman_2011]: https://us.macmillan.com/books/9780374533557/thinkingfastandslow
[book_kauffman_1993]: https://global.oup.com/academic/product/the-origins-of-order-9780195079517
[book_klerkx_2004]: https://us.macmillan.com/books/9780375421501/lostinspace
[book_lane_1934]: https://jhupbooks.press.jhu.edu/title/venetian-ships-and-shipbuilders-renaissance
[book_latour_1987]: https://www.hup.harvard.edu/books/9780674792913
[book_lawrence_2016]: https://www.routledge.com/Airbus-vs-Boeing/Lawrence/p/book/9781138287884
[book_lerner_2009]: https://press.princeton.edu/books/hardcover/9780691142197/boulevard-of-broken-dreams
[book_levin_2010]: https://openlibrary.org/search?q=Levin+Wires+That+Bind
[book_liker_2004]: https://www.mheducation.com/highered/product/toyota-way-liker/M9780071392310.html
[book_lundvall_1992]: https://openlibrary.org/works/OL9010144W
[book_march_simon_1958]: https://www.wiley.com/en-us/Organizations%2C+2nd+Edition-p-9780631186311
[book_markowitz_1959]: https://yalebooks.yale.edu/book/9780300013726/portfolio-selection/
[book_mazzucato_2013]: https://marianamazzucato.com/books/the-entrepreneurial-state
[book_mazzucato_2021]: https://marianamazzucato.com/books/mission-economy/
[book_melman_1970]: https://openlibrary.org/works/OL1299274W
[book_metcalfe_1998]: https://www.routledge.com/Evolutionary-Economics-and-Creative-Destruction/Metcalfe/p/book/9780415158671
[book_metrick_yasuda_2011]: https://openlibrary.org/works/OL3690888W
[book_meyer_lehnerd_1997]: https://www.simonandschuster.com/books/The-Power-of-Product-Platforms/Marc-H-Meyer/9780684825809
[book_miller_1995]: https://openlibrary.org/works/OL7006663W
[book_mowery_rosenberg_1998]: https://openlibrary.org/works/OL21370782W
[book_musa_1998]: https://openlibrary.org/works/OL4781285W
[book_nelson_1993]: https://global.oup.com/academic/product/national-innovation-systems-9780195076172
[book_nelson_winter_1982]: https://www.hup.harvard.edu/books/9780674272286
[book_nevins_1954]: https://openlibrary.org/search?q=Nevins+Ford+The+Times+The+Man+The+Company
[book_newhouse_1982]: https://openlibrary.org/works/OL2625941W
[book_newhouse_2007]: https://us.macmillan.com/books/9781400079131/boeingversusairbus
[book_nonaka_takeuchi_1995]: https://global.oup.com/academic/product/the-knowledge-creating-company-9780195092691
[book_oconnor_kleyner_2012]: https://openlibrary.org/works/OL3744715W
[book_ohno_1988]: https://openlibrary.org/works/OL8681881W
[book_ormerod_2005]: https://us.macmillan.com/books/9780375421099/whymostthingsfail
[book_owen_1997]: https://openlibrary.org/search?q=Owen+Concorde+Story+of+a+Supersonic+Pioneer
[book_owen_2001]: https://openlibrary.org/works/OL3341689W
[book_penrose_1959]: https://global.oup.com/academic/product/the-theory-of-the-growth-of-the-firm-9780199573844
[book_perez_2002]: https://openlibrary.org/works/OL224128W
[book_perrow_1984]: https://press.princeton.edu/books/paperback/9780691004129/normal-accidents
[book_porter_1980]: https://www.simonandschuster.com/books/Competitive-Strategy/Michael-E-Porter/9780684841489
[book_porter_1985]: https://www.simonandschuster.com/books/Competitive-Advantage/Michael-E-Porter/9780684841465
[book_posner_2001]: https://openlibrary.org/works/OL1924317W
[book_pugh_1995]: https://mitpress.mit.edu/9780262161473/building-ibm/
[book_pugh_johnson_palmer_1991]: https://mitpress.mit.edu/9780262161237/ibms-360-and-early-370-systems/
[book_rhodes_1986]: https://www.simonandschuster.com/books/The-Making-of-the-Atomic-Bomb/Richard-Rhodes/9781451677614
[book_rich_janos_1994]: https://www.hachettebookgroup.com/titles/ben-r-rich/skunk-works/9780316743006/
[book_robins_2006]: https://openlibrary.org/works/OL2083415W
[book_roe_1994]: https://press.princeton.edu/books/paperback/9780691026312/strong-managers-weak-owners
[book_rogers_1962]: https://www.simonandschuster.com/books/Diffusion-of-Innovations-5th-Edition/Everett-M-Rogers/9780743258234
[book_ruttan_2006]: https://global.oup.com/academic/product/is-war-necessary-for-economic-growth-9780195188042
[book_sanderson_uzumeri_1997]: https://openlibrary.org/works/OL33995941W
[book_schumpeter_1942]: https://www.harpercollins.com/products/capitalism-socialism-and-democracy-joseph-a-schumpeter
[book_senge_1990]: https://www.penguinrandomhouse.com/books/163984/the-fifth-discipline-by-peter-m-senge/
[book_serling_1992]: https://openlibrary.org/works/OL2769360W
[book_sharkey_1982]: https://www.cambridge.org/9780521271943
[book_shingo_1989]: https://openlibrary.org/works/OL4111563W
[book_simon_1957]: https://www.simonandschuster.com/books/Administrative-Behavior-4th-Edition/Herbert-A-Simon/9781439136218
[book_srnicek_2017]: https://www.wiley.com/en-us/Platform+Capitalism-p-9781509504879
[book_steensgaard_1974]: https://openlibrary.org/works/OL7009029W
[book_stern_2011]: https://global.oup.com/academic/product/the-company-state-9780195393736
[book_temin_galambos_1987]: https://openlibrary.org/works/OL4797079W
[book_tirole_2006]: https://press.princeton.edu/books/hardcover/9780691125565/the-theory-of-corporate-finance
[book_trigeorgis_1996]: https://mitpress.mit.edu/9780262201025/real-options/
[book_trubshaw_2000]: https://openlibrary.org/search?q=Trubshaw+Concorde+Inside+Story
[book_utterback_1994]: https://www.hbsp.harvard.edu/product/4855-HBK-ENG
[book_vance_2015]: https://www.harpercollins.com/products/elon-musk-ashlee-vance
[book_vaughan_1996]: https://press.uchicago.edu/ucp/books/book/chicago/C/bo22781921.html
[book_weick_1979]: https://www.mheducation.com/highered/product/social-psychology-organizing-weick/M9780075548089.html
[book_weick_sutcliffe_2007]: https://openlibrary.org/works/OL3749104W
[book_weiss_2014]: https://www.cornellpress.cornell.edu/book/9780801479922/america-inc/
[book_williamson_1985]: https://www.simonandschuster.com/books/The-Economic-Institutions-of-Capitalism/Oliver-E-Williamson/9780684863740
[book_womack_jones_2003]: https://www.simonandschuster.com/books/Lean-Thinking/James-P-Womack/9780743249270
[book_womack_jones_roos_1990]: https://www.simonandschuster.com/books/The-Machine-That-Changed-the-World/James-P-Womack/9780743299794
[book_wu_2010]: https://openlibrary.org/works/OL15118227W
[book_yin_2014]: https://us.sagepub.com/en-us/nam/case-study-research-and-applications/book250150
[book_zuboff_2019]: https://www.hachettebookgroup.com/titles/shoshana-zuboff/the-age-of-surveillance-capitalism/9781610395694/
[ref_aiaa_jsr]: https://arc.aiaa.org/journal/jsr
[ref_aon_space_insurance]: https://www.aon.com/
[ref_arianespace]: https://www.arianespace.com/
[ref_arstechnica_space]: https://arstechnica.com/science/space/
[ref_aviation_week]: https://aviationweek.com/
[ref_bankruptcy_code_ch11]: https://www.law.cornell.edu/uscode/text/11/chapter-11
[ref_bloomberg]: https://www.bloomberg.com/
[ref_blue_origin_press]: https://www.blueorigin.com/news/
[ref_boeing_historical_archives]: https://www.boeing.com/history/
[ref_boeing_press]: https://boeing.mediaroom.com/
[ref_breaking_defense]: https://breakingdefense.com/
[ref_bryce_tech]: https://brycetech.com/reports
[ref_china_commercial_space]: https://spacenews.com/topic/china/
[ref_chinese_space_program]: https://www.cnsa.gov.cn/english/
[ref_columbia_blue_sky]: https://clsbluesky.law.columbia.edu/
[ref_congressional_record]: https://www.congress.gov/congressional-record
[ref_crs_commercial_crew]: https://crsreports.congress.gov/product/pdf/R/R44708
[ref_defense_news]: https://www.defensenews.com/
[ref_dod_contracts]: https://www.defense.gov/News/Contracts/
[ref_doe_office_of_science]: https://science.osti.gov/
[ref_ecgi]: https://www.ecgi.global/
[ref_european_spaceflight]: https://europeanspaceflight.com/
[ref_eutelsat_oneweb]: https://www.eutelsat.com/
[ref_faa_ast]: https://www.faa.gov/space
[ref_faa_ast_licensing_regs_450]: https://www.ecfr.gov/current/title-14/chapter-III/subchapter-C/part-450
[ref_faa_financial_responsibility]: https://www.ecfr.gov/current/title-14/part-440
[ref_faa_starship_ea]: https://www.faa.gov/space/stakeholder_engagement/spacex_starship
[ref_fasb_asc280]: https://www.fasb.org/
[ref_fcc_direct_to_cell_2024]: https://docs.fcc.gov/public/attachments/DA-24-208A1.pdf
[ref_fcc_filings]: https://www.fcc.gov/wireless/systems-utilities/electronic-comment-filing-system-ecfs
[ref_fcc_starlink_2018]: https://docs.fcc.gov/public/attachments/FCC-18-38A1.pdf
[ref_fcc_starlink_gen2_2022]: https://docs.fcc.gov/public/attachments/FCC-22-91A1.pdf
[ref_gao_ccp_2019]: https://www.gao.gov/products/gao-19-504
[ref_gao_hls_2022]: https://www.gao.gov/products/gao-22-105506
[ref_gao_nssl_2023]: https://www.gao.gov/products/gao-23-105815
[ref_gao_reports]: https://www.gao.gov/reports-testimonies
[ref_harvard_corpgov_forum]: https://corpgov.law.harvard.edu/
[ref_house_science_committee_hearings]: https://science.house.gov/
[ref_iadc_guidelines]: https://www.iadc-home.org/
[ref_ibm_archives]: https://www.ibm.com/history/
[ref_iridium_chapter_11_1999]: https://www.sec.gov/Archives/edgar/data/1029074/0000912057-99-034228.txt
[ref_iridium_press_archive_1998]: https://www.iridium.com/
[ref_isro_press]: https://www.isro.gov.in/
[ref_itu_radio_regulations_2020]: https://www.itu.int/pub/R-REG-RR
[ref_jaxa_press]: https://global.jaxa.jp/press/
[ref_journal_space_law]: https://airandspacelaw.olemiss.edu/journal-of-space-law/
[ref_jsse_journal]: https://www.sciencedirect.com/journal/journal-of-space-safety-engineering
[ref_lloyds_market]: https://www.lloyds.com/
[ref_nasa_ccp_documents]: https://www.nasa.gov/commercialcrew/
[ref_nasa_crs2_press_2016]: https://www.nasa.gov/news-release/nasa-awards-international-space-station-cargo-transport-contracts/
[ref_nasa_crs_program_overview]: https://www.nasa.gov/commercial-resupply/
[ref_nasa_hls_option_a_2021]: https://www.nasa.gov/humans-in-space/artemis/
[ref_nasa_hls_option_b_2022]: https://www.nasa.gov/mission/artemis-iii/
[ref_nasa_hls_program]: https://www.nasa.gov/humans-in-space/human-landing-system/
[ref_nasa_news]: https://www.nasa.gov/news/
[ref_nasa_oig_ccp_2019]: https://oig.nasa.gov/audits/?_search=Commercial+Crew
[ref_nasa_oig_ccp_cargo_2018]: https://oig.nasa.gov/docs/IG-18-016.pdf
[ref_nasa_oig_hls_2021]: https://oig.nasa.gov/docs/IG-21-024.pdf
[ref_nasa_orbital_debris]: https://orbitaldebris.jsc.nasa.gov/
[ref_nasaspaceflight]: https://www.nasaspaceflight.com/
[ref_nber]: https://www.nber.org/
[ref_northrop_grumman_press]: https://news.northropgrumman.com/
[ref_nyt]: https://www.nytimes.com/section/science/space
[ref_nyt_starshield_2024]: https://www.nytimes.com/2024/02/16/us/politics/spacex-us-spy-agency-satellites.html
[ref_oneweb]: https://oneweb.net/
[ref_payload]: https://payloadspace.com/
[ref_payload_research]: https://payloadspace.com/research/
[ref_rocket_lab_press]: https://www.rocketlabusa.com/updates/
[ref_sec_edgar]: https://www.sec.gov/edgar/searchedgar/companysearch
[ref_sec_form_d]: https://www.sec.gov/answers/formd.htm
[ref_sec_regulation_sk]: https://www.ecfr.gov/current/title-17/part-229
[ref_space_capital]: https://www.spacecapital.com/
[ref_space_force_news]: https://www.spaceforce.mil/News/
[ref_space_force_nssl]: https://www.spaceforce.mil/News/Fact-Sheets
[ref_space_force_nssl_phase1a_2018]: https://www.af.mil/News/Article-Display/Article/1671253/
[ref_space_force_nssl_phase2_2020]: https://www.spaceforce.mil/News/Article/2312953/
[ref_space_policy_journal]: https://www.sciencedirect.com/journal/space-policy
[ref_space_policy_online]: https://spacepolicyonline.com/
[ref_spacenews]: https://spacenews.com/
[ref_spacenews_nssl_phase3]: https://spacenews.com/?s=NSSL+Phase+3
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
[ref_spacex_seattle_announcement_2015]: https://www.spacex.com/updates/
[ref_spacex_starlink]: https://www.starlink.com/
[ref_spacex_starlink_direct_to_cell_tmobile_2022]: https://www.starlink.com/business/direct-to-cell
[ref_spacex_starshield]: https://www.spacex.com/starshield/
[ref_spacex_starship_vehicle]: https://www.spacex.com/vehicles/starship/
[ref_ssrn]: https://www.ssrn.com/
[ref_stanford_spacex_case]: https://www.gsb.stanford.edu/faculty-research/case-studies
[ref_the_space_review]: https://www.thespacereview.com/
[ref_ula_press]: https://www.ulalaunch.com/about/news
[ref_un_liability_convention_1972]: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/liability-convention.html
[ref_un_outer_space_treaty_1967]: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/outerspacetreaty.html
[ref_un_registration_convention_1976]: https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/registration-convention.html
[ref_uscourts_bankruptcy]: https://www.uscourts.gov/court-programs/bankruptcy
[ref_virgin_orbit_court]: https://www.deb.uscourts.gov/
[ref_washington_post]: https://www.washingtonpost.com/business/technology/
[ref_wharton_spacex_case]: https://knowledge.wharton.upenn.edu/
[ref_wsj]: https://www.wsj.com/tech
[related_post_a167_startup_failure]: {% post_url 2026-05-09-why_startups_actually_fail %}
[related_post_a237_aerospace_framing]: {% post_url 2026-07-13-framing_and_the_co_development_mechanism %}
[related_post_a246_silicon_valley_defense]: {% post_url 2026-07-22-silicon_valley_from_defense_contracting %}
[related_post_a247_software_defined_aerospace]: {% post_url 2026-07-23-software_defined_aerospace_and_autonomy %}
[related_post_a248_contemporary_snapshot]: {% post_url 2026-07-24-contemporary_snapshot_and_extrapolation %}
[related_post_a281_spacex_framing]: {% post_url 2026-07-25-spacex_history_framing %}
[related_post_a282_spacex_value_gradient]: {% post_url 2026-07-26-spacex_history_value_gradient %}
[related_post_a283_spacex_anchor_demand]: {% post_url 2026-07-27-spacex_history_anchor_demand %}
[related_post_a284_spacex_value_capture]: {% post_url 2026-07-28-spacex_history_value_capture %}
[related_post_a285_spacex_decomposability]: {% post_url 2026-07-29-spacex_history_decomposability %}
[related_post_a286_spacex_generality_forcing]: {% post_url 2026-07-30-spacex_history_generality_forcing %}
[related_post_a287_spacex_governance]: {% post_url 2026-07-31-spacex_history_governance %}
[related_post_a90_intro_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[related_post_a96_history_rocketplanes]: {% post_url 2026-02-27-history_of_rocketplanes %}
[related_post_a97_us_space_force]: {% post_url 2026-02-28-what_does_united_states_space_force_do %}
[research_abernathy_clark_1985]: https://doi.org/10.1016/0048-7333(85)90021-6
[research_adilov_et_al_2018]: https://www.sciencedirect.com/science/article/abs/pii/S0921800917305591
[research_adler_clark_1991]: https://doi.org/10.1287/mnsc.37.3.267
[research_adner_kapoor_2010]: https://doi.org/10.1002/smj.821
[research_alchian_1963]: https://doi.org/10.2307/1909166
[research_amihud_lev_1981]: https://doi.org/10.2307/3003575
[research_anadol_cohen_2018]: https://www.hbs.edu/faculty/Pages/item.aspx?num=54001
[research_anderson_tushman_1990]: https://doi.org/10.2307/2393511
[research_argote_epple_1990]: https://doi.org/10.1126/science.247.4945.920
[research_argote_ingram_2000]: https://doi.org/10.1006/obhd.2000.2893
[research_argote_miron_spektor_2011]: https://doi.org/10.1287/orsc.1100.0621
[research_baldwin_woodard_2009]: https://doi.org/10.4337/9781849803311.00008
[research_barney_1991]: https://doi.org/10.1177/014920639101700108
[research_bebchuk_kastiel_2017]: https://doi.org/10.2139/ssrn.2954630
[research_bebchuk_kraakman_triantis_2000]: https://doi.org/10.3386/w6951
[research_berger_ofek_1995]: https://doi.org/10.1016/0304-405x(94)00798-6
[research_black_scholes_1973]: https://doi.org/10.1086/260062
[research_bonvillian_2018]: https://mitpress.mit.edu/9780262038522/the-darpa-model-for-transformative-technologies/
[research_callon_1986]: https://doi.org/10.1111/j.1467-954x.1984.tb00113.x
[research_coase_1937]: https://doi.org/10.1111/j.1468-0335.1937.tb00002.x
[research_cohen_levinthal_1990]: https://doi.org/10.2307/2393553
[research_deangelo_deangelo_1985]: https://doi.org/10.1016/0304-405x(85)90043-1
[research_duane_1964]: https://doi.org/10.1109/ta.1964.4319640
[research_dutton_thomas_1984]: https://doi.org/10.2307/258437
[research_eisenhardt_martin_2000]: https://doi.org/10.1002/1097-0266(200010/11)21:10/11<1105::aid-smj133>3.0.co;2-e
[research_ethiraj_levinthal_2004]: https://doi.org/10.1287/mnsc.1030.0145
[research_fama_jensen_1983]: https://doi.org/10.1086/467037
[research_finkelstein_sanford_2000]: https://doi.org/10.1016/s0090-2616(00)00020-6
[research_fixson_2005]: https://doi.org/10.1016/j.jom.2004.08.006
[research_gawer_cusumano_2014]: https://doi.org/10.1111/jpim.12105
[research_gertner_scharfstein_stein_1994]: https://doi.org/10.3386/w4776
[research_gompers_1995]: https://doi.org/10.1111/j.1540-6261.1995.tb05185.x
[research_gompers_ishii_metrick_2003]: https://doi.org/10.1162/00335530360535162
[research_gompers_ishii_metrick_2010]: https://doi.org/10.1093/rfs/hhp024
[research_grant_1996]: https://doi.org/10.1002/smj.4250171110
[research_grossman_hart_1986]: https://doi.org/10.1086/261404
[research_grossman_hart_1988]: https://doi.org/10.3386/w2347
[research_harris_raviv_1988]: https://www.sciencedirect.com/science/article/abs/pii/0304405X88900455
[research_hart_moore_1990]: https://doi.org/10.1086/261729
[research_helfat_peteraf_2003]: https://doi.org/10.1002/smj.332
[research_hertzfeld_2002]: https://doi.org/10.1023/a:1020207506064
[research_huber_1991]: https://doi.org/10.1287/orsc.2.1.88
[research_jacobides_et_al_2018]: https://doi.org/10.1002/smj.2904
[research_jensen_1986]: https://www.jstor.org/stable/1818789
[research_jensen_meckling_1976]: https://doi.org/10.1016/0304-405x(76)90026-x
[research_kahneman_tversky_1979]: https://doi.org/10.2307/1914185
[research_kaplan_stromberg_2003]: https://doi.org/10.1111/1467-937x.00245
[research_kaplan_stromberg_2004]: https://doi.org/10.1111/j.1540-6261.2004.00696.x
[research_kessler_courpalais_1978]: https://doi.org/10.1029/ja083ia06p02637
[research_khan_2017]: https://www.yalelawjournal.org/note/amazons-antitrust-paradox
[research_klein_crawford_alchian_1978]: https://doi.org/10.1086/466922
[research_klepper_1996]: https://www.jstor.org/stable/2118211
[research_klepper_2010]: https://doi.org/10.1016/j.jue.2009.09.004
[research_kogut_kulatilaka_1994]: https://doi.org/10.1287/mnsc.40.1.123
[research_kogut_zander_1992]: https://doi.org/10.1287/orsc.3.3.383
[research_lafontaine_slade_2007]: https://doi.org/10.1257/jel.45.3.629
[research_lane_koka_pathak_2006]: https://doi.org/10.5465/amr.2006.22527456
[research_lang_stulz_1994]: https://doi.org/10.1086/261970
[research_laporta_et_al_1998]: https://doi.org/10.1086/250042
[research_law_1987]: https://mitpress.mit.edu/9780262521376/the-social-construction-of-technological-systems/
[research_lerner_1994_syndication]: https://doi.org/10.2307/3665618
[research_levitt_march_1988]: https://doi.org/10.1146/annurev.so.14.080188.001535
[research_lewellen_1971]: https://doi.org/10.1111/j.1540-6261.1971.tb00912.x
[research_lieberman_1984]: https://doi.org/10.2307/2555676
[research_lintner_1965]: https://doi.org/10.2307/1924119
[research_maccormack_baldwin_rusnak_2012]: https://doi.org/10.1016/j.respol.2012.04.011
[research_march_1991]: https://doi.org/10.1287/orsc.2.1.71
[research_markowitz_1952]: https://doi.org/10.2307/2975974
[research_mcdonald_siegel_1986]: https://doi.org/10.2307/1884175
[research_merton_1973]: https://doi.org/10.2307/3003143
[research_monteverde_teece_1982]: https://doi.org/10.2307/3003441
[research_montgomery_1994]: https://doi.org/10.1257/jep.8.3.163
[research_murmann_frenken_2006]: https://doi.org/10.1016/j.respol.2006.04.011
[research_myers_1977]: https://doi.org/10.1016/0304-405x(77)90015-0
[research_nonaka_1994]: https://doi.org/10.1287/orsc.5.1.14
[research_novak_eppinger_2001]: https://doi.org/10.1287/mnsc.47.1.189.10662
[research_peeters_2018]: https://doi.org/10.1089/space.2017.0039
[research_peteraf_1993]: https://doi.org/10.1002/smj.4250140303
[research_rajan_servaes_zingales_2000]: https://doi.org/10.1111/0022-1082.00200
[research_rapping_1965]: https://doi.org/10.2307/1924126
[research_reuters_starshield_2024]: https://www.reuters.com/technology/space/musks-spacex-is-building-spy-satellite-network-us-intelligence-agency-sources-2024-03-16/
[research_rivkin_siggelkow_2003]: https://doi.org/10.1287/mnsc.49.3.290.12740
[research_robertson_ulrich_1998]: https://sloanreview.mit.edu/article/planning-for-product-platforms/
[research_ross_staw_1993]: https://doi.org/10.2307/256756
[research_sahlman_1990]: https://doi.org/10.1016/0304-405x(90)90065-8
[research_sanchez_mahoney_1996]: https://doi.org/10.1002/smj.4250171107
[research_scharfstein_stein_2000]: https://doi.org/10.1111/0022-1082.00299
[research_sharpe_1964]: https://doi.org/10.1111/j.1540-6261.1964.tb02865.x
[research_shleifer_vishny_1997]: https://doi.org/10.1111/j.1540-6261.1997.tb04820.x
[research_simon_1962]: https://www.jstor.org/stable/985254
[research_sosa_eppinger_rowles_2003]: https://doi.org/10.1115/1.1564074
[research_staw_1976]: https://doi.org/10.1016/0030-5073(76)90005-2
[research_stein_1997]: https://doi.org/10.1111/j.1540-6261.1997.tb03810.x
[research_suarez_utterback_1995]: https://doi.org/10.1002/smj.4250160602
[research_teece_2007]: https://doi.org/10.1002/smj.640
[research_teece_pisano_shuen_1997]: https://doi.org/10.1002/(sici)1097-0266(199708)18:7<509::aid-smj882>3.0.co;2-z
[research_todorova_durisin_2007]: https://doi.org/10.5465/amr.2007.25275513
[research_tversky_kahneman_1992]: https://doi.org/10.1007/bf00122574
[research_ulrich_1995]: https://doi.org/10.1016/0048-7333(94)00775-3
[research_villalonga_2004]: https://doi.org/10.2139/ssrn.227828
[research_volberda_foss_lyles_2010]: https://doi.org/10.1287/orsc.1090.0503
[research_walker_et_al_2020]: https://noirlab.edu/public/products/techdocs/techdoc003/
[research_weeden_chow_2012]: https://doi.org/10.1016/j.spacepol.2012.06.004
[research_weinzierl_2018]: https://doi.org/10.1257/jep.32.2.173
[research_wernerfelt_1984]: https://doi.org/10.1002/smj.4250050207
[research_williamson_1975]: https://www.jstor.org/stable/40751236
[research_winter_2003]: https://doi.org/10.1002/smj.318
[research_wright_1936]: https://doi.org/10.2514/8.155
[research_zahra_george_2002]: https://doi.org/10.5465/amr.2002.6587995
[research_zimmerman_2011]: https://openlibrary.org/search?q=Zimmerman+Economics+Satellite+Communications
