---
layout: post
mathjax: true
comments: true
title:  "Distribution and Getting Paid"
date:   2026-05-13 09:00:00 +0000
categories: business strategy startups
series: patents_and_startups
series_title: Patent and Startup Strategy
series_index: 11
---
<!-- A171 -->
<script>console.log("A171");</script>

A product can have the fit
that the [retention article][related_post_pmf] described,
and be built well
under the constraints the [execution article][related_post_build] set out,
and still fail.
It fails when the people who would keep it
cannot be reached at a price worth paying,
or when those reached
are charged less than they cost to win and to serve.
This article is about that last stretch,
[distribution][ref_distribution],
the work of reaching customers,
and getting paid,
the work of charging them enough.
The two together
decide whether a product with fit
is also a business,
and they decide it
through an arithmetic
that can be written plainly.
The treatment is general,
and it is information rather than business advice.

## A Brief History

The oldest mistake in the subject
is the belief that a good product sells itself,
that if it is built they will come.
They do not come,
or not in the numbers or at the cost required,
and the correction is associated
most sharply with Peter Thiel,
who argued that poor sales and distribution,
rather than a poor product,
are the more common cause of failure,
and that founders systematically neglect the question
because building is visible work
and selling feels beneath the engineer.
A parallel literature on traction
cataloged the limited set of channels
through which customers can actually be reached,
and urged a deliberate search among them
rather than a hopeful default to one.
Alongside this,
the software-as-a-service era
made the underlying accounting precise,
giving the discipline of unit economics,
the [lifetime value][ref_clv] of a customer
weighed against the [cost to acquire one][ref_cac],
and the [time][ref_payback] to earn that cost back,
which is the arithmetic this article develops.

## Distribution Is a Gate

Distribution is a stage of the funnel,
not a thing that happens after the real work.
The channels that reach customers are few,
search, advertising, sales teams, content,
partnerships, marketplaces, and word of mouth,
and each has a cost and a ceiling.
A founder who has not chosen a channel deliberately,
and measured what it costs to win a customer through it,
has not yet learned whether the product can be sold,
only that it can be built.
The one channel that does carry a product by itself
is the word of mouth of satisfied users,
and that channel is a dividend of fit
rather than a substitute for distribution,
which is why it is treated last
and not first.
Reaching the wrong people cheaply
is no better than failing to reach the right ones,
since only the customers
who keep using and keep paying,
the right people of [product-market fit][ref_pmf],
repay the cost of acquisition.

## What a Customer Is Worth

A paying customer yields a [contribution margin][ref_contribution_margin]
each period,
the revenue they bring
less the variable cost of serving them,
written $m$.
The customer churns at a rate $c$,
the same [churn][ref_churn] the [retention article][related_post_pmf] wrote as $\lambda$,
and so lasts on average $1 / c$ periods.
The undiscounted worth of the customer
is the margin times that lifetime,
$m \cdot (1/c) = m/c$.
Money arriving later is worth less
than money now,
so discounting the stream
at a rate $r$ per period
gives the [present value][ref_present_value]

$$
 V = \frac{m}{c + r}, 
\tag{1}
$$

which is the discounted area
under the very retention curve
the earlier article integrated.
Take a margin of twenty dollars a month,
a churn of five percent,
so an average life of twenty months,
and a discount rate of one percent a month.
The undiscounted worth is four hundred dollars,
and the discounted worth
is about three hundred and thirty-three,
the difference being the price of waiting.

## What a Customer Costs

The cost to acquire a customer
is the total spent winning them,
the sales and marketing outlay
divided by the customers it produced,
written $A$.
The first condition of a business
is that a customer be worth more than they cost,

$$
 V > A, 
\tag{2}
$$

but mere positivity is too weak a test,
since overhead, failed experiments,
and the rising cost of later customers
all consume the gap.
A common standard of health
asks for a wide margin,

$$
 \frac{V}{A} \gtrsim 3, 
\tag{3}
$$

a customer worth at least three times the cost of winning them.
A prior condition is easy to forget,
that the per-period margin must itself be positive,
$m > 0$,
because a venture that loses money on each sale
does not make it up in volume.
It only loses faster.
At an acquisition cost of one hundred dollars,
the worth of three hundred and thirty-three
gives a ratio above three,
a healthy business,
while at three hundred dollars to acquire
the ratio falls near one,
a venture spending almost as much
to win a customer as the customer will ever return.

## Payback and Runway

The ratio says whether a customer pays off.
A second number says how soon.
The payback period
is the time to recover the acquisition cost
from the margin the customer pays,

$$
 t_{\text{payback}} = \frac{A}{m}. 
\tag{4}
$$

At one hundred dollars to acquire
and twenty a month in margin,
the cost is recovered in five months,
comfortably inside the twenty-month life.
A payback longer than the lifetime
is a loss disguised as a sale,
since the customer leaves before repaying.
Payback also governs growth.
A venture that recovers its acquisition cost quickly
can spend the returned money
to acquire again,
so that a given runway,
in the sense of the [execution article][related_post_build],
funds far more growth
when payback is short
than when the cash is tied up for years.

## Why Channels Saturate

The cost to acquire a customer
is not a constant.
The cheapest customers in a channel
are won first,
and as the channel is pushed harder
the marginal cost of the next customer rises.
Acquisition adds value
only while the cost of the next customer
stays below their worth,
$A_{\text{marginal}} < V$,
and the channel reaches its ceiling
where the two are equal,
beyond which each further customer
destroys value rather than creating it.
This rising marginal cost
is why a blended average
flatters a venture that is scaling,
and why no single channel
carries a business forever.
Growth past one channel's ceiling
requires finding another,
which is the deliberate search for channels
that the traction literature urged.

## The Cheapest Channel

The least costly channel
is the product recruiting for itself.
When satisfied users bring others,
the new customers each customer brings
is the [viral coefficient][ref_kfactor]
$k = i \cdot q$,
the number of invitations a user sends
times the fraction that convert.
One acquired customer
then begins a chain,
themselves, then their $k$ recruits,
then those recruits' $k$ each,
summing while $k < 1$ to

$$
 1 + k + k^2 + \cdots = \frac{1}{1 - k}. 
\tag{5}
$$

Each paid customer thus brings $1 / (1 - k)$ in total,
and the effective cost of acquisition falls to

$$
 A_{\text{eff}} = A\,(1 - k). 
\tag{6}
$$

At a coefficient of one half
the cost halves,
and at four fifths it falls to a fifth.
The effect on viability is direct,
since dividing the worth by this lower cost

$$
 \frac{V}{A_{\text{eff}}} = \frac{1}{1 - k} \cdot \frac{V}{A} 
\tag{7}
$$

multiplies the health ratio by the same factor.
A venture paying two hundred dollars
to acquire a customer worth three hundred and thirty-three,
a ratio of about one and two-thirds
and unviable on paid acquisition alone,
reaches a healthy three and a third
at a coefficient of one half,
rescued not by spending less
but by being worth talking about.
When $k$ reaches one,
the chain no longer converges,
[growth sustains itself][ref_viral],
and paid acquisition becomes a choice rather than a necessity.
A high coefficient is a dividend of the fit
the earlier article measured,
since only a product people genuinely want
is one they tell others about,
which is the sense in which
distribution and fit are not separate problems.

## Getting Paid

Reaching customers is half the stretch.
Charging them is the other.
A price must clear two bars,
sitting above the cost to serve,
so that the margin $m$ is positive,
and below the value the customer receives,
so that buying remains worth their while.
The room between those bars
is where a business lives,
and a product that delivers great value
but captures none of it in price
is a gift, not a company.
Users who will never pay,
however numerous,
are not customers,
and counting them as traction
is a form of the vanity metric
the retention article warned against.
Everything in this article
rests on the margin $m$,
which exists only when someone
is charged more than they cost.
Distribution decides whether they can be reached.
Pricing decides whether reaching them pays.

## Epistemic State

The quantities here are estimates,
and softer ones than the symbols suggest.
Churn, margin, and acquisition cost
all drift over time
and differ across customer segments,
so a single lifetime value
averages over a population
that is not uniform.
The acquisition cost in particular
rises with scale,
which means a healthy ratio measured small
can decay as a venture grows,
and a blended average
can conceal a marginal cost
already past the ceiling.
The threshold of three
is a convention drawn from experience,
not a theorem,
and the discount rate is a judgment.
The viral coefficient is rarely stable,
since it decays as easy adopters are used up,
and a coefficient above one
is rare and seldom lasting.
What survives these cautions
is the structure,
that a customer must be worth more than they cost,
by a margin and within a time,
and that the cost is not fixed
but climbs as channels saturate.
Throughout, this is general information,
and it is not business advice.

## Out of Scope

The tactics of particular channels,
search optimization, advertising auctions,
sales-team design, and content strategy,
are practical crafts
left to their own literatures.
The depth of pricing strategy,
segmentation, discrimination, and packaging,
is a large adjacent subject
touched only at its principle here.
The accounting conventions
that define acquisition cost and margin precisely
are matters for the finance function.
The durable advantage
that a cheap and defensible channel can become
belongs to the [final article][related_post_startup_moats],
which asks what makes the whole construction last.

## Conclusion

A product with fit
becomes a business
only when the people who want it
can be reached affordably
and charged enough.
The customer must be worth more than they cost,
$V > A$,
by a wide margin
and recovered in a time
shorter than the customer stays.
The cost is not fixed,
but rises as each channel saturates,
so growth is a search across channels,
and the cheapest channel of all,
the word of mouth of users who genuinely care,
is earned by the fit
of the [retention article][related_post_pmf]
rather than bought.
The [funnel][related_post_funnel]
placed distribution and revenue
among the stages that gate survival,
and this article gave them their arithmetic.
The [final article][related_post_startup_moats]
asks the question that remains
once a venture can build, hold, reach, and charge,
namely what keeps a rival
from doing the same,
and where durable advantage comes from.

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 7 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 7, 7 are established and 0 are bespoke.
Margins and acquisition costs are in dollars, margins per period, and the churn and discount rates are fractions per period, so the payback time is in the same periods and the health ratio and viral coefficient are dimensionless.

**Equation 1, Discounted Customer Lifetime Value.**
A margin received each period from a customer who churns at a constant rate, discounted at a rate per period, has the present value of the margin divided by the sum of the churn and discount rates.
[present value][ref_present_value]

$$
 V = \frac{m}{c + r}, 
\tag{1}
$$

**Equation 2, Customer Worth Exceeds Acquisition Cost.**
The first condition of a business is that a customer be worth more than the cost of acquiring them.

$$
 V > A, 
\tag{2}
$$

**Equation 3, Ratio of Lifetime Value to Acquisition Cost.**
A common standard of health asks for a customer to be worth at least three times the cost of acquisition.

$$
 \frac{V}{A} \gtrsim 3, 
\tag{3}
$$

**Equation 4, Payback Period.**
The payback period is the acquisition cost divided by the margin per period.

$$
 t_{\text{payback}} = \frac{A}{m}. 
\tag{4}
$$

**Equation 5, Geometric Series of Viral Recruits.**
A customer, their recruits and the recruits of those recruits sum as a geometric series to one over one less the viral coefficient while that coefficient is below one.
[viral coefficient][ref_kfactor]

$$
 1 + k + k^2 + \cdots = \frac{1}{1 - k}. 
\tag{5}
$$

**Equation 6, Effective Acquisition Cost with Virality.**
Spreading the cost of one paid customer across all the customers that customer brings reduces the acquisition cost by the factor one less the viral coefficient.
[viral coefficient][ref_kfactor]

$$
 A_{\text{eff}} = A\,(1 - k). 
\tag{6}
$$

**Equation 7, Health Ratio with Virality.**
Dividing the customer worth by the effective acquisition cost multiplies the health ratio by one over one less the viral coefficient.

$$
 \frac{V}{A_{\text{eff}}} = \frac{1}{1 - k} \cdot \frac{V}{A} 
\tag{7}
$$

### Notation

- $V$, the present value of a customer
- $m$, the contribution margin per period
- $c$, the churn rate, written $\lambda$ in the retention article
- $r$, the discount rate per period
- $A$, the acquisition cost per customer
- $t_{\text{payback}}$, the payback period
- $k$, the viral coefficient, invitations sent times the fraction that convert
- $A_{\text{eff}}$, the effective acquisition cost with virality

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Tertiary Sources

- "Churn Rate." 2026. Wikipedia. Last modified May 20, at 04:51 (UTC). [https://en.wikipedia.org/w/index.php?title=Churn\_rate&oldid=1355146978][ref_churn]
- "Contribution Margin." 2025. Wikipedia. Last modified July 22, at 21:30 (UTC). [https://en.wikipedia.org/w/index.php?title=Contribution\_margin&oldid=1302001403][ref_contribution_margin]
- "Customer Acquisition Cost." 2026. Wikipedia. Last modified April 30, at 19:47 (UTC). [https://en.wikipedia.org/w/index.php?title=Customer\_acquisition\_cost&oldid=1351891701][ref_cac]
- "Customer Lifetime Value." 2026. Wikipedia. Last modified May 30, at 06:30 (UTC). [https://en.wikipedia.org/w/index.php?title=Customer\_lifetime\_value&oldid=1356854689][ref_clv]
- "Distribution (Marketing)." 2026. Wikipedia. Last modified June 17, at 12:10 (UTC). [https://en.wikipedia.org/w/index.php?title=Distribution\_(marketing)&oldid=1359820884][ref_distribution]
- "K-Factor (Marketing)." 2025. Wikipedia. Last modified November 13, at 05:29 (UTC). [https://en.wikipedia.org/w/index.php?title=K-factor\_(marketing)&oldid=1321886196][ref_kfactor]
- "Payback Period." 2026. Wikipedia. Last modified April 24, at 14:35 (UTC). [https://en.wikipedia.org/w/index.php?title=Payback\_period&oldid=1350869590][ref_payback]
- "Present Value." 2026. Wikipedia. Last modified April 4, at 05:40 (UTC). [https://en.wikipedia.org/w/index.php?title=Present\_value&oldid=1347020181][ref_present_value]
- "Product–market Fit." 2026. Wikipedia. Last modified March 17, at 13:04 (UTC). [https://en.wikipedia.org/w/index.php?title=Product%E2%80%93market\_fit&oldid=1343963599][ref_pmf]
- "Viral Marketing." 2026. Wikipedia. Last modified April 23, at 08:34 (UTC). [https://en.wikipedia.org/w/index.php?title=Viral\_marketing&oldid=1350674899][ref_viral]

### Related Posts

- Sechter, Brendan. 2026. "The Funnel of Startup Failure." *Brendan A R Sechter's Development Blog*, May 10. [https://sgeos.github.io/business/strategy/startups/2026/05/10/funnel\_of\_startup\_failure.html][related_post_funnel]
- Sechter, Brendan. 2026. "Product-Market Fit." *Brendan A R Sechter's Development Blog*, May 11. [https://sgeos.github.io/business/strategy/startups/2026/05/11/product\_market\_fit.html][related_post_pmf]
- Sechter, Brendan. 2026. "Build and Execution Risk." *Brendan A R Sechter's Development Blog*, May 12. [https://sgeos.github.io/business/strategy/startups/2026/05/12/build\_and\_execution\_risk.html][related_post_build]
- Sechter, Brendan. 2026. "What It Takes to Succeed and Where Moats Come From." *Brendan A R Sechter's Development Blog*, May 14. [https://sgeos.github.io/business/strategy/startups/2026/05/14/what\_it\_takes\_to\_succeed\_and\_where\_moats\_come\_from.html][related_post_startup_moats]

[ref_cac]: https://en.wikipedia.org/w/index.php?title=Customer_acquisition_cost&oldid=1351891701
[ref_churn]: https://en.wikipedia.org/w/index.php?title=Churn_rate&oldid=1355146978
[ref_clv]: https://en.wikipedia.org/w/index.php?title=Customer_lifetime_value&oldid=1356854689
[ref_contribution_margin]: https://en.wikipedia.org/w/index.php?title=Contribution_margin&oldid=1302001403
[ref_distribution]: https://en.wikipedia.org/w/index.php?title=Distribution_(marketing)&oldid=1359820884
[ref_kfactor]: https://en.wikipedia.org/w/index.php?title=K-factor_(marketing)&oldid=1321886196
[ref_payback]: https://en.wikipedia.org/w/index.php?title=Payback_period&oldid=1350869590
[ref_pmf]: https://en.wikipedia.org/w/index.php?title=Product%E2%80%93market_fit&oldid=1343963599
[ref_present_value]: https://en.wikipedia.org/w/index.php?title=Present_value&oldid=1347020181
[ref_viral]: https://en.wikipedia.org/w/index.php?title=Viral_marketing&oldid=1350674899
[related_post_build]: {% post_url 2026-05-12-build_and_execution_risk %}
[related_post_funnel]: {% post_url 2026-05-10-funnel_of_startup_failure %}
[related_post_pmf]: {% post_url 2026-05-11-product_market_fit %}
[related_post_startup_moats]: {% post_url 2026-05-14-what_it_takes_to_succeed_and_where_moats_come_from %}
