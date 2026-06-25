---
layout: post
mathjax: true
comments: true
title:  "Patents for the Early-Stage Founder"
date:   2026-05-07 09:00:00 +0000
categories: business intellectual-property patents
---

<!-- A165 -->
<script>console.log("A165");</script>

The early-stage founder's question about patents
is not the one the patent office answers.
The office answers whether an invention can be patented.
The founder must answer
whether a patent is worth scarce money,
scarce time,
and scarce attention,
when all three are needed
to build a product and find customers.
The earlier articles in this series
built the tools for that answer,
namely [what a patent is][related_post_patent_basics],
[how the prior art governs it][related_post_prior_art],
[whether it is a moat][related_post_patent_moat],
and [how it compares to a secret][related_post_patent_secrets].
This article turns those tools
on the founder's actual decision.
The honest summary,
developed below,
is that for most founders
patents are not the priority,
that a few cheap disciplines
preserve the option without betting the company on it,
and that a startup buys patents
for reasons other than the courtroom.
As with the rest of the series,
this is general information rather than legal or financial advice,
and it assumes filing in the United States.

## Why Founders Overrate Patents

Founders consistently overestimate
what a patent does for them.
The overestimate has a source.
A [patent][ref_patent] feels like protection,
a certificate that the idea is now safe,
and the fear that drives it,
that someone will take the idea and win with it,
is real and common.
The moat article gave the correction.
Most patents are not moats,
because the right to exclude
protects a profit
only when the patent is valid,
the infringement is detectable,
the claims are hard to design around,
and the holder can afford to enforce.
For a startup the last of these usually fails.

The deeper correction
comes from the startup side of this writing,
in [what it takes to succeed and where moats come from][related_post_startup_moats].
A startup's durable advantage
is almost never its patents.
It is the product customers prefer,
the distribution that reaches them,
the data that accumulates,
and the speed of a team
that ships faster than rivals can copy.
Ideas are cheap and abundant.
Execution is scarce and decisive.
A founder who spends the company's thin resources
defending an idea
while a competitor out-executes
has optimized the wrong thing.

## The Cost a Founder Actually Faces

The patent costs a founder meets
come in a steep sequence.
A [provisional application][ref_provisional_application]
is cheap,
a few hundred dollars in fees
and a modest sum if a professional drafts it.
A full non-provisional application,
prepared and prosecuted to grant,
commonly runs into the low tens of thousands of dollars.
Maintenance fees follow over the patent's life.
And enforcement,
the cost that decides whether the patent protects anything,
runs into the millions,
because a patent infringement suit
is among the more expensive forms of civil litigation.

That last figure is the one
that reshapes the founder's calculus.
A right that can be enforced only by spending millions
is, for a company that does not have millions,
a right that a well-funded competitor
can infringe with little to fear.
The [enforcement article][related_post_patent_enforcement]
develops this in full.
For the founder it means
that the protective value of a patent,
the thing it is nominally for,
is mostly out of reach.

## The Founder's Expected Value

The moat article gave an [expected-value][ref_expected_value] model
for what a patent is worth,

$$ E = p_v \, p_d \, p_e \, V - C, $$

the protected value $V$ scaled by the probabilities
that the patent is valid,
that infringement is detected,
and that it can be enforced,
less the cost $C$.
For a founder, one term behaves differently.
The probability of successful enforcement, $p_e$,
is small for an early-stage company,
because enforcement means funding litigation
that runs into the millions,
which a startup cannot do
against a well-resourced infringer.
With $p_e$ near zero,
the protective term $p_v \, p_d \, p_e \, V$
collapses toward zero with it.

Yet founders file patents,
and often they are right to.
The reason is a value the moat model left out,
the [signaling][ref_signaling] and acquisition value $S$.
A granted patent,
or even a pending application,
can help close investors,
satisfy an acquirer's diligence,
and add to a portfolio a buyer will pay for.
Adding it,

$$ E_{\text{founder}} = p_v \, p_d \, p_e \, V + S - C, $$

and because the protective term is small for a startup,
this reduces in practice to

$$ E_{\text{founder}} \approx S - C. $$

The founder's patent decision
is therefore mostly a question
of whether the signaling and acquisition value
exceeds the cost,
and not whether the patent could be enforced,
because for most startups it could not be.
This is why the cheap provisional
is so often worth filing,
since its cost $C$ is small
and even a modest $S$ clears it,
and why an expensive full prosecution
needs a clearer story about $S$
to justify the spend.
The value $S$ is genuinely hard to estimate,
and an honest founder
treats it as a real but fuzzy benefit
rather than a number.
The structure still holds.
A startup buys patents
for priority, signaling, and sale,
not for the courtroom.

## The Provisional as the Founder's Tool

The provisional application
fits the founder's situation almost exactly.
It is cheap,
it requires no claims and no examination,
and it establishes an early filing date
that matters under the
[first-inventor-to-file][ref_first_to_file] rule.
It confers the phrase patent pending,
which carries the signaling value $S$
at a fraction of the cost of a grant.
And it starts a twelve-month clock,
within which the founder must decide
whether to file the expensive non-provisional
or let the option lapse.

The provisional is therefore best understood
as an option, not a commitment.
It buys a year of priority and patent-pending status
for a small premium,
during which the company can learn
whether the invention,
the market,
and the funding
justify the larger spend.
A founder uses it to keep the patent option open cheaply
while putting the real money into the product,
and decides on the costly non-provisional
only when there is evidence
that the patent will earn its keep.

## The Option Value of the Provisional

The claim that the provisional is an option
can be made precise.
A provisional is, in the language of finance,
a [real option][ref_real_options],
the right but not the obligation
to acquire the full patent later,
and the precise version explains
why it is worth most
exactly when the founder is least certain.

Write $X$ for the value the patent will turn out to have,
unknown when the provisional is filed
and resolving over the following year
as the invention, the market, and the funding become clearer.
Write $K$ for the cost of the non-provisional
that converts the provisional into a real application.

A founder who must decide now,
without a provisional,
either commits the full cost $K$ or does not,
so the value of deciding now is

$$ \max\!\left(0,\; E[X] - K\right). $$

A founder who files the provisional
defers the decision until $X$ is known,
and then converts only if the realized value exceeds the cost,
so the value of waiting, before the small premium, is

$$ E\!\left[\max\!\left(0,\; X - K\right)\right]. $$

Because $\max(0, \cdot)$ is convex,
[Jensen's inequality][ref_jensen]
makes the second at least as large as the first,
and the gap between them is the option value.
That gap grows with the uncertainty in $X$.
The more unsure the founder is
about whether the patent will matter,
the more the option to wait is worth,
which inverts the usual intuition.
Uncertainty does not argue against the spend.
It argues for the cheap provisional,
because the provisional is the cheap way to wait.

A small example makes it concrete,
with values in thousands of dollars.
Suppose the patent turns out worth nothing
with probability one half,
because the invention or the market did not develop,
and forty with probability one half because it did,
and suppose the non-provisional costs twenty.
Deciding now is a break-even at best,

$$ \max\!\left(0,\; (0.5)(0) + (0.5)(40) - 20\right) = 0. $$

Waiting is worth

$$ (0.5)\max(0, 0 - 20) + (0.5)\max(0, 40 - 20) = 10, $$

ten thousand dollars,
because waiting captures the upside
and discards the case
in which the twenty thousand would have been wasted.
The provisional turns a break-even decision
into ten thousand dollars of expected value,
less its own small premium.

## Disclosure Discipline

A founder discloses constantly.
Pitching investors,
demonstrating a prototype,
publishing a paper,
and selling early units
are all disclosures,
and disclosure interacts with patent rights
in ways the prior-art article set out.
A public disclosure before filing
starts the United States grace-period clock
and forfeits patent rights
in most foreign countries outright,
which can quietly close doors
the founder did not know were open.

The discipline that follows is simple.
File the provisional before disclosing publicly,
so that the disclosure that helps raise money or sell product
does not cost the patent option.
[Confidentiality agreements][ref_nda] help
where they can be obtained,
but investors commonly decline to sign them,
which makes the inexpensive provisional,
filed first,
the practical protection.
The sequence is the point.
File, then disclose,
and the order is cheap to honor
and expensive to reverse.

## Get the Assignments Right

A patent is owned by its inventors
until they assign it,
and the company that intends to hold the patent
must actually obtain that assignment.
This is the most common and most damaging
intellectual-property mistake a startup makes,
and it has nothing to do with the patent office.
A co-founder who left,
a contractor who wrote part of the code,
or an engineer hired without a proper agreement
may each own a slice of the company's inventions,
and an unassigned co-inventor
is a defect that surfaces
at the worst possible moment,
during the [due diligence][ref_due_diligence]
of a financing or an acquisition.

The remedy is to require,
from the first day and from everyone,
founders, employees, and contractors alike,
a written agreement
assigning inventions to the company.
The cost of doing this early is trivial.
The cost of repairing it later,
by tracking down a departed contributor
whose signature a deal now depends on,
can be severe,
and occasionally the contributor
has no reason to cooperate.
Ownership is plumbing.
It is invisible when it works
and catastrophic when it does not.

## Non-Dilutive Funding and the Patent

For a founder in a research-heavy field,
there is a way to fund the work
and build a patent position
without giving up equity.
The Small Business Innovation Research
and Small Business Technology Transfer programs,
known as SBIR and STTR,
award federal research funding
that the company need not repay
and that does not dilute ownership.
Under the [Bayh-Dole Act][ref_bayh_dole],
the company retains patents
on the inventions it makes under the award,
so the funding builds the company's intellectual property
rather than the government's.

The programs also carry a data-rights protection
that behaves like a trade secret for a period,
preserved by marking the deliverables,
the connection the
[disclosure-tradeoff article][related_post_patent_secrets]
drew between patents and secrecy.
The full treatment of the rights,
the marking discipline,
and the ways they are lost
is in the
[SBIR and STTR data-rights article][related_post_sbir_ip].
For the founder the point is that
non-dilutive funding and retained patents
can be had together,
which makes these programs
worth understanding
for any company whose value
rests on funded research.

## A Decision Framework

The threads gather into a short framework.

Default to restraint.
Put the company's scarce resources
into product and distribution,
and do not let the fear of idea theft
pull money away from the work
that actually builds a moat.

File a provisional
when an invention is genuinely core,
is the kind a shipped product would reveal
or a competitor could reverse engineer,
and is valuable enough
that priority and patent-pending status are worth a small premium.
Treat the provisional as an option,
and decide on the costly non-provisional
only when the evidence is in.

Keep the disclosure discipline.
File before pitching, demonstrating, or selling.

Get the assignments in order from day one,
from everyone.

Consider the funded-research path
where the field allows it,
to build patents without dilution.

And choose among patenting, secrecy,
and defensive publication
by the logic of the disclosure-tradeoff article.
Patent what a product reveals,
keep secret what stays hidden,
and use [defensive publication][ref_defensive_publication]
to keep a piece of the commons open
when the goal is only to stop others
from fencing it off.

## Epistemic State

The settled matters here
are the structure of patent costs,
the function of the provisional application,
the first-inventor-to-file rule,
the interaction of disclosure with patent rights,
the necessity of assignment,
and the non-dilutive nature of the funded-research programs.
These should hold against independent verification.

The expected-value reframing
is a continuation of the moat article's model,
and inherits its character as a framework
rather than a measurement.
The signaling and acquisition value $S$ in particular
is real but hard to quantify,
and the claim that the enforcement probability
is near zero for a startup
is a generalization
that a well-funded or well-allied startup
can escape.

The cost figures are orders of magnitude,
not quotes,
and they vary widely with field, counsel, and jurisdiction.
The strategic advice is general,
sound in the typical case
and subject to exceptions.
Throughout, this is general information,
United States centric,
and not legal or financial advice.

## Out of Scope

The detailed mechanics of patent prosecution,
the negotiation of an assignment or a license,
and the legal process of a financing or an acquisition
are matters for counsel.
The specifics of international filing strategy
beyond the disclosure warning above
are left to the international portion of the opening article
and to local counsel.
The tax treatment of intellectual property,
and the founder's personal considerations
such as qualified small business stock,
are outside this series.
The mechanics of the funded-research programs themselves,
the eligibility, the proposals, and the award management,
are the subject of their own dedicated series.

## Conclusion

For the early-stage founder,
a patent is rarely the moat
and almost never the priority,
because the protection it nominally offers
depends on an enforcement budget
the company does not have.
What a patent does offer a startup
is priority, signaling, and value in a sale,
and those are worth securing cheaply
through a provisional,
kept as an option,
filed before disclosure,
and resting on inventions
the company actually owns.
Put the scarce money into the product,
keep the patent option open for a small premium,
get the ownership right from the first day,
and reach for the funded-research path
where the field allows it.
The next article asks
[what enforcing a patent actually requires][related_post_patent_enforcement],
which is the reality
that stands behind
the small enforcement probability
this article assumed.

## References

- [Reference, Bayh-Dole Act][ref_bayh_dole]
- [Reference, Defensive Publication][ref_defensive_publication]
- [Reference, Due Diligence][ref_due_diligence]
- [Reference, Expected Value][ref_expected_value]
- [Reference, First to File and First to Invent][ref_first_to_file]
- [Reference, Jensen's Inequality][ref_jensen]
- [Reference, Non-Disclosure Agreement][ref_nda]
- [Reference, Patent][ref_patent]
- [Reference, Provisional Application][ref_provisional_application]
- [Reference, Real Options Valuation][ref_real_options]
- [Reference, Signalling in Economics][ref_signaling]
- [Related Post, Data Rights and Intellectual Property in SBIR and STTR][related_post_sbir_ip]
- [Related Post, Patent Enforcement Reality][related_post_patent_enforcement]
- [Related Post, Patents, Trade Secrets, and the Disclosure Tradeoff][related_post_patent_secrets]
- [Related Post, Prior Art and the Foundation of Patentability][related_post_prior_art]
- [Related Post, What a Patent Is and Is Not][related_post_patent_basics]
- [Related Post, What It Takes to Succeed and Where Moats Come From][related_post_startup_moats]
- [Related Post, What Makes a Patent an Effective Moat][related_post_patent_moat]

[ref_bayh_dole]: https://en.wikipedia.org/wiki/Bayh%E2%80%93Dole_Act
[ref_defensive_publication]: https://en.wikipedia.org/wiki/Defensive_publication
[ref_due_diligence]: https://en.wikipedia.org/wiki/Due_diligence
[ref_expected_value]: https://en.wikipedia.org/wiki/Expected_value
[ref_first_to_file]: https://en.wikipedia.org/wiki/First_to_file_and_first_to_invent
[ref_jensen]: https://en.wikipedia.org/wiki/Jensen's_inequality
[ref_nda]: https://en.wikipedia.org/wiki/Non-disclosure_agreement
[ref_patent]: https://en.wikipedia.org/wiki/Patent
[ref_provisional_application]: https://en.wikipedia.org/wiki/Provisional_application
[ref_real_options]: https://en.wikipedia.org/wiki/Real_options_valuation
[ref_signaling]: https://en.wikipedia.org/wiki/Signalling_(economics)
[related_post_patent_basics]: {% post_url 2026-05-03-what_a_patent_is_and_is_not %}
[related_post_patent_enforcement]: {% post_url 2026-05-08-patent_enforcement_reality %}
[related_post_patent_moat]: {% post_url 2026-05-05-what_makes_a_patent_an_effective_moat %}
[related_post_patent_secrets]: {% post_url 2026-05-06-patents_trade_secrets_and_the_disclosure_tradeoff %}
[related_post_prior_art]: {% post_url 2026-05-04-prior_art_and_the_foundation_of_patentability %}
[related_post_sbir_ip]: {% post_url 2026-06-22-data_rights_and_intellectual_property_for_sbir_and_sttr %}
[related_post_startup_moats]: {% post_url 2026-05-14-what_it_takes_to_succeed_and_where_moats_come_from %}
