---
layout: post
mathjax: true
comments: true
title: "History of SpaceX: The Patient-Private Capital-Formation Leg and the Manufacture of Patience"
date: 2026-08-02 09:00:00 +0000
categories: history business aerospace
series: spacex_history
series_title: History of SpaceX
series_index: 10
---

<!-- A290 -->
<script>console.log("A290");</script>

This article is the tenth in the History of SpaceX series and the second of three treating the capital-formation legs that the [series opener][related_post_a281_spacex_framing] introduced. The patient-private leg concerns the private capital that financed the development the government leg did not, on terms that surrendered equity and did not surrender the mission. The article's organizing claim is that patience is not a temperament that investors possess but a structural property that instruments manufacture, and that the instruments are identifiable, describable, and largely absent from the commentary that attributes the outcome to investor conviction. The binding constraint on private capital in the venture form is the fund-life clock, which obliges a fund to return capital to its limited partners on a schedule that has no relation to the development horizon of any portfolio company. The article walks the fund-life constraint and the duration mismatch it creates, the August 2008 Founders Fund entry at the moment of maximum distress, the 2009 Draper Fisher Jurvetson entry, the January 2015 Google and Fidelity round motivated by a business line that did not yet exist, the round and valuation sequence across the 2015 through drafting-date period, the semi-annual tender-offer mechanism that gives liquidity without exit and that the article treats as the decisive structural innovation, the composition of the investor base and the horizon heterogeneity across it, and the dilution management that preserved the control configuration the [Governance article A287][related_post_a287_spacex_governance] analyzes. The article contrasts the configuration against the Iridium capital structure, in which a debt-financed constellation faced a fixed obligation schedule that no development delay could accommodate, and against the OneWeb funding withdrawal, in which a nominally patient investor proved otherwise. The article treats the contemporary defense-technology venture wave and the Anduril and Palantir comparisons as the downstream consequence. The article closes with an explicit pattern-extraction section stating the abstract patient-private capital-formation mechanic in a form other informed readers can recognize in adjacent domains without naming any downstream application.

## The Patient-Private Capital-Formation Mapping Problem

The mapping problem for a comprehensive treatment of the patient-private capital-formation leg in the SpaceX case is the question of how much private capital was supplied, by whom, at what stages, on what terms, and what structural features permitted the suppliers to tolerate a holding period substantially longer than the venture form ordinarily permits.

The last element is the analytically interesting one and is the element the commentary treats least well. The ordinary account attributes the tolerance to an investor conviction about the mission. The account is not false and it is not an explanation, because an investor's conviction does not relieve the investor's fund of its obligation to return capital to its limited partners on a schedule. The question is what structural arrangement permitted the conviction to be acted upon.

The problem can be formalized in several ways. The entrepreneurial-finance tradition from [Sahlman 1990][research_sahlman_1990] The Structure and Governance of Venture-Capital Organizations through [Gompers 1995][research_gompers_1995], [Lerner 1994][research_lerner_1994_syndication], [Kaplan and Stromberg 2003][research_kaplan_stromberg_2003], [Kaplan and Stromberg 2004][research_kaplan_stromberg_2004], [Gompers and Lerner 2001][book_gompers_lerner_2001] The Money of Invention, [Metrick and Yasuda 2011][book_metrick_yasuda_2011] Venture Capital and the Finance of Innovation, and [Lerner 2009][book_lerner_2009] Boulevard of Broken Dreams treats the fund as the unit of analysis and supplies the structural apparatus the article requires. The corporate-finance tradition from [Myers 1977][research_myers_1977] through [Jensen and Meckling 1976][research_jensen_meckling_1976], [Jensen 1986][research_jensen_1986], and [Tirole 2006][book_tirole_2006] The Theory of Corporate Finance treats the capital structure and the claims it creates. The listing-choice tradition from [Ewens and Farre-Mensa 2020][research_ewens_farre_mensa_2020] The Deregulation of the Private Equity Markets and the Decline in IPOs treats the question of why a firm remains private. The real-options tradition from [Dixit and Pindyck 1994][book_dixit_pindyck_1994] and [Trigeorgis 1996][book_trigeorgis_1996] treats the staged commitment as an option sequence. The present article draws on all four while adopting the mission-oriented-innovation framework the [series opener][related_post_a281_spacex_framing] established as primary.

The general form of the problem can be stated compactly. Let $T^{\text{mission}}$ denote the horizon over which the mission is pursued and let $T^{\text{fund}}$ denote the contractual life of the fund supplying the capital. The duration mismatch is

$$T^{\text{mission}} \gg T^{\text{fund}}$$

with the typical venture fund life at approximately ten years subject to extensions and the mission horizon measured in decades. The mismatch is the central problem, and the patient-private leg closes only where a mechanism resolves it.

The mechanism cannot be that the investors simply wait, because the fund's obligation runs to the limited partners rather than to the portfolio company. The resolution admits three logical forms and the article examines which of them the case employed. The first is a longer fund. The second is a different vehicle without a fund-life clock. The third is a mechanism by which the fund realizes its position without the portfolio company undergoing a liquidity event. The three admit the compact disjunctive statement

$$\text{mismatch resolved} \iff \left( T^{\text{fund}} \geq T^{\text{holding}} \right) \; \vee \; \left( \nexists \; T^{\text{fund}} \right) \; \vee \; \left( \text{realization} \perp \text{exit} \right)$$

with the first disjunct requiring a term the venture industry does not offer, the second requiring a change in the composition of the supplying vehicles rather than in their behavior, and the third requiring an arrangement internal to the firm. The third is the one that operated, and it is the tender-offer mechanism the [Governance article A287][related_post_a287_spacex_governance] treats from the control side and this article treats from the capital side.

The identification problem is the counterfactual. The counterfactual differential can be written as

$$\Delta V^{\text{patient-private}}_i(t) = V^{\text{observed}}_i(t) - V^{\text{impatient-capital counterfactual}}_i(t)$$

with the attribution equal to the difference between the observed trajectory and the counterfactual in which the same capital was supplied on ordinary terms with an ordinary exit expectation. The counterfactual is partially observable in this case, because the sector provides contemporaneous ventures that raised capital on ordinary terms and encountered the consequences.

The quantity the article isolates must be separated from the larger and less interesting quantity with which it is habitually conflated. The decomposition has the form

$$\underbrace{V^{\text{observed}}_i - V^{\text{no external capital}}_i}_{\text{total financing effect}} = \underbrace{\left( V^{\text{ordinary terms}}_i - V^{\text{no external capital}}_i \right)}_{\text{supply component}} + \underbrace{\left( V^{\text{observed}}_i - V^{\text{ordinary terms}}_i \right)}_{\text{terms component}}$$

with the article addressing only the second summand. The first summand is large, is uncontroversial, and establishes merely that a capital-intensive venture requires capital. The second summand is the one on which the patience claim rests, and it is the one the commentary leaves unmeasured.

## Methodological Commitments

The article commits to the same seven methodological positions the [series opener][related_post_a281_spacex_framing] established, restated at compact reference level.

The first commitment is descriptive-analytical framing rather than prescriptive advocacy. The commitment is strained here because the investors who participated have written extensively about their participation, and the accounts are simultaneously the best available primary evidence and the most interested.

The second commitment is dual-register composition with both general-history and abstract-mechanic registers.

The third commitment is primary-source anchoring. The documentary position for this article is the weakest in the series, weaker even than that of the [Governance article A287][related_post_a287_spacex_governance], because the transactions were private placements between private parties and neither side has a disclosure obligation. The article cites the [Securities and Exchange Commission EDGAR][ref_sec_edgar] system and the [Form D exempt-offering notices][ref_sec_form_d] that establish the existence and approximate size of rounds, the [Securities Act private-placement exemption][ref_securities_act_4a2] and [Regulation D][ref_reg_d] with the [Rule 506 safe harbor][ref_rule_506] under which they were conducted, the [Rule 701 compensatory exemption][ref_rule_701] and [Rule 144 resale provisions][ref_rule_144] governing the employee equity, the [Exchange Act registration threshold][ref_exchange_act_12g] and [Rule 12g-1][ref_rule_12g1] with the [Jumpstart Our Business Startups Act of 2012][ref_jobs_act_2012] that raised it, the [Rule 13e-4 issuer tender-offer provisions][ref_rule_13e4] and [Regulation 14E][ref_reg_14e] governing the tender mechanism, the [Delaware Limited Partnership Act][ref_delaware_lp_act] and the [Investment Company Act][ref_investment_company_act] and [Investment Advisers Act][ref_investment_advisers_act] provisions structuring the funds, and the participant publications at the [Founders Fund][ref_founders_fund], [Draper Fisher Jurvetson][ref_dfj], [Valor Equity Partners][ref_valor_equity], [Sequoia][ref_sequoia], and [Baillie Gifford][ref_baillie_gifford]. The article draws on secondary sources including [Berger 2021][book_berger_2021] Liftoff, [Berger 2024][book_berger_2024] Reentry, [Vance 2015][book_vance_2015] Elon Musk, [Isaacson 2023][book_isaacson_2023] Elon Musk, [Davenport 2018][book_davenport_2018] The Space Barons, and [Fernholz 2018][book_fernholz_2018] Rocket Billionaires.

The fourth commitment is contested-claim marking. Substantially every round size, valuation, ownership percentage, and investor identity in this article is a reconstructive estimate assembled from trade-press reporting and participant statements. The reader should treat the numbers in this article with more caution than those in any other article in the series.

The fifth commitment is temporal indexing as a mid-2026 snapshot.

The sixth commitment is terminological transparency with the Terminological Note section below, with attention to the distinction between a fund and a firm, which the commentary conflates and on which the fund-life argument depends.

The seventh commitment is thesis-not-proof framing of the capital-formation closure claim.

## Patient Private Capital as an Economic Property

The patient-private capital-formation property is treated as an economic property of the financing arrangement that distinguishes ventures able to hold private capital across a development horizon exceeding the ordinary holding period from ventures obliged to exit within it.

The property is a property of the arrangement rather than of the investor, and the article's central analytical move is to state it that way. An investor with a twenty-year conviction operating a ten-year fund offers ten-year capital. The conviction affects the investor's willingness to advocate internally and does not affect the contractual obligation.

The legal apparatus that produces the constraint is documentary rather than theoretical, and identifying it precisely matters because the article's claim is that the constraint is manufactured. The entity is formed under a state statute, either the [Delaware Revised Uniform Limited Partnership Act][ref_delaware_lp_act] with the corporate provisions at the [Delaware General Corporation Law][ref_dgcl] governing the portfolio companies, or the [Texas Business Organizations Code][ref_texas_boc] following the reincorporation wave of the mid 2020s that the [Governance article A287][related_post_a287_spacex_governance] treats. Formation and standing are recorded through the [Delaware Division of Corporations][ref_delaware_division_corporations] and disputes are resolved before the [Delaware Court of Chancery][ref_delaware_chancery], whose [published opinions][ref_delaware_opinions] supply the operative interpretations of what a partnership agreement may and may not waive. The manager's obligations run through the [Investment Advisers Act][ref_investment_advisers_act] as amended by the [Dodd-Frank Wall Street Reform and Consumer Protection Act][ref_dodd_frank_2010], which withdrew the private-adviser exemption on which the industry had previously relied, and the investor-facing description of the resulting regime is published at [the Securities and Exchange Commission investor education service][ref_sec_investor_gov]. Every element of the constraint is therefore locatable in a statute, a partnership agreement, or a market convention, and none of it is a property of capital as such.

The fund structure that generates the constraint admits compact description. A fund is a limited partnership with a stated term, an investment period during which capital is deployed, and a harvest period during which positions are realized and proceeds distributed. The general partner is compensated by a management fee on committed capital and a carried interest on realized gains. The carried-interest structure may be written

$$\Pi^{\text{GP}} = f \cdot K^{\text{committed}} \cdot T^{\text{fund}} + c \cdot \left[ \sum_{i} \left( V^{\text{realized}}_i - K_i \right) \right]^{+}$$

with $f$ the management-fee rate and $c$ the carry rate. The second term is triggered by realization rather than by appreciation, which is the contractual root of the exit pressure. An unrealized gain of any magnitude pays the general partner nothing.

The consequence is that the patience question reduces to a question about realization rather than about holding. A mechanism that permits realization without a portfolio-company liquidity event resolves the tension entirely, and a mechanism that does not resolves nothing. The distinction may be stated compactly

$$\text{patience achievable} \iff \exists \; \text{realization path independent of company exit}$$

with the existence of the path being the operative condition.

The valuation step-up gives a partial substitute. A fund reports an unrealized position at a carrying value derived from the most recent round price, so that a rising valuation produces a reportable return that satisfies limited-partner expectations without any realization. The reported return admits the compact form

$$\text{TVPI} = \frac{\sum_i V^{\text{carrying}}_i + \text{distributions}}{K^{\text{drawn}}}$$

with the first term in the numerator being unrealized. The measure sustains the relationship across the interval and does not pay the carry, which is the reason it is a partial substitute rather than a complete one.

The carry is moreover not merely deferred but discounted, and the distinction sharpens the constraint considerably. The present value of a carried interest realized at a horizon $T$ takes the form

$$\operatorname{PV}\left[ \Pi^{\text{carry}} \right] = c \cdot \frac{\mathbb{E}\left[ V^{\text{realized}}_T - K \right]}{\left( 1 + r^{\text{GP}} \right)^{T}}$$

with the value declining in $T$ even where the terminal amount is certain. A general partner therefore prefers an earlier realization at a lower valuation to a later realization at a higher one whenever the valuation growth rate falls short of the discount rate, which is a preference the limited partners do not necessarily share and which no quantity of conviction about the mission alters.

The duration-matching condition that a capital supplier must satisfy can be written as

$$T^{\text{vehicle}} \geq T^{\text{holding required}}$$

with the vehicle life required to exceed the holding period. The condition is satisfied trivially by a vehicle with no stated life, which is the structural reason the investor-base composition shifted as it did.

The condition is furthermore not evaluated once at entry but continuously, because the vehicle's remaining life declines while the required holding period does not. The remaining life of a supplying vehicle has the form

$$T^{\text{remaining}}_i(t) = T^{\text{vehicle}}_i - \left( t - t^{\text{inception}}_i \right)$$

with the quantity declining at unit rate. A fund that satisfied the duration condition comfortably at the moment it invested violates it at a later date without any change in the venture, the investor's view, or the development schedule. The observation is the reason the article treats the constraint as a clock rather than as a threshold, and it is the reason an arrangement adequate at one date requires replacement at another.

The dilution the channel costs admits the compact recursion the [Governance article A287][related_post_a287_spacex_governance] develops

$$e^{\text{founder}}_N = e^{\text{founder}}_0 \prod_{n=1}^{N} \left( 1 - \delta_n \right)$$

with the product declining monotonically. The patient-private leg is therefore the costly leg of the three, and the question the closing sections pose is what it purchased that the other two could not supply.

## Cross-Disciplinary Framings

The patient-private capital-formation property draws characterization from several disciplinary traditions beyond the mission-oriented-innovation framework the series adopts as primary.

The entrepreneurial-finance tradition traces from [Sahlman 1990][research_sahlman_1990] through [Gompers 1995][research_gompers_1995] Optimal Investment Monitoring and the Staging of Venture Capital, [Lerner 1994][research_lerner_1994_syndication] The Syndication of Venture Capital Investments, [Kaplan and Stromberg 2003][research_kaplan_stromberg_2003] Financial Contracting Theory Meets the Real World, [Kaplan and Stromberg 2004][research_kaplan_stromberg_2004], [Gompers and Lerner 2001][book_gompers_lerner_2001], [Metrick and Yasuda 2011][book_metrick_yasuda_2011], [Lerner 2009][book_lerner_2009], [Kortum and Lerner 2000][research_kortum_lerner_2000] Assessing the Contribution of Venture Capital to Innovation, [Hall and Lerner 2010][research_hall_lerner_2010] The Financing of R and D and Innovation, and [Lerner 1996][research_lerner_1996_government_program]. The framing yields the fund apparatus and the staging apparatus, and its central observation for this article is that the staging instrument and the fund-life instrument pull in opposite directions. Staging preserves the investor's option to discontinue and thereby shortens the effective commitment, while the mission requires lengthening it. The tension is stated compactly as

$$T^{\text{effective commitment}} = \min_{n} \left\{ t_n \; : \; \text{continuation declined at stage } n \right\} \;\; \ll \;\; T^{\text{holding required}}$$

with the staged structure rendering the committed horizon equal to the interval to the next decision point rather than to the stated fund life. The instrument the literature treats as the principal protection against an adverse selection is therefore also the principal obstacle to a long-horizon commitment, and the literature does not generally note the second property because the ventures it studies do not require a long horizon.

The corporate-finance tradition traces from [Myers 1977][research_myers_1977] Determinants of Corporate Borrowing through [Jensen and Meckling 1976][research_jensen_meckling_1976], [Jensen 1986][research_jensen_1986], [Fama and Jensen 1983][research_fama_jensen_1983], [Shleifer and Vishny 1997][research_shleifer_vishny_1997], [Hart 1995][book_hart_1995] Firms Contracts and Financial Structure, and [Tirole 2006][book_tirole_2006]. The framing contributes the account of the claims each instrument creates and the reason a debt claim and an equity claim behave differently under a development delay. The difference admits the compact statement

$$\text{debt obligation} \; : \; \text{fixed in amount and date} \qquad \text{against} \qquad \text{equity claim} \; : \; \text{residual and undated}$$

with the first defaulting on a schedule delay and the second not. The Iridium counter-example the article develops turns entirely on the distinction.

The listing-choice and private-markets tradition traces from [Ewens and Farre-Mensa 2020][research_ewens_farre_mensa_2020] and treats the expansion of the private capital supply as the enabling condition for the entire arrangement. The supply expansion can be stated as

$$K^{\text{private available}}(t) \gg K^{\text{private available}}(t_0)$$

across the period, with the consequence that a firm requiring a magnitude of capital that would once have compelled a listing can now obtain it privately.

The framing also identifies what a firm forgoes by declining to list, which is a concrete set of obligations and entitlements rather than a diffuse loss of prestige. The obligations are the continuous disclosure regime at [Regulation S-K][ref_sec_regulation_sk], the internal-control and certification requirements the [Sarbanes-Oxley Act of 2002][ref_sarbanes_oxley_2002] imposed, and the exchange governance standards at the [New York Stock Exchange Listed Company Manual][ref_nyse_listed_company_manual] and the [Nasdaq listing rules][ref_nasdaq_listing_rules]. The entitlements are access to index inclusion under the methodologies the [FTSE Russell][ref_ftse_russell] and [S and P Dow Jones Indices][ref_spdji] providers publish, which mechanically yields a class of price-insensitive buyers, and the shareholder-proposal channel at [Rule 14a-8][ref_rule_14a8] through which the [Council of Institutional Investors][ref_cii] and the proxy advisers press governance change. A firm that remains private declines both sides of that exchange, and the article treats the second side as the more consequential because index-driven demand is precisely the recurring supply of incoming buyers that the tender mechanism must otherwise manufacture by hand.

The bargaining tradition traces from [Nash 1950][research_nash_1950] The Bargaining Problem through [Rubinstein 1982][research_rubinstein_1982], [Binmore Rubinstein and Wolinsky 1986][research_binmore_rubinstein_wolinsky_1986], [Osborne and Rubinstein 1990][book_osborne_rubinstein_1990] Bargaining and Markets, and [Muthoo 1999][book_muthoo_1999] Bargaining Theory with Applications. The framing treats the round terms as a negotiated outcome and contributes the explanation for the terms improving across the sequence, because the founder's outside option improved as the venture demonstrated capability while the investors' outside options in the sector did not. The asymmetry may be written

$$\sigma^{\text{founder}}_n = \sigma\!\left( u^{\text{founder}}_n, \; u^{\text{investor}}_n \right) \qquad \text{with} \qquad \frac{d u^{\text{founder}}_n}{d n} > 0 \quad \text{and} \quad \frac{d u^{\text{investor}}_n}{d n} \approx 0$$

with $\sigma^{\text{founder}}_n$ the founder's negotiated share at round $n$ and $u$ the disagreement payoffs. The investor's outside option is approximately flat because the sector offered no comparable alternative position, which is a consequence of the concentration the [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] documents rather than of any negotiating skill.

The real-options tradition traces from [Myers 1977][research_myers_1977], [Black and Scholes 1973][research_black_scholes_1973], [Merton 1973][research_merton_1973], [McDonald and Siegel 1986][research_mcdonald_siegel_1986], [Kogut and Kulatilaka 1994][research_kogut_kulatilaka_1994], [Dixit and Pindyck 1994][book_dixit_pindyck_1994], [Trigeorgis 1996][book_trigeorgis_1996], and [Copeland and Antikarov 2001][book_copeland_antikarov_2001]. The framing treats each round as an option exercise and supplies the account of the investor's decision at each stage. The staged valuation admits the compact recursion

$$W_n = \max \left\{ 0, \; \mathbb{E}\left[ W_{n+1} \mid \mathcal{F}_n \right] - k_n \right\}$$

with $W_n$ the value of the participation right at stage $n$, $k_n$ the capital the stage requires, and $\mathcal{F}_n$ the information available at the decision. The framing's contribution to this article is that it identifies the abandonment option as valuable to the investor and costly to the venture, so that the instrument maximizing the investor's option value is not the instrument maximizing the probability the mission is completed.

The financial-sociology tradition traces from [MacKenzie 2006][book_mackenzie_2006] An Engine Not a Camera through [Ho 2009][book_ho_2009] Liquidated, [Zaloom 2006][book_zaloom_2006] Out of the Pits, [Preda 2009][book_preda_2009] Framing Finance, and [Krippner 2011][book_krippner_2011] Capitalizing on Crisis. The framing treats the horizon norms as institutionally constructed rather than natural, and it provides the most direct support for the article's claim that patience is manufactured rather than possessed, because it establishes that the short horizon the arrangement circumvents is itself an artifact of practices rather than a property of capital. The claim admits the compact contrast

$$T^{\text{norm}} = T^{\text{norm}}\!\left( \text{prevailing institutional practice} \right) \qquad \text{against} \qquad T^{\text{norm}} = \text{constant}$$

with the left form holding and the right form being the implicit assumption of the commentary that treats a ten-year fund life as a fact about capital. The ten-year term is a convention that emerged from a particular institutional history, and a convention is precisely the kind of object a sufficiently large counterparty can renegotiate.

The behavioral tradition traces from [Kahneman and Tversky 1979][research_kahneman_tversky_1979] Prospect Theory, [Tversky and Kahneman 1992][research_tversky_kahneman_1992], [Kahneman 2011][book_kahneman_2011] Thinking Fast and Slow, [Simon 1957][book_simon_1957] Administrative Behavior, and [Staw 1976][research_staw_1976]. The framing provides the skeptical reading under which the continued participation across the later rounds reflects a commitment escalation rather than a reassessment. The two readings generate different comparative statics, admitting the compact contrast

$$\frac{\partial \, P\!\left( \text{reinvest} \right)}{\partial \, s^{\text{adverse}}} \approx 0 \;\; \text{under escalation} \qquad \text{against} \qquad \frac{\partial \, P\!\left( \text{reinvest} \right)}{\partial \, s^{\text{adverse}}} < 0 \;\; \text{under reassessment}$$

with $s^{\text{adverse}}$ an adverse signal about the venture. The discrimination between the two readings requires observing an investor's response to an adverse signal, and the record offers few adverse signals after the 2008 period, which is the reason the Alternative Analytical Frameworks section records the two as not distinguishable on the available evidence.

The venture-ecosystem and regional tradition traces from [Saxenian 1994][book_saxenian_1994] Regional Advantage, [Kenney 2000][book_kenney_2000] Understanding Silicon Valley, [Lecuyer 2006][book_lecuyer_2006] Making Silicon Valley, [Klepper 2016][book_klepper_2016] Experimental Capitalism, and [Berlin 2005][book_berlin_2005] The Man Behind the Microchip. The framing gives the institutional context within which the investor set formed and the norms it operated under, and the [Silicon Valley from Defense Contracting article A246][related_post_a246_silicon_valley_defense] treats the defense-procurement substrate from which the regional capability originally derived. The framing's contribution to this article is that the secondary market on which the whole arrangement depends is itself an institutional product requiring a density of informed counterparties, admitting the compact condition

$$N^{\text{informed counterparties}} \geq N^{\text{minimum}} \quad \text{for a functioning transfer market}$$

with the density available in a small number of locations. The observation qualifies the generality of the article's central finding in a way distinct from the state-dependence limitation, because a venture may satisfy every structural condition the article states and still lack the counterparty population that makes the transfer market operate.

The incomplete-contracts and property-rights tradition traces from [Coase 1937][research_coase_1937] The Nature of the Firm through [Williamson 1971][research_williamson_1971], [Williamson 1985][book_williamson_1985] The Economic Institutions of Capitalism, [Williamson 2002][research_williamson_2002], [Klein Crawford and Alchian 1978][research_klein_crawford_alchian_1978], [Grossman and Hart 1986][research_grossman_hart_1986] The Costs and Benefits of Ownership, [Hart and Moore 1990][research_hart_moore_1990] Property Rights and the Nature of the Firm, [Hart 1988][research_hart_1988], [Tirole 1988][book_tirole_1988] The Theory of Industrial Organization, [Laffont and Tirole 1993][book_laffont_tirole_1993], and [Milgrom 2004][book_milgrom_2004] Putting Auction Theory to Work. The framing yields the account of why the arrangement had to be a recurring institutional practice rather than a written promise. A commitment to remain patient cannot be contracted upon because the contingencies are not describable in advance, so the parties substituted a repeated transaction for a contractual term. That substitution is the central object this article studies and the tradition contributes its vocabulary.

The portfolio-theory tradition traces from [Markowitz 1952][research_markowitz_1952] Portfolio Selection and [Markowitz 1959][book_markowitz_1959] through [Sharpe 1964][research_sharpe_1964], [Lintner 1965][research_lintner_1965], and [Lewellen 1971][research_lewellen_1971] A Pure Financial Rationale for the Conglomerate Merger. The tradition offers the standing objection that an investor can diversify more cheaply than a firm can, so that firm-level patience and firm-level diversification destroy value that the investor could have obtained at lower cost. The [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] engages the objection at length. Its bearing on this article is narrower and sharper. The objection presupposes a market in which the investor can rebalance, and the whole subject of this article is an arrangement in which the investor cannot, so the objection identifies precisely the cost the arrangement imposes on the capital supplier.

The internal-capital-markets tradition traces from [Gertner Scharfstein and Stein 1994][research_gertner_scharfstein_stein_1994] through [Stein 1997][research_stein_1997], [Scharfstein and Stein 2000][research_scharfstein_stein_2000] The Dark Side of Internal Capital Markets, and [Rajan Servaes and Zingales 2000][research_rajan_servaes_zingales_2000], with the diversification-discount evidence at [Berger and Ofek 1995][research_berger_ofek_1995], [Lang and Stulz 1994][research_lang_stulz_1994], [Montgomery 1994][research_montgomery_1994], and the managerial-motive account at [Amihud and Lev 1981][research_amihud_lev_1981]. The framing matters here because retained earnings from a maturing business line are the ultimate substitute for the patient-private leg, and the tradition establishes that the substitute carries its own well-documented pathology rather than being a clean improvement.

The law-and-finance and comparative-governance tradition traces from [La Porta Lopez-de-Silanes Shleifer and Vishny 1998][research_laporta_et_al_1998] Law and Finance through [Roe 1994][book_roe_1994] Strong Managers Weak Owners, [Easterbrook and Fischel 1991][book_easterbrook_fischel_1991] The Economic Structure of Corporate Law, [Hansmann 1996][book_hansmann_1996] The Ownership of Enterprise, [Manne 1965][research_manne_1965] Mergers and the Market for Corporate Control, [Grossman and Hart 1988][research_grossman_hart_1988] One Share One Vote, [Harris and Raviv 1988][research_harris_raviv_1988], [DeAngelo and DeAngelo 1985][research_deangelo_deangelo_1985], [Bebchuk Kraakman and Triantis 2000][research_bebchuk_kraakman_triantis_2000], [Gompers Ishii and Metrick 2003][research_gompers_ishii_metrick_2003], and [Gompers Ishii and Metrick 2010][research_gompers_ishii_metrick_2010]. The [Hansmann 1996][book_hansmann_1996] treatment is the most directly useful of these for the present article, because it asks which class of party should own an enterprise as a function of the costs of contracting with each class, and the arrangement this article describes is legible as an answer to that question rather than as a governance anomaly.

The auction and market-design tradition traces from [Myerson 1981][research_myerson_1981] Optimal Auction Design through [McAfee and McMillan 1988][book_mcafee_mcmillan_1988] and [Milgrom 2004][book_milgrom_2004]. The tradition bears directly on the tender mechanism, which is a recurring sale of a fixed quantity into a restricted bidder set at a price the seller sets. The tradition's central result is that the seller's revenue and the information content of the resulting price depend on the participation rule, and the participation rule in this arrangement is set by the issuer, which is the formal basis for the market-microstructure objection the Alternative Analytical Frameworks section records.

The mission-oriented innovation and developmental-state tradition traces from [Mazzucato 2013][book_mazzucato_2013] The Entrepreneurial State and [Mazzucato 2021][book_mazzucato_2021] Mission Economy through [Bonvillian 2018][research_bonvillian_2018], [Johnson 1982][book_johnson_1982] MITI and the Japanese Miracle, [Amsden 1989][book_amsden_1989] Asia's Next Giant, [Wade 1990][book_wade_1990] Governing the Market, [Evans 1995][book_evans_1995] Embedded Autonomy, [Chang 2002][book_chang_2002] Kicking Away the Ladder, and [Woo-Cumings 1999][book_woo_cumings_1999]. The tradition provides the framework the [series opener][related_post_a281_spacex_framing] adopts as primary, and its contribution here is the observation that the state supplied the patience the private market could not, through the non-dilutive channel the [Government-Anchor Capital-Formation Leg article A289][related_post_a289_spacex_government_anchor_leg] treats, so that the two legs are substitutes at the margin and not merely complements.

The space-economics tradition traces from [Weinzierl 2018][research_weinzierl_2018] Space the Final Economic Frontier through [Hertzfeld 2002][research_hertzfeld_2002] and [Adilov Alexander and Cunningham 2018][research_adilov_et_al_2018], with the policy histories at [Launius 1994][book_launius_1994], [Launius 2004][book_launius_2004], [McCurdy 1994][book_mccurdy_1994], [Handberg 1994][book_handberg_1994], [Logsdon 1970][book_logsdon_1970], and [McDougall 1985][book_mcdougall_1985] The Heavens and the Earth. The tradition is the one most directly concerned with the sector and least concerned with the financing instruments, which is the asymmetry the Historiographical Gap section records as this article's opening.

The organizational-capability tradition traces from [Penrose 1959][book_penrose_1959] The Theory of the Growth of the Firm through [Cyert and March 1963][book_cyert_march_1963], [March and Simon 1958][book_march_simon_1958], [March 1991][research_march_1991] Exploration and Exploitation, [Nelson and Winter 1982][book_nelson_winter_1982], [Teece Pisano and Shuen 1997][research_teece_pisano_shuen_1997] Dynamic Capabilities, [Teece 1986][research_teece_1986] Profiting from Technological Innovation, [Teece 2007][research_teece_2007], [Wernerfelt 1984][research_wernerfelt_1984], [Barney 1991][research_barney_1991], and [Peteraf 1993][research_peteraf_1993]. The tradition offers the constraint that binds after capital ceases to, which the [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] develops as the attention-allocation limit, and it is the reason this article declines to treat capital supply as the sole binding constraint on the trajectory it describes.

The practitioner tradition traces from [Thiel 2014][book_thiel_2014] Zero to One, [Ries 2011][book_ries_2011] The Lean Startup, [Blank 2013][book_blank_2013] The Four Steps to the Epiphany, [Moore 1991][book_moore_1991] Crossing the Chasm, and [Christensen 1997][book_christensen_1997] The Innovator's Dilemma. The framing is the one the participants themselves employed and is cited here as evidence about the decision environment rather than as analytical authority.

## The Fund-Life Constraint and the Duration Mismatch

The constraint deserves treatment before the history, because it is the obstacle every subsequent event either circumvents or fails to.

A venture fund is organized as a limited partnership under the [Delaware Limited Partnership Act][ref_delaware_lp_act] or a comparable regime, with a stated term customarily of approximately ten years subject to extensions of one or two years at the general partner's election or with limited-partner consent. The fund is exempt from registration as an investment company under the [Investment Company Act][ref_investment_company_act] provisions, and the manager is registered or exempt under the [Investment Advisers Act][ref_investment_advisers_act]. The limited-partner community's standards are documented through the [Institutional Limited Partners Association][ref_ilpa], and the industry-level structures through the [National Venture Capital Association][ref_nvca].

The term decomposes into two periods with different functions, admitting the compact form

$$T^{\text{fund}} = T^{\text{investment}} + T^{\text{harvest}} + \epsilon^{\text{extension}} \qquad \text{with} \qquad T^{\text{investment}} \approx T^{\text{harvest}} \approx 5 \text{ years}, \;\; \epsilon^{\text{extension}} \leq 2 \text{ years}$$

with capital deployed during the first period and positions realized during the second. The decomposition matters because a position taken late in the investment period faces an available holding period of approximately the harvest period alone rather than the full term, so that the nominal ten-year figure overstates the patience available to a late-deployed position by a factor approaching two.

The structure imposes the constraint through three distinct channels that the commentary generally collapses into one.

The first is contractual. The partnership agreement obliges the general partner to wind up and distribute at the term. The obligation is not discretionary.

The second is compensatory. The carried interest is earned on realization, so that a general partner holding an appreciated but unrealized position has earned nothing on it. The incentive may be stated compactly

$$\frac{\partial \Pi^{\text{GP}}}{\partial V^{\text{unrealized}}} = 0 \qquad \text{while} \qquad \frac{\partial \Pi^{\text{GP}}}{\partial V^{\text{realized}}} = c > 0$$

with the general partner's compensation insensitive to appreciation and sensitive only to realization.

The third is reputational and is the one that binds most tightly in practice. A general partner raising a successor fund is assessed on distributed capital rather than on reported carrying value, because the limited partners have learned to discount the latter. The assessment metric admits the compact form

$$\text{DPI} = \frac{\text{distributions to limited partners}}{\text{capital drawn}}$$

with a low value impeding the successor fundraise irrespective of the reported unrealized value. A general partner therefore faces a pressure to realize that operates on the fundraising cycle of approximately three to four years rather than on the fund life of ten. The binding clock admits the compact identification

$$T^{\text{binding}} = \min \left\{ T^{\text{fund}}, \; \Delta^{\text{fundraise cycle}} \right\} = \Delta^{\text{fundraise cycle}} \approx 3 \text{ to } 4 \text{ years}$$

with the reputational channel binding well before the contractual one. The identification is the reason the article treats the commentary's collapse of the three channels into one as a substantive error rather than a simplification, because the channel that actually binds is the one the partnership agreement does not mention.

The mismatch against a mission horizon is severe. The required holding period for a position taken in the 2008 period against a mission whose completion lies beyond the drafting date exceeds

$$T^{\text{holding}} > 18 \text{ years}$$

which is approximately twice the nominal fund life and approximately five times the successor-fundraise cycle. The mismatch ratios admit the compact statement

$$\rho^{\text{fund}} = \frac{T^{\text{holding}}}{T^{\text{fund}}} \approx 2 \qquad \text{and} \qquad \rho^{\text{cycle}} = \frac{T^{\text{holding}}}{\Delta^{\text{fundraise cycle}}} \approx 5$$

with both quantities exceeding unity by a margin no extension provision closes. No amount of investor conviction reconciles the figures. Only a structural mechanism does.

## The 2008 Founders Fund Entry

The August 2008 investment constitutes the first substantial external capital and occurred at the moment the [series opener][related_post_a281_spacex_framing] identifies as the near-death period, between the third and fourth Falcon 1 flights. The investor's own account is published at the [Founders Fund][ref_founders_fund] and the narrative record appears in [Berger 2021][book_berger_2021] Liftoff, [Vance 2015][book_vance_2015] Elon Musk, and [Isaacson 2023][book_isaacson_2023] Elon Musk. The vehicle record for the flights bracketing the investment is published in the firm's own archive at the [SpaceX news archive][ref_spacex_news_archive] and the [SpaceX corporate record][ref_spacex_company], with the [fourth Falcon 1 flight of September 2008][ref_spacex_press_falcon1_flight4_2008] following the investment by approximately six weeks.

The macroeconomic setting is not incidental and is documented independently of any participant account. The [National Bureau of Economic Research][ref_nber] business-cycle chronology dates the contraction as beginning in December 2007 and continuing through June 2009, so the investment fell near the midpoint of the deepest financial dislocation of the period, and the contemporaneous deterioration in business conditions is recorded in the [Conference Board][ref_conference_board] indicator series. The observation cuts against the ordinary telling rather than supporting it. Capital was contracting across the whole venture market at the moment this position was taken, which means the transaction cannot be explained by an abundance of capital seeking risk and must be explained by something to the counterparties.

The analytically interesting feature of the investment is the terms rather than the timing. The bargaining position at the moment admits the compact statement through the runway quantity

$$T^{\text{runway}} = \frac{C^{\text{cash on hand}}}{\dot{C}^{\text{burn}}}$$

with the quantity at the August 2008 date measured in weeks rather than in quarters. The bargaining apparatus predicts that an investor supplying capital to a venture at such a runway should extract control terms in proportion to the asymmetry, because the founder's disagreement payoff approaches the liquidation value. The terms agreed did not transfer control, which the [Governance article A287][related_post_a287_spacex_governance] treats from the control side.

The capital-side reading gives a complementary explanation the control-side reading does not. The investor's stated thesis was that existing venture practice systematically underfunded technically ambitious ventures, so that the investor's competitive position depended on being willing to fund specifically what others would not. Under the thesis, the terms are not a concession extracted from a weak position but a product the investor was selling. The distinction is stated compactly as

$$\text{terms} = \arg\max \left[ \text{value captured in this transaction} \right] \qquad \text{against} \qquad \arg\max \left[ \text{deal flow across future transactions} \right]$$

with the second objective recommending founder-favorable terms as a reputational investment. The condition under which the second objective dominates takes the form

$$\underbrace{\Delta u^{\text{this transaction}}}_{< 0} \; + \; \sum_{m > 0} \pi_m \, \Delta u^{\text{transaction } m} \; > \; 0$$

with $\pi_m$ the probability that the reputation secures a future transaction $m$ that would otherwise have been unavailable. The inequality holds where the investor expects a long sequence of future transactions in a category where founder selection of investors is the operative constraint. The reading is consistent with the investor's subsequent positioning and does not require attributing any unusual generosity.

## The 2009 Draper Fisher Jurvetson Entry

The 2009 entry by the firm whose record appears at the [Draper Fisher Jurvetson][ref_dfj] archive extended the investor base and occurred after the fourth Falcon 1 flight had succeeded and the CRS-1 contract the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] treats had been awarded. The vehicle record is at the [fifth Falcon 1 flight of July 2009][ref_spacex_press_falcon1_flight5_2009], the programme record at the [NASA Commercial Resupply Services programme][ref_nasa_crs_program] and the broader [NASA commercial space programmes][ref_nasa_commercial_space_programs] and [NASA commercial space office][ref_nasa_commercial_space], and the award record is traceable through the [USAspending][ref_usaspending] and [Federal Procurement Data System][ref_fpds] databases, which supply obligation-level detail that no participant account does.

The sequencing is analytically important and connects this article to the preceding one. The government award of the December 2008 period materially altered the risk profile the private investor evaluated, converting a venture with a demonstrated vehicle and no customer into a venture with both. The effect on the private capital cost admits the compact statement

$$r^{\text{private}}\big|_{\text{post-award}} < r^{\text{private}}\big|_{\text{pre-award}}$$

with the award functioning as a credit enhancement supplied by a third party at no cost to the venture. The mechanism operating on the discount rate is the removal of a distinct failure mode from the risk decomposition, admitting the compact form

$$P^{\text{failure}} = 1 - \left( 1 - p^{\text{technical}} \right)\left( 1 - p^{\text{market}} \right) \qquad \text{with} \qquad p^{\text{market}} \big|_{\text{post-award}} \ll p^{\text{market}} \big|_{\text{pre-award}}$$

with the fourth Falcon 1 flight reducing the first factor and the award reducing the second. The two reductions arrived within four months of one another, which is the reason the 2009 round priced as it did and the reason the separate contributions cannot be identified from the price alone. The interaction is the reason the three capital-formation legs are treated as a system rather than as independent channels, and it runs in the opposite direction from the interaction the [Government-Anchor Capital-Formation Leg article A289][related_post_a289_spacex_government_anchor_leg] identifies, in which the private capital financed the litigation that opened the government channel.

## The January 2015 Google and Fidelity Round

The January 2015 round in which approximately 1 billion dollars was supplied for approximately 10 percent of the firm is treated from the portfolio side in the [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] and from the governance side in the [Governance article A287][related_post_a287_spacex_governance]. The capital-formation reading adds a third element.

The round is the clearest case in the series of capital raised against a business that did not yet exist. The constellation programme was announced in January 2015 at the event recorded in the [SpaceX Seattle announcement][ref_spacex_seattle_announcement_2015], with the programme record subsequently at [SpaceX Starlink][ref_spacex_starlink], the [first operational satellite batch of May 2019][ref_spacex_press_starlink_v0_9_2019], and the [service beta of 2020][ref_spacex_press_beta_2020]. The round therefore priced an option on a business line whose first hardware flew more than four years later. The corporate investor's own disclosure obligations are discharged through the [Alphabet investor relations][ref_alphabet_ir] materials, which record the position at the parent level without disclosing terms, and the general corporate record is at the [SpaceX corporate record][ref_spacex_company].

The two reported quantities imply a third by arithmetic, admitting the compact form

$$V^{\text{post-money}} = \frac{k}{\delta} = \frac{1 \text{ billion}}{0.10} = 10 \text{ billion dollars} \qquad \text{implying} \qquad V^{\text{pre-money}} = 9 \text{ billion dollars}$$

against the figure of approximately 12 billion dollars that the trade press reported for the round. The discrepancy is stated here rather than reconciled, because the available record does not establish whether the reported figure is pre-money or post-money, whether the round included a secondary component that would not dilute, or whether the percentage is approximate to within the margin the gap requires. The reader should treat the arithmetic as a consistency check that the reported figures do not quite pass, and the Data Sources section records the general limitation of which this is an instance.

The round introduced a class of investor with a structurally different horizon. A corporate strategic investor holds a position on a balance sheet with no fund life, and a large asset manager holds a position in an open-ended vehicle with no stated term. Neither faces the constraint the preceding section describes. The duration-matching condition is therefore satisfied trivially for both, admitting the compact statement

$$T^{\text{vehicle}} \to \infty \quad \Longrightarrow \quad T^{\text{vehicle}} \geq T^{\text{holding required}} \; \text{ for every } \; T^{\text{holding required}}$$

with the condition satisfied without reference to the development schedule, the mission horizon, or any forecast whatever. The point deserves emphasis because it is the clearest instance in the article of the central claim. The balance-sheet holder is not more patient in any psychological sense than the venture fund. It is subject to a different instrument.

The shift admits the compact statement as a change in the weighted average vehicle life across the investor base

$$\bar{T}^{\text{vehicle}}(t) = \sum_i w_i(t) \, T^{\text{vehicle}}_i \qquad \text{with} \qquad \frac{d \bar{T}^{\text{vehicle}}}{dt} > 0$$

with the weighted average rising as the base broadened from closed-end venture funds toward evergreen and balance-sheet holders. The rise is the principal structural development in the financing history and it is substantially independent of any investor's conviction.

The weighted average is moreover the wrong summary statistic for the purpose, and the correct one behaves differently. What binds is the earliest term across the base rather than the average, because a single holder reaching its term generates a realization demand irrespective of the horizons the remaining holders enjoy. The binding quantity can be written as

$$T^{\text{binding}}(t) = \min_i \; T^{\text{remaining}}_i(t)$$

with the minimum rather than the mean governing. The broadening of the base therefore does not by itself relieve the pressure, because adding a perpetual holder to a base containing a fund near term leaves the minimum unchanged. The observation is what makes the tender mechanism necessary rather than merely convenient, because the mechanism operates precisely on the holder attaining the minimum.

## The Round Sequence and Valuation Trajectory

The round sequence across the 2015 through drafting-date period comprises primary rounds and secondary tender offers at a rising valuation. The existence and approximate scale of the rounds reaches the public record through the [Form D notices][ref_sec_form_d] filed with the [Securities and Exchange Commission EDGAR][ref_sec_edgar] system under the [Regulation D][ref_reg_d] and [Rule 506][ref_rule_506] exemptions, and the terms do not.

The reported valuation trajectory rises from approximately 12 billion dollars at the 2015 round through approximately 21 billion, 28 billion, and 33 billion dollars across the 2017 through 2019 period, approximately 46 billion dollars in the 2020 period, approximately 74 billion and 100 billion dollars across the 2021 period, approximately 127 billion dollars in the 2022 period, approximately 180 billion dollars in the late 2023 period, approximately 210 billion dollars in the mid 2024 period, and approximately 350 billion dollars in the late 2024 period. Every figure is a reconstructive estimate drawn from trade-press reporting of tender prices and round terms.

The trajectory's analytical function in this article is not to establish a value but to establish that a reportable return was continuously available to the holders without any realization. The step-up between consecutive rounds has the form

$$g_n = \frac{V_n}{V_{n-1}} - 1$$

with the positive sequence of $g_n$ supplying the carrying-value increases that sustained the limited-partner relationships across the interval. The cumulative effect on a position held from the 2015 round admits the compact product

$$\frac{V_N}{V_0} = \prod_{n=1}^{N} \left( 1 + g_n \right) \approx 29 \qquad \text{over} \qquad N \approx 10 \text{ rounds across } 10 \text{ years}$$

corresponding to an implied annualized rate

$$\bar{g} = \left( \frac{V_N}{V_0} \right)^{1/\Delta t} - 1 \approx 0.40$$

with $\Delta t$ the elapsed interval in years. The figures are reconstructions and inherit every limitation the Data Sources section records, and their analytical function is not to establish a return but to establish that the sequence was monotone. A monotone sequence is what the mechanism requires, and a single interruption would have suspended it. The mechanism is the partial substitute the economic-property section identifies, and its limitation is that it pays no carried interest and satisfies no distribution metric.

The operational milestones against which each successive round was priced are documented in the firm's own record and can be checked independently of any valuation report. They comprise the [first Falcon 9 flight of June 2010][ref_spacex_press_falcon9_first_flight_2010], the [first Dragon orbital demonstration of December 2010][ref_spacex_press_dragon_c1_2010], the [constellation deployment sequence][ref_spacex_press_starlink_v0_9_2019], the [next-generation vehicle programme][ref_spacex_starship_program], the [crewed spaceflight line][ref_spacex_human_spaceflight], and the [defense services line][ref_spacex_starshield], with the consolidated record at the [SpaceX news archive][ref_spacex_news_archive]. The article's position is that the milestone sequence and the valuation sequence are separately observable and that only their conjunction supports treating the latter as informative, since a rising sequence of issuer-set prices unaccompanied by demonstrated capability would carry no evidential weight at all.

## The Tender-Offer Mechanism as Liquidity Without Exit

The semi-annual tender-offer mechanism is the decisive structural innovation in the financing history and the element the article treats as the answer to the question the mapping problem poses.

The mechanism is described from the control side in the [Governance article A287][related_post_a287_spacex_governance]. The capital-side description is that the firm periodically arranges for incoming investors to purchase shares from existing holders at a price the firm sets, conducted under the [Rule 13e-4][ref_rule_13e4] and [Regulation 14E][ref_reg_14e] provisions where the issuer participates and under the [Rule 144][ref_rule_144] resale provisions for the selling holders.

The recurrence interval is itself load-bearing and is generally reported without being used. A holder reaching its term at an arbitrary date waits at most one interval for the next occasion, admitting the compact bound

$$t^{\text{wait}}_{\max} = \frac{1}{f^{\text{tender}}} = \frac{1}{2 \text{ per year}} = 6 \text{ months}$$

with the residual mismatch between the fund term and the realization opportunity bounded at approximately five percent of the ten-year term. The bound is what permits the mechanism to be treated as continuously available rather than as an episodic event. An arrangement conducting a tender every three years would leave a residual mismatch of the same order as the harvest period itself and would not resolve the constraint, which establishes that the frequency and not merely the existence of the mechanism is doing the work.

The consequence for the fund-life constraint is complete. A fund approaching its term can realize its position at a market-tested price without the portfolio company undergoing any liquidity event whatever. The realization triggers the carried interest, produces the distribution, and improves the distributed-capital metric on which the successor fundraise depends. The mechanism satisfies all three channels through which the constraint operates, admitting the compact conjunctive statement

$$\left[ \text{wind-up satisfied} \right] \wedge \left[ \frac{\partial \Pi^{\text{GP}}}{\partial \, \text{tender}} = c > 0 \right] \wedge \left[ \Delta \, \text{DPI} > 0 \right]$$

with the three conjuncts corresponding to the contractual, compensatory, and reputational channels the preceding section separates. The completeness is the reason the article treats the mechanism as decisive rather than as helpful. A mechanism satisfying two of the three channels would leave a residual pressure, and the arrangement leaves none.

The clearing condition the mechanism must satisfy at each occasion may be written

$$\sum_{i \in \mathcal{S}_t} q_i \; \leq \; \sum_{j \in \mathcal{B}_t} d_j \big( P_t \big)$$

with $\mathcal{S}_t$ the set of holders seeking to sell at the occasion, $\mathcal{B}_t$ the set of incoming buyers, and $d_j$ the demand each buyer brings at the price the firm sets. The issuer sets $P_t$ rather than discovering it, which means the issuer selects the point at which the inequality binds. The control over the clearing price is the feature the market-microstructure objection in the Alternative Analytical Frameworks section identifies as the principal challenge to the quantitative material, and the article accepts the objection.

The resolution can be stated as

$$\text{realization} \perp \text{company exit}$$

with the two events rendered independent. The independence is what manufactures the patience, and it is manufactured rather than possessed because it is a property of a recurring institutional arrangement rather than of any party's preferences.

The disclosure asymmetry the arrangement produces deserves statement alongside the mechanism itself. A holder crossing a beneficial-ownership threshold in a listed issuer files under [Schedule 13D][ref_schedule_13d] and the position becomes public, whereas the equivalent transfer in this arrangement generates no public filing at all beyond the exempt-offering notices at [Form D][ref_sec_form_d]. The consequence is that the identity and size of the incoming buyers at each occasion are unavailable to any outside party, including to the selling holders, and that the mechanism this article describes as manufacturing patience simultaneously withdraws from public view the transactions through which it operates. The [Delaware Court of Chancery][ref_delaware_chancery] supplies whatever after-the-fact scrutiny exists, and it operates only when a participant sues. The critical literature the Historiographical Gap section records treats this as the central objection, and the article regards the objection as correct on the facts while disputing that it is an argument against describing the mechanism accurately.

The mechanism's availability conditions deserve statement, because they determine how far the arrangement generalizes. The mechanism requires a continuing supply of incoming investors willing to purchase at a rising price, which requires in turn that the firm's prospects continue to improve on the incoming investors' assessment. The condition admits the compact form

$$\exists \; \text{buyer at } P_t \; \text{ with } \; P_t > P_{t-1}$$

at each tender. A firm whose prospects deteriorate finds the mechanism unavailable precisely when it would be most needed, which means the mechanism yields patience in good states and contributes none in bad ones. The state dependence takes the form

$$\mathbf{1}\left[ \text{mechanism available at } t \right] = \mathbf{1}\left[ \mathbb{E}_t\left[ V_{t+1} \right] > V_t \right]$$

with the availability indicator equal to the indicator of improving prospects. The identity is the formal statement of the asymmetry, and it establishes that the mechanism is not a hedge. A hedge pays in the adverse state. The mechanism described here is unavailable in it. The asymmetry is the principal limitation on the generality of the article's central finding.

## Investor-Base Composition and Horizon Heterogeneity

The investor base broadened across the period from a small group of venture funds to a set comprising venture funds, growth funds, corporate strategic investors, mutual-fund complexes, sovereign investors, and family offices. The participants whose involvement is publicly acknowledged include the firms whose records appear at the [Founders Fund][ref_founders_fund], the [Draper Fisher Jurvetson][ref_dfj] archive, the [Valor Equity Partners][ref_valor_equity], the [Sequoia][ref_sequoia], and the [Baillie Gifford][ref_baillie_gifford].

The analytically relevant variation across the set is the vehicle life rather than the capital magnitude. The classes admit compact ordering

$$T^{\text{closed-end venture fund}} < T^{\text{growth fund}} < T^{\text{open-ended asset manager}} < T^{\text{corporate balance sheet}} \approx T^{\text{sovereign}} \approx T^{\text{family office}} \to \infty$$

with the rightmost classes facing no stated term at all. The composition shift toward the right of the ordering reduced the aggregate pressure on the firm independently of the tender mechanism, and the two effects are complementary rather than substitutable.

The dispersion admits measurement through a concentration index over the holdings, taking the compact form

$$H_t = \sum_i \left( \frac{s_{i,t}}{\sum_k s_{k,t}} \right)^{\!2}$$

with $s_{i,t}$ the holding of investor $i$ and the index declining across the period as the base broadened. The quantity is not observable in the present case, because the position sizes are not disclosed, and it is stated here to identify precisely which unobserved quantity the article's dispersion argument depends upon. The comparison classes are observable, however. A balance-sheet holder of the kind exemplified in the [Berkshire Hathaway][ref_berkshire] and [Ford investor relations][ref_ford_ir] disclosures reports positions at the parent level under the ordinary regime, as does the corporate strategic holder at [Alphabet][ref_alphabet_ir], while the open-ended asset manager reports portfolio holdings periodically under the regime described at [the Securities and Exchange Commission investor education service][ref_sec_investor_gov]. The article's dispersion argument therefore rests on a quantity that is routinely disclosed for every class of holder except in the arrangement under study.

The dispersion of the base has a second effect the [Governance article A287][related_post_a287_spacex_governance] treats, namely that a dispersed base faces a coordination cost in assembling any coalition. The cost may be stated compactly

$$c^{\text{coalition}} \sim \left| \left\{ i : \text{holders required for a blocking position} \right\} \right| \;\; \text{increasing as } H_t \text{ falls}$$

with a lower concentration requiring a larger coalition and therefore a higher coordination cost. The capital-formation reading adds that a dispersed base also faces a coordination cost in demanding an exit, so that the dispersion serves the patience objective and the control objective through the same mechanism. The coincidence is not accidental, because both objectives are defeated by the same event, namely a coordinated action by a sufficient bloc of holders.

## Dilution Management and Control Preservation

The cumulative dilution across the sequence is the cost of the leg and is the quantity the control configuration was designed to tolerate.

The instruments through which the dilution was absorbed without control passing are documented in the corporate-law materials rather than in any transaction record. The differential-voting structure operates under the [Delaware General Corporation Law][ref_dgcl] provisions the [Governance article A287][related_post_a287_spacex_governance] analyzes, with the interpretive record at the [Delaware Court of Chancery][ref_delaware_chancery] and its [published opinions][ref_delaware_opinions], and the employee equity that constitutes a further dilution channel is issued under the [Rule 701][ref_rule_701] compensatory exemption and resold under [Rule 144][ref_rule_144]. The institutional objection to the arrangement is stated in the [Council of Institutional Investors dual-class policy][ref_cii_dual_class] and in the proxy-adviser positions at [Institutional Shareholder Services][ref_iss_governance] and [Glass Lewis][ref_glass_lewis], none of which reaches a firm that never lists.

The arithmetic is stated in the economic-property section and in the [Governance article A287][related_post_a287_spacex_governance]. The point this article adds is that the dilution and the patience are jointly determined rather than independent. A round raised at a higher valuation dilutes less for the same capital, and a higher valuation is available only where the prior capital was patient enough to permit the intervening progress. The relationship can be written as

$$\delta_n = \frac{k_n}{V_n + k_n} \qquad \text{with} \qquad V_n = V\!\left( \text{progress permitted by } \{ k_1, \ldots, k_{n-1} \} \right)$$

with the dilution of the round depending on the valuation the prior rounds' patience produced. The structure means the total dilution across a financing sequence is not the sum of a fixed set of costs but depends on the sequencing, and that a single impatient round early in the sequence raises the total cost of every subsequent round.

The sensitivity of the terminal founder share to the dilution at any single round has the form

$$\frac{\partial e^{\text{founder}}_N}{\partial \delta_n} = - \frac{e^{\text{founder}}_N}{1 - \delta_n}$$

with the magnitude increasing in $\delta_n$, so that the rounds carrying the largest dilution are also the rounds at which a marginal improvement in terms is worth most. The early rounds satisfy both conditions simultaneously, being the rounds at the lowest valuations and therefore the rounds at which the dilution per dollar is highest.

The interaction with the government leg the [Government-Anchor Capital-Formation Leg article A289][related_post_a289_spacex_government_anchor_leg] treats is direct. The non-dilutive capital displaced rounds that would otherwise have been raised at the lowest valuations in the sequence, which is where the dilution per dollar is highest. The effect is stated compactly as

$$e^{\text{founder}}_N \Big|_{\text{both legs}} \; = \; e^{\text{founder}}_0 \prod_{n \notin \mathcal{D}} \left( 1 - \delta_n \right) \qquad \text{with} \qquad \mathcal{D} = \left\{ n : \text{round displaced by non-dilutive capital} \right\}$$

with the displaced set concentrated at the low-valuation end of the sequence. The two legs therefore interact multiplicatively rather than additively, and the combined effect on the terminal founder share exceeds the sum of the separate effects.

## The Iridium Capital-Structure Counter-Example

The Iridium programme is treated from the portfolio side in the [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] and from the value-gradient side in the [Value Gradient article A282][related_post_a282_spacex_value_gradient]. The capital-structure reading is distinct and is the one that bears on this article.

The programme was financed to a substantial degree with debt, and the consequence is the one the corporate-finance framing predicts. A debt claim is fixed in amount and fixed in date, so that a schedule delay or a revenue shortfall produces a default rather than a disappointment. The default condition may be written

$$\text{default} \iff \text{cash available at } t < D_t$$

with $D_t$ contractually specified and independent of the operating reality. The consequence is a difference in the sensitivity of the failure probability to a schedule delay, admitting the compact contrast

$$\frac{\partial P^{\text{failure}}}{\partial \, \Delta t^{\text{delay}}} \bigg|_{\text{debt-financed}} \;\; \gg \;\; \frac{\partial P^{\text{failure}}}{\partial \, \Delta t^{\text{delay}}} \bigg|_{\text{equity-financed}}$$

with the delay converting directly into a missed payment under the first structure and into a deferred return under the second. The case is documented in [Finkelstein and Sanford 2000][research_finkelstein_sanford_2000] Learning from Corporate Mistakes, [Zimmerman 2011][research_zimmerman_2011], and the primary record at the [Iridium Chapter 11 filing][ref_iridium_chapter_11_1999] lodged with the [Securities and Exchange Commission EDGAR][ref_sec_edgar] system, with the proceeding conducted under the [United States Bankruptcy Code Chapter 11][ref_bankruptcy_code_ch11] provisions and administered through the [United States bankruptcy court system][ref_uscourts_bankruptcy]. The operator's own contemporaneous record survives at the [Iridium corporate news archive][ref_iridium_press_archive_1998] and the financial-press reconstruction of the 1999 failure at [Bloomberg][ref_bloomberg]. The successor entity continues to operate the constellation, which is the detail most often omitted from the citation of this case as a failure. The system worked. The capital structure did not.

The comparison to the SpaceX financing is the cleanest available demonstration that the instrument matters more than the quantity. Both ventures raised large sums for a capital-intensive constellation. The one raised equity from holders who could wait and the other raised debt from holders who could not. The difference admits the compact statement

$$\text{patience} = f\!\left( \text{claim type}, \; \text{vehicle life}, \; \text{realization path} \right)$$

with the quantity of capital appearing nowhere in the expression. A venture that raises a correct amount on a wrong instrument has not solved the capital-formation problem.

## The OneWeb Withdrawal Counter-Example

The OneWeb constellation programme supplies the complementary negation, in which the capital was equity rather than debt and proved impatient nonetheless.

The programme was funded substantially by a large investment vehicle whose stated horizon was long and whose announced thesis emphasized patient support for capital-intensive technology ventures. The vehicle declined to supply a further round in the early 2020 period, and the programme filed for Chapter 11 protection in the March 2020 period with a portion of its constellation deployed. The programme was subsequently acquired and continued under different ownership, documented through the [OneWeb corporate record][ref_oneweb] and the [Eutelsat corporate record][ref_eutelsat_oneweb], with the proceeding administered through the [United States bankruptcy court system][ref_uscourts_bankruptcy] and the sector reporting at [European Spaceflight][ref_european_spaceflight] and [Space Policy Online][ref_space_policy_online]. The Virgin Orbit wind-up documented in the [Virgin Orbit court record][ref_virgin_orbit_court] supplies a third instance of the same sequence within the same sector and the same decade, which is the reason the article treats the pattern as structural rather than as a property of any single sponsor.

The case establishes the proposition the article most needs established, which is that a stated horizon is not a structural property. The vehicle in question had a stated life and a set of investors with their own claims, and the decision to discontinue was available to it at every round irrespective of any prior representation. The distinction can be stated as

$$\text{stated horizon} \neq \text{contractual horizon} \neq \text{revealed horizon}$$

with the three quantities differing and only the third being observable after the fact. The case is the reason the article treats the structural mechanisms rather than the investor characterizations as the object of analysis.

The case also isolates the mechanism the SpaceX arrangement possessed and the OneWeb arrangement did not. A venture with a functioning secondary market can replace a departing holder. A venture without one cannot, so that a single holder's withdrawal is terminal. The difference may be stated compactly

$$P\!\left( \text{terminal} \mid \text{holder withdraws} \right) = \begin{cases} \approx 0 & \text{secondary market exists} \\ \approx 1 & \text{otherwise} \end{cases}$$

with the secondary market functioning as an insurance mechanism against a single-holder failure. The concentration measure the Investor-Base section introduces separates the two cases directly, admitting the compact contrast

$$H^{\text{OneWeb}} \approx 1 \qquad \text{against} \qquad H^{\text{SpaceX}} \ll 1$$

with the first configuration placing substantially the entire supply obligation on a single holder. The two failure conditions the article identifies, namely the absent transfer market and the concentrated base, therefore both obtained in the OneWeb case and neither obtained in the comparison case. The mechanism is the same tender arrangement the preceding section describes, which therefore performs two distinct functions and is doubly load-bearing.

## The Adverse-State Financing Regime

The article has established that the tender mechanism provides patience in favorable states and none in adverse ones. It has not said what happens in the adverse state, and the omission is consequential enough to warrant its own treatment, because the answer undermines an independence assumption the pattern-extraction section makes.

A venture whose prospects deteriorate does not simply fail to raise. It raises on a different instrument set. The instruments are documented in the financial-contracting literature at [Kaplan and Stromberg 2003][research_kaplan_stromberg_2003] and [Kaplan and Stromberg 2004][research_kaplan_stromberg_2004], which examines actual venture term sheets rather than stylized claims, and they comprise the down round at a reduced valuation, the senior liquidation preference placing the new money ahead of every prior holder, the participating preferred that takes both the preference and the residual, full-ratchet anti-dilution that reprices prior rounds retroactively, pay-to-play provisions that convert a non-participating holder's preferred stock into common, structured secondaries carrying downside protection, and venture debt secured against assets or receivables.

The instruments share a property the article's claim-type sub-property does not anticipate. Each of them moves the supplying claim toward a fixed and prioritized position and moves the founder and early-holder claim toward the residual. The liquidation waterfall that results admits the compact form

$$\Pi^{\text{common}} = \max \left\{ 0, \; V^{\text{exit}} - \sum_{n} \pi_n k_n \right\}$$

with $\pi_n$ the preference multiple attaching to round $n$ and the common holders receiving nothing until the accumulated preferences are satisfied. Where the accumulated preferences approach the enterprise value, the common claim is economically extinguished while remaining nominally outstanding, which is a condition the corporate-finance literature from [Myers 1977][research_myers_1977] treats as debt overhang and which produces the identical distortion of investment incentives that [Jensen and Meckling 1976][research_jensen_meckling_1976] and [Hart 1995][book_hart_1995] describe.

The consequence for the article's framework is direct and unwelcome. The first sub-property, which holds that the claim must be residual and undated rather than fixed in amount and date, is not a fixed property of equity as an instrument. It is a state-contingent property of the particular equity a venture is able to issue. The correct statement takes the form

$$\phi_1(s) = \mathbf{1}\left[ \text{claim residual and undated in state } s \right] \qquad \text{with} \qquad \phi_1(\text{adverse}) \to 0$$

with the sub-property degrading precisely in the state where it would carry the most value. The Iridium comparison the article develops earlier therefore requires qualification. That case is presented as a contrast between a venture that raised debt and a venture that raised equity, and the contrast holds as stated for the observed histories. It does not establish that the second venture would have retained a residual undated claim structure had it entered a comparable adverse state, because the instrument set available in that state is not the instrument set available in the state it actually occupied.

The deeper structural point concerns independence. The pattern-extraction section states the mechanic as a conjunction of five sub-properties and writes it as a product, which is the natural form for conditions that fail independently. They do not fail independently. An adverse state simultaneously withdraws the realization path, because incoming buyers at a rising price disappear, degrades the claim type, because the surviving instruments carry preferences, and concentrates the holder base, because a down round with pay-to-play provisions converts non-participating holders and leaves the participating ones proportionally larger. Three of the five sub-properties therefore fail together on a single common cause, admitting the compact statement

$$\operatorname{corr}\left( \phi_1, \phi_3 \right) \gg 0 \quad \text{and} \quad \operatorname{corr}\left( \phi_3, \phi_4 \right) \gg 0 \quad \Longrightarrow \quad \prod_{k} \phi_k \; \text{overstates the joint survival probability}$$

with the product form appropriate for a diagnostic checklist and misleading as a probability model. The article retains the product form because its function is diagnostic rather than predictive, and records the limitation here rather than concealing it.

The observation connects this article to the companion treatment of the portfolio condition. The [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] finds that four of five portfolio lines share a vehicle family and therefore supply little protection against a common-cause grounding. The present finding is the financing analogue of the same structure. In both cases an arrangement that appears to distribute risk across several independent conditions turns out to concentrate it on one, and in both cases the concentration becomes visible only in the adverse state that the observed history does not contain. The generalization worth stating is that the conditions the framework treats as separable are separable in favorable states and correlated in adverse ones, which is a property the closing article should carry forward across all ten conditions rather than only these two.

The empirical position on this section is weak and should be marked as such. No adverse-state financing round is observable in the present case, because the venture did not enter an adverse state after 2008. The section therefore reasons from the instrument set the literature documents as generally available rather than from any observed transaction, and its claims are conditional predictions rather than reconstructions. The [Iridium][research_finkelstein_sanford_2000] and [Virgin Orbit][ref_virgin_orbit_court] records supply the closest available evidence and neither involves the arrangement this article describes.

## The Contemporary Defense-Technology Venture Wave

The investor set that funded the venture across its early period subsequently articulated a broader thesis, and the resulting capital flow into the defense and national-security technology sector constitutes the principal downstream consequence of the case.

The thesis holds that ventures addressing national-security and hard-technology requirements had been systematically underfunded by a venture industry oriented toward software, and that the SpaceX outcome demonstrated the category was investable. The articulation appears in the [Andreessen Horowitz American Dynamism][ref_a16z_american_dynamism] practice, the [Founders Fund][ref_founders_fund] positioning, the [Lux Capital][ref_lux_capital] thesis, the [8VC][ref_8vc] positioning, and the [Shield Capital][ref_shield_capital] focus. The sector reporting against which the thesis can be checked appears at [Breaking Defense][ref_breaking_defense], [Defense News][ref_defense_news], and [Aviation Week][ref_aviation_week].

The demand side of the thesis is measurable in a way the supply side is not, and the article notes that the advocacy rarely cites it. Award-level obligations are published through [USAspending][ref_usaspending] and the [Federal Procurement Data System][ref_fpds], the daily award record at the [Department of Defense contract announcements][ref_dod_contracts], and the flexible instruments on which the category most depends are the other-transaction authorities at [10 United States Code 2371b][ref_10_usc_2371b] described in the [Department of Defense other-transaction guidance][ref_dod_other_transactions], which the [Government-Anchor Capital-Formation Leg article A289][related_post_a289_spacex_government_anchor_leg] treats at length. A category thesis asserting that a government customer will fund a class of ventures is testable against those records, and the article's position is that the test is available and is not generally performed.

The analytical question the article poses about the wave is whether the structural conditions that made the original case work are present in the subsequent ones. The conditions the article identifies are a realization path independent of company exit, an investor base weighted toward vehicles without a fund-life clock, and a government relationship supplying non-dilutive capital and credit enhancement at the early stage. The first condition requires a secondary market, which requires in turn a continuing supply of incoming buyers at a rising price, which is available to a small number of ventures at any time. The condition is stated compactly as

$$\left| \left\{ \text{ventures with functioning secondary markets} \right\} \right| \ll \left| \left\{ \text{ventures in the category} \right\} \right|$$

with the mechanism concentrated among a few. The joint requirement across the three conditions compounds the restriction, admitting the compact form

$$P\!\left( \text{all three conditions} \right) = P\!\left( \text{realization path} \right) \cdot P\!\left( \text{vehicle composition} \mid \cdot \right) \cdot P\!\left( \text{government relationship} \mid \cdot \right) \; \ll \; P\!\left( \text{realization path} \right)$$

with the conjunction rarer than its rarest conjunct. The implication is that the wave's capital is patient for the few ventures that attain the secondary market and is ordinary venture capital for the remainder, which is a distinction the category-level advocacy does not draw.

## The Anduril and Palantir Comparisons

The two ventures most frequently offered as the template comparisons deserve separate treatment, because they differ from the SpaceX case and from each other in ways the comparison generally elides.

The Palantir case, documented through the [Palantir investor materials][ref_palantir_ir], is the instance of a long private period followed by a direct listing rather than a conventional offering. The direct listing offers the liquidity a conventional offering gives without the capital raise or the underwriting, and it therefore constitutes a third resolution of the fund-life constraint distinct from the two the article treats. The resolutions available to a venture admit compact enumeration

$$\mathcal{R} = \left\{ \; \text{conventional listing}, \;\; \text{direct listing}, \;\; \text{acquisition}, \;\; \text{recurring private tender} \; \right\}$$

with the first three terminating the private configuration and only the fourth preserving it. The enumeration clarifies what the SpaceX arrangement purchased, which is not liquidity as such but liquidity compatible with remaining private, and the [Governance article A287][related_post_a287_spacex_governance] establishes why remaining private was the objective. The firm also adopted a multi-class structure preserving founder voting control, which the [Governance article A287][related_post_a287_spacex_governance] apparatus describes. The listing placed it inside the regime the private arrangement declines, comprising the [New York Stock Exchange Listed Company Manual][ref_nyse_listed_company_manual] standards, the [Regulation S-K][ref_sec_regulation_sk] disclosure obligations, and exposure to the [Council of Institutional Investors dual-class policy][ref_cii_dual_class] and the proxy-adviser recommendations at [Institutional Shareholder Services][ref_iss_governance] and [Glass Lewis][ref_glass_lewis]. The multi-class structure also carries index consequences under the [FTSE Russell][ref_ftse_russell] and [S and P Dow Jones Indices][ref_spdji] methodologies, which have at points restricted inclusion of firms with unequal voting rights. The case therefore demonstrates that the fund-life constraint can be resolved by listing while retaining founder control, at the cost of accepting every scrutiny mechanism the private arrangement avoids, and the article declines to characterize that trade as favorable or unfavorable because the two configurations optimize different objectives.

The Anduril case, documented through the [Anduril corporate record][ref_anduril], is the instance of a venture founded after the thesis had been articulated and funded by the investors who articulated it. The case is therefore not an independent confirmation of the thesis but a consequence of it, and the evidentiary weight it can bear is correspondingly limited. The distinction admits the compact statement

$$P\!\left( \text{funded} \mid \text{thesis held} \right) \neq P\!\left( \text{succeeds} \mid \text{funded} \right)$$

with the first quantity established by construction and the second remaining open.

The broader comparison the advocacy draws treats the three ventures as instances of a single pattern. The article's assessment is that they share an investor set and a sectoral orientation and differ on substantially every structural dimension this article treats, comprising the claim type, the vehicle composition, the realization path, and the relationship to the government channel.

## Deep Historical Comparative Precedents

The patient-private capital-formation mechanic can be compared with deep historical precedents in which private capital financed an undertaking across a horizon exceeding the ordinary commercial one.

The chartered-company form yields the earliest systematic instance and is treated from other angles in the [Governance article A287][related_post_a287_spacex_governance] and the [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience]. The capital-formation reading is that the permanent joint-stock company solved precisely the problem this article treats, by permitting an investor to realize a position through a transfer to another investor rather than through a liquidation of the underlying venture. The innovation admits the compact statement in the terms this article uses throughout

$$\text{voyage-terminated venture} \; : \; \text{realization} \equiv \text{exit} \qquad \text{against} \qquad \text{permanent joint stock} \; : \; \text{realization} \perp \text{exit}$$

with the separation this article treats as the decisive modern innovation having been accomplished in the early seventeenth century. The tender mechanism is therefore not a novel instrument but a reconstruction of a four-century-old one under conditions where the ordinary vehicle for it, namely a listed market, was deliberately declined. The [Steensgaard 1974][book_steensgaard_1974] The Asian Trade Revolution, [Stern 2011][book_stern_2011] The Company-State, and [Robins 2006][book_robins_2006] The Corporation That Changed the World treatments document the development, and the market structures that supported the transfers are treated in [Preda 2009][book_preda_2009] Framing Finance and [MacKenzie 2006][book_mackenzie_2006] An Engine Not a Camera.

The canal and railway financing of the eighteenth and nineteenth centuries contributes the instance of a private capital market financing an infrastructure with a construction period exceeding the investors' ordinary horizon, and the instance in which the mismatch produced repeated financial crises. The mismatch is the same one this article formalizes, admitting the compact statement

$$T^{\text{construction}} \gg T^{\text{subscriber horizon}} \quad \Longrightarrow \quad \text{repeated refinancing at intervals of } T^{\text{subscriber horizon}}$$

with each refinancing constituting an occasion on which the undertaking could fail for reasons unrelated to its engineering. The [Chandler 1977][book_chandler_1977] The Visible Hand, [Chandler 1962][book_chandler_1962] Strategy and Structure, [Landes 1969][book_landes_1969] The Unbound Prometheus, and [Hughes 1983][book_hughes_1983] Networks of Power treatments document the arrangements. The record is substantially less favorable than the contemporary infrastructure-finance advocacy suggests, and the reason is that the era supplied no equivalent of the transfer mechanism at the scale the undertakings required.

The Standard Oil and the late-nineteenth-century industrial consolidations supply the instance in which a retained-earnings financing displaced an external capital market entirely, documented in [Chernow 2004][book_chernow_2004] Titan. The route is the one the Category-Dominating Commercial Spinoff article A291 will treat in the present case, and it is the route that dispenses with the patience problem by dispensing with the external claim. The primary record of the consolidation and its dissolution is the [Supreme Court decision of 1911][ref_standard_oil_1911], which gives the finding of fact about the financing structure that the secondary literature paraphrases.

The two twentieth-century telecommunications settlements supply the regulated counterpart and are documented in the [consent decree of 1956][ref_att_consent_decree_1956] and the [divestiture of 1984][ref_att_divestiture_1984]. The pairing is instructive for this article because the first settlement purchased a patient capital position with a commitment to license, and the second dissolved the arrangement once the bargain was no longer politically sustainable, which establishes that a regulated revenue base is a patience mechanism with a termination risk of its own rather than a permanent substitute for the instruments this article treats.

The corporate archives of the two American firms whose long development programmes are most often compared to the present case are at the [IBM archives][ref_ibm_archives] and the [Boeing historical archives][ref_boeing_historical_archives].

The electrification and telephone build-outs supply the instance of a regulated monopoly's access to a patient bond market on the specific strength of a regulated revenue base. The [Hughes 1983][book_hughes_1983], [Nye 1990][book_nye_1990] Electrifying America, [Temin and Galambos 1987][book_temin_galambos_1987] The Fall of the Bell System, [Wu 2010][book_wu_2010] The Master Switch, and [Levin 2010][book_levin_2010] The Wires That Bind treatments document the arrangements. The case establishes that a regulated revenue base substitutes for the patience mechanisms this article treats, at the cost of the regulatory constraint.

The foundation-ownership form supplies the one historical arrangement that solves the duration problem outright rather than by mechanism, and it is the comparison the article regards as most instructive because the [Governance article A287][related_post_a287_spacex_governance] establishes that the present case does not satisfy it. The [Carl Zeiss Stiftung][ref_carl_zeiss_stiftung] statute of 1889 and the [Zeiss corporate record][ref_zeiss_corporate], the [Robert Bosch Stiftung][ref_bosch_stiftung] and the [Bosch corporate record][ref_bosch_company], and the [Novo Nordisk Foundation][ref_novo_nordisk_foundation] with its holding company at [Novo Holdings][ref_novo_holdings] under the supervisory regime the [Danish Business Authority][ref_danish_business_authority] administers each place ownership in an entity with no term, no beneficiary entitled to demand realization, and no successor problem. The duration condition is satisfied by construction rather than by a recurring transaction. The arrangement this article describes purchases a comparable effect through a mechanism that must be re-executed every six months and that is unavailable in adverse states, which is a materially weaker guarantee obtained at materially lower cost in surrendered ownership.

The semiconductor and early computing financings supply the instance most proximate to the present case in its institutional form. The [Berlin 2005][book_berlin_2005] The Man Behind the Microchip, [Malone 2014][book_malone_2014] The Intel Trinity, [Lecuyer 2006][book_lecuyer_2006] Making Silicon Valley, [Riordan and Hoddeson 1997][book_riordan_hoddeson_1997] Crystal Fire, [Saxenian 1994][book_saxenian_1994] Regional Advantage, [Kenney 2000][book_kenney_2000] Understanding Silicon Valley, and [Klepper 2016][book_klepper_2016] Experimental Capitalism document the emergence of the venture form itself. The medieval and early-modern partnership forms supply the deepest available precedent for the problem of a capital supplier whose horizon is shorter than the undertaking. The Venetian colleganza and the Genoese commenda documented in [Lane 1934][book_lane_1934] and [Grief 2006][book_grief_2006] Institutions and the Path to the Modern Economy terminated at the conclusion of a single voyage precisely because no mechanism existed for transferring a partial interest, and [de Vries and van der Woude 1997][book_devries_vanderwoude_1997] traces the transition to durable forms. The sequence establishes that the transfer mechanism is the historically decisive innovation and that its absence, not any shortage of capital or of willingness, is what confined earlier commercial undertakings to horizons a single sponsor could span.

The modern project-finance apparatus treated in [Grimsey and Lewis 2004][book_grimsey_lewis_2004] and [Yescombe 2007][book_yescombe_2007] supplies the contemporary institutional answer to the same problem in the infrastructure setting, through a special-purpose vehicle whose capital structure is matched to a contracted revenue stream. The form is unavailable to a development-stage venture for the reason the article's claim-type analysis identifies, namely that the structure presupposes a contracted revenue stream against which to size the obligations, and a venture developing a capability that does not yet exist has none. The observation identifies exactly what the government-anchor leg supplied and why it arrived first in the sequence.

The aircraft industry provides the closest sectoral precedent for a long-horizon privately financed development programme, documented in [Bilstein 1996][book_bilstein_1996], [Bilstein 2001][book_bilstein_2001], [Newhouse 1982][book_newhouse_1982] The Sporty Game, [Newhouse 2007][book_newhouse_2007], [Serling 1992][book_serling_1992], [Francillon 1979][book_francillon_1979], and [Hounshell 1984][book_hounshell_1984]. The relevant finding is that programme-scale commitments repeatedly exceeded the sponsoring firm's capacity to absorb failure and were sustained by government orders, which is the same conjunction the present series treats and which suggests the pattern is sectoral rather than singular.

The corporate research laboratory offers the precedent for patience obtained through monopoly rents rather than through capital-market instruments, documented in [Gertner 2012][book_gertner_2012] The Idea Factory, [Hiltzik 1999][book_hiltzik_1999] Dealers of Lightning, [Kearns and Nadler 1992][book_kearns_nadler_1992], and [Mowery and Rosenberg 1998][book_mowery_rosenberg_1998]. The arrangement produced long horizons without any external claim at all, and it dissolved when the rents did, which is the reason the article treats retained-earnings financing as a patience mechanism with a distinct termination risk rather than as an unconditional improvement.

The state-directed industrial finance of the postwar East Asian economies gives the comparison in which the duration problem was solved by policy rather than by instrument, documented in [Johnson 1982][book_johnson_1982], [Amsden 1989][book_amsden_1989], [Wade 1990][book_wade_1990], [Evans 1995][book_evans_1995], and [Woo-Cumings 1999][book_woo_cumings_1999]. The comparison is instructive because it achieves the longest horizons of any arrangement in this survey and does so by removing the capital supplier's option to withdraw entirely, which is the limit case of the mechanism this article describes and which carries the accountability cost the critical literature identifies.

The relevant observation is that the form was designed for a development horizon of a few years, and that substantially every difficulty this article treats follows from applying it to a horizon it was not designed for. The design point and the application admit the compact contrast

$$T^{\text{design point of the venture form}} \approx 3 \text{ to } 7 \text{ years} \qquad \text{against} \qquad T^{\text{holding required}} > 18 \text{ years}$$

with the instrument applied at approximately three times the horizon for which its terms were calibrated. The observation reframes the article's subject matter. The question is not why the investors were unusually patient but why an instrument calibrated for a semiconductor startup was the one available to a launch venture at all, and the answer is that no alternative instrument existed in the market the venture could reach.

## Historiographical Gap and Recent Scholarship

The scholarly literature bearing on the patient-private leg is mature on the fund mechanics and substantially absent on the case, and the asymmetry has a structural cause. The entrepreneurial-finance literature's empirical base is drawn from datasets of realized outcomes, and a firm that has neither exited nor failed appears in none of them.

### Primary Source Documentation

The primary record comprises the securities-law materials at the [Securities Act private-placement exemption][ref_securities_act_4a2], the [Regulation D][ref_reg_d] and [Rule 506][ref_rule_506] provisions, the [Rule 701][ref_rule_701] and [Rule 144][ref_rule_144] provisions, the [Exchange Act registration threshold][ref_exchange_act_12g] and [Rule 12g-1][ref_rule_12g1], the [Jumpstart Our Business Startups Act of 2012][ref_jobs_act_2012], the [Rule 13e-4][ref_rule_13e4] and [Regulation 14E][ref_reg_14e] tender provisions, and the [Regulation S-K][ref_sec_regulation_sk] disclosure regime that a listed issuer would face. The fund-structure materials comprise the [Delaware Limited Partnership Act][ref_delaware_lp_act], the [Investment Company Act][ref_investment_company_act] and [Investment Advisers Act][ref_investment_advisers_act] provisions, and the limited-partner standards the [Institutional Limited Partners Association][ref_ilpa] publishes. The filing record is accessible through the [Securities and Exchange Commission EDGAR][ref_sec_edgar] system and the [Form D notices][ref_sec_form_d].

### Entrepreneurial-Finance Literature

The literature is surveyed in the Cross-Disciplinary Framings section. The principal works are [Sahlman 1990][research_sahlman_1990], [Gompers 1995][research_gompers_1995], [Lerner 1994][research_lerner_1994_syndication], [Kaplan and Stromberg 2003][research_kaplan_stromberg_2003], [Kaplan and Stromberg 2004][research_kaplan_stromberg_2004], [Gompers and Lerner 2001][book_gompers_lerner_2001], [Metrick and Yasuda 2011][book_metrick_yasuda_2011], [Lerner 2009][book_lerner_2009], [Kortum and Lerner 2000][research_kortum_lerner_2000], [Hall and Lerner 2010][research_hall_lerner_2010], and [Ewens and Farre-Mensa 2020][research_ewens_farre_mensa_2020]. The gap the literature exhibits with respect to the present case is the survivorship structure of its data. The returns literature is estimated on realized positions, and a mechanism whose function is to permit indefinite non-realization is invisible to it by construction.

### Industry and Practitioner Record

The industry-level record is published by the [National Venture Capital Association][ref_nvca], with the benchmark data at the [Cambridge Associates][ref_cambridge_associates] and the transaction data at the [PitchBook][ref_pitchbook] and, for the sector, at the [Space Capital][ref_space_capital] and [BryceTech][ref_bryce_tech] publications. The participant record appears at the [Founders Fund][ref_founders_fund], the [Draper Fisher Jurvetson][ref_dfj] archive, the [Valor Equity Partners][ref_valor_equity], the [Sequoia][ref_sequoia], the [Baillie Gifford][ref_baillie_gifford], and for the subsequent wave at the [Andreessen Horowitz American Dynamism][ref_a16z_american_dynamism], [Lux Capital][ref_lux_capital], [8VC][ref_8vc], and [Shield Capital][ref_shield_capital] publications. The practitioner literature comprising [Thiel 2014][book_thiel_2014], [Ries 2011][book_ries_2011], [Blank 2013][book_blank_2013], and [Moore 1991][book_moore_1991] is cited as evidence about the decision environment.

### Case-Study and Biographical Literature

The case-study record appears in the [Anadol Cohen and Ferrari 2018][research_anadol_cohen_2018] treatment, the [Stanford Graduate School of Business case collection][ref_stanford_spacex_case], and the [Wharton knowledge repository][ref_wharton_spacex_case]. The biographical record in [Berger 2021][book_berger_2021], [Berger 2024][book_berger_2024], [Vance 2015][book_vance_2015], [Isaacson 2023][book_isaacson_2023], [Davenport 2018][book_davenport_2018], and [Fernholz 2018][book_fernholz_2018] supplies substantially the entire narrative account of the early rounds, and the accounts are simultaneously the best available and the most interested.

### Critical and Skeptical Literature

A critical literature reads the arrangement as an instance of a broader shift of economic activity into private markets beyond the reach of public disclosure and public accountability. The position draws on [Krippner 2011][book_krippner_2011] Capitalizing on Crisis, [Ho 2009][book_ho_2009] Liquidated, [Srnicek 2017][book_srnicek_2017] Platform Capitalism, [Zuboff 2019][book_zuboff_2019] The Age of Surveillance Capitalism, [Foster and McChesney 2011][book_foster_mcchesney_2011] The Endless Crisis, and [Melman 1970][book_melman_1970] Pentagon Capitalism, with the governance dimension in [Bebchuk and Kastiel 2017][research_bebchuk_kastiel_2017] and [Berle and Means 1932][book_berle_means_1932]. The concern is that the mechanisms this article describes as manufacturing patience equally manufacture opacity, and that the two are the same mechanism viewed from different positions. The concern is well founded and the article does not resolve it. The institutional expression of the concern appears in the [Council of Institutional Investors][ref_cii] positions and the [Rule 14a-8][ref_rule_14a8] shareholder-proposal channel, neither of which reaches a firm that never lists, and the governance scholarship at the [European Corporate Governance Institute][ref_ecgi] and the [Harvard Law School Forum on Corporate Governance][ref_harvard_corpgov_forum] documents the resulting accountability gap.

### Comparative Contemporary Configurations

The mission-directed venture attempting to bind itself against later capital capture has produced several contemporary arrangements that supply a comparison set for the present case without being instances of it. The [OpenAI charter][ref_openai_charter] and the subsequent restructuring recorded in the [OpenAI news record][ref_openai_news] and the [Microsoft news record][ref_microsoft_news] constitute the most-discussed failure of such a binding, which the [Governance article A287][related_post_a287_spacex_governance] treats as its principal negation case. The [Anthropic long-term benefit trust][ref_anthropic_ltbt] is a distinct attempt at the same problem through a trust rather than a nonprofit parent. The founder-control comparisons among listed technology firms are documented at [Meta investor relations][ref_meta_ir], [Snap investor relations][ref_snap_ir], and [Tesla investor relations][ref_tesla_ir]. None of these arrangements resolves the fund-life constraint this article treats, because each concerns the allocation of control rather than the duration of the supplying vehicle, and the article records them to mark the boundary between the two problems, which the commentary routinely conflates.

### Corporate Finance and Capital Structure Literature

The corporate-finance literature bearing on the article is mature and was developed for the listed firm, which is the source of its principal limitation here. The capital-structure and agency line runs from [Myers 1977][research_myers_1977] and [Jensen and Meckling 1976][research_jensen_meckling_1976] through [Jensen 1986][research_jensen_1986], [Fama and Jensen 1983][research_fama_jensen_1983], [Harris and Raviv 1988][research_harris_raviv_1988], [Shleifer and Vishny 1997][research_shleifer_vishny_1997], [Hart 1988][research_hart_1988], [Hart 1995][book_hart_1995], and [Tirole 2006][book_tirole_2006]. The diversification and internal-capital-market line runs from [Lewellen 1971][research_lewellen_1971] through [Amihud and Lev 1981][research_amihud_lev_1981], [Lang and Stulz 1994][research_lang_stulz_1994], [Gertner Scharfstein and Stein 1994][research_gertner_scharfstein_stein_1994], [Berger and Ofek 1995][research_berger_ofek_1995], [Stein 1997][research_stein_1997], [Scharfstein and Stein 2000][research_scharfstein_stein_2000], [Rajan Servaes and Zingales 2000][research_rajan_servaes_zingales_2000], and [Montgomery 1994][research_montgomery_1994]. The asset-pricing baseline is at [Markowitz 1952][research_markowitz_1952], [Markowitz 1959][book_markowitz_1959], [Sharpe 1964][research_sharpe_1964], and [Lintner 1965][research_lintner_1965]. The gap with respect to the present case is that substantially the entire empirical apparatus requires a market price, and the arrangement this article describes exists precisely to avoid producing one.

### Law and Finance Literature

The comparative and legal literature yields the account of what the control configuration cost and what it bought, and it is the literature the [Governance article A287][related_post_a287_spacex_governance] engages most directly. The principal works are [La Porta Lopez-de-Silanes Shleifer and Vishny 1998][research_laporta_et_al_1998], [Roe 1994][book_roe_1994], [Easterbrook and Fischel 1991][book_easterbrook_fischel_1991], [Hansmann 1996][book_hansmann_1996], [Berle and Means 1932][book_berle_means_1932], [Manne 1965][research_manne_1965], [Grossman and Hart 1988][research_grossman_hart_1988], [DeAngelo and DeAngelo 1985][research_deangelo_deangelo_1985], [Bebchuk Kraakman and Triantis 2000][research_bebchuk_kraakman_triantis_2000], [Bebchuk and Kastiel 2017][research_bebchuk_kastiel_2017], [Gompers Ishii and Metrick 2003][research_gompers_ishii_metrick_2003], and [Gompers Ishii and Metrick 2010][research_gompers_ishii_metrick_2010]. The gap is jurisdictional. The literature is overwhelmingly concerned with the listed firm in common-law jurisdictions, and the arrangement here is a private firm whose most instructive comparators are the civil-law foundation structures the Deep Historical Comparative Precedents section treats.

### Space Economics and Policy Literature

The sector literature is well developed on programme history and thin on financing structure, which is the asymmetry that motivates this article. The economics is at [Weinzierl 2018][research_weinzierl_2018], [Hertzfeld 2002][research_hertzfeld_2002], and [Adilov Alexander and Cunningham 2018][research_adilov_et_al_2018]. The policy and programme histories are at [Launius 1994][book_launius_1994], [Launius 2004][book_launius_2004], [McCurdy 1994][book_mccurdy_1994], [Handberg 1994][book_handberg_1994], [Logsdon 1970][book_logsdon_1970], [McDougall 1985][book_mcdougall_1985], and [Heppenheimer 1999][book_heppenheimer_1999], with the mission-architecture advocacy at [Zubrin 1996][book_zubrin_1996] and [Zubrin 2019][book_zubrin_2019]. Substantially none of this literature treats the fund-life constraint, and the article's contribution is to supply that treatment rather than to correct anything the literature asserts.

### Mission-Oriented Innovation Policy Literature

The policy literature contributes the framework the series adopts and is the literature most likely to draw the wrong lesson from this case. It comprises [Mazzucato 2013][book_mazzucato_2013], [Mazzucato 2021][book_mazzucato_2021], [Bonvillian 2018][research_bonvillian_2018], [Nelson 1959][research_nelson_1959], [Nelson 1993][book_nelson_1993], [Arrow 1962][research_arrow_1962], [Freeman and Soete 1997][research_freeman_soete_1997], [Mowery and Rosenberg 1998][book_mowery_rosenberg_1998], and [Ruttan 2006][book_ruttan_2006]. The wrong lesson available from this case is that the private capital was the decisive ingredient. The article's position is that the private capital was necessary and that the structural conditions permitting it to be patient were the scarce element, and that a policy prescription aimed at increasing capital supply without addressing those conditions would not reproduce the outcome.

### Business and Economic History Literature

The historical literature yields the comparison set and the base rates the contemporary commentary lacks. It comprises [Chandler 1962][book_chandler_1962], [Chandler 1977][book_chandler_1977], [Chandler 1990][book_chandler_1990] Scale and Scope, [Landes 1969][book_landes_1969], [Hughes 1983][book_hughes_1983], [Hounshell 1984][book_hounshell_1984], [North 1990][book_north_1990], [Grief 2006][book_grief_2006], [Lane 1934][book_lane_1934], [de Vries and van der Woude 1997][book_devries_vanderwoude_1997], [Steensgaard 1974][book_steensgaard_1974], [Stern 2011][book_stern_2011], [Robins 2006][book_robins_2006], [Chernow 2004][book_chernow_2004], [Nevins 1954][book_nevins_1954], [Fligstein 2001][book_fligstein_2001], and [Perez 2002][book_perez_2002] Technological Revolutions and Financial Capital. The [Perez 2002][book_perez_2002] treatment is the most directly relevant of these and is under-cited in the contemporary discussion, because it provides a periodization in which the availability of patient capital for a given technology class is a function of where the class sits in an installation and deployment cycle rather than a constant of the financial system.

### Trade Press and Journalistic Record

Substantially every quantitative claim in this article rests on the trade-press and business-press reconstruction appearing in [SpaceNews][ref_spacenews], [Ars Technica space coverage][ref_arstechnica_space], [Payload][ref_payload], [Payload Research][ref_payload_research], [The Space Review][ref_the_space_review], [Bloomberg][ref_bloomberg], the [New York Times][ref_nyt], the [Wall Street Journal][ref_wsj], and the [Washington Post][ref_washington_post].

## Contemporary Comparative Landscape

The contemporary landscape for the patient-private leg differs from that of the preceding legs because the mechanism the article identifies is available to a small number of ventures rather than to a category.

Blue Origin occupies the configuration in which the patient-private leg is unnecessary, because the single-funder arrangement the [Governance article A287][related_post_a287_spacex_governance] treats contributes the capital directly from a balance sheet with no fund life and no realization requirement. The configuration satisfies the duration condition trivially and dispenses with the dilution entirely, at the cost of the dependence on a single source. The trade admits the compact statement in the terms the article uses

$$T^{\text{vehicle}} \to \infty \quad \text{and} \quad \delta_n = 0 \quad \text{purchased at} \quad H = 1$$

with the configuration attaining the duration and dilution objectives outright while failing the dispersion sub-property completely. The configuration is therefore the exact complement of the OneWeb failure, holding the concentration constant at its maximum and varying the supplier's willingness to continue. The record appears at the [Blue Origin press releases][ref_blue_origin_press].

Rocket Lab took the conventional route, listing publicly and thereby resolving the fund-life constraint through the ordinary mechanism at the ordinary cost in disclosure and quarterly scrutiny. The record appears at the [Rocket Lab press releases][ref_rocket_lab_press] and in the periodic filings retrievable through [Securities and Exchange Commission EDGAR][ref_sec_edgar]. The comparison against the SpaceX route is the most direct available within the sector, because the two firms entered at comparable dates into the same market with the same customer set and resolved the same constraint by opposite means. The comparison is nonetheless confounded by scale, since the capital requirement the larger programme faced was of a different order and may itself explain the divergent choice.

The comparison set extends beyond the domestic entrants. [Arianespace][ref_arianespace] operates under a governmental-shareholder arrangement in which the duration question is answered by state ownership rather than by any market mechanism, [Axiom Space][ref_axiom_space] pursues the private-station line under conventional venture financing, and the broader European entrant record appears at [European Spaceflight][ref_european_spaceflight] with the sector-wide launch and licensing record at the [Federal Aviation Administration Office of Commercial Space Transportation][ref_faa_ast], the [Space Force National Security Space Launch programme][ref_space_force_nssl], and the technical reporting at [NASASpaceflight][ref_nasaspaceflight] and [Space Policy Online][ref_space_policy_online].

The United Launch Alliance is a joint venture of listed parents and therefore raises no external capital of its own, documented through the [United Launch Alliance news][ref_ula_press] and the parent disclosures at the [Boeing press releases][ref_boeing_press] and the [Northrop Grumman press releases][ref_northrop_grumman_press].

The broader entrant set faces the ordinary constraint without the secondary-market relief, which is the structural reason the sector exhibits a pattern of ventures raising successive rounds at rising valuations until a round fails and the venture is sold or wound up. The survival pattern can be written as

$$P\!\left( \text{survive to round } N \right) = \prod_{n=1}^{N} \left( 1 - q_n \right) \qquad \text{with} \qquad q_n = P\!\left( \text{round } n \text{ fails to close} \right)$$

with the product declining geometrically in the number of rounds a venture must raise. A venture requiring a longer development period requires a larger $N$ and therefore faces a lower survival probability for a reason having nothing to do with its engineering. The mechanism this article treats operates by removing the rounds from the product rather than by improving the per-round probability. The pattern is visible in the record the [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] documents.

## Comparative Cross-Sectional Analysis

The patient-private capital-formation leg can be applied to the venture set as a cross-sectional scoring exercise across the five sub-properties the pattern-extraction section states. The closure vector has the form

$$\boldsymbol{\phi}_j^{\text{patient-private}} \in \{0,1\}^{5}$$

with each venture's vector indicating the satisfaction status across the claim-type, vehicle-duration, realization-path, investor-dispersion, and control-preservation sub-properties.

SpaceX exhibits closure on all five. Blue Origin exhibits closure on the claim-type, vehicle-duration, and control-preservation sub-properties, with the realization-path sub-property inapplicable and the investor-dispersion sub-property failing by construction. Rocket Lab exhibits closure on the claim-type, realization-path, and investor-dispersion sub-properties and non-closure on the control-preservation sub-property. Iridium exhibited non-closure on the claim-type sub-property, which was decisive. OneWeb exhibited closure on the claim-type sub-property and non-closure on the investor-dispersion and realization-path sub-properties, which was jointly decisive.

The scoring assembles into a matrix whose rows are the ventures and whose columns are the sub-properties in the order the pattern-extraction section states

$$\begin{array}{lccccc}
 & \phi_1 & \phi_2 & \phi_3 & \phi_4 & \phi_5 \\
\text{SpaceX} & 1 & 1 & 1 & 1 & 1 \\
\text{Blue Origin} & 1 & 1 & \dagger & 0 & 1 \\
\text{Rocket Lab} & 1 & 1 & 1 & 1 & 0 \\
\text{Iridium} & 0 & \ast & \ast & \ast & \ast \\
\text{OneWeb} & 1 & \ast & 0 & 0 & \ast
\end{array}$$

with $\dagger$ marking a sub-property the configuration renders inapplicable rather than satisfied or failed, and $\ast$ marking a cell the available record does not establish. The empty cells are reported rather than imputed, and their number is the reason the section is a scoring exercise rather than an estimation. A reader should note that the two failed cases carry the most missing cells, which is precisely the pattern a survivorship problem produces.

The cross-sectional pattern indicates that the realization-path sub-property is the one that discriminates most sharply and the one least frequently discussed. The correlation with the outcome can be stated as

$$\operatorname{corr}_j\!\left( \phi_{j,3}^{\text{realization path}}, \; \text{survival} \right) \gg \operatorname{corr}_j\!\left( \phi_{j,2}^{\text{vehicle duration}}, \; \text{survival} \right)$$

with the existence of a realization path independent of company exit carrying more information than the nominal patience of the vehicles supplying the capital. The finding is the article's central empirical claim.

## Data Sources and Reconstruction Methodology

The article draws on primary and secondary sources, and its evidentiary position is the weakest in the series.

The primary-source layer comprises the securities-law and fund-structure materials identified in the Historiographical Gap section. The materials are complete and authoritative for the legal framework and supply substantially nothing about the particular transactions.

The secondary-source layer comprises the trade-press and participant record, which offers substantially every quantity in the article.

The reconstruction methodology proceeds by taking the Form D filing record as the spine, which establishes the existence and the approximate size of rounds without establishing the terms, and by using the trade-press reports of tender prices to establish the valuation sequence. The two sources are partially independent, which permits a limited cross-check on the round sizes and none on the terms.

The empirical-record limitations are severe and comprise the following. The round terms including the liquidation preferences, the protective provisions, and the anti-dilution mechanics are entirely unknown, and each one materially affects the economics the article describes. The investor identities are partially known and the position sizes are not. The cumulative capital raised is a reconstruction. The valuations are transaction prices in a thin market rather than market valuations. The consequence is that the article's structural claims are substantially better supported than its quantitative ones, and the reader should read the numbers as illustrative of a pattern rather than as measurements.

## Alternative Analytical Frameworks

The patient-private capital-formation framing the article develops is one of several analytical frameworks the surrounding literature applies.

The conviction framing, which is the framing the participants themselves employ, treats the outcome as attributable to investor belief in the mission and founder. The framing is not refuted by the evidence and is incomplete, because it gives no account of how the belief was converted into a contractual capacity to act on it. The incompleteness may be stated compactly

$$\text{observed patience} = \underbrace{\text{willingness}}_{\text{conviction framing}} \; \wedge \; \underbrace{\text{capacity}}_{\text{structural framing}}$$

with the conjunction requiring both conjuncts and the conviction account supplying only the first. The article treats the structural framing as a complement rather than as a replacement, and the OneWeb case is the demonstration that the first conjunct alone is insufficient.

The agency framing developed in [Jensen and Meckling 1976][research_jensen_meckling_1976], [Fama and Jensen 1983][research_fama_jensen_1983], [Jensen 1986][research_jensen_1986], and [Shleifer and Vishny 1997][research_shleifer_vishny_1997] treats the general partner as an agent of the limited partners and the fund-life constraint as a bonding mechanism that exists precisely to prevent the general partner from holding indefinitely. Under the framing, the mechanism this article describes as manufacturing patience is a circumvention of a control designed to protect the limited partners, and whether it benefits them is an empirical question the article cannot answer. The question admits compact statement without admitting resolution

$$\mathbb{E}\left[ u^{\text{LP}} \mid \text{tender available} \right] \; \gtrless \; \mathbb{E}\left[ u^{\text{LP}} \mid \text{wind-up enforced} \right]$$

with the ordering undetermined on the available evidence. The left side benefits from the continued appreciation and suffers from the loss of the bonding the term supplied. The article notes that the general partner selects when to invoke the mechanism and the limited partners do not, which is an asymmetry the agency framing predicts will be resolved in the general partner's favor. The scholarly and practitioner apparatus through which the framing is currently argued is collected at the [European Corporate Governance Institute][ref_ecgi] and the [Harvard Law School Forum on Corporate Governance][ref_harvard_corpgov_forum], with the investor-side positions at the [Council of Institutional Investors][ref_cii].

The comparative-institutional framing asks whether the arrangement is a feature of United States corporate law specifically or of the venture form generally, and the answer bears on how far the article's finding travels. The [United Kingdom Companies Act 2006][ref_uk_companies_act_2006] imposes a pre-emption regime that constrains the issuance sequence this article describes, the German [Aktiengesetz][ref_german_aktiengesetz] embeds codetermination and a two-tier board that alter the control calculus entirely, and the [European Union Shareholder Rights Directive][ref_eu_shareholder_rights_directive] imposes engagement obligations on institutional holders that have no United States analogue. The article's finding is therefore jurisdiction-bound to a degree its abstract statement conceals, and a reader applying the pattern outside the United States should treat the control-preservation sub-property as the one most likely to fail for reasons unrelated to the financing.

The market-microstructure framing treats the tender mechanism as a thin periodic auction whose price is set by the issuer rather than discovered, and it raises the question whether the reported valuations bear the informational content that a public market price would. The concern is stated compactly as

$$P_t^{\text{tender}} = P^{\text{issuer-set}} \quad \text{subject only to} \quad \sum_{j} d_j\big( P_t \big) \geq \sum_{i} q_i$$

with the price constrained by a participation condition rather than determined by a market-clearing one. A range of prices satisfies the inequality and the issuer selects within it, so that the reported valuation is an upper region of a feasible set rather than a point estimate of a value. The framing yields the most serious challenge to the quantitative material in this article and is the reason the Data Sources section states the limitation explicitly.

The behavioral framing developed in [Kahneman and Tversky 1979][research_kahneman_tversky_1979], [Tversky and Kahneman 1992][research_tversky_kahneman_1992], [Kahneman 2011][book_kahneman_2011], and [Staw 1976][research_staw_1976] treats the continued participation as an escalation, and it generates the prediction that the participation should be insensitive to adverse information. The prediction is not distinguishable from the favorable reading on the available evidence.

The financial-sociology framing developed in [MacKenzie 2006][book_mackenzie_2006], [Ho 2009][book_ho_2009], [Zaloom 2006][book_zaloom_2006], [Preda 2009][book_preda_2009], and [Krippner 2011][book_krippner_2011] treats the horizon norms as institutionally constructed and supplies the strongest support for the article's central claim.

The incomplete-contracts framing developed in [Grossman and Hart 1986][research_grossman_hart_1986], [Hart and Moore 1990][research_hart_moore_1990], [Hart 1988][research_hart_1988], [Williamson 1985][book_williamson_1985], and [Klein Crawford and Alchian 1978][research_klein_crawford_alchian_1978] treats the arrangement as a response to the impossibility of contracting on patience directly. Under the framing the recurring tender is not a liquidity facility but a substitute for a contractual term that could not be written, because the contingencies over an eighteen-year horizon are not describable in advance. The framing generates the prediction that the arrangement should be least stable exactly where the parties' interests diverge most, which is the adverse state, and the Adverse-State Financing Regime section above is the article's development of that prediction.

The portfolio-theory framing developed in [Markowitz 1952][research_markowitz_1952], [Sharpe 1964][research_sharpe_1964], [Lintner 1965][research_lintner_1965], and [Lewellen 1971][research_lewellen_1971] treats the arrangement as value-destroying from the capital supplier's standpoint, on the ground that a holder unable to rebalance bears idiosyncratic risk for which no market compensates. The framing is correct on its own terms and the article accepts it. What the framing does not supply is any account of who would have financed the undertaking had every supplier acted on it, and the article's position is that the arrangement transfers value from the capital supplier to the undertaking rather than creating it, which is a description the participants would likely dispute and the framing supports.

The market-design framing developed in [Myerson 1981][research_myerson_1981], [McAfee and McMillan 1988][book_mcafee_mcmillan_1988], and [Milgrom 2004][book_milgrom_2004] treats the tender as a recurring restricted-participation sale and asks what price and information properties follow from the participation rule. The framing sharpens the microstructure objection by identifying the mechanism through which issuer control of participation translates into control of the reported price, and it contributes the testable implication that widening participation should reduce the reported valuation, which no party to the arrangement has an incentive to test.

The political-economy and developmental-state framing developed in [Mazzucato 2013][book_mazzucato_2013], [Johnson 1982][book_johnson_1982], [Amsden 1989][book_amsden_1989], [Wade 1990][book_wade_1990], and [Evans 1995][book_evans_1995] treats the private patience this article describes as derivative of a public commitment rather than as an independent achievement. Under the framing the government-anchor leg supplied the risk reduction that made the private terms attainable, and describing the private leg as the locus of patience mistakes the transmission for the source. The article regards the framing as substantially correct for the period through 2008 and as progressively less accurate afterward, and the [Government-Anchor Capital-Formation Leg article A289][related_post_a289_spacex_government_anchor_leg] documents the reversal in which the firm began investing ahead of the government requirement.

The organizational-capability framing developed in [Penrose 1959][book_penrose_1959], [Teece Pisano and Shuen 1997][research_teece_pisano_shuen_1997], [Teece 1986][research_teece_1986], [March 1991][research_march_1991], and [Nelson and Winter 1982][book_nelson_winter_1982] treats capital as the non-binding constraint and managerial attention as the binding one. Under the framing the entire subject of this article is a solved problem after some date and the interesting question moves elsewhere, which the [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] develops. The framing is a useful corrective to the financing-centric reading this article necessarily adopts.

The evolutionary framing developed in [Nelson and Winter 1982][book_nelson_winter_1982], [Metcalfe 1998][book_metcalfe_1998], [Klepper 1996][research_klepper_1996], and [Klepper 2010][research_klepper_2010] supplies the selection caution, which is unusually sharp here because the mechanism the article identifies operates only in favorable states and is therefore present in substantially every surviving case and absent from substantially every failed one by construction. The hazard admits the compact statement

$$P\!\left( \text{mechanism observed} \mid \text{survived} \right) \approx 1 \qquad \text{while} \qquad P\!\left( \text{survived} \mid \text{mechanism observed} \right) \; \text{remains unidentified}$$

with the first quantity carrying no information about the second. The caution bears directly on the article's central empirical claim in the Comparative Cross-Sectional Analysis section, and the claim should be read as a structural argument supported by a negation case rather than as an estimated effect.

## Pattern Extraction

The patient-private capital-formation pattern that the SpaceX case exhibits admits the following abstract statement without naming any downstream application. A mission-directed technology venture achieves the patient-private capital-formation closure when it raises equity from a dispersed base of holders whose vehicles have no binding term, in a structure that permits any holder to realize a position by transfer rather than by forcing a liquidity event on the venture, without surrendering the control the mission requires.

The abstract mechanic requires joint satisfaction of five sub-properties, admitting the compact conjunctive form

$$\Phi^{\text{patient-private}} = \prod_{k=1}^{5} \phi_k, \qquad \phi_k \in \{0,1\}$$

First, the claim must be residual and undated rather than fixed in amount and date. Debt applied to a development programme with an uncertain schedule converts a delay into a default.

Second, the supplying vehicles must have terms exceeding the required holding period, which in practice means shifting the investor base toward vehicles with no stated term at all.

Third, a realization path independent of the venture's own liquidity event must exist. This is the sub-property that does the work, and it is the one the conviction account omits entirely.

Fourth, the holder base must be dispersed, so that no single withdrawal is terminal and so that no coalition demanding exit assembles cheaply.

Fifth, the control configuration must survive the cumulative dilution, which is a governance property and not a financing one.

The five are stated as a conjunction and written as a product, and both the statement and the notation carry an independence assumption the Adverse-State Financing Regime section shows to be false. An adverse state withdraws the realization path, degrades the claim type through the preference structure that adverse-state instruments carry, and concentrates the holder base through the participation provisions those instruments impose. Three of the five therefore fail together on a single common cause. The product form should be read as a diagnostic checklist, in which each component is a question worth asking separately, and not as a probability model, in which the components could be multiplied. A reader estimating the likelihood that a candidate venture satisfies all five should expect the joint probability to be substantially below the product of the marginals.

The mechanic admits a diagnostic procedure stated as an ordered test vector

$$\tau = \left( \text{claim residual}, \;\; T^{\text{vehicle}} \geq T^{\text{holding}}, \;\; \text{realization} \perp \text{exit}, \;\; \text{base dispersed}, \;\; v^{\text{founder}} > \tfrac{1}{2} \right)$$

with the third component the one a candidate case will usually fail and the one an assessment will usually not examine.

The mechanic carries a limitation the statement should not conceal. The realization path exists only where incoming buyers appear at a rising price, which is to say only where the venture's prospects are improving. The third component of the test vector is therefore not a fixed property of the arrangement but a state-contingent one, admitting the compact restatement

$$\tau_3(t) = \mathbf{1}\left[ \mathbb{E}_t\left[ V_{t+1} \right] > V_t \right] \qquad \text{rather than} \qquad \tau_3 = \text{constant}$$

with the component that does the most work being the one least stable across states. The mechanism therefore provides patience in good states and none in bad ones, which is the opposite of what the word patience ordinarily connotes. A venture relying on it has not obtained capital that will wait through difficulty. It has obtained capital that need not leave during success.

## Cross-References to the Series

The article back-references the [series opener][related_post_a281_spacex_framing] for the seven-plus-three framework and the near-death period at which the first external capital arrived. The article back-references the [Value Gradient article A282][related_post_a282_spacex_value_gradient] for the vehicle progression the capital financed and for the Iridium contrast. The article back-references the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] for the December 2008 award that altered the risk profile the subsequent private investors evaluated. The article back-references the [Value Capture article A284][related_post_a284_spacex_value_capture] for the business line the 2015 round was underwriting. The article back-references the [Decomposability article A285][related_post_a285_spacex_decomposability] for the rung structure that made intermediate progress legible to investors. The article back-references the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] for the application breadth that supported the valuation sequence. The article back-references the [Governance article A287][related_post_a287_spacex_governance] for the control configuration the dilution had to leave intact and for the tender mechanism treated there from the control side. The article back-references the [Portfolio Patience article A288][related_post_a288_spacex_portfolio_patience] for the line structure across which the capital was deployed. The article back-references the [Government-Anchor Capital-Formation Leg article A289][related_post_a289_spacex_government_anchor_leg] for the non-dilutive channel with which this one interacts multiplicatively.

The article forward-references the Category-Dominating Commercial Spinoff article A291, which treats the third leg and the retained-earnings channel that ultimately displaces the need for this one, and the closing article A292, which synthesizes across the framework.

The article cross-references the existing published corpus including the [Why Startups Actually Fail article A167][related_post_a167_startup_failure], the [What a Patent Is and Is Not article A161][related_post_a161_patent_intro], the [Patents Trade Secrets and the Disclosure Tradeoff article A164][related_post_a164_patents_trade_secrets], the [Money Behind an SBIR or STTR Award article A140][related_post_a140_sbir_money], the [Introduction to Space Studies article A90][related_post_a90_intro_space_studies], the [History of Rocketplanes article A96][related_post_a96_history_rocketplanes], the [What Does the United States Space Force Do article A97][related_post_a97_us_space_force], the [Framing and the Co-Development Mechanism article A237][related_post_a237_aerospace_framing], the [Silicon Valley from Defense Contracting article A246][related_post_a246_silicon_valley_defense], and the [Contemporary Snapshot article A248][related_post_a248_contemporary_snapshot].

## Terminological Note

The article adopts terminology consistent with the private-capital conventions and marks the places the popular usage diverges. The term "fund" refers to a pooled investment vehicle with a stated term, and is distinguished throughout from "firm", which refers to the manager that raises successive funds. The distinction is load-bearing, because the firm may persist indefinitely while every fund it manages terminates. The term "patient capital" refers in this article to capital whose supplier faces no binding requirement to realize within the development horizon, and not to capital whose supplier expresses a willingness to wait. The term "realization" refers to the conversion of a holding into distributable proceeds, and is distinguished from "exit", which refers to a liquidity event at the portfolio company. The article's central claim is that the two can be separated. The term "dry powder" refers to committed but undrawn capital. The term "step-up" refers to an increase in the carrying value of a position arising from a subsequent round at a higher price.

## Load-Bearing Open Questions

The article closes with the load-bearing open questions the treatment leaves unresolved. First, the round terms are entirely unknown, and the liquidation preferences and protective provisions each materially affect the economics the article describes. Second, the valuations are transaction prices in a thin market whose price the issuer sets, so their informational content is contested and the article's quantitative material inherits that contest. Third, the central claim that the realization path rather than investor conviction produced the patience is supported by the structural argument and by the OneWeb contrast, and is not established by any direct evidence about what any particular investor would have done absent the mechanism. Fourth, the mechanism operates only in favorable states, so the sample of ventures exhibiting it is selected on the outcome the article uses it to explain. Fifth, whether the arrangement benefits the limited partners whose protective fund-life constraint it circumvents is an empirical question the article poses and cannot answer. Sixth, the extension of the pattern to the contemporary defense-technology wave assumes the secondary-market condition will be satisfied for those ventures, and it will be satisfied for few of them. Seventh, the adverse-state instrument set the article reasons about is documented in the financial-contracting literature and is not observed in the present case, so the finding that three of the five sub-properties fail on a common cause is a conditional prediction rather than a reconstruction, and it would be tested only by an adverse state the observed history does not contain. Eighth, whether the correlation among sub-properties that the adverse state induces is a general feature of the framework or to the financing condition is not established here, and the closing article should examine it across all ten conditions rather than assuming either answer.

## References

### Books

- [Amsden 1989 Asia's Next Giant][book_amsden_1989]
- [Berger 2021 Liftoff][book_berger_2021]
- [Berger 2024 Reentry][book_berger_2024]
- [Berle and Means 1932 The Modern Corporation and Private Property][book_berle_means_1932]
- [Berlin 2005 The Man Behind the Microchip][book_berlin_2005]
- [Bilstein 1996 Stages to Saturn][book_bilstein_1996]
- [Bilstein 2001 Flight in America][book_bilstein_2001]
- [Blank 2013 The Four Steps to the Epiphany][book_blank_2013]
- [Chandler 1962 Strategy and Structure][book_chandler_1962]
- [Chandler 1977 The Visible Hand][book_chandler_1977]
- [Chandler 1990 Scale and Scope][book_chandler_1990]
- [Chang 2002 Kicking Away the Ladder][book_chang_2002]
- [Chernow 2004 Titan The Life of John D Rockefeller Sr][book_chernow_2004]
- [Christensen 1997 The Innovator's Dilemma][book_christensen_1997]
- [Copeland and Antikarov 2001 Real Options A Practitioner's Guide][book_copeland_antikarov_2001]
- [Cyert and March 1963 A Behavioral Theory of the Firm][book_cyert_march_1963]
- [Davenport 2018 The Space Barons][book_davenport_2018]
- [de Vries and van der Woude 1997 The First Modern Economy][book_devries_vanderwoude_1997]
- [Dixit and Pindyck 1994 Investment Under Uncertainty][book_dixit_pindyck_1994]
- [Easterbrook and Fischel 1991 The Economic Structure of Corporate Law][book_easterbrook_fischel_1991]
- [Evans 1995 Embedded Autonomy][book_evans_1995]
- [Fernholz 2018 Rocket Billionaires][book_fernholz_2018]
- [Fligstein 2001 The Architecture of Markets][book_fligstein_2001]
- [Foster and McChesney 2011 The Endless Crisis][book_foster_mcchesney_2011]
- [Francillon 1979 McDonnell Douglas Aircraft Since 1920][book_francillon_1979]
- [Gertner 2012 The Idea Factory][book_gertner_2012]
- [Gompers and Lerner 2001 The Money of Invention][book_gompers_lerner_2001]
- [Grief 2006 Institutions and the Path to the Modern Economy][book_grief_2006]
- [Grimsey and Lewis 2004 Public Private Partnerships][book_grimsey_lewis_2004]
- [Handberg 1994 Reinventing NASA][book_handberg_1994]
- [Hansmann 1996 The Ownership of Enterprise][book_hansmann_1996]
- [Hart 1995 Firms Contracts and Financial Structure][book_hart_1995]
- [Heppenheimer 1999 The Space Shuttle Decision][book_heppenheimer_1999]
- [Hiltzik 1999 Dealers of Lightning][book_hiltzik_1999]
- [Ho 2009 Liquidated An Ethnography of Wall Street][book_ho_2009]
- [Hounshell 1984 From the American System to Mass Production 1800-1932][book_hounshell_1984]
- [Hughes 1983 Networks of Power][book_hughes_1983]
- [Isaacson 2023 Elon Musk][book_isaacson_2023]
- [Johnson 1982 MITI and the Japanese Miracle][book_johnson_1982]
- [Kahneman 2011 Thinking Fast and Slow][book_kahneman_2011]
- [Kearns and Nadler 1992 Prophets in the Dark][book_kearns_nadler_1992]
- [Kenney 2000 Understanding Silicon Valley][book_kenney_2000]
- [Klepper 2016 Experimental Capitalism][book_klepper_2016]
- [Krippner 2011 Capitalizing on Crisis][book_krippner_2011]
- [Laffont and Tirole 1993 A Theory of Incentives in Procurement and Regulation][book_laffont_tirole_1993]
- [Landes 1969 The Unbound Prometheus][book_landes_1969]
- [Lane 1934 Venetian Ships and Shipbuilders of the Renaissance][book_lane_1934]
- [Launius 1994 NASA A History of the United States Civil Space Program][book_launius_1994]
- [Launius 2004 Frontiers of Space Exploration][book_launius_2004]
- [Lecuyer 2006 Making Silicon Valley][book_lecuyer_2006]
- [Lerner 2009 Boulevard of Broken Dreams][book_lerner_2009]
- [Levin 2010 The Wires That Bind][book_levin_2010]
- [Logsdon 1970 The Decision to Go to the Moon][book_logsdon_1970]
- [MacKenzie 2006 An Engine Not a Camera][book_mackenzie_2006]
- [Malone 2014 The Intel Trinity][book_malone_2014]
- [March and Simon 1958 Organizations][book_march_simon_1958]
- [Markowitz 1959 Portfolio Selection Efficient Diversification of Investments][book_markowitz_1959]
- [Mazzucato 2013 The Entrepreneurial State][book_mazzucato_2013]
- [Mazzucato 2021 Mission Economy][book_mazzucato_2021]
- [McAfee and McMillan 1988 Incentives in Government Contracting][book_mcafee_mcmillan_1988]
- [McCurdy 1994 Inside NASA][book_mccurdy_1994]
- [McDougall 1985 The Heavens and the Earth][book_mcdougall_1985]
- [Melman 1970 Pentagon Capitalism][book_melman_1970]
- [Metcalfe 1998 Evolutionary Economics and Creative Destruction][book_metcalfe_1998]
- [Metrick and Yasuda 2011 Venture Capital and the Finance of Innovation][book_metrick_yasuda_2011]
- [Milgrom 2004 Putting Auction Theory to Work][book_milgrom_2004]
- [Moore 1991 Crossing the Chasm][book_moore_1991]
- [Mowery and Rosenberg 1998 Paths of Innovation][book_mowery_rosenberg_1998]
- [Muthoo 1999 Bargaining Theory with Applications][book_muthoo_1999]
- [Nelson 1993 National Innovation Systems][book_nelson_1993]
- [Nelson and Winter 1982 An Evolutionary Theory of Economic Change][book_nelson_winter_1982]
- [Nevins 1954 Ford The Times The Man The Company][book_nevins_1954]
- [Newhouse 1982 The Sporty Game][book_newhouse_1982]
- [Newhouse 2007 Boeing versus Airbus][book_newhouse_2007]
- [North 1990 Institutions Institutional Change and Economic Performance][book_north_1990]
- [Nye 1990 Electrifying America][book_nye_1990]
- [Osborne and Rubinstein 1990 Bargaining and Markets][book_osborne_rubinstein_1990]
- [Penrose 1959 The Theory of the Growth of the Firm][book_penrose_1959]
- [Perez 2002 Technological Revolutions and Financial Capital][book_perez_2002]
- [Preda 2009 Framing Finance][book_preda_2009]
- [Ries 2011 The Lean Startup][book_ries_2011]
- [Riordan and Hoddeson 1997 Crystal Fire][book_riordan_hoddeson_1997]
- [Robins 2006 The Corporation That Changed the World][book_robins_2006]
- [Roe 1994 Strong Managers Weak Owners][book_roe_1994]
- [Ruttan 2006 Is War Necessary for Economic Growth][book_ruttan_2006]
- [Saxenian 1994 Regional Advantage][book_saxenian_1994]
- [Serling 1992 Legend and Legacy][book_serling_1992]
- [Simon 1957 Administrative Behavior][book_simon_1957]
- [Srnicek 2017 Platform Capitalism][book_srnicek_2017]
- [Steensgaard 1974 The Asian Trade Revolution of the Seventeenth Century][book_steensgaard_1974]
- [Stern 2011 The Company-State][book_stern_2011]
- [Temin and Galambos 1987 The Fall of the Bell System][book_temin_galambos_1987]
- [Thiel 2014 Zero to One][book_thiel_2014]
- [Tirole 1988 The Theory of Industrial Organization][book_tirole_1988]
- [Tirole 2006 The Theory of Corporate Finance][book_tirole_2006]
- [Trigeorgis 1996 Real Options][book_trigeorgis_1996]
- [Vance 2015 Elon Musk][book_vance_2015]
- [Wade 1990 Governing the Market][book_wade_1990]
- [Williamson 1985 The Economic Institutions of Capitalism][book_williamson_1985]
- [Woo-Cumings 1999 The Developmental State][book_woo_cumings_1999]
- [Wu 2010 The Master Switch][book_wu_2010]
- [Yescombe 2007 Public-Private Partnerships Principles of Policy and Finance][book_yescombe_2007]
- [Zaloom 2006 Out of the Pits][book_zaloom_2006]
- [Zuboff 2019 The Age of Surveillance Capitalism][book_zuboff_2019]
- [Zubrin 1996 The Case for Mars][book_zubrin_1996]
- [Zubrin 2019 The Case for Space][book_zubrin_2019]

### Reference

- [10 United States Code 2371b Other Transaction Authority][ref_10_usc_2371b]
- [8VC][ref_8vc]
- [Alphabet Investor Relations][ref_alphabet_ir]
- [Andreessen Horowitz American Dynamism][ref_a16z_american_dynamism]
- [Anduril Corporate Record][ref_anduril]
- [Anthropic Long-Term Benefit Trust][ref_anthropic_ltbt]
- [Arianespace][ref_arianespace]
- [Ars Technica Space Coverage][ref_arstechnica_space]
- [AT and T Consent Decree of 1956][ref_att_consent_decree_1956]
- [AT and T Divestiture of 1984][ref_att_divestiture_1984]
- [Aviation Week][ref_aviation_week]
- [Axiom Space][ref_axiom_space]
- [Baillie Gifford][ref_baillie_gifford]
- [Berkshire Hathaway Shareholder Letters][ref_berkshire]
- [Bloomberg][ref_bloomberg]
- [Blue Origin Press Releases][ref_blue_origin_press]
- [Boeing Historical Archives][ref_boeing_historical_archives]
- [Boeing Press Releases][ref_boeing_press]
- [Bosch Corporate Record][ref_bosch_company]
- [Breaking Defense][ref_breaking_defense]
- [BryceTech Sector Reports][ref_bryce_tech]
- [Cambridge Associates Benchmark Data][ref_cambridge_associates]
- [Carl Zeiss Stiftung Statute][ref_carl_zeiss_stiftung]
- [Conference Board Business Cycle Indicators][ref_conference_board]
- [Council of Institutional Investors][ref_cii]
- [Council of Institutional Investors Dual-Class Policy][ref_cii_dual_class]
- [Danish Business Authority][ref_danish_business_authority]
- [Defense News][ref_defense_news]
- [Delaware Court of Chancery][ref_delaware_chancery]
- [Delaware Courts Published Opinions][ref_delaware_opinions]
- [Delaware Division of Corporations][ref_delaware_division_corporations]
- [Delaware General Corporation Law][ref_dgcl]
- [Delaware Revised Uniform Limited Partnership Act][ref_delaware_lp_act]
- [Department of Defense Contract Announcements][ref_dod_contracts]
- [Department of Defense Other Transaction Guidance][ref_dod_other_transactions]
- [Dodd-Frank Wall Street Reform and Consumer Protection Act of 2010][ref_dodd_frank_2010]
- [Draper Fisher Jurvetson Archive][ref_dfj]
- [European Corporate Governance Institute][ref_ecgi]
- [European Spaceflight][ref_european_spaceflight]
- [European Union Shareholder Rights Directive][ref_eu_shareholder_rights_directive]
- [Eutelsat Corporate Record][ref_eutelsat_oneweb]
- [FAA Office of Commercial Space Transportation][ref_faa_ast]
- [Federal Procurement Data System][ref_fpds]
- [Ford Investor Relations][ref_ford_ir]
- [Founders Fund][ref_founders_fund]
- [FTSE Russell Index Methodology][ref_ftse_russell]
- [German Aktiengesetz Stock Corporation Act][ref_german_aktiengesetz]
- [Glass Lewis Proxy Voting Guidelines][ref_glass_lewis]
- [Harvard Law School Forum on Corporate Governance][ref_harvard_corpgov_forum]
- [IBM Archives][ref_ibm_archives]
- [Institutional Limited Partners Association][ref_ilpa]
- [Institutional Shareholder Services Governance][ref_iss_governance]
- [Investment Advisers Act Section 203 Registration][ref_investment_advisers_act]
- [Investment Company Act Section 3 Definition of Investment Company][ref_investment_company_act]
- [Iridium Corporate News Archive][ref_iridium_press_archive_1998]
- [Jumpstart Our Business Startups Act of 2012][ref_jobs_act_2012]
- [Lux Capital][ref_lux_capital]
- [Meta Investor Relations][ref_meta_ir]
- [Microsoft News Record][ref_microsoft_news]
- [NASA Commercial Resupply Services Program][ref_nasa_crs_program]
- [NASA Commercial Space Office][ref_nasa_commercial_space]
- [NASA Commercial Space Programs][ref_nasa_commercial_space_programs]
- [NASASpaceflight][ref_nasaspaceflight]
- [Nasdaq Listing Rules][ref_nasdaq_listing_rules]
- [National Bureau of Economic Research Business Cycle Dating][ref_nber]
- [National Venture Capital Association][ref_nvca]
- [New York Stock Exchange Listed Company Manual][ref_nyse_listed_company_manual]
- [New York Times Space Coverage][ref_nyt]
- [Northrop Grumman Press Releases][ref_northrop_grumman_press]
- [Novo Holdings][ref_novo_holdings]
- [Novo Nordisk Foundation][ref_novo_nordisk_foundation]
- [OneWeb Corporate Record][ref_oneweb]
- [OpenAI Charter][ref_openai_charter]
- [OpenAI News Record][ref_openai_news]
- [Palantir Investor Materials][ref_palantir_ir]
- [Payload][ref_payload]
- [Payload Research][ref_payload_research]
- [PitchBook Transaction Data][ref_pitchbook]
- [Robert Bosch Stiftung][ref_bosch_stiftung]
- [Rocket Lab Press Releases][ref_rocket_lab_press]
- [S and P Dow Jones Indices Methodology][ref_spdji]
- [Sarbanes-Oxley Act of 2002][ref_sarbanes_oxley_2002]
- [SEC Archive Iridium Chapter 11 Filing 1999][ref_iridium_chapter_11_1999]
- [SEC EDGAR Company Search][ref_sec_edgar]
- [SEC Form D Exempt Offering Notices][ref_sec_form_d]
- [SEC Investor Education Service][ref_sec_investor_gov]
- [SEC Regulation 14E Tender Offer Requirements][ref_reg_14e]
- [SEC Regulation D and Securities Act Rules 17 CFR Part 230][ref_reg_d]
- [SEC Regulation S-K Disclosure Requirements][ref_sec_regulation_sk]
- [SEC Rule 12g-1 Registration Threshold][ref_rule_12g1]
- [SEC Rule 13e-4 Issuer Tender Offers][ref_rule_13e4]
- [SEC Rule 144 Resale of Restricted Securities][ref_rule_144]
- [SEC Rule 14a-8 Shareholder Proposals][ref_rule_14a8]
- [SEC Rule 506 Private Placement Safe Harbor][ref_rule_506]
- [SEC Rule 701 Compensatory Benefit Plan Exemption][ref_rule_701]
- [SEC Schedule 13D Beneficial Ownership Reporting][ref_schedule_13d]
- [Securities Act Section 4 Exempted Transactions][ref_securities_act_4a2]
- [Securities Exchange Act Section 12 Registration Requirements][ref_exchange_act_12g]
- [Sequoia Capital][ref_sequoia]
- [Shield Capital][ref_shield_capital]
- [Snap Investor Relations][ref_snap_ir]
- [Space Capital Quarterly Reports][ref_space_capital]
- [Space Force National Security Space Launch Program][ref_space_force_nssl]
- [Space Policy Online][ref_space_policy_online]
- [SpaceNews][ref_spacenews]
- [SpaceX Corporate Record][ref_spacex_company]
- [SpaceX Dragon C1 Orbital Demonstration 2010][ref_spacex_press_dragon_c1_2010]
- [SpaceX Falcon 1 Flight 4 2008][ref_spacex_press_falcon1_flight4_2008]
- [SpaceX Falcon 1 Flight 5 2009][ref_spacex_press_falcon1_flight5_2009]
- [SpaceX Falcon 9 First Flight 2010][ref_spacex_press_falcon9_first_flight_2010]
- [SpaceX Human Spaceflight][ref_spacex_human_spaceflight]
- [SpaceX News Archive][ref_spacex_news_archive]
- [SpaceX Seattle Announcement 2015][ref_spacex_seattle_announcement_2015]
- [SpaceX Starlink][ref_spacex_starlink]
- [SpaceX Starlink Service Beta 2020][ref_spacex_press_beta_2020]
- [SpaceX Starlink v0.9 First Operational Batch 2019][ref_spacex_press_starlink_v0_9_2019]
- [SpaceX Starshield][ref_spacex_starshield]
- [SpaceX Starship Program][ref_spacex_starship_program]
- [Standard Oil Company v United States 1911][ref_standard_oil_1911]
- [Stanford Graduate School of Business Case Collection][ref_stanford_spacex_case]
- [Tesla Investor Relations][ref_tesla_ir]
- [Texas Business Organizations Code][ref_texas_boc]
- [The Space Review][ref_the_space_review]
- [United Kingdom Companies Act 2006][ref_uk_companies_act_2006]
- [United Launch Alliance News][ref_ula_press]
- [United States Bankruptcy Code Chapter 11][ref_bankruptcy_code_ch11]
- [United States Bankruptcy Courts][ref_uscourts_bankruptcy]
- [USAspending Federal Award Data][ref_usaspending]
- [Valor Equity Partners][ref_valor_equity]
- [Virgin Orbit Court Record][ref_virgin_orbit_court]
- [Wall Street Journal Technology Coverage][ref_wsj]
- [Washington Post Technology Coverage][ref_washington_post]
- [Wharton Knowledge Repository][ref_wharton_spacex_case]
- [Zeiss Corporate Record][ref_zeiss_corporate]

### Research

- [Adilov Alexander Cunningham 2018 An Economic Analysis of Earth Orbit Pollution][research_adilov_et_al_2018]
- [Amihud and Lev 1981 Risk Reduction as a Managerial Motive for Conglomerate Mergers][research_amihud_lev_1981]
- [Anadol Cohen and Ferrari 2018 SpaceX Case Study][research_anadol_cohen_2018]
- [Arrow 1962 Economic Welfare and the Allocation of Resources for Invention][research_arrow_1962]
- [Barney 1991 Firm Resources and Sustained Competitive Advantage][research_barney_1991]
- [Bebchuk and Kastiel 2017 The Untenable Case for Perpetual Dual-Class Stock][research_bebchuk_kastiel_2017]
- [Bebchuk Kraakman and Triantis 2000 Stock Pyramids Cross-Ownership and Dual Class Equity][research_bebchuk_kraakman_triantis_2000]
- [Berger and Ofek 1995 Diversification's Effect on Firm Value][research_berger_ofek_1995]
- [Binmore Rubinstein and Wolinsky 1986 The Nash Bargaining Solution in Economic Modelling][research_binmore_rubinstein_wolinsky_1986]
- [Black and Scholes 1973 The Pricing of Options and Corporate Liabilities][research_black_scholes_1973]
- [Bonvillian 2018 DARPA and the Advanced Research Projects Agency][research_bonvillian_2018]
- [Coase 1937 The Nature of the Firm][research_coase_1937]
- [DeAngelo and DeAngelo 1985 Managerial Ownership of Voting Rights][research_deangelo_deangelo_1985]
- [Ewens and Farre-Mensa 2020 The Deregulation of the Private Equity Markets and the Decline in IPOs][research_ewens_farre_mensa_2020]
- [Fama and Jensen 1983 Separation of Ownership and Control][research_fama_jensen_1983]
- [Finkelstein and Sanford 2000 Learning from Corporate Mistakes The Rise and Fall of Iridium][research_finkelstein_sanford_2000]
- [Freeman and Soete 1997 The Economics of Industrial Innovation][research_freeman_soete_1997]
- [Gertner Scharfstein and Stein 1994 Internal versus External Capital Markets][research_gertner_scharfstein_stein_1994]
- [Gompers 1995 Optimal Investment Monitoring and the Staging of Venture Capital][research_gompers_1995]
- [Gompers Ishii and Metrick 2003 Corporate Governance and Equity Prices][research_gompers_ishii_metrick_2003]
- [Gompers Ishii and Metrick 2010 Extreme Governance An Analysis of Dual-Class Firms in the United States][research_gompers_ishii_metrick_2010]
- [Grossman and Hart 1986 The Costs and Benefits of Ownership][research_grossman_hart_1986]
- [Grossman and Hart 1988 One Share-One Vote and the Market for Corporate Control][research_grossman_hart_1988]
- [Hall and Lerner 2010 The Financing of R and D and Innovation][research_hall_lerner_2010]
- [Harris and Raviv 1988 Corporate Governance Voting Rights and Majority Rules][research_harris_raviv_1988]
- [Hart 1988 Incomplete Contracts and the Theory of the Firm][research_hart_1988]
- [Hart and Moore 1990 Property Rights and the Nature of the Firm][research_hart_moore_1990]
- [Hertzfeld 2002 Measuring the Economic Returns from Successful NASA Life Sciences Technology Transfer][research_hertzfeld_2002]
- [Jensen 1986 Agency Costs of Free Cash Flow Corporate Finance and Takeovers][research_jensen_1986]
- [Jensen and Meckling 1976 Theory of the Firm Managerial Behavior Agency Costs and Ownership Structure][research_jensen_meckling_1976]
- [Kahneman and Tversky 1979 Prospect Theory][research_kahneman_tversky_1979]
- [Kaplan and Stromberg 2003 Financial Contracting Theory Meets the Real World][research_kaplan_stromberg_2003]
- [Kaplan and Stromberg 2004 Characteristics Contracts and Actions][research_kaplan_stromberg_2004]
- [Klein Crawford and Alchian 1978 Vertical Integration Appropriable Rents and the Competitive Contracting Process][research_klein_crawford_alchian_1978]
- [Klepper 1996 Entry Exit Growth and Innovation over the Product Life Cycle][research_klepper_1996]
- [Klepper 2010 The Origin and Growth of Industry Clusters][research_klepper_2010]
- [Kogut and Kulatilaka 1994 Operating Flexibility Global Manufacturing and the Option Value of a Multinational Network][research_kogut_kulatilaka_1994]
- [Kortum and Lerner 2000 Assessing the Contribution of Venture Capital to Innovation][research_kortum_lerner_2000]
- [La Porta Lopez-de-Silanes Shleifer and Vishny 1998 Law and Finance][research_laporta_et_al_1998]
- [Lang and Stulz 1994 Tobin's q Corporate Diversification and Firm Performance][research_lang_stulz_1994]
- [Lerner 1994 The Syndication of Venture Capital Investments][research_lerner_1994_syndication]
- [Lerner 1996 The Government as Venture Capitalist][research_lerner_1996_government_program]
- [Lewellen 1971 A Pure Financial Rationale for the Conglomerate Merger][research_lewellen_1971]
- [Lintner 1965 The Valuation of Risk Assets and the Selection of Risky Investments][research_lintner_1965]
- [Manne 1965 Mergers and the Market for Corporate Control][research_manne_1965]
- [March 1991 Exploration and Exploitation in Organizational Learning][research_march_1991]
- [Markowitz 1952 Portfolio Selection][research_markowitz_1952]
- [McDonald and Siegel 1986 The Value of Waiting to Invest][research_mcdonald_siegel_1986]
- [Merton 1973 Theory of Rational Option Pricing][research_merton_1973]
- [Montgomery 1994 Corporate Diversification][research_montgomery_1994]
- [Myers 1977 Determinants of Corporate Borrowing][research_myers_1977]
- [Myerson 1981 Optimal Auction Design][research_myerson_1981]
- [Nash 1950 The Bargaining Problem][research_nash_1950]
- [Nelson 1959 The Simple Economics of Basic Scientific Research][research_nelson_1959]
- [Peteraf 1993 The Cornerstones of Competitive Advantage][research_peteraf_1993]
- [Rajan Servaes and Zingales 2000 The Cost of Diversity][research_rajan_servaes_zingales_2000]
- [Rubinstein 1982 Perfect Equilibrium in a Bargaining Model][research_rubinstein_1982]
- [Sahlman 1990 The Structure and Governance of Venture-Capital Organizations][research_sahlman_1990]
- [Scharfstein and Stein 2000 The Dark Side of Internal Capital Markets][research_scharfstein_stein_2000]
- [Sharpe 1964 Capital Asset Prices A Theory of Market Equilibrium][research_sharpe_1964]
- [Shleifer and Vishny 1997 A Survey of Corporate Governance][research_shleifer_vishny_1997]
- [Staw 1976 Knee-Deep in the Big Muddy][research_staw_1976]
- [Stein 1997 Internal Capital Markets and the Competition for Corporate Resources][research_stein_1997]
- [Teece 1986 Profiting from Technological Innovation][research_teece_1986]
- [Teece 2007 Explicating Dynamic Capabilities The Nature and Microfoundations of Sustainable Enterprise Performance][research_teece_2007]
- [Teece Pisano Shuen 1997 Dynamic Capabilities and Strategic Management][research_teece_pisano_shuen_1997]
- [Tversky and Kahneman 1992 Advances in Prospect Theory][research_tversky_kahneman_1992]
- [Weinzierl 2018 Space the Final Economic Frontier][research_weinzierl_2018]
- [Wernerfelt 1984 A Resource-Based View of the Firm][research_wernerfelt_1984]
- [Williamson 1971 The Vertical Integration of Production Market Failure Considerations][research_williamson_1971]
- [Williamson 2002 The Theory of the Firm as Governance Structure][research_williamson_2002]
- [Zimmerman 2011 The Economics of Satellite Communications][research_zimmerman_2011]

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

[book_amsden_1989]: https://global.oup.com/academic/product/asias-next-giant-9780195076035
[book_berger_2021]: https://www.harpercollins.com/products/liftoff-eric-berger
[book_berger_2024]: https://openlibrary.org/search?q=Berger+Reentry+SpaceX
[book_berle_means_1932]: https://www.routledge.com/The-Modern-Corporation-and-Private-Property/Berle-Means/p/book/9780887388873
[book_berlin_2005]: https://global.oup.com/academic/product/the-man-behind-the-microchip-9780195311990
[book_bilstein_1996]: https://ntrs.nasa.gov/search?q=Stages+to+Saturn+Bilstein
[book_bilstein_2001]: https://jhupbooks.press.jhu.edu/title/flight-america
[book_blank_2013]: https://openlibrary.org/search?q=Blank+Four+Steps+to+the+Epiphany
[book_chandler_1962]: https://mitpress.mit.edu/9780262530095/strategy-and-structure/
[book_chandler_1977]: https://www.hup.harvard.edu/books/9780674940529
[book_chandler_1990]: https://openlibrary.org/search?q=Chandler+Scale+and+Scope
[book_chang_2002]: https://www.penguin.co.uk/books/56082/kicking-away-the-ladder/9780857281050
[book_chernow_2004]: https://openlibrary.org/search?q=Chernow+Titan
[book_christensen_1997]: https://www.hbsp.harvard.edu/product/1130-HBK-ENG
[book_copeland_antikarov_2001]: https://openlibrary.org/search?q=Copeland+and+Antikarov+Real+Options+A+Practitioners+Guide
[book_cyert_march_1963]: https://openlibrary.org/search?q=Cyert+March+Behavioral+Theory+Firm
[book_davenport_2018]: https://www.hachettebookgroup.com/titles/christian-davenport/the-space-barons/9781610398299/
[book_devries_vanderwoude_1997]: https://www.cambridge.org/9780521578257
[book_dixit_pindyck_1994]: https://openlibrary.org/search?q=Dixit+and+Pindyck+Investment+Under+Uncertainty
[book_easterbrook_fischel_1991]: https://www.hup.harvard.edu/books/9780674235397
[book_evans_1995]: https://press.princeton.edu/books/paperback/9780691037363/embedded-autonomy
[book_fernholz_2018]: https://www.hachettebookgroup.com/titles/tim-fernholz/rocket-billionaires/9781328662231/
[book_fligstein_2001]: https://press.princeton.edu/books/paperback/9780691102542/the-architecture-of-markets
[book_foster_mcchesney_2011]: https://monthlyreview.org/product/endless_crisis/
[book_francillon_1979]: https://openlibrary.org/search?q=Francillon+McDonnell+Douglas+Aircraft+Since+1920
[book_gertner_2012]: https://www.penguinrandomhouse.com/books/206061/the-idea-factory-by-jon-gertner/
[book_gompers_lerner_2001]: https://www.hbsp.harvard.edu/product/2434-HBK-ENG
[book_grief_2006]: https://www.cambridge.org/9780521671347
[book_grimsey_lewis_2004]: https://www.e-elgar.com/shop/gbp/public-private-partnerships-9781840647112.html
[book_handberg_1994]: https://openlibrary.org/search?q=Handberg+Reinventing+NASA
[book_hansmann_1996]: https://www.hup.harvard.edu/books/9780674001718
[book_hart_1995]: https://global.oup.com/academic/product/firms-contracts-and-financial-structure-9780198288817
[book_heppenheimer_1999]: https://www.si.edu/object/space-shuttle-decision%3Anmah_1197080
[book_hiltzik_1999]: https://openlibrary.org/search?q=Hiltzik+Dealers+of+Lightning
[book_ho_2009]: https://www.dukeupress.edu/liquidated
[book_hounshell_1984]: https://jhupbooks.press.jhu.edu/title/american-system-mass-production-1800-1932
[book_hughes_1983]: https://jhupbooks.press.jhu.edu/title/networks-power
[book_isaacson_2023]: https://www.simonandschuster.com/books/Elon-Musk/Walter-Isaacson/9781982181284
[book_johnson_1982]: https://www.sup.org/books/title/?id=2143
[book_kahneman_2011]: https://us.macmillan.com/books/9780374533557/thinkingfastandslow
[book_kearns_nadler_1992]: https://openlibrary.org/search?q=Kearns+Nadler+Prophets+Dark
[book_kenney_2000]: https://www.sup.org/books/title/?id=1354
[book_klepper_2016]: https://press.princeton.edu/books/hardcover/9780691169620/experimental-capitalism
[book_krippner_2011]: https://www.hup.harvard.edu/books/9780674066199
[book_laffont_tirole_1993]: https://mitpress.mit.edu/9780262121743/a-theory-of-incentives-in-procurement-and-regulation/
[book_landes_1969]: https://www.cambridge.org/9780521094184
[book_lane_1934]: https://jhupbooks.press.jhu.edu/title/venetian-ships-and-shipbuilders-renaissance
[book_launius_1994]: https://openlibrary.org/search?q=Launius+NASA+History+United+States+Civil+Space+Program
[book_launius_2004]: https://global.oup.com/academic/product/frontiers-of-space-exploration-9780313325243
[book_lecuyer_2006]: https://mitpress.mit.edu/9780262622110/making-silicon-valley/
[book_lerner_2009]: https://press.princeton.edu/books/hardcover/9780691142197/boulevard-of-broken-dreams
[book_levin_2010]: https://openlibrary.org/search?q=Levin+Wires+That+Bind
[book_logsdon_1970]: https://mitpress.mit.edu/9780262620109/the-decision-to-go-to-the-moon/
[book_mackenzie_2006]: https://mitpress.mit.edu/9780262633673/an-engine-not-a-camera/
[book_malone_2014]: https://openlibrary.org/search?q=Malone+The+Intel+Trinity
[book_march_simon_1958]: https://www.wiley.com/en-us/Organizations%2C+2nd+Edition-p-9780631186311
[book_markowitz_1959]: https://yalebooks.yale.edu/book/9780300013726/portfolio-selection/
[book_mazzucato_2013]: https://marianamazzucato.com/books/the-entrepreneurial-state
[book_mazzucato_2021]: https://marianamazzucato.com/books/mission-economy/
[book_mcafee_mcmillan_1988]: https://openlibrary.org/search?q=McAfee+and+McMillan+Incentives+in+Government+Contracting
[book_mccurdy_1994]: https://jhupbooks.press.jhu.edu/title/inside-nasa
[book_mcdougall_1985]: https://jhupbooks.press.jhu.edu/title/heavens-and-earth
[book_melman_1970]: https://openlibrary.org/search?q=Melman+Pentagon+Capitalism
[book_metcalfe_1998]: https://www.routledge.com/Evolutionary-Economics-and-Creative-Destruction/Metcalfe/p/book/9780415158671
[book_metrick_yasuda_2011]: https://openlibrary.org/search?q=Metrick+Yasuda+Venture+Capital+Finance+of+Innovation
[book_milgrom_2004]: https://www.cambridge.org/9780521551847
[book_moore_1991]: https://www.harpercollins.com/products/crossing-the-chasm-geoffrey-a-moore
[book_mowery_rosenberg_1998]: https://openlibrary.org/search?q=Mowery+Rosenberg+Paths+of+Innovation
[book_muthoo_1999]: https://www.cambridge.org/9780521576475
[book_nelson_1993]: https://global.oup.com/academic/product/national-innovation-systems-9780195076172
[book_nelson_winter_1982]: https://www.hup.harvard.edu/books/9780674272286
[book_nevins_1954]: https://openlibrary.org/search?q=Nevins+Ford+The+Times+The+Man+The+Company
[book_newhouse_1982]: https://openlibrary.org/search?q=Newhouse+The+Sporty+Game
[book_newhouse_2007]: https://us.macmillan.com/books/9781400079131/boeingversusairbus
[book_north_1990]: https://www.cambridge.org/9780521397346
[book_nye_1990]: https://mitpress.mit.edu/9780262640305/electrifying-america/
[book_osborne_rubinstein_1990]: https://www.sciencedirect.com/book/9780125286329/bargaining-and-markets
[book_penrose_1959]: https://global.oup.com/academic/product/the-theory-of-the-growth-of-the-firm-9780199573844
[book_perez_2002]: https://openlibrary.org/search?q=Perez+Technological+Revolutions+and+Financial+Capital
[book_preda_2009]: https://openlibrary.org/search?q=Preda+Framing+Finance
[book_ries_2011]: https://www.crownpublishing.com/archives/feature/lean-startup
[book_riordan_hoddeson_1997]: https://wwnorton.com/books/Crystal-Fire/
[book_robins_2006]: https://openlibrary.org/search?q=Robins+The+Corporation+That+Changed+the+World
[book_roe_1994]: https://press.princeton.edu/books/paperback/9780691026312/strong-managers-weak-owners
[book_ruttan_2006]: https://global.oup.com/academic/product/is-war-necessary-for-economic-growth-9780195188042
[book_saxenian_1994]: https://www.hup.harvard.edu/books/9780674753402
[book_serling_1992]: https://openlibrary.org/search?q=Serling+Legend+and+Legacy
[book_simon_1957]: https://www.simonandschuster.com/books/Administrative-Behavior-4th-Edition/Herbert-A-Simon/9781439136218
[book_srnicek_2017]: https://www.wiley.com/en-us/Platform+Capitalism-p-9781509504879
[book_steensgaard_1974]: https://openlibrary.org/search?q=Steensgaard+The+Asian+Trade+Revolution+of+the+Seventeenth+Century
[book_stern_2011]: https://global.oup.com/academic/product/the-company-state-9780195393736
[book_temin_galambos_1987]: https://openlibrary.org/search?q=Temin+Galambos+Fall+Bell+System
[book_thiel_2014]: https://www.penguinrandomhouse.com/books/226845/zero-to-one-by-peter-thiel-with-blake-masters/
[book_tirole_1988]: https://mitpress.mit.edu/9780262200714/the-theory-of-industrial-organization/
[book_tirole_2006]: https://press.princeton.edu/books/hardcover/9780691125565/the-theory-of-corporate-finance
[book_trigeorgis_1996]: https://mitpress.mit.edu/9780262201025/real-options/
[book_vance_2015]: https://www.harpercollins.com/products/elon-musk-ashlee-vance
[book_wade_1990]: https://press.princeton.edu/books/paperback/9780691117294/governing-the-market
[book_williamson_1985]: https://www.simonandschuster.com/books/The-Economic-Institutions-of-Capitalism/Oliver-E-Williamson/9780684863740
[book_woo_cumings_1999]: https://www.cornellpress.cornell.edu/book/9780801485664/the-developmental-state/
[book_wu_2010]: https://openlibrary.org/search?q=Wu+The+Master+Switch
[book_yescombe_2007]: https://www.sciencedirect.com/book/9780750680547/public-private-partnerships
[book_zaloom_2006]: https://openlibrary.org/search?q=Zaloom+Out+of+the+Pits
[book_zuboff_2019]: https://www.hachettebookgroup.com/titles/shoshana-zuboff/the-age-of-surveillance-capitalism/9781610395694/
[book_zubrin_1996]: https://www.simonandschuster.com/books/The-Case-for-Mars/Robert-Zubrin/9781451608113
[book_zubrin_2019]: https://openlibrary.org/search?q=Zubrin+The+Case+for+Space
[ref_10_usc_2371b]: https://www.law.cornell.edu/uscode/text/10/2371b
[ref_8vc]: https://www.8vc.com/
[ref_a16z_american_dynamism]: https://a16z.com/american-dynamism/
[ref_alphabet_ir]: https://abc.xyz/investor/
[ref_anduril]: https://www.anduril.com/
[ref_anthropic_ltbt]: https://www.anthropic.com/news/the-long-term-benefit-trust
[ref_arianespace]: https://www.arianespace.com/
[ref_arstechnica_space]: https://arstechnica.com/science/space/
[ref_att_consent_decree_1956]: https://www.corp.att.com/history/nethistory/consent-decree.html
[ref_att_divestiture_1984]: https://www.corp.att.com/history/nethistory/divestiture.html
[ref_aviation_week]: https://aviationweek.com/
[ref_axiom_space]: https://www.axiomspace.com/
[ref_baillie_gifford]: https://www.bailliegifford.com/
[ref_bankruptcy_code_ch11]: https://www.law.cornell.edu/uscode/text/11/chapter-11
[ref_berkshire]: https://www.berkshirehathaway.com/
[ref_bloomberg]: https://www.bloomberg.com/
[ref_blue_origin_press]: https://www.blueorigin.com/news/
[ref_boeing_historical_archives]: https://www.boeing.com/history/
[ref_boeing_press]: https://boeing.mediaroom.com/
[ref_bosch_company]: https://www.bosch.com/company/
[ref_bosch_stiftung]: https://www.bosch-stiftung.de/en
[ref_breaking_defense]: https://breakingdefense.com/
[ref_bryce_tech]: https://brycetech.com/reports
[ref_cambridge_associates]: https://www.cambridgeassociates.com/
[ref_carl_zeiss_stiftung]: https://www.carl-zeiss-stiftung.de/en/
[ref_cii]: https://www.cii.org/
[ref_cii_dual_class]: https://www.cii.org/dualclass_stock
[ref_conference_board]: https://www.conference-board.org/
[ref_danish_business_authority]: https://danishbusinessauthority.dk/
[ref_defense_news]: https://www.defensenews.com/
[ref_delaware_chancery]: https://courts.delaware.gov/chancery/
[ref_delaware_division_corporations]: https://corp.delaware.gov/
[ref_delaware_lp_act]: https://delcode.delaware.gov/title6/c017/
[ref_delaware_opinions]: https://courts.delaware.gov/opinions/
[ref_dfj]: https://www.dfj.com/
[ref_dgcl]: https://delcode.delaware.gov/title8/c001/
[ref_dod_contracts]: https://www.defense.gov/News/Contracts/
[ref_dod_other_transactions]: https://aida.mitre.org/ota/
[ref_dodd_frank_2010]: https://www.congress.gov/111/plaws/publ203/PLAW-111publ203.pdf
[ref_ecgi]: https://www.ecgi.global/
[ref_eu_shareholder_rights_directive]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32017L0828
[ref_european_spaceflight]: https://europeanspaceflight.com/
[ref_eutelsat_oneweb]: https://www.eutelsat.com/
[ref_exchange_act_12g]: https://www.law.cornell.edu/uscode/text/15/78l
[ref_faa_ast]: https://www.faa.gov/space
[ref_ford_ir]: https://shareholder.ford.com/
[ref_founders_fund]: https://foundersfund.com/
[ref_fpds]: https://www.fpds.gov/
[ref_ftse_russell]: https://www.lseg.com/en/ftse-russell
[ref_german_aktiengesetz]: https://www.gesetze-im-internet.de/aktg/
[ref_glass_lewis]: https://www.glasslewis.com/
[ref_harvard_corpgov_forum]: https://corpgov.law.harvard.edu/
[ref_ibm_archives]: https://www.ibm.com/history/
[ref_ilpa]: https://ilpa.org/
[ref_investment_advisers_act]: https://www.law.cornell.edu/uscode/text/15/80b-3
[ref_investment_company_act]: https://www.law.cornell.edu/uscode/text/15/80a-3
[ref_iridium_chapter_11_1999]: https://www.sec.gov/Archives/edgar/data/1029074/0000912057-99-034228.txt
[ref_iridium_press_archive_1998]: https://www.iridium.com/
[ref_iss_governance]: https://www.issgovernance.com/
[ref_jobs_act_2012]: https://www.congress.gov/112/plaws/publ106/PLAW-112publ106.pdf
[ref_lux_capital]: https://www.luxcapital.com/
[ref_meta_ir]: https://investor.atmeta.com/
[ref_microsoft_news]: https://news.microsoft.com/
[ref_nasa_commercial_space]: https://www.nasa.gov/commercial-space/
[ref_nasa_commercial_space_programs]: https://www.nasa.gov/humans-in-space/commercial-space/
[ref_nasa_crs_program]: https://www.nasa.gov/international-space-station/commercial-resupply/
[ref_nasaspaceflight]: https://www.nasaspaceflight.com/
[ref_nasdaq_listing_rules]: https://listingcenter.nasdaq.com/rulebook/nasdaq/rules
[ref_nber]: https://www.nber.org/
[ref_northrop_grumman_press]: https://news.northropgrumman.com/
[ref_novo_holdings]: https://www.novoholdings.dk/
[ref_novo_nordisk_foundation]: https://novonordiskfonden.dk/en/
[ref_nvca]: https://nvca.org/
[ref_nyse_listed_company_manual]: https://nyseguide.srorules.com/listed-company-manual
[ref_nyt]: https://www.nytimes.com/section/science/space
[ref_oneweb]: https://oneweb.net/
[ref_openai_charter]: https://openai.com/charter/
[ref_openai_news]: https://openai.com/news/
[ref_palantir_ir]: https://investors.palantir.com/
[ref_payload]: https://payloadspace.com/
[ref_payload_research]: https://payloadspace.com/research/
[ref_pitchbook]: https://pitchbook.com/
[ref_reg_14e]: https://www.ecfr.gov/current/title-17/section-240.14e-1
[ref_reg_d]: https://www.ecfr.gov/current/title-17/part-230
[ref_rocket_lab_press]: https://www.rocketlabusa.com/updates/
[ref_rule_12g1]: https://www.ecfr.gov/current/title-17/section-240.12g-1
[ref_rule_13e4]: https://www.ecfr.gov/current/title-17/section-240.13e-4
[ref_rule_144]: https://www.ecfr.gov/current/title-17/section-230.144
[ref_rule_14a8]: https://www.ecfr.gov/current/title-17/section-240.14a-8
[ref_rule_506]: https://www.ecfr.gov/current/title-17/section-230.506
[ref_rule_701]: https://www.ecfr.gov/current/title-17/section-230.701
[ref_sarbanes_oxley_2002]: https://www.congress.gov/107/plaws/publ204/PLAW-107publ204.pdf
[ref_schedule_13d]: https://www.ecfr.gov/current/title-17/section-240.13d-101
[ref_sec_edgar]: https://www.sec.gov/edgar/searchedgar/companysearch
[ref_sec_form_d]: https://www.sec.gov/answers/formd.htm
[ref_sec_investor_gov]: https://www.investor.gov/
[ref_sec_regulation_sk]: https://www.ecfr.gov/current/title-17/part-229
[ref_securities_act_4a2]: https://www.law.cornell.edu/uscode/text/15/77d
[ref_sequoia]: https://www.sequoiacap.com/
[ref_shield_capital]: https://www.shieldcap.com/
[ref_snap_ir]: https://investor.snap.com/
[ref_space_capital]: https://www.spacecapital.com/
[ref_space_force_nssl]: https://www.spaceforce.mil/News/Fact-Sheets
[ref_space_policy_online]: https://spacepolicyonline.com/
[ref_spacenews]: https://spacenews.com/
[ref_spacex_company]: https://www.spacex.com/
[ref_spacex_human_spaceflight]: https://www.spacex.com/humanspaceflight/
[ref_spacex_news_archive]: https://www.spacex.com/updates/
[ref_spacex_press_beta_2020]: https://www.spacex.com/updates/
[ref_spacex_press_dragon_c1_2010]: https://www.spacex.com/updates/
[ref_spacex_press_falcon1_flight4_2008]: https://www.spacex.com/news/2013/02/11/spacex-successfully-launches-falcon-1-orbit
[ref_spacex_press_falcon1_flight5_2009]: https://www.spacex.com/updates/
[ref_spacex_press_falcon9_first_flight_2010]: https://www.spacex.com/updates/
[ref_spacex_press_starlink_v0_9_2019]: https://www.spacex.com/updates/
[ref_spacex_seattle_announcement_2015]: https://www.spacex.com/updates/
[ref_spacex_starlink]: https://www.starlink.com/
[ref_spacex_starshield]: https://www.spacex.com/starshield/
[ref_spacex_starship_program]: https://www.spacex.com/vehicles/starship/
[ref_spdji]: https://www.spglobal.com/spdji/en/
[ref_standard_oil_1911]: https://supreme.justia.com/cases/federal/us/221/1/
[ref_stanford_spacex_case]: https://www.gsb.stanford.edu/faculty-research/case-studies
[ref_tesla_ir]: https://ir.tesla.com/
[ref_texas_boc]: https://statutes.capitol.texas.gov/Docs/BO/htm/BO.21.htm
[ref_the_space_review]: https://www.thespacereview.com/
[ref_uk_companies_act_2006]: https://www.legislation.gov.uk/ukpga/2006/46/contents
[ref_ula_press]: https://www.ulalaunch.com/about/news
[ref_usaspending]: https://www.usaspending.gov/
[ref_uscourts_bankruptcy]: https://www.uscourts.gov/court-programs/bankruptcy
[ref_valor_equity]: https://www.valorep.com/
[ref_virgin_orbit_court]: https://www.deb.uscourts.gov/
[ref_washington_post]: https://www.washingtonpost.com/business/technology/
[ref_wharton_spacex_case]: https://knowledge.wharton.upenn.edu/
[ref_wsj]: https://www.wsj.com/tech
[ref_zeiss_corporate]: https://www.zeiss.com/corporate/en/home.html
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
[related_post_a90_intro_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[related_post_a96_history_rocketplanes]: {% post_url 2026-02-27-history_of_rocketplanes %}
[related_post_a97_us_space_force]: {% post_url 2026-02-28-what_does_united_states_space_force_do %}
[research_adilov_et_al_2018]: https://www.sciencedirect.com/science/article/abs/pii/S0921800917305591
[research_amihud_lev_1981]: https://www.jstor.org/stable/3003457
[research_anadol_cohen_2018]: https://www.hbs.edu/faculty/Pages/item.aspx?num=54001
[research_arrow_1962]: https://www.nber.org/system/files/chapters/c2144/c2144.pdf
[research_barney_1991]: https://journals.sagepub.com/doi/10.1177/014920639101700108
[research_bebchuk_kastiel_2017]: https://www.virginialawreview.org/articles/untenable-case-perpetual-dual-class-stock/
[research_bebchuk_kraakman_triantis_2000]: https://www.nber.org/chapters/c9013
[research_berger_ofek_1995]: https://doi.org/10.1016/0304-405X(94)00798-6
[research_binmore_rubinstein_wolinsky_1986]: https://www.jstor.org/stable/2555382
[research_black_scholes_1973]: https://www.jstor.org/stable/1831029
[research_bonvillian_2018]: https://mitpress.mit.edu/9780262038522/the-darpa-model-for-transformative-technologies/
[research_coase_1937]: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-0335.1937.tb00002.x
[research_deangelo_deangelo_1985]: https://www.sciencedirect.com/science/article/abs/pii/0304405X85900436
[research_ewens_farre_mensa_2020]: https://academic.oup.com/rfs/article-abstract/33/12/5463/5866533
[research_fama_jensen_1983]: https://www.jstor.org/stable/725104
[research_finkelstein_sanford_2000]: https://doi.org/10.1016/S0090-2616(00)00020-6
[research_freeman_soete_1997]: https://mitpress.mit.edu/9780262561136/the-economics-of-industrial-innovation/
[research_gertner_scharfstein_stein_1994]: https://academic.oup.com/qje/article-abstract/109/4/1211/1866357
[research_gompers_1995]: https://www.jstor.org/stable/2329227
[research_gompers_ishii_metrick_2003]: https://academic.oup.com/qje/article/118/1/107/1917017
[research_gompers_ishii_metrick_2010]: https://academic.oup.com/rfs/article/23/3/1051/1568225
[research_grossman_hart_1986]: https://www.jstor.org/stable/1833199
[research_grossman_hart_1988]: https://www.sciencedirect.com/science/article/abs/pii/0304405X88900443
[research_hall_lerner_2010]: https://www.sciencedirect.com/science/article/pii/S0169721810010142
[research_harris_raviv_1988]: https://www.sciencedirect.com/science/article/abs/pii/0304405X88900455
[research_hart_1988]: https://www.jstor.org/stable/764953
[research_hart_moore_1990]: https://www.jstor.org/stable/2937861
[research_hertzfeld_2002]: https://www.sciencedirect.com/science/article/abs/pii/S0265964602000188
[research_jensen_1986]: https://www.jstor.org/stable/1818789
[research_jensen_meckling_1976]: https://www.sciencedirect.com/science/article/pii/0304405X7690026X
[research_kahneman_tversky_1979]: https://www.jstor.org/stable/1914185
[research_kaplan_stromberg_2003]: https://academic.oup.com/restud/article-abstract/70/2/281/1571073
[research_kaplan_stromberg_2004]: https://academic.oup.com/rfs/article-abstract/17/1/1/1601330
[research_klein_crawford_alchian_1978]: https://www.jstor.org/stable/725234
[research_klepper_1996]: https://www.jstor.org/stable/2118211
[research_klepper_2010]: https://academic.oup.com/icc/article/19/1/135/731929
[research_kogut_kulatilaka_1994]: https://pubsonline.informs.org/doi/10.1287/mnsc.40.1.123
[research_kortum_lerner_2000]: https://www.rand.org/pubs/reprints/RP924.html
[research_lang_stulz_1994]: https://www.journals.uchicago.edu/doi/10.1086/261970
[research_laporta_et_al_1998]: https://www.journals.uchicago.edu/doi/10.1086/250042
[research_lerner_1994_syndication]: https://www.jstor.org/stable/3665602
[research_lerner_1996_government_program]: https://www.nber.org/papers/w5753
[research_lewellen_1971]: https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1971.tb00912.x
[research_lintner_1965]: https://www.jstor.org/stable/1924119
[research_manne_1965]: https://www.journals.uchicago.edu/doi/10.1086/259036
[research_march_1991]: https://pubsonline.informs.org/doi/10.1287/orsc.2.1.71
[research_markowitz_1952]: https://www.jstor.org/stable/2975974
[research_mcdonald_siegel_1986]: https://academic.oup.com/qje/article-abstract/101/4/707/1885353
[research_merton_1973]: https://www.jstor.org/stable/3003143
[research_montgomery_1994]: https://www.aeaweb.org/articles?id=10.1257/jep.8.3.163
[research_myers_1977]: https://www.sciencedirect.com/science/article/abs/pii/0304405X77900150
[research_myerson_1981]: https://pubsonline.informs.org/doi/10.1287/moor.6.1.58
[research_nash_1950]: https://www.jstor.org/stable/1907266
[research_nelson_1959]: https://www.journals.uchicago.edu/doi/10.1086/258177
[research_peteraf_1993]: https://onlinelibrary.wiley.com/doi/10.1002/smj.4250140303
[research_rajan_servaes_zingales_2000]: https://onlinelibrary.wiley.com/doi/10.1111/0022-1082.00200
[research_rubinstein_1982]: https://www.jstor.org/stable/1912531
[research_sahlman_1990]: https://www.sciencedirect.com/science/article/pii/0304405X9090065E
[research_scharfstein_stein_2000]: https://onlinelibrary.wiley.com/doi/10.1111/0022-1082.00299
[research_sharpe_1964]: https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1964.tb02865.x
[research_shleifer_vishny_1997]: https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1997.tb04820.x
[research_staw_1976]: https://www.sciencedirect.com/science/article/abs/pii/003050737690005X
[research_stein_1997]: https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1997.tb03810.x
[research_teece_1986]: https://www.sciencedirect.com/science/article/abs/pii/0048733386900272
[research_teece_2007]: https://onlinelibrary.wiley.com/doi/10.1002/smj.640
[research_teece_pisano_shuen_1997]: https://onlinelibrary.wiley.com/doi/10.1002/%28SICI%291097-0266%28199708%2918%3A7%3C509%3A%3AAID-SMJ882%3E3.0.CO%3B2-Z
[research_tversky_kahneman_1992]: https://link.springer.com/article/10.1007/BF00122574
[research_weinzierl_2018]: https://www.aeaweb.org/articles?id=10.1257/jep.32.2.173
[research_wernerfelt_1984]: https://onlinelibrary.wiley.com/doi/10.1002/smj.4250050207
[research_williamson_1971]: https://www.jstor.org/stable/1815199
[research_williamson_2002]: https://www.aeaweb.org/articles?id=10.1257/089533002760278776
[research_zimmerman_2011]: https://openlibrary.org/search?q=Zimmerman+Economics+Satellite+Communications
