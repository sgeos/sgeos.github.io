---
layout: post
mathjax: true
comments: true
title: "Building an Integrated Enterprise from Distressed Acquisitions"
date: 2026-08-15 09:00:00 +0000
categories: business economics finance
---

<!-- A379 -->
<script>console.log("A379");</script>

A firm is vertically integrated when it owns successive stages of a supply chain,
such as a supplier and the manufacturer that buys from it
[Vertical Integration][ref_vertical_integration],
and horizontally integrated when it combines firms at the same stage of production
[Horizontal Integration][ref_horizontal_integration].
One way to assemble such a firm is to buy the pieces,
and one way to buy them cheaply is to buy them while they are distressed,
bankrupt or forced to sell at a discount,
and then to put their assets to a different use.

This article asks whether that strategy rests on established theory.
The answer is that it rests on four bodies of theory,
each well developed on its own,
and on no theory of the strategy as a whole.
The first concerns which activities belong inside one firm.
The second treats mergers as a market that moves assets toward better users.
The third accounts for distressed assets selling below their value.
The fourth addresses when bought resources can be redeployed.
The article sets out each with a small model and worked numbers,
shows where they reinforce one another and where they conflict,
and reviews what is known about buyers of distressed firms and about serial acquirers.

The companion article on the conglomerate discount covers what happens to value if the businesses combined are unrelated
[What the Conglomerate Discount Measures][related_post_conglomerate_discount].
This article concerns related businesses,
where the combination is meant to create value through the supply chain or through scale.
It does not value any real company,
does not give legal or investment advice,
and does not survey the law of bankruptcy or competition in any jurisdiction.
Every numerical example is hypothetical.

## What Belongs Inside One Firm

Coase asked in 1937 why firms exist at all,
if markets coordinate production through prices
[Coase 1937][research_coase_1937].
The answer the literature built on that question is that using the market has costs,
and that some transactions are cheaper to organize inside a firm
[Theory of the Firm][ref_theory_of_the_firm].
Williamson framed vertical integration as a response to market failure,
against a policy view that treated it mainly as a strategic device with anticompetitive effects
[Williamson 1971][research_williamson_1971].
Klein, Crawford and Alchian connected integration to appropriable rents,
the value that one party to a specialized relationship can capture from the other once investments are sunk
[Klein et al. 1978][research_klein_crawford_alchian_1978].
The resulting risk is known as the hold-up problem
[Hold-up Problem][ref_hold_up_problem].

### A Model of Hold-up

A small model shows why hold-up favours integration.
A supplier can make an investment $I$ that is specific to one buyer,
with all values in the same arbitrary money units.
The investment creates value $2k\sqrt{I}$ for the relationship,
where $k$ is a positive constant that scales the value of the investment.
The investment is efficient where its marginal value equals its marginal cost of one,
which gives the first-best level and surplus.

$$
I^{*} = k^{2},
\qquad
S^{*} = 2k\sqrt{I^{*}} - I^{*} = k^{2}
$$

If the parties cannot write a complete contract in advance,
the value is bargained over after the investment is sunk.
Suppose the supplier then receives half of it.
The supplier invests to maximize its own share net of cost,
which lowers the investment and the total surplus.

$$
\max_{I}\; k\sqrt{I} - I
\;\;\Rightarrow\;\;
I^{h} = \frac{k^{2}}{4},
\qquad
S^{h} = 2k\sqrt{I^{h}} - I^{h} = \frac{3k^{2}}{4}
$$

With $k = 10$,
the first-best investment is 100 and the surplus 100,
while under hold-up the investment falls to 25 and the surplus to 75.
A quarter of the surplus is lost to underinvestment.
If owning the supplier removes the hold-up but costs $G$ per period in administration and weaker incentives,
integration pays if $G < 25$.
The loss rises with the square of $k$,
so integration pays most where specific investment matters most.

### Ownership Has Costs Too

The model treats integration as a fixed cost.
Property rights theory locates where that cost comes from.
Grossman and Hart distinguish specific contractual rights from residual rights of control over assets,
and define ownership as the purchase of the residual rights.
When one party buys them the other loses them,
which distorts the incentives of the party that sold.
Firm 1 should buy firm 2 if its gain in productivity from control exceeds firm 2's loss from giving control up
[Grossman and Hart 1986][research_grossman_hart_1986].
Hart and Moore identify a firm with the assets its owners control,
and they show how changes in ownership alter the incentives of employees as well as of owner-managers
[Hart and Moore 1990][research_hart_moore_1990].
The implication this article draws for an acquirer is that buying a supplier transfers control
and can weaken the incentives of the people who made the supplier valuable.

### What the Evidence Shows

Lafontaine and Slade review the empirical work on which transactions are brought inside firms
and on what integration does to prices, quantities, investment and profits
[Lafontaine and Slade 2007][research_lafontaine_slade_2007].
Several studies complicate the simple picture of integration as a way to secure supply.
Atalay, Hortaçsu and Syverson find that roughly half of upstream establishments report no shipments to downstream establishments within the same firm.
They argue that vertical ownership promotes transfers of intangible inputs,
and they find that an acquired establishment begins to resemble its acquirer along several dimensions after the change of ownership
[Atalay et al. 2014][research_atalay_hortacsu_syverson_2014].
In cement and ready-mixed concrete,
Hortaçsu and Syverson see little sign that integration forecloses rivals.
Prices fall and quantities rise as markets become more integrated,
and the productivity advantage of integrated producers comes from the logistics of large local concrete operations,
which non-vertical firms with similar operations share
[Hortaçsu and Syverson 2007][research_hortacsu_syverson_2007].
Major airlines, according to Forbes and Lederman,
are more likely to own the regional carriers that fly routes where adaptation decisions are frequent and costly,
consistent with ownership economizing on renegotiation
[Forbes and Lederman 2009][research_forbes_lederman_2009].
Aghion, Griffith and Howitt report a U-shaped relation between product market competition and vertical integration
[Aghion et al. 2006][research_aghion_griffith_howitt_2006].

In one large sample the stock market rewarded vertical combinations.
Fan and Goyal measure vertical relatedness with industry commodity flows for mergers completed from 1962 to 1996.
Almost a third of the mergers display vertical relatedness,
and their wealth effects are significantly larger than those of diversifying mergers
and comparable to those of purely horizontal mergers
[Fan and Goyal 2006][research_fan_goyal_2006].

## Horizontal Scale and the Efficiency Tradeoff

A horizontal combination can lower costs through scale and raise prices through market power.
Williamson posed the question of how a competition authority should weigh the two
when a merger yields economies but also increases market power
[Williamson 1972][research_williamson_1972].
Regulatory approval is a condition of many such combinations
[Horizontal Integration][ref_horizontal_integration].

A linear approximation shows the shape of the tradeoff.
Let the pre-merger price equal unit cost,
let the merger raise the price by the fraction $x$ and lower unit cost by the fraction $s$,
and let $\eta$ be the absolute price elasticity of demand.
The deadweight loss from the higher price is approximately $\tfrac{1}{2}\eta x^{2}$ of pre-merger revenue,
and the cost saving on the reduced output is approximately $s(1 - \eta x)$ of it.
Total surplus rises if the second exceeds the first.

$$
s > \frac{\eta\, x^{2}}{2\left(1 - \eta x\right)}
$$

With $\eta = 2$,
a price rise of 10 percent requires a cost reduction of only 1.25 percent to leave total surplus unchanged.
A price rise of 5 percent requires 0.28 percent,
and one of 20 percent requires 6.67 percent.
Because the deadweight loss grows with the square of the price rise,
modest cost savings offset modest price increases under a total-surplus standard.
That standard counts the gains to the merging firms as well as the losses to buyers,
and whether a combination is lawful depends on the standard and the practice of the authority with jurisdiction,
which this article does not survey.

## Mergers as a Market for Assets

The second body of theory treats acquisitions as the way assets move to the firms that can use them best.
Jovanovic and Rousseau extend the Q-theory of investment to mergers.
A firm's merger and acquisition investment responds to its Q about 2.6 times as strongly as its direct investment,
and they read the merger waves of 1900, the 1920s, the 1980s and the 1990s as responses to profitable reallocation opportunities,
while the wave of the 1960s was probably caused by something else
[Jovanovic and Rousseau 2002][research_jovanovic_rousseau_2002].
Maksimovic and Phillips find that close to seven percent of plants change ownership in peak expansion years,
that sales depend on the organization and prior efficiency of buyers and sellers,
and that the transactions, especially sales of plants and divisions, tend to improve the allocation of resources
[Maksimovic and Phillips 2001][research_maksimovic_phillips_2001].
Andrade, Mitchell and Stafford report that merger activity clusters by industry,
that deregulation accounted for nearly half of merger activity from the late 1980s,
that the combined announcement return of the merging parties is positive over 1973 to 1998,
and that operating performance improves after mergers relative to industry peers
[Andrade et al. 2001][research_andrade_mitchell_stafford_2001].

That the combined parties gain does not mean the acquirer does.
Roll argues that bidders affected by hubris pay too much for their targets,
and that the takeover record supports this explanation as much as it supports synergy, taxes or the replacement of inefficient management
[Roll 1986][research_roll_1986].
Betton, Eckbo and Thorburn survey the takeover literature as a whole
[Betton et al. 2008][research_betton_eckbo_thorburn_2008].

## Why Distressed Assets Are Cheap

The third body of theory is the closest to the question.
Shleifer and Vishny argue that when a firm in financial distress must sell assets,
its industry peers, who would value them most,
are likely to be in difficulty themselves,
so the assets sell below their value in best use.
This makes assets cheap in bad times and is a private cost of leverage
[Shleifer and Vishny 1992][research_shleifer_vishny_1992].
Shleifer and Vishny later reviewed the role of fire sales in finance and macroeconomics
[Shleifer and Vishny 2011][research_shleifer_vishny_2011].

### A Model of the Fire-Sale Price

Let $V_{b}$ be the value of an asset to its best user,
$V_{o}$ its value to an outsider,
and $L$ the most that financially constrained peers can pay.
If competing outsiders bid up to $V_{o}$ and no unconstrained peer bids against them,
the price and the fire-sale discount are as follows.

$$
P = \max\left(V_{o},\, L\right) \quad \text{when } L < V_{b},
\qquad
D = 1 - \frac{P}{V_{b}}
$$

Taking $V_{b} = 100$, $V_{o} = 70$ and $L = 60$,
the asset sells for 70 at a discount of 30 percent.

The gain to a buyer whose own value for the asset is $V_{a}$ decomposes into four terms.
The first is the discount, which every buyer at this price obtains.
The second is the buyer's shortfall from the best user.
The third is the cost of integrating the asset, $C$.
The fourth is any synergy with the rest of the buyer's chain, $S$.

$$
\text{gain} = \underbrace{\left(V_{b} - P\right)}_{\text{discount}} - \underbrace{\left(V_{b} - V_{a}\right)}_{\text{use gap}} - C + S
$$

Given an integration cost of 8 and a synergy of 5 where one applies,
three buyers fare very differently.
An outsider values the asset at 70,
so its use gap equals the discount and its gain is $30 - 30 - 8 = -8$.
An unconstrained peer values it at 100 and has a synergy of 5,
so its gain is $30 - 0 - 8 + 5 = 27$.
A buyer that repurposes the asset to a use worth 85 gains $30 - 15 - 8 = 7$.

The decomposition exposes the central tension of the strategy.
The discount exists because the best users cannot buy.
A buyer that captures the discount but lacks the best user's capability captures little,
since the use gap consumes what the discount gave.
The buyer that gains most is a best user that is not constrained when its peers are.

### The Evidence on Fire Sales

Pulvino finds that financially constrained airlines receive lower prices than unconstrained rivals when selling used narrow-body aircraft,
and are more likely to sell to industry outsiders,
especially in downturns.
Unconstrained airlines increase purchases when aircraft prices are depressed,
and constrained airlines do not
[Pulvino 1998][research_pulvino_1998].
This is the unconstrained peer of the model, observed.
Acharya, Bharath and Srinivasan report that creditors of defaulted firms in the United States from 1982 to 1999
recover significantly less when the defaulter's industry is in distress.
The effect is strongest where assets are specific to the industry and the other firms in it are illiquid,
which they interpret as a fire-sale effect rather than only an effect of the downturn
[Acharya et al. 2007][research_acharya_bharath_srinivasan_2007].

The way a firm is sold matters.
In Swedish bankruptcy auctions,
Eckbo and Thorburn find fire-sale discounts when the auction ends in piecemeal liquidation,
but not where the firm is sold as a going concern,
and in going-concern sales neither industry-wide distress nor the buyer's industry appears to affect prices
[Eckbo and Thorburn 2008][research_eckbo_thorburn_2008].
A going-concern buyer may therefore pay close to full value,
while a buyer of the pieces may pay a discount but must then assemble the pieces again.

### Buying Through Bankruptcy

In the United States,
a firm in Chapter 11 can sell divisions or other assets during the case,
for example in what is called a 363 sale,
and the existing management may help such a sale realize a higher price than a liquidation under Chapter 7
[Chapter 11, Title 11, United States Code][ref_chapter_11].
Foroughi, Gilson, Hotchkiss and Waldock document the rise of mergers and acquisitions in bankruptcy,
which they report blurs the line between reorganization and liquidation.
In the version of the paper read for this article,
such sales are countercyclical,
more likely when financing a reorganization costs more than the financing available to a buyer,
and more common with greater reliance on secured debt, but only for sales of going concerns.
Overall creditor recoveries are higher for businesses sold as going concerns
[Foroughi et al. 2015][research_foroughi_2015].

Bankruptcy status itself appears to matter less than the state of the industry.
Plant-level data lead Maksimovic and Phillips to conclude
that industry conditions explain the productivity, asset sales and closures of bankrupt firms much better than Chapter 11 status does
[Maksimovic and Phillips 1998][research_maksimovic_phillips_1998].
The buyer's opportunity therefore lies in the industry's condition rather than in the legal process.

Not every bankrupt asset is redeployed well.
Ma, Tong and Wang document that innovative firms in Chapter 11 sell their core patents rather than peripheral ones,
driven by secured creditors exercising control over collateralized patents,
and that the patents sold diffuse more slowly under new ownership
and are more likely to be bought by patent assertion entities
[Ma et al. 2021][research_ma_tong_wang_2021].

### Buyers of Distressed Firms

Investors who buy the debt of distressed firms are known as vulture investors
[Vulture Fund][ref_vulture_fund].
Hotchkiss and Mooradian study 288 firms that defaulted on public debt.
Operating performance after restructuring improves more relative to the pre-default level
when the vulture investor becomes chief executive or chairman or gains control,
and the target's stock and bonds earn positive abnormal returns when a vulture purchase is announced.
They conclude that vulture investors add value by disciplining managers
[Hotchkiss and Mooradian 1997][research_hotchkiss_mooradian_1997].
In that evidence the gain comes from control and governance,
which this article reads as the transfer of residual control rights that property rights theory describes.

## Redeploying What Was Bought

The fourth body of theory concerns what a buyer can do with assets after the purchase.

**Redeployability sets the floor on value.**
Benmelech and Bergman construct measures of how easily the collateral in airline debt can be redeployed.
Debt backed by more redeployable aircraft carries lower credit spreads, higher ratings and higher loan-to-value ratios
[Benmelech and Bergman 2009][research_benmelech_bergman_2009].
Kim and Kung measure redeployability within and across industries.
After increases in uncertainty,
firms with less redeployable capital cut investment more,
and more redeployable assets have higher recovery rates and trade more actively in secondary markets
[Kim and Kung 2016][research_kim_kung_2016].
The two results bear directly on repurposing,
and this article draws an inference from them that neither paper states.
An asset that can be redeployed holds its value in distress,
so it is seldom cheap,
while an asset that is cheap in distress tends to be specific,
so it is harder to repurpose.
The discount and the difficulty of repurposing tend to come together.

**Acquirers redeploy in both directions.**
Capron, Dussauge and Mitchell study how resources move between the target and the acquirer after horizontal acquisitions in Europe and North America
[Capron et al. 1998][research_capron_dussauge_mitchell_1998].
Using survey data on 253 horizontal acquisitions in manufacturing from 1988 to 1992,
Capron finds that both asset divestiture and resource redeployment can contribute to acquisition performance,
but that performance is at significant risk when the divested assets and redeployed resources are those of the target
[Capron 1999][research_capron_1999].
Capron, Mitchell and Swaminathan show that redeployment leads to divestiture from the business that receives the redeployed resources,
and they interpret acquisition, redeployment and divestiture together as a process for reconfiguring a firm's resources
[Capron et al. 2001][research_capron_mitchell_swaminathan_2001].
In this evidence, redeployment is a common aftermath of an acquisition,
and redeploying or divesting the target's own resources is its riskiest form.

**Resources as the unit of strategy.**
Wernerfelt proposed analysing firms by their resources rather than their products
[Wernerfelt 1984][research_wernerfelt_1984],
and Barney argued that resources yield sustained advantage when they are valuable, rare, hard to imitate and hard to substitute
[Barney 1991][research_barney_1991].
Teece, Pisano and Shuen extended the view to dynamic capabilities,
the capacity to reconfigure resources as conditions change
[Teece et al. 1997][research_teece_pisano_shuen_1997].
One criticism of the resource-based view is that it assumes resources simply exist,
without investigating how key capabilities are acquired or developed
[Resource-Based View][ref_resource_based_view],
which is the question a buildup strategy has to answer.
On this view, a buildup creates lasting value only where the acquirer has a capability for redeploying what it buys that its rivals lack.

## Serial Acquisition and Roll-ups

A buildup is a sequence of acquisitions,
and research on firms that make many acquisitions addresses sequences directly.
Fuller, Netter and Stegemoller study firms that acquired five or more targets within a short period.
Bidder shareholders gain when the target is a private firm or a subsidiary
and lose when it is a public firm,
and they interpret the pattern as consistent with a liquidity discount on targets that cannot easily be sold,
together with tax and control effects
[Fuller et al. 2002][research_fuller_netter_stegemoller_2002].
This article reads that liquidity discount as the same mechanism as the fire sale,
operating on private firms that have few buyers.

Brown, Dittmar and Servaes study roll-up initial public offerings,
in which small private firms merge into a shell company that goes public at the same time.
These firms deliver poor stock returns,
and their operating performance matches comparable firms but does not justify their initial valuations.
Performance improves when the owners and managers of the combined firms remain involved as shareholders and directors,
and it worsens with higher ownership by the sponsor
[Brown et al. 2004][research_brown_dittmar_servaes_2004].
In that sample, the governance of the consolidation mattered to its success.

## Holding Liquidity for the Next Downturn

The fire-sale evidence implies that the buyer's advantage is liquidity at a time others have none.
That advantage has a cost,
because capital held in reserve earns less than capital put to work.
Let $K$ be the capital held in reserve,
$c$ the annual cost of holding it as a fraction of $K$,
$A$ the size of the asset bought in an opportunity,
$d$ the net gain per opportunity as a fraction of $A$,
and $p$ the annual probability that an opportunity arises.
Holding the reserve pays in expectation under the following condition.

$$
p\, d\, A \;\geq\; c\, K
$$

With $K = 500$ and $c = 3$ percent,
the reserve costs 15 a year.
For $A = 300$ and $d = 25$ percent,
an opportunity is worth 75.
The reserve pays if opportunities arise with an annual probability of at least $15 / 75 = 0.20$,
about once every five years.
The condition is sensitive to $d$,
which by the decomposition above is the discount net of the use gap and integration cost,
not the headline discount.
In the fire-sale example the repurposer's net gain is 7 percent of the asset's value against a headline discount of 30 percent,
so a repurposer that used the headline figure for $d$ would overstate the value of its reserve by a factor of more than four.

## How the Four Bodies of Theory Fit Together

The four bodies of theory combine into a coherent account of the conditions under which the strategy can work,
though no single model in the literature cited here contains all four.

1. **Integration must pay on its own terms.**
The hold-up model and the property rights theory say when owning the next stage is better than contracting with it.
A cheap purchase of a business that should not be integrated is still a mistake.
2. **The discount must be captured, not just observed.**
The fire-sale model says the discount exists because the best users are constrained.
A buyer that is not a best user loses most of the discount to the use gap.
3. **The buyer must be liquid when its peers are not.**
In the aircraft data unconstrained peers buy when prices are depressed,
and the reserve condition puts a price on being ready.
4. **The buyer must be able to redeploy what it buys.**
Redeployment studies find redeployment common after acquisitions
and riskiest when it takes resources from the target.
5. **The sequence must be governed.**
Roll-up offerings have performed poorly on average and better when the acquired firms' owners stay involved.

The account has a built-in conflict.
Assets are cheapest in distress if they are specific,
and specific assets are the hardest to redeploy.
The strategy therefore works best for a buyer whose own business is the best alternative use,
which is the same industry or the adjacent stage of the same chain.
That is a vertically or horizontally related buyer,
which is the case this article began with.

## Epistemic State

**Facts reported by the cited papers.**
Each finding attributed to a paper is taken from its abstract as recorded by Crossref or OpenAlex,
except for six papers whose findings are taken from abstracts reproduced in search-indexed listings.
Those are the papers of Acharya, Bharath and Srinivasan,
Benmelech and Bergman,
Capron, Dussauge and Mitchell,
Eckbo and Thorburn,
Foroughi, Gilson, Hotchkiss and Waldock,
and Hotchkiss and Mooradian.
The Foroughi paper exists in more than one version,
and a 2015 draft credits Gilson, Hotchkiss and Osborn,
so its findings are reported as those of the version read.
The Coase, Klein and coauthors, Shleifer and Vishny 2011, Betton and coauthors, and Teece and coauthors works
are cited for their subject and their widely summarized argument.
The two Williamson works are cited through reprints of articles first published in 1971 and 1968.
None of the papers was read in full.

**Analysis in this article.**
The hold-up model,
the linear surplus tradeoff,
the fire-sale price and the decomposition of the buyer's gain,
and the reserve condition
are simple models built for this article to illustrate the cited theories.
They are not the models in the cited papers,
and every number in them is hypothetical.

**Inference and judgment.**
The claim that no single theory covers the strategy is a judgment from the literature reviewed here,
which is not exhaustive.
The five-part synthesis is this article's own,
and the conflict between the size of the discount and the ease of redeployment is an inference from the redeployability and fire-sale evidence together,
not a result any cited paper states.
A reader who knows of a unified model of distressed acquisition as an integration strategy should weigh it above this synthesis.

## Out of Scope

- The law of bankruptcy, including the mechanics and protections of a 363 sale,
and the law of competition in any jurisdiction.
- Liabilities that pass to a buyer, such as environmental, pension and product liabilities,
which can make a cheap asset expensive.
- Private equity buy-and-build strategies as a distinct literature.
- Distressed debt investing as a strategy for gaining control,
beyond the vulture-investor studies cited above.
- Tax treatment of acquired losses and of asset purchases.
- Cross-border acquisitions and their regulatory review.

## Conclusion

The theory needed to judge a strategy of building an integrated enterprise from distressed acquisitions is established,
but it is spread across four literatures,
and none of them models the strategy as a whole.
Transaction cost and property rights theory say when owning the next stage of a chain is better than contracting with it,
and what control costs.
The market for corporate assets explains acquisitions as reallocation toward better users,
while research on acquirer returns warns that acquirers often pay too much.
The fire-sale literature accounts for the cheapness of distressed assets
and identifies the buyers who gain most as best users that remain unconstrained when their peers are not.
The redeployment literature finds redeployment common after acquisitions,
and the redeployability evidence suggests that assets cheap enough to be bargains are often too specific to repurpose easily.

Taken together,
these results favour a buyer in the same industry or the adjacent stage of the same chain,
with liquidity held for downturns,
a demonstrated capability for redeploying what it buys,
and governance that keeps the acquired firms' knowledge involved.
They do not favour an outsider buying whatever is cheap,
because the discount that makes the purchase cheap is largely the measure of how little an outsider can do with it.

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- Acharya, Viral V., Sreedhar T. Bharath, and Anand Srinivasan. 2007. "Does Industry-Wide Distress Affect Defaulted Firms? Evidence from Creditor Recoveries." *Journal of Financial Economics* 85 (3): 787–821. [https://doi.org/10.1016/j.jfineco.2006.05.011][research_acharya_bharath_srinivasan_2007]
- Benmelech, Efraim, and Nittai K. Bergman. 2009. "Collateral Pricing." *Journal of Financial Economics* 91 (3): 339–60. [https://doi.org/10.1016/j.jfineco.2008.03.003][research_benmelech_bergman_2009]
- Capron, Laurence. 1999. "The Long-Term Performance of Horizontal Acquisitions." *Strategic Management Journal* 20 (11): 987–1018. [https://doi.org/10.1002/(sici)1097-0266(199911)20:11\<987::aid-smj61\>3.0.co;2-b][research_capron_1999]
- Capron, Laurence, Pierre Dussauge, and Will Mitchell. 1998. "Resource Redeployment Following Horizontal Acquisitions in Europe and North America, 1988-1992." *Strategic Management Journal* 19 (7): 631–61. [https://doi.org/10.1002/(sici)1097-0266(199807)19:7\<631::aid-smj963\>3.0.co;2-9][research_capron_dussauge_mitchell_1998]
- Capron, Laurence, Will Mitchell, and Anand Swaminathan. 2001. "Asset Divestiture Following Horizontal Acquisitions: A Dynamic View." *Strategic Management Journal* 22 (9): 817–44. [https://doi.org/10.1002/smj.175][research_capron_mitchell_swaminathan_2001]
- Coase, R. H. 1937. "The Nature of the Firm." *Economica* 4 (16): 386–405. [https://doi.org/10.1111/j.1468-0335.1937.tb00002.x][research_coase_1937]
- Eckbo, B. Espen, and Karin S. Thorburn. 2008. "Automatic Bankruptcy Auctions and Fire-Sales." *Journal of Financial Economics* 89 (3): 404–22. [https://doi.org/10.1016/j.jfineco.2007.10.003][research_eckbo_thorburn_2008]
- Hotchkiss, Edith S., and Robert M. Mooradian. 1997. "Vulture Investors and the Market for Control of Distressed Firms." *Journal of Financial Economics* 43 (3): 401–32. [https://doi.org/10.1016/s0304-405x(96)00900-2][research_hotchkiss_mooradian_1997]
- Teece, David J., Gary Pisano, and Amy Shuen. 1997. "Dynamic Capabilities and Strategic Management." *Strategic Management Journal* 18 (7): 509–33. [https://doi.org/10.1002/(sici)1097-0266(199708)18:7\<509::aid-smj882\>3.0.co;2-z][research_teece_pisano_shuen_1997]
- Wernerfelt, Birger. 1984. "A Resource-Based View of the Firm." *Strategic Management Journal* 5 (2): 171–80. [https://doi.org/10.1002/smj.4250050207][research_wernerfelt_1984]

### Primary Sources, Non-Peer-Reviewed

- Aghion, Philippe, Rachel Griffith, and Peter Howitt. 2006. "Vertical Integration and Competition." *American Economic Review* 96 (2): 97–102. [https://doi.org/10.1257/000282806777211595][research_aghion_griffith_howitt_2006]
- Andrade, Gregor, Mark Mitchell, and Erik Stafford. 2001. "New Evidence and Perspectives on Mergers." *Journal of Economic Perspectives* 15 (2): 103–20. [https://doi.org/10.1257/jep.15.2.103][research_andrade_mitchell_stafford_2001]
- Atalay, Enghin, Ali Hortaçsu, and Chad Syverson. 2014. "Vertical Integration and Input Flows." *American Economic Review* 104 (4): 1120–48. [https://doi.org/10.1257/aer.104.4.1120][research_atalay_hortacsu_syverson_2014]
- Barney, Jay. 1991. "Firm Resources and Sustained Competitive Advantage." *Journal of Management* 17 (1): 99–120. [https://doi.org/10.1177/014920639101700108][research_barney_1991]
- Betton, Sandra, B. Espen Eckbo, and Karin S. Thorburn. 2008. "Corporate Takeovers\*\*Surveying the Vast Area of Corporate Takeovers Is a Daunting Task, and We Have Undoubtedly Missed Many Interesting Contributions. We Apologize to Those Who Feel Their Research Has Been Left out or Improperly Characterized, and Welcome Reactions and Comments. Some of the Material in Section 3 Is Also Found in Eckbo (2008)." In *Handbook of Empirical Corporate Finance*. Elsevier. [https://doi.org/10.1016/b978-0-444-53265-7.50007-x][research_betton_eckbo_thorburn_2008]
- Brown, Keith C., Amy Dittmar, and Henri Servaes. 2004. "Corporate Governance, Incentives, and Industry Consolidations." *Review of Financial Studies* 18 (1): 241–70. [https://doi.org/10.1093/rfs/hhh009][research_brown_dittmar_servaes_2004]
- Fan, Joseph P. H., and Vidhan K. Goyal. 2006. "On the Patterns and Wealth Effects of Vertical Mergers." *Journal of Business* 79 (2): 877–902. [https://doi.org/10.1086/499141][research_fan_goyal_2006]
- Forbes, Silke Januszewski, and Mara Lederman. 2009. "Adaptation and Vertical Integration in the Airline Industry." *American Economic Review* 99 (5): 1831–49. [https://doi.org/10.1257/aer.99.5.1831][research_forbes_lederman_2009]
- Foroughi, Pouyan, Stuart C. Gilson, Edith S. Hotchkiss, and Katherine Waldock. 2015. "Cashing Out: The Rise of M&A in Bankruptcy." Preprint, . [https://doi.org/10.2139/ssrn.2547168][research_foroughi_2015]
- Fuller, Kathleen, Jeffry Netter, and Mike Stegemoller. 2002. "What Do Returns to Acquiring Firms Tell Us? Evidence from Firms That Make Many Acquisitions." *Journal of Finance* 57 (4): 1763–93. [https://doi.org/10.1111/1540-6261.00477][research_fuller_netter_stegemoller_2002]
- Grossman, Sanford J., and Oliver D. Hart. 1986. "The Costs and Benefits of Ownership: A Theory of Vertical and Lateral Integration." *Journal of Political Economy* 94 (4): 691–719. [https://doi.org/10.1086/261404][research_grossman_hart_1986]
- Hart, Oliver, and John Moore. 1990. "Property Rights and the Nature of the Firm." *Journal of Political Economy* 98 (6): 1119–58. [https://doi.org/10.1086/261729][research_hart_moore_1990]
- Hortaçsu, Ali, and Chad Syverson. 2007. "Cementing Relationships: Vertical Integration, Foreclosure, Productivity, and Prices." *Journal of Political Economy* 115 (2): 250–301. [https://doi.org/10.1086/514347][research_hortacsu_syverson_2007]
- Jovanovic, Boyan, and Peter L. Rousseau. 2002. "The Q-Theory of Mergers." *American Economic Review* 92 (2): 198–204. [https://doi.org/10.1257/000282802320189249][research_jovanovic_rousseau_2002]
- Kim, Hyunseob, and Howard Kung. 2016. "The Asset Redeployability Channel: How Uncertainty Affects Corporate Investment." *Review of Financial Studies* 30 (1): 245–80. [https://doi.org/10.1093/rfs/hhv076][research_kim_kung_2016]
- Klein, Benjamin, Robert G. Crawford, and Armen A. Alchian. 1978. "Vertical Integration, Appropriable Rents, and the Competitive Contracting Process." *Journal of Law and Economics* 21 (2): 297–326. [https://doi.org/10.1086/466922][research_klein_crawford_alchian_1978]
- Lafontaine, Francine, and Margaret Slade. 2007. "Vertical Integration and Firm Boundaries: The Evidence." *Journal of Economic Literature* 45 (3): 629–85. [https://doi.org/10.1257/jel.45.3.629][research_lafontaine_slade_2007]
- Ma, Song, Joy Tianjiao Tong, and Wei Wang. 2021. *Bankrupt Innovative Firms*. National Bureau of Economic Research. [https://doi.org/10.3386/w28856][research_ma_tong_wang_2021]
- Maksimovic, Vojislav, and Gordon Phillips. 1998. "Asset Efficiency and Reallocation Decisions of Bankrupt Firms." *Journal of Finance* 53 (5): 1495–1532. [https://doi.org/10.1111/0022-1082.00063][research_maksimovic_phillips_1998]
- Maksimovic, Vojislav, and Gordon Phillips. 2001. "The Market for Corporate Assets: Who Engages in Mergers and Asset Sales and Are There Efficiency Gains?" *Journal of Finance* 56 (6): 2019–65. [https://doi.org/10.1111/0022-1082.00398][research_maksimovic_phillips_2001]
- Pulvino, Todd C. 1998. "Do Asset Fire Sales Exist? An Empirical Investigation of Commercial Aircraft Transactions." *Journal of Finance* 53 (3): 939–78. [https://doi.org/10.1111/0022-1082.00040][research_pulvino_1998]
- Roll, Richard. 1986. "The Hubris Hypothesis of Corporate Takeovers." *Journal of Business* 59 (2): 197. [https://doi.org/10.1086/296325][research_roll_1986]
- Shleifer, Andrei, and Robert W. Vishny. 1992. "Liquidation Values and Debt Capacity: A Market Equilibrium Approach." *Journal of Finance* 47 (4): 1343–66. [https://doi.org/10.1111/j.1540-6261.1992.tb04661.x][research_shleifer_vishny_1992]
- Shleifer, Andrei, and Robert Vishny. 2011. "Fire Sales in Finance and Macroeconomics." *Journal of Economic Perspectives* 25 (1): 29–48. [https://doi.org/10.1257/jep.25.1.29][research_shleifer_vishny_2011]
- Williamson, O. E. 1972. "Economies as an Anti-Trust Defense: The Welfare Tradeoffs." In *Readings in Industrial Economics*. Macmillan Education UK. [https://doi.org/10.1007/978-1-349-15486-9\_7][research_williamson_1972]
- Williamson, Oliver E. (1971) 1999. "The Vertical Integration of Production Market Failure Considerations." In *Firms, Markets, And Hierarchies*. Oxford University PressNew York, NY. [https://doi.org/10.1093/oso/9780195119510.003.0002][research_williamson_1971]

### Tertiary Sources

- "Chapter 11, Title 11, United States Code." 2026. Wikipedia. Last modified September 9, at 19:07 (UTC). [https://en.wikipedia.org/w/index.php?title=Chapter\_11,\_Title\_11,\_United\_States\_Code&oldid=1374085130][ref_chapter_11]
- "Hold-up Problem." 2026. Wikipedia. Last modified October 18, at 01:30 (UTC). [https://en.wikipedia.org/w/index.php?title=Hold-up\_problem&oldid=1380809520][ref_hold_up_problem]
- "Horizontal Integration." 2026. Wikipedia. Last modified May 2, at 11:23 (UTC). [https://en.wikipedia.org/w/index.php?title=Horizontal\_integration&oldid=1352151930][ref_horizontal_integration]
- "Resource-Based View." 2026. Wikipedia. Last modified September 3, at 02:26 (UTC). [https://en.wikipedia.org/w/index.php?title=Resource-based\_view&oldid=1372940236][ref_resource_based_view]
- "Theory of the Firm." 2026. Wikipedia. Last modified October 15, at 03:26 (UTC). [https://en.wikipedia.org/w/index.php?title=Theory\_of\_the\_firm&oldid=1380337754][ref_theory_of_the_firm]
- "Vertical Integration." 2026. Wikipedia. Last modified September 15, at 22:04 (UTC). [https://en.wikipedia.org/w/index.php?title=Vertical\_integration&oldid=1375102957][ref_vertical_integration]
- "Vulture Fund." 2026. Wikipedia. Last modified June 7, at 10:40 (UTC). [https://en.wikipedia.org/w/index.php?title=Vulture\_fund&oldid=1358223598][ref_vulture_fund]

### Related Posts

- Sechter, Brendan. 2026. "What the Conglomerate Discount Measures." *Brendan A R Sechter's Development Blog*, August 14. [https://sgeos.github.io/business/economics/finance/2026/08/14/conglomerate\_discount.html][related_post_conglomerate_discount]

[ref_chapter_11]: https://en.wikipedia.org/w/index.php?title=Chapter_11,_Title_11,_United_States_Code&oldid=1374085130
[ref_hold_up_problem]: https://en.wikipedia.org/w/index.php?title=Hold-up_problem&oldid=1380809520
[ref_horizontal_integration]: https://en.wikipedia.org/w/index.php?title=Horizontal_integration&oldid=1352151930
[ref_resource_based_view]: https://en.wikipedia.org/w/index.php?title=Resource-based_view&oldid=1372940236
[ref_theory_of_the_firm]: https://en.wikipedia.org/w/index.php?title=Theory_of_the_firm&oldid=1380337754
[ref_vertical_integration]: https://en.wikipedia.org/w/index.php?title=Vertical_integration&oldid=1375102957
[ref_vulture_fund]: https://en.wikipedia.org/w/index.php?title=Vulture_fund&oldid=1358223598
[related_post_conglomerate_discount]: {% post_url 2026-08-14-conglomerate_discount %}
[research_acharya_bharath_srinivasan_2007]: https://doi.org/10.1016/j.jfineco.2006.05.011
[research_aghion_griffith_howitt_2006]: https://doi.org/10.1257/000282806777211595
[research_andrade_mitchell_stafford_2001]: https://doi.org/10.1257/jep.15.2.103
[research_atalay_hortacsu_syverson_2014]: https://doi.org/10.1257/aer.104.4.1120
[research_barney_1991]: https://doi.org/10.1177/014920639101700108
[research_benmelech_bergman_2009]: https://doi.org/10.1016/j.jfineco.2008.03.003
[research_betton_eckbo_thorburn_2008]: https://doi.org/10.1016/b978-0-444-53265-7.50007-x
[research_brown_dittmar_servaes_2004]: https://doi.org/10.1093/rfs/hhh009
[research_capron_1999]: https://doi.org/10.1002/(sici)1097-0266(199911)20:11<987::aid-smj61>3.0.co;2-b
[research_capron_dussauge_mitchell_1998]: https://doi.org/10.1002/(sici)1097-0266(199807)19:7<631::aid-smj963>3.0.co;2-9
[research_capron_mitchell_swaminathan_2001]: https://doi.org/10.1002/smj.175
[research_coase_1937]: https://doi.org/10.1111/j.1468-0335.1937.tb00002.x
[research_eckbo_thorburn_2008]: https://doi.org/10.1016/j.jfineco.2007.10.003
[research_fan_goyal_2006]: https://doi.org/10.1086/499141
[research_forbes_lederman_2009]: https://doi.org/10.1257/aer.99.5.1831
[research_foroughi_2015]: https://doi.org/10.2139/ssrn.2547168
[research_fuller_netter_stegemoller_2002]: https://doi.org/10.1111/1540-6261.00477
[research_grossman_hart_1986]: https://doi.org/10.1086/261404
[research_hart_moore_1990]: https://doi.org/10.1086/261729
[research_hortacsu_syverson_2007]: https://doi.org/10.1086/514347
[research_hotchkiss_mooradian_1997]: https://doi.org/10.1016/s0304-405x(96)00900-2
[research_jovanovic_rousseau_2002]: https://doi.org/10.1257/000282802320189249
[research_kim_kung_2016]: https://doi.org/10.1093/rfs/hhv076
[research_klein_crawford_alchian_1978]: https://doi.org/10.1086/466922
[research_lafontaine_slade_2007]: https://doi.org/10.1257/jel.45.3.629
[research_ma_tong_wang_2021]: https://doi.org/10.3386/w28856
[research_maksimovic_phillips_1998]: https://doi.org/10.1111/0022-1082.00063
[research_maksimovic_phillips_2001]: https://doi.org/10.1111/0022-1082.00398
[research_pulvino_1998]: https://doi.org/10.1111/0022-1082.00040
[research_roll_1986]: https://doi.org/10.1086/296325
[research_shleifer_vishny_1992]: https://doi.org/10.1111/j.1540-6261.1992.tb04661.x
[research_shleifer_vishny_2011]: https://doi.org/10.1257/jep.25.1.29
[research_teece_pisano_shuen_1997]: https://doi.org/10.1002/(sici)1097-0266(199708)18:7<509::aid-smj882>3.0.co;2-z
[research_wernerfelt_1984]: https://doi.org/10.1002/smj.4250050207
[research_williamson_1971]: https://doi.org/10.1093/oso/9780195119510.003.0002
[research_williamson_1972]: https://doi.org/10.1007/978-1-349-15486-9_7
