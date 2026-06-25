---
layout: post
mathjax: true
comments: true
title:  "What Makes a Patent an Effective Moat"
date:   2026-05-05 09:00:00 +0000
categories: business intellectual-property patents
---

<!-- A163 -->
<script>console.log("A163");</script>

A [patent][ref_patent] is a legal right.
A moat is a business advantage.
The two are related,
but they are not the same thing,
and confusing them
is one of the more expensive mistakes
a company can make about its own patents.
[The opening article][related_post_patent_basics]
described the right.
This article asks
when that right becomes
a durable competitive advantage,
an [economic moat][ref_economic_moat],
and when it is merely an expensive certificate.
Most patents are not moats.
Understanding why
is the difference between
spending on patents that protect a business
and spending on patents that protect nothing.
As with the rest of the series,
this is general information
rather than legal or financial advice,
and it assumes filing in the United States.

## The Idea of a Moat

A moat, in business, is a durable [competitive advantage][ref_competitive_advantage],
something that protects a company's profits
from the competition that would otherwise erode them.
The term was popularized by Warren Buffett,
who looked for businesses
with an [economic moat][ref_economic_moat]
that competitors could not easily cross.
The academic version of the same idea
is the study of [barriers to entry][ref_barriers_to_entry],
the costs and obstacles
that keep new rivals out of a market.

A patent is one classic barrier.
By granting the right to exclude,
it can in principle
keep competitors out of a protected market
for the life of the patent.
That is the theory.
Whether a particular patent
actually does this
depends on a set of conditions
that are met far less often than patent holders hope.
A patent is a candidate moat.
The conditions decide
whether the candidacy succeeds.

## A Legal Right Is Not a Moat

The right to exclude is necessary for a patent moat,
but it is not sufficient.
A patent can grant
an airtight right to exclude
from something no one wants,
or from something a competitor
can avoid at trivial cost,
or from something
the holder can never detect being copied.
In each case the legal right is real
and the moat is absent.

This is the gap
where most patent disappointment lives.
A company obtains a patent,
sees the grant as a victory,
and assumes the protection is now in place.
The grant is a legal fact.
The protection is an economic outcome,
and it arrives only
when the right to exclude
attaches to something valuable,
hard to avoid,
and possible to enforce.
The rest of this article
is about those conditions.

## The Conditions for a Patent Moat

Six conditions decide
whether a patent functions as a moat.
A weakness in any one of them
can hollow out the whole.

The first is validity.
A patent likely to be invalidated
is a weak moat,
because a challenger can remove it.
Validity rests on the
[prior art][related_post_prior_art],
the subject of the previous article,
and a patent that issued
over a thin examination
sits on uncertain ground.

The second is claim scope.
The claims must be broad enough
to cover the alternatives a competitor would use,
yet narrow enough to remain valid over the prior art.
This is a genuine tension.
Broaden the claims to block more,
and they become more vulnerable to invalidation.
Narrow them to survive,
and a competitor steps around them.
The valuable patent
lives in the band
where the claims are both broad and survivable,
and that band is often narrow.

The third is detectability.
A right to exclude is only as good
as the holder's ability to tell
when it is being violated.
A patent on a visible product feature
can be checked by buying the product.
A patent on a process
hidden inside a competitor's own operations
may be infringed for years
without the holder ever knowing.

The fourth is the difficulty of designing around.
If a competent rival
can achieve the same commercial result
by a different route the claims do not cover,
and can do so cheaply,
the patent protects little.
The cost to design around
sets a ceiling
on what the patent is worth.

The fifth is enforceability.
A patent is not self-enforcing,
as the opening article noted,
and enforcement is expensive,
the subject of a later article on
[enforcement][related_post_patent_enforcement].
A holder who cannot afford to litigate
holds a right that a well-funded competitor
can infringe with little fear.

The sixth is commercial relevance and timing.
The patent must cover something
the market actually values,
and its remaining term
must overlap the period
in which that value exists.
In a fast-moving field
a patent can outlive
the relevance of the thing it protects,
granting exclusivity over a product
the market has already left behind.

## The Expected Value of a Patent Moat

These conditions can be combined into a simple model
that makes their interaction explicit.
The model is a tool for thought
rather than a valuation method to defend in court,
and its purpose is to show
how a patent strong on one axis
and weak on another
ends up shallow.

Let $V$ be the [present value][ref_npv] of the exclusivity,
the extra profit a firm would earn
as the only seller in the covered market
over the patent's enforceable life.
Let $p_v$ be the probability
the patent survives a validity challenge.
Let $p_d$ be the probability
that infringement, when it occurs, is detected.
Let $p_e$ be the probability
of successful enforcement once infringement is detected.
Let $C$ be the total cost
to obtain, maintain, and enforce the patent.
The [expected value][ref_expected_value]
of the patent as a moat is then

$$ E = p_v \, p_d \, p_e \, V - C. $$

The shape of this expression is the whole lesson.
The three probabilities are each less than one,
so they multiply downward.
A patent that is likely valid,
likely detectable,
and likely enforceable
still keeps only a fraction of $V$,
and a patent weak on any single factor
keeps almost none of it.

Consider a base case,
with all values in millions of dollars.
A patent protects exclusivity worth ten,
it has a sixty percent chance of surviving a validity challenge,
infringement is detectable seventy percent of the time,
enforcement succeeds half the time it is attempted,
and the lifetime cost is half a million.
Then

$$ E = (0.6)(0.7)(0.5)(10) - 0.5 = 2.1 - 0.5 = 1.6. $$

The headline figure was ten million.
The expected moat value is 1.6 million,
because the probabilities took
nearly eighty percent of it
before any money changed hands.

Now make the method hard to detect,
as a process used inside a competitor's own factory often is,
so that $p_d$ falls to two tenths.
Then

$$ E = (0.6)(0.2)(0.5)(10) - 0.5 = 0.6 - 0.5 = 0.1. $$

The same patent,
protecting the same market,
is now barely worth its cost,
because infringement that cannot be seen
cannot be stopped.

Detectability is not the only factor
that can collapse the value.
The protected value $V$ is itself capped
by the cheapest way a competitor can avoid the patent.
A rational competitor will not pay more to be excluded
than it costs to design around the claims.
If that [design-around][ref_design_around] costs $A$,
the value the patent can actually protect is

$$ V_{\text{eff}} = \min(V_{\text{market}}, A), $$

the lesser of the market value
and the competitor's avoidance cost.
Suppose the market value is still ten million
but a competent rival
can design around the claims for one million.
Then $V_{\text{eff}}$ is one million,
and with the base-case probabilities

$$ E = (0.6)(0.7)(0.5)(1) - 0.5 = 0.21 - 0.5 = -0.29. $$

The patent now costs more than it protects.
It is not a shallow moat.
It is a hole in the ground
the company paid to dig.

The model is deliberately crude.
Every input is an estimate,
and reasonable people will disagree on each.
Its value is not the precise number it produces
but the structure it reveals,
that the worth of a patent as a moat
is a product of several fractions,
and that one small fraction
drags the whole product toward zero.

## The Pharmaceutical Case, Where the Moat Is Real

Patents are a strong moat
in pharmaceuticals,
and the reason is that
every condition holds at once.
A [small-molecule drug][ref_small_molecule]
is often protected by a patent
on the molecule itself.
The claim is hard to design around,
because the molecule is the product,
and a competitor that changes it
no longer has the same approved drug.
Infringement is obvious,
because the infringing pill
contains the patented compound,
which a laboratory can confirm.
The value is enormous,
because an approved drug
can be a market of billions.
And the long, expensive approval process
aligns the patent term
with the period of commercial value.
Validity, scope, detectability,
difficulty of designing around,
enforceability, and relevance
are all high together.
This is the rare case
in which a single patent
is a deep and durable moat,
and it is why the pharmaceutical industry
organizes its entire strategy around patents.

## The Software Case, Where the Moat Is Thin

Software is close to the opposite.
A [software patent][ref_software_patent]
often has narrow claims,
both because broad ones founder
on the eligibility limits the opening article described
and because they founder on the prior art.
The same function
can usually be achieved
by a different implementation
the claims do not reach,
so designing around is cheap.
Infringement is hard to detect,
because the accused code
runs on a competitor's own servers
where no one outside can inspect it.
And software moves quickly,
so a patent that takes years to issue and enforce
may protect a feature
the market has already passed.
Validity, scope, detectability,
design-around difficulty, and timing
are all weak together.
This is why
a software company's real moat
is rarely its patents,
a point the closing section returns to.

## The Portfolio and the Thicket

A single patent is seldom a moat,
but a collection can be.
A [patent thicket][ref_patent_thicket]
is a dense set of overlapping patents
that together cover a product
from many angles,
so that a competitor
cannot design around one claim
without running into another.
The portfolio raises the avoidance cost $A$
far above what any single patent could,
and it multiplies the litigation risk
a competitor must weigh.
The moat, in this case,
is the thicket rather than the patent.

The portfolio effect can be stated precisely.
A competitor entering the market is blocked
if at least one patent in the portfolio
proves valid, infringed, and enforceable against it.
Let $q_i$ be the probability
that patent $i$ alone would block,
which is the single-patent product $p_v \, p_d \, p_e$
from the model above
applied to that patent.
If the patents hold or fail independently,
the probability that the portfolio blocks
is the complement of all of them failing,

$$ P_{\text{block}} = 1 - \prod_{i=1}^{n} (1 - q_i). $$

This is why a thicket of individually weak patents
can still be a strong barrier.
Suppose a portfolio holds five patents,
each with only a thirty percent chance
of blocking on its own.
No single one is frightening.
Together,

$$ P_{\text{block}} = 1 - (1 - 0.3)^5 = 1 - 0.7^5 \approx 0.83, $$

so a competitor faces
better than an eighty percent chance
of being stopped by at least one of them,
and must pay to design around or invalidate
every patent that blocks,
a total cost far above any single $A$.
The independence assumption flatters the result,
since patents in a real thicket
often share a specification and a prior-art exposure,
so that one strong reference
can fell several at once.
The true blocking probability
is therefore lower than the formula suggests,
yet the qualitative lesson holds,
that many shallow obstacles in series
can form a deep barrier in aggregate.

The thicket has its own costs.
Building and maintaining many patents
is expensive,
the strategy invites antitrust and policy scrutiny
when it is used to block competition broadly,
and numbers alone do not cure weakness,
because patents that share a flaw
can fall together to a single prior-art reference.
A portfolio is a moat
only when the patents in it
are individually defensible
and collectively hard to avoid.

## When the Moat Is Not the Patent

For most companies,
and nearly all startups,
the durable advantage is not the patent at all.
It is execution,
distribution,
accumulated data,
network effects,
brand,
and the speed of a team
that ships faster than rivals can copy.
A patent may be a feature of such a moat,
raising a competitor's cost at one point,
but it is rarely the moat itself.

This matters
because founders consistently overestimate
the protective value of patents
and underestimate the cost
of the conditions that make them work.
A patent that is narrow,
hard to detect,
cheap to design around,
and expensive to enforce
is a poor substitute
for a product customers prefer
and a company that out-executes its rivals.
The startup series develops this directly
in its article on
[what it takes to succeed and where moats come from][related_post_startup_moats].
The honest summary
is that a patent can strengthen a moat
but seldom creates one.

## Epistemic State

The structural claims here
are the six conditions
and the multiplicative model that combines them.
These are a framework for reasoning,
testable in the sense
that a competing analysis
can dispute a condition
or propose a different combination,
and they should be read that way
rather than as settled fact.

The numerical examples are illustrative.
The probabilities and values
are chosen to show the mechanism,
not measured from a particular patent,
and any real estimate
of validity, detectability, or enforcement odds
is uncertain and contested.

The contrast between pharmaceuticals and software
is a generalization
that holds broadly
but admits exceptions in both directions,
since some software patents are strong
and some pharmaceutical patents are weak.
Throughout, this is general information,
United States centric,
and not legal or financial advice.

## Out of Scope

The formal methods of patent valuation,
namely the income, market, and cost approaches,
are a specialist discipline
and are not treated here.
The modeling of licensing and royalty income,
the economics of standard-essential patents
and their licensing commitments,
and the operation of patent pools
are likewise left aside.
The mechanics of enforcement,
which determine the probability $p_e$ in the model,
belong to the [enforcement article][related_post_patent_enforcement].
The choice between patenting and secrecy,
which determines whether a patent exists to be a moat at all,
belongs to the article on
[patents and trade secrets][related_post_patent_secrets].

## Conclusion

A patent is a moat
only when validity, claim scope, detectability,
the difficulty of designing around,
enforceability, and commercial relevance
hold at the same time.
Because these combine multiplicatively,
a patent strong on five conditions
and weak on the sixth
is a shallow moat,
and the headline value of a patent
is almost never its real value.
Pharmaceuticals are the case
where every condition holds
and the patent is a deep moat.
Software is the case
where the conditions fail together
and the patent is thin.
Most businesses sit between,
and most of them
hold patents that protect less
than their owners believe.
The next articles ask
[how a patent compares to keeping a secret][related_post_patent_secrets],
[what patents mean for a founder][related_post_patent_founder],
and [what enforcing one actually requires][related_post_patent_enforcement].

## References

- [Reference, Barriers to Entry][ref_barriers_to_entry]
- [Reference, Competitive Advantage][ref_competitive_advantage]
- [Reference, Design Around][ref_design_around]
- [Reference, Economic Moat][ref_economic_moat]
- [Reference, Expected Value][ref_expected_value]
- [Reference, Net Present Value][ref_npv]
- [Reference, Patent][ref_patent]
- [Reference, Patent Thicket][ref_patent_thicket]
- [Reference, Small Molecule][ref_small_molecule]
- [Reference, Software Patent][ref_software_patent]
- [Related Post, Patent Enforcement Reality][related_post_patent_enforcement]
- [Related Post, Patents for the Early-Stage Founder][related_post_patent_founder]
- [Related Post, Patents, Trade Secrets, and the Disclosure Tradeoff][related_post_patent_secrets]
- [Related Post, Prior Art and the Foundation of Patentability][related_post_prior_art]
- [Related Post, What a Patent Is and Is Not][related_post_patent_basics]
- [Related Post, What It Takes to Succeed and Where Moats Come From][related_post_startup_moats]

[ref_barriers_to_entry]: https://en.wikipedia.org/wiki/Barriers_to_entry
[ref_competitive_advantage]: https://en.wikipedia.org/wiki/Competitive_advantage
[ref_design_around]: https://en.wikipedia.org/wiki/Design_around
[ref_economic_moat]: https://en.wikipedia.org/wiki/Economic_moat
[ref_expected_value]: https://en.wikipedia.org/wiki/Expected_value
[ref_npv]: https://en.wikipedia.org/wiki/Net_present_value
[ref_patent]: https://en.wikipedia.org/wiki/Patent
[ref_patent_thicket]: https://en.wikipedia.org/wiki/Patent_thicket
[ref_small_molecule]: https://en.wikipedia.org/wiki/Small_molecule
[ref_software_patent]: https://en.wikipedia.org/wiki/Software_patent
[related_post_patent_basics]: {% post_url 2026-05-03-what_a_patent_is_and_is_not %}
[related_post_patent_enforcement]: {% post_url 2026-05-08-patent_enforcement_reality %}
[related_post_patent_founder]: {% post_url 2026-05-07-patents_for_the_early_stage_founder %}
[related_post_patent_secrets]: {% post_url 2026-05-06-patents_trade_secrets_and_the_disclosure_tradeoff %}
[related_post_prior_art]: {% post_url 2026-05-04-prior_art_and_the_foundation_of_patentability %}
[related_post_startup_moats]: {% post_url 2026-05-14-what_it_takes_to_succeed_and_where_moats_come_from %}
