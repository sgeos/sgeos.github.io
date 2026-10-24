---
layout: post
mathjax: true
comments: true
title: "Who Keeps the Value When a Company Splits"
date: 2026-08-16 09:00:00 +0000
categories: business economics finance
---

<!-- A380 -->
<script>console.log("A380");</script>

A spin-off makes a part of a company into a separate business
[Corporate Spin-off][ref_corporate_spin_off].
A natural question is whether a split can leave the valuable part of a business with one group of owners
and the rest with another.
This article asks whether there is theory on splitting a business so that value is concentrated in the shareholders who keep the core
rather than in those who hold the spun-off unit.

The answer begins with a constraint.
In an ordinary spin-off the parent distributes the new company's shares to its own shareholders
[Reverse Morris Trust][ref_reverse_morris_trust],
and it does so in proportion to their holdings,
so the people who keep the core are the same people who receive the spin-off,
and nothing about the split can favour one of them over another.
Value can move only between groups whose claims differ.
This article organizes the literature around those groups,
which are shareholders who choose differently in an exchange,
shareholders and creditors,
shareholders and the holders of liabilities that follow the spun-off unit,
current and future investors,
and shareholders and managers.
Each section below sets out one of these channels with a small model or worked numbers and the research behind it.

This is the third of three related articles.
The first concerns the value of a conglomerate measured against its parts
[What the Conglomerate Discount Measures][related_post_conglomerate_discount],
and the second concerns building an integrated enterprise by acquisition
[Building an Integrated Enterprise from Distressed Acquisitions][related_post_distressed_acquisitions].
This article does not value any real company,
does not give legal, tax or investment advice,
and does not survey the law of any jurisdiction.
Every numerical example is hypothetical.

## The Pro-Rata Spin-off Moves No Value Between Shareholders

Let a shareholder own the fraction $w$ of the parent before the spin-off,
let $V_{C}$ be the value of the core after the separation
and $V_{S}$ the value of the spun-off company,
with both values in the same money units.
In a pro-rata distribution the shareholder receives the same fraction $w$ of the new company,
so the shareholder's wealth afterwards is the following.

$$
W = w\,V_{C} + w\,V_{S} = w\left(V_{C} + V_{S}\right)
$$

The fraction $w$ is unchanged for every shareholder,
so the split changes each shareholder's wealth only through the total $V_{C} + V_{S}$,
and it changes everyone's wealth in the same proportion.
A shareholder who wants to keep only the core must sell the spun-off shares,
at whatever price the market offers,
and a shareholder who wants only the spun-off unit must sell the parent.
Any concentration of value has to come from somewhere other than the distribution itself.

On average the total has risen.
Miles and Rosenfeld report that spin-off announcements raise stock prices,
with larger relative gains for large spin-offs than for small ones
[Miles and Rosenfeld 1983][research_miles_rosenfeld_1983].
According to Krishnaswami and Subramaniam, firms that spin off have more information asymmetry than matched peers,
that it falls significantly afterwards,
and that the gains rise with the degree of asymmetry
[Krishnaswami and Subramaniam 1999][research_krishnaswami_subramaniam_1999].
Gertner, Powers and Scharfstein find that after a spin-off the investment of the new company becomes more sensitive to its industry's investment opportunities,
a change observed only where the unit is unrelated to its parent and where the market reacted favourably to the announcement
[Gertner et al. 2002][research_gertner_powers_scharfstein_2002].
The companion article on the conglomerate discount reviews the wider announcement and long-run evidence
[What the Conglomerate Discount Measures][related_post_conglomerate_discount].
All of this is a gain to the total,
which in a pro-rata spin-off every shareholder shares in proportion.

## Shareholders Who Choose Differently

The structure that does separate the two groups is an exchange.
An exchange offer is a form of tender offer in which securities rather than cash are offered as consideration
[Exchange Offer][ref_exchange_offer].
In a split-off, as the term is used in this article,
the parent offers shares of the subsidiary in exchange for its own shares.
Shareholders who tender leave the parent and hold the subsidiary,
and shareholders who do not tender own a larger fraction of the core.
For the parent this combines a divestiture with a repurchase of its own shares,
paid for with the subsidiary's shares instead of cash.
No academic study of split-offs specifically was found for this article,
so this section rests on the algebra of the exchange and on the theory of repurchases.

### The Algebra of the Exchange

Let $N$ be the number of parent shares before the exchange.
Let $V_{C}$ and $V_{S}$ be the true values of the core and the subsidiary,
so that the true value of a parent share before the exchange is $v = (V_{C} + V_{S}) / N$.
Let $p$ be the market price of a parent share,
$V_{S}^{m}$ the market value of all the subsidiary shares offered,
and $\pi$ the premium offered to induce tendering,
so that each tendered parent share receives subsidiary shares worth $(1 + \pi)\,p$ at market prices.
The number of parent shares retired, $n$, and the true gain to the shareholders who tender, $G$, are the following.

$$
n = \frac{V_{S}^{m}}{\left(1 + \pi\right) p},
\qquad
G = V_{S} - n\,v
$$

Measured at true values, the shareholders who stay lose exactly what the tendering shareholders gain,
because together they own the same core and subsidiary as before.
Write $m_{S} = V_{S}^{m} / V_{S}$ and $m_{P} = p / v$ for the ratios of market value to true value of the subsidiary and of the parent.
Substituting into $G$ shows that the shareholders who stay gain only under the following condition.

$$
\frac{m_{S}}{m_{P}} > 1 + \pi
$$

The shareholders who keep the core gain only if the market overvalues the subsidiary relative to the parent by more than the premium.
At fair prices, with $m_{S} = m_{P} = 1$,
any positive premium transfers value from those who stay to those who leave.

### Worked Numbers

Take a parent with 100 shares,
a core with a true value of 600 and a subsidiary with a true value of 400,
so a parent share has a true value of 10.

**Fair prices with a premium of 10 percent.**
Each tendered share receives subsidiary shares worth 11,
so the offer retires $400 / 11 = 36.36$ parent shares.
The 63.64 shares that remain own a core worth 600,
or 9.43 a share,
a loss of 5.7 percent against the 10 a share they held before.
The tendering shareholders gain 36.4 in total.

**The subsidiary overvalued by 10 percent with no premium.**
If the market values the subsidiary at 440 and the parent at 10.40 a share,
the offer at market prices retires $440 / 10.40 = 42.31$ shares.
The 57.69 that remain own the core,
whose true value is 10.40 a share,
a gain of 4.0 percent,
and the tendering shareholders lose 23.1.
Here $m_{S} / m_{P} = 1.10 / 1.04 = 1.058$, which exceeds $1 + \pi = 1$.

**The same overvaluation with a premium of 10 percent.**
The ratio of 1.058 is now below 1.10,
so the premium outweighs the overvaluation.
The offer retires 38.46 shares,
and the core is worth 9.75 a share to those who stay,
a loss of 2.5 percent.

### The Connection to Repurchases

The condition is the exchange-offer form of a familiar result about repurchases.
A firm whose managers believe its stock is trading below its intrinsic value may repurchase shares,
and a tender offer at a premium signals that belief
[Share Repurchase][ref_share_repurchase].
A split-off repurchases parent shares and pays with subsidiary shares,
so it benefits the shareholders who remain when the parent is cheap relative to the subsidiary.
Concentrating value in the core's continuing holders through a split-off is therefore a bet on relative misvaluation.
It also depends on who tenders,
since a shareholder who believes the subsidiary is overvalued would decline to take it.

## Shareholders and Creditors

A long-standing theory of value transfer in a separation concerns creditors.
Galai and Masulis combined option pricing with the capital asset pricing model
and showed how unanticipated changes in a firm's capital and asset structure can affect its debt and its equity differently
[Galai and Masulis 1976][research_galai_masulis_1976].
Jensen and Meckling set out the agency costs that arise between shareholders and creditors
when shareholders control decisions that change the risk borne by debt
[Jensen and Meckling 1976][research_jensen_meckling_1976].
A spin-off that moves assets out of reach of the parent's existing creditors is such a decision.

### A Worked Example with Equity as an Option

The structural model of debt treats a firm's equity as a call option on its assets,
with the face value of debt as the strike price.
Take a firm with assets worth 1,000,
a single zero-coupon debt with a face value of 600 due in five years,
an asset volatility of 30 percent
and a risk-free rate of 4 percent.
Under the Black and Scholes formula,
the equity is worth 542.4 and the debt 457.6,
below the risk-free value of 491.2 because default is possible.

Suppose the firm spins off assets worth 300 to its shareholders,
and the debt stays with the parent.
The parent's equity falls to 281.1,
and the shareholders also hold the spun-off assets worth 300,
for a total of 581.1.
The debt falls to 418.9.
The shareholders gain 38.7,
and the bondholders lose exactly 38.7,
or 8.4 percent of their claim,
with no change in the firm's total value.

### What Happens to Bondholders

Maxwell and Rao find that bondholders suffer a significant negative abnormal return in the month a spin-off is announced,
that the loss depends on the collateral removed with the subsidiary and on the parent's financial risk,
that credit ratings are more often downgraded than upgraded afterwards,
and that bondholder losses are larger the larger the shareholder gains.
The combined value of the traded debt and equity still rises,
so a transfer from bondholders does not explain the whole gain to shareholders
[Maxwell and Rao 2003][research_maxwell_rao_2003].
Parrino studies the 1993 Marriott spin-off.
The study documents a transfer from bondholders to shareholders and a fall in the total value of the firm,
with the notes and debentures still 194.6 million dollars below their pre-announcement level on the distribution date
and industry-adjusted shareholder gains of only 80.6 million dollars
[Parrino 1997][research_parrino_1997].

The allocation of debt between the two companies is where such a transfer would be engineered,
and Dittmar's evidence does not suggest that it is done routinely.
Dittmar finds that a spun-off subsidiary has a leverage ratio below its parent's and similar to that of comparable firms that were not spun off,
and that its leverage follows the predictions of the tradeoff theory of capital structure
[Dittmar 2004][research_dittmar_2004].
Within a pro-rata spin-off, loading the subsidiary with new debt and paying the proceeds to the parent moves no value between shareholders,
since the same people own both companies.
It moves value only away from existing creditors whose claims lose collateral,
and it raises the risk of financial distress in the subsidiary.

## Shareholders and Holders of Liabilities

The same logic applies to liabilities that are not debt,
such as environmental, pension and product liabilities.
If a liability is assigned to the spun-off company and that company has limited liability,
the shareholders hold an option to walk away from any part of the liability its assets cannot cover.

### The Limited-Liability Put

Let the spun-off company hold assets worth $A$ today,
with volatility $\sigma$,
and owe a liability $L$ due at time $T$.
The value the shareholders shed onto the holders of the liability is the value of a put option on the assets with strike $L$.

$$
\text{shed} = L\,e^{-rT} N\!\left(-d_{2}\right) - A\,N\!\left(-d_{1}\right),
\qquad
d_{1} = \frac{\ln\left(A / L\right) + \left(r + \tfrac{1}{2}\sigma^{2}\right) T}{\sigma\sqrt{T}},
\qquad
d_{2} = d_{1} - \sigma\sqrt{T}
$$

Here $N$ is the standard normal distribution function and $r$ the risk-free rate.
With assets of 300,
a liability of 400 due in five years,
a volatility of 30 percent and a risk-free rate of 4 percent,
the present value of the liability is 327.5,
and the put is worth 96.8.
If the liability had stayed with a solvent parent,
the shareholders would have borne all 327.5 of it.
Assigned to the spun-off company,
they expect to bear 96.8 less,
and the holders of the liability bear that amount instead.

### Where the Law Draws the Line

The law of fraudulent conveyance is designed to reach transfers of this kind.
A fraudulent conveyance is a transfer of property that prevents, hinders or delays the collection of a debt,
sometimes by rendering the party that makes the transfer insolvent,
and the law distinguishes actual fraud from constructive fraud
[Fraudulent Conveyance][ref_fraudulent_conveyance].
Tronox illustrates what can follow when a separation is challenged.
Kerr-McGee spun off its chemical business, Tronox, around 2005 and 2006,
and Tronox inherited several contaminated sites.
One account quoted on the company's Wikipedia page says that Kerr-McGee shifted environmental liabilities into Tronox while keeping its oil and gas assets.
Tronox fell to a penny stock in 2009 after the liabilities became known,
and its Chapter 11 plan created a litigation trust to pursue its claims against Anadarko,
which had acquired Kerr-McGee,
and against Kerr-McGee itself
[Tronox][ref_tronox].
The page cites a 2014 Associated Press report of a 5.15 billion dollar environmental settlement.
The settlement came about five years after the bankruptcy,
in litigation over value that the separation was alleged to have moved.

## Current and Future Investors

A split could concentrate value in current shareholders if the market predictably mispriced one of the pieces,
and an argument from earlier research is that the spun-off shares are sold indiscriminately by institutions that cannot hold them.
That argument has weaker support than its reputation suggests.
Abarbanell, Bushee and Smith Raedy find that investment strategies and fiduciary restrictions affect institutions' demand for spun-off shares,
but that their trading is in general not associated with abnormal price movements for parents or subsidiaries around the spin-off
[Abarbanell et al. 2003][research_abarbanell_bushee_raedy_2003].
A transfer of this kind would in any case run from the shareholders who sell to those who buy,
which is a matter of each holder's own trading,
not something the parent can direct to the holders of the core.

## Shareholders and Managers

Managers choose which unit to keep and which to spin off,
and the choice can serve their own interests.
Allen, Lummer, McConnell and Reed study spin-offs of units that the parent had acquired earlier.
The original acquisitions earned negative announcement returns for the bidder and for the combination,
and the returns at the spin-off are negatively correlated with the returns at the acquisition.
They interpret part of the gain from such spin-offs as the recovery of value destroyed by the earlier acquisition
[Allen et al. 1995][research_allen_lummer_mcconnell_reed_1995].
Chemmanur and Yan model a firm whose incumbent manager is better at running some divisions than others.
A spin-off raises the chance that a more able rival gains control,
which benefits all shareholders while costing the incumbent the private benefits of control
[Chemmanur and Yan 2004][research_chemmanur_yan_2004].
Seward and Walsh conclude, from 78 spin-offs completed between 1972 and 1987,
that the selection of the new chief executives, their compensation contracts and the staffing of the new boards can be seen as efficient,
but that these practices are not strongly related to the market's reaction to the announcement
[Seward and Walsh 1996][research_seward_walsh_1996].
In this evidence the managerial channel appears in spin-offs that recover value lost to past agency costs
or that expose managers to contests for control,
and in both cases the gain is shared by the shareholders of both companies in proportion.

## Structures That Separate Control Without a Full Split

Several structures let one group keep control of the core while others hold a claim on a unit.

**Equity carve-outs.**
A carve-out sells part of a subsidiary's shares to the public,
typically up to 20 percent,
while the parent keeps control
[Equity Carve-out][ref_equity_carve_out].
The new investors pay cash,
so the question is what the parent does with it.
Allen and McConnell document that carve-outs follow poor operating performance and high leverage,
and that the average excess return is 6.63 percent when the proceeds pay down debt
against minus 0.01 percent when they are retained for investment
[Allen and McConnell 1998][research_allen_mcconnell_1998].
Nanda explains the positive response to carve-outs within the Myers and Majluf framework,
in which firms issue equity in the subsidiary when the parent is undervalued
[Nanda 1991][research_nanda_1991]
[Myers and Majluf 1984][research_myers_majluf_1984].
Vijh tests that explanation on 336 carve-outs from 1980 to 1997 and rejects it in favour of gains from divestiture
[Vijh 2002][research_vijh_2002].

**Tracking stock.**
A tracking stock pays returns tied to one division while the company keeps one board and a consolidated balance sheet,
and it typically carries limited or no voting rights
[Tracking Stock][ref_tracking_stock].
It can leave control of the whole with the parent's shareholders while selling a claim on the division,
and the single board must balance the interests of the two classes of holders.
Chemmanur and Paeglis find that tracking stocks are issued by firms whose parts are more related than in spin-offs and carve-outs,
with an announcement effect similar in size to that of spin-offs.
Tracking stocks do not show the governance gains of spin-offs or their higher probability of a later takeover,
and their market-adjusted two-year returns are significantly lower than those of spin-offs and their parents
[Chemmanur and Paeglis 2001][research_chemmanur_paeglis_2001].

**The Reverse Morris Trust.**
In United States tax law,
a Reverse Morris Trust combines a spin-off with a merger,
so that the spun-off subsidiary merges with a target and the transaction can be largely tax-free
if the subsidiary's shareholders own more than half of the merged company.
A provision added to Section 355 of the Internal Revenue Code in 1997
imposes additional tax on the distribution if a 50 percent interest in the spun-off company or the parent is sold within two years
[Reverse Morris Trust][ref_reverse_morris_trust].
The structure concentrates ownership of the merged company in the parent's shareholders as a group,
but it does so in proportion to their holdings.

## Who Can Gain, and From Whom

The channels can be summarized by asking who gains and who pays.

| Channel | Who can gain | Who pays | What limits it |
|---|---|---|---|
| Pro-rata spin-off | All shareholders in proportion | Nobody, the total changes | Nothing to limit |
| Split-off | Holders who stay, if the subsidiary is overvalued by more than the premium | Holders who tender | The premium and the tendering holders' own judgment |
| Debt allocation | Shareholders | Existing creditors | Covenants, ratings and fraudulent conveyance |
| Liability allocation | Shareholders | Holders of the liability | Fraudulent conveyance and litigation |
| Mispricing after the spin-off | Investors who buy | Investors who sell | Weak evidence of systematic price pressure |
| Managerial choice | Shareholders of both companies | Managers who lose control benefits | The value lost to past agency costs |

Only the split-off moves value between two groups of shareholders,
and it does so only through a premium or a relative mispricing.
The transfers that move value toward shareholders as a whole come from creditors and the holders of liabilities,
and these are the transfers the law of fraudulent conveyance and the terms of debt contracts are written to prevent.

## Epistemic State

**Facts reported by the cited papers.**
Each finding attributed to a paper is taken from its abstract as recorded by Crossref or OpenAlex,
except for four papers whose findings are taken from abstracts reproduced in search-indexed listings.
Those are the papers of Abarbanell and coauthors, Chemmanur and Yan, Krishnaswami and Subramaniam, and Parrino.
For Galai and Masulis the summary found describes the paper's general result on changes in capital and asset structure,
and this article does not claim that the paper analyses spin-offs specifically.
Jensen and Meckling and Myers and Majluf are cited for their widely summarized arguments.
The descriptions of exchange offers, carve-outs, tracking stocks, the Reverse Morris Trust, share repurchases and fraudulent conveyance
come from Wikipedia articles,
and the Tronox account comes from the company's Wikipedia page and the reports it cites,
including the settlement figure, which comes from a cited news report rather than a court record.
None of the papers was read in full.

**Analysis in this article.**
The pro-rata identity,
the split-off transfer condition,
the bondholder example,
and the limited-liability put
are standard algebra and option pricing applied here.
The structural debt model is a simplification that treats all debt as one zero-coupon claim,
and every number in the examples is hypothetical.
No academic study of split-offs was found,
so the split-off section rests on this algebra and on the theory of repurchases.

**Inference and judgment.**
The organizing claim,
that value can move only between groups whose claims differ,
follows from the pro-rata identity.
The table of channels and the conclusion that the transfers available to shareholders as a whole come mainly from creditors and liability holders
are this article's synthesis.
A reader who knows of empirical work on split-off exchange terms should weigh it above the algebra given here.

## Out of Scope

- The tax requirements for a tax-free separation in the United States or elsewhere,
beyond the summary of the Reverse Morris Trust.
- The law of fraudulent conveyance and of directors' duties in any jurisdiction.
- Pension law, including the treatment of underfunded plans in a separation.
- Dual-class share structures, as a separate literature on control.
- Valuation of any real spin-off, split-off or carve-out.

## Conclusion

Theory on separating a business is well developed,
but it does not support a way to concentrate value in the shareholders who keep the core through an ordinary spin-off.
A pro-rata distribution leaves every shareholder with the same fraction of both companies,
so it can only raise or lower the total that all of them share.

Value moves between groups only where their claims differ.
In a split-off,
shareholders who keep the core gain only if the market overvalues the subsidiary relative to the parent by more than the premium paid to induce tendering,
which makes the strategy a bet on relative mispricing rather than a structural advantage.
Shareholders as a whole can gain at the expense of creditors when a separation removes collateral,
as the bond evidence and the Marriott case show,
and at the expense of the holders of liabilities when those liabilities are assigned to a spun-off company that cannot pay them.
Those are the transfers that debt covenants and the law of fraudulent conveyance exist to stop,
and the Tronox case illustrates how they can be challenged.
The managerial evidence points to spin-offs that recover value lost to earlier mistakes,
which benefits the shareholders of both companies alike.


## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- Chemmanur, Thomas J., and An Yan. 2004. "A Theory of Corporate Spin-Offs." *Journal of Financial Economics* 72 (2): 259–90. [https://doi.org/10.1016/j.jfineco.2003.05.002][research_chemmanur_yan_2004]
- Galai, Dan, and Ronald W. Masulis. 1976. "The Option Pricing Model and the Risk Factor of Stock." *Journal of Financial Economics* 3 (1–2): 53–81. [https://doi.org/10.1016/0304-405x(76)90020-9][research_galai_masulis_1976]
- Jensen, Michael C., and William H. Meckling. 1976. "Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure." *Journal of Financial Economics* 3 (4): 305–60. [https://doi.org/10.1016/0304-405x(76)90026-x][research_jensen_meckling_1976]
- Krishnaswami, Sudha, and Venkat Subramaniam. 1999. "Information Asymmetry, Valuation, and the Corporate Spin-off Decision." *Journal of Financial Economics* 53 (1): 73–112. [https://doi.org/10.1016/s0304-405x(99)00017-3][research_krishnaswami_subramaniam_1999]
- Myers, Stewart C., and Nicholas S. Majluf. 1984. "Corporate Financing and Investment Decisions When Firms Have Information That Investors Do Not Have." *Journal of Financial Economics* 13 (2): 187–221. [https://doi.org/10.1016/0304-405x(84)90023-0][research_myers_majluf_1984]
- Parrino, Robert. 1997. "Spinoffs and Wealth Transfers: The Marriott Case." *Journal of Financial Economics* 43 (2): 241–74. [https://doi.org/10.1016/s0304-405x(96)00885-9][research_parrino_1997]
- Seward, James K., and James P. Walsh. 1996. "The Governance and Control of Voluntary Corporate Spin-Offs." *Strategic Management Journal* 17 (1): 25–39. [https://doi.org/10.1002/(sici)1097-0266(199601)17:1\<25::aid-smj797\>3.0.co;2-g][research_seward_walsh_1996]

### Primary Sources, Non-Peer-Reviewed

- Abarbanell, Jeffery S., Brian J. Bushee, and Jana Smith Raedy. 2003. "Institutional Investor Preferences and Price Pressure: The Case of Corporate Spin-Offs." *Journal of Business* 76 (2): 233–61. [https://doi.org/10.1086/367749][research_abarbanell_bushee_raedy_2003]
- Allen, Jeffrey W., Scott L. Lummer, John J. McConnell, and Debra K. Reed. 1995. "Can Takeover Losses Explain Spin-Off Gains?" *Journal of Financial and Quantitative Analysis* 30 (4): 465. [https://doi.org/10.2307/2331273][research_allen_lummer_mcconnell_reed_1995]
- Allen, Jeffrey W., and John J. McConnell. 1998. "Equity Carve-Outs and Managerial Discretion." *Journal of Finance* 53 (1): 163–86. [https://doi.org/10.1111/0022-1082.65022][research_allen_mcconnell_1998]
- Chemmanur, Thomas J., and Imants Paeglis. 2001. "Why Issue Tracking Stock? Insights from a Comparison with Spin-Offs and Carve-Outs." *Journal of Applied Corporate Finance* 14 (2): 102–14. [https://doi.org/10.1111/j.1745-6622.2001.tb00334.x][research_chemmanur_paeglis_2001]
- Dittmar, Amy. 2004. "Capital Structure in Corporate Spin-Offs." *Journal of Business* 77 (1): 9–43. [https://doi.org/10.1086/379860][research_dittmar_2004]
- Gertner, Robert, Eric Powers, and David Scharfstein. 2002. "Learning about Internal Capital Markets from Corporate Spin-Offs." *Journal of Finance* 57 (6): 2479–2506. [https://doi.org/10.1111/1540-6261.00503][research_gertner_powers_scharfstein_2002]
- Maxwell, William F., and Ramesh P. Rao. 2003. "Do Spin-Offs Expropriate Wealth from Bondholders?" *Journal of Finance* 58 (5): 2087–2108. [https://doi.org/10.1111/1540-6261.00598][research_maxwell_rao_2003]
- Miles, James A., and James D. Rosenfeld. 1983. "The Effect of Voluntary Spin-off Announcements on Shareholder Wealth." *Journal of Finance* 38 (5): 1597–1606. [https://doi.org/10.1111/j.1540-6261.1983.tb03843.x][research_miles_rosenfeld_1983]
- Nanda, Vikram. 1991. "On the Good News in Equity Carve-Outs." *Journal of Finance* 46 (5): 1717–37. [https://doi.org/10.1111/j.1540-6261.1991.tb04641.x][research_nanda_1991]
- Vijh, Anand M. 2002. "The Positive Announcement-Period Returns of Equity Carveouts: Asymmetric Information or Divestiture Gains?" *Journal of Business* 75 (1): 153–90. [https://doi.org/10.1086/323508][research_vijh_2002]

### Tertiary Sources

- "Corporate Spin-off." 2026. Wikipedia. Last modified October 9, at 01:56 (UTC). [https://en.wikipedia.org/w/index.php?title=Corporate\_spin-off&oldid=1379287175][ref_corporate_spin_off]
- "Equity Carve-out." 2025. Wikipedia. Last modified May 25, at 19:01 (UTC). [https://en.wikipedia.org/w/index.php?title=Equity\_carve-out&oldid=1292204263][ref_equity_carve_out]
- "Exchange Offer." 2026. Wikipedia. Last modified June 20, at 20:58 (UTC). [https://en.wikipedia.org/w/index.php?title=Exchange\_offer&oldid=1360333787][ref_exchange_offer]
- "Fraudulent Conveyance." 2026. Wikipedia. Last modified May 19, at 04:25 (UTC). [https://en.wikipedia.org/w/index.php?title=Fraudulent\_conveyance&oldid=1354956097][ref_fraudulent_conveyance]
- "Reverse Morris Trust." 2026. Wikipedia. Last modified June 9, at 18:44 (UTC). [https://en.wikipedia.org/w/index.php?title=Reverse\_Morris\_Trust&oldid=1358595870][ref_reverse_morris_trust]
- "Share Repurchase." 2026. Wikipedia. Last modified October 4, at 06:47 (UTC). [https://en.wikipedia.org/w/index.php?title=Share\_repurchase&oldid=1378386958][ref_share_repurchase]
- "Tracking Stock." 2026. Wikipedia. Last modified August 18, at 21:22 (UTC). [https://en.wikipedia.org/w/index.php?title=Tracking\_stock&oldid=1370052019][ref_tracking_stock]
- "Tronox." 2026. Wikipedia. Last modified September 15, at 13:05 (UTC). [https://en.wikipedia.org/w/index.php?title=Tronox&oldid=1375027432][ref_tronox]

### Related Posts

- Sechter, Brendan. 2026. "What the Conglomerate Discount Measures." *Brendan A R Sechter's Development Blog*, August 14. [https://sgeos.github.io/business/economics/finance/2026/08/14/conglomerate\_discount.html][related_post_conglomerate_discount]
- Sechter, Brendan. 2026. "Building an Integrated Enterprise from Distressed Acquisitions." *Brendan A R Sechter's Development Blog*, August 15. [https://sgeos.github.io/business/economics/finance/2026/08/15/distressed\_acquisitions\_and\_integration.html][related_post_distressed_acquisitions]

[ref_corporate_spin_off]: https://en.wikipedia.org/w/index.php?title=Corporate_spin-off&oldid=1379287175
[ref_equity_carve_out]: https://en.wikipedia.org/w/index.php?title=Equity_carve-out&oldid=1292204263
[ref_exchange_offer]: https://en.wikipedia.org/w/index.php?title=Exchange_offer&oldid=1360333787
[ref_fraudulent_conveyance]: https://en.wikipedia.org/w/index.php?title=Fraudulent_conveyance&oldid=1354956097
[ref_reverse_morris_trust]: https://en.wikipedia.org/w/index.php?title=Reverse_Morris_Trust&oldid=1358595870
[ref_share_repurchase]: https://en.wikipedia.org/w/index.php?title=Share_repurchase&oldid=1378386958
[ref_tracking_stock]: https://en.wikipedia.org/w/index.php?title=Tracking_stock&oldid=1370052019
[ref_tronox]: https://en.wikipedia.org/w/index.php?title=Tronox&oldid=1375027432
[related_post_conglomerate_discount]: {% post_url 2026-08-14-conglomerate_discount %}
[related_post_distressed_acquisitions]: {% post_url 2026-08-15-distressed_acquisitions_and_integration %}
[research_abarbanell_bushee_raedy_2003]: https://doi.org/10.1086/367749
[research_allen_lummer_mcconnell_reed_1995]: https://doi.org/10.2307/2331273
[research_allen_mcconnell_1998]: https://doi.org/10.1111/0022-1082.65022
[research_chemmanur_paeglis_2001]: https://doi.org/10.1111/j.1745-6622.2001.tb00334.x
[research_chemmanur_yan_2004]: https://doi.org/10.1016/j.jfineco.2003.05.002
[research_dittmar_2004]: https://doi.org/10.1086/379860
[research_galai_masulis_1976]: https://doi.org/10.1016/0304-405x(76)90020-9
[research_gertner_powers_scharfstein_2002]: https://doi.org/10.1111/1540-6261.00503
[research_jensen_meckling_1976]: https://doi.org/10.1016/0304-405x(76)90026-x
[research_krishnaswami_subramaniam_1999]: https://doi.org/10.1016/s0304-405x(99)00017-3
[research_maxwell_rao_2003]: https://doi.org/10.1111/1540-6261.00598
[research_miles_rosenfeld_1983]: https://doi.org/10.1111/j.1540-6261.1983.tb03843.x
[research_myers_majluf_1984]: https://doi.org/10.1016/0304-405x(84)90023-0
[research_nanda_1991]: https://doi.org/10.1111/j.1540-6261.1991.tb04641.x
[research_parrino_1997]: https://doi.org/10.1016/s0304-405x(96)00885-9
[research_seward_walsh_1996]: https://doi.org/10.1002/(sici)1097-0266(199601)17:1<25::aid-smj797>3.0.co;2-g
[research_vijh_2002]: https://doi.org/10.1086/323508
