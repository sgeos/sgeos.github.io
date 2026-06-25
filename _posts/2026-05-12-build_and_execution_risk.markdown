---
layout: post
mathjax: true
comments: true
title:  "Build and Execution Risk"
date:   2026-05-12 09:00:00 +0000
categories: business strategy startups
---

<!-- A170 -->
<script>console.log("A170");</script>

The [previous article][related_post_pmf]
ended by noting
that the product which earns a retention curve
is built under deep uncertainty.
This article is about that building,
and about the risk
that a venture fails
not for want of a market
but for want of reaching it
before the money runs out.
The central reframing
is that a startup does not execute a known plan.
It searches for one.
The binding risk
is therefore not whether the team can build the thing,
which is the engineer's question,
but whether the team can discover
what to build
in the finite number of attempts
that its cash allows.
That number,
and the odds it buys,
can be written down,
which is the work of this article.
The treatment is general,
and it is information rather than business advice.

## A Brief History

The modern view of execution
begins with a distinction drawn by Steve Blank,
that a startup is not a smaller version
of a large company.
A large company executes a business model
it already understands,
while a startup searches for one it does not.
The [customer development][ref_customer_development] method
made the search systematic,
and the [lean-startup][ref_lean_startup] movement
gave it a loop,
build, measure, learn,
turned as quickly and cheaply as possible.
The [minimum viable product][ref_mvp]
was named as the smallest build
that tests a hypothesis,
the device that keeps each turn of the loop short.
Paul Graham later compressed
the survival question
into a single pair of words,
default alive or default dead,
asking whether a company's present trajectory
reaches profitability or fit
before its bank balance reaches zero.
The empirical literature added a warning,
that premature scaling,
building and spending as though the search were already won,
is among the most common ways
that funded startups destroy themselves.

## Two Senses of Execution

The word execution hides two different risks.
The first is engineering execution,
whether a team can build
what it set out to build,
on time and to a standard that works.
This risk is real,
and in deep-technology ventures,
where the science itself may not cooperate,
it can be the risk that matters most.
For the typical software startup, however,
it is rarely the risk that kills,
because building a given specification
is the part the founders usually know how to do.
The second risk is search execution,
whether a team can discover
what is worth building at all,
which specification
will earn the [product-market fit][ref_pmf]
that [the previous article][related_post_pmf]
measured as retention.
This is the binding constraint
for most ventures,
and it is harder,
because the target is unknown at the outset
and is found only by trying.
The rest of this article
concerns the second sense,
and treats the search
as a sequence of attempts
made against a finite budget.

## The Build-Measure-Learn Loop

A single turn of the loop
takes a hypothesis about what to build,
builds the smallest version that tests it,
puts it in front of real users,
and reads the result
as evidence for or against the hypothesis.
Two quantities describe the turn.
Its duration is the cycle time,
written $\tau$,
the calendar cost of one attempt.
Its money cost is the burn
incurred over that time.
The whole purpose of the minimum viable product,
and of the discipline around it,
is to make $\tau$ small,
so that more attempts fit
into the same fixed runway.
A team that ships a careful product
once a quarter
and a team that ships a rough test
once every two weeks
are not working at different speeds alone.
They are buying different numbers of attempts
at the same unknown.

## Runway and the Number of Attempts

Let a venture hold cash $C$
and spend it at a [burn rate][ref_burn_rate] $b$
per unit time.
Its runway,
the time before the cash is gone,
is

$$ T = \frac{C}{b}. $$

If one turn of the loop takes time $\tau$,
the venture can complete

$$ N = \frac{T}{\tau} = \frac{C}{b\,\tau} = \frac{C}{e}, \qquad e = b\,\tau, $$

attempts before the runway ends,
where $e$ is the cost of a single attempt,
the burn multiplied by the cycle time.
The number of attempts
is the cash divided by the cost of an attempt,
and everything execution does well or badly
shows up in that fraction.
Cheaper experiments,
shorter cycles,
and a lower burn
all raise $N$,
and a venture that spends heavily
on long cycles
buys very few attempts
at the only question that matters.

## The Odds of Finding Fit

Treat each attempt
as a [trial][ref_bernoulli]
that discovers a fitting product
with probability $p$
and otherwise teaches something and fails.
The chance of at least one success
across $N$ independent attempts
is the complement of failing every time,

$$ P_{\text{fit}} = 1 - (1 - p)^{N}, $$

which is the way a [geometric process][ref_geometric]
accumulates its chance of a first success.
Put numbers to it.
A venture with six hundred thousand in the bank,
burning fifty thousand a month,
has a runway of twelve months.
At a cycle time of six weeks,
it gets $N = 8$ attempts,
and at a per-attempt success rate of $p = 0.15$,
its odds of finding fit are

$$ P_{\text{fit}} = 1 - (0.85)^{8} \approx 0.73. $$

Now move only the execution levers.
Halve the cycle time to three weeks,
and the same runway yields $N = 16$ attempts,
lifting the odds to about $0.93$.
Halve the burn instead,
stretching the runway to twenty-four months,
and the result is the same.
But let the cycles drag to three months each,
so that $N = 4$,
and the odds fall to about $0.48$,
a coin flip,
from nothing but slow building.
The market never changed.
Only the number of attempts did.

## Default Alive or Default Dead

The number of attempts a venture needs
follows from the same trial.
On average,
fit first arrives after $1 / p$ attempts,
the mean of the [geometric process][ref_geometric],

$$ \frac{1}{p} = \frac{1}{0.15} \approx 6.7 \text{ attempts}. $$

Paul Graham's question,
whether a venture is default alive or default dead,
becomes a comparison of two numbers.
A venture is default alive
when the attempts it can afford
comfortably exceed the attempts it is likely to need,
$N \gtrsim 1 / p$.
The example venture,
with $N = 8$ against a need near seven,
is barely on the living side of that line,
and the same venture building slowly,
at $N = 4$,
is on the dead side
no matter how real its market.

The comparison also sizes a raise.
To reach a chosen confidence $P^\ast$ of finding fit,
a venture needs

$$ N^\ast = \frac{\ln(1 - P^\ast)}{\ln(1 - p)}, \qquad C^\ast = e\,N^\ast, $$

attempts and the cash to fund them.
For ninety percent confidence at $p = 0.15$,
that is about fifteen attempts,
and at seventy-five thousand dollars each,
roughly $1.1$ million in the bank.
The figure is only as trustworthy
as the estimate of $p$,
but it converts a vague unease about runway
into a number that can be checked.

## Two Levers, Not One

The odds depend on two things,
the number of attempts $N$
and the quality of each attempt $p$,
and they are not interchangeable.
The value of one more attempt
is the chance that fit
first arrives on exactly that attempt,

$$ P_{\text{fit}}(N) - P_{\text{fit}}(N - 1) = p\,(1 - p)^{N - 1}, $$

which shrinks geometrically as $N$ grows.
The eighth attempt in the example above
adds about five percentage points,
against the fifteen that the first attempt adds.
Past some point,
buying more attempts returns little,
and the way forward is to raise $p$,
the quality of each attempt,
by talking to users,
sharpening the hypothesis,
and building the test that actually decides it.
Speed multiplies attempts,
and judgment improves them,
and a venture needs both,
since fast attempts that test nothing
and sharp hypotheses tested once a year
fail in opposite ways.

## Failure Modes of the Build

Each common way that building goes wrong
is a way of wasting attempts.
Over-engineering spends a large $e$
on a single attempt,
gilding a product
whose premise is not yet confirmed.
Premature scaling does the same at greater cost,
building the machinery of a winner
before the search is won,
and is among the most reliable ways
to convert a generous runway
into none.
Perfectionism lengthens $\tau$
in pursuit of a polish
that the test did not require,
trading attempts for shine.
Building without measuring
spends an attempt and reads no result,
learning nothing for the money.
The opposite error,
shipping something so rough
that it tests the wrong thing,
spends an attempt
and reads a false result,
which is worse than learning nothing.
[Technical debt][ref_technical_debt]
is the one item on the list
that is often correct to incur,
since code written to be discarded
should be written quickly,
and only the parts that survive contact
with a real market
deserve to be built well.
The discipline is to spend cheaply
while searching
and to build durably
only once there is something proven to keep.

## Epistemic State

The model treats attempts
as independent trials
with a constant success probability $p$,
and this is its largest simplification.
In reality a team learns,
so that $p$ should rise from one attempt to the next,
which is the entire point of the loop
and a reason the constant-rate odds
are pessimistic for a team that learns
and optimistic for one that does not.
The boundary of an attempt is fuzzy,
since real builds overlap and branch
rather than proceeding one at a time,
and burn is not perfectly constant.
The single probability $p$
also compresses
a great deal of skill, luck, and market structure
into one number.
What survives these simplifications
is the shape of the result,
that the odds of finding fit
rise with the number of affordable attempts,
that this number is cash divided by the cost of an attempt,
and that execution is the work
of making attempts many, cheap, and sharp.
The arithmetic is a lens for that work,
not a forecast of any particular venture.
Throughout, this is general information,
and it is not business advice.

## Out of Scope

The craft of engineering management,
the specific methods of agile development,
and the mechanics of hiring a team that can build
are operational subjects
left to their own literatures.
The deep-technology case,
in which engineering execution
is itself the dominant risk,
is noted here but not developed.
The unit economics
that decide whether a found product
can be sold at a profit
belong to the [next article][related_post_distribution],
and the durable advantage
that execution speed can become
is a thread for the
[article on moats][related_post_startup_moats]
at the end of the series.

## Conclusion

Execution risk, for most startups,
is the risk of running out of money
before discovering what to build.
The discovery is a search,
not the running of a known plan,
and a search is a sequence of attempts
bounded by the cash on hand.
The number of attempts
is the cash divided by the cost of one,
$N = C / (b\tau)$,
and the odds of success
climb with that number
and with the quality of each try.
A venture improves its position
by iterating quickly,
spending little per attempt,
and sharpening each hypothesis,
which is to say by building to learn
rather than building to impress.
What it cannot do
is change the base rate by wishing,
or buy fit
with a single expensive bet
when it could have afforded many cheap ones.
The [funnel][related_post_funnel]
that began this stretch of the series
loses most ventures
in exactly this work,
and the [first article][related_post_why_fail]
counted the bodies.
The next article
turns from building the product
to reaching and charging the people
who will pay for it.

## References

- [Reference, Bernoulli Trial][ref_bernoulli]
- [Reference, Burn Rate][ref_burn_rate]
- [Reference, Customer Development][ref_customer_development]
- [Reference, Geometric Distribution][ref_geometric]
- [Reference, Lean Startup][ref_lean_startup]
- [Reference, Minimum Viable Product][ref_mvp]
- [Reference, Product-Market Fit][ref_pmf]
- [Reference, Technical Debt][ref_technical_debt]
- [Related Post, Distribution and Getting Paid][related_post_distribution]
- [Related Post, Product-Market Fit][related_post_pmf]
- [Related Post, The Funnel of Startup Failure][related_post_funnel]
- [Related Post, What It Takes to Succeed and Where Moats Come From][related_post_startup_moats]
- [Related Post, Why Startups Actually Fail][related_post_why_fail]

[ref_bernoulli]: https://en.wikipedia.org/wiki/Bernoulli_trial
[ref_burn_rate]: https://en.wikipedia.org/wiki/Burn_rate
[ref_customer_development]: https://en.wikipedia.org/wiki/Customer_development
[ref_geometric]: https://en.wikipedia.org/wiki/Geometric_distribution
[ref_lean_startup]: https://en.wikipedia.org/wiki/Lean_startup
[ref_mvp]: https://en.wikipedia.org/wiki/Minimum_viable_product
[ref_pmf]: https://en.wikipedia.org/wiki/Product-market_fit
[ref_technical_debt]: https://en.wikipedia.org/wiki/Technical_debt
[related_post_distribution]: {% post_url 2026-05-13-distribution_and_getting_paid %}
[related_post_funnel]: {% post_url 2026-05-10-funnel_of_startup_failure %}
[related_post_pmf]: {% post_url 2026-05-11-product_market_fit %}
[related_post_startup_moats]: {% post_url 2026-05-14-what_it_takes_to_succeed_and_where_moats_come_from %}
[related_post_why_fail]: {% post_url 2026-05-09-why_startups_actually_fail %}
