---
layout: post
mathjax: true
comments: true
title: "X-Planes: Schweizer X-26 Frigate"
date: 2025-11-01 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 27
---

<!-- A323 -->
<script>console.log("A323");</script>

The [Schweizer SGS 2-32][ref_sgs_2_32] is a two-seat sailplane of 1962, built in Elmira, New York, sold to
soaring clubs, and about as far from a research aeroplane as an aircraft can be.
**The United States military bought it twice, gave it the same X-designation both times, and used it for two purposes that have nothing whatever to do with each other.**
This article is the twenty-seventh in the [X-Planes series][related_post_a297_xplanes_framing], following
the [X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], the
[X-3][related_post_a300_douglas_x3], the [X-4][related_post_a301_northrop_x4], the
[X-5][related_post_a302_bell_x5], the [X-6][related_post_a303_convair_x6], the
[X-7][related_post_a304_lockheed_x7], the [X-8][related_post_a305_aerojet_x8], the
[X-9][related_post_a306_bell_x9], the [X-10][related_post_a307_north_american_x10], the
[X-11][related_post_a308_convair_x11], the [X-12][related_post_a309_convair_x12], the
[X-13][related_post_a310_ryan_x13], the [X-14][related_post_a311_bell_x14], the
[X-15][related_post_a312_north_american_x15], the [X-16][related_post_a313_bell_x16], the
[X-17][related_post_a314_lockheed_x17], the [X-18][related_post_a315_hiller_x18], the
[X-19][related_post_a316_curtiss_wright_x19], the [X-20][related_post_a317_boeing_x20], the
[X-21][related_post_a318_northrop_x21], the [X-22][related_post_a319_bell_x22], the
[X-23][related_post_a320_martin_marietta_x23], the [X-24][related_post_a321_martin_marietta_x24], and the
[X-25][related_post_a322_bensen_x25].

As the [X-26A][ref_navair_x26a] it was flown unmodified at the [Naval Test Pilot School][ref_usntps] to
teach student test pilots what [adverse yaw][ref_adverse_yaw] feels like. As the X-26B it was the QT-2, for Quiet Thruster, a
silenced engine and a slow-turning propeller wrapped around the same airframe, flown over the Mekong Delta
at night in 1968 to watch the ground without being heard.

The whole designation, both halves of it, is [X-26][ref_x26].

**One of those programmes wanted the aircraft's worst handling trait to be as obvious as possible. The other wanted the aircraft to be as close to absent as possible.**
They are opposite requirements and they were met by the same airframe,
**because both of them are consequences of a single number**.

## The Research Question

**There are two, and the article's argument is that they have the same answer.**

**Can a student test pilot be taught to recognise adverse yaw before it matters?** A jet trainer exhibits
the phenomenon, but presents it in a fraction of a second and at small amplitude, which teaches nothing to
anyone who does not already know what happened.

**Can a manned aircraft loiter over hostile ground at night without being heard?** That is a question about
acoustics, about power, and in the end about how quiet the night is.

**The binding constraint in both cases is the lift-to-drag ratio, which for a wing of aspect ratio $A$ and zero-lift drag coefficient $C_{D_0}$ is**

$$\left( \frac{L}{D} \right)_{max} = \frac{1}{2} \sqrt{\frac{\pi e A}{C_{D_0}}}$$

Read one way that relation says a high lift-to-drag ratio **demands a long slender wing**, and a long
slender wing flown slowly is what produces large adverse yaw. Read the other way, through the power required
to sustain flight, it says a high lift-to-drag ratio **demands very little power**, and an engine that is
barely working can be silenced.

**The same property, pushed to an extreme by people who wanted neither of these things, produced both.**

## Programme Origin

[Schweizer Aircraft][ref_schweizer_aircraft] of Elmira built sailplanes for the American soaring market from
the 1930s. The SGS 2-32 was its high-performance two-seater, and by the standards of production sailplanes
it was large, heavy and very clean.

**The Navy's problem was pedagogical.** Student test pilots arriving at [Patuxent River][ref_patuxent] came
from tactical aircraft and mostly had no glider time. Yaw-roll coupling, and the [Dutch
roll][ref_dutch_roll] mode it feeds, is a phenomenon every one of them would meet, and meeting it for the
first time in a jet is both uninformative and dangerous.
**The school wanted an aircraft that exhibited the same physics slowly.** Four were ordered as the X-26A.

**The Army's problem was operational and arrived later.** Night observation over the Delta required an
aircraft that could loiter low without announcing itself, and the [specification][ref_yo3a] asked for
acoustic undetectability at 1,500 feet. Lockheed Missiles and Space Company took two X-26A airframes, serials
67-15345 and 67-15346, and rebuilt them as the QT-2, which in its Prize Crew form became the
[QT-2PC][ref_x26].

**Neither programme was a Schweizer initiative and neither aircraft was developed as a research vehicle.**

## The Vehicles

| | X-26A | X-26B |
|---|---|---|
| Basis | Schweizer SGS 2-32, unmodified | SGS 2-32 rebuilt as QT-2 and QT-2PC |
| Role | flying qualities instruction | night observation |
| Operator | United States Naval Test Pilot School | United States Army, in Vietnam |
| Power | none | [Continental O-200][ref_continental_o200], 100 horsepower |
| Propeller | none | four-blade wooden, on an extension shaft |
| Number | four ordered, with replacements | two converted |

**Specifications of the airframe both share**, from the sailplane record.

| Quantity | Value |
|---|---|
| Span | 57 ft 1.5 in |
| Wing area | 180 sq ft |
| Aspect ratio | 18.05 |
| Empty weight | 857 lb |
| Gross weight | 1,430 lb |
| Best glide ratio | 35 at 55.9 mph |
| Minimum sink | 124 ft/min |

**Three of the four X-26A airframes were lost and replaced**, which for a docile sailplane operated by a
test pilot school is worth noting instead of passing over, and is returned to under Where the Framing Breaks
Down.

**The X-26A outlasted almost every other aircraft in this series.** It remained in service at the Test Pilot
School for decades after the X-25, the X-24 and the rest had been retired to museums, because the phenomenon
it demonstrates did not change and neither did the cheapest way to demonstrate it.

## Sizing From First Principles

### The One Relation

**Everything in this article comes out of one relation.** The drag of a wing is a constant term plus a term
that lift itself creates,

$$C_D = C_{D_0} + \frac{C_L^2}{\pi e A}$$

**The second term is the common root of both halves of this article.** It is what makes the lift-to-drag
ratio high, because it falls as aspect ratio rises.
**And it is what makes a rolling wing drag asymmetrically**, which is the adverse yaw the Naval Test Pilot
School wanted to demonstrate. Induced drag as a subject is [Sibert 1943][research_sibert_1943], [Deyoung and Harper
1948][research_deyoung_harper_1948], [Jones 1950, The spanwise distribution of lift][research_jones_1950],
[Morton 1956][research_morton_1956], [Nonweiler 1960][research_nonweiler_1960], [Harry and Trobaugh 1966][research_harry_trobaugh_1966], [Loth and Boyle 1969][research_loth_boyle_1969], [Hancock 1972][research_hancock_1972], [Mamada and Ando 1974][research_mamada_ando_1974], [Sears 1974][research_sears_1974], [Haftka 1977][research_haftka_1977],
[Lundry 1977][research_lundry_1977], [Kida and Miyai 1978][research_kida_miyai_1978], [Pao and Lan 1978][research_pao_lan_1978], [Deyoung 1979][research_deyoung_1979],
[Kuhlman 1979][research_kuhlman_1979], [Bera† 1980][research_bera_1980], [Kida 1982][research_kida_1982],
[Hanin and Barsony-Nagy 1983][research_hanin_barsony_nagy_1983], [Marchman and Abtahi 1985][research_marchman_abtahi_1985], [Wilmott 1986][research_wilmott_1986], [Yeh and Plotkin 1986][research_yeh_plotkin_1986], [Kuhlman and Liaw 1987][research_kuhlman_liaw_1987], [McCutchen 1989][research_mccutchen_1989], [Sears 1990][research_sears_1990],
[Smith and Kroo 1990][research_smith_kroo_1990].

Maximising the ratio of the two coefficients puts them equal to one another,

$$\frac{C_L^2}{\pi e A} = C_{D_0} \quad \Longrightarrow \quad C_L^{\ast} = \sqrt{\pi e A \, C_{D_0}}$$

Taking an Oswald efficiency of 0.90 and a zero-lift drag coefficient of 0.012, which are ordinary values for
a clean sailplane and are **assumed rather than measured**,

$$A = \frac{b^2}{S} = \frac{(57.125)^2}{180} = 18.1$$

$$\left( \frac{L}{D} \right)_{max} = \frac{1}{2} \sqrt{\frac{\pi (0.90)(18.1)}{0.012}} = 32.7$$

against a quoted 35, which is agreement to within seven percent from geometry alone, and the lift
coefficient at which it occurs is

$$C_L^{\ast} = \sqrt{\pi (0.90)(18.1)(0.012)} = 0.784$$

**The quoted numbers agree with the relation once each is paired with the weight it belongs to.** The
best-glide speed is the speed at which the wing flies at $C_L^{\ast}$, with sea-level density
$\rho = 0.0023769$ slug per cubic foot,

$$V_{bg} = \sqrt{\frac{2 (W/S)}{\rho \, C_L^{\ast}}}, \qquad V_{bg}\big|_{7.94} = \sqrt{\frac{2 (7.94)}{(0.0023769)(0.784)}} = 92.3 \, \text{ft/s} = 62.9 \, \text{mph}, \qquad V_{bg}\big|_{6.0} = 80.2 \, \text{ft/s} = 54.7 \, \text{mph}$$

At the 1,430 pound gross weight, a wing loading of 7.94 pounds per square foot, that is 62.9 miles per hour
against a quoted 55.9, which is 13 percent adrift. The same sources quote a wing loading of 6.0 pounds per
square foot, which over 180 square feet is 1,080 pounds and not the gross weight at all.
**At that lighter weight the relation gives 54.7 miles per hour against the quoted 55.9, which is agreement to two percent.**
The quoted performance is a one-pilot number, so the discrepancy at gross weight comes from pairing it with
the wrong weight rather than from the aircraft.

The wing itself, and what a large aspect ratio buys and costs, is the induced-drag literature cited above,
and the sailplane literature it belongs to is [Lippisch 1930][research_lippisch_1930], [Turner 1942][research_turner_1942], [Klemin and Walling 1943][research_klemin_walling_1943], [Shenstone 1946][research_shenstone_1946], [The Sailplane as a meteorological probe 1948][research_the_sailplane_1948], [Johnson 1949][research_johnson_1949], [Wiggi 1949][research_wiggi_1949], [Yates 1949][research_yates_1949], [Reussner 1950][research_reussner_1950],
[Raspet 1952][research_raspet_1952], [Reussner 1953][research_reussner_1953], [Brown 1954][research_brown_1954], [MacCready 1962][research_maccready_1962], [McMasters and Palmer 1975][research_mcmasters_palmer_1975], [Pierson 1977][research_pierson_1977], [Bennett 1978][research_bennett_1978],
[McMasters 1979][research_mcmasters_1979], [Muser 1979][research_muser_1979], [Pierson and Chen 1979,
Minimum Altitude-Loss Soaring in][research_pierson_chen_1979], [Pierson and Chen 1979][research_pierson_chen_1979_2], [Sliwa and Sliwa 1979][research_sliwa_sliwa_1979],
[Turriziani 1979][research_turriziani_1979], [Janzen and Precourt 1989][research_janzen_precourt_1989],
[Hoey 1992][research_robert_g_hoey_1992], [Allen 2006][research_allen_2006], [Allen 2007][research_allen_2007], [Allen 2007][research_allen_2007_2], [Lin 2007][research_lin_2007]. The design tradition this aircraft comes out of
is set out in [Thomas on sailplane design][book_thomas_1999], and the drag bookkeeping behind the zero-lift
term is [Hoerner's compendium][book_hoerner_1965].

### Why This Aircraft Teaches Adverse Yaw

When an aeroplane rolls at rate $p$, a wing section at spanwise station $y$ meets the oncoming flow at an
incidence changed by the local vertical velocity,

$$\Delta \alpha = \frac{p \, y}{V}$$

**That changes the local lift, and through the polar above it changes the local induced drag**, upward on
the descending wing and downward on the ascending one.
**Integrating a spanwise load distribution to get a force is the oldest machinery in the subject**,
descending from lifting-line theory and the downwash it predicts, in the induced-drag literature cited
above. Integrating the asymmetry across an elliptically loaded
span gives the classical result,

$$C_{n_p} = -\frac{C_L}{8}$$

**The minus sign is the entire subject.** The wing that is rising carries more induced drag, so the
aeroplane yaws away from the direction of roll.

**Everything the article says about teaching follows from the lift coefficient sitting in that numerator.**
The adverse yaw is proportional to $C_L$, and $C_L$ is inversely proportional to the square of the speed,

$$C_L = \frac{2 (W/S)}{\rho V^2}$$

so **a slow aeroplane on a big wing produces a great deal of it**. The relation between the induced yawing and rolling moments of a wing goes back to [Munk 1925][research_munk_1925], the effect of the adverse yawing moment on lateral manoeuvrability at a high lift coefficient was measured in [Fehlner 1942][research_fehlner_1942], and the period's lateral control research is summarised in [Weick and Jones 1937][research_weick_jones_1937]. The yawing moment due to rolling is treated in [Johnson and Sternfield 1948][research_johnson_sternfield_1948] and [Martina 1953][research_martina_1953], and the roll response it competes with is measured in [Bennett and Johnson 1947][research_bennett_johnson_1947] and set against roll control power in the landing approach in [Hall and Boothe 1972][research_hall_boothe_1972]. The rest of this literature is gathered in the clusters on lateral control, ailerons and adverse yaw and on lateral-directional stability, roll damping and coupling below. The standard developments of the derivative machinery are [Etkin and Reid on flight dynamics][book_etkin_reid_1996] and, contemporary with the aircraft, [Perkins and Hage][book_perkins_hage_1949]. The account written for the pilots who would fly it is [Hurt's aerodynamics for naval aviators][book_hurt_1965].

### The Magnitude and the Rate, Which Both Help

During a steady roll at helix angle $pb/2V$ the yawing moment coefficient is

$$C_n = C_{n_p} \cdot \frac{pb}{2V}$$

and the sideslip that moment drives against the aircraft's directional stiffness is

$$\beta \approx \frac{|C_n|}{C_{n_\beta}}$$

**The helix angle is a property of the configuration rather than of the flight condition, and that deserves a proof.** In a steady
roll the moment the ailerons apply and the damping moment the roll itself generates are in balance,

$$C_{l_{\delta_a}} \delta_a + C_{l_p} \frac{pb}{2V} = 0 \quad \Longrightarrow \quad \frac{pb}{2V} = -\frac{C_{l_{\delta_a}} \delta_a}{C_{l_p}}$$

**There is no speed in that expression and no span either.** The helix angle is fixed by the aileron power
and the roll damping, both of which are shape properties, and both of which the period measured directly in
tunnels and in flight, in the roll-response literature cited above. The roll rate therefore
follows,

$$p = \frac{pb}{2V} \cdot \frac{2V}{b}$$

**and a long wing rolls slowly for the same reason a long lever turns slowly.** Bank angle is the integral
of that rate, so the time to reach a given attitude is

$$t = \frac{\phi}{p} = \frac{\phi \, b}{2 V \left( pb/2V \right)}$$

Taking the X-26A at 60 miles per hour and a generic jet trainer at 300, with **every jet quantity assumed**,

| | X-26A | jet trainer, assumed |
|---|---|---|
| Wing loading, lb/ft² | 7.9 | 60 |
| Span, ft | 57.1 | 25.3 |
| Speed, mph | 60 | 300 |
| Lift coefficient | 0.863 | 0.261 |
| Sideslip developed, deg | 6.2 | 1.4 |
| Roll rate, deg/s | 10.6 | 180 |
| Time to 45 degrees of bank, s | 4.25 | 0.25 |

**The sailplane shows the student four and a half times as much sideslip and takes seventeen times as long to do it.** The directional-stability side of that is set out in [Price 1943][research_price_1943] and [Baker 1948][research_baker_1948], measured in flight in [Crane and Reeder 1945][research_crane_reeder_1945] and examined for its sensitivity to the derivatives in [Stengel 1980][research_stengel_1980], and the coupled behaviour is treated in [Davis 1957][research_davis_1957], [Butler 1976][research_butler_1976_2] and [Velger and Shinar 1983][research_velger_shinar_1983]. The rest is gathered in the cluster on lateral-directional stability, roll damping and coupling below.

### An Index, and the Term It Cannot Omit

Multiplying the two effects gives a rough index of how observable the phenomenon is, which comes out at
**seventy-five**. Written as a scaling,

$$\beta \, t \propto \frac{(W/S) \, b}{V^3 C_{n_\beta}}$$

**The helix angle cancels out of that expression entirely**, which is not obvious and is worth saying,
because it means the comparison does not depend on how powerful the ailerons are.
**Without the directional stiffness this scaling disagrees with the worked cases by exactly a factor of two**,
which is the ratio of the two aircraft's assumed $C_{n_\beta}$, so the stiffness is an essential term and
not a refinement.

### How Slowly the Demonstration Could Be Flown

**Adverse yaw grows as lift coefficient, so the demonstration wants to be flown as slowly as it safely can be, and what bounds that is the stall.**

$$V_{stall} = \sqrt{\frac{2 (W/S)}{\rho \, C_{L_{max}}}}$$

**This cannot be predicted, because the maximum lift coefficient is not known**, and what a given section
will actually reach is a measured quantity and not a derived one, in the induced-drag and sailplane
literature cited above. The relation is therefore inverted instead. The
quoted 46 mile per hour stall implies

$$C_{L_{max}} = \frac{2 (W/S)}{\rho V_{stall}^2} = 1.11$$

at the light weight, or 1.47 at gross.
**The first is an entirely ordinary value for an unflapped sailplane section and the second is high for one**,
which is a third piece of evidence that the quoted performance figures belong to the lighter aircraft,
agreeing with what the glide speed already suggested.

Taking the light-weight value, the 60 mile per hour training case sits about thirty percent above the stall,
**which is close enough to make the phenomenon large and far enough to make it safe.** At a fixed weight the
sideslip scales as $C_L$ and therefore as $1/V^2$, so

$$\frac{V}{V_{stall}} = \frac{60}{46} = 1.30, \qquad \frac{\beta_{stall}}{\beta_{60}} = \left( \frac{60}{46} \right)^2 = 1.70$$

Flown at the stall itself the sideslip would be about seventy percent larger, and unrecoverable inattention
would cost rather more than a lesson.

**Neither aircraft is more badly behaved than the other in any dimensionless sense.** They are the same
physics. The sailplane simply runs it slowly and at large amplitude, which is the entire pedagogical
argument stated as arithmetic.

## Dependent Systems

### Reading the Same Relation as a Power Requirement

Steady flight requires power to overcome drag,

$$P = \frac{W V}{L/D}$$

**and a high lift-to-drag ratio is precisely a statement that this number is small.** Taking an assumed
2,400 pound gross weight for the QT-2PC and an assumed lift-to-drag ratio of 20, degraded from the
sailplane's 35 by the engine, the shaft, the sensors and a fixed propeller,

$$P = \frac{(2400)(110 \, \text{ft/s})}{20} = 13{,}200 \, \text{ft lb/s} = 24 \, \text{hp}$$

**Twenty-four horsepower of the hundred installed.** That margin is the whole design.

### Best Glide Is Not Minimum Power, and the Loitering Aircraft Wanted the Second

**These are different speeds and the distinction matters here.** The power-required curve and the two speeds
it distinguishes are among the oldest results in aircraft performance and are treated thoroughly in the
period literature, in [Rice 1946][research_rice_1946], [Hanks 1956][research_hanks_1956], [Bogdanovic et al 1965][research_bogdanovic_1965], [Finnestead and Antoniou 1965][research_finnestead_antoniou_1965], [Bert 1981][research_bert_1981], [Laine 1982][research_laine_1982], [Torenbeek and Wittenberg 1983][research_torenbeek_wittenberg_1983], [Hall and Rogan 1988][research_hall_rogan_1988], [Hall and Rogan 1989][research_hall_rogan_1989]. Writing the power required
against speed shows two terms pulling opposite ways,

$$P = \tfrac{1}{2} \rho V^3 S \, C_{D_0} + \frac{2 W^2}{\rho V S \pi e A}$$

Differentiating and setting the derivative to zero puts the parasite term at **three times** the induced
one, where maximising lift-to-drag put them **equal**. The consequences follow immediately,

$$C_{L, mp} = \sqrt{3} \, C_L^{\ast}, \qquad V_{mp} = \frac{V_{bg}}{3^{1/4}} = 0.760 \, V_{bg}, \qquad \left( \frac{L}{D} \right)_{mp} = \frac{\sqrt{3}}{2} \left( \frac{L}{D} \right)_{max}$$

so the power at the minimum is

$$\frac{P_{mp}}{P_{bg}} = \frac{0.760}{0.866} = 0.877$$

**a saving of 12.3 percent for flying 24 percent slower.** For the QT-2PC on the assumed figures best glide
is 81.5 miles per hour and minimum power is 62.0, and
**the quoted quiet cruise of 70 to 80 falls between them**, which is what an aircraft needing both endurance
and a speed margin actually does.

**The noise value of that choice is almost nothing, and saying so keeps two motives from being confused.**
If radiated sound power followed shaft power, 12.3 percent would be worth

$$10 \log_{10} \frac{1}{0.877} = 0.57 \text{ dB}$$

**Half a decibel. The loiter speed was chosen for endurance and not for quiet.** An engine asked for a fifth
of its rating can be throttled deep, wrapped in mufflers that would strangle it at full power, and geared
down to a large slow propeller. **None of that is available to an aircraft that needs its engine.** The
silencing practice
is [Ohta 1935][research_ohta_1935], [Nelson 1938][research_nelson_1938], [Czarnecki and Davis 1948][research_czarnecki_davis_1948], [Davis et al 1953][research_davis_1953], [Stokes and Davis
1953][research_stokes_davis_1953], [Tyler and Towle 1955][research_tyler_towle_1955], [Dyer 1956][research_dyer_1956], [Fukuda 1960][research_fukuda_1960], [Fukuda 1960][research_fukuda_1960_2], [Keast 1961][research_keast_1961], [Hukuda 1962][research_hukuda_1962], [Fukuda 1963][research_fukuda_1963], [Fukuda 1963][research_fukuda_1963_2], [Emeric 1966][research_emeric_1966], [Alfredson 1971][research_alfredson_1971], [Bender and Brammer 1973][research_bender_brammer_1973], [Mutyala and Soedel 1974][research_mutyala_soedel_1974], [Pegg and Hilton 1974][research_pegg_hilton_1974], [Bender and Brammer 1975][research_bender_brammer_1975], [Robinson 1979][research_robinson_1979], [Shaikn 1979][research_shaikn_1979], [Lux and Landwehr 1980][research_lux_landwehr_1980], [Hoffman and Kennedy 1982][research_hoffman_kennedy_1982], [Rhodes 1982][research_rhodes_1982], [Prasad and Crocker 1983][research_prasad_crocker_1983], [Thomson 1983][research_thomson_1983], [Casey 1984][research_casey_1984], [Matsushita and Suzuki 1984][research_matsushita_suzuki_1984], [Buchwalder 1985][research_buchwalder_1985], [Ferrari and Castelli 1985][research_ferrari_castelli_1985], [Tanaka et al 1985][research_tanaka_1985], [Tarnow and Pommer 1988][research_tarnow_pommer_1988].

### What Quiet Means, Quantitatively

**This article uses decibels throughout and one should be defined before it does.** Sound pressure level is
a logarithmic ratio against a fixed reference,

$$\text{SPL} = 20 \log_{10} \frac{p}{p_{ref}}, \qquad p_{ref} = 20 \, \mu\text{Pa}$$

Intensity from a compact source falls over the surface of a sphere,

$$I = \frac{W_{ac}}{4 \pi r^2}$$

**Intensity goes as the inverse square of range and pressure as the inverse first power**, which is where
the twenty in front of the logarithm comes from rather than a ten.

The level therefore falls with the logarithm of distance,

$$\text{SPL}(r) = \text{SPL}(r_0) - 20 \log_{10} \frac{r}{r_0}$$

**Every doubling of slant range costs 6.02 decibels and no more.** That is the single most useful number in the whole subject, and it sets what a design programme can hope to buy. Propagation in the lower atmosphere is reviewed in [Nyborg and Mintzer 1955][research_nyborg_mintzer_1955], atmospheric absorption is given in [Bass et al 1972][research_bass_1972] and updated in [Bass et al 1990][research_bass_1990], refraction and ground attenuation are treated in [Kriebel 1972][research_kriebel_1972] and [Rasmussen 1986][research_rasmussen_1986], and the excess attenuation of aircraft noise with distance is measured in [Wolf and Raspet 1986][research_wolf_raspet_1986]. The rest is gathered in the cluster on outdoor sound propagation and atmospheric absorption below, and the physical principles behind it are [Pierce on acoustics][book_pierce_1981]. The engineering practice of quieting machinery is [Beranek on noise and vibration control][book_beranek_1988].

The maximum range at which the aircraft is audible follows by setting the received level equal to the
ambient,

$$r_{max} = r_0 \cdot 10^{\, (\text{SPL}(r_0) - L_{amb}) / 20}$$

**Calibrating that against the record rather than assuming a source level**, the QT-2PC was reported
detectable at 750 feet, which against an assumed 40 dBA rural night ambient implies about 49.5 dBA at 250
feet. Sweeping the ambient,

| Night ambient, dBA | Detected out to, ft |
|---|---|
| 30 | 2,372 |
| 35 | 1,334 |
| 40 | 750 |
| 45 | 422 |

**A detection range is a slant range and not an altitude**, which reconciles two numbers the record gives separately. **Flyover measurement is geometry before it is acoustics**, and the conventions for relating source position, receiver position and measured level are established practice, in [Zorumski 1977][research_zorumski_1977], [Muller 1971][research_muller_1971], [Chessell 1978][research_chessell_1978], [Willshire and Hilton 1979][research_willshire_hilton_1979], [Marsh 1981][research_marsh_1981], [Shivashankara and Stubbs 1987][research_shivashankara_stubbs_1987] and [Peart 1991][research_peart_1991], with the rest gathered in the clusters on aircraft noise sources, measurement, prediction and reduction and on outdoor sound propagation below.

$$r = \sqrt{h^2 + x^2}$$

The aircraft was detectable at 750 feet and missions were flown no lower than 800.
**Those are the same statement.** At any altitude above 750 feet the detection sphere does not reach the
ground at all, so the 800 foot floor is exactly the rule that the sphere must stay clear of the listener,
with fifty feet of margin.

**The aircraft's usable altitude is set by how quiet the night is, and not by the aircraft alone.** From the
range relation above, a change $\Delta L_{amb}$ in ambient scales the detection range by

$$\frac{r_{max}(L_{amb} - \Delta L_{amb})}{r_{max}(L_{amb})} = 10^{\Delta L_{amb}/20} = 10^{5/20} = 1.78$$

so a five decibel change in ambient moves the detection range by 78 percent.
**The specification was always partly about the weather.** Detection as a subject is [Schriever 1952][research_schriever_1952], [Bellucci 1963][research_bellucci_1963], [Chew and Chapin 1963][research_chew_chapin_1963], [Ollerhead 1971][research_ollerhead_1971], [Price and Hodge 1976][research_price_hodge_1976], [Ludeman 1979][research_ludeman_1979], [Ramachandra 1979][research_ramachandra_1979], [Michel 1989][research_michel_1989], [Mueller et al 1993][research_mueller_1993], [Sheffield 2000][research_sheffield_2000].

### Why the Simple Model Is the Right One

**Atmospheric absorption is strongly frequency dependent and is negligible here.** A slow propeller
radiates at low
frequency,

$$f = \frac{N_b \, \text{rpm}}{60}$$

which for four blades at 1,000 revolutions per minute is 67 hertz.
**How much sound the air itself absorbs, and how strongly that depends on frequency and humidity, is a measured subject with a long history**,
in the propagation literature cited above.
Absorption accumulates linearly with distance at a coefficient that rises steeply with frequency,

$$L_{abs} = \alpha \, r$$

| Frequency, Hz | Coefficient, dB per 1,000 ft | Over 1,500 ft, dB |
|---|---|---|
| 63 | 0.03 | 0.045 |
| 125 | 0.09 | 0.14 |
| 500 | 0.6 | 0.9 |
| 2,000 | 3.5 | 5.3 |

**At 67 hertz the whole mission altitude costs under a tenth of a decibel**, against the 6 that spreading
alone costs per doubling. The coefficients are order-of-magnitude values for moderate humidity and are
**assumed**.
**Spreading dominates and the inverse-square model is not an approximation worth apologising for.**

### The Propeller, Which Is the Lever

Propeller rotational noise rises very steeply with tip speed,

$$V_{tip} = \frac{\pi D \, \text{rpm}}{60}$$

A conventional light aircraft propeller of 6 feet at 2,700 revolutions per minute reaches 848 feet per
second. A large slow propeller of 8.5 feet at 1,000 reaches 445.
**The exponent relating sound power to tip speed depends on which harmonic dominates and on blade loading, and sources differ, so this article gives a range rather than a number.**

| Assumed exponent | Reduction, dB |
|---|---|
| 5 | 14.0 |
| 6 | 16.8 |
| 7 | 19.6 |

The theory of how a turning blade radiates is [Goldstein's aeroacoustics][book_goldstein_1976], and the
propeller performance it sits beside is [McCormick][book_mccormick_1979].

**There is a second reason the slow propeller is quiet.** **Propeller performance was reduced to charts in advance ratio and power coefficient long before it was computed**, and those charts are what a designer choosing a diameter and a reduction ratio actually used, in the performance literature cited under best glide and minimum power. The noise that follows from the choice was a research subject by [Deming 1937][research_deming_1937] and is reviewed in [Regier and Hubbard 1953][research_regier_hubbard_1953], small propeller aircraft are treated in [Maglieri and Hubbard 1975][research_maglieri_hubbard_1975] and a low noise propeller is designed and tested in [Succi 1981][research_succi_1981], with the prediction theory in [Farassat and Succi 1980][research_farassat_succi_1980] and [Hanson 1983][research_hanson_1983] and the tone's growth with tip Mach number in [Dittmar and Hall 1991][research_dittmar_hall_1991]. The rest is gathered in the cluster on propeller and rotor noise below. The advance ratio compares forward speed to blade speed,

$$J = \frac{V}{n D}$$

and comes out at 0.65 for the conventional installation against 0.78 for the slow one,
**so the slow propeller's blade sections are also more lightly loaded**, which reduces the loading noise as
well as the thickness noise the tip speed governs. Tip Mach number is

$$M_{tip} = \frac{V_{tip}}{a}$$

falling from 0.76 to 0.40 between the two installations.

**Tens of decibels against the six the specification needed.** The lever is far more than strong enough,
**which is why the interesting question is not how they made the propeller quiet but what was still audible once they had.**

### Why Quieting One Source Has a Ceiling

**That the limit moves to the exhaust and the airframe is easy to assert and worth showing.**
**Separating an aircraft's total noise into its components, and then deciding which one to attack, is a discipline of its own**,
and one the period developed precisely because engine quieting kept running into airframe and propeller
floors, in the flyover-measurement literature cited above. Independent sources add in power rather than
in pressure,

$$L_{total} = 10 \log_{10} \sum_i 10^{L_i / 10}$$

**So the gain from quieting one source is capped by whatever remains.** Suppose the propeller starts ten
decibels above everything else combined.

| Propeller reduced by, dB | Total level, dB | Actual gain, dB |
|---|---|---|
| 0 | 60.4 | 0.0 |
| 6 | 55.5 | 5.0 |
| 10 | 53.0 | 7.4 |
| 17 | 50.8 | 9.6 |
| 25 | 50.1 | 10.3 |

**A seventeen decibel propeller reduction buys ten.** Removing the propeller entirely would buy 10.4 and no
more, because the floor is set by the other sources.
**Beyond about fifteen decibels of propeller work the total stops moving**, which is the quantitative form
of a statement that is otherwise only an intuition. Exhaust, airframe and transmission noise all become the
limit as soon as the propeller stops dominating.

### What It Gave Up to Carry an Engine

The X-26A glides at 35 to 1. The QT-2PC carries an engine, a shaft, a propeller, fuel, sensors and a second
crewman on the same wing, and on the assumed figures its glide falls to 20 to 1 at a weight 1.7 times
greater. Sink rate is power divided by weight, which is the same statement as speed divided by glide ratio,

$$V_{sink} = \frac{P}{W} = \frac{V}{L/D}$$

**Written that way it supplies a second and independent check on the polar.** Minimum sink is the
minimum-power condition derived above, not the best-glide one.

Evaluating at the minimum-power point and the light weight, with the best-glide speed of 54.7 miles per hour
and the lift-to-drag ratio of 32.7 found above,

$$V_{mp} = 0.760 \times 54.7 = 41.6 \, \text{mph} = 61.0 \, \text{ft/s}, \qquad V_{sink} = \frac{61.0}{(0.866)(32.7)} = 2.16 \, \text{ft/s} = 129 \, \text{ft/min}$$

which is **129 feet per minute at 42 miles per hour, against a quoted 124 at 46**. That is 4 percent in sink
rate and 10 percent in speed,
**from the same two assumed parameters that produced the glide ratio and without any further fitting**. The
glide ratio and the minimum sink are independent quoted numbers, so reproducing both from one polar is worth
more than reproducing either alone.

**It is still a sailplane.** Even loaded and draggy it descends at a few hundred feet a minute with the
engine stopped, which meant the crew could shut down and loiter in silence.
**No other powered aircraft of the period could buy that capability at any price**, and the glide
performance behind it is [Lundberg 1937][research_lundberg_1937], [Lundberg 1938][research_lundberg_1938],
[Jackson et al 1993][research_jackson_1993], [Colling 1995][research_colling_1995].

### The Sensors and the Mission

The observation equipment, the low-light television and the night-vision devices of the period are [Cornell Aeronautical Lab Inc Buffalo Ny 1971][research_cornell_aeronautical_lab_inc_buffalo_ny_1971], [Cornell Aeronautical Lab Inc Buffalo Ny 1971][research_cornell_aeronautical_lab_inc_buffalo_ny_1971_2],
[Cornell Aeronautical Lab Inc Buffalo Ny 1971][research_cornell_aeronautical_lab_inc_buffalo_ny_1971_3], [Bailey and McClintic 1974][research_bailey_mcclintic_1974], [Reising et al 1996][research_reising_1996], [Craig et al 1999][research_craig_1999],
[Pleban and Beal 2002][research_pleban_beal_2002], [Fischer 2006][research_fischer_2006].
**This article does not dimension them**, because the acoustic and aerodynamic questions are the ones the
airframe answers and the sensors were carried rather than enabled by it.

## The Flight Test Record

**The two halves of this designation have very unequal records.**

The X-26A flew at the Naval Test Pilot School from the late 1960s and remained in the syllabus for decades, and the Navy's product page still lists it as operational, with [two in the inventory][ref_navair_x26a]. **Its record is a curriculum rather than a test report**, and the teaching tradition it sits in is described for the Naval Test Pilot School in [Johnson 1975][research_johnson_1975] and for the Air Force school in [Eppley 1963][research_eppley_1963], with the flying-qualities course text in [Air Force Test Pilot School Edwards Afb Ca 1991][research_air_force_test_pilot_school_edwards_afb_ca_1991], the pilot rating scale in [Cooper and Harper 1969][research_cooper_harper_1969], the specification of the period in [Chalk and Wilson 1969][research_chalk_wilson_1969] and its lateral-directional requirements in [Ashkenas 1965][research_ashkenas_1965], and the history of the subject in [Ashkenas 1984][research_ashkenas_1984] and [Mitchell et al 2003][research_mitchell_2003]. Teaching flight testing through soaring is described in [Stewart 2016][research_stewart_2016]. The rest is gathered in the clusters on flying and handling qualities and on flight test below.

The QT-2PC record is short, specific and much better documented as history. In Polmar's account in
[Naval History][ref_polmar_2017], two aircraft reached the Army airfield at Soc Trang in the Mekong Delta on
22 January 1968 and began operations almost immediately, flying **591 hours of night surveillance between
24 January and 24 March 1968** under the [Prize Crew evaluation][ref_x26]. In Albertson's account in
[Army Aviation][ref_albertson_2015], repeated passes over the airfield at decreasing altitude found the
aircraft first heard at 750 feet, against a [specification of 1,500][ref_yo3a], so missions were flown no
lower than 800 feet and en route altitudes were generally 1,200 to 1,500.

**The aircraft missed its acoustic specification by 6 decibels, which is one doubling of distance.** That is
a small miss for a first article, and the Army awarded Lockheed a [YO-3A production contract in July
1968][ref_polmar_2017] on the strength of it. The two aircraft returned to the Test Pilot School in 1969 and
were [redesignated X-26B][ref_x26]. Lockheed carried the work forward through the Q-Star to the
[YO-3A][ref_yo3a].
**The YO-3A's numbers and dates differ between accounts.** The X-26 summary gives
[eleven pre-production aircraft operating in Southeast Asia from mid-1969 to late 1971][ref_x26], the YO-3A
summary gives [eleven built, nine of which operated in South Vietnam from late June 1970 to September
1971][ref_yo3a], and Polmar gives [fourteen ordered, thirteen of them shipped to Vietnam in early
1970][ref_polmar_2017]. The range all three support is operation in Vietnam during 1970 and 1971.

**Seven research records cited here name a Schweizer aircraft, the Q-Star or the YO-3A in their titles, and the only one that evaluates the YO-3A in its operational role is the Army's preliminary evaluation**, in [Condon et al 1970][research_condon_1970]. The others are described under The Source Base.
**No cited record concerns the QT-2PC itself.**

## Comparison With Ground Prediction

**Two predictions can be checked against the record and they behave very differently.**

**The glide performance check succeeds and is not impressive.** Predicting 32.7 against a quoted 35 is seven
percent from an assumed drag coefficient and an assumed span efficiency, and
**a model with two free parameters that lands within seven percent has demonstrated very little.** It is
reported because it is a consistency check on the geometry, not because it is evidence.

**The reconciliation of the quoted glide speed is worth more.** The best-glide speed relation under The One
Relation and the quoted 55.9 miles per hour disagree by 13 percent at gross weight and agree to two percent
at the one-pilot weight.
**That is a case where the model and the sources are both right and the conflict lies only in pairing a speed with the wrong weight**, and it is
the more useful of the two checks because it resolved an apparent conflict rather than confirming an
expected agreement.

**The acoustic prediction cannot be checked at all and the article says so.** The source level was
calibrated backwards out of the one reported detection distance, so the detection-range table reproduces
that distance **by construction and not by prediction**. It has no independent confirmation. What it does
provide is the sensitivity, and the sensitivity is the finding.
**The detection range moves 78 percent for a 5 decibel change in ambient, by the range ratio under What Quiet Means, so the aircraft's usable altitude was never a property of the aircraft alone.**

## What the Data Changed

**The X-26A changed how test pilots are taught and nothing else, which is not a small thing.** Generations
of graduates met adverse yaw for the first time in an aircraft that could not hurt them with it. That is a
contribution to the profession and not to aeronautics, and it does not appear in any aerodynamic result.

**The X-26B changed a good deal more.** The QT-2PC demonstrated that a manned aircraft could loiter low at
night without being heard, which was not previously established, and it did so within 6 decibels of a
demanding specification on the first attempt. **It led directly to the Q-Star and the YO-3A**, and the YO-3A
flew operationally.

**The deeper consequence is that the quiet-aircraft problem turned out to be an acoustics problem and not an aeronautics problem.**
Once the propeller was slowed, the limit moved to the exhaust, then to the airframe, then to the
transmission. **That is the signature of a design that has run out of dominant terms**, and it is why the
line stopped at the YO-3A rather than continuing indefinitely.

## The Contemporary Literature

| Cluster | Records |
|---|---|
| Propeller aerodynamics, design and propulsion | 275 |
| Propeller and rotor noise | 244 |
| Aircraft noise sources, measurement, prediction and reduction | 243 |
| Performance, power required, endurance and range | 232 |
| Aeroelasticity, flutter and gust loads | 203 |
| Flight test, system identification and parameter estimation | 202 |
| Pilot training, simulation, human factors and safety | 187 |
| Lateral control, ailerons and adverse yaw | 180 |
| Sailplanes, gliders and soaring | 178 |
| Flying and handling qualities | 160 |
| Lateral-directional stability, roll damping and coupling | 153 |
| Outdoor sound propagation and atmospheric absorption | 152 |
| Induced drag, span loading and the high aspect ratio wing | 144 |
| Community noise, annoyance and psychoacoustics | 137 |
| Acoustic and aural detection of aircraft | 134 |
| Unmanned aircraft design and operation | 104 |
| Engine exhaust noise and mufflers | 85 |
| Loss of control, upset recovery, stall and spin | 75 |
| Flight control, control allocation and fault tolerance | 74 |
| Aerodynamics, airfoils and aerodynamic design | 62 |
| Airframe noise, cabin noise and vibration | 62 |
| Surveillance, reconnaissance and observation | 54 |
| Electric, hybrid-electric and solar-powered aircraft | 41 |
| Flight dynamics, stability and simulation models | 35 |
| Other aeronautical literature | 30 |
| Wind tunnels, models and test technique | 26 |
| Rotorcraft and vertical lift flight mechanics | 12 |
| **Total** | **3,484** |

**Both halves of this designation have living descendants, and there is a pattern in what happened to them.**

**Each programme existed because of a human in the aircraft, and in each case the modern answer removed the human.**
The X-26A existed to teach a pilot to notice something. The X-26B existed to make a manned aircraft
inaudible.
**One mission is now largely discharged by systems that make noticing unnecessary, and the other by aircraft with nobody aboard that are quiet because they are small.**

### The X-26A's Argument Became a Regulation

**This is the largest thing that has happened to the first half of the X-26, and it is a considerable promotion for a claim nobody ever measured.**

Loss of control in flight is now a named accident category and the leading cause of fatal accidents in commercial aviation. **Upset prevention and recovery training became a regulatory requirement and no longer a good idea**, and the surrounding literature covers startle and surprise in [Landman et al 2017][research_landman_2017], [Landman et al 2020][research_landman_2020] and [Causse et al 2026][research_causse_2026], upset recovery training and its simulators in [Degtyarev et al 2021][research_degtyarev_2021], [Ryffel et al 2019][research_ryffel_2019] and [Wu et al 2020][research_wu_2020], the degradation of manual flying skill under automation in [Leonidov 2025][research_leonidov_2025], a loss of control accident in [Bromfield et al 2023][research_bromfield_2023], and the envelope protection and automatic recovery that make noticing unnecessary in [Lombaerts et al 2017][research_lombaerts_2017] and [Wang et al 2024][research_wang_2024]. The rest is gathered in the clusters on loss of control, upset recovery, stall and spin and on pilot training below.

**The X-26A's justification was that a pilot must meet the phenomenon somewhere safe before meeting it somewhere dangerous.**
That was an assertion in 1968 and it is a rule now.

**The other half of the answer removes the need to notice at all.** Envelope protection in a fly-by-wire
aircraft prevents the excursion instead of training the recovery, which is a different philosophy and is in
tension with the first.
**An aircraft that cannot be upset does not teach its pilot what an upset feels like**, and the training
requirement exists partly because of that.

### Adverse Yaw, Now Identified From Data Rather Than Demonstrated

The derivatives the X-26A demonstrated by feel are now extracted numerically from flight data, and the
lateral-directional behaviour is modelled, damped and allocated across control surfaces instead of flown
around, in [Zhu and Duan 2015][research_zhu_duan_2015], [Korsun et al 2018][research_korsun_2018], [Kumar and Ghosh 2018][research_kumar_ghosh_2018], [Dhayalan et al 2018][research_r_2018], [Wu et al 2018][research_wu_2018], [Ma et al 2019][research_ma_2019], [Shen et al 2021][research_shen_2021], [Lyu et al 2022][research_lyu_2022], [Wang et al 2022][research_wang_2022], [Jategaonkar 2023][research_jategaonkar_2023], [Korsun and Moung Htang 2023][research_korsun_moung_htang_2023], [Kumar and Ghosh 2023][research_kumar_ghosh_2023_2], [Shi et al 2023][research_shi_2023],
[Simmons et al 2023][research_simmons_2023_2], [Sánchez et al 2024][research_sanchez_2024], [Abdul Rashid et al 2025][research_abdul_rashid_2025].

### Quiet Flight, Attempted Again

**Electric propulsion has revived the quiet aircraft as a serious objective**, this time for community acceptability rather than concealment, and that has turned the subject from a physical one into a partly perceptual one. Psychoacoustic annoyance metrics and community response are where the effort now goes, in [Gille et al 2017][research_gille_2017], [Christian 2021][research_christian_2021], [Boucher et al 2023][research_boucher_2023] and [Tracy et al 2024][research_tracy_2024], together with the acoustic design of electric and distributed-propulsion aircraft in [Nark et al 2017][research_nark_2017], [Berton and Nark 2019][research_berton_nark_2019] and [Thomas and Hansman 2021][research_thomas_hansman_2021], design for community noise in [Iemma 2016][research_iemma_2016] and [Sahai et al 2017][research_sahai_2017], and the urban air mobility case in [Rizzi and Rafaelof 2021][research_rizzi_rafaelof_2021]. The rest is gathered in the clusters on community noise, annoyance and psychoacoustics and on aircraft noise sources below.

**The QT-2 wanted to be inaudible to an enemy, and contemporary quiet-aircraft work wants to be
acceptable to a neighbour.** The physics is identical and the criterion is not. Spherical spreading still
costs 6 decibels per doubling. What has changed is that the threshold is no longer an ambient noise level and a listening sentry,
but a population and its tolerance.

### The Mission Went Unmanned, Which Solved the Acoustic Problem by Accident

**The QT-2PC's entire difficulty was that a manned aircraft has to be big enough to carry a person.** That
set the wing area, the weight, the power and therefore the noise, and every gram of muffler and every foot
of extension shaft was spent fighting a floor set by human size.

**A small unmanned aircraft has no such floor.** Persistent low-altitude observation is now routine, and the
aircraft that fly it are quiet not because anyone silenced them but because they are small and need very
little power, in [Stewart et al 2012][research_stewart_2012], [Leahy et al 2015][research_leahy_2015], [Sonmez and Alemdaroglu 2015][research_sonmez_alemdaroglu_2015],
[Abich IV et al 2016][research_abich_iv_2016], [Frazier 2016][research_frazier_2016], [Hosseini and Mesbahi 2016][research_hosseini_mesbahi_2016], [Kisabo et al 2017][research_kisabo_2017], [Hasan et al 2018][research_hasan_2018], [Huang et al 2018][research_huang_2018], [Shin et al 2018][research_shin_2018], [Olsen et al 2019][research_olsen_2019], [Wu et al 2019][research_wu_2019_2], [Dinc and Otkur 2020][research_dinc_otkur_2020], [Chu et al 2021][research_chu_2021], [Januszewska and Pringle 2021][research_januszewska_pringle_2021], [Monzambe et al 2024][research_monzambe_2024], [Setiawan et al 2026][research_setiawan_2026].

**The programme's constraint turned out to be the thing that could be deleted**, which is also how the
[X-25][related_post_a322_bensen_x25] question, how to give a descending crewman a choice, was answered.

### And Now Everyone Wants to Hear the Aircraft

**The QT-2's problem has been inverted.** Contemporary work is largely about **detecting** small aircraft
acoustically rather than hiding them, which is the same physics read from the other end, in [Brown et al 2016][research_brown_2016], [Culver 2016][research_culver_2016], [Goldman 2016][research_goldman_2016], [Kim 2016][research_kim_2016], [Bernardini et al 2017][research_bernardini_2017], [Kloet et al 2017][research_kloet_2017], [Harvey and OYoung 2018][research_harvey_oyoung_2018], [Oleynikov et al 2018][research_oleynikov_2018], [Sedunov et al 2018][research_sedunov_2018], [Guzik et al 2019][research_guzik_2019], [Haddad et al 2019][research_haddad_2019], [Sedunov et al 2019][research_sedunov_2019], [Manickam et al 2020][research_manickam_2020], [Kozak 2021][research_kozak_2021], [Liu et al 2021][research_liu_2021],
[Uddin et al 2021][research_uddin_2021], [Aydın and Kızılay 2022][research_aydn_kzlay_2022], [Gopalan et al 2022][research_gopalan_2022], [Kadyrov et al 2022][research_kadyrov_2022], [Rasband et al 2023][research_rasband_2023], [Sahithi 2023][research_sahithi_2023], [Seidaliyeva et al 2023][research_seidaliyeva_2023], [Dafrallah and Akhloufi 2024][research_dafrallah_akhloufi_2024], [Kumar S Rajanikanth 2024][research_kumar_s_rajanikanth_2024], [Paszkowski et al 2024][research_paszkowski_2024], [Hai et al 2025][research_hai_2025], [Jekateryńczuk and Piotrowski 2025][research_jekaterynczuk_piotrowski_2025], [Lotinga et al 2025][research_lotinga_2025], [de Macedo et al 2025][research_de_macedo_2025], [Alimadadi 2026][research_alimadadi_2026], [Ghenescu et al 2026][research_ghenescu_2026], [Sesham et al 2026][research_sesham_2026].

### Propeller Noise, Computed

Propeller and rotor acoustics is now a computational discipline, with a benchmark in [Casalino et al 2021][research_casalino_2021], parametric and wake studies in [Yang et al 2017][research_yang_2017] and [Kingan and Parry 2020][research_kingan_parry_2020], positive and negative thrust in [Goyal et al 2024][research_goyal_2024], adjoint design in [Zhi et al 2025][research_zhi_2025] and prediction methods compared with flyover data in [Domogalla et al 2026][research_domogalla_2026], and outdoor propagation likewise, in [Wilson 2024][research_wilson_2024], [Ostashev and Wilson 2022][research_ostashev_wilson_2022], [Kirby 2021][research_kirby_2021] and [Hart et al 2016][research_hart_2016]. The rest is gathered in the clusters on propeller and rotor noise and on outdoor sound propagation below.

### The Very Efficient Aeroplane

High aspect ratio has become a mainstream objective rather than a sailplane peculiarity, in the transport studies [Kretov and Tiniakov 2022][research_kretov_tiniakov_2022], [Ma et al 2022][research_ma_2022], [Wahler et al 2025][research_wahler_2025] and [Gilbrook et al 2025][research_gilbrook_2025] and the high-altitude aircraft of [Fladeland et al 2019][research_fladeland_2019] and [Doyle 2020][research_doyle_2020], while the sailplane itself is still being refined, in [Aero structural optimization for sailplane wing in preliminary design 2018][research_aero_structural_2018] and [Yu 2026][research_yu_2026]. The rest is gathered in the clusters on induced drag, span loading and the high aspect ratio wing and on aeroelasticity below.

### Training, Measured Rather Than Asserted

**The X-26A's justification was a pedagogical assertion and it was never measured.** Contemporary work on
training transfer and simulator fidelity is where that assertion would now have to be defended, in [Harnyoot 2018][research_harnyoot_2018], [Myers et al 2018][research_myers_2018],
[Henriquez Huecas et al 2022][research_henriquez_huecas_2022], [Hjellvik and Mallam 2024][research_hjellvik_mallam_2024], [Zhang et al 2025][research_zhang_2025], [Somerville et al 2026][research_somerville_2026], [Somerville et al 2026][research_somerville_2026_2].

### What the Survey Shows

**Both halves of the X-26 were about a human in the aircraft, and both have been answered by removing the human.**
Adverse yaw is still taught in slow aircraft, but envelope protection now prevents the excursion instead of
teaching the recovery, so the X-26A's method is one answer among several. The X-26B's mission is flown by
unmanned aircraft that are quiet because they are small, and the same acoustic equations are now used more
often by the listener than by the flyer.

**One thing the survey does not show, and the absence is worth stating.** Nothing found here measures
whether flying a sailplane actually teaches adverse yaw better than a simulator or a briefing does.
**The X-26A's central claim remains untested sixty years on**, which is a curious position for an argument
that has meanwhile been written into regulation.

### Propeller aerodynamics, design and propulsion

Propeller aerodynamics, design, efficiency and structure, with the engines and propulsion systems that drive them. **85 of the 275 records date from before 1970.**

**275 records.** \[[Adamson 1968][research_adamson_1968]\] \[[Adler 1960][research_adler_1960]\] \[[Aerodynamic design of low-speed aircraft with a NASA 1986][research_aerodynamic_design_1986]\] \[[Aithal et al 2004][research_aithal_2004]\] \[[Aleshin et al 2018][research_aleshin_2018]\] \[[Alfares 2026][research_alfares_2026]\] \[[Almeida et al 2016][research_almeida_2016]\] \[[Alonso Castilla et al 2021][research_alonso_castilla_2021]\] \[[Altman 2002][research_altman_2002]\] \[[Annand 1950][research_annand_1950]\] \[[Army Service Forces Washington Dc 1940][research_armyserviceforceswashingtondc_1940]\] \[[Avco Lycoming Div Stratford Ct 1970][research_avco_lycoming_div_stratford_ct_1970]\] \[[Avrenli and Dempsey 2015][research_avrenli_dempsey_2015]\] \[[Baek et al 2015][research_baek_2015]\] \[[Baek et al 2021][research_baek_2021]\] \[[Baker 1942][research_baker_1942]\] \[[Ball 1987][research_ball_1987]\] \[[Balyakin 2015][research_balyakin_2015]\] \[[Barufaldi and Morales 2023][research_barufaldi_morales_2023]\] \[[Baxter 1951][research_baxter_1951]\] \[[Beauregard 1964][research_beauregard_1964]\] \[[Bell Aerospace Co Buffalo Ny 1956][research_bell_aerospace_co_buffalo_ny_1956]\] \[[Bell Aerospace Co Buffalo Ny 1956][research_bell_aerospace_co_buffalo_ny_1956_3]\] \[[Bell Aerospace Co Buffalo Ny 1956][research_bell_aerospace_co_buffalo_ny_1956_2]\] \[[Berenschot 2001][research_berenschot_2001]\] \[[Bergman 1971][research_bergman_1971]\] \[[Bergmann et al 2021][research_bergmann_2021]\] \[[Bert 1999][research_bert_1999]\] \[[Beschorner et al 2025][research_beschorner_2025]\] \[[Bhat et al 2026][research_bhat_2026]\] \[[Bienen 1927][research_bienen_1927]\] \[[Biermann and Conway 1942][research_biermann_conway_1942]\] \[[Bogdanovic et al 1965][research_bogdanovic_1965]\] \[[Borer et al 2016][research_borer_2016]\] \[[Boswell and Miller 1968][research_boswell_miller_1968]\] \[[Litherland et al][research_brandon_l_litherland]\] \[[Bravo et al 2021][research_bravo_2021]\] \[[Briardy and Head 1968][research_briardy_head_1968]\] \[[Bridges 2021][research_bridges_2021]\] \[[Brockett 1972][research_brockett_1972]\] \[[Bronz 2019][research_bronz_2019]\] \[[Brun et al 1947][research_brun_feder_1947]\] \[[Burnell and Fan 1957][research_burnell_fan_1957]\] \[[Butler et al 1966][research_butler_huang_1966]\] \[[Robb et al][research_caleb_robb]\] \[[Calise et al 1999][research_calise_1999]\] \[[Campbell and McDonald 1963][research_campbell_mcdonald_1963]\] \[[Cao et al 2026][research_cao_gao_2026]\] \[[Capone and Bare 1987][research_capone_bare_1987]\] \[[Meyer and Johnson 1952][research_carllmeyer_lavernajohnson_1952]\] \[[Carroll and Carroll 2005][research_carroll_carroll_2005]\] \[[Cavcar 2011][research_cavcar_2011]\] \[[Cavcar and Cavcar 2005][research_cavcar_cavcar_2005]\] \[[Chakraborty and Mishra 2023][research_chakraborty_mishra_2023]\] \[[Chang and Sullivan 1984][research_chang_sullivan_1984]\] \[[Chapter 12 Converting a Piston Engine Aircraft to a 2019][research_chapter_12_2019]\] \[[Chen et al 2026][research_chen_2026_5]\] \[[Chen et al 2026][research_chen_2026_4]\] \[[Cheng et al 2022][research_cheng_2022]\] \[[Cheng et al 2023][research_cheng_2023]\] \[[Clark 1953][research_clark_jr_1953]\] \[[Codon and Bowles 1979][research_codon_bowles_1979]\] \[[Colozza 2002][research_colozza_2002]\] \[[Composite propeller blade 1972][research_composite_propeller_1972]\] \[[Computer simulates aircraft-engine performance 1974][research_computer_simulates_1974]\] \[[Computer techniques for propeller blade section design 1976][research_computer_techniques_1976]\] \[[Cook 1965][research_cook_1965]\] \[[Coward 1955][research_coward_1955]\] \[[Cummings 1929][research_cummings_1929]\] \[[Cummings 1968][research_cummings_1968]\] \[[Cusati et al 2023][research_cusati_2023]\] \[[Dahms and Bardenhagen 2019][research_dahms_bardenhagen_2019]\] \[[Dailey 1955][research_dailey_1955]\] \[[De Hoff and Hall 1978][research_dehoff_hall_1978]\] \[[de Vries and Vos 2023][research_de_vries_vos_2023]\] \[[de Vries et al 2019][research_de_vries_2019]\] \[[Deng et al 2026][research_deng_2026]\] \[[Denning 1962][research_denning_1962]\] \[[Design and Analysis of 2023, Design and Analysis of Propeller][research_design_and_2023_2]\] \[[Deveaux 1965][research_deveaux_1965]\] \[[Dinc and Otkur 2020][research_dinc_otkur_2020]\] \[[Doblhoff 1956][research_doblhoff_1956]\] \[[Dorfling and Rokhsaz 2015][research_dorfling_rokhsaz_2015]\] \[[Dryden and Ballif 1930][research_dryden_ballif_1930]\] \[[Duffy 1968][research_duffy_1968]\] \[[Duhl and Thompson 1977][research_duhl_thompson_1977]\] \[[Dunlap 1969][research_dunlap_1969]\] \[[Durand 1893][research_durand_1893]\] \[[Echavarria and Poroseva 2015][research_echavarria_poroseva_2015]\] \[[Glodeck and Standahar 1944][research_edwardglodeck_raymstandahar_1944]\] \[[Epstein and OFlarity 2019][research_epstein_oflarity_2019]\] \[[Erickson et al 1965][research_erickson_johnc_1965]\] \[[Eyerci̇oğlu and Aladağ 2021][research_eyercioglu_aladag_2021]\] \[[Fard et al 2022][research_fard_2022]\] \[[Farokhi and Vertzberger 1989][research_farokhi_vertzberger_1989]\] \[[Felder et al 2009][research_felder_kim_2009]\] \[[Finger et al 2020][research_finger_2020]\] \[[Fredericks et al 2013][research_fredericks_2013]\] \[[Friedrich and Robertson 2015][research_friedrich_robertson_2015]\] \[[Fry 1967][research_fry_1967]\] \[[Gao et al 2019][research_gao_2019]\] \[[Gao et al 2024][research_gao_shao_2024]\] \[[Gayle and Jeracki 1989][research_gayle_jeracki_1989]\] \[[General Electric Co Cincinnati Oh 1964][research_general_electric_co_cincinnati_oh_1964]\] \[[Gerstle et al 1999][research_gerstle_1999]\] \[[Gilyard 1974][research_gilyard_1974]\] \[[Goland et al 1964][research_goland_miller_1964]\] \[[Zilliac 2026][research_gregorygzilliac_2026]\] \[[Gulyaeva et al 2018][research_gulyaeva_2018]\] \[[Gur 2014][research_gur_2014]\] \[[Harris 1996][research_harris_1996]\] \[[Heidelberg and Woodward 1989][research_heidelberg_woodward_1989]\] \[[Hennessy 2014][research_hennessy_2014]\] \[[Hiller Aircraft Corp Palo Alto Ca 1956][research_hiller_aircraft_corp_palo_alto_ca_1956]\] \[[Hirschkron et al 1979][research_hirschkron_1979]\] \[[Hirschkron et al 1979][research_hirschkron_1979_2]\] \[[Hirschkron et al 1979][research_hirschkron_1979_3]\] \[[Hirsh 1965][research_hirsh_1965]\] \[[Hoehne and Hoffman 1961][research_hoehne_hoffman_1961]\] \[[Hoyos et al 2021][research_hoyos_jimenez_2021]\] \[[Huang 2023][research_huang_2023_2]\] \[[Hughes and Gazzaniga 1988][research_hughes_gazzaniga_1988]\] \[[Identification method of temperature corrections to aircraft engine thrust in flight tests 2023][research_identification_method_2023]\] \[[Jamison 1966][research_jamison_1966]\] \[[Jeracki and Mitchell 1981][research_jeracki_mitchell_1981]\] \[[Jones 1965][research_jones_1965]\] \[[Jones et al 2013][research_jones_2013]\] \[[Kim et al 2025][research_kim_2025]\] \[[Koch 1998][research_koch_1998]\] \[[Korsun et al 2017][research_korsun_2017]\] \[[Korsun et al 2024][research_korsun_2024]\] \[[Kozakiewicz and Grzegorczyk 2021][research_kozakiewicz_grzegorczyk_2021]\] \[[Kriebel 1964][research_kriebel_1964]\] \[[Kruger and Uranga 2024][research_kruger_uranga_2024]\] \[[Köhler and Jeschke 2021][research_kohler_jeschke_2021]\] \[[Laitone 1983][research_laitone_1983]\] \[[Large and Pesyridis 2018][research_large_pesyridis_2018]\] \[[Lee and Ko 2025][research_lee_ko_2025]\] \[[Lee and Yee 2024][research_lee_yee_2024]\] \[[Lee et al 2022][research_lee_2022]\] \[[Leishman 1966][research_leishman_1966]\] \[[Leong Chee Hang et al 2022][research_leong_chee_hang_2022]\] \[[Level Flight Performance Flight Test and Data Reduction 2003][research_level_flight_2003]\] \[[Li and Da Ronch 2025][research_li_daronch_2025]\] \[[Li et al 2022][research_li_2022_3]\] \[[Li et al 2026][research_li_2026]\] \[[Lieberman and Hoffman 1964][research_lieberman_hoffman_1964]\] \[[Liu et al 1983][research_liu_1983]\] \[[Louis and Louis 2020][research_louis_louis_2020]\] \[[Lourenco et al 1996][research_lourenco_1996]\] \[[Lucas 1978][research_lucas_1978]\] \[[Ma et al 2020][research_ma_2020]\] \[[Ma et al 2025][research_ma_2025_2]\] \[[Macey 1956][research_macey_1956]\] \[[MacNeill and Verstraete 2017][research_macneill_verstraete_2017]\] \[[Madureira and de Almeida 2026][research_madureira_dealmeida_2026]\] \[[Magee and Taylor 1971][research_magee_taylor_1971]\] \[[Malina and Parsons 1941][research_malina_parsons_1941]\] \[[Mangold and Strohmayer 2025][research_mangold_strohmayer_2025]\] \[[Maynard and Evans 1945][research_maynard_evans_1945]\] \[[McCormick 1956][research_mccormick_b_w_1956]\] \[[McVeigh and McHugh 1984][research_mcveigh_mchugh_1984]\] \[[Meng et al 2017][research_meng_2017]\] \[[Merrill 2003][research_merrill_2003]\] \[[Meyerhoff and Zvengrowski 1962][research_meyerhoff_zvengrowski_1962]\] \[[Mikkelson et al 1984][research_mikkelson_mitchell_1984]\] \[[Mitchell and Mikkelson 1982][research_mitchell_mikkelson_1982]\] \[[Morgado et al 2013][research_morgado_silvestre_2013]\] \[[Morgan 1954][research_morgan_1954]\] \[[Morgan 1961][research_morgan_1961]\] \[[Nakka and Alexander-Ramos 2021][research_nakka_alexander_ramos_2021]\] \[[Naval Air Test Center Patuxent River Md 1957][research_naval_air_test_center_patuxent_river_md_1957]\] \[[Nelson 1965][research_nelson_1965]\] \[[Newell and Herrick 1979][research_newell_herrick_1979]\] \[[Nimal and Venkatesan 2019][research_nimal_a_2019]\] \[[Norris and Bauer 1993][research_norris_bauer_1993]\] \[[Omair Alhatim 2026][research_omair_alhatim_2026]\] \[[Orme et al 1998][research_orme_1998]\] \[[Ormsbee 1977][research_ormsbee_1977]\] \[[Ormsbee et al 1977][research_ormsbee_siddiqi_1977]\] \[[Park et al 2018][research_park_2018]\] \[[Park et al 2023][research_park_2023]\] \[[Performance characteristics of two-blade propeller fans 1930][research_performance_characteristics_1930]\] \[[Perisho 1959][research_perisho_1959]\] \[[Perry et al 2021][research_perry_2021]\] \[[Perry et al 2023][research_perry_2023]\] \[[Petrovskii 1965][research_petrovskii_1965]\] \[[Phillips 2002][research_phillips_2002]\] \[[Picolet 1932][research_picolet_1932]\] \[[Pieper 1965][research_pieper_1965]\] \[[PlCKERELL and Cresswell 1968][research_plckerell_cresswell_1968]\] \[[Plunkett 1949][research_plunkett_1949]\] \[[Povinelli 2002][research_povinelli_2002]\] \[[Propeller Performance 2012][research_propeller_performance_2012]\] \[[Propeller Propulsion Systems 2010][research_propeller_propulsion_2010]\] \[[Propeller system for Bush Hawk utility aircraft 1999][research_propeller_system_1999]\] \[[Przedpelski 1965][research_przedpelski_1965]\] \[[Qin et al 2023][research_qin_2023]\] \[[Quillet et al 2023][research_quillet_2023]\] \[[Randall 1955][research_randall_1955]\] \[[Reader 1980][research_reader_1980]\] \[[Reuter 1939][research_reuter_1939]\] \[[Rezy et al 1979][research_rezy_stuckas_1979]\] \[[Roberts 1964][research_roberts_1964]\] \[[Rocket Effect in Standard Airplane Performance 1937][research_rocket_effect_1937]\] \[[Rodger Dyson][research_rodger_dyson]\] \[[Rogers and Fasciano 2016][research_rogers_fasciano_2016]\] \[[Rose and Jeracki 1989][research_rose_jeracki_1989]\] \[[Rostami 2024][research_rostami_2024]\] \[[Saari and Wallner 1946][research_saari_wallner_1946]\] \[[Saraçyakupoğlu et al 2022][research_saracyakupoglu_2022]\] \[[Sarup 2025][research_sarup_2025]\] \[[Sarup 2026][research_sarup_2026]\] \[[Satria Palar et al 2024][research_satria_palar_2024]\] \[[Scholz 2021][research_scholz_2021]\] \[[Schrenk 1932][research_schrenk_1932]\] \[[Schwartz et al 1986][research_schwartz_1986]\] \[[Scoppe 1973][research_scoppe_1973]\] \[[Shan et al 2025][research_shan_2025]\] \[[Shang et al 2025][research_shang_2025]\] \[[Shao et al 2025][research_shao_2025]\] \[[Shi et al 2024][research_shi_2024]\] \[[Showers 1952][research_showers_1952]\] \[[Siddavatam et al 2024][research_siddavatam_2024]\] \[[Simizu 1944][research_simizu_1944]\] \[[Simmonds 1967][research_simmonds_1967]\] \[[Simmonds 1967][research_simmonds_1967_2]\] \[[Simmonds 1967][research_simmonds_1967_3]\] \[[Simmons et al 2023][research_simmons_2023_3]\] \[[Sinacori and Lange 1961][research_sinacori_lange_1961]\] \[[Stresses in a rotating propeller blade 1938][research_stresses_in_1938]\] \[[Stuart 1943][research_stuart_1943]\] \[[Sziroczak et al 2020][research_sziroczak_2020]\] \[[Søntvedt 1974][research_sntvedt_1974]\] \[[Teixeira and Cesnik 2019][research_teixeira_cesnik_2019]\] \[[Theodorsen 1960][research_theodorsen_1960]\] \[[Theodorsen 1960][research_theodorsen_1960_2]\] \[[Theodorsen and Nomicos 1961][research_theodorsen_nomicos_1961]\] \[[Traub 2016][research_traub_2016]\] \[[Traub 2017][research_traub_2017]\] \[[Tucker 1999][research_tucker_1999]\] \[[Use of reinforced plastics in a composite propeller blade 1974][research_use_of_1974]\] \[[Usov et al 2026][research_usov_2026]\] \[[Valentine and Kader 1976][research_valentine_kader_1976]\] \[[Van et al 2019][research_van_2019]\] \[[Vance 1991][research_vance_1991]\] \[[Venkatesh et al 2025][research_venkatesh_2025]\] \[[Vepa 2018][research_vepa_2018]\] \[[Vepa 2020][research_vepa_2020]\] \[[Vlasov and Ovdienko 2020][research_vlasov_ovdienko_2020]\] \[[Vollo and Brassaw 1956][research_vollo_brassaw_1956]\] \[[Waddington et al 2023][research_waddington_2023]\] \[[Wallner and Sorin 1946][research_wallner_sorin_1946]\] \[[Walz 1976][research_walz_1976]\] \[[Walz 1978][research_walz_1978]\] \[[Wang et al 2026][research_wang_2026_3]\] \[[Webb and Willer 1952][research_webb_willer_1952]\] \[[Wells 1977][research_wells_1977]\] \[[Weng et al 2021][research_weng_2021]\] \[[Wheeler et al 2021][research_wheeler_2021]\] \[[Whitmore and Merrill 2012][research_whitmore_merrill_2012]\] \[[Worobel and Peracchio 1968][research_worobel_peracchio_1968]\] \[[Wu and Mora-Camino 2012][research_wu_moracamino_2012]\] \[[Wu et al 2023][research_wu_2023]\] \[[Xiao et al 2024][research_xiao_2024]\] \[[Xie and Haberland 1999][research_xie_haberland_1999]\] \[[Xie et al 2023][research_xie_2023_2]\] \[[Yang et al 2023][research_yang_2023]\] \[[Yildiz 2022][research_yildiz_2022]\] \[[Yost 1976][research_yost_1976]\] \[[Zabinsky and Laszewski 1956][research_zabinsky_laszewski_1956]\] \[[Zhang et al 2018][research_zhang_2018_2]\] \[[Zhang et al 2023][research_zhang_2023_3]\] \[[Zhao et al 2023][research_zhao_2023_2]\] \[[Zola et al 1978][research_zola_fishbach_1978]\]

### Propeller and rotor noise

Tone, broadband and interaction noise of propellers, rotors and fans, by theory, computation, wind tunnel and flight measurement.

**244 records.** \[[A. et al 2018][research_a_f_2018]\] \[[Afari and Mankbadi 2024][research_afari_mankbadi_2024]\] \[[Akila et al 2018][research_akila_marinus_2018]\] \[[Alì et al 2026][research_ali_2026]\] \[[Amargianitakis et al 2021][research_amargianitakis_2021]\] \[[Amiet 1988][research_amiet_1988]\] \[[Patterson et al][research_andrewpatterson_nairahovakimyan]\] \[[Arndt and Borgman 1971][research_arndt_borgman_1971]\] \[[Austin D. Thai et al][research_austin_d_thai]\] \[[Barton and Mixson 1981][research_barton_mixson_1981]\] \[[Berton and Nark 2019][research_berton_nark_2019]\] \[[Bewick et al 2001][research_bewick_adams_2001]\] \[[Bhardwaj et al 2026][research_bhardwaj_2026]\] \[[Block 1986][research_block_1986]\] \[[Block and Gentry 1986][research_block_gentry_1986]\] \[[Bonomo et al 2024][research_bonomo_2024]\] \[[Borchers 2009][research_borchers_2009]\] \[[Brooks and Mackall 1984][research_brooks_mackall_1984]\] \[[Brungart et al 2019][research_brungart_2019]\] \[[Bullmore et al 1990][research_bullmore_1990]\] \[[Byrd and Cates 1977][research_byrd_cates_1977]\] \[[Cantos et al 2026][research_cantos_2026]\] \[[Casagrande Hirono et al 2023][research_casagrande_hirono_2023]\] \[[Casalino et al 2021][research_casalino_2021]\] \[[Catherines and Mayes 1975][research_catherines_mayes_1975]\] \[[Chanaud 1972][research_chanaud_1972]\] \[[Chapman 1988][research_chapman_1988]\] \[[Charles E Feiler et al 1972][research_charles_e_feiler_1972]\] \[[Chen et al 2023][research_chen_2023]\] \[[Chusseau et al 2024][research_chusseau_biron_2024]\] \[[Chyla 2024][research_chyla_2024]\] \[[Corbishley et al 2026][research_corbishley_2026]\] \[[D.L. and M.V. 1974][research_d_l_m_v_1974]\] \[[Dahan et al 1980][research_dahan_avezard_1980]\] \[[Deming 1937][research_deming_1937]\] \[[Deming 1940][research_deming_1940]\] \[[Dittmar 1977][research_dittmar_1977]\] \[[Dittmar 1978][research_dittmar_1978]\] \[[Dittmar 1981][research_dittmar_1981]\] \[[Dittmar 1984][research_dittmar_1984]\] \[[Dittmar 1985][research_dittmar_1985]\] \[[Dittmar 1989][research_dittmar_1989]\] \[[Dittmar 1989][research_dittmar_1989_2]\] \[[Dittmar and Hall 1991][research_dittmar_hall_1991]\] \[[Dittmar and Jeracki 1981][research_dittmar_jeracki_1981]\] \[[Dittmar and Jeracki 1981][research_dittmar_jeracki_1981_b]\] \[[Dittmar and Stang 1987][research_dittmar_stang_1987_2]\] \[[Dittmar and Stang 1987][research_dittmar_stang_1987]\] \[[Dittmar and Stefko 1983][research_dittmar_stefko_1983_b]\] \[[Dittmar et al 1979][research_dittmar_jeracki_1979]\] \[[Dittmar et al 1982][research_dittmar_stefko_1982]\] \[[Dittmar et al 1983][research_dittmar_stefko_1983]\] \[[Dobrzynski 1993][research_dobrzynski_1993]\] \[[Domogalla et al 2026][research_domogalla_2026]\] \[[Hanson and Parzych 1993][research_donald_b_hanson_david_j_parzych_1993]\] \[[Dunn and Farassat 1990][research_dunn_farassat_1990]\] \[[Dunn and Farassat 1992][research_dunn_farassat_1992]\] \[[Dunn and Tarkenton 1989][research_dunn_tarkenton_1989]\] \[[Dunn et al 2015][research_dunn_2015]\] \[[Elliot et al 1990][research_elliot_1990]\] \[[Elliott et al 1989][research_elliott_1989]\] \[[Envia 1992][research_envia_1992]\] \[[Ernsthausen 1937][research_ernsthausen_1937]\] \[[Evans and Dunbar 1982][research_evans_dunbar_1982]\] \[[Eversman 1990][research_eversman_1990]\] \[[Farassat and Succi 1980][research_farassat_succi_1980]\] \[[Fink 1978][research_fink_1978]\] \[[Fruncillo et al 2024][research_fruncillo_luchini_2024]\] \[[Fruncillo et al 2025][research_fruncillo_luchini_2025]\] \[[Fuller and Jones 1987][research_fuller_jones_1987]\] \[[Gandhi et al 2022][research_gandhi_pepe_2022]\] \[[Gautam et al 2025][research_gautam_hanson_2025]\] \[[Gedney et al 1998][research_gedney_abbot_1998]\] \[[Glegg and Devenport 2024][research_glegg_devenport_2024]\] \[[Goyal et al 2024][research_goyal_2024]\] \[[Goyal et al 2025][research_goyal_2025]\] \[[Greenwood and Schmitz 2014][research_greenwood_schmitz_2014]\] \[[Guo and Thomas 2015][research_guo_thomas_2015]\] \[[Guérin et al 2023][research_guerin_2023]\] \[[Gwak and Lee 2017][research_gwak_lee_2017]\] \[[Halimi et al 2019][research_halimi_2019]\] \[[Hambrey et al 2017][research_hambrey_feszty_2017]\] \[[Hanson 1976][research_hanson_1976]\] \[[Hanson 1983][research_hanson_1983]\] \[[Hanson 1985][research_hanson_1985]\] \[[Hanson 1986][research_hanson_1986]\] \[[Hanson and Fink 1978][research_hanson_fink_1978]\] \[[Hanson and Fink 1979][research_hanson_fink_1979]\] \[[Hanson and Magliozzi 1985][research_hanson_magliozzi_1985]\] \[[Hanson et al 2023][research_hanson_2023]\] \[[Hasegawa and Sakaue 2023][research_hasegawa_sakaue_2023]\] \[[Hasegawa and Sakaue 2024][research_hasegawa_sakaue_2024]\] \[[Healy 1969][research_healy_1969]\] \[[Hodgson and Guo 2006][research_hodgson_guo_2006]\] \[[Huang et al 2016][research_huang_ghorbaniasl_2016]\] \[[Huang et al 2020][research_huang_yao_2020]\] \[[Huang et al 2023][research_huang_2023]\] \[[Huang et al 2025][research_huang_2025]\] \[[Iemma et al 2021][research_iemma_2021]\] \[[Ingraham 2023][research_ingraham_2023]\] \[[Ingraham et al 2019][research_ingraham_gray_2019]\] \[[Içke and Baysal 2021][research_icke_baysal_2021]\] \[[Jeong et al 2023][research_jeong_2023]\] \[[Jia and Lee 2022][research_jia_lee_2022]\] \[[Johnston and Donham 1982][research_johnston_donham_1982]\] \[[Jung et al 2025][research_jung_2025]\] \[[Kallergis 1987][research_kallergis_1987]\] \[[Karimian et al 2023][research_karimian_paruchuri_2023]\] \[[Karimian et al 2023][research_karimian_paruchuri_2023_b]\] \[[Kato et al 2018][research_kato_2018]\] \[[Keshavan 1980][research_keshavan_1980]\] \[[Kim et al 2025][research_kim_2025_3]\] \[[Kingan and Parry 2020][research_kingan_parry_2020]\] \[[Kingan and Self 2009][research_kingan_self_2009]\] \[[Kordan et al 1985][research_kordan_vonlavante_1985]\] \[[Kotwicz Herniczek][research_kotwiczherniczek]\] \[[Lee et al 2025][research_lee_2025]\] \[[Lester and Fuller 1986][research_lester_fuller_1986]\] \[[Leth et al 1998][research_leth_samuelsson_1998]\] \[[Li et al 2023][research_li_2023_2]\] \[[Light aircraft propeller - Design parameter effects on 1993][research_light_aircraft_1993]\] \[[Loewy and Sutton 1966][research_loewy_sutton_1966]\] \[[Løvik and Holden 2024][research_lvik_holden_2024]\] \[[Ma and Guo 2018][research_ma_guo_2018]\] \[[Maglieri and Hubbard 1975][research_maglieri_hubbard_1975]\] \[[Magliozzi 1982][research_magliozzi_1982]\] \[[Magliozzi 1983][research_magliozzi_1983]\] \[[Malgoezar et al 2019][research_malgoezar_2019]\] \[[Marinus et al 2009][research_marinus_roger_2009]\] \[[Marques et al 2026][research_marques_2026]\] \[[McCurdy 1985][research_mccurdy_1985]\] \[[McCurdy 1989][research_mccurdy_1989]\] \[[McCurdy 1991][research_mccurdy_1991]\] \[[McCurdy and Powell 1984][research_mccurdy_powell_1984]\] \[[McKay and Kingan 2019][research_mckay_kingan_2019]\] \[[Merino-Martinez and Nicola Quaroni 2025][research_merino_martinez_nicola_quaroni_2025]\] \[[Metzger 1981][research_metzger_1981]\] \[[Metzger and Farassat 2007][research_metzger_farassat_2007]\] \[[Metzger et al 1976][research_metzger_1976]\] \[[Metzger et al 1980][research_metzger_menthe_1980]\] \[[Miller et al 1982][research_miller_1982]\] \[[Misol 2020][research_misol_2020]\] \[[Mixson and Powell 1984][research_mixson_powell_1984]\] \[[Mixson and Powell 1985][research_mixson_powell_1985]\] \[[Mixson et al 1979][research_mixson_barton_1979]\] \[[Mixson et al 1981][research_mixson_greene_1981]\] \[[Morhy Cavalcante et al 2026][research_morhy_cavalcante_2026]\] \[[Moshkov 2022][research_moshkov_2022]\] \[[Moshkov 2026][research_moshkov_2026_c]\] \[[Moshkov 2026][research_moshkov_2026]\] \[[Moshkov 2026][research_moshkov_2026_b]\] \[[Moshkov and Samokhin 2016][research_moshkov_samokhin_2016]\] \[[Moshkov and Samokhin 2021][research_moshkov_samokhin_2021]\] \[[Moshkov and Yakovlev 2023][research_moshkov_yakovlev_2023]\] \[[Moshkov et al 2019][research_moshkov_2019]\] \[[Nallasamy et al 1987][research_nallasamy_clark_1987]\] \[[Nallasamy et al 1989][research_nallasamy_1989]\] \[[Nark et al 2004][research_nark_2004]\] \[[Nark et al 2017][research_nark_2017]\] \[[Zawodny et al 2025][research_nikolas_s_zawodny_2025]\] \[[Noda et al 2022][research_noda_2022]\] \[[Noda et al 2025][research_noda_2025]\] \[[Oleson and Patrick 1998][research_oleson_patrick_1998]\] \[[Optimization software helps design low-noise rotorcraft 2000][research_optimization_software_2000]\] \[[Palchikovskiy et al 2023][research_palchikovskiy_2023]\] \[[Palleja-Cabre et al 2024][research_pallejacabre_macey_2024]\] \[[Park 2026][research_park_2026_b]\] \[[Parry 1995][research_parry_1995]\] \[[Parry and Crighton 1989][research_parry_crighton_1989]\] \[[Pascioni et al 2026][research_pascioni_2026]\] \[[Paswan et al 2025][research_paswan_2025]\] \[[Patrick 1986][research_patrick_1986]\] \[[Patrick and Nagel 1989][research_patrick_nagel_1989]\] \[[Pereira Gouveia da Silva et al 2025][research_pereira_gouveia_da_silva_2025]\] \[[Peterson and Warmbrodt 1996][research_peterson_warmbrodt_1996]\] \[[Pla et al 1989][research_pla_1989]\] \[[Pogosyan and Moshkov 2023][research_pogosyan_moshkov_2023]\] \[[Polacsek et al 2000][research_polacsek_spiegel_2000]\] \[[Pope et al 1987][research_pope_1987]\] \[[Pope et al 1987][research_pope_1987_2]\] \[[Qin and Huang 2024][research_qin_huang_2024]\] \[[Quaroni et al 2024][research_quaroni_merinomartinez_2024]\] \[[Ragani Lamouki et al 2026][research_ragani_lamouki_2026]\] \[[Raisbeck and Mills 1987][research_raisbeck_mills_1987]\] \[[Rathgeber and Sipes 1977][research_rathgeber_sipes_1977]\] \[[Reduced Noise in Interiors of Propfan Aircraft 1988][research_reduced_noise_1988]\] \[[Regier and Hubbard 1953][research_regier_hubbard_1953]\] \[[Rennison et al 1980][research_rennison_wilby_1980]\] \[[Revell et al 1980][research_revell_balena_1980]\] \[[Revell et al 1980][research_revell_balena_1980_b]\] \[[Revell et al 1982][research_revell_1982_2]\] \[[Revell et al 1982][research_revell_1982]\] \[[Roger et al 2022][research_roger_2022]\] \[[Ruijgrok 1980][research_ruijgrok_1980]\] \[[Runyan 1980][research_runyan_1980]\] \[[Ruotolo 1999][research_ruotolo_1999]\] \[[Madhusudhana et al 2024][research_s_v_madhusudhana_2024]\] \[[Salikuddin and Ahuja 1989][research_salikuddin_ahuja_1989]\] \[[Salikuddin et al 1990][research_salikuddin_1990]\] \[[Santos et al 2023][research_santos_2023]\] \[[Sasaki et al 2012][research_sasaki_torise_2012]\] \[[Schaeffer and Sternfeld 1978][research_schaeffer_sternfeld_1978]\] \[[Shao et al 2026][research_shao_2026]\] \[[Shreve 1977][research_shreve_1977]\] \[[Simon et al 2023][research_simon_2023]\] \[[Spencer et al 1969][research_spencer_1969]\] \[[Sree 2015][research_sree_2015]\] \[[Stabeli Diehl et al 2025][research_stabeli_diehl_2025]\] \[[Succi 1981][research_succi_1981]\] \[[Succi et al 1983][research_succi_1983]\] \[[Sun et al 2023][research_sun_2023_2]\] \[[Timushev et al 2021][research_timushev_yakovlev_2021]\] \[[Trascinelli et al 2026][research_trascinelli_2026]\] \[[Trillo 1966][research_trillo_1966]\] \[[Tsouka 2024][research_tsouka_2024]\] \[[Unruh 1987][research_unruh_1987]\] \[[Unruh 1988][research_unruh_1988]\] \[[Unruh 1988][research_unruh_1988_b]\] \[[Unruh 1989][research_unruh_1989]\] \[[van Deventer 1979][research_vandeventer_1979]\] \[[Van Treuren and Wisniewski 2019][research_vantreuren_wisniewski_2019]\] \[[Wang and Zhong 2025][research_wang_zhong_2025]\] \[[Wang et al 2024][research_wang_2024_6]\] \[[Widnall and Wolf 1980][research_widnall_wolf_1980]\] \[[Wilby and Wilby 1989][research_wilby_wilby_1989]\] \[[Wilby et al 1980][research_wilby_rennison_1980]\] \[[Woan and Gregorek 1978][research_woan_gregorek_1978]\] \[[Woodward 1987][research_woodward_1987_b]\] \[[Woodward 1987][research_woodward_1987]\] \[[Woodward and Loeffler 1991][research_woodward_loeffler_1991]\] \[[Wright and Lee 1984][research_wright_lee_1984]\] \[[Wu et al 2023][research_wu_2023_2]\] \[[Xue et al 2023][research_xue_2023]\] \[[Yang et al 2017][research_yang_2017]\] \[[Yang et al 2026][research_yang_meinke_2026]\] \[[Yin and Stuermer 2013][research_yin_stuermer_2013]\] \[[Yuen 2026][research_yuen_2026]\] \[[Zaman et al 2024][research_zaman_2024]\] \[[Zhang et al 2023][research_zhang_2023_4]\] \[[Zheng et al 2023][research_zheng_2023]\] \[[Zhi et al 2025][research_zhi_2025]\] \[[Zhong et al 2023][research_zhong_2023]\] \[[Çelebi et al 2025][research_celebi_2025]\] \[[Šulc et al 1982][research_sulc_1982]\]

### Aircraft noise sources, measurement, prediction and reduction

Aircraft noise in general, its measurement, monitoring, prediction tools and reduction programmes, where a title names no single source.

**243 records.** \[[A review of the aircraft noise problem 2011][research_a_review_2011]\] \[[Acoustic field separation with 2-layer microphone array 2023][research_acoustic_field_2023]\] \[[Action against aircraft noise 1989][research_action_against_1989]\] \[[Aircraft Flyover Noise Measurements 1976][research_aircraft_flyover_1976]\] \[[Aircraft Noise Assessment 1980][research_aircraft_noise_1980]\] \[[Aircraft Noise Flight Trajectories 2012][research_aircraft_noise_2012_b]\] \[[Aircraft Noise No Quiet in London 1969][research_aircraft_noise_1969]\] \[[Aircraft Noise Noise Sources 2012][research_aircraft_noise_2012]\] \[[Aircraft noise prediction 1989][research_aircraft_noise_1989]\] \[[Aircraft noise sources 1989][research_aircraft_noise_1989_b]\] \[[Akatsuka 2024][research_akatsuka_2024]\] \[[Ali 1989][research_ali_1989]\] \[[Allanach et al 2010][research_allanach_2010]\] \[[An Algorithm for Microphone Array Sparse Arrangement and Acoustic Imaging 2026][research_an_algorithm_2026]\] \[[An et al 2025][research_an_2025]\] \[[Ang and Cui 2022][research_ang_cui_2022]\] \[[Arcondoulis and Liu 2019][research_arcondoulis_liu_2019]\] \[[Asakura and Takagi 2020][research_asakura_takagi_2020]\] \[[Aujogue][research_aujogue]\] \[[Avallone et al 2018][research_avallone_2018]\] \[[Badgley and Laskin 1970][research_badgley_laskin_1970]\] \[[Barlow et al 1972][research_barlow_mccluskey_1972]\] \[[Barstow 1940][research_barstow_1940]\] \[[Barstow 1941][research_barstow_1941]\] \[[Berry and Harris 2024][research_berry_harris_2024]\] \[[Berry and Speakman 1993][research_berry_speakman_1993]\] \[[Bertsch et al 2010][research_bertsch_dobrzynski_2010]\] \[[Bertsch et al 2019][research_bertsch_2019]\] \[[Bertsch et al 2023][research_bertsch_pottpollenske_2023]\] \[[Bohn and Shovlin 1981][research_bohn_shovlin_1981]\] \[[Bossler and Smith 1974][research_bossler_smith_1974]\] \[[Boston et al 1984][research_boston_1984]\] \[[Bowles et al 1974][research_bowles_1974]\] \[[Brear et al 2003][research_brear_kerrebrock_2003]\] \[[Brown et al 1969][research_brown_cox_1969]\] \[[Brusniak et al 2019][research_brusniak_2019]\] \[[Bryson et al 2016][research_bryson_2016]\] \[[Bui et al 2021][research_bui_2021]\] \[[Caillet et al 2026][research_caillet_2026]\] \[[Campanella 1976][research_campanella_1976]\] \[[Certified Aircraft Noise Data 2012][research_certified_aircraft_2012]\] \[[Charly Kone et al 2025][research_charly_kone_2025]\] \[[Cheeseman 1975][research_cheeseman_1975]\] \[[Chen et al 2015][research_chen_2015_2]\] \[[Chen et al 2021][research_chen_2021_2]\] \[[Chopra 2002][research_chopra_2002]\] \[[Ciaburro et al 2020][research_ciaburro_2020]\] \[[Clark 1981][research_clark_1981]\] \[[Cochrane and Boissevain 1978][research_cochrane_boissevain_1978]\] \[[Cochrane and Carros 1975][research_cochrane_carros_1975]\] \[[Cochrane et al 1981][research_cochrane_riddle_1981]\] \[[Cochrane et al 1982][research_cochrane_riddle_1982]\] \[[Coen and Richwine 2017][research_coen_richwine_2017]\] \[[Cole and England 1967][research_cole_england_1967]\] \[[Conners et al 2005][research_conners_howe_2005]\] \[[Connor et al 1975][research_connor_hilton_1975]\] \[[Cross 1984][research_cross_1984]\] \[[Cross and Watts 1983][research_cross_watts_1983]\] \[[Culver 2016][research_culver_2016]\] \[[Cuppoletti et al 2024][research_cuppoletti_2024]\] \[[Development of a New Computer System for Aircraft Noise 1976][research_development_of_1976]\] \[[Dittmar 1983][research_dittmar_1983]\] \[[Dolmans and Patrick 1998][research_dolmans_patrick_1998]\] \[[Domogalla et al 2021][research_domogalla_bertsch_2021]\] \[[Durbin 1983][research_durbin_1983]\] \[[Eisenhut and Strohmayer 2026][research_eisenhut_strohmayer_2026]\] \[[Envia 2018][research_envia_2018]\] \[[Eppel 1981][research_eppel_1981]\] \[[Ffowcs Williams and Hawkings 1969][research_ffowcs_williams_hawkings_1969]\] \[[Fidell et al 1989][research_fidell_1989_2]\] \[[Fleming 1954][research_fleming_1954]\] \[[Ford 1990][research_ford_1990]\] \[[Ford CEng MRAeS 1992][research_fordcengmraes_1992]\] \[[Frampton et al 1993][research_frampton_1993]\] \[[Friedlander et al 2018][research_friedlander_2018]\] \[[Fujita et al 2021][research_fujita_2021]\] \[[Gasaway 1969][research_gasaway_1969]\] \[[Gasaway and Hatfield 1963][research_gasaway_hatfield_1963]\] \[[Geiger 2002][research_geiger_2002]\] \[[Gennaretti et al 2017][research_gennaretti_2017]\] \[[Gibbs 2023][research_gibbs_2023]\] \[[Griffith 1971][research_griffith_1971]\] \[[Griffith and Roberts 1972][research_griffith_roberts_1972]\] \[[Santos et al 2025][research_h_t_santos_2025]\] \[[Hai et al 2025][research_hai_2025]\] \[[Hargest 1966][research_hargest_1966]\] \[[Harlamert 1974][research_harlamert_1974]\] \[[Henke et al 2010][research_henke_lammering_2010]\] \[[Hille et al 2023][research_hille_stumpf_2023]\] \[[Hilton and Henderson 1978][research_hilton_henderson_1978]\] \[[Hilton et al 1975][research_hilton_1975]\] \[[Hilton et al 1975][research_hilton_1975_2]\] \[[Hilton et al 1975][research_hilton_connor_1975_b]\] \[[Homans et al 1978][research_homans_1978]\] \[[Hosier 1977][research_hosier_1977]\] \[[Howard 1977][research_howard_1977]\] \[[Hubbard 1993][research_hubbard_1993]\] \[[Human reaction to aircraft noise 1989][research_human_reaction_1989]\] \[[Humpert et al 2015][research_humpert_gaeta_2015]\] \[[Hübner and Strümpfel 2020][research_hubner_strumpfel_2020]\] \[[Ingram 1964][research_ingram_1964]\] \[[Izquierdo et al 2017][research_izquierdo_2017]\] \[[Fowler et al][research_jennifer_fowler]\] \[[Johansson 2023][research_johansson_2023]\] \[[Jones 1946][research_jones_1946]\] \[[Ju et al 2026][research_ju_2026]\] \[[Jäger et al 2021][research_jager_2021]\] \[[Kayser et al 2024][research_kayser_2024]\] \[[Kelly 1993][research_kelly_1993]\] \[[Kelly and Wilson 1995][research_kelly_wilson_1995]\] \[[Kim et al 2025][research_kim_2025_4]\] \[[Knowd 1982][research_knowd_1982]\] \[[Ko et al 2026][research_ko_2026]\] \[[Komadina et al 2002][research_komadina_drake_2002]\] \[[Kone et al 2024][research_kone_ghinet_2024_b]\] \[[Koopmann 1976][research_koopmann_1976]\] \[[Kourbatski 2024][research_kourbatski_2024]\] \[[Kozupa et al 2023][research_kozupa_2023]\] \[[Krivosheikin and Perelygin 2015][research_krivosheikin_perelygin_2015]\] \[[Kryter and Williams 1966][research_kryter_williams_1966]\] \[[Kukreja 2008][research_kukreja_2008]\] \[[Kurbjun 1959][research_kurbjun_1959]\] \[[Large 1975][research_large_1975]\] \[[Lee and Motsinger 1975][research_lee_motsinger_1975]\] \[[Legriffon et al 2023][research_legriffon_bertsch_2023]\] \[[Lennart S Hultgren et al 2020][research_lennart_s_hultgren_2020]\] \[[Li 1981][research_li_1981]\] \[[Li et al 2020][research_li_2020]\] \[[Lilley 2004][research_lilley_2004]\] \[[Lilley 2006][research_lilley_2006]\] \[[Lincke and Pieren 2024][research_lincke_pieren_2024_2]\] \[[Little and Russell 1976][research_little_russell_1976]\] \[[Mahak et al 2017][research_mahak_2017]\] \[[Maniet 2001][research_maniet_jr_2001]\] \[[Maria Thoma et al 2024][research_maria_thoma_2024]\] \[[Matouk 2024][research_matouk_2024]\] \[[Casanova et al 2025][research_matthias_casanova_2025]\] \[[McCracken 1979][research_mccracken_1979]\] \[[Khorrami et al][research_mehdi_r_khorrami]\] \[[Melton 1985][research_melton_1985]\] \[[Mengle et al 2006][research_mengle_ganz_2006]\] \[[Methods for aircraft noise prediction 2011][research_methods_for_2011]\] \[[Metzger 1973][research_metzger_1973]\] \[[Metzger and Worobel 1973][research_metzger_worobel_1973]\] \[[Miguel 1974][research_miguel_1974]\] \[[Miller and Eagan 1997][research_miller_eagan_1997]\] \[[Miller and Eagan 1997][research_miller_eagan_1997_b]\] \[[Miller and Eagan 1998][research_miller_eagan_1998]\] \[[Monitoring of aircraft noise† 2011][research_monitoring_of_2011]\] \[[Morinaga et al 2021][research_morinaga_2021]\] \[[Moses and Zeitlin 1975][research_moses_zeitlin_1975]\] \[[Muller 1971][research_muller_1971]\] \[[Munro and Ahuja 2003][research_munro_ahuja_2003]\] \[[Nishinomiya et al 1978][research_nishinomiya_1978]\] \[[Nnonyelu 2020][research_nnonyelu_2020]\] \[[Nnonyelu 2021][research_nnonyelu_2021]\] \[[Novak 1970][research_novak_1970]\] \[[Okada 1994][research_okada_1994]\] \[[Ollerhead 1982][research_ollerhead_1982]\] \[[Olson et al 2004][research_olson_hill_2004]\] \[[Liem 2018][research_pliem_2018]\] \[[Panel Discussion Aircraft Noise Prediction 1976][research_panel_discussion_1976]\] \[[Papamoschou and Debiasi 2003][research_papamoschou_debiasi_2003]\] \[[Park et al 2026][research_park_2026]\] \[[Paterson et al 1973][research_paterson_1973]\] \[[Peart 1991][research_peart_1991]\] \[[Pegg et al 1974][research_pegg_1974]\] \[[Peng et al 2026][research_peng_2026]\] \[[Peterse 2024][research_peterse_2024]\] \[[Pinker 2024][research_pinker_2024]\] \[[Plucinsky 1973][research_plucinsky_1973]\] \[[Posey 2008][research_posey_2008]\] \[[Pott-Pollenske 2021][research_pottpollenske_2021]\] \[[Qian 2026][research_qian_2026]\] \[[Queen and Cochrane 1982][research_queen_cochrane_1982]\] \[[Raney 1975][research_raney_1975]\] \[[Rasband et al 2023][research_rasband_2023]\] \[[Raza and Stansbury 2025][research_raza_stansbury_2025]\] \[[Riddle et al 1981][research_riddle_innis_1981]\] \[[Riddle et al 1987][research_riddle_stevens_1987]\] \[[Rogers and Cook 1952][research_rogers_cook_1952]\] \[[Roxner and Postolsky 2024][research_roxner_postolsky_2024]\] \[[Rusciano and Viscardi 2008][research_rusciano_viscardi_2008]\] \[[Sakaliyski et al 2007][research_sakaliyski_hileman_2007]\] \[[Salikuddin 1990][research_salikuddin_1990_2]\] \[[Sankar and Brentner 2008][research_sankar_brentner_2008]\] \[[Schairer et al 1971][research_schairer_1971]\] \[[Schlinker 1979][research_schlinker_1979]\] \[[Schwab and Zellmann 2020][research_schwab_zellmann_2020]\] \[[Segall and Gardner 2026][research_segall_gardner_2026]\] \[[Shahady 1975][research_shahady_1975]\] \[[Shapiro and Sherman Edwards 1967][research_shapiro_sherman_edwards_1967]\] \[[Shovlin et al 1979][research_shovlin_1979]\] \[[Simson 2024][research_simson_2024]\] \[[Soderman 2006][research_soderman_2006]\] \[[Soderman and Noble 1975][research_soderman_noble_1975]\] \[[Source Noise Suppression of Subsonic Tip Speed Fans 1975][research_source_noise_1975]\] \[[Stephenson et al 1990][research_stephenson_1990]\] \[[Stephenson et al 2019][research_stephenson_2019]\] \[[Stoll et al 2013][research_stoll_stilson_2013]\] \[[Su et al 2025][research_su_2025]\] \[[Sunago et al 2009][research_sunago_sasaki_2009]\] \[[Svane and Plovsing 2024][research_svane_plovsing_2024]\] \[[Swearingen 2006][research_swearingen_2006]\] \[[Takaishi et al 2023][research_takaishi_2023]\] \[[Takaishi et al 2024][research_takaishi_2024]\] \[[Tam 2015][research_tam_2015]\] \[[Terashima et al 2021][research_terashima_2021]\] \[[The inﬂuence of operational factors on aircraft noise levels 2011][research_the_influence_2011]\] \[[The main sources of aircraft noise 2011][research_the_main_2011]\] \[[Thorpe 1970][research_thorpe_1970]\] \[[Torija Martinez et al 2023][research_torija_martinez_2023]\] \[[Tracy et al 2002][research_tracy_sturdza_2002]\] \[[Trethewey 1988][research_trethewey_1988]\] \[[Tsutsumino et al 2025][research_tsutsumino_2025]\] \[[Tweeddale 1941][research_tweeddale_1941]\] \[[Typical aircraft noise levels 1989][research_typical_aircraft_1989]\] \[[Unruh 1980][research_unruh_1980]\] \[[Wang and Antesberger 2024][research_wang_antesberger_2024]\] \[[Wang and Crocker 1983][research_wang_crocker_1983]\] \[[Wang and Qin 2024][research_wang_qin_2024]\] \[[Wang et al 2022][research_wang_qin_2022]\] \[[Wang et al 2023][research_wang_2023_3]\] \[[Weston et al 2024][research_weston_2024]\] \[[Wilkerson 1975][research_wilkerson_1975]\] \[[Patterson et al][research_william_c_patterson]\] \[[Williams 1974][research_williams_1974]\] \[[Willis and Daniels 1981][research_willis_daniels_1981]\] \[[Willshire 1983][research_willshire_1983]\] \[[Wilson 2025][research_wilson_2025]\] \[[Wilson Committee Report on Noise 1963][research_wilson_committee_1963]\] \[[Xiang and Jiang 2015][research_xiang_jiang_2015]\] \[[Xie et al 2024][research_xie_2024]\] \[[Xu et al 2025][research_xu_2025]\] \[[Yeong et al 2009][research_yeong_chiles_2009]\] \[[Yunus et al 2023][research_yunus_2023]\] \[[Zaporozhets and Jagniatinskis 2021][research_zaporozhets_jagniatinskis_2021]\] \[[Zellmann et al 2018][research_zellmann_2018]\] \[[Zhang et al 2023][research_zhang_2023_7]\] \[[Zhong et al 2019][research_zhong_2019]\] \[[Zorumski 1977][research_zorumski_1977]\] \[[Драмшини 2022, Development of Algorithms of the][research__2022]\] \[[Тsekhmistro and Shapovalov 2023][research_sekhmistro_shapovalov_2023]\]

### Performance, power required, endurance and range

Aircraft performance, power required, endurance, range, glide and sink rate, drag and fuel consumption.

**232 records.** \[[11. Aircraft Range and Endurance in Steady Flight 2011][research_aircraft_range_2011]\] \[[A Method of Comparing Performance 1936][research_a_method_1936]\] \[[Abu Salem et al 2023][research_abu_salem_2023]\] \[[Ahearn et al 1965][research_ahearn_headrick_1965]\] \[[Ahmed et al 2024][research_ahmed_2024_2]\] \[[Air Force Test Pilot School Edwards Afb Ca 1962][research_airforcetestpilotschooledwardsafbca_1962]\] \[[Air Force Test Pilot School Edwards Afb Ca 1962][research_airforcetestpilotschooledwardsafbca_1962_b]\] \[[Air Force Test Pilot School Edwards Afb Ca 1967][research_airforcetestpilotschooledwardsafbca_1967]\] \[[Air Force Test Pilot School Edwards Afb Ca 1967][research_airforcetestpilotschooledwardsafbca_1967_b]\] \[[Air Force Test Pilot School Edwards Afb Ca 1979][research_air_force_test_pilot_school_edwards_afb_ca_1979]\] \[[Air Force Test Pilot School Edwards Afb Ca 1987][research_air_force_test_pilot_school_edwards_afb_ca_1987]\] \[[Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991]\] \[[Air Force Test Pilot School Edwards Afb Ca 1992][research_airforcetestpilotschooledwardsafbca_1992]\] \[[Air Force Test Pilot School Edwards Afb Ca 1994][research_air_force_test_pilot_school_edwards_afb_ca_1994]\] \[[Aircraft performance monitoring from flight data 2015][research_aircraft_performance_2015]\] \[[Appa and Ausman 1997][research_appa_ausman_1997]\] \[[Appa et al 1998][research_appa_1998]\] \[[Arum et al 2020][research_arum_2020]\] \[[Ashkenas and Klyde 1989][research_ashkenas_klyde_1989]\] \[[Bakar et al 2021][research_bakar_2021]\] \[[Baldwin 1973][research_baldwin_1973_b]\] \[[Barde et al 2022][research_barde_birzare_2022]\] \[[Barman and Erzberger 1976][research_barman_erzberger_1976]\] \[[Beck et al 2018][research_beck_2018]\] \[[Bergman 1976][research_bergman_1976]\] \[[Berkowitz 1950][research_berkowitz_1950]\] \[[Bert 1981][research_bert_1981]\] \[[Bhandari et al 2026][research_bhandari_2026]\] \[[Bhatia 2019][research_bhatia_2019]\] \[[Blake 2002][research_blake_2002]\] \[[Bonnin and Hoogreef 2025][research_bonnin_hoogreef_2025]\] \[[Botros et al 2018][research_botros_walker_2018]\] \[[Bray et al 1960][research_bray_1960]\] \[[Bull and Bridges 1985][research_bull_bridges_1985]\] \[[Burton and Hoburg 2018][research_burton_hoburg_2018]\] \[[Cao 2026][research_cao_2026]\] \[[Cao et al 2023][research_cao_2023_2]\] \[[Chang and Hung 2021][research_chang_hung_2021]\] \[[Chu et al 2021][research_chu_2021]\] \[[Chung et al 1993][research_chung_1993]\] \[[Clarke and Merson 1979][research_clarke_merson_1979]\] \[[Cleek et al 1978][research_cleek_jr_1978]\] \[[Cleek et al 1978][research_cleek_jr_1978_b]\] \[[Cleek et al 1978][research_cleek_jr_1978_c]\] \[[Cleek et al 1979][research_cleek_nathanh_1979]\] \[[Cleek et al 1979][research_cleek_nathanh_1979_b]\] \[[Cleek et al 1979][research_cleek_nathanh_1979_c]\] \[[Cleek et al 1979][research_cleek_nathanh_1979_d]\] \[[Cleek et al 1979][research_cleek_nathanh_1979_e]\] \[[Connelly 1982][research_connelly_1982]\] \[[Deal et al 2024][research_deal_2024]\] \[[Deuschle et al 2024][research_deuschle_2024]\] \[[Dodbele et al 1987][research_dodbele_1987]\] \[[Dunlap and Porter 1971][research_dunlap_porter_1971]\] \[[Ellis 1971][research_ellis_1971]\] \[[Fakhraian et al 2023][research_fakhraian_2023]\] \[[Fay and Johnstone 1960][research_fay_johnstone_1960]\] \[[Figliola 2005][research_figliola_2005]\] \[[Finnestead and Antoniou 1965][research_finnestead_antoniou_1965]\] \[[Finnestead et al 1970][research_finnestead_connor_1970]\] \[[Fischer 2006][research_fischer_2006]\] \[[Fladeland et al 2019][research_fladeland_2019]\] \[[Flight Test Data Analysis of Hybrid Vertical Take-off and Landing Unmanned Aerial Vehicle 2016][research_flight_test_2016]\] \[[Foch and Ailinger 1992][research_foch_ailinger_1992]\] \[[Rodriguez et al][research_gabino_martinez_rodriguez]\] \[[Gang and Kwon 2018][research_gang_kwon_2018]\] \[[Gao 2023][research_gao_2023]\] \[[Garfinkel 1951][research_garfinkel_1951]\] \[[Gatti et al 2015][research_gatti_giulietti_2015]\] \[[Geuther and Capristan 2020][research_geuther_capristan_2020]\] \[[Godwin et al 1964][research_godwin_frazier_1964]\] \[[Goncharenko 2022][research_goncharenko_2022]\] \[[Graham and Rodriquez 1951][research_graham_rodriquez_1951]\] \[[Grendysa 2019][research_grendysa_2019]\] \[[Gyorgyfalvy 1965][research_gyorgyfalvy_1965]\] \[[Haefner et al 2026][research_haefner_2026]\] \[[Haftka et al 1987][research_haftka_grossman_1987]\] \[[Haider 2024][research_haider_2024]\] \[[Hall 1961][research_hall_1961]\] \[[Hall and Rogan 1988][research_hall_rogan_1988]\] \[[Hall and Rogan 1989][research_hall_rogan_1989]\] \[[Hayes 1945][research_hayes_1945]\] \[[Hebert et al 1973][research_hebert_1973]\] \[[Hedrick and Nichols 1975][research_hedrick_nichols_1975]\] \[[Hoerner 1936][research_hoerner_1936]\] \[[Hosseini and Mesbahi 2016][research_hosseini_mesbahi_2016]\] \[[Hunter 1959][research_hunter_1959]\] \[[Hwang et al 2016][research_hwang_2016]\] \[[Hwang et al 2016][research_hwang_2016_2]\] \[[Jentys and Breitsamter 2023][research_jentys_breitsamter_2023]\] \[[Jeong et al 2022][research_jeong_2022]\] \[[Jin 2024][research_jin_2024]\] \[[Jin and Lee 2015][research_jin_lee_2015]\] \[[Jobe 1984][research_jobe_1984]\] \[[Johnson 1972][research_johnson_1972_2]\] \[[Joo and Hwang 2017][research_joo_hwang_2017]\] \[[Kai 2024][research_kai_2024]\] \[[Kaptsov and Rodrigues 2018][research_kaptsov_rodrigues_2018]\] \[[Katz 2017][research_katz_2017]\] \[[Keenohan 1942][research_keenohan_1942]\] \[[Keskin 2026][research_keskin_2026]\] \[[Kim et al 2022][research_kim_2022_3]\] \[[Kim et al 2022][research_kim_2022_4]\] \[[Korsun et al 2018][research_korsun_2018]\] \[[Kraft 1985][research_kraft_1985]\] \[[Kumar et al 2025][research_kumar_2025]\] \[[Kutney and Piszkin 1964][research_kutney_piszkin_1964]\] \[[Laine 1982][research_laine_1982]\] \[[Laitone 1994][research_laitone_1994]\] \[[Lapygin and Tretyakov 1986][research_lapygin_tret_yakov_1986]\] \[[Lei and Liu 2019][research_lei_liu_2019]\] \[[Leng][research_leng]\] \[[Letica and Rizzi 2024][research_letica_rizzi_2024]\] \[[Li and Qi 2022][research_li_qi_2022]\] \[[Li and Rodrigues 2025][research_li_rodrigues_2025]\] \[[Linnell 1963][research_linnell_1963]\] \[[Liu and Stumpf 2018][research_liu_stumpf_2018]\] \[[Lobanovskii 1983][research_lobanovskii_1983]\] \[[Luqmanul Hakim et al 2018][research_luqmanul_hakim_2018]\] \[[Lush 1950][research_lush_1950]\] \[[Luskin 1950][research_luskin_1950]\] \[[Lyu and Liem 2020][research_lyu_liem_2020]\] \[[Maikapar 1966][research_maikapar_1966]\] \[[Mastroddi et al 2018][research_mastroddi_2018]\] \[[Matranga and Armstrong 1959][research_matranga_armstrong_1959]\] \[[McDonnell and Ning 2020][research_mcdonnell_ning_2020]\] \[[Meckstroth and Ordóñez 2020][research_meckstroth_ordonez_2020]\] \[[Mentzer and Nourse 1940][research_mentzer_nourse_1940]\] \[[Mihalik and Keane 2022][research_mihalik_keane_2022]\] \[[Miller 1942][research_miller_1942]\] \[[Miller and Koch 1985][research_miller_koch_1985]\] \[[Mockelman et al 2026][research_mockelman_crane_2026]\] \[[Moelyadi et al 2021][research_moelyadi_2021]\] \[[Mrusek 2021][research_mrusek_2021]\] \[[Newell et al 1963][research_newell_1963]\] \[[Newsom and Tosti 1959][research_newsom_tosti_1959]\] \[[Nicolaides and Tragarz 1971][research_nicolaides_tragarz_1971]\] \[[Nikhade et al 2023][research_nikhade_barde_2023]\] \[[Ogburn et al 1994][research_ogburn_1994]\] \[[Ordonez 2003][research_ordonez_2003]\] \[[P5 et al 2026][research_p5_2026]\] \[[Palmer and Petitt 1976][research_palmer_petitt_1976]\] \[[Pate 1964][research_pate_1964]\] \[[Pate and Deitering 1963][research_pate_deitering_1963]\] \[[Patterson 1989][research_patterson_1989]\] \[[Pei et al 2016][research_pei_2016]\] \[[Perez and Jansen 2014][research_perez_jansen_2014]\] \[[Pfaff 1968][research_pfaff_1968]\] \[[Pfeifle and Fichter 2023][research_pfeifle_fichter_2023]\] \[[Phillips and Everest 1953][research_phillips_everest_1953]\] \[[Pitkin 1968][research_pitkin_1968]\] \[[Power 1963][research_power_1963]\] \[[Qiang and Wang 2025][research_qiang_wang_2025]\] \[[Rao et al 2023][research_rao_2023]\] \[[Ratvasky et al 2010][research_ratvasky_barnhart_2010]\] \[[Ray et al 1988][research_ray_1988]\] \[[Raymer 2004][research_raymer_2004]\] \[[Reed 1941][research_reed_1941]\] \[[Report No. 297. The reduction of observed airplane performance to standard conditions 1929][research_report_no_1929]\] \[[Report No. 408. General 1932, Report No. 408. General Formulas][research_report_no_1932_4]\] \[[Report no. 485, The 1935, Report no. 485, The drag of][research_report_no_1935_2]\] \[[Riboldi 2019][research_riboldi_2019]\] \[[Rice 1946][research_rice_1946]\] \[[Richardson 1976][research_richardson_1976]\] \[[Riggins and Camberos 2020][research_riggins_camberos_2020]\] \[[Roberts 1963][research_roberts_1963]\] \[[Rockefeller 1937][research_rockefeller_1937]\] \[[Ross 1984][research_ross_1984]\] \[[Ryu et al 2022][research_ryu_2022]\] \[[Sachs 2016][research_sachs_2016]\] \[[Sagan et al 2025][research_sagan_lau_2025]\] \[[Salucci et al 2026][research_salucci_2026]\] \[[Sanders 1957][research_sanders_1957]\] \[[Sathish Kumar Sunnam et al. 2019][research_sathish_kumar_sunnam_et_al_2019]\] \[[Sawake 2026][research_sawake_2026]\] \[[Schairer 1937][research_schairer_1937]\] \[[Schäffer et al 2023][research_schaffer_bertsch_2023]\] \[[Secretary Of The Air Force Washington Dc 2001][research_secretaryoftheairforcewashingtondc_2001]\] \[[Seginer and Salomon 1983][research_seginer_salomon_1983]\] \[[Shimoyama and Kamisori 2017][research_shimoyama_kamisori_2017]\] \[[Shin et al 2018][research_shin_2018]\] \[[Simpson 1979][research_simpson_1979]\] \[[Sleeman 1971][research_sleeman_1971]\] \[[Smith 1983][research_smith_1983]\] \[[Snyder 1950][research_snyder_1950]\] \[[Snyder and Kohlman 2018][research_snyder_kohlman_2018]\] \[[Soltmann and Hall 2017][research_soltmann_hall_2017]\] \[[Somsel 1970][research_somsel_1970]\] \[[Son and Yee 2018][research_son_yee_2018]\] \[[Sonmez and Alemdaroglu 2015][research_sonmez_alemdaroglu_2015]\] \[[Steen 1994][research_steen_1994]\] \[[Stepniewski 1940][research_stepniewski_1940]\] \[[Stratford 1948][research_stratford_1948]\] \[[Strike 1982][research_strike_w_t_1982]\] \[[Sullivan and Clancy 1989][research_sullivan_clancy_1989]\] \[[Sun et al 2020][research_sun_2020]\] \[[Sun et al 2020][research_sun_2020_3]\] \[[Suvarna et al 2022][research_suvarna_shukla_2022]\] \[[Sóbester 2021][research_sobester_2021]\] \[[Taylor and Papadales 1976][research_taylor_papadales_1976]\] \[[Tenhave et al 2026][research_tenhave_2026]\] \[[Tomaszewski and Goraj 2019][research_tomaszewski_goraj_2019]\] \[[Torenbeek and Wittenberg 1983][research_torenbeek_wittenberg_1983]\] \[[Traub 2016][research_traub_2016_b]\] \[[Trevelyan and Blundell 1949][research_trevelyan_blundell_1949]\] \[[Underwood 1942][research_underwood_1942_2]\] \[[Van Wyckhouse 1966][research_vanwyckhouse_1966]\] \[[Vegh 2025][research_vegh_2025]\] \[[Wang et al 2019][research_wang_2019_2]\] \[[Ward 1968][research_ward_1968]\] \[[Watter 1930][research_watter_1930]\] \[[Weiser and Ossmann 2022][research_weiser_ossmann_2022]\] \[[Weiser et al 2023][research_weiser_2023]\] \[[Wendt 1947][research_wendt_1947]\] \[[Whoric 1973][research_whoric_1973]\] \[[Williams 1940][research_williams_1940]\] \[[Wooley and Childs 1954][research_wooley_childs_1954]\] \[[Woolf 2012][research_woolf_2012]\] \[[Wrestler and Clifton G. 1965][research_wrestler_clifton_g_1965]\] \[[Wu et al 2019][research_wu_2019_2]\] \[[Wu et al 2019][research_wu_2019]\] \[[Xu et al 2015][research_xu_2015]\] \[[Yager 1983][research_yager_1983]\] \[[Yegorov 1945][research_yegorov_1945]\] \[[Yongtao and Zhi 2014][research_yongtao_zhi_2014]\] \[[Yuan et al 2024][research_yuan_2024]\] \[[Yurttav et al 2025][research_yurttav_2025]\] \[[Zafirov 2020][research_zafirov_2020]\] \[[Zhang et al 2022][research_zhang_ma_2022]\] \[[Zhao and Gao 2019][research_zhao_gao_2019]\] \[[Zhu 2025][research_zhu_2025]\] \[[李 2023][research__2023]\]

### Aeroelasticity, flutter and gust loads

Flutter, divergence, aileron reversal and buzz, gust loads and the flexible high aspect ratio wing. **134 of the 203 records date from 2015 or later.**

**203 records.** \[[Abichandani and Rosenberg 1952][research_abichandani_rosenberg_1952]\] \[[Afonso et al 2017][research_afonso_2017]\] \[[Ahmadi and Farsadi 2024][research_ahmadi_farsadi_2024]\] \[[Ahmadi et al 2024][research_ahmadi_2024]\] \[[Alam and Hromcik 2019][research_alam_hromcik_2019]\] \[[Alam et al 2015][research_alam_2015]\] \[[Alexander 2025][research_alexander_2025_b]\] \[[Alighanbari 2002][research_alighanbari_2002]\] \[[Anderson et al 1973][research_anderson_1973]\] \[[Araujo-Estrada and Windsor 2021][research_araujo_estrada_windsor_2021]\] \[[Arnold 1942][research_arnold_1942]\] \[[Awadalla Ali Haj Ahmed 2024][research_awadalla_ali_haj_ahmed_2024]\] \[[Azzi et al 2024][research_azzi_tahiliani_2024]\] \[[Bachelder et al 2023][research_bachelder_aponso_2023]\] \[[Balatti et al 2021][research_balatti_2021]\] \[[Balatti et al 2023][research_balatti_2023]\] \[[Banerjee 1984][research_banerjee_1984]\] \[[Banerjee 1988][research_banerjee_1988]\] \[[Bartels et al 2017][research_bartels_2017]\] \[[Bendiksen 1993][research_bendiksen_1993]\] \[[Bergen and Arnold 1940][research_bergen_arnold_1940]\] \[[Bi et al 2017][research_bi_2017]\] \[[Bowers et al 2016][research_bowers_2016]\] \[[Bras et al 2022][research_bras_2022]\] \[[Bromfield and Dillman 2015][research_bromfield_dillman_2015]\] \[[Bromfield et al 2023][research_bromfield_2023_2]\] \[[Brown 1959][research_brown_1959]\] \[[Browne et al 2025][research_browne_2025]\] \[[Burris and Bender 1969][research_burris_bender_1969]\] \[[Cao et al 2024][research_cao_2024]\] \[[Cavaliere and Fezans 2024][research_cavaliere_fezans_2024]\] \[[Cecrdle 2011][research_cecrdle_2011]\] \[[Changchuan et al 2018][research_changchuan_2018]\] \[[Chen and Han 2017][research_chen_han_2017]\] \[[Chen et al 2025][research_chen_2025_5]\] \[[Cheung et al 2020][research_cheung_2020]\] \[[Chu and Widnall 1974][research_chu_widnall_1974]\] \[[Cole 1986][research_cole_1986]\] \[[Cole 1988][research_cole_1988]\] \[[Corwin et al 1989][research_corwin_1989]\] \[[Croom and Huffman 1957][research_croom_huffman_1957]\] \[[Birdsall 1970][research_d_l_birdsall_1970]\] \[[De Gaspari et al 2024][research_de_gaspari_2024]\] \[[Della Vecchia et al 2017][research_della_vecchia_2017]\] \[[Dickinson 1953][research_dickinson_1953]\] \[[Dilmi 2022][research_dilmi_2022]\] \[[Doggett and Soistmann 1992][research_doggett_soistmann_1992]\] \[[Douglas Aircraft Co Long Beach Ca 1962][research_douglas_aircraft_co_long_beach_ca_1962]\] \[[Duan and Zhang 2018][research_duan_zhang_2018]\] \[[Dussart et al 2019][research_dussart_2019]\] \[[Eckhaus 1962][research_eckhaus_1962]\] \[[Elyasi et al 2020][research_elyasi_2020]\] \[[Farhat 1998][research_farhat_1998]\] \[[Farhat 2000][research_farhat_2000]\] \[[Farhat 2001][research_farhat_2001]\] \[[Felt and Kehoe 1985][research_felt_kehoe_1985]\] \[[Fournier et al 2022][research_fournier_2022]\] \[[Försching and Zingel 1988][research_forsching_zingel_1988]\] \[[Gao et al 2024][research_gao_2024]\] \[[Gavrilovic et al 2018][research_gavrilovic_2018]\] \[[Ghalandari et al 2022][research_ghalandari_2022]\] \[[Gimmestad 1980][research_gimmestad_1980]\] \[[Goland 1952][research_goland_1952]\] \[[Gu et al 2024][research_gu_2024]\] \[[Guimarães Neto 2025][research_guimaraes_neto_2025]\] \[[Guo et al 2022][research_guo_2022_2]\] \[[Haftka 1977][research_haftka_1977]\] \[[Hansen et al 2022][research_hansen_2022]\] \[[Hanson et al 2014][research_hanson_2014]\] \[[Hao et al 2023][research_hao_2023]\] \[[Hicks et al 2014][research_hicks_durbin_2014]\] \[[Hillebrand et al 2025][research_hillebrand_2025]\] \[[Hoseini and Hodges 2019][research_hoseini_hodges_2019]\] \[[Hu et al 2022][research_hu_2022]\] \[[Hu et al 2026][research_hu_2026_2]\] \[[Hui and Chen 2023][research_hui_chen_2023]\] \[[Hunn 1953][research_hunn_1953]\] \[[Ibren et al 2020][research_ibren_2020]\] \[[Iovnovich et al 2018][research_iovnovich_2018]\] \[[Jernell 1978][research_jernell_1978]\] \[[Jones 1976][research_jones_1976]\] \[[Karpel 1990][research_karpel_1990]\] \[[Khalil and Bauknecht 2024][research_khalil_bauknecht_2024]\] \[[Khalil and Fezans 2020][research_khalil_fezans_2020]\] \[[Khalil et al 2022][research_khalil_2022]\] \[[Kheiri and Riazat 2025][research_kheiri_riazat_2025]\] \[[Khuat et al 2025][research_khuat_2025]\] \[[Kilimtzidis and Kostopoulos 2023][research_kilimtzidis_kostopoulos_2023]\] \[[Kirsch et al 2020][research_kirsch_2020]\] \[[Klein et al 2017][research_klein_krainski_2017]\] \[[Klug et al 2023][research_klug_2023]\] \[[Konar 2020][research_konar_2020]\] \[[Krawczyk et al 2024][research_krawczyk_2024]\] \[[Krzywoblocki 1943][research_krzywoblocki_1943]\] \[[Kumar et al 2025][research_kumar_2025_2]\] \[[Lagemann et al 2024][research_lagemann_2024]\] \[[Le Clainche et al 2019][research_le_clainche_2019]\] \[[Lee et al 2022][research_lee_2022_2]\] \[[Levin and Katz 1984][research_levin_katz_1984]\] \[[Leylek and Costello 2010][research_leylek_costello_2010]\] \[[Li and Qin 2020][research_li_qin_2020]\] \[[Li and Qin 2021][research_li_qin_2021]\] \[[Li and Qin 2022][research_li_qin_2022]\] \[[Li et al 2024][research_li_2024]\] \[[Liu 2018][research_liu_2018_3]\] \[[Liu and Sun 2016][research_liu_sun_2016]\] \[[Liu et al 2017][research_liu_2017_2]\] \[[Liu et al 2023][research_liu_zhang_2023]\] \[[Liu et al 2026][research_liu_fan_2026]\] \[[Lomax 1948][research_lomax_1948]\] \[[Luderer and Thielecke 2025][research_luderer_thielecke_2025]\] \[[Malisani et al 2021][research_malisani_2021]\] \[[Mallik et al 2015][research_mallik_2015]\] \[[Mardanpour et al 2018][research_mardanpour_2018]\] \[[McCarthy et al 1955][research_mccarthy_1955]\] \[[McDonnell Aircraft Corp St Louis Mo 1950][research_mcdonnell_aircraft_corp_st_louis_mo_1950]\] \[[Mohamed et al 2021][research_mohamed_2021]\] \[[Müller et al 2026][research_muller_2026]\] \[[NACA Conference on Aircraft 1957][research_naca_conference_1957]\] \[[Nagaraja et al 1982][research_nagaraja_1982]\] \[[Narimani et al 2025][research_narimani_2025]\] \[[Negahban et al 2024][research_negahban_2024]\] \[[Nejati et al 2018][research_nejati_2018]\] \[[Nguyen et al 2017][research_nguyen_2017]\] \[[Nguyen and Xiong][research_nhan_nguyen_juntao_xiong]\] \[[Oktay and Özen 2022][research_oktay_ozen_2022]\] \[[Onkar et al 2024][research_onkar_2024]\] \[[Otsuka et al 2021][research_otsuka_2021]\] \[[Otsuka et al 2022][research_otsuka_2022]\] \[[Ouellette et al 2026][research_ouellette_2026]\] \[[Portapas and Cooke 2020][research_portapas_cooke_2020]\] \[[Pusch et al 2019][research_pusch_2019]\] \[[Pushtaev 1989][research_pushtaev_1989]\] \[[Qi and Zhao 2020][research_qi_zhao_2020]\] \[[Qi et al 2018][research_qi_2018]\] \[[Qiao et al 2018][research_qiao_2018]\] \[[Qiao et al 2025][research_qiao_2025]\] \[[Qu and Li 2022][research_qu_li_2022]\] \[[Quinn 1963][research_quinn_1963]\] \[[Rankine and Leondes 1972][research_rankine_leondes_1972]\] \[[Reed 1966][research_reed_1966]\] \[[Rehman 2022][research_rehman_2022]\] \[[Rhoads 1952][research_rhoads_1952]\] \[[Rieck et al 2026][research_rieck_2026]\] \[[Bartels and Jacobson][research_robert_bartels_kevin_jacobson]\] \[[Rodden 1956][research_rodden_1956]\] \[[Rodden 1989][research_rodden_1989]\] \[[Rokhsaz and Kliment 2017][research_rokhsaz_kliment_2017]\] \[[Roos 1985][research_roos_1985]\] \[[Roskam and Dusto 1969][research_roskam_dusto_1969]\] \[[Roskam et al 1968][research_roskam_1968]\] \[[Runyan et al 1952][research_runyan_1952]\] \[[Ryan Aeronautical Co San Diego Ca 1963][research_ryan_aeronautical_co_san_diego_ca_1963]\] \[[Sabatini et al 2026][research_sabatini_2026]\] \[[Sahyoun et al 2026][research_sahyoun_2026]\] \[[Saltari et al 2017][research_saltari_2017]\] \[[Shi and Wan 2015][research_shi_wan_2015]\] \[[Silvestre and Luckner 2015][research_silvestre_luckner_2015]\] \[[Soneda et al 2019][research_soneda_2019]\] \[[Spada et al 2017][research_spada_2017]\] \[[Steger and Bailey 1980][research_steger_bailey_1980]\] \[[Wright][research_stephen_j_wright]\] \[[Sudha et al 2018][research_sudha_2018]\] \[[Suleman et al 2016][research_suleman_2016]\] \[[Swaim 1971][research_swaim_1971]\] \[[Swaim and Connor 1968][research_swaim_connor_1968]\] \[[Swaim and Staab 1978][research_swaim_staab_1978]\] \[[Swaim and Yen 1979][research_swaim_yen_1979]\] \[[Szczyglowski et al 2019][research_szczyglowski_2019]\] \[[Tang et al 2016][research_tang_2016]\] \[[Tantaroudas and Karachalios 2026][research_tantaroudas_karachalios_2026]\] \[[Teixeira and Cesnik 2020][research_teixeira_cesnik_2020]\] \[[Thomson 1946][research_thomson_1946]\] \[[Toffol 2024][research_toffol_2024]\] \[[Tsatsas et al 2022][research_tsatsas_2022]\] \[[Ulvr et al 2026][research_ulvr_2026]\] \[[Van Gaasbeek 1980][research_vangaasbeek_1980]\] \[[Veley et al 2008][research_veley_2008]\] \[[Versiani et al 2019][research_versiani_2019]\] \[[Wang 2019][research_wang_2019]\] \[[Wang and Chen 2024][research_wang_chen_2024]\] \[[Wang et al 2019][research_wang_2019_4]\] \[[Wang et al 2021][research_wang_wu_2021]\] \[[Wang et al 2022][research_wang_2022_3]\] \[[Wang et al 2022][research_wang_2022_2]\] \[[Wang et al 2026][research_wang_2026_2]\] \[[Watson 1982][research_watson_1982]\] \[[Westin et al 2023][research_westin_2023]\] \[[White 1971][research_white_1971]\] \[[Willebeek-LeMair and Rhinehart 2023][research_willebeeklemair_rhinehart_2023]\] \[[Wu et al 2017][research_wu_2017_2]\] \[[Xie et al 2017][research_xie_2017]\] \[[Xiong et al 2026][research_xiong_2026]\] \[[Yan et al 2024][research_yan_tian_2024]\] \[[Yang and Li 2022][research_yang_li_2022]\] \[[Yang et al 2016][research_yang_2016]\] \[[Yeager et al 1997][research_yeager_1997]\] \[[Yi et al 2025][research_yi_2025]\] \[[You et al 2020][research_you_2020_2]\] \[[Zhang and Zhao 2023][research_zhang_zhao_2023]\] \[[Zhang et al 2026][research_zhang_2026_4]\] \[[Zheng et al 2026][research_zheng_2026]\] \[[Ziakos et al 2025][research_ziakos_2025]\]

### Flight test, system identification and parameter estimation

Flight test technique and management, system identification and parameter estimation from flight data, and flight test reports.

**202 records.** \[[Abramson 1975][research_abramson_1975]\] \[[Abramson 1977][research_abramson_1977]\] \[[Advisory Group for Aerospace Research and Development 1984][research_advisorygroupforaerospaceresearchanddevelopment_1984]\] \[[Air Force Flight Test Center Edwards Afb Ca 1970][research_air_force_flight_test_center_edwards_afb_ca_1970]\] \[[Air Force Flight Test Center Edwards Afb Ca 1974][research_air_force_flight_test_center_edwards_afb_ca_1974_2]\] \[[Air Force Flight Test Center Edwards Afb Ca 1974][research_air_force_flight_test_center_edwards_afb_ca_1974]\] \[[Air Force Flight Test Center Edwards Afb Ca 1995][research_air_force_flight_test_center_edwards_afb_ca_1995]\] \[[Air Force Flight Test Center Edwards Afb Ca 2002][research_air_force_flight_test_center_edwards_afb_ca_2002_2]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_air_force_test_pilot_school_edwards_afb_ca_1990]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_air_force_test_pilot_school_edwards_afb_ca_1990_2]\] \[[Air Force Test Pilot School Edwards Afb Ca 1993][research_air_force_test_pilot_school_edwards_afb_ca_1993]\] \[[Air Proving Ground Center Eglin Afb Fl 1954][research_air_proving_ground_center_eglin_afb_fl_1954]\] \[[Air Proving Ground Center Eglin Afb Fl 1955][research_air_proving_ground_center_eglin_afb_fl_1955]\] \[[Air Proving Ground Center Eglin Afb Fl 1955][research_air_proving_ground_center_eglin_afb_fl_1955_2]\] \[[Aircraft and Rotorcraft System Identification: Engineering Methods with Flight Test Examples, Second Edition (Bookshelf) 2016][research_aircraft_and_2016]\] \[[Alford 2004][research_alford_2004]\] \[[Alford and Knarr 1999][research_alford_knarr_1999]\] \[[Allen and White 1957][research_allen_white_1957]\] \[[American Institute of Aeronautics and Astronautics 1992][research_american_institute_of_aeronautics_and_astronautics_1992]\] \[[Armstrong 1977][research_armstrong_1977]\] \[[Army Aviation School Fort Rucker Al 1961][research_army_aviation_school_fort_rucker_al_1961]\] \[[Arnold 1981][research_arnold_1981]\] \[[Bachelder and Klyde 2011][research_bachelder_klyde_2011]\] \[[Baier 1970][research_baier_1970]\] \[[Barnette 1978][research_barnette_1978]\] \[[Beale and Cook 1985][research_beale_cook_1985]\] \[[Bender and OConnor 1974][research_bender_o_connor_1974]\] \[[Bennett et al 1978][research_bennett_1978_2]\] \[[Bleimeyer 1981][research_bleimeyer_1981]\] \[[Boeing Co Morton Pa Vertol Div 1961][research_boeing_co_morton_pa_vertol_div_1961]\] \[[Brandon and Morelli 2016][research_brandon_morelli_2016]\] \[[Brennan and McDaniel 1994][research_brennan_mcdaniel_1994]\] \[[Burt and Uselton 1976][research_burt_uselton_1976]\] \[[Bussolari et al 1987][research_bussolari_youngren_1987]\] \[[Camponogara et al 2019][research_camponogara_2019]\] \[[Carico 1998][research_carico_1998]\] \[[Che et al 2021][research_che_2021]\] \[[Choi 2025][research_choi_2025]\] \[[Manning et al 1992][research_clarke_o_manning_1992]\] \[[Condon et al 1970][research_condon_1970]\] \[[Cotton 1974][research_cotton_1974]\] \[[Crawford and Hodgson 1961][research_crawford_hodgson_1961]\] \[[Cusimano and Johnson 1994][research_cusimano_johnson_1994]\] \[[Day and Guthrie 1958][research_day_guthrie_1958]\] \[[Day and Reisert 1959][research_day_reisert_1959]\] \[[Deckert and Ferry 1959][research_deckert_ferry_1959]\] \[[Deckert and Hodgson 1962][research_deckert_hodgson_1962]\] \[[Dias 2023][research_dias_2023]\] \[[Doko and Sasongko 2026][research_doko_sasongko_2026]\] \[[Dong et al 2024][research_dong_2024_2]\] \[[Donizetti et al 2023][research_donizetti_2023]\] \[[Dooley and Yeary 1979][research_dooley_yeary_1979]\] \[[Du 2024][research_du_2024_2]\] \[[Dunlap and Schalk 1956][research_dunlap_1956]\] \[[Dwyer 1994][research_dwyer_1994]\] \[[Evans and Schilling 1983][research_evans_schilling_1983]\] \[[Evans and Schilling 1984][research_evans_schilling_1984]\] \[[Faulcon and Monteith 1978][research_faulcon_monteith_1978]\] \[[Fechter and Mills 1988][research_fechter_mills_1988]\] \[[Feimin 2021][research_feimin_2021]\] \[[Feng 2022][research_feng_2022]\] \[[Fenwick 1966][research_fenwick_1966]\] \[[Fenwick 1967][research_fenwick_1967]\] \[[Ferrell et al 1974][research_ferrell_1974]\] \[[Fosdick 1970][research_fosdick_1970]\] \[[Burcham et al 1992][research_frank_w_burcham_1992]\] \[[Freuler and Hoffmann 1977][research_freuler_hoffmann_1977]\] \[[Gavurin 1965][research_gavurin_1965]\] \[[George et al 2022][research_george_2022]\] \[[Gera et al 1981][research_gera_1981]\] \[[Gillard 1998][research_gillard_1998]\] \[[Glenn and Midkiff 1951][research_glenn_midkiff_1951]\] \[[Gonczy 2015][research_gonczy_2015]\] \[[Grauer 2021][research_grauer_2021]\] \[[Grauer and Morelli 2023][research_grauer_morelli_2023]\] \[[Grauer et al 2017][research_grauer_2017]\] \[[Gray 2026][research_gray_2026]\] \[[Hamory and Murray 1993][research_hamory_murray_1993]\] \[[Hart 1992][research_hart_1992]\] \[[He and Ai 2018][research_he_ai_2018]\] \[[Holberg and Grabowsky 1981][research_holberg_grabowsky_1981]\] \[[Hou and Song 2024][research_hou_song_2024]\] \[[Howell 1988][research_howell_1988]\] \[[Ignatyev et al 2019][research_ignatyev_2019]\] \[[Iliff and Maine 1984][research_iliff_maine_1984]\] \[[Irvine 1968][research_irvine_1968]\] \[[Ishola et al 2024][research_ishola_2024]\] \[[Jategaonkar 2023][research_jategaonkar_2023]\] \[[Johnson and Anderson 1966][research_johnson_anderson_1966]\] \[[Jones 1970][research_jones_1970]\] \[[Kayten and Koven 1945][research_kayten_koven_1945]\] \[[Kelley et al 1990][research_kelley_1990]\] \[[Kelly 1988][research_kelly_1988]\] \[[Kim and Jeong 2026][research_kim_jeong_2026]\] \[[Kim et al 2025][research_kim_2025_5]\] \[[Kizer 1977][research_kizer_1977]\] \[[Klein et al 1982][research_klein_1982]\] \[[Klein et al 1983][research_klein_1983]\] \[[Korsun and Moung Htang 2023][research_korsun_moung_htang_2023]\] \[[Kulba et al 2021][research_kulba_2021]\] \[[Kumar and Ghosh 2018][research_kumar_ghosh_2018]\] \[[Kumar and Ghosh 2023][research_kumar_ghosh_2023_2]\] \[[Kuppuswamy and Kiran 1981][research_kuppuswamy_kiran_1981]\] \[[Li et al 2025][research_li_2025]\] \[[Li et al 2025][research_li_2025_2]\] \[[Lichota 2023][research_lichota_2023]\] \[[Lichota et al 2017][research_lichota_2017]\] \[[Liu 1962][research_liu_1962]\] \[[Liu et al 2015][research_liu_2015_2]\] \[[Lofthouse and Cummings 2017][research_lofthouse_cummings_2017]\] \[[Lu et al 2015][research_lu_2015]\] \[[Lustig et al 1960][research_lustig_1960]\] \[[Macmillan 1981][research_macmillan_1981]\] \[[Marston et al 2015][research_marston_sternberg_2015]\] \[[Martin 1978][research_martin_1978]\] \[[Matheny and Gatlin 1978][research_matheny_gatlin_1978]\] \[[Matsuki et al 2018][research_matsuki_2018]\] \[[Mehra et al 1972][research_mehra_1972]\] \[[Mehra et al 1974][research_mehra_1974]\] \[[Michaels 1969][research_michaels_1969]\] \[[Monstein et al 2019][research_monstein_2019]\] \[[Moralez et al 2004][research_moralez_2004]\] \[[Morelli and Cooper 2015][research_morelli_cooper_2015]\] \[[Morris and Alexander 1978][research_morris_alexander_1978]\] \[[Narendra and Tripathi 1973][research_narendra_tripathi_1973]\] \[[Nash 1982][research_nash_1982]\] \[[Naval Air Test Center Patuxent River Md 1963][research_naval_air_test_center_patuxent_river_md_1963]\] \[[Neves et al 2020][research_neves_2020]\] \[[Nicolaides 1976][research_nicolaides_1976]\] \[[North American Aviation Inc Los Angeles Ca 1956][research_northamericanaviationinclosangelesca_1956]\] \[[North American Aviation Inc Los Angeles Ca 1963][research_north_american_aviation_inc_los_angeles_ca_1963]\] \[[Norton 1990][research_norton_1990]\] \[[Obermark 2004][research_obermark_2004]\] \[[Ouda 2021][research_ouda_2021]\] \[[Ovcharenko and Poplavsky 2021][research_ovcharenko_poplavsky_2021]\] \[[Palkin and Zenchenko 2025][research_palkin_zenchenko_2025]\] \[[Park 2026][research_park_2026_2]\] \[[Park et al 2018][research_park_2018_2]\] \[[Paulson and Shanks 1959][research_paulson_shanks_1959]\] \[[Paulson and Shanks 1961][research_paulson_shanks_1961_2]\] \[[Pawlak 1994][research_pawlak_1994]\] \[[Peebles 2007][research_peebles_2007]\] \[[Perkins et al 1977][research_perkins_1977]\] \[[Petersen 1981][research_petersen_1981]\] \[[Hamory and Murray 1992][research_philip_j_hamory_james_e_murray_1992]\] \[[Quanyan 2021][research_quanyan_2021]\] \[[Rediess and Melton 1994][research_rediess_melton_1994]\] \[[Kulikova N.V. CHulin N.A. 2023][research_refinement_of_2023]\] \[[Rhoads 1970][research_rhoads_1970]\] \[[Rice and Hazlwood 1994][research_rice_hazlwood_1994]\] \[[Roberts 1988][research_roberts_1988_b]\] \[[Rodden and Giesing 1970][research_rodden_giesing_1970]\] \[[Sandstrom and White 1961][research_sandstrom_white_1961]\] \[[Savory and Toy 1984][research_savory_toy_1984]\] \[[Schade and Crane 1965][research_schade_crane_1965]\] \[[Schofield 1984][research_schofield_1984]\] \[[Schreadley 1977][research_schreadley_1977]\] \[[Schumacher 1952][research_schumacher_1952]\] \[[Seacord and Teitelbaum 1947][research_seacord_teitelbaum_1947]\] \[[Shi et al 2023][research_shi_2023]\] \[[Sibert 1947][research_sibert_1947]\] \[[Sim and Curry 1978][research_sim_curry_1978]\] \[[Simmons et al 2023][research_simmons_2023_2]\] \[[Simmons et al 2023][research_simmons_2023_4]\] \[[Simulation in support of flight test - In retrospect 1988][research_simulation_in_1988]\] \[[Srivastava 2016][research_srivastava_2016]\] \[[Stange 1959][research_stange_1959]\] \[[Strattan 1978][research_strattan_1978]\] \[[Strier and Julian 1955][research_strier_1955]\] \[[Svendsen 1994][research_svendsen_1994]\] \[[Tai et al 2023][research_tai_2023_2]\] \[[Tai et al 2024][research_tai_2024]\] \[[Tangler 1979][research_tangler_1979]\] \[[Townsend and Phillips 1955][research_townsend_phillips_1955]\] \[[Townsend and Phillips 1956][research_townsend_phillips_1956]\] \[[Tracy 1981][research_tracy_1981]\] \[[Traven and Whitley 1995][research_traven_whitley_1995]\] \[[Tsoubanos 1979][research_tsoubanos_1979]\] \[[Ulry et al 1976][research_ulry_1976]\] \[[Vagianos and Rooney 1964][research_vagianos_rooney_1964]\] \[[Van Pelt 1981][research_vanpelt_1981]\] \[[Vaughn and Lindsay 1988][research_vaughn_lindsay_1988]\] \[[Wang 2024][research_wang_2024_7]\] \[[Wang and Zhang 2020][research_wang_zhang_2020]\] \[[Wang et al 2015][research_wang_2015]\] \[[Wang et al 2022][research_wang_2022_4]\] \[[Wang et al 2023][research_wang_2023]\] \[[Ward 1988][research_ward_1988]\] \[[Watts 1976][research_watts_1976]\] \[[Wei and Renliang 2015][research_wei_renliang_2015]\] \[[Weiss et al 1986][research_weiss_eterno_1986]\] \[[Winn and Kishi 1972][research_winn_kishi_1972]\] \[[Xue and Haibin 2017][research_xue_haibin_2017]\] \[[Yancey 1964][research_yancey_1964]\] \[[Yasue 2020][research_yasue_2020]\] \[[Zajdel et al 2022][research_zajdel_2022]\] \[[Zajdel et al 2024][research_zajdel_2024]\] \[[Zajdel et al 2024][research_zajdel_2024_2]\] \[[Zelenka et al 1995][research_zelenka_1995]\] \[[Zhang 2024][research_zhang_2024]\] \[[Zhang and Zhou 2024][research_zhang_zhou_2024]\] \[[Zhou 2022][research_zhou_2022]\]

### Pilot training, simulation, human factors and safety

Pilot training and selection, simulators and their fidelity, startle and surprise, workload, human factors and aviation safety. **103 of the 187 records date from 2015 or later.**

**187 records.** \[[Abramov et al 2019][research_abramov_2019]\] \[[Adolph 1981][research_adolph_1981]\] \[[Aguiar and Cuevas 2017][research_aguiar_cuevas_2017]\] \[[Aguiar et al 2017][research_aguiar_2017]\] \[[Air Force Flight Test Center Edwards Afb Ca 2002][research_air_force_flight_test_center_edwards_afb_ca_2002]\] \[[Air Force Test Pilot School Edwards Afb Ca 1962][research_air_force_test_pilot_school_edwards_afb_ca_1962]\] \[[Aircraft Safety Office 1971][research_aircraft_safety_office_1971]\] \[[Aleksandrov 2025][research_aleksandrov_2025]\] \[[Allen et al 2000][research_allen_eveker_2000]\] \[[Aláez et al 2022][research_alaez_2022]\] \[[Army Aviation Center And Fort Rucker Al 1992][research_armyaviationcenterandfortruckeral_1992]\] \[[Atmaca et al 2025][research_atmaca_2025]\] \[[Badzli 2023][research_badzli_2023]\] \[[Bagley et al 2026][research_bagley_2026]\] \[[Baisden 1980][research_baisden_1980]\] \[[Beard et al 2013][research_beard_2013]\] \[[Borst 1978][research_borst_1978]\] \[[Bortolussi 1997][research_bortolussi_1997]\] \[[Boyd 2015][research_boyd_2015]\] \[[Boyd 2015][research_boyd_2015_2]\] \[[Boyd and Stolzer 2016][research_boyd_stolzer_2016]\] \[[Bray and Larsen 1965][research_bray_larsen_1965]\] \[[Brian Trubshaw Test Pilot 2006][research_brian_trubshaw_2006]\] \[[Bronder et al 2012][research_bronder_lee_2012]\] \[[Bynum 1978][research_bynum_1978]\] \[[Cain 1979][research_cain_1979]\] \[[Carico][research_carico]\] \[[Carico et al][research_carico_chengjianhe]\] \[[Carico et al 2001][research_carico_he_2001]\] \[[Caro 2017][research_caro_2017]\] \[[Carroll et al 2021][research_carroll_2021]\] \[[Causse et al 2026][research_causse_2026]\] \[[Chappelle et al 2014][research_chappelle_swearengen_2014]\] \[[Chen et al 2025][research_chen_2025_4]\] \[[Chen et al 2025][research_chen_2025]\] \[[Chen et al 2025][research_chen_2025_3]\] \[[Chen et al 2026][research_chen_2026]\] \[[Clewley and Nixon 2019][research_clewley_nixon_2019]\] \[[Clothier et al 2015][research_clothier_2015]\] \[[Clousing 1965][research_clousing_1965]\] \[[Cornell Aeronautical Lab Inc Buffalo Ny 1947][research_cornell_aeronautical_lab_inc_buffalo_ny_1947]\] \[[Cotting 2016][research_cotting_2016]\] \[[Craig et al 1999][research_craig_1999]\] \[[Cross and Ryley 2024][research_cross_ryley_2024]\] \[[Cunningham 1962][research_cunningham_1962]\] \[[Department Of The Air Force Washington Dc 2005][research_department_of_the_air_force_washington_dc_2005]\] \[[Diarra et al 2023][research_diarra_2023]\] \[[Dohme 1981][research_dohme_1981]\] \[[Donateo and Totaro 2019][research_donateo_totaro_2019]\] \[[Dong et al 2024][research_dong_2024]\] \[[Dreyfus and Dreyfus 1979][research_dreyfus_dreyfus_1979]\] \[[Du et al 2024][research_du_2024]\] \[[Duchevet et al 2025][research_duchevet_2025]\] \[[Dusterberry 1964][research_dusterberry_1964]\] \[[Eppley 1963][research_eppley_1963]\] \[[Eshmuradov and Bekbaev 2023][research_eshmuradov_bekbaev_2023]\] \[[Morelli][research_eugeneamorelli]\] \[[Gardini et al 2022][research_gardini_2022]\] \[[Geister et al 2017][research_geister_2017]\] \[[General Electric Co Schenectady Ny 1952][research_generalelectriccoschenectadyny_1952]\] \[[Gilbert et al 1976][research_gilbert_nguyen_1976]\] \[[Gleason et al 1996][research_gleason_walker_1996]\] \[[Grantham et al 1984][research_grantham_1984]\] \[[Grantham et al 1985][research_grantham_1985]\] \[[Grether 1973][research_grether_1973]\] \[[Griffin and McBride 1986][research_griffin_mcbride_1986]\] \[[Grindley et al 2025][research_grindley_2025]\] \[[Gu 2025][research_gu_2025]\] \[[Guldal and Andersson 2020][research_guldal_andersson_2020]\] \[[Guthridge 2025][research_guthridge_2025]\] \[[Harnyoot 2018][research_harnyoot_2018]\] \[[Hart 1956][research_hart_1956]\] \[[Hart 1984][research_hart_1984]\] \[[Hashii and Thompson 2018][research_hashii_thompson_2018]\] \[[Henderson 2022][research_henderson_2022]\] \[[Hess 1977][research_hess_1977]\] \[[Hjellvik and Mallam 2024][research_hjellvik_mallam_2024]\] \[[Houston et al 1954][research_houston_smith_1954]\] \[[Hunter and Burke 1992][research_hunter_burke_1992]\] \[[Intano and Howse 1991][research_intano_howse_1991]\] \[[Irsyad Lukman and Agoes Moelyadi 2018][research_irsyad_lukman_agoes_moelyadi_2018]\] \[[Jiao et al 2022][research_jiao_2022]\] \[[Johnson 1975][research_johnson_1975]\] \[[Jolley and Caro 1970][research_jolley_1970]\] \[[Litt et al 2022][research_jonathan_s_litt_2022]\] \[[Justiz and Patel 1988][research_justiz_patel_1988]\] \[[Kellogg 1946][research_kellogg_1946]\] \[[Kibbee 1978][research_kibbee_1978]\] \[[Kim 2020][research_kim_2020]\] \[[Kim and Kim 2020][research_kim_kim_2020]\] \[[Kyrpenko 2015][research_kyrpenko_2015]\] \[[la Cour-Harbo 2018][research_la_cour_harbo_2018]\] \[[Landman et al 2017][research_landman_2017]\] \[[Landman et al 2020][research_landman_2020]\] \[[Lang 1981][research_lang_1981]\] \[[Lee et al 2021][research_lee_2021]\] \[[Leonidov 2025][research_leonidov_2025]\] \[[Li et al 2023][research_li_2023]\] \[[Lilla et al 2025][research_lilla_2025]\] \[[Litt et al 2012][research_litt_2012]\] \[[Liu et al 2018][research_liu_2018_2]\] \[[Haworth et al][research_loran_haworth]\] \[[Löhr and Haines 2024][research_lohr_haines_2024]\] \[[MacDonald and Shepherd 2008][research_macdonald_shepherd_2008]\] \[[Mamich A.V. et al 2025][research_mamich_a_v_2025]\] \[[Ogburn et al 1991][research_marilyn_e_ogburn_1991]\] \[[McAree et al 2018][research_mcaree_2018]\] \[[Metodiev 2024][research_metodiev_2024]\] \[[Middleton et al 1975][research_middleton_hurt_1975]\] \[[Miller and Khinoo 1994][research_miller_khinoo_1994]\] \[[Minor 2008][research_minor_2008]\] \[[Mostarac et al 2022][research_mostarac_rescic_2022]\] \[[Murray et al 1992][research_murray_1992]\] \[[Myers et al 2018][research_myers_2018]\] \[[Na and Cho 2022][research_na_cho_2022]\] \[[Navaratna et al 2019][research_navaratna_2019]\] \[[Neff 2019][research_neff_2019]\] \[[Northrop Aircraft Inc Hawthorne Ca 1952][research_northrop_aircraft_inc_hawthorne_ca_1952]\] \[[Oh and Yoon 2022][research_oh_yoon_2022]\] \[[Harendra et al 1973][research_pbharendra_mjjoglekar_1973]\] \[[Paullin et al 2011][research_paullin_2011]\] \[[Pauls and Gollnick 2025][research_pauls_gollnick_2025]\] \[[Pavlusíková and Chodelka 2023][research_pavlusikova_chodelka_2023]\] \[[Petitt 2017][research_petitt_2017]\] \[[Pioneering woman test pilot receives outstanding leadership 2001][research_pioneering_woman_2001]\] \[[Pleban and Beal 2002][research_pleban_beal_2002]\] \[[Powell-Dunford et al 2016][research_powell_dunford_2016]\] \[[Primatesta et al 2019][research_primatesta_2019]\] \[[Pugh 1972][research_pugh_1972]\] \[[QinetiQ welcomes a new chief test pilot to MOD Boscombe Down 2002][research_qinetiq_welcomes_2002]\] \[[Quinn and Breidenbach 1978][research_quinn_breidenbach_1978]\] \[[Ratvasky et al 2003][research_ratvasky_blankenship_2003]\] \[[Rawson 1963][research_rawson_1963]\] \[[Reising et al 1996][research_reising_1996]\] \[[Rey et al 2021][research_rey_2021]\] \[[Reynolds et al 2018][research_reynolds_2018]\] \[[Ringland and Craig 1977][research_ringland_craig_1977]\] \[[Roberts and Brown 1988][research_roberts_brown_1988]\] \[[Roberts and Shawler 1994][research_roberts_shawler_1994]\] \[[Rusakov and Krupetskyh 2012][research_rusakov_krupetskyh_2012]\] \[[Saastamoinen and Maunula 2021][research_saastamoinen_maunula_2021]\] \[[Saravo 1976][research_saravo_1976]\] \[[Schollenberger et al 2025][research_schollenberger_2025]\] \[[Schwartz and Wray 1969][research_schwartz_wray_1969]\] \[[Serra and Branco 2026][research_serra_branco_2026]\] \[[Seville Research Corp Pensacola Fl 1979][research_seville_research_corp_pensacola_fl_1979]\] \[[Shafer 1991][research_shafer_1991]\] \[[Shafer 1992][research_shafer_1992]\] \[[Shannon and Wang 1973][research_shannon_wang_1973]\] \[[Sharma 2016][research_sharma_2016]\] \[[Simmons 2023][research_simmons_2023]\] \[[Sims and Kimberlin 1995][research_sims_kimberlin_1995]\] \[[Siqueira et al 2025][research_siqueira_2025]\] \[[Socha et al 2026][research_socha_2026]\] \[[Somerville et al 2025][research_somerville_2025]\] \[[Somerville et al 2026][research_somerville_2026]\] \[[Somerville et al 2026][research_somerville_2026_2]\] \[[Spanò Cuomo and Guglieri 2021][research_spano_cuomo_guglieri_2021]\] \[[Sun 2026][research_sun_2026]\] \[[Surkova and Dolhoierova 2025][research_surkova_dolhoierova_2025]\] \[[The Development of Aviation Training Syllabus Material 1948][research_the_development_1948]\] \[[Trollip 1977][research_trollip_1977]\] \[[Truong et al 2024][research_truong_2024]\] \[[Vicory 1968][research_vicory_1968]\] \[[Vidović et al 2022][research_vidovic_2022]\] \[[Vitsas 2016][research_vitsas_2016]\] \[[Vlaskamp et al 2025][research_vlaskamp_2025]\] \[[Vlaskamp et al 2026][research_vlaskamp_2026]\] \[[Vlaskamp et al 2026][research_vlaskamp_2026_2]\] \[[Walker 2015][research_walker_2015]\] \[[Walker 2024][research_walker_2024]\] \[[Walker et al 2016][research_walker_2016]\] \[[Warner 1993][research_warner_1993]\] \[[Washington et al 2017][research_washington_2017]\] \[[Watson et al 2020][research_watson_2020]\] \[[Wei et al 2022][research_wei_2022_2]\] \[[Wesolek 2007][research_wesolek_2007]\] \[[Yazgan and Kucuk Yilmaz 2018][research_yazgan_kucuk_yilmaz_2018]\] \[[You 2020][research_you_2020]\] \[[Yusuf et al 2022][research_yusuf_2022]\] \[[Zaal et al 2015][research_zaal_2015]\] \[[Zeller and Gary 2001][research_zeller_jr_2001]\] \[[Zhang et al 2025][research_zhang_2025]\] \[[Zikmund et al 2019][research_zikmund_2019]\] \[[Şenol 2020][research_senol_2020]\] \[[Дмитренко 2024][research__2024]\] \[[Задкова 2015, Pilots Errors Accounting and][research__2015]\]

### Lateral control, ailerons and adverse yaw

Ailerons, spoilers and rudders, the rolling and yawing moments they produce, and adverse yaw. **74 of the 180 records date from before 1970.**

**This is the X-26A's keystone literature, and it is old.** The yawing moment of a deflected aileron was measured and tabulated in the decades before the aircraft flew, which is why the subject is documented under the period's vocabulary of ailerons, yawing moment and lateral control.

**180 records.** \[[Adams 1951][research_adams_1951]\] \[[Altman 1952][research_altman_1952]\] \[[Arena et al 1993][research_arena_1993]\] \[[Ashkenas 1946][research_ashkenas_1946]\] \[[Baker 1941][research_baker_1941]\] \[[Becker and Korycinski 1944][research_becker_korycinski_1944]\] \[[Bennett and Johnson 1947][research_bennett_johnson_1947]\] \[[Bischoff et al 1974][research_bischoff_1974]\] \[[Braslow 1944][research_braslow_1944]\] \[[Braslow and Visconti 1949][research_braslow_visconti_1949]\] \[[Cobleigh et al 1994][research_brent_r_cobleigh_1994]\] \[[Bretoi 1952][research_bretoi_1952]\] \[[Brincklow and Hunsaker 2021][research_brincklow_hunsaker_2021]\] \[[Brincklow et al 2021][research_brincklow_montgomery_2021]\] \[[Brincklow et al 2024][research_brincklow_montgomery_2024]\] \[[Bruington et al 2001][research_bruington_brenernan_2001]\] \[[Campbell and Goodman 1949][research_campbell_goodman_1949]\] \[[Cancro 1953][research_cancro_1953]\] \[[CFD Analysis of Boeing-737 3D Aerofoil and Adverse YAW on 2017][research_cfd_analysis_of_2017]\] \[[Chen et al 2026][research_chen_2026_3]\] \[[Childress 1958][research_childress_1958]\] \[[Christophersen and Spahr 1944][research_christophersen_spahr_1944]\] \[[Claudia Alice 2010][research_claudiaalice_2010]\] \[[Cliff and Lutze 1972][research_cliff_lutze_1972]\] \[[Cobleigh 1994][research_cobleigh_1994]\] \[[Crandall 1943][research_crandall_1943]\] \[[Crane and Holtzclaw 1944][research_crane_holtzclaw_1944]\] \[[David and Seifert 2012][research_david_seifert_2012]\] \[[Davis 1957][research_davis_1957]\] \[[De Gaspari and Mantegazza 2024][research_de_gaspari_mantegazza_2024]\] \[[Dennis and Scherrer 1951][research_dennis_scherrer_1951]\] \[[Deters and Russell 1947][research_deters_russell_1947]\] \[[Deters and Russell 1947, Investigation of the Aileron and][research_deters_russell_1947_2]\] \[[Di Donato et al 2017][research_di_donato_2017]\] \[[Duerksen 1997][research_duerksen_1997]\] \[[Eggleston and Diederich 1957][research_eggleston_diederich_1957]\] \[[El-Ramly et al 1976][research_el_ramly_1976]\] \[[Ellerbroek et al 2007][research_ellerbroek_stroosma_2007]\] \[[Ellis 1972][research_ellis_1972]\] \[[Esparza 1975][research_esparza_1975]\] \[[Failure of an Aileron Control Cable in an Aircraft 2005][research_failure_of_2005]\] \[[Fehlner 1942][research_fehlner_1942]\] \[[Fischel and Schneiter 1947][research_fischel_schneiter_1947]\] \[[Fournier and Silvers 1958][research_fournier_silvers_1958]\] \[[Graham 1945][research_graham_1945]\] \[[Gregorek 1984][research_gregorek_1984]\] \[[Gregorek 1995][research_gregorek_1995]\] \[[Guo et al 2020][research_guo_2020]\] \[[Hall and Boothe 1972][research_hall_boothe_1972]\] \[[Hall and Mason 2012][research_hall_mason_2012]\] \[[Hammond and Henderson 1961][research_hammond_henderson_1961]\] \[[Haque et al 2016][research_haque_asrar_2016]\] \[[Harman 1944][research_harman_1944]\] \[[Helicopter Yaw Control 1990][research_helicopter_yaw_1990]\] \[[Higgins and Jacobs 1928][research_higgins_jacobs_1928]\] \[[Hoholis et al 2016][research_hoholis_2016]\] \[[Hopkins and Lovette 1977][research_hopkins_lovette_1977]\] \[[Hu et al 2025][research_hu_2025]\] \[[Huang and Wu 2006][research_huang_wu_2006]\] \[[Hunsaker et al 2019][research_hunsaker_moorthamers_2019]\] \[[Hunsaker et al 2020][research_hunsaker_2020]\] \[[Hunsaker et al 2020][research_hunsaker_montgomery_2020]\] \[[Hunsaker et al 2021][research_hunsaker_moorthamers_2021]\] \[[Huzita 1971][research_huzita_1971]\] \[[Ivey 1945][research_ivey_1945]\] \[[Jacobs 1983][research_jacobs_1983]\] \[[Jacobs and Bartlett 1981][research_jacobs_bartlett_1981]\] \[[James and Vaughn 1976][research_james_vaughn_1976]\] \[[Jayalakshmi et al 2021][research_jayalakshmi_patel_2021]\] \[[Jennings 1931][research_jennings_1931]\] \[[Jeong et al 2015][research_jeong_2015]\] \[[Jiang 1999][research_jiang_1999]\] \[[Jiang et al 2000][research_jiang_an_2000]\] \[[Johnson and Hagerman 1950][research_johnson_hagerman_1950]\] \[[Johnson and Sternfield 1948][research_johnson_sternfield_1948]\] \[[Kelley and Enevoldson 1981][research_kelley_enevoldson_1981]\] \[[Kelly and Brown 1980][research_kelly_brown_1980]\] \[[Kemp 1943][research_kemp_1943]\] \[[Kigotho et al 2022][research_kigotho_bodylski_2022]\] \[[Kohlman 1977][research_kohlman_1977]\] \[[Kou et al 2021][research_kou_2021]\] \[[Kowalska and Goetzendorf-Grabowski 2022][research_kowalska_goetzendorfgrabowski_2022]\] \[[Krishnan et al 2020][research_krishnan_2020]\] \[[Levy 1992][research_levy_1992]\] \[[Li and Yang 2017][research_li_yang_2017_2]\] \[[Li and Yang 2017][research_li_yang_2017]\] \[[Li et al 2022][research_li_2022]\] \[[Lovell and Stassi 1950][research_lovell_stassi_1950]\] \[[Luoma 1944][research_luoma_1944]\] \[[Ma et al 2023][research_ma_abouhamzeh_2023]\] \[[MACKlNNON and Madden 1972][research_macklnnon_madden_1972]\] \[[Mao and Zhao 1990][research_mao_zhao_1990]\] \[[Andino et al][research_marlyn_andino]\] \[[Martina 1953][research_martina_1953]\] \[[Martina 1954][research_martina_1954]\] \[[Masud et al 2016][research_masud_malik_2016]\] \[[McKee 1943][research_mckee_1943]\] \[[McLaughlin and Shaw][research_mclaughlin_shaw]\] \[[Molchanov 1981][research_molchanov_1981]\] \[[Moore and Moore 2012][research_moore_moore_2012]\] \[[Moore and Moore 2012][research_moore_moore_2012_b]\] \[[Moul and Brown 1979][research_moul_brown_1979]\] \[[Munk 1925][research_munk_1925]\] \[[Murray and Warren 1944][research_murray_warren_1944]\] \[[Myala et al 2020][research_myala_2020]\] \[[National Advisory Committee for Aeronautics report No. 570. The effect of lateral controls in producing motion of an airplane as computed from wind-tunnel data 1937][research_national_advisory_1937]\] \[[National advisory committee for aeronautics: Report No. 424, Wind-tunnel research comparing lateral control devices, particularly at high angles of attack. IV. Floating tip ailerons on rectangular wings 1932][research_national_advisory_1932]\] \[[Nazarenko and Nevezhina 1972][research_nazarenko_nevezhina_1972]\] \[[ODonnell and Mohseni 2019][research_odonnell_mohseni_2019]\] \[[Ogawara et al 2024][research_ogawara_2024]\] \[[Pamadi and Pai 1980][research_pamadi_pai_1980]\] \[[Paulson 1976][research_paulson_1976]\] \[[Pearson 1937][research_pearson_1937]\] \[[Phillips 1942][research_phillips_1942]\] \[[Platt and Shortal 1937][research_platt_shortal_1937]\] \[[Purser 1941][research_purser_1941]\] \[[Qian et al 2022][research_qian_2022]\] \[[Qin et al 2014][research_qin_wang_2014]\] \[[Qiu and Ang 2019][research_qiu_ang_2019]\] \[[Qu et al 2017][research_qu_2017]\] \[[MacLeod 1952][research_r_g_macleod_1952]\] \[[R. 1935][research_r_1935]\] \[[Radetskaya 2022][research_radetskaya_2022]\] \[[Rao 1992][research_rao_1992]\] \[[Rao et al 1987][research_rao_1987]\] \[[Report No. 423, Wind-tunnel 1932, Report No. 423, Wind-tunnel][research_report_no_1932_3]\] \[[Report No. 439, Wind-Tunnel 1932, Report No. 439, Wind-Tunnel][research_report_no_1932_2]\] \[[Report No. 444, Wind-Tunnel 1932, Report No. 444, Wind-Tunnel][research_report_no_1932]\] \[[Report no. 510, wind-tunnel 1935, Report no. 510, wind-tunnel][research_report_no_1935]\] \[[Robert C Platt 1935][research_robert_c_platt_1935]\] \[[Rosenberg 1944][research_rosenberg_1944]\] \[[Sachs and Moelyadi 2006][research_sachs_moelyadi_2006]\] \[[Sandu et al 2025][research_sandu_2025]\] \[[Schneiter and Watson 1948][research_schneiter_watson_1948]\] \[[Sekaran 1983][research_sekaran_1983]\] \[[Shankar and Yathisha 2023][research_shankar_l_2023]\] \[[Shearwood et al 2020][research_shearwood_2020]\] \[[Shmilovich et al 2023][research_shmilovich_yadlin_2023]\] \[[Shmilovich et al 2026][research_shmilovich_2026]\] \[[Shortal 1934][research_shortal_1934]\] \[[Sinkovec et al 2015][research_sinkovec_loshek_2015]\] \[[Sohail et al 2011][research_sohail_muhammad_2011]\] \[[Soinne 1999][research_soinne_1999]\] \[[Soule and Wetmore 1933][research_soule_wetmore_1933]\] \[[Spearman and Webster 1951][research_spearman_webster_1951]\] \[[Stewart 1939][research_stewart_1939]\] \[[Stewart 2008][research_stewart_2008]\] \[[Tavella et al 1987][research_tavella_1987]\] \[[Tay et al 2025][research_tay_chong_2025]\] \[[The Pearson Rotary Aileron 1930][research_the_pearson_1930]\] \[[The Simplification of Lateral Control 1936][research_the_simplification_1936]\] \[[Toll 1943][research_toll_1943]\] \[[Underwood 1942, Aerodynamic Characteristics for][research_underwood_1942]\] \[[Vechtel and Buch 2022][research_vechtel_buch_2022]\] \[[Venkataraman and Seiler 2019][research_venkataraman_seiler_2019]\] \[[Wang et al 2013][research_wang_qin_2013]\] \[[Wei et al 2017][research_wei_2017]\] \[[Weick and Harris 1933][research_weick_harris_1933]\] \[[Weick and Harris 1934][research_weick_harris_1934]\] \[[Weick and Jones 1937][research_weick_jones_1937]\] \[[Weick and Jones 1976][research_weick_jones_1976]\] \[[Weick and Noyes 1933][research_weick_noyes_1933]\] \[[Weick and Noyes 1933][research_weick_noyes_1933_2]\] \[[Weick and Shortal 1933][research_weick_shortal_1933]\] \[[Weick and Shortal 1935][research_weick_shortal_1935]\] \[[Weick and Wenzinger 1935][research_weick_wenzinger_1935]\] \[[Weisshaar 1977][research_weisshaar_1977]\] \[[Weisshaar 1990][research_weisshaar_1990]\] \[[Wenzinger and Bamber 1938][research_wenzinger_bamber_1938]\] \[[Wenzinger and Rogallo 1941][research_wenzinger_rogallo_1941]\] \[[Whitaker 1975][research_whitaker_1975]\] \[[Whiting 1996][research_whiting_1996]\] \[[Wiley 1954][research_wiley_1954]\] \[[Wiley and Taylor 1954][research_wiley_taylor_1954]\] \[[Wu et al 2020][research_wu_2020_3]\] \[[Xiong et al 2025][research_xiong_2025]\] \[[Yan et al 2024][research_yan_2024]\] \[[Yeo et al 2015][research_yeo_2015]\] \[[Zhang et al 2013][research_zhang_yu_2013]\] \[[Zuhri 2025][research_zuhri_2025]\]

### Sailplanes, gliders and soaring

Sailplanes, gliders, motor gliders and soaring flight, including the design, performance and flight test of sailplanes and the dynamic soaring of unmanned aircraft.

**The sailplane is a research instrument in its own right.** The cluster includes sailplanes used for boundary layer, turbulence and post-stall research, and a record on teaching flight testing through soaring.

**178 records.** \[[A sailplane wing constructed of foam core and polyester 1974][research_a_sailplane_1974]\] \[[Achleitner et al 2019][research_achleitner_rohdebrandenburger_2019]\] \[[Aero structural optimization for sailplane wing in preliminary design 2018][research_aero_structural_2018]\] \[[Allen 2006][research_allen_2006]\] \[[Allen 2007][research_allen_2007]\] \[[Allen 2007][research_allen_2007_2]\] \[[Amalia et al 2018][research_amalia_2018]\] \[[Amalia et al 2019][research_amalia_2019]\] \[[An evaluation of sailplane drag coefficient parameters from 1974][research_an_evaluation_1974]\] \[[Anderle et al 2003][research_anderle_smrcek_2003]\] \[[Axten and Maughmer 2020][research_axten_maughmer_2020]\] \[[Axten et al 2024][research_axten_chidekel_2024]\] \[[Barnes 2015][research_barnes_2015]\] \[[Bennett 1978][research_bennett_1978]\] \[[Bennett et al 1974][research_bennett_owens_1974]\] \[[Bonnin][research_bonnin]\] \[[Bonnin et al 2013][research_bonnin_toomer_2013]\] \[[Boyer 1908][research_boyer_1908]\] \[[Bozack 1984][research_bozack_1984]\] \[[Bramesfeld and Maughmer 2002][research_bramesfeld_maughmer_2002]\] \[[Brodsky and Luby 2013][research_brodsky_luby_2013]\] \[[Brown 1954][research_brown_1954]\] \[[Bucur and Lupuleasa 2026][research_bucur_lupuleasa_2026]\] \[[Budd and Monheim 2015][research_budd_monheim_2015]\] \[[Cao 2023][research_cao_2023]\] \[[Chen][research_chen]\] \[[Cheng and Langelaan 2014][research_cheng_langelaan_2014]\] \[[Chick et al 2023][research_chick_cornwellarquitt_2023]\] \[[Collazo Garcia et al 2019][research_collazogarcia_ranjan_2019]\] \[[Colling 1995][research_colling_1995]\] \[[Computational Simulation of F3F Glider Flight Performance: Applied Research on Composite Material Optimization Design 2025][research_computational_simulation_2025]\] \[[Czarnocki et al 2019][research_czarnocki_dudek_2019]\] \[[Guido 1991][research_d_1991]\] \[[d and de Socio 1999][research_d_desocio_1999]\] \[[d and Menichetti 2000][research_d_menichetti_2000]\] \[[Dandwani et al 2025][research_dandwani_bragadoaldana_2025]\] \[[de Matteis and Tamilia 1993][research_dematteis_tamilia_1993]\] \[[Dees 2010][research_dees_2010]\] \[[Dees 2013][research_dees_2013]\] \[[Deittert et al 2009][research_deittert_richards_2009]\] \[[Demircali and Uvet 2017][research_demircali_uvet_2017]\] \[[Demircali and Uvet 2018][research_demircali_uvet_2018]\] \[[Deprez 1908][research_deprez_1908]\] \[[Dubnický et al 2023][research_dubnicky_splichal_2023]\] \[[Dudek et al 2020][research_dudek_2020]\] \[[Dutta 2026][research_dutta_2026]\] \[[Edwards 2015][research_edwards_2015]\] \[[Erb et al 2009][research_erb_aldrich_2009]\] \[[Genalo][research_genalo]\] \[[Genalo and Pierson 1978][research_genalo_pierson_1978]\] \[[Gliding and Soaring Flight 1938][research_gliding_and_1938]\] \[[Grossman et al 1986][research_grossman_gurdal_1986]\] \[[Göksel][research_goksel]\] \[[Heinrich et al 1964][research_heinrich_nietz_1964]\] \[[Horstmann and Quast 1980][research_horstmann_quast_1980]\] \[[Huang et al 2006][research_huang_pippalapalli_2006]\] \[[Instruments for Soaring Flight 1999][research_instruments_for_1999]\] \[[Irving 1999][research_irving_1999]\] \[[Janzen and Precourt 1989][research_janzen_precourt_1989]\] \[[Johnson 1949][research_johnson_1949]\] \[[Kakade et al 2022][research_kakade_chikkala_2022]\] \[[Kehoe and Ellison 1985][research_kehoe_ellison_1985]\] \[[Kensche 2003][research_kensche_2003]\] \[[Kentfield 2012][research_kentfield_2012]\] \[[Keskin et al 2021][research_keskin_2021]\] \[[Klemin and Walling 1943][research_klemin_walling_1943]\] \[[Kochersberger et al 2003][research_kochersberger_player_2003]\] \[[Koessler 2018][research_koessler_2018]\] \[[Kohne et al 2024][research_kohne_korzilius_2024]\] \[[Krebs and Bramesfeld 2016][research_krebs_bramesfeld_2016]\] \[[Krebs and Bramesfeld 2017][research_krebs_bramesfeld_2017]\] \[[Kroo 2000][research_kroo_2000]\] \[[Kubrynski 2012][research_kubrynski_2012]\] \[[Kuettner 1952][research_kuettner_1952]\] \[[Kulhánek 2019][research_kulhanek_2019]\] \[[Kumar et al 2026][research_kumar_mathi_2026]\] \[[Kuźniar and Orkisz 2019][research_kuzniar_orkisz_2019]\] \[[Ladeira et al 2024][research_ladeira_2024]\] \[[Lamp and Luckner 2013][research_lamp_luckner_2013]\] \[[Larrabee 1974][research_larrabee_1974]\] \[[Lauk and Unt 2015][research_lauk_unt_2015]\] \[[Lauk et al 2017][research_lauk_seegel_2017]\] \[[le Roux et al 2025][research_leroux_bosman_2025]\] \[[Lendraitis 2019][research_lendraitis_2019]\] \[[Lin 2007][research_lin_2007]\] \[[Lindstedt et al 2019][research_lindstedt_2019]\] \[[Lippisch 1930][research_lippisch_1930]\] \[[Lippisch 1935][research_lippisch_1935]\] \[[Lorenz 1985][research_lorenz_1985]\] \[[Lundberg 1937][research_lundberg_1937]\] \[[Lundberg 1938][research_lundberg_1938]\] \[[Lupp and Cesnik 2015][research_lupp_cesnik_2015]\] \[[MacCready 1962][research_maccready_1962]\] \[[Madelung 1923][research_madelung_1923]\] \[[Marsden 1974][research_marsden_1974]\] \[[Maughmer][research_maughmer]\] \[[Maughmer 2003][research_maughmer_2003]\] \[[Maughmer et al 2024][research_maughmer_metkowski_2024]\] \[[McMasters 1979][research_mcmasters_1979]\] \[[McMasters and Palmer 1975][research_mcmasters_palmer_1975]\] \[[Metzger 1974][research_metzger_1974]\] \[[Miller 1985][research_miller_1985_b]\] \[[Mulyanto and Zulkarnain 2020][research_mulyanto_zulkarnain_2020]\] \[[Mulyanto and Zulkarnain 2021][research_mulyanto_zulkarnain_2021]\] \[[Muser 1979][research_muser_1979]\] \[[Nash-Webber 1973][research_nash_webber_1973]\] \[[Neto and Signor 2023][research_neto_signor_2023]\] \[[Oliveira et al 2021][research_oliveira_payne_2021]\] \[[Orkisz et al 2019][research_orkisz_wygonik_2019]\] \[[Pfeiffer 2017][research_pfeiffer_2017]\] \[[Pierson 1977][research_pierson_1977]\] \[[Pierson and Chen 1979, Minimum Altitude-Loss Soaring in][research_pierson_chen_1979]\] \[[Pierson and Chen 1979][research_pierson_chen_1979_2]\] \[[Pierson and De Jong 1978][research_pierson_dejong_1978]\] \[[Pilcher 2021][research_pilcher_2021]\] \[[Poznanski et al 2025][research_poznanski_mays_2025]\] \[[Puttur and Layng 2025][research_puttur_layng_2025]\] \[[Raffel et al 2019][research_raffel_2019]\] \[[Ramšak 2012][research_ramsak_2012]\] \[[Range et al 2013][research_range_werner_2013]\] \[[Raspet 1952][research_raspet_1952]\] \[[Raspet 1955][research_raspet_1955]\] \[[Reeder 1959][research_reeder_1959]\] \[[Report No. 434. Lift 1932, Report No. 434. Lift and drag][research_report_no_1932_5]\] \[[Reussner 1950][research_reussner_1950]\] \[[Reussner 1953][research_reussner_1953]\] \[[Hoey 1992][research_robert_g_hoey_1992]\] \[[Romadhon et al 2024][research_romadhon_2024]\] \[[Rosales et al 2021][research_rosales_guijarroreyes_2021]\] \[[Sachs and da Costa 2003][research_sachs_dacosta_2003]\] \[[Sachs and Grüter 2017][research_sachs_gruter_2017]\] \[[Sachs et al 2013][research_sachs_lenz_2013]\] \[[Sakamoto and Cota 1965][research_sakamoto_cota_1965]\] \[[Sakamoto et al 2007][research_sakamoto_takemura_2007]\] \[[Sampaio et al 2014][research_sampaio_hernandes_2014]\] \[[Sandlin and Saiki 1993][research_sandlin_saiki_1993]\] \[[Satuluri and Seeni 2022][research_satuluri_seeni_2022]\] \[[Schreder 1975][research_schreder_1975]\] \[[Scientific and Technical Aspects of Soaring Flight 1952][research_scientific_and_1952]\] \[[Shenstone 1938][research_shenstone_1938]\] \[[Shenstone 1946][research_shenstone_1946]\] \[[Shenstone 1953][research_shenstone_1953]\] \[[Shrey. J. Mistry et al. 2018][research_shrey_j_mistry_et_al_2018]\] \[[Silvestre 2013][research_silvestre_2013]\] \[[Sim 1990][research_sim_1990]\] \[[Sinha and Ravande 2006][research_sinha_ravande_2006]\] \[[Slater 1955][research_slater_1955]\] \[[Sliwa and Sliwa 1979][research_sliwa_sliwa_1979]\] \[[Somers 1977][research_somers_1977]\] \[[Somers 1981][research_somers_1981]\] \[[Somers and Foster 1979][research_somers_foster_1979]\] \[[Stewart 2016][research_stewart_2016]\] \[[Suzuki and Kawamura 1995][research_suzuki_kawamura_1995]\] \[[Suzuki and Kawamura 1996][research_suzuki_kawamura_1996]\] \[[Swaminathan and Mohan 2018][research_swaminathan_mohan_2018]\] \[[Taylor 2011][research_taylor_2011]\] \[[Tetlow 1983][research_tetlow_1983]\] \[[The DRAG of a Sailplane 1999][research_the_drag_1999]\] \[[The Sailplane as a meteorological probe 1948][research_the_sailplane_1948]\] \[[The Sailplane in the Atmosphere 1999][research_the_sailplane_1999]\] \[[Thomas 2003][research_thomas_2003]\] \[[Turner 1942][research_turner_1942]\] \[[Turriziani 1979][research_turriziani_1979]\] \[[Vilchis Medina et al 2018][research_vilchismedina_siegel_2018]\] \[[Vilchis Medina et al 2019][research_vilchismedina_siegel_2019]\] \[[Voß and Ohme 2018][research_voss_ohme_2018]\] \[[Ward and Bennett 1974][research_ward_bennett_1974]\] \[[Wei et al 2022][research_wei_2022]\] \[[Welch 1995][research_welch_1995]\] \[[Wiggi 1949][research_wiggi_1949]\] \[[Wilk 2024][research_wilk_2024]\] \[[Wilkinson 1954][research_wilkinson_1954]\] \[[Wolek et al 2016][research_wolek_2016]\] \[[Yamin and Giyats 2022][research_yamin_giyats_2022]\] \[[Yates 1949][research_yates_1949]\] \[[Yu 2026][research_yu_2026]\] \[[Zhang et al 2011][research_zhang_millane_2011]\] \[[Zhao 2025][research_zhao_2025]\]

### Flying and handling qualities

Flying and handling qualities, their criteria and specifications, pilot rating and the course texts of the test pilot schools.

**160 records.** \[[Adams and Hatch 1971][research_adams_hatch_1971]\] \[[AHarrah and Lockenour 1971][research_a_harrah_lockenour_1971]\] \[[Air Force Test Pilot School Edwards Afb Ca 1969][research_air_force_test_pilot_school_edwards_afb_ca_1969]\] \[[Air Force Test Pilot School Edwards Afb Ca 1981][research_air_force_test_pilot_school_edwards_afb_ca_1981]\] \[[Air Force Test Pilot School Edwards Afb Ca 1988][research_air_force_test_pilot_school_edwards_afb_ca_1988]\] \[[Air Force Test Pilot School Edwards Afb Ca 1988][research_air_force_test_pilot_school_edwards_afb_ca_1988_2]\] \[[Air Force Test Pilot School Edwards Afb Ca 1988][research_air_force_test_pilot_school_edwards_afb_ca_1988_3]\] \[[Air Force Test Pilot School Edwards Afb Ca 1988][research_air_force_test_pilot_school_edwards_afb_ca_1988_4]\] \[[Air Force Test Pilot School Edwards Afb Ca 1988][research_air_force_test_pilot_school_edwards_afb_ca_1988_5]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_air_force_test_pilot_school_edwards_afb_ca_1990_3]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_air_force_test_pilot_school_edwards_afb_ca_1990_4]\] \[[Air Force Test Pilot School Edwards Afb Ca 1991][research_air_force_test_pilot_school_edwards_afb_ca_1991]\] \[[Air Force Test Pilot School Edwards Afb Ca 1991][research_air_force_test_pilot_school_edwards_afb_ca_1991_2]\] \[[Air Force Test Pilot School Edwards Afb Ca 1992][research_air_force_test_pilot_school_edwards_afb_ca_1992]\] \[[Aircraft longitudinal handling qualities design 2011][research_aircraft_longitudinal_2011]\] \[[Alexander 2025][research_alexander_2025]\] \[[Anderson 1960][research_anderson_1960]\] \[[Anderson 1970][research_anderson_1970]\] \[[Antonakis 2025][research_antonakis_2025]\] \[[Antonakis 2025][research_antonakis_2025_2]\] \[[Ashkenas 1971][research_ashkenas_1971]\] \[[Ashkenas 1984][research_ashkenas_1984]\] \[[Bachelder and Aponso 2020][research_bachelder_aponso_2020]\] \[[Bahr et al 2021][research_bahr_2021]\] \[[Bailes et al 1975][research_bailes_1975]\] \[[Baughman and Longeauay 2015][research_baughman_longeauay_2015]\] \[[Bechelder et al 2025][research_bechelder_bjorkman_2025]\] \[[Berger et al 2022][research_berger_2022_2]\] \[[Berger et al 2022][research_berger_2022]\] \[[Berger et al 2025][research_berger_christensen_2025]\] \[[Berry et al 1976][research_berry_1976]\] \[[Bischoff 1983][research_bischoff_1983]\] \[[Black and Moorhouse 1979][research_black_moorhouse_1979]\] \[[Blackburn 1968][research_blackburn_1968]\] \[[Boeing Vertol Co Philadelphia Pa 1983][research_boeing_vertol_co_philadelphia_pa_1983]\] \[[Boothe et al 1974][research_boothe_1974]\] \[[Bowes and Miller 1976][research_bowes_miller_1976]\] \[[Breul 1963][research_breul_1963]\] \[[Brewer 1946][research_brewer_1946]\] \[[Campos and Marques 2021][research_campos_marques_2021]\] \[[Carpenter 1970][research_carpenter_1970]\] \[[Chalk 1964][research_chalk_1964]\] \[[Chalk and Wilson 1969][research_chalk_wilson_1969]\] \[[Chance Vought Corp Dallas Tx 1979][research_chance_vought_corp_dallas_tx_1979]\] \[[Chowhan et al 2019][research_chowhan_2019]\] \[[Clark 1982][research_clark_1982]\] \[[Cooper and Harper 1969][research_cooper_harper_1969]\] \[[Crombie and Moorhouse 1980][research_crombie_moorhouse_1980]\] \[[Crother et al 1973][research_crother_1973]\] \[[Curry et al 1965][research_curry_1965]\] \[[Daughaday and Duwaldt 1955][research_daughaday_duwaldt_1955]\] \[[Difranco 1970][research_difranco_1970]\] \[[DiFranco 1971][research_difranco_1971]\] \[[Doman 1995][research_doman_1995]\] \[[Dussart et al 2019][research_dussart_2019_2]\] \[[Edwards et al 1997][research_edwards_1997]\] \[[Eney 1968][research_eney_1968]\] \[[Ford 1989][research_ford_1989_2]\] \[[Franklin 1972][research_franklin_1972]\] \[[Franklin et al 1988][research_franklin_1988]\] \[[Gallagher 1971][research_gallagher_1971]\] \[[Garkushenko and Vinogradov 2016][research_garkushenko_vinogradov_2016]\] \[[Gerken 1979][research_gerken_1979]\] \[[Giles 1972][research_giles_1972]\] \[[Goldstein 1982][research_goldstein_1982]\] \[[Gray 1964][research_gray_1964]\] \[[Gray 2009][research_gray_2009]\] \[[Gray and Kemper 2009][research_gray_kemper_2009]\] \[[Green 1988][research_green_1988]\] \[[Griffin and Bellaire 1968][research_griffin_bellaire_1968]\] \[[Hall et al 1974][research_hall_1974]\] \[[Handling qualities 2000][research_handling_qualities_2000]\] \[[Handling Qualities Analysis 2008][research_handling_qualities_2008]\] \[[Harper and Robert P. 1955][research_harper_robert_p_1955]\] \[[Harper and Sardanowsky 1969][research_harper_sardanowsky_1969]\] \[[Harris et al 1985][research_harris_1985]\] \[[Hebbar and Pashilkar 2016][research_hebbar_pashilkar_2016]\] \[[Helicopter Handling Qualities 1982][research_helicopter_handling_1982]\] \[[Henriquez Huecas et al 2022][research_henriquez_huecas_2022]\] \[[Hess 2016][research_hess_2016]\] \[[Higgins and Shomber 1965][research_higgins_shomber_1965]\] \[[Hoh and Mitchell 1983][research_hoh_mitchell_1983]\] \[[Hoh et al 1981][research_hoh_1981]\] \[[Holleman and Gilyard 1972][research_holleman_gilyard_1972]\] \[[Huff 1949][research_huff_w_w_1949]\] \[[Humphreys-Jennings et al 2020][research_humphreys_jennings_2020]\] \[[Ioannis and Ioannis 2026][research_ioannis_ioannis_2026]\] \[[Ivler et al 2022][research_ivler_2022]\] \[[Jackson et al 1993][research_jackson_1993]\] \[[Jacobson and Joshi 1977][research_jacobson_joshi_1977]\] \[[Jacobson and Joshi 1978][research_jacobson_joshi_1978]\] \[[Jewell et al 1979][research_jewell_1979]\] \[[Ji et al 2017][research_ji_2017]\] \[[Ji et al 2022][research_ji_2022]\] \[[Ham et al 1993][research_johnnie_a_ham_1993]\] \[[Johnston et al 1965][research_johnston_1965_2]\] \[[Johnston et al 1974][research_johnston_1974]\] \[[Key 1971][research_key_1971]\] \[[Key 1982][research_key_1982]\] \[[Kidd and Bull 1963][research_kidd_bull_1963]\] \[[Kier et al 1972][research_kier_1972]\] \[[Kozhanov et al 2022][research_kozhanov_2022]\] \[[Kriechbaum and Stineman 1972][research_kriechbaum_stineman_1972]\] \[[Lampton et al 2024][research_lampton_2024]\] \[[Lee et al 2020][research_lee_2020_2]\] \[[Levi and Nelson 1964][research_levi_nelson_1964]\] \[[Levison 1982][research_levison_1982]\] \[[Lusardi 2023][research_lusardi_2023]\] \[[Malcom 1969][research_malcom_1969]\] \[[Malpica and Lusardi 2013][research_malpica_lusardi_2013]\] \[[Mandal and Gu 2016][research_mandal_gu_2016]\] \[[McCormick 1969][research_mccormick_1969]\] \[[McGREGOR and Smith 1966][research_mcgregor_smith_1966]\] \[[Michael Feary][research_michael_feary]\] \[[Miller 1970][research_miller_1970]\] \[[Miller and Clark 1965][research_miller_clark_1965]\] \[[Mitcham 1949][research_mitcham_1949]\] \[[Mitchell et al 2003][research_mitchell_2003]\] \[[Momiyama 1977][research_momiyama_1977]\] \[[Mooij 1985][research_mooij_1985_c]\] \[[Mooij 1985][research_mooij_1985_b]\] \[[Mooij 1985][research_mooij_1985]\] \[[Nagata et al 1973][research_nagata_1973]\] \[[Nagy and Kirsten 1976][research_nagy_kirsten_1976]\] \[[Neal and Smith 1971][research_neal_smith_1971]\] \[[Ogburn and Brown 1980][research_ogburn_brown_1980]\] \[[Pauli et al 1974][research_pauli_corliss_1974]\] \[[Zaal et al][research_peter_zaal]\] \[[Place et al 1974][research_place_1974]\] \[[Ranaudo et al 2000][research_ranaudo_2000]\] \[[Reeder 1958][research_reeder_1958]\] \[[Rhoads 1967][research_rhoads_1967]\] \[[Riccardi et al 2025][research_riccardi_mamino_2025]\] \[[Robert E Lee 2005][research_robert_e_lee_2005]\] \[[Rohling 1969][research_rohling_1969]\] \[[Rotorcraft handling qualities design 2011][research_rotorcraft_handling_2011]\] \[[Saetti and Rogers 2020][research_saetti_rogers_2020]\] \[[Saucez][research_saucez]\] \[[Shomber and Gertsen 1967][research_shomber_gertsen_1967]\] \[[Shubert and Jones 2025][research_shubert_jones_2025]\] \[[Smith 1977][research_smith_1977]\] \[[Smith 2023][research_smith_2023]\] \[[Smith and Geddes 1979][research_smith_geddes_1979]\] \[[Solies 1995][research_solies_1995]\] \[[Srinathkumar 2015][research_srinathkumar_2015]\] \[[Stoliker and Bosworth 1996][research_stoliker_bosworth_1996]\] \[[Sun et al 2020][research_sun_2020_2]\] \[[Tapscott 1964][research_tapscott_1964]\] \[[Tritschler and OConnor 2016][research_tritschler_oconnor_2016]\] \[[Van Dam 1981][research_van_dam_1981]\] \[[Van Dam et al 1980][research_van_dam_1980]\] \[[van Dam et al 1981][research_van_dam_1981_2]\] \[[Walsh 1993][research_walsh_1993]\] \[[Walter et al 2022][research_walter_2022]\] \[[Wang et al 2025][research_wang_2025]\] \[[Wanner 1973][research_wanner_1973]\] \[[Whitbeck and Hofmann 1978][research_whitbeck_hofmann_1978]\] \[[Wilhelm and Schafranek 1986][research_wilhelm_schafranek_1986]\] \[[Wilson et al 1993][research_wilson_1993]\] \[[Yan 2017][research_yan_2017]\]

### Lateral-directional stability, roll damping and coupling

Static and dynamic lateral-directional stability, roll damping, sideslip, Dutch roll and the coupling of roll and yaw. **42 of the 153 records date from before 1970.**

**153 records.** \[[Abdul Rashid et al 2025][research_abdul_rashid_2025]\] \[[Adams 1976][research_adams_1976]\] \[[Air Force Test Pilot School Edwards Afb Ca 1989][research_air_force_test_pilot_school_edwards_afb_ca_1989]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_air_force_test_pilot_school_edwards_afb_ca_1990_5]\] \[[Aircraft lateral-directional handling qualities design 2011][research_aircraft_lateral_directional_2011]\] \[[Akishita et al 1986][research_akishita_1986]\] \[[Albostan and Gökaşan 2018][research_albostan_gokasan_2018]\] \[[Alston 1936][research_alston_1936]\] \[[Ananthkrishnan and Sinha 2023][research_ananthkrishnan_sinha_2023]\] \[[Arabian and Schmeer 1955][research_arabian_schmeer_1955]\] \[[Ashkenas 1965][research_ashkenas_1965]\] \[[Ashkenas 1965][research_ashkenas_1965_2]\] \[[Bailey et al 1988][research_bailey_1988]\] \[[Baker 1948][research_baker_1948]\] \[[Banerjee et al 2017][research_banerjee_2017]\] \[[Bian et al 2019][research_bian_2019]\] \[[Bird and Jaquet 1951][research_bird_jaquet_1951]\] \[[Bird et al 1952][research_bird_1952]\] \[[Bischoff and Palmer 1983][research_bischoff_palmer_1983]\] \[[Boyden 1971][research_boyden_1971]\] \[[Bradley 1975][research_bradley_1975]\] \[[Brown 1981][research_brown_1981]\] \[[Brown and Adams 1948][research_brown_adams_1948]\] \[[Brown and Heinke 1956][research_brown_heinke_1956]\] \[[Burken et al 1996][research_burken_1996]\] \[[Burt 1975][research_burt_1975]\] \[[Butler 1976][research_butler_1976_2]\] \[[Butler and Langham 1978][research_butler_langham_1978]\] \[[Calloway 1983][research_calloway_1983]\] \[[Chalk 1983][research_chalk_1983]\] \[[Chambers 1966][research_chambers_1966]\] \[[Chevalier and Burke 1972][research_chevalier_burke_1972]\] \[[Ciliberti and Nicolosi 2025][research_ciliberti_nicolosi_2025]\] \[[Coe and Newsom 1974][research_coe_newsom_1974]\] \[[Coe et al 1975][research_coe_1975]\] \[[Coletti 1954][research_coletti_1954]\] \[[Crane and Reeder 1945][research_crane_reeder_1945]\] \[[Dahiya 2016][research_dahiya_2016]\] \[[Dahiya 2017][research_dahiya_2017]\] \[[Davari and Laitone 1977][research_davari_laitone_1977]\] \[[DeSanti 1988][research_desanti_1988]\] \[[Eastman 1986][research_eastman_1986]\] \[[Er-El et al 1989][research_er_el_1989]\] \[[Esteban et al 2015][research_esteban_2015]\] \[[Fajar and Arifianto 2018][research_fajar_arifianto_2018]\] \[[Fetterman and Penland 1960][research_fetterman_penland_1960]\] \[[Fink et al 1970][research_fink_1970]\] \[[Franklin 1971][research_franklin_1971]\] \[[Frierson et al 1978][research_frierson_1978]\] \[[Fu et al 2020][research_fu_2020]\] \[[Ganiev 1978][research_ganiev_1978]\] \[[Garcia-Baquero et al 2018][research_garcia_baquero_2018]\] \[[Gates and Sternfield 1950][research_gates_sternfield_1950]\] \[[Goglia and Arunkumar 1983][research_goglia_arunkumar_1983]\] \[[Grunwald 1961][research_grunwald_1961]\] \[[Gu 1986][research_gu_1986]\] \[[Gundry 1977][research_gundry_1977]\] \[[Guruswamy 2021][research_guruswamy_2021]\] \[[Guruswamy 2021][research_guruswamy_2021_2]\] \[[Hacker 1977][research_hacker_1977]\] \[[Hamel 1970][research_hamel_1970]\] \[[Hancock 1972][research_hancock_1972]\] \[[Hawks 1982][research_hawks_1982]\] \[[Healy et al 2022][research_healy_2022]\] \[[Hewes 1959][research_hewes_1959]\] \[[Higgins et al 2020][research_higgins_2020]\] \[[Hwang and Pi 1978][research_hwang_pi_1978]\] \[[Hwang and Pi 1979][research_hwang_pi_1979]\] \[[Iliff and Wang 1996][research_iliff_wang_1996]\] \[[Iliff and Wang 1997][research_iliff_wang_1997]\] \[[Iliff and Wang 1999][research_iliff_wang_1999]\] \[[Jenke 1976][research_jenke_1976]\] \[[Jeong et al 2024][research_jeong_2024]\] \[[Johnston et al 1965][research_johnston_1965]\] \[[Jones 1950][research_jones_1950_2]\] \[[Katz and Levin 1986][research_katz_levin_1986]\] \[[Khanna et al 2022][research_khanna_2022]\] \[[Kumar and Ghosh 2023][research_kumar_ghosh_2023]\] \[[Lichtenstein 1952][research_lichtenstein_1952]\] \[[Lichtenstein and Williams 1961][research_lichtenstein_williams_1961]\] \[[Linehan and Mohseni 2016][research_linehan_mohseni_2016]\] \[[Loomis and Porter 1965][research_loomis_porter_1965]\] \[[Lungu and Lungu 2015][research_lungu_lungu_2015]\] \[[Lungu and Lungu 2016][research_lungu_lungu_2016]\] \[[Lyu et al 2022][research_lyu_2022]\] \[[Ma et al 2019][research_ma_2019]\] \[[MACKlNNON and Madden 1972][research_macklnnon_madden_1972_2]\] \[[Malvestuto et al 1950][research_malvestuto_1950]\] \[[McNeill and Innis 1965][research_mcneill_innis_1965]\] \[[Meissner 1973][research_meissner_1973]\] \[[Miles 1952][research_miles_1952]\] \[[Miller and Franklin 1968][research_miller_franklin_1968]\] \[[Mitchell and Hoh 1984][research_mitchell_hoh_1984]\] \[[Mohamed and Joy 2021][research_mohamed_joy_2021]\] \[[Mohammadi Farhadi et al 2018][research_mohammadi_farhadi_2018]\] \[[Motyka and Hall 1973][research_motyka_hall_1973]\] \[[Murrieta-Mendoza et al 2016][research_murrieta_mendoza_2016]\] \[[Navaratna et al 2022][research_navaratna_2022]\] \[[Ni et al 2025][research_ni_2025]\] \[[Ogren et al 1974][research_ogren_1974]\] \[[Ohta et al 1979][research_ohta_1979]\] \[[Ohta et al 1982][research_ohta_1982]\] \[[Optimal Switching Techniques For Aircraft Lateral Dynamics 2019][research_optimal_switching_2019]\] \[[Pan and Huang 2019][research_pan_huang_2019]\] \[[Peron and Carpenter 1992][research_peron_carpenter_1992]\] \[[Petersen et al 1962][research_petersen_1962]\] \[[Polhamus and King 1949][research_polhamus_king_1949]\] \[[Posingies 1968][research_posingies_1968]\] \[[Price 1943][research_price_1943]\] \[[Putman 1969][research_putman_1969]\] \[[Rajeswari and Padma Suresh 2015][research_rajeswari_padma_suresh_2015]\] \[[Raney and Batterson 1989][research_raney_batterson_1989]\] \[[Rossow 1986][research_rossow_1986]\] \[[Sanghi et al 2024][research_sanghi_2024]\] \[[Schade et al 1952][research_schade_1952]\] \[[Scherrer and Dennis 1951][research_scherrer_dennis_1951]\] \[[Schieni et al 2024][research_schieni_2024]\] \[[Schy and Hannah 1977][research_schy_hannah_1977]\] \[[Schütte and Hummel 2023][research_schutte_hummel_2023]\] \[[Seckel and Graziani 1956][research_seckel_graziani_1956]\] \[[Sen et al 1987][research_sen_1987]\] \[[Shen et al 2021][research_shen_2021]\] \[[Shrivastava and Stengel 1989][research_shrivastava_stengel_1989]\] \[[Siddiqui et al 2023][research_siddiqui_2023]\] \[[Snell 1993][research_snell_1993]\] \[[Snell et al 1991][research_snell_1991]\] \[[Sommer and Tapscott 1966][research_sommer_tapscott_1966]\] \[[Sponder 1950][research_sponder_1950]\] \[[Stengel 1975][research_stengel_1975]\] \[[Stengel 1980][research_stengel_1980]\] \[[Sternfield 1954][research_sternfield_1954]\] \[[Stone 1945][research_stone_1945]\] \[[Suarez et al 1993][research_suarez_1993]\] \[[Suit and Batterson 1986][research_suit_batterson_1986]\] \[[Swarnkar and Kothari 2016][research_swarnkar_kothari_2016]\] \[[Szalai 1967][research_szalai_1967]\] \[[Sánchez et al 2024][research_sanchez_2024]\] \[[Tai et al 2023][research_tai_2023]\] \[[Tai et al 2025][research_tai_2025]\] \[[Teper and Stapleford 1966][research_teper_stapleford_1966]\] \[[Tobak and Schiff 1975][research_tobak_schiff_1975]\] \[[van Gool 1982][research_van_gool_1982]\] \[[van Rooyen and Eshelby 1981][research_van_rooyen_eshelby_1981]\] \[[Velger and Shinar 1983][research_velger_shinar_1983]\] \[[Vidan 2016][research_vidan_2016]\] \[[Vomaske et al 1961][research_vomaske_1961]\] \[[Walchner 1969][research_walchner_1969_2]\] \[[Walchner et al 1969][research_walchner_1969]\] \[[Wang et al 2022][research_wang_2022]\] \[[Wells et al 1982][research_wells_1982]\] \[[Wu et al 2018][research_wu_2018]\] \[[Yin et al 2020][research_yin_2020]\] \[[Zhai et al 2024][research_zhai_2024]\]

### Outdoor sound propagation and atmospheric absorption

Spherical spreading, atmospheric absorption, refraction, ground effect and turbulent scattering, with the duct propagation that shares their equations. **68 of the 152 records date from 2015 or later.**

**152 records.** \[[Abrahamson 1975][research_abrahamson_1975]\] \[[Aircraft noise propagation 2011][research_aircraft_noise_2011]\] \[[Albert 1990][research_albert_1990]\] \[[Almgren 1987][research_almgren_1987]\] \[[André 1977][research_andre_1977]\] \[[Attenborough 1985][research_attenborough_1985]\] \[[Attenborough 2022][research_attenborough_2022]\] \[[Aurégan 2018][research_auregan_2018]\] \[[Bass 1976][research_bass_1976_2]\] \[[Bass et al 1972][research_bass_1972]\] \[[Bass et al 1990][research_bass_1990]\] \[[Bauer 1977][research_bauer_1977]\] \[[Bishop and Franken 1968][research_bishop_franken_1968]\] \[[Brown 1950][research_brown_1950]\] \[[Burrin 1970][research_burrin_1970]\] \[[Canard-Caruana et al 1990][research_canard_caruana_1990]\] \[[Carnes et al 1993][research_carnes_1993]\] \[[Carr et al 2024][research_carr_2024]\] \[[Castro Mota et al 2025][research_castro_mota_2025]\] \[[Chessell 1978][research_chessell_1978]\] \[[Chobeau et al 2017][research_chobeau_2017]\] \[[Cole and Dobbins 1971][research_cole_dobbins_1971]\] \[[Crighton 1979][research_crighton_1979]\] \[[Davidson 1975][research_davidson_1975]\] \[[DeLoach 1975][research_deloach_1975]\] \[[Diamond 1963][research_diamond_1963]\] \[[Diamond and Lee 1965][research_diamond_lee_1965]\] \[[Dickinson 1976][research_dickinson_1976]\] \[[Dickinson 1979][research_dickinson_1979]\] \[[Doak and Vaidya 1970][research_doak_vaidya_1970]\] \[[Doebler et al 2023][research_doebler_2023]\] \[[Domen 1998][research_domen_1998]\] \[[Downing et al 1996][research_downing_zamot_1996]\] \[[Dragna and Blanc-Benon 2017][research_dragna_blanc_benon_2017]\] \[[Dragna and Blanc-Benon 2017][research_dragna_blanc_benon_2017_2]\] \[[Ecotière 2023][research_ecotiere_2023]\] \[[Eser 2023][research_eser_2023]\] \[[Evans 1975][research_evans_1975]\] \[[Evans et al 1972][research_evans_1972]\] \[[Evans et al 1972][research_evans_1972_2]\] \[[Fidell et al 1989][research_fidell_1989]\] \[[Finn and Rogers 2015][research_finn_rogers_2015]\] \[[Finn and Rogers 2016][research_finn_rogers_2016_2]\] \[[Finn and Rogers 2016][research_finn_rogers_2016]\] \[[Foss 1979][research_foss_1979]\] \[[Goestchel et al 2022][research_goestchel_2022]\] \[[Groves 1955][research_groves_1955]\] \[[Groves 1956][research_groves_1956_2]\] \[[Groves 1956][research_groves_1956]\] \[[Gu et al 2026][research_gu_2026]\] \[[Hall et al 2016][research_hall_2016]\] \[[Hart et al 2016][research_hart_2016]\] \[[Hart et al 2021][research_hart_2021]\] \[[Henyey 2009][research_henyey_2009]\] \[[Hilton and Kasper 1974][research_hilton_kasper_1974]\] \[[Hohenwarter et al 2022][research_hohenwarter_2022]\] \[[Hussain and Dutilleux 2020][research_hussain_dutilleux_2020]\] \[[Jeff Berton][research_jeff_berton]\] \[[Jeffery et al 1977][research_jeffery_1977]\] \[[Jing and Ye 2021][research_jing_ye_2021]\] \[[Joel B Lonzaga, An exact solution of an augmented][research_joel_b_lonzaga_2]\] \[[Joel B. Lonzaga, Nonlinear Acoustic Propagation in][research_joel_b_lonzaga]\] \[[Kamrath 2022][research_kamrath_2022]\] \[[Kamrath et al 2016][research_kamrath_2016]\] \[[Kapoor et al 2021][research_kapoor_2021]\] \[[Ke and Zheng 2016][research_ke_zheng_2016]\] \[[Keshavarz and Ohadi 2017][research_keshavarz_ohadi_2017]\] \[[Keyel et al 2017][research_keyel_2017]\] \[[Kingan et al 2023][research_kingan_2023]\] \[[Kirby 2021][research_kirby_2021_2]\] \[[Kirby 2021][research_kirby_2021]\] \[[Kirby 2022][research_kirby_2022]\] \[[Kone et al 2023][research_kone_ghinet_2023]\] \[[Kone et al 2024][research_kone_ghinet_2024]\] \[[Kraxberger et al 2024][research_kraxberger_2024]\] \[[Kriebel 1972][research_kriebel_1972]\] \[[Laly et al 2023][research_laly_2023]\] \[[Lee and Sutherland 1976][research_lee_sutherland_1976]\] \[[Letcher 1995][research_letcher_1995]\] \[[Loubeau 2021][research_loubeau_2021]\] \[[Lyon and Pande 1971][research_lyon_pande_1971]\] \[[Marsh 1981][research_marsh_1981]\] \[[Mechel 1962][research_mechel_1962]\] \[[Mechel et al 1963][research_mechel_1963]\] \[[Mellish et al 2020][research_mellish_2020]\] \[[Mo et al 2016][research_mo_2016]\] \[[Mo et al 2017][research_mo_2017]\] \[[Mobley et al 2016][research_mobley_2016]\] \[[Morfey and Howell 1981][research_morfey_howell_1981]\] \[[Morfey and Tester 1977][research_morfey_tester_1977]\] \[[Mungiole and Wilson 2003][research_mungiole_wilson_2003]\] \[[Nayfeh 1980][research_nayfeh_1980]\] \[[Norris and Ostashev 2022][research_norris_ostashev_2022]\] \[[Nyborg and Mintzer 1955][research_nyborg_mintzer_1955]\] \[[Ohm et al 2020][research_ohm_2020]\] \[[Oncley 1970][research_oncley_1970]\] \[[Ostashev and Goedecke 2005][research_ostashev_goedecke_2005]\] \[[Ostashev and Wilson 2022][research_ostashev_wilson_2022]\] \[[Ostrikov et al 2020][research_ostrikov_2020]\] \[[Panel Discussion Acoustic Wave Propagation through 1976][research_panel_discussion_1976_b]\] \[[Pao and Evans 1971][research_pao_evans_1971]\] \[[Parry et al 2020][research_parry_2020_2]\] \[[Parry et al 2020][research_parry_2020]\] \[[Pasareanu et al 2018][research_pasareanu_2018]\] \[[Pena and Diamond 1965][research_pena_diamond_1965]\] \[[Peplow and Liu 2025][research_peplow_liu_2025]\] \[[Plotkin and Shepherd 2006][research_plotkin_shepherd_2006]\] \[[Polly 1969][research_polly_1969]\] \[[Pridmore-Brown 1962][research_pridmore_brown_1962]\] \[[Putnam 1975][research_putnam_1975]\] \[[Rasmussen 1986][research_rasmussen_1986]\] \[[Rasmussen 1990][research_rasmussen_1990]\] \[[Richards and Attenborough 1986][research_richards_attenborough_1986]\] \[[Ruijgrok 1983][research_ruijgrok_1983]\] \[[Ryan et al 2022][research_ryan_2022]\] \[[Rydin et al 2018][research_rydin_2018]\] \[[Sabine and Burkhard 1959][research_sabine_burkhard_1959]\] \[[Schwartz 1976][research_schwartz_1976]\] \[[Shankar 1972][research_shankar_1972]\] \[[Shields and Bass 1977][research_shields_bass_1977]\] \[[Shivashankara and Stubbs 1987][research_shivashankara_stubbs_1987]\] \[[Soom and Gu 1981][research_soom_gu_1981]\] \[[Southerland et al 1986][research_southerland_platus_1986]\] \[[Stenzel 1947][research_stenzel_1947]\] \[[Sutherland and Wesler 1990][research_sutherland_wesler_1990]\] \[[Swearingen and White 2020][research_swearingen_white_2020]\] \[[Takeya and Okumoto 1959][research_takeya_okumoto_1959]\] \[[Tester 1973][research_tester_1973_2]\] \[[Tester 1973][research_tester_1973]\] \[[Tipton and Sparrow 2019][research_tipton_sparrow_2019]\] \[[Tombolato et al 2024][research_tombolato_2024]\] \[[Trikootam and Hornikx 2019][research_trikootam_hornikx_2019]\] \[[Troian et al 2017][research_troian_2017]\] \[[Vecchiotti et al 2024][research_vecchiotti_2024]\] \[[Wang and Li 2019][research_wang_li_2019]\] \[[Wang et al 2024][research_wang_2024_5]\] \[[West 1994][research_west_1994]\] \[[West et al 2015][research_west_2015]\] \[[White 2025][research_white_2025]\] \[[Willshire 1990][research_willshire_1990]\] \[[Willshire and Hilton 1979][research_willshire_hilton_1979]\] \[[Wilson 2024][research_wilson_2024]\] \[[Wilson et al 2016][research_wilson_2016]\] \[[Wilson et al 2022][research_wilson_2022]\] \[[Wolf and Raspet 1986][research_wolf_raspet_1986]\] \[[Woolworth 2022][research_woolworth_2022]\] \[[Woolworth 2023][research_woolworth_2023]\] \[[Yamashita and Matsui 1978][research_yamashita_matsui_1978]\] \[[Yokota et al 2023][research_yokota_2023]\] \[[Yokota et al 2025][research_yokota_2025]\] \[[Zheng et al 2019][research_zheng_2019]\] \[[Zorumski and Willshire 1989][research_zorumski_willshire_1989]\]

### Induced drag, span loading and the high aspect ratio wing

Induced drag, span loading, lifting-line and lifting-surface theory, winglets and the high aspect ratio wing.

**144 records.** \[[Adamson and Boatright 1950][research_adamson_boatright_1950]\] \[[Ajaj 2021][research_ajaj_2021]\] \[[Antonakis and Biannic 2024][research_antonakis_biannic_2024]\] \[[Army Aviation Board Fort Rucker Al 1957][research_armyaviationboardfortruckeral_1957]\] \[[Ashill 1970][research_ashill_1970]\] \[[Barrett-Gonzalez and Wolf 2021][research_barrett_gonzalez_wolf_2021]\] \[[Bauer et al 2016][research_bauer_2016]\] \[[Bera 1976][research_bera_1976]\] \[[Bera† 1980][research_bera_1980]\] \[[Bilanin and Donaldson 1975][research_bilanin_donaldson_1975]\] \[[Bloom and Jen 1974][research_bloom_jen_1974]\] \[[Bobbitt 1957][research_bobbitt_1957]\] \[[Bobbitt 1959][research_bobbitt_1959]\] \[[Bowers 1979][research_bowers_1979]\] \[[Bowers 2018][research_bowers_2018]\] \[[Thinesh and Y Harmin 2018][research_c_y_harmin_2018]\] \[[Chakraborty et al 2015][research_chakraborty_2015]\] \[[Chau and Zingg 2022][research_chau_zingg_2022]\] \[[Chau and Zingg 2022][research_chau_zingg_2022_2]\] \[[Chau and Zingg 2023][research_chau_zingg_2023]\] \[[Chau et al 2026][research_chau_2026]\] \[[Cheng 1978][research_cheng_1978]\] \[[Cheng and Meng 1980][research_cheng_meng_1980]\] \[[Cook 1979][research_cook_1979]\] \[[Curtiss 1965][research_curtiss_h_c_1965]\] \[[Dalton and Wang 1990][research_dalton_wang_1990]\] \[[Deyoung 1950][research_deyoung_1950]\] \[[Deyoung 1979][research_deyoung_1979]\] \[[Deyoung and Harper 1948][research_deyoung_harper_1948]\] \[[Dragos 1985][research_dragos_1985]\] \[[Dragoş 1990][research_dragos_1990]\] \[[Dym and Williams 2015][research_dym_williams_2015]\] \[[Feero et al 2016][research_feero_2016]\] \[[Flechner and Jacobs 1978][research_flechner_jacobs_1978]\] \[[Fu et al 2021][research_fu_2021]\] \[[Gaifullin 2023][research_gaifullin_2023]\] \[[Gilbrook et al 2025][research_gilbrook_2025]\] \[[Golubinskii and Golubkin 1983][research_golubinskii_golubkin_1983]\] \[[Golubkin 1980][research_golubkin_1980_2]\] \[[Golubkin 1980][research_golubkin_1980]\] \[[Goodman 1976][research_goodman_1976]\] \[[Graham 1971][research_graham_1971]\] \[[Griffin et al 1983][research_griffin_1983]\] \[[Hall et al 1994][research_hall_yang_1994]\] \[[Hanin and Barsony-Nagy 1983][research_hanin_barsony_nagy_1983]\] \[[Hanks 1956][research_hanks_1956]\] \[[Harry and Trobaugh 1966][research_harry_trobaugh_1966]\] \[[He et al 2020][research_he_2020]\] \[[Higuchi et al 1987][research_higuchi_1987]\] \[[Hoerner 1952][research_hoerner_1952]\] \[[Hopkins 1977][research_hopkins_1977]\] \[[Hosseini et al 2020][research_hosseini_2020]\] \[[James 1975][research_james_1975]\] \[[Jang and Ahn 2022][research_jang_ahn_2022]\] \[[Johnson 1972][research_johnson_1972]\] \[[Jones 1950, The spanwise distribution of lift][research_jones_1950]\] \[[Kacik and Goetzendorf-Grabowski 2025][research_kacik_goetzendorf_grabowski_2025]\] \[[Katz 1989][research_katz_1989]\] \[[Keener 1985][research_keener_1985]\] \[[Kennelly et al 1990][research_kennelly_1990]\] \[[Kholyavko 1971][research_kholyavko_1971]\] \[[Kiang 1971][research_kiang_1971]\] \[[Kida 1982][research_kida_1982]\] \[[Kida and Miyai 1978][research_kida_miyai_1978]\] \[[Kretov and Tiniakov 2022][research_kretov_tiniakov_2022]\] \[[Kuhlman 1979][research_kuhlman_1979]\] \[[Kuhlman and Liaw 1987][research_kuhlman_liaw_1987]\] \[[Lazos and Visser 2006][research_lazos_visser_2006]\] \[[Lee et al 2017][research_lee_2017_2]\] \[[Lerbs 1955][research_lerbs_1955]\] \[[Levinsky et al 1968][research_levinsky_1968]\] \[[Li et al 2022][research_li_2022_5]\] \[[Li et al 2023][research_li_2023_4]\] \[[Loth and Boyle 1969][research_loth_boyle_1969]\] \[[Lundry 1977][research_lundry_1977]\] \[[Ma 1989][research_ma_1989]\] \[[Ma et al 2022][research_ma_2022]\] \[[Ma et al 2025][research_ma_2025_3]\] \[[Malmuth 1966][research_malmuth_1966]\] \[[Mamada and Ando 1974][research_mamada_ando_1974]\] \[[Mansour 1985][research_mansour_1985]\] \[[Marchman and Abtahi 1985][research_marchman_abtahi_1985]\] \[[Martinez 1989][research_martinez_1989]\] \[[McCormick 1959][research_mccormick_1959]\] \[[McCutchen 1989][research_mccutchen_1989]\] \[[Menon et al 2022][research_menon_2022]\] \[[Miles 1953][research_miles_1953]\] \[[Milla and Blick 1966][research_milla_blick_1966]\] \[[Mitcheltree et al 1986][research_mitcheltree_1986]\] \[[Mokry and Rainbird 1975][research_mokry_rainbird_1975]\] \[[Morita 1970][research_morita_1970]\] \[[Morita 1971][research_morita_1971]\] \[[Morita 1971][research_morita_1971_2]\] \[[Moriya 1972][research_moriya_1972]\] \[[Morton 1956][research_morton_1956]\] \[[Mr. S. Aravindan et al 2017][research_mr_s_aravindan_2017]\] \[[Narayan 1975][research_narayan_1975]\] \[[Nelson 1964][research_nelson_1964]\] \[[Nonweiler 1960][research_nonweiler_1960]\] \[[Pao and Lan 1978][research_pao_lan_1978]\] \[[Pavel et al 2018][research_pavel_jan_2018]\] \[[Pavlenko and Reslan 2022][research_pavlenko_reslan_2022]\] \[[Pelykh and Andryushchenko 2024][research_pelykh_andryushchenko_2024]\] \[[Perry 1978][research_perry_1978]\] \[[Pfeifle et al 2022][research_pfeifle_2022]\] \[[Portnoy 1976][research_portnoy_1976]\] \[[Portnoy 1977][research_portnoy_1977]\] \[[Pyo 1995][research_pyo_1995]\] \[[Quinn et al 2025][research_quinn_2025]\] \[[Stallings 1986][research_r_l_stallings_jr_1986]\] \[[Rand et al 2004][research_rand_khromov_2004]\] \[[Reynolds 1963][research_reynolds_1963]\] \[[Rice and Oetting 1976][research_rice_oetting_1976]\] \[[Ruffini et al 2020][research_ruffini_2020]\] \[[Kandasamy et al 2018][research_s_2018]\] \[[Sanz 1986][research_sanz_1986]\] \[[Schauerhamer and Robinson 2017][research_schauerhamer_robinson_2017]\] \[[Schulderfrei et al 1951][research_schulderfrei_1951]\] \[[Sears 1948][research_sears_1948]\] \[[Sears 1974][research_sears_1974]\] \[[Sears 1990][research_sears_1990]\] \[[Secco and Martins 2019][research_secco_martins_2019]\] \[[Shirbhate et al 2025][research_shirbhate_2025]\] \[[Sibert 1943][research_sibert_1943]\] \[[Sim and Curry 1985][research_sim_curry_1985]\] \[[Sivells and Neely 1947][research_sivells_neely_1947]\] \[[Smith and Kroo 1990][research_smith_kroo_1990]\] \[[Tan and Plotkin 1986][research_tan_plotkin_1986]\] \[[Uzun 2025][research_uzun_2025]\] \[[von Kármán and Tsien 1945][research_von_karman_tsien_1945]\] \[[Wahler et al 2025][research_wahler_2025]\] \[[Whitcomb 1940][research_whitcomb_1940]\] \[[White 1963][research_white_1963]\] \[[Wilmott 1986][research_wilmott_1986]\] \[[Wings and Winglets 1999][research_wings_and_1999]\] \[[Wu and Talmadge 1961][research_wu_talmadge_1961]\] \[[Xieyuan 1985][research_xieyuan_1985]\] \[[Yates 1974][research_yates_1974]\] \[[Yeh and Plotkin 1986][research_yeh_plotkin_1986]\] \[[Yu and Ansell 2023][research_yu_ansell_2023]\] \[[Yuan et al 2018][research_yuan_2018]\] \[[Zhou et al 2020][research_zhou_2020_2]\] \[[Zohar and Er-El 1988][research_zohar_er_el_1988]\] \[[Zong et al 2021][research_zong_2021]\]

### Community noise, annoyance and psychoacoustics

Annoyance, community response, health effects and the psychoacoustic metrics that predict them, for aircraft and for the urban air mobility vehicles now proposed. **87 of the 137 records date from 2015 or later.**

**137 records.** \[[Aalmoes and Sieben 2021][research_aalmoes_sieben_2021]\] \[[Abwanzo 2016][research_abwanzo_2016]\] \[[Aircraft Noise and Certification 2019][research_aircraft_noise_2019]\] \[[Aircraft Noise Monitoring 1979][research_aircraft_noise_1979]\] \[[Akdeniz et al 2020][research_akdeniz_2020]\] \[[Akiyama et al 2023][research_akiyama_2023]\] \[[Alexandre and Barde 1974][research_alexandre_barde_1974]\] \[[Christian][research_andrew_christian]\] \[[Ang et al 2024][research_ang_2024]\] \[[Bauer 2021][research_bauer_2021]\] \[[Bauermeister and Donner 1980][research_bauermeister_donner_1980]\] \[[Bolt Beranek And Newman Inc Los Angeles Ca 1965][research_bolt_beranek_and_newman_inc_los_angeles_ca_1965]\] \[[Boucher et al 2023][research_boucher_2023]\] \[[Boullet et al 2023][research_boullet_2023]\] \[[Calculation of aircraft noise contours around airports 1989][research_calculation_of_1989]\] \[[Chabot and Bird 2015][research_chabot_bird_2015]\] \[[Christian 2021][research_christian_2021]\] \[[Clemente Carrari et al 2025][research_clemente_carrari_2025]\] \[[Curtis 1977][research_curtis_1977]\] \[[Dani][research_dani]\] \[[Di 2017][research_di_2017]\] \[[Felcyn and Ptak 2022][research_felcyn_ptak_2022]\] \[[Fidell 2018][research_fidell_2018]\] \[[Fidell et al 1998][research_fidell_1998]\] \[[Flindell et al 2021][research_flindell_2021]\] \[[Galloway and Bennett 1981][research_galloway_bennett_1981]\] \[[Gasaway 1970][research_gasaway_1970]\] \[[Georgiou et al 2026][research_georgiou_2026]\] \[[Gille et al 2017][research_gille_2017]\] \[[Gillfillan 1961][research_gillfillan_1961]\] \[[Gillfillian 1962][research_gillfillian_1962]\] \[[Green et al 2023][research_green_2023]\] \[[Guerrero et al 2026][research_guerrero_2026]\] \[[He et al 2026][research_he_2026_2]\] \[[Hede 2017][research_hede_2017]\] \[[Higbie 1995][research_higbie_1995]\] \[[Hiramatsu 2023][research_hiramatsu_2023]\] \[[Holger 1980][research_holger_1980]\] \[[Howie and Brugger 2000][research_howie_brugger_2000]\] \[[Huang et al 2023][research_huang_2023_4]\] \[[Iemma 2016][research_iemma_2016]\] \[[Jovanovic and Novak 2022][research_jovanovic_novak_2022]\] \[[Jovanovic and Novak 2022][research_jovanovic_novak_2022_2]\] \[[Jovanovic et al 2022][research_jovanovic_2022]\] \[[Jovanovic et al 2023][research_jovanovic_2023]\] \[[Kafali and Güçlü 2023][research_kafali_guclu_2023]\] \[[Keilman 2019][research_keilman_2019]\] \[[Kim][research_kim]\] \[[Kim et al 2022][research_kim_2022_2]\] \[[Ko 1975][research_ko_1975]\] \[[Ko 1975][research_ko_1975_2]\] \[[Ko 1979][research_ko_1979]\] \[[Kodji et al 2023][research_kodji_2023]\] \[[Kodji et al 2024][research_kodji_2024]\] \[[Krishnamurthy and Rizzi 2022][research_krishnamurthy_rizzi_2022]\] \[[Kryter 1966][research_kryter_1966]\] \[[Kryter 1967][research_kryter_1967]\] \[[Kryter 1982][research_kryter_1982]\] \[[Kuhlmann et al 2024][research_kuhlmann_romerostarke_2024]\] \[[Kull and Finegold 2024][research_kull_finegold_2024]\] \[[Kyi and Feng 2026][research_kyi_feng_2026]\] \[[König et al 2024][research_konig_2024]\] \[[Lang 2024][research_lang_2024]\] \[[Lauber 1967][research_lauber_1967]\] \[[Lechner et al 2021][research_lechner_2021]\] \[[Lee et al 2026][research_lee_2026]\] \[[Li et al 2021][research_li_2021]\] \[[Lincke and Pieren 2024][research_lincke_pieren_2024]\] \[[Lincke et al 2025][research_lincke_2025]\] \[[Lotinga et al 2025][research_lotinga_2025_2]\] \[[Lotinga et al 2025][research_lotinga_2025]\] \[[Ludlow 2024][research_ludlow_2024]\] \[[Lv et al 2023][research_lv_2023]\] \[[Mackie and Lawrence 2019][research_mackie_lawrence_2019]\] \[[Marquis-Favre et al 2023][research_marquis_favre_2023]\] \[[McCurdy 1984][research_mccurdy_1984]\] \[[McNeill and Vomaske 1959][research_mcneill_vomaske_1959]\] \[[McPIKE 1972][research_mcpike_1972]\] \[[McPike 1976][research_mcpike_1976]\] \[[Melton and Jacobson 1983][research_melton_jacobson_1983]\] \[[Min et al 2015][research_min_lim_2015]\] \[[Monzambe et al 2024][research_monzambe_2024]\] \[[Nguyen and Yano 2024][research_nguyen_yano_2024]\] \[[Nguyen et al 2018][research_nguyen_2018_2]\] \[[Odell 1977][research_odell_1977]\] \[[Ollerhead 1973][research_ollerhead_1973]\] \[[Page et al 2021][research_page_2021]\] \[[Page et al 2026][research_page_2026]\] \[[Papamoschou and Phong 2018][research_papamoschou_phong_2018]\] \[[Phun et al 2015][research_phun_2015]\] \[[Raw and Griffiths 1985][research_raw_griffiths_1985]\] \[[Reddingius 1974][research_reddingius_1974]\] \[[Reddingius 1977][research_reddingius_1977]\] \[[Rehm and Jansen 1978][research_rehm_jansen_1978]\] \[[Rizzi and Rafaelof 2021][research_rizzi_rafaelof_2021]\] \[[Rizzi and Scata 2022][research_rizzi_scata_jr_2022]\] \[[Rizzi et al 2016][research_rizzi_2016]\] \[[Rizzi et al 2024][research_rizzi_2024]\] \[[Roberts 1988][research_roberts_1988]\] \[[Roncen 2025][research_roncen_2025]\] \[[Sahai et al 2017][research_sahai_2017]\] \[[Sawyer 1967][research_sawyer_1967]\] \[[Scanlan 1948][research_scanlan_1948]\] \[[Schaffer et al 2023][research_schaffer_bertsch_2023_b]\] \[[Schomer et al 1991][research_schomer_1991]\] \[[Schreckenberg et al 2023][research_schreckenberg_2023]\] \[[Speakman et al 1978][research_speakman_1978]\] \[[Sperry 1979][research_sperry_1979]\] \[[Stewart et al 2012][research_stewart_2012]\] \[[Tarnopolsky 1978][research_tarnopolsky_1978]\] \[[Taylor 1984][research_taylor_1984]\] \[[Terzakis et al 2025][research_terzakis_2025]\] \[[Thalheimer 2021][research_thalheimer_2021]\] \[[Thirtyacre et al 2021][research_thirtyacre_2021]\] \[[Thomas and Hansman 2019][research_thomas_hansman_2019]\] \[[Thomas and Hansman 2020][research_thomas_hansman_2020]\] \[[Thomas and Hansman 2021][research_thomas_hansman_2021]\] \[[Thomas and Jones 1982][research_thomas_jones_1982]\] \[[Thottathil Varghese et al 2022][research_thottathil_varghese_2022]\] \[[Tokashiki 2023][research_tokashiki_2023]\] \[[Tracy et al 2024][research_tracy_2024]\] \[[Vaughn et al 2023][research_vaughn_2023]\] \[[Vulkan and Hyde 1981][research_vulkan_hyde_1981]\] \[[Bauer 2025][research_w_bauer_2025]\] \[[Wang et al 2015][research_wang_2015_2]\] \[[Webster 1971][research_webster_1971]\] \[[Welch et al 2026][research_welch_2026]\] \[[Weslet and Sutherland 1987][research_weslet_sutherland_1987]\] \[[Woods 1972][research_woods_1972]\] \[[Wu and Redonnet 2021][research_wu_redonnet_2021]\] \[[Yamada 2023][research_yamada_2023]\] \[[Yeow 1984][research_yeow_1984]\] \[[Yoon et al 2019][research_yoon_2019]\] \[[Zaporozhets et al 2022][research_zaporozhets_2022]\] \[[Zhang et al 2023][research_zhang_2023_5]\] \[[Zhang et al 2025][research_zhang_2025_2]\] \[[Zorić 2024][research_zoric_2024]\]

### Acoustic and aural detection of aircraft

Hearing, locating and classifying an aircraft from its sound, together with the radar, radio and visual detection literature that the same problem draws on. **86 of the 134 records date from 2015 or later.**

**The literature turned from the listener on the ground to the drone overhead.** Of the 86 records from 2015 or later, 66 name an unmanned aircraft or a drone, while the period records concern ground observers, sound ranging and the aural and visual detectability of military aircraft, which is the inversion the review above describes.

**134 records.** \[[Abbott 2016][research_abbott_2016]\] \[[Alexander and Kinzly 1979][research_alexander_kinzly_1979]\] \[[Alimadadi 2026][research_alimadadi_2026]\] \[[Amanatiadis et al 2017][research_amanatiadis_2017]\] \[[Aydın and Kızılay 2022][research_aydn_kzlay_2022]\] \[[Baldwin 1973][research_baldwin_1973]\] \[[Baldwin and Frederickson 1966][research_baldwin_frederickson_1966]\] \[[Barry and Magliozzi 1971][research_barry_magliozzi_1971]\] \[[Basak et al 2022][research_basak_2022]\] \[[Bellucci 1963][research_bellucci_1963]\] \[[Bernardini et al 2017][research_bernardini_2017]\] \[[Bishop and Tufariello 2019][research_bishop_tufariello_2019]\] \[[Blackburn and Joslin 2021][research_blackburn_joslin_2021]\] \[[Blanchard et al 2020][research_blanchard_2020]\] \[[Brown et al 2016][research_brown_2016]\] \[[Che Mamat and Abdul Aziz 2022][research_che_mamat_abdul_aziz_2022]\] \[[Chen et al 2015][research_chen_2015]\] \[[Chew and Chapin 1963][research_chew_chapin_1963]\] \[[Corridor-Wide Surveillance Using Unmanned Aircraft Systems 2023][research_corridor_wide_surveillance_2023]\] \[[Dafrallah and Akhloufi 2024][research_dafrallah_akhloufi_2024]\] \[[de Macedo et al 2025][research_de_macedo_2025]\] \[[Dekoninck 2020][research_dekoninck_2020]\] \[[Dingeldein et al 1975][research_dingeldein_connor_1975]\] \[[Dolph et al 2021][research_dolph_2021]\] \[[Ernst and Sachau 2025][research_ernst_sachau_2025]\] \[[Fang et al 2023][research_fang_2023]\] \[[Fidell et al 1990][research_fidell_secrist_1990]\] \[[Fidell et al 1990][research_fidell_reddingius_1990]\] \[[Forkun et al 2020][research_forkun_makaryshkin_2020]\] \[[Frederickson et al 1967][research_frederickson_1967]\] \[[Gager et al 1962][research_gager_headrick_1962]\] \[[Gaston et al 2013][research_gaston_2013]\] \[[Gayne 1965][research_gayne_1965]\] \[[Ghenescu et al 2026][research_ghenescu_2026]\] \[[Go and Choi 2021][research_go_choi_2021]\] \[[Goldman 2016][research_goldman_2016]\] \[[Gopalan et al 2022][research_gopalan_2022]\] \[[Guzik et al 2019][research_guzik_2019]\] \[[Haddad et al 2019][research_haddad_2019]\] \[[Han et al 2024][research_han_2024]\] \[[Harvey and OYoung 2016][research_harvey_oyoung_2016]\] \[[Harvey and OYoung 2018][research_harvey_oyoung_2018]\] \[[Hess 2012][research_hess_2012]\] \[[Highland et al 2020][research_highland_2020]\] \[[Hilton et al 1975][research_hilton_connor_1975]\] \[[Hoff 1982][research_hoff_1982]\] \[[Huang et al 2026][research_huang_du_2026]\] \[[Jack et al 2014][research_jack_hoffler_2014]\] \[[JanakiRam 1980][research_janakiram_1980]\] \[[JanakiRam and Scruggs 1982][research_janakiram_scruggs_1982]\] \[[Jekateryńczuk and Piotrowski 2025][research_jekaterynczuk_piotrowski_2025]\] \[[Jekateryńczuk et al 2025][research_jekaterynczuk_2025]\] \[[Juřička and Juřičková 2020][research_juricka_jurickova_2020]\] \[[Kadyrov et al 2022][research_kadyrov_2022]\] \[[Kartashov et al 2021][research_kartashov_2021]\] \[[Kim 2016][research_kim_2016]\] \[[Kim et al 2025][research_kim_2025_2]\] \[[Kletschkowski 2012][research_kletschkowski_2012]\] \[[Kloet et al 2017][research_kloet_2017]\] \[[Kocur et al 2023][research_kocur_2023]\] \[[Kozak 2021][research_kozak_2021]\] \[[Kozeruk and Korzhik 2022][research_kozeruk_korzhik_2022]\] \[[Kozeruk and Korzhyk 2019][research_kozeruk_korzhyk_2019]\] \[[Kumar S Rajanikanth 2024][research_kumar_s_rajanikanth_2024]\] \[[Kurdyla 1963][research_kurdyla_1963]\] \[[Landers and Lacoss 1978][research_landers_lacoss_1978]\] \[[Lee 2019][research_lee_2019]\] \[[Lee and Lee 2026][research_lee_lee_2026]\] \[[Lim et al 2025][research_lim_2025_2]\] \[[Liu et al 2021][research_liu_2021]\] \[[Loewy 1963][research_loewy_1963]\] \[[Loffi et al 2021][research_loffi_2021]\] \[[Ludeman 1979][research_ludeman_1979]\] \[[Manickam et al 2020][research_manickam_2020]\] \[[Marcus and Räf 2019][research_marcus_raf_2019]\] \[[Memorandum, US Reconnaissance Aircraft Reports Interception][research_memorandum_us]\] \[[Michel 1989][research_michel_1989]\] \[[Minwalla et al 2016][research_minwalla_2016_2]\] \[[Minwalla et al 2016][research_minwalla_2016]\] \[[Moreland Jr. et al 1965][research_moreland_jr_1965]\] \[[Morge-Rollet et al 2022][research_morge_rollet_2022]\] \[[Mueller et al 1993][research_mueller_1993]\] \[[Muneer et al 2026][research_muneer_2026]\] \[[Muniraj and Farhood 2019][research_muniraj_farhood_2019]\] \[[Najafi et al 2025][research_najafi_2025]\] \[[Nemec et al 2024][research_nemec_bedonian_2024]\] \[[Ogiso et al 2019][research_ogiso_2019]\] \[[Oh et al 2023][research_oh_lerud_2023]\] \[[Oleynikov et al 2018][research_oleynikov_2018]\] \[[Ollerhead 1971][research_ollerhead_1971]\] \[[Paszkowski et al 2024][research_paszkowski_2024]\] \[[Poe and Arthur C. 1974][research_poe_arthur_c_1974]\] \[[Price and Hodge 1976][research_price_hodge_1976]\] \[[Quaranta and Dimino 2007][research_quaranta_dimino_2007]\] \[[Rakesh and Reddy 2023][research_rakesh_reddy_2023]\] \[[Ramachandra 1979][research_ramachandra_1979]\] \[[Rao Pittu et al 2023][research_rao_pittu_2023]\] \[[Render and Jenkinson 1996][research_render_jenkinson_1996]\] \[[Research on control takeover techniques for counter-UAV (Unmanned Aircraft Vehicle) 2025][research_research_on_2025]\] \[[Rizzi et al 2017][research_rizzi_christian_2017]\] \[[Rodenhiser et al 2007][research_rodenhiser_durgin_2007]\] \[[Sahai et al 2016][research_sahai_wefers_2016]\] \[[Sahawneh et al 2015][research_sahawneh_2015]\] \[[Sahithi 2023][research_sahithi_2023]\] \[[Sanchez-Galan et al 2025][research_sanchez_galan_2025]\] \[[Scharine and Letowski 2013][research_scharine_letowski_2013]\] \[[Schriever 1952][research_schriever_1952]\] \[[Sedunov et al 2018][research_sedunov_2018]\] \[[Sedunov et al 2019][research_sedunov_2019]\] \[[Seidaliyeva et al 2023][research_seidaliyeva_2023]\] \[[Sesham et al 2026][research_sesham_2026]\] \[[Sheffield 2000][research_sheffield_2000]\] \[[Shelley 2018][research_shelley_2018]\] \[[Siegel and Crain 1960][research_siegel_crain_1960]\] \[[Siegel and Lanterman 1963][research_siegel_lanterman_1963]\] \[[Smith][research_smith]\] \[[Stalnov et al 2022][research_stalnov_2022]\] \[[Starr et al 1975][research_starr_sernas_1975]\] \[[Svatos et al 2021][research_svatos_2021]\] \[[Tabassum and Bai 2022][research_tabassum_bai_2022]\] \[[Thomason et al 1967][research_thomason_1967]\] \[[Tong et al 2013][research_tong_hu_2013]\] \[[Trinks and Haseborg 1982][research_trinks_haseborg_1982]\] \[[Uddin et al 2021][research_uddin_2021]\] \[[Verba et al 2024][research_verba_2024]\] \[[Wallace and Vance 2019][research_wallace_vance_2019]\] \[[Wilson et al 2021][research_wilson_2021]\] \[[Wokoun 1962][research_wokoun_1962]\] \[[Woo et al 2020][research_woo_2020]\] \[[Wright 1966][research_wright_1966]\] \[[Wu et al 2021][research_wu_2021_2]\] \[[Yu 2011][research_yu_2011]\] \[[Zou et al 2021][research_zou_2021]\] \[[Zu et al 2017][research_zu_2017]\]

### Unmanned aircraft design and operation

Unmanned aircraft design, operation and regulation, and the observation missions they now fly. **98 of the 104 records date from 2015 or later.**

**The mission that went unmanned has an almost wholly recent literature**, which is the second half of the pattern the review above describes.

**104 records.** \[[Alieksieiev and Tsybov 2025][research_alieksieiev_tsybov_2025]\] \[[Altman 2008][research_altman_2008]\] \[[An Overview On Unmanned Aerial Vehicle 2017][research_an_overview_2017]\] \[[Barr et al 2018][research_barr_2018]\] \[[Bauer and Nagy 2024][research_bauer_nagy_2024]\] \[[Bookstaber 2000][research_bookstaber_2000]\] \[[Cheng et al 2025][research_cheng_2025]\] \[[Choi 2020][research_choi_2020]\] \[[Cieślak 2021][research_cieslak_2021]\] \[[Ciolponea 2022][research_ciolponea_2022]\] \[[Combey et al 2026][research_combey_2026]\] \[[Coombes et al 2017][research_coombes_2017]\] \[[De Luca et al 2025][research_de_luca_2025]\] \[[Design and Fluid Flow Analysis of Unmanned Aerial Vehicle (UAV) 2015][research_design_and_2015]\] \[[Ducard 2015][research_ducard_2015]\] \[[Dudziak et al 2020][research_dudziak_2020]\] \[[El Gaouti et al 2024][research_el_gaouti_2024]\] \[[Elzoghby et al 2017][research_elzoghby_2017]\] \[[Evaluating The Use of Manned and Unmanned Aircraft Systems in Strategic Offensive Tasks 2015][research_evaluating_the_2015]\] \[[Fry 2008][research_fry_2008]\] \[[Fu et al 2026][research_fu_2026]\] \[[Garcia and Eskandarian 2026][research_garcia_eskandarian_2026]\] \[[Geng et al 2024][research_geng_2024]\] \[[Ghofur et al 2020][research_ghofur_m_2020]\] \[[Han and Barakos 2020][research_han_barakos_2020]\] \[[Hashim 2020][research_hashim_2020]\] \[[He et al 2024][research_he_2024]\] \[[Henderson 2023][research_henderson_2023]\] \[[Henry et al 2023][research_henry_2023]\] \[[Hrishikeshavan et al 2015][research_hrishikeshavan_2015]\] \[[Irmawan and Eko Prasetiyo 2020][research_irmawan_eko_prasetiyo_2020]\] \[[Islam et al 2015][research_islam_2015]\] \[[Jianhong and Yanxiang 2026][research_jianhong_yanxiang_2026]\] \[[Jimenez et al 2016][research_jimenez_2016]\] \[[Jurczyk 2018][research_jurczyk_2018]\] \[[Kaneko and Martins 2023][research_kaneko_martins_2023]\] \[[Kang and Woolsey 2020][research_kang_woolsey_2020]\] \[[Kant et al 2023][research_kant_2023]\] \[[Kapnik 2019][research_kapnik_2019]\] \[[Keleş 2022][research_keles_2022]\] \[[Kim and Atkins 2022][research_kim_atkins_2022]\] \[[Kimathi and Lantos 2023][research_kimathi_lantos_2023]\] \[[Kistyarev and Wang 2025][research_kistyarev_wang_2025]\] \[[Kochuk et al 2021][research_kochuk_2021]\] \[[Konert and Kasprzyk 2024][research_konert_kasprzyk_2024]\] \[[Kopecki 2016][research_kopecki_2016]\] \[[Kumari and Raghunath 2016][research_kumari_raghunath_2016]\] \[[Leylek and Costello 2015][research_leylek_costello_2015]\] \[[Li 2019][research_li_2019]\] \[[Lim et al 2023][research_lim_2023_2]\] \[[Lu et al 2025][research_lu_2025_3]\] \[[Ma et al 2024][research_ma_2024]\] \[[Macdonald and Schneider 2019][research_macdonald_schneider_2019]\] \[[Majka 2015][research_majka_2015]\] \[[Mark et al 2019][research_mark_2019]\] \[[Marshall and Anderson 2015][research_marshall_anderson_2015]\] \[[Mathur and Atkins 2023][research_mathur_atkins_2023]\] \[[Matos and Marta 2024][research_matos_marta_2024]\] \[[Matt et al 2025][research_matt_2025]\] \[[Mihelič and Pozderec 2023][research_mihelic_pozderec_2023]\] \[[Mosov et al 2020][research_mosov_2020]\] \[[Multi-Rotors A Revolution In 2015][research_multi_rotors_a_2015]\] \[[Müller and Moormann 2023][research_muller_moormann_2023]\] \[[Nam and Joshi 2017][research_nam_joshi_2017]\] \[[Pande 2025][research_pande_2025]\] \[[Papa 2023][research_papa_2023]\] \[[Papageorgiou et al 2018][research_papageorgiou_2018]\] \[[Papageorgiou et al 2020][research_papageorgiou_2020]\] \[[Patterson et al 2016][research_patterson_2016]\] \[[Pecho et al 2019][research_pecho_2019]\] \[[Pentz and Tang 2017][research_pentz_tang_2017]\] \[[Pestana 2010][research_pestana_2010]\] \[[Pham et al 2025][research_pham_2025]\] \[[Pöysä et al 2018][research_poysa_2018]\] \[[Dhayalan et al 2018][research_r_2018]\] \[[Rhudy et al 2023][research_rhudy_2023]\] \[[Rogalski 2018][research_rogalski_2018]\] \[[Ryan and Cummings 2016][research_ryan_cummings_2016]\] \[[Sudhakar et al 2025][research_s_2025_2]\] \[[Sabatini et al 2015][research_sabatini_2015]\] \[[Santoso and Hariyanto 2022][research_santoso_hariyanto_2022]\] \[[Sells and Crossley 2023][research_sells_crossley_2023]\] \[[Si et al 2023][research_si_2023]\] \[[Simmons et al 2019][research_simmons_2019]\] \[[Sun et al 2019][research_sun_2019]\] \[[Tsuji 2024][research_tsuji_2024]\] \[[Unmanned and Uncontrolled The 2015][research_unmanned_and_2015]\] \[[Venkataraman et al 2017][research_venkataraman_2017]\] \[[Venkataraman et al 2019][research_venkataraman_2019]\] \[[Vránics 2020][research_vranics_2020]\] \[[Wan et al 2019][research_wan_2019]\] \[[Wang et al 2020][research_wang_2020_3]\] \[[Winslow et al 2018][research_winslow_2018]\] \[[Wood et al 2019][research_wood_2019]\] \[[Xu and Wang 2016][research_xu_wang_2016]\] \[[Yu 2018][research_yu_2018]\] \[[Yuan 2026][research_yuan_2026]\] \[[Yuma Proving Ground Az 2013][research_yuma_proving_ground_az_2013]\] \[[Yuma Test Center Yuma Proving Ground Az 2008][research_yuma_test_center_yuma_proving_ground_az_2008]\] \[[Zhang 2026][research_zhang_2026_10]\] \[[Zhang et al 2025][research_zhang_2025_3]\] \[[Zhou and Wang 2026][research_zhou_wang_2026]\] \[[Zhu and Duan 2015][research_zhu_duan_2015]\] \[[Żugaj 2017][research_zugaj_2017]\]

### Engine exhaust noise and mufflers

Exhaust, intake and jet noise, and the mufflers and silencers that treat them, including muffler designs for engines other than aircraft engines. **8 of the 85 records date from 2015 or later.**

**85 records.** \[[Ahuja and Bushell 1973][research_ahuja_bushell_1973]\] \[[Alfredson 1971][research_alfredson_1971]\] \[[Arseneau 1997][research_arseneau_1997]\] \[[Bender and Brammer 1973][research_bender_brammer_1973]\] \[[Bender and Brammer 1975][research_bender_brammer_1975]\] \[[Benzakein et al 1973][research_benzakein_kazin_1973]\] \[[Buchwalder 1985][research_buchwalder_1985]\] \[[Butzel 1982][research_butzel_1982]\] \[[Casey 1984][research_casey_1984]\] \[[Chessell 1979][research_chessell_1979]\] \[[Ciepluch 1973][research_ciepluch_1973]\] \[[Czarnecki and Davis 1948][research_czarnecki_davis_1948]\] \[[Czarnigowski et al 2019][research_czarnigowski_skiba_2019]\] \[[Dash et al 2003][research_dash_2003]\] \[[Davis et al 1953][research_davis_1953]\] \[[Doelling 1961][research_doelling_1961]\] \[[Doelling and Bolt 1961][research_doelling_bolt_1961]\] \[[Doelling and Bolt 1961][research_doelling_bolt_1961_2]\] \[[Dyer 1956][research_dyer_1956]\] \[[Emeric 1966][research_emeric_1966]\] \[[Envia 2016][research_envia_2016]\] \[[Experimental Analysis of Exhaust Noise Using a Muffler and 2017][research_experimental_analysis_2017]\] \[[Ferrari and Castelli 1985][research_ferrari_castelli_1985]\] \[[Fischer 1992][research_fischer_1992]\] \[[Fukuda 1960][research_fukuda_1960]\] \[[Fukuda 1960][research_fukuda_1960_2]\] \[[Fukuda 1963][research_fukuda_1963]\] \[[Fukuda 1963][research_fukuda_1963_2]\] \[[Gerber 2003][research_gerber_2003]\] \[[Hargest 1972][research_hargest_1972]\] \[[Hay 1971][research_hay_1971]\] \[[Hirschorn 1960][research_hirschorn_1960]\] \[[Hoffman and Kennedy 1982][research_hoffman_kennedy_1982]\] \[[Hosier 1976][research_hosier_1976]\] \[[Hukuda 1962][research_hukuda_1962]\] \[[Hultgren 2015][research_hultgren_2015]\] \[[Jacques 1976][research_jacques_1976]\] \[[Jaron et al 2023][research_jaron_2023]\] \[[Kaldschmidt et al 1973][research_kaldschmidt_syltebo_1973]\] \[[Keast 1961][research_keast_1961]\] \[[Kenny 2004][research_kenny_2004]\] \[[Kester 1974][research_kester_1974]\] \[[Knott 1974][research_knott_1974]\] \[[Ko 1971][research_ko_1971]\] \[[Kodres 2000][research_kodres_2000]\] \[[Li et al 2024][research_li_yuan_2024]\] \[[Lux and Landwehr 1980][research_lux_landwehr_1980]\] \[[MacGregor et al 1973][research_macgregor_1973]\] \[[Masuda 1996][research_masuda_1996]\] \[[Matsushita and Suzuki 1984][research_matsushita_suzuki_1984]\] \[[Morris et al 1973][research_morris_1973]\] \[[Mutyala and Soedel 1974][research_mutyala_soedel_1974]\] \[[Nagao 1998][research_nagao_1998]\] \[[Nassif 1969][research_nassif_1969]\] \[[Nelson 1938][research_nelson_1938]\] \[[Nelson et al 2012][research_nelson_2012]\] \[[Ohta 1935][research_ohta_1935]\] \[[Pao 1971][research_pao_1971]\] \[[Patrick et al 2000][research_patrick_lobo_2000]\] \[[Pegg and Hilton 1974][research_pegg_hilton_1974]\] \[[Pietrasanta and Galloway 1956][research_pietrasanta_galloway_1956]\] \[[Prasad and Crocker 1983][research_prasad_crocker_1983]\] \[[Rhodes 1982][research_rhodes_1982]\] \[[Robinson 1979][research_robinson_1979]\] \[[Samimy et al 2003][research_samimy_2003]\] \[[Samimy et al 2004][research_samimy_2004]\] \[[Semrau et al 1974][research_semrau_1974]\] \[[Shaikn 1979][research_shaikn_1979]\] \[[Shivashankara 1978][research_shivashankara_1978]\] \[[Shivashankara 1983][research_shivashankara_1983]\] \[[Simcox et al 1976][research_simcox_1976]\] \[[Stephens 2010][research_stephens_2010]\] \[[Stephens 2013][research_stephens_2013]\] \[[Stokes and Davis 1953][research_stokes_davis_1953]\] \[[Tam 1987][research_tam_1987]\] \[[Tanaka et al 1985][research_tanaka_1985]\] \[[Tarnow and Pommer 1988][research_tarnow_pommer_1988]\] \[[Taylor et al 1973][research_taylor_1973]\] \[[Thomson 1983][research_thomson_1983]\] \[[Tyler and Towle 1955][research_tyler_towle_1955]\] \[[Viswanathan 2018][research_viswanathan_2018]\] \[[Wang 1981][research_wang_1981]\] \[[Wu 2010][research_wu_2010]\] \[[Yoshikawa 1992][research_yoshikawa_1992]\] \[[Yu and Huang 2018][research_yu_huang_2018]\]

### Loss of control, upset recovery, stall and spin

Loss of control in flight, upset prevention and recovery, stall, spin and envelope protection. **53 of the 75 records date from 2015 or later.**

**The literature the X-26A's argument fed into is recent.** The training requirement and the envelope protection described above both belong to the last decade of this cluster.

**75 records.** \[[Altunkaya et al 2024][research_altunkaya_2024]\] \[[Anderson 1985][research_anderson_1985]\] \[[Autenrieb 2025][research_autenrieb_2025]\] \[[Bihrle and Barnhart 1974][research_bihrle_barnhart_1974]\] \[[Blanchard 1981][research_blanchard_1981]\] \[[Bottasso and Montinari 2015][research_bottasso_montinari_2015]\] \[[Bowman 1965][research_bowman_1965]\] \[[Bromfield et al 2023][research_bromfield_2023]\] \[[Cano and Sobel 2016][research_cano_sobel_2016]\] \[[de Visser and Pool 2023][research_de_visser_pool_2023]\] \[[Degtyarev et al 2021][research_degtyarev_2021]\] \[[Donaldson et al 2012][research_donaldson_priest_2012]\] \[[El Safany and Bromfield 2025][research_el_safany_bromfield_2025]\] \[[Emami and Roudbari 2019][research_emami_roudbari_2019]\] \[[Feistel et al 1978][research_feistel_1978]\] \[[Feistel et al 1981][research_feistel_1981]\] \[[Gill et al 2015][research_gill_2015]\] \[[Glīzde 2017][research_glizde_2017]\] \[[Golovkin et al 2019][research_golovkin_2019]\] \[[Gresham et al 2024][research_gresham_2024]\] \[[Hamza et al 2022][research_hamza_2022]\] \[[He et al 2026][research_he_2026]\] \[[Healy 1958][research_healy_1958]\] \[[Hurley 1969][research_hurley_1969]\] \[[Israel Moguel 2015][research_israel_moguel_2015]\] \[[Johannes 1971][research_johannes_1971]\] \[[Kao 1974][research_kao_1974]\] \[[Karpuk and Mosca 2024][research_karpuk_mosca_2024]\] \[[Lang et al 2022][research_lang_2022]\] \[[Lang et al 2025][research_lang_2025]\] \[[Ledegang and Groen 2015][research_ledegang_groen_2015]\] \[[Lee et al 2017][research_lee_2017]\] \[[Lombaerts et al 2017][research_lombaerts_2017]\] \[[Ma and Chen 2023][research_ma_chen_2023]\] \[[Ma et al 2022][research_ma_2022_2]\] \[[Malik et al 2017][research_malik_2017]\] \[[Marcinkiewicz et al 2019][research_marcinkiewicz_2019]\] \[[Milillo 1972][research_milillo_1972]\] \[[Moreira et al 2022][research_moreira_2022]\] \[[Nabi et al 2018][research_nabi_2018]\] \[[Nelson 1974][research_nelson_1974]\] \[[Campbell et al][research_newton_h_campbell]\] \[[Campbell et al 2021][research_newton_h_campbell_2021]\] \[[Pitts et al 1974][research_pitts_1974]\] \[[Rebont et al 1977][research_rebont_1977]\] \[[Roudbari and Saghafi 2016][research_roudbari_saghafi_2016]\] \[[Ryffel et al 2019][research_ryffel_2019]\] \[[Bainetov 2016][research_s_d_bainetov_2016]\] \[[Schuet et al 2017][research_schuet_2017]\] \[[Shmelоv et al 2019][research_shmelv_vladov_2019]\] \[[Smaili et al 2018][research_smaili_2018]\] \[[Sparks and Moerder 2002][research_sparks_moerder_2002]\] \[[Srijayantha 1983][research_srijayantha_1983]\] \[[Stough et al 1987][research_stough_1987]\] \[[Taylor and Miller 1982][research_taylor_miller_1982]\] \[[Tong et al 2023][research_tong_2023]\] \[[Van Baelen et al 2020][research_van_baelen_2020]\] \[[Van Dommelen 1995][research_van_dommelen_1995]\] \[[Wang et al 2024][research_wang_2024]\] \[[Wang et al 2025][research_wang_2025_2]\] \[[Wei et al 2020][research_wei_2020]\] \[[White et al 2021][research_white_2021]\] \[[Wu et al 2020][research_wu_2020_2]\] \[[Wu et al 2020][research_wu_2020]\] \[[Ye et al 2015][research_ye_2015]\] \[[Yildiz et al 2019][research_yildiz_2019]\] \[[Yin et al 2019][research_yin_2019]\] \[[Yip et al 1992][research_yip_1992]\] \[[Yu et al 2020][research_yu_2020]\] \[[Yu et al 2023][research_yu_2023]\] \[[Yue et al 2025][research_yue_2025]\] \[[Zhang and Liu 2026][research_zhang_liu_2026]\] \[[Zhao and Jim Zhu 2017][research_zhao_jim_zhu_2017]\] \[[Zheng et al 2018][research_zheng_2018]\] \[[Ç. Altunkaya et al 2025][research_c_altunkaya_2025]\]

### Flight control, control allocation and fault tolerance

Flight control systems and laws, control allocation, fault tolerance and autopilots.

**74 records.** \[[Abdullina and Efanov 2020][research_abdullina_efanov_2020]\] \[[Almutairi and Aouf 2017][research_almutairi_aouf_2017]\] \[[Amitary and Jansen 2011][research_amitary_jansen_2011]\] \[[Anderson and Innis 1965][research_anderson_innis_1965]\] \[[Anderson and Schroers 1972][research_anderson_schroers_1972]\] \[[Banerjee 2019][research_banerjee_2019]\] \[[Bian et al 2018][research_bian_2018]\] \[[Bolds-Moorehead et al 2015][research_boldsmoorehead_chaney_2015]\] \[[Bowersox and Fan 2000][research_bowersox_fan_2000]\] \[[Burken et al 2006][research_burken_2006]\] \[[Burken et al 2006][research_burken_2006_2]\] \[[Carithers and Montalvo 2018][research_carithers_montalvo_2018]\] \[[Chengtao et al 2011][research_chengtao_lixin_2011]\] \[[Cochran 2015][research_cochran_2015]\] \[[Coldsnow et al 2009][research_coldsnow_2009]\] \[[Cole et al 2007][research_cole_cogan_2007]\] \[[Comer and Chakraborty 2024][research_comer_chakraborty_2024]\] \[[Cong et al 2023][research_cong_2023]\] \[[Control of ground objects escorting from aircraft 2021][research_control_of_2021]\] \[[Craig 1965][research_craig_1965]\] \[[Curtiss 1971][research_curtiss_1971]\] \[[Demarchi and Haning 1978][research_demarchi_haning_1978]\] \[[Dong et al 2016][research_dong_2016]\] \[[Dong et al 2016][research_dong_2016_2]\] \[[Dravid 1971][research_dravid_1971]\] \[[Durand and Wasicko 1967][research_durand_wasicko_1967]\] \[[Farajollahi and Markazi 2010][research_farajollahi_markazi_2010]\] \[[Fasel 2002][research_fasel_2002]\] \[[Flight Sciences Lab Inc Buffalo Ny 1964][research_flight_sciences_lab_inc_buffalo_ny_1964]\] \[[Gates and Schy 1951][research_gates_schy_1951]\] \[[Grana and Shanks 1952][research_grana_shanks_1952]\] \[[Hamed 1993][research_hamed_1993]\] \[[Hartmann et al 1976][research_hartmann_1976]\] \[[Heidenreich 1947][research_heidenreich_1947]\] \[[Hendrick 1977][research_hendrick_1977]\] \[[Pearson and Jones 1976][research_henryapearson_roberttjones_1976]\] \[[Herrmann and Ben-Asher 2016][research_herrmann_ben_asher_2016]\] \[[Hess 2018][research_hess_2018]\] \[[Hess and Peng 2018][research_hess_peng_2018]\] \[[Jenney 1979][research_jenney_1979]\] \[[Ji et al 2023][research_ji_2023]\] \[[Jing and Ma 2025][research_jing_ma_2025]\] \[[Kang and Choi 2022][research_kang_choi_2022]\] \[[Kotitschke et al 2026][research_kotitschke_2026]\] \[[Lee 2023][research_lee_2023]\] \[[Lewis 1929][research_lewis_1929]\] \[[Lewis 1930][research_lewis_1930]\] \[[Liang et al 2026][research_liang_2026]\] \[[Lu et al 2017][research_lu_2017]\] \[[Lu et al 2019][research_lu_2019]\] \[[Maughmer et al 1990][research_maughmer_1990]\] \[[Mothes 2019][research_mothes_2019]\] \[[Mueller et al 2004][research_mueller_paluszek_2004]\] \[[Okumoto and Elsanker 1973][research_okumoto_elsanker_1973]\] \[[Paulson and Shanks 1961][research_paulson_shanks_1961]\] \[[Persoon et al 1980][research_persoon_1980]\] \[[Powers and Sarrafian 1986][research_powers_sarrafian_1986]\] \[[Quagliarella and Iuliano 2017][research_quagliarella_iuliano_2017]\] \[[Rogers 2004][research_rogers_2004]\] \[[Scordamaglia et al 2025][research_scordamaglia_2025]\] \[[Shang 2007][research_shang_2007]\] \[[Shi et al 2023][research_shi_2023_2]\] \[[Shmilovich and Princen 2026][research_shmilovich_princen_2026]\] \[[Strailman 1952][research_strailman_1952]\] \[[Swaim 1970][research_swaim_1970]\] \[[Takeda 1970][research_takeda_1970]\] \[[Vile et al 2020][research_vile_2020]\] \[[Wagdi 1977][research_wagdi_1977]\] \[[Whitaker et al 1977][research_whitaker_1977]\] \[[Wolowicz and Yancey 1973][research_wolowicz_yancey_1973]\] \[[Xie et al 2023][research_xie_2023]\] \[[Xu et al 2020][research_xu_2020]\] \[[Yang and Gao 2020][research_yang_gao_2020]\] \[[Zhang et al][research_yang_zhang]\]

### Aerodynamics, airfoils and aerodynamic design

Airfoils, boundary layers, high-lift and laminar flow, computational aerodynamics and aerodynamic design.

**62 records.** \[[Addessio and Skifstad 1975][research_addessio_skifstad_1975]\] \[[Atkin 2001][research_atkin_2001]\] \[[Bernot 1979][research_bernot_1979]\] \[[Bishara et al 2018][research_bishara_2018]\] \[[Borodulin et al 2017][research_borodulin_2017]\] \[[Bright et al 2013][research_bright_2013]\] \[[Calvert 1950][research_calvert_1950]\] \[[Chaudhuri 1977][research_chaudhuri_1977]\] \[[Chernyshev et al 2019][research_chernyshev_2019]\] \[[Coder and Somers 2020][research_coder_somers_2020]\] \[[Collier et al 1990][research_collier_1990]\] \[[Cordner 1967][research_cordner_1967]\] \[[Corson 1941][research_corson_1941]\] \[[Drakin 1963][research_drakin_1963]\] \[[Englar 1970][research_englar_1970]\] \[[Fejtek 1993][research_fejtek_1993]\] \[[Gardner and Downey 1950][research_gardner_downey_1950]\] \[[Greenhalgh 1983][research_greenhalgh_1983]\] \[[Greer et al 1999][research_greer_hamory_1999]\] \[[Greer et al 2000][research_greer_2000]\] \[[Hansmann and Stumpf 2026][research_hansmann_stumpf_2026]\] \[[Head and Hohenemser 1951][research_head_hohenemser_1951]\] \[[High-Fidelity Aerodynamic Models 2015][research_high_fidelity_aerodynamic_2015]\] \[[Human-Powered Aircraft Wing Design A Case Study in 2014][research_human_powered_aircraft_2014]\] \[[Introduction to Aircraft Aerodynamic Design 2021][research_introduction_to_2021]\] \[[Jones 1964][research_jones_1964]\] \[[Katz and Maskew 1988][research_katz_maskew_1988]\] \[[Keller 2019][research_keller_2019]\] \[[khan and Padhy 2019][research_khan_padhy_2019]\] \[[Kubrynski 1999][research_kubrynski_1999]\] \[[Lamar et al 1981][research_lamar_1981]\] \[[Lange and Gieseler 1953][research_lange_gieseler_1953]\] \[[Larrabee 1975][research_larrabee_1975]\] \[[Lindstrom et al 1970][research_lindstrom_rebeske_1970]\] \[[Livescu 2016][research_livescu_2016]\] \[[Matheson 1987][research_matheson_1987]\] \[[May and Widdison 1971][research_may_widdison_1971]\] \[[Meyer and Jiran 1981][research_meyer_jiran_1981]\] \[[Mokhtari et al 2020][research_mokhtari_2020]\] \[[Murillo and McMasters 1984][research_murillo_mcmasters_1984]\] \[[NACA Conference on High-speed Aerodynamics. a Compilation 1958][research_naca_conference_1958]\] \[[Nie et al 2025][research_nie_2025]\] \[[Obayashi 1999][research_obayashi_1999]\] \[[Olson 2015][research_olson_2015]\] \[[Otsuka et al 2017][research_otsuka_2017]\] \[[Pivko 1956][research_pivko_1956]\] \[[Quick 1937][research_quick_1937]\] \[[Roy 2009][research_roy_2009]\] \[[Shindo and Joppa 1980][research_shindo_joppa_1980]\] \[[Sidhu 2023][research_sidhu_2023]\] \[[Tai 1993][research_tai_1993]\] \[[Tokugawa et al 2026][research_tokugawa_2026]\] \[[Vaughn et al 2008][research_vaughn_miltone_2008]\] \[[Wang 1980][research_wang_1980]\] \[[Wang 2026][research_wang_2026]\] \[[Williams and Howe 1970][research_williams_howe_1970]\] \[[Wing Design Considerations 2021][research_wing_design_2021]\] \[[Yang][research_yang]\] \[[Yih et al 1952][research_yih_1952]\] \[[Zhang 2026][research_zhang_2026_8]\] \[[Zhang et al 2015][research_zhang_2015_2]\] \[[Zhu et al 2023][research_zhu_2023]\]

### Airframe noise, cabin noise and vibration

Noise from the airframe itself, noise and vibration inside the aircraft, and the paths between them.

**62 records.** \[[Bolds 1961][research_bolds_1961]\] \[[Bolds 1962][research_bolds_1962]\] \[[Burley 1974][research_burley_1974]\] \[[Choudhari et al 2011][research_choudhari_2011]\] \[[Clarkson and Mead 1973][research_clarkson_mead_1973]\] \[[Dalan and Cohen 1985][research_dalan_cohen_1985]\] \[[Dobrzynski 1981][research_dobrzynski_1981]\] \[[Doherty and Butzel 1979][research_doherty_butzel_1979]\] \[[Doherty and Butzel 1979][research_doherty_butzel_1979_2]\] \[[Douglas Aircraft Co Long Beach Ca 1963][research_douglas_aircraft_co_long_beach_ca_1963]\] \[[Elkoby et al 2007][research_elkoby_2007]\] \[[Esnault][research_esnault]\] \[[Fink 1979][research_fink_1979]\] \[[Fink and Schlinker 1980][research_fink_schlinker_1980]\] \[[Ford 2004][research_ford_2004]\] \[[Grosveld 1985][research_grosveld_1985]\] \[[Grosveld 1988][research_grosveld_1988]\] \[[Grosveld et al 1980][research_grosveld_navaneethan_1980]\] \[[Heitman and Mixson 1986][research_heitman_mixson_1986]\] \[[Heller and Dobrzynski 1977][research_heller_dobrzynski_1977]\] \[[Howe 1978][research_howe_1978]\] \[[Howe 1981][research_howe_1981]\] \[[Howe 1999][research_howe_1999]\] \[[Howlett 1979][research_howlett_1979]\] \[[Humphreys et al 2016][research_humphreys_2016]\] \[[Hutchins 1972][research_hutchins_1972]\] \[[Kholodar 2016][research_kholodar_2016]\] \[[Khorrami et al 2009][research_khorrami_2009]\] \[[Kuantama et al 2019][research_kuantama_2019]\] \[[Kuhn 1975][research_kuhn_1975]\] \[[Landmann et al 1989][research_landmann_1989]\] \[[Langer and Blech 2019][research_langer_blech_2019]\] \[[Lauchle and Park 2002][research_lauchle_park_2002]\] \[[Lockard et al 2008][research_lockard_2008]\] \[[Mayes and Edge 1962][research_mayes_edge_1962]\] \[[Mixson et al 1977][research_mixson_barton_1977]\] \[[Morgan and Hardin 1975][research_morgan_hardin_1975]\] \[[Probst et al 2017][research_probst_2017]\] \[[Ravetta et al 2019][research_ravetta_2019]\] \[[Ride quality of crew-manned military aircraft 1975][research_ride_quality_1975]\] \[[Shaw et al 1988][research_shaw_1988]\] \[[Sikora and Mendenhall 1974][research_sikora_mendenhall_1974]\] \[[Simpson 1990][research_simpson_1990]\] \[[Soovere 1982][research_soovere_1982]\] \[[Soovere 1985][research_soovere_1985]\] \[[Strelkov and Kharlamov 1967][research_strelkov_kharlamov_1967]\] \[[Takahashi et al 2023][research_takahashi_2023]\] \[[The measurement and analysis of aircraft vibration 1976][research_the_measurement_1976]\] \[[Thomas 1961][research_thomas_1961_2]\] \[[Thomas 1961][research_thomas_1961]\] \[[Townsend 1966][research_townsend_1966]\] \[[Turkdogru Gurun et al 2021][research_turkdogru_gurun_2021]\] \[[Unruh 1981][research_unruh_1981]\] \[[Unruh et al 2002][research_unruh_2002]\] \[[Vaicaitis 1980][research_vaicaitis_1980]\] \[[Vaicaitis and Mixson 1985][research_vaicaitis_mixson_1985]\] \[[Wanglomklang et al 2025][research_wanglomklang_2025]\] \[[Wilby 1982][research_wilby_1982]\] \[[Williams 2002][research_williams_2002]\] \[[Winter 2023][research_winter_2023]\] \[[Yamamoto et al 2023][research_yamamoto_2023]\] \[[Zheng 2021][research_zheng_2021]\]

### Surveillance, reconnaissance and observation

Surveillance, reconnaissance and night observation aircraft, manned and unmanned, and their sensors.

**54 records.** \[[Abich IV et al 2016][research_abich_iv_2016]\] \[[Amelin 2022][research_amelin_2022]\] \[[Anderson 1976][research_anderson_1976]\] \[[Bailey and McClintic 1974][research_bailey_mcclintic_1974]\] \[[Beech Aircraft Corp Wichita Ks 1966][research_beech_aircraft_corp_wichita_ks_1966]\] \[[Bell Aerospace Co Buffalo Ny 1955][research_bell_aerospace_co_buffalo_ny_1955]\] \[[Bell Aerospace Co Buffalo Ny 1955][research_bell_aerospace_co_buffalo_ny_1955_2]\] \[[Bell Aerospace Co Buffalo Ny 1957][research_bell_aerospace_co_buffalo_ny_1957]\] \[[Belsky 2022][research_belsky_2022]\] \[[Blosser 1952][research_blosser_1952]\] \[[Blosser 1953][research_blosser_1953]\] \[[Bracken and Grotte 1979][research_bracken_grotte_1979]\] \[[Bucklew 2009][research_bucklew_2009]\] \[[Clark 2013][research_clark_2013]\] \[[Cornell Aeronautical Lab Inc Buffalo Ny 1971][research_cornell_aeronautical_lab_inc_buffalo_ny_1971]\] \[[Cornell Aeronautical Lab Inc Buffalo Ny 1971][research_cornell_aeronautical_lab_inc_buffalo_ny_1971_2]\] \[[Cornell Aeronautical Lab Inc Buffalo Ny 1971][research_cornell_aeronautical_lab_inc_buffalo_ny_1971_3]\] \[[Dunnavan 1983][research_dunnavan_1983]\] \[[Fisher et al 1956][research_fisher_1956]\] \[[Forsythe 1946][research_forsythe_a_c_r_1946]\] \[[Frazier 2016][research_frazier_2016]\] \[[Hasan et al 2018][research_hasan_2018]\] \[[Henderson 1978][research_henderson_1978]\] \[[High altitude reconnaissance aircraft design 1989][research_high_altitude_1989]\] \[[Hinds and Shames 1975][research_hinds_shames_1975]\] \[[Holley and Irving B. 1946][research_holley_irving_b_1946]\] \[[Huang et al 2018][research_huang_2018]\] \[[Januszewska and Pringle 2021][research_januszewska_pringle_2021]\] \[[Kisabo et al 2017][research_kisabo_2017]\] \[[Koper 1976][research_koper_1976]\] \[[Kumar 1997][research_kumar_1997]\] \[[Leahy et al 2015][research_leahy_2015]\] \[[Lempert 1975][research_lempert_1975]\] \[[Lowrance and Smith 1996][research_lowrance_smith_1996]\] \[[Mack 2003][research_mack_2003]\] \[[McQUILLEN and Huang 1971][research_mcquillen_huang_1971]\] \[[Meullen et al 1956][research_meullen_1956]\] \[[Olsen et al 2019][research_olsen_2019]\] \[[Quirion and Liu 2020][research_quirion_liu_2020]\] \[[Rader 1989][research_rader_1989]\] \[[Reconnaissance and Auxiliary Aircraft 2008][research_reconnaissance_and_2008]\] \[[Rexcharles Enyinna Donatus et al 2026][research_rexcharles_enyinna_donatus_2026]\] \[[Rutherford and Crowder 1958][research_rutherford_crowder_1958]\] \[[Sakthivel and Venkatesan 2017][research_sakthivel_venkatesan_2017]\] \[[Schutz and Kutrzyba 2000][research_schutz_kutrzyba_2000]\] \[[Setiawan et al 2026][research_setiawan_2026]\] \[[SlEWERT and Stewart 1967][research_slewert_stewart_1967]\] \[[Stottier 1995][research_stottier_1995]\] \[[Tittel 2010][research_tittel_2010]\] \[[Uhl 2003][research_uhl_2003]\] \[[Whittingham and Swan 1960][research_whittingham_swan_1960]\] \[[Widger 1963][research_widger_1963]\] \[[Yazdi 1991][research_yazdi_1991]\] \[[Zhen 2019][research_zhen_2019]\]

### Electric, hybrid-electric and solar-powered aircraft

Electric, hybrid-electric, solar and fuel cell propulsion, where a title names no other cluster's subject. **36 of the 41 records date from 2015 or later.**

**41 records.** \[[Simmons et al][research_benjamin_m_simmons]\] \[[Binghua and Hui 2021][research_binghua_hui_2021]\] \[[Brinza et al 2026][research_brinza_2026]\] \[[Buckley et al 2020][research_buckley_2020]\] \[[Cahn et al 1966][research_cahn_1966]\] \[[Danjuma 2022][research_danjuma_2022]\] \[[Danjuma et al 2021][research_danjuma_2021]\] \[[Development and Application of Solar-Powered Aircraft Technology 2025][research_development_and_2025]\] \[[Doyle 2020][research_doyle_2020]\] \[[Dr. Olivia Davis 2021][research_dr_olivia_davis_2021]\] \[[Figueira et al 2025][research_figueira_2025]\] \[[Finger et al 2020][research_finger_2020_2]\] \[[Gong 2024][research_gong_2024]\] \[[Green 1931][research_green_1931]\] \[[Hace 2019][research_hace_2019]\] \[[Hoelzen et al 2018][research_hoelzen_2018]\] \[[Hu et al 2026][research_hu_2026]\] \[[In-Flight Testing into Atmospheric Electricity for Future Aircraft 2025][research_in_flight_testing_2025]\] \[[Isikveren 2018][research_isikveren_2018]\] \[[Kellermann et al 2020][research_kellermann_2020]\] \[[Likhite 2022][research_likhite_2022]\] \[[Lim et al 2023][research_lim_2023]\] \[[Lobitz et al 2023][research_lobitz_2023]\] \[[Mukhachev et al 2022][research_mukhachev_2022]\] \[[Nasoulis et al 2022][research_nasoulis_2022]\] \[[Ogawa et al 2015][research_ogawa_2015]\] \[[Palaia et al 2023][research_palaia_2023]\] \[[Pornet and Isikveren 2015][research_pornet_isikveren_2015]\] \[[Prasannakumar et al 2024][research_prasannakumar_2024]\] \[[Reid et al 2024][research_reid_2024]\] \[[Reiquam 1982][research_reiquam_1982]\] \[[Riboldi 2018][research_riboldi_2018]\] \[[Staats et al 2025][research_staats_2025]\] \[[Schnulo et al][research_sydney_schnulo]\] \[[Tuck et al 2018][research_tuck_2018]\] \[[Wahler et al 2025][research_wahler_2025_2]\] \[[Wall and Meyer 2020][research_wall_meyer_2020]\] \[[Wen et al 2023][research_wen_2023]\] \[[Yang et al 2019][research_yang_2019_2]\] \[[Zhu et al 2016][research_zhu_2016]\] \[[Жданов and Зінченко 2015][research___2015]\]

### Flight dynamics, stability and simulation models

Flight dynamics models, longitudinal and dynamic stability, simulation and the response to turbulence.

**35 records.** \[[Abhishek and Prasad 2016][research_abhishek_prasad_2016]\] \[[Abzug and DaRos 1955][research_abzug_daros_1955]\] \[[An Introduction to the Longitudinal Static Stability of 1966][research_an_introduction_1966]\] \[[Antipov 2020][research_antipov_2020]\] \[[Aziz and Loya 2025][research_aziz_loya_2025]\] \[[Barnes and Yager 1985][research_barnes_yager_1985]\] \[[Beeman 1972][research_beeman_1972]\] \[[Beyers 1983][research_beyers_1983]\] \[[Beyers 1988][research_beyers_1988]\] \[[Churchill and Dugan 1982][research_churchill_dugan_1982]\] \[[Ferguson and Thomson 2015][research_ferguson_thomson_2015]\] \[[Ferguson et al 1984][research_ferguson_hanson_1984]\] \[[Grantham et al 1974][research_grantham_nguyen_1974]\] \[[Grubin 1972][research_grubin_1972]\] \[[Gupta et al 2016][research_gupta_2016]\] \[[Hacker and Wroblewski 2009][research_hacker_wroblewski_2009]\] \[[Hitzel and Zimper 2018][research_hitzel_zimper_2018]\] \[[Houbolt 1971][research_houbolt_1971]\] \[[Houck et al 1977][research_houck_moore_1977]\] \[[Juhasz et al 2022][research_juhasz_2022]\] \[[Metodiev 2025][research_metodiev_2025]\] \[[Montalvo and Costello 2015][research_montalvo_costello_2015]\] \[[Moul and Brown 1959][research_moul_brown_1959]\] \[[Nagabhushan 1983][research_nagabhushan_1983]\] \[[Oruc et al 2017][research_oruc_2017]\] \[[Phillips 1975][research_phillips_1975]\] \[[Reid 1978][research_reid_1978]\] \[[Rodgers 1966][research_rodgers_1966]\] \[[Shayak et al 2024][research_shayak_2024]\] \[[Steiner and Pratt 1967][research_steiner_pratt_1967]\] \[[Thelander 1965][research_thelander_1965]\] \[[Thorson and Bohne 1960][research_thorson_bohne_1960]\] \[[Trevino 1986][research_trevino_1986]\] \[[Yuan et al 2019][research_yuan_2019]\] \[[Yuan et al 2020][research_yuan_2020]\]

### Other aeronautical literature

**The residual, reported and not hidden.** Records about a whole aircraft that belong to no other cluster in the table, including configuration and design studies, air data, test capability and the hazards of low-level operation.

**It holds 0.9 percent of the survey and is heterogeneous**, with no family in it large enough to name as a literature of its own.

**30 records.** \[[Abdukayumov 2022][research_abdukayumov_2022]\] \[[Air Force Test Pilot School Edwards Afb Ca 1994][research_air_force_test_pilot_school_edwards_afb_ca_1994_2]\] \[[Bailey et al 1996][research_bailey_knoedler_1996]\] \[[Bevilaqua 2021][research_bevilaqua_2021]\] \[[Bryant 1963][research_bryant_1963]\] \[[Carico 1995][research_carico_1995]\] \[[Coiro and Nicolosi 2001][research_coiro_nicolosi_2001]\] \[[Continental Army Command Fort Monroe Va 1958][research_continental_army_command_fort_monroe_va_1958]\] \[[Dynamic Response Analysis of a High Glide Ratio Parachute 2021][research_dynamic_response_2021]\] \[[Engblom et al 2016][research_engblom_2016]\] \[[Ericsson 1987][research_ericsson_1987]\] \[[Finch and Matranga 1959][research_finch_matranga_1959]\] \[[Forehand and Bair 1969][research_forehand_bair_1969]\] \[[General Aviation Aircraft Design 2022][research_general_aviation_2022]\] \[[Graves 1982][research_graves_1982]\] \[[Guidry et al 2001][research_guidry_2001]\] \[[High-Speed Water-Based Aircraft 1953][research_highspeed_waterbased_1953]\] \[[Hightower 1985][research_hightower_1985]\] \[[Hom et al 1983][research_hom_1983]\] \[[Ivanković et al 2023][research_ivankovic_2023]\] \[[Kristl et al 1999][research_kristl_1999]\] \[[Miller et al 1983][research_miller_1983]\] \[[Murphy et al 2019][research_murphy_frink_2019]\] \[[Nam and Mavris 2018][research_nam_mavris_2018]\] \[[Petrescu et al 2017][research_petrescu_2017]\] \[[Ralles 1966][research_ralles_1966]\] \[[Smith and Bernier 1966][research_smith_bernier_1966]\] \[[Thompson 2014][research_thompson_2014]\] \[[Wild 1966][research_wild_1966]\] \[[Zhu et al 2023][research_zhu_2023_2]\]

### Wind tunnels, models and test technique

Wind tunnels, their control and corrections, and model test technique.

**26 records.** \[[Anderson 1968][research_anderson_1968]\] \[[Bamber 1961][research_bamber_1961]\] \[[Billingsley 1976][research_billingsley_1976]\] \[[Bliss 1980][research_bliss_1980]\] \[[Boswell 1970][research_boswell_1970]\] \[[Butler 1976][research_butler_1976]\] \[[Cook 1964][research_cook_1964]\] \[[Czysz 1963][research_czysz_1963]\] \[[Diggins 1951][research_diggins_1951]\] \[[Dowell and Bliss 1978][research_dowell_bliss_1978]\] \[[Emslie 1966][research_emslie_1966]\] \[[Feistel et al 1981][research_feistel_1981_2]\] \[[Hoehne 1967][research_hoehne_1967]\] \[[Hunton and James Harry A. 1948][research_hunton_james_harry_a_1948]\] \[[Kashitani et al 2019][research_kashitani_2019]\] \[[Kilgore and Averett 1964][research_kilgore_averett_1964]\] \[[Mennell 1975][research_mennell_1975]\] \[[Muhlstein and Coe 1979][research_muhlstein_coe_1979]\] \[[Nicolaides 1971][research_nicolaides_1971]\] \[[Petty 1975][research_petty_1975]\] \[[Rittenhouse 1959][research_rittenhouse_1959]\] \[[Stallings and Hartman 1981][research_stallings_hartman_1981]\] \[[Wallace 1952][research_wallace_1952]\] \[[Whittley and Garland 1961][research_whittley_garland_1961]\] \[[Wind Tunnel Balance and Calibration Machine 1974][research_wind_tunnel_1974]\] \[[Winther et al 1981][research_winther_1981]\]

### Rotorcraft and vertical lift flight mechanics

Helicopter, tilt-rotor and other vertical lift flight mechanics, hover and their test facilities, where a title names no other cluster's subject.

**12 records.** \[[Cox and Abbott 1966][research_cox_abbott_1966]\] \[[Culpepper and Murphy 1979][research_culpepper_murphy_1979]\] \[[Durbin and McGeer 1982][research_durbin_mcgeer_1982]\] \[[Edenborough 1968][research_edenborough_1968]\] \[[Heyson 1980][research_heyson_1980]\] \[[Kelley et al 1986][research_kelley_phelps_1986]\] \[[Magee and Taylor 1971][research_magee_taylor_1971_2]\] \[[Olson 1978][research_olson_1978]\] \[[Reader 1976][research_reader_1976]\] \[[Reilly 1970][research_reilly_1970]\] \[[Swaim 1969][research_swaim_1969]\] \[[Zhang and Xia 2017][research_zhang_xia_2017]\]

## Where the Framing Breaks Down

**Treating this as one aircraft is a convenience of the designation system and not a fact.** The X-26A and
the X-26B share an airframe and share nothing else. They had different customers, different services,
different missions and different decades of relevance.
**An article organised around the shared lift-to-drag ratio is making an argument, and the reader should know it is an argument.**

**The unifying claim is real but it is not a claim about intent.** Nobody at the Naval Test Pilot School
chose the SGS 2-32 because its aspect ratio implied a low power requirement, and nobody at Lockheed chose it
because its wing produced instructive adverse yaw.
**Each programme chose it for its own reason and the common cause is visible only in retrospect.** The
article derives the connection and does not assert that anyone at the time saw it.

**Neither aircraft was developed and neither answered an aerodynamic unknown**, which is the same finding
the previous article made about the [X-25][related_post_a322_bensen_x25].
**Two consecutive designations went to off-the-shelf civil aircraft bought for their existing properties.**
That is evidence about the designation system, and it belongs with the rest of it in the closing article of
this series. The vehicle-by-vehicle record for the series generally is [Jenkins, Landis and Miller on the
American X-vehicles][book_jenkins_landis_miller_2003].

**Finally, the three lost airframes are unexplained here.** Three of four X-26As were destroyed and
replaced. A docile sailplane operated by an organisation of professional test pilots should not have that
record, and this article does not know why it does.
**It is stated as an open question and not smoothed over**, because the obvious inference, that an aircraft
used to demonstrate departures will occasionally depart, is exactly the kind of plausible reasoning that
should not be presented as fact.

## The Source Base

**The aircraft has almost no technical literature.**
Of the 3,484 research records in this article's references, **seven** carry the X-26, Schweizer, the SGS, the QT-2, the Q-Star or the YO-3 in their titles, and **none is about either X-26**. Two concern a different Schweizer sailplane, the SGS 1-36, in a National Aeronautics and Space Administration flutter clearance and a study of its flight at very high angles of attack, in [Kehoe and Ellison 1985][research_kehoe_ellison_1985] and [Sim 1990][research_sim_1990]. One names the Q-Star as an experimental quiet aircraft, in [Griffith 1971][research_griffith_1971]. The other four concern the YO-3A, which is the QT-2's operational descendant.
**The Army's preliminary evaluation of the YO-3A is the only evaluation of the type in its operational role among them**, in [Condon et al 1970][research_condon_1970], and the remaining three come from the later research use of the aircraft, a measurement of its propeller thrust and torque in [Ormsbee et al 1977][research_ormsbee_siddiqi_1977] and its work as an acoustic research aircraft in [Cross and Watts 1983][research_cross_watts_1983] and [Cross 1984][research_cross_1984]. The specifications come from sailplane references and museum material, and the operational detail from historical accounts rather than from test reports.

**That is a property of the procurement.** An off-the-shelf aircraft bought for properties it already has
generates no development literature, because nothing was developed, and the
[X-25][related_post_a322_bensen_x25] is the same case.

**The supporting physics is abundant on one side and thinner on the other.** Lateral control and adverse yaw are extremely well documented once the period's own vocabulary is used, in the cluster on lateral control, ailerons and adverse yaw, and the propeller-noise and propagation literature is substantial.
**74 of that cluster's 180 records date from before 1970**, and its titles are phrased in terms of ailerons, spoilers, rudders, rolling and yawing moment and lateral control, while the count under Thin Subjects shows how rarely a title uses the bare term adverse yaw.

**The research survey holds 3,484 research records drawn from Crossref, the National Aeronautics and Space Administration's Technical Reports Server and the Defense Technical Information Center**, of which 1,063 are report primaries, being 30.5 percent, by the identifier rule set out under The Definition of Primary. **The median publication year is 2001.** Of the 3,441 dated records, 678 were published in 1971 or earlier, by which year the YO-3A had finished operating in Vietnam, being 19.7 percent, and 1,495 were published in 2015 or later, being 43.4 percent.

### The Definition of Primary

**Primacy is a property of the document, and this survey derives it from the identifier.** A record is a report primary when its address is on the National Aeronautics and Space Administration's Technical Reports Server or it carries a digital object identifier under the 10.21236 prefix, which Crossref registers for Defense Technical Information Center reports. **The period reports on lateral control, propeller noise and sound propagation that carry this article's argument are report primaries under that rule**, and so are the Army's evaluation of the YO-3A, the YO-3A propeller study and the YO-3A systems manual. **The rule does not reach the journal and conference papers among the first-hand sources**, such as the in-flight acoustic test technique of the YO-3A and the papers on atmospheric absorption in the Journal of the Acoustical Society of America, so 30.5 percent is a lower bound on how much of the survey is first-hand.

### Thin Subjects

**Seven subjects that this article's derivations depend on have thin literatures.** Each count below is the number of research records in this survey whose title carries at least one of the listed terms, with a hyphen read as a space.

| Subject | Title terms counted | Records |
|---|---|---|
| Adverse yaw named as such | adverse yaw, proverse yaw | 7 |
| The glide ratio, best glide and minimum sink | glide ratio, best glide, glide performance, gliding performance, minimum sink, sink rate, sinking speed, sink speed, speed polar, glide speed | 16 |
| Power required and the minimum-power speed | power required, minimum power, maximum endurance | 13 |
| The test pilot schools | test pilot school, test pilot schools | 12 |
| The transfer of training from one device to another | transfer of training, training transfer, transfer effectiveness, quasi transfer | 6 |
| Hearing an aircraft, its audibility and aural detection | aural, audibility, audible, nondetectability, non detectability | 15 |
| The ambient noise and masking that set a detection threshold | ambient noise, background noise, ambient acoustic, ambient soundscape, masking, masker | 10 |

**Adverse yaw is documented under other names.** Seven titles name adverse or proverse yaw, one of them from before 2017, while the lateral control cluster holds 180 records on ailerons, rolling and yawing moments and lateral control, so the X-26A's lesson rests on the period's vocabulary rather than on its own name.

**Glide performance is carried by the sailplane literature rather than named.** Of the 16 titles that name a glide ratio, best glide or sink rate, one names a sailplane, and the sailplane cluster holds 178 records.

**Power required has almost no period literature under its own name.** Thirteen titles name power required, a minimum-power speed or maximum endurance, and one of them dates from before 2000, so the distinction between best glide and minimum power rests on the standard performance relation derived above, which the performance cluster treats inside range, endurance and drag.

**The test pilot schools are described rather than studied.** Twelve titles name a test pilot school, one of them the Naval Test Pilot School, and none names a sailplane.

**The X-26A's central claim has no direct literature.** Six titles name the transfer of training, all six of them from 2015 or later and all concerning simulators or virtual reality, and none compares a sailplane with another device.

**Detection by ear was a period subject.** Of the 15 titles that name hearing an aircraft, its audibility or aural detection, six date from before 1980, and the later ones concern noise contours, prediction codes, rotorcraft and cockpit alerts.

**The ambient threshold is rarely the subject of a title.** Ten titles name ambient noise, background noise or masking, and four of them concern detection, while the rest concern annoyance and perception.

### What the Survey Admits

**A record is admitted only when a person reading its title finds it on this article's subject.** The subject is the aircraft, manned or unmanned, and its flight, performance, stability, control, flight test and noise, together with the propagation and detection of sound in the atmosphere and the training and safety of the people who fly. Many words this subject depends on also name something else, and a record that shares only such a word is excluded. Glider also names the ocean glider, a gliding mammal and a mathematical object, and soaring also appears as a figure of speech in politics and literature. Propeller also names the ship's propeller and the ventilation fan, rudder also names a ship's rudder and several artists, and aileron also names a pharmaceutical company. Upset also names single-event upset in electronic memory, startle also names the startle response in clinical and animal research, aspect ratio also names a property of honeycomb cores and roughness elements, and noise also names noise in the radar and radio sense. Audibility is also a question of alarms, sirens, train horns and dwellings, and detection also belongs to seismology and to explosives screening. A neutral title on propeller theory or blade stress that appears in the Journal of Ship Research or International Shipbuilding Progress is treated as marine work and excluded. Satellites, spacecraft attitude, ballistic projectiles, ballistic re-entry bodies and launch vehicles are excluded, and so are unmanned aircraft used only as instruments for another discipline, such as crop, peatland and rock-wall surveys. The winged space shuttle orbiter is kept for its gliding flight. Correction notices, peer-review records, figure records, encyclopedia and dictionary entries, standards and recommended practices, and news items are excluded as well, because a survey counts research works. Book reviews are not admitted either, and nor is a second deposit of a document already held, such as a report-server copy of a meeting paper whose own record is kept, because counting it would count one work twice. The residual cluster admits a record only when its title concerns a whole aircraft's configuration, design, flight or operation and no named cluster fits it, and a record whose only link to this article is the aircraft as a structure, its landing gear and tyres, ground equipment, maintenance or law is excluded.

**Some records of doubtful relevance are kept.** Muffler designs for engines other than aircraft engines are kept, because the acoustics of an exhaust silencer does not depend on the vehicle. Unmanned aircraft flown as observers of wildlife, fire, roads and the sea are kept, because persistent low-altitude observation is the mission the X-26B's line carried. Missile wing aerodynamics, aircraft weather reconnaissance, the flight mechanics of birds, and law on unmanned aircraft are kept, because each shares this subject's physics or its mission, and a reader may weigh each accordingly.

**Every research title has been read for relevance, so the off-topic share that remains is a matter of reading judgement.** A reading of titles cannot show that a work is relevant in substance, so this is a statement about titles only.

## Epistemic State

**Historical fact, from the public record.** The X-26A is an unmodified Schweizer SGS 2-32 operated by the
United States Naval Test Pilot School for flying-qualities instruction. Four were ordered and three were
lost and replaced. Two airframes, serials 67-15345 and 67-15346, were converted by Lockheed Missiles and
Space Company to QT-2 and QT-2PC configuration with a Continental O-200 of 100 horsepower driving a
four-blade propeller through an extension shaft. Two aircraft arrived at Soc Trang on 22 January 1968 and
flew 591 hours of night surveillance between 24 January and 24 March 1968. The specification called for
acoustic undetectability at 1,500 feet, the aircraft was first heard at 750 in passes over the airfield, and
missions were flown no lower than 800. The aircraft returned in 1969 and were redesignated X-26B. The work
continued through the Q-Star to the YO-3A, which operated in Vietnam during 1970 and 1971, although the
accounts disagree on how many were built and when operations began.

**Engineering analysis, derived here and checkable.** That adverse yaw is proportional to lift coefficient
follows from the classical elliptic-loading result. That the observability index scales as wing loading
times span over the cube of speed and the directional stiffness, with the helix angle cancelling, is
algebra. The 6.02 decibels per doubling of range is exact for spherical spreading. The statement that the
QT-2PC missed its specification by one doubling follows from the two reported distances and nothing else.

**Assumed, and marked as such throughout.** The Oswald efficiency of 0.90 and zero-lift drag coefficient of
0.012. Every quantity describing the comparison jet trainer. The helix angles and directional stiffnesses of
both aircraft. The QT-2PC gross weight of 2,400 pounds and its lift-to-drag ratio of 20. The 40 dBA night
ambient. The propeller diameters and speeds. **None of these is a measurement of an X-26.**

**Inference, and labelled as inference.** That the two programmes selected the same airframe for reasons
traceable to a single property is an inference drawn here, **not a documented rationale**, and the article
says so under Where the Framing Breaks Down. That the acoustic limit moved to the exhaust and airframe once
the propeller was slowed follows from the tip-speed arithmetic being far larger than the shortfall,
**but no source consulted states which term actually dominated**.

**What the record does not settle.** Why three of four X-26A airframes were lost. The QT-2PC's actual gross
weight, drag polar and propeller geometry. What the measured sound level was at any stated distance, as
opposed to the detection distance. Whether the 1,500 foot specification was ever met by any aircraft in the
line. How long the X-26A actually remained in service, which sources describe loosely as decades.

**Written from current knowledge.** The contemporary survey postdates the editorial date of this article.

## Out of Scope

The sensor packages the QT-2PC and YO-3A carried, including low-light television and infrared. The tactical
conduct of night observation operations. The Schweizer company history and the American soaring movement.
Sailplane structural design and certification. Psychoacoustics and the perception of aircraft noise, as
distinct from its physical propagation. The YO-3A's own programme, which deserves its own treatment. Modern
active noise control.

## Conclusion

**The Schweizer X-26 is one airframe, two aircraft, and a single number.**

A high lift-to-drag ratio requires a long slender wing, and a long slender wing flown slowly produces
adverse yaw four and a half times larger than a jet's and seventeen times slower, which is why the Naval
Test Pilot School could teach with it.
**The same high lift-to-drag ratio means the aircraft needs twenty-four horsepower of the hundred it carries**,
which is why Lockheed could throttle the engine, bury it in mufflers, and turn a large propeller slowly
enough to be inaudible beyond 750 feet.

**The two programmes wanted opposite things and both got them from the same property.** One wanted a fault
made visible. The other wanted an aircraft made absent.

**Neither aircraft was developed.** Both were bought off the shelf for properties a sailplane manufacturer
had already optimised for entirely unrelated reasons, which is the second consecutive time this series has
found that, and is evidence about the designation system rather than about aeroplanes.

The next article in this series takes up the Lockheed X-27.
## References

### Books

- [Beranek on noise and vibration control][book_beranek_1988]
- [Etkin and Reid on flight dynamics][book_etkin_reid_1996]
- [Goldstein's aeroacoustics][book_goldstein_1976]
- [Hoerner's compendium][book_hoerner_1965]
- [Hurt's aerodynamics for naval aviators][book_hurt_1965]
- [Jenkins, Landis and Miller on the American X-vehicles][book_jenkins_landis_miller_2003]
- [McCormick][book_mccormick_1979]
- [Perkins and Hage][book_perkins_hage_1949]
- [Pierce on acoustics][book_pierce_1981]
- [Thomas on sailplane design][book_thomas_1999]

[book_beranek_1988]: https://openlibrary.org/works/OL9166941W
[book_etkin_reid_1996]: https://openlibrary.org/works/OL19844466W
[book_goldstein_1976]: https://openlibrary.org/works/OL6915157W
[book_hoerner_1965]: https://openlibrary.org/works/OL5289632W
[book_hurt_1965]: https://openlibrary.org/works/OL4297319W
[book_jenkins_landis_miller_2003]: https://openlibrary.org/works/OL20394726W
[book_mccormick_1979]: https://openlibrary.org/works/OL1968708W
[book_perkins_hage_1949]: https://openlibrary.org/works/OL36764926W
[book_pierce_1981]: https://openlibrary.org/works/OL4812143W
[book_thomas_1999]: https://openlibrary.org/works/OL512230W

### Reference

- [adverse yaw][ref_adverse_yaw]
- [Albertson, Flying on the QT][ref_albertson_2015]
- [Continental O-200][ref_continental_o200]
- [Dutch roll][ref_dutch_roll]
- [Naval Test Pilot School][ref_usntps]
- [Patuxent River][ref_patuxent]
- [Polmar, Historic Aircraft, Silent (By) Night][ref_polmar_2017]
- [Schweizer Aircraft][ref_schweizer_aircraft]
- [Schweizer SGS 2-32][ref_sgs_2_32]
- [X-26][ref_x26]
- [X-26A][ref_navair_x26a]
- [YO-3A][ref_yo3a]

[ref_adverse_yaw]: https://en.wikipedia.org/wiki/Adverse_yaw
[ref_albertson_2015]: https://armyaviationmagazine.com/flying-on-the-qt/
[ref_continental_o200]: https://en.wikipedia.org/wiki/Continental_O-200
[ref_dutch_roll]: https://en.wikipedia.org/wiki/Dutch_roll
[ref_navair_x26a]: https://www.navair.navy.mil/product/x-26a-frigate-glider
[ref_patuxent]: https://en.wikipedia.org/wiki/Naval_Air_Station_Patuxent_River
[ref_polmar_2017]: https://www.usni.org/magazines/naval-history-magazine/2017/october/historic-aircraft-silent-night
[ref_schweizer_aircraft]: https://en.wikipedia.org/wiki/Schweizer_Aircraft
[ref_sgs_2_32]: https://en.wikipedia.org/wiki/Schweizer_SGS_2-32
[ref_usntps]: https://en.wikipedia.org/wiki/United_States_Naval_Test_Pilot_School
[ref_x26]: https://en.wikipedia.org/wiki/Schweizer_X-26_Frigate
[ref_yo3a]: https://en.wikipedia.org/wiki/Lockheed_YO-3_Quiet_Star

### Related Post

- [X-1][related_post_a298_bell_x1]
- [X-10][related_post_a307_north_american_x10]
- [X-11][related_post_a308_convair_x11]
- [X-12][related_post_a309_convair_x12]
- [X-13][related_post_a310_ryan_x13]
- [X-14][related_post_a311_bell_x14]
- [X-15][related_post_a312_north_american_x15]
- [X-16][related_post_a313_bell_x16]
- [X-17][related_post_a314_lockheed_x17]
- [X-18][related_post_a315_hiller_x18]
- [X-19][related_post_a316_curtiss_wright_x19]
- [X-2][related_post_a299_bell_x2]
- [X-20][related_post_a317_boeing_x20]
- [X-21][related_post_a318_northrop_x21]
- [X-22][related_post_a319_bell_x22]
- [X-23][related_post_a320_martin_marietta_x23]
- [X-24][related_post_a321_martin_marietta_x24]
- [X-25][related_post_a322_bensen_x25]
- [X-3][related_post_a300_douglas_x3]
- [X-4][related_post_a301_northrop_x4]
- [X-5][related_post_a302_bell_x5]
- [X-6][related_post_a303_convair_x6]
- [X-7][related_post_a304_lockheed_x7]
- [X-8][related_post_a305_aerojet_x8]
- [X-9][related_post_a306_bell_x9]
- [X-Planes series][related_post_a297_xplanes_framing]

[related_post_a297_xplanes_framing]: {% post_url 2025-10-06-x_planes_framing %}
[related_post_a298_bell_x1]: {% post_url 2025-10-07-x_planes_bell_x1 %}
[related_post_a299_bell_x2]: {% post_url 2025-10-08-x_planes_bell_x2 %}
[related_post_a300_douglas_x3]: {% post_url 2025-10-09-x_planes_douglas_x3 %}
[related_post_a301_northrop_x4]: {% post_url 2025-10-10-x_planes_northrop_x4 %}
[related_post_a302_bell_x5]: {% post_url 2025-10-11-x_planes_bell_x5 %}
[related_post_a303_convair_x6]: {% post_url 2025-10-12-x_planes_convair_x6 %}
[related_post_a304_lockheed_x7]: {% post_url 2025-10-13-x_planes_lockheed_x7 %}
[related_post_a305_aerojet_x8]: {% post_url 2025-10-14-x_planes_aerojet_x8 %}
[related_post_a306_bell_x9]: {% post_url 2025-10-15-x_planes_bell_x9 %}
[related_post_a307_north_american_x10]: {% post_url 2025-10-16-x_planes_north_american_x10 %}
[related_post_a308_convair_x11]: {% post_url 2025-10-17-x_planes_convair_x11 %}
[related_post_a309_convair_x12]: {% post_url 2025-10-18-x_planes_convair_x12 %}
[related_post_a310_ryan_x13]: {% post_url 2025-10-19-x_planes_ryan_x13 %}
[related_post_a311_bell_x14]: {% post_url 2025-10-20-x_planes_bell_x14 %}
[related_post_a312_north_american_x15]: {% post_url 2025-10-21-x_planes_north_american_x15 %}
[related_post_a313_bell_x16]: {% post_url 2025-10-22-x_planes_bell_x16 %}
[related_post_a314_lockheed_x17]: {% post_url 2025-10-23-x_planes_lockheed_x17 %}
[related_post_a315_hiller_x18]: {% post_url 2025-10-24-x_planes_hiller_x18 %}
[related_post_a316_curtiss_wright_x19]: {% post_url 2025-10-25-x_planes_curtiss_wright_x19 %}
[related_post_a317_boeing_x20]: {% post_url 2025-10-26-x_planes_boeing_x20 %}
[related_post_a318_northrop_x21]: {% post_url 2025-10-27-x_planes_northrop_x21 %}
[related_post_a319_bell_x22]: {% post_url 2025-10-28-x_planes_bell_x22 %}
[related_post_a320_martin_marietta_x23]: {% post_url 2025-10-29-x_planes_martin_marietta_x23 %}
[related_post_a321_martin_marietta_x24]: {% post_url 2025-10-30-x_planes_martin_marietta_x24 %}
[related_post_a322_bensen_x25]: {% post_url 2025-10-31-x_planes_bensen_x25 %}

### Research

- [11. Aircraft Range and Endurance in Steady Flight 2011][research_aircraft_range_2011]
- [A Method of Comparing Performance 1936][research_a_method_1936]
- [A review of the aircraft noise problem 2011][research_a_review_2011]
- [A sailplane wing constructed of foam core and polyester 1974][research_a_sailplane_1974]
- [A. et al 2018][research_a_f_2018]
- [Aalmoes and Sieben 2021][research_aalmoes_sieben_2021]
- [Abbott 2016][research_abbott_2016]
- [Abdukayumov 2022][research_abdukayumov_2022]
- [Abdul Rashid et al 2025][research_abdul_rashid_2025]
- [Abdullina and Efanov 2020][research_abdullina_efanov_2020]
- [Abhishek and Prasad 2016][research_abhishek_prasad_2016]
- [Abich IV et al 2016][research_abich_iv_2016]
- [Abichandani and Rosenberg 1952][research_abichandani_rosenberg_1952]
- [Abrahamson 1975][research_abrahamson_1975]
- [Abramov et al 2019][research_abramov_2019]
- [Abramson 1975][research_abramson_1975]
- [Abramson 1977][research_abramson_1977]
- [Abu Salem et al 2023][research_abu_salem_2023]
- [Abwanzo 2016][research_abwanzo_2016]
- [Abzug and DaRos 1955][research_abzug_daros_1955]
- [Achleitner et al 2019][research_achleitner_rohdebrandenburger_2019]
- [Acoustic field separation with 2-layer microphone array 2023][research_acoustic_field_2023]
- [Action against aircraft noise 1989][research_action_against_1989]
- [Adams 1951][research_adams_1951]
- [Adams 1976][research_adams_1976]
- [Adams and Hatch 1971][research_adams_hatch_1971]
- [Adamson 1968][research_adamson_1968]
- [Adamson and Boatright 1950][research_adamson_boatright_1950]
- [Addessio and Skifstad 1975][research_addessio_skifstad_1975]
- [Adler 1960][research_adler_1960]
- [Adolph 1981][research_adolph_1981]
- [Advisory Group for Aerospace Research and Development 1984][research_advisorygroupforaerospaceresearchanddevelopment_1984]
- [Aero structural optimization for sailplane wing in preliminary design 2018][research_aero_structural_2018]
- [Aerodynamic design of low-speed aircraft with a NASA 1986][research_aerodynamic_design_1986]
- [Afari and Mankbadi 2024][research_afari_mankbadi_2024]
- [Afonso et al 2017][research_afonso_2017]
- [Aguiar and Cuevas 2017][research_aguiar_cuevas_2017]
- [Aguiar et al 2017][research_aguiar_2017]
- [AHarrah and Lockenour 1971][research_a_harrah_lockenour_1971]
- [Ahearn et al 1965][research_ahearn_headrick_1965]
- [Ahmadi and Farsadi 2024][research_ahmadi_farsadi_2024]
- [Ahmadi et al 2024][research_ahmadi_2024]
- [Ahmed et al 2024][research_ahmed_2024_2]
- [Ahuja and Bushell 1973][research_ahuja_bushell_1973]
- [Air Force Flight Test Center Edwards Afb Ca 1970][research_air_force_flight_test_center_edwards_afb_ca_1970]
- [Air Force Flight Test Center Edwards Afb Ca 1974][research_air_force_flight_test_center_edwards_afb_ca_1974]
- [Air Force Flight Test Center Edwards Afb Ca 1974][research_air_force_flight_test_center_edwards_afb_ca_1974_2]
- [Air Force Flight Test Center Edwards Afb Ca 1995][research_air_force_flight_test_center_edwards_afb_ca_1995]
- [Air Force Flight Test Center Edwards Afb Ca 2002][research_air_force_flight_test_center_edwards_afb_ca_2002]
- [Air Force Flight Test Center Edwards Afb Ca 2002][research_air_force_flight_test_center_edwards_afb_ca_2002_2]
- [Air Force Test Pilot School Edwards Afb Ca 1962][research_air_force_test_pilot_school_edwards_afb_ca_1962]
- [Air Force Test Pilot School Edwards Afb Ca 1962][research_airforcetestpilotschooledwardsafbca_1962]
- [Air Force Test Pilot School Edwards Afb Ca 1962][research_airforcetestpilotschooledwardsafbca_1962_b]
- [Air Force Test Pilot School Edwards Afb Ca 1967][research_airforcetestpilotschooledwardsafbca_1967]
- [Air Force Test Pilot School Edwards Afb Ca 1967][research_airforcetestpilotschooledwardsafbca_1967_b]
- [Air Force Test Pilot School Edwards Afb Ca 1969][research_air_force_test_pilot_school_edwards_afb_ca_1969]
- [Air Force Test Pilot School Edwards Afb Ca 1979][research_air_force_test_pilot_school_edwards_afb_ca_1979]
- [Air Force Test Pilot School Edwards Afb Ca 1981][research_air_force_test_pilot_school_edwards_afb_ca_1981]
- [Air Force Test Pilot School Edwards Afb Ca 1987][research_air_force_test_pilot_school_edwards_afb_ca_1987]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_air_force_test_pilot_school_edwards_afb_ca_1988]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_air_force_test_pilot_school_edwards_afb_ca_1988_2]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_air_force_test_pilot_school_edwards_afb_ca_1988_3]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_air_force_test_pilot_school_edwards_afb_ca_1988_4]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_air_force_test_pilot_school_edwards_afb_ca_1988_5]
- [Air Force Test Pilot School Edwards Afb Ca 1989][research_air_force_test_pilot_school_edwards_afb_ca_1989]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_air_force_test_pilot_school_edwards_afb_ca_1990]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_air_force_test_pilot_school_edwards_afb_ca_1990_2]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_air_force_test_pilot_school_edwards_afb_ca_1990_3]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_air_force_test_pilot_school_edwards_afb_ca_1990_4]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_air_force_test_pilot_school_edwards_afb_ca_1990_5]
- [Air Force Test Pilot School Edwards Afb Ca 1991][research_air_force_test_pilot_school_edwards_afb_ca_1991]
- [Air Force Test Pilot School Edwards Afb Ca 1991][research_air_force_test_pilot_school_edwards_afb_ca_1991_2]
- [Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991]
- [Air Force Test Pilot School Edwards Afb Ca 1992][research_air_force_test_pilot_school_edwards_afb_ca_1992]
- [Air Force Test Pilot School Edwards Afb Ca 1992][research_airforcetestpilotschooledwardsafbca_1992]
- [Air Force Test Pilot School Edwards Afb Ca 1993][research_air_force_test_pilot_school_edwards_afb_ca_1993]
- [Air Force Test Pilot School Edwards Afb Ca 1994][research_air_force_test_pilot_school_edwards_afb_ca_1994]
- [Air Force Test Pilot School Edwards Afb Ca 1994][research_air_force_test_pilot_school_edwards_afb_ca_1994_2]
- [Air Proving Ground Center Eglin Afb Fl 1954][research_air_proving_ground_center_eglin_afb_fl_1954]
- [Air Proving Ground Center Eglin Afb Fl 1955][research_air_proving_ground_center_eglin_afb_fl_1955]
- [Air Proving Ground Center Eglin Afb Fl 1955][research_air_proving_ground_center_eglin_afb_fl_1955_2]
- [Aircraft and Rotorcraft System Identification: Engineering Methods with Flight Test Examples, Second Edition (Bookshelf) 2016][research_aircraft_and_2016]
- [Aircraft Flyover Noise Measurements 1976][research_aircraft_flyover_1976]
- [Aircraft lateral-directional handling qualities design 2011][research_aircraft_lateral_directional_2011]
- [Aircraft longitudinal handling qualities design 2011][research_aircraft_longitudinal_2011]
- [Aircraft Noise and Certification 2019][research_aircraft_noise_2019]
- [Aircraft Noise Assessment 1980][research_aircraft_noise_1980]
- [Aircraft Noise Flight Trajectories 2012][research_aircraft_noise_2012_b]
- [Aircraft Noise Monitoring 1979][research_aircraft_noise_1979]
- [Aircraft Noise No Quiet in London 1969][research_aircraft_noise_1969]
- [Aircraft Noise Noise Sources 2012][research_aircraft_noise_2012]
- [Aircraft noise prediction 1989][research_aircraft_noise_1989]
- [Aircraft noise propagation 2011][research_aircraft_noise_2011]
- [Aircraft noise sources 1989][research_aircraft_noise_1989_b]
- [Aircraft performance monitoring from flight data 2015][research_aircraft_performance_2015]
- [Aircraft Safety Office 1971][research_aircraft_safety_office_1971]
- [Aithal et al 2004][research_aithal_2004]
- [Ajaj 2021][research_ajaj_2021]
- [Akatsuka 2024][research_akatsuka_2024]
- [Akdeniz et al 2020][research_akdeniz_2020]
- [Akila et al 2018][research_akila_marinus_2018]
- [Akishita et al 1986][research_akishita_1986]
- [Akiyama et al 2023][research_akiyama_2023]
- [Alam and Hromcik 2019][research_alam_hromcik_2019]
- [Alam et al 2015][research_alam_2015]
- [Albert 1990][research_albert_1990]
- [Albostan and Gökaşan 2018][research_albostan_gokasan_2018]
- [Aleksandrov 2025][research_aleksandrov_2025]
- [Aleshin et al 2018][research_aleshin_2018]
- [Alexander 2025][research_alexander_2025]
- [Alexander 2025][research_alexander_2025_b]
- [Alexander and Kinzly 1979][research_alexander_kinzly_1979]
- [Alexandre and Barde 1974][research_alexandre_barde_1974]
- [Alfares 2026][research_alfares_2026]
- [Alford 2004][research_alford_2004]
- [Alford and Knarr 1999][research_alford_knarr_1999]
- [Alfredson 1971][research_alfredson_1971]
- [Ali 1989][research_ali_1989]
- [Alieksieiev and Tsybov 2025][research_alieksieiev_tsybov_2025]
- [Alighanbari 2002][research_alighanbari_2002]
- [Alimadadi 2026][research_alimadadi_2026]
- [Allanach et al 2010][research_allanach_2010]
- [Allen 2006][research_allen_2006]
- [Allen 2007][research_allen_2007]
- [Allen 2007][research_allen_2007_2]
- [Allen and White 1957][research_allen_white_1957]
- [Allen et al 2000][research_allen_eveker_2000]
- [Almeida et al 2016][research_almeida_2016]
- [Almgren 1987][research_almgren_1987]
- [Almutairi and Aouf 2017][research_almutairi_aouf_2017]
- [Alonso Castilla et al 2021][research_alonso_castilla_2021]
- [Alston 1936][research_alston_1936]
- [Altman 1952][research_altman_1952]
- [Altman 2002][research_altman_2002]
- [Altman 2008][research_altman_2008]
- [Altunkaya et al 2024][research_altunkaya_2024]
- [Aláez et al 2022][research_alaez_2022]
- [Alì et al 2026][research_ali_2026]
- [Amalia et al 2018][research_amalia_2018]
- [Amalia et al 2019][research_amalia_2019]
- [Amanatiadis et al 2017][research_amanatiadis_2017]
- [Amargianitakis et al 2021][research_amargianitakis_2021]
- [Amelin 2022][research_amelin_2022]
- [American Institute of Aeronautics and Astronautics 1992][research_american_institute_of_aeronautics_and_astronautics_1992]
- [Amiet 1988][research_amiet_1988]
- [Amitary and Jansen 2011][research_amitary_jansen_2011]
- [An Algorithm for Microphone Array Sparse Arrangement and Acoustic Imaging 2026][research_an_algorithm_2026]
- [An et al 2025][research_an_2025]
- [An evaluation of sailplane drag coefficient parameters from 1974][research_an_evaluation_1974]
- [An Introduction to the Longitudinal Static Stability of 1966][research_an_introduction_1966]
- [An Overview On Unmanned Aerial Vehicle 2017][research_an_overview_2017]
- [Ananthkrishnan and Sinha 2023][research_ananthkrishnan_sinha_2023]
- [Anderle et al 2003][research_anderle_smrcek_2003]
- [Anderson 1960][research_anderson_1960]
- [Anderson 1968][research_anderson_1968]
- [Anderson 1970][research_anderson_1970]
- [Anderson 1976][research_anderson_1976]
- [Anderson 1985][research_anderson_1985]
- [Anderson and Innis 1965][research_anderson_innis_1965]
- [Anderson and Schroers 1972][research_anderson_schroers_1972]
- [Anderson et al 1973][research_anderson_1973]
- [Andino et al][research_marlyn_andino]
- [André 1977][research_andre_1977]
- [Ang and Cui 2022][research_ang_cui_2022]
- [Ang et al 2024][research_ang_2024]
- [Annand 1950][research_annand_1950]
- [Antipov 2020][research_antipov_2020]
- [Antonakis 2025][research_antonakis_2025]
- [Antonakis 2025][research_antonakis_2025_2]
- [Antonakis and Biannic 2024][research_antonakis_biannic_2024]
- [Appa and Ausman 1997][research_appa_ausman_1997]
- [Appa et al 1998][research_appa_1998]
- [Arabian and Schmeer 1955][research_arabian_schmeer_1955]
- [Araujo-Estrada and Windsor 2021][research_araujo_estrada_windsor_2021]
- [Arcondoulis and Liu 2019][research_arcondoulis_liu_2019]
- [Arena et al 1993][research_arena_1993]
- [Armstrong 1977][research_armstrong_1977]
- [Army Aviation Board Fort Rucker Al 1957][research_armyaviationboardfortruckeral_1957]
- [Army Aviation Center And Fort Rucker Al 1992][research_armyaviationcenterandfortruckeral_1992]
- [Army Aviation School Fort Rucker Al 1961][research_army_aviation_school_fort_rucker_al_1961]
- [Army Service Forces Washington Dc 1940][research_armyserviceforceswashingtondc_1940]
- [Arndt and Borgman 1971][research_arndt_borgman_1971]
- [Arnold 1942][research_arnold_1942]
- [Arnold 1981][research_arnold_1981]
- [Arseneau 1997][research_arseneau_1997]
- [Arum et al 2020][research_arum_2020]
- [Asakura and Takagi 2020][research_asakura_takagi_2020]
- [Ashill 1970][research_ashill_1970]
- [Ashkenas 1946][research_ashkenas_1946]
- [Ashkenas 1965][research_ashkenas_1965]
- [Ashkenas 1965][research_ashkenas_1965_2]
- [Ashkenas 1971][research_ashkenas_1971]
- [Ashkenas 1984][research_ashkenas_1984]
- [Ashkenas and Klyde 1989][research_ashkenas_klyde_1989]
- [Atkin 2001][research_atkin_2001]
- [Atmaca et al 2025][research_atmaca_2025]
- [Attenborough 1985][research_attenborough_1985]
- [Attenborough 2022][research_attenborough_2022]
- [Aujogue][research_aujogue]
- [Aurégan 2018][research_auregan_2018]
- [Austin D. Thai et al][research_austin_d_thai]
- [Autenrieb 2025][research_autenrieb_2025]
- [Avallone et al 2018][research_avallone_2018]
- [Avco Lycoming Div Stratford Ct 1970][research_avco_lycoming_div_stratford_ct_1970]
- [Avrenli and Dempsey 2015][research_avrenli_dempsey_2015]
- [Awadalla Ali Haj Ahmed 2024][research_awadalla_ali_haj_ahmed_2024]
- [Axten and Maughmer 2020][research_axten_maughmer_2020]
- [Axten et al 2024][research_axten_chidekel_2024]
- [Aydın and Kızılay 2022][research_aydn_kzlay_2022]
- [Aziz and Loya 2025][research_aziz_loya_2025]
- [Azzi et al 2024][research_azzi_tahiliani_2024]
- [Bachelder and Aponso 2020][research_bachelder_aponso_2020]
- [Bachelder and Klyde 2011][research_bachelder_klyde_2011]
- [Bachelder et al 2023][research_bachelder_aponso_2023]
- [Badgley and Laskin 1970][research_badgley_laskin_1970]
- [Badzli 2023][research_badzli_2023]
- [Baek et al 2015][research_baek_2015]
- [Baek et al 2021][research_baek_2021]
- [Bagley et al 2026][research_bagley_2026]
- [Bahr et al 2021][research_bahr_2021]
- [Baier 1970][research_baier_1970]
- [Bailes et al 1975][research_bailes_1975]
- [Bailey and McClintic 1974][research_bailey_mcclintic_1974]
- [Bailey et al 1988][research_bailey_1988]
- [Bailey et al 1996][research_bailey_knoedler_1996]
- [Bainetov 2016][research_s_d_bainetov_2016]
- [Baisden 1980][research_baisden_1980]
- [Bakar et al 2021][research_bakar_2021]
- [Baker 1941][research_baker_1941]
- [Baker 1942][research_baker_1942]
- [Baker 1948][research_baker_1948]
- [Balatti et al 2021][research_balatti_2021]
- [Balatti et al 2023][research_balatti_2023]
- [Baldwin 1973][research_baldwin_1973]
- [Baldwin 1973][research_baldwin_1973_b]
- [Baldwin and Frederickson 1966][research_baldwin_frederickson_1966]
- [Ball 1987][research_ball_1987]
- [Balyakin 2015][research_balyakin_2015]
- [Bamber 1961][research_bamber_1961]
- [Banerjee 1984][research_banerjee_1984]
- [Banerjee 1988][research_banerjee_1988]
- [Banerjee 2019][research_banerjee_2019]
- [Banerjee et al 2017][research_banerjee_2017]
- [Barde et al 2022][research_barde_birzare_2022]
- [Barlow et al 1972][research_barlow_mccluskey_1972]
- [Barman and Erzberger 1976][research_barman_erzberger_1976]
- [Barnes 2015][research_barnes_2015]
- [Barnes and Yager 1985][research_barnes_yager_1985]
- [Barnette 1978][research_barnette_1978]
- [Barr et al 2018][research_barr_2018]
- [Barrett-Gonzalez and Wolf 2021][research_barrett_gonzalez_wolf_2021]
- [Barry and Magliozzi 1971][research_barry_magliozzi_1971]
- [Barstow 1940][research_barstow_1940]
- [Barstow 1941][research_barstow_1941]
- [Bartels and Jacobson][research_robert_bartels_kevin_jacobson]
- [Bartels et al 2017][research_bartels_2017]
- [Barton and Mixson 1981][research_barton_mixson_1981]
- [Barufaldi and Morales 2023][research_barufaldi_morales_2023]
- [Basak et al 2022][research_basak_2022]
- [Bass 1976][research_bass_1976_2]
- [Bass et al 1972][research_bass_1972]
- [Bass et al 1990][research_bass_1990]
- [Bauer 1977][research_bauer_1977]
- [Bauer 2021][research_bauer_2021]
- [Bauer 2025][research_w_bauer_2025]
- [Bauer and Nagy 2024][research_bauer_nagy_2024]
- [Bauer et al 2016][research_bauer_2016]
- [Bauermeister and Donner 1980][research_bauermeister_donner_1980]
- [Baughman and Longeauay 2015][research_baughman_longeauay_2015]
- [Baxter 1951][research_baxter_1951]
- [Beale and Cook 1985][research_beale_cook_1985]
- [Beard et al 2013][research_beard_2013]
- [Beauregard 1964][research_beauregard_1964]
- [Bechelder et al 2025][research_bechelder_bjorkman_2025]
- [Beck et al 2018][research_beck_2018]
- [Becker and Korycinski 1944][research_becker_korycinski_1944]
- [Beech Aircraft Corp Wichita Ks 1966][research_beech_aircraft_corp_wichita_ks_1966]
- [Beeman 1972][research_beeman_1972]
- [Bell Aerospace Co Buffalo Ny 1955][research_bell_aerospace_co_buffalo_ny_1955]
- [Bell Aerospace Co Buffalo Ny 1955][research_bell_aerospace_co_buffalo_ny_1955_2]
- [Bell Aerospace Co Buffalo Ny 1956][research_bell_aerospace_co_buffalo_ny_1956]
- [Bell Aerospace Co Buffalo Ny 1956][research_bell_aerospace_co_buffalo_ny_1956_2]
- [Bell Aerospace Co Buffalo Ny 1956][research_bell_aerospace_co_buffalo_ny_1956_3]
- [Bell Aerospace Co Buffalo Ny 1957][research_bell_aerospace_co_buffalo_ny_1957]
- [Bellucci 1963][research_bellucci_1963]
- [Belsky 2022][research_belsky_2022]
- [Bender and Brammer 1973][research_bender_brammer_1973]
- [Bender and Brammer 1975][research_bender_brammer_1975]
- [Bender and OConnor 1974][research_bender_o_connor_1974]
- [Bendiksen 1993][research_bendiksen_1993]
- [Bennett 1978][research_bennett_1978]
- [Bennett and Johnson 1947][research_bennett_johnson_1947]
- [Bennett et al 1974][research_bennett_owens_1974]
- [Bennett et al 1978][research_bennett_1978_2]
- [Benzakein et al 1973][research_benzakein_kazin_1973]
- [Bera 1976][research_bera_1976]
- [Bera† 1980][research_bera_1980]
- [Berenschot 2001][research_berenschot_2001]
- [Bergen and Arnold 1940][research_bergen_arnold_1940]
- [Berger et al 2022][research_berger_2022]
- [Berger et al 2022][research_berger_2022_2]
- [Berger et al 2025][research_berger_christensen_2025]
- [Bergman 1971][research_bergman_1971]
- [Bergman 1976][research_bergman_1976]
- [Bergmann et al 2021][research_bergmann_2021]
- [Berkowitz 1950][research_berkowitz_1950]
- [Bernardini et al 2017][research_bernardini_2017]
- [Bernot 1979][research_bernot_1979]
- [Berry and Harris 2024][research_berry_harris_2024]
- [Berry and Speakman 1993][research_berry_speakman_1993]
- [Berry et al 1976][research_berry_1976]
- [Bert 1981][research_bert_1981]
- [Bert 1999][research_bert_1999]
- [Berton and Nark 2019][research_berton_nark_2019]
- [Bertsch et al 2010][research_bertsch_dobrzynski_2010]
- [Bertsch et al 2019][research_bertsch_2019]
- [Bertsch et al 2023][research_bertsch_pottpollenske_2023]
- [Beschorner et al 2025][research_beschorner_2025]
- [Bevilaqua 2021][research_bevilaqua_2021]
- [Bewick et al 2001][research_bewick_adams_2001]
- [Beyers 1983][research_beyers_1983]
- [Beyers 1988][research_beyers_1988]
- [Bhandari et al 2026][research_bhandari_2026]
- [Bhardwaj et al 2026][research_bhardwaj_2026]
- [Bhat et al 2026][research_bhat_2026]
- [Bhatia 2019][research_bhatia_2019]
- [Bi et al 2017][research_bi_2017]
- [Bian et al 2018][research_bian_2018]
- [Bian et al 2019][research_bian_2019]
- [Bienen 1927][research_bienen_1927]
- [Biermann and Conway 1942][research_biermann_conway_1942]
- [Bihrle and Barnhart 1974][research_bihrle_barnhart_1974]
- [Bilanin and Donaldson 1975][research_bilanin_donaldson_1975]
- [Billingsley 1976][research_billingsley_1976]
- [Binghua and Hui 2021][research_binghua_hui_2021]
- [Bird and Jaquet 1951][research_bird_jaquet_1951]
- [Bird et al 1952][research_bird_1952]
- [Birdsall 1970][research_d_l_birdsall_1970]
- [Bischoff 1983][research_bischoff_1983]
- [Bischoff and Palmer 1983][research_bischoff_palmer_1983]
- [Bischoff et al 1974][research_bischoff_1974]
- [Bishara et al 2018][research_bishara_2018]
- [Bishop and Franken 1968][research_bishop_franken_1968]
- [Bishop and Tufariello 2019][research_bishop_tufariello_2019]
- [Black and Moorhouse 1979][research_black_moorhouse_1979]
- [Blackburn 1968][research_blackburn_1968]
- [Blackburn and Joslin 2021][research_blackburn_joslin_2021]
- [Blake 2002][research_blake_2002]
- [Blanchard 1981][research_blanchard_1981]
- [Blanchard et al 2020][research_blanchard_2020]
- [Bleimeyer 1981][research_bleimeyer_1981]
- [Bliss 1980][research_bliss_1980]
- [Block 1986][research_block_1986]
- [Block and Gentry 1986][research_block_gentry_1986]
- [Bloom and Jen 1974][research_bloom_jen_1974]
- [Blosser 1952][research_blosser_1952]
- [Blosser 1953][research_blosser_1953]
- [Bobbitt 1957][research_bobbitt_1957]
- [Bobbitt 1959][research_bobbitt_1959]
- [Boeing Co Morton Pa Vertol Div 1961][research_boeing_co_morton_pa_vertol_div_1961]
- [Boeing Vertol Co Philadelphia Pa 1983][research_boeing_vertol_co_philadelphia_pa_1983]
- [Bogdanovic et al 1965][research_bogdanovic_1965]
- [Bohn and Shovlin 1981][research_bohn_shovlin_1981]
- [Bolds 1961][research_bolds_1961]
- [Bolds 1962][research_bolds_1962]
- [Bolds-Moorehead et al 2015][research_boldsmoorehead_chaney_2015]
- [Bolt Beranek And Newman Inc Los Angeles Ca 1965][research_bolt_beranek_and_newman_inc_los_angeles_ca_1965]
- [Bonnin][research_bonnin]
- [Bonnin and Hoogreef 2025][research_bonnin_hoogreef_2025]
- [Bonnin et al 2013][research_bonnin_toomer_2013]
- [Bonomo et al 2024][research_bonomo_2024]
- [Bookstaber 2000][research_bookstaber_2000]
- [Boothe et al 1974][research_boothe_1974]
- [Borchers 2009][research_borchers_2009]
- [Borer et al 2016][research_borer_2016]
- [Borodulin et al 2017][research_borodulin_2017]
- [Borst 1978][research_borst_1978]
- [Bortolussi 1997][research_bortolussi_1997]
- [Bossler and Smith 1974][research_bossler_smith_1974]
- [Boston et al 1984][research_boston_1984]
- [Boswell 1970][research_boswell_1970]
- [Boswell and Miller 1968][research_boswell_miller_1968]
- [Botros et al 2018][research_botros_walker_2018]
- [Bottasso and Montinari 2015][research_bottasso_montinari_2015]
- [Boucher et al 2023][research_boucher_2023]
- [Boullet et al 2023][research_boullet_2023]
- [Bowers 1979][research_bowers_1979]
- [Bowers 2018][research_bowers_2018]
- [Bowers et al 2016][research_bowers_2016]
- [Bowersox and Fan 2000][research_bowersox_fan_2000]
- [Bowes and Miller 1976][research_bowes_miller_1976]
- [Bowles et al 1974][research_bowles_1974]
- [Bowman 1965][research_bowman_1965]
- [Boyd 2015][research_boyd_2015]
- [Boyd 2015][research_boyd_2015_2]
- [Boyd and Stolzer 2016][research_boyd_stolzer_2016]
- [Boyden 1971][research_boyden_1971]
- [Boyer 1908][research_boyer_1908]
- [Bozack 1984][research_bozack_1984]
- [Bracken and Grotte 1979][research_bracken_grotte_1979]
- [Bradley 1975][research_bradley_1975]
- [Bramesfeld and Maughmer 2002][research_bramesfeld_maughmer_2002]
- [Brandon and Morelli 2016][research_brandon_morelli_2016]
- [Bras et al 2022][research_bras_2022]
- [Braslow 1944][research_braslow_1944]
- [Braslow and Visconti 1949][research_braslow_visconti_1949]
- [Bravo et al 2021][research_bravo_2021]
- [Bray and Larsen 1965][research_bray_larsen_1965]
- [Bray et al 1960][research_bray_1960]
- [Brear et al 2003][research_brear_kerrebrock_2003]
- [Brennan and McDaniel 1994][research_brennan_mcdaniel_1994]
- [Bretoi 1952][research_bretoi_1952]
- [Breul 1963][research_breul_1963]
- [Brewer 1946][research_brewer_1946]
- [Brian Trubshaw Test Pilot 2006][research_brian_trubshaw_2006]
- [Briardy and Head 1968][research_briardy_head_1968]
- [Bridges 2021][research_bridges_2021]
- [Bright et al 2013][research_bright_2013]
- [Brincklow and Hunsaker 2021][research_brincklow_hunsaker_2021]
- [Brincklow et al 2021][research_brincklow_montgomery_2021]
- [Brincklow et al 2024][research_brincklow_montgomery_2024]
- [Brinza et al 2026][research_brinza_2026]
- [Brockett 1972][research_brockett_1972]
- [Brodsky and Luby 2013][research_brodsky_luby_2013]
- [Bromfield and Dillman 2015][research_bromfield_dillman_2015]
- [Bromfield et al 2023][research_bromfield_2023]
- [Bromfield et al 2023][research_bromfield_2023_2]
- [Bronder et al 2012][research_bronder_lee_2012]
- [Bronz 2019][research_bronz_2019]
- [Brooks and Mackall 1984][research_brooks_mackall_1984]
- [Brown 1950][research_brown_1950]
- [Brown 1954][research_brown_1954]
- [Brown 1959][research_brown_1959]
- [Brown 1981][research_brown_1981]
- [Brown and Adams 1948][research_brown_adams_1948]
- [Brown and Heinke 1956][research_brown_heinke_1956]
- [Brown et al 1969][research_brown_cox_1969]
- [Brown et al 2016][research_brown_2016]
- [Browne et al 2025][research_browne_2025]
- [Bruington et al 2001][research_bruington_brenernan_2001]
- [Brun et al 1947][research_brun_feder_1947]
- [Brungart et al 2019][research_brungart_2019]
- [Brusniak et al 2019][research_brusniak_2019]
- [Bryant 1963][research_bryant_1963]
- [Bryson et al 2016][research_bryson_2016]
- [Buchwalder 1985][research_buchwalder_1985]
- [Bucklew 2009][research_bucklew_2009]
- [Buckley et al 2020][research_buckley_2020]
- [Bucur and Lupuleasa 2026][research_bucur_lupuleasa_2026]
- [Budd and Monheim 2015][research_budd_monheim_2015]
- [Bui et al 2021][research_bui_2021]
- [Bull and Bridges 1985][research_bull_bridges_1985]
- [Bullmore et al 1990][research_bullmore_1990]
- [Burcham et al 1992][research_frank_w_burcham_1992]
- [Burken et al 1996][research_burken_1996]
- [Burken et al 2006][research_burken_2006]
- [Burken et al 2006][research_burken_2006_2]
- [Burley 1974][research_burley_1974]
- [Burnell and Fan 1957][research_burnell_fan_1957]
- [Burrin 1970][research_burrin_1970]
- [Burris and Bender 1969][research_burris_bender_1969]
- [Burt 1975][research_burt_1975]
- [Burt and Uselton 1976][research_burt_uselton_1976]
- [Burton and Hoburg 2018][research_burton_hoburg_2018]
- [Bussolari et al 1987][research_bussolari_youngren_1987]
- [Butler 1976][research_butler_1976]
- [Butler 1976][research_butler_1976_2]
- [Butler and Langham 1978][research_butler_langham_1978]
- [Butler et al 1966][research_butler_huang_1966]
- [Butzel 1982][research_butzel_1982]
- [Bynum 1978][research_bynum_1978]
- [Byrd and Cates 1977][research_byrd_cates_1977]
- [Cahn et al 1966][research_cahn_1966]
- [Caillet et al 2026][research_caillet_2026]
- [Cain 1979][research_cain_1979]
- [Calculation of aircraft noise contours around airports 1989][research_calculation_of_1989]
- [Calise et al 1999][research_calise_1999]
- [Calloway 1983][research_calloway_1983]
- [Calvert 1950][research_calvert_1950]
- [Campanella 1976][research_campanella_1976]
- [Campbell and Goodman 1949][research_campbell_goodman_1949]
- [Campbell and McDonald 1963][research_campbell_mcdonald_1963]
- [Campbell et al][research_newton_h_campbell]
- [Campbell et al 2021][research_newton_h_campbell_2021]
- [Camponogara et al 2019][research_camponogara_2019]
- [Campos and Marques 2021][research_campos_marques_2021]
- [Canard-Caruana et al 1990][research_canard_caruana_1990]
- [Cancro 1953][research_cancro_1953]
- [Cano and Sobel 2016][research_cano_sobel_2016]
- [Cantos et al 2026][research_cantos_2026]
- [Cao 2023][research_cao_2023]
- [Cao 2026][research_cao_2026]
- [Cao et al 2023][research_cao_2023_2]
- [Cao et al 2024][research_cao_2024]
- [Cao et al 2026][research_cao_gao_2026]
- [Capone and Bare 1987][research_capone_bare_1987]
- [Carico][research_carico]
- [Carico 1995][research_carico_1995]
- [Carico 1998][research_carico_1998]
- [Carico et al][research_carico_chengjianhe]
- [Carico et al 2001][research_carico_he_2001]
- [Carithers and Montalvo 2018][research_carithers_montalvo_2018]
- [Carnes et al 1993][research_carnes_1993]
- [Caro 2017][research_caro_2017]
- [Carpenter 1970][research_carpenter_1970]
- [Carr et al 2024][research_carr_2024]
- [Carroll and Carroll 2005][research_carroll_carroll_2005]
- [Carroll et al 2021][research_carroll_2021]
- [Casagrande Hirono et al 2023][research_casagrande_hirono_2023]
- [Casalino et al 2021][research_casalino_2021]
- [Casanova et al 2025][research_matthias_casanova_2025]
- [Casey 1984][research_casey_1984]
- [Castro Mota et al 2025][research_castro_mota_2025]
- [Catherines and Mayes 1975][research_catherines_mayes_1975]
- [Causse et al 2026][research_causse_2026]
- [Cavaliere and Fezans 2024][research_cavaliere_fezans_2024]
- [Cavcar 2011][research_cavcar_2011]
- [Cavcar and Cavcar 2005][research_cavcar_cavcar_2005]
- [Cecrdle 2011][research_cecrdle_2011]
- [Certified Aircraft Noise Data 2012][research_certified_aircraft_2012]
- [CFD Analysis of Boeing-737 3D Aerofoil and Adverse YAW on 2017][research_cfd_analysis_of_2017]
- [Chabot and Bird 2015][research_chabot_bird_2015]
- [Chakraborty and Mishra 2023][research_chakraborty_mishra_2023]
- [Chakraborty et al 2015][research_chakraborty_2015]
- [Chalk 1964][research_chalk_1964]
- [Chalk 1983][research_chalk_1983]
- [Chalk and Wilson 1969][research_chalk_wilson_1969]
- [Chambers 1966][research_chambers_1966]
- [Chanaud 1972][research_chanaud_1972]
- [Chance Vought Corp Dallas Tx 1979][research_chance_vought_corp_dallas_tx_1979]
- [Chang and Hung 2021][research_chang_hung_2021]
- [Chang and Sullivan 1984][research_chang_sullivan_1984]
- [Changchuan et al 2018][research_changchuan_2018]
- [Chapman 1988][research_chapman_1988]
- [Chappelle et al 2014][research_chappelle_swearengen_2014]
- [Chapter 12 Converting a Piston Engine Aircraft to a 2019][research_chapter_12_2019]
- [Charles E Feiler et al 1972][research_charles_e_feiler_1972]
- [Charly Kone et al 2025][research_charly_kone_2025]
- [Chau and Zingg 2022][research_chau_zingg_2022]
- [Chau and Zingg 2022][research_chau_zingg_2022_2]
- [Chau and Zingg 2023][research_chau_zingg_2023]
- [Chau et al 2026][research_chau_2026]
- [Chaudhuri 1977][research_chaudhuri_1977]
- [Che et al 2021][research_che_2021]
- [Che Mamat and Abdul Aziz 2022][research_che_mamat_abdul_aziz_2022]
- [Cheeseman 1975][research_cheeseman_1975]
- [Chen][research_chen]
- [Chen and Han 2017][research_chen_han_2017]
- [Chen et al 2015][research_chen_2015]
- [Chen et al 2015][research_chen_2015_2]
- [Chen et al 2021][research_chen_2021_2]
- [Chen et al 2023][research_chen_2023]
- [Chen et al 2025][research_chen_2025]
- [Chen et al 2025][research_chen_2025_3]
- [Chen et al 2025][research_chen_2025_4]
- [Chen et al 2025][research_chen_2025_5]
- [Chen et al 2026][research_chen_2026]
- [Chen et al 2026][research_chen_2026_3]
- [Chen et al 2026][research_chen_2026_4]
- [Chen et al 2026][research_chen_2026_5]
- [Cheng 1978][research_cheng_1978]
- [Cheng and Langelaan 2014][research_cheng_langelaan_2014]
- [Cheng and Meng 1980][research_cheng_meng_1980]
- [Cheng et al 2022][research_cheng_2022]
- [Cheng et al 2023][research_cheng_2023]
- [Cheng et al 2025][research_cheng_2025]
- [Chengtao et al 2011][research_chengtao_lixin_2011]
- [Chernyshev et al 2019][research_chernyshev_2019]
- [Chessell 1978][research_chessell_1978]
- [Chessell 1979][research_chessell_1979]
- [Cheung et al 2020][research_cheung_2020]
- [Chevalier and Burke 1972][research_chevalier_burke_1972]
- [Chew and Chapin 1963][research_chew_chapin_1963]
- [Chick et al 2023][research_chick_cornwellarquitt_2023]
- [Childress 1958][research_childress_1958]
- [Chobeau et al 2017][research_chobeau_2017]
- [Choi 2020][research_choi_2020]
- [Choi 2025][research_choi_2025]
- [Chopra 2002][research_chopra_2002]
- [Choudhari et al 2011][research_choudhari_2011]
- [Chowhan et al 2019][research_chowhan_2019]
- [Christian][research_andrew_christian]
- [Christian 2021][research_christian_2021]
- [Christophersen and Spahr 1944][research_christophersen_spahr_1944]
- [Chu and Widnall 1974][research_chu_widnall_1974]
- [Chu et al 2021][research_chu_2021]
- [Chung et al 1993][research_chung_1993]
- [Churchill and Dugan 1982][research_churchill_dugan_1982]
- [Chusseau et al 2024][research_chusseau_biron_2024]
- [Chyla 2024][research_chyla_2024]
- [Ciaburro et al 2020][research_ciaburro_2020]
- [Ciepluch 1973][research_ciepluch_1973]
- [Cieślak 2021][research_cieslak_2021]
- [Ciliberti and Nicolosi 2025][research_ciliberti_nicolosi_2025]
- [Ciolponea 2022][research_ciolponea_2022]
- [Clark 1953][research_clark_jr_1953]
- [Clark 1981][research_clark_1981]
- [Clark 1982][research_clark_1982]
- [Clark 2013][research_clark_2013]
- [Clarke and Merson 1979][research_clarke_merson_1979]
- [Clarkson and Mead 1973][research_clarkson_mead_1973]
- [Claudia Alice 2010][research_claudiaalice_2010]
- [Cleek et al 1978][research_cleek_jr_1978]
- [Cleek et al 1978][research_cleek_jr_1978_b]
- [Cleek et al 1978][research_cleek_jr_1978_c]
- [Cleek et al 1979][research_cleek_nathanh_1979]
- [Cleek et al 1979][research_cleek_nathanh_1979_b]
- [Cleek et al 1979][research_cleek_nathanh_1979_c]
- [Cleek et al 1979][research_cleek_nathanh_1979_d]
- [Cleek et al 1979][research_cleek_nathanh_1979_e]
- [Clemente Carrari et al 2025][research_clemente_carrari_2025]
- [Clewley and Nixon 2019][research_clewley_nixon_2019]
- [Cliff and Lutze 1972][research_cliff_lutze_1972]
- [Clothier et al 2015][research_clothier_2015]
- [Clousing 1965][research_clousing_1965]
- [Cobleigh 1994][research_cobleigh_1994]
- [Cobleigh et al 1994][research_brent_r_cobleigh_1994]
- [Cochran 2015][research_cochran_2015]
- [Cochrane and Boissevain 1978][research_cochrane_boissevain_1978]
- [Cochrane and Carros 1975][research_cochrane_carros_1975]
- [Cochrane et al 1981][research_cochrane_riddle_1981]
- [Cochrane et al 1982][research_cochrane_riddle_1982]
- [Coder and Somers 2020][research_coder_somers_2020]
- [Codon and Bowles 1979][research_codon_bowles_1979]
- [Coe and Newsom 1974][research_coe_newsom_1974]
- [Coe et al 1975][research_coe_1975]
- [Coen and Richwine 2017][research_coen_richwine_2017]
- [Coiro and Nicolosi 2001][research_coiro_nicolosi_2001]
- [Coldsnow et al 2009][research_coldsnow_2009]
- [Cole 1986][research_cole_1986]
- [Cole 1988][research_cole_1988]
- [Cole and Dobbins 1971][research_cole_dobbins_1971]
- [Cole and England 1967][research_cole_england_1967]
- [Cole et al 2007][research_cole_cogan_2007]
- [Coletti 1954][research_coletti_1954]
- [Collazo Garcia et al 2019][research_collazogarcia_ranjan_2019]
- [Collier et al 1990][research_collier_1990]
- [Colling 1995][research_colling_1995]
- [Colozza 2002][research_colozza_2002]
- [Combey et al 2026][research_combey_2026]
- [Comer and Chakraborty 2024][research_comer_chakraborty_2024]
- [Composite propeller blade 1972][research_composite_propeller_1972]
- [Computational Simulation of F3F Glider Flight Performance: Applied Research on Composite Material Optimization Design 2025][research_computational_simulation_2025]
- [Computer simulates aircraft-engine performance 1974][research_computer_simulates_1974]
- [Computer techniques for propeller blade section design 1976][research_computer_techniques_1976]
- [Condon et al 1970][research_condon_1970]
- [Cong et al 2023][research_cong_2023]
- [Connelly 1982][research_connelly_1982]
- [Conners et al 2005][research_conners_howe_2005]
- [Connor et al 1975][research_connor_hilton_1975]
- [Continental Army Command Fort Monroe Va 1958][research_continental_army_command_fort_monroe_va_1958]
- [Control of ground objects escorting from aircraft 2021][research_control_of_2021]
- [Cook 1964][research_cook_1964]
- [Cook 1965][research_cook_1965]
- [Cook 1979][research_cook_1979]
- [Coombes et al 2017][research_coombes_2017]
- [Cooper and Harper 1969][research_cooper_harper_1969]
- [Corbishley et al 2026][research_corbishley_2026]
- [Cordner 1967][research_cordner_1967]
- [Cornell Aeronautical Lab Inc Buffalo Ny 1947][research_cornell_aeronautical_lab_inc_buffalo_ny_1947]
- [Cornell Aeronautical Lab Inc Buffalo Ny 1971][research_cornell_aeronautical_lab_inc_buffalo_ny_1971]
- [Cornell Aeronautical Lab Inc Buffalo Ny 1971][research_cornell_aeronautical_lab_inc_buffalo_ny_1971_2]
- [Cornell Aeronautical Lab Inc Buffalo Ny 1971][research_cornell_aeronautical_lab_inc_buffalo_ny_1971_3]
- [Corridor-Wide Surveillance Using Unmanned Aircraft Systems 2023][research_corridor_wide_surveillance_2023]
- [Corson 1941][research_corson_1941]
- [Corwin et al 1989][research_corwin_1989]
- [Cotting 2016][research_cotting_2016]
- [Cotton 1974][research_cotton_1974]
- [Coward 1955][research_coward_1955]
- [Cox and Abbott 1966][research_cox_abbott_1966]
- [Craig 1965][research_craig_1965]
- [Craig et al 1999][research_craig_1999]
- [Crandall 1943][research_crandall_1943]
- [Crane and Holtzclaw 1944][research_crane_holtzclaw_1944]
- [Crane and Reeder 1945][research_crane_reeder_1945]
- [Crawford and Hodgson 1961][research_crawford_hodgson_1961]
- [Crighton 1979][research_crighton_1979]
- [Crombie and Moorhouse 1980][research_crombie_moorhouse_1980]
- [Croom and Huffman 1957][research_croom_huffman_1957]
- [Cross 1984][research_cross_1984]
- [Cross and Ryley 2024][research_cross_ryley_2024]
- [Cross and Watts 1983][research_cross_watts_1983]
- [Crother et al 1973][research_crother_1973]
- [Culpepper and Murphy 1979][research_culpepper_murphy_1979]
- [Culver 2016][research_culver_2016]
- [Cummings 1929][research_cummings_1929]
- [Cummings 1968][research_cummings_1968]
- [Cunningham 1962][research_cunningham_1962]
- [Cuppoletti et al 2024][research_cuppoletti_2024]
- [Curry et al 1965][research_curry_1965]
- [Curtis 1977][research_curtis_1977]
- [Curtiss 1965][research_curtiss_h_c_1965]
- [Curtiss 1971][research_curtiss_1971]
- [Cusati et al 2023][research_cusati_2023]
- [Cusimano and Johnson 1994][research_cusimano_johnson_1994]
- [Czarnecki and Davis 1948][research_czarnecki_davis_1948]
- [Czarnigowski et al 2019][research_czarnigowski_skiba_2019]
- [Czarnocki et al 2019][research_czarnocki_dudek_2019]
- [Czysz 1963][research_czysz_1963]
- [d and de Socio 1999][research_d_desocio_1999]
- [d and Menichetti 2000][research_d_menichetti_2000]
- [D.L. and M.V. 1974][research_d_l_m_v_1974]
- [Dafrallah and Akhloufi 2024][research_dafrallah_akhloufi_2024]
- [Dahan et al 1980][research_dahan_avezard_1980]
- [Dahiya 2016][research_dahiya_2016]
- [Dahiya 2017][research_dahiya_2017]
- [Dahms and Bardenhagen 2019][research_dahms_bardenhagen_2019]
- [Dailey 1955][research_dailey_1955]
- [Dalan and Cohen 1985][research_dalan_cohen_1985]
- [Dalton and Wang 1990][research_dalton_wang_1990]
- [Dandwani et al 2025][research_dandwani_bragadoaldana_2025]
- [Dani][research_dani]
- [Danjuma 2022][research_danjuma_2022]
- [Danjuma et al 2021][research_danjuma_2021]
- [Dash et al 2003][research_dash_2003]
- [Daughaday and Duwaldt 1955][research_daughaday_duwaldt_1955]
- [Davari and Laitone 1977][research_davari_laitone_1977]
- [David and Seifert 2012][research_david_seifert_2012]
- [Davidson 1975][research_davidson_1975]
- [Davis 1957][research_davis_1957]
- [Davis et al 1953][research_davis_1953]
- [Day and Guthrie 1958][research_day_guthrie_1958]
- [Day and Reisert 1959][research_day_reisert_1959]
- [De Gaspari and Mantegazza 2024][research_de_gaspari_mantegazza_2024]
- [De Gaspari et al 2024][research_de_gaspari_2024]
- [De Hoff and Hall 1978][research_dehoff_hall_1978]
- [De Luca et al 2025][research_de_luca_2025]
- [de Macedo et al 2025][research_de_macedo_2025]
- [de Matteis and Tamilia 1993][research_dematteis_tamilia_1993]
- [de Visser and Pool 2023][research_de_visser_pool_2023]
- [de Vries and Vos 2023][research_de_vries_vos_2023]
- [de Vries et al 2019][research_de_vries_2019]
- [Deal et al 2024][research_deal_2024]
- [Deckert and Ferry 1959][research_deckert_ferry_1959]
- [Deckert and Hodgson 1962][research_deckert_hodgson_1962]
- [Dees 2010][research_dees_2010]
- [Dees 2013][research_dees_2013]
- [Degtyarev et al 2021][research_degtyarev_2021]
- [Deittert et al 2009][research_deittert_richards_2009]
- [Dekoninck 2020][research_dekoninck_2020]
- [Della Vecchia et al 2017][research_della_vecchia_2017]
- [DeLoach 1975][research_deloach_1975]
- [Demarchi and Haning 1978][research_demarchi_haning_1978]
- [Deming 1937][research_deming_1937]
- [Deming 1940][research_deming_1940]
- [Demircali and Uvet 2017][research_demircali_uvet_2017]
- [Demircali and Uvet 2018][research_demircali_uvet_2018]
- [Deng et al 2026][research_deng_2026]
- [Denning 1962][research_denning_1962]
- [Dennis and Scherrer 1951][research_dennis_scherrer_1951]
- [Department Of The Air Force Washington Dc 2005][research_department_of_the_air_force_washington_dc_2005]
- [Deprez 1908][research_deprez_1908]
- [DeSanti 1988][research_desanti_1988]
- [Design and Analysis of 2023, Design and Analysis of Propeller][research_design_and_2023_2]
- [Design and Fluid Flow Analysis of Unmanned Aerial Vehicle (UAV) 2015][research_design_and_2015]
- [Deters and Russell 1947][research_deters_russell_1947]
- [Deters and Russell 1947, Investigation of the Aileron and][research_deters_russell_1947_2]
- [Deuschle et al 2024][research_deuschle_2024]
- [Deveaux 1965][research_deveaux_1965]
- [Development and Application of Solar-Powered Aircraft Technology 2025][research_development_and_2025]
- [Development of a New Computer System for Aircraft Noise 1976][research_development_of_1976]
- [Deyoung 1950][research_deyoung_1950]
- [Deyoung 1979][research_deyoung_1979]
- [Deyoung and Harper 1948][research_deyoung_harper_1948]
- [Dhayalan et al 2018][research_r_2018]
- [Di 2017][research_di_2017]
- [Di Donato et al 2017][research_di_donato_2017]
- [Diamond 1963][research_diamond_1963]
- [Diamond and Lee 1965][research_diamond_lee_1965]
- [Diarra et al 2023][research_diarra_2023]
- [Dias 2023][research_dias_2023]
- [Dickinson 1953][research_dickinson_1953]
- [Dickinson 1976][research_dickinson_1976]
- [Dickinson 1979][research_dickinson_1979]
- [Difranco 1970][research_difranco_1970]
- [DiFranco 1971][research_difranco_1971]
- [Diggins 1951][research_diggins_1951]
- [Dilmi 2022][research_dilmi_2022]
- [Dinc and Otkur 2020][research_dinc_otkur_2020]
- [Dingeldein et al 1975][research_dingeldein_connor_1975]
- [Dittmar 1977][research_dittmar_1977]
- [Dittmar 1978][research_dittmar_1978]
- [Dittmar 1981][research_dittmar_1981]
- [Dittmar 1983][research_dittmar_1983]
- [Dittmar 1984][research_dittmar_1984]
- [Dittmar 1985][research_dittmar_1985]
- [Dittmar 1989][research_dittmar_1989]
- [Dittmar 1989][research_dittmar_1989_2]
- [Dittmar and Hall 1991][research_dittmar_hall_1991]
- [Dittmar and Jeracki 1981][research_dittmar_jeracki_1981]
- [Dittmar and Jeracki 1981][research_dittmar_jeracki_1981_b]
- [Dittmar and Stang 1987][research_dittmar_stang_1987]
- [Dittmar and Stang 1987][research_dittmar_stang_1987_2]
- [Dittmar and Stefko 1983][research_dittmar_stefko_1983_b]
- [Dittmar et al 1979][research_dittmar_jeracki_1979]
- [Dittmar et al 1982][research_dittmar_stefko_1982]
- [Dittmar et al 1983][research_dittmar_stefko_1983]
- [Doak and Vaidya 1970][research_doak_vaidya_1970]
- [Doblhoff 1956][research_doblhoff_1956]
- [Dobrzynski 1981][research_dobrzynski_1981]
- [Dobrzynski 1993][research_dobrzynski_1993]
- [Dodbele et al 1987][research_dodbele_1987]
- [Doebler et al 2023][research_doebler_2023]
- [Doelling 1961][research_doelling_1961]
- [Doelling and Bolt 1961][research_doelling_bolt_1961]
- [Doelling and Bolt 1961][research_doelling_bolt_1961_2]
- [Doggett and Soistmann 1992][research_doggett_soistmann_1992]
- [Doherty and Butzel 1979][research_doherty_butzel_1979]
- [Doherty and Butzel 1979][research_doherty_butzel_1979_2]
- [Dohme 1981][research_dohme_1981]
- [Doko and Sasongko 2026][research_doko_sasongko_2026]
- [Dolmans and Patrick 1998][research_dolmans_patrick_1998]
- [Dolph et al 2021][research_dolph_2021]
- [Doman 1995][research_doman_1995]
- [Domen 1998][research_domen_1998]
- [Domogalla et al 2021][research_domogalla_bertsch_2021]
- [Domogalla et al 2026][research_domogalla_2026]
- [Donaldson et al 2012][research_donaldson_priest_2012]
- [Donateo and Totaro 2019][research_donateo_totaro_2019]
- [Dong et al 2016][research_dong_2016]
- [Dong et al 2016][research_dong_2016_2]
- [Dong et al 2024][research_dong_2024]
- [Dong et al 2024][research_dong_2024_2]
- [Donizetti et al 2023][research_donizetti_2023]
- [Dooley and Yeary 1979][research_dooley_yeary_1979]
- [Dorfling and Rokhsaz 2015][research_dorfling_rokhsaz_2015]
- [Douglas Aircraft Co Long Beach Ca 1962][research_douglas_aircraft_co_long_beach_ca_1962]
- [Douglas Aircraft Co Long Beach Ca 1963][research_douglas_aircraft_co_long_beach_ca_1963]
- [Dowell and Bliss 1978][research_dowell_bliss_1978]
- [Downing et al 1996][research_downing_zamot_1996]
- [Doyle 2020][research_doyle_2020]
- [Dr. Olivia Davis 2021][research_dr_olivia_davis_2021]
- [Dragna and Blanc-Benon 2017][research_dragna_blanc_benon_2017]
- [Dragna and Blanc-Benon 2017][research_dragna_blanc_benon_2017_2]
- [Dragos 1985][research_dragos_1985]
- [Dragoş 1990][research_dragos_1990]
- [Drakin 1963][research_drakin_1963]
- [Dravid 1971][research_dravid_1971]
- [Dreyfus and Dreyfus 1979][research_dreyfus_dreyfus_1979]
- [Dryden and Ballif 1930][research_dryden_ballif_1930]
- [Du 2024][research_du_2024_2]
- [Du et al 2024][research_du_2024]
- [Duan and Zhang 2018][research_duan_zhang_2018]
- [Dubnický et al 2023][research_dubnicky_splichal_2023]
- [Ducard 2015][research_ducard_2015]
- [Duchevet et al 2025][research_duchevet_2025]
- [Dudek et al 2020][research_dudek_2020]
- [Dudziak et al 2020][research_dudziak_2020]
- [Duerksen 1997][research_duerksen_1997]
- [Duffy 1968][research_duffy_1968]
- [Duhl and Thompson 1977][research_duhl_thompson_1977]
- [Dunlap 1969][research_dunlap_1969]
- [Dunlap and Porter 1971][research_dunlap_porter_1971]
- [Dunlap and Schalk 1956][research_dunlap_1956]
- [Dunn and Farassat 1990][research_dunn_farassat_1990]
- [Dunn and Farassat 1992][research_dunn_farassat_1992]
- [Dunn and Tarkenton 1989][research_dunn_tarkenton_1989]
- [Dunn et al 2015][research_dunn_2015]
- [Dunnavan 1983][research_dunnavan_1983]
- [Durand 1893][research_durand_1893]
- [Durand and Wasicko 1967][research_durand_wasicko_1967]
- [Durbin 1983][research_durbin_1983]
- [Durbin and McGeer 1982][research_durbin_mcgeer_1982]
- [Dussart et al 2019][research_dussart_2019]
- [Dussart et al 2019][research_dussart_2019_2]
- [Dusterberry 1964][research_dusterberry_1964]
- [Dutta 2026][research_dutta_2026]
- [Dwyer 1994][research_dwyer_1994]
- [Dyer 1956][research_dyer_1956]
- [Dym and Williams 2015][research_dym_williams_2015]
- [Dynamic Response Analysis of a High Glide Ratio Parachute 2021][research_dynamic_response_2021]
- [Eastman 1986][research_eastman_1986]
- [Echavarria and Poroseva 2015][research_echavarria_poroseva_2015]
- [Eckhaus 1962][research_eckhaus_1962]
- [Ecotière 2023][research_ecotiere_2023]
- [Edenborough 1968][research_edenborough_1968]
- [Edwards 2015][research_edwards_2015]
- [Edwards et al 1997][research_edwards_1997]
- [Eggleston and Diederich 1957][research_eggleston_diederich_1957]
- [Eisenhut and Strohmayer 2026][research_eisenhut_strohmayer_2026]
- [El Gaouti et al 2024][research_el_gaouti_2024]
- [El Safany and Bromfield 2025][research_el_safany_bromfield_2025]
- [El-Ramly et al 1976][research_el_ramly_1976]
- [Elkoby et al 2007][research_elkoby_2007]
- [Ellerbroek et al 2007][research_ellerbroek_stroosma_2007]
- [Elliot et al 1990][research_elliot_1990]
- [Elliott et al 1989][research_elliott_1989]
- [Ellis 1971][research_ellis_1971]
- [Ellis 1972][research_ellis_1972]
- [Elyasi et al 2020][research_elyasi_2020]
- [Elzoghby et al 2017][research_elzoghby_2017]
- [Emami and Roudbari 2019][research_emami_roudbari_2019]
- [Emeric 1966][research_emeric_1966]
- [Emslie 1966][research_emslie_1966]
- [Eney 1968][research_eney_1968]
- [Engblom et al 2016][research_engblom_2016]
- [Englar 1970][research_englar_1970]
- [Envia 1992][research_envia_1992]
- [Envia 2016][research_envia_2016]
- [Envia 2018][research_envia_2018]
- [Eppel 1981][research_eppel_1981]
- [Eppley 1963][research_eppley_1963]
- [Epstein and OFlarity 2019][research_epstein_oflarity_2019]
- [Er-El et al 1989][research_er_el_1989]
- [Erb et al 2009][research_erb_aldrich_2009]
- [Erickson et al 1965][research_erickson_johnc_1965]
- [Ericsson 1987][research_ericsson_1987]
- [Ernst and Sachau 2025][research_ernst_sachau_2025]
- [Ernsthausen 1937][research_ernsthausen_1937]
- [Eser 2023][research_eser_2023]
- [Eshmuradov and Bekbaev 2023][research_eshmuradov_bekbaev_2023]
- [Esnault][research_esnault]
- [Esparza 1975][research_esparza_1975]
- [Esteban et al 2015][research_esteban_2015]
- [Evaluating The Use of Manned and Unmanned Aircraft Systems in Strategic Offensive Tasks 2015][research_evaluating_the_2015]
- [Evans 1975][research_evans_1975]
- [Evans and Dunbar 1982][research_evans_dunbar_1982]
- [Evans and Schilling 1983][research_evans_schilling_1983]
- [Evans and Schilling 1984][research_evans_schilling_1984]
- [Evans et al 1972][research_evans_1972]
- [Evans et al 1972][research_evans_1972_2]
- [Eversman 1990][research_eversman_1990]
- [Experimental Analysis of Exhaust Noise Using a Muffler and 2017][research_experimental_analysis_2017]
- [Eyerci̇oğlu and Aladağ 2021][research_eyercioglu_aladag_2021]
- [Failure of an Aileron Control Cable in an Aircraft 2005][research_failure_of_2005]
- [Fajar and Arifianto 2018][research_fajar_arifianto_2018]
- [Fakhraian et al 2023][research_fakhraian_2023]
- [Fang et al 2023][research_fang_2023]
- [Farajollahi and Markazi 2010][research_farajollahi_markazi_2010]
- [Farassat and Succi 1980][research_farassat_succi_1980]
- [Fard et al 2022][research_fard_2022]
- [Farhat 1998][research_farhat_1998]
- [Farhat 2000][research_farhat_2000]
- [Farhat 2001][research_farhat_2001]
- [Farokhi and Vertzberger 1989][research_farokhi_vertzberger_1989]
- [Fasel 2002][research_fasel_2002]
- [Faulcon and Monteith 1978][research_faulcon_monteith_1978]
- [Fay and Johnstone 1960][research_fay_johnstone_1960]
- [Fechter and Mills 1988][research_fechter_mills_1988]
- [Feero et al 2016][research_feero_2016]
- [Fehlner 1942][research_fehlner_1942]
- [Feimin 2021][research_feimin_2021]
- [Feistel et al 1978][research_feistel_1978]
- [Feistel et al 1981][research_feistel_1981]
- [Feistel et al 1981][research_feistel_1981_2]
- [Fejtek 1993][research_fejtek_1993]
- [Felcyn and Ptak 2022][research_felcyn_ptak_2022]
- [Felder et al 2009][research_felder_kim_2009]
- [Felt and Kehoe 1985][research_felt_kehoe_1985]
- [Feng 2022][research_feng_2022]
- [Fenwick 1966][research_fenwick_1966]
- [Fenwick 1967][research_fenwick_1967]
- [Ferguson and Thomson 2015][research_ferguson_thomson_2015]
- [Ferguson et al 1984][research_ferguson_hanson_1984]
- [Ferrari and Castelli 1985][research_ferrari_castelli_1985]
- [Ferrell et al 1974][research_ferrell_1974]
- [Fetterman and Penland 1960][research_fetterman_penland_1960]
- [Ffowcs Williams and Hawkings 1969][research_ffowcs_williams_hawkings_1969]
- [Fidell 2018][research_fidell_2018]
- [Fidell et al 1989][research_fidell_1989]
- [Fidell et al 1989][research_fidell_1989_2]
- [Fidell et al 1990][research_fidell_reddingius_1990]
- [Fidell et al 1990][research_fidell_secrist_1990]
- [Fidell et al 1998][research_fidell_1998]
- [Figliola 2005][research_figliola_2005]
- [Figueira et al 2025][research_figueira_2025]
- [Finch and Matranga 1959][research_finch_matranga_1959]
- [Finger et al 2020][research_finger_2020]
- [Finger et al 2020][research_finger_2020_2]
- [Fink 1978][research_fink_1978]
- [Fink 1979][research_fink_1979]
- [Fink and Schlinker 1980][research_fink_schlinker_1980]
- [Fink et al 1970][research_fink_1970]
- [Finn and Rogers 2015][research_finn_rogers_2015]
- [Finn and Rogers 2016][research_finn_rogers_2016]
- [Finn and Rogers 2016][research_finn_rogers_2016_2]
- [Finnestead and Antoniou 1965][research_finnestead_antoniou_1965]
- [Finnestead et al 1970][research_finnestead_connor_1970]
- [Fischel and Schneiter 1947][research_fischel_schneiter_1947]
- [Fischer 1992][research_fischer_1992]
- [Fischer 2006][research_fischer_2006]
- [Fisher et al 1956][research_fisher_1956]
- [Fladeland et al 2019][research_fladeland_2019]
- [Flechner and Jacobs 1978][research_flechner_jacobs_1978]
- [Fleming 1954][research_fleming_1954]
- [Flight Sciences Lab Inc Buffalo Ny 1964][research_flight_sciences_lab_inc_buffalo_ny_1964]
- [Flight Test Data Analysis of Hybrid Vertical Take-off and Landing Unmanned Aerial Vehicle 2016][research_flight_test_2016]
- [Flindell et al 2021][research_flindell_2021]
- [Foch and Ailinger 1992][research_foch_ailinger_1992]
- [Ford 1989][research_ford_1989_2]
- [Ford 1990][research_ford_1990]
- [Ford 2004][research_ford_2004]
- [Ford CEng MRAeS 1992][research_fordcengmraes_1992]
- [Forehand and Bair 1969][research_forehand_bair_1969]
- [Forkun et al 2020][research_forkun_makaryshkin_2020]
- [Forsythe 1946][research_forsythe_a_c_r_1946]
- [Fosdick 1970][research_fosdick_1970]
- [Foss 1979][research_foss_1979]
- [Fournier and Silvers 1958][research_fournier_silvers_1958]
- [Fournier et al 2022][research_fournier_2022]
- [Fowler et al][research_jennifer_fowler]
- [Frampton et al 1993][research_frampton_1993]
- [Franklin 1971][research_franklin_1971]
- [Franklin 1972][research_franklin_1972]
- [Franklin et al 1988][research_franklin_1988]
- [Frazier 2016][research_frazier_2016]
- [Fredericks et al 2013][research_fredericks_2013]
- [Frederickson et al 1967][research_frederickson_1967]
- [Freuler and Hoffmann 1977][research_freuler_hoffmann_1977]
- [Friedlander et al 2018][research_friedlander_2018]
- [Friedrich and Robertson 2015][research_friedrich_robertson_2015]
- [Frierson et al 1978][research_frierson_1978]
- [Fruncillo et al 2024][research_fruncillo_luchini_2024]
- [Fruncillo et al 2025][research_fruncillo_luchini_2025]
- [Fry 1967][research_fry_1967]
- [Fry 2008][research_fry_2008]
- [Fu et al 2020][research_fu_2020]
- [Fu et al 2021][research_fu_2021]
- [Fu et al 2026][research_fu_2026]
- [Fujita et al 2021][research_fujita_2021]
- [Fukuda 1960][research_fukuda_1960]
- [Fukuda 1960][research_fukuda_1960_2]
- [Fukuda 1963][research_fukuda_1963]
- [Fukuda 1963][research_fukuda_1963_2]
- [Fuller and Jones 1987][research_fuller_jones_1987]
- [Försching and Zingel 1988][research_forsching_zingel_1988]
- [Gager et al 1962][research_gager_headrick_1962]
- [Gaifullin 2023][research_gaifullin_2023]
- [Gallagher 1971][research_gallagher_1971]
- [Galloway and Bennett 1981][research_galloway_bennett_1981]
- [Gandhi et al 2022][research_gandhi_pepe_2022]
- [Gang and Kwon 2018][research_gang_kwon_2018]
- [Ganiev 1978][research_ganiev_1978]
- [Gao 2023][research_gao_2023]
- [Gao et al 2019][research_gao_2019]
- [Gao et al 2024][research_gao_2024]
- [Gao et al 2024][research_gao_shao_2024]
- [Garcia and Eskandarian 2026][research_garcia_eskandarian_2026]
- [Garcia-Baquero et al 2018][research_garcia_baquero_2018]
- [Gardini et al 2022][research_gardini_2022]
- [Gardner and Downey 1950][research_gardner_downey_1950]
- [Garfinkel 1951][research_garfinkel_1951]
- [Garkushenko and Vinogradov 2016][research_garkushenko_vinogradov_2016]
- [Gasaway 1969][research_gasaway_1969]
- [Gasaway 1970][research_gasaway_1970]
- [Gasaway and Hatfield 1963][research_gasaway_hatfield_1963]
- [Gaston et al 2013][research_gaston_2013]
- [Gates and Schy 1951][research_gates_schy_1951]
- [Gates and Sternfield 1950][research_gates_sternfield_1950]
- [Gatti et al 2015][research_gatti_giulietti_2015]
- [Gautam et al 2025][research_gautam_hanson_2025]
- [Gavrilovic et al 2018][research_gavrilovic_2018]
- [Gavurin 1965][research_gavurin_1965]
- [Gayle and Jeracki 1989][research_gayle_jeracki_1989]
- [Gayne 1965][research_gayne_1965]
- [Gedney et al 1998][research_gedney_abbot_1998]
- [Geiger 2002][research_geiger_2002]
- [Geister et al 2017][research_geister_2017]
- [Genalo][research_genalo]
- [Genalo and Pierson 1978][research_genalo_pierson_1978]
- [General Aviation Aircraft Design 2022][research_general_aviation_2022]
- [General Electric Co Cincinnati Oh 1964][research_general_electric_co_cincinnati_oh_1964]
- [General Electric Co Schenectady Ny 1952][research_generalelectriccoschenectadyny_1952]
- [Geng et al 2024][research_geng_2024]
- [Gennaretti et al 2017][research_gennaretti_2017]
- [George et al 2022][research_george_2022]
- [Georgiou et al 2026][research_georgiou_2026]
- [Gera et al 1981][research_gera_1981]
- [Gerber 2003][research_gerber_2003]
- [Gerken 1979][research_gerken_1979]
- [Gerstle et al 1999][research_gerstle_1999]
- [Geuther and Capristan 2020][research_geuther_capristan_2020]
- [Ghalandari et al 2022][research_ghalandari_2022]
- [Ghenescu et al 2026][research_ghenescu_2026]
- [Ghofur et al 2020][research_ghofur_m_2020]
- [Gibbs 2023][research_gibbs_2023]
- [Gilbert et al 1976][research_gilbert_nguyen_1976]
- [Gilbrook et al 2025][research_gilbrook_2025]
- [Giles 1972][research_giles_1972]
- [Gill et al 2015][research_gill_2015]
- [Gillard 1998][research_gillard_1998]
- [Gille et al 2017][research_gille_2017]
- [Gillfillan 1961][research_gillfillan_1961]
- [Gillfillian 1962][research_gillfillian_1962]
- [Gilyard 1974][research_gilyard_1974]
- [Gimmestad 1980][research_gimmestad_1980]
- [Gleason et al 1996][research_gleason_walker_1996]
- [Glegg and Devenport 2024][research_glegg_devenport_2024]
- [Glenn and Midkiff 1951][research_glenn_midkiff_1951]
- [Gliding and Soaring Flight 1938][research_gliding_and_1938]
- [Glodeck and Standahar 1944][research_edwardglodeck_raymstandahar_1944]
- [Glīzde 2017][research_glizde_2017]
- [Go and Choi 2021][research_go_choi_2021]
- [Godwin et al 1964][research_godwin_frazier_1964]
- [Goestchel et al 2022][research_goestchel_2022]
- [Goglia and Arunkumar 1983][research_goglia_arunkumar_1983]
- [Goland 1952][research_goland_1952]
- [Goland et al 1964][research_goland_miller_1964]
- [Goldman 2016][research_goldman_2016]
- [Goldstein 1982][research_goldstein_1982]
- [Golovkin et al 2019][research_golovkin_2019]
- [Golubinskii and Golubkin 1983][research_golubinskii_golubkin_1983]
- [Golubkin 1980][research_golubkin_1980]
- [Golubkin 1980][research_golubkin_1980_2]
- [Goncharenko 2022][research_goncharenko_2022]
- [Gonczy 2015][research_gonczy_2015]
- [Gong 2024][research_gong_2024]
- [Goodman 1976][research_goodman_1976]
- [Gopalan et al 2022][research_gopalan_2022]
- [Goyal et al 2024][research_goyal_2024]
- [Goyal et al 2025][research_goyal_2025]
- [Graham 1945][research_graham_1945]
- [Graham 1971][research_graham_1971]
- [Graham and Rodriquez 1951][research_graham_rodriquez_1951]
- [Grana and Shanks 1952][research_grana_shanks_1952]
- [Grantham et al 1974][research_grantham_nguyen_1974]
- [Grantham et al 1984][research_grantham_1984]
- [Grantham et al 1985][research_grantham_1985]
- [Grauer 2021][research_grauer_2021]
- [Grauer and Morelli 2023][research_grauer_morelli_2023]
- [Grauer et al 2017][research_grauer_2017]
- [Graves 1982][research_graves_1982]
- [Gray 1964][research_gray_1964]
- [Gray 2009][research_gray_2009]
- [Gray 2026][research_gray_2026]
- [Gray and Kemper 2009][research_gray_kemper_2009]
- [Green 1931][research_green_1931]
- [Green 1988][research_green_1988]
- [Green et al 2023][research_green_2023]
- [Greenhalgh 1983][research_greenhalgh_1983]
- [Greenwood and Schmitz 2014][research_greenwood_schmitz_2014]
- [Greer et al 1999][research_greer_hamory_1999]
- [Greer et al 2000][research_greer_2000]
- [Gregorek 1984][research_gregorek_1984]
- [Gregorek 1995][research_gregorek_1995]
- [Grendysa 2019][research_grendysa_2019]
- [Gresham et al 2024][research_gresham_2024]
- [Grether 1973][research_grether_1973]
- [Griffin and Bellaire 1968][research_griffin_bellaire_1968]
- [Griffin and McBride 1986][research_griffin_mcbride_1986]
- [Griffin et al 1983][research_griffin_1983]
- [Griffith 1971][research_griffith_1971]
- [Griffith and Roberts 1972][research_griffith_roberts_1972]
- [Grindley et al 2025][research_grindley_2025]
- [Grossman et al 1986][research_grossman_gurdal_1986]
- [Grosveld 1985][research_grosveld_1985]
- [Grosveld 1988][research_grosveld_1988]
- [Grosveld et al 1980][research_grosveld_navaneethan_1980]
- [Groves 1955][research_groves_1955]
- [Groves 1956][research_groves_1956]
- [Groves 1956][research_groves_1956_2]
- [Grubin 1972][research_grubin_1972]
- [Grunwald 1961][research_grunwald_1961]
- [Gu 1986][research_gu_1986]
- [Gu 2025][research_gu_2025]
- [Gu et al 2024][research_gu_2024]
- [Gu et al 2026][research_gu_2026]
- [Guerrero et al 2026][research_guerrero_2026]
- [Guido 1991][research_d_1991]
- [Guidry et al 2001][research_guidry_2001]
- [Guimarães Neto 2025][research_guimaraes_neto_2025]
- [Guldal and Andersson 2020][research_guldal_andersson_2020]
- [Gulyaeva et al 2018][research_gulyaeva_2018]
- [Gundry 1977][research_gundry_1977]
- [Guo and Thomas 2015][research_guo_thomas_2015]
- [Guo et al 2020][research_guo_2020]
- [Guo et al 2022][research_guo_2022_2]
- [Gupta et al 2016][research_gupta_2016]
- [Gur 2014][research_gur_2014]
- [Guruswamy 2021][research_guruswamy_2021]
- [Guruswamy 2021][research_guruswamy_2021_2]
- [Guthridge 2025][research_guthridge_2025]
- [Guzik et al 2019][research_guzik_2019]
- [Guérin et al 2023][research_guerin_2023]
- [Gwak and Lee 2017][research_gwak_lee_2017]
- [Gyorgyfalvy 1965][research_gyorgyfalvy_1965]
- [Göksel][research_goksel]
- [Hace 2019][research_hace_2019]
- [Hacker 1977][research_hacker_1977]
- [Hacker and Wroblewski 2009][research_hacker_wroblewski_2009]
- [Haddad et al 2019][research_haddad_2019]
- [Haefner et al 2026][research_haefner_2026]
- [Haftka 1977][research_haftka_1977]
- [Haftka et al 1987][research_haftka_grossman_1987]
- [Hai et al 2025][research_hai_2025]
- [Haider 2024][research_haider_2024]
- [Halimi et al 2019][research_halimi_2019]
- [Hall 1961][research_hall_1961]
- [Hall and Boothe 1972][research_hall_boothe_1972]
- [Hall and Mason 2012][research_hall_mason_2012]
- [Hall and Rogan 1988][research_hall_rogan_1988]
- [Hall and Rogan 1989][research_hall_rogan_1989]
- [Hall et al 1974][research_hall_1974]
- [Hall et al 1994][research_hall_yang_1994]
- [Hall et al 2016][research_hall_2016]
- [Ham et al 1993][research_johnnie_a_ham_1993]
- [Hambrey et al 2017][research_hambrey_feszty_2017]
- [Hamed 1993][research_hamed_1993]
- [Hamel 1970][research_hamel_1970]
- [Hammond and Henderson 1961][research_hammond_henderson_1961]
- [Hamory and Murray 1992][research_philip_j_hamory_james_e_murray_1992]
- [Hamory and Murray 1993][research_hamory_murray_1993]
- [Hamza et al 2022][research_hamza_2022]
- [Han and Barakos 2020][research_han_barakos_2020]
- [Han et al 2024][research_han_2024]
- [Hancock 1972][research_hancock_1972]
- [Handling qualities 2000][research_handling_qualities_2000]
- [Handling Qualities Analysis 2008][research_handling_qualities_2008]
- [Hanin and Barsony-Nagy 1983][research_hanin_barsony_nagy_1983]
- [Hanks 1956][research_hanks_1956]
- [Hansen et al 2022][research_hansen_2022]
- [Hansmann and Stumpf 2026][research_hansmann_stumpf_2026]
- [Hanson 1976][research_hanson_1976]
- [Hanson 1983][research_hanson_1983]
- [Hanson 1985][research_hanson_1985]
- [Hanson 1986][research_hanson_1986]
- [Hanson and Fink 1978][research_hanson_fink_1978]
- [Hanson and Fink 1979][research_hanson_fink_1979]
- [Hanson and Magliozzi 1985][research_hanson_magliozzi_1985]
- [Hanson and Parzych 1993][research_donald_b_hanson_david_j_parzych_1993]
- [Hanson et al 2014][research_hanson_2014]
- [Hanson et al 2023][research_hanson_2023]
- [Hao et al 2023][research_hao_2023]
- [Haque et al 2016][research_haque_asrar_2016]
- [Harendra et al 1973][research_pbharendra_mjjoglekar_1973]
- [Hargest 1966][research_hargest_1966]
- [Hargest 1972][research_hargest_1972]
- [Harlamert 1974][research_harlamert_1974]
- [Harman 1944][research_harman_1944]
- [Harnyoot 2018][research_harnyoot_2018]
- [Harper and Robert P. 1955][research_harper_robert_p_1955]
- [Harper and Sardanowsky 1969][research_harper_sardanowsky_1969]
- [Harris 1996][research_harris_1996]
- [Harris et al 1985][research_harris_1985]
- [Harry and Trobaugh 1966][research_harry_trobaugh_1966]
- [Hart 1956][research_hart_1956]
- [Hart 1984][research_hart_1984]
- [Hart 1992][research_hart_1992]
- [Hart et al 2016][research_hart_2016]
- [Hart et al 2021][research_hart_2021]
- [Hartmann et al 1976][research_hartmann_1976]
- [Harvey and OYoung 2016][research_harvey_oyoung_2016]
- [Harvey and OYoung 2018][research_harvey_oyoung_2018]
- [Hasan et al 2018][research_hasan_2018]
- [Hasegawa and Sakaue 2023][research_hasegawa_sakaue_2023]
- [Hasegawa and Sakaue 2024][research_hasegawa_sakaue_2024]
- [Hashii and Thompson 2018][research_hashii_thompson_2018]
- [Hashim 2020][research_hashim_2020]
- [Hawks 1982][research_hawks_1982]
- [Haworth et al][research_loran_haworth]
- [Hay 1971][research_hay_1971]
- [Hayes 1945][research_hayes_1945]
- [He and Ai 2018][research_he_ai_2018]
- [He et al 2020][research_he_2020]
- [He et al 2024][research_he_2024]
- [He et al 2026][research_he_2026]
- [He et al 2026][research_he_2026_2]
- [Head and Hohenemser 1951][research_head_hohenemser_1951]
- [Healy 1958][research_healy_1958]
- [Healy 1969][research_healy_1969]
- [Healy et al 2022][research_healy_2022]
- [Hebbar and Pashilkar 2016][research_hebbar_pashilkar_2016]
- [Hebert et al 1973][research_hebert_1973]
- [Hede 2017][research_hede_2017]
- [Hedrick and Nichols 1975][research_hedrick_nichols_1975]
- [Heidelberg and Woodward 1989][research_heidelberg_woodward_1989]
- [Heidenreich 1947][research_heidenreich_1947]
- [Heinrich et al 1964][research_heinrich_nietz_1964]
- [Heitman and Mixson 1986][research_heitman_mixson_1986]
- [Helicopter Handling Qualities 1982][research_helicopter_handling_1982]
- [Helicopter Yaw Control 1990][research_helicopter_yaw_1990]
- [Heller and Dobrzynski 1977][research_heller_dobrzynski_1977]
- [Henderson 1978][research_henderson_1978]
- [Henderson 2022][research_henderson_2022]
- [Henderson 2023][research_henderson_2023]
- [Hendrick 1977][research_hendrick_1977]
- [Henke et al 2010][research_henke_lammering_2010]
- [Hennessy 2014][research_hennessy_2014]
- [Henriquez Huecas et al 2022][research_henriquez_huecas_2022]
- [Henry et al 2023][research_henry_2023]
- [Henyey 2009][research_henyey_2009]
- [Herrmann and Ben-Asher 2016][research_herrmann_ben_asher_2016]
- [Hess 1977][research_hess_1977]
- [Hess 2012][research_hess_2012]
- [Hess 2016][research_hess_2016]
- [Hess 2018][research_hess_2018]
- [Hess and Peng 2018][research_hess_peng_2018]
- [Hewes 1959][research_hewes_1959]
- [Heyson 1980][research_heyson_1980]
- [Hicks et al 2014][research_hicks_durbin_2014]
- [Higbie 1995][research_higbie_1995]
- [Higgins and Jacobs 1928][research_higgins_jacobs_1928]
- [Higgins and Shomber 1965][research_higgins_shomber_1965]
- [Higgins et al 2020][research_higgins_2020]
- [High altitude reconnaissance aircraft design 1989][research_high_altitude_1989]
- [High-Fidelity Aerodynamic Models 2015][research_high_fidelity_aerodynamic_2015]
- [High-Speed Water-Based Aircraft 1953][research_highspeed_waterbased_1953]
- [Highland et al 2020][research_highland_2020]
- [Hightower 1985][research_hightower_1985]
- [Higuchi et al 1987][research_higuchi_1987]
- [Hille et al 2023][research_hille_stumpf_2023]
- [Hillebrand et al 2025][research_hillebrand_2025]
- [Hiller Aircraft Corp Palo Alto Ca 1956][research_hiller_aircraft_corp_palo_alto_ca_1956]
- [Hilton and Henderson 1978][research_hilton_henderson_1978]
- [Hilton and Kasper 1974][research_hilton_kasper_1974]
- [Hilton et al 1975][research_hilton_1975]
- [Hilton et al 1975][research_hilton_1975_2]
- [Hilton et al 1975][research_hilton_connor_1975]
- [Hilton et al 1975][research_hilton_connor_1975_b]
- [Hinds and Shames 1975][research_hinds_shames_1975]
- [Hiramatsu 2023][research_hiramatsu_2023]
- [Hirschkron et al 1979][research_hirschkron_1979]
- [Hirschkron et al 1979][research_hirschkron_1979_2]
- [Hirschkron et al 1979][research_hirschkron_1979_3]
- [Hirschorn 1960][research_hirschorn_1960]
- [Hirsh 1965][research_hirsh_1965]
- [Hitzel and Zimper 2018][research_hitzel_zimper_2018]
- [Hjellvik and Mallam 2024][research_hjellvik_mallam_2024]
- [Hodgson and Guo 2006][research_hodgson_guo_2006]
- [Hoehne 1967][research_hoehne_1967]
- [Hoehne and Hoffman 1961][research_hoehne_hoffman_1961]
- [Hoelzen et al 2018][research_hoelzen_2018]
- [Hoerner 1936][research_hoerner_1936]
- [Hoerner 1952][research_hoerner_1952]
- [Hoey 1992][research_robert_g_hoey_1992]
- [Hoff 1982][research_hoff_1982]
- [Hoffman and Kennedy 1982][research_hoffman_kennedy_1982]
- [Hoh and Mitchell 1983][research_hoh_mitchell_1983]
- [Hoh et al 1981][research_hoh_1981]
- [Hohenwarter et al 2022][research_hohenwarter_2022]
- [Hoholis et al 2016][research_hoholis_2016]
- [Holberg and Grabowsky 1981][research_holberg_grabowsky_1981]
- [Holger 1980][research_holger_1980]
- [Holleman and Gilyard 1972][research_holleman_gilyard_1972]
- [Holley and Irving B. 1946][research_holley_irving_b_1946]
- [Hom et al 1983][research_hom_1983]
- [Homans et al 1978][research_homans_1978]
- [Hopkins 1977][research_hopkins_1977]
- [Hopkins and Lovette 1977][research_hopkins_lovette_1977]
- [Horstmann and Quast 1980][research_horstmann_quast_1980]
- [Hoseini and Hodges 2019][research_hoseini_hodges_2019]
- [Hosier 1976][research_hosier_1976]
- [Hosier 1977][research_hosier_1977]
- [Hosseini and Mesbahi 2016][research_hosseini_mesbahi_2016]
- [Hosseini et al 2020][research_hosseini_2020]
- [Hou and Song 2024][research_hou_song_2024]
- [Houbolt 1971][research_houbolt_1971]
- [Houck et al 1977][research_houck_moore_1977]
- [Houston et al 1954][research_houston_smith_1954]
- [Howard 1977][research_howard_1977]
- [Howe 1978][research_howe_1978]
- [Howe 1981][research_howe_1981]
- [Howe 1999][research_howe_1999]
- [Howell 1988][research_howell_1988]
- [Howie and Brugger 2000][research_howie_brugger_2000]
- [Howlett 1979][research_howlett_1979]
- [Hoyos et al 2021][research_hoyos_jimenez_2021]
- [Hrishikeshavan et al 2015][research_hrishikeshavan_2015]
- [Hu et al 2022][research_hu_2022]
- [Hu et al 2025][research_hu_2025]
- [Hu et al 2026][research_hu_2026]
- [Hu et al 2026][research_hu_2026_2]
- [Huang 2023][research_huang_2023_2]
- [Huang and Wu 2006][research_huang_wu_2006]
- [Huang et al 2006][research_huang_pippalapalli_2006]
- [Huang et al 2016][research_huang_ghorbaniasl_2016]
- [Huang et al 2018][research_huang_2018]
- [Huang et al 2020][research_huang_yao_2020]
- [Huang et al 2023][research_huang_2023]
- [Huang et al 2023][research_huang_2023_4]
- [Huang et al 2025][research_huang_2025]
- [Huang et al 2026][research_huang_du_2026]
- [Hubbard 1993][research_hubbard_1993]
- [Huff 1949][research_huff_w_w_1949]
- [Hughes and Gazzaniga 1988][research_hughes_gazzaniga_1988]
- [Hui and Chen 2023][research_hui_chen_2023]
- [Hukuda 1962][research_hukuda_1962]
- [Hultgren 2015][research_hultgren_2015]
- [Human reaction to aircraft noise 1989][research_human_reaction_1989]
- [Human-Powered Aircraft Wing Design A Case Study in 2014][research_human_powered_aircraft_2014]
- [Humpert et al 2015][research_humpert_gaeta_2015]
- [Humphreys et al 2016][research_humphreys_2016]
- [Humphreys-Jennings et al 2020][research_humphreys_jennings_2020]
- [Hunn 1953][research_hunn_1953]
- [Hunsaker et al 2019][research_hunsaker_moorthamers_2019]
- [Hunsaker et al 2020][research_hunsaker_2020]
- [Hunsaker et al 2020][research_hunsaker_montgomery_2020]
- [Hunsaker et al 2021][research_hunsaker_moorthamers_2021]
- [Hunter 1959][research_hunter_1959]
- [Hunter and Burke 1992][research_hunter_burke_1992]
- [Hunton and James Harry A. 1948][research_hunton_james_harry_a_1948]
- [Hurley 1969][research_hurley_1969]
- [Hussain and Dutilleux 2020][research_hussain_dutilleux_2020]
- [Hutchins 1972][research_hutchins_1972]
- [Huzita 1971][research_huzita_1971]
- [Hwang and Pi 1978][research_hwang_pi_1978]
- [Hwang and Pi 1979][research_hwang_pi_1979]
- [Hwang et al 2016][research_hwang_2016]
- [Hwang et al 2016][research_hwang_2016_2]
- [Hübner and Strümpfel 2020][research_hubner_strumpfel_2020]
- [Ibren et al 2020][research_ibren_2020]
- [Identification method of temperature corrections to aircraft engine thrust in flight tests 2023][research_identification_method_2023]
- [Iemma 2016][research_iemma_2016]
- [Iemma et al 2021][research_iemma_2021]
- [Ignatyev et al 2019][research_ignatyev_2019]
- [Iliff and Maine 1984][research_iliff_maine_1984]
- [Iliff and Wang 1996][research_iliff_wang_1996]
- [Iliff and Wang 1997][research_iliff_wang_1997]
- [Iliff and Wang 1999][research_iliff_wang_1999]
- [In-Flight Testing into Atmospheric Electricity for Future Aircraft 2025][research_in_flight_testing_2025]
- [Ingraham 2023][research_ingraham_2023]
- [Ingraham et al 2019][research_ingraham_gray_2019]
- [Ingram 1964][research_ingram_1964]
- [Instruments for Soaring Flight 1999][research_instruments_for_1999]
- [Intano and Howse 1991][research_intano_howse_1991]
- [Introduction to Aircraft Aerodynamic Design 2021][research_introduction_to_2021]
- [Ioannis and Ioannis 2026][research_ioannis_ioannis_2026]
- [Iovnovich et al 2018][research_iovnovich_2018]
- [Irmawan and Eko Prasetiyo 2020][research_irmawan_eko_prasetiyo_2020]
- [Irsyad Lukman and Agoes Moelyadi 2018][research_irsyad_lukman_agoes_moelyadi_2018]
- [Irvine 1968][research_irvine_1968]
- [Irving 1999][research_irving_1999]
- [Ishola et al 2024][research_ishola_2024]
- [Isikveren 2018][research_isikveren_2018]
- [Islam et al 2015][research_islam_2015]
- [Israel Moguel 2015][research_israel_moguel_2015]
- [Ivanković et al 2023][research_ivankovic_2023]
- [Ivey 1945][research_ivey_1945]
- [Ivler et al 2022][research_ivler_2022]
- [Izquierdo et al 2017][research_izquierdo_2017]
- [Içke and Baysal 2021][research_icke_baysal_2021]
- [Jack et al 2014][research_jack_hoffler_2014]
- [Jackson et al 1993][research_jackson_1993]
- [Jacobs 1983][research_jacobs_1983]
- [Jacobs and Bartlett 1981][research_jacobs_bartlett_1981]
- [Jacobson and Joshi 1977][research_jacobson_joshi_1977]
- [Jacobson and Joshi 1978][research_jacobson_joshi_1978]
- [Jacques 1976][research_jacques_1976]
- [James 1975][research_james_1975]
- [James and Vaughn 1976][research_james_vaughn_1976]
- [Jamison 1966][research_jamison_1966]
- [JanakiRam 1980][research_janakiram_1980]
- [JanakiRam and Scruggs 1982][research_janakiram_scruggs_1982]
- [Jang and Ahn 2022][research_jang_ahn_2022]
- [Januszewska and Pringle 2021][research_januszewska_pringle_2021]
- [Janzen and Precourt 1989][research_janzen_precourt_1989]
- [Jaron et al 2023][research_jaron_2023]
- [Jategaonkar 2023][research_jategaonkar_2023]
- [Jayalakshmi et al 2021][research_jayalakshmi_patel_2021]
- [Jeff Berton][research_jeff_berton]
- [Jeffery et al 1977][research_jeffery_1977]
- [Jekateryńczuk and Piotrowski 2025][research_jekaterynczuk_piotrowski_2025]
- [Jekateryńczuk et al 2025][research_jekaterynczuk_2025]
- [Jenke 1976][research_jenke_1976]
- [Jenney 1979][research_jenney_1979]
- [Jennings 1931][research_jennings_1931]
- [Jentys and Breitsamter 2023][research_jentys_breitsamter_2023]
- [Jeong et al 2015][research_jeong_2015]
- [Jeong et al 2022][research_jeong_2022]
- [Jeong et al 2023][research_jeong_2023]
- [Jeong et al 2024][research_jeong_2024]
- [Jeracki and Mitchell 1981][research_jeracki_mitchell_1981]
- [Jernell 1978][research_jernell_1978]
- [Jewell et al 1979][research_jewell_1979]
- [Ji et al 2017][research_ji_2017]
- [Ji et al 2022][research_ji_2022]
- [Ji et al 2023][research_ji_2023]
- [Jia and Lee 2022][research_jia_lee_2022]
- [Jiang 1999][research_jiang_1999]
- [Jiang et al 2000][research_jiang_an_2000]
- [Jianhong and Yanxiang 2026][research_jianhong_yanxiang_2026]
- [Jiao et al 2022][research_jiao_2022]
- [Jimenez et al 2016][research_jimenez_2016]
- [Jin 2024][research_jin_2024]
- [Jin and Lee 2015][research_jin_lee_2015]
- [Jing and Ma 2025][research_jing_ma_2025]
- [Jing and Ye 2021][research_jing_ye_2021]
- [Jobe 1984][research_jobe_1984]
- [Joel B Lonzaga, An exact solution of an augmented][research_joel_b_lonzaga_2]
- [Joel B. Lonzaga, Nonlinear Acoustic Propagation in][research_joel_b_lonzaga]
- [Johannes 1971][research_johannes_1971]
- [Johansson 2023][research_johansson_2023]
- [Johnson 1949][research_johnson_1949]
- [Johnson 1972][research_johnson_1972]
- [Johnson 1972][research_johnson_1972_2]
- [Johnson 1975][research_johnson_1975]
- [Johnson and Anderson 1966][research_johnson_anderson_1966]
- [Johnson and Hagerman 1950][research_johnson_hagerman_1950]
- [Johnson and Sternfield 1948][research_johnson_sternfield_1948]
- [Johnston and Donham 1982][research_johnston_donham_1982]
- [Johnston et al 1965][research_johnston_1965]
- [Johnston et al 1965][research_johnston_1965_2]
- [Johnston et al 1974][research_johnston_1974]
- [Jolley and Caro 1970][research_jolley_1970]
- [Jones 1946][research_jones_1946]
- [Jones 1950][research_jones_1950_2]
- [Jones 1950, The spanwise distribution of lift][research_jones_1950]
- [Jones 1964][research_jones_1964]
- [Jones 1965][research_jones_1965]
- [Jones 1970][research_jones_1970]
- [Jones 1976][research_jones_1976]
- [Jones et al 2013][research_jones_2013]
- [Joo and Hwang 2017][research_joo_hwang_2017]
- [Jovanovic and Novak 2022][research_jovanovic_novak_2022]
- [Jovanovic and Novak 2022][research_jovanovic_novak_2022_2]
- [Jovanovic et al 2022][research_jovanovic_2022]
- [Jovanovic et al 2023][research_jovanovic_2023]
- [Ju et al 2026][research_ju_2026]
- [Juhasz et al 2022][research_juhasz_2022]
- [Jung et al 2025][research_jung_2025]
- [Jurczyk 2018][research_jurczyk_2018]
- [Justiz and Patel 1988][research_justiz_patel_1988]
- [Juřička and Juřičková 2020][research_juricka_jurickova_2020]
- [Jäger et al 2021][research_jager_2021]
- [Kacik and Goetzendorf-Grabowski 2025][research_kacik_goetzendorf_grabowski_2025]
- [Kadyrov et al 2022][research_kadyrov_2022]
- [Kafali and Güçlü 2023][research_kafali_guclu_2023]
- [Kai 2024][research_kai_2024]
- [Kakade et al 2022][research_kakade_chikkala_2022]
- [Kaldschmidt et al 1973][research_kaldschmidt_syltebo_1973]
- [Kallergis 1987][research_kallergis_1987]
- [Kamrath 2022][research_kamrath_2022]
- [Kamrath et al 2016][research_kamrath_2016]
- [Kandasamy et al 2018][research_s_2018]
- [Kaneko and Martins 2023][research_kaneko_martins_2023]
- [Kang and Choi 2022][research_kang_choi_2022]
- [Kang and Woolsey 2020][research_kang_woolsey_2020]
- [Kant et al 2023][research_kant_2023]
- [Kao 1974][research_kao_1974]
- [Kapnik 2019][research_kapnik_2019]
- [Kapoor et al 2021][research_kapoor_2021]
- [Kaptsov and Rodrigues 2018][research_kaptsov_rodrigues_2018]
- [Karimian et al 2023][research_karimian_paruchuri_2023]
- [Karimian et al 2023][research_karimian_paruchuri_2023_b]
- [Karpel 1990][research_karpel_1990]
- [Karpuk and Mosca 2024][research_karpuk_mosca_2024]
- [Kartashov et al 2021][research_kartashov_2021]
- [Kashitani et al 2019][research_kashitani_2019]
- [Kato et al 2018][research_kato_2018]
- [Katz 1989][research_katz_1989]
- [Katz 2017][research_katz_2017]
- [Katz and Levin 1986][research_katz_levin_1986]
- [Katz and Maskew 1988][research_katz_maskew_1988]
- [Kayser et al 2024][research_kayser_2024]
- [Kayten and Koven 1945][research_kayten_koven_1945]
- [Ke and Zheng 2016][research_ke_zheng_2016]
- [Keast 1961][research_keast_1961]
- [Keener 1985][research_keener_1985]
- [Keenohan 1942][research_keenohan_1942]
- [Kehoe and Ellison 1985][research_kehoe_ellison_1985]
- [Keilman 2019][research_keilman_2019]
- [Keleş 2022][research_keles_2022]
- [Keller 2019][research_keller_2019]
- [Kellermann et al 2020][research_kellermann_2020]
- [Kelley and Enevoldson 1981][research_kelley_enevoldson_1981]
- [Kelley et al 1986][research_kelley_phelps_1986]
- [Kelley et al 1990][research_kelley_1990]
- [Kellogg 1946][research_kellogg_1946]
- [Kelly 1988][research_kelly_1988]
- [Kelly 1993][research_kelly_1993]
- [Kelly and Brown 1980][research_kelly_brown_1980]
- [Kelly and Wilson 1995][research_kelly_wilson_1995]
- [Kemp 1943][research_kemp_1943]
- [Kennelly et al 1990][research_kennelly_1990]
- [Kenny 2004][research_kenny_2004]
- [Kensche 2003][research_kensche_2003]
- [Kentfield 2012][research_kentfield_2012]
- [Keshavan 1980][research_keshavan_1980]
- [Keshavarz and Ohadi 2017][research_keshavarz_ohadi_2017]
- [Keskin 2026][research_keskin_2026]
- [Keskin et al 2021][research_keskin_2021]
- [Kester 1974][research_kester_1974]
- [Key 1971][research_key_1971]
- [Key 1982][research_key_1982]
- [Keyel et al 2017][research_keyel_2017]
- [Khalil and Bauknecht 2024][research_khalil_bauknecht_2024]
- [Khalil and Fezans 2020][research_khalil_fezans_2020]
- [Khalil et al 2022][research_khalil_2022]
- [khan and Padhy 2019][research_khan_padhy_2019]
- [Khanna et al 2022][research_khanna_2022]
- [Kheiri and Riazat 2025][research_kheiri_riazat_2025]
- [Kholodar 2016][research_kholodar_2016]
- [Kholyavko 1971][research_kholyavko_1971]
- [Khorrami et al][research_mehdi_r_khorrami]
- [Khorrami et al 2009][research_khorrami_2009]
- [Khuat et al 2025][research_khuat_2025]
- [Kiang 1971][research_kiang_1971]
- [Kibbee 1978][research_kibbee_1978]
- [Kida 1982][research_kida_1982]
- [Kida and Miyai 1978][research_kida_miyai_1978]
- [Kidd and Bull 1963][research_kidd_bull_1963]
- [Kier et al 1972][research_kier_1972]
- [Kigotho et al 2022][research_kigotho_bodylski_2022]
- [Kilgore and Averett 1964][research_kilgore_averett_1964]
- [Kilimtzidis and Kostopoulos 2023][research_kilimtzidis_kostopoulos_2023]
- [Kim][research_kim]
- [Kim 2016][research_kim_2016]
- [Kim 2020][research_kim_2020]
- [Kim and Atkins 2022][research_kim_atkins_2022]
- [Kim and Jeong 2026][research_kim_jeong_2026]
- [Kim and Kim 2020][research_kim_kim_2020]
- [Kim et al 2022][research_kim_2022_2]
- [Kim et al 2022][research_kim_2022_3]
- [Kim et al 2022][research_kim_2022_4]
- [Kim et al 2025][research_kim_2025]
- [Kim et al 2025][research_kim_2025_2]
- [Kim et al 2025][research_kim_2025_3]
- [Kim et al 2025][research_kim_2025_4]
- [Kim et al 2025][research_kim_2025_5]
- [Kimathi and Lantos 2023][research_kimathi_lantos_2023]
- [Kingan and Parry 2020][research_kingan_parry_2020]
- [Kingan and Self 2009][research_kingan_self_2009]
- [Kingan et al 2023][research_kingan_2023]
- [Kirby 2021][research_kirby_2021]
- [Kirby 2021][research_kirby_2021_2]
- [Kirby 2022][research_kirby_2022]
- [Kirsch et al 2020][research_kirsch_2020]
- [Kisabo et al 2017][research_kisabo_2017]
- [Kistyarev and Wang 2025][research_kistyarev_wang_2025]
- [Kizer 1977][research_kizer_1977]
- [Klein et al 1982][research_klein_1982]
- [Klein et al 1983][research_klein_1983]
- [Klein et al 2017][research_klein_krainski_2017]
- [Klemin and Walling 1943][research_klemin_walling_1943]
- [Kletschkowski 2012][research_kletschkowski_2012]
- [Kloet et al 2017][research_kloet_2017]
- [Klug et al 2023][research_klug_2023]
- [Knott 1974][research_knott_1974]
- [Knowd 1982][research_knowd_1982]
- [Ko 1971][research_ko_1971]
- [Ko 1975][research_ko_1975]
- [Ko 1975][research_ko_1975_2]
- [Ko 1979][research_ko_1979]
- [Ko et al 2026][research_ko_2026]
- [Koch 1998][research_koch_1998]
- [Kochersberger et al 2003][research_kochersberger_player_2003]
- [Kochuk et al 2021][research_kochuk_2021]
- [Kocur et al 2023][research_kocur_2023]
- [Kodji et al 2023][research_kodji_2023]
- [Kodji et al 2024][research_kodji_2024]
- [Kodres 2000][research_kodres_2000]
- [Koessler 2018][research_koessler_2018]
- [Kohlman 1977][research_kohlman_1977]
- [Kohne et al 2024][research_kohne_korzilius_2024]
- [Komadina et al 2002][research_komadina_drake_2002]
- [Konar 2020][research_konar_2020]
- [Kone et al 2023][research_kone_ghinet_2023]
- [Kone et al 2024][research_kone_ghinet_2024]
- [Kone et al 2024][research_kone_ghinet_2024_b]
- [Konert and Kasprzyk 2024][research_konert_kasprzyk_2024]
- [Koopmann 1976][research_koopmann_1976]
- [Kopecki 2016][research_kopecki_2016]
- [Koper 1976][research_koper_1976]
- [Kordan et al 1985][research_kordan_vonlavante_1985]
- [Korsun and Moung Htang 2023][research_korsun_moung_htang_2023]
- [Korsun et al 2017][research_korsun_2017]
- [Korsun et al 2018][research_korsun_2018]
- [Korsun et al 2024][research_korsun_2024]
- [Kotitschke et al 2026][research_kotitschke_2026]
- [Kotwicz Herniczek][research_kotwiczherniczek]
- [Kou et al 2021][research_kou_2021]
- [Kourbatski 2024][research_kourbatski_2024]
- [Kowalska and Goetzendorf-Grabowski 2022][research_kowalska_goetzendorfgrabowski_2022]
- [Kozak 2021][research_kozak_2021]
- [Kozakiewicz and Grzegorczyk 2021][research_kozakiewicz_grzegorczyk_2021]
- [Kozeruk and Korzhik 2022][research_kozeruk_korzhik_2022]
- [Kozeruk and Korzhyk 2019][research_kozeruk_korzhyk_2019]
- [Kozhanov et al 2022][research_kozhanov_2022]
- [Kozupa et al 2023][research_kozupa_2023]
- [Kraft 1985][research_kraft_1985]
- [Krawczyk et al 2024][research_krawczyk_2024]
- [Kraxberger et al 2024][research_kraxberger_2024]
- [Krebs and Bramesfeld 2016][research_krebs_bramesfeld_2016]
- [Krebs and Bramesfeld 2017][research_krebs_bramesfeld_2017]
- [Kretov and Tiniakov 2022][research_kretov_tiniakov_2022]
- [Kriebel 1964][research_kriebel_1964]
- [Kriebel 1972][research_kriebel_1972]
- [Kriechbaum and Stineman 1972][research_kriechbaum_stineman_1972]
- [Krishnamurthy and Rizzi 2022][research_krishnamurthy_rizzi_2022]
- [Krishnan et al 2020][research_krishnan_2020]
- [Kristl et al 1999][research_kristl_1999]
- [Krivosheikin and Perelygin 2015][research_krivosheikin_perelygin_2015]
- [Kroo 2000][research_kroo_2000]
- [Kruger and Uranga 2024][research_kruger_uranga_2024]
- [Kryter 1966][research_kryter_1966]
- [Kryter 1967][research_kryter_1967]
- [Kryter 1982][research_kryter_1982]
- [Kryter and Williams 1966][research_kryter_williams_1966]
- [Krzywoblocki 1943][research_krzywoblocki_1943]
- [Kuantama et al 2019][research_kuantama_2019]
- [Kubrynski 1999][research_kubrynski_1999]
- [Kubrynski 2012][research_kubrynski_2012]
- [Kuettner 1952][research_kuettner_1952]
- [Kuhlman 1979][research_kuhlman_1979]
- [Kuhlman and Liaw 1987][research_kuhlman_liaw_1987]
- [Kuhlmann et al 2024][research_kuhlmann_romerostarke_2024]
- [Kuhn 1975][research_kuhn_1975]
- [Kukreja 2008][research_kukreja_2008]
- [Kulba et al 2021][research_kulba_2021]
- [Kulhánek 2019][research_kulhanek_2019]
- [Kulikova N.V. CHulin N.A. 2023][research_refinement_of_2023]
- [Kull and Finegold 2024][research_kull_finegold_2024]
- [Kumar 1997][research_kumar_1997]
- [Kumar and Ghosh 2018][research_kumar_ghosh_2018]
- [Kumar and Ghosh 2023][research_kumar_ghosh_2023]
- [Kumar and Ghosh 2023][research_kumar_ghosh_2023_2]
- [Kumar et al 2025][research_kumar_2025]
- [Kumar et al 2025][research_kumar_2025_2]
- [Kumar et al 2026][research_kumar_mathi_2026]
- [Kumar S Rajanikanth 2024][research_kumar_s_rajanikanth_2024]
- [Kumari and Raghunath 2016][research_kumari_raghunath_2016]
- [Kuppuswamy and Kiran 1981][research_kuppuswamy_kiran_1981]
- [Kurbjun 1959][research_kurbjun_1959]
- [Kurdyla 1963][research_kurdyla_1963]
- [Kutney and Piszkin 1964][research_kutney_piszkin_1964]
- [Kuźniar and Orkisz 2019][research_kuzniar_orkisz_2019]
- [Kyi and Feng 2026][research_kyi_feng_2026]
- [Kyrpenko 2015][research_kyrpenko_2015]
- [Köhler and Jeschke 2021][research_kohler_jeschke_2021]
- [König et al 2024][research_konig_2024]
- [la Cour-Harbo 2018][research_la_cour_harbo_2018]
- [Ladeira et al 2024][research_ladeira_2024]
- [Lagemann et al 2024][research_lagemann_2024]
- [Laine 1982][research_laine_1982]
- [Laitone 1983][research_laitone_1983]
- [Laitone 1994][research_laitone_1994]
- [Laly et al 2023][research_laly_2023]
- [Lamar et al 1981][research_lamar_1981]
- [Lamp and Luckner 2013][research_lamp_luckner_2013]
- [Lampton et al 2024][research_lampton_2024]
- [Landers and Lacoss 1978][research_landers_lacoss_1978]
- [Landman et al 2017][research_landman_2017]
- [Landman et al 2020][research_landman_2020]
- [Landmann et al 1989][research_landmann_1989]
- [Lang 1981][research_lang_1981]
- [Lang 2024][research_lang_2024]
- [Lang et al 2022][research_lang_2022]
- [Lang et al 2025][research_lang_2025]
- [Lange and Gieseler 1953][research_lange_gieseler_1953]
- [Langer and Blech 2019][research_langer_blech_2019]
- [Lapygin and Tretyakov 1986][research_lapygin_tret_yakov_1986]
- [Large 1975][research_large_1975]
- [Large and Pesyridis 2018][research_large_pesyridis_2018]
- [Larrabee 1974][research_larrabee_1974]
- [Larrabee 1975][research_larrabee_1975]
- [Lauber 1967][research_lauber_1967]
- [Lauchle and Park 2002][research_lauchle_park_2002]
- [Lauk and Unt 2015][research_lauk_unt_2015]
- [Lauk et al 2017][research_lauk_seegel_2017]
- [Lazos and Visser 2006][research_lazos_visser_2006]
- [Le Clainche et al 2019][research_le_clainche_2019]
- [le Roux et al 2025][research_leroux_bosman_2025]
- [Leahy et al 2015][research_leahy_2015]
- [Lechner et al 2021][research_lechner_2021]
- [Ledegang and Groen 2015][research_ledegang_groen_2015]
- [Lee 2019][research_lee_2019]
- [Lee 2023][research_lee_2023]
- [Lee and Ko 2025][research_lee_ko_2025]
- [Lee and Lee 2026][research_lee_lee_2026]
- [Lee and Motsinger 1975][research_lee_motsinger_1975]
- [Lee and Sutherland 1976][research_lee_sutherland_1976]
- [Lee and Yee 2024][research_lee_yee_2024]
- [Lee et al 2017][research_lee_2017]
- [Lee et al 2017][research_lee_2017_2]
- [Lee et al 2020][research_lee_2020_2]
- [Lee et al 2021][research_lee_2021]
- [Lee et al 2022][research_lee_2022]
- [Lee et al 2022][research_lee_2022_2]
- [Lee et al 2025][research_lee_2025]
- [Lee et al 2026][research_lee_2026]
- [Legriffon et al 2023][research_legriffon_bertsch_2023]
- [Lei and Liu 2019][research_lei_liu_2019]
- [Leishman 1966][research_leishman_1966]
- [Lempert 1975][research_lempert_1975]
- [Lendraitis 2019][research_lendraitis_2019]
- [Leng][research_leng]
- [Lennart S Hultgren et al 2020][research_lennart_s_hultgren_2020]
- [Leong Chee Hang et al 2022][research_leong_chee_hang_2022]
- [Leonidov 2025][research_leonidov_2025]
- [Lerbs 1955][research_lerbs_1955]
- [Lester and Fuller 1986][research_lester_fuller_1986]
- [Letcher 1995][research_letcher_1995]
- [Leth et al 1998][research_leth_samuelsson_1998]
- [Letica and Rizzi 2024][research_letica_rizzi_2024]
- [Level Flight Performance Flight Test and Data Reduction 2003][research_level_flight_2003]
- [Levi and Nelson 1964][research_levi_nelson_1964]
- [Levin and Katz 1984][research_levin_katz_1984]
- [Levinsky et al 1968][research_levinsky_1968]
- [Levison 1982][research_levison_1982]
- [Levy 1992][research_levy_1992]
- [Lewis 1929][research_lewis_1929]
- [Lewis 1930][research_lewis_1930]
- [Leylek and Costello 2010][research_leylek_costello_2010]
- [Leylek and Costello 2015][research_leylek_costello_2015]
- [Li 1981][research_li_1981]
- [Li 2019][research_li_2019]
- [Li and Da Ronch 2025][research_li_daronch_2025]
- [Li and Qi 2022][research_li_qi_2022]
- [Li and Qin 2020][research_li_qin_2020]
- [Li and Qin 2021][research_li_qin_2021]
- [Li and Qin 2022][research_li_qin_2022]
- [Li and Rodrigues 2025][research_li_rodrigues_2025]
- [Li and Yang 2017][research_li_yang_2017]
- [Li and Yang 2017][research_li_yang_2017_2]
- [Li et al 2020][research_li_2020]
- [Li et al 2021][research_li_2021]
- [Li et al 2022][research_li_2022]
- [Li et al 2022][research_li_2022_3]
- [Li et al 2022][research_li_2022_5]
- [Li et al 2023][research_li_2023]
- [Li et al 2023][research_li_2023_2]
- [Li et al 2023][research_li_2023_4]
- [Li et al 2024][research_li_2024]
- [Li et al 2024][research_li_yuan_2024]
- [Li et al 2025][research_li_2025]
- [Li et al 2025][research_li_2025_2]
- [Li et al 2026][research_li_2026]
- [Liang et al 2026][research_liang_2026]
- [Lichota 2023][research_lichota_2023]
- [Lichota et al 2017][research_lichota_2017]
- [Lichtenstein 1952][research_lichtenstein_1952]
- [Lichtenstein and Williams 1961][research_lichtenstein_williams_1961]
- [Lieberman and Hoffman 1964][research_lieberman_hoffman_1964]
- [Liem 2018][research_pliem_2018]
- [Light aircraft propeller - Design parameter effects on 1993][research_light_aircraft_1993]
- [Likhite 2022][research_likhite_2022]
- [Lilla et al 2025][research_lilla_2025]
- [Lilley 2004][research_lilley_2004]
- [Lilley 2006][research_lilley_2006]
- [Lim et al 2023][research_lim_2023]
- [Lim et al 2023][research_lim_2023_2]
- [Lim et al 2025][research_lim_2025_2]
- [Lin 2007][research_lin_2007]
- [Lincke and Pieren 2024][research_lincke_pieren_2024]
- [Lincke and Pieren 2024][research_lincke_pieren_2024_2]
- [Lincke et al 2025][research_lincke_2025]
- [Lindstedt et al 2019][research_lindstedt_2019]
- [Lindstrom et al 1970][research_lindstrom_rebeske_1970]
- [Linehan and Mohseni 2016][research_linehan_mohseni_2016]
- [Linnell 1963][research_linnell_1963]
- [Lippisch 1930][research_lippisch_1930]
- [Lippisch 1935][research_lippisch_1935]
- [Litherland et al][research_brandon_l_litherland]
- [Litt et al 2012][research_litt_2012]
- [Litt et al 2022][research_jonathan_s_litt_2022]
- [Little and Russell 1976][research_little_russell_1976]
- [Liu 1962][research_liu_1962]
- [Liu 2018][research_liu_2018_3]
- [Liu and Stumpf 2018][research_liu_stumpf_2018]
- [Liu and Sun 2016][research_liu_sun_2016]
- [Liu et al 1983][research_liu_1983]
- [Liu et al 2015][research_liu_2015_2]
- [Liu et al 2017][research_liu_2017_2]
- [Liu et al 2018][research_liu_2018_2]
- [Liu et al 2021][research_liu_2021]
- [Liu et al 2023][research_liu_zhang_2023]
- [Liu et al 2026][research_liu_fan_2026]
- [Livescu 2016][research_livescu_2016]
- [Lobanovskii 1983][research_lobanovskii_1983]
- [Lobitz et al 2023][research_lobitz_2023]
- [Lockard et al 2008][research_lockard_2008]
- [Loewy 1963][research_loewy_1963]
- [Loewy and Sutton 1966][research_loewy_sutton_1966]
- [Loffi et al 2021][research_loffi_2021]
- [Lofthouse and Cummings 2017][research_lofthouse_cummings_2017]
- [Lomax 1948][research_lomax_1948]
- [Lombaerts et al 2017][research_lombaerts_2017]
- [Loomis and Porter 1965][research_loomis_porter_1965]
- [Lorenz 1985][research_lorenz_1985]
- [Loth and Boyle 1969][research_loth_boyle_1969]
- [Lotinga et al 2025][research_lotinga_2025]
- [Lotinga et al 2025][research_lotinga_2025_2]
- [Loubeau 2021][research_loubeau_2021]
- [Louis and Louis 2020][research_louis_louis_2020]
- [Lourenco et al 1996][research_lourenco_1996]
- [Lovell and Stassi 1950][research_lovell_stassi_1950]
- [Lowrance and Smith 1996][research_lowrance_smith_1996]
- [Lu et al 2015][research_lu_2015]
- [Lu et al 2017][research_lu_2017]
- [Lu et al 2019][research_lu_2019]
- [Lu et al 2025][research_lu_2025_3]
- [Lucas 1978][research_lucas_1978]
- [Ludeman 1979][research_ludeman_1979]
- [Luderer and Thielecke 2025][research_luderer_thielecke_2025]
- [Ludlow 2024][research_ludlow_2024]
- [Lundberg 1937][research_lundberg_1937]
- [Lundberg 1938][research_lundberg_1938]
- [Lundry 1977][research_lundry_1977]
- [Lungu and Lungu 2015][research_lungu_lungu_2015]
- [Lungu and Lungu 2016][research_lungu_lungu_2016]
- [Luoma 1944][research_luoma_1944]
- [Lupp and Cesnik 2015][research_lupp_cesnik_2015]
- [Luqmanul Hakim et al 2018][research_luqmanul_hakim_2018]
- [Lusardi 2023][research_lusardi_2023]
- [Lush 1950][research_lush_1950]
- [Luskin 1950][research_luskin_1950]
- [Lustig et al 1960][research_lustig_1960]
- [Lux and Landwehr 1980][research_lux_landwehr_1980]
- [Lv et al 2023][research_lv_2023]
- [Lyon and Pande 1971][research_lyon_pande_1971]
- [Lyu and Liem 2020][research_lyu_liem_2020]
- [Lyu et al 2022][research_lyu_2022]
- [Löhr and Haines 2024][research_lohr_haines_2024]
- [Løvik and Holden 2024][research_lvik_holden_2024]
- [Ma 1989][research_ma_1989]
- [Ma and Chen 2023][research_ma_chen_2023]
- [Ma and Guo 2018][research_ma_guo_2018]
- [Ma et al 2019][research_ma_2019]
- [Ma et al 2020][research_ma_2020]
- [Ma et al 2022][research_ma_2022]
- [Ma et al 2022][research_ma_2022_2]
- [Ma et al 2023][research_ma_abouhamzeh_2023]
- [Ma et al 2024][research_ma_2024]
- [Ma et al 2025][research_ma_2025_2]
- [Ma et al 2025][research_ma_2025_3]
- [MacCready 1962][research_maccready_1962]
- [Macdonald and Schneider 2019][research_macdonald_schneider_2019]
- [MacDonald and Shepherd 2008][research_macdonald_shepherd_2008]
- [Macey 1956][research_macey_1956]
- [MacGregor et al 1973][research_macgregor_1973]
- [Mack 2003][research_mack_2003]
- [Mackie and Lawrence 2019][research_mackie_lawrence_2019]
- [MACKlNNON and Madden 1972][research_macklnnon_madden_1972]
- [MACKlNNON and Madden 1972][research_macklnnon_madden_1972_2]
- [MacLeod 1952][research_r_g_macleod_1952]
- [Macmillan 1981][research_macmillan_1981]
- [MacNeill and Verstraete 2017][research_macneill_verstraete_2017]
- [Madelung 1923][research_madelung_1923]
- [Madhusudhana et al 2024][research_s_v_madhusudhana_2024]
- [Madureira and de Almeida 2026][research_madureira_dealmeida_2026]
- [Magee and Taylor 1971][research_magee_taylor_1971]
- [Magee and Taylor 1971][research_magee_taylor_1971_2]
- [Maglieri and Hubbard 1975][research_maglieri_hubbard_1975]
- [Magliozzi 1982][research_magliozzi_1982]
- [Magliozzi 1983][research_magliozzi_1983]
- [Mahak et al 2017][research_mahak_2017]
- [Maikapar 1966][research_maikapar_1966]
- [Majka 2015][research_majka_2015]
- [Malcom 1969][research_malcom_1969]
- [Malgoezar et al 2019][research_malgoezar_2019]
- [Malik et al 2017][research_malik_2017]
- [Malina and Parsons 1941][research_malina_parsons_1941]
- [Malisani et al 2021][research_malisani_2021]
- [Mallik et al 2015][research_mallik_2015]
- [Malmuth 1966][research_malmuth_1966]
- [Malpica and Lusardi 2013][research_malpica_lusardi_2013]
- [Malvestuto et al 1950][research_malvestuto_1950]
- [Mamada and Ando 1974][research_mamada_ando_1974]
- [Mamich A.V. et al 2025][research_mamich_a_v_2025]
- [Mandal and Gu 2016][research_mandal_gu_2016]
- [Mangold and Strohmayer 2025][research_mangold_strohmayer_2025]
- [Manickam et al 2020][research_manickam_2020]
- [Maniet 2001][research_maniet_jr_2001]
- [Manning et al 1992][research_clarke_o_manning_1992]
- [Mansour 1985][research_mansour_1985]
- [Mao and Zhao 1990][research_mao_zhao_1990]
- [Marchman and Abtahi 1985][research_marchman_abtahi_1985]
- [Marcinkiewicz et al 2019][research_marcinkiewicz_2019]
- [Marcus and Räf 2019][research_marcus_raf_2019]
- [Mardanpour et al 2018][research_mardanpour_2018]
- [Maria Thoma et al 2024][research_maria_thoma_2024]
- [Marinus et al 2009][research_marinus_roger_2009]
- [Mark et al 2019][research_mark_2019]
- [Marques et al 2026][research_marques_2026]
- [Marquis-Favre et al 2023][research_marquis_favre_2023]
- [Marsden 1974][research_marsden_1974]
- [Marsh 1981][research_marsh_1981]
- [Marshall and Anderson 2015][research_marshall_anderson_2015]
- [Marston et al 2015][research_marston_sternberg_2015]
- [Martin 1978][research_martin_1978]
- [Martina 1953][research_martina_1953]
- [Martina 1954][research_martina_1954]
- [Martinez 1989][research_martinez_1989]
- [Mastroddi et al 2018][research_mastroddi_2018]
- [Masud et al 2016][research_masud_malik_2016]
- [Masuda 1996][research_masuda_1996]
- [Matheny and Gatlin 1978][research_matheny_gatlin_1978]
- [Matheson 1987][research_matheson_1987]
- [Mathur and Atkins 2023][research_mathur_atkins_2023]
- [Matos and Marta 2024][research_matos_marta_2024]
- [Matouk 2024][research_matouk_2024]
- [Matranga and Armstrong 1959][research_matranga_armstrong_1959]
- [Matsuki et al 2018][research_matsuki_2018]
- [Matsushita and Suzuki 1984][research_matsushita_suzuki_1984]
- [Matt et al 2025][research_matt_2025]
- [Maughmer][research_maughmer]
- [Maughmer 2003][research_maughmer_2003]
- [Maughmer et al 1990][research_maughmer_1990]
- [Maughmer et al 2024][research_maughmer_metkowski_2024]
- [May and Widdison 1971][research_may_widdison_1971]
- [Mayes and Edge 1962][research_mayes_edge_1962]
- [Maynard and Evans 1945][research_maynard_evans_1945]
- [McAree et al 2018][research_mcaree_2018]
- [McCarthy et al 1955][research_mccarthy_1955]
- [McCormick 1956][research_mccormick_b_w_1956]
- [McCormick 1959][research_mccormick_1959]
- [McCormick 1969][research_mccormick_1969]
- [McCracken 1979][research_mccracken_1979]
- [McCurdy 1984][research_mccurdy_1984]
- [McCurdy 1985][research_mccurdy_1985]
- [McCurdy 1989][research_mccurdy_1989]
- [McCurdy 1991][research_mccurdy_1991]
- [McCurdy and Powell 1984][research_mccurdy_powell_1984]
- [McCutchen 1989][research_mccutchen_1989]
- [McDonnell Aircraft Corp St Louis Mo 1950][research_mcdonnell_aircraft_corp_st_louis_mo_1950]
- [McDonnell and Ning 2020][research_mcdonnell_ning_2020]
- [McGREGOR and Smith 1966][research_mcgregor_smith_1966]
- [McKay and Kingan 2019][research_mckay_kingan_2019]
- [McKee 1943][research_mckee_1943]
- [McLaughlin and Shaw][research_mclaughlin_shaw]
- [McMasters 1979][research_mcmasters_1979]
- [McMasters and Palmer 1975][research_mcmasters_palmer_1975]
- [McNeill and Innis 1965][research_mcneill_innis_1965]
- [McNeill and Vomaske 1959][research_mcneill_vomaske_1959]
- [McPIKE 1972][research_mcpike_1972]
- [McPike 1976][research_mcpike_1976]
- [McQUILLEN and Huang 1971][research_mcquillen_huang_1971]
- [McVeigh and McHugh 1984][research_mcveigh_mchugh_1984]
- [Mechel 1962][research_mechel_1962]
- [Mechel et al 1963][research_mechel_1963]
- [Meckstroth and Ordóñez 2020][research_meckstroth_ordonez_2020]
- [Mehra et al 1972][research_mehra_1972]
- [Mehra et al 1974][research_mehra_1974]
- [Meissner 1973][research_meissner_1973]
- [Mellish et al 2020][research_mellish_2020]
- [Melton 1985][research_melton_1985]
- [Melton and Jacobson 1983][research_melton_jacobson_1983]
- [Memorandum, US Reconnaissance Aircraft Reports Interception][research_memorandum_us]
- [Meng et al 2017][research_meng_2017]
- [Mengle et al 2006][research_mengle_ganz_2006]
- [Mennell 1975][research_mennell_1975]
- [Menon et al 2022][research_menon_2022]
- [Mentzer and Nourse 1940][research_mentzer_nourse_1940]
- [Merino-Martinez and Nicola Quaroni 2025][research_merino_martinez_nicola_quaroni_2025]
- [Merrill 2003][research_merrill_2003]
- [Methods for aircraft noise prediction 2011][research_methods_for_2011]
- [Metodiev 2024][research_metodiev_2024]
- [Metodiev 2025][research_metodiev_2025]
- [Metzger 1973][research_metzger_1973]
- [Metzger 1974][research_metzger_1974]
- [Metzger 1981][research_metzger_1981]
- [Metzger and Farassat 2007][research_metzger_farassat_2007]
- [Metzger and Worobel 1973][research_metzger_worobel_1973]
- [Metzger et al 1976][research_metzger_1976]
- [Metzger et al 1980][research_metzger_menthe_1980]
- [Meullen et al 1956][research_meullen_1956]
- [Meyer and Jiran 1981][research_meyer_jiran_1981]
- [Meyer and Johnson 1952][research_carllmeyer_lavernajohnson_1952]
- [Meyerhoff and Zvengrowski 1962][research_meyerhoff_zvengrowski_1962]
- [Michael Feary][research_michael_feary]
- [Michaels 1969][research_michaels_1969]
- [Michel 1989][research_michel_1989]
- [Middleton et al 1975][research_middleton_hurt_1975]
- [Miguel 1974][research_miguel_1974]
- [Mihalik and Keane 2022][research_mihalik_keane_2022]
- [Mihelič and Pozderec 2023][research_mihelic_pozderec_2023]
- [Mikkelson et al 1984][research_mikkelson_mitchell_1984]
- [Miles 1952][research_miles_1952]
- [Miles 1953][research_miles_1953]
- [Milillo 1972][research_milillo_1972]
- [Milla and Blick 1966][research_milla_blick_1966]
- [Miller 1942][research_miller_1942]
- [Miller 1970][research_miller_1970]
- [Miller 1985][research_miller_1985_b]
- [Miller and Clark 1965][research_miller_clark_1965]
- [Miller and Eagan 1997][research_miller_eagan_1997]
- [Miller and Eagan 1997][research_miller_eagan_1997_b]
- [Miller and Eagan 1998][research_miller_eagan_1998]
- [Miller and Franklin 1968][research_miller_franklin_1968]
- [Miller and Khinoo 1994][research_miller_khinoo_1994]
- [Miller and Koch 1985][research_miller_koch_1985]
- [Miller et al 1982][research_miller_1982]
- [Miller et al 1983][research_miller_1983]
- [Min et al 2015][research_min_lim_2015]
- [Minor 2008][research_minor_2008]
- [Minwalla et al 2016][research_minwalla_2016]
- [Minwalla et al 2016][research_minwalla_2016_2]
- [Misol 2020][research_misol_2020]
- [Mitcham 1949][research_mitcham_1949]
- [Mitchell and Hoh 1984][research_mitchell_hoh_1984]
- [Mitchell and Mikkelson 1982][research_mitchell_mikkelson_1982]
- [Mitchell et al 2003][research_mitchell_2003]
- [Mitcheltree et al 1986][research_mitcheltree_1986]
- [Mixson and Powell 1984][research_mixson_powell_1984]
- [Mixson and Powell 1985][research_mixson_powell_1985]
- [Mixson et al 1977][research_mixson_barton_1977]
- [Mixson et al 1979][research_mixson_barton_1979]
- [Mixson et al 1981][research_mixson_greene_1981]
- [Mo et al 2016][research_mo_2016]
- [Mo et al 2017][research_mo_2017]
- [Mobley et al 2016][research_mobley_2016]
- [Mockelman et al 2026][research_mockelman_crane_2026]
- [Moelyadi et al 2021][research_moelyadi_2021]
- [Mohamed and Joy 2021][research_mohamed_joy_2021]
- [Mohamed et al 2021][research_mohamed_2021]
- [Mohammadi Farhadi et al 2018][research_mohammadi_farhadi_2018]
- [Mokhtari et al 2020][research_mokhtari_2020]
- [Mokry and Rainbird 1975][research_mokry_rainbird_1975]
- [Molchanov 1981][research_molchanov_1981]
- [Momiyama 1977][research_momiyama_1977]
- [Monitoring of aircraft noise† 2011][research_monitoring_of_2011]
- [Monstein et al 2019][research_monstein_2019]
- [Montalvo and Costello 2015][research_montalvo_costello_2015]
- [Monzambe et al 2024][research_monzambe_2024]
- [Mooij 1985][research_mooij_1985]
- [Mooij 1985][research_mooij_1985_b]
- [Mooij 1985][research_mooij_1985_c]
- [Moore and Moore 2012][research_moore_moore_2012]
- [Moore and Moore 2012][research_moore_moore_2012_b]
- [Moralez et al 2004][research_moralez_2004]
- [Moreira et al 2022][research_moreira_2022]
- [Moreland Jr. et al 1965][research_moreland_jr_1965]
- [Morelli][research_eugeneamorelli]
- [Morelli and Cooper 2015][research_morelli_cooper_2015]
- [Morfey and Howell 1981][research_morfey_howell_1981]
- [Morfey and Tester 1977][research_morfey_tester_1977]
- [Morgado et al 2013][research_morgado_silvestre_2013]
- [Morgan 1954][research_morgan_1954]
- [Morgan 1961][research_morgan_1961]
- [Morgan and Hardin 1975][research_morgan_hardin_1975]
- [Morge-Rollet et al 2022][research_morge_rollet_2022]
- [Morhy Cavalcante et al 2026][research_morhy_cavalcante_2026]
- [Morinaga et al 2021][research_morinaga_2021]
- [Morita 1970][research_morita_1970]
- [Morita 1971][research_morita_1971]
- [Morita 1971][research_morita_1971_2]
- [Moriya 1972][research_moriya_1972]
- [Morris and Alexander 1978][research_morris_alexander_1978]
- [Morris et al 1973][research_morris_1973]
- [Morton 1956][research_morton_1956]
- [Moses and Zeitlin 1975][research_moses_zeitlin_1975]
- [Moshkov 2022][research_moshkov_2022]
- [Moshkov 2026][research_moshkov_2026]
- [Moshkov 2026][research_moshkov_2026_b]
- [Moshkov 2026][research_moshkov_2026_c]
- [Moshkov and Samokhin 2016][research_moshkov_samokhin_2016]
- [Moshkov and Samokhin 2021][research_moshkov_samokhin_2021]
- [Moshkov and Yakovlev 2023][research_moshkov_yakovlev_2023]
- [Moshkov et al 2019][research_moshkov_2019]
- [Mosov et al 2020][research_mosov_2020]
- [Mostarac et al 2022][research_mostarac_rescic_2022]
- [Mothes 2019][research_mothes_2019]
- [Motyka and Hall 1973][research_motyka_hall_1973]
- [Moul and Brown 1959][research_moul_brown_1959]
- [Moul and Brown 1979][research_moul_brown_1979]
- [Mr. S. Aravindan et al 2017][research_mr_s_aravindan_2017]
- [Mrusek 2021][research_mrusek_2021]
- [Mueller et al 1993][research_mueller_1993]
- [Mueller et al 2004][research_mueller_paluszek_2004]
- [Muhlstein and Coe 1979][research_muhlstein_coe_1979]
- [Mukhachev et al 2022][research_mukhachev_2022]
- [Muller 1971][research_muller_1971]
- [Multi-Rotors A Revolution In 2015][research_multi_rotors_a_2015]
- [Mulyanto and Zulkarnain 2020][research_mulyanto_zulkarnain_2020]
- [Mulyanto and Zulkarnain 2021][research_mulyanto_zulkarnain_2021]
- [Muneer et al 2026][research_muneer_2026]
- [Mungiole and Wilson 2003][research_mungiole_wilson_2003]
- [Muniraj and Farhood 2019][research_muniraj_farhood_2019]
- [Munk 1925][research_munk_1925]
- [Munro and Ahuja 2003][research_munro_ahuja_2003]
- [Murillo and McMasters 1984][research_murillo_mcmasters_1984]
- [Murphy et al 2019][research_murphy_frink_2019]
- [Murray and Warren 1944][research_murray_warren_1944]
- [Murray et al 1992][research_murray_1992]
- [Murrieta-Mendoza et al 2016][research_murrieta_mendoza_2016]
- [Muser 1979][research_muser_1979]
- [Mutyala and Soedel 1974][research_mutyala_soedel_1974]
- [Myala et al 2020][research_myala_2020]
- [Myers et al 2018][research_myers_2018]
- [Müller and Moormann 2023][research_muller_moormann_2023]
- [Müller et al 2026][research_muller_2026]
- [Na and Cho 2022][research_na_cho_2022]
- [Nabi et al 2018][research_nabi_2018]
- [NACA Conference on Aircraft 1957][research_naca_conference_1957]
- [NACA Conference on High-speed Aerodynamics. a Compilation 1958][research_naca_conference_1958]
- [Nagabhushan 1983][research_nagabhushan_1983]
- [Nagao 1998][research_nagao_1998]
- [Nagaraja et al 1982][research_nagaraja_1982]
- [Nagata et al 1973][research_nagata_1973]
- [Nagy and Kirsten 1976][research_nagy_kirsten_1976]
- [Najafi et al 2025][research_najafi_2025]
- [Nakka and Alexander-Ramos 2021][research_nakka_alexander_ramos_2021]
- [Nallasamy et al 1987][research_nallasamy_clark_1987]
- [Nallasamy et al 1989][research_nallasamy_1989]
- [Nam and Joshi 2017][research_nam_joshi_2017]
- [Nam and Mavris 2018][research_nam_mavris_2018]
- [Narayan 1975][research_narayan_1975]
- [Narendra and Tripathi 1973][research_narendra_tripathi_1973]
- [Narimani et al 2025][research_narimani_2025]
- [Nark et al 2004][research_nark_2004]
- [Nark et al 2017][research_nark_2017]
- [Nash 1982][research_nash_1982]
- [Nash-Webber 1973][research_nash_webber_1973]
- [Nasoulis et al 2022][research_nasoulis_2022]
- [Nassif 1969][research_nassif_1969]
- [National Advisory Committee for Aeronautics report No. 570. The effect of lateral controls in producing motion of an airplane as computed from wind-tunnel data 1937][research_national_advisory_1937]
- [National advisory committee for aeronautics: Report No. 424, Wind-tunnel research comparing lateral control devices, particularly at high angles of attack. IV. Floating tip ailerons on rectangular wings 1932][research_national_advisory_1932]
- [Naval Air Test Center Patuxent River Md 1957][research_naval_air_test_center_patuxent_river_md_1957]
- [Naval Air Test Center Patuxent River Md 1963][research_naval_air_test_center_patuxent_river_md_1963]
- [Navaratna et al 2019][research_navaratna_2019]
- [Navaratna et al 2022][research_navaratna_2022]
- [Nayfeh 1980][research_nayfeh_1980]
- [Nazarenko and Nevezhina 1972][research_nazarenko_nevezhina_1972]
- [Neal and Smith 1971][research_neal_smith_1971]
- [Neff 2019][research_neff_2019]
- [Negahban et al 2024][research_negahban_2024]
- [Nejati et al 2018][research_nejati_2018]
- [Nelson 1938][research_nelson_1938]
- [Nelson 1964][research_nelson_1964]
- [Nelson 1965][research_nelson_1965]
- [Nelson 1974][research_nelson_1974]
- [Nelson et al 2012][research_nelson_2012]
- [Nemec et al 2024][research_nemec_bedonian_2024]
- [Neto and Signor 2023][research_neto_signor_2023]
- [Neves et al 2020][research_neves_2020]
- [Newell and Herrick 1979][research_newell_herrick_1979]
- [Newell et al 1963][research_newell_1963]
- [Newsom and Tosti 1959][research_newsom_tosti_1959]
- [Nguyen and Xiong][research_nhan_nguyen_juntao_xiong]
- [Nguyen and Yano 2024][research_nguyen_yano_2024]
- [Nguyen et al 2017][research_nguyen_2017]
- [Nguyen et al 2018][research_nguyen_2018_2]
- [Ni et al 2025][research_ni_2025]
- [Nicolaides 1971][research_nicolaides_1971]
- [Nicolaides 1976][research_nicolaides_1976]
- [Nicolaides and Tragarz 1971][research_nicolaides_tragarz_1971]
- [Nie et al 2025][research_nie_2025]
- [Nikhade et al 2023][research_nikhade_barde_2023]
- [Nimal and Venkatesan 2019][research_nimal_a_2019]
- [Nishinomiya et al 1978][research_nishinomiya_1978]
- [Nnonyelu 2020][research_nnonyelu_2020]
- [Nnonyelu 2021][research_nnonyelu_2021]
- [Noda et al 2022][research_noda_2022]
- [Noda et al 2025][research_noda_2025]
- [Nonweiler 1960][research_nonweiler_1960]
- [Norris and Bauer 1993][research_norris_bauer_1993]
- [Norris and Ostashev 2022][research_norris_ostashev_2022]
- [North American Aviation Inc Los Angeles Ca 1956][research_northamericanaviationinclosangelesca_1956]
- [North American Aviation Inc Los Angeles Ca 1963][research_north_american_aviation_inc_los_angeles_ca_1963]
- [Northrop Aircraft Inc Hawthorne Ca 1952][research_northrop_aircraft_inc_hawthorne_ca_1952]
- [Norton 1990][research_norton_1990]
- [Novak 1970][research_novak_1970]
- [Nyborg and Mintzer 1955][research_nyborg_mintzer_1955]
- [Obayashi 1999][research_obayashi_1999]
- [Obermark 2004][research_obermark_2004]
- [Odell 1977][research_odell_1977]
- [ODonnell and Mohseni 2019][research_odonnell_mohseni_2019]
- [Ogawa et al 2015][research_ogawa_2015]
- [Ogawara et al 2024][research_ogawara_2024]
- [Ogburn and Brown 1980][research_ogburn_brown_1980]
- [Ogburn et al 1991][research_marilyn_e_ogburn_1991]
- [Ogburn et al 1994][research_ogburn_1994]
- [Ogiso et al 2019][research_ogiso_2019]
- [Ogren et al 1974][research_ogren_1974]
- [Oh and Yoon 2022][research_oh_yoon_2022]
- [Oh et al 2023][research_oh_lerud_2023]
- [Ohm et al 2020][research_ohm_2020]
- [Ohta 1935][research_ohta_1935]
- [Ohta et al 1979][research_ohta_1979]
- [Ohta et al 1982][research_ohta_1982]
- [Okada 1994][research_okada_1994]
- [Oktay and Özen 2022][research_oktay_ozen_2022]
- [Okumoto and Elsanker 1973][research_okumoto_elsanker_1973]
- [Oleson and Patrick 1998][research_oleson_patrick_1998]
- [Oleynikov et al 2018][research_oleynikov_2018]
- [Oliveira et al 2021][research_oliveira_payne_2021]
- [Ollerhead 1971][research_ollerhead_1971]
- [Ollerhead 1973][research_ollerhead_1973]
- [Ollerhead 1982][research_ollerhead_1982]
- [Olsen et al 2019][research_olsen_2019]
- [Olson 1978][research_olson_1978]
- [Olson 2015][research_olson_2015]
- [Olson et al 2004][research_olson_hill_2004]
- [Omair Alhatim 2026][research_omair_alhatim_2026]
- [Oncley 1970][research_oncley_1970]
- [Onkar et al 2024][research_onkar_2024]
- [Optimal Switching Techniques For Aircraft Lateral Dynamics 2019][research_optimal_switching_2019]
- [Optimization software helps design low-noise rotorcraft 2000][research_optimization_software_2000]
- [Ordonez 2003][research_ordonez_2003]
- [Orkisz et al 2019][research_orkisz_wygonik_2019]
- [Orme et al 1998][research_orme_1998]
- [Ormsbee 1977][research_ormsbee_1977]
- [Ormsbee et al 1977][research_ormsbee_siddiqi_1977]
- [Oruc et al 2017][research_oruc_2017]
- [Ostashev and Goedecke 2005][research_ostashev_goedecke_2005]
- [Ostashev and Wilson 2022][research_ostashev_wilson_2022]
- [Ostrikov et al 2020][research_ostrikov_2020]
- [Otsuka et al 2017][research_otsuka_2017]
- [Otsuka et al 2021][research_otsuka_2021]
- [Otsuka et al 2022][research_otsuka_2022]
- [Ouda 2021][research_ouda_2021]
- [Ouellette et al 2026][research_ouellette_2026]
- [Ovcharenko and Poplavsky 2021][research_ovcharenko_poplavsky_2021]
- [P5 et al 2026][research_p5_2026]
- [Page et al 2021][research_page_2021]
- [Page et al 2026][research_page_2026]
- [Palaia et al 2023][research_palaia_2023]
- [Palchikovskiy et al 2023][research_palchikovskiy_2023]
- [Palkin and Zenchenko 2025][research_palkin_zenchenko_2025]
- [Palleja-Cabre et al 2024][research_pallejacabre_macey_2024]
- [Palmer and Petitt 1976][research_palmer_petitt_1976]
- [Pamadi and Pai 1980][research_pamadi_pai_1980]
- [Pan and Huang 2019][research_pan_huang_2019]
- [Pande 2025][research_pande_2025]
- [Panel Discussion Acoustic Wave Propagation through 1976][research_panel_discussion_1976_b]
- [Panel Discussion Aircraft Noise Prediction 1976][research_panel_discussion_1976]
- [Pao 1971][research_pao_1971]
- [Pao and Evans 1971][research_pao_evans_1971]
- [Pao and Lan 1978][research_pao_lan_1978]
- [Papa 2023][research_papa_2023]
- [Papageorgiou et al 2018][research_papageorgiou_2018]
- [Papageorgiou et al 2020][research_papageorgiou_2020]
- [Papamoschou and Debiasi 2003][research_papamoschou_debiasi_2003]
- [Papamoschou and Phong 2018][research_papamoschou_phong_2018]
- [Park 2026][research_park_2026_2]
- [Park 2026][research_park_2026_b]
- [Park et al 2018][research_park_2018]
- [Park et al 2018][research_park_2018_2]
- [Park et al 2023][research_park_2023]
- [Park et al 2026][research_park_2026]
- [Parry 1995][research_parry_1995]
- [Parry and Crighton 1989][research_parry_crighton_1989]
- [Parry et al 2020][research_parry_2020]
- [Parry et al 2020][research_parry_2020_2]
- [Pasareanu et al 2018][research_pasareanu_2018]
- [Pascioni et al 2026][research_pascioni_2026]
- [Paswan et al 2025][research_paswan_2025]
- [Paszkowski et al 2024][research_paszkowski_2024]
- [Pate 1964][research_pate_1964]
- [Pate and Deitering 1963][research_pate_deitering_1963]
- [Paterson et al 1973][research_paterson_1973]
- [Patrick 1986][research_patrick_1986]
- [Patrick and Nagel 1989][research_patrick_nagel_1989]
- [Patrick et al 2000][research_patrick_lobo_2000]
- [Patterson 1989][research_patterson_1989]
- [Patterson et al][research_andrewpatterson_nairahovakimyan]
- [Patterson et al][research_william_c_patterson]
- [Patterson et al 2016][research_patterson_2016]
- [Pauli et al 1974][research_pauli_corliss_1974]
- [Paullin et al 2011][research_paullin_2011]
- [Pauls and Gollnick 2025][research_pauls_gollnick_2025]
- [Paulson 1976][research_paulson_1976]
- [Paulson and Shanks 1959][research_paulson_shanks_1959]
- [Paulson and Shanks 1961][research_paulson_shanks_1961]
- [Paulson and Shanks 1961][research_paulson_shanks_1961_2]
- [Pavel et al 2018][research_pavel_jan_2018]
- [Pavlenko and Reslan 2022][research_pavlenko_reslan_2022]
- [Pavlusíková and Chodelka 2023][research_pavlusikova_chodelka_2023]
- [Pawlak 1994][research_pawlak_1994]
- [Pearson 1937][research_pearson_1937]
- [Pearson and Jones 1976][research_henryapearson_roberttjones_1976]
- [Peart 1991][research_peart_1991]
- [Pecho et al 2019][research_pecho_2019]
- [Peebles 2007][research_peebles_2007]
- [Pegg and Hilton 1974][research_pegg_hilton_1974]
- [Pegg et al 1974][research_pegg_1974]
- [Pei et al 2016][research_pei_2016]
- [Pelykh and Andryushchenko 2024][research_pelykh_andryushchenko_2024]
- [Pena and Diamond 1965][research_pena_diamond_1965]
- [Peng et al 2026][research_peng_2026]
- [Pentz and Tang 2017][research_pentz_tang_2017]
- [Peplow and Liu 2025][research_peplow_liu_2025]
- [Pereira Gouveia da Silva et al 2025][research_pereira_gouveia_da_silva_2025]
- [Perez and Jansen 2014][research_perez_jansen_2014]
- [Performance characteristics of two-blade propeller fans 1930][research_performance_characteristics_1930]
- [Perisho 1959][research_perisho_1959]
- [Perkins et al 1977][research_perkins_1977]
- [Peron and Carpenter 1992][research_peron_carpenter_1992]
- [Perry 1978][research_perry_1978]
- [Perry et al 2021][research_perry_2021]
- [Perry et al 2023][research_perry_2023]
- [Persoon et al 1980][research_persoon_1980]
- [Pestana 2010][research_pestana_2010]
- [Peterse 2024][research_peterse_2024]
- [Petersen 1981][research_petersen_1981]
- [Petersen et al 1962][research_petersen_1962]
- [Peterson and Warmbrodt 1996][research_peterson_warmbrodt_1996]
- [Petitt 2017][research_petitt_2017]
- [Petrescu et al 2017][research_petrescu_2017]
- [Petrovskii 1965][research_petrovskii_1965]
- [Petty 1975][research_petty_1975]
- [Pfaff 1968][research_pfaff_1968]
- [Pfeiffer 2017][research_pfeiffer_2017]
- [Pfeifle and Fichter 2023][research_pfeifle_fichter_2023]
- [Pfeifle et al 2022][research_pfeifle_2022]
- [Pham et al 2025][research_pham_2025]
- [Phillips 1942][research_phillips_1942]
- [Phillips 1975][research_phillips_1975]
- [Phillips 2002][research_phillips_2002]
- [Phillips and Everest 1953][research_phillips_everest_1953]
- [Phun et al 2015][research_phun_2015]
- [Picolet 1932][research_picolet_1932]
- [Pieper 1965][research_pieper_1965]
- [Pierson 1977][research_pierson_1977]
- [Pierson and Chen 1979][research_pierson_chen_1979_2]
- [Pierson and Chen 1979, Minimum Altitude-Loss Soaring in][research_pierson_chen_1979]
- [Pierson and De Jong 1978][research_pierson_dejong_1978]
- [Pietrasanta and Galloway 1956][research_pietrasanta_galloway_1956]
- [Pilcher 2021][research_pilcher_2021]
- [Pinker 2024][research_pinker_2024]
- [Pioneering woman test pilot receives outstanding leadership 2001][research_pioneering_woman_2001]
- [Pitkin 1968][research_pitkin_1968]
- [Pitts et al 1974][research_pitts_1974]
- [Pivko 1956][research_pivko_1956]
- [Pla et al 1989][research_pla_1989]
- [Place et al 1974][research_place_1974]
- [Platt and Shortal 1937][research_platt_shortal_1937]
- [PlCKERELL and Cresswell 1968][research_plckerell_cresswell_1968]
- [Pleban and Beal 2002][research_pleban_beal_2002]
- [Plotkin and Shepherd 2006][research_plotkin_shepherd_2006]
- [Plucinsky 1973][research_plucinsky_1973]
- [Plunkett 1949][research_plunkett_1949]
- [Poe and Arthur C. 1974][research_poe_arthur_c_1974]
- [Pogosyan and Moshkov 2023][research_pogosyan_moshkov_2023]
- [Polacsek et al 2000][research_polacsek_spiegel_2000]
- [Polhamus and King 1949][research_polhamus_king_1949]
- [Polly 1969][research_polly_1969]
- [Pope et al 1987][research_pope_1987]
- [Pope et al 1987][research_pope_1987_2]
- [Pornet and Isikveren 2015][research_pornet_isikveren_2015]
- [Portapas and Cooke 2020][research_portapas_cooke_2020]
- [Portnoy 1976][research_portnoy_1976]
- [Portnoy 1977][research_portnoy_1977]
- [Posey 2008][research_posey_2008]
- [Posingies 1968][research_posingies_1968]
- [Pott-Pollenske 2021][research_pottpollenske_2021]
- [Povinelli 2002][research_povinelli_2002]
- [Powell-Dunford et al 2016][research_powell_dunford_2016]
- [Power 1963][research_power_1963]
- [Powers and Sarrafian 1986][research_powers_sarrafian_1986]
- [Poznanski et al 2025][research_poznanski_mays_2025]
- [Prasad and Crocker 1983][research_prasad_crocker_1983]
- [Prasannakumar et al 2024][research_prasannakumar_2024]
- [Price 1943][research_price_1943]
- [Price and Hodge 1976][research_price_hodge_1976]
- [Pridmore-Brown 1962][research_pridmore_brown_1962]
- [Primatesta et al 2019][research_primatesta_2019]
- [Probst et al 2017][research_probst_2017]
- [Propeller Performance 2012][research_propeller_performance_2012]
- [Propeller Propulsion Systems 2010][research_propeller_propulsion_2010]
- [Propeller system for Bush Hawk utility aircraft 1999][research_propeller_system_1999]
- [Przedpelski 1965][research_przedpelski_1965]
- [Pugh 1972][research_pugh_1972]
- [Purser 1941][research_purser_1941]
- [Pusch et al 2019][research_pusch_2019]
- [Pushtaev 1989][research_pushtaev_1989]
- [Putman 1969][research_putman_1969]
- [Putnam 1975][research_putnam_1975]
- [Puttur and Layng 2025][research_puttur_layng_2025]
- [Pyo 1995][research_pyo_1995]
- [Pöysä et al 2018][research_poysa_2018]
- [Qi and Zhao 2020][research_qi_zhao_2020]
- [Qi et al 2018][research_qi_2018]
- [Qian 2026][research_qian_2026]
- [Qian et al 2022][research_qian_2022]
- [Qiang and Wang 2025][research_qiang_wang_2025]
- [Qiao et al 2018][research_qiao_2018]
- [Qiao et al 2025][research_qiao_2025]
- [Qin and Huang 2024][research_qin_huang_2024]
- [Qin et al 2014][research_qin_wang_2014]
- [Qin et al 2023][research_qin_2023]
- [QinetiQ welcomes a new chief test pilot to MOD Boscombe Down 2002][research_qinetiq_welcomes_2002]
- [Qiu and Ang 2019][research_qiu_ang_2019]
- [Qu and Li 2022][research_qu_li_2022]
- [Qu et al 2017][research_qu_2017]
- [Quagliarella and Iuliano 2017][research_quagliarella_iuliano_2017]
- [Quanyan 2021][research_quanyan_2021]
- [Quaranta and Dimino 2007][research_quaranta_dimino_2007]
- [Quaroni et al 2024][research_quaroni_merinomartinez_2024]
- [Queen and Cochrane 1982][research_queen_cochrane_1982]
- [Quick 1937][research_quick_1937]
- [Quillet et al 2023][research_quillet_2023]
- [Quinn 1963][research_quinn_1963]
- [Quinn and Breidenbach 1978][research_quinn_breidenbach_1978]
- [Quinn et al 2025][research_quinn_2025]
- [Quirion and Liu 2020][research_quirion_liu_2020]
- [R. 1935][research_r_1935]
- [Rader 1989][research_rader_1989]
- [Radetskaya 2022][research_radetskaya_2022]
- [Raffel et al 2019][research_raffel_2019]
- [Ragani Lamouki et al 2026][research_ragani_lamouki_2026]
- [Raisbeck and Mills 1987][research_raisbeck_mills_1987]
- [Rajeswari and Padma Suresh 2015][research_rajeswari_padma_suresh_2015]
- [Rakesh and Reddy 2023][research_rakesh_reddy_2023]
- [Ralles 1966][research_ralles_1966]
- [Ramachandra 1979][research_ramachandra_1979]
- [Ramšak 2012][research_ramsak_2012]
- [Ranaudo et al 2000][research_ranaudo_2000]
- [Rand et al 2004][research_rand_khromov_2004]
- [Randall 1955][research_randall_1955]
- [Raney 1975][research_raney_1975]
- [Raney and Batterson 1989][research_raney_batterson_1989]
- [Range et al 2013][research_range_werner_2013]
- [Rankine and Leondes 1972][research_rankine_leondes_1972]
- [Rao 1992][research_rao_1992]
- [Rao et al 1987][research_rao_1987]
- [Rao et al 2023][research_rao_2023]
- [Rao Pittu et al 2023][research_rao_pittu_2023]
- [Rasband et al 2023][research_rasband_2023]
- [Rasmussen 1986][research_rasmussen_1986]
- [Rasmussen 1990][research_rasmussen_1990]
- [Raspet 1952][research_raspet_1952]
- [Raspet 1955][research_raspet_1955]
- [Rathgeber and Sipes 1977][research_rathgeber_sipes_1977]
- [Ratvasky et al 2003][research_ratvasky_blankenship_2003]
- [Ratvasky et al 2010][research_ratvasky_barnhart_2010]
- [Ravetta et al 2019][research_ravetta_2019]
- [Raw and Griffiths 1985][research_raw_griffiths_1985]
- [Rawson 1963][research_rawson_1963]
- [Ray et al 1988][research_ray_1988]
- [Raymer 2004][research_raymer_2004]
- [Raza and Stansbury 2025][research_raza_stansbury_2025]
- [Reader 1976][research_reader_1976]
- [Reader 1980][research_reader_1980]
- [Rebont et al 1977][research_rebont_1977]
- [Reconnaissance and Auxiliary Aircraft 2008][research_reconnaissance_and_2008]
- [Reddingius 1974][research_reddingius_1974]
- [Reddingius 1977][research_reddingius_1977]
- [Rediess and Melton 1994][research_rediess_melton_1994]
- [Reduced Noise in Interiors of Propfan Aircraft 1988][research_reduced_noise_1988]
- [Reed 1941][research_reed_1941]
- [Reed 1966][research_reed_1966]
- [Reeder 1958][research_reeder_1958]
- [Reeder 1959][research_reeder_1959]
- [Regier and Hubbard 1953][research_regier_hubbard_1953]
- [Rehm and Jansen 1978][research_rehm_jansen_1978]
- [Rehman 2022][research_rehman_2022]
- [Reid 1978][research_reid_1978]
- [Reid et al 2024][research_reid_2024]
- [Reilly 1970][research_reilly_1970]
- [Reiquam 1982][research_reiquam_1982]
- [Reising et al 1996][research_reising_1996]
- [Render and Jenkinson 1996][research_render_jenkinson_1996]
- [Rennison et al 1980][research_rennison_wilby_1980]
- [Report No. 297. The reduction of observed airplane performance to standard conditions 1929][research_report_no_1929]
- [Report No. 408. General 1932, Report No. 408. General Formulas][research_report_no_1932_4]
- [Report No. 423, Wind-tunnel 1932, Report No. 423, Wind-tunnel][research_report_no_1932_3]
- [Report No. 434. Lift 1932, Report No. 434. Lift and drag][research_report_no_1932_5]
- [Report No. 439, Wind-Tunnel 1932, Report No. 439, Wind-Tunnel][research_report_no_1932_2]
- [Report No. 444, Wind-Tunnel 1932, Report No. 444, Wind-Tunnel][research_report_no_1932]
- [Report no. 485, The 1935, Report no. 485, The drag of][research_report_no_1935_2]
- [Report no. 510, wind-tunnel 1935, Report no. 510, wind-tunnel][research_report_no_1935]
- [Research on control takeover techniques for counter-UAV (Unmanned Aircraft Vehicle) 2025][research_research_on_2025]
- [Reussner 1950][research_reussner_1950]
- [Reussner 1953][research_reussner_1953]
- [Reuter 1939][research_reuter_1939]
- [Revell et al 1980][research_revell_balena_1980]
- [Revell et al 1980][research_revell_balena_1980_b]
- [Revell et al 1982][research_revell_1982]
- [Revell et al 1982][research_revell_1982_2]
- [Rexcharles Enyinna Donatus et al 2026][research_rexcharles_enyinna_donatus_2026]
- [Rey et al 2021][research_rey_2021]
- [Reynolds 1963][research_reynolds_1963]
- [Reynolds et al 2018][research_reynolds_2018]
- [Rezy et al 1979][research_rezy_stuckas_1979]
- [Rhoads 1952][research_rhoads_1952]
- [Rhoads 1967][research_rhoads_1967]
- [Rhoads 1970][research_rhoads_1970]
- [Rhodes 1982][research_rhodes_1982]
- [Rhudy et al 2023][research_rhudy_2023]
- [Riboldi 2018][research_riboldi_2018]
- [Riboldi 2019][research_riboldi_2019]
- [Riccardi et al 2025][research_riccardi_mamino_2025]
- [Rice 1946][research_rice_1946]
- [Rice and Hazlwood 1994][research_rice_hazlwood_1994]
- [Rice and Oetting 1976][research_rice_oetting_1976]
- [Richards and Attenborough 1986][research_richards_attenborough_1986]
- [Richardson 1976][research_richardson_1976]
- [Riddle et al 1981][research_riddle_innis_1981]
- [Riddle et al 1987][research_riddle_stevens_1987]
- [Ride quality of crew-manned military aircraft 1975][research_ride_quality_1975]
- [Rieck et al 2026][research_rieck_2026]
- [Riggins and Camberos 2020][research_riggins_camberos_2020]
- [Ringland and Craig 1977][research_ringland_craig_1977]
- [Rittenhouse 1959][research_rittenhouse_1959]
- [Rizzi and Rafaelof 2021][research_rizzi_rafaelof_2021]
- [Rizzi and Scata 2022][research_rizzi_scata_jr_2022]
- [Rizzi et al 2016][research_rizzi_2016]
- [Rizzi et al 2017][research_rizzi_christian_2017]
- [Rizzi et al 2024][research_rizzi_2024]
- [Robb et al][research_caleb_robb]
- [Robert C Platt 1935][research_robert_c_platt_1935]
- [Robert E Lee 2005][research_robert_e_lee_2005]
- [Roberts 1963][research_roberts_1963]
- [Roberts 1964][research_roberts_1964]
- [Roberts 1988][research_roberts_1988]
- [Roberts 1988][research_roberts_1988_b]
- [Roberts and Brown 1988][research_roberts_brown_1988]
- [Roberts and Shawler 1994][research_roberts_shawler_1994]
- [Robinson 1979][research_robinson_1979]
- [Rockefeller 1937][research_rockefeller_1937]
- [Rocket Effect in Standard Airplane Performance 1937][research_rocket_effect_1937]
- [Rodden 1956][research_rodden_1956]
- [Rodden 1989][research_rodden_1989]
- [Rodden and Giesing 1970][research_rodden_giesing_1970]
- [Rodenhiser et al 2007][research_rodenhiser_durgin_2007]
- [Rodger Dyson][research_rodger_dyson]
- [Rodgers 1966][research_rodgers_1966]
- [Rodriguez et al][research_gabino_martinez_rodriguez]
- [Rogalski 2018][research_rogalski_2018]
- [Roger et al 2022][research_roger_2022]
- [Rogers 2004][research_rogers_2004]
- [Rogers and Cook 1952][research_rogers_cook_1952]
- [Rogers and Fasciano 2016][research_rogers_fasciano_2016]
- [Rohling 1969][research_rohling_1969]
- [Rokhsaz and Kliment 2017][research_rokhsaz_kliment_2017]
- [Romadhon et al 2024][research_romadhon_2024]
- [Roncen 2025][research_roncen_2025]
- [Roos 1985][research_roos_1985]
- [Rosales et al 2021][research_rosales_guijarroreyes_2021]
- [Rose and Jeracki 1989][research_rose_jeracki_1989]
- [Rosenberg 1944][research_rosenberg_1944]
- [Roskam and Dusto 1969][research_roskam_dusto_1969]
- [Roskam et al 1968][research_roskam_1968]
- [Ross 1984][research_ross_1984]
- [Rossow 1986][research_rossow_1986]
- [Rostami 2024][research_rostami_2024]
- [Rotorcraft handling qualities design 2011][research_rotorcraft_handling_2011]
- [Roudbari and Saghafi 2016][research_roudbari_saghafi_2016]
- [Roxner and Postolsky 2024][research_roxner_postolsky_2024]
- [Roy 2009][research_roy_2009]
- [Ruffini et al 2020][research_ruffini_2020]
- [Ruijgrok 1980][research_ruijgrok_1980]
- [Ruijgrok 1983][research_ruijgrok_1983]
- [Runyan 1980][research_runyan_1980]
- [Runyan et al 1952][research_runyan_1952]
- [Ruotolo 1999][research_ruotolo_1999]
- [Rusakov and Krupetskyh 2012][research_rusakov_krupetskyh_2012]
- [Rusciano and Viscardi 2008][research_rusciano_viscardi_2008]
- [Rutherford and Crowder 1958][research_rutherford_crowder_1958]
- [Ryan Aeronautical Co San Diego Ca 1963][research_ryan_aeronautical_co_san_diego_ca_1963]
- [Ryan and Cummings 2016][research_ryan_cummings_2016]
- [Ryan et al 2022][research_ryan_2022]
- [Rydin et al 2018][research_rydin_2018]
- [Ryffel et al 2019][research_ryffel_2019]
- [Ryu et al 2022][research_ryu_2022]
- [Saari and Wallner 1946][research_saari_wallner_1946]
- [Saastamoinen and Maunula 2021][research_saastamoinen_maunula_2021]
- [Sabatini et al 2015][research_sabatini_2015]
- [Sabatini et al 2026][research_sabatini_2026]
- [Sabine and Burkhard 1959][research_sabine_burkhard_1959]
- [Sachs 2016][research_sachs_2016]
- [Sachs and da Costa 2003][research_sachs_dacosta_2003]
- [Sachs and Grüter 2017][research_sachs_gruter_2017]
- [Sachs and Moelyadi 2006][research_sachs_moelyadi_2006]
- [Sachs et al 2013][research_sachs_lenz_2013]
- [Saetti and Rogers 2020][research_saetti_rogers_2020]
- [Sagan et al 2025][research_sagan_lau_2025]
- [Sahai et al 2016][research_sahai_wefers_2016]
- [Sahai et al 2017][research_sahai_2017]
- [Sahawneh et al 2015][research_sahawneh_2015]
- [Sahithi 2023][research_sahithi_2023]
- [Sahyoun et al 2026][research_sahyoun_2026]
- [Sakaliyski et al 2007][research_sakaliyski_hileman_2007]
- [Sakamoto and Cota 1965][research_sakamoto_cota_1965]
- [Sakamoto et al 2007][research_sakamoto_takemura_2007]
- [Sakthivel and Venkatesan 2017][research_sakthivel_venkatesan_2017]
- [Salikuddin 1990][research_salikuddin_1990_2]
- [Salikuddin and Ahuja 1989][research_salikuddin_ahuja_1989]
- [Salikuddin et al 1990][research_salikuddin_1990]
- [Saltari et al 2017][research_saltari_2017]
- [Salucci et al 2026][research_salucci_2026]
- [Samimy et al 2003][research_samimy_2003]
- [Samimy et al 2004][research_samimy_2004]
- [Sampaio et al 2014][research_sampaio_hernandes_2014]
- [Sanchez-Galan et al 2025][research_sanchez_galan_2025]
- [Sanders 1957][research_sanders_1957]
- [Sandlin and Saiki 1993][research_sandlin_saiki_1993]
- [Sandstrom and White 1961][research_sandstrom_white_1961]
- [Sandu et al 2025][research_sandu_2025]
- [Sanghi et al 2024][research_sanghi_2024]
- [Sankar and Brentner 2008][research_sankar_brentner_2008]
- [Santos et al 2023][research_santos_2023]
- [Santos et al 2025][research_h_t_santos_2025]
- [Santoso and Hariyanto 2022][research_santoso_hariyanto_2022]
- [Sanz 1986][research_sanz_1986]
- [Saravo 1976][research_saravo_1976]
- [Saraçyakupoğlu et al 2022][research_saracyakupoglu_2022]
- [Sarup 2025][research_sarup_2025]
- [Sarup 2026][research_sarup_2026]
- [Sasaki et al 2012][research_sasaki_torise_2012]
- [Sathish Kumar Sunnam et al. 2019][research_sathish_kumar_sunnam_et_al_2019]
- [Satria Palar et al 2024][research_satria_palar_2024]
- [Satuluri and Seeni 2022][research_satuluri_seeni_2022]
- [Saucez][research_saucez]
- [Savory and Toy 1984][research_savory_toy_1984]
- [Sawake 2026][research_sawake_2026]
- [Sawyer 1967][research_sawyer_1967]
- [Scanlan 1948][research_scanlan_1948]
- [Schade and Crane 1965][research_schade_crane_1965]
- [Schade et al 1952][research_schade_1952]
- [Schaeffer and Sternfeld 1978][research_schaeffer_sternfeld_1978]
- [Schaffer et al 2023][research_schaffer_bertsch_2023_b]
- [Schairer 1937][research_schairer_1937]
- [Schairer et al 1971][research_schairer_1971]
- [Scharine and Letowski 2013][research_scharine_letowski_2013]
- [Schauerhamer and Robinson 2017][research_schauerhamer_robinson_2017]
- [Scherrer and Dennis 1951][research_scherrer_dennis_1951]
- [Schieni et al 2024][research_schieni_2024]
- [Schlinker 1979][research_schlinker_1979]
- [Schneiter and Watson 1948][research_schneiter_watson_1948]
- [Schnulo et al][research_sydney_schnulo]
- [Schofield 1984][research_schofield_1984]
- [Schollenberger et al 2025][research_schollenberger_2025]
- [Scholz 2021][research_scholz_2021]
- [Schomer et al 1991][research_schomer_1991]
- [Schreadley 1977][research_schreadley_1977]
- [Schreckenberg et al 2023][research_schreckenberg_2023]
- [Schreder 1975][research_schreder_1975]
- [Schrenk 1932][research_schrenk_1932]
- [Schriever 1952][research_schriever_1952]
- [Schuet et al 2017][research_schuet_2017]
- [Schulderfrei et al 1951][research_schulderfrei_1951]
- [Schumacher 1952][research_schumacher_1952]
- [Schutz and Kutrzyba 2000][research_schutz_kutrzyba_2000]
- [Schwab and Zellmann 2020][research_schwab_zellmann_2020]
- [Schwartz 1976][research_schwartz_1976]
- [Schwartz and Wray 1969][research_schwartz_wray_1969]
- [Schwartz et al 1986][research_schwartz_1986]
- [Schy and Hannah 1977][research_schy_hannah_1977]
- [Schäffer et al 2023][research_schaffer_bertsch_2023]
- [Schütte and Hummel 2023][research_schutte_hummel_2023]
- [Scientific and Technical Aspects of Soaring Flight 1952][research_scientific_and_1952]
- [Scoppe 1973][research_scoppe_1973]
- [Scordamaglia et al 2025][research_scordamaglia_2025]
- [Seacord and Teitelbaum 1947][research_seacord_teitelbaum_1947]
- [Sears 1948][research_sears_1948]
- [Sears 1974][research_sears_1974]
- [Sears 1990][research_sears_1990]
- [Secco and Martins 2019][research_secco_martins_2019]
- [Seckel and Graziani 1956][research_seckel_graziani_1956]
- [Secretary Of The Air Force Washington Dc 2001][research_secretaryoftheairforcewashingtondc_2001]
- [Sedunov et al 2018][research_sedunov_2018]
- [Sedunov et al 2019][research_sedunov_2019]
- [Segall and Gardner 2026][research_segall_gardner_2026]
- [Seginer and Salomon 1983][research_seginer_salomon_1983]
- [Seidaliyeva et al 2023][research_seidaliyeva_2023]
- [Sekaran 1983][research_sekaran_1983]
- [Sells and Crossley 2023][research_sells_crossley_2023]
- [Semrau et al 1974][research_semrau_1974]
- [Sen et al 1987][research_sen_1987]
- [Serra and Branco 2026][research_serra_branco_2026]
- [Sesham et al 2026][research_sesham_2026]
- [Setiawan et al 2026][research_setiawan_2026]
- [Seville Research Corp Pensacola Fl 1979][research_seville_research_corp_pensacola_fl_1979]
- [Shafer 1991][research_shafer_1991]
- [Shafer 1992][research_shafer_1992]
- [Shahady 1975][research_shahady_1975]
- [Shaikn 1979][research_shaikn_1979]
- [Shan et al 2025][research_shan_2025]
- [Shang 2007][research_shang_2007]
- [Shang et al 2025][research_shang_2025]
- [Shankar 1972][research_shankar_1972]
- [Shankar and Yathisha 2023][research_shankar_l_2023]
- [Shannon and Wang 1973][research_shannon_wang_1973]
- [Shao et al 2025][research_shao_2025]
- [Shao et al 2026][research_shao_2026]
- [Shapiro and Sherman Edwards 1967][research_shapiro_sherman_edwards_1967]
- [Sharma 2016][research_sharma_2016]
- [Shaw et al 1988][research_shaw_1988]
- [Shayak et al 2024][research_shayak_2024]
- [Shearwood et al 2020][research_shearwood_2020]
- [Sheffield 2000][research_sheffield_2000]
- [Shelley 2018][research_shelley_2018]
- [Shen et al 2021][research_shen_2021]
- [Shenstone 1938][research_shenstone_1938]
- [Shenstone 1946][research_shenstone_1946]
- [Shenstone 1953][research_shenstone_1953]
- [Shi and Wan 2015][research_shi_wan_2015]
- [Shi et al 2023][research_shi_2023]
- [Shi et al 2023][research_shi_2023_2]
- [Shi et al 2024][research_shi_2024]
- [Shields and Bass 1977][research_shields_bass_1977]
- [Shimoyama and Kamisori 2017][research_shimoyama_kamisori_2017]
- [Shin et al 2018][research_shin_2018]
- [Shindo and Joppa 1980][research_shindo_joppa_1980]
- [Shirbhate et al 2025][research_shirbhate_2025]
- [Shivashankara 1978][research_shivashankara_1978]
- [Shivashankara 1983][research_shivashankara_1983]
- [Shivashankara and Stubbs 1987][research_shivashankara_stubbs_1987]
- [Shmelоv et al 2019][research_shmelv_vladov_2019]
- [Shmilovich and Princen 2026][research_shmilovich_princen_2026]
- [Shmilovich et al 2023][research_shmilovich_yadlin_2023]
- [Shmilovich et al 2026][research_shmilovich_2026]
- [Shomber and Gertsen 1967][research_shomber_gertsen_1967]
- [Shortal 1934][research_shortal_1934]
- [Shovlin et al 1979][research_shovlin_1979]
- [Showers 1952][research_showers_1952]
- [Shreve 1977][research_shreve_1977]
- [Shrey. J. Mistry et al. 2018][research_shrey_j_mistry_et_al_2018]
- [Shrivastava and Stengel 1989][research_shrivastava_stengel_1989]
- [Shubert and Jones 2025][research_shubert_jones_2025]
- [Si et al 2023][research_si_2023]
- [Sibert 1943][research_sibert_1943]
- [Sibert 1947][research_sibert_1947]
- [Siddavatam et al 2024][research_siddavatam_2024]
- [Siddiqui et al 2023][research_siddiqui_2023]
- [Sidhu 2023][research_sidhu_2023]
- [Siegel and Crain 1960][research_siegel_crain_1960]
- [Siegel and Lanterman 1963][research_siegel_lanterman_1963]
- [Sikora and Mendenhall 1974][research_sikora_mendenhall_1974]
- [Silvestre 2013][research_silvestre_2013]
- [Silvestre and Luckner 2015][research_silvestre_luckner_2015]
- [Sim 1990][research_sim_1990]
- [Sim and Curry 1978][research_sim_curry_1978]
- [Sim and Curry 1985][research_sim_curry_1985]
- [Simcox et al 1976][research_simcox_1976]
- [Simizu 1944][research_simizu_1944]
- [Simmonds 1967][research_simmonds_1967]
- [Simmonds 1967][research_simmonds_1967_2]
- [Simmonds 1967][research_simmonds_1967_3]
- [Simmons 2023][research_simmons_2023]
- [Simmons et al][research_benjamin_m_simmons]
- [Simmons et al 2019][research_simmons_2019]
- [Simmons et al 2023][research_simmons_2023_2]
- [Simmons et al 2023][research_simmons_2023_3]
- [Simmons et al 2023][research_simmons_2023_4]
- [Simon et al 2023][research_simon_2023]
- [Simpson 1979][research_simpson_1979]
- [Simpson 1990][research_simpson_1990]
- [Sims and Kimberlin 1995][research_sims_kimberlin_1995]
- [Simson 2024][research_simson_2024]
- [Simulation in support of flight test - In retrospect 1988][research_simulation_in_1988]
- [Sinacori and Lange 1961][research_sinacori_lange_1961]
- [Sinha and Ravande 2006][research_sinha_ravande_2006]
- [Sinkovec et al 2015][research_sinkovec_loshek_2015]
- [Siqueira et al 2025][research_siqueira_2025]
- [Sivells and Neely 1947][research_sivells_neely_1947]
- [Slater 1955][research_slater_1955]
- [Sleeman 1971][research_sleeman_1971]
- [SlEWERT and Stewart 1967][research_slewert_stewart_1967]
- [Sliwa and Sliwa 1979][research_sliwa_sliwa_1979]
- [Smaili et al 2018][research_smaili_2018]
- [Smith][research_smith]
- [Smith 1977][research_smith_1977]
- [Smith 1983][research_smith_1983]
- [Smith 2023][research_smith_2023]
- [Smith and Bernier 1966][research_smith_bernier_1966]
- [Smith and Geddes 1979][research_smith_geddes_1979]
- [Smith and Kroo 1990][research_smith_kroo_1990]
- [Snell 1993][research_snell_1993]
- [Snell et al 1991][research_snell_1991]
- [Snyder 1950][research_snyder_1950]
- [Snyder and Kohlman 2018][research_snyder_kohlman_2018]
- [Socha et al 2026][research_socha_2026]
- [Soderman 2006][research_soderman_2006]
- [Soderman and Noble 1975][research_soderman_noble_1975]
- [Sohail et al 2011][research_sohail_muhammad_2011]
- [Soinne 1999][research_soinne_1999]
- [Solies 1995][research_solies_1995]
- [Soltmann and Hall 2017][research_soltmann_hall_2017]
- [Somers 1977][research_somers_1977]
- [Somers 1981][research_somers_1981]
- [Somers and Foster 1979][research_somers_foster_1979]
- [Somerville et al 2025][research_somerville_2025]
- [Somerville et al 2026][research_somerville_2026]
- [Somerville et al 2026][research_somerville_2026_2]
- [Sommer and Tapscott 1966][research_sommer_tapscott_1966]
- [Somsel 1970][research_somsel_1970]
- [Son and Yee 2018][research_son_yee_2018]
- [Soneda et al 2019][research_soneda_2019]
- [Sonmez and Alemdaroglu 2015][research_sonmez_alemdaroglu_2015]
- [Soom and Gu 1981][research_soom_gu_1981]
- [Soovere 1982][research_soovere_1982]
- [Soovere 1985][research_soovere_1985]
- [Soule and Wetmore 1933][research_soule_wetmore_1933]
- [Source Noise Suppression of Subsonic Tip Speed Fans 1975][research_source_noise_1975]
- [Southerland et al 1986][research_southerland_platus_1986]
- [Spada et al 2017][research_spada_2017]
- [Spanò Cuomo and Guglieri 2021][research_spano_cuomo_guglieri_2021]
- [Sparks and Moerder 2002][research_sparks_moerder_2002]
- [Speakman et al 1978][research_speakman_1978]
- [Spearman and Webster 1951][research_spearman_webster_1951]
- [Spencer et al 1969][research_spencer_1969]
- [Sperry 1979][research_sperry_1979]
- [Sponder 1950][research_sponder_1950]
- [Sree 2015][research_sree_2015]
- [Srijayantha 1983][research_srijayantha_1983]
- [Srinathkumar 2015][research_srinathkumar_2015]
- [Srivastava 2016][research_srivastava_2016]
- [Staats et al 2025][research_staats_2025]
- [Stabeli Diehl et al 2025][research_stabeli_diehl_2025]
- [Stallings 1986][research_r_l_stallings_jr_1986]
- [Stallings and Hartman 1981][research_stallings_hartman_1981]
- [Stalnov et al 2022][research_stalnov_2022]
- [Stange 1959][research_stange_1959]
- [Starr et al 1975][research_starr_sernas_1975]
- [Steen 1994][research_steen_1994]
- [Steger and Bailey 1980][research_steger_bailey_1980]
- [Steiner and Pratt 1967][research_steiner_pratt_1967]
- [Stengel 1975][research_stengel_1975]
- [Stengel 1980][research_stengel_1980]
- [Stenzel 1947][research_stenzel_1947]
- [Stephens 2010][research_stephens_2010]
- [Stephens 2013][research_stephens_2013]
- [Stephenson et al 1990][research_stephenson_1990]
- [Stephenson et al 2019][research_stephenson_2019]
- [Stepniewski 1940][research_stepniewski_1940]
- [Sternfield 1954][research_sternfield_1954]
- [Stewart 1939][research_stewart_1939]
- [Stewart 2008][research_stewart_2008]
- [Stewart 2016][research_stewart_2016]
- [Stewart et al 2012][research_stewart_2012]
- [Stokes and Davis 1953][research_stokes_davis_1953]
- [Stoliker and Bosworth 1996][research_stoliker_bosworth_1996]
- [Stoll et al 2013][research_stoll_stilson_2013]
- [Stone 1945][research_stone_1945]
- [Stottier 1995][research_stottier_1995]
- [Stough et al 1987][research_stough_1987]
- [Strailman 1952][research_strailman_1952]
- [Stratford 1948][research_stratford_1948]
- [Strattan 1978][research_strattan_1978]
- [Strelkov and Kharlamov 1967][research_strelkov_kharlamov_1967]
- [Stresses in a rotating propeller blade 1938][research_stresses_in_1938]
- [Strier and Julian 1955][research_strier_1955]
- [Strike 1982][research_strike_w_t_1982]
- [Stuart 1943][research_stuart_1943]
- [Su et al 2025][research_su_2025]
- [Suarez et al 1993][research_suarez_1993]
- [Succi 1981][research_succi_1981]
- [Succi et al 1983][research_succi_1983]
- [Sudha et al 2018][research_sudha_2018]
- [Sudhakar et al 2025][research_s_2025_2]
- [Suit and Batterson 1986][research_suit_batterson_1986]
- [Suleman et al 2016][research_suleman_2016]
- [Sullivan and Clancy 1989][research_sullivan_clancy_1989]
- [Sun 2026][research_sun_2026]
- [Sun et al 2019][research_sun_2019]
- [Sun et al 2020][research_sun_2020]
- [Sun et al 2020][research_sun_2020_2]
- [Sun et al 2020][research_sun_2020_3]
- [Sun et al 2023][research_sun_2023_2]
- [Sunago et al 2009][research_sunago_sasaki_2009]
- [Surkova and Dolhoierova 2025][research_surkova_dolhoierova_2025]
- [Sutherland and Wesler 1990][research_sutherland_wesler_1990]
- [Suvarna et al 2022][research_suvarna_shukla_2022]
- [Suzuki and Kawamura 1995][research_suzuki_kawamura_1995]
- [Suzuki and Kawamura 1996][research_suzuki_kawamura_1996]
- [Svane and Plovsing 2024][research_svane_plovsing_2024]
- [Svatos et al 2021][research_svatos_2021]
- [Svendsen 1994][research_svendsen_1994]
- [Swaim 1969][research_swaim_1969]
- [Swaim 1970][research_swaim_1970]
- [Swaim 1971][research_swaim_1971]
- [Swaim and Connor 1968][research_swaim_connor_1968]
- [Swaim and Staab 1978][research_swaim_staab_1978]
- [Swaim and Yen 1979][research_swaim_yen_1979]
- [Swaminathan and Mohan 2018][research_swaminathan_mohan_2018]
- [Swarnkar and Kothari 2016][research_swarnkar_kothari_2016]
- [Swearingen 2006][research_swearingen_2006]
- [Swearingen and White 2020][research_swearingen_white_2020]
- [Szalai 1967][research_szalai_1967]
- [Szczyglowski et al 2019][research_szczyglowski_2019]
- [Sziroczak et al 2020][research_sziroczak_2020]
- [Sánchez et al 2024][research_sanchez_2024]
- [Sóbester 2021][research_sobester_2021]
- [Søntvedt 1974][research_sntvedt_1974]
- [Tabassum and Bai 2022][research_tabassum_bai_2022]
- [Tai 1993][research_tai_1993]
- [Tai et al 2023][research_tai_2023]
- [Tai et al 2023][research_tai_2023_2]
- [Tai et al 2024][research_tai_2024]
- [Tai et al 2025][research_tai_2025]
- [Takahashi et al 2023][research_takahashi_2023]
- [Takaishi et al 2023][research_takaishi_2023]
- [Takaishi et al 2024][research_takaishi_2024]
- [Takeda 1970][research_takeda_1970]
- [Takeya and Okumoto 1959][research_takeya_okumoto_1959]
- [Tam 1987][research_tam_1987]
- [Tam 2015][research_tam_2015]
- [Tan and Plotkin 1986][research_tan_plotkin_1986]
- [Tanaka et al 1985][research_tanaka_1985]
- [Tang et al 2016][research_tang_2016]
- [Tangler 1979][research_tangler_1979]
- [Tantaroudas and Karachalios 2026][research_tantaroudas_karachalios_2026]
- [Tapscott 1964][research_tapscott_1964]
- [Tarnopolsky 1978][research_tarnopolsky_1978]
- [Tarnow and Pommer 1988][research_tarnow_pommer_1988]
- [Tavella et al 1987][research_tavella_1987]
- [Tay et al 2025][research_tay_chong_2025]
- [Taylor 1984][research_taylor_1984]
- [Taylor 2011][research_taylor_2011]
- [Taylor and Miller 1982][research_taylor_miller_1982]
- [Taylor and Papadales 1976][research_taylor_papadales_1976]
- [Taylor et al 1973][research_taylor_1973]
- [Teixeira and Cesnik 2019][research_teixeira_cesnik_2019]
- [Teixeira and Cesnik 2020][research_teixeira_cesnik_2020]
- [Tenhave et al 2026][research_tenhave_2026]
- [Teper and Stapleford 1966][research_teper_stapleford_1966]
- [Terashima et al 2021][research_terashima_2021]
- [Terzakis et al 2025][research_terzakis_2025]
- [Tester 1973][research_tester_1973]
- [Tester 1973][research_tester_1973_2]
- [Tetlow 1983][research_tetlow_1983]
- [Thalheimer 2021][research_thalheimer_2021]
- [The Development of Aviation Training Syllabus Material 1948][research_the_development_1948]
- [The DRAG of a Sailplane 1999][research_the_drag_1999]
- [The inﬂuence of operational factors on aircraft noise levels 2011][research_the_influence_2011]
- [The main sources of aircraft noise 2011][research_the_main_2011]
- [The measurement and analysis of aircraft vibration 1976][research_the_measurement_1976]
- [The Pearson Rotary Aileron 1930][research_the_pearson_1930]
- [The Sailplane as a meteorological probe 1948][research_the_sailplane_1948]
- [The Sailplane in the Atmosphere 1999][research_the_sailplane_1999]
- [The Simplification of Lateral Control 1936][research_the_simplification_1936]
- [Thelander 1965][research_thelander_1965]
- [Theodorsen 1960][research_theodorsen_1960]
- [Theodorsen 1960][research_theodorsen_1960_2]
- [Theodorsen and Nomicos 1961][research_theodorsen_nomicos_1961]
- [Thinesh and Y Harmin 2018][research_c_y_harmin_2018]
- [Thirtyacre et al 2021][research_thirtyacre_2021]
- [Thomas 1961][research_thomas_1961]
- [Thomas 1961][research_thomas_1961_2]
- [Thomas 2003][research_thomas_2003]
- [Thomas and Hansman 2019][research_thomas_hansman_2019]
- [Thomas and Hansman 2020][research_thomas_hansman_2020]
- [Thomas and Hansman 2021][research_thomas_hansman_2021]
- [Thomas and Jones 1982][research_thomas_jones_1982]
- [Thomason et al 1967][research_thomason_1967]
- [Thompson 2014][research_thompson_2014]
- [Thomson 1946][research_thomson_1946]
- [Thomson 1983][research_thomson_1983]
- [Thorpe 1970][research_thorpe_1970]
- [Thorson and Bohne 1960][research_thorson_bohne_1960]
- [Thottathil Varghese et al 2022][research_thottathil_varghese_2022]
- [Timushev et al 2021][research_timushev_yakovlev_2021]
- [Tipton and Sparrow 2019][research_tipton_sparrow_2019]
- [Tittel 2010][research_tittel_2010]
- [Tobak and Schiff 1975][research_tobak_schiff_1975]
- [Toffol 2024][research_toffol_2024]
- [Tokashiki 2023][research_tokashiki_2023]
- [Tokugawa et al 2026][research_tokugawa_2026]
- [Toll 1943][research_toll_1943]
- [Tomaszewski and Goraj 2019][research_tomaszewski_goraj_2019]
- [Tombolato et al 2024][research_tombolato_2024]
- [Tong et al 2013][research_tong_hu_2013]
- [Tong et al 2023][research_tong_2023]
- [Torenbeek and Wittenberg 1983][research_torenbeek_wittenberg_1983]
- [Torija Martinez et al 2023][research_torija_martinez_2023]
- [Townsend 1966][research_townsend_1966]
- [Townsend and Phillips 1955][research_townsend_phillips_1955]
- [Townsend and Phillips 1956][research_townsend_phillips_1956]
- [Tracy 1981][research_tracy_1981]
- [Tracy et al 2002][research_tracy_sturdza_2002]
- [Tracy et al 2024][research_tracy_2024]
- [Trascinelli et al 2026][research_trascinelli_2026]
- [Traub 2016][research_traub_2016]
- [Traub 2016][research_traub_2016_b]
- [Traub 2017][research_traub_2017]
- [Traven and Whitley 1995][research_traven_whitley_1995]
- [Trethewey 1988][research_trethewey_1988]
- [Trevelyan and Blundell 1949][research_trevelyan_blundell_1949]
- [Trevino 1986][research_trevino_1986]
- [Trikootam and Hornikx 2019][research_trikootam_hornikx_2019]
- [Trillo 1966][research_trillo_1966]
- [Trinks and Haseborg 1982][research_trinks_haseborg_1982]
- [Tritschler and OConnor 2016][research_tritschler_oconnor_2016]
- [Troian et al 2017][research_troian_2017]
- [Trollip 1977][research_trollip_1977]
- [Truong et al 2024][research_truong_2024]
- [Tsatsas et al 2022][research_tsatsas_2022]
- [Tsoubanos 1979][research_tsoubanos_1979]
- [Tsouka 2024][research_tsouka_2024]
- [Tsuji 2024][research_tsuji_2024]
- [Tsutsumino et al 2025][research_tsutsumino_2025]
- [Tuck et al 2018][research_tuck_2018]
- [Tucker 1999][research_tucker_1999]
- [Turkdogru Gurun et al 2021][research_turkdogru_gurun_2021]
- [Turner 1942][research_turner_1942]
- [Turriziani 1979][research_turriziani_1979]
- [Tweeddale 1941][research_tweeddale_1941]
- [Tyler and Towle 1955][research_tyler_towle_1955]
- [Typical aircraft noise levels 1989][research_typical_aircraft_1989]
- [Uddin et al 2021][research_uddin_2021]
- [Uhl 2003][research_uhl_2003]
- [Ulry et al 1976][research_ulry_1976]
- [Ulvr et al 2026][research_ulvr_2026]
- [Underwood 1942][research_underwood_1942_2]
- [Underwood 1942, Aerodynamic Characteristics for][research_underwood_1942]
- [Unmanned and Uncontrolled The 2015][research_unmanned_and_2015]
- [Unruh 1980][research_unruh_1980]
- [Unruh 1981][research_unruh_1981]
- [Unruh 1987][research_unruh_1987]
- [Unruh 1988][research_unruh_1988]
- [Unruh 1988][research_unruh_1988_b]
- [Unruh 1989][research_unruh_1989]
- [Unruh et al 2002][research_unruh_2002]
- [Use of reinforced plastics in a composite propeller blade 1974][research_use_of_1974]
- [Usov et al 2026][research_usov_2026]
- [Uzun 2025][research_uzun_2025]
- [Vagianos and Rooney 1964][research_vagianos_rooney_1964]
- [Vaicaitis 1980][research_vaicaitis_1980]
- [Vaicaitis and Mixson 1985][research_vaicaitis_mixson_1985]
- [Valentine and Kader 1976][research_valentine_kader_1976]
- [Van Baelen et al 2020][research_van_baelen_2020]
- [Van Dam 1981][research_van_dam_1981]
- [Van Dam et al 1980][research_van_dam_1980]
- [van Dam et al 1981][research_van_dam_1981_2]
- [van Deventer 1979][research_vandeventer_1979]
- [Van Dommelen 1995][research_van_dommelen_1995]
- [Van et al 2019][research_van_2019]
- [Van Gaasbeek 1980][research_vangaasbeek_1980]
- [van Gool 1982][research_van_gool_1982]
- [Van Pelt 1981][research_vanpelt_1981]
- [van Rooyen and Eshelby 1981][research_van_rooyen_eshelby_1981]
- [Van Treuren and Wisniewski 2019][research_vantreuren_wisniewski_2019]
- [Van Wyckhouse 1966][research_vanwyckhouse_1966]
- [Vance 1991][research_vance_1991]
- [Vaughn and Lindsay 1988][research_vaughn_lindsay_1988]
- [Vaughn et al 2008][research_vaughn_miltone_2008]
- [Vaughn et al 2023][research_vaughn_2023]
- [Vecchiotti et al 2024][research_vecchiotti_2024]
- [Vechtel and Buch 2022][research_vechtel_buch_2022]
- [Vegh 2025][research_vegh_2025]
- [Veley et al 2008][research_veley_2008]
- [Velger and Shinar 1983][research_velger_shinar_1983]
- [Venkataraman and Seiler 2019][research_venkataraman_seiler_2019]
- [Venkataraman et al 2017][research_venkataraman_2017]
- [Venkataraman et al 2019][research_venkataraman_2019]
- [Venkatesh et al 2025][research_venkatesh_2025]
- [Vepa 2018][research_vepa_2018]
- [Vepa 2020][research_vepa_2020]
- [Verba et al 2024][research_verba_2024]
- [Versiani et al 2019][research_versiani_2019]
- [Vicory 1968][research_vicory_1968]
- [Vidan 2016][research_vidan_2016]
- [Vidović et al 2022][research_vidovic_2022]
- [Vilchis Medina et al 2018][research_vilchismedina_siegel_2018]
- [Vilchis Medina et al 2019][research_vilchismedina_siegel_2019]
- [Vile et al 2020][research_vile_2020]
- [Viswanathan 2018][research_viswanathan_2018]
- [Vitsas 2016][research_vitsas_2016]
- [Vlaskamp et al 2025][research_vlaskamp_2025]
- [Vlaskamp et al 2026][research_vlaskamp_2026]
- [Vlaskamp et al 2026][research_vlaskamp_2026_2]
- [Vlasov and Ovdienko 2020][research_vlasov_ovdienko_2020]
- [Vollo and Brassaw 1956][research_vollo_brassaw_1956]
- [Vomaske et al 1961][research_vomaske_1961]
- [von Kármán and Tsien 1945][research_von_karman_tsien_1945]
- [Voß and Ohme 2018][research_voss_ohme_2018]
- [Vránics 2020][research_vranics_2020]
- [Vulkan and Hyde 1981][research_vulkan_hyde_1981]
- [Waddington et al 2023][research_waddington_2023]
- [Wagdi 1977][research_wagdi_1977]
- [Wahler et al 2025][research_wahler_2025]
- [Wahler et al 2025][research_wahler_2025_2]
- [Walchner 1969][research_walchner_1969_2]
- [Walchner et al 1969][research_walchner_1969]
- [Walker 2015][research_walker_2015]
- [Walker 2024][research_walker_2024]
- [Walker et al 2016][research_walker_2016]
- [Wall and Meyer 2020][research_wall_meyer_2020]
- [Wallace 1952][research_wallace_1952]
- [Wallace and Vance 2019][research_wallace_vance_2019]
- [Wallner and Sorin 1946][research_wallner_sorin_1946]
- [Walsh 1993][research_walsh_1993]
- [Walter et al 2022][research_walter_2022]
- [Walz 1976][research_walz_1976]
- [Walz 1978][research_walz_1978]
- [Wan et al 2019][research_wan_2019]
- [Wang 1980][research_wang_1980]
- [Wang 1981][research_wang_1981]
- [Wang 2019][research_wang_2019]
- [Wang 2024][research_wang_2024_7]
- [Wang 2026][research_wang_2026]
- [Wang and Antesberger 2024][research_wang_antesberger_2024]
- [Wang and Chen 2024][research_wang_chen_2024]
- [Wang and Crocker 1983][research_wang_crocker_1983]
- [Wang and Li 2019][research_wang_li_2019]
- [Wang and Qin 2024][research_wang_qin_2024]
- [Wang and Zhang 2020][research_wang_zhang_2020]
- [Wang and Zhong 2025][research_wang_zhong_2025]
- [Wang et al 2013][research_wang_qin_2013]
- [Wang et al 2015][research_wang_2015]
- [Wang et al 2015][research_wang_2015_2]
- [Wang et al 2019][research_wang_2019_2]
- [Wang et al 2019][research_wang_2019_4]
- [Wang et al 2020][research_wang_2020_3]
- [Wang et al 2021][research_wang_wu_2021]
- [Wang et al 2022][research_wang_2022]
- [Wang et al 2022][research_wang_2022_2]
- [Wang et al 2022][research_wang_2022_3]
- [Wang et al 2022][research_wang_2022_4]
- [Wang et al 2022][research_wang_qin_2022]
- [Wang et al 2023][research_wang_2023]
- [Wang et al 2023][research_wang_2023_3]
- [Wang et al 2024][research_wang_2024]
- [Wang et al 2024][research_wang_2024_5]
- [Wang et al 2024][research_wang_2024_6]
- [Wang et al 2025][research_wang_2025]
- [Wang et al 2025][research_wang_2025_2]
- [Wang et al 2026][research_wang_2026_2]
- [Wang et al 2026][research_wang_2026_3]
- [Wanglomklang et al 2025][research_wanglomklang_2025]
- [Wanner 1973][research_wanner_1973]
- [Ward 1968][research_ward_1968]
- [Ward 1988][research_ward_1988]
- [Ward and Bennett 1974][research_ward_bennett_1974]
- [Warner 1993][research_warner_1993]
- [Washington et al 2017][research_washington_2017]
- [Watson 1982][research_watson_1982]
- [Watson et al 2020][research_watson_2020]
- [Watter 1930][research_watter_1930]
- [Watts 1976][research_watts_1976]
- [Webb and Willer 1952][research_webb_willer_1952]
- [Webster 1971][research_webster_1971]
- [Wei and Renliang 2015][research_wei_renliang_2015]
- [Wei et al 2017][research_wei_2017]
- [Wei et al 2020][research_wei_2020]
- [Wei et al 2022][research_wei_2022]
- [Wei et al 2022][research_wei_2022_2]
- [Weick and Harris 1933][research_weick_harris_1933]
- [Weick and Harris 1934][research_weick_harris_1934]
- [Weick and Jones 1937][research_weick_jones_1937]
- [Weick and Jones 1976][research_weick_jones_1976]
- [Weick and Noyes 1933][research_weick_noyes_1933]
- [Weick and Noyes 1933][research_weick_noyes_1933_2]
- [Weick and Shortal 1933][research_weick_shortal_1933]
- [Weick and Shortal 1935][research_weick_shortal_1935]
- [Weick and Wenzinger 1935][research_weick_wenzinger_1935]
- [Weiser and Ossmann 2022][research_weiser_ossmann_2022]
- [Weiser et al 2023][research_weiser_2023]
- [Weiss et al 1986][research_weiss_eterno_1986]
- [Weisshaar 1977][research_weisshaar_1977]
- [Weisshaar 1990][research_weisshaar_1990]
- [Welch 1995][research_welch_1995]
- [Welch et al 2026][research_welch_2026]
- [Wells 1977][research_wells_1977]
- [Wells et al 1982][research_wells_1982]
- [Wen et al 2023][research_wen_2023]
- [Wendt 1947][research_wendt_1947]
- [Weng et al 2021][research_weng_2021]
- [Wenzinger and Bamber 1938][research_wenzinger_bamber_1938]
- [Wenzinger and Rogallo 1941][research_wenzinger_rogallo_1941]
- [Weslet and Sutherland 1987][research_weslet_sutherland_1987]
- [Wesolek 2007][research_wesolek_2007]
- [West 1994][research_west_1994]
- [West et al 2015][research_west_2015]
- [Westin et al 2023][research_westin_2023]
- [Weston et al 2024][research_weston_2024]
- [Wheeler et al 2021][research_wheeler_2021]
- [Whitaker 1975][research_whitaker_1975]
- [Whitaker et al 1977][research_whitaker_1977]
- [Whitbeck and Hofmann 1978][research_whitbeck_hofmann_1978]
- [Whitcomb 1940][research_whitcomb_1940]
- [White 1963][research_white_1963]
- [White 1971][research_white_1971]
- [White 2025][research_white_2025]
- [White et al 2021][research_white_2021]
- [Whiting 1996][research_whiting_1996]
- [Whitmore and Merrill 2012][research_whitmore_merrill_2012]
- [Whittingham and Swan 1960][research_whittingham_swan_1960]
- [Whittley and Garland 1961][research_whittley_garland_1961]
- [Whoric 1973][research_whoric_1973]
- [Widger 1963][research_widger_1963]
- [Widnall and Wolf 1980][research_widnall_wolf_1980]
- [Wiggi 1949][research_wiggi_1949]
- [Wilby 1982][research_wilby_1982]
- [Wilby and Wilby 1989][research_wilby_wilby_1989]
- [Wilby et al 1980][research_wilby_rennison_1980]
- [Wild 1966][research_wild_1966]
- [Wiley 1954][research_wiley_1954]
- [Wiley and Taylor 1954][research_wiley_taylor_1954]
- [Wilhelm and Schafranek 1986][research_wilhelm_schafranek_1986]
- [Wilk 2024][research_wilk_2024]
- [Wilkerson 1975][research_wilkerson_1975]
- [Wilkinson 1954][research_wilkinson_1954]
- [Willebeek-LeMair and Rhinehart 2023][research_willebeeklemair_rhinehart_2023]
- [Williams 1940][research_williams_1940]
- [Williams 1974][research_williams_1974]
- [Williams 2002][research_williams_2002]
- [Williams and Howe 1970][research_williams_howe_1970]
- [Willis and Daniels 1981][research_willis_daniels_1981]
- [Willshire 1983][research_willshire_1983]
- [Willshire 1990][research_willshire_1990]
- [Willshire and Hilton 1979][research_willshire_hilton_1979]
- [Wilmott 1986][research_wilmott_1986]
- [Wilson 2024][research_wilson_2024]
- [Wilson 2025][research_wilson_2025]
- [Wilson Committee Report on Noise 1963][research_wilson_committee_1963]
- [Wilson et al 1993][research_wilson_1993]
- [Wilson et al 2016][research_wilson_2016]
- [Wilson et al 2021][research_wilson_2021]
- [Wilson et al 2022][research_wilson_2022]
- [Wind Tunnel Balance and Calibration Machine 1974][research_wind_tunnel_1974]
- [Wing Design Considerations 2021][research_wing_design_2021]
- [Wings and Winglets 1999][research_wings_and_1999]
- [Winn and Kishi 1972][research_winn_kishi_1972]
- [Winslow et al 2018][research_winslow_2018]
- [Winter 2023][research_winter_2023]
- [Winther et al 1981][research_winther_1981]
- [Woan and Gregorek 1978][research_woan_gregorek_1978]
- [Wokoun 1962][research_wokoun_1962]
- [Wolek et al 2016][research_wolek_2016]
- [Wolf and Raspet 1986][research_wolf_raspet_1986]
- [Wolowicz and Yancey 1973][research_wolowicz_yancey_1973]
- [Woo et al 2020][research_woo_2020]
- [Wood et al 2019][research_wood_2019]
- [Woods 1972][research_woods_1972]
- [Woodward 1987][research_woodward_1987]
- [Woodward 1987][research_woodward_1987_b]
- [Woodward and Loeffler 1991][research_woodward_loeffler_1991]
- [Wooley and Childs 1954][research_wooley_childs_1954]
- [Woolf 2012][research_woolf_2012]
- [Woolworth 2022][research_woolworth_2022]
- [Woolworth 2023][research_woolworth_2023]
- [Worobel and Peracchio 1968][research_worobel_peracchio_1968]
- [Wrestler and Clifton G. 1965][research_wrestler_clifton_g_1965]
- [Wright][research_stephen_j_wright]
- [Wright 1966][research_wright_1966]
- [Wright and Lee 1984][research_wright_lee_1984]
- [Wu 2010][research_wu_2010]
- [Wu and Mora-Camino 2012][research_wu_moracamino_2012]
- [Wu and Redonnet 2021][research_wu_redonnet_2021]
- [Wu and Talmadge 1961][research_wu_talmadge_1961]
- [Wu et al 2017][research_wu_2017_2]
- [Wu et al 2018][research_wu_2018]
- [Wu et al 2019][research_wu_2019]
- [Wu et al 2019][research_wu_2019_2]
- [Wu et al 2020][research_wu_2020]
- [Wu et al 2020][research_wu_2020_2]
- [Wu et al 2020][research_wu_2020_3]
- [Wu et al 2021][research_wu_2021_2]
- [Wu et al 2023][research_wu_2023]
- [Wu et al 2023][research_wu_2023_2]
- [Xiang and Jiang 2015][research_xiang_jiang_2015]
- [Xiao et al 2024][research_xiao_2024]
- [Xie and Haberland 1999][research_xie_haberland_1999]
- [Xie et al 2017][research_xie_2017]
- [Xie et al 2023][research_xie_2023]
- [Xie et al 2023][research_xie_2023_2]
- [Xie et al 2024][research_xie_2024]
- [Xieyuan 1985][research_xieyuan_1985]
- [Xiong et al 2025][research_xiong_2025]
- [Xiong et al 2026][research_xiong_2026]
- [Xu and Wang 2016][research_xu_wang_2016]
- [Xu et al 2015][research_xu_2015]
- [Xu et al 2020][research_xu_2020]
- [Xu et al 2025][research_xu_2025]
- [Xue and Haibin 2017][research_xue_haibin_2017]
- [Xue et al 2023][research_xue_2023]
- [Yager 1983][research_yager_1983]
- [Yamada 2023][research_yamada_2023]
- [Yamamoto et al 2023][research_yamamoto_2023]
- [Yamashita and Matsui 1978][research_yamashita_matsui_1978]
- [Yamin and Giyats 2022][research_yamin_giyats_2022]
- [Yan 2017][research_yan_2017]
- [Yan et al 2024][research_yan_2024]
- [Yan et al 2024][research_yan_tian_2024]
- [Yancey 1964][research_yancey_1964]
- [Yang][research_yang]
- [Yang and Gao 2020][research_yang_gao_2020]
- [Yang and Li 2022][research_yang_li_2022]
- [Yang et al 2016][research_yang_2016]
- [Yang et al 2017][research_yang_2017]
- [Yang et al 2019][research_yang_2019_2]
- [Yang et al 2023][research_yang_2023]
- [Yang et al 2026][research_yang_meinke_2026]
- [Yasue 2020][research_yasue_2020]
- [Yates 1949][research_yates_1949]
- [Yates 1974][research_yates_1974]
- [Yazdi 1991][research_yazdi_1991]
- [Yazgan and Kucuk Yilmaz 2018][research_yazgan_kucuk_yilmaz_2018]
- [Ye et al 2015][research_ye_2015]
- [Yeager et al 1997][research_yeager_1997]
- [Yegorov 1945][research_yegorov_1945]
- [Yeh and Plotkin 1986][research_yeh_plotkin_1986]
- [Yeo et al 2015][research_yeo_2015]
- [Yeong et al 2009][research_yeong_chiles_2009]
- [Yeow 1984][research_yeow_1984]
- [Yi et al 2025][research_yi_2025]
- [Yih et al 1952][research_yih_1952]
- [Yildiz 2022][research_yildiz_2022]
- [Yildiz et al 2019][research_yildiz_2019]
- [Yin and Stuermer 2013][research_yin_stuermer_2013]
- [Yin et al 2019][research_yin_2019]
- [Yin et al 2020][research_yin_2020]
- [Yip et al 1992][research_yip_1992]
- [Yokota et al 2023][research_yokota_2023]
- [Yokota et al 2025][research_yokota_2025]
- [Yongtao and Zhi 2014][research_yongtao_zhi_2014]
- [Yoon et al 2019][research_yoon_2019]
- [Yoshikawa 1992][research_yoshikawa_1992]
- [Yost 1976][research_yost_1976]
- [You 2020][research_you_2020]
- [You et al 2020][research_you_2020_2]
- [Yu 2011][research_yu_2011]
- [Yu 2018][research_yu_2018]
- [Yu 2026][research_yu_2026]
- [Yu and Ansell 2023][research_yu_ansell_2023]
- [Yu and Huang 2018][research_yu_huang_2018]
- [Yu et al 2020][research_yu_2020]
- [Yu et al 2023][research_yu_2023]
- [Yuan 2026][research_yuan_2026]
- [Yuan et al 2018][research_yuan_2018]
- [Yuan et al 2019][research_yuan_2019]
- [Yuan et al 2020][research_yuan_2020]
- [Yuan et al 2024][research_yuan_2024]
- [Yue et al 2025][research_yue_2025]
- [Yuen 2026][research_yuen_2026]
- [Yuma Proving Ground Az 2013][research_yuma_proving_ground_az_2013]
- [Yuma Test Center Yuma Proving Ground Az 2008][research_yuma_test_center_yuma_proving_ground_az_2008]
- [Yunus et al 2023][research_yunus_2023]
- [Yurttav et al 2025][research_yurttav_2025]
- [Yusuf et al 2022][research_yusuf_2022]
- [Zaal et al][research_peter_zaal]
- [Zaal et al 2015][research_zaal_2015]
- [Zabinsky and Laszewski 1956][research_zabinsky_laszewski_1956]
- [Zafirov 2020][research_zafirov_2020]
- [Zajdel et al 2022][research_zajdel_2022]
- [Zajdel et al 2024][research_zajdel_2024]
- [Zajdel et al 2024][research_zajdel_2024_2]
- [Zaman et al 2024][research_zaman_2024]
- [Zaporozhets and Jagniatinskis 2021][research_zaporozhets_jagniatinskis_2021]
- [Zaporozhets et al 2022][research_zaporozhets_2022]
- [Zawodny et al 2025][research_nikolas_s_zawodny_2025]
- [Zelenka et al 1995][research_zelenka_1995]
- [Zeller and Gary 2001][research_zeller_jr_2001]
- [Zellmann et al 2018][research_zellmann_2018]
- [Zhai et al 2024][research_zhai_2024]
- [Zhang 2024][research_zhang_2024]
- [Zhang 2026][research_zhang_2026_10]
- [Zhang 2026][research_zhang_2026_8]
- [Zhang and Liu 2026][research_zhang_liu_2026]
- [Zhang and Xia 2017][research_zhang_xia_2017]
- [Zhang and Zhao 2023][research_zhang_zhao_2023]
- [Zhang and Zhou 2024][research_zhang_zhou_2024]
- [Zhang et al][research_yang_zhang]
- [Zhang et al 2011][research_zhang_millane_2011]
- [Zhang et al 2013][research_zhang_yu_2013]
- [Zhang et al 2015][research_zhang_2015_2]
- [Zhang et al 2018][research_zhang_2018_2]
- [Zhang et al 2022][research_zhang_ma_2022]
- [Zhang et al 2023][research_zhang_2023_3]
- [Zhang et al 2023][research_zhang_2023_4]
- [Zhang et al 2023][research_zhang_2023_5]
- [Zhang et al 2023][research_zhang_2023_7]
- [Zhang et al 2025][research_zhang_2025]
- [Zhang et al 2025][research_zhang_2025_2]
- [Zhang et al 2025][research_zhang_2025_3]
- [Zhang et al 2026][research_zhang_2026_4]
- [Zhao 2025][research_zhao_2025]
- [Zhao and Gao 2019][research_zhao_gao_2019]
- [Zhao and Jim Zhu 2017][research_zhao_jim_zhu_2017]
- [Zhao et al 2023][research_zhao_2023_2]
- [Zhen 2019][research_zhen_2019]
- [Zheng 2021][research_zheng_2021]
- [Zheng et al 2018][research_zheng_2018]
- [Zheng et al 2019][research_zheng_2019]
- [Zheng et al 2023][research_zheng_2023]
- [Zheng et al 2026][research_zheng_2026]
- [Zhi et al 2025][research_zhi_2025]
- [Zhong et al 2019][research_zhong_2019]
- [Zhong et al 2023][research_zhong_2023]
- [Zhou 2022][research_zhou_2022]
- [Zhou and Wang 2026][research_zhou_wang_2026]
- [Zhou et al 2020][research_zhou_2020_2]
- [Zhu 2025][research_zhu_2025]
- [Zhu and Duan 2015][research_zhu_duan_2015]
- [Zhu et al 2016][research_zhu_2016]
- [Zhu et al 2023][research_zhu_2023]
- [Zhu et al 2023][research_zhu_2023_2]
- [Ziakos et al 2025][research_ziakos_2025]
- [Zikmund et al 2019][research_zikmund_2019]
- [Zilliac 2026][research_gregorygzilliac_2026]
- [Zohar and Er-El 1988][research_zohar_er_el_1988]
- [Zola et al 1978][research_zola_fishbach_1978]
- [Zong et al 2021][research_zong_2021]
- [Zorić 2024][research_zoric_2024]
- [Zorumski 1977][research_zorumski_1977]
- [Zorumski and Willshire 1989][research_zorumski_willshire_1989]
- [Zou et al 2021][research_zou_2021]
- [Zu et al 2017][research_zu_2017]
- [Zuhri 2025][research_zuhri_2025]
- [Ç. Altunkaya et al 2025][research_c_altunkaya_2025]
- [Çelebi et al 2025][research_celebi_2025]
- [Şenol 2020][research_senol_2020]
- [Šulc et al 1982][research_sulc_1982]
- [Żugaj 2017][research_zugaj_2017]
- [Дмитренко 2024][research__2024]
- [Драмшини 2022, Development of Algorithms of the][research__2022]
- [Жданов and Зінченко 2015][research___2015]
- [Задкова 2015, Pilots Errors Accounting and][research__2015]
- [Тsekhmistro and Shapovalov 2023][research_sekhmistro_shapovalov_2023]
- [李 2023][research__2023]

[research__2015]: https://doi.org/10.18372/2411-264x.7.10225
[research__2022]: https://doi.org/10.25791/aviakosmos.6.2022.1285
[research__2023]: https://doi.org/10.1360/ssi-2023-0130
[research__2024]: https://doi.org/10.36535/0235-5000-2024-04-4
[research___2015]: https://doi.org/10.20535/0203-377129201560714
[research_a_f_2018]: https://doi.org/10.1063/1.5032021
[research_a_harrah_lockenour_1971]: https://doi.org/10.2514/3.59105
[research_a_method_1936]: https://doi.org/10.1108/eb030030
[research_a_review_2011]: https://doi.org/10.1201/b12545-5
[research_a_sailplane_1974]: https://doi.org/10.2514/6.1974-258
[research_aalmoes_sieben_2021]: https://doi.org/10.3397/in-2021-2160
[research_abbott_2016]: https://doi.org/10.1121/1.4970051
[research_abdukayumov_2022]: https://doi.org/10.32743/unitech.2022.103.10.14410
[research_abdul_rashid_2025]: https://doi.org/10.15866/irease.v18i5.25896
[research_abdullina_efanov_2020]: https://doi.org/10.3103/s1068799820010043
[research_abhishek_prasad_2016]: https://doi.org/10.2514/1.c033707
[research_abich_iv_2016]: https://doi.org/10.1080/00140139.2016.1216171
[research_abichandani_rosenberg_1952]: https://doi.org/10.2514/8.2362
[research_abrahamson_1975]: https://ntrs.nasa.gov/citations/19750041732
[research_abramov_2019]: https://doi.org/10.2514/1.c034790
[research_abramson_1975]: https://doi.org/10.21236/ada027164
[research_abramson_1977]: https://doi.org/10.21236/ada055140
[research_abu_salem_2023]: https://doi.org/10.3390/en16237881
[research_abwanzo_2016]: https://doi.org/10.2139/ssrn.2861230
[research_abzug_daros_1955]: https://doi.org/10.21236/ada003615
[research_achleitner_rohdebrandenburger_2019]: https://doi.org/10.2514/6.2019-2816
[research_acoustic_field_2023]: https://doi.org/10.23977/jeis.2023.080209
[research_action_against_1989]: https://doi.org/10.1017/cbo9780511584527.003
[research_adams_1951]: https://ntrs.nasa.gov/citations/19930083072
[research_adams_1976]: https://ntrs.nasa.gov/citations/19770007090
[research_adams_hatch_1971]: https://doi.org/10.2514/3.59103
[research_adamson_1968]: https://doi.org/10.21236/ad0671029
[research_adamson_boatright_1950]: https://ntrs.nasa.gov/citations/20090021561
[research_addessio_skifstad_1975]: https://ntrs.nasa.gov/citations/19750022032
[research_adler_1960]: https://doi.org/10.21236/ad0266063
[research_adolph_1981]: https://doi.org/10.2514/6.1981-2487
[research_advisorygroupforaerospaceresearchanddevelopment_1984]: https://ntrs.nasa.gov/citations/19840026325
[research_aero_structural_2018]: https://doi.org/10.20474/jater-4.1.5
[research_aerodynamic_design_1986]: https://doi.org/10.2514/6.1986-2693
[research_afari_mankbadi_2024]: https://doi.org/10.3390/aerospace11060453
[research_afonso_2017]: https://doi.org/10.1017/aer.2017.29
[research_aguiar_2017]: https://doi.org/10.1016/j.aap.2017.03.017
[research_aguiar_cuevas_2017]: https://doi.org/10.15394/ijaa.2017.1176
[research_ahearn_headrick_1965]: https://doi.org/10.21236/ad0361253
[research_ahmadi_2024]: https://doi.org/10.1016/j.ast.2024.109023
[research_ahmadi_farsadi_2024]: https://doi.org/10.1016/j.ast.2023.108849
[research_ahmed_2024_2]: https://doi.org/10.9790/1684-2106013437
[research_ahuja_bushell_1973]: https://doi.org/10.1016/s0022-460x(73)80242-1
[research_air_force_flight_test_center_edwards_afb_ca_1970]: https://doi.org/10.21236/ada529707
[research_air_force_flight_test_center_edwards_afb_ca_1974]: https://doi.org/10.21236/ada011562
[research_air_force_flight_test_center_edwards_afb_ca_1974_2]: https://doi.org/10.21236/ada011561
[research_air_force_flight_test_center_edwards_afb_ca_1995]: https://doi.org/10.21236/ada402886
[research_air_force_flight_test_center_edwards_afb_ca_2002]: https://doi.org/10.21236/ada402888
[research_air_force_flight_test_center_edwards_afb_ca_2002_2]: https://doi.org/10.21236/ada403258
[research_air_force_test_pilot_school_edwards_afb_ca_1962]: https://doi.org/10.21236/ada320203
[research_air_force_test_pilot_school_edwards_afb_ca_1969]: https://doi.org/10.21236/ada319985
[research_air_force_test_pilot_school_edwards_afb_ca_1979]: https://doi.org/10.21236/ada320202
[research_air_force_test_pilot_school_edwards_afb_ca_1981]: https://doi.org/10.21236/ada320347
[research_air_force_test_pilot_school_edwards_afb_ca_1987]: https://doi.org/10.21236/ada320212
[research_air_force_test_pilot_school_edwards_afb_ca_1988]: https://doi.org/10.21236/ada319979
[research_air_force_test_pilot_school_edwards_afb_ca_1988_2]: https://doi.org/10.21236/ada319974
[research_air_force_test_pilot_school_edwards_afb_ca_1988_3]: https://doi.org/10.21236/ada319984
[research_air_force_test_pilot_school_edwards_afb_ca_1988_4]: https://doi.org/10.21236/ada319975
[research_air_force_test_pilot_school_edwards_afb_ca_1988_5]: https://doi.org/10.21236/ada319973
[research_air_force_test_pilot_school_edwards_afb_ca_1989]: https://doi.org/10.21236/ada319980
[research_air_force_test_pilot_school_edwards_afb_ca_1990]: https://doi.org/10.21236/ada320062
[research_air_force_test_pilot_school_edwards_afb_ca_1990_2]: https://doi.org/10.21236/ada320058
[research_air_force_test_pilot_school_edwards_afb_ca_1990_3]: https://doi.org/10.21236/ada319977
[research_air_force_test_pilot_school_edwards_afb_ca_1990_4]: https://doi.org/10.21236/ada319976
[research_air_force_test_pilot_school_edwards_afb_ca_1990_5]: https://doi.org/10.21236/ada319978
[research_air_force_test_pilot_school_edwards_afb_ca_1991]: https://doi.org/10.21236/ada319972
[research_air_force_test_pilot_school_edwards_afb_ca_1991_2]: https://doi.org/10.21236/ada319981
[research_air_force_test_pilot_school_edwards_afb_ca_1992]: https://doi.org/10.21236/ada319982
[research_air_force_test_pilot_school_edwards_afb_ca_1993]: https://doi.org/10.21236/ada320063
[research_air_force_test_pilot_school_edwards_afb_ca_1994]: https://doi.org/10.21236/ada320219
[research_air_force_test_pilot_school_edwards_afb_ca_1994_2]: https://doi.org/10.21236/ada320066
[research_air_proving_ground_center_eglin_afb_fl_1954]: https://doi.org/10.21236/adb193040
[research_air_proving_ground_center_eglin_afb_fl_1955]: https://doi.org/10.21236/ad0068388
[research_air_proving_ground_center_eglin_afb_fl_1955_2]: https://doi.org/10.21236/adb191132
[research_aircraft_and_2016]: https://doi.org/10.1109/mcs.2015.2512078
[research_aircraft_flyover_1976]: https://doi.org/10.2514/5.9781600865206.0103.0121
[research_aircraft_lateral_directional_2011]: https://doi.org/10.1049/pbce074e_ch9
[research_aircraft_longitudinal_2011]: https://doi.org/10.1049/pbce074e_ch10
[research_aircraft_noise_1969]: https://doi.org/10.1038/2231089a0
[research_aircraft_noise_1979]: https://doi.org/10.1108/eb035547
[research_aircraft_noise_1980]: https://doi.org/10.1108/eb035589
[research_aircraft_noise_1989]: https://doi.org/10.1017/cbo9780511584527.008
[research_aircraft_noise_1989_b]: https://doi.org/10.1017/cbo9780511584527.004
[research_aircraft_noise_2011]: https://doi.org/10.1201/b12545-4
[research_aircraft_noise_2012]: https://doi.org/10.1017/cbo9781139161893.019
[research_aircraft_noise_2012_b]: https://doi.org/10.1017/cbo9781139161893.021
[research_aircraft_noise_2019]: https://doi.org/10.12968/s1478-2774(23)50273-8
[research_aircraft_performance_2015]: https://doi.org/10.17559/tv-20131220145918
[research_aircraft_range_2011]: https://doi.org/10.1515/9781400839063-014
[research_aircraft_safety_office_1971]: https://ntrs.nasa.gov/citations/19710021280
[research_airforcetestpilotschooledwardsafbca_1962]: https://doi.org/10.21236/ada320207
[research_airforcetestpilotschooledwardsafbca_1962_b]: https://doi.org/10.21236/ada320208
[research_airforcetestpilotschooledwardsafbca_1967]: https://doi.org/10.21236/ada320224
[research_airforcetestpilotschooledwardsafbca_1967_b]: https://doi.org/10.21236/ada320209
[research_airforcetestpilotschooledwardsafbca_1991]: https://doi.org/10.21236/ada320218
[research_airforcetestpilotschooledwardsafbca_1992]: https://doi.org/10.21236/ada320221
[research_aithal_2004]: https://doi.org/10.21236/ada422143
[research_ajaj_2021]: https://doi.org/10.2514/1.c035940
[research_akatsuka_2024]: https://doi.org/10.3397/in_2024_4469
[research_akdeniz_2020]: https://doi.org/10.1108/aeat-03-2020-0056
[research_akila_marinus_2018]: https://doi.org/10.2514/6.2018-3451
[research_akishita_1986]: https://doi.org/10.2514/3.45385
[research_akiyama_2023]: https://doi.org/10.3397/in_2023_0074
[research_alaez_2022]: https://doi.org/10.3390/info13120585
[research_alam_2015]: https://doi.org/10.1016/j.ast.2014.12.020
[research_alam_hromcik_2019]: https://doi.org/10.1016/j.conengprac.2019.05.005
[research_albert_1990]: https://ntrs.nasa.gov/citations/19910007374
[research_albostan_gokasan_2018]: https://doi.org/10.1016/j.ast.2018.04.011
[research_aleksandrov_2025]: https://doi.org/10.37547/tajet/volume07issue12-09
[research_aleshin_2018]: https://doi.org/10.14419/ijet.v7i4.36.28189
[research_alexander_2025]: https://doi.org/10.4050/sm_handling_2025-5295
[research_alexander_2025_b]: https://doi.org/10.4050/sm_handling_2025-5289
[research_alexander_kinzly_1979]: https://doi.org/10.1177/001872087902100303
[research_alexandre_barde_1974]: https://doi.org/10.3397/1.2831968
[research_alfares_2026]: https://doi.org/10.3390/en19081931
[research_alford_2004]: https://doi.org/10.21236/ada423468
[research_alford_knarr_1999]: https://doi.org/10.21236/ada371942
[research_alfredson_1971]: https://ntrs.nasa.gov/citations/19710058264
[research_ali_1989]: https://doi.org/10.21236/ada215757
[research_ali_2026]: https://doi.org/10.1016/j.ast.2026.112114
[research_alieksieiev_tsybov_2025]: https://doi.org/10.26552/aer.c.2025.2.5
[research_alighanbari_2002]: https://doi.org/10.2514/2.2986
[research_alimadadi_2026]: https://doi.org/10.47176/pd.2026.1559
[research_allanach_2010]: https://doi.org/10.21236/ada571511
[research_allen_2006]: https://ntrs.nasa.gov/citations/20070022832
[research_allen_2007]: https://ntrs.nasa.gov/citations/20070005019
[research_allen_2007_2]: https://ntrs.nasa.gov/citations/20070021638
[research_allen_eveker_2000]: https://doi.org/10.21236/ada385250
[research_allen_white_1957]: https://doi.org/10.21236/ad0118718
[research_almeida_2016]: https://doi.org/10.5380/reterm.v15i2.62174
[research_almgren_1987]: https://doi.org/10.1016/0022-460x(87)90531-1
[research_almutairi_aouf_2017]: https://doi.org/10.1017/aer.2017.3
[research_alonso_castilla_2021]: https://doi.org/10.3390/aerospace9010005
[research_alston_1936]: https://doi.org/10.1108/eb030012
[research_altman_1952]: https://doi.org/10.21236/ada075871
[research_altman_2002]: https://doi.org/10.2514/6.2002-3468
[research_altman_2008]: https://doi.org/10.21236/ada494088
[research_altunkaya_2024]: https://doi.org/10.1016/j.ifacol.2025.01.184
[research_amalia_2018]: https://doi.org/10.1088/1742-6596/1130/1/012006
[research_amalia_2019]: https://doi.org/10.1088/1757-899x/645/1/012006
[research_amanatiadis_2017]: https://doi.org/10.1002/cpe.4145
[research_amargianitakis_2021]: https://doi.org/10.3397/in-2021-2555
[research_amelin_2022]: https://doi.org/10.18127/j20700784-202212-10
[research_american_institute_of_aeronautics_and_astronautics_1992]: https://ntrs.nasa.gov/citations/19930027254
[research_amiet_1988]: https://doi.org/10.1017/s0022112088001971
[research_amitary_jansen_2011]: https://doi.org/10.21236/ada564013
[research_an_2025]: https://doi.org/10.1061/jaeeez.aseng-6056
[research_an_algorithm_2026]: https://doi.org/10.17559/tv-20250425002622
[research_an_evaluation_1974]: https://doi.org/10.2514/6.1974-1020
[research_an_introduction_1966]: https://doi.org/10.1016/c2013-0-08104-2
[research_an_overview_2017]: https://doi.org/10.21884/ijmter.2017.4120.y54mr
[research_ananthkrishnan_sinha_2023]: https://doi.org/10.61653/joast.v65i4.2013.877
[research_anderle_smrcek_2003]: https://doi.org/10.14311/430
[research_anderson_1960]: https://ntrs.nasa.gov/citations/19630004821
[research_anderson_1968]: https://doi.org/10.21236/ad0675550
[research_anderson_1970]: https://doi.org/10.21236/ad0710590
[research_anderson_1973]: https://doi.org/10.2514/3.60204
[research_anderson_1976]: https://doi.org/10.1117/12.954801
[research_anderson_1985]: https://doi.org/10.2514/3.45218
[research_anderson_innis_1965]: https://doi.org/10.2514/6.1965-715
[research_anderson_schroers_1972]: https://ntrs.nasa.gov/citations/19730008267
[research_andre_1977]: https://doi.org/10.1016/0022-460x(77)90590-9
[research_andrew_christian]: https://ntrs.nasa.gov/citations/20230006776
[research_andrewpatterson_nairahovakimyan]: https://ntrs.nasa.gov/citations/20210017160
[research_ang_2024]: https://doi.org/10.1515/noise-2024-0001
[research_ang_cui_2022]: https://doi.org/10.1016/j.apacoust.2022.108978
[research_annand_1950]: https://doi.org/10.1017/s0001925900000354
[research_antipov_2020]: https://doi.org/10.2514/1.j058976
[research_antonakis_2025]: https://doi.org/10.1016/j.ast.2025.110020
[research_antonakis_2025_2]: https://doi.org/10.1007/s13272-025-00815-4
[research_antonakis_biannic_2024]: https://doi.org/10.2514/1.c037707
[research_appa_1998]: https://doi.org/10.21236/ada366980
[research_appa_ausman_1997]: https://doi.org/10.21236/ada329138
[research_arabian_schmeer_1955]: https://ntrs.nasa.gov/citations/20090026307
[research_araujo_estrada_windsor_2021]: https://doi.org/10.2514/1.c036224
[research_arcondoulis_liu_2019]: https://doi.org/10.1016/j.jsv.2018.11.005
[research_arena_1993]: https://ntrs.nasa.gov/citations/19930064312
[research_armstrong_1977]: https://doi.org/10.21236/adb029224
[research_army_aviation_school_fort_rucker_al_1961]: https://doi.org/10.21236/ad0255507
[research_armyaviationboardfortruckeral_1957]: https://doi.org/10.21236/ad0134995
[research_armyaviationcenterandfortruckeral_1992]: https://doi.org/10.21236/ada383063
[research_armyserviceforceswashingtondc_1940]: https://doi.org/10.21236/ada377432
[research_arndt_borgman_1971]: https://doi.org/10.4050/jahs.16.36
[research_arnold_1942]: https://doi.org/10.2514/8.10949
[research_arnold_1981]: https://doi.org/10.2514/6.1981-2444
[research_arseneau_1997]: https://doi.org/10.1121/1.420443
[research_arum_2020]: https://doi.org/10.3390/electronics9010179
[research_asakura_takagi_2020]: https://doi.org/10.3397/1/376811
[research_ashill_1970]: https://doi.org/10.1017/s0001925900005503
[research_ashkenas_1946]: https://ntrs.nasa.gov/citations/19930084594
[research_ashkenas_1965]: https://doi.org/10.21236/ad0627989
[research_ashkenas_1965_2]: https://doi.org/10.21236/ad0627659
[research_ashkenas_1971]: https://doi.org/10.2514/3.59104
[research_ashkenas_1984]: https://doi.org/10.2514/3.44963
[research_ashkenas_klyde_1989]: https://ntrs.nasa.gov/citations/19890011628
[research_atkin_2001]: https://doi.org/10.1007/978-3-540-45359-8_7
[research_atmaca_2025]: https://doi.org/10.2339/politeknik.1611963
[research_attenborough_1985]: https://doi.org/10.1016/0022-460x(85)90538-3
[research_attenborough_2022]: https://doi.org/10.1121/10.0010350
[research_aujogue]: https://doi.org/10.70675/54571960z44b5z4098zbf77z390e787e10ff
[research_auregan_2018]: https://doi.org/10.1121/1.5037585
[research_austin_d_thai]: https://ntrs.nasa.gov/citations/20240004303
[research_autenrieb_2025]: https://doi.org/10.2514/1.g009203
[research_avallone_2018]: https://doi.org/10.1177/1475472x18788961
[research_avco_lycoming_div_stratford_ct_1970]: https://doi.org/10.21236/ad0869088
[research_avrenli_dempsey_2015]: https://doi.org/10.15394/jaaer.2015.1629
[research_awadalla_ali_haj_ahmed_2024]: https://doi.org/10.47191/etj/v9i10.08
[research_axten_chidekel_2024]: https://doi.org/10.2514/6.2024-0680
[research_axten_maughmer_2020]: https://doi.org/10.2514/6.2020-2710
[research_aydn_kzlay_2022]: https://doi.org/10.1016/j.apacoust.2022.108773
[research_aziz_loya_2025]: https://doi.org/10.3389/arc.2025.14524
[research_azzi_tahiliani_2024]: https://doi.org/10.2514/6.2024-84319
[research_bachelder_aponso_2020]: https://doi.org/10.4050/sm_2020_hq-915
[research_bachelder_aponso_2023]: https://doi.org/10.4050/sm_2023_hq-1194
[research_bachelder_klyde_2011]: https://ntrs.nasa.gov/citations/20120000422
[research_badgley_laskin_1970]: https://doi.org/10.21236/ad0869822
[research_badzli_2023]: https://doi.org/10.15199/48.2023.08.23
[research_baek_2015]: https://doi.org/10.1016/j.compfluid.2015.06.010
[research_baek_2021]: https://doi.org/10.46300/91010.2021.15.3
[research_bagley_2026]: https://doi.org/10.1016/j.ssci.2025.107010
[research_bahr_2021]: https://doi.org/10.1017/aer.2021.114
[research_baier_1970]: https://doi.org/10.21236/ad0878050
[research_bailes_1975]: https://doi.org/10.21236/ada033827
[research_bailey_1988]: https://ntrs.nasa.gov/citations/19880063393
[research_bailey_knoedler_1996]: https://doi.org/10.21236/ada303524
[research_bailey_mcclintic_1974]: https://doi.org/10.21236/ada437794
[research_baisden_1980]: https://doi.org/10.21236/ada091113
[research_bakar_2021]: https://doi.org/10.3390/aerospace8080228
[research_baker_1941]: https://ntrs.nasa.gov/citations/20040073485
[research_baker_1942]: https://doi.org/10.1017/s0368393100100082
[research_baker_1948]: https://doi.org/10.1108/eb031614
[research_balatti_2021]: https://doi.org/10.1016/j.ast.2021.106805
[research_balatti_2023]: https://doi.org/10.1016/j.jfluidstructs.2023.103892
[research_baldwin_1973]: https://doi.org/10.21236/ad0758875
[research_baldwin_1973_b]: https://doi.org/10.21236/ad0758870
[research_baldwin_frederickson_1966]: https://doi.org/10.21236/ada021006
[research_ball_1987]: https://ntrs.nasa.gov/citations/19880006428
[research_balyakin_2015]: https://doi.org/10.3103/s1068799815010079
[research_bamber_1961]: https://doi.org/10.21236/ad0267450
[research_banerjee_1984]: https://doi.org/10.2514/3.45022
[research_banerjee_1988]: https://doi.org/10.2514/3.45607
[research_banerjee_2017]: https://doi.org/10.2514/1.c033313
[research_banerjee_2019]: https://doi.org/10.2514/1.c034888
[research_barde_birzare_2022]: https://doi.org/10.1063/5.0116450
[research_barlow_mccluskey_1972]: https://doi.org/10.21236/ad0753646
[research_barman_erzberger_1976]: https://doi.org/10.2514/3.58706
[research_barnes_2015]: https://doi.org/10.2514/6.2015-2552
[research_barnes_yager_1985]: https://ntrs.nasa.gov/citations/19850015443
[research_barnette_1978]: https://doi.org/10.21236/ada051798
[research_barr_2018]: https://doi.org/10.1111/jofo.12258
[research_barrett_gonzalez_wolf_2021]: https://doi.org/10.3390/act10100265
[research_barry_magliozzi_1971]: https://doi.org/10.21236/ad0729432
[research_barstow_1940]: https://doi.org/10.1121/1.1916087
[research_barstow_1941]: https://doi.org/10.1121/1.1902182
[research_bartels_2017]: https://doi.org/10.2514/1.c034064
[research_barton_mixson_1981]: https://doi.org/10.2514/3.57483
[research_barufaldi_morales_2023]: https://doi.org/10.2514/1.c036890
[research_basak_2022]: https://doi.org/10.1109/tccn.2021.3099114
[research_bass_1972]: https://doi.org/10.1121/1.1913183
[research_bass_1976_2]: https://doi.org/10.21236/ada026767
[research_bass_1990]: https://doi.org/10.1121/1.400176
[research_bauer_1977]: https://doi.org/10.2514/3.58844
[research_bauer_2016]: https://doi.org/10.3390/aerospace3040036
[research_bauer_2021]: https://doi.org/10.3397/in-2021-1333
[research_bauer_nagy_2024]: https://doi.org/10.3390/aerospace11010079
[research_bauermeister_donner_1980]: https://doi.org/10.1108/eb035635
[research_baughman_longeauay_2015]: https://doi.org/10.21236/ada616887
[research_baxter_1951]: https://doi.org/10.1017/s0368393100124423
[research_beale_cook_1985]: https://doi.org/10.1109/tie.1985.350144
[research_beard_2013]: https://ntrs.nasa.gov/citations/20130014431
[research_beauregard_1964]: https://doi.org/10.2514/6.1964-176
[research_bechelder_bjorkman_2025]: https://doi.org/10.4050/sm_handling_2025-5299
[research_beck_2018]: https://doi.org/10.3390/en11010252
[research_becker_korycinski_1944]: https://ntrs.nasa.gov/citations/19930090920
[research_beech_aircraft_corp_wichita_ks_1966]: https://doi.org/10.21236/ad0645216
[research_beeman_1972]: https://ntrs.nasa.gov/citations/19760006024
[research_bell_aerospace_co_buffalo_ny_1955]: https://doi.org/10.21236/ad0125728
[research_bell_aerospace_co_buffalo_ny_1955_2]: https://doi.org/10.21236/ad0125726
[research_bell_aerospace_co_buffalo_ny_1956]: https://doi.org/10.21236/ad0102191
[research_bell_aerospace_co_buffalo_ny_1956_2]: https://doi.org/10.21236/ad0102194
[research_bell_aerospace_co_buffalo_ny_1956_3]: https://doi.org/10.21236/ad0102745
[research_bell_aerospace_co_buffalo_ny_1957]: https://doi.org/10.21236/ad0136057
[research_bellucci_1963]: https://doi.org/10.21236/ad0410176
[research_belsky_2022]: https://doi.org/10.34759/trd-2022-123-16
[research_bender_brammer_1973]: https://doi.org/10.1121/1.1982292
[research_bender_brammer_1975]: https://doi.org/10.1121/1.380651
[research_bender_o_connor_1974]: https://doi.org/10.21236/ada005220
[research_bendiksen_1993]: https://doi.org/10.2514/6.1993-1479
[research_benjamin_m_simmons]: https://ntrs.nasa.gov/citations/20250003662
[research_bennett_1978]: https://ntrs.nasa.gov/citations/19780015138
[research_bennett_1978_2]: https://doi.org/10.2514/3.58360
[research_bennett_johnson_1947]: https://ntrs.nasa.gov/citations/19930081894
[research_bennett_owens_1974]: https://doi.org/10.2514/6.1974-1023
[research_benzakein_kazin_1973]: https://doi.org/10.2514/3.60198
[research_bera_1976]: https://doi.org/10.2514/3.44509
[research_bera_1980]: https://doi.org/10.1080/0020739800110412
[research_berenschot_2001]: https://doi.org/10.1016/s1369-8869(00)00018-5
[research_bergen_arnold_1940]: https://doi.org/10.2514/8.1231
[research_berger_2022]: https://doi.org/10.4050/jahs.67.032009
[research_berger_2022_2]: https://doi.org/10.4050/jahs.67.032008
[research_berger_christensen_2025]: https://doi.org/10.4050/sm_handling_2025-5294
[research_bergman_1971]: https://doi.org/10.2514/3.59176
[research_bergman_1976]: https://doi.org/10.1177/001872087601800205
[research_bergmann_2021]: https://doi.org/10.3390/aerospace8020043
[research_berkowitz_1950]: https://doi.org/10.1016/0016-0032(50)90415-7
[research_bernardini_2017]: https://doi.org/10.2352/issn.2470-1173.2017.10.imawm-168
[research_bernot_1979]: https://ntrs.nasa.gov/citations/19790014013
[research_berry_1976]: https://ntrs.nasa.gov/citations/19770011063
[research_berry_harris_2024]: https://doi.org/10.25144/21506
[research_berry_speakman_1993]: https://doi.org/10.21236/ada262494
[research_bert_1981]: https://doi.org/10.2514/3.44738
[research_bert_1999]: https://doi.org/10.1016/s1369-8869(99)00013-0
[research_berton_nark_2019]: https://doi.org/10.2514/1.c035242
[research_bertsch_2019]: https://doi.org/10.2514/1.c034809
[research_bertsch_dobrzynski_2010]: https://doi.org/10.2514/1.43188
[research_bertsch_pottpollenske_2023]: https://doi.org/10.2514/6.2023-3928
[research_beschorner_2025]: https://doi.org/10.2514/1.c038220
[research_bevilaqua_2021]: https://doi.org/10.2514/1.c036012
[research_bewick_adams_2001]: https://doi.org/10.2514/6.2001-2268
[research_beyers_1983]: https://doi.org/10.2514/3.44822
[research_beyers_1988]: https://doi.org/10.2514/3.45559
[research_bhandari_2026]: https://doi.org/10.2514/1.c038411
[research_bhardwaj_2026]: https://doi.org/10.1016/j.jsv.2026.119948
[research_bhat_2026]: https://doi.org/10.1063/5.0311082
[research_bhatia_2019]: https://doi.org/10.33552/gjes.2019.03.000568
[research_bi_2017]: https://doi.org/10.1016/j.cja.2016.12.028
[research_bian_2018]: https://doi.org/10.1080/00207179.2018.1473643
[research_bian_2019]: https://doi.org/10.1109/access.2019.2894961
[research_bienen_1927]: https://ntrs.nasa.gov/citations/19930090802
[research_biermann_conway_1942]: https://ntrs.nasa.gov/citations/19930091827
[research_bihrle_barnhart_1974]: https://ntrs.nasa.gov/citations/19750008470
[research_bilanin_donaldson_1975]: https://doi.org/10.2514/3.44476
[research_billingsley_1976]: https://doi.org/10.21236/ada024445
[research_binghua_hui_2021]: https://doi.org/10.5768/jao202142.0603003
[research_bird_1952]: https://ntrs.nasa.gov/citations/19930083189
[research_bird_jaquet_1951]: https://ntrs.nasa.gov/citations/19930092084
[research_bischoff_1974]: https://doi.org/10.2514/3.60378
[research_bischoff_1983]: https://doi.org/10.2514/3.44899
[research_bischoff_palmer_1983]: https://doi.org/10.21236/ada327418
[research_bishara_2018]: https://doi.org/10.3390/en11020383
[research_bishop_franken_1968]: https://ntrs.nasa.gov/citations/19690002239
[research_bishop_tufariello_2019]: https://doi.org/10.1121/1.5101099
[research_black_moorhouse_1979]: https://doi.org/10.21236/ada085085
[research_blackburn_1968]: https://doi.org/10.4050/jahs.13.71
[research_blackburn_joslin_2021]: https://doi.org/10.15394/jaaer.2021.1886
[research_blake_2002]: https://doi.org/10.21236/ada401264
[research_blanchard_1981]: https://ntrs.nasa.gov/citations/19810012555
[research_blanchard_2020]: https://doi.org/10.1121/10.0001930
[research_bleimeyer_1981]: https://doi.org/10.2514/6.1981-2515
[research_bliss_1980]: https://doi.org/10.21236/ada093301
[research_block_1986]: https://ntrs.nasa.gov/citations/19860060682
[research_block_gentry_1986]: https://ntrs.nasa.gov/citations/19860021869
[research_bloom_jen_1974]: https://doi.org/10.2514/3.44407
[research_blosser_1952]: https://doi.org/10.21236/ad0010761
[research_blosser_1953]: https://doi.org/10.21236/ad0015187
[research_bobbitt_1957]: https://ntrs.nasa.gov/citations/19930092295
[research_bobbitt_1959]: https://ntrs.nasa.gov/citations/19980232231
[research_boeing_co_morton_pa_vertol_div_1961]: https://doi.org/10.21236/ad0256426
[research_boeing_vertol_co_philadelphia_pa_1983]: https://doi.org/10.21236/ada134323
[research_bogdanovic_1965]: https://doi.org/10.2514/3.43689
[research_bohn_shovlin_1981]: https://doi.org/10.2514/3.57568
[research_bolds_1961]: https://doi.org/10.21236/ad0269208
[research_bolds_1962]: https://doi.org/10.21236/ad0277128
[research_boldsmoorehead_chaney_2015]: https://doi.org/10.2514/6.2015-3226
[research_bolt_beranek_and_newman_inc_los_angeles_ca_1965]: https://doi.org/10.21236/ad0617954
[research_bonnin]: https://doi.org/10.70675/2c6e0a6azc487z4165z85d2ze0fe44aa0ced
[research_bonnin_hoogreef_2025]: https://doi.org/10.2514/1.c037893
[research_bonnin_toomer_2013]: https://doi.org/10.2514/6.2013-4841
[research_bonomo_2024]: https://doi.org/10.1177/1475472x241278650
[research_bookstaber_2000]: https://doi.org/10.21236/ada520346
[research_boothe_1974]: https://doi.org/10.21236/ad0782218
[research_borchers_2009]: https://doi.org/10.1121/1.3117315
[research_borer_2016]: https://ntrs.nasa.gov/citations/20160010157
[research_borodulin_2017]: https://doi.org/10.1063/1.4999952
[research_borst_1978]: https://doi.org/10.21236/ada050593
[research_bortolussi_1997]: https://ntrs.nasa.gov/citations/19980008050
[research_bossler_smith_1974]: https://doi.org/10.1121/1.1919882
[research_boston_1984]: https://doi.org/10.2514/3.48239
[research_boswell_1970]: https://doi.org/10.1108/eb034643
[research_boswell_miller_1968]: https://doi.org/10.21236/ad0847214
[research_botros_walker_2018]: https://doi.org/10.1109/med.2018.8443024
[research_bottasso_montinari_2015]: https://doi.org/10.4050/jahs.60.022005
[research_boucher_2023]: https://doi.org/10.3397/nc_2023_01_1107
[research_boullet_2023]: https://doi.org/10.3397/in_2023_0457
[research_bowers_1979]: https://doi.org/10.2514/3.58557
[research_bowers_2016]: https://ntrs.nasa.gov/citations/20160003578
[research_bowers_2018]: https://ntrs.nasa.gov/citations/20180006672
[research_bowersox_fan_2000]: https://doi.org/10.21236/ada384726
[research_bowes_miller_1976]: https://doi.org/10.21236/ada026963
[research_bowles_1974]: https://ntrs.nasa.gov/citations/19740052233
[research_bowman_1965]: https://ntrs.nasa.gov/citations/19980228384
[research_boyd_2015]: https://doi.org/10.1016/j.aap.2015.01.021
[research_boyd_2015_2]: https://doi.org/10.1016/j.aap.2015.03.005
[research_boyd_stolzer_2016]: https://doi.org/10.1016/j.aap.2015.10.024
[research_boyden_1971]: https://doi.org/10.2514/3.59135
[research_boyer_1908]: https://doi.org/10.1038/scientificamerican07251908-63
[research_bozack_1984]: https://doi.org/10.2514/6.1984-792
[research_bracken_grotte_1979]: https://doi.org/10.2514/3.44639
[research_bradley_1975]: https://doi.org/10.21236/ada016906
[research_bramesfeld_maughmer_2002]: https://doi.org/10.2514/6.2002-2723
[research_brandon_l_litherland]: https://ntrs.nasa.gov/citations/20210016834
[research_brandon_morelli_2016]: https://doi.org/10.2514/1.c033133
[research_bras_2022]: https://doi.org/10.1016/j.ast.2022.107400
[research_braslow_1944]: https://ntrs.nasa.gov/citations/19930092788
[research_braslow_visconti_1949]: https://ntrs.nasa.gov/citations/19930085838
[research_bravo_2021]: https://doi.org/10.1016/j.energy.2020.118823
[research_bray_1960]: https://ntrs.nasa.gov/citations/19980223952
[research_bray_larsen_1965]: https://ntrs.nasa.gov/citations/20000011983
[research_brear_kerrebrock_2003]: https://doi.org/10.1115/fedsm2003-45690
[research_brennan_mcdaniel_1994]: https://doi.org/10.21236/ada284253
[research_brent_r_cobleigh_1994]: https://ntrs.nasa.gov/citations/19950007820
[research_bretoi_1952]: https://doi.org/10.1115/1.4015798
[research_breul_1963]: https://doi.org/10.21236/ad0402774
[research_brewer_1946]: https://ntrs.nasa.gov/citations/20050031173
[research_brian_trubshaw_2006]: https://doi.org/10.1108/aeat.2006.12778fae.001
[research_briardy_head_1968]: https://doi.org/10.21236/ad0673964
[research_bridges_2021]: https://doi.org/10.4271/01-14-02-0009
[research_bright_2013]: https://ntrs.nasa.gov/citations/20130003192
[research_brincklow_hunsaker_2021]: https://doi.org/10.1017/aer.2020.139
[research_brincklow_montgomery_2021]: https://doi.org/10.2514/6.2021-0327
[research_brincklow_montgomery_2024]: https://doi.org/10.1017/aer.2024.21
[research_brinza_2026]: https://doi.org/10.3390/app16031347
[research_brockett_1972]: https://doi.org/10.21236/ad0765322
[research_brodsky_luby_2013]: https://doi.org/10.21236/ada602311
[research_bromfield_2023]: https://doi.org/10.1017/aer.2023.18
[research_bromfield_2023_2]: https://doi.org/10.1016/j.apergo.2023.104101
[research_bromfield_dillman_2015]: https://doi.org/10.1016/j.promfg.2015.07.873
[research_bronder_lee_2012]: https://doi.org/10.2514/6.2012-3082
[research_bronz_2019]: https://doi.org/10.2514/6.2019-3171
[research_brooks_mackall_1984]: https://ntrs.nasa.gov/citations/19840037262
[research_brown_1950]: https://doi.org/10.21236/ad0109768
[research_brown_1954]: https://doi.org/10.1108/eb032460
[research_brown_1959]: https://ntrs.nasa.gov/citations/19980228294
[research_brown_1981]: https://ntrs.nasa.gov/citations/19820003178
[research_brown_2016]: https://doi.org/10.1121/1.4969768
[research_brown_adams_1948]: https://ntrs.nasa.gov/citations/19930091961
[research_brown_cox_1969]: https://doi.org/10.21236/ad0867010
[research_brown_heinke_1956]: https://ntrs.nasa.gov/citations/19930084532
[research_browne_2025]: https://doi.org/10.2514/1.c037981
[research_bruington_brenernan_2001]: https://doi.org/10.21236/ada390163
[research_brun_feder_1947]: https://ntrs.nasa.gov/citations/20090023708
[research_brungart_2019]: https://doi.org/10.3397/1/376723
[research_brusniak_2019]: https://ntrs.nasa.gov/citations/20200002461
[research_bryant_1963]: https://doi.org/10.21236/ad0426130
[research_bryson_2016]: https://doi.org/10.2514/1.c033455
[research_buchwalder_1985]: https://doi.org/10.1121/1.392714
[research_bucklew_2009]: https://doi.org/10.21236/ada517761
[research_buckley_2020]: https://doi.org/10.2514/1.c035463
[research_bucur_lupuleasa_2026]: https://doi.org/10.19062/1842-9238.2026.24.1.4
[research_budd_monheim_2015]: https://ntrs.nasa.gov/citations/20160008707
[research_bui_2021]: https://doi.org/10.1250/ast.42.50
[research_bull_bridges_1985]: https://doi.org/10.2514/3.45108
[research_bullmore_1990]: https://doi.org/10.1016/0022-460x(90)90524-4
[research_burken_1996]: https://ntrs.nasa.gov/citations/19970001151
[research_burken_2006]: https://ntrs.nasa.gov/citations/20060023991
[research_burken_2006_2]: https://ntrs.nasa.gov/citations/20060018301
[research_burley_1974]: https://ntrs.nasa.gov/citations/19740011555
[research_burnell_fan_1957]: https://doi.org/10.21236/ad0149920
[research_burrin_1970]: https://doi.org/10.1121/1.1974646
[research_burris_bender_1969]: https://doi.org/10.21236/ad0865310
[research_burt_1975]: https://doi.org/10.2514/3.59795
[research_burt_uselton_1976]: https://doi.org/10.2514/3.58650
[research_burton_hoburg_2018]: https://doi.org/10.2514/1.c034405
[research_bussolari_youngren_1987]: https://ntrs.nasa.gov/citations/19880027146
[research_butler_1976]: https://doi.org/10.21236/ada023690
[research_butler_1976_2]: https://doi.org/10.21236/ada032654
[research_butler_huang_1966]: https://doi.org/10.21236/ad0629637
[research_butler_langham_1978]: https://doi.org/10.21236/ada060516
[research_butzel_1982]: https://doi.org/10.2514/3.44809
[research_bynum_1978]: https://doi.org/10.21236/ada060566
[research_byrd_cates_1977]: https://doi.org/10.1121/1.2015866
[research_c_altunkaya_2025]: https://doi.org/10.2514/1.g008188
[research_c_y_harmin_2018]: https://doi.org/10.14419/ijet.v7i4.13.21355
[research_cahn_1966]: https://doi.org/10.2514/3.43783
[research_caillet_2026]: https://doi.org/10.1007/s13272-026-00957-z
[research_cain_1979]: https://doi.org/10.21236/ada379310
[research_calculation_of_1989]: https://doi.org/10.1017/cbo9780511584527.015
[research_caleb_robb]: https://ntrs.nasa.gov/citations/20230016548
[research_calise_1999]: https://ntrs.nasa.gov/citations/20000032102
[research_calloway_1983]: https://ntrs.nasa.gov/citations/19840002070
[research_calvert_1950]: https://doi.org/10.21236/adb812248
[research_campanella_1976]: https://doi.org/10.1121/1.2003160
[research_campbell_goodman_1949]: https://ntrs.nasa.gov/citations/19930082704
[research_campbell_mcdonald_1963]: https://doi.org/10.4095/325091
[research_camponogara_2019]: https://doi.org/10.1109/taes.2019.2913613
[research_campos_marques_2021]: https://doi.org/10.3390/aerospace8030077
[research_canard_caruana_1990]: https://doi.org/10.3397/1.2827762
[research_cancro_1953]: https://ntrs.nasa.gov/citations/19930087846
[research_cano_sobel_2016]: https://doi.org/10.4236/eng.2016.84016
[research_cantos_2026]: https://doi.org/10.1063/5.0301867
[research_cao_2023]: https://doi.org/10.54254/2753-8818/5/20230580
[research_cao_2023_2]: https://doi.org/10.1177/09544100231181872
[research_cao_2024]: https://doi.org/10.23967/j.rimni.2024.03.004
[research_cao_2026]: https://doi.org/10.54097/1d7p8y94
[research_cao_gao_2026]: https://doi.org/10.2514/1.c038744
[research_capone_bare_1987]: https://ntrs.nasa.gov/citations/19870015000
[research_carico]: https://doi.org/10.1109/aero.2002.1035428
[research_carico_1995]: https://doi.org/10.21236/ada300966
[research_carico_1998]: https://doi.org/10.21236/ada350677
[research_carico_chengjianhe]: https://doi.org/10.1109/aero.2001.931221
[research_carico_he_2001]: https://doi.org/10.21236/ada389261
[research_carithers_montalvo_2018]: https://doi.org/10.3390/aerospace5040113
[research_carllmeyer_lavernajohnson_1952]: https://ntrs.nasa.gov/citations/19930086856
[research_carnes_1993]: https://ntrs.nasa.gov/citations/19940019735
[research_caro_2017]: https://doi.org/10.4324/9781315243092-1
[research_carpenter_1970]: https://doi.org/10.2514/6.1970-1332
[research_carr_2024]: https://doi.org/10.1016/j.jsv.2023.118118
[research_carroll_2021]: https://doi.org/10.1027/2192-0923/a000209
[research_carroll_carroll_2005]: https://doi.org/10.2514/1.6361
[research_casagrande_hirono_2023]: https://doi.org/10.3397/in_2022_0584
[research_casalino_2021]: https://doi.org/10.1016/j.ast.2021.106707
[research_casey_1984]: https://doi.org/10.1121/1.391268
[research_castro_mota_2025]: https://doi.org/10.1016/j.enganabound.2025.106308
[research_catherines_mayes_1975]: https://ntrs.nasa.gov/citations/19760027129
[research_causse_2026]: https://doi.org/10.1027/2192-0923/a000317
[research_cavaliere_fezans_2024]: https://doi.org/10.2514/1.g007762
[research_cavcar_2011]: https://doi.org/10.2514/1.c031351
[research_cavcar_cavcar_2005]: https://doi.org/10.2514/1.6095
[research_cecrdle_2011]: https://doi.org/10.2514/6.2011-1849
[research_celebi_2025]: https://doi.org/10.30518/jav.1638955
[research_certified_aircraft_2012]: https://doi.org/10.1017/cbo9781139161893.025
[research_cfd_analysis_of_2017]: https://doi.org/10.15623/ijret.2017.0606015
[research_chabot_bird_2015]: https://doi.org/10.1139/juvs-2015-0021
[research_chakraborty_2015]: https://doi.org/10.2514/1.c033120
[research_chakraborty_mishra_2023]: https://doi.org/10.2514/1.c036813
[research_chalk_1964]: https://doi.org/10.2514/3.43604
[research_chalk_1983]: https://doi.org/10.2514/3.19820
[research_chalk_wilson_1969]: https://doi.org/10.2514/3.44041
[research_chambers_1966]: https://ntrs.nasa.gov/citations/19660020422
[research_chanaud_1972]: https://doi.org/10.1121/1.1912815
[research_chance_vought_corp_dallas_tx_1979]: https://doi.org/10.21236/ada358711
[research_chang_hung_2021]: https://doi.org/10.3390/app112411887
[research_chang_sullivan_1984]: https://doi.org/10.2514/3.48441
[research_changchuan_2018]: https://doi.org/10.2514/1.c034162
[research_chapman_1988]: https://doi.org/10.1016/0022-460x(88)90355-0
[research_chappelle_swearengen_2014]: https://doi.org/10.21236/ada600491
[research_chapter_12_2019]: https://doi.org/10.1515/9781683923312-014
[research_charles_e_feiler_1972]: https://ntrs.nasa.gov/citations/19730003288
[research_charly_kone_2025]: https://doi.org/10.3397/in_2025_1073928
[research_chau_2026]: https://doi.org/10.2514/1.c038646
[research_chau_zingg_2022]: https://doi.org/10.2514/1.c036389
[research_chau_zingg_2022_2]: https://doi.org/10.1017/aer.2022.64
[research_chau_zingg_2023]: https://doi.org/10.2514/1.c037158
[research_chaudhuri_1977]: https://doi.org/10.21236/ada064016
[research_che_2021]: https://doi.org/10.1049/icp.2021.0285
[research_che_mamat_abdul_aziz_2022]: https://doi.org/10.30880/ijie.2022.14.03.010
[research_cheeseman_1975]: https://doi.org/10.1016/0022-460x(75)90319-3
[research_chen]: https://doi.org/10.31274/rtd-180817-1316
[research_chen_2015]: https://doi.org/10.1155/2015/784298
[research_chen_2015_2]: https://doi.org/10.1016/j.apacoust.2015.02.013
[research_chen_2021_2]: https://doi.org/10.1088/1742-6596/1925/1/012007
[research_chen_2023]: https://doi.org/10.1007/s42401-023-00194-w
[research_chen_2025]: https://doi.org/10.3390/drones9090662
[research_chen_2025_3]: https://doi.org/10.1177/15553434251401784
[research_chen_2025_4]: https://doi.org/10.1080/00140139.2025.2529317
[research_chen_2025_5]: https://doi.org/10.3390/app15084333
[research_chen_2026]: https://doi.org/10.1177/00187208261434426
[research_chen_2026_3]: https://doi.org/10.1109/tie.2025.3639811
[research_chen_2026_4]: https://doi.org/10.1177/1475472x261473631
[research_chen_2026_5]: https://doi.org/10.3390/drones10040249
[research_chen_han_2017]: https://doi.org/10.21595/mme.2017.18505
[research_cheng_1978]: https://ntrs.nasa.gov/citations/19790029975
[research_cheng_2022]: https://doi.org/10.1016/j.ast.2022.107714
[research_cheng_2023]: https://doi.org/10.1088/1742-6596/2459/1/012092
[research_cheng_2025]: https://doi.org/10.3390/drones9110738
[research_cheng_langelaan_2014]: https://doi.org/10.2514/6.2014-0969
[research_cheng_meng_1980]: https://doi.org/10.1017/s0022112080002686
[research_chengtao_lixin_2011]: https://doi.org/10.1016/j.proeng.2011.10.004
[research_chernyshev_2019]: https://doi.org/10.1186/s42774-019-0007-6
[research_chessell_1978]: https://doi.org/10.1016/s0022-460x(78)80033-9
[research_chessell_1979]: https://doi.org/10.1121/1.2017371
[research_cheung_2020]: https://doi.org/10.2514/1.c035732
[research_chevalier_burke_1972]: https://doi.org/10.2514/3.44337
[research_chew_chapin_1963]: https://doi.org/10.21236/ad0402734
[research_chick_cornwellarquitt_2023]: https://doi.org/10.2514/6.2023-71874
[research_childress_1958]: https://doi.org/10.21236/ad0212827
[research_chobeau_2017]: https://doi.org/10.1016/j.jsv.2016.11.005
[research_choi_2020]: https://doi.org/10.12985/ksaa.2020.28.4.055
[research_choi_2025]: https://doi.org/10.46226/jss.2025.11.32.3.115
[research_chopra_2002]: https://doi.org/10.21236/ada411456
[research_choudhari_2011]: https://ntrs.nasa.gov/citations/20110015496
[research_chowhan_2019]: https://doi.org/10.1002/j.2334-5837.2019.00697.x
[research_christian_2021]: https://doi.org/10.1121/10.0008224
[research_christophersen_spahr_1944]: https://ntrs.nasa.gov/citations/19930092586
[research_chu_2021]: https://doi.org/10.3390/drones5020044
[research_chu_widnall_1974]: https://doi.org/10.2514/3.49577
[research_chung_1993]: https://ntrs.nasa.gov/citations/19940029436
[research_churchill_dugan_1982]: https://ntrs.nasa.gov/citations/19820012300
[research_chusseau_biron_2024]: https://doi.org/10.25144/20526
[research_chyla_2024]: https://doi.org/10.25144/22719
[research_ciaburro_2020]: https://doi.org/10.3390/buildings10050096
[research_ciepluch_1973]: https://doi.org/10.3397/1.2831943
[research_cieslak_2021]: https://doi.org/10.37105/sd.110
[research_ciliberti_nicolosi_2025]: https://doi.org/10.1186/s42774-024-00189-x
[research_ciolponea_2022]: https://doi.org/10.2478/raft-2022-0042
[research_clark_1981]: https://ntrs.nasa.gov/citations/19810025404
[research_clark_1982]: https://doi.org/10.2514/3.57365
[research_clark_2013]: https://doi.org/10.21236/ada589119
[research_clark_jr_1953]: https://doi.org/10.21236/ad0015749
[research_clarke_merson_1979]: https://doi.org/10.2514/6.1979-1798
[research_clarke_o_manning_1992]: https://ntrs.nasa.gov/citations/19930027286
[research_clarkson_mead_1973]: https://doi.org/10.1016/s0022-460x(73)80036-7
[research_claudiaalice_2010]: https://doi.org/10.13111/2066-8201.2010.2.1.10
[research_cleek_jr_1978]: https://doi.org/10.21236/ada060056
[research_cleek_jr_1978_b]: https://doi.org/10.21236/ada060057
[research_cleek_jr_1978_c]: https://doi.org/10.21236/ada060058
[research_cleek_nathanh_1979]: https://doi.org/10.21236/ada069578
[research_cleek_nathanh_1979_b]: https://doi.org/10.21236/ada069579
[research_cleek_nathanh_1979_c]: https://doi.org/10.21236/ada069576
[research_cleek_nathanh_1979_d]: https://doi.org/10.21236/ada069577
[research_cleek_nathanh_1979_e]: https://doi.org/10.21236/ada069575
[research_clemente_carrari_2025]: https://doi.org/10.3397/in_2025_1092889
[research_clewley_nixon_2019]: https://doi.org/10.1080/1463922x.2019.1574929
[research_cliff_lutze_1972]: https://doi.org/10.2514/3.44339
[research_clothier_2015]: https://doi.org/10.1016/j.ssci.2015.06.007
[research_clousing_1965]: https://ntrs.nasa.gov/citations/19650048239
[research_cobleigh_1994]: https://doi.org/10.2514/6.1994-1803
[research_cochran_2015]: https://doi.org/10.2514/1.g000628
[research_cochrane_boissevain_1978]: https://doi.org/10.2514/6.1978-1468
[research_cochrane_carros_1975]: https://doi.org/10.2514/6.1975-1220
[research_cochrane_riddle_1981]: https://doi.org/10.2514/6.1981-2625
[research_cochrane_riddle_1982]: https://doi.org/10.2514/3.44814
[research_coder_somers_2020]: https://doi.org/10.1016/j.ast.2020.106217
[research_codon_bowles_1979]: https://doi.org/10.2514/3.58589
[research_coe_1975]: https://ntrs.nasa.gov/citations/19750022117
[research_coe_newsom_1974]: https://ntrs.nasa.gov/citations/19740023393
[research_coen_richwine_2017]: https://doi.org/10.1121/1.4987181
[research_coiro_nicolosi_2001]: https://doi.org/10.1016/s1369-8869(00)00020-3
[research_coldsnow_2009]: https://doi.org/10.21236/ada516721
[research_cole_1986]: https://ntrs.nasa.gov/citations/19860017807
[research_cole_1988]: https://doi.org/10.2514/3.45609
[research_cole_cogan_2007]: https://ntrs.nasa.gov/citations/20090009358
[research_cole_dobbins_1971]: https://doi.org/10.1175/1520-0469(1971)028<0202:motaos>2.0.co;2
[research_cole_england_1967]: https://doi.org/10.21236/ad0658448
[research_coletti_1954]: https://ntrs.nasa.gov/citations/19930093712
[research_collazogarcia_ranjan_2019]: https://doi.org/10.2514/6.2019-2818
[research_collier_1990]: https://ntrs.nasa.gov/citations/19910055306
[research_colling_1995]: https://ntrs.nasa.gov/citations/19950020760
[research_colozza_2002]: https://ntrs.nasa.gov/citations/20020082943
[research_combey_2026]: https://doi.org/10.2514/1.c038518
[research_comer_chakraborty_2024]: https://doi.org/10.4050/jahs.69.032003
[research_composite_propeller_1972]: https://doi.org/10.1016/0010-4361(72)90442-9
[research_computational_simulation_2025]: https://doi.org/10.25236/ijfet.2025.070201
[research_computer_simulates_1974]: https://doi.org/10.1049/ep.1974.0015
[research_computer_techniques_1976]: https://doi.org/10.1016/0010-4485(76)90140-8
[research_condon_1970]: https://doi.org/10.21236/ad0874773
[research_cong_2023]: https://doi.org/10.3390/aerospace10030241
[research_connelly_1982]: https://doi.org/10.21236/ada120473
[research_conners_howe_2005]: https://doi.org/10.2514/6.2005-1016
[research_connor_hilton_1975]: https://ntrs.nasa.gov/citations/19750010161
[research_continental_army_command_fort_monroe_va_1958]: https://doi.org/10.21236/ad0300621
[research_control_of_2021]: https://doi.org/10.36652/0869-4931-2021-75-8-364-369
[research_cook_1964]: https://doi.org/10.21236/ada953004
[research_cook_1965]: https://doi.org/10.2514/6.1965-709
[research_cook_1979]: https://doi.org/10.1090/qam/542990
[research_coombes_2017]: https://doi.org/10.2514/1.c033856
[research_cooper_harper_1969]: https://ntrs.nasa.gov/citations/19690013177
[research_corbishley_2026]: https://doi.org/10.1177/1475472x261419070
[research_cordner_1967]: https://doi.org/10.21236/ad0656480
[research_cornell_aeronautical_lab_inc_buffalo_ny_1947]: https://doi.org/10.21236/ada800190
[research_cornell_aeronautical_lab_inc_buffalo_ny_1971]: https://doi.org/10.21236/ad0734887
[research_cornell_aeronautical_lab_inc_buffalo_ny_1971_2]: https://doi.org/10.21236/ad0734886
[research_cornell_aeronautical_lab_inc_buffalo_ny_1971_3]: https://doi.org/10.21236/ad0734885
[research_corridor_wide_surveillance_2023]: https://doi.org/10.5038/cutr-nicr-y2-4-4.1
[research_corson_1941]: https://ntrs.nasa.gov/citations/19930085187
[research_corwin_1989]: https://doi.org/10.21236/ada217067
[research_cotting_2016]: https://doi.org/10.2514/6.2016-0268
[research_cotton_1974]: https://doi.org/10.21236/ada000894
[research_coward_1955]: https://doi.org/10.21236/ad0101718
[research_cox_abbott_1966]: https://doi.org/10.1016/0022-460x(66)90105-2
[research_craig_1965]: https://doi.org/10.21236/ad0628087
[research_craig_1999]: https://doi.org/10.21236/ada400115
[research_crandall_1943]: https://ntrs.nasa.gov/citations/19930092802
[research_crane_holtzclaw_1944]: https://ntrs.nasa.gov/citations/19930091880
[research_crane_reeder_1945]: https://ntrs.nasa.gov/citations/20050028615
[research_crawford_hodgson_1961]: https://doi.org/10.21236/ad0256791
[research_crighton_1979]: https://doi.org/10.1121/1.2017528
[research_crombie_moorhouse_1980]: https://doi.org/10.21236/ada088629
[research_croom_huffman_1957]: https://ntrs.nasa.gov/citations/19930084891
[research_cross_1984]: https://ntrs.nasa.gov/citations/19850001767
[research_cross_ryley_2024]: https://doi.org/10.1017/aer.2024.113
[research_cross_watts_1983]: https://doi.org/10.2514/6.1983-2754
[research_crother_1973]: https://doi.org/10.21236/ada004416
[research_culpepper_murphy_1979]: https://ntrs.nasa.gov/citations/19790053283
[research_culver_2016]: https://doi.org/10.1121/1.4949961
[research_cummings_1929]: https://doi.org/10.1115/1.4058955
[research_cummings_1968]: https://doi.org/10.21236/ad0844459
[research_cunningham_1962]: https://doi.org/10.4271/620345
[research_cuppoletti_2024]: https://doi.org/10.3397/in_2024_3401
[research_curry_1965]: https://doi.org/10.21236/ad0617748
[research_curtis_1977]: https://doi.org/10.1121/1.381618
[research_curtiss_1971]: https://doi.org/10.2514/3.59098
[research_curtiss_h_c_1965]: https://doi.org/10.21236/ad0628669
[research_cusati_2023]: https://doi.org/10.3390/aerospace10030276
[research_cusimano_johnson_1994]: https://doi.org/10.2514/6.1994-2120
[research_czarnecki_davis_1948]: https://ntrs.nasa.gov/citations/19930082326
[research_czarnigowski_skiba_2019]: https://doi.org/10.19206/ce-2019-203
[research_czarnocki_dudek_2019]: https://doi.org/10.1051/matecconf/201930403011
[research_czysz_1963]: https://doi.org/10.21236/ad0407689
[research_d_1991]: https://doi.org/10.2514/6.1991-2862
[research_d_desocio_1999]: https://doi.org/10.2514/6.1999-4254
[research_d_l_birdsall_1970]: https://doi.org/10.1017/s0001924000114812
[research_d_l_m_v_1974]: https://doi.org/10.1016/s0022-460x(74)80340-8
[research_d_menichetti_2000]: https://doi.org/10.2514/6.2000-975
[research_dafrallah_akhloufi_2024]: https://doi.org/10.1139/dsa-2023-0049
[research_dahan_avezard_1980]: https://doi.org/10.2514/6.1980-997
[research_dahiya_2016]: https://doi.org/10.18535/ijecs/v5i11.89
[research_dahiya_2017]: https://doi.org/10.26438/ijcse/v5i9.2126
[research_dahms_bardenhagen_2019]: https://doi.org/10.1108/aeat-01-2018-0033
[research_dailey_1955]: https://doi.org/10.21236/ad0095757
[research_dalan_cohen_1985]: https://doi.org/10.2514/3.45223
[research_dalton_wang_1990]: https://doi.org/10.1016/0045-7930(90)90006-j
[research_dandwani_bragadoaldana_2025]: https://doi.org/10.2514/6.2025-3426
[research_dani]: https://doi.org/10.70675/0b07d2afzee24z4ec1z91fbz315dba170a85
[research_danjuma_2021]: https://doi.org/10.24191/jmeche.v18i3.15428
[research_danjuma_2022]: https://doi.org/10.22178/pos.81-10
[research_dash_2003]: https://doi.org/10.21236/ada461788
[research_daughaday_duwaldt_1955]: https://doi.org/10.21236/ad0103817
[research_davari_laitone_1977]: https://ntrs.nasa.gov/citations/19780032271
[research_david_seifert_2012]: https://doi.org/10.1016/j.ijheatfluidflow.2012.05.006
[research_davidson_1975]: https://doi.org/10.1175/1520-0469(1975)032<2201:spif>2.0.co;2
[research_davis_1953]: https://ntrs.nasa.gov/citations/19930083819
[research_davis_1957]: https://doi.org/10.2514/8.3998
[research_day_guthrie_1958]: https://doi.org/10.21236/ad0339907
[research_day_reisert_1959]: https://ntrs.nasa.gov/citations/19980227870
[research_de_gaspari_2024]: https://doi.org/10.1016/j.compstruct.2024.118502
[research_de_gaspari_mantegazza_2024]: https://doi.org/10.1109/access.2024.3390557
[research_de_luca_2025]: https://doi.org/10.1016/j.eng.2025.02.004
[research_de_macedo_2025]: https://doi.org/10.1016/j.array.2025.100511
[research_de_visser_pool_2023]: https://doi.org/10.2514/1.c037283
[research_de_vries_2019]: https://doi.org/10.2514/1.c035388
[research_de_vries_vos_2023]: https://doi.org/10.2514/1.c036909
[research_deal_2024]: https://doi.org/10.2514/1.i011328
[research_deckert_ferry_1959]: https://doi.org/10.21236/ada951617
[research_deckert_hodgson_1962]: https://doi.org/10.21236/ad0270921
[research_dees_2010]: https://doi.org/10.2514/6.2010-9300
[research_dees_2013]: https://doi.org/10.2514/5.9781600868986.0841.0868
[research_degtyarev_2021]: https://doi.org/10.26467/2079-0619-2021-24-1-8-15
[research_dehoff_hall_1978]: https://doi.org/10.21236/ada058891
[research_deittert_richards_2009]: https://doi.org/10.2514/6.2009-6012
[research_dekoninck_2020]: https://doi.org/10.3390/proceedings2020059013
[research_della_vecchia_2017]: https://doi.org/10.1177/1045389x17704521
[research_deloach_1975]: https://doi.org/10.1121/1.2001853
[research_demarchi_haning_1978]: https://doi.org/10.21236/ada060326
[research_dematteis_tamilia_1993]: https://doi.org/10.1017/s0001924000026671
[research_deming_1937]: https://ntrs.nasa.gov/citations/19930081380
[research_deming_1940]: https://ntrs.nasa.gov/citations/19930081525
[research_demircali_uvet_2017]: https://doi.org/10.12955/cbup.v5.1072
[research_demircali_uvet_2018]: https://doi.org/10.3390/app8091541
[research_deng_2026]: https://doi.org/10.3390/en19102442
[research_denning_1962]: https://doi.org/10.1108/eb033654
[research_dennis_scherrer_1951]: https://ntrs.nasa.gov/citations/19630002661
[research_department_of_the_air_force_washington_dc_2005]: https://doi.org/10.21236/ada495209
[research_deprez_1908]: https://doi.org/10.1038/scientificamerican09121908-165supp
[research_desanti_1988]: https://doi.org/10.2514/3.45671
[research_design_and_2015]: https://doi.org/10.21275/v4i11.nov151216
[research_design_and_2023_2]: https://doi.org/10.56726/irjmets46767
[research_deters_russell_1947]: https://ntrs.nasa.gov/citations/19930082045
[research_deters_russell_1947_2]: https://ntrs.nasa.gov/citations/19930082456
[research_deuschle_2024]: https://doi.org/10.1088/1742-6596/2716/1/012030
[research_deveaux_1965]: https://doi.org/10.21236/ad0627361
[research_development_and_2025]: https://doi.org/10.15302/j-sscae-2024.10.024
[research_development_of_1976]: https://doi.org/10.2514/5.9781600865206.0093.0102
[research_deyoung_1950]: https://ntrs.nasa.gov/citations/19930082673
[research_deyoung_1979]: https://ntrs.nasa.gov/citations/19790015752
[research_deyoung_harper_1948]: https://ntrs.nasa.gov/citations/19930091985
[research_di_2017]: https://doi.org/10.1121/1.4988047
[research_di_donato_2017]: https://doi.org/10.2514/1.g000252
[research_diamond_1963]: https://doi.org/10.21236/ad0408741
[research_diamond_lee_1965]: https://doi.org/10.1029/jz070i022p05499
[research_diarra_2023]: https://doi.org/10.3389/fnrgo.2023.1059476
[research_dias_2023]: https://doi.org/10.2514/1.c037252
[research_dickinson_1953]: https://doi.org/10.21236/ada953109
[research_dickinson_1976]: https://doi.org/10.1016/0022-460x(76)90953-6
[research_dickinson_1979]: https://doi.org/10.1121/1.2017960
[research_difranco_1970]: https://doi.org/10.2514/3.44199
[research_difranco_1971]: https://doi.org/10.21236/ad0742246
[research_diggins_1951]: https://doi.org/10.21236/ad0895227
[research_dilmi_2022]: https://doi.org/10.1061/(asce)as.1943-5525.0001401
[research_dinc_otkur_2020]: https://doi.org/10.1108/aeat-09-2020-0196
[research_dingeldein_connor_1975]: https://ntrs.nasa.gov/citations/19750010163
[research_dittmar_1977]: https://ntrs.nasa.gov/citations/19780005911
[research_dittmar_1978]: https://ntrs.nasa.gov/citations/19790007586
[research_dittmar_1981]: https://ntrs.nasa.gov/citations/19810014303
[research_dittmar_1983]: https://ntrs.nasa.gov/citations/19840006806
[research_dittmar_1984]: https://ntrs.nasa.gov/citations/19850002480
[research_dittmar_1985]: https://ntrs.nasa.gov/citations/19860004537
[research_dittmar_1989]: https://ntrs.nasa.gov/citations/19890012257
[research_dittmar_1989_2]: https://ntrs.nasa.gov/citations/19890015515
[research_dittmar_hall_1991]: https://ntrs.nasa.gov/citations/19920007487
[research_dittmar_jeracki_1979]: https://ntrs.nasa.gov/citations/19790017669
[research_dittmar_jeracki_1981]: https://ntrs.nasa.gov/citations/19810017231
[research_dittmar_jeracki_1981_b]: https://ntrs.nasa.gov/citations/19820008934
[research_dittmar_stang_1987]: https://ntrs.nasa.gov/citations/19870018965
[research_dittmar_stang_1987_2]: https://ntrs.nasa.gov/citations/19880029338
[research_dittmar_stefko_1982]: https://ntrs.nasa.gov/citations/19830003570
[research_dittmar_stefko_1983]: https://ntrs.nasa.gov/citations/19830014841
[research_dittmar_stefko_1983_b]: https://ntrs.nasa.gov/citations/19840008878
[research_doak_vaidya_1970]: https://doi.org/10.1016/0022-460x(70)90090-8
[research_doblhoff_1956]: https://doi.org/10.21236/ad0109767
[research_dobrzynski_1981]: https://doi.org/10.2514/3.44712
[research_dobrzynski_1993]: https://doi.org/10.1006/jsvi.1993.1152
[research_dodbele_1987]: https://doi.org/10.2514/3.45444
[research_doebler_2023]: https://doi.org/10.1121/10.0019016
[research_doelling_1961]: https://doi.org/10.21236/ad0404785
[research_doelling_bolt_1961]: https://doi.org/10.21236/ad0403701
[research_doelling_bolt_1961_2]: https://doi.org/10.21236/ad0403730
[research_doggett_soistmann_1992]: https://doi.org/10.2514/3.46155
[research_doherty_butzel_1979]: https://doi.org/10.21236/adb049608
[research_doherty_butzel_1979_2]: https://doi.org/10.21236/adb049493
[research_dohme_1981]: https://doi.org/10.21236/adp001308
[research_doko_sasongko_2026]: https://doi.org/10.11648/j.ajae.20261201.11
[research_dolmans_patrick_1998]: https://doi.org/10.2514/6.1998-2235
[research_dolph_2021]: https://doi.org/10.2514/1.i010911
[research_doman_1995]: https://doi.org/10.21236/ada305053
[research_domen_1998]: https://doi.org/10.21236/ada339252
[research_domogalla_2026]: https://doi.org/10.1007/s13272-026-00945-3
[research_domogalla_bertsch_2021]: https://doi.org/10.3390/aerospace9010003
[research_donald_b_hanson_david_j_parzych_1993]: https://ntrs.nasa.gov/citations/19930015905
[research_donaldson_priest_2012]: https://ntrs.nasa.gov/citations/20120014586
[research_donateo_totaro_2019]: https://doi.org/10.1108/aeat-01-2018-0036
[research_dong_2016]: https://doi.org/10.1016/j.ast.2016.06.006
[research_dong_2016_2]: https://doi.org/10.1155/2016/5037678
[research_dong_2024]: https://doi.org/10.61935/acetr.4.1.2024.p130
[research_dong_2024_2]: https://doi.org/10.61935/acetr.4.1.2024.p124
[research_donizetti_2023]: https://doi.org/10.2514/1.c037027
[research_dooley_yeary_1979]: https://doi.org/10.21236/ada071648
[research_dorfling_rokhsaz_2015]: https://doi.org/10.2514/1.c032859
[research_douglas_aircraft_co_long_beach_ca_1962]: https://doi.org/10.21236/ad0404510
[research_douglas_aircraft_co_long_beach_ca_1963]: https://doi.org/10.21236/ad0425406
[research_dowell_bliss_1978]: https://doi.org/10.21236/ada055735
[research_downing_zamot_1996]: https://ntrs.nasa.gov/citations/19960055062
[research_doyle_2020]: https://doi.org/10.1049/et.2020.0310
[research_dr_olivia_davis_2021]: https://doi.org/10.71465/ajaae269
[research_dragna_blanc_benon_2017]: https://doi.org/10.1121/1.5014743
[research_dragna_blanc_benon_2017_2]: https://doi.org/10.1121/1.5006180
[research_dragos_1985]: https://doi.org/10.1007/bf01184848
[research_dragos_1990]: https://doi.org/10.1007/bf01173739
[research_drakin_1963]: https://doi.org/10.21236/ad0295828
[research_dravid_1971]: https://doi.org/10.1049/iipi.1971.0005
[research_dreyfus_dreyfus_1979]: https://doi.org/10.21236/ada071320
[research_dryden_ballif_1930]: https://doi.org/10.6028/jres.005.011
[research_du_2024]: https://doi.org/10.3390/drones8080354
[research_du_2024_2]: https://doi.org/10.54254/2755-2721/103/20241042
[research_duan_zhang_2018]: https://doi.org/10.1007/s42401-018-0009-9
[research_dubnicky_splichal_2023]: https://doi.org/10.21495/em2023-59
[research_ducard_2015]: https://doi.org/10.1515/amcs-2015-0014
[research_duchevet_2025]: https://doi.org/10.1177/00187208251342100
[research_dudek_2020]: https://doi.org/10.3390/en13174393
[research_dudziak_2020]: https://doi.org/10.20858/sjsutst.2020.108.3
[research_duerksen_1997]: https://ntrs.nasa.gov/citations/19970031951
[research_duffy_1968]: https://doi.org/10.21236/ad0678493
[research_duhl_thompson_1977]: https://doi.org/10.2514/3.58816
[research_dunlap_1956]: https://doi.org/10.21236/ad0098048
[research_dunlap_1969]: https://doi.org/10.2514/3.44103
[research_dunlap_porter_1971]: https://doi.org/10.21236/ad0725741
[research_dunn_2015]: https://doi.org/10.1260/1475-472x.14.1-2.51
[research_dunn_farassat_1990]: https://doi.org/10.2514/6.1990-3934
[research_dunn_farassat_1992]: https://doi.org/10.2514/3.11128
[research_dunn_tarkenton_1989]: https://ntrs.nasa.gov/citations/19890005449
[research_dunnavan_1983]: https://doi.org/10.5962/bhl.title.61939
[research_durand_1893]: https://doi.org/10.1115/1.4061318
[research_durand_wasicko_1967]: https://doi.org/10.2514/3.43812
[research_durbin_1983]: https://doi.org/10.1016/0022-460x(83)90830-1
[research_durbin_mcgeer_1982]: https://doi.org/10.2514/3.57415
[research_dussart_2019]: https://doi.org/10.3390/aerospace6060063
[research_dussart_2019_2]: https://doi.org/10.3390/aerospace6060070
[research_dusterberry_1964]: https://ntrs.nasa.gov/citations/19660003380
[research_dutta_2026]: https://doi.org/10.58445/rars.4118
[research_dwyer_1994]: https://doi.org/10.2514/6.1994-2158
[research_dyer_1956]: https://doi.org/10.1121/1.2369207
[research_dym_williams_2015]: https://doi.org/10.1177/0306419015573908
[research_dynamic_response_2021]: https://doi.org/10.5829/ije.2021.34.01a.22
[research_eastman_1986]: https://doi.org/10.2514/3.55556
[research_echavarria_poroseva_2015]: https://doi.org/10.2514/6.2015-0016
[research_eckhaus_1962]: https://doi.org/10.2514/8.9589
[research_ecotiere_2023]: https://doi.org/10.3397/in_2023_0874
[research_edenborough_1968]: https://doi.org/10.2514/3.43915
[research_edwardglodeck_raymstandahar_1944]: https://ntrs.nasa.gov/citations/20150017973
[research_edwards_1997]: https://doi.org/10.21236/ada325252
[research_edwards_2015]: https://doi.org/10.21236/ada614555
[research_eggleston_diederich_1957]: https://ntrs.nasa.gov/citations/19930092312
[research_eisenhut_strohmayer_2026]: https://doi.org/10.3390/aerospace13030292
[research_el_gaouti_2024]: https://doi.org/10.3390/math12111619
[research_el_ramly_1976]: https://doi.org/10.2514/3.58736
[research_el_safany_bromfield_2025]: https://doi.org/10.1017/aer.2025.24
[research_elkoby_2007]: https://ntrs.nasa.gov/citations/20070021691
[research_ellerbroek_stroosma_2007]: https://doi.org/10.2514/6.2007-6800
[research_elliot_1990]: https://doi.org/10.1016/0022-460x(90)90525-5
[research_elliott_1989]: https://doi.org/10.1016/0022-460x(89)90778-5
[research_ellis_1971]: https://ntrs.nasa.gov/citations/19720003283
[research_ellis_1972]: https://doi.org/10.4271/720317
[research_elyasi_2020]: https://doi.org/10.1007/s40430-020-02633-7
[research_elzoghby_2017]: https://doi.org/10.3390/s17040887
[research_emami_roudbari_2019]: https://doi.org/10.1109/taes.2018.2883848
[research_emeric_1966]: https://doi.org/10.21236/ad0643771
[research_emslie_1966]: https://doi.org/10.1108/eb034155
[research_eney_1968]: https://doi.org/10.2514/3.43938
[research_engblom_2016]: https://ntrs.nasa.gov/citations/20190001544
[research_englar_1970]: https://doi.org/10.21236/ad0882075
[research_envia_1992]: https://ntrs.nasa.gov/citations/19930035172
[research_envia_2016]: https://doi.org/10.1177/1475472x16642134
[research_envia_2018]: https://doi.org/10.1201/b20287-1
[research_eppel_1981]: https://ntrs.nasa.gov/citations/19820002158
[research_eppley_1963]: https://doi.org/10.21236/ad0400112
[research_epstein_oflarity_2019]: https://doi.org/10.2514/1.b37015
[research_er_el_1989]: https://doi.org/10.2514/3.45754
[research_erb_aldrich_2009]: https://doi.org/10.2514/6.2009-1711
[research_erickson_johnc_1965]: https://doi.org/10.21236/ad0623527
[research_ericsson_1987]: https://doi.org/10.2514/3.45416
[research_ernst_sachau_2025]: https://doi.org/10.1121/10.0041347
[research_ernsthausen_1937]: https://ntrs.nasa.gov/citations/19930094591
[research_eser_2023]: https://doi.org/10.3397/no_2023_0040
[research_eshmuradov_bekbaev_2023]: https://doi.org/10.2139/ssrn.4466563
[research_esnault]: https://doi.org/10.70675/362b1219z257az45e0z8d00zfc968011807b
[research_esparza_1975]: https://ntrs.nasa.gov/citations/19750021092
[research_esteban_2015]: https://doi.org/10.1016/j.ifacol.2015.08.070
[research_eugeneamorelli]: https://ntrs.nasa.gov/citations/20230012591
[research_evaluating_the_2015]: https://doi.org/10.21535/rt4q5x62
[research_evans_1972]: https://doi.org/10.1121/1.1981611
[research_evans_1972_2]: https://doi.org/10.1121/1.1913000
[research_evans_1975]: https://doi.org/10.1121/1.1995101
[research_evans_dunbar_1982]: https://doi.org/10.1121/1.387731
[research_evans_schilling_1983]: https://ntrs.nasa.gov/citations/19830067137
[research_evans_schilling_1984]: https://ntrs.nasa.gov/citations/19840013469
[research_eversman_1990]: https://doi.org/10.2514/3.45948
[research_experimental_analysis_2017]: https://doi.org/10.7324/rjc.2017.1021629
[research_eyercioglu_aladag_2021]: https://doi.org/10.46519/ij3dptdi.958048
[research_failure_of_2005]: https://doi.org/10.31399/asm.tb.faesmch.t51270152
[research_fajar_arifianto_2018]: https://doi.org/10.30536/j.jtd.2017.v0.a2760
[research_fakhraian_2023]: https://doi.org/10.3390/drones7070478
[research_fang_2023]: https://doi.org/10.1109/jlt.2022.3208451
[research_farajollahi_markazi_2010]: https://doi.org/10.1109/iccet.2010.5486075
[research_farassat_succi_1980]: https://ntrs.nasa.gov/citations/19800063486
[research_fard_2022]: https://doi.org/10.1109/tte.2022.3197332
[research_farhat_1998]: https://doi.org/10.21236/ada361695
[research_farhat_2000]: https://doi.org/10.21236/ada389378
[research_farhat_2001]: https://doi.org/10.21236/ada387498
[research_farokhi_vertzberger_1989]: https://ntrs.nasa.gov/citations/19900027291
[research_fasel_2002]: https://doi.org/10.21236/ada406456
[research_faulcon_monteith_1978]: https://ntrs.nasa.gov/citations/19780014805
[research_fay_johnstone_1960]: https://doi.org/10.21236/ad0248516
[research_fechter_mills_1988]: https://doi.org/10.2514/6.1988-2174
[research_feero_2016]: https://doi.org/10.1007/s12650-016-0365-7
[research_fehlner_1942]: https://ntrs.nasa.gov/citations/19930092512
[research_feimin_2021]: https://doi.org/10.1049/icp.2021.0269
[research_feistel_1978]: https://ntrs.nasa.gov/citations/19780065878
[research_feistel_1981]: https://ntrs.nasa.gov/citations/19980202341
[research_feistel_1981_2]: https://ntrs.nasa.gov/citations/19810058335
[research_fejtek_1993]: https://ntrs.nasa.gov/citations/19940006303
[research_felcyn_ptak_2022]: https://doi.org/10.24425/aoa.2022.142892
[research_felder_kim_2009]: https://ntrs.nasa.gov/citations/20130010780
[research_felt_kehoe_1985]: https://ntrs.nasa.gov/citations/19860063064
[research_feng_2022]: https://doi.org/10.1049/icp.2022.1595
[research_fenwick_1966]: https://doi.org/10.21236/ad0737274
[research_fenwick_1967]: https://doi.org/10.21236/ad0738376
[research_ferguson_hanson_1984]: https://ntrs.nasa.gov/citations/19850049865
[research_ferguson_thomson_2015]: https://doi.org/10.2514/1.c032657
[research_ferrari_castelli_1985]: https://doi.org/10.3397/1.2827647
[research_ferrell_1974]: https://doi.org/10.21236/ada109440
[research_fetterman_penland_1960]: https://ntrs.nasa.gov/citations/19660024030
[research_ffowcs_williams_hawkings_1969]: https://doi.org/10.1016/0022-460x(69)90125-4
[research_fidell_1989]: https://doi.org/10.21236/ada214164
[research_fidell_1989_2]: https://doi.org/10.21236/ada353797
[research_fidell_1998]: https://doi.org/10.21236/ada388876
[research_fidell_2018]: https://doi.org/10.13189/cea.2018.060204
[research_fidell_reddingius_1990]: https://doi.org/10.1121/1.2027879
[research_fidell_secrist_1990]: https://ntrs.nasa.gov/citations/19900015553
[research_figliola_2005]: https://doi.org/10.21236/ada435403
[research_figueira_2025]: https://doi.org/10.2514/1.c037964
[research_finch_matranga_1959]: https://ntrs.nasa.gov/citations/19980236840
[research_finger_2020]: https://doi.org/10.2514/1.c035897
[research_finger_2020_2]: https://doi.org/10.2514/1.c035428
[research_fink_1970]: https://ntrs.nasa.gov/citations/19700013310
[research_fink_1978]: https://doi.org/10.2514/3.58433
[research_fink_1979]: https://doi.org/10.2514/3.58586
[research_fink_schlinker_1980]: https://doi.org/10.2514/3.57880
[research_finn_rogers_2015]: https://doi.org/10.1121/1.4926900
[research_finn_rogers_2016]: https://doi.org/10.1175/jtech-d-15-0170.1
[research_finn_rogers_2016_2]: https://doi.org/10.1121/1.4950227
[research_finnestead_antoniou_1965]: https://doi.org/10.21236/ad0467490
[research_finnestead_connor_1970]: https://doi.org/10.21236/ad0874210
[research_fischel_schneiter_1947]: https://ntrs.nasa.gov/citations/19930082125
[research_fischer_1992]: https://doi.org/10.1121/1.405201
[research_fischer_2006]: https://doi.org/10.21236/ada445827
[research_fisher_1956]: https://doi.org/10.21236/ad0092459
[research_fladeland_2019]: https://ntrs.nasa.gov/citations/20190032041
[research_flechner_jacobs_1978]: https://ntrs.nasa.gov/citations/19780015109
[research_fleming_1954]: https://doi.org/10.1017/s0368393100098552
[research_flight_sciences_lab_inc_buffalo_ny_1964]: https://doi.org/10.21236/ad0442900
[research_flight_test_2016]: https://doi.org/10.21535/dnk59q51
[research_flindell_2021]: https://doi.org/10.1016/j.apacoust.2021.108032
[research_foch_ailinger_1992]: https://doi.org/10.2514/6.1992-1263
[research_ford_1989_2]: https://doi.org/10.1108/eb036732
[research_ford_1990]: https://doi.org/10.1108/eb036902
[research_ford_2004]: https://doi.org/10.1108/aeat.2004.12776faf.002
[research_fordcengmraes_1992]: https://doi.org/10.1108/eb037224
[research_forehand_bair_1969]: https://doi.org/10.2514/3.44086
[research_forkun_makaryshkin_2020]: https://doi.org/10.31891/2307-5732-2020-289-5-21-27
[research_forsching_zingel_1988]: https://doi.org/10.1016/s0889-9746(88)80021-5
[research_forsythe_a_c_r_1946]: https://doi.org/10.1175/1520-0477-27.4.160
[research_fosdick_1970]: https://doi.org/10.21236/ad0880677
[research_foss_1979]: https://doi.org/10.1121/1.383343
[research_fournier_2022]: https://doi.org/10.2514/1.g006084
[research_fournier_silvers_1958]: https://ntrs.nasa.gov/citations/19930089979
[research_frampton_1993]: https://doi.org/10.21236/ada405069
[research_frank_w_burcham_1992]: https://ntrs.nasa.gov/citations/19920023620
[research_franklin_1971]: https://doi.org/10.2514/3.44303
[research_franklin_1972]: https://doi.org/10.2514/3.58970
[research_franklin_1988]: https://ntrs.nasa.gov/citations/19890040834
[research_frazier_2016]: https://doi.org/10.1111/puar.12549
[research_fredericks_2013]: https://ntrs.nasa.gov/citations/20140001088
[research_frederickson_1967]: https://doi.org/10.21236/ad0650403
[research_freuler_hoffmann_1977]: https://doi.org/10.2514/6.1977-1216
[research_friedlander_2018]: https://ntrs.nasa.gov/citations/20180005558
[research_friedrich_robertson_2015]: https://doi.org/10.2514/1.c032660
[research_frierson_1978]: https://doi.org/10.2514/3.58341
[research_fruncillo_luchini_2024]: https://doi.org/10.2514/6.2024-3320
[research_fruncillo_luchini_2025]: https://doi.org/10.61782/fa.2025.0537
[research_fry_1967]: https://doi.org/10.2514/6.1967-411
[research_fry_2008]: https://doi.org/10.21236/ada494062
[research_fu_2020]: https://doi.org/10.1155/2020/8971275
[research_fu_2021]: https://doi.org/10.1038/s41598-021-95187-0
[research_fu_2026]: https://doi.org/10.1109/taes.2026.3664344
[research_fujita_2021]: https://doi.org/10.3397/in-2021-1668
[research_fukuda_1960]: https://doi.org/10.1299/kikai1938.26.1167
[research_fukuda_1960_2]: https://doi.org/10.1299/kikai1938.26.1174
[research_fukuda_1963]: https://doi.org/10.1299/jsme1958.6.255
[research_fukuda_1963_2]: https://doi.org/10.1299/kikai1938.29.415
[research_fuller_jones_1987]: https://doi.org/10.1016/s0022-460x(87)80208-0
[research_gabino_martinez_rodriguez]: https://ntrs.nasa.gov/citations/20240007499
[research_gager_headrick_1962]: https://doi.org/10.21236/ad0391099
[research_gaifullin_2023]: https://doi.org/10.1134/s0015462823600426
[research_gallagher_1971]: https://doi.org/10.2514/3.59189
[research_galloway_bennett_1981]: https://doi.org/10.21236/ada098540
[research_gandhi_pepe_2022]: https://doi.org/10.4050/f-0078-2022-1256
[research_gang_kwon_2018]: https://doi.org/10.1016/j.ijhydene.2018.04.049
[research_ganiev_1978]: https://doi.org/10.1007/bf01091671
[research_gao_2019]: https://doi.org/10.1109/access.2019.2917316
[research_gao_2023]: https://doi.org/10.56028/aetr.8.1.804.2023
[research_gao_2024]: https://doi.org/10.1016/j.ast.2024.109671
[research_gao_shao_2024]: https://doi.org/10.1061/jaeeez.aseng-5076
[research_garcia_baquero_2018]: https://doi.org/10.1016/j.ifacol.2018.07.099
[research_garcia_eskandarian_2026]: https://doi.org/10.3390/drones10010065
[research_gardini_2022]: https://doi.org/10.1590/jatm.v14.1282
[research_gardner_downey_1950]: https://doi.org/10.21236/ad0069271
[research_garfinkel_1951]: https://doi.org/10.1090/qam/43664
[research_garkushenko_vinogradov_2016]: https://doi.org/10.3103/s1068799816040085
[research_gasaway_1969]: https://doi.org/10.21236/ad0702422
[research_gasaway_1970]: https://doi.org/10.21236/ad0705964
[research_gasaway_hatfield_1963]: https://doi.org/10.21236/ad0428331
[research_gaston_2013]: https://doi.org/10.21236/ada592042
[research_gates_schy_1951]: https://ntrs.nasa.gov/citations/19930082984
[research_gates_sternfield_1950]: https://ntrs.nasa.gov/citations/20050019392
[research_gatti_giulietti_2015]: https://doi.org/10.1016/j.ast.2015.05.009
[research_gautam_hanson_2025]: https://doi.org/10.1121/10.0036571
[research_gavrilovic_2018]: https://doi.org/10.2514/1.c034531
[research_gavurin_1965]: https://doi.org/10.21236/ad0626468
[research_gayle_jeracki_1989]: https://ntrs.nasa.gov/citations/19900036595
[research_gayne_1965]: https://doi.org/10.2514/6.1965-329
[research_gedney_abbot_1998]: https://doi.org/10.1115/imece1998-0506
[research_geiger_2002]: https://doi.org/10.2514/6.2002-5833
[research_geister_2017]: https://doi.org/10.2514/1.c034337
[research_genalo]: https://doi.org/10.31274/rtd-180814-4061
[research_genalo_pierson_1978]: https://doi.org/10.1080/03052157808902389
[research_general_aviation_2022]: https://doi.org/10.1016/c2018-0-03861-x
[research_general_electric_co_cincinnati_oh_1964]: https://doi.org/10.21236/ad0447839
[research_generalelectriccoschenectadyny_1952]: https://doi.org/10.21236/ad0000287
[research_geng_2024]: https://doi.org/10.32604/jai.2024.047642
[research_gennaretti_2017]: https://doi.org/10.1177/1475472x17709927
[research_george_2022]: https://doi.org/10.14704/web/v19i1/web19216
[research_georgiou_2026]: https://doi.org/10.1121/10.0042533
[research_gera_1981]: https://ntrs.nasa.gov/citations/19820030371
[research_gerber_2003]: https://doi.org/10.1121/1.1560250
[research_gerken_1979]: https://doi.org/10.21236/ada132587
[research_gerstle_1999]: https://doi.org/10.21236/ada361474
[research_geuther_capristan_2020]: https://ntrs.nasa.gov/citations/20200002786
[research_ghalandari_2022]: https://doi.org/10.32604/cmc.2022.020884
[research_ghenescu_2026]: https://doi.org/10.3390/s26061778
[research_ghofur_m_2020]: https://doi.org/10.54317/kom.v2ioktober.180
[research_gibbs_2023]: https://doi.org/10.3397/in_2022_0695
[research_gilbert_nguyen_1976]: https://ntrs.nasa.gov/citations/19760017178
[research_gilbrook_2025]: https://doi.org/10.1108/aeat-06-2024-0160
[research_giles_1972]: https://doi.org/10.2514/3.58942
[research_gill_2015]: https://doi.org/10.2514/1.g000966
[research_gillard_1998]: https://doi.org/10.21236/ada362903
[research_gille_2017]: https://doi.org/10.1016/j.apacoust.2016.08.022
[research_gillfillan_1961]: https://doi.org/10.1061/jaceal.0000090
[research_gillfillian_1962]: https://doi.org/10.1061/taceat.0008607
[research_gilyard_1974]: https://ntrs.nasa.gov/citations/19740017478
[research_gimmestad_1980]: https://doi.org/10.2514/3.44673
[research_gleason_walker_1996]: https://doi.org/10.2514/6.1996-159
[research_glegg_devenport_2024]: https://doi.org/10.1016/b978-0-443-19112-1.00017-5
[research_glenn_midkiff_1951]: https://doi.org/10.21236/adb802822
[research_gliding_and_1938]: https://doi.org/10.1038/141442b0
[research_glizde_2017]: https://doi.org/10.1515/tae-2017-0010
[research_go_choi_2021]: https://doi.org/10.3390/drones5030075
[research_godwin_frazier_1964]: https://doi.org/10.21236/ad0613504
[research_goestchel_2022]: https://doi.org/10.1016/j.jsv.2022.116974
[research_goglia_arunkumar_1983]: https://ntrs.nasa.gov/citations/19830013935
[research_goksel]: https://doi.org/10.15476/elte.2025.157
[research_goland_1952]: https://doi.org/10.21236/ad0004240
[research_goland_miller_1964]: https://doi.org/10.21236/ad0608186
[research_goldman_2016]: https://doi.org/10.1121/1.4969771
[research_goldstein_1982]: https://doi.org/10.4050/sm_handling_1982-4947
[research_golovkin_2019]: https://doi.org/10.1615/tsagiscij.2019032577
[research_golubinskii_golubkin_1983]: https://doi.org/10.1007/bf01090751
[research_golubkin_1980]: https://doi.org/10.1007/bf01089616
[research_golubkin_1980_2]: https://doi.org/10.1007/bf01089658
[research_goncharenko_2022]: https://doi.org/10.3846/aviation.2022.16920
[research_gonczy_2015]: https://doi.org/10.1051/matecconf/20152900002
[research_gong_2024]: https://doi.org/10.1051/e3sconf/202455304009
[research_goodman_1976]: https://doi.org/10.1007/bf01535386
[research_gopalan_2022]: https://doi.org/10.1121/10.0015471
[research_goyal_2024]: https://doi.org/10.1016/j.ast.2024.109021
[research_goyal_2025]: https://doi.org/10.2514/1.c038073
[research_graham_1945]: https://ntrs.nasa.gov/citations/19930093551
[research_graham_1971]: https://doi.org/10.1017/s0001925900005667
[research_graham_rodriquez_1951]: https://doi.org/10.21236/ada073847
[research_grana_shanks_1952]: https://ntrs.nasa.gov/citations/20050029465
[research_grantham_1984]: https://ntrs.nasa.gov/citations/19850002694
[research_grantham_1985]: https://ntrs.nasa.gov/citations/19850025831
[research_grantham_nguyen_1974]: https://ntrs.nasa.gov/citations/19740013545
[research_grauer_2017]: https://doi.org/10.2514/1.c034407
[research_grauer_2021]: https://doi.org/10.2514/1.c035933
[research_grauer_morelli_2023]: https://doi.org/10.2514/1.c037583
[research_graves_1982]: https://ntrs.nasa.gov/citations/19820021437
[research_gray_1964]: https://doi.org/10.2514/6.1964-192
[research_gray_2009]: https://doi.org/10.2514/6.2009-6317
[research_gray_2026]: https://doi.org/10.61278/itea.47.1.1003
[research_gray_kemper_2009]: https://doi.org/10.2514/6.2009-1746
[research_green_1931]: https://doi.org/10.1109/ee.1931.6430352
[research_green_1988]: https://doi.org/10.2514/6.1988-4142
[research_green_2023]: https://doi.org/10.3397/nc_2023_01_1108
[research_greenhalgh_1983]: https://doi.org/10.21236/ada152240
[research_greenwood_schmitz_2014]: https://doi.org/10.2514/1.c032045
[research_greer_2000]: https://ntrs.nasa.gov/citations/20000095076
[research_greer_hamory_1999]: https://ntrs.nasa.gov/citations/19990049398
[research_gregorek_1984]: https://ntrs.nasa.gov/citations/19930062826
[research_gregorek_1995]: https://ntrs.nasa.gov/citations/19950021556
[research_gregorygzilliac_2026]: https://ntrs.nasa.gov/citations/20260008447
[research_grendysa_2019]: https://doi.org/10.1108/aeat-09-2018-0256
[research_gresham_2024]: https://doi.org/10.2514/1.c036835
[research_grether_1973]: https://doi.org/10.21236/ad0767203
[research_griffin_1983]: https://doi.org/10.21236/ada133188
[research_griffin_bellaire_1968]: https://doi.org/10.21236/ad0850270
[research_griffin_mcbride_1986]: https://doi.org/10.21236/ada168246
[research_griffith_1971]: https://doi.org/10.1121/1.1975595
[research_griffith_roberts_1972]: https://doi.org/10.4271/720339
[research_grindley_2025]: https://doi.org/10.1016/j.apergo.2025.104516
[research_grossman_gurdal_1986]: https://doi.org/10.2514/6.1986-2623
[research_grosveld_1985]: https://doi.org/10.2514/3.45094
[research_grosveld_1988]: https://doi.org/10.2514/3.45683
[research_grosveld_navaneethan_1980]: https://doi.org/10.2514/6.1980-1874
[research_groves_1955]: https://doi.org/10.1016/0021-9169(55)90119-7
[research_groves_1956]: https://doi.org/10.1016/0021-9169(56)90125-8
[research_groves_1956_2]: https://doi.org/10.1016/0021-9169(56)90088-5
[research_grubin_1972]: https://doi.org/10.2514/3.44325
[research_grunwald_1961]: https://ntrs.nasa.gov/citations/19980227742
[research_gu_1986]: https://doi.org/10.2514/3.25863
[research_gu_2024]: https://doi.org/10.2514/1.j063646
[research_gu_2025]: https://doi.org/10.1049/icp.2024.3065
[research_gu_2026]: https://doi.org/10.1016/j.jsv.2026.120049
[research_guerin_2023]: https://doi.org/10.3397/in_2023_1053
[research_guerrero_2026]: https://doi.org/10.2514/1.d0553
[research_guidry_2001]: https://doi.org/10.21236/ada389720
[research_guimaraes_neto_2025]: https://doi.org/10.1016/j.ast.2025.110115
[research_guldal_andersson_2020]: https://doi.org/10.1002/j.2334-5837.2020.00742.x
[research_gulyaeva_2018]: https://doi.org/10.31174/nt2018-158vi18-13
[research_gundry_1977]: https://doi.org/10.2514/3.58832
[research_guo_2020]: https://doi.org/10.3390/electronics9020364
[research_guo_2022_2]: https://doi.org/10.32604/cmes.2022.020638
[research_guo_thomas_2015]: https://doi.org/10.2514/1.c033048
[research_gupta_2016]: https://doi.org/10.2514/1.c033346
[research_gur_2014]: https://doi.org/10.2514/1.c032557
[research_guruswamy_2021]: https://doi.org/10.1016/j.ast.2021.107158
[research_guruswamy_2021_2]: https://doi.org/10.2514/1.j060055
[research_guthridge_2025]: https://doi.org/10.58940/2329-258x.2062
[research_guzik_2019]: https://doi.org/10.1121/1.5137614
[research_gwak_lee_2017]: https://doi.org/10.7776/ask.2017.36.2.089
[research_gyorgyfalvy_1965]: https://doi.org/10.2514/3.43693
[research_h_t_santos_2025]: https://doi.org/10.3397/in_2025_1074416
[research_hace_2019]: https://doi.org/10.3390/en12152974
[research_hacker_1977]: https://doi.org/10.2514/3.44571
[research_hacker_wroblewski_2009]: https://doi.org/10.21236/ada503222
[research_haddad_2019]: https://doi.org/10.1121/1.5136641
[research_haefner_2026]: https://doi.org/10.2514/1.c038360
[research_haftka_1977]: https://doi.org/10.2514/3.7400
[research_haftka_grossman_1987]: https://ntrs.nasa.gov/citations/19930074238
[research_hai_2025]: https://doi.org/10.1121/10.0037814
[research_haider_2024]: https://doi.org/10.31181/rme313
[research_halimi_2019]: https://doi.org/10.1177/1475472x19859889
[research_hall_1961]: https://ntrs.nasa.gov/citations/19980228266
[research_hall_1974]: https://doi.org/10.2514/3.60377
[research_hall_2016]: https://doi.org/10.1121/1.4970324
[research_hall_boothe_1972]: https://doi.org/10.2514/3.58945
[research_hall_mason_2012]: https://doi.org/10.2514/6.2012-2482
[research_hall_rogan_1988]: https://ntrs.nasa.gov/citations/19880066527
[research_hall_rogan_1989]: https://ntrs.nasa.gov/citations/19890015788
[research_hall_yang_1994]: https://doi.org/10.2514/3.46569
[research_hambrey_feszty_2017]: https://doi.org/10.2514/6.2017-3917
[research_hamed_1993]: https://doi.org/10.21236/ada268106
[research_hamel_1970]: https://doi.org/10.2514/3.44215
[research_hammond_henderson_1961]: https://ntrs.nasa.gov/citations/19650014317
[research_hamory_murray_1993]: https://ntrs.nasa.gov/citations/19930013913
[research_hamza_2022]: https://doi.org/10.2139/ssrn.4089181
[research_han_2024]: https://doi.org/10.3390/s24175805
[research_han_barakos_2020]: https://doi.org/10.2514/1.c035978
[research_hancock_1972]: https://doi.org/10.1017/s0001924000044055
[research_handling_qualities_2000]: https://doi.org/10.2514/5.9781600866555.0119.0169
[research_handling_qualities_2008]: https://doi.org/10.1201/b15919-14
[research_hanin_barsony_nagy_1983]: https://doi.org/10.2514/3.8147
[research_hanks_1956]: https://doi.org/10.21236/ad0096084
[research_hansen_2022]: https://doi.org/10.2514/1.g006577
[research_hansmann_stumpf_2026]: https://doi.org/10.1007/s13272-026-00979-7
[research_hanson_1976]: https://doi.org/10.2514/6.1976-565
[research_hanson_1983]: https://doi.org/10.2514/3.60132
[research_hanson_1985]: https://doi.org/10.2514/3.8943
[research_hanson_1986]: https://doi.org/10.2514/6.1986-1892
[research_hanson_2014]: https://ntrs.nasa.gov/citations/20140005730
[research_hanson_2023]: https://doi.org/10.1016/j.jsv.2023.117751
[research_hanson_fink_1978]: https://ntrs.nasa.gov/citations/19780024890
[research_hanson_fink_1979]: https://doi.org/10.1016/0022-460x(79)90554-6
[research_hanson_magliozzi_1985]: https://doi.org/10.2514/3.45081
[research_hao_2023]: https://doi.org/10.3390/aerospace10060511
[research_haque_asrar_2016]: https://doi.org/10.1051/epjconf/201611402128
[research_hargest_1966]: https://doi.org/10.1016/0022-460x(66)90134-9
[research_hargest_1972]: https://doi.org/10.1016/0022-460x(72)90617-7
[research_harlamert_1974]: https://doi.org/10.4271/740359
[research_harman_1944]: https://ntrs.nasa.gov/citations/19930092577
[research_harnyoot_2018]: https://doi.org/10.2139/ssrn.3179421
[research_harper_robert_p_1955]: https://doi.org/10.21236/ad0092496
[research_harper_sardanowsky_1969]: https://doi.org/10.21236/ad0858184
[research_harris_1985]: https://doi.org/10.2514/3.45233
[research_harris_1996]: https://ntrs.nasa.gov/citations/19960047059
[research_harry_trobaugh_1966]: https://doi.org/10.21236/ad0641246
[research_hart_1956]: https://doi.org/10.21236/ad0108104
[research_hart_1984]: https://doi.org/10.2514/6.1984-2528
[research_hart_1992]: https://doi.org/10.2514/6.1992-4118
[research_hart_2016]: https://doi.org/10.1121/1.4950136
[research_hart_2021]: https://doi.org/10.1121/10.0005280
[research_hartmann_1976]: https://ntrs.nasa.gov/citations/19760010067
[research_harvey_oyoung_2016]: https://doi.org/10.1139/juvs-2015-0029
[research_harvey_oyoung_2018]: https://doi.org/10.3390/drones2010004
[research_hasan_2018]: https://doi.org/10.1108/ijius-02-2018-0004
[research_hasegawa_sakaue_2023]: https://doi.org/10.21203/rs.3.rs-3500881/v1
[research_hasegawa_sakaue_2024]: https://doi.org/10.1016/j.sna.2024.115273
[research_hashii_thompson_2018]: https://doi.org/10.2514/6.2018-2920
[research_hashim_2020]: https://doi.org/10.5373/jardcs/v12i7/20202025
[research_hawks_1982]: https://doi.org/10.2514/3.44751
[research_hay_1971]: https://doi.org/10.1016/0022-460x(71)90063-0
[research_hayes_1945]: https://doi.org/10.2514/8.11255
[research_he_2020]: https://doi.org/10.1109/access.2020.3012714
[research_he_2024]: https://doi.org/10.1109/access.2024.3415822
[research_he_2026]: https://doi.org/10.1007/s42401-026-00494-x
[research_he_2026_2]: https://doi.org/10.3390/s26061842
[research_he_ai_2018]: https://doi.org/10.1007/s11432-018-9580-3
[research_head_hohenemser_1951]: https://doi.org/10.21236/ad0109764
[research_healy_1958]: https://ntrs.nasa.gov/citations/20050028492
[research_healy_1969]: https://doi.org/10.1121/1.1972312
[research_healy_2022]: https://doi.org/10.2514/1.c036372
[research_hebbar_pashilkar_2016]: https://doi.org/10.14429/dsj.66.9196
[research_hebert_1973]: https://doi.org/10.21236/ad0766942
[research_hede_2017]: https://doi.org/10.4103/nah.nah_106_16
[research_hedrick_nichols_1975]: https://doi.org/10.2514/3.59905
[research_heidelberg_woodward_1989]: https://ntrs.nasa.gov/citations/19890011408
[research_heidenreich_1947]: https://doi.org/10.1109/t-aiee.1947.5059620
[research_heinrich_nietz_1964]: https://doi.org/10.21236/ad0600861
[research_heitman_mixson_1986]: https://doi.org/10.2514/3.45263
[research_helicopter_handling_1982]: https://ntrs.nasa.gov/citations/19820015334
[research_helicopter_yaw_1990]: https://doi.org/10.1108/eb036942
[research_heller_dobrzynski_1977]: https://doi.org/10.2514/3.58851
[research_henderson_1978]: https://doi.org/10.1175/1520-0477(1978)059<1136:uawrut>2.0.co;2
[research_henderson_2022]: https://doi.org/10.1016/j.tranpol.2022.06.006
[research_henderson_2023]: https://doi.org/10.3390/drones7010063
[research_hendrick_1977]: https://ntrs.nasa.gov/citations/19780011171
[research_henke_lammering_2010]: https://doi.org/10.2514/1.45785
[research_hennessy_2014]: https://ntrs.nasa.gov/citations/20150005309
[research_henriquez_huecas_2022]: https://doi.org/10.4050/jahs.67.032007
[research_henry_2023]: https://doi.org/10.1016/j.ast.2023.108645
[research_henryapearson_roberttjones_1976]: https://ntrs.nasa.gov/citations/19760011979
[research_henyey_2009]: https://doi.org/10.21236/ada531751
[research_herrmann_ben_asher_2016]: https://doi.org/10.2514/1.c033517
[research_hess_1977]: https://ntrs.nasa.gov/citations/19780011167
[research_hess_2012]: https://doi.org/10.2514/1.c031805
[research_hess_2016]: https://doi.org/10.1016/j.ifacol.2016.12.206
[research_hess_2018]: https://doi.org/10.2514/1.c034596
[research_hess_peng_2018]: https://doi.org/10.2514/1.c034497
[research_hewes_1959]: https://ntrs.nasa.gov/citations/19980228042
[research_heyson_1980]: https://ntrs.nasa.gov/citations/19800011749
[research_hicks_durbin_2014]: https://doi.org/10.21236/ada606506
[research_higbie_1995]: https://doi.org/10.1121/1.412907
[research_higgins_2020]: https://doi.org/10.2514/1.c035647
[research_higgins_jacobs_1928]: https://ntrs.nasa.gov/citations/19930091328
[research_higgins_shomber_1965]: https://doi.org/10.2514/3.43684
[research_high_altitude_1989]: https://doi.org/10.2514/6.1989-2109
[research_high_fidelity_aerodynamic_2015]: https://doi.org/10.1142/9781783266296_0008
[research_highland_2020]: https://doi.org/10.1139/juvs-2020-0011
[research_highspeed_waterbased_1953]: https://doi.org/10.1108/eb032259
[research_hightower_1985]: https://doi.org/10.21236/ada163129
[research_higuchi_1987]: https://doi.org/10.2514/3.9821
[research_hille_stumpf_2023]: https://doi.org/10.2514/6.2023-0211
[research_hillebrand_2025]: https://doi.org/10.2514/1.c038610
[research_hiller_aircraft_corp_palo_alto_ca_1956]: https://doi.org/10.21236/ad0127939
[research_hilton_1975]: https://ntrs.nasa.gov/citations/19750010159
[research_hilton_1975_2]: https://ntrs.nasa.gov/citations/19750009288
[research_hilton_connor_1975]: https://ntrs.nasa.gov/citations/19750010164
[research_hilton_connor_1975_b]: https://ntrs.nasa.gov/citations/19750010160
[research_hilton_henderson_1978]: https://doi.org/10.3397/1.2832093
[research_hilton_kasper_1974]: https://doi.org/10.1121/1.1914075
[research_hinds_shames_1975]: https://doi.org/10.21236/ada011449
[research_hiramatsu_2023]: https://doi.org/10.21810/aer.v1i1.5368
[research_hirschkron_1979]: https://doi.org/10.21236/ada089336
[research_hirschkron_1979_2]: https://doi.org/10.21236/ada089279
[research_hirschkron_1979_3]: https://doi.org/10.21236/ada089337
[research_hirschorn_1960]: https://doi.org/10.1121/1.2369426
[research_hirsh_1965]: https://doi.org/10.21236/ad0621684
[research_hitzel_zimper_2018]: https://doi.org/10.2514/1.c033696
[research_hjellvik_mallam_2024]: https://doi.org/10.1007/s10055-024-01058-0
[research_hodgson_guo_2006]: https://doi.org/10.1260/095745606777071036
[research_hoehne_1967]: https://doi.org/10.21236/ad0656486
[research_hoehne_hoffman_1961]: https://doi.org/10.21236/ad0256533
[research_hoelzen_2018]: https://doi.org/10.3390/en11010217
[research_hoerner_1936]: https://doi.org/10.1108/eb030033
[research_hoerner_1952]: https://doi.org/10.21236/ada800374
[research_hoff_1982]: https://doi.org/10.1121/1.388362
[research_hoffman_kennedy_1982]: https://doi.org/10.1121/1.387681
[research_hoh_1981]: https://doi.org/10.21236/ada100045
[research_hoh_mitchell_1983]: https://doi.org/10.21236/ada132857
[research_hohenwarter_2022]: https://doi.org/10.1051/aacus/2022005
[research_hoholis_2016]: https://doi.org/10.2514/1.c033642
[research_holberg_grabowsky_1981]: https://doi.org/10.2514/6.1981-2492
[research_holger_1980]: https://doi.org/10.3397/1.2832146
[research_holleman_gilyard_1972]: https://ntrs.nasa.gov/citations/19720014376
[research_holley_irving_b_1946]: https://doi.org/10.21236/ada529945
[research_hom_1983]: https://ntrs.nasa.gov/citations/19830035490
[research_homans_1978]: https://doi.org/10.21236/ada051999
[research_hopkins_1977]: https://doi.org/10.2514/3.58766
[research_hopkins_lovette_1977]: https://ntrs.nasa.gov/citations/19770013088
[research_horstmann_quast_1980]: https://ntrs.nasa.gov/citations/19800022879
[research_hoseini_hodges_2019]: https://doi.org/10.2514/1.c035098
[research_hosier_1976]: https://ntrs.nasa.gov/citations/19760007042
[research_hosier_1977]: https://ntrs.nasa.gov/citations/19770019976
[research_hosseini_2020]: https://doi.org/10.1177/0954410020923060
[research_hosseini_mesbahi_2016]: https://doi.org/10.2514/1.g001737
[research_hou_song_2024]: https://doi.org/10.1049/icp.2024.0623
[research_houbolt_1971]: https://doi.org/10.1007/978-1-4684-8346-8_26
[research_houck_moore_1977]: https://ntrs.nasa.gov/citations/19780005098
[research_houston_smith_1954]: https://doi.org/10.1037/e420302004-001
[research_howard_1977]: https://ntrs.nasa.gov/citations/19800006836
[research_howe_1978]: https://doi.org/10.1016/0022-460x(78)90391-7
[research_howe_1981]: https://doi.org/10.1016/0022-460x(81)90342-4
[research_howe_1999]: https://doi.org/10.21236/ada361764
[research_howell_1988]: https://doi.org/10.2514/6.1988-2185
[research_howie_brugger_2000]: https://doi.org/10.21236/ada377206
[research_howlett_1979]: https://doi.org/10.1121/1.2017963
[research_hoyos_jimenez_2021]: https://doi.org/10.1088/1742-6596/1733/1/012011
[research_hrishikeshavan_2015]: https://doi.org/10.2514/1.c032633
[research_hu_2022]: https://doi.org/10.2514/1.j061763
[research_hu_2025]: https://doi.org/10.3390/drones9090635
[research_hu_2026]: https://doi.org/10.1016/j.ast.2026.112874
[research_hu_2026_2]: https://doi.org/10.2514/1.j066674
[research_huang_2018]: https://doi.org/10.1177/1550147718755069
[research_huang_2023]: https://doi.org/10.3397/in_2023_1142
[research_huang_2023_2]: https://doi.org/10.54254/2753-8818/5/20230263
[research_huang_2023_4]: https://doi.org/10.1121/10.0020838
[research_huang_2025]: https://doi.org/10.3390/aerospace12020154
[research_huang_du_2026]: https://doi.org/10.54941/ahfe1007848
[research_huang_ghorbaniasl_2016]: https://doi.org/10.2514/6.2016-2874
[research_huang_pippalapalli_2006]: https://doi.org/10.2514/6.2006-446
[research_huang_wu_2006]: https://doi.org/10.2514/1.21144
[research_huang_yao_2020]: https://doi.org/10.2514/6.2020-2596
[research_hubbard_1993]: https://ntrs.nasa.gov/citations/19950058489
[research_hubner_strumpfel_2020]: https://doi.org/10.37544/1863-4672-2020-06-18
[research_huff_w_w_1949]: https://doi.org/10.21236/ad0035641
[research_hughes_gazzaniga_1988]: https://doi.org/10.2514/6.1988-3149
[research_hui_chen_2023]: https://doi.org/10.2514/1.i011183
[research_hukuda_1962]: https://doi.org/10.1299/kikai1938.28.966
[research_hultgren_2015]: https://ntrs.nasa.gov/citations/20150023070
[research_human_powered_aircraft_2014]: https://doi.org/10.1002/9781118534748.ch12
[research_human_reaction_1989]: https://doi.org/10.1017/cbo9780511584527.002
[research_humpert_gaeta_2015]: https://doi.org/10.2514/6.2015-2360
[research_humphreys_2016]: https://ntrs.nasa.gov/citations/20160009091
[research_humphreys_jennings_2020]: https://doi.org/10.3390/aerospace7050051
[research_hunn_1953]: https://doi.org/10.1017/s0368393100131128
[research_hunsaker_2020]: https://doi.org/10.2514/1.j059038
[research_hunsaker_montgomery_2020]: https://doi.org/10.2514/6.2020-1264
[research_hunsaker_moorthamers_2019]: https://doi.org/10.2514/6.2019-2917
[research_hunsaker_moorthamers_2021]: https://doi.org/10.1002/zamm.201900177
[research_hunter_1959]: https://ntrs.nasa.gov/citations/19980231993
[research_hunter_burke_1992]: https://doi.org/10.21236/ada253387
[research_hunton_james_harry_a_1948]: https://ntrs.nasa.gov/citations/20090026988
[research_hurley_1969]: https://doi.org/10.2514/3.44089
[research_hussain_dutilleux_2020]: https://doi.org/10.1121/1.5147110
[research_hutchins_1972]: https://doi.org/10.21236/ad0761199
[research_huzita_1971]: https://doi.org/10.2322/jjsass1969.19.378
[research_hwang_2016]: https://doi.org/10.5139/ijass.2016.17.1.132
[research_hwang_2016_2]: https://doi.org/10.20910/jase.2016.10.1.59
[research_hwang_pi_1978]: https://ntrs.nasa.gov/citations/19780063998
[research_hwang_pi_1979]: https://ntrs.nasa.gov/citations/19790054122
[research_ibren_2020]: https://doi.org/10.37934/cfdl.12.4.7989
[research_icke_baysal_2021]: https://doi.org/10.2514/6.2021-2283
[research_identification_method_2023]: https://doi.org/10.36652/0869-4931-2023-77-12-560-566
[research_iemma_2016]: https://doi.org/10.1515/noise-2016-0005
[research_iemma_2021]: https://doi.org/10.3397/in-2021-2203
[research_ignatyev_2019]: https://doi.org/10.1016/j.ifacol.2019.11.278
[research_iliff_maine_1984]: https://ntrs.nasa.gov/citations/19840012507
[research_iliff_wang_1996]: https://ntrs.nasa.gov/citations/19970004545
[research_iliff_wang_1997]: https://ntrs.nasa.gov/citations/19970010502
[research_iliff_wang_1999]: https://ntrs.nasa.gov/citations/19990019364
[research_in_flight_testing_2025]: https://doi.org/10.12968/s1478-2774(25)50117-5
[research_ingraham_2023]: https://doi.org/10.2514/6.2023-2039
[research_ingraham_gray_2019]: https://ntrs.nasa.gov/citations/20190027611
[research_ingram_1964]: https://doi.org/10.21236/ad0611173
[research_instruments_for_1999]: https://doi.org/10.1142/9781848160897_0005
[research_intano_howse_1991]: https://doi.org/10.21236/ada243594
[research_introduction_to_2021]: https://doi.org/10.1017/9781139094672.003
[research_ioannis_ioannis_2026]: https://doi.org/10.70322/dav.2026.10005
[research_iovnovich_2018]: https://doi.org/10.2514/1.c034716
[research_irmawan_eko_prasetiyo_2020]: https://doi.org/10.22146/jnteti.v9i1.142
[research_irsyad_lukman_agoes_moelyadi_2018]: https://doi.org/10.1088/1742-6596/1005/1/012050
[research_irvine_1968]: https://doi.org/10.21236/ad0680316
[research_irving_1999]: https://doi.org/10.1142/p045
[research_ishola_2024]: https://doi.org/10.3390/robotics13120179
[research_isikveren_2018]: https://doi.org/10.2514/1.c034355
[research_islam_2015]: https://doi.org/10.2316/journal.206.2015.2.206-3960
[research_israel_moguel_2015]: https://doi.org/10.4172/2168-9873.1000147
[research_ivankovic_2023]: https://doi.org/10.3390/aerospace10030315
[research_ivey_1945]: https://ntrs.nasa.gov/citations/19930092785
[research_ivler_2022]: https://doi.org/10.4050/jahs.67.012002
[research_izquierdo_2017]: https://doi.org/10.3390/s18010025
[research_jack_hoffler_2014]: https://ntrs.nasa.gov/citations/20140011502
[research_jackson_1993]: https://ntrs.nasa.gov/citations/19930069741
[research_jacobs_1983]: https://ntrs.nasa.gov/citations/19850007386
[research_jacobs_bartlett_1981]: https://ntrs.nasa.gov/citations/19810010483
[research_jacobson_joshi_1977]: https://doi.org/10.2514/3.44591
[research_jacobson_joshi_1978]: https://doi.org/10.2514/3.58351
[research_jacques_1976]: https://doi.org/10.1016/0022-460x(76)90736-7
[research_jager_2021]: https://doi.org/10.1515/noise-2021-0007
[research_james_1975]: https://doi.org/10.1017/s0022112075002339
[research_james_vaughn_1976]: https://doi.org/10.1016/0010-4361(76)90016-1
[research_jamison_1966]: https://doi.org/10.1108/eb034204
[research_janakiram_1980]: https://doi.org/10.21236/ada088325
[research_janakiram_scruggs_1982]: https://doi.org/10.2514/3.44811
[research_jang_ahn_2022]: https://doi.org/10.3390/app12199436
[research_januszewska_pringle_2021]: https://doi.org/10.7901/2169-3358-2021.1.1141599
[research_janzen_precourt_1989]: https://doi.org/10.21236/ada213513
[research_jaron_2023]: https://doi.org/10.3397/in_2023_1064
[research_jategaonkar_2023]: https://doi.org/10.61653/joast.v57i1.2005.674
[research_jayalakshmi_patel_2021]: https://doi.org/10.14429/dsj.71.15347
[research_jeff_berton]: https://ntrs.nasa.gov/citations/20210015845
[research_jeffery_1977]: https://doi.org/10.2514/3.58846
[research_jekaterynczuk_2025]: https://doi.org/10.3390/app15105378
[research_jekaterynczuk_piotrowski_2025]: https://doi.org/10.3390/s25227057
[research_jenke_1976]: https://doi.org/10.21236/ada027027
[research_jenney_1979]: https://doi.org/10.21236/ada080133
[research_jennifer_fowler]: https://ntrs.nasa.gov/citations/20230018434
[research_jennings_1931]: https://doi.org/10.1108/eb029462
[research_jentys_breitsamter_2023]: https://doi.org/10.1016/j.ast.2023.108652
[research_jeong_2015]: https://doi.org/10.2514/1.c032747
[research_jeong_2022]: https://doi.org/10.5139/jksas.2022.50.7.471
[research_jeong_2023]: https://doi.org/10.3397/in_2023_0536
[research_jeong_2024]: https://doi.org/10.5302/j.icros.2024.23.0206
[research_jeracki_mitchell_1981]: https://ntrs.nasa.gov/citations/19810058354
[research_jernell_1978]: https://ntrs.nasa.gov/citations/19780017136
[research_jewell_1979]: https://doi.org/10.2514/3.58536
[research_ji_2017]: https://doi.org/10.2514/1.c033667
[research_ji_2022]: https://doi.org/10.1016/j.ast.2022.107501
[research_ji_2023]: https://doi.org/10.3390/aerospace10040365
[research_jia_lee_2022]: https://doi.org/10.4050/jahs.67.012009
[research_jiang_1999]: https://doi.org/10.4271/1999-01-5618
[research_jiang_an_2000]: https://doi.org/10.2514/6.2000-4324
[research_jianhong_yanxiang_2026]: https://doi.org/10.1108/aeat-01-2025-0009
[research_jiao_2022]: https://doi.org/10.3390/drones6110324
[research_jimenez_2016]: https://doi.org/10.15394/ijaaa.2016.1118
[research_jin_2024]: https://doi.org/10.54097/xv395z51
[research_jin_lee_2015]: https://doi.org/10.5139/ijass.2015.16.2.311
[research_jing_ma_2025]: https://doi.org/10.1108/aeat-01-2024-0025
[research_jing_ye_2021]: https://doi.org/10.21595/jve.2021.21888
[research_jobe_1984]: https://doi.org/10.21236/ada326842
[research_joel_b_lonzaga]: https://ntrs.nasa.gov/citations/20230006744
[research_joel_b_lonzaga_2]: https://ntrs.nasa.gov/citations/20220009972
[research_johannes_1971]: https://doi.org/10.1007/978-1-4684-8346-8_28
[research_johansson_2023]: https://doi.org/10.25144/14535
[research_johnnie_a_ham_1993]: https://ntrs.nasa.gov/citations/19940008851
[research_johnson_1949]: https://ntrs.nasa.gov/citations/20090026465
[research_johnson_1972]: https://ntrs.nasa.gov/citations/19720014357
[research_johnson_1972_2]: https://doi.org/10.21236/ad0754909
[research_johnson_1975]: https://doi.org/10.2514/6.1975-1048
[research_johnson_anderson_1966]: https://doi.org/10.21236/ada951585
[research_johnson_hagerman_1950]: https://ntrs.nasa.gov/citations/19930082848
[research_johnson_sternfield_1948]: https://ntrs.nasa.gov/citations/19930082416
[research_johnston_1965]: https://ntrs.nasa.gov/citations/19650018345
[research_johnston_1965_2]: https://doi.org/10.21236/ad0622578
[research_johnston_1974]: https://doi.org/10.21236/ada014366
[research_johnston_donham_1982]: https://doi.org/10.2514/3.61568
[research_jolley_1970]: https://doi.org/10.21236/ad0706764
[research_jonathan_s_litt_2022]: https://ntrs.nasa.gov/citations/20210026061
[research_jones_1946]: https://ntrs.nasa.gov/citations/19930084600
[research_jones_1950]: https://ntrs.nasa.gov/citations/19760012005
[research_jones_1950_2]: https://doi.org/10.2514/8.1517
[research_jones_1964]: https://ntrs.nasa.gov/citations/19640042175
[research_jones_1965]: https://doi.org/10.21236/ad0637744
[research_jones_1970]: https://doi.org/10.21236/ad0880948
[research_jones_1976]: https://doi.org/10.2514/3.44558
[research_jones_2013]: https://ntrs.nasa.gov/citations/20140008926
[research_joo_hwang_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000777
[research_jovanovic_2022]: https://doi.org/10.2139/ssrn.4135995
[research_jovanovic_2023]: https://doi.org/10.1016/j.jairtraman.2023.102405
[research_jovanovic_novak_2022]: https://doi.org/10.1121/10.0015773
[research_jovanovic_novak_2022_2]: https://doi.org/10.1121/10.0015775
[research_ju_2026]: https://doi.org/10.1016/j.rineng.2026.112210
[research_juhasz_2022]: https://doi.org/10.4050/jahs.67.022003
[research_jung_2025]: https://doi.org/10.2514/1.c038132
[research_jurczyk_2018]: https://doi.org/10.2478/sjpna-2018-0001
[research_juricka_jurickova_2020]: https://doi.org/10.35116/aa.2020.0002
[research_justiz_patel_1988]: https://ntrs.nasa.gov/citations/19880066423
[research_kacik_goetzendorf_grabowski_2025]: https://doi.org/10.1108/aeat-02-2025-0045
[research_kadyrov_2022]: https://doi.org/10.1121/10.0010579
[research_kafali_guclu_2023]: https://doi.org/10.1108/aeat-04-2023-0100
[research_kai_2024]: https://doi.org/10.2514/1.g007917
[research_kakade_chikkala_2022]: https://doi.org/10.1149/10701.0493ecst
[research_kaldschmidt_syltebo_1973]: https://ntrs.nasa.gov/citations/19740009642
[research_kallergis_1987]: https://doi.org/10.3397/1.2827688
[research_kamrath_2016]: https://doi.org/10.1121/1.4949788
[research_kamrath_2022]: https://doi.org/10.1121/10.0015532
[research_kaneko_martins_2023]: https://doi.org/10.2514/1.c036921
[research_kang_choi_2022]: https://doi.org/10.1007/s42405-021-00425-4
[research_kang_woolsey_2020]: https://doi.org/10.1016/j.ast.2020.106030
[research_kant_2023]: https://doi.org/10.1109/tai.2022.3153763
[research_kao_1974]: https://doi.org/10.2514/3.60345
[research_kapnik_2019]: https://doi.org/10.25172/jalc.84.4.4
[research_kapoor_2021]: https://doi.org/10.3390/atmos12111424
[research_kaptsov_rodrigues_2018]: https://doi.org/10.2514/1.g002806
[research_karimian_paruchuri_2023]: https://doi.org/10.2514/6.2023-3655
[research_karimian_paruchuri_2023_b]: https://doi.org/10.2514/6.2023-3219
[research_karpel_1990]: https://doi.org/10.2514/3.25281
[research_karpuk_mosca_2024]: https://doi.org/10.2514/1.c037744
[research_kartashov_2021]: https://doi.org/10.30837/rt.2021.3.206.11
[research_kashitani_2019]: https://doi.org/10.1299/jsmedmc.2019.446
[research_kato_2018]: https://doi.org/10.1299/jsmecmd.2018.31.162
[research_katz_1989]: https://ntrs.nasa.gov/citations/19890060001
[research_katz_2017]: https://doi.org/10.2514/1.c034373
[research_katz_levin_1986]: https://doi.org/10.2514/3.45386
[research_katz_maskew_1988]: https://doi.org/10.2514/3.45564
[research_kayser_2024]: https://doi.org/10.3397/in_2024_3262
[research_kayten_koven_1945]: https://ntrs.nasa.gov/citations/19930092456
[research_ke_zheng_2016]: https://doi.org/10.1016/j.jsv.2016.01.034
[research_keast_1961]: https://doi.org/10.21236/ad0273892
[research_keener_1985]: https://doi.org/10.2514/3.45163
[research_keenohan_1942]: https://doi.org/10.1111/j.1949-8594.1942.tb05689.x
[research_kehoe_ellison_1985]: https://ntrs.nasa.gov/citations/19850024805
[research_keilman_2019]: https://doi.org/10.5703/1288284316930
[research_keles_2022]: https://doi.org/10.2139/ssrn.4113879
[research_keller_2019]: https://doi.org/10.1007/s13272-019-00396-z
[research_kellermann_2020]: https://doi.org/10.3390/aerospace8010003
[research_kelley_1990]: https://ntrs.nasa.gov/citations/19910032671
[research_kelley_enevoldson_1981]: https://ntrs.nasa.gov/citations/19820005275
[research_kelley_phelps_1986]: https://ntrs.nasa.gov/citations/19860000179
[research_kellogg_1946]: https://doi.org/10.1037/h0060547
[research_kelly_1988]: https://doi.org/10.2514/6.1988-2129
[research_kelly_1993]: https://ntrs.nasa.gov/citations/19930046469
[research_kelly_brown_1980]: https://ntrs.nasa.gov/citations/19800020867
[research_kelly_wilson_1995]: https://doi.org/10.2514/3.46830
[research_kemp_1943]: https://ntrs.nasa.gov/citations/19930092931
[research_kennelly_1990]: https://ntrs.nasa.gov/citations/19920022969
[research_kenny_2004]: https://ntrs.nasa.gov/citations/20050186644
[research_kensche_2003]: https://doi.org/10.2514/6.2003-2778
[research_kentfield_2012]: https://doi.org/10.2514/6.2012-3207
[research_keshavan_1980]: https://doi.org/10.2514/3.44661
[research_keshavarz_ohadi_2017]: https://doi.org/10.1016/j.apm.2017.05.022
[research_keskin_2021]: https://doi.org/10.1108/aeat-02-2021-0054
[research_keskin_2026]: https://doi.org/10.1108/aeat-04-2026-0122
[research_kester_1974]: https://ntrs.nasa.gov/citations/19750034462
[research_key_1971]: https://doi.org/10.21236/ad0725746
[research_key_1982]: https://doi.org/10.2514/3.57366
[research_keyel_2017]: https://doi.org/10.1016/j.envsoft.2017.07.008
[research_khalil_2022]: https://doi.org/10.2514/1.c036426
[research_khalil_bauknecht_2024]: https://doi.org/10.2514/1.c037503
[research_khalil_fezans_2020]: https://doi.org/10.1017/aer.2020.85
[research_khan_padhy_2019]: https://doi.org/10.15406/fmrij.2019.03.00053
[research_khanna_2022]: https://doi.org/10.1108/aeat-08-2021-0231
[research_kheiri_riazat_2025]: https://doi.org/10.1017/aer.2025.10028
[research_kholodar_2016]: https://doi.org/10.2514/1.c033772
[research_kholyavko_1971]: https://doi.org/10.1007/bf01019800
[research_khorrami_2009]: https://ntrs.nasa.gov/citations/20090020451
[research_khuat_2025]: https://doi.org/10.55248/gengpi.6.0325.1229
[research_kiang_1971]: https://doi.org/10.1007/978-1-4684-8346-8_6
[research_kibbee_1978]: https://ntrs.nasa.gov/citations/19780012175
[research_kida_1982]: https://doi.org/10.1002/zamm.19820620912
[research_kida_miyai_1978]: https://doi.org/10.1017/s0001925900008477
[research_kidd_bull_1963]: https://doi.org/10.21236/ad0400265
[research_kier_1972]: https://ntrs.nasa.gov/citations/19730024215
[research_kigotho_bodylski_2022]: https://doi.org/10.2514/1.c036582
[research_kilgore_averett_1964]: https://doi.org/10.2514/3.43598
[research_kilimtzidis_kostopoulos_2023]: https://doi.org/10.3390/aerospace10030251
[research_kim]: https://doi.org/10.14711/thesis-991013106347603412
[research_kim_2016]: https://doi.org/10.1121/1.4969770
[research_kim_2020]: https://doi.org/10.2514/1.i010763
[research_kim_2022_2]: https://doi.org/10.1080/10447318.2022.2087662
[research_kim_2022_3]: https://doi.org/10.5139/jksas.2022.50.7.489
[research_kim_2022_4]: https://doi.org/10.5139/jksas.2022.50.7.479
[research_kim_2025]: https://doi.org/10.2514/1.c038270
[research_kim_2025_2]: https://doi.org/10.12985/ksaa.2025.33.2.061
[research_kim_2025_3]: https://doi.org/10.1007/s12206-025-0410-3
[research_kim_2025_4]: https://doi.org/10.1121/10.0037186
[research_kim_2025_5]: https://doi.org/10.5762/kais.2025.26.7.451
[research_kim_atkins_2022]: https://doi.org/10.3390/app12020576
[research_kim_jeong_2026]: https://doi.org/10.47116/apjcri.2026.07.24
[research_kim_kim_2020]: https://doi.org/10.12985/ksaa.2020.28.1.075
[research_kimathi_lantos_2023]: https://doi.org/10.3311/ppee.21948
[research_kingan_2023]: https://doi.org/10.1016/j.jsv.2023.117894
[research_kingan_parry_2020]: https://doi.org/10.1017/jfm.2020.504
[research_kingan_self_2009]: https://doi.org/10.2514/6.2009-3135
[research_kirby_2021]: https://doi.org/10.1121/10.0004407
[research_kirby_2021_2]: https://doi.org/10.1121/10.0003567
[research_kirby_2022]: https://doi.org/10.1121/10.0015615
[research_kirsch_2020]: https://doi.org/10.1016/j.jfluidstructs.2020.102930
[research_kisabo_2017]: https://doi.org/10.3844/jastsp.2017.18.29
[research_kistyarev_wang_2025]: https://doi.org/10.1007/s42496-025-00249-5
[research_kizer_1977]: https://doi.org/10.21236/ada057928
[research_klein_1982]: https://doi.org/10.1016/s1474-6670(17)63154-9
[research_klein_1983]: https://doi.org/10.2514/3.44895
[research_klein_krainski_2017]: https://doi.org/10.4050/sm_2017_hq-1572
[research_klemin_walling_1943]: https://doi.org/10.2514/8.11033
[research_kletschkowski_2012]: https://doi.org/10.1007/978-94-007-2537-9_13
[research_kloet_2017]: https://doi.org/10.1177/1756829316681868
[research_klug_2023]: https://doi.org/10.1007/s13272-023-00645-2
[research_knott_1974]: https://doi.org/10.21236/ad0786467
[research_knowd_1982]: https://doi.org/10.1121/1.387258
[research_ko_1971]: https://doi.org/10.1121/1.1912784
[research_ko_1975]: https://doi.org/10.1016/s0022-460x(75)80142-8
[research_ko_1975_2]: https://doi.org/10.1016/s0022-460x(75)80250-1
[research_ko_1979]: https://doi.org/10.1016/0022-460x(79)90027-0
[research_ko_2026]: https://doi.org/10.1016/j.ast.2025.110878
[research_koch_1998]: https://ntrs.nasa.gov/citations/19980017535
[research_kochersberger_player_2003]: https://doi.org/10.2514/6.2003-96
[research_kochuk_2021]: https://doi.org/10.32620/aktt.2021.6.02
[research_kocur_2023]: https://doi.org/10.2139/ssrn.4390738
[research_kodji_2023]: https://doi.org/10.4103/nah.nah_1_23
[research_kodji_2024]: https://doi.org/10.1371/journal.pone.0307760
[research_kodres_2000]: https://doi.org/10.21236/ada380948
[research_koessler_2018]: https://doi.org/10.2514/6.2018-0019
[research_kohler_jeschke_2021]: https://doi.org/10.1007/s13272-021-00536-4
[research_kohlman_1977]: https://ntrs.nasa.gov/citations/19770019178
[research_kohne_korzilius_2024]: https://doi.org/10.2514/6.2024-81823
[research_komadina_drake_2002]: https://doi.org/10.2514/6.2002-519
[research_konar_2020]: https://doi.org/10.1108/aeat-11-2019-0229
[research_kone_ghinet_2023]: https://doi.org/10.3397/in_2023_0463
[research_kone_ghinet_2024]: https://doi.org/10.3397/nc_2024_0154
[research_kone_ghinet_2024_b]: https://doi.org/10.3397/in_2024_3084
[research_konert_kasprzyk_2024]: https://doi.org/10.1007/s10846-024-02084-5
[research_konig_2024]: https://doi.org/10.1121/10.0028514
[research_koopmann_1976]: https://doi.org/10.1016/0022-460x(76)90688-x
[research_kopecki_2016]: https://doi.org/10.1108/aeat-10-2012-0187
[research_koper_1976]: https://doi.org/10.1117/12.954798
[research_kordan_vonlavante_1985]: https://doi.org/10.2514/6.1985-2
[research_korsun_2017]: https://doi.org/10.1016/j.procs.2017.01.017
[research_korsun_2018]: https://doi.org/10.1088/1757-899x/312/1/012015
[research_korsun_2024]: https://doi.org/10.31857/s0002338824030066
[research_korsun_moung_htang_2023]: https://doi.org/10.3934/mina.2024003
[research_kotitschke_2026]: https://doi.org/10.1007/s42401-026-00498-7
[research_kotwiczherniczek]: https://doi.org/10.22215/etd/2017-12146
[research_kou_2021]: https://doi.org/10.1109/tte.2021.3068724
[research_kourbatski_2024]: https://doi.org/10.1177/1475472x241230646
[research_kowalska_goetzendorfgrabowski_2022]: https://doi.org/10.1108/aeat-01-2022-0001
[research_kozak_2021]: https://doi.org/10.20535/2617-0965.eae.228902
[research_kozakiewicz_grzegorczyk_2021]: https://doi.org/10.2478/jok-2021-0044
[research_kozeruk_korzhik_2022]: https://doi.org/10.20535/radap.2022.89.29-38
[research_kozeruk_korzhyk_2019]: https://doi.org/10.20535/radap.2019.76.15-20
[research_kozhanov_2022]: https://doi.org/10.52348/2712-8873_mmtt_2022_5_45
[research_kozupa_2023]: https://doi.org/10.3397/in_2023_0131
[research_kraft_1985]: https://doi.org/10.1016/s1474-6670(17)60918-2
[research_krawczyk_2024]: https://doi.org/10.2514/1.c037420
[research_kraxberger_2024]: https://doi.org/10.3397/in_2024_3224
[research_krebs_bramesfeld_2016]: https://doi.org/10.1017/aer.2016.83
[research_krebs_bramesfeld_2017]: https://doi.org/10.2514/6.2017-4090
[research_kretov_tiniakov_2022]: https://doi.org/10.3390/aerospace9090497
[research_kriebel_1964]: https://doi.org/10.2514/3.43582
[research_kriebel_1972]: https://doi.org/10.1121/1.1912816
[research_kriechbaum_stineman_1972]: https://doi.org/10.2514/3.58994
[research_krishnamurthy_rizzi_2022]: https://doi.org/10.3397/nc-2022-676
[research_krishnan_2020]: https://doi.org/10.2514/1.c035680
[research_kristl_1999]: https://doi.org/10.21236/ada388763
[research_krivosheikin_perelygin_2015]: https://doi.org/10.17586/0021-3454-2015-58-3-221-225
[research_kroo_2000]: https://doi.org/10.2514/6.2000-4336
[research_kruger_uranga_2024]: https://doi.org/10.2514/1.c037284
[research_kryter_1966]: https://doi.org/10.1126/science.151.3716.1346
[research_kryter_1967]: https://doi.org/10.1016/0022-460x(67)90116-2
[research_kryter_1982]: https://doi.org/10.1121/1.388332
[research_kryter_williams_1966]: https://doi.org/10.1121/1.1909862
[research_krzywoblocki_1943]: https://doi.org/10.2514/8.11023
[research_kuantama_2019]: https://doi.org/10.1177/1461348419866292
[research_kubrynski_1999]: https://doi.org/10.1007/978-3-322-89952-1_3
[research_kubrynski_2012]: https://doi.org/10.2514/6.2012-2662
[research_kuettner_1952]: https://doi.org/10.21236/ad0012012
[research_kuhlman_1979]: https://ntrs.nasa.gov/citations/19790015753
[research_kuhlman_liaw_1987]: https://ntrs.nasa.gov/citations/19870061823
[research_kuhlmann_romerostarke_2024]: https://doi.org/10.3397/in_2024_3394
[research_kuhn_1975]: https://doi.org/10.21236/ada955472
[research_kukreja_2008]: https://doi.org/10.2514/1.32799
[research_kulba_2021]: https://doi.org/10.37701/dndivsovt.10.2021.12
[research_kulhanek_2019]: https://doi.org/10.1108/aeat-06-2018-0162
[research_kull_finegold_2024]: https://doi.org/10.25144/21510
[research_kumar_1997]: https://doi.org/10.21236/ada398405
[research_kumar_2025]: https://doi.org/10.55248/gengpi.6.0225.0726
[research_kumar_2025_2]: https://doi.org/10.55248/gengpi.6.0225.0762
[research_kumar_ghosh_2018]: https://doi.org/10.15866/irease.v11i6.14521
[research_kumar_ghosh_2023]: https://doi.org/10.61653/joast.v66i4.2014.481
[research_kumar_ghosh_2023_2]: https://doi.org/10.1108/aeat-09-2019-0179
[research_kumar_mathi_2026]: https://doi.org/10.2139/ssrn.6300265
[research_kumar_s_rajanikanth_2024]: https://doi.org/10.21275/sr24125030857
[research_kumari_raghunath_2016]: https://doi.org/10.18535/ijecs/v5i6.05
[research_kuppuswamy_kiran_1981]: https://doi.org/10.2514/6.1981-2381
[research_kurbjun_1959]: https://ntrs.nasa.gov/citations/19980228220
[research_kurdyla_1963]: https://doi.org/10.21236/ad0434421
[research_kutney_piszkin_1964]: https://doi.org/10.2514/3.43551
[research_kuzniar_orkisz_2019]: https://doi.org/10.2478/kones-2019-0036
[research_kyi_feng_2026]: https://doi.org/10.1016/j.urbmob.2026.100231
[research_kyrpenko_2015]: https://doi.org/10.15561/18189172.2015.0602
[research_la_cour_harbo_2018]: https://doi.org/10.1007/s10846-018-0853-1
[research_ladeira_2024]: https://doi.org/10.1177/03064190241283914
[research_lagemann_2024]: https://doi.org/10.1038/s41467-024-49361-3
[research_laine_1982]: https://doi.org/10.2514/3.57454
[research_laitone_1983]: https://doi.org/10.2514/3.44910
[research_laitone_1994]: https://doi.org/10.2514/3.46639
[research_laly_2023]: https://doi.org/10.3397/in_2022_0054
[research_lamar_1981]: https://doi.org/10.2514/3.57490
[research_lamp_luckner_2013]: https://doi.org/10.1007/978-3-642-38253-6_29
[research_lampton_2024]: https://doi.org/10.2514/1.g008058
[research_landers_lacoss_1978]: https://doi.org/10.1121/1.2004395
[research_landman_2017]: https://doi.org/10.1177/0018720817723428
[research_landman_2020]: https://doi.org/10.1080/24721840.2020.1763798
[research_landmann_1989]: https://ntrs.nasa.gov/citations/19900005550
[research_lang_1981]: https://doi.org/10.2514/6.1981-2416
[research_lang_2022]: https://doi.org/10.1007/s42401-022-00156-8
[research_lang_2024]: https://doi.org/10.25144/22842
[research_lang_2025]: https://doi.org/10.1109/taes.2025.3571683
[research_lange_gieseler_1953]: https://doi.org/10.21236/ad0015004
[research_langer_blech_2019]: https://doi.org/10.1002/pamm.201900388
[research_lapygin_tret_yakov_1986]: https://doi.org/10.1007/bf01409732
[research_large_1975]: https://doi.org/10.1108/eb035260
[research_large_pesyridis_2018]: https://doi.org/10.20944/preprints201810.0608.v1
[research_larrabee_1974]: https://doi.org/10.2514/6.1974-1004
[research_larrabee_1975]: https://ntrs.nasa.gov/citations/19760003917
[research_lauber_1967]: https://doi.org/10.1016/0022-460x(67)90114-9
[research_lauchle_park_2002]: https://doi.org/10.21236/ada408916
[research_lauk_seegel_2017]: https://doi.org/10.3846/16487788.2017.1415228
[research_lauk_unt_2015]: https://doi.org/10.3846/16487788.2015.1104793
[research_lazos_visser_2006]: https://ntrs.nasa.gov/citations/20060045566
[research_le_clainche_2019]: https://doi.org/10.2514/1.c034863
[research_leahy_2015]: https://doi.org/10.1007/s10514-015-9519-z
[research_lechner_2021]: https://doi.org/10.1051/aacus/2021005
[research_ledegang_groen_2015]: https://doi.org/10.1080/10508414.2015.1131085
[research_lee_2017]: https://doi.org/10.2514/1.g001742
[research_lee_2017_2]: https://doi.org/10.5139/ijass.2017.18.4.651
[research_lee_2019]: https://doi.org/10.1109/aero.2019.8741667
[research_lee_2020_2]: https://doi.org/10.1007/s12555-018-9403-7
[research_lee_2021]: https://doi.org/10.12985/ksaa.2021.29.4.028
[research_lee_2022]: https://doi.org/10.2514/1.c036214
[research_lee_2022_2]: https://doi.org/10.12985/ksaa.2022.30.2.044
[research_lee_2023]: https://doi.org/10.5139/jksas.2023.51.3.183
[research_lee_2025]: https://doi.org/10.1109/access.2025.3632030
[research_lee_2026]: https://doi.org/10.1121/10.0042757
[research_lee_ko_2025]: https://doi.org/10.31818/jknst.2025.12.8.4.803
[research_lee_lee_2026]: https://doi.org/10.1007/s12555-026-00142-2
[research_lee_motsinger_1975]: https://doi.org/10.3397/1.2832000
[research_lee_sutherland_1976]: https://doi.org/10.21236/ada031058
[research_lee_yee_2024]: https://doi.org/10.2514/1.c037225
[research_legriffon_bertsch_2023]: https://doi.org/10.25144/14610
[research_lei_liu_2019]: https://doi.org/10.1016/j.mechatronics.2019.06.008
[research_leishman_1966]: https://doi.org/10.21236/ad0638632
[research_lempert_1975]: https://doi.org/10.21236/ada004190
[research_lendraitis_2019]: https://doi.org/10.5755/j01.mech.25.4.22325
[research_leng]: https://doi.org/10.70675/3f7f5214z94b2z4e05z848fzc56f908e8d81
[research_lennart_s_hultgren_2020]: https://ntrs.nasa.gov/citations/20205008042
[research_leong_chee_hang_2022]: https://doi.org/10.37934/arfmts.96.1.8295
[research_leonidov_2025]: https://doi.org/10.22488/okstate.26.100218
[research_lerbs_1955]: https://doi.org/10.21236/ad0076232
[research_leroux_bosman_2025]: https://doi.org/10.2139/ssrn.5760782
[research_lester_fuller_1986]: https://ntrs.nasa.gov/citations/19860060704
[research_letcher_1995]: https://doi.org/10.21236/ada299647
[research_leth_samuelsson_1998]: https://doi.org/10.2514/6.1998-2283
[research_letica_rizzi_2024]: https://doi.org/10.3397/nc_2024_0035
[research_level_flight_2003]: https://doi.org/10.2514/5.9781600861840.0083.0096
[research_levi_nelson_1964]: https://doi.org/10.2514/3.43579
[research_levin_katz_1984]: https://doi.org/10.2514/3.48218
[research_levinsky_1968]: https://doi.org/10.21236/ad0680969
[research_levison_1982]: https://doi.org/10.2514/3.57394
[research_levy_1992]: https://doi.org/10.2514/6.1992-4193
[research_lewis_1929]: https://doi.org/10.1109/jaiee.1929.6535434
[research_lewis_1930]: https://doi.org/10.1109/t-aiee.1930.5055462
[research_leylek_costello_2010]: https://doi.org/10.2514/6.2010-7507
[research_leylek_costello_2015]: https://doi.org/10.2514/1.c033056
[research_li_1981]: https://doi.org/10.21236/ada112945
[research_li_2019]: https://doi.org/10.1139/juvs-2018-0022
[research_li_2020]: https://doi.org/10.1109/access.2020.3041445
[research_li_2021]: https://doi.org/10.3397/in-2021-1488
[research_li_2022]: https://doi.org/10.1108/aeat-11-2021-0351
[research_li_2022_3]: https://doi.org/10.3390/drones6030078
[research_li_2022_5]: https://doi.org/10.2514/1.c036413
[research_li_2023]: https://doi.org/10.3390/pr11020542
[research_li_2023_2]: https://doi.org/10.3397/in_2023_0446
[research_li_2023_4]: https://doi.org/10.3390/aerospace10070603
[research_li_2024]: https://doi.org/10.3390/aerospace11121015
[research_li_2025]: https://doi.org/10.1088/1742-6596/3044/1/012002
[research_li_2025_2]: https://doi.org/10.2514/1.d0391
[research_li_2026]: https://doi.org/10.1016/j.ast.2025.111519
[research_li_daronch_2025]: https://doi.org/10.2514/6.2025-3094
[research_li_qi_2022]: https://doi.org/10.1049/icp.2022.1715
[research_li_qin_2020]: https://doi.org/10.1016/j.ast.2019.105622
[research_li_qin_2021]: https://doi.org/10.1016/j.jfluidstructs.2021.103407
[research_li_qin_2022]: https://doi.org/10.3390/app122010537
[research_li_rodrigues_2025]: https://doi.org/10.23919/ecc65951.2025.11187156
[research_li_yang_2017]: https://doi.org/10.2514/1.c033670
[research_li_yang_2017_2]: https://doi.org/10.2514/1.c034293
[research_li_yuan_2024]: https://doi.org/10.3390/pr12102186
[research_liang_2026]: https://doi.org/10.1360/ssi-2025-0330
[research_lichota_2017]: https://doi.org/10.2514/1.c033794
[research_lichota_2023]: https://doi.org/10.1108/aeat-01-2023-0013
[research_lichtenstein_1952]: https://ntrs.nasa.gov/citations/19930083215
[research_lichtenstein_williams_1961]: https://ntrs.nasa.gov/citations/19980227800
[research_lieberman_hoffman_1964]: https://doi.org/10.21236/ad0607666
[research_light_aircraft_1993]: https://doi.org/10.2514/6.1993-4443
[research_likhite_2022]: https://doi.org/10.55041/ijsrem16477
[research_lilla_2025]: https://doi.org/10.1007/s13272-025-00870-x
[research_lilley_2004]: https://doi.org/10.2514/6.2004-2922
[research_lilley_2006]: https://doi.org/10.2514/6.2006-2842
[research_lim_2023]: https://doi.org/10.5762/kais.2023.24.12.452
[research_lim_2023_2]: https://doi.org/10.5762/kais.2023.24.12.204
[research_lim_2025_2]: https://doi.org/10.3390/s25061928
[research_lin_2007]: https://ntrs.nasa.gov/citations/20080008290
[research_lincke_2025]: https://doi.org/10.1051/aacus/2025053
[research_lincke_pieren_2024]: https://doi.org/10.1051/aacus/2024036
[research_lincke_pieren_2024_2]: https://doi.org/10.3397/in_2024_3459
[research_lindstedt_2019]: https://doi.org/10.2478/fas-2019-0005
[research_lindstrom_rebeske_1970]: https://doi.org/10.21236/ad0877594
[research_linehan_mohseni_2016]: https://doi.org/10.2514/1.c033766
[research_linnell_1963]: https://doi.org/10.21236/ad0408661
[research_lippisch_1930]: https://ntrs.nasa.gov/citations/19930094854
[research_lippisch_1935]: https://ntrs.nasa.gov/citations/19930094655
[research_litt_2012]: https://ntrs.nasa.gov/citations/20120015476
[research_little_russell_1976]: https://doi.org/10.1115/76-gt-116
[research_liu_1962]: https://doi.org/10.4050/jahs.7.2.10
[research_liu_1983]: https://ntrs.nasa.gov/citations/19830009259
[research_liu_2015_2]: https://doi.org/10.1016/j.cja.2014.12.013
[research_liu_2017_2]: https://doi.org/10.1016/j.ast.2017.10.006
[research_liu_2018_2]: https://doi.org/10.1109/access.2018.2814958
[research_liu_2018_3]: https://doi.org/10.1049/joe.2018.9016
[research_liu_2021]: https://doi.org/10.1080/08839514.2021.1922849
[research_liu_fan_2026]: https://doi.org/10.1016/j.isatra.2026.06.042
[research_liu_stumpf_2018]: https://doi.org/10.2514/1.c034296
[research_liu_sun_2016]: https://doi.org/10.1155/2016/1060574
[research_liu_zhang_2023]: https://doi.org/10.1002/aisy.202300420
[research_livescu_2016]: https://doi.org/10.2514/1.j055429
[research_lobanovskii_1983]: https://doi.org/10.1007/bf01090577
[research_lobitz_2023]: https://doi.org/10.3390/aerospace10110938
[research_lockard_2008]: https://ntrs.nasa.gov/citations/20080018593
[research_loewy_1963]: https://doi.org/10.4050/jahs.8.36
[research_loewy_sutton_1966]: https://doi.org/10.21236/ad0629646
[research_loffi_2021]: https://doi.org/10.15394/ijaaa.2021.1568
[research_lofthouse_cummings_2017]: https://doi.org/10.2514/1.c034045
[research_lohr_haines_2024]: https://doi.org/10.36001/phme.2024.v8i1.4040
[research_lomax_1948]: https://ntrs.nasa.gov/citations/19930082187
[research_lombaerts_2017]: https://doi.org/10.2514/1.g002525
[research_loomis_porter_1965]: https://doi.org/10.2514/3.43697
[research_loran_haworth]: https://ntrs.nasa.gov/citations/20240011252
[research_lorenz_1985]: https://doi.org/10.1002/oca.4660060206
[research_loth_boyle_1969]: https://doi.org/10.21236/ad0704502
[research_lotinga_2025]: https://doi.org/10.1038/s44384-024-00001-6
[research_lotinga_2025_2]: https://doi.org/10.1121/10.0039056
[research_loubeau_2021]: https://doi.org/10.26226/morressier.606f15dd30a2e980041f248f
[research_louis_louis_2020]: https://doi.org/10.1088/1757-899x/955/1/012034
[research_lourenco_1996]: https://doi.org/10.21236/ada310244
[research_lovell_stassi_1950]: https://ntrs.nasa.gov/citations/19930082798
[research_lowrance_smith_1996]: https://doi.org/10.21236/ada381746
[research_lu_2015]: https://doi.org/10.2514/1.g001247
[research_lu_2017]: https://doi.org/10.1016/j.dt.2016.11.001
[research_lu_2019]: https://doi.org/10.1109/access.2019.2956818
[research_lu_2025_3]: https://doi.org/10.3390/drones9040268
[research_lucas_1978]: https://doi.org/10.21236/adb028240
[research_ludeman_1979]: https://doi.org/10.21236/ada066995
[research_luderer_thielecke_2025]: https://doi.org/10.2514/1.c037946
[research_ludlow_2024]: https://doi.org/10.25144/19306
[research_lundberg_1937]: https://doi.org/10.1108/eb030250
[research_lundberg_1938]: https://doi.org/10.1108/eb030261
[research_lundry_1977]: https://doi.org/10.2514/3.44595
[research_lungu_lungu_2015]: https://doi.org/10.1002/asjc.1133
[research_lungu_lungu_2016]: https://doi.org/10.1016/j.neucom.2015.06.084
[research_luoma_1944]: https://ntrs.nasa.gov/citations/19930092838
[research_lupp_cesnik_2015]: https://doi.org/10.2514/6.2015-2242
[research_luqmanul_hakim_2018]: https://doi.org/10.1088/1742-6596/1005/1/012038
[research_lusardi_2023]: https://doi.org/10.4050/sm_2023_hq-1186
[research_lush_1950]: https://doi.org/10.1017/s0368393100121686
[research_luskin_1950]: https://doi.org/10.2514/8.1511
[research_lustig_1960]: https://doi.org/10.21236/ad0249771
[research_lux_landwehr_1980]: https://doi.org/10.1121/1.384665
[research_lv_2023]: https://doi.org/10.3397/in_2022_0366
[research_lvik_holden_2024]: https://doi.org/10.25144/22726
[research_lyon_pande_1971]: https://doi.org/10.1121/1.1977713
[research_lyu_2022]: https://doi.org/10.1155/2022/2490675
[research_lyu_liem_2020]: https://doi.org/10.1016/j.treng.2020.100035
[research_ma_1989]: https://doi.org/10.2514/3.45778
[research_ma_2019]: https://doi.org/10.3390/app9204236
[research_ma_2020]: https://doi.org/10.2514/1.c035581
[research_ma_2022]: https://doi.org/10.1016/j.ast.2022.107395
[research_ma_2022_2]: https://doi.org/10.3390/aerospace9110691
[research_ma_2024]: https://doi.org/10.1088/1361-6501/ad762d
[research_ma_2025_2]: https://doi.org/10.1061/jaeeez.aseng-5669
[research_ma_2025_3]: https://doi.org/10.2514/1.c038551
[research_ma_abouhamzeh_2023]: https://doi.org/10.2514/6.2023-2102
[research_ma_chen_2023]: https://doi.org/10.1051/sands/2023020
[research_ma_guo_2018]: https://doi.org/10.1108/aeat-08-2017-0183
[research_maccready_1962]: https://doi.org/10.1029/jz067i003p01041
[research_macdonald_schneider_2019]: https://doi.org/10.1080/09636412.2019.1551565
[research_macdonald_shepherd_2008]: https://doi.org/10.1109/aero.2008.4526555
[research_macey_1956]: https://doi.org/10.21236/ad0102197
[research_macgregor_1973]: https://doi.org/10.1016/s0022-460x(73)80356-6
[research_mack_2003]: https://doi.org/10.21236/ada413591
[research_mackie_lawrence_2019]: https://doi.org/10.69554/jjjb3489
[research_macklnnon_madden_1972]: https://doi.org/10.2514/3.59028
[research_macklnnon_madden_1972_2]: https://doi.org/10.2514/3.58960
[research_macmillan_1981]: https://doi.org/10.2514/6.1981-2350
[research_macneill_verstraete_2017]: https://doi.org/10.1017/aer.2017.32
[research_madelung_1923]: https://doi.org/10.4271/230030
[research_madureira_dealmeida_2026]: https://doi.org/10.26678/abcm.conem2026.con26-0122
[research_magee_taylor_1971]: https://doi.org/10.21236/ad0735733
[research_magee_taylor_1971_2]: https://doi.org/10.21236/ad0735632
[research_maglieri_hubbard_1975]: https://ntrs.nasa.gov/citations/19750052586
[research_magliozzi_1982]: https://doi.org/10.2514/3.57361
[research_magliozzi_1983]: https://doi.org/10.2514/6.1983-717
[research_mahak_2017]: https://doi.org/10.1177/1475472x16684702
[research_maikapar_1966]: https://doi.org/10.1016/0021-8928(66)90071-2
[research_majka_2015]: https://doi.org/10.3390/aerospace2020222
[research_malcom_1969]: https://doi.org/10.2514/3.59426
[research_malgoezar_2019]: https://doi.org/10.1177/1475472x19852952
[research_malik_2017]: https://doi.org/10.15632/jtam-pl.55.3.963
[research_malina_parsons_1941]: https://doi.org/10.21236/ada800514
[research_malisani_2021]: https://doi.org/10.1088/1757-899x/1024/1/012066
[research_mallik_2015]: https://doi.org/10.2514/1.c033096
[research_malmuth_1966]: https://doi.org/10.2514/3.3483
[research_malpica_lusardi_2013]: https://doi.org/10.21236/ada589936
[research_malvestuto_1950]: https://ntrs.nasa.gov/citations/19930091081
[research_mamada_ando_1974]: https://doi.org/10.2514/3.59236
[research_mamich_a_v_2025]: https://doi.org/10.36652/0869-4931-2025-79-11-514-519
[research_mandal_gu_2016]: https://doi.org/10.3390/aerospace3040042
[research_mangold_strohmayer_2025]: https://doi.org/10.3390/aerospace12040275
[research_manickam_2020]: https://doi.org/10.1177/0954410020943086
[research_maniet_jr_2001]: https://doi.org/10.21236/ada409180
[research_mansour_1985]: https://doi.org/10.2514/3.9056
[research_mao_zhao_1990]: https://doi.org/10.1016/s1474-6670(17)51901-1
[research_marchman_abtahi_1985]: https://doi.org/10.2514/3.45176
[research_marcinkiewicz_2019]: https://doi.org/10.1108/aeat-01-2018-0042
[research_marcus_raf_2019]: https://doi.org/10.2514/1.c034930
[research_mardanpour_2018]: https://doi.org/10.1016/j.jsv.2018.06.067
[research_maria_thoma_2024]: https://doi.org/10.2514/1.c037332
[research_marilyn_e_ogburn_1991]: https://ntrs.nasa.gov/citations/19910063214
[research_marinus_roger_2009]: https://doi.org/10.2514/6.2009-3330
[research_mark_2019]: https://doi.org/10.2514/1.c034979
[research_marlyn_andino]: https://ntrs.nasa.gov/citations/20240016289
[research_marques_2026]: https://doi.org/10.1177/1475472x261419107
[research_marquis_favre_2023]: https://doi.org/10.1016/j.apacoust.2023.109560
[research_marsden_1974]: https://doi.org/10.2514/6.1974-1035
[research_marsh_1981]: https://doi.org/10.1121/1.386523
[research_marshall_anderson_2015]: https://doi.org/10.25148/lawrev.10.2.6
[research_marston_sternberg_2015]: https://ntrs.nasa.gov/citations/20160008713
[research_martin_1978]: https://doi.org/10.21236/ada066904
[research_martina_1953]: https://ntrs.nasa.gov/citations/19930083652
[research_martina_1954]: https://ntrs.nasa.gov/citations/19930092195
[research_martinez_1989]: https://doi.org/10.2514/3.45813
[research_mastroddi_2018]: https://doi.org/10.1007/bf03405802
[research_masud_malik_2016]: https://doi.org/10.2514/6.2016-1038
[research_masuda_1996]: https://doi.org/10.1121/1.414586
[research_matheny_gatlin_1978]: https://ntrs.nasa.gov/citations/19780012197
[research_matheson_1987]: https://doi.org/10.21236/ada189048
[research_mathur_atkins_2023]: https://doi.org/10.2514/1.c036916
[research_matos_marta_2024]: https://doi.org/10.3390/aerospace11120959
[research_matouk_2024]: https://doi.org/10.1177/1475472x241259103
[research_matranga_armstrong_1959]: https://ntrs.nasa.gov/citations/19980235626
[research_matsuki_2018]: https://doi.org/10.1108/aeat-03-2016-0052
[research_matsushita_suzuki_1984]: https://doi.org/10.1121/1.391266
[research_matt_2025]: https://doi.org/10.2514/1.c038147
[research_matthias_casanova_2025]: https://ntrs.nasa.gov/citations/20250009012
[research_maughmer]: https://doi.org/10.18260/1-2--10745
[research_maughmer_1990]: https://ntrs.nasa.gov/citations/19900012418
[research_maughmer_2003]: https://doi.org/10.2514/6.2003-2777
[research_maughmer_metkowski_2024]: https://doi.org/10.2514/6.2024-0681
[research_may_widdison_1971]: https://doi.org/10.21236/ad0724185
[research_mayes_edge_1962]: https://doi.org/10.1121/1.2369558
[research_maynard_evans_1945]: https://ntrs.nasa.gov/citations/19930093330
[research_mcaree_2018]: https://doi.org/10.1017/aer.2018.14
[research_mccarthy_1955]: https://doi.org/10.21236/ad0110593
[research_mccormick_1959]: https://doi.org/10.2514/8.8022
[research_mccormick_1969]: https://doi.org/10.21236/ad0863818
[research_mccormick_b_w_1956]: https://doi.org/10.21236/ad0140228
[research_mccracken_1979]: https://ntrs.nasa.gov/citations/19800005852
[research_mccurdy_1984]: https://ntrs.nasa.gov/citations/19850028697
[research_mccurdy_1985]: https://ntrs.nasa.gov/citations/19860007607
[research_mccurdy_1989]: https://ntrs.nasa.gov/citations/19890046390
[research_mccurdy_1991]: https://ntrs.nasa.gov/citations/19920002540
[research_mccurdy_powell_1984]: https://ntrs.nasa.gov/citations/19840024054
[research_mccutchen_1989]: https://doi.org/10.2514/3.45790
[research_mcdonnell_aircraft_corp_st_louis_mo_1950]: https://doi.org/10.21236/ad0109763
[research_mcdonnell_ning_2020]: https://doi.org/10.2514/1.c035566
[research_mcgregor_smith_1966]: https://doi.org/10.2514/3.43780
[research_mckay_kingan_2019]: https://doi.org/10.2514/6.2019-2499
[research_mckee_1943]: https://ntrs.nasa.gov/citations/19930092921
[research_mclaughlin_shaw]: https://doi.org/10.1109/naecon.1989.40233
[research_mcmasters_1979]: https://ntrs.nasa.gov/citations/19790018909
[research_mcmasters_palmer_1975]: https://ntrs.nasa.gov/citations/19760003940
[research_mcneill_innis_1965]: https://ntrs.nasa.gov/citations/20000011990
[research_mcneill_vomaske_1959]: https://ntrs.nasa.gov/citations/19980232016
[research_mcpike_1972]: https://doi.org/10.2514/3.59033
[research_mcpike_1976]: https://doi.org/10.3397/1.2832045
[research_mcquillen_huang_1971]: https://doi.org/10.2514/3.59126
[research_mcveigh_mchugh_1984]: https://doi.org/10.4050/jahs.29.55
[research_mechel_1962]: https://doi.org/10.21236/ad0296946
[research_mechel_1963]: https://doi.org/10.21236/ad0431012
[research_meckstroth_ordonez_2020]: https://doi.org/10.2514/6.2020-3155
[research_mehdi_r_khorrami]: https://ntrs.nasa.gov/citations/20210017256
[research_mehra_1972]: https://ntrs.nasa.gov/citations/19720054594
[research_mehra_1974]: https://doi.org/10.2514/3.60327
[research_meissner_1973]: https://ntrs.nasa.gov/citations/19740002946
[research_mellish_2020]: https://doi.org/10.1121/10.0000490
[research_melton_1985]: https://doi.org/10.2514/3.45145
[research_melton_jacobson_1983]: https://doi.org/10.2514/3.44945
[research_memorandum_us]: https://doi.org/10.1163/ejb9789004244627.b03011
[research_meng_2017]: https://doi.org/10.1007/s00158-017-1725-1
[research_mengle_ganz_2006]: https://ntrs.nasa.gov/citations/20060020696
[research_mennell_1975]: https://ntrs.nasa.gov/citations/19750013277
[research_menon_2022]: https://doi.org/10.1103/physrevfluids.7.114102
[research_mentzer_nourse_1940]: https://doi.org/10.2514/8.1103
[research_merino_martinez_nicola_quaroni_2025]: https://doi.org/10.3397/in_2025_1076063
[research_merrill_2003]: https://ntrs.nasa.gov/citations/20030067980
[research_methods_for_2011]: https://doi.org/10.1201/b12545-8
[research_metodiev_2024]: https://doi.org/10.3897/arb.v36.e10
[research_metodiev_2025]: https://doi.org/10.3897/arb.v37.e12
[research_metzger_1973]: https://doi.org/10.2514/6.1973-1032
[research_metzger_1974]: https://doi.org/10.2514/6.1974-1001
[research_metzger_1976]: https://ntrs.nasa.gov/citations/19760048988
[research_metzger_1981]: https://doi.org/10.4271/810560
[research_metzger_farassat_2007]: https://doi.org/10.1002/9780470209707.ch90
[research_metzger_menthe_1980]: https://ntrs.nasa.gov/citations/19810018561
[research_metzger_worobel_1973]: https://doi.org/10.4271/730288
[research_meullen_1956]: https://doi.org/10.21236/ad0113062
[research_meyer_jiran_1981]: https://ntrs.nasa.gov/citations/19820030848
[research_meyerhoff_zvengrowski_1962]: https://doi.org/10.21236/ad0647299
[research_michael_feary]: https://ntrs.nasa.gov/citations/20210021950
[research_michaels_1969]: https://doi.org/10.21236/ad0859290
[research_michel_1989]: https://doi.org/10.1121/1.398687
[research_middleton_hurt_1975]: https://ntrs.nasa.gov/citations/19750024018
[research_miguel_1974]: https://doi.org/10.2514/3.44404
[research_mihalik_keane_2022]: https://doi.org/10.2514/1.c035944
[research_mihelic_pozderec_2023]: https://doi.org/10.60073/euper.2023.10.03
[research_mikkelson_mitchell_1984]: https://ntrs.nasa.gov/citations/19840024274
[research_miles_1952]: https://doi.org/10.1090/qam/51096
[research_miles_1953]: https://doi.org/10.1017/s0001925900000901
[research_milillo_1972]: https://doi.org/10.21236/ad0751461
[research_milla_blick_1966]: https://doi.org/10.2514/3.43785
[research_miller_1942]: https://doi.org/10.2514/8.10948
[research_miller_1970]: https://doi.org/10.2514/3.44206
[research_miller_1982]: https://doi.org/10.2514/3.44747
[research_miller_1983]: https://doi.org/10.2514/3.44931
[research_miller_1985_b]: https://doi.org/10.2514/6.1985-75
[research_miller_clark_1965]: https://doi.org/10.2514/3.43639
[research_miller_eagan_1997]: https://doi.org/10.21236/ada334209
[research_miller_eagan_1997_b]: https://doi.org/10.21236/ada334216
[research_miller_eagan_1998]: https://doi.org/10.21236/ada387239
[research_miller_franklin_1968]: https://doi.org/10.2514/3.43919
[research_miller_khinoo_1994]: https://doi.org/10.2514/6.1994-3433
[research_miller_koch_1985]: https://doi.org/10.21236/ada158227
[research_min_lim_2015]: https://doi.org/10.2514/6.2015-2389
[research_minor_2008]: https://doi.org/10.2514/6.2008-1601
[research_minwalla_2016]: https://doi.org/10.1139/juvs-2014-0022
[research_minwalla_2016_2]: https://doi.org/10.1142/s2301385016500102
[research_misol_2020]: https://doi.org/10.1016/j.apacoust.2019.107086
[research_mitcham_1949]: https://ntrs.nasa.gov/citations/20010062502
[research_mitchell_2003]: https://doi.org/10.21236/ada417898
[research_mitchell_hoh_1984]: https://doi.org/10.2514/3.8551
[research_mitchell_mikkelson_1982]: https://ntrs.nasa.gov/citations/19820018343
[research_mitcheltree_1986]: https://doi.org/10.2514/3.45357
[research_mixson_barton_1977]: https://ntrs.nasa.gov/citations/19770054214
[research_mixson_barton_1979]: https://doi.org/10.2514/6.1979-646
[research_mixson_greene_1981]: https://ntrs.nasa.gov/citations/19810010547
[research_mixson_powell_1984]: https://doi.org/10.2514/6.1984-2349
[research_mixson_powell_1985]: https://doi.org/10.2514/3.45229
[research_mo_2016]: https://doi.org/10.1016/j.apacoust.2015.10.011
[research_mo_2017]: https://doi.org/10.1121/1.4977005
[research_mobley_2016]: https://doi.org/10.3397/1/376381
[research_mockelman_crane_2026]: https://doi.org/10.2514/6.2026-1303
[research_moelyadi_2021]: https://doi.org/10.1088/1757-899x/1173/1/012055
[research_mohamed_2021]: https://doi.org/10.2514/1.c035920
[research_mohamed_joy_2021]: https://doi.org/10.1017/aer.2021.61
[research_mohammadi_farhadi_2018]: https://doi.org/10.14311/ap.2018.58.0077
[research_mokhtari_2020]: https://doi.org/10.1007/s42401-020-00063-w
[research_mokry_rainbird_1975]: https://doi.org/10.2514/3.44488
[research_molchanov_1981]: https://doi.org/10.1007/bf01094614
[research_momiyama_1977]: https://ntrs.nasa.gov/citations/19780011177
[research_monitoring_of_2011]: https://doi.org/10.1201/b12545-11
[research_monstein_2019]: https://doi.org/10.2514/1.c035171
[research_montalvo_costello_2015]: https://doi.org/10.2514/1.c032634
[research_monzambe_2024]: https://doi.org/10.1016/j.procir.2024.07.065
[research_mooij_1985]: https://doi.org/10.1007/978-94-017-1193-7_5
[research_mooij_1985_b]: https://doi.org/10.1007/978-94-017-1193-7_6
[research_mooij_1985_c]: https://doi.org/10.1007/978-94-017-1193-7
[research_moore_moore_2012]: https://doi.org/10.2514/6.2012-692
[research_moore_moore_2012_b]: https://doi.org/10.2514/1.a32074
[research_moralez_2004]: https://ntrs.nasa.gov/citations/20050010185
[research_moreira_2022]: https://doi.org/10.2514/1.g006443
[research_moreland_jr_1965]: https://doi.org/10.21236/ad0741947
[research_morelli_cooper_2015]: https://doi.org/10.2514/1.c033121
[research_morfey_howell_1981]: https://doi.org/10.2514/3.51026
[research_morfey_tester_1977]: https://doi.org/10.1016/0022-460x(77)90408-4
[research_morgado_silvestre_2013]: https://doi.org/10.2514/6.2013-4379
[research_morgan_1954]: https://doi.org/10.21236/ad0115985
[research_morgan_1961]: https://doi.org/10.21236/ad0259813
[research_morgan_hardin_1975]: https://doi.org/10.2514/3.59844
[research_morge_rollet_2022]: https://doi.org/10.3390/s22176701
[research_morhy_cavalcante_2026]: https://doi.org/10.3397/nc_2026_0205
[research_morinaga_2021]: https://doi.org/10.3397/in-2021-2041
[research_morita_1970]: https://doi.org/10.1299/kikai1938.36.1681
[research_morita_1971]: https://doi.org/10.1299/jsme1958.14.550
[research_morita_1971_2]: https://doi.org/10.1299/kikai1938.37.1525
[research_moriya_1972]: https://doi.org/10.1299/jsme1958.15.466
[research_morris_1973]: https://doi.org/10.1016/s0022-460x(73)80060-4
[research_morris_alexander_1978]: https://ntrs.nasa.gov/citations/19790034158
[research_morton_1956]: https://doi.org/10.1108/eb032772
[research_moses_zeitlin_1975]: https://doi.org/10.1016/0022-460x(75)90014-0
[research_moshkov_2019]: https://doi.org/10.36336/akustika20193466
[research_moshkov_2022]: https://doi.org/10.1007/s42401-021-00127-5
[research_moshkov_2026]: https://doi.org/10.1007/s42401-026-00537-3
[research_moshkov_2026_b]: https://doi.org/10.1007/s42417-026-02419-6
[research_moshkov_2026_c]: https://doi.org/10.1063/5.0321990
[research_moshkov_samokhin_2016]: https://doi.org/10.1615/tsagiscij.2017019465
[research_moshkov_samokhin_2021]: https://doi.org/10.34759/vst-2021-1-19-34
[research_moshkov_yakovlev_2023]: https://doi.org/10.1063/5.0125051
[research_mosov_2020]: https://doi.org/10.33269/nvcz.2020.1.34-41
[research_mostarac_rescic_2022]: https://doi.org/10.7307/ptt.v34i6.4158
[research_mothes_2019]: https://doi.org/10.3390/aerospace6060068
[research_motyka_hall_1973]: https://doi.org/10.2514/3.60289
[research_moul_brown_1959]: https://ntrs.nasa.gov/citations/19980228212
[research_moul_brown_1979]: https://ntrs.nasa.gov/citations/19790061390
[research_mr_s_aravindan_2017]: https://doi.org/10.17577/ijertv6is020019
[research_mrusek_2021]: https://doi.org/10.19080/ttsr.2021.05.555651
[research_mueller_1993]: https://ntrs.nasa.gov/citations/19950058524
[research_mueller_paluszek_2004]: https://doi.org/10.21236/ada451761
[research_muhlstein_coe_1979]: https://doi.org/10.2514/3.58576
[research_mukhachev_2022]: https://doi.org/10.1177/09544100211053753
[research_muller_1971]: https://doi.org/10.1016/0022-460x(71)90664-x
[research_muller_2026]: https://doi.org/10.2514/1.c038139
[research_muller_moormann_2023]: https://doi.org/10.1142/s2301385024430040
[research_multi_rotors_a_2015]: https://doi.org/10.21275/v4i11.nov151540
[research_mulyanto_zulkarnain_2020]: https://doi.org/10.1063/5.0002635
[research_mulyanto_zulkarnain_2021]: https://doi.org/10.1088/1757-899x/1173/1/012048
[research_muneer_2026]: https://doi.org/10.1038/s41598-026-48487-2
[research_mungiole_wilson_2003]: https://doi.org/10.21236/ada413843
[research_muniraj_farhood_2019]: https://doi.org/10.1016/j.conengprac.2018.10.022
[research_munk_1925]: https://ntrs.nasa.gov/citations/19930091263
[research_munro_ahuja_2003]: https://ntrs.nasa.gov/citations/20030065823
[research_murillo_mcmasters_1984]: https://doi.org/10.2514/3.48242
[research_murphy_frink_2019]: https://ntrs.nasa.gov/citations/20200002425
[research_murray_1992]: https://ntrs.nasa.gov/citations/19920006768
[research_murray_warren_1944]: https://ntrs.nasa.gov/citations/19930092937
[research_murrieta_mendoza_2016]: https://doi.org/10.1016/j.ifacol.2016.09.001
[research_muser_1979]: https://ntrs.nasa.gov/citations/19790018908
[research_mutyala_soedel_1974]: https://doi.org/10.1121/1.1914111
[research_myala_2020]: https://doi.org/10.1017/aer.2020.131
[research_myers_2018]: https://doi.org/10.15394/ijaaa.2018.1203
[research_na_cho_2022]: https://doi.org/10.12985/ksaa.2022.30.2.007
[research_nabi_2018]: https://doi.org/10.2514/1.g003184
[research_naca_conference_1957]: https://ntrs.nasa.gov/citations/19710070068
[research_naca_conference_1958]: https://ntrs.nasa.gov/citations/19710069971
[research_nagabhushan_1983]: https://doi.org/10.2514/3.44859
[research_nagao_1998]: https://doi.org/10.1121/1.423193
[research_nagaraja_1982]: https://doi.org/10.2514/3.61555
[research_nagata_1973]: https://doi.org/10.21236/ad0776360
[research_nagy_kirsten_1976]: https://doi.org/10.21236/adb012970
[research_najafi_2025]: https://doi.org/10.1007/s10846-024-02216-x
[research_nakka_alexander_ramos_2021]: https://doi.org/10.2514/1.c035678
[research_nallasamy_1989]: https://doi.org/10.2514/3.45803
[research_nallasamy_clark_1987]: https://doi.org/10.2514/6.1987-525
[research_nam_joshi_2017]: https://doi.org/10.1177/1550147717732920
[research_nam_mavris_2018]: https://doi.org/10.2514/1.c032099
[research_narayan_1975]: https://doi.org/10.1017/s0001925900007332
[research_narendra_tripathi_1973]: https://doi.org/10.2514/3.44364
[research_narimani_2025]: https://doi.org/10.1016/j.ast.2025.109992
[research_nark_2004]: https://ntrs.nasa.gov/citations/20040075556
[research_nark_2017]: https://ntrs.nasa.gov/citations/20170006070
[research_nash_1982]: https://doi.org/10.2514/3.57422
[research_nash_webber_1973]: https://ntrs.nasa.gov/citations/19740001939
[research_nasoulis_2022]: https://doi.org/10.1017/aer.2022.32
[research_nassif_1969]: https://doi.org/10.1243/jmes_jour_1969_011_049_02
[research_national_advisory_1932]: https://doi.org/10.1016/s0016-0032(32)90809-6
[research_national_advisory_1937]: https://doi.org/10.1016/s0016-0032(37)91594-1
[research_naval_air_test_center_patuxent_river_md_1957]: https://doi.org/10.21236/ad0125304
[research_naval_air_test_center_patuxent_river_md_1963]: https://doi.org/10.21236/ad0669901
[research_navaratna_2019]: https://doi.org/10.2514/1.c035199
[research_navaratna_2022]: https://doi.org/10.2514/1.c036157
[research_nayfeh_1980]: https://doi.org/10.1016/0022-460x(80)90665-3
[research_nazarenko_nevezhina_1972]: https://doi.org/10.1007/bf01186488
[research_neal_smith_1971]: https://doi.org/10.2514/3.59174
[research_neff_2019]: https://doi.org/10.15394/ijaaa.2019.1303
[research_negahban_2024]: https://doi.org/10.3390/drones8080392
[research_nejati_2018]: https://doi.org/10.1007/s40430-018-1224-3
[research_nelson_1938]: https://doi.org/10.1121/1.1902044
[research_nelson_1964]: https://doi.org/10.21236/ad0430928
[research_nelson_1965]: https://doi.org/10.21236/ad0620929
[research_nelson_1974]: https://doi.org/10.21236/ad0787193
[research_nelson_2012]: https://doi.org/10.21236/ada561825
[research_nemec_bedonian_2024]: https://doi.org/10.2514/6.2024-4671
[research_neto_signor_2023]: https://doi.org/10.2514/6.2023-76306
[research_neves_2020]: https://doi.org/10.1016/j.ast.2020.106179
[research_newell_1963]: https://doi.org/10.21236/ad0425705
[research_newell_herrick_1979]: https://doi.org/10.21236/ada093516
[research_newsom_tosti_1959]: https://ntrs.nasa.gov/citations/19980228402
[research_newton_h_campbell]: https://ntrs.nasa.gov/citations/20205009996
[research_newton_h_campbell_2021]: https://ntrs.nasa.gov/citations/20205002641
[research_nguyen_2017]: https://ntrs.nasa.gov/citations/20170009884
[research_nguyen_2018_2]: https://doi.org/10.3397/1/376639
[research_nguyen_yano_2024]: https://doi.org/10.3397/in_2024_4261
[research_nhan_nguyen_juntao_xiong]: https://ntrs.nasa.gov/citations/20210025832
[research_ni_2025]: https://doi.org/10.1088/1742-6596/3044/1/012001
[research_nicolaides_1971]: https://doi.org/10.21236/ad0731564
[research_nicolaides_1976]: https://doi.org/10.21236/ada056569
[research_nicolaides_tragarz_1971]: https://doi.org/10.21236/ad0731143
[research_nie_2025]: https://doi.org/10.2514/1.j064474
[research_nikhade_barde_2023]: https://doi.org/10.9734/bpi/rader/v3/5335b
[research_nikolas_s_zawodny_2025]: https://ntrs.nasa.gov/citations/20250009190
[research_nimal_a_2019]: https://doi.org/10.37200/ijpr/v23i4/pr190169
[research_nishinomiya_1978]: https://doi.org/10.1109/tbc.1978.266298
[research_nnonyelu_2020]: https://doi.org/10.15199/48.2020.12.14
[research_nnonyelu_2021]: https://doi.org/10.15199/48.2021.01.13
[research_noda_2022]: https://doi.org/10.3389/fpace.2022.1004828
[research_noda_2025]: https://doi.org/10.20965/jrm.2025.p0799
[research_nonweiler_1960]: https://doi.org/10.1017/s0368393100072485
[research_norris_bauer_1993]: https://doi.org/10.2514/3.46372
[research_norris_ostashev_2022]: https://doi.org/10.1121/10.0010965
[research_north_american_aviation_inc_los_angeles_ca_1963]: https://doi.org/10.21236/ad0410334
[research_northamericanaviationinclosangelesca_1956]: https://doi.org/10.21236/ad0159109
[research_northrop_aircraft_inc_hawthorne_ca_1952]: https://doi.org/10.21236/ad0024361
[research_norton_1990]: https://doi.org/10.21236/ada257262
[research_novak_1970]: https://doi.org/10.2514/6.1970-1409
[research_nyborg_mintzer_1955]: https://doi.org/10.21236/ad0067880
[research_obayashi_1999]: https://doi.org/10.1007/978-3-322-89952-1_2
[research_obermark_2004]: https://doi.org/10.21236/ada422954
[research_odell_1977]: https://doi.org/10.3397/1.2832067
[research_odonnell_mohseni_2019]: https://doi.org/10.2514/1.c034704
[research_ogawa_2015]: https://doi.org/10.1299/jsmekyushu.2015.68.321
[research_ogawara_2024]: https://doi.org/10.1299/jsmecs.2024.62.04a1
[research_ogburn_1994]: https://ntrs.nasa.gov/citations/19950007832
[research_ogburn_brown_1980]: https://ntrs.nasa.gov/citations/19800019869
[research_ogiso_2019]: https://doi.org/10.1299/jsmermd.2019.1p2-r04
[research_ogren_1974]: https://doi.org/10.21236/ad0784134
[research_oh_lerud_2023]: https://doi.org/10.1121/10.0023933
[research_oh_yoon_2022]: https://doi.org/10.1016/j.trip.2022.100732
[research_ohm_2020]: https://doi.org/10.1121/10.0002030
[research_ohta_1935]: https://doi.org/10.1299/jsmemagazine.38.214_93
[research_ohta_1979]: https://doi.org/10.2514/3.55828
[research_ohta_1982]: https://doi.org/10.2514/3.56143
[research_okada_1994]: https://doi.org/10.4271/940001
[research_oktay_ozen_2022]: https://doi.org/10.30518/jav.1080139
[research_okumoto_elsanker_1973]: https://doi.org/10.21236/ad0767182
[research_oleson_patrick_1998]: https://doi.org/10.2514/6.1998-2284
[research_oleynikov_2018]: https://doi.org/10.30837/rt.2018.4.195.21
[research_oliveira_payne_2021]: https://doi.org/10.2514/6.2021-2513
[research_ollerhead_1971]: https://doi.org/10.21236/ad0730788
[research_ollerhead_1973]: https://doi.org/10.1016/s0022-460x(73)80191-9
[research_ollerhead_1982]: https://ntrs.nasa.gov/citations/19830003569
[research_olsen_2019]: https://doi.org/10.1142/s2301385019500079
[research_olson_1978]: https://ntrs.nasa.gov/citations/19790004865
[research_olson_2015]: https://doi.org/10.2514/6.2015-1679
[research_olson_hill_2004]: https://doi.org/10.1121/1.4785130
[research_omair_alhatim_2026]: https://doi.org/10.59543/jidmis.v3.852
[research_oncley_1970]: https://doi.org/10.1121/1.1974014
[research_onkar_2024]: https://doi.org/10.1007/s12046-024-02629-2
[research_optimal_switching_2019]: https://doi.org/10.26634/jic.6.4.14950
[research_optimization_software_2000]: https://doi.org/10.1108/aeat.2000.12772daf.002
[research_ordonez_2003]: https://doi.org/10.1016/s0360-5442(03)00105-1
[research_orkisz_wygonik_2019]: https://doi.org/10.19206/ce-2019-416
[research_orme_1998]: https://ntrs.nasa.gov/citations/19980228162
[research_ormsbee_1977]: https://ntrs.nasa.gov/citations/19770024212
[research_ormsbee_siddiqi_1977]: https://ntrs.nasa.gov/citations/19770024214
[research_oruc_2017]: https://doi.org/10.2514/1.c034101
[research_ostashev_goedecke_2005]: https://doi.org/10.21236/ada431684
[research_ostashev_wilson_2022]: https://doi.org/10.1121/10.0015855
[research_ostrikov_2020]: https://doi.org/10.1134/s1063771020010066
[research_otsuka_2017]: https://doi.org/10.1016/j.jsv.2017.07.012
[research_otsuka_2021]: https://doi.org/10.1115/1.4050276
[research_otsuka_2022]: https://doi.org/10.2514/1.c036285
[research_ouda_2021]: https://doi.org/10.1504/ijaac.2021.114921
[research_ouellette_2026]: https://doi.org/10.2514/1.c038471
[research_ovcharenko_poplavsky_2021]: https://doi.org/10.1134/s1064230721060149
[research_p5_2026]: https://doi.org/10.55041/ijsrem61623
[research_page_2021]: https://doi.org/10.3397/in-2021-1650
[research_page_2026]: https://doi.org/10.3397/nc_2026_0192
[research_palaia_2023]: https://doi.org/10.3390/app131911113
[research_palchikovskiy_2023]: https://doi.org/10.31857/s0320791923600087
[research_palkin_zenchenko_2025]: https://doi.org/10.18127/j20700784-202509-06
[research_pallejacabre_macey_2024]: https://doi.org/10.2514/6.2024-3407
[research_palmer_petitt_1976]: https://doi.org/10.2514/6.1976-1712
[research_pamadi_pai_1980]: https://doi.org/10.2514/3.44663
[research_pan_huang_2019]: https://doi.org/10.1108/aeat-04-2018-0119
[research_pande_2025]: https://doi.org/10.36948/ijfmr.2025.v07i05.58371
[research_panel_discussion_1976]: https://doi.org/10.2514/5.9781600865206.0195.0199
[research_panel_discussion_1976_b]: https://doi.org/10.2514/5.9781600865206.0089.0089
[research_pao_1971]: https://doi.org/10.1016/0022-460x(71)90611-0
[research_pao_evans_1971]: https://doi.org/10.1121/1.1975517
[research_pao_lan_1978]: https://ntrs.nasa.gov/citations/19780009059
[research_papa_2023]: https://doi.org/10.3390/electronics12071591
[research_papageorgiou_2018]: https://doi.org/10.2514/1.c034314
[research_papageorgiou_2020]: https://doi.org/10.2514/1.c035640
[research_papamoschou_debiasi_2003]: https://doi.org/10.2514/2.6103
[research_papamoschou_phong_2018]: https://doi.org/10.2514/6.2018-1740
[research_park_2018]: https://doi.org/10.1155/2018/5782017
[research_park_2018_2]: https://doi.org/10.1108/aeat-06-2017-0149
[research_park_2023]: https://doi.org/10.5139/jksas.2023.51.7.497
[research_park_2026]: https://doi.org/10.1016/j.ast.2026.111650
[research_park_2026_2]: https://doi.org/10.5139/jksas.2026.54.3.329
[research_park_2026_b]: https://doi.org/10.21741/9781644904251-59
[research_parry_1995]: https://doi.org/10.1017/s0022112095001686
[research_parry_2020]: https://doi.org/10.1016/j.apacoust.2020.107548
[research_parry_2020_2]: https://doi.org/10.1016/j.apacoust.2019.107122
[research_parry_crighton_1989]: https://doi.org/10.2514/3.10244
[research_pasareanu_2018]: https://doi.org/10.1121/1.5027506
[research_pascioni_2026]: https://doi.org/10.2514/1.c038487
[research_paswan_2025]: https://doi.org/10.1177/1475472x251382211
[research_paszkowski_2024]: https://doi.org/10.12913/22998624/175863
[research_pate_1964]: https://doi.org/10.21236/ad0450195
[research_pate_deitering_1963]: https://doi.org/10.21236/ad0297204
[research_paterson_1973]: https://doi.org/10.2514/3.60243
[research_patrick_1986]: https://doi.org/10.2514/6.1986-1906
[research_patrick_lobo_2000]: https://doi.org/10.2514/6.2000-1940
[research_patrick_nagel_1989]: https://doi.org/10.2514/6.1989-1145
[research_patterson_1989]: https://doi.org/10.2514/6.1989-2011
[research_patterson_2016]: https://doi.org/10.1139/juvs-2015-0014
[research_pauli_corliss_1974]: https://ntrs.nasa.gov/citations/19740020624
[research_paullin_2011]: https://doi.org/10.21236/ada554209
[research_pauls_gollnick_2025]: https://doi.org/10.1007/s13272-025-00926-y
[research_paulson_1976]: https://ntrs.nasa.gov/citations/19760019130
[research_paulson_shanks_1959]: https://ntrs.nasa.gov/citations/19980237090
[research_paulson_shanks_1961]: https://ntrs.nasa.gov/citations/19980227997
[research_paulson_shanks_1961_2]: https://ntrs.nasa.gov/citations/19980227410
[research_pavel_jan_2018]: https://doi.org/10.1051/matecconf/201823300027
[research_pavlenko_reslan_2022]: https://doi.org/10.34759/vst-2022-3-17-28
[research_pavlusikova_chodelka_2023]: https://doi.org/10.26552/pas.z.2023.1.13
[research_pawlak_1994]: https://doi.org/10.2514/6.1994-2116
[research_pbharendra_mjjoglekar_1973]: https://ntrs.nasa.gov/citations/19730022217
[research_pearson_1937]: https://ntrs.nasa.gov/citations/19930081392
[research_peart_1991]: https://ntrs.nasa.gov/citations/19920005568
[research_pecho_2019]: https://doi.org/10.1016/j.trpro.2019.07.067
[research_peebles_2007]: https://ntrs.nasa.gov/citations/20070038172
[research_pegg_1974]: https://ntrs.nasa.gov/citations/19740022310
[research_pegg_hilton_1974]: https://ntrs.nasa.gov/citations/19740013539
[research_pei_2016]: https://doi.org/10.2514/1.c033683
[research_pelykh_andryushchenko_2024]: https://doi.org/10.15587/2706-5448.2024.298600
[research_pena_diamond_1965]: https://doi.org/10.21236/ad0473746
[research_peng_2026]: https://doi.org/10.1177/1475472x261452750
[research_pentz_tang_2017]: https://doi.org/10.4018/ijasot.2017010104
[research_peplow_liu_2025]: https://doi.org/10.1016/j.apacoust.2025.110811
[research_pereira_gouveia_da_silva_2025]: https://doi.org/10.3397/in_2025_1092741
[research_perez_jansen_2014]: https://doi.org/10.2514/6.2014-2732
[research_performance_characteristics_1930]: https://doi.org/10.1016/s0016-0032(30)90828-9
[research_perisho_1959]: https://doi.org/10.4050/jahs.4.2.4
[research_perkins_1977]: https://doi.org/10.21236/ada062275
[research_peron_carpenter_1992]: https://ntrs.nasa.gov/citations/19920012114
[research_perry_1978]: https://ntrs.nasa.gov/citations/19780023100
[research_perry_2021]: https://doi.org/10.2514/1.c036048
[research_perry_2023]: https://doi.org/10.2514/1.c036616
[research_persoon_1980]: https://doi.org/10.21236/ada097094
[research_pestana_2010]: https://ntrs.nasa.gov/citations/20100042224
[research_peter_zaal]: https://ntrs.nasa.gov/citations/20250009018
[research_peterse_2024]: https://doi.org/10.25144/19287
[research_petersen_1962]: https://ntrs.nasa.gov/citations/19650014323
[research_petersen_1981]: https://doi.org/10.2514/6.1981-2417
[research_peterson_warmbrodt_1996]: https://ntrs.nasa.gov/citations/20020043032
[research_petitt_2017]: https://doi.org/10.4018/ijasot.2017070103
[research_petrescu_2017]: https://doi.org/10.3844/jastsp.2017.224.233
[research_petrovskii_1965]: https://doi.org/10.1007/bf00830316
[research_petty_1975]: https://doi.org/10.21236/ada016728
[research_pfaff_1968]: https://doi.org/10.21236/ad0832104
[research_pfeiffer_2017]: https://doi.org/10.2514/6.2017-4089
[research_pfeifle_2022]: https://doi.org/10.2514/1.c036490
[research_pfeifle_fichter_2023]: https://doi.org/10.2514/1.g006929
[research_pham_2025]: https://doi.org/10.55248/gengpi.6.0925.35106
[research_philip_j_hamory_james_e_murray_1992]: https://ntrs.nasa.gov/citations/19930027283
[research_phillips_1942]: https://ntrs.nasa.gov/citations/20150015694
[research_phillips_1975]: https://ntrs.nasa.gov/citations/19760028267
[research_phillips_2002]: https://doi.org/10.2514/2.2914
[research_phillips_everest_1953]: https://doi.org/10.21236/ada636692
[research_phun_2015]: https://doi.org/10.4236/jep.2015.69086
[research_picolet_1932]: https://doi.org/10.1016/s0016-0032(32)90592-4
[research_pieper_1965]: https://doi.org/10.21236/ad0613339
[research_pierson_1977]: https://doi.org/10.1017/s0001925900007976
[research_pierson_chen_1979]: https://ntrs.nasa.gov/citations/19790018900
[research_pierson_chen_1979_2]: https://doi.org/10.2514/3.58520
[research_pierson_dejong_1978]: https://doi.org/10.1002/nme.1620121111
[research_pietrasanta_galloway_1956]: https://doi.org/10.1121/1.1918130
[research_pilcher_2021]: https://doi.org/10.32920/ryerson.14653626.v1
[research_pinker_2024]: https://doi.org/10.25144/21563
[research_pioneering_woman_2001]: https://doi.org/10.1108/aeat.2001.12773aab.035
[research_pitkin_1968]: https://doi.org/10.2514/3.29409
[research_pitts_1974]: https://ntrs.nasa.gov/citations/19750009281
[research_pivko_1956]: https://doi.org/10.1108/eb032722
[research_pla_1989]: https://ntrs.nasa.gov/citations/19890016304
[research_place_1974]: https://doi.org/10.21236/ad0785104
[research_platt_shortal_1937]: https://ntrs.nasa.gov/citations/19930091677
[research_plckerell_cresswell_1968]: https://doi.org/10.2514/3.43968
[research_pleban_beal_2002]: https://doi.org/10.21236/ada402194
[research_pliem_2018]: https://doi.org/10.1088/1742-6596/1005/1/012027
[research_plotkin_shepherd_2006]: https://ntrs.nasa.gov/citations/20060049123
[research_plucinsky_1973]: https://doi.org/10.4271/730289
[research_plunkett_1949]: https://doi.org/10.1115/1.4010011
[research_poe_arthur_c_1974]: https://doi.org/10.21236/ada017599
[research_pogosyan_moshkov_2023]: https://doi.org/10.18287/2409-4579-2023-9-1-6-15
[research_polacsek_spiegel_2000]: https://doi.org/10.2514/6.2000-2086
[research_polhamus_king_1949]: https://ntrs.nasa.gov/citations/20050030036
[research_polly_1969]: https://doi.org/10.1121/1.1972308
[research_pope_1987]: https://doi.org/10.1016/0022-460x(87)90364-6
[research_pope_1987_2]: https://doi.org/10.1016/0022-460x(87)90365-8
[research_pornet_isikveren_2015]: https://doi.org/10.1016/j.paerosci.2015.09.002
[research_portapas_cooke_2020]: https://doi.org/10.3846/aviation.2020.12175
[research_portnoy_1976]: https://doi.org/10.1017/s0001924000034370
[research_portnoy_1977]: https://doi.org/10.1017/s0001924000033169
[research_posey_2008]: https://doi.org/10.1121/1.2935040
[research_posingies_1968]: https://doi.org/10.21236/ad0680275
[research_pottpollenske_2021]: https://doi.org/10.2514/6.2021-2117
[research_povinelli_2002]: https://ntrs.nasa.gov/citations/20020082902
[research_powell_dunford_2016]: https://doi.org/10.3357/amhp.4638.2016
[research_power_1963]: https://doi.org/10.1002/j.2161-4296.1963.tb02024.x
[research_powers_sarrafian_1986]: https://ntrs.nasa.gov/citations/19860062935
[research_poysa_2018]: https://doi.org/10.1007/s10344-018-1238-2
[research_poznanski_mays_2025]: https://doi.org/10.2514/6.2025-1618
[research_prasad_crocker_1983]: https://doi.org/10.1016/0022-460x(83)90807-6
[research_prasannakumar_2024]: https://doi.org/10.2514/1.c037398
[research_price_1943]: https://doi.org/10.1108/eb031071
[research_price_hodge_1976]: https://doi.org/10.21236/ada035084
[research_pridmore_brown_1962]: https://doi.org/10.1121/1.1918146
[research_primatesta_2019]: https://doi.org/10.1007/s10846-019-01015-z
[research_probst_2017]: https://doi.org/10.2514/1.c034203
[research_propeller_performance_2012]: https://doi.org/10.1017/cbo9781139161893.009
[research_propeller_propulsion_2010]: https://doi.org/10.2514/5.9781600867538.0435.0466
[research_propeller_system_1999]: https://doi.org/10.1108/aeat.1999.12771eab.017
[research_przedpelski_1965]: https://doi.org/10.2514/6.1965-708
[research_pugh_1972]: https://doi.org/10.2514/6.1972-812
[research_purser_1941]: https://ntrs.nasa.gov/citations/19930092832
[research_pusch_2019]: https://doi.org/10.1007/s13272-019-00367-4
[research_pushtaev_1989]: https://doi.org/10.1016/0041-5553(89)90024-4
[research_putman_1969]: https://doi.org/10.21236/ad0859807
[research_putnam_1975]: https://ntrs.nasa.gov/citations/19750024046
[research_puttur_layng_2025]: https://doi.org/10.2514/6.2025-98910
[research_pyo_1995]: https://doi.org/10.21236/ada298179
[research_qi_2018]: https://doi.org/10.1109/taes.2018.2836598
[research_qi_zhao_2020]: https://doi.org/10.2514/1.g004761
[research_qian_2022]: https://doi.org/10.1049/icp.2022.1719
[research_qian_2026]: https://doi.org/10.59400/sv3837
[research_qiang_wang_2025]: https://doi.org/10.3390/sym17111997
[research_qiao_2018]: https://doi.org/10.1016/j.jfluidstructs.2018.07.009
[research_qiao_2025]: https://doi.org/10.23967/j.rimni.2024.10.56530
[research_qin_2023]: https://doi.org/10.1049/cth2.12427
[research_qin_huang_2024]: https://doi.org/10.2514/6.2024-3103
[research_qin_wang_2014]: https://doi.org/10.2514/6.2014-2992
[research_qinetiq_welcomes_2002]: https://doi.org/10.1108/aeat.2002.12774cab.040
[research_qiu_ang_2019]: https://doi.org/10.1155/2019/5046395
[research_qu_2017]: https://doi.org/10.1016/j.ast.2017.07.036
[research_qu_li_2022]: https://doi.org/10.1088/1742-6596/2258/1/012074
[research_quagliarella_iuliano_2017]: https://doi.org/10.1109/mci.2017.2742718
[research_quanyan_2021]: https://doi.org/10.1049/icp.2021.0176
[research_quaranta_dimino_2007]: https://doi.org/10.2514/1.24824
[research_quaroni_merinomartinez_2024]: https://doi.org/10.2514/6.2024-3209
[research_queen_cochrane_1982]: https://doi.org/10.2514/3.57446
[research_quick_1937]: https://doi.org/10.1108/eb030240
[research_quillet_2023]: https://doi.org/10.2514/1.c036927
[research_quinn_1963]: https://doi.org/10.21236/ad0431128
[research_quinn_2025]: https://doi.org/10.1016/j.ast.2025.109987
[research_quinn_breidenbach_1978]: https://doi.org/10.2514/6.1978-1498
[research_quirion_liu_2020]: https://doi.org/10.1142/s2301385021500023
[research_r_1935]: https://doi.org/10.1016/s0016-0032(35)90380-5
[research_r_2018]: https://doi.org/10.1108/aeat-03-2016-0050
[research_r_g_macleod_1952]: https://ntrs.nasa.gov/citations/19930086896
[research_r_l_stallings_jr_1986]: https://ntrs.nasa.gov/citations/19870035655
[research_rader_1989]: https://doi.org/10.1117/12.948613
[research_radetskaya_2022]: https://doi.org/10.18698/2541-8009-2022-10-833
[research_raffel_2019]: https://doi.org/10.2514/1.c035399
[research_ragani_lamouki_2026]: https://doi.org/10.1177/1475472x261452754
[research_raisbeck_mills_1987]: https://doi.org/10.4271/871034
[research_rajeswari_padma_suresh_2015]: https://doi.org/10.17485/ijst/2015/v8i24/80161
[research_rakesh_reddy_2023]: https://doi.org/10.22214/ijraset.2023.55928
[research_ralles_1966]: https://doi.org/10.21236/ad0645885
[research_ramachandra_1979]: https://doi.org/10.2514/3.58556
[research_ramsak_2012]: https://doi.org/10.5545/sv-jme.2009.153
[research_ranaudo_2000]: https://ntrs.nasa.gov/citations/20000120385
[research_rand_khromov_2004]: https://doi.org/10.2514/1.9085
[research_randall_1955]: https://doi.org/10.21236/ad0056013
[research_raney_1975]: https://ntrs.nasa.gov/citations/19760006011
[research_raney_batterson_1989]: https://ntrs.nasa.gov/citations/19890012431
[research_range_werner_2013]: https://doi.org/10.1109/epe.2013.6631957
[research_rankine_leondes_1972]: https://doi.org/10.2514/3.58980
[research_rao_1987]: https://doi.org/10.2514/3.45433
[research_rao_1992]: https://ntrs.nasa.gov/citations/19920062929
[research_rao_2023]: https://doi.org/10.3390/aerospace10040331
[research_rao_pittu_2023]: https://doi.org/10.14445/23488379/ijeee-v10i11p102
[research_rasband_2023]: https://doi.org/10.3397/nc_2023_0105
[research_rasmussen_1986]: https://doi.org/10.1016/0022-460x(86)90271-3
[research_rasmussen_1990]: https://doi.org/10.1016/0022-460x(90)90845-q
[research_raspet_1952]: https://doi.org/10.21236/ad0000965
[research_raspet_1955]: https://doi.org/10.1007/978-3-663-20219-6_44
[research_rathgeber_sipes_1977]: https://doi.org/10.4271/770444
[research_ratvasky_barnhart_2010]: https://ntrs.nasa.gov/citations/20110016128
[research_ratvasky_blankenship_2003]: https://ntrs.nasa.gov/citations/20030054467
[research_ravetta_2019]: https://ntrs.nasa.gov/citations/20200002611
[research_raw_griffiths_1985]: https://doi.org/10.1016/s0022-460x(85)81223-2
[research_rawson_1963]: https://doi.org/10.21236/ad0429114
[research_ray_1988]: https://ntrs.nasa.gov/citations/19880011767
[research_raymer_2004]: https://doi.org/10.2514/1.523
[research_raza_stansbury_2025]: https://doi.org/10.3390/drones9080577
[research_reader_1976]: https://doi.org/10.21236/ada026548
[research_reader_1980]: https://doi.org/10.21236/ada080953
[research_rebont_1977]: https://doi.org/10.2514/3.44574
[research_reconnaissance_and_2008]: https://doi.org/10.5040/9798400685590.ch-005
[research_reddingius_1974]: https://doi.org/10.21236/ad0785360
[research_reddingius_1977]: https://doi.org/10.21236/ada042143
[research_rediess_melton_1994]: https://doi.org/10.2514/6.1994-2172
[research_reduced_noise_1988]: https://doi.org/10.1108/eb036706
[research_reed_1941]: https://doi.org/10.2514/8.10668
[research_reed_1966]: https://doi.org/10.1016/0022-460x(66)90142-8
[research_reeder_1958]: https://doi.org/10.4050/jahs.3.4
[research_reeder_1959]: https://ntrs.nasa.gov/citations/19980231066
[research_refinement_of_2023]: https://doi.org/10.36652/0869-4931-2023-77-2-86-94
[research_regier_hubbard_1953]: https://doi.org/10.1121/1.1917574
[research_rehm_jansen_1978]: https://doi.org/10.1016/0022-460x(78)90490-x
[research_rehman_2022]: https://doi.org/10.13111/2066-8201.2022.14.3.8
[research_reid_1978]: https://doi.org/10.2514/3.58307
[research_reid_2024]: https://doi.org/10.1016/j.ast.2024.109479
[research_reilly_1970]: https://doi.org/10.21236/ad0881186
[research_reiquam_1982]: https://doi.org/10.2514/3.62574
[research_reising_1996]: https://doi.org/10.21236/ada503312
[research_render_jenkinson_1996]: https://doi.org/10.2514/3.46912
[research_rennison_wilby_1980]: https://doi.org/10.2514/6.1980-998
[research_report_no_1929]: https://doi.org/10.1016/s0016-0032(29)91862-7
[research_report_no_1932]: https://doi.org/10.1016/s0016-0032(32)91222-8
[research_report_no_1932_2]: https://doi.org/10.1016/s0016-0032(32)91220-4
[research_report_no_1932_3]: https://doi.org/10.1016/s0016-0032(32)90109-4
[research_report_no_1932_4]: https://doi.org/10.1016/s0016-0032(32)90588-2
[research_report_no_1932_5]: https://doi.org/10.1016/s0016-0032(32)91416-1
[research_report_no_1935]: https://doi.org/10.1016/s0016-0032(35)90374-x
[research_report_no_1935_2]: https://doi.org/10.1016/s0016-0032(35)91460-0
[research_research_on_2025]: https://doi.org/10.31276/cntt.2024.3063
[research_reussner_1950]: https://doi.org/10.1108/eb031925
[research_reussner_1953]: https://doi.org/10.1108/eb032300
[research_reuter_1939]: https://ntrs.nasa.gov/citations/20090015032
[research_revell_1982]: https://doi.org/10.2514/3.57353
[research_revell_1982_2]: https://doi.org/10.2514/3.57352
[research_revell_balena_1980]: https://doi.org/10.2514/6.1980-1000
[research_revell_balena_1980_b]: https://doi.org/10.2514/6.1980-1001
[research_rexcharles_enyinna_donatus_2026]: https://doi.org/10.62154/ajastr.2026.022.01019
[research_rey_2021]: https://doi.org/10.1016/j.treng.2021.100087
[research_reynolds_1963]: https://doi.org/10.21236/ad0426123
[research_reynolds_2018]: https://ntrs.nasa.gov/citations/20180004464
[research_rezy_stuckas_1979]: https://doi.org/10.4271/790605
[research_rhoads_1952]: https://doi.org/10.21236/ad0014479
[research_rhoads_1967]: https://doi.org/10.21236/ad0820790
[research_rhoads_1970]: https://doi.org/10.21236/ad0876589
[research_rhodes_1982]: https://doi.org/10.1121/1.387863
[research_rhudy_2023]: https://doi.org/10.2514/1.i011221
[research_riboldi_2018]: https://doi.org/10.1016/j.ast.2018.07.042
[research_riboldi_2019]: https://doi.org/10.1016/j.ast.2019.105507
[research_riccardi_mamino_2025]: https://doi.org/10.4050/sm_handling_2025-5298
[research_rice_1946]: https://doi.org/10.21236/adb803248
[research_rice_hazlwood_1994]: https://doi.org/10.2514/6.1994-2166
[research_rice_oetting_1976]: https://doi.org/10.2514/3.44522
[research_richards_attenborough_1986]: https://doi.org/10.1016/s0022-460x(86)80029-3
[research_richardson_1976]: https://doi.org/10.21236/adb012971
[research_riddle_innis_1981]: https://doi.org/10.2514/6.1981-2409
[research_riddle_stevens_1987]: https://doi.org/10.4271/872315
[research_ride_quality_1975]: https://doi.org/10.1016/0022-460x(75)90294-1
[research_rieck_2026]: https://doi.org/10.1007/s13272-026-00991-x
[research_riggins_camberos_2020]: https://doi.org/10.2514/1.c035659
[research_ringland_craig_1977]: https://ntrs.nasa.gov/citations/19780011168
[research_rittenhouse_1959]: https://doi.org/10.21236/ad0207771
[research_rizzi_2016]: https://ntrs.nasa.gov/citations/20160009097
[research_rizzi_2024]: https://doi.org/10.2514/1.c037435
[research_rizzi_christian_2017]: https://ntrs.nasa.gov/citations/20200002352
[research_rizzi_rafaelof_2021]: https://doi.org/10.3397/in-2021-1482
[research_rizzi_scata_jr_2022]: https://doi.org/10.1121/10.0015626
[research_robert_bartels_kevin_jacobson]: https://ntrs.nasa.gov/citations/20230005959
[research_robert_c_platt_1935]: https://ntrs.nasa.gov/citations/19930091614
[research_robert_e_lee_2005]: https://ntrs.nasa.gov/citations/20050210000
[research_robert_g_hoey_1992]: https://ntrs.nasa.gov/citations/19930027287
[research_roberts_1963]: https://doi.org/10.21236/ad0420853
[research_roberts_1964]: https://doi.org/10.21236/ad0608187
[research_roberts_1988]: https://doi.org/10.2514/6.1988-2113
[research_roberts_1988_b]: https://doi.org/10.2514/6.1988-2077
[research_roberts_brown_1988]: https://doi.org/10.2514/6.1988-2083
[research_roberts_shawler_1994]: https://doi.org/10.2514/6.1994-2181
[research_robinson_1979]: https://doi.org/10.1121/1.382748
[research_rockefeller_1937]: https://doi.org/10.2514/8.469
[research_rocket_effect_1937]: https://doi.org/10.2514/8.10178
[research_rodden_1956]: https://doi.org/10.2514/8.3630
[research_rodden_1989]: https://doi.org/10.2514/3.45842
[research_rodden_giesing_1970]: https://doi.org/10.2514/3.44159
[research_rodenhiser_durgin_2007]: https://doi.org/10.2514/1.25060
[research_rodger_dyson]: https://ntrs.nasa.gov/citations/20230006821
[research_rodgers_1966]: https://doi.org/10.2514/3.43765
[research_rogalski_2018]: https://doi.org/10.1108/aeat-02-2018-0088
[research_roger_2022]: https://doi.org/10.1177/1475472x221107372
[research_rogers_2004]: https://ntrs.nasa.gov/citations/20040086693
[research_rogers_cook_1952]: https://doi.org/10.21236/ad0013026
[research_rogers_fasciano_2016]: https://doi.org/10.2514/1.c033430
[research_rohling_1969]: https://doi.org/10.2514/3.44097
[research_rokhsaz_kliment_2017]: https://doi.org/10.2514/1.c033850
[research_romadhon_2024]: https://doi.org/10.56521/teknika.v10i1.1211
[research_roncen_2025]: https://doi.org/10.1016/j.jsv.2025.119058
[research_roos_1985]: https://ntrs.nasa.gov/citations/19850058569
[research_rosales_guijarroreyes_2021]: https://doi.org/10.2514/6.2021-2546
[research_rose_jeracki_1989]: https://ntrs.nasa.gov/citations/19900004036
[research_rosenberg_1944]: https://doi.org/10.2514/8.11091
[research_roskam_1968]: https://doi.org/10.2514/3.43981
[research_roskam_dusto_1969]: https://doi.org/10.2514/3.44100
[research_ross_1984]: https://doi.org/10.2514/3.45004
[research_rossow_1986]: https://doi.org/10.2514/3.45333
[research_rostami_2024]: https://doi.org/10.20944/preprints202406.0862.v1
[research_rotorcraft_handling_2011]: https://doi.org/10.1049/pbce074e_ch11
[research_roudbari_saghafi_2016]: https://doi.org/10.1109/taes.2016.140693
[research_roxner_postolsky_2024]: https://doi.org/10.25144/22991
[research_roy_2009]: https://doi.org/10.21236/ada511003
[research_ruffini_2020]: https://doi.org/10.1007/s40799-020-00394-5
[research_ruijgrok_1980]: https://doi.org/10.1016/0022-460x(80)90358-2
[research_ruijgrok_1983]: https://doi.org/10.2514/3.48197
[research_runyan_1952]: https://doi.org/10.2514/8.2220
[research_runyan_1980]: https://ntrs.nasa.gov/citations/19800051799
[research_ruotolo_1999]: https://doi.org/10.2514/6.1999-1934
[research_rusakov_krupetskyh_2012]: https://doi.org/10.18372/2415-8151.2.6104
[research_rusciano_viscardi_2008]: https://doi.org/10.1121/1.2934066
[research_rutherford_crowder_1958]: https://doi.org/10.1071/es58017
[research_ryan_2022]: https://doi.org/10.1515/noise-2022-0008
[research_ryan_aeronautical_co_san_diego_ca_1963]: https://doi.org/10.21236/ad0426250
[research_ryan_cummings_2016]: https://doi.org/10.1109/thms.2014.2376355
[research_rydin_2018]: https://doi.org/10.1007/s10915-018-0751-5
[research_ryffel_2019]: https://doi.org/10.1080/00140139.2018.1501093
[research_ryu_2022]: https://doi.org/10.2514/1.i010967
[research_s_2018]: https://doi.org/10.1016/j.ifacol.2018.05.052
[research_s_2025_2]: https://doi.org/10.1108/aeat-08-2024-0241
[research_s_d_bainetov_2016]: https://doi.org/10.21557/mth.48304777
[research_s_v_madhusudhana_2024]: https://doi.org/10.34293/acsjse.v4i1.102
[research_saari_wallner_1946]: https://ntrs.nasa.gov/citations/20030063991
[research_saastamoinen_maunula_2021]: https://doi.org/10.1016/j.procs.2021.08.171
[research_sabatini_2015]: https://doi.org/10.1108/aeat-06-2014-0081
[research_sabatini_2026]: https://doi.org/10.2514/1.g009632
[research_sabine_burkhard_1959]: https://doi.org/10.1121/1.1936155
[research_sachs_2016]: https://doi.org/10.3390/aerospace3040031
[research_sachs_dacosta_2003]: https://doi.org/10.2514/6.2003-5303
[research_sachs_gruter_2017]: https://doi.org/10.2514/6.2017-1862
[research_sachs_lenz_2013]: https://doi.org/10.2514/6.2013-4842
[research_sachs_moelyadi_2006]: https://doi.org/10.1016/j.jtbi.2005.07.016
[research_saetti_rogers_2020]: https://doi.org/10.4050/sm_2020_hq-916
[research_sagan_lau_2025]: https://doi.org/10.2514/1.c038007
[research_sahai_2017]: https://doi.org/10.2514/1.c034009
[research_sahai_wefers_2016]: https://doi.org/10.1016/j.apacoust.2015.08.002
[research_sahawneh_2015]: https://doi.org/10.2514/1.i010284
[research_sahithi_2023]: https://doi.org/10.22214/ijraset.2023.53462
[research_sahyoun_2026]: https://doi.org/10.1007/s13272-026-00954-2
[research_sakaliyski_hileman_2007]: https://doi.org/10.2514/6.2007-1032
[research_sakamoto_cota_1965]: https://doi.org/10.21236/ad0615908
[research_sakamoto_takemura_2007]: https://doi.org/10.1115/detc2007-34369
[research_sakthivel_venkatesan_2017]: https://doi.org/10.2514/1.c034226
[research_salikuddin_1990]: https://doi.org/10.1016/0022-460x(90)90714-b
[research_salikuddin_1990_2]: https://doi.org/10.1016/0022-460x(90)90671-l
[research_salikuddin_ahuja_1989]: https://doi.org/10.1016/0022-460x(89)90612-3
[research_saltari_2017]: https://doi.org/10.2514/1.c034159
[research_salucci_2026]: https://doi.org/10.2514/1.c038427
[research_samimy_2003]: https://doi.org/10.21236/ada422153
[research_samimy_2004]: https://doi.org/10.21236/ada423107
[research_sampaio_hernandes_2014]: https://doi.org/10.1109/aero.2014.6836414
[research_sanchez_2024]: https://doi.org/10.3846/aviation.2024.22577
[research_sanchez_galan_2025]: https://doi.org/10.3390/drones9040230
[research_sanders_1957]: https://doi.org/10.1108/eb032813
[research_sandlin_saiki_1993]: https://ntrs.nasa.gov/citations/19930022666
[research_sandstrom_white_1961]: https://doi.org/10.21236/ad0257074
[research_sandu_2025]: https://doi.org/10.13111/2066-8201.2025.17.4.17
[research_sanghi_2024]: https://doi.org/10.2514/1.c037470
[research_sankar_brentner_2008]: https://doi.org/10.21236/ada508845
[research_santos_2023]: https://doi.org/10.3397/in_2023_0504
[research_santoso_hariyanto_2022]: https://doi.org/10.28989/vortex.v3i2.1236
[research_sanz_1986]: https://doi.org/10.2514/3.9447
[research_saracyakupoglu_2022]: https://doi.org/10.46519/ij3dptdi.1128158
[research_saravo_1976]: https://doi.org/10.2514/6.1976-902
[research_sarup_2025]: https://doi.org/10.3390/wevj16090530
[research_sarup_2026]: https://doi.org/10.3390/wevj17030126
[research_sasaki_torise_2012]: https://doi.org/10.4236/ojfd.2012.24a035
[research_sathish_kumar_sunnam_et_al_2019]: https://doi.org/10.24247/ijmperdaug201984
[research_satria_palar_2024]: https://doi.org/10.2514/1.c037848
[research_satuluri_seeni_2022]: https://doi.org/10.1149/10701.0837ecst
[research_saucez]: https://doi.org/10.70675/f03a0681z9efcz414ez8944zcc71830d8acb
[research_savory_toy_1984]: https://doi.org/10.1049/sm.1984.0028
[research_sawake_2026]: https://doi.org/10.22214/ijraset.2026.79088
[research_sawyer_1967]: https://doi.org/10.1016/0022-460x(67)90115-0
[research_scanlan_1948]: https://doi.org/10.21236/ada955900
[research_schade_1952]: https://doi.org/10.2514/8.2396
[research_schade_crane_1965]: https://ntrs.nasa.gov/citations/20000012002
[research_schaeffer_sternfeld_1978]: https://ntrs.nasa.gov/citations/19790002683
[research_schaffer_bertsch_2023]: https://doi.org/10.3397/in_2022_0182
[research_schaffer_bertsch_2023_b]: https://doi.org/10.25144/14823
[research_schairer_1937]: https://doi.org/10.2514/8.498
[research_schairer_1971]: https://doi.org/10.2514/3.44221
[research_scharine_letowski_2013]: https://doi.org/10.21236/ada588880
[research_schauerhamer_robinson_2017]: https://doi.org/10.2514/1.c034187
[research_scherrer_dennis_1951]: https://ntrs.nasa.gov/citations/19930086518
[research_schieni_2024]: https://doi.org/10.2514/1.g008048
[research_schlinker_1979]: https://doi.org/10.2514/3.46348
[research_schneiter_watson_1948]: https://ntrs.nasa.gov/citations/19930082263
[research_schofield_1984]: https://ntrs.nasa.gov/citations/19850001750
[research_schollenberger_2025]: https://doi.org/10.1007/s13272-025-00869-4
[research_scholz_2021]: https://doi.org/10.31224/osf.io/zdgcn
[research_schomer_1991]: https://doi.org/10.21236/ada243719
[research_schreadley_1977]: https://doi.org/10.21236/ada043979
[research_schreckenberg_2023]: https://doi.org/10.3397/in_2022_0794
[research_schreder_1975]: https://doi.org/10.4271/750510
[research_schrenk_1932]: https://ntrs.nasa.gov/citations/19930094751
[research_schriever_1952]: https://doi.org/10.1190/1.1437827
[research_schuet_2017]: https://doi.org/10.2514/1.g001729
[research_schulderfrei_1951]: https://ntrs.nasa.gov/citations/19930083056
[research_schumacher_1952]: https://doi.org/10.21236/ada075866
[research_schutte_hummel_2023]: https://doi.org/10.2514/1.c037128
[research_schutz_kutrzyba_2000]: https://doi.org/10.21236/ada389329
[research_schwab_zellmann_2020]: https://doi.org/10.2514/1.c035779
[research_schwartz_1976]: https://ntrs.nasa.gov/citations/19760058011
[research_schwartz_1986]: https://ntrs.nasa.gov/citations/19860017810
[research_schwartz_wray_1969]: https://doi.org/10.21236/ad0864071
[research_schy_hannah_1977]: https://doi.org/10.2514/3.58787
[research_scientific_and_1952]: https://doi.org/10.1108/eb032206
[research_scoppe_1973]: https://doi.org/10.21236/ad0771965
[research_scordamaglia_2025]: https://doi.org/10.1109/ojcsys.2025.3619810
[research_seacord_teitelbaum_1947]: https://ntrs.nasa.gov/citations/20010062501
[research_sears_1948]: https://doi.org/10.1090/qam/27194
[research_sears_1974]: https://doi.org/10.2514/3.60348
[research_sears_1990]: https://doi.org/10.2514/3.45918
[research_secco_martins_2019]: https://doi.org/10.2514/1.c034934
[research_seckel_graziani_1956]: https://doi.org/10.21236/ad0119202
[research_secretaryoftheairforcewashingtondc_2001]: https://doi.org/10.21236/ada433970
[research_sedunov_2018]: https://doi.org/10.1121/1.5036415
[research_sedunov_2019]: https://doi.org/10.1121/1.5136640
[research_segall_gardner_2026]: https://doi.org/10.2514/6.2026-4315
[research_seginer_salomon_1983]: https://ntrs.nasa.gov/citations/19830013888
[research_seidaliyeva_2023]: https://doi.org/10.3390/s24010125
[research_sekaran_1983]: https://doi.org/10.2514/3.28362
[research_sekhmistro_shapovalov_2023]: https://doi.org/10.30837/rt.2023.3.214.06
[research_sells_crossley_2023]: https://doi.org/10.2514/1.c036330
[research_semrau_1974]: https://doi.org/10.21236/ada001737
[research_sen_1987]: https://doi.org/10.1080/00207178708933768
[research_senol_2020]: https://doi.org/10.1108/aeat-03-2020-0058
[research_serra_branco_2026]: https://doi.org/10.1007/s44465-026-00035-y
[research_sesham_2026]: https://doi.org/10.1007/s44163-026-00869-1
[research_setiawan_2026]: https://doi.org/10.55927/ijis.v5i4.23
[research_seville_research_corp_pensacola_fl_1979]: https://doi.org/10.21236/ada092021
[research_shafer_1991]: https://ntrs.nasa.gov/citations/19910063180
[research_shafer_1992]: https://ntrs.nasa.gov/citations/19920019867
[research_shahady_1975]: https://doi.org/10.2514/3.59851
[research_shaikn_1979]: https://doi.org/10.1121/1.382659
[research_shan_2025]: https://doi.org/10.3390/wevj16040212
[research_shang_2007]: https://doi.org/10.21236/ada476250
[research_shang_2025]: https://doi.org/10.1049/pel2.70134
[research_shankar_1972]: https://doi.org/10.1016/0022-460x(72)90538-x
[research_shankar_l_2023]: https://doi.org/10.18090/samriddhi.v15i03.06
[research_shannon_wang_1973]: https://doi.org/10.21236/ad0764866
[research_shao_2025]: https://doi.org/10.3390/aerospace12100859
[research_shao_2026]: https://doi.org/10.1016/j.ast.2026.112387
[research_shapiro_sherman_edwards_1967]: https://doi.org/10.1108/eb034234
[research_sharma_2016]: https://doi.org/10.15394/ijaaa.2016.1146
[research_shaw_1988]: https://doi.org/10.2514/3.45555
[research_shayak_2024]: https://doi.org/10.3389/fpace.2024.1308872
[research_shearwood_2020]: https://doi.org/10.3390/aerospace7100150
[research_sheffield_2000]: https://doi.org/10.21236/ada389709
[research_shelley_2018]: https://doi.org/10.26686/pq.v14i3.5107
[research_shen_2021]: https://doi.org/10.1016/j.cja.2020.07.022
[research_shenstone_1938]: https://doi.org/10.1017/s0368393100104183
[research_shenstone_1946]: https://doi.org/10.1108/eb031356
[research_shenstone_1953]: https://doi.org/10.1108/eb032247
[research_shi_2023]: https://doi.org/10.1088/1742-6596/2658/1/012023
[research_shi_2023_2]: https://doi.org/10.1007/s00158-023-03559-z
[research_shi_2024]: https://doi.org/10.3390/en17040786
[research_shi_wan_2015]: https://doi.org/10.1108/aeat-01-2013-0004
[research_shields_bass_1977]: https://ntrs.nasa.gov/citations/19770021966
[research_shimoyama_kamisori_2017]: https://doi.org/10.2514/1.c033978
[research_shin_2018]: https://doi.org/10.1061/(asce)as.1943-5525.0000832
[research_shindo_joppa_1980]: https://ntrs.nasa.gov/citations/19810016502
[research_shirbhate_2025]: https://doi.org/10.1007/s12046-025-02838-3
[research_shivashankara_1978]: https://doi.org/10.2514/3.58412
[research_shivashankara_1983]: https://doi.org/10.2514/3.44858
[research_shivashankara_stubbs_1987]: https://doi.org/10.2514/3.45517
[research_shmelv_vladov_2019]: https://doi.org/10.30929/1995-0519.2019.1.27-32
[research_shmilovich_2026]: https://doi.org/10.2514/1.c037586
[research_shmilovich_princen_2026]: https://doi.org/10.2514/1.c038755
[research_shmilovich_yadlin_2023]: https://doi.org/10.2514/6.2023-0655
[research_shomber_gertsen_1967]: https://doi.org/10.2514/3.43851
[research_shortal_1934]: https://ntrs.nasa.gov/citations/19930081536
[research_shovlin_1979]: https://ntrs.nasa.gov/citations/19790056747
[research_showers_1952]: https://doi.org/10.21236/ada075980
[research_shreve_1977]: https://doi.org/10.4271/770443
[research_shrey_j_mistry_et_al_2018]: https://doi.org/10.24247/ijmperdjun20181
[research_shrivastava_stengel_1989]: https://ntrs.nasa.gov/citations/19890035138
[research_shubert_jones_2025]: https://doi.org/10.4050/sm_handling_2025-5291
[research_si_2023]: https://doi.org/10.3390/drones7100612
[research_sibert_1943]: https://doi.org/10.2514/8.10986
[research_sibert_1947]: https://doi.org/10.2514/8.1376
[research_siddavatam_2024]: https://doi.org/10.3390/wevj15050187
[research_siddiqui_2023]: https://doi.org/10.1007/s11012-023-01649-2
[research_sidhu_2023]: https://doi.org/10.64336/001c.70226
[research_siegel_crain_1960]: https://doi.org/10.21236/ad0245849
[research_siegel_lanterman_1963]: https://doi.org/10.21236/ad0298331
[research_sikora_mendenhall_1974]: https://doi.org/10.1007/bf02323323
[research_silvestre_2013]: https://doi.org/10.1007/978-3-642-38253-6_37
[research_silvestre_luckner_2015]: https://doi.org/10.2514/1.j054023
[research_sim_1990]: https://ntrs.nasa.gov/citations/19910000766
[research_sim_curry_1978]: https://ntrs.nasa.gov/citations/19790001897
[research_sim_curry_1985]: https://ntrs.nasa.gov/citations/19870009137
[research_simcox_1976]: https://doi.org/10.2514/3.58676
[research_simizu_1944]: https://doi.org/10.1299/kikai1938.9.37-1_210
[research_simmonds_1967]: https://doi.org/10.21236/ad0820762
[research_simmonds_1967_2]: https://doi.org/10.21236/ad0820760
[research_simmonds_1967_3]: https://doi.org/10.21236/ad0820761
[research_simmons_2019]: https://doi.org/10.2514/1.c035160
[research_simmons_2023]: https://doi.org/10.2514/1.c036896
[research_simmons_2023_2]: https://doi.org/10.2514/1.c037260
[research_simmons_2023_3]: https://doi.org/10.2514/1.c036773
[research_simmons_2023_4]: https://doi.org/10.2514/1.c037259
[research_simon_2023]: https://doi.org/10.3397/in_2022_0091
[research_simpson_1979]: https://doi.org/10.21236/ada075226
[research_simpson_1990]: https://doi.org/10.2514/3.45954
[research_sims_kimberlin_1995]: https://doi.org/10.2514/6.1995-3938
[research_simson_2024]: https://doi.org/10.25144/22197
[research_simulation_in_1988]: https://doi.org/10.2514/6.1988-2130
[research_sinacori_lange_1961]: https://doi.org/10.21236/ad0266422
[research_sinha_ravande_2006]: https://doi.org/10.2514/6.2006-447
[research_sinkovec_loshek_2015]: https://doi.org/10.2514/6.2015-1888
[research_siqueira_2025]: https://doi.org/10.3846/aviation.2025.23175
[research_sivells_neely_1947]: https://ntrs.nasa.gov/citations/19930091938
[research_slater_1955]: https://doi.org/10.1002/j.1477-8696.1955.tb00219.x
[research_sleeman_1971]: https://doi.org/10.2514/3.59114
[research_slewert_stewart_1967]: https://doi.org/10.2514/3.59308
[research_sliwa_sliwa_1979]: https://ntrs.nasa.gov/citations/19790018901
[research_smaili_2018]: https://doi.org/10.2514/1.c034422
[research_smith]: https://doi.org/10.33915/etd.1943
[research_smith_1977]: https://doi.org/10.21236/ada069198
[research_smith_1983]: https://doi.org/10.2307/3104760
[research_smith_2023]: https://doi.org/10.4050/sm_2023_hq-1192
[research_smith_bernier_1966]: https://doi.org/10.21236/ad0375124
[research_smith_geddes_1979]: https://doi.org/10.21236/ada077858
[research_smith_kroo_1990]: https://ntrs.nasa.gov/citations/19900063583
[research_snell_1991]: https://ntrs.nasa.gov/citations/19910065049
[research_snell_1993]: https://ntrs.nasa.gov/citations/19930067373
[research_sntvedt_1974]: https://doi.org/10.1016/0045-7949(74)90082-0
[research_snyder_1950]: https://doi.org/10.21236/ad0109766
[research_snyder_kohlman_2018]: https://ntrs.nasa.gov/citations/20180004867
[research_sobester_2021]: https://doi.org/10.2514/1.c036180
[research_socha_2026]: https://doi.org/10.1016/j.apergo.2025.104713
[research_soderman_2006]: https://ntrs.nasa.gov/citations/20110013067
[research_soderman_noble_1975]: https://doi.org/10.2514/3.59813
[research_sohail_muhammad_2011]: https://doi.org/10.1063/1.3651865
[research_soinne_1999]: https://doi.org/10.2514/6.1999-3147
[research_solies_1995]: https://doi.org/10.2514/6.1995-3912
[research_soltmann_hall_2017]: https://doi.org/10.2514/1.c033982
[research_somers_1977]: https://ntrs.nasa.gov/citations/19770011105
[research_somers_1981]: https://ntrs.nasa.gov/citations/19820045882
[research_somers_foster_1979]: https://ntrs.nasa.gov/citations/19790018927
[research_somerville_2025]: https://doi.org/10.3390/mti9030024
[research_somerville_2026]: https://doi.org/10.3390/sci8040070
[research_somerville_2026_2]: https://doi.org/10.3390/technologies14020094
[research_sommer_tapscott_1966]: https://ntrs.nasa.gov/citations/19660027560
[research_somsel_1970]: https://doi.org/10.21236/ad0703719
[research_son_yee_2018]: https://doi.org/10.2514/1.c034490
[research_soneda_2019]: https://doi.org/10.1299/jsmetld.2019.28.1008
[research_sonmez_alemdaroglu_2015]: https://doi.org/10.4028/www.scientific.net/amm.798.556
[research_soom_gu_1981]: https://doi.org/10.1121/1.386944
[research_soovere_1982]: https://doi.org/10.2514/3.44755
[research_soovere_1985]: https://doi.org/10.2514/3.45117
[research_soule_wetmore_1933]: https://ntrs.nasa.gov/citations/19930081319
[research_source_noise_1975]: https://doi.org/10.2514/5.9781600865121.0157.0178
[research_southerland_platus_1986]: https://doi.org/10.21236/ada401387
[research_spada_2017]: https://doi.org/10.1016/j.ast.2017.01.010
[research_spano_cuomo_guglieri_2021]: https://doi.org/10.1142/s2301385021500072
[research_sparks_moerder_2002]: https://ntrs.nasa.gov/citations/20030013634
[research_speakman_1978]: https://doi.org/10.21236/ada053701
[research_spearman_webster_1951]: https://ntrs.nasa.gov/citations/19930086448
[research_spencer_1969]: https://doi.org/10.21236/ad0864116
[research_sperry_1979]: https://doi.org/10.3397/1.2832120
[research_sponder_1950]: https://ntrs.nasa.gov/citations/20050028453
[research_sree_2015]: https://ntrs.nasa.gov/citations/20150008245
[research_srijayantha_1983]: https://ntrs.nasa.gov/citations/19840003043
[research_srinathkumar_2015]: https://doi.org/10.4050/jahs.60.022010
[research_srivastava_2016]: https://doi.org/10.2514/1.c033722
[research_staats_2025]: https://doi.org/10.3390/aerospace12121085
[research_stabeli_diehl_2025]: https://doi.org/10.3397/in_2025_1073187
[research_stallings_hartman_1981]: https://doi.org/10.21236/ada103383
[research_stalnov_2022]: https://doi.org/10.1121/10.0011546
[research_stange_1959]: https://doi.org/10.21236/ada955359
[research_starr_sernas_1975]: https://doi.org/10.2514/3.44424
[research_steen_1994]: https://ntrs.nasa.gov/citations/19950022917
[research_steger_bailey_1980]: https://doi.org/10.2514/3.50756
[research_steiner_pratt_1967]: https://doi.org/10.2514/3.43849
[research_stengel_1975]: https://doi.org/10.2514/3.44482
[research_stengel_1980]: https://doi.org/10.2514/3.55959
[research_stenzel_1947]: https://doi.org/10.21236/ada037035
[research_stephen_j_wright]: https://ntrs.nasa.gov/citations/20210026290
[research_stephens_2010]: https://ntrs.nasa.gov/citations/20100042194
[research_stephens_2013]: https://ntrs.nasa.gov/citations/20140000338
[research_stephenson_1990]: https://ntrs.nasa.gov/citations/19900014097
[research_stephenson_2019]: https://doi.org/10.1121/1.5092213
[research_stepniewski_1940]: https://doi.org/10.1108/eb030722
[research_sternfield_1954]: https://doi.org/10.2514/8.2988
[research_stewart_1939]: https://doi.org/10.2514/8.879
[research_stewart_2008]: https://ntrs.nasa.gov/citations/20080012495
[research_stewart_2012]: https://doi.org/10.21236/ada563620
[research_stewart_2016]: https://doi.org/10.2514/6.2016-0274
[research_stokes_davis_1953]: https://ntrs.nasa.gov/citations/19930083683
[research_stoliker_bosworth_1996]: https://ntrs.nasa.gov/citations/19970004646
[research_stoll_stilson_2013]: https://doi.org/10.2514/6.2013-4374
[research_stone_1945]: https://doi.org/10.21236/ada801302
[research_stottier_1995]: https://doi.org/10.21236/ada293962
[research_stough_1987]: https://ntrs.nasa.gov/citations/19870014181
[research_strailman_1952]: https://doi.org/10.1109/ee.1952.6437597
[research_stratford_1948]: https://doi.org/10.1108/eb031680
[research_strattan_1978]: https://doi.org/10.21236/ada052447
[research_strelkov_kharlamov_1967]: https://doi.org/10.1007/bf01040744
[research_stresses_in_1938]: https://doi.org/10.1016/s0016-0032(38)90054-7
[research_strier_1955]: https://doi.org/10.21236/ad0073570
[research_strike_w_t_1982]: https://doi.org/10.21236/ada116279
[research_stuart_1943]: https://doi.org/10.2514/8.11009
[research_su_2025]: https://doi.org/10.1177/1475472x251350278
[research_suarez_1993]: https://ntrs.nasa.gov/citations/19930038615
[research_succi_1981]: https://ntrs.nasa.gov/citations/19820019213
[research_succi_1983]: https://doi.org/10.1016/0022-460x(83)90385-1
[research_sudha_2018]: https://doi.org/10.2514/1.c034585
[research_suit_batterson_1986]: https://ntrs.nasa.gov/citations/19860015232
[research_sulc_1982]: https://doi.org/10.1016/0022-460x(82)90435-7
[research_suleman_2016]: https://doi.org/10.1017/aer.2016.94
[research_sullivan_clancy_1989]: https://doi.org/10.2514/6.1989-3385
[research_sun_2019]: https://doi.org/10.2514/1.c035135
[research_sun_2020]: https://doi.org/10.1016/j.trc.2020.01.026
[research_sun_2020_2]: https://doi.org/10.1016/j.ast.2020.106126
[research_sun_2020_3]: https://doi.org/10.3390/app10072243
[research_sun_2023_2]: https://doi.org/10.3390/drones7040252
[research_sun_2026]: https://doi.org/10.61173/f2703w61
[research_sunago_sasaki_2009]: https://doi.org/10.2514/1.40726
[research_surkova_dolhoierova_2025]: https://doi.org/10.33251/2522-1477-2025-14-112-123
[research_sutherland_wesler_1990]: https://ntrs.nasa.gov/citations/19900015545
[research_suvarna_shukla_2022]: https://doi.org/10.2514/6.2022-4061
[research_suzuki_kawamura_1995]: https://doi.org/10.2514/6.1995-1225
[research_suzuki_kawamura_1996]: https://doi.org/10.2514/3.46982
[research_svane_plovsing_2024]: https://doi.org/10.25144/21507
[research_svatos_2021]: https://doi.org/10.21014/acta_imeko.v10i2.1041
[research_svendsen_1994]: https://doi.org/10.2514/6.1994-2160
[research_swaim_1969]: https://doi.org/10.2514/3.44031
[research_swaim_1970]: https://doi.org/10.2514/3.44151
[research_swaim_1971]: https://doi.org/10.2514/3.44230
[research_swaim_connor_1968]: https://doi.org/10.2514/3.43907
[research_swaim_staab_1978]: https://doi.org/10.2514/3.58377
[research_swaim_yen_1979]: https://doi.org/10.2514/3.58579
[research_swaminathan_mohan_2018]: https://doi.org/10.2514/6.2018-2832
[research_swarnkar_kothari_2016]: https://doi.org/10.1016/j.ifacol.2016.03.117
[research_swearingen_2006]: https://doi.org/10.21236/ada457441
[research_swearingen_white_2020]: https://doi.org/10.1121/1.5147606
[research_sydney_schnulo]: https://ntrs.nasa.gov/citations/20205005264
[research_szalai_1967]: https://ntrs.nasa.gov/citations/19670017216
[research_szczyglowski_2019]: https://doi.org/10.2514/1.c035452
[research_sziroczak_2020]: https://doi.org/10.1016/j.energy.2020.117937
[research_tabassum_bai_2022]: https://doi.org/10.1016/j.ast.2021.107323
[research_tai_1993]: https://doi.org/10.2514/6.1993-523
[research_tai_2023]: https://doi.org/10.3390/aerospace10040350
[research_tai_2023_2]: https://doi.org/10.2514/1.j062188
[research_tai_2024]: https://doi.org/10.1016/j.cja.2024.05.031
[research_tai_2025]: https://doi.org/10.1016/j.ast.2024.109788
[research_takahashi_2023]: https://doi.org/10.3397/in_2023_0588
[research_takaishi_2023]: https://doi.org/10.3397/in_2023_0112
[research_takaishi_2024]: https://doi.org/10.3397/1/377221
[research_takeda_1970]: https://doi.org/10.5100/jje.6.137
[research_takeya_okumoto_1959]: https://doi.org/10.5636/jgg.10.118
[research_tam_1987]: https://doi.org/10.1016/s0022-460x(87)81303-2
[research_tam_2015]: https://doi.org/10.21236/ada616071
[research_tan_plotkin_1986]: https://doi.org/10.2514/3.9413
[research_tanaka_1985]: https://doi.org/10.1121/1.392718
[research_tang_2016]: https://doi.org/10.1016/j.cja.2015.12.001
[research_tangler_1979]: https://doi.org/10.21236/ada074141
[research_tantaroudas_karachalios_2026]: https://doi.org/10.24132/acm.2026.1114
[research_tapscott_1964]: https://doi.org/10.4050/vfs-f20-002
[research_tarnopolsky_1978]: https://doi.org/10.1016/0022-460x(78)90482-0
[research_tarnow_pommer_1988]: https://doi.org/10.1121/1.396353
[research_tavella_1987]: https://doi.org/10.2514/3.45485
[research_tay_chong_2025]: https://doi.org/10.3390/biomimetics10040253
[research_taylor_1973]: https://doi.org/10.21236/ad0759177
[research_taylor_1984]: https://doi.org/10.1016/0022-460x(84)90582-0
[research_taylor_2011]: https://ntrs.nasa.gov/citations/20110015943
[research_taylor_miller_1982]: https://ntrs.nasa.gov/citations/19820036251
[research_taylor_papadales_1976]: https://doi.org/10.2514/6.1976-876
[research_teixeira_cesnik_2019]: https://doi.org/10.2514/1.j057575
[research_teixeira_cesnik_2020]: https://doi.org/10.1017/aer.2019.165
[research_tenhave_2026]: https://doi.org/10.3390/aerospace13010059
[research_teper_stapleford_1966]: https://doi.org/10.2514/3.43725
[research_terashima_2021]: https://doi.org/10.1250/ast.42.344
[research_terzakis_2025]: https://doi.org/10.1051/aacus/2025050
[research_tester_1973]: https://doi.org/10.1016/s0022-460x(73)80102-6
[research_tester_1973_2]: https://doi.org/10.1016/s0022-460x(73)80359-1
[research_tetlow_1983]: https://doi.org/10.1016/0261-3069(83)90216-9
[research_thalheimer_2021]: https://doi.org/10.3397/in-2021-1694
[research_the_development_1948]: https://doi.org/10.1037/e512322009-001
[research_the_drag_1999]: https://doi.org/10.1142/9781848160897_0003
[research_the_influence_2011]: https://doi.org/10.1201/b12545-9
[research_the_main_2011]: https://doi.org/10.1201/b12545-6
[research_the_measurement_1976]: https://doi.org/10.1016/0022-460x(76)90852-x
[research_the_pearson_1930]: https://doi.org/10.1108/eb029311
[research_the_sailplane_1948]: https://doi.org/10.1029/tr029i005p00631
[research_the_sailplane_1999]: https://doi.org/10.1142/9781848160897_0007
[research_the_simplification_1936]: https://doi.org/10.1108/eb030011
[research_thelander_1965]: https://doi.org/10.21236/ad0617354
[research_theodorsen_1960]: https://doi.org/10.21236/ad0240849
[research_theodorsen_1960_2]: https://doi.org/10.21236/ad0240956
[research_theodorsen_nomicos_1961]: https://doi.org/10.21236/ad0266411
[research_thirtyacre_2021]: https://doi.org/10.15394/ijaaa.2021.1584
[research_thomas_1961]: https://doi.org/10.21236/ad0400231
[research_thomas_1961_2]: https://doi.org/10.21236/ad0400232
[research_thomas_2003]: https://doi.org/10.2514/6.2003-2776
[research_thomas_hansman_2019]: https://doi.org/10.2514/1.c035100
[research_thomas_hansman_2020]: https://doi.org/10.2514/6.2020-2877
[research_thomas_hansman_2021]: https://doi.org/10.2514/1.c036177
[research_thomas_jones_1982]: https://doi.org/10.1016/0022-460x(82)90536-3
[research_thomason_1967]: https://doi.org/10.21236/ad0379058
[research_thompson_2014]: https://doi.org/10.2514/6.2014-2875
[research_thomson_1946]: https://doi.org/10.2514/8.11345
[research_thomson_1983]: https://doi.org/10.1121/1.388926
[research_thorpe_1970]: https://doi.org/10.1121/1.1912069
[research_thorson_bohne_1960]: https://doi.org/10.2514/8.8416
[research_thottathil_varghese_2022]: https://doi.org/10.32604/sv.2022.016180
[research_timushev_yakovlev_2021]: https://doi.org/10.36336/akustika202141100
[research_tipton_sparrow_2019]: https://doi.org/10.1121/1.5101904
[research_tittel_2010]: https://doi.org/10.21236/ada523208
[research_tobak_schiff_1975]: https://doi.org/10.2514/3.49699
[research_toffol_2024]: https://doi.org/10.3390/app14219883
[research_tokashiki_2023]: https://doi.org/10.3397/in_2023_0783
[research_tokugawa_2026]: https://doi.org/10.2514/1.c038397
[research_toll_1943]: https://ntrs.nasa.gov/citations/19930092922
[research_tomaszewski_goraj_2019]: https://doi.org/10.1108/aeat-03-2018-0099
[research_tombolato_2024]: https://doi.org/10.1515/noise-2024-0006
[research_tong_2023]: https://doi.org/10.3390/aerospace10100886
[research_tong_hu_2013]: https://doi.org/10.1109/chinasip.2013.6625289
[research_torenbeek_wittenberg_1983]: https://doi.org/10.2514/3.44920
[research_torija_martinez_2023]: https://doi.org/10.1121/10.0018828
[research_townsend_1966]: https://doi.org/10.1108/eb034163
[research_townsend_phillips_1955]: https://doi.org/10.21236/ad0080282
[research_townsend_phillips_1956]: https://doi.org/10.21236/ad0088187
[research_tracy_1981]: https://doi.org/10.2514/6.1981-2464
[research_tracy_2024]: https://doi.org/10.3397/nc_2024_0053
[research_tracy_sturdza_2002]: https://doi.org/10.2514/6.2002-146
[research_trascinelli_2026]: https://doi.org/10.1017/jfm.2026.11801
[research_traub_2016]: https://doi.org/10.2514/1.c033491
[research_traub_2016_b]: https://doi.org/10.2514/1.c033416
[research_traub_2017]: https://doi.org/10.2514/1.c034023
[research_traven_whitley_1995]: https://doi.org/10.21236/ada300965
[research_trethewey_1988]: https://doi.org/10.3397/1.2827700
[research_trevelyan_blundell_1949]: https://doi.org/10.1017/s0001925900000093
[research_trevino_1986]: https://doi.org/10.2514/3.45372
[research_trikootam_hornikx_2019]: https://doi.org/10.1016/j.buildenv.2018.11.037
[research_trillo_1966]: https://doi.org/10.1016/0022-460x(66)90111-8
[research_trinks_haseborg_1982]: https://doi.org/10.1109/taes.1982.313318
[research_tritschler_oconnor_2016]: https://doi.org/10.2514/1.g000401
[research_troian_2017]: https://doi.org/10.1016/j.jsv.2016.10.014
[research_trollip_1977]: https://doi.org/10.21236/ada043246
[research_truong_2024]: https://doi.org/10.3390/drones8120774
[research_tsatsas_2022]: https://doi.org/10.1061/(asce)as.1943-5525.0001390
[research_tsoubanos_1979]: https://doi.org/10.21236/ada065018
[research_tsouka_2024]: https://doi.org/10.25144/19354
[research_tsuji_2024]: https://doi.org/10.12792/jiiae.12.42
[research_tsutsumino_2025]: https://doi.org/10.3397/in_2025_1060169
[research_tuck_2018]: https://doi.org/10.1139/juvs-2018-0006
[research_tucker_1999]: https://ntrs.nasa.gov/citations/20000025333
[research_turkdogru_gurun_2021]: https://doi.org/10.3397/in-2021-1382
[research_turner_1942]: https://doi.org/10.1108/eb030873
[research_turriziani_1979]: https://ntrs.nasa.gov/citations/19790019963
[research_tweeddale_1941]: https://doi.org/10.1121/1.1916124
[research_tyler_towle_1955]: https://doi.org/10.1121/1.2369150
[research_typical_aircraft_1989]: https://doi.org/10.1017/cbo9780511584527.016
[research_uddin_2021]: https://doi.org/10.1109/access.2021.3074966
[research_uhl_2003]: https://doi.org/10.1117/12.501838
[research_ulry_1976]: https://doi.org/10.21236/ada041208
[research_ulvr_2026]: https://doi.org/10.3389/fpsyg.2026.1898551
[research_underwood_1942]: https://ntrs.nasa.gov/citations/19930092768
[research_underwood_1942_2]: https://ntrs.nasa.gov/citations/19930092755
[research_unmanned_and_2015]: https://doi.org/10.4172/2168-9792.1000140
[research_unruh_1980]: https://doi.org/10.2514/6.1980-1037
[research_unruh_1981]: https://doi.org/10.2514/3.57545
[research_unruh_1987]: https://doi.org/10.2514/3.45499
[research_unruh_1988]: https://doi.org/10.2514/3.45654
[research_unruh_1988_b]: https://doi.org/10.2514/6.1988-267
[research_unruh_1989]: https://ntrs.nasa.gov/citations/19890019784
[research_unruh_2002]: https://ntrs.nasa.gov/citations/20020059663
[research_use_of_1974]: https://doi.org/10.1016/0010-4361(74)90389-9
[research_usov_2026]: https://doi.org/10.1177/1475472x261473630
[research_uzun_2025]: https://doi.org/10.30518/jav.1583881
[research_vagianos_rooney_1964]: https://doi.org/10.21236/ad0625722
[research_vaicaitis_1980]: https://doi.org/10.2514/3.57877
[research_vaicaitis_mixson_1985]: https://doi.org/10.2514/3.45126
[research_valentine_kader_1976]: https://doi.org/10.21236/ada035756
[research_van_2019]: https://doi.org/10.1016/j.ifacol.2019.11.295
[research_van_baelen_2020]: https://doi.org/10.2514/1.g004596
[research_van_dam_1980]: https://ntrs.nasa.gov/citations/19800059144
[research_van_dam_1981]: https://ntrs.nasa.gov/citations/19810058359
[research_van_dam_1981_2]: https://doi.org/10.2514/3.57531
[research_van_dommelen_1995]: https://doi.org/10.21236/ada329654
[research_van_gool_1982]: https://doi.org/10.2514/3.56164
[research_van_rooyen_eshelby_1981]: https://doi.org/10.2514/3.44710
[research_vance_1991]: https://doi.org/10.21236/ada247040
[research_vandeventer_1979]: https://doi.org/10.4271/790594
[research_vangaasbeek_1980]: https://doi.org/10.21236/ada089008
[research_vanpelt_1981]: https://doi.org/10.2514/6.1981-2375
[research_vantreuren_wisniewski_2019]: https://doi.org/10.1115/gt2019-90534
[research_vanwyckhouse_1966]: https://doi.org/10.21236/ad0630927
[research_vaughn_2023]: https://doi.org/10.3397/in_2023_0226
[research_vaughn_lindsay_1988]: https://doi.org/10.2514/6.1988-2102
[research_vaughn_miltone_2008]: https://doi.org/10.21236/ada476334
[research_vecchiotti_2024]: https://doi.org/10.3390/acoustics6020026
[research_vechtel_buch_2022]: https://doi.org/10.1007/s13272-022-00595-1
[research_vegh_2025]: https://doi.org/10.2514/1.c038393
[research_veley_2008]: https://doi.org/10.21236/ada478915
[research_velger_shinar_1983]: https://doi.org/10.2514/3.44823
[research_venkataraman_2017]: https://doi.org/10.2514/1.c033832
[research_venkataraman_2019]: https://doi.org/10.1016/j.conengprac.2018.12.002
[research_venkataraman_seiler_2019]: https://doi.org/10.2514/1.c035141
[research_venkatesh_2025]: https://doi.org/10.34218/ijmet_16_01_006
[research_vepa_2018]: https://doi.org/10.3390/aerospace5010021
[research_vepa_2020]: https://doi.org/10.1201/9780429202315-6
[research_verba_2024]: https://doi.org/10.18127/j20700784-202404-01
[research_versiani_2019]: https://doi.org/10.1016/j.ast.2019.01.058
[research_vicory_1968]: https://doi.org/10.21236/ad0676791
[research_vidan_2016]: https://doi.org/10.19062/2247-3173.2016.18.1.28
[research_vidovic_2022]: https://doi.org/10.1016/j.trpro.2022.09.022
[research_vilchismedina_siegel_2018]: https://doi.org/10.1109/icarcv.2018.8581107
[research_vilchismedina_siegel_2019]: https://doi.org/10.4204/eptcs.306.37
[research_vile_2020]: https://doi.org/10.1049/cth2.12042
[research_viswanathan_2018]: https://doi.org/10.1177/1475472x18778279
[research_vitsas_2016]: https://doi.org/10.1061/(asce)as.1943-5525.0000589
[research_vlaskamp_2025]: https://doi.org/10.1016/j.ergon.2025.103733
[research_vlaskamp_2026]: https://doi.org/10.1007/s10111-026-00888-z
[research_vlaskamp_2026_2]: https://doi.org/10.1007/s10111-026-00866-5
[research_vlasov_ovdienko_2020]: https://doi.org/10.1088/1742-6596/1560/1/012059
[research_vollo_brassaw_1956]: https://doi.org/10.21236/ad0102193
[research_vomaske_1961]: https://ntrs.nasa.gov/citations/19980227082
[research_von_karman_tsien_1945]: https://doi.org/10.1090/qam/12010
[research_voss_ohme_2018]: https://doi.org/10.1007/s13272-018-0300-9
[research_vranics_2020]: https://doi.org/10.32560/rk.2020.1.12
[research_vulkan_hyde_1981]: https://doi.org/10.3397/1.2832177
[research_w_bauer_2025]: https://doi.org/10.3397/in_2025_1076556
[research_waddington_2023]: https://doi.org/10.2514/1.c037237
[research_wagdi_1977]: https://doi.org/10.2514/3.58903
[research_wahler_2025]: https://doi.org/10.3390/aerospace12020077
[research_wahler_2025_2]: https://doi.org/10.2514/1.c037516
[research_walchner_1969]: https://doi.org/10.21236/ad0700062
[research_walchner_1969_2]: https://doi.org/10.2514/3.5098
[research_walker_2015]: https://doi.org/10.31356/avi-fac0003
[research_walker_2016]: https://doi.org/10.31356/avi-fac0002
[research_walker_2024]: https://doi.org/10.58940/2374-6793.1884
[research_wall_meyer_2020]: https://doi.org/10.2514/1.b37419
[research_wallace_1952]: https://doi.org/10.21236/ad0043099
[research_wallace_vance_2019]: https://doi.org/10.15394/ijaaa.2019.1421
[research_wallner_sorin_1946]: https://ntrs.nasa.gov/citations/20030063996
[research_walsh_1993]: https://ntrs.nasa.gov/citations/19930013934
[research_walter_2022]: https://doi.org/10.4050/jahs.67.042010
[research_walz_1976]: https://doi.org/10.21236/ada024663
[research_walz_1978]: https://doi.org/10.21236/ada059795
[research_wan_2019]: https://doi.org/10.3390/app9040798
[research_wang_1980]: https://doi.org/10.21236/ada080073
[research_wang_1981]: https://doi.org/10.2514/3.57493
[research_wang_2015]: https://doi.org/10.1016/j.cja.2014.12.026
[research_wang_2015_2]: https://doi.org/10.3397/1/376325
[research_wang_2019]: https://doi.org/10.1063/1.5087963
[research_wang_2019_2]: https://doi.org/10.1016/j.cja.2019.07.022
[research_wang_2019_4]: https://doi.org/10.2514/1.g003980
[research_wang_2020_3]: https://doi.org/10.1109/jsen.2020.2994589
[research_wang_2022]: https://doi.org/10.3390/aerospace9080433
[research_wang_2022_2]: https://doi.org/10.1007/s42405-022-00442-x
[research_wang_2022_3]: https://doi.org/10.2514/1.j060909
[research_wang_2022_4]: https://doi.org/10.3390/aerospace9110689
[research_wang_2023]: https://doi.org/10.1016/j.cja.2022.05.008
[research_wang_2023_3]: https://doi.org/10.1109/jsen.2023.3240888
[research_wang_2024]: https://doi.org/10.3390/aerospace11010070
[research_wang_2024_5]: https://doi.org/10.1016/j.jsv.2024.118591
[research_wang_2024_6]: https://doi.org/10.3397/in_2024_2841
[research_wang_2024_7]: https://doi.org/10.61935/acetr.4.1.2024.p120
[research_wang_2025]: https://doi.org/10.1016/j.ast.2025.110533
[research_wang_2025_2]: https://doi.org/10.1109/taes.2025.3616272
[research_wang_2026]: https://doi.org/10.70121/001c.155068
[research_wang_2026_2]: https://doi.org/10.1016/j.ast.2025.111272
[research_wang_2026_3]: https://doi.org/10.1088/1742-6596/3207/1/012114
[research_wang_antesberger_2024]: https://doi.org/10.3397/in_2024_3276
[research_wang_chen_2024]: https://doi.org/10.3390/aerospace11090711
[research_wang_crocker_1983]: https://doi.org/10.1121/1.389873
[research_wang_li_2019]: https://doi.org/10.1121/1.5136785
[research_wang_qin_2013]: https://doi.org/10.1016/j.proeng.2013.12.034
[research_wang_qin_2022]: https://doi.org/10.1016/j.apacoust.2022.109000
[research_wang_qin_2024]: https://doi.org/10.3397/in_2024_2969
[research_wang_wu_2021]: https://doi.org/10.1016/j.jfluidstructs.2021.103286
[research_wang_zhang_2020]: https://doi.org/10.1088/1757-899x/751/1/012028
[research_wang_zhong_2025]: https://doi.org/10.3397/in_2025_1075003
[research_wanglomklang_2025]: https://doi.org/10.1080/0305215x.2025.2563669
[research_wanner_1973]: https://doi.org/10.1017/s0001924000042032
[research_ward_1968]: https://doi.org/10.2514/3.43928
[research_ward_1988]: https://doi.org/10.2514/6.1988-2116
[research_ward_bennett_1974]: https://doi.org/10.2514/6.1974-951
[research_warner_1993]: https://doi.org/10.21236/ada267019
[research_washington_2017]: https://doi.org/10.1016/j.paerosci.2017.10.001
[research_watson_1982]: https://ntrs.nasa.gov/citations/19820017338
[research_watson_2020]: https://doi.org/10.2514/1.c035733
[research_watter_1930]: https://doi.org/10.1115/1.4057273
[research_watts_1976]: https://doi.org/10.21236/ada030344
[research_webb_willer_1952]: https://doi.org/10.21236/ada075990
[research_webster_1971]: https://doi.org/10.21236/ad0729067
[research_wei_2017]: https://doi.org/10.2514/1.c034079
[research_wei_2020]: https://doi.org/10.1109/access.2020.2964728
[research_wei_2022]: https://doi.org/10.1108/aeat-12-2021-0364
[research_wei_2022_2]: https://doi.org/10.3390/s22207933
[research_wei_renliang_2015]: https://doi.org/10.2514/1.c032774
[research_weick_harris_1933]: https://ntrs.nasa.gov/citations/19930091498
[research_weick_harris_1934]: https://ntrs.nasa.gov/citations/19930091518
[research_weick_jones_1937]: https://ntrs.nasa.gov/citations/19930091680
[research_weick_jones_1976]: https://ntrs.nasa.gov/citations/19760011978
[research_weick_noyes_1933]: https://ntrs.nasa.gov/citations/19930081241
[research_weick_noyes_1933_2]: https://ntrs.nasa.gov/citations/19930091496
[research_weick_shortal_1933]: https://ntrs.nasa.gov/citations/19930091512
[research_weick_shortal_1935]: https://ntrs.nasa.gov/citations/19930081340
[research_weick_wenzinger_1935]: https://ntrs.nasa.gov/citations/19930091572
[research_weiser_2023]: https://doi.org/10.2514/1.g007326
[research_weiser_ossmann_2022]: https://doi.org/10.1016/j.ifacol.2022.07.213
[research_weiss_eterno_1986]: https://doi.org/10.23919/acc.1986.4789172
[research_weisshaar_1977]: https://doi.org/10.2514/3.44579
[research_weisshaar_1990]: https://doi.org/10.2514/3.25276
[research_welch_1995]: https://doi.org/10.1017/s0001924000049630
[research_welch_2026]: https://doi.org/10.4103/nah.nah_207_25
[research_wells_1977]: https://doi.org/10.2514/3.58923
[research_wells_1982]: https://doi.org/10.2514/3.57377
[research_wen_2023]: https://doi.org/10.3390/aerospace10121001
[research_wendt_1947]: https://doi.org/10.2514/8.1329
[research_weng_2021]: https://doi.org/10.3390/wevj12040199
[research_wenzinger_bamber_1938]: https://ntrs.nasa.gov/citations/19930081450
[research_wenzinger_rogallo_1941]: https://ntrs.nasa.gov/citations/19930091784
[research_weslet_sutherland_1987]: https://doi.org/10.1121/1.2024592
[research_wesolek_2007]: https://doi.org/10.21236/ada465655
[research_west_1994]: https://doi.org/10.21236/ada288727
[research_west_2015]: https://ntrs.nasa.gov/citations/20150006845
[research_westin_2023]: https://doi.org/10.3390/axioms12090826
[research_weston_2024]: https://doi.org/10.3397/nc_2024_0167
[research_wheeler_2021]: https://doi.org/10.1109/jproc.2021.3073291
[research_whitaker_1975]: https://ntrs.nasa.gov/citations/19750010151
[research_whitaker_1977]: https://ntrs.nasa.gov/citations/19780011159
[research_whitbeck_hofmann_1978]: https://doi.org/10.21236/ada067177
[research_whitcomb_1940]: https://ntrs.nasa.gov/citations/20030063138
[research_white_1963]: https://doi.org/10.21236/ad0296103
[research_white_1971]: https://doi.org/10.2514/3.59169
[research_white_2021]: https://doi.org/10.1007/s13272-021-00542-6
[research_white_2025]: https://doi.org/10.1121/10.0037888
[research_whiting_1996]: https://ntrs.nasa.gov/citations/19960012279
[research_whitmore_merrill_2012]: https://doi.org/10.2514/1.c031645
[research_whittingham_swan_1960]: https://doi.org/10.1071/es60025
[research_whittley_garland_1961]: https://doi.org/10.21236/ad0271500
[research_whoric_1973]: https://doi.org/10.21236/ad0914456
[research_widger_1963]: https://doi.org/10.1175/1520-0477-44.9.549
[research_widnall_wolf_1980]: https://doi.org/10.2514/3.44681
[research_wiggi_1949]: https://doi.org/10.1080/00431672.1949.9930056
[research_wilby_1982]: https://doi.org/10.4271/820961
[research_wilby_rennison_1980]: https://doi.org/10.2514/6.1980-999
[research_wilby_wilby_1989]: https://doi.org/10.2514/3.45721
[research_wild_1966]: https://doi.org/10.1119/1.2351010
[research_wiley_1954]: https://ntrs.nasa.gov/citations/19930088380
[research_wiley_taylor_1954]: https://ntrs.nasa.gov/citations/19930088283
[research_wilhelm_schafranek_1986]: https://doi.org/10.2514/3.45377
[research_wilk_2024]: https://doi.org/10.58445/rars.1626
[research_wilkerson_1975]: https://doi.org/10.3397/1.2831989
[research_wilkinson_1954]: https://doi.org/10.1017/s0368393100100276
[research_willebeeklemair_rhinehart_2023]: https://doi.org/10.4050/sm_2023_hq-1196
[research_william_c_patterson]: https://ntrs.nasa.gov/citations/20230006106
[research_williams_1940]: https://doi.org/10.1017/s0368393100106571
[research_williams_1974]: https://doi.org/10.3397/1.2831973
[research_williams_2002]: https://doi.org/10.21236/ada400135
[research_williams_howe_1970]: https://doi.org/10.21236/ad0877764
[research_willis_daniels_1981]: https://ntrs.nasa.gov/citations/19820007006
[research_willshire_1983]: https://doi.org/10.2514/3.44874
[research_willshire_1990]: https://ntrs.nasa.gov/citations/19910007369
[research_willshire_hilton_1979]: https://doi.org/10.1121/1.2017692
[research_wilmott_1986]: https://doi.org/10.1017/s0001924000015347
[research_wilson_1993]: https://doi.org/10.21236/ada273685
[research_wilson_2016]: https://doi.org/10.1121/1.4949797
[research_wilson_2021]: https://doi.org/10.1139/juvs-2020-0021
[research_wilson_2022]: https://doi.org/10.1121/10.0010967
[research_wilson_2024]: https://doi.org/10.1121/at.2024.20.4.78
[research_wilson_2025]: https://doi.org/10.3397/nc_2025_0151
[research_wilson_committee_1963]: https://doi.org/10.1108/eb033763
[research_wind_tunnel_1974]: https://doi.org/10.1177/002029407400700205
[research_wing_design_2021]: https://doi.org/10.1017/9781139094672.011
[research_wings_and_1999]: https://doi.org/10.1142/9781848160897_0002
[research_winn_kishi_1972]: https://doi.org/10.21236/ad0753343
[research_winslow_2018]: https://doi.org/10.2514/1.c034483
[research_winter_2023]: https://doi.org/10.3397/in_2022_0318
[research_winther_1981]: https://doi.org/10.2514/3.56103
[research_woan_gregorek_1978]: https://ntrs.nasa.gov/citations/19780057923
[research_wokoun_1962]: https://doi.org/10.21236/ad0283554
[research_wolek_2016]: https://doi.org/10.2514/1.g001345
[research_wolf_raspet_1986]: https://doi.org/10.1121/1.2024031
[research_wolowicz_yancey_1973]: https://ntrs.nasa.gov/citations/19730023226
[research_woo_2020]: https://doi.org/10.1007/s10846-020-01152-w
[research_wood_2019]: https://doi.org/10.2514/1.c035416
[research_woods_1972]: https://doi.org/10.1016/0022-460x(72)90616-5
[research_woodward_1987]: https://doi.org/10.2514/6.1987-2657
[research_woodward_1987_b]: https://doi.org/10.2514/6.1987-526
[research_woodward_loeffler_1991]: https://ntrs.nasa.gov/citations/19910009732
[research_wooley_childs_1954]: https://doi.org/10.21236/ad0037710
[research_woolf_2012]: https://doi.org/10.21236/ada583117
[research_woolworth_2022]: https://doi.org/10.1121/10.0010542
[research_woolworth_2023]: https://doi.org/10.1121/10.0019006
[research_worobel_peracchio_1968]: https://doi.org/10.21236/ad0828077
[research_wrestler_clifton_g_1965]: https://doi.org/10.21236/ad0622404
[research_wright_1966]: https://doi.org/10.21236/ad0645537
[research_wright_lee_1984]: https://doi.org/10.2514/6.1984-251
[research_wu_2010]: https://doi.org/10.3397/1.3502423
[research_wu_2017_2]: https://doi.org/10.2514/1.c034356
[research_wu_2018]: https://doi.org/10.1016/j.ast.2018.07.037
[research_wu_2019]: https://doi.org/10.2514/1.g003704
[research_wu_2019_2]: https://doi.org/10.1109/taes.2018.2876738
[research_wu_2020]: https://doi.org/10.1088/1757-899x/790/1/012162
[research_wu_2020_2]: https://doi.org/10.1109/access.2020.2972570
[research_wu_2020_3]: https://doi.org/10.3390/en13061379
[research_wu_2021_2]: https://doi.org/10.3397/in-2021-3258
[research_wu_2023]: https://doi.org/10.3390/aerospace10050387
[research_wu_2023_2]: https://doi.org/10.3397/in_2023_0595
[research_wu_moracamino_2012]: https://doi.org/10.2514/6.2012-4442
[research_wu_redonnet_2021]: https://doi.org/10.3390/aerospace8090264
[research_wu_talmadge_1961]: https://doi.org/10.21236/ad0266566
[research_xiang_jiang_2015]: https://doi.org/10.1121/1.4933545
[research_xiao_2024]: https://doi.org/10.3390/aerospace11050408
[research_xie_2017]: https://doi.org/10.1155/2017/2564314
[research_xie_2023]: https://doi.org/10.2514/1.g006872
[research_xie_2023_2]: https://doi.org/10.2514/1.c037239
[research_xie_2024]: https://doi.org/10.1515/noise-2024-0005
[research_xie_haberland_1999]: https://doi.org/10.1016/s1369-8869(99)00012-9
[research_xieyuan_1985]: https://doi.org/10.2514/3.45086
[research_xiong_2025]: https://doi.org/10.1002/asjc.3568
[research_xiong_2026]: https://doi.org/10.1016/j.ast.2026.112223
[research_xu_2015]: https://doi.org/10.1016/j.ijhydene.2015.09.028
[research_xu_2020]: https://doi.org/10.1109/access.2020.3041855
[research_xu_2025]: https://doi.org/10.1016/j.isatra.2025.05.009
[research_xu_wang_2016]: https://doi.org/10.1371/journal.pone.0167168
[research_xue_2023]: https://doi.org/10.3390/aerospace10030254
[research_xue_haibin_2017]: https://doi.org/10.1108/aeat-01-2015-0007
[research_yager_1983]: https://ntrs.nasa.gov/citations/19830019708
[research_yamada_2023]: https://doi.org/10.3397/in_2022_0475
[research_yamamoto_2023]: https://doi.org/10.3397/in_2023_0627
[research_yamashita_matsui_1978]: https://doi.org/10.1121/1.2004016
[research_yamin_giyats_2022]: https://doi.org/10.56741/jnest.v1i02.143
[research_yan_2017]: https://doi.org/10.11648/j.acis.20170502.12
[research_yan_2024]: https://doi.org/10.1016/j.cja.2023.09.016
[research_yan_tian_2024]: https://doi.org/10.3390/aerospace11050332
[research_yancey_1964]: https://ntrs.nasa.gov/citations/19650001037
[research_yang]: https://doi.org/10.14711/thesis-hdl171519
[research_yang_2016]: https://doi.org/10.1177/0954410016629497
[research_yang_2017]: https://doi.org/10.1134/s1063771017060033
[research_yang_2019_2]: https://doi.org/10.1016/j.ast.2019.105493
[research_yang_2023]: https://doi.org/10.1016/j.ast.2023.108142
[research_yang_gao_2020]: https://doi.org/10.1109/tac.2019.2918122
[research_yang_li_2022]: https://doi.org/10.3390/aerospace9090515
[research_yang_meinke_2026]: https://doi.org/10.2514/1.j066232
[research_yang_zhang]: https://ntrs.nasa.gov/citations/20210017005
[research_yasue_2020]: https://doi.org/10.2514/1.c035564
[research_yates_1949]: https://doi.org/10.1002/j.1477-8696.1949.tb00994.x
[research_yates_1974]: https://doi.org/10.2514/3.60355
[research_yazdi_1991]: https://doi.org/10.2514/6.1991-3125
[research_yazgan_kucuk_yilmaz_2018]: https://doi.org/10.1108/aeat-03-2017-0096
[research_ye_2015]: https://doi.org/10.1155/2015/254975
[research_yeager_1997]: https://doi.org/10.21236/ada406400
[research_yegorov_1945]: https://ntrs.nasa.gov/citations/20050028476
[research_yeh_plotkin_1986]: https://doi.org/10.2514/3.9458
[research_yeo_2015]: https://doi.org/10.2514/1.c032682
[research_yeong_chiles_2009]: https://doi.org/10.2514/6.2009-4207
[research_yeow_1984]: https://doi.org/10.1016/0022-460x(84)90265-7
[research_yi_2025]: https://doi.org/10.1063/5.0299020
[research_yih_1952]: https://doi.org/10.21236/ad0009799
[research_yildiz_2019]: https://doi.org/10.2514/1.g004180
[research_yildiz_2022]: https://doi.org/10.1108/aeat-08-2021-0238
[research_yin_2019]: https://doi.org/10.2514/1.g004193
[research_yin_2020]: https://doi.org/10.2514/1.c035829
[research_yin_stuermer_2013]: https://doi.org/10.1007/s13272-013-0089-5
[research_yip_1992]: https://ntrs.nasa.gov/citations/19920073534
[research_yokota_2023]: https://doi.org/10.3397/in_2023_0967
[research_yokota_2025]: https://doi.org/10.3397/in_2025_1074214
[research_yongtao_zhi_2014]: https://doi.org/10.1109/ccdc.2014.6852791
[research_yoon_2019]: https://doi.org/10.1007/s12206-019-0309-y
[research_yoshikawa_1992]: https://doi.org/10.1121/1.404020
[research_yost_1976]: https://ntrs.nasa.gov/citations/19770012115
[research_you_2020]: https://doi.org/10.1088/1742-6596/1678/1/012032
[research_you_2020_2]: https://doi.org/10.2514/1.j058002
[research_yu_2011]: https://doi.org/10.21236/ada563588
[research_yu_2018]: https://doi.org/10.4236/mme.2018.84017
[research_yu_2020]: https://doi.org/10.1007/s42405-020-00266-7
[research_yu_2023]: https://doi.org/10.1002/rnc.6570
[research_yu_2026]: https://doi.org/10.62051/ijmee.v8n2.04
[research_yu_ansell_2023]: https://doi.org/10.2514/1.c036857
[research_yu_huang_2018]: https://doi.org/10.1109/access.2018.2801260
[research_yuan_2018]: https://doi.org/10.1108/aeat-01-2018-0073
[research_yuan_2019]: https://doi.org/10.2514/1.c035190
[research_yuan_2020]: https://doi.org/10.2514/1.c035811
[research_yuan_2024]: https://doi.org/10.1016/j.ast.2024.109305
[research_yuan_2026]: https://doi.org/10.54254/2753-8818/2026.dl34744
[research_yue_2025]: https://doi.org/10.3390/drones9010063
[research_yuen_2026]: https://doi.org/10.58445/rars.3632
[research_yuma_proving_ground_az_2013]: https://doi.org/10.21236/ada568947
[research_yuma_test_center_yuma_proving_ground_az_2008]: https://doi.org/10.21236/ada503063
[research_yunus_2023]: https://doi.org/10.1016/j.ast.2023.108410
[research_yurttav_2025]: https://doi.org/10.1017/aer.2024.84
[research_yusuf_2022]: https://doi.org/10.3390/s22031068
[research_zaal_2015]: https://doi.org/10.2514/1.c033115
[research_zabinsky_laszewski_1956]: https://doi.org/10.21236/ad0102024
[research_zafirov_2020]: https://doi.org/10.3897/arb.v32.e09
[research_zajdel_2022]: https://doi.org/10.3390/aerospace9020111
[research_zajdel_2024]: https://doi.org/10.1108/aeat-03-2024-0086
[research_zajdel_2024_2]: https://doi.org/10.1108/aeat-04-2023-0115
[research_zaman_2024]: https://doi.org/10.1016/j.jsv.2024.118604
[research_zaporozhets_2022]: https://doi.org/10.23890/ijast.vm03is02.0204
[research_zaporozhets_jagniatinskis_2021]: https://doi.org/10.3397/in-2021-2352
[research_zelenka_1995]: https://ntrs.nasa.gov/citations/19950026069
[research_zeller_jr_2001]: https://doi.org/10.21236/ada398689
[research_zellmann_2018]: https://doi.org/10.2514/1.c034275
[research_zhai_2024]: https://doi.org/10.1016/j.isatra.2024.08.007
[research_zhang_2015_2]: https://doi.org/10.1016/j.ast.2015.02.024
[research_zhang_2018_2]: https://doi.org/10.1049/iet-epa.2017.0639
[research_zhang_2023_3]: https://doi.org/10.1016/j.cja.2022.07.024
[research_zhang_2023_4]: https://doi.org/10.1088/1742-6596/2569/1/012026
[research_zhang_2023_5]: https://doi.org/10.3397/in_2023_0555
[research_zhang_2023_7]: https://doi.org/10.3390/aerospace10050439
[research_zhang_2024]: https://doi.org/10.1088/1742-6596/2820/1/012004
[research_zhang_2025]: https://doi.org/10.1038/s41598-025-12929-0
[research_zhang_2025_2]: https://doi.org/10.1016/j.apacoust.2025.110947
[research_zhang_2025_3]: https://doi.org/10.1088/1742-6596/3078/1/012007
[research_zhang_2026_10]: https://doi.org/10.54097/8b2agg53
[research_zhang_2026_4]: https://doi.org/10.1007/s42401-026-00483-0
[research_zhang_2026_8]: https://doi.org/10.54254/2755-2721/2026.mh31452
[research_zhang_liu_2026]: https://doi.org/10.1016/j.simpat.2026.103301
[research_zhang_ma_2022]: https://doi.org/10.3390/app12136765
[research_zhang_millane_2011]: https://doi.org/10.2316/p.2011.759-065
[research_zhang_xia_2017]: https://doi.org/10.2514/1.c034388
[research_zhang_yu_2013]: https://doi.org/10.1155/2013/714168
[research_zhang_zhao_2023]: https://doi.org/10.3390/aerospace10120981
[research_zhang_zhou_2024]: https://doi.org/10.1088/1742-6596/2820/1/012041
[research_zhao_2023_2]: https://doi.org/10.2514/1.c037208
[research_zhao_2025]: https://doi.org/10.54097/dg56wy94
[research_zhao_gao_2019]: https://doi.org/10.1108/ec-05-2018-0215
[research_zhao_jim_zhu_2017]: https://doi.org/10.2514/1.g001835
[research_zhen_2019]: https://doi.org/10.1109/access.2019.2929870
[research_zheng_2018]: https://doi.org/10.1016/j.cja.2018.05.006
[research_zheng_2019]: https://doi.org/10.1121/1.5101517
[research_zheng_2021]: https://doi.org/10.1177/1475472x20984092
[research_zheng_2023]: https://doi.org/10.2514/1.j062602
[research_zheng_2026]: https://doi.org/10.1016/j.ast.2026.113066
[research_zhi_2025]: https://doi.org/10.1016/j.cja.2025.103481
[research_zhong_2019]: https://doi.org/10.1177/1475472x19871525
[research_zhong_2023]: https://doi.org/10.1016/j.apacoust.2023.109298
[research_zhou_2020_2]: https://doi.org/10.1007/s42241-020-0006-4
[research_zhou_2022]: https://doi.org/10.26855/ea.2022.12.003
[research_zhou_wang_2026]: https://doi.org/10.2514/1.c038092
[research_zhu_2016]: https://doi.org/10.1108/aeat-11-2013-0199
[research_zhu_2023]: https://doi.org/10.1007/s11071-023-08442-6
[research_zhu_2023_2]: https://doi.org/10.3390/aerospace10050442
[research_zhu_2025]: https://doi.org/10.54254/2755-2721/2025.25239
[research_zhu_duan_2015]: https://doi.org/10.1108/aeat-06-2013-0112
[research_ziakos_2025]: https://doi.org/10.1007/s13272-025-00851-0
[research_zikmund_2019]: https://doi.org/10.1051/matecconf/201930406005
[research_zohar_er_el_1988]: https://doi.org/10.2514/3.45578
[research_zola_fishbach_1978]: https://ntrs.nasa.gov/citations/19780009098
[research_zong_2021]: https://doi.org/10.1088/1742-6596/1786/1/012024
[research_zoric_2024]: https://doi.org/10.25144/22753
[research_zorumski_1977]: https://ntrs.nasa.gov/citations/19780051748
[research_zorumski_willshire_1989]: https://doi.org/10.2514/3.10141
[research_zou_2021]: https://doi.org/10.1109/access.2021.3053302
[research_zu_2017]: https://doi.org/10.3390/s17030514
[research_zugaj_2017]: https://doi.org/10.2478/tar-2017-0017
[research_zuhri_2025]: https://doi.org/10.55981/ijoa.2025.9106
