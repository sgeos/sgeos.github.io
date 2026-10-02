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
The second means that the belligerents would be
unusually concentrated for a war but far less so than in either world war,
and that concentration turns out to predict how belligerents fare afterwards.

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
which the subsection on breaks takes up below.

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
because the instruments disagree about the present ordering,
and the disagreement is categorical rather than marginal.

**Military expenditure puts the United States far ahead.**
The [Stockholm International Peace Research Institute's database][data_sipri_milex_database],
whose published definitions count armed forces, defence ministries,
paramilitaries judged trained for military operations and military aid
to the donor rather than the recipient,
is the standard series.
Its [2026 fact sheet][data_sipri_2026_milex] puts world spending at 2,887 billion current dollars
in 2025, the United States at 954 billion and 33 percent of the world total,
and China at an estimated 336 billion and 12 percent.

$$
\frac{954}{336} \approx 2.84
$$

**Output puts the answer either way, depending on the price basis.**
[World Bank indicators][data_world_bank_wdi] for 2025
give Chinese gross domestic product as about 63 percent of the American figure
at market exchange rates and about 134 percent at purchasing power parity.

$$
\frac{1.34}{0.63} \approx 2.1
$$

That factor of roughly two is a single number,
the ratio of China's purchasing power parity conversion factor
to its market exchange rate,
and it alone decides whether a transition has occurred on this measure.
Purchasing power parity is a consumption deflator.
It is roughly the right conversion for conscript pay and domestically produced steel
and roughly the wrong one for imported machine tools and semiconductors,
which is why no single answer is available
and why the [Lowy Institute][data_lowy_2025_asia_power_index]
uses purchasing power parity for economic weight
and both bases for military spending.

**Composite indices built around outcomes narrow the Chinese lead or reverse it.**
Lowy scores comprehensive power at 80.4 for the United States against 73.7 for China,
and its defence networks measure, which counts alliances,
scores 81.4 against 18.9.

$$
\frac{81.4}{18.9} \approx 4.3
$$

Expressed throughout as Chinese standing relative to American,
the five instruments give the following.

$$
1.89, \qquad
\frac{336}{954} \approx 0.35, \qquad
1.34, \qquad
0.63, \qquad
\frac{73.7}{80.4} \approx 0.92
$$

**Five instruments, five answers, spanning from
China at nearly twice the United States to China at about a third of it.**

$$
\frac{1.89}{0.35} \approx 5.4
$$

The extreme readings differ by a factor of more than five.
**The instrument producing the most dramatic Chinese lead
is the one this article uses**,
which is a reason to distrust the levels it reports
and the reason every comparison in this article is built
on ratios and on direction rather than on levels.
The index publishes its weights and its own caveat
that "it is of course possible to reach other value judgements
about the relative importance of the measures",
which is a candour the composite literature does not always show.

### The case against gross indicators, which is the strongest objection here

The general objection is that gross measures count what a state has
rather than what it can bring to bear after paying for itself.
[Beckley][journal_beckley_2018_power_of_nations] states it directly,
arguing that standard indicators
"exaggerate the wealth and military power of poor, populous countries,
such as China and India",
and that a net measure predicts dispute and war outcomes better
over two centuries of great-power cases.
His [earlier article][journal_beckley_2012_chinas_century]
applies the same argument to the present pair,
and his [work on development and military effectiveness][journal_beckley_2010_economic_development]
supplies the micro-foundation,
which is that wealthier societies convert resources into fighting power more efficiently.

[Anders, Fariss and Markowitz][journal_anders_2020_surplus_domestic_product]
make the same move for output rather than for capability,
separating the subsistence income a state must spend on its population
from the surplus it could allocate to arms,
and reporting that the resulting measure
"outperforms GDP at measuring the distribution of power resources".
**Both critiques point the same way,
which is that this article's headline index overstates China.**
That is the conservative direction for an argument
that a war would not change relative standing much,
so the index is reported as published rather than adjusted.

The sharpest objection is not about what the index counts
but about whether it works.
[Carroll and Kenkel][journal_carroll_kenkel_2019_prediction_proxies]
report that the capability ratio
"is barely better than random guessing at predicting militarized dispute outcomes",
and build a replacement from the same underlying components
that is "an order of magnitude better".
**The defect is therefore in the aggregation rule and not in the measurements**,
which is consistent with the decomposition performed above,
where the index's verdict turned out to rest on two components out of six.

Other critiques are older and narrower.
[Brooks and Wohlforth][journal_brooks_wohlforth_2016_rise_and_fall]
add that the conversion from economic weight into military power
has itself become harder,
so that "the transition from a great power to a superpower
is much harder now than it was in the past",
which bears directly on reading an industrial-age index forward.
[Markowitz and Fariss][journal_markowitz_fariss_2013_going_the_distance]
observe that capability counted at home is not capability projected abroad
and propose a distance adjustment.
[Kadera and Sorokin][journal_kadera_sorokin_2004_measuring_national_power]
examine what an index of this family can and cannot represent.
[Tellis and others][research_tellis_2000_measuring_national_power],
writing for a defence sponsor rather than a journal,
built an alternative framework for the postindustrial case
on the ground that material aggregates had stopped tracking usable power.
And [Höhn's survey][research_hohn_2014_geopolitics_measurement],
which catalogues the field,
records the plain reason this index persists,
namely that it "is the most used power index,
not because it is superior in quality,
but because it is supported by a huge dataset".

**That sentence is the honest summary of why this article uses it too.**
The alternative instruments are better in various ways and none of them
runs from 1816 to 2022 for every state in the system,
which is what a base rate across ninety-five wars requires.

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
as the decomposition at the start of this article established,
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

This reframes the earlier null result for these two cases.
**The world wars cannot test the bystander hypothesis at all**,
because they left no bystanders worth the name.
Other wars can test it, many of them do have large non-participant pools,
and what those cases show is taken up next.
It is not what the hypothesis predicts.

### Where the present case would sit

The prospective case can be placed on the same scale.
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
Expressed against the two world wars,
the prospective belligerent share is a little over a third
of the 1939 figure and a little over two fifths of the 1914 figure.

$$
\frac{0.3552}{0.8229} \approx 0.43,
\qquad
\frac{0.3552}{0.9808} \approx 0.36
$$

**The tempting next sentence is that a majority staying out
has never happened in a great-power war, and it is false.**
The same data that produced everything else here
return twenty wars with at least twenty thousand battle deaths
in which the belligerents held a smaller share than 0.3552,
among them the Russo-Japanese War at 0.1424,
the Second Russo-Turkish at 0.1392 and the Gulf War at 0.2741.
Small belligerent shares are ordinary.
What is unusual about this case is the opposite of what that sentence claims,
and stating it correctly turns out to be more useful.

$$
\frac{73}{76} \approx 0.96
$$

**Of the seventy-six wars where the comparison can be made,
seventy-three had less concentrated belligerents than this one would have,
putting the prospective case at about the ninety-sixth percentile.**
It is unusually concentrated for a war
and far less concentrated than either world war.

### What belligerent concentration predicts, which is not what was expected

Having built the measure, the obvious question is whether it predicts anything,
and the answer is yes and in the opposite direction from the bystander hypothesis.

| Belligerents' combined share | Wars | Median change | Share that lost |
|------------------------------|------|---------------|-----------------|
| Under 0.2 | 61 | +0.082 | 38 percent |
| 0.2 to 0.4 | 12 | -0.052 | 83 percent |
| 0.4 to 0.6 | 1 | -0.068 | 100 percent |
| Over 0.6 | 2 | -0.031 | 100 percent |

$$
r = -0.225 \quad (n = 76)
$$

**The more of the world's capability the belligerents hold,
the worse they do afterwards.**
When they hold under a fifth of it they more often gain,
with a median of plus eight percent and only thirty-eight percent declining.
The bottom three rows carry fifteen wars between them,
and the last two carry three,
so the monotonic appearance of the table is weaker than it looks
and the correlation is the quantity to trust.

The band the prospective case falls into is the second row,
and it is worth naming its members because twelve is a readable number.
They are the invasion of Afghanistan, the Russo-Finnish War,
the First Russo-Turkish, the second phase of the Laotian war,
the Sino-Russian war of 1900, Italian unification, the Roman Republic,
the Manchurian war, the Sino-French war, Kosovo,
the Gulf War and the Anglo-Persian war.
**Ten of those twelve ended with the belligerents holding less than they started with,
at a median of minus five percent.**

That is a real result and it is a modest one.
It points the same way as the headline conclusion,
which is that the belligerents in this war
would most likely come out of it slightly smaller relative to everyone else,
and it reaches that conclusion by a mechanism
different from the one asserted in the scenario literature.
**The mechanism is not that bystanders capture something.
It is that concentrated belligerents have more to lose.**

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

### The one historical case where a bystander demonstrably gained

The bystander argument has been structural so far.
There is one case in the record where the mechanism is documented
in the contemporaneous official correspondence
rather than reconstructed from an index,
and it involves the same two principals.

Japan did not fight in Korea.
It supplied the war.
The [State Department's own record][government_frus_1952_japan_procurement]
shows American officials worrying in 1953
about Japanese dependence on that trade,
noting the Japanese fear of
"a drastic decline in United States special procurement following a Korean armistice"
at a time when Japan had failed "to regain more than 30 percent
of its prewar export volume".
A [companion document][government_frus_1952_japan_dollar_earnings]
is blunter still about the dependence it had created,
describing a government "wasteful of its substance
and confident that the United States will bail it out
through special procurement, Korean rehabilitation, or new loans".

**That is a bystander gaining materially from a war it did not join,
recorded by the belligerent that was paying for it, as it happened.**
It is also the case this article's own base rate assigns
the largest stalemate effect to,
with the American share falling 13 percent over the following decade
while the Chinese share rose 18.

The documents do not settle the size of the effect,
and no verified dollar series for the procurement programme
was obtained for this article,
so what they establish is the mechanism and not its magnitude.
**That distinction is the honest one and it is the pattern throughout this subject.**

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
at this level of belligerent concentration.
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

### The research programme behind the claim, and its own assessment of itself

The position just stated is not one author's.
It belongs to a programme with a documented internal history,
and the history matters because the programme has revised itself
in ways that bear on this article's question.

[Organski and Kugler's *War Ledger*][book_organski_kugler_1980_war_ledger]
is the founding empirical statement,
and the phoenix-factor chapter quoted above is its third.
[Kugler and Arbetman][journal_kugler_arbetman_1989_phoenix]
later tested a mechanism for that recovery,
asking whether the destruction of political structures
accelerates it as a collective-goods argument would predict,
and concluded "somewhat reluctantly"
that the proposed explanation does not account for
"the well-established difference in the postwar recovery among victors and vanquished".
**The recovery asymmetry survived its own best explanation being refuted**,
which is a reason to treat the finding as robust
and the mechanism as open.

[Lemke][book_lemke_2002_regions_of_war_and_peace]
extended the theory downward to regional hierarchies,
finding that parity and dissatisfaction correlate with war
across regions but with cross-regional variation.
[Tammen, Kugler and Lemke][reference_tammen_2017_foundations]
restate the programme's current form,
describing it as "a dynamic and structural model
for analyzing fundamental shifts in global power".
[Copeland's dynamic differentials theory][book_copeland_2018_origins_of_major_war]
sharpens the initiation question,
locating war in a declining state's anticipation of further decline,
which is a theory of why the war starts
and not of what the distribution looks like afterwards.

The main rival inside the family is power cycle theory.
[Doran and Parsons][journal_doran_parsons_1980_war_cycle]
locate war at inflection points on an already-traced capability curve
across nine major powers from 1816 to 1975,
and [Doran's later statement][journal_doran_1989_systemic_disequilibrium]
applies it to the disequilibrium of 1885 to 1914.
**It is operationalised on near-identical inputs to the index this article uses,
so it inherits every measurement problem documented above.**

[DiCicco and Levy][journal_dicicco_levy_1999_power_shifts]
assess the programme from inside it
and find the record mixed,
with some developments progressive
and "other areas of the research program exhibit signs of degeneration",
naming the timing and initiation of wars
and the causal mechanisms driving them.
That is an unusually candid self-assessment
and it is the reason this article treats the theory as a prior
rather than as a settled result.

### The popular version of the argument, and why it is not used here

The claim that a rising power and a ruling power tend toward war
reaches most readers through Graham Allison's Thucydides Trap,
whose [original statement][commentary_allison_2015_thucydides_trap]
reports that "in 12 of 16 cases over the past 500 years, the result was war"
and concludes that "war is more likely than not".

$$
\frac{12}{16} = 0.75
$$

**That framework is not used in this article, and the reasons are worth stating
because the dataset behind it is the sort of thing this article otherwise likes.**

The objections are specific and they come from several directions.
[Platias and Trigkas][journal_platias_trigkas_2021_unravelling]
write that "no other text in the intellectual history of International Relations
has become as frequent a victim of confirmation bias and selective presentism".
[Kang and Ma][journal_kang_ma_2018_power_transitions]
observe that the East Asian historical record does not fit the pattern,
which matters for a framework applied to East Asia.
[Fitzpatrick][journal_fitzpatrick_2025_farewell]
traces the Anglo-German case in the dataset
back through Kennedy to a historiography that has since moved,
arguing that "improving the quality of contemporary international relations
might well rely upon improving our communication of paradigm changes
in German historiography".
[Welch][journal_welch_2003_stop_reading_thucydides]
made the general case two decades earlier,
that Thucydides's influence on the field "is largely pernicious".
[Morley][journal_morley_2026_thucydiocies],
writing as a classicist,
notes that Thucydides "does not say that war was inevitable".

The methodological objection is the one that bears on this article directly.
[Kitchen and Cox][journal_kitchen_cox_2019_structural_power],
reviewing the decline debate,
quote Beckley's complaint that
"most studies do not look at a comprehensive set of indicators"
and instead paint "impressionistic pictures of the balance of power,
presenting titbits of information on a handful of metrics",
and Huntington's older one that declinist writings
"do not elaborate testable propositions
involving independent and dependent variables".

**Both complaints apply to the sixteen-case framework and neither applies to a base rate
computed from a published dataset with its coding rules in print.**
That is the reason this article computed one.
It is also a reason to hold this article's own result to the same standard,
which is what the measurement sections above were for.

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

### What the theory says a currency transition requires

The inertia argument has a formal basis worth stating,
because it determines whether a shock of war magnitude could move the position at all.
[Gopinath and Stein][journal_gopinath_stein_2021_dominant_currency]
show that a currency's role in invoicing
and its role as a safe store of value reinforce one another,
so that "a single dominant currency in trade invoicing and global banking"
can emerge even among similar candidates,
with firms in emerging markets borrowing in it
and the dominant currency earning a lower return in consequence.
The [dominant currency paradigm][journal_gopinath_2020_dominant_currency_paradigm]
supplies the trade-side evidence,
and [Boz and others][journal_boz_2022_invoicing_patterns]
the invoicing data behind it.

**Complementarity cuts both ways and the literature says so.**
If the roles reinforce one another on the way up
they can unwind together on the way down,
which is why [Eichengreen][research_eichengreen_2005_sterlings_past]
argued twenty years ago that reserve-currency competition
is not a winner-take-all game
and that several currencies have shared the role before.
[Eichengreen, Chiţu and Mehl][journal_eichengreen_2015_stability_or_upheaval]
develop the long-run series,
and [their later work][journal_eichengreen_2019_mars_or_mercury]
finds that geopolitical alignment, not only economics,
predicts which currency a state's reserve manager holds,
which is the mechanism a war would operate through.

The sterling precedent is the empirical anchor.
[Eichengreen and Flandreau][journal_eichengreen_flandreau_2009_rise_and_fall]
date the dollar's overtaking to the mid-1920s rather than to 1945,
concluding that "the network effects thought to lend inertia
to international currency status
and to create incumbency advantages for the dominant international currency
do not apply in the reserve currency domain".
**That is a direct denial of the premise
on which the dollar is usually assumed to be unmovable.**
[Ilzetzki, Reinhart and Rogoff][journal_ilzetzki_2020_euro_punching]
ask the complementary question about the euro,
and why a currency area of comparable size
has not taken the share its economy would suggest.

The book-length treatments split the same way.
[Prasad][book_prasad_2015_dollar_trap]
argues the dollar's position is reinforced by the very crises
that are supposed to threaten it,
and [McDowell][book_mcdowell_2023_bucking_the_buck]
examines the backlash that financial sanctions have provoked.

### What losing the position would actually cost

Most commentary asserts that losing reserve status would be serious
without saying how serious.
[Jiang, Krishnamurthy, Lustig and Richmond][research_jiang_2026_dollar_erosion]
quantify it, estimating that the loss of seigniorage
runs at about one percent of gross domestic product a year,
that clearing the resulting excess supply of American goods
requires a real depreciation of about 8.8 percent,
and that roughly half of gross domestic product in dollar bonds
would have to be reabsorbed by domestic investors,
raising the real interest rate by about 90 basis points
for "an aggregate wealth loss of roughly one year of U.S. GDP".

$$
0.01 \;\text{per year}, \qquad 8.8 \;\text{percent}, \qquad 90 \;\text{basis points}
$$

**One year of output is a large number and it is not a catastrophic one**,
being roughly the scale this article's base rate assigns
to losing a large war on the capability measure.
That the two converge from completely different directions
is worth recording without making more of it than a coincidence of magnitude.

[Weiss's earlier paper][research_weiss_2022_geopolitics_dollar]
reaches the structural version of the same conclusion,
noting that around three quarters of foreign government holdings
of safe American assets are held by states with some military tie to the United States,
so that the reserve position and the alliance system are not independent variables.
**A war that damaged the alliance system
would therefore act on the currency through the same channel**,
which is the strongest available argument
that the financial and military questions are one question.
[Bianchi and Sosa-Padilla's working paper][research_bianchi_2023_sanctions_dollar]
models the anticipation effect that would run ahead of any such event.

### War finance, where the constraint is older than the scenario

How a war is paid for shapes what it does to the victor,
and the American record is documented.
The [Congressional Research Service's series][government_crs_costs_of_major_wars]
puts the Second World War at 35.8 percent of gross domestic product at its 1945 peak
and the Korean War at 4.2 percent at its 1952 peak,
while stating plainly that its estimates
"do not reflect costs of veterans' benefits, interest on war-related debt,
or assistance to allies"
and should be treated "not as truly comparable figures on a continuum,
but as snapshots of vastly different periods of U.S. history".

[Ohanian][journal_ohanian_1997_macroeconomic_effects_war_finance]
compares the two directly,
finding the Second World War financed primarily by debt
and Korea almost exclusively by taxation,
and that applying the Korean policy to the Second World War
"would have resulted in much lower output and welfare relative to the actual policy".
[Hall and Sargent][journal_hall_sargent_2011_interest_rate_risk]
decompose the postwar debt dynamics
and note that their estimates "differ conceptually and quantitatively
from the interest payments reported by the US government",
and [their later paper][research_hall_sargent_2020_debt_and_taxes]
extends the accounting across eight wars from 1812.

**The mechanism that actually retired the Second World War debt
was not growth and not taxation.**
[Reinhart and Sbrancia][research_reinhart_sbrancia_2011_liquidation]
document financial repression,
reporting that for the United States and the United Kingdom
"the annual liquidation of debt via negative real interest rates
amounted on average from 3 to 4 percent of GDP a year"
across 1945 to 1980.
That rate is directly comparable to the projected net interest burden quoted above,
and it is the reason a debt-service constraint
is not the same as an inability to fight.
[Rockoff's][book_rockoff_2012_americas_economic_way_of_war]
history covers the longer arc,
and [his study of the First World War][research_rockoff_2004_until_its_over]
documents the balance-sheet consequence that matters most here,
which is that the United States moved from net debtor to net creditor
between 1914 and 1919 while the fighting was in Europe.

[Crawford's accounting][research_crawford_2021_budgetary_costs]
of the post-2001 wars reaches about 8 trillion dollars
in budgetary costs and future obligations,
of which interest on borrowing is over a trillion,
which is the modern illustration of the item
the older congressional series excludes by construction.
[Edwards][research_edwards_2010_war_costs]
makes the general point,
that one third to one half of the present value of historical war costs
arrives as veterans' benefits distributed over decades,
with a half-life above thirty years after hostilities end.

**None of that appears in any capability index**,
and none of it appears in the scenario literature either.

### The fiscal position, from the issuing authority

The debt figures used above come from the Treasury's own publication.
[Debt to the Penny][data_treasury_debt_to_the_penny]
gives total public debt outstanding and the portion held by the public,
and the [Bank for International Settlements credit series][data_bis_total_credit]
gives the internationally comparable version
for both states on a consistent definition.

**The comparison between the two states is where the definitions bite.**
On the Bank's general-government measure,
the Chinese and American positions are closer than the headline Chinese figure suggests,
while the [International Monetary Fund's augmented measure][government_imf_2026_china_article_iv],
which expands the perimeter "to include government-guided funds
and the activity of local government financing vehicles",
is substantially higher.
**That measure is formally contested inside the same document**,
whose statement by the member state's executive director
records that they "hold different views on the characterization
of the fiscal expansion as modest,
as well as issues related to the concept of augmented debt".
Three perimeters are in circulation and they differ by definition rather than by vintage,
so any sentence of the form that Chinese debt is a particular share of output
is wrong unless it names the perimeter.

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

### What the theory of proliferation decisions actually holds

The cascade claim assumes a model of why states build weapons,
and the field offers three that do not agree.
[Sagan's][journal_sagan_1997_why_states_build]
canonical statement sets out security, domestic politics and norms
as rival accounts of the same decision.
[Hymans][book_hymans_2006_psychology_of_proliferation]
locates it instead in the identity conceptions of individual leaders,
which predicts that the decision is rarer and less responsive to circumstance
than a security model implies.
[Narang][journal_narang_2017_strategies_of_proliferation]
shifts the question from whether to how,
distinguishing hedging, sprinting, hiding and sheltered pursuit,
and observing that a state's choice among them
changes what an observer would see.

**Those three disagree about what a visible alliance failure would do**,
and the article records that rather than choosing.
On a security model it is close to sufficient.
On an identity model it is close to irrelevant.
On a strategies model it changes the route and not the destination.

[Mehta and Whitlark][journal_mehta_whitlark_2017_latency]
take up the state in between,
asking what latency buys a state that does not cross the threshold,
and [Lanoszka][book_lanoszka_2018_atomic_assurance]
argues that economic and technological dependence
restrains allies more reliably than assurance does,
which is a third mechanism distinct from both
[Bleek and Lorber's][journal_bleek_lorber_2014_security_guarantees] guarantees
and [Gerzhoy's][journal_gerzhoy_2015_alliance_coercion] threats of abandonment.

### The instruments the alliance system has actually built

The reassurance architecture is documentary and can be read rather than characterised.
The [Washington Declaration][government_us_2023_washington_declaration]
records the bargain in its own words,
that the Republic of Korea "has full confidence in U.S. extended deterrence commitments"
and reaffirms "its longstanding commitment to its obligations
under the Nuclear Nonproliferation Treaty",
in exchange for a United States commitment
"to make every effort to consult with the ROK
on any possible nuclear weapons employment on the Korean Peninsula".

**The hedge in that sentence is the whole of the instrument.**
The commitment is to make every effort to consult,
not to obtain consent,
and the declaration bounds it by existing declaratory policy.
The [Nuclear Consultative Group fact sheet][government_dod_2025_ncg_fact_sheet]
describes the body created to carry it,
co-chaired at assistant secretary level and meeting twice a year at principal level.
That is the instrument whose announcement,
as the natural experiment above reports,
moved allied opinion on indigenous weapons by seven tenths of a percentage point.

The trilateral and quadrilateral arrangements are often read as consolidation.
Read in their own text they are narrower than that.
The [Spirit of Camp David][government_us_2023_camp_david]
commits the three governments "to consult with each other in an expeditious manner",
which is a consultation pledge and not a defence obligation,
and its Taiwan language goes no further than
"the importance of peace and stability across the Taiwan Strait".
The [Wilmington Declaration][government_us_2024_wilmington_declaration]
contains no mutual defence commitment and no extended deterrence language at all,
its substantive undertakings being public-health and infrastructure initiatives.
**A survey that models the Quad as a security alliance is modelling something
the document does not establish.**

On the other side, the [joint statement of February 2022][government_kremlin_2022_joint_statement]
records that the relationship between Russia and China
is "superior to political and military alliances of the Cold War era"
and that "friendship between the two States has no limits",
while also stating that it is "neither aimed against third countries"
nor alliance-like in obligation.
It is a declaration of alignment without a commitment clause,
which is the same shape as the documents on the other side
and is worth noting because the two are usually contrasted rather than compared.

### Taiwan's own programme, which is the closest historical case

The island at the centre of this contingency
pursued nuclear weapons itself and was stopped.
[Albright and Stricker's][research_albright_2018_taiwan_nuclear_program]
book-length account and the
[National Security Archive's document collection][research_nsarchive_2019_taiwans_bomb]
together establish the shape of it.
The programme ran from the late 1960s to 1988
under presidential direction,
and it ended through the defection of a senior insider to American intelligence
rather than through reassurance.

**That is the Gerzhoy mechanism in the case closest to hand.**
A threatened ally pursued weapons while formally protected,
and what stopped it was patron coercion and intelligence penetration.
It is also the reason a cascade argument cannot treat Taiwan as a passive object,
though what Taiwan would do in the scenarios this series covers
is outside what any located source addresses.

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
[Henry's book-length treatment][book_henry_2022_reliability]
develops the argument at length,
and [Tomz and Weeks][journal_tomz_weeks_2021_military_alliances]
supply the variable underneath it,
which is whether publics support honouring a commitment at all.

**So a war fought to prove a commitment
could reduce allied confidence by proving it too well**,
and that is a possibility no scenario in the surveyed literature models.

## A Survey of the Contemporary Literature

The sections above used the literature to argue.
This one reports it, including the parts that cut against the argument.
The organising principle is by dispute rather than by topic,
because on almost every question that matters here
the literature contains two defensible positions
and the article's contribution is to say which evidence separates them.

### Measuring national power, where the instruments disagree categorically

The measurement dispute is set out with its figures in
the opening sections of this article and is not repeated here.
What belongs in a survey is the shape of the literature.

**There is no agreed instrument and the field says so.**
The index this article uses descends from
[Singer, Bremer and Stuckey][book_singer_1972_capability_distribution]
and persists, on [Höhn's][research_hohn_2014_geopolitics_measurement] account,
for reasons of coverage rather than quality.
The critiques divide into three kinds.
[Carroll and Kenkel][journal_carroll_kenkel_2019_prediction_proxies]
attack the aggregation rule and show a replacement built from the same data
predicts dispute outcomes an order of magnitude better.
[Beckley][journal_beckley_2018_power_of_nations] and
[Anders, Fariss and Markowitz][journal_anders_2020_surplus_domestic_product]
attack the gross-against-net confusion,
in capability and in output respectively.
[Markowitz and Fariss][journal_markowitz_fariss_2013_going_the_distance]
and [Brooks and Wohlforth][journal_brooks_wohlforth_2016_rise_and_fall]
attack the conversion assumption,
the first on distance and the second on the growing difficulty
of turning economic weight into military power.
[Kadera and Sorokin][journal_kadera_sorokin_2004_measuring_national_power]
and [Tellis and others][research_tellis_2000_measuring_national_power]
propose alternative frameworks outright.

**Every one of those critiques points the same way**,
which is that the headline index overstates China relative to the United States.
The article reports the index anyway,
because overstating the challenger is the conservative direction
for an argument that a war would not change relative standing much.

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

### What the official assessments say about the balance itself

The force-balance claims underneath the scenario literature
come from a small number of official publications,
and they are more cautious than the commentary built on them.
The [Department of Defense annual report to Congress][government_dod_2025_china_report],
used in the [previous article][related_post_rebuilding] for its naval tables,
counts ships by class and prints no aggregate,
which is the posture of a document that knows a total
would be quoted beyond what its counting rules support.

The alliance picture comes from the same kind of source.
The [Congressional Research Service][government_crs_2026_extended_deterrence]
records that the 2026 National Defense Strategy
does not explicitly mention extended deterrence,
and a [companion product][government_crs_2025_national_defense_strategy]
sets out what reprioritisation toward the Western Hemisphere and the Indo-Pacific
would mean for forces in Europe and the Middle East.
The [NATO analysis][government_crs_2026_nato_summit]
records the division of labour being proposed,
in which the United States continues to provide the nuclear guarantee
while allies "assume primary responsibility for the conventional defense of Europe".
The [Japan assessment][government_crs_2026_japan_defense]
records a government nearly doubling defence spending between 2023 and 2028,
and the [Philippines report][government_crs_2026_philippines]
records the basing arithmetic,
noting that the northernmost site opened to American forces
sits about 500 kilometres from southern Taiwan.

**None of those is a forecast and all of them are the baseline
against which a war's effect would have to be measured.**
The baseline is moving without a war,
which is the observation this article keeps arriving at from different directions.

The legal position of the territory itself is also primary and often paraphrased.
The [Taiwan Relations Act][government_us_1979_taiwan_relations_act]
is the instrument that creates the ambiguity every scenario turns on,
and it is worth noting that Taiwan is not covered
by an extended deterrence commitment of the kind
the Korean and Japanese documents above record.

### The shipping and energy record, which is measured rather than modelled

The blockade literature prices a disruption.
Two public datasets measure the traffic that would be disrupted.
The [International Monetary Fund's port and chokepoint data][data_imf_portwatch],
built from vessel transponder records,
publishes daily transit counts for twenty-eight chokepoints from 2019,
and [UNCTAD's seaborne trade series][data_unctad_seaborne_trade]
gives the world totals those transits should be set against.
**The two do not measure the same thing**,
since one counts tonnage crossing a boundary
and the other counts cargo once at loading,
and a single shipment can cross several chokepoints,
so the ratio between them is an order-of-magnitude check and nothing finer.

On the energy side the [Energy Information Administration's analyses][government_eia_2025_hormuz]
give the comparative scale for a chokepoint disruption,
reporting about 20 million barrels a day through the Strait of Hormuz in 2024,
around a fifth of global petroleum liquids consumption,
and [its assessment of strategic stocks][government_eia_2026_strategic_stocks]
reports Chinese government-held crude inventories
at about 360 million barrels in December 2025
against a United States Strategic Petroleum Reserve near 414 million.

$$
\frac{360}{414} \approx 0.87
$$

**Those two figures are close, and the comparison is only valid
because both are government-held stocks on the same basis.**
The wider Chinese figure that circulates, near 1.4 billion barrels,
folds in commercial and refinery stocks
in a treatment that source applies to China and to no other country,
which is the sort of asymmetry that produces a startling ratio
and does not survive being read.

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

### Hedging, where the concept has been narrowed by its own literature

That material used the word hedging loosely.
[Kuik][journal_kuik_2008_essence_of_hedging]
gave the concept its standard treatment through the Malaysian and Singaporean cases,
and [Lim and Cooper][journal_lim_cooper_2015_reassessing_hedging]
then narrowed it sharply.
Their accepted manuscript argues that hedging behaviour
"should not include costless activities
that do not require states to face tradeoffs in their security choices",
and that once redefined as signalling that generates ambiguity
about a secondary state's shared security interests,
hedging "occurs in far narrower" circumstances than is widely believed.

**On the narrow definition, most of what the survey data above measure is not hedging.**
Expressing a preference to a pollster is costless.
That is a reason to read the ISEAS oscillation
as information about sentiment rather than about alignment,
and it strengthens the reading already given
that three reversals within sampling error are noise around parity.

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

The works cited above as a group have an internal order worth setting out,
because the field moved from measuring capabilities to describing architecture
for reasons it stated at the time.

[Ikenberry's journal statement][journal_ikenberry_1999_institutions_restraint]
precedes the book and is the compact form of the argument,
that a victor's advantage is transient
and that institutions are how it is converted into something durable.
[After Victory][book_ikenberry_2019_after_victory] develops it through
the settlements of 1815, 1919 and 1945.
Two decades later [the same author][journal_ikenberry_2018_end_of_liberal_order]
asked whether the order was ending,
and concluded that the threat came from inside the West
rather than from the rising states the theory had expected.
[Lim and Ikenberry][journal_lim_ikenberry_2023_illiberal_hegemony]
then applied the framework prospectively to China,
restating the hegemonic-war mechanism in current prose,
that "in the wake of hegemonic war,
a newly powerful state rises up and seeks to rebuild international order".

[Ikenberry and Nexon][journal_ikenberry_nexon_2019_hegemony_studies]
survey where the subfield had arrived,
and [Cooley and Nexon's][book_cooley_nexon_2020_exit_from_hegemony]
book reverses the question from construction to unravelling.
Their [earlier article][journal_cooley_nexon_2013_empire_compensate]
is the empirical anchor for that,
examining the overseas basing network
and finding it "combines elements of liberal multilateralism
with neo-imperial hegemony",
which is the concrete form in which a hegemonic position is actually held
and therefore the thing a war would act upon.

[Lake][journal_lake_2007_escape_state_of_nature]
supplies the conceptual move the whole group depends on,
that it is "a fallacy to infer that all relationships
within this system are anarchic",
and that hierarchy is "a fragile relationship, easily abused"
precisely because it rests on the legitimacy subordinates confer.
His [book-length treatment][book_lake_2017_hierarchy]
develops the authority relation.

**If that is right, the quantity a war would damage
is not capability but the consent of subordinate states**,
which is unmeasured by every instrument in this article
and is the same gap the Suez case exposed.

The current positions in that literature divide on what follows.
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

### The historical case the Suez analogy rests on

The Suez argument above was stated without its source,
and the source is worth having because it is an institutional record
rather than a retrospective.
[Boughton's study][journal_boughton_2001_northwest_of_suez],
written from inside the International Monetary Fund,
documents that all four combatants sought and obtained assistance from the Fund,
and locates the British collapse precisely.

> For the United Kingdom, therefore, the need for assistance from the IMF
> resulted not from economics but from the psychological impact
> of a political crisis on financial markets.

**That sentence is the Suez mechanism in one line, and it is not a capability mechanism.**
A reserve drain driven by market sentiment
forced a policy reversal that no material loss would have compelled,
which is exactly the channel a capability index cannot see
and exactly the channel the alliance literature above describes.

### The longer record of victors who declined

[Kennedy's][book_kennedy_1987_rise_and_fall]
survey is the standard account,
and its central claim is about sequence rather than about war.

> The fact remains that all of the major shifts
> in the world's military-power balances have followed alterations
> in the productive balances.

His reproduction of the manufacturing-share tables
makes the British case concrete,
with Britain falling from 13.6 percent of world manufacturing output in 1913
to 9.9 percent in 1928 while on the winning side,
and the United States rising from 32.0 to 39.3 across the same war.

$$
13.6 \longrightarrow 9.9,
\qquad
32.0 \longrightarrow 39.3
$$

Kennedy also supplies the term the decline literature argues over,
warning that decision-makers face
"the awkward and enduring fact that the sum total
of the United States' global interests and obligations
is nowadays far larger than the country's power to defend them all simultaneously".
**The forecast attached to that argument did not hold on this article's own measure.**
American capability share rose for roughly two decades after he published,
which is a documented instance of a careful, quantitative,
book-length structural prediction failing inside a decade,
and it belongs with the prediction-accuracy material above
rather than being quietly omitted from it.

[Harrison's][research_harrison_1998_economics_of_wwii]
wartime accounts give the complementary measure
for the one case where a war did move the distribution decisively,
with American output roughly doubling between 1938 and 1944
while the Axis total fell.
The underlying long-run series come from
[the Maddison Project][data_maddison_project_2023],
whose [methodology paper][journal_bolt_vanzanden_2024_maddison]
documents the construction,
and the measurement uncertainty in those series is itself substantial,
which [Fariss and others][research_fariss_2017_latent_estimation]
address by building a model that reconciles
the competing historical output estimates rather than choosing among them.

[Schroeder][journal_schroeder_1992_vienna_settlement]
supplies the historian's objection to the whole framing,
asking whether the settlement of 1815
rested on a balance of power at all,
which is a reminder that the quantity this article measures
is a modern analytical construct
and not a category the participants in these wars would have recognised.

### Relative gain by abstention, where the theory is formal

The bystander argument has a formal literature behind it
that the scenario sources do not cite.
[Christensen and Snyder][journal_christensen_snyder_1990_chain_gangs]
set out buck-passing and chain-ganging
as the two errors multipolarity invites,
with the choice between them turning on perceived offensive advantage.
That is the mechanism by which a state stays out of a war it could join,
and it is the precondition for any bystander gain.

Whether states pursue relative position at all is a separate dispute.
[Grieco][journal_grieco_1988_anarchy_limits]
argued that states are positional and therefore resist cooperation
that benefits others more.
[Powell][journal_powell_1991_absolute_relative_gains]
and [Snidal][journal_snidal_1991_relative_gains]
answered formally,
showing that the concern for relative gains
depends on the constraints the states face
rather than being a fixed preference,
and the three positions are set out together
in [their joint exchange][journal_grieco_powell_snidal_1993_relative_gains].

**This matters for the bystander argument in a specific way.**
If relative position is what states pursue,
a non-participant gains from a war between two others
even if its own output falls,
and the trade modelling quoted above measures the wrong thing.
If states pursue absolute gains,
the trade modelling measures the right thing
and the capability arithmetic is the distraction.
**The article cannot settle that and reports the arithmetic on both.**

### Blockade, which is the form in which this question usually arrives

Several of the economic estimates above price a blockade rather than an invasion,
and the operational literature on that is older than the current debate.
[Mirski][journal_mirski_2013_stranglehold]
sets out the context, conduct and consequences of an American naval blockade of China,
and [Lanteigne][journal_lanteigne_2008_malacca_dilemma]
describes the dependence that makes it conceivable.
[Posen's][journal_posen_2003_command_of_the_commons]
account of command of the commons
is the structural statement of why the United States could attempt one at all.
[Collins][journal_collins_2018_maritime_oil_blockade]
gives the strongest published objection,
arguing that the political, economic and financial requirements of sustaining one
mean "even a militarily successful blockader
could find its political, economic, and diplomatic position untenable
well before a blockade could exert its full effects".
[Davis and Gholz][journal_davis_gholz_2026_blockade_by_fire]
take the question from the other side,
examining a Chinese blockade by missile attack on ports
and noting that "even militarily successful blockades
have rarely achieved all their political goals".

**That last clause is this article's subject in miniature**,
and it is the clearest statement in the surveyed literature
that military success and political outcome are separate variables.

[McKinney and Harris][journal_mckinney_harris_2021_broken_nest]
occupy the position furthest from the rest,
proposing deterrence through the threat of destroying what an invader would capture,
which is relevant here because it is the one published proposal
whose explicit object is the postwar economic distribution
rather than the fighting.

### The recent journal literature, which has turned to this contingency

The last three years have produced a body of work
aimed directly at the war this series is about,
and it is listed here because its existence bounds the claim
that the subject is neglected.
[Cunningham and Ven Bruusgaard][journal_cunningham_2026_escalate_to_survive]
examine nuclear first use in contemporary great-power conflict.
[Evangelista][journal_evangelista_2024_nuclear_umbrella]
takes up extended deterrence precedents for a postwar settlement,
which is the closest located treatment of a postwar security guarantee.
[Greitens and Kardon][journal_greitens_kardon_2025_security_without_exclusivity]
describe hybrid alignment under competition,
which is the formal version of the hedging the survey data show.
[Trachtenberg][journal_trachtenberg_2025_rules_based_order]
examines the rules-based order historically.
[Priebe and others][journal_priebe_2024_competing_visions]
set out the restraint positions,
and [Cancian][journal_cancian_2025_states_of_denial]
the denial-defence debate.
[Burrows][journal_burrows_2026_china_war_scenario]
asks whether a China war scenario would break the insiders' hold,
which is a question about expertise rather than about outcomes.

**What that body of work does not contain is a study of the postwar distribution**,
which is the gap this article has been describing,
and the point of listing the near misses is to show it is a real absence
rather than a failure to look.

### The long-peace literature, which bears on whether the base rate still applies

[Gaddis][journal_gaddis_1986_long_peace]
named the postwar absence of great-power war,
and [Mueller][journal_mueller_1988_essential_irrelevance]
argued that nuclear weapons were not what produced it.
[Cederman, Warren and Sornette][journal_cederman_2011_testing_clausewitz]
model war severity directly.

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

**That matters for this article's method rather than for its subject.**
If the postwar period is a draw from the same distribution as the century before it,
a base rate computed across 1823 to 2003 applies to the next case.
If it is a regime change, it does not.
The statistics currently cannot tell the difference,
and the article computes the base rate while recording that.

### The policy record, which is primary and mostly unquoted

Several documents bear on the alignment question
and are available in their own words rather than through commentary.
The European Union's [strategic outlook][government_eu_2019_china_strategic_outlook]
introduced the formulation that has governed European policy since,
that China is "simultaneously, in different policy areas,
a cooperation partner, a negotiating partner,
an economic competitor and a systemic rival",
and the [Strategic Compass][government_eu_2022_strategic_compass]
carries it into defence planning.
**Reading the Compass for Taiwan returns nothing**,
which is a fact about European planning
rather than about European interests,
and it bears on the assumption that European states
would be participants rather than bystanders.

The non-aligned grouping has expanded in its own documents.
The [Johannesburg declaration][government_brics_2023_johannesburg]
records the invitations issued in 2023,
and the [Rio declaration][government_brics_2025_rio]
records which of them became members and which became partners,
a distinction that press accounts routinely collapse.

On the industrial side the legislative record is explicit.
The [CHIPS and Science Act][government_us_2022_chips_act]
sets out the appropriations by fiscal year
rather than the aggregate figures usually quoted,
and a [later public law][government_us_2025_pl_119_21]
raised the advanced manufacturing investment credit from 25 to 35 percent,
which is the sort of change that dates a secondary source silently.
The [October 2022 export controls][government_bis_2022_export_controls]
state the thresholds in the Federal Register
rather than in the paraphrases that circulate.

$$
25 \longrightarrow 35 \;\text{percent}
$$

And the island's own exposure is published by its own ministry.
The [Taiwan energy statistics handbook][data_taiwan_moea_energy]
puts dependence on imported energy at 94.62 percent in 2025,
with oil at 99.03 and liquefied natural gas at 99.82.

$$
94.62, \qquad 99.03, \qquad 99.82 \;\text{percent}
$$

**Those three numbers are the reason the blockade literature exists**,
and they come from the government of the territory in question
rather than from an analyst's estimate.

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
[Tetlock's tournament][book_tetlock_2005_expert_political_judgment] gives the general base rate.
[Gilpin][journal_gilpin_1988_hegemonic_war] notes that neither the Greeks nor the Europeans of 1914
anticipated what their wars would do.
[Nordhaus][research_nordhaus_2002_iraq_cost] provides a worked instance.

**That the measurement choice determines the answer.**
This is agreed by the people who build the instruments.
The [Correlates of War codebook][data_cow_nmc_v7] warns against longitudinal use of components.
[Lowy][data_lowy_2025_asia_power_index] states that other value judgements about its weights are possible.
[SIPRI][data_sipri_2026_milex] warns that its revision replaces all previously published data.
[Carroll and Kenkel][journal_carroll_kenkel_2019_prediction_proxies] show the standard ratio barely beats guessing.
[Allison's own project][commentary_allison_2015_thucydides_trap]
states that its cases use rise and rule
"according to their conventional definitions,
generally emphasizing rapid shifts in relative GDP and military strength",
which is a measurement choice presented as a convention.

### Seven disagreements, each with both sides named

**Whether a war durably changes the distribution at all.**
[Organski and Kugler][journal_organski_kugler_1977_phoenix] say losers resume antebellum status in fifteen to twenty years.
This article's computation finds every large-war loser down at ten years,
with a median loss of 42 percent.
The windows differ and the samples differ, and the two have not been reconciled.

**Whether non-participants gain.**
RAND asserts that victors "will be weakened relative to noncombatant states",
and Frederick says the great power that benefits most is the one that did not fight.
The historical test in this article finds no such pattern,
and the relationship that does appear runs the other way,
with concentrated belligerents faring worse rather than bystanders faring better.
[Nikkei's][commentary_nikkei_2022_taiwan_emergency] trade modelling finds non-belligerents bearing heavy absolute costs.
All three can hold simultaneously and the article says so.

**Whether the belligerents decline symmetrically.**
The scenario table here treats symmetric outcomes as two of four cases.
[Gompert and others][research_gompert_2016_war_with_china] estimate Chinese losses at about four times American losses.
Nothing in the capability data adjudicates this,
because the capability index is insensitive to the trade interdiction
that drives the asymmetry.

**Whether Taiwan is militarily worth taking.**
[Green and Talmadge][journal_green_talmadge_2022] say yes through submarine basing and surveillance.
[Caverley][journal_caverley_2025] says the island adds under three percent of relevant coastline
and would make little difference.
Both are published, recent, and methodologically explicit.

**Whether security guarantees restrain allies.**
[Bleek and Lorber][journal_bleek_lorber_2014_security_guarantees] find they do.
[Gerzhoy][journal_gerzhoy_2015_alliance_coercion] finds restraint came instead from threats of abandonment.
[Monteiro and Debs][journal_monteiro_debs_2014_strategic_logic] provide a framework in which both can be true
depending on which of willingness and opportunity binds.

**Whether a cascade would follow a visible American failure.**
The wargames and RAND treat it as a live risk.
[Fuhrmann and Tkach's][journal_fuhrmann_tkach_2015_nuclear_latency] base rate is about one in three over seventy years.
The one natural experiment, on the Washington Declaration,
found allied opinion unmoved by the alliance signal in either direction.

**Whether the system is already bipolar, and who counts.**
[Lind][journal_lind_2024_back_to_bipolarity] says yes and that neither Russia nor India is a great power.
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

**No study relates belligerent concentration to belligerent fortune.**
The measure is trivial to construct from published data
and this article found a correlation of minus 0.225 across seventy-six wars,
which is the sort of result a literature on the consequences of war
might have been expected to produce already.
Nothing located does, and the finding here is offered
as a first pass that wants replication rather than as a settled one.

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
Three harnesses re-entered 263 constants by hand from the article text
and recomputed each,
which caught two arithmetic errors before publication,
a relative change stated as 1.07 that is 1.06,
and a claim that the capability ratio has exceeded one in every year since 1995
when it dips below in 2002.

**The publication review caught a third and larger error, which was not arithmetic.**
Three passes of this article asserted that a great-power war
in which the belligerents hold a minority of world capability
would be without precedent, and that the resulting pool of non-participants
was the novel feature of the prospective case.
That is false, and the data used throughout refute it.
Twenty wars with at least twenty thousand battle deaths
had less concentrated belligerents than this one would have.
**The claim survived three passes because nobody had computed it,
including the author, and it was reached by reasoning from the two world wars
rather than from the ninety-five wars in the file.**
Computing it returned a relationship running the other way,
which is now reported in place of the refuted one
and which supports the article's conclusion by a different mechanism.
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
Two State Department documents in the Foreign Relations series,
whose quotations on Japanese procurement dependence
were confirmed against the Department's own published text.
The Belfer Center reprint of the Thucydides Trap essay,
for the two sentences quoted from it.
The Chang and others paper, for the Iraq cost figure,
whose two-column layout interleaves on extraction
exactly as the previous article recorded for scanned sources.

**Where a secondary source was available and a primary one existed, the primary was used.**
That is the whole of the reference pass.
Alliance commitments are quoted from the declarations rather than from descriptions of them,
the legislative figures from the public laws rather than from the aggregates in circulation,
the Taiwanese energy dependence from the Taiwanese ministry,
the reserve series from the Fund's own interface,
and the force-balance posture from the annual report that declines to print a total.
**Thirty of the two hundred and two references are government documents
and twenty are datasets**, which is a quarter of the external total,
against about a tenth in the previous article in this series.

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
That applies to [Organski and Kugler][journal_organski_kugler_1977_phoenix],
[Carroll and Kenkel][journal_carroll_kenkel_2019_prediction_proxies],
[Monteiro and Debs][journal_monteiro_debs_2014_strategic_logic],
[Gerzhoy][journal_gerzhoy_2015_alliance_coercion],
[Bleek and Lorber][journal_bleek_lorber_2014_security_guarantees],
[Fuhrmann and Tkach][journal_fuhrmann_tkach_2015_nuclear_latency],
[Rauchhaus][journal_rauchhaus_2009_nuclear_peace],
[Bell and Miller][journal_bell_miller_2015_questioning],
[Sechser and Fuhrmann][journal_sechser_fuhrmann_2013_nuclear_blackmail],
[Beckley][journal_beckley_2018_power_of_nations],
[Anders and others][journal_anders_2020_surplus_domestic_product],
[Brooks and Wohlforth][journal_brooks_wohlforth_2016_rise_and_fall],
[Green and Talmadge][journal_green_talmadge_2022],
[Snyder][journal_snyder_1984_security_dilemma],
[Henry][journal_henry_2020_what_allies_want],
[Powell][journal_powell_2006_commitment_problem],
[Levy][journal_levy_1987_declining_power],
[Fearon][journal_fearon_1995_rationalist],
[Chadefaux][journal_chadefaux_2011_bargaining],
[DiCicco and Levy][journal_dicicco_levy_1999_power_shifts],
[Doran and Parsons][journal_doran_parsons_1980_war_cycle],
[Lind][journal_lind_2024_back_to_bipolarity],
[Mearsheimer][journal_mearsheimer_2019_bound_to_fail]
and [Walt][journal_walt_2025_hedging_hegemony].
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
The concentration result rests on twelve comparable wars
and a correlation of minus 0.225 across seventy-six,
with no controls and a span of 180 years,
so it is a first pass that wants replication rather than an identified effect.
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

**On the distribution of power in the world, a modest loss to the belligerents,
by a mechanism other than the one usually asserted.**
The belligerents of 1914 held 82 percent of measured world capability
and those of 1939 held 98 percent.
Two states fighting this war would hold about 36 percent,
and about 45 percent on the widest plausible coalition,
which is less concentrated than either world war
and more concentrated than ninety-six percent of the wars in the record.
Across those wars, belligerent concentration predicts belligerent fortune
at a correlation of minus 0.225,
and in the band this case falls into
ten of twelve belligerent sets came out smaller,
at a median of minus five percent.
**That is not the bystander mechanism the scenario literature asserts.**
Nobody captures anything. Concentrated belligerents simply have more to lose,
and these would be concentrated.

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
and likely to leave both of them slightly smaller
relative to the states that stayed out.**
Each of those three is a statement about measured capability,
each rests on an instrument whose makers warn against this use,
and the third is the weakest of them,
resting on twelve comparable wars and a correlation of minus 0.225.

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
- [Book, Copeland 2018, The Origins of Major War][book_copeland_2018_origins_of_major_war]
- [Book, Gilpin 1981, War and Change in World Politics][book_gilpin_1981_war_and_change]
- [Book, Henry 2022, Reliability and Alliance Interdependence][book_henry_2022_reliability]
- [Book, Hymans 2006, The Psychology of Nuclear Proliferation][book_hymans_2006_psychology_of_proliferation]
- [Book, Ikenberry 2019, After Victory][book_ikenberry_2019_after_victory]
- [Book, Kennedy 1987, The Rise and Fall of the Great Powers][book_kennedy_1987_rise_and_fall]
- [Book, Lake 2017, Hierarchy in International Relations][book_lake_2017_hierarchy]
- [Book, Lanoszka 2018, Atomic Assurance][book_lanoszka_2018_atomic_assurance]
- [Book, Lemke 2002, Regions of War and Peace][book_lemke_2002_regions_of_war_and_peace]
- [Book, McDowell 2023, Bucking the Buck][book_mcdowell_2023_bucking_the_buck]
- [Book, Organski and Kugler 1980, The War Ledger][book_organski_kugler_1980_war_ledger]
- [Book, Prasad 2015, The Dollar Trap][book_prasad_2015_dollar_trap]
- [Book, Rockoff 2012, America's Economic Way of War][book_rockoff_2012_americas_economic_way_of_war]
- [Book, Singer, Bremer and Stuckey 1972, Capability Distribution, Uncertainty, and Major Power War, 1820 to 1965][book_singer_1972_capability_distribution]
- [Book, Tetlock 2005, Expert Political Judgment][book_tetlock_2005_expert_political_judgment]
- [Commentary, Arms Control Today 2026, 2026 NPT Review Conference Stymied by Disputes][commentary_act_2026_npt_revcon]
- [Commentary, Allison 2015, The Thucydides Trap, Are the United States and China Headed for War][commentary_allison_2015_thucydides_trap]
- [Commentary, Nikkei 2022, 2.6tn Dollars Could Evaporate From the Global Economy in a Taiwan Emergency][commentary_nikkei_2022_taiwan_emergency]
- [Data, Bank for International Settlements 2025, Triennial Central Bank Survey, OTC Foreign Exchange Turnover in April 2025][data_bis_2025_triennial]
- [Data, Bank for International Settlements 2026, Credit to the Non-Financial Sector][data_bis_total_credit]
- [Data, Congressional Budget Office 2026, Budget and Economic Projections][data_cbo_2026_projections]
- [Data, Chicago Council on Global Affairs 2022, Thinking Nuclear, South Korean Attitudes on Nuclear Weapons][data_chicago_council_2022_south_korea]
- [Data, Correlates of War 2020, Inter-State War Data version 4.0][data_cow_interstate_war_v4]
- [Data, Sarkees and Wayman 2010, Correlates of War Inter-State Wars Codebook][data_cow_interstate_wars_codebook]
- [Data, Correlates of War 2025, National Material Capabilities version 7.0][data_cow_nmc_v7]
- [Data, International Monetary Fund 2026, Currency Composition of Official Foreign Exchange Reserves][data_imf_cofer]
- [Data, International Monetary Fund 2026, PortWatch Chokepoint and Port Monitoring][data_imf_portwatch]
- [Data, ISEAS Yusof Ishak Institute 2026, The State of Southeast Asia 2026 Survey Report][data_iseas_2026_state_of_southeast_asia]
- [Data, Korea Institute for National Unification 2023, KINU Unification Survey 2023][data_kinu_2023_unification_survey]
- [Data, Lowy Institute 2025, Asia Power Index][data_lowy_2025_asia_power_index]
- [Data, Groningen Growth and Development Centre 2023, Maddison Project Database][data_maddison_project_2023]
- [Data, SIPRI 2026, Trends in World Military Expenditure 2025][data_sipri_2026_milex]
- [Data, SIPRI 2026, Military Expenditure Database][data_sipri_milex_database]
- [Data, Ministry of Economic Affairs 2025, Energy Statistics Handbook of the Republic of China][data_taiwan_moea_energy]
- [Data, United States Treasury 2026, Debt to the Penny][data_treasury_debt_to_the_penny]
- [Data, United States Treasury 2026, Major Foreign Holders of Treasury Securities][data_treasury_tic_2026]
- [Data, United Nations Conference on Trade and Development 2026, Seaborne Trade][data_unctad_seaborne_trade]
- [Data, World Bank 2026, World Development Indicators][data_world_bank_wdi]
- [Government, Bureau of Industry and Security 2022, Implementation of Additional Export Controls, 87 Federal Register 62186][government_bis_2022_export_controls]
- [Government, BRICS 2023, Johannesburg II Declaration][government_brics_2023_johannesburg]
- [Government, BRICS 2025, Rio de Janeiro Declaration][government_brics_2025_rio]
- [Government, Congressional Research Service 2025, National Defense Strategy, Potential Implications of Prioritizing the Western Hemisphere and China][government_crs_2025_national_defense_strategy]
- [Government, Congressional Research Service 2026, United States Extended Deterrence and Regional Nuclear Capabilities][government_crs_2026_extended_deterrence]
- [Government, Congressional Research Service 2026, Japan's Evolving Defense Policy and the United States-Japan Alliance][government_crs_2026_japan_defense]
- [Government, Congressional Research Service 2026, NATO, Issues for the July 2026 Summit][government_crs_2026_nato_summit]
- [Government, Congressional Research Service 2026, The Philippines, Background and United States Relations][government_crs_2026_philippines]
- [Government, Congressional Research Service 2010, Costs of Major United States Wars][government_crs_costs_of_major_wars]
- [Government, Department of Defense 2025, Annual Report to Congress on Military and Security Developments Involving the People's Republic of China][government_dod_2025_china_report]
- [Government, Department of Defense 2025, Republic of Korea Nuclear Consultative Group Fact Sheet][government_dod_2025_ncg_fact_sheet]
- [Government, Energy Information Administration 2025, The Strait of Hormuz Remains a Critical Oil Chokepoint][government_eia_2025_hormuz]
- [Government, Energy Information Administration 2026, China, the United States and Japan Hold Most Strategic Oil Inventories][government_eia_2026_strategic_stocks]
- [Government, European Commission 2019, EU-China, A Strategic Outlook][government_eu_2019_china_strategic_outlook]
- [Government, Council of the European Union 2022, A Strategic Compass for Security and Defence][government_eu_2022_strategic_compass]
- [Government, Department of State 1953, Foreign Relations of the United States 1952 to 1954 volume 14 part 2 document 684][government_frus_1952_japan_dollar_earnings]
- [Government, Department of State 1953, Foreign Relations of the United States 1952 to 1954 volume 14 part 2 document 646][government_frus_1952_japan_procurement]
- [Government, International Monetary Fund 2026, People's Republic of China 2025 Article IV Consultation][government_imf_2026_china_article_iv]
- [Government, Government of Japan 2022, National Security Strategy of Japan][government_japan_2022_nss]
- [Government, Government of Japan 2025, The Status Report of Plutonium Management in Japan 2024][government_japan_2025_plutonium]
- [Government, Ministry of Defense of Japan 2025, Overview of the FY2026 Defense Budget][government_japan_2026_defense_budget]
- [Government, President of Russia 2022, Joint Statement of the Russian Federation and the People's Republic of China][government_kremlin_2022_joint_statement]
- [Government, Lloyd's Market Association 2026, Joint War Committee Listed Areas][government_lma_2026_jwc_listed_areas]
- [Government, National Intelligence Council 2021, Global Trends 2040, A More Contested World][government_nic_2021_global_trends]
- [Government, United States 1979, Taiwan Relations Act, Public Law 96-8][government_us_1979_taiwan_relations_act]
- [Government, United States 2022, CHIPS and Science Act, Public Law 117-167][government_us_2022_chips_act]
- [Government, United States 2023, The Spirit of Camp David, Joint Statement of Japan, the Republic of Korea and the United States][government_us_2023_camp_david]
- [Government, United States 2023, Washington Declaration][government_us_2023_washington_declaration]
- [Government, United States 2024, The Wilmington Declaration][government_us_2024_wilmington_declaration]
- [Government, United States 2025, Public Law 119-21, Section 70308][government_us_2025_pl_119_21]
- [Journal, Anders, Fariss and Markowitz 2020, Bread Before Guns or Butter, International Studies Quarterly 64 number 2][journal_anders_2020_surplus_domestic_product]
- [Journal, Anderson and Press 2025, Access Denied, International Security 50 number 1][journal_anderson_press_2025_access_denied]
- [Journal, Arslanalp, Eichengreen and Simpson-Bell 2022, The Stealth Erosion of Dollar Dominance, Journal of International Economics 138][journal_arslanalp_2022_stealth_erosion]
- [Journal, Beckley 2010, Economic Development and Military Effectiveness, Journal of Strategic Studies 33 number 1][journal_beckley_2010_economic_development]
- [Journal, Beckley 2012, China's Century, International Security 36 number 3][journal_beckley_2012_chinas_century]
- [Journal, Beckley 2015, The Myth of Entangling Alliances, International Security 39 number 4][journal_beckley_2015_entangling_alliances]
- [Journal, Beckley 2018, The Power of Nations, International Security 43 number 2][journal_beckley_2018_power_of_nations]
- [Journal, Bell and Miller 2015, Questioning the Effect of Nuclear Weapons on Conflict, Journal of Conflict Resolution 59 number 1][journal_bell_miller_2015_questioning]
- [Journal, Bianchi and Sosa-Padilla 2025, International Sanctions and Dollar Dominance, The Economic Journal 135 number 672][journal_bianchi_sosa_padilla_2025_sanctions_dollar]
- [Journal, Bleek and Lorber 2014, Security Guarantees and Allied Nuclear Proliferation, Journal of Conflict Resolution 58 number 3][journal_bleek_lorber_2014_security_guarantees]
- [Journal, Bolt and van Zanden 2024, Maddison-Style Estimates of the Evolution of the World Economy, Journal of Economic Surveys 39 number 2][journal_bolt_vanzanden_2024_maddison]
- [Journal, Boughton 2001, Northwest of Suez, IMF Staff Papers 48 number 3][journal_boughton_2001_northwest_of_suez]
- [Journal, Boz and others 2022, Patterns of Invoicing Currency in Global Trade, Journal of International Economics 136][journal_boz_2022_invoicing_patterns]
- [Journal, Brooks and Wohlforth 2016, The Rise and Fall of the Great Powers in the Twenty-first Century, International Security 40 number 3][journal_brooks_wohlforth_2016_rise_and_fall]
- [Journal, Burrows 2026, Would a China War Scenario Break the Insiders' Hold, Texas National Security Review 9 number 1][journal_burrows_2026_china_war_scenario]
- [Journal, Cancian 2025, States of Denial, Survival 67 number 2][journal_cancian_2025_states_of_denial]
- [Journal, Carroll and Kenkel 2019, Prediction, Proxies, and Power, American Journal of Political Science 63 number 3][journal_carroll_kenkel_2019_prediction_proxies]
- [Journal, Caverley 2025, So What, Texas National Security Review 8 number 3][journal_caverley_2025]
- [Journal, Cederman, Warren and Sornette 2011, Testing Clausewitz, International Organization 65 number 4][journal_cederman_2011_testing_clausewitz]
- [Journal, Chadefaux 2011, Bargaining Over Power, International Theory 3 number 2][journal_chadefaux_2011_bargaining]
- [Journal, Chang, Chen, Mellers and Tetlock 2016, Developing Expert Political Judgment, Judgment and Decision Making 11 number 5][journal_chang_2016_developing_expert_judgment]
- [Journal, Chitu, Eichengreen and Mehl 2014, When Did the Dollar Overtake Sterling as the Leading International Currency, Journal of Development Economics 111][journal_chitu_2014_bond_markets]
- [Journal, Christensen and Snyder 1990, Chain Gangs and Passed Bucks, International Organization 44 number 2][journal_christensen_snyder_1990_chain_gangs]
- [Journal, Cirillo and Taleb 2016, On the Statistical Properties and Tail Risk of Violent Conflicts, Physica A 452][journal_cirillo_taleb_2016_tail_risk]
- [Journal, Clauset 2018, Trends and Fluctuations in the Severity of Interstate Wars, Science Advances 4 number 2][journal_clauset_2018_trends_fluctuations]
- [Journal, Collins 2018, A Maritime Oil Blockade Against China, Naval War College Review 71 number 2][journal_collins_2018_maritime_oil_blockade]
- [Journal, Cooley and Nexon 2013, The Empire Will Compensate You, Perspectives on Politics 11 number 4][journal_cooley_nexon_2013_empire_compensate]
- [Journal, Cunningham and Ven Bruusgaard 2026, Escalate to Survive, International Security 50 number 4][journal_cunningham_2026_escalate_to_survive]
- [Journal, Davis and Gholz 2026, Blockade by Fire, International Security 50 number 4][journal_davis_gholz_2026_blockade_by_fire]
- [Journal, Davis and Weinstein 2002, Bones, Bombs, and Break Points, American Economic Review 92 number 5][journal_davis_weinstein_2002_bones_bombs]
- [Journal, DiCicco and Levy 1999, Power Shifts and Problem Shifts, Journal of Conflict Resolution 43 number 6][journal_dicicco_levy_1999_power_shifts]
- [Journal, Doran 1989, Systemic Disequilibrium, Foreign Policy Role, and the Power Cycle, Journal of Conflict Resolution 33 number 3][journal_doran_1989_systemic_disequilibrium]
- [Journal, Doran and Parsons 1980, War and the Cycle of Relative Power, American Political Science Review 74 number 4][journal_doran_parsons_1980_war_cycle]
- [Journal, Eichengreen, Chitu and Mehl 2015, Stability or Upheaval, IMF Economic Review 64 number 2][journal_eichengreen_2015_stability_or_upheaval]
- [Journal, Eichengreen, Mehl and Chitu 2019, Mars or Mercury, Economic Policy 34 number 98][journal_eichengreen_2019_mars_or_mercury]
- [Journal, Eichengreen and Flandreau 2009, The Rise and Fall of the Dollar, European Review of Economic History 13 number 3][journal_eichengreen_flandreau_2009_rise_and_fall]
- [Journal, Evangelista 2024, A Nuclear Umbrella for Ukraine, International Security 48 number 3][journal_evangelista_2024_nuclear_umbrella]
- [Journal, Farrell and Newman 2019, Weaponized Interdependence, International Security 44 number 1][journal_farrell_newman_2019_weaponized]
- [Journal, Fearon 1995, Rationalist Explanations for War, International Organization 49 number 3][journal_fearon_1995_rationalist]
- [Journal, Fitzpatrick 2025, A Farewell to the Thucydides Trap, German History 43 number 2][journal_fitzpatrick_2025_farewell]
- [Journal, Fuhrmann and Tkach 2015, Almost Nuclear, Conflict Management and Peace Science 32 number 4][journal_fuhrmann_tkach_2015_nuclear_latency]
- [Journal, Gaddis 1986, The Long Peace, International Security 10 number 4][journal_gaddis_1986_long_peace]
- [Journal, Gavin 2010, Same As It Ever Was, International Security 34 number 3][journal_gavin_2010_same_as_it_ever_was]
- [Journal, Gerzhoy 2015, Alliance Coercion and Nuclear Restraint, International Security 39 number 4][journal_gerzhoy_2015_alliance_coercion]
- [Journal, Gilpin 1988, The Theory of Hegemonic War, Journal of Interdisciplinary History 18 number 4][journal_gilpin_1988_hegemonic_war]
- [Journal, Gopinath and others 2020, Dominant Currency Paradigm, American Economic Review 110 number 3][journal_gopinath_2020_dominant_currency_paradigm]
- [Journal, Gopinath and Stein 2021, Banking, Trade, and the Making of a Dominant Currency, Quarterly Journal of Economics 136 number 2][journal_gopinath_stein_2021_dominant_currency]
- [Journal, Green and Talmadge 2022, Then What, International Security 47 number 1][journal_green_talmadge_2022]
- [Journal, Greitens and Kardon 2025, Security without Exclusivity, International Security 49 number 3][journal_greitens_kardon_2025_security_without_exclusivity]
- [Journal, Grieco 1988, Anarchy and the Limits of Cooperation, International Organization 42 number 3][journal_grieco_1988_anarchy_limits]
- [Journal, Grieco, Powell and Snidal 1993, The Relative-Gains Problem for International Cooperation, American Political Science Review 87 number 3][journal_grieco_powell_snidal_1993_relative_gains]
- [Journal, Hall and Sargent 2011, Interest Rate Risk and Other Determinants of Post-War United States Government Debt, American Economic Journal Macroeconomics 3 number 3][journal_hall_sargent_2011_interest_rate_risk]
- [Journal, Henry 2020, What Allies Want, International Security 44 number 4][journal_henry_2020_what_allies_want]
- [Journal, Ikenberry 1999, Institutions, Strategic Restraint, and the Persistence of American Postwar Order, International Security 23 number 3][journal_ikenberry_1999_institutions_restraint]
- [Journal, Ikenberry 2018, The End of Liberal International Order, International Affairs 94 number 1][journal_ikenberry_2018_end_of_liberal_order]
- [Journal, Ikenberry 2024, Three Worlds, International Affairs 100 number 1][journal_ikenberry_2024_three_worlds]
- [Journal, Ikenberry and Nexon 2019, Hegemony Studies 3.0, Security Studies 28 number 3][journal_ikenberry_nexon_2019_hegemony_studies]
- [Journal, Ilzetzki, Reinhart and Rogoff 2020, Why Is the Euro Punching Below Its Weight, Economic Policy 35 number 103][journal_ilzetzki_2020_euro_punching]
- [Journal, Kadera and Sorokin 2004, Measuring National Power, International Interactions 30 number 3][journal_kadera_sorokin_2004_measuring_national_power]
- [Journal, Kang and Ma 2018, Power Transitions, The Washington Quarterly 41 number 1][journal_kang_ma_2018_power_transitions]
- [Journal, Kitchen and Cox 2019, Power, Structural Power, and American Decline, Cambridge Review of International Affairs 32 number 6][journal_kitchen_cox_2019_structural_power]
- [Journal, Kugler and Arbetman 1989, Exploring the Phoenix Factor with the Collective Goods Perspective, Journal of Conflict Resolution 33 number 1][journal_kugler_arbetman_1989_phoenix]
- [Journal, Kuik 2008, The Essence of Hedging, Contemporary Southeast Asia 30 number 2][journal_kuik_2008_essence_of_hedging]
- [Journal, Lake 2007, Escape from the State of Nature, International Security 32 number 1][journal_lake_2007_escape_state_of_nature]
- [Journal, Lanteigne 2008, China's Maritime Security and the Malacca Dilemma, Asian Security 4 number 2][journal_lanteigne_2008_malacca_dilemma]
- [Journal, Levy 1987, Declining Power and the Preventive Motivation for War, World Politics 40 number 1][journal_levy_1987_declining_power]
- [Journal, Lim and Cooper 2015, Reassessing Hedging, Security Studies 24 number 4][journal_lim_cooper_2015_reassessing_hedging]
- [Journal, Lim and Ikenberry 2023, China and the Logic of Illiberal Hegemony, Security Studies 32 number 1][journal_lim_ikenberry_2023_illiberal_hegemony]
- [Journal, Lind 2024, Back to Bipolarity, International Security 49 number 2][journal_lind_2024_back_to_bipolarity]
- [Journal, Markowitz and Fariss 2013, Going the Distance, International Interactions 39 number 2][journal_markowitz_fariss_2013_going_the_distance]
- [Journal, McKinney and Harris 2021, Broken Nest, Parameters 51 number 4][journal_mckinney_harris_2021_broken_nest]
- [Journal, Mearsheimer 2019, Bound to Fail, International Security 43 number 4][journal_mearsheimer_2019_bound_to_fail]
- [Journal, Mehta and Whitlark 2017, The Benefits and Burdens of Nuclear Latency, International Studies Quarterly 61 number 3][journal_mehta_whitlark_2017_latency]
- [Journal, Menon 2026, A New World Order, Texas National Security Review 9 number 1][journal_menon_2026_new_world_order]
- [Journal, Mirski 2013, Stranglehold, Journal of Strategic Studies 36 number 3][journal_mirski_2013_stranglehold]
- [Journal, Monteiro and Debs 2014, The Strategic Logic of Nuclear Proliferation, International Security 39 number 2][journal_monteiro_debs_2014_strategic_logic]
- [Journal, Morley 2026, Thucydiocies, Public Humanities 2][journal_morley_2026_thucydiocies]
- [Journal, Mueller 1988, The Essential Irrelevance of Nuclear Weapons, International Security 13 number 2][journal_mueller_1988_essential_irrelevance]
- [Journal, Narang 2017, Strategies of Nuclear Proliferation, International Security 41 number 3][journal_narang_2017_strategies_of_proliferation]
- [Journal, Nemeth 2026, How a United States Suez Moment Could Hollow the Alliance System, Texas National Security Review 9 number 1][journal_nemeth_2026_suez_moment]
- [Journal, Ohanian 1997, The Macroeconomic Effects of War Finance in the United States, American Economic Review 87 number 1][journal_ohanian_1997_macroeconomic_effects_war_finance]
- [Journal, Organski and Kugler 1977, The Costs of Major Wars, The Phoenix Factor, American Political Science Review 71 number 4][journal_organski_kugler_1977_phoenix]
- [Journal, Platias and Trigkas 2021, Unravelling the Thucydides Trap, The Chinese Journal of International Politics 14 number 2][journal_platias_trigkas_2021_unravelling]
- [Journal, Posen 2003, Command of the Commons, International Security 28 number 1][journal_posen_2003_command_of_the_commons]
- [Journal, Powell 1991, Absolute and Relative Gains in International Relations Theory, American Political Science Review 85 number 4][journal_powell_1991_absolute_relative_gains]
- [Journal, Powell 2006, War as a Commitment Problem, International Organization 60 number 1][journal_powell_2006_commitment_problem]
- [Journal, Priebe and others 2024, Competing Visions of Restraint, International Security 49 number 2][journal_priebe_2024_competing_visions]
- [Journal, Rauchhaus 2009, Evaluating the Nuclear Peace Hypothesis, Journal of Conflict Resolution 53 number 2][journal_rauchhaus_2009_nuclear_peace]
- [Journal, Sagan 1997, Why Do States Build Nuclear Weapons, International Security 21 number 3][journal_sagan_1997_why_states_build]
- [Journal, Schroeder 1992, Did the Vienna Settlement Rest on a Balance of Power, The American Historical Review 97 number 3][journal_schroeder_1992_vienna_settlement]
- [Journal, Sechser and Fuhrmann 2013, Crisis Bargaining and Nuclear Blackmail, International Organization 67 number 1][journal_sechser_fuhrmann_2013_nuclear_blackmail]
- [Journal, Snidal 1991, Relative Gains and the Pattern of International Cooperation, American Political Science Review 85 number 3][journal_snidal_1991_relative_gains]
- [Journal, Snyder 1984, The Security Dilemma in Alliance Politics, World Politics 36 number 4][journal_snyder_1984_security_dilemma]
- [Journal, Tomz and Weeks 2021, Military Alliances and Public Support for War, International Studies Quarterly 65 number 3][journal_tomz_weeks_2021_military_alliances]
- [Journal, Trachtenberg 2025, The Rules-Based International Order, International Security 50 number 2][journal_trachtenberg_2025_rules_based_order]
- [Journal, Verschuur, Lumma and Hall 2025, Systemic Impacts of Disruptions at Maritime Chokepoints, Nature Communications 16][journal_verschuur_2025_chokepoints]
- [Journal, Von Hippel 2019, Mitigating the Threat of Nuclear-Weapon Proliferation via Nuclear-Submarine Programs, Journal for Peace and Nuclear Disarmament 2 number 1][journal_von_hippel_2019_naval_propulsion]
- [Journal, Walt 2025, Hedging on Hegemony, International Security 49 number 4][journal_walt_2025_hedging_hegemony]
- [Journal, Welch 2003, Why International Relations Theorists Should Stop Reading Thucydides, Review of International Studies 29 number 3][journal_welch_2003_stop_reading_thucydides]
- [Reference, Tammen, Kugler and Lemke 2017, Foundations of Power Transition Theory, Oxford Research Encyclopedia of Politics][reference_tammen_2017_foundations]
- [Related Post, What Published Wargames Say About a War With China][related_post_published_wargames]
- [Related Post, What Rebuilding Would Take After a War With China][related_post_rebuilding]
- [Research, Albright and Stricker 2018, Taiwan's Former Nuclear Weapons Program][research_albright_2018_taiwan_nuclear_program]
- [Research, Atlantic Council 2025, Welcome to 2035][research_atlantic_council_2025_welcome_2035]
- [Research, Atlantic Council 2026, Welcome to 2036][research_atlantic_council_2026_welcome_2036]
- [Research, Bianchi and Sosa-Padilla 2023, International Sanctions and Dollar Dominance, NBER Working Paper 31024][research_bianchi_2023_sanctions_dollar]
- [Research, Cancian, Cancian and Heginbotham 2023, The First Battle of the Next War][research_cancian_2023_first_battle]
- [Research, Crawford 2021, The United States Budgetary Costs of the Post-9/11 Wars][research_crawford_2021_budgetary_costs]
- [Research, Dooley, Folkerts-Landau and Garber 2022, US Sanctions Reinforce the Dollar's Dominance][research_dooley_2022_sanctions_reinforce]
- [Research, European Council on Foreign Relations 2023, Living in an a la Carte World][research_ecfr_2023_a_la_carte]
- [Research, Edwards 2010, United States War Costs, Two Parts Temporary, One Part Permanent, NBER Working Paper 16108][research_edwards_2010_war_costs]
- [Research, Eichengreen 2005, Sterling's Past, Dollar's Future, NBER Working Paper 11336][research_eichengreen_2005_sterlings_past]
- [Research, Evans 2023, Alternative Futures Following a Great Power War, Volume 2][research_evans_2023_alternative_futures_v2]
- [Research, Fariss and others 2017, Latent Estimation of GDP, GDP per capita, and Population][research_fariss_2017_latent_estimation]
- [Research, Goes and Bekkers 2022, The Impact of Geopolitical Conflicts on Trade, Growth, and Innovation][research_goes_bekkers_2022_geopolitical_conflicts]
- [Research, Gompert, Cevallos and Garafola 2016, War with China, Thinking Through the Unthinkable][research_gompert_2016_war_with_china]
- [Research, Hall and Sargent 2020, Debt and Taxes in Eight United States Wars and Two Insurrections, NBER Working Paper 27115][research_hall_sargent_2020_debt_and_taxes]
- [Research, Harrison 1998, The Economics of World War II, An Overview][research_harrison_1998_economics_of_wwii]
- [Research, Hohn 2014, Geopolitics and the Measurement of National Power][research_hohn_2014_geopolitics_measurement]
- [Research, Jiang and others 2026, Dollar Erosion, NBER Working Paper 35328][research_jiang_2026_dollar_erosion]
- [Research, Kwende and Nephew 2025, Improving the Analytical Usefulness of the IMF's COFER Data][research_kwende_nephew_2025_cofer]
- [Research, Nordhaus 2002, The Economic Consequences of a War with Iraq][research_nordhaus_2002_iraq_cost]
- [Research, National Security Archive 2019, Taiwan's Quest for the Bomb][research_nsarchive_2019_taiwans_bomb]
- [Research, Priebe and others 2023, Alternative Futures Following a Great Power War, Volume 1][research_priebe_2023_alternative_futures_v1]
- [Research, Priebe and Frederick 2023, Alternative Futures Following a Great Power War, In Conversation][research_priebe_frederick_2023_conversation]
- [Research, Reinhart and Sbrancia 2011, The Liquidation of Government Debt, NBER Working Paper 16893][research_reinhart_sbrancia_2011_liquidation]
- [Research, Rhodium Group 2022, The Global Economic Disruptions from a Taiwan Conflict][research_rhodium_2022_taiwan_disruptions]
- [Research, Rockoff 2004, Until It's Over, Over There, NBER Working Paper 10580][research_rockoff_2004_until_its_over]
- [Research, Tarapore 2024, Deterring an Attack on Taiwan, Policy Options for India and Other Non-Belligerent States][research_tarapore_2024_deterring_attack]
- [Research, Tellis and others 2000, Measuring National Power in the Postindustrial Age][research_tellis_2000_measuring_national_power]
- [Research, Vest and Kratz 2023, Sanctioning China in a Taiwan Crisis][research_vest_kratz_2023_sanctioning_china]
- [Research, Weiss 2022, Geopolitics and the United States Dollar's Future as a Reserve Currency][research_weiss_2022_geopolitics_dollar]
- [Research, Weiss 2025, De-Dollarization, Diversification, Exploring Central Bank Gold Purchases][research_weiss_2025_dedollarization]

[book_cooley_nexon_2020_exit_from_hegemony]: https://doi.org/10.1093/oso/9780190916473.001.0001
[book_copeland_2018_origins_of_major_war]: https://doi.org/10.7591/9780801467059
[book_gilpin_1981_war_and_change]: https://doi.org/10.1017/cbo9780511664267
[book_henry_2022_reliability]: https://doi.org/10.1515/9781501763052
[book_hymans_2006_psychology_of_proliferation]: https://doi.org/10.1017/CBO9780511491412
[book_ikenberry_2019_after_victory]: https://doi.org/10.23943/princeton/9780691169217.001.0001
[book_kennedy_1987_rise_and_fall]: https://archive.org/details/the-rise-and-fall-of-the-great-powers-economic-change-and-military-conflict-from-1500-to-2000
[book_lake_2017_hierarchy]: https://doi.org/10.7591/9780801458934
[book_lanoszka_2018_atomic_assurance]: https://doi.org/10.7591/cornell/9781501729188.001.0001
[book_lemke_2002_regions_of_war_and_peace]: https://doi.org/10.1017/cbo9780511491511
[book_mcdowell_2023_bucking_the_buck]: https://doi.org/10.1093/oso/9780197679876.001.0001
[book_organski_kugler_1980_war_ledger]: https://doi.org/10.7208/chicago/9780226351841.001.0001
[book_prasad_2015_dollar_trap]: https://doi.org/10.1515/9781400873647
[book_rockoff_2012_americas_economic_way_of_war]: https://doi.org/10.1017/cbo9781139046534
[book_singer_1972_capability_distribution]: https://doi.org/10.4324/9780203128398-28
[book_tetlock_2005_expert_political_judgment]: https://doi.org/10.1515/9781400888818
[commentary_act_2026_npt_revcon]: https://www.armscontrol.org/act/2026-06/news/2026-npt-review-conference-stymied-disputes
[commentary_allison_2015_thucydides_trap]: https://www.belfercenter.org/publication/thucydides-trap-are-us-and-china-headed-war
[commentary_nikkei_2022_taiwan_emergency]: https://asia.nikkei.com/static/vdata/infographics/2-dot-6tn-dollars-could-evaporate-from-global-economy-in-taiwan-emergency/
[data_bis_2025_triennial]: https://www.bis.org/statistics/rpfx25_fx.htm
[data_bis_total_credit]: https://data.bis.org/topics/TOTAL_CREDIT
[data_cbo_2026_projections]: https://www.cbo.gov/publication/51118
[data_chicago_council_2022_south_korea]: https://globalaffairs.org/research/public-opinion-survey/thinking-nuclear-south-korean-attitudes-nuclear-weapons
[data_cow_interstate_war_v4]: https://correlatesofwar.org/data-sets/cow-war/
[data_cow_interstate_wars_codebook]: https://correlatesofwar.org/wp-content/uploads/Inter-StateWars_Codebook.pdf
[data_cow_nmc_v7]: https://correlatesofwar.org/data-sets/national-material-capabilities/
[data_imf_cofer]: https://data.imf.org/en/datasets/IMF.STA:COFER
[data_imf_portwatch]: https://portwatch.imf.org/
[data_iseas_2026_state_of_southeast_asia]: https://www.iseas.edu.sg/wp-content/uploads/2026/03/The-State-of-Southeast-Asia-2026-Survey-Final-Single.pdf
[data_kinu_2023_unification_survey]: https://repo.kinu.or.kr/handle/2015.oak/14362
[data_lowy_2025_asia_power_index]: https://power.lowyinstitute.org/
[data_maddison_project_2023]: https://www.rug.nl/ggdc/historicaldevelopment/maddison/releases/maddison-project-database-2023
[data_sipri_2026_milex]: https://doi.org/10.55163/ZLHQ1057
[data_sipri_milex_database]: https://www.sipri.org/databases/milex
[data_taiwan_moea_energy]: https://ea01.moeaea.gov.tw/a0303/02/en/publication/handbook/
[data_treasury_debt_to_the_penny]: https://fiscaldata.treasury.gov/datasets/debt-to-the-penny/debt-to-the-penny
[data_treasury_tic_2026]: https://ticdata.treasury.gov/resource-center/data-chart-center/tic/Documents/slt_table5.html
[data_unctad_seaborne_trade]: https://unctadstat.unctad.org/datacentre/dataviewer/US.SeaborneTrade
[data_world_bank_wdi]: https://datatopics.worldbank.org/world-development-indicators/
[government_bis_2022_export_controls]: https://www.govinfo.gov/content/pkg/FR-2022-10-13/pdf/2022-21658.pdf
[government_brics_2023_johannesburg]: http://www.brics.utoronto.ca/docs/230823-declaration.html
[government_brics_2025_rio]: http://www.brics.utoronto.ca/docs/250706-declaration.html
[government_crs_2025_national_defense_strategy]: https://www.everycrsreport.com/reports/IF13137.html
[government_crs_2026_extended_deterrence]: https://www.everycrsreport.com/reports/IF12735.html
[government_crs_2026_japan_defense]: https://www.everycrsreport.com/reports/IN12708.html
[government_crs_2026_nato_summit]: https://www.everycrsreport.com/reports/R49018.html
[government_crs_2026_philippines]: https://www.everycrsreport.com/reports/R47055.html
[government_crs_costs_of_major_wars]: https://www.everycrsreport.com/reports/RS22926.html
[government_dod_2025_china_report]: https://media.defense.gov/2025/Dec/23/2003849070/-1/-1/1/ANNUAL-REPORT-TO-CONGRESS-MILITARY-AND-SECURITY-DEVELOPMENTS-INVOLVING-THE-PEOPLES-REPUBLIC-OF-CHINA-2025.PDF
[government_dod_2025_ncg_fact_sheet]: https://media.defense.gov/2025/Jan/10/2003626634/-1/-1/1/THE-UNITED-STATES-OF-AMERICA-REPUBLIC-OF-KOREA-NUCLEAR-CONSULTATIVE-GROUP-FACT-SHEET.PDF
[government_eia_2025_hormuz]: https://www.eia.gov/todayinenergy/detail.php?id=65504
[government_eia_2026_strategic_stocks]: https://www.eia.gov/todayinenergy/detail.php?id=67504
[government_eu_2019_china_strategic_outlook]: https://commission.europa.eu/system/files/2019-03/communication-eu-china-a-strategic-outlook.pdf
[government_eu_2022_strategic_compass]: https://data.consilium.europa.eu/doc/document/ST-7371-2022-INIT/en/pdf
[government_frus_1952_japan_dollar_earnings]: https://history.state.gov/historicaldocuments/frus1952-54v14p2/d684
[government_frus_1952_japan_procurement]: https://history.state.gov/historicaldocuments/frus1952-54v14p2/d646
[government_imf_2026_china_article_iv]: https://doi.org/10.5089/9798229038911.002.A001
[government_japan_2022_nss]: https://www.cas.go.jp/jp/siryou/221216anzenhoshou/nss-e.pdf
[government_japan_2025_plutonium]: https://www.aec.go.jp/bunya/04/plutonium/20250805_e.pdf
[government_japan_2026_defense_budget]: https://www.mod.go.jp/en/d_act/d_budget/pdf/fy2026_20251226a.pdf
[government_kremlin_2022_joint_statement]: http://en.kremlin.ru/supplement/5770
[government_lma_2026_jwc_listed_areas]: https://lmalloyds.com/specialist-areas/underwriting/listed-areas/
[government_nic_2021_global_trends]: https://www.dni.gov/index.php/gt2040-home
[government_us_1979_taiwan_relations_act]: https://www.govinfo.gov/content/pkg/STATUTE-93/pdf/STATUTE-93-Pg14.pdf
[government_us_2022_chips_act]: https://www.govinfo.gov/content/pkg/PLAW-117publ167/html/PLAW-117publ167.htm
[government_us_2023_camp_david]: https://kr.usembassy.gov/081923-the-spirit-of-camp-david-joint-statement-of-japan-the-republic-of-korea-and-the-united-states/
[government_us_2023_washington_declaration]: https://kr.usembassy.gov/042723-washington-declaration/
[government_us_2024_wilmington_declaration]: https://bidenwhitehouse.archives.gov/briefing-room/statements-releases/2024/09/21/the-wilmington-declaration-joint-statement-from-the-leaders-of-australia-india-japan-and-the-united-states/
[government_us_2025_pl_119_21]: https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm
[journal_anders_2020_surplus_domestic_product]: https://doi.org/10.1093/isq/sqaa013
[journal_anderson_press_2025_access_denied]: https://doi.org/10.1162/isec.a.7
[journal_arslanalp_2022_stealth_erosion]: https://doi.org/10.1016/j.jinteco.2022.103656
[journal_beckley_2010_economic_development]: https://doi.org/10.1080/01402391003603581
[journal_beckley_2012_chinas_century]: https://doi.org/10.1162/isec_a_00066
[journal_beckley_2015_entangling_alliances]: https://doi.org/10.1162/isec_a_00197
[journal_beckley_2018_power_of_nations]: https://doi.org/10.1162/isec_a_00328
[journal_bell_miller_2015_questioning]: https://doi.org/10.1177/0022002713499718
[journal_bianchi_sosa_padilla_2025_sanctions_dollar]: https://doi.org/10.1093/ej/ueaf052
[journal_bleek_lorber_2014_security_guarantees]: https://doi.org/10.1177/0022002713509050
[journal_bolt_vanzanden_2024_maddison]: https://doi.org/10.1111/joes.12618
[journal_boughton_2001_northwest_of_suez]: https://doi.org/10.2307/4621678
[journal_boz_2022_invoicing_patterns]: https://doi.org/10.1016/j.jinteco.2022.103604
[journal_brooks_wohlforth_2016_rise_and_fall]: https://doi.org/10.1162/ISEC_a_00225
[journal_burrows_2026_china_war_scenario]: https://doi.org/10.1353/tns.00028
[journal_cancian_2025_states_of_denial]: https://doi.org/10.1080/00396338.2025.2481778
[journal_carroll_kenkel_2019_prediction_proxies]: https://doi.org/10.1111/ajps.12442
[journal_caverley_2025]: https://doi.org/10.1353/tns.00004
[journal_cederman_2011_testing_clausewitz]: https://doi.org/10.1017/s0020818311000245
[journal_chadefaux_2011_bargaining]: https://doi.org/10.1017/s175297191100008x
[journal_chang_2016_developing_expert_judgment]: https://doi.org/10.1017/s1930297500004599
[journal_chitu_2014_bond_markets]: https://doi.org/10.1016/j.jdeveco.2013.09.008
[journal_christensen_snyder_1990_chain_gangs]: https://doi.org/10.1017/S0020818300035232
[journal_cirillo_taleb_2016_tail_risk]: https://doi.org/10.1016/j.physa.2016.01.050
[journal_clauset_2018_trends_fluctuations]: https://doi.org/10.1126/sciadv.aao3580
[journal_collins_2018_maritime_oil_blockade]: https://digital-commons.usnwc.edu/nwc-review/vol71/iss2/6/
[journal_cooley_nexon_2013_empire_compensate]: https://doi.org/10.1017/S1537592713002818
[journal_cunningham_2026_escalate_to_survive]: https://doi.org/10.1162/isec.a.405
[journal_davis_gholz_2026_blockade_by_fire]: https://doi.org/10.1162/isec.a.407
[journal_davis_weinstein_2002_bones_bombs]: https://doi.org/10.1257/000282802762024502
[journal_dicicco_levy_1999_power_shifts]: https://doi.org/10.1177/0022002799043006001
[journal_doran_1989_systemic_disequilibrium]: https://doi.org/10.1177/0022002789033003001
[journal_doran_parsons_1980_war_cycle]: https://doi.org/10.2307/1954315
[journal_eichengreen_2015_stability_or_upheaval]: https://doi.org/10.1057/imfer.2015.19
[journal_eichengreen_2019_mars_or_mercury]: https://doi.org/10.1093/epolic/eiz005
[journal_eichengreen_flandreau_2009_rise_and_fall]: https://doi.org/10.1017/s1361491609990153
[journal_evangelista_2024_nuclear_umbrella]: https://doi.org/10.1162/isec_a_00476
[journal_farrell_newman_2019_weaponized]: https://doi.org/10.1162/isec_a_00351
[journal_fearon_1995_rationalist]: https://doi.org/10.1017/s0020818300033324
[journal_fitzpatrick_2025_farewell]: https://doi.org/10.1093/gerhis/ghaf028
[journal_fuhrmann_tkach_2015_nuclear_latency]: https://doi.org/10.1177/0738894214559672
[journal_gaddis_1986_long_peace]: https://doi.org/10.2307/2538951
[journal_gavin_2010_same_as_it_ever_was]: https://doi.org/10.1162/isec.2010.34.3.7
[journal_gerzhoy_2015_alliance_coercion]: https://doi.org/10.1162/isec_a_00198
[journal_gilpin_1988_hegemonic_war]: https://doi.org/10.2307/204816
[journal_gopinath_2020_dominant_currency_paradigm]: https://doi.org/10.1257/aer.20171201
[journal_gopinath_stein_2021_dominant_currency]: https://doi.org/10.1093/qje/qjaa036
[journal_green_talmadge_2022]: https://doi.org/10.1162/isec_a_00437
[journal_greitens_kardon_2025_security_without_exclusivity]: https://doi.org/10.1162/isec_a_00504
[journal_grieco_1988_anarchy_limits]: https://doi.org/10.1017/S0020818300027715
[journal_grieco_powell_snidal_1993_relative_gains]: https://doi.org/10.2307/2938747
[journal_hall_sargent_2011_interest_rate_risk]: https://doi.org/10.1257/mac.3.3.192
[journal_henry_2020_what_allies_want]: https://doi.org/10.1162/isec_a_00375
[journal_ikenberry_1999_institutions_restraint]: https://doi.org/10.1162/isec.23.3.43
[journal_ikenberry_2018_end_of_liberal_order]: https://doi.org/10.1093/ia/iix241
[journal_ikenberry_2024_three_worlds]: https://doi.org/10.1093/ia/iiad284
[journal_ikenberry_nexon_2019_hegemony_studies]: https://doi.org/10.1080/09636412.2019.1604981
[journal_ilzetzki_2020_euro_punching]: https://doi.org/10.1093/epolic/eiaa018
[journal_kadera_sorokin_2004_measuring_national_power]: https://doi.org/10.1080/03050620490492097
[journal_kang_ma_2018_power_transitions]: https://doi.org/10.1080/0163660X.2018.1445905
[journal_kitchen_cox_2019_structural_power]: https://doi.org/10.1080/09557571.2019.1606158
[journal_kugler_arbetman_1989_phoenix]: https://doi.org/10.1177/0022002789033001004
[journal_kuik_2008_essence_of_hedging]: https://doi.org/10.1355/cs30-2a
[journal_lake_2007_escape_state_of_nature]: https://doi.org/10.1162/isec.2007.32.1.47
[journal_lanteigne_2008_malacca_dilemma]: https://doi.org/10.1080/14799850802006555
[journal_levy_1987_declining_power]: https://doi.org/10.2307/2010195
[journal_lim_cooper_2015_reassessing_hedging]: https://doi.org/10.1080/09636412.2015.1103130
[journal_lim_ikenberry_2023_illiberal_hegemony]: https://doi.org/10.1080/09636412.2023.2178963
[journal_lind_2024_back_to_bipolarity]: https://doi.org/10.1162/isec_a_00494
[journal_markowitz_fariss_2013_going_the_distance]: https://doi.org/10.1080/03050629.2013.768458
[journal_mckinney_harris_2021_broken_nest]: https://doi.org/10.55540/0031-1723.3089
[journal_mearsheimer_2019_bound_to_fail]: https://doi.org/10.1162/isec_a_00342
[journal_mehta_whitlark_2017_latency]: https://doi.org/10.1093/isq/sqx028
[journal_menon_2026_new_world_order]: https://doi.org/10.1353/tns.00024
[journal_mirski_2013_stranglehold]: https://doi.org/10.1080/01402390.2012.743885
[journal_monteiro_debs_2014_strategic_logic]: https://doi.org/10.1162/isec_a_00177
[journal_morley_2026_thucydiocies]: https://doi.org/10.1017/pub.2026.10147
[journal_mueller_1988_essential_irrelevance]: https://doi.org/10.2307/2538971
[journal_narang_2017_strategies_of_proliferation]: https://doi.org/10.1162/isec_a_00268
[journal_nemeth_2026_suez_moment]: https://doi.org/10.1353/tns.00025
[journal_ohanian_1997_macroeconomic_effects_war_finance]: https://ideas.repec.org/a/aea/aecrev/v87y1997i1p23-40.html
[journal_organski_kugler_1977_phoenix]: https://doi.org/10.2307/1961484
[journal_platias_trigkas_2021_unravelling]: https://doi.org/10.1093/cjip/poaa023
[journal_posen_2003_command_of_the_commons]: https://doi.org/10.1162/016228803322427965
[journal_powell_1991_absolute_relative_gains]: https://doi.org/10.2307/1963947
[journal_powell_2006_commitment_problem]: https://doi.org/10.1017/s0020818306060061
[journal_priebe_2024_competing_visions]: https://doi.org/10.1162/isec_a_00498
[journal_rauchhaus_2009_nuclear_peace]: https://doi.org/10.1177/0022002708330387
[journal_sagan_1997_why_states_build]: https://doi.org/10.1162/isec.21.3.54
[journal_schroeder_1992_vienna_settlement]: https://doi.org/10.1086/ahr/97.3.683
[journal_sechser_fuhrmann_2013_nuclear_blackmail]: https://doi.org/10.1017/s0020818312000392
[journal_snidal_1991_relative_gains]: https://doi.org/10.2307/1963847
[journal_snyder_1984_security_dilemma]: https://doi.org/10.2307/2010183
[journal_tomz_weeks_2021_military_alliances]: https://doi.org/10.1093/isq/sqab015
[journal_trachtenberg_2025_rules_based_order]: https://doi.org/10.1162/isec.a.11
[journal_verschuur_2025_chokepoints]: https://doi.org/10.1038/s41467-025-65403-w
[journal_von_hippel_2019_naval_propulsion]: https://doi.org/10.1080/25751654.2019.1625504
[journal_walt_2025_hedging_hegemony]: https://doi.org/10.1162/isec_a_00508
[journal_welch_2003_stop_reading_thucydides]: https://doi.org/10.1017/S0260210503003012
[reference_tammen_2017_foundations]: https://doi.org/10.1093/acrefore/9780190228637.013.296
[related_post_published_wargames]: {% post_url 2026-08-11-published_wargames_of_war_with_china %}
[related_post_rebuilding]: {% post_url 2026-08-12-rebuilding_after_war_with_china %}
[research_albright_2018_taiwan_nuclear_program]: https://isis-online.org/uploads/isis-reports/documents/TaiwansFormerNuclearWeaponsProgram_POD_color_withCover.pdf
[research_atlantic_council_2025_welcome_2035]: https://www.atlanticcouncil.org/content-series/atlantic-council-strategy-paper-series/welcome-to-2035/
[research_atlantic_council_2026_welcome_2036]: https://www.atlanticcouncil.org/content-series/atlantic-council-strategy-paper-series/welcome-to-2036/
[research_bianchi_2023_sanctions_dollar]: https://doi.org/10.3386/w31024
[research_cancian_2023_first_battle]: https://www.csis.org/analysis/first-battle-next-war-wargaming-chinese-invasion-taiwan
[research_crawford_2021_budgetary_costs]: https://costsofwar.watson.brown.edu/sites/default/files/papers/Costs-of-War_US-Budgetary-Costs-of-Post-9-11-Wars.pdf
[research_dooley_2022_sanctions_reinforce]: https://doi.org/10.3386/w29943
[research_ecfr_2023_a_la_carte]: https://ecfr.eu/publication/living-in-an-a-la-carte-world-what-european-policymakers-should-learn-from-global-public-opinion/
[research_edwards_2010_war_costs]: https://doi.org/10.3386/w16108
[research_eichengreen_2005_sterlings_past]: https://doi.org/10.3386/w11336
[research_evans_2023_alternative_futures_v2]: https://www.rand.org/pubs/research_reports/RRA591-2.html
[research_fariss_2017_latent_estimation]: https://arxiv.org/abs/1706.01099
[research_goes_bekkers_2022_geopolitical_conflicts]: https://www.wto.org/english/res_e/reser_e/ersd202209_e.pdf
[research_gompert_2016_war_with_china]: https://doi.org/10.7249/RR1140
[research_hall_sargent_2020_debt_and_taxes]: https://doi.org/10.3386/w27115
[research_harrison_1998_economics_of_wwii]: https://warwick.ac.uk/fac/soc/economics/staff/mharrison/public/ww2overview1998.pdf
[research_hohn_2014_geopolitics_measurement]: https://ediss.sub.uni-hamburg.de/handle/ediss/5238
[research_jiang_2026_dollar_erosion]: https://doi.org/10.3386/w35328
[research_kwende_nephew_2025_cofer]: https://doi.org/10.5089/9798229004855.005
[research_nordhaus_2002_iraq_cost]: https://doi.org/10.3386/w9361
[research_nsarchive_2019_taiwans_bomb]: https://nsarchive.gwu.edu/briefing-book/nuclear-vault/2019-01-10/taiwans-bomb
[research_priebe_2023_alternative_futures_v1]: https://www.rand.org/pubs/research_reports/RRA591-1.html
[research_priebe_frederick_2023_conversation]: https://www.rand.org/pubs/commentary/2023/05/alternative-futures-following-a-great-power-war-miranda.html
[research_reinhart_sbrancia_2011_liquidation]: https://doi.org/10.3386/w16893
[research_rhodium_2022_taiwan_disruptions]: https://rhg.com/research/taiwan-economic-disruptions/
[research_rockoff_2004_until_its_over]: https://doi.org/10.3386/w10580
[research_tarapore_2024_deterring_attack]: https://www.aspi.org.au/report/deterring-attack-taiwan-policy-options-india-and-other-non-belligerent-states/
[research_tellis_2000_measuring_national_power]: https://doi.org/10.7249/mr1110
[research_vest_kratz_2023_sanctioning_china]: https://www.atlanticcouncil.org/in-depth-research-reports/report/sanctioning-china-in-a-taiwan-crisis-scenarios-and-risks/
[research_weiss_2022_geopolitics_dollar]: https://doi.org/10.17016/IFDP.2022.1359
[research_weiss_2025_dedollarization]: https://doi.org/10.17016/IFDP.2025.1420
