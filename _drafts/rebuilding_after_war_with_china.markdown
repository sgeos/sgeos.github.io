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

The constraint here is not money but yards.
[Labs 2025][research_labs_2025_cbo_shipbuilding]
at the Congressional Budget Office records that essentially all Navy battle force ships
are built by seven shipyards,
that destroyers and submarines took five to six years to build in the 2000s
and now take eight to nine years on average,
and that a new submarine takes about nine years.

The CSIS passage names two yards for large surface combatants
and puts the loss at a dozen or more.
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

The structural cause is consolidation.
Following the 1993 meeting known as the Last Supper,
the number of aerospace and defence prime contractors fell from 51 to 5.
[Rumbaugh 2026][research_rumbaugh_2026_solid_rocket_motors]
records the same pattern in solid rocket motors,
where the domestic supplier base shrank from six to two between 2000 and 2015.

### The workforce, which is the constraint behind the others

[Government Accountability Office 2025][research_gao_2025_shipbuilding_workforce]
reports that over the next decade the shipbuilding industrial base
"will require 174,000 new workers to keep pace with Navy shipbuilding goals",
and that all seven shipbuilders face workforce limitations.

$$
\frac{174{,}000}{10} = 17{,}400 \ \text{workers per year}
$$

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
The Navy confirmed the slide's authenticity and simultaneously limited it,
stating that it was "developed by the Office of Naval Intelligence from multiple public sources
as part of an overall brief on strategic competition"
and was "not intended as a deep-dive into the PRC commercial shipbuilding industry".
The reporter noted that it is unclear how much commercial capacity
the United States figure incorporates.

The defensible comparison comes from
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
The bombing "destroyed almost half of all structures in these cities,
a total of 2.2 million buildings",
two thirds of productive capacity vanished,
300,000 people were killed,
and 40 percent of the urban population was made homeless.
Hiroshima lost more than two thirds of its built-up area
and more than 20 percent of its population.

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

The inference the authors draw is that Germany grew at nearly 8 percent a year through the 1950s
because it had been pushed off its path temporarily rather than stripped of its plant,
and that "More than half the economy's growth in the 1950s remains to be explained"
by capital accumulation alone.

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

### The phoenix factor

[Organski and Kugler 1977][journal_organski_kugler_1977]
examined 32 cases and found that while losers' power is eroded at first,
"the effects of the loss dissipate,
losers accelerate their recovery and soon resume antebellum status"
over a long run they put at fifteen to twenty years.
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

Three years is fast by the standards of the fifteen-year literature.
It is very slow by the standards of a war that the games end in three weeks,
and nothing in the estimate assumes the war is still going on.

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

[Tarnoff 2018][research_tarnoff_2018_marshall_plan]
gives the official totals,
roughly 13.3 billion dollars to 16 countries from April 1948 to June 1952,
about 143 billion in 2017 dollars,
with the first-year appropriation of 4 billion amounting to roughly 13 percent
of a federal budget near 30 billion dollars.
**No figure for the plan as a share of donor gross domestic product
appears in that source**,
and none is asserted here.

### What reconstruction costs when somebody measures it

[The World Bank and partners 2025][research_world_bank_2025_rdna4]
assessed Ukraine after almost three years of war.
Direct damage reached 176 billion dollars,
and total reconstruction and recovery needs over the next decade reached 524 billion,
which the assessment puts at approximately 2.8 times Ukraine's 2024 nominal gross domestic product.
Thirteen percent of the housing stock was damaged or destroyed.

That ratio is the most transferable quantity in the reconstruction literature,
because it is dimensionless.

$$
\frac{\text{reconstruction needs}}{\text{annual output}} \approx 2.8
$$

For comparison of scale rather than of case,
[SIGIR 2013][research_sigir_2013_learning_from_iraq]
recorded 60.64 billion dollars of United States relief and reconstruction funding for Iraq
across nine years,
averaging more than 15 million dollars a day,
with at least 8 billion judged wasted.
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

Taiwan's population is about 23.4 million.
Writing $P$ for population and $\rho$ for the required ratio per thousand,
the requirement follows.

$$
F = \rho \times \frac{P}{1000} = 20 \times 23{,}400 = 468{,}000 \ \text{personnel}
$$

Quinlivan also states a rule of five for sustainment,
five personnel in the force for each one deployed on a six-month rotation.

$$
5 \times 468{,}000 = 2{,}340{,}000 \ \text{personnel}
$$

**This calculation is my own and appears in no source located.**
It applies a ratio derived from Bosnia, Kosovo, Somalia, Haiti, Afghanistan and Iraq
to a case none of those resembles,
and it assumes a garrison model rather than a compliant population.
It is offered as the order of magnitude the published literature implies,
and as evidence that the two bodies of work have never been joined.
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
model soot injection against food supply.
At 5 teragrams of soot from 100 weapons,
direct fatalities are 27 million and 255 million people are without food at the end of year two.
At 150 teragrams from 4,400 weapons,
direct fatalities are 360 million
and 5.341 billion people are without food.
Global mean surface temperature falls 1.5 degrees Celsius at the low end
and 14.8 degrees at the high end,
and the climatic impacts "would last for about a decade".

The ratio between the direct and the indirect toll is the finding.

$$
\frac{255}{27} \approx 9.4 \ \text{at 5 Tg},
\qquad
\frac{5{,}341}{360} \approx 14.8 \ \text{at 150 Tg}
$$

[Shi and others 2025][journal_shi_2025_adapting_agriculture]
address recovery rather than damage,
finding maize production down 7 percent at 5 teragrams and 80 percent at 150,
"with recovery taking 7 to 12 years",
and seed availability as the binding bottleneck.
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
synthesis states that major uncertainties limit modelling at every stage of the causal pathway,
and it explicitly excluded radioactive fallout,
which matters for any recovery argument built on it.

**Every one of those studies models South Asia or the United States and Russia.**
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
[Nemeth 2026][journal_nemeth_2026_suez_moment]
gives the two paths for the alliance system after a visible defeat,
a hollowing into ceremonial shells
or an adaptation in which the United States becomes first among equals.
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
The consequence studies are about other theatres.
- **The occupation force-density literature and the invasion literature have never been joined.**
The arithmetic above took minutes and appears nowhere.

A fifth observation follows from the four.
There appears to be no published work whose central thesis
is that the wargaming literature ignores the aftermath.
What exists is adjacent and assemblable,
which is what this article has done.

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
The World Bank press release for the Ukraine figures.

**Verified against the registry rather than read.**
Every journal citation was checked against Crossref for title, authors, journal, volume, issue, year and pages.
Several of those articles exist for this article only as registry records and abstracts,
because MIT Press, Oxford University Press, Wiley, Sage, Taylor and Francis and JSTOR
all refuse automated clients.
Where an abstract is the only layer verified, no number from inside the article is quoted.

**Documented only through a summary or a press account.**
The 200-to-1 shipbuilding slide, through the outlet that obtained it and the Navy's own caveat.
The Nature Food soot table, through a research sweep's extraction rather than my own reading.
The National Academies synthesis, through its catalogue page.

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

**Not verified and therefore absent.**
Any figure for the Marshall Plan as a share of donor output.
Any figure for occupation-era aid to Japan.
Any estimate of Taiwan's own reconstruction cost or of its grid resilience programme.
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
Losers of major wars resume antebellum standing within fifteen to twenty years.

Throughput and relationships do not heal on that clock.
Two shipyards build large surface combatants,
a destroyer takes eight to nine years,
and the report that sinks a dozen of them says replacement would take decades.
Carriers have no replacement rate at all,
because the yards can only sustain the fleet that exists.
Munitions run on a 52-month cycle
and the anti-ship missiles the games consume in the first week
are the ones a peer war needs most.
Replacing programme inventories takes 8.4 years at surge rates,
and that figure explicitly excludes combat losses.
Leading-edge semiconductor capacity takes a minimum of three years
and 350 billion dollars to rebuild somewhere else.
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
about 468,000 personnel for Taiwan and roughly five times that to sustain them,
took minutes to compute and appears in none of it.

A literature that models the first three weeks in twenty-four iterations
and the following twenty years in one conditional clause
is not describing a war.
It is describing a battle,
and then stopping where the hard part starts.

## References

- [Book, Goemans 2000, War and Punishment][book_goemans_2000_war_and_punishment]
- [Book, Ikenberry 2019, After Victory][book_ikenberry_2019_after_victory]
- [Book, Ikle 2005, Every War Must End][book_ikle_2005_every_war_must_end]
- [Book, Reiter 2009, How Wars End][book_reiter_2009_how_wars_end]
- [Commentary, Blanchette and McGregor 2026, After the Invasion, China Considers the Problem of Ruling Taiwan][commentary_blanchette_2026_after_invasion]
- [Commentary, Heath 2023, Wargames Cannot Tell Us How to Deter a Chinese Attack on Taiwan][commentary_heath_2023_wargames_deterrence]
- [Commentary, Heim, Burdette and Beauchamp-Mustafaga 2024, Denial Is the Worst Except for All the Others][commentary_heim_2024_denial_worst]
- [Commentary, Sudduth 2026, Double-Edged Swords, How Military Purges Shape Authoritarian Appetite for War][commentary_sudduth_2026_double_edged_swords]
- [Commentary, Tetreau 2023, Where the Wargames Were Not][commentary_tetreau_2023_where_the_wargames_were_not]
- [Commentary, Trevithick 2023, Alarming Navy Intelligence Slide on Chinese Shipbuilding Capacity][commentary_twz_2023_oni_slide]
- [Data, Boston Consulting Group and Semiconductor Industry Association 2021, Strengthening the Global Semiconductor Value Chain][data_bcg_sia_2021_value_chain]
- [Data, Chicago Council on Global Affairs 2022, Thinking Nuclear, South Korean Attitudes on Nuclear Weapons][data_chicago_council_2022_south_korea]
- [Data, Office of the United States Trade Representative 2025, Report on China's Targeting of the Maritime, Logistics and Shipbuilding Sectors][data_ustr_2025_maritime]
- [Government, Office of the Director of National Intelligence 2026, Annual Threat Assessment][government_odni_2026_threat_assessment]
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
- [Research, Gompert, Cevallos and Garafola 2016, War with China, Thinking Through the Unthinkable][research_gompert_2016_war_with_china]
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
- [Research, Quinlivan 2003, Burden of Victory, the Painful Arithmetic of Stability Operations][research_quinlivan_2003_burden_of_victory]
- [Research, Rumbaugh 2026, Solid Rocket Motors for Missile Defense][research_rumbaugh_2026_solid_rocket_motors]
- [Research, Special Inspector General for Iraq Reconstruction 2013, Learning From Iraq][research_sigir_2013_learning_from_iraq]
- [Research, Stewart 2023, Island Blitz, a Campaign Analysis of a Taiwan Takeover][research_stewart_2023_island_blitz]
- [Research, Tarnoff 2018, The Marshall Plan, Design, Accomplishments, and Significance][research_tarnoff_2018_marshall_plan]
- [Research, World Bank 1996, Bosnia and Herzegovina, the Priority Reconstruction and Recovery Program][research_world_bank_1996_bosnia]
- [Research, World Bank and partners 2025, Ukraine Fourth Rapid Damage and Needs Assessment][research_world_bank_2025_rdna4]

[book_goemans_2000_war_and_punishment]: https://doi.org/10.1515/9781400823956
[book_ikenberry_2019_after_victory]: https://doi.org/10.23943/princeton/9780691169217.001.0001
[book_ikle_2005_every_war_must_end]: https://cup.columbia.edu/book/every-war-must-end/9780231136679
[book_reiter_2009_how_wars_end]: https://doi.org/10.1515/9781400831036
[commentary_blanchette_2026_after_invasion]: https://warontherocks.com/after-the-invasion-china-considers-the-problem-of-ruling-taiwan/
[commentary_heath_2023_wargames_deterrence]: https://www.rand.org/pubs/external_publications/EP70064.html
[commentary_heim_2024_denial_worst]: https://warontherocks.com/2024/06/denial-is-the-worst-except-for-all-the-others-getting-the-u-s-theory-of-victory-right-for-a-war-with-china/
[commentary_sudduth_2026_double_edged_swords]: https://warontherocks.com/double-edged-swords-how-military-purges-shape-authoritarian-appetite-for-war/
[commentary_tetreau_2023_where_the_wargames_were_not]: https://warontherocks.com/2023/09/where-the-wargames-werent-assessing-10-years-of-u-s-chinese-military-assessments/
[commentary_twz_2023_oni_slide]: https://www.twz.com/alarming-navy-intel-slide-warns-of-chinas-200-times-greater-shipbuilding-capacity
[data_bcg_sia_2021_value_chain]: https://www.semiconductors.org/wp-content/uploads/2021/05/BCG-x-SIA-Strengthening-the-Global-Semiconductor-Value-Chain-April-2021_1.pdf
[data_chicago_council_2022_south_korea]: https://globalaffairs.org/research/public-opinion-survey/thinking-nuclear-south-korean-attitudes-nuclear-weapons
[data_ustr_2025_maritime]: https://ustr.gov/sites/default/files/enforcement/301Investigations/USTRReportChinaTargetingMaritime.pdf
[government_odni_2026_threat_assessment]: https://archive.dni.gov/files/ODNI/documents/assessments/ATA-2026-Unclassified-Report.pdf
[government_uscc_2025_taiwan_chapter]: https://www.uscc.gov/sites/default/files/2025-11/Chapter_11--Taiwan.pdf
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
[research_quinlivan_2003_burden_of_victory]: https://www.rand.org/content/dam/rand/pubs/corporate_pubs/2007/RAND_CP22-2003-08.pdf
[research_rumbaugh_2026_solid_rocket_motors]: https://csis-website-prod.s3.amazonaws.com/s3fs-public/2026-06/260612_Rumbaugh_Rocket_Motors.pdf
[research_sigir_2013_learning_from_iraq]: https://web.archive.org/web/20131104045644id_/http://www.sigir.mil/files/learningfromiraq/Report_-_March_2013.pdf
[research_stewart_2023_island_blitz]: https://cimsec.org/island-blitz-a-campaign-analysis-of-a-taiwan-takeover-by-the-pla/
[research_tarnoff_2018_marshall_plan]: https://www.everycrsreport.com/reports/R45079.html
[research_world_bank_1996_bosnia]: http://documents.worldbank.org/curated/en/998241468743939643/pdf/multi0page.pdf
[research_world_bank_2025_rdna4]: https://www.worldbank.org/en/news/press-release/2025/02/25/updated-ukraine-recovery-and-reconstruction-needs-assessment-released
