---
layout: post
mathjax: true
comments: true
title: "What the Conglomerate Discount Measures"
date: 2026-08-14 09:00:00 +0000
categories: business economics finance
---

<!-- A378 -->
<script>console.log("A378");</script>

A conglomerate is a firm that operates businesses in several unrelated industries
[Conglomerate][ref_conglomerate_company].
Investors and analysts commonly say that such firms trade at a conglomerate discount,
meaning that the market values the whole at less than the sum of what its businesses would be worth on their own
[Conglomerate Discount][ref_conglomerate_discount].
The claim is used to argue for breakups,
and the gap is often quoted as a single figure,
such as an average of 13 to 15 percent in developed economies
[Conglomerate Discount][ref_conglomerate_discount].

This article asks whether the mathematics for establishing that gap is settled.
The short answer has two parts.
The arithmetic of the standard measures is fully specified and widely replicated,
and under those measures diversified firms in the United States have on average been valued below their imputed stand-alone values.
Whether the measured gap is a causal effect of conglomeration,
and how large it is for any single firm,
is not settled,
because the value of a business outside the conglomerate cannot be observed while it is inside one.

The article sets out the standard measures with worked numbers,
shows where each one can be biased,
separates the evidence that the gap is caused by conglomeration from the evidence that it is an artifact of selection or measurement,
and reviews the international and spin-off evidence.
It does not value any real company,
does not recommend for or against any breakup,
and does not treat a result from one sample as a law.
Every numerical example is hypothetical,
and the figures that come from the literature are attributed to the papers that report them.

## A Brief History

The question is older than the measures.
Lewellen argued in 1971 that combining businesses with imperfectly correlated cash flows
lowers the probability of default and so raises the capacity of the combined firm to carry debt,
which is the coinsurance argument for conglomerate mergers
[Lewellen 1971][research_lewellen_1971].
That argument was made at the end of the diversification trend of the late 1960s and early 1970s
[Servaes 1996][research_servaes_1996].

Servaes studied that period directly and found no evidence that diversified firms were valued at a premium during the 1960s and 1970s.
The same study found a large diversification discount in the 1960s,
which declined to zero during the 1970s
[Servaes 1996][research_servaes_1996].
By the 1980s the trend had reversed toward focus.
Comment and Jarrell documented that reversal,
a positive relation between stock returns and increases in focus,
and the failure of diversified firms to exploit the financial economies of scope that coinsurance and internal capital markets were supposed to provide
[Comment and Jarrell 1995][research_comment_jarrell_1995].

The two most common measures were published in 1994 and 1995.
Lang and Stulz compared the Tobin's q of diversified firms with that of portfolios of single-segment firms
[Lang and Stulz 1994][research_lang_stulz_1994],
and Berger and Ofek compared actual firm value with the sum of imputed stand-alone segment values
[Berger and Ofek 1995][research_berger_ofek_1995].
Both found a discount.
Much of the later literature uses one of these measures or argues against it,
and Hund, Monk and Tice describe the Berger and Ofek measure as widely used
[Hund et al. 2024][research_hund_monk_tice_2024].
Two surveys review the literature that followed,
one published in 2003
[Martin and Sayrak 2003][research_martin_sayrak_2003]
and one in 2013
[Erdorf et al. 2013][research_erdorf_2013].

## The Quantity of Interest Is a Counterfactual

The phrase "value inside and outside a conglomerate" names a comparison between two states of the world,
only one of which exists at any time.
Let $V^{c}$ be the market value of the firm as it is,
with its segments operated together,
and let $V^{s}_{i}$ be the value segment $i$ would have if it were operated as an independent firm.
The delta the question asks about is the following.

$$
\Delta = V^{c} - \sum_{i=1}^{n} V^{s}_{i}
\tag{1}
$$

The first term is observed for a listed firm.
The second term is never observed for the same segments at the same time,
because a segment that is operated inside the conglomerate is not also trading as an independent company.
Every measure in the literature therefore replaces $V^{s}_{i}$ with an estimate built from other firms,
and most of the disputes reviewed below are, at bottom, disputes about whether that estimate is a fair stand-in.

This is the same structure as a treatment effect in econometrics.
Diversification is the treatment,
the firm's actual value is the treated outcome,
and the stand-alone value is the untreated outcome that must be imputed.
The analogy matters because it tells the reader in advance what can go wrong.
If the firms that receive the treatment differ from the firms used to impute the untreated outcome,
the comparison measures that difference as well as the treatment.

## The Imputed-Value Measure

Berger and Ofek impute a stand-alone value for each segment by multiplying an accounting quantity of the segment
by the median ratio of total capital to that quantity among single-segment firms in the same industry.
They then compare the sum of those imputed values with the firm's actual value
[Berger and Ofek 1995][research_berger_ofek_1995].

Define the symbols before the equations.
$V$ is the firm's total capital,
taken as the market value of equity plus the book value of debt
[Mansi and Reeb 2002][research_mansi_reeb_2002].
$A_{i}$ is an accounting item for segment $i$,
such as its sales or its assets,
in the same currency units as $V$.
$m_{i}$ is the median, across single-segment firms in segment $i$'s industry,
of the ratio of total capital to the same accounting item,
and is a pure number.
The imputed value of the firm and its excess value are then defined as follows.

$$
I(V) = \sum_{i=1}^{n} A_{i}\, m_{i}
\tag{2}
$$

$$
EV = \ln\!\left(\frac{V}{I(V)}\right)
\tag{3}
$$

A negative excess value is a discount and a positive one is a premium.
Because the excess value is a logarithm,
it converts to a percentage shortfall of actual value below imputed value as follows.

$$
d = 1 - e^{EV}
\tag{4}
$$

Berger and Ofek report that comparing the sum of the stand-alone values with actual value
implies an average value loss of 13 to 15 percent for diversified firms in the United States from 1986 to 1991.
They also report that the loss is smaller when the segments are in the same two-digit Standard Industrial Classification code,
that overinvestment and cross-subsidization contribute to it,
and that tax benefits of diversification reduce it modestly
[Berger and Ofek 1995][research_berger_ofek_1995].
Practitioners perform the same calculation under the name sum-of-the-parts analysis,
valuing each segment, summing the results to an enterprise value and subtracting net debt to reach an equity value
[Sum-of-the-Parts Analysis][ref_sum_of_the_parts].

### A Worked Example

Consider a hypothetical firm with three segments,
with all money figures in millions of dollars.
Segment A makes industrial machinery,
with sales of 4,000 and assets of 3,000.
Segment B makes specialty chemicals,
with sales of 2,500 and assets of 2,800.
Segment C makes consumer products,
with sales of 1,500 and assets of 900.
The firm's equity has a market value of 6,500 and its debt a book value of 3,500,
so $V = 10{,}000$.

Suppose the median capital-to-sales ratios of single-segment peers are 1.2, 1.6 and 2.0 for the three industries,
and the median capital-to-assets ratios are 1.5, 1.3 and 2.6.
The sales-based imputed value is the following.

$$
I_{\text{sales}} = 4{,}000 \times 1.2 + 2{,}500 \times 1.6 + 1{,}500 \times 2.0 = 4{,}800 + 4{,}000 + 3{,}000 = 11{,}800
\tag{5}
$$

$$
EV_{\text{sales}} = \ln\!\left(\frac{10{,}000}{11{,}800}\right) = -0.1655,
\qquad
d_{\text{sales}} = 1 - e^{-0.1655} = 15.3\%
\tag{6}
$$

The asset-based imputed value is the following.

$$
I_{\text{assets}} = 3{,}000 \times 1.5 + 2{,}800 \times 1.3 + 900 \times 2.6 = 4{,}500 + 3{,}640 + 2{,}340 = 10{,}480
\tag{7}
$$

$$
EV_{\text{assets}} = \ln\!\left(\frac{10{,}000}{10{,}480}\right) = -0.0469,
\qquad
d_{\text{assets}} = 4.6\%
\tag{8}
$$

The same firm, the same peers and the same market price give a discount of 15.3 percent on one accounting base and 4.6 percent on the other,
a gap of 11.9 log points.
Nothing in the definition says which base is correct.
Sales and assets each proxy for the scale of a segment,
and they disagree whenever a segment's asset intensity differs from that of its median peer,
as it does for all three segments here and for segment C most of all.
The measure is fully specified once the base is chosen,
but the choice of base is a modelling decision that moves the answer by about as much as the published average discount.

### The Measure Is Linear in the Peer Multiples

The imputed value is a weighted sum of peer multiples,
so a proportional error in the multiples passes straight through to the excess value.
If every peer multiple is too high by a factor $(1 + b)$,
the measured excess value is too low by $\ln(1 + b)$.

$$
EV_{\text{measured}} = EV_{\text{true}} - \ln(1 + b)
\tag{9}
$$

In the worked example,
if peer multiples matched on size were 10 percent lower than the industry medians,
the sales-based excess value would rise from $-0.1655$ to $\ln\left(10{,}000 / (0.9 \times 11{,}800)\right) = -0.0602$,
a shift of 10.5 log points.
If the size-matched multiples were 15.3 percent below the industry medians,
the sales-based discount would vanish.

This is not a hypothetical concern.
Hund, Monk and Tice report that the Berger and Ofek procedure consistently matches large and old diversified firms with small and young focused firms,
and that because valuation multiples decline with sales and age the procedure manufactures a discount.
With matching on sales and age the return-weighted discount they estimate is zero,
and they conclude that for most firms the discount is an artifact of the method
[Hund et al. 2024][research_hund_monk_tice_2024].
That is one recent paper and its conclusion is contested by the literature reviewed below,
but the mechanism it identifies follows directly from the linearity of the measure.

### Averaging Across Firms

A published average discount is an average of excess values across many firms,
and the result depends on whether the logarithms or the ratios are averaged.
Two hypothetical firms trading at 0.6 and 1.2 times their imputed values illustrate the difference.
The mean of their logarithmic excess values is $\left(\ln 0.6 + \ln 1.2\right)/2 = -0.1643$,
which converts to a discount of 15.1 percent.
The mean of their ratios is $0.9$,
a discount of 10.0 percent.
Neither is wrong,
since one is a geometric mean and the other an arithmetic mean,
but a reader comparing figures across papers should check which was reported,
along with whether means or medians were used and how extreme values were trimmed.

## The Tobin's q Measure

Tobin's q is the ratio of a firm's market value to the replacement cost of its assets
[Tobin's q][ref_tobins_q].
Lang and Stulz show that q and diversification are negatively related throughout the 1980s,
that the relation holds across diversification measures and controls,
and that diversified firms have lower q than comparable portfolios of pure-play firms.
They also report that firms that choose to diversify were poor performers relative to firms that did not,
and they find no evidence that diversification provides a valuable intangible asset
[Lang and Stulz 1994][research_lang_stulz_1994].
The second finding is an early warning of the selection problem discussed below.

One way to build the portfolio comparison, weighting each peer q by the segment's assets, is as follows.
Let $K_{i}$ be the replacement cost of segment $i$'s assets and $K = \sum_{i} K_{i}$.
Let $\bar{q}_{i}$ be the median q of single-segment firms in segment $i$'s industry.
The firm's own q and its imputed q are then defined as follows.

$$
q = \frac{V}{K},
\qquad
\hat{q} = \sum_{i=1}^{n} \frac{K_{i}}{K}\, \bar{q}_{i}
\tag{10}
$$

Using the same hypothetical firm with replacement costs of 3,600, 3,200 and 1,000 for the three segments,
and peer median q of 1.30, 1.25 and 1.90,
the firm's q is $10{,}000 / 7{,}800 = 1.282$
and its imputed q is $\left(3{,}600 \times 1.30 + 3{,}200 \times 1.25 + 1{,}000 \times 1.90\right) / 7{,}800 = 1.356$.
The log ratio is $\ln(1.282 / 1.356) = -0.056$,
a discount of about 5.5 percent.
This is yet another figure for the same firm,
which illustrates again that the size of a discount depends on which quantity is used to scale the segments.

The q measure has its own accounting bias.
Custódio shows that under purchase accounting acquired assets enter the books at their transaction value,
which usually exceeds the target's previous book value,
so measured q is lower for the merged firm than for the portfolio of the pre-merger firms.
Conglomerates are more acquisitive than focused firms,
so their q is depressed for an accounting reason.
Subtracting goodwill from book assets eliminates a substantial part of the q-based discount,
while market-to-sales measures do not have this bias
[CustÓDio 2014][research_custodio_2014].

## Why a Measured Discount Is Not Yet a Causal Effect

Write $Y$ for a firm's excess value,
$D = 1$ for a diversified firm and $D = 0$ for a focused one,
and $Y_{1}$ and $Y_{0}$ for the excess value a firm would have if it were diversified and if it were not.
The raw comparison between groups decomposes exactly into a treatment effect and a selection term.

$$
\underbrace{E[Y \mid D=1] - E[Y \mid D=0]}_{\text{measured discount}}
=
\underbrace{E[Y_{1} - Y_{0} \mid D=1]}_{\text{effect on diversified firms}}
+
\underbrace{E[Y_{0} \mid D=1] - E[Y_{0} \mid D=0]}_{\text{selection}}
\tag{11}
$$

The selection term is the difference between what diversified firms would have been worth undiversified
and what focused firms are actually worth.
If the firms that diversify were already worth less than their peers,
the selection term is negative and the measured discount overstates the effect of diversification.
As a hypothetical illustration,
a measured discount of 14 log points with a selection term of $-10$ log points
implies an effect of only $-4$ log points.
The identity holds for any sample.
What the data cannot supply without further assumptions is the selection term.

Several papers estimate it and find it large.
Campa and Kedia control for the endogeneity of the decision to diversify with three econometric techniques.
The choice to diversify is strongly and negatively correlated with firm value,
and once it is modelled the discount always drops and sometimes becomes a premium
[Campa and Kedia 2002][research_campa_kedia_2002].
Graham, Lemmon and Wolf study several hundred firms that expand by acquisition or add segments.
Much of the decline in excess value, by that account, occurs because the firms acquire business units that were already discounted,
not because diversifying destroys value.
Excess value, they add, does not fall when the number of reported segments rises only because of a change in reporting
[Graham et al. 2002][research_graham_lemmon_wolf_2002].
Villalonga matches diversifying and single-segment firms on their propensity to diversify
and finds that on average diversification does not destroy value
[Villalonga 2000][research_villalonga_2000].
Chang, Kogut and Yang apply a selection correction to the discount on geographically diversified firms
and report results that contradict the earlier finding
[Chang et al. 2016][research_chang_kogut_yang_2016].

The selection argument has not won outright.
In the estimates of Ammann, Hoechle and Schmid the discount disappears in a Heckman selection model
but remains statistically and economically significant once firm fixed effects are included,
including within selection and instrumental-variable frameworks
[Ammann et al. 2011][research_ammann_hoechle_schmid_2011].
Eulerich and Fligge study about 6,000 German firm-years from 2000 to 2019
and measure a discount of 7.9 to 11.5 percent.
They report that design choices related to self-selection have the largest effect on the result,
and two-stage least squares yields no causal relation between diversification and market value
across the instruments and excess-value measures they test
[Eulerich and Fligge 2024][research_eulerich_fligge_2024].
The disagreement between these results turns on assumptions that cannot be tested from the data alone,
namely which instruments are valid and whether firm fixed effects absorb the relevant differences between firms.

Survival adds a further selection channel.
Altieri and Nicodano model a sample that omits controls for each firm's likelihood of surviving in it.
They show that the measured discount then moves with the conglomerates' default probability relative to focused firms,
that the effect disappears when survival probability is controlled for,
and that the data support a selection bias against the relative value of firms with higher survival probability
[Altieri and Nicodano 2023][research_altieri_nicodano_2023].

## Measurement Critiques

The selection critique questions the comparison group.
A second family of critiques questions the inputs.

**Segment data.**
Villalonga rebuilt business units from the Business Information Tracking Series,
a census database that covers the United States economy at the establishment level,
on the argument that such units are more consistently and objectively defined than the segments firms report.
On a sample that shows a discount with segment data,
the rebuilt units show a diversification premium that is robust to variations in sample, business-unit definition and measures of excess value
[Villalonga 2004][research_villalonga_2004].
Segment reporting itself changed in 1997,
when Statement of Financial Accounting Standards No. 131,
or SFAS 131,
established a new segment-reporting standard for public companies in the United States
[He 2009][research_he_2009].
According to Berger and Hann, the new standard increased the number of reported segments,
revealed previously hidden information about diversification,
and affected market valuations
[Berger and Hann 2003][research_berger_hann_2003].
A discount measured across the change in standard is therefore measured on two different definitions of a segment.
The same paper finds a diversification premium in data after 1997,
using diversity measures and a control for the endogeneity of the decision to diversify,
and a discount in the earlier data that is statistically weaker once endogeneity is controlled for
[He 2009][research_he_2009].

**The book value of debt.**
The standard measure adds the market value of equity to the book value of debt.
Mansi and Reeb argue that because diversification lowers risk,
the debt of a diversified firm is worth more relative to its book value than the debt of a focused firm,
so that using book values understates the diversified firm's total capital.
They report that losses to shareholders from diversification depend on leverage,
that firms with no debt show no discount,
and that once the bias is addressed diversification is insignificantly related to excess value
[Mansi and Reeb 2002][research_mansi_reeb_2002].
Glaser and Müller estimate market values of debt for a whole sample of German firms.
Book values understate the value of diversified firms in that sample,
and mainly equity-financed firms show no discount
[Glaser and Müller 2010][research_glaser_muller_2010].
Ammann, Hoechle and Schmid also find that the discount rises with leverage and is absent for all-equity firms,
but conclude that using an imputed market value of debt reduces the discount only by a small fraction
[Ammann et al. 2011][research_ammann_hoechle_schmid_2011].
The worked example shows why the direct correction can be small.
Raising the debt of the hypothetical firm from its book value of 3,500 to a market value of 3,700
moves the sales-based excess value from $-0.1655$ to $\ln(10{,}200 / 11{,}800) = -0.1457$,
a change of 2.0 log points.

**Debt maturity.**
In data on 30,135 firms from 1978 to 2022,
Onali and Ye observe that multi-division firms have debt maturities at least one year longer than stand-alone firms,
and that the excess values of both Berger and Ofek and of Mansi and Reeb rise with debt maturity.
They conclude that traditional measures of the discount could be misleading
[Onali and Ye 2025][research_onali_ye_2025].

**Measurement error in q.**
Whited treats q as a noisy proxy for investment opportunities.
With an estimator consistent under measurement error,
the study finds no evidence of inefficient allocation of investment across divisions,
and it attributes the earlier results to measurement error and to the correlation between investment opportunities and liquidity
[Whited 2001][research_whited_2001].
This critique is aimed at the evidence for one mechanism behind the discount rather than at the discount itself,
but it matters because that mechanism is a leading argument that the discount is real.

## Mechanisms That Would Make the Discount Real

If the discount is real,
something about operating businesses together must lower their combined value.
A leading candidate in the literature is the internal capital market,
the process by which headquarters reallocates cash among divisions.
Theory supplies arguments on both sides.

**The case that internal capital markets add value.**
Stein models a headquarters that, unlike a bank, has control rights that let it shift funds from weaker projects to stronger ones,
a practice the paper calls winner-picking,
and shows that this can create value even when it does nothing to relax the firm's overall credit constraint.
The model also implies that internal capital markets may work better when headquarters oversees a small and focused set of projects
[Stein 1997][research_stein_1997].
Duchin finds that multidivision firms hold less cash than stand-alone firms because their investment opportunities are diversified,
and the paper reads the pattern as efficient transfers from low-productivity to high-productivity divisions
[Duchin 2010][research_duchin_2010].
Hann, Ogneva and Ozbas estimate that diversified firms have on average a lower cost of capital than comparable portfolios of stand-alone firms,
with a larger benefit when segment cash flows are less correlated,
which is consistent with the coinsurance argument
[Hann et al. 2013][research_hann_ogneva_ozbas_2013].
During recessions, according to Dimitrov and Tice,
the sales and inventories of bank-dependent focused firms fall more
than those of comparable segments of bank-dependent diversified firms,
with no difference among firms that do not depend on banks
[Dimitrov and Tice 2006][research_dimitrov_tice_2006].
For Kuppuswamy and Villalonga, the value of diversification increased during the 2007 to 2009 financial crisis,
because conglomerates gained both financing and investment advantages
[Kuppuswamy and Villalonga 2016][research_kuppuswamy_villalonga_2016].

**The case that internal capital markets destroy value.**
Scharfstein and Stein model rent-seeking by division managers that leads headquarters to misallocate capital
[Scharfstein and Stein 2000][research_scharfstein_stein_2000].
Rajan, Servaes and Zingales model power struggles between divisions.
When divisions are similar,
funds flow from poor opportunities to good ones,
but as diversity in resources and opportunities grows,
funds can flow toward the least efficient division.
They report evidence consistent with this in a panel of diversified United States firms from 1980 to 1993
[Rajan et al. 2000][research_rajan_servaes_zingales_2000].
Shin and Stulz show that a segment's investment depends on the cash flow of the firm's other segments,
and that this sensitivity does not depend on whether the segment's investment opportunities are better than the others'
[Shin and Stulz 1998][research_shin_stulz_1998].
Lamont shows that after the 1986 fall in oil prices,
oil companies cut investment in their non-oil subsidiaries relative to industry medians,
evidence that the finance costs of different parts of one firm are linked
[Lamont 1997][research_lamont_1997].
Ozbas and Scharfstein document that unrelated segments of conglomerates invest less than stand-alone firms in high-q industries,
with larger differences where top management owns little of the firm
[Ozbas and Scharfstein 2009][research_ozbas_scharfstein_2009].
Kisgen and Kong use changes in federal government spending as demand shocks
and identify cross-subsidization between segments that worsens operating performance and increases the discount
[Kisgen and Kong 2022][research_kisgen_kong_2022].
Chen and Chen observe declines in both excess value and investment efficiency after asset purchases that increase a firm's diversity
[Chen and Chen 2011][research_chen_chen_2011].
Lamont and Polk use changes in industry investment as a source of variation that the firm does not choose,
and increases in diversity turn out to be negatively related to firm value,
a result they state is not caused by measurement error
[Lamont and Polk 2002][research_lamont_polk_2002].
Burch and Nanda reconstruct diversified firms after spin-offs and relate the gains in aggregate value to reductions in divisional diversity,
concluding that the discount is at least partly a real loss and not only an artifact of selection or measurement
[Burch and Nanda 2003][research_burch_nanda_2003].

**Agency and governance.**
Denis, Denis and Sarin report that diversification falls as managerial and blockholder ownership rises,
and that firms refocus after control threats, financial distress and management turnover.
They read this as evidence that agency problems sustain value-reducing diversification
[Denis et al. 1997][research_denis_denis_sarin_1997].
Hoechle, Schmid, Walter and Yermack find that adding governance variables narrows the discount by 16 to 21 percent in panel models
and by 37 percent in dynamic panel models,
in which the discount nonetheless remains negative and significant
[Hoechle et al. 2012][research_hoechle_2012].

**Models in which a discount is consistent with value maximization.**
A discount does not by itself show that managers are destroying value.
Maksimovic and Phillips build a neoclassical model in which a conglomerate discount is consistent with profit maximization,
and their plant-level data indicate that most conglomerates grow across segments in a way consistent with optimal behaviour
[Maksimovic and Phillips 2002][research_maksimovic_phillips_2002].
Matsusaka models diversification as a search for businesses that match a firm's organizational capabilities,
which can produce a discount alongside positive returns to diversification announcements
[Matsusaka 2001][research_matsusaka_2001].
Gomes and Livdan argue that the main empirical findings on diversification and performance are consistent with maximizing shareholder value
[Gomes and Livdan 2004][research_gomes_livdan_2004].
Anjos and Fracassi model synergies that decline as technology specializes,
which accounts for the long decline in diversification since the late 1970s and matches the size of the discount among other moments
[Anjos and Fracassi 2018][research_anjos_fracassi_2018].
In models of this kind the firms that diversify can differ systematically from those that stay focused,
which gives the selection term of the previous section an economic interpretation.

## Cash Flows, Discount Rates and Prices

A difference in value must come from a difference in expected cash flows,
a difference in the rate at which they are discounted,
or both.
A constant-growth valuation makes the point explicit.
Let $C$ be next year's cash flow,
$r$ the discount rate and $g$ the growth rate,
with $r > g$.

$$
V = \frac{C}{r - g}
\tag{12}
$$

For two firms with the same growth rate,
the log difference in their values splits into a cash-flow term and a discount-rate term.

$$
\ln V^{c} - \ln V^{s} = \left(\ln C^{c} - \ln C^{s}\right) - \left[\ln\left(r^{c} - g\right) - \ln\left(r^{s} - g\right)\right]
\tag{13}
$$

With $g = 4$ percent,
a discount rate of 10 percent for the conglomerate against 9 percent for the stand-alone portfolio
lowers value by the factor $0.05 / 0.06 = 0.833$,
a discount of 16.7 percent with identical cash flows.
Under these assumptions,
a difference of one percentage point in expected return is enough to produce a discount of the size usually reported.

Lamont and Polk find that firms trading at a discount have higher subsequent returns than firms trading at a premium,
and that slightly more than half of the cross-sectional variation in excess values is due to expected future cash flows,
with the remainder due to expected returns and the covariation of the two
[Lamont and Polk 2001][research_lamont_polk_2001].
Part of the variation in measured excess values therefore reflects differences in expected returns,
not differences in cash flow.
Reed, Saffi and Van Wesep offer one reason prices could differ without any difference in cash flows.
Investors disagree less about a conglomerate than about each of its divisions,
and when short sales are constrained greater disagreement raises prices,
so pure-play firms can trade above conglomerates for this reason alone.
Empirically, conglomerates show less disagreement among investors and fewer short-sale constraints than pure plays,
and both measures predict valuation differences
[Reed et al. 2021][research_reed_saffi_van_wesep_2021].
For banks, Bressan and Weissensteiner relate the financial conglomerate discount to lower skewness in returns
and to the higher expected returns that investors demand for it
[Bressan and Weissensteiner 2021][research_bressan_weissensteiner_2021].
If the discount is a difference in discount rates,
breaking a firm up captures it only if the pieces then attract a lower cost of capital,
which is a separate question from whether they are better run.

## The Discount Varies by Place, Time and Industry

The discount is not a constant.
Lins and Servaes estimate no significant discount for Germany,
a discount of 10 percent in Japan and one of 15 percent in the United Kingdom for 1992 and 1994.
In Japan only firms with strong links to an industrial group are discounted
[Lins and Servaes 1999][research_lins_servaes_1999].
In seven emerging markets at the end of 1995 the same authors measure a discount of about seven percent,
concentrated in firms that belong to industrial groups and in firms whose managers hold between 10 and 30 percent of the shares
[Lins and Servaes 2002][research_lins_servaes_2002].
Khanna and Palepu find that affiliates of the most diversified Indian business groups outperform unaffiliated firms,
in contrast to the lines of business of conglomerates in the United States
[Khanna and Palepu 2000][research_khanna_palepu_2000].
A 2011 study in a practitioner journal reports conglomerate multiples about 10 percent below those of pure-play peers in North America and Western Europe,
and premiums in Japan and Latin America
[Khorana et al. 2011][research_khorana_2011].

The discount also moves over time.
Servaes documents its fall from large to zero between the 1960s and the 1970s
[Servaes 1996][research_servaes_1996].
Rudolph and Schwetzler study firms in four regions
and conclude that the 2008 to 2009 financial crisis narrowed the discount where capital markets were well developed,
with an insignificant effect in Continental Europe
[Rudolph and Schwetzler 2013][research_rudolph_schwetzler_2013].
Doerr, Marin, Suverato and Verdier model international competition as a discipline on division managers
that improves capital allocation and lowers the discount,
confirm the prediction with the import shock from China,
and use it to explain why exporters show a smaller discount than non-exporters
[Doerr et al. 2025][research_doerr_2025].

Industry structure matters too.
In the data of Santalo and Becerra, diversified firms perform better in industries with few specialized competitors
and worse as specialized firms gain combined market share
[Santalo and Becerra 2008][research_santalo_becerra_2008].
Among financial firms,
Laeven and Levine conclude that conglomerates combining lending with other financial services are valued below portfolios of specialized firms,
and they attribute the gap to agency problems
[Laeven and Levine 2007][research_laeven_levine_2007].

In this article's reading,
a discount that changes sign between countries and shrinks in a crisis
is easier to explain as a variable relation between diversification and the surrounding capital markets
than as a fixed property of conglomerates.

## The Evidence from Breakups

A spin-off distributes the shares of a subsidiary to the parent's shareholders,
creating an independent listed company
[Corporate Spin-off][ref_corporate_spin_off].
It is the closest thing to an observation of a segment's stand-alone value,
since after it the former segment trades on its own.
It is still not a clean experiment,
because firms choose whether to spin off,
and the announcement price reflects the probability of completion and every other piece of news released with it.

The announcement evidence is positive on average.
Veld and Veld-Merkoulova combine 26 event studies in a meta-analysis
and obtain a significantly positive average abnormal return of 3.02 percent around the announcement.
Returns are higher for larger spin-offs, for tax-favoured or regulation-favoured divestments, and for spin-offs that improve industrial focus
[Veld and Veld-Merkoulova 2009][research_veld_2009].
Desai and Jain find that focus-increasing spin-offs earn larger announcement returns and larger long-run abnormal returns than spin-offs that do not increase focus
[Desai and Jain 1999][research_desai_jain_1999].

The long-run evidence is weaker than it once appeared.
Cusatis, Miles and Woolridge report positive abnormal returns for spun-off firms, their parents and the combinations,
but the abnormal performance is confined to firms involved in takeovers,
which suggests that the spin-off works by making a transfer of control cheaper
[Cusatis et al. 1993][research_cusatis_miles_woolridge_1993].
Veld and Veld-Merkoulova note that later studies with more refined statistical tests no longer find the long-run superior performance that early studies reported
[Veld and Veld-Merkoulova 2009][research_veld_2009].

The announcement return is not the same quantity as the discount.
An average announcement return of about 3 percent of the parent's value is far smaller than a measured discount of 13 to 15 percent,
but the two figures come from different samples,
and an announcement return is an expected value that discounts for the chance the spin-off fails or disappoints.
The comparison cannot show what fraction of a discount a breakup recovers.
If the samples were comparable,
the gap would suggest that the market does not expect a breakup to recover the whole measured discount,
but they are not,
so this is a hypothesis rather than a finding.

## What Can Be Computed for One Company

For a single listed firm,
the arithmetic of a sum-of-the-parts estimate is straightforward and fully reproducible.
Its uncertainty is not reported by the arithmetic,
and an honest estimate states it.
The following procedure keeps the modelling choices visible.

1. Identify the segments from the firm's segment disclosures,
and record that their boundaries are management's choice.
2. For each segment,
choose a peer set of focused listed firms,
and match on size and age as well as industry,
since Hund, Monk and Tice find that matching on industry alone biases the result
[Hund et al. 2024][research_hund_monk_tice_2024].
3. Compute the imputed value on more than one base,
such as sales, assets and operating earnings,
and report the range rather than a single figure.
4. Use the market value of debt where it can be estimated,
and state the leverage of the firm,
since several studies find the discount concentrated in levered firms
[Mansi and Reeb 2002][research_mansi_reeb_2002]
[Ammann et al. 2011][research_ammann_hoechle_schmid_2011].
5. Subtract the cost of the headquarters and any shared services that the stand-alone firms would have to duplicate,
and add any tax benefits or financing advantages they would lose,
since the imputed value otherwise assumes these are zero.
6. Report the excess value as a range across these choices,
and treat any figure within that range as consistent with no discount at all if the range includes zero.

In the worked example the range across two bases alone runs from 4.6 to 15.3 percent,
and a size bias of 10 percent in the peers moves the upper figure from 15.3 to 5.8 percent.
An analyst who reports only one of these numbers is reporting a modelling choice as if it were a measurement.

## Epistemic State

**Facts reported by the cited papers.**
The definitions of the Berger and Ofek excess value and the Lang and Stulz comparison of q are those the papers publish.
The 13 to 15 percent average loss for 1986 to 1991 is Berger and Ofek's,
the international figures are those of Lins and Servaes,
the German figure of 7.9 to 11.5 percent is that of Eulerich and Fligge,
the governance reductions of 16 to 21 and 37 percent are those of Hoechle and coauthors,
and the 3.02 percent announcement return is the meta-analytic average of Veld and Veld-Merkoulova.
Each finding attributed to a paper is taken from that paper's abstract,
except for ten papers whose findings are taken from summaries of the abstract and from published listings.
Those are the papers of Cusatis and coauthors, Burch and Nanda, Desai and Jain, Glaser and Müller, Hann and coauthors,
Hoechle and coauthors, Laeven and Levine, Lamont and Polk 2002, Rudolph and Schwetzler, and Villalonga 2000.
None of the papers was read in full,
so details of sample construction, trimming and estimation are not reported here unless the abstract states them.
The two surveys and the Lewellen paper are cited for their subject and their argument as titled and widely summarized,
and the Scharfstein and Stein paper for the model its title describes.
The weighting by assets in the q example is one construction among several and is not claimed to be the one Lang and Stulz use.

**Analysis in this article.**
The counterfactual framing,
the treatment-effect decomposition,
the linearity of the imputed value in the peer multiples,
the averaging comparison
and the constant-growth decomposition
are standard algebra applied here to the question,
and each can be checked from the stated equations.
Every worked number comes from hypothetical inputs chosen to be plausible,
and none describes a real firm.
The worked examples show how large the effect of each modelling choice can be,
not how large it is in any published sample.

**Inference and judgment.**
The conclusion that the measure is settled while its interpretation is not
is a judgment about the state of a literature that remains active.
Papers published in 2024 and 2025 continue to question the standard measure on peer matching and on debt maturity,
while a 2024 study of German firms still measures a discount of 7.9 to 11.5 percent,
and the instrumental-variable and fixed-effect results conflict on assumptions that the data cannot test.
A reader who holds that firm fixed effects adequately control for selection
will weigh the Ammann and coauthors result more heavily than this article does,
and a reader who distrusts the available instruments will discount the Campa and Kedia and Eulerich and Fligge results.
Both positions are defensible.

## Out of Scope

- Valuation of any real company,
or any opinion on a proposed or completed breakup.
- Holding-company discounts on firms whose assets are themselves listed securities,
and the closed-end fund discount,
which raise a related but different measurement question.
- Geographic diversification across countries,
except where it is cited as a parallel to the selection argument.
- The strategy literature on related and unrelated diversification and on the role of the corporate centre.
- Tax treatment of spin-offs,
which affects whether a breakup is worth doing but not the size of the discount.
- Private conglomerates and family business groups that are not listed,
for which no market value of the whole exists.

## Conclusion

The mathematics of the measurement is established.
The Berger and Ofek excess value and the Lang and Stulz comparison of q are precisely defined,
easy to reproduce,
and have been applied to many samples in many countries.
Under them,
diversified firms in the United States in the 1980s and early 1990s were valued on average below the imputed values of their segments,
with a widely cited loss of 13 to 15 percent.

What the mathematics cannot do is observe the counterfactual it estimates.
The stand-alone value of a segment is imputed from other firms,
and the result depends on the accounting base,
on how the peers are matched,
on how debt is valued,
on how segments are defined
and on how extreme values are averaged.
The worked example in this article produces discounts from about 5 to 15 percent for one firm on reasonable choices,
and a size bias of about 15 percent in the peer multiples would move the larger figure to zero.

Whether conglomeration causes the measured gap remains contested.
Corrections for the selection of firms into diversification shrink the discount and sometimes reverse it,
while fixed-effect estimates, industry-shock designs and spin-off reconstructions find that part of it is real.
Its size varies with country, period, industry and the state of capital markets,
and part of its variation across firms reflects expected returns rather than cash flows.
A sum-of-the-parts gap for one company is best read as a range of estimates whose sign is not guaranteed,
and spin-off evidence does not show that a breakup reliably recovers it.

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 13 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 13, 11 are established and 2 are bespoke.
Values are in millions of dollars of total capital, taken as the market value of equity plus the book value of debt, and excess values are natural logarithms, so a difference of 0.01 is one log point and converts to a percentage only through Equation 4.

**Equation 1, Conglomerate Discount as a Counterfactual Difference.**
The discount is the value of the firm as it is less the sum of the values its segments would have as independent firms, a quantity whose second term is never observed for the same segments at the same time.
[Conglomerate Discount][ref_conglomerate_discount]

$$
\Delta = V^{c} - \sum_{i=1}^{n} V^{s}_{i}
\tag{1}
$$

**Equation 2, Imputed Value of a Diversified Firm.**
Each segment's accounting item is multiplied by the median ratio of total capital to that item among single-segment firms in its industry, and the products are summed.
[Berger and Ofek 1995][research_berger_ofek_1995]

$$
I(V) = \sum_{i=1}^{n} A_{i}\, m_{i}
\tag{2}
$$

**Equation 3, Excess Value.**
The excess value is the natural logarithm of the ratio of actual to imputed value, so a negative figure is a discount and a positive one a premium.
[Berger and Ofek 1995][research_berger_ofek_1995]

$$
EV = \ln\!\left(\frac{V}{I(V)}\right)
\tag{3}
$$

**Equation 4, Percentage Discount from a Logarithmic Excess Value.**
Exponentiating the excess value recovers the ratio of actual to imputed value, and one minus that ratio is the percentage shortfall.

$$
d = 1 - e^{EV}
\tag{4}
$$

**Equation 5, Sales-Based Imputed Value of the Hypothetical Firm.**
The imputed value of Equation 2 is evaluated with segment sales and the median capital-to-sales ratios of the three peer industries.
[Berger and Ofek 1995][research_berger_ofek_1995]

$$
I_{\text{sales}} = 4{,}000 \times 1.2 + 2{,}500 \times 1.6 + 1{,}500 \times 2.0 = 4{,}800 + 4{,}000 + 3{,}000 = 11{,}800
\tag{5}
$$

**Equation 6, Sales-Based Excess Value and Discount of the Hypothetical Firm.**
Equations 3 and 4 applied to the sales-based imputed value give an excess value of minus 0.1655 and a discount of 15.3 percent.
[Berger and Ofek 1995][research_berger_ofek_1995]

$$
EV_{\text{sales}} = \ln\!\left(\frac{10{,}000}{11{,}800}\right) = -0.1655,
\qquad
d_{\text{sales}} = 1 - e^{-0.1655} = 15.3\%
\tag{6}
$$

**Equation 7, Asset-Based Imputed Value of the Hypothetical Firm.**
The imputed value of Equation 2 is evaluated with segment assets and the median capital-to-assets ratios of the three peer industries.
[Berger and Ofek 1995][research_berger_ofek_1995]

$$
I_{\text{assets}} = 3{,}000 \times 1.5 + 2{,}800 \times 1.3 + 900 \times 2.6 = 4{,}500 + 3{,}640 + 2{,}340 = 10{,}480
\tag{7}
$$

**Equation 8, Asset-Based Excess Value and Discount of the Hypothetical Firm.**
Equations 3 and 4 applied to the asset-based imputed value give an excess value of minus 0.0469 and a discount of 4.6 percent for the same firm.
[Berger and Ofek 1995][research_berger_ofek_1995]

$$
EV_{\text{assets}} = \ln\!\left(\frac{10{,}000}{10{,}480}\right) = -0.0469,
\qquad
d_{\text{assets}} = 4.6\%
\tag{8}
$$

*Equation 9, Bespoke Bias in Excess Value from Mismeasured Peer Multiples.*
The article assumes that every peer multiple is too high by the same factor, so the error passes through the linear imputed value and lowers the measured excess value by the logarithm of that factor.
[Hund et al. 2024][research_hund_monk_tice_2024]

$$
EV_{\text{measured}} = EV_{\text{true}} - \ln(1 + b)
\tag{9}
$$

**Equation 10, Tobin's q and the Asset-Weighted Imputed q.**
The firm's q is its market value over the replacement cost of its assets, and its imputed q weights the median q of single-segment peers in each segment's industry by that segment's share of replacement cost.
[Tobin's q][ref_tobins_q]
[Lang and Stulz 1994][research_lang_stulz_1994]

$$
q = \frac{V}{K},
\qquad
\hat{q} = \sum_{i=1}^{n} \frac{K_{i}}{K}\, \bar{q}_{i}
\tag{10}
$$

**Equation 11, Decomposition of a Group Difference into Treatment Effect and Selection.**
Adding and subtracting the untreated outcome of diversified firms splits the raw difference in mean excess value into the effect of diversification on diversified firms and a selection term, an identity that holds in any sample.

$$
\underbrace{E[Y \mid D=1] - E[Y \mid D=0]}_{\text{measured discount}}
=
\underbrace{E[Y_{1} - Y_{0} \mid D=1]}_{\text{effect on diversified firms}}
+
\underbrace{E[Y_{0} \mid D=1] - E[Y_{0} \mid D=0]}_{\text{selection}}
\tag{11}
$$

**Equation 12, Constant-Growth Valuation.**
A cash flow that grows at a constant rate forever and is discounted at a higher constant rate has a present value equal to next year's cash flow divided by the difference of the two rates.

$$
V = \frac{C}{r - g}
\tag{12}
$$

*Equation 13, Bespoke Split of a Log Value Difference into Cash-Flow and Discount-Rate Terms.*
Taking logarithms of Equation 12 for the conglomerate and the stand-alone portfolio under the assumption of a common growth rate separates the value gap into a cash-flow term and a discount-rate term.

$$
\ln V^{c} - \ln V^{s} = \left(\ln C^{c} - \ln C^{s}\right) - \left[\ln\left(r^{c} - g\right) - \ln\left(r^{s} - g\right)\right]
\tag{13}
$$

### Notation

- $V^{c}$, the market value of the firm as it is, with its segments operated together
- $V^{s}_{i}$, the value segment $i$ would have as an independent firm, written $V^{s}$ for the stand-alone portfolio as a whole
- $I(V)$, the imputed value of the firm, the sum of its segments' imputed stand-alone values
- $A_{i}$, an accounting item of segment $i$, such as its sales or its assets, in the same currency units as $V$
- $m_{i}$, the median ratio of total capital to the same accounting item among single-segment firms in segment $i$'s industry
- $EV$, the excess value, the natural logarithm of actual over imputed value
- $b$, the proportional error common to every peer multiple
- $\hat{q}$, the imputed q, the replacement-cost-weighted average of the peer median $\bar{q}_{i}$
- $K_{i}$, the replacement cost of segment $i$'s assets, with $K$ their sum
- $Y_{1}$, the excess value a firm would have if diversified, with $Y_{0}$ the value it would have if focused and $D$ the indicator of diversification
- $C$, next year's cash flow, with $C^{c}$ for the conglomerate and $C^{s}$ for the stand-alone portfolio
- $r$, the discount rate, with $r^{c}$ and $r^{s}$ for the conglomerate and the stand-alone portfolio
- $g$, the constant growth rate of the cash flow, below the discount rate

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- Altieri, Michela, and Giovanna Nicodano. 2023. "Survival and Value: The Conglomerate Case." *European Financial Management* 30 (3): 1305–43. [https://doi.org/10.1111/eufm.12442][research_altieri_nicodano_2023]
- Ammann, Manuel, Daniel Hoechle, and Markus Schmid. 2011. "Is There Really No Conglomerate Discount?" *Journal of Business Finance & Accounting* 39 (1–2): 264–88. [https://doi.org/10.1111/j.1468-5957.2011.02261.x][research_ammann_hoechle_schmid_2011]
- Berger, Philip G., and Rebecca Hann. 2003. "The Impact of SFAS No. 131 on Information and Monitoring." *Journal of Accounting Research* 41 (2): 163–223. [https://doi.org/10.1111/1475-679x.00100][research_berger_hann_2003]
- Berger, Philip G., and Eli Ofek. 1995. "Diversification's Effect on Firm Value." *Journal of Financial Economics* 37 (1): 39–65. [https://doi.org/10.1016/0304-405x(94)00798-6][research_berger_ofek_1995]
- Bressan, Silvia, and Alex Weissensteiner. 2021. "The Financial Conglomerate Discount: Insights from Stock Return Skewness." *International Review of Financial Analysis* 74: 101662. [https://doi.org/10.1016/j.irfa.2021.101662][research_bressan_weissensteiner_2021]
- Burch, Timothy R., and Vikram Nanda. 2003. "Divisional Diversity and the Conglomerate Discount: Evidence from Spinoffs." *Journal of Financial Economics* 70 (1): 69–98. [https://doi.org/10.1016/s0304-405x(03)00142-9][research_burch_nanda_2003]
- Chang, Sungyong, Bruce Kogut, and Jae-Suk Yang. 2016. "Global Diversification Discount and Its Discontents: A Bit of Self-Selection Makes a World of Difference." *Strategic Management Journal* 37 (11): 2254–74. [https://doi.org/10.1002/smj.2574][research_chang_kogut_yang_2016]
- Chen, Sheng-Syan, and I-Ju Chen. 2011. "Inefficient Investment and the Diversification Discount: Evidence from Corporate Asset Purchases." *Journal of Business Finance & Accounting* 38 (7–8): 887–914. [https://doi.org/10.1111/j.1468-5957.2011.02251.x][research_chen_chen_2011]
- Comment, Robert, and Gregg A. Jarrell. 1995. "Corporate Focus and Stock Returns." *Journal of Financial Economics* 37 (1): 67–87. [https://doi.org/10.1016/0304-405x(94)00777-x][research_comment_jarrell_1995]
- Cusatis, Patrick J., James A. Miles, and J. Randall Woolridge. 1993. "Restructuring through Spinoffs." *Journal of Financial Economics* 33 (3): 293–311. [https://doi.org/10.1016/0304-405x(93)90009-z][research_cusatis_miles_woolridge_1993]
- Desai, Hemang, and Prem C. Jain. 1999. "Firm Performance and Focus: Long-Run Stock Market Performance Following Spinoffs." *Journal of Financial Economics* 54 (1): 75–101. [https://doi.org/10.1016/s0304-405x(99)00032-x][research_desai_jain_1999]
- Doerr, S., D. Marin, D. Suverato, and T. Verdier. 2025. "International Trade and the Allocation of Capital within Firms." *Journal of International Economics* 153: 104023. [https://doi.org/10.1016/j.jinteco.2024.104023][research_doerr_2025]
- Erdorf, Stefan, Thomas Hartmann-Wendels, Nicolas Heinrichs, and Michael Matz. 2013. "Corporate Diversification and Firm Value: A Survey of Recent Literature." *Financial Markets and Portfolio Management* 27 (2): 187–215. [https://doi.org/10.1007/s11408-013-0209-6][research_erdorf_2013]
- Eulerich, Marc, and Benjamin Fligge. 2024. "Reevaluating the Conglomerate Discount in Germany: The Role of Design Choices." *Journal of Business Economics* 95 (1): 155–85. [https://doi.org/10.1007/s11573-023-01188-y][research_eulerich_fligge_2024]
- Glaser, Markus, and Sebastian Müller. 2010. "Is the Diversification Discount Caused by the Book Value Bias of Debt?" *Journal of Banking & Finance* 34 (10): 2307–17. [https://doi.org/10.1016/j.jbankfin.2010.02.017][research_glaser_muller_2010]
- He, Xi. 2009. "Corporate Diversification and Firm Value: Evidence from Post-1997 Data." *International Review of Finance* 9 (4): 359–85. [https://doi.org/10.1111/j.1468-2443.2009.01096.x][research_he_2009]
- Hoechle, Daniel, Markus Schmid, Ingo Walter, and David Yermack. 2012. "How Much of the Diversification Discount Can Be Explained by Poor Corporate Governance?" *Journal of Financial Economics* 103 (1): 41–60. [https://doi.org/10.1016/j.jfineco.2011.03.025][research_hoechle_2012]
- Laeven, Luc, and Ross Levine. 2007. "Is There a Diversification Discount in Financial Conglomerates?" *Journal of Financial Economics* 85 (2): 331–67. [https://doi.org/10.1016/j.jfineco.2005.06.001][research_laeven_levine_2007]
- Lamont, Owen A., and Christopher Polk. 2002. "Does Diversification Destroy Value? Evidence from the Industry Shocks." *Journal of Financial Economics* 63 (1): 51–77. [https://doi.org/10.1016/s0304-405x(01)00089-7][research_lamont_polk_2002]
- Lins, Karl V., and Henri Servaes. 2002. "Is Corporate Diversification Beneficial in Emerging Markets?" *Financial Management* 31 (2): 5. [https://doi.org/10.2307/3666220][research_lins_servaes_2002]
- Martin, John D., and Akin Sayrak. 2003. "Corporate Diversification and Shareholder Value: A Survey of Recent Literature." *Journal of Corporate Finance* 9 (1): 37–57. [https://doi.org/10.1016/s0929-1199(01)00053-0][research_martin_sayrak_2003]
- Rudolph, Christin, and Bernhard Schwetzler. 2013. "Conglomerates on the Rise Again? A Cross-Regional Study on the Impact of the 2008–2009 Financial Crisis on the Diversification Discount." *Journal of Corporate Finance* 22: 153–65. [https://doi.org/10.1016/j.jcorpfin.2013.04.006][research_rudolph_schwetzler_2013]
- Veld, Chris, and Yulia V. Veld-Merkoulova. 2009. "Value Creation through Spin-Offs: A Review of the Empirical Evidence." *International Journal of Management Reviews* 11 (4): 407–20. [https://doi.org/10.1111/j.1468-2370.2008.00243.x][research_veld_2009]

### Primary Sources, Non-Peer-Reviewed

- Anjos, Fernando, and Cesare Fracassi. 2018. "Technological Specialization and the Decline of Diversified Firms." *Journal of Financial and Quantitative Analysis* 53 (4): 1581–1614. [https://doi.org/10.1017/s0022109018000583][research_anjos_fracassi_2018]
- Campa, Jose Manuel, and Simi Kedia. 2002. "Explaining the Diversification Discount." *Journal of Finance* 57 (4): 1731–62. [https://doi.org/10.1111/1540-6261.00476][research_campa_kedia_2002]
- CustÓDio, CLÁUDIA. 2014. "Mergers and Acquisitions Accounting and the Diversification Discount." *Journal of Finance* 69 (1): 219–40. [https://doi.org/10.1111/jofi.12108][research_custodio_2014]
- Denis, David J., Diane K. Denis, and Atulya Sarin. 1997. "Agency Problems, Equity Ownership, and Corporate Diversification." *Journal of Finance* 52 (1): 135–60. [https://doi.org/10.1111/j.1540-6261.1997.tb03811.x][research_denis_denis_sarin_1997]
- Dimitrov, Valentin, and Sheri Tice. 2006. "Corporate Diversification and Credit Constraints: Real Effects across the Business Cycle." *Review of Financial Studies* 19 (4): 1465–98. [https://doi.org/10.1093/rfs/hhj028][research_dimitrov_tice_2006]
- Duchin, Ran. 2010. "Cash Holdings and Corporate Diversification." *Journal of Finance* 65 (3): 955–92. [https://doi.org/10.1111/j.1540-6261.2010.01558.x][research_duchin_2010]
- Gomes, Joao, and Dmitry Livdan. 2004. "Optimal Diversification: Reconciling Theory and Evidence." *Journal of Finance* 59 (2): 507–35. [https://doi.org/10.1111/j.1540-6261.2004.00641.x][research_gomes_livdan_2004]
- Graham, John R., Michael L. Lemmon, and Jack G. Wolf. 2002. "Does Corporate Diversification Destroy Value?" *Journal of Finance* 57 (2): 695–720. [https://doi.org/10.1111/1540-6261.00439][research_graham_lemmon_wolf_2002]
- Hann, Rebecca N., Maria Ogneva, and Oguzhan Ozbas. 2013. "Corporate Diversification and the Cost of Capital." *Journal of Finance* 68 (5): 1961–99. [https://doi.org/10.1111/jofi.12067][research_hann_ogneva_ozbas_2013]
- Hund, John E., Donald Monk, and Sheri Tice. 2024. "The Berger–Ofek Diversification Discount Is Just Poor Firm Matching." *Critical Finance Review* 13 (1–2): 1–44. [https://doi.org/10.1561/104.00000135][research_hund_monk_tice_2024]
- Khanna, Tarun, and Krishna Palepu. 2000. "Is Group Affiliation Profitable in Emerging Markets? An Analysis of Diversified Indian Business Groups." *Journal of Finance* 55 (2): 867–91. [https://doi.org/10.1111/0022-1082.00229][research_khanna_palepu_2000]
- Khorana, Ajay, Anil Shivdasani, Carsten Stendevad, and Sergey Sanzhar. 2011. "Spin-Offs: Tackling the Conglomerate Discount." *Journal of Applied Corporate Finance* 23 (4): 90–101. [https://doi.org/10.1111/j.1745-6622.2011.00355.x][research_khorana_2011]
- Kisgen, Darren J., and Lei Kong. 2022. "Cross-Subsidization in Conglomerate Firms: Evidence from Government Spending Shocks." *Journal of Financial and Quantitative Analysis* 59 (1): 339–68. [https://doi.org/10.1017/s0022109022001004][research_kisgen_kong_2022]
- Kuppuswamy, Venkat, and Belén Villalonga. 2016. "Does Diversification Create Value in the Presence of External Financing Constraints? Evidence from the 2007–2009 Financial Crisis." *Management Science* 62 (4): 905–23. [https://doi.org/10.1287/mnsc.2015.2165][research_kuppuswamy_villalonga_2016]
- Lamont, Owen. 1997. "Cash Flow and Investment: Evidence from Internal Capital Markets." *Journal of Finance* 52 (1): 83–109. [https://doi.org/10.1111/j.1540-6261.1997.tb03809.x][research_lamont_1997]
- Lamont, Owen A., and Christopher Polk. 2001. "The Diversification Discount: Cash Flows versus Returns." *Journal of Finance* 56 (5): 1693–1721. [https://doi.org/10.1111/0022-1082.00386][research_lamont_polk_2001]
- Lang, Larry H. P., and René M. Stulz. 1994. "Tobin's q, Corporate Diversification, and Firm Performance." *Journal of Political Economy* 102 (6): 1248–80. [https://doi.org/10.1086/261970][research_lang_stulz_1994]
- Lewellen, Wilbur G. 1971. "A Pure Financial Rationale for the Conglomerate Merger." *Journal of Finance* 26 (2): 521–37. [https://doi.org/10.1111/j.1540-6261.1971.tb00912.x][research_lewellen_1971]
- Lins, Karl, and Henri Servaes. 1999. "International Evidence on the Value of Corporate Diversification." *Journal of Finance* 54 (6): 2215–39. [https://doi.org/10.1111/0022-1082.00186][research_lins_servaes_1999]
- Maksimovic, Vojislav, and Gordon Phillips. 2002. "Do Conglomerate Firms Allocate Resources Inefficiently across Industries? Theory and Evidence." *Journal of Finance* 57 (2): 721–67. [https://doi.org/10.1111/1540-6261.00440][research_maksimovic_phillips_2002]
- Mansi, Sattar A., and David M. Reeb. 2002. "Corporate Diversification: What Gets Discounted?" *Journal of Finance* 57 (5): 2167–83. [https://doi.org/10.1111/0022-1082.00492][research_mansi_reeb_2002]
- Matsusaka, John G. 2001. "Corporate Diversification, Value Maximization, and Organizational Capabilities." *Journal of Business* 74 (3): 409–31. [https://doi.org/10.1086/321932][research_matsusaka_2001]
- Onali, Enrico, and Xiaoxia Ye. 2025. "Corporate Diversification and Debt Maturity." *Journal of Financial and Quantitative Analysis* 61 (3): 1387–1428. [https://doi.org/10.1017/s0022109025102238][research_onali_ye_2025]
- Ozbas, Oguzhan, and David S. Scharfstein. 2009. "Evidence on the Dark Side of Internal Capital Markets." *Review of Financial Studies* 23 (2): 581–99. [https://doi.org/10.1093/rfs/hhp071][research_ozbas_scharfstein_2009]
- Rajan, Raghuram, Henri Servaes, and Luigi Zingales. 2000. "The Cost of Diversity: The Diversification Discount and Inefficient Investment." *Journal of Finance* 55 (1): 35–80. [https://doi.org/10.1111/0022-1082.00200][research_rajan_servaes_zingales_2000]
- Reed, Adam V., Pedro A. C. Saffi, and Edward D. Van Wesep. 2021. "Short-Sales Constraints and the Diversification Puzzle." *Management Science* 67 (2): 1159–82. [https://doi.org/10.1287/mnsc.2019.3467][research_reed_saffi_van_wesep_2021]
- Santalo, Juan, and Manuel Becerra. 2008. "Competition from Specialized Firms and the Diversification–Performance Linkage." *Journal of Finance* 63 (2): 851–83. [https://doi.org/10.1111/j.1540-6261.2008.01333.x][research_santalo_becerra_2008]
- Scharfstein, David S., and Jeremy C. Stein. 2000. "The Dark Side of Internal Capital Markets: Divisional Rent-Seeking and Inefficient Investment." *Journal of Finance* 55 (6): 2537–64. [https://doi.org/10.1111/0022-1082.00299][research_scharfstein_stein_2000]
- Servaes, Henri. 1996. "The Value of Diversification during the Conglomerate Merger Wave." *Journal of Finance* 51 (4): 1201–25. [https://doi.org/10.1111/j.1540-6261.1996.tb04067.x][research_servaes_1996]
- Shin, H.-H., and R. M. Stulz. 1998. "Are Internal Capital Markets Efficient?" *Quarterly Journal of Economics* 113 (2): 531–52. [https://doi.org/10.1162/003355398555676][research_shin_stulz_1998]
- Stein, Jeremy C. 1997. "Internal Capital Markets and the Competition for Corporate Resources." *Journal of Finance* 52 (1): 111–33. [https://doi.org/10.1111/j.1540-6261.1997.tb03810.x][research_stein_1997]
- Villalonga, Belen. 2000. "Does Diversification Cause the 'Diversification Discount'?" Preprint, . [https://doi.org/10.2139/ssrn.227828][research_villalonga_2000]
- Villalonga, Belén. 2004. "Diversification Discount or Premium? New Evidence from the Business Information Tracking Series." *Journal of Finance* 59 (2): 479–506. [https://doi.org/10.1111/j.1540-6261.2004.00640.x][research_villalonga_2004]
- Whited, Toni M. 2001. "Is It Inefficient Investment That Causes the Diversification Discount?" *Journal of Finance* 56 (5): 1667–91. [https://doi.org/10.1111/0022-1082.00385][research_whited_2001]

### Tertiary Sources

- "Conglomerate (Company)." 2026. Wikipedia. Last modified September 7, at 04:37 (UTC). [https://en.wikipedia.org/w/index.php?title=Conglomerate\_(company)&oldid=1373662347][ref_conglomerate_company]
- "Conglomerate Discount." 2025. Wikipedia. Last modified November 15, at 15:06 (UTC). [https://en.wikipedia.org/w/index.php?title=Conglomerate\_discount&oldid=1322312579][ref_conglomerate_discount]
- "Corporate Spin-off." 2026. Wikipedia. Last modified October 9, at 01:56 (UTC). [https://en.wikipedia.org/w/index.php?title=Corporate\_spin-off&oldid=1379287175][ref_corporate_spin_off]
- "Sum-of-the-Parts Analysis." 2026. Wikipedia. Last modified September 5, at 00:25 (UTC). [https://en.wikipedia.org/w/index.php?title=Sum-of-the-parts\_analysis&oldid=1373271388][ref_sum_of_the_parts]
- "Tobin's q." 2026. Wikipedia. Last modified September 11, at 22:25 (UTC). [https://en.wikipedia.org/w/index.php?title=Tobin's\_q&oldid=1374409547][ref_tobins_q]

[ref_conglomerate_company]: https://en.wikipedia.org/w/index.php?title=Conglomerate_(company)&oldid=1373662347
[ref_conglomerate_discount]: https://en.wikipedia.org/w/index.php?title=Conglomerate_discount&oldid=1322312579
[ref_corporate_spin_off]: https://en.wikipedia.org/w/index.php?title=Corporate_spin-off&oldid=1379287175
[ref_sum_of_the_parts]: https://en.wikipedia.org/w/index.php?title=Sum-of-the-parts_analysis&oldid=1373271388
[ref_tobins_q]: https://en.wikipedia.org/w/index.php?title=Tobin's_q&oldid=1374409547
[research_altieri_nicodano_2023]: https://doi.org/10.1111/eufm.12442
[research_ammann_hoechle_schmid_2011]: https://doi.org/10.1111/j.1468-5957.2011.02261.x
[research_anjos_fracassi_2018]: https://doi.org/10.1017/s0022109018000583
[research_berger_hann_2003]: https://doi.org/10.1111/1475-679x.00100
[research_berger_ofek_1995]: https://doi.org/10.1016/0304-405x(94)00798-6
[research_bressan_weissensteiner_2021]: https://doi.org/10.1016/j.irfa.2021.101662
[research_burch_nanda_2003]: https://doi.org/10.1016/s0304-405x(03)00142-9
[research_campa_kedia_2002]: https://doi.org/10.1111/1540-6261.00476
[research_chang_kogut_yang_2016]: https://doi.org/10.1002/smj.2574
[research_chen_chen_2011]: https://doi.org/10.1111/j.1468-5957.2011.02251.x
[research_comment_jarrell_1995]: https://doi.org/10.1016/0304-405x(94)00777-x
[research_cusatis_miles_woolridge_1993]: https://doi.org/10.1016/0304-405x(93)90009-z
[research_custodio_2014]: https://doi.org/10.1111/jofi.12108
[research_denis_denis_sarin_1997]: https://doi.org/10.1111/j.1540-6261.1997.tb03811.x
[research_desai_jain_1999]: https://doi.org/10.1016/s0304-405x(99)00032-x
[research_dimitrov_tice_2006]: https://doi.org/10.1093/rfs/hhj028
[research_doerr_2025]: https://doi.org/10.1016/j.jinteco.2024.104023
[research_duchin_2010]: https://doi.org/10.1111/j.1540-6261.2010.01558.x
[research_erdorf_2013]: https://doi.org/10.1007/s11408-013-0209-6
[research_eulerich_fligge_2024]: https://doi.org/10.1007/s11573-023-01188-y
[research_glaser_muller_2010]: https://doi.org/10.1016/j.jbankfin.2010.02.017
[research_gomes_livdan_2004]: https://doi.org/10.1111/j.1540-6261.2004.00641.x
[research_graham_lemmon_wolf_2002]: https://doi.org/10.1111/1540-6261.00439
[research_hann_ogneva_ozbas_2013]: https://doi.org/10.1111/jofi.12067
[research_he_2009]: https://doi.org/10.1111/j.1468-2443.2009.01096.x
[research_hoechle_2012]: https://doi.org/10.1016/j.jfineco.2011.03.025
[research_hund_monk_tice_2024]: https://doi.org/10.1561/104.00000135
[research_khanna_palepu_2000]: https://doi.org/10.1111/0022-1082.00229
[research_khorana_2011]: https://doi.org/10.1111/j.1745-6622.2011.00355.x
[research_kisgen_kong_2022]: https://doi.org/10.1017/s0022109022001004
[research_kuppuswamy_villalonga_2016]: https://doi.org/10.1287/mnsc.2015.2165
[research_laeven_levine_2007]: https://doi.org/10.1016/j.jfineco.2005.06.001
[research_lamont_1997]: https://doi.org/10.1111/j.1540-6261.1997.tb03809.x
[research_lamont_polk_2001]: https://doi.org/10.1111/0022-1082.00386
[research_lamont_polk_2002]: https://doi.org/10.1016/s0304-405x(01)00089-7
[research_lang_stulz_1994]: https://doi.org/10.1086/261970
[research_lewellen_1971]: https://doi.org/10.1111/j.1540-6261.1971.tb00912.x
[research_lins_servaes_1999]: https://doi.org/10.1111/0022-1082.00186
[research_lins_servaes_2002]: https://doi.org/10.2307/3666220
[research_maksimovic_phillips_2002]: https://doi.org/10.1111/1540-6261.00440
[research_mansi_reeb_2002]: https://doi.org/10.1111/0022-1082.00492
[research_martin_sayrak_2003]: https://doi.org/10.1016/s0929-1199(01)00053-0
[research_matsusaka_2001]: https://doi.org/10.1086/321932
[research_onali_ye_2025]: https://doi.org/10.1017/s0022109025102238
[research_ozbas_scharfstein_2009]: https://doi.org/10.1093/rfs/hhp071
[research_rajan_servaes_zingales_2000]: https://doi.org/10.1111/0022-1082.00200
[research_reed_saffi_van_wesep_2021]: https://doi.org/10.1287/mnsc.2019.3467
[research_rudolph_schwetzler_2013]: https://doi.org/10.1016/j.jcorpfin.2013.04.006
[research_santalo_becerra_2008]: https://doi.org/10.1111/j.1540-6261.2008.01333.x
[research_scharfstein_stein_2000]: https://doi.org/10.1111/0022-1082.00299
[research_servaes_1996]: https://doi.org/10.1111/j.1540-6261.1996.tb04067.x
[research_shin_stulz_1998]: https://doi.org/10.1162/003355398555676
[research_stein_1997]: https://doi.org/10.1111/j.1540-6261.1997.tb03810.x
[research_veld_2009]: https://doi.org/10.1111/j.1468-2370.2008.00243.x
[research_villalonga_2000]: https://doi.org/10.2139/ssrn.227828
[research_villalonga_2004]: https://doi.org/10.1111/j.1540-6261.2004.00640.x
[research_whited_2001]: https://doi.org/10.1111/0022-1082.00385
