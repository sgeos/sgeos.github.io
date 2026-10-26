---
layout: post
mathjax: true
comments: true
title:  "Patent Enforcement Reality"
date:   2026-05-08 09:00:00 +0000
categories: business intellectual-property patents
series: patents_and_startups
series_title: Patent and Startup Strategy
series_index: 6
---
<!-- A166 -->
<script>console.log("A166");</script>

A patent is a right to exclude,
but the state that grants the right
does not enforce it.
Enforcement is the holder's burden,
carried through litigation the holder funds,
and patent litigation is among the most expensive,
slowest, and riskiest forms of civil suit.
This is the reality
that stood behind the small enforcement probability
the [moat article][related_post_patent_moat] put in its model
and the [founder article][related_post_patent_founder] leaned on.
A patent that cannot be enforced
protects nothing,
and whether a given holder can enforce a given patent
is a question of money, time, and nerve
at least as much as of law.
This article sets out what enforcement actually requires.
As with the rest of the series,
this is general information rather than legal advice,
and it assumes filing in the United States.

## A Brief History

Patent enforcement has swung
between extremes within living memory.
The creation of the
[United States Court of Appeals for the Federal Circuit][ref_cafc]
in 1982
gave patent appeals a single specialized court
and, for two decades,
a reputation for strengthening patents.
The pendulum then swung back.
The Supreme Court's decision in
[eBay v. MercExchange][ref_ebay]
in 2006
ended the near-automatic injunction,
the [America Invents Act][ref_aia] of 2011
created a cheaper administrative path
to challenge validity,
and a wave of assertion
by entities that made no products
provoked a decade of decisions and reforms
aimed at curbing abusive suits.
The lesson of the history
is that the value of a patent in enforcement
is not fixed by the grant.
It moves with the courts, the statutes, and the costs,
and it has moved a great deal.

## The State Does Not Enforce

The most basic fact of enforcement
is the one the opening article named.
A patent is not self-enforcing.
No agency patrols the market for infringers.
The holder must notice the infringement,
decide to act,
and bring a [patent infringement suit][ref_patent_infringement]
in federal court,
because patents are creatures of federal law.
The burden of proof, the cost, and the risk
all sit with the holder.

This single fact
reorganizes everything that follows.
A right that the owner must enforce at the owner's expense
is worth what the owner can afford to spend on it,
and against whom.
A holder who cannot fund a suit
holds a right
that a competitor with deeper pockets
can infringe in practical safety.

## The Cost and the Clock

A patent infringement suit
is a multi-year, multi-million-dollar undertaking.
A contested case
that runs toward trial
commonly costs each side
in the millions of dollars,
and the most valuable cases cost more.
The money buys a long sequence.
A complaint opens the case.
A [claim construction][ref_markman] hearing,
often called a Markman hearing,
fixes the meaning of the claims,
and because the claims define the right,
this step alone
frequently decides the outcome.
Discovery, the exchange of documents and testimony,
consumes much of the cost.
A trial follows for the cases that reach one,
and an appeal to the Federal Circuit follows many verdicts.
The whole arc runs years,
often three to five,
during which the technology and the market
do not stand still.

For a small company
the cost and the clock are usually decisive.
A startup cannot divert millions of dollars
and years of attention
into a lawsuit
without ceasing to be a startup,
which is the concrete reason
the founder article treated the enforcement probability
as near zero.

## Asserting Puts the Patent at Risk

Enforcement is not only expensive.
It is dangerous to the patent itself.
A patent that is never asserted
is never seriously tested,
but the moment it is asserted
the defendant has every incentive
to destroy it.
The defendant will argue non-infringement,
and, more dangerously,
will argue that the patent is invalid
over [prior art][related_post_prior_art]
that the examiner never saw.

The America Invents Act
sharpened this risk
by creating [inter partes review][ref_ipr],
an administrative proceeding
before the [Patent Trial and Appeal Board][ref_ptab]
in which a challenger
attacks the patent's validity
on prior-art grounds,
faster and more cheaply than a trial,
and with a record of invalidating
a large share of the claims it reviews.
A holder who asserts a patent
therefore wagers the asset.
A win brings damages, and perhaps an injunction.
A loss can leave the patent
narrowed or dead,
and a patent struck down
is gone against everyone,
not only the defendant who killed it.
The decision to enforce
is a decision to put the patent on trial.

## The Wager of Assertion

The risk of asserting a patent can be priced,
and the price explains
why holders so often decline to sue
on patents they believe are strong.

A patent's value is rarely confined to a single infringer.
A strong patent is a threat
against every potential infringer in the market,
and that threat is the source of the licenses it can command.
Call the wider value $W$,
the worth of the patent as a credible threat
against everyone other than the defendant at hand.

Asserting the patent against one defendant
puts $W$ at risk,
because if the patent is invalidated
it is dead against everyone,
not only against the defendant who killed it.
Let $p_v$ be the probability the patent survives the validity challenge,
$p_i$ the probability infringement is found if it survives,
$D$ the damages from this defendant,
and $C_p$ the cost of suing.
The expected value of asserting is

$$ E[\text{assert}] = p_v \, p_i \, D - C_p - (1 - p_v)\, W. $$

The first two terms are the gain the moat article would recognize,
the probability-weighted damages less the cost.
The third term is new and often dominant.
With probability $1 - p_v$ the patent is struck down,
and the holder loses not this case alone
but the wider value $W$ that the threat was worth.

A worked instance, in millions of dollars.
Suppose the patent is worth fifty as a threat across the market,
survives validity with probability seven tenths,
and would, if it survives,
win damages of ten from this defendant with probability eight tenths,
at a litigation cost of two.
The gain from the suit is

$$ (0.7)(0.8)(10) - 2 = 3.6, $$

but the wager against the wider value is

$$ (1 - 0.7)(50) = 15, $$

so the expected value of asserting is

$$ 3.6 - 15 = -11.4, $$

a loss of more than eleven million.
The holder is far better off
licensing under the threat than testing the patent in court,
because a patent worth fifty million untested
can be worth nothing the day after a verdict.
This is the formal reason
a credible threat is often more valuable than a suit,
and why the strongest patents
are frequently the ones least often litigated.

## What a Win Is Worth

The remedies for infringement
are narrower than they once were.
An injunction,
the order that actually stops the infringer,
is no longer automatic.
Since eBay v. MercExchange
a court weighs a four-factor test,
and a holder who does not practice the invention
often cannot meet it,
winning money but not exclusion.
Damages are the more reliable remedy.
Their floor is a
[reasonable royalty][ref_royalty],
the royalty a willing licensor and licensee
would have negotiated,
and a holder who practices the patent
and can prove lost sales
may instead recover lost profits.
Willful infringement
can raise the award,
and a court may shift attorney fees
in an exceptional case,
but these are the exceptions.
The ordinary outcome of a successful suit
is a reasonable royalty,
which is often far less
than the headline value of the market at issue.

## The Economics of the Settlement

Most patent suits never reach a verdict.
They [settle][ref_settlement],
and the logic of the settlement
shows where the leverage in enforcement really lies.

Let $D$ be the damages at stake if the plaintiff wins,
$q$ the probability the patent is held valid and infringed,
which folds the merits into one number,
$C_p$ the plaintiff's cost of litigating to the end,
and $C_d$ the defendant's.
A plaintiff who fights to the end
expects the [expected value][ref_expected_value] $qD - C_p$,
and so will not settle for less.
A defendant who fights to the end
expects to pay $qD + C_d$,
and so will not pay more.
Settlement is rational for any amount in the range

$$ \left[\, qD - C_p,\; qD + C_d \,\right]. $$

The width of that range is $C_p + C_d$,
the combined cost of fighting,
and a settlement exists
because both sides prefer to split that saving
rather than burn it on lawyers.

Two features of the range
explain the reality of enforcement.
The center of the range is $qD$,
the merits times the stakes,
so a holder with a genuinely strong patent,
large damages,
and the resources to threaten trial credibly
can extract real value.
But look at what happens
when the patent is weak,
so that $q$ approaches zero.
The plaintiff's walk-away, $qD - C_p$,
goes negative,
meaning a rational plaintiff
would lose money at trial.
The defendant's walk-away, $qD + C_d$,
stays positive at about $C_d$.
A defendant will pay up to its own cost of defense
to make even a meritless case disappear.
This is the nuisance value of a patent suit,

$$ S_{\text{nuisance}} \approx C_d, $$

a settlement extracted
not from the strength of the patent
but from the cost of defending against it.

A worked instance,
in millions of dollars.
With damages $D = 10$,
a merits probability $q = 0.3$,
and equal litigation costs $C_p = C_d = 2$,
the settlement range is

$$ \left[\, (0.3)(10) - 2,\; (0.3)(10) + 2 \,\right] = \left[\, 1,\; 5 \,\right], $$

centered on the expected merits outcome of three.
Now let the patent be almost certainly invalid,
$q = 0.02$.
The plaintiff would lose money at trial,
since $qD - C_p = 0.2 - 2 = -1.8$,
yet the defendant still faces about two
in defense costs,
so a settlement near two
can be pulled from a case
that should never have been brought.

The lesson runs in two directions.
A well-resourced holder
can wield the cost of defense
as a weapon against a smaller rival,
and a [non-practicing entity][ref_patent_troll]
that makes nothing
and so fears no countersuit
can build a business on nuisance settlements alone.
The cost of litigation,
not the merit of the patent,
is the lever,
which is why enforcement
favors whoever can better afford the fight.

## Enforcement Without a Courtroom

Because litigation is so costly,
most enforcement happens in its shadow
rather than in it.
A credible threat to sue
is itself the instrument,
and most disputes resolve
into a license negotiated
under that threat.
Large companies with deep portfolios
practice a mutual version of this,
[cross-licensing][ref_cross_license]
their patents to one another
so that each is free to operate
and none sues,
a détente that smaller players,
holding fewer patents,
cannot enter on equal terms.
The credibility of the threat
is everything,
and credibility is bought
with the resources and the will to litigate.
A holder who cannot fight
cannot threaten,
and a license
is only as valuable as the suit behind it.

## The Players

The cost structure sorts the participants.
Operating companies enforce against competitors,
usually reluctantly,
because litigation is a distraction from building.
[Non-practicing entities][ref_patent_troll],
which hold patents to assert rather than to make products,
turn the cost asymmetry into a model,
since they have no operations to countersue
and no product to enjoin,
and they often fund their suits
through [litigation finance][ref_litigation_funding]
that supplies the capital in exchange for a share of the award.
Defensive aggregators and [patent pools][ref_patent_pool]
form on the other side
to blunt these suits.
The common thread
is that the ability to bear cost and risk,
not the quality of the underlying invention,
determines who prevails.

## The Reality for the Small Holder

The threads gather into a hard conclusion
for the founder and the small company.
A patent's protective value
is gated by enforceability,
and enforceability is mostly out of reach
for a holder who cannot fund a multi-million-dollar suit
against an opponent who can.
This is why the founder article
counseled valuing a patent
for priority, signaling, and sale
rather than for litigation.

The asymmetry cuts both ways,
and the second edge is easy to forget.
A small company is not only
a holder who cannot enforce.
It is also a target
that cannot easily defend.
The same nuisance economics
that a startup cannot exploit as a plaintiff
can be turned against it as a defendant,
when a well-funded holder
or a non-practicing entity
asserts a patent
and offers to settle
for less than the cost of defense.
For the small company,
the cost of patent litigation
is a danger from both sides of the caption.

## Epistemic State

The settled matters here
are that a patent is not self-enforcing,
that infringement suits are expensive and slow,
that asserting a patent exposes it
to invalidation over prior art,
that injunctions are no longer automatic after eBay,
and that most suits settle.
These should hold against independent verification.

The settlement model is a simplification.
It folds the merits into a single probability $q$,
assumes both sides estimate the odds and the costs alike,
and ignores the asymmetries of information,
risk tolerance,
and strategic reputation
that shape real negotiations.
It is offered to make the structure of leverage clear,
not to predict a particular settlement.
The assertion wager is a simplification in the same spirit,
compressing the patent's market-wide threat value
into a single number $W$ that is hard to estimate,
and treating invalidation as all-or-nothing.

The cost and duration figures
are typical orders of magnitude,
not quotes,
and they vary widely with the stakes,
the venue,
and the parties.
The characterization of non-practicing-entity behavior
is a general pattern
with honest and abusive examples alike.
Throughout, this is general information,
United States centric,
and not legal advice.

## Out of Scope

The detailed procedure of an infringement trial
and of an inter partes review,
the rules of claim construction,
and the methods of computing damages
are matters for specialists and counsel.
The ongoing policy debate over patent reform,
venue,
and the proper treatment of non-practicing entities
is large and unsettled
and is not adjudicated here.
The enforcement of patents outside the United States,
which varies by jurisdiction
and includes systems with faster or cheaper procedures,
is left to local counsel.

## Conclusion

A patent is worth,
in the end,
what its holder can enforce,
and enforcement is expensive, slow,
and dangerous to the patent itself.
The state grants the right
but leaves the fight to the owner,
the fight costs millions and takes years,
asserting the patent risks losing it,
and the leverage in the fight
comes from the ability to bear its cost
rather than from the merit of the invention.
For most holders, and nearly all small ones,
this places real enforcement out of reach,
which is the deepest reason
that most patents are not moats
and that a startup
should value a patent for what it signals
rather than for what it could win.
This closes the patent half of the series.
The startup half takes up the question
the founder article raised and this one confirmed,
namely [what it takes to succeed and where moats come from][related_post_startup_moats]
when the patent is not the answer.

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Tertiary Sources

- "Cross-Licensing." 2026. Wikipedia. Last modified May 3, at 09:12 (UTC). [https://en.wikipedia.org/w/index.php?title=Cross-licensing&oldid=1352286744][ref_cross_license]
- "EBay Inc. v. MercExchange, L.L.C." 2026. Wikipedia. Last modified May 1, at 05:06 (UTC). [https://en.wikipedia.org/w/index.php?title=EBay\_Inc.\_v.\_MercExchange,\_L.L.C.&oldid=1351961752][ref_ebay]
- "Expected Value." 2026. Wikipedia. Last modified June 18, at 22:28 (UTC). [https://en.wikipedia.org/w/index.php?title=Expected\_value&oldid=1360048950][ref_expected_value]
- "Inter Partes Review." 2025. Wikipedia. Last modified January 16, at 17:53 (UTC). [https://en.wikipedia.org/w/index.php?title=Inter\_partes\_review&oldid=1269845198][ref_ipr]
- "Leahy–Smith America Invents Act." 2026. Wikipedia. Last modified June 8, at 18:31 (UTC). [https://en.wikipedia.org/w/index.php?title=Leahy%E2%80%93Smith\_America\_Invents\_Act&oldid=1358443806][ref_aia]
- "Legal Financing." 2026. Wikipedia. Last modified June 14, at 14:01 (UTC). [https://en.wikipedia.org/w/index.php?title=Legal\_financing&oldid=1359304543][ref_litigation_funding]
- "Markman v. Westview Instruments, Inc." 2026. Wikipedia. Last modified April 27, at 11:26 (UTC). [https://en.wikipedia.org/w/index.php?title=Markman\_v.\_Westview\_Instruments,\_Inc.&oldid=1351346978][ref_markman]
- "Patent Infringement." 2026. Wikipedia. Last modified May 30, at 09:27 (UTC). [https://en.wikipedia.org/w/index.php?title=Patent\_infringement&oldid=1356867726][ref_patent_infringement]
- "Patent Pool." 2026. Wikipedia. Last modified March 14, at 23:29 (UTC). [https://en.wikipedia.org/w/index.php?title=Patent\_pool&oldid=1343538585][ref_patent_pool]
- "Patent Trial and Appeal Board." 2026. Wikipedia. Last modified February 9, at 06:47 (UTC). [https://en.wikipedia.org/w/index.php?title=Patent\_Trial\_and\_Appeal\_Board&oldid=1337403188][ref_ptab]
- "Patent Troll." 2026. Wikipedia. Last modified May 15, at 01:08 (UTC). [https://en.wikipedia.org/w/index.php?title=Patent\_troll&oldid=1354216036][ref_patent_troll]
- "Royalty Payment." 2026. Wikipedia. Last modified June 24, at 15:12 (UTC). [https://en.wikipedia.org/w/index.php?title=Royalty\_payment&oldid=1360931726][ref_royalty]
- "Settlement (Litigation)." 2026. Wikipedia. Last modified June 19, at 23:15 (UTC). [https://en.wikipedia.org/w/index.php?title=Settlement\_(litigation)&oldid=1360209803][ref_settlement]
- "United States Court of Appeals for the Federal Circuit." 2026. Wikipedia. Last modified June 5, at 03:02 (UTC). [https://en.wikipedia.org/w/index.php?title=United\_States\_Court\_of\_Appeals\_for\_the\_Federal\_Circuit&oldid=1357860994][ref_cafc]

### Related Posts

- Sechter, Brendan. 2026. "Prior Art and the Foundation of Patentability." *Brendan A R Sechter's Development Blog*, May 4. [https://sgeos.github.io/business/intellectual-property/patents/2026/05/04/prior\_art\_and\_the\_foundation\_of\_patentability.html][related_post_prior_art]
- Sechter, Brendan. 2026. "What Makes a Patent an Effective Moat." *Brendan A R Sechter's Development Blog*, May 5. [https://sgeos.github.io/business/intellectual-property/patents/2026/05/05/what\_makes\_a\_patent\_an\_effective\_moat.html][related_post_patent_moat]
- Sechter, Brendan. 2026. "Patents for the Early-Stage Founder." *Brendan A R Sechter's Development Blog*, May 7. [https://sgeos.github.io/business/intellectual-property/patents/2026/05/07/patents\_for\_the\_early\_stage\_founder.html][related_post_patent_founder]
- Sechter, Brendan. 2026. "What It Takes to Succeed and Where Moats Come From." *Brendan A R Sechter's Development Blog*, May 14. [https://sgeos.github.io/business/strategy/startups/2026/05/14/what\_it\_takes\_to\_succeed\_and\_where\_moats\_come\_from.html][related_post_startup_moats]

[ref_aia]: https://en.wikipedia.org/w/index.php?title=Leahy%E2%80%93Smith_America_Invents_Act&oldid=1358443806
[ref_cafc]: https://en.wikipedia.org/w/index.php?title=United_States_Court_of_Appeals_for_the_Federal_Circuit&oldid=1357860994
[ref_cross_license]: https://en.wikipedia.org/w/index.php?title=Cross-licensing&oldid=1352286744
[ref_ebay]: https://en.wikipedia.org/w/index.php?title=EBay_Inc._v._MercExchange,_L.L.C.&oldid=1351961752
[ref_expected_value]: https://en.wikipedia.org/w/index.php?title=Expected_value&oldid=1360048950
[ref_ipr]: https://en.wikipedia.org/w/index.php?title=Inter_partes_review&oldid=1269845198
[ref_litigation_funding]: https://en.wikipedia.org/w/index.php?title=Legal_financing&oldid=1359304543
[ref_markman]: https://en.wikipedia.org/w/index.php?title=Markman_v._Westview_Instruments,_Inc.&oldid=1351346978
[ref_patent_infringement]: https://en.wikipedia.org/w/index.php?title=Patent_infringement&oldid=1356867726
[ref_patent_pool]: https://en.wikipedia.org/w/index.php?title=Patent_pool&oldid=1343538585
[ref_patent_troll]: https://en.wikipedia.org/w/index.php?title=Patent_troll&oldid=1354216036
[ref_ptab]: https://en.wikipedia.org/w/index.php?title=Patent_Trial_and_Appeal_Board&oldid=1337403188
[ref_royalty]: https://en.wikipedia.org/w/index.php?title=Royalty_payment&oldid=1360931726
[ref_settlement]: https://en.wikipedia.org/w/index.php?title=Settlement_(litigation)&oldid=1360209803
[related_post_patent_founder]: {% post_url 2026-05-07-patents_for_the_early_stage_founder %}
[related_post_patent_moat]: {% post_url 2026-05-05-what_makes_a_patent_an_effective_moat %}
[related_post_prior_art]: {% post_url 2026-05-04-prior_art_and_the_foundation_of_patentability %}
[related_post_startup_moats]: {% post_url 2026-05-14-what_it_takes_to_succeed_and_where_moats_come_from %}
