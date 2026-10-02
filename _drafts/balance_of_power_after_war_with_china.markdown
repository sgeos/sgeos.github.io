---
layout: post
mathjax: true
comments: true
title:  "Whether a War With China Would Change the Global Balance of Power"
date:   2026-08-13 09:00:00 +0000
categories: geopolitics military war-gaming
series: war_with_china
series_title: A War With China
series_index: 3
---

<!-- A376 -->
<script>console.log("A376");</script>

The [first article in this series][related_post_published_wargames]
read the published wargames of a war between the United States and the People's Republic of China,
or PRC,
and reported what they say about whether such a war is won.
The [second][related_post_rebuilding]
took up the reconstitution problem the games decline to model
and found that the published record stops at the point where the subject begins.
This article asks the question that motivates both.
Suppose the war happens.
What does it do to the distribution of power in the world?

The honest answer begins with a measurement problem and ends with a base rate,
and neither is what the scenario literature leads a reader to expect.
**The standard quantitative index of national capability
already places China ahead of the United States,
and has done so in every year since 1995 but one.**
On the same index the two prospective belligerents together hold
just over a third of world capability,
against the eighty-two percent held by the belligerents of 1914
and the ninety-eight percent held by those of 1939.
Those two facts together do most of the work in this article.
The first means that a war fought to arrest a transition
would be fought after the transition had already been recorded by the instrument
most often used to detect it.
The second means that, for the first time in the record of great-power war,
there exists a pool of non-participants large enough
to absorb a substantial redistribution of relative standing.

The title asks whether, and the qualification is not rhetorical.
Across ninety-five inter-state wars between 1823 and 2003
the median belligerent came out of the following decade
with its share of world capability
about seven percent higher in relative terms than it went in.
Winners did better than losers
and the difference is statistically distinguishable from zero,
but **thirty-eight percent of the winners of those wars
held a smaller share of world capability ten years later than before the fighting began.**
Victory is not a reliable instrument for improving one's position.
Among the largest wars the asymmetry sharpens into something stranger,
and that result is developed below.

This article does three things the surveyed literature does not do.
It computes the base rate rather than asserting one.
It shows that the measurement instrument determines the answer,
with a worked decomposition of the index that is usually quoted without one.
And it takes the index's own documented caveats,
which are real and are routinely ignored by works that cite it,
and puts numbers on them.
One of those caveats raises the recorded capability
of exactly those states whose underlying data are worst,
and another cuts the recorded urban population of the United States
by forty-four percent in a single year.

* Contents
{:toc}

## What the First Two Articles Left Open

The first article established that the public analytical record
describes a war that is extraordinarily costly to both sides
and whose military outcome the games do not agree on.
The second established that the record stops before reconstitution,
that the published horizon is about three weeks in the most cited games
and day forty-six in the most detailed public campaign model,
and that no public game located for that article
continues into the period after the fighting.

Both articles therefore left the same thing open.
A war is instrumental.
States fight for a position afterwards,
and the published work on this contingency
concentrates almost entirely on the fighting.
[Priebe and others 2023][research_priebe_2023_alternative_futures_v1]
is the closest published match located for either article,
and its companion [volume on historical cases][research_evans_2023_alternative_futures_v2]
states plainly that "the long-term consequences of such a conflict remain poorly understood".

That sentence is the warrant for this article,
and it also sets the standard this article has to meet.
A survey that merely collected more assertions about the postwar order
would add confidence without adding information.
So the organising decision here is to begin from data
that exist independently of anyone's scenario,
and to be explicit about what those data can and cannot support.

## The Measure Decides the Answer

Any claim about the balance of power presupposes an instrument.
The instrument most used in quantitative international relations research
is the Composite Index of National Capability,
or CINC,
introduced by [Singer, Bremer and Stuckey in 1972][book_singer_1972_capability_distribution]
and maintained since by the Correlates of War project.
It is worth stating precisely what it does,
because the answer to this article's question
changes sign depending on which instrument is chosen,
and that dependence is rarely shown.

### What the index is

The [Correlates of War National Material Capabilities documentation][data_cow_nmc_v7]
defines the index as follows.
It "reflects an average of a state's share of the system total
of each element of capabilities in each year,
weighting each component equally".
The six elements are military expenditure, military personnel,
iron and steel production, primary energy consumption,
total population and urban population.
Writing $x_{c,i,t}$ for the value of component $c$
held by state $i$ in year $t$,
each component share is that state's part of the world total.

$$
s_{c,i,t} = \frac{x_{c,i,t}}{\sum_{j} x_{c,j,t}},
\qquad
\sum_{i} s_{c,i,t} = 1 \;\text{for every } c
$$

The index is then the mean of the six shares.

$$
\mathrm{CINC}_{i,t}
= \frac{1}{6} \sum_{c=1}^{6}
\frac{x_{c,i,t}}{\sum_{j} x_{c,j,t}}
$$

Because every term is a share of a world total,
the index is bounded between zero and one,
and summing it across all states in a year should give one.
A state's CINC is therefore read directly as its share of world capability.
That reading is what makes the index useful,
and it is also what a later subsection shows does not quite hold.

### The index already records the transition

Version 7.0 of the National Material Capabilities data,
released in 2025,
runs from 1816 to 2022,
and 2022 is the most recent year available in the series.
Computed from that file, with every year renormalised to sum to one
for reasons given below,
the two states in question stand as follows.

$$
\mathrm{CINC}_{\mathrm{CHN},\,2022} = 0.2325,
\qquad
\mathrm{CINC}_{\mathrm{USA},\,2022} = 0.1227
$$

The ratio is the quantity of interest.

$$
\frac{0.2325}{0.1227} \approx 1.89
$$

**On the most widely used quantitative index of national capability,
China held about one and nine tenths times the capability share of the United States
in the most recent year for which the index is published.**
Restricting attention to the one hundred and sixty states
present in the data in every year from 1990 to 2022,
so that the comparison is not disturbed by states entering or leaving the system,
the ratio crosses one between 1994 and 1995
and exceeds one in every subsequent year but one.
The exception is 2002, where it reads 0.9987,
and that single year turns out to be an artefact
of a documented break in one of the six component series,
which the subsection after next takes up.

| Year | China | United States | Ratio | India |
|------|-------|---------------|-------|-------|
| 1990 | 0.1159 | 0.1467 | 0.791 | 0.0625 |
| 1995 | 0.1484 | 0.1461 | 1.016 | 0.0680 |
| 2000 | 0.1685 | 0.1484 | 1.135 | 0.0719 |
| 2005 | 0.1772 | 0.1615 | 1.098 | 0.0785 |
| 2010 | 0.2146 | 0.1516 | 1.415 | 0.0816 |
| 2016 | 0.2358 | 0.1361 | 1.732 | 0.0892 |
| 2020 | 0.2430 | 0.1270 | 1.913 | 0.0981 |
| 2022 | 0.2394 | 0.1264 | 1.895 | 0.1016 |

Over that window China's share of capability among the constant set
roughly doubled while the American share fell by about a seventh.

$$
\frac{0.2394 - 0.1159}{0.1159} \approx +1.06,
\qquad
\frac{0.1264 - 0.1467}{0.1467} \approx -0.14
$$

Two features of that table are worth marking before the decomposition.
The Chinese share peaks in 2020 at 0.2430 and is slightly lower in 2022,
which is the first sustained reversal in the series since the 1990s
and is too short a run to interpret.
And the Indian column rises monotonically throughout,
which becomes the subject of a later section.

**Three different denominators appear in this article
and they give three different numbers for the same quantity**,
so the convention is stated once here.
The published index for 2022 gives China 0.2341 and the United States 0.1236.
Renormalising that year to its own observed total,
which is the convention used for the historical base rates below,
gives 0.2325 and 0.1227.
Restricting to the 160 states present throughout 1990 to 2022,
which is the convention in the table above,
gives 0.2394 and 0.1264.
The three levels are not interchangeable and each is labelled where it is used.
The ratio, by contrast, is identical under all three
and not merely similar.

$$
\left. \frac{\mathrm{CINC}_{\mathrm{CHN},\,2022}}{\mathrm{CINC}_{\mathrm{USA},\,2022}}
\right|_{\text{any reference set}} = 1.8945
$$

The equality is exact rather than approximate,
and the reason is worth stating because it governs
which quantities in this article deserve confidence.
Every one of those three conventions
divides both states by the same denominator,
so the denominator cancels in the ratio and cannot affect it.
Dividing the rounded figures quoted above
reproduces the ratio only to three places,
which is an artefact of the rounding and not a real disagreement.
**A ratio of two states' shares is invariant to the choice of reference set.
A level is not.**
Accordingly the ratios reported in this article are robust,
the levels carry the reference set with them,
and the comparisons across eras in later sections
are all constructed as ratios for that reason.

The first two agree exactly on the unrounded values,
since renormalising a year divides both states by the same total
and cannot change their ratio.
The third differs slightly because its denominator is a different set of states.
A quantity that is robust to the denominator
is reported with more confidence than one that is not,
and the levels in this article are much less robust than the ratios.

This is a strong claim and it should be weakened immediately,
because the index is not measuring what a reader is likely to assume.

### Which components produce that result

Decomposing the 2022 index into its six components
locates the entire result in three of them.
The table gives each state's share of the world total of each component,
in percent, computed from the same file.

| Component | China | United States | Ratio |
|-----------|-------|---------------|-------|
| Military expenditure | 10.83 | 41.57 | 0.26 |
| Military personnel | 9.79 | 6.54 | 1.50 |
| Iron and steel production | 53.89 | 4.26 | 12.64 |
| Primary energy consumption | 30.27 | 14.11 | 2.14 |
| Total population | 17.89 | 4.30 | 4.16 |
| Urban population | 17.79 | 3.35 | 5.31 |
| **Index, the average of the six** | **23.41** | **12.36** | **1.89** |

**The index says China leads because one sixth of it is iron and steel production,
where China held more than half of world output,
and because two further sixths are population measures.**
On the single component that most directly measures military capacity,
the United States led by nearly four to one.

$$
\frac{41.57}{10.83} \approx 3.84
$$

The underlying 2022 values make the asymmetry concrete.
Chinese iron and steel production is recorded as 1,017,959 thousand metric tons
against 80,535 for the United States,
while military expenditure is recorded as
218.6 billion current United States dollars against 838.8 billion.

$$
\frac{1{,}017{,}959}{80{,}535} \approx 12.64,
\qquad
\frac{838{,}814}{218{,}639} \approx 3.84
$$

Both of the components on which the index is decisive
are measured in tons and in people.
Neither is measured in anything a 2022 military would expend.

An index that gives steel tonnage and military spending equal weight
is an industrial-age instrument,
and it was designed as one.
That is not a hidden flaw.
It is the stated construction,
and it means the index answers the question
of which state could out-produce the other in a long industrial war,
which is a defensible thing to want to know
and is not the same as which state is more powerful today.
The gross-against-net distinction
is the standing objection to indices of this family,
and it is taken up with the alternative instruments below.

### The index does not sum to one, and the codebook says so

Working with the file rather than with the published summaries
surfaces a property that affects any share computed from the series.
The index is defined as an average of shares of world totals,
so across the states in any one year it should sum to one.
It does not.

**The project documents this, and the documentation deserves to be quoted
before anything is made of it.**
The codebook sets out the construction in three steps,
of which the third is the relevant one.

> For each state, the values of the non-missing shares are averaged
> to produce the CINC score.
> So if a state had share values of 0.01, 0.02, 0.02, 0.03, 0.03, and 0.076,
> the CINC (average) value would be 0.031.
> The average is computed across the non-missing components only.

It then states the consequence in the same paragraph.

> Because CINC is sometimes computed on a varying number of components,
> the sum of all CINC scores across all states in the system in any year
> may be slightly greater than or less than 1.0.

So the behaviour is deliberate and disclosed.
A state missing one or more components
is averaged over the components it has,
which is a defensible choice,
and the sums therefore depart from one.
Expressed as a formula,
with $A_{i,t}$ the set of components actually recorded,
the published value is the following
rather than the sixfold average given earlier.

$$
\mathrm{CINC}^{\text{published}}_{i,t}
= \frac{1}{|A_{i,t}|} \sum_{c \in A_{i,t}}
\frac{x_{c,i,t}}{\sum_{j} x_{c,j,t}}
$$

Where $A_{i,t}$ has all six members the two formulas agree.
Where it does not, the published value is larger
by the ratio of six to the number of components present.

$$
\frac{\mathrm{CINC}^{\text{published}}_{i,t}}
{\mathrm{CINC}_{i,t}} = \frac{6}{|A_{i,t}|}
$$

**What the article adds is the magnitude, because the word doing the work
in the codebook's sentence is "slightly".**
Summed over the states present in each year,
the published values exceed one in most years of the series.
The deviation reaches 1.0747 in 1860,
and the median absolute deviation across all 207 years is about 0.021.

$$
\max_{t} \left| \sum_{i} \mathrm{CINC}^{\text{published}}_{i,t} - 1 \right| = 0.0747,
\qquad
\operatorname{median}_{t} \left| \cdot \right| \approx 0.021
$$

**And 183 of the 207 years miss one by more than a thousandth.**

$$
\frac{183}{207} \approx 0.88
$$

Nearly nine years in ten fail the invariant
that makes the index readable as a share.
Recomputing the index from the six component columns
and dividing by six as the headline definition states
produces a sum of one in all 207 years,
to within floating-point rounding of one part in $10^{15}$,
which confirms that the averaging rule is the whole of the cause.

The per-state effect is larger than the aggregate suggests.
China in 1860 is the extreme case.
Military expenditure and urban population are both recorded as missing,
so the published index divides by four.

$$
0.17429 \;\text{published}, \qquad
0.11619 \;\text{on the sixfold definition}, \qquad
\frac{6}{4} = 1.5
$$

**The published series puts China's 1860 share of world capability
half again as high as the sixfold definition would.**
Across the whole file, 2,804 of 17,121 state-years,
or 16.4 percent,
have at least one missing component,
and the incidence falls sharply over time.

| Period | State-years with a missing component | Share |
|--------|--------------------------------------|-------|
| 1816 to 1899 | 1,266 of 2,922 | 43.3 percent |
| 1900 to 1949 | 603 of 2,792 | 21.6 percent |
| 1950 to 2022 | 935 of 11,407 | 8.2 percent |

The direction of the effect is what matters for a survey.
Missing data are not distributed at random across states.
They are concentrated where statistical capacity was weakest,
which in the nineteenth and early twentieth centuries
means disproportionately the non-European states.
**The averaging rule therefore raises the recorded capability
of precisely those states whose underlying measurement is worst,
and by a mechanism invisible unless the component columns are inspected.**

One small discrepancy is worth recording
because it bears on how current the documentation is.
The codebook states that
"83.29% of the state-year observations in the set have data on all six components;
13.76% have data on five; 2.71% have data on four;
0.23% of cases have data only on two or three components".
Recomputed on the version 7.0 file those figures are
83.62, 13.50, 2.66 and 0.22 percent.

$$
83.29 \longrightarrow 83.62,
\qquad
13.76 \longrightarrow 13.50,
\qquad
2.71 \longrightarrow 2.66
$$

The differences are small and in no way change the picture,
but they indicate the passage was carried forward from an earlier version
rather than regenerated,
which is a reason to verify the documentation's numbers
against the file a reader actually has.

### Three breaks in the series, all of them documented

The averaging rule is a property of the published column.
The next problem is a property of the underlying measurements.
Three discontinuities matter here,
and the project documents every one of them.
**What this article adds is not their discovery but their size
in the one comparison most readers of the index care about.**

**The industrial component changes what it measures in 1900.**

> Iron and Steel production reflects a state's production of
> pig iron (1816-1899) and steel (1900-2012) in each year for the period 1816-2012.

The codebook is candid about the choice of year.

> By 1900, the preferred product of this economic sector was clearly steel,
> hence our use of steel output as an indicator.
> This date is somewhat arbitrary since any year from 1890 to around 1910
> could have been chosen for the same reason.

That splice falls inside the period from which most of this article's
base rates are drawn,
and it sits between the Franco-Prussian War and the First World War.
Any comparison straddling 1900 on this component
compares pig iron with steel.

**The urban component changes what it counts in 2002.**
Through 2001 the variable is
"population living in cities with population greater than 100,000".
From 2002 it is built instead from United Nations urban agglomerations,
and the codebook describes the construction plainly.

> These data report population values for cities with populations over 300,000
> in the period 1950-2014.
> In order to construct the data, we summed the population values
> for all cities identified as an urban agglomeration
> of 300,000 or more people during a given year.

Two things change at once.
The threshold rises from one hundred thousand to three hundred thousand,
which removes every city between those sizes,
and the unit changes from the city proper to the agglomeration,
which adds suburbs.
The first subtracts most from states with many mid-sized cities.

**The project checked whether this mattered and reported that it did not.**

> Because the transition to urban agglomeration as a measure of urban population
> is an important change to the NMC data,
> we conducted a series of analyses to explore the extent
> to which such a change impacted the CINC values of states.
> Looking at data over the 1950-2007 period,
> we observed an overall correlation between the existing urban population value
> and the urban agglomeration measure of approximately .89.

> The mean difference in magnitude between the existing urban population measures
> and the urban agglomeration measure is approximately 35%.

And on the index itself, a correlation of about 0.99
between the series computed each way.

**That 0.99 is the right statistic for the wrong question.**
It is computed across the whole panel of states,
so it is dominated by the large majority
for whom the change is small or offsetting.
It bounds the error for a researcher using the panel.
It does not bound the error in any particular bilateral comparison,
and the bilateral comparison is what almost every citation of this index makes.

For China the change is not small.
Recorded urban population rises smoothly
from 330,560 thousand in 1995 to 612,933 thousand in 2001,
then reads 294,634 in 2002.

$$
\frac{294{,}634 - 612{,}933}{612{,}933} \approx -0.52
$$

A state with a very large number of cities
between one hundred thousand and three hundred thousand people
loses more than half its recorded urban population
the moment the threshold triples.
The series resumes a smooth rise from the lower level
and does not regain its 2001 value until 2018.

The effect on the index can be attributed exactly,
because the index is a sum of six equally weighted terms
and each contributes its own change divided by six.

$$
\Delta \mathrm{CINC}_{i} = \frac{1}{6} \sum_{c=1}^{6} \Delta s_{c,i}
$$

The decomposition is therefore exact rather than approximate,
and its terms must sum to the published change,
which is the check performed below.

| Component | 2001 share | 2002 share | Contribution to the index |
|-----------|-----------|-----------|---------------------------|
| Military expenditure | 5.41 | 7.83 | +0.404 |
| Military personnel | 11.32 | 11.09 | -0.038 |
| Iron and steel production | 17.74 | 20.16 | +0.403 |
| Primary energy consumption | 12.68 | 13.77 | +0.181 |
| Total population | 20.85 | 20.71 | -0.024 |
| Urban population | 31.26 | 18.56 | **-2.117** |
| **Net** | | | **-1.190** |

The contributions sum to the published change in the index
from 16.543 to 15.354,
which confirms the attribution rather than merely illustrating it.
**The definitional change alone removed 2.117 index points
while every other component together added 0.927.**
Holding the urban share at its 2001 value
and leaving everything else as published
puts the 2002 ratio at 1.14 rather than 0.9987.

$$
\frac{17.471}{15.374} \approx 1.14
$$

**So the single year in which this index does not place China ahead of the United States
is a year in which a definition changed.**
A panel correlation of 0.99 did not prevent that,
and could not have, because it is not a statement about any one pair of states.

**The urban component changes again for the years from 2017**,
and here the codebook names the state most affected.

> This change in operationalization underscores the importance of
> using the NMC data as a means to compare values of capabilities
> between states within years
> but should be used with caution as time series values of
> individual components within individual states.

The preceding sentences identify the United States
as "the most prominent case where this occurs".
Read in the file, the effect is again large.
Recorded United States urban population falls
from 197,817 thousand in 2016 to 109,994 thousand in 2017,
while the Chinese figure rises from 526,464 to 609,219.

$$
\frac{109{,}994 - 197{,}817}{197{,}817} \approx -0.44,
\qquad
\frac{609{,}219 - 526{,}464}{526{,}464} \approx +0.16
$$

**A single definitional change cut the American figure by 44 percent
and raised the Chinese figure by 16 percent, in the same year.**
Substituting the 2016 urban shares into the 2022 index
and leaving the other five components as published
gives a ratio of 1.832 rather than 1.895.

$$
\frac{1.8945}{1.8318} - 1 \approx +0.034
$$

About three and a half percent of the 2022 ratio
is therefore attributable to that revision.
The direction of the gap is unaffected and its size is slightly overstated,
which is the honest summary.

A fourth discontinuity sits in Chinese military expenditure,
recorded as 84.3 billion current United States dollars in 2004
and 29.9 billion in 2005.

$$
\frac{29.9 - 84.3}{84.3} \approx -0.65
$$

Chinese military spending did not fall by nearly two thirds in 2005.
The series recovers to 46.2 billion by 2007
and climbs without further interruption to 218.6 billion in 2022.
No note accounting for this one was located in the codebook,
and the search was not exhaustive,
so it is reported as an observation rather than a diagnosed cause.

### The warning the data producers give, and what it costs this article

The sentence quoted above is not a minor caveat
and it is directed at exactly the use this article makes of the data.
The codebook says the index is a means
"to compare values of capabilities between states within years"
and should be used "with caution as time series values
of individual components within individual states".

**That is a warning from the people who built the instrument
against reading it longitudinally**,
and the base rates in the next section are longitudinal.
Three things should be said about that rather than one.

The warning is addressed to individual components
within individual states,
and this article's comparisons are of a state's share of a world total,
taken in one year and then in another.
That is the use the codebook endorses, performed twice,
which is not the same thing as the use it cautions against.
The distinction is real but it is narrower than a reader might like.

The breaks documented above show the caution is earned.
Where a component is respliced,
a state's share in the later year is not commensurable
with its share in the earlier one,
and the 2017 urban population revision
demonstrates this inside the window the headline figures come from.

**So the honest position is that ratios and orders of magnitude
from this instrument are usable
and precise levels and short-run changes are not.**
That principle is applied throughout what follows.
It is also why the base-rate comparisons use intervals of five and ten years
rather than annual changes,
why the named cases are reported individually
rather than only as a median,
and why no figure in this article is quoted to a precision
that the instrument does not support.
### What the alternative instruments say

The choice of instrument is not a technicality,
because the instruments disagree about the present ordering.

Gross domestic product at market exchange rates
and the same quantity at purchasing power parity
give different answers about whether a transition has occurred at all,
and the gap between them for this pair of states is unusually wide.
Military expenditure, taken alone,
puts the United States far ahead on every published series.
Composite indices built to weight outcomes rather than inputs
tend to narrow the Chinese lead or reverse it.

The general objection to gross indicators
is that they count what a state has
rather than what it can bring to bear after paying for itself.
A state with a very large population
has correspondingly large internal claims on its output,
so counting population as capability double counts.
This is the net-against-gross argument,
and it is the single most important reason
that the CINC result above should not be read as a finding about military power.

## The Base Rate for Postwar Power Shifts

With an instrument in hand, the historical question becomes tractable.
Rather than ask what analysts expect a great-power war to do
to the distribution of power,
it is possible to ask what great-power wars have in fact done.

### How the base rate was computed

The [Correlates of War Inter-State War Data][data_cow_interstate_war_v4],
version 4.0,
whose outcome codes are defined in its
[published codebook][data_cow_interstate_wars_codebook],
records 95 inter-state wars from 1823 to 2003
across 337 participant entries,
each coded with the participant's side and the outcome it obtained.
Joining that to the capability series gives,
for every belligerent in every war,
its share of world capability before the war
and its share some fixed interval after the war ended.

Two design choices carry most of the weight
and both are departures from the obvious approach.

**The denominator holds its membership fixed.**
The international system grew from 46 members in 1860
to 195 in 2022,
and decolonisation alone added roughly a hundred states between 1945 and 1975.
Every incumbent's share of the whole system falls when the system expands,
whatever happens to its capability.
A naive comparison of a belligerent's share before and after a war
therefore charges the United Kingdom for the independence of its colonies
as though that were war damage.
Each comparison here is computed over the set of states
present in both the earlier and the later year,
which removes entry and exit.
Ratios of the index within a year are ratios of capability,
so restricting the denominator is well defined.
Writing $C$ for the set of states present in both years,
the share and the quantity reported throughout are these.

$$
S_{i,t} = \frac{\mathrm{CINC}_{i,t}}{\sum_{j \in C} \mathrm{CINC}_{j,t}},
\qquad
\delta_{i} = \frac{S_{i,\,t_{1}} - S_{i,\,t_{0}}}{S_{i,\,t_{0}}}
$$

Here $t_{0}$ is the year before the war began
and $t_{1}$ is five or ten years after it ended.

**An equal window before the war is measured as well.**
If a belligerent's share was already moving in the same direction
at the same rate before the war began,
the war revealed a shift rather than caused one.
The prewar comparison uses a window of identical length,
so the two quantities are on the same footing.

$$
\tau_{i} = \frac{S_{i,\,t_{0}} - S_{i,\,t_{0}-h}}{S_{i,\,t_{0}-h}},
\qquad
h \in \{5, 10\}
$$

That distinction is the central dispute in power transition theory
and it can be tested rather than assumed.

The interval after the war is reported at five and ten years.
A reading taken immediately at the armistice
catches wartime mobilisation still in place,
which is not a durable change in position.

### What the record shows

The table reports the relative change in a belligerent's share
of world capability from the year before the war
to ten years after it ended,
with membership held fixed.

| Group | Observations | Median change | Mean change | Share that declined |
|-------|--------------|---------------|-------------|---------------------|
| All participants | 306 | +0.071 | +0.197 | 44.8 percent |
| Winners | 146 | +0.118 | +0.298 | 38.4 percent |
| Losers | 103 | -0.021 | +0.092 | 52.4 percent |
| Stalemates | 28 | +0.100 | +0.272 | 32.1 percent |

The winner-against-loser difference is in the expected direction
and it is unlikely to be noise.
A two-sided Mann-Whitney test on the two change distributions
gives a standardised statistic of 3.00.

$$
z = 3.00, \qquad p \approx 0.0027
$$

A rank test is the right tool here rather than a comparison of means,
because the change distribution has heavy tails
and the means above are visibly pulled by them.

The size of the effect is the surprise.
The median winner improved its relative share by about twelve percent
over the following decade,
and the median loser gave up about two percent.
The gap between the two medians is roughly fourteen points of relative change.

$$
0.118 - (-0.021) = 0.139
$$

**Set against the variance, that is a weak effect.**
Thirty-eight percent of winners declined,
and nearly half of all losers improved their position.

$$
\Pr(\delta < 0 \mid \text{winner}) = 0.384,
\qquad
\Pr(\delta > 0 \mid \text{loser}) = 0.476
$$

Those two are frequencies in this sample rather than probabilities,
and they are written this way to make the overlap visible.
Winning a war moved a state's share of world capability
in the expected direction rather more often than not,
and by an amount that a decade of ordinary economic performance
could easily supply or erase.

### In large wars the asymmetry is in the downside

Restricting to wars with at least one hundred thousand recorded battle deaths
changes the picture in a way that matters for this subject,
because a war between the United States and China
would belong to that class and not to the class of colonial expeditions
that dominates the full sample.

| Group | Observations | Median change | Share that declined |
|-------|--------------|---------------|---------------------|
| All participants in large wars | 33 | -0.021 | 51.5 percent |
| Winners of large wars | 17 | +0.126 | 35.3 percent |
| Losers of large wars | 11 | -0.418 | 100 percent |

**Every loser of a large war in the record
held a smaller share of world capability a decade later,
and the median loss was about forty-two percent of its prewar share.**

$$
\Pr(\delta < 0 \mid \text{loser, large war}) = \frac{11}{11} = 1
$$

Winners of large wars did about as well as winners generally,
with a median gain near thirteen percent,
and more than a third of them still declined.

The asymmetry is therefore not between winning and losing symmetrically.
It is between a reliable and severe penalty for losing a large war
and an unreliable, modest reward for winning one.
The two medians differ by more than a factor of three in magnitude.

$$
\frac{|-0.418|}{0.126} \approx 3.3
$$

Eleven observations is a small sample
and the uniformity of the decline should be read with that in mind,
but the uniformity is itself the finding.
No large-war loser escaped.

### Whether the war causes the shift or reveals it

Power transition theory is usually read as holding
that a war ratifies a shift already underway.
If that is right, the prewar trajectory should predict the postwar change.
Across the 267 observations where both can be computed at the ten-year horizon,
the correlation is essentially zero.

$$
r = -0.038
$$

At the five-year horizon it is similar.

$$
r_{10} = -0.038 \;(n = 267),
\qquad
r_{5} = -0.082 \;(n = 286)
$$

The sign is slightly negative rather than positive,
which if anything suggests mild reversion,
but neither value is distinguishable from no relationship at this sample size.
Squaring the larger of the two bounds how little is explained.

$$
r_{5}^{2} \approx 0.0067
$$

Under one percent of the variation in postwar change
is accounted for by the prewar trajectory.

This is a genuinely informative null.
**A belligerent's trajectory before a war
carries no useful information about how its share of world capability
will move in the decade after that war.**
The war is not a formality that confirms a trend.
Whatever the fighting and the settlement do,
they do something the previous trajectory did not anticipate.

The caveat is that a correlation of pre-war trend with post-war change
tests only the linear and contemporaneous version of the claim.
A theory holding that transitions become visible over longer periods,
or that the relevant trend is in a different quantity such as growth rate,
is untouched by this test.

### Four cases that invert the expected sign

Medians conceal the cases a reader already has intuitions about,
so the individual results are given for the wars most often invoked.
All figures are relative change in share of world capability
from the year before the war to ten years after its end,
with membership held fixed.

| War | State | Outcome | Before | After | Change |
|-----|-------|---------|--------|-------|--------|
| Russo-Japanese, 1904 to 1905 | Japan | winner | 0.0317 | 0.0259 | -0.183 |
| Russo-Japanese, 1904 to 1905 | Russia | loser | 0.1106 | 0.1195 | +0.080 |
| Franco-Prussian, 1870 to 1871 | Germany | winner | 0.0798 | 0.1014 | +0.271 |
| Franco-Prussian, 1870 to 1871 | France | loser | 0.1080 | 0.1052 | -0.026 |
| World War I | United Kingdom | winner | 0.1159 | 0.0906 | -0.218 |
| World War I | Germany | loser | 0.1474 | 0.0848 | -0.425 |
| World War II | United States | winner | 0.2409 | 0.3238 | +0.344 |
| World War II | United Kingdom | winner | 0.0922 | 0.0595 | -0.355 |
| World War II | Soviet Union | winner | 0.1639 | 0.2178 | +0.329 |
| World War II | Japan | loser | 0.0605 | 0.0364 | -0.398 |
| Korean, 1950 to 1953 | United States | stalemate | 0.2722 | 0.2376 | -0.127 |
| Korean, 1950 to 1953 | China | stalemate | 0.1037 | 0.1224 | +0.180 |
| Vietnam, phase 2 | United States | loser | 0.2037 | 0.1347 | -0.339 |

**The Russo-Japanese War inverts the sign on both sides.**
Japan won and held eighteen percent less of world capability a decade later.
Russia lost, and despite a revolution in the interval,
held eight percent more.
This is the canonical Asian power transition
and the quantitative record of its aftermath
points the opposite way from the narrative.

The United Kingdom won both world wars and declined after each,
by twenty-two percent and then thirty-six percent.
The Korean War, which the dataset codes a stalemate for both,
cost the United States thirteen percent of its relative share
while China gained eighteen percent.
Two of the strongest results in the table
belong to a state that won nothing.

Three of these entries deserve a note rather than a silent pass.
France appears in the dataset twice for the Second World War,
coded a loser for the 1940 campaign and a winner subsequently,
which is a faithful representation of what happened
and not a data error.
Its share fell on both codings,
by thirty percent and thirty-three percent.
Russia is coded a winner of the First World War
despite exiting it in 1918,
which is a coding convention of the dataset rather than a judgement
and is a reason to treat that one row cautiously.

### What the base rate does and does not license

These are historical frequencies, not predictions,
and three limits on their use should be stated before they are used at all.

The record is overwhelmingly pre-nuclear.
Of the large wars in the sample,
only the Korean War was fought by a nuclear-armed state,
and none was fought between two of them.
Any mechanism by which nuclear weapons truncate a war,
limit its aims or change its settlement
is absent from the base rate by construction.

The index is an industrial-age instrument,
as the previous section established,
so the base rate measures what wars did
to belligerents' shares of steel, energy, population and troops.
A war whose main effect ran through semiconductors,
financial infrastructure or software
would be partly invisible to it.

And a before-and-after comparison is not a causal estimate.
States that fight wars are not a random sample of states.
The prewar trend test above addresses one version of that worry
and leaves others untouched.

## Who Gains From a War They Do Not Fight

The scenario literature asks mostly who wins.
That is a question about the balance between the two belligerents.
The distribution of world power can move substantially
without the balance between them moving at all,
if both lose ground to everyone else.
This is the mechanism behind the standing realist advice
to let other great powers do the fighting,
and it is testable.

### The belligerents did not systematically lose ground

For each war, summing the belligerents' shares before and after
and holding the denominator's membership fixed
gives the combined belligerent share.
Writing $B$ for the set of belligerents,
the quantity is their combined share
and the bystander share is its complement.

$$
B_{t} = \sum_{i \in B} S_{i,t},
\qquad
1 - B_{t} = \sum_{i \notin B} S_{i,t}
$$

Because shares over a fixed membership sum to one,
a fall in the belligerents' combined share
is exactly a rise in the combined share of the states that stayed out.

At the ten-year horizon, across the 76 wars where every belligerent
survives into the later year as a system member,
the belligerents' combined share rose by a median of 2.5 percent
and fell in 36 of 76 cases.

$$
\frac{36}{76} \approx 0.474,
\qquad
\operatorname{median} \frac{\Delta B}{B} = +0.025
$$

Among the ten largest of those wars
the median change was -1.5 percent
and the belligerents lost ground in five of ten,
which is as close to a coin flip as a sample of ten can report.

$$
\frac{5}{10} = 0.5
$$

**On the face of it the bystander-gain hypothesis is not supported.**
The combined position of the states doing the fighting
was about as likely to improve as to deteriorate.

### Why that result is biased, and in which direction

The survival requirement in the previous paragraph is doing damage
and the direction is knowable.
A war is excluded if any belligerent is absent from the system
in either the earlier or the later year.
That condition removes the cases in which a belligerent was destroyed,
which is the largest possible loss of capability share.
The excluded large wars are identifiable.

| War | Belligerent absent from one endpoint |
|-----|--------------------------------------|
| Franco-Prussian | Bavaria, Baden, Wuerttemburg |
| World War I | Austria-Hungary |
| Third Sino-Japanese | Japan |
| World War II | Germany, Ethiopia |
| Vietnam, phase 2 | South Vietnam |

**The two world wars are excluded from that base rate
by the dissolution of a belligerent,
so the base rate is computed on a sample
from which the most consequential cases have been removed,
and removed for a reason correlated with the outcome.**
The reported figure should therefore be read
as an upper bound on belligerent fortunes.

### In the world wars there was no bystander large enough

Computing the two world wars separately,
with the dissolved belligerents mapped onto successor states
so that their capability is neither lost nor double counted,
gives a result that explains the whole puzzle.
Austria-Hungary is mapped onto Austria, Hungary and Czechoslovakia.
Germany after 1945 is mapped onto the two German states.
Ethiopia is excluded for absence in 1938 and is small enough not to matter.

| War | Belligerent share before | Ten years after | Change |
|-----|--------------------------|-----------------|--------|
| World War I, measured 1913 against 1928 | 0.8229 | 0.7761 | -0.057 |
| World War II, measured 1938 against 1955 | 0.9808 | 0.9610 | -0.020 |

The belligerents' combined share barely moved.

$$
\frac{0.7761 - 0.8229}{0.8229} \approx -0.057,
\qquad
\frac{0.9610 - 0.9808}{0.9808} \approx -0.020
$$

The reason is in the first column.
**The belligerents of 1914 held 82 percent of measured world capability
and those of 1939 held 98 percent.
There was no bystander large enough to gain anything.**
A redistribution away from the fighting powers
was arithmetically almost impossible,
because the fighting powers were very nearly the whole system.
The pool available to receive it was this.

$$
1 - 0.8229 = 0.1771,
\qquad
1 - 0.9808 = 0.0192
$$

**In 1939 the states not fighting held under two percent
of measured world capability between them.**
A transfer of standing to non-participants
had almost nowhere to go.

This reframes the earlier null result.
The bystander-gain hypothesis was not tested fairly by the historical record,
because the historical record of great-power war
does not contain a case with a large pool of non-participants.

### The present case is structurally different

That is precisely what distinguishes the contingency this series is about.
Using 2022 shares, the most recent available,
the two prospective belligerents hold the following.

$$
0.1227 + 0.2325 = 0.3552
$$

Adding the United States treaty allies and partners in the region
most often assumed into the fight,
namely Japan, South Korea, Australia and Taiwan,
raises the figure to about 41 percent.
Adding the three largest European members of the North Atlantic Treaty Organization,
or NATO,
raises it to about 45 percent.

| Belligerent set | Share of world capability | Bystander pool |
|-----------------|---------------------------|----------------|
| The two principals alone | 35.5 percent | 64.5 percent |
| With Japan, South Korea, Australia, Taiwan | 41.1 percent | 58.9 percent |
| Adding the United Kingdom, France, Germany | 45.0 percent | 55.0 percent |

**Even on the most expansive plausible coalition,
a majority of measured world capability stays out of this war.**
That has not been true of a great-power war in the period the data cover.
Set against 1939 the difference is not incremental.

$$
\frac{0.6448}{0.0192} \approx 34
$$

The bystander pool is about thirty-four times the size it was
in the last general war among great powers.
Expressed against the two world wars,
the prospective belligerent share is a little over a third
of the 1939 figure and a little over two fifths of the 1914 figure.

$$
\frac{0.3552}{0.8229} \approx 0.43,
\qquad
\frac{0.3552}{0.9808} \approx 0.36
$$

The single largest non-participant is the one the regional framing tends to omit.
India held 9.9 percent of world capability on this index in 2022,
which is about four fifths of the American share.

$$
\frac{0.0987}{0.1227} \approx 0.80
$$

A war that cost both principals a quarter of their relative standing
would, mechanically, move India past the United States on this index
without India doing anything at all.
That is an arithmetic observation about shares and not a forecast,
and it illustrates why the question in this article's title
cannot be answered by examining the two belligerents alone.

### The control case nobody fought

One further comparison belongs here
because it bounds how much of the variance in power shifts
great-power war explains at all.

Between 1990 and 2022 Russia's share of world capability
fell from 0.1342 to 0.0391 among the constant membership set,
having bottomed at 0.0373 in 2016.

$$
\frac{0.0391 - 0.1342}{0.1342} \approx -0.71
$$

**Russia lost 71 percent of its relative standing without fighting a great-power war,
which is substantially more than the median large-war loser lost,
and more than any individual belligerent in the named-case table above.**
The largest redistribution of measured capability in the modern portion of the series
was produced by the dissolution of a state from within.

Two readings of that are available and the article does not choose between them.
Either great-power war is a comparatively minor cause
of changes in the distribution of power,
which would make the entire scenario literature a study of a second-order mechanism.
Or the index is a poor instrument for sudden political discontinuities,
and it recorded the Soviet dissolution as a capability loss
when what happened was a change in which flag the capability sat under.
The second reading has obvious force,
since much of the lost share reappears as Ukraine, Kazakhstan and the other successors.
The first is not thereby disposed of,
because the same objection applies to every war in the sample
in which borders moved.

## Applying the Base Rate to This Case

The base rate and the present standing can be combined,
and the result is worth stating plainly
because it is not the result the scenario literature implies.

### The arithmetic

The exercise is mechanical.
Take the 2022 shares, apply the median relative change
for winners and for losers of large wars,
and hold India fixed as a state that stays out.
Every input has appeared above.

$$
\mathrm{CINC}_{\mathrm{CHN}} = 0.2325, \quad
\mathrm{CINC}_{\mathrm{USA}} = 0.1227, \quad
\mathrm{CINC}_{\mathrm{IND}} = 0.0987
$$

$$
\delta_{\text{win}} = +0.126, \qquad \delta_{\text{lose}} = -0.418
$$

Each outcome maps a present share to a post-war one by a single multiplication,
and the bystander pool follows as the complement.

$$
S' = S\,(1 + \delta),
\qquad
P' = 1 - S'_{\mathrm{CHN}} - S'_{\mathrm{USA}}
$$

The four combinations give the following.

| Outcome | China | United States | India | Ratio | Bystander pool |
|---------|-------|---------------|-------|-------|----------------|
| United States wins, China loses | 0.1353 | 0.1382 | 0.0987 | 0.979 | 72.7 percent |
| China wins, United States loses | 0.2618 | 0.0714 | 0.0987 | 3.666 | 66.7 percent |
| Both at the loser median | 0.1353 | 0.0714 | 0.0987 | 1.895 | 79.3 percent |
| Both at the winner median | 0.2618 | 0.1382 | 0.0987 | 1.895 | 60.0 percent |

### Three results that follow

**An American victory at the historical median
does not restore American primacy on this index. It produces a tie.**
In the row where the United States wins and China loses,
both at the median rate for large wars,
the ratio moves from 1.895 against the United States to 0.979 in its favour.

$$
\frac{0.1353}{0.1382} \approx 0.98
$$

That is the most favourable of the four rows,
and the gain it represents is the difference
between being outweighed nearly two to one and being level.

**A defeated China would still hold a larger share of world capability
than the United States holds today.**

$$
\frac{0.1353}{0.1227} \approx 1.10
$$

This follows from the size of the present gap rather than from anything subtle.
China can absorb the median large-war defeat,
which is the loss of about two fifths of its relative standing,
and remain above the current American level.

**If the United States loses, India passes it without fighting.**

$$
\frac{0.0987}{0.0714} \approx 1.38
$$

In that row the ordering becomes China, then India, then the United States,
and India has done nothing.

The fourth observation is the one that connects back to the bystander section.
In the two symmetric rows the ratio between the belligerents
is unchanged at 1.895,
because multiplying both by the same factor cannot alter their ratio.
Yet the bystander pool moves from 60.0 percent to 79.3 percent
across those same two rows.
**The balance of power between the belligerents
and the distribution of power in the world
are separate quantities, and a war can move one without moving the other.**
That is the argument of this article compressed into two table rows.

### What this exercise is not

It is an application of a median to a single case,
and the dispersion behind that median is wide.
More than a third of large-war winners declined,
so the first row is not a forecast
but the central tendency of a scattered sample.
The eleven large-war losers are uniform in direction
and far from uniform in magnitude.

Holding India fixed is an assumption and a conservative one.
A state whose exports and borders are both affected by a Pacific war
would not be unaffected,
and the direction of the effect on India is not obvious.

And the index remains an industrial-age instrument.
Every number in the table is a share of steel, energy, population and troops.
A reader who holds that those quantities no longer constitute power
should read the table as a statement about the instrument
rather than about the world,
which is a defensible reading and is the reason
the following sections turn to the literature
rather than extending the arithmetic.

## What the Scenario Literature Projects

Having computed a base rate, the article turns to what has been written.
The scenario literature is thinner than the volume of commentary suggests,
and the thinness is itself documented by the people who produced it.

### The one study built for this question

[Priebe and others 2023][research_priebe_2023_alternative_futures_v1]
is the only located study whose object is the postwar world
rather than the war.
It was commissioned by the Directorate of Strategy, Posture, and Assessments
at Headquarters Air Force,
and it carries a caveat on its own currency,
that it "was finalized in January 2021,
before the February 2022 Russian invasion of Ukraine".

Its central result is negative and it is stated as such.

> One key finding from our hypothetical scenarios was a negative one.
> We could not envision a plausible scenario,
> having excluded strategic nuclear exchange,
> in which the United States would so thoroughly defeat China or Russia
> that either would lose its great power status.

The report's judgement on the scale of postwar change follows directly.

> The aftermath of a great power war appears more likely to bring
> an evolution than a revolution in global or regional strategic dynamics.

**And then it names its historical analogues,
which is where this article's computation becomes useful.**
The report continues that
"overall the consequences from our scenarios
are historically more similar to middle-tier conflicts,
such as the Franco-Prussian or Korean wars".

Those two wars are in the base-rate table above,
and what happened after them can be stated rather than estimated.
After the Franco-Prussian War the winner's share of world capability
rose by 27 percent over the following decade
while the loser's fell by 3 percent.

$$
\delta_{\mathrm{GMY}} = +0.271,
\qquad
\delta_{\mathrm{FRN}} = -0.026
$$

After the Korean War, which the war data code a stalemate for both principals,
the American share fell by 13 percent and the Chinese share rose by 18 percent.

$$
\delta_{\mathrm{USA}} = -0.127,
\qquad
\delta_{\mathrm{CHN}} = +0.180
$$

The gap between the two is the part worth holding on to.

$$
0.180 - (-0.127) = 0.307
$$

**An evolution rather than a revolution is still a quarter of a state's
relative standing changing hands within ten years.**
The RAND characterisation and the measured outcomes are consistent,
and together they are more informative than either alone.
Korea is the more arresting of the two,
because it is the case in which the side that did not win gained,
and because it is the only United States-China war in the historical record.

Three further conclusions from the same report
bear directly on the arguments above.

> Wartime victory might not produce a favorable postwar setting.
> For example, victors will be weakened relative to noncombatant states
> and could face stronger balancing coalitions.

> U.S. allies and partners might face new incentives to proliferate
> after a great power war that degrades U.S. power.

The first is the bystander hypothesis, asserted.
This article tested it and found the historical record
does not support it in the aggregate,
for the reason that the historical record contains no case
with a bystander pool large enough.
**RAND and this article agree about the mechanism
and disagree about whether the past demonstrates it.
Both can be right, because the structural condition is new.**

The project's own researchers were explicit
about why the study existed at all.
Interviewed on publication,
[Priebe and Frederick][research_priebe_frederick_2023_conversation]
said that "there's very little attention or planning devoted to the aftermath",
that "the winner of the war might not end up looking like the winner
in the peace that follows",
and, on the third-party question,
that the great power benefiting most consistently across their scenarios
was in each case the one that did not fight.
Frederick adds the specific form.
A war between the United States and Russia most directly benefits China,
and a war between the United States and China most directly benefits Russia,
in both cases irrespective of which belligerent wins.
The report goes on to recommend that someone build the missing instrument,
under a heading reading "Wargame Set After a Great Power War".
**A recommendation to construct such a game
is evidence that it did not exist when the recommendation was written.**

### How often prewar forecasts of the balance of power have been right

The companion [historical volume][research_evans_2023_alternative_futures_v2]
examines "ten cases of great power conflict since 1853"
and grades each against five forecasting dimensions.
Its conclusion is blunt.

> In the years prior to each of the conflicts surveyed here,
> politicians and military planners held flawed assumptions
> and made inaccurate predictions
> about critical aspects of the war that would follow.

The grading is published as a colour-coded table rather than as counts,
so the column of interest was read off the rendered page
rather than from the text layer, which carries no colour.
The legend is explicit.

> Dark red indicates each of the great power combatants' prewar assumptions
> about this factor were incorrect;
> light green indicates that all of the great power combatants
> accurately forecasted major features of the war;
> yellow indicates mixed success.

On the column headed "Consequences for Regional and Global Balance of Power",
the ten wars grade as one green, six yellow and three dark red.

$$
\frac{1}{10} \;\text{fully accurate}, \qquad
\frac{3}{10} \;\text{wholly inaccurate}
$$

**In one case out of ten did every great-power combatant
correctly forecast what the war would do to the balance of power.**
The single success is the Russo-Turkish War of 1877 to 1878.
The three failures are the First World War
and the two theatres of the Second.

That pattern is worth stating separately from the ratio,
because it is not random.
**The three cases in which every combatant was wrong
about the consequences for the balance of power
are the three largest wars in the sample,
and the one case in which everyone was right is among the smallest.**
Forecasting accuracy on this dimension falls as the stakes rise.
A reader may draw the obvious inference about a prospective war
larger than any in that table.

### The wargames stop before the question

The most cited open-source wargame of this contingency,
[Cancian, Cancian and Heginbotham's][research_cancian_2023_first_battle]
twenty-four-iteration study,
disposes of the postwar distribution of power in one clause.
Its executive summary records that
"the high losses damaged the U.S. global position for many years",
and elsewhere that "victory is not everything"
and that the United States "might win a pyrrhic victory,
suffering more in the long run than the 'defeated' Chinese".
It also lists the mechanism this article has been pursuing.

> Loss of Global Position.
> The world would not be standing still during and after a U.S.-China conflict.
> Other countries, for example, Russia, North Korea, or Iran,
> might take advantage of U.S. distraction to pursue their agendas.
> After the war, a weakened U.S. military
> might not be able to sustain the balance of power in Europe or the Middle East.

That is the bystander hypothesis again,
in a different form and still as an assertion.
The report is explicit that developing it is out of scope,
stating that a policy assessment
"requires a political and foreign policy assessment of benefits, costs, and values
that goes beyond the scope of the current effort".
**That is a legitimate scoping decision and not a criticism.
It is recorded here because the scope of the field's flagship game
is a fact about the field.**

### The official foresight product routes around the war entirely

The [National Intelligence Council's Global Trends 2040][government_nic_2021_global_trends]
is the United States government's flagship twenty-year foresight publication.
Its structural judgement is close to the one this article reaches by measurement.

> No single state is likely to be positioned to dominate
> across all regions or domains,
> opening the door for a broader range of actors to advance their interests.

It then models five alternative worlds for 2040.
**None of the five reaches its distribution of power through a great-power war.**
The scenario that comes closest, Competitive Coexistence,
states that "the risk of major war is low".
The most fragmented, Separate Silos,
has "small conflicts" at the edges of blocs.
Tragedy and Mobilization has the major militaries avoiding "direct armed conflict"
while "nuclear weapons proliferate".

So the official product that models the distribution of power
does not model the war,
and the wargames that model the war do not model the distribution of power.
That is the gap this article sits in,
and neither body of work is at fault for it,
since each is doing the thing it was built to do.

### What the expert surveys expect, and how fast it is moving

The [Atlantic Council's annual expert survey][research_atlantic_council_2026_welcome_2036]
puts numbers on professional expectations.
In the 2026 edition, 447 respondents from 72 countries
were asked about the world of 2036.
Seven percent expect the United States to be the dominant global power
and four percent expect China to be,
with around nine in ten expecting a bipolar or multipolar distribution.

$$
0.07 + 0.04 = 0.11
$$

**Eleven percent of a panel of specialists
expect either state to be dominant a decade out.**
Fifty-eight percent expect China to be the top economic power
against 33 percent for the United States,
while nearly three quarters still expect American military primacy.

$$
\frac{58}{33} \approx 1.8
$$

The movement across editions is steeper than the levels.
The [2025 edition][research_atlantic_council_2025_welcome_2035]
records the year-on-year change explicitly,
reporting that expectations of American dominance a decade out fell
"from 81 percent to 71 percent for military power,
63 percent to 58 percent for technological innovation,
52 percent to 49 percent for economic power,
and 32 percent to 24 percent for diplomatic power".
The four movements in one year were these.

$$
-10, \quad -5, \quad -3, \quad -8 \;\text{percentage points}
$$

**A panel of several hundred specialists moved ten points
on the military question in a single year, without a war occurring.**
Set against the base rate computed above,
where the median large-war winner gained about thirteen percent
of its relative standing over a decade,
that is a comparable magnitude of revision
produced by nothing more than a year of observation.
The comparison is between a measured quantity and an opinion
and should not be pressed hard,
but it does suggest that expectations about the balance of power
are not stable enough to serve as the baseline
against which a war's effect could be judged.

### The alliance system, where the mechanism is reputational

[Nemeth 2026][journal_nemeth_2026_suez_moment]
supplies the most developed account of a transmission channel
that none of the capability data can see.
His argument is that a visible demonstration of American shortfall,
which he deliberately sets below the threshold of catastrophic defeat,
would propagate through the alliance system by perception alone.

> A Suez moment for the US need not involve a catastrophic defeat
> or even the outbreak of a full-scale conventional war.
> It could arise from a limited skirmish in, for example, the South China Sea,
> or from a series of inconclusive engagements
> that cumulatively expose a new strategic reality.

> And unlike the original Suez crisis,
> where the United States could fill the vacuum left by a declining Britain,
> no other benign hegemon is capable of assuming a similar role today.

He gives two branches, a hollowing of the alliances into "nominal shells"
and an adaptation in which the United States becomes "first among equals",
and he judges the second "arguably more probable".

**The Suez analogy is well chosen and it cuts both ways.**
Suez is the canonical case of a power losing standing
through a short conflict it did not lose militarily,
and it is canonical precisely because
the loss is invisible in the capability data.
British capability share declined at between three and five percent a year
through the whole of the 1950s and 1960s,
and the 1956 decline is smaller than that of 1955, 1958 or 1959.
British military spending rose in 1956 and British steel output rose in 1956 and 1957.
So if Suez is the right analogy,
then the quantity this article has been measuring is the wrong quantity,
and the article says so rather than defending its instrument.

## The Theory Says the War Is Not the Cause

The measurement sections and the base rate both point in one direction,
and it turns out to be the direction the theoretical literature already pointed.
This is the part of the subject where the scholarship is clearest
and the commentary least reflects it.

### Hegemonic war ratifies a shift it did not produce

[Gilpin 1988][journal_gilpin_1988_hegemonic_war],
restating the argument of [his 1981 book][book_gilpin_1981_war_and_change],
describes the resolution of a hegemonic war as
"the establishment of a new international system
that reflects the emergent distribution of power in the system".

The operative word is emergent.
On this account the distribution has already changed before the war,
by differential growth,
and the war converts an unrecognised distribution into an acknowledged one.
Gilpin also supplies the caution
that most constrains confident forecasting,
noting that the consequences of the Peloponnesian War
"were not anticipated by the great powers of the day",
nor were those of the First World War anticipated by European statesmen,
and that "in neither case did the protagonists fight the war
that they had wanted or expected".

### The strongest form of the claim is that the war does not change the distribution at all

[Organski and Kugler's phoenix factor][journal_organski_kugler_1977_phoenix]
is the empirical statement.
Their published abstract reports a sample of 32 cases
analysed as time series.

> The findings register unexpected but systematic patterns after major conflicts.
> While winners and neutrals are affected marginally by the conflict,
> losers' powers are at first eroded.
> Over the long run, fifteen to twenty years,
> the effects of the loss dissipate.
> Losers accelerate their recovery and soon resume antebellum status.

Two things about that finding deserve emphasis.
The first is that it was already used in the
[previous article in this series][related_post_rebuilding],
where it bore on reconstruction rather than on relative standing.
The second is that it points the opposite way
from the large-war result computed here,
where every one of eleven losers held a smaller share of world capability
ten years after the war.
**The two results are not necessarily in conflict,
because theirs runs to fifteen or twenty years and this one stops at ten,
and because the samples and the measures differ.**
Where they can be compared, they disagree,
and this article does not resolve it.
The honest statement is that the recovery horizon
is longer than the horizon at which the effect is largest,
and an article interested in the decade after a war
should use the decade, while noting what the longer window shows.

### The direction of causation is the same in every formal treatment

[Powell 2006][journal_powell_2006_commitment_problem]
derives war from a commitment problem
in which "large, rapid shifts in the distribution of power can lead to war".
[Levy 1987][journal_levy_1987_declining_power]
treats the preventive motivation as
"an intervening variable between changing power differentials
and the outbreak of war".
[Fearon 1995][journal_fearon_1995_rationalist]
locates war in private information about capabilities and the incentive to misrepresent it,
which makes fighting a procedure for revealing a distribution
that already obtains.

In each the shift is upstream and the war is downstream.
**No theory in this family treats the war as the cause of the redistribution.**
That is a strong and underappreciated consensus,
and it means the question in this article's title
is one the dominant theory answers in the negative before any evidence is gathered.

The consensus is not unanimous.
[Chadefaux 2011][journal_chadefaux_2011_bargaining]
shows that under complete information
"shifts in power never lead to war
when countries can negotiate over the determinants of their power",
so a shift alone is never sufficient.
And [DiCicco and Levy 1999][journal_dicicco_levy_1999_power_shifts],
reviewing the research programme from inside it,
find that while some developments are progressive,
"other areas of the research program exhibit signs of degeneration",
naming the timing and initiation of wars
and the causal mechanisms driving them.

### Independent corroboration from economics

[Davis and Weinstein 2002][journal_davis_weinstein_2002_bones_bombs],
examining the Allied bombing of Japanese cities as a shock to relative city sizes,
conclude that "long-run city size is robust even to large temporary shocks".
That paper also appeared in the previous article,
where it bounded the persistence of physical destruction.
Here it bears on something broader.
If the most concentrated destruction ever visited on an industrial society
did not durably change the relative size of its cities,
the prior that a war durably changes the relative size of its economies
should be weak.

### Where the theory turns from capability to order

The literature's response to all this
has been to change the object of study.
[Ikenberry's After Victory][book_ikenberry_2019_after_victory]
asks not what the victor's share becomes
but what the victor does with a transient advantage,
and sets out three choices,
to dominate the defeated, to withdraw,
or to use a commanding position
to obtain acquiescence in a mutually acceptable order.
[Cooley and Nexon][book_cooley_nexon_2020_exit_from_hegemony]
reverse the question and ask how such an order comes apart,
locating the mechanism in great-power contestation,
the loss of a patronage monopoly
and transnational counter-order movements,
and noting that analysts
"have only recently begun to appreciate the significance of these three processes"
because attention has gone to power transitions and great-power wars.

**That move is the right one and it is also an admission.**
The distribution of capabilities is not where the action is,
on the field's own account,
which is a reason to hold the arithmetic in this article lightly
and a reason the arithmetic is worth doing,
since the alternative is an order literature with no quantitative anchor at all.

## The Objection From the Economic Modelling

The bystander argument above was built from capability shares.
There is a second literature, built from trade and output,
and it does not agree.
Stating the disagreement properly is more useful than resolving it,
because the two literatures measure different things
and the difference is the point.

### Non-belligerents are not insulated

[Nikkei's estimate][commentary_nikkei_2022_taiwan_emergency],
constructed from the Organisation for Economic Co-operation and Development
Trade in Value Added database,
models a halt to trade between China and the major economies
and puts the total loss at 2.61 trillion United States dollars,
"an amount equal to 3% of the world's gross domestic product".
Its distribution is the part that matters here.
China loses 7.6 percent of nominal gross domestic product,
Japan 3.7 percent, Europe 2.1 percent and the United States 1.3 percent.

$$
\frac{3.7}{1.3} \approx 2.8
$$

**On that estimate a non-belligerent treaty ally
bears nearly three times the proportional output loss of the United States.**
Japan would almost certainly be a belligerent in the scenarios this series covers,
which weakens the example without removing the point,
since the mechanism is trade exposure rather than participation.

[Rhodium's analysis][research_rhodium_2022_taiwan_disruptions]
reaches the same structural conclusion from a different direction,
noting that
"even countries that, on the surface, appear only remotely linked to Taiwan
would also face risks",
because a collapse in Chinese import demand
reaches commodity exporters with no Taiwan exposure at all.
Its headline figure is "well over two trillion dollars in a blockade scenario",
and it explicitly disclaims the thing this article would most want,
stating that the authors "do not purport to estimate GDP losses
or other measures of foregone economic welfare".

### The belligerents are not expected to decline symmetrically either

[Gompert, Cevallos and Garafola][research_gompert_2016_war_with_china]
estimate for a war of one year
"on the order of a 25 to 35 percent reduction in Chinese gross domestic product,
compared with a reduction in U.S. GDP on the order of 5 to 10 percent".

$$
\frac{30}{7.5} = 4
$$

Taking the midpoints, China loses about four times as much as the United States.
**If that asymmetry holds, the belligerents do not decline together,
and the symmetric rows in this article's scenario table
are the least likely of the four.**
The reason given is not military.
It is that the Chinese economy is more trade-dependent
and more exposed to maritime interdiction.

### What the two literatures are actually measuring

The disagreement is less sharp than it looks, and the reconciliation is instructive.

A share of world capability can rise while output falls,
provided output falls faster elsewhere.
The capability index counts steel, energy, population and troops,
quantities that a blockade does not destroy
even when it stops them being sold.
The output estimates count value added,
which a blockade destroys immediately
and which recovers when trade resumes.
So an economy can take a very large output loss
and a small capability loss in the same war,
and the ordering of states by the two measures can differ.

**The precise statement is this.
The capability data say the belligerents' relative standing
is unlikely to move as much as the scenario literature implies.
The trade data say the absolute cost falls on everybody,
and disproportionately on the trade-exposed,
whether or not they fight.**
Neither claim refutes the other.
Together they describe a war that makes
a large number of states poorer
and a small number of states relatively stronger,
and the states made relatively stronger
are not necessarily the ones made less poor.

[Tarapore 2024][research_tarapore_2024_deterring_attack]
is the one located study that takes the non-belligerent category as its subject,
and it takes the opposite side of the question from this article's arithmetic.
He argues that India has
"an abiding interest in a stable status quo,
both in the Indo-Pacific region generally,
where great-power conflict would derail its national growth",
and that India's gains come from deterrence activity
undertaken to prevent the war rather than from the war itself.
**That is a direct challenge to the India result computed above
and it should be read as one.**
The arithmetic says India's share rises if the belligerents' shares fall.
Tarapore says India's growth, which is the thing generating its share, would be hit.
Both can be true if the belligerents are hit harder,
and neither this article nor the source establishes that they would be.

## The Financial Order, Where the Erosion Is Real and Not Where It Is Sought

Capability indices cannot see the mechanism that most commentary invokes.
If a war broke the dollar's role,
the distribution of power would change in a way no steel tonnage records.
That claim is testable against published series,
and the series were pulled directly for this article
rather than taken from secondary accounts.

### The dollar's reserve share is eroding on a long, steady trend

The [International Monetary Fund's Currency Composition
of Official Foreign Exchange Reserves][data_imf_cofer],
retrieved from the Fund's own interface with a payload stamped 30 September 2026,
gives the quarterly series from 1999.
The dollar share stood at 75.03 percent in the first quarter of 1999
and 56.70 percent in the second quarter of 2026,
with the series minimum of 56.52 percent in the fourth quarter of 2025.
The euro stood at 20.60 percent.

$$
75.03 \longrightarrow 56.70 \;\text{percent over 27 years}
$$

**The erosion is real, it is large, and it is slow.**

$$
75.03 - 56.70 = 18.33 \;\text{points},
\qquad
\frac{-18.33}{27.25} \approx -0.67 \;\text{points per year}
$$

Eighteen points of share is a substantial movement,
and spread across twenty-seven years it is about two thirds of a point annually.

A caveat belongs with any figure from this series.
From the third quarter of 2025 the Fund
[changed the methodology][research_kwende_nephew_2025_cofer],
imputing the formerly unallocated portion
so that shares now cover all global reserves rather than the allocated subset.
The series is reconstructed consistently back to 1999,
so comparisons within it hold,
but the familiar phrase about the dollar's share of *allocated* reserves
no longer describes a published series,
and any secondary source predating 2025 is on a discontinued basis.

### The 2022 reserve freeze did not accelerate it

This is the part that is usually asserted and rarely measured.
Splitting the series at the first quarter of 2022,
when the Russian central bank's reserves were immobilised,
gives the drift before and after.

$$
\frac{59.42 - 75.03}{23} \approx -0.68 \;\text{points per year},
\qquad
\frac{56.70 - 59.42}{4.25} \approx -0.64 \;\text{points per year}
$$

**The dollar's reserve share has declined slightly more slowly
since the freeze than it did in the twenty-three years before it.**
Whatever the freezing of a great power's reserves did,
it did not visibly accelerate reserve diversification away from the dollar.

The second half of the finding is sharper.
The renminbi's share of world reserves
peaked at 2.85 percent in the fourth quarter of 2021,
one quarter *before* the freeze,
and fell thereafter to a low of 1.95 percent in the third quarter of 2025,
standing at 2.11 percent in the second quarter of 2026.

$$
\frac{2.11 - 2.85}{2.85} \approx -0.26
$$

**Reserve managers have been diversifying out of the dollar for a quarter century
and they have not been diversifying into the renminbi.**
A quarter of the renminbi's peak share has gone since the event
that was supposed to make it attractive.
The Federal Reserve reaches a compatible conclusion by a different route,
[finding][research_weiss_2025_dedollarization]
that official gold accumulation
"is generally not associated with de-dollarization
of international reserves at the country level,
except in a few prominent cases".

The scholarly literature splits on the mechanism rather than the measurement.
[Dooley, Folkerts-Landau and Garber][research_dooley_2022_sanctions_reinforce]
argue sanctions strengthen the dollar,
because reserves serve a collateral function
that a demonstrated willingness to sanction makes more valuable.
[Bianchi and Sosa-Padilla][journal_bianchi_sosa_padilla_2025_sanctions_dollar]
model the opposite, with anticipated sanctions reducing the dollar convenience yield.
[Arslanalp, Eichengreen and Simpson-Bell][journal_arslanalp_2022_stealth_erosion],
writing in the month of the freeze about the two decades before it,
described a shift "a quarter into the Chinese renminbi,
and three quarters into the currencies of smaller countries".
**The data since have reversed the first of those two limbs**,
which is a case of a well-made empirical finding
being overtaken by the period that followed it
rather than of a finding being wrong.

### The function that is eroding is not the function that confers leverage

The reserve share and the transactional share are moving in opposite directions.
The [Bank for International Settlements triennial survey][data_bis_2025_triennial]
reports the dollar on one side of 89.2 percent of foreign exchange trades in April 2025,
up from 88.4 percent in 2022.

$$
87 \to 88 \to 88 \to 88 \to 89
\quad \text{across 2013, 2016, 2019, 2022, 2025}
$$

Shares sum to two hundred rather than one hundred on this measure,
because two currencies stand on each side of a trade.

**Store-of-value share is falling and medium-of-exchange centrality is rising.**
This matters for the question in this article's title
because the coercive instruments that make financial power a strategic asset,
the ones [Farrell and Newman][journal_farrell_newman_2019_weaponized]
describe as working through chokepoints in networks,
run through payment and settlement rather than through reserve holdings.
A survey that treats a declining reserve share
as evidence of declining financial power
is watching the wrong variable.

### Reserve-currency dominance has been lost and regained before

The inertia argument holds that network effects make the incumbent currency
nearly impossible to dislodge, which would mean a war could not do it.
[Chiţu, Eichengreen and Mehl][journal_chitu_2014_bond_markets]
find that the dollar overtook sterling in the bond markets as early as 1929,
much sooner than the usual account allows,
and record something the inertia literature rarely quotes.

> Eichengreen and Flandreau's data indicate that sterling re-took the lead
> from the dollar for a brief period after 1931.

**Primacy in this domain has been lost and regained once already.**
That cuts against both the claim that a shock could not displace the dollar
and the claim that displacement would be permanent.
[Gopinath and Stein][journal_gopinath_stein_2021_dominant_currency]
supply the theoretical reason the position is sticky,
namely that a currency's invoicing role and its safe-asset role reinforce one another,
which also implies the two could unwind together.

### The fiscal constraint has moved more than the military balance

The capacity to fight a long war is a fiscal question,
and here the baseline has changed in a way the older scenario literature predates.
Projections published by the Congressional Budget Office
and distributed through its [open data repository][data_cbo_2026_projections]
put net interest at 3.195 percent of gross domestic product in fiscal year 2025,
already above defence discretionary spending at 2.940 percent,
and at 4.591 percent by fiscal year 2036.

For comparison, the Korean War cost about 4.2 percent of gross domestic product
at its 1952 peak, and the Second World War about 35.8 percent at its 1945 peak.

$$
4.591 > 4.2
$$

**On current-law projections, debt service alone passes
the peak cost of the Korean War within a decade.**
The projected extended baseline has net interest exceeding
all discretionary spending including defence from about 2050.
None of this is a forecast, since the extended baseline embeds current law,
and none of it is a claim that a war could not be financed.
It is a claim that the fiscal headroom assumed
by analyses concluding that a long war favours the United States
is smaller than when those analyses were written,
and that no located source tests that conclusion
against current debt-service projections.

The mutual-hostage premise has weakened on the other side too.
[Treasury's holdings table][data_treasury_tic_2026] records
mainland China holding 618.0 billion dollars of Treasury securities in July 2026,
third behind Japan and the United Kingdom,
against 1,033.8 billion in January 2022.

$$
\frac{618.0 - 1{,}033.8}{1{,}033.8} \approx -0.40
$$

That is a fall of about two fifths in nominal terms
while the foreign total rose.
The table's own notes caution that custody-based data
"may not provide a precise accounting of individual country ownership",
so the figure is a lower bound on a custody basis
rather than a measure of ownership,
and Belgium and the Cayman Islands both appear
at levels no domestic demand explains.

### Decoupling is asymmetric, and against China

The fragmentation literature bears on the balance of power directly,
because what matters is relative loss.
[Góes and Bekkers][research_goes_bekkers_2022_geopolitical_conflicts],
modelling a decoupling into two blocs with diffusion of ideas,
report the asymmetry explicitly.

> While welfare losses in the Western bloc range anywhere
> between minus 1 percent and minus 8 percent, median minus 4 percent,
> in the Eastern bloc it falls in the minus 8 percent
> to minus 12 percent range, median minus 10.5 percent.

$$
\frac{10.5}{4} \approx 2.6
$$

**A decoupling costs the Chinese bloc about two and a half times
what it costs the Western bloc, by median.**
That points the same way as the war-cost asymmetry
reported by Gompert and others,
and it is the strongest available reason
to doubt the symmetric rows in this article's scenario table.

### The market that prices this risk does not currently price it

One concrete institutional fact is worth more here
than another round of estimates.
The Joint War Committee of the Lloyd's Market Association
and the International Underwriting Association
publishes the [list of areas][government_lma_2026_jwc_listed_areas]
in which vessels are considered at increased risk of war perils
and for which underwriters must be notified.

The circular current at the time of writing,
dated 16 September 2026,
was read in full for this article.
**Taiwan, the Taiwan Strait, the South China Sea,
mainland China and Hong Kong appear nowhere in it.**
The Southern Red Sea, the Black Sea, the Gulf of Guinea
and fourteen Middle Eastern entries do.

That is an absence read from the document rather than inferred.
It does not forecast anything,
since a listing can be added in days and the committee reviews periodically.
What it establishes is a baseline.
**The commercial market that prices war risk for the waterway
carrying more container traffic than any other
is, as of that date, charging nothing extra for it.**
A survey predicting a war that reorders the world
should record that the institution with money on the question
is not pricing one.

A related caution applies to the one peer-reviewed quantification of the chokepoint.
[Verschuur, Lumma and Hall][journal_verschuur_2025_chokepoints]
report an expected value of trade disrupted at the Taiwan Strait
of 37.3 billion dollars a year,
which circulates as a conflict figure.
Read in the paper, interstate conflict accounts for 13.2 billion of it,
the remainder being chiefly tropical cyclones,
and the estimated economic risk is 0.9 billion a year
"given shorter detours in case of disruptions".

$$
\frac{13.2}{37.3} \approx 0.35,
\qquad
\frac{0.9}{37.3} \approx 0.024
$$

**The headline figure is mostly weather,
and the modelled economic risk is under three percent of it.**

## Alliances and Proliferation, Where the Cascade Is Asserted More Often Than Measured

The one mechanism by which a Pacific war
could change the distribution of power quickly
runs through the alliance system rather than through industry.
If a visible American shortfall caused several wealthy states
to acquire nuclear weapons,
the distribution of the only capability that reliably deters great powers
would change within a decade.
Both RAND and the wargaming literature name this possibility.
The dedicated literature is markedly less confident.

### The base rate for cascades is about one in three

[Fuhrmann and Tkach][journal_fuhrmann_tkach_2015_nuclear_latency],
introducing a dataset of nuclear latency, report the relevant frequency.

> We show that nuclear latency is far more common than nuclear proliferation.
> 31 countries developed the capacity to build nuclear bombs from 1939 to 2012,
> and only 10 of those states went on to acquire atomic arsenals.

$$
\frac{10}{31} \approx 0.32
$$

**Roughly one latent capability in three became an arsenal
over seventy-three years.**
That is not a cascade.
It is also the number against which
any claim that a defeat would produce one should be set.
[Gavin][journal_gavin_2010_same_as_it_ever_was]
makes the historiographical version of the same point,
identifying a set of "myths about the history of the nuclear age"
underlying what he calls nuclear alarmism.

### The theory says allies are the states with opportunity and without willingness

[Monteiro and Debs][journal_monteiro_debs_2014_strategic_logic]
give the cleanest statement of why an alliance failure
is nonetheless the condition under which a cascade would occur.

> Willingness requires the presence of a grave security threat
> against which no ally offers reliable protection.
> Opportunity requires that the state pursuing nuclear weapons
> possess high relative power vis-a-vis its adversaries
> or enjoy the protection of a powerful ally.

**On that account a protected ally is precisely a state
that has the opportunity and lacks the willingness,
and a visible failure of protection converts one into the other.**
This is the strongest theoretical warrant in the literature
for the mechanism the wargames assert,
and it is worth noting that it comes from a formal argument
rather than from a scenario.

What restrains allies is itself disputed.
[Bleek and Lorber][journal_bleek_lorber_2014_security_guarantees]
find that security guarantees "significantly reduce proliferation proclivity
among their recipients".
[Gerzhoy][journal_gerzhoy_2015_alliance_coercion],
examining the West German case, reaches close to the opposite conclusion.

> Rather than preferring to renounce nuclear armament,
> Germany was compelled to do so by U.S. threats of military abandonment,
> contradicting the established logic of the security model.

**If Gerzhoy is right the implication for this article's subject is sharp.**
Restraint came from the patron's capacity to threaten abandonment credibly.
A patron weakened by a war has less of that capacity
at exactly the moment its reassurance is least believed,
so the two mechanisms fail together rather than substituting for one another.

### The one natural experiment says reassurance did not move opinion

South Korea is the case most cited for an imminent cascade,
and it has produced an unusually clean test.

The [Chicago Council's 2022 survey][data_chicago_council_2022_south_korea],
1,500 adults polled from 1 to 4 December 2021
with a margin of error of plus or minus 2.5 percent,
found 71 percent favouring an indigenous weapon
and, when forced to choose,
67 percent preferring that to redeployed American weapons against 9 percent.

$$
\frac{67}{9} \approx 7.4
$$

That survey was used in the [previous article][related_post_rebuilding]
and the ratio of roughly seven to one still holds.

The [Korea Institute for National Unification's 2023 survey][data_kinu_2023_unification_survey]
complicates it in two ways.
Its own time series shows support falling,
from 71.3 percent in 2021 to 69 percent in 2022 and 60.2 percent in 2023,
and its authors note this is "contrary to media reports".

$$
\frac{60.2 - 71.3}{71.3} \approx -0.16
$$

More importantly it shows the number is fragile to framing.

> When presented with six different possibilities of risks
> and asked whether nuclear weapons would be necessary
> in the face of those possibilities,
> public opinion in favor of continuing nuclear development dropped dramatically.
> Across all six items, only 36% to 37% agree with nuclear development.

Against the headline number that is close to a halving.

$$
\frac{36.5}{71.3} \approx 0.51
$$

And when the choice is posed against the alliance itself,
49.5 percent chose the continued presence of United States forces
and 33.8 percent chose nuclear weapons.

$$
\frac{49.5}{33.8} \approx 1.5
$$

**The natural experiment is the valuable part.**
The survey was in the field when the Washington Declaration was announced
on 27 April 2023,
with 504 respondents before and 497 after.
Support for indigenous weapons moved from 59.9 to 60.6 percent.

$$
p = 0.358
$$

> In other words, the Washington Declaration,
> which called for expanded deterrence
> in exchange for South Korea's giving up of its own nuclear armament,
> did not change South Korean public opinion in favor of nuclear armament.

Trust in extended deterrence rose from 68.7 to 75.6 percent
at $p = 0.103$, which also fails the conventional threshold.

**So the flagship reassurance instrument of the past decade
produced no measurable movement in the opinion it was designed to address.**
That cuts both ways for this article's question.
It weakens the claim that assurance can prevent a cascade.
It equally weakens the claim that assurance failure would cause one,
since the opinion in question appears not to respond to the alliance signal at all.

### Latency is already built, which changes what a war would have to do

Japan's position is the clearest case.
The [Cabinet Office's plutonium management report][government_japan_2025_plutonium]
records that at the end of 2024 Japan held
approximately 44.4 tonnes of separated plutonium,
of which approximately 8.6 tonnes was held domestically
and 35.8 tonnes abroad.

$$
21.7 + 14.1 = 35.8,
\qquad
8.6 + 35.8 = 44.4
$$

The overseas holdings are 21.7 tonnes in the United Kingdom
and 14.1 tonnes in France,
so **four fifths of the stock sits in two other states**.

$$
\frac{35.8}{44.4} \approx 0.81
$$

Japan's [National Security Strategy][government_japan_2022_nss]
commits it to "observing the Three Non-Nuclear Principles"
and describes the alliance, "including the provision of extended deterrence",
as the cornerstone of its security policy.
The same document set a defence budget target of two percent of gross domestic product
for fiscal year 2027,
and the [Ministry of Defense's budget overview][government_japan_2026_defense_budget]
records that the government "has brought forward the goal
to achieve the defense budget level of 2% of GDP
outlined in the current National Security Strategy (NSS) in FY2025".

**The target was met two years early, without a war.**
That is a second instance of the pattern this article keeps finding,
in which the quantity a war is supposed to change
is already changing for other reasons and at a comparable rate.

Australia's path under AUKUS raises the regime question rather than the capability one.
[Von Hippel][journal_von_hippel_2019_naval_propulsion]
sets out the mechanism,
which is the provision allowing a non-nuclear-weapon state
to remove material from safeguards for non-proscribed military use.

> No non-nuclear-weapon state has yet invoked paragraph 14,
> but a number have expressed interest in acquiring submarines
> powered by nuclear reactors.

He lists five that have considered it,
namely Brazil, Canada, Iran, Australia and South Korea,
which is the same list on which the hedging debate sits.
That article predates the AUKUS announcement by two years
and should be read as an account of the legal mechanism
rather than of the arrangement.

### The regime these arguments assume is already failing

[Arms Control Today's reporting][commentary_act_2026_npt_revcon]
on the 2026 Review Conference records that
diplomats from 130 states "failed to agree on ways to address
rising nuclear weapons dangers",
and places it in a sequence.

> This marks the third-straight NPT review conference
> at which states-parties failed to agree on a final conference outcome document.

The conference president is quoted saying
that a third failure "is disastrous for this regime".
**Three consecutive failures is a trend in the institution
that the proliferation-cascade argument treats as the constraint.**

The alliance baseline has moved too.
The [Congressional Research Service][government_crs_2026_extended_deterrence]
records that the 2026 National Defense Strategy
"did not explicitly mention extended deterrence,
instead stating that allies and partners would 'take primary responsibility'
for their own defense with 'critical but more limited U.S. support'".

That matters for how this article's question should be posed.
A war's effect on the alliance system
has to be measured against a baseline that is already moving,
and the baseline is moving in the direction
the war is supposed to push it.

### Allies may not want what the cascade literature assumes they want

[Henry][journal_henry_2020_what_allies_want]
tests the interdependence assumption on a Taiwan Strait case
and finds it does not hold in the form usually asserted.

> The First Taiwan Strait Crisis (1954-55) case study
> suggests that allies do not desire U.S. loyalty in all situations.
> Instead, they want the United States to be a reliable ally,
> posing no risk of abandonment or entrapment.

**Allied confidence is therefore not a monotonic function
of demonstrated American willingness to fight for Taiwan**,
because a demonstration of willingness also raises entrapment risk.
[Beckley][journal_beckley_2015_entangling_alliances]
makes the complementary point from the American side,
counting only five cases of plausible entanglement since 1945,
two of which are Taiwan Strait crises.

## A Survey of the Contemporary Literature

The sections above used the literature to argue.
This one reports it, including the parts that cut against the argument.
The organising principle is by dispute rather than by topic,
because on almost every question that matters here
the literature contains two defensible positions
and the article's contribution is to say which evidence separates them.

### Measuring national power, where the instruments disagree categorically

The disagreement among instruments is not marginal.
On the index used throughout this article,
China stood at 1.89 times the United States in 2022.
[SIPRI's 2026 fact sheet][data_sipri_2026_milex]
reports that "in 2025 the USA spent 2.8 times as much on the military as China",
with the United States at 954 billion current dollars and 33 percent of world spending
and China at an estimated 336 billion and 12 percent.
World Bank indicators for 2025 put Chinese gross domestic product
at about 134 percent of the American figure on purchasing power parity
and about 63 percent at market exchange rates.
The [Lowy Institute's Asia Power Index][data_lowy_2025_asia_power_index]
scores the United States at 80.4 and China at 73.7 for comprehensive power,
while scoring defence networks at 81.4 against 18.9.
Expressed as Chinese standing relative to American,
the five instruments give the following.

$$
1.89, \qquad
\frac{336}{954} \approx 0.35, \qquad
1.34, \qquad
0.63, \qquad
\frac{73.7}{80.4} \approx 0.92
$$

**Five instruments, five answers, spanning from
China at nearly twice the United States to China at under a quarter.**

$$
\frac{1.89}{0.35} \approx 5.4
$$

The extreme readings differ by a factor of more than five.
On the component where the alliance system is counted
the gap is wider still.

$$
\frac{81.4}{18.9} \approx 4.3
$$

The index that produces the most dramatic Chinese lead
is the one this article uses,
which is a reason to distrust the levels it reports
and the reason the argument above was built on ratios and on direction.

The critiques are specific.
[Carroll and Kenkel][journal_carroll_kenkel_2019_prediction_proxies]
report that the capability ratio
"is barely better than random guessing at predicting militarized dispute outcomes",
and build a replacement from the same underlying data
that is "an order of magnitude better".
**That is the most damaging available finding about this instrument,
and it is damaging in the right way,
since it indicts the aggregation rule rather than the measurements.**
[Beckley][journal_beckley_2018_power_of_nations]
argues that gross indicators
"exaggerate the wealth and military power of poor, populous countries,
such as China and India",
and that net measures predict dispute outcomes better.
[Anders, Fariss and Markowitz][journal_anders_2020_surplus_domestic_product]
make the same move for output,
separating subsistence income from the surplus
that can actually be converted into arms.
[Brooks and Wohlforth][journal_brooks_wohlforth_2016_rise_and_fall]
add that the conversion itself has become harder,
so that "the transition from a great power to a superpower
is much harder now than it was in the past".

Every one of those critiques points the same way,
which is that this article's headline index
overstates China relative to the United States.
The article reports the index anyway,
because overstating the challenger is the conservative direction
for an argument that a war would not change the standing much.

### Power transition theory, where the family agrees the war is not the cause

Covered above and summarised here for the survey's completeness.
[Gilpin][journal_gilpin_1988_hegemonic_war] has the settlement reflect an emergent distribution.
[Organski and Kugler][journal_organski_kugler_1977_phoenix] have losers resume antebellum status in fifteen to twenty years.
[Powell][journal_powell_2006_commitment_problem], [Levy][journal_levy_1987_declining_power]
and [Fearon][journal_fearon_1995_rationalist] all run causation from shift to war.
[Chadefaux][journal_chadefaux_2011_bargaining] shows a shift alone is never sufficient under complete information.
[Doran and Parsons][journal_doran_parsons_1980_war_cycle]
offer the main rival within the family,
locating war at inflection points on an already-traced capability curve,
which inherits the same measurement problems
because it is operationalised on near-identical inputs.
[DiCicco and Levy][journal_dicicco_levy_1999_power_shifts]
assess the programme from inside and find parts of it degenerating.

### Whether Taiwan itself changes the military balance

This is the sharpest two-sided dispute in the field
and it bears directly on whether the war's object is worth the war.
[Green and Talmadge][journal_green_talmadge_2022]
argue Chinese control of the island
"would likely improve the military balance in China's favor"
through submarine basing and ocean surveillance.
[Caverley][journal_caverley_2025] answers with a kill-chain model
and reaches the opposite conclusion,
that the transformation "would make little difference to the broader military balance".
His quantitative argument is the memorable one.

> At 395 kilometers from north to south,
> the additional range ring provided by Taiwan
> is a minor bump along the Chinese mainland's 14,500 km of coastline.

$$
\frac{395}{14{,}500} \approx 0.027
$$

**Less than three percent.**
[Anderson and Press][journal_anderson_press_2025_access_denied]
come at the same question from the American side
and find that the current approach to defending Taiwan
"exposes U.S. forces to significant risk of catastrophic defeat".

### The economics of a conflict, where the estimates measure different things

Covered above.
The important methodological point for a survey
is that the headline numbers are not commensurable.
[Rhodium][research_rhodium_2022_taiwan_disruptions] measures trade and investment at risk of disruption
and explicitly declines to estimate welfare loss.
[Nikkei][commentary_nikkei_2022_taiwan_emergency] measures value added lost under a trade halt.
[Gompert and others][research_gompert_2016_war_with_china] measure reduction in gross domestic product for a year of war.
Three quantities, three units, one subject.
The previous article in this series found the same pattern
in the reconstruction-cost literature
and the diagnosis here is identical.

[Vest and Kratz][research_vest_kratz_2023_sanctioning_china]
add the financial dimension,
estimating "at least \$3 trillion in trade and financial flows"
at immediate risk in a maximalist sanctions scenario,
and noting that 77 percent of China's trade
is settled in currencies other than the renminbi.

### Hedging and alignment, where the survey data oscillate around parity

The [ISEAS State of Southeast Asia survey][data_iseas_2026_state_of_southeast_asia],
fielded from 5 January to 20 February 2026 with 2,008 respondents,
asked which rival ASEAN should choose if forced.
China took 52.0 percent against the United States at 48.0,
having been 47.7 against 52.3 the previous year.

$$
52.0 - 48.0 = 4.0,
\qquad
52.3 - 47.7 = 4.6
$$

The margin reversed sign between the two years
while barely changing in magnitude.
The report's own reading is the right one,
that the margin "reflects a deeply divided strategic landscape
rather than a decisive shift toward one pole".
**Three consecutive reversals within sampling error
should be read as noise around parity and not as a trend.**

Two findings from the same survey bear on this article more directly.
Concern about "forceful reunification with Taiwan"
ranks at 8.6 percent among factors that could worsen regional views of China,
and American support for Taiwan ranks lowest of all at 2.6 percent
among factors that could worsen views of the United States,
far behind trade measures at 43.4 percent.
**In the region that would host the war,
Taiwan is not the dominant factor in alignment.**

European opinion runs the same way.
[European Council on Foreign Relations polling][research_ecfr_2023_a_la_carte]
of 16,168 respondents across eleven European Union states in April 2023
found about a quarter wanting their country to take the American side
in a Taiwan conflict, with a clear majority preferring neutrality.
A later and larger survey of 25,266 respondents
found 8 percent of Europeans supporting their own troops fighting in such a war
against 32 percent of Americans.

### The alliance literature, where loyalty is not the variable it is assumed to be

Covered above through [Henry][journal_henry_2020_what_allies_want]
and [Beckley][journal_beckley_2015_entangling_alliances].
[Snyder's][journal_snyder_1984_security_dilemma] original formulation
is the source of the abandonment and entrapment pair
and remains the frame most of this work operates in.

### Nuclear weapons and the base rate, where the estimates are unstable to specification

The historical base rate computed in this article
is drawn almost entirely from pre-nuclear cases,
which raises the question of whether nuclear weapons change it.
The literature does not give a stable answer.
[Rauchhaus][journal_rauchhaus_2009_nuclear_peace]
finds that when both sides have nuclear weapons
"the odds of war precipitously drop",
with more risk-taking at lower intensities.
[Bell and Miller][journal_bell_miller_2015_questioning]
re-estimate and find that nuclear dyads
"are not significantly less likely to fight wars",
noting that previous work had suggested
such dyads were "some 2.7 million times less likely to fight wars".

$$
2{,}700{,}000 \longrightarrow \text{not significant}
$$

**A headline effect of nearly three million to one
reduced to statistical insignificance by a change of estimator
is the clearest available illustration
of how little weight these estimates bear.**
[Sechser and Fuhrmann][journal_sechser_fuhrmann_2013_nuclear_blackmail],
using more than 200 compellent threats from 1918 to 2001,
find that "compellent threats from nuclear states are no more likely to succeed".

### The long peace, where the statistics do not yet support a trend

[Clauset][journal_clauset_2018_trends_fluctuations],
using the same war data this article uses,
finds that the postwar absence of great-power war
is not yet distinguishable from a fluctuation.

> The models indicate that the postwar pattern of peace
> would need to endure at least another 100 to 140 years
> to become a statistically significant trend.

[Cirillo and Taleb][journal_cirillo_taleb_2016_tail_risk]
reach a compatible conclusion from a different method,
finding the true mean of war casualties
"considerably larger than the sample mean"
and that "no particular trend can be asserted"
in inter-arrival times between tail events.

### Prediction accuracy, where the measured record is poor

[Tetlock's][book_tetlock_2005_expert_political_judgment]
tournament produced 82,361 probability estimates
and the two numbers most relevant here are these.
Events experts called impossible or nearly impossible
occurred about 15 percent of the time,
and events they called certain or nearly certain
failed to occur about 27 percent of the time.

$$
\Pr(\text{occurs} \mid \text{called impossible}) \approx 0.15,
\qquad
\Pr(\text{fails} \mid \text{called certain}) \approx 0.27
$$

**Both of those should be near zero and neither is.**
[Chang and others][journal_chang_2016_developing_expert_judgment]
later showed that under an hour of debiasing training
improved accuracy by 6 to 11 percent,
which is encouraging about the remedy
and unflattering about the baseline.

The worked example closest to this subject
is [Nordhaus's][research_nordhaus_2002_iraq_cost] pre-invasion costing of the Iraq war,
which opens by observing that
"nations historically have consistently underestimated
the cost of military conflicts"
and gives a range of 100 billion to 1.9 trillion dollars.
[Chang and others][journal_chang_2016_developing_expert_judgment]
report the outturn in passing, writing that the United States
"would continue its involvement in the country for over a decade
at an estimated cost between \$4 and \$6 trillion",
a figure they attribute to Bilmes
and which is not independently checked here.
Taken at its lower end it exceeds the top of the forecast range
by a factor of about two.

$$
\frac{4.0}{1.9} \approx 2.1
$$

**A paper whose thesis was that cost estimates run low
was itself low, and by more than its own upper bound.**

### The order literature, which changed the object of study

[Mearsheimer][journal_mearsheimer_2019_bound_to_fail]
argues the liberal international order was "bound to fail"
and that multipolarity will produce "two bounded orders".
[Ikenberry][book_ikenberry_2019_after_victory] sets out the victor's three choices,
and [elsewhere][journal_ikenberry_2024_three_worlds]
describes a drift toward a global West, East and South.
[Cooley and Nexon][book_cooley_nexon_2020_exit_from_hegemony]
model the unravelling instead of the construction.
[Walt][journal_walt_2025_hedging_hegemony]
reviews the realist debate and concludes
that "a Chinese bid for hegemony in Asia is likely to fail",
on the ground that bids for regional hegemony
are usually thwarted by balancing coalitions,
which is the same mechanism RAND's scenarios produced.
[Menon][journal_menon_2026_new_world_order],
writing from outside the Western institutions that dominate this survey,
argues the world is "between orders"
and that this "may mark a return to the historical norm".

The dissenting measurement comes from [Lind][journal_lind_2024_back_to_bipolarity],
who validates capability metrics against known historical balances
and concludes that "China on most dimensions
is not only a great power but a superpower"
while "neither Russia nor India is a great power".
**That conclusion is in direct tension with this article's arithmetic**,
which puts India at about four fifths of the American capability share
and has it passing the United States
in one of the four scenario rows.
The tension is not resolvable here
and it is exactly the measurement dependence this article has been documenting.
Lind's method validates metrics by their ability
to reproduce balances we already believe in,
which is a defensible procedure
and one that cannot discover a great power nobody currently recognises.

## Where the Sources Agree and Where They Do Not

### Four agreements that hold across methods

**That the published record stops before the question.**
RAND's project director says there is "very little attention or planning
devoted to the aftermath".
RAND recommends building a wargame set after a great-power war.
The most cited public wargame places the political assessment out of scope
and gives the postwar distribution of power one clause.
The official foresight product models five distributions of power
and reaches none of them through a great-power war.
No source located for this article contradicts that description.

**That victory does not guarantee a better postwar position.**
RAND states it in its conclusions.
The wargame states it as "victory is not everything".
The base rate computed here puts a number on it,
with more than a third of large-war winners declining.
Kennedy's manufacturing shares show the same for Britain after 1918.
This is the firmest agreement in the whole survey
and it crosses method, era and discipline.

**That prewar forecasts about consequences are usually wrong.**
RAND's ten-case coding gives one full success in ten
on the balance-of-power dimension.
Tetlock's tournament gives the general base rate.
Gilpin notes that neither the Greeks nor the Europeans of 1914
anticipated what their wars would do.
Nordhaus provides a worked instance.

**That the measurement choice determines the answer.**
This is agreed by the people who build the instruments.
The Correlates of War codebook warns against longitudinal use of components.
Lowy states that other value judgements about its weights are possible.
SIPRI warns that its revision replaces all previously published data.
Carroll and Kenkel show the standard ratio barely beats guessing.
Allison's own project concedes there are no agreed metrics of national power.

### Seven disagreements, each with both sides named

**Whether a war durably changes the distribution at all.**
Organski and Kugler say losers resume antebellum status in fifteen to twenty years.
This article's computation finds every large-war loser down at ten years,
with a median loss of 42 percent.
The windows differ and the samples differ, and the two have not been reconciled.

**Whether non-participants gain.**
RAND asserts that victors "will be weakened relative to noncombatant states",
and Frederick says the great power that benefits most is the one that did not fight.
The historical test in this article finds no such pattern,
for the reason that no historical case had a large enough bystander pool.
Nikkei's trade modelling finds non-belligerents bearing heavy absolute costs.
All three can hold simultaneously and the article says so.

**Whether the belligerents decline symmetrically.**
The scenario table here treats symmetric outcomes as two of four cases.
Gompert and others estimate Chinese losses at about four times American losses.
Nothing in the capability data adjudicates this,
because the capability index is insensitive to the trade interdiction
that drives the asymmetry.

**Whether Taiwan is militarily worth taking.**
Green and Talmadge say yes through submarine basing and surveillance.
Caverley says the island adds under three percent of relevant coastline
and would make little difference.
Both are published, recent, and methodologically explicit.

**Whether security guarantees restrain allies.**
Bleek and Lorber find they do.
Gerzhoy finds restraint came instead from threats of abandonment.
Monteiro and Debs provide a framework in which both can be true
depending on which of willingness and opportunity binds.

**Whether a cascade would follow a visible American failure.**
The wargames and RAND treat it as a live risk.
Fuhrmann and Tkach's base rate is about one in three over seventy years.
The one natural experiment, on the Washington Declaration,
found allied opinion unmoved by the alliance signal in either direction.

**Whether the system is already bipolar, and who counts.**
Lind says yes and that neither Russia nor India is a great power.
The capability data used here put India at four fifths of the United States.
The Atlantic Council's expert panel expects multipolarity by nine to one.
These cannot all be right,
and the disagreement is about measurement rather than about the world.

### What the pattern of disagreement shows

Every disagreement above is a disagreement about an instrument
or about a window,
and not one is a disagreement about an observed event.
That is characteristic of a field
whose central object has not occurred,
and it is the reason this article put so much weight
on data generated for other purposes.
**Where the sources agree, they agree about the past.
Where they disagree, they disagree about how to measure it.**

## Six Gaps in the Literature

**No published wargame continues into the postwar distribution of power.**
RAND recommends building one.
Nothing located for this article indicates one exists.
This is the same gap the previous article found for reconstruction,
one step further out.

**No study models a great-power war
in which the belligerents hold a minority of world capability.**
Every historical case has the belligerents at 82 percent or more.
The structural condition that makes bystander redistribution possible
is new and unmodelled.

**The two literatures on cost do not share units.**
Capability share, value added at risk, and reduction in gross domestic product
are three different quantities reported in the same debates
as though they were comparable.
No source located attempts a reconciliation,
and this article's attempt above is partial.

**There is no post-conflict strategy study for China
equivalent to the one that exists for Russia.**
RAND published a planning-for-the-aftermath study for Russia in 2024.
No China equivalent was located.
Whether that is absence or classification cannot be determined from outside.

**No located study tests the long-war conclusion
against current debt-service projections.**
The judgement that a protracted conflict favours the United States
rests on trade and output.
It was reached before net interest overtook defence discretionary spending
as a share of output, which happened on the projections cited above in 2025.
Whether that changes the conclusion is a live question
and no source located addresses it.

**The effect of great-power nuclear use on the nonproliferation regime
appears unaddressed.**
The regime literature addresses the consequences of review-conference failure.
The proliferation literature addresses cascades after conventional alliance failure.
No located source addresses what the treaty regime does
after a nuclear weapon is used by a great power,
which is a branch that several of the scenarios in this series pass through.

## Epistemic State

**Computed from primary data for this article.**
Every quantitative claim about capability shares, base rates and scenario arithmetic
was computed from two files,
the Correlates of War National Material Capabilities version 7.0
and the Inter-State War Data version 4.0,
both downloaded from the project's own site.
The computation is independently checkable.
Three harnesses re-entered 238 constants by hand from the article text
and recomputed each,
which caught two errors before publication,
a relative change stated as 1.07 that is 1.06,
and a claim that the capability ratio has exceeded one in every year since 1995
when it dips below in 2002.
**The third harness checks only the article's own arithmetic
on figures it quotes from the literature.**
It cannot establish that a source says what the article reports,
which is done by reading the source,
and it is kept separate from the two that recompute from primary data
so that the distinction is not lost.
**The second of those turned into a section,
because tracing the dip located a documented definitional break.**

**Read in primary text.**
Both volumes of the RAND Alternative Futures study, in full.
The Correlates of War version 7.0 codebook.
The published CINC series and its six components.
The inter-state war participant file.
The Joint War Committee listed-areas circular of 16 September 2026, in full,
which is how the absence of Taiwan from it is reported as an absence
rather than inferred from silence.

**Retrieved and recomputed rather than quoted.**
The reserve-composition series was pulled from the International Monetary Fund's
own data interface and parsed for this article,
with a payload stamped 30 September 2026.
The dollar and renminbi shares, the series minimum,
and the before-and-after drift rates across the 2022 reserve freeze
are all computed from that file.
**That computation produced the one result in this article
that most surprised its author**,
which is that the dollar's reserve share has declined slightly more slowly
since the freeze than in the twenty-three years before it,
and that the renminbi's share peaked a quarter before the freeze
rather than rising after it.
Several widely repeated claims about accelerated de-dollarisation
do not survive contact with the series.

**Read at one remove, and labelled where used.**
Several quotations in the survey come from publisher-deposited abstracts
rather than from article bodies,
because the publishers in question refuse automated access.
That applies to Organski and Kugler, Carroll and Kenkel,
Monteiro and Debs, Gerzhoy, Bleek and Lorber, Fuhrmann and Tkach,
Rauchhaus, Bell and Miller, Sechser and Fuhrmann, Beckley,
Anders and others, Brooks and Wohlforth, Green and Talmadge, Snyder,
Henry, Powell, Levy, Fearon, Chadefaux, DiCicco and Levy,
Doran and Parsons, Lind, Mearsheimer and Walt.
**An abstract is the publisher's summary and not the author's running prose,
and no page-located claim is made from one.**

**One figure was read off an image rather than text.**
The RAND forecasting-accuracy table is published as a colour-coded grid,
and colour does not survive text extraction.
The page was rendered and read directly.
The count of one green, six yellow and three red
on the balance-of-power column
agrees with the count stated in the previous article in this series,
which was obtained independently,
and with a separate reconstruction by pixel classification.
Three independent routes to the same count
is the basis for reporting it.

**What bounds this survey.**
English-language sources only.
Several institutional catalogues render their indexes in script
and could not be enumerated, including Carnegie, Brookings, Stimson and Hudson,
so think-tank coverage is thinner than journal coverage
and the gap is not random with respect to the subject.
Foreign Affairs is essentially unrepresented for the same reason.
No Chinese-language source was consulted,
which for an article about Chinese standing is a material limitation
and not a minor one.

**Where this article is most likely to be wrong.**
The base rate rests on an industrial-age index,
and the strongest critique of that index
reports it barely outperforms guessing at predicting dispute outcomes.
If that critique is right,
the base rate measures something real about steel and population
and little about power.
The scenario arithmetic applies a median to a single case
with wide dispersion behind it.
The bystander argument is structural rather than empirical,
since the historical record cannot test it.
And the whole article measures capability,
while the most persuasive account of how a Pacific war
would change the world, the Suez analogy,
describes a mechanism that capability data cannot see.

## Out of Scope

- The conduct of the war, which the [first article][related_post_published_wargames] covers.
- Reconstitution and reconstruction, which the [second][related_post_rebuilding] covers.
- Classified assessments, which exist and are not public.
- Any recommendation about force structure, alliance management or industrial policy.
- Chinese-language and Russian-language scholarship on the postwar order.
- The domestic political consequences within either belligerent,
beyond the regime-survival material already covered in the previous article.
- Any forecast of whether the war occurs,
on which this article takes no position.
- Normative questions about whether any of this should be fought over.
- Any claim that the survey above is exhaustive.
It is bounded by language, by what registries index,
and by publishers that refuse automated access.

## Conclusion

The question in the title has three answers
and the article has argued that the third is the useful one.

**On the measured distribution of capability, probably less than expected.**
The transition the war would be fought over
was recorded by the standard instrument in 1995.
The median large-war winner improves its relative standing by about an eighth
and the median large-war loser gives up about two fifths,
so an American victory at the historical rate produces approximate parity
rather than restored primacy,
and a Chinese defeat at the historical rate
leaves China above where the United States stands today.
RAND, working by scenario rather than by base rate,
reached the compatible conclusion
that no plausible non-nuclear outcome strips either state of great-power status,
and named the Franco-Prussian and Korean wars as the scale of analogue.
Those two wars moved relative standing by 27 and 18 percent respectively.
That is a real change and it is not a new world.

**On the distribution of power in the world, possibly a great deal,
and for a reason that has no historical precedent.**
The belligerents of 1914 held 82 percent of measured world capability
and those of 1939 held 98 percent.
Two states fighting this war would hold about 36 percent,
and about 45 percent on the widest plausible coalition.
For the first time in the period the data cover,
there would be a pool of non-participants
large enough to absorb a serious redistribution.
Whether it would is not knowable from the historical record,
because the historical record contains no such case.
**The honest statement is that the mechanism everyone asserts
has never been testable before and now would be.**

**And on what should be believed about any of this, very little with confidence.**
In one of ten historical great-power wars
did every combatant correctly forecast the consequences for the balance of power,
and the three cases where all of them were wrong are the three largest.
The index this article leans on
does not sum to one in 183 of its 207 years,
contains a definitional change that cut recorded American urban population by 44 percent,
and is reported by its sharpest critics
to barely outperform random guessing at the task it exists for.
The most persuasive single account of how such a war would change the world,
the hollowing of an alliance system after a visible humiliation,
describes a mechanism that left no trace in any capability series after Suez.

So the article ends where the data end rather than where the question does.
**A war between the United States and China
would be unlikely to restore an American advantage that has already gone,
unlikely to remove China from the ranks of great powers,
and uniquely likely, by the arithmetic of who would be fighting,
to transfer standing to states doing nothing at all.**
Each of those three is a statement about measured capability,
each rests on an instrument whose makers warn against this use,
and the third has never happened before.

The financial series point the same way and from a different direction.
The dollar's reserve share has fallen by eighteen points since 1999,
which is a genuine erosion,
and it fell no faster after a great power's reserves were seized
than in the two decades before.
The currency that was supposed to benefit
has lost a quarter of its peak share since that event.
**If the slowest-moving instrument of American power
did not respond measurably to the sharpest financial shock of the century,
the prior that it would respond to a Pacific war should be weak.**
That is a thinner set of conclusions
than the volume of writing on this subject would suggest is available,
and the thinness is the finding.

## References

- [Book, Cooley and Nexon 2020, Exit from Hegemony][book_cooley_nexon_2020_exit_from_hegemony]
- [Book, Gilpin 1981, War and Change in World Politics][book_gilpin_1981_war_and_change]
- [Book, Ikenberry 2019, After Victory][book_ikenberry_2019_after_victory]
- [Book, Singer, Bremer and Stuckey 1972, Capability Distribution, Uncertainty, and Major Power War, 1820 to 1965][book_singer_1972_capability_distribution]
- [Book, Tetlock 2005, Expert Political Judgment][book_tetlock_2005_expert_political_judgment]
- [Commentary, Arms Control Today 2026, 2026 NPT Review Conference Stymied by Disputes][commentary_act_2026_npt_revcon]
- [Commentary, Nikkei 2022, 2.6tn Dollars Could Evaporate From the Global Economy in a Taiwan Emergency][commentary_nikkei_2022_taiwan_emergency]
- [Data, Bank for International Settlements 2025, Triennial Central Bank Survey, OTC Foreign Exchange Turnover in April 2025][data_bis_2025_triennial]
- [Data, Congressional Budget Office 2026, Budget and Economic Projections][data_cbo_2026_projections]
- [Data, Chicago Council on Global Affairs 2022, Thinking Nuclear, South Korean Attitudes on Nuclear Weapons][data_chicago_council_2022_south_korea]
- [Data, Correlates of War 2020, Inter-State War Data version 4.0][data_cow_interstate_war_v4]
- [Data, Sarkees and Wayman 2010, Correlates of War Inter-State Wars Codebook][data_cow_interstate_wars_codebook]
- [Data, Correlates of War 2025, National Material Capabilities version 7.0][data_cow_nmc_v7]
- [Data, International Monetary Fund 2026, Currency Composition of Official Foreign Exchange Reserves][data_imf_cofer]
- [Data, ISEAS Yusof Ishak Institute 2026, The State of Southeast Asia 2026 Survey Report][data_iseas_2026_state_of_southeast_asia]
- [Data, Korea Institute for National Unification 2023, KINU Unification Survey 2023][data_kinu_2023_unification_survey]
- [Data, Lowy Institute 2025, Asia Power Index][data_lowy_2025_asia_power_index]
- [Data, SIPRI 2026, Trends in World Military Expenditure 2025][data_sipri_2026_milex]
- [Data, United States Treasury 2026, Major Foreign Holders of Treasury Securities][data_treasury_tic_2026]
- [Government, Congressional Research Service 2026, United States Extended Deterrence and Regional Nuclear Capabilities][government_crs_2026_extended_deterrence]
- [Government, Government of Japan 2022, National Security Strategy of Japan][government_japan_2022_nss]
- [Government, Government of Japan 2025, The Status Report of Plutonium Management in Japan 2024][government_japan_2025_plutonium]
- [Government, Ministry of Defense of Japan 2025, Overview of the FY2026 Defense Budget][government_japan_2026_defense_budget]
- [Government, Lloyd's Market Association 2026, Joint War Committee Listed Areas][government_lma_2026_jwc_listed_areas]
- [Government, National Intelligence Council 2021, Global Trends 2040, A More Contested World][government_nic_2021_global_trends]
- [Journal, Anders, Fariss and Markowitz 2020, Bread Before Guns or Butter, International Studies Quarterly 64 number 2][journal_anders_2020_surplus_domestic_product]
- [Journal, Anderson and Press 2025, Access Denied, International Security 50 number 1][journal_anderson_press_2025_access_denied]
- [Journal, Arslanalp, Eichengreen and Simpson-Bell 2022, The Stealth Erosion of Dollar Dominance, Journal of International Economics 138][journal_arslanalp_2022_stealth_erosion]
- [Journal, Beckley 2015, The Myth of Entangling Alliances, International Security 39 number 4][journal_beckley_2015_entangling_alliances]
- [Journal, Beckley 2018, The Power of Nations, International Security 43 number 2][journal_beckley_2018_power_of_nations]
- [Journal, Bell and Miller 2015, Questioning the Effect of Nuclear Weapons on Conflict, Journal of Conflict Resolution 59 number 1][journal_bell_miller_2015_questioning]
- [Journal, Bianchi and Sosa-Padilla 2025, International Sanctions and Dollar Dominance, The Economic Journal 135 number 672][journal_bianchi_sosa_padilla_2025_sanctions_dollar]
- [Journal, Bleek and Lorber 2014, Security Guarantees and Allied Nuclear Proliferation, Journal of Conflict Resolution 58 number 3][journal_bleek_lorber_2014_security_guarantees]
- [Journal, Brooks and Wohlforth 2016, The Rise and Fall of the Great Powers in the Twenty-first Century, International Security 40 number 3][journal_brooks_wohlforth_2016_rise_and_fall]
- [Journal, Carroll and Kenkel 2019, Prediction, Proxies, and Power, American Journal of Political Science 63 number 3][journal_carroll_kenkel_2019_prediction_proxies]
- [Journal, Caverley 2025, So What, Texas National Security Review 8 number 3][journal_caverley_2025]
- [Journal, Chadefaux 2011, Bargaining Over Power, International Theory 3 number 2][journal_chadefaux_2011_bargaining]
- [Journal, Chang, Chen, Mellers and Tetlock 2016, Developing Expert Political Judgment, Judgment and Decision Making 11 number 5][journal_chang_2016_developing_expert_judgment]
- [Journal, Chitu, Eichengreen and Mehl 2014, When Did the Dollar Overtake Sterling as the Leading International Currency, Journal of Development Economics 111][journal_chitu_2014_bond_markets]
- [Journal, Cirillo and Taleb 2016, On the Statistical Properties and Tail Risk of Violent Conflicts, Physica A 452][journal_cirillo_taleb_2016_tail_risk]
- [Journal, Clauset 2018, Trends and Fluctuations in the Severity of Interstate Wars, Science Advances 4 number 2][journal_clauset_2018_trends_fluctuations]
- [Journal, Davis and Weinstein 2002, Bones, Bombs, and Break Points, American Economic Review 92 number 5][journal_davis_weinstein_2002_bones_bombs]
- [Journal, DiCicco and Levy 1999, Power Shifts and Problem Shifts, Journal of Conflict Resolution 43 number 6][journal_dicicco_levy_1999_power_shifts]
- [Journal, Doran and Parsons 1980, War and the Cycle of Relative Power, American Political Science Review 74 number 4][journal_doran_parsons_1980_war_cycle]
- [Journal, Farrell and Newman 2019, Weaponized Interdependence, International Security 44 number 1][journal_farrell_newman_2019_weaponized]
- [Journal, Fearon 1995, Rationalist Explanations for War, International Organization 49 number 3][journal_fearon_1995_rationalist]
- [Journal, Fuhrmann and Tkach 2015, Almost Nuclear, Conflict Management and Peace Science 32 number 4][journal_fuhrmann_tkach_2015_nuclear_latency]
- [Journal, Gavin 2010, Same As It Ever Was, International Security 34 number 3][journal_gavin_2010_same_as_it_ever_was]
- [Journal, Gerzhoy 2015, Alliance Coercion and Nuclear Restraint, International Security 39 number 4][journal_gerzhoy_2015_alliance_coercion]
- [Journal, Gilpin 1988, The Theory of Hegemonic War, Journal of Interdisciplinary History 18 number 4][journal_gilpin_1988_hegemonic_war]
- [Journal, Gopinath and Stein 2021, Banking, Trade, and the Making of a Dominant Currency, Quarterly Journal of Economics 136 number 2][journal_gopinath_stein_2021_dominant_currency]
- [Journal, Green and Talmadge 2022, Then What, International Security 47 number 1][journal_green_talmadge_2022]
- [Journal, Henry 2020, What Allies Want, International Security 44 number 4][journal_henry_2020_what_allies_want]
- [Journal, Ikenberry 2024, Three Worlds, International Affairs 100 number 1][journal_ikenberry_2024_three_worlds]
- [Journal, Levy 1987, Declining Power and the Preventive Motivation for War, World Politics 40 number 1][journal_levy_1987_declining_power]
- [Journal, Lind 2024, Back to Bipolarity, International Security 49 number 2][journal_lind_2024_back_to_bipolarity]
- [Journal, Mearsheimer 2019, Bound to Fail, International Security 43 number 4][journal_mearsheimer_2019_bound_to_fail]
- [Journal, Menon 2026, A New World Order, Texas National Security Review 9 number 1][journal_menon_2026_new_world_order]
- [Journal, Monteiro and Debs 2014, The Strategic Logic of Nuclear Proliferation, International Security 39 number 2][journal_monteiro_debs_2014_strategic_logic]
- [Journal, Nemeth 2026, How a United States Suez Moment Could Hollow the Alliance System, Texas National Security Review 9 number 1][journal_nemeth_2026_suez_moment]
- [Journal, Organski and Kugler 1977, The Costs of Major Wars, The Phoenix Factor, American Political Science Review 71 number 4][journal_organski_kugler_1977_phoenix]
- [Journal, Powell 2006, War as a Commitment Problem, International Organization 60 number 1][journal_powell_2006_commitment_problem]
- [Journal, Rauchhaus 2009, Evaluating the Nuclear Peace Hypothesis, Journal of Conflict Resolution 53 number 2][journal_rauchhaus_2009_nuclear_peace]
- [Journal, Sechser and Fuhrmann 2013, Crisis Bargaining and Nuclear Blackmail, International Organization 67 number 1][journal_sechser_fuhrmann_2013_nuclear_blackmail]
- [Journal, Snyder 1984, The Security Dilemma in Alliance Politics, World Politics 36 number 4][journal_snyder_1984_security_dilemma]
- [Journal, Verschuur, Lumma and Hall 2025, Systemic Impacts of Disruptions at Maritime Chokepoints, Nature Communications 16][journal_verschuur_2025_chokepoints]
- [Journal, Von Hippel 2019, Mitigating the Threat of Nuclear-Weapon Proliferation via Nuclear-Submarine Programs, Journal for Peace and Nuclear Disarmament 2 number 1][journal_von_hippel_2019_naval_propulsion]
- [Journal, Walt 2025, Hedging on Hegemony, International Security 49 number 4][journal_walt_2025_hedging_hegemony]
- [Related Post, What Published Wargames Say About a War With China][related_post_published_wargames]
- [Related Post, What Rebuilding Would Take After a War With China][related_post_rebuilding]
- [Research, Atlantic Council 2025, Welcome to 2035][research_atlantic_council_2025_welcome_2035]
- [Research, Atlantic Council 2026, Welcome to 2036][research_atlantic_council_2026_welcome_2036]
- [Research, Cancian, Cancian and Heginbotham 2023, The First Battle of the Next War][research_cancian_2023_first_battle]
- [Research, Dooley, Folkerts-Landau and Garber 2022, US Sanctions Reinforce the Dollar's Dominance][research_dooley_2022_sanctions_reinforce]
- [Research, European Council on Foreign Relations 2023, Living in an a la Carte World][research_ecfr_2023_a_la_carte]
- [Research, Evans 2023, Alternative Futures Following a Great Power War, Volume 2][research_evans_2023_alternative_futures_v2]
- [Research, Goes and Bekkers 2022, The Impact of Geopolitical Conflicts on Trade, Growth, and Innovation][research_goes_bekkers_2022_geopolitical_conflicts]
- [Research, Gompert, Cevallos and Garafola 2016, War with China, Thinking Through the Unthinkable][research_gompert_2016_war_with_china]
- [Research, Kwende and Nephew 2025, Improving the Analytical Usefulness of the IMF's COFER Data][research_kwende_nephew_2025_cofer]
- [Research, Nordhaus 2002, The Economic Consequences of a War with Iraq][research_nordhaus_2002_iraq_cost]
- [Research, Priebe and others 2023, Alternative Futures Following a Great Power War, Volume 1][research_priebe_2023_alternative_futures_v1]
- [Research, Priebe and Frederick 2023, Alternative Futures Following a Great Power War, In Conversation][research_priebe_frederick_2023_conversation]
- [Research, Rhodium Group 2022, The Global Economic Disruptions from a Taiwan Conflict][research_rhodium_2022_taiwan_disruptions]
- [Research, Tarapore 2024, Deterring an Attack on Taiwan, Policy Options for India and Other Non-Belligerent States][research_tarapore_2024_deterring_attack]
- [Research, Vest and Kratz 2023, Sanctioning China in a Taiwan Crisis][research_vest_kratz_2023_sanctioning_china]
- [Research, Weiss 2025, De-Dollarization, Diversification, Exploring Central Bank Gold Purchases][research_weiss_2025_dedollarization]

[book_cooley_nexon_2020_exit_from_hegemony]: https://doi.org/10.1093/oso/9780190916473.001.0001
[book_gilpin_1981_war_and_change]: https://doi.org/10.1017/cbo9780511664267
[book_ikenberry_2019_after_victory]: https://doi.org/10.23943/princeton/9780691169217.001.0001
[book_singer_1972_capability_distribution]: https://doi.org/10.4324/9780203128398-28
[book_tetlock_2005_expert_political_judgment]: https://doi.org/10.1515/9781400888818
[commentary_act_2026_npt_revcon]: https://www.armscontrol.org/act/2026-06/news/2026-npt-review-conference-stymied-disputes
[commentary_nikkei_2022_taiwan_emergency]: https://asia.nikkei.com/static/vdata/infographics/2-dot-6tn-dollars-could-evaporate-from-global-economy-in-taiwan-emergency/
[data_bis_2025_triennial]: https://www.bis.org/statistics/rpfx25_fx.htm
[data_cbo_2026_projections]: https://www.cbo.gov/publication/51118
[data_chicago_council_2022_south_korea]: https://globalaffairs.org/research/public-opinion-survey/thinking-nuclear-south-korean-attitudes-nuclear-weapons
[data_cow_interstate_war_v4]: https://correlatesofwar.org/data-sets/cow-war/
[data_cow_interstate_wars_codebook]: https://correlatesofwar.org/wp-content/uploads/Inter-StateWars_Codebook.pdf
[data_cow_nmc_v7]: https://correlatesofwar.org/data-sets/national-material-capabilities/
[data_imf_cofer]: https://data.imf.org/en/datasets/IMF.STA:COFER
[data_iseas_2026_state_of_southeast_asia]: https://www.iseas.edu.sg/wp-content/uploads/2026/03/The-State-of-Southeast-Asia-2026-Survey-Final-Single.pdf
[data_kinu_2023_unification_survey]: https://repo.kinu.or.kr/handle/2015.oak/14362
[data_lowy_2025_asia_power_index]: https://power.lowyinstitute.org/
[data_sipri_2026_milex]: https://doi.org/10.55163/ZLHQ1057
[data_treasury_tic_2026]: https://ticdata.treasury.gov/resource-center/data-chart-center/tic/Documents/slt_table5.html
[government_crs_2026_extended_deterrence]: https://www.everycrsreport.com/reports/IF12735.html
[government_japan_2022_nss]: https://www.cas.go.jp/jp/siryou/221216anzenhoshou/nss-e.pdf
[government_japan_2025_plutonium]: https://www.aec.go.jp/bunya/04/plutonium/20250805_e.pdf
[government_japan_2026_defense_budget]: https://www.mod.go.jp/en/d_act/d_budget/pdf/fy2026_20251226a.pdf
[government_lma_2026_jwc_listed_areas]: https://lmalloyds.com/specialist-areas/underwriting/listed-areas/
[government_nic_2021_global_trends]: https://www.dni.gov/index.php/gt2040-home
[journal_anders_2020_surplus_domestic_product]: https://doi.org/10.1093/isq/sqaa013
[journal_anderson_press_2025_access_denied]: https://doi.org/10.1162/isec.a.7
[journal_arslanalp_2022_stealth_erosion]: https://doi.org/10.1016/j.jinteco.2022.103656
[journal_beckley_2015_entangling_alliances]: https://doi.org/10.1162/isec_a_00197
[journal_beckley_2018_power_of_nations]: https://doi.org/10.1162/isec_a_00328
[journal_bell_miller_2015_questioning]: https://doi.org/10.1177/0022002713499718
[journal_bianchi_sosa_padilla_2025_sanctions_dollar]: https://doi.org/10.1093/ej/ueaf052
[journal_bleek_lorber_2014_security_guarantees]: https://doi.org/10.1177/0022002713509050
[journal_brooks_wohlforth_2016_rise_and_fall]: https://doi.org/10.1162/ISEC_a_00225
[journal_carroll_kenkel_2019_prediction_proxies]: https://doi.org/10.1111/ajps.12442
[journal_caverley_2025]: https://doi.org/10.1353/tns.00004
[journal_chadefaux_2011_bargaining]: https://doi.org/10.1017/s175297191100008x
[journal_chang_2016_developing_expert_judgment]: https://doi.org/10.1017/s1930297500004599
[journal_chitu_2014_bond_markets]: https://doi.org/10.1016/j.jdeveco.2013.09.008
[journal_cirillo_taleb_2016_tail_risk]: https://doi.org/10.1016/j.physa.2016.01.050
[journal_clauset_2018_trends_fluctuations]: https://doi.org/10.1126/sciadv.aao3580
[journal_davis_weinstein_2002_bones_bombs]: https://doi.org/10.1257/000282802762024502
[journal_dicicco_levy_1999_power_shifts]: https://doi.org/10.1177/0022002799043006001
[journal_doran_parsons_1980_war_cycle]: https://doi.org/10.2307/1954315
[journal_farrell_newman_2019_weaponized]: https://doi.org/10.1162/isec_a_00351
[journal_fearon_1995_rationalist]: https://doi.org/10.1017/s0020818300033324
[journal_fuhrmann_tkach_2015_nuclear_latency]: https://doi.org/10.1177/0738894214559672
[journal_gavin_2010_same_as_it_ever_was]: https://doi.org/10.1162/isec.2010.34.3.7
[journal_gerzhoy_2015_alliance_coercion]: https://doi.org/10.1162/isec_a_00198
[journal_gilpin_1988_hegemonic_war]: https://doi.org/10.2307/204816
[journal_gopinath_stein_2021_dominant_currency]: https://doi.org/10.1093/qje/qjaa036
[journal_green_talmadge_2022]: https://doi.org/10.1162/isec_a_00437
[journal_henry_2020_what_allies_want]: https://doi.org/10.1162/isec_a_00375
[journal_ikenberry_2024_three_worlds]: https://doi.org/10.1093/ia/iiad284
[journal_levy_1987_declining_power]: https://doi.org/10.2307/2010195
[journal_lind_2024_back_to_bipolarity]: https://doi.org/10.1162/isec_a_00494
[journal_mearsheimer_2019_bound_to_fail]: https://doi.org/10.1162/isec_a_00342
[journal_menon_2026_new_world_order]: https://doi.org/10.1353/tns.00024
[journal_monteiro_debs_2014_strategic_logic]: https://doi.org/10.1162/isec_a_00177
[journal_nemeth_2026_suez_moment]: https://doi.org/10.1353/tns.00025
[journal_organski_kugler_1977_phoenix]: https://doi.org/10.2307/1961484
[journal_powell_2006_commitment_problem]: https://doi.org/10.1017/s0020818306060061
[journal_rauchhaus_2009_nuclear_peace]: https://doi.org/10.1177/0022002708330387
[journal_sechser_fuhrmann_2013_nuclear_blackmail]: https://doi.org/10.1017/s0020818312000392
[journal_snyder_1984_security_dilemma]: https://doi.org/10.2307/2010183
[journal_verschuur_2025_chokepoints]: https://doi.org/10.1038/s41467-025-65403-w
[journal_von_hippel_2019_naval_propulsion]: https://doi.org/10.1080/25751654.2019.1625504
[journal_walt_2025_hedging_hegemony]: https://doi.org/10.1162/isec_a_00508
[related_post_published_wargames]: {% post_url 2026-08-11-published_wargames_of_war_with_china %}
[related_post_rebuilding]: {% post_url 2026-08-12-rebuilding_after_war_with_china %}
[research_atlantic_council_2025_welcome_2035]: https://www.atlanticcouncil.org/content-series/atlantic-council-strategy-paper-series/welcome-to-2035/
[research_atlantic_council_2026_welcome_2036]: https://www.atlanticcouncil.org/content-series/atlantic-council-strategy-paper-series/welcome-to-2036/
[research_cancian_2023_first_battle]: https://www.csis.org/analysis/first-battle-next-war-wargaming-chinese-invasion-taiwan
[research_dooley_2022_sanctions_reinforce]: https://doi.org/10.3386/w29943
[research_ecfr_2023_a_la_carte]: https://ecfr.eu/publication/living-in-an-a-la-carte-world-what-european-policymakers-should-learn-from-global-public-opinion/
[research_evans_2023_alternative_futures_v2]: https://www.rand.org/pubs/research_reports/RRA591-2.html
[research_goes_bekkers_2022_geopolitical_conflicts]: https://www.wto.org/english/res_e/reser_e/ersd202209_e.pdf
[research_gompert_2016_war_with_china]: https://doi.org/10.7249/RR1140
[research_kwende_nephew_2025_cofer]: https://doi.org/10.5089/9798229004855.005
[research_nordhaus_2002_iraq_cost]: https://doi.org/10.3386/w9361
[research_priebe_2023_alternative_futures_v1]: https://www.rand.org/pubs/research_reports/RRA591-1.html
[research_priebe_frederick_2023_conversation]: https://www.rand.org/pubs/commentary/2023/05/alternative-futures-following-a-great-power-war-miranda.html
[research_rhodium_2022_taiwan_disruptions]: https://rhg.com/research/taiwan-economic-disruptions/
[research_tarapore_2024_deterring_attack]: https://www.aspi.org.au/report/deterring-attack-taiwan-policy-options-india-and-other-non-belligerent-states/
[research_vest_kratz_2023_sanctioning_china]: https://www.atlanticcouncil.org/in-depth-research-reports/report/sanctioning-china-in-a-taiwan-crisis-scenarios-and-risks/
[research_weiss_2025_dedollarization]: https://doi.org/10.17016/IFDP.2025.1420
