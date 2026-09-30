---
layout: post
mathjax: true
comments: true
title: "What Rebuilding Would Take After a War With China"
date: 2026-08-12 09:00:00 +0000
categories: geopolitics military war-gaming
---

<!-- A375 -->
<script>console.log("A375");</script>

The [previous article][related_post_published_wargames]
read the published wargames of a war between the United States and China
and reported what they say about whether such a war is won.
This one takes up the question those games decline to answer.
Every major public wargame stops within about three weeks of the first shot.
The wars they model would not stop there.

The reports say so themselves,
which is the starting point for everything below.
What follows assembles what the published record contains about the aftermath,
covering war termination,
the reconstitution of destroyed forces,
economic reconstruction,
regime survival,
occupation,
recovery from nuclear use,
and the shape of the postwar order.
It also records where the record is empty,
because four of the gaps are large enough to be findings in their own right.

The equations below are arithmetic on published figures.
They check whether the numbers in the reports agree with one another,
and they express the comparisons made here.
None of them is a model of a war or of a recovery.
Readers who want the corpus background may start with the
[account of postwar Japanese and West German reconstruction][related_post_postwar_japan_germany],
which treats the historical cases this article leans on,
and with the
[account of China's rise][related_post_china_rise]
for the industrial base under discussion.

**The finding that organised this article was not the one expected at the outset.**
The expectation was that rebuilding would prove slow.
For buildings and even for industrial capacity the empirical literature says the opposite,
and says it with data.
What does not come back on the same clock is throughput,
specialised production ecosystems,
and trade relationships.
That distinction is the spine of what follows.

## Where the Wargames Stop

### The horizon is stated in the reports

The Center for Strategic and International Studies,
or CSIS,
ran its invasion game 24 times.
[Cancian, Cancian and Heginbotham 2023][research_cancian_2023_first_battle]
record the horizon plainly.
The games "lasted an average of six turns",
which the report gives as 21 days of campaign time,
and "getting to final resolution would require many additional weeks of combat.
In the case of stalemate, the war might have continued for many months".
The report adds that "escalation decisions were not part of the game".
Each turn represents three and a half days,
so the horizon is a product of two stated quantities.

$$
6 \ \text{turns} \times 3.5 \ \text{days per turn} = 21 \ \text{days}
$$

Writing $T_g$ for the modelled horizon and $T_w$ for the war the same report describes,
the relation is an inequality the authors assert rather than a quantity they measure.

$$
T_g \approx 21 \ \text{days},
\qquad
T_w \gg T_g
$$

[Gompert, Cevallos and Garafola 2016][research_gompert_2016_war_with_china]
at the RAND Corporation reach the termination question directly
and find no mechanism that closes it.
Both sides have "considerable, if asymmetric, capacity to prolong a conflict
that neither one is militarily compelled or politically ready to end",
and "History offers no encouragement
that destructive but stalemated fighting induces belligerents to agree to stop".

[Predd and others 2025][research_predd_2025_protracted_war],
sponsored by the Office of Net Assessment,
exists because the planning baseline assumes otherwise.
Their finding is that "Neither China nor the United States
possesses overwhelming conventional military power
or significant economic overmatch that would ensure rapid victory",
and that the opening phase could set the stage for protraction.

The CSIS report names the same problem in its own risk list,
which is worth quoting because it undercuts the use most readers make of it.
The war "might not end after this initial phase but drag on for months or even years",
conflict "might be episodic, with periodic ceasefires",
and then the authors say the quiet part.
"This project is called The First Battle of the Next War for a reason.
Opening battles, even if seemingly decisive, generally do not end a conflict."
Its casualty figures carry the matching caveat,
that they "do not encompass the full scope of the war"
and that the "numbers presented here represent a floor, not a ceiling".

**The intelligence community states the protraction risk in its own voice,
which is worth recording because it is the official judgment
against which the three-week games should be read.**
The [Office of the Director of National Intelligence 2026][government_odni_2026_threat_assessment]
annual threat assessment holds that
"a protracted war with the U.S. risks unprecedented economic costs
to the U.S., Chinese, and global economies".
It judges that Chinese officials themselves
"recognize that an amphibious invasion of Taiwan would be extremely
challenging and carry a high risk of failure,
especially in the event of U.S. intervention",
and that Chinese leaders "do not currently plan to execute an invasion of Taiwan
in 2027, nor do they have a fixed timeline for achieving unification".
The same document expects disruption to the United States transportation sector
from Chinese cyber attack to be "significant but recoverable",
a word chosen carefully and applied to one sector only.

[Tetreau 2023][commentary_tetreau_2023_where_the_wargames_were_not]
surveyed ten assessments from the preceding decade
and named conflict termination as one of the principal gaps,
noting that "few consider the conditions under which a conflict might be de-escalated".
[Heath 2023][commentary_heath_2023_wargames_deterrence]
argues that combat wargames should not be repurposed
to answer questions about deterrence, escalation or termination at all.

A note on citation hygiene belongs here,
because it bears on every number below.
Heath attributes 22 iterations to the CSIS game.
The CSIS report states 24,
which was checked in the report text for this article.
The discrepancy is small and it is the kind that propagates,
so both figures are reported with their sources named.
The gap is one twelfth of the count.

$$
\frac{24 - 22}{24} \approx 0.083
$$

### The single paragraph on rebuilding

The CSIS report does address reconstitution,
in one passage,
and that passage is the most consequential thing in the public record about the aftermath.

> With only two U.S. shipyards currently building large surface combatants,
> it would take decades to replace the dozen or more such ships lost
> while continuing the Navy's build program.
> Lost carriers could not be replaced
> because the current shipyard capacity is sufficient only to maintain the current carrier force.
> Aircraft would be a bit easier to replace.
> For example, the United States lost an average of 200 to 500 aircraft across the scenarios.
> At current procurement rates of about 120 such aircraft per year,
> it would take two to four years to replace those aircraft,
> assuming no further attrition and no retirement of aging aircraft in the force.

The report then states the bound on its own estimate.
Ships and aircraft "would take longer to replace
if the war went beyond the three or four weeks of game play
or if losses from engagements in the South China Sea were calculated and included".

## Reconstitution Is Bounded by Throughput

### Aircraft, which is the easy case

Take $L$ as the number of aircraft lost
and $\dot{q}$ as the annual procurement rate.
Replacement time is the quotient.

$$
T = \frac{L}{\dot{q}}
$$

With the report's own figures the bracket follows.

$$
\frac{200}{120} \approx 1.7 \ \text{years},
\qquad
\frac{500}{120} \approx 4.2 \ \text{years}
$$

That reproduces the published two to four years,
which is a check on the arithmetic and not an independent finding.
The assumptions the report attaches are doing real work,
since it stipulates no further attrition and no retirements,
and both are false in any war that lasts longer than the game.

For scale on the other side,
[Gunzinger and Penney 2026][research_gunzinger_2026_rebuilding_air_force]
at the Mitchell Institute estimate People's Liberation Army Air Force procurement
at over 250 combat aircraft per year through 2027.

$$
\frac{250}{120} \approx 2.1
$$

The replacement rate available to one side is about twice that available to the other,
before any account of who lost more.

### Surface combatants and carriers, which are not the easy case

**The constraint here is not money but yards,
and the Navy has now said so itself in the plainest terms in this article.**
The [Navy's shipbuilding plan for fiscal year 2027][government_navy_2026_shipbuilding_plan],
submitted under section 231 of title 10 of the United States Code,
opens by stating that the department
"currently operates 291 battle force ships,
while the Navy requirement by law is 355",
and then supplies the sentence that settles the money question.
"Over the past two decades, the shipbuilding budget has doubled,
yet we have no more ships now than in 2003."
The plan calls the problem "structural" rather than merely industrial,
observes that "Many shipbuilders are using 1960's technology
with 1980's manufacturing processes",
and concedes that its own projections
"assume industry increases manufacturing capacity
and produces future ships on time and within budget".
A doubled budget that bought no additional fleet in twenty years
is the throughput constraint stated by the organisation that holds the money.

[Labs 2025][research_labs_2025_cbo_shipbuilding]
at the Congressional Budget Office records that essentially all Navy battle force ships
are built by seven shipyards,
that destroyers and submarines took five to six years to build in the 2000s
and now take eight to nine years on average,
and that a new submarine takes about nine years.
The [Government Accountability Office 2022][research_gao_2022_industrial_base]
gives the history behind that count,
reporting that capacity and competition in shipbuilding
"declined significantly over the past 50 years,
with 14 shipyards that built Navy ships closing".
Three more left the defence industry and one opened,
"leaving only seven shipyards owned by four prime contractors".
Seven yards under four owners is a narrower market than seven yards alone implies.
Taking the midpoints of the two brackets,
build duration has lengthened by half again within a generation.

$$
\frac{8.5}{5.5} \approx 1.55
$$

The CSIS passage names two yards for large surface combatants
and puts the loss at a dozen or more.
**That two is independently confirmed by the Department of Defense,
which counted the same collapse market by market.**
The competition report's table of prime contractors by weapons category
gives surface ships as 8 in 1990, 5 in 1998 and 2 in 2020,
and names the two survivors as General Dynamics and Huntington Ingalls.
The same table records missiles and munitions
going from 30 prime contractors three decades ago to seven.

$$
\frac{8}{2} = 4,
\qquad
\frac{30}{7} \approx 4.3
$$

Two independent sectors lost about three quarters of their prime contractors,
which is the pattern rather than a shipbuilding peculiarity.

Writing $n$ for the number of building yards,
$B$ for the build duration
and $L$ for hulls lost,
a first-order replacement time under serial construction is as follows.

$$
T \approx \frac{L}{n} \times \frac{B}{k}
$$

Here $k$ is the number of hulls a yard carries concurrently,
which the public sources do not state,
so the expression is a shape rather than a calculation.
Working it at the low end of the loss and the midpoint of the build
shows why the shape matters more than the precision.

$$
\frac{12}{2} \times \frac{8.5}{1} = 51 \ \text{years},
\qquad
\frac{12}{2} \times \frac{8.5}{2} \approx 26 \ \text{years}
$$

Even two hulls at a time in each of two yards,
which is generous against the delivery record below,
leaves a quarter century.
What the sources do support is the direction.
With 12 to 20 hulls lost,
two yards,
and an eight to nine year build,
"decades" is arithmetic rather than rhetoric,
and the report reaches that word by the same route.

For carriers the quantity is not long but undefined.
The report states that capacity "is sufficient only to maintain the current carrier force",
which means the replacement rate net of programmed construction is zero.

$$
\dot{q}_{\text{net}} = 0
\quad \Rightarrow \quad
T = \frac{L}{\dot{q}_{\text{net}}} \ \text{is undefined}
$$

A quantity that does not exist is a different kind of finding from a long one.
Two carriers were lost in every base iteration of the game.

### Submarines, where the gap is already open in peacetime

[O'Rourke 2026][research_orourke_2026_virginia_class]
at the Congressional Research Service records that the Virginia class
has been procured at about two boats per year since 2011,
that the actual production rate "has never reached 2.0 boats per year",
and that since 2022 it has run about 1.1 to 1.2 per year.
The Navy is working toward 2.0 and subsequently 2.33 per year.

$$
\frac{2.33}{1.2} \approx 1.9
$$

Reaching the planned rate requires almost doubling output before any wartime loss is replaced.
Stated as an annual shortfall against the target rate,
the gap is more than a boat a year.

$$
2.33 - 1.2 = 1.13 \ \text{boats per year}
$$

[Oakley 2026][research_oakley_2026_gao_shipbuilding]
at the Government Accountability Office reports that two boats were delivered in 2025
and both were over three years late.

### Munitions, where the cycle is the whole story

[Cancian and Park 2026][research_cancian_2026_last_rounds]
state the production cycle in full.
Manufacturing lead time for a first delivery "has historically been about 24 months",
has stretched "to 36 months or more",
and lot production takes "another 12 months",
giving "about 52 months in all, over four years".

Their worked example for the Joint Air-to-Surface Standoff Missile,
or JASSM,
decomposes it.
Six months of administrative lead time,
36 months to first delivery,
and 11 months to complete the lot.

$$
6 + 36 + 11 = 53 \ \text{months} \approx 4.4 \ \text{years}
$$

The two figures agree,
which is what a consistency check is for.

The scale problem is separate from the cycle problem.
[Cancian and Park 2026][research_cancian_2026_missile_rebuild]
record Tomahawk procurement averaging 86 missiles a year over ten fiscal years
against a stated manufacturer capacity goal above 1,000 a year
and recent annual production below 200.
For the Patriot interceptor the baseline is about 650 a year
with a surge rate of 2,000,
against United States procurement averaging 225 a year over the past decade.

$$
\frac{2{,}000}{225} \approx 8.9
$$

Reaching the surge rate is close to a ninefold step up from the decade average,
and the surge rate is the one that exists on paper today.
Measured instead against the current baseline rather than the procurement average,
the step is smaller and still large.

$$
\frac{2{,}000}{650} \approx 3.1
$$

For the Tomahawk the same comparison uses expenditure against production.
More than 1,000 were expended and recent annual production is below 200.

$$
\frac{1{,}000}{200} = 5 \ \text{years}
$$

That is the replacement time at the recent rate,
before the four-year cycle above is added to it.

The Taiwan-specific version of the shortfall is older and sharper.
[Jones 2023][research_jones_2023_empty_bins]
reports that across nearly two dozen iterations of the CSIS game
the United States expended more than 5,000 long-range missiles in three weeks,
and that in every iteration it expended its entire inventory
of Long Range Anti-Ship Missiles within the first week.
[Cancian and Park 2026][research_cancian_2026_six_reasons]
note that those same anti-ship munitions were barely touched in the 2026 air campaign against Iran,
so their inventories are intact,
and that they "would rapidly dwindle in a war against a near-peer naval power".

The structural cause is consolidation,
and the Department of Defense has measured it in its own words.
The [State of Competition within the Defense Industrial Base][government_dod_2022_competition]
report finds that "Since the 1990s, the defense sector has consolidated substantially,
transitioning from 51 to 5 aerospace and defense prime contractors",
and dates the change precisely,
with "the total number of U.S.-based prime contractors declining from 51 in 1993 to 5 in 2000".
The five it names are Lockheed Martin, Raytheon, General Dynamics,
Northrop Grumman and Boeing.
The report is also clear that the trend did not stop,
having "continued in the last five years,
due to vertical and horizontal integrations
and the entry of private equity firms performing roll ups".
**The 1993 meeting that is conventionally called the Last Supper
appears nowhere in the report**,
so the figures are cited here from the department
and the nickname is left to the secondary literature that uses it.
The department is also not the origin of the figure,
since both of its footnotes on the point
cite the final report of the Commission on the Future of the United States Aerospace Industry
of November 2002.
That commission report was not retrieved for this article,
so the chain is recorded at one remove
rather than presented as though the earliest source had been read.

An older independent measurement agrees on the direction.
The [General Accounting Office 1998][research_gao_1998_defense_consolidation]
reported that the defence industry
"is now more concentrated than at any time in more than half a century",
and that "the number of contractors producing tactical missiles has dropped from 13 to 4".
Its table gives surface ships falling from 8 to 5 between 1990 and 1998,
which matches the department's later figure for 1998,
while its tactical missile count of 4 for that year
sits against the department's 3.
The small disagreement is left visible rather than reconciled,
because two agencies counting the same market differently
is information about the difficulty of the count.
[Rumbaugh 2026][research_rumbaugh_2026_solid_rocket_motors]
records the same pattern in solid rocket motors,
where the domestic supplier base shrank from six to two between 2000 and 2015.
Both consolidations are large multiples rather than trims.

$$
\frac{51}{5} \approx 10.2,
\qquad
\frac{6}{2} = 3
$$

A base that has contracted by a factor of ten
is the reason surge capacity has to be bought in advance rather than found in a crisis.

### The workforce, which is the constraint behind the others

[Government Accountability Office 2025][research_gao_2025_shipbuilding_workforce]
reports that over the next decade the shipbuilding industrial base
"will require 174,000 new workers to keep pace with Navy shipbuilding goals",
and that all seven shipbuilders face workforce limitations.

$$
\frac{174{,}000}{10} = 17{,}400 \ \text{workers per year}
$$

**That requirement is larger than the workforce that exists.**
The Section 301 report cited above,
drawing on a Maritime Administration fact sheet,
records that in 2023 the United States shipbuilding industry
directly employed 105,652 people.

$$
\frac{174{,}000}{105{,}652} \approx 1.65
$$

The two figures measure different things and are reported together for that reason.
The 174,000 is new workers the Government Accountability Office says are needed
over a decade to meet Navy shipbuilding goals,
which includes replacing those who leave,
while the 105,652 is total employment across private shipbuilding and repair,
naval and commercial work together.
Set side by side they say that the decade's hiring target
exceeds the entire present headcount by about two thirds.
The Congressional Budget Office notes that employment
in the shipbuilding and boatbuilding industry has not grown since 1990.
A hiring requirement of that size against a flat sector
is the reason the yard count cannot simply be raised when needed.
The same office records that for some ships,
including submarines,
approximately 70 percent of the suppliers of critical components have no competitors.

### The general case, and the number that bounds it

[Cancian and others 2021][research_cancian_2021_industrial_mobilization]
measured replacement time across major acquisition programmes
using procurement justification exhibits from 1999, 2008 and 2020.
Replacing programme inventories at surge rates would take an average of 8.4 years,
against 13.8 years at peacetime efficiency rates.

$$
\frac{13.8}{8.4} \approx 1.64
$$

Surging buys a factor of about 1.6,
not a factor of ten.
Set the surge figure against the horizon the wargames actually model,
and the mismatch between the two literatures becomes a single number.

$$
\frac{8.4 \times 365}{21} \approx 146
$$

The replacement clock runs about a hundred and fifty times longer than the clock the games run on.
Navy shipbuilding has the longest replacement times of all categories,
and the industrial base has become more brittle over time,
since replacement takes longer at 2020 rates than at 1999 rates.

**The caveat on those two numbers is as important as the numbers.**
The authors state that the calculations "do not directly assess the wartime problem,
replacing equipment losses in combat",
that such losses "are likely to be quite large" in the authors' words,
and that the replacement times would be "even more demanding".
Anyone quoting 8.4 years as a loss-replacement estimate is misreading it,
and this article does not.

The same report closes the mobilisation analogy that usually gets invoked here.
"Future wars are unlikely to have the long strategic warning
that the United States had before World War II.
Existing industrial mobilization capabilities are all that will likely be available."
Even with that warning,
"it was late 1943 to early 1944
before U.S. forces were large enough and sufficiently equipped
to take on the main elements of the Axis armed forces".

### The asymmetry, and what the widely quoted ratio is worth

The figure that circulates is that Chinese shipbuilding capacity
is roughly 200 times that of the United States.
Its origin is an Office of Naval Intelligence slide
reported by [The War Zone in 2023][commentary_twz_2023_oni_slide],
showing about 23,250,000 tons of Chinese capacity
against under 100,000 tons for the United States.

$$
\frac{23{,}250{,}000}{100{,}000} \approx 232
$$

The Navy confirmed the slide's authenticity and simultaneously limited it,
stating that it was "developed by the Office of Naval Intelligence from multiple public sources
as part of an overall brief on strategic competition"
and was "not intended as a deep-dive into the PRC commercial shipbuilding industry".
The reporter noted that it is unclear how much commercial capacity
the United States figure incorporates.

**A search of the public record found no released Office of Naval Intelligence document
that states Chinese shipbuilding capacity or tonnage.**
The office's own China page lists four public items,
a 2015 publication on the People's Liberation Army Navy,
two videos and a 2022 recognition poster,
and the 2015 publication contains no such figure.
The widely quoted ratio therefore has no public primary behind it at all.
This is a statement about the public record and not about the slide,
which may well be authentic,
and the office produces classified material that nothing here can speak to.
What follows is that the number should be attributed to the outlet that obtained it
rather than to the intelligence community,
which is how it is treated above.

**The primary document on this question is a statutory trade investigation
rather than a briefing slide, and it was published.**
The [Office of the United States Trade Representative 2025][data_ustr_2025_maritime]
report on its Section 301 investigation
into China's targeting of the maritime, logistics and shipbuilding sectors
finds that "China increased its commercial vessel tonnage from just 5 percent
in 1999 to over 50 percent of global tonnage by 2023".
It records a Chinese policy target of 35 percent of global shipbuilding output,
and puts Chinese state support to the sector
at approximately 132 billion dollars across eight years.
The tonnage share rose by an order of magnitude in a generation.

$$
\frac{50}{5} = 10
$$

That is a finding of an administrative proceeding
with a record and a comment period,
which is a different evidentiary object from an unreleased slide.

The independent expert comparison comes from
[Funaiole 2026][research_funaiole_2026_testimony],
who testified that Chinese output grew from under 5 percent of the global total in 2000
to more than 53 percent in 2025,
while United States output was 0.11 percent in 2024 and effectively none in 2025.

$$
\frac{53}{0.11} \approx 482
$$

That ratio is larger than the slide's,
computed from different quantities,
and it measures commercial output share rather than warship-building capacity.
The testimony and the trade investigation agree on the Chinese trajectory
to within their rounding,
which is the check that matters,
since the two were prepared by different institutions from different sources.
Funaiole states the limitation himself,
that warships and commercial vessels
"have substantially different design and construction requirements,
so integrating their production may create inefficiencies at individual shipyards".
**A ratio of commercial tonnage is not a ratio of destroyer throughput,
and this article uses it only for the direction of the asymmetry.**

## What the Record Says About Recovery

Set against all of that,
the empirical literature on recovery from war damage is remarkably optimistic,
and it is optimistic with data rather than with sentiment.

### Japanese cities recovered their position in fifteen years

[Davis and Weinstein 2002][journal_davis_weinstein_2002]
studied 303 Japanese cities of which 66 were bombed.

$$
\frac{66}{303} \approx 0.218
$$

About a fifth of the sample took the damage and the rest serve as the control.
The bombing "destroyed almost half of all structures in these cities,
a total of 2.2 million buildings",
two thirds of productive capacity vanished,
and "Three hundred thousand Japanese were killed".
Hiroshima lost more than two thirds of its built-up area
and more than 20 percent of its population.

**Reading the primary survey behind those figures produced three disagreements,
and they are reported rather than reconciled.**
The [United States Strategic Bombing Survey's summary report on the Pacific war][government_ussbs_1946_pacific_summary]
of July 1946 is the source the paper names for its sample of 66 cities,
and the counts do not match.
The survey puts buildings destroyed by air attack at 2,510,000,
against the paper's 2.2 million.

$$
\frac{2{,}510}{2{,}200} \approx 1.14
$$

The survey gives civilian casualties of "approximately 806,000"
of which "approximately 330,000 were fatalities",
against the paper's three hundred thousand killed.
**The third disagreement is the one that matters,
because it is a difference of subject rather than of magnitude.**
The paper states that "Forty percent of the population was rendered homeless".
The survey's 40 percent is not a population share.
"In the aggregate some 40 percent of the built-up area of the 66 cities attacked was destroyed",
and the homelessness figure it gives is smaller,
that "Approximately 30 percent of the entire urban population of Japan
lost their homes and many of their possessions".
An earlier draft of this article compounded the problem
by inserting the word urban into the paper's sentence,
which the paper does not contain,
producing a claim that matched neither source.
Forty percent of built-up area destroyed
and thirty percent of the urban population made homeless
are both survey findings,
and forty percent of a population made homeless is not.

The recovery result is a regression coefficient of $-1.0$
on prior-period growth,
which means full mean reversion.
"The typical city completely recovered its former relative size
within 15 years following the end of World War II."
Reconstruction spending was not the mechanism,
contributing under one percentage point
against cumulative city growth of 55 to 96 percent.

Two qualifications belong with that finding and are usually dropped.
[Brakman, Garretsen and Schramm 2004][journal_brakman_2004_german_bombing]
find the German effect "significant but temporary"
in West Germany and absent in East Germany,
which points at institutions rather than rubble.
[Nguyen and others 2025][journal_nguyen_2025_german_cities]
apply synthetic control to 53 West German cities
and find mean reversion for only 50 to 70 percent of them,
with a sizeable minority never returning to trend.
The complement is the part that matters for a forecast.

$$
100 - 70 = 30 \ \text{percent},
\qquad
100 - 50 = 50 \ \text{percent}
$$

Between a third and a half of cities never came back to their path,
which is a different claim from the one the fifteen-year result is usually used to support.

### German capacity was never what was destroyed

[Eichengreen and Ritschl 2009][journal_eichengreen_ritschl_2009]
report that West German industrial capacity in mid-1944
stood more than a third above 1936 levels,
and that "In 1948, surviving industrial capacity was 13 percent higher than in 1936".
German output in 1948 was a different matter,
at 64 percent of 1938 levels,
while United Kingdom output in the same year
was 13 percent above its own prewar level.
The two 13 percent figures describe different countries and different quantities,
and conflating them inverts the argument.
Writing $Y$ for output and $K$ for industrial capacity,
both indexed to their own prewar year,
the German pair moves in opposite directions.

$$
Y_{1948} = 64,
\qquad
K_{1948} = 113
$$

Output stood 36 percent below its 1938 level
while capacity stood 13 percent above its 1936 level.
What the bombing destroyed was production, not the means of production.

The inference the authors draw is that Germany grew at nearly 8 percent a year through the 1950s
because it had been pushed off its path temporarily rather than stripped of its plant,
and that "More than half the economy's growth in the 1950s remains to be explained"
by capital accumulation alone.

**The bombing survey measured that distinction at plant level in 1945,
and its finding is this article's thesis stated thirty years before the econometrics.**
The [Over-all Report on the European war][government_ussbs_1945_overall_report],
issued in September 1945,
examined the anti-friction bearing industry after repeated attacks.
Building destruction "equaled approximately one-half the preraid floor space of the industry,
while the equivalent of another half was heavily damaged".
The machines inside those buildings came through very differently.
"The damage to the machine tools was not proportionate to the damage to the buildings.
Machine tools destroyed equaled 12 percent of the original inventory
and those damaged an additional 30 percent."

$$
\frac{50}{12} \approx 4.2
$$

Buildings were destroyed at roughly four times the rate of the machine tools they housed.
The survey drew the operational conclusion in the same passage,
that "it proved more difficult to put the plants out of operation than had been foreseen"
and that "Even direct hits on vital processes did not put a plant out of operation".

The same report states the lag between capacity and output as a general rule.
"During the process of contraction
the shrinkage in final output always lags behind the shrinkage in productive activity",
because stocks of parts and semifinished products carry final assembly for a while.
It also bounds what the bombing achieved against production in its heaviest year,
holding that "the total loss of German armament output from air raids in 1943
cannot be put higher than about 3 to 5 percent".
On housing the survey is precise where the secondary literature rounds,
recording that 49 of the larger cities
"had 39 percent of their dwelling units destroyed or seriously damaged",
which it gives as 2,164,800 out of 5,554,500.

$$
\frac{2{,}164{,}800}{5{,}554{,}500} \approx 0.390
$$

**Two wars, measured by the same organisation, give the same shape.**
Buildings and dwellings took heavy and quantified damage,
the machine tools and the productive capacity behind them took much less,
and output fell further than either.

### Vietnam, with its correction attached

[Miguel and Roland 2011][journal_miguel_roland_2011]
found that United States bombing of Vietnam,
at 6,162,000 tons across Indochina and concentrated so that roughly 70 percent
fell on 10 percent of districts,
had no robust long-run effect on poverty, consumption, infrastructure, literacy or density through 2002.
**That paper carries a [corrigendum][journal_miguel_roland_2024_corrigendum]**,
which corrected a projection error that displaced every district
by roughly two degrees of latitude and survived twelve years of citation.
The corrected interval preserves the headline null.
The finding is citable and it should never be cited without the correction.
The concentration of the tonnage is worth stating as a ratio,
because it is what gives the study its statistical power.

$$
\frac{70 \ \text{percent of tonnage}}{10 \ \text{percent of districts}} = 7
$$

### The phoenix factor

[Organski and Kugler 1977][journal_organski_kugler_1977]
examined 32 cases and found that while losers' power is eroded at first,
"the effects of the loss dissipate,
losers accelerate their recovery and soon resume antebellum status"
over a long run they put at fifteen to twenty years.
The full statement of that result is the third chapter of
[The War Ledger][book_organski_kugler_1980_war_ledger],
which carries the same title as the phenomenon.
The book's interior text was not obtained for this article,
so the result is quoted from the journal article
and the book is cited as the fuller treatment rather than as a source of quotations.
[Koubi 2005][journal_koubi_2005]
goes further and finds a positive causal effect of war duration on subsequent growth,
though concentrated in civil wars,
which is where a peer-conflict article should treat it with care.

The agreement between the fifteen-year city result and the fifteen to twenty year power result,
reached by entirely different methods,
is the strongest quantitative claim in this literature.

## Reconciling the Two

The wargame says decades and undefined.
The economic history says fifteen years and full reversion.
Both are correct,
because they are measuring different objects.

### Semiconductors are an ecosystem, not a building

[Boston Consulting Group and the Semiconductor Industry Association 2021][data_bcg_sia_2021_value_chain]
priced the replacement of Taiwanese foundry capacity elsewhere.
A permanent complete disruption "could take a minimum of three years
and $350 billion of investment in what would be an unprecedented effort".

$$
\frac{350}{3} \approx 117 \ \text{billion dollars per year}
$$

The asymmetry between the lost revenue and the damage it causes is the point.
One year of complete disruption costs Taiwanese foundries their 42 billion dollars of revenue
and costs electronic device makers 490 billion dollars.

$$
\frac{490}{42} \approx 11.7
$$

The published figure is twelve times,
which the arithmetic reproduces.
The same study puts the cost of fully self-sufficient regional supply chains
at a minimum of one trillion dollars of upfront investment
and a 35 to 65 percent increase in semiconductor prices,
and records that 92 percent of world capacity below 10 nanometres sat in Taiwan on 2019 data,
with the remaining 8 percent in South Korea.
Research to volume manufacturing runs about 10 to 15 years in this industry.
The two investment figures are worth comparing directly,
since one replaces Taiwan and the other replaces the trading system.

$$
\frac{1{,}000}{350} \approx 2.9
$$

Full regional self-sufficiency costs about three times what replacing Taiwanese capacity costs.

Three years is fast by the standards of the fifteen-year literature.
It is very slow by the standards of a war that the games end in three weeks,
and nothing in the estimate assumes the war is still going on.

### The island holds about twenty days of stored energy

The foundries need power,
and the published figure for how long the island can supply it
sits almost exactly on the wargame horizon.
The [US-China Economic and Security Review Commission 2025][government_uscc_2025_taiwan_chapter]
reports that Taiwan "is almost entirely reliant on imported energy",
that increased reliance on natural gas
"does not address the island's vulnerability to a blockade scenario,
given that it only has storage capacity to hold 20 days' worth of stockpiles",
and that coal stockpiles in early 2025
"were estimated to last 42 days at regular consumption,
which could be extended dependent on rationing".
Natural gas supplied 42 percent of Taiwan's energy in 2024
against a 2030 target of 50 percent,
which is the commission's wording,
and the last nuclear plant shut in May 2025.
The commission records what that closure traded away,
noting that earthquake and accident concerns outweighed
"nuclear's value as a domestic power supply
that can mitigate risk of disruptions to imports".
The share of supply is therefore rising toward the fuel
that the same chapter says is held for twenty days.

Set the gas figure against the horizon established at the top of this article.

$$
\frac{T_g}{T_{\text{LNG}}} = \frac{21}{20} \approx 1.05,
\qquad
\frac{T_{\text{coal}}}{T_g} = \frac{42}{21} = 2
$$

**The modelled war ends at about the moment the island's gas runs out.**
That coincidence is not a finding about the wargames,
which model an invasion and not a blockade,
and the two quantities were measured by different people for different purposes.
It is a finding about the aftermath.
A game that stops at 21 days stops before the energy question becomes binding,
and every reconstruction estimate in this article
assumes electricity is available to do the rebuilding.
Coal buys twice the horizon and no more,
and a rationed grid is not a grid that runs leading-edge lithography.

The commission also supplies a small measured case
of infrastructure repair under Chinese pressure,
which is the only one this article located with dates on both sides of a repeat event.
After undersea cables to the Matsu Islands were cut in February 2023
the islands "were almost entirely without internet service for several weeks
while waiting for the cables to be repaired".
When the same two cables were damaged again in January 2025,
microwave and satellite backup installed in the interval
"enabled most public services and businesses to continue functioning
while the cables were repaired".
**The repair time did not improve.
The redundancy did.**
That is this article's thesis at the smallest scale on which anyone has tested it,
and the instrument that worked was built before the war rather than after it.

### Trade relationships recover on a decadal clock, and more slowly now

[Glick and Taylor 2010][journal_glick_taylor_2010]
estimated a gravity model of bilateral trade from 1870 to 1997.
The contemporaneous coefficient is $-1.78$.

$$
1 - e^{-1.78} \approx 0.83
$$

Trade between adversaries falls by over 80 percent,
and the recovery path is the part this article needs.
Trade "returns to its normal prewar level about a decade later",
and is "still 42 percent below the prewar level five years after the cessation of war
and 21 percent below even after eight years".

The era comparison is the most uncomfortable number in the article.
A significantly negative effect lasted four years in the 1870 to 1938 subperiod
and nine years in the 1939 to 1997 subperiod.

$$
\frac{9}{4} = 2.25
$$

The modern, more integrated economy repaired its trade relationships
more slowly rather than faster.
The two world wars sit far above the average case,
and their coefficients convert the same way.

$$
1 - e^{-3.02} \approx 0.951,
\qquad
1 - e^{-2.74} \approx 0.935
$$

Trade between adversaries fell about 95 percent in the first
and about 94 percent in the second.
Neutrals are not exempt,
losing 12 percent of trade with belligerents over the full sample,
and 65 percent in the Second World War.
[Federle and others 2026][journal_federle_2026_price_of_war],
across 150 years and 60 countries,
find a war of average intensity associated with an output drop near 10 percent
at the war site and consumer prices about 20 percent higher,
with third parties affected through trade linkages and shared borders.

### The Marshall Plan did not pay for reconstruction

The reflex comparison for postwar rebuilding is the Marshall Plan,
and the measured effect is not what the reflex assumes.
[De Long and Eichengreen 1991][research_delong_eichengreen_1991_marshall]
find that aid of about 3 percent of West European output per year
raised the private investment share of national income by one percentage point,
which raises growth by half a point,
cumulating to about 2 percent of national product over four years.
Their conclusion is that "the investment effects of Marshall Plan aid
were simply too small to trigger an economic miracle".
What the aid did was fiscal and political.
Aid of two and a half percent of national product
went "a substantial way toward closing" an excess demand gap of seven or eight percent,
shortening the distributional fight that follows a war.
The annual flow and the share of the gap it closed are both modest.

$$
\frac{13.2}{4} = 3.3 \ \text{billion dollars per year},
\qquad
\frac{2.5}{7.5} \approx 0.33
$$

Aid covering about a third of an excess demand gap
is a stabilisation instrument rather than a construction budget.

[Tarnoff 2018][research_tarnoff_2018_marshall_plan]
gives the official totals,
roughly 13.3 billion dollars to 16 countries from April 1948 to June 1952,
about 143 billion in 2017 dollars,
with the first-year appropriation of 4 billion amounting to roughly 13 percent
of a federal budget near 30 billion dollars.
**No figure for the plan as a share of donor gross domestic product
appears in that source**,
and none is asserted here.

**The statute and the administration's own accounts are available
and they give different numbers from the secondary summaries.**
The [Economic Cooperation Act of 1948][government_economic_cooperation_act_1948],
enacted on 3 April 1948 at 62 Stat. 137,
authorised "not to exceed $4,300,000,000"
for the twelve months following enactment,
and states plainly that the authorisation is limited to that period
"in order that subsequent Congresses may pass on any subsequent authorizations".
An authorisation is not an appropriation,
which is why the 4.3 billion in the statute
and the roughly 4 billion first-year figure quoted above
are both correct and are not the same quantity.

The [thirteenth and last report of the Economic Cooperation Administration][government_eca_1951_thirteenth_report],
covering the quarter ended 30 June 1951,
gives the programme's own accounting.
"During the three and a quarter years that the Marshall Plan has been in operation
a total of $12.3 billion has been made available to ECA",
of which 12.2 billion had been obligated and 10.7 billion expended.

$$
\frac{10.7}{12.3} \approx 0.87
$$

Thirteen percent of the money made available had not been spent
when the programme's final report was written,
which is a fact about the speed of reconstruction spending
rather than about its size.
The figure also sits below the 13.3 billion quoted from the secondary account above,
because one counts what reached the administration
and the other counts the programme as later totalled.

### What reconstruction costs when somebody measures it

The [Fourth Rapid Damage and Needs Assessment][research_world_bank_2025_rdna4],
prepared by the World Bank with the government of Ukraine,
the European Commission and the United Nations,
assessed Ukraine after almost three years of war.
It is the one case in this literature where a damaged economy at war
has been costed line by line by its eventual funders,
and it is read here in the full report rather than in the press release.
Direct damage reached 176.1 billion dollars,
and total reconstruction and recovery needs estimated over ten years reached 524.6 billion,
which the assessment puts at "approximately 2.8 times the estimated nominal
GDP of Ukraine for 2024".
Needs exceed measured damage by a factor near three,
because recovery is not the same thing as repair.

$$
\frac{524.6}{176.1} \approx 2.98
$$

That ratio is the most transferable quantity in the reconstruction literature,
because it is dimensionless.

$$
\frac{\text{reconstruction needs}}{\text{annual output}} \approx 2.8
$$

**The sector detail is where the assessment speaks to this article's thesis.**
Housing took 57.6 billion dollars of the damage
and carries 83.7 billion of the needs,
the largest sectoral share at about 16 percent of the total.

$$
\frac{83.7}{57.6} \approx 1.45
$$

Housing is the most nearly physical category in the assessment
and its needs-to-damage multiple is roughly half the economy-wide figure.
The categories that push the aggregate multiple to three
are the ones with no damaged asset behind them at all,
among them explosive hazards management at almost 30 billion dollars
and debris clearance and demolition at around 13 billion.
**Rebuilding what was hit is the cheap part of recovery,
and the assessment's own arithmetic says so.**

The assessment also measures the gap between plant and output directly.
Thirteen percent of the total housing stock was damaged or destroyed,
affecting more than 2.5 million households,
while "2024 GDP is 78 percent of 2021 GDP in real terms".
Writing $K$ for the housing stock and $Y$ for real output,
each as a share of its own baseline,
the two quantities have moved by different amounts in the same direction.

$$
K \ge 87, \qquad Y \approx 78
$$

The inequality is deliberate.
The 13 percent is housing damaged or destroyed together,
so the share of the stock still standing is at least 87 percent
and is higher than that to the extent damaged units are repairable.
The two figures also carry different baselines,
the housing share against the current stock and the output share against 2021,
so the pair is a comparison of magnitudes and not a matched ratio.
What survives those caveats is the direction.
**At most a seventh of the housing is gone
and something near a fifth of the output is gone**,
which is the same shape as the German pair above
and is measured here in a war that has not stopped.

The damage figure itself grew between assessments,
and the report states the growth rather than leaving it to be computed.
Direct damage rose by almost 24 billion dollars against the third assessment's 152.5 billion,
which the report gives as 15.5 percent.

$$
\frac{176.1 - 152.5}{152.5} \approx 0.155
$$

A war that is being assessed while it continues
adds about a sixth to its own damage bill in a single year.

For comparison of scale rather than of case,
[SIGIR 2013][research_sigir_2013_learning_from_iraq]
recorded 60.64 billion dollars of United States relief and reconstruction funding for Iraq
across nine years,
averaging more than 15 million dollars a day,
with at least 8 billion judged wasted.
Expenditure of 53.26 billion dollars across nine years gives the daily rate.

$$
\frac{53.26 \times 10^{9}}{9 \times 365} \approx 16.2 \ \text{million dollars per day}
$$

**Occupation-era aid to Japan was listed as unverified in an earlier draft
and a primary figure has now been located.**
A [State Department paper of March 1962][government_frus_1962_garioa_settlement],
published in the Foreign Relations of the United States series,
records that total disbursements to Japan
under the Government and Relief in Occupied Areas appropriations
for fiscal years 1947 through 1952,
together with earlier emergency assistance from the Army,
"were about $1.99 billion",
and that after deductions the United States claim "was about $1.8 billion".
Japan settled that claim for 490 million dollars over fifteen years.

$$
\frac{490}{1{,}800} \approx 0.27
$$

Japan repaid a bit over a quarter of the claimed sum.
Two cautions belong with those figures.
They cover Japan alone and not Germany or Korea,
and they bundle the relief appropriations
with the economic rehabilitation spending
that a 1948 proviso authorised out of the same account
rather than through a separate one.
The department's own view of the bookkeeping was unflattering.
A [memorandum of conversation from 1954][government_frus_1954_garioa_bookkeeping]
records Secretary Dulles observing that
"the bookkeeping on the GARIOA funds had been very fuzzy and sloppy",
which is a caution about the figure
issued by the government that produced it.

The [World Bank 1996][research_world_bank_1996_bosnia]
priced Bosnian priority reconstruction at 5.1 billion dollars over three to four years.
Taiwan's own reconstruction has no published estimate at all,
which is treated below as one of the gaps.

## Ending the War Is Harder Than Winning It

The termination literature explains why the games stop where they do
and why the war would not.

[Iklé 2005][book_ikle_2005_every_war_must_end]
established the general observation that governments enter wars
with elaborate plans for fighting and almost none for stopping.
[Reiter 2009][book_reiter_2009_how_wars_end]
supplies the mechanism most applicable here.
War termination turns on information about the balance of power
and on fear that the other side cannot credibly commit to abide by a settlement.
Where the commitment problem is severe,
a state refuses limited terms and pursues absolute victory.
Neither side in a Taiwan war could credibly promise not to rearm and try again,
which is the condition Reiter identifies as fatal to a negotiated end.

[Goemans 2000][book_goemans_2000_war_and_punishment]
adds regime type.
Leaders of mixed regimes,
who expect punishment whether they lose moderately or disastrously,
have a disincentive to settle on moderately losing terms
and therefore gamble for resurrection.
[Stanley and Sawyer 2009][journal_stanley_sawyer_2009]
find that rational updating during a war
"can develop a significant lag, which extends the war beyond a logical ending point",
and that a change in the domestic governing coalition
is often what restarts it.
[Croco 2011][journal_croco_2011]
sharpens this into culpability,
finding that audiences punish culpable leaders who lose and spare non-culpable ones,
which means a settlement may become available only after the leadership that started the war is gone.
[Flavin 2003][journal_flavin_2003_conflict_termination]
states the distinction the planning literature keeps losing,
that "Conflict termination is the formal end of fighting, not the end of conflict".

**Joint doctrine confirms the narrowness he complains of.**
[Joint Publication 3-0][government_jp_3_0_2018]
defines termination criteria as
"The specified standards approved by the President and/or the Secretary of Defense
that must be met before a military operation can be concluded",
and frames the military end state as
"a point in time or a set of conditions
beyond which the President does not require the military instrument of national power
as the primary means to achieve remaining national objectives".
**Termination in doctrine is therefore the end of an operation
and the start of somebody else's problem**,
which is precisely the handoff no source in this article costs.

**The strategy literature has thought about the end of the war more carefully
than the wargames have, and it does not promise one.**
[Heim, Burdette and Beauchamp-Mustafaga 2024][commentary_heim_2024_denial_worst]
argue for a denial theory of victory over cost imposition,
and are explicit that denial is not a termination mechanism.
Denial "gives Beijing space to decide to stop the war
after it realizes that its military operation has failed",
but it "does not rest on the assumption that China will immediately stop fighting
after the invasion fails".
They name the continuation directly,
that "It is certainly possible that China would shift to a blockade
or strategic bombing of Taiwan
to see if it could still achieve its original political objective".

That sentence and the energy figures above belong together,
and no source located joins them.
The recommended American strategy for defeating an invasion
anticipates a shift to blockade as the likely next move,
and the island holds about twenty days of gas and about forty days of coal.
**A theory of victory that succeeds on its own terms
hands the aftermath to the constraint the reconstruction literature never prices.**

[Krepinevich 2020][research_krepinevich_2020_protracted_great_power_war]
draws the conclusion for the nuclear case.
Great-power wars can be protracted "only if political constraints are imposed on vertical escalation",
victors "would not be able to impose anything like unconditional surrender",
"Regime change would be out of the question",
and the result "would be less a peace
than the start of the next round in an open-ended struggle for geostrategic advantage".

## Regime Survival, Where the Rhetoric Outruns the Evidence

### What the wargame asserts, and what it admits in the same sentence

The most cited claim about the aftermath is that a failed invasion would threaten Communist Party rule.
Its source is the CSIS report,
and the sentence is worth reading closely.

> Although the project did not explore what effects these losses might have
> on the Chinese political system,
> the CCP would be risking its hold on power.

The assertion and the admission that it was not studied occupy one sentence,
and the supporting footnote is to an opinion essay.
RAND's counterpart judgment is hedged in the other direction,
holding that "the regime and its security forces presumably could withstand such challenges",
at a cost in repression and legitimacy.
**Neither is a finding.
One is an assertion the authors disclaim,
and the other rests on a hedge the authors chose deliberately.**

### The base rates say defeat alone is a weak predictor

The political science that would settle it exists and has not been applied to this case.
[Goemans 2008][journal_goemans_2008_which_way_out]
reports that of leaders who lost office in a regular manner,
92 percent retired safely and 8 percent suffered punishment,
while of those removed irregularly,
only 20 percent escaped punishment,
41 percent were exiled,
22 percent imprisoned
and 18 percent killed.
Those four shares sum to 101 rather than 100,
which the paper attributes to rounding and which is recorded here
because an unexplained sum is how a transcription error hides.

$$
20 + 41 + 22 + 18 = 101
$$

The conditional result is the one that matters,
and it cuts against the popular story.
For the relevant regime type,
defeat in an international crisis "would only mildly worsen the prospects of such a leader,
since he or she would face an increase of only 3 percentage points
in the chances of an irregular removal from office",
while a draw almost halves the risk,
from 27 percent to 14 percent.

$$
\Delta_{\text{defeat}} \approx +3 \ \text{points},
\qquad
27 \rightarrow 14 \ \text{for a draw}
$$

[Goemans, Gleditsch and Chiozza 2009][journal_goemans_2009_archigos]
give the population rates from 3,025 leader spells across 188 countries from 1875 to 2004.
The [dataset behind that paper][data_archigos_2016_leader_dataset]
has since been extended,
version 4.1 of March 2016 covering 1875 to the end of 2015,
and its authors ask that the version and date be cited alongside the article.
The rates quoted here are the published ones and not recomputed from the current file.
Exits were 64.63 percent regular and 19.07 percent irregular,
and post-tenure fates were 63.64 percent no punishment,
12.43 percent exile,
5.09 percent imprisonment
and 3.83 percent death.
The exit categories in that dataset sum as they should,
which is the check the previous figures invite.

$$
64.63 + 19.07 + 6.08 + 1.98 + 0.17 + 2.38 + 5.59 + 0.10 = 100.00
$$

[Bueno de Mesquita, Siverson and Woller 1992][journal_bueno_de_mesquita_1992]
established the directional relationship between defeat and violent regime change
across all war participation from 1816 to 1975,
and [Debs and Goemans 2010][journal_debs_goemans_2010]
give the theory,
that the less punitive the consequences of losing office,
the more a leader can concede to strike a bargain.

### The counter-evidence, which is Chinese and specific

[Fravel 2005][journal_fravel_2005_regime_insecurity]
found that China has settled 17 of 23 territorial disputes,
often with substantial compromises,
and that "state leaders are more likely to compromise in territorial disputes
when confronting internal threats to regime security".
That is the opposite of gambling for resurrection.

$$
\frac{17}{23} \approx 0.74
$$

Roughly three quarters of the disputes were settled,
many of them on terms that conceded territory.
[Quek and Johnston 2018][journal_quek_johnston_2018]
tested Chinese public tolerance for backing down
and found that leaders may prefer more flexibility in a crisis rather than less.
[Sudduth 2026][commentary_sudduth_2026_double_edged_swords]
adds that personalist leaders face considerably lower odds of removal after defeat
than non-personalist counterparts.

Taken together the honest summary is that the theory points both ways,
the base rates are modest,
the one China-specific empirical finding points toward compromise,
and no published study applies any of it to a failed Taiwan invasion.

## Occupation Arithmetic, Which Nobody Appears to Have Done

If the invasion succeeds,
the aftermath is an occupation,
and the occupation literature has a number.
[Quinlivan 2003][research_quinlivan_2003_burden_of_victory]
states that successful population security has required
"force ratios either as large as or larger than 20 security personnel
per thousand inhabitants",
counting troops and police together,
which is roughly ten times the ratio required for simple policing.

**The provenance of that ratio needs stating carefully,
because it is not what it is usually said to be.**
The earlier [Quinlivan 1995][research_quinlivan_1995_force_requirements]
article in *Parameters* is routinely credited with establishing a 20-per-thousand rule,
and reading it shows that it does no such thing.
It is descriptive throughout,
organised into sections on ratios of one to four, four to ten, and above ten per thousand,
and its own summary claim is weak,
that "Force ratios larger than ten members of the security forces
for every thousand of population are not uncommon in current operations".
Twenty per thousand appears in it as a measured value in two cases rather than as a norm,
the British in Malaya, where "the British generated a force ratio
of about 20 per thousand of population",
and Northern Ireland, "giving a force ratio of about 20 per thousand".
**What 1995 contributed was the population-proportional method.
The norm was hardened later by other hands.**

Doctrine is where it hardened.
The 2006 counterinsurgency field manual
[FM 3-24][government_fm_3_24_2006]
states at paragraph 1-67 that "Most density recommendations fall within a range
of 20 to 25 counterinsurgents for every 1000 residents in an AO",
and that "Twenty counterinsurgents per 1000 residents
is often considered the minimum troop density required for effective COIN operations",
while adding that "as with any fixed ratio,
such calculations remain very dependent upon the situation".
It attributes the number to nobody.
**The 2014 revision of that manual removed the ratio altogether**,
so the figure this article is about to use
appears in no current United States doctrinal publication.

Taiwan's registered population was 23,299,132 at the end of December 2025,
according to the
[Ministry of the Interior's monthly bulletin of interior statistics][data_moi_2026_taiwan_population].
Writing $P$ for population and $\rho$ for the required ratio per thousand,
the requirement follows.

$$
F = \rho \times \frac{P}{1000} = 20 \times 23{,}299 = 465{,}980 \ \text{personnel}
$$

Quinlivan also states a rule of five for sustainment,
five personnel in the force for each one deployed on a six-month rotation.

$$
5 \times 465{,}980 \approx 2{,}330{,}000 \ \text{personnel}
$$

**The population is falling, so the requirement falls with it.**
The same series gives 23,400,220 at the end of 2024
and 23,224,721 at the end of August 2026,
a decline of about 175,000 in twenty months.
At the most recent figure the garrison requirement is about 464,000,
so the quantity is drifting downward by a few hundred personnel a month.
That sensitivity is worth stating because it is small.
**A demographic trend of that size does not change the conclusion,
which is what a claim about an order of magnitude should look like.**

**This calculation is my own and appears in no source located.**
It applies a ratio derived from Bosnia, Kosovo, Somalia, Haiti, Afghanistan and Iraq
to a case none of those resembles,
and it assumes a garrison model rather than a compliant population.
It is offered as the order of magnitude the published literature implies,
and as evidence that the two bodies of work have never been joined.

Two comparisons put that figure in proportion.
Against the invasion force in the most detailed public campaign model,
[Stewart 2023][research_stewart_2023_island_blitz],
which lands 262,000 troops by day 19,
the garrison requirement is larger than the invasion.

$$
\frac{465{,}980}{262{,}000} \approx 1.78
$$

Against the actual deployment in Iraq in 2003,
which Quinlivan records at 6.1 personnel per thousand inhabitants,
the required ratio is more than three times what was fielded.

$$
\frac{20}{6.1} \approx 3.3
$$

The two operations that did reach the ratio were Bosnia at 22.6 and Kosovo at 23.7 per thousand,
on populations far smaller than Taiwan's.
For context on the resistance side,
[Lee, Chen and Chen 2024][journal_lee_2024_taiwan_attitudes]
report willingness to fight between 68 and 75 percent across five survey waves,
and [Blanchette and McGregor 2026][commentary_blanchette_2026_after_invasion]
report that about 7 percent of Taiwanese adults,
roughly 1.3 million people,
support immediate independence.

[McGregor and Blanchette 2026][research_mcgregor_2026_after_annexation]
is the one serious treatment of how Beijing would govern the island,
describing a three-stage conception of security crackdown,
institutional restructuring beyond the Hong Kong model,
and a decades-long project of psychological re-engineering.
Their framing of the field is the point for this article,
that attention to how Beijing might seize Taiwan
"has come at the expense of an equally significant question
of how it would attempt to rule the island afterwards".

## Recovery From Nuclear Use, Where the Taiwan Case Is Absent

The nuclear consequence literature is large, quantitative, and about other wars.
[Xia and others 2022][journal_xia_2022_nature_food]
model soot injection against food supply across six scenarios.
Their first table is read here in the published paper,
which is open access,
and every figure below is taken from it directly.
At 5 teragrams of soot from 100 weapons of 15 kilotons,
direct fatalities are 27 million and 255 million people are without food at the end of year two.
At 150 teragrams from 4,400 weapons of 100 kilotons,
direct fatalities are 360 million
and 5.341 billion people are without food.
Maximum average surface air temperature over crop regions
falls 1.5 degrees Celsius at the low end
and 14.8 degrees at the high end,
peaking within one to two years
and with the reduction "lasting for more than 10 years".

The ratio between the direct and the indirect toll is the finding.

$$
\frac{255}{27} \approx 9.4 \ \text{at 5 Tg},
\qquad
\frac{5{,}341}{360} \approx 14.8 \ \text{at 150 Tg}
$$

Two further ratios describe how the scenarios scale.
A thirtyfold increase in soot multiplies direct deaths by about thirteen
and the starving by about twenty-one.

$$
\frac{150}{5} = 30,
\qquad
\frac{360}{27} \approx 13.3,
\qquad
\frac{5{,}341}{255} \approx 20.9
$$

The indirect toll grows faster than the direct one,
which is the whole argument of that literature.

**The same paper carries a second table that the secondary accounts of it drop,
and it is the one that bears on this article.**
It reports the change in food calorie availability in year two
for each nuclear-armed nation,
assuming no trade.
Under its central livestock assumption
Chinese availability falls 14.1 percent at 5 teragrams
against a global average fall of 8.2 percent,
and 99.5 percent at 150 teragrams against a global 81.3 percent.

$$
\frac{14.1}{8.2} \approx 1.72
$$

China loses over 70 percent more of its food calories than the world average
in a scenario that is a war between India and Pakistan
and has nothing to do with China at all.
Of the nine nuclear-armed states in the table
only North Korea fares worse at that soot level, at 18.1 percent,
while France, Russia and the United Kingdom show small gains
because the no-trade assumption stops them exporting.
The mechanism is latitude and diet rather than proximity to the detonations.

**The paper also states a scope limit that no recovery argument may ignore.**
Impacts in the warring nations themselves
"are likely to be dominated by local problems,
such as infrastructure destruction, radioactive contamination and
supply chain disruptions,
so the results here apply only to indirect effects from soot injection in remote locations".
The model is therefore silent about the belligerents,
which is precisely the population an article about postwar recovery would want.

[Shi and others 2025][journal_shi_2025_adapting_agriculture]
address recovery rather than damage,
finding maize production down 7 percent at 5 teragrams and 80 percent at 150,
"with recovery taking 7 to 12 years",
and seed availability as the binding bottleneck.

$$
\frac{80}{7} \approx 11.4
$$

The crop loss scales more steeply than the soot does at the low end.
[Jehn and others 2025][journal_jehn_2025_food_trade]
find that at 37 teragrams most countries lose 50 to 100 percent of food imports.
[Chan and others 2025][journal_chan_2025_resilience]
state the neglect directly,
that recovery measures remain heavily neglected relative to prevention,
and find expected deaths peaking in the 250 to 550 detonation range.

The science is contested at the fire-physics end rather than the climate end.
[Reisner and others 2018][journal_reisner_2018]
produced no nuclear winter in their firestorm simulations,
and [Robock, Toon and Bardeen 2019][journal_robock_2019_comment]
objected that the modelled target resembled a low-density suburb.
Both sides agree the uncertainty is in the plume and not in the response to soot aloft.
The [National Academies 2025][research_nas_2025_nuclear_war_effects]
consensus study,
read here in full rather than from its catalogue entry,
states the uncertainty position in its own words.
"It is important to bear in mind that uncertainties are involved in the analysis
of every step of the causal pathway
that leads from a nuclear weapons exchange
to its environmental and societal and economic endpoints",
and those uncertainties "interact with each other and propagate along the pathway,
such that, regardless of the relative certainty of knowledge at any one point,
the overall analytical uncertainty will always increase along the pathway".
Its concluding chapter holds that the compounded uncertainty and the missing data
"fundamentally constrain the quantification of precise environmental
and societal and economic outcomes from any given nuclear war scenario".
The study also excluded radioactive fallout by design,
stating that "an evaluation of the effects of radioactive fallout
was not included in the scope of the work",
which matters for any recovery argument built on it.

**Reading that report in full settled a question this article had left open.
It contains no economic recovery analysis and no recovery timescale for human systems.**
What it offers on recovery is a physical result,
that in the largest simulation "ocean recovery from the conflict
is decades at the surface and hundreds of years at depth",
and a research gap,
that "There are major research gaps around quantifying the impacts
of abrupt cooling and environmental shocks on crop yields, livestock, fisheries,
pollution exposure pathways, and ecosystem recovery timelines".
The newest and most authoritative synthesis in the field
therefore does not answer the question this article is asking,
and says as much.

### The one government study that did model recuperation is from 1979

**The most substantial official treatment of recovery after nuclear use
is nearly fifty years old.**
The Office of Technology Assessment's
[Effects of Nuclear War][government_ota_1979_effects_of_nuclear_war],
prepared for the Senate Committee on Foreign Relations,
devotes a chapter to what it calls the recuperation period,
and its framing has not been superseded.
Recovery is posed as a race.
"In effect, the country would enter a race, with economic viability as the prize",
in which production must be restored
before the consumption of stocks and the wearing out of surviving goods overtakes it.
If that race is lost,
consumption sinks to the level of production and depresses it further,
and "At some point this spiral would stop,
but by the time it did so
the United States might have returned to the economic equivalent of the Middle Ages".

The study is candid about the limit of its own method,
in terms no modern document improves on.
"The effects of a nuclear war that cannot be calculated
are at least as important as those for which calculations are attempted."
It sorts consequences into three classes,
those that can be calculated,
"Effects that would surely take place, but whose magnitude cannot be calculated",
and effects whose likelihood is as incalculable as their magnitude,
among which it lists "a long downward economic spiral before viability is attained"
and political disintegration.
On the central question it is blunt.
"Nobody knows how to estimate the likelihood
that industrial civilization might collapse in the areas attacked."
And on the planning question that the wargame literature inherits,
"The economic and social problems following a nuclear attack
cannot be foreseen clearly enough to permit drafting of detailed recovery plans".

Its statement of the asymmetry between destruction and rebuilding
is the cleanest in any source located,
and it is the thesis of this article in one sentence written in 1979.
Structures destroyed in seconds or hours
"might not be rebuilt or replaced for years, or even decades",
while the dead "might not be replaced in a demographic sense for several generations".
For the standing reference on weapons effects themselves
the corresponding document is
[Glasstone and Dolan 1977][government_glasstone_dolan_1977],
issued jointly by the Department of Defense and the Department of Energy.

**None of those studies models a war between China and the United States,
and reading the primary tables makes the claim more precise than it first appears.**
The scenarios divide into regional exchanges in South Asia
and a single global exchange.
The 150 teragram case is not a United States and Russia scenario,
since the paper states it "assumes attacks on France, Germany, Japan,
United Kingdom, United States, Russia and China".
China is therefore a target in the largest scenario in the literature,
but as one member of a general exchange among all the major arsenals,
entered at the top of an escalation ladder rather than from a war over Taiwan.
The distinction matters because the quantity a recovery estimate needs
is the damage to two belligerents and their trading partners,
and no published scenario supplies it.
[Xia and others 2015][journal_xia_2015_chinese_agriculture]
is the closest to the case at hand,
finding first-year Chinese wheat production down 53 percent
and effects decaying over more than a decade,
and its detonations are in South Asia.
The RAND volumes on
[keeping a Taiwan conflict under the nuclear threshold][research_beauchamp_2024_denial_without_disaster_v3]
model escalation toward use,
and the [Atlantic Council exercises][research_garlauskas_2025_guardian_tiger]
model political response to use,
with neither exercise achieving a stable resolution.
On the civil defence side,
[Buddemeier and Dillon 2009][research_buddemeier_2009_response_planning]
show that early adequate sheltering followed by informed delayed evacuation
saves more lives than immediate evacuation.

## The Postwar Order

[Priebe and others 2023][research_priebe_2023_alternative_futures_v1]
is the closest published match to this article's subject.
In the scenario where China annexes Taiwan after an eight-month war
ending in a Chinese non-strategic nuclear demonstration,
a United States-led counterbalancing coalition forms
and both Japan and South Korea pursue nuclear weapons.
The companion [volume on historical cases][research_evans_2023_alternative_futures_v2]
codes ten great-power conflicts since 1853
and finds prewar predictions about consequences for the balance of power
inaccurate in three cases,
partially accurate in six
and accurate in one,
while stating that "the long-term consequences of such a conflict remain poorly understood".

On allied nuclear latency the demand signal already exists.
The [Chicago Council 2022][data_chicago_council_2022_south_korea]
found 71 percent of South Koreans favouring an indigenous nuclear weapon,
and 67 percent preferring that to redeployed United States weapons when forced to choose.

$$
\frac{67}{9} \approx 7.4
$$

The preference for an indigenous arsenal runs more than seven to one
against the alliance-managed alternative.
[Nemeth 2026][journal_nemeth_2026_suez_moment]
gives the two paths for the alliance system after a visible defeat,
a hollowing into ceremonial shells
or an adaptation in which the United States becomes first among equals.
His supporting figures put the naval balance at 395 Chinese battle-force ships
against roughly 295 for the United States in 2025.

$$
\frac{395}{295} \approx 1.34
$$

**Checking that ratio against the primary documents changed what it means.**
The 395 is not a count of Chinese ships in 2025.
It is a projection made in 2023.
The [Department of Defense annual report to Congress][government_dod_2023_china_report]
for that year
states that the People's Liberation Army Navy
"is the largest navy in the world with a battle force of over 370 platforms"
and that its "overall battle force is expected to grow to 395 ships by 2025
and 435 ships by 2030".
**The 2025 edition of the same report gives no fleet total at all**,
having been restructured to about half the length of the 2023 edition,
so no current official count is available to test the projection against.
The American figure does have a current primary,
since the Navy's own plan states 291 battle force ships.
Recomputed on the two firmest numbers,
a 2023 measurement of over 370 against a 2026 statement of 291,
the ratio is smaller and rests on quantities three years apart.

$$
\frac{370}{291} \approx 1.27
$$

Either way the direction holds and the precision does not,
and a ratio assembled from a projection and a count
should not be quoted to three figures.

[Ikenberry 2019][book_ikenberry_2019_after_victory]
supplies the older theoretical baseline,
that the order a victor builds depends on its capacity for credible self-restraint.

Whether Taiwan is worth the reconstruction is itself disputed.
[Green and Talmadge 2022][journal_green_talmadge_2022]
argue Chinese control of the island would materially improve China's position,
and [Caverley 2025][journal_caverley_2025]
rebuts them with a kill-chain model,
finding the transformation "would make little difference to the broader military balance".

## Four Gaps in the Literature

These are stated as gaps in a bounded search rather than as proofs of absence.
Each was reached independently and checked against the sources named above.

- **No wargame models the post-invasion period.**
CSIS terminates at three to four weeks and says so.
[Stewart 2023][research_stewart_2023_island_blitz]
models the campaign to the seizure of Taipei on day 46
and states that it does not model occupation or sustained resistance.
- **The reverse case is one clause.**
The fate of Communist Party rule after a failed invasion
exists in the public record as a conditional sentence in an executive summary
whose authors disclaim having studied it.
- **Nobody has modelled nuclear consequences or recovery for a Taiwan scenario.**
The escalation studies stop at use.
The consequence studies are about other theatres,
and the one scenario that includes China as a target
reaches it through a general exchange among every major arsenal.
Reading the 2025 National Academies report in full
confirmed that the field's newest synthesis
carries no economic recovery analysis and no recovery timescale for human systems,
and names that as a research gap in its own text.
**The only official study containing a recuperation analysis dates from 1979.**
- **The occupation force-density literature and the invasion literature have never been joined.**
The arithmetic above took minutes and appears nowhere.
The reference pass made this gap wider rather than narrower.
The ratio the arithmetic depends on
is descriptive in the 1995 article usually credited with it,
prescriptive in a 2006 field manual that attributes it to nobody,
and **absent from that manual's 2014 revision**,
so the number is applied to no Taiwan case
and no longer appears in the doctrine that made it a norm.

A fifth observation follows from the four.
There appears to be no published work whose central thesis
is that the wargaming literature ignores the aftermath.
What exists is adjacent and assemblable,
which is what this article has done.

**A sixth observation came out of the reference pass itself.**
The primary documents are more candid about all of this than the secondary literature is.
The Navy says its doubled budget bought no additional ships.
The intelligence community says a protracted war
risks unprecedented economic costs.
The National Academies says its own causal pathway cannot be quantified.
The Office of Technology Assessment said in 1979
that "Nobody knows how to estimate the likelihood
that industrial civilization might collapse in the areas attacked".
**The confidence in this field increases with distance from the primary sources**,
which is a finding about the literature rather than about the war.

## Epistemic State

**Read in primary text for this article.**
The CSIS invasion report, including the reconstitution passage, the horizon statements and the regime-risk sentence.
The RAND 2016 report's termination and economic passages.
The CSIS industrial mobilisation report, including its 8.4 and 13.8 year figures and its own caveat.
The two 2026 CSIS munitions analyses.
The Congressional Budget Office shipbuilding testimony, through a Wayback copy because the canonical host refuses automated clients.
The Congressional Research Service Virginia class report through the EveryCRSReport mirror.
Both Government Accountability Office shipbuilding reports through files.gao.gov.
The Funaiole testimony.
The Quinlivan force-ratio essay.
The Boston Consulting Group and Semiconductor Industry Association study.
The Davis and Weinstein working paper.
The Eichengreen and Ritschl working paper.
The Glick and Taylor working paper.
The De Long and Eichengreen working paper.
The Goemans 2008 and Archigos working papers, for the base rates quoted.
The Krepinevich executive summary.
The full Fourth Rapid Damage and Needs Assessment for Ukraine,
replacing the press release this article first cited,
which is the source of the sector split, the housing figures and the real output ratio.
The Nature Food paper, which is open access,
including both its scenario table and its per-nation calorie table.
The Office of the United States Trade Representative Section 301 report
on the maritime, logistics and shipbuilding sectors.
The Office of the Director of National Intelligence annual threat assessment.
The US-China Economic and Security Review Commission Taiwan chapter,
for the energy stockpile and undersea cable passages.
The Heim, Burdette and Beauchamp-Mustafaga essay,
whose quotations were checked against the page source rather than a summary of it.
The National Academies report in full, through the read-online view,
since its own catalogue page puts the file behind a login.
The Office of Technology Assessment study of 1979,
through a scan of the printed edition,
with the page offset between scan and folio confirmed at several points.
Both bombing survey reports,
the Pacific summary from a scan
and the European over-all report from page images,
the latter transcribed by eye because its optical character recognition is unusable for quotation.
The Navy shipbuilding plan for fiscal year 2027, direct from the Navy comptroller.
The Department of Defense competition report and both accountability office reports,
through the Wayback Machine, since the canonical hosts refuse automated clients.
The two annual reports to Congress on Chinese military developments, for 2023 and 2025.
The Economic Cooperation Act as enacted, and the final report of its administering agency.
Two State Department documents in the Foreign Relations of the United States series.
The 1995 Quinlivan article, through an archived copy of the original electronic edition.
The approved December 2006 counterinsurgency field manual and its 2014 revision.
Joint Publication 3-0.
The Ministry of the Interior population series, parsed from the published spreadsheet.

**Every quotation added in the reference pass was checked against the source text
rather than against an intermediary's report of it.**
Nineteen were confirmed on the first pass.
Several others failed a literal string match
and were confirmed only after normalising for scanned hyphenation,
two-column interleaving and a running header that fell inside a sentence.
**That distinction matters, because a failed match is not evidence of a bad quotation
and a passing match on a summary is not evidence of a good one.**

**Reachability of the references.**
Ninety-seven references carry 94 external addresses,
the other three being internal cross-references to published posts.
Seventy-nine of the 94 resolve to a 200 response.
The remaining fifteen are catalogued publisher and agency blocks,
every one of them a journal digital object identifier
or the Congressional Budget Office,
and each was verified through the registry instead.
**Reaching that count required two different user agents.**
Nine addresses answer a browser string and refuse an honest one that carries a contact address,
and two government hosts do the exact opposite,
so a sweep that sends a single agent reports blocks that are properties of the client.
That measurement is recorded in the project's URL verification notes
rather than left in this article.

**Verified against the registry rather than read.**
Every journal citation was checked against Crossref for title, authors, journal, volume, issue, year and pages.
Several of those articles exist for this article only as registry records and abstracts,
because MIT Press, Oxford University Press, Wiley, Sage, Taylor and Francis and JSTOR
all refuse automated clients.
Where an abstract is the only layer verified, no number from inside the article is quoted.

**Documented only through a summary or a press account.**
The 200-to-1 shipbuilding slide, through the outlet that obtained it and the Navy's own caveat.
That slide is no longer load-bearing,
because the Section 301 report now carries the tonnage-share claim as a government finding,
and a search of the public record found no released intelligence publication stating it.

**Cited at one remove, with the earliest source not read.**
The 51-to-5 consolidation figure,
which the Department of Defense states three times
and attributes to a presidential commission report of 2002 that was not retrieved.
The seven-yards-and-four-primes count,
which the accountability office reports from a departmental industrial capabilities report
that was not retrieved.
The phoenix factor result,
quoted from the 1977 journal article,
with the 1980 book cited as the fuller treatment and its interior text not obtained.

**Derived in this article.**
The aircraft replacement bracket, which reproduces the published figure.
The undefined carrier replacement time.
The submarine rate ratio.
The munitions cycle sum, which reproduces the published 52 months.
The Patriot surge multiple.
The workforce annual requirement.
The surge-to-peacetime ratio.
The commercial shipbuilding output ratio.
The aircraft procurement ratio.
The semiconductor cost per year and the twelve times revenue asymmetry, which reproduces the published figure.
The trade destruction fraction from the published coefficient, which reproduces the published 80 percent.
The era persistence ratio.
The Ukraine needs-to-output ratio, which the assessment itself states.
The occupation force requirement and its sustaining base.
The nuclear indirect-to-direct toll ratios.

**Assumptions this article introduces that its sources do not make.**
The occupation calculation applies a ratio from unrelated cases to Taiwan
and assumes a garrison model.
The surface combatant replacement expression omits concurrency,
which the public sources do not state,
and it is presented as a shape rather than a result.
The comparison of Chinese and American aircraft procurement rates
sets a Mitchell Institute estimate against a CSIS figure,
which are different instruments.
Each is flagged where it is used.

**Corrections and collisions found while checking.**
A research sweep reported German industrial capacity in 1948 as 13 percent above 1936.
The source contains that sentence,
and it separately contains a different 13 percent figure about United Kingdom output.
Both are now stated with their subjects attached.
A sweep also supplied a RAND quotation containing the phrase foreshorten it
that does not appear in the report text,
and it was dropped.
Heath's 22 iterations and the CSIS report's 24
are both reported with their sources,
because the discrepancy is real.
The Miguel and Roland corrigendum is cited alongside the original,
because the original's headline result survived a projection error
that ran for twelve years.
A sweep reported a civil defence funding pledge at two different values
in two outlets,
so no figure for it appears here.

**Corrections the primary-reference pass produced.**
All six figures this article quotes from the Nature Food scenario table
were confirmed against the published table,
so the earlier reliance on a sweep's extraction is withdrawn rather than merely noted.
Reading the same paper corrected a claim this article had made too strongly.
The draft said that every study in that literature
models South Asia or the United States and Russia.
The largest scenario in fact assumes attacks on seven countries including China,
so the claim is now the narrower and correct one,
that no study models a war between China and the United States
arising from a conflict over Taiwan.
The draft also computed the growth in Ukrainian damage
as a ratio of two rounded figures and reported about 16 percent.
The report states 15.5 percent,
and the unrounded values it prints give that figure,
so the article now uses the source's own number.
The draft further stated Taiwan's grid resilience as unverified and absent.
The commission chapter supplies stockpile durations,
which is not a resilience programme cost,
so the absent item has been narrowed rather than removed.

**Four further corrections came from reading the primaries behind secondary accounts.**
The draft reported Japanese bombing damage from Davis and Weinstein alone.
The bombing survey gives 2,510,000 buildings destroyed against the paper's 2.2 million,
330,000 fatalities against the paper's three hundred thousand,
and, most importantly,
a 40 percent figure that describes built-up area destroyed
rather than a share of population made homeless.
**The draft had additionally inserted the word urban into the paper's sentence**,
producing a claim that matched neither the paper nor the survey.
All three quantities now appear with their subjects and sources attached.

The draft credited Quinlivan's 1995 article
with establishing the 20-per-thousand force ratio.
Reading it shows the article is descriptive
and reaches 20 per thousand as a measured value in two historical cases,
so the article now credits it with the method
and locates the norm in the 2006 field manual,
while recording that the 2014 revision of that manual deleted the ratio.

The draft gave Taiwan's population as about 23.4 million with no source.
That was the end-of-2024 figure.
The official series is now cited,
the calculation uses the end-of-2025 figure,
and the declining trend is stated
along with its small effect on the result.

The draft took a naval balance ratio from a journal author.
The 395 in it is a 2023 departmental projection of what 2025 would hold,
not a count,
and the 2025 edition of that report gives no fleet total at all,
so the ratio is now presented with both quantities dated
and with a second ratio computed from the firmest available numbers.

**One claim was strengthened rather than corrected.**
The draft asserted that no study models nuclear consequences or recovery for this theatre.
Reading the 2025 National Academies report in full confirmed
that it contains no economic recovery analysis and no recovery timescale for human systems,
and that it says so itself by naming the research gap.
The only official study with a recuperation analysis
turns out to be the Office of Technology Assessment's of 1979.

**Not verified and therefore absent.**
Any figure for the Marshall Plan as a share of donor output.
Any estimate of Taiwan's own reconstruction cost,
or any costing of its grid resilience programme,
as distinct from the stockpile durations reported above.
Any figure from three Parameters articles whose publisher refuses automated access.

**Inference.**
The organising claim, that capital stock recovers on a decadal clock
while throughput, production ecosystems and trade relationships do not,
is this article's reading of sources that do not state it in that form.
The four gaps are inferences from a bounded search.

## Out of Scope

- The conduct of the war itself,
which the [previous article][related_post_published_wargames] covers.
- Classified assessments of reconstitution, which exist and are not public.
- Any recommendation about force structure, industrial policy or alliance management.
- The legal questions of occupation, reparations and war crimes adjudication.
- Chinese-language planning literature on reconstruction,
which would require a separate survey.
- A model of recovery of this article's own construction,
which would add assumptions to a subject whose published record is already thin.
- Normative questions about whether any of this should be fought over,
on which this article takes no position.

## Conclusion

The published wargames end at about 21 days and say so.
Read for what happens next,
the record splits in a way neither side of it advertises.

Physical destruction heals faster than intuition expects.
Japanese cities recovered their relative size in about fifteen years
with reconstruction spending contributing under one percentage point.
West German industrial capacity in 1948 stood above its 1936 level,
so what the bombing destroyed was output rather than plant.
The bombing survey had measured the same thing at plant level in 1945,
finding half the floor space of an industry destroyed
and only 12 percent of its machine tools.
Losers of major wars resume antebellum standing within fifteen to twenty years.
Ukraine, assessed while still at war,
shows at most a seventh of its housing gone against a fifth of its output,
and its housing needs run at 1.45 times housing damage
where the whole economy's needs run at three times.

Throughput and relationships do not heal on that clock.
Two shipyards build large surface combatants,
which is the Department of Defense's own count of surface ship primes for 2020,
down from eight in 1990.
A destroyer takes eight to nine years,
and the report that sinks a dozen of them says replacement would take decades.
The Navy states that its shipbuilding budget doubled across two decades
and bought no additional ships.
Carriers have no replacement rate at all,
because the yards can only sustain the fleet that exists.
Munitions run on a 52-month cycle
and the anti-ship missiles the games consume in the first week
are the ones a peer war needs most.
Replacing programme inventories takes 8.4 years at surge rates,
and that figure explicitly excludes combat losses.
Leading-edge semiconductor capacity takes a minimum of three years
and 350 billion dollars to rebuild somewhere else,
and the island those foundries sit on
holds about twenty days of stored gas and about forty days of coal.
Trade between former adversaries is still a fifth below its old level eight years on,
and the modern era repaired itself more slowly than the era before 1938.

The aftermath is therefore not a smaller version of the war.
It is a different problem with different binding constraints,
and the constraint is rarely money.
It is yards, cycles, skilled workers, seed stock, and relationships,
none of which respond to appropriation on the timescale of a crisis.

What the record does not contain is the more useful finding.
No public wargame models the period after the landing or after the failure.
No study examines whether the Chinese state survives losing,
though the most cited report asserts it might not
in the same sentence that disclaims having looked.
No consequence or recovery study exists for nuclear use in this theatre.
And the occupation arithmetic that follows from the literature's own ratio,
about 466,000 personnel for Taiwan and roughly five times that to sustain them,
took minutes to compute and appears in none of it.

**Reading the primary documents rather than the accounts of them
changed the article in one consistent direction.**
Every correction made the secondary literature look more confident than its sources,
and every primary document read here was more candid about its own limits
than the works citing it.
The clearest statement of the whole problem is nearly fifty years old.
A study prepared for the Senate in 1979 said
that the effects which cannot be calculated
"are at least as important as those for which calculations are attempted",
and that nobody knows how to estimate
whether industrial civilisation survives in the areas attacked.
Nothing published since has improved on that,
and the newest authoritative synthesis says as much about itself.

A literature that models the first three weeks in twenty-four iterations
and the following twenty years in one conditional clause
is not describing a war.
It is describing a battle,
and then stopping where the hard part starts.

## References

- [Book, Goemans 2000, War and Punishment][book_goemans_2000_war_and_punishment]
- [Book, Ikenberry 2019, After Victory][book_ikenberry_2019_after_victory]
- [Book, Ikle 2005, Every War Must End][book_ikle_2005_every_war_must_end]
- [Book, Organski and Kugler 1980, The War Ledger][book_organski_kugler_1980_war_ledger]
- [Book, Reiter 2009, How Wars End][book_reiter_2009_how_wars_end]
- [Commentary, Blanchette and McGregor 2026, After the Invasion, China Considers the Problem of Ruling Taiwan][commentary_blanchette_2026_after_invasion]
- [Commentary, Heath 2023, Wargames Cannot Tell Us How to Deter a Chinese Attack on Taiwan][commentary_heath_2023_wargames_deterrence]
- [Commentary, Heim, Burdette and Beauchamp-Mustafaga 2024, Denial Is the Worst Except for All the Others][commentary_heim_2024_denial_worst]
- [Commentary, Sudduth 2026, Double-Edged Swords, How Military Purges Shape Authoritarian Appetite for War][commentary_sudduth_2026_double_edged_swords]
- [Commentary, Tetreau 2023, Where the Wargames Were Not][commentary_tetreau_2023_where_the_wargames_were_not]
- [Commentary, Trevithick 2023, Alarming Navy Intelligence Slide on Chinese Shipbuilding Capacity][commentary_twz_2023_oni_slide]
- [Data, Boston Consulting Group and Semiconductor Industry Association 2021, Strengthening the Global Semiconductor Value Chain][data_bcg_sia_2021_value_chain]
- [Data, Chicago Council on Global Affairs 2022, Thinking Nuclear, South Korean Attitudes on Nuclear Weapons][data_chicago_council_2022_south_korea]
- [Data, Goemans, Gleditsch and Chiozza 2016, Archigos, a Data Set on Leaders 1875 to 2015, Version 4.1][data_archigos_2016_leader_dataset]
- [Data, Office of the United States Trade Representative 2025, Report on China's Targeting of the Maritime, Logistics and Shipbuilding Sectors][data_ustr_2025_maritime]
- [Data, Republic of China Ministry of the Interior 2026, Monthly Bulletin of Interior Statistics, Resident Population][data_moi_2026_taiwan_population]
- [Government, Department of Defense 2022, State of Competition within the Defense Industrial Base][government_dod_2022_competition]
- [Government, Department of Defense 2023, Military and Security Developments Involving the People’s Republic of China][government_dod_2023_china_report]
- [Government, Department of State 1954, Memorandum of Conversation on the Government and Relief in Occupied Areas Claim][government_frus_1954_garioa_bookkeeping]
- [Government, Department of State 1962, Settlement of the United States Claim for Postwar Economic Assistance to Japan][government_frus_1962_garioa_settlement]
- [Government, Department of the Army and United States Marine Corps 2006, FM 3-24, Counterinsurgency][government_fm_3_24_2006]
- [Government, Department of the Navy 2026, United States Navy Shipbuilding Plan, Fiscal Year 2027][government_navy_2026_shipbuilding_plan]
- [Government, Economic Cooperation Administration 1951, Thirteenth Report to Congress][government_eca_1951_thirteenth_report]
- [Government, Glasstone and Dolan 1977, The Effects of Nuclear Weapons, Third Edition, TID-28061][government_glasstone_dolan_1977]
- [Government, Joint Chiefs of Staff 2018, Joint Publication 3-0, Joint Operations][government_jp_3_0_2018]
- [Government, Office of Technology Assessment 1979, The Effects of Nuclear War][government_ota_1979_effects_of_nuclear_war]
- [Government, Office of the Director of National Intelligence 2026, Annual Threat Assessment][government_odni_2026_threat_assessment]
- [Government, United States Congress 1948, Economic Cooperation Act of 1948, 62 Stat. 137][government_economic_cooperation_act_1948]
- [Government, United States Strategic Bombing Survey 1945, Over-all Report, European War][government_ussbs_1945_overall_report]
- [Government, United States Strategic Bombing Survey 1946, Summary Report, Pacific War][government_ussbs_1946_pacific_summary]
- [Government, US-China Economic and Security Review Commission 2025, Annual Report to Congress, Taiwan Chapter][government_uscc_2025_taiwan_chapter]
- [Journal, Brakman, Garretsen and Schramm 2004, The Strategic Bombing of German Cities, Journal of Economic Geography 4 number 2][journal_brakman_2004_german_bombing]
- [Journal, Bueno de Mesquita, Siverson and Woller 1992, War and the Fate of Regimes, American Political Science Review 86 number 3][journal_bueno_de_mesquita_1992]
- [Journal, Caverley 2025, So What, Texas National Security Review 8 number 3][journal_caverley_2025]
- [Journal, Chan and others 2025, Resilience Reconsidered, International Journal of Disaster Risk Science 16 number 4][journal_chan_2025_resilience]
- [Journal, Croco 2011, The Decider's Dilemma, American Political Science Review 105 number 3][journal_croco_2011]
- [Journal, Davis and Weinstein 2002, Bones, Bombs, and Break Points, American Economic Review 92 number 5][journal_davis_weinstein_2002]
- [Journal, Debs and Goemans 2010, Regime Type, the Fate of Leaders, and War, American Political Science Review 104 number 3][journal_debs_goemans_2010]
- [Journal, Eichengreen and Ritschl 2009, Understanding West German Economic Growth in the 1950s, Cliometrica 3 number 3][journal_eichengreen_ritschl_2009]
- [Journal, Federle and others 2026, The Price of War, American Economic Review 116 number 3][journal_federle_2026_price_of_war]
- [Journal, Flavin 2003, Planning for Conflict Termination and Post-Conflict Success, Parameters 33 number 3][journal_flavin_2003_conflict_termination]
- [Journal, Fravel 2005, Regime Insecurity and International Cooperation, International Security 30 number 2][journal_fravel_2005_regime_insecurity]
- [Journal, Glick and Taylor 2010, Collateral Damage, Review of Economics and Statistics 92 number 1][journal_glick_taylor_2010]
- [Journal, Goemans 2008, Which Way Out, Journal of Conflict Resolution 52 number 6][journal_goemans_2008_which_way_out]
- [Journal, Goemans, Gleditsch and Chiozza 2009, Introducing Archigos, Journal of Peace Research 46 number 2][journal_goemans_2009_archigos]
- [Journal, Green and Talmadge 2022, Then What, International Security 47 number 1][journal_green_talmadge_2022]
- [Journal, Jehn and others 2025, Food Trade Disruption After Global Catastrophes, Earth System Dynamics 16 number 5][journal_jehn_2025_food_trade]
- [Journal, Koubi 2005, War and Economic Performance, Journal of Peace Research 42 number 1][journal_koubi_2005]
- [Journal, Lee, Chen and Chen 2024, Core Public Attitudes toward Defense and Security in Taiwan, Taiwan Politics][journal_lee_2024_taiwan_attitudes]
- [Journal, Miguel and Roland 2011, The Long-Run Impact of Bombing Vietnam, Journal of Development Economics 96 number 1][journal_miguel_roland_2011]
- [Journal, Miguel and Roland 2024, Corrigendum to The Long-Run Impact of Bombing Vietnam, Journal of Development Economics 166][journal_miguel_roland_2024_corrigendum]
- [Journal, Nemeth 2026, How a United States Suez Moment Could Hollow the Alliance System, Texas National Security Review 9 number 1][journal_nemeth_2026_suez_moment]
- [Journal, Nguyen and others 2025, Second World War Bombing and the German City System, Global Challenges and Regional Science 1][journal_nguyen_2025_german_cities]
- [Journal, Organski and Kugler 1977, The Costs of Major Wars, the Phoenix Factor, American Political Science Review 71 number 4][journal_organski_kugler_1977]
- [Journal, Quek and Johnston 2018, Can China Back Down, International Security 42 number 3][journal_quek_johnston_2018]
- [Journal, Reisner and others 2018, Climate Impact of a Regional Nuclear Weapons Exchange, Journal of Geophysical Research Atmospheres 123 number 5][journal_reisner_2018]
- [Journal, Robock, Toon and Bardeen 2019, Comment on Climate Impact of a Regional Nuclear Weapon Exchange, Journal of Geophysical Research Atmospheres 124 number 23][journal_robock_2019_comment]
- [Journal, Shi and others 2025, Adapting Agriculture to Climate Catastrophes, Environmental Research Letters 20 number 6][journal_shi_2025_adapting_agriculture]
- [Journal, Stanley and Sawyer 2009, The Equifinality of War Termination, Journal of Conflict Resolution 53 number 5][journal_stanley_sawyer_2009]
- [Journal, Xia and others 2015, Decadal Reduction of Chinese Agriculture After a Regional Nuclear War, Earth's Future 3 number 2][journal_xia_2015_chinese_agriculture]
- [Journal, Xia and others 2022, Global Food Insecurity and Famine From Nuclear War Soot Injection, Nature Food 3 number 8][journal_xia_2022_nature_food]
- [Related Post, Industrialization Waves and Geopolitical Positioning, China's Rise][related_post_china_rise]
- [Related Post, Industrialization Waves and Geopolitical Positioning, Postwar Japan and West Germany][related_post_postwar_japan_germany]
- [Related Post, What Published Wargames Say About a War With China][related_post_published_wargames]
- [Research, Beauchamp-Mustafaga and others 2024, Denial Without Disaster, Volume 3][research_beauchamp_2024_denial_without_disaster_v3]
- [Research, Buddemeier and Dillon 2009, Key Response Planning Factors for the Aftermath of Nuclear Terrorism][research_buddemeier_2009_response_planning]
- [Research, Cancian and others 2021, Industrial Mobilization, Assessing Surge Capabilities and System Brittleness][research_cancian_2021_industrial_mobilization]
- [Research, Cancian and Park 2026, Last Rounds, Status of Key Munitions at the Iran War Ceasefire][research_cancian_2026_last_rounds]
- [Research, Cancian and Park 2026, Rebuilding United States Missile Inventory, a Multiyear Project][research_cancian_2026_missile_rebuild]
- [Research, Cancian and Park 2026, Six Reasons Why the United States Is Low on Munitions][research_cancian_2026_six_reasons]
- [Research, Cancian, Cancian and Heginbotham 2023, The First Battle of the Next War][research_cancian_2023_first_battle]
- [Research, De Long and Eichengreen 1991, The Marshall Plan, History's Most Successful Structural Adjustment Program][research_delong_eichengreen_1991_marshall]
- [Research, Evans 2023, Alternative Futures Following a Great Power War, Volume 2][research_evans_2023_alternative_futures_v2]
- [Research, Funaiole 2026, Testimony on Countering Chinese Dominance in Global Shipbuilding][research_funaiole_2026_testimony]
- [Research, Garlauskas, Gilbert and Imai 2025, A Rising Nuclear Double-Threat in East Asia][research_garlauskas_2025_guardian_tiger]
- [Research, General Accounting Office 1998, Defense Industry, Consolidation and Options for Preserving Competition][research_gao_1998_defense_consolidation]
- [Research, Gompert, Cevallos and Garafola 2016, War with China, Thinking Through the Unthinkable][research_gompert_2016_war_with_china]
- [Research, Government Accountability Office 2022, Defense Industrial Base, DOD Should Take Actions to Strengthen Its Risk Mitigation Approach][research_gao_2022_industrial_base]
- [Research, Government Accountability Office 2025, Shipbuilding and Repair, Private Sector Industrial Base Investments][research_gao_2025_shipbuilding_workforce]
- [Research, Gunzinger and Penney 2026, Rebuilding America's Air Force][research_gunzinger_2026_rebuilding_air_force]
- [Research, Jones 2023, Empty Bins in a Wartime Environment][research_jones_2023_empty_bins]
- [Research, Krepinevich 2020, Protracted Great-Power War, a Preliminary Assessment][research_krepinevich_2020_protracted_great_power_war]
- [Research, Labs 2025, The Navy's 2025 Shipbuilding Plan and the Shipbuilding Industrial Base][research_labs_2025_cbo_shipbuilding]
- [Research, McGregor and Blanchette 2026, After Annexation, How China Plans to Run Taiwan][research_mcgregor_2026_after_annexation]
- [Research, National Academies 2025, Potential Environmental Effects of Nuclear War][research_nas_2025_nuclear_war_effects]
- [Research, O'Rourke 2026, Navy Virginia-Class Submarine Program][research_orourke_2026_virginia_class]
- [Research, Oakley 2026, Navy and Coast Guard Shipbuilding, a Strategy-Driven Approach Is Needed][research_oakley_2026_gao_shipbuilding]
- [Research, Predd and others 2025, Thinking Through Protracted War with China, Nine Scenarios][research_predd_2025_protracted_war]
- [Research, Priebe and others 2023, Alternative Futures Following a Great Power War, Volume 1][research_priebe_2023_alternative_futures_v1]
- [Research, Quinlivan 1995, Force Requirements in Stability Operations, Parameters 25][research_quinlivan_1995_force_requirements]
- [Research, Quinlivan 2003, Burden of Victory, the Painful Arithmetic of Stability Operations][research_quinlivan_2003_burden_of_victory]
- [Research, Rumbaugh 2026, Solid Rocket Motors for Missile Defense][research_rumbaugh_2026_solid_rocket_motors]
- [Research, Special Inspector General for Iraq Reconstruction 2013, Learning From Iraq][research_sigir_2013_learning_from_iraq]
- [Research, Stewart 2023, Island Blitz, a Campaign Analysis of a Taiwan Takeover][research_stewart_2023_island_blitz]
- [Research, Tarnoff 2018, The Marshall Plan, Design, Accomplishments, and Significance][research_tarnoff_2018_marshall_plan]
- [Research, World Bank 1996, Bosnia and Herzegovina, the Priority Reconstruction and Recovery Program][research_world_bank_1996_bosnia]
- [Research, World Bank, Government of Ukraine, European Commission and United Nations 2025, Ukraine Fourth Rapid Damage and Needs Assessment, February 2022 to December 2024][research_world_bank_2025_rdna4]

[book_goemans_2000_war_and_punishment]: https://doi.org/10.1515/9781400823956
[book_ikenberry_2019_after_victory]: https://doi.org/10.23943/princeton/9780691169217.001.0001
[book_ikle_2005_every_war_must_end]: https://cup.columbia.edu/book/every-war-must-end/9780231136679
[book_organski_kugler_1980_war_ledger]: https://doi.org/10.7208/chicago/9780226351841.001.0001
[book_reiter_2009_how_wars_end]: https://doi.org/10.1515/9781400831036
[commentary_blanchette_2026_after_invasion]: https://warontherocks.com/after-the-invasion-china-considers-the-problem-of-ruling-taiwan/
[commentary_heath_2023_wargames_deterrence]: https://www.rand.org/pubs/external_publications/EP70064.html
[commentary_heim_2024_denial_worst]: https://warontherocks.com/2024/06/denial-is-the-worst-except-for-all-the-others-getting-the-u-s-theory-of-victory-right-for-a-war-with-china/
[commentary_sudduth_2026_double_edged_swords]: https://warontherocks.com/double-edged-swords-how-military-purges-shape-authoritarian-appetite-for-war/
[commentary_tetreau_2023_where_the_wargames_were_not]: https://warontherocks.com/2023/09/where-the-wargames-werent-assessing-10-years-of-u-s-chinese-military-assessments/
[commentary_twz_2023_oni_slide]: https://www.twz.com/alarming-navy-intel-slide-warns-of-chinas-200-times-greater-shipbuilding-capacity
[data_archigos_2016_leader_dataset]: http://ksgleditsch.com/archigos.html
[data_bcg_sia_2021_value_chain]: https://www.semiconductors.org/wp-content/uploads/2021/05/BCG-x-SIA-Strengthening-the-Global-Semiconductor-Value-Chain-April-2021_1.pdf
[data_chicago_council_2022_south_korea]: https://globalaffairs.org/research/public-opinion-survey/thinking-nuclear-south-korean-attitudes-nuclear-weapons
[data_moi_2026_taiwan_population]: https://statis.moi.gov.tw/micst/report/321010.xlsx
[data_ustr_2025_maritime]: https://ustr.gov/sites/default/files/enforcement/301Investigations/USTRReportChinaTargetingMaritime.pdf
[government_dod_2022_competition]: https://web.archive.org/web/20240102044927/https://media.defense.gov/2022/Feb/15/2002939087/-1/-1/1/STATE-OF-COMPETITION-WITHIN-THE-DEFENSE-INDUSTRIAL-BASE.PDF
[government_dod_2023_china_report]: https://web.archive.org/web/2024/https://media.defense.gov/2023/Oct/19/2003323409/-1/-1/1/2023-MILITARY-AND-SECURITY-DEVELOPMENTS-INVOLVING-THE-PEOPLES-REPUBLIC-OF-CHINA.PDF
[government_eca_1951_thirteenth_report]: https://www.govinfo.gov/content/pkg/SERIALSET-11551_00_00-005-0249-0000/pdf/SERIALSET-11551_00_00-005-0249-0000.pdf
[government_economic_cooperation_act_1948]: https://www.govinfo.gov/content/pkg/STATUTE-62/pdf/STATUTE-62-Pg137.pdf
[government_fm_3_24_2006]: https://archive.org/download/FugitiveDistro_FM_3_24_Counterinsurgency_Anonymous/FM%203%2024%20Counterinsurgency_READ_EN_282.pdf
[government_frus_1954_garioa_bookkeeping]: https://history.state.gov/historicaldocuments/frus1952-54v14p2/d712
[government_frus_1962_garioa_settlement]: https://history.state.gov/historicaldocuments/frus1961-63v22/d353
[government_glasstone_dolan_1977]: https://doi.org/10.2172/6852629
[government_jp_3_0_2018]: https://web.archive.org/web/20200113010443id_/https://www.jcs.mil/Portals/36/Documents/Doctrine/pubs/jp3_0ch1.pdf
[government_navy_2026_shipbuilding_plan]: https://www.secnav.navy.mil/fmc/fmb/Documents/27pres/30%20Year%20Shipbuilding%20Plan.pdf
[government_odni_2026_threat_assessment]: https://archive.dni.gov/files/ODNI/documents/assessments/ATA-2026-Unclassified-Report.pdf
[government_ota_1979_effects_of_nuclear_war]: https://ia801509.us.archive.org/13/items/effectsofnuclear00unit/effectsofnuclear00unit.pdf
[government_uscc_2025_taiwan_chapter]: https://www.uscc.gov/sites/default/files/2025-11/Chapter_11--Taiwan.pdf
[government_ussbs_1945_overall_report]: https://books.google.com/books?id=4PBmAAAAMAAJ
[government_ussbs_1946_pacific_summary]: https://archive.org/download/summaryreportpac00unit/summaryreportpac00unit.pdf
[journal_brakman_2004_german_bombing]: https://doi.org/10.1093/jeg/4.2.201
[journal_bueno_de_mesquita_1992]: https://doi.org/10.2307/1964127
[journal_caverley_2025]: https://doi.org/10.1353/tns.00004
[journal_chan_2025_resilience]: https://doi.org/10.1007/s13753-025-00657-y
[journal_croco_2011]: https://doi.org/10.1017/S0003055411000219
[journal_davis_weinstein_2002]: https://doi.org/10.1257/000282802762024502
[journal_debs_goemans_2010]: https://doi.org/10.1017/S0003055410000195
[journal_eichengreen_ritschl_2009]: https://doi.org/10.1007/s11698-008-0035-7
[journal_federle_2026_price_of_war]: https://doi.org/10.1257/aer.20241355
[journal_flavin_2003_conflict_termination]: https://doi.org/10.55540/0031-1723.2162
[journal_fravel_2005_regime_insecurity]: https://doi.org/10.1162/016228805775124534
[journal_glick_taylor_2010]: https://doi.org/10.1162/rest.2009.12023
[journal_goemans_2008_which_way_out]: https://doi.org/10.1177/0022002708323316
[journal_goemans_2009_archigos]: https://doi.org/10.1177/0022343308100719
[journal_green_talmadge_2022]: https://doi.org/10.1162/isec_a_00437
[journal_jehn_2025_food_trade]: https://doi.org/10.5194/esd-16-1585-2025
[journal_koubi_2005]: https://doi.org/10.1177/0022343305049667
[journal_lee_2024_taiwan_attitudes]: https://doi.org/10.58570/WRON8266
[journal_miguel_roland_2011]: https://doi.org/10.1016/j.jdeveco.2010.07.004
[journal_miguel_roland_2024_corrigendum]: https://doi.org/10.1016/j.jdeveco.2023.103151
[journal_nemeth_2026_suez_moment]: https://doi.org/10.1353/tns.00025
[journal_nguyen_2025_german_cities]: https://doi.org/10.1016/j.gcrs.2025.100004
[journal_organski_kugler_1977]: https://doi.org/10.2307/1961484
[journal_quek_johnston_2018]: https://doi.org/10.1162/isec_a_00303
[journal_reisner_2018]: https://doi.org/10.1002/2017JD027331
[journal_robock_2019_comment]: https://doi.org/10.1029/2019JD030777
[journal_shi_2025_adapting_agriculture]: https://doi.org/10.1088/1748-9326/adcfb5
[journal_stanley_sawyer_2009]: https://doi.org/10.1177/0022002709343194
[journal_xia_2015_chinese_agriculture]: https://doi.org/10.1002/2014EF000283
[journal_xia_2022_nature_food]: https://doi.org/10.1038/s43016-022-00573-0
[related_post_china_rise]: {% post_url 2026-03-23-china_rise %}
[related_post_postwar_japan_germany]: {% post_url 2026-03-21-postwar_japan_and_west_germany %}
[related_post_published_wargames]: {% post_url 2026-08-11-published_wargames_of_war_with_china %}
[research_beauchamp_2024_denial_without_disaster_v3]: https://www.rand.org/pubs/research_reports/RRA2312-3.html
[research_buddemeier_2009_response_planning]: https://www.osti.gov/servlets/purl/966550
[research_cancian_2021_industrial_mobilization]: https://csis-website-prod.s3.amazonaws.com/s3fs-public/publication/210108_Cancian_Industrial_Mobilization.pdf
[research_cancian_2023_first_battle]: https://csis-website-prod.s3.amazonaws.com/s3fs-public/publication/230109_Cancian_FirstBattle_NextWar.pdf
[research_cancian_2026_last_rounds]: https://www.csis.org/analysis/last-rounds-status-key-munitions-iran-war-ceasefire
[research_cancian_2026_missile_rebuild]: https://www.csis.org/analysis/rebuilding-us-missile-inventory-multiyear-project
[research_cancian_2026_six_reasons]: https://www.csis.org/analysis/six-reasons-why-united-states-low-munitions
[research_delong_eichengreen_1991_marshall]: https://www.nber.org/system/files/working_papers/w3899/w3899.pdf
[research_evans_2023_alternative_futures_v2]: https://www.rand.org/pubs/research_reports/RRA591-2.html
[research_funaiole_2026_testimony]: https://docs.house.gov/meetings/FA/FA05/20260722/119432/HHRG-119-FA05-Wstate-FunaioleM-20260722.pdf
[research_gao_1998_defense_consolidation]: https://web.archive.org/web/2024/https://www.gao.gov/assets/nsiad-98-141.pdf
[research_gao_2022_industrial_base]: https://web.archive.org/web/2024/https://www.gao.gov/assets/gao-22-104154.pdf
[research_gao_2025_shipbuilding_workforce]: https://files.gao.gov/reports/GAO-25-106286/index.html
[research_garlauskas_2025_guardian_tiger]: https://www.atlanticcouncil.org/in-depth-research-reports/report/a-rising-nuclear-double-threat-in-east-asia-insights-from-our-guardian-tiger-i-and-ii-tabletop-exercises/
[research_gompert_2016_war_with_china]: https://www.rand.org/content/dam/rand/pubs/research_reports/RR1100/RR1140/RAND_RR1140.pdf
[research_gunzinger_2026_rebuilding_air_force]: https://www.mitchellaerospacepower.org/app/uploads/2026/04/Rebuilding-Americas-Air-Force-FINAL.pdf
[research_jones_2023_empty_bins]: https://csis-website-prod.s3.amazonaws.com/s3fs-public/2023-01/230119_Jones_Empty_Bins.pdf
[research_krepinevich_2020_protracted_great_power_war]: https://www.cnas.org/publications/reports/protracted-great-power-war
[research_labs_2025_cbo_shipbuilding]: https://www.cbo.gov/publication/61218
[research_mcgregor_2026_after_annexation]: https://www.lowyinstitute.org/publications/after-annexation-how-china-plans-run-taiwan
[research_nas_2025_nuclear_war_effects]: https://doi.org/10.17226/27515
[research_oakley_2026_gao_shipbuilding]: https://files.gao.gov/reports/GAO-26-109068/index.html
[research_orourke_2026_virginia_class]: https://www.everycrsreport.com/reports/RL32418.html
[research_predd_2025_protracted_war]: https://www.rand.org/pubs/research_reports/RRA1475-1.html
[research_priebe_2023_alternative_futures_v1]: https://www.rand.org/pubs/research_reports/RRA591-1.html
[research_quinlivan_1995_force_requirements]: https://doi.org/10.55540/0031-1723.1751
[research_quinlivan_2003_burden_of_victory]: https://www.rand.org/content/dam/rand/pubs/corporate_pubs/2007/RAND_CP22-2003-08.pdf
[research_rumbaugh_2026_solid_rocket_motors]: https://csis-website-prod.s3.amazonaws.com/s3fs-public/2026-06/260612_Rumbaugh_Rocket_Motors.pdf
[research_sigir_2013_learning_from_iraq]: https://web.archive.org/web/20131104045644id_/http://www.sigir.mil/files/learningfromiraq/Report_-_March_2013.pdf
[research_stewart_2023_island_blitz]: https://cimsec.org/island-blitz-a-campaign-analysis-of-a-taiwan-takeover-by-the-pla/
[research_tarnoff_2018_marshall_plan]: https://www.everycrsreport.com/reports/R45079.html
[research_world_bank_1996_bosnia]: https://documents.worldbank.org/curated/en/998241468743939643/pdf/multi0page.pdf
[research_world_bank_2025_rdna4]: https://documents.worldbank.org/curated/en/099022025114040022/pdf/P1801741ca39ec0d81b5371ff73a675a0a8.pdf
