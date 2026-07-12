---
layout: post
mathjax: true
comments: true
title:  "Patents, Trade Secrets, and the Disclosure Tradeoff"
date:   2026-05-06 09:00:00 +0000
categories: business intellectual-property patents
series: patents_and_startups
series_title: Patent and Startup Strategy
series_index: 4
---
<!-- A164 -->
<script>console.log("A164");</script>

A [patent][ref_patent] and a [trade secret][ref_trade_secret]
are opposite answers to the same question,
how to keep the value of an invention
from flowing to competitors.
A patent answers by disclosing the invention to the public
in exchange for a limited right to exclude.
A trade secret answers by never disclosing it at all,
and lasting exactly as long as the secret holds.
The two strategies are usually mutually exclusive
for the same piece of information,
because the disclosure that earns a patent
destroys the secrecy a trade secret depends on.
Choosing between them
is the disclosure tradeoff,
and it is one of the most consequential
early decisions an inventor makes.
[The opening article][related_post_patent_basics]
described the patent bargain,
and [the prior-art article][related_post_prior_art]
described how disclosure
sets the line of what is already known.
This article sets the patent against its alternative.
As with the rest of the series,
this is general information rather than legal advice,
and it assumes filing in the United States.

## A Brief History

Secrecy is the older strategy by far.
Craft guilds guarded their methods for centuries,
and the recipe held in confidence
long predates the patent grant
that was invented to coax such recipes into the open.
The patent bargain was in part a response to secrecy,
an offer of a limited monopoly
in exchange for the public teaching
that a guarded secret withholds.

The modern law of trade secrets is recent by comparison.
In the United States
it was harmonized across the states
by the [Uniform Trade Secrets Act][ref_utsa] of 1979,
revised in 1985,
and then given a federal civil cause of action
by the [Defend Trade Secrets Act][ref_dtsa] of 2016.
The canonical example remains
the formula for Coca-Cola,
held as a [trade secret][ref_coca_cola]
for more than a century,
far longer than any patent could have protected it,
and a standing reminder
that for the right invention
secrecy outlasts the patent term.

## What a Trade Secret Is

A trade secret is information
that derives economic value
from not being generally known,
and that its owner takes reasonable measures to keep secret.
Both halves are required.
Information that is valuable but unguarded
is not a trade secret,
and information that is guarded but worthless
is not worth protecting.
The reasonable-measures requirement
has teeth.
A company claiming a trade secret
must show that it actually protected it,
through confidentiality agreements,
access controls,
marking,
and need-to-know restrictions.
A secret left lying around
is not a secret the law will defend.

The crucial limit
is what trade-secret law does not reach.
It protects against misappropriation,
namely theft,
or use in breach of a duty of confidence.
It does not protect against
two perfectly lawful routes to the same knowledge.
A competitor may
[reverse engineer][ref_reverse_engineering]
a product to learn how it works,
and a competitor may
independently discover the same thing
without ever touching the secret.
Both are proper means,
and against both
a trade secret offers nothing.

## Two Opposite Bargains

The patent and the trade secret
trade away opposite things.

A patent gives up secrecy
to gain a strong but time-limited exclusion.
It lasts about twenty years from filing,
it is published for all competitors to read and to design around,
and within its term
it excludes even a competitor
who invented the same thing independently.

A trade secret gives up
the protection against independent invention
to gain a term that has no fixed limit.
It can last forever,
as the Coca-Cola formula has,
or it can end tomorrow
when a competitor reverse engineers the product
or independently arrives at the method.
It is never published,
so it teaches competitors nothing,
but it cannot stop a competitor
who finds the same answer by honest means.

The choice between them
is therefore a choice
between a known, limited, disclosed, and broad protection,
and an unknown, potentially unlimited, hidden, and narrow one.

## The Decision Factors

Several factors decide
which bargain fits a given invention.

The first is the ease of reverse engineering.
If the invention is visible in a shipped product
and can be understood by taking it apart,
secrecy is fragile,
because every sale is an opportunity to lose it,
and a patent is the better choice.
If the invention is a process or method
used out of sight
and hard to infer from the product,
secrecy can hold.

The second is the expected lifespan of the value.
If the invention will matter
for far longer than a patent term,
and it can be kept secret,
secrecy protects a value
that a patent would eventually release.
If the value is short-lived,
the patent term is more than enough.

The third is the risk of independent invention.
In a crowded, fast-moving field
where many capable teams work in parallel,
a secret is likely to be independently discovered,
and possibly patented by someone else,
while a patent at least secures priority
to the first to file.

The fourth is cost.
A patent carries the costs of filing, prosecution,
maintenance, and enforcement.
A trade secret carries the cost
of an ongoing secrecy program.
Neither is free,
and the costs have different shapes,
one front-loaded and legal,
the other continuous and operational.

The fifth is the cost of disclosure itself.
A patent teaches competitors how the invention works,
which lets them design around it
and build on it.
A trade secret teaches them nothing.
For an invention whose value
lies as much in the know-how as in the legal right,
the teaching a patent forces
can be a real cost.

## The Expected Life of a Secret

Duration is where the two strategies differ most,
and the difference can be made precise.
A patent has a fixed term,
twenty years from filing,
less the years lost to prosecution,
so its effective protective life
is known in advance.
Call it $T$ years.

A trade secret has no fixed term.
It lasts until it is lost,
whether by leak,
by reverse engineering,
or by independent discovery.
Model the loss as a constant annual hazard.
Let $h$ be the probability
that the secret is lost in any given year.
The number of years it survives
then follows a [geometric distribution][ref_geometric_distribution],
whose [expected value][ref_expected_value] is

$$ E[L] = \frac{1}{h}. $$

Secrecy offers a longer expected protected life
than a patent exactly when

$$ \frac{1}{h} > T, $$

that is, when the annual hazard is small enough
that the secret is expected to outlast the patent term.

Consider three cases.
A secret with a ten percent annual hazard,
$h = 0.10$,
has an expected life of ten years,
shorter than the patent term,
so the patent protects longer.
A secret with a five percent hazard,
$h = 0.05$,
lasts twenty years on average,
longer than the term that survives prosecution.
A secret with a three percent hazard,
$h = 0.03$,
lasts roughly thirty-three years,
well beyond any patent,
which is the regime
in which the Coca-Cola formula lives.

The hazard $h$ is set mostly by one thing,
the ease of reverse engineering.
A product shipped to customers
and open to inspection
carries a high hazard,
because every unit sold
is a chance for a competitor to learn the secret,
and for such an invention
the fixed patent term
beats the short expected life of secrecy.
A process kept inside a factory,
never shipped and hard to infer,
carries a low hazard,
and for it secrecy can outlast many patents.

One thing the duration math does not capture
must be stated separately.
A patent protects even against a competitor
who invents the same thing independently.
A trade secret does not.
However long a secret's expected life,
an independent inventor
can reach the same idea,
use it freely,
and even patent it,
subject only to the limited
[prior commercial use defense][research_35_usc_273]
that shields an earlier secret user
from being excluded by the later patent.
Secrecy trades the patent's protection against independent invention
for the chance at a longer,
though uncertain,
life.

## The Discounted Value of the Choice

The duration comparison ignores the time value of money,
and money has one.
A year of protection now
is worth more than a year of protection two decades out,
so the choice is better made
in [present value][ref_present_value],
discounting future protection at a rate $r$.

A patent protects a stream worth $A$ per year
for the fixed term $T$.
Discounted at rate $r$,
its present value is

$$ V_{\text{patent}} = A \, \frac{1 - e^{-rT}}{r}. $$

A trade secret protects the same annual value $A$
for an uncertain time,
ending at the constant hazard $h$.
Weighting each future year
by the probability the secret survives to it,
and treating the hazard as a continuous rate
for a clean closed form,
its value is a [perpetuity][ref_perpetuity]

$$ V_{\text{secret}} = \frac{A}{r + h}. $$

The form of this result is the lesson.
The hazard $h$ enters exactly where the discount rate $r$ does.
An annual chance of losing the secret
is, in present-value terms,
indistinguishable from an equal addition to the discount rate,
so a secret with a high disclosure hazard
is worth no more than a safe cash flow
discounted very steeply.

The comparison sharpens the earlier one.
Take a discount rate of ten percent
and an effective patent term of seventeen years.
The patent's present-value factor is

$$ \frac{1 - e^{-(0.10)(17)}}{0.10} \approx 8.17, $$

so the patent is worth about $8.17 \, A$.
The secret matches it when

$$ \frac{1}{r + h} = 8.17, $$

which gives a hazard of about $h \approx 0.022$.
The secret wins on value
only when its annual hazard is below roughly two percent,
a far stricter bar than the duration comparison gave,
where secrecy pulled ahead
at a hazard below one seventeenth,
nearer six percent.
Discounting favors the patent,
because the patent's protection is guaranteed and near
while the secret's long tail
is uncertain and far away,
and the present discounts the far future twice,
once for time and once for the hazard.

## The Hybrid Strategy

The choice is rarely all of one or all of the other.
A company can patent the parts of an invention
that a shipped product reveals anyway,
and keep secret the parts
that stay hidden in its own operations.
The visible device is patented.
The manufacturing process that makes it cheaply
is kept secret.
Each piece of information
goes to the strategy that fits it.

The seam between the two
is the moment of disclosure.
Filing and publishing a patent
ends the secrecy of everything the patent discloses,
so an inventor cannot patent a thing
and also keep that same thing secret.
This is the same seam
the prior-art article described
from the other side,
since the disclosure that ends secrecy
is also the disclosure that becomes prior art.
It is why the sequence matters.
A premature public disclosure,
made before filing,
can forfeit foreign patent rights
and start the clock at home,
which is the practical reason
that confidentiality agreements
guard the period before filing,
keeping both options open
until the inventor chooses between them.

## Government-Funded Research, a Special Case

Government research funding
shows the patent-and-secret choice
under a particular and unusually favorable set of rules.
Under the Small Business Innovation Research
and Small Business Technology Transfer programs,
known as SBIR and STTR,
a company that makes an invention under a federal award
may retain its patents under the
[Bayh-Dole Act][ref_bayh_dole],
so the funding dilutes neither equity nor ownership.

Alongside the patent right
sits a protection that behaves like a trade secret.
The programs grant a data-rights protection period
during which the government,
though it paid for the work,
may not release the company's technical data outside the government
or use it to have the work redone by a competitor.
That protection is preserved by marking the deliverables,
which is the funded-research version
of the reasonable-measures requirement
that trade-secret law imposes,
and a company that fails to mark
can lose the protection
as surely as a company that fails to guard a secret.
The protection is also time-limited,
broadening toward government use after the period,
so a company builds its long-term position
on patents and continued innovation
rather than on the data rights alone.
The full treatment is in the
[SBIR and STTR data-rights article][related_post_sbir_ip].
The lesson it carries back here
is that the patent-and-secret choice
is seldom a clean either-or,
and that the right answer is often
to patent some things,
guard others,
and observe whatever marking and secrecy discipline
the governing regime demands.

## Epistemic State

The settled matters here
are the definition of a trade secret
and its reasonable-measures requirement,
the harmonizing role of the Uniform Trade Secrets Act
and the federal cause of action under the Defend Trade Secrets Act,
the fact that trade-secret law
does not reach reverse engineering or independent invention,
and the fixed twenty-year patent term.
These should hold against independent verification.

The expected-life model is a simplification.
A constant annual hazard
is a convenient assumption rather than a measured fact,
real disclosure risk varies over time,
and the single number $h$
stands in for many distinct ways a secret can be lost.
The discounted-value model adds a constant discount rate
and treats the hazard as continuous,
both for tractability,
and it prices only the duration of protection,
not the more severe outcome
in which an independent inventor patents the idea
and excludes the original secret holder.
The models are offered to make the comparison precise in shape,
not to predict the value of a particular secret.

The decision factors and the hybrid strategy
are practical generalizations,
sound in the typical case
and subject to exceptions.
Throughout, this is general information,
United States centric,
and not legal advice.

## Out of Scope

The detailed mechanics of trade-secret litigation,
the standards for proving misappropriation,
and the criminal liability
under the [Economic Espionage Act][ref_eea] of 1996
are left to specialists.
The law governing employee mobility,
including confidentiality and non-competition agreements
and the doctrine of inevitable disclosure,
is a large adjacent subject
treated only in passing.
The country-by-country variation in trade-secret law
is left to local counsel,
and the formal valuation
of either a patent or a secret
belongs to the methods named
in the [moat article][related_post_patent_moat].

## Conclusion

A patent and a trade secret
protect an invention in opposite ways,
and the choice between them
turns on a few clear factors.
Patent what a product reveals,
what a competitor could reverse engineer or independently invent,
and what matters most within a twenty-year horizon.
Keep secret what stays hidden,
what is hard to reverse engineer,
and what may need to last far longer than a patent term,
accepting that secrecy offers no protection
against a competitor who finds the same answer honestly.
Most often the answer is both,
patenting the visible
and guarding the hidden,
with confidentiality holding the line
until the choice is made.
The next articles turn to
[what patents mean for a founder][related_post_patent_founder]
and [what enforcing one actually requires][related_post_patent_enforcement].

## References

- [Reference, Bayh-Dole Act][ref_bayh_dole]
- [Reference, Coca-Cola Formula][ref_coca_cola]
- [Reference, Defend Trade Secrets Act][ref_dtsa]
- [Reference, Economic Espionage Act of 1996][ref_eea]
- [Reference, Expected Value][ref_expected_value]
- [Reference, Geometric Distribution][ref_geometric_distribution]
- [Reference, Patent][ref_patent]
- [Reference, Perpetuity][ref_perpetuity]
- [Reference, Present Value][ref_present_value]
- [Reference, Reverse Engineering][ref_reverse_engineering]
- [Reference, Trade Secret][ref_trade_secret]
- [Reference, Uniform Trade Secrets Act][ref_utsa]
- [Related Post, Data Rights and Intellectual Property in SBIR and STTR][related_post_sbir_ip]
- [Related Post, Patent Enforcement Reality][related_post_patent_enforcement]
- [Related Post, Patents for the Early-Stage Founder][related_post_patent_founder]
- [Related Post, Prior Art and the Foundation of Patentability][related_post_prior_art]
- [Related Post, What a Patent Is and Is Not][related_post_patent_basics]
- [Related Post, What Makes a Patent an Effective Moat][related_post_patent_moat]
- [Research, United States Code Title 35 Section 273, Prior Commercial Use Defense][research_35_usc_273]

[ref_bayh_dole]: https://en.wikipedia.org/wiki/Bayh%E2%80%93Dole_Act
[ref_coca_cola]: https://en.wikipedia.org/wiki/Coca-Cola_formula
[ref_dtsa]: https://en.wikipedia.org/wiki/Defend_Trade_Secrets_Act
[ref_eea]: https://en.wikipedia.org/wiki/Economic_Espionage_Act_of_1996
[ref_expected_value]: https://en.wikipedia.org/wiki/Expected_value
[ref_geometric_distribution]: https://en.wikipedia.org/wiki/Geometric_distribution
[ref_patent]: https://en.wikipedia.org/wiki/Patent
[ref_perpetuity]: https://en.wikipedia.org/wiki/Perpetuity
[ref_present_value]: https://en.wikipedia.org/wiki/Present_value
[ref_reverse_engineering]: https://en.wikipedia.org/wiki/Reverse_engineering
[ref_trade_secret]: https://en.wikipedia.org/wiki/Trade_secret
[ref_utsa]: https://en.wikipedia.org/wiki/Uniform_Trade_Secrets_Act
[related_post_patent_basics]: {% post_url 2026-05-03-what_a_patent_is_and_is_not %}
[related_post_patent_enforcement]: {% post_url 2026-05-08-patent_enforcement_reality %}
[related_post_patent_founder]: {% post_url 2026-05-07-patents_for_the_early_stage_founder %}
[related_post_patent_moat]: {% post_url 2026-05-05-what_makes_a_patent_an_effective_moat %}
[related_post_prior_art]: {% post_url 2026-05-04-prior_art_and_the_foundation_of_patentability %}
[related_post_sbir_ip]: {% post_url 2026-06-22-data_rights_and_intellectual_property_for_sbir_and_sttr %}
[research_35_usc_273]: https://www.law.cornell.edu/uscode/text/35/273
