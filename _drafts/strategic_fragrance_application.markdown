---
layout: post
mathjax: true
comments: true
title:  "Strategic Fragrance Application Under the Three-Spray and Four-Spray Scenarios"
date:   2025-10-05 09:00:00 +0000
categories: lifestyle fragrance war-gaming
---

<!-- A377 -->
<script>console.log("A377");</script>

The question arrived in the following form.
"When it comes to fragrance application for men,
what are the conventional application points under the 3-push and 4-push scenarios?"
It was put to a general-purpose language model,
which answered in a planning register,
naming points and assigning sprays to them
as though the matter had been settled by doctrine.
It has not been settled.
The conventional answers are widely repeated,
mutually inconsistent in their details,
and almost never accompanied by a statement of what the application is meant to achieve,
against whom,
at what distance,
for how long,
or at what cost to the people who did not ask to be included.

This article treats the question as a planning problem and adjudicates it.
It generalises the question in three directions.
The wearer may be a man or a woman.
The application target may be a person,
an animal,
a bag,
a garment or a room.
The application platform may be a spray atomizer,
a rollerball,
a solid,
an oil or a mist.
The main line of the analysis concerns the case the question asked about,
spray-applied fine fragrance on a human wearer,
and the other targets and platforms are treated in shorter sections.

A hypothesis is stated before the analysis and adjudicated after it.
The hypothesis is that the conventional three-spray and four-spray doctrines are sound.
**It is partially supported.**
The conventional doctrines place fragrance at broadly defensible points
for reasons that are mostly wrong,
and they prescribe a dose that is too large for the indoor encounters
in which most fragrance is worn
and too small for the outdoor ones.
**The four-push scenario is adequate for a full working day
only when it is split into a morning application and a midday sequel**,
and in a small shared office no spray count is adequate at all,
because the room rather than the wearer becomes the source.
The difference between the conventional points for men and for women
turns out to be a difference in clothing and hair,
and it disappears when those are held fixed.

The article does five things the conventional literature does not.
It converts sprays into dose,
so that advice given for different products can be compared.
It models how dose becomes concentration at a receiver,
and shows that the detection radius grows only as the square root of the spray count.
It adjudicates six scenarios against stated constraints on detection, collateral and overkill.
It identifies the wearer as the least reliable judge of the application,
for a physiological reason that has been measured.
And it states which of its results are structural,
holding across every variation of its assumptions,
and which are calibrated and should be read as illustrations.

The article does not evaluate particular fragrances,
does not rank brands,
and does not offer a full analysis of offensive applications of aerosol delivery,
which are adjacent and are bounded in a short section near the end.

## The Question as Received, and Its Generalisation

### Terms

The question's unit is the push,
one depression of an atomizer pump,
which this article calls a spray or an actuation interchangeably.
An **application point** is a location on the target where a spray is placed.
**Projection** is the distance at which a fragrance can be detected by others,
and **[sillage][ref_sillage]** is the trade term for the trail a fragrance leaves in the air behind a moving wearer.
**Longevity** is the time over which it remains detectable at all.
The **wearer** is the person who applies the fragrance to themselves.
A **receiver** is anyone who might detect it.
An **intended receiver** is a receiver the application is meant to reach,
and an **unintended receiver** is anyone else.
The **end state** is the condition the application is meant to produce,
stated in terms of who detects the fragrance, at what distance and for how long.

### What the conventional answer leaves unstated

The conventional answer to the question as asked can be summarised quickly,
and it is set out in detail in the section on placement.
For men it places three sprays on the two sides of the neck and the chest,
and a fourth on the back of the neck or the wrists.
For women it places sprays on the wrists, the neck, behind the ears, the décolletage and the hair,
with the inner elbows and the backs of the knees as further options.

What the conventional answer does not state is the end state.
A three-push plan intended to be noticed by a dinner companion at half a metre
and a three-push plan intended to be noticed by a colleague across an open-plan office
are different plans that happen to share a spray count.
The same spray count in a different product is a different dose.
The same dose in a different room is a different exposure.
**An application point cannot be evaluated without an end state,
and a spray count cannot be evaluated without a product, a room and a distance.**
This article supplies those,
which is the whole of the difference between the question as received and the question as adjudicated.

### The generalisation

The adjudicated question is the following.
Given a wearer,
a fragrance of known concentration delivered by a known platform,
an application target,
and a scenario specifying receivers, distances, air and duration,
which spray count and which application points meet the end state
without unacceptable collateral or overkill,
and do the conventional answers coincide with them?

## A Brief History of Where Fragrance Goes

The question of where to put fragrance is older than the spray,
and the spray changed the question.

The earliest perfumer known by name is
[Tapputi][ref_tapputi],
recorded on a cuneiform tablet from Assur of about 1200 BC.
Egyptian practice used fragrant oils and unguents applied by hand,
held in jars of the kind the [Metropolitan Museum of Art][history_met_ointment_jar] preserves,
and the incense [kyphi][ref_kyphi],
which was burned to scent spaces rather than applied to people.
The conical headpieces shown in Egyptian tomb paintings
were long read as cones of scented fat that melted onto the wearer.
The two such cones recovered from Amarna and examined by
[Stevens and colleagues][research_stevens_2019_head_cones]
turned out to be hollow and made of wax,
and the authors read them as symbolic rather than as a fragrance platform,
so that interpretation is best treated as unresolved.

Hand application persisted for three thousand years,
and with it a dosing regime set by the finger and the stopper rather than by the pump.
[Eau de Cologne][history_farina_dpma],
the dilute citrus water whose name became the generic term for a light fragrance,
dates to the Farina business founded in Cologne in July 1709,
and it was splashed and dabbed.
Eugène Rimmel, the London perfumer,
advertised himself in 1862 as the patentee of a
[perfume vaporiser for balls, soirées and theatres][history_bodleian_rimmel],
a device for scenting rooms rather than people,
and he also sold [perfumed valentines][history_vam_rimmel_valentine],
an early instance of fragrance applied to paper.
The personal atomizer came from medicine.
Allen DeVilbiss, a physician in Toledo, Ohio, built atomizers for the nose and throat,
and his son Thomas turned the company toward perfume atomizers,
which became its best-selling product
according to the [University of Toledo's account][history_utoledo_devilbiss].
Secondary accounts date the move into perfume to about 1907.

**The spray made the dose discrete.**
A splash or a dab has no natural unit,
while a pump delivers a fixed volume each time it is pressed,
which is the only reason the question can be asked in pushes at all.
Modern fine-fragrance pumps are manufactured to nominal doses,
and [Aptar's VP4 pump][primary_aptar_vp4],
a widely used fragrance pump,
is offered at 70, 100 and 140 microlitres per actuation.
The planning value of 0.10 mL used in this article is the middle of that range.
It also gives the number of actuations in a 100 mL bottle
as somewhere between 714 and 1,429 depending on the pump,
and 1,000 at the planning value.

## The Hypothesis

A hypothesis that cannot fail is not worth adjudicating,
so this one is stated with its rejection criteria attached.

**Hypothesis.**
The conventional three-spray and four-spray doctrines are sound
for spray-applied fine fragrance on a human wearer.
The claim decomposes into three parts,
each of which can be supported or rejected independently.

- **H1, dose.**
  Three or four sprays is the smallest dose that meets a conversational-distance end state
  without unacceptable collateral or overkill,
  and the fourth spray adds less than the third.
- **H2, placement.**
  The conventional application points are chosen for the mechanism that actually operates,
  which the conventional literature names as warmth at the pulse points.
- **H3, the wearer.**
  The difference between the conventional application points for men and for women
  is a property of clothing and hair rather than of the wearer's sex.

**Rejection criteria.**
H1 is rejected in a scenario if the smallest adequate dose there is not three or four sprays,
or if no dose is adequate.
H2 is rejected if the named mechanism is not the operative one,
and partially supported if the named mechanism operates but does not dominate.
H3 is rejected if the wearer's sex changes the preferred points
once clothing, hair and the identity of the intended receiver are held fixed.
The overall hypothesis is supported only if all three parts are supported,
rejected if all three are rejected,
and partially supported otherwise.

The criteria were written before the adjudication was run,
and the scenario parameters were not revised after the results were seen,
with one exception that is recorded in the Epistemic State section.

## Planning Assumptions, Constraints and Restraints

Every quantity the adjudication uses is listed here with its class.
**Measured** quantities come from a cited source.
**Calibrated** quantities were chosen so that the model reproduces
a commonly reported qualitative outcome,
and they carry the weakest warrant in the article.
**Assumed** quantities are planning values that a reader with better data should replace.

| Symbol | Quantity | Planning value | Class |
|---|---|---|---|
| $v_s$ | Volume delivered per actuation | 0.10 mL | Measured range, value assumed |
| $\rho$ | Density of the finished fragrance | 0.82 g/mL | Assumed from the ethanol density |
| $c$ | Mass fraction of aromatic compounds | 0.03 to 0.25 by class | Measured range |
| $\eta$ | Fraction of the spray that lands on the target | 0.70 | Assumed |
| $\tau$ | Lumped emission time constant | 3 h | Assumed |
| $u$ | Air speed past the wearer | 0.1 m/s indoors, 1.0 m/s outdoors | Assumed |
| $a$ | Plume spread per metre of distance | 0.3 | Assumed |
| $C_{50}$ | Median detection concentration of the blend, in total aromatic mass | 30 µg/m³ | Calibrated |
| $\sigma$ | Spread of receiver thresholds, natural log units | 1.2 | Assumed |
| $C_{\mathrm{over}}$ | Median concentration judged too strong | $30\,C_{50}$ | Assumed |
| $V$, $\lambda$ | Room volume and air change rate | By scenario | Measured range |

The calibrated threshold deserves a sentence of defence.
Individual fragrance materials are detected at very low concentrations,
linalool at 3.2 ng/L, which is 3.2 µg/m³,
according to [Elsharif, Banerjee and Buettner][research_elsharif_2015_linalool].
A blend is diluted in its own carrier of weaker materials,
so if its most potent constituents make up a few percent of its aromatic mass,
the blend's threshold expressed in total aromatic mass is of order tens of µg/m³.
The value of 30 µg/m³ was then chosen so that three sprays of eau de parfum
are detectable at a little under two metres indoors when fresh,
which matches the projection the trade literature commonly describes.
It is the weakest number in the article,
and the sensitivity analysis varies it by a factor of three in each direction.

The scenario distances follow Edward Hall's [proxemic zones][ref_proxemics],
in which intimate distance extends to about 0.46 m,
personal distance to 1.2 m
and social distance to 3.7 m.

**Constraints** are conditions the plan must satisfy.
The adjudication imposes three.
An intended receiver must detect the fragrance more often than not,
an unintended receiver must detect it no more than one time in five,
and an intended receiver must find it too strong no more than one time in ten.
**Restraints** are actions the plan may not take regardless of effect.
The plan may not apply fragrance to a person who has not consented,
may not exceed the limits set out in the safety section,
and may not treat the wearer's own nose as a measuring instrument,
for reasons established in a later section.

## The Dose Model

### Mass per actuation

The quantity that matters is not the number of sprays
but the mass of aromatic material placed on the target.
Write $N$ for the number of actuations,
$v_s$ for the volume each delivers in millilitres,
$\rho$ for the density of the finished product in grams per millilitre,
$c$ for the mass fraction of aromatic compounds,
and $\eta$ for the fraction of the sprayed mass that lands on the target rather than in the air around it.
The deposited aromatic mass $m_0$ in grams is then the product.

$$
m_0 = N \, v_s \, \rho \, c \, \eta
$$

For an eau de parfum at fifteen percent,
one actuation of 0.10 mL at 0.82 g/mL carries
$0.10 \times 0.82 \times 0.15 = 0.0123$ g,
or 12.3 mg of aromatic material before deposition losses.
Three actuations deposit
$3 \times 12.3 \times 0.70 = 25.8$ mg on the wearer,
and four deposit 34.4 mg.
Not all of the deposited mass reaches the air.
Some is absorbed through the skin,
and [Bronaugh and colleagues][research_bronaugh_1990_absorption]
found that on unoccluded skin absorption varied widely between fragrance compounds,
presumably because evaporation competes with penetration,
while under occlusion more than half of the applied dose of the compound tested in humans was absorbed.
Clothing over an application point is a partial occlusion,
which is one reason the adjudication treats covered skin as a slower and lossier point.
The figure that a reader should carry forward is that
**the entire three-spray scenario concerns about a quarter of a gram of product
and about twenty-six milligrams of the material that is actually smelled.**

### The spray-equivalent

The original question was posed in sprays,
and a spray is not a unit of dose.
Four sprays of an eau de toilette at ten percent
and four sprays of an extrait at twenty-five percent
differ in aromatic mass by a factor of two and a half.
Define the spray-equivalent $N_{\mathrm{eq}}$
as the dose expressed in actuations of a reference eau de parfum at $c_{\mathrm{ref}} = 0.15$,
holding the pump volume and density fixed.

$$
N_{\mathrm{eq}} = N \, \frac{c}{c_{\mathrm{ref}}}
$$

Four sprays of eau de toilette are $4 \times 0.10 / 0.15 = 2.7$ spray-equivalents.
Three sprays of an extrait at twenty-five percent are 5.0.
Ten sprays of a body mist at two percent are 1.3.
**The three-push and four-push scenarios are therefore not comparable across products
until they are converted**,
and much of the disagreement in published application advice
is advice about different doses expressed in the same unit.
Every result below is stated for the reference eau de parfum unless another class is named.

| Class | Aromatic fraction, planning value | Mass per actuation | Spray-equivalents per actuation |
|---|---|---|---|
| Body mist | 0.02 | 1.6 mg | 0.13 |
| Eau de cologne | 0.03 | 2.5 mg | 0.20 |
| Eau de toilette | 0.10 | 8.2 mg | 0.67 |
| Eau de parfum | 0.15 | 12.3 mg | 1.00 |
| Extrait or parfum | 0.25 | 20.5 mg | 1.67 |

## Emission and Decay

### The lumped emission model

A fragrance is a mixture of compounds with volatilities spanning several orders of magnitude,
which is the physical basis of the [top, heart and base structure][ref_note_perfumery] described in the trade literature.
Perfume engineering models each component separately,
computing headspace concentrations from activity coefficients
and dividing by each component's detection threshold to obtain an odour value,
an approach developed by the Rodrigues group at Porto
from [Mata, Gomes and Rodrigues][research_mata_2005_engineering_perfumes]
onward and summarised by [Rodrigues, Nogueira and Faria][research_rodrigues_2021_perfume_engineering].
The adjudication collapses that mixture into a single pool
that empties at a rate proportional to what remains.
Write $\tau$ for the emission time constant in hours
and $t$ for the time since application.
The emission rate $q$ in micrograms per second is then as follows.

$$
q(t) = \frac{m_0}{\tau} \, e^{-t/\tau}
$$

With $m_0 = 25.8$ mg and $\tau = 3$ h,
the initial emission rate is
$25{,}830 \text{ µg} / 10{,}800 \text{ s} = 2.39$ µg/s.
Eight hours later it has fallen by a factor of $e^{8/3} = 14$.

This is the first simplification that a reader should distrust.
A real fragrance front-loads its most volatile material,
so the early emission is higher than the lumped model says
and the late emission comes from a smaller and heavier residue.
The adjudication results that depend on this simplification are flagged where they appear.

### Temperature

Evaporation from skin is governed by the vapour pressure of each compound,
which rises steeply with temperature.
The [Clausius and Clapeyron relation][ref_clausius_clapeyron] gives the ratio of vapour pressures,
and therefore approximately of emission rates,
at two absolute temperatures $T_1$ and $T_2$
for a compound with molar enthalpy of vaporisation $\Delta H_{\mathrm{vap}}$,
where $R$ is the molar gas constant.

$$
\frac{q(T_2)}{q(T_1)} \approx \frac{p(T_2)}{p(T_1)}
= \exp\!\left[ \frac{\Delta H_{\mathrm{vap}}}{R} \left( \frac{1}{T_1} - \frac{1}{T_2} \right) \right]
$$

For linalool, a common heart-note material,
the [Chemistry WebBook][data_nist_linalool]
of the National Institute of Standards and Technology
gives a measured enthalpy of vaporisation of 50.3 kJ/mol near its boiling point
and standard values of 55.3 and 65.0 kJ/mol from two extrapolations.
Skin is not uniformly warm.
In normal-weight adults at rest in a thermoneutral room,
[Savastano and colleagues][research_savastano_2009_regional_temperature]
measured abdominal skin at 32.8 °C and the fingernail bed at 28.6 °C,
and the extremities are generally cooler than the trunk,
as [Webb's][research_webb_1992_skin_temperature] sixteen-site measurements also show.
Taking $\Delta H_{\mathrm{vap}} = 55.3$ kJ/mol,
$T_1 = 301.75$ K for the coolest distal skin
and $T_2 = 305.95$ K for the trunk,
the ratio is as follows.

$$
\frac{q(305.95)}{q(301.75)}
= \exp\!\left[ \frac{55{,}300}{8.314} \left( \frac{1}{301.75} - \frac{1}{305.95} \right) \right]
= 1.35
$$

Across the three enthalpies the factor runs from 1.32 to 1.43,
and for a more typical two-kelvin difference between wrist and trunk it is about 1.15.
**Warmer skin emits faster and is exhausted sooner.**
It does not emit more in total,
because the mass is fixed at application.
Since the detection radius at application scales as the square root of the emission rate,
the entire temperature advantage of trunk over extremity
is worth $\sqrt{1.35} = 1.16$ in starting radius,
which is almost exactly what a fourth spray adds to three.
The temperature effect is real,
it is the only part of the pulse-point rationale with a physical mechanism,
and it is the size of one spray in four.

## Transport to the Receiver

### The near field

Between the wearer and a receiver at conversational distance,
the fragrance travels as a plume carried and diluted by moving air.
Indoors much of that air movement is generated by the wearer.
A standing person heats the surrounding air and drives a rising boundary layer,
which [Craven and Settles][research_craven_settles_2006_thermal_plume]
measured as a plume reaching a time-averaged vertical velocity of about 0.24 m/s
some 0.4 m above the head.
Fragrance placed anywhere on the torso is collected by that flow and carried upward past the face,
which matters for placement and is taken up in that section.
A [Gaussian plume][ref_atmospheric_dispersion] from a continuous point source has a centreline concentration
inversely proportional to the air speed and to the product of its two lateral spreads.
Taking both spreads to grow linearly with distance, $\sigma = a\,r$,
the concentration $C$ at distance $r$ in metres is as follows.

$$
C(r, t) = \frac{q(t)}{\pi \, u \, a^2 \, r^2}
$$

At $t = 0$, three sprays, $u = 0.1$ m/s and $a = 0.3$,
the concentration at one metre is
$2.39 / (\pi \times 0.1 \times 0.09 \times 1) = 85$ µg/m³.
At half a metre it is four times that, 338 µg/m³,
and at the wearer's own nose, about 0.2 m from the neck, it is 2,100 µg/m³.

### The detection radius

Setting $C(r) = C_{50}$ and solving for $r$
gives the distance $r^{*}$ at which the median receiver can just detect the fragrance.

$$
r^{*}(t) = \sqrt{ \frac{q(t)}{\pi \, u \, a^2 \, C_{50}} }
= \sqrt{ \frac{N \, v_s \, \rho \, c \, \eta}{\pi \, u \, a^2 \, C_{50} \, \tau} } \; e^{-t/2\tau}
$$

**This is the central result on dose,
and it does not depend on the calibrated threshold in the way the absolute numbers do.**
The detection radius grows with the square root of the spray count.
Going from three sprays to four multiplies the radius by $\sqrt{4/3} = 1.155$
and the detected area by $4/3$.
Doubling the dose buys forty-one percent more radius.
The absolute radius at application is 1.68 m for three sprays indoors
and 1.94 m for four,
but those numbers inherit the calibration of $C_{50}$
and are illustrative rather than predictive.

The same expression yields a half-life for the radius.
Because the radius decays as $e^{-t/2\tau}$,
it halves after $2\tau \ln 2$.

$$
t_{1/2}^{(r)} = 2\,\tau \ln 2 = 4.16 \text{ h} \quad \text{for } \tau = 3 \text{ h}
$$

**The radius half-life is independent of dose.**
No spray count changes how quickly the projected footprint shrinks.
Dose sets the starting radius and nothing else.

### Wind

Outdoors the air speed past the wearer rises by about an order of magnitude.
Because the concentration is inversely proportional to $u$,
the detection radius scales as $u^{-1/2}$.
A breeze of 1.0 m/s shrinks the three-spray radius from 1.68 m to 0.53 m,
and recovering the indoor radius outdoors requires ten times the dose,
which is thirty sprays.
**No conventional spray count projects outdoors in moving air the way it does indoors**,
and this is the one regime where the four-push scenario is underpowered rather than overpowered.

### The far field, where the room becomes the source

In an enclosed space the plume does not leave.
Ventilation rates span an order of magnitude.
The United States Environmental Protection Agency's
[Exposure Factors Handbook][data_epa_efh_ch19]
recommends a median of 0.45 air changes per hour for residences
and reports a mean of 1.5 for non-residential buildings.
Treat the room as a well-mixed volume $V$ in cubic metres
ventilated at an air change rate $\lambda$ per hour.
The room concentration $C_{\mathrm{room}}$ obeys a mass balance
in which the wearer's emission enters and the ventilation removes a fixed fraction per hour.

$$
\frac{dC_{\mathrm{room}}}{dt} = \frac{q(t)}{V} - \lambda \, C_{\mathrm{room}},
\qquad C_{\mathrm{room}}(0) = 0
$$

With the exponentially decaying source, the solution is as follows.

$$
C_{\mathrm{room}}(t) = \frac{m_0}{\tau V} \cdot \frac{e^{-t/\tau} - e^{-\lambda t}}{\lambda - 1/\tau}
$$

It peaks when its derivative vanishes.

$$
t_{\mathrm{peak}} = \frac{\ln(\lambda \tau)}{\lambda - 1/\tau}
$$

For a shared office of 30 m³ at one air change per hour,
three sprays peak at $t = \ln 3 / (2/3) = 1.65$ h
with a room concentration of 166 µg/m³.
At that moment the plume adds only 49 µg/m³ at one metre.
**The room concentration exceeds the near-field concentration at conversational distance
from twenty minutes after application onward,
and it is the same everywhere in the room.**
In that regime the wearer is no longer the source in any operational sense.
The room is the source,
and every occupant is a receiver whether intended or not.
This is the condition the trade literature describes as a fragrance that fills a room,
and it is area denial in the literal sense of the term.

The open-plan office of 500 m³ at two air changes per hour
holds the same three sprays at a peak of 6.0 µg/m³ after 1.08 h,
a fifth of the median threshold,
so the near field governs and the wearer remains the source.
The difference between the two offices is a factor of thirty-three in $\lambda V$,
and it decides the scenario before spray count is considered.

## Perception

### Intensity grows slowly with concentration

Perceived odour intensity $\psi$ follows [Stevens' power law][ref_stevens_power_law]
in concentration,
introduced in [Stevens' 1957 paper][research_stevens_1957_psychophysical_law],
with an exponent $n$ well below one.
The table of exponents reproduced by
[Moskowitz and colleagues][research_moskowitz_1979_psychophysical]
gives 0.55 for coffee odour and 0.6 for heptane,
and they note values as low as 0.2 to 0.3 for some odorants in a liquid diluent.
The constant $k$ sets the scale and drops out of every ratio used here.

$$
\psi = k \, C^{\,n}
$$

With $n = 0.5$ the fourth spray raises perceived intensity at a fixed distance
by $(4/3)^{0.5} - 1 = 15$ percent.
With $n = 0.3$ it raises it by 9 percent.
**The fourth spray is mostly invisible to a receiver who was already detecting the third**,
and mostly visible to receivers who were not,
because detection is a threshold event and intensity is not.

### Receivers differ

Receivers do not share a threshold.
Detection ability falls with age,
and in the large sample of [Doty and colleagues][research_doty_1984_age]
more than half of those aged 65 to 80 showed major impairment of smell identification.
It differs slightly by sex,
in a direction and size taken up in the section on the wearer.
And it fails entirely for some compounds in some people.
[Sato-Akuhara and colleagues][research_sato_akuhara_2023_musk]
cite specific anosmia to the musk exaltolide in 7.2 to 9 percent of people of European descent
and to muscone in 6 percent,
and [Keller and colleagues][research_keller_2007_or7d4]
tied variation in one odorant receptor gene to differences in how androstenone is perceived.
A musk-heavy fragrance therefore has receivers for whom no dose is detectable,
and the wearer may be one of them.
The adjudication represents this by a log-normal distribution of thresholds,
so the probability that a receiver drawn at random detects concentration $C$
is the standard normal distribution function $\Phi$ of the log ratio.

$$
P_{\mathrm{det}}(C) = \Phi\!\left( \frac{\ln C - \ln C_{50}}{\sigma} \right)
$$

The same form with $C_{\mathrm{over}}$ in place of $C_{50}$
gives the probability $P_{\mathrm{over}}$ that a receiver finds the fragrance too strong.
With $\sigma = 1.2$, one standard deviation of threshold is a factor of $e^{1.2} = 3.3$ in concentration,
so a receiver at the sixteenth percentile of sensitivity
needs 3.3 times the concentration the median receiver needs.

**Overkill is a near-field phenomenon.**
At half a metre, fifteen minutes after application,
one spray produces about 104 µg/m³ and a four percent chance that the receiver finds it too strong.
Three sprays produce 311 µg/m³ and a nineteen percent chance.
At 0.3 m, which is the distance of an embrace,
three sprays produce a forty-nine percent chance.
The conventional three-push is therefore adjudicated,
at intimate distance and in the first hour,
as about as likely to be judged excessive as not.

## The Wearer Is the Least Reliable Sensor

Every receiver in the adjudication is somebody other than the wearer,
and that is deliberate.
The wearer is the one receiver whose readings cannot be used.

### Adaptation

Continuous exposure to an odour reduces its perceived intensity within minutes,
and the effect is strongest for the person closest to the source.
[Dalton's review of olfactory adaptation][research_dalton_2000_adaptation]
describes a stimulus-specific loss of sensitivity during exposure,
with raised thresholds and reduced intensity above threshold,
both depending on the concentration and the duration of exposure,
and notes that the effect can be very long-lasting.
The review does not supply the time constants used below,
which are planning values chosen to be conservative about how fast adaptation sets in.
The wearer is the receiver with the highest exposure by an order of magnitude.
At 0.2 m from a neck application the near-field equation gives 2,100 µg/m³ at application,
twenty-five times what a receiver at one metre experiences.
Model the wearer's perceived intensity relative to its initial value
as an adaptation factor $A(t)$ that decays from one toward a floor $\beta$
with a time constant $\tau_a$.

$$
A(t) = \beta + (1 - \beta)\, e^{-t/\tau_a}
$$

With an assumed floor of $\beta = 0.3$ and an assumed $\tau_a = 5$ min,
the wearer perceives half the initial intensity when
$e^{-t/\tau_a} = (0.5 - 0.3)/(1 - 0.3)$,
which is at $t = 5 \ln 3.5 = 6.3$ min.
At that moment the emission rate is still
$e^{-6.3/180} = 0.966$ of its initial value.

**Six minutes after application the wearer believes half the fragrance has gone,
and ninety-seven percent of the emission is still present.**

### The reapplication spiral

A wearer who uses perceived intensity as the measure of effectiveness
and reapplies when it falls to half
will reapply at about six minutes,
adapt to the new level,
and reapply again.
Each cycle adds dose that every other receiver perceives at full sensitivity,
because no other receiver has spent the morning at 0.2 m from the source.
The process has no internal stopping condition.
It ends at the bottle, at the schedule, or at a remark from a colleague,
and the remark is the only one of the three that carries information about the end state.

This is the mechanism behind the overapplication that the trade literature warns against,
and the adjudication's restraint follows from it.
**The wearer may not use self-perception to decide whether to reapply.**
Reapplication is scheduled in advance as a sequel, as in the open-plan case,
or triggered by an independent observer.
The independent observer serves as the plan's red cell,
a receiver who did not participate in the application
and whose report is therefore not contaminated by it.
A red cell can be a household member asked at the door,
and it is the cheapest instrument in this article.

A secondary effect compounds the first.
The wearer adapts not only during the day
but across days to a fragrance worn daily,
so a signature fragrance is perceived more weakly by its wearer each month
while it is perceived identically by everyone else.
The sensible response is to hold the dose fixed by count
and to ignore the impression that the fragrance has grown weaker,
because the impression measures the wearer and not the fragrance.

## Scenarios and Adjudication

### The scenarios

Six scenarios were defined before the adjudication was run.
Each states an end state,
the distance to the intended receiver,
the distance to the nearest unintended receiver,
and the air in which the encounter takes place.

| Scenario | Window after application | Intended receiver | Unintended receiver | Air |
|---|---|---|---|---|
| S1 shared office | 0.5 to 8.5 h | 1.0 m | 2.5 m | 30 m³, 1 change per hour |
| S2 open-plan office | 0.5 to 8.5 h | 1.0 m | 2.5 m | 500 m³, 2 changes per hour |
| S3 interview | 0.5 to 1.5 h | 1.5 m | None | 30 m³, 1 change per hour |
| S4 dinner | 0.25 to 4.25 h | 0.5 m | 2.0 m | 200 m³, 3 changes per hour |
| S5 outdoor event | 0.25 to 4.25 h | 0.5 m | 3.0 m | Open air, 1.0 m/s |
| S6 elevator | 0.5 to 0.55 h | None | 0.6 m | Still air, 0.1 m/s |

The elevator is not an end state anyone seeks.
It is a phase line that every morning application crosses on the way to S1 or S2,
and it is adjudicated as a constraint on those scenarios.

### Measures of effectiveness

For each course of action the adjudication computes three measures,
each averaged over the scenario's time window.
**Detection** $D$ is the mean probability that the intended receiver detects the fragrance.
**Collateral** $K$ is the mean probability that the unintended receiver does.
**Overkill** $O$ is the mean probability that the intended receiver finds it too strong.
The concentration at each receiver is the near-field plume plus the room term.

$$
D = \frac{1}{t_1 - t_0} \int_{t_0}^{t_1}
P_{\mathrm{det}}\!\big( C(r_i, t) + C_{\mathrm{room}}(t) \big) \, dt
$$

$K$ and $O$ follow by replacing $r_i$ with the unintended receiver's distance $r_u$,
or $C_{50}$ with $C_{\mathrm{over}}$.
A course of action is **feasible** when $D \geq 0.5$, $K \leq 0.2$ and $O \leq 0.1$.
The recommended course of action in each scenario
is the smallest feasible spray count,
because any spray beyond it buys detection the end state does not require
at a cost in collateral and product.

### Results for the reference eau de parfum

Each cell gives $D$, $K$ and $O$ in that order.

| Scenario | N = 1 | N = 2 | N = 3 | N = 4 | N = 5 | N = 6 |
|---|---|---|---|---|---|---|
| S1 shared office | 0.53 / 0.48 / 0.01 | 0.72 / 0.68 / 0.03 | 0.81 / 0.78 / 0.05 | 0.86 / 0.84 / 0.08 | 0.90 / 0.87 / 0.11 | 0.92 / 0.90 / 0.13 |
| S2 open-plan office | 0.16 / 0.02 / 0.00 | 0.30 / 0.06 / 0.00 | 0.40 / 0.11 / 0.00 | 0.48 / 0.15 / 0.01 | 0.54 / 0.19 / 0.01 ✓ | 0.59 / 0.23 / 0.01 |
| S3 interview | 0.70 / . / 0.01 ✓ | 0.87 / . / 0.04 ✓ | 0.93 / . / 0.08 ✓ | 0.95 / . / 0.13 | 0.97 / . / 0.17 | 0.98 / . / 0.21 |
| S4 dinner | 0.69 / 0.09 / 0.01 ✓ | 0.85 / 0.22 / 0.05 | 0.91 / 0.33 / 0.09 | 0.94 / 0.42 / 0.13 | 0.96 / 0.49 / 0.18 | 0.97 / 0.54 / 0.22 |
| S5 outdoor | 0.09 / 0.00 / 0.00 | 0.21 / 0.00 / 0.00 | 0.31 / 0.00 / 0.00 | 0.39 / 0.00 / 0.00 | 0.46 / 0.00 / 0.00 | 0.52 / 0.00 / 0.00 ✓ |
| S6 elevator | . / 0.74 / . | . / 0.89 / . | . / 0.94 / . | . / 0.96 / . | . / 0.98 / . | . / 0.98 / . |


A check mark denotes a feasible course of action,
and a full stop denotes a measure that does not apply because the scenario has no such receiver.

**S1, the shared office, has no feasible course of action at any spray count.**
Detection and collateral rise together and never separate by more than five points,
because from twenty minutes onward the room term dominates both receivers equally.
The office mate at 2.5 m smells what the visitor at 1.0 m smells.
This result survived every sensitivity case in the next subsection,
since it is a property of the room term and not of the threshold.
The conventional three-push in this scenario
delivers 0.81 detection to the intended receiver
and 0.78 to the unintended one.

**S2, the open-plan office, is feasible at five sprays and at no smaller single dose.**
The large ventilated volume keeps the room term low,
so collateral stays bounded,
but the eight-hour window asks a decaying source to perform at hour eight as it did at hour one.
The conventional four-push misses the detection constraint by two points.

**S3, the interview, is feasible from one spray to three.**
The smallest feasible dose is one.
The scenario's difficulty is not dose but the sign of the objective,
which is taken up separately below.

**S4, dinner, is feasible at one spray and at nothing larger.**
At half a metre the near field is strong,
so a single spray is detected more often than not across four hours,
and the second spray already pushes the diner at the next table past the collateral constraint.
The conventional three-push violates the collateral constraint by thirteen points.

**S5, the outdoor event, is feasible only at six sprays.**
Moving air dilutes by a factor of ten,
and nothing below six reaches the detection constraint at half a metre.
This is the only scenario in which more than four sprays is the adjudicated answer,
and it is also the least robust result in the table.

**S6, the elevator, is violated by every morning application.**
Thirty minutes after a single spray,
a passenger at 0.6 m detects the wearer with probability 0.74.
No spray count from one to six reduces that below the collateral constraint,
so the elevator is not a decision point at all.
It is a standing cost of any nonzero course of action,
and the plan must either accept it or apply after the commute.

### Concentration classes

Repeating the adjudication for the other two common classes
moves the smallest feasible dose in the expected direction
and changes no qualitative result.

| Scenario | Eau de toilette | Eau de parfum | Extrait |
|---|---|---|---|
| S1 shared office | None | None | None |
| S2 open-plan office | None up to six | 5 | 3 |
| S3 interview | 1 | 1 | 1 |
| S4 dinner | 1 | 1 | 1 |
| S5 outdoor event | None up to six | 6 | 4 |
| S6 elevator | Standing cost | Standing cost | Standing cost |

The conventional three-push appears as the smallest feasible dose exactly once,
for an extrait in the open-plan office.
The four-push appears exactly once,
for an extrait outdoors.

### The sequel, in which the four-push is split

The open-plan result is driven by exponential decay over an eight-hour window,
and the obvious response is to treat the day as two phases.
A sequel is an application planned in advance for a later phase,
here at 4.5 h, which is about the middle of the working day.
Concentrations from the two applications add,
since both the plume and the room equations are linear in the source.

| Morning sprays | Midday sprays | Total | $D$ | $K$ | $O$ | Feasible |
|---|---|---|---|---|---|---|
| 3 | 0 | 3 | 0.40 | 0.11 | 0.00 | No |
| 4 | 0 | 4 | 0.48 | 0.15 | 0.01 | No |
| 6 | 0 | 6 | 0.59 | 0.23 | 0.01 | No |
| 2 | 1 | 3 | 0.44 | 0.10 | 0.00 | No |
| 2 | 2 | 4 | 0.53 | 0.15 | 0.00 | Yes |
| 3 | 1 | 4 | 0.53 | 0.15 | 0.00 | Yes |
| 3 | 2 | 5 | 0.60 | 0.19 | 0.01 | Yes |

**Four sprays split as three and one, or two and two,
achieve what five sprays applied at once achieve, with one spray fewer.**
The reason is visible in the decay model.
A spray applied at seven in the morning spends most of its mass before the afternoon,
and a spray applied at noon spends its mass when the end state still needs it.
Holding the morning emission rate at hour eight with a single application
would require $e^{7.5/3} = 12$ times the dose,
almost all of which would be emitted in the morning as collateral.
**The four-push scenario, executed as a single application, is the wrong plan.
Executed as a sequel, it is the smallest adequate plan for the full working day.**

The sequel has a sustainment requirement,
which is that the wearer carries a second platform to the midday decision point.
That requirement is taken up in the section on application platforms.

### Sensitivity

The calibrated threshold and four assumed parameters were varied one at a time.
Each cell gives the smallest feasible single application of eau de parfum.

| Case | S1 | S2 | S3 | S4 | S5 | S6 |
|---|---|---|---|---|---|---|
| Base case | None | 5 | 1 | 1 | 6 | Cost |
| Threshold tripled to 90 µg/m³ | None | None | 2 | 2 | None | Cost |
| Threshold divided by three to 10 µg/m³ | None | None | 1 | None | 2 | Cost |
| Time constant 1.5 h | None | 5 | 1 | 1 | 6 | Cost |
| Time constant 6 h | None | 5 | 1 | 1 | 6 | Cost |
| Threshold spread 0.8 | None | 5 | 1 | 1 | 6 | Cost |
| Threshold spread 1.6 | None | None | 1 | 1 | 6 | Cost |
| Plume spread 0.2 | None | None | 1 | 1 | 3 | Cost |
| Plume spread 0.45 | None | None | 1 | 2 | None | Cost |

None means no count from one to six is feasible,
and Cost means every nonzero count violates the collateral constraint.

The results divide cleanly into two kinds.
**Structural results** hold in every case.
The shared office is infeasible,
the elevator is a standing cost,
and the interview needs one or two sprays.
Dinner needs one or two in every case but one,
and in that case,
a threshold three times more sensitive than planned,
even a single spray reaches the next table too often.
**Calibrated results** move with the threshold and the plume spread,
and the open-plan and outdoor answers belong to this kind.
A reader should rely on the first kind
and treat the second as an illustration of how the reasoning runs.
The emission time constant barely matters at the level of the smallest feasible dose,
which is reassuring given how crude the lumped model is.

### The interview, where the sign of the objective is unknown

S3 was adjudicated as though detection by the interviewer were desirable,
and the evidence does not establish that it is.
[Baron's 1983 study][research_baron_1983_sweet_smell]
of applicants wearing a pleasant scent
is summarised in a later review by
[Sorokowska, Sorokowski and Havlíček][research_sorokowska_2016_body_odor_review]
as finding scented candidates rated especially favourably by female interviewers
but not necessarily by male ones.
In a follow-up, [Baron][research_baron_1986_too_much]
found that male interviewers marked down applicants
who combined scent with other positive cues such as smiling and eye contact,
which he described as too much of a good thing.

The interview is therefore the one scenario in which detection may be a cost,
and its plan has a branch.
**If the interviewer is known and the evidence favours detection,
the plan is one spray.
If the interviewer is unknown, the plan is zero.**
The difference between the two is a single spray,
and the downside of the wrong branch is larger than the upside of the right one,
because an interview is a single encounter with no sequel.

A second finding bears on every scenario.
In a double-blind study by
[Roberts and colleagues][research_roberts_2009_deodorant],
men given a fragranced antimicrobial deodorant rather than an identical inactive one
reported higher self-confidence,
and women watching video clips of them,
who could not smell them,
rated them more attractive.
Photographs showed no difference,
which locates the effect in behaviour.
**Part of the effect of a fragrance on others is mediated by the wearer
and requires no receiver to detect anything.**
That part of the effect is fully delivered by the smallest dose the wearer knows has been applied,
which is one more reason the adjudicated doses are small.

## Placement

### The conventional points

The conventional points can be stated with confidence only at the level of agreement among sources,
because most of the grooming and fashion press that publishes them
could not be retrieved in full for this article,
and the sources that could be retrieved do not agree in detail.
The [Wikipedia article on perfume][ref_perfume]
describes application to pulse points
behind the ears, at the nape of the neck, under the armpits and on the insides of the wrists.
[Chanel's guidance][guidance_chanel_apply]
names pulse points such as the wrist and neck
and offers clothing as an alternative that preserves the fragrance as composed.
The commonly repeated men's plans place
three sprays on the two sides of the neck and the chest,
with a fourth on the nape or the wrists.
The commonly repeated women's plans place
sprays on the wrists, the neck, behind the ears and on the décolletage,
with the hair, the inner elbows and the backs of the knees as further options.
Spray distances given in retail guidance range from about 10 cm to 20 cm.

The stated rationale is almost always warmth at the pulse points.
**No source located for this article measured a pulse-specific mechanism**,
and the temperature section above shows that the extremities,
including the wrist,
are cooler than the trunk rather than warmer.
The pulse is the wrong mechanism for the wrist
and an unnecessary one for the neck,
whose advantage comes from proximity to the receiver's nose.

The companion rule that the wrists must not be rubbed together
because rubbing crushes the fragrance molecules
has no physical basis in the form stated,
since rubbing does not break covalent bonds.
The only test located was informal.
[Victoria Frolova][commentary_bois_de_jasmin_rubbing] rubbed a fragrance on her wrists until the skin was pink
and found after fifteen minutes that nobody could tell any dramatic difference.
Rubbing warms and spreads the application,
which by the temperature model should shorten the top notes slightly,
and the effect is plausible, small and unmeasured.

### What makes a point good

Five properties decide a point's value,
and each corresponds to a term in the models above.

1. **Temperature** sets the emission rate and its exhaustion,
   through the Clausius and Clapeyron factor.
2. **Coverage** by clothing slows emission,
   occludes some of the dose into the skin,
   and delays the start of projection.
3. **Geometry** sets the distance to the receiver's nose
   and whether the thermal plume carries the emission toward it.
4. **Attrition** removes dose by contact,
   most of all by handwashing.
5. **Self-exposure** sets the distance to the wearer's own nose,
   and with it the speed of the adaptation that drives the reapplication spiral.

Attrition deserves an equation, because it is the property on which the wrist fails.
Suppose each handwash removes a fraction $w$ of the dose remaining on the wrist,
and the wearer washes every $\Delta t$ hours.
Averaged over the day, washing adds a loss rate to the emission rate,
and the effective time constant $\tau_{\mathrm{eff}}$ is as follows.

$$
\frac{1}{\tau_{\mathrm{eff}}} = \frac{1}{\tau} + \frac{-\ln(1 - w)}{\Delta t}
$$

With the assumed values $w = 0.5$ and $\Delta t = 2$ h,
the washing term is $0.693 / 2 = 0.35$ per hour
against an emission term of 0.33 per hour,
so $\tau_{\mathrm{eff}} = 1 / 0.68 = 1.5$ h.
**Handwashing halves the working life of a wrist application**
and sends the removed half down a drain rather than toward a receiver.
The wrist is also the point most likely to transfer fragrance to food, paper and other people's hands,
and the point most often raised to the wearer's own nose,
which is the self-exposure pathway at its most direct.

### The points assessed

The following table assesses each conventional point against the five properties.
Entries are relative and qualitative except where an equation above supports them.

| Point | Temperature | Coverage | Geometry | Attrition | Self-exposure | Assessment |
|---|---|---|---|---|---|---|
| Sides of the neck | Trunk-warm | Exposed | Face height, in the plume | Low | High, about 0.2 m | Strong projection, fast self-adaptation, sun-exposed |
| Base of the throat or sternum | Trunk-warm | Usually covered | Below the face, in the plume | Low | Moderate | Best single point |
| Nape of the neck | Warm | Exposed or under hair | Behind the head | Low | Low | Best second point, projects behind the wearer |
| Behind the ears | Warm | Exposed or under hair | Face height | Low | High | Equivalent to the neck, with a smaller target |
| Wrists | Cooler | Exposed | Mobile | High | Very high when raised | Weakest skin point |
| Inner elbows | Intermediate | Often covered | Mobile | Low | Low | Adequate, slow |
| Backs of the knees | Intermediate | Exposed in a skirt | Low, in the plume | Low | Very low | Adequate for a long, low-intensity trail |
| Underarms | Warm | Covered | In the plume | Interacts with deodorant | Moderate | Excluded for irritation and sensitisation |
| Hair | Cool | Exposed | Face height, moves | Low | Moderate | Long life, use a hair mist |
| Clothing | Ambient | Not applicable | Wherever the garment is | Removable | Varies | Longest life, staining risk, removable |

**The base of the throat or the sternum is the best single point.**
It is on the warm trunk,
it sits in the thermal plume below the face so that its emission rises toward any receiver at face height,
it suffers little attrition,
and if a collar covers it, the emission is slowed and the self-exposure reduced.
**The nape is the best second point**,
because it projects behind the wearer,
which is where the trail described as sillage is formed,
and it is the warm point furthest from the wearer's own nose.
**The wrist is the weakest skin point**,
cooler than the trunk,
washed several times a day,
and raised to the wearer's own nose by the gesture used to check whether the fragrance is still there,
which is the gesture that adapts the wearer fastest.

### The adjudicated plans

The original question asked for the conventional points
under the three-push and four-push scenarios,
and the answer is set out below beside the adjudicated alternative.
The conventional columns are a composite of commonly repeated advice
rather than a quotation of any one source.
The adjudicated plans are the same for any wearer,
with variants for long hair and for an open neckline.

| Plan | Conventional, men | Conventional, women | Adjudicated |
|---|---|---|---|
| One push | Chest | One wrist or the neck | Sternum or base of the throat |
| Two pushes | Both sides of the neck | Both wrists | Sternum and nape |
| Three pushes | Both sides of the neck and the chest | Both wrists and the neck | Sternum, nape and one garment point such as the inside of a collar or a scarf |
| Four pushes | Both sides of the neck, the chest, and the nape or wrists | Wrists, neck and behind the ears, or the hair | Three in the morning at sternum, nape and garment, and one at midday at the sternum, by spray or rollerball |

Three further rules complete the plans.

- **The scenario sets the count and the table sets the points.**
  For dinner and the interview the adjudicated count is one,
  and the one-push plan applies regardless of habit.
  For the full working day in an open-plan office it is four, split as shown.
  In a small shared office or under a fragrance-free policy it is zero.
- **Long hair substitutes for the nape.**
  A hair mist or a single spray from 20 cm onto the lengths,
  not the scalp,
  places dose on a cool, mobile, long-lived point that projects behind and around the wearer.
- **An open neckline moves the sternum point onto exposed skin.**
  It then projects sooner and exhausts faster,
  and in daylight with a citrus-heavy product it is the point that photosensitivity concerns.

### Whether the conventional points survive

The conventional neck points survive,
for proximity rather than pulse.
The conventional chest point survives and is promoted to the first point.
The conventional nape point survives and is promoted to the second.
The conventional wrist points do not survive as skin points,
on temperature, attrition and self-exposure together.
The hair and garment points survive and are underused,
since they are the only points with no skin exposure,
and the garment is the only one that can be taken off.

## Whether the Wearer's Sex Changes the Answer

H3 asks whether the conventional difference between men's and women's points
is a property of the wearer or of what the wearer is wearing.
Setting the two conventional lists side by side
and asking what each difference depends on gives the answer directly.

| Conventional difference | What it depends on |
|---|---|
| Décolletage for women, chest for men | Neckline. It is the same anatomical point, covered or not |
| Hair for women | Hair length |
| Backs of the knees for women | Skirt length, which exposes or covers the point |
| Wrists emphasised for women | No physical difference identified |
| Beard for some men | Facial hair, a hair point at the worst possible self-exposure distance |

Every difference with a physical basis resolves to clothing or hair.
No source located for this article measured a difference in fragrance emission or longevity
attributable to the wearer's sex once those are held fixed,
and claims about skin oiliness and longevity in the retail literature
were not found in the peer-reviewed literature at all.
**H3 is supported.**

The receiver's sex is a different matter,
though a small one.
In a meta-analysis of olfactory testing,
[Sorokowski and colleagues][research_sorokowski_2019_sex_differences]
found women outperforming men in every domain,
with effect sizes between 0.08 and 0.30 that the authors describe as weak,
and a threshold effect of 0.16.
[Doty and Cameron's review][research_doty_cameron_2009_sex_differences]
reaches a consistent conclusion.
Read as a shift in the log threshold of 0.16 standard deviations,
and taking this article's threshold spread of 1.2 natural log units as the standard deviation,
an effect of that size moves the median threshold by a factor of about $e^{0.16 \times 1.2} = 1.2$.
That is a fifth of a spray per spray,
below the resolution of the pump,
and it does not change any adjudicated count.
The conversion assumes that the test's threshold units and this article's share a spread,
which is an inference and not a measurement.

## Other Application Platforms

The spray count is a property of one platform.
The other platforms in common use either have no natural unit of dose
or carry so little aromatic material per unit that the spray-count framing breaks.
Each is assessed here by what it changes in the dose and transport models.

| Platform | Carrier | Dose control | What it changes |
|---|---|---|---|
| Spray atomizer | Ethanol | Fixed volume per actuation | The reference case |
| Rollerball | Ethanol or oil | Stroke length, poorly controlled | Precise placement, no overspray, $\eta$ near one |
| Splash bottle | Ethanol | None | Large and variable dose, usually of dilute product |
| Solid perfume | Wax, oil or fat | Fingertip load | Low emission rate, intimate range only |
| Perfume oil or attar | Oil, no ethanol | Dab or stroke | Slow emission, long life, short radius |
| Body mist | Ethanol and water | Fixed volume, low concentration | Many sprays for one spray-equivalent |
| Hair mist | Less ethanol, more water | Fixed volume | Formulated for the hair point |
| Aftershave | Ethanol, astringents | Palm load | Low concentration on freshly shaved skin |

**The rollerball and the solid are the intimate-range platforms.**
Their deposition efficiency is near one, since nothing is lost to the air in the act of application,
and their dose is small and concentrated at a single point.
In the adjudication's terms they reach S4 without the collateral that a spray brings,
and they are the correct sequel platform for S2,
since a midday stroke at one point delivers roughly the single spray the sequel requires
without a plume in the office.
Many rollerballs are an alcohol-based eau de parfum in different packaging,
so the platform changes the deposition and not necessarily the product.

**The [solid perfume][ref_solid_perfume] and the [attar][ref_attar] trade radius for longevity.**
An oil or wax carrier lowers the vapour pressure of the aromatic material dissolved in it,
which in the emission model raises $\tau$.
Because the detection radius scales as $\tau^{-1/2}$ at application,
and its half-life scales as $\tau$,
a carrier that triples the time constant
shrinks the starting radius by $\sqrt{3}$ and triples the time over which it decays.
Attar is distilled into an oil base,
traditionally sandalwood oil and now often liquid paraffin,
with Kannauj in India as its historic centre.

**Body mists invert the spray-count question.**
At about two percent aromatic content,
a body mist delivers 0.13 spray-equivalents per actuation,
so the conventional three-push of a body mist is 0.4 spray-equivalents,
below the one-spray dose the adjudication found adequate for dinner.
A body mist used to the same end state takes about eight sprays,
and the instruction on such products to spray liberally
is consistent with the dose model rather than a marketing excess.

**Aftershave** is applied to freshly shaved skin,
which the safety section excludes as a point for fine fragrance.
[Aftershave][ref_aftershave] formulations include astringents and antiseptics for that reason
and are low in aromatic content,
so the conventional practice of following aftershave with a separate fragrance
is a two-platform plan in which the aftershave contributes little to the end state.

**Layering**, the use of scented washes and lotions from the same line as the fragrance,
adds dose at many points at once,
and the claim that it extends longevity rests on retail guidance rather than measurement.
The effect it certainly has is to add dose that the spray count does not record,
so a layered plan should be adjudicated as a higher spray-equivalent.

## Other Application Targets

### Animals

**The adjudicated course of action for applying human fragrance to an animal is zero.**
The reasons are physiological and they are not close.
Domestic cats lack a functional form of the liver enzyme UGT1A6,
as [Court and Greenblatt][research_court_greenblatt_2000_cat_ugt1a6] established,
which leaves them poorly able to glucuronidate phenolic compounds
of the kind present in many essential oils.
Veterinary guidance from [VCA Animal Hospitals][guidance_vca_cats_essential_oils]
lists essential oils toxic to cats on that basis,
and the [ASPCA][guidance_aspca_essential_oils],
the American Society for the Prevention of Cruelty to Animals,
advises against essential-oil diffusers in homes with birds,
whose respiratory systems are unusually sensitive to airborne compounds.
Dogs present a receiver problem rather than a toxicity problem in the first instance.
The usual claim that a dog's nose is uniformly far more sensitive than a human's
is weaker than its popularity suggests,
since [McGann][research_mcgann_2017_human_olfaction]
reviews evidence that humans outperform dogs for some odorants,
but a dog's nose is in any case the receiver nearest the application point,
and the dog did not consent.

Where an animal is to be scented at all,
veterinary guidance quoted by [PetMD][guidance_petmd_dog_perfume]
and by the [American Kennel Club][guidance_akc_dog_perfume]
is to use a product made for the species,
to keep it away from the face, eyes, ears and genitals,
and not to mask an odour that may have a medical cause.
In the terms of this article,
that is a different product,
a single point on the coat away from the receiver's own nose,
and an investigation of the reason for the application before it is made.

### Bags, garments and textiles

A bag or garment is a target without skin chemistry, skin absorption or body heat.
In the emission model its time constant is longer than skin's,
since the fabric surface is cooler,
and in the transport model it lacks the thermal plume that carries scent upward from the body.
It therefore holds fragrance longer and projects it less.

The conventional prohibitions are about materials rather than effect.
Luxury leather houses advise against direct contact between perfume and their leather goods,
and silk and pale fabrics stain.
The standard workaround is to scent an intermediate,
such as a cotton pad, a scarf or a sachet placed inside the bag,
and this is conventional practice rather than a sourced recommendation.
A scarf is the most useful of these,
because it is a garment point that can be removed,
which makes it the only application point with an off switch.

Paper is the oldest textile-adjacent target in the record,
from the perfumed valentines noted in the history section
to the scented letter,
and it is adjudicated as a one-receiver, intimate-range application with no collateral
and no further analysis.

### Rooms

A room is the one target for which area denial is the stated end state.
The far-field equation of the transport section applies directly,
with the source now a product designed to emit continuously.
[Room fragrance platforms][ref_air_freshener] include sprays,
reed diffusers that evaporate from soaked reeds,
electrically heated plug-in devices,
candles and incense,
and the burning of [bakhoor][ref_bakhoor],
scented wood chips or blocks used in the Arabian Peninsula to perfume rooms, clothing and hair.

The steady state of a continuous room source $E$ in micrograms per hour,
in a room of volume $V$ ventilated at $\lambda$ per hour,
is the emission divided by the ventilation flow.

$$
C_{\mathrm{room}}^{\infty} = \frac{E}{\lambda V}
$$

A reed diffuser emitting 20 mg per hour of aromatic material
into a 40 m³ living room at half an air change per hour
holds $20{,}000 / (0.5 \times 40) = 1{,}000$ µg/m³,
thirty-three times the median detection threshold used in this article
and above its planning value for too strong.
The emission figure is an assumption for illustration,
and the conclusion it supports is relative.
**The steady state is inversely proportional to ventilation,
so a room fragrance product tuned for a draughty room is overpowering in a sealed one**,
and closing a window doubles the concentration as surely as doubling the product does.

Two cautions specific to rooms carry over from the safety section.
Room products emit continuously for hours or weeks,
so their contribution to the indoor terpene and ozone chemistry
described by [Nazaroff and Weschler][research_nazaroff_weschler_2004]
is much larger than that of a personal application.
And every occupant of a room is a receiver,
including the animals discussed above,
for whom the restraint on diffusers is the operative one.

A car is a room with a volume of about 3 m³.
By the far-field equation, the wearer's own morning application
reaches room-regime concentrations in a closed car within minutes,
and any room product added to it is applied to the smallest volume in this article.

## Safety

The restraints stated at the outset are given content here.
Each is a limit that no end state justifies exceeding.

### Contact allergy

Fragrance ingredients are among the commonest causes of allergic contact dermatitis.
The [European Commission's Scientific Committee on Consumer Safety][research_sccs_2012_fragrance_allergens],
or SCCS,
concluded in 2012 that one to three percent of the general European population
is allergic to fragrance ingredients,
and it classified 82 substances as established contact allergens in humans,
54 single chemicals and 28 natural extracts.
The [EDEN Fragrance Study][research_diepgen_2015_eden],
which patch tested 3,119 people drawn from the general population of five European countries,
found reactions to fragrance mix I in 2.6 percent
and to fragrance mix II in 1.9 percent,
and gave a conservative estimate of fragrance allergy of 1.9 percent.

Regulation follows the same evidence.
[Commission Regulation 2023/1545 of the European Union][primary_eu_2023_1545]
added 56 fragrance allergens to the 24 already subject to individual labelling in cosmetic products,
with labelling required above 0.001 percent in leave-on products
and 0.01 percent in rinse-off products.
The industry's own instrument is the set of
[standards maintained by the International Fragrance Association][primary_ifra_52nd_amendment],
or IFRA,
which prohibit, restrict or specify the purity of individual materials.

The operational consequence for this article is narrow and firm.
**Sensitisation is cumulative and largely irreversible,
so the application plan minimises the dose placed on skin
whenever skin is not required by the end state.**
A wearer who has reacted to a fragrance stops wearing it on skin,
and the clothing and hair points in the placement section
are the fallback rather than a workaround.
Broken, irritated or freshly shaved skin is excluded as an application point,
because a compromised barrier increases both irritation and the likelihood of sensitisation.

### Photosensitivity

Bergamot oil contains furocoumarins, principally bergapten,
which under ultraviolet light cause a phototoxic reaction and lasting pigmentation
known as [berloque dermatitis][ref_berloque_dermatitis].
IFRA restricts furocoumarin content in leave-on products for this reason,
as its [furocoumarin update][primary_ifra_furocoumarins] describes,
so a compliant modern product presents a low risk.
The residual guidance is that the sides of the neck and the décolletage are sun-exposed points,
and a wearer using an older, unregulated or home-blended product
containing citrus oils should move the application under clothing
for an outdoor scenario in daylight.

### Eyes, mucous membranes and ingestion

Fine fragrance is mostly ethanol.
The [National Capital Poison Center][guidance_poison_control_perfume]
gives typical alcohol contents of about ninety percent for eau de parfum
and sixty percent for eau de cologne,
and warns that in a child ingested alcohol can lower blood sugar to dangerous levels.
Bottles are therefore stored as a household chemical is stored,
out of reach of children,
and the spray is never directed toward the face, the eyes or the mouth,
including the wearer's own.
Spraying from 10 to 15 cm at the neck keeps the plume clear of the eyes
only if the head is turned away,
and the placement section assumes that it is.

### Flammability

Ethanol has a flash point of about 13 °C
according to the [NIOSH Pocket Guide][guidance_niosh_ethanol],
NIOSH being the United States National Institute for Occupational Safety and Health,
and its vapour is flammable in air between 3.3 and 19 percent by volume.
A freshly sprayed point carries flammable vapour for the seconds before the ethanol evaporates.
Fragrance is not applied near an open flame, a lit cigarette or a gas hob,
and a pressurised aerosol can is additionally kept away from heat.

### Indoor air and receivers who did not consent

The adjudication's collateral constraint is not a matter of taste alone.
A survey of 1,136 adults in the United States by
[Steinemann][research_steinemann_2016]
found that 34.7 percent reported health problems,
including respiratory, migraine and skin effects,
when exposed to fragranced consumer products.
The figure rests on self-report from an online panel
and measures reported sensitivity rather than diagnosed effect,
so it should not be read as a prevalence of harm.
It is nonetheless large enough that an unintended receiver
must be presumed sensitive until shown otherwise.

Workplaces have responded with written policy.
The United States Centers for Disease Control and Prevention,
or CDC,
adopted an indoor environmental quality policy in 2009
asking employees to be as fragrance-free as possible,
though the text survives only as
[quoted by a secondary source][commentary_cdc_policy_secondary]
and no current copy on the agency's own site was located.
In the United States the [Job Accommodation Network][guidance_jan_fragrance]
lists fragrance sensitivity among conditions for which employers make accommodations
such as relocation or reduced exposure.
**A wearer in a workplace with a fragrance-free policy adopts the zero-spray course of action**,
which the adjudication already identified as the only one that satisfies S1 and S6.

Fragrance also takes part in indoor chemistry.
Terpenes common in fragrances react with ozone indoors
to form formaldehyde and secondary organic aerosol,
as reviewed by [Nazaroff and Weschler][research_nazaroff_weschler_2004]
and measured by [Singer and colleagues][research_singer_2006_secondary_pollutants].
The quantities from a personal application are small next to those from room fragrance products,
which is why the room is treated with more caution below.

### Materials

Ethanol and fragrance oils stain silk and pale fabrics and can mark leather.
Pearls are damaged by acids and by cosmetics, hairspray and perfume,
as the [Gemological Institute of America][guidance_gia_pearl_care] notes,
and the jeweller's rule that pearls go on last and come off first
follows from that.
Fragrance is applied and allowed to dry before jewellery is put on.

### Transport

Air travel imposes a sustainment constraint of its own.
In the United States the
[Transportation Security Administration's liquids rule][guidance_tsa_311]
limits carry-on liquids to containers of 100 mL or 3.4 ounces in a single quart-sized bag,
so the sequel platform for a travel day is a small atomizer or a solid.

## Adjacent Offensive Applications

The same delivery physics serves purposes this article does not adjudicate,
and the boundary is drawn here so that its location is explicit.

**Pepper spray** delivers an inflammatory agent, oleoresin capsicum,
by the same pressurised aerosol mechanism used by some fragrance and deodorant products.
Its strength is best described by the content of capsaicin and related capsaicinoids
rather than by the percentage of oleoresin capsicum or a Scoville rating,
because, as [Reilly, Crouch and Yost][research_reilly_2001_pepper_spray] found,
commercial products are not standardised for capsaicinoid content
even when labelled by heat rating.
The [Wikipedia article on pepper spray][ref_pepper_spray] summarises the same point.
**Bear spray** is a related product registered in the United States
by the Environmental Protection Agency, or EPA, as a pesticide,
and [interagency guidance][guidance_igbc_bear_spray] advises carrying only EPA-registered products.
In the United Kingdom such sprays fall within
[section 5 of the Firearms Act 1968][primary_uk_firearms_act_s5],
in its paragraph on noxious substances,
which prohibits weapons designed for the discharge of any noxious liquid, gas or other thing,
though the statute does not name pepper spray as such.
**Malodorants**, odours selected to be offensive to nearly everyone,
were the subject of research for the United States Department of Defense
reported in [2002][commentary_acs_2002_malodorant]
and of later [military small-business research topics][primary_navy_sbir_malodorant].

These products share with fragrance an aerosol platform, a plume and a receiver.
They differ in that the receiver's consent is absent by design,
which places them outside every restraint this article operates under,
and in that the end state is incapacitation or dispersal rather than detection.
Collateral and overkill have their ordinary meanings in that literature as well.
**A full analysis of offensive applications is out of scope**,
and nothing in the adjudication above transfers to them.
Two points are stated so that the boundary is not crossed by accident.
A fragrance is never sprayed at another person,
which falls under the restraint on consent.
And a fragrance applied at the overkill end of the adjudicated range
is not an offensive application,
merely a poorly planned one.

## Findings

### The hypothesis adjudicated

**H1, dose, is partially supported.**
Its second clause holds without exception.
The fourth spray adds less than the third,
by $\sqrt{4/3}$ in detection radius and by about fifteen percent in perceived intensity at a fixed distance,
and this follows from the square-root scaling of the plume and the compressive power law of perception,
neither of which depends on the calibrated threshold.
Its first clause, that three or four sprays is the smallest adequate dose,
is rejected in four of the six scenarios
and supported only in modified form in the remaining two.
For dinner and the interview the adequate dose is one.
For the shared office and the elevator no positive dose is adequate.
For the open-plan office, four sprays are adequate only when split into a morning application and a midday sequel.
Outdoors, four sprays are adequate only for an extrait,
and an eau de parfum needs six.

**H2, placement, is partially supported.**
The conventional points are broadly sound and the conventional reason for them is not.
No pulse-specific mechanism was found.
Warmth operates, through vapour pressure,
and is worth about one spray in four.
The dominant mechanisms are geometric,
namely distance to the receiver,
the thermal plume that carries torso emissions upward,
and distance to the wearer's own nose.
The neck, chest and nape survive on geometry,
and the wrist fails on temperature, attrition and self-exposure together.

**H3, the wearer, is supported.**
Every conventional difference between men's and women's points with a physical basis
resolves to clothing or hair,
and the receiver's sex has an effect smaller than the pump can resolve.

**The overall hypothesis is partially supported.**

### Doctrine

The findings reduce to a short set of rules,
each traceable to a section above.

1. **State the end state before choosing a count.**
   A spray count without a receiver, a distance, a room and a duration is not a plan.
2. **Convert to spray-equivalents.**
   Four sprays of eau de toilette and four of extrait differ by a factor of two and a half.
3. **Check the room before the wearer.**
   If the room's volume times its air change rate is small,
   the room becomes the source and no count separates intended from unintended receivers.
4. **Default to one spray at the sternum.**
   It meets the close-range end states,
   which are where most fragrance is worn.
5. **Split rather than escalate.**
   For a long day, a morning application and a midday sequel
   outperform a single larger application with fewer sprays.
6. **Never reapply on the wearer's own judgement.**
   Schedule the sequel in advance or ask a red cell.
7. **Prefer the trunk, the nape, the hair and the garment to the wrists.**
8. **When the sign of the objective is unknown, apply zero.**
9. **Do not apply human fragrance to animals,
   and treat every room product as an application to every occupant of the room.**

## Epistemic State

**Measured and sourced.**
The physical constants and product facts are sourced.
These are the pump volumes from a manufacturer's specification,
the enthalpy of vaporisation of linalool,
the flash point of ethanol,
the concentration ranges of the product classes,
the ventilation rates from the Environmental Protection Agency,
the thermal plume velocity,
the odour power-law exponents,
the age, sex and specific anosmia findings,
the allergy prevalence and the regulatory limits.
Each is cited to a source that was read in full or in abstract.
The Craven and Settles plume velocity,
the dates of the DeVilbiss perfume atomizer,
the Chanel application advice,
the Metropolitan Museum and VCA pages,
and several retail claims
were confirmed only from search results and not from the pages themselves,
and they are worded accordingly.

**Modelled.**
Every number in the adjudication tables is the output of a deterministic model
whose equations are all displayed in the article
and whose parameters are all listed in the planning assumptions.
The model is deliberately simple.
It collapses a fragrance into one pool with one time constant,
treats the plume as a Gaussian with linear spreading in steady air,
treats each room as perfectly mixed,
and represents receivers by a log-normal threshold.
**Each of these is wrong in detail**,
and the sensitivity analysis is the article's account of how much that matters.
The structural results,
namely the square-root scaling,
the dose-independence of the radius half-life,
the infeasibility of the small shared office,
the elevator's standing cost,
and the advantage of the split sequel over escalation,
follow from the form of the equations and survive every variation tested.
The calibrated results,
namely the specific counts for the open-plan office and the outdoor event,
do not survive every variation and are illustrations.

**Assumed.**
The deposition efficiency of 0.70,
the time constant of three hours,
the adaptation floor and time constant,
the handwashing removal fraction and interval,
the overkill threshold at thirty times the detection threshold,
and the reed diffuser emission rate
are planning values with no direct source.
The adaptation values in particular are not supplied by the adaptation literature cited,
which describes the effect without the time constants used here.

**Not found.**
No peer-reviewed study was found of a pulse-specific mechanism,
of skin hydration or oiliness as a determinant of fragrance longevity,
of the effect of rubbing an application,
of optimal spray distance,
or of fragrance retention on worn clothing.
The conventional advice on all of these rests on retail and editorial sources,
and the article reports it as convention rather than as evidence.
The conventional plans in the placement tables are a composite of commonly repeated advice
rather than a quotation of any single source,
because most of the editorial sources could not be retrieved in full.

**One revision after adjudication.**
The first run of the adjudication required detection with probability 0.8,
averaged over the scenario window,
and found almost every scenario infeasible,
because an exponentially decaying source cannot hold a high detection probability for eight hours
without overkill at the start.
The threshold was lowered to 0.5, more likely than not,
before any spray count result was examined,
and this is the exception noted in the statement of the hypothesis.
The infeasibility at 0.8 is itself a finding,
and it is the reason the sequel exists.

**Vantage.**
The article carries an editorial date of 5 October 2025 and was written a year later.
A small number of sources postdate the editorial date,
most visibly the International Fragrance Association's letter of August 2026 on its 52nd amendment,
and they are cited because they are the current statement of a standard
rather than because the analysis depends on them.

**Where to disagree.**
A reader with measured emission curves for a real fragrance on real skin
should replace the lumped time constant and rerun the tables.
A reader with a measured detection threshold for a blend
should replace the calibrated value,
which would move the open-plan and outdoor counts and nothing structural.
A reader who believes the collateral constraint is too strict
is disputing the end state rather than the analysis,
and the analysis supports that dispute being had explicitly.

## Out of Scope

- **Fragrance composition and selection.**
  Which fragrance to wear is a separate question.
  The finding of [Lenochová and colleagues][research_lenochova_2012_perfume_blend]
  that people choose perfumes that blend well with their own body odour
  suggests that the wearer's own choice carries information this article does not model.
- **Pheromone claims.**
  Products marketed as containing human pheromones are outside the analysis,
  since [Wyatt's review][research_wyatt_2015_pheromones]
  found no robust bioassay-led evidence that any proposed human pheromone is one.
- **Cultural practice.**
  Traditions of fragrance use that differ from the Western spray convention,
  including attar and bakhoor, are mentioned and not analysed.
- **Health effects beyond irritation and sensitisation.**
  Questions about endocrine activity of fragrance constituents are outside the evidence reviewed.
- **Scent marketing.**
  The deliberate scenting of shops and hotels is a room application by a commercial actor
  and is not assessed.
- **Offensive applications.**
  Pepper spray, bear spray and malodorants are bounded in their own section
  and are not analysed.
- **Storage and degradation.**
  Fragrance degrades with heat and light,
  and the effect on the emission model of a degraded product is not modelled.

## Conclusion

The question asked for the conventional application points
under the three-push and four-push scenarios,
and the conventional answer exists.
For men it is both sides of the neck and the chest,
with the nape or the wrists as the fourth.
For women it is the wrists, the neck, behind the ears and the décolletage,
with the hair as an option.

The adjudicated answer differs from it in three ways.
The points move toward the sternum, the nape, the hair and the garment,
and away from the wrists,
because the operative mechanisms are geometry and attrition rather than the pulse.
The counts fall,
because the encounters in which fragrance is mostly worn are close,
indoor and short,
and one spray of eau de parfum meets them.
And the four-push survives only as a plan executed in two phases,
three sprays in the morning and one at midday,
which outperforms a single application of five.

**The hypothesis that the conventional doctrines are sound is partially supported.**
They name defensible points for the wrong reason
and prescribe a dose calibrated to no stated end state.
The single most consequential finding is not about points or counts at all.
It is that the wearer,
who decides when the fragrance has faded,
is the one receiver whose perception has been degraded by the application itself,
and that every plan which leaves reapplication to the wearer's judgement
ends in overapplication.
The remedy is a schedule or a second opinion,
and the second opinion is free.

## References

- [Commentary, American Chemical Society 2002, The Smell of Fear, Researchers Seek Universal Malodorant][commentary_acs_2002_malodorant]
- [Commentary, Frolova 2013, Do Not Crush the Molecules, Testing a Perfume Myth][commentary_bois_de_jasmin_rubbing]
- [Commentary, Invisible Disabilities Association, CDC Indoor Environmental Quality Policy on Fragrance][commentary_cdc_policy_secondary]
- [Data, EPA Exposure Factors Handbook, Chapter 19, Building Characteristics][data_epa_efh_ch19]
- [Data, NIST Chemistry WebBook, Linalool Phase Change Data][data_nist_linalool]
- [Guidance, American Kennel Club, Is Dog Perfume Safe][guidance_akc_dog_perfume]
- [Guidance, ASPCA 2018, Latest Home Trend Harmful to Your Pets][guidance_aspca_essential_oils]
- [Guidance, Chanel, How Do I Apply My Fragrance][guidance_chanel_apply]
- [Guidance, Gemological Institute of America, Pearl Care and Cleaning][guidance_gia_pearl_care]
- [Guidance, Interagency Grizzly Bear Committee, Bear Spray][guidance_igbc_bear_spray]
- [Guidance, Job Accommodation Network, Fragrance Sensitivity][guidance_jan_fragrance]
- [Guidance, National Capital Poison Center, Perfume][guidance_poison_control_perfume]
- [Guidance, NIOSH Pocket Guide to Chemical Hazards, Ethyl Alcohol][guidance_niosh_ethanol]
- [Guidance, PetMD, Should Dogs Wear Perfume][guidance_petmd_dog_perfume]
- [Guidance, Transportation Security Administration, Liquids, Aerosols and Gels Rule][guidance_tsa_311]
- [Guidance, VCA Animal Hospitals, Essential Oil and Liquid Potpourri Poisoning in Cats][guidance_vca_cats_essential_oils]
- [History, Bodleian Libraries 2013, Rimmel's Scented World][history_bodleian_rimmel]
- [History, German Patent and Trade Mark Office, Farina][history_farina_dpma]
- [History, Metropolitan Museum of Art, Egyptian Ointment Jar][history_met_ointment_jar]
- [History, University of Toledo Libraries, DeVilbiss Atomizers][history_utoledo_devilbiss]
- [History, Victoria and Albert Museum, Rimmel Perfumed Sachet Valentine][history_vam_rimmel_valentine]
- [Primary, Aptar, VP4 Fragrance Pump][primary_aptar_vp4]
- [Primary, Commission Regulation 2023/1545 of the European Union on Labelling of Fragrance Allergens][primary_eu_2023_1545]
- [Primary, Firearms Act 1968, Section 5][primary_uk_firearms_act_s5]
- [Primary, IFRA 2025, Furocoumarins Update][primary_ifra_furocoumarins]
- [Primary, IFRA 2026, End of Consultation Letter for the 52nd Amendment to the IFRA Standards][primary_ifra_52nd_amendment]
- [Primary, United States Navy Small Business Innovation Research Topic N113-174][primary_navy_sbir_malodorant]
- [Reference, Aftershave][ref_aftershave]
- [Reference, Air Freshener][ref_air_freshener]
- [Reference, Atmospheric Dispersion Modeling][ref_atmospheric_dispersion]
- [Reference, Attar][ref_attar]
- [Reference, Bakhoor][ref_bakhoor]
- [Reference, Berloque Dermatitis][ref_berloque_dermatitis]
- [Reference, Clausius and Clapeyron Relation][ref_clausius_clapeyron]
- [Reference, Kyphi][ref_kyphi]
- [Reference, Note in Perfumery][ref_note_perfumery]
- [Reference, Pepper Spray][ref_pepper_spray]
- [Reference, Perfume][ref_perfume]
- [Reference, Proxemics][ref_proxemics]
- [Reference, Sillage][ref_sillage]
- [Reference, Solid Perfume][ref_solid_perfume]
- [Reference, Stevens's Power Law][ref_stevens_power_law]
- [Reference, Tapputi][ref_tapputi]
- [Research, Baron 1983, Sweet Smell of Success, The Impact of Pleasant Artificial Scents on Evaluations of Job Applicants][research_baron_1983_sweet_smell]
- [Research, Baron 1986, Self-Presentation in Job Interviews, When There Can Be Too Much of a Good Thing][research_baron_1986_too_much]
- [Research, Bronaugh and others 1990, In Vivo Percutaneous Absorption of Fragrance Ingredients in Rhesus Monkeys and Humans][research_bronaugh_1990_absorption]
- [Research, Court and Greenblatt 2000, Molecular Genetic Basis for Deficient Acetaminophen Glucuronidation by Cats, UGT1A6 Is a Pseudogene][research_court_greenblatt_2000_cat_ugt1a6]
- [Research, Craven and Settles 2006, A Computational and Experimental Investigation of the Human Thermal Plume][research_craven_settles_2006_thermal_plume]
- [Research, Dalton 2000, Psychophysical and Behavioral Characteristics of Olfactory Adaptation][research_dalton_2000_adaptation]
- [Research, Diepgen and others 2015, Prevalence of Fragrance Contact Allergy in the General Population of Five European Countries][research_diepgen_2015_eden]
- [Research, Doty and Cameron 2009, Sex Differences and Reproductive Hormone Influences on Human Odor Perception][research_doty_cameron_2009_sex_differences]
- [Research, Doty and others 1984, Smell Identification Ability, Changes with Age][research_doty_1984_age]
- [Research, Elsharif, Banerjee and Buettner 2015, Structure-Odor Relationships of Linalool, Linalyl Acetate and Their Corresponding Oxygenated Derivatives][research_elsharif_2015_linalool]
- [Research, Keller and others 2007, Genetic Variation in a Human Odorant Receptor Alters Odour Perception][research_keller_2007_or7d4]
- [Research, Lenochová and others 2012, Psychology of Fragrance Use][research_lenochova_2012_perfume_blend]
- [Research, Mata, Gomes and Rodrigues 2005, Engineering Perfumes][research_mata_2005_engineering_perfumes]
- [Research, McGann 2017, Poor Human Olfaction Is a 19th-Century Myth][research_mcgann_2017_human_olfaction]
- [Research, Moskowitz and others 1979, Psychophysical Measurement as a Tool for Perfumery and the Cosmetic Industry][research_moskowitz_1979_psychophysical]
- [Research, Nazaroff and Weschler 2004, Cleaning Products and Air Fresheners, Exposure to Primary and Secondary Air Pollutants][research_nazaroff_weschler_2004]
- [Research, Reilly, Crouch and Yost 2001, Quantitative Analysis of Capsaicinoids in Fresh Peppers, Oleoresin Capsicum and Pepper Spray Products][research_reilly_2001_pepper_spray]
- [Research, Roberts and others 2009, Manipulation of Body Odour Alters Men's Self-Confidence and Judgements of Their Visual Attractiveness by Women][research_roberts_2009_deodorant]
- [Research, Rodrigues, Nogueira and Faria 2021, Perfume and Flavor Engineering, A Chemical Engineering Perspective][research_rodrigues_2021_perfume_engineering]
- [Research, Sato-Akuhara and others 2023, Genetic Variation in the Human Olfactory Receptor OR5AN1 Associates with the Perception of Musks][research_sato_akuhara_2023_musk]
- [Research, Savastano and others 2009, Adiposity and Human Regional Body Temperature][research_savastano_2009_regional_temperature]
- [Research, SCCS 2012, Opinion on Fragrance Allergens in Cosmetic Products][research_sccs_2012_fragrance_allergens]
- [Research, Singer and others 2006, Indoor Secondary Pollutants from Cleaning Product and Air Freshener Use in the Presence of Ozone][research_singer_2006_secondary_pollutants]
- [Research, Sorokowska, Sorokowski and Havlíček 2016, Body Odor Based Personality Judgments, The Effect of Fragranced Cosmetics][research_sorokowska_2016_body_odor_review]
- [Research, Sorokowski and others 2019, Sex Differences in Human Olfaction, A Meta-Analysis][research_sorokowski_2019_sex_differences]
- [Research, Steinemann 2016, Fragranced Consumer Products, Exposures and Effects from Emissions][research_steinemann_2016]
- [Research, Stevens 1957, On the Psychophysical Law][research_stevens_1957_psychophysical_law]
- [Research, Stevens and others 2019, From Representation to Reality, Ancient Egyptian Wax Head Cones from Amarna][research_stevens_2019_head_cones]
- [Research, Webb 1992, Temperatures of Skin, Subcutaneous Tissue, Muscle and Core in Resting Men][research_webb_1992_skin_temperature]
- [Research, Wyatt 2015, The Search for Human Pheromones, The Lost Decades][research_wyatt_2015_pheromones]

[commentary_acs_2002_malodorant]: https://www.sciencedaily.com/releases/2002/01/020107074622.htm
[commentary_bois_de_jasmin_rubbing]: https://boisdejasmin.com/2013/11/dont-crush-molecules-perfume-myth-testing-fragrance.html
[commentary_cdc_policy_secondary]: https://invisibledisabilities.org/environmental-illness/cdc-fragrance-free-policy
[data_epa_efh_ch19]: https://www.epa.gov/sites/default/files/2015-09/documents/efh-chapter19.pdf
[data_nist_linalool]: https://webbook.nist.gov/cgi/cbook.cgi?ID=C78706&Mask=4
[guidance_akc_dog_perfume]: https://www.akc.org/expert-advice/health/dog-perfume-safe/
[guidance_aspca_essential_oils]: https://www.aspca.org/news/latest-home-trend-harmful-your-pets-what-you-need-know
[guidance_chanel_apply]: https://services.chanel.cn/en_SG/faq/fragrance-beauty-24/products-25/how-do-i-apply-my-fragrance-112
[guidance_gia_pearl_care]: https://www.gia.edu/pearl-care-cleaning
[guidance_igbc_bear_spray]: https://igbconline.org/bear-spray/
[guidance_jan_fragrance]: https://askjan.org/disabilities/Fragrance-Sensitivity.cfm
[guidance_niosh_ethanol]: https://www.cdc.gov/niosh/npg/npgd0262.html
[guidance_petmd_dog_perfume]: https://www.petmd.com/dog/news/should-dogs-wear-perfume
[guidance_poison_control_perfume]: https://www.poison.org/articles/perfume
[guidance_tsa_311]: https://www.tsa.gov/travel/security-screening/liquids-aerosols-gels-rule
[guidance_vca_cats_essential_oils]: https://vcahospitals.com/know-your-pet/essential-oil-and-liquid-potpourri-poisoning-in-cats
[history_bodleian_rimmel]: https://blogs.bodleian.ox.ac.uk/jjcoll/2013/02/01/rimmels-scented-world/
[history_farina_dpma]: https://www.dpma.de/english/our_office/publications/milestones/brandswithhistory/farina/index.html
[history_met_ointment_jar]: https://www.metmuseum.org/art/collection/search/543971
[history_utoledo_devilbiss]: https://www.utoledo.edu/library/virtualexhibitions/wtx/excase11-ch4.html
[history_vam_rimmel_valentine]: https://collections.vam.ac.uk/item/O1025277/greeting-card-rimmel/
[primary_aptar_vp4]: https://www.aptar.com/products/beauty/vp4/
[primary_eu_2023_1545]: https://eur-lex.europa.eu/eli/reg/2023/1545/oj
[primary_ifra_52nd_amendment]: https://ifrafragrance.org/latest-updates/ifra-news/ifra-publishes-end-of-consultation-letter-for-the-52nd-amendment-to-the-ifra-standards
[primary_ifra_furocoumarins]: https://ifrafragrance.org/latest-updates/furocoumarins-update
[primary_navy_sbir_malodorant]: https://www.navysbir.com/n11_3/N113-174.htm
[primary_uk_firearms_act_s5]: https://www.legislation.gov.uk/ukpga/1968/27/section/5
[ref_aftershave]: https://en.wikipedia.org/wiki/Aftershave
[ref_air_freshener]: https://en.wikipedia.org/wiki/Air_freshener
[ref_atmospheric_dispersion]: https://en.wikipedia.org/wiki/Atmospheric_dispersion_modeling
[ref_attar]: https://en.wikipedia.org/wiki/Attar
[ref_bakhoor]: https://en.wikipedia.org/wiki/Bakhoor
[ref_berloque_dermatitis]: https://en.wikipedia.org/wiki/Berloque_dermatitis
[ref_clausius_clapeyron]: https://en.wikipedia.org/wiki/Clausius%E2%80%93Clapeyron_relation
[ref_kyphi]: https://en.wikipedia.org/wiki/Kyphi
[ref_note_perfumery]: https://en.wikipedia.org/wiki/Note_(perfumery)
[ref_pepper_spray]: https://en.wikipedia.org/wiki/Pepper_spray
[ref_perfume]: https://en.wikipedia.org/wiki/Perfume
[ref_proxemics]: https://en.wikipedia.org/wiki/Proxemics
[ref_sillage]: https://en.wikipedia.org/wiki/Sillage_(perfume)
[ref_solid_perfume]: https://en.wikipedia.org/wiki/Solid_perfume
[ref_stevens_power_law]: https://en.wikipedia.org/wiki/Stevens%27s_power_law
[ref_tapputi]: https://en.wikipedia.org/wiki/Tapputi
[research_baron_1983_sweet_smell]: https://doi.org/10.1037/0021-9010.68.4.709
[research_baron_1986_too_much]: https://doi.org/10.1111/j.1559-1816.1986.tb02275.x
[research_bronaugh_1990_absorption]: https://doi.org/10.1016/0278-6915(90)90111-Y
[research_court_greenblatt_2000_cat_ugt1a6]: https://doi.org/10.1097/00008571-200006000-00009
[research_craven_settles_2006_thermal_plume]: https://doi.org/10.1115/1.2353274
[research_dalton_2000_adaptation]: https://doi.org/10.1093/chemse/25.4.487
[research_diepgen_2015_eden]: https://doi.org/10.1111/bjd.14151
[research_doty_1984_age]: https://doi.org/10.1126/science.6505700
[research_doty_cameron_2009_sex_differences]: https://doi.org/10.1016/j.physbeh.2009.02.032
[research_elsharif_2015_linalool]: https://doi.org/10.3389/fchem.2015.00057
[research_keller_2007_or7d4]: https://doi.org/10.1038/nature06162
[research_lenochova_2012_perfume_blend]: https://doi.org/10.1371/journal.pone.0033810
[research_mata_2005_engineering_perfumes]: https://doi.org/10.1002/aic.10530
[research_mcgann_2017_human_olfaction]: https://doi.org/10.1126/science.aam7263
[research_moskowitz_1979_psychophysical]: https://library.scconline.org/v030n02/25
[research_nazaroff_weschler_2004]: https://doi.org/10.1016/j.atmosenv.2004.02.040
[research_reilly_2001_pepper_spray]: https://doi.org/10.1520/JFS14999J
[research_roberts_2009_deodorant]: https://doi.org/10.1111/j.1468-2494.2008.00477.x
[research_rodrigues_2021_perfume_engineering]: https://doi.org/10.3390/molecules26113095
[research_sato_akuhara_2023_musk]: https://doi.org/10.1093/chemse/bjac037
[research_savastano_2009_regional_temperature]: https://doi.org/10.3945/ajcn.2009.27567
[research_sccs_2012_fragrance_allergens]: https://ec.europa.eu/health/scientific_committees/consumer_safety/docs/sccs_o_102.pdf
[research_singer_2006_secondary_pollutants]: https://doi.org/10.1016/j.atmosenv.2006.06.005
[research_sorokowska_2016_body_odor_review]: https://doi.org/10.3389/fpsyg.2016.00530
[research_sorokowski_2019_sex_differences]: https://doi.org/10.3389/fpsyg.2019.00242
[research_steinemann_2016]: https://doi.org/10.1007/s11869-016-0442-z
[research_stevens_1957_psychophysical_law]: https://doi.org/10.1037/h0046162
[research_stevens_2019_head_cones]: https://doi.org/10.15184/aqy.2019.175
[research_webb_1992_skin_temperature]: https://doi.org/10.1007/BF00625070
[research_wyatt_2015_pheromones]: https://doi.org/10.1098/rspb.2014.2994
