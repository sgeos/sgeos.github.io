---
layout: post
mathjax: true
comments: true
title: "What Published Wargames Say About a War With China"
date: 2026-08-11 09:00:00 +0000
categories: geopolitics military war-gaming
---

<!-- A374 -->
<script>console.log("A374");</script>

A recurring argument holds that the People's Republic of China,
or PRC,
faces a demographic and economic decline
that could tempt its leadership to use force against Taiwan
before the balance of power moves against it.
If that argument is accepted as a premise,
the natural next question is what the public analytical record says would happen in such a war.

This article answers that question by reading the published wargames and the econometric estimates that accompany them.
It began as an exchange with an external large language model,
which produced a confident summary of the literature.
Every claim in that summary was checked here against the primary reports,
and several did not survive.
The corrections are listed in the Epistemic State section,
because the way a plausible summary diverges from its sources is itself part of the finding.

The article does not forecast whether a war will happen,
does not argue for or against any policy toward Taiwan,
and does not treat a wargame outcome as a probability.
The authors of the reports make the same disclaimer,
and the article holds them to it.
The equations that follow are arithmetic on published figures.
They check whether the numbers in the reports agree with one another
and express the comparisons the prose makes,
and none of them is a model of a war.
Readers who want the economic background may start with the
[account of China's rise in the industrialization series][related_post_china_rise]
and its
[closing snapshot and extrapolation][related_post_industrialization_snapshot].
Readers interested in why wargames are useful at all may find the
[discussion of metagaming as strategy][related_post_metagaming]
a helpful companion.

## The Premise, Demography and the Closing Window

### What the demographic data show

The National Bureau of Statistics of China reported a year-end 2025 population of 1,404.89 million,
a decrease of 3.39 million from the end of 2024,
in its [statistical communiqué on 2025][data_nbs_2025_communique].
There were 7.92 million births at a crude birth rate of 5.63 per thousand
and 11.31 million deaths at a crude death rate of 8.04 per thousand.

The first check is the population balance.
Let $P_0$ be the year-end 2024 population and $P_1$ the year-end 2025 population,
both in millions,
let $B$ and $D$ be the births and deaths during 2025 in millions,
and let $M$ be net international migration in millions,
which the communiqué does not report.
The bureau's
[communiqué for 2024][data_nbs_2024_communique]
states the year-end 2024 population directly as 1,408.28 million,
which is also what the 2025 decrease implies,
since $1{,}404.89 + 3.39 = 1{,}408.28$.

$$
P_1 = P_0 + B - D + M
$$

Substituting the published values gives the migration term the other figures imply.

$$
1{,}404.89 = 1{,}408.28 + 7.92 - 11.31 + M
\quad\Rightarrow\quad
M \approx 0.00
$$

Births less deaths account for the entire reported decrease to the precision published,
so the decline is natural decrease and not emigration.

The same balance closes for the year before.
The 2024 communiqué reports 9.54 million births and 10.93 million deaths
against a decrease of 1.39 million.

$$
B_{2024} - D_{2024} = 9.54 - 10.93 = -1.39
$$

Natural decrease accounts for the whole of that year as well.
Setting the two decreases side by side shows how fast the decline is steepening.

$$
\frac{3.39}{1.39} \approx 2.44
$$

The 2025 decrease is roughly two and a half times the 2024 decrease,
which is a sharper change than the smallness of either figure suggests.

The second check is the crude rates.
Let $\bar{P}$ be the mean population over the year in millions,
taken as the average of the two year-end figures,
and let $b$ and $d$ be the crude birth and death rates per thousand population.

$$
\bar{P} = \frac{P_0 + P_1}{2},
\qquad
b = 1000 \, \frac{B}{\bar{P}},
\qquad
d = 1000 \, \frac{D}{\bar{P}}
$$

With $\bar{P} = 1{,}406.585$ million,
the rates follow.

$$
b = 1000 \times \frac{7.92}{1{,}406.585} \approx 5.63,
\qquad
d = 1000 \times \frac{11.31}{1{,}406.585} \approx 8.04
$$

Both match the published rates,
so the communiqué uses a mid-year denominator close to the simple average.
The natural growth rate $r_n$ per thousand is the difference of the two rates.

$$
r_n = b - d = 5.63 - 8.04 = -2.41 \ \text{per thousand}
$$

That also matches the printed figure.
As a proportion of the starting population the annual decline is small.

$$
\frac{3.39}{1{,}408.28} \approx 0.24 \ \text{percent}
$$

The demographic argument therefore rests on the direction and persistence of the trend
rather than on the size of a single year's change.

Marriage registrations are a leading indicator of births in China,
because births outside marriage remain uncommon.
[Reuters reported][news_reuters_marriages_2024]
that registrations fell to a little over 6.1 million in 2024 from 7.68 million in 2023,
citing Ministry of Civil Affairs figures.
Writing $m_{2023}$ and $m_{2024}$ for the registrations in millions,
the proportional decline is as follows.

$$
\frac{m_{2023} - m_{2024}}{m_{2023}} = \frac{7.68 - 6.1}{7.68} \approx 0.206
$$

The ministry's own bulletin,
reported through the
[State Council Information Office][data_scio_2025_marriage_registrations],
puts the 2024 figure at 6.106 million registrations,
a fall of 20.5 percent,
with a marriage rate of 4.3 per thousand people
and 3.513 million divorces concluded.
The precise count confirms the decline of about a fifth
and allows two further checks.
The marriage rate should be the registrations against the year-end population.

$$
1000 \times \frac{6.106}{1{,}408.28} \approx 4.34 \ \text{per thousand}
$$

That agrees with the published 4.3.
The ratio of divorces concluded to marriages registered follows from the same bulletin.

$$
\frac{3.513}{6.106} \approx 0.575
$$

The bulletin's account also names the cause that demography alone would predict.
The population aged 20 to 39,
the core marrying ages,
fell from about 435 million in 2013 to about 371 million in 2023.

$$
435 - 371 = 64 \ \text{million},
\qquad
\frac{64}{435} \approx 0.147
$$

A seventh of the marrying-age cohort disappeared in a decade,
so part of the fall in marriages is arithmetic before it is anything about preferences.

A RAND Corporation study,
[Pollard, Bouey, Wang and Pandey 2025][research_pollard_2025_fertility_decline],
projects the old age dependency ratio.
Let $N_{65+}$ be the number of people aged 65 and older
and $N_{15\text{ to }64}$ the number aged 15 to 64.

$$
R_{\text{old}} = \frac{N_{65+}}{N_{15\text{ to }64}}
$$

The study projects $R_{\text{old}}$ rising from 0.21 in 2024 to 0.52 by 2050.

$$
\frac{0.52}{0.21} \approx 2.48
$$

The ratio therefore more than doubles.
Spread over the 26 years between the two dates,
the implied compound growth rate $g$ per year is as follows.

$$
g = \left( \frac{0.52}{0.21} \right)^{1/26} - 1 \approx 0.0355
$$

The ratio grows by about 3.5 percent a year.
Its reciprocal is easier to picture,
since it counts working-age adults for each person aged 65 and older.

$$
\frac{1}{R_{\text{old}}} \approx
\begin{cases}
4.76 & \text{in 2024} \\
1.92 & \text{in 2050}
\end{cases}
$$

Fewer than two working-age adults would stand behind each older person by 2050,
which is the fiscal pressure the premise relies on.
The same study lists broad strain on government finances
and rising pension and health care costs
among the structural security implications of the trend.

### What the data do not yet show

The premise is often extended to claim that the People's Liberation Army,
or PLA,
already faces a shrinking pool of recruits.
The RAND study does not support that claim for the near term.
Its experts expected the impact of demographic decline on PLA readiness and personnel levels
to be minimal over the next decade,
noted that economic downturns have historically increased enlistment,
and placed the force size concern for large ground operations in the decades ahead.
A United States Naval War College report on PLA Navy recruiting,
[Richter and Arostegui 2026][research_richter_2026_filling_the_ranks],
identifies low physical fitness among potential recruits as a problem
and documents a rising share of recruits with college degrees.
Fitness and talent competition are real constraints.
A contracting cohort is a long-run constraint and not yet a binding one.

### The closing window argument and its critics

The strategic form of the premise is most closely associated with Hal Brands and Michael Beckley,
who argued in a
[2021 Foreign Policy essay][commentary_brands_beckley_2021_declining_power]
and in the book
[Danger Zone][commentary_brands_beckley_2022_danger_zone]
that a China which has peaked
is more dangerous than a rising one,
because it may conclude that its opportunity is closing.
They call the situation a peaking power trap
and write that China "will be sorely tempted to use force to resolve the Taiwan question on its terms in the next decade
before Washington and Taipei can finish retooling their militaries".
Their demographic figure is that from 2020 to 2050
China loses about 200 million working-age adults and gains about 200 million senior citizens.
That figure can be checked against the RAND projection used above.
RAND puts the working-age population at 745 million in 2050,
so a loss of 200 million implies a 2020 base of about 945 million.

$$
745 + 200 = 945
$$

O'Hanlon's independent account has the working-age population peaking above 900 million in 2011
and falling to roughly 700 million by mid-century,
a decline of about the same 200 million.
Three sources therefore agree on the magnitude while differing on the baseline year.
[Howard 2026][commentary_howard_2026_peaked_power]
restates the argument
and adds that depleted American precision munitions could make the environment more permissive for preventive action.

The argument has serious critics.
[Mastro and Scissors 2022][commentary_mastro_scissors_2022_peak]
wrote that "current income and defense spending trajectories suggest that China will have more resources
to compete militarily with the United States over the next ten years than it has had over the last 20",
so that Beijing has space to bide its time.
[O'Hanlon 2023][commentary_ohanlon_2023_shrinking_population]
at the Brookings Institution
agreed that demography will constrain Chinese power
but rejected the inference that this makes near-term aggression likely,
pointing to the difficulty of a decisive victory in a great-power war.
[Medeiros 2024][commentary_medeiros_2024_delusion_peak_china]
called the peak thesis a delusion that underrates a durable competitor.
His objection is about perception more than about statistics.
"Xi still believes China is rising, and he is acting accordingly," he writes,
adding that China peaking economically is not the same as China peaking geopolitically,
a distinction he says many advocates of the argument lose.
If the premise of this article is a leadership that acts on a belief about decline,
then Medeiros is denying the belief as well as the decline.

The external summary that prompted this article attributed the closing window argument to Brookings.
The Brookings piece found for this article argues against the inference.
That misattribution is recorded in the Epistemic State section.

The official American assessment sides with the critics on the narrow question of timing.
The [threat assessment of the United States intelligence community][government_odni_2026_threat_assessment],
prepared with information available as of 14 March 2026,
states that "Chinese leaders do not currently plan to execute an invasion of Taiwan in 2027,
nor do they have a fixed timeline for achieving unification".
An article built on the premise of a closing window
should say early that the body charged with assessing Chinese intent does not see one.

### What Beijing states in its own documents

The wargames model an attempt to take Taiwan by force,
and the PRC's own published position is the primary source for whether that is contemplated at all.
The 2022 white paper
[The Taiwan Question and China's Reunification in the New Era][government_prc_2022_taiwan_white_paper],
issued by the Taiwan Affairs Office of the State Council and the State Council Information Office,
states that peaceful reunification is the first choice of the Communist Party of China,
which the document calls the CPC,
and of the Chinese government,
the full sentence reading that "national reunification by peaceful means is the first choice
of the CPC and the Chinese government in resolving the Taiwan question".
It also states that "we will not renounce the use of force,
and we reserve the option of taking all necessary measures",
which it frames as guarding against external interference and separatist activity.
The document neither announces a timetable nor concedes one.
It establishes that force is retained as an option and preference is stated for the alternative,
which is the minimum the scenarios above assume and no more than that.

## Which Wargames Are Public

Much of the wargaming of a war with China is classified and not open to public scrutiny.
The public record consists of a small number of think tank projects
from the RAND Corporation,
the Center for a New American Security or CNAS,
the Center for Strategic and International Studies or CSIS,
and the Heritage Foundation,
and most of them model the same scenario,
an attempt by the PRC to take Taiwan by force.
The nuclear study among them was a joint project of CSIS
and the Massachusetts Institute of Technology,
which the table shortens to MIT.
The table lists the projects this article draws on.

<div style="overflow-x: auto;" markdown="1">

| Project | Sponsor | Published | Scenario year | Runs | Method |
|---|---|---|---|---|---|
| War with China | RAND | 2016 | 2015 and 2025 | Analytic cases | Structured assessment of four war types |
| Dangerous Straits | CNAS | June 2022 | 2027 | One high-level game | Strategic and operational seminar game |
| The First Battle of the Next War | CSIS | January 2023 | 2026 | 24 | Rules-based operational game |
| Confronting Armageddon | CSIS and MIT | December 2024 | 2028 | 15 | The 2023 game with nuclear rules added |
| Lights Out | CSIS | July 2025 | Blockade scenarios | 26 | Escalation-matrix game plus free play |
| TIDALWAVE | Heritage Foundation | January 2026 | Longer than six months | Not stated in the archived summary | Computer simulation described as enabled by artificial intelligence |
| TIDALWAVE II, Azure Dragon | Heritage Foundation | January 2026 | 2030 | One tabletop exercise | Nuclear escalation exercise |

</div>

The scenario years cluster between 2026 and 2030,
and the origin of that clustering is a matter of record.
On 9 March 2021,
at the Senate Committee on Armed Services
[hearing on United States Indo-Pacific Command][government_sasc_2021_indopacom],
Admiral Philip Davidson told Senator Dan Sullivan that
"I think the threat is manifest during this decade, in fact, in the next six years".
Counting from the year of that testimony gives the date the literature returns to.

$$
2021 + 6 = 2027
$$

The Heritage summary discussed below says in its own words that
"many insiders point to 2027 as the year for a potential conflict between China and the U.S."
The scenario years are therefore anchored to a statement about military capability timelines,
made by a commander in open testimony.
**None of the reports read here ties its scenario year to demographic projections**,
so the external summary's suggestion that the timing reflects a demographic peak
is not supported by these sources.

## The Invasion Result

### What the CSIS game found

[Cancian, Cancian and Heginbotham 2023][research_cancian_2023_first_battle]
built a rules-based wargame of a Chinese amphibious invasion of Taiwan in 2026
and ran it 24 times.
Their summary finding is that in most scenarios
the United States, Taiwan and Japan defeated the invasion and preserved an autonomous Taiwan,
at a high cost to every party.

The report sorts its iterations into scenario families.
Three base iterations used the most likely assumptions,
eighteen pessimistic iterations used assumptions favorable to China,
two optimistic iterations used assumptions favorable to the defenders,
and one iteration had Taiwan fight with no American intervention.
Writing $N$ for the total and a subscript for each family,
the counts reconcile with the stated total.

$$
N = N_{\text{base}} + N_{\text{pess}} + N_{\text{opt}} + N_{\text{alone}} = 3 + 18 + 2 + 1 = 24
$$

The outcomes are less one-sided than the summary finding suggests.
All three base iterations and both optimistic iterations ended in decisive Chinese defeat.
Of the eighteen pessimistic iterations,
four ended in decisive Chinese defeat
and fourteen ended in stalemate,
of which three were judged to be trending toward China,
seven trending against China,
and four indeterminate.
The single iteration without American intervention ended in a PLA victory,
with PLA armor reaching the presidential office in Taipei after ten weeks.

$$
24 = \underbrace{(3 + 2 + 4)}_{\text{decisive defeat}} + \underbrace{14}_{\text{stalemate}} + \underbrace{1}_{\text{PLA victory}},
\qquad
14 = 3 + 7 + 4
$$

Let $f_k$ be the fraction of all iterations ending in outcome $k$,
with $n_k$ the count of such iterations.

$$
f_k = \frac{n_k}{N}
$$

The three outcome classes then take the following shares.

$$
f_{\text{defeat}} = \frac{9}{24} = 0.375,
\qquad
f_{\text{stalemate}} = \frac{14}{24} \approx 0.583,
\qquad
f_{\text{victory}} = \frac{1}{24} \approx 0.042
$$

Stalemate was the most common single outcome across the project.
Within the pessimistic family alone,
decisive defeat fell to a little over a fifth.

$$
\frac{4}{18} \approx 0.22
$$

No iteration with prompt American intervention and access to bases in Japan produced a Chinese occupation of Taipei.
These fractions describe how the designers distributed their runs across assumptions,
and the Limits section explains why they are not probabilities.

The report also describes a deliberately extreme scenario called Ragnarok,
built to find the conditions under which China wins despite intervention,
which also ended in PLA victory.
The report does not state how many times Ragnarok was run,
and the four stated family counts already sum to 24,
so its place in the total could not be reconciled from the text.

The report states four conditions that the defense needed in every successful case.
Taiwan must resist and not capitulate.
The United States must join the fighting within days and with its full capabilities,
because there is no Ukraine model in which supplies alone suffice for an island that China can isolate.
The United States must be able to fight from its bases in Japan.
The United States must have enough long-range anti-ship missiles to strike the Chinese fleet from outside its defenses.

### Losses in the base scenario

The base scenario averages in the report's loss table are shown here.

| Party | Combat aircraft lost | Ships lost |
|---|---|---|
| United States | 270 | 17 |
| Japan | 112 | 26 |
| United States and Japan combined | 382 | 43 |
| China | 155 | 138 |

The combined row is the sum of the two national rows,
which confirms the table is internally consistent.
Let $A$ denote average combat aircraft lost and $S$ average ships lost,
with a subscript for the party.

$$
A_{\text{US}} + A_{\text{JP}} = 270 + 112 = 382,
\qquad
S_{\text{US}} + S_{\text{JP}} = 17 + 26 = 43
$$

In every base iteration the United States lost two aircraft carriers
and between seven and twenty other major surface warships.
About ninety percent of American, Japanese and Taiwanese aircraft losses occurred on the ground,
destroyed by missiles at crowded and unhardened bases.
Taiwan lost all 26 ships of its navy and roughly half of its operational air force.
The report estimates that in three weeks the United States would suffer about half as many casualties as in twenty years of war in Iraq and Afghanistan.

China's naval losses averaged 138 major ships,
of which 86 were amphibious ships and 52 other major surface warships.
The report states that the 86 amphibious ships were about ninety percent of the amphibious fleet in the game.
Writing $S_{\text{amph}}$ for amphibious ships lost,
$S_{\text{other}}$ for other major warships lost,
and $F_{\text{amph}}$ for the size of the amphibious fleet,
the composition and the implied fleet size follow.

$$
S_{\text{CN}} = S_{\text{amph}} + S_{\text{other}} = 86 + 52 = 138,
\qquad
F_{\text{amph}} \approx \frac{S_{\text{amph}}}{0.9} = \frac{86}{0.9} \approx 96
$$

The game's Chinese amphibious fleet was therefore on the order of ninety to one hundred ships,
and amphibious ships made up about 62 percent of China's naval losses.

$$
\frac{S_{\text{amph}}}{S_{\text{CN}}} = \frac{86}{138} \approx 0.62
$$

The invasion was defeated by sinking its lift,
which is why transports make up most of the ship loss count.

Two exchange ratios summarize the naval and air fighting.
Let $E_S$ be Chinese ships lost per coalition ship lost
and $E_A$ Chinese aircraft lost per coalition aircraft lost,
where the coalition is the United States and Japan together.

$$
E_S = \frac{S_{\text{CN}}}{S_{\text{US}} + S_{\text{JP}}} = \frac{138}{43} \approx 3.2,
\qquad
E_A = \frac{A_{\text{CN}}}{A_{\text{US}} + A_{\text{JP}}} = \frac{155}{382} \approx 0.41
$$

China lost about three ships for every coalition ship
while the coalition lost more than twice as many aircraft as China,
mostly on the ground.

The report's text gives Chinese aircraft losses as averaging 161 per iteration,
while its table gives 155.
The discrepancy is small and is reported here as found.

For personnel,
the report estimates about 7,000 Chinese casualties in ground combat,
roughly a third assumed killed,
and about 15,000 soldiers lost at sea,
half assumed killed.
Let $K$ be the implied number of Chinese dead.

$$
K \approx \frac{7000}{3} + \frac{15000}{2} \approx 2{,}300 + 7{,}500 \approx 9{,}800
$$

The report adds that many,
and probably an overwhelming majority,
of the more than 30,000 Chinese survivors on Taiwan would likely become prisoners.
Let $C$ be the number captured.
Because neither the share captured nor the exact survivor count is given,
the sum is an order of magnitude and not a bound.

$$
K + C \sim 9{,}800 + 30{,}000 \approx 40{,}000
$$

The phrase tens of thousands of troops killed or captured is therefore accurate for killed and captured together,
and not for killed alone.

In the pessimistic scenarios,
those more favorable to China,
losses rose for most parties.
The report's pessimistic averages are 484 aircraft for the United States,
161 for Japan,
and 327 for China,
with ship losses of 14 for the United States,
14 for Japan,
and 113 for China.
Let $\mu$ be the ratio of a pessimistic average to the corresponding base average.

$$
\mu_{A,\text{US}} = \frac{484}{270} \approx 1.79,
\qquad
\mu_{A,\text{CN}} = \frac{327}{155} \approx 2.11,
\qquad
\mu_{S,\text{CN}} = \frac{113}{138} \approx 0.82
$$

Worse assumptions for the defenders roughly doubled China's aircraft losses
while reducing its ship losses,
because more of its fleet survived long enough to land troops.
The exchange ratios move accordingly.

$$
E_S^{\text{pess}} = \frac{113}{14 + 14} \approx 4.0,
\qquad
E_A^{\text{pess}} = \frac{327}{484 + 161} \approx 0.51
$$

The fighting became bloodier in the air for every party,
the attacker included.

### The pyrrhic victory warning

The report's authors warn that the United States might win a pyrrhic victory,
suffering more in the long run than the defeated side,
and that the perception of high costs might itself undermine deterrence.
They also note that failure to occupy Taiwan might destabilize Chinese Communist Party rule.
That second observation becomes important in the nuclear results below.

## Escalation and Nuclear Use

### Dangerous Straits

[Pettyjohn, Wasser and Dougherty 2022][research_pettyjohn_2022_dangerous_straits]
reported a game run by the CNAS Gaming Lab with NBC's Meet the Press,
set in 2027.
The game found no quick victory for either side.
Neither Beijing nor Washington held the upper hand after the first week,
which the authors read as pointing to a protracted conflict.
China faced a dilemma between keeping the war limited in the hope that the United States stayed out
and striking American forces preemptively at the cost of a longer war.
The team playing China brandished nuclear weapons
and conducted a high-altitude nuclear demonstration near Hawaii,
despite China's declared policy of no first use.
The authors caution that a single game cannot establish how likely such a step would be.

### Confronting Armageddon

[Cancian, Cancian and Heginbotham 2024][research_cancian_2024_confronting_armageddon]
added nuclear rules to the 2023 game,
moved it to 2028,
and ran it fifteen times.
The outcomes were as follows.

| Outcome | Games |
|---|---|
| PLA phased withdrawal under a ceasefire | 5 |
| Status quo ante | 1 |
| Strategic nuclear exchange | 3 |
| Ceasefire leaving a PRC enclave on Taiwan | 5 |
| Inconclusive at end of play | 1 |

$$
5 + 1 + 3 + 5 + 1 = 15
$$

In twelve games the China team reached a crisis as its invasion force faced defeat,
and in seven of those the China team recommended nuclear use.
Of eight cases of nuclear use across the project,
seven were Chinese first use when the China team faced conventional defeat and chose to gamble for resurrection.
The eighth was an American team that mistakenly believed it was losing.
China teams that went nuclear employed between twelve and thirty weapons in those cases.

The sequence can be written as a chain of observed frequencies.
Let $G$ be the number of games,
$G_c$ the games in which the China team reached a crisis,
$G_n$ the games in which it recommended nuclear use,
$U$ the cases of nuclear use,
and $U_{\text{CN}}$ the cases of Chinese first use facing conventional defeat.

$$
\frac{G_c}{G} = \frac{12}{15} = 0.80,
\qquad
\frac{G_n}{G_c} = \frac{7}{12} \approx 0.58,
\qquad
\frac{U_{\text{CN}}}{U} = \frac{7}{8} = 0.875
$$

A China team that reached a crisis recommended nuclear use a little more often than not,
and nearly all nuclear use began that way.
The seven recommendations then resolved as follows.

$$
7 = \underbrace{2}_{\text{United States withdrew}} + \underbrace{1}_{\text{total counterforce, enclave}} + \underbrace{3}_{\text{countervalue, conflagration}} + \underbrace{1}_{\text{strike on operational targets}}
$$

Countervalue responses against Chinese cities always escalated to the deaths of hundreds of millions.
A limited American nuclear strike against Chinese forces on and around Taiwan
did not surrender Taiwan and did not lead inevitably to strikes on cities.
The report finds that no set of circumstances produced a complete victory for either side,
and that conventional strikes on the Chinese mainland did not by themselves provoke a nuclear response in the games.
It states plainly that the probability of nuclear use cannot be inferred from its results,
and the frequencies above are subject to the same caution.

The nuclear study also reports that by the end of the first week
the United States and Japan had usually lost 270 aircraft and 20 ships,
including two carriers.
Setting that against the three-week base averages of the 2023 game gives a rough sense of how front-loaded the losses are.

$$
\frac{270}{382} \approx 0.71,
\qquad
\frac{20}{43} \approx 0.47
$$

About seven in ten aircraft losses and about half of ship losses would fall in the first week.
The two figures come from different scenario years and game versions,
so the comparison is indicative only.

### TIDALWAVE II

The Heritage Foundation's
[report on a limited nuclear war over Taiwan][research_heritage_2026_limited_nuclear_war]
describes a tabletop exercise that introduced nuclear escalation three weeks into a 2030 conflict.
As summarized on the foundation's page,
the exercise found compelling pressures for theater nuclear use,
found that escalation could be contained below a large strategic exchange,
found that theater nuclear war could prove indecisive and protracted,
and found American shortfalls in both conventional precision munitions and non-strategic nuclear weapons.
The full report could not be retrieved for this article,
so these findings rest on the summary alone.

## Blockade Instead of Invasion

The external summary described an invasion as the scenario the games examine.
CSIS also examined the alternative most often named as more likely.
[Cancian, Cancian and Heginbotham 2025][research_cancian_2025_lights_out]
ran twenty-one blockade games across a matrix of Chinese and coalition escalation levels
plus five free-play games,
and declined to name winners.

$$
21 + 5 = 26
$$

Almost every scenario produced casualties,
in the thousands even at low escalation.
At higher escalation the United States lost hundreds of aircraft and dozens of warships,
and Chinese losses were often higher than American ones.
In the base variant where China used submarines and mines
and Taiwan fought assertively without American combat forces,
coalition casualties were 2,256 and Chinese casualties were 206.
In the base variant of a wider war on both sides
they were 20,529 and 13,515.
Let $L_{\text{co}}$ and $L_{\text{CN}}$ be coalition and Chinese casualties,
with superscripts for the lower and the wider war variant.

$$
\frac{L_{\text{co}}^{\text{wide}}}{L_{\text{co}}^{\text{low}}} = \frac{20{,}529}{2{,}256} \approx 9.1,
\qquad
\frac{L_{\text{CN}}^{\text{wide}}}{L_{\text{CN}}^{\text{low}}} = \frac{13{,}515}{206} \approx 65.6
$$

Escalation raised China's losses proportionally far more than the coalition's.
The casualty exchange ratio shows the same shift from the other direction.

$$
\frac{L_{\text{co}}^{\text{low}}}{L_{\text{CN}}^{\text{low}}} = \frac{2{,}256}{206} \approx 11.0,
\qquad
\frac{L_{\text{co}}^{\text{wide}}}{L_{\text{CN}}^{\text{wide}}} = \frac{20{,}529}{13{,}515} \approx 1.52
$$

In a submarine and mine blockade the defenders absorbed about eleven casualties for each Chinese casualty,
while in a wider war the ratio approached parity.
A low-level blockade is cheap for China in lives,
and escalating it removes most of that advantage.

Any blockade created escalatory pressures that were difficult to contain,
and two of the five free-play games spiraled into general war,
with American missiles striking the Chinese mainland and Chinese missiles striking Guam and Japan.
Without American intervention,
Chinese submarines and mines destroyed forty percent of ships inbound to Taiwan.

The report gives that loss as a rate per inbound voyage.
If one assumes,
as the report does not,
that each voyage faces the same independent chance of loss,
the probability $p_k$ that a single merchant ship survives $k$ inbound voyages follows.

$$
p_k = (1 - 0.4)^k = 0.6^k,
\qquad
p_2 = 0.36,
\qquad
p_4 \approx 0.13
$$

Under that assumption a ship making only two runs would already be more likely than not to be sunk,
which illustrates the report's finding that commercial shipping would not accept the risk
and that acquiring ships to run the blockade was critical.
The independence assumption is this article's and not the report's.

Energy was the decisive shortfall.
Natural gas ran out in about ten days in every scenario,
coal in about seven weeks,
and oil in about twenty weeks without resupply.
For a stockpile $I$ drawn down at a consumption rate $c$ and replenished at a resupply rate $s$,
the exhaustion time $T$ is the stock divided by the net drawdown.

$$
T = \frac{I}{c - s}, \qquad c > s
$$

The report states exhaustion times and not stocks and rates,
so the equation is used here only to compare them.
Taking seven weeks as 49 days and twenty weeks as 140 days,
coal and oil lasted about five and fourteen times as long as gas.

$$
\frac{T_{\text{coal}}}{T_{\text{gas}}} = \frac{49}{10} \approx 4.9,
\qquad
\frac{T_{\text{oil}}}{T_{\text{gas}}} = \frac{140}{10} = 14
$$

Because gas runs out first,
the reduction in electricity comes before any shortage of fuel for transport.
Food was not a problem.
The report concludes that a blockade is not a low-cost, low-risk option for China
and is also a poor precursor to invasion,
because it alerts other states and costs China assets it would need for a landing.

## Munitions and Sustainment

### The CSIS munitions finding

[Jones 2023][research_jones_2023_empty_bins]
drew on the invasion game to assess the American defense industrial base.
Across nearly two dozen iterations the United States expended more than 5,000 long-range missiles in a typical three weeks of fighting.
The components are the Joint Air-to-Surface Standoff Missile or JASSM,
the Long Range Anti-Ship Missile or LRASM,
the Harpoon anti-ship missile,
and the Tomahawk Land Attack Missile or TLAM.

$$
4000_{\text{JASSM}} + 450_{\text{LRASM}} + 400_{\text{Harpoon}} + 400_{\text{TLAM}} = 5250
$$

The sum confirms the report's more than 5,000.
Spread over twenty-one days,
the average expenditure rate $\dot{m}$ across all four types follows.

$$
\dot{m} = \frac{5250}{21} = 250 \ \text{missiles per day}
$$

The Long Range Anti-Ship Missile was a small share of the total by number.

$$
\frac{450}{5250} \approx 0.086
$$

It still mattered most,
because it could strike ships from outside Chinese air defenses.
In every iteration the United States expended its inventory of Long Range Anti-Ship Missiles within the first week,
and the invasion report projected an inventory of roughly 450 for 2026.
Writing $I_{\text{LRASM}}$ for that inventory
and $T_{\text{ex}}$ for the time it lasts,
the exhaustion relation is the same as for the energy stocks,
with no resupply during the fighting.

$$
T_{\text{ex}} = \frac{I_{\text{LRASM}}}{\dot{m}_{\text{LRASM}}} \le 7 \ \text{days}
\quad\Rightarrow\quad
\dot{m}_{\text{LRASM}} \ge \frac{450}{7} \approx 64 \ \text{missiles per day}
$$

The rate is a lower bound because the inventory was gone within the week, possibly well before its end.
Jones summarizes the finding as the United States likely running out of some long-range precision munitions in less than one week.

### TIDALWAVE

The Heritage Foundation's TIDALWAVE project,
released in January 2026 according to
[Newsweek][news_newsweek_2026_tidalwave_redactions],
is the most pessimistic public result for the United States.
It is described by the foundation as a simulation enabled by artificial intelligence
that models an extended conflict longer than six months,
built from open sources,
and focused on fuel and munitions.
The foundation's
[live pages][research_heritage_2026_tidalwave]
refuse automated retrieval.
An archived copy of the
[executive summary][research_greenway_2026_tidalwave_archived],
captured on 14 April 2026 and bylined Robert Greenway and Anna Gustafson,
is the primary text used here.
It describes an artificial-intelligence-enabled simulation of an escalation scenario longer than six months,
built on more than 7,000 open sources reviewed by experts,
with four models covering United States fuel, United States munitions, PLA fuel and PLA munitions.
The outputs are first-deficit days,
collapse windows,
and the magnitude and location of unmet demand.

**The archived summary does not contain the figures most widely quoted from this project.**
The claims that the United States culminates in less than half the PRC's time,
that critical munitions become unavailable within five to seven days
and are exhausted within thirty-five to forty days,
and that up to ninety percent of aircraft at forward bases are destroyed on the ground,
appear in a search-engine summary of the foundation's site
and in a [news article][news_amac_2026_tidalwave]
from the Association of Mature American Citizens,
or AMAC,
but not in the executive summary itself.
They are reported here as press claims about the project and not as findings read in the primary text.
This article's first draft attributed them to the executive summary,
which was wrong,
and the correction is recorded in the Epistemic State section.

What the archived summary does state is directional and in one respect the opposite of the press account.
Its stated purpose is to produce recommendations that "extend our sustainment
and push the U.S. culmination date beyond that of the PRC",
which implies that the United States culminates first as matters stand.
On munitions it reports that in the highest-intensity cases
"platform destruction, not munition exhaustion, limits combat power",
with aircraft and ships destroyed so fast that some of the magazine is never fired.
That is a different failure from running out of missiles,
and it cuts against the simple reading that stockpile depth is the binding constraint.

The summary also states two quantitative results about the other side.
Strikes on fixed production and storage sites could hold PLA sustainment of a moderate to high-intensity conflict
to more than 90 days in the air domain and 120 to 140 days at sea.
Taking the air figure as the tighter bound,
the naval window is longer by the following factors.

$$
\frac{120}{90} \approx 1.33,
\qquad
\frac{140}{90} \approx 1.56
$$

The summary further notes that 43 percent of China's oil imports come from the Gulf region,
which is the dependency the targeting discussion rests on.
On the American side it names concentrated forward basing at Guam and Kadena,
vulnerable to missile strikes in the opening hours and days,
and a sealift, airlift and replenishment capacity it judges very likely insufficient for surge demand.

[Newsweek][news_newsweek_2026_tidalwave_redactions]
reported that the government requested redactions before release in January 2026.
The model itself is not public,
so its assumptions cannot be audited in the way the CSIS rules can,
and the full report was not retrieved for this article.

## The Economic Estimates Are Not Wargames

The external summary stated that every published wargame shows a global depression.
The wargames above do not model the world economy.
The CSIS invasion report scores outcomes on Taiwan's political autonomy
and explicitly excludes economic damage from that score.
The economic figures come from separate analyses.

[Gompert, Cevallos and Garafola 2016][research_gompert_2016_war_with_china]
at RAND estimated that a yearlong severe war could reduce Chinese gross domestic product,
or GDP,
by 25 to 35 percent,
against 5 to 10 percent for the United States.
The authors judged that by 2025 improved Chinese anti-access and area-denial capability would narrow the gap in military losses,
making an American military victory less likely without making a Chinese one likely,
so that nonmilitary factors, which favor the United States, could decide a long war.
They also suggested that economic damage of that size could aggravate political turmoil inside China.

Bloomberg Economics has published two model runs.
The January 2024 estimate,
as reported by
[Taiwan News][news_taiwan_news_2024_bloomberg],
put the first-year cost of a war at 10.2 percent of global GDP,
about 10 trillion dollars,
with losses of 16.7 percent for China,
6.7 percent for the United States,
and 40 percent for Taiwan.
A blockade cost 5 percent of global GDP,
with losses of 8.9 percent for China,
3.3 percent for the United States,
and 12.2 percent for Taiwan.
The February 2026 update by Jennifer Welch and Maeva Cousin,
as republished by
[Insurance Journal][news_insurance_journal_2026_bloomberg],
put the war case at 9.6 percent of global GDP,
about 10.6 trillion dollars,
with losses of 11 percent for China,
6.6 percent for the United States,
40 percent for Taiwan,
23 percent for South Korea,
and 14.7 percent for Japan.

A dollar loss and a percentage loss together imply the size of the world economy the model assumed.
Let $\Delta Y$ be the first-year dollar loss,
$\ell$ the proportional loss,
and $W$ the implied world GDP,
all in trillions of dollars except $\ell$.

$$
W = \frac{\Delta Y}{\ell}
$$

The two Bloomberg runs give the following bases.

$$
W_{2024} \approx \frac{10}{0.102} \approx 98,
\qquad
W_{2026} \approx \frac{10.6}{0.096} \approx 110
$$

Both are plausible magnitudes for world output in the years concerned,
and the difference is consistent with growth between the two runs and with the rounding of the 2024 dollar figure.
The dollar and percentage figures therefore agree with each other in both reports.

The estimates agree that China loses a larger share of output than the United States,
and they disagree by a wide margin on how much larger.
Let $L_{\text{China}}$ and $L_{\text{United States}}$ be the first-year proportional GDP losses.
For RAND the ratio is a range,
bounded by pairing the ends of the two published ranges.

$$
\frac{25}{10} = 2.5 \;\le\; \frac{L_{\text{China}}}{L_{\text{United States}}} \;\le\; \frac{35}{5} = 7
$$

The three estimates can then be set side by side.

$$
\frac{L_{\text{China}}}{L_{\text{United States}}} \approx
\begin{cases}
\dfrac{30}{7.5} = 4.0 & \text{RAND 2016, range midpoints} \\[2ex]
\dfrac{16.7}{6.7} \approx 2.5 & \text{Bloomberg 2024} \\[2ex]
\dfrac{11}{6.6} \approx 1.7 & \text{Bloomberg 2026}
\end{cases}
$$

The ratio has fallen with each successive estimate,
and the latest falls below even the lower end of the RAND range.
That does not establish a trend in the underlying reality,
since the models differ in method and scenario,
but it does mean the claim that war is economically catastrophic for China alone is weaker in the most recent estimate than in the oldest.

Two further comparisons come from the 2024 Bloomberg run.
A blockade costs the world about half as much as a war,
and in a blockade China still loses more than the United States in proportion.

$$
\frac{\ell_{\text{blockade}}}{\ell_{\text{war}}} = \frac{5}{10.2} \approx 0.49,
\qquad
\frac{8.9}{3.3} \approx 2.7
$$

Taiwan's proportional loss in a war is about four times the world's in both runs.

$$
\frac{40}{10.2} \approx 3.9,
\qquad
\frac{40}{9.6} \approx 4.2
$$

In both Bloomberg estimates the largest proportional loss falls on Taiwan,
and the RAND study does not estimate Taiwan's loss.

## A Survey of the Contemporary Literature

The eight studies read closely above are a small part of a large literature.
This section surveys the rest of it,
grouped by the question each cluster tries to answer.
The grouping is by position where positions conflict,
because a survey that lists titles without saying who disagrees with whom
hides the only thing a reader needs.

### Operational wargames beyond the four read closely

The Center for a New American Security has run a series of games
whose published outputs are shorter than the CSIS reports and narrower in scope.
[The Poison Frog Strategy][research_dougherty_2021_poison_frog]
gamed a Chinese seizure of the Dongsha islands
and found few credible options to compel a withdrawal,
with sanctions too weak to matter.
[When the Chips Are Down][research_wasser_2022_chips_down]
ran a single game with thirty participants over four moves from 2025 to 2029,
triggered by corrupted code halting leading-edge semiconductor fabrication for two months.
[Avoiding the Brink][research_pettyjohn_2023_avoiding_brink]
ran two tabletop exercises identical except for the size of the Chinese nuclear force,
roughly 700 warheads in a 2027 setting against more than 1,000 in 2030,
and found that neither side credited the other's nuclear threats.
[No Winners in This Game][research_kilcrease_2023_no_winners]
gamed the economic domain alone and judged technology-denial options modest at best.

[Bad Blood][research_pettyjohn_2023_bad_blood]
is the most quotable of the set because members of Congress played it.
Over two moves representing the first six days of a 2027 war,
the American side lost more than 90 aircraft,
two attack submarines sunk and three damaged,
two amphibious ships sunk and a carrier damaged,
and ran out of standoff maritime strike weapons in three days.
The Chinese side lost more than 150 aircraft,
15 submarines,
more than 100 surface ships and a carrier,
landed about 50,000 troops and lost more than 40,000 of them.
That last pair is the starkest casualty ratio in the public record.

$$
\frac{40{,}000}{50{,}000} = 0.80
$$

Four in five of the troops put ashore became casualties in six days of play.
The authors state that such exercises are indicative and not predictive.

CSIS has also published crisis simulations distinct from its invasion game.
[Shadow Risk][research_jensen_2022_shadow_risk]
ran twenty simulations of a 2027 standoff over Kinmen as a conjoint experiment,
ten offering players long-term military options and ten offering only immediate ones,
and found that the availability of long-term options made deferral more attractive
while raising the magnitude of escalation in the following round.
That is a result about how the menu shapes the choice,
which is a different kind of finding from a loss table.

The RAND Corporation's contribution is mostly analytic rather than gamed.
[The U.S.-China Military Scorecard][research_heginbotham_2015_scorecard]
measured ten operational areas across four snapshot years from 1996 to 2017
and concluded that China need not reach parity to challenge the United States near its own coast.
[Inflection Point][research_ochmanek_2023_inflection_point]
argues American posture has become insolvent.
[Denial Without Disaster][research_goldfeld_2024_denial_without_disaster],
in four volumes,
builds an escalation framework from Chinese-language sources and historical cases
and ties long-range strike to several unintended escalation pathways.

The Atlantic Council has gamed narrower questions.
[Aquatic Tiger][research_garlauskas_2026_aquatic_tiger]
tested long-range autonomous underwater vehicles across three moves
and found them useful before a conflict and attrited faster than they could be replaced inside one.
[Guardian Tiger I and II][research_garlauskas_2025_guardian_tiger]
ran two exercises with more than sixty participants on simultaneous Chinese and North Korean threats.
[A Maritime Blockade of Taiwan][research_jestrab_2023_maritime_blockade]
judges blockade the most strategically viable Chinese option
and records that Taiwan imports about 98 percent of its energy by sea.
The Mitchell Institute's
[Rebuilding America's Air Force][research_gunzinger_2026_rebuilding_air_force]
compared two 2035 force mixes across three moves against a landing campaign
and concluded that the current trajectory cannot sustain deep strike.
The Council on Foreign Relations'
[The Next Taiwan Crisis Will Not Be Like the Last][research_stares_2025_next_taiwan_crisis]
argues the next crisis will differ from the modelled ones in five ways,
including a trigger outside the strait and a war lasting years.

### Allied and European games, which reach different conclusions about the same war

The Sasakawa Peace Foundation's
[tabletop exercise on the Taiwan Strait crisis][research_spf_2024_taiwan_strait_ttx]
is the most numerically explicit non-American game in the public record.
Nineteen players in four teams plus a ten-person control group
played four turns on an operational hex map.
At the end of play Japan had lost 15 surface vessels and about 2,500 personnel,
the United States 8 surface vessels,
two carriers,
nine nuclear submarines and about 11,000 personnel,
China 81 surface vessels,
46 amphibious warships,
two carriers and more than 40,000 personnel,
and Taiwan 18 surface vessels and about 13,000 personnel.
China had expended roughly 75 percent of its missile capability by the fourteenth day,
and play stopped when the Chinese team signalled tactical nuclear use.

Setting the Chinese naval losses beside the CSIS base-scenario average
shows two independently designed games landing close to one another.

$$
81 + 46 = 127 \quad \text{against} \quad 138
$$

The Japanese game destroyed 127 major Chinese ships and the American game 138,
a difference of about eight percent,
which is closer agreement than the difference in their rules would lead one to expect.

The exercise is also unusually candid about its own weaknesses.
Its authors record that Taiwan's role was weak,
that the design was centred on the United States and China,
that hex adjudication abstracted the battle,
and that gray-zone, coast guard, evacuation and refugee dynamics were not simulated at all.

Other allied work reaches past the fighting itself.
The Japan Forum for Strategic Studies ran a
policy simulation with sitting legislators and former vice-ministers.
The International Institute for Strategic Studies'
[Deterrence Failure in a Cross-Strait Conflict][research_iiss_2023_deterrence_failure]
worked three failure scenarios set in 2027, 2032 and 2037
and concluded that the military balance is necessary but not sufficient
and that basing access cannot be assumed.
The Royal United Services Institute's
[study of the effect on European defence][research_rusi_2024_european_defence]
asks which American capabilities would be demanded in two theatres at once
and finds that a denial-oriented strategy creates far fewer two-theatre gaps
than one requiring strikes on the Chinese mainland.
The United States Studies Centre's
[grey-zone simulation][research_ussc_2026_grey_zone_games]
found that uncertainty about American commitment
pushed the Australian and Japanese teams to act more assertively.
The [Körber Policy Game][research_koerber_2021_policy_game]
put senior Europeans in national teams and found economic instruments the response of choice,
with the teams arguing that the North Atlantic Treaty's Article 5 would not apply.

### Invasion feasibility in the peer-reviewed literature

The academic literature is older, slower and more sceptical than the think-tank literature,
and it mostly argues that an invasion is hard.
[Biddle and Oelrich 2016][journal_biddle_oelrich_2016]
argue that anti-access capabilities are real but bounded by the physics of over-the-horizon targeting,
so that neither side can hold command of the commons
and a contested zone forms between two spheres.
[Beckley 2017][journal_beckley_2017]
argues China's maritime neighbours can deny it sea and air control across the near seas
at a cost they can afford.
[Heginbotham and Samuels 2018][journal_heginbotham_samuels_2018]
make the parallel argument for Japan,
recording that Chinese military spending was half of Japan's in 1996
and some three and a half times as large at the time of writing.
[Kastner 2015][journal_kastner_2016]
weighs the shifting military balance against economic integration and Taiwanese identity
and concludes the relationship is stabilising unless the military shift outpaces the rest.
[Timbie and Ellis 2021][journal_timbie_ellis_2021]
make the porcupine case for many small systems over few large ones.
[Cancian 2025][journal_cancian_2025_states_of_denial]
attacks the assumption that a minimal Chinese lodgement means Chinese victory,
and argues that denial achieved over weeks is sufficient
and requires a far less improbable sequence of political decisions than denial in seventy-two hours.

Against that line stands a smaller and more recent group.
[Mastro 2021][commentary_mastro_2021_taiwan_temptation]
argues that twenty-five years of modernisation now support the four campaigns an invasion requires
and that Xi Jinping has tied unification to his own legacy.
[Montgomery and Yoshihara 2025][journal_montgomery_yoshihara_2025]
survey coercive options short of invasion.
[Easton 2026][journal_easton_2026_stratagems]
argues that surprise and deception of the kind Russia used against Ukraine
may drive Chinese preparation.

### Whether Taiwan is worth the war, which the wargames never ask

Two articles argue directly with each other about what conquest would buy.
[Green and Talmadge 2022][journal_green_talmadge_2022]
argue that Chinese control of Taiwan would improve the balance in China's favour,
because submarines based on the island and hydrophone arrays off it
would close a missing link in the Chinese kill chain.
[Caverley 2025][journal_caverley_2025]
rebuts them with a three-component kill-chain model,
finding that Taiwan extends the Chinese engagement zone only 100 to 300 kilometres
beyond what mainland systems already cover without space-based sensors,
and that submarine-launched salvos rise from roughly 10 per week to 42 per week
in the case most favourable to China.

$$
\frac{42}{10} = 4.2
$$

A fourfold increase in salvo rate is the strongest form of the pessimistic case,
and Caverley's point is that it is smaller than the rhetoric of a decisive island suggests.
No wargame in this survey scores that question,
because every one of them takes the value of Taiwan as given.

### The nuclear escalation literature, which is split down the middle

The public wargames find nuclear use plausible.
The academic literature disagrees with itself about why and how much.
[Talmadge 2017][journal_talmadge_2017]
is the canonical pessimistic case,
arguing that a conventional campaign could threaten Chinese retaliatory forces
and that wartime perception could push Beijing to limited use despite no first use.
[Cunningham and Fravel 2015][journal_cunningham_fravel_2015]
and [Cunningham and Fravel 2019][journal_cunningham_fravel_2019]
read Chinese military writing and conclude the opposite,
that Chinese strategists doubt escalation can be controlled once it starts,
which restrains even limited use,
and that the asymmetry between that belief and greater American confidence is itself the danger.
[Wu 2022][journal_wu_2022]
argues inadvertent escalation risk is extremely low,
because Chinese forces would survive conventional attack
and command is centralised around negative control.
[Wu 2020][journal_wu_2020]
models survivability and finds retaliation far from assured yet still sufficient to deter.
[Glaser and Fetter 2016][journal_glaser_fetter_2016]
argue the United States should give up damage limitation against China.
[Hiim, Fravel and Trøan 2023][journal_hiim_2023]
describe an entangled security dilemma in which conventional and nuclear systems cannot be separated.
[Kearn 2025][journal_kearn_2025]
argues American tactical nuclear first use would not deter Beijing and would invite escalation.

The split matters for how the CSIS nuclear results should be read.
That study found seven of eight nuclear uses beginning with a China team facing conventional defeat.
Talmadge and Kearn would treat that as confirmation.
Wu would treat it as an artifact of players who do not share Chinese doctrinal beliefs,
which is a criticism of the method and not of the finding.

### Deterrence theory, which doubts that more certainty helps

[Goldstein 2013][journal_goldstein_2013]
argues the near-term danger is crisis escalation and not long-run rivalry,
and that escalation pressure is highest early,
which compresses the window for diplomacy.
[Harris and McKinney 2024][journal_harris_mckinney_2024]
attack the assumption that greater certainty, severity and speed always strengthen deterrence,
and conclude that strategic clarity over Taiwan would be unlikely to strengthen it.
Both cut against the reflex that the answer to a wargame's bad result
is a firmer declaratory commitment.

### Blockade, where the academic literature is more pessimistic than the games

[Mirski 2013][journal_mirski_2013]
examines the reverse case of an American blockade of China
and finds it viable only in a narrow context.
[Cunningham 2020][journal_cunningham_2020_maritime_rung]
argues that a blockade designed to minimise escalation
would still invite deliberate non-nuclear Chinese escalation,
so the escalation saving is illusory.
[Davis and Gholz 2026][journal_davis_gholz_2026]
is the most pessimistic recent finding in the peer-reviewed literature.
Using Monte Carlo simulation,
they argue China could suppress Taiwanese trade substantially
by striking ports with standoff missiles rather than by interdicting ships,
at relatively low escalation risk and without expending its fleet.
They add that militarily successful blockades have rarely achieved their political goals.
[Henley 2023][research_henley_2023_beyond_first_battle]
argues a prolonged blockade sealing western ports and airfields would likely decide the conflict,
and identifies the gap in sustaining Taiwan even after an invasion has been repelled.
The [China Maritime Studies Institute volume on amphibious warfare][research_erickson_2024_amphibious_warfare]
is the largest open-source treatment of the landing campaign itself.

### Economic estimates, and why they do not corroborate one another

The economic literature looks larger than it is.
Only three independent estimates exist,
and most of the documents that appear to confirm them are citing them.

[Rhodium Group 2022][research_rhodium_2022_disruptions]
put well over two trillion dollars of economic activity at risk in the first year of a blockade
and stated plainly that it does not purport to estimate losses of gross domestic product.
The [Institute for Economics and Peace 2023][research_iep_2023_gpi]
put a blockade at 2.7 trillion dollars,
a 2.8 percent fall in global output,
with China contracting about 7 percent and Taiwan by almost 40 percent.
Bloomberg Economics put the same contingency at 5 percent of global output.
The two blockade estimates differ by a factor approaching two.

$$
\frac{5.0}{2.8} \approx 1.79
$$

Both describe a blockade.
The difference is method,
since the Institute for Economics and Peace prices trade disruption and excludes recession effects,
while Bloomberg models a macroeconomic shock.
A reader who saw only the two headline numbers would think one of them wrong.
Neither is wrong.
They are answers to different questions.

[RAND 2025][research_shatz_2025_economic_deterrence]
models sanctions alone with a computable general equilibrium model covering more than 145 economies
and finds Chinese output falling more than 2.5 percent a year under full coalition sanctions,
with global output down about 0.5 percent.
Those numbers sit an order of magnitude below the war estimates
because they price a different event,
and quoting them beside war figures would misrepresent both.

Exposure studies measure the stakes without pricing them.
[CSIS ChinaPower][research_csis_2024_crossroads_commerce]
finds 2.45 trillion dollars of goods transited the strait in 2022,
over one-fifth of global maritime trade.
[Verschuur, Lumma and Hall 2025][journal_verschuur_2025],
the only peer-reviewed quantitative work located here,
ranks the Taiwan Strait first among 24 chokepoints
at 37.3 billion dollars of trade disrupted per year in expectation,
while noting that the economic risk is only about 0.9 billion because detours are short.
That figure is an annualised expectation under ordinary probabilities
and is not comparable to a conflict scenario.
[Lloyd's][research_lloyds_2024_geopolitical_scenario]
prices a five-year geopolitical conflict scenario at 14.5 trillion dollars as a weighted average.
[Vest and Kratz 2023][research_vest_2023_sanctioning_china]
put more than three trillion dollars of trade and financial flows at immediate risk under full sanctions.
[Blanchette, DiPippo and Johnstone 2023][research_blanchette_2023_scared_strait]
ran closed-door exercises with financial firms and reached no headline number at all,
concluding that the conflict is the sanction.

### Semiconductor dependence, stated precisely

The claim that Taiwan makes most of the world's advanced chips is true
and is usually stated in a way that cannot be checked.
The underlying figure comes from
[Boston Consulting Group and the Semiconductor Industry Association][data_bcg_sia_2021_value_chain],
which found that on 2019 data
92 percent of world capacity below 10 nanometres was in Taiwan and the remaining 8 percent in South Korea,
while capacity below 10 nanometres was only about 2 percent of all capacity
and Taiwan held about 40 percent of logic capacity overall.
[TrendForce][data_trendforce_2023_foundry_capacity]
measured 2023 capacity at 16 and 14 nanometres and below
at 68 percent for Taiwan,
and capacity of the class used for the smallest nodes at close to 80 percent.

The two numbers are often quoted against each other as though one refuted the other.

$$
92 \ \text{percent below 10 nm in 2019}
\quad \text{against} \quad
68 \ \text{percent at 16 and 14 nm and below in 2023}
$$

They differ in node threshold and in year,
and neither is a statement about all semiconductors.
The defensible form of the claim states the threshold and the date,
which is what the rest of this article tries to do with every number it carries.

### Official assessments, which are more cautious than the commentary

The [Office of the Director of National Intelligence][government_odni_2026_threat_assessment],
in its threat assessment prepared with information available as of 14 March 2026,
states that "Chinese leaders do not currently plan to execute an invasion of Taiwan in 2027,
nor do they have a fixed timeline for achieving unification",
and that "Chinese officials recognize that an amphibious invasion of Taiwan
would be extremely challenging and carry a high risk of failure,
especially in the event of U.S. intervention".
It expects Beijing in 2026 to continue "seeking to set the conditions
for eventual unification with Taiwan short of conflict".
That is the sharpest official contradiction of the closing-window reading available,
and it comes from the body whose job is to say what Beijing intends.

The [United States-China Economic and Security Review Commission][government_uscc_2025_taiwan_chapter]
documents the pressure campaign in numbers.
Incursions into Taiwan's air defence identification zone rose from 20 in 2019 to 3,075 in 2024.

$$
\frac{3{,}075}{20} = 153.75
$$

Crossings of the median line rose from 22 instances in 2020 to 1,472 in 2024,
which the Commission states as an increase of 6,591 percent.

$$
\frac{1{,}472 - 22}{22} \approx 65.9 \quad \text{or} \quad 6{,}591 \ \text{percent}
$$

The recomputation matches the published figure.
The [Institute for the Study of War][research_isw_2025_justice_mission]
reconstructed one such exercise from open sources in December 2025,
counting 18 navy vessels,
14 coast guard ships
and 201 air sorties of which 125 crossed the median line,
and read the pattern as a rehearsal for isolating Taiwan's main ports.
The Commission also records that officials have warned a blockade could begin within a matter of hours,
that three linked landing barges formed a 2,700-foot mobile pier in March 2025,
and that Taiwan requested a 2025 defence budget of 647 billion New Taiwan dollars,
which it gives as 19.7 billion United States dollars.

$$
\frac{647}{19.7} \approx 32.8
$$

The implied exchange rate is close to the market rate of the period,
which is the kind of check that catches a transposed figure.

The Department of Defense publishes an annual report on Chinese military power,
the [2025 edition of which appeared on 23 December 2025][government_dod_2025_china_report].
Its server refused every retrieval route tried for this article,
so its findings are reported here from a
[summary by a China military specialist][commentary_erickson_2025_dod_report_set],
which gives the operational warhead stockpile in the low 600s through 2024
and a projection of more than 1,000 by 2030.
Taking those two figures at face value gives an implied growth rate.

$$
\left( \frac{1000}{600} \right)^{1/6} - 1 \approx 0.089
$$

About 9 percent a year compounded over six years,
which is rapid for a nuclear force and slower than the doubling language often used about it.
Taiwan's own [national defence report][government_mnd_2025_defense_report]
and the [Congressional Research Service summary of its defence issues][government_crs_2026_taiwan_defense]
complete the official picture.

### Wargaming as a method, and what its practitioners say it cannot do

The strongest criticism of the wargames in this article comes from people who design wargames.
[Perla and McGrady 2011][journal_perla_mcgrady_2011]
locate a wargame's power in narrative and in turning participants into decision-makers,
not in predictive fidelity.
[McGrady 2019][commentary_mcgrady_2019_getting_story_right]
puts it bluntly,
that wargames are about understanding and not knowledge,
about ideas and not facts,
and that they are unrepeatable, chaotic, vague and messy events.
[Lin-Greenberg, Pauly and Schneider 2022][journal_lin_greenberg_2022]
set out what would make a wargame usable as research,
resting its comparative advantage on ecological validity
while naming recruitment, bias and generalisability as the constraints.
[Curry 2020][journal_curry_2020]
reviews a century of declassified professional games
and finds many of them contained major errors,
which is a caution against treating any single game as authoritative.
[Downes-Martin 2014][journal_downes_martin_2014]
names the institutional problem,
that a sponsor, a boss and a set of players can each distort a game's findings.
[Bartels 2020][research_bartels_2020_building_better_games]
proposes designing games around the kind of information they can actually generate.

[Schneider 2023][commentary_schneider_2023_war_games_reveal]
makes the observation most damaging to the genre this article surveys,
that the recent Washington games about Taiwan revealed little that was new
and that their significance lies in American factional politics and in signalling,
so that a game often reveals more about the interests of the players
than about the outcome of the war.
[Heath 2023][commentary_heath_2023_wargames_deterrence]
argues that combat wargames should not be repurposed to answer questions about deterrence,
escalation or war termination,
which is precisely what most public commentary does with them.
[Fuka 2025][commentary_fuka_2025_coming_wave]
supplies the mirror image,
reporting a Chinese designer's criticism that Western Taiwan games
are stuck in a mentality that privileges land manoeuvre
and fails to model the electromagnetic environment.

### Artificial intelligence in wargaming, which is where the field is arguing now

[Reddie and others 2018][journal_reddie_2018]
proposed computer-based wargames repeatable enough to support statistical inference,
and [Reddie and Goldblum 2023][journal_reddie_goldblum_2023]
built a platform to measure how tailored capabilities move the nuclear threshold.
Large language models then entered the field.
[Rivera and others 2024][research_rivera_2024_escalation_risks]
found that all five off-the-shelf models they tested escalated in hard-to-predict ways.
[Lamparth and others 2024][research_lamparth_2024_human_vs_machine]
ran a crisis game with 107 national security experts
and compared them against model-simulated players,
finding considerable agreement alongside significant divergence.
[Payne 2026][research_payne_2026_ai_arms_influence]
reports frontier models attempting deception and reasoning about adversary beliefs in nuclear crises,
and records that no model ever chose accommodation or withdrawal under pressure.

[Panda and Reddie 2026][commentary_panda_reddie_2026_ai_wargaming]
supply the rebuttal,
arguing that such results reveal machine psychology and not human nuclear decision-making,
and that the models escalate because their training corpus is thick with coercive strategy
and thin with de-escalatory reasoning.
[Geist, Frank and Menthe 2024][research_geist_2024_ai_wargames_limits]
draw the boundary that matters for this article.
They find artificial intelligence most promising for games
that are well bounded and repeated many times,
and least promising for games designed to explore systems or generate innovation
and for games "played as one-offs or a very limited number of times".
Most of the public Taiwan games are one-offs or near enough.
[Jensen and others 2024][commentary_jensen_2024_democratize_wargaming]
take the opposite side and argue generative models cut cost and improve rigour.
The TIDALWAVE project discussed above is the first large public artifact of that argument,
and its executive summary is also the clearest illustration of the problem,
since the figures most widely quoted from it cannot be found in it.

## Where the Record Agrees and Where It Does Not

### Points of agreement

Across the sources read for this article,
several findings recur.

- **An invasion with prompt American intervention rarely succeeds in the CSIS games,
but it often stalemates.**
Nine of twenty-four iterations ended in clear Chinese defeat,
fourteen in stalemate,
and the Chinese successes came only when the United States stayed out or when the scenario removed American airpower by design.
- **Every party pays heavily.**
Carriers, surface ships and hundreds of aircraft are lost,
most aircraft on the ground,
and the Chinese amphibious fleet is largely destroyed.
- **No project finds a quick war.**
CNAS found no upper hand after a week,
CSIS scored most pessimistic iterations as stalemates when play ended,
and TIDALWAVE models a conflict of more than six months.
- **Precision munitions run short within days to weeks.**
CSIS found the anti-ship missile inventory gone in the first week.
TIDALWAVE measures first-deficit days and collapse windows for both sides,
though its archived summary adds that in the most intense cases platforms are destroyed
before their magazines are emptied.
- **Nuclear use is a live possibility in every project that permitted it.**
CNAS and TIDALWAVE II saw nuclear signaling or theater use,
and Confronting Armageddon saw nuclear use in eight instances across fifteen games.
- **Taiwan's economy is devastated in every case modeled.**

### Points of disagreement

The external summary described the record as uniform.
It is not.

- **Who culminates first.**
CSIS finds the invasion fleet destroyed before China can secure ports in its base cases.
TIDALWAVE states its aim as pushing the American culmination date beyond the PRC's,
which implies the United States culminates first as matters stand.
These do not describe the same war,
and the difference lies in assumptions about duration, sustainment and forward basing
that cannot be fully compared because TIDALWAVE's model is not public.
- **Whether a Chinese defeat is the end of the story.**
The conventional CSIS game treats destruction of the amphibious fleet as decisive.
The nuclear CSIS game finds that exactly that moment generated the greatest pressure for Chinese nuclear use.
- **How much worse the economic outcome is for China.**
The ratio of Chinese to American output loss ranges from about four in the RAND study to about 1.7 in the latest Bloomberg run.

## What the Record Implies for the Closing Window Gamble

This section is inference and is marked as such.

The premise of the article is a leadership that acts because it fears decline.
The conventional results suggest that such a leadership would probably fail to take Taiwan if Taiwan resists and the United States intervenes promptly from Japan.
The external summary concluded from this that the gamble is statistically disastrous for the PRC and stopped there.

Two findings complicate that conclusion.
First,
the outcomes are conditional on choices by Taipei, Washington and Tokyo that a Chinese planner might judge uncertain,
and the single decisive variable in the CSIS game,
whether the United States fights at once from Japanese bases,
is exactly the variable a planner betting on a closing window would be betting on.
Second,
the nuclear games found that a failing invasion that threatened Communist Party rule
was the circumstance most likely to produce Chinese nuclear use.
The premise itself holds that the regime's legitimacy is already strained.
If so,
the conventional defeat that the summary treated as the end of the gamble
is the point at which the nuclear games locate the greatest danger.
The CSIS authors draw a related conclusion
when they recommend preparing face-saving off-ramps that let Beijing end a failing war without choosing between nuclear use and regime collapse.

The inference therefore runs as follows.
The public wargames do not show that a closing window gamble is safe for China.
They also do not show that its failure would be safe for anyone else.

## Limits of Wargaming as Evidence

A wargame is a structured argument about a war and not a sample from the distribution of possible wars.
Several limits apply to everything above.

- **The sample is narrow.**
[Tetreau 2023][commentary_tetreau_2023_where_the_wargames_were_not]
reviewed ten major assessments from the preceding decade
and found that seven considered Chinese efforts to take Taiwan,
most of them an invasion,
while flashpoints in the South China Sea and the East China Sea received little attention.
He also criticized the near-universal assumption that war begins by deliberate choice,
leaving accident and miscalculation aside.
- **The scenarios reflect American planning assumptions.**
[Michaels and Williams 2025][commentary_michaels_williams_2025_wargame_china_perspective]
ran a game in which experts played Beijing's side.
Their players concluded that attacking American forces made little strategic sense
and favored limited missile strikes, coercion, and generous surrender terms over a massive landing.
If Beijing reasons that way,
the invasion games answer a question China may not ask.
- **Public games lack classified data.**
The CSIS reports build rules from open sources and historical analogies,
so the performance of weapons, space systems and cyber operations is estimated.
- **Frequencies are not probabilities.**
The CSIS authors state that modeling an invasion does not imply that it is likely,
and that the frequency of nuclear use in their games does not indicate its probability.
- **Political decisions are thinly modeled.**
The nuclear study says it minimized political factors,
and the blockade study declined to judge political outcomes at all.

The narrowness and the frequency problem can both be stated as ratios.
Tetreau's concentration of attention on Taiwan is the first.

$$
\frac{7}{10} = 0.70
$$

The second is the design of the invasion game,
which ran nine pessimistic iterations for every optimistic one.

$$
\frac{N_{\text{pess}}}{N_{\text{opt}}} = \frac{18}{2} = 9
$$

The designers ran more pessimistic iterations because the base results raised the question of what it would take for China to win.
That is a sound way to explore assumptions,
and it means the outcome fractions computed earlier describe the design, which is not the world.
Had the proportions of pessimistic and optimistic runs been reversed,
the fraction of decisive Chinese defeats would have risen with no change in anything the game models.

## Epistemic State

**Documented in primary reports read in full or in their executive summaries.**
The CSIS invasion, nuclear and blockade results,
including the iteration counts, outcome categories, loss tables and energy exhaustion times,
were read from the published PDF reports.
The CNAS findings were read from its executive summary.
The RAND 2016 economic estimates and four war cases were read from the report's summary.
The RAND 2025 demographic projections and its assessment of PLA force size were read from the report.
The 2024 and 2025 population figures were read from the two National Bureau of Statistics communiqués.
The marriage, divorce and cohort figures were read from the State Council Information Office account
of the Ministry of Civil Affairs bulletin.
The CSIS munitions expenditure figures were read from the Jones report.
The Davidson quotation was read from the stenographic transcript of the Senate hearing of 9 March 2021.
The reunification passages were read from the 2022 white paper.
The TIDALWAVE description, the culmination aim, the platform-destruction finding,
the PLA sustainment windows and the Gulf oil dependency
were read from an archived copy of the executive summary captured on 14 April 2026.
The Brands and Beckley essay was read in Foreign Policy,
the Mastro and Scissors essay in the American Enterprise Institute republication,
and the Medeiros essay in a copy of the Foreign Affairs print article.

**Documented only through summaries or press accounts.**
The widely quoted TIDALWAVE figures,
being the culmination ratio, the five to seven and thirty-five to forty day munitions brackets,
and the ninety percent of aircraft destroyed at forward bases,
rest on a search-engine summary and the AMAC article,
and are absent from the archived executive summary.
They are reported as press claims and are not used as findings.
The TIDALWAVE II results rest on the summary text of the foundation's report page.
The Bloomberg Economics figures rest on Taiwan News and Insurance Journal accounts,
because Bloomberg refuses automated retrieval.
The full TIDALWAVE report, which runs to about 400 pages according to Newsweek, was not retrieved.
The Danger Zone book is cited from its publisher page and was not read.

**Derived in this article.**
Every displayed equation is arithmetic on published figures and can be rechecked from the cited sources.
The consistency checks are the population balance and implied migration,
the crude rates from counts,
the natural growth rate,
the reconciliation of the CSIS family counts and outcome partition,
the combined loss row,
the Chinese ship composition,
the Armageddon outcome and recommendation partitions,
the blockade game count,
the missile expenditure sum,
the 2024 population balance,
the marriage rate recomputed from the registration count,
the working-age loss cross-checked across three sources,
and the implied world GDP behind each Bloomberg run.
The derived comparisons are the marriage decline,
the dependency ratio multiple, growth rate and reciprocal,
the CSIS outcome fractions,
the implied amphibious fleet size and share,
the ship and aircraft exchange ratios,
the implied Chinese dead and the order of magnitude of dead and captured,
the pessimistic-to-base multipliers,
the Armageddon conditional frequencies,
the first-week share of losses,
the blockade casualty growth and exchange ratios,
the energy exhaustion ratios,
the missile expenditure rates and share,
the ratio of the two annual population decreases,
the divorce to marriage ratio,
the marrying-age cohort loss,
the PLA sustainment windows,
the ratios of Chinese to American economic loss,
the blockade and Taiwan loss comparisons,
and the design ratios in the Limits section.

**Assumptions introduced by this article and not made by the sources.**
The implied migration term takes the reported decrease as exact to two decimal places.
The crude rate check uses a simple average of year-end populations as the mean population.
The implied amphibious fleet size treats the report's about ninety percent as exactly ninety percent.
The ship survival calculation assumes each inbound voyage faces an independent forty percent chance of loss.
The first-week share compares figures from two different game versions and scenario years.
The RAND ratio bounds pair the ends of two ranges the report does not pair.
Each is stated where it is used.

**Unresolved.**
The CSIS invasion report's four stated scenario family counts sum to 24,
and the report also describes a Ragnarok scenario without stating its iteration count.
Whether Ragnarok falls inside the 24 could not be determined from the text.
The report's table and text also disagree slightly on average Chinese aircraft losses,
155 against 161.

**Inference.**
The section on the closing window gamble,
including the observation that conventional Chinese defeat coincides with the greatest nuclear pressure in the CSIS games,
is the author's reading of the combined results
and is not a finding stated in that form by any single report.

**Claims in the source conversation that were corrected.**

- It stated that the invasion fails in the vast majority of CSIS iterations.
The report says the invasion is defeated in most scenarios,
but only nine of twenty-four iterations ended in clear defeat and fourteen ended in stalemate.
- It described dozens of Chinese capital ships sunk.
The base scenario average was 138 major ships,
86 of them amphibious ships.
Capital ship is not the report's term and misdescribes the composition.
- It stated that nearly all wargames show American munitions exhausted within the first week to a month.
That range conflates two sources.
CSIS found anti-ship missiles gone in the first week,
and TIDALWAVE reports critical munitions exhausted in thirty-five to forty days.
- It cited AMAC for logistics simulations.
AMAC is a news outlet reporting on the Heritage Foundation's TIDALWAVE project,
and the summary did not mention that TIDALWAVE projects American defeat,
which contradicts the uniform consensus the summary asserted.
- It stated that every published wargame shows a multi-trillion-dollar global depression.
The wargames do not model the global economy.
The dollar figures come from Bloomberg Economics,
and the RAND estimates are an economic assessment accompanying an analytic study.
- It attributed the closing window argument to the Brookings Institution.
The Brookings piece found for this article argues against the inference,
and the argument is most associated with Brands and Beckley.
- It suggested the PLA already faces a shrinking pool of young recruits.
The 2025 RAND study expects minimal impact on PLA personnel levels over the next decade
and places the constraint further out.
- It claimed that nearly a third of China's population reaches retirement age by 2050.
That figure was not verified.
The RAND projection of an old age dependency ratio of 0.52 by 2050 is reported in its place.
- It suggested that the scenario years were chosen around a demographic peak.
The reports read here give no such rationale.
The clustering traces instead to Admiral Davidson's March 2021 testimony about the next six years,
which the primary-reference pass located in the hearing transcript.

**A claim in this article's own first draft that was corrected.**
The drafting pass attributed four TIDALWAVE figures to the foundation's executive summary,
namely the culmination ratio,
the two munitions brackets,
and the share of aircraft destroyed on the ground.
**The archived executive summary contains none of them.**
They came from a search-engine summary and a news article.
The figures are now reported as press claims,
the two equations built on them have been removed,
and the section rests on what the archived primary actually states,
which includes the finding that platform destruction and not munition exhaustion
limits combat power in the most intense cases.

**Bounds.**
The article is authoritative only as a reading of the public reports named in it,
as of its editorial date.
It is not authoritative on classified assessments,
on Chinese internal planning,
or on the likelihood of any war.

## Out of Scope

- Classified American, allied and Chinese assessments,
which are not public and which the public games cannot be checked against.
- Scenarios other than Taiwan,
including conflicts in the South China Sea, over the Senkaku Islands, or on the Korean Peninsula.
- Chinese open-source military writing on Taiwan campaigns,
which would require a separate survey in Chinese-language sources.
- Gray-zone coercion short of blockade,
such as a customs quarantine by coast guard forces,
which the blockade study treats only at its lowest escalation levels.
- The effect of the war in Ukraine and of Middle East operations on American munitions stocks after the reports were written.
- A quantitative model of the war itself,
such as a Lanchester attrition model or a campaign simulation,
which would add assumptions of this article's own to results it exists to report.
- Normative questions of whether and how the United States should defend Taiwan,
on which the CSIS authors explicitly take no position and neither does this article.

## Conclusion

The premise that a declining China might strike before its window closes is contested,
and its demographic half is better supported than its strategic half.
The population is shrinking entirely through natural decrease,
marriages fell by about a fifth in a single year,
and the number of working-age adults for each older person is projected to fall from nearly five to fewer than two by 2050,
but the best available study does not expect a near-term shortage of PLA recruits,
and prominent analysts reject the inference that decline makes aggression likely.

Taking the premise as given,
the published wargames agree that an invasion of Taiwan would be extremely costly for every party,
that China rarely succeeds when Taiwan resists and the United States intervenes promptly from Japan,
that the war would not be short,
that precision munitions would run out early,
and that nuclear use is a real risk.
They do not agree on who exhausts their capacity first,
and the most recent computer model reaches the opposite conclusion from the most detailed tabletop game.
The econometric estimates, which are not wargames, agree that Taiwan suffers most and China loses more output than the United States,
by a margin that shrinks in successive estimates.

The most consequential finding for the premise is the one the external summary omitted.
The same games that make a Chinese invasion look likely to fail
identify a failing invasion as the moment of greatest nuclear danger.
A gamble that the public record says China would probably lose
is not thereby a gamble the rest of the world could safely watch it lose.

## References

- [Commentary, Brands and Beckley 2021, Foreign Policy Essay on China as a Declining Power][commentary_brands_beckley_2021_declining_power]
- [Commentary, Brands and Beckley 2022, Danger Zone, The Coming Conflict with China][commentary_brands_beckley_2022_danger_zone]
- [Commentary, Erickson 2025, Summary of the Department of Defense Annual Reports on Chinese Military Power][commentary_erickson_2025_dod_report_set]
- [Commentary, Fuka 2025, The Coming Wave, Chinese Doctrine on the Tabletop][commentary_fuka_2025_coming_wave]
- [Commentary, Heath 2023, Wargames Cannot Tell Us How to Deter a Chinese Attack on Taiwan][commentary_heath_2023_wargames_deterrence]
- [Commentary, Howard 2026, Is China a Peaked Power? And So What If It Is?][commentary_howard_2026_peaked_power]
- [Commentary, Jensen, Atalan and Tadross 2024, It Is Time to Democratize Wargaming Using Generative Artificial Intelligence][commentary_jensen_2024_democratize_wargaming]
- [Commentary, Mastro 2021, The Taiwan Temptation, Foreign Affairs][commentary_mastro_2021_taiwan_temptation]
- [Commentary, Mastro and Scissors 2022, Foreign Affairs Essay Against the Peak China Thesis][commentary_mastro_scissors_2022_peak]
- [Commentary, McGrady 2019, Getting the Story Right About Wargaming][commentary_mcgrady_2019_getting_story_right]
- [Commentary, Medeiros 2024, The Delusion of Peak China][commentary_medeiros_2024_delusion_peak_china]
- [Commentary, Michaels and Williams 2025, A Wargame to Take Taiwan, from China's Perspective][commentary_michaels_williams_2025_wargame_china_perspective]
- [Commentary, O'Hanlon 2023, China's Shrinking Population and Constraints on Its Future Power][commentary_ohanlon_2023_shrinking_population]
- [Commentary, Panda and Reddie 2026, On Artificial Intelligence Wargaming and Nuclear War][commentary_panda_reddie_2026_ai_wargaming]
- [Commentary, Schneider 2023, What War Games Really Reveal, Foreign Affairs][commentary_schneider_2023_war_games_reveal]
- [Commentary, Tetreau 2023, War on the Rocks Review of Ten Years of U.S.-Chinese Military Assessments][commentary_tetreau_2023_where_the_wargames_were_not]
- [Data, National Bureau of Statistics of China 2025, Statistical Communiqué on the 2024 National Economic and Social Development][data_nbs_2024_communique]
- [Data, National Bureau of Statistics of China 2026, Statistical Communiqué on the 2025 National Economic and Social Development][data_nbs_2025_communique]
- [Data, State Council Information Office 2025, China's Tally of Marriage Registrations Down in 2024][data_scio_2025_marriage_registrations]
- [Data, TrendForce 2023, Foundry Capacity Share by Region and Process Node][data_trendforce_2023_foundry_capacity]
- [Data, Varas and others 2021, Strengthening the Global Semiconductor Value Chain in an Uncertain Era][data_bcg_sia_2021_value_chain]
- [Government, Congressional Research Service 2026, Taiwan, Defense and Military Issues][government_crs_2026_taiwan_defense]
- [Government, Department of Defense 2025, Military and Security Developments Involving the People's Republic of China][government_dod_2025_china_report]
- [Government, Ministry of National Defense of the Republic of China 2025, National Defense Report][government_mnd_2025_defense_report]
- [Government, Office of the Director of National Intelligence 2026, Annual Threat Assessment of the United States Intelligence Community][government_odni_2026_threat_assessment]
- [Government, Senate Committee on Armed Services 2021, Hearing to Receive Testimony on United States Indo-Pacific Command][government_sasc_2021_indopacom]
- [Government, Taiwan Affairs Office and State Council Information Office 2022, The Taiwan Question and China's Reunification in the New Era][government_prc_2022_taiwan_white_paper]
- [Government, US-China Economic and Security Review Commission 2025, Annual Report to Congress, Taiwan Chapter][government_uscc_2025_taiwan_chapter]
- [Journal, Beckley 2017, The Emerging Military Balance in East Asia, International Security 42 number 2][journal_beckley_2017]
- [Journal, Biddle and Oelrich 2016, Future Warfare in the Western Pacific, International Security 41 number 1][journal_biddle_oelrich_2016]
- [Journal, Cancian 2025, States of Denial, Sensibly Defending Taiwan, Survival 67 number 2][journal_cancian_2025_states_of_denial]
- [Journal, Caverley 2025, So What, Texas National Security Review 8 number 3][journal_caverley_2025]
- [Journal, Cunningham 2020, The Maritime Rung on the Escalation Ladder, Security Studies 29 number 4][journal_cunningham_2020_maritime_rung]
- [Journal, Cunningham and Fravel 2015, Assuring Assured Retaliation, International Security 40 number 2][journal_cunningham_fravel_2015]
- [Journal, Cunningham and Fravel 2019, Dangerous Confidence, International Security 44 number 2][journal_cunningham_fravel_2019]
- [Journal, Curry 2020, Professional Wargaming, a Flawed but Useful Tool, Simulation and Gaming 51 number 5][journal_curry_2020]
- [Journal, Davis and Gholz 2026, Blockade by Fire, International Security 50 number 4][journal_davis_gholz_2026]
- [Journal, Downes-Martin 2014, Your Boss, Players, and Sponsor, Naval War College Review 67 number 1][journal_downes_martin_2014]
- [Journal, Easton 2026, Stratagems and Surprise Attacks, Naval War College Review 79 number 1][journal_easton_2026_stratagems]
- [Journal, Glaser and Fetter 2016, Should the United States Reject Mutual Assured Destruction, International Security 41 number 1][journal_glaser_fetter_2016]
- [Journal, Goldstein 2013, First Things First, International Security 37 number 4][journal_goldstein_2013]
- [Journal, Green and Talmadge 2022, Then What, International Security 47 number 1][journal_green_talmadge_2022]
- [Journal, Harris and McKinney 2024, Strategic Clarity or Calamity, International Affairs 100 number 3][journal_harris_mckinney_2024]
- [Journal, Heginbotham and Samuels 2018, Active Denial, International Security 42 number 4][journal_heginbotham_samuels_2018]
- [Journal, Hiim, Fravel and Troan 2023, The Dynamics of an Entangled Security Dilemma, International Security 47 number 4][journal_hiim_2023]
- [Journal, Kastner 2016, Is the Taiwan Strait Still a Flash Point, International Security 40 number 3][journal_kastner_2016]
- [Journal, Kearn 2025, Limited Nuclear War and the Defense of Taiwan, Journal of Strategic Studies][journal_kearn_2025]
- [Journal, Lin-Greenberg, Pauly and Schneider 2022, Wargaming for International Relations Research, European Journal of International Relations 28 number 1][journal_lin_greenberg_2022]
- [Journal, Mirski 2013, Stranglehold, Journal of Strategic Studies 36 number 3][journal_mirski_2013]
- [Journal, Montgomery and Yoshihara 2025, Conquering Taiwan by Other Means, The Washington Quarterly 48 number 1][journal_montgomery_yoshihara_2025]
- [Journal, Perla and McGrady 2011, Why Wargaming Works, Naval War College Review 64 number 3][journal_perla_mcgrady_2011]
- [Journal, Reddie and Goldblum 2023, Evidence of the Unthinkable, Journal of Peace Research 60 number 5][journal_reddie_goldblum_2023]
- [Journal, Reddie and others 2018, Next-Generation Wargames, Science 362 number 6421][journal_reddie_2018]
- [Journal, Talmadge 2017, Would China Go Nuclear, International Security 41 number 4][journal_talmadge_2017]
- [Journal, Timbie and Ellis 2021, A Large Number of Small Things, Texas National Security Review 5 number 1][journal_timbie_ellis_2021]
- [Journal, Verschuur, Lumma and Hall 2025, Systemic Impacts of Disruptions at Maritime Chokepoints, Nature Communications 16][journal_verschuur_2025]
- [Journal, Wu 2020, Living with Uncertainty, International Security 44 number 4][journal_wu_2020]
- [Journal, Wu 2022, Assessing Inadvertent Nuclear Escalation, International Security 46 number 3][journal_wu_2022]
- [News, AMAC 2026, Artificial Intelligence War Game Exposes United States Weaknesses in China Conflict][news_amac_2026_tidalwave]
- [News, Insurance Journal 2026, The 10 Trillion Dollar Fight, Modeling a United States and China War Over Taiwan][news_insurance_journal_2026_bloomberg]
- [News, Newsweek 2026, United States Government Requested Redactions to Report on China War Vulnerabilities][news_newsweek_2026_tidalwave_redactions]
- [News, Reuters 2025, Marriages in China Plunge by a Record in 2024][news_reuters_marriages_2024]
- [News, Taiwan News 2024, Report on the Bloomberg Economics Estimate of the Cost of a Chinese Invasion of Taiwan][news_taiwan_news_2024_bloomberg]
- [Related Post, Industrialization Waves and Geopolitical Positioning, China's Rise][related_post_china_rise]
- [Related Post, Industrialization Waves and Geopolitical Positioning, Contemporary Snapshot and Extrapolation][related_post_industrialization_snapshot]
- [Related Post, Metagaming as a Framework for Real-Life Strategy][related_post_metagaming]
- [Research, Bartels 2020, Building Better Games for National Security Policy Analysis][research_bartels_2020_building_better_games]
- [Research, Blanchette, DiPippo and Johnstone 2023, Scared Strait, Understanding the Economic and Financial Impacts of a Taiwan Crisis][research_blanchette_2023_scared_strait]
- [Research, Boyd, Gady and Nouwens 2023, Deterrence Failure in a Cross-Strait Conflict][research_iiss_2023_deterrence_failure]
- [Research, Cancian, Cancian and Heginbotham 2023, The First Battle of the Next War, Wargaming a Chinese Invasion of Taiwan][research_cancian_2023_first_battle]
- [Research, Cancian, Cancian and Heginbotham 2024, Confronting Armageddon, Wargaming Nuclear Deterrence and Its Failures in a U.S.-China Conflict over Taiwan][research_cancian_2024_confronting_armageddon]
- [Research, Cancian, Cancian and Heginbotham 2025, Lights Out? Wargaming a Chinese Blockade of Taiwan][research_cancian_2025_lights_out]
- [Research, Dougherty, Matuschak and Hunter 2021, The Poison Frog Strategy][research_dougherty_2021_poison_frog]
- [Research, Erickson, Kennedy and Martinson 2024, Chinese Amphibious Warfare, Prospects for a Cross-Strait Invasion][research_erickson_2024_amphibious_warfare]
- [Research, Fix, Kirch and Schuebel 2021, Escalation in the Taiwan Strait, Koerber Policy Game][research_koerber_2021_policy_game]
- [Research, Funaiole and others 2024, Crossroads of Commerce, How the Taiwan Strait Propels the Global Economy][research_csis_2024_crossroads_commerce]
- [Research, Garlauskas and others 2026, Aquatic Tiger, Long-Range Submarine Drones in a Taiwan Conflict][research_garlauskas_2026_aquatic_tiger]
- [Research, Garlauskas, Gilbert and Imai 2025, A Rising Nuclear Double-Threat in East Asia][research_garlauskas_2025_guardian_tiger]
- [Research, Geist, Frank and Menthe 2024, Understanding the Limits of Artificial Intelligence for Warfighters, Volume 4, Wargames][research_geist_2024_ai_wargames_limits]
- [Research, Goldfeld and others 2024, Denial Without Disaster, Keeping a Conflict over Taiwan Under the Nuclear Threshold][research_goldfeld_2024_denial_without_disaster]
- [Research, Gompert, Cevallos and Garafola 2016, War with China, Thinking Through the Unthinkable][research_gompert_2016_war_with_china]
- [Research, Greenway and Gustafson 2026, TIDALWAVE Executive Summary, Archived Copy][research_greenway_2026_tidalwave_archived]
- [Research, Gunzinger and Penney 2026, Rebuilding America's Air Force][research_gunzinger_2026_rebuilding_air_force]
- [Research, Heginbotham and others 2015, The U.S.-China Military Scorecard][research_heginbotham_2015_scorecard]
- [Research, Henley 2023, Beyond the First Battle, Overcoming a Protracted Blockade of Taiwan][research_henley_2023_beyond_first_battle]
- [Research, Heritage Foundation 2026, Limited Nuclear War Over Taiwan, An Initial Exercise][research_heritage_2026_limited_nuclear_war]
- [Research, Heritage Foundation 2026, TIDALWAVE Executive Summary][research_heritage_2026_tidalwave]
- [Research, Institute for Economics and Peace 2023, Global Peace Index, the Impact of a Chinese Blockade of Taiwan][research_iep_2023_gpi]
- [Research, Jensen, Lin and Ramos 2022, Shadow Risk, What Crisis Simulations Reveal][research_jensen_2022_shadow_risk]
- [Research, Jestrab 2023, A Maritime Blockade of Taiwan by the People's Republic of China][research_jestrab_2023_maritime_blockade]
- [Research, Jones 2023, Empty Bins in a Wartime Environment, The Challenge to the U.S. Defense Industrial Base][research_jones_2023_empty_bins]
- [Research, Kaushal and Suess 2024, The Impact of a Taiwan Strait Crisis on European Defence][research_rusi_2024_european_defence]
- [Research, Kilcrease 2023, No Winners in This Game][research_kilcrease_2023_no_winners]
- [Research, Lamparth and others 2024, Human versus Machine, Behavioral Differences in Wargame Simulations][research_lamparth_2024_human_vs_machine]
- [Research, Lloyd's and the Cambridge Centre for Risk Studies 2024, Geopolitical Conflict Systemic Risk Scenario][research_lloyds_2024_geopolitical_scenario]
- [Research, Ochmanek and others 2023, Inflection Point][research_ochmanek_2023_inflection_point]
- [Research, Payne 2026, AI Arms and Influence, Frontier Models in Simulated Nuclear Crises][research_payne_2026_ai_arms_influence]
- [Research, Pettyjohn and Dennis 2023, Avoiding the Brink, Escalation Management in a War to Defend Taiwan][research_pettyjohn_2023_avoiding_brink]
- [Research, Pettyjohn, Wasser and Dougherty 2022, Dangerous Straits, Wargaming a Future Conflict over Taiwan][research_pettyjohn_2022_dangerous_straits]
- [Research, Pettyjohn, Wasser and Metrick 2023, Bad Blood, a Tabletop Exercise for the House Select Committee][research_pettyjohn_2023_bad_blood]
- [Research, Pollard, Bouey, Wang and Pandey 2025, Fertility Decline in China and Its National Military, Structural, and Regime Security][research_pollard_2025_fertility_decline]
- [Research, Richter and Arostegui 2026, China Maritime Report 53, Filling the Ranks][research_richter_2026_filling_the_ranks]
- [Research, Rivera and others 2024, Escalation Risks from Language Models in Military and Diplomatic Decision-Making][research_rivera_2024_escalation_risks]
- [Research, Sasakawa Peace Foundation 2024, Table Top Exercise on the Taiwan Strait Crisis][research_spf_2024_taiwan_strait_ttx]
- [Research, Shatz and others 2025, Economic Deterrence in a China Contingency][research_shatz_2025_economic_deterrence]
- [Research, Sperzel and others 2025, Special Report on a Surprise Exercise Around Taiwan][research_isw_2025_justice_mission]
- [Research, Stares and Sacks 2025, The Next Taiwan Crisis Will Not Be Like the Last][research_stares_2025_next_taiwan_crisis]
- [Research, Vest and Kratz 2023, Sanctioning China in a Taiwan Crisis, Scenarios and Risks][research_vest_2023_sanctioning_china]
- [Research, Vest, Kratz and Goujon 2022, The Global Economic Disruptions from a Taiwan Conflict][research_rhodium_2022_disruptions]
- [Research, Wasser, Rasser and Kelley 2022, When the Chips Are Down, Gaming the Global Semiconductor Competition][research_wasser_2022_chips_down]
- [Research, Watterson and others 2026, Grey-Zone Games, Lessons from the 2025 Trilateral Simulation][research_ussc_2026_grey_zone_games]

[commentary_brands_beckley_2021_declining_power]: https://foreignpolicy.com/2021/09/24/china-great-power-united-states/
[commentary_brands_beckley_2022_danger_zone]: https://www.aei.org/research-products/book/danger-zone-the-coming-conflict-with-china/
[commentary_erickson_2025_dod_report_set]: https://www.andrewerickson.com/2025/12/u-s-department-of-defense-war-annual-reports-to-congress-on-chinas-military-power-2000-to-2025-download-complete-set-read-highlights-here/
[commentary_fuka_2025_coming_wave]: https://warontherocks.com/2025/11/the-coming-wave-chinese-doctrine-on-the-tabletop/
[commentary_heath_2023_wargames_deterrence]: https://www.rand.org/pubs/external_publications/EP70064.html
[commentary_howard_2026_peaked_power]: https://smallwarsjournal.com/2026/07/24/is-china-a-peaked-power-and-so-what-if-it-is/
[commentary_jensen_2024_democratize_wargaming]: https://www.csis.org/analysis/it-time-democratize-wargaming-using-generative-ai
[commentary_mastro_2021_taiwan_temptation]: https://www.foreignaffairs.com/articles/china/2021-06-03/china-taiwan-war-temptation
[commentary_mastro_scissors_2022_peak]: https://www.foreignaffairs.com/china/china-hasnt-reached-peak-its-power
[commentary_mcgrady_2019_getting_story_right]: https://warontherocks.com/2019/11/getting-the-story-right-about-wargaming/
[commentary_medeiros_2024_delusion_peak_china]: https://www.foreignaffairs.com/china/delusion-peak-china-united-states-evan-medeiros
[commentary_michaels_williams_2025_wargame_china_perspective]: https://warontherocks.com/2025/10/a-wargame-to-take-taiwan-from-chinas-perspective/
[commentary_ohanlon_2023_shrinking_population]: https://www.brookings.edu/articles/chinas-shrinking-population-and-constraints-on-its-future-power/
[commentary_panda_reddie_2026_ai_wargaming]: https://warontherocks.com/im-sorry-dave-im-afraid-i-cant-de-escalate-on-ai-wargaming-and-nuclear-war/
[commentary_schneider_2023_war_games_reveal]: https://www.foreignaffairs.com/united-states/what-war-games-really-reveal
[commentary_tetreau_2023_where_the_wargames_were_not]: https://warontherocks.com/2023/09/where-the-wargames-werent-assessing-10-years-of-u-s-chinese-military-assessments/
[data_bcg_sia_2021_value_chain]: https://www.semiconductors.org/wp-content/uploads/2021/05/BCG-x-SIA-Strengthening-the-Global-Semiconductor-Value-Chain-April-2021_1.pdf
[data_nbs_2024_communique]: https://www.stats.gov.cn/english/PressRelease/202502/t20250228_1958822.html
[data_nbs_2025_communique]: https://www.stats.gov.cn/english/PressRelease/202602/t20260228_1962661.html
[data_scio_2025_marriage_registrations]: http://english.scio.gov.cn/pressroom/2025-07/31/content_118005719.html
[data_trendforce_2023_foundry_capacity]: https://www.trendforce.com/presscenter/news/20231214-11959.html
[government_crs_2026_taiwan_defense]: https://www.congress.gov/crs-product/IF12481
[government_dod_2025_china_report]: https://media.defense.gov/2025/Dec/23/2003849070/-1/-1/1/ANNUAL-REPORT-TO-CONGRESS-MILITARY-AND-SECURITY-DEVELOPMENTS-INVOLVING-THE-PEOPLES-REPUBLIC-OF-CHINA-2025.PDF
[government_mnd_2025_defense_report]: https://www.mnd.gov.tw/en/File/54549
[government_odni_2026_threat_assessment]: https://archive.dni.gov/files/ODNI/documents/assessments/ATA-2026-Unclassified-Report.pdf
[government_prc_2022_taiwan_white_paper]: http://english.scio.gov.cn/whitepapers/2022-08/10/content_78365819.htm
[government_sasc_2021_indopacom]: https://www.armed-services.senate.gov/imo/media/doc/21-10_03-09-2021.pdf
[government_uscc_2025_taiwan_chapter]: https://www.uscc.gov/sites/default/files/2025-11/Chapter_11--Taiwan.pdf
[journal_beckley_2017]: https://doi.org/10.1162/isec_a_00294
[journal_biddle_oelrich_2016]: https://doi.org/10.1162/isec_a_00249
[journal_cancian_2025_states_of_denial]: https://doi.org/10.1080/00396338.2025.2481778
[journal_caverley_2025]: https://doi.org/10.1353/tns.00004
[journal_cunningham_2020_maritime_rung]: https://doi.org/10.1080/09636412.2020.1811462
[journal_cunningham_fravel_2015]: https://doi.org/10.1162/isec_a_00215
[journal_cunningham_fravel_2019]: https://doi.org/10.1162/isec_a_00359
[journal_curry_2020]: https://doi.org/10.1177/1046878120901852
[journal_davis_gholz_2026]: https://doi.org/10.1162/isec.a.407
[journal_downes_martin_2014]: https://digital-commons.usnwc.edu/nwc-review/vol67/iss1/5/
[journal_easton_2026_stratagems]: https://digital-commons.usnwc.edu/nwc-review/vol79/iss1/4/
[journal_glaser_fetter_2016]: https://doi.org/10.1162/isec_a_00248
[journal_goldstein_2013]: https://doi.org/10.1162/isec_a_00114
[journal_green_talmadge_2022]: https://doi.org/10.1162/isec_a_00437
[journal_harris_mckinney_2024]: https://doi.org/10.1093/ia/iiae071
[journal_heginbotham_samuels_2018]: https://doi.org/10.1162/isec_a_00313
[journal_hiim_2023]: https://doi.org/10.1162/isec_a_00457
[journal_kastner_2016]: https://doi.org/10.1162/isec_a_00227
[journal_kearn_2025]: https://doi.org/10.1080/01402390.2025.2572643
[journal_lin_greenberg_2022]: https://doi.org/10.1177/13540661211064090
[journal_mirski_2013]: https://doi.org/10.1080/01402390.2012.743885
[journal_montgomery_yoshihara_2025]: https://doi.org/10.1080/0163660X.2025.2479328
[journal_perla_mcgrady_2011]: https://digital-commons.usnwc.edu/nwc-review/vol64/iss3/8/
[journal_reddie_2018]: https://doi.org/10.1126/science.aav2135
[journal_reddie_goldblum_2023]: https://doi.org/10.1177/00223433221094734
[journal_talmadge_2017]: https://doi.org/10.1162/isec_a_00274
[journal_timbie_ellis_2021]: https://tnsr.org/2021/12/a-large-number-of-small-things-a-porcupine-strategy-for-taiwan/
[journal_verschuur_2025]: https://doi.org/10.1038/s41467-025-65403-w
[journal_wu_2020]: https://doi.org/10.1162/isec_a_00376
[journal_wu_2022]: https://doi.org/10.1162/isec_a_00428
[news_amac_2026_tidalwave]: https://amac.us/newsline/national-security/shocking-new-ai-driven-u-s-china-war-game-was-so-accurate-the-trump-administration-asked-for-redactions/
[news_insurance_journal_2026_bloomberg]: https://www.insurancejournal.com/news/international/2026/02/12/857770.htm
[news_newsweek_2026_tidalwave_redactions]: https://www.newsweek.com/us-government-requested-redactions-report-china-war-vulnerabilities-11391583
[news_reuters_marriages_2024]: https://kathmandupost.com/world/2025/02/10/chinese-marriages-slid-by-a-fifth-in-2024-fanning-birthrate-concerns
[news_taiwan_news_2024_bloomberg]: https://www.taiwannews.com.tw/news/5075352
[related_post_china_rise]: {% post_url 2026-03-23-china_rise %}
[related_post_industrialization_snapshot]: {% post_url 2026-03-26-contemporary_snapshot_and_extrapolation %}
[related_post_metagaming]: {% post_url 2026-01-14-metagaming_framework_for_life_strategy %}
[research_bartels_2020_building_better_games]: https://www.rand.org/pubs/rgs_dissertations/RGSD437.html
[research_blanchette_2023_scared_strait]: https://www.csis.org/analysis/scared-strait-understanding-economic-and-financial-impacts-taiwan-crisis
[research_cancian_2023_first_battle]: https://csis-website-prod.s3.amazonaws.com/s3fs-public/publication/230109_Cancian_FirstBattle_NextWar.pdf
[research_cancian_2024_confronting_armageddon]: https://csis-website-prod.s3.amazonaws.com/s3fs-public/2024-12/241213_Cancian_Confronting_Armageddon.pdf
[research_cancian_2025_lights_out]: https://csis-website-prod.s3.amazonaws.com/s3fs-public/2025-07/250730_Cancian_Taiwan_Blockade.pdf
[research_csis_2024_crossroads_commerce]: https://features.csis.org/chinapower/china-taiwan-strait-trade/
[research_dougherty_2021_poison_frog]: https://www.cnas.org/publications/reports/the-poison-frog-strategy
[research_erickson_2024_amphibious_warfare]: https://digital-commons.usnwc.edu/cmsi-studies/8/
[research_garlauskas_2025_guardian_tiger]: https://www.atlanticcouncil.org/in-depth-research-reports/report/a-rising-nuclear-double-threat-in-east-asia-insights-from-our-guardian-tiger-i-and-ii-tabletop-exercises/
[research_garlauskas_2026_aquatic_tiger]: https://www.atlanticcouncil.org/in-depth-research-reports/issue-brief/aquatic-tiger-how-long-range-submarine-drones-could-play-a-role-in-a-taiwan-conflict/
[research_geist_2024_ai_wargames_limits]: https://www.rand.org/pubs/research_reports/RRA1722-4.html
[research_goldfeld_2024_denial_without_disaster]: https://www.rand.org/pubs/research_reports/RRA2312-1.html
[research_gompert_2016_war_with_china]: https://www.rand.org/content/dam/rand/pubs/research_reports/RR1100/RR1140/RAND_RR1140.pdf
[research_greenway_2026_tidalwave_archived]: https://web.archive.org/web/20260414184735/https://www.heritage.org/tidalwave/introduction/executive-summary
[research_gunzinger_2026_rebuilding_air_force]: https://www.mitchellaerospacepower.org/app/uploads/2026/04/Rebuilding-Americas-Air-Force-FINAL.pdf
[research_heginbotham_2015_scorecard]: https://www.rand.org/pubs/research_reports/RR392.html
[research_henley_2023_beyond_first_battle]: https://digital-commons.usnwc.edu/cmsi-maritime-reports/26/
[research_heritage_2026_limited_nuclear_war]: https://www.heritage.org/defense/report/limited-nuclear-war-over-taiwan-initial-exercise
[research_heritage_2026_tidalwave]: https://www.heritage.org/tidalwave/introduction/executive-summary
[research_iep_2023_gpi]: https://www.economicsandpeace.org/wp-content/uploads/2023/09/GPI-2023-Web.pdf
[research_iiss_2023_deterrence_failure]: https://www.iiss.org/globalassets/pages---content--migration/blogs/research-paper/deterrence-failure-in-a-crossstrait-conflict-report.pdf
[research_isw_2025_justice_mission]: https://understandingwar.org/research/china-taiwan/china-taiwan-special-report-december-31-2025/
[research_jensen_2022_shadow_risk]: https://www.csis.org/analysis/shadow-risk-what-crisis-simulations-reveal-about-dangers-deferring-us-responses-chinas
[research_jestrab_2023_maritime_blockade]: https://www.atlanticcouncil.org/content-series/atlantic-council-strategy-paper-series/a-maritime-blockade-of-taiwan-by-the-peoples-republic-of-china-a-strategy-to-defeat-fear-and-coercion/
[research_jones_2023_empty_bins]: https://csis-website-prod.s3.amazonaws.com/s3fs-public/2023-01/230119_Jones_Empty_Bins.pdf
[research_kilcrease_2023_no_winners]: https://www.cnas.org/publications/reports/no-winners-in-this-game
[research_koerber_2021_policy_game]: https://koerber-stiftung.de/site/assets/files/19430/koerber-policy-game_escalation-in-the-taiwan-strait-1.pdf
[research_lamparth_2024_human_vs_machine]: https://arxiv.org/abs/2403.03407
[research_lloyds_2024_geopolitical_scenario]: https://www.lloyds.com/insights/media-centre/press-releases/geopolitical-conflict-scenario
[research_ochmanek_2023_inflection_point]: https://www.rand.org/pubs/research_reports/RRA2555-1.html
[research_payne_2026_ai_arms_influence]: https://arxiv.org/abs/2602.14740
[research_pettyjohn_2022_dangerous_straits]: https://s3.amazonaws.com/files.cnas.org/CNAS+Report-Dangerous+Straits-Defense-Jun+2022-FINAL-print.pdf
[research_pettyjohn_2023_avoiding_brink]: https://www.cnas.org/publications/reports/avoiding-the-brink
[research_pettyjohn_2023_bad_blood]: https://www.cnas.org/publications/congressional-testimony/bad-blood-ttx
[research_pollard_2025_fertility_decline]: https://www.rand.org/content/dam/rand/pubs/research_reports/RRA3300/RRA3372-1/RAND_RRA3372-1.pdf
[research_rhodium_2022_disruptions]: https://rhg.com/research/taiwan-economic-disruptions/
[research_richter_2026_filling_the_ranks]: https://digital-commons.usnwc.edu/cmsi-maritime-reports/53/
[research_rivera_2024_escalation_risks]: https://arxiv.org/abs/2401.03408
[research_rusi_2024_european_defence]: https://static.rusi.org/the-impact-of-a-taiwan-strait-crisis-on-european-defence.pdf
[research_shatz_2025_economic_deterrence]: https://www.rand.org/pubs/research_reports/RRA4022-1.html
[research_spf_2024_taiwan_strait_ttx]: https://www.spf.org/en/global-data/user33/report_ttx_thetaiwanstraitcrisis.pdf
[research_stares_2025_next_taiwan_crisis]: https://www.cfr.org/report/next-taiwan-crisis-wont-be-last
[research_ussc_2026_grey_zone_games]: https://www.ussc.edu.au/grey-zone-games-lessons-from-the-2025-australia-japan-united-states-simulation
[research_vest_2023_sanctioning_china]: https://www.atlanticcouncil.org/in-depth-research-reports/report/sanctioning-china-in-a-taiwan-crisis-scenarios-and-risks/
[research_wasser_2022_chips_down]: https://www.cnas.org/publications/reports/when-the-chips-are-down
