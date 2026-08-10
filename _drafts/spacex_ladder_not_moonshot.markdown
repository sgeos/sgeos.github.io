---
layout: post
mathjax: true
comments: true
title: "Why SpaceX Built a Ladder Instead of a Moonshot"
date: 2026-08-06 09:00:00 +0000
categories: business history aerospace
---

<!-- A369 -->
<script>console.log("A369");</script>

On 21 October 1993 the United States Congress cancelled the [Superconducting Super Collider][ref_ssc_wiki].
About two billion dollars had been spent. Fourteen miles of tunnel had been bored under Waxahachie, Texas.
**Nothing else existed.** There was no smaller collider that worked, no instrument anyone could use, no
result anyone could publish. The programme had been designed to produce exactly one thing, and it was
cancelled about a fifth of the way to producing it.

Nine years later a company was founded that would spend the next two decades doing something close to the
opposite. **Every vehicle SpaceX built was sold to somebody before the next one was designed.**

This article is about that difference. It is a rewritten and retargeted version of a more technical
treatment in the [History of SpaceX series][related_post_a285_spacex_decomposability], aimed at a reader who
has no particular interest in launch vehicles but a considerable interest in
**why some ambitious projects survive and others evaporate.**

**The argument is not that SpaceX is clever.** It is that a particular way of arranging a long project
changes its odds enormously, that the arrangement is describable in arithmetic a reader can check, and that
**it has real costs which are usually left out of the telling.**

## The Idea in One Paragraph

Suppose you want to build something that will take twenty years. You have two ways to arrange the work.

**You can build it as one thing.** Design the finished article, break the work into stages, and execute the
stages. Nothing is useful until the last stage is done. This is how the Super Collider was arranged, how
[ITER][ref_iter_organization] is arranged, and how most large public science projects are arranged.

**Or you can build it as a ladder.** Design a sequence of intermediate versions, each of which is useful and
saleable on its own, and each of which teaches you something you need for the next. The finished article is
the top rung. **If you never reach it, you still have the rungs.**

That is the whole idea, and it is old.
**The formal version goes back to [Simon's Architecture of Complexity][research_simon_1962] in 1962**, which
argued that complex systems that survive are almost always built from stable intermediate forms, and that
this is true of biological evolution, social organisation and engineering alike. The design-theory version
is [Alexander][book_alexander_1964] and, more directly, [Baldwin and Clark on
modularity][book_baldwin_clark_2000], which treats the ability to develop and value parts independently as
the central property of a design.

The software version is [Boehm's spiral model][research_boehm_1988], the manufacturing version is the
product-platform literature of [Meyer and Lehnerd][book_meyer_lehnerd_1997] and [Sanderson and
Uzumeri][book_sanderson_uzumeri_1997], and the finance version is real options, in
[Trigeorgis][book_trigeorgis_1996] and [Dixit and Pindyck][book_dixit_pindyck_1994], where the right to stop
is itself worth money.

**Four fields discovered the same thing and gave it four names.** What follows is why it matters more than
it sounds like it should.

## Why the Arrangement Matters More Than the Odds

**The surprising part is that a ladder does not need better luck than a monolith. It needs the same luck, arranged differently.**

Suppose a project has eight stages and each stage succeeds with probability $p$. If the project only
delivers when every stage succeeds, then

$$P(\text{deliver}) = p^{N}$$

At $p = 0.9$, which is a generous assumption for any twenty-year technical programme,

$$P(\text{deliver}) = 0.9^{8} = 0.43$$

**So a programme in which every individual stage is ninety percent likely to work is more likely than not to deliver nothing at all.**
That is not a statement about incompetence. It is what multiplying eight numbers slightly below one does.

Now arrange the same eight stages as a ladder, where reaching rung $k$ means rungs one through $k$ are each
independently useful. The expected number of rungs completed is

$$E[\text{rungs}] = \sum_{k=1}^{N} p^{k}$$

$$E[\text{rungs}] = 0.9 + 0.81 + \dots + 0.9^{8} = 5.13$$

**Five of the eight rungs, in expectation, from exactly the same per-stage odds.**

| Per-stage odds | Monolith delivers everything | Ladder delivers, on average | Ladder delivers something |
|---|---|---|---|
| 0.95 | 66 percent of the time | 80 percent of the value | 95 percent of the time |
| 0.90 | 43 percent | 64 percent | 90 percent |
| 0.80 | 17 percent | 42 percent | 80 percent |
| 0.70 | 6 percent | 27 percent | 70 percent |

**The gap widens as the odds get worse**, which is the opposite of comforting, because long technical
programmes are exactly where per-stage odds are worst.

## The Shape of the Risk, Not Just Its Size

Averages hide the more important difference.
**The monolith's outcome is binary and the ladder's is graded.**

At $p = 0.9$ and eight stages, the monolith produces everything with probability 0.43 and nothing with
probability 0.57. There is no middle. The ladder's outcomes spread across the whole range, with a 43 percent
chance of finishing and only a 10 percent chance of producing nothing at all.

**This matters because of who is watching.** A programme that has delivered three of eight rungs has
customers, revenue, employed engineers and a track record, and cancelling it takes something away from
someone. A programme that has delivered fourteen miles of tunnel has a hole.
**The ladder is not only more likely to produce value, it is much harder to kill**, and those two properties
reinforce each other.

**In the language of real options this is the value of the right to abandon**, which [Copeland and
Antikarov][book_copeland_antikarov_2001] treat at length. A monolithic programme has that right in a legal
sense and cannot exercise it usefully, because abandoning it yields nothing.
**A ladder can be abandoned at a profit**, and an arrangement that can be stopped without loss is one that
is easier to start.

**That is the mechanism the Super Collider lacked**, and it is worth being precise about what killed it. It
was not that the physics was wrong or the engineering impossible. It was that at the moment somebody asked
what had been bought for two billion dollars, **the honest answer was a hole in Texas and a promise.**

## The Ladder SpaceX Actually Climbed

The history is more interesting than the abstraction, and it is well documented in [Berger's
Liftoff][book_berger_2021] on the early years, [Berger's Reentry][book_berger_2024] on what came after, and
the biographical treatments by [Vance][book_vance_2015] and [Isaacson][book_isaacson_2023].

The engineering background, for a reader who wants it, is [Sutton and Biblarz on rocket
propulsion][book_sutton_biblarz_2010], [Huzel and Huang on engine design][book_huzel_huang_1992], and [Wertz
and Larson on space mission analysis][book_wertz_larson_1999].

**Falcon 1, 2002 to 2009.** A small two-stage rocket carrying about 670 kilogrammes to orbit, with one
engine on the first stage. It flew five times. **Three of those flights failed.** It never made much money.
What it produced was an engine that worked, a company that knew how to run a launch site, and a
demonstration that the thing could be done at all.

**Falcon 9, from 2005.** The same kerosene and liquid oxygen, the same engine,
**nine of them instead of one**, carrying about 10,450 kilogrammes. It first flew on 4 June 2010 and has
been through four major configurations since. This is the rung that pays for everything else.

**Dragon 1, 2006 to 2020.** A cargo spacecraft, built under a [NASA Commercial Orbital Transportation
Services agreement][ref_nasa_cots] signed on 18 August 2006. It is the clearest example of a rung that paid,
and the arithmetic is worth stating plainly.

$$\frac{\text{revenue}}{\text{development cost}} = \frac{\$3.04 \text{ billion}}{\$300 \text{ million}} \approx 10$$

**Roughly ten dollars of contracted revenue for every dollar of development.** That is not a typical outcome
and it should not be presented as one, but it illustrates what a rung is for. Dragon 1 was built as a step
toward carrying people, and it paid for itself many times over before it ever did.

**Falcon Heavy, from 2011.** Three Falcon 9 first stages bolted together.
**Twenty-seven engines, all of them the engine Falcon 1 needed one of.**

**Dragon 2, from 2014.** The crew version, which is what Dragon 1 was a step toward.

**Starship and Super Heavy, from 2016.** The top of the ladder as currently drawn, and the only rung whose
independent value is still an open question rather than a matter of record.

## The Part of the Story the Vehicle List Misses

**The ladder is usually told as a sequence of vehicles, and the most interesting version of it happens one level down, in the engines.**

Falcon 1 used one Merlin engine. Falcon 9 uses nine. Falcon Heavy uses twenty-seven.
**Every vehicle in the family pays into the same production line**, which means the engine gets cheaper for
reasons that have nothing to do with any particular vehicle succeeding.

The relevant relation is the learning curve, sometimes called Wright's law, which is one of the more
reliable empirical regularities in manufacturing. It is treated at length in [Argote][book_argote_1999] and
in the organisational-learning literature that follows it, including [Argote and Ingram on knowledge
transfer][research_argote_ingram_2000] and [the later review][research_argote_miron_spektor_2011].
**Its origins are in mass production rather than in aerospace**, and [Hounshell's history of the American
system][book_hounshell_1984] is where the mechanism was first documented at scale. Unit cost falls by a
fixed fraction for every **doubling** of cumulative production,

$$C(n) = C(1) \, n^{\log_2 b}$$

where $b$ is the learning rate. A rate of $b = 0.85$ means each doubling costs fifteen percent less.

Now compare two designs that build the same number of airframes, one using a single large engine and one
using nine small ones. The nine-engine design has nine times the cumulative engine production, and

$$\frac{C_9}{C_1} = 9^{\log_2 b} = 9^{-0.2345} = 0.60$$

**A forty percent lower unit engine cost, on the same number of airframes.**

**The elegant part is that this ratio does not depend on how many airframes are built.** Nine times the
units is a fixed 3.17 extra doublings whether the fleet is ten aircraft or three hundred, so the advantage
appears immediately and never erodes.

| Learning rate | Unit cost advantage of nine engines over one |
|---|---|
| 0.80 | 51 percent lower |
| 0.85 | 40 percent lower |
| 0.90 | 28 percent lower |
| 0.95 | 15 percent lower |

**This is what the product-platform literature calls commonality**, and [Meyer and
Lehnerd][book_meyer_lehnerd_1997] make the same argument for consumer products that this section makes for
engines. The modularity research puts it more formally still, in [Baldwin and
Woodard][research_baldwin_woodard_2009] and in [Ethiraj and Levinthal on the limits of modular
design][research_ethiraj_levinthal_2004], which is worth reading alongside because it argues that modularity
can be taken too far.

**This is the ladder operating on a component rather than on a vehicle**, and it is invisible in any telling
that lists the rockets in order. It is also the strongest argument in the whole story, because unlike the
vehicle sequence it does not depend on commercial judgement or good fortune.
**It is arithmetic about how many times you have built the thing.**

## What the Ladder Costs

**An article that only lists the advantages of an arrangement is an advertisement.** The ladder has three
real costs and the third is the interesting one.

**It is slower to the top.** Every intermediate version has to be finished, qualified, sold and supported,
and none of that effort points at the final capability. A monolithic programme spends all of its effort on
the thing it is trying to build. **If it succeeds, it gets there first.**

**It constrains what you can build.** A rung has to be saleable now, which means the architecture must admit
useful intermediate forms. Some designs do not.
**If the only valuable version of a thing is the finished version, there is no ladder to climb**, and
insisting on one produces a worse design rather than a safer project. This is a real limit and it is where
the pattern stops being general advice.

**It can strand you on a profitable rung.** This is the subtle one.
**A rung that pays well is a reason not to climb**, and the better it pays the stronger the reason. The
organisation acquires customers who want the current product, staff whose expertise is the current product,
and a revenue line that a board is reluctant to disturb.

**That is the same mechanism that makes successful firms slow to replace their own products**, treated at
length in [Christensen][book_christensen_1997], extended in [Christensen and
Raynor][book_christensen_raynor_2003], and grounded in the evolutionary account of the firm in [Nelson and
Winter][book_nelson_winter_1982] and the older resource argument in [Penrose][book_penrose_1959]. The
industry-lifecycle version, where the profitable configuration crowds out the next one, is
[Utterback][book_utterback_1994] and [Klepper][research_klepper_1996]. The ladder does not remove it.
**The ladder creates it.** A programme with no intermediate revenue has nothing to protect and therefore
nothing to be distracted by, which is the one genuine advantage the monolithic arrangement has.

## Three Projects That Did Not Have Rungs

**The Superconducting Super Collider** is the cleanest case, and its history is treated in [Riordan,
Hoddeson and Kolb][book_riordan_hoddeson_kolb_2015]. Cancelled 21 October 1993 after roughly two billion
dollars of an estimated ten billion, or about a fifth of the way. **There was no partial collider.** The
design did not admit one, because a collider's energy is set by its circumference and half a ring is not a
small ring.

**That last point deserves emphasis, because it is a defence of the programme rather than an indictment.**
The SSC could not have been built as a ladder. The physics forbade it.
**Which means the lesson is not that its managers chose badly, but that some projects genuinely do not decompose**,
and those projects need a different kind of political protection than a ladder provides.

**Apollo is the instructive near-miss and belongs here rather than among the successes.** It was arranged as
a ladder of sorts, with Mercury and Gemini preceding it, and [Logsdon on the decision][book_logsdon_1970],
[Bilstein on the Saturn vehicles][book_bilstein_1980] and [Heppenheimer on what came
after][book_heppenheimer_1999] together show what happened next.
**The rungs were technical rather than commercial**, so when the political demand ended there was no
customer to keep paying, and the capability was dismantled.
**A rung that only an internal sponsor values is a rung that vanishes when the sponsor does.**

**Iridium** filed for bankruptcy on 13 August 1999, with the business history covered in the [contemporary
press][ref_bloomberg] and the vertical-integration analysis in [Fine's Clockspeed][book_fine_1998]. The
satellite constellation had to be almost entirely in place before it could offer service at all, so the
capital went in years before any revenue could come out, and the market it eventually met was not the market
it had been designed for. **A constellation is a monolith made of many small pieces**, which is a useful
reminder that a ladder is about independent value rather than about being built in parts.

**ITER** is the ongoing case, treated in the [organisation's own programme reports][ref_iter_organization].
A single machine, decades of construction, no intermediate configuration that produces power.
**It may well work.** The point is not that it will fail but that it has spent decades with nothing to point
at except progress toward something, which is precisely the position from which the Super Collider was
cancelled.

## Where This Is the Wrong Idea

**The pattern is not general advice and treating it as such would be a mistake.**

**Some things do not decompose.** A collider, a bridge, a tunnel and a fusion reactor are each worthless at
ninety percent. Where the physics or the geometry forbids a useful intermediate, the ladder is not available
at any price, and the correct response is to argue for the monolith honestly rather than to pretend a ladder
exists.

**Some ladders are illusions.** An intermediate version that is technically buildable but that nobody will
buy is not a rung. It is a delay with extra steps.
**The market-progression literature is unusually useful here**, since [Rogers on
diffusion][book_rogers_1962] and [Moore's Crossing the Chasm][book_moore_1991] are both about the gap
between a product existing and a product selling, which is exactly where an imagined rung fails.
**The test is whether somebody outside the organisation pays for it**, and that test is much harder to pass
than an internal milestone review.

**The argument is about arrangement, not about ambition.** Nothing here says a project should be less
ambitious. The Super Collider and Starship are comparably ambitious.
**They differ in whether anything is worth having before the end.**

**And the sample is one.** This article draws its positive example from a single company in a single
industry over two decades, which is not evidence that the arrangement generalises. The arithmetic
generalises.
**Whether the arithmetic describes your situation is a separate question the arithmetic cannot answer.**

## Epistemic State

**Historical fact, from the public record.** The Superconducting Super Collider was cancelled on 21 October
1993 after approximately two billion dollars had been spent against an estimate exceeding ten billion, with
roughly fourteen miles of tunnel bored. Iridium filed for bankruptcy protection on 13 August 1999. SpaceX
was founded in March 2002. Falcon 1 flew five times between 2006 and 2009, of which the first three failed.
The NASA Commercial Orbital Transportation Services agreement was signed on 18 August 2006. Falcon 9 first
flew on 4 June 2010. Dragon 1 flew from 2010 to 2020.

**Arithmetic, derived here and checkable.** The compounding-risk comparison, the expected-rungs sum, and the
learning-curve ratio are all elementary and are computed in the article rather than asserted.
**The result that the nine-engine cost advantage is independent of fleet size follows from the logarithm and is exact within the model.**

**Assumed, and marked as such.** The per-stage success probability of 0.9 and the eight-stage decomposition
are illustrative and are not measurements of any programme. The learning rate of 0.85 is a representative
manufacturing figure, not a measured SpaceX value.
**The Dragon 1 figures of roughly three hundred million dollars of development against roughly 3.04 billion of contracted revenue are approximate, drawn from the source article's reconstruction, and neither is an audited number.**

**Inference, and labelled as such.** That the ladder arrangement made SpaceX harder to cancel is an
inference from the structure and not from any documented decision.
**That the Super Collider could not have been arranged as a ladder is an inference from the physics of colliders**,
and a reader who knows that literature better may reasonably disagree. That the third cost, being stranded
on a profitable rung, applies to SpaceX specifically is **not** claimed here. It is a general property of
the arrangement and no evidence is offered that it has occurred.

**A framing this article deliberately does not adopt.** The mission-oriented-innovation literature,
principally [Mazzucato][book_mazzucato_2013], would read this story as being about public direction of
technology rather than about programme arrangement.
**That reading is compatible with everything here and is not argued for or against**, because the arithmetic
does not distinguish them.

**What this article cannot establish.** Whether the arrangement caused the outcome or merely accompanied it.
A single positive case cannot separate those, and the negation cases are chosen rather than sampled.
**The honest status of the whole argument is that it is a mechanism with arithmetic behind it and one worked example, which is weaker than evidence and stronger than a story.**

## Out of Scope

The engineering of any particular vehicle. Reusability, which is a large and separate argument and is
treated in the [series opener][related_post_a281_spacex_framing]. The launch market and its economics. The
regulatory history. Government procurement mechanics, which the [anchor-demand
article][related_post_a283_spacex_anchor_demand] covers. Comparative assessment of other launch providers.
Anything about the merits of the destinations these vehicles are aimed at.

## Conclusion

**Two billion dollars bought fourteen miles of tunnel and nothing else, because the programme that spent it had been arranged so that nothing existed until everything did.**

The alternative is not a better team or a larger budget. It is an arrangement in which each step is worth
something to somebody before the next one starts.
**The arithmetic says that this changes the expected outcome dramatically without changing the odds of any individual step**,
which is the part that is easy to miss, and that it changes the shape of the risk from all-or-nothing to
graded, which matters more than the average.

**It is not free.** It is slower to the summit, it constrains what can be designed, and it creates the
precise conditions under which an organisation stops climbing because the current rung pays too well.

**And it is not always available.** Some things are worthless at ninety percent, and for those the honest
course is to say so and argue for them on their merits, rather than to invent intermediate deliverables that
nobody wants.

**The question worth carrying away is not whether to be ambitious.** It is whether anything you are building
is worth having before you finish it.

## References

### Book

[book_alexander_1964]: https://www.hup.harvard.edu/books/9780674627512
[book_argote_1999]: https://openlibrary.org/search?q=Argote+Organizational+Learning+Creating+Retaining+Transferring+Knowledge
[book_baldwin_clark_2000]: https://mitpress.mit.edu/9780262024662/design-rules/
[book_berger_2021]: https://williammorrow.com/liftoff-eric-berger/
[book_berger_2024]: https://williammorrow.com/reentry-eric-berger/
[book_bilstein_1980]: https://ntrs.nasa.gov/search?q=Stages+to+Saturn
[book_christensen_1997]: https://www.hbsp.harvard.edu/product/1130-HBK-ENG
[book_christensen_raynor_2003]: https://www.hbsp.harvard.edu/product/3595-HBK-ENG
[book_copeland_antikarov_2001]: https://openlibrary.org/search?q=Copeland+and+Antikarov+Real+Options+A+Practitioners+Guide
[book_dixit_pindyck_1994]: https://openlibrary.org/search?q=Dixit+and+Pindyck+Investment+Under+Uncertainty
[book_fine_1998]: https://www.hachettebookgroup.com/titles/charles-h-fine/clockspeed/9780738201535/
[book_heppenheimer_1999]: https://www.si.edu/object/space-shuttle-decision%3Anmah_1197080
[book_hounshell_1984]: https://jhupbooks.press.jhu.edu/title/american-system-mass-production-1800-1932
[book_huzel_huang_1992]: https://arc.aiaa.org/doi/book/10.2514/4.866197
[book_isaacson_2023]: https://www.simonandschuster.com/books/Elon-Musk/Walter-Isaacson/9781982181284
[book_logsdon_1970]: https://mitpress.mit.edu/9780262620109/the-decision-to-go-to-the-moon/
[book_mazzucato_2013]: https://marianamazzucato.com/books/the-entrepreneurial-state
[book_meyer_lehnerd_1997]: https://www.simonandschuster.com/books/The-Power-of-Product-Platforms/Marc-H-Meyer/9780684825809
[book_moore_1991]: https://www.harpercollins.com/products/crossing-the-chasm-geoffrey-a-moore
[book_nelson_winter_1982]: https://www.hup.harvard.edu/books/9780674272286
[book_penrose_1959]: https://global.oup.com/academic/product/the-theory-of-the-growth-of-the-firm-9780199573844
[book_riordan_hoddeson_kolb_2015]: https://openlibrary.org/search?q=Riordan+Hoddeson+Kolb+Tunnel+Visions
[book_rogers_1962]: https://www.simonandschuster.com/books/Diffusion-of-Innovations-5th-Edition/Everett-M-Rogers/9780743258234
[book_sanderson_uzumeri_1997]: https://openlibrary.org/search?q=Sanderson+and+Uzumeri+Managing+Product+Families
[book_sutton_biblarz_2010]: https://www.wiley.com/en-us/Rocket+Propulsion+Elements%2C+9th+Edition-p-9781118753651
[book_trigeorgis_1996]: https://mitpress.mit.edu/9780262201025/real-options/
[book_utterback_1994]: https://www.hbsp.harvard.edu/product/4855-HBK-ENG
[book_vance_2015]: https://www.harpercollins.com/products/elon-musk-ashlee-vance
[book_wertz_larson_1999]: https://link.springer.com/book/9780792359012

### Reference

[ref_bloomberg]: https://www.bloomberg.com/
[ref_iter_organization]: https://www.iter.org/
[ref_nasa_cots]: https://www.nasa.gov/commercial-orbital-transportation-services-cots/
[ref_ssc_wiki]: https://en.wikipedia.org/wiki/Superconducting_Super_Collider
[research_argote_ingram_2000]: https://www.sciencedirect.com/science/article/abs/pii/S0749597800928930
[research_argote_miron_spektor_2011]: https://pubsonline.informs.org/doi/10.1287/orsc.1100.0621
[research_baldwin_woodard_2009]: https://www.hbs.edu/faculty/Pages/item.aspx?num=32196
[research_boehm_1988]: https://ieeexplore.ieee.org/document/59
[research_ethiraj_levinthal_2004]: https://pubsonline.informs.org/doi/10.1287/mnsc.1030.0145
[research_klepper_1996]: https://www.jstor.org/stable/2118211
[research_simon_1962]: https://www.jstor.org/stable/985254

### Related Post

[related_post_a281_spacex_framing]: {% post_url 2026-07-25-spacex_history_framing %}
[related_post_a283_spacex_anchor_demand]: {% post_url 2026-07-27-spacex_history_anchor_demand %}
[related_post_a285_spacex_decomposability]: {% post_url 2026-07-29-spacex_history_decomposability %}
