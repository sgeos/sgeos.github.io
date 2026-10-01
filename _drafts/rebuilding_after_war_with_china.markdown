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
The most cited of them stop within about three weeks of the first shot,
and the most detailed public campaign model runs to day 46
and stops at the seizure of Taipei.
**No public game located for this article continues into the period it is about.**
That absence is set out with its bounds in the gaps section below.
The wars they model would not stop where the games do.

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
It then surveys the wider literature behind those sections,
sets out the places where the sources agree and the places where they contradict one another,
and records where the record is empty,
because five of the gaps are large enough to count as results in their own right.

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

**What organised this article was not what was expected at the outset.**
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
and that passage carries more of the public record's weight on the aftermath
than anything else located for this article.

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
and the Navy states it more plainly than any other source quoted here.**
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
Taking the midpoints of the budget office's two build-duration brackets,
five to six years in the 2000s against eight to nine now,
duration has lengthened by half again within a generation.

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
The [Office of the United States Trade Representative's report][data_ustr_2025_maritime]
on its Section 301 investigation
into China's targeting of the maritime, logistics and shipbuilding sectors,
which the section on asymmetry below returns to,
draws on a Maritime Administration fact sheet
recording that in 2023 the United States shipbuilding industry
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

**The premise underneath that analogy has itself been attacked,
and the attack is quantitative.**
The usual reason for expecting mobilisation to go well
is learning by doing in the production of military durables.
[Field 2023][journal_field_2023_manufacturing_productivity]
measures what actually happened to American manufacturing productivity
and finds the opposite of the premise.
Total factor productivity in the sector
"fell at a rate of −1.4 per cent per year between 1941 and 1948,
−3.7 per cent a year between 1941 and 1944,
and −5.1 per cent a year between 1941 and 1945".
Compounding the slowest of those rates across its own seven-year window
gives the cumulative fall.

$$
(1 - 0.014)^{7} \approx 0.906
$$

**Manufacturing productivity was about nine percent lower in 1948 than in 1941**,
which is the article's own compounding of a rate the paper states annually.
Field attributes the loss to "the sudden, radical, and temporary changes
in the product mix",
to "the behavioural pathologies accompanying the transition to a shortage economy",
and to resource shocks.
If the canonical mobilisation succeeded while productivity fell,
then the analogy supports a conclusion about brute scale
and not one about getting better at building things under pressure.

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

The Navy confirmed the slide's authenticity and simultaneously limited it.
Its statement calls China the People's Republic of China,
abbreviated there to PRC,
and says the slide was "developed by the Office of Naval Intelligence from multiple public sources
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
The [Section 301 report][data_ustr_2025_maritime]
introduced in the workforce section above
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
**The two figures are easy to merge and the merger is wrong in a specific way.**
The survey states one 40 percent and one 30 percent,
the first about built-up area and the second about the urban population.
Attaching the word urban to the 40 percent
produces a sentence that reads like a quotation from either source
and corresponds to neither.
Forty percent of built-up area destroyed
and thirty percent of the urban population made homeless
are both survey findings.
Forty percent of a population made homeless is not one.

The recovery result is a regression coefficient of $-1.0$
on prior-period growth,
which means full mean reversion.
"The typical city completely recovered its former relative size
within 15 years following the end of World War II."
Reconstruction spending was not the mechanism,
contributing under one percentage point
against cumulative city growth of 55 to 96 percent.

Two qualifications belong with that result and are usually dropped.
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
which is more than half a century before the econometrics reached it.**
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

**Two wars, measured by the same organisation, give the same shape,
and the Pacific report supplies the mechanism.**
It records that "Machine tools and most other production equipment
in industrial plants were not directly damaged by the blast wave,
but were damaged by collapsing buildings or ensuing general fires".
The tools are harder to destroy than the structures around them,
and they are lost only when the structure falls on them or the fire reaches them.
Across both theatres the pattern is therefore the same.
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
The result is citable and it should never be cited without the correction.
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

The fifteen-year city result and the fifteen to twenty year power result
were reached by entirely different methods on different units of analysis,
and they agree.
That convergence is the firmest quantitative footing
anything in the recovery literature read here stands on.

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
It is very slow by the standards of a war the most cited games end in three weeks,
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
In the commission's own wording,
natural gas supplied 42 percent of Taiwan's energy in 2024
against a target of 50 percent by 2030,
and the last nuclear plant shut in May 2025.
The commission records what that closure traded away,
noting that earthquake and accident concerns outweighed
"nuclear's value as a domestic power supply
that can mitigate risk of disruptions to imports".

**The electorate has since moved and the institutions have not.**
A national referendum on 23 August 2025 asked whether the Maanshan plant should restart.
The [Central Election Commission's results][data_roc_cec_referendums]
record 4,341,432 votes in favour against 1,511,693 opposed,
which is 74.17 percent in favour on a turnout of 29.53 percent.
**It failed.**
The Referendum Act requires affirmative votes to reach a quarter of eligible voters,
a threshold of 5,000,523 against an electorate of 20,002,091.

$$
5{,}000{,}523 - 4{,}341{,}432 = 659{,}091 \ \text{votes short}
$$

A proposal carried by nearly three to one
fell about 659,000 votes short of a participation threshold,
so the island's energy exposure is now a function of turnout rules
rather than of public preference.
The share of supply is therefore rising toward the fuel
that the same chapter says is held for twenty days.

Set the gas figure against the horizon established at the top of this article.
Writing $T_g$ for the modelled horizon,
$T_{\text{LNG}}$ for the days of liquefied natural gas held
and $T_{\text{coal}}$ for the days of coal,
the two comparisons follow.

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

**The provenance of the twenty-day figure needs stating,
because it is weaker than it first appears.**
A search of Taiwan's own energy statistics for this article
found no published stockpile day-count for natural gas or coal.
The Energy Administration publishes import dependence, fuel shares and reserve margins,
and Taiwan Power's coal pages speak of maintaining an appropriate safety inventory
without giving a number of days.
**The twenty and forty-two day figures are therefore the commission's,
carried in its own footnotes,
and not statistics the Taiwanese government publishes in that form.**
They are reported here because a congressional commission is a serious source
and because nothing better was located,
and they should be read as its characterisation rather than as an official series.

**One stockpile is statutory and it is the wrong one.**
Article 24 of the [Petroleum Administration Act][government_roc_petroleum_act]
requires refiners and importers to hold not less than 60 days
of the previous twelve months' average domestic sales,
with the government holding a further 30 days through the Petroleum Fund.

$$
60 + 30 = 90 \ \text{days of statutory petroleum stock}
$$

**Petroleum has a 90-day statutory reserve.
The fuel the island is moving toward has none**,
and the only figure available for it is a commission's twenty days.
A game that stops at 21 days stops before the energy question becomes binding,
and every reconstruction estimate in this article
assumes electricity is available to do the rebuilding.
Coal buys twice the horizon and no more,
and a rationed grid is not a grid that runs leading-edge lithography.

**Food has its own horizon and it is longer than the energy one.**
[Ferreira and Critelli 2023][journal_ferreira_critelli_2023_food_resiliency]
report that Taiwan's food stocks, rice excepted,
could endure trade disruption for only six months,
and identify which products a resupply operation would have to carry first.
Taiwan's own agriculture ministry puts the food self-sufficiency ratio
at 30.36 percent on a calorie basis for 2025,
against 57.16 percent measured by value.

$$
\frac{57.16}{30.36} \approx 1.88
$$

**The island is nearly twice as self-sufficient in the value of its food
as in the calories of it**, which is what an export-oriented agriculture looks like
and is the wrong way round for a siege.
Set the three horizons together.
Gas runs about 20 days, coal about 42, and food about 180.

$$
20 : 42 : 180
$$

**The binding constraint in a long blockade is energy and not food**,
which inverts the intuition that a besieged island starves,
and which matters because the reconstruction literature prices neither.

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
That is this article's thesis at the smallest scale
at which this article found it tested,
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

The era comparison cuts against the intuition the rest of the section builds.
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
which abbreviates its own name to ECA,
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
It is the only case this article located
in which a damaged economy still at war
has been costed sector by sector by its eventual funders.
Direct damage reached 176.1 billion dollars,
and total reconstruction and recovery needs estimated over ten years reached 524.6 billion,
which the assessment puts at "approximately 2.8 times the estimated nominal
GDP of Ukraine for 2024".
Needs exceed measured damage by a factor near three,
because recovery is not the same thing as repair.

$$
\frac{524.6}{176.1} \approx 2.98
$$

That ratio travels between cases better than any other quantity here,
because it is dimensionless.

$$
\frac{\text{reconstruction needs}}{\text{annual output}} \approx 2.8
$$

**The sector detail is where the assessment speaks to the thesis above.**
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
the Special Inspector General for Iraq Reconstruction,
which signs itself SIGIR,
[recorded in its 2013 final report][research_sigir_2013_learning_from_iraq]
60.64 billion dollars of United States relief and reconstruction funding for Iraq
across nine years,
averaging more than 15 million dollars a day,
with at least 8 billion judged wasted.
Expenditure of 53.26 billion dollars across nine years gives the daily rate.

$$
\frac{53.26 \times 10^{9}}{9 \times 365} \approx 16.2 \ \text{million dollars per day}
$$

**Occupation-era aid to Japan is quantified in the official record
and is rarely quoted from it.**
A [State Department paper of March 1962][government_frus_1962_garioa_settlement],
published in the Foreign Relations of the United States series,
records that total disbursements to Japan
under the Government and Relief in Occupied Areas appropriations,
abbreviated in the official record to GARIOA,
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
Taiwan's own reconstruction has no published estimate that this article could find,
which is set out below as one of the gaps.

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
show that rational updating during a war
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
which is precisely the handoff that no source in this article prices.

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

The claim about the aftermath that circulates most widely
is that a failed invasion would threaten Communist Party rule.
Its source is the CSIS report,
which abbreviates the Chinese Communist Party to CCP,
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
Exits were 64.63 percent regular and 19.07 percent irregular,
and post-tenure fates were 63.64 percent no punishment,
12.43 percent exile,
5.09 percent imprisonment
and 3.83 percent death.
The exit categories in that paper sum as they should,
which is the check the previous figures invite.

$$
64.63 + 19.07 + 6.08 + 1.98 + 0.17 + 2.38 + 5.59 + 0.10 = 100.00
$$

The [dataset behind that paper][data_archigos_2016_leader_dataset]
has since been extended,
version 4.1 of March 2016 covering 1875 to the end of 2015,
and its authors ask that the version and date be cited alongside the article.
**The rates above are the published ones
and were not recomputed from the current file**,
so they describe the 1875 to 2004 window and not the longer one.

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
the one China-specific empirical result located points toward compromise,
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
writes counterinsurgency as COIN
and area of operations as AO.
It states at paragraph 1-67 that "Most density recommendations fall within a range
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

**This calculation is the article's own and appears in no source located.**
It applies a ratio derived from Bosnia, Kosovo, Somalia, Haiti, Afghanistan and Iraq
to a case none of those resembles,
and it assumes a garrison model rather than a compliant population.
It is offered as the order of magnitude the published literature implies,
and as evidence that the two bodies of work have never been joined.

Two comparisons put that figure in proportion.
Against the invasion force in the most detailed public campaign model located,
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
report willingness to fight between 68 and 75 percent across five survey waves.
**That number should not be used without the measurement literature attached.**
[Lai and others 2026][journal_lai_2026_lost_in_words]
run survey experiments in Taiwan and find
a value frame raises stated willingness to fight while a cost frame lowers it,
and report that military recruits are *less* willing to fight than civilians,
which they attribute to greater awareness of the costs.
[Fu, Yin and Han 2024][journal_fu_2024_human_cost_of_war]
find support for military action falling faster
with Chinese civilian casualties than with Taiwanese military losses.
**Willingness to fight is an artefact of question wording to a degree
that a single percentage cannot carry**,
and this article uses it only as a range.
On the independence question,
[Blanchette and McGregor 2026][commentary_blanchette_2026_after_invasion]
report that about 7 percent of Taiwanese adults,
roughly 1.3 million people,
support immediate independence.

[McGregor and Blanchette 2026][research_mcgregor_2026_after_annexation]
is the most developed treatment of how Beijing would govern the island
that this article located,
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
The paper is open access,
so every figure below is taken from its first table directly.
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

The ratio between the direct and the indirect toll carries the argument.

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

**The same paper carries a second table that the accounts of it consulted here
do not reproduce, and it is the one that bears on this article.**
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

**The science is contested at the fire-physics end rather than the climate end,
and the dissenting paper says so itself.**
[Reisner and others 2018][journal_reisner_2018]
modelled the fireball, the firestorm and the Earth system together
for the same India and Pakistan exchange the earlier work assumed.
Their climate result is not the disagreement.
When their Earth system model is started with the assumed soot load aloft,
"the impact on climate variables such as global temperature and precipitation
in our simulations is similar to that predicted by previously published work".
The disagreement is upstream of that.
Their firestorm simulations produce about 3.7 billion kilograms of black carbon
against the 5 billion the earlier scenario injects,
and, far more consequentially,
"the vast majority of the black carbon never reaches an altitude above weather systems".

$$
\frac{3.7}{5.0} = 0.74
$$

A quarter less soot produced would matter little.
Soot that stays below the weather matters entirely,
because rain removes it.

[Robock, Toon and Bardeen 2019][journal_robock_2019_comment]
reply that the smaller plume is an artefact of the fire model rather than a finding.
They object that the target area chosen was "suburban Atlanta
that includes a golf course, playground, and individual houses with large yards,
with little material to burn,
which is not representative of densely populated cities in India and Pakistan",
that the winds used were "stronger than typical winds",
that moist convection was excluded,
and that the fire model "has not been shown to accurately simulate firestorms
observed in Hamburg, Dresden, and Hiroshima during World War II".
**Every one of those objections is about how much soot is lofted and how high,
and none is about what the climate does once it is there.**
The contested step is the fuel and the plume,
and the National Academies report puts the difficulty in the same place.
It records that "The amount of smoke produced from urban fires varies between studies
based on assumptions about burnable material and fire characteristics",
and that "challenges remain in predicting
whether fires will inject soot into the upper troposphere".
**Two groups of modellers and an independent committee
all put the uncertainty at the same step**,
which makes the disagreement a tractable scientific question
rather than a standoff between schools.
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

**The report contains no economic recovery analysis
and no recovery timescale for human systems.**
What it offers on recovery is a physical result,
that in the largest simulation "ocean recovery from the conflict
is decades at the surface and hundreds of years at depth",
and a research gap,
that "There are major research gaps around quantifying the impacts
of abrupt cooling and environmental shocks on crop yields, livestock, fisheries,
pollution exposure pathways, and ecosystem recovery timelines".
The newest synthesis in the field
therefore does not answer the question this article is asking,
and says as much.

### The government study that did model recuperation is from 1979

**The most substantial official treatment of recovery after nuclear use
that this article located is nearly fifty years old.**
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
and the primary tables make that claim more precise than it first looks.**
The scenarios divide into regional exchanges in South Asia
and a single global exchange.
The 150 teragram case is not a United States and Russia scenario,
since the paper states it "assumes attacks on France, Germany, Japan,
United Kingdom, United States, Russia and China".
China is therefore a target in the largest scenario this article surveys,
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
is the closest published match to the subject here that was located.
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
states that the People's Liberation Army Navy,
which it abbreviates to PLAN,
"is the largest navy in the world with a battle force of over 370 platforms"
and that its "overall battle force is expected to grow to 395 ships by 2025
and 435 ships by 2030".
**The [2025 edition of the same report][government_dod_2025_china_report]
gives no fleet total at all**,
having been restructured to about half the length of the 2023 edition.
Its Taiwan Strait military balance table counts ships by class,
giving China 3 aircraft carriers, 3 amphibious assault ships, 8 cruisers,
42 destroyers, 50 frigates, 50 corvettes and 46 attack submarines,
against Taiwan's 4 destroyers, 22 frigates, 7 corvettes and 2 attack submarines.
It prints no aggregate and says only that
"The PLAN has the largest force of principal combatants, submarines,
and amphibious warfare ships in Asia".
**The class rows could be added up and they are not added up here.**
A battle force total follows counting rules
about which auxiliaries and patrol craft are included,
and a sum of these rows would produce a number
that looked official and answered to no published definition.
So no current official total is available to test the projection against.
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

Whether the island is worth taking at all is itself disputed.
[Green and Talmadge 2022][journal_green_talmadge_2022]
argue Chinese control of the island would materially improve China's position,
and [Caverley 2025][journal_caverley_2025]
rebuts them with a kill-chain model,
finding the transformation "would make little difference to the broader military balance".

## A Survey of the Contemporary Literature

The sources read closely above are a small part of several large literatures.
This section surveys the rest,
grouped by the question each cluster tries to answer
and organised by position where positions conflict,
because a survey that lists titles without saying who contradicts whom
hides the only thing a reader needs.
Every work named here was confirmed in a bibliographic registry
with matching authors, title, year and venue.
**Where a work is named without a finding attached,
that is deliberate and means its text was not retrieved**,
and no claim is attributed to it.

### War termination, where the bargaining literature disagrees with itself

Reiter, Goemans and Iklé carry the termination argument earlier in this piece.
The formal literature behind them is larger and does not speak with one voice.

**The baseline is that war is a bargaining failure.**
[Fearon 1995][journal_fearon_1995_rationalist_explanations]
shows that under broad conditions
settlements exist that rational states would prefer to fighting,
and reduces the puzzle to two mechanisms,
private information with an incentive to misrepresent it,
and situations where states cannot credibly commit.

**The disagreement is about which mechanism matters for long wars,
and it bears directly on a war nobody can end.**
[Powell 2006][journal_powell_2006_commitment_problem]
argues that informational explanations "often provide a poor account
of prolonged conflict",
and recasts bargaining indivisibilities as commitment problems.
That is the position the termination section above implicitly adopts
when it says neither side could promise not to rearm.

**A third position holds that neither mechanism is needed.**
[Slantchev 2003][journal_slantchev_2003_power_to_hurt]
models warfare as costly bargaining
and shows that "inefficient fighting can occur in equilibrium
under complete information and very general assumptions favoring peace".
**If that is right, a Taiwan war could run long
even with both sides fully informed and both able to commit**,
which removes the last mechanism by which better intelligence
or a more credible guarantee would shorten it.

**On whether settlements can be engineered, the evidence is split.**
[Fortna 2003][journal_fortna_2003_scraps_of_paper]
tests the durability of peace with hazard analysis
and finds that "stronger agreements enhance the durability of peace",
against a counterargument that agreements are epiphenomenal
and merely reflect the underlying probability of resumption.
[Walter 1997][journal_walter_1997_critical_barrier]
supplies the mechanism and the uncomfortable condition.
Across 1940 to 1990,
55 percent of interstate wars were resolved at the bargaining table
against only 20 percent of civil wars,
and groups "almost always chose to fight to the finish
unless an outside power stepped in to guarantee a peace agreement".

$$
\frac{55}{20} = 2.75
$$

Interstate wars settled at nearly three times the rate of civil wars,
and the difference Walter identifies is third-party enforcement.
**A Taiwan war has no available third party**,
since the plausible guarantors are the belligerents,
and Beijing's position is that the conflict is internal,
which places it in the category with the lower settlement rate
and the missing enforcement mechanism.

[Weisiger 2013][book_weisiger_2013_logics_of_war]
traces the longest and deadliest conflicts to preventive wars driven by mutual distrust,
while optimism-driven wars are corrected quickly by battlefield reality and settle cheaply.
[Thyne 2012][journal_thyne_2012_intra_war_bargaining]
finds that the strength and stability of executives
affect both the information and the commitment channels,
which connects this literature to the regime-survival section above.

**The most unsettling result in the cluster inverts the obvious intuition.**
[Wolford, Reiter and Carrubba 2011][journal_wolford_2011_information_commitment]
show that when asymmetric information and shifting-power commitment problems coexist,
resolving uncertainty by fighting can continue a war rather than end it,
wars can become less likely to settle the longer they last,
and war aims rise over time.
**Fighting longer is normally expected to reveal who is winning and so to shorten the war.
On this account it can do the opposite.**

The informational side has not conceded.
[Shirkey 2016][journal_shirkey_2016_uncertainty_duration]
argues directly against the commitment account of long wars,
holding that states generate fresh uncertainty while fighting
and that disagreements about the capacity to bear costs
outlast disagreements about military capability.
[Weisiger 2016][journal_weisiger_2016_learning_battlefield]
fuses the two channels,
finding settlement more likely after extensive fighting and deteriorating results,
and treating leader replacement as part of the information-updating process,
especially in autocracies,
which is the same mechanism the regime-survival section above examines.

**On whether a great-power war can be deliberately ended at all, the field splits.**
[Mearsheimer 2025][journal_mearsheimer_2025_war_and_politics]
argues that meaningful limits on when great powers start wars are almost impossible
and that wars tend to escape political control and escalate,
which is in flat tension with a bargaining tradition
that treats termination as a controllable equilibrium.
[Talmadge 2017][journal_talmadge_2017_would_china_go_nuclear]
supplies a mechanism specific to this war,
that a conventional American campaign could threaten China's retaliatory capability
and make limited nuclear escalation look like the least-bad response
despite a declared no-first-use policy.
**That paper is the bridge between the termination section
and its nuclear section, and no wargame in the public record plays it out.**

On settlement design the evidence runs against the pessimists and then qualifies itself.
[Licklider 1995][journal_licklider_1995_negotiated_settlements]
finds negotiated settlements structurally fragile
because power-sharing leaves the loser able to resume,
while [Hartzell and Hoddie 2003][journal_hartzell_2003_institutionalizing_peace]
record that the more dimensions of power sharing an agreement specifies, the longer peace holds.
[Werner and Yuen 2005][journal_werner_yuen_2005_making_keeping_peace]
qualify the design literature from inside it,
finding that ceasefires produced by third-party pressure are more likely to fail
and that terms consistent with battlefield results matter more than enforcement provisions.
**That is in direct tension with Walter's third-party-guarantee result**,
and the article does not resolve it,
because the two use different samples and different outcome measures.

### Recovery economics, where the central question is what makes damage persist

Davis and Weinstein, Eichengreen and Ritschl, Organski and Kugler,
and Miguel and Roland carried the recovery argument earlier.
Each of them has an opponent in print.

**Whether bombed cities return to trend is unresolved and the dispute is methodological.**
[Davis and Weinstein 2008][journal_davis_weinstein_2008_multiple_equilibria]
extend their own work to 114 Japanese cities across eight manufacturing industries
and report no support for multiple equilibria,
with cities recovering population, manufacturing share and even industry mix.
[Bosker, Brakman, Garretsen and Schramm 2007][journal_bosker_2007_multiple_equilibria]
apply the same framework to German bombing
but add spatial interdependence,
and do find multiple equilibria with evidence for two stable states,
reporting that the evidence weakens when geography is ignored.
**The two results are not strictly comparable**,
because the specifications differ over whether spatial interdependence belongs in the model,
and the literature has not settled which is correct.
[Redding, Sturm and Wolf 2011][journal_redding_2011_history_industry_location]
side with multiplicity on a cleaner shock,
treating the move of Germany's air hub from Berlin to Frankfurt
as a shift between steady states rather than a return to fundamentals.

**The cleanest decomposition of what persists supports the thesis here
and narrows it at the same time.**
[Waldinger 2016][journal_waldinger_2016_bombs_brains]
uses the dismissal of scientists in Nazi Germany and wartime bombing as separate shocks
and finds that a 10 percent human-capital shock cut scientific output
by 0.2 standard deviations and persisted,
while a 10 percent physical-capital shock cut it by 0.05 standard deviations
and did not persist.

$$
\frac{0.2}{0.05} = 4
$$

**The human-capital shock was four times larger in effect and, unlike the physical one, lasted.**
That is the strongest single piece of evidence in this survey
for the proposition that buildings are the recoverable part,
and it also says what the irrecoverable part is,
which the sources used here otherwise leave vague.

**On Germany the revisionist position is stronger than the article's own framing allowed.**
[Vonyo 2018][book_vonyo_2018_economic_consequences]
argues the war did not destroy the foundations of German economic power
and that recovery was driven by wartime legacies of enhanced industrial capacity
and an enlarged labour force
rather than by liberal reform or the Marshall Plan.
**That sets him against the De Long and Eichengreen framing used above**,
and in the same direction as the reading of the capacity index given above.
[Vonyo 2012][journal_vonyo_2012_bombing_of_germany]
adds the constraint that the plant-survives story usually omits,
finding that destruction of urban housing
left urban industry short of labour and capacity underutilised,
while rural areas gained workers and lost industrial productivity.
**Capacity that survives is not capacity that can be used
if the workers have nowhere to live**,
which is a refinement the Ukrainian housing figures above should be read against.

**Against the optimistic reading stands a literature arguing recovery is a myth.**
[Cerra and Saxena 2008][journal_cerra_saxena_2008_myth_of_recovery]
find output losses from financial and some political crises highly persistent,
with civil wars the partial exception showing some rebound.
[Mueller 2012][journal_mueller_2012_comment]
attacks that exception directly in the same journal,
showing the civil-war coding misrepresents the impact
and that correct coding gives an average output loss of 18 percent,
making civil wars worse than every other crisis category they studied.
[Collier 1999][journal_collier_1999_economic_consequences]
cuts across both with a counterintuitive result,
that economies recover rapidly after long civil wars
and continue to decline after short ones.

**Four studies locate persistence in four different places,
and none of them is physical capital.**
[Feigenbaum, Lee and Mezzanotti 2022][journal_feigenbaum_2022_capital_destruction]
find effects of Sherman's March persisting to 1920
and attribute them to underdeveloped financial markets rather than to the destruction.
[Riano and Valencia Caicedo 2024][journal_riano_2024_collateral_damage]
find heavily bombed regions of Laos
showing 7.1 percent lower output per head almost fifty years later
for each standard deviation of bombing intensity,
with unexploded ordnance as the transmission mechanism.
**That mechanism has a line item in the Ukrainian assessment above**,
explosive hazards management at almost 30 billion dollars,
which is the same hazard priced prospectively.
[Dell and Querubin 2018][journal_dell_querubin_2018_nation_building]
find that bombing in Vietnam increased insurgent activity,
weakened local governance and reduced civic engagement,
which is a direct counterweight to the Miguel and Roland null used above.
[Costalli, Moretti and Pischedda 2017][journal_costalli_2017_economic_costs]
estimate an average annual loss of 17.5 percent of output per head by synthetic control
and find ethnic fractionalisation robustly associated with higher costs
through eroded interethnic trust.

**One strand finds destruction can raise output, which no part of this article anticipated.**
[Hornbeck and Keniston 2017][journal_hornbeck_keniston_2017_creative_destruction]
study the Great Boston Fire of 1872
and show that enabling widespread simultaneous reconstruction
set off a virtuous circle of upgrades,
raising land values on burned and neighbouring unburned plots,
which implies that durable obsolete buildings had been constraining growth beforehand.
[Siodla 2015][journal_siodla_2015_razing_san_francisco]
finds density rising at least 60 percent in razed relative to unburned areas
of San Francisco by 1914,
with a large differential persisting today.
**Neither is a war**, and neither involves killed workers, destroyed institutions or lost trade,
so the mechanism is coordination rather than recovery.
It is included because it is the one argument in the literature
that destruction is not uniformly costly,
and an article claiming buildings come back easily
should state the version of that claim it is not making.

**On aid the evidence is unhelpful to anyone planning a reconstruction.**
[Rajan and Subramanian 2008][journal_rajan_subramanian_2008_aid_and_growth]
find little robust evidence of any relationship between aid and growth
once the bias that aid follows poor growth is corrected,
and no evidence that aid works better in better policy environments.
[Collier and Hoeffler 2004][journal_collier_hoeffler_2004_aid_policy_growth]
argue post-conflict settings differ,
with absorptive capacity roughly doubling in years four to ten,
so aid should phase in where historically it has tapered out.
**[Girod 2011][journal_girod_2011_effective_foreign_aid]
supplies the most uncomfortable result for the subject here.**
Aid improves development only where donors have little strategic interest in the recipient
and the recipient is desperate for income.
A reconstruction of an ally the donor cannot afford to lose
is precisely the case that result predicts will go badly.

### Nuclear consequences, where the dispute has a measurable crossover

Sections above settle on the plume as the contested step.
The literature is more precise than that,
and one paper locates the crossover.

**The climate response to a given soot load is not in dispute.**
[Coupe and others 2019][journal_coupe_2019_nuclear_winter_responses]
run the same 150 teragram injection through two structurally independent models
and obtain similar nuclear winter,
with the newer model's faster soot removal failing to shrink the response.
[Hess 2021][journal_hess_2021_two_views]
states the disagreement in print,
that the camps differ on fuel loading
and on the amount and initial altitude of the black carbon fed to the models,
rather than on the models themselves.

**[Wagman and others 2020][journal_wagman_2020_multiscale]
turn that qualitative statement into a number.**
Working from Sandia and Lawrence Livermore,
they find that at one gram of fuel burned per square centimetre
there is no global mean forcing at all,
while at sixteen grams per square centimetre
black carbon reaches the stratosphere and the surface cools.

$$
\frac{16}{1} = 16
$$

**A sixteenfold range in one input spans the entire distance
between no effect and nuclear winter.**
That is the sharpest statement available of why the dispute persists,
and it explains why both sides can be internally consistent.
They also obtain about four years of forcing
against the eight to fifteen years the opposing group simulates.

The fuel-loading estimate under attack is
[Toon and others 2007][journal_toon_2007_atmospheric_effects],
which found low-yield weapons on city centres
producing about a hundred times the smoke per kilotonne
that earlier full-scale-war analyses assumed.
[Reisner and others 2019][journal_reisner_2019_reply]
reply to the criticism of their own work,
holding that firestorms are difficult to form,
that black carbon scales nonlinearly with fuel load,
and that their case was already a worst case.

**The plume physics has a separate dispute that cuts across the camps.**
[Tarshish and Romps 2022][journal_tarshish_romps_2022_latent_heating]
calculate that a dry plume needs at least a 60 kelvin anomaly to reach the cold point
and that simulated dry firestorm plumes fall short by a factor of two or more,
so only moist plumes reach the stratosphere.
**The strongest observational evidence runs the other way.**
[Peterson and others 2021][journal_peterson_2021_black_summer]
report that more than half of 38 observed pyrocumulonimbus events
in Australia's Black Summer injected smoke directly into the stratosphere,
with plumes continuing to rise over three months
"in a manner consistent with existing nuclear winter theory".

**On the food pathway the literature has an optimistic pole
that the nuclear section above did not represent.**
[Jägermeyr and others 2020][journal_jagermeyr_2020_food_security]
give a 12 percent single-year global caloric loss from a 5 teragram war
across six harmonised crop models,
which they note quadruples the largest observed historical anomaly.
[Scherrer and others 2020][journal_scherrer_2020_fisheries]
find fish biomass and catch falling up to 18 and 29 percent for a decade,
while noting that prewar stock rebuilding could create a buffer.
Against the famine pole,
[Rivers and others 2024][journal_rivers_2024_food_system_adaptation]
model a 150 teragram scenario and find global famine
only without trade and without adaptation,
with maintained trade and rapid resilient-food scale-up
sufficient in their model to feed the global population.
**What divides them is therefore human response and not soot**,
which is a different kind of uncertainty from the fire-physics one
and is more amenable to policy.

### The grid, which is the recovery constraint nobody in the wargames prices

Two results in the consequence literature bear directly on rebuilding
and belong in this article rather than in the nuclear section alone.
[Baker and others 2021][journal_baker_2021_large_transformers]
report that large power transformers have replacement times measured in months to years,
that no large power transformer has ever undergone threat-level electromagnetic pulse testing,
and that claims of immunity are premature.
**That is the same shape as the shipyard constraint**,
a long-lead component with few suppliers
whose replacement clock is set by manufacturing rather than by money.
[Blouin and others 2024][journal_blouin_2024_electricity_loss]
model catastrophic electricity loss against the food supply chain
and conclude that a recovery measured in weeks to months still permits adequate calories
if distribution is equitable,
while a year-long recovery across most of the continental United States
could precipitate famine.
**The threshold between inconvenience and famine is the repair time of the grid**,
which is a reconstruction variable and not a war-fighting one.

For the single-detonation case the planning literature is more settled.
[Dillon 2014][journal_dillon_2014_shelter_times]
calculates that rapid adequate sheltering could save tens of thousands of lives,
and gives an operational rule,
to leave a poor shelter within thirty minutes if better shelter is fifteen minutes away.
[Scouras 2019][journal_scouras_2019_global_catastrophic_risk]
frames the whole field honestly,
holding that nuclear war is a global catastrophic but not an existential risk,
that nuclear winter may kill more than blast, prompt radiation and fallout combined,
and that likelihood estimates are largely intuition.

### Chinese nuclear posture, where the two sides hold opposite beliefs about control

[Kristensen and others 2025][journal_kristensen_2025_chinese_nuclear_weapons]
estimate approximately 600 Chinese warheads with more in production,
the fastest growth among the nine nuclear-armed states.
[Hiim, Fravel and Trøan 2023][journal_hiim_2023_entangled_security_dilemma]
find from Chinese-language sources
limited evidence of a doctrinal shift but a clear posture shift toward secure second strike,
driven by fear of American limited nuclear use
and of non-nuclear threats to Chinese nuclear forces.

**The asymmetry that matters most here is one of belief.**
[Cunningham and Fravel 2019][journal_cunningham_fravel_2019_dangerous_confidence]
document that Chinese strategists doubt escalation can be controlled
and plan only retaliatory strikes,
while American analysts are more confident that limited use would stay limited.
**Two sides that disagree about whether a nuclear war can be kept limited
are more likely to produce one that is not**,
and that mechanism appears in no public wargame of this conflict.

### Regime survival, where the literature contains the strongest objection to its own use

Modest base rates were the conclusion above.
The literature contains something sharper,
and it sits inside the body of work usually cited for the opposite claim.

**[Croco and Weeks 2016][journal_croco_weeks_2016_war_outcomes_tenure]
find that tenure is sensitive to war outcomes
only for culpable democratic leaders
and for culpable non-democratic leaders who are also vulnerable to removal.
Non-democratic leaders who are not vulnerable are insensitive regardless of culpability.**
That conditional is the one that matters for a personalised leadership,
and it is evidence against the claim that defeat endangers the Party,
published by two of the authors whose earlier work is cited for the claim.

Three further results point the same way.
[Weeks 2012][journal_weeks_2012_strongmen]
argues personalist regimes lack an effective domestic audience
and any predictable mechanism for removing a belligerent leader.
[Di Lonardo, Sun and Tyson 2020][journal_dilonardo_2020_autocratic_stability]
model foreign threats as increasing the probability an autocrat retains power,
either by compelling greater domestic security
or by letting the autocrat exploit the threat to deter challengers.
[Piplani and Talmadge 2015][journal_piplani_talmadge_2015_war_helps]
find coup risk declining in the presence of enduring interstate conflict
and report no evidence at all that war increases it.

**The purge literature supplies the mechanism and a cost.**
[Sudduth 2017][journal_sudduth_2017_elite_purges]
finds that dictators purge when elite capability to remove them is temporarily low
rather than when coup risk is high.
[Talmadge 2015][book_talmadge_2015_dictators_army]
finds that regimes facing coup threats
adopt promotion, training and command practices that squander military power.
[Brown, Fariss and McMahon 2015][journal_brown_2015_recouping]
close the loop in a direction this article should record,
finding that leaders who coup-proof
substitute for degraded fighting effectiveness
by pursuing chemical, biological or nuclear weapons and by forging alliances.
**A regime that purges its way to internal safety
buys the capability it lost on the unconventional market**,
which connects the regime-survival question to the nuclear one.

### The postwar order, where the proliferation cascade is not a simple function of defeat

A demand signal already exists in South Korean opinion, as reported above.
The literature disputes what drives it.

**The result that complicates the cascade story runs backwards.**
[Sukin 2019][journal_sukin_2019_credible_commitments_backfire]
runs survey experiments in 2018 and 2019
and finds that increases in the credibility of the American guarantee
*increased* South Korean support for acquiring nuclear weapons,
because some respondents fear allied miscalculation and entrapment.
**If entrapment rather than abandonment is doing the work,
allied proliferation is not a simple function of a visible American failure**,
and the demand signal the article quotes
cannot be read straight off as a response to weakening commitment.

[Fuhrmann and Tkach 2015][journal_fuhrmann_tkach_2015_nuclear_latency]
supply the base rate against cascade reasoning,
recording that 31 countries developed the capacity to build nuclear weapons
between 1939 and 2012 and only ten acquired arsenals.

$$
\frac{10}{31} \approx 0.32
$$

Under a third of latent states ever built an arsenal.
[Gavin 2010][journal_gavin_2010_same_as_it_ever_was]
attacks cascade reasoning directly as nuclear alarmism.

**On whether one abandonment collapses an alliance system, the evidence resists the inference.**
[Henry 2020][journal_henry_2020_what_allies_want]
argues allies do not want indiscriminate loyalty,
and documents several allies in the First Taiwan Strait Crisis
actively encouraging American disloyalty to Taipei
in order to reduce their own entrapment risk.

On the shape of the order itself the field is split three ways.
[Brooks and Wohlforth 2016][journal_brooks_wohlforth_2016_rise_and_fall]
deny a near-term transition on capability grounds,
holding that converting economic into military capacity is harder than it was.
[Mearsheimer 2019][journal_mearsheimer_2019_bound_to_fail]
holds that a liberal order is possible only under unipolarity
and predicts a thin international order plus two bounded ones.
[Ikenberry 2018][journal_ikenberry_2018_end_of_liberal_order]
places the crisis inside the West rather than in rising revisionist states.

**What a victorious coalition should expect has been measured directly.**
[Wolford 2017][journal_wolford_2017_shared_victory]
analyses war-winning coalitions from 1816 to 2007
and finds that larger coalitions are associated with less durable postwar peace
among their own members,
as are more extensive prewar alliance commitments.
**The coalition that wins the war is a predictor of the instability that follows it**,
which is the only quantitative result located
that treats the victors' postwar relations as the dependent variable.

### The defence industrial base, where the camps disagree about the binding constraint

Yards, workforce and consolidation are treated above as one constraint.
The literature does not treat them that way,
and it divides into four positions about what actually binds.

**Money.** The defence-inflation literature puts the constraint in cost escalation,
which implies that appropriations can fix it.
This is the premise underneath most European rearmament instruments.
[Fabbrini 2024][journal_fabbrini_2024_defence_union]
examines the European instrument built on that premise,
and [Kowalski and Sahmali 2025][journal_kowalski_2025_nato_pledge]
find that member-state sovereignty over spending
outweighs the alliance role in the industrial capacity pledge,
which is a limit on what money alone can buy.

**Workforce.**
[Gerber and others 2026][research_gerber_2026_workforce]
at RAND find workforce shortfalls threatening reconstitution
within twelve to twenty-four months of a conflict,
which is the position the accountability office figures in this article support.

**Consolidation and monopsony.**
[Deutch 2022][journal_deutch_2022_consolidation]
finds that consolidation left firms less financially secure rather than more,
and that asset reductions were marginal,
which cuts against the efficiency rationale for the mergers.
[Bellais 2023][journal_bellais_2023_market_structures]
argues that reform adjusted how the market functions
without questioning institutional features inherited from the Cold War.
[Hyatt and Everhart 2025][journal_hyatt_2025_shrinking_base]
survey firms that actually left the defence market and their stated reasons.
**The opposing position in this camp is
[Gholz and Sapolsky 2000][journal_gholz_sapolsky_2000_restructuring],
whose text was not retrieved for this article**,
so it is named as a landmark in the debate and no finding is attributed to it.

**Lead time rather than capacity.**
[Hellberg 2026][journal_hellberg_2026_supply_chains],
from forty-five interviews,
relocates the bottleneck to a peacetime supply-chain structure
built for small batches,
which yields lead-time blowout rather than absent plant.
[Hellberg and Lundmark 2025][journal_hellberg_2025_european_chains]
find demand exceeding available supply capacity in Europe after 2022.
[Scarazzato and others 2024][journal_scarazzato_2024_arms_production]
report that arms production actually fell 3.5 percent in real terms in 2022
while orders had not yet converted into revenue,
and that many firms faced difficulty scaling up.

**The sharpest measurement in this cluster is European and recent.**
[Knezevic 2026][journal_knezevic_2026_capacity_gap]
constructs a capacity gap index for 155 millimetre ammunition
and finds delivered output running 20 to 50 percent below announced capacity
across 2023 to 2025,
with a measured learning rate of 5 to 8 percent per doubling
against the 10 to 25 percent that the usual learning curve assumes.

$$
\frac{5}{10} = 0.5,
\qquad
\frac{8}{25} = 0.32
$$

**Learning is running at between a third and a half of the assumed rate.**
That is a direct test of the premise that announced capacity becomes delivered output,
and it fails in the one case where a Western industrial base
has recently tried to surge a single munition under wartime demand.

### Mobilisation history, which does not support the analogy drawn from it

The Second World War mobilisation is the stock reassurance in this field,
and the economic history has moved against the reassuring reading.
[Field 2023][journal_field_2023_manufacturing_productivity],
discussed above,
measures falling manufacturing productivity through the war.
[Salavrakos 2017][journal_salavrakos_2017_japanese_armaments]
reassesses Japanese wartime armaments production.
[Harrison 1998][book_harrison_1998_economics_ww2]
is the standard comparative volume,
and [Rockoff 2012][book_rockoff_2012_economic_way_of_war]
the standard American account.
**The analogy is contested rather than settled**,
and an article invoking 1941 should say which side it is taking.

### Force ratios, where the critics make three different objections

The twenty-per-thousand figure this article uses has a critical literature,
and its objections are routinely collapsed into one.
They are three.

**The measurement objection** holds that the denominator is wrong,
since what matters is population in contested areas rather than national population.
[Kalyvas 2006][book_kalyvas_2006_logic_of_violence]
supplies the underlying account of territorial control
on which that objection rests.

**The specification objection** holds that force size is not the operative variable.
[Lyall and Wilson 2009][journal_lyall_wilson_2009_rage_machines]
find mechanisation rather than force size explains counterinsurgency outcomes.
[King 2022][journal_king_2022_urban_insurgency]
inverts the relation,
treating shrinking state force size as a cause of increased urban conflict.
[Phayal 2019][journal_phayal_2019_peacekeeping]
finds that peacekeeping deployment restrains violence
but that military capacity is not the mechanism.

**The sample objection** holds that ratios are fitted to cases chosen because they resolved.
[Friedman 2011][journal_friedman_2011_manpower]
mounts the formal large-sample test across 171 campaigns since the First World War,
asking both how force size should be measured
and whether it relates to success at all.

**The most damaging qualification comes from inside the army's own analysis.**
[Goode 2009][journal_goode_2009_force_requirements],
writing from the Center for Army Analysis,
states that understanding has advanced little since 1995,
makes no policy recommendation,
and holds that force levels are necessary but not sufficient.
**That is the institution that uses the ratio
declining to defend it as a planning number.**

The dissent from the dissent is
[Lalwani 2017][journal_lalwani_2017_size_still_matters],
who finds material preponderance remains essential
and sometimes the most important factor.

**The peacekeeping evidence sharpens the unit of measurement rather than rejecting it.**
[Hultman, Kathman and Shannon 2014][journal_hultman_2014_beyond_keeping_peace]
find a dose-response relationship in peacekeeping
that holds for armed military troops and not for police or observers.
Quinlivan's ratio counts troops and police together.
**If the peacekeeping result transfers,
the article's 466,000 is the wrong composition even at the right magnitude.**

### Occupation outcomes, where the base rates point in both directions

[Edelstein 2010][book_edelstein_2010_occupational_hazards]
examines 26 military occupations since 1815
and finds occasional success against more frequent failure.
[Liberman 1998][book_liberman_1998_does_conquest_pay]
argues the other way,
that invaders can exploit industrial societies and sustain control,
which is the position most directly relevant to a Taiwan annexation.
[Downes 2021][book_downes_2021_catastrophic_success]
finds foreign-imposed regime change raises civil-war risk in the target.
[Dobbins, McGinn and Crane 2003][research_dobbins_2003_nation_building]
supply the resource benchmark,
that nation-building requires substantial investments of money, troops and time.

**The post-1945 base rate is a poor guide here in either direction.**
[Fazal 2011][book_fazal_2011_state_death]
finds that the violent death of states became rare after 1945,
while [Altman 2020][journal_altman_2020_territorial_conquest]
shows that partial conquest never went away
and that the modern pattern is the fait accompli over small areas.
A full annexation of a populous island
matches neither the vanishing pattern nor the surviving one.

### Resistance to occupation, where a headline result has been shown to be fragile

[Stephan and Chenoweth 2008][journal_stephan_chenoweth_2008_why_civil_resistance]
established the influential result that nonviolent campaigns outperform violent ones,
and [Chenoweth and Lewis 2013][journal_chenoweth_lewis_2013_navco]
extended the data with an explicit anti-occupation category.
**[Chenoweth 2020][journal_chenoweth_2020_future_of_resistance]
reports that even as civil resistance peaked in popularity in the 2010s
"its effectiveness had begun to decline",
and dates the decline before the pandemic.**

[Dworschak 2023][journal_dworschak_2023_streetlight]
is the more careful qualification and is often described loosely,
so it is worth stating exactly.
He reproduces the original results successfully.
He then shows that cases may have been overlooked through a streetlight effect,
and quantifies the fragility by simulation,
finding the main results "highly sensitive to variable selection
and undercoverage bias, bootstrapping, and omitted variable bias".
**That is a successful replication followed by a sensitivity analysis
that undermines confidence in the estimate,
which is a different and more interesting thing than a failed replication.**
An article leaning on that literature for Taiwanese resistance
would be leaning on a result its own author has qualified
and an independent assessment has shown to be fragile,
which is why this article does not lean on it.

The safer anchor is occupation-specific.
[Stringer and Hooiveld 2023][journal_stringer_2023_urban_resistance]
examine Dutch urban resistance in the Second World War,
frame it explicitly against Taiwan and Ukraine,
and claim the feasibility of urban guerrilla activity rather than its effectiveness.
**Feasibility and effectiveness are different claims
and the distinction is the reason to prefer this one.**

[Heath, Lilly and Han 2023][research_heath_2023_can_taiwan_resist]
at RAND assess whether Taiwan could resist a large-scale attack,
and [Martin and others 2022][research_martin_2022_coercive_quarantine]
model a coercive quarantine rather than an invasion,
which is the scenario the energy stockpile figures above actually bear on.

### The cost of a Taiwan contingency, where three incommensurable quantities wear the same units

The figures quoted for what a Taiwan conflict would cost
range from about two trillion dollars to about ten.
**That spread is not a disagreement about magnitude.
It is three different quantities reported in the same units**,
and the authors of the careful ones say so.

**The first quantity is activity at risk.**
The Rhodium Group's 2022 note puts well over two trillion dollars of activity at risk
in a blockade halting Taiwanese trade,
assembled from value-added trade, foregone downstream revenue,
trade finance and investment stocks.
Its authors state plainly that they
"do not purport to estimate GDP losses or other measures of foregone economic welfare"
and are providing "a snapshot of activity at risk at the beginning of a blockade".
**Exposure is mechanically larger than welfare loss**,
because substitution, inventories and reallocation absorb part of any gross flow.

**The second quantity is welfare or output loss, and it comes in far smaller.**
[Goes and Bekkers 2022][journal_goes_bekkers_2022_geopolitical_conflicts]
build a multi-sector general-equilibrium model with dynamic knowledge diffusion
and reach decoupling welfare losses as large as 15 percent in some regions,
while stating explicitly that
"without diffusion of ideas the size and variation across regions
of the welfare losses would be substantially smaller".
[Javorcik and others 2024][journal_javorcik_2024_friendshoring]
put friendshoring losses at up to 4.7 percent of output in the worst-affected economies.
[Attinasi and others 2024][journal_attinasi_2024_decoupling_costs]
find welfare losses roughly five times larger in the short run than the long run,
driven by rigid wages and low input substitutability.
[Felbermayr, Mahlkow and Sandkamp 2023][journal_felbermayr_2023_cutting_value_chain]
find damage scaling inversely with the target economy's size.
**Four models, four different answers, and in each case the authors name
the assumption that produced the magnitude.**

$$
\frac{15}{4.7} \approx 3.2
$$

The highest and lowest headline welfare estimates differ by about threefold
before any disagreement about scenario.
**The spread within that family is traceable to three modelling choices
rather than to disagreement about the world**,
namely whether knowledge diffusion is in the model,
whether commodity linkages are granular,
and whether the horizon is short or long.
**Every refinement added since the baseline has pushed the estimate up
and none has pushed it down**,
which is worth noticing because it is the pattern
a literature produces when its baseline was too simple
rather than when it is converging on a value.

**The third quantity bundles destruction, mobilisation and financial panic**,
and it is the one the press quotes.
The widely cited ten trillion dollar figure, about a tenth of world output,
is attached to a war rather than to a blockade,
and this article could not read the method behind it,
so it is reported as a figure of unverified construction
and nothing is inferred from it.

**The only properly specified input-output disruption estimate located is tiny.**
[Nassar and others 2024][research_usgs_2024_gallium_germanium]
at the United States Geological Survey
couple post-disruption price equilibria with economic input-output tables
and find that a complete Chinese export cutoff of gallium and germanium
would reduce American output by about 3.4 billion dollars,
within a range of 1.7 to 9.0 billion.
**A total cutoff of two critical minerals costs less than a rounding error
on the trillion-dollar figures**, which is either a reassurance
or a demonstration that the headline numbers measure something else entirely.

**One group refuses to produce a number at all, and its reason is methodological.**
The CSIS commentary on the economic impact of a Taiwan crisis
declines a dollar figure by design,
seeking to understand firm psychology
rather than using formal models to estimate the impact.
[Martin and others 2023][research_martin_2023_supply_chain_interdependence]
reach a tabletop judgment rather than a cost,
concluding that there are generally no good short-term options.
**No peer-reviewed macroeconomic model of a Taiwan contingency was located.
Every dollar figure in circulation comes from think tanks or private forecasters.**

### Whether decoupling policy achieves what it is for

Four results face the same way and against the premise of the policy.
[Crosignani and others 2024][research_crosignani_2024_geopolitical_risk]
give firm-level evidence that American export controls
destroyed about 130 billion dollars of supplier market capitalisation
and produced no evidence of reshoring or friend-shoring.
[Goldberg and others 2024][research_goldberg_2024_industrial_policy]
find that Chinese semiconductor subsidies
are not exceptional relative to other countries
once differences in market size are taken into account,
which undercuts the subsidy-race framing.
[Bown and Wang 2024][journal_bown_wang_2024_semiconductors]
document that modern semiconductor policy spans tariffs, export controls,
investment screening and antitrust rather than subsidies alone.
The industry study this article already uses
prices full regional self-sufficiency at a minimum of one trillion dollars
and a 35 to 65 percent increase in chip prices.

**On who can actually weaponise a supply chain the literature is more careful
than the policy debate.**
[Beaumier and Cartwright 2023][journal_beaumier_cartwright_2023_cross_network]
map the chain as four interrelated networks
and show that American centrality in design
is what permits leverage over the assembled-chip trade.
[Cha 2023][journal_cha_2023_collective_resilience]
finds that past targets of Chinese economic coercion
export 46.6 billion dollars of goods on which China is more than 70 percent import-dependent,
making collective retaliation feasible.
[Chen and Evers 2023][journal_chen_evers_2023_wars_without_gun_smoke]
add the domestic condition,
that high-value firms in the dominant power tend to oppose economic statecraft
while low-value firms in the rising power cooperate with it.

### Taiwan's own preparation, where official accounts and scholarship disagree

[Davis and Gholz 2026][journal_davis_gholz_2026_blockade_by_fire]
model a blockade executed by missile attacks on ports
rather than by interdicting shipping at sea,
and find China likely able to suppress Taiwan's trade substantially
at relatively low escalation risk and without exposing its fleet.
**That is the scenario the stockpile figures above actually bear on**,
and it is cheaper for the attacker than the invasion the wargames model.

On the energy transition the scholarship divides over whether security counts as a criterion.
[Gao, Yeh and Chen 2022][journal_gao_2022_unjust_failed_transition]
document the 2025 energy mix target being missed by a wide margin.
[Lau and Tsai 2022][journal_lau_tsai_2022_decarbonization_roadmap]
score security and reliability alongside sustainability
and recommend delaying the nuclear phase-out to 2050.
[Wu 2023][journal_wu_2023_taiwan_security]
goes furthest and treats the energy shift as a deterrence failure
rather than an energy-policy choice,
arguing that reduced conscription and changed energy policy
have together eroded Taiwan's deterrence.

**On civil defence the official account and the scholarly assessment do not match.**
Taiwan's own defence review reports a resilience committee inaugurated in 2024,
one-year conscription restored, recall training extended to fourteen days,
and a commitment to exceed 3 percent of output on defence.
[Mangold 2026][journal_mangold_2026_cultural_factors]
reports the same reforms as culturally blocked,
finding from elite interviews a military culture that undervalues conscripts and reserves,
institutional resistance to sharing defence with civilian agencies,
and suspicion of trained civilians.
**Inputs are not outcomes**, and an article that cited only the review
would be reporting a budget as though it were a capability.

**On undersea cables the data cut against the sabotage narrative in one direction
and support it in another.**
Taiwan's digital ministry reports that inside the contiguous zone in 2025
six of seven cable faults were human-caused,
with anchor damage the largest single category across 2022 to 2025.
Beyond that zone, about 44 percent of 2025 faults were caused by earthquakes,
one December event cutting six systems at once.
[Mok 2026][journal_mok_2026_undersea_cable_resilience]
finds the real vulnerability in a lack of redundancy,
limited repair capacity and gaps in maritime law
rather than in attribution.
**The Matsu case above is therefore the right lesson drawn from a thin evidence base**,
since deliberate interference is a minority of cable faults
and redundancy helps regardless of who cut the cable.

## Where the Sources Agree and Where They Do Not

The sections above read each body of work on its own terms.
Set side by side,
the sources disagree in nine places that matter,
and the disagreements are more informative than the agreements
because each one marks a quantity that is not settled.

### Three agreements that hold across methods

**Capital stock is damaged less than output falls.**
The bombing survey measured it at plant level in 1945,
finding machine tools destroyed at a quarter the rate of the buildings housing them.
Eichengreen and Ritschl measured it as an index pair for 1948,
output at 64 against capacity at 113.
The Ukraine assessment measures it in a war still running,
at most a seventh of the housing gone against a fifth of the output.
Three measurements, three methods, eighty years apart, same direction.
**The separate claim that capital also recovers quickly
rests on the city literature rather than on these three**,
and that literature is the one that disagrees with itself below.

**Replacement of major platforms runs in decades and not years.**
The budget office, the accountability office, the research service,
the Navy's own plan and the CSIS reconstitution passage
were produced by five institutions with different incentives
and give the same picture of yards, build durations and workforce.

**Termination is not a solved problem.**
Iklé, Reiter, Goemans, Stanley and Sawyer, Croco, Krepinevich,
the RAND 2016 report, the denial essay and joint doctrine
agree that fighting stops for reasons the fighting itself does not supply.
None of them offers a mechanism that closes a Taiwan war.

### Nine disagreements, each with both sides named

**How many times the invasion game was run.**
Heath says 22 and the CSIS report says 24.
The report text was checked for this article and gives 24.
The discrepancy is one twelfth and it propagates into anything quoting Heath.

**Whether bombed cities return to trend.**
Davis and Weinstein find full mean reversion in Japan within fifteen years.
Brakman, Garretsen and Schramm find the German effect
"significant but temporary" in the west and absent in the east.
Nguyen and others find reversion for only 50 to 70 percent of West German cities.
**The three results are compatible only if the mechanism is institutional**,
which is what the second and third papers argue and the first does not test.

**What the Japanese bombing destroyed, in numbers.**
Davis and Weinstein give 2.2 million buildings and three hundred thousand killed.
The bombing survey gives 2,510,000 and approximately 330,000.
The survey is the earlier and primary document
and the paper is the one the recovery literature cites.

**How many prime contractors remained in each market.**
The accountability office in 1998 and the department in 2022
agree on surface ships at 1998 and differ on tactical missiles,
four against three.
Neither published the counting rule.

**Whether war is bad for subsequent growth.**
Organski and Kugler find losers recover to antebellum standing.
Koubi finds a positive causal effect of war duration on later growth.
Federle and others find an output drop near 10 percent at the war site.
**Part of the split is about the sample**,
since Koubi's effect concentrates in civil wars,
and partly about whether the counterfactual is the prewar level or the prewar path.

**Whether a failed invasion endangers Communist Party rule.**
The CSIS report says the party "would be risking its hold on power"
in a sentence that disclaims having studied it.
RAND judges that "the regime and its security forces presumably could withstand such challenges".
Goemans' base rates put the increase in irregular-removal risk at about 3 points.
Fravel finds Chinese leaders compromise when internally insecure.
**Four sources, four directions, and no study of the actual case.**

**Whether soot from burning cities reaches the stratosphere.**
Reisner and others find most of it does not.
Robock, Toon and Bardeen find the fire model unrepresentative.
**Both agree on what happens to the climate once soot is aloft**,
which narrows the dispute to a tractable question about plumes.

**What Chinese shipbuilding capacity is relative to American.**
The leaked slide implies about 232 to 1 on tonnage capacity.
Funaiole's testimony gives about 482 to 1 on commercial output share.
The trade investigation gives a tenfold rise in Chinese share of global tonnage
and no ratio at all.
**None of the three measures warship construction**,
which is the quantity a reconstitution estimate needs.

**Whether Taiwan is worth taking.**
Green and Talmadge argue Chinese control would materially improve China's position.
Caverley rebuts with a kill-chain model
and finds it "would make little difference to the broader military balance".
This is a live dispute in the same journal family
and neither side prices the reconstruction.

### What the pattern of disagreement shows

**The agreements are about mechanisms and the disagreements are about magnitudes.**
Every source agrees that yards constrain replacement,
that capital outlasts output,
and that wars do not end for military reasons alone.
They disagree on how many yards, how much capital, how long, and how likely.
**For an article asking what rebuilding would take,
that is the wrong way round**,
because a mechanism without a magnitude cannot be planned against.

## Five Gaps in the Literature

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
The field's newest synthesis,
the 2025 National Academies consensus study,
carries no economic recovery analysis and no recovery timescale for human systems,
and names that as a research gap itself.
**The only official study containing a recuperation analysis that this search found
dates from 1979.**
- **The occupation force-density literature and the invasion literature have never been joined.**
The arithmetic above took minutes and appears nowhere.
**The provenance of the ratio widens the gap rather than narrowing it.**
It is descriptive in the 1995 article usually credited with it,
prescriptive in a 2006 field manual that attributes it to nobody,
and **absent from that manual's 2014 revision**,
so the number is applied to no Taiwan case
and no longer appears in the doctrine that made it a norm.

- **Nobody has priced Taiwan's own reconstruction.**
Two independent searches for this article,
across bibliographic registries, a development-bank document repository
and the congressional commission's annual report,
found no published estimate of what rebuilding Taiwan would cost,
nor of its wartime economic damage in currency terms.
The works that look as though they should contain one do not.
The exposure estimates say in their own text that they are not welfare estimates,
and the invasion wargame says only that the island's economy was devastated.
**This is an absence in the reachable literature rather than a proof of non-existence**,
since several think-tank catalogues could not be enumerated without a search engine.
It is also the gap that matters most to the question this article asks,
because every other figure here describes the cost to somebody else.

A sixth observation follows from the five.
There appears to be no published work whose central thesis
is that the wargaming literature ignores the aftermath.
What exists is adjacent and assemblable,
which is what this article has done.

**A seventh observation is about the sources rather than the subject.**
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
The two Government Accountability Office shipbuilding reports of 2025 and 2026, through files.gao.gov.
The Funaiole testimony.
The Quinlivan force-ratio essay of 2003.
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
The Department of Defense competition report,
and the two older accountability office reports on the industrial base,
of 1998 and 2022, through the Wayback Machine,
since gao.gov refuses automated clients on those paths where files.gao.gov served the newer pair.
The two annual reports to Congress on Chinese military developments, for 2023 and 2025,
both reached through media.defense.gov with a referer header,
the 2025 edition's Taiwan Strait balance table being a raster image read by eye.
The Economic Cooperation Act as enacted, and the final report of its administering agency.
Two State Department documents in the Foreign Relations of the United States series.
The 1995 Quinlivan article, through an archived copy of the original electronic edition.
The approved December 2006 counterinsurgency field manual and its 2014 revision.
Joint Publication 3-0.
The Ministry of the Interior population series, parsed from the published spreadsheet.

**How the literature survey was built, and what bounds it.**
Discovery used bibliographic registries and open repositories
rather than a search engine,
because this session's web-search budget was exhausted before the survey began.
Every work named in it was confirmed in Crossref or OpenAlex
with matching authors, title, year and venue.
**A result is attached to a work only where an abstract or full text was read.**
A work named without one was not obtained,
and no claim is attributed to it,
which applies to several landmarks whose publishers refuse automated clients.
The bounds are real and not random with respect to the subject.
English-language sources only,
several think-tank catalogues that render their indexes in script
and so could not be enumerated,
and publishers that return a refusal to any automated request.
**A survey assembled this way under-represents grey literature
and over-represents indexed journals**, and the article's own reference composition shows it.

**Every quotation added in the reference pass was checked against the source text
rather than against an intermediary's report of it.**
Nineteen were confirmed on the first pass.
Several others failed a literal string match
and were confirmed only after normalising for scanned hyphenation,
two-column interleaving and a running header that fell inside a sentence.
**That distinction matters, because a failed match is not evidence of a bad quotation
and a passing match on a summary is not evidence of a good one.**

**Composition of the reference set.**
There are 222 references, of which 219 carry external addresses
and three are internal cross-references to published posts.
By category they are 134 journal articles, 41 research reports,
17 government documents, 15 books, 6 commentaries and 6 data sources.
The median publication year is 2019,
with 49.5 percent from 2020 onward, 26.1 percent from the 2010s,
14.7 percent from the 2000s and 9.6 percent earlier,
the oldest being the bombing survey of 1945.
**Twenty-three of the 219 are primary government documents or datasets,
which is 10.5 percent**,
and that share fell as the survey added journal literature,
which is what a survey section does to a corpus.
These figures are recomputed from the reference list by script
rather than stated and left to drift.

**Reachability.**
Of the 219 external addresses, 130 return a 200 response.
**Reaching that number required two user agents**,
since 117 answer an honest agent carrying a contact address
and a further 13 answer only a browser string,
while two government hosts refuse the browser string and answer the honest one.
A sweep sending a single agent therefore reports blocks
that are properties of the client rather than of the document.

**The 89 that do not resolve are almost all one thing,
and the failure is not where it appears to be.**
Eighty-seven are journal digital object identifiers.
Each resolves correctly at the registry,
returning a 302 redirect to the publisher,
and the publisher then refuses the automated client.
**The identifier works and the paywall does not**,
which is a fact about publisher bot policy
and not about the citation.
The remaining two are the Congressional Budget Office
and a defence media host,
both catalogued blocks reached for this article by other routes.
Every journal citation was checked against Crossref
for title, authors, journal and year,
which is the verification of record where the publisher will not answer.

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
and that it names the research gap itself.
The only official study with a recuperation analysis located
is the Office of Technology Assessment's of 1979.

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
**The section pairing agreements against disagreements is also a construction of this piece.**
No source located arranges these works that way,
the groupings are editorial judgments about what counts as the same question,
and a different reader could reasonably sort them differently.
What is not editorial is the content of each disagreement,
since both sides of all nine are quoted from sources read for this article.

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
- Any claim that the literature survey above is exhaustive.
It is bounded by English-language sources,
by what registries and open repositories index,
and by publishers that refuse automated access,
and those bounds are not random with respect to the subject.

## Conclusion

The most cited public wargames end at about 21 days and say so,
and the longest public campaign model stops at day 46
with Taipei taken and nothing after it.
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

What the record does not contain is more useful than what it does.
No public wargame models the period after the landing or after the failure.
No study examines whether the Chinese state survives losing,
though the report most often quoted on the point asserts it might not
in the same sentence that disclaims having looked.
No consequence or recovery study exists for nuclear use in this theatre.
And the occupation arithmetic that follows from the literature's own ratio,
about 466,000 personnel for Taiwan and roughly five times that to sustain them,
took minutes to compute and appears in none of it.

**Reading the primary documents rather than the accounts of them
changed this article in two directions, and honesty requires both.**
Several corrections found a secondary account
more confident than the source it rested on,
including the Japanese damage figures, the force-ratio attribution
and the naval balance projection.
**Others were this article's own**,
among them a ratio computed from rounded inputs,
a population figure two years stale,
and a claim stated more broadly than the evidence allowed.
The corrections are listed individually below rather than totalled,
because a count would invite exactly the false precision the pass was correcting.
What held without exception is the smaller observation.
Every primary document read here was more candid about its own limits
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

- [Book, Downes 2021, Catastrophic Success, Why Foreign-Imposed Regime Change Goes Wrong][book_downes_2021_catastrophic_success]
- [Book, Edelstein 2010, Occupational Hazards, Success and Failure in Military Occupation][book_edelstein_2010_occupational_hazards]
- [Book, Fazal 2011, State Death, the Politics and Geography of Conquest, Occupation, and Annexation][book_fazal_2011_state_death]
- [Book, Goemans 2000, War and Punishment][book_goemans_2000_war_and_punishment]
- [Book, Harrison 1998, The Economics of World War II][book_harrison_1998_economics_ww2]
- [Book, Ikenberry 2019, After Victory][book_ikenberry_2019_after_victory]
- [Book, Ikle 2005, Every War Must End][book_ikle_2005_every_war_must_end]
- [Book, Kalyvas 2006, The Logic of Violence in Civil War][book_kalyvas_2006_logic_of_violence]
- [Book, Liberman 1998, Does Conquest Pay, the Exploitation of Occupied Industrial Societies][book_liberman_1998_does_conquest_pay]
- [Book, Organski and Kugler 1980, The War Ledger][book_organski_kugler_1980_war_ledger]
- [Book, Reiter 2009, How Wars End][book_reiter_2009_how_wars_end]
- [Book, Rockoff 2012, America’s Economic Way of War][book_rockoff_2012_economic_way_of_war]
- [Book, Talmadge 2015, The Dictator’s Army, Battlefield Effectiveness in Authoritarian Regimes][book_talmadge_2015_dictators_army]
- [Book, Vonyo 2018, The Economic Consequences of the War, West Germany’s Growth Miracle After 1945][book_vonyo_2018_economic_consequences]
- [Book, Weisiger 2013, Logics of War, Sources of Limited and Unlimited Conflict][book_weisiger_2013_logics_of_war]
- [Commentary, Blanchette and McGregor 2026, After the Invasion, China Considers the Problem of Ruling Taiwan][commentary_blanchette_2026_after_invasion]
- [Commentary, Heath 2023, Wargames Cannot Tell Us How to Deter a Chinese Attack on Taiwan][commentary_heath_2023_wargames_deterrence]
- [Commentary, Heim, Burdette and Beauchamp-Mustafaga 2024, Denial Is the Worst Except for All the Others][commentary_heim_2024_denial_worst]
- [Commentary, Sudduth 2026, Double-Edged Swords, How Military Purges Shape Authoritarian Appetite for War][commentary_sudduth_2026_double_edged_swords]
- [Commentary, Tetreau 2023, Where the Wargames Were Not][commentary_tetreau_2023_where_the_wargames_were_not]
- [Commentary, Trevithick 2023, Alarming Navy Intelligence Slide on Chinese Shipbuilding Capacity][commentary_twz_2023_oni_slide]
- [Data, Boston Consulting Group and Semiconductor Industry Association 2021, Strengthening the Global Semiconductor Value Chain][data_bcg_sia_2021_value_chain]
- [Data, Central Election Commission of the Republic of China, National Referendum Results Database][data_roc_cec_referendums]
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
- [Government, Department of War 2025, Military and Security Developments Involving the People’s Republic of China][government_dod_2025_china_report]
- [Government, Economic Cooperation Administration 1951, Thirteenth Report to Congress][government_eca_1951_thirteenth_report]
- [Government, Glasstone and Dolan 1977, The Effects of Nuclear Weapons, Third Edition, TID-28061][government_glasstone_dolan_1977]
- [Government, Joint Chiefs of Staff 2018, Joint Publication 3-0, Joint Operations][government_jp_3_0_2018]
- [Government, Office of Technology Assessment 1979, The Effects of Nuclear War][government_ota_1979_effects_of_nuclear_war]
- [Government, Office of the Director of National Intelligence 2026, Annual Threat Assessment][government_odni_2026_threat_assessment]
- [Government, Republic of China 2026, Petroleum Administration Act, Article 24][government_roc_petroleum_act]
- [Government, United States Congress 1948, Economic Cooperation Act of 1948, 62 Stat. 137][government_economic_cooperation_act_1948]
- [Government, United States Strategic Bombing Survey 1945, Over-all Report, European War][government_ussbs_1945_overall_report]
- [Government, United States Strategic Bombing Survey 1946, Summary Report, Pacific War][government_ussbs_1946_pacific_summary]
- [Government, US-China Economic and Security Review Commission 2025, Annual Report to Congress, Taiwan Chapter][government_uscc_2025_taiwan_chapter]
- [Journal, Altman 2020, The Evolution of Territorial Conquest After 1945, International Organization 74 number 3][journal_altman_2020_territorial_conquest]
- [Journal, Attinasi, Boeckelmann and Meunier 2024, The Economic Costs of Supply Chain Decoupling, The World Economy][journal_attinasi_2024_decoupling_costs]
- [Journal, Baker and others 2021, Large Transformer Criticality, Threats, and Opportunities, Journal of Critical Infrastructure Policy 2 number 2][journal_baker_2021_large_transformers]
- [Journal, Beaumier and Cartwright 2023, Cross-Network Weaponization in the Semiconductor Supply Chain, International Studies Quarterly 68 number 1][journal_beaumier_cartwright_2023_cross_network]
- [Journal, Bellais 2023, Market Structures, Competition and Innovation, Defence and Peace Economics][journal_bellais_2023_market_structures]
- [Journal, Blouin and others 2024, Assessing the Impact of Catastrophic Electricity Loss on the Food Supply Chain, International Journal of Disaster Risk Science 15][journal_blouin_2024_electricity_loss]
- [Journal, Bosker, Brakman, Garretsen and Schramm 2007, Looking for Multiple Equilibria When Geography Matters, Journal of Urban Economics 61 number 1][journal_bosker_2007_multiple_equilibria]
- [Journal, Bown and Wang 2024, Semiconductors and Modern Industrial Policy, Journal of Economic Perspectives 38 number 4][journal_bown_wang_2024_semiconductors]
- [Journal, Brakman, Garretsen and Schramm 2004, The Strategic Bombing of German Cities, Journal of Economic Geography 4 number 2][journal_brakman_2004_german_bombing]
- [Journal, Brooks and Wohlforth 2016, The Rise and Fall of the Great Powers in the Twenty-First Century, International Security 40 number 3][journal_brooks_wohlforth_2016_rise_and_fall]
- [Journal, Brown, Fariss and McMahon 2015, Recouping After Coup-Proofing, International Interactions 42 number 1][journal_brown_2015_recouping]
- [Journal, Bueno de Mesquita, Siverson and Woller 1992, War and the Fate of Regimes, American Political Science Review 86 number 3][journal_bueno_de_mesquita_1992]
- [Journal, Caverley 2025, So What, Texas National Security Review 8 number 3][journal_caverley_2025]
- [Journal, Cerra and Saxena 2008, Growth Dynamics, the Myth of Economic Recovery, American Economic Review 98 number 1][journal_cerra_saxena_2008_myth_of_recovery]
- [Journal, Cha 2023, Collective Resilience, International Security 48 number 1][journal_cha_2023_collective_resilience]
- [Journal, Chan and others 2025, Resilience Reconsidered, International Journal of Disaster Risk Science 16 number 4][journal_chan_2025_resilience]
- [Journal, Chen and Evers 2023, Wars Without Gun Smoke, International Security 48 number 2][journal_chen_evers_2023_wars_without_gun_smoke]
- [Journal, Chenoweth 2020, The Future of Nonviolent Resistance, Journal of Democracy 31 number 3][journal_chenoweth_2020_future_of_resistance]
- [Journal, Chenoweth and Lewis 2013, Unpacking Nonviolent Campaigns, Journal of Peace Research 50 number 3][journal_chenoweth_lewis_2013_navco]
- [Journal, Collier 1999, On the Economic Consequences of Civil War, Oxford Economic Papers 51 number 1][journal_collier_1999_economic_consequences]
- [Journal, Collier and Hoeffler 2004, Aid, Policy and Growth in Post-Conflict Societies, European Economic Review 48 number 5][journal_collier_hoeffler_2004_aid_policy_growth]
- [Journal, Costalli, Moretti and Pischedda 2017, The Economic Costs of Civil War, Journal of Peace Research 54 number 1][journal_costalli_2017_economic_costs]
- [Journal, Coupe and others 2019, Nuclear Winter Responses to Nuclear War Between the United States and Russia, Journal of Geophysical Research Atmospheres 124 number 15][journal_coupe_2019_nuclear_winter_responses]
- [Journal, Croco 2011, The Decider's Dilemma, American Political Science Review 105 number 3][journal_croco_2011]
- [Journal, Croco and Weeks 2016, War Outcomes and Leader Tenure, World Politics 68 number 4][journal_croco_weeks_2016_war_outcomes_tenure]
- [Journal, Cunningham and Fravel 2019, Dangerous Confidence, Chinese Views on Nuclear Escalation, International Security 44 number 2][journal_cunningham_fravel_2019_dangerous_confidence]
- [Journal, Davis and Gholz 2026, Blockade by Fire, International Security 50 number 4][journal_davis_gholz_2026_blockade_by_fire]
- [Journal, Davis and Weinstein 2002, Bones, Bombs, and Break Points, American Economic Review 92 number 5][journal_davis_weinstein_2002]
- [Journal, Davis and Weinstein 2008, A Search for Multiple Equilibria in Urban Industrial Structure, Journal of Regional Science 48 number 1][journal_davis_weinstein_2008_multiple_equilibria]
- [Journal, Debs and Goemans 2010, Regime Type, the Fate of Leaders, and War, American Political Science Review 104 number 3][journal_debs_goemans_2010]
- [Journal, Dell and Querubin 2018, Nation Building Through Foreign Intervention, Quarterly Journal of Economics 133 number 2][journal_dell_querubin_2018_nation_building]
- [Journal, Deutch 2022, Consolidation of the United States Defense Industrial Base, Defense Acquisition Research Journal 29 number 2][journal_deutch_2022_consolidation]
- [Journal, Di Lonardo, Sun and Tyson 2020, Autocratic Stability in the Shadow of Foreign Threats, American Political Science Review 114 number 4][journal_dilonardo_2020_autocratic_stability]
- [Journal, Dillon 2014, Determining Optimal Fallout Shelter Times Following a Nuclear Detonation, Proceedings of the Royal Society A 470][journal_dillon_2014_shelter_times]
- [Journal, Dworschak 2023, Civil Resistance in the Streetlight, Comparative Politics 55 number 2][journal_dworschak_2023_streetlight]
- [Journal, Eichengreen and Ritschl 2009, Understanding West German Economic Growth in the 1950s, Cliometrica 3 number 3][journal_eichengreen_ritschl_2009]
- [Journal, Fabbrini 2024, European Defence Union, European Foreign Affairs Review][journal_fabbrini_2024_defence_union]
- [Journal, Fearon 1995, Rationalist Explanations for War, International Organization 49 number 3][journal_fearon_1995_rationalist_explanations]
- [Journal, Federle and others 2026, The Price of War, American Economic Review 116 number 3][journal_federle_2026_price_of_war]
- [Journal, Feigenbaum, Lee and Mezzanotti 2022, Capital Destruction and Economic Growth, American Economic Journal Applied Economics 14 number 4][journal_feigenbaum_2022_capital_destruction]
- [Journal, Felbermayr, Mahlkow and Sandkamp 2023, Cutting Through the Value Chain, Empirica 50 number 1][journal_felbermayr_2023_cutting_value_chain]
- [Journal, Ferreira and Critelli 2023, Taiwan’s Food Resiliency or Not in a Conflict with China, Parameters 53 number 2][journal_ferreira_critelli_2023_food_resiliency]
- [Journal, Field 2023, The Decline of US Manufacturing Productivity Between 1941 and 1948, Economic History Review][journal_field_2023_manufacturing_productivity]
- [Journal, Flavin 2003, Planning for Conflict Termination and Post-Conflict Success, Parameters 33 number 3][journal_flavin_2003_conflict_termination]
- [Journal, Fortna 2003, Scraps of Paper, Agreements and the Durability of Peace, International Organization 57 number 2][journal_fortna_2003_scraps_of_paper]
- [Journal, Fravel 2005, Regime Insecurity and International Cooperation, International Security 30 number 2][journal_fravel_2005_regime_insecurity]
- [Journal, Friedman 2011, Manpower and Counterinsurgency, Security Studies 20 number 4][journal_friedman_2011_manpower]
- [Journal, Fu, Yin and Han 2024, The Human Cost of War, Conflict Management and Peace Science 42 number 5][journal_fu_2024_human_cost_of_war]
- [Journal, Fuhrmann and Tkach 2015, Almost Nuclear, Introducing the Nuclear Latency Dataset, Conflict Management and Peace Science 32 number 4][journal_fuhrmann_tkach_2015_nuclear_latency]
- [Journal, Gao, Yeh and Chen 2022, An Unjust and Failed Energy Transition Strategy, Energy Strategy Reviews][journal_gao_2022_unjust_failed_transition]
- [Journal, Gavin 2010, Same As It Ever Was, Nuclear Alarmism, Proliferation, and the Cold War, International Security 34 number 3][journal_gavin_2010_same_as_it_ever_was]
- [Journal, Gholz and Sapolsky 2000, Restructuring the United States Defense Industry, International Security 24 number 3][journal_gholz_sapolsky_2000_restructuring]
- [Journal, Girod 2011, Effective Foreign Aid Following Civil War, American Journal of Political Science 56 number 1][journal_girod_2011_effective_foreign_aid]
- [Journal, Glick and Taylor 2010, Collateral Damage, Review of Economics and Statistics 92 number 1][journal_glick_taylor_2010]
- [Journal, Goemans 2008, Which Way Out, Journal of Conflict Resolution 52 number 6][journal_goemans_2008_which_way_out]
- [Journal, Goemans, Gleditsch and Chiozza 2009, Introducing Archigos, Journal of Peace Research 46 number 2][journal_goemans_2009_archigos]
- [Journal, Goes and Bekkers 2022, The Impact of Geopolitical Conflicts on Trade, Growth, and Innovation, WTO Staff Working Paper][journal_goes_bekkers_2022_geopolitical_conflicts]
- [Journal, Goode 2009, A Historical Basis for Force Requirements in Counterinsurgency, Parameters 39 number 4][journal_goode_2009_force_requirements]
- [Journal, Green and Talmadge 2022, Then What, International Security 47 number 1][journal_green_talmadge_2022]
- [Journal, Hartzell and Hoddie 2003, Institutionalizing Peace, American Journal of Political Science 47 number 2][journal_hartzell_2003_institutionalizing_peace]
- [Journal, Hellberg 2026, Reconfiguring Defence Supply Chains, Defence and Peace Economics][journal_hellberg_2026_supply_chains]
- [Journal, Hellberg and Lundmark 2025, Transformation in European Defence Supply Chains, Scandinavian Journal of Military Studies][journal_hellberg_2025_european_chains]
- [Journal, Henry 2020, What Allies Want, International Security 44 number 4][journal_henry_2020_what_allies_want]
- [Journal, Hess 2021, The Impact of a Regional Nuclear Conflict Between India and Pakistan, Two Views, Journal for Peace and Nuclear Disarmament 4 number 1][journal_hess_2021_two_views]
- [Journal, Hiim, Fravel and Trøan 2023, The Dynamics of an Entangled Security Dilemma, International Security 47 number 4][journal_hiim_2023_entangled_security_dilemma]
- [Journal, Hornbeck and Keniston 2017, Creative Destruction, Barriers to Urban Growth and the Great Boston Fire of 1872, American Economic Review 107 number 6][journal_hornbeck_keniston_2017_creative_destruction]
- [Journal, Hultman, Kathman and Shannon 2014, Beyond Keeping Peace, American Political Science Review 108 number 4][journal_hultman_2014_beyond_keeping_peace]
- [Journal, Hyatt and Everhart 2025, The Shrinking Defense Industrial Base, Defense Acquisition Research Journal 32 number 2][journal_hyatt_2025_shrinking_base]
- [Journal, Ikenberry 2018, The End of Liberal International Order, International Affairs 94 number 1][journal_ikenberry_2018_end_of_liberal_order]
- [Journal, Javorcik and others 2024, Economic Costs of Friendshoring, The World Economy][journal_javorcik_2024_friendshoring]
- [Journal, Jehn and others 2025, Food Trade Disruption After Global Catastrophes, Earth System Dynamics 16 number 5][journal_jehn_2025_food_trade]
- [Journal, Jägermeyr and others 2020, A Regional Nuclear Conflict Would Compromise Global Food Security, Proceedings of the National Academy of Sciences 117 number 13][journal_jagermeyr_2020_food_security]
- [Journal, King 2022, Urban Insurgency in the Twenty-First Century, International Affairs 98 number 2][journal_king_2022_urban_insurgency]
- [Journal, Knezevic 2026, War Reindustrialization of the European Union, the Capacity Gap and Wright’s Law, Vojno delo 78 number 2][journal_knezevic_2026_capacity_gap]
- [Journal, Koubi 2005, War and Economic Performance, Journal of Peace Research 42 number 1][journal_koubi_2005]
- [Journal, Kowalski and Sahmali 2025, NATO and the Defence Production Challenge, Journal of Military and Strategic Studies][journal_kowalski_2025_nato_pledge]
- [Journal, Kristensen and others 2025, Chinese Nuclear Weapons 2025, Bulletin of the Atomic Scientists 81 number 2][journal_kristensen_2025_chinese_nuclear_weapons]
- [Journal, Lai and others 2026, Lost in Words, Framing Effects on Public Willingness to Fight, Public Opinion Quarterly 90][journal_lai_2026_lost_in_words]
- [Journal, Lalwani 2017, Size Still Matters, Explaining Sri Lanka’s Counterinsurgency Victory, Small Wars and Insurgencies 28 number 1][journal_lalwani_2017_size_still_matters]
- [Journal, Lau and Tsai 2022, A Decarbonization Roadmap for Taiwan, Sustainability 14][journal_lau_tsai_2022_decarbonization_roadmap]
- [Journal, Lee, Chen and Chen 2024, Core Public Attitudes toward Defense and Security in Taiwan, Taiwan Politics][journal_lee_2024_taiwan_attitudes]
- [Journal, Licklider 1995, The Consequences of Negotiated Settlements in Civil Wars, American Political Science Review 89 number 3][journal_licklider_1995_negotiated_settlements]
- [Journal, Lyall and Wilson 2009, Rage Against the Machines, International Organization 63 number 1][journal_lyall_wilson_2009_rage_machines]
- [Journal, Mangold 2026, The Cultural Factors of Defence Reforms, the Case of Taiwan, International Journal of Asia Pacific Studies 22 number 2][journal_mangold_2026_cultural_factors]
- [Journal, Mearsheimer 2019, Bound to Fail, the Rise and Fall of the Liberal International Order, International Security 43 number 4][journal_mearsheimer_2019_bound_to_fail]
- [Journal, Mearsheimer 2025, War and International Politics, International Security][journal_mearsheimer_2025_war_and_politics]
- [Journal, Miguel and Roland 2011, The Long-Run Impact of Bombing Vietnam, Journal of Development Economics 96 number 1][journal_miguel_roland_2011]
- [Journal, Miguel and Roland 2024, Corrigendum to The Long-Run Impact of Bombing Vietnam, Journal of Development Economics 166][journal_miguel_roland_2024_corrigendum]
- [Journal, Mok 2026, Toward Undersea Cable Resilience, Texas National Security Review 9 number 3][journal_mok_2026_undersea_cable_resilience]
- [Journal, Mueller 2012, Growth Dynamics, the Myth of Economic Recovery, Comment, American Economic Review 102 number 7][journal_mueller_2012_comment]
- [Journal, Nemeth 2026, How a United States Suez Moment Could Hollow the Alliance System, Texas National Security Review 9 number 1][journal_nemeth_2026_suez_moment]
- [Journal, Nguyen and others 2025, Second World War Bombing and the German City System, Global Challenges and Regional Science 1][journal_nguyen_2025_german_cities]
- [Journal, Organski and Kugler 1977, The Costs of Major Wars, the Phoenix Factor, American Political Science Review 71 number 4][journal_organski_kugler_1977]
- [Journal, Peterson and others 2021, Australia’s Black Summer Pyrocumulonimbus Super Outbreak, npj Climate and Atmospheric Science 4][journal_peterson_2021_black_summer]
- [Journal, Phayal 2019, UN Troop Deployment and Preventing Violence Against Civilians, International Interactions 45 number 4][journal_phayal_2019_peacekeeping]
- [Journal, Piplani and Talmadge 2015, When War Helps Civil-Military Relations, Journal of Conflict Resolution 60 number 8][journal_piplani_talmadge_2015_war_helps]
- [Journal, Powell 2006, War as a Commitment Problem, International Organization 60 number 1][journal_powell_2006_commitment_problem]
- [Journal, Quek and Johnston 2018, Can China Back Down, International Security 42 number 3][journal_quek_johnston_2018]
- [Journal, Rajan and Subramanian 2008, Aid and Growth, Review of Economics and Statistics 90 number 4][journal_rajan_subramanian_2008_aid_and_growth]
- [Journal, Redding, Sturm and Wolf 2011, History and Industry Location, Review of Economics and Statistics 93 number 3][journal_redding_2011_history_industry_location]
- [Journal, Reisner and others 2018, Climate Impact of a Regional Nuclear Weapons Exchange, Journal of Geophysical Research Atmospheres 123 number 5][journal_reisner_2018]
- [Journal, Reisner and others 2019, Reply to Comment by Robock and Others, Journal of Geophysical Research Atmospheres 124 number 23][journal_reisner_2019_reply]
- [Journal, Riano and Valencia Caicedo 2024, Collateral Damage, the Legacy of the Secret War in Laos, Economic Journal][journal_riano_2024_collateral_damage]
- [Journal, Rivers and others 2024, Food System Adaptation and Maintaining Trade Could Mitigate Global Famine, Global Food Security 43][journal_rivers_2024_food_system_adaptation]
- [Journal, Robock, Toon and Bardeen 2019, Comment on Climate Impact of a Regional Nuclear Weapon Exchange, Journal of Geophysical Research Atmospheres 124 number 23][journal_robock_2019_comment]
- [Journal, Salavrakos 2017, A Re-assessment of Japanese Armaments Production During World War II, Defence and Peace Economics][journal_salavrakos_2017_japanese_armaments]
- [Journal, Scarazzato and others 2024, Developments in Arms Production and the Effects of the War in Ukraine, Defence and Peace Economics][journal_scarazzato_2024_arms_production]
- [Journal, Scherrer and others 2020, Marine Wild-Capture Fisheries After Nuclear War, Proceedings of the National Academy of Sciences 117 number 47][journal_scherrer_2020_fisheries]
- [Journal, Scouras 2019, Nuclear War as a Global Catastrophic Risk, Journal of Benefit-Cost Analysis 10 number 2][journal_scouras_2019_global_catastrophic_risk]
- [Journal, Shi and others 2025, Adapting Agriculture to Climate Catastrophes, Environmental Research Letters 20 number 6][journal_shi_2025_adapting_agriculture]
- [Journal, Shirkey 2016, Uncertainty and War Duration, International Studies Review 18 number 2][journal_shirkey_2016_uncertainty_duration]
- [Journal, Siodla 2015, Razing San Francisco, Journal of Urban Economics 89][journal_siodla_2015_razing_san_francisco]
- [Journal, Slantchev 2003, The Power to Hurt, American Political Science Review 97 number 1][journal_slantchev_2003_power_to_hurt]
- [Journal, Stanley and Sawyer 2009, The Equifinality of War Termination, Journal of Conflict Resolution 53 number 5][journal_stanley_sawyer_2009]
- [Journal, Stephan and Chenoweth 2008, Why Civil Resistance Works, International Security 33 number 1][journal_stephan_chenoweth_2008_why_civil_resistance]
- [Journal, Stringer and Hooiveld 2023, Urban Resistance to Occupation, Parameters 53 number 2][journal_stringer_2023_urban_resistance]
- [Journal, Sudduth 2017, Strategic Logic of Elite Purges in Dictatorships, Comparative Political Studies 50 number 13][journal_sudduth_2017_elite_purges]
- [Journal, Sukin 2019, Credible Nuclear Security Commitments Can Backfire, Journal of Conflict Resolution 64 number 6][journal_sukin_2019_credible_commitments_backfire]
- [Journal, Talmadge 2017, Would China Go Nuclear, International Security 41 number 4][journal_talmadge_2017_would_china_go_nuclear]
- [Journal, Tarshish and Romps 2022, Latent Heating Is Required for Firestorm Plumes to Reach the Stratosphere, Journal of Geophysical Research Atmospheres 127 number 16][journal_tarshish_romps_2022_latent_heating]
- [Journal, Thyne 2012, Information, Commitment, and Intra-War Bargaining, International Studies Quarterly 56 number 2][journal_thyne_2012_intra_war_bargaining]
- [Journal, Toon and others 2007, Atmospheric Effects and Societal Consequences of Regional Scale Nuclear Conflicts, Atmospheric Chemistry and Physics 7 number 8][journal_toon_2007_atmospheric_effects]
- [Journal, Vonyo 2012, The Bombing of Germany, European Review of Economic History 16 number 1][journal_vonyo_2012_bombing_of_germany]
- [Journal, Wagman and others 2020, Examining the Climate Effects of a Regional Nuclear Weapons Exchange, Journal of Geophysical Research Atmospheres 125 number 24][journal_wagman_2020_multiscale]
- [Journal, Waldinger 2016, Bombs, Brains, and Science, Review of Economics and Statistics 98 number 5][journal_waldinger_2016_bombs_brains]
- [Journal, Walter 1997, The Critical Barrier to Civil War Settlement, International Organization 51 number 3][journal_walter_1997_critical_barrier]
- [Journal, Weeks 2012, Strongmen and Straw Men, American Political Science Review 106 number 2][journal_weeks_2012_strongmen]
- [Journal, Weisiger 2016, Learning from the Battlefield, International Organization 70 number 2][journal_weisiger_2016_learning_battlefield]
- [Journal, Werner and Yuen 2005, Making and Keeping Peace, International Organization 59 number 2][journal_werner_yuen_2005_making_keeping_peace]
- [Journal, Wolford 2017, The Problem of Shared Victory, Journal of Politics 79 number 2][journal_wolford_2017_shared_victory]
- [Journal, Wolford, Reiter and Carrubba 2011, Information, Commitment, and War, Journal of Conflict Resolution 55 number 4][journal_wolford_2011_information_commitment]
- [Journal, Wu 2023, Taiwan’s Security, Civilian Control and External Threat, Cogent Arts and Humanities][journal_wu_2023_taiwan_security]
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
- [Research, Crosignani and others 2024, Geopolitical Risk and Decoupling, Evidence from United States Export Controls][research_crosignani_2024_geopolitical_risk]
- [Research, De Long and Eichengreen 1991, The Marshall Plan, History's Most Successful Structural Adjustment Program][research_delong_eichengreen_1991_marshall]
- [Research, Dobbins, McGinn and Crane 2003, America’s Role in Nation-Building, From Germany to Iraq][research_dobbins_2003_nation_building]
- [Research, Evans 2023, Alternative Futures Following a Great Power War, Volume 2][research_evans_2023_alternative_futures_v2]
- [Research, Funaiole 2026, Testimony on Countering Chinese Dominance in Global Shipbuilding][research_funaiole_2026_testimony]
- [Research, Garlauskas, Gilbert and Imai 2025, A Rising Nuclear Double-Threat in East Asia][research_garlauskas_2025_guardian_tiger]
- [Research, General Accounting Office 1998, Defense Industry, Consolidation and Options for Preserving Competition][research_gao_1998_defense_consolidation]
- [Research, Gerber and others 2026, Breaking Glass, Missing Hands, Addressing Workforce Constraints][research_gerber_2026_workforce]
- [Research, Goldberg and others 2024, Industrial Policy in the Global Semiconductor Sector][research_goldberg_2024_industrial_policy]
- [Research, Gompert, Cevallos and Garafola 2016, War with China, Thinking Through the Unthinkable][research_gompert_2016_war_with_china]
- [Research, Government Accountability Office 2022, Defense Industrial Base, DOD Should Take Actions to Strengthen Its Risk Mitigation Approach][research_gao_2022_industrial_base]
- [Research, Government Accountability Office 2025, Shipbuilding and Repair, Private Sector Industrial Base Investments][research_gao_2025_shipbuilding_workforce]
- [Research, Gunzinger and Penney 2026, Rebuilding America's Air Force][research_gunzinger_2026_rebuilding_air_force]
- [Research, Heath, Lilly and Han 2023, Can Taiwan Resist a Large-Scale Military Attack by China][research_heath_2023_can_taiwan_resist]
- [Research, Jones 2023, Empty Bins in a Wartime Environment][research_jones_2023_empty_bins]
- [Research, Krepinevich 2020, Protracted Great-Power War, a Preliminary Assessment][research_krepinevich_2020_protracted_great_power_war]
- [Research, Labs 2025, The Navy's 2025 Shipbuilding Plan and the Shipbuilding Industrial Base][research_labs_2025_cbo_shipbuilding]
- [Research, Martin and others 2022, Implications of a Coercive Quarantine of Taiwan][research_martin_2022_coercive_quarantine]
- [Research, Martin and others 2023, Supply Chain Interdependence and Geopolitical Vulnerability, Taiwan and High-End Semiconductors][research_martin_2023_supply_chain_interdependence]
- [Research, McGregor and Blanchette 2026, After Annexation, How China Plans to Run Taiwan][research_mcgregor_2026_after_annexation]
- [Research, Nassar and others 2024, Quantifying Potential Effects of China’s Gallium and Germanium Export Restrictions on the United States Economy][research_usgs_2024_gallium_germanium]
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

[book_downes_2021_catastrophic_success]: https://doi.org/10.7591/cornell/9781501761140.001.0001
[book_edelstein_2010_occupational_hazards]: https://doi.org/10.7591/9780801458569
[book_fazal_2011_state_death]: https://doi.org/10.1515/9781400841448
[book_goemans_2000_war_and_punishment]: https://doi.org/10.1515/9781400823956
[book_harrison_1998_economics_ww2]: https://doi.org/10.1017/cbo9780511523632
[book_ikenberry_2019_after_victory]: https://doi.org/10.23943/princeton/9780691169217.001.0001
[book_ikle_2005_every_war_must_end]: https://cup.columbia.edu/book/every-war-must-end/9780231136679
[book_kalyvas_2006_logic_of_violence]: https://doi.org/10.1017/cbo9780511818462
[book_liberman_1998_does_conquest_pay]: https://doi.org/10.1515/9781400821747
[book_organski_kugler_1980_war_ledger]: https://doi.org/10.7208/chicago/9780226351841.001.0001
[book_reiter_2009_how_wars_end]: https://doi.org/10.1515/9781400831036
[book_rockoff_2012_economic_way_of_war]: https://doi.org/10.1017/cbo9781139046534
[book_talmadge_2015_dictators_army]: https://doi.org/10.7591/9781501701764
[book_vonyo_2018_economic_consequences]: https://doi.org/10.1017/9781316414927
[book_weisiger_2013_logics_of_war]: https://doi.org/10.7591/cornell/9780801451867.001.0001
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
[data_roc_cec_referendums]: https://db.cec.gov.tw/static/referendums/list/N.json
[data_ustr_2025_maritime]: https://ustr.gov/sites/default/files/enforcement/301Investigations/USTRReportChinaTargetingMaritime.pdf
[government_dod_2022_competition]: https://web.archive.org/web/20240102044927/https://media.defense.gov/2022/Feb/15/2002939087/-1/-1/1/STATE-OF-COMPETITION-WITHIN-THE-DEFENSE-INDUSTRIAL-BASE.PDF
[government_dod_2023_china_report]: https://web.archive.org/web/2024/https://media.defense.gov/2023/Oct/19/2003323409/-1/-1/1/2023-MILITARY-AND-SECURITY-DEVELOPMENTS-INVOLVING-THE-PEOPLES-REPUBLIC-OF-CHINA.PDF
[government_dod_2025_china_report]: https://media.defense.gov/2025/Dec/23/2003849070/-1/-1/1/ANNUAL-REPORT-TO-CONGRESS-MILITARY-AND-SECURITY-DEVELOPMENTS-INVOLVING-THE-PEOPLES-REPUBLIC-OF-CHINA-2025.PDF
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
[government_roc_petroleum_act]: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=J0020019
[government_uscc_2025_taiwan_chapter]: https://www.uscc.gov/sites/default/files/2025-11/Chapter_11--Taiwan.pdf
[government_ussbs_1945_overall_report]: https://books.google.com/books?id=4PBmAAAAMAAJ
[government_ussbs_1946_pacific_summary]: https://archive.org/download/summaryreportpac00unit/summaryreportpac00unit.pdf
[journal_altman_2020_territorial_conquest]: https://doi.org/10.1017/s0020818320000119
[journal_attinasi_2024_decoupling_costs]: https://doi.org/10.1111/twec.13655
[journal_baker_2021_large_transformers]: https://doi.org/10.18278/jcip.2.2.5
[journal_beaumier_cartwright_2023_cross_network]: https://doi.org/10.1093/isq/sqae003
[journal_bellais_2023_market_structures]: https://doi.org/10.1080/10242694.2023.2182869
[journal_blouin_2024_electricity_loss]: https://doi.org/10.1007/s13753-024-00574-6
[journal_bosker_2007_multiple_equilibria]: https://doi.org/10.1016/j.jue.2006.07.001
[journal_bown_wang_2024_semiconductors]: https://doi.org/10.1257/jep.38.4.81
[journal_brakman_2004_german_bombing]: https://doi.org/10.1093/jeg/4.2.201
[journal_brooks_wohlforth_2016_rise_and_fall]: https://doi.org/10.1162/isec_a_00225
[journal_brown_2015_recouping]: https://doi.org/10.1080/03050629.2015.1046598
[journal_bueno_de_mesquita_1992]: https://doi.org/10.2307/1964127
[journal_caverley_2025]: https://doi.org/10.1353/tns.00004
[journal_cerra_saxena_2008_myth_of_recovery]: https://doi.org/10.1257/aer.98.1.439
[journal_cha_2023_collective_resilience]: https://doi.org/10.1162/isec_a_00465
[journal_chan_2025_resilience]: https://doi.org/10.1007/s13753-025-00657-y
[journal_chen_evers_2023_wars_without_gun_smoke]: https://doi.org/10.1162/isec_a_00473
[journal_chenoweth_2020_future_of_resistance]: https://doi.org/10.1353/jod.2020.0046
[journal_chenoweth_lewis_2013_navco]: https://doi.org/10.1177/0022343312471551
[journal_collier_1999_economic_consequences]: https://doi.org/10.1093/oep/51.1.168
[journal_collier_hoeffler_2004_aid_policy_growth]: https://doi.org/10.1016/j.euroecorev.2003.11.005
[journal_costalli_2017_economic_costs]: https://doi.org/10.1177/0022343316675200
[journal_coupe_2019_nuclear_winter_responses]: https://doi.org/10.1029/2019jd030509
[journal_croco_2011]: https://doi.org/10.1017/S0003055411000219
[journal_croco_weeks_2016_war_outcomes_tenure]: https://doi.org/10.1017/s0043887116000071
[journal_cunningham_fravel_2019_dangerous_confidence]: https://doi.org/10.1162/isec_a_00359
[journal_davis_gholz_2026_blockade_by_fire]: https://doi.org/10.1162/isec.a.407
[journal_davis_weinstein_2002]: https://doi.org/10.1257/000282802762024502
[journal_davis_weinstein_2008_multiple_equilibria]: https://doi.org/10.1111/j.1467-9787.2008.00545.x
[journal_debs_goemans_2010]: https://doi.org/10.1017/S0003055410000195
[journal_dell_querubin_2018_nation_building]: https://doi.org/10.1093/qje/qjx037
[journal_deutch_2022_consolidation]: https://doi.org/10.22594/dau.21-889.29.02
[journal_dillon_2014_shelter_times]: https://doi.org/10.1098/rspa.2013.0693
[journal_dilonardo_2020_autocratic_stability]: https://doi.org/10.1017/s0003055420000489
[journal_dworschak_2023_streetlight]: https://doi.org/10.5129/001041523x16745900727169
[journal_eichengreen_ritschl_2009]: https://doi.org/10.1007/s11698-008-0035-7
[journal_fabbrini_2024_defence_union]: https://doi.org/10.54648/eerr2024004
[journal_fearon_1995_rationalist_explanations]: https://doi.org/10.1017/s0020818300033324
[journal_federle_2026_price_of_war]: https://doi.org/10.1257/aer.20241355
[journal_feigenbaum_2022_capital_destruction]: https://doi.org/10.1257/app.20200397
[journal_felbermayr_2023_cutting_value_chain]: https://doi.org/10.1007/s10663-022-09561-w
[journal_ferreira_critelli_2023_food_resiliency]: https://doi.org/10.55540/0031-1723.3222
[journal_field_2023_manufacturing_productivity]: https://doi.org/10.1111/ehr.13239
[journal_flavin_2003_conflict_termination]: https://doi.org/10.55540/0031-1723.2162
[journal_fortna_2003_scraps_of_paper]: https://doi.org/10.1017/s0020818303572046
[journal_fravel_2005_regime_insecurity]: https://doi.org/10.1162/016228805775124534
[journal_friedman_2011_manpower]: https://doi.org/10.1080/09636412.2011.625768
[journal_fu_2024_human_cost_of_war]: https://doi.org/10.1177/07388942241290445
[journal_fuhrmann_tkach_2015_nuclear_latency]: https://doi.org/10.1177/0738894214559672
[journal_gao_2022_unjust_failed_transition]: https://doi.org/10.1016/j.esr.2022.100991
[journal_gavin_2010_same_as_it_ever_was]: https://doi.org/10.1162/isec.2010.34.3.7
[journal_gholz_sapolsky_2000_restructuring]: https://doi.org/10.1162/016228899560220
[journal_girod_2011_effective_foreign_aid]: https://doi.org/10.1111/j.1540-5907.2011.00552.x
[journal_glick_taylor_2010]: https://doi.org/10.1162/rest.2009.12023
[journal_goemans_2008_which_way_out]: https://doi.org/10.1177/0022002708323316
[journal_goemans_2009_archigos]: https://doi.org/10.1177/0022343308100719
[journal_goes_bekkers_2022_geopolitical_conflicts]: https://doi.org/10.30875/25189808-2022-9
[journal_goode_2009_force_requirements]: https://doi.org/10.55540/0031-1723.2499
[journal_green_talmadge_2022]: https://doi.org/10.1162/isec_a_00437
[journal_hartzell_2003_institutionalizing_peace]: https://doi.org/10.1111/1540-5907.00022
[journal_hellberg_2025_european_chains]: https://doi.org/10.31374/sjms.303
[journal_hellberg_2026_supply_chains]: https://doi.org/10.1080/10242694.2026.2655381
[journal_henry_2020_what_allies_want]: https://doi.org/10.1162/isec_a_00375
[journal_hess_2021_two_views]: https://doi.org/10.1080/25751654.2021.1882772
[journal_hiim_2023_entangled_security_dilemma]: https://doi.org/10.1162/isec_a_00457
[journal_hornbeck_keniston_2017_creative_destruction]: https://doi.org/10.1257/aer.20141707
[journal_hultman_2014_beyond_keeping_peace]: https://doi.org/10.1017/s0003055414000446
[journal_hyatt_2025_shrinking_base]: https://doi.org/10.22594/dau.24-932.32.02
[journal_ikenberry_2018_end_of_liberal_order]: https://doi.org/10.1093/ia/iix241
[journal_jagermeyr_2020_food_security]: https://doi.org/10.1073/pnas.1919049117
[journal_javorcik_2024_friendshoring]: https://doi.org/10.1111/twec.13555
[journal_jehn_2025_food_trade]: https://doi.org/10.5194/esd-16-1585-2025
[journal_king_2022_urban_insurgency]: https://doi.org/10.1093/ia/iiac007
[journal_knezevic_2026_capacity_gap]: https://doi.org/10.5937/vojdelo2602137k
[journal_koubi_2005]: https://doi.org/10.1177/0022343305049667
[journal_kowalski_2025_nato_pledge]: https://doi.org/10.55016/2cfa0x64
[journal_kristensen_2025_chinese_nuclear_weapons]: https://doi.org/10.1080/00963402.2025.2467011
[journal_lai_2026_lost_in_words]: https://doi.org/10.1093/poq/nfag007
[journal_lalwani_2017_size_still_matters]: https://doi.org/10.1080/09592318.2016.1263470
[journal_lau_tsai_2022_decarbonization_roadmap]: https://doi.org/10.3390/su14148425
[journal_lee_2024_taiwan_attitudes]: https://doi.org/10.58570/WRON8266
[journal_licklider_1995_negotiated_settlements]: https://doi.org/10.2307/2082982
[journal_lyall_wilson_2009_rage_machines]: https://doi.org/10.1017/s0020818309090031
[journal_mangold_2026_cultural_factors]: https://doi.org/10.21315/ijaps2026.22.2.8
[journal_mearsheimer_2019_bound_to_fail]: https://doi.org/10.1162/isec_a_00342
[journal_mearsheimer_2025_war_and_politics]: https://doi.org/10.1162/isec_a_00507
[journal_miguel_roland_2011]: https://doi.org/10.1016/j.jdeveco.2010.07.004
[journal_miguel_roland_2024_corrigendum]: https://doi.org/10.1016/j.jdeveco.2023.103151
[journal_mok_2026_undersea_cable_resilience]: https://doi.org/10.1353/tns.00041
[journal_mueller_2012_comment]: https://doi.org/10.1257/aer.102.7.3774
[journal_nemeth_2026_suez_moment]: https://doi.org/10.1353/tns.00025
[journal_nguyen_2025_german_cities]: https://doi.org/10.1016/j.gcrs.2025.100004
[journal_organski_kugler_1977]: https://doi.org/10.2307/1961484
[journal_peterson_2021_black_summer]: https://doi.org/10.1038/s41612-021-00192-9
[journal_phayal_2019_peacekeeping]: https://doi.org/10.1080/03050629.2019.1593161
[journal_piplani_talmadge_2015_war_helps]: https://doi.org/10.1177/0022002714567950
[journal_powell_2006_commitment_problem]: https://doi.org/10.1017/s0020818306060061
[journal_quek_johnston_2018]: https://doi.org/10.1162/isec_a_00303
[journal_rajan_subramanian_2008_aid_and_growth]: https://doi.org/10.1162/rest.90.4.643
[journal_redding_2011_history_industry_location]: https://doi.org/10.1162/rest_a_00096
[journal_reisner_2018]: https://doi.org/10.1002/2017JD027331
[journal_reisner_2019_reply]: https://doi.org/10.1029/2019jd031281
[journal_riano_2024_collateral_damage]: https://doi.org/10.1093/ej/ueae004
[journal_rivers_2024_food_system_adaptation]: https://doi.org/10.1016/j.gfs.2024.100807
[journal_robock_2019_comment]: https://doi.org/10.1029/2019JD030777
[journal_salavrakos_2017_japanese_armaments]: https://doi.org/10.1080/10242694.2017.1293776
[journal_scarazzato_2024_arms_production]: https://doi.org/10.1080/10242694.2024.2381784
[journal_scherrer_2020_fisheries]: https://doi.org/10.1073/pnas.2008256117
[journal_scouras_2019_global_catastrophic_risk]: https://doi.org/10.1017/bca.2019.16
[journal_shi_2025_adapting_agriculture]: https://doi.org/10.1088/1748-9326/adcfb5
[journal_shirkey_2016_uncertainty_duration]: https://doi.org/10.1093/isr/viv005
[journal_siodla_2015_razing_san_francisco]: https://doi.org/10.1016/j.jue.2015.07.001
[journal_slantchev_2003_power_to_hurt]: https://doi.org/10.1017/s000305540300056x
[journal_stanley_sawyer_2009]: https://doi.org/10.1177/0022002709343194
[journal_stephan_chenoweth_2008_why_civil_resistance]: https://doi.org/10.1162/isec.2008.33.1.7
[journal_stringer_2023_urban_resistance]: https://doi.org/10.55540/0031-1723.3244
[journal_sudduth_2017_elite_purges]: https://doi.org/10.1177/0010414016688004
[journal_sukin_2019_credible_commitments_backfire]: https://doi.org/10.1177/0022002719888689
[journal_talmadge_2017_would_china_go_nuclear]: https://doi.org/10.1162/isec_a_00274
[journal_tarshish_romps_2022_latent_heating]: https://doi.org/10.1029/2022jd036667
[journal_thyne_2012_intra_war_bargaining]: https://doi.org/10.1111/j.1468-2478.2012.00719.x
[journal_toon_2007_atmospheric_effects]: https://doi.org/10.5194/acp-7-1973-2007
[journal_vonyo_2012_bombing_of_germany]: https://doi.org/10.1093/ereh/her006
[journal_wagman_2020_multiscale]: https://doi.org/10.1029/2020jd033056
[journal_waldinger_2016_bombs_brains]: https://doi.org/10.1162/rest_a_00565
[journal_walter_1997_critical_barrier]: https://doi.org/10.1162/002081897550384
[journal_weeks_2012_strongmen]: https://doi.org/10.1017/s0003055412000111
[journal_weisiger_2016_learning_battlefield]: https://doi.org/10.1017/s0020818316000059
[journal_werner_yuen_2005_making_keeping_peace]: https://doi.org/10.1017/s0020818305050095
[journal_wolford_2011_information_commitment]: https://doi.org/10.1177/0022002710393921
[journal_wolford_2017_shared_victory]: https://doi.org/10.1086/688700
[journal_wu_2023_taiwan_security]: https://doi.org/10.1080/23311983.2023.2220211
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
[research_crosignani_2024_geopolitical_risk]: https://doi.org/10.59576/sr.1096
[research_delong_eichengreen_1991_marshall]: https://www.nber.org/system/files/working_papers/w3899/w3899.pdf
[research_dobbins_2003_nation_building]: https://doi.org/10.7249/mr1753
[research_evans_2023_alternative_futures_v2]: https://www.rand.org/pubs/research_reports/RRA591-2.html
[research_funaiole_2026_testimony]: https://docs.house.gov/meetings/FA/FA05/20260722/119432/HHRG-119-FA05-Wstate-FunaioleM-20260722.pdf
[research_gao_1998_defense_consolidation]: https://web.archive.org/web/2024/https://www.gao.gov/assets/nsiad-98-141.pdf
[research_gao_2022_industrial_base]: https://web.archive.org/web/2024/https://www.gao.gov/assets/gao-22-104154.pdf
[research_gao_2025_shipbuilding_workforce]: https://files.gao.gov/reports/GAO-25-106286/index.html
[research_garlauskas_2025_guardian_tiger]: https://www.atlanticcouncil.org/in-depth-research-reports/report/a-rising-nuclear-double-threat-in-east-asia-insights-from-our-guardian-tiger-i-and-ii-tabletop-exercises/
[research_gerber_2026_workforce]: https://doi.org/10.7249/rra3665-2
[research_goldberg_2024_industrial_policy]: https://doi.org/10.3386/w32651
[research_gompert_2016_war_with_china]: https://www.rand.org/content/dam/rand/pubs/research_reports/RR1100/RR1140/RAND_RR1140.pdf
[research_gunzinger_2026_rebuilding_air_force]: https://www.mitchellaerospacepower.org/app/uploads/2026/04/Rebuilding-Americas-Air-Force-FINAL.pdf
[research_heath_2023_can_taiwan_resist]: https://doi.org/10.7249/rra1658-1
[research_jones_2023_empty_bins]: https://csis-website-prod.s3.amazonaws.com/s3fs-public/2023-01/230119_Jones_Empty_Bins.pdf
[research_krepinevich_2020_protracted_great_power_war]: https://www.cnas.org/publications/reports/protracted-great-power-war
[research_labs_2025_cbo_shipbuilding]: https://www.cbo.gov/publication/61218
[research_martin_2022_coercive_quarantine]: https://doi.org/10.7249/rra1279-1
[research_martin_2023_supply_chain_interdependence]: https://doi.org/10.7249/rra2354-1
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
[research_usgs_2024_gallium_germanium]: https://doi.org/10.3133/ofr20241057
[research_world_bank_1996_bosnia]: https://documents.worldbank.org/curated/en/998241468743939643/pdf/multi0page.pdf
[research_world_bank_2025_rdna4]: https://documents.worldbank.org/curated/en/099022025114040022/pdf/P1801741ca39ec0d81b5371ff73a675a0a8.pdf
