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

This article is the seventh in the History of SpaceX series and treats the governance forcing-function condition that the [series opener][related_post_a281_spacex_framing] introduced as the sixth of seven forcing-function conditions in the seven-plus-three analytical framework. The governance condition requires that a mission-directed technology venture adopt a control configuration that permits the venture to raise the capital its mission requires without transferring to the capital providers the authority to redirect the mission. The condition is distinct from every other condition in the framework because it concerns not what the venture builds but who decides what the venture builds, and because it becomes binding precisely at the moments when the other conditions are being satisfied. A venture that raises no capital faces no capital-capture hazard, and a venture that raises the capital an insatiable mission demands faces the hazard in its most acute form. The article walks the SpaceX control trajectory through the specific 2002 founding capital structure, the specific dual-class share architecture, the specific sequence of more than thirty financing rounds across the specific 2002 through drafting-date period, the specific January 2015 Google and Fidelity round that introduced strategic investors at scale, the specific semi-annual tender-offer liquidity mechanism that substitutes for a public listing, the specific repeatedly deferred initial-public-offering decision, and the specific Starlink separation question that remains open at the drafting date. The article contrasts the SpaceX configuration against the specific OpenAI governance failure of November 2023, in which a control structure designed explicitly to resist capital capture was tested and defeated within five days, and against the specific Tesla compensation litigation that illustrates the limits of founder control under public-company conditions. The article draws on the corporate-governance literature from [Berle and Means 1932][book_berle_means_1932] The Modern Corporation and Private Property through [Jensen and Meckling 1976][research_jensen_meckling_1976], [Grossman and Hart 1988][research_grossman_hart_1988] One Share-One Vote and the Market for Corporate Control, [Shleifer and Vishny 1997][research_shleifer_vishny_1997] A Survey of Corporate Governance, and [Bebchuk and Kastiel 2017][research_bebchuk_kastiel_2017] The Untenable Case for Perpetual Dual-Class Stock, and on the foundation-ownership literature that [Hansmann 1996][book_hansmann_1996] The Ownership of Enterprise frames. The article treats the specific Carl Zeiss Stiftung of 1889, the specific Robert Bosch ownership separation, and the specific Novo Nordisk Foundation structure as the specific centurial precedents for a control configuration that has survived across multiple generations of capital formation. The article closes with an explicit pattern-extraction section stating the abstract governance mechanic in a form other informed readers can recognize in adjacent domains without naming any specific downstream application.

## The Governance Mapping Problem

The mapping problem for a comprehensive treatment of the governance condition in the SpaceX case is the question of which specific control instruments the specific firm adopted, how the specific instruments behaved across the specific sequence of financing events that the mission required, and whether the specific instruments in fact prevented a specific redirection of the mission that would otherwise have occurred. The third element is the difficult one. A control configuration that is never tested supplies no evidence that it works, and the specific counterfactual in which the specific capital providers attempt a redirection and fail is not directly observable for a firm in which the specific attempt was never made.

The problem admits several formalizations depending on the analytical tradition consulted. The agency tradition from [Berle and Means 1932][book_berle_means_1932] through [Jensen and Meckling 1976][research_jensen_meckling_1976] Theory of the Firm and [Fama and Jensen 1983][research_fama_jensen_1983] Separation of Ownership and Control treats the governance property as the specific alignment configuration between the specific manager and the specific residual claimants, and treats founder control as a specific agency problem rather than as a specific solution. The incomplete-contracts tradition from [Grossman and Hart 1986][research_grossman_hart_1986] The Costs and Benefits of Ownership and [Hart and Moore 1990][research_hart_moore_1990] Property Rights and the Nature of the Firm through [Hart 1995][book_hart_1995] Firms Contracts and Financial Structure treats the governance property as the specific allocation of residual control rights over decisions that the specific financing contracts do not specify. The security-benefits tradition from [Grossman and Hart 1988][research_grossman_hart_1988] and [Harris and Raviv 1988][research_harris_raviv_1988] Corporate Governance Voting Rights and Majority Rules treats the specific one-share-one-vote configuration as the arrangement that maximizes the specific security benefits and treats every specific deviation as a transfer toward the specific private benefits of control. The law-and-finance tradition from [La Porta Lopez-de-Silanes Shleifer and Vishny 1998][research_laporta_et_al_1998] Law and Finance treats the governance property as a specific function of the specific legal regime within which the specific firm incorporates. The present article draws on all four traditions while adopting the mission-oriented-innovation framework the [series opener][related_post_a281_spacex_framing] established as the primary organizing structure, and it departs from the agency tradition on the specific question of whose objective function is normative.

The general form of the governance mapping problem can be stated compactly. Let $e_i(t)$ denote the specific cash-flow share of the specific claimant $i$ at time $t$, and let $v_i(t)$ denote the specific voting share of the specific claimant $i$ at time $t$. The specific control wedge admits the compact form

$$w_i(t) = \frac{v_i(t)}{e_i(t)}$$

with $w_i = 1$ under the specific one-share-one-vote configuration, $w_i > 1$ for a specific claimant whose voting rights exceed the specific economic exposure, and $w_i < 1$ for a specific claimant in the specific complementary position. The specific governance condition the article treats requires that the specific founder wedge be sufficiently large that the specific control condition

$$v^{\text{founder}}(t) > \tfrac{1}{2} \qquad \forall t \in [t_0, T]$$

holds across the specific entire financing horizon, and not merely at the specific founding.

The specific difficulty the condition addresses is that the specific cash-flow share declines mechanically with each specific financing round. Let $\delta_n$ denote the specific dilution fraction of the specific round $n$. The specific cash-flow share follows the specific recursion

$$e^{\text{founder}}_n = e^{\text{founder}}_{n-1} \left( 1 - \delta_n \right) \qquad \text{so} \qquad e^{\text{founder}}_N = e^{\text{founder}}_0 \prod_{n=1}^{N} \left( 1 - \delta_n \right)$$

with the specific product declining monotonically in the specific round count. Under a specific one-share-one-vote configuration the specific voting share follows the specific identical recursion, and the specific control condition therefore fails at a specific finite round count determined by the specific initial share and the specific per-round dilution. Under a specific dual-class configuration in which the specific issued shares carry inferior voting rights, the specific voting recursion decouples from the specific cash-flow recursion, and the specific control condition can hold for arbitrarily large $N$.

The specific decoupling admits the compact statement

$$\frac{\partial v^{\text{founder}}}{\partial \delta_n} \approx 0 \qquad \text{while} \qquad \frac{\partial e^{\text{founder}}}{\partial \delta_n} < 0$$

with the specific voting share substantially insensitive to the specific dilution that the specific cash-flow share absorbs. The specific decoupling is the specific whole of the technical content of the dual-class instrument, and the specific remainder of the analytical question concerns what the specific decoupling is used for.

The specific capital-capture event that the condition is designed to prevent admits definition as a specific change in the specific mission objective attributable to the specific preferences of the specific capital providers. Let $M(t)$ denote the specific mission objective and let $\mathcal{F}_t$ denote the specific information available at time $t$. The specific capture indicator admits the compact form

$$\kappa(t) = \mathbb{1}\!\left[ M(t) \neq M(t^-) \; \wedge \; \Delta M \in \arg\max_{M'} \sum_{i \neq \text{founder}} e_i \cdot U_i(M') \right]$$

taking the specific value unity when the specific mission changes and the specific change moves toward the specific capital-weighted preference of the specific non-founder claimants. The specific SpaceX record exhibits $\kappa(t) = 0$ across the specific observed period, which is the specific empirical claim the article defends and the specific claim whose interpretation is contested, because an unchanged mission is equally consistent with a specific effective control configuration and with a specific absence of any capital provider who wished to change it.

The specific identification problem is therefore acute. The specific counterfactual differential admits the compact form

$$\Delta V^{\text{governance}}_i(t) = V^{\text{observed}}_i(t) - V^{\text{capture counterfactual}}_i(t)$$

with the specific attribution equal to the difference between the specific observed trajectory and the specific counterfactual trajectory under a specific one-share-one-vote configuration facing the specific identical financing sequence. The specific counterfactual specifications the article treats include a specific investor-controlled counterfactual in which the specific board redirects the venture toward the specific near-term commercial opportunity, a specific acquisition counterfactual in which the specific venture is sold to a specific incumbent, and a specific public-market counterfactual in which the specific quarterly reporting cycle constrains the specific investment horizon.

## Methodological Commitments

The article commits to the same seven methodological positions that the [series opener][related_post_a281_spacex_framing] established for the series as a whole. These commitments are restated here at compact reference level, with specific attention to the ways the governance material strains them.

The first commitment is descriptive-analytical framing rather than prescriptive advocacy. The commitment is harder to honor in the governance material than elsewhere in the series, because the corporate-governance literature is substantially normative and because the specific dual-class instrument the article describes is the subject of an active policy dispute. The article describes what the specific instrument did in the specific case and declines to recommend it.

The second commitment is dual-register composition with both general-history and abstract-mechanic registers.

The third commitment is primary-source anchoring. The article cites primary sources for each substantive claim with preference for the specific [Delaware General Corporation Law][ref_dgcl] provisions that authorize the specific instruments, the specific [Texas Business Organizations Code][ref_texas_boc] provisions relevant to the specific reported reincorporation, the specific [Delaware Court of Chancery][ref_delaware_chancery] record, the specific [Securities and Exchange Commission EDGAR][ref_sec_edgar] filings and the specific [Form D exempt-offering][ref_sec_form_d] regime under which the specific private rounds were conducted, the specific [Securities Act private-placement exemption][ref_securities_act_4a2] and the specific [Regulation D][ref_reg_d] rules that authorize them, the specific [Exchange Act registration-threshold provision][ref_exchange_act_12g] that determines when a specific private issuer becomes a specific reporting company, the specific [Delaware Division of Corporations][ref_delaware_division_corporations] and [Texas Secretary of State][ref_texas_sos] filing systems, the specific [SEC investor-education materials][ref_sec_investor_gov], the specific [SpaceX news archive][ref_spacex_news_archive], the specific [OpenAI charter][ref_openai_charter] and [OpenAI announcements][ref_openai_news], the specific [Carl Zeiss Stiftung][ref_carl_zeiss_stiftung] documentation, the specific [Robert Bosch Stiftung][ref_bosch_stiftung] and [Bosch corporate][ref_bosch_company] documentation, and the specific [Novo Nordisk Foundation][ref_novo_nordisk_foundation] and [Novo Holdings][ref_novo_holdings] documentation. The article draws on secondary sources including [Berger 2021][book_berger_2021] Liftoff, [Berger 2024][book_berger_2024] Reentry, [Vance 2015][book_vance_2015] Elon Musk, [Isaacson 2023][book_isaacson_2023] Elon Musk, [Davenport 2018][book_davenport_2018] The Space Barons, and [Fernholz 2018][book_fernholz_2018] Rocket Billionaires.

The fourth commitment is contested-claim marking. The commitment binds more heavily in this article than in any other in the series. The specific SpaceX ownership percentages, the specific voting percentages, the specific round valuations, and the specific share-class terms are not disclosed by the specific firm and are reconstructed from specific trade-press reporting, specific state-level filings, and specific investor communications that reach the public record indirectly. Every specific numerical claim about the specific capital structure in this article is a reconstructive estimate and is marked as such.

The fifth commitment is temporal indexing as a mid-2026 snapshot. The specific governance material is more perishable than the specific technical material treated elsewhere in the series, because a specific single financing event or a specific single legal decision can alter the specific configuration.

The sixth commitment is terminological transparency with the Terminological Note section below. The specific governance vocabulary is unusually contested, and specific terms including control, ownership, and independence carry specific different meanings across the specific legal, financial-economic, and organizational literatures.

The seventh commitment is thesis-not-proof framing of the governance closure claim. The specific claim that the specific control configuration prevented a specific capture that would otherwise have occurred is not demonstrable from the specific available record and is advanced as an interpretation consistent with the record.

## Governance as an Economic Property

The governance property is treated in the article as a specific economic property of a firm's control allocation that distinguishes ventures able to sustain a specific mission objective across a specific extended financing sequence from ventures whose objective is reset by the specific preferences of whichever capital providers hold the specific decisive claim at each specific stage. The property admits formal characterization, measurement, and comparison across firms and legal regimes.

The specific formal characterization begins from the specific separation of the specific two rights that a specific share ordinarily bundles. The specific cash-flow right entitles the holder to a specific fraction of the specific residual, and the specific control right entitles the holder to a specific fraction of the specific decision authority. The specific aggregate identities are

$$\sum_i e_i = 1 \qquad \text{and} \qquad \sum_i v_i = 1$$

with the specific two distributions coinciding under one-share-one-vote and diverging under every specific deviation from it. The specific aggregate wedge across the specific claimant set admits the compact form

$$W = \sum_i \left| v_i - e_i \right|$$

taking the specific value zero under one-share-one-vote and increasing in the specific degree of separation. The specific measure is symmetric across claimants and therefore does not by itself indicate who holds the specific excess control.

The specific security-benefits argument that [Grossman and Hart 1988][research_grossman_hart_1988] and [Harris and Raviv 1988][research_harris_raviv_1988] develop holds that the specific one-share-one-vote configuration is optimal because it aligns the specific decision authority with the specific economic exposure and thereby causes the specific controlling party to internalize the specific consequences of the specific decisions. The specific argument admits statement as the specific condition under which a specific controller approves a specific project

$$e^{\text{controller}} \cdot \Delta V^{\text{security}} + \Delta B^{\text{private}} > 0$$

with $\Delta V^{\text{security}}$ the specific change in the specific total security value and $\Delta B^{\text{private}}$ the specific change in the specific private benefits accruing to the specific controller alone. Under one-share-one-vote with a specific majority holder the specific first term dominates and the specific controller approves substantially the specific value-increasing projects. As $e^{\text{controller}}$ falls while $v^{\text{controller}}$ is held fixed, the specific first term shrinks and the specific private-benefit term becomes decisive at a specific threshold

$$e^{\text{controller}} < \frac{-\Delta B^{\text{private}}}{\Delta V^{\text{security}}}$$

below which the specific controller rejects specific value-increasing projects that reduce the specific private benefits and approves specific value-decreasing projects that increase them. The specific inequality is the specific formal core of the case against dual-class structures, and the specific SpaceX configuration sits deep inside the region the inequality identifies as hazardous.

The specific counterargument the article develops does not deny the specific inequality. The specific counterargument holds that the specific quantity the specific inequality labels a private benefit is in the specific mission-directed case the specific object the specific venture exists to pursue, and that the specific security value against which it is compared is measured over a specific horizon shorter than the specific mission horizon. Let $\rho^{\text{controller}}$ and $\rho^{\text{investor}}$ denote the specific discount rates the specific two parties apply. The specific horizon divergence admits the compact form

$$\rho^{\text{controller}} < \rho^{\text{investor}} \implies \exists \; \text{projects with} \; \text{NPV}_{\rho^{\text{controller}}} > 0 > \text{NPV}_{\rho^{\text{investor}}}$$

with a specific nonempty set of projects that the specific controller values positively and the specific diversified investor values negatively. The specific reusability development that the [Value Gradient article A282][related_post_a282_spacex_value_gradient] treats and the specific Starship development that the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats both occupy that specific set across substantial portions of their specific development periods.

The specific mission-persistence probability admits the compact form

$$P^{\text{persistence}}(T) = \prod_{n=1}^{N(T)} \left[ 1 - q_n \right]$$

with $q_n$ the specific probability that the specific financing round $n$ produces a specific mission redirection. Under a specific one-share-one-vote configuration the specific hazard $q_n$ rises with the specific cumulative dilution, because the specific coalition required to redirect becomes progressively easier to assemble. Under a specific dual-class configuration the specific hazard remains substantially constant and near zero across rounds, and the specific persistence probability therefore does not decay with the specific financing intensity that an insatiable mission demands.

The specific control-contestability measure admits the compact form

$$C^{\text{contest}} = \min \left\{ \sum_{i \in S} v_i \; : \; S \subseteq \mathcal{I} \setminus \{\text{founder}\}, \; \sum_{i \in S} v_i > \tfrac{1}{2} \right\}$$

giving the specific smallest voting mass a specific coalition excluding the founder must assemble to prevail. The specific measure is infinite, in the sense that no specific such coalition exists, whenever the specific founder holds a specific majority of votes. The specific SpaceX configuration at the drafting date is reported to place the specific measure in that regime, and the specific OpenAI configuration of November 2023 placed it in a specific regime where the specific formal measure suggested contestability was impossible while the specific effective measure proved otherwise.

The specific distinction between the specific formal and the specific effective control measures is the specific analytical contribution the OpenAI counter-example supplies. The specific effective control admits the compact form

$$v^{\text{effective}}_i = f\!\left( v^{\text{formal}}_i, \; d_i, \; \sigma_i \right)$$

with $d_i$ the specific resource dependence of the specific organization on the specific party $i$ and $\sigma_i$ the specific credibility of the specific party's threat to withdraw. A specific party holding zero formal votes but supplying a specific resource without which the specific organization cannot operate holds a specific effective control that the specific formal measure does not register.

## Cross-Disciplinary Framings

The governance property admits characterization from several disciplinary traditions beyond the mission-oriented-innovation framework the series adopts as primary.

The agency tradition traces from [Berle and Means 1932][book_berle_means_1932] The Modern Corporation and Private Property through [Jensen and Meckling 1976][research_jensen_meckling_1976] Theory of the Firm Managerial Behavior Agency Costs and Ownership Structure, [Fama and Jensen 1983][research_fama_jensen_1983] Separation of Ownership and Control, [Jensen 1986][research_jensen_1986] Agency Costs of Free Cash Flow, and the specific survey in [Shleifer and Vishny 1997][research_shleifer_vishny_1997] A Survey of Corporate Governance. The framing treats the specific separation of ownership from control as the specific central problem of the modern corporation and treats the specific governance apparatus as the specific set of instruments that mitigate it. The specific agency cost admits the compact decomposition

$$AC = C^{\text{monitoring}} + C^{\text{bonding}} + L^{\text{residual}}$$

with the specific monitoring expenditure borne by the principal, the specific bonding expenditure borne by the agent, and the specific residual loss equal to the specific remaining divergence. The framing classifies the specific SpaceX configuration as one in which the specific monitoring and bonding instruments are substantially disabled by design, so that the specific residual-loss term carries the entire burden. The specific framing supplies the specific sharpest available statement of what the specific configuration risks.

The incomplete-contracts and property-rights tradition traces from [Coase 1937][research_coase_1937] The Nature of the Firm through [Williamson 1975][research_williamson_1975] Markets and Hierarchies, [Williamson 1985][book_williamson_1985] The Economic Institutions of Capitalism, [Grossman and Hart 1986][research_grossman_hart_1986], [Hart and Moore 1990][research_hart_moore_1990], and [Hart 1995][book_hart_1995] Firms Contracts and Financial Structure. The framing treats the specific control right as valuable precisely because the specific financing contracts cannot specify the specific actions to be taken in the specific contingencies that a specific long-horizon development program encounters. The specific residual-control allocation admits the compact form

$$\text{RC} = \left\{ a \in \mathcal{A} \; : \; a \notin \text{dom}(\text{contract}) \right\}$$

with the specific residual set comprising the specific actions the specific contract does not address. The framing supplies the specific most useful account of why a specific mission-directed venture values control disproportionately, because the specific mission is a statement about the specific behavior in specific unforeseen contingencies and is therefore precisely the specific object that a specific contract cannot secure.

The law-and-finance tradition traces from [La Porta Lopez-de-Silanes Shleifer and Vishny 1998][research_laporta_et_al_1998] Law and Finance through the specific comparative-governance literature and treats the specific control configuration as a specific function of the specific legal regime. The specific Delaware regime that the specific [Delaware General Corporation Law][ref_dgcl] establishes permits the specific issuance of multiple classes with specific differential voting rights substantially without constraint, and the specific permissiveness is a specific competitive product of the specific state-charter market that [Roe 1994][book_roe_1994] Strong Managers Weak Owners and [Easterbrook and Fischel 1991][book_easterbrook_fischel_1991] The Economic Structure of Corporate Law analyze from opposing positions. The specific investor-protection index the tradition constructs admits the compact form

$$IP_j = \sum_{k} \omega_k \cdot \mathbb{1}\!\left[ \text{protection } k \text{ present in regime } j \right]$$

with the specific weighted sum across the specific protection set. The specific United States regime scores highly on the specific index while permitting the specific dual-class deviation, which establishes that the specific index measures the specific protection of minority claimants against specific expropriation rather than the specific allocation of control as such. The specific comparative regimes differ materially. The specific [United Kingdom Companies Act 2006][ref_uk_companies_act_2006] and the specific listing regime built on it have historically constrained the specific instrument far more tightly, the specific German [Aktiengesetz][ref_german_aktiengesetz] restricts specific multiple-voting arrangements in specific ways the specific Delaware regime does not, and the specific [European Union Shareholder Rights Directive][ref_eu_shareholder_rights_directive] establishes a specific engagement framework with no specific Delaware analogue. The specific [OECD Principles of Corporate Governance][ref_oecd_corporate_governance] supply the specific international benchmark against which the specific regimes are compared.

The dual-class empirical tradition traces from [DeAngelo and DeAngelo 1985][research_deangelo_deangelo_1985] Managerial Ownership of Voting Rights through [Gompers Ishii and Metrick 2003][research_gompers_ishii_metrick_2003] Corporate Governance and Equity Prices, [Gompers Ishii and Metrick 2010][research_gompers_ishii_metrick_2010] Extreme Governance An Analysis of Dual-Class Firms in the United States, [Bebchuk Kraakman and Triantis 2000][research_bebchuk_kraakman_triantis_2000] Stock Pyramids Cross-Ownership and Dual Class Equity, and [Bebchuk and Kastiel 2017][research_bebchuk_kastiel_2017] The Untenable Case for Perpetual Dual-Class Stock. The framing supplies the specific empirical record against which the specific SpaceX configuration should be assessed. The specific central empirical finding is that the specific firm value declines in the specific wedge and that the specific decline steepens with the specific time elapsed since the specific initial public offering, which motivates the specific sunset provisions the specific policy literature recommends. The specific value relation admits the compact form

$$\frac{\partial q}{\partial w} < 0 \qquad \text{and} \qquad \frac{\partial^2 q}{\partial w \, \partial \tau} < 0$$

with $q$ a specific valuation ratio, $w$ the specific wedge, and $\tau$ the specific time since listing. The specific SpaceX case lies outside the specific estimation sample because the specific firm has never listed, and the specific applicability of the specific finding to an unlisted firm is precisely the specific question the article must address rather than assume.

The bargaining tradition traces from [Nash 1950][research_nash_1950] The Bargaining Problem through [Rubinstein 1982][research_rubinstein_1982] Perfect Equilibrium in a Bargaining Model, [Binmore Rubinstein and Wolinsky 1986][research_binmore_rubinstein_wolinsky_1986] The Nash Bargaining Solution in Economic Modelling, [Osborne and Rubinstein 1990][book_osborne_rubinstein_1990] Bargaining and Markets, and [Muthoo 1999][book_muthoo_1999] Bargaining Theory with Applications. The framing treats the specific control terms as the specific outcome of a specific negotiation between the specific founder and the specific investors whose specific outcome depends on the specific outside options each party holds. The specific split admits the compact form

$$\left( u^{\text{founder}}, u^{\text{investor}} \right) = \arg\max \left( u^{\text{founder}} - d^{\text{founder}} \right)^{\beta} \left( u^{\text{investor}} - d^{\text{investor}} \right)^{1-\beta}$$

with $d$ the specific disagreement payoffs and $\beta$ the specific relative bargaining power. The framing supplies the specific explanation for why the specific control terms tightened rather than loosened across the specific SpaceX financing sequence, because the specific founder disagreement payoff improved as the specific venture demonstrated capability while the specific investor disagreement payoff deteriorated as the specific competing investment opportunities in the specific sector failed to materialize.

The entrepreneurial-finance tradition traces from [Sahlman 1990][research_sahlman_1990] The Structure and Governance of Venture-Capital Organizations through [Gompers 1995][research_gompers_1995] Optimal Investment Monitoring and the Staging of Venture Capital, [Kaplan and Stromberg 2003][research_kaplan_stromberg_2003] Financial Contracting Theory Meets the Real World, [Kaplan and Stromberg 2004][research_kaplan_stromberg_2004] Characteristics Contracts and Actions, [Lerner 1994][research_lerner_1994_syndication] The Syndication of Venture Capital Investments, [Gompers and Lerner 2001][book_gompers_lerner_2001] The Money of Invention, and [Metrick and Yasuda 2011][book_metrick_yasuda_2011] Venture Capital and the Finance of Innovation. The framing treats the specific control allocation as one term in a specific bundle that also comprises the specific liquidation preferences, the specific board composition, the specific protective provisions, and the specific staging structure. The specific observation the framing supplies is that the specific staged-financing instrument that [Gompers 1995][research_gompers_1995] identifies as the specific principal investor control device operates independently of the specific voting rights, because an investor who declines to fund the specific next round exercises a specific control that no specific share class can neutralize. The specific staged control admits the compact form

$$v^{\text{staged}}_i(t) = \mathbb{1}\!\left[ k_i(t) > 0 \right] \cdot \frac{k_i(t)}{\sum_j k_j(t)}$$

with the specific investor's specific effective influence at the specific round proportional to the specific share of the specific required capital the specific investor supplies, and independent of any specific voting arithmetic. The specific instrument is neutralized only by the specific breadth of the specific investor base, because a specific required capital that many specific parties are willing to supply gives no specific single party the specific withholding threat.

The private-markets and listing-choice tradition traces from [Ewens and Farre-Mensa 2020][research_ewens_farre_mensa_2020] The Deregulation of the Private Equity Markets and the Decline in IPOs and treats the specific decision to remain private as a specific rational response to the specific expansion of the specific private capital supply. The framing supplies the specific most direct explanation for the specific SpaceX listing deferral, because a specific firm that can raise the specific capital it requires privately obtains the specific capital without incurring the specific governance obligations that a specific listing imposes.

The foundation-ownership tradition traces from [Hansmann 1996][book_hansmann_1996] The Ownership of Enterprise and treats the specific class of firms in which the specific controlling owner is a specific foundation with no specific personal residual claimant. The framing supplies the specific only substantial body of evidence on the specific question of whether a specific control configuration insulated from the specific capital market can persist across specific generations, and the specific evidence is the specific centurial European record the Foundation-Ownership Precedents section treats. The specific defining feature of the specific class admits the compact statement

$$\nexists \; i \; : \; e_i > 0 \; \wedge \; i \in \text{natural persons}$$

with no specific natural person holding a specific residual claim. The specific consequence is that the specific agency apparatus, which derives its specific predictions from the specific divergence between a specific manager's objective and a specific residual claimant's objective, has no specific residual claimant to anchor the specific comparison and therefore makes no specific determinate prediction about the specific class.

The organizational-institutionalism tradition traces from [Selznick 1949][book_selznick_1949] TVA and the Grass Roots through [Hargrove 1994][book_hargrove_1994] Prisoners of Myth, [Fligstein 2001][book_fligstein_2001] The Architecture of Markets, and [Chandler 1962][book_chandler_1962] Strategy and Structure, [Chandler 1977][book_chandler_1977] The Visible Hand, and [Chandler 1990][book_chandler_1990] Scale and Scope. The framing treats the specific mission as an organizational commitment that is sustained or eroded by the specific processes through which the specific organization adapts to its specific environment, and it supplies the specific vocabulary of goal displacement that names the specific failure mode the governance condition is intended to prevent. The specific displacement admits the compact form

$$D(t) = \left\| M^{\text{enacted}}(t) - M^{\text{chartered}} \right\|$$

with the specific distance between the specific mission the specific organization enacts and the specific mission it was constituted to pursue. The specific measure is what the governance apparatus is intended to hold near zero, and the specific difficulty of specifying it operationally is precisely the specific fifth sub-property the pattern-extraction section states.

The financial-sociology tradition traces from [MacKenzie 2006][book_mackenzie_2006] An Engine Not a Camera through [Ho 2009][book_ho_2009] Liquidated, [Zaloom 2006][book_zaloom_2006] Out of the Pits, [Preda 2009][book_preda_2009] Framing Finance, and [Krippner 2011][book_krippner_2011] Capitalizing on Crisis. The framing treats the specific capital-market pressures as culturally and institutionally constituted rather than as a specific natural force, and it supplies the specific account of the specific quarterly-reporting horizon as a specific artifact of a specific set of practices rather than as a specific necessary feature of public ownership.

The resource-based and dynamic-capabilities tradition traces from [Penrose 1959][book_penrose_1959] The Theory of the Growth of the Firm through [Wernerfelt 1984][research_wernerfelt_1984] A Resource-Based View of the Firm, [Barney 1991][research_barney_1991] Firm Resources and Sustained Competitive Advantage, [Peteraf 1993][research_peteraf_1993] The Cornerstones of Competitive Advantage, [Teece Pisano and Shuen 1997][research_teece_pisano_shuen_1997] Dynamic Capabilities and Strategic Management, [Eisenhardt and Martin 2000][research_eisenhardt_martin_2000], [Helfat and Peteraf 2003][research_helfat_peteraf_2003], [Winter 2003][research_winter_2003], [Teece 2007][research_teece_2007], and [Teece 2018][research_teece_2018]. The framing supplies the specific account of why the specific control question is more consequential for this specific class of firm than for a specific firm whose specific assets are redeployable. A specific capability accumulated against a specific mission is specific to that mission, so that a specific redirection destroys the specific accumulated value rather than merely reallocating it. The specific asset specificity is what converts a specific governance question from a specific distributional matter into a specific efficiency matter.

The real-options tradition traces from [Myers 1977][research_myers_1977] Determinants of Corporate Borrowing through [Black and Scholes 1973][research_black_scholes_1973], [Merton 1973][research_merton_1973], [McDonald and Siegel 1986][research_mcdonald_siegel_1986] The Value of Waiting to Invest, [Kogut and Kulatilaka 1994][research_kogut_kulatilaka_1994], [Dixit and Pindyck 1994][book_dixit_pindyck_1994] Investment Under Uncertainty, [Trigeorgis 1996][book_trigeorgis_1996] Real Options, and [Copeland and Antikarov 2001][book_copeland_antikarov_2001] Real Options A Practitioner's Guide. The framing treats the specific retained control as an option whose specific value derives from the specific asymmetry between a specific controller who can act on a specific contingency and a specific controller who cannot.

The procurement and contract-economics tradition traces from [Laffont and Tirole 1993][book_laffont_tirole_1993] A Theory of Incentives in Procurement and Regulation and [McAfee and McMillan 1988][book_mcafee_mcmillan_1988] Incentives in Government Contracting through [Myerson 1981][research_myerson_1981] Optimal Auction Design, [Milgrom 2004][book_milgrom_2004] Putting Auction Theory to Work, [Bajari and Tadelis 2001][research_bajari_tadelis_2001], [Bajari McMillan and Tadelis 2009][research_bajari_mcmillan_tadelis_2009], [Corts and Singh 2004][research_corts_singh_2004], [Kalnins and Mayer 2004][research_kalnins_mayer_2004], [Levin and Tadelis 2010][research_levin_tadelis_2010], [Che and Chung 1999][research_che_chung_1999], and [Gagnepain and Ivaldi 2002][research_gagnepain_ivaldi_2002]. The framing is relevant because the specific state customer that the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] treats is itself a specific party with a specific interest in the specific provider's governance, and specific procurement regimes impose specific organizational-conflict-of-interest and specific foreign-ownership constraints that operate as a specific governance instrument entirely outside the specific corporate-law channel.

The institutional-economics tradition traces from [North 1990][book_north_1990] Institutions Institutional Change and Economic Performance through [Ostrom 1990][book_ostrom_1990] Governing the Commons, [Greif 2006][book_grief_2006] Institutions and the Path to the Modern Economy, and [Acemoglu and Robinson 2012][book_acemoglu_robinson_2012] Why Nations Fail. The framing treats the specific corporate form as one specific institution among many for organizing a specific long-horizon collective undertaking, and it supplies the specific comparative frame within which the specific foundation, the specific chartered company, the specific cooperative, and the specific state agency are alternatives to the specific investor-owned corporation rather than deviations from it.

The innovation-systems and mission-oriented tradition traces from [Schumpeter 1942][book_schumpeter_1942] Capitalism Socialism and Democracy through [Freeman 1987][book_freeman_1987] Technology Policy and Economic Performance, [Lundvall 1992][book_lundvall_1992] National Systems of Innovation, [Nelson 1993][book_nelson_1993] National Innovation Systems, [Mowery and Rosenberg 1998][book_mowery_rosenberg_1998] Paths of Innovation, [Perez 2002][book_perez_2002] Technological Revolutions and Financial Capital, [Ruttan 2006][book_ruttan_2006] Is War Necessary for Economic Growth, [Weiss 2014][book_weiss_2014] America Inc, [Hartley 2017][book_hartley_2017] The Economics of Arms, [Mazzucato 2013][book_mazzucato_2013] The Entrepreneurial State, and [Mazzucato 2021][book_mazzucato_2021] Mission Economy. The [Schumpeter 1942][book_schumpeter_1942] argument that the specific large firm insulated from specific competitive pressure is the specific efficient locus of innovation is the specific closest antecedent in the specific economics literature to the specific claim the governance condition makes, and the specific fact that the specific argument has been contested for eight decades is a specific reason for caution rather than a specific endorsement. The [Perez 2002][book_perez_2002] treatment of the specific relationship between financial capital and production capital across a specific technological surge supplies the specific macro-level frame within which the specific tension between the specific controller's horizon and the specific investor's horizon is a specific instance of a specific recurring pattern rather than a specific idiosyncrasy of this specific firm.

The professions and organizational-culture tradition traces from [Larson 1977][book_larson_1977] The Rise of Professionalism and [Abbott 1988][book_abbott_1988] The System of Professions through [Kunda 1992][book_kunda_1992] Engineering Culture. The framing treats the specific engineering workforce as a specific party with its specific own claims and its specific own normative commitments rather than as a specific factor of production, and it supplies the specific analytical basis for the specific resource-dependence account that the OpenAI counter-example requires. The specific workforce is the specific third party to the specific founder-investor bargain, and the specific governance literature substantially omits it.

## The Founding Capital Structure 2002 through 2008

The specific founding capital structure established the specific initial conditions from which the specific subsequent control trajectory follows. The specific firm was incorporated in the specific state of Delaware in the specific 2002 period as Space Exploration Technologies Corporation, under the specific [Delaware General Corporation Law][ref_dgcl] regime whose specific permissiveness toward differential voting rights the preceding section describes. The specific founding capital was supplied substantially by the specific founder from the specific proceeds of prior ventures, in an amount that the specific biographical treatments in [Berger 2021][book_berger_2021] Liftoff, [Vance 2015][book_vance_2015] Elon Musk, and [Isaacson 2023][book_isaacson_2023] Elon Musk place at approximately 100 million dollars across the specific initial period. The specific figure is a reconstructive estimate.

The specific significance of the specific self-funded founding for the governance condition is that it establishes the specific initial control condition at its specific maximum. The specific founding wedge satisfies

$$w^{\text{founder}}(t_0) = \frac{v^{\text{founder}}(t_0)}{e^{\text{founder}}(t_0)} = 1 \qquad \text{with} \qquad e^{\text{founder}}(t_0) \approx 1$$

so that the specific control condition holds trivially without any specific instrument. The specific dual-class apparatus is unnecessary at the specific founding and becomes necessary only as the specific cash-flow share declines. The specific observation matters because it establishes the specific sequence. The specific control instruments were adopted in anticipation of a specific dilution that had not yet occurred, which distinguishes the specific case from the specific pattern in which a specific control instrument is adopted defensively after a specific threat materializes.

The specific 2002 through 2008 period is treated at length in the [series opener][related_post_a281_spacex_framing] as the specific pre-anchor prologue and in the [Value Gradient article A282][related_post_a282_spacex_value_gradient] as the specific Falcon 1 development period. The specific governance-relevant feature of the specific period is that the specific firm raised substantially little external capital across it, and that the specific external capital it did raise arrived at the specific moment of maximum distress. The specific August 2008 Founders Fund investment, which the Patient-Private Capital-Formation Leg article A290 will treat in detail, occurred between the specific third and fourth Falcon 1 flights, at a specific point when the specific firm's remaining cash was measured in weeks.

The specific timing of the specific investment relative to the specific cash position is what determines the specific bargaining position, and the specific relationship admits the compact form

$$\Theta = \frac{C^{\text{cash on hand}}}{\dot{C}^{\text{burn}}}$$

with $\Theta$ the specific runway measured in time and the specific founder's specific bargaining power declining as $\Theta$ approaches zero. The specific runway at the specific moment of the specific 2008 investment is reported in the specific biographical treatments as measured in weeks rather than in quarters. The specific bargaining position at that specific moment was as unfavorable to the specific founder as it would ever be. The specific disagreement payoff for the specific founder approached the specific liquidation value of the specific firm, and the specific standard prediction of the bargaining apparatus the preceding section states is that the specific investor should have extracted specific control terms in proportion. The specific terms that were in fact agreed did not transfer control. The specific divergence between the specific predicted and the specific observed outcome is the specific most analytically interesting feature of the specific early financing record, and the specific available explanations comprise the specific investor's own stated preference for founder-led governance, the specific idiosyncratic composition of the specific investor set, and the specific possibility that the specific founder's willingness to continue funding the specific venture personally supplied a specific credible outside option that the specific distress did not eliminate. The specific third explanation admits the compact statement

$$d^{\text{founder}} = \max\left\{ V^{\text{liquidation}}, \; V^{\text{self-funded continuation}} \right\}$$

with the specific second term nonzero only for a specific founder possessing specific independent resources. The specific term is the specific structural reason that specific wealthy founders obtain specific better control terms than specific equally capable founders without independent means, and it is a specific feature of the specific case that limits its transferability.

## The Dual-Class Share Architecture

The specific control instrument the specific firm adopted is a specific multiple-class common-stock structure in which the specific classes carry specific differential voting rights. The specific instrument is authorized by the specific [Delaware General Corporation Law][ref_dgcl] provisions governing the specific certificate of incorporation in [subchapter I][ref_dgcl_sc01], the specific classes and series of stock in [subchapter V][ref_dgcl_sc05], the specific voting rights in [subchapter VII][ref_dgcl_sc07], and the specific directors and officers in [subchapter IV][ref_dgcl_sc04]. The specific instrument is available to any specific Delaware corporation without any specific showing of purpose, and the specific chartering process is administered through the specific [Delaware Division of Corporations][ref_delaware_division_corporations].

The specific reported configuration places the specific founder holding at approximately 42 percent of the specific outstanding equity and approximately 79 percent of the specific voting power as of the specific early 2020s, corresponding to a specific wedge of

$$w^{\text{founder}} = \frac{v^{\text{founder}}}{e^{\text{founder}}} \approx \frac{0.79}{0.42} \approx 1.9$$

and to a specific control condition satisfied with substantial margin. Both specific figures are reconstructive estimates drawn from the specific trade-press reporting and specific investor communications rather than from any specific disclosure, and the specific precise class structure and the specific per-class voting ratios are not public. The specific reported reincorporation of the specific firm from the specific state of Delaware to the specific state of Texas in the specific 2024 period, which the specific [Texas Business Organizations Code][ref_texas_boc] would govern, is reported rather than documented in a specific public filing available to the article, and the specific corresponding registry is the specific [Texas Secretary of State][ref_texas_sos]. The specific corporate identity and the specific public-facing corporate materials appear at the specific [SpaceX corporate site][ref_spacex_company].

The specific general form of the specific two-class arrangement admits compact statement. Let $n_A$ and $n_B$ denote the specific share counts of the specific superior and inferior classes and let $\lambda$ denote the specific votes per superior share with the specific inferior share carrying one vote. The specific voting share of a specific holder of the specific entire superior class is

$$v = \frac{\lambda \, n_A}{\lambda \, n_A + n_B}$$

and the specific corresponding cash-flow share is $e = n_A / (n_A + n_B)$ under the specific assumption of equal economic rights across classes. The specific control condition $v > 1/2$ reduces to the specific requirement

$$\frac{n_A}{n_B} > \frac{1}{\lambda}$$

so that a specific tenfold voting ratio permits the specific control condition to hold while the specific founder holds slightly more than one eleventh of the specific outstanding shares. The specific arithmetic is the specific reason a specific dual-class structure sustains control across a specific dilution sequence that would otherwise terminate it, and it is the specific reason the specific policy literature regards the specific instrument as capable of producing arbitrarily large separations.

The specific instrument is not unlimited in its specific effect. The specific staged-financing control that [Gompers 1995][research_gompers_1995] identifies operates through the specific investor's decision whether to fund the specific subsequent round rather than through any specific vote, and the specific instrument therefore does not neutralize it. The specific protective provisions customary in specific preferred-stock financings confer specific class-level veto rights over specific enumerated actions including specific liquidation, specific charter amendment, and specific creation of senior securities, and the specific provisions operate irrespective of the specific common-stock voting arithmetic. The specific fiduciary duties that the specific [Delaware Court of Chancery][ref_delaware_chancery] enforces constrain the specific controller in specific transactions in which the specific controller stands on both sides. The specific control the specific instrument confers is therefore a specific control over the specific ordinary business and the specific board composition rather than a specific unconditional authority.

## The Financing Sequence and Dilution Management

The specific financing sequence comprises more than thirty rounds across the specific 2002 through drafting-date period. The specific rounds are conducted as specific private placements exempt from specific registration under the specific [Securities Act private-placement exemption][ref_securities_act_4a2] and the specific [Regulation D][ref_reg_d] safe harbor, and specifically under the specific [Rule 506][ref_rule_506] provisions that permit an unlimited specific offering amount to specific accredited investors. The specific existence and approximate size of many of the specific rounds reaches the public record through the specific [Form D][ref_sec_form_d] notice filings and the specific state-level filings that the specific [Securities and Exchange Commission EDGAR][ref_sec_edgar] system and specific state regulators publish. The specific terms are not published.

The specific employee equity compensation that the specific firm issues operates under a specific separate exemption in [Rule 701][ref_rule_701], and the specific subsequent resale of the specific restricted securities so issued operates under [Rule 144][ref_rule_144]. The specific two rules together constitute the specific machinery by which a specific unlisted firm can compensate a specific large workforce in equity, and they are as load-bearing for the specific configuration as the specific voting instrument itself. A specific firm unable to issue and later permit the resale of specific employee equity could not retain a specific technical workforce across a specific decade-scale private period.

The specific reported valuation trajectory rises from a specific figure in the specific hundreds of millions of dollars across the specific late 2000s, through approximately 12 billion dollars at the specific January 2015 round, approximately 33 billion dollars in the specific 2019 period, approximately 100 billion dollars in the specific 2021 period, approximately 127 billion dollars in the specific 2022 period, approximately 180 billion dollars in the specific late 2023 period, approximately 210 billion dollars in the specific mid 2024 period, and approximately 350 billion dollars in the specific late 2024 period, with specific subsequent rounds at higher figures. Every specific figure in the specific sequence is a reconstructive estimate drawn from specific trade-press reporting of specific tender-offer prices and specific primary-round terms.

The specific analytically important feature of the specific sequence is not the specific valuation trajectory but the specific relationship between the specific capital raised and the specific voting rights transferred. The specific cumulative capital raised across the specific sequence admits the compact form

$$K^{\text{cumulative}} = \sum_{n=1}^{N} k_n$$

and the specific cumulative voting transferred admits the compact form

$$\Delta v^{\text{transferred}} = \sum_{n=1}^{N} \Delta v_n \approx 0$$

with the specific second sum near zero despite the specific first sum reaching the specific tens of billions of dollars. The specific ratio

$$\eta = \frac{\Delta v^{\text{transferred}}}{K^{\text{cumulative}}}$$

is the specific quantity the governance condition requires to be small, and it is the specific quantity that distinguishes the specific SpaceX financing history from the specific ordinary venture-financing history in which the specific ratio is bounded below by the specific pro-rata relationship between capital and equity.

The specific investor set across the specific sequence has broadened from a specific small group of specific venture funds to a specific set comprising specific sovereign wealth funds, specific mutual-fund complexes, specific corporate strategic investors, and specific family offices. The specific broadening is itself a specific governance instrument, because a specific dispersed investor base faces a specific coordination cost in assembling the specific coalition the contestability measure defines. The specific coordination cost admits the compact form

$$C^{\text{coalition}}(S) = \gamma \cdot |S| \cdot \left( 1 - h \right)$$

with $|S|$ the specific coalition size required and $h$ a specific concentration measure of the specific investor base. The specific cost rises as the specific base disperses, so that the specific dispersion supplements the specific voting arithmetic rather than merely accompanying it.

## The January 2015 Google and Fidelity Round

The specific January 2015 round in which the specific Google and Fidelity investors supplied approximately 1 billion dollars for approximately 10 percent of the specific firm constitutes the specific most analytically significant single financing event in the specific sequence, for three reasons.

The specific first reason is scale. The specific round was substantially larger than any specific prior round and established that the specific firm could raise the specific capital a specific constellation program would require without a specific public listing. The specific round arithmetic admits the compact form

$$V^{\text{post}} = \frac{k}{\delta} \qquad \text{and} \qquad V^{\text{pre}} = V^{\text{post}} - k$$

with $k$ the specific capital supplied and $\delta$ the specific fraction acquired, giving a specific post-money figure of approximately 10 billion dollars at the specific reported terms. The specific implied valuation of approximately 12 billion dollars is a reconstructive estimate and the specific spread between the specific arithmetic and the specific reported figure reflects the specific imprecision of the specific public reporting rather than any specific identified structural feature.

The specific second reason is that the specific round was motivated by a specific business line that did not yet exist. The specific Starlink constellation that the [Value Capture article A284][related_post_a284_spacex_value_capture] treats had been announced days before the specific round in the specific Seattle announcement, and the specific investor thesis was accordingly a specific bet on a specific future satellite-broadband business rather than on the specific existing launch-service business. The specific structure is a specific instance of the specific pattern the Portfolio-Patience article A288 will treat, in which a specific capability base supports a specific option on a specific adjacent business that the specific capital market prices before the specific business exists.

The specific third reason is that the specific round introduced a specific strategic corporate investor whose specific own business interests intersected the specific venture's. A specific strategic investor differs from a specific financial investor in that the specific objective function includes specific terms unrelated to the specific venture's own returns, which raises the specific capture hazard the governance condition addresses in its specific most concrete form. The specific hazard admits the compact statement

$$U^{\text{strategic}}_i = e_i \cdot V^{\text{venture}} + \phi_i \cdot V^{\text{own business}}$$

with $\phi_i$ the specific weight the specific strategic investor places on the specific effect of the specific venture's decisions on the specific investor's own business. The specific weight can be negative, in the specific case where the specific venture's success would damage the specific investor's existing position, and a specific strategic investor with a specific negative weight has a specific interest in slowing the specific venture that no specific financial investor shares. The specific control configuration is the specific instrument that renders the specific weight irrelevant, because a specific investor who cannot vote cannot act on the specific interest. The specific value the specific investors were purchasing was substantially a specific option on a specific business that did not yet exist, admitting the compact form

$$V^{\text{round}} = V^{\text{launch service}} + p^{\text{constellation}} \cdot \left[ V^{\text{constellation}} - K^{\text{deployment}} \right]^{+}$$

with the specific second term an option payoff weighted by the specific probability that the specific constellation reaches deployment. The specific structure is the specific reason a specific round of that specific size could be raised against a specific business line announced days earlier, and it is the specific reason the specific investors accepted specific terms conferring no specific control over the specific program whose specific success their specific return depended on.

The specific record does not indicate that any specific such attempt occurred. The specific analytical claim the article advances is the specific weaker one that the specific configuration made the specific attempt pointless rather than that the specific attempt was made and defeated.

## The Tender-Offer Liquidity Mechanism

The specific firm has conducted specific periodic tender offers, reported at approximately semi-annual frequency across the specific recent period, in which specific employees and specific early investors sell specific shares to specific incoming investors at a specific price the specific firm sets. The specific mechanism is the specific governance-critical innovation in the specific financing history and deserves treatment on its own terms. The specific issuer-tender-offer conduct is governed by the specific [Rule 13e-4][ref_rule_13e4] provisions and the specific [Regulation 14E][ref_reg_14e] antifraud and timing requirements, which apply to a specific issuer repurchase irrespective of whether the specific issuer is a specific reporting company, and the specific resale mechanics operate under [Rule 144][ref_rule_144].

The specific problem the mechanism solves is that a specific private firm's specific equity compensation is illiquid, and that the specific illiquidity becomes intolerable to specific employees as the specific holding period extends across the specific decade-scale horizon a specific mission-directed venture requires. The specific ordinary solution is a specific public listing, which supplies the specific liquidity and simultaneously transfers the specific governance obligations that the specific condition seeks to avoid. The specific tender-offer mechanism decouples the specific two.

The specific decoupling admits the compact statement. Let $L$ denote the specific liquidity supplied to specific existing holders and let $G$ denote the specific governance obligations incurred. A specific public listing produces

$$\left( L^{\text{IPO}}, \; G^{\text{IPO}} \right) \qquad \text{with both terms large}$$

whereas the specific tender-offer mechanism produces

$$\left( L^{\text{tender}}, \; G^{\text{tender}} \right) \qquad \text{with} \qquad L^{\text{tender}} \lesssim L^{\text{IPO}}, \quad G^{\text{tender}} \approx 0$$

so that the specific mechanism obtains substantially the specific liquidity benefit at substantially none of the specific governance cost. The specific mechanism is available only to a specific firm whose specific shares command sufficient demand that a specific buyer appears at the specific price the specific firm sets, which is to say only to a specific firm that does not need the specific public market. The specific availability condition is the specific reason the mechanism is not a general solution.

The specific mechanism confers a specific further control benefit that is easily overlooked. The specific firm controls the specific transfer, and the specific transfer restrictions customary in specific private-company charters permit the specific firm to determine who may acquire the specific shares. The specific right of first refusal and the specific transfer-approval provisions admit the compact characterization as a specific admissible-buyer set

$$\mathcal{B}^{\text{admissible}} \subsetneq \mathcal{B}^{\text{willing}}$$

with the specific firm selecting the specific buyers from the specific willing set. The specific selection permits the specific firm to exclude specific parties whose specific accumulation of the specific shares would be strategically unwelcome, which is an instrument that no specific public company possesses.

## The Deferred Initial-Public-Offering Decision

The specific decision not to list has been sustained across the specific entire history of the specific firm and across specific repeated public statements that a specific listing of the specific parent company is not contemplated. The specific decision is the specific single most consequential governance decision the specific firm has made, and it is substantially overdetermined.

The specific legal precondition deserves statement before the specific economic determinants, because a specific firm does not remain private merely by declining to list. A specific issuer becomes a specific reporting company by operation of the specific [Exchange Act registration threshold][ref_exchange_act_12g] once its specific total assets and its specific holder-of-record count exceed specific statutory levels, and the specific threshold is implemented in the specific [Rule 12g-1][ref_rule_12g1] provisions. The specific threshold was raised substantially by the specific [Jumpstart Our Business Startups Act of 2012][ref_jobs_act_2012], which also excluded specific holders who received their specific securities under specific employee compensation plans from the specific count. The specific statutory change is the specific single legal development most responsible for the specific viability of the specific configuration this article describes, because it permitted a specific firm to accumulate a specific large employee and investor base without triggering the specific reporting obligation. The specific configuration is therefore not a specific timeless option available to any specific founder. It is a specific artifact of a specific statutory settlement dating to the specific 2012 period.

The specific first determinant is the specific one the private-markets tradition identifies. The specific expansion of the specific private capital supply that [Ewens and Farre-Mensa 2020][research_ewens_farre_mensa_2020] document has made the specific capital available privately, which removes the specific principal historical reason to list. The specific listing decision admits the compact form

$$\text{list} \iff \left[ K^{\text{required}} > K^{\text{private available}} \right] \; \vee \; \left[ L^{\text{required}} > L^{\text{tender}} \right]$$

with the specific listing warranted only when the specific capital requirement exceeds the specific private supply or the specific liquidity requirement exceeds what the specific tender mechanism supplies. Neither specific condition has bound. The specific cost the specific deferral imposes is a specific illiquidity discount in the specific price at which the specific private capital is supplied, admitting the compact form

$$r^{\text{private}} = r^{\text{public}} + \pi^{\text{illiquidity}} + \pi^{\text{opacity}}$$

with the specific two premia compensating the specific investor for the specific absence of a specific liquid market and for the specific absence of the specific disclosure. The specific deferral is rational for the specific controller whenever the specific governance value of the specific retained control exceeds the specific capitalized value of the specific two premia, and the specific magnitude of the specific premia has fallen across the specific period as the specific private secondary market has deepened.

The specific second determinant is the specific governance obligation a specific listing imposes. The specific obligations comprise the specific periodic disclosure and the specific internal-control attestation that the specific [Sarbanes-Oxley Act of 2002][ref_sarbanes_oxley_2002] imposes, the specific quarterly earnings cycle, the specific proxy access through which specific shareholders present specific proposals under [Rule 14a-8][ref_rule_14a8], the specific say-on-pay advisory vote that the specific [Dodd-Frank Act of 2010][ref_dodd_frank_2010] introduced, the specific beneficial-ownership disclosure on [Schedule 13D][ref_schedule_13d] that makes a specific accumulating position visible, the specific listing standards that the specific [NYSE Listed Company Manual][ref_nyse_listed_company_manual] and the specific [Nasdaq listing rules][ref_nasdaq_listing_rules] impose, the specific market for corporate control that [Manne 1965][research_manne_1965] Mergers and the Market for Corporate Control describes, and the specific exposure to specific activist campaigns. The specific obligations are individually survivable under a specific dual-class structure and jointly constitute a specific ongoing constraint that a specific unlisted firm does not face.

The specific third determinant is specific to the mission-directed case. The specific disclosure obligation would require the specific firm to publish the specific cost and specific schedule performance of a specific development program whose specific difficulties are severe and whose specific timeline is long. The specific publication would supply the specific raw material for a specific narrative of failure at each specific intermediate setback, and the specific narrative would in turn affect the specific cost of capital and the specific customer relationships. The specific effect admits the compact statement

$$\text{Var}\!\left[ V^{\text{market}} \mid \text{disclosed} \right] \gg \text{Var}\!\left[ V^{\text{market}} \mid \text{undisclosed} \right]$$

with the specific disclosed valuation substantially more volatile across the specific development period. The specific volatility is not merely uncomfortable. It feeds back into the specific ability to raise the specific subsequent capital and into the specific retention of the specific personnel whose specific compensation is denominated in the specific equity.

The specific counterargument the governance literature supplies is that the specific disclosure and the specific market discipline are precisely the specific mechanisms that prevent a specific controller from persisting in a specific mistaken course, and that a specific firm which exempts itself from them retains no specific external correction. The specific counterargument is correct as stated. The specific question the case poses is whether the specific external correction would have distinguished a specific mistaken course from a specific difficult but correct one, and the specific Space Shuttle and specific Constellation records that the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats supply specific reasons for doubt about the specific discriminating power of specific external oversight applied to specific long-horizon development programs.

## The Starlink Separation Question

The specific question whether the specific Starlink business will be separated and listed independently has been raised repeatedly across the specific period since the specific 2019 deployment began and remains unresolved at the drafting date. The specific question is governance-critical because a specific separation would create the specific first public-market claim on the specific SpaceX capability base.

The specific case for separation rests on the specific valuation argument that a specific subscription-revenue business is valued on specific different multiples than a specific launch-service business, and on the specific capital argument that a specific listed Starlink could raise specific capital against its specific own cash flows. The specific case against separation rests on the specific integration argument that the [Value Capture article A284][related_post_a284_spacex_value_capture] develops, under which the specific value is created precisely by the specific joint operation of the specific launch and specific constellation businesses, and on the specific governance argument the present article develops.

The specific governance argument admits compact statement. A specific separation transfers the specific financing loop that the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] formalizes from a specific internal transfer to a specific external one. Under the specific integrated configuration the specific Starlink surplus funds the specific Starship development by a specific internal capital allocation that the specific controller directs. Under the specific separated configuration the specific transfer would require a specific dividend, a specific intercompany agreement, or a specific related-party transaction, each of which is subject to a specific fiduciary review that the specific internal allocation is not. The specific difference admits the compact form

$$\text{cost of transfer} = \begin{cases} \approx 0 & \text{integrated} \\ C^{\text{fiduciary}} + C^{\text{minority}} & \text{separated} \end{cases}$$

with the specific separated configuration incurring a specific review cost and a specific minority-protection cost on every specific transfer. The specific separation decision therefore turns on a specific comparison between a specific sum-of-parts valuation and a specific integrated valuation net of the specific transfer frictions, admitting the compact form

$$\Delta = \left[ V^{\text{Starlink standalone}} + V^{\text{SpaceX ex-Starlink}} \right] - \left[ V^{\text{integrated}} + \Pi^{\text{control}} \right]$$

with $\Pi^{\text{control}}$ the specific value the specific controller assigns to the specific unimpeded internal capital allocation. The specific separation is undertaken when $\Delta > 0$, and the specific inclusion of the specific control term is what distinguishes the specific decision facing this specific firm from the specific ordinary conglomerate-discount calculation. The specific costs are not prohibitive and they are not zero, and a specific controller whose specific principal use of the specific subsidiary's cash flow is to fund a specific parent-level mission has a specific interest in avoiding them.

## The OpenAI Counter-Example

The specific OpenAI governance structure from the specific December 2015 founding through the specific November 2023 board crisis and the specific subsequent restructuring constitutes the canonical governance negation case in the specific contemporary technology sector. The specific case is analytically valuable precisely because the specific structure was designed explicitly and self-consciously to resist capital capture, and because it failed. The specific record is documented in the specific [OpenAI charter][ref_openai_charter] and the specific [OpenAI announcements][ref_openai_news], supplemented by the specific contemporaneous reporting in [The New York Times][ref_nyt], [Bloomberg][ref_bloomberg], the [Wall Street Journal][ref_wsj], and [The Washington Post][ref_washington_post].

The specific structure comprised a specific nonprofit entity founded in the specific December 2015 period whose specific board held the specific ultimate control authority, and beneath it a specific capped-profit subsidiary created in the specific March 2019 period whose specific investors received returns limited by a specific multiple of the specific invested capital. The specific arrangement placed the specific control authority in the hands of a specific board explicitly constituted so that a specific majority of its specific members held no specific equity in the specific enterprise. The specific design intent was that the specific board would be able to act against the specific financial interest of the specific investors where the specific charter mission required it.

The specific formal control measure for the specific arrangement was maximal. In the notation the economic-property section establishes, the specific nonprofit board held

$$v^{\text{board}} = 1 \qquad \text{with} \qquad e^{\text{board}} = 0 \qquad \text{so} \qquad w^{\text{board}} = \frac{v}{e} \to \infty$$

with the specific wedge unbounded. The specific SpaceX wedge of approximately 1.9 is modest by comparison. If the specific formal wedge were the operative quantity, the specific OpenAI structure would have been the specific most capture-resistant arrangement in the specific sector.

The specific November 2023 events established that the specific formal wedge is not the operative quantity. The specific board removed the specific chief executive on the specific November 17 2023 date. Within the specific following days substantially the entire specific employee body signed a specific letter indicating an intention to depart for the specific principal investor, the specific principal investor made clear that it would receive them, and the specific board reversed itself. The specific chief executive was reinstated on approximately the specific November 21 2023 date and the specific board was reconstituted. The specific elapsed interval was approximately five days.

The specific analytical content of the specific episode is the specific distinction between formal and effective control that the economic-property section formalizes. The specific effective control satisfied

$$v^{\text{effective}}_{\text{board}} \approx 0 \qquad \text{despite} \qquad v^{\text{formal}}_{\text{board}} = 1$$

because the specific organization's specific productive capacity resided in specific personnel who could depart, and the specific personnel's specific economic interest was aligned with the specific investor rather than with the specific board. The specific resource-dependence term in the specific effective-control expression dominated the specific formal term entirely. The specific board possessed the specific authority to remove the specific chief executive and did not possess the specific capacity to operate the specific organization afterward, and a specific control that cannot survive its own exercise is not a specific control.

The specific structural conditions that produced the specific outcome admit compact statement. Let $\theta$ denote the specific fraction of the specific organization's specific productive value embodied in specific mobile human capital, and let $\alpha$ denote the specific fraction of the specific personnel's specific compensation contingent on the specific equity value. The specific board's specific effective authority declines in both, and the specific condition under which a specific formally controlling body can in fact prevail is

$$\theta \cdot \alpha < \bar{\tau}$$

for a specific threshold $\bar{\tau}$ determined by the specific switching costs the specific personnel would face. A specific research organization whose specific value is substantially its specific researchers and whose specific researchers hold specific substantial equity-linked claims sits far above the specific threshold. The specific condition is not a specific defect of the specific particular board or the specific particular individuals, and a specific differently composed board facing the specific identical conditions would have faced the specific identical outcome. The specific coordination structure that produced the specific rapid reversal admits the compact statement as a specific threshold model in which each specific individual departs once a specific sufficient fraction of specific colleagues has committed to depart

$$\text{depart}_i \iff f^{\text{committed}} \geq \theta_i$$

with $\theta_i$ the specific individual threshold and the specific cascade completing whenever the specific distribution of the specific thresholds admits no specific stable interior equilibrium. The specific published letter served the specific function of making the specific committed fraction common knowledge, which is the specific mechanism by which a specific latent majority becomes a specific realized one.

The specific subsequent trajectory has moved the specific structure toward specific conventional arrangements. The specific restructuring toward a specific public benefit corporation and the specific reported removal of the specific return cap in the specific 2025 period complete the specific convergence. The specific capped-profit instrument was itself a specific transitional device whose specific removal was predictable from the specific moment the specific capital requirement exceeded what specific capped-return investors would supply. The specific removal admits the compact statement that a specific return cap $\bar{R}$ binds only while

$$\bar{R} > R^{\text{market}}\!\left( \text{risk} \right)$$

and ceases to be acceptable to specific incoming investors once the specific required market return on the specific risk exceeds the specific cap. A specific cap set generously enough never to bind imposes no specific discipline, and a specific cap set tightly enough to discipline eventually blocks the specific financing. The specific instrument therefore has no specific stable configuration under a specific capital requirement that grows.

The specific comparison with the specific SpaceX configuration is direct and instructive. The specific SpaceX controller holds a specific formal wedge that is modest relative to the specific OpenAI board's, and holds in addition a specific position in the specific resource-dependence structure that the specific OpenAI board lacked entirely. The specific controller is not merely the specific holder of the specific votes. The specific controller is also the specific person whose specific departure the specific personnel and the specific investors would regard as the specific principal risk to the specific enterprise, which places the specific resource-dependence term on the specific same side as the specific formal term rather than against it. The specific governance condition is therefore not satisfied by the specific voting arithmetic alone, and the specific arithmetic is the specific visible part of an arrangement whose specific operative part is the specific alignment between the specific formal authority and the specific effective authority.

## The Tesla Comparison and the Limits of Public-Company Founder Control

The specific Tesla case supplies the specific complementary negation, in which the specific same individual operating under specific public-company conditions without a specific dual-class structure encountered specific constraints that the specific SpaceX configuration does not impose. The specific case is directly comparative because the specific controller, the specific management style, and the specific approximate period are held constant while the specific governance configuration varies.

The specific Tesla equity position is reported at approximately 13 percent following specific share dispositions across the specific 2021 through 2022 period, with the specific ordinary one-share-one-vote configuration and therefore

$$w^{\text{Tesla}} = \frac{v}{e} \approx 1 \qquad \text{against} \qquad w^{\text{SpaceX}} \approx 1.9$$

and a specific control condition that fails rather than holds. The specific consequence is that the specific Tesla controller governs by a specific combination of specific board relationships, specific retail-shareholder support, and specific personal prominence rather than by a specific voting majority.

The specific 2018 chief-executive performance award and the specific ensuing litigation illustrate the specific difference concretely. The specific Delaware Court of Chancery in the specific Tornetta matter rescinded the specific award in the specific January 2024 decision on the specific ground that the specific approval process had been controlled rather than independent, and the specific court declined to reverse itself following the specific shareholder ratification vote of the specific mid 2024 period. The specific record is accessible through the specific [Delaware Court of Chancery][ref_delaware_chancery] and the specific [Delaware courts opinions archive][ref_delaware_opinions], and the specific corresponding corporate disclosures appear in the specific [Tesla investor materials][ref_tesla_ir]. The specific subsequent shareholder approval of a specific reincorporation from the specific state of Delaware to the specific state of Texas under the specific [Texas Business Organizations Code][ref_texas_boc] constitutes a specific forum response to a specific substantive constraint.

The specific analytical lesson is that the specific fiduciary apparatus binds a specific controller who lacks a specific voting majority substantially more tightly than one who holds it, because the specific controlled-transaction doctrines apply the specific entire-fairness standard to a specific transaction in which the specific controller stands on both sides and the specific standard is applied by a specific court rather than by a specific vote. The specific standard-selection rule that produces the specific difference admits the compact statement

$$\text{standard} = \begin{cases} \text{business judgment} & \text{if no controller stands on both sides} \\ \text{entire fairness} & \text{otherwise, absent cleansing} \end{cases}$$

with the specific second branch shifting the specific burden to the specific defendant and subjecting the specific transaction to a specific substantive review rather than to a specific deferential one. The specific cleansing procedures require a specific independent committee and a specific informed majority-of-the-minority vote, and the specific finding that the specific process was controlled rather than independent is what removed the specific cleansing in the specific matter.

The specific control a specific founder exercises without a specific voting majority is therefore a specific substitute rather than an equivalent, admitting the compact form

$$v^{\text{effective}} = \beta_1 v^{\text{formal}} + \beta_2 \, s^{\text{board relationships}} + \beta_3 \, s^{\text{retail support}} + \beta_4 \, d^{\text{indispensability}}$$

with the specific latter three terms substantially more contestable and more perishable than the specific first. The specific public statements in which the specific individual expressed a specific preference for a specific greater voting share at Tesla before committing specific further artificial-intelligence and specific robotics work to it constitute a specific direct statement of the specific governance condition this article treats, applied by the specific person to whom it applies.

The specific comparison establishes that the specific SpaceX configuration is not simply an expression of a specific individual preference for control. The specific same individual accepted a specific substantially weaker control position at a specific different firm whose specific capital was raised in the specific public market, which indicates that the specific control configuration tracks the specific financing channel rather than tracking the specific person.

## Foundation-Ownership Precedents

The specific foundation-ownership arrangements of the specific German and specific Danish industrial tradition constitute the specific longest-running experiments in a specific control configuration insulated from the specific capital market. The specific arrangements are the specific positive precedents for the governance condition, and they are the specific only available evidence on the specific question of whether a specific capture-resistant configuration can persist beyond the specific lifetime of the specific founder.

The specific Carl Zeiss Stiftung established in the specific 1889 period by the specific physicist Ernst Abbe, with the specific governing statute completed in the specific 1896 period, is the specific earliest of the specific arrangements. The specific founder transferred the specific ownership of the specific optical works to a specific foundation whose specific statute defined the specific purposes and constrained the specific successors, and the specific foundation remains the specific owner of the specific Carl Zeiss and specific Schott enterprises at the drafting date. The specific record is accessible through the specific [Carl Zeiss Stiftung][ref_carl_zeiss_stiftung] documentation and the specific [Carl Zeiss corporate][ref_zeiss_corporate] materials, and the specific German legal form within which the specific arrangement operates is governed by the specific [Aktiengesetz][ref_german_aktiengesetz] provisions on specific share classes and specific corporate organs. The specific statute is analytically remarkable because it constrained the specific foundation itself rather than merely establishing it, prohibiting specific family control, fixing specific labor conditions including a specific limited working day and a specific pension provision, and specifying that no specific individual could derive a specific personal claim from the specific enterprise. The specific instrument is therefore a specific commitment device operating against the specific founder's own successors as much as against the specific external capital market. The specific statutory constraint admits the compact form

$$\mathcal{A}^{\text{permitted}} = \mathcal{A} \setminus \mathcal{A}^{\text{prohibited by statute}}$$

with the specific foundation's specific action set restricted by the specific founding instrument rather than merely directed by it. The specific distinction between a specific restriction and a specific direction is the specific whole of the difference between a specific commitment device and a specific statement of intent, because a specific direction can be reinterpreted by a specific successor and a specific restriction must be amended.

The specific Robert Bosch arrangement supplies the specific cleanest available separation of the specific two rights. The specific configuration established following the specific founder's death in the specific 1942 period and implemented in the specific 1964 period places approximately 94 percent of the specific share capital with the specific charitable foundation and approximately 0.01 percent of the specific voting rights, while a specific industrial trust holds approximately 93 percent of the specific voting rights against approximately 0.01 percent of the specific capital. The specific record is accessible through the specific [Robert Bosch Stiftung][ref_bosch_stiftung] documentation, the specific [Bosch corporate][ref_bosch_company] materials, and the specific [Bosch annual reporting][ref_bosch_annual_report] that discloses the specific ownership split. The specific wedges are

$$w^{\text{foundation}} = \frac{0.0001}{0.94} \approx 0.0001 \qquad \text{and} \qquad w^{\text{trust}} = \frac{0.93}{0.0001} \approx 9300$$

with the specific separation approaching the specific theoretical limit in both directions. The specific arrangement demonstrates that the specific wedge admits values orders of magnitude beyond anything a specific dual-class listed company exhibits, and that a specific configuration at that specific extreme has operated a specific major industrial enterprise across approximately six decades without the specific expropriation the agency tradition predicts.

The specific Novo Nordisk arrangement places the specific Novo Nordisk Foundation, through the specific Novo Holdings entity, in control of the specific operating company by means of a specific two-class share structure in which the specific superior class carries a specific tenfold voting right. The specific reported position is approximately 28 percent of the specific capital and approximately 77 percent of the specific votes, corresponding to

$$w^{\text{Novo}} = \frac{0.77}{0.28} \approx 2.8$$

which is the specific closest of the specific three precedents to the specific SpaceX configuration in magnitude. The specific record is accessible through the specific [Novo Nordisk Foundation][ref_novo_nordisk_foundation] documentation, the specific [Novo Holdings][ref_novo_holdings] materials, and the specific [Novo Nordisk investor disclosures][ref_novo_nordisk_investors] that report the specific class structure. The specific Danish corporate and foundation registry framework is administered through the specific [Danish Business Authority][ref_danish_business_authority]. The specific arrangement is distinguished from the specific SpaceX case by the specific fact that the specific operating company is publicly listed, so that the specific configuration combines the specific capture resistance with the specific public-market disclosure and liquidity that the specific SpaceX configuration forgoes.

The specific comparative significance of the specific three precedents rests on the specific survival evidence they supply. The specific arrangements have persisted across approximately 137 years, approximately 84 years, and approximately 76 years respectively at the drafting date, spanning specific wars, specific currency collapses, specific generational transitions, and specific complete turnovers of the specific operating businesses. The specific survival function admits the compact form

$$S(t) = P\!\left( \text{configuration intact at } t \mid \text{established at } 0 \right)$$

with the specific foundation-owned population exhibiting a specific substantially flatter hazard than the specific founder-controlled population, for the specific structural reason that a specific foundation does not die and a specific founder does. The specific observation identifies the specific principal unresolved question about the specific SpaceX configuration, because the specific instrument the specific firm employs is tied to a specific individual and the specific precedents that demonstrate centurial persistence are not.

The specific three cases are the specific best documented instances of a specific broader class. The specific class includes specific Nordic sphere-holding arrangements in which a specific family foundation controls a specific holding company that in turn controls a specific portfolio of specific listed operating companies, specific German family-foundation arrangements beyond the specific two treated here, and specific arrangements in specific other jurisdictions in which a specific trust or a specific charitable entity holds the specific controlling block of a specific major enterprise. The specific common structural feature is the specific separation of the specific entity that holds the specific economic interest from the specific entity that exercises the specific control, and the specific common consequence is that no specific natural person can capture the specific enterprise by acquiring the specific shares. The specific arrangements are concentrated in specific jurisdictions whose specific foundation law permits them, which is a specific further instance of the specific legal-origins point the law-and-finance framing makes.

The specific literature on the specific arrangements is thinner than their specific significance warrants, and [Hansmann 1996][book_hansmann_1996] The Ownership of Enterprise remains the specific principal theoretical treatment of the specific class of firms in which the specific residual claimant is absent or attenuated. The specific empirical finding the specific literature reports is that the specific foundation-owned firms exhibit specific lower profitability variance, specific longer investment horizons, and specific comparable or slightly lower returns than specific comparable investor-owned firms, which is the specific profile the mission-directed configuration would predict.

## The Sunset-Provision and Successor Question

The specific sub-property the cross-sectional analysis identifies as unsatisfied deserves treatment on its own terms, because it is the specific respect in which the specific configuration differs from every specific arrangement that has demonstrated centurial persistence.

The specific policy literature that [Bebchuk and Kastiel 2017][research_bebchuk_kastiel_2017] represents proposes the specific sunset provision as the specific remedy for the specific perpetual dual-class structure. A specific sunset converts the specific superior class to a specific ordinary class upon a specific triggering event, which may be the specific passage of a specific fixed interval, the specific death or incapacity of the specific founder, the specific transfer of the specific shares outside a specific permitted class of holders, or the specific decline of the specific founder's economic stake below a specific threshold. The specific instrument admits the compact statement as a specific stopping time

$$\lambda^{\text{effective}}(t) = \lambda \cdot \mathbb{1}\!\left[ t < T^{\text{sunset}} \right] + 1 \cdot \mathbb{1}\!\left[ t \geq T^{\text{sunset}} \right]$$

with the specific voting ratio collapsing to unity at the specific trigger. The specific policy argument for the specific instrument rests on the specific empirical finding that the specific value discount associated with the specific wedge steepens with the specific tenure, which implies that the specific benefits of the specific founder control are front-loaded and the specific costs are back-loaded.

The specific argument has a specific weakness in the specific mission-directed case that the specific policy literature does not address. A specific mission whose specific completion horizon exceeds the specific sunset interval is not protected by a specific configuration that terminates before the specific mission does. The specific condition for a specific sunset to be compatible with the specific mission is

$$T^{\text{sunset}} > T^{\text{mission}}$$

and a specific Mars-transportation objective of the specific kind the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats has a specific horizon that no specific conventional sunset interval approaches. The specific policy instrument and the specific mission-directed configuration are therefore in specific direct tension, and the specific tension is not resolvable by adjusting the specific interval, because an interval long enough to protect the specific mission is long enough to reproduce substantially the specific perpetual structure the instrument was designed to prevent.

The specific foundation instrument resolves the specific tension by a specific different route. A specific foundation does not sunset because it does not die, and the specific commitment it embodies binds the specific successors rather than expiring for their benefit. The specific difference between a specific sunset and a specific foundation is therefore not a specific difference of degree along a single dimension. The specific sunset assumes that the specific founder control is a specific transitional necessity to be unwound, and the specific foundation assumes that it is a specific permanent arrangement to be institutionalized. The specific two instruments answer specific different questions.

The specific succession record across the specific comparison set supports a specific compact empirical generalization. A specific arrangement resting on a specific individual's holdings terminates at a specific transition unless a specific instrument transfers it, and the specific instruments available comprise the specific trust, the specific foundation, the specific family holding company, and the specific voting agreement. Each of the specific instruments has been used at scale, each is documented in the specific precedents this article treats, and none is present in the specific SpaceX configuration at the drafting date so far as the specific public record discloses. The specific absence may reflect a specific deliberate choice, a specific matter not yet reached, or a specific arrangement that exists and is not public. The article cannot distinguish among the specific three.

The specific analytical significance of the specific open question is that it determines which of the specific two readings of the specific case is correct. Under the specific first reading the specific configuration is a specific durable institutional innovation of the specific kind the specific foundation precedents represent. Under the specific second reading it is a specific personal arrangement that will terminate with the specific person, and the specific mission it protects will then face the specific capital market on specific ordinary terms at whatever specific stage of completion it has reached. The specific evidence available at the drafting date does not discriminate, and the specific article declines to guess.

## Deep Historical Comparative Precedents

The governance mechanic admits comparison with specific deep historical precedents that establish the specific property as a recurring feature of enterprises pursuing specific objectives beyond the specific horizon of their specific capital providers.

The specific chartered-company form of the specific early modern period constitutes the specific origin of the specific problem. The specific English and specific Dutch East India Companies separated the specific ownership from the specific control at a specific scale and across a specific distance that made the specific agency problem acute, and the specific governance instruments the specific companies developed comprise the specific earliest systematic attempts at its solution. The specific treatments in [Steensgaard 1974][book_steensgaard_1974] The Asian Trade Revolution of the Seventeenth Century, [Stern 2011][book_stern_2011] The Company-State, and [Robins 2006][book_robins_2006] The Corporation That Changed the World document the specific arrangements. The specific relevance to the present case is that the specific chartered form was created precisely to permit a specific enterprise requiring specific capital beyond any specific individual's means to pursue a specific objective across a specific horizon longer than any specific individual investment, which is the specific problem the governance condition restates.

The specific Standard Oil trust and the specific subsequent holding-company form illustrate the specific instrument by which a specific controller retains a specific unified direction across a specific dispersed ownership. The specific treatment in [Chernow 2004][book_chernow_2004] Titan documents the specific arrangement, and the specific antitrust response is treated in [Bork 1978][book_bork_1978] The Antitrust Paradox, [Posner 2001][book_posner_2001] Antitrust Law, and [Hovenkamp 2005][book_hovenkamp_2005] The Antitrust Enterprise. The specific case establishes that the specific control instruments the article treats have a specific long history of attracting specific regulatory attention when the specific enterprises they govern attain specific market positions, which is a specific hazard the SpaceX configuration will encounter as the specific constellation-deployment position consolidates.

The specific Ford Motor Company supplies the specific longest-running dual-class arrangement in the specific American industrial record. The specific Class B shares held by the specific founding family confer approximately 40 percent of the specific voting power against a specific equity position of a specific few percent, corresponding to

$$w^{\text{Ford}} = \frac{v}{e} \approx \frac{0.40}{0.02} \approx 20$$

which is approximately an order of magnitude above the specific SpaceX figure and which illustrates that the specific wedge magnitude alone carries no specific information about the specific quality of the specific resulting stewardship. The specific treatments in [Ford and Crowther 1922][book_ford_crowther_1922] My Life and Work, [Nevins 1954][book_nevins_1954] Ford, and [Hounshell 1984][book_hounshell_1984] From the American System to Mass Production document the specific origins. The specific case is instructive in both directions. The specific arrangement preserved a specific family direction across approximately a century, and the specific same arrangement has been identified in the specific governance literature as a specific contributor to specific periods of specific underperformance in which a specific external correction was unavailable.

The specific Bell System supplies the specific case of a specific enterprise whose specific long-horizon research programme was financed by a specific regulated monopoly rent rather than by a specific control instrument. The specific treatments in [Gertner 2012][book_gertner_2012] The Idea Factory, [Temin and Galambos 1987][book_temin_galambos_1987] The Fall of the Bell System, [Wu 2010][book_wu_2010] The Master Switch, and [Levin 2010][book_levin_2010] The Wires That Bind document the specific arrangement and its specific dissolution. The specific case establishes that the specific mission-protection function the governance condition performs can be discharged by a specific regulatory arrangement rather than by a specific ownership arrangement, and that the specific regulatory route terminates whenever the specific regulatory settlement changes.

The specific Berkshire Hathaway arrangement supplies a specific contemporary instance of a specific dual-class structure adopted explicitly to preserve a specific investment philosophy against a specific market pressure toward a specific shorter horizon, documented in [Schroeder 2008][book_schroeder_2008] The Snowball. The specific case is analytically close to the specific SpaceX case in its specific stated rationale and distant in its specific business substance.

The specific technology-sector dual-class wave from the specific 2004 period forward established the specific arrangement as a specific sector norm. The specific treatments in [Isaacson 2011][book_isaacson_2011] Steve Jobs, [Stone 2013][book_stone_2013] The Everything Store, [Thiel 2014][book_thiel_2014] Zero to One, [Malone 2014][book_malone_2014] The Intel Trinity, and [Saxenian 1994][book_saxenian_1994] Regional Advantage document the specific sector context. The specific significance of the specific wave for the present article is that it substantially normalized the specific instrument, so that the specific SpaceX configuration required no specific unusual persuasion of the specific investor base at the specific moment it was established.

The specific Xerox case supplies the specific canonical instance of a specific governance failure in the specific opposite direction from the specific cases treated above. The specific corporation possessed a specific research capability of extraordinary depth and a specific conventional governance structure, and the specific structure proved unable to direct the specific capability toward any specific commercial purpose the specific corporation could capture. The specific treatments in [Hiltzik 1999][book_hiltzik_1999] Dealers of Lightning, [Smith and Alexander 1988][book_smith_alexander_1988] Fumbling the Future, and [Kearns and Nadler 1992][book_kearns_nadler_1992] Prophets in the Dark document the specific episode, and the [Value Capture article A284][related_post_a284_spacex_value_capture] treats it as the specific value-capture negation case. The specific governance reading is that a specific dispersed-ownership corporation with a specific professional management and a specific quarterly reporting obligation could not sustain a specific commitment to a specific capability whose specific commercial application lay outside its specific existing business. The specific case establishes that the specific hazard the governance condition addresses is not exclusively the specific hazard of a specific hostile investor. It includes the specific hazard of a specific management structure with no specific party holding a specific durable commitment to anything in particular.

The specific IBM System/360 decision of the specific 1964 period supplies the specific counterpart instance in which a specific large corporation did sustain a specific bet-the-company commitment. The specific treatments in [Pugh Johnson and Palmer 1991][book_pugh_johnson_palmer_1991] IBM's 360 and Early 370 Systems and [Pugh 1995][book_pugh_1995] Building IBM document the specific decision, and the specific [IBM archives][ref_ibm_archives] hold the specific institutional record. The specific governance-relevant feature is that the specific decision was taken under a specific founding-family leadership whose specific position, while not resting on a specific formal dual-class instrument, supplied a specific analogous durability of commitment. The specific case is the specific closest historical analogue to the specific 2017 architectural decision the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats.

The specific RCA trajectory under a specific long-tenured founding executive, documented in [Bilby 1986][book_bilby_1986] The General, supplies a specific further instance of a specific durable personal commitment sustaining a specific long-horizon technical programme, and it supplies equally the specific cautionary sequel in which the specific commitment outlived its specific usefulness and the specific enterprise had no specific mechanism to correct it.

The specific Iridium case supplies the specific instance in which a specific governance structure permitted a specific single irreversible bet at a specific scale the specific market would not support, documented in [Finkelstein and Sanford 2000][research_finkelstein_sanford_2000] Learning from Corporate Mistakes. The specific case is treated in the [Value Gradient article A282][related_post_a282_spacex_value_gradient] and the [Decomposability article A285][related_post_a285_spacex_decomposability] as the specific single-bet contrast, and its specific governance dimension is that no specific party in the specific structure held both the specific information and the specific incentive to halt the specific programme.

The specific research-university and specific national-laboratory forms supply the specific institutional precedent for a specific long-horizon research enterprise governed without a specific residual claimant at all. The specific treatments in [Selznick 1949][book_selznick_1949] TVA and the Grass Roots, [Hargrove 1994][book_hargrove_1994] Prisoners of Myth, [Norberg and O'Neill 1996][book_norberg_oneill_1996] Transforming Computer Technology, and [Bonvillian 2018][research_bonvillian_2018] on the specific DARPA institutional configuration document the specific arrangements. The specific goal-displacement failure mode that [Selznick 1949][book_selznick_1949] names is the specific canonical statement of what the governance condition seeks to prevent, and the specific fact that it was named in a specific study of a specific public agency rather than of a specific firm establishes that the specific hazard is not specific to the specific capital market.

The specific precedent set admits summary through a specific comparison of the specific hazard rates governing the specific loss of the specific configuration. Let $h_c(t)$ denote the specific instantaneous hazard for the specific class $c$. The specific ordering the specific record supports is

$$h^{\text{foundation}} < h^{\text{family dual class}} < h^{\text{founder dual class}} < h^{\text{regulated monopoly}}$$

with the specific foundation arrangements exhibiting the specific flattest hazard because the specific controlling entity does not die, and the specific regulated-monopoly arrangement exhibiting the specific steepest because the specific configuration depends on a specific political settlement that any specific administration can revisit. The specific SpaceX configuration sits in the specific third position, and the specific distance between the specific third and the specific first is the specific successor problem.

## Historiographical Gap and Recent Scholarship

The scholarly literature on the specific SpaceX governance configuration is substantially thinner than the literature on any specific other condition in the seven-plus-three framework, and the specific thinness has a specific structural cause rather than a specific accidental one. The specific corporate-governance literature is overwhelmingly an empirical literature built on specific public-company disclosure, and a specific firm that has never listed supplies substantially none of the specific data the specific literature's methods require.

### Primary Source Documentation

The specific primary source documentation comprises the specific [Delaware General Corporation Law][ref_dgcl] provisions authorizing the specific instruments, the specific [Texas Business Organizations Code][ref_texas_boc] provisions relevant to the specific reported reincorporation, the specific [Delaware Court of Chancery][ref_delaware_chancery] record including the specific compensation litigation the Tesla comparison treats, the specific [Securities and Exchange Commission EDGAR][ref_sec_edgar] system, the specific [Form D][ref_sec_form_d] exempt-offering notices through which the specific private rounds reach the public record, the specific [SpaceX news archive][ref_spacex_news_archive], and the specific [OpenAI charter][ref_openai_charter] and [OpenAI announcements][ref_openai_news] for the specific counter-example. The specific foundation precedents are documented through the specific [Carl Zeiss Stiftung][ref_carl_zeiss_stiftung], [Robert Bosch Stiftung][ref_bosch_stiftung], [Bosch corporate][ref_bosch_company], [Novo Nordisk Foundation][ref_novo_nordisk_foundation], and [Novo Holdings][ref_novo_holdings] records. The specific institutional-investor policy positions on the specific dual-class question are documented through the specific [Council of Institutional Investors][ref_cii].

### Scholarly Infrastructure and Working-Paper Record

A specific feature of the specific corporate-governance field is that a substantial portion of the specific active literature circulates as specific working papers well before specific journal publication, so that a specific survey confined to specific published articles lags the specific field by a specific interval of years. The specific principal repositories are the specific [European Corporate Governance Institute][ref_ecgi] working-paper series, the specific [National Bureau of Economic Research][ref_nber] series, and the specific [Social Science Research Network][ref_ssrn]. The specific practitioner-facing commentary that tracks specific doctrinal developments appears in the specific [Harvard Law School Forum on Corporate Governance][ref_harvard_corpgov_forum] and the specific [Columbia Blue Sky Blog][ref_columbia_blue_sky]. The specific article draws on the specific published literature for its specific claims and notes the specific repositories because a specific reader wishing to extend the specific survey beyond the drafting date will find the specific frontier there rather than in the specific journals.

### Theoretical Corporate-Governance Literature

The specific theoretical literature is mature and is surveyed above in the Cross-Disciplinary Framings section. The specific principal works are [Berle and Means 1932][book_berle_means_1932], [Jensen and Meckling 1976][research_jensen_meckling_1976], [Fama and Jensen 1983][research_fama_jensen_1983], [Grossman and Hart 1986][research_grossman_hart_1986], [Grossman and Hart 1988][research_grossman_hart_1988], [Harris and Raviv 1988][research_harris_raviv_1988], [Hart and Moore 1990][research_hart_moore_1990], [Hart 1995][book_hart_1995], [Shleifer and Vishny 1997][research_shleifer_vishny_1997], [Tirole 2006][book_tirole_2006] The Theory of Corporate Finance, and the specific legal-economic treatments in [Easterbrook and Fischel 1991][book_easterbrook_fischel_1991] and [Roe 1994][book_roe_1994]. The specific gap the literature exhibits with respect to the present case is that substantially the entire theoretical apparatus takes the specific maximization of the specific security value as the specific normative objective, and the specific mission-directed case posits an objective that the specific apparatus can represent only as a specific private benefit of control.

### Empirical Dual-Class Literature

The specific empirical literature comprises [DeAngelo and DeAngelo 1985][research_deangelo_deangelo_1985], [Gompers Ishii and Metrick 2003][research_gompers_ishii_metrick_2003], [Gompers Ishii and Metrick 2010][research_gompers_ishii_metrick_2010], [Bebchuk Kraakman and Triantis 2000][research_bebchuk_kraakman_triantis_2000], and the specific policy argument in [Bebchuk and Kastiel 2017][research_bebchuk_kastiel_2017]. The specific literature's central estimate is that the specific firm value declines in the specific wedge and that the specific decline steepens with the specific time since listing. The specific applicability of the specific estimates to an unlisted firm is unresolved, and the specific direction of the specific selection bias is not obvious. A specific sample of firms that listed with a specific dual-class structure excludes by construction the specific firms whose specific controllers valued control sufficiently to forgo listing entirely, which is the specific population the SpaceX case belongs to.

### Entrepreneurial-Finance and Private-Markets Literature

The specific entrepreneurial-finance literature comprising [Sahlman 1990][research_sahlman_1990], [Gompers 1995][research_gompers_1995], [Lerner 1994][research_lerner_1994_syndication], [Kaplan and Stromberg 2003][research_kaplan_stromberg_2003], [Kaplan and Stromberg 2004][research_kaplan_stromberg_2004], [Gompers and Lerner 2001][book_gompers_lerner_2001], [Metrick and Yasuda 2011][book_metrick_yasuda_2011], and [Lerner 2009][book_lerner_2009] Boulevard of Broken Dreams supplies the specific contracting apparatus. The specific private-markets literature that [Ewens and Farre-Mensa 2020][research_ewens_farre_mensa_2020] represents supplies the specific listing-choice apparatus, and the specific venture-capital effects literature in [Kortum and Lerner 2000][research_kortum_lerner_2000] and [Hall and Lerner 2010][research_hall_lerner_2010] supplies the specific sector-level context. The specific contemporary defense-technology venture wave that the Patient-Private Capital-Formation Leg article A290 will treat has generated a specific emerging literature that remains substantially in the specific trade and practitioner registers.

### Foundation-Ownership and Alternative-Form Literature

The specific literature on the specific foundation-owned firm is small, and [Hansmann 1996][book_hansmann_1996] The Ownership of Enterprise remains the specific principal theoretical treatment of the specific broader class of firms with attenuated residual claims. The specific empirical literature on the specific Danish and specific German industrial foundations is substantially European and substantially recent. The specific gap is notable because the specific arrangements supply the specific only long-run evidence bearing on the specific central question the present article poses.

### Comparative and Non-United-States Literature

The specific comparative literature is substantial and is systematically underused in the specific United States governance debate. The specific developmental-state tradition comprising [Johnson 1982][book_johnson_1982] MITI and the Japanese Miracle, [Amsden 1989][book_amsden_1989] Asia's Next Giant, [Wade 1990][book_wade_1990] Governing the Market, [Evans 1995][book_evans_1995] Embedded Autonomy, [Woo-Cumings 1999][book_woo_cumings_1999] The Developmental State, and [Chang 2002][book_chang_2002] Kicking Away the Ladder documents the specific arrangements under which specific other states have sustained specific long-horizon industrial programmes, and the specific contemporary extensions appear in [Block 2008][research_block_2008] and [Weiss and Thurbon 2021][research_weiss_thurbon_2021]. The specific European corporate-law materials comprising the specific [United Kingdom Companies Act 2006][ref_uk_companies_act_2006], the specific [German Aktiengesetz][ref_german_aktiengesetz], and the specific [European Union Shareholder Rights Directive][ref_eu_shareholder_rights_directive] establish that the specific instrument this article treats is substantially a specific United States artifact, and the specific [OECD Principles of Corporate Governance][ref_oecd_corporate_governance] supply the specific comparative benchmark. The specific institutional-economics frame in [North 1990][book_north_1990], [Ostrom 1990][book_ostrom_1990], [Greif 2006][book_grief_2006], and [Acemoglu and Robinson 2012][book_acemoglu_robinson_2012] situates the specific national variation within the specific broader question of institutional selection.

### Methodological Literature on Case-Study and Counterfactual Inference

The specific methodological problem is more severe here than elsewhere in the series, because the specific central claim concerns an event that did not occur. The specific case-study methodology literature comprising [Yin 2014][book_yin_2014] Case Study Research and Applications and [Creswell 2014][book_creswell_2014] Research Design supplies the specific standards. The specific standard the article attempts to meet is the specific explicit statement of the specific rival explanations together with the specific identification of observations that would discriminate among them, and the article reports that no such observation is available for its central claim. The specific paradigm literature in [Kuhn 1962][book_kuhn_1962] and the specific evolutionary treatments in [Nelson and Winter 1982][book_nelson_winter_1982] and [Metcalfe 1998][book_metcalfe_1998] supply the specific selection caution, and the specific complexity and failure treatments in [Kauffman 1993][book_kauffman_1993], [Ormerod 2005][book_ormerod_2005] Why Most Things Fail, and [Beinhocker 2006][book_beinhocker_2006] The Origin of Wealth supply the specific base-rate framing within which a specific single surviving configuration should be interpreted.

### Adjacent Literature on Mission-Directed and Public-Purpose Organizations

The specific literature on organizations constituted to pursue a specific purpose other than a specific financial return bears directly on the specific question and is largely disjoint from the specific corporate-governance literature. The specific public-private-partnership treatments in [Grimsey and Lewis 2004][book_grimsey_lewis_2004], [Osborne 2000][book_osborne_2000], [Yescombe 2007][book_yescombe_2007], [Hodge and Greve 2007][research_hodge_greve_2007], [Bovaird 2004][research_bovaird_2004] treat the specific hybrid forms. The specific public-agency treatments in [Selznick 1949][book_selznick_1949], [Hargrove 1994][book_hargrove_1994], [Handberg 1994][book_handberg_1994] Reinventing NASA, and [McCurdy 1994][book_mccurdy_1994] Inside NASA treat the specific goal-displacement hazard in organizations with no specific residual claimant at all. The specific finding that the specific hazard appears in substantially every organizational form is the specific reason the article treats the governance condition as a specific general problem rather than as a specific artifact of the specific capital market.

### Critical and Skeptical Literature

A specific critical literature treats the specific control configurations the article describes as a specific entrenchment of a specific unaccountable elite rather than as a specific protection of a specific mission. The specific position is stated most directly in [Bebchuk and Kastiel 2017][research_bebchuk_kastiel_2017] within the specific governance literature, and in the specific broader political-economy register in [Melman 1970][book_melman_1970] Pentagon Capitalism, [Foster and McChesney 2011][book_foster_mcchesney_2011] The Endless Crisis, [Srnicek 2017][book_srnicek_2017] Platform Capitalism, [Zuboff 2019][book_zuboff_2019] The Age of Surveillance Capitalism, and [Khan 2017][research_khan_2017] Amazon's Antitrust Paradox. The specific concern the specific literature raises with respect to the present case is not the specific mission but the specific concentration, because a specific configuration that resists specific capital capture equally resists every specific other form of external accountability, including the specific forms that a specific society might have specific reason to want. The specific article regards the specific concern as well founded and does not resolve it.

### Trade Press and Journalistic Record

The specific governance record reaches the public substantially through the specific business press rather than through the specific disclosure system. The specific coverage appears in [Bloomberg][ref_bloomberg], the [New York Times][ref_nyt], the [Wall Street Journal][ref_wsj], the [Washington Post][ref_washington_post], [SpaceNews][ref_spacenews], [Ars Technica space coverage][ref_arstechnica_space], [Payload][ref_payload], and [Payload Research][ref_payload_research]. The specific dependence of the specific analytical record on the specific journalistic record is a specific methodological weakness the article states rather than conceals.

## Contemporary Comparative Landscape

The contemporary landscape for the governance condition across the specific sector and the specific adjacent technology sector exhibits a specific range of configurations.

Blue Origin occupies a specific configuration that satisfies the governance condition by a specific different route. The specific firm has been substantially funded by a specific single individual without a specific external capital raise at scale, so that the specific capture hazard does not arise because no specific external claimant exists. The specific configuration admits the compact statement

$$e^{\text{founder}} \approx v^{\text{founder}} \approx 1 \qquad \text{so} \qquad w \approx 1 \quad \text{with} \quad C^{\text{contest}} = \infty$$

with the specific contestability infinite despite a specific unit wedge. The specific route is available only to a specific founder whose specific independent resources are commensurate with the specific mission's specific capital requirement, and the Portfolio-Patience article A288 will treat the specific consequences of the specific route for the specific pace of the specific development. The specific record is available through the specific [Blue Origin press releases][ref_blue_origin_press].

Rocket Lab operates as a specific publicly listed company under a specific conventional single-class structure, and therefore satisfies none of the specific governance condition's requirements. The specific configuration is the specific control condition of the sector, in the sense that it is what a specific space-launch firm looks like when it raises specific public capital on specific ordinary terms. The specific record is available through the specific [Rocket Lab press releases][ref_rocket_lab_press].

The United Launch Alliance occupies the specific limiting case in the specific opposite direction. The specific entity is a specific joint venture of two specific incumbent parents, so that the specific control resides entirely with specific parties whose specific principal businesses lie elsewhere. The specific configuration is the specific pure form of what the governance condition is intended to prevent, and the specific consequences for the specific investment horizon are visible in the specific vehicle-development record the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats. The specific record is available through the specific [United Launch Alliance news][ref_ula_press].

The specific adjacent technology sector supplies the specific richer comparative material. The specific dual-class structures adopted at scale across the specific 2004 period forward have made the specific instrument a sector norm, and the specific range of wedges observed spans from approximately unity to values well above the specific SpaceX figure. The specific comparator disclosures appear in the specific [Alphabet investor materials][ref_alphabet_ir], the specific [Meta investor materials][ref_meta_ir], the specific [Snap investor materials][ref_snap_ir], the specific [Ford investor materials][ref_ford_ir], and the specific [Berkshire Hathaway shareholder materials][ref_berkshire], and the specific listed structures supply the specific only fully documented wedges available for comparison because the specific disclosure obligation that produces them is the specific obligation the SpaceX configuration avoids. The specific artificial-intelligence sector has produced two specific contemporary experiments in structures that go beyond the specific voting instrument. The specific OpenAI arrangement the counter-example section treats attempted control by a specific nonprofit board and failed. A specific further experiment places a specific portion of the specific board-election authority with a specific trust constituted to represent specific long-term interests rather than specific shareholder interests, described in the specific [long-term benefit trust announcement][ref_anthropic_ltbt]. The specific investor relationships in the specific sector are documented in part through the specific [Microsoft news archive][ref_microsoft_news]. The specific arrangement is too recent for any specific assessment, and the specific analytical question it raises is precisely the specific one the OpenAI episode answers unfavorably, namely whether a specific formal authority unaccompanied by a specific resource position can prevail when tested.

The specific broader private-market landscape supplies the specific relevant base rate. The specific expansion of the specific private capital pool that [Ewens and Farre-Mensa 2020][research_ewens_farre_mensa_2020] document has produced a specific cohort of firms that reach substantial scale without listing, and the specific venture-capital literature in [Gompers and Lerner 2001][book_gompers_lerner_2001], [Metrick and Yasuda 2011][book_metrick_yasuda_2011], [Lerner 2009][book_lerner_2009], [Kortum and Lerner 2000][research_kortum_lerner_2000], and [Hall and Lerner 2010][research_hall_lerner_2010] documents the specific institutional apparatus that supports them. The specific practitioner literature in [Thiel 2014][book_thiel_2014] Zero to One, [Ries 2011][book_ries_2011] The Lean Startup, [Blank 2013][book_blank_2013] The Four Steps to the Epiphany, and [Moore 1991][book_moore_1991] Crossing the Chasm has substantially normalized the specific founder-control preference within the specific sector, and the specific regional-institutional treatments in [Saxenian 1994][book_saxenian_1994] Regional Advantage, [Kenney 2000][book_kenney_2000] Understanding Silicon Valley, [Lecuyer 2006][book_lecuyer_2006] Making Silicon Valley, and [Klepper 2016][book_klepper_2016] Experimental Capitalism document the specific conditions under which the specific preference became enforceable.

The specific institutional-investor and specific index-provider response constitutes a specific countervailing force that the specific landscape must include. The specific [Council of Institutional Investors][ref_cii] has advocated specific one-share-one-vote policies and specific mandatory sunset provisions in its specific [dual-class stock position][ref_cii_dual_class], the specific proxy advisers whose recommendations shape specific institutional voting publish their specific policies through [ISS][ref_iss_governance] and [Glass Lewis][ref_glass_lewis], and specific index providers including [S&P Dow Jones Indices][ref_spdji] and [FTSE Russell][ref_ftse_russell] have at various points restricted the specific inclusion of specific multi-class issuers. The specific corporate-governance practice literature that the specific [Conference Board][ref_conference_board] publishes documents the specific diffusion of the specific policies. The specific pressure operates only on specific listed firms, which is a specific further reason the specific unlisted configuration is attractive to a specific controller who values control. The specific effect admits the compact statement that the specific governance-pressure gradient runs

$$P^{\text{pressure}}\!\left( \text{listed, single class} \right) > P^{\text{pressure}}\!\left( \text{listed, dual class} \right) \gg P^{\text{pressure}}\!\left( \text{unlisted} \right)$$

with the specific unlisted configuration substantially outside the specific reach of the specific instruments the specific institutional investors have developed. The specific comparison set arrayed by the specific wedge admits the compact form

$$w^{\text{ULA}} \approx w^{\text{Rocket Lab}} \approx 1 \; < \; w^{\text{SpaceX}} \approx 1.9 \; < \; w^{\text{Novo}} \approx 2.8 \; \ll \; w^{\text{Bosch trust}} \approx 9300$$

with the specific ordering establishing that the specific SpaceX wedge is unremarkable by the specific standards of the specific arrangements that have demonstrated the specific longest persistence. The specific analytically operative variable is therefore not the specific wedge magnitude but the specific combination of the specific wedge with the specific financing channel and the specific successor provision.

## Comparative Cross-Sectional Analysis

The governance condition admits application to the specific organization set as a specific cross-sectional scoring exercise across the specific five sub-properties the pattern-extraction section states. The specific closure vector admits the compact form

$$\boldsymbol{\phi}_j^{\text{governance}} \in \{0, 1\}^{5}$$

with each specific organization's specific vector indicating the specific satisfaction status across the specific formal-instrument, specific effective-alignment, specific financing-channel, specific successor-commitment, and specific mission-specificity sub-properties.

SpaceX exhibits specific closure on the specific formal-instrument, specific effective-alignment, specific financing-channel, and specific mission-specificity sub-properties, and specific non-closure on the specific successor-commitment sub-property. The specific single non-closure is the specific analytically important finding of the exercise, because it identifies the specific respect in which the specific configuration differs from the specific centurial precedents rather than the specific respect in which it resembles them.

Blue Origin exhibits specific closure on the specific effective-alignment, specific financing-channel, and specific mission-specificity sub-properties, with the specific formal instrument unnecessary and the specific successor commitment absent. OpenAI exhibited specific closure on the specific formal-instrument and specific mission-specificity sub-properties and specific non-closure on the specific effective-alignment sub-property, and the specific non-closure was decisive. The specific foundation-owned precedents exhibit specific closure on all five, and they are the specific only organizations in the specific comparison set that do. The specific publicly listed single-class firms exhibit specific closure on none.

The specific cross-sectional pattern indicates that the specific formal-instrument sub-property is the specific easiest to satisfy and the specific successor-commitment sub-property the specific hardest, and that the specific two are substantially uncorrelated across the specific set. The specific correlation structure admits the compact statement

$$\operatorname{corr}_j\!\left( \phi_{j,1}^{\text{formal}}, \; \phi_{j,4}^{\text{successor}} \right) \approx 0$$

with the specific adoption of a specific voting instrument carrying substantially no information about whether the specific arrangement will survive the specific controller. The specific finding is the specific reason the article treats the specific successor question as the specific principal open question rather than as a specific detail.

## Data Sources and Reconstruction Methodology

The article draws on specific primary and specific secondary sources to reconstruct the governance trajectory, and it confronts a specific evidentiary situation substantially worse than that of any other article in the series.

The specific primary-source layer comprises the specific statutory and specific case-law materials identified in the Historiographical Gap section, the specific exempt-offering notices that reach the specific public record, the specific corporate communications of the specific firm and the specific comparison organizations, and the specific foundation documentation for the specific centurial precedents. The specific statutory and specific foundation materials are complete and authoritative. The specific SpaceX-specific materials are neither.

The specific secondary-source layer comprises the specific biographical and specific trade-press record identified above.

The specific reconstruction methodology proceeds by triangulation. The specific ownership and voting figures are assembled from specific trade-press reports of specific round terms, specific litigation disclosures in unrelated matters, and specific investor communications that reach the specific public indirectly. Where the specific sources disagree the article reports the specific range rather than selecting a specific point estimate. Where a specific figure is reported by a specific single source without corroboration the article marks it as such.

The specific empirical-record limitations are severe and are stated explicitly rather than managed. The specific firm publishes no specific financial statements, no specific ownership schedule, no specific charter, and no specific bylaws. The specific share classes and the specific per-class voting ratios are not public. The specific board composition is not published. The specific protective provisions negotiated in the specific successive rounds are not public. The specific consequence is that substantially every specific quantitative claim in this article about the specific SpaceX capital structure carries a specific wider uncertainty than the specific corresponding claims in the specific preceding articles of the series, and the specific reader should discount them accordingly. The specific qualitative claim that the specific founder retains a specific voting majority is corroborated across substantially all specific available sources and is the specific single claim the article treats as well established.

## Alternative Analytical Frameworks

The governance framing the article develops is one of several analytical frameworks the surrounding literature applies to the specific configuration.

The agency framing developed in [Jensen and Meckling 1976][research_jensen_meckling_1976], [Fama and Jensen 1983][research_fama_jensen_1983], and [Shleifer and Vishny 1997][research_shleifer_vishny_1997] is the specific principal alternative and treats the specific configuration as a specific entrenchment that raises the specific residual loss. The framing predicts specific value destruction increasing in the specific wedge and the specific tenure, and it predicts specific expropriation of the specific minority through specific related-party transactions and specific perquisite consumption. The specific available record does not permit a specific test of the specific prediction, because the specific transactions the specific prediction concerns are precisely the specific transactions a specific unlisted firm does not disclose. The specific prediction admits the compact form

$$V\!\left( w, \tau \right) = V^{\ast} - \beta_1 w - \beta_2 w \tau, \qquad \beta_1, \beta_2 > 0$$

with the specific value declining in the specific wedge and the specific decline compounding with the specific tenure. The framing is not refuted by the specific SpaceX record. It is untested by it.

The stewardship framing treats the specific controller as a specific steward whose specific objective is aligned with the specific long-run enterprise rather than as a specific agent whose specific objective diverges from it, and it predicts that a specific control configuration insulating the specific steward improves rather than degrades the specific outcome. The specific stewardship premise admits the compact statement as a specific restriction on the specific objective

$$U^{\text{controller}} = U^{\text{enterprise}} \qquad \text{against the agency premise} \qquad U^{\text{controller}} = e \cdot U^{\text{enterprise}} + B^{\text{private}}$$

with the specific two framings differing in whether the specific private-benefit term is present rather than in any specific empirical claim about the specific observed behavior. The framing is the specific mirror image of the specific agency framing and shares its specific weakness, in that both derive their specific predictions from a specific assumption about the specific controller's objective that the specific evidence is asked to confirm rather than to establish.

The resource-dependence framing, whose specific organizational-sociology antecedents appear in [Selznick 1949][book_selznick_1949] TVA and the Grass Roots and whose specific market-architecture development appears in [Fligstein 2001][book_fligstein_2001] The Architecture of Markets, treats the specific effective control as determined by the specific pattern of dependencies rather than by the specific formal authority. The specific dependence-weighted control admits the compact form

$$v^{\text{effective}}_i = \frac{d_i \, \sigma_i}{\sum_j d_j \, \sigma_j}$$

with $d_i$ the specific criticality of the specific resource the specific party supplies and $\sigma_i$ the specific credibility of the specific withdrawal threat, and with the specific formal votes entering only insofar as they constitute one specific resource among others. The framing supplies the specific analytical apparatus that the OpenAI counter-example requires and that the specific voting-rights literature lacks entirely, and the article adopts it as a specific supplement rather than as a specific alternative.

The managerial-power framing treats the specific governance arrangements as themselves the specific product of the specific power they purport to constrain, and it reads the specific dual-class instrument as a specific outcome of a specific bargaining process in which the specific founder's specific bargaining power was decisive. The framing is consistent with the specific bargaining apparatus the Cross-Disciplinary Framings section develops and it supplies a specific deflationary reading under which the specific configuration reflects nothing beyond the specific relative scarcity of specific credible mission-directed founders against specific abundant capital.

The political-economy and rent-seeking framing developed in [Buchanan and Tullock 1962][book_buchanan_tullock_1962], [Stigler 1971][research_stigler_1971], and [Krueger 1974][research_krueger_1974] treats the specific configuration as one element of a specific broader arrangement in which a specific concentrated private interest obtains specific favorable treatment from a specific state customer. The framing raises the specific accountability concern that the critical literature states, and it observes correctly that the specific governance condition as the article formulates it is entirely silent on the specific question of accountability to any specific party other than the specific capital providers.

The behavioral framing developed in [Kahneman and Tversky 1979][research_kahneman_tversky_1979], [Tversky and Kahneman 1992][research_tversky_kahneman_1992], [Kahneman 2011][book_kahneman_2011], [Staw 1976][research_staw_1976], and [Ross and Staw 1993][research_ross_staw_1993] treats the specific insulated controller as specifically exposed to the specific escalation and specific overconfidence hazards that a specific external correction would otherwise check. The specific escalation hazard admits the compact form

$$P\!\left( \text{continue} \mid \text{negative signal} \right) = g\!\left( c^{\text{sunk}}, \; r^{\text{public commitment}}, \; 1 - \eta^{\text{external check}} \right)$$

increasing in the specific sunk cost, in the specific publicity of the specific prior commitment, and in the specific absence of the specific external check. The specific configuration the article describes sets the specific third argument near its specific maximum by construction. The framing supplies the specific most concrete statement of the specific cost the configuration incurs, and it is the specific framing under which the specific Space Shuttle and specific Constellation program records that the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] treats are read as specific evidence that the specific external correction is itself unreliable.

The real-options framing developed in [Dixit and Pindyck 1994][book_dixit_pindyck_1994] and [Trigeorgis 1996][book_trigeorgis_1996] treats the specific retained control as a specific option to redirect the specific enterprise in specific contingencies not yet realized, and it values the specific configuration by the specific option value rather than by the specific expected cash flows. The specific option value admits the compact form

$$V^{\text{control}} = \sum_{s \in \mathcal{S}} p(s) \cdot \left[ \max_{a \in \mathcal{A}} V(a, s) - V\!\left( a^{\text{default}}, s \right) \right]^{+}$$

with the specific value equal to the specific probability-weighted gain from being able to choose the specific action rather than accepting the specific default across the specific contingency set. The specific value rises with the specific dispersion of the specific contingencies, which is why the specific control premium is largest precisely where the specific programme is least predictable. The framing supplies the specific formal account of why a specific controller facing a specific highly uncertain long-horizon programme values control disproportionately to any specific individual decision the specific control would be used to make.

The legal-origins and comparative-governance framing developed in [La Porta Lopez-de-Silanes Shleifer and Vishny 1998][research_laporta_et_al_1998], [Roe 1994][book_roe_1994], and [Easterbrook and Fischel 1991][book_easterbrook_fischel_1991] treats the specific configuration as a specific artifact of the specific permissive United States chartering regime and observes that the specific arrangement would be unavailable or substantially constrained in specific other jurisdictions. The framing correctly identifies the specific configuration as contingent on a specific legal settlement that is itself contested and revisable.

The financial-sociology framing developed in [MacKenzie 2006][book_mackenzie_2006], [Ho 2009][book_ho_2009], [Zaloom 2006][book_zaloom_2006], [Preda 2009][book_preda_2009], and [Krippner 2011][book_krippner_2011] treats the specific short-horizon pressure the configuration is designed to resist as a specific institutionally constructed artifact rather than as a specific natural property of specific dispersed ownership, and it raises the specific possibility that the specific problem the governance condition solves is a specific problem a specific differently organized capital market would not present.

The resource-based and dynamic-capabilities framing developed in [Wernerfelt 1984][research_wernerfelt_1984], [Barney 1991][research_barney_1991], [Teece Pisano and Shuen 1997][research_teece_pisano_shuen_1997], and [Teece 2007][research_teece_2007] treats the specific control configuration as one specific resource among the specific bundle that produces the specific competitive position, and it predicts that the specific configuration is valuable in proportion to the specific specificity of the specific other assets it governs. The framing supplies the specific reason the specific configuration matters more here than at a specific firm whose specific assets are redeployable, and it supplies equally the specific prediction that the specific configuration's value declines as the specific capability base becomes more general, which is precisely the specific direction the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] documents.

The platform and two-sided-market framing developed in [Rochet and Tirole 2003][research_rochet_tirole_2003], [Rochet and Tirole 2006][research_rochet_tirole_2006], [Parker and Van Alstyne 2005][research_parker_vanalstyne_2005], [Eisenmann Parker and Van Alstyne 2006][research_eisenmann_et_al_2006], [Armstrong 2006][research_armstrong_2006], [Rysman 2009][research_rysman_2009], [Gawer and Cusumano 2014][research_gawer_cusumano_2014], [Hagiu and Wright 2015][research_hagiu_wright_2015], [Cusumano and Gawer 2002][book_cusumano_gawer_2002] Platform Leadership, and [Van Alstyne Parker and Choudary 2016][book_vanalstyne_parker_choudary_2016] Platform Revolution treats the specific enterprise as a specific platform whose specific governance affects the specific willingness of specific complementors to invest. The framing raises a specific consideration the shareholder-centered literature omits entirely, namely that a specific concentrated and durable control may be attractive rather than threatening to a specific complementor who requires assurance that the specific platform rules will not change.

The path-dependence framing developed in [David 1985][research_david_1985] Clio and the Economics of QWERTY and [Arthur 1989][research_arthur_1989] Competing Technologies Increasing Returns and Lock-In treats the specific configuration as a specific early choice whose specific persistence reflects specific accumulated switching costs rather than specific continuing optimality, and the specific industry-life-cycle treatment in [Klepper 1996][research_klepper_1996] and [Klepper 2010][research_klepper_2010] supplies the specific sector-level analogue.

The actor-network framing developed in [Latour 1987][book_latour_1987], [Callon 1986][research_callon_1986] Some Elements of a Sociology of Translation, and [Law 1987][research_law_1987] Technology and Heterogeneous Engineering treats the specific control as an achievement continuously reproduced through the specific enrollment of specific human and specific non-human actors rather than as a specific property conferred by a specific document. The framing supplies the specific most complete account of the specific OpenAI episode, in which a specific formal document conferred an authority that the specific network declined to enact.

The evolutionary and selection framing developed in [Nelson and Winter 1982][book_nelson_winter_1982] and [Metcalfe 1998][book_metcalfe_1998] supplies the specific caution that the specific observed configuration is a specific survivor and that the specific population of specific founder-controlled ventures whose specific controllers persisted in specific mistaken courses until the specific enterprise failed is substantially unobserved.

## Pattern Extraction

The governance pattern that the SpaceX case exhibits admits the following abstract statement without naming any specific downstream application. A mission-directed technology venture achieves the governance closure when the venture can absorb the specific quantity of external capital its mission requires across the specific duration its mission requires without transferring to the specific capital providers the authority to alter what the mission is.

The abstract governance mechanic requires joint satisfaction of five sub-properties, admitting the compact conjunctive form

$$\Phi^{\text{governance}} = \prod_{k=1}^{5} \phi_k, \qquad \phi_k \in \{0,1\}$$

with the specific closure obtaining only when every specific sub-property indicator takes the specific value unity.

First, the venture must possess a specific formal instrument that decouples the specific voting rights from the specific cash-flow rights, so that the specific control condition survives an arbitrary specific dilution sequence.

Second, the specific effective control must align with the specific formal control. The specific party holding the specific votes must also occupy a specific position in the specific resource-dependence structure such that the specific exercise of the specific formal authority does not destroy the specific organization's capacity to act. A specific formal authority held by a specific party on whom the specific organization does not depend is not a specific control.

Third, the venture must obtain its specific capital through a specific channel that does not itself impose the specific governance obligations the specific instrument is designed to avoid, and it must supply the specific liquidity its specific personnel require by a specific mechanism other than a specific public listing.

Fourth, the specific arrangement must bind the specific controller's successors, or it terminates with the specific controller. The specific transition hazard admits the compact form

$$P\!\left( \text{configuration survives transition} \right) = P\!\left( \text{successor identified} \right) \cdot P\!\left( \text{instrument transfers} \right) \cdot P\!\left( \text{successor sustains mission} \right)$$

with the specific product requiring all three factors and with a specific arrangement lacking any specific formal successor provision setting the specific second factor by default rather than by design. This is the specific sub-property the specific centurial precedents satisfy and the specific SpaceX configuration does not.

Fifth, the specific mission must be specified with sufficient precision that a specific deviation from it is observable. A specific mission stated so broadly that substantially any specific course of action satisfies it supplies no specific constraint, and the specific governance apparatus protecting it protects nothing.

The specific relationship among the specific sub-properties is not symmetric. The specific first is the specific easiest to obtain and receives substantially all of the specific attention in the specific practitioner literature. The specific second is the specific one whose failure the OpenAI case demonstrates and which the specific voting-rights literature does not address. The specific fourth is the specific one that distinguishes an arrangement lasting a specific career from one lasting a specific century.

The specific abstract mechanic admits a specific diagnostic procedure applicable to a specific candidate case in an adjacent domain, stated as an ordered test vector

$$\tau = \left( w > 1, \;\; v^{\text{effective}} \approx v^{\text{formal}}, \;\; G^{\text{channel}} \approx 0, \;\; \exists \, \text{successor binding}, \;\; \text{mission falsifiable} \right)$$

with each specific component evaluating one of the specific five sub-properties. The specific procedure's specific practical value lies in the specific second and fourth components, because a specific candidate case will almost always satisfy the specific first and will almost never be examined on the specific others.

The specific mechanic carries a specific cost that the specific statement should not conceal. A specific configuration that resists specific capital capture resists every specific other form of external correction by the specific same mechanism, and it therefore converts the specific question of whether the specific venture pursues a specific worthwhile mission into a specific question about the specific judgment of a specific individual or a specific small body. The specific mechanic is not a specific guarantee of a specific good outcome. It is a specific transfer of the specific decision about what counts as a specific good outcome from the specific capital market to the specific controller.

## Cross-References to the Series

The article back-references the [series opener][related_post_a281_spacex_framing] for the specific seven-plus-three framework introduction and the specific founding narrative. The article back-references the [Value Gradient article A282][related_post_a282_spacex_value_gradient] for the specific reusability development whose specific investment horizon the governance configuration protected. The article back-references the [Anchor Demand article A283][related_post_a283_spacex_anchor_demand] for the specific state-customer relationships that supplied the specific revenue against which the specific private financing was raised. The article back-references the [Value Capture article A284][related_post_a284_spacex_value_capture] for the specific Starlink business whose specific separation question the article treats. The article back-references the [Decomposability article A285][related_post_a285_spacex_decomposability] for the specific vehicle-family structure across which the specific capital was allocated. The article back-references the [Generality-Forcing article A286][related_post_a286_spacex_generality_forcing] for the specific self-financing loop whose specific internal capital allocation the governance configuration makes possible, and for the specific mission-persistence sub-property that the specific article identified as unresolved and that the present article locates in the governance apparatus.

The article forward-references the specific subsequent articles. The Portfolio-Patience article A288 treats the specific internalized portfolio across which the specific controller allocates capital without external review. The Government-Anchor Capital-Formation Leg article A289, the Patient-Private Capital-Formation Leg article A290, and the Category-Dominating Commercial Spinoff article A291 treat the specific three financing channels whose specific governance terms the present article analyzes. The closing article A292 synthesizes across the framework.

The article cross-references the existing published corpus including the [Introduction to Space Studies article A90][related_post_a90_intro_space_studies], the [History of Rocketplanes article A96][related_post_a96_history_rocketplanes], the [What Does the United States Space Force Do article A97][related_post_a97_us_space_force], the [Framing and the Co-Development Mechanism article A237][related_post_a237_aerospace_framing], the [Silicon Valley from Defense Contracting article A246][related_post_a246_silicon_valley_defense], the [Software-Defined Aerospace article A247][related_post_a247_software_defined_aerospace], the [Contemporary Snapshot article A248][related_post_a248_contemporary_snapshot], the [What a Patent Is and Is Not article A161][related_post_a161_patent_intro], the [Patents Trade Secrets and the Disclosure Tradeoff article A164][related_post_a164_patents_trade_secrets], and the [Why Startups Actually Fail article A167][related_post_a167_startup_failure].

## Terminological Note

The article adopts specific terminology consistent with the corporate-governance conventions and departs from them where the specific departure is analytically necessary. The term "control" refers to the specific authority to determine the specific composition of the specific board and thereby the specific ordinary business of the specific enterprise, and not to the specific unconditional authority to take any specific action. The term "wedge" refers to the specific ratio of the specific voting share to the specific cash-flow share. The term "capital capture" refers to a specific change in the specific mission objective attributable to the specific preferences of the specific capital providers, and it is distinguished from the specific expropriation that the agency literature treats, which concerns the specific transfer of value rather than the specific redirection of purpose. The term "formal control" refers to the specific authority the specific governing documents confer, and the term "effective control" refers to the specific authority that survives its own exercise. The term "sunset provision" refers to a specific charter term under which a specific superior voting class converts to a specific ordinary class upon a specific triggering event or the specific passage of a specific interval. The term "foundation ownership" refers to an arrangement in which a specific entity without specific personal residual claimants holds the specific controlling interest.

## Load-Bearing Open Questions

The article closes with the specific load-bearing open questions the governance treatment leaves unresolved. First, the specific central claim that the specific control configuration prevented a specific capture that would otherwise have occurred is not demonstrable, because no specific capture attempt is recorded and the specific counterfactual is unobservable. Second, the specific quantitative capital-structure claims rest on specific reconstructive estimates that the specific private-firm status precludes verifying. Third, the specific successor question is entirely unresolved, and the specific configuration at the drafting date supplies no specific mechanism by which the specific arrangement survives the specific controller. Fourth, the specific relationship between the specific governance configuration and the specific accountability of the specific enterprise to specific parties other than its specific capital providers is not addressed by the specific condition as formulated, and the specific critical literature is correct that the specific omission is substantive rather than incidental. Fifth, the specific applicability of the specific empirical dual-class findings to a specific unlisted firm is unresolved in both directions, and the specific selection structure of the specific available samples makes the specific direction of the specific bias genuinely uncertain. Sixth, the specific effect of a specific Starlink separation on the specific configuration is unknown and would constitute the specific first substantial test of the specific arrangement.

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
[related_post_a90_intro_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[related_post_a96_history_rocketplanes]: {% post_url 2026-02-27-history_of_rocketplanes %}
[related_post_a97_us_space_force]: {% post_url 2026-02-28-what_does_united_states_space_force_do %}
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
