---
layout: post
mathjax: true
comments: true
title:  "The Money Behind an SBIR or STTR Award"
date:   2026-06-23 09:00:00 +0000
categories: business funding sbir
---

<!-- A140 -->
<script>console.log("A140");</script>

The earlier articles wrote the technical proposal and described the rights the
company keeps, and along the way they kept deferring the money to a later
article.
This is that article, and it is about three things that decide whether an award
is worth having, the cost proposal that fits the work into the dollars, the
indirect rate that decides how much of the award actually reaches the work, and
the cash flow that determines whether a company that won an award can survive it.
One idea organizes the subject, that the award is a fixed pot and the company
must do three things with it, justify it in a compliant budget, account for it in
a way the government will accept, and finance the gap between spending it and
being paid, and a company that can do the engineering but not these three loses
the value of the award or the company itself.
This is the one article in the series with arithmetic, because the indirect rate
is a number and it matters.
The usual caution holds, that the cost principles, the fee limits, and the rate
mechanics change and depend on the company's structure, so the figures below are
illustrative and current-as-of and the cost regulations and the
[agency instructions][research_sbir_gov] are the authority.

## The Cost Proposal

The cost volume is the budget that accompanies the technical proposal, and it has
its own logic.
It must account for every dollar the work will spend, it must total no more than
the cap the solicitation set, and it must match the
[work plan][related_post_phase_one], since a budget that funds more or fewer
people than the technical volume describes signals that the two were written by
different hands.
Unlike a commercial bid, an SBIR or STTR cost proposal is usually evaluated for
reasonableness rather than scored on lowest price, so the goal is a budget that
is realistic and justified rather than artificially cheap, because a budget too
low to do the work is as damaging as one too high to be credible.
The agency states the budget format and the cost categories in its instructions,
the National Institutes of Health in its [grant guidance][research_nih] and the
contract agencies in their own, so the company fills the prescribed form rather
than inventing one.
The structure of that budget rests on a distinction that governs all of
government cost accounting, the line between direct and indirect costs.

## Direct and Indirect Costs

Every dollar a company spends is either direct or indirect, and the difference is
whether it can be tied to one project.
The direct costs are the ones attributable to the specific award, the labor of
the people working on it, the materials and equipment it consumes, the travel it
requires, and the subcontractors and consultants it engages within the work-split
limits the eligibility article set.
Equipment bought with award funds can carry title rules of its own, so a company
may find it has budgeted for equipment it does not ultimately own.
The [indirect costs][ref_indirect] are the ones the company incurs that cannot be
tied to a single project, and they fall into pools, the fringe benefits that load
every salary, the [overhead][ref_overhead] of facilities and indirect labor, and
the general and administrative cost of running the company, its executives, its
accounting, its business development.
The fringe is the [employee-benefit][ref_fringe] burden on labor, and the
overhead and the general and administrative pools cover everything the company
needs to exist but that no single project pays for, and the whole apparatus of
[cost accounting][ref_cost_accounting] exists to sort these dollars correctly.

## The Indirect Rate

The indirect costs reach the award through a rate, and the rate is the most
important number in the budget.
An indirect rate is a pool of indirect cost divided by a base over which it is
spread,

$$ \text{rate} = \frac{\text{indirect cost pool}}{\text{allocation base}}, $$

so an overhead rate might be the overhead pool divided by direct labor, and a
general-and-administrative rate the general-and-administrative pool divided by
total cost.
The effect is that a dollar of direct labor arrives at the award loaded by the
rates stacked on it,

$$ \text{loaded cost} \approx \text{direct labor} \times (1 + f) \times (1 + o) \times (1 + g), $$

with $f$, $o$, and $g$ the fringe, overhead, and general-and-administrative rates,
an illustrative chain whose exact application depends on the company's accounting
structure.
A company with no history proposes a provisional rate, which it must build by
modeling its costs forward without the data an established firm would have, and
later settles it against its actual costs, while an established firm carries rates
negotiated with its cognizant agency, and either way the rate decides how much of
a fixed award funds the work and how much covers the company, so a rate set too
high prices the company out of competitiveness and one set too low starves it of
the overhead it genuinely needs.
The settling of a provisional rate against the actual one is itself a risk, since
a rate that comes in higher than billed leaves the company to absorb an
under-recovery and one that comes in lower obliges it to repay an over-recovery,
and on a fixed-price award the company bears the whole of the variance, so the
provisional rate is estimated with care rather than optimism.

## Fee and the Two Contract Types

On a contract the company may also earn a margin.
A cost-reimbursement award, in the family of the
[cost-plus contract][ref_cost_plus], pays the company its allowable costs plus a
fee, a reasonable profit commonly capped near a single-digit percentage on these
awards, so the company is not merely reimbursed but earns something, while a
[fixed-price][ref_fixed_price] award pays an agreed amount for the work and lets
the company keep the difference if it delivers for less.
Grants generally carry no fee, since they fund the work rather than buy a
deliverable, so whether a company earns a margin depends on the agency and the
instrument, the grant-versus-contract distinction the survey drew.
The program also generally requires no cost share, unlike some federal research
funding, so the company need not contribute matching money of its own beyond the
Phase II enhancement the earlier article described.
The two contract types also differ in risk and in what they demand of the
accounting, since a cost-reimbursement award requires the government to trust the
company's books in a way a fixed-price award does not.

## Compliant Accounting

The government will not reimburse costs it cannot trust, so it requires an
accounting system that meets its standards.
The system must segregate direct from indirect costs, accumulate costs by
project, record labor through a timekeeping discipline, and exclude the costs the
rules forbid, and for a cost-reimbursement award it must be judged adequate before
the award, a determination that at the [defense agencies][research_dod] involves
the [Defense Contract Audit Agency][ref_dcaa].
For a small startup this is real and early work, since a compliant system is not
the spreadsheet a founder kept before, and setting it up, with proper timekeeping
and cost segregation, is a prerequisite for the cost-reimbursement awards rather
than an afterthought.
The standard is proportionate, since the smallest firms are spared the full
[cost-accounting standards][ref_cost_accounting] that govern large contractors,
but even the smallest must keep books the government can audit.

## Allowable and Unallowable Costs

Not every real cost may be charged to the government.
The cost principles of the [acquisition regulations][ref_far] sort costs into
allowable and unallowable, and a company may not charge the unallowable ones to
an award however genuinely it incurred them, the entertainment, the alcohol, the
lobbying, and certain interest and penalties among them.
The company must therefore know the rules and structure its accounting to exclude
the unallowable costs from the pools it bills, since charging an unallowable cost
is not a clerical error but a finding in an audit and a source of the liability
the compliance article will treat.
The discipline is to learn the cost principles early and build them into the
accounting rather than discovering them when a cost is disallowed after the fact.

## Cash Flow, the Quiet Killer

The award that bankrupts the company is the one whose cash was never planned.
Payment lags the work, since the company spends on payroll and materials now and
invoices and waits for reimbursement later, and between phases there is the gap
the [Phase II article][related_post_phase_two] described during which no award
money flows at all, so a company can hold a two-million-dollar Phase II and still
miss a payroll.
The discipline is to manage the [cash flow][ref_cash_flow] as deliberately as the
technology, to invoice promptly and track the [burn rate][ref_burn_rate] and the
runway it leaves, and to arrange the outside financing, the matching funds and the
investment the Phase II and [Phase III][related_post_phase_three] articles
described, that bridges the spans the award does not cover.
Beyond that, a company can finance the receivable itself, with a
[line of credit][ref_line_of_credit] or the factoring of its government invoices,
which turns a slow-paying invoice into cash now at a cost.
A company that plans the cash survives the award, and one that treats a won award
as money in hand discovers that the money arrives slowly and the bills arrive on
time.

## A Note on Assistance Funds

The program offers a small help with the business side.
A company may request a modest amount of technical and business assistance
funding, outside the award's own cap, to pay for the commercialization help, the
market research, and the intellectual-property advice that a small technical team
often lacks, the support the strategy article will place in its wider ecosystem.
It is not large, but it is non-dilutive money for exactly the business
capabilities the program wants the company to build, so a company takes it where
it is offered.

## Common Money Mistakes

The money is lost in a few recognizable ways.
A budget that does not match the work plan undermines the technical proposal, an
indirect rate set carelessly either prices the company out or starves it, and an
accounting system that is not compliant blocks the cost-reimbursement award the
company won.
Charging unallowable costs invites a disallowance and worse, underestimating the
indirect burden makes a budget that cannot actually do the work, and failing to
plan the cash strands a solvent-on-paper company without the money to make
payroll.
Each of these is the same error in a different place, treating the money as
simpler than the engineering when it is governed by rules just as exacting.

## Scale and the UAV Case

The running example puts numbers to it.
The small company building its [unmanned aircraft][related_post_prototyping] sets
up a compliant accounting system with real timekeeping before it needs one,
computes its fringe, overhead, and general-and-administrative rates, and budgets
its Phase II so that the loaded cost of its small team plus its materials and its
flight-test travel fits under the cap with a reasonable fee on top.
It learns which of its costs are unallowable and keeps them out of the billed
pools, and above all it plans the cash, lining up the financing to carry payroll
across the gap before Phase II and the lag within it.
It treats the budget and the books as seriously as the airframe, because an award
it cannot account for or finance is an award it cannot keep.

## Out of Scope

Several matters belong to specialists or other articles.
The detailed cost principles, the mechanics of a rate negotiation, and the
conduct of an audit are matters for an accountant and for the regulations rather
than for this overview, and the precise fee limits and rate structures change and
must be read from the current rules.
The reporting and the audits that follow an award are the subject of the
compliance article, the financing strategy is developed in the strategy article,
and tax is outside this scope entirely.
Nothing here is accounting, financial, or tax advice.

## Conclusion

The money behind an award is where the technical plan meets the dollars, and it
turns on three things, a compliant cost proposal that fits the work into the cap,
an indirect rate that decides how much of the award reaches the work, and a cash
plan that carries the company from spending to reimbursement.
The company that masters them earns a margin, keeps its overhead funded, and
stays solvent through the lags and the gaps, while the company that neglects them
can win an award and still fail, blocked by an inadequate system or stranded
without the cash to use the money it won.
The money is governed by rules as exacting as the engineering, and a company
built on funded research learns them as a core discipline rather than leaving
them to chance.

## References

- [Reference, Burn Rate][ref_burn_rate]
- [Reference, Cash Flow][ref_cash_flow]
- [Reference, Cost Accounting][ref_cost_accounting]
- [Reference, Cost-Plus Contract][ref_cost_plus]
- [Reference, Defense Contract Audit Agency][ref_dcaa]
- [Reference, Employee Benefits][ref_fringe]
- [Reference, Federal Acquisition Regulation][ref_far]
- [Reference, Fixed-Price Contract][ref_fixed_price]
- [Reference, Indirect Costs][ref_indirect]
- [Reference, Line of Credit][ref_line_of_credit]
- [Reference, Overhead in Business][ref_overhead]
- [Related Post, Phase II and the Commercialization Plan for SBIR and STTR][related_post_phase_two]
- [Related Post, Phase III and the Valley of Death for SBIR and STTR][related_post_phase_three]
- [Related Post, Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass][related_post_prototyping]
- [Related Post, Writing the Phase I SBIR and STTR Proposal][related_post_phase_one]
- [Research, NIH Grants and Funding][research_nih]
- [Research, SBIR and STTR (the official program portal)][research_sbir_gov]
- [Research, The Defense SBIR and STTR Innovation Portal][research_dod]

[ref_burn_rate]: https://en.wikipedia.org/wiki/Burn_rate
[ref_cash_flow]: https://en.wikipedia.org/wiki/Cash_flow
[ref_cost_accounting]: https://en.wikipedia.org/wiki/Cost_accounting
[ref_cost_plus]: https://en.wikipedia.org/wiki/Cost-plus_contract
[ref_dcaa]: https://en.wikipedia.org/wiki/Defense_Contract_Audit_Agency
[ref_fringe]: https://en.wikipedia.org/wiki/Employee_benefits
[ref_far]: https://en.wikipedia.org/wiki/Federal_Acquisition_Regulation
[ref_fixed_price]: https://en.wikipedia.org/wiki/Fixed-price_contract
[ref_indirect]: https://en.wikipedia.org/wiki/Indirect_costs
[ref_line_of_credit]: https://en.wikipedia.org/wiki/Line_of_credit
[ref_overhead]: https://en.wikipedia.org/wiki/Overhead_(business)
[related_post_phase_two]: {% post_url 2026-06-20-phase_ii_and_the_commercialization_plan_for_sbir_and_sttr %}
[related_post_phase_three]: {% post_url 2026-06-21-phase_iii_and_the_valley_of_death_for_sbir_and_sttr %}
[related_post_prototyping]: {% post_url 2026-05-30-prototyping_fixed_wing_aircraft_with_lightweight_pla_and_fiberglass %}
[related_post_phase_one]: {% post_url 2026-06-19-writing_the_phase_i_proposal_for_sbir_and_sttr %}
[research_nih]: https://grants.nih.gov/
[research_sbir_gov]: https://www.sbir.gov/
[research_dod]: https://www.dodsbirsttr.mil/
