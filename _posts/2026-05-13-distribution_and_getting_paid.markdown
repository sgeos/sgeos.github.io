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

$$ V = \frac{m}{c + r}, $$

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

$$ V > A, $$

but mere positivity is too weak a test,
since overhead, failed experiments,
and the rising cost of later customers
all consume the gap.
A common standard of health
asks for a wide margin,

$$ \frac{V}{A} \gtrsim 3, $$

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

$$ t_{\text{payback}} = \frac{A}{m}. $$

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

$$ 1 + k + k^2 + \cdots = \frac{1}{1 - k}. $$

Each paid customer thus brings $1 / (1 - k)$ in total,
and the effective cost of acquisition falls to

$$ A_{\text{eff}} = A\,(1 - k). $$

At a coefficient of one half
the cost halves,
and at four fifths it falls to a fifth.
The effect on viability is direct,
since dividing the worth by this lower cost

$$ \frac{V}{A_{\text{eff}}} = \frac{1}{1 - k} \cdot \frac{V}{A} $$

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

## References

- [Reference, Churn Rate][ref_churn]
- [Reference, Contribution Margin][ref_contribution_margin]
- [Reference, Customer Acquisition Cost][ref_cac]
- [Reference, Customer Lifetime Value][ref_clv]
- [Reference, Distribution][ref_distribution]
- [Reference, K-factor][ref_kfactor]
- [Reference, Payback Period][ref_payback]
- [Reference, Present Value][ref_present_value]
- [Reference, Product-Market Fit][ref_pmf]
- [Reference, Viral Marketing][ref_viral]
- [Related Post, Build and Execution Risk][related_post_build]
- [Related Post, Product-Market Fit][related_post_pmf]
- [Related Post, The Funnel of Startup Failure][related_post_funnel]
- [Related Post, What It Takes to Succeed and Where Moats Come From][related_post_startup_moats]

[ref_cac]: https://en.wikipedia.org/wiki/Customer_acquisition_cost
[ref_churn]: https://en.wikipedia.org/wiki/Churn_rate
[ref_clv]: https://en.wikipedia.org/wiki/Customer_lifetime_value
[ref_contribution_margin]: https://en.wikipedia.org/wiki/Contribution_margin
[ref_distribution]: https://en.wikipedia.org/wiki/Distribution_(marketing)
[ref_kfactor]: https://en.wikipedia.org/wiki/K-factor_(marketing)
[ref_payback]: https://en.wikipedia.org/wiki/Payback_period
[ref_pmf]: https://en.wikipedia.org/wiki/Product-market_fit
[ref_present_value]: https://en.wikipedia.org/wiki/Present_value
[ref_viral]: https://en.wikipedia.org/wiki/Viral_marketing
[related_post_build]: {% post_url 2026-05-12-build_and_execution_risk %}
[related_post_funnel]: {% post_url 2026-05-10-funnel_of_startup_failure %}
[related_post_pmf]: {% post_url 2026-05-11-product_market_fit %}
[related_post_startup_moats]: {% post_url 2026-05-14-what_it_takes_to_succeed_and_where_moats_come_from %}
