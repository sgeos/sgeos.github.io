---
layout: post
mathjax: true
comments: true
title: "History of SpaceX: Governance That Resists Capital Capture Across Thirty-Plus Funding Rounds"
date: 2026-07-30 09:00:00 +0000
categories: history business aerospace
series: spacex_history
series_title: History of SpaceX
series_index: 7
---

<!-- A287 -->
<script>console.log("A287");</script>

This article is the seventh in the History of SpaceX series and treats the governance forcing-function condition that the [series opener][related_post_a281_spacex_framing] introduced as the sixth of seven forcing-function conditions in the seven-plus-three analytical framework. The governance condition requires that a mission-directed technology venture adopt a control configuration that permits the venture to raise the capital its mission requires without transferring to the capital providers the authority to redirect the mission. The condition is distinct from every other condition in the framework because it concerns not what the venture builds but who decides what the venture builds, and because it becomes binding precisely at the moments when the other conditions are being satisfied. A venture that raises no capital faces no capital-capture hazard, and a venture that raises the capital an insatiable mission demands faces the hazard in its most acute form. The article walks the SpaceX control trajectory through the 2002 founding capital structure, the dual-class share architecture, the sequence of more than thirty financing rounds across the 2002 through drafting-date period, the January 2015 Google and Fidelity round that introduced strategic investors at scale, the semi-annual tender-offer liquidity mechanism that substitutes for a public listing, the repeatedly deferred initial-public-offering decision, and the Starlink separation question that remains open at the drafting date. The article contrasts the SpaceX configuration against the OpenAI governance failure of November 2023, in which a control structure designed explicitly to resist capital capture was tested and defeated within five days, and against the Tesla compensation litigation that illustrates the limits of founder control under public-company conditions. The article draws on the corporate-governance literature from [Berle and Means 1932][book_berle_means_1932] The Modern Corporation and Private Property through [Jensen and Meckling 1976][research_jensen_meckling_1976], [Grossman and Hart 1988][research_grossman_hart_1988] One Share-One Vote and the Market for Corporate Control, [Shleifer and Vishny 1997][research_shleifer_vishny_1997] A Survey of Corporate Governance, and [Bebchuk and Kastiel 2017][research_bebchuk_kastiel_2017] The Untenable Case for Perpetual Dual-Class Stock, and on the foundation-ownership literature that [Hansmann 1996][book_hansmann_1996] The Ownership of Enterprise frames. The article treats the Carl Zeiss Stiftung of 1889, the Robert Bosch ownership separation, and the Novo Nordisk Foundation structure as the centurial precedents for a control configuration that has survived across multiple generations of capital formation. The article closes with an explicit pattern-extraction section stating the abstract governance mechanic in a form other informed readers can recognize in adjacent domains without naming any downstream application.

## The Governance Mapping Problem

The mapping problem for a comprehensive treatment of the governance condition in the SpaceX case is the question of which control instruments the firm adopted, how the instruments behaved across the sequence of financing events that the mission required, and whether the instruments in fact prevented a redirection of the mission that would otherwise have occurred. The third element is the difficult one. A control configuration that is never tested provides no evidence that it works, and the counterfactual in which the capital providers attempt a redirection and fail is not directly observable for a firm in which the attempt was never made.

The problem admits several formalizations depending on the analytical tradition consulted. The agency tradition from [Berle and Means 1932][book_berle_means_1932] through [Jensen and Meckling 1976][research_jensen_meckling_1976] Theory of the Firm and [Fama and Jensen 1983][research_fama_jensen_1983] Separation of Ownership and Control treats the governance property as the alignment configuration between the manager and the residual claimants, and treats founder control as an agency problem rather than as a solution. The incomplete-contracts tradition from [Grossman and Hart 1986][research_grossman_hart_1986] The Costs and Benefits of Ownership and [Hart and Moore 1990][research_hart_moore_1990] Property Rights and the Nature of the Firm through [Hart 1995][book_hart_1995] Firms Contracts and Financial Structure treats the governance property as the allocation of residual control rights over decisions that the financing contracts do not specify. The security-benefits tradition from [Grossman and Hart 1988][research_grossman_hart_1988] and [Harris and Raviv 1988][research_harris_raviv_1988] Corporate Governance Voting Rights and Majority Rules treats the one-share-one-vote configuration as the arrangement that maximizes the security benefits and treats every deviation as a transfer toward the private benefits of control. The law-and-finance tradition from [La Porta Lopez-de-Silanes Shleifer and Vishny 1998][research_laporta_et_al_1998] Law and Finance treats the governance property as a function of the legal regime within which the firm incorporates. The present article draws on all four traditions while adopting the mission-oriented-innovation framework the [series opener][related_post_a281_spacex_framing] established as the primary organizing structure, and it departs from the agency tradition on the question of whose objective function is normative.

The general form of the governance mapping problem can be stated compactly. Let $e_i(t)$ denote the cash-flow share of the claimant $i$ at time $t$, and let $v_i(t)$ denote the voting share of the claimant $i$ at time $t$. The control wedge may be written

$$w_i(t) = \frac{v_i(t)}{e_i(t)}$$

with $w_i = 1$ under the one-share-one-vote configuration, $w_i > 1$ for a claimant whose voting rights exceed the economic exposure, and $w_i < 1$ for a claimant in the complementary position. The governance condition the article treats requires that the founder wedge be sufficiently large that the control condition

$$v^{\text{founder}}(t) > \tfrac{1}{2} \qquad \forall t \in [t_0, T]$$

holds across the entire financing horizon, and not merely at the founding.

The difficulty the condition addresses is that the cash-flow share declines mechanically with each financing round. Let $\delta_n$ denote the dilution fraction of the round $n$. The cash-flow share follows the recursion

$$e^{\text{founder}}_n = e^{\text{founder}}_{n-1} \left( 1 - \delta_n \right) \qquad \text{so} \qquad e^{\text{founder}}_N = e^{\text{founder}}_0 \prod_{n=1}^{N} \left( 1 - \delta_n \right)$$

with the product declining monotonically in the round count. Under a one-share-one-vote configuration the voting share follows the identical recursion, and the control condition therefore fails at a finite round count determined by the initial share and the per-round dilution. Under a dual-class configuration in which the issued shares carry inferior voting rights, the voting recursion decouples from the cash-flow recursion, and the control condition can hold for arbitrarily large $N$.

The decoupling takes the compact statement

$$\frac{\partial v^{\text{founder}}}{\partial \delta_n} \approx 0 \qquad \text{while} \qquad \frac{\partial e^{\text{founder}}}{\partial \delta_n} < 0$$

with the voting share substantially insensitive to the dilution that the cash-flow share absorbs. The decoupling is the whole of the technical content of the dual-class instrument, and the remainder of the analytical question concerns what the decoupling is used for.

The capital-capture event that the condition is designed to prevent permits definition as a change in the mission objective attributable to the preferences of the capital providers. Let $M(t)$ denote the mission objective and let $\mathcal{F}_t$ denote the information available at time $t$. The capture indicator has the concise form

$$\kappa(t) = \mathbb{1}\!\left[ M(t) \neq M(t^-) \; \wedge \; \Delta M \in \arg\max_{M'} \sum_{i \neq \text{founder}} e_i \cdot U_i(M') \right]$$

taking the value unity when the mission changes and the change moves toward the capital-weighted preference of the non-founder claimants. The SpaceX record exhibits $\kappa(t) = 0$ across the observed period, which is the empirical claim the article defends and the claim whose interpretation is contested, because an unchanged mission is equally consistent with an effective control configuration and with an absence of any capital provider who wished to change it.

The identification problem is therefore acute. The counterfactual differential takes the form

$$\Delta V^{\text{governance}}_i(t) = V^{\text{observed}}_i(t) - V^{\text{capture counterfactual}}_i(t)$$

with the attribution equal to the difference between the observed trajectory and the counterfactual trajectory under a one-share-one-vote configuration facing the identical financing sequence. The counterfactual specifications the article treats include an investor-controlled counterfactual in which the board redirects the venture toward the near-term commercial opportunity, an acquisition counterfactual in which the venture is sold to an incumbent, and a public-market counterfactual in which the quarterly reporting cycle constrains the investment horizon.

## Methodological Commitments

The article commits to the same seven methodological positions that the [series opener][related_post_a281_spacex_framing] established for the series as a whole. These commitments are restated here at compact reference level, with attention to the ways the governance material strains them.

The first commitment is descriptive-analytical framing rather than prescriptive advocacy. The commitment is harder to honor in the governance material than elsewhere in the series, because the corporate-governance literature is substantially normative and because the dual-class instrument the article describes is the subject of an active policy dispute. The article describes what the instrument did in the case and declines to recommend it.

The second commitment is dual-register composition with both general-history and abstract-mechanic registers.

The third commitment is primary-source anchoring. The article cites primary sources for each substantive claim with preference for the [Delaware General Corporation Law][ref_dgcl] provisions that authorize the instruments, the [Texas Business Organizations Code][ref_texas_boc] provisions relevant to the reported reincorporation, the [Delaware Court of Chancery][ref_delaware_chancery] record, the [Securities and Exchange Commission EDGAR][ref_sec_edgar] filings and the [Form D exempt-offering][ref_sec_form_d] regime under which the private rounds were conducted, the [Securities Act private-placement exemption][ref_securities_act_4a2] and the [Regulation D][ref_reg_d] rules that authorize them, the [Exchange Act registration-threshold provision][ref_exchange_act_12g] that determines when a private issuer becomes a reporting company, the [Delaware Division of Corporations][ref_delaware_division_corporations] and [Texas Secretary of State][ref_texas_sos] filing systems, the [SEC investor-education materials][ref_sec_investor_gov], the [SpaceX news archive][ref_spacex_news_archive], the [OpenAI charter][ref_openai_charter] and [OpenAI announcements][ref_openai_news], the [Carl Zeiss Stiftung][ref_carl_zeiss_stiftung] documentation, the [Robert Bosch Stiftung][ref_bosch_stiftung] and [Bosch corporate][ref_bosch_company] documentation, and the [Novo Nordisk Foundation][ref_novo_nordisk_foundation] and [Novo Holdings][ref_novo_holdings] documentation. The article draws on secondary sources including [Berger 2021][book_berger_2021] Liftoff, [Berger 2024][book_berger_2024] Reentry, [Vance 2015][book_vance_2015] Elon Musk, [Isaacson 2023][book_isaacson_2023] Elon Musk, [Davenport 2018][book_davenport_2018] The Space Barons, and [Fernholz 2018][book_fernholz_2018] Rocket Billionaires.

The fourth commitment is contested-claim marking. The commitment binds more heavily in this article than in any other in the series. The SpaceX ownership percentages, the voting percentages, the round valuations, and the share-class terms are not disclosed by the firm and are reconstructed from trade-press reporting, state-level filings, and investor communications that reach the public record indirectly. Every numerical claim about the capital structure in this article is a reconstructive estimate and is marked as such.

The fifth commitment is temporal indexing as a mid-2026 snapshot. The governance material is more perishable than the technical material treated elsewhere in the series, because a single financing event or a single legal decision can alter the configuration.

The sixth commitment is terminological transparency with the Terminological Note section below. The governance vocabulary is unusually contested, and terms including control, ownership, and independence carry different meanings across the legal, financial-economic, and organizational literatures.

The seventh commitment is thesis-not-proof framing of the governance closure claim. The claim that the control configuration prevented a capture that would otherwise have occurred is not demonstrable from the available record and is advanced as an interpretation consistent with the record.

## Governance as an Economic Property

The governance property is treated in the article as an economic property of a firm's control allocation that distinguishes ventures able to sustain a mission objective across an extended financing sequence from ventures whose objective is reset by the preferences of whichever capital providers hold the decisive claim at each stage. The property allows formal characterization, measurement, and comparison across firms and legal regimes.

The formal characterization begins from the separation of the two rights that a share ordinarily bundles. The cash-flow right entitles the holder to a fraction of the residual, and the control right entitles the holder to a fraction of the decision authority. The aggregate identities are

$$\sum_i e_i = 1 \qquad \text{and} \qquad \sum_i v_i = 1$$

with the two distributions coinciding under one-share-one-vote and diverging under every deviation from it. The aggregate wedge across the claimant set can be written as

$$W = \sum_i \left| v_i - e_i \right|$$

taking the value zero under one-share-one-vote and increasing in the degree of separation. The measure is symmetric across claimants and therefore does not by itself indicate who holds the excess control.

The security-benefits argument that [Grossman and Hart 1988][research_grossman_hart_1988] and [Harris and Raviv 1988][research_harris_raviv_1988] develop holds that the one-share-one-vote configuration is optimal because it aligns the decision authority with the economic exposure and thereby causes the controlling party to internalize the consequences of the decisions. The argument can be stated as the condition under which a controller approves a project

$$e^{\text{controller}} \cdot \Delta V^{\text{security}} + \Delta B^{\text{private}} > 0$$

with $\Delta V^{\text{security}}$ the change in the total security value and $\Delta B^{\text{private}}$ the change in the private benefits accruing to the controller alone. Under one-share-one-vote with a majority holder the first term dominates and the controller approves substantially the value-increasing projects. As $e^{\text{controller}}$ falls while $v^{\text{controller}}$ is held fixed, the first term shrinks and the private-benefit term becomes decisive at a threshold

$$e^{\text{controller}} < \frac{-\Delta B^{\text{private}}}{\Delta V^{\text{security}}}$$

below which the controller rejects value-increasing projects that reduce the private benefits and approves value-decreasing projects that increase them. The inequality is the formal core of the case against dual-class structures, and the SpaceX configuration sits deep inside the region the inequality identifies as hazardous.

The counterargument the article develops does not deny the inequality. The counterargument holds that the quantity the inequality labels a private benefit is in the mission-directed case the object the venture exists to pursue, and that the security value against which it is compared is measured over a horizon shorter than the mission horizon. Let $\rho^{\text{controller}}$ and $\rho^{\text{investor}}$ denote the discount rates the two parties apply. The horizon divergence has the form

$$\rho^{\text{controller}} < \rho^{\text{investor}} \implies \exists \; \text{projects with} \; \text{NPV}_{\rho^{\text{controller}}} > 0 > \text{NPV}_{\rho^{\text{investor}}}$$

with a nonempty set of projects that the controller values positively and the diversified investor values negatively. The reusability development that the [Value Gradient article A282][related_post_a282_spacex_value_gradient] treats and the Starship development that the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats both occupy that set across substantial portions of their development periods.

The mission-persistence probability may be written

$$P^{\text{persistence}}(T) = \prod_{n=1}^{N(T)} \left[ 1 - q_n \right]$$

with $q_n$ the probability that the financing round $n$ produces a mission redirection. Under a one-share-one-vote configuration the hazard $q_n$ rises with the cumulative dilution, because the coalition required to redirect becomes progressively easier to assemble. Under a dual-class configuration the hazard remains substantially constant and near zero across rounds, and the persistence probability therefore does not decay with the financing intensity that an insatiable mission demands.

The control-contestability measure admits the compact form

$$C^{\text{contest}} = \min \left\{ \sum_{i \in S} v_i \; : \; S \subseteq \mathcal{I} \setminus \{\text{founder}\}, \; \sum_{i \in S} v_i > \tfrac{1}{2} \right\}$$

giving the smallest voting mass a coalition excluding the founder must assemble to prevail. The measure is infinite, in the sense that no such coalition exists, whenever the founder holds a majority of votes. The SpaceX configuration at the drafting date is reported to place the measure in that regime, and the OpenAI arrangement of November 2023 placed it in a regime where the formal measure suggested contestability was impossible while the effective measure proved otherwise.

The distinction between the formal and the effective control measures is the analytical contribution the OpenAI counter-example offers. The effective control takes the form

$$v^{\text{effective}}_i = f\!\left( v^{\text{formal}}_i, \; d_i, \; \sigma_i \right)$$

with $d_i$ the resource dependence of the organization on the party $i$ and $\sigma_i$ the credibility of the party's threat to withdraw. A party holding zero formal votes but supplying a resource without which the organization cannot operate holds an effective control that the formal measure does not register.

## Cross-Disciplinary Framings

The governance property can be characterized from several disciplinary traditions beyond the mission-oriented-innovation framework the series adopts as primary.

The agency tradition traces from [Berle and Means 1932][book_berle_means_1932] The Modern Corporation and Private Property through [Jensen and Meckling 1976][research_jensen_meckling_1976] Theory of the Firm Managerial Behavior Agency Costs and Ownership Structure, [Fama and Jensen 1983][research_fama_jensen_1983] Separation of Ownership and Control, [Jensen 1986][research_jensen_1986] Agency Costs of Free Cash Flow, and the survey in [Shleifer and Vishny 1997][research_shleifer_vishny_1997] A Survey of Corporate Governance. The framing treats the separation of ownership from control as the central problem of the modern corporation and treats the governance apparatus as the set of instruments that mitigate it. The agency cost admits the compact decomposition

$$AC = C^{\text{monitoring}} + C^{\text{bonding}} + L^{\text{residual}}$$

with the monitoring expenditure borne by the principal, the bonding expenditure borne by the agent, and the residual loss equal to the remaining divergence. The framing classifies the SpaceX configuration as one in which the monitoring and bonding instruments are substantially disabled by design, so that the residual-loss term carries the entire burden. The framing gives the sharpest available statement of what the configuration risks.

The incomplete-contracts and property-rights tradition traces from [Coase 1937][research_coase_1937] The Nature of the Firm through [Williamson 1975][research_williamson_1975] Markets and Hierarchies, [Williamson 1985][book_williamson_1985] The Economic Institutions of Capitalism, [Grossman and Hart 1986][research_grossman_hart_1986], [Hart and Moore 1990][research_hart_moore_1990], and [Hart 1995][book_hart_1995] Firms Contracts and Financial Structure. The framing treats the control right as valuable precisely because the financing contracts cannot specify the actions to be taken in the contingencies that a long-horizon development program encounters. The residual-control allocation can be written as

$$\text{RC} = \left\{ a \in \mathcal{A} \; : \; a \notin \text{dom}(\text{contract}) \right\}$$

with the residual set comprising the actions the contract does not address. The framing provides the most useful account of why a mission-directed venture values control disproportionately, because the mission is a statement about the behavior in unforeseen contingencies and is therefore precisely the object that a contract cannot secure.

The law-and-finance tradition traces from [La Porta Lopez-de-Silanes Shleifer and Vishny 1998][research_laporta_et_al_1998] Law and Finance through the comparative-governance literature and treats the control configuration as a function of the legal regime. The Delaware regime that the [Delaware General Corporation Law][ref_dgcl] establishes permits the issuance of multiple classes with differential voting rights substantially without constraint, and the permissiveness is a competitive product of the state-charter market that [Roe 1994][book_roe_1994] Strong Managers Weak Owners and [Easterbrook and Fischel 1991][book_easterbrook_fischel_1991] The Economic Structure of Corporate Law analyze from opposing positions. The investor-protection index the tradition constructs has the form

$$IP_j = \sum_{k} \omega_k \cdot \mathbb{1}\!\left[ \text{protection } k \text{ present in regime } j \right]$$

with the weighted sum across the protection set. The United States regime scores highly on the index while permitting the dual-class deviation, which establishes that the index measures the protection of minority claimants against expropriation rather than the allocation of control as such. The comparative regimes differ materially. The [United Kingdom Companies Act 2006][ref_uk_companies_act_2006] and the listing regime built on it have historically constrained the instrument far more tightly, the German [Aktiengesetz][ref_german_aktiengesetz] restricts multiple-voting arrangements in ways the Delaware regime does not, and the [European Union Shareholder Rights Directive][ref_eu_shareholder_rights_directive] establishes an engagement framework with no Delaware analogue. The [OECD Principles of Corporate Governance][ref_oecd_corporate_governance] supply the international benchmark against which the regimes are compared.

The dual-class empirical tradition traces from [DeAngelo and DeAngelo 1985][research_deangelo_deangelo_1985] Managerial Ownership of Voting Rights through [Gompers Ishii and Metrick 2003][research_gompers_ishii_metrick_2003] Corporate Governance and Equity Prices, [Gompers Ishii and Metrick 2010][research_gompers_ishii_metrick_2010] Extreme Governance An Analysis of Dual-Class Firms in the United States, [Bebchuk Kraakman and Triantis 2000][research_bebchuk_kraakman_triantis_2000] Stock Pyramids Cross-Ownership and Dual Class Equity, and [Bebchuk and Kastiel 2017][research_bebchuk_kastiel_2017] The Untenable Case for Perpetual Dual-Class Stock. The framing offers the empirical record against which the SpaceX configuration should be assessed. The central empirical finding is that the firm value declines in the wedge and that the decline steepens with the time elapsed since the initial public offering, which motivates the sunset provisions the policy literature recommends. The value relation may be written

$$\frac{\partial q}{\partial w} < 0 \qquad \text{and} \qquad \frac{\partial^2 q}{\partial w \, \partial \tau} < 0$$

with $q$ a valuation ratio, $w$ the wedge, and $\tau$ the time since listing. The SpaceX case lies outside the estimation sample because the firm has never listed, and the applicability of the finding to an unlisted firm is precisely the question the article must address rather than assume.

The bargaining tradition traces from [Nash 1950][research_nash_1950] The Bargaining Problem through [Rubinstein 1982][research_rubinstein_1982] Perfect Equilibrium in a Bargaining Model, [Binmore Rubinstein and Wolinsky 1986][research_binmore_rubinstein_wolinsky_1986] The Nash Bargaining Solution in Economic Modelling, [Osborne and Rubinstein 1990][book_osborne_rubinstein_1990] Bargaining and Markets, and [Muthoo 1999][book_muthoo_1999] Bargaining Theory with Applications. The framing treats the control terms as the outcome of a negotiation between the founder and the investors whose outcome depends on the outside options each party holds. The split permits the concise form

$$\left( u^{\text{founder}}, u^{\text{investor}} \right) = \arg\max \left( u^{\text{founder}} - d^{\text{founder}} \right)^{\beta} \left( u^{\text{investor}} - d^{\text{investor}} \right)^{1-\beta}$$

with $d$ the disagreement payoffs and $\beta$ the relative bargaining power. The framing gives the explanation for why the control terms tightened rather than loosened across the SpaceX financing sequence, because the founder disagreement payoff improved as the venture demonstrated capability while the investor disagreement payoff deteriorated as the competing investment opportunities in the sector failed to materialize.

The entrepreneurial-finance tradition traces from [Sahlman 1990][research_sahlman_1990] The Structure and Governance of Venture-Capital Organizations through [Gompers 1995][research_gompers_1995] Optimal Investment Monitoring and the Staging of Venture Capital, [Kaplan and Stromberg 2003][research_kaplan_stromberg_2003] Financial Contracting Theory Meets the Real World, [Kaplan and Stromberg 2004][research_kaplan_stromberg_2004] Characteristics Contracts and Actions, [Lerner 1994][research_lerner_1994_syndication] The Syndication of Venture Capital Investments, [Gompers and Lerner 2001][book_gompers_lerner_2001] The Money of Invention, and [Metrick and Yasuda 2011][book_metrick_yasuda_2011] Venture Capital and the Finance of Innovation. The framing treats the control allocation as one term in a bundle that also comprises the liquidation preferences, the board composition, the protective provisions, and the staging structure. The observation the framing yields is that the staged-financing instrument that [Gompers 1995][research_gompers_1995] identifies as the principal investor control device operates independently of the voting rights, because an investor who declines to fund the next round exercises a control that no share class can neutralize. The staged control takes the form

$$v^{\text{staged}}_i(t) = \mathbb{1}\!\left[ k_i(t) > 0 \right] \cdot \frac{k_i(t)}{\sum_j k_j(t)}$$

with the investor's effective influence at the round proportional to the share of the required capital the investor yields, and independent of any voting arithmetic. The instrument is neutralized only by the breadth of the investor base, because a required capital that many parties are willing to supply gives no single party the withholding threat.

The private-markets and listing-choice tradition traces from [Ewens and Farre-Mensa 2020][research_ewens_farre_mensa_2020] The Deregulation of the Private Equity Markets and the Decline in IPOs and treats the decision to remain private as a rational response to the expansion of the private capital supply. The framing contributes the most direct explanation for the SpaceX listing deferral, because a firm that can raise the capital it requires privately obtains the capital without incurring the governance obligations that a listing imposes.

The foundation-ownership tradition traces from [Hansmann 1996][book_hansmann_1996] The Ownership of Enterprise and treats the class of firms in which the controlling owner is a foundation with no personal residual claimant. The framing contributes the only substantial body of evidence on the question of whether a control configuration insulated from the capital market can persist across generations, and the evidence is the centurial European record the Foundation-Ownership Precedents section treats. The defining feature of the class can be stated as

$$\nexists \; i \; : \; e_i > 0 \; \wedge \; i \in \text{natural persons}$$

with no natural person holding a residual claim. The consequence is that the agency apparatus, which derives its predictions from the divergence between a manager's objective and a residual claimant's objective, has no residual claimant to anchor the comparison and therefore makes no determinate prediction about the class.

The organizational-institutionalism tradition traces from [Selznick 1949][book_selznick_1949] TVA and the Grass Roots through [Hargrove 1994][book_hargrove_1994] Prisoners of Myth, [Fligstein 2001][book_fligstein_2001] The Architecture of Markets, and [Chandler 1962][book_chandler_1962] Strategy and Structure, [Chandler 1977][book_chandler_1977] The Visible Hand, and [Chandler 1990][book_chandler_1990] Scale and Scope. The framing treats the mission as an organizational commitment that is sustained or eroded by the processes through which the organization adapts to its environment, and it provides the vocabulary of goal displacement that names the failure mode the governance condition is intended to prevent. The displacement can be written as

$$D(t) = \left\| M^{\text{enacted}}(t) - M^{\text{chartered}} \right\|$$

with the distance between the mission the organization enacts and the mission it was constituted to pursue. The measure is what the governance apparatus is intended to hold near zero, and the difficulty of specifying it operationally is precisely the fifth sub-property the pattern-extraction section states.

The financial-sociology tradition traces from [MacKenzie 2006][book_mackenzie_2006] An Engine Not a Camera through [Ho 2009][book_ho_2009] Liquidated, [Zaloom 2006][book_zaloom_2006] Out of the Pits, [Preda 2009][book_preda_2009] Framing Finance, and [Krippner 2011][book_krippner_2011] Capitalizing on Crisis. The framing treats the capital-market pressures as culturally and institutionally constituted rather than as a natural force, and it offers the account of the quarterly-reporting horizon as an artifact of a set of practices rather than as a necessary feature of public ownership.

The resource-based and dynamic-capabilities tradition traces from [Penrose 1959][book_penrose_1959] The Theory of the Growth of the Firm through [Wernerfelt 1984][research_wernerfelt_1984] A Resource-Based View of the Firm, [Barney 1991][research_barney_1991] Firm Resources and Sustained Competitive Advantage, [Peteraf 1993][research_peteraf_1993] The Cornerstones of Competitive Advantage, [Teece Pisano and Shuen 1997][research_teece_pisano_shuen_1997] Dynamic Capabilities and Strategic Management, [Eisenhardt and Martin 2000][research_eisenhardt_martin_2000], [Helfat and Peteraf 2003][research_helfat_peteraf_2003], [Winter 2003][research_winter_2003], [Teece 2007][research_teece_2007], and [Teece 2018][research_teece_2018]. The framing gives the account of why the control question is more consequential for this class of firm than for a firm whose assets are redeployable. A capability accumulated against a mission is to that mission, so that a redirection destroys the accumulated value rather than merely reallocating it. The asset specificity is what converts a governance question from a distributional matter into an efficiency matter.

The real-options tradition traces from [Myers 1977][research_myers_1977] Determinants of Corporate Borrowing through [Black and Scholes 1973][research_black_scholes_1973], [Merton 1973][research_merton_1973], [McDonald and Siegel 1986][research_mcdonald_siegel_1986] The Value of Waiting to Invest, [Kogut and Kulatilaka 1994][research_kogut_kulatilaka_1994], [Dixit and Pindyck 1994][book_dixit_pindyck_1994] Investment Under Uncertainty, [Trigeorgis 1996][book_trigeorgis_1996] Real Options, and [Copeland and Antikarov 2001][book_copeland_antikarov_2001] Real Options A Practitioner's Guide. The framing treats the retained control as an option whose value derives from the asymmetry between a controller who can act on a contingency and a controller who cannot.

The procurement and contract-economics tradition traces from [Laffont and Tirole 1993][book_laffont_tirole_1993] A Theory of Incentives in Procurement and Regulation and [McAfee and McMillan 1988][book_mcafee_mcmillan_1988] Incentives in Government Contracting through [Myerson 1981][research_myerson_1981] Optimal Auction Design, [Milgrom 2004][book_milgrom_2004] Putting Auction Theory to Work, [Bajari and Tadelis 2001][research_bajari_tadelis_2001], [Bajari McMillan and Tadelis 2009][research_bajari_mcmillan_tadelis_2009], [Corts and Singh 2004][research_corts_singh_2004], [Kalnins and Mayer 2004][research_kalnins_mayer_2004], [Levin and Tadelis 2010][research_levin_tadelis_2010], [Che and Chung 1999][research_che_chung_1999], and [Gagnepain and Ivaldi 2002][research_gagnepain_ivaldi_2002]. The framing is relevant because the state customer that the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] treats is itself a party with an interest in the provider's governance, and procurement regimes impose organizational-conflict-of-interest and foreign-ownership constraints that operate as a governance instrument entirely outside the corporate-law channel.

The institutional-economics tradition traces from [North 1990][book_north_1990] Institutions Institutional Change and Economic Performance through [Ostrom 1990][book_ostrom_1990] Governing the Commons, [Greif 2006][book_grief_2006] Institutions and the Path to the Modern Economy, and [Acemoglu and Robinson 2012][book_acemoglu_robinson_2012] Why Nations Fail. The framing treats the corporate form as one institution among many for organizing a long-horizon collective undertaking, and it yields the comparative frame within which the foundation, the chartered company, the cooperative, and the state agency are alternatives to the investor-owned corporation rather than deviations from it.

The innovation-systems and mission-oriented tradition traces from [Schumpeter 1942][book_schumpeter_1942] Capitalism Socialism and Democracy through [Freeman 1987][book_freeman_1987] Technology Policy and Economic Performance, [Lundvall 1992][book_lundvall_1992] National Systems of Innovation, [Nelson 1993][book_nelson_1993] National Innovation Systems, [Mowery and Rosenberg 1998][book_mowery_rosenberg_1998] Paths of Innovation, [Perez 2002][book_perez_2002] Technological Revolutions and Financial Capital, [Ruttan 2006][book_ruttan_2006] Is War Necessary for Economic Growth, [Weiss 2014][book_weiss_2014] America Inc, [Hartley 2017][book_hartley_2017] The Economics of Arms, [Mazzucato 2013][book_mazzucato_2013] The Entrepreneurial State, and [Mazzucato 2021][book_mazzucato_2021] Mission Economy. The [Schumpeter 1942][book_schumpeter_1942] argument that the large firm insulated from competitive pressure is the efficient locus of innovation is the closest antecedent in the economics literature to the claim the governance condition makes, and the fact that the argument has been contested for eight decades is a reason for caution rather than an endorsement. The [Perez 2002][book_perez_2002] treatment of the relationship between financial capital and production capital across a technological surge supplies the macro-level frame within which the tension between the controller's horizon and the investor's horizon is an instance of a recurring pattern rather than an idiosyncrasy of this firm.

The professions and organizational-culture tradition traces from [Larson 1977][book_larson_1977] The Rise of Professionalism and [Abbott 1988][book_abbott_1988] The System of Professions through [Kunda 1992][book_kunda_1992] Engineering Culture. The framing treats the engineering workforce as a party with its own claims and its own normative commitments rather than as a factor of production, and it contributes the analytical basis for the resource-dependence account that the OpenAI counter-example requires. The workforce is the third party to the founder-investor bargain, and the governance literature substantially omits it.

## The Founding Capital Structure 2002 through 2008

The founding capital structure established the initial conditions from which the subsequent control trajectory follows. The firm was incorporated in the state of Delaware in the 2002 period as Space Exploration Technologies Corporation, under the [Delaware General Corporation Law][ref_dgcl] regime whose permissiveness toward differential voting rights the preceding section describes. The founding capital was supplied substantially by the founder from the proceeds of prior ventures, in an amount that the biographical treatments in [Berger 2021][book_berger_2021] Liftoff, [Vance 2015][book_vance_2015] Elon Musk, and [Isaacson 2023][book_isaacson_2023] Elon Musk place at approximately 100 million dollars across the initial period. The figure is a reconstructive estimate.

The significance of the self-funded founding for the governance condition is that it establishes the initial control condition at its maximum. The founding wedge satisfies

$$w^{\text{founder}}(t_0) = \frac{v^{\text{founder}}(t_0)}{e^{\text{founder}}(t_0)} = 1 \qquad \text{with} \qquad e^{\text{founder}}(t_0) \approx 1$$

so that the control condition holds trivially without any instrument. The dual-class apparatus is unnecessary at the founding and becomes necessary only as the cash-flow share declines. The observation matters because it establishes the sequence. The control instruments were adopted in anticipation of a dilution that had not yet occurred, which distinguishes the case from the pattern in which a control instrument is adopted defensively after a threat materializes.

The 2002 through 2008 period is treated at length in the [series opener][related_post_a281_spacex_framing] as the pre-anchor prologue and in the [Value Gradient article A282][related_post_a282_spacex_value_gradient] as the Falcon 1 development period. The governance-relevant feature of the period is that the firm raised substantially little external capital across it, and that the external capital it did raise arrived at the moment of maximum distress. The August 2008 Founders Fund investment, which the Patient-Private Capital-Formation Leg article A290 will treat in detail, occurred between the third and fourth Falcon 1 flights, at a point when the firm's remaining cash was measured in weeks.

The timing of the investment relative to the cash position is what determines the bargaining position, and the relationship has the form

$$\Theta = \frac{C^{\text{cash on hand}}}{\dot{C}^{\text{burn}}}$$

with $\Theta$ the runway measured in time and the founder's bargaining power declining as $\Theta$ approaches zero. The runway at the moment of the 2008 investment is reported in the biographical treatments as measured in weeks rather than in quarters. The bargaining position at that moment was as unfavorable to the founder as it would ever be. The disagreement payoff for the founder approached the liquidation value of the firm, and the standard prediction of the bargaining apparatus the preceding section states is that the investor should have extracted control terms in proportion. The terms that were in fact agreed did not transfer control. The divergence between the predicted and the observed outcome is the most analytically interesting feature of the early financing record, and the available explanations comprise the investor's own stated preference for founder-led governance, the idiosyncratic composition of the investor set, and the possibility that the founder's willingness to continue funding the venture personally supplied a credible outside option that the distress did not eliminate. The third explanation may be stated compactly

$$d^{\text{founder}} = \max\left\{ V^{\text{liquidation}}, \; V^{\text{self-funded continuation}} \right\}$$

with the second term nonzero only for a founder possessing independent resources. The term is the structural reason that wealthy founders obtain better control terms than equally capable founders without independent means, and it is a feature of the case that limits its transferability.

## The Dual-Class Share Architecture

The control instrument the firm adopted is a multiple-class common-stock structure in which the classes carry differential voting rights. The instrument is authorized by the [Delaware General Corporation Law][ref_dgcl] provisions governing the certificate of incorporation in [subchapter I][ref_dgcl_sc01], the classes and series of stock in [subchapter V][ref_dgcl_sc05], the voting rights in [subchapter VII][ref_dgcl_sc07], and the directors and officers in [subchapter IV][ref_dgcl_sc04]. The instrument is available to any Delaware corporation without any showing of purpose, and the chartering process is administered through the [Delaware Division of Corporations][ref_delaware_division_corporations].

The reported configuration places the founder holding at approximately 42 percent of the outstanding equity and approximately 79 percent of the voting power as of the early 2020s, corresponding to a wedge of

$$w^{\text{founder}} = \frac{v^{\text{founder}}}{e^{\text{founder}}} \approx \frac{0.79}{0.42} \approx 1.9$$

and to a control condition satisfied with substantial margin. Both figures are reconstructive estimates drawn from the trade-press reporting and investor communications rather than from any disclosure, and the precise class structure and the per-class voting ratios are not public. The reported reincorporation of the firm from the state of Delaware to the state of Texas in the 2024 period, which the [Texas Business Organizations Code][ref_texas_boc] would govern, is reported rather than documented in a public filing available to the article, and the corresponding registry is the [Texas Secretary of State][ref_texas_sos]. The corporate identity and the public-facing corporate materials appear at the [SpaceX corporate site][ref_spacex_company].

The general form of the two-class arrangement supports compact statement. Let $n_A$ and $n_B$ denote the share counts of the superior and inferior classes and let $\lambda$ denote the votes per superior share with the inferior share carrying one vote. The voting share of a holder of the entire superior class is

$$v = \frac{\lambda \, n_A}{\lambda \, n_A + n_B}$$

and the corresponding cash-flow share is $e = n_A / (n_A + n_B)$ under the assumption of equal economic rights across classes. The control condition $v > 1/2$ reduces to the requirement

$$\frac{n_A}{n_B} > \frac{1}{\lambda}$$

so that a tenfold voting ratio permits the control condition to hold while the founder holds slightly more than one eleventh of the outstanding shares. The arithmetic is the reason a dual-class structure sustains control across a dilution sequence that would otherwise terminate it, and it is the reason the policy literature regards the instrument as capable of producing arbitrarily large separations.

The instrument is not unlimited in its effect. The staged-financing control that [Gompers 1995][research_gompers_1995] identifies operates through the investor's decision whether to fund the subsequent round rather than through any vote, and the instrument therefore does not neutralize it. The protective provisions customary in preferred-stock financings confer class-level veto rights over enumerated actions including liquidation, charter amendment, and creation of senior securities, and the provisions operate irrespective of the common-stock voting arithmetic. The fiduciary duties that the [Delaware Court of Chancery][ref_delaware_chancery] enforces constrain the controller in transactions in which the controller stands on both sides. The control the instrument confers is therefore a control over the ordinary business and the board composition rather than an unconditional authority.

## The Financing Sequence and Dilution Management

The financing sequence comprises more than thirty rounds across the 2002 through drafting-date period. The rounds are conducted as private placements exempt from registration under the [Securities Act private-placement exemption][ref_securities_act_4a2] and the [Regulation D][ref_reg_d] safe harbor, and specifically under the [Rule 506][ref_rule_506] provisions that permit an unlimited offering amount to accredited investors. The existence and approximate size of many of the rounds reaches the public record through the [Form D][ref_sec_form_d] notice filings and the state-level filings that the [Securities and Exchange Commission EDGAR][ref_sec_edgar] system and state regulators publish. The terms are not published.

The employee equity compensation that the firm issues operates under a separate exemption in [Rule 701][ref_rule_701], and the subsequent resale of the restricted securities so issued operates under [Rule 144][ref_rule_144]. The two rules together constitute the machinery by which an unlisted firm can compensate a large workforce in equity, and they are as load-bearing for the configuration as the voting instrument itself. A firm unable to issue and later permit the resale of employee equity could not retain a technical workforce across a decade-scale private period.

The reported valuation trajectory rises from a figure in the hundreds of millions of dollars across the late 2000s, through approximately 12 billion dollars at the January 2015 round, approximately 33 billion dollars in the 2019 period, approximately 100 billion dollars in the 2021 period, approximately 127 billion dollars in the 2022 period, approximately 180 billion dollars in the late 2023 period, approximately 210 billion dollars in the mid 2024 period, and approximately 350 billion dollars in the late 2024 period, with subsequent rounds at higher figures. Every figure in the sequence is a reconstructive estimate drawn from trade-press reporting of tender-offer prices and primary-round terms.

The analytically important feature of the sequence is not the valuation trajectory but the relationship between the capital raised and the voting rights transferred. The cumulative capital raised across the sequence may be written

$$K^{\text{cumulative}} = \sum_{n=1}^{N} k_n$$

and the cumulative voting transferred yields the compact form

$$\Delta v^{\text{transferred}} = \sum_{n=1}^{N} \Delta v_n \approx 0$$

with the second sum near zero despite the first sum reaching the tens of billions of dollars. The ratio

$$\eta = \frac{\Delta v^{\text{transferred}}}{K^{\text{cumulative}}}$$

is the quantity the governance condition requires to be small, and it is the quantity that distinguishes the SpaceX financing history from the ordinary venture-financing history in which the ratio is bounded below by the pro-rata relationship between capital and equity.

The investor set across the sequence has broadened from a small group of venture funds to a set comprising sovereign wealth funds, mutual-fund complexes, corporate strategic investors, and family offices. The broadening is itself a governance instrument, because a dispersed investor base faces a coordination cost in assembling the coalition the contestability measure defines. The coordination cost takes the form

$$C^{\text{coalition}}(S) = \gamma \cdot |S| \cdot \left( 1 - h \right)$$

with $|S|$ the coalition size required and $h$ a concentration measure of the investor base. The cost rises as the base disperses, so that the dispersion supplements the voting arithmetic rather than merely accompanying it.

## The January 2015 Google and Fidelity Round

The January 2015 round in which the Google and Fidelity investors supplied approximately 1 billion dollars for approximately 10 percent of the firm constitutes the most analytically significant single financing event in the sequence, for three reasons.

The first reason is scale. The round was substantially larger than any prior round and established that the firm could raise the capital a constellation program would require without a public listing. The round arithmetic can be written as

$$V^{\text{post}} = \frac{k}{\delta} \qquad \text{and} \qquad V^{\text{pre}} = V^{\text{post}} - k$$

with $k$ the capital supplied and $\delta$ the fraction acquired, giving a post-money figure of approximately 10 billion dollars at the reported terms. The implied valuation of approximately 12 billion dollars is a reconstructive estimate and the spread between the arithmetic and the reported figure reflects the imprecision of the public reporting rather than any identified structural feature.

The second reason is that the round was motivated by a business line that did not yet exist. The Starlink constellation that the [Value Capture article A284][related_post_a284_spacex_value_capture] treats had been announced days before the round in the Seattle announcement, and the investor thesis was accordingly a bet on a future satellite-broadband business rather than on the existing launch-service business. The structure is an instance of the pattern the Portfolio-Patience article A288 will treat, in which a capability base supports an option on an adjacent business that the capital market prices before the business exists.

The third reason is that the round introduced a strategic corporate investor whose own business interests intersected the venture's. A strategic investor differs from a financial investor in that the objective function includes terms unrelated to the venture's own returns, which raises the capture hazard the governance condition addresses in its most concrete form. The hazard is stated compactly as

$$U^{\text{strategic}}_i = e_i \cdot V^{\text{venture}} + \phi_i \cdot V^{\text{own business}}$$

with $\phi_i$ the weight the strategic investor places on the effect of the venture's decisions on the investor's own business. The weight can be negative, in the case where the venture's success would damage the investor's existing position, and a strategic investor with a negative weight has an interest in slowing the venture that no financial investor shares. The control configuration is the instrument that renders the weight irrelevant, because an investor who cannot vote cannot act on the interest. The value the investors were purchasing was substantially an option on a business that did not yet exist, admitting the compact form

$$V^{\text{round}} = V^{\text{launch service}} + p^{\text{constellation}} \cdot \left[ V^{\text{constellation}} - K^{\text{deployment}} \right]^{+}$$

with the second term an option payoff weighted by the probability that the constellation reaches deployment. The structure is the reason a round of that size could be raised against a business line announced days earlier, and it is the reason the investors accepted terms conferring no control over the program whose success their return depended on.

The record does not indicate that any such attempt occurred. The analytical claim the article advances is the weaker one that the configuration made the attempt pointless rather than that the attempt was made and defeated.

## The Tender-Offer Liquidity Mechanism

The firm has conducted periodic tender offers, reported at approximately semi-annual frequency across the recent period, in which employees and early investors sell shares to incoming investors at a price the firm sets. The mechanism is the governance-critical innovation in the financing history and deserves treatment on its own terms. The issuer-tender-offer conduct is governed by the [Rule 13e-4][ref_rule_13e4] provisions and the [Regulation 14E][ref_reg_14e] antifraud and timing requirements, which apply to an issuer repurchase irrespective of whether the issuer is a reporting company, and the resale mechanics operate under [Rule 144][ref_rule_144].

The problem the mechanism solves is that a private firm's equity compensation is illiquid, and that the illiquidity becomes intolerable to employees as the holding period extends across the decade-scale horizon a mission-directed venture requires. The ordinary solution is a public listing, which provides the liquidity and simultaneously transfers the governance obligations that the condition seeks to avoid. The tender-offer mechanism decouples the two.

The decoupling allows the brief statement. Let $L$ denote the liquidity supplied to existing holders and let $G$ denote the governance obligations incurred. A public listing produces

$$\left( L^{\text{IPO}}, \; G^{\text{IPO}} \right) \qquad \text{with both terms large}$$

whereas the tender-offer mechanism produces

$$\left( L^{\text{tender}}, \; G^{\text{tender}} \right) \qquad \text{with} \qquad L^{\text{tender}} \lesssim L^{\text{IPO}}, \quad G^{\text{tender}} \approx 0$$

so that the mechanism obtains substantially the liquidity benefit at substantially none of the governance cost. The mechanism is available only to a firm whose shares command sufficient demand that a buyer appears at the price the firm sets, which is to say only to a firm that does not need the public market. The availability condition is the reason the mechanism is not a general solution.

The mechanism confers a further control benefit that is easily overlooked. The firm controls the transfer, and the transfer restrictions customary in private-company charters permit the firm to determine who may acquire the shares. The right of first refusal and the transfer-approval provisions admit the compact characterization as an admissible-buyer set

$$\mathcal{B}^{\text{admissible}} \subsetneq \mathcal{B}^{\text{willing}}$$

with the firm selecting the buyers from the willing set. The selection permits the firm to exclude parties whose accumulation of the shares would be strategically unwelcome, which is an instrument that no public company possesses.

## The Deferred Initial-Public-Offering Decision

The decision not to list has been sustained across the entire history of the firm and across repeated public statements that a listing of the parent company is not contemplated. The decision is the single most consequential governance decision the firm has made, and it is substantially overdetermined.

The legal precondition deserves statement before the economic determinants, because a firm does not remain private merely by declining to list. An issuer becomes a reporting company by operation of the [Exchange Act registration threshold][ref_exchange_act_12g] once its total assets and its holder-of-record count exceed statutory levels, and the threshold is implemented in the [Rule 12g-1][ref_rule_12g1] provisions. The threshold was raised substantially by the [Jumpstart Our Business Startups Act of 2012][ref_jobs_act_2012], which also excluded holders who received their securities under employee compensation plans from the count. The statutory change is the single legal development most responsible for the viability of the configuration this article describes, because it permitted a firm to accumulate a large employee and investor base without triggering the reporting obligation. The configuration is therefore not a timeless option available to any founder. It is an artifact of a statutory settlement dating to the 2012 period.

The first determinant is the one the private-markets tradition identifies. The expansion of the private capital supply that [Ewens and Farre-Mensa 2020][research_ewens_farre_mensa_2020] document has made the capital available privately, which removes the principal historical reason to list. The listing decision has the form

$$\text{list} \iff \left[ K^{\text{required}} > K^{\text{private available}} \right] \; \vee \; \left[ L^{\text{required}} > L^{\text{tender}} \right]$$

with the listing warranted only when the capital requirement exceeds the private supply or the liquidity requirement exceeds what the tender mechanism offers. Neither condition has bound. The cost the deferral imposes is an illiquidity discount in the price at which the private capital is supplied, admitting the compact form

$$r^{\text{private}} = r^{\text{public}} + \pi^{\text{illiquidity}} + \pi^{\text{opacity}}$$

with the two premia compensating the investor for the absence of a liquid market and for the absence of the disclosure. The deferral is rational for the controller whenever the governance value of the retained control exceeds the capitalized value of the two premia, and the magnitude of the premia has fallen across the period as the private secondary market has deepened.

The second determinant is the governance obligation a listing imposes. The obligations comprise the periodic disclosure and the internal-control attestation that the [Sarbanes-Oxley Act of 2002][ref_sarbanes_oxley_2002] imposes, the quarterly earnings cycle, the proxy access through which shareholders present proposals under [Rule 14a-8][ref_rule_14a8], the say-on-pay advisory vote that the [Dodd-Frank Act of 2010][ref_dodd_frank_2010] introduced, the beneficial-ownership disclosure on [Schedule 13D][ref_schedule_13d] that makes an accumulating position visible, the listing standards that the [NYSE Listed Company Manual][ref_nyse_listed_company_manual] and the [Nasdaq listing rules][ref_nasdaq_listing_rules] impose, the market for corporate control that [Manne 1965][research_manne_1965] Mergers and the Market for Corporate Control describes, and the exposure to activist campaigns. The obligations are individually survivable under a dual-class structure and jointly constitute an ongoing constraint that an unlisted firm does not face.

The third determinant is to the mission-directed case. The disclosure obligation would require the firm to publish the cost and schedule performance of a development program whose difficulties are severe and whose timeline is long. The publication would supply the raw material for a narrative of failure at each intermediate setback, and the narrative would in turn affect the cost of capital and the customer relationships. The effect takes the compact statement

$$\text{Var}\!\left[ V^{\text{market}} \mid \text{disclosed} \right] \gg \text{Var}\!\left[ V^{\text{market}} \mid \text{undisclosed} \right]$$

with the disclosed valuation substantially more volatile across the development period. The volatility is not merely uncomfortable. It feeds back into the ability to raise the subsequent capital and into the retention of the personnel whose compensation is denominated in the equity.

The counterargument the governance literature provides is that the disclosure and the market discipline are precisely the mechanisms that prevent a controller from persisting in a mistaken course, and that a firm which exempts itself from them retains no external correction. The counterargument is correct as stated. The question the case poses is whether the external correction would have distinguished a mistaken course from a difficult but correct one, and the Space Shuttle and Constellation records that the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats supply reasons for doubt about the discriminating power of external oversight applied to long-horizon development programs.

## The Starlink Separation Question

The question whether the Starlink business will be separated and listed independently has been raised repeatedly across the period since the 2019 deployment began and remains unresolved at the drafting date. The question is governance-critical because a separation would create the first public-market claim on the SpaceX capability base.

The case for separation rests on the valuation argument that a subscription-revenue business is valued on different multiples than a launch-service business, and on the capital argument that a listed Starlink could raise capital against its own cash flows. The case against separation rests on the integration argument that the [Value Capture article A284][related_post_a284_spacex_value_capture] develops, under which the value is created precisely by the joint operation of the launch and constellation businesses, and on the governance argument the present article develops.

The governance argument can be stated compactly. A separation transfers the financing loop that the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] formalizes from an internal transfer to an external one. Under the integrated configuration the Starlink surplus funds the Starship development by an internal capital allocation that the controller directs. Under the separated configuration the transfer would require a dividend, an intercompany agreement, or a related-party transaction, each of which is subject to a fiduciary review that the internal allocation is not. The difference may be written

$$\text{cost of transfer} = \begin{cases} \approx 0 & \text{integrated} \\ C^{\text{fiduciary}} + C^{\text{minority}} & \text{separated} \end{cases}$$

with the separated configuration incurring a review cost and a minority-protection cost on every transfer. The separation decision therefore turns on a comparison between a sum-of-parts valuation and an integrated valuation net of the transfer frictions, admitting the compact form

$$\Delta = \left[ V^{\text{Starlink standalone}} + V^{\text{SpaceX ex-Starlink}} \right] - \left[ V^{\text{integrated}} + \Pi^{\text{control}} \right]$$

with $\Pi^{\text{control}}$ the value the controller assigns to the unimpeded internal capital allocation. The separation is undertaken when $\Delta > 0$, and the inclusion of the control term is what distinguishes the decision facing this firm from the ordinary conglomerate-discount calculation. The costs are not prohibitive and they are not zero, and a controller whose principal use of the subsidiary's cash flow is to fund a parent-level mission has an interest in avoiding them.

## The OpenAI Counter-Example

The OpenAI governance structure from the December 2015 founding through the November 2023 board crisis and the subsequent restructuring constitutes the canonical governance negation case in the contemporary technology sector. The case is analytically valuable precisely because the structure was designed explicitly and self-consciously to resist capital capture, and because it failed. The record is documented in the [OpenAI charter][ref_openai_charter] and the [OpenAI announcements][ref_openai_news], supplemented by the contemporaneous reporting in [The New York Times][ref_nyt], [Bloomberg][ref_bloomberg], the [Wall Street Journal][ref_wsj], and [The Washington Post][ref_washington_post].

The structure comprised a nonprofit entity founded in the December 2015 period whose board held the ultimate control authority, and beneath it a capped-profit subsidiary created in the March 2019 period whose investors received returns limited by a multiple of the invested capital. The arrangement placed the control authority in the hands of a board explicitly constituted so that a majority of its members held no equity in the enterprise. The design intent was that the board would be able to act against the financial interest of the investors where the charter mission required it.

The formal control measure for the arrangement was maximal. In the notation the economic-property section establishes, the nonprofit board held

$$v^{\text{board}} = 1 \qquad \text{with} \qquad e^{\text{board}} = 0 \qquad \text{so} \qquad w^{\text{board}} = \frac{v}{e} \to \infty$$

with the wedge unbounded. The SpaceX wedge of approximately 1.9 is modest by comparison. If the formal wedge were the operative quantity, the OpenAI structure would have been the most capture-resistant arrangement in the sector.

The November 2023 events established that the formal wedge is not the operative quantity. The board removed the chief executive on the November 17 2023 date. Within the following days substantially the entire employee body signed a letter indicating an intention to depart for the principal investor, the principal investor made clear that it would receive them, and the board reversed itself. The chief executive was reinstated on approximately the November 21 2023 date and the board was reconstituted. The elapsed interval was approximately five days.

The analytical content of the episode is the distinction between formal and effective control that the economic-property section formalizes. The effective control satisfied

$$v^{\text{effective}}_{\text{board}} \approx 0 \qquad \text{despite} \qquad v^{\text{formal}}_{\text{board}} = 1$$

because the organization's productive capacity resided in personnel who could depart, and the personnel's economic interest was aligned with the investor rather than with the board. The resource-dependence term in the effective-control expression dominated the formal term entirely. The board possessed the authority to remove the chief executive and did not possess the capacity to operate the organization afterward, and a control that cannot survive its own exercise is not a control.

The structural conditions that produced the outcome admit compact statement. Let $\theta$ denote the fraction of the organization's productive value embodied in mobile human capital, and let $\alpha$ denote the fraction of the personnel's compensation contingent on the equity value. The board's effective authority declines in both, and the condition under which a formally controlling body can in fact prevail is

$$\theta \cdot \alpha < \bar{\tau}$$

for a threshold $\bar{\tau}$ determined by the switching costs the personnel would face. A research organization whose value is substantially its researchers and whose researchers hold substantial equity-linked claims sits far above the threshold. The condition is not a defect of the particular board or the particular individuals, and a differently composed board facing the identical conditions would have faced the identical outcome. The coordination structure that produced the rapid reversal has the concise statement as a threshold model in which each individual departs once a sufficient fraction of colleagues has committed to depart

$$\text{depart}_i \iff f^{\text{committed}} \geq \theta_i$$

with $\theta_i$ the individual threshold and the cascade completing whenever the distribution of the thresholds admits no stable interior equilibrium. The published letter served the function of making the committed fraction common knowledge, which is the mechanism by which a latent majority becomes a realized one.

The subsequent trajectory has moved the structure toward conventional arrangements. The restructuring toward a public benefit corporation and the reported removal of the return cap in the 2025 period complete the convergence. The capped-profit instrument was itself a transitional device whose removal was predictable from the moment the capital requirement exceeded what capped-return investors would supply. The removal admits the compact statement that a return cap $\bar{R}$ binds only while

$$\bar{R} > R^{\text{market}}\!\left( \text{risk} \right)$$

and ceases to be acceptable to incoming investors once the required market return on the risk exceeds the cap. A cap set generously enough never to bind imposes no discipline, and a cap set tightly enough to discipline eventually blocks the financing. The instrument therefore has no stable configuration under a capital requirement that grows.

The comparison with the SpaceX configuration is direct and instructive. The SpaceX controller holds a formal wedge that is modest relative to the OpenAI board's, and holds in addition a position in the resource-dependence structure that the OpenAI board lacked entirely. The controller is not merely the holder of the votes. The controller is also the person whose departure the personnel and the investors would regard as the principal risk to the enterprise, which places the resource-dependence term on the same side as the formal term rather than against it. The governance condition is therefore not satisfied by the voting arithmetic alone, and the arithmetic is the visible part of an arrangement whose operative part is the alignment between the formal authority and the effective authority.

## The Tesla Comparison and the Limits of Public-Company Founder Control

The Tesla case offers the complementary negation, in which the same individual operating under public-company conditions without a dual-class structure encountered constraints that the SpaceX configuration does not impose. The case is directly comparative because the controller, the management style, and the approximate period are held constant while the governance configuration varies.

The Tesla equity position is reported at approximately 13 percent following share dispositions across the 2021 through 2022 period, with the ordinary one-share-one-vote configuration and therefore

$$w^{\text{Tesla}} = \frac{v}{e} \approx 1 \qquad \text{against} \qquad w^{\text{SpaceX}} \approx 1.9$$

and a control condition that fails rather than holds. The consequence is that the Tesla controller governs by a combination of board relationships, retail-shareholder support, and personal prominence rather than by a voting majority.

The 2018 chief-executive performance award and the ensuing litigation illustrate the difference concretely. The Delaware Court of Chancery in the Tornetta matter rescinded the award in the January 2024 decision on the ground that the approval process had been controlled rather than independent, and the court declined to reverse itself following the shareholder ratification vote of the mid 2024 period. The record is accessible through the [Delaware Court of Chancery][ref_delaware_chancery] and the [Delaware courts opinions archive][ref_delaware_opinions], and the corresponding corporate disclosures appear in the [Tesla investor materials][ref_tesla_ir]. The subsequent shareholder approval of a reincorporation from the state of Delaware to the state of Texas under the [Texas Business Organizations Code][ref_texas_boc] constitutes a forum response to a substantive constraint.

The analytical lesson is that the fiduciary apparatus binds a controller who lacks a voting majority substantially more tightly than one who holds it, because the controlled-transaction doctrines apply the entire-fairness standard to a transaction in which the controller stands on both sides and the standard is applied by a court rather than by a vote. The standard-selection rule that produces the difference can be stated as

$$\text{standard} = \begin{cases} \text{business judgment} & \text{if no controller stands on both sides} \\ \text{entire fairness} & \text{otherwise, absent cleansing} \end{cases}$$

with the second branch shifting the burden to the defendant and subjecting the transaction to a substantive review rather than to a deferential one. The cleansing procedures require an independent committee and an informed majority-of-the-minority vote, and the finding that the process was controlled rather than independent is what removed the cleansing in the matter.

The control a founder exercises without a voting majority is therefore a substitute rather than an equivalent, admitting the compact form

$$v^{\text{effective}} = \beta_1 v^{\text{formal}} + \beta_2 \, s^{\text{board relationships}} + \beta_3 \, s^{\text{retail support}} + \beta_4 \, d^{\text{indispensability}}$$

with the latter three terms substantially more contestable and more perishable than the first. The public statements in which the individual expressed a preference for a greater voting share at Tesla before committing further artificial-intelligence and robotics work to it constitute a direct statement of the governance condition this article treats, applied by the person to whom it applies.

The comparison establishes that the SpaceX configuration is not simply an expression of an individual preference for control. The same individual accepted a substantially weaker control position at a different firm whose capital was raised in the public market, which indicates that the control configuration tracks the financing channel rather than tracking the person.

## Foundation-Ownership Precedents

The foundation-ownership arrangements of the German and Danish industrial tradition constitute the longest-running experiments in a control configuration insulated from the capital market. The arrangements are the positive precedents for the governance condition, and they are the only available evidence on the question of whether a capture-resistant configuration can persist beyond the lifetime of the founder.

The Carl Zeiss Stiftung established in the 1889 period by the physicist Ernst Abbe, with the governing statute completed in the 1896 period, is the earliest of the arrangements. The founder transferred the ownership of the optical works to a foundation whose statute defined the purposes and constrained the successors, and the foundation remains the owner of the Carl Zeiss and Schott enterprises at the drafting date. The record is accessible through the [Carl Zeiss Stiftung][ref_carl_zeiss_stiftung] documentation and the [Carl Zeiss corporate][ref_zeiss_corporate] materials, and the German legal form within which the arrangement operates is governed by the [Aktiengesetz][ref_german_aktiengesetz] provisions on share classes and corporate organs. The statute is analytically remarkable because it constrained the foundation itself rather than merely establishing it, prohibiting family control, fixing labor conditions including a limited working day and a pension provision, and specifying that no individual could derive a personal claim from the enterprise. The instrument is therefore a commitment device operating against the founder's own successors as much as against the external capital market. The statutory constraint permits the concise form

$$\mathcal{A}^{\text{permitted}} = \mathcal{A} \setminus \mathcal{A}^{\text{prohibited by statute}}$$

with the foundation's action set restricted by the founding instrument rather than merely directed by it. The distinction between a restriction and a direction is the whole of the difference between a commitment device and a statement of intent, because a direction can be reinterpreted by a successor and a restriction must be amended.

The Robert Bosch arrangement gives the cleanest available separation of the two rights. The configuration established following the founder's death in the 1942 period and implemented in the 1964 period places approximately 94 percent of the share capital with the charitable foundation and approximately 0.01 percent of the voting rights, while an industrial trust holds approximately 93 percent of the voting rights against approximately 0.01 percent of the capital. The record is accessible through the [Robert Bosch Stiftung][ref_bosch_stiftung] documentation, the [Bosch corporate][ref_bosch_company] materials, and the [Bosch annual reporting][ref_bosch_annual_report] that discloses the ownership split. The wedges are

$$w^{\text{foundation}} = \frac{0.0001}{0.94} \approx 0.0001 \qquad \text{and} \qquad w^{\text{trust}} = \frac{0.93}{0.0001} \approx 9300$$

with the separation approaching the theoretical limit in both directions. The arrangement demonstrates that the wedge permits values orders of magnitude beyond anything a dual-class listed company exhibits, and that a configuration at that extreme has operated a major industrial enterprise across approximately six decades without the expropriation the agency tradition predicts.

The Novo Nordisk arrangement places the Novo Nordisk Foundation, through the Novo Holdings entity, in control of the operating company by means of a two-class share structure in which the superior class carries a tenfold voting right. The reported position is approximately 28 percent of the capital and approximately 77 percent of the votes, corresponding to

$$w^{\text{Novo}} = \frac{0.77}{0.28} \approx 2.8$$

which is the closest of the three precedents to the SpaceX configuration in magnitude. The record is accessible through the [Novo Nordisk Foundation][ref_novo_nordisk_foundation] documentation, the [Novo Holdings][ref_novo_holdings] materials, and the [Novo Nordisk investor disclosures][ref_novo_nordisk_investors] that report the class structure. The Danish corporate and foundation registry framework is administered through the [Danish Business Authority][ref_danish_business_authority]. The arrangement is distinguished from the SpaceX case by the fact that the operating company is publicly listed, so that the configuration combines the capture resistance with the public-market disclosure and liquidity that the SpaceX arrangement forgoes.

The comparative significance of the three precedents rests on the survival evidence they supply. The arrangements have persisted across approximately 137 years, approximately 84 years, and approximately 76 years respectively at the drafting date, spanning wars, currency collapses, generational transitions, and complete turnovers of the operating businesses. The survival function takes the form

$$S(t) = P\!\left( \text{configuration intact at } t \mid \text{established at } 0 \right)$$

with the foundation-owned population exhibiting a substantially flatter hazard than the founder-controlled population, for the structural reason that a foundation does not die and a founder does. The observation identifies the principal unresolved question about the SpaceX configuration, because the instrument the firm employs is tied to an individual and the precedents that demonstrate centurial persistence are not.

The three cases are the best documented instances of a broader class. The class includes specific Nordic sphere-holding arrangements in which a family foundation controls a holding company that in turn controls a portfolio of listed operating companies, German family-foundation arrangements beyond the two treated here, and arrangements in other jurisdictions in which a trust or a charitable entity holds the controlling block of a major enterprise. The common structural feature is the separation of the entity that holds the economic interest from the entity that exercises the control, and the common consequence is that no natural person can capture the enterprise by acquiring the shares. The arrangements are concentrated in jurisdictions whose foundation law permits them, which is a further instance of the legal-origins point the law-and-finance framing makes.

The literature on the arrangements is thinner than their significance warrants, and [Hansmann 1996][book_hansmann_1996] The Ownership of Enterprise remains the principal theoretical treatment of the class of firms in which the residual claimant is absent or attenuated. The empirical finding the literature reports is that the foundation-owned firms exhibit lower profitability variance, longer investment horizons, and comparable or slightly lower returns than comparable investor-owned firms, which is the profile the mission-directed configuration would predict.

## The Sunset-Provision and Successor Question

The sub-property the cross-sectional analysis identifies as unsatisfied deserves treatment on its own terms, because it is the respect in which the configuration differs from every arrangement that has demonstrated centurial persistence.

The policy literature that [Bebchuk and Kastiel 2017][research_bebchuk_kastiel_2017] represents proposes the sunset provision as the remedy for the perpetual dual-class structure. A sunset converts the superior class to an ordinary class upon a triggering event, which may be the passage of a fixed interval, the death or incapacity of the founder, the transfer of the shares outside a permitted class of holders, or the decline of the founder's economic stake below a threshold. The instrument yields the compact statement as a stopping time

$$\lambda^{\text{effective}}(t) = \lambda \cdot \mathbb{1}\!\left[ t < T^{\text{sunset}} \right] + 1 \cdot \mathbb{1}\!\left[ t \geq T^{\text{sunset}} \right]$$

with the voting ratio collapsing to unity at the trigger. The policy argument for the instrument rests on the empirical finding that the value discount associated with the wedge steepens with the tenure, which implies that the benefits of the founder control are front-loaded and the costs are back-loaded.

The argument has a weakness in the mission-directed case that the policy literature does not address. A mission whose completion horizon exceeds the sunset interval is not protected by a configuration that terminates before the mission does. The condition for a sunset to be compatible with the mission is

$$T^{\text{sunset}} > T^{\text{mission}}$$

and a Mars-transportation objective of the kind the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats has a horizon that no conventional sunset interval approaches. The policy instrument and the mission-directed configuration are therefore in direct tension, and the tension is not resolvable by adjusting the interval, because an interval long enough to protect the mission is long enough to reproduce substantially the perpetual structure the instrument was designed to prevent.

The foundation instrument resolves the tension by a different route. A foundation does not sunset because it does not die, and the commitment it embodies binds the successors rather than expiring for their benefit. The difference between a sunset and a foundation is therefore not a difference of degree along a single dimension. The sunset assumes that the founder control is a transitional necessity to be unwound, and the foundation assumes that it is a permanent arrangement to be institutionalized. The two instruments answer different questions.

The succession record across the comparison set supports a compact empirical generalization. An arrangement resting on an individual's holdings terminates at a transition unless an instrument transfers it, and the instruments available comprise the trust, the foundation, the family holding company, and the voting agreement. Each of the instruments has been used at scale, each is documented in the precedents this article treats, and none is present in the SpaceX configuration at the drafting date so far as the public record discloses. The absence may reflect a deliberate choice, a matter not yet reached, or an arrangement that exists and is not public. The article cannot distinguish among the three.

The analytical significance of the open question is that it determines which of the two readings of the case is correct. Under the first reading the configuration is a durable institutional innovation of the kind the foundation precedents represent. Under the second reading it is a personal arrangement that will terminate with the person, and the mission it protects will then face the capital market on ordinary terms at whatever stage of completion it has reached. The evidence available at the drafting date does not discriminate, and the article declines to guess.

## Deep Historical Comparative Precedents

The governance mechanic allows comparison with deep historical precedents that establish the property as a recurring feature of enterprises pursuing objectives beyond the horizon of their capital providers.

The chartered-company form of the early modern period constitutes the origin of the problem. The English and Dutch East India Companies separated the ownership from the control at a scale and across a distance that made the agency problem acute, and the governance instruments the companies developed comprise the earliest systematic attempts at its solution. The treatments in [Steensgaard 1974][book_steensgaard_1974] The Asian Trade Revolution of the Seventeenth Century, [Stern 2011][book_stern_2011] The Company-State, and [Robins 2006][book_robins_2006] The Corporation That Changed the World document the arrangements. The relevance to the present case is that the chartered form was created precisely to permit an enterprise requiring capital beyond any individual's means to pursue an objective across a horizon longer than any individual investment, which is the problem the governance condition restates.

The Standard Oil trust and the subsequent holding-company form illustrate the instrument by which a controller retains a unified direction across a dispersed ownership. The treatment in [Chernow 2004][book_chernow_2004] Titan documents the arrangement, and the antitrust response is treated in [Bork 1978][book_bork_1978] The Antitrust Paradox, [Posner 2001][book_posner_2001] Antitrust Law, and [Hovenkamp 2005][book_hovenkamp_2005] The Antitrust Enterprise. The case establishes that the control instruments the article treats have a long history of attracting regulatory attention when the enterprises they govern attain market positions, which is a hazard the SpaceX configuration will encounter as the constellation-deployment position consolidates.

The Ford Motor Company supplies the longest-running dual-class arrangement in the American industrial record. The Class B shares held by the founding family confer approximately 40 percent of the voting power against an equity position of a few percent, corresponding to

$$w^{\text{Ford}} = \frac{v}{e} \approx \frac{0.40}{0.02} \approx 20$$

which is approximately an order of magnitude above the SpaceX figure and which illustrates that the wedge magnitude alone carries no information about the quality of the resulting stewardship. The treatments in [Ford and Crowther 1922][book_ford_crowther_1922] My Life and Work, [Nevins 1954][book_nevins_1954] Ford, and [Hounshell 1984][book_hounshell_1984] From the American System to Mass Production document the origins. The case is instructive in both directions. The arrangement preserved a family direction across approximately a century, and the same arrangement has been identified in the governance literature as a contributor to periods of underperformance in which an external correction was unavailable.

The Bell System supplies the case of an enterprise whose long-horizon research programme was financed by a regulated monopoly rent rather than by a control instrument. The treatments in [Gertner 2012][book_gertner_2012] The Idea Factory, [Temin and Galambos 1987][book_temin_galambos_1987] The Fall of the Bell System, [Wu 2010][book_wu_2010] The Master Switch, and [Levin 2010][book_levin_2010] The Wires That Bind document the arrangement and its dissolution. The case establishes that the mission-protection function the governance condition performs can be discharged by a regulatory arrangement rather than by an ownership arrangement, and that the regulatory route terminates whenever the regulatory settlement changes.

The Berkshire Hathaway arrangement yields a contemporary instance of a dual-class structure adopted explicitly to preserve an investment philosophy against a market pressure toward a shorter horizon, documented in [Schroeder 2008][book_schroeder_2008] The Snowball. The case is analytically close to the SpaceX case in its stated rationale and distant in its business substance.

The technology-sector dual-class wave from the 2004 period forward established the arrangement as a sector norm. The treatments in [Isaacson 2011][book_isaacson_2011] Steve Jobs, [Stone 2013][book_stone_2013] The Everything Store, [Thiel 2014][book_thiel_2014] Zero to One, [Malone 2014][book_malone_2014] The Intel Trinity, and [Saxenian 1994][book_saxenian_1994] Regional Advantage document the sector context. The significance of the wave for the present article is that it substantially normalized the instrument, so that the SpaceX configuration required no unusual persuasion of the investor base at the moment it was established.

The Xerox case gives the canonical instance of a governance failure in the opposite direction from the cases treated above. The corporation possessed a research capability of extraordinary depth and a conventional governance structure, and the structure proved unable to direct the capability toward any commercial purpose the corporation could capture. The treatments in [Hiltzik 1999][book_hiltzik_1999] Dealers of Lightning, [Smith and Alexander 1988][book_smith_alexander_1988] Fumbling the Future, and [Kearns and Nadler 1992][book_kearns_nadler_1992] Prophets in the Dark document the episode, and the [Value Capture article A284][related_post_a284_spacex_value_capture] treats it as the value-capture negation case. The governance reading is that a dispersed-ownership corporation with a professional management and a quarterly reporting obligation could not sustain a commitment to a capability whose commercial application lay outside its existing business. The case establishes that the hazard the governance condition addresses is not exclusively the hazard of a hostile investor. It includes the hazard of a management structure with no party holding a durable commitment to anything in particular.

The IBM System/360 decision of the 1964 period contributes the counterpart instance in which a large corporation did sustain a bet-the-company commitment. The treatments in [Pugh Johnson and Palmer 1991][book_pugh_johnson_palmer_1991] IBM's 360 and Early 370 Systems and [Pugh 1995][book_pugh_1995] Building IBM document the decision, and the [IBM archives][ref_ibm_archives] hold the institutional record. The governance-relevant feature is that the decision was taken under a founding-family leadership whose position, while not resting on a formal dual-class instrument, supplied an analogous durability of commitment. The case is the closest historical analogue to the 2017 architectural decision the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats.

The RCA trajectory under a long-tenured founding executive, documented in [Bilby 1986][book_bilby_1986] The General, supplies a further instance of a durable personal commitment sustaining a long-horizon technical programme, and it yields equally the cautionary sequel in which the commitment outlived its usefulness and the enterprise had no mechanism to correct it.

The Iridium case contributes the instance in which a governance structure permitted a single irreversible bet at a scale the market would not support, documented in [Finkelstein and Sanford 2000][research_finkelstein_sanford_2000] Learning from Corporate Mistakes. The case is treated in the [Value Gradient article A282][related_post_a282_spacex_value_gradient] and the [Decomposability article A285][related_post_a285_spacex_decomposability] as the single-bet contrast, and its governance dimension is that no party in the structure held both the information and the incentive to halt the programme.

The research-university and national-laboratory forms supply the institutional precedent for a long-horizon research enterprise governed without a residual claimant at all. The treatments in [Selznick 1949][book_selznick_1949] TVA and the Grass Roots, [Hargrove 1994][book_hargrove_1994] Prisoners of Myth, [Norberg and O'Neill 1996][book_norberg_oneill_1996] Transforming Computer Technology, and [Bonvillian 2018][research_bonvillian_2018] on the DARPA institutional configuration document the arrangements. The goal-displacement failure mode that [Selznick 1949][book_selznick_1949] names is the canonical statement of what the governance condition seeks to prevent, and the fact that it was named in a study of a public agency rather than of a firm establishes that the hazard is not to the capital market.

The precedent set supports summary through a comparison of the hazard rates governing the loss of the configuration. Let $h_c(t)$ denote the instantaneous hazard for the class $c$. The ordering the record supports is

$$h^{\text{foundation}} < h^{\text{family dual class}} < h^{\text{founder dual class}} < h^{\text{regulated monopoly}}$$

with the foundation arrangements exhibiting the flattest hazard because the controlling entity does not die, and the regulated-monopoly arrangement exhibiting the steepest because the configuration depends on a political settlement that any administration can revisit. The SpaceX configuration sits in the third position, and the distance between the third and the first is the successor problem.

## Historiographical Gap and Recent Scholarship

The scholarly literature on the SpaceX governance configuration is substantially thinner than the literature on any other condition in the seven-plus-three framework, and the thinness has a structural cause rather than an accidental one. The corporate-governance literature is overwhelmingly an empirical literature built on public-company disclosure, and a firm that has never listed supplies substantially none of the data the literature's methods require.

### Primary Source Documentation

The primary source documentation comprises the [Delaware General Corporation Law][ref_dgcl] provisions authorizing the instruments, the [Texas Business Organizations Code][ref_texas_boc] provisions relevant to the reported reincorporation, the [Delaware Court of Chancery][ref_delaware_chancery] record including the compensation litigation the Tesla comparison treats, the [Securities and Exchange Commission EDGAR][ref_sec_edgar] system, the [Form D][ref_sec_form_d] exempt-offering notices through which the private rounds reach the public record, the [SpaceX news archive][ref_spacex_news_archive], and the [OpenAI charter][ref_openai_charter] and [OpenAI announcements][ref_openai_news] for the counter-example. The foundation precedents are documented through the [Carl Zeiss Stiftung][ref_carl_zeiss_stiftung], [Robert Bosch Stiftung][ref_bosch_stiftung], [Bosch corporate][ref_bosch_company], [Novo Nordisk Foundation][ref_novo_nordisk_foundation], and [Novo Holdings][ref_novo_holdings] records. The institutional-investor policy positions on the dual-class question are documented through the [Council of Institutional Investors][ref_cii].

### Scholarly Infrastructure and Working-Paper Record

A feature of the corporate-governance field is that a substantial portion of the active literature circulates as working papers well before journal publication, so that a survey confined to published articles lags the field by an interval of years. The principal repositories are the [European Corporate Governance Institute][ref_ecgi] working-paper series, the [National Bureau of Economic Research][ref_nber] series, and the [Social Science Research Network][ref_ssrn]. The practitioner-facing commentary that tracks doctrinal developments appears in the [Harvard Law School Forum on Corporate Governance][ref_harvard_corpgov_forum] and the [Columbia Blue Sky Blog][ref_columbia_blue_sky]. The article draws on the published literature for its claims and notes the repositories because a reader wishing to extend the survey beyond the drafting date will find the frontier there rather than in the journals.

### Theoretical Corporate-Governance Literature

The theoretical literature is mature and is surveyed above in the Cross-Disciplinary Framings section. The principal works are [Berle and Means 1932][book_berle_means_1932], [Jensen and Meckling 1976][research_jensen_meckling_1976], [Fama and Jensen 1983][research_fama_jensen_1983], [Grossman and Hart 1986][research_grossman_hart_1986], [Grossman and Hart 1988][research_grossman_hart_1988], [Harris and Raviv 1988][research_harris_raviv_1988], [Hart and Moore 1990][research_hart_moore_1990], [Hart 1995][book_hart_1995], [Shleifer and Vishny 1997][research_shleifer_vishny_1997], [Tirole 2006][book_tirole_2006] The Theory of Corporate Finance, and the legal-economic treatments in [Easterbrook and Fischel 1991][book_easterbrook_fischel_1991] and [Roe 1994][book_roe_1994]. The gap the literature exhibits with respect to the present case is that substantially the entire theoretical apparatus takes the maximization of the security value as the normative objective, and the mission-directed case posits an objective that the apparatus can represent only as a private benefit of control.

### Empirical Dual-Class Literature

The empirical literature comprises [DeAngelo and DeAngelo 1985][research_deangelo_deangelo_1985], [Gompers Ishii and Metrick 2003][research_gompers_ishii_metrick_2003], [Gompers Ishii and Metrick 2010][research_gompers_ishii_metrick_2010], [Bebchuk Kraakman and Triantis 2000][research_bebchuk_kraakman_triantis_2000], and the policy argument in [Bebchuk and Kastiel 2017][research_bebchuk_kastiel_2017]. The literature's central estimate is that the firm value declines in the wedge and that the decline steepens with the time since listing. The applicability of the estimates to an unlisted firm is unresolved, and the direction of the selection bias is not obvious. A sample of firms that listed with a dual-class structure excludes by construction the firms whose controllers valued control sufficiently to forgo listing entirely, which is the population the SpaceX case belongs to.

### Entrepreneurial-Finance and Private-Markets Literature

The entrepreneurial-finance literature comprising [Sahlman 1990][research_sahlman_1990], [Gompers 1995][research_gompers_1995], [Lerner 1994][research_lerner_1994_syndication], [Kaplan and Stromberg 2003][research_kaplan_stromberg_2003], [Kaplan and Stromberg 2004][research_kaplan_stromberg_2004], [Gompers and Lerner 2001][book_gompers_lerner_2001], [Metrick and Yasuda 2011][book_metrick_yasuda_2011], and [Lerner 2009][book_lerner_2009] Boulevard of Broken Dreams supplies the contracting apparatus. The private-markets literature that [Ewens and Farre-Mensa 2020][research_ewens_farre_mensa_2020] represents provides the listing-choice apparatus, and the venture-capital effects literature in [Kortum and Lerner 2000][research_kortum_lerner_2000] and [Hall and Lerner 2010][research_hall_lerner_2010] supplies the sector-level context. The contemporary defense-technology venture wave that the Patient-Private Capital-Formation Leg article A290 will treat has generated an emerging literature that remains substantially in the trade and practitioner registers.

### Foundation-Ownership and Alternative-Form Literature

The literature on the foundation-owned firm is small, and [Hansmann 1996][book_hansmann_1996] The Ownership of Enterprise remains the principal theoretical treatment of the broader class of firms with attenuated residual claims. The empirical literature on the Danish and German industrial foundations is substantially European and substantially recent. The gap is notable because the arrangements supply the only long-run evidence bearing on the central question the present article poses.

### Comparative and Non-United-States Literature

The comparative literature is substantial and is systematically underused in the United States governance debate. The developmental-state tradition comprising [Johnson 1982][book_johnson_1982] MITI and the Japanese Miracle, [Amsden 1989][book_amsden_1989] Asia's Next Giant, [Wade 1990][book_wade_1990] Governing the Market, [Evans 1995][book_evans_1995] Embedded Autonomy, [Woo-Cumings 1999][book_woo_cumings_1999] The Developmental State, and [Chang 2002][book_chang_2002] Kicking Away the Ladder documents the arrangements under which other states have sustained long-horizon industrial programmes, and the contemporary extensions appear in [Block 2008][research_block_2008] and [Weiss and Thurbon 2021][research_weiss_thurbon_2021]. The European corporate-law materials comprising the [United Kingdom Companies Act 2006][ref_uk_companies_act_2006], the [German Aktiengesetz][ref_german_aktiengesetz], and the [European Union Shareholder Rights Directive][ref_eu_shareholder_rights_directive] establish that the instrument this article treats is substantially a United States artifact, and the [OECD Principles of Corporate Governance][ref_oecd_corporate_governance] supply the comparative benchmark. The institutional-economics frame in [North 1990][book_north_1990], [Ostrom 1990][book_ostrom_1990], [Greif 2006][book_grief_2006], and [Acemoglu and Robinson 2012][book_acemoglu_robinson_2012] situates the national variation within the broader question of institutional selection.

### Methodological Literature on Case-Study and Counterfactual Inference

The methodological problem is more severe here than elsewhere in the series, because the central claim concerns an event that did not occur. The case-study methodology literature comprising [Yin 2014][book_yin_2014] Case Study Research and Applications and [Creswell 2014][book_creswell_2014] Research Design supplies the standards. The standard the article attempts to meet is the explicit statement of the rival explanations together with the identification of observations that would discriminate among them, and the article reports that no such observation is available for its central claim. The paradigm literature in [Kuhn 1962][book_kuhn_1962] and the evolutionary treatments in [Nelson and Winter 1982][book_nelson_winter_1982] and [Metcalfe 1998][book_metcalfe_1998] supply the selection caution, and the complexity and failure treatments in [Kauffman 1993][book_kauffman_1993], [Ormerod 2005][book_ormerod_2005] Why Most Things Fail, and [Beinhocker 2006][book_beinhocker_2006] The Origin of Wealth supply the base-rate framing within which a single surviving configuration should be interpreted.

### Adjacent Literature on Mission-Directed and Public-Purpose Organizations

The literature on organizations constituted to pursue a purpose other than a financial return bears directly on the question and is largely disjoint from the corporate-governance literature. The public-private-partnership treatments in [Grimsey and Lewis 2004][book_grimsey_lewis_2004], [Osborne 2000][book_osborne_2000], [Yescombe 2007][book_yescombe_2007], [Hodge and Greve 2007][research_hodge_greve_2007], [Bovaird 2004][research_bovaird_2004] treat the hybrid forms. The public-agency treatments in [Selznick 1949][book_selznick_1949], [Hargrove 1994][book_hargrove_1994], [Handberg 1994][book_handberg_1994] Reinventing NASA, and [McCurdy 1994][book_mccurdy_1994] Inside NASA treat the goal-displacement hazard in organizations with no residual claimant at all. The finding that the hazard appears in substantially every organizational form is the reason the article treats the governance condition as a general problem rather than as an artifact of the capital market.

### Critical and Skeptical Literature

A critical literature treats the control configurations the article describes as an entrenchment of an unaccountable elite rather than as a protection of a mission. The position is stated most directly in [Bebchuk and Kastiel 2017][research_bebchuk_kastiel_2017] within the governance literature, and in the broader political-economy register in [Melman 1970][book_melman_1970] Pentagon Capitalism, [Foster and McChesney 2011][book_foster_mcchesney_2011] The Endless Crisis, [Srnicek 2017][book_srnicek_2017] Platform Capitalism, [Zuboff 2019][book_zuboff_2019] The Age of Surveillance Capitalism, and [Khan 2017][research_khan_2017] Amazon's Antitrust Paradox. The concern the literature raises with respect to the present case is not the mission but the concentration, because a configuration that resists capital capture equally resists every other form of external accountability, including the forms that a society might have reason to want. The article regards the concern as well founded and does not resolve it.

### Trade Press and Journalistic Record

The governance record reaches the public substantially through the business press rather than through the disclosure system. The coverage appears in [Bloomberg][ref_bloomberg], the [New York Times][ref_nyt], the [Wall Street Journal][ref_wsj], the [Washington Post][ref_washington_post], [SpaceNews][ref_spacenews], [Ars Technica space coverage][ref_arstechnica_space], [Payload][ref_payload], and [Payload Research][ref_payload_research]. The dependence of the analytical record on the journalistic record is a methodological weakness the article states rather than conceals.

## Contemporary Comparative Landscape

The contemporary landscape for the governance condition across the sector and the adjacent technology sector exhibits a range of configurations.

Blue Origin occupies a configuration that satisfies the governance condition by a different route. The firm has been substantially funded by a single individual without an external capital raise at scale, so that the capture hazard does not arise because no external claimant exists. The configuration may be stated compactly

$$e^{\text{founder}} \approx v^{\text{founder}} \approx 1 \qquad \text{so} \qquad w \approx 1 \quad \text{with} \quad C^{\text{contest}} = \infty$$

with the contestability infinite despite a unit wedge. The route is available only to a founder whose independent resources are commensurate with the mission's capital requirement, and the Portfolio-Patience article A288 will treat the consequences of the route for the pace of the development. The record is available through the [Blue Origin press releases][ref_blue_origin_press].

Rocket Lab operates as a publicly listed company under a conventional single-class structure, and therefore satisfies none of the governance condition's requirements. The configuration is the control condition of the sector, in the sense that it is what a space-launch firm looks like when it raises public capital on ordinary terms. The record is available through the [Rocket Lab press releases][ref_rocket_lab_press].

The United Launch Alliance occupies the limiting case in the opposite direction. The entity is a joint venture of two incumbent parents, so that the control resides entirely with parties whose principal businesses lie elsewhere. The configuration is the pure form of what the governance condition is intended to prevent, and the consequences for the investment horizon are visible in the vehicle-development record the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats. The record is available through the [United Launch Alliance news][ref_ula_press].

The adjacent technology sector offers the richer comparative material. The dual-class structures adopted at scale across the 2004 period forward have made the instrument a sector norm, and the range of wedges observed spans from approximately unity to values well above the SpaceX figure. The comparator disclosures appear in the [Alphabet investor materials][ref_alphabet_ir], the [Meta investor materials][ref_meta_ir], the [Snap investor materials][ref_snap_ir], the [Ford investor materials][ref_ford_ir], and the [Berkshire Hathaway shareholder materials][ref_berkshire], and the listed structures supply the only fully documented wedges available for comparison because the disclosure obligation that produces them is the obligation the SpaceX configuration avoids. The artificial-intelligence sector has produced two contemporary experiments in structures that go beyond the voting instrument. The OpenAI arrangement the counter-example section treats attempted control by a nonprofit board and failed. A further experiment places a portion of the board-election authority with a trust constituted to represent specific long-term interests rather than shareholder interests, described in the [long-term benefit trust announcement][ref_anthropic_ltbt]. The investor relationships in the sector are documented in part through the [Microsoft news archive][ref_microsoft_news]. The arrangement is too recent for any assessment, and the analytical question it raises is precisely the one the OpenAI episode answers unfavorably, namely whether a formal authority unaccompanied by a resource position can prevail when tested.

The broader private-market landscape gives the relevant base rate. The expansion of the private capital pool that [Ewens and Farre-Mensa 2020][research_ewens_farre_mensa_2020] document has produced a cohort of firms that reach substantial scale without listing, and the venture-capital literature in [Gompers and Lerner 2001][book_gompers_lerner_2001], [Metrick and Yasuda 2011][book_metrick_yasuda_2011], [Lerner 2009][book_lerner_2009], [Kortum and Lerner 2000][research_kortum_lerner_2000], and [Hall and Lerner 2010][research_hall_lerner_2010] documents the institutional apparatus that supports them. The practitioner literature in [Thiel 2014][book_thiel_2014] Zero to One, [Ries 2011][book_ries_2011] The Lean Startup, [Blank 2013][book_blank_2013] The Four Steps to the Epiphany, and [Moore 1991][book_moore_1991] Crossing the Chasm has substantially normalized the founder-control preference within the sector, and the regional-institutional treatments in [Saxenian 1994][book_saxenian_1994] Regional Advantage, [Kenney 2000][book_kenney_2000] Understanding Silicon Valley, [Lecuyer 2006][book_lecuyer_2006] Making Silicon Valley, and [Klepper 2016][book_klepper_2016] Experimental Capitalism document the conditions under which the preference became enforceable.

The institutional-investor and index-provider response constitutes a countervailing force that the landscape must include. The [Council of Institutional Investors][ref_cii] has advocated one-share-one-vote policies and mandatory sunset provisions in its [dual-class stock position][ref_cii_dual_class], the proxy advisers whose recommendations shape institutional voting publish their policies through [ISS][ref_iss_governance] and [Glass Lewis][ref_glass_lewis], and index providers including [S&P Dow Jones Indices][ref_spdji] and [FTSE Russell][ref_ftse_russell] have at various points restricted the inclusion of multi-class issuers. The corporate-governance practice literature that the [Conference Board][ref_conference_board] publishes documents the diffusion of the policies. The pressure operates only on listed firms, which is a further reason the unlisted configuration is attractive to a controller who values control. The effect allows the brief statement that the governance-pressure gradient runs

$$P^{\text{pressure}}\!\left( \text{listed, single class} \right) > P^{\text{pressure}}\!\left( \text{listed, dual class} \right) \gg P^{\text{pressure}}\!\left( \text{unlisted} \right)$$

with the unlisted configuration substantially outside the reach of the instruments the institutional investors have developed. The comparison set arrayed by the wedge can be written as

$$w^{\text{ULA}} \approx w^{\text{Rocket Lab}} \approx 1 \; < \; w^{\text{SpaceX}} \approx 1.9 \; < \; w^{\text{Novo}} \approx 2.8 \; \ll \; w^{\text{Bosch trust}} \approx 9300$$

with the ordering establishing that the SpaceX wedge is unremarkable by the standards of the arrangements that have demonstrated the longest persistence. The analytically operative variable is therefore not the wedge magnitude but the combination of the wedge with the financing channel and the successor provision.

## Comparative Cross-Sectional Analysis

The governance condition applies to the organization set as a cross-sectional scoring exercise across the five sub-properties the pattern-extraction section states. The closure vector has the form

$$\boldsymbol{\phi}_j^{\text{governance}} \in \{0, 1\}^{5}$$

with each organization's vector indicating the satisfaction status across the formal-instrument, effective-alignment, financing-channel, successor-commitment, and mission-specificity sub-properties.

SpaceX exhibits closure on the formal-instrument, effective-alignment, financing-channel, and mission-specificity sub-properties, and non-closure on the successor-commitment sub-property. The single non-closure is the analytically important finding of the exercise, because it identifies the respect in which the configuration differs from the centurial precedents rather than the respect in which it resembles them.

Blue Origin exhibits closure on the effective-alignment, financing-channel, and mission-specificity sub-properties, with the formal instrument unnecessary and the successor commitment absent. OpenAI exhibited closure on the formal-instrument and mission-specificity sub-properties and non-closure on the effective-alignment sub-property, and the non-closure was decisive. The foundation-owned precedents exhibit closure on all five, and they are the only organizations in the comparison set that do. The publicly listed single-class firms exhibit closure on none.

The cross-sectional pattern indicates that the formal-instrument sub-property is the easiest to satisfy and the successor-commitment sub-property the hardest, and that the two are substantially uncorrelated across the set. The correlation structure is stated compactly as

$$\operatorname{corr}_j\!\left( \phi_{j,1}^{\text{formal}}, \; \phi_{j,4}^{\text{successor}} \right) \approx 0$$

with the adoption of a voting instrument carrying substantially no information about whether the arrangement will survive the controller. The finding is the reason the article treats the successor question as the principal open question rather than as a detail.

## Data Sources and Reconstruction Methodology

The article draws on primary and secondary sources to reconstruct the governance trajectory, and it confronts an evidentiary situation substantially worse than that of any other article in the series.

The primary-source layer comprises the statutory and case-law materials identified in the Historiographical Gap section, the exempt-offering notices that reach the public record, the corporate communications of the firm and the comparison organizations, and the foundation documentation for the centurial precedents. The statutory and foundation materials are complete and authoritative. The SpaceX-materials are neither.

The secondary-source layer comprises the biographical and trade-press record identified above.

The reconstruction methodology proceeds by triangulation. The ownership and voting figures are assembled from trade-press reports of round terms, litigation disclosures in unrelated matters, and investor communications that reach the public indirectly. Where the sources disagree the article reports the range rather than selecting a point estimate. Where a figure is reported by a single source without corroboration the article marks it as such.

The empirical-record limitations are severe and are stated explicitly rather than managed. The firm publishes no financial statements, no ownership schedule, no charter, and no bylaws. The share classes and the per-class voting ratios are not public. The board composition is not published. The protective provisions negotiated in the successive rounds are not public. The consequence is that substantially every quantitative claim in this article about the SpaceX capital structure carries a wider uncertainty than the corresponding claims in the preceding articles of the series, and the reader should discount them accordingly. The qualitative claim that the founder retains a voting majority is corroborated across substantially all available sources and is the single claim the article treats as well established.

## Alternative Analytical Frameworks

The governance framing the article develops is one of several analytical frameworks the surrounding literature applies to the configuration.

The agency framing developed in [Jensen and Meckling 1976][research_jensen_meckling_1976], [Fama and Jensen 1983][research_fama_jensen_1983], and [Shleifer and Vishny 1997][research_shleifer_vishny_1997] is the principal alternative and treats the configuration as an entrenchment that raises the residual loss. The framing predicts value destruction increasing in the wedge and the tenure, and it predicts expropriation of the minority through related-party transactions and perquisite consumption. The available record does not permit a test of the prediction, because the transactions the prediction concerns are precisely the transactions an unlisted firm does not disclose. The prediction may be written

$$V\!\left( w, \tau \right) = V^{\ast} - \beta_1 w - \beta_2 w \tau, \qquad \beta_1, \beta_2 > 0$$

with the value declining in the wedge and the decline compounding with the tenure. The framing is not refuted by the SpaceX record. It is untested by it.

The stewardship framing treats the controller as a steward whose objective is aligned with the long-run enterprise rather than as an agent whose objective diverges from it, and it predicts that a control configuration insulating the steward improves rather than degrades the outcome. The stewardship premise takes the compact statement as a restriction on the objective

$$U^{\text{controller}} = U^{\text{enterprise}} \qquad \text{against the agency premise} \qquad U^{\text{controller}} = e \cdot U^{\text{enterprise}} + B^{\text{private}}$$

with the two framings differing in whether the private-benefit term is present rather than in any empirical claim about the observed behavior. The framing is the mirror image of the agency framing and shares its weakness, in that both derive their predictions from an assumption about the controller's objective that the evidence is asked to confirm rather than to establish.

The resource-dependence framing, whose organizational-sociology antecedents appear in [Selznick 1949][book_selznick_1949] TVA and the Grass Roots and whose market-architecture development appears in [Fligstein 2001][book_fligstein_2001] The Architecture of Markets, treats the effective control as determined by the pattern of dependencies rather than by the formal authority. The dependence-weighted control has the concise form

$$v^{\text{effective}}_i = \frac{d_i \, \sigma_i}{\sum_j d_j \, \sigma_j}$$

with $d_i$ the criticality of the resource the party yields and $\sigma_i$ the credibility of the withdrawal threat, and with the formal votes entering only insofar as they constitute one resource among others. The framing contributes the analytical apparatus that the OpenAI counter-example requires and that the voting-rights literature lacks entirely, and the article adopts it as a supplement rather than as an alternative.

The managerial-power framing treats the governance arrangements as themselves the product of the specific power they purport to constrain, and it reads the dual-class instrument as an outcome of a bargaining process in which the founder's bargaining power was decisive. The framing is consistent with the bargaining apparatus the Cross-Disciplinary Framings section develops and it provides a deflationary reading under which the configuration reflects nothing beyond the relative scarcity of credible mission-directed founders against abundant capital.

The political-economy and rent-seeking framing developed in [Buchanan and Tullock 1962][book_buchanan_tullock_1962], [Stigler 1971][research_stigler_1971], and [Krueger 1974][research_krueger_1974] treats the configuration as one element of a broader arrangement in which a concentrated private interest obtains favorable treatment from a state customer. The framing raises the accountability concern that the critical literature states, and it observes correctly that the governance condition as the article formulates it is entirely silent on the question of accountability to any party other than the capital providers.

The behavioral framing developed in [Kahneman and Tversky 1979][research_kahneman_tversky_1979], [Tversky and Kahneman 1992][research_tversky_kahneman_1992], [Kahneman 2011][book_kahneman_2011], [Staw 1976][research_staw_1976], and [Ross and Staw 1993][research_ross_staw_1993] treats the insulated controller as specifically exposed to the escalation and overconfidence hazards that an external correction would otherwise check. The escalation hazard takes the form

$$P\!\left( \text{continue} \mid \text{negative signal} \right) = g\!\left( c^{\text{sunk}}, \; r^{\text{public commitment}}, \; 1 - \eta^{\text{external check}} \right)$$

increasing in the sunk cost, in the publicity of the prior commitment, and in the absence of the external check. The configuration the article describes sets the third argument near its maximum by construction. The framing offers the most concrete statement of the cost the configuration incurs, and it is the framing under which the Space Shuttle and Constellation program records that the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats are read as evidence that the external correction is itself unreliable.

The real-options framing developed in [Dixit and Pindyck 1994][book_dixit_pindyck_1994] and [Trigeorgis 1996][book_trigeorgis_1996] treats the retained control as an option to redirect the enterprise in contingencies not yet realized, and it values the configuration by the option value rather than by the expected cash flows. The option value can be written as

$$V^{\text{control}} = \sum_{s \in \mathcal{S}} p(s) \cdot \left[ \max_{a \in \mathcal{A}} V(a, s) - V\!\left( a^{\text{default}}, s \right) \right]^{+}$$

with the value equal to the probability-weighted gain from being able to choose the action rather than accepting the default across the contingency set. The value rises with the dispersion of the contingencies, which is why the control premium is largest precisely where the programme is least predictable. The framing gives the formal account of why a controller facing a highly uncertain long-horizon programme values control disproportionately to any individual decision the control would be used to make.

The legal-origins and comparative-governance framing developed in [La Porta Lopez-de-Silanes Shleifer and Vishny 1998][research_laporta_et_al_1998], [Roe 1994][book_roe_1994], and [Easterbrook and Fischel 1991][book_easterbrook_fischel_1991] treats the configuration as an artifact of the permissive United States chartering regime and observes that the arrangement would be unavailable or substantially constrained in other jurisdictions. The framing correctly identifies the configuration as contingent on a legal settlement that is itself contested and revisable.

The financial-sociology framing developed in [MacKenzie 2006][book_mackenzie_2006], [Ho 2009][book_ho_2009], [Zaloom 2006][book_zaloom_2006], [Preda 2009][book_preda_2009], and [Krippner 2011][book_krippner_2011] treats the short-horizon pressure the configuration is designed to resist as an institutionally constructed artifact rather than as a natural property of dispersed ownership, and it raises the possibility that the problem the governance condition solves is a problem a differently organized capital market would not present.

The resource-based and dynamic-capabilities framing developed in [Wernerfelt 1984][research_wernerfelt_1984], [Barney 1991][research_barney_1991], [Teece Pisano and Shuen 1997][research_teece_pisano_shuen_1997], and [Teece 2007][research_teece_2007] treats the control configuration as one resource among the bundle that produces the competitive position, and it predicts that the arrangement is valuable in proportion to the specificity of the other assets it governs. The framing yields the reason the configuration matters more here than at a firm whose assets are redeployable, and it contributes equally the prediction that the arrangement's value declines as the capability base becomes more general, which is precisely the direction the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] documents.

The platform and two-sided-market framing developed in [Rochet and Tirole 2003][research_rochet_tirole_2003], [Rochet and Tirole 2006][research_rochet_tirole_2006], [Parker and Van Alstyne 2005][research_parker_vanalstyne_2005], [Eisenmann Parker and Van Alstyne 2006][research_eisenmann_et_al_2006], [Armstrong 2006][research_armstrong_2006], [Rysman 2009][research_rysman_2009], [Gawer and Cusumano 2014][research_gawer_cusumano_2014], [Hagiu and Wright 2015][research_hagiu_wright_2015], [Cusumano and Gawer 2002][book_cusumano_gawer_2002] Platform Leadership, and [Van Alstyne Parker and Choudary 2016][book_vanalstyne_parker_choudary_2016] Platform Revolution treats the enterprise as a platform whose governance affects the willingness of complementors to invest. The framing raises a consideration the shareholder-centered literature omits entirely, namely that a concentrated and durable control may be attractive rather than threatening to a complementor who requires assurance that the platform rules will not change.

The path-dependence framing developed in [David 1985][research_david_1985] Clio and the Economics of QWERTY and [Arthur 1989][research_arthur_1989] Competing Technologies Increasing Returns and Lock-In treats the configuration as an early choice whose persistence reflects accumulated switching costs rather than continuing optimality, and the industry-life-cycle treatment in [Klepper 1996][research_klepper_1996] and [Klepper 2010][research_klepper_2010] supplies the sector-level analogue.

The actor-network framing developed in [Latour 1987][book_latour_1987], [Callon 1986][research_callon_1986] Some Elements of a Sociology of Translation, and [Law 1987][research_law_1987] Technology and Heterogeneous Engineering treats the control as an achievement continuously reproduced through the enrollment of human and non-human actors rather than as a property conferred by a document. The framing supplies the most complete account of the OpenAI episode, in which a formal document conferred an authority that the network declined to enact.

The evolutionary and selection framing developed in [Nelson and Winter 1982][book_nelson_winter_1982] and [Metcalfe 1998][book_metcalfe_1998] supplies the caution that the observed configuration is a survivor and that the population of founder-controlled ventures whose controllers persisted in mistaken courses until the enterprise failed is substantially unobserved.

## Pattern Extraction

The governance pattern that the SpaceX case exhibits admits the following abstract statement without naming any downstream application. A mission-directed technology venture achieves the governance closure when the venture can absorb the quantity of external capital its mission requires across the duration its mission requires without transferring to the capital providers the authority to alter what the mission is.

The abstract governance mechanic requires joint satisfaction of five sub-properties, admitting the compact conjunctive form

$$\Phi^{\text{governance}} = \prod_{k=1}^{5} \phi_k, \qquad \phi_k \in \{0,1\}$$

with the closure obtaining only when every sub-property indicator takes the value unity.

First, the venture must possess a formal instrument that decouples the voting rights from the cash-flow rights, so that the control condition survives an arbitrary dilution sequence.

Second, the effective control must align with the formal control. The party holding the votes must also occupy a position in the resource-dependence structure such that the exercise of the formal authority does not destroy the organization's capacity to act. A formal authority held by a party on whom the organization does not depend is not a control.

Third, the venture must obtain its capital through a channel that does not itself impose the governance obligations the instrument is designed to avoid, and it must supply the liquidity its personnel require by a mechanism other than a public listing.

Fourth, the arrangement must bind the controller's successors, or it terminates with the controller. The transition hazard has the form

$$P\!\left( \text{configuration survives transition} \right) = P\!\left( \text{successor identified} \right) \cdot P\!\left( \text{instrument transfers} \right) \cdot P\!\left( \text{successor sustains mission} \right)$$

with the product requiring all three factors and with an arrangement lacking any formal successor provision setting the second factor by default rather than by design. This is the sub-property the centurial precedents satisfy and the SpaceX configuration does not.

Fifth, the mission must be specified with sufficient precision that a deviation from it is observable. A mission stated so broadly that substantially any course of action satisfies it provides no constraint, and the governance apparatus protecting it protects nothing.

The relationship among the sub-properties is not symmetric. The first is the easiest to obtain and receives substantially all of the attention in the practitioner literature. The second is the one whose failure the OpenAI case demonstrates and which the voting-rights literature does not address. The fourth is the one that distinguishes an arrangement lasting a career from one lasting a century.

The abstract mechanic permits a diagnostic procedure applicable to a candidate case in an adjacent domain, stated as an ordered test vector

$$\tau = \left( w > 1, \;\; v^{\text{effective}} \approx v^{\text{formal}}, \;\; G^{\text{channel}} \approx 0, \;\; \exists \, \text{successor binding}, \;\; \text{mission falsifiable} \right)$$

with each component evaluating one of the five sub-properties. The procedure's practical value lies in the second and fourth components, because a candidate case will almost always satisfy the first and will almost never be examined on the others.

The mechanic carries a cost that the statement should not conceal. A configuration that resists capital capture resists every other form of external correction by the same mechanism, and it therefore converts the question of whether the venture pursues a worthwhile mission into a question about the judgment of an individual or a small body. The mechanic is not a guarantee of a good outcome. It is a transfer of the decision about what counts as a good outcome from the capital market to the controller.

## Cross-References to the Series

The article back-references the [series opener][related_post_a281_spacex_framing] for the seven-plus-three framework introduction and the founding narrative. The article back-references the [Value Gradient article A282][related_post_a282_spacex_value_gradient] for the reusability development whose investment horizon the governance configuration protected. The article back-references the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] for the state-customer relationships that supplied the revenue against which the private financing was raised. The article back-references the [Value Capture article A284][related_post_a284_spacex_value_capture] for the Starlink business whose separation question the article treats. The article back-references the [Decomposability article A285][related_post_a285_spacex_decomposability] for the vehicle-family structure across which the capital was allocated. The article back-references the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] for the self-financing loop whose internal capital allocation the governance configuration makes possible, and for the mission-persistence sub-property that the article identified as unresolved and that the present article locates in the governance apparatus.

The article forward-references the subsequent articles. The Portfolio-Patience article A288 treats the internalized portfolio across which the controller allocates capital without external review. The Government-Anchor Capital-Formation Leg article A289, the Patient-Private Capital-Formation Leg article A290, and the Category-Dominating Commercial Spinoff article A291 treat the three financing channels whose governance terms the present article analyzes. The closing article A292 synthesizes across the framework.

The article cross-references the existing published corpus including the [Introduction to Space Studies article A90][related_post_a90_intro_space_studies], the [History of Rocketplanes article A96][related_post_a96_history_rocketplanes], the [What Does the United States Space Force Do article A97][related_post_a97_us_space_force], the [Framing and the Co-Development Mechanism article A237][related_post_a237_aerospace_framing], the [Silicon Valley from Defense Contracting article A246][related_post_a246_silicon_valley_defense], the [Software-Defined Aerospace article A247][related_post_a247_software_defined_aerospace], the [Contemporary Snapshot article A248][related_post_a248_contemporary_snapshot], the [What a Patent Is and Is Not article A161][related_post_a161_patent_intro], the [Patents Trade Secrets and the Disclosure Tradeoff article A164][related_post_a164_patents_trade_secrets], and the [Why Startups Actually Fail article A167][related_post_a167_startup_failure].

## Terminological Note

The article adopts terminology consistent with the corporate-governance conventions and departs from them where the departure is analytically necessary. The term "control" refers to the authority to determine the composition of the board and thereby the ordinary business of the enterprise, and not to the unconditional authority to take any action. The term "wedge" refers to the ratio of the voting share to the cash-flow share. The term "capital capture" refers to a change in the mission objective attributable to the preferences of the capital providers, and it is distinguished from the expropriation that the agency literature treats, which concerns the transfer of value rather than the redirection of purpose. The term "formal control" refers to the authority the governing documents confer, and the term "effective control" refers to the authority that survives its own exercise. The term "sunset provision" refers to a charter term under which a superior voting class converts to an ordinary class upon a triggering event or the passage of an interval. The term "foundation ownership" refers to an arrangement in which an entity without personal residual claimants holds the controlling interest.

## Load-Bearing Open Questions

The article closes with the load-bearing open questions the governance treatment leaves unresolved. First, the central claim that the control configuration prevented a capture that would otherwise have occurred is not demonstrable, because no capture attempt is recorded and the counterfactual is unobservable. Second, the quantitative capital-structure claims rest on reconstructive estimates that the private-firm status precludes verifying. Third, the successor question is entirely unresolved, and the configuration at the drafting date provides no mechanism by which the arrangement survives the controller. Fourth, the relationship between the governance configuration and the accountability of the enterprise to parties other than its capital providers is not addressed by the condition as formulated, and the critical literature is correct that the omission is substantive rather than incidental. Fifth, the applicability of the empirical dual-class findings to an unlisted firm is unresolved in both directions, and the selection structure of the available samples makes the direction of the bias genuinely uncertain. Sixth, the effect of a Starlink separation on the configuration is unknown and would constitute the first substantial test of the arrangement.

## References

### Books

- [Abbott 1988 The System of Professions][book_abbott_1988]
- [Acemoglu and Robinson 2012 Why Nations Fail][book_acemoglu_robinson_2012]
- [Amsden 1989 Asia's Next Giant][book_amsden_1989]
- [Beinhocker 2006 The Origin of Wealth][book_beinhocker_2006]
- [Berger 2021 Liftoff][book_berger_2021]
- [Berger 2024 Reentry][book_berger_2024]
- [Berle and Means 1932 The Modern Corporation and Private Property][book_berle_means_1932]
- [Bilby 1986 The General David Sarnoff and the Rise of the Communications Industry][book_bilby_1986]
- [Blank 2013 The Four Steps to the Epiphany][book_blank_2013]
- [Bork 1978 The Antitrust Paradox][book_bork_1978]
- [Buchanan and Tullock 1962 The Calculus of Consent][book_buchanan_tullock_1962]
- [Chandler 1962 Strategy and Structure][book_chandler_1962]
- [Chandler 1977 The Visible Hand][book_chandler_1977]
- [Chandler 1990 Scale and Scope][book_chandler_1990]
- [Chang 2002 Kicking Away the Ladder][book_chang_2002]
- [Chernow 2004 Titan The Life of John D Rockefeller Sr][book_chernow_2004]
- [Copeland and Antikarov 2001 Real Options A Practitioner's Guide][book_copeland_antikarov_2001]
- [Creswell 2014 Research Design][book_creswell_2014]
- [Cusumano and Gawer 2002 Platform Leadership][book_cusumano_gawer_2002]
- [Davenport 2018 The Space Barons][book_davenport_2018]
- [Dixit and Pindyck 1994 Investment Under Uncertainty][book_dixit_pindyck_1994]
- [Easterbrook and Fischel 1991 The Economic Structure of Corporate Law][book_easterbrook_fischel_1991]
- [Evans 1995 Embedded Autonomy][book_evans_1995]
- [Fernholz 2018 Rocket Billionaires][book_fernholz_2018]
- [Fligstein 2001 The Architecture of Markets][book_fligstein_2001]
- [Ford and Crowther 1922 My Life and Work][book_ford_crowther_1922]
- [Foster and McChesney 2011 The Endless Crisis][book_foster_mcchesney_2011]
- [Freeman 1987 Technology Policy and Economic Performance][book_freeman_1987]
- [Gertner 2012 The Idea Factory][book_gertner_2012]
- [Gompers and Lerner 2001 The Money of Invention][book_gompers_lerner_2001]
- [Greif 2006 Institutions and the Path to the Modern Economy][book_grief_2006]
- [Grimsey and Lewis 2004 Public Private Partnerships][book_grimsey_lewis_2004]
- [Handberg 1994 Reinventing NASA][book_handberg_1994]
- [Hansmann 1996 The Ownership of Enterprise][book_hansmann_1996]
- [Hargrove 1994 Prisoners of Myth][book_hargrove_1994]
- [Hart 1995 Firms Contracts and Financial Structure][book_hart_1995]
- [Hartley 2017 The Economics of Arms][book_hartley_2017]
- [Hiltzik 1999 Dealers of Lightning][book_hiltzik_1999]
- [Ho 2009 Liquidated An Ethnography of Wall Street][book_ho_2009]
- [Hounshell 1984 From the American System to Mass Production][book_hounshell_1984]
- [Hovenkamp 2005 The Antitrust Enterprise][book_hovenkamp_2005]
- [Isaacson 2011 Steve Jobs][book_isaacson_2011]
- [Isaacson 2023 Elon Musk][book_isaacson_2023]
- [Johnson 1982 MITI and the Japanese Miracle][book_johnson_1982]
- [Kahneman 2011 Thinking Fast and Slow][book_kahneman_2011]
- [Kauffman 1993 The Origins of Order][book_kauffman_1993]
- [Kearns and Nadler 1992 Prophets in the Dark][book_kearns_nadler_1992]
- [Kenney 2000 Understanding Silicon Valley][book_kenney_2000]
- [Klepper 2016 Experimental Capitalism][book_klepper_2016]
- [Krippner 2011 Capitalizing on Crisis][book_krippner_2011]
- [Kuhn 1962 The Structure of Scientific Revolutions][book_kuhn_1962]
- [Kunda 1992 Engineering Culture][book_kunda_1992]
- [Laffont and Tirole 1993 A Theory of Incentives in Procurement and Regulation][book_laffont_tirole_1993]
- [Larson 1977 The Rise of Professionalism][book_larson_1977]
- [Latour 1987 Science in Action][book_latour_1987]
- [Lecuyer 2006 Making Silicon Valley][book_lecuyer_2006]
- [Lerner 2009 Boulevard of Broken Dreams][book_lerner_2009]
- [Levin 2010 The Wires That Bind][book_levin_2010]
- [Lundvall 1992 National Systems of Innovation][book_lundvall_1992]
- [MacKenzie 2006 An Engine Not a Camera][book_mackenzie_2006]
- [Malone 2014 The Intel Trinity][book_malone_2014]
- [Mazzucato 2013 The Entrepreneurial State][book_mazzucato_2013]
- [Mazzucato 2021 Mission Economy][book_mazzucato_2021]
- [McAfee and McMillan 1988 Incentives in Government Contracting][book_mcafee_mcmillan_1988]
- [McCurdy 1994 Inside NASA][book_mccurdy_1994]
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
- [Norberg and O'Neill 1996 Transforming Computer Technology][book_norberg_oneill_1996]
- [North 1990 Institutions Institutional Change and Economic Performance][book_north_1990]
- [Ormerod 2005 Why Most Things Fail][book_ormerod_2005]
- [Osborne 2000 Public-Private Partnerships][book_osborne_2000]
- [Osborne and Rubinstein 1990 Bargaining and Markets][book_osborne_rubinstein_1990]
- [Ostrom 1990 Governing the Commons][book_ostrom_1990]
- [Penrose 1959 The Theory of the Growth of the Firm][book_penrose_1959]
- [Perez 2002 Technological Revolutions and Financial Capital][book_perez_2002]
- [Posner 2001 Antitrust Law][book_posner_2001]
- [Preda 2009 Framing Finance][book_preda_2009]
- [Pugh 1995 Building IBM][book_pugh_1995]
- [Pugh Johnson and Palmer 1991 IBM's 360 and Early 370 Systems][book_pugh_johnson_palmer_1991]
- [Ries 2011 The Lean Startup][book_ries_2011]
- [Robins 2006 The Corporation That Changed the World][book_robins_2006]
- [Roe 1994 Strong Managers Weak Owners][book_roe_1994]
- [Ruttan 2006 Is War Necessary for Economic Growth][book_ruttan_2006]
- [Saxenian 1994 Regional Advantage][book_saxenian_1994]
- [Schroeder 2008 The Snowball][book_schroeder_2008]
- [Schumpeter 1942 Capitalism Socialism and Democracy][book_schumpeter_1942]
- [Selznick 1949 TVA and the Grass Roots][book_selznick_1949]
- [Smith and Alexander 1988 Fumbling the Future][book_smith_alexander_1988]
- [Srnicek 2017 Platform Capitalism][book_srnicek_2017]
- [Steensgaard 1974 The Asian Trade Revolution of the Seventeenth Century][book_steensgaard_1974]
- [Stern 2011 The Company-State][book_stern_2011]
- [Stone 2013 The Everything Store][book_stone_2013]
- [Temin and Galambos 1987 The Fall of the Bell System][book_temin_galambos_1987]
- [Thiel 2014 Zero to One][book_thiel_2014]
- [Tirole 2006 The Theory of Corporate Finance][book_tirole_2006]
- [Trigeorgis 1996 Real Options][book_trigeorgis_1996]
- [Van Alstyne Parker and Choudary 2016 Platform Revolution][book_vanalstyne_parker_choudary_2016]
- [Vance 2015 Elon Musk][book_vance_2015]
- [Wade 1990 Governing the Market][book_wade_1990]
- [Weiss 2014 America Inc][book_weiss_2014]
- [Williamson 1985 The Economic Institutions of Capitalism][book_williamson_1985]
- [Woo-Cumings 1999 The Developmental State][book_woo_cumings_1999]
- [Wu 2010 The Master Switch][book_wu_2010]
- [Yescombe 2007 Public-Private Partnerships Principles of Policy and Finance][book_yescombe_2007]
- [Yin 2014 Case Study Research and Applications][book_yin_2014]
- [Zaloom 2006 Out of the Pits][book_zaloom_2006]
- [Zuboff 2019 The Age of Surveillance Capitalism][book_zuboff_2019]

### Reference

- [Alphabet Investor Relations][ref_alphabet_ir]
- [Ars Technica Space Coverage][ref_arstechnica_space]
- [Berkshire Hathaway Shareholder Materials][ref_berkshire]
- [Bloomberg][ref_bloomberg]
- [Blue Origin Press Releases][ref_blue_origin_press]
- [Bosch Annual Reporting][ref_bosch_annual_report]
- [Bosch Corporate Documentation][ref_bosch_company]
- [Carl Zeiss Corporate Documentation][ref_zeiss_corporate]
- [Carl Zeiss Stiftung][ref_carl_zeiss_stiftung]
- [Columbia Law School Blue Sky Blog][ref_columbia_blue_sky]
- [Council of Institutional Investors][ref_cii]
- [Council of Institutional Investors Dual-Class Stock Position][ref_cii_dual_class]
- [Danish Business Authority][ref_danish_business_authority]
- [Delaware Court of Chancery][ref_delaware_chancery]
- [Delaware Courts Opinions Archive][ref_delaware_opinions]
- [Delaware Division of Corporations][ref_delaware_division_corporations]
- [Delaware General Corporation Law Subchapter I Formation][ref_dgcl_sc01]
- [Delaware General Corporation Law Subchapter IV Directors and Officers][ref_dgcl_sc04]
- [Delaware General Corporation Law Subchapter V Stock and Dividends][ref_dgcl_sc05]
- [Delaware General Corporation Law Subchapter VII Meetings Elections Voting and Notice][ref_dgcl_sc07]
- [Delaware General Corporation Law Title 8 Chapter 1][ref_dgcl]
- [Dodd-Frank Wall Street Reform and Consumer Protection Act of 2010][ref_dodd_frank_2010]
- [European Corporate Governance Institute][ref_ecgi]
- [European Union Shareholder Rights Directive 2017/828][ref_eu_shareholder_rights_directive]
- [Ford Motor Company Investor Relations][ref_ford_ir]
- [FTSE Russell][ref_ftse_russell]
- [German Aktiengesetz][ref_german_aktiengesetz]
- [Glass Lewis][ref_glass_lewis]
- [Harvard Law School Forum on Corporate Governance][ref_harvard_corpgov_forum]
- [IBM Archives][ref_ibm_archives]
- [Institutional Shareholder Services][ref_iss_governance]
- [Jumpstart Our Business Startups Act of 2012][ref_jobs_act_2012]
- [Meta Investor Relations][ref_meta_ir]
- [Microsoft News Archive][ref_microsoft_news]
- [Nasdaq Listing Rules][ref_nasdaq_listing_rules]
- [National Bureau of Economic Research][ref_nber]
- [New York Times Space Coverage][ref_nyt]
- [Novo Holdings][ref_novo_holdings]
- [Novo Nordisk Foundation][ref_novo_nordisk_foundation]
- [Novo Nordisk Investor Disclosures][ref_novo_nordisk_investors]
- [NYSE Listed Company Manual][ref_nyse_listed_company_manual]
- [OECD Principles of Corporate Governance][ref_oecd_corporate_governance]
- [OpenAI Announcements][ref_openai_news]
- [OpenAI Charter][ref_openai_charter]
- [Payload][ref_payload]
- [Payload Research][ref_payload_research]
- [Robert Bosch Stiftung][ref_bosch_stiftung]
- [Rocket Lab Press Releases][ref_rocket_lab_press]
- [S&P Dow Jones Indices][ref_spdji]
- [Sarbanes-Oxley Act of 2002][ref_sarbanes_oxley_2002]
- [SEC EDGAR Company Search][ref_sec_edgar]
- [SEC Form D Exempt Offering Notices][ref_sec_form_d]
- [SEC Investor Education Materials][ref_sec_investor_gov]
- [SEC Regulation 14E Tender Offer Requirements][ref_reg_14e]
- [SEC Regulation D and Securities Act Rules 17 CFR Part 230][ref_reg_d]
- [SEC Rule 12g-1 Registration Threshold][ref_rule_12g1]
- [SEC Rule 13e-4 Issuer Tender Offers][ref_rule_13e4]
- [SEC Rule 144 Resale of Restricted Securities][ref_rule_144]
- [SEC Rule 14a-8 Shareholder Proposals][ref_rule_14a8]
- [SEC Rule 506 Private Placement Safe Harbor][ref_rule_506]
- [SEC Rule 701 Compensatory Benefit Plan Exemption][ref_rule_701]
- [SEC Schedule 13D Beneficial Ownership Disclosure][ref_schedule_13d]
- [Securities Act Section 4 Exempted Transactions][ref_securities_act_4a2]
- [Securities Exchange Act Section 12 Registration Requirements][ref_exchange_act_12g]
- [Snap Investor Relations][ref_snap_ir]
- [Social Science Research Network][ref_ssrn]
- [SpaceNews][ref_spacenews]
- [SpaceX Corporate Site][ref_spacex_company]
- [SpaceX News Archive][ref_spacex_news_archive]
- [Tesla Investor Relations][ref_tesla_ir]
- [Texas Business Organizations Code][ref_texas_boc]
- [Texas Secretary of State][ref_texas_sos]
- [The Conference Board][ref_conference_board]
- [The Long-Term Benefit Trust][ref_anthropic_ltbt]
- [United Kingdom Companies Act 2006][ref_uk_companies_act_2006]
- [United Launch Alliance News][ref_ula_press]
- [Wall Street Journal Technology Coverage][ref_wsj]
- [Washington Post Technology Coverage][ref_washington_post]

### Research

- [Armstrong 2006 Competition in Two-Sided Markets][research_armstrong_2006]
- [Arthur 1989 Competing Technologies Increasing Returns and Lock-In by Historical Events][research_arthur_1989]
- [Bajari and Tadelis 2001 Incentives Versus Transaction Costs A Theory of Procurement Contracts][research_bajari_tadelis_2001]
- [Bajari McMillan and Tadelis 2009 Auctions Versus Negotiations in Procurement][research_bajari_mcmillan_tadelis_2009]
- [Barney 1991 Firm Resources and Sustained Competitive Advantage][research_barney_1991]
- [Bebchuk and Kastiel 2017 The Untenable Case for Perpetual Dual-Class Stock][research_bebchuk_kastiel_2017]
- [Bebchuk Kraakman and Triantis 2000 Stock Pyramids Cross-Ownership and Dual Class Equity][research_bebchuk_kraakman_triantis_2000]
- [Binmore Rubinstein and Wolinsky 1986 The Nash Bargaining Solution in Economic Modelling][research_binmore_rubinstein_wolinsky_1986]
- [Black and Scholes 1973 The Pricing of Options and Corporate Liabilities][research_black_scholes_1973]
- [Block 2008 Swimming Against the Current The Rise of a Hidden Developmental State][research_block_2008]
- [Bonvillian 2018 DARPA and the Advanced Research Projects Agency Model][research_bonvillian_2018]
- [Bovaird 2004 Public-Private Partnerships From Contested Concepts to Prevalent Practice][research_bovaird_2004]
- [Callon 1986 Some Elements of a Sociology of Translation][research_callon_1986]
- [Che and Chung 1999 Contractual Remedies to the Holdup Problem][research_che_chung_1999]
- [Coase 1937 The Nature of the Firm][research_coase_1937]
- [Corts and Singh 2004 The Effect of Repeated Interaction on Contract Choice][research_corts_singh_2004]
- [David 1985 Clio and the Economics of QWERTY][research_david_1985]
- [DeAngelo and DeAngelo 1985 Managerial Ownership of Voting Rights][research_deangelo_deangelo_1985]
- [Eisenhardt and Martin 2000 Dynamic Capabilities What Are They][research_eisenhardt_martin_2000]
- [Eisenmann Parker and Van Alstyne 2006 Strategies for Two-Sided Markets][research_eisenmann_et_al_2006]
- [Ewens and Farre-Mensa 2020 The Deregulation of the Private Equity Markets and the Decline in IPOs][research_ewens_farre_mensa_2020]
- [Fama and Jensen 1983 Separation of Ownership and Control][research_fama_jensen_1983]
- [Finkelstein and Sanford 2000 Learning from Corporate Mistakes The Rise and Fall of Iridium][research_finkelstein_sanford_2000]
- [Gagnepain and Ivaldi 2002 Incentive Regulatory Policies][research_gagnepain_ivaldi_2002]
- [Gawer and Cusumano 2014 Industry Platforms and Ecosystem Innovation][research_gawer_cusumano_2014]
- [Gompers 1995 Optimal Investment Monitoring and the Staging of Venture Capital][research_gompers_1995]
- [Gompers Ishii and Metrick 2003 Corporate Governance and Equity Prices][research_gompers_ishii_metrick_2003]
- [Gompers Ishii and Metrick 2010 Extreme Governance An Analysis of Dual-Class Firms in the United States][research_gompers_ishii_metrick_2010]
- [Grossman and Hart 1986 The Costs and Benefits of Ownership][research_grossman_hart_1986]
- [Grossman and Hart 1988 One Share-One Vote and the Market for Corporate Control][research_grossman_hart_1988]
- [Hagiu and Wright 2015 Multi-Sided Platforms][research_hagiu_wright_2015]
- [Hall and Lerner 2010 The Financing of R and D and Innovation][research_hall_lerner_2010]
- [Harris and Raviv 1988 Corporate Governance Voting Rights and Majority Rules][research_harris_raviv_1988]
- [Hart and Moore 1990 Property Rights and the Nature of the Firm][research_hart_moore_1990]
- [Helfat and Peteraf 2003 The Dynamic Resource-Based View][research_helfat_peteraf_2003]
- [Hodge and Greve 2007 Public-Private Partnerships An International Performance Review][research_hodge_greve_2007]
- [Jensen 1986 Agency Costs of Free Cash Flow Corporate Finance and Takeovers][research_jensen_1986]
- [Jensen and Meckling 1976 Theory of the Firm Managerial Behavior Agency Costs and Ownership Structure][research_jensen_meckling_1976]
- [Kahneman and Tversky 1979 Prospect Theory][research_kahneman_tversky_1979]
- [Kalnins and Mayer 2004 Relationships and Hybrid Contracts][research_kalnins_mayer_2004]
- [Kaplan and Stromberg 2003 Financial Contracting Theory Meets the Real World][research_kaplan_stromberg_2003]
- [Kaplan and Stromberg 2004 Characteristics Contracts and Actions][research_kaplan_stromberg_2004]
- [Khan 2017 Amazon's Antitrust Paradox][research_khan_2017]
- [Klepper 1996 Entry Exit Growth and Innovation over the Product Life Cycle][research_klepper_1996]
- [Klepper 2010 The Origin and Growth of Industry Clusters][research_klepper_2010]
- [Kogut and Kulatilaka 1994 Operating Flexibility Global Manufacturing and the Option Value of a Multinational Network][research_kogut_kulatilaka_1994]
- [Kortum and Lerner 2000 Assessing the Contribution of Venture Capital to Innovation][research_kortum_lerner_2000]
- [Krueger 1974 The Political Economy of the Rent-Seeking Society][research_krueger_1974]
- [La Porta Lopez-de-Silanes Shleifer and Vishny 1998 Law and Finance][research_laporta_et_al_1998]
- [Law 1987 Technology and Heterogeneous Engineering][research_law_1987]
- [Lerner 1994 The Syndication of Venture Capital Investments][research_lerner_1994_syndication]
- [Levin and Tadelis 2010 Contracting for Government Services Theory and Evidence][research_levin_tadelis_2010]
- [Manne 1965 Mergers and the Market for Corporate Control][research_manne_1965]
- [McDonald and Siegel 1986 The Value of Waiting to Invest][research_mcdonald_siegel_1986]
- [Merton 1973 Theory of Rational Option Pricing][research_merton_1973]
- [Myers 1977 Determinants of Corporate Borrowing][research_myers_1977]
- [Myerson 1981 Optimal Auction Design][research_myerson_1981]
- [Nash 1950 The Bargaining Problem][research_nash_1950]
- [Parker and Van Alstyne 2005 Two-Sided Network Effects][research_parker_vanalstyne_2005]
- [Peteraf 1993 The Cornerstones of Competitive Advantage][research_peteraf_1993]
- [Rochet and Tirole 2003 Platform Competition in Two-Sided Markets][research_rochet_tirole_2003]
- [Rochet and Tirole 2006 Two-Sided Markets A Progress Report][research_rochet_tirole_2006]
- [Ross and Staw 1993 Organizational Escalation and Exit][research_ross_staw_1993]
- [Rubinstein 1982 Perfect Equilibrium in a Bargaining Model][research_rubinstein_1982]
- [Rysman 2009 The Economics of Two-Sided Markets][research_rysman_2009]
- [Sahlman 1990 The Structure and Governance of Venture-Capital Organizations][research_sahlman_1990]
- [Shleifer and Vishny 1997 A Survey of Corporate Governance][research_shleifer_vishny_1997]
- [Staw 1976 Knee-Deep in the Big Muddy][research_staw_1976]
- [Stigler 1971 The Theory of Economic Regulation][research_stigler_1971]
- [Teece 2007 Explicating Dynamic Capabilities][research_teece_2007]
- [Teece 2018 Profiting from Innovation in the Digital Economy][research_teece_2018]
- [Teece Pisano and Shuen 1997 Dynamic Capabilities and Strategic Management][research_teece_pisano_shuen_1997]
- [Tversky and Kahneman 1992 Advances in Prospect Theory][research_tversky_kahneman_1992]
-
- [Weiss and Thurbon 2021 Developmental State or Economic Statecraft][research_weiss_thurbon_2021]
- [Wernerfelt 1984 A Resource-Based View of the Firm][research_wernerfelt_1984]
- [Williamson 1975 Markets and Hierarchies][research_williamson_1975]
- [Winter 2003 Understanding Dynamic Capabilities][research_winter_2003]

### Related Post

- [A90 Introduction to Space Studies][related_post_a90_intro_space_studies]
- [A96 History of Rocketplanes][related_post_a96_history_rocketplanes]
- [A97 What Does the United States Space Force Do][related_post_a97_us_space_force]
- [A161 What a Patent Is and Is Not][related_post_a161_patent_intro]
- [A164 Patents Trade Secrets and the Disclosure Tradeoff][related_post_a164_patents_trade_secrets]
- [A167 Why Startups Actually Fail][related_post_a167_startup_failure]
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

[book_abbott_1988]: https://openlibrary.org/search?q=Abbott+The+System+of+Professions
[book_acemoglu_robinson_2012]: https://openlibrary.org/search?q=Acemoglu+and+Robinson+Why+Nations+Fail
[book_amsden_1989]: https://global.oup.com/academic/product/asias-next-giant-9780195076035
[book_beinhocker_2006]: https://www.hbsp.harvard.edu/product/5062-HBK-ENG
[book_berger_2021]: https://www.harpercollins.com/products/liftoff-eric-berger
[book_berger_2024]: https://openlibrary.org/search?q=Berger+Reentry+SpaceX
[book_berle_means_1932]: https://www.routledge.com/The-Modern-Corporation-and-Private-Property/Berle-Means/p/book/9780887388873
[book_bilby_1986]: https://openlibrary.org/search?q=Bilby+General+Sarnoff+RCA
[book_blank_2013]: https://openlibrary.org/search?q=Blank+Four+Steps+to+the+Epiphany
[book_bork_1978]: https://www.hup.harvard.edu/books/9780674032545
[book_buchanan_tullock_1962]: https://www.libertyfund.org/books/the-calculus-of-consent/
[book_chandler_1962]: https://mitpress.mit.edu/9780262530095/strategy-and-structure/
[book_chandler_1977]: https://www.hup.harvard.edu/books/9780674940529
[book_chandler_1990]: https://openlibrary.org/search?q=Chandler+Scale+and+Scope
[book_chang_2002]: https://www.penguin.co.uk/books/56082/kicking-away-the-ladder/9780857281050
[book_chernow_2004]: https://openlibrary.org/search?q=Chernow+Titan
[book_copeland_antikarov_2001]: https://openlibrary.org/search?q=Copeland+and+Antikarov+Real+Options+A+Practitioners+Guide
[book_creswell_2014]: https://us.sagepub.com/en-us/nam/research-design/book255675
[book_cusumano_gawer_2002]: https://www.hbsp.harvard.edu/product/6155-HBK-ENG
[book_davenport_2018]: https://www.hachettebookgroup.com/titles/christian-davenport/the-space-barons/9781610398299/
[book_dixit_pindyck_1994]: https://openlibrary.org/search?q=Dixit+and+Pindyck+Investment+Under+Uncertainty
[book_easterbrook_fischel_1991]: https://www.hup.harvard.edu/books/9780674235397
[book_evans_1995]: https://press.princeton.edu/books/paperback/9780691037363/embedded-autonomy
[book_fernholz_2018]: https://www.hachettebookgroup.com/titles/tim-fernholz/rocket-billionaires/9781328662231/
[book_fligstein_2001]: https://press.princeton.edu/books/paperback/9780691102542/the-architecture-of-markets
[book_ford_crowther_1922]: https://openlibrary.org/search?q=Ford+My+Life+and+Work
[book_foster_mcchesney_2011]: https://monthlyreview.org/product/endless_crisis/
[book_freeman_1987]: https://openlibrary.org/search?q=Freeman+Technology+Policy+and+Economic+Performance
[book_gertner_2012]: https://www.penguinrandomhouse.com/books/206061/the-idea-factory-by-jon-gertner/
[book_gompers_lerner_2001]: https://www.hbsp.harvard.edu/product/2434-HBK-ENG
[book_grief_2006]: https://www.cambridge.org/9780521671347
[book_grimsey_lewis_2004]: https://www.e-elgar.com/shop/gbp/public-private-partnerships-9781840647112.html
[book_handberg_1994]: https://openlibrary.org/search?q=Handberg+Reinventing+NASA
[book_hansmann_1996]: https://www.hup.harvard.edu/books/9780674001718
[book_hargrove_1994]: https://openlibrary.org/search?q=Hargrove+Prisoners+of+Myth
[book_hart_1995]: https://global.oup.com/academic/product/firms-contracts-and-financial-structure-9780198288817
[book_hartley_2017]: https://openlibrary.org/search?q=Hartley+The+Economics+of+Arms
[book_hiltzik_1999]: https://openlibrary.org/search?q=Hiltzik+Dealers+of+Lightning
[book_ho_2009]: https://www.dukeupress.edu/liquidated
[book_hounshell_1984]: https://jhupbooks.press.jhu.edu/title/american-system-mass-production-1800-1932
[book_hovenkamp_2005]: https://openlibrary.org/search?q=Hovenkamp+The+Antitrust+Enterprise
[book_isaacson_2011]: https://www.simonandschuster.com/books/Steve-Jobs/Walter-Isaacson/9781451648539
[book_isaacson_2023]: https://www.simonandschuster.com/books/Elon-Musk/Walter-Isaacson/9781982181284
[book_johnson_1982]: https://www.sup.org/books/title/?id=2143
[book_kahneman_2011]: https://us.macmillan.com/books/9780374533557/thinkingfastandslow
[book_kauffman_1993]: https://global.oup.com/academic/product/the-origins-of-order-9780195079517
[book_kearns_nadler_1992]: https://openlibrary.org/search?q=Kearns+Nadler+Prophets+Dark
[book_kenney_2000]: https://www.sup.org/books/title/?id=1354
[book_klepper_2016]: https://press.princeton.edu/books/hardcover/9780691169620/experimental-capitalism
[book_krippner_2011]: https://www.hup.harvard.edu/books/9780674066199
[book_kuhn_1962]: https://press.uchicago.edu/ucp/books/book/chicago/S/bo13179781.html
[book_kunda_1992]: https://openlibrary.org/search?q=Kunda+Engineering+Culture
[book_laffont_tirole_1993]: https://mitpress.mit.edu/9780262121743/a-theory-of-incentives-in-procurement-and-regulation/
[book_larson_1977]: https://www.ucpress.edu/book/9780520039070/the-rise-of-professionalism
[book_latour_1987]: https://www.hup.harvard.edu/books/9780674792913
[book_lecuyer_2006]: https://mitpress.mit.edu/9780262622110/making-silicon-valley/
[book_lerner_2009]: https://press.princeton.edu/books/hardcover/9780691142197/boulevard-of-broken-dreams
[book_levin_2010]: https://openlibrary.org/search?q=Levin+Wires+That+Bind
[book_lundvall_1992]: https://openlibrary.org/search?q=Lundvall+National+Systems+of+Innovation
[book_mackenzie_2006]: https://mitpress.mit.edu/9780262633673/an-engine-not-a-camera/
[book_malone_2014]: https://openlibrary.org/search?q=Malone+The+Intel+Trinity
[book_mazzucato_2013]: https://marianamazzucato.com/books/the-entrepreneurial-state
[book_mazzucato_2021]: https://marianamazzucato.com/books/mission-economy/
[book_mcafee_mcmillan_1988]: https://openlibrary.org/search?q=McAfee+and+McMillan+Incentives+in+Government+Contracting
[book_mccurdy_1994]: https://jhupbooks.press.jhu.edu/title/inside-nasa
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
[book_norberg_oneill_1996]: https://jhupbooks.press.jhu.edu/title/transforming-computer-technology
[book_north_1990]: https://www.cambridge.org/9780521397346
[book_ormerod_2005]: https://us.macmillan.com/books/9780375421099/whymostthingsfail
[book_osborne_2000]: https://www.routledge.com/Public-Private-Partnerships/Osborne/p/book/9780415225236
[book_osborne_rubinstein_1990]: https://www.sciencedirect.com/book/9780125286329/bargaining-and-markets
[book_ostrom_1990]: https://www.cambridge.org/9780521405997
[book_penrose_1959]: https://global.oup.com/academic/product/the-theory-of-the-growth-of-the-firm-9780199573844
[book_perez_2002]: https://openlibrary.org/search?q=Perez+Technological+Revolutions+and+Financial+Capital
[book_posner_2001]: https://openlibrary.org/search?q=Posner+Antitrust+Law
[book_preda_2009]: https://openlibrary.org/search?q=Preda+Framing+Finance
[book_pugh_1995]: https://mitpress.mit.edu/9780262161473/building-ibm/
[book_pugh_johnson_palmer_1991]: https://mitpress.mit.edu/9780262161237/ibms-360-and-early-370-systems/
[book_ries_2011]: https://www.crownpublishing.com/archives/feature/lean-startup
[book_robins_2006]: https://openlibrary.org/search?q=Robins+The+Corporation+That+Changed+the+World
[book_roe_1994]: https://press.princeton.edu/books/paperback/9780691026312/strong-managers-weak-owners
[book_ruttan_2006]: https://global.oup.com/academic/product/is-war-necessary-for-economic-growth-9780195188042
[book_saxenian_1994]: https://www.hup.harvard.edu/books/9780674753402
[book_schroeder_2008]: https://openlibrary.org/search?q=Schroeder+The+Snowball+Warren+Buffett+and+the+Business+of+Life
[book_schumpeter_1942]: https://www.harpercollins.com/products/capitalism-socialism-and-democracy-joseph-a-schumpeter
[book_selznick_1949]: https://www.ucpress.edu/book/9780520000384/tva-and-the-grass-roots
[book_smith_alexander_1988]: https://openlibrary.org/search?q=Smith+Alexander+Fumbling+the+Future
[book_srnicek_2017]: https://www.wiley.com/en-us/Platform+Capitalism-p-9781509504879
[book_steensgaard_1974]: https://openlibrary.org/search?q=Steensgaard+The+Asian+Trade+Revolution+of+the+Seventeenth+Century
[book_stern_2011]: https://global.oup.com/academic/product/the-company-state-9780195393736
[book_stone_2013]: https://www.hachettebookgroup.com/titles/brad-stone/the-everything-store/9780316219259/
[book_temin_galambos_1987]: https://openlibrary.org/search?q=Temin+Galambos+Fall+Bell+System
[book_thiel_2014]: https://www.penguinrandomhouse.com/books/226845/zero-to-one-by-peter-thiel-with-blake-masters/
[book_tirole_2006]: https://press.princeton.edu/books/hardcover/9780691125565/the-theory-of-corporate-finance
[book_trigeorgis_1996]: https://mitpress.mit.edu/9780262201025/real-options/
[book_vanalstyne_parker_choudary_2016]: https://wwnorton.com/books/Platform-Revolution/
[book_vance_2015]: https://www.harpercollins.com/products/elon-musk-ashlee-vance
[book_wade_1990]: https://press.princeton.edu/books/paperback/9780691117294/governing-the-market
[book_weiss_2014]: https://www.cornellpress.cornell.edu/book/9780801479922/america-inc/
[book_williamson_1985]: https://www.simonandschuster.com/books/The-Economic-Institutions-of-Capitalism/Oliver-E-Williamson/9780684863740
[book_woo_cumings_1999]: https://www.cornellpress.cornell.edu/book/9780801485664/the-developmental-state/
[book_wu_2010]: https://openlibrary.org/search?q=Wu+The+Master+Switch
[book_yescombe_2007]: https://www.sciencedirect.com/book/9780750680547/public-private-partnerships
[book_yin_2014]: https://us.sagepub.com/en-us/nam/case-study-research-and-applications/book250150
[book_zaloom_2006]: https://openlibrary.org/search?q=Zaloom+Out+of+the+Pits
[book_zuboff_2019]: https://www.hachettebookgroup.com/titles/shoshana-zuboff/the-age-of-surveillance-capitalism/9781610395694/
[ref_alphabet_ir]: https://abc.xyz/investor/
[ref_anthropic_ltbt]: https://www.anthropic.com/news/the-long-term-benefit-trust
[ref_arstechnica_space]: https://arstechnica.com/science/space/
[ref_berkshire]: https://www.berkshirehathaway.com/
[ref_bloomberg]: https://www.bloomberg.com/
[ref_blue_origin_press]: https://www.blueorigin.com/news/
[ref_bosch_annual_report]: https://www.bosch.com/company/annual-report/
[ref_bosch_company]: https://www.bosch.com/company/
[ref_bosch_stiftung]: https://www.bosch-stiftung.de/en
[ref_carl_zeiss_stiftung]: https://www.carl-zeiss-stiftung.de/en/
[ref_cii]: https://www.cii.org/
[ref_cii_dual_class]: https://www.cii.org/dualclass_stock
[ref_columbia_blue_sky]: https://clsbluesky.law.columbia.edu/
[ref_conference_board]: https://www.conference-board.org/
[ref_danish_business_authority]: https://danishbusinessauthority.dk/
[ref_delaware_chancery]: https://courts.delaware.gov/chancery/
[ref_delaware_division_corporations]: https://corp.delaware.gov/
[ref_delaware_opinions]: https://courts.delaware.gov/opinions/
[ref_dgcl]: https://delcode.delaware.gov/title8/c001/
[ref_dgcl_sc01]: https://delcode.delaware.gov/title8/c001/sc01/index.html
[ref_dgcl_sc04]: https://delcode.delaware.gov/title8/c001/sc04/index.html
[ref_dgcl_sc05]: https://delcode.delaware.gov/title8/c001/sc05/index.html
[ref_dgcl_sc07]: https://delcode.delaware.gov/title8/c001/sc07/index.html
[ref_dodd_frank_2010]: https://www.congress.gov/111/plaws/publ203/PLAW-111publ203.pdf
[ref_ecgi]: https://www.ecgi.global/
[ref_eu_shareholder_rights_directive]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32017L0828
[ref_exchange_act_12g]: https://www.law.cornell.edu/uscode/text/15/78l
[ref_ford_ir]: https://shareholder.ford.com/
[ref_ftse_russell]: https://www.lseg.com/en/ftse-russell
[ref_german_aktiengesetz]: https://www.gesetze-im-internet.de/aktg/
[ref_glass_lewis]: https://www.glasslewis.com/
[ref_harvard_corpgov_forum]: https://corpgov.law.harvard.edu/
[ref_ibm_archives]: https://www.ibm.com/history/
[ref_iss_governance]: https://www.issgovernance.com/
[ref_jobs_act_2012]: https://www.congress.gov/112/plaws/publ106/PLAW-112publ106.pdf
[ref_meta_ir]: https://investor.atmeta.com/
[ref_microsoft_news]: https://news.microsoft.com/
[ref_nasdaq_listing_rules]: https://listingcenter.nasdaq.com/rulebook/nasdaq/rules
[ref_nber]: https://www.nber.org/
[ref_novo_holdings]: https://www.novoholdings.dk/
[ref_novo_nordisk_foundation]: https://novonordiskfonden.dk/en/
[ref_novo_nordisk_investors]: https://www.novonordisk.com/investors.html
[ref_nyse_listed_company_manual]: https://nyseguide.srorules.com/listed-company-manual
[ref_nyt]: https://www.nytimes.com/section/science/space
[ref_oecd_corporate_governance]: https://www.oecd.org/corporate/principles-corporate-governance/
[ref_openai_charter]: https://openai.com/charter/
[ref_openai_news]: https://openai.com/news/
[ref_payload]: https://payloadspace.com/
[ref_payload_research]: https://payloadspace.com/research/
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
[ref_securities_act_4a2]: https://www.law.cornell.edu/uscode/text/15/77d
[ref_snap_ir]: https://investor.snap.com/
[ref_spacenews]: https://spacenews.com/
[ref_spacex_company]: https://www.spacex.com/
[ref_spacex_news_archive]: https://www.spacex.com/updates/
[ref_spdji]: https://www.spglobal.com/spdji/en/
[ref_ssrn]: https://www.ssrn.com/
[ref_tesla_ir]: https://ir.tesla.com/
[ref_texas_boc]: https://statutes.capitol.texas.gov/Docs/BO/htm/BO.21.htm
[ref_texas_sos]: https://www.sos.state.tx.us/
[ref_uk_companies_act_2006]: https://www.legislation.gov.uk/ukpga/2006/46/contents
[ref_ula_press]: https://www.ulalaunch.com/about/news
[ref_washington_post]: https://www.washingtonpost.com/business/technology/
[ref_wsj]: https://www.wsj.com/tech
[ref_zeiss_corporate]: https://www.zeiss.com/corporate/en/home.html
[related_post_a161_patent_intro]: {% post_url 2026-05-03-what_a_patent_is_and_is_not %}
[related_post_a164_patents_trade_secrets]: {% post_url 2026-05-06-patents_trade_secrets_and_the_disclosure_tradeoff %}
[related_post_a167_startup_failure]: {% post_url 2026-05-09-why_startups_actually_fail %}
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
[related_post_a90_intro_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[related_post_a96_history_rocketplanes]: {% post_url 2026-02-27-history_of_rocketplanes %}
[related_post_a97_us_space_force]: {% post_url 2026-02-28-what_does_united_states_space_force_do %}
[research_armstrong_2006]: https://onlinelibrary.wiley.com/doi/10.1111/j.1756-2171.2006.tb00037.x
[research_arthur_1989]: https://www.jstor.org/stable/2234208
[research_bajari_mcmillan_tadelis_2009]: https://academic.oup.com/jleo/article-abstract/25/2/372/845776
[research_bajari_tadelis_2001]: https://www.jstor.org/stable/2696367
[research_barney_1991]: https://journals.sagepub.com/doi/10.1177/014920639101700108
[research_bebchuk_kastiel_2017]: https://www.virginialawreview.org/articles/untenable-case-perpetual-dual-class-stock/
[research_bebchuk_kraakman_triantis_2000]: https://www.nber.org/chapters/c9013
[research_binmore_rubinstein_wolinsky_1986]: https://www.jstor.org/stable/2555382
[research_black_scholes_1973]: https://www.jstor.org/stable/1831029
[research_block_2008]: https://doi.org/10.1177/0032329208318731
[research_bonvillian_2018]: https://mitpress.mit.edu/9780262038522/the-darpa-model-for-transformative-technologies/
[research_bovaird_2004]: https://doi.org/10.1177/0020852304044250
[research_callon_1986]: https://onlinelibrary.wiley.com/doi/10.1111/j.1467-954X.1984.tb00113.x
[research_che_chung_1999]: https://academic.oup.com/rand/article-abstract/30/1/97/2701540
[research_coase_1937]: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-0335.1937.tb00002.x
[research_corts_singh_2004]: https://academic.oup.com/jleo/article-abstract/20/1/230/970131
[research_david_1985]: https://www.jstor.org/stable/1805621
[research_deangelo_deangelo_1985]: https://www.sciencedirect.com/science/article/abs/pii/0304405X85900436
[research_eisenhardt_martin_2000]: https://onlinelibrary.wiley.com/doi/10.1002/1097-0266%28200010/11%2921%3A10/11%3C1105%3A%3AAID-SMJ133%3E3.0.CO%3B2-E
[research_eisenmann_et_al_2006]: https://hbr.org/2006/10/strategies-for-two-sided-markets
[research_ewens_farre_mensa_2020]: https://academic.oup.com/rfs/article-abstract/33/12/5463/5866533
[research_fama_jensen_1983]: https://www.jstor.org/stable/725104
[research_finkelstein_sanford_2000]: https://doi.org/10.1016/S0090-2616(00)00020-6
[research_gagnepain_ivaldi_2002]: https://academic.oup.com/rand/article-abstract/33/4/605/2603099
[research_gawer_cusumano_2014]: https://onlinelibrary.wiley.com/doi/10.1111/jpim.12105
[research_gompers_1995]: https://www.jstor.org/stable/2329227
[research_gompers_ishii_metrick_2003]: https://academic.oup.com/qje/article/118/1/107/1917017
[research_gompers_ishii_metrick_2010]: https://academic.oup.com/rfs/article/23/3/1051/1568225
[research_grossman_hart_1986]: https://www.jstor.org/stable/1833199
[research_grossman_hart_1988]: https://www.sciencedirect.com/science/article/abs/pii/0304405X88900443
[research_hagiu_wright_2015]: https://www.sciencedirect.com/science/article/pii/S0167718715000156
[research_hall_lerner_2010]: https://www.sciencedirect.com/science/article/pii/S0169721810010142
[research_harris_raviv_1988]: https://www.sciencedirect.com/science/article/abs/pii/0304405X88900455
[research_hart_moore_1990]: https://www.jstor.org/stable/2937861
[research_helfat_peteraf_2003]: https://onlinelibrary.wiley.com/doi/10.1002/smj.332
[research_hodge_greve_2007]: https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6210.2007.00736.x
[research_jensen_1986]: https://www.jstor.org/stable/1818789
[research_jensen_meckling_1976]: https://www.sciencedirect.com/science/article/pii/0304405X7690026X
[research_kahneman_tversky_1979]: https://www.jstor.org/stable/1914185
[research_kalnins_mayer_2004]: https://doi.org/10.1093/jleo/ewh030
[research_kaplan_stromberg_2003]: https://academic.oup.com/restud/article-abstract/70/2/281/1571073
[research_kaplan_stromberg_2004]: https://academic.oup.com/rfs/article-abstract/17/1/1/1601330
[research_khan_2017]: https://www.yalelawjournal.org/note/amazons-antitrust-paradox
[research_klepper_1996]: https://www.jstor.org/stable/2118211
[research_klepper_2010]: https://academic.oup.com/icc/article/19/1/135/731929
[research_kogut_kulatilaka_1994]: https://pubsonline.informs.org/doi/10.1287/mnsc.40.1.123
[research_kortum_lerner_2000]: https://www.rand.org/pubs/reprints/RP924.html
[research_krueger_1974]: https://www.jstor.org/stable/1808883
[research_laporta_et_al_1998]: https://www.journals.uchicago.edu/doi/10.1086/250042
[research_law_1987]: https://mitpress.mit.edu/9780262521376/the-social-construction-of-technological-systems/
[research_lerner_1994_syndication]: https://www.jstor.org/stable/3665602
[research_levin_tadelis_2010]: https://academic.oup.com/qje/article-abstract/125/3/1103/1903637
[research_manne_1965]: https://www.journals.uchicago.edu/doi/10.1086/259036
[research_mcdonald_siegel_1986]: https://academic.oup.com/qje/article-abstract/101/4/707/1885353
[research_merton_1973]: https://www.jstor.org/stable/3003143
[research_myers_1977]: https://www.sciencedirect.com/science/article/abs/pii/0304405X77900150
[research_myerson_1981]: https://pubsonline.informs.org/doi/10.1287/moor.6.1.58
[research_nash_1950]: https://www.jstor.org/stable/1907266
[research_parker_vanalstyne_2005]: https://pubsonline.informs.org/doi/10.1287/mnsc.1050.0400
[research_peteraf_1993]: https://onlinelibrary.wiley.com/doi/10.1002/smj.4250140303
[research_rochet_tirole_2003]: https://www.jstor.org/stable/40007911
[research_rochet_tirole_2006]: https://onlinelibrary.wiley.com/doi/10.1111/j.1756-2171.2006.tb00036.x
[research_ross_staw_1993]: https://doi.org/10.2307/256756
[research_rubinstein_1982]: https://www.jstor.org/stable/1912531
[research_rysman_2009]: https://www.aeaweb.org/articles?id=10.1257/jep.23.3.125
[research_sahlman_1990]: https://www.sciencedirect.com/science/article/pii/0304405X9090065E
[research_shleifer_vishny_1997]: https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1997.tb04820.x
[research_staw_1976]: https://www.sciencedirect.com/science/article/abs/pii/003050737690005X
[research_stigler_1971]: https://www.jstor.org/stable/3003160
[research_teece_2007]: https://onlinelibrary.wiley.com/doi/10.1002/smj.640
[research_teece_2018]: https://www.sciencedirect.com/science/article/pii/S0048733317301993
[research_teece_pisano_shuen_1997]: https://onlinelibrary.wiley.com/doi/10.1002/%28SICI%291097-0266%28199708%2918%3A7%3C509%3A%3AAID-SMJ882%3E3.0.CO%3B2-Z
[research_tversky_kahneman_1992]: https://link.springer.com/article/10.1007/BF00122574
[research_weiss_thurbon_2021]: https://doi.org/10.1080/13563467.2020.1766431
[research_wernerfelt_1984]: https://onlinelibrary.wiley.com/doi/10.1002/smj.4250050207
[research_williamson_1975]: https://www.jstor.org/stable/40751236
[research_winter_2003]: https://onlinelibrary.wiley.com/doi/10.1002/smj.318
