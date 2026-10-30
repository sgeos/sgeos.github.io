---
layout: post
mathjax: true
comments: true
title:  "The Funnel of Startup Failure"
date:   2026-05-10 09:00:00 +0000
categories: business strategy startups
series: patents_and_startups
series_title: Patent and Startup Strategy
series_index: 8
---
<!-- A168 -->
<script>console.log("A168");</script>

The [previous article][related_post_why_fail]
argued that a [startup][ref_startup] succeeds
only when many independent things go right,
and that this conjunction
is why failure is the default.
This article makes the conjunction precise.
A startup is best pictured as a funnel,
a sequence of stages
that a venture must clear in order,
each one conditional on the last,
and survival is the chance
of passing through all of them.
The picture explains two things at once,
why so few ventures emerge from the bottom,
and where along the funnel
most of them are actually lost.
The treatment is general,
and it is information rather than business advice.

## A Brief History

The funnel is borrowed from sales and marketing,
where it is older than any startup.
Its ancestor is the [attention, interest, desire, action model][ref_aida],
proposed at the close of the nineteenth century
to describe how a buyer moves
from first notice to purchase.
The same shape became the [purchase funnel][ref_purchase_funnel]
and then, in the digital era,
the [conversion funnel][ref_conversion_funnel],
which tracks how a population of visitors
narrows at each step
down to the few who pay.
Startup practice adapted the metaphor twice.
Once as a customer funnel,
following a single user
from acquisition through activation, retention, and revenue,
and once, less formally,
as a survival funnel,
following the company itself
through the existential stages
it must clear to keep existing.
This article concerns the second funnel.
Its logic, that a chain narrows
to the product of its stages,
is the same in both,
and it borrows one further idea
from the [theory of constraints][ref_theory_of_constraints],
namely that a chain is governed
by its narrowest link.

## The Stages

A reasonable survival funnel
has perhaps six stages,
though the exact boundaries are a modeling choice
rather than a law.
First, a real problem,
one that enough people genuinely have
and would pay to remove.
Second, a solution that works,
a product that actually solves that problem.
Third, [product-market fit][ref_pmf],
the demonstrated pull
of enough of the right people
wanting the product
strongly enough to return to it.
Fourth, distribution,
a repeatable and affordable way
to reach those people.
Fifth, monetization,
charging a price they will pay
that exceeds the cost of serving them.
Sixth, durability,
an advantage that lets the venture
keep what it has won
as others arrive to take it.
A venture must clear every stage,
and a failure at any one
ends the journey
regardless of strength elsewhere.

## The Funnel as a Product

Let $A_i$ be the event
that the venture clears stage $i$.
Survival is the joint event
that it clears all of them,
$A_1 \cap A_2 \cap \cdots \cap A_n$.
The [chain rule of probability][ref_chain_rule]
expresses the chance of that joint event
as a product of [conditional probabilities][ref_conditional_probability],

$$
 P(\text{survive}) = P(A_1)\, P(A_2 \mid A_1)\, P(A_3 \mid A_1 \cap A_2) \cdots P(A_n \mid A_1 \cap \cdots \cap A_{n-1}). 
\tag{1}
$$

Write $p_i$
for the conditional probability
of clearing stage $i$
given that every earlier stage was cleared.
Then survival is simply the product

$$
 P(\text{survive}) = \prod_{i=1}^{n} p_i, \qquad p_i = P(A_i \mid A_1 \cap \cdots \cap A_{i-1}). 
\tag{2}
$$

This identity is exact,
and it assumes nothing about independence.
The stages of a startup
are deeply dependent,
since a strong product helps distribution
and a reached market helps reveal fit,
but the conditioning absorbs every such dependence.
Each $p_i$ already presumes
that the venture stands
where the earlier stages left it.

## Why the Product Is Small

The product form
carries the whole lesson of the [previous article][related_post_why_fail].
A number of factors,
each less than one,
multiply to something far smaller
than any of them.
Suppose for a moment
that every stage had the same probability $p$.
Then survival is

$$
 P(\text{survive}) = p^{\,n}. 
\tag{3}
$$

If each of six stages
is cleared seven times in ten,
survival is $0.7^6 \approx 0.118$,
barely one venture in eight,
even though no single stage
looked especially hard.
At even odds per stage,
$0.5^6 \approx 0.016$,
fewer than two in a hundred.

Real funnels are not uniform.
Take an illustrative set of conditionals,
a real problem at $0.6$,
a working solution at $0.7$,
product-market fit at $0.4$,
distribution at $0.5$,
monetization at $0.7$,
and durability at $0.6$.
Their product is

$$
 P(\text{survive}) = (0.6)(0.7)(0.4)(0.5)(0.7)(0.6) \approx 0.035. 
\tag{4}
$$

About one venture in twenty-eight,
a survival rate
in keeping with the heavy failure
the previous article reported.
Failure is not a verdict on the founder.
It is the arithmetic of multiplying many fractions.

## The Bottleneck

The product form
also says where effort is best spent.
The marginal effect
of improving a single stage
follows from the product directly,
since holding the others fixed,

$$
 \frac{\partial P}{\partial p_i} = \frac{P}{p_i}, \qquad \frac{1}{P}\frac{\partial P}{\partial p_i} = \frac{1}{p_i}. 
\tag{5}
$$

The relative gain
from improving stage $i$
is $1 / p_i$,
which is largest
for the smallest $p_i$.
The leakiest stage
offers the most leverage,
exactly the lesson
the [theory of constraints][ref_theory_of_constraints]
draws for a production line.
In the illustration,
the weakest stage is product-market fit at $0.4$.
Raising it to $0.5$
multiplies survival by $0.5 / 0.4 = 1.25$,
a twenty-five percent improvement,
from about $0.035$ to about $0.044$.
Raising the working solution
from $0.7$ to $0.8$,
the same tenth of a point,
multiplies survival by only $0.8 / 0.7 \approx 1.14$.
The identical effort
returns nearly twice as much
when spent on the narrower stage.
A founder who polishes a strong stage
while a weak one leaks
is improving the wrong number.

## Where Startups Actually Die

The same product
describes the shape of the funnel itself.
The fraction of entering ventures
that survive to the start of stage $k$
is the partial product

$$
 S_k = \prod_{i=1}^{k} p_i, \qquad S_0 = 1, 
\tag{6}
$$

and the fraction of the original cohort
lost at stage $k$
is the drop between successive levels,

$$
 L_k = S_{k-1} - S_k = S_{k-1}\,(1 - p_k). 
\tag{7}
$$

A loss late in the funnel
is a small conditional leak
applied to a cohort already thinned,
while a loss early
falls on nearly everyone.
With the illustrative conditionals above,
the first stage removes forty percent of all entrants,
the second eighteen,
and the product-market-fit gate a further twenty-five,
so more than four in five ventures
are gone before they clear fit.
The final three stages together
account for about thirteen percent of the cohort,
fewer than one in seven of all the deaths,
for all the attention those late stages receive.

The model says leverage lies at the leakiest stage,
and the evidence of the [previous article][related_post_why_fail]
says which stage that usually is.
The dominant recorded cause of death,
no market need,
sits at the early stages,
the real problem
and [product-market fit][ref_pmf].
These are also the widest parts of the funnel,
where the most ventures enter
and the largest fraction is lost.
Yet founders, and the stories they read,
dwell on the late stages,
the scaling, the hiring, the fundraising,
that only survivors ever reach.
The funnel corrects the emphasis.
Most ventures never reach the glamorous problems,
because they are lost
in the unglamorous early work
of confirming that anyone wants the thing at all.
The stages after fit,
[distribution][related_post_distribution]
and the [advantage that makes a venture durable][related_post_startup_moats],
matter greatly,
but only for the ventures
that survive long enough to face them.

## Epistemic State

The per-stage probabilities here
are illustrative,
chosen to show the shape of the arithmetic,
not measured from data.
The decomposition into six stages
is itself a modeling choice.
Real ventures do not march
through clean sequential gates.
They iterate,
revisit earlier stages,
and pivot,
so the funnel is a simplification
of a process that loops.
The chain-rule identity is exact
given any chosen decomposition,
but the numbers placed into it are not,
and a different analyst
would draw the stages differently.

What survives this caution
is the structural conclusion,
which does not depend on the particular numbers.
Survival is a product of factors below one,
so it is small,
and the smallest factor
carries the most leverage.
That much follows from the form alone.
Throughout, this is general information,
and it is not business advice.

## Out of Scope

The within-product customer funnel,
its acquisition, activation, retention, revenue, and referral metrics,
is a distinct and detailed subject
left to the marketing literature.
The cohort and retention mathematics
that demonstrate product-market fit
belong to the [next article][related_post_pmf].
The unit economics of the monetization stage,
the cost to acquire a customer
against the value that customer returns,
belong to the [article on distribution and getting paid][related_post_distribution].
The work of clearing each stage,
the remedies rather than the accounting,
is the subject of the rest of the series
and is not treated here.

## Conclusion

A startup is a funnel,
and survival is the product
of the conditional probabilities
of clearing each stage.
Because the factors are many
and each is below one,
the product is small,
and failure is the default
for a reason no founder can wish away.
The same form shows the remedy.
Effort returns the most
at the leakiest stage,
which the record places early,
in the search for a real problem
and the [pull of product-market fit][related_post_pmf].
The next article
takes up that stage directly,
since it is both the widest part of the funnel
and the place where the most ventures are lost.

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 7 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 7, 5 are established and 2 are bespoke.
Every quantity is a dimensionless probability or a fraction of the entering cohort, and each stage probability is conditional on clearing every earlier stage, so the stage figures cannot be compared with unconditional failure rates.

**Equation 1, Chain Rule of Probability.**
The probability of clearing every stage is the product of the probability of clearing each stage conditional on clearing all earlier ones.
[chain rule of probability][ref_chain_rule]
[conditional probabilities][ref_conditional_probability]

$$
 P(\text{survive}) = P(A_1)\, P(A_2 \mid A_1)\, P(A_3 \mid A_1 \cap A_2) \cdots P(A_n \mid A_1 \cap \cdots \cap A_{n-1}). 
\tag{1}
$$

**Equation 2, Survival as a Product of Stage Conditionals.**
Writing each conditional as a stage probability makes survival the product of the stage probabilities, an identity that assumes nothing about independence.
[chain rule of probability][ref_chain_rule]

$$
 P(\text{survive}) = \prod_{i=1}^{n} p_i, \qquad p_i = P(A_i \mid A_1 \cap \cdots \cap A_{i-1}). 
\tag{2}
$$

*Equation 3, Bespoke Survival with Uniform Stage Probabilities.*
Under the simplifying assumption that every stage has the same probability, survival is that probability raised to the number of stages.

$$
 P(\text{survive}) = p^{\,n}. 
\tag{3}
$$

*Equation 4, Bespoke Survival Through an Illustrative Six-Stage Funnel.*
Survival is evaluated for an illustrative set of assumed conditionals for problem, solution, product-market fit, distribution, monetisation and durability, giving about one venture in twenty-eight.

$$
 P(\text{survive}) = (0.6)(0.7)(0.4)(0.5)(0.7)(0.6) \approx 0.035. 
\tag{4}
$$

**Equation 5, Marginal and Relative Effect of One Stage.**
Differentiating the product with the other stages held fixed shows that the relative gain from improving a stage is the reciprocal of its probability.

$$
 \frac{\partial P}{\partial p_i} = \frac{P}{p_i}, \qquad \frac{1}{P}\frac{\partial P}{\partial p_i} = \frac{1}{p_i}. 
\tag{5}
$$

**Equation 6, Fraction Surviving to a Stage.**
The fraction of the cohort that survives to the start of a stage is the partial product of the stage probabilities up to it.

$$
 S_k = \prod_{i=1}^{k} p_i, \qquad S_0 = 1, 
\tag{6}
$$

**Equation 7, Fraction Lost at a Stage.**
The fraction of the original cohort lost at a stage is the drop between successive survival levels, the surviving fraction times the stage failure probability.

$$
 L_k = S_{k-1} - S_k = S_{k-1}\,(1 - p_k). 
\tag{7}
$$

### Notation

- $A_1$, the event that the venture clears the first stage, with $A_i$ for stage $i$
- $p_i$, the conditional probability of clearing stage $i$ given that every earlier stage was cleared
- $p^{\,n}$, the survival when each of the $n$ stages has the same probability $p$
- $P$, the probability of survival
- $S_k$, the fraction of entering ventures that survive to the start of stage $k$
- $L_k$, the fraction of the original cohort lost at stage $k$

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Tertiary Sources

- "AIDA (Marketing)." 2026. Wikipedia. Last modified May 4, at 07:23 (UTC). [https://en.wikipedia.org/w/index.php?title=AIDA\_(marketing)&oldid=1352450006][ref_aida]
- "Chain Rule (Probability)." 2026. Wikipedia. Last modified June 13, at 20:35 (UTC). [https://en.wikipedia.org/w/index.php?title=Chain\_rule\_(probability)&oldid=1359205356][ref_chain_rule]
- "Conditional Probability." 2026. Wikipedia. Last modified June 22, at 18:21 (UTC). [https://en.wikipedia.org/w/index.php?title=Conditional\_probability&oldid=1360635413][ref_conditional_probability]
- "Funnel Analysis." 2026. Wikipedia. Last modified May 7, at 16:59 (UTC). [https://en.wikipedia.org/w/index.php?title=Funnel\_analysis&oldid=1353013852][ref_conversion_funnel]
- "Product–market Fit." 2026. Wikipedia. Last modified March 17, at 13:04 (UTC). [https://en.wikipedia.org/w/index.php?title=Product%E2%80%93market\_fit&oldid=1343963599][ref_pmf]
- "Purchase Funnel." 2026. Wikipedia. Last modified June 12, at 14:40 (UTC). [https://en.wikipedia.org/w/index.php?title=Purchase\_funnel&oldid=1359019435][ref_purchase_funnel]
- "Startup Company." 2026. Wikipedia. Last modified June 23, at 21:49 (UTC). [https://en.wikipedia.org/w/index.php?title=Startup\_company&oldid=1360830926][ref_startup]
- "Theory of Constraints." 2026. Wikipedia. Last modified May 20, at 12:26 (UTC). [https://en.wikipedia.org/w/index.php?title=Theory\_of\_constraints&oldid=1355194495][ref_theory_of_constraints]

### Related Posts

- Sechter, Brendan. 2026. "Why Startups Actually Fail." *Brendan A R Sechter's Development Blog*, May 9. [https://sgeos.github.io/business/strategy/startups/2026/05/09/why\_startups\_actually\_fail.html][related_post_why_fail]
- Sechter, Brendan. 2026. "Product-Market Fit." *Brendan A R Sechter's Development Blog*, May 11. [https://sgeos.github.io/business/strategy/startups/2026/05/11/product\_market\_fit.html][related_post_pmf]
- Sechter, Brendan. 2026. "Distribution and Getting Paid." *Brendan A R Sechter's Development Blog*, May 13. [https://sgeos.github.io/business/strategy/startups/2026/05/13/distribution\_and\_getting\_paid.html][related_post_distribution]
- Sechter, Brendan. 2026. "What It Takes to Succeed and Where Moats Come From." *Brendan A R Sechter's Development Blog*, May 14. [https://sgeos.github.io/business/strategy/startups/2026/05/14/what\_it\_takes\_to\_succeed\_and\_where\_moats\_come\_from.html][related_post_startup_moats]

[ref_aida]: https://en.wikipedia.org/w/index.php?title=AIDA_(marketing)&oldid=1352450006
[ref_chain_rule]: https://en.wikipedia.org/w/index.php?title=Chain_rule_(probability)&oldid=1359205356
[ref_conditional_probability]: https://en.wikipedia.org/w/index.php?title=Conditional_probability&oldid=1360635413
[ref_conversion_funnel]: https://en.wikipedia.org/w/index.php?title=Funnel_analysis&oldid=1353013852
[ref_pmf]: https://en.wikipedia.org/w/index.php?title=Product%E2%80%93market_fit&oldid=1343963599
[ref_purchase_funnel]: https://en.wikipedia.org/w/index.php?title=Purchase_funnel&oldid=1359019435
[ref_startup]: https://en.wikipedia.org/w/index.php?title=Startup_company&oldid=1360830926
[ref_theory_of_constraints]: https://en.wikipedia.org/w/index.php?title=Theory_of_constraints&oldid=1355194495
[related_post_distribution]: {% post_url 2026-05-13-distribution_and_getting_paid %}
[related_post_pmf]: {% post_url 2026-05-11-product_market_fit %}
[related_post_startup_moats]: {% post_url 2026-05-14-what_it_takes_to_succeed_and_where_moats_come_from %}
[related_post_why_fail]: {% post_url 2026-05-09-why_startups_actually_fail %}
