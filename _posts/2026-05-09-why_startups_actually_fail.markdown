---
layout: post
mathjax: true
comments: true
title:  "Why Startups Actually Fail"
date:   2026-05-09 09:00:00 +0000
categories: business strategy startups
---

<!-- A167 -->
<script>console.log("A167");</script>

Most [startups][ref_startup] fail,
and the reasons they actually fail
are not the reasons their founders fear.
Founders fear that someone will steal the idea,
or that a bigger competitor will crush them.
The record says they mostly die
of something quieter,
that not enough people wanted the thing they built,
and that the money ran out
before they found the people who did.
The enemy of a startup
is indifference far more often than imitation.
This article sets out
what the base rates and the post-mortems
actually say,
because a founder who knows
how startups really fail
can spend scarce effort
guarding against the real risks
rather than the imagined ones.
The companion patent series
made the same point from the other side,
that founders
[overrate patents][related_post_patent_founder]
and [the protection they offer][related_post_patent_moat].
This series asks what actually decides survival.
The treatment is general,
and it is information rather than business advice.

## A Brief History

The study of why startups fail
is younger than the startups themselves.
For a long time
failure was treated as private and shameful,
its lessons buried with the company.
Two developments brought it into the open.
The first was the practice,
associated with the [lean-startup movement][ref_lean_startup]
and with [customer development][ref_customer_development],
of treating a startup as a series of testable guesses
rather than a plan to be executed,
which made failure a source of data
rather than only of embarrassment.
The second was the rise of public post-mortems,
in which founders wrote candidly
about why their companies died,
and the compilation of those accounts
into a rough statistical picture.
That picture is imperfect,
because it rests on self-report,
but it is the best evidence available,
and its central finding is stable.

## The Base Rate

The first fact is the base rate,
and it is sobering.
The exact figure depends on
how one defines a startup and a failure,
so the honest statement is a range.
Of new businesses broadly,
roughly half are gone within five years
and only a third survive ten,
on long-running labor-statistics data.
Of venture-backed startups,
which take bigger risks for bigger outcomes,
the great majority
never return their investors' capital,
and estimates of outright failure
commonly run from two-thirds to nine-tenths.
However the line is drawn,
failure is not the exception for a startup.
It is the base case,
and any honest reasoning about a venture
begins from that fact
rather than from the founder's hope.

These numbers admit a simple model.
If startups failed at a constant yearly rate,
the fraction surviving to year $t$
would follow an exponential [survival function][ref_survival_analysis],

$$ S(t) = e^{-\lambda t}, $$

where $\lambda$ is the yearly [hazard][ref_failure_rate] of failure.
Fitting the curve to the five-year figure,
$S(5) = 0.5$,
gives $\lambda = \tfrac{\ln 2}{5} \approx 0.139$ per year.
That same constant rate
would then predict a ten-year survival of
$S(10) = e^{-1.39} \approx 0.25$,
yet roughly a third of businesses survive ten years.
The model under-predicts the survivors,
which means the real hazard is not constant
but falls as a company ages.
A startup is most fragile when it is young,
the liability of newness familiar to students of organizations,
and the danger concentrates
in the early search for a market
that the rest of this series examines.

## The Reasons They Actually Fail

When founders of failed startups
are asked what happened,
their accounts cluster
into a familiar set of causes.
The single most common,
appearing in something like a third to two-fifths of post-mortems,
is some version of no market need,
the absence of [product-market fit][ref_pmf],
the discovery that the product
solved a problem too few people had
or cared enough to pay to solve.
Running out of cash
and failing to raise the next round
come close behind,
though these are often
the financial face of the same problem,
since a company the market wanted
can usually raise.
The wrong team,
being outcompeted,
pricing and cost problems,
a product users did not enjoy,
and the absence of a business model
fill out the list.

The pattern in the list matters
more than any single entry.
Almost every leading cause
is a failure to make something
a market actually wanted,
or to reach and charge the people who did.
These are the failures
the rest of this series examines,
[the funnel a startup must pass through][related_post_funnel],
[the search for product-market fit][related_post_pmf],
and [the distribution that reaches paying customers][related_post_distribution].

## The Fear and the Reality

Set the list of real causes
against the list of founder fears,
and the mismatch is stark.
Founders worry that a competitor
or a contractor will steal the idea
and win with it.
That cause is essentially absent
from the post-mortems.
Startups are not, in any meaningful number,
killed by idea theft.
They are killed by indifference,
by building something
that the world declined to want.
An idea taken and executed by someone else
is so rare a cause of death
that planning around it
while neglecting the market
is a precise inversion of the real risks.
This is why the patent series
counseled against
over-investing in protecting an idea.
The idea was never the scarce thing.
A market for it was.

## The Base Rate and the Confident Founder

Nearly every founder believes
their startup will be the exception,
and the believing is itself a problem,
because it is nearly universal,
and a signal that everyone emits
carries almost no information.

Let $p$ be the base rate of success,
the fraction of startups that reach a good outcome,
which is small.
A founder's confidence is a signal,
but consider how common it is.
Write $P(C \mid S)$
for the chance a founder is confident
among those who will succeed,
and $P(C \mid F)$
for the chance among those who will fail.
Both are close to one,
because the founders who failed
were, at the start,
just as sure as the founders who won.
[Bayes' theorem][ref_bayes]
gives the probability of success
for a confident founder,

$$ P(S \mid C) = \frac{P(C \mid S)\, p}{P(C \mid S)\, p + P(C \mid F)\,(1 - p)}. $$

When the two confidence rates are equal,
the expression collapses to $p$ exactly.
Confidence then tells you nothing,
and the honest estimate of your odds
is the base rate itself.

A worked instance.
Take a base rate of success of one in ten,
$p = 0.1$,
a ninety-five percent confidence rate among future successes,
and a ninety percent rate among future failures.
Then

$$ P(S \mid C) = \frac{(0.95)(0.1)}{(0.95)(0.1) + (0.90)(0.9)} = \frac{0.095}{0.905} \approx 0.105. $$

The founder's certainty
moves the true probability of success
from one in ten to about one in nine and a half,
almost nothing.

The mechanism is clearest in odds form.
The theorem multiplies the prior odds of success
by the ratio of the two confidence rates,

$$ \frac{P(S \mid C)}{P(F \mid C)} = \frac{P(C \mid S)}{P(C \mid F)} \cdot \frac{p}{1 - p}. $$

That ratio, the Bayes factor,
is here $0.95 / 0.90 \approx 1.06$,
so confidence improves a founder's odds
by about six percent in relative terms
and nothing more.
A signal worth heeding
would carry a Bayes factor far from one,
and a founder's certainty does not.

This is the arithmetic of [base-rate neglect][ref_base_rate_fallacy],
and the [overconfidence][ref_overconfidence] it feeds
is itself a cause of failure,
because a founder who mistakes confidence for evidence
overinvests in a venture
whose real odds the confidence never improved.
The remedy is not to abandon the venture,
since someone does clear the base rate.
It is to act as though the base rate is true,
to build cheaply,
test early,
and treat the market's verdict,
rather than one's own conviction,
as the evidence that counts.

## Failure Is the Default

The base rate and the post-mortems
point at the same structural truth.
A startup succeeds
only if many independent things go right,
a real problem,
a product that solves it,
customers who can be reached,
a price they will pay,
a team that can build and sell,
and enough money to last
until those align.
Each is a hurdle,
and clearing all of them
is far less likely
than clearing any one.
Failure is therefore the default,
not because founders are foolish,
but because success is a conjunction
of many uncertain events.
The [next article][related_post_funnel]
makes that conjunction precise,
and the articles after it
take the hurdles one by one.

## Epistemic State

The base rate and the cause distribution
are empirical,
and they rest on imperfect evidence.
Post-mortems are self-reported,
and a founder's account of what killed the company
can rationalize or simplify,
so a cited cause such as no market need
may itself mask
an execution or distribution failure underneath.
The figures vary
with the definition of a startup
and of failure,
which is why this article gives ranges
rather than single numbers.
[Survivorship bias][ref_survivorship_bias]
shapes much of the popular writing on startups,
which studies winners and infers lessons
that the larger population of losers would contradict.

The Bayesian argument
is a simplification offered for its shape,
not a measurement.
It assumes confidence is nearly as common
among failures as among successes,
which is the realistic case
but not a measured constant,
and it treats success as a single binary event.

The qualitative conclusion,
that startups die of indifference far more than of theft,
is well supported by the available record.
Throughout, this is general information,
and it is not business advice.

## Out of Scope

The detailed taxonomy of failure causes,
the specific datasets and their methods,
and the variation in failure rates by sector and geography
are left to the empirical literature.
The psychology of founders,
beyond the base-rate point made here,
is a large adjacent subject.
The remedies,
namely how to find product-market fit,
how to build under uncertainty,
how to reach customers,
and where durable advantage actually comes from,
are the subjects of the articles that follow
and are not treated here.

## Conclusion

Startups fail mostly for want of a market,
not for want of secrecy,
and the founder who internalizes this
spends differently.
The base rate of failure is high,
a founder's confidence does little to change it,
and the cause of death
is almost always
that not enough people wanted the product
or could be reached and charged for it.
Idea theft, the fear that looms largest,
is the cause that matters least.
The rest of this series
follows the path a startup must walk
to beat the base rate,
beginning with
[the funnel of failure it must pass through][related_post_funnel]
and ending with
[what it takes to succeed and where moats actually come from][related_post_startup_moats].

## References

- [Reference, Base Rate Fallacy][ref_base_rate_fallacy]
- [Reference, Bayes' Theorem][ref_bayes]
- [Reference, Customer Development][ref_customer_development]
- [Reference, Failure Rate][ref_failure_rate]
- [Reference, Lean Startup][ref_lean_startup]
- [Reference, Overconfidence Effect][ref_overconfidence]
- [Reference, Product-Market Fit][ref_pmf]
- [Reference, Startup Company][ref_startup]
- [Reference, Survival Analysis][ref_survival_analysis]
- [Reference, Survivorship Bias][ref_survivorship_bias]
- [Related Post, Distribution and Getting Paid][related_post_distribution]
- [Related Post, Patents for the Early-Stage Founder][related_post_patent_founder]
- [Related Post, Product-Market Fit][related_post_pmf]
- [Related Post, The Funnel of Startup Failure][related_post_funnel]
- [Related Post, What It Takes to Succeed and Where Moats Come From][related_post_startup_moats]
- [Related Post, What Makes a Patent an Effective Moat][related_post_patent_moat]

[ref_base_rate_fallacy]: https://en.wikipedia.org/wiki/Base_rate_fallacy
[ref_bayes]: https://en.wikipedia.org/wiki/Bayes%27_theorem
[ref_customer_development]: https://en.wikipedia.org/wiki/Customer_development
[ref_failure_rate]: https://en.wikipedia.org/wiki/Failure_rate
[ref_lean_startup]: https://en.wikipedia.org/wiki/Lean_startup
[ref_overconfidence]: https://en.wikipedia.org/wiki/Overconfidence_effect
[ref_pmf]: https://en.wikipedia.org/wiki/Product-market_fit
[ref_startup]: https://en.wikipedia.org/wiki/Startup_company
[ref_survival_analysis]: https://en.wikipedia.org/wiki/Survival_analysis
[ref_survivorship_bias]: https://en.wikipedia.org/wiki/Survivorship_bias
[related_post_distribution]: {% post_url 2026-05-13-distribution_and_getting_paid %}
[related_post_funnel]: {% post_url 2026-05-10-funnel_of_startup_failure %}
[related_post_patent_founder]: {% post_url 2026-05-07-patents_for_the_early_stage_founder %}
[related_post_patent_moat]: {% post_url 2026-05-05-what_makes_a_patent_an_effective_moat %}
[related_post_pmf]: {% post_url 2026-05-11-product_market_fit %}
[related_post_startup_moats]: {% post_url 2026-05-14-what_it_takes_to_succeed_and_where_moats_come_from %}
