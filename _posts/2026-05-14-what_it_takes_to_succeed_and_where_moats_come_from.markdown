---
layout: post
mathjax: true
comments: true
title:  "What It Takes to Succeed and Where Moats Come From"
date:   2026-05-14 09:00:00 +0000
categories: business strategy startups
---

<!-- A172 -->
<script>console.log("A172");</script>

This series has walked the path a venture must travel,
from the base rates of [failure][related_post_why_fail],
through the [funnel][related_post_funnel]
of problem, fit, build, and reach,
to the [retention][related_post_pmf]
that signals a market,
the [execution][related_post_build]
that finds it before the money ends,
and the [distribution and pricing][related_post_distribution]
that turn it into revenue.
A venture that clears all of that
has a working business.
It does not yet have a durable one.
A working business earns a profit,
and a profit is a signal
that draws competitors,
who compete it away
unless something stops them.
That something is a moat,
and this final article
asks where moats come from,
and what, taken together,
it actually takes to succeed.
The treatment is general,
and it is information rather than business advice.

## A Brief History

The idea of a defensible business
is old,
but its sharpest popular form
is Warren Buffett's image of an [economic moat][ref_moat],
a structural barrier
that keeps rivals from the castle of profit.
Academic strategy gave the same intuition
a fuller anatomy,
in Michael Porter's account
of the forces that erode or protect
a [competitive advantage][ref_competitive_advantage],
and more recently
in Hamilton Helmer's enumeration
of a small number of distinct powers
from which durable advantage can come.
Across these treatments
runs a single distinction
that matters more than any taxonomy,
the difference between
being temporarily better,
which competition erases,
and being structurally protected,
which competition cannot.
The first is operational excellence,
worth having and never sufficient.
The second is a moat.
The [patent series][related_post_patent_moat]
argued that a patent
is rarely the second thing,
and this article completes that argument
by naming what usually is.

## Why Profit Invites Competition

A business that clears the funnel
earns more than its costs,
an [economic profit][ref_economic_profit],
a return above the price of the capital it uses.
That profit is a beacon.
In a market with free entry,
imitators arrive,
each competing away part of the surplus,
and in the textbook limit
the economic profit of an unprotected business
falls to zero.
Model the excess return
as eroding at a competitive rate $\delta$,

$$ \pi(t) = \pi_0\, e^{-\delta t}, $$

and the worth of the business
is the [present value][ref_present_value]
of that declining stream,
discounted at the cost of capital $r$,

$$ V = \int_0^\infty \pi_0\, e^{-\delta t}\, e^{-rt}\, dt = \frac{\pi_0}{r + \delta}. $$

A moat is whatever makes $\delta$ small.
With no barrier,
$\delta$ is large,
the profit is gone in a few years,
and the business is worth
little more than its current earnings.
With a strong barrier,
$\delta$ approaches zero,
and the value climbs toward the full perpetuity $\pi_0 / r$.
Take a business earning a million a year
above the cost of its capital,
with capital priced at ten percent.
Eroding quickly at $\delta = 0.5$,
it is worth about one and seven tenths million.
Protected so that $\delta = 0.05$,
it is worth about six and seven tenths million.
Shielded perfectly, at $\delta = 0$,
it is worth the full ten million.
More exactly,
a business realizes only the fraction

$$ \frac{V}{\pi_0 / r} = \frac{r}{r + \delta} $$

of the perpetuity a perfect moat would earn,
surrendering the rest,
$\delta / (r + \delta)$,
to competition.
At the fast erosion above
the business keeps one sixth of its ideal worth
and loses five sixths,
which is the precise sense
in which the moat, and not the profit,
is the asset.

## The Same Arithmetic, Three Times

That form should look familiar,
because this writing has met it twice before.
The worth of a customer
was the margin divided by churn plus discount.
The worth of a [trade secret][related_post_trade_secret]
was its yearly advantage
divided by the hazard of disclosure plus discount.
The worth of a business
is its profit divided by competitive erosion plus discount,

$$ \frac{m}{c + r}, \qquad \frac{A}{r + h}, \qquad \frac{\pi_0}{r + \delta}. $$

In each, a stream of value
decays at some hazard,
the churn $c$, the disclosure rate $h$, or the erosion $\delta$,
and is discounted at the same $r$,
and in each
the whole art is the lowering of that hazard.
A customer is held by retention,
a secret by secrecy,
a business by a moat,
and the three are one idea at three scales.
Durability is a small denominator.

## Where Moats Come From

A moat is not a single thing
but a small family of structural advantages,
and it is worth naming them,
because each is built differently
and each is produced
by a different part of the funnel already walked.

The first is the [network effect][ref_network_effect],
where the product grows more valuable
as more people use it.
By [Metcalfe's law][ref_metcalfe],
the value of a network
rises roughly with the square of its users,

$$ V_{\text{network}} \propto n^2, $$

so a leader with $n_A$ users
against a rival's $n_B$
holds a value advantage of $(n_A / n_B)^2$,
a lead that widens as it is used,
a $\delta$ that is negative for the leader.
This moat is the mature form
of the [virality][related_post_distribution]
the distribution article measured.

The second is [switching costs][ref_switching],
the price a customer pays to leave,
in money, effort, learning, or risk.
A customer defects
only when a rival is better
by more than that cost,

$$ \Delta v > s, $$

so a switching cost $s$
raises the bar a competitor must clear,
which lowers the churn $c$,
which is to say it lowers $\delta$ itself.
Retention and durability
are the same phenomenon
measured at the customer and at the firm.

The third is [economies of scale][ref_scale],
where a larger competitor
carries a lower cost per unit
and can price below
what a smaller rival can survive.
The fourth is the [brand][ref_brand],
the earned trust that makes a buyer
choose and pay more
without re-examining the choice.
Others include counter-positioning,
where an incumbent cannot copy a challenger
without damaging its existing business,
the cornered resource,
an exclusive hold on some scarce input,
and process power,
an operational capability
that rivals cannot quickly reproduce,
the durable form
of the [execution][related_post_build]
the build article prized.

## The Patent Is One Narrow Source

A [patent][ref_patent] belongs to this list,
but in one narrow place.
It is a cornered resource,
an exclusive legal hold
on a single invention,
and nothing more.
It is narrow,
covering only what its claims describe.
It is temporary,
expiring twenty years from filing.
And it protects an idea,
which the [first article of this series][related_post_why_fail]
showed was never the scarce thing.
This is why the [patent moat article][related_post_patent_moat]
concluded that a patent
is rarely a moat by itself,
and the present article explains the reason structurally.
The advantages that actually endure,
network effects, switching costs, scale, and brand,
are not granted by an office.
They are accumulated
by doing the funnel work so well
that the doing compounds.
A patent can guard a flank.
It is seldom the wall.

## Moats Are Earned in the Funnel

The taxonomy hides a unity.
Almost every durable advantage
is the residue of an earlier stage
performed excellently.
The fit that produced retention
becomes a switching-cost moat
when leaving grows costly.
The distribution that produced virality
becomes a network-effect moat
when each user makes the product better for the next.
The execution that produced speed
becomes process power
when the speed cannot be copied.
The growth that produced volume
becomes a scale moat
when volume lowers cost.
A moat is rarely a separate project,
bolted on after the business works.
It is the funnel done so well
that its advantages stop eroding
and begin to compound,
which is to say a $\delta$
driven not merely low
but, for the strongest companies, below zero.

## What It Takes to Succeed

Set against the whole series,
success has a shape.
It begins with a real problem,
since the [most common cause of death][related_post_why_fail]
is building what no market wanted.
It requires clearing the [funnel][related_post_funnel],
a conjunction of many stages
each of which can end the venture,
so that survival is improbable by construction
and failure is no disgrace.
It demands [fit][related_post_pmf],
a retention curve that flattens above zero,
found through [execution][related_post_build]
that spends its attempts
before the runway is gone,
and it demands [distribution and a price][related_post_distribution]
that make the found product
worth more than it costs to sell.
And then,
for the venture to last rather than merely live,
it demands a moat,
a structural reason
that the profit it earns
is not quickly competed away.
None of this can be wished into being.
The base rate is harsh,
the conjunction is long,
and most ventures fail.
What a founder controls
is the quality of each attempt
and the patience to convert
a fragile early advantage
into a durable one.

## Epistemic State

No moat is permanent.
The competitive erosion $\delta$
is never exactly zero,
and history is a record
of moats that looked impregnable
and were crossed,
by [creative destruction][ref_creative_destruction],
by counter-positioning,
and by network effects that reversed
when users left as quickly as they came.
The taxonomy of sources
is a convenience,
and its categories overlap,
since scale feeds brand
and networks raise switching costs.
The valuation models
are stylized to the point of caricature,
treating a single profit
eroding at a single constant rate,
where real businesses
earn lumpy returns
attacked unevenly on many sides.
The model is weakest, too, at its happiest end,
since a network leader's widening advantage
is a negative erosion,
an increasing return
that a single constant rate cannot represent,
that the simple perpetuity cannot value,
and that no business sustains without bound.
The figures are illustrations,
not measurements,
and $\pi_0$ and $\delta$
are estimated only with hindsight.
What survives these cautions
is the structure,
that profit invites competition,
that value is the profit
divided by the rate it erodes plus the discount,
and that the work of building a lasting company
is the slow reduction of that rate.
Throughout, this is general information,
and it is not business advice.

## Out of Scope

The detailed practice of competitive strategy,
the analysis of particular industries,
and the measurement of a given company's moat
are subjects for the strategy literature.
The mechanics of each moat type,
how network effects are engineered
or switching costs are built,
are large practical crafts
named but not taught here.
The legal machinery of patents and trade secrets
was the subject of
the [companion patent series][related_post_patent_moat]
and is not repeated.
The questions of antitrust,
which concern moats grown too wide,
are left aside entirely.

## Conclusion

A venture succeeds, in the small sense,
by clearing the funnel,
finding a real problem,
fitting a product to it,
building before the cash runs out,
and reaching and charging customers at a profit.
It succeeds in the large sense,
the sense that lasts,
only when that profit is defended
by a moat,
a structural barrier
that holds the competitive erosion $\delta$ near zero
and so lifts the value of the business
from a few years of earnings
toward a perpetuity.
The strongest moats
are not bought or granted.
They are the [funnel][related_post_funnel] done so well
that retention becomes switching cost,
virality becomes network effect,
and execution becomes process power.
A [patent][related_post_patent_moat]
may guard a corner of this,
but the wall is built
by the long work the series has described,
and by the rare combination
of a real market,
a sound execution,
and the patience
to turn an early lead
into a durable one.
Most ventures will not manage it,
which is what makes the base rate
the honest place
this series began.

## References

- [Reference, Brand Equity][ref_brand]
- [Reference, Competitive Advantage][ref_competitive_advantage]
- [Reference, Creative Destruction][ref_creative_destruction]
- [Reference, Economic Moat][ref_moat]
- [Reference, Economies of Scale][ref_scale]
- [Reference, Metcalfe's Law][ref_metcalfe]
- [Reference, Network Effect][ref_network_effect]
- [Reference, Patent][ref_patent]
- [Reference, Present Value][ref_present_value]
- [Reference, Profit in Economics][ref_economic_profit]
- [Reference, Switching Barriers][ref_switching]
- [Related Post, Build and Execution Risk][related_post_build]
- [Related Post, Distribution and Getting Paid][related_post_distribution]
- [Related Post, Patents, Trade Secrets, and the Disclosure Tradeoff][related_post_trade_secret]
- [Related Post, Product-Market Fit][related_post_pmf]
- [Related Post, The Funnel of Startup Failure][related_post_funnel]
- [Related Post, What Makes a Patent an Effective Moat][related_post_patent_moat]
- [Related Post, Why Startups Actually Fail][related_post_why_fail]

[ref_brand]: https://en.wikipedia.org/wiki/Brand_equity
[ref_competitive_advantage]: https://en.wikipedia.org/wiki/Competitive_advantage
[ref_creative_destruction]: https://en.wikipedia.org/wiki/Creative_destruction
[ref_economic_profit]: https://en.wikipedia.org/wiki/Profit_(economics)
[ref_metcalfe]: https://en.wikipedia.org/wiki/Metcalfe%27s_law
[ref_moat]: https://en.wikipedia.org/wiki/Economic_moat
[ref_network_effect]: https://en.wikipedia.org/wiki/Network_effect
[ref_patent]: https://en.wikipedia.org/wiki/Patent
[ref_present_value]: https://en.wikipedia.org/wiki/Present_value
[ref_scale]: https://en.wikipedia.org/wiki/Economies_of_scale
[ref_switching]: https://en.wikipedia.org/wiki/Switching_barriers
[related_post_build]: {% post_url 2026-05-12-build_and_execution_risk %}
[related_post_distribution]: {% post_url 2026-05-13-distribution_and_getting_paid %}
[related_post_funnel]: {% post_url 2026-05-10-funnel_of_startup_failure %}
[related_post_patent_moat]: {% post_url 2026-05-05-what_makes_a_patent_an_effective_moat %}
[related_post_pmf]: {% post_url 2026-05-11-product_market_fit %}
[related_post_trade_secret]: {% post_url 2026-05-06-patents_trade_secrets_and_the_disclosure_tradeoff %}
[related_post_why_fail]: {% post_url 2026-05-09-why_startups_actually_fail %}
