---
layout: post
mathjax: true
comments: true
title:  "Product-Market Fit"
date:   2026-05-11 09:00:00 +0000
categories: business strategy startups
series: patents_and_startups
series_title: Patent and Startup Strategy
series_index: 9
---
<!-- A169 -->
<script>console.log("A169");</script>

The [funnel article][related_post_funnel]
placed [product-market fit][ref_pmf]
at the leakiest stage of a startup,
and the [first article in this series][related_post_why_fail]
placed its absence,
no market need,
at the top of the list of causes of death.
This article asks what fit actually is,
and answers that it is not a feeling
and not a launch,
but a measurable property of retention.
A product has fit
when a cohort of the people who try it
keeps coming back,
so that the retention curve
flattens above zero
instead of decaying to nothing.
That single distinction,
a curve that settles at a plateau
against a curve that falls to zero,
is the quantitative heart of the matter.
The treatment is general,
and it is information rather than business advice.

## A Brief History

The phrase entered common use
through the venture investor Marc Andreessen,
who in 2007 called product-market fit
the only thing that matters
for a young company,
crediting an earlier formulation
by Andy Rachleff.
The underlying counsel,
to build something people want,
is older than the phrase,
and the lean-startup movement
had already recast the search for fit
as a process of validated learning
rather than a single act of insight.
Measurement came in stages.
An early and still useful heuristic,
proposed by Sean Ellis,
asked existing users
how they would feel
if they could no longer use the product,
and read a large share answering very disappointed
as a sign of fit.
The analytics era
moved the test from surveys to behavior,
to the [cohort analysis][ref_cohort_analysis]
of whether users actually return,
which is the measure this article develops.

## What Fit Actually Is

Fit is the demonstrated pull
of enough of the right people
wanting a product
strongly enough to keep using it.
Each phrase carries weight.
Enough, because a handful of enthusiasts
is not a market.
The right people, because pull
from users who will never pay
or never recur
does not sustain a company.
And keep using it,
because a product that is tried once
and abandoned has no fit,
however large the trial.
Before fit, a founder pushes the product
onto an indifferent world.
After fit, the world pulls the product
out of the founder
faster than it can be supplied.
The felt difference is real,
but a feeling is not a measurement,
and the measurement that matters
is whether the people who arrive
choose to stay.

## Retention as the Signature

Consider a cohort,
the group of users who first try a product
in the same period.
Let $R(t)$ be the fraction of that cohort
still active $t$ periods later,
so that $R(0) = 1$
because everyone is present at the start.
The shape of $R(t)$ as $t$ grows
decides the question of fit,
and there are only two fates.

In the first, the curve decays toward zero,

$$
 R(t) = e^{-\lambda t} \longrightarrow 0, 
\tag{1}
$$

an [exponential decay][ref_exponential]
in which every cohort empties out completely,
given enough time.
A company in this state
is a leaky bucket,
held at any level
only by constant acquisition,
since every cohort it contains
eventually leaks away.
In the second, the curve falls at first
and then settles at a positive level,
a plateau that does not decay.
A stable core of users
has made the product part of their routine.
The flattening of the [retention curve][ref_retention]
above zero
is the signature of product-market fit,
and its absence,
a curve that slides to the floor,
is the signature of its lack.

## The Plateau Model

A simple model captures both fates at once.
Suppose a fraction $f$ of each cohort
becomes loyal and effectively never leaves,
while the remaining fraction $1 - f$
churns away at a constant rate $\lambda$.
The retention curve is then

$$
 R(t) = f + (1 - f)\, e^{-\lambda t}. 
\tag{2}
$$

At the start $R(0) = f + (1 - f) = 1$,
and as time grows
the second term vanishes,
leaving the plateau

$$
 \lim_{t \to \infty} R(t) = f. 
\tag{3}
$$

Product-market fit, in this model,
is simply the condition $f > 0$,
the existence of a durable core,
and the size of $f$
measures how much fit a product has.
Take an illustration
with a loyal fraction of $f = 0.3$
and a monthly churn of $\lambda = 0.5$
among the rest.
The curve reads about
$0.72$ after one month,
$0.46$ after three,
$0.33$ after six,
and $0.30$ after a year,
visibly settling toward thirty percent.
A product without fit,
$f = 0$,
retains $e^{-6} \approx 0.002$ of its cohort
after the same year,
which is to say none of it.
Thirty percent forever
and zero percent
are different businesses entirely.

## The Leaky Bucket

Retention governs how large a business can grow.
In the simplest account,
a user base $N$
gains new users at a rate $a$
and loses a fraction $\lambda$ of its members each period,
so that

$$
 \frac{dN}{dt} = a - \lambda N. 
\tag{4}
$$

The base stops growing
when arrivals balance departures,
at the steady state

$$
 N^\ast = \frac{a}{\lambda}. 
\tag{5}
$$

The [churn rate][ref_churn] $\lambda$
sits in the denominator,
which is the whole point.
At a monthly acquisition of a hundred users
and a churn of one half,
the base settles at two hundred,
no matter how long the company runs.
Lower the churn to one tenth,
the improvement that fit provides,
and the same acquisition
settles at a thousand,
five times the business
from the very same spending.
The point here is narrower and prior.
Without retention,
acquisition leaks away,
and the business cannot fill.

## Lifetime and the Value of a Plateau

Retention also sets the value of a user,
through the time that user stays.
The expected lifetime
is the area under the retention curve,

$$
 L = \int_0^\infty R(t)\, dt, 
\tag{6}
$$

a standard fact from [survival analysis][ref_survival_analysis]
for any quantity that endures over time.
For a cohort that only churns,
$R(t) = e^{-\lambda t}$,
the area is $1 / \lambda$,
just two periods
at a monthly churn of one half.
A plateau transforms this.
The flat plateau of the previous section
is the idealized limit
in which the loyal core never leaves
and the lifetime grows without bound.
Any real core churns slowly,
at some small rate $\mu \ll \lambda$,
so that

$$
 R(t) = f\, e^{-\mu t} + (1 - f)\, e^{-\lambda t}, \qquad L = \frac{f}{\mu} + \frac{1 - f}{\lambda}. 
\tag{7}
$$

With a loyal fraction $f = 0.3$
churning at $\mu = 0.02$ each month,
against a remainder at $\lambda = 0.5$,
the lifetime is about $15 + 1.4 \approx 16$ months,
some eight times the two months
the same product earns without fit.
Nearly all of that lifetime
comes from the small loyal core,
which is the value a plateau creates.
A longer life
is worth more [revenue over its course][ref_clv],
and the value side of that ledger,
weighed against the cost of acquisition,
belongs to the [article on distribution and getting paid][related_post_distribution].

## Measuring Fit

The honest measure of fit
is the cohort retention curve,
read out far enough in time
to see whether it flattens or falls.
The survey heuristic
has its place as an early signal,
before there is enough history
to plot a curve,
but it is a leading indicator
and not the thing itself.
The danger throughout
is the vanity metric.
A total of registered users
rises even as every cohort churns out,
because new arrivals hide the losses,
and a founder who watches the total
can mistake a leaking bucket for a full one.
The cohort view defeats this illusion,
because it follows a fixed group over time
and cannot be flattered
by fresh acquisition.
Other honest signs accompany a flattening curve,
unprompted word of mouth,
organic growth that does not depend on paid reach,
and a rising frequency of use,
each of them
a different shadow of the same retention.

## Why Fit Gates Everything

The [funnel][related_post_funnel] explained
why this stage gates the rest.
A leak here discards
everything spent downstream.
Distribution carries users
into a product that does not hold them,
and monetization charges a base
that does not persist,
so that effort at the later stages
returns almost nothing
until the curve flattens.
This is why the search for fit
precedes the scaling of anything.
It is also why fit,
once found,
is the beginning of durability,
since a base that stays
is a base that a rival
must pry loose rather than merely attract,
a thread the [article on moats][related_post_startup_moats]
takes up at the end of the series.
The product that earns this retention
is built under deep uncertainty,
which is the subject of
the [next article on execution risk][related_post_build].

## Epistemic State

The retention models here are stylized.
Real churn is not constant,
since the chance of leaving
usually falls the longer a user stays,
which bends the curve
beyond the simple exponential.
The clean split
into a loyal fraction and a churning remainder
is an idealization
of a continuum of loyalties,
and the true plateau
is rarely flat forever.
What counts as enough retention
depends on the category,
since a daily social product
and an annual tax product
flatten at very different heights
and over very different horizons.
The survey threshold
is a rule of thumb,
not a law,
and fit is a matter of degree
rather than a line crossed once.
What survives these cautions
is the qualitative claim,
which the particular numbers only illustrate.
A retention curve that flattens above zero
is fit,
and one that decays to zero
is its absence.
Throughout, this is general information,
and it is not business advice.

## Out of Scope

The unit economics that weigh
the lifetime value of a retained customer
against the cost to acquire one
belong to a [later article][related_post_distribution].
The engineering and product work
of building toward fit
belong to the [next article][related_post_build].
The specific tooling of cohort analytics,
the category benchmarks
for what retention is good,
and the mechanics of growth loops
are practical subjects
left to the operational literature
and not treated here.

## Conclusion

Product-market fit is not a mood
and not a milestone announced at launch.
It is a measurable property of retention,
a cohort curve that flattens above zero
because a durable core of the right people
has chosen to stay.
The plateau is the thing to find,
its height is the degree of fit,
and its presence
is what makes every later stage worth attempting.
Without it,
acquisition leaks,
monetization charges a vanishing base,
and the funnel ends here,
where the record says
most ventures are in fact lost.
The next article
turns to the execution risk
of building the product
that earns the curve.

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 7 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 7, 3 are established and 4 are bespoke.
Time is counted in periods, months in the worked example, churn rates are fractions per period and retention is a dimensionless fraction of the starting cohort, so a lifetime comes out in the same periods as the rates.

*Equation 1, Bespoke Exponential Retention Without Fit.*
The article represents the fate without fit as exponential decay at a constant churn rate, so every cohort eventually empties.
[exponential decay][ref_exponential]

$$
 R(t) = e^{-\lambda t} \longrightarrow 0, 
\tag{1}
$$

*Equation 2, Bespoke Retention with a Loyal Core.*
The article models a cohort as a loyal fraction that never leaves plus a remainder that churns at a constant rate.
[retention curve][ref_retention]

$$
 R(t) = f + (1 - f)\, e^{-\lambda t}. 
\tag{2}
$$

*Equation 3, Bespoke Retention Plateau.*
In the loyal-core model the retention curve tends to the loyal fraction, which the article takes as the signature of product-market fit.

$$
 \lim_{t \to \infty} R(t) = f. 
\tag{3}
$$

**Equation 4, User Base with Constant Arrivals and Proportional Churn.**
In the simplest stock-and-flow account a user base grows by a constant arrival rate and loses a fixed fraction of its members each period.

$$
 \frac{dN}{dt} = a - \lambda N. 
\tag{4}
$$

**Equation 5, Steady-State User Base.**
The user base stops growing when arrivals balance departures, at the arrival rate divided by the churn rate.
[churn rate][ref_churn]

$$
 N^\ast = \frac{a}{\lambda}. 
\tag{5}
$$

**Equation 6, Expected Lifetime as the Area Under the Retention Curve.**
The expected lifetime of a user is the integral of the retention curve over all time, a standard fact of survival analysis.
[survival analysis][ref_survival_analysis]

$$
 L = \int_0^\infty R(t)\, dt, 
\tag{6}
$$

*Equation 7, Bespoke Two-Rate Retention and Lifetime.*
The article lets the loyal core churn at a small rate of its own, which makes retention a mixture of two exponentials and the lifetime the weighted sum of their reciprocal rates.

$$
 R(t) = f\, e^{-\mu t} + (1 - f)\, e^{-\lambda t}, \qquad L = \frac{f}{\mu} + \frac{1 - f}{\lambda}. 
\tag{7}
$$

### Notation

- $R(t)$, the fraction of a cohort still active $t$ periods after first use
- $\lambda$, the churn rate of non-loyal users per period
- $f$, the loyal fraction of each cohort
- $N$, the user base
- $a$, the rate at which new users arrive
- $N^\ast$, the steady-state user base
- $L$, the expected lifetime of a user
- $\mu$, the small churn rate of the loyal core

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Tertiary Sources

- "Churn Rate." 2026. Wikipedia. Last modified May 20, at 04:51 (UTC). [https://en.wikipedia.org/w/index.php?title=Churn\_rate&oldid=1355146978][ref_churn]
- "Cohort Analysis." 2025. Wikipedia. Last modified May 7, at 15:42 (UTC). [https://en.wikipedia.org/w/index.php?title=Cohort\_analysis&oldid=1289275607][ref_cohort_analysis]
- "Customer Lifetime Value." 2026. Wikipedia. Last modified May 30, at 06:30 (UTC). [https://en.wikipedia.org/w/index.php?title=Customer\_lifetime\_value&oldid=1356854689][ref_clv]
- "Customer Retention." 2026. Wikipedia. Last modified March 21, at 10:51 (UTC). [https://en.wikipedia.org/w/index.php?title=Customer\_retention&oldid=1344588659][ref_retention]
- "Exponential Decay." 2026. Wikipedia. Last modified June 7, at 12:11 (UTC). [https://en.wikipedia.org/w/index.php?title=Exponential\_decay&oldid=1358231453][ref_exponential]
- "Product–market Fit." 2026. Wikipedia. Last modified March 17, at 13:04 (UTC). [https://en.wikipedia.org/w/index.php?title=Product%E2%80%93market\_fit&oldid=1343963599][ref_pmf]
- "Survival Analysis." 2026. Wikipedia. Last modified June 23, at 08:34 (UTC). [https://en.wikipedia.org/w/index.php?title=Survival\_analysis&oldid=1360739849][ref_survival_analysis]

### Related Posts

- Sechter, Brendan. 2026. "Why Startups Actually Fail." *Brendan A R Sechter's Development Blog*, May 9. [https://sgeos.github.io/business/strategy/startups/2026/05/09/why\_startups\_actually\_fail.html][related_post_why_fail]
- Sechter, Brendan. 2026. "The Funnel of Startup Failure." *Brendan A R Sechter's Development Blog*, May 10. [https://sgeos.github.io/business/strategy/startups/2026/05/10/funnel\_of\_startup\_failure.html][related_post_funnel]
- Sechter, Brendan. 2026. "Build and Execution Risk." *Brendan A R Sechter's Development Blog*, May 12. [https://sgeos.github.io/business/strategy/startups/2026/05/12/build\_and\_execution\_risk.html][related_post_build]
- Sechter, Brendan. 2026. "Distribution and Getting Paid." *Brendan A R Sechter's Development Blog*, May 13. [https://sgeos.github.io/business/strategy/startups/2026/05/13/distribution\_and\_getting\_paid.html][related_post_distribution]
- Sechter, Brendan. 2026. "What It Takes to Succeed and Where Moats Come From." *Brendan A R Sechter's Development Blog*, May 14. [https://sgeos.github.io/business/strategy/startups/2026/05/14/what\_it\_takes\_to\_succeed\_and\_where\_moats\_come\_from.html][related_post_startup_moats]

[ref_churn]: https://en.wikipedia.org/w/index.php?title=Churn_rate&oldid=1355146978
[ref_clv]: https://en.wikipedia.org/w/index.php?title=Customer_lifetime_value&oldid=1356854689
[ref_cohort_analysis]: https://en.wikipedia.org/w/index.php?title=Cohort_analysis&oldid=1289275607
[ref_exponential]: https://en.wikipedia.org/w/index.php?title=Exponential_decay&oldid=1358231453
[ref_pmf]: https://en.wikipedia.org/w/index.php?title=Product%E2%80%93market_fit&oldid=1343963599
[ref_retention]: https://en.wikipedia.org/w/index.php?title=Customer_retention&oldid=1344588659
[ref_survival_analysis]: https://en.wikipedia.org/w/index.php?title=Survival_analysis&oldid=1360739849
[related_post_build]: {% post_url 2026-05-12-build_and_execution_risk %}
[related_post_distribution]: {% post_url 2026-05-13-distribution_and_getting_paid %}
[related_post_funnel]: {% post_url 2026-05-10-funnel_of_startup_failure %}
[related_post_startup_moats]: {% post_url 2026-05-14-what_it_takes_to_succeed_and_where_moats_come_from %}
[related_post_why_fail]: {% post_url 2026-05-09-why_startups_actually_fail %}
