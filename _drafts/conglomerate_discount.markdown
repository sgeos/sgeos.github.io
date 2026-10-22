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
The claim is often used to justify a breakup,
and it is usually stated as if the size of the gap were a known quantity.

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
That argument was made during the American conglomerate merger wave of the late 1960s,
when many firms diversified into unrelated industries.

The market did not reward that wave in the way its advocates expected.
Servaes studied the period directly and found no evidence that diversified firms were valued at a premium during the 1960s and 1970s.
He found a large diversification discount in the 1960s,
which declined to zero during the 1970s
[Servaes 1996][research_servaes_1996].
By the 1980s the trend had reversed toward focus.
Comment and Jarrell documented that reversal,
a positive relation between stock returns and increases in focus,
and the failure of diversified firms to exploit the financial economies of scope that coinsurance and internal capital markets were supposed to provide
[Comment and Jarrell 1995][research_comment_jarrell_1995].

The two measures still in use were published in 1994 and 1995.
Lang and Stulz compared the Tobin's q of diversified firms with that of portfolios of single-segment firms
[Lang and Stulz 1994][research_lang_stulz_1994],
and Berger and Ofek compared actual firm value with the sum of imputed stand-alone segment values
[Berger and Ofek 1995][research_berger_ofek_1995].
Both found a discount.
Much of the later literature uses one of these measures or argues against it.
Two surveys of the literature cover the decade after them
[Martin and Sayrak 2003][research_martin_sayrak_2003]
and the decade after that
[Erdorf, Hartmann-Wendels, Heinrichs and Matz 2013][research_erdorf_2013].

## The Quantity of Interest Is a Counterfactual

The phrase "value inside and outside a conglomerate" names a comparison between two states of the world,
only one of which exists at any time.
Let $V^{c}$ be the market value of the firm as it is,
with its segments operated together,
and let $V^{s}_{i}$ be the value segment $i$ would have if it were operated as an independent firm.
The delta the question asks about is the following.

$$
\Delta = V^{c} - \sum_{i=1}^{n} V^{s}_{i}
$$

The first term is observed for a listed firm.
The second term is never observed for the same segments at the same time,
because a segment that is operated inside the conglomerate is not also trading as an independent company.
Every measure in the literature therefore replaces $V^{s}_{i}$ with an estimate built from other firms,
and every dispute in the literature is, at bottom, a dispute about whether that estimate is a fair stand-in.

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
taken as the market value of equity plus the book value of debt.
$A_{i}$ is an accounting item for segment $i$,
such as its sales or its assets,
in the same currency units as $V$.
$m_{i}$ is the median, across single-segment firms in segment $i$'s industry,
of the ratio of total capital to the same accounting item,
and is a pure number.
The imputed value of the firm and its excess value are then defined as follows.

$$
I(V) = \sum_{i=1}^{n} A_{i}\, m_{i}
$$

$$
EV = \ln\!\left(\frac{V}{I(V)}\right)
$$

A negative excess value is a discount and a positive one is a premium.
Because the excess value is a logarithm,
it converts to a percentage shortfall of actual value below imputed value as follows.

$$
d = 1 - e^{EV}
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
$$

$$
EV_{\text{sales}} = \ln\!\left(\frac{10{,}000}{11{,}800}\right) = -0.1655,
\qquad
d_{\text{sales}} = 1 - e^{-0.1655} = 15.3\%
$$

The asset-based imputed value is the following.

$$
I_{\text{assets}} = 3{,}000 \times 1.5 + 2{,}800 \times 1.3 + 900 \times 2.6 = 4{,}500 + 3{,}640 + 2{,}340 = 10{,}480
$$

$$
EV_{\text{assets}} = \ln\!\left(\frac{10{,}000}{10{,}480}\right) = -0.0469,
\qquad
d_{\text{assets}} = 4.6\%
$$

The same firm, the same peers and the same market price give a discount of 15.3 percent on one accounting base and 4.6 percent on the other,
a gap of 11.9 log points.
Nothing in the definition says which base is correct.
Sales and assets each proxy for the scale of a segment,
and they disagree whenever a segment's asset intensity differs from that of its median peer,
as segment B's does here.
The measure is fully specified once the base is chosen,
but the choice of base is a modelling decision that moves the answer by about as much as the published average discount.

### The Measure Is Linear in the Peer Multiples

The imputed value is a weighted sum of peer multiples,
so a proportional error in the multiples passes straight through to the excess value.
If every peer multiple is too high by a factor $(1 + b)$,
the measured excess value is too low by $\ln(1 + b)$.

$$
EV_{\text{measured}} = EV_{\text{true}} - \ln(1 + b)
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
[Hund, Monk and Tice 2024][research_hund_monk_tice_2024].
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

The portfolio comparison works as follows.
Let $K_{i}$ be the replacement cost of segment $i$'s assets and $K = \sum_{i} K_{i}$.
Let $\bar{q}_{i}$ be the median q of single-segment firms in segment $i$'s industry.
The firm's own q and its imputed q are then defined as follows.

$$
q = \frac{V}{K},
\qquad
\hat{q} = \sum_{i=1}^{n} \frac{K_{i}}{K}\, \bar{q}_{i}
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
[Custódio 2014][research_custodio_2014].

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
They find a strong negative correlation between the choice to diversify and firm value,
and the discount in their estimates always drops and sometimes becomes a premium
[Campa and Kedia 2002][research_campa_kedia_2002].
Graham, Lemmon and Wolf study several hundred firms that expand by acquisition or add segments.
Much of the decline in excess value, in their account, occurs because the firms acquire business units that were already discounted,
not because diversifying destroys value.
They also find that excess value does not fall when the number of reported segments rises only because of a change in reporting
[Graham, Lemmon and Wolf 2002][research_graham_lemmon_wolf_2002].
Villalonga matches diversifying and single-segment firms on their propensity to diversify
and finds that on average diversification does not destroy value
[Villalonga 2000][research_villalonga_2000].
Chang, Kogut and Yang apply a selection correction to the discount on geographically diversified firms
and report results that contradict the earlier finding
[Chang, Kogut and Yang 2016][research_chang_kogut_yang_2016].

The selection argument has not won outright.
In the estimates of Ammann, Hoechle and Schmid the discount disappears in a Heckman selection model
but remains statistically and economically significant once firm fixed effects are included,
including within selection and instrumental-variable frameworks
[Ammann, Hoechle and Schmid 2011][research_ammann_hoechle_schmid_2011].
Eulerich and Fligge study about 6,000 German firm-years from 2000 to 2019
and find a discount of 7.9 to 11.5 percent.
They report that design choices related to self-selection have the largest effect on the result,
and with two-stage least squares they find no causal relation between diversification and market value
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
The segments that firms report are defined by their managers,
not by a statistical agency.
Villalonga rebuilt business units from the Business Information Tracking Series,
a census database that covers the United States economy at the establishment level.
On a sample that shows a discount with segment data,
she finds a diversification premium that is robust to variations in sample, business-unit definition and measures of excess value
[Villalonga 2004][research_villalonga_2004].
Segment reporting itself changed in 1997,
when Statement of Financial Accounting Standards No. 131 replaced the earlier standard.
According to Berger and Hann, the new standard increased the number of reported segments,
revealed previously hidden information about diversification,
and affected market valuations
[Berger and Hann 2003][research_berger_hann_2003].
A discount measured across the change in standard is therefore measured on two different definitions of a segment.

**The book value of debt.**
The standard measure adds the market value of equity to the book value of debt.
If diversification lowers risk,
the debt of a diversified firm is worth more relative to its book value than the debt of a focused firm,
and using book values understates the diversified firm's total capital.
Mansi and Reeb report that losses to shareholders from diversification depend on leverage,
that firms with no debt show no discount,
and that once the bias is addressed diversification is insignificantly related to excess value
[Mansi and Reeb 2002][research_mansi_reeb_2002].
Glaser and Müller reach a similar conclusion for German firms,
estimating market values of debt for the whole sample
[Glaser and Müller 2010][research_glaser_muller_2010].
Ammann, Hoechle and Schmid accept that the discount rises with leverage and is absent for all-equity firms,
but find that using an imputed market value of debt reduces the discount only by a small fraction
[Ammann, Hoechle and Schmid 2011][research_ammann_hoechle_schmid_2011].
The worked example shows why the direct correction can be small.
Raising the debt of the hypothetical firm from its book value of 3,500 to a market value of 3,700
moves the sales-based excess value from $-0.1655$ to $\ln(10{,}200 / 11{,}800) = -0.1457$,
a change of 2.0 log points.

**Debt maturity.**
Onali and Ye find, in data on 30,135 firms from 1978 to 2022,
that multi-division firms have debt maturities at least one year longer than stand-alone firms,
and that the excess values of both Berger and Ofek and of Mansi and Reeb rise with debt maturity.
They conclude that traditional measures of the discount could be misleading
[Onali and Ye 2025][research_onali_ye_2025].

**Measurement error in q.**
Whited treats q as a noisy proxy for investment opportunities.
With an estimator consistent under measurement error,
she finds no evidence of inefficient allocation of investment across divisions,
and she attributes the earlier results to measurement error and to the correlation between investment opportunities and liquidity
[Whited 2001][research_whited_2001].
This critique is aimed at the evidence for one mechanism behind the discount rather than at the discount itself,
but it matters because that mechanism is the main argument that the discount is real.

## Mechanisms That Would Make the Discount Real

If the discount is real,
something about operating businesses together must lower their combined value.
The leading candidate is the internal capital market,
the process by which headquarters reallocates cash among divisions.
Theory supplies arguments on both sides.

**The case that internal capital markets add value.**
Stein models a headquarters that, unlike a bank, has control rights that let it shift funds from weaker projects to stronger ones,
which he calls winner-picking,
and shows that this can create value even when it does nothing to relax the firm's overall credit constraint.
He adds that internal capital markets may work better when headquarters oversees a small and focused set of projects
[Stein 1997][research_stein_1997].
Duchin finds that multidivision firms hold less cash than stand-alone firms because their investment opportunities are diversified,
and he interprets the pattern as efficient transfers from low-productivity to high-productivity divisions
[Duchin 2010][research_duchin_2010].
Hann, Ogneva and Ozbas find that diversified firms have on average a lower cost of capital than comparable portfolios of stand-alone firms,
with a larger benefit when segment cash flows are less correlated,
which supports the coinsurance argument
[Hann, Ogneva and Ozbas 2013][research_hann_ogneva_ozbas_2013].
Dimitrov and Tice find that in recessions the sales and inventories of bank-dependent focused firms fall more than those of comparable segments of bank-dependent diversified firms,
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
[Rajan, Servaes and Zingales 2000][research_rajan_servaes_zingales_2000].
Shin and Stulz find that a segment's investment depends on the cash flow of the firm's other segments,
and that this sensitivity does not depend on whether the segment's investment opportunities are better than the others'
[Shin and Stulz 1998][research_shin_stulz_1998].
Lamont shows that after the 1986 fall in oil prices,
oil companies cut investment in their non-oil subsidiaries relative to industry medians,
evidence that the finance costs of different parts of one firm are linked
[Lamont 1997][research_lamont_1997].
Ozbas and Scharfstein find that unrelated segments of conglomerates invest less than stand-alone firms in high-q industries,
with larger differences where top management owns little of the firm
[Ozbas and Scharfstein 2009][research_ozbas_scharfstein_2009].
Kisgen and Kong use changes in federal government spending as demand shocks
and find cross-subsidization between segments that worsens operating performance and increases the discount
[Kisgen and Kong 2022][research_kisgen_kong_2022].
Chen and Chen find declines in both excess value and investment efficiency after asset purchases that increase a firm's diversity
[Chen and Chen 2011][research_chen_chen_2011].
Lamont and Polk use changes in industry investment as a source of variation that the firm does not choose,
and increases in diversity turn out to be negatively related to firm value,
a result they state is not caused by measurement error
[Lamont and Polk 2002][research_lamont_polk_2002].
Burch and Nanda reconstruct diversified firms after spin-offs and relate the gains in aggregate value to reductions in divisional diversity,
concluding that the discount is at least partly a real loss and not only an artifact of selection or measurement
[Burch and Nanda 2003][research_burch_nanda_2003].

**Agency and governance.**
Denis, Denis and Sarin find that diversification falls as managerial and blockholder ownership rises,
and that firms refocus after control threats, financial distress and management turnover.
They read this as evidence that agency problems sustain value-reducing diversification
[Denis, Denis and Sarin 1997][research_denis_denis_sarin_1997].
Hoechle, Schmid, Walter and Yermack find that adding governance variables narrows the discount by 16 to 21 percent in panel models
and by 37 percent in dynamic panel models,
in which the discount nonetheless remains negative and significant
[Hoechle, Schmid, Walter and Yermack 2012][research_hoechle_2012].

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
which explains the long decline in diversification since the late 1970s and matches the size of the discount among other moments
[Anjos and Fracassi 2018][research_anjos_fracassi_2018].
In these models firms that diversify are those whose focused prospects were weaker,
which is the selection term of the previous section given an economic interpretation.

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
$$

For two firms with the same growth rate,
the log difference in their values splits into a cash-flow term and a discount-rate term.

$$
\ln V^{c} - \ln V^{s} = \left(\ln C^{c} - \ln C^{s}\right) - \left[\ln\left(r^{c} - g\right) - \ln\left(r^{s} - g\right)\right]
$$

With $g = 4$ percent,
a discount rate of 10 percent for the conglomerate against 9 percent for the stand-alone portfolio
lowers value by the factor $0.05 / 0.06 = 0.833$,
a discount of 16.7 percent with identical cash flows.
A difference of one percentage point in expected return is enough to produce a discount of the size usually reported.

Lamont and Polk find that firms trading at a discount have higher subsequent returns than firms trading at a premium,
and that slightly more than half of the cross-sectional variation in excess values is due to expected future cash flows,
with the remainder due to expected returns and the covariation of the two
[Lamont and Polk 2001][research_lamont_polk_2001].
Part of the measured discount is therefore a higher expected return to holders of diversified firms,
not a loss of cash flow.
Reed, Saffi and Van Wesep offer one reason prices could differ without any difference in cash flows.
Investors disagree less about a conglomerate than about each of its divisions,
and when short sales are constrained greater disagreement raises prices,
so pure-play firms can trade above conglomerates for this reason alone.
In their data conglomerates show less disagreement among investors and fewer short-sale constraints than pure plays,
and both measures predict valuation differences
[Reed, Saffi and Van Wesep 2021][research_reed_saffi_van_wesep_2021].
For banks, Bressan and Weissensteiner relate the financial conglomerate discount to lower skewness in returns
and to the higher expected returns that investors demand for it
[Bressan and Weissensteiner 2021][research_bressan_weissensteiner_2021].
If the discount is a difference in discount rates,
breaking a firm up captures it only if the pieces then attract a lower cost of capital,
which is a separate question from whether they are better run.

## The Discount Varies by Place, Time and Industry

The discount is not a constant.
Lins and Servaes find no significant discount in Germany,
a discount of 10 percent in Japan and one of 15 percent in the United Kingdom for 1992 and 1994.
In Japan only firms with strong links to an industrial group are discounted
[Lins and Servaes 1999][research_lins_servaes_1999].
In seven emerging markets at the end of 1995 they find a discount of about seven percent,
concentrated in firms that belong to industrial groups and in firms whose managers hold between 10 and 30 percent of the shares
[Lins and Servaes 2002][research_lins_servaes_2002].
Khanna and Palepu find that affiliates of the most diversified Indian business groups outperform unaffiliated firms,
in contrast to the lines of business of conglomerates in the United States
[Khanna and Palepu 2000][research_khanna_palepu_2000].
Practitioner work from 2011 reports conglomerate multiples about 10 percent below those of pure-play peers in North America and Western Europe,
and premiums in Japan and Latin America
[Khorana, Shivdasani, Stendevad and Sanzhar 2011][research_khorana_2011].

The discount also moves over time.
Servaes documents its fall from large to zero between the 1960s and the 1970s
[Servaes 1996][research_servaes_1996].
Rudolph and Schwetzler study more than 65,000 firm-years across four regions
and conclude that the 2008 to 2009 financial crisis narrowed the discount where capital markets were well developed,
with an insignificant effect in Continental Europe
[Rudolph and Schwetzler 2013][research_rudolph_schwetzler_2013].
Doerr, Marin, Suverato and Verdier find that import competition from China disciplines division managers,
improves capital allocation and lowers the discount,
which they use to explain why exporters show a smaller discount than non-exporters
[Doerr, Marin, Suverato and Verdier 2025][research_doerr_2025].

Industry structure matters too.
Santalo and Becerra find that diversified firms perform better in industries with few specialized competitors
and worse as specialized firms gain combined market share
[Santalo and Becerra 2008][research_santalo_becerra_2008].
Among financial firms,
Laeven and Levine find that conglomerates combining lending with other financial services are valued below portfolios of specialized firms,
and they attribute the gap to agency problems
[Laeven and Levine 2007][research_laeven_levine_2007].

A discount that changes sign between countries and shrinks in a crisis is easier to explain as a variable relation between diversification and the surrounding capital markets than as a fixed property of conglomerates.

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
and find a significantly positive average abnormal return of 3.02 percent around the announcement.
Returns are higher for larger spin-offs, for tax-favoured or regulation-favoured divestments, and for spin-offs that improve industrial focus
[Veld and Veld-Merkoulova 2009][research_veld_2009].
Desai and Jain find that focus-increasing spin-offs earn larger announcement returns and larger long-run abnormal returns than spin-offs that do not increase focus
[Desai and Jain 1999][research_desai_jain_1999].

The long-run evidence is weaker than it once appeared.
Cusatis, Miles and Woolridge report positive abnormal returns for spun-off firms, their parents and the combinations,
but find that the abnormal performance is limited to firms involved in takeovers,
which suggests that the spin-off works by making a transfer of control cheaper
[Cusatis, Miles and Woolridge 1993][research_cusatis_miles_woolridge_1993].
Veld and Veld-Merkoulova note that later studies with more refined statistical tests no longer find the long-run superior performance that early studies reported
[Veld and Veld-Merkoulova 2009][research_veld_2009].

The announcement return is not the same quantity as the discount.
An average announcement return of about 3 percent of the parent's value is far smaller than a measured discount of 13 to 15 percent,
but the two figures come from different samples,
and an announcement return is an expected value that discounts for the chance the spin-off fails or disappoints.
The comparison cannot show what fraction of a discount a breakup recovers.
It does show that the market does not, on average, expect the whole measured discount to be recovered at announcement.

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
since the evidence above shows that industry matching alone biases the result.
3. Compute the imputed value on more than one base,
such as sales, assets and operating earnings,
and report the range rather than a single figure.
4. Use the market value of debt where it can be estimated,
and state the leverage of the firm,
since several studies find the discount concentrated in levered firms.
5. Subtract the cost of the headquarters and any shared services that the stand-alone firms would have to duplicate,
and add any tax benefits or financing advantages they would lose,
since the imputed value otherwise assumes these are zero.
6. Report the excess value as a range across these choices,
and treat any figure within that range as consistent with no discount at all if the range includes zero.

In the worked example the range across two bases alone runs from 4.6 to 15.3 percent,
and a plausible size bias in the peers is enough to move the upper figure most of the way to zero.
An analyst who reports only one of these numbers is reporting a modelling choice as if it were a measurement.

## Epistemic State

**Facts reported by the cited papers.**
The definitions of the Berger and Ofek excess value and the Lang and Stulz comparison of q are those the papers publish.
The 13 to 15 percent average loss for 1986 to 1991 is Berger and Ofek's,
the international figures are those of Lins and Servaes,
the German figure of 7.9 to 11.5 percent is that of Eulerich and Fligge,
the governance reductions of 16 to 21 and 37 percent are those of Hoechle and coauthors,
and the 3.02 percent announcement return is the meta-analytic average of Veld and Veld-Merkoulova.
Each finding attributed to a paper is taken from that paper's abstract or, for Cusatis and coauthors, Burch and Nanda, Desai and Jain, Glaser and Müller, Hann and coauthors, Hoechle and coauthors, Laeven and Levine, Lamont and Polk 2002, Rudolph and Schwetzler, and Villalonga 2000, from summaries of the abstract and published listings.
None of the papers was read in full,
so details of sample construction, trimming and estimation are not reported here unless the abstract states them.
The two surveys and the Lewellen paper are cited for their subject and their argument as titled and widely summarized.

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
Papers published in 2024 and 2025 continue to disagree on whether the Berger and Ofek discount survives better matching,
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
diversified firms in the United States in the 1980s and 1990s were valued on average below the imputed values of their segments,
with a widely cited loss of 13 to 15 percent.

What the mathematics cannot do is observe the counterfactual it estimates.
The stand-alone value of a segment is imputed from other firms,
and the result depends on the accounting base,
on how the peers are matched,
on how debt is valued,
on how segments are defined
and on how extreme values are averaged.
The worked example in this article produces discounts from about 5 to 15 percent for one firm on reasonable choices,
and a size bias in the peers can move the result to zero.

Whether conglomeration causes the measured gap remains contested.
Corrections for the selection of firms into diversification shrink the discount and sometimes reverse it,
while fixed-effect estimates, industry-shock designs and spin-off reconstructions find that part of it is real.
Its size varies with country, period, industry and the state of capital markets,
and part of it appears as higher expected returns rather than lower cash flows.
A sum-of-the-parts gap for one company is best read as a range of estimates whose sign is not guaranteed,
and spin-off evidence does not show that a breakup reliably recovers it.

## References

- [Reference, Conglomerate Discount, Wikipedia][ref_conglomerate_discount]
- [Reference, Conglomerate, Wikipedia][ref_conglomerate_company]
- [Reference, Corporate Spin-off, Wikipedia][ref_corporate_spin_off]
- [Reference, Sum-of-the-Parts Analysis, Wikipedia][ref_sum_of_the_parts]
- [Reference, Tobin's q, Wikipedia][ref_tobins_q]
- [Research, Altieri and Nicodano 2023, Survival and Value, The Conglomerate Case][research_altieri_nicodano_2023]
- [Research, Ammann, Hoechle and Schmid 2011, Is There Really No Conglomerate Discount?][research_ammann_hoechle_schmid_2011]
- [Research, Anjos and Fracassi 2018, Technological Specialization and the Decline of Diversified Firms][research_anjos_fracassi_2018]
- [Research, Berger and Hann 2003, The Impact of SFAS No. 131 on Information and Monitoring][research_berger_hann_2003]
- [Research, Berger and Ofek 1995, Diversification's Effect on Firm Value][research_berger_ofek_1995]
- [Research, Bressan and Weissensteiner 2021, The Financial Conglomerate Discount, Insights from Stock Return Skewness][research_bressan_weissensteiner_2021]
- [Research, Burch and Nanda 2003, Divisional Diversity and the Conglomerate Discount, Evidence from Spinoffs][research_burch_nanda_2003]
- [Research, Campa and Kedia 2002, Explaining the Diversification Discount][research_campa_kedia_2002]
- [Research, Chang, Kogut and Yang 2016, Global Diversification Discount and Its Discontents][research_chang_kogut_yang_2016]
- [Research, Chen and Chen 2011, Inefficient Investment and the Diversification Discount, Evidence from Corporate Asset Purchases][research_chen_chen_2011]
- [Research, Comment and Jarrell 1995, Corporate Focus and Stock Returns][research_comment_jarrell_1995]
- [Research, Cusatis, Miles and Woolridge 1993, Restructuring Through Spinoffs][research_cusatis_miles_woolridge_1993]
- [Research, Custódio 2014, Mergers and Acquisitions Accounting and the Diversification Discount][research_custodio_2014]
- [Research, Denis, Denis and Sarin 1997, Agency Problems, Equity Ownership, and Corporate Diversification][research_denis_denis_sarin_1997]
- [Research, Desai and Jain 1999, Firm Performance and Focus, Long-Run Stock Market Performance Following Spinoffs][research_desai_jain_1999]
- [Research, Dimitrov and Tice 2006, Corporate Diversification and Credit Constraints, Real Effects Across the Business Cycle][research_dimitrov_tice_2006]
- [Research, Doerr, Marin, Suverato and Verdier 2025, International Trade and the Allocation of Capital Within Firms][research_doerr_2025]
- [Research, Duchin 2010, Cash Holdings and Corporate Diversification][research_duchin_2010]
- [Research, Erdorf, Hartmann-Wendels, Heinrichs and Matz 2013, Corporate Diversification and Firm Value, A Survey of Recent Literature][research_erdorf_2013]
- [Research, Eulerich and Fligge 2024, Reevaluating the Conglomerate Discount in Germany, The Role of Design Choices][research_eulerich_fligge_2024]
- [Research, Glaser and Müller 2010, Is the Diversification Discount Caused by the Book Value Bias of Debt?][research_glaser_muller_2010]
- [Research, Gomes and Livdan 2004, Optimal Diversification, Reconciling Theory and Evidence][research_gomes_livdan_2004]
- [Research, Graham, Lemmon and Wolf 2002, Does Corporate Diversification Destroy Value?][research_graham_lemmon_wolf_2002]
- [Research, Hann, Ogneva and Ozbas 2013, Corporate Diversification and the Cost of Capital][research_hann_ogneva_ozbas_2013]
- [Research, Hoechle, Schmid, Walter and Yermack 2012, How Much of the Diversification Discount Can Be Explained by Poor Corporate Governance?][research_hoechle_2012]
- [Research, Hund, Monk and Tice 2024, The Berger and Ofek Diversification Discount Is Just Poor Firm Matching][research_hund_monk_tice_2024]
- [Research, Khanna and Palepu 2000, Is Group Affiliation Profitable in Emerging Markets?][research_khanna_palepu_2000]
- [Research, Khorana, Shivdasani, Stendevad and Sanzhar 2011, Spin-offs, Tackling the Conglomerate Discount][research_khorana_2011]
- [Research, Kisgen and Kong 2022, Cross-Subsidization in Conglomerate Firms, Evidence from Government Spending Shocks][research_kisgen_kong_2022]
- [Research, Kuppuswamy and Villalonga 2016, Does Diversification Create Value in the Presence of External Financing Constraints?][research_kuppuswamy_villalonga_2016]
- [Research, Laeven and Levine 2007, Is There a Diversification Discount in Financial Conglomerates?][research_laeven_levine_2007]
- [Research, Lamont 1997, Cash Flow and Investment, Evidence from Internal Capital Markets][research_lamont_1997]
- [Research, Lamont and Polk 2001, The Diversification Discount, Cash Flows Versus Returns][research_lamont_polk_2001]
- [Research, Lamont and Polk 2002, Does Diversification Destroy Value? Evidence from the Industry Shocks][research_lamont_polk_2002]
- [Research, Lang and Stulz 1994, Tobin's q, Corporate Diversification, and Firm Performance][research_lang_stulz_1994]
- [Research, Lewellen 1971, A Pure Financial Rationale for the Conglomerate Merger][research_lewellen_1971]
- [Research, Lins and Servaes 1999, International Evidence on the Value of Corporate Diversification][research_lins_servaes_1999]
- [Research, Lins and Servaes 2002, Is Corporate Diversification Beneficial in Emerging Markets?][research_lins_servaes_2002]
- [Research, Maksimovic and Phillips 2002, Do Conglomerate Firms Allocate Resources Inefficiently Across Industries?][research_maksimovic_phillips_2002]
- [Research, Mansi and Reeb 2002, Corporate Diversification, What Gets Discounted?][research_mansi_reeb_2002]
- [Research, Martin and Sayrak 2003, Corporate Diversification and Shareholder Value, A Survey of Recent Literature][research_martin_sayrak_2003]
- [Research, Matsusaka 2001, Corporate Diversification, Value Maximization, and Organizational Capabilities][research_matsusaka_2001]
- [Research, Onali and Ye 2025, Corporate Diversification and Debt Maturity][research_onali_ye_2025]
- [Research, Ozbas and Scharfstein 2009, Evidence on the Dark Side of Internal Capital Markets][research_ozbas_scharfstein_2009]
- [Research, Rajan, Servaes and Zingales 2000, The Cost of Diversity, The Diversification Discount and Inefficient Investment][research_rajan_servaes_zingales_2000]
- [Research, Reed, Saffi and Van Wesep 2021, Short-Sales Constraints and the Diversification Puzzle][research_reed_saffi_van_wesep_2021]
- [Research, Rudolph and Schwetzler 2013, Conglomerates on the Rise Again? The Impact of the 2008 to 2009 Financial Crisis on the Diversification Discount][research_rudolph_schwetzler_2013]
- [Research, Santalo and Becerra 2008, Competition from Specialized Firms and the Diversification and Performance Linkage][research_santalo_becerra_2008]
- [Research, Scharfstein and Stein 2000, The Dark Side of Internal Capital Markets, Divisional Rent-Seeking and Inefficient Investment][research_scharfstein_stein_2000]
- [Research, Servaes 1996, The Value of Diversification During the Conglomerate Merger Wave][research_servaes_1996]
- [Research, Shin and Stulz 1998, Are Internal Capital Markets Efficient?][research_shin_stulz_1998]
- [Research, Stein 1997, Internal Capital Markets and the Competition for Corporate Resources][research_stein_1997]
- [Research, Veld and Veld-Merkoulova 2009, Value Creation Through Spin-offs, A Review of the Empirical Evidence][research_veld_2009]
- [Research, Villalonga 2000, Does Diversification Cause the Diversification Discount?][research_villalonga_2000]
- [Research, Villalonga 2004, Diversification Discount or Premium? New Evidence from the Business Information Tracking Series][research_villalonga_2004]
- [Research, Whited 2001, Is It Inefficient Investment that Causes the Diversification Discount?][research_whited_2001]

[ref_conglomerate_company]: https://en.wikipedia.org/wiki/Conglomerate_(company)
[ref_conglomerate_discount]: https://en.wikipedia.org/wiki/Conglomerate_discount
[ref_corporate_spin_off]: https://en.wikipedia.org/wiki/Corporate_spin-off
[ref_sum_of_the_parts]: https://en.wikipedia.org/wiki/Sum-of-the-parts_analysis
[ref_tobins_q]: https://en.wikipedia.org/wiki/Tobin%27s_q
[research_altieri_nicodano_2023]: https://doi.org/10.1111/eufm.12442
[research_ammann_hoechle_schmid_2011]: https://doi.org/10.1111/j.1468-5957.2011.02261.x
[research_anjos_fracassi_2018]: https://doi.org/10.1017/s0022109018000583
[research_berger_hann_2003]: https://doi.org/10.1111/1475-679x.00100
[research_berger_ofek_1995]: https://doi.org/10.1016/0304-405X(94)00798-6
[research_bressan_weissensteiner_2021]: https://doi.org/10.1016/j.irfa.2021.101662
[research_burch_nanda_2003]: https://doi.org/10.1016/s0304-405x(03)00142-9
[research_campa_kedia_2002]: https://doi.org/10.1111/1540-6261.00476
[research_chang_kogut_yang_2016]: https://doi.org/10.1002/smj.2574
[research_chen_chen_2011]: https://doi.org/10.1111/j.1468-5957.2011.02251.x
[research_comment_jarrell_1995]: https://doi.org/10.1016/0304-405X(94)00777-X
[research_cusatis_miles_woolridge_1993]: https://doi.org/10.1016/0304-405X(93)90009-Z
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
