---
layout: post
mathjax: true
comments: true
title:  "Patents for the Early-Stage Founder"
date:   2026-05-07 09:00:00 +0000
categories: business intellectual-property patents
series: patents_and_startups
series_title: Patent and Startup Strategy
series_index: 5
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

$$
 E = p_v \, p_d \, p_e \, V - C, 
\tag{1}
$$

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

$$
 E_{\text{founder}} = p_v \, p_d \, p_e \, V + S - C, 
\tag{2}
$$

and because the protective term is small for a startup,
this reduces in practice to

$$
 E_{\text{founder}} \approx S - C. 
\tag{3}
$$

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

$$
 \max\!\left(0,\; E[X] - K\right). 
\tag{4}
$$

A founder who files the provisional
defers the decision until $X$ is known,
and then converts only if the realized value exceeds the cost,
so the value of waiting, before the small premium, is

$$
 E\!\left[\max\!\left(0,\; X - K\right)\right]. 
\tag{5}
$$

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

$$
 \max\!\left(0,\; (0.5)(0) + (0.5)(40) - 20\right) = 0. 
\tag{6}
$$

Waiting is worth

$$
 (0.5)\max(0, 0 - 20) + (0.5)\max(0, 40 - 20) = 10, 
\tag{7}
$$

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

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 7 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 7, 4 are established and 3 are bespoke.
Values and costs are in a common monetary unit, thousands of dollars in the provisional example, and probabilities are dimensionless numbers between zero and one.

*Equation 1, Bespoke Expected Value of a Patent Moat.*
The moat model of the series discounts the protected value by the product of the probabilities of validity, detection and enforcement and subtracts the cost, a construction that treats the three events as independent.
[expected-value][ref_expected_value]

$$
 E = p_v \, p_d \, p_e \, V - C, 
\tag{1}
$$

*Equation 2, Bespoke Founder Expected Value with Signalling.*
The article adds to the moat model a signalling and acquisition value that a patent provides to investors and acquirers independently of enforcement.
[signaling][ref_signaling]

$$
 E_{\text{founder}} = p_v \, p_d \, p_e \, V + S - C, 
\tag{2}
$$

*Equation 3, Bespoke Founder Value Without Enforcement.*
Taking the enforcement probability of an early-stage company as near zero removes the protective term and leaves the signalling value less the cost.

$$
 E_{\text{founder}} \approx S - C. 
\tag{3}
$$

**Equation 4, Value of Deciding Now.**
A decision maker who must commit now invests only if the expected value exceeds the cost, so the value of deciding now is the larger of zero and that difference.
[real option][ref_real_options]

$$
 \max\!\left(0,\; E[X] - K\right). 
\tag{4}
$$

**Equation 5, Value of Waiting as a Real Option.**
A decision maker who waits until the value is known converts only when it exceeds the cost, which by Jensen's inequality is worth at least as much as deciding now.
[Jensen's inequality][ref_jensen]

$$
 E\!\left[\max\!\left(0,\; X - K\right)\right]. 
\tag{5}
$$

**Equation 6, Value of Deciding Now in the Two-Outcome Example.**
For an illustrative patent worth zero or forty with equal probability and a conversion cost of twenty, deciding now breaks even at zero.

$$
 \max\!\left(0,\; (0.5)(0) + (0.5)(40) - 20\right) = 0. 
\tag{6}
$$

**Equation 7, Value of Waiting in the Two-Outcome Example.**
The same illustrative patent is worth ten when the decision waits, because waiting keeps the upside and discards the loss.

$$
 (0.5)\max(0, 0 - 20) + (0.5)\max(0, 40 - 20) = 10, 
\tag{7}
$$

### Notation

- $E$, the expected value of the patent as a moat
- $p_v$, the probability the patent is valid
- $p_d$, the probability that infringement is detected
- $p_e$, the probability of successful enforcement
- $V$, the protected value
- $C$, the cost of the patent
- $S$, the signalling and acquisition value
- $E_{\text{founder}}$, the expected value of the patent to a founder
- $X$, the value the patent will turn out to have, unknown when the provisional is filed
- $K$, the cost of the non-provisional that converts the provisional

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Tertiary Sources

- "Bayh–Dole Act." 2026. Wikipedia. Last modified May 14, at 20:01 (UTC). [https://en.wikipedia.org/w/index.php?title=Bayh%E2%80%93Dole\_Act&oldid=1354176187][ref_bayh_dole]
- "Defensive Publication." 2026. Wikipedia. Last modified April 3, at 10:55 (UTC). [https://en.wikipedia.org/w/index.php?title=Defensive\_publication&oldid=1346866157][ref_defensive_publication]
- "Due Diligence." 2026. Wikipedia. Last modified June 4, at 10:07 (UTC). [https://en.wikipedia.org/w/index.php?title=Due\_diligence&oldid=1357729520][ref_due_diligence]
- "Expected Value." 2026. Wikipedia. Last modified June 18, at 22:28 (UTC). [https://en.wikipedia.org/w/index.php?title=Expected\_value&oldid=1360048950][ref_expected_value]
- "First to File and First to Invent." 2025. Wikipedia. Last modified September 4, at 15:25 (UTC). [https://en.wikipedia.org/w/index.php?title=First\_to\_file\_and\_first\_to\_invent&oldid=1309521120][ref_first_to_file]
- "Jensen's Inequality." 2026. Wikipedia. Last modified June 10, at 20:22 (UTC). [https://en.wikipedia.org/w/index.php?title=Jensen's\_inequality&oldid=1358765414][ref_jensen]
- "Non-Disclosure Agreement." 2026. Wikipedia. Last modified April 29, at 07:43 (UTC). [https://en.wikipedia.org/w/index.php?title=Non-disclosure\_agreement&oldid=1351647748][ref_nda]
- "Patent." 2026. Wikipedia. Last modified June 23, at 20:39 (UTC). [https://en.wikipedia.org/w/index.php?title=Patent&oldid=1360822017][ref_patent]
- "Provisional Application." 2025. Wikipedia. Last modified May 23, at 19:20 (UTC). [https://en.wikipedia.org/w/index.php?title=Provisional\_application&oldid=1291846802][ref_provisional_application]
- "Real Options Valuation." 2026. Wikipedia. Last modified June 17, at 07:14 (UTC). [https://en.wikipedia.org/w/index.php?title=Real\_options\_valuation&oldid=1359795820][ref_real_options]
- "Signalling (Economics)." 2026. Wikipedia. Last modified April 27, at 09:18 (UTC). [https://en.wikipedia.org/w/index.php?title=Signalling\_(economics)&oldid=1351333538][ref_signaling]

### Related Posts

- Sechter, Brendan. 2026. "What a Patent Is and Is Not." *Brendan A R Sechter's Development Blog*, May 3. [https://sgeos.github.io/business/intellectual-property/patents/2026/05/03/what\_a\_patent\_is\_and\_is\_not.html][related_post_patent_basics]
- Sechter, Brendan. 2026. "Prior Art and the Foundation of Patentability." *Brendan A R Sechter's Development Blog*, May 4. [https://sgeos.github.io/business/intellectual-property/patents/2026/05/04/prior\_art\_and\_the\_foundation\_of\_patentability.html][related_post_prior_art]
- Sechter, Brendan. 2026. "What Makes a Patent an Effective Moat." *Brendan A R Sechter's Development Blog*, May 5. [https://sgeos.github.io/business/intellectual-property/patents/2026/05/05/what\_makes\_a\_patent\_an\_effective\_moat.html][related_post_patent_moat]
- Sechter, Brendan. 2026. "Patents, Trade Secrets, and the Disclosure Tradeoff." *Brendan A R Sechter's Development Blog*, May 6. [https://sgeos.github.io/business/intellectual-property/patents/2026/05/06/patents\_trade\_secrets\_and\_the\_disclosure\_tradeoff.html][related_post_patent_secrets]
- Sechter, Brendan. 2026. "Patent Enforcement Reality." *Brendan A R Sechter's Development Blog*, May 8. [https://sgeos.github.io/business/intellectual-property/patents/2026/05/08/patent\_enforcement\_reality.html][related_post_patent_enforcement]
- Sechter, Brendan. 2026. "What It Takes to Succeed and Where Moats Come From." *Brendan A R Sechter's Development Blog*, May 14. [https://sgeos.github.io/business/strategy/startups/2026/05/14/what\_it\_takes\_to\_succeed\_and\_where\_moats\_come\_from.html][related_post_startup_moats]
- Sechter, Brendan. 2026. "Data Rights and Intellectual Property in SBIR and STTR." *Brendan A R Sechter's Development Blog*, June 22. [https://sgeos.github.io/business/funding/sbir/2026/06/22/data\_rights\_and\_intellectual\_property\_for\_sbir\_and\_sttr.html][related_post_sbir_ip]

[ref_bayh_dole]: https://en.wikipedia.org/w/index.php?title=Bayh%E2%80%93Dole_Act&oldid=1354176187
[ref_defensive_publication]: https://en.wikipedia.org/w/index.php?title=Defensive_publication&oldid=1346866157
[ref_due_diligence]: https://en.wikipedia.org/w/index.php?title=Due_diligence&oldid=1357729520
[ref_expected_value]: https://en.wikipedia.org/w/index.php?title=Expected_value&oldid=1360048950
[ref_first_to_file]: https://en.wikipedia.org/w/index.php?title=First_to_file_and_first_to_invent&oldid=1309521120
[ref_jensen]: https://en.wikipedia.org/w/index.php?title=Jensen's_inequality&oldid=1358765414
[ref_nda]: https://en.wikipedia.org/w/index.php?title=Non-disclosure_agreement&oldid=1351647748
[ref_patent]: https://en.wikipedia.org/w/index.php?title=Patent&oldid=1360822017
[ref_provisional_application]: https://en.wikipedia.org/w/index.php?title=Provisional_application&oldid=1291846802
[ref_real_options]: https://en.wikipedia.org/w/index.php?title=Real_options_valuation&oldid=1359795820
[ref_signaling]: https://en.wikipedia.org/w/index.php?title=Signalling_(economics)&oldid=1351333538
[related_post_patent_basics]: {% post_url 2026-05-03-what_a_patent_is_and_is_not %}
[related_post_patent_enforcement]: {% post_url 2026-05-08-patent_enforcement_reality %}
[related_post_patent_moat]: {% post_url 2026-05-05-what_makes_a_patent_an_effective_moat %}
[related_post_patent_secrets]: {% post_url 2026-05-06-patents_trade_secrets_and_the_disclosure_tradeoff %}
[related_post_prior_art]: {% post_url 2026-05-04-prior_art_and_the_foundation_of_patentability %}
[related_post_sbir_ip]: {% post_url 2026-06-22-data_rights_and_intellectual_property_for_sbir_and_sttr %}
[related_post_startup_moats]: {% post_url 2026-05-14-what_it_takes_to_succeed_and_where_moats_come_from %}
