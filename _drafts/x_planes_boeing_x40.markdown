---
layout: post
mathjax: true
comments: true
title: "X-Planes: Boeing X-40"
date: 2025-11-15 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 41
---
<!-- A337 -->
<script>console.log("A337");</script>

The [X-40][ref_x40] is described almost everywhere as a subscale model of the
[X-37][related_post_a334_boeing_x37], and **by the test that matters it was not a scale model at all.**
It weighed about half what dynamic similarity required, so its trajectory could not transfer to the
full-scale vehicle even in principle. **What transferred was the software.**
This is the forty-first article in the [X-Planes series][related_post_a297_framing], following the [X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], the [X-4][related_post_a301_northrop_x4], the [X-5][related_post_a302_bell_x5], the [X-6][related_post_a303_convair_x6], the [X-7][related_post_a304_lockheed_x7], the [X-8][related_post_a305_aerojet_x8], the [X-9][related_post_a306_bell_x9], the [X-10][related_post_a307_north_american_x10], the [X-11][related_post_a308_convair_x11], the [X-12][related_post_a309_convair_x12], the [X-13][related_post_a310_ryan_x13], the [X-14][related_post_a311_bell_x14], the [X-15][related_post_a312_north_american_x15], the [X-16][related_post_a313_bell_x16], the [X-17][related_post_a314_lockheed_x17], the [X-18][related_post_a315_hiller_x18], the [X-19][related_post_a316_curtiss_wright_x19], the [X-20][related_post_a317_boeing_x20], the [X-21][related_post_a318_northrop_x21], the [X-22][related_post_a319_bell_x22], the [X-23][related_post_a320_martin_marietta_x23], the [X-24][related_post_a321_martin_marietta_x24], the [X-25][related_post_a322_bensen_x25], the [X-26][related_post_a323_schweizer_x26], the [X-27][related_post_a324_lockheed_x27], the [X-28][related_post_a325_osprey_x28], the [X-29][related_post_a326_grumman_x29], the [X-30][related_post_a327_rockwell_x30], the [X-31][related_post_a328_rockwell_mbb_x31], the [X-32][related_post_a329_boeing_x32], the [X-33][related_post_a330_lockheed_martin_x33], the [X-34][related_post_a331_orbital_sciences_x34], the [X-35][related_post_a332_lockheed_martin_x35], the [X-36][related_post_a333_mcdonnell_douglas_x36], the [X-37][related_post_a334_boeing_x37], the [X-38][related_post_a335_scaled_composites_x38], and the [X-39][related_post_a336_x39_reserved_never_assigned].

**The X-40A is the first vehicle in the series built to test a program rather than
an aerodynamic idea.** The [X-1][related_post_a298_bell_x1] measured transonic drag rise. The
[X-15][related_post_a312_north_american_x15] flew hypersonically and survived the heating. The X-40A was
dropped from a helicopter eight times so that an autopilot could practise landing \[[X-40A Space Maneuvering Vehicle][ref_nasa_x40]\], and **the question it
answers is whether that is worth doing.**

The article immediately before this one concerned a designation that was never assigned. **This one
concerns a designation that was assigned twice**, first to an operational concept and then to the test
article that outlived it \[[Boeing X-37 and X-40][ref_x37_x40]\], and the second assignment explains why the public record disagrees with itself
about how big the vehicle was.

## The Research Question

**The binding unknown was not aerodynamic and it was not thermal. It was whether an unmanned vehicle could
be trusted to land itself.**

The [Space Maneuver Vehicle][ref_smv_global] concept of the middle 1990s asked for a small reusable
spacecraft that would be launched by an expendable booster or by the Shuttle, remain on orbit for up to a
year, and then **return under fully automatic control to a horizontal landing on a designated runway**
\[[Boeing X-37 and X-40][ref_x37_x40]\]. Every part of that is hard. Only the last part could be rehearsed
cheaply, because the last part happens inside the atmosphere at speeds an ordinary aircraft reaches.

**The precedent for an orbital vehicle landing itself belonged to somebody else.** The Soviet [Buran][ref_buran] flew an uncrewed orbital mission on 15 November 1988 and landed itself on a runway at Baikonur, the first spaceplane to fly uncrewed and land in fully automatic mode \[[Buran][ref_buran]\]. On the American [Space Shuttle][ref_shuttle] a crew was aboard and took over manual control once the orbiter was subsonic \[[Space Shuttle][ref_shuttle]\]. **So the United States entered the
Space Maneuver Vehicle programme with no domestic flight experience of the thing the vehicle was for.**

**The design work had nonetheless been done, and thoroughly.** Terminal control and automatic landing of
unpowered shuttle vehicles was studied from 1970 \[[Osder 1970][research_osder_1970]\], the
automatic flare and decrab problem was worked in detail \[[Cockayne and Rusnak 1971][research_cockayne_1971]\],
a full navigation, guidance and control concept was flight-tested \[[Edwards et al 1975][research_edwards_1975]\],
and the resulting shuttle automatic landing system was documented
\[[Tsikalas and Dyer 1982][research_tsikalas_1982_b]\]. **What was missing was not theory but a vehicle willing to land
itself**, and the X-40A was cheap enough to be that vehicle.

**The precedent for the method is also American and also well documented.** The Shuttle Orbiter Approach
and Landing Test programme of 1977 carried an orbiter aloft on a carrier aircraft and released it to glide
to a runway \[[Fullerton 1975][research_fullerton_1975]\] \[[Oglesby 1975][research_oglesby_1975]\], and its
final evaluation report \[[Approach and Landing Test final evaluation 1978][research_alt_final_1978]\] and
subsequent analyses \[[Ashkenas et al 1982][research_ashkenas_1982]\] are the model for what a
drop-and-glide campaign is expected to produce. **The X-40A ran the same play at 2,600 pounds and without
a crew** \[[Boeing and the Air Force flight test the Space Maneuver Vehicle][ref_boeing_1998]\]. For all
five free flights the orbiter was ballasted to approximately 150,000 pounds
\[[Approach and Landing Test final evaluation 1978][research_alt_final_1978]\], so for vehicle weight $W$
the weight ratio is

$$\frac{W_{\text{X-40A}}}{W_{\text{orbiter}}} = \frac{2{,}600}{150{,}000} = 0.0173 < \frac{1}{50}$$

**and the X-40A weighed under a fiftieth of the vehicle whose method it borrowed.**

**The keystone question is therefore one of transfer, the same question this series asked of a
proven bound and of a wind tunnel.** If a smaller vehicle is dropped from a helicopter and lands itself,
what has been learned about a larger vehicle returning from orbit?

The answer depends entirely on what similarity holds between the two, and **similarity for a free-flight
model is a stronger requirement than geometric resemblance.** The sizing section derives what it demands
and then measures the X-40A against it. **The vehicle fails the test on mass by a factor of two**, which
sounds like a criticism and is instead the article's central observation, because it explains what the
programme bought.

## Programme Origin

**The vehicle was ordered before the designation existed and the designation was reassigned underneath
it** \[[Boeing X-37 and X-40][ref_x37_x40]\].

In October 1996 Boeing received a contract from the Air Force Research Laboratory's Military Space Plane
Technology office to build a technology demonstrator and test vehicle for the Space Maneuver Vehicle.
The first article under that programme was the
**Integrated Technology Test Bed**, an unpowered vehicle at about ninety percent of the size of the
operational concept \[[Boeing X-37 and X-40][ref_x37_x40]\].

**The X-40A designation was allocated in 1997 to the full Space Maneuver Vehicle and was soon reassigned
to the test bed instead**. The operational vehicle, which would have been the X-40B, is not recorded as built,
and its programme is presumed absorbed by the X-37A \[[Boeing X-37 and X-40][ref_x37_x40]\].
**The number therefore ended up on the only article the programme produced.** The designation
immediately preceding it in this series met a different fate, since
[a number was reserved and never assigned at all][related_post_a336_x39_reserved_never_assigned].

**Boeing built it at Phantom Works in Seal Beach, California, and the cost is the most striking figure in
the programme** \[[Boeing X-40A][ref_nmusaf_x40]\]. Fabrication and construction came to approximately one million dollars
\[[X-40 Space Maneuver Vehicle][ref_smv_global]\]. **That is not a research aircraft budget**, for a vehicle that carried a full autonomous guidance, navigation and
control system and landed itself eight times.

**The sponsoring arrangement spanned two laboratories and two states.** The Air Force Research Laboratory
at Kirtland Air Force Base in New Mexico led, with the Air Vehicles Directorate at Wright-Patterson Air
Force Base in Ohio collaborating \[[Boeing and the Air Force flight test the Space Maneuver Vehicle][ref_boeing_1998]\].
The programme manager at Boeing Phantom Works, John Fuller, described the first flight's purpose in one
sentence, being **to validate low-speed handling qualities and demonstrate autonomous approach and
landing capability** \[[Boeing and the Air Force flight test the Space Maneuver Vehicle][ref_boeing_1998]\].

**The operational concept it served explains the vehicle's proportions.** The
Space Maneuver Vehicle was to turn around in seventy-two hours or less between missions, remain on
station for up to a year, and carry satellite deployment, surveillance and logistics payloads with
aircraft-like operability \[[Boeing and the Air Force flight test the Space Maneuver Vehicle][ref_boeing_1998]\].
**A vehicle designed for aircraft-like turnaround is designed around its ground handling**, and a runway
landing is the ground handling.

## Sizing From First Principles

### What Similarity a Free-Flight Model Must Hold

**A scale model that flies is governed by two dimensionless numbers and it cannot match both.** The
practice has a long institutional history and a canonical account of it, which records the role of
dynamically scaled free-flight models across decades of aerospace programmes and states the scaling
requirements this section derives \[[Chambers 2010][research_chambers_2010]\].

Let $L$ denote a characteristic length of the vehicle, $V$ its speed, $g$ the acceleration due to gravity,
$\rho$ the air density and $\mu$ the dynamic viscosity of air. The Froude number compares inertial force
to gravitational force and governs any motion in which weight and trajectory curvature both matter, which
is every part of an approach and landing.

$$\mathrm{Fr} = \frac{V^{2}}{gL}$$

The Reynolds number compares inertial force to viscous force and governs the behaviour of the boundary
layer, and therefore the lift and drag coefficients the vehicle achieves.

$$\mathrm{Re} = \frac{\rho V L}{\mu}$$

Let $\lambda$ be the geometric scale ratio of model to full-scale vehicle. **Similarity requires
that the two vehicles share a value of the parameter**, and for the Froude number the requirement reads

$$\frac{V_{m}^{2}}{g L_{m}} = \frac{V_{f}^{2}}{g L_{f}}$$

which fixes the speed ratio, because $g$ is the same for both and $V^{2}$ must therefore scale as $L$.

$$\frac{V_{m}}{V_{f}} = \sqrt{\lambda}$$

Time follows immediately, since a length divided by a speed is a time, and this relation makes
a subscale free-flight test interpretable at all.

$$\frac{t_{m}}{t_{f}} = \sqrt{\lambda}$$

**Angular rates therefore go up rather than down**, the first result with a consequence for the
flight control system.

$$\frac{\omega_{m}}{\omega_{f}} = \frac{1}{\sqrt{\lambda}}$$

Substituting the Froude-matched speed into the Reynolds number gives the mismatch that cannot be avoided,
since the model flies in the same air as the full-scale vehicle and $\rho$ and $\mu$ therefore cancel.

$$\frac{\mathrm{Re}_{m}}{\mathrm{Re}_{f}} = \frac{V_{m} L_{m}}{V_{f} L_{f}} = \sqrt{\lambda} \cdot \lambda$$

$$\frac{\mathrm{Re}_{m}}{\mathrm{Re}_{f}} = \lambda^{3/2}$$

**The Mach number takes care of itself here, and the reason matters.** Both vehicles fly the approach
subsonically, so compressibility is a small correction for each and the Froude-matched speed reduction
moves the model further from the transonic regime rather than toward it.

$$\frac{\mathrm{Ma}_{m}}{\mathrm{Ma}_{f}} = \sqrt{\lambda}$$

**The dynamic pressure scales linearly**, and it governs the aerodynamic loads and,
through them, the structural design case.

$$\frac{\bar{q}_{m}}{\bar{q}_{f}} = \frac{\rho V_{m}^{2}}{\rho V_{f}^{2}} = \lambda$$

**And the mass condition is usually forgotten.** Froude similarity requires the model to
have the same relative density as the vehicle, so its weight must scale as the cube of the length ratio.

$$\frac{W_{m}}{W_{f}} = \lambda^{3}$$

Equivalently, and more usefully for an aircraft, the wing loading must scale linearly, since weight goes
as $\lambda^{3}$ and reference area as $\lambda^{2}$.

$$\frac{(W/S)_{m}}{(W/S)_{f}} = \lambda$$

**The rotational condition follows from the same requirement and governs the autopilot.**
A moment of inertia is a mass times the square of a length, so under mass similarity it scales as the
fifth power of the length ratio.

$$\frac{I_{m}}{I_{f}} = \frac{m_{m}}{m_{f}} \left(\frac{L_{m}}{L_{f}}\right)^{2} = \lambda^{3} \lambda^{2} = \lambda^{5}$$

**The standard single parameter that expresses all of this at once is the relative density**, which
compares the vehicle's mass to the mass of the air in a volume defined by its dimensions. Let $m$ be
the mass, $S$ the reference area and $l$ a reference length.

$$\mu = \frac{m}{\rho S l}$$

**Dynamic similarity of a free-flight model holds when the relative densities match**, and the
free-flight testing literature usually writes the requirement in this form
\[[Chambers 2010][research_chambers_2010]\].

$$\mu_{m} = \mu_{f}$$

### The Scale Ratio Is Disputed and the Dispute Is Resolvable

**Four different scale figures circulate for the same vehicle and they are not all about the same
comparison.** Boeing's press release calls the X-40A a ninety percent scale vehicle
\[[Boeing and the Air Force flight test the Space Maneuver Vehicle][ref_boeing_1998]\]. The space agency
calls it an eighty percent subscale version of the X-37 \[[X-40A Space Maneuvering Vehicle][ref_nasa_x40]\].
A contemporaneous report of the second free flight calls it eighty-five percent
\[[X-40A second free flight successful][ref_sciencedaily_x40]\]. A reference encyclopaedia hedges at eighty
to ninety percent \[[Boeing X-40][ref_x40]\].

**The published dimensions settle it.** The X-40A is 22 feet long with a 12 foot span
\[[Boeing and the Air Force flight test the Space Maneuver Vehicle][ref_boeing_1998]\], and the X-37B is
29 feet 3 inches long with a span of 14 feet 11 inches \[[Boeing X-37][ref_x37]\].

$$\lambda_{\text{length}} = \frac{6.71}{8.92} = 0.752$$

$$\lambda_{\text{span}} = \frac{3.66}{4.55} = 0.804$$

**Taking the mean of the two gives $\lambda = 0.778$**, and the check on that value is the reciprocal,
since the sources state the scale-up in the other direction.

$$\frac{1}{\lambda} = \frac{1}{0.778} = 1.285$$

against the "about 120 percent" that the sources give for the X-37 relative to the X-40A
\[[Boeing X-37][ref_x37]\]. **The agreement is adequate at eight points and the ninety percent figure is
not**, since it would require a reciprocal of 111 percent.

**The ninety percent figure is correct about a vehicle that was never built under its own designation.** The test bed was ninety
percent of the **Space Maneuver Vehicle**, the operational concept
\[[Boeing X-37 and X-40][ref_x37_x40]\], and the X-37 that everybody now compares it to was a later and
larger vehicle. **A ratio quoted without its denominator has caused a twelve point disagreement in the
literature about the best documented parameter of the aircraft.**

### The Mass Condition Fails by a Factor of Two

**This is the result the article turns on.** At $\lambda = 0.778$, Froude similarity requires a model
weight of

$$W_{m} = W_{f} \lambda^{3} = 11{,}000 \times 0.778^{3} = 5{,}186 \ \text{lb}$$

for the X-37B's published maximum takeoff weight of 11,000 lb \[[Boeing X-37][ref_x37]\], against a published X-40A weight of about **2,600 lb**
\[[Boeing and the Air Force flight test the Space Maneuver Vehicle][ref_boeing_1998]\].
**The vehicle was 50 percent of its dynamically similar mass.**

Read the other way, the mass ratio implies a scale ratio of its own, nowhere near the geometric
one.

$$\lambda_{\text{mass}} = \left(\frac{2{,}600}{11{,}000}\right)^{1/3} = 0.618$$

**A geometric ratio of 0.778 against a mass-implied ratio of 0.618 is not a scale model.** It is a vehicle of
approximately the right shape and substantially the wrong density.

**The wing loading condition fails in the same proportion, and the arithmetic behind that is short.** Taking
the estimated reference area of 100 square feet for the X-40A and scaling it by $\lambda^{2}$ for the
X-37 gives 165 square feet, so the two wing loadings are

$$\left(\frac{W}{S}\right)_{m} = \frac{2{,}600}{100} = 26.0 \ \text{lb/ft}^{2} \qquad \left(\frac{W}{S}\right)_{f} = \frac{11{,}000}{165} = 66.6 \ \text{lb/ft}^{2}$$

$$\frac{(W/S)_{m}}{(W/S)_{f}} = 0.391 \quad \text{against a required} \quad \lambda = 0.778$$

**Since speed goes as the square root of wing loading at a given lift coefficient**, the consequence is a
vehicle flying substantially slower than similarity demands.

$$\frac{V_{m}}{V_{f}} = \sqrt{0.391} = 0.625 \quad \text{against a required} \quad \sqrt{\lambda} = 0.882$$

$$\frac{0.625}{0.882} = 0.708$$

**The model therefore flew at about 71 percent of its dynamically similar speed.**

**The relative density gives the same answer in the parameter the free-flight literature uses.**
With the mass in slugs, the estimated areas above and the vehicle lengths as reference lengths,

$$\mu_{m} = \frac{80.8}{(0.001869)(100)(22.0)} = 19.7 \qquad \mu_{f} = \frac{341.9}{(0.001869)(165)(29.25)} = 37.9$$

$$\frac{\mu_{m}}{\mu_{f}} = 0.519 \quad \text{against a required} \quad 1.000$$

**Two independent formulations land on the same factor of two**, and no internal check on the finding
is stronger, since the wing loading route and the relative density route share only the
published masses.

**The shortfall was not an oversight and could not have been fixed.** The X-40A carried neither propulsion nor a thermal protection system \[[X-40A Space Maneuvering Vehicle][ref_nasa_x40]\], and as an atmospheric test bed it had no use for a payload or for orbital subsystems. **Those absent systems are the mass the
full-scale vehicle would carry**, and ballasting a one million dollar test article up to 5,186 lb, the
weight that the relation $W_{m} = W_{f} \lambda^{3}$ above requires, in order to
preserve a similarity nobody intended to exploit would have been a strange use of the money.

### Reynolds Number Does Less Than Expected

**The usual objection to subscale free flight barely applies here**, because the X-40A was
not very sub. At $\lambda = 0.778$ the Reynolds ratio is

$$\frac{\mathrm{Re}_{m}}{\mathrm{Re}_{f}} = 0.778^{3/2} = 0.686$$

**A boundary layer at 69 percent of full-scale Reynolds number is a mild extrapolation**, far milder than
the one or two orders of magnitude that a conventional dynamically scaled drop model accepts.
**The comparison is available in a single well-documented case.** A contemporaneous programme flew a
22 percent dynamically scaled drop model of the F/A-18E/F \[[Croom et al 2000][research_croom_2000]\],
and at that ratio the same relation gives

$$\frac{\mathrm{Re}_{m}}{\mathrm{Re}_{f}} = 0.22^{3/2} = 0.103$$

or about a tenth of full scale. **The X-40A sat at 69 percent where a conventional drop model sits near 10**, and on that
measure it was barely a subscale article at all.

**The absolute value matters as much as the ratio and sits comfortably high.** Taking the density at 8,000 feet as 0.001869 slug per cubic foot and the dynamic viscosity as $3.58 \times 10^{-7}$ slug per foot second, values that follow from the defining relations of the 1976 standard atmosphere \[[U.S. Standard Atmosphere, 1976][ref_atm76]\], the Reynolds number on the 22 foot length at 428 feet per second is

$$\mathrm{Re} = \frac{(0.001869)(428)(22.0)}{3.58 \times 10^{-7}} = 4.92 \times 10^{7}$$

**A Reynolds number near fifty million is far above any transition-sensitive regime**, so a 31 percent
shortfall against the full-scale vehicle moves the flow along a part of the curve where little changes.
**The Mach number confirms the same benign picture.** With the speed of sound at 8,000 feet equal to 1,085 feet per second in the same standard \[[U.S. Standard Atmosphere, 1976][ref_atm76]\],

$$\mathrm{Ma} = \frac{428}{1{,}085} = 0.394$$

and that lies well below the drag rise, so **neither of the two dimensionless numbers the model could not match
was doing much harm.** The sensitivity across the disputed scale figures is
small, and the table below sets it out in full.

| $\lambda$ | $\mathrm{Re}$ ratio | time and speed ratio | angular rate ratio |
|---|---|---|---|
| 0.750 | 0.650 | 0.866 | 1.155 |
| 0.778 | 0.686 | 0.882 | 1.134 |
| 0.800 | 0.716 | 0.894 | 1.118 |
| 0.850 | 0.784 | 0.922 | 1.085 |
| 0.900 | 0.854 | 0.949 | 1.054 |

**Nothing in that table changes a conclusion.** Whichever figure is adopted, the aerodynamic
extrapolation is modest and the mass failure is total, and **the article's finding is insensitive to the
one parameter the sources argue about.**

### What the Flight Data Show

**The 2001 flights are documented well enough to recover the flight path angle, which no source states.**
On 12 April 2001 the vehicle was released at 15,050 feet and reached 428 feet per second
\[[X-40A second free flight successful][ref_sciencedaily_x40]\]. The space agency describes the 2001
releases as made from 15,000 feet and followed by an autonomously controlled descent of 75 seconds
\[[X-40A Space Maneuvering Vehicle][ref_nasa_x40]\], and it gives no duration for the 12 April flight in
particular. **The calculation below therefore pairs that flight's altitude and speed with the series
duration.** The release at 8:45 and the stop at 8:47 recorded for 12 April
\[[X-40A second free flight successful][ref_sciencedaily_x40]\] are stated to the minute, so they place
descent and rollout together somewhere between one and three minutes, a window consistent with a 75 second
descent that does not test it.

Mean sink rate is the released altitude divided by the duration.

$$\dot{h} = \frac{15{,}050}{75} = 200.7 \ \text{ft/s}$$

**The sink rate and the speed along the flight path are related by the flight path angle**, and through
that relation the two published figures combine into a third.

$$\dot{h} = V \sin\gamma$$

The flight path angle follows directly.

$$\gamma = \arcsin\left(\frac{200.7}{428}\right) = 28.0^{\circ}$$

**In a steady glide the weight is balanced by lift across the path and by drag along it**, and the ratio
follows from that balance.

$$L = W \cos\gamma \qquad D = W \sin\gamma$$

**The effective lift to drag ratio is therefore the cotangent of the flight path angle**, a
number that describes what kind of approach this was.

$$\frac{L}{D} = \frac{W\cos\gamma}{W\sin\gamma} = \cot\gamma$$

$$\left(\frac{L}{D}\right)_{\text{eff}} = \cot 28.0^{\circ} = 1.88$$

**An effective ratio of 1.88 is a steep energy-management descent and not a best-glide profile**, and the
comparison is drawn from measured flight data. A survey of flight-determined subsonic lift and
drag for seven lifting-body and wing-body reentry configurations puts the achievable maximum for this
class in the range of roughly 3 to 4 \[[Saltzman et al 1999][research_saltzman_1999]\], with later
assessments refining the blunt-based cases \[[Saltzman et al 2002][research_saltzman_2002]\]
\[[Saltzman et al 2007][research_saltzman_2007]\]. **The X-40A was therefore flown at about half its
attainable ratio**, the profile of a vehicle managing energy toward a fixed point rather
than trying to stay airborne.

**The difficulty of that regime is the oldest result in this article's literature.** Approach and landing
at lift to drag ratios of 3 to 4 was investigated in flight in 1959 using a delta-wing aeroplane
\[[Matranga and Menard 1959][research_matranga_1959a]\], and the companion study extended the range down to 2
\[[Matranga and Armstrong 1959][research_matranga_1959b]\]. Later work flew the problem on a transport
\[[Kock et al 1972][research_kock_1972]\], and the effect of the ratio on pilot rating was quantified for a
lifting-body landing task \[[Jackson et al 1991][research_jackson_1991]\]
\[[Jackson et al 1993][research_jackson_1993]\]. **Forty years of work established that this regime is
flyable and unforgiving**, and an autonomous attempt at it should be read in that context.

**Ground range in a steady glide is the height multiplied by the lift to drag ratio**, the force
balance above rewritten for distance.

$$R = h \cot\gamma = h \left(\frac{L}{D}\right)$$

$$R = \frac{15{,}050}{\tan 28.0^{\circ}} = 28{,}353 \ \text{ft} = 4.67 \ \text{nautical miles}$$

**The energy accounting shows how little of the height became speed.** The specific energy available at
release, taking the release from a hover so that the initial kinetic term is negligible, is

$$\frac{E}{m} = g h = (32.174)(15{,}050) = 484{,}219 \ \text{ft}^{2}/\text{s}^{2}$$

against a kinetic term at 428 feet per second of

$$\frac{V^{2}}{2} = \frac{428^{2}}{2} = 91{,}592 \ \text{ft}^{2}/\text{s}^{2}$$

**so 18.9 percent of the available energy was carried as speed and 81.1 percent was spent against drag.**
Put another way, a body falling freely from that height with no drag at all would arrive at

$$V = \sqrt{2gh} = \sqrt{2(32.174)(15{,}050)} = 984 \ \text{ft/s}$$

**more than twice the speed the vehicle reached**, so the descent was dominated by
drag and was not an acceleration.

**One number does transfer, and no other in this section does.** The time scaling relation
converts the observed descent into its full-scale equivalent, because time is the one quantity whose
scaling depends on geometry alone.

$$t_{f} = \frac{t_{m}}{\sqrt{\lambda}} = \frac{75}{\sqrt{0.778}} = 85.0 \ \text{s}$$

**A 75 second rehearsal stands in for an 85 second event**, and that comparison is legitimate in a way
that the speeds and the trajectory are not, because it uses only the length ratio and not the mass.

**The 1998 flight was steeper still.** It was released at about 9,000 feet
\[[Boeing X-37 and X-40][ref_x37_x40]\] some 2.5 miles from the end of the runway
\[[Boeing X-40][ref_x40]\], which at 5,280 feet to the mile is a straight-line ratio of

$$\frac{2.5 \times 5{,}280}{9{,}000} = \frac{13{,}200}{9{,}000} = 1.47$$

and the figure falls if the release altitude of about 10,000 feet given by the Air Force museum is used
\[[Boeing X-40A][ref_nmusaf_x40]\].

$$\frac{13{,}200}{10{,}000} = 1.32$$

**Both are below the 1.88 of the 2001 flights**, and the article does not
resolve which release altitude is correct.

### The Reference Area Is Not Published and Can Be Bounded

**No source gives a wing or planform area for the X-40A**, which blocks a direct wing loading figure. The
steady glide supplies a bound instead. The lift balancing the weight component perpendicular to the
flight path is

$$L = W \cos\gamma = 2{,}600 \cos 28.0^{\circ} = 2{,}297 \ \text{lb}$$

and the same lift is produced aerodynamically, in the equation that converts a force into a
geometry.

$$L = \tfrac{1}{2} \rho V^{2} S C_{L}$$

Taking the density at a mean altitude of 8,000 feet as 0.001869 slug per cubic foot \[[U.S. Standard Atmosphere, 1976][ref_atm76]\], the dynamic pressure
at 428 feet per second is

$$\bar{q} = \tfrac{1}{2} \rho V^{2} = \tfrac{1}{2}(0.001869)(428)^{2} = 171.2 \ \text{lb/ft}^{2}$$

which fixes the product of reference area and lift coefficient without fixing either.

$$S C_{L} = \frac{2{,}297}{171.2} = 13.42 \ \text{ft}^{2}$$

**A planform area near 100 square feet is geometrically plausible for a 22 by 12 foot vehicle**, and it
implies a lift coefficient of 0.134 and a wing loading of 26 pounds per square foot. **Both are stated as
an estimate and neither is a measurement.** The useful part is the product. It is measured, and it
shows the vehicle flying at a low lift coefficient in a fast steep descent rather than at the high angle
of attack a low-speed lifting body approach would suggest.

## Dependent Systems

### Aerodynamics and Shape

**The shape was inherited forward rather than derived.** The X-40A airframe was scaled up by about 120
percent to become the X-37 \[[Boeing X-37][ref_x37]\], which makes this the rare case in the series where
the subscale article came first and set the outer mould line of its successor. **The X-38 borrowed the X-24A shape backwards in time**, as the [X-38 article][related_post_a335_scaled_composites_x38] records, and this programme ran the borrowing in the other direction.

The configuration is a [lifting body][ref_lifting_body] with a fat body, short wings and a V-tail \[[Boeing X-40][ref_x40]\]. **The class had been flown and characterised for three decades before
the X-40A**, through the manned lifting body programme \[[Thompson 1966][research_thompson_1966]\]
\[[Gentry et al 1966][research_gentry_1966]\] \[[Layton and McTigue 1969][research_layton_1969]\], its status reviews
\[[McTigue 1970][research_mctigue_1970]\] and its stability and control derivatives
\[[Kempel et al 1970][research_kempel_1970]\]. **The X-40A inherited a well-understood shape class**,
and that inheritance partly explains why a one million dollar article could be flown with confidence on its first attempt. **The aspect ratio is the property that explains the flight data.**
With a span of 12 feet and an estimated planform of 100 square feet,

$$AR = \frac{b^{2}}{S} = \frac{12^{2}}{100} = 1.44$$

**An aspect ratio near 1.4 sets an induced drag penalty that no amount of cleanliness overcomes**, since
the induced drag coefficient varies inversely with aspect ratio for a given lift coefficient.

$$C_{D_{i}} = \frac{C_{L}^{2}}{\pi e AR}$$

At the measured lift coefficient of 0.134 and an Oswald efficiency of 0.6, the induced contribution is

$$C_{D_{i}} = \frac{0.134^{2}}{\pi (0.6)(1.44)} = 0.0066$$

a value small in absolute terms and small relative to the base and profile drag of a blunt lifting body,
**and that is the point.** At low lift coefficient this shape is dominated by pressure drag rather than
induced drag, so its glide ratio is poor for reasons that have nothing to do with the wing.

### Guidance, Navigation and Control

**The vehicle existed to test this system, and its results are the only ones that transfer.** The 2001
flight series was described by the space agency as an in-flight evaluation of guidance, navigation and
control software for autonomous flight controls \[[X-40A Space Maneuvering Vehicle][ref_nasa_x40]\], and
the vehicle was fitted with navigation systems before the series began
\[[Boeing X-37 and X-40][ref_x37_x40]\].

**The scaling result from the sizing section has a direct and favourable consequence here.** Under
Froude similarity angular rates scale as the inverse square root of the length ratio, so at
$\lambda = 0.778$ the model's angular rates are

$$\frac{\omega_{m}}{\omega_{f}} = \frac{1}{\sqrt{0.778}} = 1.134$$

**times those of the full-scale vehicle.** A control system that stabilises the smaller vehicle is
working about 13 percent faster than it would need to on the larger one.
**The subscale test is conservative for the autopilot.** The usual situation is the opposite, and
this reversal is the strongest single argument for the programme.

**The mass mismatch works in the same direction and more strongly, and it can be quantified rather than
asserted.** Dynamic similarity requires the inertia ratio to be $\lambda^{5}$, while the actual inertia
ratio is the mass ratio times the square of the length ratio.

$$\left(\frac{I_{m}}{I_{f}}\right)_{\text{required}} = 0.778^{5} = 0.285$$

$$\left(\frac{I_{m}}{I_{f}}\right)_{\text{actual}} = (0.236)(0.778)^{2} = 0.143$$

$$\frac{0.143}{0.285} = 0.502$$

**The vehicle carried half the rotational inertia that similarity demanded.** Since angular acceleration
is a moment divided by an inertia, the response to a given control moment is correspondingly quicker.

$$\ddot{\theta} = \frac{M}{I} \quad \Longrightarrow \quad \frac{\ddot{\theta}_{\text{actual}}}{\ddot{\theta}_{\text{similar}}} = \frac{0.285}{0.143} = 1.99$$

**The plant responded about twice as fast as a dynamically similar model would have.** Combined with the
13 percent rate increase from the geometric scale, the control system was exercised against something
appreciably harder to fly than the aircraft it was written for, **and passing that test is informative
even though the trajectory itself does not scale.**

**The demonstrated landing accuracy means more as an angle**, because a lateral error means
little without the range it was achieved over. The published figure belongs to the 1998 flight, which
touched down left of the centreline and then tracked to within 7 feet of it
\[[Boeing X-40][ref_x40]\]. That flight was released 2.5 miles, or 13,200 feet, from the end of the
runway, and the ground track to the point of measurement is at least that long, so the angle subtended is
at most

$$\theta \le \frac{7}{13{,}200} = 5.30 \times 10^{-4} \ \text{rad} = 1.82 \ \text{arcmin}$$

**which is no more than 0.053 percent of the distance flown.** The programme should be judged on that
number, the only figure in the record that speaks directly to whether the autonomy worked. **The
touchdown offset itself is not published**, so the figure measures rollout tracking rather than the
accuracy of the touchdown point.

### Structure and Landing Gear

**The structure had to survive a helicopter drop and a runway rollout, and nothing else.** With no thermal
protection system and no orbital loads, the design case is the landing. Touchdown vertical velocity sets
the energy the gear must absorb, and for a gear stroke $s$ absorbing a sink rate $\dot{h}$ at touchdown
the mean deceleration is

$$a = \frac{\dot{h}^{2}}{2s}$$

**The touchdown sink rate for this class is measured rather than guessed at.** A statistical analysis of
landing contact conditions across three lifting-body research vehicles supplies the distribution a gear
designer would work from \[[Larson 1972][research_larson_1972]\], and the value used here sits
inside it. **A representative touchdown sink of 3 feet per second into a 6 inch stroke gives**

$$a = \frac{3^{2}}{2(0.5)} = 9 \ \text{ft/s}^{2}$$

which is about 0.28 g, and the case is undemanding because the vehicle is light.
**The gear was sized by a mass the operational vehicle would not have had**, and the structural
results therefore do not transfer either.

**The rollout is equally gentle and equally uninformative.** The vehicle stopped in a little over 7,000
feet \[[Boeing X-40][ref_x40]\], so the mean deceleration for a touchdown speed $V_{td}$ is

$$a = \frac{V_{td}^{2}}{2 s} = \frac{V_{td}^{2}}{14{,}000}$$

**No touchdown speed is published**, so the figure is bracketed rather than stated. At 150 feet per second
the mean deceleration is 1.61 feet per second squared, and at 200 feet per second it is 2.86.

$$a\big|_{150} = 0.050 \ g \qquad a\big|_{200} = 0.089 \ g$$

**Under a tenth of a gravity in either case**, the result a light vehicle with no thrust reverser and a
very long runway produces. **The X-37A overran a runway in 2006 at about 120 percent of the linear scale** \[[Boeing X-37][ref_x37]\], and the calculation above shows why the X-40A's rollout, made at a mass the larger vehicle did not share, said nothing useful about that.

### The Carrier and Release System

**Two different helicopters carried it and the change is informative.** The 1998 flight used a
[UH-60 Black Hawk][ref_uh60] releasing from a cradle at about 9,000 feet
\[[Boeing X-37 and X-40][ref_x37_x40]\]. The 2001 series used an Army
[CH-47D Chinook][ref_ch47] from the Aviation Technical Test Center at Fort Rucker, Alabama, lifting to
15,050 feet \[[X-40A second free flight successful][ref_sciencedaily_x40]\].

**The heavier helicopter bought altitude, and altitude is the test article's entire energy budget.** For
an unpowered vehicle the available specific energy at release is

$$\frac{E}{m} = gh + \tfrac{1}{2}V_{0}^{2}$$

and with release from a hover the second term is nearly zero, so **the whole flight is paid for by
height.** The two release altitudes therefore differ by exactly their ratio.

$$\frac{(E/m)_{2001}}{(E/m)_{1998}} = \frac{g(15{,}050)}{g(9{,}000)} = \frac{15{,}050}{9{,}000} = 1.672$$

**The heavier helicopter supplied 67.2 percent more energy**, and the 2001 series spent it on manoeuvres more complex than the straight-in approach flown first \[[X-40A second free flight successful][ref_sciencedaily_x40]\].

### Instrumentation

**The instrumentation requirement follows from what the programme wanted to learn.** Because the
trajectory does not scale, there is little value in high-fidelity aerodynamic instrumentation, and because
the software is the article under test, the valuable measurements are of the navigation state and of the control system's behaviour.

**The programme's own statement of objectives is broader than that argument.** The flight test approach for the 2001 series lists the evaluation of a calculated air data system and of the Honeywell satellite and inertial navigation unit under flight conditions, the tuning of the guidance, navigation and control algorithms, and parameter identification manoeuvres to improve the X-37 aerodynamic database \[[Mitchell 2004][research_mitchell_2004]\]. **The aerodynamic coefficients of a shape do not depend on its mass**, and at 69 percent of full-scale Reynolds number they carry over with the mild correction derived above, so that part of the flight data was meant to inform the successor even though the trajectory was not.

**The record also describes the navigation hardware, and it shows what the navigation testing was for.**
A paper given to the twentieth Digital Avionics Conference in October 2001 reports the testing of the
**Space Integrated Global Positioning System and Inertial Navigation System** during the X-40A approach
and landing campaign, describing it as an off-the-shelf navigation-grade unit enhanced for space and
reentry environments and testing it against differential satellite navigation
\[[Childers et al 2001][research_childers_2001]\]. **Its two stated objectives name the purpose of that testing**, being to demonstrate performance sufficient to meet the X-37 requirement for
automatic autonomous approach and landing, and **to reduce the risk of integrating that unit into
that vehicle.**

**That is a hardware qualification and not a scaling experiment.** It supports this article's thesis, because it shows the programme buying confidence in a component and a software stack rather than a trajectory, **and it does so in the words of the people who ran it.**

## The Flight Test Record

**The X-40A flew eight free flights across two programmes and three years, and every one of them ended in
an autonomous landing** \[[X-40A Space Maneuvering Vehicle][ref_nasa_x40]\] \[[Boeing X-37 and X-40][ref_x37_x40]\].

**The first flight was on 11 August 1998 at Holloman Air Force Base in New Mexico.** It was released from
a cradle beneath a UH-60 at about 9,000 feet and flew to an automatic landing on the designated runway
\[[Boeing X-37 and X-40][ref_x37_x40]\], having been released some 2.5 miles from the end of Runway 04
\[[Boeing X-40][ref_x40]\].
**Boeing described the objective as validating low-speed handling qualities and demonstrating autonomous
approach and landing** \[[Boeing and the Air Force flight test the Space Maneuver Vehicle][ref_boeing_1998]\].
That single flight was the whole of the 1998 campaign \[[X-40A Space Maneuvering Vehicle][ref_nasa_x40]\].

**The vehicle was then loaned to the space agency and flew seven more times in 2001** at Dryden Flight
Research Center at Edwards Air Force Base in California
\[[X-40A Space Maneuvering Vehicle][ref_nasa_x40]\]. The series ran between 4 April and 19 May 2001
\[[Boeing X-37 and X-40][ref_x37_x40]\], with the vehicle lifted to 15,000 feet beneath a CH-47D and
released for an autonomously controlled descent of about 75 seconds onto the main runway
\[[X-40A Space Maneuvering Vehicle][ref_nasa_x40]\].

**The second free flight is the best documented and supplies every number used in the sizing section
above.** On 12 April 2001 the vehicle was released at 15,050 feet at 8:45 in the morning Pacific time and
its wheels rolled to a stop at 8:47, having reached 428 feet per second, and the flight exercised complex
vehicle manoeuvres rather than the straight-in approach flown first
\[[X-40A second free flight successful][ref_sciencedaily_x40]\].

**Landing accuracy is published for the 1998 flight alone.** The vehicle touched down left of the
centreline, deployed its drag chutes, tracked to within 7 feet of the runway centreline and stopped in a
little over 7,000 feet \[[Boeing X-40][ref_x40]\]. That account comes from an encyclopaedia entry, and none of
the sources the entry cites for the flight carries the figures.
**Seven feet is the result that justifies the programme**, because centreline tracking is the
quantity an autonomous landing system is trusted or not trusted on.

**The record contains two conflicts and this article does not resolve either.** One account places
the first Dryden free flight on 14 March 2001 with a straight-in approach
\[[X-40A second free flight successful][ref_sciencedaily_x40]\], the Air Force museum places the first
NASA flight on 28 March 2001 \[[Boeing X-40A][ref_nmusaf_x40]\], and another gives 4 April as the start of
the series \[[Boeing X-37 and X-40][ref_x37_x40]\]. The release altitude of the 1998 flight is given as
9,000 feet \[[Boeing X-37 and X-40][ref_x37_x40]\] and as about 10,000 feet
\[[Boeing X-40A][ref_nmusaf_x40]\].

**The vehicle was retired in May 2001 and is preserved at the National Museum of the United States Air
Force** \[[Boeing X-40][ref_x40]\] \[[Boeing X-40A][ref_nmusaf_x40]\].

## Comparison With Ground Prediction

**The record holds no published ground prediction for the X-40A itself, so a direct comparison cannot be
made.** None of the article's sources reports a wind tunnel campaign, a simulation of the trajectory or a
contractor estimate of the descent that the flights could be checked against. What the article can set
beside the flight record is the expectation the programme stated, the analytical relations derived
under Sizing From First Principles, and the measured behaviour of the vehicle class the shape
came from.

**The stated expectation was met in full.** The programme manager gave the purpose of the first flight as
validating low-speed handling qualities and demonstrating autonomous approach and landing
\[[Boeing and the Air Force flight test the Space Maneuver Vehicle][ref_boeing_1998]\]. Flight returned
eight free flights, each ending in an autonomous landing, and a landing within 7 feet of the runway
centreline on the 1998 flight \[[Boeing X-40][ref_x40]\]. **That is the confirmation of an
objective and not a comparison of numbers**, because no predicted dispersion is published to set the
7 feet against.

**The navigation unit was the only component tested in flight against an independent reference.** The
Space Integrated Global Positioning System and Inertial Navigation System was evaluated during the
approach and landing campaign against differential satellite navigation
\[[Childers et al 2001][research_childers_2001]\]. Its achieved accuracies are in the full report
rather than in its abstract, as Epistemic State notes below, so the article cannot state
how closely flight matched what was required.

**The glide can be compared with its class, and it fell well short of the class maximum.** Flight-determined
subsonic lift and drag for seven lifting-body and wing-body configurations put the attainable maximum ratio
in the range of roughly 3 to 4 \[[Saltzman et al 1999][research_saltzman_1999]\], and the 2001 flight
figures give an effective ratio of 1.88. The sizing analysis above argues that the
gap reflects energy management toward a fixed point rather than an aerodynamic deficit. **The comparison is
against other vehicles' flight data and not against a prediction for this one**, which limits what it can
show.

**The analytical predictions run the other way, from the flight article toward the full-scale vehicle.**
The similarity relations predict that a dynamically similar model at a length ratio of 0.778 would weigh
5,186 lb, and the vehicle weighed about 2,600 lb. The angular rate relation predicts a model responding
about 13 percent faster than the full-scale vehicle, and the inertia shortfall roughly doubled the response
to a given control moment, as argued under Dependent Systems. **Those are predictions about
what the flights could transfer, and the X-37A overrun of 2006 is the nearest thing in the record to a test
of them**, which the next section discusses and Epistemic State
marks as an inference.

**The reference area was never predicted in public and flight recovers it only in part.** The steady glide
fixes the product of planform area and lift coefficient at 13.42 square feet, and the split between them,
a planform near 100 square feet and a lift coefficient of 0.134, is the article's estimate and not a
measurement.

## What the Data Changed

**The programme's output was a validated software stack and a shape, and the shape mattered more than
anybody expected at the time.**

**The airframe became the X-37.** The X-37A airframe is essentially the X-40A scaled up to about
120 percent \[[Boeing X-37 and X-40][ref_x37_x40]\], and the X-37 line flew the Approach and Landing Test
Vehicle flights in 2006 and then flew to orbit \[[Boeing X-37][ref_x37]\]. The scale ratio subsection
above computes 128.5 percent from the published dimensions. **A test article that cost one million dollars to build set the external geometry of a spacecraft
that has since flown for years at a time**, its sixth mission spending 908 days in orbit \[[Boeing X-37][ref_x37]\], and the series has no other
example of such a return on investment.

**The successor programme documented its approach and landing plan in detail**, describing the flight
test approach for the X-37 Approach and Landing Test Vehicle \[[Taylor 2004][research_taylor_2004]\],
its dynamics and stability and control characteristics
\[[Chaudhary et al 2001][research_chaudhary_2001]\], and, afterwards, the lessons the project drew
\[[Turner and Spanyer 2005][research_turner_2005]\].

**The autonomous landing capability was demonstrated and then demonstrated again the hard way.** The
X-37A Approach and Landing Test Vehicle overran the runway and sustained minor damage on its first free
glide flight on 7 April 2006 \[[Boeing X-37][ref_x37]\]. **That is the clearest evidence available that the
X-40A results did not transfer quantitatively**, since the same programme lineage, flying a vehicle
120 percent the size, failed to stop on the runway.

**What the X-40A settled was that the approach was tractable, not that it was solved, and the distinction
can be made numerically.** Eight successes and no failures is a small sample, and the standard one-sided
bound says how small. For $n$ trials with no observed failure, the upper limit on the failure probability
$p$ at confidence $1 - \alpha$ follows from requiring that $n$ successes be no less likely than $\alpha$.

$$(1 - p)^{n} = \alpha \quad \Longrightarrow \quad p_{\max} = 1 - \alpha^{1/n}$$

$$p_{\max} = 1 - 0.05^{1/8} = 0.312$$

**Eight clean landings bound the failure rate only below about 31 percent at 95 percent confidence.**
The bound describes the sample size rather than the vehicle, and in that precise sense
the programme established tractability and not reliability. **A vehicle returning from orbit needs a
figure several orders of magnitude smaller**, and no drop-test campaign of affordable length reaches it.

**What the flights did establish is that the concept, the sensors and the integration work at all**, a
different and necessary result. It does not establish the gains, the margins or the energy
management logic for a heavier vehicle, and the 2006 overrun is what that gap looks like in practice.

**The cost per flight is the other number that makes the programme look sensible.** One million dollars of
fabrication across eight free flights is

$$\frac{1{,}000{,}000}{8} = 125{,}000 \ \text{dollars per flight}$$

**before operating costs, which no source gives.** Whatever the true total, a programme that buys
eight autonomous landings at this order of magnitude is buying them cheaply, and the argument for the
X-40A was never that each flight proved much but that flights were affordable enough to repeat.

**The Space Maneuver Vehicle itself was never built under that name.** The operational concept the X-40A was ninety
percent of was not built as the X-40B, and the designation it briefly held moved to the test article
\[[Boeing X-37 and X-40][ref_x37_x40]\]. **The programme's surviving descendant is a space agency and then
Air Force orbital vehicle rather than the rapid-turnaround military spaceplane that justified it** \[[Boeing X-37][ref_x37]\].

## The Contemporary Literature

| Cluster | Records |
|---|---|
| Dynamic Similarity and Subscale Free Flight | 488 |
| Autonomous and Automatic Landing | 812 |
| Planetary and Lunar Precision Landing | 138 |
| Lifting Bodies and the Unpowered Approach | 352 |
| Guidance, Navigation and Control in the Literature | 422 |
| Reusable Spaceplanes and Orbital Return Vehicles | 611 |
| Entry Aerothermodynamics and Thermal Protection | 732 |
| Touchdown, Rollout and Runway Performance | 409 |
| Demonstrator Programmes and Risk Reduction | 248 |
| Drop Testing, Captive Carry and Release Dynamics | 73 |
| **Total** | **4,285** |

**The survey holds 4,285 research records in ten clusters**, drawn from Crossref, the scholarly registry of Digital Object Identifiers, from the NASA Technical Reports Server and from the Defense Technical Information Center. **Twenty-nine of them are the reports on which the argument rests**, and each is named where the argument uses it. The others map the fields the vehicle sits in, and none of them is cited as evidence for a claim about the X-40A.

### Dynamic Similarity and Subscale Free Flight

**This is the article's keystone and it has a literature of its own.** The cluster gathers dynamically scaled, free-flight and drop models, similitude, and the correlation of wind tunnel and flight data.

Of its 488 titles, 328 name a free-flight, drop, subscale or dynamically scaled model and 71 name the Reynolds number, which is the mismatch that a model matched in Froude number cannot avoid. **The mass condition that this article finds violated is the thin part**, as the section headed Thin Subjects counts.

**488 records.** \[[1967, Similitude and Models][research_similitude_and_1967]\] \[[1992, Similitude Relationships and Scaling Factors][research_similitude_relationships_1992]\] \[[1998, Dimensional Analysis and Dynamic Scaling][research_dimensional_analysis_1998]\] \[[2000, Reynolds Number Effects][research_reynolds_number_2000]\] \[[2009, Dimensional Analysis and Dynamic Similitude][research_dimensional_analysis_2009]\] \[[2015, Dimensional Analysis and Dynamic Similitude][research_dimensional_analysis_2015]\] \[[2017, Scaling and Similitude 1638][research_scaling_and_2017]\] \[[2019, Dimensional Analysis and Dynamic Similarity][research_dimensional_analysis_2019]\] \[[2021, Airborne Computer System Based Collision-Free Flight Path Finding Strategy Design for Drone Model][research_airborne_computer_2021]\] \[[2022, Principles of Dynamic Similarity][research_principles_of_2022]\] \[[Aeroelastic Tests of an 1963][research_aeroelastic_tests_1963]\] \[[Akaryildiz et al 2024][research_akaryildiz_2024]\] \[[Albrecht 1972][research_albrecht_1972]\] \[[Alexander et al 1973][research_alexander_griffin_1973]\] \[[Allen et al 2015][research_allen_sexton_2015]\] \[[Ananda et al 2017][research_ananda_2017]\] \[[Anderson and Armitage 1993][research_anderson_1993]\] \[[Arbic 1955][research_arbic_1955]\] \[[Asl et al 2017][research_asl_niezrecki_2017]\] \[[Azarov and Chernovolov 2018][research_azarov_chernovolov_2018]\] \[[Bagai et al 2010][research_bagai_cantono_2010]\] \[[Baggi et al 2022][research_baggi_2022]\] \[[Balch 1979][research_balch_1979]\] \[[Ballard et al 2013][research_ballard_tanner_2013]\] \[[Bantscheff and Breitsamter 2023][research_bantscheff_breitsamter_2023]\] \[[Barber and Johari 2001][research_barber_johari_2001]\] \[[Barnes 1965][research_barnes_1965]\] \[[Bashir et al 2017][research_bashir_khan_2017]\] \[[Bauer 1964][research_bauer_1964]\] \[[Bennett 1947][research_bennett_1947]\] \[[Bennett 1947][research_bennett_1947_b]\] \[[Bernal and Yu 2015][research_bernal_yu_2015]\] \[[Berry 1982][research_berry_1982]\] \[[Berry et al 2002][research_berry_merski_2002]\] \[[Berthold 1977][research_berthold_1977]\] \[[Berthold 1977][research_berthold_1977_b]\] \[[Bertrand-Noël et al 2022][research_bertrandnoel_bignaletcazalet_2022]\] \[[Betin et al 2023][research_betin_kaluzhynov_2023]\] \[[Betin 2026][research_betin_2026]\] \[[Beyers et al 1997][research_beyers_ericsson_1997]\] \[[Bihrle 1976][research_bihrle_1976]\] \[[Bizzarri and Hendrick 2003][research_bizzarri_hendrick_2003]\] \[[Bogar et al 1996][research_bogar_butters_1996]\] \[[Boisseau 1955][research_boisseau_1955]\] \[[Boschetti et al 2004][research_boschetti_cardenas_2004]\] \[[Bovais et al 1992][research_bovais_haupt_1992]\] \[[Boyer 1964][research_boyer_1964]\] \[[Brandon et al 1996][research_brandon_1996]\] \[[Brandon et al 1997][research_brandon_1997]\] \[[Brandt et al 2019][research_brandt_mclaughlin_2019]\] \[[Braun 1958][research_braun_1958]\] \[[Brice et al 1966][research_brice_perkins_1966]\] \[[Briggs et al 1952][research_briggs_1952]\] \[[Brion et al 2006][research_brion_aki_2006]\] \[[Britcher and Landman 2024][research_britcher_landman_2024]\] \[[Brock][research_brock_nd]\] \[[Brown and Duhon 1965][research_brown_duhon_1965]\] \[[Brown et al 2002][research_brown_yates_2002]\] \[[Brown et al 2006][research_brown_yates_2006]\] \[[Brunner et al 2021][research_brunner_kiefer_2021]\] \[[Budd et al 1993][research_budd_1993]\] \[[Buell and Kenyon 1959][research_buell_1959]\] \[[Burns 1970][research_burns_1970]\] \[[Burt and Haigh 1968][research_burt_haigh_1968]\] \[[Bushnell 2006][research_bushnell_2006]\] \[[Campbell and Seacord 1943][research_campbell_1943]\] \[[Carraway 1988][research_carrawayiii_1988]\] \[[Chamberlin and Blaha 1973][research_chamberlin_blaha_1973]\] \[[Chambers 1988][research_chambers_1988]\] \[[Chambers and Iliff 1981][research_chambers_1981]\] \[[Chambers et al 2019][research_chambers_titchener_2019]\] \[[Chambers 2010][research_chambers_2010]\] \[[Chan et al 2023][research_chan_shea_2023]\] \[[Chang et al 2015][research_chang_ryu_2015]\] \[[Chapman and Compton 1964][research_chapman_1964]\] \[[Charters 1962][research_charters_1962]\] \[[Charters et al 1955][research_charters_1955]\] \[[Chedrik et al 2004][research_chedrik_2004]\] \[[Cochran et al 1978][research_cochran_1978]\] \[[Cochran et al 1979][research_cochran_1979]\] \[[Comer et al 2024][research_comer_bhandari_2024]\] \[[Comer et al 2026][research_comer_atkinson_2026]\] \[[Comer et al 2026][research_comer_chakraborty_2026]\] \[[Constantin et al 2022][research_constantin_2022]\] \[[Cook and Giddings 1984][research_cook_1984]\] \[[Cornelison and Arnold 1997][research_cornelison_1997]\] \[[Courtin et al 2020][research_courtin_hansman_2020]\] \[[Coutinho et al 2016][research_coutinho_baptista_2016]\] \[[Cox et al 2012][research_cox_cunningham_2012]\] \[[Crogan 1961][research_crogan_1961]\] \[[Croke et al 2024][research_croke_green_2024]\] \[[Croom et al 2000][research_croom_2000]\] \[[Cruz][research_cruz_nd_b]\] \[[Cruz and Green 2019][research_cruz_green_2019]\] \[[Cunningham et al 2008][research_cunningham_foster_2008]\] \[[Dantsker 2024][research_dantsker_2024]\] \[[Dantsker 2024][research_dantsker_2024_b]\] \[[Dantsker and Mancuso 2019][research_dantsker_mancuso_2019]\] \[[Dantsker et al 2018][research_dantsker_vahora_2018]\] \[[Dantsker et al 2022][research_dantsker_haviland_2022]\] \[[Dantsker et al 2025][research_dantsker_mancuso_2025]\] \[[Dantsker and Selig 2015][research_dantsker_selig_2015]\] \[[Daum and Mollmann 2017][research_daum_mollmann_2017]\] \[[Davis 1968][research_davis_1968]\] \[[Dayman 1962][research_dayman_1962]\] \[[Dayman 1965][research_dayman_1965]\] \[[Dayman 1966][research_dayman_1966]\] \[[Dayman 1971][research_daymanjr_1971]\] \[[Dean 2024][research_dean_2024]\] \[[Denardo and Canning 1952][research_denardo_1952]\] \[[Disotell et al 2026][research_disotell_nietert_2026]\] \[[Dix and Mattasits 1980][research_dix_mattasits_1980]\] \[[Doenecke 1967][research_doenecke_1967]\] \[[Donovan 1969][research_donovan_1969]\] \[[Dougherty 1975][research_dougherty_1975]\] \[[Draper 1943][research_draper_1943]\] \[[Draper and Hewes 1948][research_draper_1948]\] \[[Droandi et al 2014][research_droandi_2014]\] \[[Du et al 2025][research_du_zhang_2025]\] \[[Eldridge-Allegra et al 2023][research_eldridgeallegra_xu_2023]\] \[[Fan et al 2025][research_fan_nie_2025]\] \[[Fang 2018][research_fang_2018]\] \[[Faúndez 2018][research_faundez_2018]\] \[[Fehrs and Helm 2025][research_fehrs_helm_2025]\] \[[Fiddes et al 1985][research_fiddes_kirby_1985]\] \[[Fisher and Cederborg 1948][research_fisher_1948]\] \[[Fisher et al 2018][research_fisher_quinn_2018]\] \[[Fisher and Windham 1955][research_fisher_1955]\] \[[Fitzgerald and Gingras 1996][research_fitzgerald_1996]\] \[[Foch and Toot 1989][research_foch_toot_1989]\] \[[Foster et al 2020][research_foster_miller_2020]\] \[[Foster et al 2020][research_foster_2020]\] \[[Fratello et al 1987][research_fratello_1987]\] \[[Fremaux 1995][research_fremaux_1995]\] \[[Gainer and Hoffman 1972][research_gainer_1972]\] \[[Gallington and Miller 1970][research_gallington_miller_1970]\] \[[Gang et al 2010][research_gang_wang_2010]\] \[[Garland and Chauvin 1957][research_garland_1957]\] \[[Gee 1978][research_gee_1978]\] \[[Geuther et al 2024][research_geuther_ackerman_2024]\] \[[Ghanchi and Gururajan 2026][research_ghanchi_gururajan_2026]\] \[[Ghate et al 2026][research_ghate_angel_2026]\] \[[Gibson and Marrone 1964][research_gibson_marrone_1964]\] \[[Gibson and Wilenius 1964][research_gibson_wilenius_1964]\] \[[Gibson 2002][research_gibson_2002]\] \[[Gilbert and Goldberg 1967][research_gilbert_goldberg_1967]\] \[[Gillis and Mitchell 1957][research_gillis_1957]\] \[[Girgis et al 2002][research_girgis_brown_2002]\] \[[Glaab et al 2014][research_glaab_2014]\] \[[Goldschmidt et al 2024][research_goldschmidt_tingle_2024]\] \[[Gonzales et al 2021][research_gonzales_kurihara_2021]\] \[[Goodyear Aerospace Corp Akron Oh 1961][research_goodyearaerospacecorpakronoh_1961]\] \[[Goodyer and Kilgore 1972][research_goodyer_kilgore_1972]\] \[[Gopal et al 2026][research_gopal_somaroutu_2026]\] \[[Grafton and Anglin 1975][research_grafton_1975]\] \[[Grafton et al 1974][research_grafton_1974]\] \[[Grana and Shanks 1952][research_grana_1952]\] \[[Gross and Fasel][research_gross_nd]\] \[[Gu et al 2012][research_gu_gross_2012]\] \[[Guo et al 2017][research_guo_zhu_2017]\] \[[Hahne et al 1993][research_hahne_1993]\] \[[Ham and Johnson 1969][research_ham_1969]\] \[[Hannemann et al 2015][research_hannemann_martinezschramm_2015]\] \[[Hannemann et al 2017][research_hannemann_martinezschramm_2017]\] \[[Harrison 1965][research_harrison_1965]\] \[[Harrison and Lockman 1968][research_harrison_lockman_1968]\] \[[Harrison and Marko 1968][research_harrison_marko_1968]\] \[[Harrison et al 1964][research_harrison_1964]\] \[[Hasegawa 2025][research_hasegawa_2025]\] \[[Hatano 1959][research_hatano_1959]\] \[[Hedlund et al 1990][research_hedlund_higgins_1990]\] \[[Hedlund and Ragsdale 1985][research_hedlund_ragsdale_1985]\] \[[Hemsch 1988][research_hemsch_1988]\] \[[Hergert et al 2017][research_hergert_2017]\] \[[Herz et al 2024][research_herz_mccrink_2024]\] \[[Hinton and Eastlake][research_hinton_nd]\] \[[Hodges and Walker 1994][research_hodges_1994]\] \[[Holdo 1993][research_holdo_1993]\] \[[Holleman 1976][research_holleman_1976]\] \[[Holmes and Woehr 1971][research_holmes_woehr_1971]\] \[[Holway 1966][research_holway_1966]\] \[[Hood 1968][research_hood_1968]\] \[[Horstman and Kussoy 1967][research_horstman_1967]\] \[[Howard and Batill 1990][research_howardjr_batill_1990]\] \[[Howell and Braslow 1955][research_howell_1955]\] \[[Hoxey et al 1997][research_hoxey_robertson_1997]\] \[[Hruby and McDevitt 1964][research_hruby_1964]\] \[[Hu and Durbin 2012][research_hu_durbin_2012]\] \[[Hu et al 2013][research_hu_2013]\] \[[Huebner et al 2009][research_huebner_smith_2009]\] \[[Hui and Yang 2013][research_hui_yang_2013]\] \[[Hutter and Jöhnk 2004][research_hutter_johnk_2004]\] \[[Hutter and Wang 2016][research_hutter_wang_2016]\] \[[Hyde and Massie 1993][research_hyde_1993]\] \[[Hyslop et al 2021][research_hyslop_doherty_2021]\] \[[Hyslop et al 2022][research_hyslop_mcgilvray_2022]\] \[[Harasani 2015][research_iharasani_2015]\] \[[Inger 2003][research_inger_2003]\] \[[Inger 2003][research_inger_2003_b]\] \[[Ishida et al 2014][research_ishida_nagai_2014]\] \[[Ishida et al 2015][research_ishida_nagai_2015]\] \[[Ivanco et al 2024][research_ivanco_keller_2024]\] \[[Iwakawa et al 2015][research_iwakawa_furukawa_2015]\] \[[Izraelevitz et al 2022][research_izraelevitz_pauken_2022]\] \[[Jackson and Buttrill 2006][research_jackson_2006]\] \[[Jaffe 1975][research_jaffe_1975]\] \[[Jaffe 1972][research_jaffe_1972]\] \[[James 1959][research_james_1959]\] \[[Janna 2020][research_janna_2020]\] \[[Jarosław et al 2026][research_jaroslaw_robert_2026]\] \[[Javeed et al 1993][research_javeed_1993]\] \[[Jayaraman et al 2022][research_jayaraman_gaurav_2022]\] \[[Jean Ross and Edwards 1987][research_jeanross_edwards_1987]\] \[[Jiang et al 2017][research_jiang_song_2017]\] \[[Johnson 1951][research_johnson_1951]\] \[[Johnson and Boisseau 1953][research_johnson_1953]\] \[[Johnson 1962][research_johnson_1962]\] \[[Jones and Laurence 2025][research_jones_laurence_2025]\] \[[Jordan 1980][research_jordan_1980]\] \[[Jordan and Bailey 2008][research_jordan_bailey_2008]\] \[[Jordan and Hahne 1992][research_jordan_1992]\] \[[Jordan et al 2005][research_jordan_langford_2005]\] \[[Jordan et al 2004][research_jordan_2004]\] \[[Jordan 1980][research_jordanjr_1980]\] \[[Jouannet et al 2012][research_jouannet_berry_2012]\] \[[Jouannet et al 2017][research_jouannet_lundstrom_2017]\] \[[Jouannet et al 2008][research_jouannet_2008]\] \[[Kang et al 2025][research_kang_han_2025]\] \[[Kaplan et al 2023][research_kaplan_patil_2023]\] \[[Karpov and Schmidt 1964][research_karpov_schmidt_1964]\] \[[Kaushik and Anemaat 2012][research_kaushik_anemaat_2012]\] \[[Keller et al 2026][research_keller_mckillipjr_2026]\] \[[Kennell et al 2016][research_kennell_neely_2016]\] \[[Kiddy 1995][research_kiddy_1995]\] \[[Kilgore and Dress 1984][research_kilgore_dress_1984]\] \[[Kilgore et al 1974][research_kilgore_adcock_1974]\] \[[Kilgore 1982][research_kilgore_1982]\] \[[Klein and Noderer 1992][research_klein_1992]\] \[[Kobayakawa and Maeda 1978][research_kobayakawa_maeda_1978]\] \[[Koratkar and Chopra 2001][research_koratkar_chopra_2001]\] \[[Kruggel et al 1999][research_kruggel_sigal_1999]\] \[[Kundu 1990][research_kundu_1990]\] \[[Kunwar and Chakraborty 2025][research_kunwar_chakraborty_2025]\] \[[Kunwar et al 2026][research_kunwar_putra_2026]\] \[[Lam and Stollenwerk 1966][research_lam_stollenwerk_1966]\] \[[Laumann 1966][research_laumann_1966]\] \[[Lee and Han 2012][research_lee_han_2012]\] \[[Lee et al 2003][research_lee_ryu_2003]\] \[[Lee et al 2023][research_lee_cho_2023]\] \[[Lei et al 2020][research_lei_zhong_2020]\] \[[Leuckert et al 2008][research_leuckert_domhardt_2008]\] \[[Levy and McDevitt 1964][research_levy_1964]\] \[[Li et al 2004][research_li_yavuz_2004]\] \[[Li et al 2022][research_li_luo_2022]\] \[[Li et al 2023][research_li_qi_2023]\] \[[Liaño et al 2014][research_liano_castillo_2014]\] \[[Lieske and Kochenderfer 1966][research_lieske_1966]\] \[[Liu et al 2019][research_liu_xiao_2019]\] \[[Lockman 1967][research_lockman_1967]\] \[[Lu et al 2015][research_lu_zhang_2015]\] \[[Lu et al 2016][research_lu_zhang_2016]\] \[[Lu et al 2019][research_lu_zhang_2019]\] \[[Lu et al 2021][research_lu_wang_2021]\] \[[Lucas 1978][research_lucas_1978]\] \[[Lyons 1961][research_lyons_1961]\] \[[MacAllister 1955][research_macallister_1955]\] \[[Madden 1958][research_madden_1958]\] \[[Maggin and Bennett 1947][research_maggin_1947]\] \[[Mahony and Hamel 2001][research_mahony_hamel_2001]\] \[[Mandal and Gu 2016][research_mandal_gu_2016]\] \[[Mao et al 2019][research_mao_xue_2019]\] \[[Martin et al 2004][research_martin_hallam_2004]\] \[[Massa and Cervenka 1995][research_massa_1995]\] \[[Maurya et al 2021][research_maurya_wang_2021]\] \[[Maxwell 2017][research_maxwell_2017]\] \[[McClinton et al 1998][research_mcclinton_voland_1998]\] \[[McKown et al][research_mckown_nd]\] \[[McQuellin and Buttsworth 2024][research_mcquellin_buttsworth_2024]\] \[[Mehrotra and Robinson 1982][research_mehrotra_robinson_1982]\] \[[Melnyk et al 2021][research_melnyk_beattie_2021]\] \[[Miller 1963][research_miller_1963]\] \[[Minami and Tsukamoto 2006][research_minami_tsukamoto_2006]\] \[[Minnema et al 2019][research_minnema_mayersoares_2019]\] \[[Miyakawa et al 1985][research_miyakawa_hirose_1985]\] \[[Mockenhaupt and Wells 1981][research_mockenhaupt_wells_1981]\] \[[Mokry 1974][research_mokry_1974]\] \[[Monti et al 2001][research_monti_paterna_2001]\] \[[Moran et al 2023][research_moran_mcquellin_2023]\] \[[Moreno et al 2018][research_moreno_fugenschuh_2018]\] \[[Mueller et al 2012][research_mueller_landolt_2012]\] \[[Muhlstein et al 1974][research_muhlsteinjr_petroff_1974]\] \[[Munzing and Catris 2015][research_munzing_catris_2015]\] \[[Murch et al 2009][research_murch_cox_2009]\] \[[Murman 1982][research_murman_1982]\] \[[Murphy 1963][research_murphy_1963]\] \[[Murphy 1956][research_murphy_1956]\] \[[Murri et al 1984][research_murri_1984]\] \[[Mwenegoha et al 2019][research_mwenegoha_moore_2019]\] \[[Neal 1970][research_neal_1970]\] \[[Nelson et al 1993][research_nelson_arenajr_1993]\] \[[Newman et al 2014][research_newman_parham_2014]\] \[[Newsom and Anglin 1975][research_newsom_1975]\] \[[Nicolaides 1953][research_nicolaides_1953]\] \[[Nicolaides and Clare 1969][research_nicolaides_1969]\] \[[Niebanck 1969][research_niebanck_1969]\] \[[Nomura et al 2022][research_nomura_itabashi_2022]\] \[[Norton 1922][research_norton_1922]\] \[[Numata et al 2013][research_numata_tsuchiya_2013]\] \[[Nutt and Martindale 1976][research_nutt_martindale_1976]\] \[[O'Kelly 1955][research_o_kelly_1955]\] \[[Obermark 2004][research_obermark_2004]\] \[[Ohe et al 2014][research_ohe_oyama_2014]\] \[[Olejnik et al 2019][research_olejnik_kachel_2019]\] \[[Olejnik et al 2020][research_olejnik_kachel_2020]\] \[[Ouellette et al 2012][research_ouellette_patil_2012]\] \[[Ouellette et al 2014][research_ouellette_patil_2014]\] \[[Owens et al 2006][research_owens_cox_2006]\] \[[Pallister et al 1992][research_pallister_parker_1992]\] \[[Pan et al 2025][research_pan_ma_2025]\] \[[Panda 2022][research_panda_2022]\] \[[Park and Derose 1980][research_park_1980]\] \[[Park et al 2012][research_park_lee_2012]\] \[[Parlett 1974][research_parlett_1974_b]\] \[[Parlett et al 1974][research_parlett_1974]\] \[[Paulson and Johnson 1947][research_paulson_1947]\] \[[Paulson and Johnson 1947][research_paulson_1947_b]\] \[[Peele et al 1968][research_peele_1968]\] \[[Penland and Romeo 1971][research_penland_romeo_1971]\] \[[Penland and Romeo 1971][research_penland_romeo_1971_b]\] \[[Petrović et al 2018][research_petrovic_maneski_2018]\] \[[Pettersson and Rizzi 2006][research_pettersson_rizzi_2006]\] \[[Pieper et al 2018][research_pieper_perry_2018]\] \[[Piet-Lahanier and Serre 2017][research_pietlahanier_serre_2017]\] \[[Pilyugin et al 1994][research_pilyugin_talipov_1994]\] \[[Platou 1968][research_platou_1968]\] \[[Pohly et al 2018][research_pohly_kang_2018]\] \[[Primich and Steinberg 1963][research_primich_1963]\] \[[Prislin][research_prislin_nd]\] \[[Prislin and Wilson 1967][research_prislin_1967]\] \[[Pusztai et al 2024][research_pusztai_lowenberg_2024]\] \[[Pyle and Saltzman 1973][research_pyle_1973]\] \[[Quast et al 1990][research_quast_henke_1990]\] \[[Ragheb et al 2013][research_ragheb_dantsker_2013]\] \[[Rainey and Igoe 1958][research_rainey_1958]\] \[[Raju Kulkarni et al 2019][research_rajukulkarni_varriale_2019]\] \[[Raju Kulkarni et al 2019][research_rajukulkarni_larocca_2019]\] \[[Raju Kulkarni et al 2022][research_rajukulkarni_larocca_2022]\] \[[Raman et al 2000][research_raman_anderson_2000]\] \[[Raney 1987][research_raney_1987]\] \[[Raney and Batterson 1989][research_raney_1989]\] \[[Raymer 2001][research_raymer_2001]\] \[[Redd et al 1979][research_redd_1979]\] \[[Reed 1966][research_reed_1966]\] \[[Reich et al 2015][research_reich_willits_2015]\] \[[Ricciardi et al 2016][research_ricciardi_2016]\] \[[Richardson 1976][research_richardson_1976]\] \[[Ritter et al 2016][research_ritter_neumann_2016]\] \[[Rivera et al 2025][research_rivera_hein_2025]\] \[[Rocha et al 2025][research_rocha_bauzermedeiros_2025]\] \[[Roepke 1972][research_roepke_1972]\] \[[Rogers and Walter K 1955][research_rogers_walterk_1955]\] \[[Rogers and Walter K. 1953][research_rogers_1953]\] \[[Rona and Soueid 2010][research_rona_soueid_2010]\] \[[Rooney et al 1977][research_rooney_craig_1977]\] \[[Rosenthal 1982][research_rosenthal_1982]\] \[[Roxburgh 2015][research_roxburgh_2015]\] \[[Rudnik and Germain 2009][research_rudnik_germain_2009]\] \[[Ruiz Garcia et al 2022][research_ruizgarcia_brown_2022]\] \[[Sadovnitchii et al 1997][research_sadovnitchii_ryabkov_1997]\] \[[Sadovnychiy et al 1998][research_sadovnychiy_betin_1998]\] \[[Sadovnychiy et al 1999][research_sadovnychiy_betin_1999]\] \[[Sadovnychiy et al 2001][research_sadovnychiy_ryzhenko_2001]\] \[[Sahu 2005][research_sahu_2005]\] \[[Samardžić et al 2013][research_samardzic_isakovic_2013]\] \[[Sansica and Hashimoto 2023][research_sansica_hashimoto_2023]\] \[[Saunders 1996][research_saunders_1996]\] \[[Schang 2024][research_schang_2024]\] \[[Scherberg and Rhode 1927][research_scherberg_1927]\] \[[Schermerhorn 1969][research_schermerhorn_1969_b]\] \[[Schermerhorn 1969][research_schermerhorn_1969]\] \[[Schrauf and Schröder 1999][research_schrauf_schroder_1999]\] \[[Seiff 1954][research_seiff_1954]\] \[[Seiff et al 1952][research_seiff_1952]\] \[[Seiler et al 2012][research_seiler_bastide_2012]\] \[[Sellers 2000][research_sellers_2000]\] \[[Sforza and Anderson 2003][research_sforza_2003]\] \[[Shahrbabaki et al 2014][research_shahrbabaki_bazazzadeh_2014]\] \[[Shakoori et al 2012][research_shakoori_mortazavi_2012]\] \[[Shakoori et al 2017][research_shakoori_betin_2017]\] \[[Shalaby 2018][research_shalaby_2018]\] \[[Sharma et al 2011][research_sharma_vidal_2011]\] \[[Shea et al 2023][research_shea_chan_2023]\] \[[Shen et al 2019][research_shen_li_2019]\] \[[Shepheard 1965][research_shepheard_1965]\] \[[Shields and Mohseni 2011][research_shields_mohseni_2011]\] \[[Shinbrot 2019][research_shinbrot_2019]\] \[[Silva et al 2009][research_silva_gamarra_2009]\] \[[Simmons and Ackerman 2026][research_simmons_ackerman_2026]\] \[[Simmons et al 2025][research_simmons_ackerman_2025]\] \[[Sims and Carter 1981][research_sims_carter_1981]\] \[[Singleton and Yeager 1998][research_singleton_1998]\] \[[Smith and Dutta 2017][research_smith_2017]\] \[[Smith et al 1996][research_smith_1996_b]\] \[[Smotrova 2002][research_smotrova_2002]\] \[[Sobron et al 2021][research_sobron_lundstrom_2021]\] \[[Soencksen and Whyte 1999][research_soencksen_whyte_1999]\] \[[Sommer 1960][research_sommer_1960]\] \[[Song et al 2013][research_song_cai_2013]\] \[[Spreiter and Steffen 1946][research_spreiter_steffen_1946]\] \[[Spurlin and Lueck 1984][research_spurlin_lueck_1984]\] \[[Squires 2004][research_squires_2004]\] \[[Starkey et al 2012][research_starkey_argrow_2012]\] \[[Stephens 1959][research_stephens_1959]\] \[[Stilley 1988][research_stilley_1988]\] \[[Stollery and Murthy 1978][research_stollery_murthy_1978]\] \[[Stout 1946][research_stout_1946]\] \[[Straub and Johnston 1987][research_straub_1987]\] \[[Straub et al 1984][research_straub_johnston_1984]\] \[[Stuessy et al 1997][research_stuessy_peeples_1997]\] \[[Stuper 1934][research_stuper_1934]\] \[[Sun et al 2024][research_sun_qiu_2024]\] \[[Tabatabaei et al 2021][research_tabatabaei_orlu_2021]\] \[[Tenhave et al 2026][research_tenhave_joiner_2026]\] \[[Threadgill et al 2024][research_threadgill_hader_2024]\] \[[Tian 1980][research_tian_1980]\] \[[Tokugawa et al 2025][research_tokugawa_ishida_2025]\] \[[Trushlyakov and Yudintsev 2019][research_trushlyakov_yudintsev_2019]\] \[[Tsushima et al 2024][research_tsushima_saitoh_2024]\] \[[Turner 1950][research_turner_1950]\] \[[Turner 1965][research_turner_1965]\] \[[Uppoor and Chopra 2026][research_uppoor_2026]\] \[[Uppoor et al 2025][research_uppoor_zheng_2025]\] \[[Uppoor et al 2026][research_uppoor_chopra_2026]\] \[[Usry and Wallace 1971][research_usry_1971]\] \[[Viviand 1991][research_viviand_1991]\] \[[Vocke and Nunez 2016][research_vocke_nunez_2016]\] \[[Von Pragenau 1966][research_pragenau_1966]\] \[[Von Pragenau 1967][research_pragenau_1967]\] \[[Vorburger et al 1985][research_vorburger_mclay_1985]\] \[[Vos et al 2007][research_vos_hodigeresiddaramaiah_2007]\] \[[Waldmann et al 2023][research_waldmann_ehrle_2023]\] \[[Wallskog 1954][research_wallskog_1954]\] \[[Wang et al 2020][research_wang_yin_2020]\] \[[Wang et al 2020][research_wang_zhang_2020]\] \[[Wang et al 2021][research_wang_2021]\] \[[Ward and Myers 1967][research_ward_myers_1967]\] \[[Ward et al 2025][research_ward_ho_2025]\] \[[Ward et al 2026][research_ward_collins_2026]\] \[[Warren 2024][research_warren_2024]\] \[[Warsop and Crowther 2019][research_warsop_crowther_2019]\] \[[Wee and Yechout 2004][research_wee_yechout_2004]\] \[[Weinacht 2003][research_weinacht_2003]\] \[[Welsh and Watt 1967][research_welsh_1967]\] \[[Welton 1965][research_welton_1965]\] \[[Wendel et al 1991][research_wendel_1991]\] \[[White and Gibson 2004][research_white_gibson_2004]\] \[[White and James J 1967][research_white_jamesj_1967]\] \[[Wilder and Prabhu 2019][research_wilder_2019]\] \[[Wilder et al 2015][research_wilder_2015]\] \[[Williams et al 1994][research_williams_1994]\] \[[Williams 2021][research_williams_2021]\] \[[Wilson and Chou 1985][research_wilson_chou_1985]\] \[[Winchenbach 1997][research_winchenbach_1997]\] \[[Winski et al 2025][research_winski_langston_2025]\] \[[Woodbury and Wallace 1974][research_woodbury_1974]\] \[[Wright 1992][research_wright_1992]\] \[[Wu 2023][research_wu_2023]\] \[[Wyborny and Requardt 1974][research_wyborny_requardt_1974]\] \[[Wyborny and Requardt 1975][research_wyborny_requardt_1975]\] \[[Xu et al 2018][research_xu_fu_2018]\] \[[Xue et al 2019][research_xue_qin_2019]\] \[[Yamasaki et al 2013][research_yamasaki_matsumoto_2013]\] \[[Yang and Li 2008][research_yang_li_2008]\] \[[Yang et al 2023][research_yang_chen_2023]\] \[[Yang et al 2025][research_yang_zhang_2025]\] \[[Yao et al 2021][research_yao_li_2021]\] \[[Yarlett et al 2000][research_yarlett_adrezin_2000]\] \[[Yates and Venkatapathy 1991][research_yates_1991]\] \[[Yerdon and Cook 2015][research_yerdon_cook_2015]\] \[[YiFan et al 2024][research_yifan_minghe_2024]\] \[[Yip 1987][research_yip_1987]\] \[[Yip et al 1990][research_yip_1990]\] \[[Yoshinaga et al 1995][research_yoshinaga_tate_1995]\] \[[You et al 2019][research_you_yasaee_2019]\] \[[Youngshin Kang et al 2008][research_kang_2008]\] \[[Yue et al 2022][research_yue_zuo_2022]\] \[[Zhou et al 2019][research_zhou_liang_2019]\] \[[Zumwalt et al 2016][research_zumwalt_cruz_2016]\]

### Autonomous and Automatic Landing

**The capability the X-40A existed to demonstrate is now ordinary and was not then.** The cluster runs from automatic landing studies for the Shuttle and autoland for transport aircraft to vision-guided landing of uncrewed aircraft.

Of its 812 titles, 273 concern uncrewed aircraft or rotorcraft, 108 concern landing on a carrier, a ship or another moving platform, and 68 concern the Shuttle, a reusable launch vehicle, a spaceplane or another unpowered return vehicle. **The landing problem the X-40A rehearsed is a small part of this literature**, which has moved to small uncrewed aircraft and to moving decks.

**812 records.** \[[1963, Flying Controls and Automatic Landing][research_flying_controls_1963]\] \[[1964, Automatic Landing][research_automatic_landing_1964]\] \[[1971, Inertially augmented approach and landing systems][research_inertially_augmented_1971]\] \[[1971, The Advance Towards Category Three Automatic Landings][research_the_advance_1971]\] \[[1978, Space Shuttle Orbiter Approach and Landing Test Final Evaluation Report][research_alt_final_1978]\] \[[1979, Evaluation of the navigation performance of shipboard-VTOL-landing guidance systems][research_evaluation_of_1979]\] \[[1979, Flight test of a VTOL digital autoland system along complex trajectories][research_flight_test_1979]\] \[[1994, 180 Fault Tolerant navigation system for aircraft landing][research_180_fault_1994]\] \[[1994, Further development and flight test of an autonomous precision landing system using a parafoil][research_further_development_1994]\] \[[1996, Aircraft Automatic Approach and Landing Using GPS][research_aircraft_automatic_1996]\] \[[2007, Automatic Landing System using a Trajectory of Laser Beam][research_automatic_landing_2007]\] \[[2008, Automatic Landing Guidance Law Design for Unmanned Aerial Vehicles based on Pursuit Guidance Law][research_automatic_landing_2008]\] \[[2008, Three-Dimensional Location Tracking System for Automatic Landing of an Unmanned Helicopter][research_three_dimensional_location_2008]\] \[[2013, LP Based Path Planning for Autonomous Landing of An Unmanned Helicopter on A Moving Platform][research_lp_based_2013]\] \[[2016, Flight Test Data Analysis of Hybrid Vertical Take-off and Landing Unmanned Aerial Vehicle][research_flight_test_2016]\] \[[2019, Radar Altimeter Aiding of GNSS for Precision Approach and Landing of RPA][research_radar_altimeter_2019]\] \[[2020, The algorithm of the color signal recognition at landing an unmanned aerial vehicle on an aircraft carrier in autonomous mode][research_the_algorithm_2020]\] \[[2024, Mobile Autonomous Recovery Landing Principle and Control Method for Unmanned Aerial Vehicle][research_mobile_autonomous_2024]\] \[[2025, Approach to solving the problem of landing an unmanned aerial vehicle on a moving landing platform][research_approach_to_2025]\] \[[2025, Trajectory Shaping Guidance for Vertical Landing of Launch Vehicle Stage][research_trajectory_shaping_2025]\] \[[Abershitz et al 2009][research_abershitz_rubinets_2009]\] \[[Abujoub et al 2018][research_abujoub_mcphee_2018]\] \[[Ahmed et al 2017][research_ahmed_hazry_2017]\] \[[Ahmed 2021][research_ahmed_2021]\] \[[Ai et al 2023][research_ai_hu_2023]\] \[[Akash and Anbarasu 2025][research_akash_anbarasu_2025]\] \[[AL-Bakri and Kluever 2017][research_albakri_kluever_2017]\] \[[Al-Bakri et al 2020][research_albakri_albakri_2020]\] \[[Al-Sharman et al 2018][research_alsharman_aljarrah_2018]\] \[[Alatorre Sevilla][research_sevilla_nd]\] \[[Ali et al 2024][research_ali_abbas_2024]\] \[[Alijani and Osman 2020][research_alijani_osman_2020]\] \[[Alonis 1988][research_alonis_1988]\] \[[Alpert 2001][research_alpert_2001]\] \[[Altmann 2013][research_altmann_2013]\] \[[Amelin 2022][research_amelin_2022]\] \[[An Su-yang et al 2016][research_ansuyang_zhangfeijuan_2016]\] \[[Anand et al 2020][research_anand_barman_2020]\] \[[Andreev and Stanchev 2020][research_andreev_stanchev_2020]\] \[[Andrews 1977][research_andrews_1977]\] \[[Anh et al 2022][research_anh_tran_2022]\] \[[Anitha and Kumar 2012][research_anitha_kumar_2012]\] \[[Aoki and Ishigami 2022][research_aoki_ishigami_2022]\] \[[Arents et al 2009][research_arents_groeneweg_2009]\] \[[Armutcuoglu et al 2004][research_armutcuoglu_kavsaoglu_2004]\] \[[Arshad et al 2021][research_arshad_kallungal_2021]\] \[[Ashkenas et al 1982][research_ashkenas_1982]\] \[[Asyraf and Omar 2026][research_asyraf_omar_2026]\] \[[Atmeh et al 2011][research_atmeh_altaq_2011]\] \[[Avtin et al 2021][research_avtin_baburov_2021_b]\] \[[Avtin et al 2021][research_avtin_baburov_2021]\] \[[Azimov 2013][research_azimov_2013]\] \[[Baca et al 2017][research_baca_stepan_2017]\] \[[Bailey and Smith 1982][research_bailey_1982]\] \[[Balas 2003][research_balas_2003]\] \[[Baldini et al 2020][research_baldini_anandkumar_2020]\] \[[Belabbas et al 2010][research_belabbas_dautermann_2010]\] \[[Belcastro and Hogge 2004][research_belcastro_2004]\] \[[Benbow 1971][research_benbow_1971]\] \[[Beresford and Asteraki 1961][research_beresford_asteraki_1961]\] \[[Berger et al 2012][research_berger_tischler_2012]\] \[[Berradi et al 2017][research_berradi_moutaouakkil_2017]\] \[[Betin et al 2023][research_betin_kyriienko_2023]\] \[[Bian et al 2018][research_bian_nener_2018]\] \[[Biannic and Roos 2018][research_biannic_roos_2018]\] \[[Bickford et al 1997][research_bickford_bickmore_1997]\] \[[Bischoff et al 1974][research_bischoff_duffy_1974]\] \[[Blom 2017][research_blom_2017]\] \[[Bobko 2012][research_bobko_2012]\] \[[Bonner and Pride 1976][research_bonner_1976]\] \[[Borges et al 2026][research_borges_burnside_2026]\] \[[Borowczyk et al 2017][research_borowczyk_nguyen_2017]\] \[[Borowczyk et al 2017][research_borowczyk_nguyen_2017_b]\] \[[Boskovic and Redding 2009][research_boskovic_redding_2009]\] \[[Bossi et al 1989][research_bossi_1989]\] \[[Brady 1969][research_brady_1969]\] \[[Brice and Sugano 1978][research_brice_sugano_1978]\] \[[Britcher et al 2024][research_britcher_datta_2024]\] \[[Brockers et al 2012][research_brockers_2012]\] \[[Broglio 1961][research_broglio_1961]\] \[[Broussard et al 1983][research_broussard_bryant_1983]\] \[[Brown et al 1983][research_brown_1983]\] \[[Brown et al 1984][research_brown_1984]\] \[[Bruckner et al 2010][research_bruckner_vangraas_2010]\] \[[Bryant et al 1998][research_bryant_tigges_1998]\] \[[Bryson 1969][research_brysonjr_1969]\] \[[Brzozowski et al 2014][research_brzozowski_kordowski_2014]\] \[[Bu et al 2016][research_bu_ai_2016]\] \[[Buchnev and Danilov 2026][research_buchnev_danilov_2026]\] \[[Bull et al 1981][research_bull_1981]\] \[[Busnardo et al 2011][research_busnardo_aitken_2011]\] \[[Cao et al 2012][research_cao_ding_2012]\] \[[Carnes et al 2015][research_carnes_bakker_2015]\] \[[Carson et al 2015][research_carson_robertson_2015]\] \[[Castro et al 2006][research_castro_bennani_2006]\] \[[Cesetti et al 2009][research_cesetti_frontoni_2009]\] \[[Cetin and Kutay 2016][research_cetin_kutay_2016]\] \[[Cetin et al 2010][research_cetin_kurnaz_2010]\] \[[Chambers 1980][research_chambers_1980]\] \[[Chamitoff 1994][research_chamitoff_1994]\] \[[Chamitoff 1995][research_chamitoff_1995]\] \[[Chen et al 2022][research_chen_man_2022]\] \[[Chen et al 2023][research_chen_han_2023]\] \[[Chen et al 2025][research_chen_wu_2025]\] \[[Chen et al 2025][research_chen_shi_2025]\] \[[Chen 2018][research_chen_2018]\] \[[Chen 2021][research_chen_2021]\] \[[Cheney and Pham 1988][research_cheney_pham_1988]\] \[[Cheng and Lai 2025][research_cheng_lai_2025]\] \[[Cheng and Shyur 2025][research_cheng_shyur_2025]\] \[[Chernenko and Burnashev 2022][research_chernenko_burnashev_2022]\] \[[Chirayath and Bindu 2014][research_chirayath_bindu_2014]\] \[[Chitrakaran et al 2005][research_chitrakaran_dawson_2005]\] \[[Choi et al 2005][research_choi_lim_2005]\] \[[Chowdhary and Johnson 2008][research_chowdhary_johnson_2008]\] \[[Chowdhury and Keshmiri 2022][research_chowdhury_keshmiri_2022]\] \[[Chowdhury et al 2026][research_chowdhury_joshi_2026]\] \[[Clary et al 1984][research_clary_1984]\] \[[Clary et al 1984][research_clary_1984_b]\] \[[Clos-Cot et al 2018][research_closcot_templai_2018]\] \[[Cocchioni et al 2014][research_cocchioni_mancini_2014]\] \[[Cockayne and Rusnak 1971][research_cockayne_1971]\] \[[Cohen et al 1994][research_cohen_pervan_1994]\] \[[Colwell 1966][research_colwell_1966]\] \[[Computer vision-based approach for 2025][research_computer_vision_2025]\] \[[Coopmans et al 2015][research_coopmans_podhradsky_2015]\] \[[Crassidis and Mook 1991][research_crassidis_mook_1991]\] \[[Crassidis and Mook 1992][research_crassidis_mook_1992]\] \[[Crassidis et al 1993][research_crassidis_mook_1993]\] \[[Crawford and Duiven 1973][research_crawford_1973]\] \[[Cui et al 2022][research_cui_chen_2022]\] \[[Dalang et al 2023][research_dalang_kulathunga_2023]\] \[[Daquan Tang et al 2016][research_daquantang_yongkangjiao_2016]\] \[[Davis et al 1985][research_davis_1985]\] \[[de Alvear Cárdenas and Looye 2021][research_dealvearcardenas_looye_2021]\] \[[De Divitiis 2003][research_dedivitiis_2003]\] \[[de Paula et al 2026][research_depaula_quintero_2026]\] \[[De Wagter and Meulenbeld 2019][research_dewagter_meulenbeld_2019]\] \[[Demarchi and Haning 1978][research_demarchi_haning_1978]\] \[[Demir and Seyfullah Babaarslan 2021][research_demir_seyfullahbabaarslan_2021]\] \[[Denaro and Beser 1986][research_denaro_1986]\] \[[Deng and Duan 2016][research_deng_duan_2016]\] \[[Deniz et al 2018][research_deniz_balakrishnan_2018]\] \[[Dermer][research_dermer_nd]\] \[[Devesa et al 2004][research_devesa_jourdan_2004]\] \[[Dieffenbach 1995][research_dieffenbach_1995]\] \[[Dieroff and Schaenzer 1990][research_dieroff_schaenzer_1990]\] \[[Ding 2015][research_ding_2015]\] \[[Dirs 1966][research_dirs_1966]\] \[[Doche et al 2001][research_doche_verniermounier_2001]\] \[[Doherr et al 1997][research_doherr_jann_1997]\] \[[Doland 1976][research_doland_1976]\] \[[Dong et al 2023][research_dong_wu_2023]\] \[[Dorr et al 1994][research_dorr_1994]\] \[[Dou and Duan 2017][research_dou_duan_2017]\] \[[Dougherty and Lee 2016][research_dougherty_lee_2016]\] \[[Douglas Aircraft Co Long Beach Ca 1963][research_ca_1963_b]\] \[[Downing and Bryant 1979][research_downing_1979]\] \[[Downing and Bryant 1987][research_downing_bryant_1987]\] \[[Downing et al 1981][research_downing_1981]\] \[[Drinkwater and Cooper 1958][research_drinkwater_1958]\] \[[Duan et al 2022][research_duan_yuan_2022]\] \[[Duehring et al 2023][research_duehring_egan_2023]\] \[[Durocher 1978][research_durocher_1978]\] \[[Dutasatria and Darma 2020][research_dutasatria_darma_2020]\] \[[Dynnikov 2020][research_dynnikov_2020]\] \[[Edwards et al 1975][research_edwards_1975]\] \[[Eichhorn et al 2022][research_eichhorn_fritzsche_2022]\] \[[Eichhorn and Silvestre 2023][research_eichhorn_silvestre_2023]\] \[[Eigenmann et al 1984][research_eigenmann_kitzmiller_1984]\] \[[Eitner et al 2013][research_eitner_braun_2013]\] \[[Ema 1992][research_ema_1992]\] \[[Engle and Truly 1977][research_engle_1977]\] \[[Epp et al 2015][research_epp_robertson_2015]\] \[[Esposito and Orlando 2024][research_esposito_orlando_2024]\] \[[Estupinan and Prazenica 2026][research_estupinan_prazenica_2026]\] \[[Evangelisti and Pfifer 2024][research_evangelisti_pfifer_2024]\] \[[Fathurrahman and Jenie 2022][research_fathurrahman_jenie_2022]\] \[[Fearnside 1959][research_fearnside_1959]\] \[[Feather and Craven 1991][research_feather_1991]\] \[[Feinreich and Gevaert 1980][research_feinreich_1980]\] \[[Ferreres and Puyou 2006][research_ferreres_puyou_2006]\] \[[Field and Rossitto 1999][research_field_rossitto_1999]\] \[[Forssell and Hyden 2003][research_forssell_hyden_2003]\] \[[Fortenbaugh 1972][research_fortenbaugh_1972]\] \[[Foster 1972][research_foster_1972]\] \[[Franklin and Innis 1972][research_franklin_1972]\] \[[Franklin and Innis 1977][research_franklin_innis_1977]\] \[[Franklin and Innis 1978][research_franklin_innis_1978]\] \[[Franklin et al 1985][research_franklin_hynes_1985]\] \[[Fravolini et al 2004][research_fravolini_campa_2004]\] \[[Fravolini et al 2015][research_fravolini_yucelen_2015]\] \[[Frenkel and Shaferman 2026][research_frenkel_shaferman_2026]\] \[[Fu et al 2025][research_fu_dang_2025]\] \[[Fujimori et al 2000][research_fujimori_kurozumi_2000]\] \[[Fullerton 1975][research_fullerton_1975]\] \[[Gabarrou et al 2010][research_gabarrou_alazard_2010]\] \[[Gallaher et al 1996][research_gallaher_coughlin_1996]\] \[[Gannett 1964][research_gannett_1964]\] \[[Gao et al 2021][research_gao_an_2021]\] \[[Gao et al 2021][research_gao_an_2021_b]\] \[[Garcia 2008][research_garcia_2008]\] \[[Garcia-Pardo et al 2001][research_garciapardo_sukhatme_2001]\] \[[Georghiou et al 1986][research_georghiou_metcalfe_1986]\] \[[Gerratt et al 2020][research_gerratt_strate_2020]\] \[[Gilson and Fenton 1973][research_gilson_1973]\] \[[Gold and Walchli 1974][research_gold_1974]\] \[[Gorskiy and Subkhangulov 2025][research_gorskiy_subkhangulov_2025]\] \[[Goto et al 2001][research_goto_miyazawa_2001]\] \[[Gouskov 1972][research_gouskov_1972]\] \[[Gracey 1967][research_gracey_1967]\] \[[Grantham and Williams 1987][research_grantham_williams_1987]\] \[[Gregory et al 2011][research_gregory_xargay_2011]\] \[[Greiser et al 2011][research_greiser_lantzsch_2011]\] \[[Guo et al 2016][research_guo_yue_2016]\] \[[Guo et al 2025][research_guo_wang_2025_b]\] \[[Guo et al 2026][research_guo_huang_2026]\] \[[Guorong Zhao et al 2006][research_guorongzhao_jixinli_2006]\] \[[Gutt et al 2004][research_gutt_fischer_2004]\] \[[Guy 1976][research_guy_1976]\] \[[Gök and Ci̇han 2022][research_gok_cihan_2022]\] \[[Haise 1977][research_haise_1977]\] \[[Halyo 1987][research_halyo_1987]\] \[[Hameed and Bindu 2019][research_hameed_bindu_2019]\] \[[Hammel 2004][research_hammel_2004]\] \[[Han and Shuping 2015][research_han_shuping_2015]\] \[[Hang et al 2025][research_hang_rui_2025]\] \[[Hann-Shing Ju and Ching-Chih Tsai 2007][research_hannshingju_chingchihtsai_2007]\] \[[Harcus and Bright 2020][research_harcus_bright_2020]\] \[[Hardy 1972][research_hardy_1972]\] \[[Harris 2018][research_harris_2018]\] \[[Harrison 1967][research_harrison_1967]\] \[[Hayashi et al 2025][research_hayashi_yamasaki_2025]\] \[[He et al 2012][research_he_lee_2012]\] \[[He et al 2023][research_he_zhang_2023]\] \[[Hebbar and Pashilkar 2017][research_hebbar_pashilkar_2017]\] \[[Hecker et al 2019][research_hecker_bestmann_2019]\] \[[Hendrick and Horn 2024][research_hendrick_horn_2024]\] \[[Heo et al 2004][research_heo_pervan_2004]\] \[[Herissé et al 2012][research_herisse_hamel_2012]\] \[[Heydari and Balakrishnan 2011][research_heydari_balakrishnan_2011]\] \[[Hoang et al 2017][research_hoang_bayasgalan_2017]\] \[[Hodgkinson and Johnston 1979][research_hodgkinson_johnston_1979]\] \[[Hofmann et al 1978][research_hofmann_1978]\] \[[Hofsäß et al 2023][research_hofsass_braun_2023]\] \[[Holley and Bryson 1975][research_holley_brysonjr_1975]\] \[[Holmes and Langelaan 2016][research_holmes_langelaan_2016]\] \[[Hoole et al 2021][research_hoole_sartor_2021]\] \[[Horn et al 2014][research_horn_tritschler_2014]\] \[[Hornbuckle 2015][research_hornbuckle_2015]\] \[[Howard 1976][research_howard_1976]\] \[[Hoy 1963][research_hoy_1963]\] \[[Hryshchenko et al 2018][research_hryshchenko_romanenko_2018]\] \[[Hu et al 2022][research_hu_guo_2022]\] \[[Huan et al 2015][research_huan_guoliang_2015]\] \[[Huang et al 2009][research_huang_liu_2009]\] \[[Huang et al 2015][research_huang_zhang_2015]\] \[[Hueschen 1984][research_hueschen_1984]\] \[[Hueschen 1985][research_hueschen_1985]\] \[[Hugo and Engelbrecht 2016][research_hugo_2016]\] \[[Humphreys et al 1988][research_humphreys_1988]\] \[[Hundley et al 1993][research_hundley_rowson_1993]\] \[[Hung et al 2024][research_hung_unger_2024]\] \[[Hunter and Wilson 1976][research_hunter_wilson_1976]\] \[[Hunter 1973][research_hunter_1973]\] \[[Hynes et al 1987][research_hynes_hardy_1987]\] \[[Hyokawa and Ueba 2023][research_hyokawa_ueba_2023]\] \[[Hyun 2005][research_hyun_2005]\] \[[Iizuka 2024][research_iizuka_2024]\] \[[Iliev and Nachev 2022][research_iliev_nachev_2022]\] \[[Ingle and Celi 1994][research_ingle_celi_1994]\] \[[Ishioka et al 2019][research_ishioka_uchiyama_2019]\] \[[Ismail et al 2015][research_ismail_pashilkar_2015]\] \[[Ivanov et al 2013][research_ivanov_huertas_2013]\] \[[Ivins 1978][research_ivins_1978]\] \[[Urnes et al 1981][research_jmurnes_moomaw_1981]\] \[[Jacklin 2008][research_jacklin_2008]\] \[[Jacob 1991][research_jacob_1991]\] \[[Jasra et al 2020][research_jasra_valentino_2020]\] \[[Jayaraman et al 2022][research_jayaraman_saini_2022]\] \[[Jeong et al 2013][research_jeong_ryu_2013]\] \[[Jiang et al 2018][research_jiang_zhen_2018]\] \[[Jin et al 2017][research_jin_zhu_2017]\] \[[Jindong and Zhiqiang 2011][research_jindong_zhiqiang_2011]\] \[[Jing et al 2020][research_jing_qi_2020]\] \[[Johannsen et al 1976][research_johannsen_pfendler_1976]\] \[[Johnsen et al 2022][research_johnsen_runnels_2022]\] \[[Johnson et al 2008][research_johnson_calise_2008]\] \[[Jones 1970][research_jones_1970]\] \[[Joo et al 2008][research_joo_alali_2008]\] \[[Joo et al 2008][research_joo_ippolito_2008]\] \[[Joos and Pfife 2012][research_joos_pfife_2012]\] \[[Joos and Varga 1999][research_joos_varga_1999]\] \[[Joshi and Compton 1985][research_joshi_compton_1985]\] \[[Juang * and Chio 2005][research_juang_chio_2005]\] \[[Juang and Chien 2008][research_juang_chien_2008]\] \[[Jump and Padfield 2006][research_jump_padfield_2006]\] \[[Jung et al 2015][research_jung_lee_2015]\] \[[Jung et al 2025][research_jung_kim_2025]\] \[[Jung 2024][research_jung_2024]\] \[[Kai et al 2018][research_kai_anglade_2018]\] \[[Kariya et al 2020][research_kariya_tanaka_2020]\] \[[Karmarker and Sorensen 1976][research_karmarker_1976]\] \[[Kaufmann and McNally 1995][research_kaufmann_1995]\] \[[Kaufmann and Ncnally 1995][research_kaufmann_1995_b]\] \[[Kawamura et al 2022][research_kawamura_kannan_2022]\] \[[Kawamura et al 2023][research_kawamura_dolph_2023]\] \[[Kawamura et al][research_kawamura_nd]\] \[[Kawamura et al][research_kawamura_nd_b]\] \[[Kaynak 2010][research_kaynak_2010]\] \[[Ke et al 2014][research_ke_zhengzhong_2014]\] \[[Keidel et al 2019][research_keidel_fasel_2019]\] \[[Keipour et al 2022][research_keipour_2022]\] \[[Keke et al 2014][research_keke_qing_2014]\] \[[Kelly and Davis 1994][research_kelly_davis_1994]\] \[[Kelly and LaBERGE 1980][research_kelly_laberge_1980]\] \[[Kelly 1977][research_kelly_1977]\] \[[Kendall et al 2022][research_kendall_idris_2022]\] \[[Kendoul 2013][research_kendoul_2013]\] \[[Khan et al 2019][research_khan_rajput_2019]\] \[[Khanapuri and Rao 2017][research_khanapuri_rao_2017]\] \[[Khatwa and Helmreich 1999][research_khatwa_helmreich_1999]\] \[[Kim et al 2009][research_kim_kim_2009]\] \[[Kim et al 2012][research_kim_kim_2012]\] \[[Kim et al 2017][research_kim_woo_2017]\] \[[Kim and Tahk 2019][research_kim_tahk_2019]\] \[[Kineyko 1982][research_kineyko_1982]\] \[[Klochan et al 2017][research_klochan_alammouri_2017]\] \[[Kluever and Neal 2015][research_kluever_neal_2015]\] \[[Kluever 2004][research_kluever_2004]\] \[[Kluever 2007][research_kluever_2007_b]\] \[[Klyde and Liang 2009][research_klyde_liang_2009]\] \[[Kocamer et al 2022][research_kocamer_uzun_2022]\] \[[Kock and Fulton 1970][research_kock_1970]\] \[[Kolesnikov 2005][research_kolesnikov_2005]\] \[[Komatsuzaki et al 2016][research_komatsuzaki_doi_2016]\] \[[Kong et al 2009][research_kong_lee_2009]\] \[[Kongkaew et al 2022][research_kongkaew_ruchanurucks_2022]\] \[[Koo and Sastry 2003][research_koo_sastry_2003]\] \[[Korn and Doehler 2003][research_korn_doehler_2003]\] \[[Kozina 1976][research_kozina_1976]\] \[[Kramer and Busquets 2000][research_kramer_2000]\] \[[Kramer et al 2013][research_kramer_2013]\] \[[Kramer et al 2014][research_kramer_2014]\] \[[Krammer and Holzapfel 2023][research_krammer_holzapfel_2023]\] \[[Krammer et al 2021][research_krammer_scherer_2021]\] \[[Krammer et al 2022][research_krammer_rosenbauer_2022]\] \[[Krasuski and Wierzbicki 2018][research_krasuski_wierzbicki_2018]\] \[[Kriegsman and Tao 1974][research_kriegsman_tao_1974]\] \[[Kubo and Suzuki 2007][research_kubo_suzuki_2007]\] \[[Kubo and Suzuki 2008][research_kubo_suzuki_2008]\] \[[Kugler and Holzapfel 2017][research_kugler_holzapfel_2017]\] \[[Kugler and Holzapfel 2017][research_kugler_holzapfel_2017_b]\] \[[Kumar et al 2007][research_kumar_shanmugam_2007]\] \[[Kumar et al 2022][research_kumar_deshpande_2022]\] \[[Kumar and Padhi 2024][research_kumar_padhi_2024]\] \[[Kumtepe et al 2022][research_kumtepe_pollack_2022]\] \[[Kurdel et al 2024][research_kurdel_gecejova_2024]\] \[[Kügler et al 2018][research_kugler_heller_2018]\] \[[Kügler et al 2019][research_kugler_rhein_2019_b]\] \[[Kügler et al 2019][research_kugler_rhein_2019]\] \[[Laili and Widayaka 2024][research_laili_widayaka_2024]\] \[[Lambregts 1981][research_lambregts_1981]\] \[[Lambregts 1982][research_lambregts_1982]\] \[[Lamp and Luckner 2015][research_lamp_luckner_2015]\] \[[Landing Sites 2008][research_landing_sites_2008]\] \[[Langelaan and Grande 2013][research_langelaan_grande_2013]\] \[[Lavergne et al 2005][research_lavergne_villaume_2005]\] \[[Law and McWhorter 1992][research_law_mcwhorter_1992]\] \[[Lawrence et al 2001][research_lawrence_selmon_2001]\] \[[Lebacqz and Chen 1977][research_lebacqz_1977]\] \[[Lee and Mesbahi 2017][research_lee_mesbahi_2017]\] \[[Lee et al 2008][research_lee_soon_2008]\] \[[Lee et al 2019][research_lee_chung_2019]\] \[[Lee et al 2020][research_lee_benedict_2020]\] \[[Lee et al 2021][research_lee_park_2021]\] \[[Lee and Park 2025][research_lee_park_2025]\] \[[Lei and Li 2012][research_lei_li_2012]\] \[[Lei et al 2021][research_lei_xiaogang_2021]\] \[[Lesonen et al 2020][research_lesonen_nazarenko_2020]\] \[[Li and Duan 2015][research_li_duan_2015]\] \[[Li and Hu 2018][research_li_hu_2018]\] \[[Li and Li 2010][research_li_li_2010]\] \[[Li et al 2012][research_li_yang_2012]\] \[[Li et al 2021][research_li_xiao_2021]\] \[[Li et al 2024][research_li_xu_2024]\] \[[Li et al 2024][research_li_zhai_2024]\] \[[Li et al 2024][research_li_zhai_2024_b]\] \[[Li et al 2025][research_li_bando_2025]\] \[[Li et al 2025][research_li_xiong_2025]\] \[[Li et al 2026][research_li_ji_2026]\] \[[Li 2017][research_li_2017]\] \[[Liang et al 2021][research_liang_chin_2021]\] \[[Lin et al 2020][research_lin_qi_2020]\] \[[Lin et al 2026][research_lin_tseng_2026]\] \[[Littell 2019][research_littell_2019]\] \[[Liu and Lee 2022][research_liu_lee_2022]\] \[[Liu et al 2011][research_liu_wang_2011]\] \[[Liu et al 2011][research_liu_li_2011]\] \[[Liu et al 2017][research_liu_zhang_2017]\] \[[Liu et al 2021][research_liu_zheng_2021]\] \[[Liu et al 2023][research_liu_wang_2023_b]\] \[[Liu et al 2024][research_liu_zhang_2024_b]\] \[[Liu et al 2024][research_liu_zhang_2024_c]\] \[[Liu Zhi and Wang Yong 2012][research_liuzhi_wangyong_2012]\] \[[Liu 2012][research_liu_2012]\] \[[Looye and Joos 2002][research_looye_joos_2002]\] \[[Looye et al 2001][research_looye_joos_2001]\] \[[Looye et al 2001][research_looye_willemsen_2001]\] \[[Looye et al 2002][research_looye_sancho_2002]\] \[[Lopez 1993][research_lopez_1993]\] \[[Loureiro et al 2019][research_loureiro_soares_2019]\] \[[Lu Keke et al 2016][research_lukeke_yujinyong_2016]\] \[[Lugo et al 2014][research_lugo_tolson_2014]\] \[[Lungu and Lungu 2015][research_lungu_lungu_2015]\] \[[Lungu and Lungu 2015][research_lungu_lungu_2015_b]\] \[[Lungu and Lungu 2018][research_lungu_lungu_2018]\] \[[Lungu et al 2011][research_lungu_lungu_2011]\] \[[Lungu 2017][research_lungu_2017]\] \[[Lv et al 2024][research_lv_fan_2024]\] \[[Lykken and Shah 1971][research_lykken_shah_1971]\] \[[Ma et al 2018][research_ma_guan_2018]\] \[[Ma et al 2025][research_ma_ding_2025]\] \[[Mackay et al 2016][research_mackay_ellingson_2016]\] \[[Mackinnon and Madden 1971][research_mackinnon_madden_1971]\] \[[MACKlNNON and Madden 1972][research_macklnnon_madden_1972]\] \[[Madden and Desai 1973][research_madden_desai_1973]\] \[[Mahoor et al 2010][research_mahoor_godzdanker_2010]\] \[[Maiuzzo 1970][research_maiuzzo_1970]\] \[[Makarenko et al 2017][research_makarenko_makarov_2017]\] \[[Malloy and Chang 1998][research_malloy_chang_1998]\] \[[Mani 2007][research_mani_2007]\] \[[Manjarrez et al 2018][research_manjarrez_davila_2018]\] \[[Marantos et al 2017][research_marantos_karras_2017]\] \[[Martorella et al 1981][research_martorella_kelly_1981]\] \[[Masafumi Morimoto et al 2007][research_masafumimorimoto_kenjiuchiyama_2007]\] \[[Matranga 1961][research_matranga_1961]\] \[[McCabe and DeMars 2018][research_mccabe_demars_2018]\] \[[McCabe et al 2017][research_mccabe_brown_2017]\] \[[McCafferty et al 2014][research_mccafferty_woodward_2014]\] \[[McGee et al 1981][research_mcgee_foster_1981]\] \[[McGee et al 1981][research_mcgee_paulkjr_1981]\] \[[McGee 1977][research_mcgee_1977]\] \[[McNally et al 1992][research_mcnally_warner_1992]\] \[[Mejias and Eng 2012][research_mejias_eng_2012]\] \[[Meng et al 2018][research_meng_he_2018]\] \[[Meng et al 2019][research_meng_wang_2019]\] \[[Meng et al 2022][research_meng_gao_2022]\] \[[Menon et al 2010][research_menon_vaddi_2010]\] \[[Merlin 2006][research_merlin_2006]\] \[[Metzger 1970][research_metzger_1970]\] \[[Meyer 1970][research_meyer_1970]\] \[[Meyerson 1990][research_meyerson_1990]\] \[[Mhenni et al 2016][research_mhenni_choley_2016]\] \[[Mi et al 2018][research_mi_lu_2018]\] \[[Miccio et al 2024][research_miccio_veneruso_2024]\] \[[Microwave scanning beam landing 1977][research_microwave_scanning_1977]\] \[[Miele et al 1987][research_miele_wang_1987]\] \[[Miele et al 1988][research_miele_wang_1988_b]\] \[[Miele et al 1988][research_miele_wang_1988]\] \[[Miller 1979][research_millerjr_1979]\] \[[Milner et al 2022][research_milner_macabiau_2022]\] \[[Miotto and Paduano 1995][research_miotto_paduano_1995]\] \[[Miotto and Paduano 1996][research_miotto_paduano_1996]\] \[[Misra et al 2022][research_misra_fraticellirivera_2022]\] \[[Mitchell and Hoh 1983][research_mitchell_hoh_1983]\] \[[Miyazawa et al 1993][research_miyazawa_ishikawa_1993]\] \[[Miyazawa et al 1996][research_miyazawa_ishikawa_1996]\] \[[Miyazawa et al 1998][research_miyazawa_motoda_1998]\] \[[Miyazawa et al 1999][research_miyazawa_motoda_1999]\] \[[Mohammadkarimi and Nobahari 2018][research_mohammadkarimi_nobahari_2018]\] \[[Mohan et al 2025][research_mohan_s_2025]\] \[[Moorhouse and Fielding 1998][research_moorhouse_fielding_1998]\] \[[Moorhouse 1991][research_moorhouse_1991]\] \[[Moreira et al 2022][research_moreira_gripp_2022]\] \[[Morello et al 1977][research_morello_1977]\] \[[Motoda et al 1999][research_motoda_miyazawa_1999]\] \[[Mu et al 2023][research_mu_zhang_2023]\] \[[Mulcare et al 1982][research_mulcare_ness_1982]\] \[[Mumm and Holzapfel 2017][research_mumm_holzapfel_2017]\] \[[Murali et al 2024][research_murali_moreno_2024]\] \[[Murray-Smith 1995][research_murraysmith_1995]\] \[[Nagarjuna and Suresh 2015][research_nagarjuna_suresh_2015]\] \[[Nagel 1983][research_nagel_1983]\] \[[Najson and Mease 2005][research_najson_mease_2005]\] \[[Narkiewicz and Zasuwa 2002][research_narkiewicz_2002]\] \[[Nastasi et al 1983][research_nastasi_martorella_1983]\] \[[Negre 1991][research_negre_1991]\] \[[Neri et al 2010][research_neri_macabiau_2010]\] \[[Newman and Bailey 1987][research_newman_bailey_1987]\] \[[Nguyen and Jacklin 2010][research_nguyen_jacklin_2010]\] \[[Nguyen et al 2018][research_nguyen_cao_2018]\] \[[Nguyen et al 2020][research_nguyen_kostiukov_2020]\] \[[Nguyen et al 2022][research_nguyen_2022]\] \[[Nho and Agarwal 1998][research_nho_agarwal_1998]\] \[[Ni et al 2026][research_ni_wei_2026]\] \[[Nogar 2020][research_nogar_2020]\] \[[Nonami et al 2010][research_nonami_kendoul_2010]\] \[[Nowak et al 2022][research_nowak_kopecki_2022]\] \[[Obye and Hakim 1984][research_obye_hakim_1984]\] \[[Oglesby 1975][research_oglesby_1975]\] \[[Ohara et al 2001][research_ohara_2001]\] \[[Ohno et al 1998][research_ohno_yamaguchi_1998]\] \[[Ohno et al 1999][research_ohno_yamaguchi_1999]\] \[[Oishi et al 2002][research_oishi_2002]\] \[[Okada 1994][research_okada_1994]\] \[[Olivares-Mendez et al 2013][research_olivaresmendez_mondragon_2013]\] \[[Osder 1970][research_osder_1970]\] \[[Oudin et al 2013][research_oudin_puyou_2013]\] \[[Packard et al 2009][research_packard_seiler_2009]\] \[[Paletta et al 2013][research_paletta_belardo_2013]\] \[[Paletta et al 2015][research_paletta_dmytriv_2015]\] \[[Paranjape 2023][research_paranjape_2023]\] \[[Park et al 2015][research_park_kim_2015]\] \[[Park et al 2025][research_park_yang_2025]\] \[[Park 2020][research_park_2020]\] \[[Parker and Templeman 1967][research_parker_templeman_1967]\] \[[Parkinson and Fitzgibbon 1989][research_parkinson_fitzgibbon_1989]\] \[[Parlini 1988][research_parlini_1988]\] \[[Parrish and Martin 1975][research_parrish_1975]\] \[[Pashilkar et al 2016][research_pashilkar_haijun_2016]\] \[[Patrick 1972][research_patrick_1972]\] \[[Peach et al 1980][research_peach_1980]\] \[[Peng et al 2025][research_peng_li_2025]\] \[[Perkasa et al 2024][research_perkasa_krisbudiman_2024]\] \[[Pessanha Santos et al 2023][research_pessanhasantos_lobo_2023]\] \[[Petrishchev 2018][research_petrishchev_2018]\] \[[Peña-Gamboa and Martinez-Torres 2026][research_penagamboa_martineztorres_2026]\] \[[Phatak and Lee 1985][research_phatak_1985]\] \[[Phillips et al 1983][research_phillips_wilson_1983]\] \[[Pines and Hueschen 1978][research_pines_hueschen_1978]\] \[[Plinge 2003][research_plinge_2003]\] \[[Pogosyan and Vereikin 2020][research_pogosyan_vereikin_2020]\] \[[Poritzky 1970][research_poritzky_1970]\] \[[Powell 1959][research_powell_1959]\] \[[Powell 1960][research_powell_1960]\] \[[Powers 1984][research_powers_1984]\] \[[Powers 1986][research_powers_1986]\] \[[Prachand et al 2025][research_prachand_rakshith_2025]\] \[[Prasad et al 2018][research_prasad_comandur_2018]\] \[[Prilliman and Slingerland 1966][research_prilliman_1966]\] \[[Pruin 1970][research_pruin_1970]\] \[[Pérez et al 2022][research_perez_theodoulis_2022]\] \[[Qayyum et al 2017][research_qayyum_bhatti_2017]\] \[[Qi et al 2018][research_qi_zhao_2018]\] \[[Qian and Zhai 2012][research_qian_zhai_2012]\] \[[Radforth 1987][research_radforth_1987]\] \[[Raja 2011][research_raja_2011]\] \[[Rajawana and Smithmaitrie 2020][research_rajawana_smithmaitrie_2020]\] \[[Rang et al 1979][research_rang_gutmann_1979]\] \[[Rao et al 2001][research_rao_sarma_2001]\] \[[Rashmi Koushik et al 2020][research_rashmikoushiketal_2020]\] \[[Recker et al 2018][research_recker_gribble_2018]\] \[[Rector and Hattendorf 1967][research_rector_hattendorf_1967]\] \[[Reed-Mohn 2000][research_reedmohn_2000]\] \[[Rithirun and Sooraksa 2013][research_rithirun_sooraksa_2013]\] \[[Robaglia et al 2018][research_robaglia_libine_2018]\] \[[Robertson 2017][research_robertson_2017]\] \[[Romere et al 1978][research_romere_eichblatt_1978]\] \[[Romere et al 1979][research_romere_eichblatt_1979]\] \[[Roshini and Subba Reddy 2023][research_roshini_subbareddy_2023]\] \[[Rosner et al 2018][research_rosner_peszor_2018]\] \[[Rouwhorst 2001][research_rouwhorst_2001]\] \[[Roux et al 2012][research_roux_mantini_2012]\] \[[Ruping et al 2021][research_ruping_xin_2021]\] \[[Rutishauser et al 2019][research_rutishauser_moore_2019]\] \[[Rutishauser et al 2022][research_rutishauser_mendeck_2022]\] \[[S. Hameed and G. R 2021][research_shameed_gr_2021]\] \[[Sachs and Moeller 1995][research_sachs_moeller_1995]\] \[[Saghafi and Esmailifar 2009][research_saghafi_esmailifar_2009]\] \[[Sagirov et al 2025][research_sagirov_solovyov_2025]\] \[[Saiki et al 2009][research_saiki_fukao_2009]\] \[[Salt 1995][research_salt_1995]\] \[[Sani and Karimian 2017][research_sani_karimian_2017]\] \[[Santos et al 2019][research_santos_lobo_2019]\] \[[Sanuki 1965][research_sanuki_1965]\] \[[Saripalli et al 2003][research_saripalli_montgomery_2003]\] \[[Saripalli 2009][research_saripalli_2009]\] \[[Sarrafian 1984][research_sarrafian_1984]\] \[[Satkunanathan and Murphy 1998][research_satkunanathan_murphy_1998]\] \[[Sato and Muraoka 2013][research_sato_muraoka_2013]\] \[[Scanlon 1987][research_scanlon_1987]\] \[[Schaeffer 1983][research_schaeffer_1983]\] \[[Schmidt 1985][research_schmidt_1985]\] \[[Schmitt and Burchett 2004][research_schmitt_burchett_2004]\] \[[Schroer 2003][research_schroer_2003]\] \[[Schumann et al 2009][research_schumann_liu_2009]\] \[[Sedlmair et al 2019][research_sedlmair_theis_2019]\] \[[Sedlmair et al 2022][research_sedlmair_theis_2022]\] \[[Setterfield et al 2021][research_setterfield_hewitt_2021]\] \[[Setterfield et al 2022][research_setterfield_hewitt_2022]\] \[[Shah et al 1972][research_shah_gevaert_1972]\] \[[Shakarian 1983][research_shakarian_1983]\] \[[Shakernia et al 1999][research_shakernia_ma_1999]\] \[[Shang et al 2022][research_shang_li_2022]\] \[[Shao et al 2018][research_shao_gu_2018]\] \[[Sharma and Hablani 2014][research_sharma_hablani_2014]\] \[[Shen and Chen 2025][research_shen_chen_2025]\] \[[Shen et al 2025][research_shen_zhang_2025]\] \[[Sheng et al 2010][research_sheng_mian_2010]\] \[[Sherry et al 2018][research_sherry_shortle_2018]\] \[[Shue and Agarwal 1999][research_shue_agarwal_1999]\] \[[Shuttle autoland support program 1976][research_shuttle_autoland_1976]\] \[[Shweyk et al 2012][research_shweyk_hyde_2012]\] \[[Silva et al 2014][research_silva_mendonca_2014]\] \[[Silva et al 2019][research_silva_fontes_2019]\] \[[Sim et al 1994][research_sim_murray_1994]\] \[[Siwen et al 2022][research_siwen_feng_2022]\] \[[Slayton 1977][research_slayton_1977]\] \[[Smitchens and Huber 1975][research_smitchens_huber_1975]\] \[[Smith][research_smith_nd]\] \[[Smith 1981][research_smith_1981]\] \[[Smith and Meyer 1981][research_smith_meyer_1981]\] \[[Smith et al 1974][research_smith_1974]\] \[[Snyder et al 1992][research_snyder_schipper_1992]\] \[[Song et al 2019][research_song_zhang_2019]\] \[[Song et al 2023][research_song_zhang_2023]\] \[[Song et al 2023][research_song_wang_2023_b]\] \[[Sorensen and Karmarkar 1977][research_sorensen_1977]\] \[[Space Shuttle Program Orbiter 1977][research_space_shuttle_1977]\] \[[Steer 2004][research_steer_2004]\] \[[Steinberg 1992][research_steinberg_1992]\] \[[Steiner and Brady 2014][research_steiner_brady_2014]\] \[[Stevens 1985][research_stevens_1985]\] \[[Stich 2012][research_stich_2012]\] \[[Streb 1972][research_strebjr_1972]\] \[[Subrahmanyam 1994][research_subrahmanyam_1994]\] \[[Subrahmanyam 1995][research_subrahmanyam_1995]\] \[[Subrata 2017][research_subrata_2017]\] \[[Sun et al 2020][research_sun_shi_2020]\] \[[Sun et al 2023][research_sun_wu_2023]\] \[[Sun and Zhao 2024][research_sun_zhao_2024]\] \[[Suzuki 2013][research_suzuki_2013]\] \[[Ruxton-davies and Powell 1970][research_truxtondavies_powell_1970]\] \[[Tadema and Theunissen 2007][research_tadema_theunissen_2007]\] \[[Tadema and Theunissen 2008][research_tadema_theunissen_2008]\] \[[Takahashi et al 2018][research_takahashi_goerzen_2018]\] \[[Takahashi 1993][research_takahashi_1993]\] \[[Tan][research_tan_nd]\] \[[Tang et al 2014][research_tang_chen_2014]\] \[[Tate 1974][research_tate_1974]\] \[[Tate 1975][research_tate_1975]\] \[[Teper et al 1981][research_teper_1981]\] \[[Thibodeaux 1977][research_thibodeaux_1977]\] \[[Thompson 1965][research_thompson_1965]\] \[[Tian et al 2022][research_tian_yu_2022]\] \[[Tian et al 2024][research_tian_yu_2024]\] \[[Tischler 2018][research_tischler_2018]\] \[[Titov et al 2025][research_titov_parnenkov_2025]\] \[[Tomita and Fujiwara 2021][research_tomita_fujiwara_2021]\] \[[Trifonov et al 2024][research_trifonov_shelkov_2024]\] \[[Trittler et al 2016][research_trittler_rothermel_2016]\] \[[Trusfus and Abdullin 2021][research_trusfus_abdullin_2021]\] \[[Tsai 2008][research_tsai_2008]\] \[[Tseng et al 2013][research_tseng_lou_2013]\] \[[Tsikalas and Dyer 1982][research_tsikalas_1982_b]\] \[[Tsikalas 1982][research_tsikalas_1982]\] \[[Tsitses et al 2024][research_tsitses_zacharia_2024]\] \[[Tsoukalas et al 2026][research_tsoukalas_unlu_2026]\] \[[Tupitsin and Stepanenko 2020][research_tupitsin_stepanenko_2020]\] \[[Tweedale and Gonano 2014][research_tweedale_gonano_2014]\] \[[Ulukır et al 2025][research_ulukir_dursun_2025]\] \[[Ulybyshev 2010][research_ulybyshev_2010]\] \[[Urnes and Hess 1983][research_urnes_hess_1983]\] \[[Urnes and Hess 1985][research_urnes_hess_1985]\] \[[Urnes et al 1979][research_urnes_hess_1979]\] \[[Utterstrom and Kestek 1965][research_utterstrom_kestek_1965]\] \[[Uybarreta et al 2025][research_uybarreta_grant_2025]\] \[[Vaispacher et al 2025][research_vaispacher_baranek_2025]\] \[[Vallot et al 1991][research_vallot_snyder_1991]\] \[[Van Graas et al 1994][research_vangraas_diggle_1994]\] \[[Veneruso et al 2024][research_veneruso_miccio_2024]\] \[[Venkateswara Rao and Go 2014][research_venkateswararao_go_2014]\] \[[Venugopalan et al 2012][research_venugopalan_taher_2012]\] \[[Verma 1991][research_verma_1991]\] \[[Videmsek and de Haag 2020][research_videmsek_dehaag_2020]\] \[[Volkov et al 2022][research_volkov_komar_2022]\] \[[Wagner and Valasek 2006][research_wagner_valasek_2006]\] \[[Wagner and Valasek 2007][research_wagner_valasek_2007]\] \[[Waitman et al 2019][research_waitman_marcos_2019]\] \[[Walker 1981][research_walker_1981]\] \[[Walker 1960][research_walker_1960]\] \[[Wan et al 2023][research_wan_pan_2023]\] \[[Wang and Cui 2018][research_wang_cui_2018]\] \[[Wang and Mou 2025][research_wang_mou_2025]\] \[[Wang et al 2006][research_wang_peng_2006]\] \[[Wang et al 2016][research_wang_chen_2016]\] \[[Wang et al 2016][research_wang_lu_2016]\] \[[Wang et al 2017][research_wang_zhang_2017]\] \[[Wang et al 2017][research_wang_lu_2017]\] \[[Wang et al 2018][research_wang_li_2018]\] \[[Wang et al 2019][research_wang_zhang_2019]\] \[[Wang et al 2019][research_wang_wu_2019]\] \[[Wang et al 2022][research_wang_lin_2022]\] \[[Wang et al 2022][research_wang_gong_2022]\] \[[Wang et al 2022][research_wang_jiang_2022]\] \[[Wang et al 2022][research_wang_bi_2022]\] \[[Wang et al 2022][research_wang_zhao_2022]\] \[[Wang et al 2023][research_wang_ma_2023]\] \[[Wang et al 2023][research_wang_tang_2023]\] \[[Wang et al 2023][research_wang_yuan_2023]\] \[[Wang et al 2023][research_wang_jiang_2023]\] \[[Wang et al 2023][research_wang_li_2023_b]\] \[[Wang et al 2025][research_wang_yang_2025]\] \[[Wang and Wang 2013][research_wang_wang_2013]\] \[[Wang and Zou 2021][research_wang_zou_2021]\] \[[Wang Lu et al 2016][research_wanglu_yaoweili_2016]\] \[[Warner 1981][research_warner_1981]\] \[[Watson et al 1986][research_watson_hardy_1986]\] \[[Wei et al 2018][research_wei_xu_2018]\] \[[Wei and Wang 2025][research_wei_wang_2025]\] \[[Wei et al 2024][research_wei_2024]\] \[[Weingarten and Chalk 1982][research_weingarten_chalk_1982]\] \[[Welch 1993][research_welch_1993]\] \[[Wenzel et al 2010][research_wenzel_masselli_2010]\] \[[Widnall and Morth 1972][research_widnall_morth_1972]\] \[[Williams et al 2000][research_williams_davis_2000]\] \[[Williams 1947][research_williams_1947]\] \[[Wilz and Johnson 1975][research_wilz_johnson_1975]\] \[[Wisely 2002][research_wisely_2002]\] \[[Woestemeyer 1964][research_woestemeyer_1964]\] \[[Wolf et al 2012][research_wolf_casoliva_2012]\] \[[Woloshen 1974][research_woloshen_1974]\] \[[Wood 1972][research_wood_1972]\] \[[Woodbury and Valasek 2015][research_woodbury_valasek_2015]\] \[[Woodbury and Valasek 2016][research_woodbury_valasek_2016]\] \[[Wu et al 2018][research_wu_zhang_2018]\] \[[Wu et al 2018][research_wu_shi_2018]\] \[[Wu et al 2023][research_wu_luo_2023]\] \[[Wu et al 2026][research_wu_zhu_2026]\] \[[Wu et al 2024][research_wu_2024_b]\] \[[Wu 2024][research_wu_2024]\] \[[Wygle 1965][research_wygle_1965]\] \[[Xargay et al 2010][research_xargay_hovakimyan_2010]\] \[[Xia et al 2025][research_xia_hu_2025]\] \[[Xiao 2026][research_xiao_2026]\] \[[Xie 2024][research_xie_2024]\] \[[Xu et al 2012][research_xu_xia_2012]\] \[[Xu et al 2017][research_xu_zhao_2017]\] \[[Xu et al 2020][research_xu_hu_2020]\] \[[Xu and Wang 2016][research_xu_wang_2016]\] \[[Xu 2025][research_xu_2025]\] \[[Yakimenko and Altmann 2015][research_yakimenko_altmann_2015]\] \[[Yan et al 2016][research_yan_tan_2016]\] \[[Yanagihara et al 1999][research_yanagihara_shigemi_1999]\] \[[Yang and Liu 2021][research_yang_liu_2021]\] \[[Yang et al 2024][research_yang_hao_2024]\] \[[Yang et al 2026][research_yang_yang_2026]\] \[[Yang and Wang 2013][research_yang_wang_2013]\] \[[Yang 2025][research_yang_2025]\] \[[Yao et al 2025][research_yao_li_2025]\] \[[Yao et al 2025][research_yao_li_2025_b]\] \[[Yao et al 2025][research_yao_kan_2025]\] \[[Yao and Wu 2019][research_yao_wu_2019]\] \[[Yelin Zhang et al 2016][research_yelinzhang_yangzhuwang_2016]\] \[[Yi et al 2011][research_yi_2011]\] \[[Yilmaz et al 2019][research_yilmaz_warren_2019]\] \[[Yong Jiang et al 2006][research_yongjiang_jiecao_2006]\] \[[Yu et al 2017][research_yu_wang_2017]\] \[[Yu et al 2017][research_yu_cai_2017]\] \[[Yu et al 2020][research_yu_yang_2020]\] \[[Yu et al 2024][research_yu_zhang_2024]\] \[[Yuan et al 2006][research_yuan_gong_2006]\] \[[Yuan et al 2019][research_yuan_sun_2019]\] \[[Yuan et al 2022][research_yuan_xu_2022]\] \[[Yuta Akai et al 2007][research_yutaakai_kenjiuchiyama_2007]\] \[[Zahn et al][research_zahn_nd]\] \[[Zavalishin et al 2021][research_zavalishin_zatuchny_2021]\] \[[Zhang and Jia 2013][research_zhang_jia_2013]\] \[[Zhang et al 2005][research_zhang_gray_2005]\] \[[Zhang et al 2007][research_zhang_cai_2007]\] \[[Zhang et al 2016][research_zhang_liu_2016]\] \[[Zhang et al 2019][research_zhang_zhai_2019_b]\] \[[Zhang et al 2019][research_zhang_zhai_2019]\] \[[Zhang et al 2021][research_zhang_li_2021]\] \[[Zhang et al 2021][research_zhang_hu_2021]\] \[[Zhang et al 2022][research_zhang_selezneva_2022]\] \[[Zhang et al 2023][research_zhang_wang_2023]\] \[[Zhang et al 2025][research_zhang_ma_2025]\] \[[Zhang and Wang 2013][research_zhang_wang_2013]\] \[[Zhang and Zhang 2011][research_zhang_zhang_2011]\] \[[Zhang 2024][research_zhang_2024]\] \[[Zhao et al 2013][research_zhao_yang_2013]\] \[[Zhao et al 2013][research_zhao_pei_2013]\] \[[Zhao et al 2014][research_zhao_sheng_2014]\] \[[Zhao and Pei 2012][research_zhao_pei_2012]\] \[[Zhen et al 2018][research_zhen_jiang_2018]\] \[[Zhen et al 2019][research_zhen_peng_2019]\] \[[Zheng et al 2017][research_zheng_jin_2017]\] \[[Zheng and Wang 2019][research_zheng_wang_2019]\] \[[Zhihui Zheng et al 2016][research_zhihuizheng_haipingwei_2016]\] \[[Zhimin and Guanxin 2008][research_zhimin_guanxin_2008]\] \[[Zhishuai et al 2023][research_zhishuai_di_2023]\] \[[Zhou and Feng 2023][research_zhou_feng_2023]\] \[[Zhou and Neusypin 2023][research_zhou_neusypin_2023]\] \[[Zhou et al 2020][research_zhou_zheng_2020]\] \[[Zhou et al 2020][research_zhou_ohashi_2020]\] \[[Zhou et al 2023][research_zhou_li_2023]\] \[[Zhou et al 2023][research_zhou_jin_2023]\] \[[Zhou et al 2024][research_zhou_yang_2024]\] \[[Zhou and Takaba 2019][research_zhou_takaba_2019]\] \[[Zhou 2026][research_zhou_2026]\] \[[Zhu et al 2021][research_zhu_liu_2021]\] \[[Zhu et al 2025][research_zhu_lee_2025]\] \[[Zhu and Yang 2020][research_zhu_yang_2020]\] \[[Zhu Qi-dan et al 2009][research_zhuqidan_wangtong_2009_b]\] \[[Zhu Qi-dan et al 2009][research_zhuqidan_wangtong_2009]\] \[[Zhu 2024][research_zhu_2024]\] \[[Zou et al 2025][research_zou_chen_2025]\] \[[Çeti̇n et al 2024][research_cetin_aygun_2024]\] \[[Бабич and others, 2017, Features of landing approach for aircraft in automatic and yoke control modes in conditions of vertical wind shear][research_features_of_landing_2017]\] \[[Філяшкін and Мельников, 2012, Automatic landing control plane based on the predictive model algorithm][research_automatic_landing_control_2012]\]

### Planetary and Lunar Precision Landing

**Precision landing on the Moon, Mars, asteroids and comets is the autonomous landing problem without a runway.** The cluster gathers powered descent guidance, terrain-relative navigation and hazard avoidance for landers.

Of its 138 titles, 48 name vision, optical, crater, terrain, lidar or hazard sensing, and 1 names satellite navigation. **The X-40A's reliance on satellite and inertial navigation has almost no counterpart there.**

**138 records.** \[[1962, Terminal Guidance System For Soft Lunar Landing][research_terminal_guidance_1962]\] \[[1964, A Minimum Fuel Vertical Touchdown Lunar Landing Guidance Technique][research_a_minimum_1964]\] \[[Acikmese and Ploen 2005][research_acikmese_ploen_2005]\] \[[Acikmese and Ploen 2007][research_acikmese_ploen_2007]\] \[[Ali et al][research_ali_nd]\] \[[Ali et al][research_ali_nd_b]\] \[[Amzajerdian et al 2016][research_amzajerdian_2016]\] \[[Andert et al 2015][research_andert_ammann_2015]\] \[[Bailey et al 2025][research_bailey_2025]\] \[[Banerjee and Padhi 2017][research_banerjee_padhi_2017]\] \[[Banerjee and Padhi 2018][research_banerjee_padhi_2018]\] \[[Bigot and Murdoch 2025][research_bigot_2025]\] \[[Bishop et al 2016][research_bishop_crain_2016]\] \[[Blackmore et al 2010][research_blackmore_acikmese_2010]\] \[[Bonetti et al 2013][research_bonetti_dezaiacomo_2013]\] \[[Brandon M. Jones][research_jones_nd]\] \[[Burkhart et al 2013][research_burkhart_2013]\] \[[Chen and Wang 2023][research_chen_wang_2023]\] \[[Chen et al 2013][research_chen_2013]\] \[[Chen et al 2013][research_chen_2013_b]\] \[[Cohanim and Collins 2009][research_cohanim_2009]\] \[[Collicott and Woffinden 2021][research_collicott_woffinden_2021]\] \[[Cork and Moore 1967][research_cork_moore_1967]\] \[[Crain et al 2016][research_crain_2016]\] \[[Cruz et al][research_cruz_nd]\] \[[D'Souza and D'Souza 1997][research_dsouza_dsouza_1997]\] \[[Dan Tuckness 1994][research_dantuckness_1994]\] \[[de Lafontaine et al 2006][research_delafontaine_levesque_2006]\] \[[de Lafontaine 1992][research_delafontaine_1992]\] \[[Delaune et al 2010][research_delaune_derosa_2010]\] \[[Delaune et al 2016][research_delaune_lebesnerais_2016]\] \[[Du and Zhang 2020][research_du_zhang_2020]\] \[[Dubois-Matra and Bishop 2004][research_duboismatra_bishop_2004]\] \[[Ely et al 2010][research_ely_heyne_2010]\] \[[Federici et al 2026][research_federici_benedikter_2026]\] \[[Feld et al][research_feld_nd]\] \[[Feng et al 2009][research_feng_cui_2009]\] \[[Feng and Wasynczuk 1967][research_feng_wasynczuk_1967]\] \[[Friia et al 2023][research_friia_mahajan_2023]\] \[[Furfaro et al 2013][research_furfaro_cersosimo_2013]\] \[[Galassi 2011][research_galassi_2011]\] \[[Gao et al 2010][research_gao_cui_2010]\] \[[Gaskell 2005][research_gaskell_2005]\] \[[Gee et al 2014][research_gee_2014]\] \[[Gerth and Mooij 2014][research_gerth_mooij_2014]\] \[[Gleichman et al 1991][research_gleichman_1991]\] \[[Greenhalgh et al 2026][research_greenhalgh_2026]\] \[[Hall et al 1963][research_hall_dietrich_1963]\] \[[Hamel et al 2025][research_hamel_garant_2025]\] \[[Hammock and Jackson 1963][research_hammock_1963]\] \[[Hart and Devolites 2014][research_hart_2014]\] \[[Henderson 1963][research_henderson_1963]\] \[[Horvath et al 2002][research_horvath_2002]\] \[[Hu et al 2021][research_hu_huang_2021]\] \[[Hu et al 2024][research_hu_jing_2024]\] \[[Huang and Wang 2007][research_huang_wang_2007]\] \[[Izzo et al 2011][research_izzo_weiss_2011]\] \[[Jia et al 2020][research_jia_2020]\] \[[Jiaxing et al 2025][research_jiaxing_dayi_2025]\] \[[Johnson and Ivanov 2011][research_johnson_2011]\] \[[Johnson et al 2020][research_johnson_lu_2020]\] \[[Kluever 2008][research_kluever_2008]\] \[[Klumpp 1966][research_klumpp_1966]\] \[[Konstantinidis and Förstner 2020][research_konstantinidis_forstner_2020]\] \[[Kubota et al 2003][research_kubota_hashimoto_2003]\] \[[Lee 2011][research_lee_2011]\] \[[Li and Cui 2011][research_li_cui_2011]\] \[[Li et al 2006][research_li_cui_2006]\] \[[Li et al 2007][research_li_cui_2007]\] \[[Li et al 2024][research_li_wang_2024]\] \[[Li 2008][research_li_2008]\] \[[Likhachev et al 2014][research_likhachev_sikharulidze_2014]\] \[[Lin and Cui 2022][research_lin_cui_2022]\] \[[Lugo et al 2022][research_lugo_dwyercianciolo_2022]\] \[[Lévesque and de Lafontaine 2006][research_levesque_delafontaine_2006]\] \[[Maass et al 2020][research_maass_woicke_2020]\] \[[Mammarella et al 2011][research_mammarella_rodrigalvarez_2011]\] \[[Mauritz et al 1997][research_mauritz_1997]\] \[[Mikrin et al 2020][research_mikrin_orlovskii_2020]\] \[[Miso et al 1999][research_miso_1999]\] \[[Mohiuddin et al 2025][research_mohiuddin_2025]\] \[[Moholkar et al 2024][research_moholkar_2024]\] \[[Mourikis et al 2007][research_mourikis_trawny_2007]\] \[[Mukhopadhyay 1969][research_mukhopadhyay_1969]\] \[[Muraca and King 1975][research_muraca_1975]\] \[[Park et al 2019][research_park_jung_2019]\] \[[Parracino et al 2024][research_parracino_ceresoli_2024]\] \[[Polsgrove et al 2018][research_polsgrove_2018]\] \[[Polsgrove et al 2018][research_polsgrove_2018_b]\] \[[Reiley et al 1991][research_reiley_1991]\] \[[Ribarich 1967][research_ribarich_1967]\] \[[Rimer and Sperling 1965][research_rimer_sperling_1965]\] \[[Rimer and Sperling 1966][research_rimer_sperling_1966]\] \[[Mathavaraj and Padhi 2017][research_s_padhi_2017]\] \[[Sabiron et al 2013][research_sabiron_chavent_2013]\] \[[Sachan and Padhi 2016][research_sachan_padhi_2016]\] \[[Schiavone et al 2012][research_schiavone_2012]\] \[[Scorsoglio et al 2025][research_scorsoglio_gaudet_2025]\] \[[Scorsoglio et al 2022][research_scorsoglio_2022]\] \[[Serrano 2006][research_serrano_2006]\] \[[Shuang and Liu 2009][research_shuang_liu_2009]\] \[[Shuang et al 2005][research_shuang_hutao_2005]\] \[[Shuang and Pingyuan 2008][research_shuang_2008]\] \[[Shuang and Pingyuan 2006][research_shuang_pingyuan_2006]\] \[[Smith and Peng 1996][research_smith_1996]\] \[[Steinfeldt et al 2008][research_steinfeldt_grant_2008]\] \[[Sunday][research_sunday_nd]\] \[[Szmuk et al 2017][research_szmuk_eren_2017]\] \[[Thompson 2024][research_thompson_2024]\] \[[Tian et al 2018][research_tian_yu_2018]\] \[[Tomita and Ho 2025][research_tomita_2025]\] \[[Tomita and Ho 2025][research_tomita_ho_2025]\] \[[Tomita et al 2022][research_tomita_2022]\] \[[Topcu et al 2005][research_topcu_casoliva_2005]\] \[[Trawny et al 2015][research_trawny_2015]\] \[[Tsuyuki et al 2005][research_tsuyuki_2005]\] \[[Tu et al 1998][research_tu_munir_1998]\] \[[Ueno and Yamaguchi 1999][research_ueno_yamaguchi_1999]\] \[[Utkarsh R. Moholkar 2025][research_moholkar_2025]\] \[[Vaquero et al 2022][research_vaquero_kennedy_2022]\] \[[Watson-Morgan et al][research_watson_morgan_nd]\] \[[Weismuller et al 2007][research_weismuller_caballero_2007]\] \[[Wibben et al 2012][research_wibben_furfaro_2012]\] \[[Woestemeyer 1967][research_woestemeyer_1967]\] \[[Woicke and Krüger 2023][research_woicke_kruger_2023]\] \[[Woicke and Mooij 2017][research_woicke_mooij_2017]\] \[[Wolf et al 2011][research_wolf_2011]\] \[[Xiangyu et al 2004][research_xiangyu_hutao_2004]\] \[[Xu et al 2017][research_xu_wang_2017]\] \[[Xu et al 2017][research_xu_wang_2017_b]\] \[[Xu et al 2021][research_xu_huang_2021]\] \[[Xu Xibao et al 2016][research_xuxibao_guojifeng_2016]\] \[[Yan and Hexi 2025][research_yan_hexi_2025]\] \[[Yu et al 2015][research_yu_xu_2015]\] \[[Yu et al 2018][research_yu_li_2018]\] \[[Yu et al 2019][research_yu_li_2019]\] \[[Yuan and He 2025][research_yuan_he_2025]\] \[[Yuan et al 2018][research_yuan_zhu_2018]\]

### Lifting Bodies and the Unpowered Approach

**A vehicle with a lift to drag ratio near two arrives steeply and has one attempt.** This cluster covers lifting-body aerodynamics, unpowered approach technique, terminal area energy management and the flare, which together describe the last four nautical miles that the X-40A actually flew.

**352 records.** \[[1981, Optimal Glide of Reentry Vehicles][research_optimal_glide_1981]\] \[[1985, Low Lift-to-Drag Aerobrake Heat-Transfer Test at Mach 10][research_low_lift_to_drag_1985]\] \[[1994, Slender Lifting Body Axial Force Prediction in Hypersonic Rarefied Flow][research_slender_lifting_1994]\] \[[1995, Gliding and Unpowered Flights][research_gliding_and_1995]\] \[[2009, Robust Airspeed Estimation of an Unpowered Gliding Vehicle by Using Multiple Model Kalman Filters][research_robust_airspeed_2009]\] \[[2017, The Traditional Glide Path][research_the_traditional_2017]\] \[[2021, A Manageable Glide-path][research_a_manageable_2021]\] \[[2023, Mathematical model of the UAV landing approach system on the example of the course-glide path system][research_mathematical_model_2023]\] \[[Adams et al 1973][research_adams_johnc_1973]\] \[[Air Force Test Pilot School Edwards Afb Ca 1992][research_airforcetestpilotschooledwardsafbca_1992]\] \[[Aircraft Steady Gliding Longitudinal 2011][research_6_aircraft_2011]\] \[[Aircraft Steady Gliding Longitudinal 2011][research_aircraft_steady_2011]\] \[[Algorithms for Flexible Flight 2012][research_algorithms_flexible_2012]\] \[[Almosnino 2016][research_almosnino_2016]\] \[[Anderson et al 1967][research_anderson_schultz_1967]\] \[[Anoshin et al 2012][research_anoshin_bobylev_2012]\] \[[Aradag et al 2007][research_aradag_seidel_2007]\] \[[Badarudin Mohamad Badry et al 2013][research_badarudinmohamadbadry_lee_2013]\] \[[Bai et al 2014][research_bai_ren_2014]\] \[[Banks and Fisher 2006][research_banks_2006]\] \[[Baran et al 2014][research_baran_blanchard_2014]\] \[[Barret 1998][research_barret_1998]\] \[[Baumgartner and Elvin 1995][research_baumgartner_1995]\] \[[Bedrov et al 1966][research_bedrov_vadichin_1966]\] \[[Bergeron et al 2011][research_bergeron_tavan_2011]\] \[[Berthelot et al 2026][research_berthelot_craft_2026]\] \[[Binz et al 2017][research_binz_hartmann_2017]\] \[[Bobylev et al 2008][research_bobylev_dyadkin_2008]\] \[[Bohn et al 1970][research_bohn_1970]\] \[[Borodin 2001][research_borodin_2001]\] \[[Bugg and Sleeman 1967][research_bugg_1967]\] \[[Buhler and Linhart 1969][research_buhler_1969]\] \[[Bull and Foster 1974][research_bull_foster_1974]\] \[[Burchett 2004][research_burchett_2004]\] \[[Burkhardt et al 1999][research_burkhardt_graesslin_1999]\] \[[Calise and Bae 1987][research_calise_bae_1987]\] \[[Campos 1989][research_campos_1989]\] \[[Cao and Zhang 2015][research_cao_zhang_2015]\] \[[Carman 1980][research_carman_1980_c]\] \[[Carman and Montez 1980][research_carman_1980]\] \[[Carman and Montez 1980][research_carman_1980_b]\] \[[Chen et al 2020][research_chen_zhou_2020_b]\] \[[Chernyi and Gonor 1973][research_chernyi_gonor_1973]\] \[[Chin 1970][research_chin_1970]\] \[[Chu and Li 2017][research_chu_li_2017]\] \[[Clemmons 1971][research_clemmons_1971]\] \[[Cochrane and Graham 1971][research_cochrane_1971]\] \[[Croom and Fournier 1966][research_croom_1966]\] \[[Crouch 1999][research_crouch_1999]\] \[[D'Angelo et al 1999][research_dangelo_minisci_1999]\] \[[Dana and Gentry 1970][research_dana_1970]\] \[[Dana et al 1969][research_dana_1969]\] \[[Deng et al 2025][research_deng_xu_2025]\] \[[Di Campli Bayard de Volo and Di Pietro 2018][research_dicamplibayarddevolo_dipietro_2018]\] \[[Dillman et al 2020][research_dillman_slagle_2020]\] \[[Din et al 2020][research_din_janujua_2020]\] \[[Ding et al 2016][research_ding_guo_2016]\] \[[Dong et al 2023][research_dong_huang_2023]\] \[[Dong et al 2025][research_dong_zhao_2025]\] \[[Dragan and Stoica 1997][research_dragan_stoica_1997]\] \[[Durand and Wasicko 1967][research_durand_wasicko_1967]\] \[[Edwards and Foster 1973][research_edwards_1973]\] \[[Elias 1974][research_elias_1974]\] \[[Elliott 1968][research_elliott_1968]\] \[[Engel and Putnam 2025][research_engel_putnam_2025]\] \[[Enmi et al 2018][research_enmi_qian_2018]\] \[[Erwin 1990][research_erwin_1990]\] \[[Fang et al 2026][research_fang_chen_2026]\] \[[Fang et al 2018][research_fang_2018_b]\] \[[Fang et al 2019][research_fang_2019]\] \[[Farajollahi and Markazi 2010][research_farajollahi_markazi_2010]\] \[[Faulders et al 1967][research_faulders_lekawa_1967]\] \[[Feng et al 2025][research_feng_bai_2025]\] \[[Ferris and Kelly 1968][research_ferris_1968]\] \[[First Glide Flight of 1966][research_first_glide_1966]\] \[[Florence 1979][research_florence_1979]\] \[[Friz and Samareh 2020][research_friz_samareh_2020]\] \[[Fuhrmann 2003][research_fuhrmann_2003]\] \[[Galanis et al 1998][research_galanis_jennings_1998]\] \[[Gamble et al 1984][research_gamble_spratlin_1984]\] \[[Gamse and Mort 1966][research_gamse_1966]\] \[[Gao et al 2014][research_gao_li_2014]\] \[[Gao et al 2019][research_gao_cai_2019]\] \[[Gavrilovski et al 2011][research_gavrilovski_ward_2011]\] \[[Gentry et al 1966][research_gentry_1966]\] \[[Gentry 1968][research_gentry_1968]\] \[[Gong et al 2020][research_gong_guo_2020]\] \[[Grantham 2003][research_grantham_2003]\] \[[Grenestedt and Spletzer 2010][research_grenestedt_spletzer_2010]\] \[[Grewal et al 1976][research_grewal_schneider_1976]\] \[[Grodsky and Mandour 1967][research_grodsky_mandour_1967]\] \[[Grumondz et al 2012][research_grumondz_polishchuk_2012]\] \[[Guo and Fang 2022][research_guo_fang_2022]\] \[[Hall and Soares 2008][research_hall_soares_2008]\] \[[Han et al 2025][research_han_wang_2025]\] \[[Han and Xiong 2016][research_han_xiong_2016]\] \[[Hawthorne 1976][research_hawthorne_1976]\] \[[Hawthorne 1976][research_hawthorne_1976_b]\] \[[Hawthorne 1976][research_hawthorne_1976_c]\] \[[Hawthorne 1976][research_hawthorne_1976_d]\] \[[Hawthorne 1976][research_hawthorne_1976_e]\] \[[Hawthorne 1976][research_hawthorne_1976_f]\] \[[Hawthorne 1976][research_hawthorne_1976_g]\] \[[Hawthorne 1976][research_hawthorne_1976_h]\] \[[Hawthorne 1976][research_hawthorne_1976_i]\] \[[Hawthorne 1976][research_hawthorne_1976_j]\] \[[Hawthorne 1976][research_hawthorne_1976_k]\] \[[Hawthorne 1976][research_hawthorne_1976_l]\] \[[Hawthorne 1976][research_hawthorne_1976_m]\] \[[Hess 1972][research_hess_1972]\] \[[Hewes 1961][research_hewes_1961]\] \[[Hoag and Schofield 1970][research_hoag_1970]\] \[[Hollis and Hollingsworth 2012][research_hollis_hollingsworth_2012]\] \[[Holmes 1970][research_holmes_1970]\] \[[Holt et al 2016][research_holt_garry_2016]\] \[[Honda et al 2019][research_honda_tajima_2019]\] \[[Hook and Freeman 1989][research_hook_1989]\] \[[Horneman and Kluever 2004][research_horneman_kluever_2004]\] \[[Hu Wei-jun and Zhou Jun 2009][research_huweijun_zhoujun_2009]\] \[[Huang et al 2014][research_huang_zhang_2014]\] \[[Huang et al 2023][research_huang_deng_2023]\] \[[Huang et al 2024][research_huang_yu_2024]\] \[[Huang 1968][research_huang_1968]\] \[[Hugo and Lago 2022][research_hugo_lago_2022]\] \[[Hyde 2005][research_hyde_2005]\] \[[Iden 1959][research_iden_1959]\] \[[Jackson and Cruz 1992][research_jackson_1992]\] \[[Jackson et al 1991][research_jackson_1991]\] \[[Jackson et al 1993][research_jackson_1993]\] \[[Jackson et al 1993][research_jackson_rivers_1993_b]\] \[[Jackson and Rivers 1998][research_jackson_rivers_1998]\] \[[Jackson et al 1992][research_jackson_1992_b]\] \[[Jackson et al 1994][research_jackson_1994]\] \[[Jackson 1961][research_jackson_1961]\] \[[Jenkins et al 1968][research_jenkins_1968]\] \[[Ji et al 2023][research_ji_hua_2023]\] \[[Jiang and Yang 2014][research_jiang_yang_2014]\] \[[Johannesen et al 1985][research_johannesen_vinh_1985]\] \[[McTigue 1970][research_mctigue_1970]\] \[[Johnson 1949][research_johnson_1949]\] \[[Johnson et al 2018][research_johnson_cerimele_2018]\] \[[Kageyama and Hiraoka 2004][research_kageyama_hiraoka_2004]\] \[[Katz and Roglin 2000][research_katz_roglin_2000]\] \[[Kawato et al 2002][research_kawato_watanabe_2002]\] \[[Kawato et al 2003][research_kawato_watanabe_2003]\] \[[Kayton 1968][research_kayton_1968]\] \[[Kelly and McNulty 1963][research_kelly_1963]\] \[[Kempel 1971][research_kempel_1971]\] \[[Kempel and Manke 1974][research_kempel_1974]\] \[[Kempel and Painter 1994][research_kempel_painter_1994]\] \[[Kempel and Thompson 1971][research_kempel_1971_b]\] \[[Kempel et al 1975][research_kempel_1975]\] \[[Kempel et al 1994][research_kempel_1994]\] \[[Keskin 2026][research_keskin_2026]\] \[[Khattak et al 2023][research_khattak_chan_2023]\] \[[Khurana et al 2012][research_khurana_suzuki_2012]\] \[[Khurana and Suzuki 2013][research_khurana_suzuki_2013]\] \[[Khurana and Suzuki 2014][research_khurana_suzuki_2014]\] \[[Kim 2026][research_kim_2026]\] \[[Kock et al 1972][research_kock_1972]\] \[[Kock and Painter 1968][research_kock_1968]\] \[[Kock and Painter 1969][research_kock_1969]\] \[[Korzun et al 2020][research_korzun_tang_2020]\] \[[Kotfilia and Painter 1969][research_kotfilia_painter_1969]\] \[[Kurniawan et al 2022][research_kurniawan_stefanie_2022]\] \[[Kutluay et al 2009][research_kutluay_mahmutyazicioglu_2009]\] \[[La et al 1993][research_la_shivananda_1993]\] \[[Lan et al 2020][research_lan_xu_2020]\] \[[Lan et al 2021][research_lan_tan_2021]\] \[[Lancaster 1977][research_lancaster_1977]\] \[[Lapygin and Yakunina 2009][research_lapygin_yakunina_2009]\] \[[Lawrance and Sukkarieh 2009][research_lawrance_sukkarieh_2009]\] \[[Layton 1970][research_layton_1970]\] \[[Layton and McTigue 1969][research_layton_1969]\] \[[Leng et al 2023][research_leng_wang_2023]\] \[[Leparoux et al 2022][research_leparoux_herisse_2022]\] \[[Levin 1968][research_levin_1968]\] \[[Li et al 2018][research_li_xiao_2018]\] \[[Li et al 2022][research_li_shi_2022]\] \[[Li et al 2024][research_li_chang_2024]\] \[[Li et al 2025][research_li_pei_2025]\] \[[Liang et al 2014][research_liang_li_2014]\] \[[Lin et al 2020][research_lin_meghdadhasheminasab_2020]\] \[[Lina and Whitten 1968][research_lina_whitten_1968]\] \[[Ling 2017][research_ling_2017]\] \[[Liu et al 2006][research_liu_zhou_2006]\] \[[Liu et al 2014][research_liu_ding_2014]\] \[[Liu et al 2024][research_liu_hu_2024]\] \[[Liu et al 2024][research_liu_zhang_2024]\] \[[Luo and Li 2011][research_luo_li_2011]\] \[[Lusty and Miele 1966][research_lusty_miele_1966]\] \[[M2-F2 Lifting Body Accident 1967][research_m2_f2_1967]\] \[[Mahmood et al 2022][research_mahmood_rehman_2022]\] \[[Mahmood and ur Rehman 2023][research_mahmood_urrehman_2023]\] \[[Mahmood 2025][research_mahmood_2025]\] \[[Mahrous et al 2026][research_mahrous_khalil_2026]\] \[[Maikapar 1993][research_maikapar_1993]\] \[[Manke et al 1970][research_manke_1970]\] \[[Marcum 1998][research_marcum_1998]\] \[[Marcum 1998][research_marcum_1998_b]\] \[[Marcum 2000][research_marcum_2000]\] \[[Matranga and Armstrong 1959][research_matranga_1959b]\] \[[Matranga and Menard 1959][research_matranga_1959a]\] \[[Mayanna et al 2006][research_mayanna_grimm_2006]\] \[[Mbagwu et al 2023][research_mbagwu_dalle_2023]\] \[[McFarland 1981][research_mcfarland_1981]\] \[[McFARLAND 1991][research_mcfarland_1991]\] \[[McFarland 1994][research_mcfarland_1994]\] \[[Merlin 2014][research_merlin_2014]\] \[[Miao et al 2026][research_miao_wang_2026]\] \[[Misra and Bai 2019][research_misra_bai_2019]\] \[[Mohamed et al 2022][research_mohamed_safwat_2022]\] \[[Mooij 2024][research_mooij_2024]\] \[[Moore 1991][research_moore_1991]\] \[[Moore 2013][research_moore_2013]\] \[[Morio et al 2007][research_morio_falcoz_2007]\] \[[Morio et al 2009][research_morio_cazaurang_2009]\] \[[Morio et al 2010][research_morio_cazaurang_2010]\] \[[Morth 1972][research_morth_1972]\] \[[Mu et al 2016][research_mu_yu_2016]\] \[[Mu et al 2018][research_mu_yu_2018]\] \[[Mu et al 2019][research_mu_yu_2019]\] \[[Munusamy et al 2022][research_munusamy_stephen_2022]\] \[[Murcia Piñeros et al 2022][research_murciapineros_vilhenademoraes_2022]\] \[[Naeseth 1970][research_naeseth_1970]\] \[[Nelson et al 1997][research_nelson_price_1997]\] \[[Neuhaus 2018][research_neuhaus_2018]\] \[[Nietubicz 1975][research_nietubicz_1975]\] \[[Octavianie and Ichsan 2020][research_octavianie_ichsan_2020]\] \[[P.V and Laxman 2023][research_pv_laxman_2023]\] \[[Painter and Sitterle 1974][research_painter_1974]\] \[[Pfaff 1968][research_pfaff_1968]\] \[[Putman 1969][research_putman_1969]\] \[[Pyle 1971][research_pyle_1971]\] \[[Pyle and Ash 1970][research_pyle_1970]\] \[[Qi et al 2021][research_qi_li_2021]\] \[[Quinn 1963][research_quinn_1963]\] \[[Rao et al 2012][research_rao_uhlig_2012]\] \[[Rasmussen 1979][research_rasmussen_1979]\] \[[Redlich 1971][research_redlich_1971]\] \[[Reed et al 1997][research_reed_1997]\] \[[Reimann 2016][research_reimann_2016]\] \[[Rivers et al 1991][research_rivers_1991]\] \[[Rizvi et al 2013][research_rizvi_he_2013]\] \[[Kempel et al 1970][research_kempel_1970]\] \[[Robinson et al 2025][research_robinson_ouhabi_2025]\] \[[Rodi and Bennett 2012][research_rodi_bennett_2012]\] \[[Ruf et al 1996][research_ruf_1996]\] \[[Ryan Aeronautical Co San Diego Ca 1963][research_ca_1963]\] \[[Salgueiro Filipe et al 2009][research_salgueirofilipe_deweerdt_2009]\] \[[Saltzman et al 1999][research_saltzman_1999]\] \[[Saltzman et al 2002][research_saltzman_2002]\] \[[Saltzman et al 2007][research_saltzman_2007]\] \[[Santos 2009][research_santos_2009]\] \[[Santos 2011][research_santos_2011]\] \[[Sayadi et al 2018][research_sayadi_kosari_2018]\] \[[Senkans et al 2021][research_senkans_kish_2021]\] \[[Sforza 2020][research_sforza_2020]\] \[[Shi et al 2009][research_shi_tang_2009]\] \[[Shi et al 2025][research_shi_li_2025]\] \[[Shi Linan et al 2014][research_shilinan_lihuifeng_2014]\] \[[Silvestre 2013][research_silvestre_2013]\] \[[Sim 1973][research_sim_1973]\] \[[Sim 1973][research_sim_1973_b]\] \[[Simplício et al 2018][research_simplicio_navarrotapia_2018]\] \[[Slegers et al 2007][research_slegers_beyer_2007]\] \[[Smith 1965][research_smith_1965]\] \[[Smith et al 1998][research_smith_amitay_1998]\] \[[Soistmann and Spain 1993][research_soistmann_1993]\] \[[Song et al 2026][research_song_shi_2026]\] \[[Songhui et al 2020][research_songhui_chufeng_2020]\] \[[Sostaric et al 2017][research_sostaric_cerimele_2017]\] \[[Spearman and Torres 1994][research_spearman_1994]\] \[[Spearman 1985][research_spearman_1985]\] \[[Stadler 1993][research_stadler_1993]\] \[[Starkey and Lewis 2000][research_starkey_lewis_2000]\] \[[Stevens et al 1966][research_stevens_1966]\] \[[Strutz 1972][research_strutz_1972]\] \[[Study of the influence 1967][research_study_influence_1967]\] \[[Suit et al 1964][research_suit_1964]\] \[[Sun et al 2025][research_sun_huang_2025]\] \[[Sun et al 2026][research_sun_chang_2026]\] \[[Suppes and Suppes 2026][research_suppes_2026]\] \[[Takahashi et al 2024][research_takahashi_camberos_2024]\] \[[Tan et al 2025][research_tan_yang_2025]\] \[[Tang 1970][research_tang_1970]\] \[[Tang 1971][research_tang_1971_b]\] \[[Tang and Pearson 1971][research_tang_1971]\] \[[Tang and Pearson 1973][research_tang_1973]\] \[[Tangthong and Aktimagool 2021][research_tangthong_aktimagool_2021]\] \[[Tanno et al 2017][research_tanno_komuro_2017]\] \[[Tartabini et al 2000][research_tartabini_2000]\] \[[Tendero Ventanas][research_ventanas_nd]\] \[[Teng et al 2021][research_teng_chen_2021]\] \[[Thompson 1964][research_thompson_1964]\] \[[Thompson 1970][research_thompson_1970]\] \[[Thompson 1970][research_thompson_1970_b]\] \[[Thompson 1966][research_thompson_1966]\] \[[Tsukamoto et al 2003][research_tsukamoto_deturris_2003]\] \[[Ungvichian 1986][research_ungvichian_1986]\] \[[van Oort et al 2007][research_vanoort_chu_2007]\] \[[Vetter 1966][research_vetter_1966]\] \[[Vidal 1974][research_vidal_1974]\] \[[Viladegut 2018][research_viladegut_2018]\] \[[Voloshenyuk 2018][research_voloshenyuk_2018]\] \[[Vorobуev et al 2020][research_vorobev_beliatskaya_2020]\] \[[Wallace and Gray 1963][research_wallace_1963]\] \[[Wang et al 2014][research_wang_li_2014]\] \[[Wang et al 2014][research_wang_xu_2014]\] \[[Wang et al 2022][research_wang_yang_2022]\] \[[Wang et al 2024][research_wang_liu_2024]\] \[[Wang et al 2025][research_wang_shao_2025]\] \[[Wang et al 2026][research_wang_ding_2026]\] \[[Wang 1963][research_wang_1963]\] \[[Ward and Costello 2012][research_ward_costello_2012]\] \[[Ward and Costello 2013][research_ward_costello_2013]\] \[[Ward et al 2011][research_ward_gavrilovski_2011_b]\] \[[Ward et al 2011][research_ward_gavrilovski_2011]\] \[[Ward et al 2013][research_ward_gavrilovski_2013]\] \[[Ware et al 1991][research_ware_spencerjr_1991]\] \[[Watson et al 1983][research_watson_1983]\] \[[Way et al 2024][research_way_sescu_2024]\] \[[Wei and Du 2018][research_wei_du_2018]\] \[[Wei et al 2025][research_wei_kang_2025]\] \[[Williamson 1980][research_williamson_1980]\] \[[Wolf 1996][research_wolf_1996]\] \[[Wood et al 2007][research_wood_avadhanula_2007]\] \[[Wu et al 2014][research_wu_cai_2014]\] \[[Wu 2015][research_wu_2015]\] \[[Wu 2018][research_wu_2018]\] \[[Xiaoqing Chen et al 2010][research_xiaoqingchen_zhongxihou_2010]\] \[[Xu and Lan 2018][research_xu_lan_2018]\] \[[Yan and He 2020][research_yan_he_2020]\] \[[Yan et al 2025][research_yan_chen_2025]\] \[[Yang et al 2016][research_yang_qiu_2016]\] \[[Ye et al 2024][research_ye_wang_2024]\] \[[Yin et al 2024][research_yin_2024]\] \[[Zhang et al 2016][research_zhang_wang_2016]\] \[[Zhang et al 2017][research_zhang_wang_2017]\] \[[Zhang et al 2022][research_zhang_chang_2022]\] \[[Zhang et al 2023][research_zhang_chen_2023]\] \[[Zhang et al 2025][research_zhang_wang_2025]\] \[[Zhao et al 2018][research_zhao_he_2018]\] \[[Zheng and Liu 2018][research_zheng_liu_2018]\] \[[Zheng et al 2014][research_zheng_liang_2014]\] \[[Zhou et al 2013][research_zhou_zhou_2013]\] \[[Zhou et al 2020][research_zhou_wang_2020]\] \[[Zhou et al 2023][research_zhou_zheng_2023]\] \[[Zhu et al 2021][research_zhu_bai_2021]\] \[[Zhu Qidan et al 2009][research_zhuqidan_zhangwen_2009]\] \[[Zucker 1970][research_zucker_1970]\] \[[Кашматов, 2008, Application of quasi-object control systems by angular position of airplane for the translation of airplane from horizontal flight in a glide slope approach][research_application_of_quasi_object_2008]\]

### Guidance, Navigation and Control in the Literature

**The X-40A was a flying testbed for software, so this is the cluster its results belong to.** Integrated satellite and inertial navigation, filtering, and terminal guidance are the components whose integration the flights exercised.

Of its 422 titles, 173 name integration, fusion, coupling, a Kalman filter or another filter, which is the work of making the sensors agree.

**422 records.** \[[1962, Damping An Inertial Navigation System][research_damping_an_1962]\] \[[1962, Multiple Inertial System Operation In Long Term Navigation][research_multiple_inertial_1962]\] \[[1962, The King Inertial Navigation Gyro][research_the_king_1962]\] \[[1964, Navigation and Guidance Systems Employing a Gimballess IMU][research_navigation_and_1964]\] \[[1964, Statistical Filtering of Space Navigation Measurements][research_statistical_filtering_1964]\] \[[1964, Stellar Techniques for Midcourse Navigation Guidance][research_stellar_techniques_1964]\] \[[1972, Development of STOLAND, a versatile navigation, guidance and control system][research_development_of_1972]\] \[[1997, Inertial Navigation With External Measurements][research_inertial_navigation_1997]\] \[[1997, Part I Inertial Navigation][research_part_i_1997]\] \[[1997, Part II Inertial Navigation With Aids][research_part_ii_1997]\] \[[1998, Control and Guidance System Modeling][research_control_and_1998]\] \[[1999, Discussion Questions for Integrated Navigation and Guidance Systems][research_discussion_questions_1999]\] \[[1999, Inertial Navigation Sensors and Systems][research_inertial_navigation_1999]\] \[[1999, Integrated vision/inertial navigation system design using nonlinear filtering][research_integrated_vision_inertial_1999]\] \[[1999, Kalman Filter Inertial Navigation System Flight Applications][research_kalman_filter_1999]\] \[[2001, 4 Inertial Navigation System][research_4_inertial_2001]\] \[[2004, Appendix B Inertial navigation system error budgets][research_appendix_b_2004]\] \[[2004, Appendix D Comparison of GPS and GLONASS satellite navigation systems][research_appendix_d_2004]\] \[[2004, Basic principles of strapdown inertial navigation systems][research_basic_principles_2004]\] \[[2004, Fundamental principles and historical developments of inertial navigation][research_fundamental_principles_2004]\] \[[2004, Inertial navigation system alignment][research_inertial_navigation_2004]\] \[[2004, Integrated navigation systems][research_integrated_navigation_2004]\] \[[2007, 3 Inertiale Navigation][research_3_inertiale_2007]\] \[[2007, Inertial Navigation System Ground Alignment][research_inertial_navigation_2007]\] \[[2007, The Inertial Navigation System Equations][research_the_inertial_2007]\] \[[2008, Chapteer 8. GPS Modernization and Global Navigation Satellite System GNSS][research_chapteer_8_2008]\] \[[2011, 3 Inertiale Navigation][research_3_inertiale_2011]\] \[[2011, KPCA-Kalman Filtering for the MEMS-SINS/GPS Integrated Navigation System][research_kpca_kalman_filtering_2011]\] \[[2012, Chapter 6. Piloting and Inertial Navigation][research_chapter_6_2012]\] \[[2012, Fusion of Multi-Antenna Carrier Phase Differential GPS and Inertial Measurements for Performance Evaluation of High Accuracy Integrated Aircraft Navigation Systems][research_fusion_of_2012]\] \[[2013, 5 Inertial navigation accuracy][research_5_inertial_2013]\] \[[2013, Inertial navigation][research_inertial_navigation_2013_b]\] \[[2013, Inertial navigation systems][research_inertial_navigation_2013]\] \[[2018, A Study on High Precision MEMS-IMU/GPS/Magnetometer/Barometer Integrated Navigation System][research_a_study_2018]\] \[[2018, Inertial Navigation][research_inertial_navigation_2018]\] \[[2022, Introduction and overview of inertial navigation systems][research_introduction_and_2022]\] \[[2022, Navigation-grade inertial sensors][research_navigation_grade_inertial_2022]\] \[[2023, 4 Inertial Navigation System][research_4_inertial_2023]\] \[[2023, Automatic Guidance and Control-Autopilots][research_automatic_guidance_2023]\] \[[2023, Research on Inertial Navigation Technology of Unmanned Aerial Vehicles with Integrated Reinforcement Learning Algorithm][research_research_on_2023]\] \[[Abdolkarimi and Mosavi 2020][research_abdolkarimi_mosavi_2020]\] \[[Aftatah and Zebbara 2024][research_aftatah_zebbara_2024]\] \[[Alford and Bingham 1990][research_alford_bingham_1990]\] \[[Alford et al 1994][research_alford_chamdani_1994]\] \[[Ali 2007][research_ali_2007]\] \[[Allen and Lin 2007][research_allen_lin_2007]\] \[[An Li et al 2010][research_anli_guobinchang_2010]\] \[[Andrews 1979][research_andrews_1979]\] \[[Atmeh and Subbarao 2016][research_atmeh_subbarao_2016]\] \[[Awin 2013][research_awin_2013]\] \[[Azinheira et al 2000][research_azinheira_depaiva_2000]\] \[[Bar-Itzhack and Porat 1980][research_baritzhack_porat_1980]\] \[[Barczyk and Lynch 2011][research_barczyk_lynch_2011]\] \[[Baselga et al 2009][research_baselga_garciaasenjo_2009]\] \[[Bennett et al 2017][research_bennett_2017]\] \[[Besant 1994][research_besant_1994]\] \[[Bhatia and Geller 2020][research_bhatia_geller_2020]\] \[[Bian et al 2024][research_bian_li_2024]\] \[[Binns et al 1996][research_binns_englehart_1996]\] \[[Bo et al 2020][research_bo_xiaogang_2020]\] \[[Brinda and Dasgupta 2006][research_brinda_dasgupta_2006]\] \[[Brink et al 2010][research_brink_hurtado_2010]\] \[[Brown 2023][research_brown_2023]\] \[[Brunch et al 2002][research_brunch_gilbreath_2002]\] \[[Buell and Oleinik 1998][research_buell_oleinik_1998]\] \[[Cai et al 2024][research_cai_yang_2024]\] \[[Cai et al 2025][research_cai_gao_2025]\] \[[Canniff 1969][research_canniff_1969]\] \[[Capderou 2012][research_capderou_2012]\] \[[Cappello et al 2016][research_cappello_sabatini_2016]\] \[[Carloni and Bousson 2016][research_carloni_bousson_2016]\] \[[Chan and Pervan 2011][research_chan_pervan_2011]\] \[[Chandramohan et al 2010][research_chandramohan_yucelen_2010]\] \[[Chatterji et al 1995][research_chatterji_menon_1995]\] \[[Che et al 2012][research_che_liu_2012]\] \[[Chelnokov and Perelyaev 2020][research_chelnokov_perelyaev_2020]\] \[[Chelnokov 2019][research_chelnokov_2019]\] \[[Chen and Li 2016][research_chen_li_2016]\] \[[Chen et al 2011][research_chen_yu_2011]\] \[[Chen et al 2021][research_chen_chang_2021]\] \[[Chen et al 2025][research_chen_huang_2025]\] \[[Chen Songyue et al 2018][research_chensongyue_wangliang_2018]\] \[[Chernodarov et al 2021][research_chernodarov_patrikeev_2021]\] \[[Chernodarov et al 2022][research_chernodarov_patrikeev_2022]\] \[[Chhetri et al 2026][research_chhetri_jetawatthana_2026]\] \[[Childers et al 2001][research_childers_2001]\] \[[Chin 1985][research_chin_1985]\] \[[Cohen et al 1994][research_cohen_parkinson_1994]\] \[[Collinson 1963][research_collinson_1963]\] \[[Condomines 2018][research_condomines_2018]\] \[[Contreras and Hajiyev 2019][research_contreras_hajiyev_2019]\] \[[Corban et al 2001][research_corban_gilbert_2001]\] \[[Corban et al 2004][research_corban_gilbert_2004]\] \[[Cordoba 2007][research_cordoba_2007]\] \[[Cox 1978][research_cox_1978]\] \[[Crassidis 2005][research_crassidis_2005]\] \[[Crespillo et al 2016][research_crespillo_grosch_2016]\] \[[Cronin 2013][research_cronin_2013]\] \[[Curtis 2005][research_curtis_2005]\] \[[Dai et al 2010][research_dai_li_2010]\] \[[Dai et al 2018][research_dai_tan_2018]\] \[[Dai and Sun 2023][research_dai_sun_2023]\] \[[Dasaro 1970][research_dasaro_1970]\] \[[DeBra et al 1981][research_debra_breakwell_1981]\] \[[DeMars et al 2014][research_demars_darling_2014]\] \[[Dill and Uijt de Haag 2016][research_dill_uijtdehaag_2016]\] \[[Draper 1981][research_draper_1981_b]\] \[[Draper 1981][research_draper_1981]\] \[[Duke et al 1983][research_duke_swann_1983]\] \[[Ebner and Mark 1977][research_ebner_mark_1977]\] \[[Eck and Geering 2003][research_eck_geering_2003]\] \[[Edwards 1972][research_edwards_1972]\] \[[El-Diasty and Pagiatakis 2008][research_eldiasty_pagiatakis_2008]\] \[[El-Mowafy 2005][research_elmowafy_2005]\] \[[El-Rabbany 2006][research_elrabbany_2006]\] \[[Elkaim et al 2014][research_elkaim_lie_2014]\] \[[Faisal and James 2025][research_faisal_james_2025]\] \[[Fan et al 2022][research_fan_tian_2022]\] \[[Fariz et al 2013][research_fariz_ushaq_2013]\] \[[Fedotov and Perepelkina 2019][research_fedotov_perepelkina_2019]\] \[[Feldman 1967][research_feldman_1967]\] \[[Filyashkin and Yatskivsky 2013][research_filyashkin_yatskivsky_2013]\] \[[Fischenberg 1995][research_fischenberg_1995]\] \[[Fowler 1990][research_fowler_1990]\] \[[Fresconi et al 2014][research_fresconi_celmins_2014]\] \[[Fresconi 2011][research_fresconi_2011]\] \[[Gai 1996][research_gai_1996]\] \[[Garcia-Quinchia et al 2009][research_garciaquinchia_yiguo_2009]\] \[[Genin 1969][research_genin_1969]\] \[[Gentry et al 1975][research_gentry_dappolito_1975]\] \[[George and Sukkarieh 2007][research_george_sukkarieh_2007]\] \[[Glavine et al 2018][research_glavine_desilva_2018]\] \[[Gong et al 2015][research_gong_zhang_2015]\] \[[Graovac 2007][research_graovac_2007]\] \[[Graves and Masciarelli 2002][research_graves_masciarelli_2002]\] \[[Griffiths and Miller 1986][research_griffiths_miller_1986]\] \[[Gryte et al 2017][research_gryte_hansen_2017]\] \[[Gu et al 2022][research_gu_xing_2022]\] \[[Gunderson and Hardy 1965][research_gunderson_hardy_1965]\] \[[Gómez and Walker 2017][research_gomez_walker_2017]\] \[[Haak 1994][research_haak_1994]\] \[[Hadaegh et al 1996][research_hadaegh_mettler_1996]\] \[[Halaas and Bieniawski 2010][research_halaas_bieniawski_2010]\] \[[Halbe et al 2018][research_halbe_spiess_2018]\] \[[Hammouche et al 2016][research_hammouche_sakhi_2016]\] \[[Han and Wang 2011][research_han_wang_2011]\] \[[Han 2024][research_han_2024]\] \[[Hao and Huang 2009][research_hao_huang_2009]\] \[[Hao et al 2009][research_hao_lei_2009]\] \[[Harigae et al 2003][research_harigae_tomita_2003]\] \[[Harigae and Tanabe 1990][research_harigae_tanabe_1990]\] \[[Hartl 1989][research_hartl_1989]\] \[[He et al 2025][research_he_zhang_2025]\] \[[Helers and Kraemer 1977][research_helers_kraemer_1977]\] \[[Hellings 1973][research_hellings_1973]\] \[[Hemann et al 2016][research_hemann_singh_2016]\] \[[Hoag 1983][research_hoag_1983]\] \[[Hofmann-Wellenhof et al 2003][research_hofmannwellenhof_legat_2003]\] \[[Hong et al 2018][research_hong_ryoo_2018]\] \[[Horri et al 2024][research_horri_holderbaum_2024]\] \[[Hsiao et al 1997][research_hsiao_ho_1997]\] \[[hua and yan 2018][research_hua_yan_2018]\] \[[Huang et al 2022][research_huang_yang_2022]\] \[[Huang et al 2026][research_huang_luo_2026]\] \[[Humphrey and Humphrey 1997][research_humphrey_humphrey_1997]\] \[[Hwang et al 2005][research_hwang_oh_2005]\] \[[Indig et al 2017][research_indig_benasher_2017]\] \[[Ishimoto 1995][research_ishimoto_1995]\] \[[Jekeli 2015][research_jekeli_2015]\] \[[Jetawatthana and Khamvilai 2026][research_jetawatthana_khamvilai_2026]\] \[[Jiang et al 2017][research_jiang_zhang_2017]\] \[[Jin et al 2025][research_jin_huang_2025]\] \[[Johansen and Fossen 2020][research_johansen_fossen_2020]\] \[[Johnson et al 2006][research_johnson_shalaev_2006]\] \[[Kaertner 2006][research_kaertner_2006]\] \[[Kahn and Edwards 2015][research_kahn_edwards_2015]\] \[[Kahn and Edwards 2019][research_kahn_edwards_2019]\] \[[Kalikhman et al 2018][research_kalikhman_kalikhman_2018]\] \[[Kaneshige et al 1999][research_kaneshige_bull_1999]\] \[[Kang et al 2007][research_kang_li_2007]\] \[[Karpenko et al 2010][research_karpenko_sekhavat_2010]\] \[[Kawaguchi et al 1997][research_kawaguchi_hashimoto_1997]\] \[[Kawamura and Azimov 2022][research_kawamura_azimov_2022]\] \[[Kelly 1994][research_kelly_1994]\] \[[Kendoul et al 2009][research_kendoul_nonami_2009]\] \[[Kendoul et al 2009][research_kendoul_yu_2009]\] \[[Kendoul 2012][research_kendoul_2012]\] \[[Ketterle et al 2008][research_ketterle_vuletic_2008]\] \[[Keviczky and Balas 2005][research_keviczky_balas_2005]\] \[[Keviczky and Balas 2006][research_keviczky_balas_2006]\] \[[Khalifa and Hashim 2026][research_khalifa_hashim_2026]\] \[[Kim and Langley 2003][research_kim_langley_2003]\] \[[Kim et al 2006][research_kim_lee_2006]\] \[[Kim and Um 2015][research_kim_um_2015]\] \[[Kleinert and Schleith 2010][research_kleinert_schleith_2010]\] \[[Kling 1989][research_kling_1989]\] \[[Knapp et al 2017][research_knapp_ivler_2017]\] \[[Krempasky 1996][research_krempasky_1996]\] \[[Kugler et al 2018][research_kugler_seiferth_2018]\] \[[Kugler 1996][research_kugler_1996]\] \[[Kulik et al 2025][research_kulik_ruth_2025]\] \[[Landherr and Klein 1987][research_landherr_klein_1987]\] \[[Landherr and Klein 1989][research_landherr_klein_1989]\] \[[Langston 1967][research_langston_1967]\] \[[Lawrence 1993][research_lawrence_1993]\] \[[Lee 1974][research_lee_1974]\] \[[Lee 1976][research_lee_1976]\] \[[Lemmens 2011][research_lemmens_2011]\] \[[Li and Li 2018][research_li_li_2018_c]\] \[[Li and Li 2018][research_li_li_2018_b]\] \[[Li and Li 2018][research_li_li_2018]\] \[[Li et al 2014][research_li_pan_2014]\] \[[Li et al 2014][research_li_qian_2014]\] \[[Li et al 2016][research_li_wang_2016]\] \[[Li et al 2020][research_li_jia_2020]\] \[[Li et al 2021][research_li_cheng_2021]\] \[[Li et al 2021][research_li_zhang_2021]\] \[[Li et al 2023][research_li_zeng_2023]\] \[[Li et al 2023][research_li_hu_2023]\] \[[Li Bo et al 2016][research_libo_zhangshengbing_2016]\] \[[Li 2020][research_li_2020]\] \[[Li 2025][research_li_2025]\] \[[Liang and Ren 2018][research_liang_ren_2018]\] \[[Liao et al 2021][research_liao_li_2021]\] \[[Liu and Hao 2023][research_liu_hao_2023]\] \[[Liu et al 2006][research_liu_li_2006]\] \[[Liu et al 2015][research_liu_liu_2015]\] \[[Liu et al 2020][research_liu_wang_2020]\] \[[Liu et al 2023][research_liu_di_2023]\] \[[Liu et al 2023][research_liu_he_2023]\] \[[Lu et al 2017][research_lu_lei_2017]\] \[[Lu and Yang 2018][research_lu_yang_2018]\] \[[Lu 2021][research_lu_2021]\] \[[Lu 2021][research_lu_2021_b]\] \[[Lund 2004][research_lund_2004]\] \[[Luo et al 2021][research_luo_guo_2021]\] \[[Luo et al 2025][research_luo_liu_2025]\] \[[Luo et al 2025][research_luo_song_2025]\] \[[Luyang Liang et al 2016][research_luyangliang_fengzhou_2016]\] \[[Lv et al 2021][research_lv_an_2021]\] \[[Löbl et al 2018][research_lobl_weiss_2018]\] \[[Madigan 1970][research_madigan_1970]\] \[[Manfred and Ryno 2008][research_manfred_ryno_2008]\] \[[Margaria et al 2007][research_margaria_dovis_2007]\] \[[Mario Andres Cordoba 2001][research_marioandrescordoba_2001]\] \[[Marshall et al 2011][research_marshall_cronin_2011]\] \[[Marshall et al 2021][research_marshall_sun_2021]\] \[[Matveev 2017][research_matveev_2017]\] \[[Mendes and Langley 1999][research_mendes_langley_1999]\] \[[Meyers and Weiderman 1988][research_meyers_weiderman_1988]\] \[[Mickelson and Carrico 1989][research_mickelson_carrico_1989]\] \[[Milner 2002][research_milner_2002]\] \[[Minghui et al 2017][research_minghui_qiuying_2017]\] \[[Mo et al 2018][research_mo_jianhua_2018]\] \[[Mohamed and Mamatas 2012][research_mohamed_mamatas_2012]\] \[[Mokrane et al 2022][research_mokrane_benallegue_2022]\] \[[Morelli and Klein 1995][research_morelli_1995]\] \[[Moriwaki 2015][research_moriwaki_2015]\] \[[Munguía 2014][research_munguia_2014]\] \[[Murakami et al 2008][research_murakami_kwak_2008]\] \[[Neal 1973][research_neal_1973]\] \[[Neusypin et al 2023][research_neusypin_kupriyanov_2023]\] \[[Ni et al 2023][research_ni_dai_2023]\] \[[Nielson et al 1986][research_nielson_swearingen_1986]\] \[[Niemela 1982][research_niemela_1982]\] \[[Ninomiya et al 2005][research_ninomiya_suzuki_2005]\] \[[Ninomiya et al 2006][research_ninomiya_suzuki_2006]\] \[[Niu et al 2025][research_niu_wang_2025]\] \[[Nobahari and Mohammadkarimi 2017][research_nobahari_mohammadkarimi_2017]\] \[[Nonami et al 2010][research_nonami_kendoul_2010_b]\] \[[Noureldin et al 2012][research_noureldin_karamat_2012]\] \[[Noureldin et al 2012][research_noureldin_karamat_2012_b]\] \[[Nurse et al 1978][research_nurse_prohaska_1978_b]\] \[[Nurse et al 1978][research_nurse_prohaska_1978]\] \[[Ogneru and Raileanu 2026][research_ogneru_raileanu_2026]\] \[[Olds 1998][research_olds_1998]\] \[[Olson 2015][research_olson_2015]\] \[[Olson and Sunkel 1983][research_olson_sunkel_1983]\] \[[Ouyang and Wu 2021][research_ouyang_wu_2021]\] \[[Sreena and Thomas 2017][research_pv_thomas_2017]\] \[[Padhi and Chawla 2016][research_padhi_chawla_2016]\] \[[Panzieri et al 2002][research_panzieri_pascucci_2002]\] \[[Paraforos et al 2015][research_paraforos_griepentrog_2015]\] \[[Payne et al 1975][research_payne_shoaf_1975]\] \[[Perepelkina and Fedotov 2023][research_perepelkina_fedotov_2023]\] \[[Peshekhonov 2020][research_peshekhonov_2020]\] \[[Phillips 2008][research_phillips_2008]\] \[[Pravitra and Johnson 2024][research_pravitra_johnson_2024]\] \[[Pu et al 2021][research_pu_xiaodong_2021]\] \[[Qian et al 2015][research_qian_wang_2015]\] \[[Rafatnia et al 2019][research_rafatnia_nourmohammadi_2019]\] \[[Ramasamy 2015][research_ramasamy_2015]\] \[[Raquet and Amt 2008][research_raquet_amt_2008]\] \[[Ren et al 2011][research_ren_cai_2011]\] \[[Ren et al 2020][research_ren_zi_2020]\] \[[Rezaifard and Abbasi 2017][research_rezaifard_abbasi_2017]\] \[[Richeson and Pines 2007][research_richeson_pines_2007]\] \[[Rigatos 2012][research_rigatos_2012]\] \[[Roberts and Bhanu 1992][research_roberts_bhanu_1992]\] \[[Sabatini et al 2013][research_sabatini_rodriguez_2013]\] \[[Sadraey 2011][research_sadraey_2011]\] \[[Sahawneh et al 2010][research_sahawneh_aljarrah_2010]\] \[[Santong Zhang and Shiwu Yang 2008][research_santongzhang_shiwuyang_2008]\] \[[Savkin et al 2021][research_savkin_antonov_2021]\] \[[Scherzinger and Blake Reid 1989][research_scherzinger_blakereid_1989]\] \[[Schmidt 2011][research_schmidt_2011]\] \[[Schumann et al 2011][research_schumann_mbaya_2011]\] \[[Schwartz 1983][research_schwartz_1983]\] \[[Schwarz 1981][research_schwarz_1981]\] \[[Sciegienny et al 1978][research_sciegienny_nurse_1978]\] \[[Seanor][research_seanor_nd]\] \[[Selezneva et al 2022][research_selezneva_neusypin_2022]\] \[[Shaiju and Sreeja 2022][research_shaiju_sreeja_2022]\] \[[Shamaghdari et al 2014][research_shamaghdari_nikravesh_2014]\] \[[Sheard et al 2008][research_sheard_scaysbrook_2008]\] \[[Shen 2021][research_shen_2021_b]\] \[[Shen 2021][research_shen_2021]\] \[[Shimizu and Murata 2008][research_shimizu_murata_2008]\] \[[Shufeldt 1961][research_shufeldt_1961]\] \[[Sickle 2023][research_sickle_2023]\] \[[Simmons et al][research_simmons_nd]\] \[[Simplício et al 2020][research_simplicio_marcos_2020]\] \[[Singh et al 2022][research_singh_menghal_2022]\] \[[Sivalingam and Hagen 2026][research_sivalingam_hagen_2026]\] \[[Slater 1956][research_slater_1956]\] \[[Smith and Biezad 1986][research_smithjr_biezad_1986]\] \[[Smith 2011][research_smith_2011]\] \[[Sokolov et al 2022][research_sokolov_sukhanov_2022]\] \[[Soloviev and Yang 2016][research_soloviev_yang_2016]\] \[[Son et al 2023][research_son_oh_2023]\] \[[Song et al 2023][research_song_wang_2023]\] \[[Staas and Philip C 1963][research_staas_philipc_1963]\] \[[Starkey et al 2026][research_starkey_sequeira_2026]\] \[[Stephan 2025][research_stephan_2025]\] \[[Stolle et al 2015][research_stolle_bolting_2015]\] \[[Sukenik 2004][research_sukenik_2004]\] \[[Sun et al 2022][research_sun_chen_2022]\] \[[Sun and Tang 2011][research_sun_tang_2011]\] \[[Suzuki et al 2016][research_suzuki_min_2016]\] \[[Taghizadeh et al 2022][research_taghizadeh_nezhadshahbodaghi_2022]\] \[[Taylor and Pamadi 1983][research_taylor_1983]\] \[[Tazartes and Mark 1988][research_tazartes_mark_1988]\] \[[Tekinalp and Kumbasar 2015][research_tekinalp_kumbasar_2015]\] \[[Tennstedt et al 2023][research_tennstedt_rajagopalan_2023]\] \[[Tennstedt and Schon 2021][research_tennstedt_schon_2021]\] \[[Tennstedt and Schön 2025][research_tennstedt_schon_2025]\] \[[Terheyden and Zickwolff 1986][research_terheyden_zickwolff_1986]\] \[[Theunissen 1994][research_theunissen_1994]\] \[[Tie et al 2018][research_tie_cao_2018]\] \[[Tkhorenko et al 2023][research_tkhorenko_karshakov_2023]\] \[[Toda and Koike 2021][research_toda_koike_2021]\] \[[Tokluoglu and Cavus 2019][research_tokluoglu_cavus_2019]\] \[[Tooley and Wyatt 2024][research_tooley_wyatt_2024]\] \[[Tsukamoto et al 2004][research_tsukamoto_suzuki_2004]\] \[[Tsukerman et al 2017][research_tsukerman_weiss_2017]\] \[[Vasconcelos et al 2005][research_vasconcelos_oliveira_2005]\] \[[Vepa and Zhahir 2010][research_vepa_zhahir_2010]\] \[[Verma and Mettler 2017][research_verma_mettler_2017]\] \[[Viswanathan et al 2017][research_viswanathan_sanyal_2017]\] \[[Wang et al 2014][research_wang_wang_2014]\] \[[Wang et al 2017][research_wang_zhou_2017]\] \[[Wang et al 2018][research_wang_jia_2018]\] \[[Wang et al 2018][research_wang_dong_2018]\] \[[Wang et al 2021][research_wang_li_2021]\] \[[Wang et al 2022][research_wang_zhao_2022_b]\] \[[Wang et al 2022][research_wang_zheng_2022]\] \[[Wang et al 2023][research_wang_zhai_2023]\] \[[Wang et al 2025][research_wang_wang_2025_b]\] \[[Wang 2022][research_wang_2022]\] \[[Ward et al 2015][research_ward_costello_2015]\] \[[Welker et al 2011][research_welker_huffman_2011]\] \[[Welker et al 2013][research_welker_pachter_2013]\] \[[Weng et al 2020][research_weng_liu_2020]\] \[[Westbrook 1975][research_westbrook_1975]\] \[[Widnall and Grundy 1974][research_widnall_1974]\] \[[Widnall et al 1982][research_widnall_gobbini_1982]\] \[[Wilcox 1963][research_wilcox_1963]\] \[[Williamson et al 2005][research_williamson_speyer_2005]\] \[[Wilson et al 2015][research_wilson_goktogan_2015]\] \[[Wilson and Riccardi 2022][research_wilson_riccardi_2022]\] \[[Wolfe 1976][research_wolfe_1976]\] \[[Woodbury et al 2015][research_woodbury_valasek_2015_b]\] \[[Wu and Guo 1994][research_wu_guo_1994]\] \[[Wu et al 2005][research_wu_johnson_2005]\] \[[Wu et al 2017][research_wu_gu_2017]\] \[[Xiang and Zhou 2022][research_xiang_zhou_2022]\] \[[Xiong et al 2018][research_xiong_zhao_2018]\] \[[Xiu-zhen et al 2014][research_xiuzhen_shaolei_2014]\] \[[Xu et al 2021][research_xu_liu_2021]\] \[[Xuguo et al 2018][research_xuguo_ke_2018]\] \[[Yan et al 2015][research_yan_wang_2015]\] \[[Yan et al 2023][research_yan_zhao_2023]\] \[[Yan and Xu 2013][research_yan_xu_2013]\] \[[Yang et al 2017][research_yang_wang_2017]\] \[[Yang et al 2018][research_yang_shi_2018]\] \[[Yang et al 2025][research_yang_chen_2025]\] \[[Yang and Tan 2014][research_yang_tan_2014]\] \[[Yingying et al 2011][research_yingying_yanshun_2011]\] \[[Yue et al 2017][research_yue_lian_2017]\] \[[Yue and Yuan 2002][research_yue_yuan_2002]\] \[[Zakharin and Ponomarenko 2023][research_zakharin_ponomarenko_2023]\] \[[Zhang et al 2009][research_zhang_wan_2009]\] \[[Zhang et al 2014][research_zhang_lin_2014]\] \[[Zhang et al 2016][research_zhang_shi_2016]\] \[[Zhang et al 2019][research_zhang_li_2019_d]\] \[[Zhang et al 2022][research_zhang_zhou_2022]\] \[[Zhang et al 2023][research_zhang_wang_2023_b]\] \[[Zhang et al 2023][research_zhang_zhang_2023]\] \[[Zhang Dayong et al 2008][research_zhangdayong_wuwenqi_2008]\] \[[Zhang 2008][research_zhang_2008]\] \[[Zhang 2019][research_zhang_2019]\] \[[Zhao et al 2014][research_zhao_chen_2014]\] \[[Zhao et al 2019][research_zhao_zhou_2019]\] \[[Zhao et al 2023][research_zhao_blunt_2023]\] \[[Zhao 2024][research_zhao_2024]\] \[[Zhi et al 2022][research_zhi_liu_2022]\] \[[Zhong et al 2017][research_zhong_liu_2017]\] \[[Zhou et al 2010][research_zhou_knedlik_2010]\] \[[Zhou et al 2013][research_zhou_yang_2013]\] \[[Zhou et al 2021][research_zhou_zhong_2021]\] \[[Zhou et al 2021][research_zhou_zhong_2021_b]\] \[[Zhu et al 2024][research_zhu_zhang_2024]\]

### Reusable Spaceplanes and Orbital Return Vehicles

**The programme the vehicle served has an extensive paper literature and little flight hardware.** Reusable launch vehicles, spaceplanes and orbital return vehicles have been studied continuously for decades.

Of its 611 titles, 175 name a concept, a study, a design, a trade or an optimisation, and 34 name a flight test, a flight experiment, a demonstrator or a return from flight.

**611 records.** \[[1981, Orbital Aerodynamic Maneuvers][research_orbital_aerodynamic_1981]\] \[[1999, Reusable Space Launch Vehicles][research_reusable_space_1999]\] \[[2002, SPACEPLANE HISTORY][research_spaceplane_history_2002]\] \[[2002, Spaceplane Low-cost Potential][research_spaceplane_low_cost_2002]\] \[[2002, The Spaceplane Space Age][research_the_spaceplane_2002]\] \[[2004, Advanced Hypersonic Spaceplane Multi-Role Architecture using Turbine Based Combined Cycle][research_advanced_hypersonic_2004]\] \[[2004, Tripropellant Engine Technology for Reusable Launch Vehicles][research_tripropellant_engine_2004]\] \[[2004, X-37 Flight Demonstrator Project Capabilities for Future Space Transportation System Development][research_x_37_flight_2004]\] \[[2011, The graphic Skylon reusable spaceplane][research_the_graphic_2011]\] \[[2016, Effect of Ground Proximity on Aerodynamic Forces and Moments of Reusable Launch Vehicle at Subsonic Speed][research_effect_of_ground_2016]\] \[[2016, Numerical Optimization on Approach and Landing for Reusable Launch Vehicle][research_numerical_optimization_2016]\] \[[2016, Spaceplane Coordinates][research_spaceplane_coordinates_2016]\] \[[2017, Designing a Reusable Spacecraft][research_designing_a_2017]\] \[[2018, ISRO Releases the Special Issue on 'Reusable Launch Vehicle-Technology Demonstrator'][research_isro_releases_the_2018]\] \[[2018, Performance and Technological Feasibility of Aerospace Plane Horizontal Launch and Landing with Ekranoplane Assistance][research_performance_and_2018]\] \[[2026, Response Analysis of Landing Leg Deployment and Landing Transient Impact of Reusable Launch Vehicle][research_response_analysis_2026]\] \[[2026, Reusable Launch Vehicle Landing Gear Mechanism Technologies A Review][research_reusable_launch_2026]\] \[[Abe et al 2005][research_abe_shimada_2005]\] \[[Abrahamm and Valsa 2018][research_abrahamm_valsa_2018]\] \[[Ahmed et al 2003][research_ahmed_2003]\] \[[Al Bakri][research_bakri_nd]\] \[[Al Fatih et al 2021][research_alfatih_shimoyama_2021]\] \[[Allen et al 1994][research_allen_sauvageau_1994]\] \[[Alvord et al 2024][research_alvord_arias_2024]\] \[[Andrews 1998][research_andrews_1998]\] \[[Aprovitola et al 2019][research_aprovitola_iuspa_2019]\] \[[Aprovitola et al 2019][research_aprovitola_iuspa_2019_b]\] \[[Arora and Ananthasayanam 2003][research_arora_ananthasayanam_2003]\] \[[Arora et al 2003][research_arora_george_2003]\] \[[Ashford 1993][research_ashford_1993]\] \[[Ashikhmina and Prosuntsov 2021][research_ashikhmina_prosuntsov_2021]\] \[[Ashok Gandhi et al 2020][research_ashokgandhi_jayan_2020]\] \[[Assured crew return vehicle 1992][research_assured_crew_1992]\] \[[Badikov et al 2026][research_badikov_volkova_2026]\] \[[Baillif et al 1995][research_baillif_bodepudi_1995]\] \[[Balakin et al 2018][research_balakin_elisov_2018]\] \[[Balepin et al 2001][research_balepin_czysz_2001]\] \[[Ball et al 1997][research_ball_oittinen_1997]\] \[[Baluragi et al 2011][research_baluragi_gupta_2011]\] \[[Barret 1999][research_barret_1999]\] \[[Barthelemy 1989][research_barthelemy_1989]\] \[[Baumgartner 1997][research_baumgartner_1997]\] \[[Bayer 1998][research_bayer_1998]\] \[[Bentley 2009][research_bentley_2009_c]\] \[[Bentley 2009][research_bentley_2009]\] \[[Bentley 2009][research_bentley_2009_b]\] \[[Benton 1989][research_benton_1989]\] \[[Berend and Talbot 2006][research_berend_talbot_2006]\] \[[Berkes 1992][research_berkes_1992]\] \[[Betin 1991][research_betin_1991]\] \[[Birkeland and Meuser 1999][research_birkeland_meuser_1999]\] \[[Blackstock 1970][research_blackstock_1970]\] \[[Blades and Redgrave 2000][research_blades_redgrave_2000]\] \[[Blosser 1997][research_blosser_1997]\] \[[Bo et al 2017][research_bo_yuan_2017]\] \[[Bonnal and Caporicci 2000][research_bonnal_caporicci_2000]\] \[[Borden et al 1999][research_borden_1999]\] \[[Bossi et al 1991][research_bossi_1991]\] \[[Bouslog et al 1998][research_bouslog_1998]\] \[[Boye 2020][research_boye_2020]\] \[[Brevault et al 2019][research_brevault_balesdent_2019]\] \[[Brevault et al 2020][research_brevault_balesdent_2020]\] \[[Brevault et al 2020][research_brevault_balesdent_2020_b]\] \[[Brinda et al 2005][research_brinda_arora_2005]\] \[[Brociek et al 2023][research_brociek_hetmaniok_2023]\] \[[Brock and Franke 2004][research_brock_franke_2004]\] \[[Brown and Olds 2005][research_brown_olds_2005]\] \[[Brown and Olds 2006][research_brown_olds_2006]\] \[[Bruce 1964][research_bruce_1964]\] \[[Buffo 1990][research_buffo_1990]\] \[[Manu et al 2024][research_c_vinaykumar_2024]\] \[[Calhoun 2000][research_calhoun_2000]\] \[[Campbell 1991][research_campbell_1991]\] \[[Cao et al 2024][research_cao_zhou_2024]\] \[[Caogen et al 2008][research_caogen_hongjun_2008]\] \[[Castaldi et al 2023][research_castaldi_emami_2023]\] \[[Cavdar and Mooij 2024][research_cavdar_mooij_2024]\] \[[Cazin 1989][research_cazin_1989]\] \[[Chae et al 2019][research_chae_mankodi_2019]\] \[[Chai et al 2017][research_chai_savvaris_2017]\] \[[Chai et al 2019][research_chai_savvaris_2019]\] \[[Chai et al 2019][research_chai_savvaris_2019_b]\] \[[Chang et al 2026][research_chang_seo_2026]\] \[[Charette et al 1998][research_charette_leonard_1998]\] \[[Chase and Chase 1997][research_chase_chase_1997]\] \[[Chase and McKinney 2005][research_chase_mckinney_2005]\] \[[Chase et al 1997][research_chase_mckinney_1997]\] \[[Chase 1996][research_chase_1996]\] \[[Chase 1997][research_chase_1997]\] \[[Chaudhary et al 2001][research_chaudhary_2001]\] \[[Chavagnac et al 2013][research_chavagnac_gai_2013]\] \[[Chavagnac 2003][research_chavagnac_2003]\] \[[Chawla et al 2010][research_chawla_sarmah_2010]\] \[[Chen et al 2018][research_chen_mu_2018]\] \[[Chen et al 2025][research_chen_yang_2025]\] \[[Chen et al 2025][research_chen_zhu_2025]\] \[[Chen Liu et al 2016][research_chenliu_chaoyangdong_2016]\] \[[Cheng et al 2021][research_cheng_jing_2021]\] \[[Cheng et al 2023][research_cheng_hu_2023]\] \[[Chiba et al 2006][research_chiba_obayashi_2006]\] \[[Chiesa et al 2005][research_chiesa_grassi_2005]\] \[[Chiu and Pitts 1991][research_chiu_pitts_1991]\] \[[Choo et al 2018][research_choo_mun_2018]\] \[[Christol 1993][research_christol_1993]\] \[[Chung et al 2025][research_chung_echigo_2025]\] \[[Clancy 2001][research_clancy_2001]\] \[[Clapp 1995][research_clapp_1995]\] \[[Cook 1995][research_cook_1995]\] \[[Cook 1996][research_cook_1996]\] \[[Cordes and Hertzfeld 1997][research_cordes_hertzfeld_1997]\] \[[Coue 2003][research_coue_2003]\] \[[Cowling 2011][research_cowling_2011]\] \[[Cui et al 2021][research_cui_zhang_2021]\] \[[Cummings 2003][research_cummings_2003]\] \[[Cusick and Kontis 2019][research_cusick_kontis_2019]\] \[[Czysz and Murthy 1996][research_czysz_murthy_1996]\] \[[Dai et al 2017][research_dai_liu_2017]\] \[[Daidzic 2016][research_daidzic_2016]\] \[[Dan Rugescu 2006][research_danrugescu_2006]\] \[[Daniel et al 2004][research_daniel_tumino_2004]\] \[[Daniel and Ramusat 2005][research_daniel_ramusat_2005]\] \[[Davis et al 2003][research_davis_engler_2003]\] \[[Davis 2002][research_davis_2002]\] \[[de Divitiis and Corraro 2007][research_dedivitiis_corraro_2007]\] \[[de Mûelenaere and Alonso 2018][research_demuelenaere_alonso_2018]\] \[[De Ridder and Mooij 2011][research_deridder_mooij_2011]\] \[[Defense Science Board Washington Dc 1992][research_defensescienceboardwashingtondc_1992]\] \[[Demidovich 2017][research_demidovich_2017]\] \[[Der Kiureghian 2001][research_derkiureghian_2001]\] \[[Dey et al 2018][research_dey_giri_2018]\] \[[Dissel et al 2007][research_dissel_kothari_2007]\] \[[Doman 2004][research_doman_2004]\] \[[Donahue et al 2008][research_donahue_weldon_2008]\] \[[Donahue 1997][research_donahue_1997]\] \[[Dong et al 2017][research_dong_zong_2017]\] \[[Dongpo et al 2025][research_dongpo_aiying_2025]\] \[[Dorsey et al 1999][research_dorsey_wu_1999]\] \[[Dorsey et al 2000][research_dorsey_myers_2000]\] \[[Douglas 2003][research_douglas_2003]\] \[[Dragone 2000][research_dragone_2000]\] \[[Driessen 2005][research_driessen_2005]\] \[[Dufour et al 2015][research_dufour_demuelenaere_2015]\] \[[Dumbacher and Klevatt 1994][research_dumbacher_klevatt_1994]\] \[[Dunker et al 2025][research_dunker_berdermann_2025]\] \[[Eckmann et al 1997][research_eckmann_cotta_1997]\] \[[Edwards et al 2010][research_edwards_mavris_2010]\] \[[Eggers et al 2011][research_eggers_dittrich_2011]\] \[[Eklund 2004][research_eklund_2004]\] \[[Ellis 1989][research_ellis_1989]\] \[[Elvin 1996][research_elvin_1996]\] \[[Enriquez 2025][research_enriquez_2025]\] \[[Ernst and Leidinger 1988][research_ernst_leidinger_1988]\] \[[Eymar and Deneu 2002][research_eymar_deneu_2002]\] \[[Fain et al 2026][research_fain_lambert_2026]\] \[[Fallon et al 1999][research_fallonii_taylor_1999]\] \[[Fang et al 2017][research_fang_ying_2017]\] \[[Feng et al 2026][research_feng_lang_2026]\] \[[Ferrandon 1997][research_ferrandon_1997]\] \[[Feustel-Büechl 1988][research_feustelbuechl_1988]\] \[[Filatyev et al 2014][research_filatyev_buzuluk_2014]\] \[[Fitzsimmons 1996][research_fitzsimmons_1996]\] \[[Freeman et al 1996][research_freeman_talay_1996]\] \[[Freeman et al 1997][research_freeman_talay_1997]\] \[[French 2001][research_french_2001]\] \[[Froning et al 1996][research_froningjr_mckinney_1996]\] \[[Froning 2006][research_froning_2006]\] \[[Fuchs et al 2018][research_fuchs_haskell_2018]\] \[[Fusaro et al 2016][research_fusaro_viola_2016]\] \[[Gage and Vander Kam 2003][research_gage_vanderkam_2003]\] \[[Gao et al 2012][research_gao_jiang_2012]\] \[[Gao et al 2021][research_gao_shao_2021]\] \[[Gao et al 2023][research_gao_wei_2023]\] \[[Gardinier and Taylor 1999][research_gardinier_taylor_1999]\] \[[Garg and Dodiyal 2009][research_garg_dodiyal_2009]\] \[[Gaverina et al 2026][research_gaverina_eiras_2026]\] \[[Geetha et al 2015][research_geethas_priyagnair_2015]\] \[[Gettatelli et al 2023][research_gettatelli_benedikter_2023]\] \[[Gibney 2015][research_gibney_2015]\] \[[Goldyn et al 2025][research_goldyn_marwege_2025]\] \[[Gong et al 2015][research_gong_bing_2015]\] \[[Gong et al 2022][research_gong_wang_2022]\] \[[Goyal et al 2021][research_goyal_babuska_2021]\] \[[Grace 1964][research_grace_1964]\] \[[Grantz 2011][research_grantz_2011]\] \[[Griffin and Takahashi 2022][research_griffin_takahashi_2022]\] \[[Grigoli 2024][research_grigoli_2024]\] \[[Grossi et al 2026][research_grossi_fabiani_2026]\] \[[Grosveld et al 2004][research_grosveld_2004]\] \[[Guadagnini et al 2023][research_guadagnini_dezaiacomo_2023]\] \[[Guo et al 2025][research_guo_du_2025]\] \[[Gupta et al 2018][research_gupta_anilkumar_2018]\] \[[Haggerty 1986][research_haggerty_1986]\] \[[Halbe et al 2014][research_halbe_raja_2014]\] \[[Hall and Shtessel 2005][research_hall_shtessel_2005]\] \[[Hallion et al 1995][research_hallion_becker_1995]\] \[[Haney and Rothschild 2003][research_haney_rothschild_2003]\] \[[Hannigan et al 1993][research_hannigan_sved_1993]\] \[[Hannum and Berkopec 1989][research_hannum_berkopec_1989]\] \[[Hao et al 2017][research_hao_peng_2017]\] \[[Hardin 1986][research_hardin_1986]\] \[[Hardy et al 1993][research_hardy_eldrenkamp_1993]\] \[[Hasegawa and Kanda 2019][research_hasegawa_kanda_2019]\] \[[Hasegawa et al 2021][research_hasegawa_fukui_2021]\] \[[Hellman et al 2010][research_hellman_ngo_2010]\] \[[Hellman et al 2011][research_hellman_remillard_2011]\] \[[Hellman et al 2011][research_hellman_wallace_2011]\] \[[Hellman and Tejtel 2008][research_hellman_tejtel_2008]\] \[[Herholz and Valentiny 1988][research_herholz_valentiny_1988]\] \[[Hertzfeld 2000][research_hertzfeld_2000]\] \[[Herzog et al 1998][research_herzog_yue_1998]\] \[[Hetmaniok et al 2024][research_hetmaniok_brociek_2024]\] \[[Hong et al 2005][research_hong_lee_2005]\] \[[Hoyt 2006][research_hoyt_2006]\] \[[Hu et al 2022][research_hu_ji_2022]\] \[[Huang et al 2024][research_huang_dai_2024]\] \[[Huang 2016][research_huang_2016]\] \[[Huayanay Villar et al 2024][research_huayanayvillar_aldana_2024]\] \[[Hudson and Stephens 2006][research_hudson_2006]\] \[[Hudson and Stephens 2009][research_hudson_2009]\] \[[Hunt 1989][research_hunt_1989]\] \[[Inokuchi 1996][research_inokuchi_1996]\] \[[Ishikawa and Ogasawara 2001][research_ishikawa_ogasawara_2001]\] \[[Ishimoto et al 2005][research_ishimoto_fujii_2005]\] \[[Ito and Nomoto 1990][research_ito_nomoto_1990]\] \[[Ito et al 1990][research_ito_akimoto_1990]\] \[[Jacobson 2004][research_jacobson_2004]\] \[[Jacobson 2004][research_jacobson_2004_b]\] \[[Jalaja et al 2023][research_jalaja_manwatkar_2023]\] \[[Jameson 2001][research_jameson_2001]\] \[[Janicik 1999][research_janicik_1999]\] \[[Jategaonkar et al 2006][research_jategaonkar_behr_2006]\] \[[Jathaveda et al 2023][research_jathaveda_manokaran_2023]\] \[[Jee et al 2014][research_jee_yalagach_2014]\] \[[Jee et al 2014][research_jee_brinda_2014]\] \[[Jia et al 2020][research_jia_fu_2020]\] \[[Jianguo et al 2016][research_jianguo_guoqing_2016]\] \[[Jiawei 2024][research_jiawei_2024]\] \[[Jo and Ahn 2021][research_jo_ahn_2021]\] \[[Jo and Ahn 2022][research_jo_ahn_2022]\] \[[Jones et al 1987][research_jones_gruszczynski_1987]\] \[[Jouhaud 1992][research_jouhaud_1992]\] \[[Ju et al 2022][research_ju_wei_2022]\] \[[Junaid R and Beebi M 2015][research_junaidr_beebim_2015]\] \[[Kalden 2007][research_kalden_2007]\] \[[Kam and Gage 2004][research_kam_gage_2004]\] \[[Kaplan 2002][research_kaplan_2002]\] \[[Karasopoulos et al 1998][research_karasopoulos_cervisi_1998]\] \[[Karel 1967][research_karel_1967]\] \[[Kato 1991][research_kato_1991]\] \[[Kelly et al 2010][research_kelly_menich_2010]\] \[[Khamlak 2026][research_khamlak_2026]\] \[[Khan and Chakraborty 2023][research_khan_chakraborty_2023]\] \[[Khan and Chakraborty 2026][research_khan_chakraborty_2026]\] \[[Kiehn 2020][research_kiehn_2020]\] \[[Kilgore and Kilgore 1997][research_kilgore_kilgore_1997]\] \[[Kim et al 2021][research_kim_lee_2021]\] \[[Kim et al 2024][research_kim_woldeyohannis_2024]\] \[[Kim et al 2026][research_kim_ko_2026]\] \[[Klevatt and Gaubatz 1998][research_klevatt_gaubatz_1998]\] \[[Kluever and Horneman 2005][research_kluever_horneman_2005]\] \[[Kluever et al 2009][research_kluever_horneman_2009]\] \[[Kluever 2007][research_kluever_2007]\] \[[Kluever 2022][research_kluever_2022]\] \[[Knapp 1999][research_knapp_1999]\] \[[Kobayashi and Maita 1995][research_kobayashi_maita_1995]\] \[[Kobayashi et al 2001][research_kobayashi_sato_2001]\] \[[Kobayashi and Tanatsugu 2001][research_kobayashi_tanatsugu_2001]\] \[[Koch et al 2025][research_koch_wilken_2025]\] \[[Koelle 1993][research_koelle_1993]\] \[[Koelle 2000][research_koelle_2000]\] \[[Koelle 2000][research_koelle_2000_b]\] \[[Koelle 2002][research_koelle_2002]\] \[[Kokan and Olds 2002][research_kokan_olds_2002]\] \[[Komar and Christenson 1996][research_komar_christenson_1996]\] \[[Komatsu and Ohyagi 2001][research_komatsu_ohyagi_2001]\] \[[Komatsu et al 2005][research_komatsu_suzuki_2005]\] \[[Kondrashev and Lutsenko 2026][research_kondrashev_lutsenko_2026]\] \[[Kondrashov 2023][research_kondrashov_2023]\] \[[Krishnan and Sajikumar 2023][research_krishnan_sajikumar_2023]\] \[[Kroncke 1985][research_kroncke_1985]\] \[[Kudo and Kato 1991][research_kudo_kato_1991]\] \[[Kumar and Mahulikar 2016][research_kumar_mahulikar_2016]\] \[[Kumar 2001][research_kumar_2001]\] \[[Kuzin et al 2009][research_kuzin_lozin_2009]\] \[[Lachman et al 2025][research_lachman_ratliff_2025]\] \[[Lagimoniere and Avram 2024][research_lagimoniere_avram_2024]\] \[[Larsen 2000][research_larsen_2000]\] \[[Larsen 2003][research_larsen_2003]\] \[[Larsen 2005][research_larsen_2005]\] \[[Lauer 2006][research_lauer_2006]\] \[[Launius 2013][research_launius_2013]\] \[[Launius 2013][research_launius_2013_b]\] \[[Le and Goo 2021][research_le_goo_2021]\] \[[Le and Goo 2021][research_le_goo_2021_b]\] \[[Le Goff and Moreau 2013][research_legoff_moreau_2013]\] \[[Lee et al 2026][research_lee_jo_2026]\] \[[Lee et al 2026][research_lee_kim_2026]\] \[[Lei et al 2017][research_lei_yan_2017]\] \[[Leisman 2000][research_leisman_2000]\] \[[Letchworth 2011][research_letchworth_2011]\] \[[Li et al 2019][research_li_peng_2019]\] \[[Li et al 2023][research_li_zhao_2023]\] \[[Li et al 2025][research_li_zhao_2025]\] \[[Li et al 2025][research_li_xu_2025]\] \[[Li et al 2025][research_li_wang_2025]\] \[[Li et al 2025][research_li_li_2025]\] \[[Li et al 2026][research_li_du_2026]\] \[[Liang et al 2020][research_liang_wang_2020]\] \[[Liang et al 2022][research_liang_xu_2022]\] \[[Liao et al 2023][research_liao_song_2023]\] \[[Liao et al 2023][research_liao_chu_2023]\] \[[Liaoni Wu et al 2008][research_liaoniwu_yiminhuang_2008]\] \[[Lindberg et al 1997][research_lindberg_schade_1997]\] \[[Liu et al 2017][research_liu_dai_2017]\] \[[Liu et al 2023][research_liu_yan_2023]\] \[[Liu et al 2025][research_liu_liu_2025_b]\] \[[Liu et al 2025][research_liu_liu_2025_c]\] \[[Liu et al 2025][research_liu_kuang_2025]\] \[[Logsdon and Williamson 1997][research_logsdon_williamson_1997]\] \[[London and Sumrall 1999][research_london_1999]\] \[[Lu 1999][research_lu_1999]\] \[[Lu 1996][research_lu_1996]\] \[[Lu 1997][research_lu_1997]\] \[[Luo et al 2022][research_luo_wu_2022]\] \[[Ma et al 2005][research_ma_zhao_2005]\] \[[Ma et al 2018][research_ma_chen_2018]\] \[[MacConochie 2000][research_macconochie_2000]\] \[[MacLeod 2026][research_macleod_2026]\] \[[Maddock and Minisci 2016][research_maddock_minisci_2016]\] \[[Maiorova et al 2016][research_maiorova_prosuntsov_2016]\] \[[Maita and Kobayashi 1996][research_maita_kobayashi_1996]\] \[[Maita et al 1993][research_maita_stockmans_1993]\] \[[Manley et al 2000][research_manley_2000]\] \[[Manokaran et al 2009][research_manokaran_vidya_2009]\] \[[Mao et al 2018][research_mao_dou_2018]\] \[[Marlow 2003][research_marlow_2003]\] \[[Marshall 1986][research_marshall_1986_b]\] \[[Martin et al 2024][research_martin_stay_2024]\] \[[Martin 2006][research_martin_2006]\] \[[Martindale 2006][research_martindale_2006]\] \[[Martins et al 2025][research_martins_rassi_2025]\] \[[Masilamani et al 2018][research_masilamani_kumar_2018]\] \[[Mastromatteo et al 2023][research_mastromatteo_gaverina_2023]\] \[[Mastromatteo et al 2026][research_mastromatteo_gaverina_2026]\] \[[Mathavaraj et al 2010][research_mathavaraj_halbe_2010]\] \[[Mathavaraj and Padhi 2020][research_mathavaraj_padhi_2020]\] \[[McClure 1998][research_mcclure_1998]\] \[[McGuire et al 2004][research_mcguire_gage_2004]\] \[[McKenzie 2003][research_mckenzie_2003]\] \[[Mehta and Bowles 2001][research_mehta_bowles_2001_b]\] \[[Mehta and Bowles 2001][research_mehta_bowles_2001]\] \[[Mendham 2003][research_mendham_2003]\] \[[Menees et al 1987][research_menees_wilson_1987]\] \[[Meng et al 2009][research_meng_wu_2009]\] \[[Menon et al 2009][research_menon_postlethwaite_2009]\] \[[Menon et al 2025][research_menon_ck_2025]\] \[[Meyerson and Taylor 2001][research_meyerson_taylor_2001]\] \[[Meyerson 1998][research_meyerson_1998]\] \[[Michalski and Johnson 2007][research_michalski_johnson_2007]\] \[[Mikula et al 2000][research_mikula_holthaus_2000]\] \[[Miotto and LePome 2003][research_miotto_lepome_2003]\] \[[Mo et al 2024][research_mo_li_2024]\] \[[Mori et al 1999][research_mori_maita_1999]\] \[[Mori et al 2001][research_mori_maita_2001]\] \[[Morino et al 2001][research_morino_shimoda_2001]\] \[[Morris 1995][research_morrisjr_1995]\] \[[Moses et al 1999][research_moses_1999]\] \[[Mowry and Grasso 2020][research_mowry_grasso_2020]\] \[[Mu and Zhang 2014][research_mu_zhang_2014]\] \[[Mukundan et al 2022][research_mukundan_maity_2022]\] \[[Ménou][research_menou_nd]\] \[[Naftel and Powell 1993][research_naftel_1993]\] \[[Nag et al 2023][research_nag_senthil_2023]\] \[[Najam 2014][research_najam_2014]\] \[[Nazar et al 2020][research_nazar_gandhi_2020]\] \[[Nebylov and Nebylov 2011][research_nebylov_nebylov_2011]\] \[[Nelson 2003][research_nelson_2003]\] \[[Ngo and Blake 2003][research_ngo_blake_2003]\] \[[Ngo and Doman 2002][research_ngo_doman_2002]\] \[[Ning et al 2007][research_ning_zhang_2007]\] \[[Niu et al 2019][research_niu_meng_2019]\] \[[Nizin et al 2016][research_nizin_antony_2016]\] \[[Noh et al 2024][research_noh_sharif_2024]\] \[[Nuhija 2021][research_nuhija_2021]\] \[[Obermann and Williamson 1998][research_obermann_williamson_1998]\] \[[Ohkami et al 1991][research_ohkami_yamanaka_1991]\] \[[Olds and Bellini 1998][research_olds_bellini_1998]\] \[[Olds et al 1999][research_olds_bradford_1999]\] \[[Otsu et al 2006][research_otsu_abe_2006]\] \[[Otsu et al 2015][research_otsu_yamada_2015]\] \[[Pace and Maji 2008][research_pace_maji_2008]\] \[[Palmer et al 1997][research_palmer_henline_1997]\] \[[Pavanasam et al 2024][research_pavanasam_anil_2024]\] \[[Pei et al 2025][research_pei_liu_2025]\] \[[Pengxin et al 2015][research_pengxin_feng_2015]\] \[[Penn and Lindley 1997][research_penn_lindley_1997]\] \[[Piacquadio et al 2023][research_piacquadio_pridohl_2023]\] \[[Pienkowski et al 2003][research_pienkowski_whitmore_2003]\] \[[Pogorelov 2008][research_pogorelov_2008]\] \[[Pogorelov 2009][research_pogorelov_2009]\] \[[Post and Dagli 2004][research_post_dagli_2004]\] \[[Powell and Cruz 1991][research_powell_1991]\] \[[Prasad 2022][research_prasad_2022]\] \[[Preliminary subsystem designs for 1990][research_preliminary_subsystem_1990]\] \[[Preliminary subsystem designs for 1990][research_preliminary_subsystem_1990_b]\] \[[Preliminary Subsystem Designs for 1990][research_preliminary_subsystem_1990_c]\] \[[Purcell et al 2025][research_purcell_wicklund_2025]\] \[[Qian et al 2012][research_qian_jiang_2012]\] \[[Qu et al 2023][research_qu_zhang_2023]\] \[[Radhakrishnan et al 2023][research_radhakrishnan_hari_2023]\] \[[Radhakrishnan et al 2024][research_radhakrishnan_hari_2024]\] \[[Rasky et al 2001][research_rasky_milos_2001]\] \[[Rasky et al 2006][research_rasky_pittman_2006]\] \[[Rasky 1995][research_rasky_1995]\] \[[Redding 1984][research_redding_jr_1984]\] \[[Redondo Gutierrez et al 2022][research_redondogutierrez_seelbinder_2022]\] \[[Ren et al 2025][research_ren_wang_2025]\] \[[Ren et al 2025][research_ren_ma_2025]\] \[[Rey 2000][research_rey_2000]\] \[[Ricciardi et al 2020][research_ricciardi_maddock_2020]\] \[[Rimani et al 2022][research_rimani_viola_2022]\] \[[Robinson et al 1995][research_robinson_nolen_1995]\] \[[Rodriguez et al 2005][research_rodriguez_2005]\] \[[Roessler 1967][research_roessler_1967]\] \[[Rogers and Dragone 1996][research_rogers_dragone_1996]\] \[[Rogers et al 2004][research_rogers_safie_2004]\] \[[Romano et al 2024][research_romano_cecchetti_2024]\] \[[Rooney 2003][research_rooney_2003]\] \[[Rubenstein and Carter 2000][research_rubenstein_carter_2000]\] \[[Ruppe 1985][research_ruppe_1985]\] \[[Russo et al 2026][research_russo_voto_2026]\] \[[Salt 2015][research_salt_2015]\] \[[Sarkar et al 2021][research_sarkar_amrr_2021]\] \[[Sasa et al 1991][research_sasa_takizawa_1991]\] \[[Sawyer and Bush 1998][research_sawyer_bush_1998]\] \[[Sawyer et al 1997][research_sawyer_bush_1997]\] \[[Sawyer et al 1999][research_sawyer_hodge_1999]\] \[[Scarlatella et al 2024][research_scarlatella_guadagnini_2024]\] \[[Schierman et al 2001][research_schierman_ward_2001]\] \[[Schierman et al 2001][research_schierman_ward_2001_b]\] \[[Schierman et al 2004][research_schierman_gandhi_2004]\] \[[Schmidt and Mann 1996][research_schmidt_mann_1996]\] \[[Schneider et al 2005][research_schneider_searcy_2005]\] \[[Schwabacher et al 2002][research_schwabacher_2002]\] \[[Schwelkart and Hallion 1997][research_schwelkart_hallion_1997]\] \[[Sexton 2003][research_sexton_2003]\] \[[Sha et al 2026][research_sha_li_2026]\] \[[Shaw et al 1997][research_shaw_taylor_1997]\] \[[Shawyer 2023][research_shawyer_2023]\] \[[Shepperd et al 2000][research_shepperd_lentsch_2000]\] \[[Shepperd and Staugler 1999][research_shepperd_staugler_1999]\] \[[Shi et al 2025][research_shi_li_2025_b]\] \[[Shiji and Kulik 2026][research_shiji_kulik_2026]\] \[[Shtessel et al 1997][research_shtessel_tournes_1997]\] \[[Shtessel et al 2000][research_shtessel_hall_2000]\] \[[Shtessel et al 2002][research_shtessel_zhu_2002]\] \[[Shulga and Shcheglov 2021][research_shulga_shcheglov_2021]\] \[[Sillen 1993][research_sillen_1993]\] \[[Singh 2023][research_singh_2023]\] \[[Sippel and Pohl 1996][research_sippel_pohl_1996]\] \[[Sippel and Sippel 1997][research_sippel_sippel_1997]\] \[[Sithara and Shenil 2022][research_sithara_shenil_2022]\] \[[Sivan and Murmu 2017][research_sivan_murmu_2017]\] \[[Sivan and Pandian 2018][research_sivan_pandian_2018]\] \[[Skariya et al 2014][research_skariya_sebastian_2014]\] \[[Smith 2003][research_smith_2003]\] \[[Solntsev 2014][research_solntsev_2014]\] \[[Song et al 2005][research_song_liao_2005]\] \[[Song et al 2024][research_song_zhang_2024]\] \[[Spidaliere et al 2004][research_spidaliere_zipay_2004]\] \[[Sponable et al 2004][research_sponable_morse_2004]\] \[[Springer 1996][research_springer_1996]\] \[[Sruthi S et al 2015][research_sruthis_sumathyr_2015]\] \[[Stadler 1998][research_stadler_1998]\] \[[Staniszewski 1999][research_staniszewski_1999]\] \[[Stapleton et al 1997][research_stapleton_galati_1997]\] \[[Stein 2005][research_stein_2005]\] \[[Stern and Chu 1963][research_stern_chu_1963]\] \[[Stower 2024][research_stower_2024]\] \[[Su and Kiang 2022][research_su_kiang_2022]\] \[[Su and Liu 2025][research_su_liu_2025_b]\] \[[Su and Liu 2025][research_su_liu_2025]\] \[[Su et al 2021][research_su_dai_2021]\] \[[Su et al 2021][research_su_dai_2021_b]\] \[[Su and Wang 2015][research_su_wang_2015]\] \[[Surzhikov 2018][research_surzhikov_2018_b]\] \[[Sushnigdha 2021][research_sushnigdha_2021]\] \[[Svyatushenko and Yagodnikov 2021][research_svyatushenko_yagodnikov_2021]\] \[[Swathy et al 2018][research_swathy_geetha_2018]\] \[[Taguchi et al 1999][research_taguchi_maita_1999]\] \[[Taguchi et al 2001][research_taguchi_futamura_2001]\] \[[Takahashi et al 1997][research_takahashi_mizobata_1997]\] \[[Talay and Stone 1991][research_talay_1991]\] \[[Tanck and Steadman 1998][research_tanck_steadman_1998]\] \[[Taniguchi 2000][research_taniguchi_2000]\] \[[Tao Guo et al 2010][research_taoguo_daweiliu_2010]\] \[[Tariq et al 2026][research_tariq_wasim_2026]\] \[[Tatry et al 1997][research_tatry_deneu_1997]\] \[[Temple 2006][research_temple_2006]\] \[[Teng et al 2025][research_teng_han_2025]\] \[[Tetlow et al 2000][research_tetlow_schoettle_2000]\] \[[The NASA IVHM Technology 2000][research_nasa_ivhm_2000]\] \[[Thies 2022][research_thies_2022]\] \[[Thomas 1998][research_thomas_1998]\] \[[Throckmorton 1989][research_throckmorton_1989]\] \[[Tian et al 2013][research_tian_zong_2013]\] \[[Tian et al 2015][research_tian_fan_2015]\] \[[Toso and Maddock 2017][research_toso_maddock_2017]\] \[[Tournes and Johnson 1998][research_tournes_johnson_1998]\] \[[Tournes and Johnson 1998][research_tournes_johnson_1998_b]\] \[[Tournes and Johnson 2001][research_tournes_johnson_2001]\] \[[Tournes et al 1998][research_tournes_landrum_1998]\] \[[Trivailo et al 2013][research_trivailo_lentsch_2013]\] \[[Troya et al 2018][research_troya_mailloux_2018]\] \[[Tsuchiya and Suzuki 1998][research_tsuchiya_suzuki_1998]\] \[[Tsuchiya and Suzuki 2001][research_tsuchiya_suzuki_2001]\] \[[Tsukahara et al 2001][research_tsukahara_yamao_2001]\] \[[Tuohy 1998][research_tuohy_1998]\] \[[Turner 2003][research_turner_2003_b]\] \[[Turner and London 2000][research_turner_2000]\] \[[Turner 2003][research_turner_2003]\] \[[Umadevi et al 2017][research_umadevi_navas_2017]\] \[[Urschel and Cox 2003][research_urschel_cox_2003]\] \[[Vaglio-Laurin and Finke 1965][research_vagliolaurin_finke_1965]\] \[[Valentine et al 2004][research_valentine_2004]\] \[[Verderame et al 1999][research_verderame_phillips_1999]\] \[[Vinod et al 2012][research_vinod_geetha_2012]\] \[[Wakamatsu et al 1999][research_wakamatsu_ono_1999]\] \[[Wallace et al 2003][research_wallace_olds_2003]\] \[[Wang et al 2009][research_wang_wu_2009]\] \[[Wang et al 2015][research_wang_hua_2015]\] \[[Wang et al 2016][research_wang_hua_2016]\] \[[Wang et al 2017][research_wang_zou_2017]\] \[[Wang et al 2018][research_wang_li_2018_b]\] \[[Wang et al 2018][research_wang_song_2018]\] \[[Wang et al 2020][research_wang_chen_2020]\] \[[Wang et al 2022][research_wang_wei_2022]\] \[[Wang et al 2023][research_wang_li_2023]\] \[[Wang et al 2024][research_wang_xu_2024]\] \[[Wang et al 2025][research_wang_gan_2025]\] \[[Wangu and Mouyos 1998][research_wangu_mouyos_1998]\] \[[Wei et al 2022][research_wei_wang_2022]\] \[[Weiland 2003][research_weiland_2003]\] \[[Welberg et al 2015][research_welberg_werner_2015]\] \[[Welge et al 2000][research_welge_2000]\] \[[Wen et al 2021][research_wen_huang_2021]\] \[[Whiting et al 2024][research_whiting_neill_2024]\] \[[Whitmore and Dunbar 2003][research_whitmore_dunbar_2003]\] \[[Whitmore et al 2004][research_whitmore_2004]\] \[[Wierzbanowski and Ramasubramanian 2020][research_wierzbanowski_ramasubramanian_2020]\] \[[Williams and Al Seyab 2026][research_williams_alseyab_2026]\] \[[Wright 1989][research_wright_1989]\] \[[Wu et al 2019][research_wu_luo_2019]\] \[[Wu et al 2020][research_wu_tian_2020]\] \[[Wu and Wang 2018][research_wu_wang_2018]\] \[[Wu and Zhang 2023][research_wu_zhang_2023]\] \[[X-33, X-34, X-37 Press 1999][research_x_33_1999]\] \[[Xiang et al 2024][research_xiang_guo_2024]\] \[[Xiang et al 2025][research_xiang_guo_2025]\] \[[Xinguo et al 2024][research_xinguo_ting_2024]\] \[[Xu et al 2022][research_xu_guan_2022]\] \[[Xu et al 2023][research_xu_guan_2023]\] \[[Xu et al 2025][research_xu_guo_2025]\] \[[Xu and Tang 2010][research_xu_tang_2010]\] \[[Bhavana 2013][research_y_2013]\] \[[Yamada et al 2014][research_yamada_kawano_2014]\] \[[Yamada and Suzuki 2016][research_yamada_suzuki_2016]\] \[[Yamanaka et al 2001][research_yamanaka_maita_2001]\] \[[Yamanaka 1989][research_yamanaka_1989]\] \[[Yamanaka 2003][research_yamanaka_2003]\] \[[Yan and von der Dunk 1992][research_yan_vonderdunk_1992]\] \[[Yanagihara et al 1991][research_yanagihara_suzuki_1991]\] \[[Yang et al 2006][research_yang_hu_2006]\] \[[Yang et al 2024][research_yang_gan_2024]\] \[[Yap et al 2012][research_yap_macias_2012]\] \[[Ye et al 2021][research_ye_li_2021]\] \[[Ye 2023][research_ye_2023]\] \[[Yoon et al 2021][research_yoon_kim_2021]\] \[[Youssef et al 2001][research_youssef_2001]\] \[[Yu et al 2014][research_yu_sun_2014]\] \[[Yue et al 2019][research_yue_titurus_2019]\] \[[Yue et al 2022][research_yue_titurus_2022]\] \[[Yue et al 2022][research_yue_lin_2022]\] \[[Zeiler et al 1999][research_zeiler_mcghee_1999]\] \[[Zhang et al 2017][research_zhang_tang_2017]\] \[[Zhang et al 2017][research_zhang_zong_2017]\] \[[Zhang et al 2017][research_zhang_wu_2017]\] \[[Zhang et al 2017][research_zhang_wei_2017]\] \[[Zhang et al 2017][research_zhang_guo_2017]\] \[[Zhang et al 2017][research_zhang_mu_2017]\] \[[Zhang et al 2017][research_zhang_li_2017]\] \[[Zhang et al 2018][research_zhang_wei_2018]\] \[[Zhang et al 2019][research_zhang_wei_2019_b]\] \[[Zhang et al 2021][research_zhang_lin_2021]\] \[[Zhang et al 2021][research_zhang_mu_2021]\] \[[Zhang et al 2021][research_zhang_jing_2021]\] \[[Zhang et al 2022][research_zhang_zhang_2022]\] \[[Zhang et al 2023][research_zhang_liu_2023]\] \[[Zhang et al 2025][research_zhang_wang_2025_d]\] \[[Zhao et al 2020][research_zhao_li_2020]\] \[[Zhao et al 2021][research_zhao_he_2021]\] \[[Zhi et al 2015][research_zhi_ran_2015]\] \[[Zhiqiang et al 2015][research_zhiqiang_huiping_2015]\] \[[Zhou et al 2015][research_zhou_xiao_2015]\] \[[Zhou et al 2026][research_zhou_wan_2026]\] \[[Zhou 2025][research_zhou_2025]\] \[[Zilong et al 2019][research_zilong_zhaokui_2019]\] \[[Zimpfer 1999][research_zimpfer_1999]\] \[[Zubrin and Clapp 1996][research_zubrin_clapp_1996]\] \[[Zuppardi and Mongelluzzo 2023][research_zuppardi_mongelluzzo_2023]\] \[[Ашихмина and others, 2018, Thermal design of the wing skin of a tourist class reusable spacecraft][research_thermal_design_of_2018]\]

### Entry Aerothermodynamics and Thermal Protection

**This cluster covers what the X-40A did not test.** Entry guidance, hypersonic aerodynamics and thermal protection are the parts of the mission that begin in orbit, and the vehicle carried no thermal protection system at all. **The cluster is here to mark the boundary of what the flights addressed**, not because the flights addressed it.

Of its 732 titles, 214 concern thermal protection, ablation or insulation.

**732 records.** \[[1963, Design Considerations for a Re-Entry Vehicle Thermal Protection System][research_design_considerations_1963]\] \[[1972, Re-entry Thermal Analysis of Variable Thickness Spherical Vehicles][research_re_entry_thermal_1972]\] \[[1972, Structural design aspects of reusable surface insulation thermal protection systems][research_structural_design_1972]\] \[[1972, Thermal performance evaluation of REI panel steps and gaps for Space Shuttle thermal protection system][research_thermal_performance_1972]\] \[[1975, Vibration of a Reentry Vehicle][research_vibration_of_1975]\] \[[1977, Reentry vehicle nosetip material screening tests - Series M][research_reentry_vehicle_1977]\] \[[1981, Re-entry Vehicle Soft-Recovery Techniques][research_re_entry_vehicle_1981]\] \[[1981, The Effect of Surface Roughness Character on Turbulent Re-entry Heating][research_the_effect_1981]\] \[[1981, Thermal Protection System for the Galileo Mission Atmospheric Entry Probe][research_thermal_protection_1981]\] \[[1981, Wind-Tunnel Study of Ascent Heating of Multiple Re-entry Vehicle Configurations][research_wind_tunnel_study_1981]\] \[[1983, Tile-Gap Flow in the Shuttle Orbiter Thermal Protection System][research_tile_gap_flow_1983]\] \[[1994, Aerodynamic Optimization for Hypersonic Flight at Very High Altitudes][research_aerodynamic_optimization_1994]\] \[[2000, Reentry Control for Low UD Vehicles][research_reentry_control_2000]\] \[[2004, Bifurcation Analysis for the Inertial Coupling Problem of a Reentry Vehicle][research_bifurcation_analysis_2004]\] \[[2004, Nonlinear Flight Control for Re-entry Flight Vehicle][research_nonlinear_flight_2004]\] \[[2004, The Development of Thermal Protection System of " Manned Spacecraft"][research_the_development_2004]\] \[[2012, Research on Attitude Tracking Control of Reentry Vehicle via Dynamic Inversion Method][research_research_on_attitude_2012]\] \[[2013, Chapter 12 Methodology of Formation of the Windward Surface of a Winged Reentry Vehicle with Reduced Thermal Intensity][research_chapter_12_2013]\] \[[2013, Chapter 13 Numerical Modeling of Hypersonic Heat Transfer on the Windward Side of the Buran Reentry Vehicle][research_chapter_13_2013]\] \[[2013, Sunken Reentry Vehicle][research_sunken_reentry_2013]\] \[[2013, Thermal Protection System Conception][research_thermal_protection_2013]\] \[[2025, Reentry Maneuvering Vehicle Ascent Phase Trajectory Design][research_reentry_maneuvering_2025]\] \[[Abe et al 2001][research_abe_fujita_2001]\] \[[Abensur 1994][research_abensur_1994]\] \[[Achambath et al 2019][research_achambath_ramjatan_2019]\] \[[Achambath and Schwartzentruber 2018][research_achambath_schwartzentruber_2018]\] \[[Adhikari et al 2024][research_adhikari_black_2024]\] \[[Agustin et al 1999][research_agustin_mangoubi_1999]\] \[[Ai et al 2022][research_ai_wang_2022]\] \[[Alber 2012][research_alber_2012]\] \[[Alberts et al 2026][research_alberts_thomas_2026]\] \[[Alexander and T. M 1978][research_alexander_tm_1978]\] \[[Allison 2017][research_allison_2017]\] \[[Almeida 2021][research_almeida_2021]\] \[[Amato et al 2026][research_amato_giannino_2026]\] \[[An et al 2017][research_an_wang_2017]\] \[[An et al 2019][research_an_wang_2019]\] \[[An et al 2025][research_an_wang_2025]\] \[[Anderson and Kinzel 2023][research_anderson_kinzel_2023]\] \[[Anderson et al 2021][research_anderson_loewenson_2021]\] \[[Annaloro et al 2020][research_annaloro_galera_2020]\] \[[Arias et al 2022][research_arias_johnson_2022]\] \[[Arrington and Woods 1972][research_arrington_1972]\] \[[Aruna and Devi 2012][research_aruna_devi_2012]\] \[[Asl and Farahani 2013][research_asl_farahani_2013]\] \[[Asma and Van der Haegen 2010][research_asma_vanderhaegen_2010]\] \[[Aso et al 1993][research_aso_kumamoto_1993]\] \[[Bailet et al 2022][research_bailet_denis_2022]\] \[[Baker and Kramer 1979][research_baker_kramer_1979]\] \[[Balakrishnan and Kurian 2014][research_balakrishnan_kurian_2014]\] \[[Balint et al 2010][research_balint_kaslik_2010]\] \[[Banerjee and Poovathingal 2021][research_banerjee_poovathingal_2021]\] \[[Bannova 2006][research_bannova_2006]\] \[[Baradell and McLellan 1963][research_baradell_1963]\] \[[Barbera 1980][research_barbera_1980]\] \[[Bauer and Kummer 1970][research_bauer_kummer_1970]\] \[[Baysal and Luo 1999][research_baysal_1999]\] \[[Beck et al 2014][research_beck_driver_2014]\] \[[Becker 1964][research_becker_1964]\] \[[Bednarcyk et al 2023][research_bednarcyk_gustafson_2023]\] \[[Bell 1965][research_bell_1965]\] \[[Beresh 2022][research_beresh_2022]\] \[[Bertelrud et al 1992][research_bertelrud_kolodziej_1992]\] \[[Bettinger 2021][research_bettinger_2021]\] \[[Bettis and Hosder 2010][research_bettis_hosder_2010]\] \[[Bhungalia et al 2004][research_bhungalia_clewitt_2004]\] \[[Bin and Hongxin 2006][research_bin_hongxin_2006]\] \[[Bliamis et al 2018][research_bliamis_panagiotou_2018]\] \[[Blodgett et al 1986][research_blodgett_conrad_1986]\] \[[Blonigan et al 2025][research_blonigan_tencer_2025]\] \[[Blosser 2002][research_blosser_2002]\] \[[Blosser 2004][research_blosser_2004]\] \[[Bodkin et al 2024][research_bodkin_akamine_2024]\] \[[Boeing Scientific Research Labs Seattle Wa 1963][research_wa_1963]\] \[[Bohon et al 1975][research_bohon_sawyer_1975]\] \[[Bohon et al 1977][research_bohon_shideler_1977]\] \[[Bolender and Doman 2005][research_bolender_doman_2005]\] \[[Borzykh et al 2013][research_borzykh_voronin_2013]\] \[[Bouslog et al 1993][research_bouslog_an_1993]\] \[[Bouyahiaoui et al 2020][research_bouyahiaoui_haoui_2020]\] \[[Boylan 1965][research_boylan_1965]\] \[[Brooks et al 1962][research_brooks_swann_1962]\] \[[Brune et al 2017][research_brune_hosder_2017]\] \[[Bu et al 2019][research_bu_lei_2019]\] \[[Bulmer 1973][research_bulmer_1973]\] \[[Butt et al 2010][research_butt_yan_2010]\] \[[Butt et al 2011][research_butt_yan_2011]\] \[[Butt et al 2011][research_butt_yan_2011_b]\] \[[Butt et al 2013][research_butt_yan_2013]\] \[[Butt 2013][research_butt_2013]\] \[[Byrne et al 1996][research_byrne_sturgis_1996]\] \[[Cai et al 2013][research_cai_jianmei_2013]\] \[[Cai et al 2013][research_cai_song_2013]\] \[[Cai et al 2014][research_cai_song_2014]\] \[[Cain and Snelling 2022][research_cain_snelling_2022]\] \[[Carpenter et al 2019][research_carpenter_chocron_2019]\] \[[Cassanto 1966][research_cassanto_1966]\] \[[Cavallo and Ferrara 1996][research_cavallo_ferrara_1996]\] \[[Cavallo et al 1996][research_cavallo_demaria_1996]\] \[[Chang et al 2018][research_chang_guo_2018]\] \[[Chang et al 2018][research_chang_miao_2018]\] \[[Chang et al 2021][research_chang_yee_2021]\] \[[Chang et al 2022][research_chang_huang_2022]\] \[[Changsheng et al 2006][research_changsheng_wuxing_2006]\] \[[Channon and Barry 1967][research_channon_barry_1967]\] \[[Chen and Blosser 2002][research_chen_blosser_2002]\] \[[Chen and He 2025][research_chen_he_2025]\] \[[Chen et al 2006][research_chen_squire_2006]\] \[[Chen et al 2016][research_chen_zhu_2016]\] \[[Chen et al 2018][research_chen_ma_2018]\] \[[Chen et al 2020][research_chen_zhou_2020_e]\] \[[Chen et al 2020][research_chen_zhou_2020]\] \[[Chen et al 2020][research_chen_zhou_2020_c]\] \[[Chen et al 2020][research_chen_zhou_2020_d]\] \[[Cheng et al 2014][research_cheng_li_2014]\] \[[Cheng et al 2016][research_cheng_sheng_2016]\] \[[Cheng et al 2026][research_cheng_wang_2026]\] \[[Chevalier et al 2026][research_chevalier_dubroca_2026]\] \[[Chiesa et al 2005][research_chiesa_corpino_2005]\] \[[Chiesa et al 2012][research_chiesa_cardile_2012]\] \[[Chimonas 1986][research_chimonas_1986]\] \[[Chin et al 1964][research_chin_hearne_1964]\] \[[Chinnaraj et al 2024][research_chinnaraj_kim_2024]\] \[[Christoph 1985][research_christoph_1985]\] \[[Chu and Mooij 2001][research_chu_mooij_2001]\] \[[Clapp 1965][research_clapp_1965]\] \[[Clark et al 1978][research_clark_dicus_1978]\] \[[Clayton and Tinker 1992][research_clayton_tinker_1992]\] \[[Cliff et al 1992][research_cliff_well_1992]\] \[[Cooper et al 1984][research_cooper_miserentino_1984]\] \[[Costa and Sachs 2002][research_costa_sachs_2002]\] \[[Cowart and Olds 2000][research_cowart_olds_2000]\] \[[Cui et al 2017][research_cui_zhao_2017]\] \[[Cui et al 2025][research_cui_zhen_2025]\] \[[Cui et al 2026][research_cui_li_2026]\] \[[Culler et al 2007][research_culler_williams_2007]\] \[[Curtin 2026][research_curtin_2026]\] \[[Cvrlje 1999][research_cvrlje_1999]\] \[[D'Souza et al 2022][research_dsouza_mcguire_2022]\] \[[da Costa and Sachs 2002][research_dacosta_sachs_2002]\] \[[da Costa and Sachs 2003][research_dacosta_sachs_2003]\] \[[Da Costa 2003][research_dacosta_2003]\] \[[Dabas et al 2025][research_dabas_sheikh_2025]\] \[[Dang et al 2022][research_dang_stern_2022]\] \[[Daniels and Dryden, 1974, An Airborne Telescope-Camera System for High-Resolution Reentry Vehicle Photography][research_daniels_dryden_1974]\] \[[Daryabeigi 2002][research_daryabeigi_2002]\] \[[Das et al 2023][research_das_pei_2023]\] \[[Das et al 2024][research_das_wang_2024]\] \[[Davis 1969][research_davis_1969]\] \[[De Giorgis et al 1999][research_degiorgis_borriello_1999]\] \[[De Matteis 2003][research_dematteis_2003]\] \[[de Paula Vieira et al 2018][research_depaulavieira_sperandiodiasgoncalves_2018]\] \[[de Ridder and Mooij 2009][research_deridder_mooij_2009]\] \[[De Vita et al 2015][research_devita_viola_2015]\] \[[Dec and Braun 2006][research_dec_braun_2006]\] \[[Dec and Braun 2013][research_dec_braun_2013]\] \[[Del Corso et al 2015][research_corso_2015]\] \[[Desai and Lyons 2005][research_desai_2005]\] \[[Desai et al 2008][research_desai_2008]\] \[[Desao et al 2006][research_desao_2006]\] \[[Deyst 1968][research_deyst_1968]\] \[[Dhanasekaran et al 2011][research_dhanasekaran_balamurali_2011]\] \[[DiFranco 1971][research_difranco_1971]\] \[[Dimri and Matai 2011][research_dimri_matai_2011]\] \[[Ding et al 2023][research_ding_li_2023]\] \[[Dirling and Eitman 1984][research_dirlingjr_eitman_1984]\] \[[Doihara and Nishida 2002][research_doihara_nishida_2002]\] \[[Donahue and Farrell 1979][research_donahue_farrell_1979]\] \[[Dong et al 2023][research_dong_li_2023]\] \[[Dorsey et al 2004][research_dorsey_poteet_2004]\] \[[Doyle 1982][research_doyle_1982]\] \[[Dr. Michael Johnson 2020][research_drmichaeljohnson_2020]\] \[[Driver et al 2014][research_driver_carballo_2014]\] \[[Du et al 2016][research_du_jing_2016]\] \[[Duda 2016][research_duda_2016]\] \[[Duston et al 2004][research_duston_seghi_2004]\] \[[Edwards 1969][research_edwards_1969]\] \[[Efremov et al 2023][research_efremov_efremov_2023]\] \[[Emery and Bardot 2006][research_emery_bardot_2006]\] \[[Fahrenthold and Park 2005][research_fahrenthold_park_2005]\] \[[Fahy et al 2021][research_fahy_buttsworth_2021]\] \[[Fan 2015][research_fan_2015]\] \[[Feldman et al 2019][research_feldman_2019]\] \[[Feng et al 2019][research_feng_guo_2019]\] \[[Feng et al 2022][research_feng_wang_2022]\] \[[Fenghua et al 2021][research_fenghua_meng_2021]\] \[[Ferguson et al 2005][research_ferguson_zhang_2005]\] \[[Department of Astrophysics and Ferreira Santos 2022][research_ferreirasantos_2022]\] \[[Filatyev 2000][research_filatyev_2000]\] \[[Finke 1990][research_finke_1990]\] \[[Finson et al 1980][research_finson_clarke_1980]\] \[[Fong et al 1970][research_fong_ehrlich_1970]\] \[[Frankenthal 1964][research_frankenthal_1964]\] \[[Franze and Barz 2025][research_franze_barz_2025]\] \[[Franze and Basov 2026][research_franze_basov_2026]\] \[[Frapard 2003][research_frapard_2003]\] \[[Frayssinet 2019][research_frayssinet_2019]\] \[[Fremaux and Johnson 2006][research_fremaux_2006]\] \[[Frohme 1975][research_frohme_1975]\] \[[Fuhry 1999][research_fuhry_1999]\] \[[Gao and Cai 2017][research_gao_cai_2017]\] \[[Gao et al 2014][research_gao_jiang_2014]\] \[[Gao et al 2015][research_gao_li_2015]\] \[[Gao et al 2018][research_gao_cai_2018]\] \[[Gao and Yao 2018][research_gao_yao_2018]\] \[[Gaohua et al 2014][research_gaohua_jianmei_2014]\] \[[Garcia and Fowler 1974][research_garcia_fowler_1974]\] \[[Geng et al 2013][research_geng_sheng_2013]\] \[[Geng et al 2014][research_geng_sheng_2014]\] \[[Ghasemi et al 2012][research_ghasemi_moradi_2012]\] \[[Gielda et al 1990][research_gielda_deese_1990]\] \[[Glass and Glass 2002][research_glass_glass_2002]\] \[[Gnoffo et al 1994][research_gnoffo_weilmuenster_1994]\] \[[Gockel 1993][research_gockel_1993]\] \[[Godines et al 2024][research_godines_abdi_2024]\] \[[Gogu et al 2007][research_gogu_bapanapalli_2007]\] \[[Gogu et al 2009][research_gogu_bapanapalli_2009]\] \[[Goldberg 1966][research_goldberg_1966]\] \[[Goldman et al 2015][research_goldman_dowell_2015]\] \[[Goldstein et al 1978][research_goldstein_leiser_1978]\] \[[Golomazov and Ivankov 2018][research_golomazov_ivankov_2018]\] \[[Gong et al 1984][research_gong_ko_1984]\] \[[Goto et al 2004][research_goto_kawakita_2004]\] \[[Goz and Theodoulis 2025][research_goz_theodoulis_2025]\] \[[Grabowsky et al 1981][research_grabowsky_eldridge_1981]\] \[[Groener et al 1980][research_groener_stetson_1980]\] \[[Gulli and Maddalena 2014][research_gulli_maddalena_2014]\] \[[Gulli and Maddalena 2015][research_gulli_maddalena_2015_b]\] \[[Gulli et al 2014][research_gulli_maddalena_2014_b]\] \[[Gulli et al 2014][research_gulli_maddalena_2014_c]\] \[[Gulli et al 2015][research_gulli_maddalena_2015]\] \[[Gunckel 1966][research_gunckel_1966]\] \[[Guo et al 2017][research_guo_qi_2017]\] \[[Guo et al 2017][research_guo_wang_2017]\] \[[Guo et al 2018][research_guo_chang_2018]\] \[[Guo et al 2025][research_guo_luo_2025]\] \[[Guo et al 2025][research_guo_yang_2025]\] \[[Guo Jianguo et al 2016][research_guojianguo_fengzhenxin_2016]\] \[[Gupta and Ramkumar 2015][research_gupta_ramkumar_2015]\] \[[Haiqing et al 2025][research_haiqing_junfeng_2025]\] \[[Hammond et al 1967][research_hammond_adler_1967]\] \[[Han and Han 2024][research_han_han_2024]\] \[[Hankey 1963][research_hankey_1963]\] \[[Hanlon et al 2006][research_hanlon_deshmukh_2006]\] \[[Harl 2008][research_harl_2008]\] \[[Harpold 1980][research_harpold_1980]\] \[[Hayashi et al 2006][research_hayashi_aso_2006]\] \[[Hayes 1972][research_hayes_1972]\] \[[Hays et al 2022][research_hays_dsouza_2022]\] \[[He et al 2025][research_he_zhao_2025]\] \[[Heng and Sherman 1996][research_heng_sherman_1996]\] \[[Hicks and Paller 2025][research_hicks_paller_2025]\] \[[Hiltz et al 1968][research_hiltz_florence_1968]\] \[[Hirschel and Weiland 2009][research_hirschel_weiland_2009]\] \[[Hodge et al 1981][research_hodge_phillips_1981]\] \[[Hollis 2017][research_hollis_2017]\] \[[Holloway 1967][research_holloway_1967]\] \[[Hou et al 2015][research_hou_wang_2015]\] \[[Housner et al 1982][research_housner_edighoffer_1982]\] \[[Hu and Liu 2025][research_hu_liu_2025]\] \[[Hu et al 2016][research_hu_wang_2016]\] \[[Hu et al 2018][research_hu_li_2018]\] \[[Hu et al 2021][research_hu_chen_2021]\] \[[Hu et al 2024][research_hu_xiao_2024]\] \[[Huang and Dai 2023][research_huang_dai_2023]\] \[[Huang and Fan 2022][research_huang_fan_2022]\] \[[Huang et al 2019][research_huang_yao_2019]\] \[[Huang et al 2024][research_huang_gong_2024]\] \[[Huang et al 2025][research_huang_li_2025]\] \[[Huang and Yao 2018][research_huang_yao_2018]\] \[[Huang and Yao 2019][research_huang_yao_2019_b]\] \[[Hull et al 1981][research_hull_french_1981]\] \[[Humes 1978][research_humes_1978]\] \[[Hunt and Eiswirth 1996][research_hunt_eiswirth_1996]\] \[[Huynh and Kriz 2009][research_huynh_kriz_2009]\] \[[Inatani et al 1992][research_inatani_akiba_1992]\] \[[Ishimoto et al 1996][research_ishimoto_takizawa_1996]\] \[[Ivanov et al 1993][research_ivanov_bitzer_1993]\] \[[Ivanov et al 2007][research_ivanov_vashchenkov_2007]\] \[[Ivanov et al 2011][research_ivanov_vashchenkov_2011]\] \[[Jaensch and Markl 1991][research_jaensch_markl_1991]\] \[[Jayanthi and Jain 2019][research_jayanthi_jain_2019]\] \[[Ji and Zhou 2018][research_ji_zhou_2018]\] \[[Jiang et al 2014][research_jiang_ye_2014]\] \[[Jiang et al 2017][research_jiang_wang_2017]\] \[[Jiang et al 2018][research_jiang_chen_2018]\] \[[Jiang et al 2026][research_jiang_xie_2026]\] \[[Jiang and Yu 2019][research_jiang_yu_2019]\] \[[Jianguo et al 2017][research_jianguo_xiangyu_2017]\] \[[Jiayuan et al 2018][research_jiayuan_peng_2018]\] \[[Jie Liang 2020][research_jieliangzhihuilixuguoliweiboshi_2020]\] \[[Jits et al 2005][research_jits_wright_2005]\] \[[Johnis 2023][research_johnis_2023]\] \[[Johnson 2019][research_johnson_2019]\] \[[Johnson 1967][research_johnson_1967]\] \[[Johnston and Candler 2023][research_johnston_candler_2023]\] \[[Joint Conference on Lifting 1960][research_joint_conference_1960]\] \[[Jones and Diamant 1989][research_jones_diamant_1989]\] \[[Jordan and Buffington 1987][research_jordan_buffington_1987]\] \[[Jouhaud et al 2007][research_jouhaud_ferreres_2007]\] \[[Jumper and Seward 1992][research_jumper_seward_1992]\] \[[Kai and Ohtake 1996][research_kai_ohtake_1996]\] \[[Kanda et al 2006][research_kanda_ueda_2006]\] \[[Kashkovsky et al 2014][research_kashkovsky_vashchenkov_2014]\] \[[Kashkovsky et al 2019][research_kashkovsky_vashchenkov_2019]\] \[[Kashkovsky 2014][research_kashkovsky_2014]\] \[[Khalil et al 2023][research_khalil_abdelgawad_2023]\] \[[Kharchenko and Kryukov 2018][research_kharchenko_kryukov_2018]\] \[[Kim and Choi 2026][research_kim_choi_2026]\] \[[Kim et al 2020][research_kim_kim_2020]\] \[[Kimmel et al 2011][research_kimmel_adamczak_2011]\] \[[Klingenberg et al 2026][research_klingenberg_willems_2026]\] \[[Knab et al 1995][research_knab_gogel_1995]\] \[[Ko et al 1987][research_ko_1987]\] \[[Koike et al 2018][research_koike_takahashi_2018]\] \[[Kolodziej and Rasky 2003][research_kolodziej_rasky_2003]\] \[[Kontinos and Palmer 1999][research_kontinos_palmer_1999]\] \[[Koo et al 2018][research_koo_natali_2018]\] \[[Kozak and Sharipov 2012][research_kozak_sharipov_2012]\] \[[Krishnamoorthy and Clarke 2016][research_krishnamoorthy_clarke_2016]\] \[[Kryvoruka and Ashurst 1973][research_kryvoruka_ashurst_1973]\] \[[Kubota et al 2020][research_kubota_yoko_2020]\] \[[Kulu 2025][research_kulu_2025]\] \[[Kumar and Mahulikar 2017][research_kumar_mahulikar_2017]\] \[[Kumar Sulur Loganathan 2023][research_kumarsulurloganathan_2023]\] \[[Kundu 2013][research_kundu_2013]\] \[[Langston et al 2021][research_langston_peterson_2021]\] \[[Laub and White 2006][research_laub_white_2006]\] \[[Le and Goo 2025][research_le_goo_2025]\] \[[Le et al 2019][research_le_goo_2019]\] \[[Le et al 2023][research_le_han_2023]\] \[[Lefevre et al 2025][research_lefevre_lock_2025]\] \[[Leveugle and Reinhard 1999][research_leveugle_reinhard_1999]\] \[[Li et al 2008][research_li_jing_2008]\] \[[Li et al 2010][research_li_shen_2010]\] \[[Li et al 2012][research_li_zhang_2012]\] \[[Li et al 2016][research_li_chao_2016]\] \[[Li et al 2017][research_li_wu_2017]\] \[[Li et al 2018][research_li_chao_2018]\] \[[Li et al 2018][research_li_chao_2018_b]\] \[[Li et al 2022][research_li_li_2022]\] \[[Li et al 2022][research_li_chao_2022]\] \[[Li et al 2023][research_li_li_2023]\] \[[Li and Zhang 2021][research_li_zhang_2021_b]\] \[[Li 1989][research_li_1989]\] \[[Lian et al 2004][research_lian_bang_2004]\] \[[Liang et al 2025][research_liang_xu_2025]\] \[[Lin-lin et al 2015][research_linlin_jianqiao_2015]\] \[[Litvintsev et al 2019][research_litvintsev_molchanova_2019]\] \[[Liu and He 2017][research_liu_he_2017]\] \[[Liu et al 2002][research_liu_chen_2002]\] \[[Liu et al 2015][research_liu_ren_2015]\] \[[Liu et al 2016][research_liu_wang_2016]\] \[[Liu et al 2018][research_liu_liu_2018]\] \[[Liu et al 2020][research_liu_hou_2020]\] \[[Liu et al 2021][research_liu_dong_2021]\] \[[Liu et al 2022][research_liu_liu_2022]\] \[[Liu et al 2023][research_liu_hu_2023]\] \[[Liu 2025][research_liu_2025]\] \[[Longani 2000][research_longani_2000]\] \[[Lu et al 2005][research_lu_antoun_2005]\] \[[Luo et al 2026][research_luo_tang_2026]\] \[[Lv et al 2023][research_lv_wang_2023]\] \[[Lv and Zhou 2023][research_lv_zhou_2023]\] \[[Lyons 1977][research_lyons_1977]\] \[[Ma et al 2020][research_ma_wu_2020]\] \[[Ma et al 2024][research_ma_liu_2024]\] \[[Machin and Daum 2026][research_machin_daum_2026]\] \[[Mahmoud and Maaruf 2021][research_mahmoud_maaruf_2021]\] \[[Mahulikar et al 2008][research_mahulikar_khurana_2008]\] \[[Marinelli and Green 1988][research_marinelli_green_1988]\] \[[Marley and Driscoll 2017][research_marley_driscoll_2017]\] \[[Marley and Driscoll 2018][research_marley_driscoll_2018]\] \[[Marschall 2011][research_marschall_2011]\] \[[Martin and Boyd 2008][research_martin_boyd_2008]\] \[[Martin and Panesi 2022][research_martin_panesi_2022]\] \[[Masaki and Yakura 1968][research_masaki_yakura_1968]\] \[[Matsuda et al 2013][research_matsuda_kihara_2013]\] \[[Matsumoto et al 2015][research_matsumoto_kondoh_2015]\] \[[Matsunaga et al 2017][research_matsunaga_takahashi_2017]\] \[[Mazaheri et al 2014][research_mazaheri_bruce_2014]\] \[[McAfee et al 2025][research_mcafee_alpert_2025]\] \[[McAfee et al 2026][research_mcafee_rabin_2026]\] \[[McAnally and Engel 1979][research_mcanally_engel_1979]\] \[[McDowell and Williamson 1980][research_mcdowell_williamsonjr_1980]\] \[[McDowell and Williamson 1982][research_mcdowell_williamsonjr_1982]\] \[[Meckler 1965][research_meckler_1965]\] \[[Mehra 1971][research_mehra_1971]\] \[[Mehta 1989][research_mehta_1989]\] \[[Meng et al 2016][research_meng_jiang_2016]\] \[[Meseguer et al 2012][research_meseguer_perezgrande_2012]\] \[[Meyer et al 1981][research_meyerjr_jarvis_1981]\] \[[Miki and Fujii 2018][research_miki_fujii_2018]\] \[[Miller et al 2023][research_miller_kazemba_2023_b]\] \[[Miller et al 2023][research_miller_kazemba_2023]\] \[[Milos and Chen 2013][research_milos_chen_2013]\] \[[Milos and Squire 1999][research_milos_squire_1999]\] \[[Minisci and Vasile 2013][research_minisci_vasile_2013]\] \[[Minwen and Dayi 2014][research_minwen_dayi_2014]\] \[[Miyashita et al 2024][research_miyashita_sugihara_2024]\] \[[Mo et al 2023][research_mo_lu_2023]\] \[[Molchanova et al 2016][research_molchanova_kashkovsky_2016]\] \[[Molina et al 1996][research_molina_simeonides_1996]\] \[[Montella et al 2024][research_montella_vio_2024]\] \[[Mooij and Hanninen 2009][research_mooij_hanninen_2009]\] \[[Mooij 2003][research_mooij_2003]\] \[[Morelli 2009][research_morelli_2009]\] \[[Morgado et al 2022][research_morgado_garbacz_2022]\] \[[Morgan and Williams 2025][research_morgan_williams_2025]\] \[[Morrison et al 1982][research_morrison_chien_1982]\] \[[Moura and Borges Ribeiro 2025][research_moura_borgesribeiro_2025_b]\] \[[Moura and Borges Ribeiro 2025][research_moura_borgesribeiro_2025_c]\] \[[Moura and Borges Ribeiro 2025][research_moura_borgesribeiro_2025]\] \[[Mullenix and Povitsky 2016][research_mullenix_povitsky_2016]\] \[[Musal et al 1964][research_musal_hm_1964]\] \[[Nabi and Najafi 2024][research_nabi_najafi_2024]\] \[[Nakamura et al 2014][research_nakamura_kamimura_2014]\] \[[Nakasato et al 2015][research_nakasato_takahashi_2015]\] \[[Nakhod 2026][research_nakhod_2026]\] \[[Nance 2013][research_nance_2013]\] \[[Nathan 2007][research_nathan_2007]\] \[[Newman et al 1992][research_newman_fulcher_1992]\] \[[Nie et al 2023][research_nie_zhang_2023]\] \[[Ochi 2004][research_ochi_2004]\] \[[Oertel 1993][research_oertel_1993]\] \[[Ohya and Kato 1985][research_ohya_kato_1985]\] \[[Okojie et al 2023][research_okojie_go_2023]\] \[[Olynick and Henline 1996][research_olynick_henline_1996]\] \[[Olynick 1996][research_olynick_1996]\] \[[Olynick 1998][research_olynick_1998]\] \[[Ortloff 1968][research_ortloff_1968]\] \[[Otsu et al 1998][research_otsu_suzuki_1998]\] \[[Otsu et al 2001][research_otsu_kanai_2001]\] \[[Otsu et al 2004][research_otsu_matsushita_2004]\] \[[Otsu et al 2006][research_otsu_matsuda_2006]\] \[[Otsu et al 2008][research_otsu_nakamura_2008]\] \[[Otsu et al 2009][research_otsu_katsurayama_2009]\] \[[Otsu and Takama 2012][research_otsu_takama_2012]\] \[[Otsu 2016][research_otsu_2016]\] \[[Otsu 2018][research_otsu_2018]\] \[[Paciorri et al 2026][research_paciorri_assonitis_2026]\] \[[Palaninathan and Bindu 2005][research_palaninathan_bindu_2005]\] \[[Palmer et al 2009][research_palmer_pulsonetti_2009]\] \[[Palumbo et al 2012][research_palumbo_morani_2012]\] \[[Paolozzi 2004][research_paolozzi_2004]\] \[[Papadopoulos and Subrahmanyam 2005][research_papadopoulos_subrahmanyam_2005]\] \[[Park and Park 2017][research_park_park_2017]\] \[[Parker 2022][research_parker_2022]\] \[[Pastore et al 2021][research_pastore_delfini_2021]\] \[[Patel and Subbarao 2024][research_patel_subbarao_2024]\] \[[Patel and Venkatasubbaiah 2015][research_patel_venkatasubbaiah_2015]\] \[[Patera 2006][research_patera_2006]\] \[[Paulson 1959][research_paulson_1959]\] \[[Pavlov and Simakova 2021][research_pavlov_simakova_2021]\] \[[Peicheng et al 2018][research_peicheng_rong_2018]\] \[[Peipei et al 2017][research_peipei_junbo_2017]\] \[[Peng et al 2019][research_peng_qi_2019]\] \[[Peng et al 2020][research_peng_qi_2020]\] \[[Perkins and Tannas 1967][research_perkins_tannasjr_1967]\] \[[Perminov 1969][research_perminov_1969]\] \[[Petley et al 1984][research_petley_smith_1984]\] \[[Pezzella and Viviani 2024][research_pezzella_viviani_2024]\] \[[Phillips and Kryvoruka 1973][research_phillips_kryvoruka_1973]\] \[[Pittman and Dillon 1977][research_pittman_dillon_1977]\] \[[Pitts and Kourtides 1989][research_pitts_kourtides_1989]\] \[[Platus 1967][research_platus_1967]\] \[[Platus 1978][research_platus_1978]\] \[[Platus 1979][research_platus_1979]\] \[[Platus 1980][research_platus_1980]\] \[[Platus 1983][research_platus_1983]\] \[[Plumb 1971][research_plumb_1971]\] \[[Poteet and Blosser 2004][research_poteet_blosser_2004]\] \[[Poteet et al 2004][research_poteet_abukhajeel_2004]\] \[[Prakash and Zhong 2008][research_prakash_zhong_2008]\] \[[Prakash and Zhong 2009][research_prakash_zhong_2009]\] \[[Qian et al 2014][research_qian_qi_2014]\] \[[Qin et al 2023][research_qin_fu_2023]\] \[[Qin Changmao et al 2010][research_qinchangmao_qinaiming_2010]\] \[[Dileep et al 2025][research_r_ss_2025]\] \[[Rabinskiy and Tushavina 2019][research_rabinskiy_tushavina_2019]\] \[[Rajesh Yadav et al 2016][research_rajeshyadav_mohammadfaisal_2016]\] \[[Rakow and Waas 2005][research_rakow_waas_2005]\] \[[Rana and Chudoba 2016][research_rana_chudoba_2016]\] \[[Rataczak et al 2024][research_rataczak_boyd_2024]\] \[[Ravichandran et al 2023][research_ravichandran_ahmed_2023]\] \[[Ren et al 2017][research_ren_fu_2017]\] \[[Reyhanoglu and Alvarado 2013][research_reyhanoglu_alvarado_2013]\] \[[Reynerson 2006][research_reynerson_2006]\] \[[Richmond 2022][research_richmond_2022]\] \[[Rigali et al 1980][research_rigali_sterk_1980]\] \[[Rigatos et al 2023][research_rigatos_abbaszadeh_2023]\] \[[Ringel et al 2022][research_ringel_panerai_2022]\] \[[Rivers 1968][research_rivers_1968]\] \[[Roberts 2024][research_roberts_2024]\] \[[Rochelle et al 1972][research_rochelle_roberts_1972]\] \[[Roenneke and Cornwell 1992][research_roenneke_cornwell_1992]\] \[[Roenneke and Well 1995][research_roenneke_well_1995]\] \[[Roenneke and Well 1996][research_roenneke_well_1996]\] \[[Rogers et al 2022][research_rogers_schroeder_2022]\] \[[Romanov et al 2017][research_romanov_burke_2017]\] \[[Rossman and Braun 2017][research_rossman_braun_2017]\] \[[Rougeux et al 2009][research_rougeux_malomolina_2009]\] \[[Rufolo et al 2024][research_rufolo_destefanofumo_2024]\] \[[Sai Naga Bharghava et al 2024][research_sainagabharghava_krishnatmali_2024]\] \[[Samotokhin 2021][research_samotokhin_2021]\] \[[Sanson et al 2017][research_sanson_villedieu_2017]\] \[[Savino et al 2009][research_savino_viviani_2009]\] \[[Sawyer 1984][research_sawyer_1984]\] \[[Schiavazzi and Juliano 2020][research_schiavazzi_juliano_2020]\] \[[Schierman et al 2004][research_schierman_ward_2004]\] \[[Schonberg et al 2025][research_schonberg_squire_2025]\] \[[Schonberg and Squire 2024][research_schonberg_squire_2024_b]\] \[[Schonberg and Squire 2024][research_schonberg_squire_2024]\] \[[Schouler et al 2021][research_schouler_prevereaud_2021]\] \[[Schänzer 1993][research_schanzer_1993]\] \[[Scoville and Rajula 2005][research_scoville_rajula_2005]\] \[[Sepka and Samareh 2015][research_sepka_samareh_2015]\] \[[Sforza 2016][research_sforza_2016]\] \[[Shahzad and Weiduo 2019][research_shahzad_weiduo_2019]\] \[[Shan et al 2015][research_shan_huifeng_2015]\] \[[Shao et al 2015][research_shao_wang_2015_b]\] \[[Shao et al 2016][research_shao_deyang_2016]\] \[[Shao et al 2017][research_shao_wu_2017]\] \[[Shao et al 2025][research_shao_zhao_2025]\] \[[Shao and Wang 2015][research_shao_wang_2015]\] \[[Shao and Wang 2016][research_shao_wang_2016]\] \[[Sharma et al 2008][research_sharma_gogu_2008]\] \[[Sharma et al 2024][research_sharma_giangaspero_2024]\] \[[Sheldon 1967][research_sheldon_1967]\] \[[Shen et al 2016][research_shen_sheng_2016]\] \[[Shen et al 2023][research_shen_xia_2023]\] \[[Sheng et al 2015][research_sheng_geng_2015]\] \[[ShengZe Chen et al 2014][research_shengzechen_xuanzhang_2014]\] \[[Shenming et al 2017][research_shenming_tao_2017]\] \[[Shenming et al 2018][research_shenming_tao_2018]\] \[[Sherman 1978][research_sherman_1978]\] \[[Shideler et al 1985][research_shideler_webb_1985]\] \[[Shimada and Ohwada 2020][research_shimada_ohwada_2020]\] \[[Shinnick 1966][research_shinnick_1966]\] \[[Shou et al 2021][research_shou_xu_2021]\] \[[Shuai et al 2022][research_shuai_daqian_2022]\] \[[Shuping Tan and Zhibin Li 2010][research_shupingtan_zhibinli_2010]\] \[[Silva and Augusto Aparecido Gomes 2021][research_silva_augustoaparecidogomes_2021]\] \[[Simeonides 2006][research_simeonides_2006]\] \[[Simons 1975][research_simons_1975]\] \[[Simons 1976][research_simons_1976]\] \[[Sims and Hahn 1964][research_sims_hahn_1964]\] \[[Singh et al 1989][research_singh_tiwari_1989]\] \[[Sipe and Hinde 2008][research_sipe_hinde_2008]\] \[[Sivells 1969][research_sivells_1969]\] \[[Sivolella 2014][research_sivolella_2014]\] \[[Skolnik and Putnam 2020][research_skolnik_putnam_2020]\] \[[Smith et al 2018][research_smith_2018]\] \[[Snapp and Rodriguez 2011][research_snapp_rodriguez_2011]\] \[[Spearman 1984][research_spearman_1984]\] \[[Spencer and Fournier 1973][research_spencer_1973]\] \[[Spravka and Jorris 2015][research_spravka_jorris_2015_b]\] \[[Spravka and Jorris 2015][research_spravka_jorris_2015]\] \[[Staylor 1970][research_staylor_1970]\] \[[Stern 2004][research_stern_2004]\] \[[Stern 2008][research_stern_2008]\] \[[Stetson and Lewis 1977][research_stetson_lewis_1977]\] \[[Stewart et al 1986][research_stewart_leiser_1986]\] \[[Strauss 1967][research_strauss_1967]\] \[[Strouhal and Curry 1966][research_strouhal_curry_1966]\] \[[Su et al 2013][research_su_yu_2013]\] \[[Su et al 2025][research_su_hong_2025]\] \[[Sun et al 2015][research_sun_yang_2015]\] \[[Sun et al 2023][research_sun_zhu_2023]\] \[[Sun et al 2024][research_sun_jia_2024]\] \[[Sun et al 2024][research_sun_jing_2024]\] \[[Sun et al 2025][research_sun_xu_2025]\] \[[Sunasawa and Ohta 1997][research_sunasawa_ohta_1997]\] \[[Surzhikov 2015][research_surzhikov_2015]\] \[[Surzhikov 2018][research_surzhikov_2018]\] \[[Suzuki et al 2014][research_suzuki_fujita_2014]\] \[[Swann 1960][research_swann_1960]\] \[[Swanson 1958][research_swanson_1958]\] \[[Szalai et al 2005][research_szalai_chen_2005]\] \[[Tablole and Banavar 1998][research_tablole_banavar_1998]\] \[[Tahsini and Mousavi 2014][research_tahsini_mousavi_2014]\] \[[Taihua et al 2011][research_taihua_xianhong_2011]\] \[[Takahashi et al 2013][research_takahashi_yamada_2013]\] \[[Takahashi et al 2014][research_takahashi_ha_2014]\] \[[Takahashi et al 2015][research_takahashi_yamada_2015]\] \[[Takahashi et al 2016][research_takahashi_nakasato_2016]\] \[[Takahashi and Yamada 2018][research_takahashi_yamada_2018]\] \[[Tancredi and Grassi 2007][research_tancredi_grassi_2007]\] \[[Tang et al 2018][research_tang_long_2018]\] \[[Tang et al 2020][research_tang_zhai_2020]\] \[[Tava and Suzuki 2002][research_tava_suzuki_2002]\] \[[Teixeira and Páscoa 2026][research_teixeira_pascoa_2026]\] \[[Tewell 1984][research_tewell_1984]\] \[[Thomas and Perlbachs 1967][research_thomas_perlbachs_1967]\] \[[Thomas 2025][research_thomas_2025]\] \[[Throckmorton 1981][research_throckmorton_1981]\] \[[Tian et al 2025][research_tian_dong_2025]\] \[[Tian et al 2025][research_tian_luo_2025]\] \[[Tieshan et al 2021][research_tieshan_zhiyao_2021]\] \[[Tirtey et al 2005][research_tirtey_paris_2005]\] \[[Tobin and Dec 2015][research_tobin_dec_2015]\] \[[Tong 1991][research_tong_1991]\] \[[Trujillo et al 1983][research_trujillo_meyerjr_1983]\] \[[Tushavina 2025][research_tushavina_2025]\] \[[Uffelman and Deffenbaugh 1979][research_uffelman_deffenbaugh_1979]\] \[[Valente et al 2006][research_valente_bartuli_2006]\] \[[van den Abeelen 2016][research_vandenabeelen_2016]\] \[[van den Abeelen 2016][research_vandenabeelen_2016_b]\] \[[Vendemia 1965][research_vendemia_1965]\] \[[Verkhovsky et al 2023][research_verkhovsky_gyazova_2023]\] \[[Villanueva 2022][research_villanueva_2022]\] \[[Vinh and Medepalli 1994][research_vinh_medepalli_1994]\] \[[Violette 2024][research_violette_2024]\] \[[Violette 2026][research_violette_2026]\] \[[Viviani et al 2006][research_viviani_pezzella_2006]\] \[[Viviani et al 2008][research_viviani_pezzella_2008]\] \[[Viviani and Pezzella 2007][research_viviani_pezzella_2007_b]\] \[[Viviani and Pezzella 2007][research_viviani_pezzella_2007]\] \[[Viviani and Pezzella 2009][research_viviani_pezzella_2009]\] \[[Viviani and Pezzella 2010][research_viviani_pezzella_2010]\] \[[Vo et al 1993][research_vo_garrard_1993]\] \[[Walker et al 2018][research_walker_mueschke_2018]\] \[[Wallner and Well 2002][research_wallner_well_2002]\] \[[Walpot et al 2006][research_walpot_noeding_2006]\] \[[Wang et al 2011][research_wang_liu_2011]\] \[[Wang et al 2012][research_wang_liu_2012]\] \[[Wang et al 2013][research_wang_tang_2013]\] \[[Wang et al 2013][research_wang_zhang_2013]\] \[[Wang et al 2014][research_wang_wu_2014]\] \[[Wang et al 2015][research_wang_zong_2015]\] \[[Wang et al 2016][research_wang_zhou_2016]\] \[[Wang et al 2017][research_wang_feng_2017]\] \[[Wang et al 2019][research_wang_liu_2019]\] \[[Wang et al 2020][research_wang_xu_2020]\] \[[Wang et al 2025][research_wang_wang_2025]\] \[[Wang et al 2025][research_wang_yang_2025_b]\] \[[Wang et al 2025][research_wang_ai_2025]\] \[[Ward and Smart 2026][research_ward_smart_2026]\] \[[Watanabe et al 1997][research_watanabe_ishimoto_1997]\] \[[Watts 2005][research_watts_2005]\] \[[Webb and Bettinger 2024][research_webb_bettinger_2024]\] \[[Webb et al 2026][research_webb_bettinger_2026]\] \[[Weiwei et al 2022][research_weiwei_runde_2022]\] \[[Wenming et al 2015][research_wenming_zhi_2015]\] \[[White and Beck 2011][research_white_beck_2011]\] \[[White 2010][research_white_2010]\] \[[Whitfield and Griffith 1963][research_whitfield_1963]\] \[[Williams et al 1995][research_williams_curry_1995]\] \[[Williamson et al 2025][research_williamson_bi_2025]\] \[[Williamson 1978][research_williamsonjr_1978]\] \[[Williamson 1992][research_williamson_1992]\] \[[Windhorst et al 1997][research_windhorst_ardema_1997]\] \[[Wiseman and Lopez 2026][research_wiseman_lopez_2026]\] \[[Wittliff et al 1992][research_wittliff_oconnor_1992]\] \[[Woollard et al 2016][research_woollard_braun_2016]\] \[[Wortman 1969][research_wortman_1969]\] \[[Wright et al 2006][research_wright_milos_2006]\] \[[Wright et al 2014][research_wright_beck_2014]\] \[[Wright and Zoby 1971][research_wright_1971]\] \[[Wu et al 1994][research_wu_lycans_1994]\] \[[Wu et al 2012][research_wu_tang_2012]\] \[[Wu et al 2017][research_wu_lian_2017]\] \[[Wu et al 2025][research_wu_yuan_2025]\] \[[Wurster et al 1999][research_wurster_riley_1999]\] \[[Wurster and Stone 1993][research_wurster_stone_1993]\] \[[Wuxing et al 2015][research_wuxing_chunwang_2015]\] \[[Wuxing et al 2015][research_wuxing_pengxin_2015]\] \[[Xiang et al 2026][research_xiang_du_2026]\] \[[Xingling and Honglun 2014][research_xingling_honglun_2014]\] \[[Xu et al 2004][research_xu_mirmirani_2004]\] \[[Xu et al 2012][research_xu_sun_2012]\] \[[Xu et al 2022][research_xu_dong_2022]\] \[[Xu 2015][research_xu_2015]\] \[[Yadav et al 2018][research_yadav_bodavula_2018]\] \[[Yafei et al 2015][research_yafei_jianqiao_2015]\] \[[Yamada et al 2011][research_yamada_suzuki_2011]\] \[[Yamamoto et al 1996][research_yamamoto_atsumi_1996]\] \[[Yan et al 2015][research_yan_luo_2015]\] \[[Yang and Meng 2012][research_yang_meng_2012]\] \[[Yang et al 2015][research_yang_zhang_2015]\] \[[Yang et al 2022][research_yang_wang_2022]\] \[[Yang et al 2025][research_yang_men_2025]\] \[[Yang and Qi 2016][research_yang_qi_2016]\] \[[Yang and Wang 2012][research_yang_wang_2012]\] \[[Yankui et al 2005][research_yankui_2005]\] \[[Yao and Jia 2023][research_yao_jia_2023]\] \[[Yao et al 2013][research_yao_wang_2013]\] \[[Ye et al 2017][research_ye_chaofang_2017]\] \[[Yee et al 2023][research_yee_parkinson_2023]\] \[[Yoshinaga et al 1996][research_yoshinaga_tate_1996]\] \[[Young 1966][research_young_1966]\] \[[Yu et al 2021][research_yu_ni_2021]\] \[[Yu et al 2026][research_yu_wang_2026]\] \[[Zeng et al 2026][research_zeng_wang_2026]\] \[[Zhai et al 2016][research_zhai_qi_2016]\] \[[Zhai et al 2019][research_zhai_qi_2019]\] \[[Zhang and Chen 2011][research_zhang_chen_2011]\] \[[Zhang and Ding 2023][research_zhang_ding_2023]\] \[[Zhang and Han 2025][research_zhang_han_2025]\] \[[Zhang and Hu 2025][research_zhang_hu_2025]\] \[[Zhang et al 2013][research_zhang_sun_2013]\] \[[Zhang et al 2018][research_zhang_yu_2018]\] \[[Zhang et al 2019][research_zhang_li_2019]\] \[[Zhang et al 2022][research_zhang_xu_2022]\] \[[Zhang et al 2022][research_zhang_wang_2022]\] \[[Zhang et al 2022][research_zhang_shou_2022]\] \[[Zhang et al 2023][research_zhang_gao_2023]\] \[[Zhang et al 2023][research_zhang_bai_2023]\] \[[Zhang et al 2024][research_zhang_yu_2024]\] \[[Zhang et al 2025][research_zhang_han_2025_b]\] \[[Zhang et al 2025][research_zhang_yin_2025]\] \[[Zhang et al 2025][research_zhang_wang_2025_b]\] \[[Zhang et al 2026][research_zhang_liao_2026]\] \[[Zhang and Wang 2025][research_zhang_wang_2025_c]\] \[[Zhang 1992][research_zhang_1992]\] \[[Zhang 2015][research_zhang_2015]\] \[[Zhao et al 2013][research_zhao_li_2013]\] \[[Zhao and Tang 2015][research_zhao_tang_2015]\] \[[Zhao and Zhou 2013][research_zhao_zhou_2013]\] \[[Zheng et al 2025][research_zheng_zou_2025]\] \[[Zheng and Selezneva 2022][research_zheng_selezneva_2022]\] \[[Zheng and Sergeevna 2022][research_zheng_sergeevna_2022]\] \[[Zhengchun 2018][research_zhengchun_2018]\] \[[Zhou and Wang 1987][research_zhou_wang_1987]\] \[[Zhu and Liu 2015][research_zhu_liu_2015]\] \[[Zhu et al 2016][research_zhu_li_2016]\] \[[Zimmerman et al 2003][research_zimmerman_dukeman_2003]\] \[[Zimmerman et al 2002][research_zimmerman_2002]\] \[[Zong et al 2013][research_zong_wang_2013]\] \[[Zuppardi and Mongelluzzo 2023][research_zuppardi_mongelluzzo_2023_b]\] \[[Борзых and Воронин, 2012, Dynamics of Interaction of Transformable Mechanical Landing Device of the Reentry Vehicle with the Landing Surface][research_dynamics_of_interaction_2012]\] \[[안미치코, 2013, Aerodynamics Calculation of Reentry Body in Hypersonic Flowfield][research_aerodynamics_calculation_of_2013]\]

### Touchdown, Rollout and Runway Performance

**The landing does not end at touchdown and the X-37A's 2006 overrun is why this cluster matters.** Gear loads, braking, rollout distance and runway excursion are the terminal problem, and they are governed by the mass the X-40A did not carry.

Of its 409 titles, 239 concern landing gear, struts and shock absorbers, and 129 concern the runway, the tyre, braking, friction or the landing distance.

**409 records.** \[[1958, Tire-runway braking friction coefficients][research_tire_runway_braking_1958]\] \[[1960, Flight tests to determine the coefficients of friction between an aircraft tyre and various wet runway surfaces. Part I][research_flight_tests_1960]\] \[[1963, Influence of tire tread pattern and runway surface condition on braking friction and rolling resistance of a modern aircraft tire][research_influence_of_1963]\] \[[1982, The effect of additional runway lights and autopilot failure on the landing performance of a medium size transport aircraft][research_the_effect_1982]\] \[[1987, Redesigned aircraft landing gear to be analysed for stresses][research_redesigned_aircraft_1987]\] \[[2015, Assessment of Factors Responsible for the Excursion of Runway in International Airport][research_assessment_of_2015]\] \[[2019, Anatomy of a No-Equipment-Failed NEF ICNS System Malfunction The Case of Singapore Airlines Sq-327 Runway Excursion][research_anatomy_of_2019]\] \[[2020, "LaGuardia Airport Design Build for Extending Runway Decks for Safety Area Improvements, Queens, NY"][research_laguardia_airport_2020]\] \[[2022, Methodology for assessing the accuracy of UAV landing on the runway][research_methodology_for_2022]\] \[[Rubtsova A.S. 2022][research_study_of_2022]\] \[[2025, Multi-architecture Design Method for Landing Gear System Based on Domain Specific Modeling][research_multi_architecture_design_2025]\] \[[Rajesh and Bt 2015][research_a_bt_2015]\] \[[Abe et al 2018][research_abe_kasamura_2018]\] \[[Abu-Jbara et al 2015][research_abujbara_alheadary_2015]\] \[[Acarbay and Kiyak 2022][research_acarbay_kiyak_2022]\] \[[Airoldi and Janszen 2005][research_airoldi_janszen_2005]\] \[[Akinyemi and Adebiyi 2016][research_akinyemi_adebiyi_2016]\] \[[Albach and Fewel 1965][research_albach_fewel_1965]\] \[[Alcedo 1980][research_alcedo_1980]\] \[[Alexeev et al 2023][research_alexeev_zemlyanyy_2023]\] \[[Allen et al 1962][research_allen_1962]\] \[[Alroqi and Wang 2017][research_alroqi_wang_2017]\] \[[An et al 2023][research_an_liu_2023]\] \[[Arnaldo Valdés et al 2011][research_arnaldovaldes_gomezcomendador_2011]\] \[[Arreola-Nepomuceno et al 2025][research_arreolanepomuceno_valdez_2025]\] \[[Aspidova et al 2022][research_aspidova_eremin_2022]\] \[[Asthana and Bhat 2012][research_asthana_bhat_2012]\] \[[Attri 1969][research_attri_1969]\] \[[Baimukhametov and White 2026][research_baimukhametov_white_2026]\] \[[Bakulin et al 2016][research_bakulin_borzykh_2016]\] \[[Banerjee and Padhi 2015][research_banerjee_padhi_2015]\] \[[Barnes et al 2007][research_barnes_mcmichael_2007]\] \[[Batill 1982][research_batill_1982]\] \[[Batterbee et al 2007][research_batterbee_sims_2007]\] \[[Beachem 1964][research_beachem_1964]\] \[[Benedetto et al 2014][research_benedetto_damico_2014]\] \[[Berry 1999][research_berry_1999]\] \[[Berry 2000][research_berry_2000]\] \[[Bhagat et al 2011][research_bhagat_glussich_2011]\] \[[Black 1964][research_black_1964]\] \[[Blanchard 1961][research_blanchard_1961]\] \[[Bourne and Kirsten 1983][research_bourne_1983]\] \[[Brando et al 2016][research_brando_dannier_2016]\] \[[Brassard et al 2019][research_brassard_laforte_2019]\] \[[Brown and Redwine 1948][research_brown_1948]\] \[[Brusa et al 2025][research_brusa_delprete_2025]\] \[[Bukov and Bykov 2017][research_bukov_bykov_2017]\] \[[Burgan and Paddison 1974][research_burgan_1974]\] \[[Burton 1981][research_burton_1981]\] \[[Butter 2017][research_butter_2017]\] \[[Cai et al 2024][research_cai_lei_2024]\] \[[Callerio 1940][research_callerio_1940]\] \[[Campi et al 2019][research_campi_cruciani_2019]\] \[[Caves and Kirkland 1999][research_caves_kirkland_1999]\] \[[Cejpek 2018][research_cejpek_2018]\] \[[Cetinkaya and Ozkol 2017][research_cetinkaya_ozkol_2017]\] \[[Chai and Mason 1996][research_chai_mason_1996]\] \[[Chaloff et al 1974][research_chaloff_1974]\] \[[Chang et al 2016][research_chang_yang_2016]\] \[[Chang 2016][research_chang_2016]\] \[[Chen et al 2013][research_chen_nie_2013]\] \[[Chen and Xue 2023][research_chen_xue_2023]\] \[[Chen 2023][research_chen_2023]\] \[[Chi et al 2009][research_chi_xiaopeng_2009]\] \[[Chinvorarat 2021][research_chinvorarat_2021]\] \[[Chinvorarat and Vallikul 2021][research_chinvorarat_vallikul_2021]\] \[[Choong and Lim 2026][research_choong_lim_2026]\] \[[Chu et al 2016][research_chu_guo_2016]\] \[[Chu et al 2024][research_chu_liu_2024]\] \[[Chu et al 2025][research_chu_lv_2025]\] \[[Chuang et al 2021][research_chuang_yubing_2021]\] \[[Crist and Symes 1981][research_crist_symes_1981]\] \[[Currey 1969][research_currey_1969]\] \[[D'Andrea et al 2022][research_dandrea_didomenico_2022]\] \[[Daoxin 2021][research_daoxin_2021]\] \[[Daugherty et al 1988][research_daugherty_yager_1988]\] \[[Daugherty and Stubbs 1992][research_daugherty_stubbs_1992]\] \[[Deloach et al 2009][research_deloach_2009]\] \[[Delprete et al 2023][research_delprete_dagna_2023]\] \[[Di Leo et al 2018][research_dileo_leon_2018]\] \[[Digges 1971][research_digges_1971]\] \[[Distefano and Leonardi 2018][research_distefano_leonardi_2018]\] \[[Di̇nç 2021][research_dinc_2021]\] \[[Douglas et al 2021][research_douglas_ellis_2021]\] \[[Duda et al 2022][research_duda_deuring_2022]\] \[[Durmuşoğlu 2026][research_durmusoglu_2026]\] \[[Durán-Giraldo et al 2022][research_durangiraldo_gonzalezsierra_2022]\] \[[Earl 1967][research_earl_1967]\] \[[Eldred 1953][research_eldred_1953]\] \[[Erasmus et al 2014][research_erasmus_hattingh_2014]\] \[[Fahaz Firoz et al 2023][research_fahazfiroz_rupikaraj_2023]\] \[[Fan and Wang 2007][research_fan_wang_2007]\] \[[Fasanella et al 1984][research_fasanella_1984]\] \[[Fasanella et al 2004][research_fasanella_2004]\] \[[Fasanella et al 2012][research_fasanella_2012]\] \[[Feld 1968][research_feld_1968]\] \[[Fenwick 1966][research_fenwick_1966_c]\] \[[Fenwick 1967][research_fenwick_1967]\] \[[Fisher 1960][research_fisher_1960]\] \[[Frank et al 2014][research_frank_durand_2014]\] \[[Frisby 1960][research_frisby_1960]\] \[[Fu et al 2023][research_fu_hang_2023]\] \[[Furnish and Anders 1971][research_furnish_anders_1971]\] \[[Gan et al 2021][research_gan_fang_2021_b]\] \[[Gan et al 2021][research_gan_fang_2021]\] \[[Gandhewar and Sonkusare 2014][research_gandhewar_gsonkusare_2014]\] \[[Gao et al 2023][research_gao_sun_2023]\] \[[Gao et al 2025][research_gao_wang_2025]\] \[[Gaétan 2009][research_gaetan_2009]\] \[[Ghods et al 2024][research_ghods_khalesi_2024]\] \[[Gong et al 2025][research_gong_chen_2025]\] \[[Goodall 1977][research_goodall_1977]\] \[[Green 2015][research_green_2015]\] \[[Groomes 1964][research_groomes_1964]\] \[[Guida 2023][research_guida_2023]\] \[[Gupta et al 2025][research_gupta_sai_2025]\] \[[Habas et al 2022][research_habas_alattar_2022]\] \[[Hailiang and Lixin 2015][research_hailiang_lixin_2015]\] \[[Hamilton et al 1980][research_hamilton_1980]\] \[[Han et al 2022][research_han_jiao_2022]\] \[[Han 2025][research_han_2025]\] \[[Hinchey 1968][research_hinchey_1968]\] \[[Ho and Romero 2013][research_ho_romero_2013]\] \[[Hoess et al 1963][research_hoess_voorhees_1963]\] \[[Hoffman et al 1961][research_hoffman_1961]\] \[[Hollinger 1958][research_hollinger_1958]\] \[[Hong et al 2016][research_hong_dilshod_2016]\] \[[Hong et al 2016][research_hong_dilshod_2016_b]\] \[[Hoole et al 2020][research_hoole_sartor_2020]\] \[[Hou et al 2020][research_hou_zhang_2020]\] \[[Huang 2019][research_huang_2019]\] \[[Huang and Jia 2018][research_huang_jia_2018]\] \[[Huang et al 2016][research_huang_nie_2016]\] \[[Huang et al 2019][research_huang_liu_2019]\] \[[Huili et al 2023][research_huili_xiying_2023]\] \[[Iwabuchi and Minesugi 2026][research_iwabuchi_minesugi_2026]\] \[[Jackson and Fasanella 2004][research_jackson_2004]\] \[[Jackson and Fasanella 2004][research_jackson_2004_b]\] \[[Jackson and Fasanella 2004][research_jackson_2004_c]\] \[[Jackson and Fasanella 2016][research_jackson_2016]\] \[[Jackson et al 2003][research_jackson_2003]\] \[[Jackson et al 2018][research_jackson_2018]\] \[[Jackson et al 2018][research_jackson_2018_b]\] \[[Jamal-Eddine 2025][research_jamaleddine_2025]\] \[[Jamieson and White 2019][research_jamieson_white_2019]\] \[[Jamieson and White 2021][research_jamieson_white_2021]\] \[[Jebáček and Horák 2016][research_jebacek_horak_2016]\] \[[Jenkins and Donovan 1942][research_jenkins_donovan_1942]\] \[[Jenkins and Donovan 1942][research_jenkins_donovan_1942_b]\] \[[Ji Teng and Shahneh 2018][research_jiteng_shahneh_2018]\] \[[Jia et al 2011][research_jia_han_2011]\] \[[Jia et al 2019][research_jia_jizhen_2019]\] \[[Jiang and Wang 2023][research_jiang_wang_2023]\] \[[Jiang 2011][research_jiang_2011]\] \[[Jiao et al 2017][research_jiao_liu_2017]\] \[[Jobmann and Thielecke 2024][research_jobmann_thielecke_2024]\] \[[Joel P and Dr. Vijayan 2014][research_joelp_r_2014]\] \[[Jones and Boiffier 2011][research_jones_boiffier_2011]\] \[[Joshi et al 2015][research_joshi_jeon_2015]\] \[[Joyner 1969][research_joyner_1969]\] \[[Joyner 1970][research_joyner_1970]\] \[[Kadam et al 2018][research_kadam_sathish_2018]\] \[[Kang and Choi 2024][research_kang_choi_2024]\] \[[Kansas Univ Lawrence 1952][research_lawrence_1952]\] \[[Kellas 2017][research_kellas_2017]\] \[[Ketabdari et al 2020][research_ketabdari_toraldo_2020]\] \[[Khan et al 2021][research_khan_mehmood_2021]\] \[[Kim et al 2014][research_kim_kim_2014]\] \[[Kim et al 2015][research_kim_shin_2015]\] \[[Kim et al 2018][research_kim_han_2018]\] \[[Kim et al 2021][research_kim_jeong_2021]\] \[[kim hyunsu and Je-hyung Jeon 2018][research_kimhyunsu_jehyungjeon_2018]\] \[[Kling and Hornung 2019][research_kling_hornung_2019]\] \[[Kolnick and Morris 1955][research_kolnick_1955]\] \[[Krabacher 1993][research_krabacher_1993]\] \[[Krishnan et al 2017][research_krishnan_thejus_2017]\] \[[Krüger et al 1997][research_kruger_besselink_1997]\] \[[Kuchinka 1965][research_kuchinka_1965]\] \[[Kumar et al 2024][research_kumar_dhanush_2024]\] \[[Kumar 2010][research_kumar_2010]\] \[[Laforte et al 2015][research_laforte_wesley_2015]\] \[[Landing Strip-Sierra Nevada 2020][research_landing_stripsierra_2020]\] \[[Langberg et al 2022][research_langberg_tyler_2022]\] \[[Larson and Wilson 1967][research_larson_1967]\] \[[Larson 1972][research_larson_1972]\] \[[Lavender 1965][research_lavender_1965]\] \[[Lee et al 1973][research_lee_1973]\] \[[Lee et al 2022][research_lee_payan_2022]\] \[[Lee and Swegle 1963][research_lee_1963]\] \[[Lee 2009][research_lee_2009]\] \[[Lee 2023][research_lee_2023]\] \[[Lei and Liu 2026][research_lei_liu_2026]\] \[[Leland and Taylor 1964][research_leland_taylor_1964]\] \[[Li et al 2013][research_li_cui_2013]\] \[[Li et al 2017][research_li_jiang_2017]\] \[[Li et al 2023][research_li_zhang_2023]\] \[[Li et al 2023][research_li_sun_2023]\] \[[Li et al 2024][research_li_angelov_2024]\] \[[Li et al 2024][research_li_xia_2024]\] \[[Li and Wu 2024][research_li_wu_2024]\] \[[Liseitsev 2025][research_liseitsev_2025]\] \[[Littell and Kellas 2018][research_littell_2018]\] \[[Littell et al 2007][research_littell_2007]\] \[[Littell et al 2015][research_littell_2015]\] \[[Liu et al 2017][research_liu_chen_2017]\] \[[Liu et al 2023][research_liu_wang_2023]\] \[[Liu et al 2025][research_liu_sun_2025]\] \[[Liu et al 2025][research_liu_liu_2025]\] \[[Logan 1976][research_logan_1976]\] \[[Logan et al 1978][research_logan_1978]\] \[[Lu and Lei 2010][research_lu_lei_2010]\] \[[Lu et al 2010][research_lu_wang_2010]\] \[[Lu and Tao 2025][research_lu_tao_2025]\] \[[Luong et al 2025][research_luong_le_2025]\] \[[Lystad 1975][research_lystad_1975]\] \[[Ma et al 2013][research_ma_sun_2013]\] \[[Ma et al 2013][research_ma_wu_2013]\] \[[Macy et al 1989][research_macy_shea_1989]\] \[[Maeda et al 2014][research_maeda_otsuki_2014]\] \[[Maeda et al 2016][research_maeda_otsuki_2016]\] \[[Maemori et al 2003][research_maemori_tanigawa_2003]\] \[[Mark 2009][research_mark_2009]\] \[[Marylin et al 2007][research_marylin_christian_2007]\] \[[Mason et al 2021][research_mason_zahn_2021]\] \[[Mathew et al 2023][research_mathew_dutta_2023]\] \[[Mazur 2020][research_mazur_2020]\] \[[McCown-McClintick and Orr 2000][research_mccown_mcclintick_2000]\] \[[McGehee et al 1959][research_mcgehee_1959]\] \[[Mehmood et al 2021][research_mehmood_majeed_2021]\] \[[Meriwether and Harris 1962][research_meriwether_1962]\] \[[Midtfjord and Huseby 2020][research_midtfjord_huseby_2020]\] \[[Mikhailov and Nedel'ko 2012][research_mikhailov_nedelko_2012_b]\] \[[Mikhailov and Nedel'ko 2012][research_mikhailov_nedelko_2012]\] \[[Mohaghegh 2025][research_mohaghegh_2025]\] \[[Mosby 1965][research_mosby_1965]\] \[[Muehter 1974][research_muehter_1974]\] \[[Muhammad Hadi Widanto et al 2025][research_muhammadhadiwidanto_rizkifitriansyah_2025]\] \[[Nadan and Lee 2018][research_nadan_lee_2018]\] \[[Nagarani et al 2020][research_nagarani_venkatakrishnan_2020]\] \[[Nanda et al 2025][research_nanda_gopalakrishna_2025]\] \[[Nazir et al 2018][research_nazir_aziz_2018]\] \[[Nedel'ko and Alimov 2018][research_nedelko_alimov_2018]\] \[[Neumaier et al 2022][research_neumaier_kranemann_2022]\] \[[Novakovic 2014][research_novakovic_2014]\] \[[O`Callaghan 2016][research_ocallaghan_2016]\] \[[Okafor et al 2018][research_okafor_jemitola_2018]\] \[[Oza et al 2015][research_oza_hu_2015]\] \[[Padmanabhan and Dowell 2015][research_padmanabhan_dowell_2015]\] \[[Paquita et al 2024][research_paquita_persadanta_2024]\] \[[Pasindu and Fwa 2015][research_pasindu_fwa_2015]\] \[[Pasindu 2020][research_pasindu_2020]\] \[[Paul et al 2019][research_paul_suresh_2019]\] \[[Peck][research_peck_nd]\] \[[Perry and Schneider 1984][research_perry_schneider_1984]\] \[[Peter and Umap 2021][research_peter_umap_2021]\] \[[Phillips et al 1973][research_phillips_1973]\] \[[Pi 1988][research_pi_1988]\] \[[Pipenberg et al 2019][research_pipenberg_keennon_2019]\] \[[Pirooz et al 2021][research_pirooz_mirmahdi_2021]\] \[[Pollack and Urch 1991][research_pollack_urch_1991]\] \[[Pouly et al 2009][research_pouly_lauffenburger_2009]\] \[[Pouya and Saghafi 2009][research_pouya_saghafi_2009]\] \[[Pragadheswaran and Balguri 2015][research_pragadheswaran_balguri_2015]\] \[[Pritchard 2001][research_pritchard_2001]\] \[[Putnam and Gardner][research_putnam_nd]\] \[[Putov et al 2015][research_putov_putov_2015]\] \[[Putov et al 2016][research_putov_putov_2016]\] \[[Pytka 2023][research_pytka_2023]\] \[[Qi et al 2025][research_qi_zhao_2025]\] \[[Qi et al 2026][research_qi_liu_2026]\] \[[Qian and Wang 2022][research_qian_wang_2022]\] \[[Karthikeyan et al 2022][research_r_sridhar_2022]\] \[[Ralph 1999][research_ralph_1999]\] \[[Ramirez et al 2025][research_ramirez_dux_2025]\] \[[Rammon and Nirbito 2019][research_rammon_nirbito_2019]\] \[[Rao et al 2022][research_rao_zhang_2022]\] \[[Reiser et al 2024][research_reiser_villani_2024]\] \[[Ren et al 2018][research_ren_wang_2018]\] \[[Ren et al 2023][research_ren_wang_2023]\] \[[Richards and Erickson 2019][research_richards_erickson_2019]\] \[[Richards and Tate 2023][research_richards_tate_2023]\] \[[Ridha 1968][research_ridha_1968]\] \[[Rogers 1973][research_rogers_1973]\] \[[Saff and Rosenfeld 1982][research_saff_rosenfeld_1982]\] \[[Sanders 1972][research_sanders_1972]\] \[[Sankar 2012][research_sankar_2012]\] \[[Saputra 2017][research_saputra_2017]\] \[[Scholz et al 2026][research_scholz_theuser_2026]\] \[[Sen 1990][research_sen_1990_b]\] \[[Sen 1990][research_sen_1990]\] \[[Senpheng and Ruchanurucks 2015][research_senpheng_ruchanurucks_2015]\] \[[Sforza 2014][research_sforza_2014]\] \[[Shafa et al 2011][research_shafa_cunio_2011]\] \[[Shao et al 2020][research_shao_yang_2020]\] \[[Sharf and Monterrubio 1999][research_sharf_monterrubio_1999]\] \[[Shi et al 2016][research_shi_tanigawa_2016]\] \[[Shi et al 2026][research_shi_li_2026]\] \[[Shin and Kim 2013][research_shin_kim_2013]\] \[[Shrotri and Schrage 2009][research_shrotri_schrage_2009_b]\] \[[Shrotri and Schrage 2009][research_shrotri_schrage_2009]\] \[[Shuhua Zhu et al 2008][research_shuhuazhu_mingbotong_2008]\] \[[Shukla 2024][research_shukla_2024]\] \[[Si et al 2024][research_si_zhao_2024]\] \[[Siboro et al 2023][research_siboro_zainul_2023]\] \[[Silsby 1956][research_silsby_1956]\] \[[Silsby and Harrin 1955][research_silsby_1955]\] \[[Silsby et al 1953][research_silsby_1953]\] \[[Singh et al 2021][research_singh_chaudhary_2021]\] \[[Sivakumar and Syedhaleem 2018][research_sivakumar_syedhaleem_2018]\] \[[Song and Wang 2025][research_song_wang_2025]\] \[[Sonowal et al 2021][research_sonowal_pandey_2021]\] \[[Sotirios and Jackson 2008][research_sotirios_2008]\] \[[Sreeletha et al 2019][research_sreeletha_noble_2019]\] \[[Stachiw et al 2020][research_stachiw_khouli_2020]\] \[[Stalnov et al 2013][research_stalnov_angland_2013]\] \[[Stickle 1961][research_stickle_1961]\] \[[Stickle and Silsby 1960][research_stickle_1960]\] \[[Strelets et al 2023][research_strelets_tarasov_2023]\] \[[Sun 2026][research_sun_2026]\] \[[Suszyński et al 2025][research_suszynski_kowalski_2025]\] \[[Swamy and Zebenay 2021][research_swamy_zebenay_2021]\] \[[Taylor 1958][research_taylor_1958]\] \[[Tho and Wang 2009][research_tho_wang_2009]\] \[[Tian and Sun 2014][research_tian_sun_2014]\] \[[Tire Overspeed Landing Test][research_tire_overspeed_nd]\] \[[Titov and Serebryanskiy 2023][research_titov_serebryanskiy_2023]\] \[[Titov and Serebryansky 2023][research_titov_serebryansky_2023_b]\] \[[Titov and Serebryansky 2023][research_titov_serebryansky_2023]\] \[[Titov and Serebryansky 2026][research_titov_serebryansky_2026]\] \[[Tomac et al 2016][research_tomac_rizzi_2016]\] \[[Toraldo et al 2023][research_toraldo_ketabdari_2023]\] \[[Tripathi et al 2018][research_tripathi_patel_2018]\] \[[Tripathi et al 2024][research_tripathi_patel_2024]\] \[[Tripathi et al 2024][research_tripathi_kumarsinha_2024]\] \[[Tsapparellas et al 2023][research_tsapparellas_jelev_2023]\] \[[Udayakumar and Ibrahim 2019][research_udayakumar_ibrahim_2019]\] \[[van den Broek et al 2025][research_vandenbroek_simpson_2025]\] \[[van den Broek et al 2026][research_vandenbroek_hunns_2026]\] \[[Van Es 2017][research_vanes_2017]\] \[[Vassilakos et al 2011][research_vassilakos_2011]\] \[[Veaux 1988][research_veaux_1988]\] \[[Vijayanandh et al 2020][research_vijayanandh_kiran_2020]\] \[[Viscardi et al 2021][research_viscardi_arena_2021]\] \[[Wahi and Straub 1977][research_wahi_straub_1977]\] \[[Walton 2025][research_walton_2025]\] \[[Wang and Chen 2019][research_wang_chen_2019]\] \[[Wang and Holzapfel 2018][research_wang_holzapfel_2018]\] \[[Wang et al 2005][research_wang_peng_2005]\] \[[Wang et al 2007][research_wang_jau_2007]\] \[[Wang et al 2016][research_wang_wang_2016]\] \[[Wang et al 2016][research_wang_yu_2016]\] \[[Wang et al 2024][research_wang_yin_2024]\] \[[Wang et al 2024][research_wang_feng_2024]\] \[[Wang et al 2025][research_wang_mu_2025]\] \[[Wang et al 2026][research_wang_zhang_2026]\] \[[Wang Shihao et al 2018][research_wangshihao_yanzilin_2018]\] \[[Wang 2016][research_wang_2016]\] \[[Wang 2022][research_wang_2022_b]\] \[[Wang 2024][research_wang_2024]\] \[[Watson et al 1981][research_watson_1981]\] \[[Wei and Nie 2005][research_wei_2005]\] \[[Wei et al 2026][research_wei_diaz_2026]\] \[[Wijaya and Nurrohmad 2020][research_wijaya_nurrohmad_2020]\] \[[Wilson 1967][research_wilson_1967]\] \[[Wilson 1980][research_wilson_1980]\] \[[Witte et al 2016][research_witte_roll_2016]\] \[[Wong et al 2017][research_wong_ryan_2017]\] \[[Wood et al 2012][research_wood_2012]\] \[[Wood 1968][research_wood_1968]\] \[[Wu et al 2022][research_wu_shi_2022]\] \[[Xiao 2022][research_xiao_2022]\] \[[Xie and Li 2016][research_xie_li_2016]\] \[[Xin 2021][research_xin_2021]\] \[[Yadav and Ramamoorthy 1991][research_yadav_ramamoorthy_1991]\] \[[Yager 1983][research_yager_1983]\] \[[Yager 1991][research_yager_1991]\] \[[Yang et al 2022][research_yang_wu_2022]\] \[[Yang and Yanguang 2015][research_yang_yanguang_2015]\] \[[Yao et al 2022][research_yao_ma_2022]\] \[[Yassir Fadhilah et al 2024][research_yassirfadhilah_mubarok_2024]\] \[[Yin et al 2024][research_yin_li_2024]\] \[[Yntema and Milwitzky 1952][research_yntema_1952]\] \[[Yongsheng 2021][research_yongsheng_2021]\] \[[Yongsheng 2021][research_yongsheng_2021_b]\] \[[Zakrajsek et al 2017][research_zakrajsek_vogel_2017]\] \[[Zammit-Mangion et al 2006][research_zammitmangion_zammit_2006]\] \[[Zhang and Yang 2015][research_zhang_yang_2015]\] \[[Zhang et al 2016][research_zhang_sun_2016]\] \[[Zhang et al 2019][research_zhang_wei_2019]\] \[[Zhang et al 2020][research_zhang_nie_2020]\] \[[Zhang et al 2026][research_zhang_chen_2026]\] \[[Zhang et al 2026][research_zhang_yuan_2026]\] \[[Zhang and Wang 2024][research_zhang_wang_2024]\] \[[Zhang 2011][research_zhang_2011]\] \[[Zhao et al 2011][research_zhao_cui_2011]\] \[[Zhao et al 2016][research_zhao_wang_2016]\] \[[Zhao and Zhao 2024][research_zhao_zhao_2024]\] \[[Zheng and Yin 2025][research_zheng_yin_2025]\] \[[Zheng 2021][research_zheng_2021]\] \[[Zhicong and Voronko 2023][research_zhicong_voronko_2023]\] \[[Zhongping 2023][research_zhongping_2023]\] \[[Zhou et al 2024][research_zhou_zuo_2024]\] \[[Zhou and Wang 2012][research_zhou_wang_2012]\] \[[Zhu and Wang 2025][research_zhu_wang_2025]\] \[[Zwirglmaier et al 2014][research_zwirglmaier_drees_2014]\] \[[Çabuk 2021][research_cabuk_2021]\] \[[Çabuk 2023][research_cabuk_2023]\] \[[Štumper et al 2015][research_stumper_kraus_2015]\] \[[Яцковий and Вірченко, 2017, modeling of design and technological parameters of the airplane landing gear][research_modeling_of_design_2017]\]

### Demonstrator Programmes and Risk Reduction

**Whether a demonstrator is worth building is the frame in which a one million dollar test article that flew eight times should be judged.** The cluster gathers flight test programmes, their planning and instrumentation, and technology demonstrators.

Of its 248 titles, 206 concern flight test programmes, flight testing or test instrumentation, and 18 name cost, value, benefit, economics or risk reduction. **How to test a demonstrator is asked far more often than whether to build one.**

**248 records.** \[[1970, Flight Test Programme][research_flight_test_1970]\] \[[1990, ORBITEC Orbital Technology Demonstration Program][research_orbitec_orbital_1990]\] \[[2002, Titan II Operational Flight Test and Evaluation Programs History][research_titan_ii_2002]\] \[[2023, Technology Demonstrator, Close Air Support, and Legacy Programs][research_technology_demonstrator_2023]\] \[[2026, Design validation and verification for non-intrusive flight test instrumentation NIFTI using Model-Based Systems Engineering MBSE][research_design_validation_2026]\] \[[A Typical Avionics Integration Flight Test Program][research_a_typical]\] \[[Jacob da Motta 2020][research_ajacobdamotta_2020]\] \[[Adelgren et al 2004][research_adelgren_2004]\] \[[Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990]\] \[[Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991]\] \[[Air Force Test Pilot School Edwards Afb Ca 1993][research_airforcetestpilotschooledwardsafbca_1993]\] \[[Alaverdi and Paris 2001][research_alaverdi_2001]\] \[[Alexander 1979][research_alexander_1979]\] \[[Alich and Castillo 2007][research_alich_castillo_2007]\] \[[Almeida 2011][research_almeida_2011]\] \[[Ambrosio et al 2026][research_ambrosio_camargo_2026]\] \[[Anderson et al 1983][research_anderson_vincent_1983]\] \[[Andreeva-Mori et al][research_andreeva_mori_nd]\] \[[Armstrong 1977][research_armstrong_1977]\] \[[Arnold 1981][research_arnold_1981]\] \[[Asher et al 2013][research_asher_2013]\] \[[Barnhart et al 2007][research_barnhart_sullivan_2007]\] \[[Barton and Culp 1985][research_barton_1985]\] \[[Bekar et al 2025][research_bekar_tanyeri_2025]\] \[[Bender 1969][research_bender_1969]\] \[[Bennett and Abel 1981][research_bennett_abel_1981]\] \[[Benyamen and Keshmiri 2022][research_benyamen_2022]\] \[[Berg 1966][research_berg_1966]\] \[[Bieniawski et al 2014][research_bieniawski_rosenzweig_2014]\] \[[Bleimeyer 1981][research_bleimeyer_1981]\] \[[Blevins et al 2022][research_blevins_mckinnis_2022]\] \[[Bolt 1981][research_bolt_1981]\] \[[Boothe et al 1974][research_boothe_chen_1974]\] \[[Brand 1981][research_brand_1981]\] \[[Bratt 1965][research_bratt_1965]\] \[[Brennan and McDaniel 1994][research_brennan_mcdaniel_1994]\] \[[Brieger et al 2008][research_brieger_ossmann_2008]\] \[[Brooks 1986][research_brooks_1986]\] \[[Bufalino 1995][research_bufalino_1995]\] \[[Bunge et al 2015][research_bunge_munerasavino_2015]\] \[[Burgess 1970][research_burgess_1970]\] \[[Burns 1992][research_burnsiii_1992]\] \[[Cady and Olsen 1996][research_cady_olsen_1996]\] \[[Cady 1997][research_cady_1997]\] \[[Call et al 1981][research_call_kelly_1981]\] \[[Campbell and Kresge 2003][research_campbell_kresge_2003]\] \[[Campbell et al 2007][research_campbell_lee_2007]\] \[[Camponogara et al 2019][research_camponogara_oliveira_2019]\] \[[Cassell et al 2019][research_cassell_2019]\] \[[Chao et al 2017][research_chao_2017]\] \[[Cheney 1988][research_cheney_1988]\] \[[Cho and Nagati 1995][research_cho_1995]\] \[[Clarke and Randall 1997][research_clarke_randall_1997]\] \[[Clough 1990][research_clough_1990]\] \[[Coker et al 1978][research_coker_hoffman_1978]\] \[[Colgren 1996][research_colgren_1996]\] \[[Cook 1981][research_cook_1981]\] \[[Coskun and Genc 2021][research_coskun_genc_2021]\] \[[Currin et al 2011][research_currin_2011]\] \[[Curtiss and Zhao 1988][research_curtiss_1988]\] \[[Davis 1989][research_davis_1989]\] \[[Deel et al 1972][research_deel_1972]\] \[[Deets and Brown 1986][research_deets_1986]\] \[[Demo 1986][research_demo_1986]\] \[[Depaola et al 2018][research_depaola_chimento_2018]\] \[[Donelson et al 1989][research_donelson_lewerenz_1989]\] \[[Droege 1947][research_droege_1947]\] \[[Dunn 1990][research_dunn_1990]\] \[[Durbin 1959][research_durbin_1959]\] \[[Dwyer 1994][research_dwyer_1994]\] \[[Edwards 1981][research_edwards_1981]\] \[[Eilertson 1975][research_eilertson_1975]\] \[[Ellery et al 2006][research_ellery_richter_2006]\] \[[Fegely et al 2016][research_fegely_tischler_2016]\] \[[Flight Test Results Pertaining 1970][research_flight_test_1970_b]\] \[[Fralish 1998][research_fralish_1998]\] \[[Frinell 1983][research_frinell_1983]\] \[[Fu et al 2022][research_fu_shi_2022]\] \[[Förder and Steiner 2020][research_forder_steiner_2020]\] \[[Galloway et al 1998][research_galloway_slivinsky_1998]\] \[[Geister et al 2017][research_geister_2017]\] \[[Godwin et al 1964][research_godwin_frazier_1964]\] \[[Grauer et al 2017][research_grauer_morelli_2017]\] \[[Gray 2016][research_gray_2016]\] \[[Green and Fernandez 1994][research_green_fernandez_1994]\] \[[Guerrero et al 2022][research_guerrero_pelluault_2022]\] \[[Gupta 2023][research_gupta_2023]\] \[[Haberbusch and Walls 2008][research_haberbusch_walls_2008]\] \[[Hahne and Fremaux 2008][research_hahne_2008]\] \[[Hall][research_hall_nd]\] \[[Hall et al 1999][research_hall_1999]\] \[[Hardy 1983][research_hardy_1983]\] \[[Hart 1992][research_hart_1992]\] \[[Havey and Ferguson 1990][research_havey_ferguson_1990]\] \[[Hepler et al 1973][research_hepler_1973]\] \[[Hicks and Matheny 1987][research_hicks_matheny_1987]\] \[[Hiliuta and Botez 2006][research_hiliuta_botez_2006]\] \[[Hill and Huhlein 1993][research_hill_huhlein_1993]\] \[[Hillaker 1983][research_hillaker_1983]\] \[[Hillaker 1983][research_hillaker_1983_b]\] \[[Hoffelner et al 2023][research_hoffelner_maly_2023]\] \[[Holberg and Grabowsky 1981][research_holberg_grabowsky_1981]\] \[[Hopping et al 1986][research_hopping_counts_1986]\] \[[Horton et al 1964][research_horton_1964]\] \[[Howland 1953][research_howland_1953]\] \[[Huang and Wang 2015][research_huang_wang_2015]\] \[[Huebner et al 2001][research_huebner_rock_2001]\] \[[Huebner et al 2001][research_huebner_rock_2001_b]\] \[[Hughes and Chrispin 1988][research_hughes_chrispin_1988]\] \[[Hummer et al 2018][research_hummer_jurkovich_2018]\] \[[Ide and Landman 2025][research_ide_landman_2025]\] \[[Jackson and Coyle 1983][research_jackson_coyle_1983]\] \[[Jann and Greiner-Perth 2009][research_jann_greinerperth_2009]\] \[[Janssens and Kimberlin 2000][research_janssens_2000]\] \[[Jarvis 1989][research_jarvis_1989]\] \[[Jensen et al 2020][research_jensen_coy_2020]\] \[[Jia and Wang 2024][research_jia_wang_2024]\] \[[Ju et al 2024][research_ju_jiang_2024]\] \[[Juhasz et al 2020][research_juhasz_xin_2020]\] \[[Kannan et al][research_kannan_nd]\] \[[Kirsten and Ash 1974][research_kirsten_1974]\] \[[Kish et al 2017][research_kish_rhoney_2017]\] \[[Kobald et al 2017][research_kobald_fischer_2017]\] \[[Kobald et al 2018][research_kobald_fischer_2018]\] \[[Koenig and Harris 2017][research_koenig_harris_2017]\] \[[Kohlman et al 1987][research_kohlman_schweikhard_1987]\] \[[Kohrs 1982][research_kohrs_1982]\] \[[Kreutz 1971][research_kreutz_1971]\] \[[Krumenacker and Pellicano 1992][research_krumenacker_pellicano_1992]\] \[[Kuppuswamy and Kiran 1981][research_kuppuswamy_kiran_1981]\] \[[Kwon and Park 2013][research_kwon_park_2013]\] \[[Lamy 1983][research_lamy_1983]\] \[[Larsson et al 2020][research_larsson_2020]\] \[[Le 2025][research_le_2025]\] \[[Lee et al 1998][research_lee_chang_1998]\] \[[Lee et al 2011][research_lee_park_2011]\] \[[Lewerenz 1987][research_lewerenz_1987]\] \[[Lieberman 1963][research_lieberman_1963]\] \[[Liu 2025][research_liu_2025_b]\] \[[Long 1968][research_long_1968]\] \[[Lovell and Parlett 1956][research_lovell_1956]\] \[[Lovtsov and Karpov 2011][research_lovtsov_karpov_2011]\] \[[Lu et al 2017][research_lu_harris_2017]\] \[[Luria and Guyton 1992][research_luria_guyton_1992]\] \[[Machnik et al 2022][research_machnik_decker_2022]\] \[[Macmillan 1981][research_macmillan_1981]\] \[[Mangum 1965][research_mangum_1965]\] \[[Mannai 1962][research_mannai_1962]\] \[[Manning and Gleason 1992][research_manning_gleason_1992]\] \[[Manning et al 1992][research_manning_baum_1992]\] \[[Martínez Morán 2018][research_martinezmoran_2018]\] \[[Mayhue 1962][research_mayhue_1962]\] \[[McNally and Bach 1988][research_mcnally_1988]\] \[[McTigue and Ryan 1968][research_mctigue_ryan_1968]\] \[[Mead 1998][research_mead_1998]\] \[[Melgaard 1986][research_melgaard_1986]\] \[[Meyers et al 1968][research_meyers_tompkins_1968]\] \[[Minor et al 2004][research_minor_2004]\] \[[Mitchell 2004][research_mitchell_2004]\] \[[Monteil 2024][research_monteil_2024]\] \[[Moorhouse 1990][research_moorhouse_1990]\] \[[Moorhouse 1994][research_moorhouse_1994]\] \[[Morgenfeld 1992][research_morgenfeld_1992]\] \[[Motaghedi 2003][research_motaghedi_2003]\] \[[Mouritsen 1994][research_mouritsen_1994]\] \[[Neumannn et al 2016][research_neumannn_moore_2016]\] \[[Nial 1972][research_nial_1972]\] \[[Niehaus 1962][research_niehaus_1962]\] \[[Niewald and Parker 1999][research_niewald_parker_1999]\] \[[Nippress and Wilson 1992][research_nippress_wilson_1992]\] \[[Painter and Sitterle 1972][research_painter_1972]\] \[[Palomino 2022][research_palomino_2022]\] \[[Pausder et al 1983][research_pausder_meyer_1983]\] \[[Pavlinsky 1993][research_pavlinsky_1993]\] \[[Petersen 1981][research_petersen_1981]\] \[[Ponton and Warnes 2007][research_ponton_warnes_2007]\] \[[Prahl 1968][research_prahl_1968]\] \[[Pérez Rus and Le Gal 2024][research_perezrus_legal_2024]\] \[[Randolph et al 2015][research_randolph_mullenax_2015]\] \[[Rediess and Melton 1994][research_rediess_1994]\] \[[Ricciardi and Minwalla 2016][research_ricciardi_minwalla_2016]\] \[[Rice and Hazlwood 1994][research_rice_hazlwood_1994]\] \[[Rice and Locksley 2000][research_rice_locksley_2000]\] \[[Rice 1946][research_rice_1946]\] \[[Rimmer 1952][research_rimmer_1952]\] \[[Roberts 1988][research_roberts_1988]\] \[[Roberts 1990][research_roberts_1990]\] \[[Robertson and Hartfield 1992][research_robertson_1992]\] \[[Rusbarsky 1990][research_rusbarsky_1990]\] \[[Sabatini 2014][research_sabatini_2014]\] \[[Sahasrabudhe et al 2011][research_sahasrabudhe_pritchard_2011]\] \[[Sanderson 1965][research_sanderson_1965]\] \[[Schifferle et al 1999][research_schifferle_deppe_1999]\] \[[Schneider et al 2012][research_schneider_larson_2012]\] \[[Schrader 2023][research_schrader_2023]\] \[[Sefic and Cutler 1986][research_sefic_cutler_1986]\] \[[Shaw and Richter 1985][research_shaw_richter_1985]\] \[[Shields 1981][research_shields_1981]\] \[[Shim et al 2023][research_shim_park_2023]\] \[[Simpson 1972][research_simpson_1972]\] \[[Simulation in support of 1988][research_simulation_support_1988]\] \[[Slivinsky et al 1995][research_slivinsky_breitling_1995]\] \[[Smith et al 1994][research_smith_purvis_1994]\] \[[Song et al 2020][research_song_liu_2020]\] \[[Stiles 2022][research_stiles_2022]\] \[[Stottier 1995][research_stottier_1995]\] \[[Stout 1971][research_stout_1971]\] \[[Swanson et al 2025][research_swanson_miller_2025]\] \[[Szymanski et al 2025][research_szymanski_2025]\] \[[Tancredi et al 2007][research_tancredi_accardo_2007]\] \[[Taylor 2004][research_taylor_2004]\] \[[Thato Elijah and Rui Vasconcellos 2026][research_elijah_2026]\] \[[Thompson and Horton 1981][research_thompson_1981]\] \[[Thornton and Lamy 1992][research_thornton_lamy_1992]\] \[[Thornton 1994][research_thornton_1994]\] \[[Torres-Martinez et al 2010][research_torresmartinez_heaps_2010]\] \[[Tracy 1981][research_tracy_1981]\] \[[Trevino et al 2012][research_trevino_schwartz_2012]\] \[[Tsohas and Heister 2010][research_tsohas_heister_2010]\] \[[Tuozzo et al 2017][research_tuozzo_fox_2017]\] \[[Turner and Spanyer 2005][research_turner_2005]\] \[[Van Bavel 2014][research_vanbavel_2014]\] \[[Van Gaasbeek 1980][research_vangaasbeek_1980]\] \[[Van Pelt 1981][research_pelt_1981]\] \[[Van Wyckhouse 1966][research_vanwyckhouse_1966]\] \[[Vanatta and Inderhees 1988][research_vanatta_inderhees_1988]\] \[[Verhaegen 1988][research_verhaegen_1988]\] \[[Voss et al 2026][research_voss_tang_2026]\] \[[Try et al 2020][research_w_p_2020]\] \[[Wang et al 1986][research_wang_demiroz_1986]\] \[[Wardana et al 2021][research_wardana_pranoto_2021]\] \[[Wells 1987][research_wells_1987]\] \[[Wernicke and Wernicke 1997][research_wernicke_1997]\] \[[Westphal and Wagner 2001][research_westphal_wagner_2001]\] \[[White et al 2024][research_white_fonnegra_2024]\] \[[Williams and Hartford 1987][research_williams_hartford_1987]\] \[[Williams 2017][research_williams_2017]\] \[[Wolf and Bossert 2001][research_wolf_bossert_2001]\] \[[Woodbury and Gorman 1983][research_woodbury_gorman_1983]\] \[[Wu and Liu 2021][research_wu_liu_2021]\] \[[Xi et al 2023][research_xi_li_2023]\] \[[Yeom et al 2009][research_yeom_oh_2009]\] \[[Yun et al 2019][research_yun_seo_2019]\] \[[Zeyuan et al 2021][research_zeyuan_huahui_2021]\] \[[Zhixin 2022][research_zhixin_2022]\] \[[Zieja et al 2015][research_zieja_kosinski_2015]\] \[[Николаев, 2020, Determining the Rational Composition of a Plane Group When Planning a Flight Test][research_determining_the_rational_2020]\]

### Drop Testing, Captive Carry and Release Dynamics

**This cluster covers the manoeuvre that began every X-40A flight.** Release from a carrier vehicle is a transient with its own dynamics, and it is the one part of the flight profile that has no counterpart in the operational mission.

Of its 73 titles, 50 concern separation, release, captive carry or air launch, and 23 concern drop tests.

**73 records.** \[[Acquatella and Reiner 2014][research_acquatella_reiner_2014]\] \[[Albertson et al 2012][research_albertson_tartabini_2012]\] \[[Allee 1980][research_allee_1980]\] \[[Black 1968][research_black_1968]\] \[[Bledsoe 2011][research_bledsoe_2011]\] \[[Bledsoe and Bernatovich 2015][research_bledsoe_2015]\] \[[Carman et al 1980][research_carman_jb_1980]\] \[[Carten 1978][research_carten_1978]\] \[[Chudej 1994][research_chudej_1994]\] \[[Cross 1989][research_cross_1989]\] \[[Daughetee 1974][research_daughetee_1974]\] \[[Deslandes and Donauer 2010][research_deslandes_2010]\] \[[Douglas Aircraft Co Long Beach Ca 1962][research_douglasaircraftcolongbeachca_1962]\] \[[Dutta et al 2024][research_dutta_guechaahumada_2024]\] \[[Flotten 2005][research_flotten_2005]\] \[[Fuchs and Jackson 2011][research_fuchs_jackson_2011]\] \[[Gao et al 2017][research_gao_tang_2017]\] \[[Grenoble et al 2018][research_grenoble_nguyen_2018]\] \[[Hallberg et al 2008][research_hallberg_cenko_2008]\] \[[Hatchell et al 2011][research_hatchell_mauss_2011]\] \[[Herbst et al 2000][research_herbst_forrest_2000]\] \[[Hinson 1959][research_hinson_1959]\] \[[Hinson and Lee 1959][research_hinson_1959_b]\] \[[Homan et al 1980][research_homan_1980]\] \[[Hudson 2005][research_hudson_2005]\] \[[Jacobson 2005][research_jacobson_2005]\] \[[Jia et al 2026][research_jia_qi_2026]\] \[[Karlgaard et al 2024][research_karlgaard_deshmukh_2024]\] \[[Kawaguchi et al 2017][research_kawaguchi_suzuki_2017]\] \[[Ko and Schuster 1983][research_ko_1983]\] \[[Ko and Schuster 1984][research_ko_1984]\] \[[Kozak et al 2013][research_kozak_yildiz_2013]\] \[[Kumar et al 2023][research_kumar_rjustus_2023]\] \[[Lee and Basford 1957][research_lee_1957]\] \[[Leo et al 2014][research_leo_fenza_2014]\] \[[Lijewski and Suhs 1994][research_lijewski_suhs_1994]\] \[[Lu et al 2024][research_lu_yue_2024]\] \[[Mehta et al 2012][research_mehta_bowles_2012]\] \[[Mehta et al 2014][research_mehta_bowles_2014]\] \[[Moiseev and Poluboyarinov 2011][research_moiseev_poluboyarinov_2011]\] \[[Moog et al 1979][research_moog_1979]\] \[[Naftel et al 1986][research_naftel_1986]\] \[[Norwood and Chichester 2015][research_norwood_chichester_2015]\] \[[Podruzhin and Zagidulin 2017][research_podruzhin_zagidulin_2017]\] \[[Poth et al 1993][research_pothjr_fisher_1993]\] \[[Pu et al 2024][research_pu_wang_2024]\] \[[Qiu et al 2019][research_qiu_sang_2019]\] \[[Romero and Bledsoe 2015][research_romero_bledsoe_2015]\] \[[Roshanian and Talebi 2008][research_roshanian_talebi_2008]\] \[[Runkle and Drobnik 1979][research_runkle_drobnik_1979]\] \[[Sarigul-Klijn et al 2005][research_sarigulklijn_sarigulklijn_2005]\] \[[Sarigul-Klijn et al 2008][research_sarigulklijn_sarigulklijn_2008]\] \[[Sohier et al 2014][research_sohier_farges_2014_b]\] \[[Sohier et al 2014][research_sohier_farges_2014]\] \[[Sohier et al 2015][research_sohier_pietlahanier_2015]\] \[[Song et al 2020][research_song_ai_2020]\] \[[Spahr 1974][research_spahr_1974]\] \[[Starr et al 1962][research_starr_1962]\] \[[Tamer 2021][research_tamer_2021]\] \[[Turnbow 1961][research_turnbow_1961]\] \[[Verstraete et al 2009][research_verstraete_bizzarri_2009]\] \[[Wang and Wang 1997][research_wang_wang_1997]\] \[[Way et al 2003][research_way_desai_2003]\] \[[Wei and Gjestvang 2001][research_wei_gjestvang_2001]\] \[[Wilhite 1977][research_wilhite_1977]\] \[[Woods et al 2000][research_woods_2000]\] \[[Woods et al 2000][research_woods_2000_b]\] \[[Yang et al 2016][research_yang_ye_2016]\] \[[Yang et al 2021][research_yang_ye_2021]\] \[[Yu et al 2025][research_yu_baek_2025]\] \[[Zhang et al 2024][research_zhang_cai_2024]\] \[[Zhang and Zhang 2020][research_zhang_zhang_2020_b]\] \[[Zhu et al 2021][research_zhu_wang_2021]\]

## Where the Framing Breaks Down

**Treating the X-40A through the similarity keystone is correct about the physics and misleading about
the programme, in three ways.**

**First, the programme never claimed dynamic similarity and the framing risks knocking down an argument
nobody made.** Boeing described the vehicle as a technology demonstrator \[[Boeing and the Air Force flight test the Space Maneuver Vehicle][ref_boeing_1998]\] and the space agency described
the flights as software evaluation \[[X-40A Space Maneuvering Vehicle][ref_nasa_x40]\]. **Neither promised that the trajectory would scale**, and the mass
result above is a finding about what the vehicle could have delivered rather than about a broken promise.

**Second, similarity analysis assumes the objective is prediction, and here it was rehearsal.** A great
deal of what an autonomous landing programme must retire is not physics at all, being the integration of
navigation sensors, the handling of dropouts, the release transient, the interaction with range safety,
and the question of whether the whole apparatus works on a real morning in real air. **None of that scales
because none of it is a similarity problem**, and all of it is retired by flying.

**Third, the keystone flatters the flight data by treating a 75 second glide as representative.** The
X-37's return from orbit passes through hypersonic, supersonic and transonic flight and a thermal
environment the X-40A never approached. **The X-40A tested the last four nautical miles of a mission that
begins in orbit**, and calling that risk reduction for the mission is a claim about proportion that the
flight data cannot support.

## The Source Base

**Forty-three curated sources carry the argument, and the survey maps the field around them.** Twenty-nine of the forty-three are reports that also sit in the survey, and the other 4,256 survey records carry no claim about the X-40A.

**Fourteen of the forty-three are reference works and contemporaneous accounts.** The manufacturer's press release and the space agency's programme page supply the dimensions and the flight profile. A designation reference, a defence reference site and the Air Force museum's fact sheet supply the programme's history, one is a contemporaneous report of the second free flight, two encyclopaedia entries describe the X-40 and its successor, five define terms or name other vehicles, and the 1976 standard atmosphere supplies the properties of the air. **Every dimensional claim traces to that set**, and every derived number is computed here rather than quoted.

**Twenty-nine are primary technical reports, which makes the curated set 67 percent primary, and they are not decorative.** They supply the canonical account of dynamically scaled free-flight practice, the measured lift and drag of seven lifting-body configurations against which this article's claim about attainable ratios is checked, the statistical distribution of lifting-body touchdown conditions behind its landing gear figure, four decades of low lift-to-drag approach and landing research beginning in 1959, the design literature for automatic landing of unpowered vehicles, the Shuttle Approach and Landing Test programme that is this campaign's direct methodological precedent, the stated objectives of the 2001 flight series, and the successor programme's own flight test documents.

**The research survey holds 4,285 research records drawn from Crossref, the NASA Technical Reports Server and the Defense Technical Information Center**, of which 659 are report primaries, being 15.4 percent, by the identifier rule set out under The Definition of Primary. **The median publication year of the 4,253 dated records is 2012.** Of those, 1,392 were published before 2001, the year of the second campaign, being 32.7 percent, and 1,844 were published in 2015 or later, being 43.4 percent.

### The Definition of Primary

**Primacy is a property of the document, and this survey derives it from the identifier.** A record is a report primary when its address is on the NASA Technical Reports Server or it carries a digital object identifier under the 10.21236 prefix, which Crossref registers for Defense Technical Information Center reports. **All twenty-nine of the reports the argument rests on are report primaries under that rule.** The rule does not reach conference papers and journal articles that report flight tests at first hand, such as the X-37 programme's papers to the American Institute of Aeronautics and Astronautics, so 15.4 percent is a lower bound on how much of the survey is first-hand.

### Thin Subjects

**Several subjects that this article's derivations depend on have thin literatures.** Each count below is the number of research records in this survey whose title carries at least one of the listed terms, with a hyphen read as a space. Where a row joins two groups of terms with the word together, a title must carry a term from each group.

| Subject | Title terms counted | Records |
|---|---|---|
| the relative density of a free-flight model | relative density, mass parameter, relative mass, mass ratio | 0 |
| Froude similarity | froude | 2 |
| dynamically scaled drop models | drop model, drop models | 9 |
| the inertia of a scaled model | inertia together with scaled, scale model, similar, similitude, free flight, free flying, drop model | 1 |
| the reliability bound from flights without failure | zero failure, success run, reliability demonstration, binomial, confidence bound, failure free | 0 |
| the worth of a flight demonstrator | demonstrator, demonstration together with cost, value, worth, benefit, affordab, economic | 9 |
| runway overrun and excursion | overrun, excursion | 39 |

**The parameter in which the free-flight literature states dynamic similarity is absent from its titles.** No title carries a relative density, a mass parameter, a relative mass or a mass ratio, although the article displays the relative density as the canonical similarity condition and finds the X-40A at about half of it. **The condition is stated inside the reports, as the canonical account of free-flight practice states it**, and not in what they are called.

**Froude similarity and the drop model are named rarely.** Two titles name the Froude number and nine name a drop model, and one names the inertia of a scaled or dynamically similar model, which is the quantity behind this article's finding that the X-40A responded about twice as fast as a similar model would have.

**The reliability bound has no literature here.** No title in the survey names a zero-failure bound, a success run or a reliability demonstration, so the statement that eight clean landings bound the failure rate only below about 31 percent rests on the binomial relation derived above and not on a body of flight-test reliability work.

**The worth of a demonstrator is rarely the subject of a title.** Nine titles name a demonstrator or a demonstration together with its cost, value, benefit or economics, and the article's argument that eight affordable flights were the point of the programme stands on the X-40A's own record.

**Runway overrun and excursion, on which the closing argument rests, is better represented**, with 39 records whose title contains overrun or excursion.

### What the Survey Admits

**A record is admitted only when a person reading its title finds it on this article's subject.** The subjects are the ten clusters above, and the object must be a flight vehicle or a method stated for one. Many words this subject depends on also name something else, and a record that shares only such a word is excluded. **The runway is a piece of apparatus in animal behaviour research**, a straight alley a rat runs down for reinforcement, and it is also where fashion is shown. **Disaster risk reduction shares both words with flight risk reduction and nothing else.** **Subscale is a psychometrics term**, a subscale being a component of a test instrument. **Relative density is a soil mechanics term**, and moment of inertia names a nuclear physics model of rotational bands as well as the section property of a beam. Similitude also governs model studies of piles, dams, bridges, ships, plates, shells and rotating machinery. Energy management also names the control of buildings, microgrids and electric cars, rollout also names a class of algorithm, Autoland is also the name of a company in a court case, and free flight is also a concept of air traffic management.

**The admission rule also excludes neighbouring literatures that share a technique and not the subject.** Navigation of cars, ships, underwater vehicles, pedestrians, trains and ground robots is excluded, because the X-40A's navigation problem is that of a flight vehicle. So are orbital manoeuvring, rendezvous and docking, the homing, interception and tracking of missiles and reentry vehicles, the acoustics of aircraft and their components, the internal aerodynamics of engines, fans and compressors, airfoil and wing design at a stated Reynolds number, runway pavement construction, and fluid mechanics with no flight application, such as flow past cylinders and the statistics of wall turbulence. Records on wind turbines, electrical machines and power networks, granular media, geophysics and astrophysics are excluded as well, together with correction, erratum, retraction and withdrawal notices, figure and supplementary-material records, peer-review reports and journal front matter, because the survey counts research works. Second deposits of one document, such as a conference paper and its journal version under the same title, are counted once. A review of a book, a news item, signed or unsigned, together with a news writer's reply to a letter about a news story, a patent abstract, an abstract reprinted in another journal's abstract section, and a reference or definition entry of two pages or fewer are not admitted either, while an authored encyclopedia article of more than two pages and a textbook chapter are research works and are kept. So are a signed comment on a paper, a discussion of a paper, the author's reply to either and a signed letter on a research subject, because each argues about a result, and they are admitted when their subject is this article's.

**The survey keeps 145 records of doubtful relevance.** Their titles do not settle whether they are on the subject, and a reader may weigh each accordingly. They are navigation methods whose platform the title does not name, such as dead reckoning aided by satellite navigation, general chapters and facilities on similitude, Reynolds number effects and wind tunnel testing, crash and drop tests of airframes, runway surfaces and sites, guidance of gliding vehicles and munitions whose purpose the title leaves open, and propulsion, orbital and programme titles that may or may not concern a flight vehicle in the regimes this article treats. Quadrotor and multirotor landing and drone landing gear are kept within the scope of uncrewed landing, and lunar and planetary landers within the planetary landing cluster.

**Every research title has been read for relevance, so the off-topic share that remains is a matter of reading judgement.** A reading of titles cannot show that a work is relevant in substance, so this is a statement about titles only.

## Epistemic State

### Historical Fact

Boeing received a contract from the Air Force Research Laboratory's Military Space Plane Technology office
in October 1996 to build a technology demonstrator for the Space Maneuver Vehicle. The X-40A designation
was allocated to the operational vehicle in 1997 and reassigned to the Integrated Technology Test Bed. The
vehicle was built at Boeing Phantom Works in Seal Beach, California, is 22 feet long with a 12 foot span,
weighs about 2,600 pounds, and cost approximately one million dollars to fabricate. It first flew on
11 August 1998 at Holloman Air Force Base after release from a UH-60. It was loaned to the space agency
and flew seven free flights at Dryden Flight Research Center in 2001, released
from a CH-47D at about 15,000 feet for descents of about 75 seconds. The second of those flights was on
12 April 2001, released at 15,050 feet, reaching 428 feet per second. The vehicle was retired in May 2001
and is preserved at the National Museum of the United States Air Force. The X-37 airframe is about
120 percent of the X-40A.

### Engineering Analysis

**Every quantitative result here is computed from published dimensions, masses and flight figures using
standard relations, and each can be recomputed from the figures the article gives.** The scale ratios follow from the
published lengths and spans. The Froude, Reynolds, time, angular rate and mass conditions are the standard
free-flight similarity relations and carry no vehicle property at all. The flight path angle, effective
lift to drag ratio and ground range follow from the released altitude, the duration and the speed. The
product of reference area and lift coefficient follows from the steady glide.

**Three results are sensitivities rather than assertions.** The scale ratio is tabulated across the full
range of published figures and no conclusion moves. The reference area is bounded rather than stated. The
landing gear deceleration uses a representative sink rate and stroke, neither of which is published, and
is offered only to show that the case is undemanding.

### Inference

**That the mass shortfall explains what the programme bought is an inference**, not a claim any source
makes. The sources describe a technology demonstrator and a software evaluation. The observation that its
mass ratio and its geometric ratio disagree by a wide margin is arithmetic, and the conclusion that the
trajectory therefore could not transfer follows from the similarity relations, **but no source frames the
vehicle this way and the programme may never have intended the comparison.**

**That the 2006 X-37A runway overrun evidences the limits of transfer is an inference.** The two events
are connected by programme lineage and by the shape, and the article does not know how much of the
guidance software was common between them.

**That the subscale test was conservative for the flight control system is an inference from the angular
rate relation**, and it holds only to the extent that control system difficulty tracks angular rate, which
is a simplification.

### What the Record Does Not Settle

**The reference area, and therefore the wing loading and the lift coefficient, are not published.** The
product of area and lift coefficient is recovered from the flight data and the split between them is an
estimate.

**The release altitude of the 1998 flight is given as both 9,000 and about 10,000 feet**, and the two
imply straight-line glide ratios of 1.47 and 1.32.

**The start date of the 2001 series is given as 14 March, 28 March and 4 April 2001.** One account describes a
first free flight on the earliest date flying a straight-in approach, which would make the 12 April flight
the second, and that is consistent with the sources describing 12 April as the second free flight. The
conflict is recorded rather than resolved.

**The 75 second descent is the space agency's description of the 2001 releases from 15,000 feet and is not
stated for the 12 April flight.** The flight path angle, glide ratio and ground range are computed by
pairing it with that flight's 15,050 foot release and 428 feet per second, and they inherit that
pairing.

**The only published landing accuracy, 7 feet of centreline tracking on the 1998 flight, comes from an
encyclopaedia entry** whose cited sources do not carry the figure, and the touchdown offset that preceded it
is not published. The 2.5 mile release distance of that flight rests on the same entry, whose cited source does not
carry it either.

**The X-37B weight used in the mass comparison is a maximum takeoff weight including payload and
propellant.** A landing weight would be lower and would reduce the computed shortfall, so
**the factor of two is an upper bound on the mismatch and not a measurement of it.** No landing weight is
published.

**The navigation hardware is described in the record.** A paper to the twentieth Digital Avionics Conference names the Space Integrated Global
Positioning System and Inertial Navigation System, reports its testing during the X-40A approach and
landing campaign against differential satellite navigation, and states its objectives as demonstrating
performance sufficient for the X-37 requirement and reducing the risk of integrating that unit into that
vehicle \[[Childers et al 2001][research_childers_2001]\].
**The wider instrumentation suite is described only through the flight test objectives**, which name a calculated air data system and parameter identification manoeuvres \[[Mitchell 2004][research_mitchell_2004]\], and the achieved
navigation accuracies are in the full report rather than in its abstract, so they are not quoted here.

**Whether any of the X-40A software was common with the X-37A Approach and Landing Test Vehicle is not
established**, which weakens the inference drawn from the 2006 overrun.

## Out of Scope

The X-37 as an orbital vehicle, which has its own article in this series. The Space Maneuver Vehicle
operational concept and the military spacelift debate that produced it. The Approach and Landing Test
Vehicle campaign of 2005 and 2006 and its carrier aircraft arrangements. Buran's autonomous landing and
the Soviet automatic landing system, which deserve separate treatment. The Shuttle's automatic landing modes and the manual control its crews took over. Thermal protection system development, which the X-40A
did not carry and did not test. Modern autonomous landing practice in uncrewed aircraft, which is surveyed
here and not analysed.

## Conclusion

**The X-40A is remembered as a subscale model and the arithmetic shows it was not one.** Its geometric
ratio to the X-37 is about 0.78 and the scale ratio its mass implies is about 0.62, so it flew at roughly half the weight
that dynamic similarity demanded. **The Froude number was never matched, so the speeds, the times and the
trajectory never scaled**, and no trajectory result from those eight flights transfers to the vehicle it was built to inform. The aerodynamic coefficients were another matter, because they depend on the shape and not on the mass, and the flights carried parameter identification manoeuvres for the X-37 aerodynamic database \[[Mitchell 2004][research_mitchell_2004]\].

**What it bought instead was eight rehearsals.** An autonomous guidance, navigation and control system was
exercised in real air, against a plant that its smaller scale made about 13 percent quicker to respond, and its mass deficit
quicker again, than the full-scale vehicle would be, and it landed the aircraft every time, once within 7 feet of the
centreline. **The subscale test was harder than the full-scale case in the one dimension that mattered**,
and it gives the programme its strongest argument.

**The most durable output was the shape.** A one million dollar test article defined the outer mould line
of a spacecraft that has since spent years in orbit. **And the clearest evidence of what did not transfer
came in 2006**, when the 120 percent vehicle built on that shape overran the runway on its first free
flight.

The next article returns to a vehicle designed to be shot down.

## References

### Reference

- [Boeing and the Air Force flight test the Space Maneuver Vehicle][ref_boeing_1998]
- [Boeing CH-47 Chinook][ref_ch47]
- [Boeing X-37][ref_x37]
- [Boeing X-37 and X-40][ref_x37_x40]
- [Boeing X-40][ref_x40]
- [Boeing X-40A][ref_nmusaf_x40]
- [Buran][ref_buran]
- [Lifting body][ref_lifting_body]
- [Sikorsky UH-60 Black Hawk][ref_uh60]
- [Space Shuttle][ref_shuttle]
- [U.S. Standard Atmosphere, 1976][ref_atm76]
- [X-40 Space Maneuver Vehicle][ref_smv_global]
- [X-40A second free flight successful][ref_sciencedaily_x40]
- [X-40A Space Maneuvering Vehicle][ref_nasa_x40]

### Related Post

- [X-Planes: Aerojet X-8 Aerobee][related_post_a305_aerojet_x8]
- [X-Planes: Bell X-1][related_post_a298_bell_x1]
- [X-Planes: Bell X-14][related_post_a311_bell_x14]
- [X-Planes: Bell X-16][related_post_a313_bell_x16]
- [X-Planes: Bell X-2][related_post_a299_bell_x2]
- [X-Planes: Bell X-22][related_post_a319_bell_x22]
- [X-Planes: Bell X-5][related_post_a302_bell_x5]
- [X-Planes: Bell X-9 Shrike][related_post_a306_bell_x9]
- [X-Planes: Bensen X-25][related_post_a322_bensen_x25]
- [X-Planes: Boeing X-20 Dyna-Soar][related_post_a317_boeing_x20]
- [X-Planes: Boeing X-32][related_post_a329_boeing_x32]
- [X-Planes: Boeing X-37][related_post_a334_boeing_x37]
- [X-Planes: Convair X-11][related_post_a308_convair_x11]
- [X-Planes: Convair X-12][related_post_a309_convair_x12]
- [X-Planes: Convair X-6][related_post_a303_convair_x6]
- [X-Planes: Curtiss-Wright X-19][related_post_a316_curtiss_wright_x19]
- [X-Planes: Douglas X-3 Stiletto][related_post_a300_douglas_x3]
- [X-Planes: Framing and the Research Aircraft Model][related_post_a297_framing]
- [X-Planes: Grumman X-29][related_post_a326_grumman_x29]
- [X-Planes: Hiller X-18][related_post_a315_hiller_x18]
- [X-Planes: Lockheed Martin X-33][related_post_a330_lockheed_martin_x33]
- [X-Planes: Lockheed Martin X-35][related_post_a332_lockheed_martin_x35]
- [X-Planes: Lockheed X-17][related_post_a314_lockheed_x17]
- [X-Planes: Lockheed X-27][related_post_a324_lockheed_x27]
- [X-Planes: Lockheed X-7][related_post_a304_lockheed_x7]
- [X-Planes: Martin Marietta X-23 PRIME and a Contested Assignment][related_post_a320_martin_marietta_x23]
- [X-Planes: Martin Marietta X-24][related_post_a321_martin_marietta_x24]
- [X-Planes: McDonnell Douglas X-36][related_post_a333_mcdonnell_douglas_x36]
- [X-Planes: North American X-10][related_post_a307_north_american_x10]
- [X-Planes: North American X-15][related_post_a312_north_american_x15]
- [X-Planes: Northrop X-21][related_post_a318_northrop_x21]
- [X-Planes: Northrop X-4 Bantam][related_post_a301_northrop_x4]
- [X-Planes: Orbital Sciences X-34][related_post_a331_orbital_sciences_x34]
- [X-Planes: Osprey X-28 Sea Skimmer][related_post_a325_osprey_x28]
- [X-Planes: Rockwell X-30 and the National Aero-Space Plane][related_post_a327_rockwell_x30]
- [X-Planes: Rockwell-MBB X-31][related_post_a328_rockwell_mbb_x31]
- [X-Planes: Ryan X-13 Vertijet][related_post_a310_ryan_x13]
- [X-Planes: Scaled Composites X-38][related_post_a335_scaled_composites_x38]
- [X-Planes: Schweizer X-26 Frigate][related_post_a323_schweizer_x26]
- [X-Planes: X-39, Reserved but Never Assigned][related_post_a336_x39_reserved_never_assigned]

### Research

- [1958, Tire-runway braking friction coefficients][research_tire_runway_braking_1958]
- [1960, Flight tests to determine the coefficients of friction between an aircraft tyre and various wet runway surfaces. Part I][research_flight_tests_1960]
- [1962, Damping An Inertial Navigation System][research_damping_an_1962]
- [1962, Multiple Inertial System Operation In Long Term Navigation][research_multiple_inertial_1962]
- [1962, Terminal Guidance System For Soft Lunar Landing][research_terminal_guidance_1962]
- [1962, The King Inertial Navigation Gyro][research_the_king_1962]
- [1963, Design Considerations for a Re-Entry Vehicle Thermal Protection System][research_design_considerations_1963]
- [1963, Flying Controls and Automatic Landing][research_flying_controls_1963]
- [1963, Influence of tire tread pattern and runway surface condition on braking friction and rolling resistance of a modern aircraft tire][research_influence_of_1963]
- [1964, A Minimum Fuel Vertical Touchdown Lunar Landing Guidance Technique][research_a_minimum_1964]
- [1964, Automatic Landing][research_automatic_landing_1964]
- [1964, Navigation and Guidance Systems Employing a Gimballess IMU][research_navigation_and_1964]
- [1964, Statistical Filtering of Space Navigation Measurements][research_statistical_filtering_1964]
- [1964, Stellar Techniques for Midcourse Navigation Guidance][research_stellar_techniques_1964]
- [1967, Similitude and Models][research_similitude_and_1967]
- [1970, Flight Test Programme][research_flight_test_1970]
- [1971, Inertially augmented approach and landing systems][research_inertially_augmented_1971]
- [1971, The Advance Towards Category Three Automatic Landings][research_the_advance_1971]
- [1972, Development of STOLAND, a versatile navigation, guidance and control system][research_development_of_1972]
- [1972, Re-entry Thermal Analysis of Variable Thickness Spherical Vehicles][research_re_entry_thermal_1972]
- [1972, Structural design aspects of reusable surface insulation thermal protection systems][research_structural_design_1972]
- [1972, Thermal performance evaluation of REI panel steps and gaps for Space Shuttle thermal protection system][research_thermal_performance_1972]
- [1975, Vibration of a Reentry Vehicle][research_vibration_of_1975]
- [1977, Reentry vehicle nosetip material screening tests - Series M][research_reentry_vehicle_1977]
- [1978, Space Shuttle Orbiter Approach and Landing Test Final Evaluation Report][research_alt_final_1978]
- [1979, Evaluation of the navigation performance of shipboard-VTOL-landing guidance systems][research_evaluation_of_1979]
- [1979, Flight test of a VTOL digital autoland system along complex trajectories][research_flight_test_1979]
- [1981, Optimal Glide of Reentry Vehicles][research_optimal_glide_1981]
- [1981, Orbital Aerodynamic Maneuvers][research_orbital_aerodynamic_1981]
- [1981, Re-entry Vehicle Soft-Recovery Techniques][research_re_entry_vehicle_1981]
- [1981, The Effect of Surface Roughness Character on Turbulent Re-entry Heating][research_the_effect_1981]
- [1981, Thermal Protection System for the Galileo Mission Atmospheric Entry Probe][research_thermal_protection_1981]
- [1981, Wind-Tunnel Study of Ascent Heating of Multiple Re-entry Vehicle Configurations][research_wind_tunnel_study_1981]
- [1982, The effect of additional runway lights and autopilot failure on the landing performance of a medium size transport aircraft][research_the_effect_1982]
- [1983, Tile-Gap Flow in the Shuttle Orbiter Thermal Protection System][research_tile_gap_flow_1983]
- [1985, Low Lift-to-Drag Aerobrake Heat-Transfer Test at Mach 10][research_low_lift_to_drag_1985]
- [1987, Redesigned aircraft landing gear to be analysed for stresses][research_redesigned_aircraft_1987]
- [1990, ORBITEC Orbital Technology Demonstration Program][research_orbitec_orbital_1990]
- [1992, Similitude Relationships and Scaling Factors][research_similitude_relationships_1992]
- [1994, 180 Fault Tolerant navigation system for aircraft landing][research_180_fault_1994]
- [1994, Aerodynamic Optimization for Hypersonic Flight at Very High Altitudes][research_aerodynamic_optimization_1994]
- [1994, Further development and flight test of an autonomous precision landing system using a parafoil][research_further_development_1994]
- [1994, Slender Lifting Body Axial Force Prediction in Hypersonic Rarefied Flow][research_slender_lifting_1994]
- [1995, Gliding and Unpowered Flights][research_gliding_and_1995]
- [1996, Aircraft Automatic Approach and Landing Using GPS][research_aircraft_automatic_1996]
- [1997, Inertial Navigation With External Measurements][research_inertial_navigation_1997]
- [1997, Part I Inertial Navigation][research_part_i_1997]
- [1997, Part II Inertial Navigation With Aids][research_part_ii_1997]
- [1998, Control and Guidance System Modeling][research_control_and_1998]
- [1998, Dimensional Analysis and Dynamic Scaling][research_dimensional_analysis_1998]
- [1999, Discussion Questions for Integrated Navigation and Guidance Systems][research_discussion_questions_1999]
- [1999, Inertial Navigation Sensors and Systems][research_inertial_navigation_1999]
- [1999, Integrated vision/inertial navigation system design using nonlinear filtering][research_integrated_vision_inertial_1999]
- [1999, Kalman Filter Inertial Navigation System Flight Applications][research_kalman_filter_1999]
- [1999, Reusable Space Launch Vehicles][research_reusable_space_1999]
- [2000, Reentry Control for Low UD Vehicles][research_reentry_control_2000]
- [2000, Reynolds Number Effects][research_reynolds_number_2000]
- [2001, 4 Inertial Navigation System][research_4_inertial_2001]
- [2002, SPACEPLANE HISTORY][research_spaceplane_history_2002]
- [2002, Spaceplane Low-cost Potential][research_spaceplane_low_cost_2002]
- [2002, The Spaceplane Space Age][research_the_spaceplane_2002]
- [2002, Titan II Operational Flight Test and Evaluation Programs History][research_titan_ii_2002]
- [2004, Advanced Hypersonic Spaceplane Multi-Role Architecture using Turbine Based Combined Cycle][research_advanced_hypersonic_2004]
- [2004, Appendix B Inertial navigation system error budgets][research_appendix_b_2004]
- [2004, Appendix D Comparison of GPS and GLONASS satellite navigation systems][research_appendix_d_2004]
- [2004, Basic principles of strapdown inertial navigation systems][research_basic_principles_2004]
- [2004, Bifurcation Analysis for the Inertial Coupling Problem of a Reentry Vehicle][research_bifurcation_analysis_2004]
- [2004, Fundamental principles and historical developments of inertial navigation][research_fundamental_principles_2004]
- [2004, Inertial navigation system alignment][research_inertial_navigation_2004]
- [2004, Integrated navigation systems][research_integrated_navigation_2004]
- [2004, Nonlinear Flight Control for Re-entry Flight Vehicle][research_nonlinear_flight_2004]
- [2004, The Development of Thermal Protection System of " Manned Spacecraft"][research_the_development_2004]
- [2004, Tripropellant Engine Technology for Reusable Launch Vehicles][research_tripropellant_engine_2004]
- [2004, X-37 Flight Demonstrator Project Capabilities for Future Space Transportation System Development][research_x_37_flight_2004]
- [2007, 3 Inertiale Navigation][research_3_inertiale_2007]
- [2007, Automatic Landing System using a Trajectory of Laser Beam][research_automatic_landing_2007]
- [2007, Inertial Navigation System Ground Alignment][research_inertial_navigation_2007]
- [2007, The Inertial Navigation System Equations][research_the_inertial_2007]
- [2008, Automatic Landing Guidance Law Design for Unmanned Aerial Vehicles based on Pursuit Guidance Law][research_automatic_landing_2008]
- [2008, Chapteer 8. GPS Modernization and Global Navigation Satellite System GNSS][research_chapteer_8_2008]
- [2008, Three-Dimensional Location Tracking System for Automatic Landing of an Unmanned Helicopter][research_three_dimensional_location_2008]
- [2009, Dimensional Analysis and Dynamic Similitude][research_dimensional_analysis_2009]
- [2009, Robust Airspeed Estimation of an Unpowered Gliding Vehicle by Using Multiple Model Kalman Filters][research_robust_airspeed_2009]
- [2011, 3 Inertiale Navigation][research_3_inertiale_2011]
- [2011, KPCA-Kalman Filtering for the MEMS-SINS/GPS Integrated Navigation System][research_kpca_kalman_filtering_2011]
- [2011, The graphic Skylon reusable spaceplane][research_the_graphic_2011]
- [2012, Chapter 6. Piloting and Inertial Navigation][research_chapter_6_2012]
- [2012, Fusion of Multi-Antenna Carrier Phase Differential GPS and Inertial Measurements for Performance Evaluation of High Accuracy Integrated Aircraft Navigation Systems][research_fusion_of_2012]
- [2012, Research on Attitude Tracking Control of Reentry Vehicle via Dynamic Inversion Method][research_research_on_attitude_2012]
- [2013, 5 Inertial navigation accuracy][research_5_inertial_2013]
- [2013, Chapter 12 Methodology of Formation of the Windward Surface of a Winged Reentry Vehicle with Reduced Thermal Intensity][research_chapter_12_2013]
- [2013, Chapter 13 Numerical Modeling of Hypersonic Heat Transfer on the Windward Side of the Buran Reentry Vehicle][research_chapter_13_2013]
- [2013, Inertial navigation][research_inertial_navigation_2013_b]
- [2013, Inertial navigation systems][research_inertial_navigation_2013]
- [2013, LP Based Path Planning for Autonomous Landing of An Unmanned Helicopter on A Moving Platform][research_lp_based_2013]
- [2013, Sunken Reentry Vehicle][research_sunken_reentry_2013]
- [2013, Thermal Protection System Conception][research_thermal_protection_2013]
- [2015, Assessment of Factors Responsible for the Excursion of Runway in International Airport][research_assessment_of_2015]
- [2015, Dimensional Analysis and Dynamic Similitude][research_dimensional_analysis_2015]
- [2016, Effect of Ground Proximity on Aerodynamic Forces and Moments of Reusable Launch Vehicle at Subsonic Speed][research_effect_of_ground_2016]
- [2016, Flight Test Data Analysis of Hybrid Vertical Take-off and Landing Unmanned Aerial Vehicle][research_flight_test_2016]
- [2016, Numerical Optimization on Approach and Landing for Reusable Launch Vehicle][research_numerical_optimization_2016]
- [2016, Spaceplane Coordinates][research_spaceplane_coordinates_2016]
- [2017, Designing a Reusable Spacecraft][research_designing_a_2017]
- [2017, Scaling and Similitude 1638][research_scaling_and_2017]
- [2017, The Traditional Glide Path][research_the_traditional_2017]
- [2018, A Study on High Precision MEMS-IMU/GPS/Magnetometer/Barometer Integrated Navigation System][research_a_study_2018]
- [2018, Inertial Navigation][research_inertial_navigation_2018]
- [2018, ISRO Releases the Special Issue on 'Reusable Launch Vehicle-Technology Demonstrator'][research_isro_releases_the_2018]
- [2018, Performance and Technological Feasibility of Aerospace Plane Horizontal Launch and Landing with Ekranoplane Assistance][research_performance_and_2018]
- [2019, Anatomy of a No-Equipment-Failed NEF ICNS System Malfunction The Case of Singapore Airlines Sq-327 Runway Excursion][research_anatomy_of_2019]
- [2019, Dimensional Analysis and Dynamic Similarity][research_dimensional_analysis_2019]
- [2019, Radar Altimeter Aiding of GNSS for Precision Approach and Landing of RPA][research_radar_altimeter_2019]
- [2020, "LaGuardia Airport Design Build for Extending Runway Decks for Safety Area Improvements, Queens, NY"][research_laguardia_airport_2020]
- [2020, The algorithm of the color signal recognition at landing an unmanned aerial vehicle on an aircraft carrier in autonomous mode][research_the_algorithm_2020]
- [2021, A Manageable Glide-path][research_a_manageable_2021]
- [2021, Airborne Computer System Based Collision-Free Flight Path Finding Strategy Design for Drone Model][research_airborne_computer_2021]
- [2022, Introduction and overview of inertial navigation systems][research_introduction_and_2022]
- [2022, Methodology for assessing the accuracy of UAV landing on the runway][research_methodology_for_2022]
- [2022, Navigation-grade inertial sensors][research_navigation_grade_inertial_2022]
- [2022, Principles of Dynamic Similarity][research_principles_of_2022]
- [2023, 4 Inertial Navigation System][research_4_inertial_2023]
- [2023, Automatic Guidance and Control-Autopilots][research_automatic_guidance_2023]
- [2023, Mathematical model of the UAV landing approach system on the example of the course-glide path system][research_mathematical_model_2023]
- [2023, Research on Inertial Navigation Technology of Unmanned Aerial Vehicles with Integrated Reinforcement Learning Algorithm][research_research_on_2023]
- [2023, Technology Demonstrator, Close Air Support, and Legacy Programs][research_technology_demonstrator_2023]
- [2024, Mobile Autonomous Recovery Landing Principle and Control Method for Unmanned Aerial Vehicle][research_mobile_autonomous_2024]
- [2025, Approach to solving the problem of landing an unmanned aerial vehicle on a moving landing platform][research_approach_to_2025]
- [2025, Multi-architecture Design Method for Landing Gear System Based on Domain Specific Modeling][research_multi_architecture_design_2025]
- [2025, Reentry Maneuvering Vehicle Ascent Phase Trajectory Design][research_reentry_maneuvering_2025]
- [2025, Trajectory Shaping Guidance for Vertical Landing of Launch Vehicle Stage][research_trajectory_shaping_2025]
- [2026, Design validation and verification for non-intrusive flight test instrumentation NIFTI using Model-Based Systems Engineering MBSE][research_design_validation_2026]
- [2026, Response Analysis of Landing Leg Deployment and Landing Transient Impact of Reusable Launch Vehicle][research_response_analysis_2026]
- [2026, Reusable Launch Vehicle Landing Gear Mechanism Technologies A Review][research_reusable_launch_2026]
- [A Typical Avionics Integration Flight Test Program][research_a_typical]
- [Abdolkarimi and Mosavi 2020][research_abdolkarimi_mosavi_2020]
- [Abe et al 2001][research_abe_fujita_2001]
- [Abe et al 2005][research_abe_shimada_2005]
- [Abe et al 2018][research_abe_kasamura_2018]
- [Abensur 1994][research_abensur_1994]
- [Abershitz et al 2009][research_abershitz_rubinets_2009]
- [Abrahamm and Valsa 2018][research_abrahamm_valsa_2018]
- [Abu-Jbara et al 2015][research_abujbara_alheadary_2015]
- [Abujoub et al 2018][research_abujoub_mcphee_2018]
- [Acarbay and Kiyak 2022][research_acarbay_kiyak_2022]
- [Achambath and Schwartzentruber 2018][research_achambath_schwartzentruber_2018]
- [Achambath et al 2019][research_achambath_ramjatan_2019]
- [Acikmese and Ploen 2005][research_acikmese_ploen_2005]
- [Acikmese and Ploen 2007][research_acikmese_ploen_2007]
- [Acquatella and Reiner 2014][research_acquatella_reiner_2014]
- [Adams et al 1973][research_adams_johnc_1973]
- [Adelgren et al 2004][research_adelgren_2004]
- [Adhikari et al 2024][research_adhikari_black_2024]
- [Aeroelastic Tests of an 1963][research_aeroelastic_tests_1963]
- [Aftatah and Zebbara 2024][research_aftatah_zebbara_2024]
- [Agustin et al 1999][research_agustin_mangoubi_1999]
- [Ahmed 2021][research_ahmed_2021]
- [Ahmed et al 2003][research_ahmed_2003]
- [Ahmed et al 2017][research_ahmed_hazry_2017]
- [Ai et al 2022][research_ai_wang_2022]
- [Ai et al 2023][research_ai_hu_2023]
- [Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990]
- [Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991]
- [Air Force Test Pilot School Edwards Afb Ca 1992][research_airforcetestpilotschooledwardsafbca_1992]
- [Air Force Test Pilot School Edwards Afb Ca 1993][research_airforcetestpilotschooledwardsafbca_1993]
- [Aircraft Steady Gliding Longitudinal 2011][research_6_aircraft_2011]
- [Aircraft Steady Gliding Longitudinal 2011][research_aircraft_steady_2011]
- [Airoldi and Janszen 2005][research_airoldi_janszen_2005]
- [Akaryildiz et al 2024][research_akaryildiz_2024]
- [Akash and Anbarasu 2025][research_akash_anbarasu_2025]
- [Akinyemi and Adebiyi 2016][research_akinyemi_adebiyi_2016]
- [Al Bakri][research_bakri_nd]
- [Al Fatih et al 2021][research_alfatih_shimoyama_2021]
- [AL-Bakri and Kluever 2017][research_albakri_kluever_2017]
- [Al-Bakri et al 2020][research_albakri_albakri_2020]
- [Al-Sharman et al 2018][research_alsharman_aljarrah_2018]
- [Alatorre Sevilla][research_sevilla_nd]
- [Alaverdi and Paris 2001][research_alaverdi_2001]
- [Albach and Fewel 1965][research_albach_fewel_1965]
- [Alber 2012][research_alber_2012]
- [Alberts et al 2026][research_alberts_thomas_2026]
- [Albertson et al 2012][research_albertson_tartabini_2012]
- [Albrecht 1972][research_albrecht_1972]
- [Alcedo 1980][research_alcedo_1980]
- [Alexander 1979][research_alexander_1979]
- [Alexander and T. M 1978][research_alexander_tm_1978]
- [Alexander et al 1973][research_alexander_griffin_1973]
- [Alexeev et al 2023][research_alexeev_zemlyanyy_2023]
- [Alford and Bingham 1990][research_alford_bingham_1990]
- [Alford et al 1994][research_alford_chamdani_1994]
- [Algorithms for Flexible Flight 2012][research_algorithms_flexible_2012]
- [Ali 2007][research_ali_2007]
- [Ali et al][research_ali_nd]
- [Ali et al][research_ali_nd_b]
- [Ali et al 2024][research_ali_abbas_2024]
- [Alich and Castillo 2007][research_alich_castillo_2007]
- [Alijani and Osman 2020][research_alijani_osman_2020]
- [Allee 1980][research_allee_1980]
- [Allen and Lin 2007][research_allen_lin_2007]
- [Allen et al 1962][research_allen_1962]
- [Allen et al 1994][research_allen_sauvageau_1994]
- [Allen et al 2015][research_allen_sexton_2015]
- [Allison 2017][research_allison_2017]
- [Almeida 2011][research_almeida_2011]
- [Almeida 2021][research_almeida_2021]
- [Almosnino 2016][research_almosnino_2016]
- [Alonis 1988][research_alonis_1988]
- [Alpert 2001][research_alpert_2001]
- [Alroqi and Wang 2017][research_alroqi_wang_2017]
- [Altmann 2013][research_altmann_2013]
- [Alvord et al 2024][research_alvord_arias_2024]
- [Amato et al 2026][research_amato_giannino_2026]
- [Ambrosio et al 2026][research_ambrosio_camargo_2026]
- [Amelin 2022][research_amelin_2022]
- [Amzajerdian et al 2016][research_amzajerdian_2016]
- [An et al 2017][research_an_wang_2017]
- [An et al 2019][research_an_wang_2019]
- [An et al 2023][research_an_liu_2023]
- [An et al 2025][research_an_wang_2025]
- [An Li et al 2010][research_anli_guobinchang_2010]
- [An Su-yang et al 2016][research_ansuyang_zhangfeijuan_2016]
- [Anand et al 2020][research_anand_barman_2020]
- [Ananda et al 2017][research_ananda_2017]
- [Anderson and Armitage 1993][research_anderson_1993]
- [Anderson and Kinzel 2023][research_anderson_kinzel_2023]
- [Anderson et al 1967][research_anderson_schultz_1967]
- [Anderson et al 1983][research_anderson_vincent_1983]
- [Anderson et al 2021][research_anderson_loewenson_2021]
- [Andert et al 2015][research_andert_ammann_2015]
- [Andreev and Stanchev 2020][research_andreev_stanchev_2020]
- [Andreeva-Mori et al][research_andreeva_mori_nd]
- [Andrews 1977][research_andrews_1977]
- [Andrews 1979][research_andrews_1979]
- [Andrews 1998][research_andrews_1998]
- [Anh et al 2022][research_anh_tran_2022]
- [Anitha and Kumar 2012][research_anitha_kumar_2012]
- [Annaloro et al 2020][research_annaloro_galera_2020]
- [Anoshin et al 2012][research_anoshin_bobylev_2012]
- [Aoki and Ishigami 2022][research_aoki_ishigami_2022]
- [Aprovitola et al 2019][research_aprovitola_iuspa_2019]
- [Aprovitola et al 2019][research_aprovitola_iuspa_2019_b]
- [Aradag et al 2007][research_aradag_seidel_2007]
- [Arbic 1955][research_arbic_1955]
- [Arents et al 2009][research_arents_groeneweg_2009]
- [Arias et al 2022][research_arias_johnson_2022]
- [Armstrong 1977][research_armstrong_1977]
- [Armutcuoglu et al 2004][research_armutcuoglu_kavsaoglu_2004]
- [Arnaldo Valdés et al 2011][research_arnaldovaldes_gomezcomendador_2011]
- [Arnold 1981][research_arnold_1981]
- [Arora and Ananthasayanam 2003][research_arora_ananthasayanam_2003]
- [Arora et al 2003][research_arora_george_2003]
- [Arreola-Nepomuceno et al 2025][research_arreolanepomuceno_valdez_2025]
- [Arrington and Woods 1972][research_arrington_1972]
- [Arshad et al 2021][research_arshad_kallungal_2021]
- [Aruna and Devi 2012][research_aruna_devi_2012]
- [Asher et al 2013][research_asher_2013]
- [Ashford 1993][research_ashford_1993]
- [Ashikhmina and Prosuntsov 2021][research_ashikhmina_prosuntsov_2021]
- [Ashkenas et al 1982][research_ashkenas_1982]
- [Ashok Gandhi et al 2020][research_ashokgandhi_jayan_2020]
- [Asl and Farahani 2013][research_asl_farahani_2013]
- [Asl et al 2017][research_asl_niezrecki_2017]
- [Asma and Van der Haegen 2010][research_asma_vanderhaegen_2010]
- [Aso et al 1993][research_aso_kumamoto_1993]
- [Aspidova et al 2022][research_aspidova_eremin_2022]
- [Assured crew return vehicle 1992][research_assured_crew_1992]
- [Asthana and Bhat 2012][research_asthana_bhat_2012]
- [Asyraf and Omar 2026][research_asyraf_omar_2026]
- [Atmeh and Subbarao 2016][research_atmeh_subbarao_2016]
- [Atmeh et al 2011][research_atmeh_altaq_2011]
- [Attri 1969][research_attri_1969]
- [Avtin et al 2021][research_avtin_baburov_2021]
- [Avtin et al 2021][research_avtin_baburov_2021_b]
- [Awin 2013][research_awin_2013]
- [Azarov and Chernovolov 2018][research_azarov_chernovolov_2018]
- [Azimov 2013][research_azimov_2013]
- [Azinheira et al 2000][research_azinheira_depaiva_2000]
- [Baca et al 2017][research_baca_stepan_2017]
- [Badarudin Mohamad Badry et al 2013][research_badarudinmohamadbadry_lee_2013]
- [Badikov et al 2026][research_badikov_volkova_2026]
- [Bagai et al 2010][research_bagai_cantono_2010]
- [Baggi et al 2022][research_baggi_2022]
- [Bai et al 2014][research_bai_ren_2014]
- [Bailet et al 2022][research_bailet_denis_2022]
- [Bailey and Smith 1982][research_bailey_1982]
- [Bailey et al 2025][research_bailey_2025]
- [Baillif et al 1995][research_baillif_bodepudi_1995]
- [Baimukhametov and White 2026][research_baimukhametov_white_2026]
- [Baker and Kramer 1979][research_baker_kramer_1979]
- [Bakulin et al 2016][research_bakulin_borzykh_2016]
- [Balakin et al 2018][research_balakin_elisov_2018]
- [Balakrishnan and Kurian 2014][research_balakrishnan_kurian_2014]
- [Balas 2003][research_balas_2003]
- [Balch 1979][research_balch_1979]
- [Baldini et al 2020][research_baldini_anandkumar_2020]
- [Balepin et al 2001][research_balepin_czysz_2001]
- [Balint et al 2010][research_balint_kaslik_2010]
- [Ball et al 1997][research_ball_oittinen_1997]
- [Ballard et al 2013][research_ballard_tanner_2013]
- [Baluragi et al 2011][research_baluragi_gupta_2011]
- [Banerjee and Padhi 2015][research_banerjee_padhi_2015]
- [Banerjee and Padhi 2017][research_banerjee_padhi_2017]
- [Banerjee and Padhi 2018][research_banerjee_padhi_2018]
- [Banerjee and Poovathingal 2021][research_banerjee_poovathingal_2021]
- [Banks and Fisher 2006][research_banks_2006]
- [Bannova 2006][research_bannova_2006]
- [Bantscheff and Breitsamter 2023][research_bantscheff_breitsamter_2023]
- [Bar-Itzhack and Porat 1980][research_baritzhack_porat_1980]
- [Baradell and McLellan 1963][research_baradell_1963]
- [Baran et al 2014][research_baran_blanchard_2014]
- [Barber and Johari 2001][research_barber_johari_2001]
- [Barbera 1980][research_barbera_1980]
- [Barczyk and Lynch 2011][research_barczyk_lynch_2011]
- [Barnes 1965][research_barnes_1965]
- [Barnes et al 2007][research_barnes_mcmichael_2007]
- [Barnhart et al 2007][research_barnhart_sullivan_2007]
- [Barret 1998][research_barret_1998]
- [Barret 1999][research_barret_1999]
- [Barthelemy 1989][research_barthelemy_1989]
- [Barton and Culp 1985][research_barton_1985]
- [Baselga et al 2009][research_baselga_garciaasenjo_2009]
- [Bashir et al 2017][research_bashir_khan_2017]
- [Batill 1982][research_batill_1982]
- [Batterbee et al 2007][research_batterbee_sims_2007]
- [Bauer 1964][research_bauer_1964]
- [Bauer and Kummer 1970][research_bauer_kummer_1970]
- [Baumgartner 1997][research_baumgartner_1997]
- [Baumgartner and Elvin 1995][research_baumgartner_1995]
- [Bayer 1998][research_bayer_1998]
- [Baysal and Luo 1999][research_baysal_1999]
- [Beachem 1964][research_beachem_1964]
- [Beck et al 2014][research_beck_driver_2014]
- [Becker 1964][research_becker_1964]
- [Bednarcyk et al 2023][research_bednarcyk_gustafson_2023]
- [Bedrov et al 1966][research_bedrov_vadichin_1966]
- [Bekar et al 2025][research_bekar_tanyeri_2025]
- [Belabbas et al 2010][research_belabbas_dautermann_2010]
- [Belcastro and Hogge 2004][research_belcastro_2004]
- [Bell 1965][research_bell_1965]
- [Benbow 1971][research_benbow_1971]
- [Bender 1969][research_bender_1969]
- [Benedetto et al 2014][research_benedetto_damico_2014]
- [Bennett 1947][research_bennett_1947]
- [Bennett 1947][research_bennett_1947_b]
- [Bennett and Abel 1981][research_bennett_abel_1981]
- [Bennett et al 2017][research_bennett_2017]
- [Bentley 2009][research_bentley_2009]
- [Bentley 2009][research_bentley_2009_b]
- [Bentley 2009][research_bentley_2009_c]
- [Benton 1989][research_benton_1989]
- [Benyamen and Keshmiri 2022][research_benyamen_2022]
- [Berend and Talbot 2006][research_berend_talbot_2006]
- [Beresford and Asteraki 1961][research_beresford_asteraki_1961]
- [Beresh 2022][research_beresh_2022]
- [Berg 1966][research_berg_1966]
- [Berger et al 2012][research_berger_tischler_2012]
- [Bergeron et al 2011][research_bergeron_tavan_2011]
- [Berkes 1992][research_berkes_1992]
- [Bernal and Yu 2015][research_bernal_yu_2015]
- [Berradi et al 2017][research_berradi_moutaouakkil_2017]
- [Berry 1982][research_berry_1982]
- [Berry 1999][research_berry_1999]
- [Berry 2000][research_berry_2000]
- [Berry et al 2002][research_berry_merski_2002]
- [Bertelrud et al 1992][research_bertelrud_kolodziej_1992]
- [Berthelot et al 2026][research_berthelot_craft_2026]
- [Berthold 1977][research_berthold_1977]
- [Berthold 1977][research_berthold_1977_b]
- [Bertrand-Noël et al 2022][research_bertrandnoel_bignaletcazalet_2022]
- [Besant 1994][research_besant_1994]
- [Betin 1991][research_betin_1991]
- [Betin 2026][research_betin_2026]
- [Betin et al 2023][research_betin_kaluzhynov_2023]
- [Betin et al 2023][research_betin_kyriienko_2023]
- [Bettinger 2021][research_bettinger_2021]
- [Bettis and Hosder 2010][research_bettis_hosder_2010]
- [Beyers et al 1997][research_beyers_ericsson_1997]
- [Bhagat et al 2011][research_bhagat_glussich_2011]
- [Bhatia and Geller 2020][research_bhatia_geller_2020]
- [Bhavana 2013][research_y_2013]
- [Bhungalia et al 2004][research_bhungalia_clewitt_2004]
- [Bian et al 2018][research_bian_nener_2018]
- [Bian et al 2024][research_bian_li_2024]
- [Biannic and Roos 2018][research_biannic_roos_2018]
- [Bickford et al 1997][research_bickford_bickmore_1997]
- [Bieniawski et al 2014][research_bieniawski_rosenzweig_2014]
- [Bigot and Murdoch 2025][research_bigot_2025]
- [Bihrle 1976][research_bihrle_1976]
- [Bin and Hongxin 2006][research_bin_hongxin_2006]
- [Binns et al 1996][research_binns_englehart_1996]
- [Binz et al 2017][research_binz_hartmann_2017]
- [Birkeland and Meuser 1999][research_birkeland_meuser_1999]
- [Bischoff et al 1974][research_bischoff_duffy_1974]
- [Bishop et al 2016][research_bishop_crain_2016]
- [Bizzarri and Hendrick 2003][research_bizzarri_hendrick_2003]
- [Black 1964][research_black_1964]
- [Black 1968][research_black_1968]
- [Blackmore et al 2010][research_blackmore_acikmese_2010]
- [Blackstock 1970][research_blackstock_1970]
- [Blades and Redgrave 2000][research_blades_redgrave_2000]
- [Blanchard 1961][research_blanchard_1961]
- [Bledsoe 2011][research_bledsoe_2011]
- [Bledsoe and Bernatovich 2015][research_bledsoe_2015]
- [Bleimeyer 1981][research_bleimeyer_1981]
- [Blevins et al 2022][research_blevins_mckinnis_2022]
- [Bliamis et al 2018][research_bliamis_panagiotou_2018]
- [Blodgett et al 1986][research_blodgett_conrad_1986]
- [Blom 2017][research_blom_2017]
- [Blonigan et al 2025][research_blonigan_tencer_2025]
- [Blosser 1997][research_blosser_1997]
- [Blosser 2002][research_blosser_2002]
- [Blosser 2004][research_blosser_2004]
- [Bo et al 2017][research_bo_yuan_2017]
- [Bo et al 2020][research_bo_xiaogang_2020]
- [Bobko 2012][research_bobko_2012]
- [Bobylev et al 2008][research_bobylev_dyadkin_2008]
- [Bodkin et al 2024][research_bodkin_akamine_2024]
- [Boeing Scientific Research Labs Seattle Wa 1963][research_wa_1963]
- [Bogar et al 1996][research_bogar_butters_1996]
- [Bohn et al 1970][research_bohn_1970]
- [Bohon et al 1975][research_bohon_sawyer_1975]
- [Bohon et al 1977][research_bohon_shideler_1977]
- [Boisseau 1955][research_boisseau_1955]
- [Bolender and Doman 2005][research_bolender_doman_2005]
- [Bolt 1981][research_bolt_1981]
- [Bonetti et al 2013][research_bonetti_dezaiacomo_2013]
- [Bonnal and Caporicci 2000][research_bonnal_caporicci_2000]
- [Bonner and Pride 1976][research_bonner_1976]
- [Boothe et al 1974][research_boothe_chen_1974]
- [Borden et al 1999][research_borden_1999]
- [Borges et al 2026][research_borges_burnside_2026]
- [Borodin 2001][research_borodin_2001]
- [Borowczyk et al 2017][research_borowczyk_nguyen_2017]
- [Borowczyk et al 2017][research_borowczyk_nguyen_2017_b]
- [Borzykh et al 2013][research_borzykh_voronin_2013]
- [Boschetti et al 2004][research_boschetti_cardenas_2004]
- [Boskovic and Redding 2009][research_boskovic_redding_2009]
- [Bossi et al 1989][research_bossi_1989]
- [Bossi et al 1991][research_bossi_1991]
- [Bourne and Kirsten 1983][research_bourne_1983]
- [Bouslog et al 1993][research_bouslog_an_1993]
- [Bouslog et al 1998][research_bouslog_1998]
- [Bouyahiaoui et al 2020][research_bouyahiaoui_haoui_2020]
- [Bovais et al 1992][research_bovais_haupt_1992]
- [Boye 2020][research_boye_2020]
- [Boyer 1964][research_boyer_1964]
- [Boylan 1965][research_boylan_1965]
- [Brady 1969][research_brady_1969]
- [Brand 1981][research_brand_1981]
- [Brando et al 2016][research_brando_dannier_2016]
- [Brandon et al 1996][research_brandon_1996]
- [Brandon et al 1997][research_brandon_1997]
- [Brandon M. Jones][research_jones_nd]
- [Brandt et al 2019][research_brandt_mclaughlin_2019]
- [Brassard et al 2019][research_brassard_laforte_2019]
- [Bratt 1965][research_bratt_1965]
- [Braun 1958][research_braun_1958]
- [Brennan and McDaniel 1994][research_brennan_mcdaniel_1994]
- [Brevault et al 2019][research_brevault_balesdent_2019]
- [Brevault et al 2020][research_brevault_balesdent_2020]
- [Brevault et al 2020][research_brevault_balesdent_2020_b]
- [Brice and Sugano 1978][research_brice_sugano_1978]
- [Brice et al 1966][research_brice_perkins_1966]
- [Brieger et al 2008][research_brieger_ossmann_2008]
- [Briggs et al 1952][research_briggs_1952]
- [Brinda and Dasgupta 2006][research_brinda_dasgupta_2006]
- [Brinda et al 2005][research_brinda_arora_2005]
- [Brink et al 2010][research_brink_hurtado_2010]
- [Brion et al 2006][research_brion_aki_2006]
- [Britcher and Landman 2024][research_britcher_landman_2024]
- [Britcher et al 2024][research_britcher_datta_2024]
- [Brociek et al 2023][research_brociek_hetmaniok_2023]
- [Brock][research_brock_nd]
- [Brock and Franke 2004][research_brock_franke_2004]
- [Brockers et al 2012][research_brockers_2012]
- [Broglio 1961][research_broglio_1961]
- [Brooks 1986][research_brooks_1986]
- [Brooks et al 1962][research_brooks_swann_1962]
- [Broussard et al 1983][research_broussard_bryant_1983]
- [Brown 2023][research_brown_2023]
- [Brown and Duhon 1965][research_brown_duhon_1965]
- [Brown and Olds 2005][research_brown_olds_2005]
- [Brown and Olds 2006][research_brown_olds_2006]
- [Brown and Redwine 1948][research_brown_1948]
- [Brown et al 1983][research_brown_1983]
- [Brown et al 1984][research_brown_1984]
- [Brown et al 2002][research_brown_yates_2002]
- [Brown et al 2006][research_brown_yates_2006]
- [Bruce 1964][research_bruce_1964]
- [Bruckner et al 2010][research_bruckner_vangraas_2010]
- [Brunch et al 2002][research_brunch_gilbreath_2002]
- [Brune et al 2017][research_brune_hosder_2017]
- [Brunner et al 2021][research_brunner_kiefer_2021]
- [Brusa et al 2025][research_brusa_delprete_2025]
- [Bryant et al 1998][research_bryant_tigges_1998]
- [Bryson 1969][research_brysonjr_1969]
- [Brzozowski et al 2014][research_brzozowski_kordowski_2014]
- [Bu et al 2016][research_bu_ai_2016]
- [Bu et al 2019][research_bu_lei_2019]
- [Buchnev and Danilov 2026][research_buchnev_danilov_2026]
- [Budd et al 1993][research_budd_1993]
- [Buell and Kenyon 1959][research_buell_1959]
- [Buell and Oleinik 1998][research_buell_oleinik_1998]
- [Bufalino 1995][research_bufalino_1995]
- [Buffo 1990][research_buffo_1990]
- [Bugg and Sleeman 1967][research_bugg_1967]
- [Buhler and Linhart 1969][research_buhler_1969]
- [Bukov and Bykov 2017][research_bukov_bykov_2017]
- [Bull and Foster 1974][research_bull_foster_1974]
- [Bull et al 1981][research_bull_1981]
- [Bulmer 1973][research_bulmer_1973]
- [Bunge et al 2015][research_bunge_munerasavino_2015]
- [Burchett 2004][research_burchett_2004]
- [Burgan and Paddison 1974][research_burgan_1974]
- [Burgess 1970][research_burgess_1970]
- [Burkhardt et al 1999][research_burkhardt_graesslin_1999]
- [Burkhart et al 2013][research_burkhart_2013]
- [Burns 1970][research_burns_1970]
- [Burns 1992][research_burnsiii_1992]
- [Burt and Haigh 1968][research_burt_haigh_1968]
- [Burton 1981][research_burton_1981]
- [Bushnell 2006][research_bushnell_2006]
- [Busnardo et al 2011][research_busnardo_aitken_2011]
- [Butt 2013][research_butt_2013]
- [Butt et al 2010][research_butt_yan_2010]
- [Butt et al 2011][research_butt_yan_2011]
- [Butt et al 2011][research_butt_yan_2011_b]
- [Butt et al 2013][research_butt_yan_2013]
- [Butter 2017][research_butter_2017]
- [Byrne et al 1996][research_byrne_sturgis_1996]
- [Cady 1997][research_cady_1997]
- [Cady and Olsen 1996][research_cady_olsen_1996]
- [Cai et al 2013][research_cai_jianmei_2013]
- [Cai et al 2013][research_cai_song_2013]
- [Cai et al 2014][research_cai_song_2014]
- [Cai et al 2024][research_cai_lei_2024]
- [Cai et al 2024][research_cai_yang_2024]
- [Cai et al 2025][research_cai_gao_2025]
- [Cain and Snelling 2022][research_cain_snelling_2022]
- [Calhoun 2000][research_calhoun_2000]
- [Calise and Bae 1987][research_calise_bae_1987]
- [Call et al 1981][research_call_kelly_1981]
- [Callerio 1940][research_callerio_1940]
- [Campbell 1991][research_campbell_1991]
- [Campbell and Kresge 2003][research_campbell_kresge_2003]
- [Campbell and Seacord 1943][research_campbell_1943]
- [Campbell et al 2007][research_campbell_lee_2007]
- [Campi et al 2019][research_campi_cruciani_2019]
- [Camponogara et al 2019][research_camponogara_oliveira_2019]
- [Campos 1989][research_campos_1989]
- [Canniff 1969][research_canniff_1969]
- [Cao and Zhang 2015][research_cao_zhang_2015]
- [Cao et al 2012][research_cao_ding_2012]
- [Cao et al 2024][research_cao_zhou_2024]
- [Caogen et al 2008][research_caogen_hongjun_2008]
- [Capderou 2012][research_capderou_2012]
- [Cappello et al 2016][research_cappello_sabatini_2016]
- [Carloni and Bousson 2016][research_carloni_bousson_2016]
- [Carman 1980][research_carman_1980_c]
- [Carman and Montez 1980][research_carman_1980]
- [Carman and Montez 1980][research_carman_1980_b]
- [Carman et al 1980][research_carman_jb_1980]
- [Carnes et al 2015][research_carnes_bakker_2015]
- [Carpenter et al 2019][research_carpenter_chocron_2019]
- [Carraway 1988][research_carrawayiii_1988]
- [Carson et al 2015][research_carson_robertson_2015]
- [Carten 1978][research_carten_1978]
- [Cassanto 1966][research_cassanto_1966]
- [Cassell et al 2019][research_cassell_2019]
- [Castaldi et al 2023][research_castaldi_emami_2023]
- [Castro et al 2006][research_castro_bennani_2006]
- [Cavallo and Ferrara 1996][research_cavallo_ferrara_1996]
- [Cavallo et al 1996][research_cavallo_demaria_1996]
- [Cavdar and Mooij 2024][research_cavdar_mooij_2024]
- [Caves and Kirkland 1999][research_caves_kirkland_1999]
- [Cazin 1989][research_cazin_1989]
- [Cejpek 2018][research_cejpek_2018]
- [Cesetti et al 2009][research_cesetti_frontoni_2009]
- [Cetin and Kutay 2016][research_cetin_kutay_2016]
- [Cetin et al 2010][research_cetin_kurnaz_2010]
- [Cetinkaya and Ozkol 2017][research_cetinkaya_ozkol_2017]
- [Chae et al 2019][research_chae_mankodi_2019]
- [Chai and Mason 1996][research_chai_mason_1996]
- [Chai et al 2017][research_chai_savvaris_2017]
- [Chai et al 2019][research_chai_savvaris_2019]
- [Chai et al 2019][research_chai_savvaris_2019_b]
- [Chaloff et al 1974][research_chaloff_1974]
- [Chamberlin and Blaha 1973][research_chamberlin_blaha_1973]
- [Chambers 1980][research_chambers_1980]
- [Chambers 1988][research_chambers_1988]
- [Chambers 2010][research_chambers_2010]
- [Chambers and Iliff 1981][research_chambers_1981]
- [Chambers et al 2019][research_chambers_titchener_2019]
- [Chamitoff 1994][research_chamitoff_1994]
- [Chamitoff 1995][research_chamitoff_1995]
- [Chan and Pervan 2011][research_chan_pervan_2011]
- [Chan et al 2023][research_chan_shea_2023]
- [Chandramohan et al 2010][research_chandramohan_yucelen_2010]
- [Chang 2016][research_chang_2016]
- [Chang et al 2015][research_chang_ryu_2015]
- [Chang et al 2016][research_chang_yang_2016]
- [Chang et al 2018][research_chang_guo_2018]
- [Chang et al 2018][research_chang_miao_2018]
- [Chang et al 2021][research_chang_yee_2021]
- [Chang et al 2022][research_chang_huang_2022]
- [Chang et al 2026][research_chang_seo_2026]
- [Changsheng et al 2006][research_changsheng_wuxing_2006]
- [Channon and Barry 1967][research_channon_barry_1967]
- [Chao et al 2017][research_chao_2017]
- [Chapman and Compton 1964][research_chapman_1964]
- [Charette et al 1998][research_charette_leonard_1998]
- [Charters 1962][research_charters_1962]
- [Charters et al 1955][research_charters_1955]
- [Chase 1996][research_chase_1996]
- [Chase 1997][research_chase_1997]
- [Chase and Chase 1997][research_chase_chase_1997]
- [Chase and McKinney 2005][research_chase_mckinney_2005]
- [Chase et al 1997][research_chase_mckinney_1997]
- [Chatterji et al 1995][research_chatterji_menon_1995]
- [Chaudhary et al 2001][research_chaudhary_2001]
- [Chavagnac 2003][research_chavagnac_2003]
- [Chavagnac et al 2013][research_chavagnac_gai_2013]
- [Chawla et al 2010][research_chawla_sarmah_2010]
- [Che et al 2012][research_che_liu_2012]
- [Chedrik et al 2004][research_chedrik_2004]
- [Chelnokov 2019][research_chelnokov_2019]
- [Chelnokov and Perelyaev 2020][research_chelnokov_perelyaev_2020]
- [Chen 2018][research_chen_2018]
- [Chen 2021][research_chen_2021]
- [Chen 2023][research_chen_2023]
- [Chen and Blosser 2002][research_chen_blosser_2002]
- [Chen and He 2025][research_chen_he_2025]
- [Chen and Li 2016][research_chen_li_2016]
- [Chen and Wang 2023][research_chen_wang_2023]
- [Chen and Xue 2023][research_chen_xue_2023]
- [Chen et al 2006][research_chen_squire_2006]
- [Chen et al 2011][research_chen_yu_2011]
- [Chen et al 2013][research_chen_2013]
- [Chen et al 2013][research_chen_2013_b]
- [Chen et al 2013][research_chen_nie_2013]
- [Chen et al 2016][research_chen_zhu_2016]
- [Chen et al 2018][research_chen_ma_2018]
- [Chen et al 2018][research_chen_mu_2018]
- [Chen et al 2020][research_chen_zhou_2020]
- [Chen et al 2020][research_chen_zhou_2020_b]
- [Chen et al 2020][research_chen_zhou_2020_c]
- [Chen et al 2020][research_chen_zhou_2020_d]
- [Chen et al 2020][research_chen_zhou_2020_e]
- [Chen et al 2021][research_chen_chang_2021]
- [Chen et al 2022][research_chen_man_2022]
- [Chen et al 2023][research_chen_han_2023]
- [Chen et al 2025][research_chen_huang_2025]
- [Chen et al 2025][research_chen_shi_2025]
- [Chen et al 2025][research_chen_wu_2025]
- [Chen et al 2025][research_chen_yang_2025]
- [Chen et al 2025][research_chen_zhu_2025]
- [Chen Liu et al 2016][research_chenliu_chaoyangdong_2016]
- [Chen Songyue et al 2018][research_chensongyue_wangliang_2018]
- [Cheney 1988][research_cheney_1988]
- [Cheney and Pham 1988][research_cheney_pham_1988]
- [Cheng and Lai 2025][research_cheng_lai_2025]
- [Cheng and Shyur 2025][research_cheng_shyur_2025]
- [Cheng et al 2014][research_cheng_li_2014]
- [Cheng et al 2016][research_cheng_sheng_2016]
- [Cheng et al 2021][research_cheng_jing_2021]
- [Cheng et al 2023][research_cheng_hu_2023]
- [Cheng et al 2026][research_cheng_wang_2026]
- [Chernenko and Burnashev 2022][research_chernenko_burnashev_2022]
- [Chernodarov et al 2021][research_chernodarov_patrikeev_2021]
- [Chernodarov et al 2022][research_chernodarov_patrikeev_2022]
- [Chernyi and Gonor 1973][research_chernyi_gonor_1973]
- [Chevalier et al 2026][research_chevalier_dubroca_2026]
- [Chhetri et al 2026][research_chhetri_jetawatthana_2026]
- [Chi et al 2009][research_chi_xiaopeng_2009]
- [Chiba et al 2006][research_chiba_obayashi_2006]
- [Chiesa et al 2005][research_chiesa_corpino_2005]
- [Chiesa et al 2005][research_chiesa_grassi_2005]
- [Chiesa et al 2012][research_chiesa_cardile_2012]
- [Childers et al 2001][research_childers_2001]
- [Chimonas 1986][research_chimonas_1986]
- [Chin 1970][research_chin_1970]
- [Chin 1985][research_chin_1985]
- [Chin et al 1964][research_chin_hearne_1964]
- [Chinnaraj et al 2024][research_chinnaraj_kim_2024]
- [Chinvorarat 2021][research_chinvorarat_2021]
- [Chinvorarat and Vallikul 2021][research_chinvorarat_vallikul_2021]
- [Chirayath and Bindu 2014][research_chirayath_bindu_2014]
- [Chitrakaran et al 2005][research_chitrakaran_dawson_2005]
- [Chiu and Pitts 1991][research_chiu_pitts_1991]
- [Cho and Nagati 1995][research_cho_1995]
- [Choi et al 2005][research_choi_lim_2005]
- [Choo et al 2018][research_choo_mun_2018]
- [Choong and Lim 2026][research_choong_lim_2026]
- [Chowdhary and Johnson 2008][research_chowdhary_johnson_2008]
- [Chowdhury and Keshmiri 2022][research_chowdhury_keshmiri_2022]
- [Chowdhury et al 2026][research_chowdhury_joshi_2026]
- [Christol 1993][research_christol_1993]
- [Christoph 1985][research_christoph_1985]
- [Chu and Li 2017][research_chu_li_2017]
- [Chu and Mooij 2001][research_chu_mooij_2001]
- [Chu et al 2016][research_chu_guo_2016]
- [Chu et al 2024][research_chu_liu_2024]
- [Chu et al 2025][research_chu_lv_2025]
- [Chuang et al 2021][research_chuang_yubing_2021]
- [Chudej 1994][research_chudej_1994]
- [Chung et al 2025][research_chung_echigo_2025]
- [Clancy 2001][research_clancy_2001]
- [Clapp 1965][research_clapp_1965]
- [Clapp 1995][research_clapp_1995]
- [Clark et al 1978][research_clark_dicus_1978]
- [Clarke and Randall 1997][research_clarke_randall_1997]
- [Clary et al 1984][research_clary_1984]
- [Clary et al 1984][research_clary_1984_b]
- [Clayton and Tinker 1992][research_clayton_tinker_1992]
- [Clemmons 1971][research_clemmons_1971]
- [Cliff et al 1992][research_cliff_well_1992]
- [Clos-Cot et al 2018][research_closcot_templai_2018]
- [Clough 1990][research_clough_1990]
- [Cocchioni et al 2014][research_cocchioni_mancini_2014]
- [Cochran et al 1978][research_cochran_1978]
- [Cochran et al 1979][research_cochran_1979]
- [Cochrane and Graham 1971][research_cochrane_1971]
- [Cockayne and Rusnak 1971][research_cockayne_1971]
- [Cohanim and Collins 2009][research_cohanim_2009]
- [Cohen et al 1994][research_cohen_parkinson_1994]
- [Cohen et al 1994][research_cohen_pervan_1994]
- [Coker et al 1978][research_coker_hoffman_1978]
- [Colgren 1996][research_colgren_1996]
- [Collicott and Woffinden 2021][research_collicott_woffinden_2021]
- [Collinson 1963][research_collinson_1963]
- [Colwell 1966][research_colwell_1966]
- [Comer et al 2024][research_comer_bhandari_2024]
- [Comer et al 2026][research_comer_atkinson_2026]
- [Comer et al 2026][research_comer_chakraborty_2026]
- [Computer vision-based approach for 2025][research_computer_vision_2025]
- [Condomines 2018][research_condomines_2018]
- [Constantin et al 2022][research_constantin_2022]
- [Contreras and Hajiyev 2019][research_contreras_hajiyev_2019]
- [Cook 1981][research_cook_1981]
- [Cook 1995][research_cook_1995]
- [Cook 1996][research_cook_1996]
- [Cook and Giddings 1984][research_cook_1984]
- [Cooper et al 1984][research_cooper_miserentino_1984]
- [Coopmans et al 2015][research_coopmans_podhradsky_2015]
- [Corban et al 2001][research_corban_gilbert_2001]
- [Corban et al 2004][research_corban_gilbert_2004]
- [Cordes and Hertzfeld 1997][research_cordes_hertzfeld_1997]
- [Cordoba 2007][research_cordoba_2007]
- [Cork and Moore 1967][research_cork_moore_1967]
- [Cornelison and Arnold 1997][research_cornelison_1997]
- [Coskun and Genc 2021][research_coskun_genc_2021]
- [Costa and Sachs 2002][research_costa_sachs_2002]
- [Coue 2003][research_coue_2003]
- [Courtin et al 2020][research_courtin_hansman_2020]
- [Coutinho et al 2016][research_coutinho_baptista_2016]
- [Cowart and Olds 2000][research_cowart_olds_2000]
- [Cowling 2011][research_cowling_2011]
- [Cox 1978][research_cox_1978]
- [Cox et al 2012][research_cox_cunningham_2012]
- [Crain et al 2016][research_crain_2016]
- [Crassidis 2005][research_crassidis_2005]
- [Crassidis and Mook 1991][research_crassidis_mook_1991]
- [Crassidis and Mook 1992][research_crassidis_mook_1992]
- [Crassidis et al 1993][research_crassidis_mook_1993]
- [Crawford and Duiven 1973][research_crawford_1973]
- [Crespillo et al 2016][research_crespillo_grosch_2016]
- [Crist and Symes 1981][research_crist_symes_1981]
- [Crogan 1961][research_crogan_1961]
- [Croke et al 2024][research_croke_green_2024]
- [Cronin 2013][research_cronin_2013]
- [Croom and Fournier 1966][research_croom_1966]
- [Croom et al 2000][research_croom_2000]
- [Cross 1989][research_cross_1989]
- [Crouch 1999][research_crouch_1999]
- [Cruz][research_cruz_nd_b]
- [Cruz and Green 2019][research_cruz_green_2019]
- [Cruz et al][research_cruz_nd]
- [Cui et al 2017][research_cui_zhao_2017]
- [Cui et al 2021][research_cui_zhang_2021]
- [Cui et al 2022][research_cui_chen_2022]
- [Cui et al 2025][research_cui_zhen_2025]
- [Cui et al 2026][research_cui_li_2026]
- [Culler et al 2007][research_culler_williams_2007]
- [Cummings 2003][research_cummings_2003]
- [Cunningham et al 2008][research_cunningham_foster_2008]
- [Currey 1969][research_currey_1969]
- [Currin et al 2011][research_currin_2011]
- [Curtin 2026][research_curtin_2026]
- [Curtis 2005][research_curtis_2005]
- [Curtiss and Zhao 1988][research_curtiss_1988]
- [Cusick and Kontis 2019][research_cusick_kontis_2019]
- [Cvrlje 1999][research_cvrlje_1999]
- [Czysz and Murthy 1996][research_czysz_murthy_1996]
- [D'Andrea et al 2022][research_dandrea_didomenico_2022]
- [D'Angelo et al 1999][research_dangelo_minisci_1999]
- [D'Souza and D'Souza 1997][research_dsouza_dsouza_1997]
- [D'Souza et al 2022][research_dsouza_mcguire_2022]
- [Da Costa 2003][research_dacosta_2003]
- [da Costa and Sachs 2002][research_dacosta_sachs_2002]
- [da Costa and Sachs 2003][research_dacosta_sachs_2003]
- [Dabas et al 2025][research_dabas_sheikh_2025]
- [Dai and Sun 2023][research_dai_sun_2023]
- [Dai et al 2010][research_dai_li_2010]
- [Dai et al 2017][research_dai_liu_2017]
- [Dai et al 2018][research_dai_tan_2018]
- [Daidzic 2016][research_daidzic_2016]
- [Dalang et al 2023][research_dalang_kulathunga_2023]
- [Dan Rugescu 2006][research_danrugescu_2006]
- [Dan Tuckness 1994][research_dantuckness_1994]
- [Dana and Gentry 1970][research_dana_1970]
- [Dana et al 1969][research_dana_1969]
- [Dang et al 2022][research_dang_stern_2022]
- [Daniel and Ramusat 2005][research_daniel_ramusat_2005]
- [Daniel et al 2004][research_daniel_tumino_2004]
- [Daniels and Dryden, 1974, An Airborne Telescope-Camera System for High-Resolution Reentry Vehicle Photography][research_daniels_dryden_1974]
- [Dantsker 2024][research_dantsker_2024]
- [Dantsker 2024][research_dantsker_2024_b]
- [Dantsker and Mancuso 2019][research_dantsker_mancuso_2019]
- [Dantsker and Selig 2015][research_dantsker_selig_2015]
- [Dantsker et al 2018][research_dantsker_vahora_2018]
- [Dantsker et al 2022][research_dantsker_haviland_2022]
- [Dantsker et al 2025][research_dantsker_mancuso_2025]
- [Daoxin 2021][research_daoxin_2021]
- [Daquan Tang et al 2016][research_daquantang_yongkangjiao_2016]
- [Daryabeigi 2002][research_daryabeigi_2002]
- [Das et al 2023][research_das_pei_2023]
- [Das et al 2024][research_das_wang_2024]
- [Dasaro 1970][research_dasaro_1970]
- [Daugherty and Stubbs 1992][research_daugherty_stubbs_1992]
- [Daugherty et al 1988][research_daugherty_yager_1988]
- [Daughetee 1974][research_daughetee_1974]
- [Daum and Mollmann 2017][research_daum_mollmann_2017]
- [Davis 1968][research_davis_1968]
- [Davis 1969][research_davis_1969]
- [Davis 1989][research_davis_1989]
- [Davis 2002][research_davis_2002]
- [Davis et al 1985][research_davis_1985]
- [Davis et al 2003][research_davis_engler_2003]
- [Dayman 1962][research_dayman_1962]
- [Dayman 1965][research_dayman_1965]
- [Dayman 1966][research_dayman_1966]
- [Dayman 1971][research_daymanjr_1971]
- [de Alvear Cárdenas and Looye 2021][research_dealvearcardenas_looye_2021]
- [De Divitiis 2003][research_dedivitiis_2003]
- [de Divitiis and Corraro 2007][research_dedivitiis_corraro_2007]
- [De Giorgis et al 1999][research_degiorgis_borriello_1999]
- [de Lafontaine 1992][research_delafontaine_1992]
- [de Lafontaine et al 2006][research_delafontaine_levesque_2006]
- [De Matteis 2003][research_dematteis_2003]
- [de Mûelenaere and Alonso 2018][research_demuelenaere_alonso_2018]
- [de Paula et al 2026][research_depaula_quintero_2026]
- [de Paula Vieira et al 2018][research_depaulavieira_sperandiodiasgoncalves_2018]
- [de Ridder and Mooij 2009][research_deridder_mooij_2009]
- [De Ridder and Mooij 2011][research_deridder_mooij_2011]
- [De Vita et al 2015][research_devita_viola_2015]
- [De Wagter and Meulenbeld 2019][research_dewagter_meulenbeld_2019]
- [Dean 2024][research_dean_2024]
- [DeBra et al 1981][research_debra_breakwell_1981]
- [Dec and Braun 2006][research_dec_braun_2006]
- [Dec and Braun 2013][research_dec_braun_2013]
- [Deel et al 1972][research_deel_1972]
- [Deets and Brown 1986][research_deets_1986]
- [Defense Science Board Washington Dc 1992][research_defensescienceboardwashingtondc_1992]
- [Del Corso et al 2015][research_corso_2015]
- [Delaune et al 2010][research_delaune_derosa_2010]
- [Delaune et al 2016][research_delaune_lebesnerais_2016]
- [Deloach et al 2009][research_deloach_2009]
- [Delprete et al 2023][research_delprete_dagna_2023]
- [Demarchi and Haning 1978][research_demarchi_haning_1978]
- [DeMars et al 2014][research_demars_darling_2014]
- [Demidovich 2017][research_demidovich_2017]
- [Demir and Seyfullah Babaarslan 2021][research_demir_seyfullahbabaarslan_2021]
- [Demo 1986][research_demo_1986]
- [Denardo and Canning 1952][research_denardo_1952]
- [Denaro and Beser 1986][research_denaro_1986]
- [Deng and Duan 2016][research_deng_duan_2016]
- [Deng et al 2025][research_deng_xu_2025]
- [Deniz et al 2018][research_deniz_balakrishnan_2018]
- [Depaola et al 2018][research_depaola_chimento_2018]
- [Department of Astrophysics and Ferreira Santos 2022][research_ferreirasantos_2022]
- [Der Kiureghian 2001][research_derkiureghian_2001]
- [Dermer][research_dermer_nd]
- [Desai and Lyons 2005][research_desai_2005]
- [Desai et al 2008][research_desai_2008]
- [Desao et al 2006][research_desao_2006]
- [Deslandes and Donauer 2010][research_deslandes_2010]
- [Devesa et al 2004][research_devesa_jourdan_2004]
- [Dey et al 2018][research_dey_giri_2018]
- [Deyst 1968][research_deyst_1968]
- [Dhanasekaran et al 2011][research_dhanasekaran_balamurali_2011]
- [Di Campli Bayard de Volo and Di Pietro 2018][research_dicamplibayarddevolo_dipietro_2018]
- [Di Leo et al 2018][research_dileo_leon_2018]
- [Dieffenbach 1995][research_dieffenbach_1995]
- [Dieroff and Schaenzer 1990][research_dieroff_schaenzer_1990]
- [DiFranco 1971][research_difranco_1971]
- [Digges 1971][research_digges_1971]
- [Dileep et al 2025][research_r_ss_2025]
- [Dill and Uijt de Haag 2016][research_dill_uijtdehaag_2016]
- [Dillman et al 2020][research_dillman_slagle_2020]
- [Dimri and Matai 2011][research_dimri_matai_2011]
- [Din et al 2020][research_din_janujua_2020]
- [Ding 2015][research_ding_2015]
- [Ding et al 2016][research_ding_guo_2016]
- [Ding et al 2023][research_ding_li_2023]
- [Dirling and Eitman 1984][research_dirlingjr_eitman_1984]
- [Dirs 1966][research_dirs_1966]
- [Disotell et al 2026][research_disotell_nietert_2026]
- [Dissel et al 2007][research_dissel_kothari_2007]
- [Distefano and Leonardi 2018][research_distefano_leonardi_2018]
- [Dix and Mattasits 1980][research_dix_mattasits_1980]
- [Di̇nç 2021][research_dinc_2021]
- [Doche et al 2001][research_doche_verniermounier_2001]
- [Doenecke 1967][research_doenecke_1967]
- [Doherr et al 1997][research_doherr_jann_1997]
- [Doihara and Nishida 2002][research_doihara_nishida_2002]
- [Doland 1976][research_doland_1976]
- [Doman 2004][research_doman_2004]
- [Donahue 1997][research_donahue_1997]
- [Donahue and Farrell 1979][research_donahue_farrell_1979]
- [Donahue et al 2008][research_donahue_weldon_2008]
- [Donelson et al 1989][research_donelson_lewerenz_1989]
- [Dong et al 2017][research_dong_zong_2017]
- [Dong et al 2023][research_dong_huang_2023]
- [Dong et al 2023][research_dong_li_2023]
- [Dong et al 2023][research_dong_wu_2023]
- [Dong et al 2025][research_dong_zhao_2025]
- [Dongpo et al 2025][research_dongpo_aiying_2025]
- [Donovan 1969][research_donovan_1969]
- [Dorr et al 1994][research_dorr_1994]
- [Dorsey et al 1999][research_dorsey_wu_1999]
- [Dorsey et al 2000][research_dorsey_myers_2000]
- [Dorsey et al 2004][research_dorsey_poteet_2004]
- [Dou and Duan 2017][research_dou_duan_2017]
- [Dougherty 1975][research_dougherty_1975]
- [Dougherty and Lee 2016][research_dougherty_lee_2016]
- [Douglas 2003][research_douglas_2003]
- [Douglas Aircraft Co Long Beach Ca 1962][research_douglasaircraftcolongbeachca_1962]
- [Douglas Aircraft Co Long Beach Ca 1963][research_ca_1963_b]
- [Douglas et al 2021][research_douglas_ellis_2021]
- [Downing and Bryant 1979][research_downing_1979]
- [Downing and Bryant 1987][research_downing_bryant_1987]
- [Downing et al 1981][research_downing_1981]
- [Doyle 1982][research_doyle_1982]
- [Dr. Michael Johnson 2020][research_drmichaeljohnson_2020]
- [Dragan and Stoica 1997][research_dragan_stoica_1997]
- [Dragone 2000][research_dragone_2000]
- [Draper 1943][research_draper_1943]
- [Draper 1981][research_draper_1981]
- [Draper 1981][research_draper_1981_b]
- [Draper and Hewes 1948][research_draper_1948]
- [Driessen 2005][research_driessen_2005]
- [Drinkwater and Cooper 1958][research_drinkwater_1958]
- [Driver et al 2014][research_driver_carballo_2014]
- [Droandi et al 2014][research_droandi_2014]
- [Droege 1947][research_droege_1947]
- [Du and Zhang 2020][research_du_zhang_2020]
- [Du et al 2016][research_du_jing_2016]
- [Du et al 2025][research_du_zhang_2025]
- [Duan et al 2022][research_duan_yuan_2022]
- [Dubois-Matra and Bishop 2004][research_duboismatra_bishop_2004]
- [Duda 2016][research_duda_2016]
- [Duda et al 2022][research_duda_deuring_2022]
- [Duehring et al 2023][research_duehring_egan_2023]
- [Dufour et al 2015][research_dufour_demuelenaere_2015]
- [Duke et al 1983][research_duke_swann_1983]
- [Dumbacher and Klevatt 1994][research_dumbacher_klevatt_1994]
- [Dunker et al 2025][research_dunker_berdermann_2025]
- [Dunn 1990][research_dunn_1990]
- [Durand and Wasicko 1967][research_durand_wasicko_1967]
- [Durbin 1959][research_durbin_1959]
- [Durmuşoğlu 2026][research_durmusoglu_2026]
- [Durocher 1978][research_durocher_1978]
- [Durán-Giraldo et al 2022][research_durangiraldo_gonzalezsierra_2022]
- [Duston et al 2004][research_duston_seghi_2004]
- [Dutasatria and Darma 2020][research_dutasatria_darma_2020]
- [Dutta et al 2024][research_dutta_guechaahumada_2024]
- [Dwyer 1994][research_dwyer_1994]
- [Dynnikov 2020][research_dynnikov_2020]
- [Earl 1967][research_earl_1967]
- [Ebner and Mark 1977][research_ebner_mark_1977]
- [Eck and Geering 2003][research_eck_geering_2003]
- [Eckmann et al 1997][research_eckmann_cotta_1997]
- [Edwards 1969][research_edwards_1969]
- [Edwards 1972][research_edwards_1972]
- [Edwards 1981][research_edwards_1981]
- [Edwards and Foster 1973][research_edwards_1973]
- [Edwards et al 1975][research_edwards_1975]
- [Edwards et al 2010][research_edwards_mavris_2010]
- [Efremov et al 2023][research_efremov_efremov_2023]
- [Eggers et al 2011][research_eggers_dittrich_2011]
- [Eichhorn and Silvestre 2023][research_eichhorn_silvestre_2023]
- [Eichhorn et al 2022][research_eichhorn_fritzsche_2022]
- [Eigenmann et al 1984][research_eigenmann_kitzmiller_1984]
- [Eilertson 1975][research_eilertson_1975]
- [Eitner et al 2013][research_eitner_braun_2013]
- [Eklund 2004][research_eklund_2004]
- [El-Diasty and Pagiatakis 2008][research_eldiasty_pagiatakis_2008]
- [El-Mowafy 2005][research_elmowafy_2005]
- [El-Rabbany 2006][research_elrabbany_2006]
- [Eldred 1953][research_eldred_1953]
- [Eldridge-Allegra et al 2023][research_eldridgeallegra_xu_2023]
- [Elias 1974][research_elias_1974]
- [Elkaim et al 2014][research_elkaim_lie_2014]
- [Ellery et al 2006][research_ellery_richter_2006]
- [Elliott 1968][research_elliott_1968]
- [Ellis 1989][research_ellis_1989]
- [Elvin 1996][research_elvin_1996]
- [Ely et al 2010][research_ely_heyne_2010]
- [Ema 1992][research_ema_1992]
- [Emery and Bardot 2006][research_emery_bardot_2006]
- [Engel and Putnam 2025][research_engel_putnam_2025]
- [Engle and Truly 1977][research_engle_1977]
- [Enmi et al 2018][research_enmi_qian_2018]
- [Enriquez 2025][research_enriquez_2025]
- [Epp et al 2015][research_epp_robertson_2015]
- [Erasmus et al 2014][research_erasmus_hattingh_2014]
- [Ernst and Leidinger 1988][research_ernst_leidinger_1988]
- [Erwin 1990][research_erwin_1990]
- [Esposito and Orlando 2024][research_esposito_orlando_2024]
- [Estupinan and Prazenica 2026][research_estupinan_prazenica_2026]
- [Evangelisti and Pfifer 2024][research_evangelisti_pfifer_2024]
- [Eymar and Deneu 2002][research_eymar_deneu_2002]
- [Fahaz Firoz et al 2023][research_fahazfiroz_rupikaraj_2023]
- [Fahrenthold and Park 2005][research_fahrenthold_park_2005]
- [Fahy et al 2021][research_fahy_buttsworth_2021]
- [Fain et al 2026][research_fain_lambert_2026]
- [Faisal and James 2025][research_faisal_james_2025]
- [Fallon et al 1999][research_fallonii_taylor_1999]
- [Fan 2015][research_fan_2015]
- [Fan and Wang 2007][research_fan_wang_2007]
- [Fan et al 2022][research_fan_tian_2022]
- [Fan et al 2025][research_fan_nie_2025]
- [Fang 2018][research_fang_2018]
- [Fang et al 2017][research_fang_ying_2017]
- [Fang et al 2018][research_fang_2018_b]
- [Fang et al 2019][research_fang_2019]
- [Fang et al 2026][research_fang_chen_2026]
- [Farajollahi and Markazi 2010][research_farajollahi_markazi_2010]
- [Fariz et al 2013][research_fariz_ushaq_2013]
- [Fasanella et al 1984][research_fasanella_1984]
- [Fasanella et al 2004][research_fasanella_2004]
- [Fasanella et al 2012][research_fasanella_2012]
- [Fathurrahman and Jenie 2022][research_fathurrahman_jenie_2022]
- [Faulders et al 1967][research_faulders_lekawa_1967]
- [Faúndez 2018][research_faundez_2018]
- [Fearnside 1959][research_fearnside_1959]
- [Feather and Craven 1991][research_feather_1991]
- [Federici et al 2026][research_federici_benedikter_2026]
- [Fedotov and Perepelkina 2019][research_fedotov_perepelkina_2019]
- [Fegely et al 2016][research_fegely_tischler_2016]
- [Fehrs and Helm 2025][research_fehrs_helm_2025]
- [Feinreich and Gevaert 1980][research_feinreich_1980]
- [Feld 1968][research_feld_1968]
- [Feld et al][research_feld_nd]
- [Feldman 1967][research_feldman_1967]
- [Feldman et al 2019][research_feldman_2019]
- [Feng and Wasynczuk 1967][research_feng_wasynczuk_1967]
- [Feng et al 2009][research_feng_cui_2009]
- [Feng et al 2019][research_feng_guo_2019]
- [Feng et al 2022][research_feng_wang_2022]
- [Feng et al 2025][research_feng_bai_2025]
- [Feng et al 2026][research_feng_lang_2026]
- [Fenghua et al 2021][research_fenghua_meng_2021]
- [Fenwick 1966][research_fenwick_1966_c]
- [Fenwick 1967][research_fenwick_1967]
- [Ferguson et al 2005][research_ferguson_zhang_2005]
- [Ferrandon 1997][research_ferrandon_1997]
- [Ferreres and Puyou 2006][research_ferreres_puyou_2006]
- [Ferris and Kelly 1968][research_ferris_1968]
- [Feustel-Büechl 1988][research_feustelbuechl_1988]
- [Fiddes et al 1985][research_fiddes_kirby_1985]
- [Field and Rossitto 1999][research_field_rossitto_1999]
- [Filatyev 2000][research_filatyev_2000]
- [Filatyev et al 2014][research_filatyev_buzuluk_2014]
- [Filyashkin and Yatskivsky 2013][research_filyashkin_yatskivsky_2013]
- [Finke 1990][research_finke_1990]
- [Finson et al 1980][research_finson_clarke_1980]
- [First Glide Flight of 1966][research_first_glide_1966]
- [Fischenberg 1995][research_fischenberg_1995]
- [Fisher 1960][research_fisher_1960]
- [Fisher and Cederborg 1948][research_fisher_1948]
- [Fisher and Windham 1955][research_fisher_1955]
- [Fisher et al 2018][research_fisher_quinn_2018]
- [Fitzgerald and Gingras 1996][research_fitzgerald_1996]
- [Fitzsimmons 1996][research_fitzsimmons_1996]
- [Flight Test Results Pertaining 1970][research_flight_test_1970_b]
- [Florence 1979][research_florence_1979]
- [Flotten 2005][research_flotten_2005]
- [Foch and Toot 1989][research_foch_toot_1989]
- [Fong et al 1970][research_fong_ehrlich_1970]
- [Forssell and Hyden 2003][research_forssell_hyden_2003]
- [Fortenbaugh 1972][research_fortenbaugh_1972]
- [Foster 1972][research_foster_1972]
- [Foster et al 2020][research_foster_2020]
- [Foster et al 2020][research_foster_miller_2020]
- [Fowler 1990][research_fowler_1990]
- [Fralish 1998][research_fralish_1998]
- [Frank et al 2014][research_frank_durand_2014]
- [Frankenthal 1964][research_frankenthal_1964]
- [Franklin and Innis 1972][research_franklin_1972]
- [Franklin and Innis 1977][research_franklin_innis_1977]
- [Franklin and Innis 1978][research_franklin_innis_1978]
- [Franklin et al 1985][research_franklin_hynes_1985]
- [Franze and Barz 2025][research_franze_barz_2025]
- [Franze and Basov 2026][research_franze_basov_2026]
- [Frapard 2003][research_frapard_2003]
- [Fratello et al 1987][research_fratello_1987]
- [Fravolini et al 2004][research_fravolini_campa_2004]
- [Fravolini et al 2015][research_fravolini_yucelen_2015]
- [Frayssinet 2019][research_frayssinet_2019]
- [Freeman et al 1996][research_freeman_talay_1996]
- [Freeman et al 1997][research_freeman_talay_1997]
- [Fremaux 1995][research_fremaux_1995]
- [Fremaux and Johnson 2006][research_fremaux_2006]
- [French 2001][research_french_2001]
- [Frenkel and Shaferman 2026][research_frenkel_shaferman_2026]
- [Fresconi 2011][research_fresconi_2011]
- [Fresconi et al 2014][research_fresconi_celmins_2014]
- [Friia et al 2023][research_friia_mahajan_2023]
- [Frinell 1983][research_frinell_1983]
- [Frisby 1960][research_frisby_1960]
- [Friz and Samareh 2020][research_friz_samareh_2020]
- [Frohme 1975][research_frohme_1975]
- [Froning 2006][research_froning_2006]
- [Froning et al 1996][research_froningjr_mckinney_1996]
- [Fu et al 2022][research_fu_shi_2022]
- [Fu et al 2023][research_fu_hang_2023]
- [Fu et al 2025][research_fu_dang_2025]
- [Fuchs and Jackson 2011][research_fuchs_jackson_2011]
- [Fuchs et al 2018][research_fuchs_haskell_2018]
- [Fuhrmann 2003][research_fuhrmann_2003]
- [Fuhry 1999][research_fuhry_1999]
- [Fujimori et al 2000][research_fujimori_kurozumi_2000]
- [Fullerton 1975][research_fullerton_1975]
- [Furfaro et al 2013][research_furfaro_cersosimo_2013]
- [Furnish and Anders 1971][research_furnish_anders_1971]
- [Fusaro et al 2016][research_fusaro_viola_2016]
- [Förder and Steiner 2020][research_forder_steiner_2020]
- [Gabarrou et al 2010][research_gabarrou_alazard_2010]
- [Gage and Vander Kam 2003][research_gage_vanderkam_2003]
- [Gai 1996][research_gai_1996]
- [Gainer and Hoffman 1972][research_gainer_1972]
- [Galanis et al 1998][research_galanis_jennings_1998]
- [Galassi 2011][research_galassi_2011]
- [Gallaher et al 1996][research_gallaher_coughlin_1996]
- [Gallington and Miller 1970][research_gallington_miller_1970]
- [Galloway et al 1998][research_galloway_slivinsky_1998]
- [Gamble et al 1984][research_gamble_spratlin_1984]
- [Gamse and Mort 1966][research_gamse_1966]
- [Gan et al 2021][research_gan_fang_2021]
- [Gan et al 2021][research_gan_fang_2021_b]
- [Gandhewar and Sonkusare 2014][research_gandhewar_gsonkusare_2014]
- [Gang et al 2010][research_gang_wang_2010]
- [Gannett 1964][research_gannett_1964]
- [Gao and Cai 2017][research_gao_cai_2017]
- [Gao and Yao 2018][research_gao_yao_2018]
- [Gao et al 2010][research_gao_cui_2010]
- [Gao et al 2012][research_gao_jiang_2012]
- [Gao et al 2014][research_gao_jiang_2014]
- [Gao et al 2014][research_gao_li_2014]
- [Gao et al 2015][research_gao_li_2015]
- [Gao et al 2017][research_gao_tang_2017]
- [Gao et al 2018][research_gao_cai_2018]
- [Gao et al 2019][research_gao_cai_2019]
- [Gao et al 2021][research_gao_an_2021]
- [Gao et al 2021][research_gao_an_2021_b]
- [Gao et al 2021][research_gao_shao_2021]
- [Gao et al 2023][research_gao_sun_2023]
- [Gao et al 2023][research_gao_wei_2023]
- [Gao et al 2025][research_gao_wang_2025]
- [Gaohua et al 2014][research_gaohua_jianmei_2014]
- [Garcia 2008][research_garcia_2008]
- [Garcia and Fowler 1974][research_garcia_fowler_1974]
- [Garcia-Pardo et al 2001][research_garciapardo_sukhatme_2001]
- [Garcia-Quinchia et al 2009][research_garciaquinchia_yiguo_2009]
- [Gardinier and Taylor 1999][research_gardinier_taylor_1999]
- [Garg and Dodiyal 2009][research_garg_dodiyal_2009]
- [Garland and Chauvin 1957][research_garland_1957]
- [Gaskell 2005][research_gaskell_2005]
- [Gaverina et al 2026][research_gaverina_eiras_2026]
- [Gavrilovski et al 2011][research_gavrilovski_ward_2011]
- [Gaétan 2009][research_gaetan_2009]
- [Gee 1978][research_gee_1978]
- [Gee et al 2014][research_gee_2014]
- [Geetha et al 2015][research_geethas_priyagnair_2015]
- [Geister et al 2017][research_geister_2017]
- [Geng et al 2013][research_geng_sheng_2013]
- [Geng et al 2014][research_geng_sheng_2014]
- [Genin 1969][research_genin_1969]
- [Gentry 1968][research_gentry_1968]
- [Gentry et al 1966][research_gentry_1966]
- [Gentry et al 1975][research_gentry_dappolito_1975]
- [George and Sukkarieh 2007][research_george_sukkarieh_2007]
- [Georghiou et al 1986][research_georghiou_metcalfe_1986]
- [Gerratt et al 2020][research_gerratt_strate_2020]
- [Gerth and Mooij 2014][research_gerth_mooij_2014]
- [Gettatelli et al 2023][research_gettatelli_benedikter_2023]
- [Geuther et al 2024][research_geuther_ackerman_2024]
- [Ghanchi and Gururajan 2026][research_ghanchi_gururajan_2026]
- [Ghasemi et al 2012][research_ghasemi_moradi_2012]
- [Ghate et al 2026][research_ghate_angel_2026]
- [Ghods et al 2024][research_ghods_khalesi_2024]
- [Gibney 2015][research_gibney_2015]
- [Gibson 2002][research_gibson_2002]
- [Gibson and Marrone 1964][research_gibson_marrone_1964]
- [Gibson and Wilenius 1964][research_gibson_wilenius_1964]
- [Gielda et al 1990][research_gielda_deese_1990]
- [Gilbert and Goldberg 1967][research_gilbert_goldberg_1967]
- [Gillis and Mitchell 1957][research_gillis_1957]
- [Gilson and Fenton 1973][research_gilson_1973]
- [Girgis et al 2002][research_girgis_brown_2002]
- [Glaab et al 2014][research_glaab_2014]
- [Glass and Glass 2002][research_glass_glass_2002]
- [Glavine et al 2018][research_glavine_desilva_2018]
- [Gleichman et al 1991][research_gleichman_1991]
- [Gnoffo et al 1994][research_gnoffo_weilmuenster_1994]
- [Gockel 1993][research_gockel_1993]
- [Godines et al 2024][research_godines_abdi_2024]
- [Godwin et al 1964][research_godwin_frazier_1964]
- [Gogu et al 2007][research_gogu_bapanapalli_2007]
- [Gogu et al 2009][research_gogu_bapanapalli_2009]
- [Gold and Walchli 1974][research_gold_1974]
- [Goldberg 1966][research_goldberg_1966]
- [Goldman et al 2015][research_goldman_dowell_2015]
- [Goldschmidt et al 2024][research_goldschmidt_tingle_2024]
- [Goldstein et al 1978][research_goldstein_leiser_1978]
- [Goldyn et al 2025][research_goldyn_marwege_2025]
- [Golomazov and Ivankov 2018][research_golomazov_ivankov_2018]
- [Gong et al 1984][research_gong_ko_1984]
- [Gong et al 2015][research_gong_bing_2015]
- [Gong et al 2015][research_gong_zhang_2015]
- [Gong et al 2020][research_gong_guo_2020]
- [Gong et al 2022][research_gong_wang_2022]
- [Gong et al 2025][research_gong_chen_2025]
- [Gonzales et al 2021][research_gonzales_kurihara_2021]
- [Goodall 1977][research_goodall_1977]
- [Goodyear Aerospace Corp Akron Oh 1961][research_goodyearaerospacecorpakronoh_1961]
- [Goodyer and Kilgore 1972][research_goodyer_kilgore_1972]
- [Gopal et al 2026][research_gopal_somaroutu_2026]
- [Gorskiy and Subkhangulov 2025][research_gorskiy_subkhangulov_2025]
- [Goto et al 2001][research_goto_miyazawa_2001]
- [Goto et al 2004][research_goto_kawakita_2004]
- [Gouskov 1972][research_gouskov_1972]
- [Goyal et al 2021][research_goyal_babuska_2021]
- [Goz and Theodoulis 2025][research_goz_theodoulis_2025]
- [Grabowsky et al 1981][research_grabowsky_eldridge_1981]
- [Grace 1964][research_grace_1964]
- [Gracey 1967][research_gracey_1967]
- [Grafton and Anglin 1975][research_grafton_1975]
- [Grafton et al 1974][research_grafton_1974]
- [Grana and Shanks 1952][research_grana_1952]
- [Grantham 2003][research_grantham_2003]
- [Grantham and Williams 1987][research_grantham_williams_1987]
- [Grantz 2011][research_grantz_2011]
- [Graovac 2007][research_graovac_2007]
- [Grauer et al 2017][research_grauer_morelli_2017]
- [Graves and Masciarelli 2002][research_graves_masciarelli_2002]
- [Gray 2016][research_gray_2016]
- [Green 2015][research_green_2015]
- [Green and Fernandez 1994][research_green_fernandez_1994]
- [Greenhalgh et al 2026][research_greenhalgh_2026]
- [Gregory et al 2011][research_gregory_xargay_2011]
- [Greiser et al 2011][research_greiser_lantzsch_2011]
- [Grenestedt and Spletzer 2010][research_grenestedt_spletzer_2010]
- [Grenoble et al 2018][research_grenoble_nguyen_2018]
- [Grewal et al 1976][research_grewal_schneider_1976]
- [Griffin and Takahashi 2022][research_griffin_takahashi_2022]
- [Griffiths and Miller 1986][research_griffiths_miller_1986]
- [Grigoli 2024][research_grigoli_2024]
- [Grodsky and Mandour 1967][research_grodsky_mandour_1967]
- [Groener et al 1980][research_groener_stetson_1980]
- [Groomes 1964][research_groomes_1964]
- [Gross and Fasel][research_gross_nd]
- [Grossi et al 2026][research_grossi_fabiani_2026]
- [Grosveld et al 2004][research_grosveld_2004]
- [Grumondz et al 2012][research_grumondz_polishchuk_2012]
- [Gryte et al 2017][research_gryte_hansen_2017]
- [Gu et al 2012][research_gu_gross_2012]
- [Gu et al 2022][research_gu_xing_2022]
- [Guadagnini et al 2023][research_guadagnini_dezaiacomo_2023]
- [Guerrero et al 2022][research_guerrero_pelluault_2022]
- [Guida 2023][research_guida_2023]
- [Gulli and Maddalena 2014][research_gulli_maddalena_2014]
- [Gulli and Maddalena 2015][research_gulli_maddalena_2015_b]
- [Gulli et al 2014][research_gulli_maddalena_2014_b]
- [Gulli et al 2014][research_gulli_maddalena_2014_c]
- [Gulli et al 2015][research_gulli_maddalena_2015]
- [Gunckel 1966][research_gunckel_1966]
- [Gunderson and Hardy 1965][research_gunderson_hardy_1965]
- [Guo and Fang 2022][research_guo_fang_2022]
- [Guo et al 2016][research_guo_yue_2016]
- [Guo et al 2017][research_guo_qi_2017]
- [Guo et al 2017][research_guo_wang_2017]
- [Guo et al 2017][research_guo_zhu_2017]
- [Guo et al 2018][research_guo_chang_2018]
- [Guo et al 2025][research_guo_du_2025]
- [Guo et al 2025][research_guo_luo_2025]
- [Guo et al 2025][research_guo_wang_2025_b]
- [Guo et al 2025][research_guo_yang_2025]
- [Guo et al 2026][research_guo_huang_2026]
- [Guo Jianguo et al 2016][research_guojianguo_fengzhenxin_2016]
- [Guorong Zhao et al 2006][research_guorongzhao_jixinli_2006]
- [Gupta 2023][research_gupta_2023]
- [Gupta and Ramkumar 2015][research_gupta_ramkumar_2015]
- [Gupta et al 2018][research_gupta_anilkumar_2018]
- [Gupta et al 2025][research_gupta_sai_2025]
- [Gutt et al 2004][research_gutt_fischer_2004]
- [Guy 1976][research_guy_1976]
- [Gómez and Walker 2017][research_gomez_walker_2017]
- [Gök and Ci̇han 2022][research_gok_cihan_2022]
- [Haak 1994][research_haak_1994]
- [Habas et al 2022][research_habas_alattar_2022]
- [Haberbusch and Walls 2008][research_haberbusch_walls_2008]
- [Hadaegh et al 1996][research_hadaegh_mettler_1996]
- [Haggerty 1986][research_haggerty_1986]
- [Hahne and Fremaux 2008][research_hahne_2008]
- [Hahne et al 1993][research_hahne_1993]
- [Hailiang and Lixin 2015][research_hailiang_lixin_2015]
- [Haiqing et al 2025][research_haiqing_junfeng_2025]
- [Haise 1977][research_haise_1977]
- [Halaas and Bieniawski 2010][research_halaas_bieniawski_2010]
- [Halbe et al 2014][research_halbe_raja_2014]
- [Halbe et al 2018][research_halbe_spiess_2018]
- [Hall][research_hall_nd]
- [Hall and Shtessel 2005][research_hall_shtessel_2005]
- [Hall and Soares 2008][research_hall_soares_2008]
- [Hall et al 1963][research_hall_dietrich_1963]
- [Hall et al 1999][research_hall_1999]
- [Hallberg et al 2008][research_hallberg_cenko_2008]
- [Hallion et al 1995][research_hallion_becker_1995]
- [Halyo 1987][research_halyo_1987]
- [Ham and Johnson 1969][research_ham_1969]
- [Hameed and Bindu 2019][research_hameed_bindu_2019]
- [Hamel et al 2025][research_hamel_garant_2025]
- [Hamilton et al 1980][research_hamilton_1980]
- [Hammel 2004][research_hammel_2004]
- [Hammock and Jackson 1963][research_hammock_1963]
- [Hammond et al 1967][research_hammond_adler_1967]
- [Hammouche et al 2016][research_hammouche_sakhi_2016]
- [Han 2024][research_han_2024]
- [Han 2025][research_han_2025]
- [Han and Han 2024][research_han_han_2024]
- [Han and Shuping 2015][research_han_shuping_2015]
- [Han and Wang 2011][research_han_wang_2011]
- [Han and Xiong 2016][research_han_xiong_2016]
- [Han et al 2022][research_han_jiao_2022]
- [Han et al 2025][research_han_wang_2025]
- [Haney and Rothschild 2003][research_haney_rothschild_2003]
- [Hang et al 2025][research_hang_rui_2025]
- [Hankey 1963][research_hankey_1963]
- [Hanlon et al 2006][research_hanlon_deshmukh_2006]
- [Hann-Shing Ju and Ching-Chih Tsai 2007][research_hannshingju_chingchihtsai_2007]
- [Hannemann et al 2015][research_hannemann_martinezschramm_2015]
- [Hannemann et al 2017][research_hannemann_martinezschramm_2017]
- [Hannigan et al 1993][research_hannigan_sved_1993]
- [Hannum and Berkopec 1989][research_hannum_berkopec_1989]
- [Hao and Huang 2009][research_hao_huang_2009]
- [Hao et al 2009][research_hao_lei_2009]
- [Hao et al 2017][research_hao_peng_2017]
- [Harasani 2015][research_iharasani_2015]
- [Harcus and Bright 2020][research_harcus_bright_2020]
- [Hardin 1986][research_hardin_1986]
- [Hardy 1972][research_hardy_1972]
- [Hardy 1983][research_hardy_1983]
- [Hardy et al 1993][research_hardy_eldrenkamp_1993]
- [Harigae and Tanabe 1990][research_harigae_tanabe_1990]
- [Harigae et al 2003][research_harigae_tomita_2003]
- [Harl 2008][research_harl_2008]
- [Harpold 1980][research_harpold_1980]
- [Harris 2018][research_harris_2018]
- [Harrison 1965][research_harrison_1965]
- [Harrison 1967][research_harrison_1967]
- [Harrison and Lockman 1968][research_harrison_lockman_1968]
- [Harrison and Marko 1968][research_harrison_marko_1968]
- [Harrison et al 1964][research_harrison_1964]
- [Hart 1992][research_hart_1992]
- [Hart and Devolites 2014][research_hart_2014]
- [Hartl 1989][research_hartl_1989]
- [Hasegawa 2025][research_hasegawa_2025]
- [Hasegawa and Kanda 2019][research_hasegawa_kanda_2019]
- [Hasegawa et al 2021][research_hasegawa_fukui_2021]
- [Hatano 1959][research_hatano_1959]
- [Hatchell et al 2011][research_hatchell_mauss_2011]
- [Havey and Ferguson 1990][research_havey_ferguson_1990]
- [Hawthorne 1976][research_hawthorne_1976]
- [Hawthorne 1976][research_hawthorne_1976_b]
- [Hawthorne 1976][research_hawthorne_1976_c]
- [Hawthorne 1976][research_hawthorne_1976_d]
- [Hawthorne 1976][research_hawthorne_1976_e]
- [Hawthorne 1976][research_hawthorne_1976_f]
- [Hawthorne 1976][research_hawthorne_1976_g]
- [Hawthorne 1976][research_hawthorne_1976_h]
- [Hawthorne 1976][research_hawthorne_1976_i]
- [Hawthorne 1976][research_hawthorne_1976_j]
- [Hawthorne 1976][research_hawthorne_1976_k]
- [Hawthorne 1976][research_hawthorne_1976_l]
- [Hawthorne 1976][research_hawthorne_1976_m]
- [Hayashi et al 2006][research_hayashi_aso_2006]
- [Hayashi et al 2025][research_hayashi_yamasaki_2025]
- [Hayes 1972][research_hayes_1972]
- [Hays et al 2022][research_hays_dsouza_2022]
- [He et al 2012][research_he_lee_2012]
- [He et al 2023][research_he_zhang_2023]
- [He et al 2025][research_he_zhang_2025]
- [He et al 2025][research_he_zhao_2025]
- [Hebbar and Pashilkar 2017][research_hebbar_pashilkar_2017]
- [Hecker et al 2019][research_hecker_bestmann_2019]
- [Hedlund and Ragsdale 1985][research_hedlund_ragsdale_1985]
- [Hedlund et al 1990][research_hedlund_higgins_1990]
- [Helers and Kraemer 1977][research_helers_kraemer_1977]
- [Hellings 1973][research_hellings_1973]
- [Hellman and Tejtel 2008][research_hellman_tejtel_2008]
- [Hellman et al 2010][research_hellman_ngo_2010]
- [Hellman et al 2011][research_hellman_remillard_2011]
- [Hellman et al 2011][research_hellman_wallace_2011]
- [Hemann et al 2016][research_hemann_singh_2016]
- [Hemsch 1988][research_hemsch_1988]
- [Henderson 1963][research_henderson_1963]
- [Hendrick and Horn 2024][research_hendrick_horn_2024]
- [Heng and Sherman 1996][research_heng_sherman_1996]
- [Heo et al 2004][research_heo_pervan_2004]
- [Hepler et al 1973][research_hepler_1973]
- [Herbst et al 2000][research_herbst_forrest_2000]
- [Hergert et al 2017][research_hergert_2017]
- [Herholz and Valentiny 1988][research_herholz_valentiny_1988]
- [Herissé et al 2012][research_herisse_hamel_2012]
- [Hertzfeld 2000][research_hertzfeld_2000]
- [Herz et al 2024][research_herz_mccrink_2024]
- [Herzog et al 1998][research_herzog_yue_1998]
- [Hess 1972][research_hess_1972]
- [Hetmaniok et al 2024][research_hetmaniok_brociek_2024]
- [Hewes 1961][research_hewes_1961]
- [Heydari and Balakrishnan 2011][research_heydari_balakrishnan_2011]
- [Hicks and Matheny 1987][research_hicks_matheny_1987]
- [Hicks and Paller 2025][research_hicks_paller_2025]
- [Hiliuta and Botez 2006][research_hiliuta_botez_2006]
- [Hill and Huhlein 1993][research_hill_huhlein_1993]
- [Hillaker 1983][research_hillaker_1983]
- [Hillaker 1983][research_hillaker_1983_b]
- [Hiltz et al 1968][research_hiltz_florence_1968]
- [Hinchey 1968][research_hinchey_1968]
- [Hinson 1959][research_hinson_1959]
- [Hinson and Lee 1959][research_hinson_1959_b]
- [Hinton and Eastlake][research_hinton_nd]
- [Hirschel and Weiland 2009][research_hirschel_weiland_2009]
- [Ho and Romero 2013][research_ho_romero_2013]
- [Hoag 1983][research_hoag_1983]
- [Hoag and Schofield 1970][research_hoag_1970]
- [Hoang et al 2017][research_hoang_bayasgalan_2017]
- [Hodge et al 1981][research_hodge_phillips_1981]
- [Hodges and Walker 1994][research_hodges_1994]
- [Hodgkinson and Johnston 1979][research_hodgkinson_johnston_1979]
- [Hoess et al 1963][research_hoess_voorhees_1963]
- [Hoffelner et al 2023][research_hoffelner_maly_2023]
- [Hoffman et al 1961][research_hoffman_1961]
- [Hofmann et al 1978][research_hofmann_1978]
- [Hofmann-Wellenhof et al 2003][research_hofmannwellenhof_legat_2003]
- [Hofsäß et al 2023][research_hofsass_braun_2023]
- [Holberg and Grabowsky 1981][research_holberg_grabowsky_1981]
- [Holdo 1993][research_holdo_1993]
- [Holleman 1976][research_holleman_1976]
- [Holley and Bryson 1975][research_holley_brysonjr_1975]
- [Hollinger 1958][research_hollinger_1958]
- [Hollis 2017][research_hollis_2017]
- [Hollis and Hollingsworth 2012][research_hollis_hollingsworth_2012]
- [Holloway 1967][research_holloway_1967]
- [Holmes 1970][research_holmes_1970]
- [Holmes and Langelaan 2016][research_holmes_langelaan_2016]
- [Holmes and Woehr 1971][research_holmes_woehr_1971]
- [Holt et al 2016][research_holt_garry_2016]
- [Holway 1966][research_holway_1966]
- [Homan et al 1980][research_homan_1980]
- [Honda et al 2019][research_honda_tajima_2019]
- [Hong et al 2005][research_hong_lee_2005]
- [Hong et al 2016][research_hong_dilshod_2016]
- [Hong et al 2016][research_hong_dilshod_2016_b]
- [Hong et al 2018][research_hong_ryoo_2018]
- [Hood 1968][research_hood_1968]
- [Hook and Freeman 1989][research_hook_1989]
- [Hoole et al 2020][research_hoole_sartor_2020]
- [Hoole et al 2021][research_hoole_sartor_2021]
- [Hopping et al 1986][research_hopping_counts_1986]
- [Horn et al 2014][research_horn_tritschler_2014]
- [Hornbuckle 2015][research_hornbuckle_2015]
- [Horneman and Kluever 2004][research_horneman_kluever_2004]
- [Horri et al 2024][research_horri_holderbaum_2024]
- [Horstman and Kussoy 1967][research_horstman_1967]
- [Horton et al 1964][research_horton_1964]
- [Horvath et al 2002][research_horvath_2002]
- [Hou et al 2015][research_hou_wang_2015]
- [Hou et al 2020][research_hou_zhang_2020]
- [Housner et al 1982][research_housner_edighoffer_1982]
- [Howard 1976][research_howard_1976]
- [Howard and Batill 1990][research_howardjr_batill_1990]
- [Howell and Braslow 1955][research_howell_1955]
- [Howland 1953][research_howland_1953]
- [Hoxey et al 1997][research_hoxey_robertson_1997]
- [Hoy 1963][research_hoy_1963]
- [Hoyt 2006][research_hoyt_2006]
- [Hruby and McDevitt 1964][research_hruby_1964]
- [Hryshchenko et al 2018][research_hryshchenko_romanenko_2018]
- [Hsiao et al 1997][research_hsiao_ho_1997]
- [Hu and Durbin 2012][research_hu_durbin_2012]
- [Hu and Liu 2025][research_hu_liu_2025]
- [Hu et al 2013][research_hu_2013]
- [Hu et al 2016][research_hu_wang_2016]
- [Hu et al 2018][research_hu_li_2018]
- [Hu et al 2021][research_hu_chen_2021]
- [Hu et al 2021][research_hu_huang_2021]
- [Hu et al 2022][research_hu_guo_2022]
- [Hu et al 2022][research_hu_ji_2022]
- [Hu et al 2024][research_hu_jing_2024]
- [Hu et al 2024][research_hu_xiao_2024]
- [Hu Wei-jun and Zhou Jun 2009][research_huweijun_zhoujun_2009]
- [hua and yan 2018][research_hua_yan_2018]
- [Huan et al 2015][research_huan_guoliang_2015]
- [Huang 1968][research_huang_1968]
- [Huang 2016][research_huang_2016]
- [Huang 2019][research_huang_2019]
- [Huang and Dai 2023][research_huang_dai_2023]
- [Huang and Fan 2022][research_huang_fan_2022]
- [Huang and Jia 2018][research_huang_jia_2018]
- [Huang and Wang 2007][research_huang_wang_2007]
- [Huang and Wang 2015][research_huang_wang_2015]
- [Huang and Yao 2018][research_huang_yao_2018]
- [Huang and Yao 2019][research_huang_yao_2019_b]
- [Huang et al 2009][research_huang_liu_2009]
- [Huang et al 2014][research_huang_zhang_2014]
- [Huang et al 2015][research_huang_zhang_2015]
- [Huang et al 2016][research_huang_nie_2016]
- [Huang et al 2019][research_huang_liu_2019]
- [Huang et al 2019][research_huang_yao_2019]
- [Huang et al 2022][research_huang_yang_2022]
- [Huang et al 2023][research_huang_deng_2023]
- [Huang et al 2024][research_huang_dai_2024]
- [Huang et al 2024][research_huang_gong_2024]
- [Huang et al 2024][research_huang_yu_2024]
- [Huang et al 2025][research_huang_li_2025]
- [Huang et al 2026][research_huang_luo_2026]
- [Huayanay Villar et al 2024][research_huayanayvillar_aldana_2024]
- [Hudson 2005][research_hudson_2005]
- [Hudson and Stephens 2006][research_hudson_2006]
- [Hudson and Stephens 2009][research_hudson_2009]
- [Huebner et al 2001][research_huebner_rock_2001]
- [Huebner et al 2001][research_huebner_rock_2001_b]
- [Huebner et al 2009][research_huebner_smith_2009]
- [Hueschen 1984][research_hueschen_1984]
- [Hueschen 1985][research_hueschen_1985]
- [Hughes and Chrispin 1988][research_hughes_chrispin_1988]
- [Hugo and Engelbrecht 2016][research_hugo_2016]
- [Hugo and Lago 2022][research_hugo_lago_2022]
- [Hui and Yang 2013][research_hui_yang_2013]
- [Huili et al 2023][research_huili_xiying_2023]
- [Hull et al 1981][research_hull_french_1981]
- [Humes 1978][research_humes_1978]
- [Hummer et al 2018][research_hummer_jurkovich_2018]
- [Humphrey and Humphrey 1997][research_humphrey_humphrey_1997]
- [Humphreys et al 1988][research_humphreys_1988]
- [Hundley et al 1993][research_hundley_rowson_1993]
- [Hung et al 2024][research_hung_unger_2024]
- [Hunt 1989][research_hunt_1989]
- [Hunt and Eiswirth 1996][research_hunt_eiswirth_1996]
- [Hunter 1973][research_hunter_1973]
- [Hunter and Wilson 1976][research_hunter_wilson_1976]
- [Hutter and Jöhnk 2004][research_hutter_johnk_2004]
- [Hutter and Wang 2016][research_hutter_wang_2016]
- [Huynh and Kriz 2009][research_huynh_kriz_2009]
- [Hwang et al 2005][research_hwang_oh_2005]
- [Hyde 2005][research_hyde_2005]
- [Hyde and Massie 1993][research_hyde_1993]
- [Hynes et al 1987][research_hynes_hardy_1987]
- [Hyokawa and Ueba 2023][research_hyokawa_ueba_2023]
- [Hyslop et al 2021][research_hyslop_doherty_2021]
- [Hyslop et al 2022][research_hyslop_mcgilvray_2022]
- [Hyun 2005][research_hyun_2005]
- [Ide and Landman 2025][research_ide_landman_2025]
- [Iden 1959][research_iden_1959]
- [Iizuka 2024][research_iizuka_2024]
- [Iliev and Nachev 2022][research_iliev_nachev_2022]
- [Inatani et al 1992][research_inatani_akiba_1992]
- [Indig et al 2017][research_indig_benasher_2017]
- [Inger 2003][research_inger_2003]
- [Inger 2003][research_inger_2003_b]
- [Ingle and Celi 1994][research_ingle_celi_1994]
- [Inokuchi 1996][research_inokuchi_1996]
- [Ishida et al 2014][research_ishida_nagai_2014]
- [Ishida et al 2015][research_ishida_nagai_2015]
- [Ishikawa and Ogasawara 2001][research_ishikawa_ogasawara_2001]
- [Ishimoto 1995][research_ishimoto_1995]
- [Ishimoto et al 1996][research_ishimoto_takizawa_1996]
- [Ishimoto et al 2005][research_ishimoto_fujii_2005]
- [Ishioka et al 2019][research_ishioka_uchiyama_2019]
- [Ismail et al 2015][research_ismail_pashilkar_2015]
- [Ito and Nomoto 1990][research_ito_nomoto_1990]
- [Ito et al 1990][research_ito_akimoto_1990]
- [Ivanco et al 2024][research_ivanco_keller_2024]
- [Ivanov et al 1993][research_ivanov_bitzer_1993]
- [Ivanov et al 2007][research_ivanov_vashchenkov_2007]
- [Ivanov et al 2011][research_ivanov_vashchenkov_2011]
- [Ivanov et al 2013][research_ivanov_huertas_2013]
- [Ivins 1978][research_ivins_1978]
- [Iwabuchi and Minesugi 2026][research_iwabuchi_minesugi_2026]
- [Iwakawa et al 2015][research_iwakawa_furukawa_2015]
- [Izraelevitz et al 2022][research_izraelevitz_pauken_2022]
- [Izzo et al 2011][research_izzo_weiss_2011]
- [Jacklin 2008][research_jacklin_2008]
- [Jackson 1961][research_jackson_1961]
- [Jackson and Buttrill 2006][research_jackson_2006]
- [Jackson and Coyle 1983][research_jackson_coyle_1983]
- [Jackson and Cruz 1992][research_jackson_1992]
- [Jackson and Fasanella 2004][research_jackson_2004]
- [Jackson and Fasanella 2004][research_jackson_2004_b]
- [Jackson and Fasanella 2004][research_jackson_2004_c]
- [Jackson and Fasanella 2016][research_jackson_2016]
- [Jackson and Rivers 1998][research_jackson_rivers_1998]
- [Jackson et al 1991][research_jackson_1991]
- [Jackson et al 1992][research_jackson_1992_b]
- [Jackson et al 1993][research_jackson_1993]
- [Jackson et al 1993][research_jackson_rivers_1993_b]
- [Jackson et al 1994][research_jackson_1994]
- [Jackson et al 2003][research_jackson_2003]
- [Jackson et al 2018][research_jackson_2018]
- [Jackson et al 2018][research_jackson_2018_b]
- [Jacob 1991][research_jacob_1991]
- [Jacob da Motta 2020][research_ajacobdamotta_2020]
- [Jacobson 2004][research_jacobson_2004]
- [Jacobson 2004][research_jacobson_2004_b]
- [Jacobson 2005][research_jacobson_2005]
- [Jaensch and Markl 1991][research_jaensch_markl_1991]
- [Jaffe 1972][research_jaffe_1972]
- [Jaffe 1975][research_jaffe_1975]
- [Jalaja et al 2023][research_jalaja_manwatkar_2023]
- [Jamal-Eddine 2025][research_jamaleddine_2025]
- [James 1959][research_james_1959]
- [Jameson 2001][research_jameson_2001]
- [Jamieson and White 2019][research_jamieson_white_2019]
- [Jamieson and White 2021][research_jamieson_white_2021]
- [Janicik 1999][research_janicik_1999]
- [Jann and Greiner-Perth 2009][research_jann_greinerperth_2009]
- [Janna 2020][research_janna_2020]
- [Janssens and Kimberlin 2000][research_janssens_2000]
- [Jarosław et al 2026][research_jaroslaw_robert_2026]
- [Jarvis 1989][research_jarvis_1989]
- [Jasra et al 2020][research_jasra_valentino_2020]
- [Jategaonkar et al 2006][research_jategaonkar_behr_2006]
- [Jathaveda et al 2023][research_jathaveda_manokaran_2023]
- [Javeed et al 1993][research_javeed_1993]
- [Jayanthi and Jain 2019][research_jayanthi_jain_2019]
- [Jayaraman et al 2022][research_jayaraman_gaurav_2022]
- [Jayaraman et al 2022][research_jayaraman_saini_2022]
- [Jean Ross and Edwards 1987][research_jeanross_edwards_1987]
- [Jebáček and Horák 2016][research_jebacek_horak_2016]
- [Jee et al 2014][research_jee_brinda_2014]
- [Jee et al 2014][research_jee_yalagach_2014]
- [Jekeli 2015][research_jekeli_2015]
- [Jenkins and Donovan 1942][research_jenkins_donovan_1942]
- [Jenkins and Donovan 1942][research_jenkins_donovan_1942_b]
- [Jenkins et al 1968][research_jenkins_1968]
- [Jensen et al 2020][research_jensen_coy_2020]
- [Jeong et al 2013][research_jeong_ryu_2013]
- [Jetawatthana and Khamvilai 2026][research_jetawatthana_khamvilai_2026]
- [Ji and Zhou 2018][research_ji_zhou_2018]
- [Ji et al 2023][research_ji_hua_2023]
- [Ji Teng and Shahneh 2018][research_jiteng_shahneh_2018]
- [Jia and Wang 2024][research_jia_wang_2024]
- [Jia et al 2011][research_jia_han_2011]
- [Jia et al 2019][research_jia_jizhen_2019]
- [Jia et al 2020][research_jia_2020]
- [Jia et al 2020][research_jia_fu_2020]
- [Jia et al 2026][research_jia_qi_2026]
- [Jiang 2011][research_jiang_2011]
- [Jiang and Wang 2023][research_jiang_wang_2023]
- [Jiang and Yang 2014][research_jiang_yang_2014]
- [Jiang and Yu 2019][research_jiang_yu_2019]
- [Jiang et al 2014][research_jiang_ye_2014]
- [Jiang et al 2017][research_jiang_song_2017]
- [Jiang et al 2017][research_jiang_wang_2017]
- [Jiang et al 2017][research_jiang_zhang_2017]
- [Jiang et al 2018][research_jiang_chen_2018]
- [Jiang et al 2018][research_jiang_zhen_2018]
- [Jiang et al 2026][research_jiang_xie_2026]
- [Jianguo et al 2016][research_jianguo_guoqing_2016]
- [Jianguo et al 2017][research_jianguo_xiangyu_2017]
- [Jiao et al 2017][research_jiao_liu_2017]
- [Jiawei 2024][research_jiawei_2024]
- [Jiaxing et al 2025][research_jiaxing_dayi_2025]
- [Jiayuan et al 2018][research_jiayuan_peng_2018]
- [Jie Liang 2020][research_jieliangzhihuilixuguoliweiboshi_2020]
- [Jin et al 2017][research_jin_zhu_2017]
- [Jin et al 2025][research_jin_huang_2025]
- [Jindong and Zhiqiang 2011][research_jindong_zhiqiang_2011]
- [Jing et al 2020][research_jing_qi_2020]
- [Jits et al 2005][research_jits_wright_2005]
- [Jo and Ahn 2021][research_jo_ahn_2021]
- [Jo and Ahn 2022][research_jo_ahn_2022]
- [Jobmann and Thielecke 2024][research_jobmann_thielecke_2024]
- [Joel P and Dr. Vijayan 2014][research_joelp_r_2014]
- [Johannesen et al 1985][research_johannesen_vinh_1985]
- [Johannsen et al 1976][research_johannsen_pfendler_1976]
- [Johansen and Fossen 2020][research_johansen_fossen_2020]
- [Johnis 2023][research_johnis_2023]
- [Johnsen et al 2022][research_johnsen_runnels_2022]
- [Johnson 1949][research_johnson_1949]
- [Johnson 1951][research_johnson_1951]
- [Johnson 1962][research_johnson_1962]
- [Johnson 1967][research_johnson_1967]
- [Johnson 2019][research_johnson_2019]
- [Johnson and Boisseau 1953][research_johnson_1953]
- [Johnson and Ivanov 2011][research_johnson_2011]
- [Johnson et al 2006][research_johnson_shalaev_2006]
- [Johnson et al 2008][research_johnson_calise_2008]
- [Johnson et al 2018][research_johnson_cerimele_2018]
- [Johnson et al 2020][research_johnson_lu_2020]
- [Johnston and Candler 2023][research_johnston_candler_2023]
- [Joint Conference on Lifting 1960][research_joint_conference_1960]
- [Jones 1970][research_jones_1970]
- [Jones and Boiffier 2011][research_jones_boiffier_2011]
- [Jones and Diamant 1989][research_jones_diamant_1989]
- [Jones and Laurence 2025][research_jones_laurence_2025]
- [Jones et al 1987][research_jones_gruszczynski_1987]
- [Joo et al 2008][research_joo_alali_2008]
- [Joo et al 2008][research_joo_ippolito_2008]
- [Joos and Pfife 2012][research_joos_pfife_2012]
- [Joos and Varga 1999][research_joos_varga_1999]
- [Jordan 1980][research_jordan_1980]
- [Jordan 1980][research_jordanjr_1980]
- [Jordan and Bailey 2008][research_jordan_bailey_2008]
- [Jordan and Buffington 1987][research_jordan_buffington_1987]
- [Jordan and Hahne 1992][research_jordan_1992]
- [Jordan et al 2004][research_jordan_2004]
- [Jordan et al 2005][research_jordan_langford_2005]
- [Joshi and Compton 1985][research_joshi_compton_1985]
- [Joshi et al 2015][research_joshi_jeon_2015]
- [Jouannet et al 2008][research_jouannet_2008]
- [Jouannet et al 2012][research_jouannet_berry_2012]
- [Jouannet et al 2017][research_jouannet_lundstrom_2017]
- [Jouhaud 1992][research_jouhaud_1992]
- [Jouhaud et al 2007][research_jouhaud_ferreres_2007]
- [Joyner 1969][research_joyner_1969]
- [Joyner 1970][research_joyner_1970]
- [Ju et al 2022][research_ju_wei_2022]
- [Ju et al 2024][research_ju_jiang_2024]
- [Juang * and Chio 2005][research_juang_chio_2005]
- [Juang and Chien 2008][research_juang_chien_2008]
- [Juhasz et al 2020][research_juhasz_xin_2020]
- [Jump and Padfield 2006][research_jump_padfield_2006]
- [Jumper and Seward 1992][research_jumper_seward_1992]
- [Junaid R and Beebi M 2015][research_junaidr_beebim_2015]
- [Jung 2024][research_jung_2024]
- [Jung et al 2015][research_jung_lee_2015]
- [Jung et al 2025][research_jung_kim_2025]
- [Kadam et al 2018][research_kadam_sathish_2018]
- [Kaertner 2006][research_kaertner_2006]
- [Kageyama and Hiraoka 2004][research_kageyama_hiraoka_2004]
- [Kahn and Edwards 2015][research_kahn_edwards_2015]
- [Kahn and Edwards 2019][research_kahn_edwards_2019]
- [Kai and Ohtake 1996][research_kai_ohtake_1996]
- [Kai et al 2018][research_kai_anglade_2018]
- [Kalden 2007][research_kalden_2007]
- [Kalikhman et al 2018][research_kalikhman_kalikhman_2018]
- [Kam and Gage 2004][research_kam_gage_2004]
- [Kanda et al 2006][research_kanda_ueda_2006]
- [Kaneshige et al 1999][research_kaneshige_bull_1999]
- [Kang and Choi 2024][research_kang_choi_2024]
- [Kang et al 2007][research_kang_li_2007]
- [Kang et al 2025][research_kang_han_2025]
- [Kannan et al][research_kannan_nd]
- [Kansas Univ Lawrence 1952][research_lawrence_1952]
- [Kaplan 2002][research_kaplan_2002]
- [Kaplan et al 2023][research_kaplan_patil_2023]
- [Karasopoulos et al 1998][research_karasopoulos_cervisi_1998]
- [Karel 1967][research_karel_1967]
- [Kariya et al 2020][research_kariya_tanaka_2020]
- [Karlgaard et al 2024][research_karlgaard_deshmukh_2024]
- [Karmarker and Sorensen 1976][research_karmarker_1976]
- [Karpenko et al 2010][research_karpenko_sekhavat_2010]
- [Karpov and Schmidt 1964][research_karpov_schmidt_1964]
- [Karthikeyan et al 2022][research_r_sridhar_2022]
- [Kashkovsky 2014][research_kashkovsky_2014]
- [Kashkovsky et al 2014][research_kashkovsky_vashchenkov_2014]
- [Kashkovsky et al 2019][research_kashkovsky_vashchenkov_2019]
- [Kato 1991][research_kato_1991]
- [Katz and Roglin 2000][research_katz_roglin_2000]
- [Kaufmann and McNally 1995][research_kaufmann_1995]
- [Kaufmann and Ncnally 1995][research_kaufmann_1995_b]
- [Kaushik and Anemaat 2012][research_kaushik_anemaat_2012]
- [Kawaguchi et al 1997][research_kawaguchi_hashimoto_1997]
- [Kawaguchi et al 2017][research_kawaguchi_suzuki_2017]
- [Kawamura and Azimov 2022][research_kawamura_azimov_2022]
- [Kawamura et al][research_kawamura_nd]
- [Kawamura et al][research_kawamura_nd_b]
- [Kawamura et al 2022][research_kawamura_kannan_2022]
- [Kawamura et al 2023][research_kawamura_dolph_2023]
- [Kawato et al 2002][research_kawato_watanabe_2002]
- [Kawato et al 2003][research_kawato_watanabe_2003]
- [Kaynak 2010][research_kaynak_2010]
- [Kayton 1968][research_kayton_1968]
- [Ke et al 2014][research_ke_zhengzhong_2014]
- [Keidel et al 2019][research_keidel_fasel_2019]
- [Keipour et al 2022][research_keipour_2022]
- [Keke et al 2014][research_keke_qing_2014]
- [Kellas 2017][research_kellas_2017]
- [Keller et al 2026][research_keller_mckillipjr_2026]
- [Kelly 1977][research_kelly_1977]
- [Kelly 1994][research_kelly_1994]
- [Kelly and Davis 1994][research_kelly_davis_1994]
- [Kelly and LaBERGE 1980][research_kelly_laberge_1980]
- [Kelly and McNulty 1963][research_kelly_1963]
- [Kelly et al 2010][research_kelly_menich_2010]
- [Kempel 1971][research_kempel_1971]
- [Kempel and Manke 1974][research_kempel_1974]
- [Kempel and Painter 1994][research_kempel_painter_1994]
- [Kempel and Thompson 1971][research_kempel_1971_b]
- [Kempel et al 1970][research_kempel_1970]
- [Kempel et al 1975][research_kempel_1975]
- [Kempel et al 1994][research_kempel_1994]
- [Kendall et al 2022][research_kendall_idris_2022]
- [Kendoul 2012][research_kendoul_2012]
- [Kendoul 2013][research_kendoul_2013]
- [Kendoul et al 2009][research_kendoul_nonami_2009]
- [Kendoul et al 2009][research_kendoul_yu_2009]
- [Kennell et al 2016][research_kennell_neely_2016]
- [Keskin 2026][research_keskin_2026]
- [Ketabdari et al 2020][research_ketabdari_toraldo_2020]
- [Ketterle et al 2008][research_ketterle_vuletic_2008]
- [Keviczky and Balas 2005][research_keviczky_balas_2005]
- [Keviczky and Balas 2006][research_keviczky_balas_2006]
- [Khalifa and Hashim 2026][research_khalifa_hashim_2026]
- [Khalil et al 2023][research_khalil_abdelgawad_2023]
- [Khamlak 2026][research_khamlak_2026]
- [Khan and Chakraborty 2023][research_khan_chakraborty_2023]
- [Khan and Chakraborty 2026][research_khan_chakraborty_2026]
- [Khan et al 2019][research_khan_rajput_2019]
- [Khan et al 2021][research_khan_mehmood_2021]
- [Khanapuri and Rao 2017][research_khanapuri_rao_2017]
- [Kharchenko and Kryukov 2018][research_kharchenko_kryukov_2018]
- [Khattak et al 2023][research_khattak_chan_2023]
- [Khatwa and Helmreich 1999][research_khatwa_helmreich_1999]
- [Khurana and Suzuki 2013][research_khurana_suzuki_2013]
- [Khurana and Suzuki 2014][research_khurana_suzuki_2014]
- [Khurana et al 2012][research_khurana_suzuki_2012]
- [Kiddy 1995][research_kiddy_1995]
- [Kiehn 2020][research_kiehn_2020]
- [Kilgore 1982][research_kilgore_1982]
- [Kilgore and Dress 1984][research_kilgore_dress_1984]
- [Kilgore and Kilgore 1997][research_kilgore_kilgore_1997]
- [Kilgore et al 1974][research_kilgore_adcock_1974]
- [Kim 2026][research_kim_2026]
- [Kim and Choi 2026][research_kim_choi_2026]
- [Kim and Langley 2003][research_kim_langley_2003]
- [Kim and Tahk 2019][research_kim_tahk_2019]
- [Kim and Um 2015][research_kim_um_2015]
- [Kim et al 2006][research_kim_lee_2006]
- [Kim et al 2009][research_kim_kim_2009]
- [Kim et al 2012][research_kim_kim_2012]
- [Kim et al 2014][research_kim_kim_2014]
- [Kim et al 2015][research_kim_shin_2015]
- [Kim et al 2017][research_kim_woo_2017]
- [Kim et al 2018][research_kim_han_2018]
- [Kim et al 2020][research_kim_kim_2020]
- [Kim et al 2021][research_kim_jeong_2021]
- [Kim et al 2021][research_kim_lee_2021]
- [Kim et al 2024][research_kim_woldeyohannis_2024]
- [Kim et al 2026][research_kim_ko_2026]
- [kim hyunsu and Je-hyung Jeon 2018][research_kimhyunsu_jehyungjeon_2018]
- [Kimmel et al 2011][research_kimmel_adamczak_2011]
- [Kineyko 1982][research_kineyko_1982]
- [Kirsten and Ash 1974][research_kirsten_1974]
- [Kish et al 2017][research_kish_rhoney_2017]
- [Klein and Noderer 1992][research_klein_1992]
- [Kleinert and Schleith 2010][research_kleinert_schleith_2010]
- [Klevatt and Gaubatz 1998][research_klevatt_gaubatz_1998]
- [Kling 1989][research_kling_1989]
- [Kling and Hornung 2019][research_kling_hornung_2019]
- [Klingenberg et al 2026][research_klingenberg_willems_2026]
- [Klochan et al 2017][research_klochan_alammouri_2017]
- [Kluever 2004][research_kluever_2004]
- [Kluever 2007][research_kluever_2007]
- [Kluever 2007][research_kluever_2007_b]
- [Kluever 2008][research_kluever_2008]
- [Kluever 2022][research_kluever_2022]
- [Kluever and Horneman 2005][research_kluever_horneman_2005]
- [Kluever and Neal 2015][research_kluever_neal_2015]
- [Kluever et al 2009][research_kluever_horneman_2009]
- [Klumpp 1966][research_klumpp_1966]
- [Klyde and Liang 2009][research_klyde_liang_2009]
- [Knab et al 1995][research_knab_gogel_1995]
- [Knapp 1999][research_knapp_1999]
- [Knapp et al 2017][research_knapp_ivler_2017]
- [Ko and Schuster 1983][research_ko_1983]
- [Ko and Schuster 1984][research_ko_1984]
- [Ko et al 1987][research_ko_1987]
- [Kobald et al 2017][research_kobald_fischer_2017]
- [Kobald et al 2018][research_kobald_fischer_2018]
- [Kobayakawa and Maeda 1978][research_kobayakawa_maeda_1978]
- [Kobayashi and Maita 1995][research_kobayashi_maita_1995]
- [Kobayashi and Tanatsugu 2001][research_kobayashi_tanatsugu_2001]
- [Kobayashi et al 2001][research_kobayashi_sato_2001]
- [Kocamer et al 2022][research_kocamer_uzun_2022]
- [Koch et al 2025][research_koch_wilken_2025]
- [Kock and Fulton 1970][research_kock_1970]
- [Kock and Painter 1968][research_kock_1968]
- [Kock and Painter 1969][research_kock_1969]
- [Kock et al 1972][research_kock_1972]
- [Koelle 1993][research_koelle_1993]
- [Koelle 2000][research_koelle_2000]
- [Koelle 2000][research_koelle_2000_b]
- [Koelle 2002][research_koelle_2002]
- [Koenig and Harris 2017][research_koenig_harris_2017]
- [Kohlman et al 1987][research_kohlman_schweikhard_1987]
- [Kohrs 1982][research_kohrs_1982]
- [Koike et al 2018][research_koike_takahashi_2018]
- [Kokan and Olds 2002][research_kokan_olds_2002]
- [Kolesnikov 2005][research_kolesnikov_2005]
- [Kolnick and Morris 1955][research_kolnick_1955]
- [Kolodziej and Rasky 2003][research_kolodziej_rasky_2003]
- [Komar and Christenson 1996][research_komar_christenson_1996]
- [Komatsu and Ohyagi 2001][research_komatsu_ohyagi_2001]
- [Komatsu et al 2005][research_komatsu_suzuki_2005]
- [Komatsuzaki et al 2016][research_komatsuzaki_doi_2016]
- [Kondrashev and Lutsenko 2026][research_kondrashev_lutsenko_2026]
- [Kondrashov 2023][research_kondrashov_2023]
- [Kong et al 2009][research_kong_lee_2009]
- [Kongkaew et al 2022][research_kongkaew_ruchanurucks_2022]
- [Konstantinidis and Förstner 2020][research_konstantinidis_forstner_2020]
- [Kontinos and Palmer 1999][research_kontinos_palmer_1999]
- [Koo and Sastry 2003][research_koo_sastry_2003]
- [Koo et al 2018][research_koo_natali_2018]
- [Koratkar and Chopra 2001][research_koratkar_chopra_2001]
- [Korn and Doehler 2003][research_korn_doehler_2003]
- [Korzun et al 2020][research_korzun_tang_2020]
- [Kotfilia and Painter 1969][research_kotfilia_painter_1969]
- [Kozak and Sharipov 2012][research_kozak_sharipov_2012]
- [Kozak et al 2013][research_kozak_yildiz_2013]
- [Kozina 1976][research_kozina_1976]
- [Krabacher 1993][research_krabacher_1993]
- [Kramer and Busquets 2000][research_kramer_2000]
- [Kramer et al 2013][research_kramer_2013]
- [Kramer et al 2014][research_kramer_2014]
- [Krammer and Holzapfel 2023][research_krammer_holzapfel_2023]
- [Krammer et al 2021][research_krammer_scherer_2021]
- [Krammer et al 2022][research_krammer_rosenbauer_2022]
- [Krasuski and Wierzbicki 2018][research_krasuski_wierzbicki_2018]
- [Krempasky 1996][research_krempasky_1996]
- [Kreutz 1971][research_kreutz_1971]
- [Kriegsman and Tao 1974][research_kriegsman_tao_1974]
- [Krishnamoorthy and Clarke 2016][research_krishnamoorthy_clarke_2016]
- [Krishnan and Sajikumar 2023][research_krishnan_sajikumar_2023]
- [Krishnan et al 2017][research_krishnan_thejus_2017]
- [Kroncke 1985][research_kroncke_1985]
- [Kruggel et al 1999][research_kruggel_sigal_1999]
- [Krumenacker and Pellicano 1992][research_krumenacker_pellicano_1992]
- [Kryvoruka and Ashurst 1973][research_kryvoruka_ashurst_1973]
- [Krüger et al 1997][research_kruger_besselink_1997]
- [Kubo and Suzuki 2007][research_kubo_suzuki_2007]
- [Kubo and Suzuki 2008][research_kubo_suzuki_2008]
- [Kubota et al 2003][research_kubota_hashimoto_2003]
- [Kubota et al 2020][research_kubota_yoko_2020]
- [Kuchinka 1965][research_kuchinka_1965]
- [Kudo and Kato 1991][research_kudo_kato_1991]
- [Kugler 1996][research_kugler_1996]
- [Kugler and Holzapfel 2017][research_kugler_holzapfel_2017]
- [Kugler and Holzapfel 2017][research_kugler_holzapfel_2017_b]
- [Kugler et al 2018][research_kugler_seiferth_2018]
- [Kulik et al 2025][research_kulik_ruth_2025]
- [Kulu 2025][research_kulu_2025]
- [Kumar 2001][research_kumar_2001]
- [Kumar 2010][research_kumar_2010]
- [Kumar and Mahulikar 2016][research_kumar_mahulikar_2016]
- [Kumar and Mahulikar 2017][research_kumar_mahulikar_2017]
- [Kumar and Padhi 2024][research_kumar_padhi_2024]
- [Kumar et al 2007][research_kumar_shanmugam_2007]
- [Kumar et al 2022][research_kumar_deshpande_2022]
- [Kumar et al 2023][research_kumar_rjustus_2023]
- [Kumar et al 2024][research_kumar_dhanush_2024]
- [Kumar Sulur Loganathan 2023][research_kumarsulurloganathan_2023]
- [Kumtepe et al 2022][research_kumtepe_pollack_2022]
- [Kundu 1990][research_kundu_1990]
- [Kundu 2013][research_kundu_2013]
- [Kunwar and Chakraborty 2025][research_kunwar_chakraborty_2025]
- [Kunwar et al 2026][research_kunwar_putra_2026]
- [Kuppuswamy and Kiran 1981][research_kuppuswamy_kiran_1981]
- [Kurdel et al 2024][research_kurdel_gecejova_2024]
- [Kurniawan et al 2022][research_kurniawan_stefanie_2022]
- [Kutluay et al 2009][research_kutluay_mahmutyazicioglu_2009]
- [Kuzin et al 2009][research_kuzin_lozin_2009]
- [Kwon and Park 2013][research_kwon_park_2013]
- [Kügler et al 2018][research_kugler_heller_2018]
- [Kügler et al 2019][research_kugler_rhein_2019]
- [Kügler et al 2019][research_kugler_rhein_2019_b]
- [La et al 1993][research_la_shivananda_1993]
- [Lachman et al 2025][research_lachman_ratliff_2025]
- [Laforte et al 2015][research_laforte_wesley_2015]
- [Lagimoniere and Avram 2024][research_lagimoniere_avram_2024]
- [Laili and Widayaka 2024][research_laili_widayaka_2024]
- [Lam and Stollenwerk 1966][research_lam_stollenwerk_1966]
- [Lambregts 1981][research_lambregts_1981]
- [Lambregts 1982][research_lambregts_1982]
- [Lamp and Luckner 2015][research_lamp_luckner_2015]
- [Lamy 1983][research_lamy_1983]
- [Lan et al 2020][research_lan_xu_2020]
- [Lan et al 2021][research_lan_tan_2021]
- [Lancaster 1977][research_lancaster_1977]
- [Landherr and Klein 1987][research_landherr_klein_1987]
- [Landherr and Klein 1989][research_landherr_klein_1989]
- [Landing Sites 2008][research_landing_sites_2008]
- [Landing Strip-Sierra Nevada 2020][research_landing_stripsierra_2020]
- [Langberg et al 2022][research_langberg_tyler_2022]
- [Langelaan and Grande 2013][research_langelaan_grande_2013]
- [Langston 1967][research_langston_1967]
- [Langston et al 2021][research_langston_peterson_2021]
- [Lapygin and Yakunina 2009][research_lapygin_yakunina_2009]
- [Larsen 2000][research_larsen_2000]
- [Larsen 2003][research_larsen_2003]
- [Larsen 2005][research_larsen_2005]
- [Larson 1972][research_larson_1972]
- [Larson and Wilson 1967][research_larson_1967]
- [Larsson et al 2020][research_larsson_2020]
- [Laub and White 2006][research_laub_white_2006]
- [Lauer 2006][research_lauer_2006]
- [Laumann 1966][research_laumann_1966]
- [Launius 2013][research_launius_2013]
- [Launius 2013][research_launius_2013_b]
- [Lavender 1965][research_lavender_1965]
- [Lavergne et al 2005][research_lavergne_villaume_2005]
- [Law and McWhorter 1992][research_law_mcwhorter_1992]
- [Lawrance and Sukkarieh 2009][research_lawrance_sukkarieh_2009]
- [Lawrence 1993][research_lawrence_1993]
- [Lawrence et al 2001][research_lawrence_selmon_2001]
- [Layton 1970][research_layton_1970]
- [Layton and McTigue 1969][research_layton_1969]
- [Le 2025][research_le_2025]
- [Le and Goo 2021][research_le_goo_2021]
- [Le and Goo 2021][research_le_goo_2021_b]
- [Le and Goo 2025][research_le_goo_2025]
- [Le et al 2019][research_le_goo_2019]
- [Le et al 2023][research_le_han_2023]
- [Le Goff and Moreau 2013][research_legoff_moreau_2013]
- [Lebacqz and Chen 1977][research_lebacqz_1977]
- [Lee 1974][research_lee_1974]
- [Lee 1976][research_lee_1976]
- [Lee 2009][research_lee_2009]
- [Lee 2011][research_lee_2011]
- [Lee 2023][research_lee_2023]
- [Lee and Basford 1957][research_lee_1957]
- [Lee and Han 2012][research_lee_han_2012]
- [Lee and Mesbahi 2017][research_lee_mesbahi_2017]
- [Lee and Park 2025][research_lee_park_2025]
- [Lee and Swegle 1963][research_lee_1963]
- [Lee et al 1973][research_lee_1973]
- [Lee et al 1998][research_lee_chang_1998]
- [Lee et al 2003][research_lee_ryu_2003]
- [Lee et al 2008][research_lee_soon_2008]
- [Lee et al 2011][research_lee_park_2011]
- [Lee et al 2019][research_lee_chung_2019]
- [Lee et al 2020][research_lee_benedict_2020]
- [Lee et al 2021][research_lee_park_2021]
- [Lee et al 2022][research_lee_payan_2022]
- [Lee et al 2023][research_lee_cho_2023]
- [Lee et al 2026][research_lee_jo_2026]
- [Lee et al 2026][research_lee_kim_2026]
- [Lefevre et al 2025][research_lefevre_lock_2025]
- [Lei and Li 2012][research_lei_li_2012]
- [Lei and Liu 2026][research_lei_liu_2026]
- [Lei et al 2017][research_lei_yan_2017]
- [Lei et al 2020][research_lei_zhong_2020]
- [Lei et al 2021][research_lei_xiaogang_2021]
- [Leisman 2000][research_leisman_2000]
- [Leland and Taylor 1964][research_leland_taylor_1964]
- [Lemmens 2011][research_lemmens_2011]
- [Leng et al 2023][research_leng_wang_2023]
- [Leo et al 2014][research_leo_fenza_2014]
- [Leparoux et al 2022][research_leparoux_herisse_2022]
- [Lesonen et al 2020][research_lesonen_nazarenko_2020]
- [Letchworth 2011][research_letchworth_2011]
- [Leuckert et al 2008][research_leuckert_domhardt_2008]
- [Leveugle and Reinhard 1999][research_leveugle_reinhard_1999]
- [Levin 1968][research_levin_1968]
- [Levy and McDevitt 1964][research_levy_1964]
- [Lewerenz 1987][research_lewerenz_1987]
- [Li 1989][research_li_1989]
- [Li 2008][research_li_2008]
- [Li 2017][research_li_2017]
- [Li 2020][research_li_2020]
- [Li 2025][research_li_2025]
- [Li and Cui 2011][research_li_cui_2011]
- [Li and Duan 2015][research_li_duan_2015]
- [Li and Hu 2018][research_li_hu_2018]
- [Li and Li 2010][research_li_li_2010]
- [Li and Li 2018][research_li_li_2018]
- [Li and Li 2018][research_li_li_2018_b]
- [Li and Li 2018][research_li_li_2018_c]
- [Li and Wu 2024][research_li_wu_2024]
- [Li and Zhang 2021][research_li_zhang_2021_b]
- [Li Bo et al 2016][research_libo_zhangshengbing_2016]
- [Li et al 2004][research_li_yavuz_2004]
- [Li et al 2006][research_li_cui_2006]
- [Li et al 2007][research_li_cui_2007]
- [Li et al 2008][research_li_jing_2008]
- [Li et al 2010][research_li_shen_2010]
- [Li et al 2012][research_li_yang_2012]
- [Li et al 2012][research_li_zhang_2012]
- [Li et al 2013][research_li_cui_2013]
- [Li et al 2014][research_li_pan_2014]
- [Li et al 2014][research_li_qian_2014]
- [Li et al 2016][research_li_chao_2016]
- [Li et al 2016][research_li_wang_2016]
- [Li et al 2017][research_li_jiang_2017]
- [Li et al 2017][research_li_wu_2017]
- [Li et al 2018][research_li_chao_2018]
- [Li et al 2018][research_li_chao_2018_b]
- [Li et al 2018][research_li_xiao_2018]
- [Li et al 2019][research_li_peng_2019]
- [Li et al 2020][research_li_jia_2020]
- [Li et al 2021][research_li_cheng_2021]
- [Li et al 2021][research_li_xiao_2021]
- [Li et al 2021][research_li_zhang_2021]
- [Li et al 2022][research_li_chao_2022]
- [Li et al 2022][research_li_li_2022]
- [Li et al 2022][research_li_luo_2022]
- [Li et al 2022][research_li_shi_2022]
- [Li et al 2023][research_li_hu_2023]
- [Li et al 2023][research_li_li_2023]
- [Li et al 2023][research_li_qi_2023]
- [Li et al 2023][research_li_sun_2023]
- [Li et al 2023][research_li_zeng_2023]
- [Li et al 2023][research_li_zhang_2023]
- [Li et al 2023][research_li_zhao_2023]
- [Li et al 2024][research_li_angelov_2024]
- [Li et al 2024][research_li_chang_2024]
- [Li et al 2024][research_li_wang_2024]
- [Li et al 2024][research_li_xia_2024]
- [Li et al 2024][research_li_xu_2024]
- [Li et al 2024][research_li_zhai_2024]
- [Li et al 2024][research_li_zhai_2024_b]
- [Li et al 2025][research_li_bando_2025]
- [Li et al 2025][research_li_li_2025]
- [Li et al 2025][research_li_pei_2025]
- [Li et al 2025][research_li_wang_2025]
- [Li et al 2025][research_li_xiong_2025]
- [Li et al 2025][research_li_xu_2025]
- [Li et al 2025][research_li_zhao_2025]
- [Li et al 2026][research_li_du_2026]
- [Li et al 2026][research_li_ji_2026]
- [Lian et al 2004][research_lian_bang_2004]
- [Liang and Ren 2018][research_liang_ren_2018]
- [Liang et al 2014][research_liang_li_2014]
- [Liang et al 2020][research_liang_wang_2020]
- [Liang et al 2021][research_liang_chin_2021]
- [Liang et al 2022][research_liang_xu_2022]
- [Liang et al 2025][research_liang_xu_2025]
- [Liao et al 2021][research_liao_li_2021]
- [Liao et al 2023][research_liao_chu_2023]
- [Liao et al 2023][research_liao_song_2023]
- [Liaoni Wu et al 2008][research_liaoniwu_yiminhuang_2008]
- [Liaño et al 2014][research_liano_castillo_2014]
- [Lieberman 1963][research_lieberman_1963]
- [Lieske and Kochenderfer 1966][research_lieske_1966]
- [Lijewski and Suhs 1994][research_lijewski_suhs_1994]
- [Likhachev et al 2014][research_likhachev_sikharulidze_2014]
- [Lin and Cui 2022][research_lin_cui_2022]
- [Lin et al 2020][research_lin_meghdadhasheminasab_2020]
- [Lin et al 2020][research_lin_qi_2020]
- [Lin et al 2026][research_lin_tseng_2026]
- [Lin-lin et al 2015][research_linlin_jianqiao_2015]
- [Lina and Whitten 1968][research_lina_whitten_1968]
- [Lindberg et al 1997][research_lindberg_schade_1997]
- [Ling 2017][research_ling_2017]
- [Liseitsev 2025][research_liseitsev_2025]
- [Littell 2019][research_littell_2019]
- [Littell and Kellas 2018][research_littell_2018]
- [Littell et al 2007][research_littell_2007]
- [Littell et al 2015][research_littell_2015]
- [Litvintsev et al 2019][research_litvintsev_molchanova_2019]
- [Liu 2012][research_liu_2012]
- [Liu 2025][research_liu_2025]
- [Liu 2025][research_liu_2025_b]
- [Liu and Hao 2023][research_liu_hao_2023]
- [Liu and He 2017][research_liu_he_2017]
- [Liu and Lee 2022][research_liu_lee_2022]
- [Liu et al 2002][research_liu_chen_2002]
- [Liu et al 2006][research_liu_li_2006]
- [Liu et al 2006][research_liu_zhou_2006]
- [Liu et al 2011][research_liu_li_2011]
- [Liu et al 2011][research_liu_wang_2011]
- [Liu et al 2014][research_liu_ding_2014]
- [Liu et al 2015][research_liu_liu_2015]
- [Liu et al 2015][research_liu_ren_2015]
- [Liu et al 2016][research_liu_wang_2016]
- [Liu et al 2017][research_liu_chen_2017]
- [Liu et al 2017][research_liu_dai_2017]
- [Liu et al 2017][research_liu_zhang_2017]
- [Liu et al 2018][research_liu_liu_2018]
- [Liu et al 2019][research_liu_xiao_2019]
- [Liu et al 2020][research_liu_hou_2020]
- [Liu et al 2020][research_liu_wang_2020]
- [Liu et al 2021][research_liu_dong_2021]
- [Liu et al 2021][research_liu_zheng_2021]
- [Liu et al 2022][research_liu_liu_2022]
- [Liu et al 2023][research_liu_di_2023]
- [Liu et al 2023][research_liu_he_2023]
- [Liu et al 2023][research_liu_hu_2023]
- [Liu et al 2023][research_liu_wang_2023]
- [Liu et al 2023][research_liu_wang_2023_b]
- [Liu et al 2023][research_liu_yan_2023]
- [Liu et al 2024][research_liu_hu_2024]
- [Liu et al 2024][research_liu_zhang_2024]
- [Liu et al 2024][research_liu_zhang_2024_b]
- [Liu et al 2024][research_liu_zhang_2024_c]
- [Liu et al 2025][research_liu_kuang_2025]
- [Liu et al 2025][research_liu_liu_2025]
- [Liu et al 2025][research_liu_liu_2025_b]
- [Liu et al 2025][research_liu_liu_2025_c]
- [Liu et al 2025][research_liu_sun_2025]
- [Liu Zhi and Wang Yong 2012][research_liuzhi_wangyong_2012]
- [Lockman 1967][research_lockman_1967]
- [Logan 1976][research_logan_1976]
- [Logan et al 1978][research_logan_1978]
- [Logsdon and Williamson 1997][research_logsdon_williamson_1997]
- [London and Sumrall 1999][research_london_1999]
- [Long 1968][research_long_1968]
- [Longani 2000][research_longani_2000]
- [Looye and Joos 2002][research_looye_joos_2002]
- [Looye et al 2001][research_looye_joos_2001]
- [Looye et al 2001][research_looye_willemsen_2001]
- [Looye et al 2002][research_looye_sancho_2002]
- [Lopez 1993][research_lopez_1993]
- [Loureiro et al 2019][research_loureiro_soares_2019]
- [Lovell and Parlett 1956][research_lovell_1956]
- [Lovtsov and Karpov 2011][research_lovtsov_karpov_2011]
- [Lu 1996][research_lu_1996]
- [Lu 1997][research_lu_1997]
- [Lu 1999][research_lu_1999]
- [Lu 2021][research_lu_2021]
- [Lu 2021][research_lu_2021_b]
- [Lu and Lei 2010][research_lu_lei_2010]
- [Lu and Tao 2025][research_lu_tao_2025]
- [Lu and Yang 2018][research_lu_yang_2018]
- [Lu et al 2005][research_lu_antoun_2005]
- [Lu et al 2010][research_lu_wang_2010]
- [Lu et al 2015][research_lu_zhang_2015]
- [Lu et al 2016][research_lu_zhang_2016]
- [Lu et al 2017][research_lu_harris_2017]
- [Lu et al 2017][research_lu_lei_2017]
- [Lu et al 2019][research_lu_zhang_2019]
- [Lu et al 2021][research_lu_wang_2021]
- [Lu et al 2024][research_lu_yue_2024]
- [Lu Keke et al 2016][research_lukeke_yujinyong_2016]
- [Lucas 1978][research_lucas_1978]
- [Lugo et al 2014][research_lugo_tolson_2014]
- [Lugo et al 2022][research_lugo_dwyercianciolo_2022]
- [Lund 2004][research_lund_2004]
- [Lungu 2017][research_lungu_2017]
- [Lungu and Lungu 2015][research_lungu_lungu_2015]
- [Lungu and Lungu 2015][research_lungu_lungu_2015_b]
- [Lungu and Lungu 2018][research_lungu_lungu_2018]
- [Lungu et al 2011][research_lungu_lungu_2011]
- [Luo and Li 2011][research_luo_li_2011]
- [Luo et al 2021][research_luo_guo_2021]
- [Luo et al 2022][research_luo_wu_2022]
- [Luo et al 2025][research_luo_liu_2025]
- [Luo et al 2025][research_luo_song_2025]
- [Luo et al 2026][research_luo_tang_2026]
- [Luong et al 2025][research_luong_le_2025]
- [Luria and Guyton 1992][research_luria_guyton_1992]
- [Lusty and Miele 1966][research_lusty_miele_1966]
- [Luyang Liang et al 2016][research_luyangliang_fengzhou_2016]
- [Lv and Zhou 2023][research_lv_zhou_2023]
- [Lv et al 2021][research_lv_an_2021]
- [Lv et al 2023][research_lv_wang_2023]
- [Lv et al 2024][research_lv_fan_2024]
- [Lykken and Shah 1971][research_lykken_shah_1971]
- [Lyons 1961][research_lyons_1961]
- [Lyons 1977][research_lyons_1977]
- [Lystad 1975][research_lystad_1975]
- [Lévesque and de Lafontaine 2006][research_levesque_delafontaine_2006]
- [Löbl et al 2018][research_lobl_weiss_2018]
- [M2-F2 Lifting Body Accident 1967][research_m2_f2_1967]
- [Ma et al 2005][research_ma_zhao_2005]
- [Ma et al 2013][research_ma_sun_2013]
- [Ma et al 2013][research_ma_wu_2013]
- [Ma et al 2018][research_ma_chen_2018]
- [Ma et al 2018][research_ma_guan_2018]
- [Ma et al 2020][research_ma_wu_2020]
- [Ma et al 2024][research_ma_liu_2024]
- [Ma et al 2025][research_ma_ding_2025]
- [Maass et al 2020][research_maass_woicke_2020]
- [MacAllister 1955][research_macallister_1955]
- [MacConochie 2000][research_macconochie_2000]
- [Machin and Daum 2026][research_machin_daum_2026]
- [Machnik et al 2022][research_machnik_decker_2022]
- [Mackay et al 2016][research_mackay_ellingson_2016]
- [Mackinnon and Madden 1971][research_mackinnon_madden_1971]
- [MACKlNNON and Madden 1972][research_macklnnon_madden_1972]
- [MacLeod 2026][research_macleod_2026]
- [Macmillan 1981][research_macmillan_1981]
- [Macy et al 1989][research_macy_shea_1989]
- [Madden 1958][research_madden_1958]
- [Madden and Desai 1973][research_madden_desai_1973]
- [Maddock and Minisci 2016][research_maddock_minisci_2016]
- [Madigan 1970][research_madigan_1970]
- [Maeda et al 2014][research_maeda_otsuki_2014]
- [Maeda et al 2016][research_maeda_otsuki_2016]
- [Maemori et al 2003][research_maemori_tanigawa_2003]
- [Maggin and Bennett 1947][research_maggin_1947]
- [Mahmood 2025][research_mahmood_2025]
- [Mahmood and ur Rehman 2023][research_mahmood_urrehman_2023]
- [Mahmood et al 2022][research_mahmood_rehman_2022]
- [Mahmoud and Maaruf 2021][research_mahmoud_maaruf_2021]
- [Mahony and Hamel 2001][research_mahony_hamel_2001]
- [Mahoor et al 2010][research_mahoor_godzdanker_2010]
- [Mahrous et al 2026][research_mahrous_khalil_2026]
- [Mahulikar et al 2008][research_mahulikar_khurana_2008]
- [Maikapar 1993][research_maikapar_1993]
- [Maiorova et al 2016][research_maiorova_prosuntsov_2016]
- [Maita and Kobayashi 1996][research_maita_kobayashi_1996]
- [Maita et al 1993][research_maita_stockmans_1993]
- [Maiuzzo 1970][research_maiuzzo_1970]
- [Makarenko et al 2017][research_makarenko_makarov_2017]
- [Malloy and Chang 1998][research_malloy_chang_1998]
- [Mammarella et al 2011][research_mammarella_rodrigalvarez_2011]
- [Mandal and Gu 2016][research_mandal_gu_2016]
- [Manfred and Ryno 2008][research_manfred_ryno_2008]
- [Mangum 1965][research_mangum_1965]
- [Mani 2007][research_mani_2007]
- [Manjarrez et al 2018][research_manjarrez_davila_2018]
- [Manke et al 1970][research_manke_1970]
- [Manley et al 2000][research_manley_2000]
- [Mannai 1962][research_mannai_1962]
- [Manning and Gleason 1992][research_manning_gleason_1992]
- [Manning et al 1992][research_manning_baum_1992]
- [Manokaran et al 2009][research_manokaran_vidya_2009]
- [Manu et al 2024][research_c_vinaykumar_2024]
- [Mao et al 2018][research_mao_dou_2018]
- [Mao et al 2019][research_mao_xue_2019]
- [Marantos et al 2017][research_marantos_karras_2017]
- [Marcum 1998][research_marcum_1998]
- [Marcum 1998][research_marcum_1998_b]
- [Marcum 2000][research_marcum_2000]
- [Margaria et al 2007][research_margaria_dovis_2007]
- [Marinelli and Green 1988][research_marinelli_green_1988]
- [Mario Andres Cordoba 2001][research_marioandrescordoba_2001]
- [Mark 2009][research_mark_2009]
- [Marley and Driscoll 2017][research_marley_driscoll_2017]
- [Marley and Driscoll 2018][research_marley_driscoll_2018]
- [Marlow 2003][research_marlow_2003]
- [Marschall 2011][research_marschall_2011]
- [Marshall 1986][research_marshall_1986_b]
- [Marshall et al 2011][research_marshall_cronin_2011]
- [Marshall et al 2021][research_marshall_sun_2021]
- [Martin 2006][research_martin_2006]
- [Martin and Boyd 2008][research_martin_boyd_2008]
- [Martin and Panesi 2022][research_martin_panesi_2022]
- [Martin et al 2004][research_martin_hallam_2004]
- [Martin et al 2024][research_martin_stay_2024]
- [Martindale 2006][research_martindale_2006]
- [Martins et al 2025][research_martins_rassi_2025]
- [Martorella et al 1981][research_martorella_kelly_1981]
- [Martínez Morán 2018][research_martinezmoran_2018]
- [Marylin et al 2007][research_marylin_christian_2007]
- [Masafumi Morimoto et al 2007][research_masafumimorimoto_kenjiuchiyama_2007]
- [Masaki and Yakura 1968][research_masaki_yakura_1968]
- [Masilamani et al 2018][research_masilamani_kumar_2018]
- [Mason et al 2021][research_mason_zahn_2021]
- [Massa and Cervenka 1995][research_massa_1995]
- [Mastromatteo et al 2023][research_mastromatteo_gaverina_2023]
- [Mastromatteo et al 2026][research_mastromatteo_gaverina_2026]
- [Mathavaraj and Padhi 2017][research_s_padhi_2017]
- [Mathavaraj and Padhi 2020][research_mathavaraj_padhi_2020]
- [Mathavaraj et al 2010][research_mathavaraj_halbe_2010]
- [Mathew et al 2023][research_mathew_dutta_2023]
- [Matranga 1961][research_matranga_1961]
- [Matranga and Armstrong 1959][research_matranga_1959b]
- [Matranga and Menard 1959][research_matranga_1959a]
- [Matsuda et al 2013][research_matsuda_kihara_2013]
- [Matsumoto et al 2015][research_matsumoto_kondoh_2015]
- [Matsunaga et al 2017][research_matsunaga_takahashi_2017]
- [Matveev 2017][research_matveev_2017]
- [Mauritz et al 1997][research_mauritz_1997]
- [Maurya et al 2021][research_maurya_wang_2021]
- [Maxwell 2017][research_maxwell_2017]
- [Mayanna et al 2006][research_mayanna_grimm_2006]
- [Mayhue 1962][research_mayhue_1962]
- [Mazaheri et al 2014][research_mazaheri_bruce_2014]
- [Mazur 2020][research_mazur_2020]
- [Mbagwu et al 2023][research_mbagwu_dalle_2023]
- [McAfee et al 2025][research_mcafee_alpert_2025]
- [McAfee et al 2026][research_mcafee_rabin_2026]
- [McAnally and Engel 1979][research_mcanally_engel_1979]
- [McCabe and DeMars 2018][research_mccabe_demars_2018]
- [McCabe et al 2017][research_mccabe_brown_2017]
- [McCafferty et al 2014][research_mccafferty_woodward_2014]
- [McClinton et al 1998][research_mcclinton_voland_1998]
- [McClure 1998][research_mcclure_1998]
- [McCown-McClintick and Orr 2000][research_mccown_mcclintick_2000]
- [McDowell and Williamson 1980][research_mcdowell_williamsonjr_1980]
- [McDowell and Williamson 1982][research_mcdowell_williamsonjr_1982]
- [McFarland 1981][research_mcfarland_1981]
- [McFARLAND 1991][research_mcfarland_1991]
- [McFarland 1994][research_mcfarland_1994]
- [McGee 1977][research_mcgee_1977]
- [McGee et al 1981][research_mcgee_foster_1981]
- [McGee et al 1981][research_mcgee_paulkjr_1981]
- [McGehee et al 1959][research_mcgehee_1959]
- [McGuire et al 2004][research_mcguire_gage_2004]
- [McKenzie 2003][research_mckenzie_2003]
- [McKown et al][research_mckown_nd]
- [McNally and Bach 1988][research_mcnally_1988]
- [McNally et al 1992][research_mcnally_warner_1992]
- [McQuellin and Buttsworth 2024][research_mcquellin_buttsworth_2024]
- [McTigue 1970][research_mctigue_1970]
- [McTigue and Ryan 1968][research_mctigue_ryan_1968]
- [Mead 1998][research_mead_1998]
- [Meckler 1965][research_meckler_1965]
- [Mehmood et al 2021][research_mehmood_majeed_2021]
- [Mehra 1971][research_mehra_1971]
- [Mehrotra and Robinson 1982][research_mehrotra_robinson_1982]
- [Mehta 1989][research_mehta_1989]
- [Mehta and Bowles 2001][research_mehta_bowles_2001]
- [Mehta and Bowles 2001][research_mehta_bowles_2001_b]
- [Mehta et al 2012][research_mehta_bowles_2012]
- [Mehta et al 2014][research_mehta_bowles_2014]
- [Mejias and Eng 2012][research_mejias_eng_2012]
- [Melgaard 1986][research_melgaard_1986]
- [Melnyk et al 2021][research_melnyk_beattie_2021]
- [Mendes and Langley 1999][research_mendes_langley_1999]
- [Mendham 2003][research_mendham_2003]
- [Menees et al 1987][research_menees_wilson_1987]
- [Meng et al 2009][research_meng_wu_2009]
- [Meng et al 2016][research_meng_jiang_2016]
- [Meng et al 2018][research_meng_he_2018]
- [Meng et al 2019][research_meng_wang_2019]
- [Meng et al 2022][research_meng_gao_2022]
- [Menon et al 2009][research_menon_postlethwaite_2009]
- [Menon et al 2010][research_menon_vaddi_2010]
- [Menon et al 2025][research_menon_ck_2025]
- [Meriwether and Harris 1962][research_meriwether_1962]
- [Merlin 2006][research_merlin_2006]
- [Merlin 2014][research_merlin_2014]
- [Meseguer et al 2012][research_meseguer_perezgrande_2012]
- [Metzger 1970][research_metzger_1970]
- [Meyer 1970][research_meyer_1970]
- [Meyer et al 1981][research_meyerjr_jarvis_1981]
- [Meyers and Weiderman 1988][research_meyers_weiderman_1988]
- [Meyers et al 1968][research_meyers_tompkins_1968]
- [Meyerson 1990][research_meyerson_1990]
- [Meyerson 1998][research_meyerson_1998]
- [Meyerson and Taylor 2001][research_meyerson_taylor_2001]
- [Mhenni et al 2016][research_mhenni_choley_2016]
- [Mi et al 2018][research_mi_lu_2018]
- [Miao et al 2026][research_miao_wang_2026]
- [Miccio et al 2024][research_miccio_veneruso_2024]
- [Michalski and Johnson 2007][research_michalski_johnson_2007]
- [Mickelson and Carrico 1989][research_mickelson_carrico_1989]
- [Microwave scanning beam landing 1977][research_microwave_scanning_1977]
- [Midtfjord and Huseby 2020][research_midtfjord_huseby_2020]
- [Miele et al 1987][research_miele_wang_1987]
- [Miele et al 1988][research_miele_wang_1988]
- [Miele et al 1988][research_miele_wang_1988_b]
- [Mikhailov and Nedel'ko 2012][research_mikhailov_nedelko_2012]
- [Mikhailov and Nedel'ko 2012][research_mikhailov_nedelko_2012_b]
- [Miki and Fujii 2018][research_miki_fujii_2018]
- [Mikrin et al 2020][research_mikrin_orlovskii_2020]
- [Mikula et al 2000][research_mikula_holthaus_2000]
- [Miller 1963][research_miller_1963]
- [Miller 1979][research_millerjr_1979]
- [Miller et al 2023][research_miller_kazemba_2023]
- [Miller et al 2023][research_miller_kazemba_2023_b]
- [Milner 2002][research_milner_2002]
- [Milner et al 2022][research_milner_macabiau_2022]
- [Milos and Chen 2013][research_milos_chen_2013]
- [Milos and Squire 1999][research_milos_squire_1999]
- [Minami and Tsukamoto 2006][research_minami_tsukamoto_2006]
- [Minghui et al 2017][research_minghui_qiuying_2017]
- [Minisci and Vasile 2013][research_minisci_vasile_2013]
- [Minnema et al 2019][research_minnema_mayersoares_2019]
- [Minor et al 2004][research_minor_2004]
- [Minwen and Dayi 2014][research_minwen_dayi_2014]
- [Miotto and LePome 2003][research_miotto_lepome_2003]
- [Miotto and Paduano 1995][research_miotto_paduano_1995]
- [Miotto and Paduano 1996][research_miotto_paduano_1996]
- [Miso et al 1999][research_miso_1999]
- [Misra and Bai 2019][research_misra_bai_2019]
- [Misra et al 2022][research_misra_fraticellirivera_2022]
- [Mitchell 2004][research_mitchell_2004]
- [Mitchell and Hoh 1983][research_mitchell_hoh_1983]
- [Miyakawa et al 1985][research_miyakawa_hirose_1985]
- [Miyashita et al 2024][research_miyashita_sugihara_2024]
- [Miyazawa et al 1993][research_miyazawa_ishikawa_1993]
- [Miyazawa et al 1996][research_miyazawa_ishikawa_1996]
- [Miyazawa et al 1998][research_miyazawa_motoda_1998]
- [Miyazawa et al 1999][research_miyazawa_motoda_1999]
- [Mo et al 2018][research_mo_jianhua_2018]
- [Mo et al 2023][research_mo_lu_2023]
- [Mo et al 2024][research_mo_li_2024]
- [Mockenhaupt and Wells 1981][research_mockenhaupt_wells_1981]
- [Mohaghegh 2025][research_mohaghegh_2025]
- [Mohamed and Mamatas 2012][research_mohamed_mamatas_2012]
- [Mohamed et al 2022][research_mohamed_safwat_2022]
- [Mohammadkarimi and Nobahari 2018][research_mohammadkarimi_nobahari_2018]
- [Mohan et al 2025][research_mohan_s_2025]
- [Mohiuddin et al 2025][research_mohiuddin_2025]
- [Moholkar et al 2024][research_moholkar_2024]
- [Moiseev and Poluboyarinov 2011][research_moiseev_poluboyarinov_2011]
- [Mokrane et al 2022][research_mokrane_benallegue_2022]
- [Mokry 1974][research_mokry_1974]
- [Molchanova et al 2016][research_molchanova_kashkovsky_2016]
- [Molina et al 1996][research_molina_simeonides_1996]
- [Monteil 2024][research_monteil_2024]
- [Montella et al 2024][research_montella_vio_2024]
- [Monti et al 2001][research_monti_paterna_2001]
- [Moog et al 1979][research_moog_1979]
- [Mooij 2003][research_mooij_2003]
- [Mooij 2024][research_mooij_2024]
- [Mooij and Hanninen 2009][research_mooij_hanninen_2009]
- [Moore 1991][research_moore_1991]
- [Moore 2013][research_moore_2013]
- [Moorhouse 1990][research_moorhouse_1990]
- [Moorhouse 1991][research_moorhouse_1991]
- [Moorhouse 1994][research_moorhouse_1994]
- [Moorhouse and Fielding 1998][research_moorhouse_fielding_1998]
- [Moran et al 2023][research_moran_mcquellin_2023]
- [Moreira et al 2022][research_moreira_gripp_2022]
- [Morelli 2009][research_morelli_2009]
- [Morelli and Klein 1995][research_morelli_1995]
- [Morello et al 1977][research_morello_1977]
- [Moreno et al 2018][research_moreno_fugenschuh_2018]
- [Morgado et al 2022][research_morgado_garbacz_2022]
- [Morgan and Williams 2025][research_morgan_williams_2025]
- [Morgenfeld 1992][research_morgenfeld_1992]
- [Mori et al 1999][research_mori_maita_1999]
- [Mori et al 2001][research_mori_maita_2001]
- [Morino et al 2001][research_morino_shimoda_2001]
- [Morio et al 2007][research_morio_falcoz_2007]
- [Morio et al 2009][research_morio_cazaurang_2009]
- [Morio et al 2010][research_morio_cazaurang_2010]
- [Moriwaki 2015][research_moriwaki_2015]
- [Morris 1995][research_morrisjr_1995]
- [Morrison et al 1982][research_morrison_chien_1982]
- [Morth 1972][research_morth_1972]
- [Mosby 1965][research_mosby_1965]
- [Moses et al 1999][research_moses_1999]
- [Motaghedi 2003][research_motaghedi_2003]
- [Motoda et al 1999][research_motoda_miyazawa_1999]
- [Moura and Borges Ribeiro 2025][research_moura_borgesribeiro_2025]
- [Moura and Borges Ribeiro 2025][research_moura_borgesribeiro_2025_b]
- [Moura and Borges Ribeiro 2025][research_moura_borgesribeiro_2025_c]
- [Mourikis et al 2007][research_mourikis_trawny_2007]
- [Mouritsen 1994][research_mouritsen_1994]
- [Mowry and Grasso 2020][research_mowry_grasso_2020]
- [Mu and Zhang 2014][research_mu_zhang_2014]
- [Mu et al 2016][research_mu_yu_2016]
- [Mu et al 2018][research_mu_yu_2018]
- [Mu et al 2019][research_mu_yu_2019]
- [Mu et al 2023][research_mu_zhang_2023]
- [Muehter 1974][research_muehter_1974]
- [Mueller et al 2012][research_mueller_landolt_2012]
- [Muhammad Hadi Widanto et al 2025][research_muhammadhadiwidanto_rizkifitriansyah_2025]
- [Muhlstein et al 1974][research_muhlsteinjr_petroff_1974]
- [Mukhopadhyay 1969][research_mukhopadhyay_1969]
- [Mukundan et al 2022][research_mukundan_maity_2022]
- [Mulcare et al 1982][research_mulcare_ness_1982]
- [Mullenix and Povitsky 2016][research_mullenix_povitsky_2016]
- [Mumm and Holzapfel 2017][research_mumm_holzapfel_2017]
- [Munguía 2014][research_munguia_2014]
- [Munusamy et al 2022][research_munusamy_stephen_2022]
- [Munzing and Catris 2015][research_munzing_catris_2015]
- [Muraca and King 1975][research_muraca_1975]
- [Murakami et al 2008][research_murakami_kwak_2008]
- [Murali et al 2024][research_murali_moreno_2024]
- [Murch et al 2009][research_murch_cox_2009]
- [Murcia Piñeros et al 2022][research_murciapineros_vilhenademoraes_2022]
- [Murman 1982][research_murman_1982]
- [Murphy 1956][research_murphy_1956]
- [Murphy 1963][research_murphy_1963]
- [Murray-Smith 1995][research_murraysmith_1995]
- [Murri et al 1984][research_murri_1984]
- [Musal et al 1964][research_musal_hm_1964]
- [Mwenegoha et al 2019][research_mwenegoha_moore_2019]
- [Ménou][research_menou_nd]
- [Nabi and Najafi 2024][research_nabi_najafi_2024]
- [Nadan and Lee 2018][research_nadan_lee_2018]
- [Naeseth 1970][research_naeseth_1970]
- [Naftel and Powell 1993][research_naftel_1993]
- [Naftel et al 1986][research_naftel_1986]
- [Nag et al 2023][research_nag_senthil_2023]
- [Nagarani et al 2020][research_nagarani_venkatakrishnan_2020]
- [Nagarjuna and Suresh 2015][research_nagarjuna_suresh_2015]
- [Nagel 1983][research_nagel_1983]
- [Najam 2014][research_najam_2014]
- [Najson and Mease 2005][research_najson_mease_2005]
- [Nakamura et al 2014][research_nakamura_kamimura_2014]
- [Nakasato et al 2015][research_nakasato_takahashi_2015]
- [Nakhod 2026][research_nakhod_2026]
- [Nance 2013][research_nance_2013]
- [Nanda et al 2025][research_nanda_gopalakrishna_2025]
- [Narkiewicz and Zasuwa 2002][research_narkiewicz_2002]
- [Nastasi et al 1983][research_nastasi_martorella_1983]
- [Nathan 2007][research_nathan_2007]
- [Nazar et al 2020][research_nazar_gandhi_2020]
- [Nazir et al 2018][research_nazir_aziz_2018]
- [Neal 1970][research_neal_1970]
- [Neal 1973][research_neal_1973]
- [Nebylov and Nebylov 2011][research_nebylov_nebylov_2011]
- [Nedel'ko and Alimov 2018][research_nedelko_alimov_2018]
- [Negre 1991][research_negre_1991]
- [Nelson 2003][research_nelson_2003]
- [Nelson et al 1993][research_nelson_arenajr_1993]
- [Nelson et al 1997][research_nelson_price_1997]
- [Neri et al 2010][research_neri_macabiau_2010]
- [Neuhaus 2018][research_neuhaus_2018]
- [Neumaier et al 2022][research_neumaier_kranemann_2022]
- [Neumannn et al 2016][research_neumannn_moore_2016]
- [Neusypin et al 2023][research_neusypin_kupriyanov_2023]
- [Newman and Bailey 1987][research_newman_bailey_1987]
- [Newman et al 1992][research_newman_fulcher_1992]
- [Newman et al 2014][research_newman_parham_2014]
- [Newsom and Anglin 1975][research_newsom_1975]
- [Ngo and Blake 2003][research_ngo_blake_2003]
- [Ngo and Doman 2002][research_ngo_doman_2002]
- [Nguyen and Jacklin 2010][research_nguyen_jacklin_2010]
- [Nguyen et al 2018][research_nguyen_cao_2018]
- [Nguyen et al 2020][research_nguyen_kostiukov_2020]
- [Nguyen et al 2022][research_nguyen_2022]
- [Nho and Agarwal 1998][research_nho_agarwal_1998]
- [Ni et al 2023][research_ni_dai_2023]
- [Ni et al 2026][research_ni_wei_2026]
- [Nial 1972][research_nial_1972]
- [Nicolaides 1953][research_nicolaides_1953]
- [Nicolaides and Clare 1969][research_nicolaides_1969]
- [Nie et al 2023][research_nie_zhang_2023]
- [Niebanck 1969][research_niebanck_1969]
- [Niehaus 1962][research_niehaus_1962]
- [Nielson et al 1986][research_nielson_swearingen_1986]
- [Niemela 1982][research_niemela_1982]
- [Nietubicz 1975][research_nietubicz_1975]
- [Niewald and Parker 1999][research_niewald_parker_1999]
- [Ning et al 2007][research_ning_zhang_2007]
- [Ninomiya et al 2005][research_ninomiya_suzuki_2005]
- [Ninomiya et al 2006][research_ninomiya_suzuki_2006]
- [Nippress and Wilson 1992][research_nippress_wilson_1992]
- [Niu et al 2019][research_niu_meng_2019]
- [Niu et al 2025][research_niu_wang_2025]
- [Nizin et al 2016][research_nizin_antony_2016]
- [Nobahari and Mohammadkarimi 2017][research_nobahari_mohammadkarimi_2017]
- [Nogar 2020][research_nogar_2020]
- [Noh et al 2024][research_noh_sharif_2024]
- [Nomura et al 2022][research_nomura_itabashi_2022]
- [Nonami et al 2010][research_nonami_kendoul_2010]
- [Nonami et al 2010][research_nonami_kendoul_2010_b]
- [Norton 1922][research_norton_1922]
- [Norwood and Chichester 2015][research_norwood_chichester_2015]
- [Noureldin et al 2012][research_noureldin_karamat_2012]
- [Noureldin et al 2012][research_noureldin_karamat_2012_b]
- [Novakovic 2014][research_novakovic_2014]
- [Nowak et al 2022][research_nowak_kopecki_2022]
- [Nuhija 2021][research_nuhija_2021]
- [Numata et al 2013][research_numata_tsuchiya_2013]
- [Nurse et al 1978][research_nurse_prohaska_1978]
- [Nurse et al 1978][research_nurse_prohaska_1978_b]
- [Nutt and Martindale 1976][research_nutt_martindale_1976]
- [O'Kelly 1955][research_o_kelly_1955]
- [O`Callaghan 2016][research_ocallaghan_2016]
- [Obermann and Williamson 1998][research_obermann_williamson_1998]
- [Obermark 2004][research_obermark_2004]
- [Obye and Hakim 1984][research_obye_hakim_1984]
- [Ochi 2004][research_ochi_2004]
- [Octavianie and Ichsan 2020][research_octavianie_ichsan_2020]
- [Oertel 1993][research_oertel_1993]
- [Oglesby 1975][research_oglesby_1975]
- [Ogneru and Raileanu 2026][research_ogneru_raileanu_2026]
- [Ohara et al 2001][research_ohara_2001]
- [Ohe et al 2014][research_ohe_oyama_2014]
- [Ohkami et al 1991][research_ohkami_yamanaka_1991]
- [Ohno et al 1998][research_ohno_yamaguchi_1998]
- [Ohno et al 1999][research_ohno_yamaguchi_1999]
- [Ohya and Kato 1985][research_ohya_kato_1985]
- [Oishi et al 2002][research_oishi_2002]
- [Okada 1994][research_okada_1994]
- [Okafor et al 2018][research_okafor_jemitola_2018]
- [Okojie et al 2023][research_okojie_go_2023]
- [Olds 1998][research_olds_1998]
- [Olds and Bellini 1998][research_olds_bellini_1998]
- [Olds et al 1999][research_olds_bradford_1999]
- [Olejnik et al 2019][research_olejnik_kachel_2019]
- [Olejnik et al 2020][research_olejnik_kachel_2020]
- [Olivares-Mendez et al 2013][research_olivaresmendez_mondragon_2013]
- [Olson 2015][research_olson_2015]
- [Olson and Sunkel 1983][research_olson_sunkel_1983]
- [Olynick 1996][research_olynick_1996]
- [Olynick 1998][research_olynick_1998]
- [Olynick and Henline 1996][research_olynick_henline_1996]
- [Ortloff 1968][research_ortloff_1968]
- [Osder 1970][research_osder_1970]
- [Otsu 2016][research_otsu_2016]
- [Otsu 2018][research_otsu_2018]
- [Otsu and Takama 2012][research_otsu_takama_2012]
- [Otsu et al 1998][research_otsu_suzuki_1998]
- [Otsu et al 2001][research_otsu_kanai_2001]
- [Otsu et al 2004][research_otsu_matsushita_2004]
- [Otsu et al 2006][research_otsu_abe_2006]
- [Otsu et al 2006][research_otsu_matsuda_2006]
- [Otsu et al 2008][research_otsu_nakamura_2008]
- [Otsu et al 2009][research_otsu_katsurayama_2009]
- [Otsu et al 2015][research_otsu_yamada_2015]
- [Oudin et al 2013][research_oudin_puyou_2013]
- [Ouellette et al 2012][research_ouellette_patil_2012]
- [Ouellette et al 2014][research_ouellette_patil_2014]
- [Ouyang and Wu 2021][research_ouyang_wu_2021]
- [Owens et al 2006][research_owens_cox_2006]
- [Oza et al 2015][research_oza_hu_2015]
- [P.V and Laxman 2023][research_pv_laxman_2023]
- [Pace and Maji 2008][research_pace_maji_2008]
- [Paciorri et al 2026][research_paciorri_assonitis_2026]
- [Packard et al 2009][research_packard_seiler_2009]
- [Padhi and Chawla 2016][research_padhi_chawla_2016]
- [Padmanabhan and Dowell 2015][research_padmanabhan_dowell_2015]
- [Painter and Sitterle 1972][research_painter_1972]
- [Painter and Sitterle 1974][research_painter_1974]
- [Palaninathan and Bindu 2005][research_palaninathan_bindu_2005]
- [Paletta et al 2013][research_paletta_belardo_2013]
- [Paletta et al 2015][research_paletta_dmytriv_2015]
- [Pallister et al 1992][research_pallister_parker_1992]
- [Palmer et al 1997][research_palmer_henline_1997]
- [Palmer et al 2009][research_palmer_pulsonetti_2009]
- [Palomino 2022][research_palomino_2022]
- [Palumbo et al 2012][research_palumbo_morani_2012]
- [Pan et al 2025][research_pan_ma_2025]
- [Panda 2022][research_panda_2022]
- [Panzieri et al 2002][research_panzieri_pascucci_2002]
- [Paolozzi 2004][research_paolozzi_2004]
- [Papadopoulos and Subrahmanyam 2005][research_papadopoulos_subrahmanyam_2005]
- [Paquita et al 2024][research_paquita_persadanta_2024]
- [Paraforos et al 2015][research_paraforos_griepentrog_2015]
- [Paranjape 2023][research_paranjape_2023]
- [Park 2020][research_park_2020]
- [Park and Derose 1980][research_park_1980]
- [Park and Park 2017][research_park_park_2017]
- [Park et al 2012][research_park_lee_2012]
- [Park et al 2015][research_park_kim_2015]
- [Park et al 2019][research_park_jung_2019]
- [Park et al 2025][research_park_yang_2025]
- [Parker 2022][research_parker_2022]
- [Parker and Templeman 1967][research_parker_templeman_1967]
- [Parkinson and Fitzgibbon 1989][research_parkinson_fitzgibbon_1989]
- [Parlett 1974][research_parlett_1974_b]
- [Parlett et al 1974][research_parlett_1974]
- [Parlini 1988][research_parlini_1988]
- [Parracino et al 2024][research_parracino_ceresoli_2024]
- [Parrish and Martin 1975][research_parrish_1975]
- [Pashilkar et al 2016][research_pashilkar_haijun_2016]
- [Pasindu 2020][research_pasindu_2020]
- [Pasindu and Fwa 2015][research_pasindu_fwa_2015]
- [Pastore et al 2021][research_pastore_delfini_2021]
- [Patel and Subbarao 2024][research_patel_subbarao_2024]
- [Patel and Venkatasubbaiah 2015][research_patel_venkatasubbaiah_2015]
- [Patera 2006][research_patera_2006]
- [Patrick 1972][research_patrick_1972]
- [Paul et al 2019][research_paul_suresh_2019]
- [Paulson 1959][research_paulson_1959]
- [Paulson and Johnson 1947][research_paulson_1947]
- [Paulson and Johnson 1947][research_paulson_1947_b]
- [Pausder et al 1983][research_pausder_meyer_1983]
- [Pavanasam et al 2024][research_pavanasam_anil_2024]
- [Pavlinsky 1993][research_pavlinsky_1993]
- [Pavlov and Simakova 2021][research_pavlov_simakova_2021]
- [Payne et al 1975][research_payne_shoaf_1975]
- [Peach et al 1980][research_peach_1980]
- [Peck][research_peck_nd]
- [Peele et al 1968][research_peele_1968]
- [Pei et al 2025][research_pei_liu_2025]
- [Peicheng et al 2018][research_peicheng_rong_2018]
- [Peipei et al 2017][research_peipei_junbo_2017]
- [Peng et al 2019][research_peng_qi_2019]
- [Peng et al 2020][research_peng_qi_2020]
- [Peng et al 2025][research_peng_li_2025]
- [Pengxin et al 2015][research_pengxin_feng_2015]
- [Penland and Romeo 1971][research_penland_romeo_1971]
- [Penland and Romeo 1971][research_penland_romeo_1971_b]
- [Penn and Lindley 1997][research_penn_lindley_1997]
- [Perepelkina and Fedotov 2023][research_perepelkina_fedotov_2023]
- [Perkasa et al 2024][research_perkasa_krisbudiman_2024]
- [Perkins and Tannas 1967][research_perkins_tannasjr_1967]
- [Perminov 1969][research_perminov_1969]
- [Perry and Schneider 1984][research_perry_schneider_1984]
- [Peshekhonov 2020][research_peshekhonov_2020]
- [Pessanha Santos et al 2023][research_pessanhasantos_lobo_2023]
- [Peter and Umap 2021][research_peter_umap_2021]
- [Petersen 1981][research_petersen_1981]
- [Petley et al 1984][research_petley_smith_1984]
- [Petrishchev 2018][research_petrishchev_2018]
- [Petrović et al 2018][research_petrovic_maneski_2018]
- [Pettersson and Rizzi 2006][research_pettersson_rizzi_2006]
- [Pezzella and Viviani 2024][research_pezzella_viviani_2024]
- [Peña-Gamboa and Martinez-Torres 2026][research_penagamboa_martineztorres_2026]
- [Pfaff 1968][research_pfaff_1968]
- [Phatak and Lee 1985][research_phatak_1985]
- [Phillips 2008][research_phillips_2008]
- [Phillips and Kryvoruka 1973][research_phillips_kryvoruka_1973]
- [Phillips et al 1973][research_phillips_1973]
- [Phillips et al 1983][research_phillips_wilson_1983]
- [Pi 1988][research_pi_1988]
- [Piacquadio et al 2023][research_piacquadio_pridohl_2023]
- [Pienkowski et al 2003][research_pienkowski_whitmore_2003]
- [Pieper et al 2018][research_pieper_perry_2018]
- [Piet-Lahanier and Serre 2017][research_pietlahanier_serre_2017]
- [Pilyugin et al 1994][research_pilyugin_talipov_1994]
- [Pines and Hueschen 1978][research_pines_hueschen_1978]
- [Pipenberg et al 2019][research_pipenberg_keennon_2019]
- [Pirooz et al 2021][research_pirooz_mirmahdi_2021]
- [Pittman and Dillon 1977][research_pittman_dillon_1977]
- [Pitts and Kourtides 1989][research_pitts_kourtides_1989]
- [Platou 1968][research_platou_1968]
- [Platus 1967][research_platus_1967]
- [Platus 1978][research_platus_1978]
- [Platus 1979][research_platus_1979]
- [Platus 1980][research_platus_1980]
- [Platus 1983][research_platus_1983]
- [Plinge 2003][research_plinge_2003]
- [Plumb 1971][research_plumb_1971]
- [Podruzhin and Zagidulin 2017][research_podruzhin_zagidulin_2017]
- [Pogorelov 2008][research_pogorelov_2008]
- [Pogorelov 2009][research_pogorelov_2009]
- [Pogosyan and Vereikin 2020][research_pogosyan_vereikin_2020]
- [Pohly et al 2018][research_pohly_kang_2018]
- [Pollack and Urch 1991][research_pollack_urch_1991]
- [Polsgrove et al 2018][research_polsgrove_2018]
- [Polsgrove et al 2018][research_polsgrove_2018_b]
- [Ponton and Warnes 2007][research_ponton_warnes_2007]
- [Poritzky 1970][research_poritzky_1970]
- [Post and Dagli 2004][research_post_dagli_2004]
- [Poteet and Blosser 2004][research_poteet_blosser_2004]
- [Poteet et al 2004][research_poteet_abukhajeel_2004]
- [Poth et al 1993][research_pothjr_fisher_1993]
- [Pouly et al 2009][research_pouly_lauffenburger_2009]
- [Pouya and Saghafi 2009][research_pouya_saghafi_2009]
- [Powell 1959][research_powell_1959]
- [Powell 1960][research_powell_1960]
- [Powell and Cruz 1991][research_powell_1991]
- [Powers 1984][research_powers_1984]
- [Powers 1986][research_powers_1986]
- [Prachand et al 2025][research_prachand_rakshith_2025]
- [Pragadheswaran and Balguri 2015][research_pragadheswaran_balguri_2015]
- [Prahl 1968][research_prahl_1968]
- [Prakash and Zhong 2008][research_prakash_zhong_2008]
- [Prakash and Zhong 2009][research_prakash_zhong_2009]
- [Prasad 2022][research_prasad_2022]
- [Prasad et al 2018][research_prasad_comandur_2018]
- [Pravitra and Johnson 2024][research_pravitra_johnson_2024]
- [Preliminary subsystem designs for 1990][research_preliminary_subsystem_1990]
- [Preliminary subsystem designs for 1990][research_preliminary_subsystem_1990_b]
- [Preliminary Subsystem Designs for 1990][research_preliminary_subsystem_1990_c]
- [Prilliman and Slingerland 1966][research_prilliman_1966]
- [Primich and Steinberg 1963][research_primich_1963]
- [Prislin][research_prislin_nd]
- [Prislin and Wilson 1967][research_prislin_1967]
- [Pritchard 2001][research_pritchard_2001]
- [Pruin 1970][research_pruin_1970]
- [Pu et al 2021][research_pu_xiaodong_2021]
- [Pu et al 2024][research_pu_wang_2024]
- [Purcell et al 2025][research_purcell_wicklund_2025]
- [Pusztai et al 2024][research_pusztai_lowenberg_2024]
- [Putman 1969][research_putman_1969]
- [Putnam and Gardner][research_putnam_nd]
- [Putov et al 2015][research_putov_putov_2015]
- [Putov et al 2016][research_putov_putov_2016]
- [Pyle 1971][research_pyle_1971]
- [Pyle and Ash 1970][research_pyle_1970]
- [Pyle and Saltzman 1973][research_pyle_1973]
- [Pytka 2023][research_pytka_2023]
- [Pérez et al 2022][research_perez_theodoulis_2022]
- [Pérez Rus and Le Gal 2024][research_perezrus_legal_2024]
- [Qayyum et al 2017][research_qayyum_bhatti_2017]
- [Qi et al 2018][research_qi_zhao_2018]
- [Qi et al 2021][research_qi_li_2021]
- [Qi et al 2025][research_qi_zhao_2025]
- [Qi et al 2026][research_qi_liu_2026]
- [Qian and Wang 2022][research_qian_wang_2022]
- [Qian and Zhai 2012][research_qian_zhai_2012]
- [Qian et al 2012][research_qian_jiang_2012]
- [Qian et al 2014][research_qian_qi_2014]
- [Qian et al 2015][research_qian_wang_2015]
- [Qin Changmao et al 2010][research_qinchangmao_qinaiming_2010]
- [Qin et al 2023][research_qin_fu_2023]
- [Qiu et al 2019][research_qiu_sang_2019]
- [Qu et al 2023][research_qu_zhang_2023]
- [Quast et al 1990][research_quast_henke_1990]
- [Quinn 1963][research_quinn_1963]
- [Rabinskiy and Tushavina 2019][research_rabinskiy_tushavina_2019]
- [Radforth 1987][research_radforth_1987]
- [Radhakrishnan et al 2023][research_radhakrishnan_hari_2023]
- [Radhakrishnan et al 2024][research_radhakrishnan_hari_2024]
- [Rafatnia et al 2019][research_rafatnia_nourmohammadi_2019]
- [Ragheb et al 2013][research_ragheb_dantsker_2013]
- [Rainey and Igoe 1958][research_rainey_1958]
- [Raja 2011][research_raja_2011]
- [Rajawana and Smithmaitrie 2020][research_rajawana_smithmaitrie_2020]
- [Rajesh and Bt 2015][research_a_bt_2015]
- [Rajesh Yadav et al 2016][research_rajeshyadav_mohammadfaisal_2016]
- [Raju Kulkarni et al 2019][research_rajukulkarni_larocca_2019]
- [Raju Kulkarni et al 2019][research_rajukulkarni_varriale_2019]
- [Raju Kulkarni et al 2022][research_rajukulkarni_larocca_2022]
- [Rakow and Waas 2005][research_rakow_waas_2005]
- [Ralph 1999][research_ralph_1999]
- [Raman et al 2000][research_raman_anderson_2000]
- [Ramasamy 2015][research_ramasamy_2015]
- [Ramirez et al 2025][research_ramirez_dux_2025]
- [Rammon and Nirbito 2019][research_rammon_nirbito_2019]
- [Rana and Chudoba 2016][research_rana_chudoba_2016]
- [Randolph et al 2015][research_randolph_mullenax_2015]
- [Raney 1987][research_raney_1987]
- [Raney and Batterson 1989][research_raney_1989]
- [Rang et al 1979][research_rang_gutmann_1979]
- [Rao et al 2001][research_rao_sarma_2001]
- [Rao et al 2012][research_rao_uhlig_2012]
- [Rao et al 2022][research_rao_zhang_2022]
- [Raquet and Amt 2008][research_raquet_amt_2008]
- [Rashmi Koushik et al 2020][research_rashmikoushiketal_2020]
- [Rasky 1995][research_rasky_1995]
- [Rasky et al 2001][research_rasky_milos_2001]
- [Rasky et al 2006][research_rasky_pittman_2006]
- [Rasmussen 1979][research_rasmussen_1979]
- [Rataczak et al 2024][research_rataczak_boyd_2024]
- [Ravichandran et al 2023][research_ravichandran_ahmed_2023]
- [Raymer 2001][research_raymer_2001]
- [Recker et al 2018][research_recker_gribble_2018]
- [Rector and Hattendorf 1967][research_rector_hattendorf_1967]
- [Redd et al 1979][research_redd_1979]
- [Redding 1984][research_redding_jr_1984]
- [Rediess and Melton 1994][research_rediess_1994]
- [Redlich 1971][research_redlich_1971]
- [Redondo Gutierrez et al 2022][research_redondogutierrez_seelbinder_2022]
- [Reed 1966][research_reed_1966]
- [Reed et al 1997][research_reed_1997]
- [Reed-Mohn 2000][research_reedmohn_2000]
- [Reich et al 2015][research_reich_willits_2015]
- [Reiley et al 1991][research_reiley_1991]
- [Reimann 2016][research_reimann_2016]
- [Reiser et al 2024][research_reiser_villani_2024]
- [Ren et al 2011][research_ren_cai_2011]
- [Ren et al 2017][research_ren_fu_2017]
- [Ren et al 2018][research_ren_wang_2018]
- [Ren et al 2020][research_ren_zi_2020]
- [Ren et al 2023][research_ren_wang_2023]
- [Ren et al 2025][research_ren_ma_2025]
- [Ren et al 2025][research_ren_wang_2025]
- [Rey 2000][research_rey_2000]
- [Reyhanoglu and Alvarado 2013][research_reyhanoglu_alvarado_2013]
- [Reynerson 2006][research_reynerson_2006]
- [Rezaifard and Abbasi 2017][research_rezaifard_abbasi_2017]
- [Ribarich 1967][research_ribarich_1967]
- [Ricciardi and Minwalla 2016][research_ricciardi_minwalla_2016]
- [Ricciardi et al 2016][research_ricciardi_2016]
- [Ricciardi et al 2020][research_ricciardi_maddock_2020]
- [Rice 1946][research_rice_1946]
- [Rice and Hazlwood 1994][research_rice_hazlwood_1994]
- [Rice and Locksley 2000][research_rice_locksley_2000]
- [Richards and Erickson 2019][research_richards_erickson_2019]
- [Richards and Tate 2023][research_richards_tate_2023]
- [Richardson 1976][research_richardson_1976]
- [Richeson and Pines 2007][research_richeson_pines_2007]
- [Richmond 2022][research_richmond_2022]
- [Ridha 1968][research_ridha_1968]
- [Rigali et al 1980][research_rigali_sterk_1980]
- [Rigatos 2012][research_rigatos_2012]
- [Rigatos et al 2023][research_rigatos_abbaszadeh_2023]
- [Rimani et al 2022][research_rimani_viola_2022]
- [Rimer and Sperling 1965][research_rimer_sperling_1965]
- [Rimer and Sperling 1966][research_rimer_sperling_1966]
- [Rimmer 1952][research_rimmer_1952]
- [Ringel et al 2022][research_ringel_panerai_2022]
- [Rithirun and Sooraksa 2013][research_rithirun_sooraksa_2013]
- [Ritter et al 2016][research_ritter_neumann_2016]
- [Rivera et al 2025][research_rivera_hein_2025]
- [Rivers 1968][research_rivers_1968]
- [Rivers et al 1991][research_rivers_1991]
- [Rizvi et al 2013][research_rizvi_he_2013]
- [Robaglia et al 2018][research_robaglia_libine_2018]
- [Roberts 1988][research_roberts_1988]
- [Roberts 1990][research_roberts_1990]
- [Roberts 2024][research_roberts_2024]
- [Roberts and Bhanu 1992][research_roberts_bhanu_1992]
- [Robertson 2017][research_robertson_2017]
- [Robertson and Hartfield 1992][research_robertson_1992]
- [Robinson et al 1995][research_robinson_nolen_1995]
- [Robinson et al 2025][research_robinson_ouhabi_2025]
- [Rocha et al 2025][research_rocha_bauzermedeiros_2025]
- [Rochelle et al 1972][research_rochelle_roberts_1972]
- [Rodi and Bennett 2012][research_rodi_bennett_2012]
- [Rodriguez et al 2005][research_rodriguez_2005]
- [Roenneke and Cornwell 1992][research_roenneke_cornwell_1992]
- [Roenneke and Well 1995][research_roenneke_well_1995]
- [Roenneke and Well 1996][research_roenneke_well_1996]
- [Roepke 1972][research_roepke_1972]
- [Roessler 1967][research_roessler_1967]
- [Rogers 1973][research_rogers_1973]
- [Rogers and Dragone 1996][research_rogers_dragone_1996]
- [Rogers and Walter K 1955][research_rogers_walterk_1955]
- [Rogers and Walter K. 1953][research_rogers_1953]
- [Rogers et al 2004][research_rogers_safie_2004]
- [Rogers et al 2022][research_rogers_schroeder_2022]
- [Romano et al 2024][research_romano_cecchetti_2024]
- [Romanov et al 2017][research_romanov_burke_2017]
- [Romere et al 1978][research_romere_eichblatt_1978]
- [Romere et al 1979][research_romere_eichblatt_1979]
- [Romero and Bledsoe 2015][research_romero_bledsoe_2015]
- [Rona and Soueid 2010][research_rona_soueid_2010]
- [Rooney 2003][research_rooney_2003]
- [Rooney et al 1977][research_rooney_craig_1977]
- [Rosenthal 1982][research_rosenthal_1982]
- [Roshanian and Talebi 2008][research_roshanian_talebi_2008]
- [Roshini and Subba Reddy 2023][research_roshini_subbareddy_2023]
- [Rosner et al 2018][research_rosner_peszor_2018]
- [Rossman and Braun 2017][research_rossman_braun_2017]
- [Rougeux et al 2009][research_rougeux_malomolina_2009]
- [Rouwhorst 2001][research_rouwhorst_2001]
- [Roux et al 2012][research_roux_mantini_2012]
- [Roxburgh 2015][research_roxburgh_2015]
- [Rubenstein and Carter 2000][research_rubenstein_carter_2000]
- [Rubtsova A.S. 2022][research_study_of_2022]
- [Rudnik and Germain 2009][research_rudnik_germain_2009]
- [Ruf et al 1996][research_ruf_1996]
- [Rufolo et al 2024][research_rufolo_destefanofumo_2024]
- [Ruiz Garcia et al 2022][research_ruizgarcia_brown_2022]
- [Runkle and Drobnik 1979][research_runkle_drobnik_1979]
- [Ruping et al 2021][research_ruping_xin_2021]
- [Ruppe 1985][research_ruppe_1985]
- [Rusbarsky 1990][research_rusbarsky_1990]
- [Russo et al 2026][research_russo_voto_2026]
- [Rutishauser et al 2019][research_rutishauser_moore_2019]
- [Rutishauser et al 2022][research_rutishauser_mendeck_2022]
- [Ruxton-davies and Powell 1970][research_truxtondavies_powell_1970]
- [Ryan Aeronautical Co San Diego Ca 1963][research_ca_1963]
- [S. Hameed and G. R 2021][research_shameed_gr_2021]
- [Sabatini 2014][research_sabatini_2014]
- [Sabatini et al 2013][research_sabatini_rodriguez_2013]
- [Sabiron et al 2013][research_sabiron_chavent_2013]
- [Sachan and Padhi 2016][research_sachan_padhi_2016]
- [Sachs and Moeller 1995][research_sachs_moeller_1995]
- [Sadovnitchii et al 1997][research_sadovnitchii_ryabkov_1997]
- [Sadovnychiy et al 1998][research_sadovnychiy_betin_1998]
- [Sadovnychiy et al 1999][research_sadovnychiy_betin_1999]
- [Sadovnychiy et al 2001][research_sadovnychiy_ryzhenko_2001]
- [Sadraey 2011][research_sadraey_2011]
- [Saff and Rosenfeld 1982][research_saff_rosenfeld_1982]
- [Saghafi and Esmailifar 2009][research_saghafi_esmailifar_2009]
- [Sagirov et al 2025][research_sagirov_solovyov_2025]
- [Sahasrabudhe et al 2011][research_sahasrabudhe_pritchard_2011]
- [Sahawneh et al 2010][research_sahawneh_aljarrah_2010]
- [Sahu 2005][research_sahu_2005]
- [Sai Naga Bharghava et al 2024][research_sainagabharghava_krishnatmali_2024]
- [Saiki et al 2009][research_saiki_fukao_2009]
- [Salgueiro Filipe et al 2009][research_salgueirofilipe_deweerdt_2009]
- [Salt 1995][research_salt_1995]
- [Salt 2015][research_salt_2015]
- [Saltzman et al 1999][research_saltzman_1999]
- [Saltzman et al 2002][research_saltzman_2002]
- [Saltzman et al 2007][research_saltzman_2007]
- [Samardžić et al 2013][research_samardzic_isakovic_2013]
- [Samotokhin 2021][research_samotokhin_2021]
- [Sanders 1972][research_sanders_1972]
- [Sanderson 1965][research_sanderson_1965]
- [Sani and Karimian 2017][research_sani_karimian_2017]
- [Sankar 2012][research_sankar_2012]
- [Sansica and Hashimoto 2023][research_sansica_hashimoto_2023]
- [Sanson et al 2017][research_sanson_villedieu_2017]
- [Santong Zhang and Shiwu Yang 2008][research_santongzhang_shiwuyang_2008]
- [Santos 2009][research_santos_2009]
- [Santos 2011][research_santos_2011]
- [Santos et al 2019][research_santos_lobo_2019]
- [Sanuki 1965][research_sanuki_1965]
- [Saputra 2017][research_saputra_2017]
- [Sarigul-Klijn et al 2005][research_sarigulklijn_sarigulklijn_2005]
- [Sarigul-Klijn et al 2008][research_sarigulklijn_sarigulklijn_2008]
- [Saripalli 2009][research_saripalli_2009]
- [Saripalli et al 2003][research_saripalli_montgomery_2003]
- [Sarkar et al 2021][research_sarkar_amrr_2021]
- [Sarrafian 1984][research_sarrafian_1984]
- [Sasa et al 1991][research_sasa_takizawa_1991]
- [Satkunanathan and Murphy 1998][research_satkunanathan_murphy_1998]
- [Sato and Muraoka 2013][research_sato_muraoka_2013]
- [Saunders 1996][research_saunders_1996]
- [Savino et al 2009][research_savino_viviani_2009]
- [Savkin et al 2021][research_savkin_antonov_2021]
- [Sawyer 1984][research_sawyer_1984]
- [Sawyer and Bush 1998][research_sawyer_bush_1998]
- [Sawyer et al 1997][research_sawyer_bush_1997]
- [Sawyer et al 1999][research_sawyer_hodge_1999]
- [Sayadi et al 2018][research_sayadi_kosari_2018]
- [Scanlon 1987][research_scanlon_1987]
- [Scarlatella et al 2024][research_scarlatella_guadagnini_2024]
- [Schaeffer 1983][research_schaeffer_1983]
- [Schang 2024][research_schang_2024]
- [Scherberg and Rhode 1927][research_scherberg_1927]
- [Schermerhorn 1969][research_schermerhorn_1969]
- [Schermerhorn 1969][research_schermerhorn_1969_b]
- [Scherzinger and Blake Reid 1989][research_scherzinger_blakereid_1989]
- [Schiavazzi and Juliano 2020][research_schiavazzi_juliano_2020]
- [Schiavone et al 2012][research_schiavone_2012]
- [Schierman et al 2001][research_schierman_ward_2001]
- [Schierman et al 2001][research_schierman_ward_2001_b]
- [Schierman et al 2004][research_schierman_gandhi_2004]
- [Schierman et al 2004][research_schierman_ward_2004]
- [Schifferle et al 1999][research_schifferle_deppe_1999]
- [Schmidt 1985][research_schmidt_1985]
- [Schmidt 2011][research_schmidt_2011]
- [Schmidt and Mann 1996][research_schmidt_mann_1996]
- [Schmitt and Burchett 2004][research_schmitt_burchett_2004]
- [Schneider et al 2005][research_schneider_searcy_2005]
- [Schneider et al 2012][research_schneider_larson_2012]
- [Scholz et al 2026][research_scholz_theuser_2026]
- [Schonberg and Squire 2024][research_schonberg_squire_2024]
- [Schonberg and Squire 2024][research_schonberg_squire_2024_b]
- [Schonberg et al 2025][research_schonberg_squire_2025]
- [Schouler et al 2021][research_schouler_prevereaud_2021]
- [Schrader 2023][research_schrader_2023]
- [Schrauf and Schröder 1999][research_schrauf_schroder_1999]
- [Schroer 2003][research_schroer_2003]
- [Schumann et al 2009][research_schumann_liu_2009]
- [Schumann et al 2011][research_schumann_mbaya_2011]
- [Schwabacher et al 2002][research_schwabacher_2002]
- [Schwartz 1983][research_schwartz_1983]
- [Schwarz 1981][research_schwarz_1981]
- [Schwelkart and Hallion 1997][research_schwelkart_hallion_1997]
- [Schänzer 1993][research_schanzer_1993]
- [Sciegienny et al 1978][research_sciegienny_nurse_1978]
- [Scorsoglio et al 2022][research_scorsoglio_2022]
- [Scorsoglio et al 2025][research_scorsoglio_gaudet_2025]
- [Scoville and Rajula 2005][research_scoville_rajula_2005]
- [Seanor][research_seanor_nd]
- [Sedlmair et al 2019][research_sedlmair_theis_2019]
- [Sedlmair et al 2022][research_sedlmair_theis_2022]
- [Sefic and Cutler 1986][research_sefic_cutler_1986]
- [Seiff 1954][research_seiff_1954]
- [Seiff et al 1952][research_seiff_1952]
- [Seiler et al 2012][research_seiler_bastide_2012]
- [Selezneva et al 2022][research_selezneva_neusypin_2022]
- [Sellers 2000][research_sellers_2000]
- [Sen 1990][research_sen_1990]
- [Sen 1990][research_sen_1990_b]
- [Senkans et al 2021][research_senkans_kish_2021]
- [Senpheng and Ruchanurucks 2015][research_senpheng_ruchanurucks_2015]
- [Sepka and Samareh 2015][research_sepka_samareh_2015]
- [Serrano 2006][research_serrano_2006]
- [Setterfield et al 2021][research_setterfield_hewitt_2021]
- [Setterfield et al 2022][research_setterfield_hewitt_2022]
- [Sexton 2003][research_sexton_2003]
- [Sforza 2014][research_sforza_2014]
- [Sforza 2016][research_sforza_2016]
- [Sforza 2020][research_sforza_2020]
- [Sforza and Anderson 2003][research_sforza_2003]
- [Sha et al 2026][research_sha_li_2026]
- [Shafa et al 2011][research_shafa_cunio_2011]
- [Shah et al 1972][research_shah_gevaert_1972]
- [Shahrbabaki et al 2014][research_shahrbabaki_bazazzadeh_2014]
- [Shahzad and Weiduo 2019][research_shahzad_weiduo_2019]
- [Shaiju and Sreeja 2022][research_shaiju_sreeja_2022]
- [Shakarian 1983][research_shakarian_1983]
- [Shakernia et al 1999][research_shakernia_ma_1999]
- [Shakoori et al 2012][research_shakoori_mortazavi_2012]
- [Shakoori et al 2017][research_shakoori_betin_2017]
- [Shalaby 2018][research_shalaby_2018]
- [Shamaghdari et al 2014][research_shamaghdari_nikravesh_2014]
- [Shan et al 2015][research_shan_huifeng_2015]
- [Shang et al 2022][research_shang_li_2022]
- [Shao and Wang 2015][research_shao_wang_2015]
- [Shao and Wang 2016][research_shao_wang_2016]
- [Shao et al 2015][research_shao_wang_2015_b]
- [Shao et al 2016][research_shao_deyang_2016]
- [Shao et al 2017][research_shao_wu_2017]
- [Shao et al 2018][research_shao_gu_2018]
- [Shao et al 2020][research_shao_yang_2020]
- [Shao et al 2025][research_shao_zhao_2025]
- [Sharf and Monterrubio 1999][research_sharf_monterrubio_1999]
- [Sharma and Hablani 2014][research_sharma_hablani_2014]
- [Sharma et al 2008][research_sharma_gogu_2008]
- [Sharma et al 2011][research_sharma_vidal_2011]
- [Sharma et al 2024][research_sharma_giangaspero_2024]
- [Shaw and Richter 1985][research_shaw_richter_1985]
- [Shaw et al 1997][research_shaw_taylor_1997]
- [Shawyer 2023][research_shawyer_2023]
- [Shea et al 2023][research_shea_chan_2023]
- [Sheard et al 2008][research_sheard_scaysbrook_2008]
- [Sheldon 1967][research_sheldon_1967]
- [Shen 2021][research_shen_2021]
- [Shen 2021][research_shen_2021_b]
- [Shen and Chen 2025][research_shen_chen_2025]
- [Shen et al 2016][research_shen_sheng_2016]
- [Shen et al 2019][research_shen_li_2019]
- [Shen et al 2023][research_shen_xia_2023]
- [Shen et al 2025][research_shen_zhang_2025]
- [Sheng et al 2010][research_sheng_mian_2010]
- [Sheng et al 2015][research_sheng_geng_2015]
- [ShengZe Chen et al 2014][research_shengzechen_xuanzhang_2014]
- [Shenming et al 2017][research_shenming_tao_2017]
- [Shenming et al 2018][research_shenming_tao_2018]
- [Shepheard 1965][research_shepheard_1965]
- [Shepperd and Staugler 1999][research_shepperd_staugler_1999]
- [Shepperd et al 2000][research_shepperd_lentsch_2000]
- [Sherman 1978][research_sherman_1978]
- [Sherry et al 2018][research_sherry_shortle_2018]
- [Shi et al 2009][research_shi_tang_2009]
- [Shi et al 2016][research_shi_tanigawa_2016]
- [Shi et al 2025][research_shi_li_2025]
- [Shi et al 2025][research_shi_li_2025_b]
- [Shi et al 2026][research_shi_li_2026]
- [Shi Linan et al 2014][research_shilinan_lihuifeng_2014]
- [Shideler et al 1985][research_shideler_webb_1985]
- [Shields 1981][research_shields_1981]
- [Shields and Mohseni 2011][research_shields_mohseni_2011]
- [Shiji and Kulik 2026][research_shiji_kulik_2026]
- [Shim et al 2023][research_shim_park_2023]
- [Shimada and Ohwada 2020][research_shimada_ohwada_2020]
- [Shimizu and Murata 2008][research_shimizu_murata_2008]
- [Shin and Kim 2013][research_shin_kim_2013]
- [Shinbrot 2019][research_shinbrot_2019]
- [Shinnick 1966][research_shinnick_1966]
- [Shou et al 2021][research_shou_xu_2021]
- [Shrotri and Schrage 2009][research_shrotri_schrage_2009]
- [Shrotri and Schrage 2009][research_shrotri_schrage_2009_b]
- [Shtessel et al 1997][research_shtessel_tournes_1997]
- [Shtessel et al 2000][research_shtessel_hall_2000]
- [Shtessel et al 2002][research_shtessel_zhu_2002]
- [Shuai et al 2022][research_shuai_daqian_2022]
- [Shuang and Liu 2009][research_shuang_liu_2009]
- [Shuang and Pingyuan 2006][research_shuang_pingyuan_2006]
- [Shuang and Pingyuan 2008][research_shuang_2008]
- [Shuang et al 2005][research_shuang_hutao_2005]
- [Shue and Agarwal 1999][research_shue_agarwal_1999]
- [Shufeldt 1961][research_shufeldt_1961]
- [Shuhua Zhu et al 2008][research_shuhuazhu_mingbotong_2008]
- [Shukla 2024][research_shukla_2024]
- [Shulga and Shcheglov 2021][research_shulga_shcheglov_2021]
- [Shuping Tan and Zhibin Li 2010][research_shupingtan_zhibinli_2010]
- [Shuttle autoland support program 1976][research_shuttle_autoland_1976]
- [Shweyk et al 2012][research_shweyk_hyde_2012]
- [Si et al 2024][research_si_zhao_2024]
- [Siboro et al 2023][research_siboro_zainul_2023]
- [Sickle 2023][research_sickle_2023]
- [Sillen 1993][research_sillen_1993]
- [Silsby 1956][research_silsby_1956]
- [Silsby and Harrin 1955][research_silsby_1955]
- [Silsby et al 1953][research_silsby_1953]
- [Silva and Augusto Aparecido Gomes 2021][research_silva_augustoaparecidogomes_2021]
- [Silva et al 2009][research_silva_gamarra_2009]
- [Silva et al 2014][research_silva_mendonca_2014]
- [Silva et al 2019][research_silva_fontes_2019]
- [Silvestre 2013][research_silvestre_2013]
- [Sim 1973][research_sim_1973]
- [Sim 1973][research_sim_1973_b]
- [Sim et al 1994][research_sim_murray_1994]
- [Simeonides 2006][research_simeonides_2006]
- [Simmons and Ackerman 2026][research_simmons_ackerman_2026]
- [Simmons et al][research_simmons_nd]
- [Simmons et al 2025][research_simmons_ackerman_2025]
- [Simons 1975][research_simons_1975]
- [Simons 1976][research_simons_1976]
- [Simplício et al 2018][research_simplicio_navarrotapia_2018]
- [Simplício et al 2020][research_simplicio_marcos_2020]
- [Simpson 1972][research_simpson_1972]
- [Sims and Carter 1981][research_sims_carter_1981]
- [Sims and Hahn 1964][research_sims_hahn_1964]
- [Simulation in support of 1988][research_simulation_support_1988]
- [Singh 2023][research_singh_2023]
- [Singh et al 1989][research_singh_tiwari_1989]
- [Singh et al 2021][research_singh_chaudhary_2021]
- [Singh et al 2022][research_singh_menghal_2022]
- [Singleton and Yeager 1998][research_singleton_1998]
- [Sipe and Hinde 2008][research_sipe_hinde_2008]
- [Sippel and Pohl 1996][research_sippel_pohl_1996]
- [Sippel and Sippel 1997][research_sippel_sippel_1997]
- [Sithara and Shenil 2022][research_sithara_shenil_2022]
- [Sivakumar and Syedhaleem 2018][research_sivakumar_syedhaleem_2018]
- [Sivalingam and Hagen 2026][research_sivalingam_hagen_2026]
- [Sivan and Murmu 2017][research_sivan_murmu_2017]
- [Sivan and Pandian 2018][research_sivan_pandian_2018]
- [Sivells 1969][research_sivells_1969]
- [Sivolella 2014][research_sivolella_2014]
- [Siwen et al 2022][research_siwen_feng_2022]
- [Skariya et al 2014][research_skariya_sebastian_2014]
- [Skolnik and Putnam 2020][research_skolnik_putnam_2020]
- [Slater 1956][research_slater_1956]
- [Slayton 1977][research_slayton_1977]
- [Slegers et al 2007][research_slegers_beyer_2007]
- [Slivinsky et al 1995][research_slivinsky_breitling_1995]
- [Smitchens and Huber 1975][research_smitchens_huber_1975]
- [Smith][research_smith_nd]
- [Smith 1965][research_smith_1965]
- [Smith 1981][research_smith_1981]
- [Smith 2003][research_smith_2003]
- [Smith 2011][research_smith_2011]
- [Smith and Biezad 1986][research_smithjr_biezad_1986]
- [Smith and Dutta 2017][research_smith_2017]
- [Smith and Meyer 1981][research_smith_meyer_1981]
- [Smith and Peng 1996][research_smith_1996]
- [Smith et al 1974][research_smith_1974]
- [Smith et al 1994][research_smith_purvis_1994]
- [Smith et al 1996][research_smith_1996_b]
- [Smith et al 1998][research_smith_amitay_1998]
- [Smith et al 2018][research_smith_2018]
- [Smotrova 2002][research_smotrova_2002]
- [Snapp and Rodriguez 2011][research_snapp_rodriguez_2011]
- [Snyder et al 1992][research_snyder_schipper_1992]
- [Sobron et al 2021][research_sobron_lundstrom_2021]
- [Soencksen and Whyte 1999][research_soencksen_whyte_1999]
- [Sohier et al 2014][research_sohier_farges_2014]
- [Sohier et al 2014][research_sohier_farges_2014_b]
- [Sohier et al 2015][research_sohier_pietlahanier_2015]
- [Soistmann and Spain 1993][research_soistmann_1993]
- [Sokolov et al 2022][research_sokolov_sukhanov_2022]
- [Solntsev 2014][research_solntsev_2014]
- [Soloviev and Yang 2016][research_soloviev_yang_2016]
- [Sommer 1960][research_sommer_1960]
- [Son et al 2023][research_son_oh_2023]
- [Song and Wang 2025][research_song_wang_2025]
- [Song et al 2005][research_song_liao_2005]
- [Song et al 2013][research_song_cai_2013]
- [Song et al 2019][research_song_zhang_2019]
- [Song et al 2020][research_song_ai_2020]
- [Song et al 2020][research_song_liu_2020]
- [Song et al 2023][research_song_wang_2023]
- [Song et al 2023][research_song_wang_2023_b]
- [Song et al 2023][research_song_zhang_2023]
- [Song et al 2024][research_song_zhang_2024]
- [Song et al 2026][research_song_shi_2026]
- [Songhui et al 2020][research_songhui_chufeng_2020]
- [Sonowal et al 2021][research_sonowal_pandey_2021]
- [Sorensen and Karmarkar 1977][research_sorensen_1977]
- [Sostaric et al 2017][research_sostaric_cerimele_2017]
- [Sotirios and Jackson 2008][research_sotirios_2008]
- [Space Shuttle Program Orbiter 1977][research_space_shuttle_1977]
- [Spahr 1974][research_spahr_1974]
- [Spearman 1984][research_spearman_1984]
- [Spearman 1985][research_spearman_1985]
- [Spearman and Torres 1994][research_spearman_1994]
- [Spencer and Fournier 1973][research_spencer_1973]
- [Spidaliere et al 2004][research_spidaliere_zipay_2004]
- [Sponable et al 2004][research_sponable_morse_2004]
- [Spravka and Jorris 2015][research_spravka_jorris_2015]
- [Spravka and Jorris 2015][research_spravka_jorris_2015_b]
- [Spreiter and Steffen 1946][research_spreiter_steffen_1946]
- [Springer 1996][research_springer_1996]
- [Spurlin and Lueck 1984][research_spurlin_lueck_1984]
- [Squires 2004][research_squires_2004]
- [Sreeletha et al 2019][research_sreeletha_noble_2019]
- [Sreena and Thomas 2017][research_pv_thomas_2017]
- [Sruthi S et al 2015][research_sruthis_sumathyr_2015]
- [Staas and Philip C 1963][research_staas_philipc_1963]
- [Stachiw et al 2020][research_stachiw_khouli_2020]
- [Stadler 1993][research_stadler_1993]
- [Stadler 1998][research_stadler_1998]
- [Stalnov et al 2013][research_stalnov_angland_2013]
- [Staniszewski 1999][research_staniszewski_1999]
- [Stapleton et al 1997][research_stapleton_galati_1997]
- [Starkey and Lewis 2000][research_starkey_lewis_2000]
- [Starkey et al 2012][research_starkey_argrow_2012]
- [Starkey et al 2026][research_starkey_sequeira_2026]
- [Starr et al 1962][research_starr_1962]
- [Staylor 1970][research_staylor_1970]
- [Steer 2004][research_steer_2004]
- [Stein 2005][research_stein_2005]
- [Steinberg 1992][research_steinberg_1992]
- [Steiner and Brady 2014][research_steiner_brady_2014]
- [Steinfeldt et al 2008][research_steinfeldt_grant_2008]
- [Stephan 2025][research_stephan_2025]
- [Stephens 1959][research_stephens_1959]
- [Stern 2004][research_stern_2004]
- [Stern 2008][research_stern_2008]
- [Stern and Chu 1963][research_stern_chu_1963]
- [Stetson and Lewis 1977][research_stetson_lewis_1977]
- [Stevens 1985][research_stevens_1985]
- [Stevens et al 1966][research_stevens_1966]
- [Stewart et al 1986][research_stewart_leiser_1986]
- [Stich 2012][research_stich_2012]
- [Stickle 1961][research_stickle_1961]
- [Stickle and Silsby 1960][research_stickle_1960]
- [Stiles 2022][research_stiles_2022]
- [Stilley 1988][research_stilley_1988]
- [Stolle et al 2015][research_stolle_bolting_2015]
- [Stollery and Murthy 1978][research_stollery_murthy_1978]
- [Stottier 1995][research_stottier_1995]
- [Stout 1946][research_stout_1946]
- [Stout 1971][research_stout_1971]
- [Stower 2024][research_stower_2024]
- [Straub and Johnston 1987][research_straub_1987]
- [Straub et al 1984][research_straub_johnston_1984]
- [Strauss 1967][research_strauss_1967]
- [Streb 1972][research_strebjr_1972]
- [Strelets et al 2023][research_strelets_tarasov_2023]
- [Strouhal and Curry 1966][research_strouhal_curry_1966]
- [Strutz 1972][research_strutz_1972]
- [Study of the influence 1967][research_study_influence_1967]
- [Stuessy et al 1997][research_stuessy_peeples_1997]
- [Stuper 1934][research_stuper_1934]
- [Su and Kiang 2022][research_su_kiang_2022]
- [Su and Liu 2025][research_su_liu_2025]
- [Su and Liu 2025][research_su_liu_2025_b]
- [Su and Wang 2015][research_su_wang_2015]
- [Su et al 2013][research_su_yu_2013]
- [Su et al 2021][research_su_dai_2021]
- [Su et al 2021][research_su_dai_2021_b]
- [Su et al 2025][research_su_hong_2025]
- [Subrahmanyam 1994][research_subrahmanyam_1994]
- [Subrahmanyam 1995][research_subrahmanyam_1995]
- [Subrata 2017][research_subrata_2017]
- [Suit et al 1964][research_suit_1964]
- [Sukenik 2004][research_sukenik_2004]
- [Sun 2026][research_sun_2026]
- [Sun and Tang 2011][research_sun_tang_2011]
- [Sun and Zhao 2024][research_sun_zhao_2024]
- [Sun et al 2015][research_sun_yang_2015]
- [Sun et al 2020][research_sun_shi_2020]
- [Sun et al 2022][research_sun_chen_2022]
- [Sun et al 2023][research_sun_wu_2023]
- [Sun et al 2023][research_sun_zhu_2023]
- [Sun et al 2024][research_sun_jia_2024]
- [Sun et al 2024][research_sun_jing_2024]
- [Sun et al 2024][research_sun_qiu_2024]
- [Sun et al 2025][research_sun_huang_2025]
- [Sun et al 2025][research_sun_xu_2025]
- [Sun et al 2026][research_sun_chang_2026]
- [Sunasawa and Ohta 1997][research_sunasawa_ohta_1997]
- [Sunday][research_sunday_nd]
- [Suppes and Suppes 2026][research_suppes_2026]
- [Surzhikov 2015][research_surzhikov_2015]
- [Surzhikov 2018][research_surzhikov_2018]
- [Surzhikov 2018][research_surzhikov_2018_b]
- [Sushnigdha 2021][research_sushnigdha_2021]
- [Suszyński et al 2025][research_suszynski_kowalski_2025]
- [Suzuki 2013][research_suzuki_2013]
- [Suzuki et al 2014][research_suzuki_fujita_2014]
- [Suzuki et al 2016][research_suzuki_min_2016]
- [Svyatushenko and Yagodnikov 2021][research_svyatushenko_yagodnikov_2021]
- [Swamy and Zebenay 2021][research_swamy_zebenay_2021]
- [Swann 1960][research_swann_1960]
- [Swanson 1958][research_swanson_1958]
- [Swanson et al 2025][research_swanson_miller_2025]
- [Swathy et al 2018][research_swathy_geetha_2018]
- [Szalai et al 2005][research_szalai_chen_2005]
- [Szmuk et al 2017][research_szmuk_eren_2017]
- [Szymanski et al 2025][research_szymanski_2025]
- [Tabatabaei et al 2021][research_tabatabaei_orlu_2021]
- [Tablole and Banavar 1998][research_tablole_banavar_1998]
- [Tadema and Theunissen 2007][research_tadema_theunissen_2007]
- [Tadema and Theunissen 2008][research_tadema_theunissen_2008]
- [Taghizadeh et al 2022][research_taghizadeh_nezhadshahbodaghi_2022]
- [Taguchi et al 1999][research_taguchi_maita_1999]
- [Taguchi et al 2001][research_taguchi_futamura_2001]
- [Tahsini and Mousavi 2014][research_tahsini_mousavi_2014]
- [Taihua et al 2011][research_taihua_xianhong_2011]
- [Takahashi 1993][research_takahashi_1993]
- [Takahashi and Yamada 2018][research_takahashi_yamada_2018]
- [Takahashi et al 1997][research_takahashi_mizobata_1997]
- [Takahashi et al 2013][research_takahashi_yamada_2013]
- [Takahashi et al 2014][research_takahashi_ha_2014]
- [Takahashi et al 2015][research_takahashi_yamada_2015]
- [Takahashi et al 2016][research_takahashi_nakasato_2016]
- [Takahashi et al 2018][research_takahashi_goerzen_2018]
- [Takahashi et al 2024][research_takahashi_camberos_2024]
- [Talay and Stone 1991][research_talay_1991]
- [Tamer 2021][research_tamer_2021]
- [Tan][research_tan_nd]
- [Tan et al 2025][research_tan_yang_2025]
- [Tanck and Steadman 1998][research_tanck_steadman_1998]
- [Tancredi and Grassi 2007][research_tancredi_grassi_2007]
- [Tancredi et al 2007][research_tancredi_accardo_2007]
- [Tang 1970][research_tang_1970]
- [Tang 1971][research_tang_1971_b]
- [Tang and Pearson 1971][research_tang_1971]
- [Tang and Pearson 1973][research_tang_1973]
- [Tang et al 2014][research_tang_chen_2014]
- [Tang et al 2018][research_tang_long_2018]
- [Tang et al 2020][research_tang_zhai_2020]
- [Tangthong and Aktimagool 2021][research_tangthong_aktimagool_2021]
- [Taniguchi 2000][research_taniguchi_2000]
- [Tanno et al 2017][research_tanno_komuro_2017]
- [Tao Guo et al 2010][research_taoguo_daweiliu_2010]
- [Tariq et al 2026][research_tariq_wasim_2026]
- [Tartabini et al 2000][research_tartabini_2000]
- [Tate 1974][research_tate_1974]
- [Tate 1975][research_tate_1975]
- [Tatry et al 1997][research_tatry_deneu_1997]
- [Tava and Suzuki 2002][research_tava_suzuki_2002]
- [Taylor 1958][research_taylor_1958]
- [Taylor 2004][research_taylor_2004]
- [Taylor and Pamadi 1983][research_taylor_1983]
- [Tazartes and Mark 1988][research_tazartes_mark_1988]
- [Teixeira and Páscoa 2026][research_teixeira_pascoa_2026]
- [Tekinalp and Kumbasar 2015][research_tekinalp_kumbasar_2015]
- [Temple 2006][research_temple_2006]
- [Tendero Ventanas][research_ventanas_nd]
- [Teng et al 2021][research_teng_chen_2021]
- [Teng et al 2025][research_teng_han_2025]
- [Tenhave et al 2026][research_tenhave_joiner_2026]
- [Tennstedt and Schon 2021][research_tennstedt_schon_2021]
- [Tennstedt and Schön 2025][research_tennstedt_schon_2025]
- [Tennstedt et al 2023][research_tennstedt_rajagopalan_2023]
- [Teper et al 1981][research_teper_1981]
- [Terheyden and Zickwolff 1986][research_terheyden_zickwolff_1986]
- [Tetlow et al 2000][research_tetlow_schoettle_2000]
- [Tewell 1984][research_tewell_1984]
- [Thato Elijah and Rui Vasconcellos 2026][research_elijah_2026]
- [The NASA IVHM Technology 2000][research_nasa_ivhm_2000]
- [Theunissen 1994][research_theunissen_1994]
- [Thibodeaux 1977][research_thibodeaux_1977]
- [Thies 2022][research_thies_2022]
- [Tho and Wang 2009][research_tho_wang_2009]
- [Thomas 1998][research_thomas_1998]
- [Thomas 2025][research_thomas_2025]
- [Thomas and Perlbachs 1967][research_thomas_perlbachs_1967]
- [Thompson 1964][research_thompson_1964]
- [Thompson 1965][research_thompson_1965]
- [Thompson 1966][research_thompson_1966]
- [Thompson 1970][research_thompson_1970]
- [Thompson 1970][research_thompson_1970_b]
- [Thompson 2024][research_thompson_2024]
- [Thompson and Horton 1981][research_thompson_1981]
- [Thornton 1994][research_thornton_1994]
- [Thornton and Lamy 1992][research_thornton_lamy_1992]
- [Threadgill et al 2024][research_threadgill_hader_2024]
- [Throckmorton 1981][research_throckmorton_1981]
- [Throckmorton 1989][research_throckmorton_1989]
- [Tian 1980][research_tian_1980]
- [Tian and Sun 2014][research_tian_sun_2014]
- [Tian et al 2013][research_tian_zong_2013]
- [Tian et al 2015][research_tian_fan_2015]
- [Tian et al 2018][research_tian_yu_2018]
- [Tian et al 2022][research_tian_yu_2022]
- [Tian et al 2024][research_tian_yu_2024]
- [Tian et al 2025][research_tian_dong_2025]
- [Tian et al 2025][research_tian_luo_2025]
- [Tie et al 2018][research_tie_cao_2018]
- [Tieshan et al 2021][research_tieshan_zhiyao_2021]
- [Tire Overspeed Landing Test][research_tire_overspeed_nd]
- [Tirtey et al 2005][research_tirtey_paris_2005]
- [Tischler 2018][research_tischler_2018]
- [Titov and Serebryanskiy 2023][research_titov_serebryanskiy_2023]
- [Titov and Serebryansky 2023][research_titov_serebryansky_2023]
- [Titov and Serebryansky 2023][research_titov_serebryansky_2023_b]
- [Titov and Serebryansky 2026][research_titov_serebryansky_2026]
- [Titov et al 2025][research_titov_parnenkov_2025]
- [Tkhorenko et al 2023][research_tkhorenko_karshakov_2023]
- [Tobin and Dec 2015][research_tobin_dec_2015]
- [Toda and Koike 2021][research_toda_koike_2021]
- [Tokluoglu and Cavus 2019][research_tokluoglu_cavus_2019]
- [Tokugawa et al 2025][research_tokugawa_ishida_2025]
- [Tomac et al 2016][research_tomac_rizzi_2016]
- [Tomita and Fujiwara 2021][research_tomita_fujiwara_2021]
- [Tomita and Ho 2025][research_tomita_2025]
- [Tomita and Ho 2025][research_tomita_ho_2025]
- [Tomita et al 2022][research_tomita_2022]
- [Tong 1991][research_tong_1991]
- [Tooley and Wyatt 2024][research_tooley_wyatt_2024]
- [Topcu et al 2005][research_topcu_casoliva_2005]
- [Toraldo et al 2023][research_toraldo_ketabdari_2023]
- [Torres-Martinez et al 2010][research_torresmartinez_heaps_2010]
- [Toso and Maddock 2017][research_toso_maddock_2017]
- [Tournes and Johnson 1998][research_tournes_johnson_1998]
- [Tournes and Johnson 1998][research_tournes_johnson_1998_b]
- [Tournes and Johnson 2001][research_tournes_johnson_2001]
- [Tournes et al 1998][research_tournes_landrum_1998]
- [Tracy 1981][research_tracy_1981]
- [Trawny et al 2015][research_trawny_2015]
- [Trevino et al 2012][research_trevino_schwartz_2012]
- [Trifonov et al 2024][research_trifonov_shelkov_2024]
- [Tripathi et al 2018][research_tripathi_patel_2018]
- [Tripathi et al 2024][research_tripathi_kumarsinha_2024]
- [Tripathi et al 2024][research_tripathi_patel_2024]
- [Trittler et al 2016][research_trittler_rothermel_2016]
- [Trivailo et al 2013][research_trivailo_lentsch_2013]
- [Troya et al 2018][research_troya_mailloux_2018]
- [Trujillo et al 1983][research_trujillo_meyerjr_1983]
- [Trusfus and Abdullin 2021][research_trusfus_abdullin_2021]
- [Trushlyakov and Yudintsev 2019][research_trushlyakov_yudintsev_2019]
- [Try et al 2020][research_w_p_2020]
- [Tsai 2008][research_tsai_2008]
- [Tsapparellas et al 2023][research_tsapparellas_jelev_2023]
- [Tseng et al 2013][research_tseng_lou_2013]
- [Tsikalas 1982][research_tsikalas_1982]
- [Tsikalas and Dyer 1982][research_tsikalas_1982_b]
- [Tsitses et al 2024][research_tsitses_zacharia_2024]
- [Tsohas and Heister 2010][research_tsohas_heister_2010]
- [Tsoukalas et al 2026][research_tsoukalas_unlu_2026]
- [Tsuchiya and Suzuki 1998][research_tsuchiya_suzuki_1998]
- [Tsuchiya and Suzuki 2001][research_tsuchiya_suzuki_2001]
- [Tsukahara et al 2001][research_tsukahara_yamao_2001]
- [Tsukamoto et al 2003][research_tsukamoto_deturris_2003]
- [Tsukamoto et al 2004][research_tsukamoto_suzuki_2004]
- [Tsukerman et al 2017][research_tsukerman_weiss_2017]
- [Tsushima et al 2024][research_tsushima_saitoh_2024]
- [Tsuyuki et al 2005][research_tsuyuki_2005]
- [Tu et al 1998][research_tu_munir_1998]
- [Tuohy 1998][research_tuohy_1998]
- [Tuozzo et al 2017][research_tuozzo_fox_2017]
- [Tupitsin and Stepanenko 2020][research_tupitsin_stepanenko_2020]
- [Turnbow 1961][research_turnbow_1961]
- [Turner 1950][research_turner_1950]
- [Turner 1965][research_turner_1965]
- [Turner 2003][research_turner_2003]
- [Turner 2003][research_turner_2003_b]
- [Turner and London 2000][research_turner_2000]
- [Turner and Spanyer 2005][research_turner_2005]
- [Tushavina 2025][research_tushavina_2025]
- [Tweedale and Gonano 2014][research_tweedale_gonano_2014]
- [Udayakumar and Ibrahim 2019][research_udayakumar_ibrahim_2019]
- [Ueno and Yamaguchi 1999][research_ueno_yamaguchi_1999]
- [Uffelman and Deffenbaugh 1979][research_uffelman_deffenbaugh_1979]
- [Ulukır et al 2025][research_ulukir_dursun_2025]
- [Ulybyshev 2010][research_ulybyshev_2010]
- [Umadevi et al 2017][research_umadevi_navas_2017]
- [Ungvichian 1986][research_ungvichian_1986]
- [Uppoor and Chopra 2026][research_uppoor_2026]
- [Uppoor et al 2025][research_uppoor_zheng_2025]
- [Uppoor et al 2026][research_uppoor_chopra_2026]
- [Urnes and Hess 1983][research_urnes_hess_1983]
- [Urnes and Hess 1985][research_urnes_hess_1985]
- [Urnes et al 1979][research_urnes_hess_1979]
- [Urnes et al 1981][research_jmurnes_moomaw_1981]
- [Urschel and Cox 2003][research_urschel_cox_2003]
- [Usry and Wallace 1971][research_usry_1971]
- [Utkarsh R. Moholkar 2025][research_moholkar_2025]
- [Utterstrom and Kestek 1965][research_utterstrom_kestek_1965]
- [Uybarreta et al 2025][research_uybarreta_grant_2025]
- [Vaglio-Laurin and Finke 1965][research_vagliolaurin_finke_1965]
- [Vaispacher et al 2025][research_vaispacher_baranek_2025]
- [Valente et al 2006][research_valente_bartuli_2006]
- [Valentine et al 2004][research_valentine_2004]
- [Vallot et al 1991][research_vallot_snyder_1991]
- [Van Bavel 2014][research_vanbavel_2014]
- [van den Abeelen 2016][research_vandenabeelen_2016]
- [van den Abeelen 2016][research_vandenabeelen_2016_b]
- [van den Broek et al 2025][research_vandenbroek_simpson_2025]
- [van den Broek et al 2026][research_vandenbroek_hunns_2026]
- [Van Es 2017][research_vanes_2017]
- [Van Gaasbeek 1980][research_vangaasbeek_1980]
- [Van Graas et al 1994][research_vangraas_diggle_1994]
- [van Oort et al 2007][research_vanoort_chu_2007]
- [Van Pelt 1981][research_pelt_1981]
- [Van Wyckhouse 1966][research_vanwyckhouse_1966]
- [Vanatta and Inderhees 1988][research_vanatta_inderhees_1988]
- [Vaquero et al 2022][research_vaquero_kennedy_2022]
- [Vasconcelos et al 2005][research_vasconcelos_oliveira_2005]
- [Vassilakos et al 2011][research_vassilakos_2011]
- [Veaux 1988][research_veaux_1988]
- [Vendemia 1965][research_vendemia_1965]
- [Veneruso et al 2024][research_veneruso_miccio_2024]
- [Venkateswara Rao and Go 2014][research_venkateswararao_go_2014]
- [Venugopalan et al 2012][research_venugopalan_taher_2012]
- [Vepa and Zhahir 2010][research_vepa_zhahir_2010]
- [Verderame et al 1999][research_verderame_phillips_1999]
- [Verhaegen 1988][research_verhaegen_1988]
- [Verkhovsky et al 2023][research_verkhovsky_gyazova_2023]
- [Verma 1991][research_verma_1991]
- [Verma and Mettler 2017][research_verma_mettler_2017]
- [Verstraete et al 2009][research_verstraete_bizzarri_2009]
- [Vetter 1966][research_vetter_1966]
- [Vidal 1974][research_vidal_1974]
- [Videmsek and de Haag 2020][research_videmsek_dehaag_2020]
- [Vijayanandh et al 2020][research_vijayanandh_kiran_2020]
- [Viladegut 2018][research_viladegut_2018]
- [Villanueva 2022][research_villanueva_2022]
- [Vinh and Medepalli 1994][research_vinh_medepalli_1994]
- [Vinod et al 2012][research_vinod_geetha_2012]
- [Violette 2024][research_violette_2024]
- [Violette 2026][research_violette_2026]
- [Viscardi et al 2021][research_viscardi_arena_2021]
- [Viswanathan et al 2017][research_viswanathan_sanyal_2017]
- [Viviand 1991][research_viviand_1991]
- [Viviani and Pezzella 2007][research_viviani_pezzella_2007]
- [Viviani and Pezzella 2007][research_viviani_pezzella_2007_b]
- [Viviani and Pezzella 2009][research_viviani_pezzella_2009]
- [Viviani and Pezzella 2010][research_viviani_pezzella_2010]
- [Viviani et al 2006][research_viviani_pezzella_2006]
- [Viviani et al 2008][research_viviani_pezzella_2008]
- [Vo et al 1993][research_vo_garrard_1993]
- [Vocke and Nunez 2016][research_vocke_nunez_2016]
- [Volkov et al 2022][research_volkov_komar_2022]
- [Voloshenyuk 2018][research_voloshenyuk_2018]
- [Von Pragenau 1966][research_pragenau_1966]
- [Von Pragenau 1967][research_pragenau_1967]
- [Vorburger et al 1985][research_vorburger_mclay_1985]
- [Vorobуev et al 2020][research_vorobev_beliatskaya_2020]
- [Vos et al 2007][research_vos_hodigeresiddaramaiah_2007]
- [Voss et al 2026][research_voss_tang_2026]
- [Wagner and Valasek 2006][research_wagner_valasek_2006]
- [Wagner and Valasek 2007][research_wagner_valasek_2007]
- [Wahi and Straub 1977][research_wahi_straub_1977]
- [Waitman et al 2019][research_waitman_marcos_2019]
- [Wakamatsu et al 1999][research_wakamatsu_ono_1999]
- [Waldmann et al 2023][research_waldmann_ehrle_2023]
- [Walker 1960][research_walker_1960]
- [Walker 1981][research_walker_1981]
- [Walker et al 2018][research_walker_mueschke_2018]
- [Wallace and Gray 1963][research_wallace_1963]
- [Wallace et al 2003][research_wallace_olds_2003]
- [Wallner and Well 2002][research_wallner_well_2002]
- [Wallskog 1954][research_wallskog_1954]
- [Walpot et al 2006][research_walpot_noeding_2006]
- [Walton 2025][research_walton_2025]
- [Wan et al 2023][research_wan_pan_2023]
- [Wang 1963][research_wang_1963]
- [Wang 2016][research_wang_2016]
- [Wang 2022][research_wang_2022]
- [Wang 2022][research_wang_2022_b]
- [Wang 2024][research_wang_2024]
- [Wang and Chen 2019][research_wang_chen_2019]
- [Wang and Cui 2018][research_wang_cui_2018]
- [Wang and Holzapfel 2018][research_wang_holzapfel_2018]
- [Wang and Mou 2025][research_wang_mou_2025]
- [Wang and Wang 1997][research_wang_wang_1997]
- [Wang and Wang 2013][research_wang_wang_2013]
- [Wang and Zou 2021][research_wang_zou_2021]
- [Wang et al 1986][research_wang_demiroz_1986]
- [Wang et al 2005][research_wang_peng_2005]
- [Wang et al 2006][research_wang_peng_2006]
- [Wang et al 2007][research_wang_jau_2007]
- [Wang et al 2009][research_wang_wu_2009]
- [Wang et al 2011][research_wang_liu_2011]
- [Wang et al 2012][research_wang_liu_2012]
- [Wang et al 2013][research_wang_tang_2013]
- [Wang et al 2013][research_wang_zhang_2013]
- [Wang et al 2014][research_wang_li_2014]
- [Wang et al 2014][research_wang_wang_2014]
- [Wang et al 2014][research_wang_wu_2014]
- [Wang et al 2014][research_wang_xu_2014]
- [Wang et al 2015][research_wang_hua_2015]
- [Wang et al 2015][research_wang_zong_2015]
- [Wang et al 2016][research_wang_chen_2016]
- [Wang et al 2016][research_wang_hua_2016]
- [Wang et al 2016][research_wang_lu_2016]
- [Wang et al 2016][research_wang_wang_2016]
- [Wang et al 2016][research_wang_yu_2016]
- [Wang et al 2016][research_wang_zhou_2016]
- [Wang et al 2017][research_wang_feng_2017]
- [Wang et al 2017][research_wang_lu_2017]
- [Wang et al 2017][research_wang_zhang_2017]
- [Wang et al 2017][research_wang_zhou_2017]
- [Wang et al 2017][research_wang_zou_2017]
- [Wang et al 2018][research_wang_dong_2018]
- [Wang et al 2018][research_wang_jia_2018]
- [Wang et al 2018][research_wang_li_2018]
- [Wang et al 2018][research_wang_li_2018_b]
- [Wang et al 2018][research_wang_song_2018]
- [Wang et al 2019][research_wang_liu_2019]
- [Wang et al 2019][research_wang_wu_2019]
- [Wang et al 2019][research_wang_zhang_2019]
- [Wang et al 2020][research_wang_chen_2020]
- [Wang et al 2020][research_wang_xu_2020]
- [Wang et al 2020][research_wang_yin_2020]
- [Wang et al 2020][research_wang_zhang_2020]
- [Wang et al 2021][research_wang_2021]
- [Wang et al 2021][research_wang_li_2021]
- [Wang et al 2022][research_wang_bi_2022]
- [Wang et al 2022][research_wang_gong_2022]
- [Wang et al 2022][research_wang_jiang_2022]
- [Wang et al 2022][research_wang_lin_2022]
- [Wang et al 2022][research_wang_wei_2022]
- [Wang et al 2022][research_wang_yang_2022]
- [Wang et al 2022][research_wang_zhao_2022]
- [Wang et al 2022][research_wang_zhao_2022_b]
- [Wang et al 2022][research_wang_zheng_2022]
- [Wang et al 2023][research_wang_jiang_2023]
- [Wang et al 2023][research_wang_li_2023]
- [Wang et al 2023][research_wang_li_2023_b]
- [Wang et al 2023][research_wang_ma_2023]
- [Wang et al 2023][research_wang_tang_2023]
- [Wang et al 2023][research_wang_yuan_2023]
- [Wang et al 2023][research_wang_zhai_2023]
- [Wang et al 2024][research_wang_feng_2024]
- [Wang et al 2024][research_wang_liu_2024]
- [Wang et al 2024][research_wang_xu_2024]
- [Wang et al 2024][research_wang_yin_2024]
- [Wang et al 2025][research_wang_ai_2025]
- [Wang et al 2025][research_wang_gan_2025]
- [Wang et al 2025][research_wang_mu_2025]
- [Wang et al 2025][research_wang_shao_2025]
- [Wang et al 2025][research_wang_wang_2025]
- [Wang et al 2025][research_wang_wang_2025_b]
- [Wang et al 2025][research_wang_yang_2025]
- [Wang et al 2025][research_wang_yang_2025_b]
- [Wang et al 2026][research_wang_ding_2026]
- [Wang et al 2026][research_wang_zhang_2026]
- [Wang Lu et al 2016][research_wanglu_yaoweili_2016]
- [Wang Shihao et al 2018][research_wangshihao_yanzilin_2018]
- [Wangu and Mouyos 1998][research_wangu_mouyos_1998]
- [Ward and Costello 2012][research_ward_costello_2012]
- [Ward and Costello 2013][research_ward_costello_2013]
- [Ward and Myers 1967][research_ward_myers_1967]
- [Ward and Smart 2026][research_ward_smart_2026]
- [Ward et al 2011][research_ward_gavrilovski_2011]
- [Ward et al 2011][research_ward_gavrilovski_2011_b]
- [Ward et al 2013][research_ward_gavrilovski_2013]
- [Ward et al 2015][research_ward_costello_2015]
- [Ward et al 2025][research_ward_ho_2025]
- [Ward et al 2026][research_ward_collins_2026]
- [Wardana et al 2021][research_wardana_pranoto_2021]
- [Ware et al 1991][research_ware_spencerjr_1991]
- [Warner 1981][research_warner_1981]
- [Warren 2024][research_warren_2024]
- [Warsop and Crowther 2019][research_warsop_crowther_2019]
- [Watanabe et al 1997][research_watanabe_ishimoto_1997]
- [Watson et al 1981][research_watson_1981]
- [Watson et al 1983][research_watson_1983]
- [Watson et al 1986][research_watson_hardy_1986]
- [Watson-Morgan et al][research_watson_morgan_nd]
- [Watts 2005][research_watts_2005]
- [Way et al 2003][research_way_desai_2003]
- [Way et al 2024][research_way_sescu_2024]
- [Webb and Bettinger 2024][research_webb_bettinger_2024]
- [Webb et al 2026][research_webb_bettinger_2026]
- [Wee and Yechout 2004][research_wee_yechout_2004]
- [Wei and Du 2018][research_wei_du_2018]
- [Wei and Gjestvang 2001][research_wei_gjestvang_2001]
- [Wei and Nie 2005][research_wei_2005]
- [Wei and Wang 2025][research_wei_wang_2025]
- [Wei et al 2018][research_wei_xu_2018]
- [Wei et al 2022][research_wei_wang_2022]
- [Wei et al 2024][research_wei_2024]
- [Wei et al 2025][research_wei_kang_2025]
- [Wei et al 2026][research_wei_diaz_2026]
- [Weiland 2003][research_weiland_2003]
- [Weinacht 2003][research_weinacht_2003]
- [Weingarten and Chalk 1982][research_weingarten_chalk_1982]
- [Weismuller et al 2007][research_weismuller_caballero_2007]
- [Weiwei et al 2022][research_weiwei_runde_2022]
- [Welberg et al 2015][research_welberg_werner_2015]
- [Welch 1993][research_welch_1993]
- [Welge et al 2000][research_welge_2000]
- [Welker et al 2011][research_welker_huffman_2011]
- [Welker et al 2013][research_welker_pachter_2013]
- [Wells 1987][research_wells_1987]
- [Welsh and Watt 1967][research_welsh_1967]
- [Welton 1965][research_welton_1965]
- [Wen et al 2021][research_wen_huang_2021]
- [Wendel et al 1991][research_wendel_1991]
- [Weng et al 2020][research_weng_liu_2020]
- [Wenming et al 2015][research_wenming_zhi_2015]
- [Wenzel et al 2010][research_wenzel_masselli_2010]
- [Wernicke and Wernicke 1997][research_wernicke_1997]
- [Westbrook 1975][research_westbrook_1975]
- [Westphal and Wagner 2001][research_westphal_wagner_2001]
- [White 2010][research_white_2010]
- [White and Beck 2011][research_white_beck_2011]
- [White and Gibson 2004][research_white_gibson_2004]
- [White and James J 1967][research_white_jamesj_1967]
- [White et al 2024][research_white_fonnegra_2024]
- [Whitfield and Griffith 1963][research_whitfield_1963]
- [Whiting et al 2024][research_whiting_neill_2024]
- [Whitmore and Dunbar 2003][research_whitmore_dunbar_2003]
- [Whitmore et al 2004][research_whitmore_2004]
- [Wibben et al 2012][research_wibben_furfaro_2012]
- [Widnall and Grundy 1974][research_widnall_1974]
- [Widnall and Morth 1972][research_widnall_morth_1972]
- [Widnall et al 1982][research_widnall_gobbini_1982]
- [Wierzbanowski and Ramasubramanian 2020][research_wierzbanowski_ramasubramanian_2020]
- [Wijaya and Nurrohmad 2020][research_wijaya_nurrohmad_2020]
- [Wilcox 1963][research_wilcox_1963]
- [Wilder and Prabhu 2019][research_wilder_2019]
- [Wilder et al 2015][research_wilder_2015]
- [Wilhite 1977][research_wilhite_1977]
- [Williams 1947][research_williams_1947]
- [Williams 2017][research_williams_2017]
- [Williams 2021][research_williams_2021]
- [Williams and Al Seyab 2026][research_williams_alseyab_2026]
- [Williams and Hartford 1987][research_williams_hartford_1987]
- [Williams et al 1994][research_williams_1994]
- [Williams et al 1995][research_williams_curry_1995]
- [Williams et al 2000][research_williams_davis_2000]
- [Williamson 1978][research_williamsonjr_1978]
- [Williamson 1980][research_williamson_1980]
- [Williamson 1992][research_williamson_1992]
- [Williamson et al 2005][research_williamson_speyer_2005]
- [Williamson et al 2025][research_williamson_bi_2025]
- [Wilson 1967][research_wilson_1967]
- [Wilson 1980][research_wilson_1980]
- [Wilson and Chou 1985][research_wilson_chou_1985]
- [Wilson and Riccardi 2022][research_wilson_riccardi_2022]
- [Wilson et al 2015][research_wilson_goktogan_2015]
- [Wilz and Johnson 1975][research_wilz_johnson_1975]
- [Winchenbach 1997][research_winchenbach_1997]
- [Windhorst et al 1997][research_windhorst_ardema_1997]
- [Winski et al 2025][research_winski_langston_2025]
- [Wisely 2002][research_wisely_2002]
- [Wiseman and Lopez 2026][research_wiseman_lopez_2026]
- [Witte et al 2016][research_witte_roll_2016]
- [Wittliff et al 1992][research_wittliff_oconnor_1992]
- [Woestemeyer 1964][research_woestemeyer_1964]
- [Woestemeyer 1967][research_woestemeyer_1967]
- [Woicke and Krüger 2023][research_woicke_kruger_2023]
- [Woicke and Mooij 2017][research_woicke_mooij_2017]
- [Wolf 1996][research_wolf_1996]
- [Wolf and Bossert 2001][research_wolf_bossert_2001]
- [Wolf et al 2011][research_wolf_2011]
- [Wolf et al 2012][research_wolf_casoliva_2012]
- [Wolfe 1976][research_wolfe_1976]
- [Woloshen 1974][research_woloshen_1974]
- [Wong et al 2017][research_wong_ryan_2017]
- [Wood 1968][research_wood_1968]
- [Wood 1972][research_wood_1972]
- [Wood et al 2007][research_wood_avadhanula_2007]
- [Wood et al 2012][research_wood_2012]
- [Woodbury and Gorman 1983][research_woodbury_gorman_1983]
- [Woodbury and Valasek 2015][research_woodbury_valasek_2015]
- [Woodbury and Valasek 2016][research_woodbury_valasek_2016]
- [Woodbury and Wallace 1974][research_woodbury_1974]
- [Woodbury et al 2015][research_woodbury_valasek_2015_b]
- [Woods et al 2000][research_woods_2000]
- [Woods et al 2000][research_woods_2000_b]
- [Woollard et al 2016][research_woollard_braun_2016]
- [Wortman 1969][research_wortman_1969]
- [Wright 1989][research_wright_1989]
- [Wright 1992][research_wright_1992]
- [Wright and Zoby 1971][research_wright_1971]
- [Wright et al 2006][research_wright_milos_2006]
- [Wright et al 2014][research_wright_beck_2014]
- [Wu 2015][research_wu_2015]
- [Wu 2018][research_wu_2018]
- [Wu 2023][research_wu_2023]
- [Wu 2024][research_wu_2024]
- [Wu and Guo 1994][research_wu_guo_1994]
- [Wu and Liu 2021][research_wu_liu_2021]
- [Wu and Wang 2018][research_wu_wang_2018]
- [Wu and Zhang 2023][research_wu_zhang_2023]
- [Wu et al 1994][research_wu_lycans_1994]
- [Wu et al 2005][research_wu_johnson_2005]
- [Wu et al 2012][research_wu_tang_2012]
- [Wu et al 2014][research_wu_cai_2014]
- [Wu et al 2017][research_wu_gu_2017]
- [Wu et al 2017][research_wu_lian_2017]
- [Wu et al 2018][research_wu_shi_2018]
- [Wu et al 2018][research_wu_zhang_2018]
- [Wu et al 2019][research_wu_luo_2019]
- [Wu et al 2020][research_wu_tian_2020]
- [Wu et al 2022][research_wu_shi_2022]
- [Wu et al 2023][research_wu_luo_2023]
- [Wu et al 2024][research_wu_2024_b]
- [Wu et al 2025][research_wu_yuan_2025]
- [Wu et al 2026][research_wu_zhu_2026]
- [Wurster and Stone 1993][research_wurster_stone_1993]
- [Wurster et al 1999][research_wurster_riley_1999]
- [Wuxing et al 2015][research_wuxing_chunwang_2015]
- [Wuxing et al 2015][research_wuxing_pengxin_2015]
- [Wyborny and Requardt 1974][research_wyborny_requardt_1974]
- [Wyborny and Requardt 1975][research_wyborny_requardt_1975]
- [Wygle 1965][research_wygle_1965]
- [X-33, X-34, X-37 Press 1999][research_x_33_1999]
- [Xargay et al 2010][research_xargay_hovakimyan_2010]
- [Xi et al 2023][research_xi_li_2023]
- [Xia et al 2025][research_xia_hu_2025]
- [Xiang and Zhou 2022][research_xiang_zhou_2022]
- [Xiang et al 2024][research_xiang_guo_2024]
- [Xiang et al 2025][research_xiang_guo_2025]
- [Xiang et al 2026][research_xiang_du_2026]
- [Xiangyu et al 2004][research_xiangyu_hutao_2004]
- [Xiao 2022][research_xiao_2022]
- [Xiao 2026][research_xiao_2026]
- [Xiaoqing Chen et al 2010][research_xiaoqingchen_zhongxihou_2010]
- [Xie 2024][research_xie_2024]
- [Xie and Li 2016][research_xie_li_2016]
- [Xin 2021][research_xin_2021]
- [Xingling and Honglun 2014][research_xingling_honglun_2014]
- [Xinguo et al 2024][research_xinguo_ting_2024]
- [Xiong et al 2018][research_xiong_zhao_2018]
- [Xiu-zhen et al 2014][research_xiuzhen_shaolei_2014]
- [Xu 2015][research_xu_2015]
- [Xu 2025][research_xu_2025]
- [Xu and Lan 2018][research_xu_lan_2018]
- [Xu and Tang 2010][research_xu_tang_2010]
- [Xu and Wang 2016][research_xu_wang_2016]
- [Xu et al 2004][research_xu_mirmirani_2004]
- [Xu et al 2012][research_xu_sun_2012]
- [Xu et al 2012][research_xu_xia_2012]
- [Xu et al 2017][research_xu_wang_2017]
- [Xu et al 2017][research_xu_wang_2017_b]
- [Xu et al 2017][research_xu_zhao_2017]
- [Xu et al 2018][research_xu_fu_2018]
- [Xu et al 2020][research_xu_hu_2020]
- [Xu et al 2021][research_xu_huang_2021]
- [Xu et al 2021][research_xu_liu_2021]
- [Xu et al 2022][research_xu_dong_2022]
- [Xu et al 2022][research_xu_guan_2022]
- [Xu et al 2023][research_xu_guan_2023]
- [Xu et al 2025][research_xu_guo_2025]
- [Xu Xibao et al 2016][research_xuxibao_guojifeng_2016]
- [Xue et al 2019][research_xue_qin_2019]
- [Xuguo et al 2018][research_xuguo_ke_2018]
- [Yadav and Ramamoorthy 1991][research_yadav_ramamoorthy_1991]
- [Yadav et al 2018][research_yadav_bodavula_2018]
- [Yafei et al 2015][research_yafei_jianqiao_2015]
- [Yager 1983][research_yager_1983]
- [Yager 1991][research_yager_1991]
- [Yakimenko and Altmann 2015][research_yakimenko_altmann_2015]
- [Yamada and Suzuki 2016][research_yamada_suzuki_2016]
- [Yamada et al 2011][research_yamada_suzuki_2011]
- [Yamada et al 2014][research_yamada_kawano_2014]
- [Yamamoto et al 1996][research_yamamoto_atsumi_1996]
- [Yamanaka 1989][research_yamanaka_1989]
- [Yamanaka 2003][research_yamanaka_2003]
- [Yamanaka et al 2001][research_yamanaka_maita_2001]
- [Yamasaki et al 2013][research_yamasaki_matsumoto_2013]
- [Yan and He 2020][research_yan_he_2020]
- [Yan and Hexi 2025][research_yan_hexi_2025]
- [Yan and von der Dunk 1992][research_yan_vonderdunk_1992]
- [Yan and Xu 2013][research_yan_xu_2013]
- [Yan et al 2015][research_yan_luo_2015]
- [Yan et al 2015][research_yan_wang_2015]
- [Yan et al 2016][research_yan_tan_2016]
- [Yan et al 2023][research_yan_zhao_2023]
- [Yan et al 2025][research_yan_chen_2025]
- [Yanagihara et al 1991][research_yanagihara_suzuki_1991]
- [Yanagihara et al 1999][research_yanagihara_shigemi_1999]
- [Yang 2025][research_yang_2025]
- [Yang and Li 2008][research_yang_li_2008]
- [Yang and Liu 2021][research_yang_liu_2021]
- [Yang and Meng 2012][research_yang_meng_2012]
- [Yang and Qi 2016][research_yang_qi_2016]
- [Yang and Tan 2014][research_yang_tan_2014]
- [Yang and Wang 2012][research_yang_wang_2012]
- [Yang and Wang 2013][research_yang_wang_2013]
- [Yang and Yanguang 2015][research_yang_yanguang_2015]
- [Yang et al 2006][research_yang_hu_2006]
- [Yang et al 2015][research_yang_zhang_2015]
- [Yang et al 2016][research_yang_qiu_2016]
- [Yang et al 2016][research_yang_ye_2016]
- [Yang et al 2017][research_yang_wang_2017]
- [Yang et al 2018][research_yang_shi_2018]
- [Yang et al 2021][research_yang_ye_2021]
- [Yang et al 2022][research_yang_wang_2022]
- [Yang et al 2022][research_yang_wu_2022]
- [Yang et al 2023][research_yang_chen_2023]
- [Yang et al 2024][research_yang_gan_2024]
- [Yang et al 2024][research_yang_hao_2024]
- [Yang et al 2025][research_yang_chen_2025]
- [Yang et al 2025][research_yang_men_2025]
- [Yang et al 2025][research_yang_zhang_2025]
- [Yang et al 2026][research_yang_yang_2026]
- [Yankui et al 2005][research_yankui_2005]
- [Yao and Jia 2023][research_yao_jia_2023]
- [Yao and Wu 2019][research_yao_wu_2019]
- [Yao et al 2013][research_yao_wang_2013]
- [Yao et al 2021][research_yao_li_2021]
- [Yao et al 2022][research_yao_ma_2022]
- [Yao et al 2025][research_yao_kan_2025]
- [Yao et al 2025][research_yao_li_2025]
- [Yao et al 2025][research_yao_li_2025_b]
- [Yap et al 2012][research_yap_macias_2012]
- [Yarlett et al 2000][research_yarlett_adrezin_2000]
- [Yassir Fadhilah et al 2024][research_yassirfadhilah_mubarok_2024]
- [Yates and Venkatapathy 1991][research_yates_1991]
- [Ye 2023][research_ye_2023]
- [Ye et al 2017][research_ye_chaofang_2017]
- [Ye et al 2021][research_ye_li_2021]
- [Ye et al 2024][research_ye_wang_2024]
- [Yee et al 2023][research_yee_parkinson_2023]
- [Yelin Zhang et al 2016][research_yelinzhang_yangzhuwang_2016]
- [Yeom et al 2009][research_yeom_oh_2009]
- [Yerdon and Cook 2015][research_yerdon_cook_2015]
- [Yi et al 2011][research_yi_2011]
- [YiFan et al 2024][research_yifan_minghe_2024]
- [Yilmaz et al 2019][research_yilmaz_warren_2019]
- [Yin et al 2024][research_yin_2024]
- [Yin et al 2024][research_yin_li_2024]
- [Yingying et al 2011][research_yingying_yanshun_2011]
- [Yip 1987][research_yip_1987]
- [Yip et al 1990][research_yip_1990]
- [Yntema and Milwitzky 1952][research_yntema_1952]
- [Yong Jiang et al 2006][research_yongjiang_jiecao_2006]
- [Yongsheng 2021][research_yongsheng_2021]
- [Yongsheng 2021][research_yongsheng_2021_b]
- [Yoon et al 2021][research_yoon_kim_2021]
- [Yoshinaga et al 1995][research_yoshinaga_tate_1995]
- [Yoshinaga et al 1996][research_yoshinaga_tate_1996]
- [You et al 2019][research_you_yasaee_2019]
- [Young 1966][research_young_1966]
- [Youngshin Kang et al 2008][research_kang_2008]
- [Youssef et al 2001][research_youssef_2001]
- [Yu et al 2014][research_yu_sun_2014]
- [Yu et al 2015][research_yu_xu_2015]
- [Yu et al 2017][research_yu_cai_2017]
- [Yu et al 2017][research_yu_wang_2017]
- [Yu et al 2018][research_yu_li_2018]
- [Yu et al 2019][research_yu_li_2019]
- [Yu et al 2020][research_yu_yang_2020]
- [Yu et al 2021][research_yu_ni_2021]
- [Yu et al 2024][research_yu_zhang_2024]
- [Yu et al 2025][research_yu_baek_2025]
- [Yu et al 2026][research_yu_wang_2026]
- [Yuan and He 2025][research_yuan_he_2025]
- [Yuan et al 2006][research_yuan_gong_2006]
- [Yuan et al 2018][research_yuan_zhu_2018]
- [Yuan et al 2019][research_yuan_sun_2019]
- [Yuan et al 2022][research_yuan_xu_2022]
- [Yue and Yuan 2002][research_yue_yuan_2002]
- [Yue et al 2017][research_yue_lian_2017]
- [Yue et al 2019][research_yue_titurus_2019]
- [Yue et al 2022][research_yue_lin_2022]
- [Yue et al 2022][research_yue_titurus_2022]
- [Yue et al 2022][research_yue_zuo_2022]
- [Yun et al 2019][research_yun_seo_2019]
- [Yuta Akai et al 2007][research_yutaakai_kenjiuchiyama_2007]
- [Zahn et al][research_zahn_nd]
- [Zakharin and Ponomarenko 2023][research_zakharin_ponomarenko_2023]
- [Zakrajsek et al 2017][research_zakrajsek_vogel_2017]
- [Zammit-Mangion et al 2006][research_zammitmangion_zammit_2006]
- [Zavalishin et al 2021][research_zavalishin_zatuchny_2021]
- [Zeiler et al 1999][research_zeiler_mcghee_1999]
- [Zeng et al 2026][research_zeng_wang_2026]
- [Zeyuan et al 2021][research_zeyuan_huahui_2021]
- [Zhai et al 2016][research_zhai_qi_2016]
- [Zhai et al 2019][research_zhai_qi_2019]
- [Zhang 1992][research_zhang_1992]
- [Zhang 2008][research_zhang_2008]
- [Zhang 2011][research_zhang_2011]
- [Zhang 2015][research_zhang_2015]
- [Zhang 2019][research_zhang_2019]
- [Zhang 2024][research_zhang_2024]
- [Zhang and Chen 2011][research_zhang_chen_2011]
- [Zhang and Ding 2023][research_zhang_ding_2023]
- [Zhang and Han 2025][research_zhang_han_2025]
- [Zhang and Hu 2025][research_zhang_hu_2025]
- [Zhang and Jia 2013][research_zhang_jia_2013]
- [Zhang and Wang 2013][research_zhang_wang_2013]
- [Zhang and Wang 2024][research_zhang_wang_2024]
- [Zhang and Wang 2025][research_zhang_wang_2025_c]
- [Zhang and Yang 2015][research_zhang_yang_2015]
- [Zhang and Zhang 2011][research_zhang_zhang_2011]
- [Zhang and Zhang 2020][research_zhang_zhang_2020_b]
- [Zhang Dayong et al 2008][research_zhangdayong_wuwenqi_2008]
- [Zhang et al 2005][research_zhang_gray_2005]
- [Zhang et al 2007][research_zhang_cai_2007]
- [Zhang et al 2009][research_zhang_wan_2009]
- [Zhang et al 2013][research_zhang_sun_2013]
- [Zhang et al 2014][research_zhang_lin_2014]
- [Zhang et al 2016][research_zhang_liu_2016]
- [Zhang et al 2016][research_zhang_shi_2016]
- [Zhang et al 2016][research_zhang_sun_2016]
- [Zhang et al 2016][research_zhang_wang_2016]
- [Zhang et al 2017][research_zhang_guo_2017]
- [Zhang et al 2017][research_zhang_li_2017]
- [Zhang et al 2017][research_zhang_mu_2017]
- [Zhang et al 2017][research_zhang_tang_2017]
- [Zhang et al 2017][research_zhang_wang_2017]
- [Zhang et al 2017][research_zhang_wei_2017]
- [Zhang et al 2017][research_zhang_wu_2017]
- [Zhang et al 2017][research_zhang_zong_2017]
- [Zhang et al 2018][research_zhang_wei_2018]
- [Zhang et al 2018][research_zhang_yu_2018]
- [Zhang et al 2019][research_zhang_li_2019]
- [Zhang et al 2019][research_zhang_li_2019_d]
- [Zhang et al 2019][research_zhang_wei_2019]
- [Zhang et al 2019][research_zhang_wei_2019_b]
- [Zhang et al 2019][research_zhang_zhai_2019]
- [Zhang et al 2019][research_zhang_zhai_2019_b]
- [Zhang et al 2020][research_zhang_nie_2020]
- [Zhang et al 2021][research_zhang_hu_2021]
- [Zhang et al 2021][research_zhang_jing_2021]
- [Zhang et al 2021][research_zhang_li_2021]
- [Zhang et al 2021][research_zhang_lin_2021]
- [Zhang et al 2021][research_zhang_mu_2021]
- [Zhang et al 2022][research_zhang_chang_2022]
- [Zhang et al 2022][research_zhang_selezneva_2022]
- [Zhang et al 2022][research_zhang_shou_2022]
- [Zhang et al 2022][research_zhang_wang_2022]
- [Zhang et al 2022][research_zhang_xu_2022]
- [Zhang et al 2022][research_zhang_zhang_2022]
- [Zhang et al 2022][research_zhang_zhou_2022]
- [Zhang et al 2023][research_zhang_bai_2023]
- [Zhang et al 2023][research_zhang_chen_2023]
- [Zhang et al 2023][research_zhang_gao_2023]
- [Zhang et al 2023][research_zhang_liu_2023]
- [Zhang et al 2023][research_zhang_wang_2023]
- [Zhang et al 2023][research_zhang_wang_2023_b]
- [Zhang et al 2023][research_zhang_zhang_2023]
- [Zhang et al 2024][research_zhang_cai_2024]
- [Zhang et al 2024][research_zhang_yu_2024]
- [Zhang et al 2025][research_zhang_han_2025_b]
- [Zhang et al 2025][research_zhang_ma_2025]
- [Zhang et al 2025][research_zhang_wang_2025]
- [Zhang et al 2025][research_zhang_wang_2025_b]
- [Zhang et al 2025][research_zhang_wang_2025_d]
- [Zhang et al 2025][research_zhang_yin_2025]
- [Zhang et al 2026][research_zhang_chen_2026]
- [Zhang et al 2026][research_zhang_liao_2026]
- [Zhang et al 2026][research_zhang_yuan_2026]
- [Zhao 2024][research_zhao_2024]
- [Zhao and Pei 2012][research_zhao_pei_2012]
- [Zhao and Tang 2015][research_zhao_tang_2015]
- [Zhao and Zhao 2024][research_zhao_zhao_2024]
- [Zhao and Zhou 2013][research_zhao_zhou_2013]
- [Zhao et al 2011][research_zhao_cui_2011]
- [Zhao et al 2013][research_zhao_li_2013]
- [Zhao et al 2013][research_zhao_pei_2013]
- [Zhao et al 2013][research_zhao_yang_2013]
- [Zhao et al 2014][research_zhao_chen_2014]
- [Zhao et al 2014][research_zhao_sheng_2014]
- [Zhao et al 2016][research_zhao_wang_2016]
- [Zhao et al 2018][research_zhao_he_2018]
- [Zhao et al 2019][research_zhao_zhou_2019]
- [Zhao et al 2020][research_zhao_li_2020]
- [Zhao et al 2021][research_zhao_he_2021]
- [Zhao et al 2023][research_zhao_blunt_2023]
- [Zhen et al 2018][research_zhen_jiang_2018]
- [Zhen et al 2019][research_zhen_peng_2019]
- [Zheng 2021][research_zheng_2021]
- [Zheng and Liu 2018][research_zheng_liu_2018]
- [Zheng and Selezneva 2022][research_zheng_selezneva_2022]
- [Zheng and Sergeevna 2022][research_zheng_sergeevna_2022]
- [Zheng and Wang 2019][research_zheng_wang_2019]
- [Zheng and Yin 2025][research_zheng_yin_2025]
- [Zheng et al 2014][research_zheng_liang_2014]
- [Zheng et al 2017][research_zheng_jin_2017]
- [Zheng et al 2025][research_zheng_zou_2025]
- [Zhengchun 2018][research_zhengchun_2018]
- [Zhi et al 2015][research_zhi_ran_2015]
- [Zhi et al 2022][research_zhi_liu_2022]
- [Zhicong and Voronko 2023][research_zhicong_voronko_2023]
- [Zhihui Zheng et al 2016][research_zhihuizheng_haipingwei_2016]
- [Zhimin and Guanxin 2008][research_zhimin_guanxin_2008]
- [Zhiqiang et al 2015][research_zhiqiang_huiping_2015]
- [Zhishuai et al 2023][research_zhishuai_di_2023]
- [Zhixin 2022][research_zhixin_2022]
- [Zhong et al 2017][research_zhong_liu_2017]
- [Zhongping 2023][research_zhongping_2023]
- [Zhou 2025][research_zhou_2025]
- [Zhou 2026][research_zhou_2026]
- [Zhou and Feng 2023][research_zhou_feng_2023]
- [Zhou and Neusypin 2023][research_zhou_neusypin_2023]
- [Zhou and Takaba 2019][research_zhou_takaba_2019]
- [Zhou and Wang 1987][research_zhou_wang_1987]
- [Zhou and Wang 2012][research_zhou_wang_2012]
- [Zhou et al 2010][research_zhou_knedlik_2010]
- [Zhou et al 2013][research_zhou_yang_2013]
- [Zhou et al 2013][research_zhou_zhou_2013]
- [Zhou et al 2015][research_zhou_xiao_2015]
- [Zhou et al 2019][research_zhou_liang_2019]
- [Zhou et al 2020][research_zhou_ohashi_2020]
- [Zhou et al 2020][research_zhou_wang_2020]
- [Zhou et al 2020][research_zhou_zheng_2020]
- [Zhou et al 2021][research_zhou_zhong_2021]
- [Zhou et al 2021][research_zhou_zhong_2021_b]
- [Zhou et al 2023][research_zhou_jin_2023]
- [Zhou et al 2023][research_zhou_li_2023]
- [Zhou et al 2023][research_zhou_zheng_2023]
- [Zhou et al 2024][research_zhou_yang_2024]
- [Zhou et al 2024][research_zhou_zuo_2024]
- [Zhou et al 2026][research_zhou_wan_2026]
- [Zhu 2024][research_zhu_2024]
- [Zhu and Liu 2015][research_zhu_liu_2015]
- [Zhu and Wang 2025][research_zhu_wang_2025]
- [Zhu and Yang 2020][research_zhu_yang_2020]
- [Zhu et al 2016][research_zhu_li_2016]
- [Zhu et al 2021][research_zhu_bai_2021]
- [Zhu et al 2021][research_zhu_liu_2021]
- [Zhu et al 2021][research_zhu_wang_2021]
- [Zhu et al 2024][research_zhu_zhang_2024]
- [Zhu et al 2025][research_zhu_lee_2025]
- [Zhu Qi-dan et al 2009][research_zhuqidan_wangtong_2009]
- [Zhu Qi-dan et al 2009][research_zhuqidan_wangtong_2009_b]
- [Zhu Qidan et al 2009][research_zhuqidan_zhangwen_2009]
- [Zieja et al 2015][research_zieja_kosinski_2015]
- [Zilong et al 2019][research_zilong_zhaokui_2019]
- [Zimmerman et al 2002][research_zimmerman_2002]
- [Zimmerman et al 2003][research_zimmerman_dukeman_2003]
- [Zimpfer 1999][research_zimpfer_1999]
- [Zong et al 2013][research_zong_wang_2013]
- [Zou et al 2025][research_zou_chen_2025]
- [Zubrin and Clapp 1996][research_zubrin_clapp_1996]
- [Zucker 1970][research_zucker_1970]
- [Zumwalt et al 2016][research_zumwalt_cruz_2016]
- [Zuppardi and Mongelluzzo 2023][research_zuppardi_mongelluzzo_2023]
- [Zuppardi and Mongelluzzo 2023][research_zuppardi_mongelluzzo_2023_b]
- [Zwirglmaier et al 2014][research_zwirglmaier_drees_2014]
- [Çabuk 2021][research_cabuk_2021]
- [Çabuk 2023][research_cabuk_2023]
- [Çeti̇n et al 2024][research_cetin_aygun_2024]
- [Štumper et al 2015][research_stumper_kraus_2015]
- [Ашихмина and others, 2018, Thermal design of the wing skin of a tourist class reusable spacecraft][research_thermal_design_of_2018]
- [Бабич and others, 2017, Features of landing approach for aircraft in automatic and yoke control modes in conditions of vertical wind shear][research_features_of_landing_2017]
- [Борзых and Воронин, 2012, Dynamics of Interaction of Transformable Mechanical Landing Device of the Reentry Vehicle with the Landing Surface][research_dynamics_of_interaction_2012]
- [Кашматов, 2008, Application of quasi-object control systems by angular position of airplane for the translation of airplane from horizontal flight in a glide slope approach][research_application_of_quasi_object_2008]
- [Николаев, 2020, Determining the Rational Composition of a Plane Group When Planning a Flight Test][research_determining_the_rational_2020]
- [Філяшкін and Мельников, 2012, Automatic landing control plane based on the predictive model algorithm][research_automatic_landing_control_2012]
- [Яцковий and Вірченко, 2017, modeling of design and technological parameters of the airplane landing gear][research_modeling_of_design_2017]
- [안미치코, 2013, Aerodynamics Calculation of Reentry Body in Hypersonic Flowfield][research_aerodynamics_calculation_of_2013]

[ref_atm76]: https://ntrs.nasa.gov/citations/19770009539
[ref_boeing_1998]: https://boeing.mediaroom.com/1998-08-11-Boeing-and-U.S.-Air-Force-Flight-Test-Space-Maneuver-Vehicle
[ref_buran]: https://en.wikipedia.org/wiki/Buran_(spacecraft)
[ref_ch47]: https://en.wikipedia.org/wiki/Boeing_CH-47_Chinook
[ref_lifting_body]: https://en.wikipedia.org/wiki/Lifting_body
[ref_nasa_x40]: https://www.nasa.gov/aeronautics/nasa-aircraft/x-40/
[ref_nmusaf_x40]: https://www.nationalmuseum.af.mil/Visit/Museum-Exhibits/Fact-Sheets/Display/Article/195752/boeing-x-40a/
[ref_sciencedaily_x40]: https://www.sciencedaily.com/releases/2001/04/010417074551.htm
[ref_shuttle]: https://en.wikipedia.org/wiki/Space_Shuttle
[ref_smv_global]: https://www.globalsecurity.org/space/systems/x-40.htm
[ref_uh60]: https://en.wikipedia.org/wiki/Sikorsky_UH-60_Black_Hawk
[ref_x37]: https://en.wikipedia.org/wiki/Boeing_X-37
[ref_x37_x40]: https://www.designation-systems.net/dusrm/app4/x-37.html
[ref_x40]: https://en.wikipedia.org/wiki/Boeing_X-40

[related_post_a297_framing]: {% post_url 2025-10-06-x_planes_framing %}
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
[related_post_a323_schweizer_x26]: {% post_url 2025-11-01-x_planes_schweizer_x26 %}
[related_post_a324_lockheed_x27]: {% post_url 2025-11-02-x_planes_lockheed_x27 %}
[related_post_a325_osprey_x28]: {% post_url 2025-11-03-x_planes_osprey_x28 %}
[related_post_a326_grumman_x29]: {% post_url 2025-11-04-x_planes_grumman_x29 %}
[related_post_a327_rockwell_x30]: {% post_url 2025-11-05-x_planes_rockwell_x30 %}
[related_post_a328_rockwell_mbb_x31]: {% post_url 2025-11-06-x_planes_rockwell_mbb_x31 %}
[related_post_a329_boeing_x32]: {% post_url 2025-11-07-x_planes_boeing_x32 %}
[related_post_a330_lockheed_martin_x33]: {% post_url 2025-11-08-x_planes_lockheed_martin_x33 %}
[related_post_a331_orbital_sciences_x34]: {% post_url 2025-11-09-x_planes_orbital_sciences_x34 %}
[related_post_a332_lockheed_martin_x35]: {% post_url 2025-11-10-x_planes_lockheed_martin_x35 %}
[related_post_a333_mcdonnell_douglas_x36]: {% post_url 2025-11-11-x_planes_mcdonnell_douglas_x36 %}
[related_post_a334_boeing_x37]: {% post_url 2025-11-12-x_planes_boeing_x37 %}
[related_post_a335_scaled_composites_x38]: {% post_url 2025-11-13-x_planes_scaled_composites_x38 %}
[related_post_a336_x39_reserved_never_assigned]: {% post_url 2025-11-14-x_planes_x39_reserved_never_assigned %}

[research_180_fault_1994]: https://doi.org/10.1016/0967-0661(94)90532-0
[research_3_inertiale_2007]: https://doi.org/10.1524/9783486595154.27
[research_3_inertiale_2011]: https://doi.org/10.1524/9783486705720.27
[research_4_inertial_2001]: https://doi.org/10.1515/9783110800234.101
[research_4_inertial_2023]: https://doi.org/10.1515/9783110784329-004
[research_5_inertial_2013]: https://doi.org/10.4324/9780080941523-108
[research_6_aircraft_2011]: https://doi.org/10.1515/9781400839063-009
[research_a_bt_2015]: https://doi.org/10.4172/2168-9792.1000144
[research_a_manageable_2021]: https://doi.org/10.2307/j.ctv1m0kjm2.17
[research_a_minimum_1964]: https://doi.org/10.2514/5.9781600864872.0965.0994
[research_a_study_2018]: https://doi.org/10.25236/csbioe.2018.11
[research_a_typical]: https://doi.org/10.1049/sbra507e_ch11
[research_abdolkarimi_mosavi_2020]: https://doi.org/10.1007/s10291-020-01023-9
[research_abe_fujita_2001]: https://doi.org/10.2514/6.2001-1905
[research_abe_kasamura_2018]: https://doi.org/10.1299/jsmemecj.2018.j0260204
[research_abe_shimada_2005]: https://doi.org/10.2322/tjsass.48.135
[research_abensur_1994]: https://doi.org/10.2514/6.1994-3465
[research_abershitz_rubinets_2009]: https://doi.org/10.2514/6.2009-1832
[research_abrahamm_valsa_2018]: https://doi.org/10.18520/cs/v114/i01/144-147
[research_abujbara_alheadary_2015]: https://doi.org/10.1109/icuas.2015.7152407
[research_abujoub_mcphee_2018]: https://doi.org/10.1109/oceans.2018.8604820
[research_acarbay_kiyak_2022]: https://doi.org/10.1108/aeat-09-2021-0272
[research_achambath_ramjatan_2019]: https://doi.org/10.2514/6.2019-1283
[research_achambath_schwartzentruber_2018]: https://doi.org/10.2514/6.2018-0493
[research_acikmese_ploen_2005]: https://doi.org/10.2514/6.2005-6288
[research_acikmese_ploen_2007]: https://doi.org/10.2514/1.27553
[research_acquatella_reiner_2014]: https://doi.org/10.3384/ecp14096589
[research_adams_johnc_1973]: https://doi.org/10.21236/ad0756499
[research_adelgren_2004]: https://doi.org/10.21236/ada428090
[research_adhikari_black_2024]: https://doi.org/10.1063/5.0187505
[research_advanced_hypersonic_2004]: https://doi.org/10.2514/6.iac-04-p.p.17
[research_aerodynamic_optimization_1994]: https://doi.org/10.2514/5.9781600866326.0296.0307
[research_aerodynamics_calculation_of_2013]: https://doi.org/10.17958/ksmt.15.6.201312.819
[research_aeroelastic_tests_1963]: https://ntrs.nasa.gov/citations/20070030987
[research_aftatah_zebbara_2024]: https://doi.org/10.56294/dm2024.405
[research_agustin_mangoubi_1999]: https://doi.org/10.2514/2.4461
[research_ahmed_2003]: https://ntrs.nasa.gov/citations/20030106488
[research_ahmed_2021]: https://doi.org/10.1109/icns52807.2021.9441573
[research_ahmed_hazry_2017]: https://doi.org/10.5954/icarob.2017.gs11-10
[research_ai_hu_2023]: https://doi.org/10.23919/ccc58697.2023.10240026
[research_ai_wang_2022]: https://doi.org/10.1016/j.compstruct.2022.116073
[research_airborne_computer_2021]: https://doi.org/10.22266/ijies2021.1231.22
[research_aircraft_automatic_1996]: https://doi.org/10.2514/5.9781600866395.0397.0425
[research_aircraft_steady_2011]: https://doi.org/10.2307/j.ctvcm4h26.11
[research_airforceflighttestcenteredwardsafbca_1974]: https://doi.org/10.21236/ada011561
[research_airforcetestpilotschooledwardsafbca_1990]: https://doi.org/10.21236/ada320062
[research_airforcetestpilotschooledwardsafbca_1991]: https://doi.org/10.21236/ada320218
[research_airforcetestpilotschooledwardsafbca_1992]: https://doi.org/10.21236/ada320221
[research_airforcetestpilotschooledwardsafbca_1993]: https://doi.org/10.21236/ada320063
[research_airoldi_janszen_2005]: https://doi.org/10.1016/j.ast.2005.04.001
[research_ajacobdamotta_2020]: https://doi.org/10.5162/ettc2020/2.6
[research_akaryildiz_2024]: https://doi.org/10.2514/6.2024-2876
[research_akash_anbarasu_2025]: https://doi.org/10.1109/ipmml68499.2025.11407142
[research_akinyemi_adebiyi_2016]: https://doi.org/10.1504/ijrs.2016.078387
[research_alaverdi_2001]: https://doi.org/10.2514/6.2001-4015
[research_albach_fewel_1965]: https://doi.org/10.4271/650843
[research_albakri_albakri_2020]: https://doi.org/10.2514/1.g004934
[research_albakri_kluever_2017]: https://doi.org/10.4236/aast.2017.24004
[research_alber_2012]: https://doi.org/10.1007/978-3-642-22537-6_5
[research_alberts_thomas_2026]: https://doi.org/10.1016/j.actamat.2026.122613
[research_albertson_tartabini_2012]: https://doi.org/10.2514/6.2012-4863
[research_albrecht_1972]: https://doi.org/10.4050/sm_vstol_1972-2724
[research_alcedo_1980]: https://doi.org/10.4050/jahs.25.3.3
[research_alexander_1979]: https://doi.org/10.21236/ada068345
[research_alexander_griffin_1973]: https://doi.org/10.21236/ad0763725
[research_alexander_tm_1978]: https://doi.org/10.21236/ada063655
[research_alexeev_zemlyanyy_2023]: https://doi.org/10.23919/icins51816.2023.10168487
[research_alfatih_shimoyama_2021]: https://doi.org/10.2514/6.2021-3039
[research_alford_bingham_1990]: https://doi.org/10.21236/ada225125
[research_alford_chamdani_1994]: https://doi.org/10.21236/ada284339
[research_algorithms_flexible_2012]: https://doi.org/10.18698/2308-6033-2012-1-72
[research_ali_2007]: https://doi.org/10.2514/6.2007-6662
[research_ali_abbas_2024]: https://doi.org/10.31026/j.eng.2024.09.09
[research_ali_nd]: https://ntrs.nasa.gov/citations/20260000718
[research_ali_nd_b]: https://ntrs.nasa.gov/citations/20260000331
[research_alich_castillo_2007]: https://doi.org/10.2514/6.2007-1608
[research_alijani_osman_2020]: https://doi.org/10.1109/iccad49821.2020.9260498
[research_allee_1980]: https://doi.org/10.21236/ada087490
[research_allen_1962]: https://doi.org/10.21236/ad0404489
[research_allen_lin_2007]: https://doi.org/10.2514/6.2007-867
[research_allen_sauvageau_1994]: https://doi.org/10.2514/6.1994-4499
[research_allen_sexton_2015]: https://doi.org/10.2514/6.2015-1171
[research_allison_2017]: https://doi.org/10.2514/6.2017-5350
[research_almeida_2011]: https://doi.org/10.2514/6.2011-6673
[research_almeida_2021]: https://doi.org/10.2514/6.2021-1566
[research_almosnino_2016]: https://doi.org/10.2514/6.2016-3266
[research_alonis_1988]: https://doi.org/10.21236/ada194058
[research_alpert_2001]: https://doi.org/10.2514/6.2001-4282
[research_alroqi_wang_2017]: https://doi.org/10.4028/www.scientific.net/aef.23.88
[research_alsharman_aljarrah_2018]: https://doi.org/10.1115/1.4039943
[research_alt_final_1978]: https://ntrs.nasa.gov/citations/19780011246
[research_altmann_2013]: https://doi.org/10.2514/6.2013-1345
[research_alvord_arias_2024]: https://doi.org/10.1109/aero58975.2024.10521242
[research_amato_giannino_2026]: https://doi.org/10.2514/6.2026-5098
[research_ambrosio_camargo_2026]: https://doi.org/10.1007/s40430-026-06481-9
[research_amelin_2022]: https://doi.org/10.18127/j20700784-202212-10
[research_amzajerdian_2016]: https://doi.org/10.2514/6.2016-5591
[research_an_liu_2023]: https://doi.org/10.54254/2755-2721/9/20230063
[research_an_wang_2017]: https://doi.org/10.1016/j.actaastro.2017.06.026
[research_an_wang_2019]: https://doi.org/10.1109/access.2019.2948963
[research_an_wang_2025]: https://doi.org/10.1061/jaeeez.aseng-6056
[research_anand_barman_2020]: https://doi.org/10.1007/978-3-030-34152-7_8
[research_ananda_2017]: https://doi.org/10.2514/6.2017-4077
[research_anatomy_of_2019]: https://doi.org/10.1109/icnsurv.2019.8735188
[research_anderson_1993]: https://ntrs.nasa.gov/citations/20030020362
[research_anderson_kinzel_2023]: https://doi.org/10.2514/6.2023-0391
[research_anderson_loewenson_2021]: https://doi.org/10.2514/6.2021-2798
[research_anderson_schultz_1967]: https://doi.org/10.2514/6.1967-136
[research_anderson_vincent_1983]: https://doi.org/10.2514/6.1983-2746
[research_andert_ammann_2015]: https://doi.org/10.1007/978-3-319-17518-8_35
[research_andreev_stanchev_2020]: https://doi.org/10.1504/ijris.2020.109645
[research_andreeva_mori_nd]: https://ntrs.nasa.gov/citations/20230018557
[research_andrews_1977]: https://ntrs.nasa.gov/citations/19770061462
[research_andrews_1979]: https://doi.org/10.2514/3.55903
[research_andrews_1998]: https://doi.org/10.2514/6.1998-3955
[research_anh_tran_2022]: https://doi.org/10.23890/ijast.vm03is02.0201
[research_anitha_kumar_2012]: https://doi.org/10.1016/j.proeng.2012.06.271
[research_anli_guobinchang_2010]: https://doi.org/10.1109/car.2010.5456846
[research_annaloro_galera_2020]: https://doi.org/10.1016/j.actaastro.2020.03.006
[research_anoshin_bobylev_2012]: https://doi.org/10.1615/tsagiscij.2013007140
[research_ansuyang_zhangfeijuan_2016]: https://doi.org/10.1109/cgncc.2016.7828756
[research_aoki_ishigami_2022]: https://doi.org/10.1080/01691864.2022.2141078
[research_appendix_b_2004]: https://doi.org/10.1049/pbra017e_appendixb
[research_appendix_d_2004]: https://doi.org/10.1049/pbra017e_appendixd
[research_application_of_quasi_object_2008]: https://doi.org/10.18372/1990-5548.18.642
[research_approach_to_2025]: https://doi.org/10.36652/0869-4931-2025-79-3-125-128
[research_aprovitola_iuspa_2019]: https://doi.org/10.5772/intechopen.85603
[research_aprovitola_iuspa_2019_b]: https://doi.org/10.1155/2019/6069528
[research_aradag_seidel_2007]: https://doi.org/10.2514/6.2007-4477
[research_arbic_1955]: https://ntrs.nasa.gov/citations/19690088091
[research_arents_groeneweg_2009]: https://doi.org/10.2514/6.2009-5984
[research_arias_johnson_2022]: https://doi.org/10.2514/6.2022-1641
[research_armstrong_1977]: https://doi.org/10.21236/adb029224
[research_armutcuoglu_kavsaoglu_2004]: https://doi.org/10.2514/1.271
[research_arnaldovaldes_gomezcomendador_2011]: https://doi.org/10.1016/j.ssci.2010.09.020
[research_arnold_1981]: https://doi.org/10.2514/6.1981-2444
[research_arora_ananthasayanam_2003]: https://doi.org/10.2514/6.2003-5547
[research_arora_george_2003]: https://doi.org/10.2514/6.2003-5546
[research_arreolanepomuceno_valdez_2025]: https://doi.org/10.1007/978-3-032-10862-3_15
[research_arrington_1972]: https://ntrs.nasa.gov/citations/19720015257
[research_arshad_kallungal_2021]: https://doi.org/10.1109/icmt52455.2021.9502764
[research_aruna_devi_2012]: https://doi.org/10.1504/ijad.2012.049128
[research_asher_2013]: https://ntrs.nasa.gov/citations/20140010193
[research_ashford_1993]: https://doi.org/10.2514/6.1993-5057
[research_ashikhmina_prosuntsov_2021]: https://doi.org/10.1063/5.0036218
[research_ashkenas_1982]: https://ntrs.nasa.gov/citations/19820055479
[research_ashokgandhi_jayan_2020]: https://doi.org/10.1007/978-981-15-5862-7_30
[research_asl_farahani_2013]: https://doi.org/10.4028/www.scientific.net/amm.307.227
[research_asl_niezrecki_2017]: https://doi.org/10.1007/978-3-319-54858-6_21
[research_asma_vanderhaegen_2010]: https://doi.org/10.2514/6.2010-4963
[research_aso_kumamoto_1993]: https://doi.org/10.2514/6.1993-2984
[research_aspidova_eremin_2022]: https://doi.org/10.1134/s106423072206003x
[research_assessment_of_2015]: https://doi.org/10.21090/ijaerd.020914
[research_assured_crew_1992]: https://ntrs.nasa.gov/citations/19930003722
[research_asthana_bhat_2012]: https://doi.org/10.4028/www.scientific.net/amm.225.275
[research_asyraf_omar_2026]: https://doi.org/10.30880/paat.2026.06.01.005
[research_atmeh_altaq_2011]: https://doi.org/10.1115/imece2011-63264
[research_atmeh_subbarao_2016]: https://doi.org/10.3390/aerospace3010008
[research_attri_1969]: https://doi.org/10.21236/ad0699476
[research_automatic_guidance_2023]: https://doi.org/10.2514/5.9781624106170.0729.0836
[research_automatic_landing_1964]: https://doi.org/10.1108/eb033884
[research_automatic_landing_2007]: https://doi.org/10.5302/j.icros.2007.13.1.039
[research_automatic_landing_2008]: https://doi.org/10.5302/j.icros.2008.14.12.1253
[research_automatic_landing_control_2012]: https://doi.org/10.18372/1990-5548.33.5507
[research_avtin_baburov_2021]: https://doi.org/10.1007/978-981-16-0897-1_5
[research_avtin_baburov_2021_b]: https://doi.org/10.1007/978-981-16-0897-1_7
[research_awin_2013]: https://doi.org/10.4028/www.scientific.net/amm.367.528
[research_azarov_chernovolov_2018]: https://doi.org/10.18577/2071-9140-2018-0-2-75-87
[research_azimov_2013]: https://doi.org/10.2514/6.2013-5258
[research_azinheira_depaiva_2000]: https://doi.org/10.1016/s1474-6670(17)37983-1
[research_baca_stepan_2017]: https://doi.org/10.1109/ecmr.2017.8098700
[research_badarudinmohamadbadry_lee_2013]: https://doi.org/10.1016/j.ast.2013.08.007
[research_badikov_volkova_2026]: https://doi.org/10.1007/978-3-032-05757-0_17
[research_bagai_cantono_2010]: https://doi.org/10.4050/vfs-f66-000080
[research_baggi_2022]: https://doi.org/10.1109/ccta49430.2022.9966141
[research_bai_ren_2014]: https://doi.org/10.1109/chicc.2014.6896993
[research_bailet_denis_2022]: https://doi.org/10.2514/1.a34968
[research_bailey_1982]: https://ntrs.nasa.gov/citations/19830004840
[research_bailey_2025]: https://ntrs.nasa.gov/citations/20250002914
[research_baillif_bodepudi_1995]: https://doi.org/10.2514/6.1995-1330
[research_baimukhametov_white_2026]: https://doi.org/10.1061/9780784487037.091
[research_baker_kramer_1979]: https://doi.org/10.2514/6.1979-201
[research_bakri_nd]: https://doi.org/10.32469/10355/70012
[research_bakulin_borzykh_2016]: https://doi.org/10.3103/s1068799816010049
[research_balakin_elisov_2018]: https://doi.org/10.1063/1.5081577
[research_balakrishnan_kurian_2014]: https://doi.org/10.2514/1.a32712
[research_balas_2003]: https://doi.org/10.3166/ejc.9.207-226
[research_balch_1979]: https://doi.org/10.4050/jahs.24.45
[research_baldini_anandkumar_2020]: https://doi.org/10.23919/acc45564.2020.9147400
[research_balepin_czysz_2001]: https://doi.org/10.2514/2.5870
[research_balint_kaslik_2010]: https://doi.org/10.1016/j.nonrwa.2009.04.017
[research_ball_oittinen_1997]: https://doi.org/10.2514/6.1997-3926
[research_ballard_tanner_2013]: https://doi.org/10.4050/vfs-f69-0173
[research_baluragi_gupta_2011]: https://doi.org/10.1007/s12666-011-0073-x
[research_banerjee_padhi_2015]: https://doi.org/10.1109/cca.2015.7320710
[research_banerjee_padhi_2017]: https://doi.org/10.2514/6.2017-1266
[research_banerjee_padhi_2018]: https://doi.org/10.2514/6.2018-1872
[research_banerjee_poovathingal_2021]: https://doi.org/10.2514/6.2021-1631
[research_banks_2006]: https://ntrs.nasa.gov/citations/20060026026
[research_bannova_2006]: https://doi.org/10.1061/40830(188)121
[research_bantscheff_breitsamter_2023]: https://doi.org/10.3390/aerospace10070581
[research_baradell_1963]: https://doi.org/10.2514/6.1963-1424
[research_baran_blanchard_2014]: https://doi.org/10.2514/6.2014-3548
[research_barber_johari_2001]: https://doi.org/10.2514/6.2001-2074
[research_barbera_1980]: https://doi.org/10.2514/6.1980-1576
[research_barczyk_lynch_2011]: https://doi.org/10.1109/cdc.2011.6160733
[research_baritzhack_porat_1980]: https://doi.org/10.2514/3.55999
[research_barnes_1965]: https://doi.org/10.21236/ad0654783
[research_barnes_mcmichael_2007]: https://doi.org/10.2514/6.2007-2077
[research_barnhart_sullivan_2007]: https://doi.org/10.2514/6.2007-6040
[research_barret_1998]: https://ntrs.nasa.gov/citations/19990103152
[research_barret_1999]: https://doi.org/10.2514/6.1999-382
[research_barthelemy_1989]: https://doi.org/10.2514/6.1989-5053
[research_barton_1985]: https://ntrs.nasa.gov/citations/19860050720
[research_baselga_garciaasenjo_2009]: https://doi.org/10.1017/s0373463309990117
[research_bashir_khan_2017]: https://doi.org/10.14716/ijtech.v8i3.6319
[research_basic_principles_2004]: https://doi.org/10.1049/pbra017e_ch3
[research_batill_1982]: https://doi.org/10.21236/ada122312
[research_batterbee_sims_2007]: https://doi.org/10.1088/0964-1726/16/6/046
[research_bauer_1964]: https://doi.org/10.2514/6.1964-1018
[research_bauer_kummer_1970]: https://doi.org/10.2514/6.1970-273
[research_baumgartner_1995]: https://doi.org/10.2514/6.1995-3531
[research_baumgartner_1997]: https://doi.org/10.1063/1.51920
[research_bayer_1998]: https://doi.org/10.2514/6.1998-1546
[research_baysal_1999]: https://doi.org/10.2514/2.2499
[research_beachem_1964]: https://doi.org/10.21236/ad0601723
[research_beck_driver_2014]: https://doi.org/10.2514/1.a32635
[research_becker_1964]: https://doi.org/10.2514/6.1964-551
[research_bednarcyk_gustafson_2023]: https://doi.org/10.2514/6.2023-0724
[research_bedrov_vadichin_1966]: https://doi.org/10.1007/978-1-4899-6411-3_37
[research_bekar_tanyeri_2025]: https://doi.org/10.3390/aerospace12060501
[research_belabbas_dautermann_2010]: https://doi.org/10.1109/plans.2010.5507312
[research_belcastro_2004]: https://ntrs.nasa.gov/citations/20040074342
[research_bell_1965]: https://doi.org/10.21236/ad0631590
[research_benbow_1971]: https://doi.org/10.2514/6.1971-958
[research_bender_1969]: https://doi.org/10.2514/6.1969-318
[research_benedetto_damico_2014]: https://doi.org/10.1016/j.ssci.2013.09.008
[research_bennett_1947]: https://ntrs.nasa.gov/citations/20050019246
[research_bennett_1947_b]: https://ntrs.nasa.gov/citations/20050028507
[research_bennett_2017]: https://doi.org/10.2514/6.2017-3652
[research_bennett_abel_1981]: https://doi.org/10.2514/6.1981-652
[research_bentley_2009]: https://doi.org/10.1007/978-0-387-76510-5_10
[research_bentley_2009_b]: https://doi.org/10.1007/978-0-387-76510-5_9
[research_bentley_2009_c]: https://doi.org/10.1007/978-0-387-76510-5_5
[research_benton_1989]: https://doi.org/10.2514/3.26063
[research_benyamen_2022]: https://doi.org/10.1109/icuas54217.2022.9836206
[research_berend_talbot_2006]: https://doi.org/10.1016/j.ast.2005.11.004
[research_beresford_asteraki_1961]: https://doi.org/10.1049/pi-b-2.1961.0013
[research_beresh_2022]: https://doi.org/10.2172/2006213
[research_berg_1966]: https://doi.org/10.1109/taes.1966.4501991
[research_berger_tischler_2012]: https://doi.org/10.2514/6.2012-4503
[research_bergeron_tavan_2011]: https://doi.org/10.2514/6.2011-2530
[research_berkes_1992]: https://doi.org/10.1017/s0001924000025070
[research_bernal_yu_2015]: https://doi.org/10.2514/6.2015-0038
[research_berradi_moutaouakkil_2017]: https://doi.org/10.1109/irsec.2017.8477252
[research_berry_1982]: https://ntrs.nasa.gov/citations/19820014377
[research_berry_1999]: https://doi.org/10.4271/1999-01-5523
[research_berry_2000]: https://doi.org/10.2514/6.2000-5601
[research_berry_merski_2002]: https://doi.org/10.2514/6.2002-4701
[research_bertelrud_kolodziej_1992]: https://doi.org/10.2514/6.1992-4104
[research_berthelot_craft_2026]: https://doi.org/10.2514/6.2026-112174
[research_berthold_1977]: https://ntrs.nasa.gov/citations/19770014233
[research_berthold_1977_b]: https://ntrs.nasa.gov/citations/19770014231
[research_bertrandnoel_bignaletcazalet_2022]: https://doi.org/10.1016/j.jsse.2021.12.002
[research_besant_1994]: https://doi.org/10.1007/978-1-4615-2498-4_13
[research_betin_1991]: https://doi.org/10.1016/0265-9646(91)90024-c
[research_betin_2026]: https://doi.org/10.3849/aimt.02050
[research_betin_kaluzhynov_2023]: https://doi.org/10.1007/978-3-031-36201-9_11
[research_betin_kyriienko_2023]: https://doi.org/10.1007/978-3-031-36201-9_4
[research_bettinger_2021]: https://doi.org/10.1016/j.asr.2021.01.056
[research_bettis_hosder_2010]: https://doi.org/10.2514/6.2010-4642
[research_beyers_ericsson_1997]: https://doi.org/10.2514/6.1997-730
[research_bhagat_glussich_2011]: https://doi.org/10.1177/1071181311551358
[research_bhatia_geller_2020]: https://doi.org/10.1002/navi.397
[research_bhungalia_clewitt_2004]: https://doi.org/10.2514/6.2004-5826
[research_bian_li_2024]: https://doi.org/10.1007/978-981-99-5636-4_8
[research_bian_nener_2018]: https://doi.org/10.1080/00207179.2018.1473643
[research_biannic_roos_2018]: https://doi.org/10.3390/aerospace5010018
[research_bickford_bickmore_1997]: https://doi.org/10.2514/6.1997-2901
[research_bieniawski_rosenzweig_2014]: https://doi.org/10.2514/6.2014-1457
[research_bifurcation_analysis_2004]: https://doi.org/10.1201/9780203298916-7
[research_bigot_2025]: https://doi.org/10.5194/epsc-dps2025-690
[research_bihrle_1976]: https://ntrs.nasa.gov/citations/19760020126
[research_bin_hongxin_2006]: https://doi.org/10.1109/chicc.2006.4346800
[research_binns_englehart_1996]: https://doi.org/10.1142/s0218194096000107
[research_binz_hartmann_2017]: https://doi.org/10.1007/978-3-319-65283-2_20
[research_birkeland_meuser_1999]: https://doi.org/10.2514/6.1999-4463
[research_bischoff_duffy_1974]: https://doi.org/10.2514/3.60378
[research_bishop_crain_2016]: https://doi.org/10.2514/6.2016-0098
[research_bizzarri_hendrick_2003]: https://doi.org/10.2514/6.2003-6930
[research_black_1964]: https://doi.org/10.2514/3.27626
[research_black_1968]: https://doi.org/10.2514/6.1968-361
[research_blackmore_acikmese_2010]: https://doi.org/10.2514/1.47202
[research_blackstock_1970]: https://doi.org/10.2514/3.30113
[research_blades_redgrave_2000]: https://doi.org/10.2514/6.2000-1778
[research_blanchard_1961]: https://ntrs.nasa.gov/citations/19980228014
[research_bledsoe_2011]: https://ntrs.nasa.gov/citations/20110011029
[research_bledsoe_2015]: https://ntrs.nasa.gov/citations/20150003470
[research_bleimeyer_1981]: https://doi.org/10.2514/6.1981-2515
[research_blevins_mckinnis_2022]: https://doi.org/10.2514/6.2022-2292
[research_bliamis_panagiotou_2018]: https://doi.org/10.2514/6.2018-5376
[research_blodgett_conrad_1986]: https://doi.org/10.2514/6.1986-9821
[research_blom_2017]: https://doi.org/10.1109/icnsurv.2017.8012008
[research_blonigan_tencer_2025]: https://doi.org/10.2514/6.2025-2133
[research_blosser_1997]: https://doi.org/10.1063/1.51930
[research_blosser_2002]: https://doi.org/10.2514/6.2002-503
[research_blosser_2004]: https://doi.org/10.2514/1.9182
[research_bo_xiaogang_2020]: https://doi.org/10.1155/2020/1420393
[research_bo_yuan_2017]: https://doi.org/10.2514/6.2017-2172
[research_bobko_2012]: https://ntrs.nasa.gov/citations/20120016871
[research_bobylev_dyadkin_2008]: https://doi.org/10.1134/s0010952508010097
[research_bodkin_akamine_2024]: https://doi.org/10.2514/6.2024-1310
[research_bogar_butters_1996]: https://doi.org/10.2514/6.1996-4570
[research_bohn_1970]: https://ntrs.nasa.gov/citations/19700016796
[research_bohon_sawyer_1975]: https://doi.org/10.2514/3.57043
[research_bohon_shideler_1977]: https://doi.org/10.2514/3.57244
[research_boisseau_1955]: https://ntrs.nasa.gov/citations/20050029385
[research_bolender_doman_2005]: https://doi.org/10.21236/ada444974
[research_bolt_1981]: https://doi.org/10.2514/6.1981-2394
[research_bonetti_dezaiacomo_2013]: https://doi.org/10.2514/6.2013-5021
[research_bonnal_caporicci_2000]: https://doi.org/10.1016/s0094-5765(00)00050-3
[research_bonner_1976]: https://ntrs.nasa.gov/citations/19760026053
[research_boothe_chen_1974]: https://doi.org/10.21236/ad0782218
[research_borden_1999]: https://ntrs.nasa.gov/citations/19990070318
[research_borges_burnside_2026]: https://doi.org/10.1109/sieds69358.2026.11540136
[research_borodin_2001]: https://doi.org/10.1023/a:1019298109749
[research_borowczyk_nguyen_2017]: https://doi.org/10.1016/j.ifacol.2017.08.1980
[research_borowczyk_nguyen_2017_b]: https://doi.org/10.2514/1.g002703
[research_borzykh_voronin_2013]: https://doi.org/10.18287/1998-6629-2013-0-4(42)-86-93
[research_boschetti_cardenas_2004]: https://doi.org/10.2514/6.2004-4969
[research_boskovic_redding_2009]: https://doi.org/10.2514/6.2009-6264
[research_bossi_1989]: https://ntrs.nasa.gov/citations/19900006621
[research_bossi_1991]: https://ntrs.nasa.gov/citations/19910008803
[research_bourne_1983]: https://ntrs.nasa.gov/citations/19840002076
[research_bouslog_1998]: https://ntrs.nasa.gov/citations/19980200836
[research_bouslog_an_1993]: https://doi.org/10.2514/6.1993-2763
[research_bouyahiaoui_haoui_2020]: https://doi.org/10.1016/j.ijheatmasstransfer.2019.119045
[research_bovais_haupt_1992]: https://doi.org/10.2514/6.1992-4079
[research_boye_2020]: https://doi.org/10.1109/aero47225.2020.9172642
[research_boyer_1964]: https://doi.org/10.2514/6.1964-1121
[research_boylan_1965]: https://doi.org/10.21236/ad0460154
[research_brady_1969]: https://doi.org/10.4050/jahs.14.48
[research_brand_1981]: https://ntrs.nasa.gov/citations/19830035754
[research_brando_dannier_2016]: https://doi.org/10.1109/speedam.2016.7525892
[research_brandon_1996]: https://ntrs.nasa.gov/citations/19960028603
[research_brandon_1997]: https://ntrs.nasa.gov/citations/19980001023
[research_brandt_mclaughlin_2019]: https://doi.org/10.2514/6.2019-0283
[research_brassard_laforte_2019]: https://doi.org/10.4271/2019-01-1974
[research_bratt_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50016-6
[research_braun_1958]: https://doi.org/10.21236/ad0202249
[research_brennan_mcdaniel_1994]: https://doi.org/10.21236/ada284253
[research_brevault_balesdent_2019]: https://doi.org/10.2514/6.2019-0704
[research_brevault_balesdent_2020]: https://doi.org/10.1007/978-3-030-39126-3_12
[research_brevault_balesdent_2020_b]: https://doi.org/10.2514/1.a34601
[research_brice_perkins_1966]: https://doi.org/10.21236/ad0801520
[research_brice_sugano_1978]: https://doi.org/10.2514/6.1978-1446
[research_brieger_ossmann_2008]: https://doi.org/10.2514/6.2008-6556
[research_briggs_1952]: https://ntrs.nasa.gov/citations/19930086880
[research_brinda_arora_2005]: https://doi.org/10.2514/6.2005-3291
[research_brinda_dasgupta_2006]: https://doi.org/10.2514/1.23221
[research_brink_hurtado_2010]: https://doi.org/10.2514/6.2010-3403
[research_brion_aki_2006]: https://doi.org/10.2514/6.2006-3864
[research_britcher_datta_2024]: https://doi.org/10.4050/f-0080-2024-1339
[research_britcher_landman_2024]: https://doi.org/10.1016/b978-0-12-818099-0.00005-7
[research_brociek_hetmaniok_2023]: https://doi.org/10.1016/j.applthermaleng.2022.119405
[research_brock_franke_2004]: https://doi.org/10.2514/6.2004-3903
[research_brock_nd]: https://ntrs.nasa.gov/citations/20220001764
[research_brockers_2012]: https://ntrs.nasa.gov/citations/20130010537
[research_broglio_1961]: https://doi.org/10.21236/ad0294976
[research_brooks_1986]: https://doi.org/10.2514/6.1986-9796
[research_brooks_swann_1962]: https://doi.org/10.4271/620484
[research_broussard_bryant_1983]: https://doi.org/10.23919/acc.1983.4788169
[research_brown_1948]: https://doi.org/10.21236/adb812167
[research_brown_1983]: https://ntrs.nasa.gov/citations/19830018574
[research_brown_1984]: https://ntrs.nasa.gov/citations/19840024323
[research_brown_2023]: https://doi.org/10.18278/sesa.4.1.5
[research_brown_duhon_1965]: https://doi.org/10.2514/6.1965-209
[research_brown_olds_2005]: https://doi.org/10.2514/6.2005-707
[research_brown_olds_2006]: https://doi.org/10.2514/1.16577
[research_brown_yates_2002]: https://doi.org/10.2514/6.2002-4410
[research_brown_yates_2006]: https://doi.org/10.2514/1.19221
[research_bruce_1964]: https://doi.org/10.21236/ad0602669
[research_bruckner_vangraas_2010]: https://doi.org/10.1007/s10291-010-0193-5
[research_brunch_gilbreath_2002]: https://doi.org/10.21236/ada422034
[research_brune_hosder_2017]: https://doi.org/10.2514/1.a33732
[research_brunner_kiefer_2021]: https://doi.org/10.1007/s00348-021-03267-8
[research_brusa_delprete_2025]: https://doi.org/10.1109/isse65546.2025.11370106
[research_bryant_tigges_1998]: https://doi.org/10.2514/6.1998-4572
[research_brysonjr_1969]: https://doi.org/10.2514/6.1969-865
[research_brzozowski_kordowski_2014]: https://doi.org/10.1109/metroaerospace.2014.6865895
[research_bu_ai_2016]: https://doi.org/10.1109/icves.2016.7548174
[research_bu_lei_2019]: https://doi.org/10.1016/j.actaastro.2019.05.039
[research_buchnev_danilov_2026]: https://doi.org/10.32743/unitech.2026.147.6.23019
[research_budd_1993]: https://ntrs.nasa.gov/citations/19930009427
[research_buell_1959]: https://ntrs.nasa.gov/citations/19650018601
[research_buell_oleinik_1998]: https://doi.org/10.1002/j.2161-4296.1998.tb02380.x
[research_bufalino_1995]: https://doi.org/10.2514/6.1995-3899
[research_buffo_1990]: https://doi.org/10.2514/6.1990-3674
[research_bugg_1967]: https://ntrs.nasa.gov/citations/19670019428
[research_buhler_1969]: https://ntrs.nasa.gov/citations/19700010491
[research_bukov_bykov_2017]: https://doi.org/10.1134/s1064230717040062
[research_bull_1981]: https://ntrs.nasa.gov/citations/19810010516
[research_bull_foster_1974]: https://doi.org/10.2514/6.1974-811
[research_bulmer_1973]: https://doi.org/10.2514/3.50699
[research_bunge_munerasavino_2015]: https://doi.org/10.2514/6.2015-3225
[research_burchett_2004]: https://doi.org/10.2514/1.10938
[research_burgan_1974]: https://doi.org/10.21236/ada000101
[research_burgess_1970]: https://doi.org/10.1017/s0001924000048016
[research_burkhardt_graesslin_1999]: https://doi.org/10.2514/6.1999-4167
[research_burkhart_2013]: https://ntrs.nasa.gov/citations/20150005559
[research_burns_1970]: https://doi.org/10.2514/6.1970-587
[research_burnsiii_1992]: https://doi.org/10.2514/6.1992-1211
[research_burt_haigh_1968]: https://doi.org/10.2514/6.1968-387
[research_burton_1981]: https://doi.org/10.21236/ada097744
[research_bushnell_2006]: https://doi.org/10.1146/annurev.fluid.38.050304.092208
[research_busnardo_aitken_2011]: https://doi.org/10.2514/6.2011-428
[research_butt_2013]: https://doi.org/10.21307/ijssis-2017-560
[research_butt_yan_2010]: https://doi.org/10.1109/cdc.2010.5717701
[research_butt_yan_2011]: https://doi.org/10.1002/asjc.450
[research_butt_yan_2011_b]: https://doi.org/10.3182/20110828-6-it-1002.00534
[research_butt_yan_2013]: https://doi.org/10.1080/00207721.2013.828798
[research_butter_2017]: https://doi.org/10.1201/9781315210469-150
[research_byrne_sturgis_1996]: https://doi.org/10.2514/6.1996-3438
[research_c_vinaykumar_2024]: https://doi.org/10.4271/2024-26-0434
[research_ca_1963]: https://doi.org/10.21236/ad0426250
[research_ca_1963_b]: https://doi.org/10.21236/ad0406168
[research_cabuk_2021]: https://doi.org/10.31202/ecjse.952728
[research_cabuk_2023]: https://doi.org/10.1007/s13369-023-07731-x
[research_cady_1997]: https://doi.org/10.1063/1.52034
[research_cady_olsen_1996]: https://doi.org/10.2514/6.1996-3011
[research_cai_gao_2025]: https://doi.org/10.1109/jsen.2024.3519880
[research_cai_jianmei_2013]: https://doi.org/10.2514/6.2013-4525
[research_cai_lei_2024]: https://doi.org/10.1007/s42405-024-00786-6
[research_cai_song_2013]: https://doi.org/10.1177/0954410013486239
[research_cai_song_2014]: https://doi.org/10.1177/0954410014555894
[research_cai_yang_2024]: https://doi.org/10.3390/aerospace11120975
[research_cain_snelling_2022]: https://doi.org/10.1109/aero53065.2022.9843496
[research_calhoun_2000]: https://doi.org/10.2514/6.2000-1046
[research_calise_bae_1987]: https://doi.org/10.2514/6.1987-2568
[research_call_kelly_1981]: https://doi.org/10.2514/6.1981-2403
[research_callerio_1940]: https://ntrs.nasa.gov/citations/19930094479
[research_campbell_1943]: https://ntrs.nasa.gov/citations/19930091848
[research_campbell_1991]: https://doi.org/10.1088/2058-7058/4/10/9
[research_campbell_kresge_2003]: https://doi.org/10.1109/dasc.2003.1245892
[research_campbell_lee_2007]: https://doi.org/10.2514/1.29719
[research_campi_cruciani_2019]: https://doi.org/10.3390/en12183483
[research_camponogara_oliveira_2019]: https://doi.org/10.1109/taes.2019.2913613
[research_campos_1989]: https://doi.org/10.1017/s0001924000022090
[research_canniff_1969]: https://doi.org/10.2514/6.1969-842
[research_cao_ding_2012]: https://doi.org/10.1109/ibcast.2012.6177533
[research_cao_zhang_2015]: https://doi.org/10.1109/icspcc.2015.7338798
[research_cao_zhou_2024]: https://doi.org/10.1007/978-981-97-3998-1_131
[research_caogen_hongjun_2008]: https://doi.org/10.1016/j.actaastro.2007.12.059
[research_capderou_2012]: https://doi.org/10.1007/978-2-287-99050-2_14
[research_cappello_sabatini_2016]: https://doi.org/10.1109/icuas.2016.7502644
[research_carloni_bousson_2016]: https://doi.org/10.15866/irece.v7i4.10757
[research_carman_1980]: https://ntrs.nasa.gov/citations/19800019907
[research_carman_1980_b]: https://ntrs.nasa.gov/citations/19800016874
[research_carman_1980_c]: https://ntrs.nasa.gov/citations/19800018908
[research_carman_jb_1980]: https://doi.org/10.21236/ada087561
[research_carnes_bakker_2015]: https://doi.org/10.2514/6.2015-0603
[research_carpenter_chocron_2019]: https://doi.org/10.1115/hvis2019-063
[research_carrawayiii_1988]: https://doi.org/10.2514/6.1988-4669
[research_carson_robertson_2015]: https://doi.org/10.2514/6.2015-4417
[research_carten_1978]: https://doi.org/10.21236/ada057610
[research_cassanto_1966]: https://doi.org/10.2514/3.28728
[research_cassell_2019]: https://ntrs.nasa.gov/citations/20190031937
[research_castaldi_emami_2023]: https://doi.org/10.1016/j.ifacol.2023.10.654
[research_castro_bennani_2006]: https://doi.org/10.1109/cacsd-cca-isic.2006.4777166
[research_cavallo_demaria_1996]: https://doi.org/10.2514/3.21704
[research_cavallo_ferrara_1996]: https://doi.org/10.2514/3.21578
[research_cavdar_mooij_2024]: https://doi.org/10.2514/6.2024-1458
[research_caves_kirkland_1999]: https://doi.org/10.3141/1662-08
[research_cazin_1989]: https://doi.org/10.2514/6.1989-5020
[research_cejpek_2018]: https://doi.org/10.1108/aeat-11-2016-0216
[research_cesetti_frontoni_2009]: https://doi.org/10.1109/med.2009.5164661
[research_cetin_aygun_2024]: https://doi.org/10.56753/asrel.2024.2.3
[research_cetin_kurnaz_2010]: https://doi.org/10.1007/978-94-007-1110-5_16
[research_cetin_kutay_2016]: https://doi.org/10.1109/icmae.2016.7549576
[research_cetinkaya_ozkol_2017]: https://doi.org/10.1109/icmae.2017.8038678
[research_chae_mankodi_2019]: https://doi.org/10.1007/s42405-019-00243-9
[research_chai_mason_1996]: https://doi.org/10.2514/6.1996-4038
[research_chai_savvaris_2017]: https://doi.org/10.1109/taes.2017.2680698
[research_chai_savvaris_2019]: https://doi.org/10.1007/978-981-13-9845-2_7
[research_chai_savvaris_2019_b]: https://doi.org/10.1109/tcyb.2017.2778195
[research_chaloff_1974]: https://doi.org/10.21236/ada002858
[research_chamberlin_blaha_1973]: https://doi.org/10.2514/6.1973-139
[research_chambers_1980]: https://doi.org/10.1016/b978-0-08-024449-5.50021-7
[research_chambers_1981]: https://ntrs.nasa.gov/citations/19810022574
[research_chambers_1988]: https://ntrs.nasa.gov/citations/19880051465
[research_chambers_2010]: https://ntrs.nasa.gov/citations/20110012492
[research_chambers_titchener_2019]: https://doi.org/10.2514/6.2019-2101
[research_chamitoff_1994]: https://doi.org/10.1016/s1474-6670(17)45823-x
[research_chamitoff_1995]: https://doi.org/10.1016/b978-0-08-042238-1.50057-4
[research_chan_pervan_2011]: https://doi.org/10.1017/s0373463311000038
[research_chan_shea_2023]: https://doi.org/10.2514/6.2023-0425
[research_chandramohan_yucelen_2010]: https://doi.org/10.2514/6.2010-7574
[research_chang_2016]: https://doi.org/10.2991/amsm-16.2016.52
[research_chang_guo_2018]: https://doi.org/10.1016/j.ifacol.2018.09.668
[research_chang_huang_2022]: https://doi.org/10.3390/aerospace10010001
[research_chang_miao_2018]: https://doi.org/10.1109/gncc42960.2018.9018895
[research_chang_ryu_2015]: https://doi.org/10.5139/jksas.2015.43.12.1089
[research_chang_seo_2026]: https://doi.org/10.2514/6.2026-5119
[research_chang_yang_2016]: https://doi.org/10.1016/j.aap.2016.06.007
[research_chang_yee_2021]: https://doi.org/10.2514/6.2021-0671
[research_changsheng_wuxing_2006]: https://doi.org/10.1109/chicc.2006.4347462
[research_channon_barry_1967]: https://doi.org/10.2514/6.1967-1125
[research_chao_2017]: https://doi.org/10.2514/6.2017-1631
[research_chapman_1964]: https://ntrs.nasa.gov/citations/19640007103
[research_chapteer_8_2008]: https://doi.org/10.4324/9780203305225-11
[research_chapter_12_2013]: https://doi.org/10.1615/978-1-56700-309-3.234
[research_chapter_13_2013]: https://doi.org/10.1615/978-1-56700-309-3.236
[research_chapter_6_2012]: https://doi.org/10.1515/9781400841660.155
[research_charette_leonard_1998]: https://doi.org/10.1063/1.54896
[research_charters_1955]: https://ntrs.nasa.gov/citations/19930093745
[research_charters_1962]: https://doi.org/10.1515/9781400875030-017
[research_chase_1996]: https://doi.org/10.4271/965565
[research_chase_1997]: https://doi.org/10.1063/1.52112
[research_chase_chase_1997]: https://doi.org/10.2514/6.1997-2980
[research_chase_mckinney_1997]: https://doi.org/10.2514/6.1997-5630
[research_chase_mckinney_2005]: https://doi.org/10.2514/6.2005-6745
[research_chatterji_menon_1995]: https://doi.org/10.2514/6.1995-3196
[research_chaudhary_2001]: https://ntrs.nasa.gov/citations/20020023442
[research_chavagnac_2003]: https://doi.org/10.2514/6.2003-6983
[research_chavagnac_gai_2013]: https://doi.org/10.1016/j.actaastro.2012.09.001
[research_chawla_sarmah_2010]: https://doi.org/10.1016/j.ast.2010.04.001
[research_che_liu_2012]: https://doi.org/10.1007/978-3-642-29187-6_60
[research_chedrik_2004]: https://doi.org/10.2514/6.2004-4642
[research_chelnokov_2019]: https://doi.org/10.23919/icins.2019.8769350
[research_chelnokov_perelyaev_2020]: https://doi.org/10.23919/icins43215.2020.9133921
[research_chen_2013]: https://ntrs.nasa.gov/citations/20150007791
[research_chen_2013_b]: https://ntrs.nasa.gov/citations/20150007796
[research_chen_2018]: https://doi.org/10.23940/ijpe.18.09.p2.19471957
[research_chen_2021]: https://doi.org/10.1109/wcmeim54377.2021.00034
[research_chen_2023]: https://doi.org/10.54097/6rbgfh93
[research_chen_blosser_2002]: https://doi.org/10.2514/6.2002-501
[research_chen_chang_2021]: https://doi.org/10.1007/s10291-021-01144-9
[research_chen_han_2023]: https://doi.org/10.1007/978-981-19-6613-2_212
[research_chen_he_2025]: https://doi.org/10.1177/16878132251348391
[research_chen_huang_2025]: https://doi.org/10.1109/cac67268.2025.11487626
[research_chen_li_2016]: https://doi.org/10.1109/cgncc.2016.7828876
[research_chen_ma_2018]: https://doi.org/10.1093/imamci/dny012
[research_chen_man_2022]: https://doi.org/10.1109/iccasit55263.2022.9986874
[research_chen_mu_2018]: https://doi.org/10.1117/12.2317531
[research_chen_nie_2013]: https://doi.org/10.21595/jve.2013.14589
[research_chen_shi_2025]: https://doi.org/10.1049/cth2.70002
[research_chen_squire_2006]: https://doi.org/10.2514/6.2006-2951
[research_chen_wang_2023]: https://doi.org/10.1007/978-981-19-6613-2_154
[research_chen_wu_2025]: https://doi.org/10.1109/isaes66870.2025.11274377
[research_chen_xue_2023]: https://doi.org/10.1080/13588265.2023.2242102
[research_chen_yang_2025]: https://doi.org/10.34133/space.0260
[research_chen_yu_2011]: https://doi.org/10.1109/imtc.2011.5944155
[research_chen_zhou_2020]: https://doi.org/10.1007/978-981-15-8901-0_13
[research_chen_zhou_2020_b]: https://doi.org/10.1007/978-981-15-8901-0_10
[research_chen_zhou_2020_c]: https://doi.org/10.1007/978-981-15-8901-0_11
[research_chen_zhou_2020_d]: https://doi.org/10.1007/978-981-15-8901-0_9
[research_chen_zhou_2020_e]: https://doi.org/10.1007/978-981-15-8901-0_7
[research_chen_zhu_2016]: https://doi.org/10.1109/chicc.2016.7555061
[research_chen_zhu_2025]: https://doi.org/10.23919/ccc64809.2025.11179204
[research_cheney_1988]: https://doi.org/10.2514/6.1988-2125
[research_cheney_pham_1988]: https://doi.org/10.2514/6.1988-2126
[research_cheng_hu_2023]: https://doi.org/10.1109/cac59555.2023.10451262
[research_cheng_jing_2021]: https://doi.org/10.1016/j.ast.2021.106965
[research_cheng_lai_2025]: https://doi.org/10.1002/rob.70147
[research_cheng_li_2014]: https://doi.org/10.2514/1.a32580
[research_cheng_sheng_2016]: https://doi.org/10.1109/chicc.2016.7555053
[research_cheng_shyur_2025]: https://doi.org/10.1007/978-981-96-1235-2_8
[research_cheng_wang_2026]: https://doi.org/10.1002/pc.71385
[research_chenliu_chaoyangdong_2016]: https://doi.org/10.1109/cgncc.2016.7829094
[research_chensongyue_wangliang_2018]: https://doi.org/10.1049/cp.2018.0351
[research_chernenko_burnashev_2022]: https://doi.org/10.20535/0203-3771422021268461
[research_chernodarov_patrikeev_2021]: https://doi.org/10.23919/icins43216.2021.9470815
[research_chernodarov_patrikeev_2022]: https://doi.org/10.23919/icins51784.2022.9815376
[research_chernyi_gonor_1973]: https://doi.org/10.1007/978-94-010-2559-1_11
[research_chevalier_dubroca_2026]: https://doi.org/10.2514/1.a36307
[research_chhetri_jetawatthana_2026]: https://doi.org/10.1142/s230138502830003x
[research_chi_xiaopeng_2009]: https://doi.org/10.1109/icicta.2009.242
[research_chiba_obayashi_2006]: https://doi.org/10.2514/1.12782
[research_chiesa_cardile_2012]: https://doi.org/10.2514/6.2012-5924
[research_chiesa_corpino_2005]: https://doi.org/10.2514/6.2005-3345
[research_chiesa_grassi_2005]: https://doi.org/10.2514/6.2005-3346
[research_childers_2001]: https://ntrs.nasa.gov/citations/20020022180
[research_chimonas_1986]: https://doi.org/10.1029/jd091id13p14557
[research_chin_1970]: https://ntrs.nasa.gov/citations/19700028517
[research_chin_1985]: https://doi.org/10.2514/6.1985-1878
[research_chin_hearne_1964]: https://doi.org/10.2514/6.1964-1311
[research_chinnaraj_kim_2024]: https://doi.org/10.3390/ma17215229
[research_chinvorarat_2021]: https://doi.org/10.2139/ssrn.3877178
[research_chinvorarat_vallikul_2021]: https://doi.org/10.1108/aeat-10-2020-0237
[research_chirayath_bindu_2014]: https://doi.org/10.1109/epscicon.2014.6887480
[research_chitrakaran_dawson_2005]: https://doi.org/10.21236/ada465706
[research_chiu_pitts_1991]: https://doi.org/10.2514/6.1991-695
[research_cho_1995]: https://doi.org/10.2514/6.1995-560
[research_choi_lim_2005]: https://doi.org/10.1007/978-3-540-30585-9_12
[research_choo_mun_2018]: https://doi.org/10.6108/kspe.2018.22.2.138
[research_choong_lim_2026]: https://doi.org/10.1007/978-3-032-08476-7_66
[research_chowdhary_johnson_2008]: https://doi.org/10.2514/6.2008-6781
[research_chowdhury_joshi_2026]: https://doi.org/10.5220/0014326200004052
[research_chowdhury_keshmiri_2022]: https://doi.org/10.1109/aero53065.2022.9843777
[research_christol_1993]: https://doi.org/10.1016/0265-9646(93)90007-v
[research_christoph_1985]: https://doi.org/10.2514/6.1985-905
[research_chu_guo_2016]: https://doi.org/10.1109/aus.2016.7748119
[research_chu_li_2017]: https://doi.org/10.2991/icmeit-17.2017.130
[research_chu_liu_2024]: https://doi.org/10.1061/jitse4.iseng-2419
[research_chu_lv_2025]: https://doi.org/10.3390/biomimetics10050327
[research_chu_mooij_2001]: https://doi.org/10.2514/6.2001-4169
[research_chuang_yubing_2021]: https://doi.org/10.1049/icp.2021.0146
[research_chudej_1994]: https://doi.org/10.1007/bfb0035498
[research_chung_echigo_2025]: https://doi.org/10.2514/6.2025-1897
[research_clancy_2001]: https://doi.org/10.1007/978-1-4471-0275-5_1
[research_clapp_1965]: https://doi.org/10.2514/6.1965-492
[research_clapp_1995]: https://doi.org/10.2514/6.1995-2955
[research_clark_dicus_1978]: https://doi.org/10.1007/978-1-4615-9083-5_41
[research_clarke_randall_1997]: https://doi.org/10.1117/12.280372
[research_clary_1984]: https://ntrs.nasa.gov/citations/19840016498
[research_clary_1984_b]: https://ntrs.nasa.gov/citations/19840063562
[research_clayton_tinker_1992]: https://doi.org/10.2514/3.11516
[research_clemmons_1971]: https://doi.org/10.2514/3.59170
[research_cliff_well_1992]: https://doi.org/10.2514/6.1992-4301
[research_closcot_templai_2018]: https://doi.org/10.1109/aero.2018.8396467
[research_clough_1990]: https://doi.org/10.2514/6.1990-3307
[research_cocchioni_mancini_2014]: https://doi.org/10.1109/icuas.2014.6842282
[research_cochran_1978]: https://doi.org/10.21236/ada061109
[research_cochran_1979]: https://doi.org/10.21236/ada080606
[research_cochrane_1971]: https://ntrs.nasa.gov/citations/19720018319
[research_cockayne_1971]: https://ntrs.nasa.gov/citations/19720017949
[research_cohanim_2009]: https://doi.org/10.2514/1.42002
[research_cohen_parkinson_1994]: https://doi.org/10.1002/j.2161-4296.1994.tb02323.x
[research_cohen_pervan_1994]: https://doi.org/10.1002/j.2161-4296.1994.tb02568.x
[research_coker_hoffman_1978]: https://doi.org/10.21236/ada070376
[research_colgren_1996]: https://doi.org/10.2514/6.1996-3743
[research_collicott_woffinden_2021]: https://doi.org/10.2514/6.2021-0375
[research_collinson_1963]: https://doi.org/10.1017/s0373463300020506
[research_colwell_1966]: https://doi.org/10.1108/eb034185
[research_comer_atkinson_2026]: https://doi.org/10.2514/6.2026-2063
[research_comer_bhandari_2024]: https://doi.org/10.2514/6.2024-2644
[research_comer_chakraborty_2026]: https://doi.org/10.2514/1.g009060
[research_computer_vision_2025]: https://doi.org/10.31673/2412-4338.2025.038701
[research_condomines_2018]: https://doi.org/10.1016/b978-1-78548-285-4.50003-5
[research_constantin_2022]: https://doi.org/10.2514/6.2022-2133
[research_contreras_hajiyev_2019]: https://doi.org/10.24425/mms.2019.129586
[research_control_and_1998]: https://doi.org/10.2514/5.9781600861697.0049.0098
[research_cook_1981]: https://doi.org/10.2514/6.1981-2380
[research_cook_1984]: https://ntrs.nasa.gov/citations/19860017820
[research_cook_1995]: https://doi.org/10.2514/6.1995-6153
[research_cook_1996]: https://doi.org/10.2514/6.1996-4563
[research_cooper_miserentino_1984]: https://doi.org/10.2514/3.25678
[research_coopmans_podhradsky_2015]: https://doi.org/10.1109/red-uas.2015.7440998
[research_corban_gilbert_2001]: https://doi.org/10.21236/ada415546
[research_corban_gilbert_2004]: https://doi.org/10.21236/ada433221
[research_cordes_hertzfeld_1997]: https://doi.org/10.1016/s0265-9646(97)00006-4
[research_cordoba_2007]: https://doi.org/10.3182/20070625-5-fr-2916.00007
[research_cork_moore_1967]: https://doi.org/10.2514/6.1967-619
[research_cornelison_1997]: https://ntrs.nasa.gov/citations/20020048460
[research_corso_2015]: https://ntrs.nasa.gov/citations/20160006468
[research_coskun_genc_2021]: https://doi.org/10.1109/eurocon52738.2021.9535625
[research_costa_sachs_2002]: https://doi.org/10.2514/6.2002-4848
[research_coue_2003]: https://doi.org/10.2514/6.iac-03-iaa.2.p.02
[research_courtin_hansman_2020]: https://doi.org/10.2514/6.2020-0977
[research_coutinho_baptista_2016]: https://doi.org/10.1016/j.engstruct.2016.04.016
[research_cowart_olds_2000]: https://doi.org/10.2514/6.2000-5265
[research_cowling_2011]: https://doi.org/10.2514/6.2011-2370
[research_cox_1978]: https://doi.org/10.1002/j.2161-4296.1978.tb01335.x
[research_cox_cunningham_2012]: https://doi.org/10.2514/6.2012-5029
[research_crain_2016]: https://ntrs.nasa.gov/citations/20170009198
[research_crassidis_2005]: https://doi.org/10.2514/6.2005-6052
[research_crassidis_mook_1991]: https://doi.org/10.2514/6.1991-2666
[research_crassidis_mook_1992]: https://doi.org/10.2514/6.1992-4619
[research_crassidis_mook_1993]: https://doi.org/10.2514/3.21101
[research_crawford_1973]: https://ntrs.nasa.gov/citations/19760008154
[research_crespillo_grosch_2016]: https://doi.org/10.1109/icnsurv.2016.7486340
[research_crist_symes_1981]: https://doi.org/10.21236/ada105512
[research_crogan_1961]: https://doi.org/10.21236/ad0323887
[research_croke_green_2024]: https://doi.org/10.4050/f-0080-2024-1228
[research_cronin_2013]: https://doi.org/10.21236/ada594988
[research_croom_1966]: https://ntrs.nasa.gov/citations/19660028846
[research_croom_2000]: https://ntrs.nasa.gov/citations/20000091591
[research_cross_1989]: https://doi.org/10.1007/978-3-642-84010-4_29
[research_crouch_1999]: https://doi.org/10.1086/384495
[research_cruz_green_2019]: https://doi.org/10.2514/6.2019-2898
[research_cruz_nd]: https://ntrs.nasa.gov/citations/20240007788
[research_cruz_nd_b]: https://ntrs.nasa.gov/citations/20220005262
[research_cui_chen_2022]: https://doi.org/10.1109/ddcls55054.2022.9858388
[research_cui_li_2026]: https://doi.org/10.1002/acs.70086
[research_cui_zhang_2021]: https://doi.org/10.1145/3463858.3463884
[research_cui_zhao_2017]: https://doi.org/10.1016/j.applthermaleng.2017.06.113
[research_cui_zhen_2025]: https://doi.org/10.1002/rnc.8012
[research_culler_williams_2007]: https://doi.org/10.2514/6.2007-6395
[research_cummings_2003]: https://doi.org/10.2514/6.2003-233
[research_cunningham_foster_2008]: https://doi.org/10.2514/6.2008-6200
[research_currey_1969]: https://doi.org/10.1016/s0010-4485(69)80081-3
[research_currin_2011]: https://ntrs.nasa.gov/citations/20120000402
[research_curtin_2026]: https://doi.org/10.2514/6.2026-112716
[research_curtis_2005]: https://doi.org/10.2514/6.2005-6282
[research_curtiss_1988]: https://ntrs.nasa.gov/citations/19880064556
[research_cusick_kontis_2019]: https://doi.org/10.2514/6.2019-2929
[research_cvrlje_1999]: https://doi.org/10.2514/6.1999-3412
[research_czysz_murthy_1996]: https://doi.org/10.2514/6.1996-4574
[research_dabas_sheikh_2025]: https://doi.org/10.52202/083092-0073
[research_dacosta_2003]: https://doi.org/10.2514/6.iac-03-v.p.10
[research_dacosta_sachs_2002]: https://doi.org/10.2514/6.2002-5219
[research_dacosta_sachs_2003]: https://doi.org/10.2514/6.2003-7079
[research_dai_li_2010]: https://doi.org/10.1109/aici.2010.162
[research_dai_liu_2017]: https://doi.org/10.23919/chicc.2017.8027911
[research_dai_sun_2023]: https://doi.org/10.1007/978-981-99-6944-9_48
[research_dai_tan_2018]: https://doi.org/10.1109/inertialsensors.2018.8577165
[research_daidzic_2016]: https://doi.org/10.15394/ijaaa.2016.1116
[research_dalang_kulathunga_2023]: https://doi.org/10.1109/icacr59381.2023.10314602
[research_damping_an_1962]: https://doi.org/10.2514/5.9781600864827.0325.0348
[research_dana_1969]: https://ntrs.nasa.gov/citations/19690020352
[research_dana_1970]: https://ntrs.nasa.gov/citations/19710000633
[research_dandrea_didomenico_2022]: https://doi.org/10.1109/speedam53979.2022.9842005
[research_dang_stern_2022]: https://doi.org/10.2514/1.a35247
[research_dangelo_minisci_1999]: https://doi.org/10.2514/6.1999-4165
[research_daniel_ramusat_2005]: https://doi.org/10.2514/6.2005-6618
[research_daniel_tumino_2004]: https://doi.org/10.2514/6.2004-5825
[research_daniels_dryden_1974]: https://doi.org/10.1117/12.7971680
[research_danrugescu_2006]: https://doi.org/10.2514/6.iac-06-b5.5.11
[research_dantsker_2024]: https://doi.org/10.2514/6.2024-4395
[research_dantsker_2024_b]: https://doi.org/10.2514/6.2024-2842
[research_dantsker_haviland_2022]: https://doi.org/10.2514/6.2022-3638
[research_dantsker_mancuso_2019]: https://doi.org/10.2514/6.2019-1616
[research_dantsker_mancuso_2025]: https://doi.org/10.2514/6.2025-2416
[research_dantsker_selig_2015]: https://doi.org/10.2514/6.2015-2568
[research_dantsker_vahora_2018]: https://doi.org/10.2514/6.2018-4219
[research_dantuckness_1994]: https://doi.org/10.1002/j.2161-4296.1994.tb02573.x
[research_daoxin_2021]: https://doi.org/10.1109/iccasit53235.2021.9633460
[research_daquantang_yongkangjiao_2016]: https://doi.org/10.1109/cgncc.2016.7829144
[research_daryabeigi_2002]: https://doi.org/10.2514/2.3863
[research_das_pei_2023]: https://doi.org/10.1088/1742-6596/2633/1/012005
[research_das_wang_2024]: https://doi.org/10.1049/icp.2024.0657
[research_dasaro_1970]: https://doi.org/10.21236/ad0706219
[research_daugherty_stubbs_1992]: https://doi.org/10.4271/922038
[research_daugherty_yager_1988]: https://doi.org/10.4271/881402
[research_daughetee_1974]: https://doi.org/10.2514/6.1974-343
[research_daum_mollmann_2017]: https://doi.org/10.2514/6.2017-4204
[research_davis_1968]: https://doi.org/10.2514/3.29455
[research_davis_1969]: https://doi.org/10.2514/6.1969-27
[research_davis_1985]: https://ntrs.nasa.gov/citations/19850018410
[research_davis_1989]: https://doi.org/10.2514/6.1989-2949
[research_davis_2002]: https://doi.org/10.21236/ada404007
[research_davis_engler_2003]: https://doi.org/10.2514/6.2003-2706
[research_dayman_1962]: https://ntrs.nasa.gov/citations/19620006382
[research_dayman_1965]: https://ntrs.nasa.gov/citations/19650053701
[research_dayman_1966]: https://ntrs.nasa.gov/citations/19670013912
[research_daymanjr_1971]: https://doi.org/10.2514/6.1971-265
[research_dealvearcardenas_looye_2021]: https://doi.org/10.2514/6.2021-0781
[research_dean_2024]: https://doi.org/10.1136/bmj.q1157
[research_debra_breakwell_1981]: https://doi.org/10.21236/ada114636
[research_dec_braun_2006]: https://doi.org/10.2514/6.2006-780
[research_dec_braun_2013]: https://doi.org/10.2514/1.a32313
[research_dedivitiis_2003]: https://doi.org/10.2514/2.3155
[research_dedivitiis_corraro_2007]: https://doi.org/10.2514/6.2007-6495
[research_deel_1972]: https://doi.org/10.21236/ad0909933
[research_deets_1986]: https://doi.org/10.2514/6.1986-2754
[research_defensescienceboardwashingtondc_1992]: https://doi.org/10.21236/ada274530
[research_degiorgis_borriello_1999]: https://doi.org/10.2514/3.27192
[research_delafontaine_1992]: https://doi.org/10.2514/3.20877
[research_delafontaine_levesque_2006]: https://doi.org/10.2514/6.2006-6075
[research_delaune_derosa_2010]: https://doi.org/10.2514/6.2010-8028
[research_delaune_lebesnerais_2016]: https://doi.org/10.1016/j.robot.2016.01.007
[research_deloach_2009]: https://ntrs.nasa.gov/citations/20090007692
[research_delprete_dagna_2023]: https://doi.org/10.3390/app132011465
[research_demarchi_haning_1978]: https://doi.org/10.21236/ada060326
[research_demars_darling_2014]: https://doi.org/10.21236/ada605594
[research_dematteis_2003]: https://doi.org/10.2514/6.iac-03-a.7.06
[research_demidovich_2017]: https://doi.org/10.1109/icnsurv.2017.8012003
[research_demir_seyfullahbabaarslan_2021]: https://doi.org/10.11648/j.ajset.20210602.13
[research_demo_1986]: https://doi.org/10.2514/6.1986-9797
[research_demuelenaere_alonso_2018]: https://doi.org/10.2514/6.2018-0416
[research_denardo_1952]: https://ntrs.nasa.gov/citations/20090023659
[research_denaro_1986]: https://ntrs.nasa.gov/citations/19880003095
[research_deng_duan_2016]: https://doi.org/10.1007/s11071-016-2670-z
[research_deng_xu_2025]: https://doi.org/10.1088/1742-6596/2977/1/012007
[research_deniz_balakrishnan_2018]: https://doi.org/10.2514/6.2018-1839
[research_depaola_chimento_2018]: https://doi.org/10.2514/6.2018-2102
[research_depaula_quintero_2026]: https://doi.org/10.2514/1.g009512
[research_depaulavieira_sperandiodiasgoncalves_2018]: https://doi.org/10.26678/abcm.encit2018.cit18-0219
[research_deridder_mooij_2009]: https://doi.org/10.2514/6.2009-5769
[research_deridder_mooij_2011]: https://doi.org/10.1016/j.actaastro.2010.08.032
[research_derkiureghian_2001]: https://doi.org/10.1016/s0951-8320(01)00084-9
[research_dermer_nd]: https://doi.org/10.31979/etd.wtda-f4gc
[research_desai_2005]: https://ntrs.nasa.gov/citations/20050060761
[research_desai_2008]: https://ntrs.nasa.gov/citations/20090004445
[research_desao_2006]: https://ntrs.nasa.gov/citations/20060028186
[research_design_considerations_1963]: https://doi.org/10.2514/5.9781600864834.0761.0782
[research_design_validation_2026]: https://doi.org/10.36334/modsim2025.c01.pattarakunnan
[research_designing_a_2017]: https://doi.org/10.2307/j.ctvx072b5.27
[research_deslandes_2010]: https://doi.org/10.2514/6.2010-681
[research_determining_the_rational_2020]: https://doi.org/10.25791/aviakosmos.11.2020.1189
[research_development_of_1972]: https://doi.org/10.2514/6.1972-789
[research_devesa_jourdan_2004]: https://doi.org/10.2514/1.3612
[research_devita_viola_2015]: https://doi.org/10.2514/6.2015-3540
[research_dewagter_meulenbeld_2019]: https://doi.org/10.1177/1756829319880302
[research_dey_giri_2018]: https://doi.org/10.1109/icarcv.2018.8581321
[research_deyst_1968]: https://doi.org/10.1109/tac.1968.1098871
[research_dhanasekaran_balamurali_2011]: https://doi.org/10.4028/www.scientific.net/amm.70.201
[research_dicamplibayarddevolo_dipietro_2018]: https://doi.org/10.2514/6.2018-2463
[research_dieffenbach_1995]: https://doi.org/10.1117/12.211487
[research_dieroff_schaenzer_1990]: https://doi.org/10.2514/6.1990-1301
[research_difranco_1971]: https://doi.org/10.21236/ad0742246
[research_digges_1971]: https://doi.org/10.21236/ad0728647
[research_dileo_leon_2018]: https://doi.org/10.2514/6.2018-0491
[research_dill_uijtdehaag_2016]: https://doi.org/10.1002/navi.134
[research_dillman_slagle_2020]: https://doi.org/10.2514/6.2020-1266
[research_dimensional_analysis_1998]: https://doi.org/10.1017/cbo9780511803352.006
[research_dimensional_analysis_2009]: https://doi.org/10.1201/9781420085259-9
[research_dimensional_analysis_2015]: https://doi.org/10.1201/b18979-10
[research_dimensional_analysis_2019]: https://doi.org/10.1017/9781108377096.006
[research_dimri_matai_2011]: https://doi.org/10.4028/www.scientific.net/amm.110-116.2554
[research_din_janujua_2020]: https://doi.org/10.2514/6.2020-1849
[research_dinc_2021]: https://doi.org/10.20290/estubtdb.900786
[research_ding_2015]: https://doi.org/10.2991/icmmcce-15.2015.441
[research_ding_guo_2016]: https://doi.org/10.1109/cgncc.2016.7829000
[research_ding_li_2023]: https://doi.org/10.2174/9789815050028123040003
[research_dirlingjr_eitman_1984]: https://doi.org/10.2514/6.1984-1771
[research_dirs_1966]: https://doi.org/10.1108/eb034187
[research_discussion_questions_1999]: https://doi.org/10.2514/5.9781600861994.0213.0217
[research_disotell_nietert_2026]: https://doi.org/10.2514/6.2026-4270
[research_dissel_kothari_2007]: https://doi.org/10.2514/1.26064
[research_distefano_leonardi_2018]: https://doi.org/10.1108/aeat-11-2017-0244
[research_dix_mattasits_1980]: https://doi.org/10.21236/ada087237
[research_doche_verniermounier_2001]: https://doi.org/10.1007/3-540-45251-6_34
[research_doenecke_1967]: https://doi.org/10.1016/0017-9310(67)90058-0
[research_doherr_jann_1997]: https://doi.org/10.2514/6.1997-1543
[research_doihara_nishida_2002]: https://doi.org/10.1007/s001930200119
[research_doland_1976]: https://ntrs.nasa.gov/citations/19760011117
[research_doman_2004]: https://doi.org/10.2514/1.14041
[research_donahue_1997]: https://doi.org/10.2514/2.3249
[research_donahue_farrell_1979]: https://doi.org/10.21236/ada083336
[research_donahue_weldon_2008]: https://doi.org/10.2514/1.29313
[research_donelson_lewerenz_1989]: https://doi.org/10.2514/6.1989-2582
[research_dong_huang_2023]: https://doi.org/10.23919/ccc58697.2023.10239805
[research_dong_li_2023]: https://doi.org/10.1002/rnc.6722
[research_dong_wu_2023]: https://doi.org/10.1049/icp.2023.3008
[research_dong_zhao_2025]: https://doi.org/10.1007/978-981-96-2244-3_24
[research_dong_zong_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000670
[research_dongpo_aiying_2025]: https://doi.org/10.52202/083092-0006
[research_donovan_1969]: https://doi.org/10.21236/ad0862137
[research_dorr_1994]: https://ntrs.nasa.gov/citations/19950037642
[research_dorsey_myers_2000]: https://doi.org/10.2514/6.2000-1043
[research_dorsey_poteet_2004]: https://doi.org/10.2514/1.9173
[research_dorsey_wu_1999]: https://doi.org/10.1063/1.57503
[research_dou_duan_2017]: https://doi.org/10.1016/j.ast.2016.11.012
[research_dougherty_1975]: https://doi.org/10.2514/3.7045
[research_dougherty_lee_2016]: https://doi.org/10.2514/1.g001229
[research_douglas_2003]: https://doi.org/10.2514/6.iac-03-v.3.03
[research_douglas_ellis_2021]: https://doi.org/10.2514/6.2021-3023
[research_douglasaircraftcolongbeachca_1962]: https://doi.org/10.21236/ad0404510
[research_downing_1979]: https://ntrs.nasa.gov/citations/19810038145
[research_downing_1981]: https://doi.org/10.2514/6.1981-1643
[research_downing_bryant_1987]: https://doi.org/10.1016/0005-1098(87)90003-3
[research_doyle_1982]: https://doi.org/10.2514/3.62248
[research_dragan_stoica_1997]: https://doi.org/10.1016/s1474-6670(17)41189-x
[research_dragone_2000]: https://doi.org/10.2514/6.2000-5309
[research_draper_1943]: https://ntrs.nasa.gov/citations/19930092574
[research_draper_1948]: https://ntrs.nasa.gov/citations/20050028617
[research_draper_1981]: https://doi.org/10.2514/3.19748
[research_draper_1981_b]: https://doi.org/10.1109/mcs.1981.1100795
[research_driessen_2005]: https://ntrs.nasa.gov/citations/20050215313
[research_drinkwater_1958]: https://ntrs.nasa.gov/citations/19980232089
[research_driver_carballo_2014]: https://doi.org/10.2514/1.a32728
[research_drmichaeljohnson_2020]: https://doi.org/10.71465/ajaae138
[research_droandi_2014]: https://doi.org/10.4050/f-0070-2014-9439
[research_droege_1947]: https://doi.org/10.1115/1.4017522
[research_dsouza_dsouza_1997]: https://doi.org/10.2514/6.1997-3709
[research_dsouza_mcguire_2022]: https://doi.org/10.2514/6.2022-0418
[research_du_jing_2016]: https://doi.org/10.1360/n092016-00106
[research_du_zhang_2020]: https://doi.org/10.23919/ccc50068.2020.9189031
[research_du_zhang_2025]: https://doi.org/10.1007/978-981-97-9771-4_47
[research_duan_yuan_2022]: https://doi.org/10.1109/taes.2022.3156070
[research_duboismatra_bishop_2004]: https://doi.org/10.2514/6.2004-5279
[research_duda_2016]: https://doi.org/10.1016/j.ast.2016.01.015
[research_duda_deuring_2022]: https://doi.org/10.2514/6.2022-3527
[research_duehring_egan_2023]: https://doi.org/10.4050/f-0079-2023-0088
[research_dufour_demuelenaere_2015]: https://doi.org/10.1007/s00158-015-1267-3
[research_duke_swann_1983]: https://doi.org/10.2514/3.19848
[research_dumbacher_klevatt_1994]: https://doi.org/10.2514/6.1994-4682
[research_dunker_berdermann_2025]: https://doi.org/10.52202/083095-0020
[research_dunn_1990]: https://doi.org/10.2514/6.1990-1309
[research_durand_wasicko_1967]: https://doi.org/10.2514/3.43812
[research_durangiraldo_gonzalezsierra_2022]: https://doi.org/10.11144/javeriana.iued26.pdlg
[research_durbin_1959]: https://doi.org/10.1016/b978-1-4831-9728-9.50011-4
[research_durmusoglu_2026]: https://doi.org/10.3390/math14122195
[research_durocher_1978]: https://doi.org/10.2514/3.55782
[research_duston_seghi_2004]: https://doi.org/10.21236/ada461309
[research_dutasatria_darma_2020]: https://doi.org/10.1088/1742-6596/1528/1/012047
[research_dutta_guechaahumada_2024]: https://doi.org/10.2514/6.2024-4328
[research_dwyer_1994]: https://doi.org/10.2514/6.1994-2158
[research_dynamics_of_interaction_2012]: https://doi.org/10.18698/2308-6033-2012-8-448
[research_dynnikov_2020]: https://doi.org/10.1201/9780429070372-59
[research_earl_1967]: https://doi.org/10.21236/ad0817527
[research_ebner_mark_1977]: https://doi.org/10.2514/6.1977-1109
[research_eck_geering_2003]: https://doi.org/10.2514/6.2003-5595
[research_eckmann_cotta_1997]: https://doi.org/10.1063/1.51905
[research_edwards_1969]: https://doi.org/10.2514/6.1969-718
[research_edwards_1972]: https://doi.org/10.2514/6.1972-883
[research_edwards_1973]: https://ntrs.nasa.gov/citations/19730019021
[research_edwards_1975]: https://ntrs.nasa.gov/citations/19750008540
[research_edwards_1981]: https://doi.org/10.2514/6.1981-655
[research_edwards_mavris_2010]: https://doi.org/10.2514/6.2010-8667
[research_effect_of_ground_2016]: https://doi.org/10.15623/ijret.2016.0509033
[research_efremov_efremov_2023]: https://doi.org/10.1016/j.actaastro.2022.10.056
[research_eggers_dittrich_2011]: https://doi.org/10.2514/6.2011-2298
[research_eichhorn_fritzsche_2022]: https://doi.org/10.2514/6.2022-1933
[research_eichhorn_silvestre_2023]: https://doi.org/10.2514/6.2023-0035
[research_eigenmann_kitzmiller_1984]: https://doi.org/10.2514/6.1984-1215
[research_eilertson_1975]: https://doi.org/10.4050/vfs-f31-038
[research_eitner_braun_2013]: https://doi.org/10.2514/6.2013-4527
[research_eklund_2004]: https://doi.org/10.2514/6.2004-5950
[research_eldiasty_pagiatakis_2008]: https://doi.org/10.5081/jgps.7.2.170
[research_eldred_1953]: https://doi.org/10.4271/530157
[research_eldridgeallegra_xu_2023]: https://doi.org/10.2514/6.2023-1426
[research_elias_1974]: https://doi.org/10.2514/6.1974-125
[research_elijah_2026]: https://doi.org/10.59535/jece.v4i1.450
[research_elkaim_lie_2014]: https://doi.org/10.1007/978-90-481-9707-1_56
[research_ellery_richter_2006]: https://doi.org/10.1016/j.actaastro.2005.07.052
[research_elliott_1968]: https://doi.org/10.2514/6.1968-1157
[research_ellis_1989]: https://doi.org/10.2514/6.1989-1406
[research_elmowafy_2005]: https://doi.org/10.5081/jgps.4.1.2
[research_elrabbany_2006]: https://doi.org/10.1109/itsc.2006.1706837
[research_elvin_1996]: https://doi.org/10.1063/1.49950
[research_ely_heyne_2010]: https://doi.org/10.2514/6.2010-7718
[research_ema_1992]: https://doi.org/10.1080/00140139208967835
[research_emery_bardot_2006]: https://doi.org/10.1615/ihtc13.p22.190
[research_engel_putnam_2025]: https://doi.org/10.2514/1.a35925
[research_engle_1977]: https://ntrs.nasa.gov/citations/19780044557
[research_enmi_qian_2018]: https://doi.org/10.1051/eucass/201810105
[research_enriquez_2025]: https://doi.org/10.2514/6.2025-0878
[research_epp_robertson_2015]: https://doi.org/10.2514/6.2015-0324
[research_erasmus_hattingh_2014]: https://doi.org/10.1016/j.engfailanal.2013.07.030
[research_ernst_leidinger_1988]: https://doi.org/10.2514/6.1988-2686
[research_erwin_1990]: https://doi.org/10.2514/6.1990-3815
[research_esposito_orlando_2024]: https://doi.org/10.1063/5.0210478
[research_estupinan_prazenica_2026]: https://doi.org/10.2514/6.2026-0124
[research_evaluation_of_1979]: https://doi.org/10.2514/6.1979-1708
[research_evangelisti_pfifer_2024]: https://doi.org/10.2514/1.g007518
[research_eymar_deneu_2002]: https://doi.org/10.1007/978-94-015-9880-4_13
[research_fahazfiroz_rupikaraj_2023]: https://doi.org/10.34293/acsjse.v3i1.63
[research_fahrenthold_park_2005]: https://doi.org/10.2514/1.6759
[research_fahy_buttsworth_2021]: https://doi.org/10.2514/1.a34863
[research_fain_lambert_2026]: https://doi.org/10.2514/6.2026-5087
[research_faisal_james_2025]: https://doi.org/10.70322/dav.2025.10017
[research_fallonii_taylor_1999]: https://doi.org/10.2514/6.1999-1720
[research_fan_2015]: https://doi.org/10.4028/www.scientific.net/amr.1091.103
[research_fan_nie_2025]: https://doi.org/10.1007/978-981-96-2204-7_58
[research_fan_tian_2022]: https://doi.org/10.1007/978-981-16-7258-3_39
[research_fan_wang_2007]: https://doi.org/10.1117/12.775199
[research_fang_2018]: https://doi.org/10.1007/978-3-319-91821-1_6
[research_fang_2018_b]: https://doi.org/10.1016/j.ast.2018.09.023
[research_fang_2019]: https://doi.org/10.1016/j.ifacol.2019.11.251
[research_fang_chen_2026]: https://doi.org/10.3390/a19070503
[research_fang_ying_2017]: https://doi.org/10.23919/chicc.2017.8028136
[research_farajollahi_markazi_2010]: https://doi.org/10.1109/iccet.2010.5486075
[research_fariz_ushaq_2013]: https://doi.org/10.4028/www.scientific.net/amm.332.79
[research_fasanella_1984]: https://ntrs.nasa.gov/citations/19850002092
[research_fasanella_2004]: https://ntrs.nasa.gov/citations/20040086069
[research_fasanella_2012]: https://ntrs.nasa.gov/citations/20140010066
[research_fathurrahman_jenie_2022]: https://doi.org/10.2514/6.2022-4060
[research_faulders_lekawa_1967]: https://doi.org/10.2514/6.1967-575
[research_faundez_2018]: https://doi.org/10.1088/1742-6596/1043/1/012057
[research_fearnside_1959]: https://doi.org/10.1017/s0373463300045859
[research_feather_1991]: https://ntrs.nasa.gov/citations/19920005842
[research_features_of_landing_2017]: https://doi.org/10.18372/2073-4751.4.12814
[research_federici_benedikter_2026]: https://doi.org/10.2514/1.g009534
[research_fedotov_perepelkina_2019]: https://doi.org/10.23919/icins.2019.8769349
[research_fegely_tischler_2016]: https://doi.org/10.4050/f-0072-2016-11500
[research_fehrs_helm_2025]: https://doi.org/10.2514/6.2025-1714
[research_feinreich_1980]: https://ntrs.nasa.gov/citations/19800023830
[research_feld_1968]: https://doi.org/10.2514/3.29429
[research_feld_nd]: https://ntrs.nasa.gov/citations/20250003172
[research_feldman_1967]: https://doi.org/10.2514/6.1967-588
[research_feldman_2019]: https://ntrs.nasa.gov/citations/20190030273
[research_feng_bai_2025]: https://doi.org/10.3390/aerospace12110956
[research_feng_cui_2009]: https://doi.org/10.1117/12.855287
[research_feng_guo_2019]: https://doi.org/10.1177/0142331219836470
[research_feng_lang_2026]: https://doi.org/10.1016/j.ast.2026.113480
[research_feng_wang_2022]: https://doi.org/10.1109/ccdc55256.2022.10034211
[research_feng_wasynczuk_1967]: https://doi.org/10.2514/6.1967-594
[research_fenghua_meng_2021]: https://doi.org/10.1007/978-981-15-8155-7_277
[research_fenwick_1966_c]: https://doi.org/10.21236/ad0737274
[research_fenwick_1967]: https://doi.org/10.21236/ad0738376
[research_ferguson_zhang_2005]: https://doi.org/10.2514/6.2005-3363
[research_ferrandon_1997]: https://doi.org/10.1016/s0265-9646(97)00008-8
[research_ferreirasantos_2022]: https://doi.org/10.47191/etj/v7i8.02
[research_ferreres_puyou_2006]: https://doi.org/10.2514/1.18535
[research_ferris_1968]: https://ntrs.nasa.gov/citations/19680024407
[research_feustelbuechl_1988]: https://doi.org/10.1179/030801888789798574
[research_fiddes_kirby_1985]: https://doi.org/10.1017/s0001924000050971
[research_field_rossitto_1999]: https://doi.org/10.2514/6.1999-4095
[research_filatyev_2000]: https://doi.org/10.1016/s0094-5765(00)00016-3
[research_filatyev_buzuluk_2014]: https://doi.org/10.1016/j.actaastro.2014.03.007
[research_filyashkin_yatskivsky_2013]: https://doi.org/10.1109/apuavd.2013.6705327
[research_finke_1990]: https://doi.org/10.21236/ada231552
[research_finson_clarke_1980]: https://doi.org/10.21236/ada082438
[research_first_glide_1966]: https://ntrs.nasa.gov/citations/19660014496
[research_fischenberg_1995]: https://doi.org/10.2514/6.1995-3438
[research_fisher_1948]: https://ntrs.nasa.gov/citations/20050028618
[research_fisher_1955]: https://ntrs.nasa.gov/citations/20050029459
[research_fisher_1960]: https://ntrs.nasa.gov/citations/19980228267
[research_fisher_quinn_2018]: https://doi.org/10.2514/6.2018-4283
[research_fitzgerald_1996]: https://doi.org/10.2514/6.1996-3524
[research_fitzsimmons_1996]: https://doi.org/10.2514/6.1996-4414
[research_flight_test_1970]: https://doi.org/10.1108/eb034622
[research_flight_test_1970_b]: https://ntrs.nasa.gov/citations/19710000627
[research_flight_test_1979]: https://doi.org/10.2514/6.1979-1703
[research_flight_test_2016]: https://doi.org/10.21535/dnk59q51
[research_flight_tests_1960]: https://doi.org/10.1016/0043-1648(60)90310-0
[research_florence_1979]: https://doi.org/10.2514/6.1979-1627
[research_flotten_2005]: https://doi.org/10.21236/ada456476
[research_flying_controls_1963]: https://doi.org/10.1108/eb033786
[research_foch_toot_1989]: https://doi.org/10.1007/978-3-642-84010-4_30
[research_fong_ehrlich_1970]: https://doi.org/10.21236/ad0866735
[research_forder_steiner_2020]: https://doi.org/10.5162/ettc2020/2.1
[research_forssell_hyden_2003]: https://doi.org/10.23919/ecc.2003.7085135
[research_fortenbaugh_1972]: https://doi.org/10.2514/6.1972-873
[research_foster_1972]: https://doi.org/10.2514/6.1972-755
[research_foster_2020]: https://ntrs.nasa.gov/citations/20200002814
[research_foster_miller_2020]: https://doi.org/10.2514/6.2020-1504
[research_fowler_1990]: https://doi.org/10.21236/ada223762
[research_fralish_1998]: https://doi.org/10.21236/ada341227
[research_frank_durand_2014]: https://doi.org/10.2514/6.2014-3010
[research_frankenthal_1964]: https://doi.org/10.21236/ad0610257
[research_franklin_1972]: https://ntrs.nasa.gov/citations/19770026207
[research_franklin_hynes_1985]: https://doi.org/10.2514/6.1985-1944
[research_franklin_innis_1977]: https://doi.org/10.2514/6.1977-609
[research_franklin_innis_1978]: https://doi.org/10.2514/3.58306
[research_franze_barz_2025]: https://doi.org/10.1007/s12567-024-00588-2
[research_franze_basov_2026]: https://doi.org/10.2514/6.2026-5005
[research_frapard_2003]: https://doi.org/10.2514/6.iac-03-v.3.07
[research_fratello_1987]: https://ntrs.nasa.gov/citations/19870062335
[research_fravolini_campa_2004]: https://doi.org/10.2514/1.9175
[research_fravolini_yucelen_2015]: https://doi.org/10.2514/6.2015-0611
[research_frayssinet_2019]: https://doi.org/10.2514/6.2019-3224
[research_freeman_talay_1996]: https://doi.org/10.1061/40177(207)52
[research_freeman_talay_1997]: https://doi.org/10.1016/s0094-5765(97)00197-5
[research_fremaux_1995]: https://doi.org/10.2514/3.46895
[research_fremaux_2006]: https://ntrs.nasa.gov/citations/20060045567
[research_french_2001]: https://ntrs.nasa.gov/citations/20010095443
[research_frenkel_shaferman_2026]: https://doi.org/10.2514/6.2026-2167
[research_fresconi_2011]: https://doi.org/10.2514/6.2011-6248
[research_fresconi_celmins_2014]: https://doi.org/10.21236/ada593328
[research_friia_mahajan_2023]: https://doi.org/10.2514/6.2023-0692
[research_frinell_1983]: https://doi.org/10.2514/6.1983-2743
[research_frisby_1960]: https://doi.org/10.21236/ad0244172
[research_friz_samareh_2020]: https://doi.org/10.2514/6.2020-4120
[research_frohme_1975]: https://ntrs.nasa.gov/citations/19760019160
[research_froning_2006]: https://doi.org/10.2514/6.2006-8014
[research_froningjr_mckinney_1996]: https://doi.org/10.2514/6.1996-4519
[research_fu_dang_2025]: https://doi.org/10.1007/978-981-96-2268-9_8
[research_fu_hang_2023]: https://doi.org/10.1109/icmee59781.2023.10525523
[research_fu_shi_2022]: https://doi.org/10.1016/j.cja.2021.01.006
[research_fuchs_haskell_2018]: https://doi.org/10.2514/6.2018-0084
[research_fuchs_jackson_2011]: https://doi.org/10.4050/jahs.56.012005
[research_fuhrmann_2003]: https://doi.org/10.2514/6.2003-3807
[research_fuhry_1999]: https://doi.org/10.2514/6.1999-4211
[research_fujimori_kurozumi_2000]: https://doi.org/10.2514/2.4536
[research_fullerton_1975]: https://ntrs.nasa.gov/citations/19760035694
[research_fundamental_principles_2004]: https://doi.org/10.1049/pbra017e_ch2
[research_furfaro_cersosimo_2013]: https://doi.org/10.2514/1.58246
[research_furnish_anders_1971]: https://doi.org/10.4271/710401
[research_further_development_1994]: https://doi.org/10.2514/6.1994-2141
[research_fusaro_viola_2016]: https://doi.org/10.1007/s12567-016-0131-7
[research_fusion_of_2012]: https://doi.org/10.2514/6.2012-2480
[research_gabarrou_alazard_2010]: https://doi.org/10.3182/20100906-5-jp-2022.00091
[research_gaetan_2009]: https://doi.org/10.3182/20090902-3-us-2007.00072
[research_gage_vanderkam_2003]: https://doi.org/10.2514/6.2003-1330
[research_gai_1996]: https://doi.org/10.2514/3.21573
[research_gainer_1972]: https://ntrs.nasa.gov/citations/19720018825
[research_galanis_jennings_1998]: https://doi.org/10.1207/s15327108ijap0802_1
[research_galassi_2011]: https://doi.org/10.1007/978-3-642-21916-0_69
[research_gallaher_coughlin_1996]: https://doi.org/10.2514/6.1996-3702
[research_gallington_miller_1970]: https://doi.org/10.2514/6.1970-971
[research_galloway_slivinsky_1998]: https://doi.org/10.1061/40339(206)45
[research_gamble_spratlin_1984]: https://doi.org/10.2514/6.1984-2123
[research_gamse_1966]: https://ntrs.nasa.gov/citations/19660008616
[research_gan_fang_2021]: https://doi.org/10.3390/app11125445
[research_gan_fang_2021_b]: https://doi.org/10.1017/aer.2021.115
[research_gandhewar_gsonkusare_2014]: https://doi.org/10.9790/1684-11327578
[research_gang_wang_2010]: https://doi.org/10.4028/www.scientific.net/kem.439-440.704
[research_gannett_1964]: https://ntrs.nasa.gov/citations/19650004580
[research_gao_an_2021]: https://doi.org/10.1016/b978-0-12-822990-3.00009-7
[research_gao_an_2021_b]: https://doi.org/10.1016/b978-0-12-822990-3.00003-6
[research_gao_cai_2017]: https://doi.org/10.1007/s12555-015-0311-9
[research_gao_cai_2018]: https://doi.org/10.1061/(asce)as.1943-5525.0000799
[research_gao_cai_2019]: https://doi.org/10.1109/access.2019.2936974
[research_gao_cui_2010]: https://doi.org/10.1109/icicip.2010.5565297
[research_gao_jiang_2012]: https://doi.org/10.1016/j.jfranklin.2011.11.003
[research_gao_jiang_2014]: https://doi.org/10.2514/6.2014-4415
[research_gao_li_2014]: https://doi.org/10.1109/cgncc.2014.7007365
[research_gao_li_2015]: https://doi.org/10.1360/n092014-00472
[research_gao_shao_2021]: https://doi.org/10.1007/978-981-15-8155-7_97
[research_gao_sun_2023]: https://doi.org/10.1109/iccasit58768.2023.10351579
[research_gao_tang_2017]: https://doi.org/10.2514/6.2017-2253
[research_gao_wang_2025]: https://doi.org/10.5267/j.esm.2025.7.002
[research_gao_wei_2023]: https://doi.org/10.3390/en16237717
[research_gao_yao_2018]: https://doi.org/10.1016/j.ast.2018.05.041
[research_gaohua_jianmei_2014]: https://doi.org/10.1108/aeat-10-2012-0198
[research_garcia_2008]: https://doi.org/10.1109/date.2008.4484898
[research_garcia_fowler_1974]: https://doi.org/10.2514/3.62050
[research_garciapardo_sukhatme_2001]: https://doi.org/10.21236/ada593397
[research_garciaquinchia_yiguo_2009]: https://doi.org/10.1109/isie.2009.5220306
[research_gardinier_taylor_1999]: https://doi.org/10.2514/6.1999-1757
[research_garg_dodiyal_2009]: https://doi.org/10.1109/aero.2009.4839389
[research_garland_1957]: https://ntrs.nasa.gov/citations/20050019361
[research_gaskell_2005]: https://doi.org/10.2514/6.2005-6813
[research_gaverina_eiras_2026]: https://doi.org/10.1117/12.3096303
[research_gavrilovski_ward_2011]: https://doi.org/10.2514/6.2011-2517
[research_gee_1978]: https://ntrs.nasa.gov/citations/19780010099
[research_gee_2014]: https://ntrs.nasa.gov/citations/20140010030
[research_geethas_priyagnair_2015]: https://doi.org/10.17577/ijertv4is050929
[research_geister_2017]: https://doi.org/10.2514/1.c034337
[research_geng_sheng_2013]: https://doi.org/10.1108/ijicc-02-2013-0002
[research_geng_sheng_2014]: https://doi.org/10.1016/j.cja.2014.03.013
[research_genin_1969]: https://doi.org/10.1016/b978-0-08-013290-7.50005-4
[research_gentry_1966]: https://ntrs.nasa.gov/citations/19670039468
[research_gentry_1968]: https://doi.org/10.2514/6.1968-243
[research_gentry_dappolito_1975]: https://doi.org/10.1002/j.2161-4296.1975.tb00726.x
[research_george_sukkarieh_2007]: https://doi.org/10.1109/aero.2007.352849
[research_georghiou_metcalfe_1986]: https://doi.org/10.1007/978-1-349-07455-6_35
[research_gerratt_strate_2020]: https://doi.org/10.1109/plans46316.2020.9109926
[research_gerth_mooij_2014]: https://doi.org/10.2514/6.2014-0088
[research_gettatelli_benedikter_2023]: https://doi.org/10.2514/6.2023-2644
[research_geuther_ackerman_2024]: https://doi.org/10.4050/f-0080-2024-1185
[research_ghanchi_gururajan_2026]: https://doi.org/10.2514/6.2026-1866
[research_ghasemi_moradi_2012]: https://doi.org/10.1061/(asce)as.1943-5525.0000123
[research_ghate_angel_2026]: https://doi.org/10.2514/6.2026-0020
[research_ghods_khalesi_2024]: https://doi.org/10.1109/icrom64545.2024.10903594
[research_gibney_2015]: https://doi.org/10.1038/nature.2015.16908
[research_gibson_2002]: https://doi.org/10.2514/6.2002-424
[research_gibson_marrone_1964]: https://doi.org/10.1016/b978-1-4831-9828-6.50011-4
[research_gibson_wilenius_1964]: https://doi.org/10.2514/6.1964-1119
[research_gielda_deese_1990]: https://doi.org/10.2514/6.1990-3013
[research_gilbert_goldberg_1967]: https://doi.org/10.2514/6.1967-155
[research_gillis_1957]: https://ntrs.nasa.gov/citations/19930092326
[research_gilson_1973]: https://ntrs.nasa.gov/citations/19750011059
[research_girgis_brown_2002]: https://doi.org/10.2514/6.2002-575
[research_glaab_2014]: https://ntrs.nasa.gov/citations/20140011506
[research_glass_glass_2002]: https://doi.org/10.2514/6.2002-5137
[research_glavine_desilva_2018]: https://doi.org/10.1109/mercon.2018.8421936
[research_gleichman_1991]: https://doi.org/10.1117/12.43734
[research_gliding_and_1995]: https://doi.org/10.2514/5.9781600868535.0193.0214
[research_gnoffo_weilmuenster_1994]: https://doi.org/10.2514/3.26448
[research_gockel_1993]: https://doi.org/10.2514/6.1993-5090
[research_godines_abdi_2024]: https://doi.org/10.33599/nasampe/s.24.0231
[research_godwin_frazier_1964]: https://doi.org/10.21236/ad0613504
[research_gogu_bapanapalli_2007]: https://doi.org/10.2514/6.2007-1860
[research_gogu_bapanapalli_2009]: https://doi.org/10.2514/1.35669
[research_gok_cihan_2022]: https://doi.org/10.17350/hjse19030000258
[research_gold_1974]: https://doi.org/10.2514/6.1974-952
[research_goldberg_1966]: https://doi.org/10.2514/6.1966-464
[research_goldman_dowell_2015]: https://doi.org/10.2514/1.a33001
[research_goldschmidt_tingle_2024]: https://doi.org/10.2514/1.j063568
[research_goldstein_leiser_1978]: https://doi.org/10.1007/978-1-4615-9083-5_40
[research_goldyn_marwege_2025]: https://doi.org/10.2514/1.a36174
[research_golomazov_ivankov_2018]: https://doi.org/10.1134/s0038094618070109
[research_gomez_walker_2017]: https://doi.org/10.2514/1.g002081
[research_gong_bing_2015]: https://doi.org/10.2514/6.2015-3606
[research_gong_chen_2025]: https://doi.org/10.23919/acc63710.2025.11107562
[research_gong_guo_2020]: https://doi.org/10.1016/j.ast.2020.106361
[research_gong_ko_1984]: https://doi.org/10.2514/6.1984-1761
[research_gong_wang_2022]: https://doi.org/10.3390/sym14091862
[research_gong_zhang_2015]: https://doi.org/10.1109/tim.2015.2454672
[research_gonzales_kurihara_2021]: https://doi.org/10.2514/6.2021-0871
[research_goodall_1977]: https://doi.org/10.21236/ada048891
[research_goodyearaerospacecorpakronoh_1961]: https://doi.org/10.21236/ad0323899
[research_goodyer_kilgore_1972]: https://doi.org/10.2514/6.1972-995
[research_gopal_somaroutu_2026]: https://doi.org/10.2514/6.2026-2544
[research_gorskiy_subkhangulov_2025]: https://doi.org/10.52467/2949-401x-2025-3-1-189-206
[research_goto_kawakita_2004]: https://doi.org/10.2322/tjsass.47.99
[research_goto_miyazawa_2001]: https://doi.org/10.2514/6.2001-4242
[research_gouskov_1972]: https://doi.org/10.1016/s1474-6670(17)68461-1
[research_goyal_babuska_2021]: https://doi.org/10.2514/6.2021-1166
[research_goz_theodoulis_2025]: https://doi.org/10.2514/6.2025-2266
[research_grabowsky_eldridge_1981]: https://doi.org/10.2514/6.1981-2372
[research_grace_1964]: https://doi.org/10.2514/6.1964-296
[research_gracey_1967]: https://ntrs.nasa.gov/citations/19670053094
[research_grafton_1974]: https://ntrs.nasa.gov/citations/19740018330
[research_grafton_1975]: https://ntrs.nasa.gov/citations/19760003954
[research_grana_1952]: https://ntrs.nasa.gov/citations/20050029465
[research_grantham_2003]: https://ntrs.nasa.gov/citations/20030093586
[research_grantham_williams_1987]: https://doi.org/10.2514/6.1987-2290
[research_grantz_2011]: https://doi.org/10.2514/6.2011-7315
[research_graovac_2007]: https://doi.org/10.5772/4767
[research_grauer_morelli_2017]: https://doi.org/10.2514/6.2017-0935
[research_graves_masciarelli_2002]: https://doi.org/10.2514/6.2002-4622
[research_gray_2016]: https://doi.org/10.2514/6.2016-1034
[research_green_2015]: https://ntrs.nasa.gov/citations/20150008952
[research_green_fernandez_1994]: https://doi.org/10.2514/6.1994-2107
[research_greenhalgh_2026]: https://ntrs.nasa.gov/citations/20260000383
[research_gregory_xargay_2011]: https://doi.org/10.2514/6.2011-6608
[research_greiser_lantzsch_2011]: https://doi.org/10.4050/vfs-f67-000076
[research_grenestedt_spletzer_2010]: https://doi.org/10.1109/cdc.2010.5717109
[research_grenoble_nguyen_2018]: https://doi.org/10.2514/6.2018-1376
[research_grewal_schneider_1976]: https://doi.org/10.1016/s1474-6670(17)67131-3
[research_griffin_takahashi_2022]: https://doi.org/10.2514/6.2022-3656
[research_griffiths_miller_1986]: https://doi.org/10.21236/ada170357
[research_grigoli_2024]: https://doi.org/10.52202/078373-0087
[research_grodsky_mandour_1967]: https://doi.org/10.2514/6.1967-574
[research_groener_stetson_1980]: https://doi.org/10.2514/6.1980-447
[research_groomes_1964]: https://doi.org/10.21236/ad0617544
[research_gross_nd]: https://ntrs.nasa.gov/citations/16517099584357
[research_grossi_fabiani_2026]: https://doi.org/10.2514/6.2026-5034
[research_grosveld_2004]: https://ntrs.nasa.gov/citations/20050071534
[research_grumondz_polishchuk_2012]: https://doi.org/10.3103/s1068799812030051
[research_gryte_hansen_2017]: https://doi.org/10.2514/6.2017-1035
[research_gu_gross_2012]: https://doi.org/10.5772/38260
[research_gu_xing_2022]: https://doi.org/10.3390/rs14235975
[research_guadagnini_dezaiacomo_2023]: https://doi.org/10.3390/aerospace11010035
[research_guerrero_pelluault_2022]: https://doi.org/10.5162/ettc2022/4.3
[research_guida_2023]: https://doi.org/10.21741/9781644902813-19
[research_gulli_maddalena_2014]: https://doi.org/10.2514/1.a32980
[research_gulli_maddalena_2014_b]: https://doi.org/10.2514/1.a32692
[research_gulli_maddalena_2014_c]: https://doi.org/10.2514/6.2014-2804
[research_gulli_maddalena_2015]: https://doi.org/10.2514/1.a32981
[research_gulli_maddalena_2015_b]: https://doi.org/10.2514/6.2015-3554
[research_gunckel_1966]: https://doi.org/10.1016/b978-1-4831-6716-9.50006-0
[research_gunderson_hardy_1965]: https://doi.org/10.1016/s1474-6670(17)69064-5
[research_guo_chang_2018]: https://doi.org/10.1016/j.isatra.2018.04.001
[research_guo_du_2025]: https://doi.org/10.1007/978-981-95-3025-0_10
[research_guo_fang_2022]: https://doi.org/10.1088/1742-6596/2383/1/012127
[research_guo_huang_2026]: https://doi.org/10.3724/j.issn.2096-9287.2025.20250067
[research_guo_luo_2025]: https://doi.org/10.1016/j.ast.2024.109891
[research_guo_qi_2017]: https://doi.org/10.1109/ccdc.2017.7978346
[research_guo_wang_2017]: https://doi.org/10.1007/978-981-10-5230-9_5
[research_guo_wang_2025_b]: https://doi.org/10.3390/drones9050364
[research_guo_yang_2025]: https://doi.org/10.1016/j.ast.2025.110602
[research_guo_yue_2016]: https://doi.org/10.1109/cgncc.2016.7828939
[research_guo_zhu_2017]: https://doi.org/10.1016/j.cja.2016.12.034
[research_guojianguo_fengzhenxin_2016]: https://doi.org/10.1109/vss.2016.7506927
[research_guorongzhao_jixinli_2006]: https://doi.org/10.1109/wcica.2006.1712768
[research_gupta_2023]: https://doi.org/10.61653/joast.v65i4.2013.871
[research_gupta_anilkumar_2018]: https://doi.org/10.18520/cs/v114/i01/131-136
[research_gupta_ramkumar_2015]: https://doi.org/10.12783/fae.2015.0401.02
[research_gupta_sai_2025]: https://doi.org/10.1007/978-981-96-7011-6_11
[research_gutt_fischer_2004]: https://doi.org/10.2514/6.2004-5027
[research_guy_1976]: https://doi.org/10.2514/3.44533
[research_haak_1994]: https://doi.org/10.21236/ada288609
[research_habas_alattar_2022]: https://doi.org/10.1109/icra46639.2022.9812409
[research_haberbusch_walls_2008]: https://doi.org/10.2514/6.2008-4851
[research_hadaegh_mettler_1996]: https://doi.org/10.2514/6.1996-3924
[research_haggerty_1986]: https://doi.org/10.1016/0265-9646(86)90037-8
[research_hahne_1993]: https://ntrs.nasa.gov/citations/19930009206
[research_hahne_2008]: https://ntrs.nasa.gov/citations/20080033127
[research_hailiang_lixin_2015]: https://doi.org/10.1016/j.proeng.2014.12.619
[research_haiqing_junfeng_2025]: https://doi.org/10.1007/978-981-96-3592-4_25
[research_haise_1977]: https://ntrs.nasa.gov/citations/19780044556
[research_halaas_bieniawski_2010]: https://doi.org/10.2514/6.2010-8415
[research_halbe_raja_2014]: https://doi.org/10.2514/1.61615
[research_halbe_spiess_2018]: https://doi.org/10.2514/6.2018-1343
[research_hall_1999]: https://doi.org/10.2514/6.1999-535
[research_hall_dietrich_1963]: https://doi.org/10.2514/6.1963-345
[research_hall_nd]: https://doi.org/10.1109/dasc.2000.886956
[research_hall_shtessel_2005]: https://doi.org/10.2514/6.2005-6145
[research_hall_soares_2008]: https://doi.org/10.1109/dasc.2008.4702786
[research_hallberg_cenko_2008]: https://doi.org/10.2514/6.2008-6381
[research_hallion_becker_1995]: https://doi.org/10.21236/ada302634
[research_halyo_1987]: https://ntrs.nasa.gov/citations/19870016373
[research_ham_1969]: https://doi.org/10.4050/vfs-f25-026
[research_hameed_bindu_2019]: https://doi.org/10.1109/icaset.2019.8714376
[research_hamel_garant_2025]: https://doi.org/10.52202/083087-0043
[research_hamilton_1980]: https://ntrs.nasa.gov/citations/19800007831
[research_hammel_2004]: https://ntrs.nasa.gov/citations/20120003301
[research_hammock_1963]: https://ntrs.nasa.gov/citations/19650076423
[research_hammond_adler_1967]: https://doi.org/10.2514/3.59573
[research_hammouche_sakhi_2016]: https://doi.org/10.5220/0005984103900397
[research_han_2024]: https://doi.org/10.1016/j.sasc.2024.200105
[research_han_2025]: https://doi.org/10.1109/iceace67491.2025.11439877
[research_han_han_2024]: https://doi.org/10.1063/5.0196415
[research_han_jiao_2022]: https://doi.org/10.1109/iccasit55263.2022.9986717
[research_han_shuping_2015]: https://doi.org/10.1109/chicc.2015.7260483
[research_han_wang_2011]: https://doi.org/10.1007/s10291-011-0240-x
[research_han_wang_2025]: https://doi.org/10.1007/978-981-96-2260-3_26
[research_han_xiong_2016]: https://doi.org/10.1109/imcec.2016.7867213
[research_haney_rothschild_2003]: https://doi.org/10.2514/6.2003-5121
[research_hang_rui_2025]: https://doi.org/10.1007/978-981-96-2208-5_25
[research_hankey_1963]: https://doi.org/10.21236/ad0403936
[research_hanlon_deshmukh_2006]: https://doi.org/10.1117/12.658712
[research_hannemann_martinezschramm_2015]: https://doi.org/10.2514/6.2015-3608
[research_hannemann_martinezschramm_2017]: https://doi.org/10.2514/6.2017-2235
[research_hannigan_sved_1993]: https://doi.org/10.2514/6.1993-5081
[research_hannshingju_chingchihtsai_2007]: https://doi.org/10.1109/taes.2007.357136
[research_hannum_berkopec_1989]: https://doi.org/10.2514/6.1989-5014
[research_hao_huang_2009]: https://doi.org/10.1109/iciecs.2009.5364140
[research_hao_lei_2009]: https://doi.org/10.1109/iitaw.2009.51
[research_hao_peng_2017]: https://doi.org/10.2514/6.2017-2108
[research_harcus_bright_2020]: https://doi.org/10.1109/saupec/robmech/prasa48453.2020.9040964
[research_hardin_1986]: https://doi.org/10.1126/science.3945808
[research_hardy_1972]: https://ntrs.nasa.gov/citations/19720013238
[research_hardy_1983]: https://doi.org/10.2514/6.1983-1057
[research_hardy_eldrenkamp_1993]: https://doi.org/10.2514/6.1993-4161
[research_harigae_tanabe_1990]: https://doi.org/10.1016/b978-0-08-037027-9.50009-4
[research_harigae_tomita_2003]: https://doi.org/10.9746/sicetr1965.39.276
[research_harl_2008]: https://doi.org/10.2514/6.2008-6215
[research_harpold_1980]: https://ntrs.nasa.gov/citations/19800016873
[research_harris_2018]: https://doi.org/10.2514/6.2018-3516
[research_harrison_1964]: https://ntrs.nasa.gov/citations/19650004337
[research_harrison_1965]: https://ntrs.nasa.gov/citations/19650022833
[research_harrison_1967]: https://doi.org/10.2514/6.1967-599
[research_harrison_lockman_1968]: https://doi.org/10.2514/6.1968-407
[research_harrison_marko_1968]: https://doi.org/10.2514/6.1968-406
[research_hart_1992]: https://doi.org/10.2514/6.1992-4118
[research_hart_2014]: https://ntrs.nasa.gov/citations/20140003934
[research_hartl_1989]: https://doi.org/10.1007/978-3-642-74585-0_1
[research_hasegawa_2025]: https://doi.org/10.2514/6.2025-1335
[research_hasegawa_fukui_2021]: https://doi.org/10.2322/tastj.19.577
[research_hasegawa_kanda_2019]: https://doi.org/10.2322/tastj.17.301
[research_hatano_1959]: https://doi.org/10.2208/jscej1949.1959.61_18
[research_hatchell_mauss_2011]: https://doi.org/10.1177/1475921711414237
[research_havey_ferguson_1990]: https://doi.org/10.2514/6.1990-1274
[research_hawthorne_1976]: https://ntrs.nasa.gov/citations/19760023182
[research_hawthorne_1976_b]: https://ntrs.nasa.gov/citations/19760023183
[research_hawthorne_1976_c]: https://ntrs.nasa.gov/citations/19760022074
[research_hawthorne_1976_d]: https://ntrs.nasa.gov/citations/19760022075
[research_hawthorne_1976_e]: https://ntrs.nasa.gov/citations/19760022076
[research_hawthorne_1976_f]: https://ntrs.nasa.gov/citations/19760022077
[research_hawthorne_1976_g]: https://ntrs.nasa.gov/citations/19760023184
[research_hawthorne_1976_h]: https://ntrs.nasa.gov/citations/19760023177
[research_hawthorne_1976_i]: https://ntrs.nasa.gov/citations/19760023178
[research_hawthorne_1976_j]: https://ntrs.nasa.gov/citations/19760023179
[research_hawthorne_1976_k]: https://ntrs.nasa.gov/citations/19760023180
[research_hawthorne_1976_l]: https://ntrs.nasa.gov/citations/19760025149
[research_hawthorne_1976_m]: https://ntrs.nasa.gov/citations/19760023181
[research_hayashi_aso_2006]: https://doi.org/10.2514/1.15332
[research_hayashi_yamasaki_2025]: https://doi.org/10.2514/6.2025-1948
[research_hayes_1972]: https://doi.org/10.2514/6.1972-694
[research_hays_dsouza_2022]: https://doi.org/10.2514/6.2022-0417
[research_he_lee_2012]: https://doi.org/10.2514/6.2012-2471
[research_he_zhang_2023]: https://doi.org/10.1007/978-981-19-6613-2_501
[research_he_zhang_2025]: https://doi.org/10.1007/s10291-025-01898-6
[research_he_zhao_2025]: https://doi.org/10.3390/en18133417
[research_hebbar_pashilkar_2017]: https://doi.org/10.1007/s12046-017-0613-0
[research_hecker_bestmann_2019]: https://doi.org/10.17285/0869-7035.0011
[research_hedlund_higgins_1990]: https://doi.org/10.2514/6.1990-1379
[research_hedlund_ragsdale_1985]: https://doi.org/10.2514/6.1985-226
[research_helers_kraemer_1977]: https://doi.org/10.1016/0005-1098(77)90005-x
[research_hellings_1973]: https://doi.org/10.21236/ad0763718
[research_hellman_ngo_2010]: https://doi.org/10.2514/6.2010-8668
[research_hellman_remillard_2011]: https://doi.org/10.21236/ada554045
[research_hellman_tejtel_2008]: https://doi.org/10.2514/6.2008-2566
[research_hellman_wallace_2011]: https://doi.org/10.21236/ada551823
[research_hemann_singh_2016]: https://doi.org/10.1109/iros.2016.7759267
[research_hemsch_1988]: https://doi.org/10.2514/6.1988-216
[research_henderson_1963]: https://doi.org/10.2514/6.1963-1010
[research_hendrick_horn_2024]: https://doi.org/10.1007/s13272-023-00704-8
[research_heng_sherman_1996]: https://doi.org/10.1063/1.49920
[research_heo_pervan_2004]: https://doi.org/10.1002/j.2161-4296.2004.tb00350.x
[research_hepler_1973]: https://doi.org/10.21236/ad0776359
[research_herbst_forrest_2000]: https://doi.org/10.1115/imece2000-2606
[research_hergert_2017]: https://ntrs.nasa.gov/citations/20180006640
[research_herholz_valentiny_1988]: https://doi.org/10.2514/6.1988-4736
[research_herisse_hamel_2012]: https://doi.org/10.1109/tro.2011.2163435
[research_hertzfeld_2000]: https://doi.org/10.2514/6.2000-5113
[research_herz_mccrink_2024]: https://doi.org/10.4050/f-0080-2024-1311
[research_herzog_yue_1998]: https://doi.org/10.2514/6.1998-3604
[research_hess_1972]: https://doi.org/10.21236/ad0755480
[research_hetmaniok_brociek_2024]: https://doi.org/10.7148/2024-0261
[research_hewes_1961]: https://ntrs.nasa.gov/citations/19980227405
[research_heydari_balakrishnan_2011]: https://doi.org/10.2514/6.2011-6641
[research_hicks_matheny_1987]: https://doi.org/10.2514/6.1987-2949
[research_hicks_paller_2025]: https://doi.org/10.2514/1.g008644
[research_hiliuta_botez_2006]: https://doi.org/10.2514/6.2006-3482
[research_hill_huhlein_1993]: https://doi.org/10.2514/6.1993-2701
[research_hillaker_1983]: https://doi.org/10.2514/6.1983-2730
[research_hillaker_1983_b]: https://doi.org/10.2514/6.1983-1063
[research_hiltz_florence_1968]: https://doi.org/10.2514/3.29469
[research_hinchey_1968]: https://doi.org/10.2514/6.1968-345
[research_hinson_1959]: https://ntrs.nasa.gov/citations/19650017031
[research_hinson_1959_b]: https://ntrs.nasa.gov/citations/19980228289
[research_hinton_nd]: https://doi.org/10.18260/1-2--8119
[research_hirschel_weiland_2009]: https://doi.org/10.1007/978-3-540-89974-7_9
[research_ho_romero_2013]: https://doi.org/10.69554/tdxw8274
[research_hoag_1970]: https://ntrs.nasa.gov/citations/19710000636
[research_hoag_1983]: https://doi.org/10.2514/3.19795
[research_hoang_bayasgalan_2017]: https://doi.org/10.23919/acc.2017.7963823
[research_hodge_phillips_1981]: https://doi.org/10.2514/6.1981-2421
[research_hodges_1994]: https://ntrs.nasa.gov/citations/19960024355
[research_hodgkinson_johnston_1979]: https://doi.org/10.2514/6.1979-1783
[research_hoess_voorhees_1963]: https://doi.org/10.4271/630441
[research_hoffelner_maly_2023]: https://doi.org/10.4050/f-0079-2023-18156
[research_hoffman_1961]: https://ntrs.nasa.gov/citations/20040008118
[research_hofmann_1978]: https://ntrs.nasa.gov/citations/19780014128
[research_hofmannwellenhof_legat_2003]: https://doi.org/10.1007/978-3-7091-6078-7_11
[research_hofsass_braun_2023]: https://doi.org/10.2514/6.2023-4223
[research_holberg_grabowsky_1981]: https://doi.org/10.2514/6.1981-2492
[research_holdo_1993]: https://doi.org/10.1016/0167-6105(93)90272-p
[research_holleman_1976]: https://ntrs.nasa.gov/citations/19760010068
[research_holley_brysonjr_1975]: https://doi.org/10.2514/6.1975-1077
[research_hollinger_1958]: https://doi.org/10.1016/0016-0032(58)90226-6
[research_hollis_2017]: https://doi.org/10.2514/6.2017-3122
[research_hollis_hollingsworth_2012]: https://doi.org/10.2514/6.2012-3063
[research_holloway_1967]: https://ntrs.nasa.gov/citations/19670059075
[research_holmes_1970]: https://ntrs.nasa.gov/citations/19710002742
[research_holmes_langelaan_2016]: https://doi.org/10.4050/f-0072-2016-11575
[research_holmes_woehr_1971]: https://doi.org/10.2514/6.1971-278
[research_holt_garry_2016]: https://doi.org/10.2514/6.2016-3881
[research_holway_1966]: https://doi.org/10.2514/6.1966-774
[research_homan_1980]: https://ntrs.nasa.gov/citations/19800016876
[research_honda_tajima_2019]: https://doi.org/10.1007/978-3-030-15035-8_21
[research_hong_dilshod_2016]: https://doi.org/10.14257/astl.2016.138.20
[research_hong_dilshod_2016_b]: https://doi.org/10.14257/ijca.2016.9.12.24
[research_hong_lee_2005]: https://doi.org/10.1017/s172771910000054x
[research_hong_ryoo_2018]: https://doi.org/10.5220/0006908204500457
[research_hood_1968]: https://ntrs.nasa.gov/citations/19680024045
[research_hook_1989]: https://ntrs.nasa.gov/citations/19900026347
[research_hoole_sartor_2020]: https://doi.org/10.2514/6.2020-0681
[research_hoole_sartor_2021]: https://doi.org/10.1017/aer.2021.45
[research_hopping_counts_1986]: https://doi.org/10.2514/6.1986-9744
[research_horn_tritschler_2014]: https://doi.org/10.21236/ada613620
[research_hornbuckle_2015]: https://doi.org/10.21236/ad1019476
[research_horneman_kluever_2004]: https://doi.org/10.2514/6.2004-5183
[research_horri_holderbaum_2024]: https://doi.org/10.3390/app14156635
[research_horstman_1967]: https://ntrs.nasa.gov/citations/19670039778
[research_horton_1964]: https://ntrs.nasa.gov/citations/19640029332
[research_horvath_2002]: https://ntrs.nasa.gov/citations/20030005447
[research_hou_wang_2015]: https://doi.org/10.1109/jas.2015.7081658
[research_hou_zhang_2020]: https://doi.org/10.1177/0036850420950122
[research_housner_edighoffer_1982]: https://doi.org/10.2514/3.62249
[research_howard_1976]: https://doi.org/10.1037/e506152009-061
[research_howardjr_batill_1990]: https://doi.org/10.2514/6.1990-1263
[research_howell_1955]: https://ntrs.nasa.gov/citations/20050019382
[research_howland_1953]: https://doi.org/10.4271/530162
[research_hoxey_robertson_1997]: https://doi.org/10.1016/s0167-6105(97)00185-2
[research_hoy_1963]: https://doi.org/10.21236/ad0409438
[research_hoyt_2006]: https://doi.org/10.2514/6.2006-7278
[research_hruby_1964]: https://ntrs.nasa.gov/citations/19650025659
[research_hryshchenko_romanenko_2018]: https://doi.org/10.1109/msnmc.2018.8576171
[research_hsiao_ho_1997]: https://doi.org/10.2514/6.1997-3693
[research_hu_2013]: https://doi.org/10.4050/sm_2013_arf-36
[research_hu_chen_2021]: https://doi.org/10.1007/s12555-019-0474-x
[research_hu_durbin_2012]: https://doi.org/10.21236/ada567602
[research_hu_guo_2022]: https://doi.org/10.1049/icp.2022.2002
[research_hu_huang_2021]: https://doi.org/10.1007/978-981-15-8155-7_334
[research_hu_ji_2022]: https://doi.org/10.1117/12.2656651
[research_hu_jing_2024]: https://doi.org/10.1016/j.actaastro.2024.07.035
[research_hu_li_2018]: https://doi.org/10.1016/j.neucom.2018.01.031
[research_hu_liu_2025]: https://doi.org/10.1007/978-981-96-2212-2_48
[research_hu_wang_2016]: https://doi.org/10.1007/s11771-016-3351-2
[research_hu_xiao_2024]: https://doi.org/10.1016/j.jfranklin.2023.12.038
[research_hua_yan_2018]: https://doi.org/10.1109/gncc42960.2018.9018695
[research_huan_guoliang_2015]: https://doi.org/10.1109/chicc.2015.7260524
[research_huang_1968]: https://doi.org/10.1007/bf00928758
[research_huang_2016]: https://doi.org/10.1109/ecc.2016.7810266
[research_huang_2019]: https://doi.org/10.1016/j.actaastro.2019.03.073
[research_huang_dai_2023]: https://doi.org/10.2514/1.a35612
[research_huang_dai_2024]: https://doi.org/10.1088/1742-6596/2764/1/012068
[research_huang_deng_2023]: https://doi.org/10.3390/app13031848
[research_huang_fan_2022]: https://doi.org/10.2514/1.a35251
[research_huang_gong_2024]: https://doi.org/10.1061/jaeeez.aseng-5205
[research_huang_jia_2018]: https://doi.org/10.2991/jimec-18.2018.61
[research_huang_li_2025]: https://doi.org/10.2514/1.a36290
[research_huang_liu_2009]: https://doi.org/10.2514/1.34476
[research_huang_liu_2019]: https://doi.org/10.12783/dtcse/ammms2018/27238
[research_huang_luo_2026]: https://doi.org/10.1007/s00371-026-04641-5
[research_huang_nie_2016]: https://doi.org/10.21595/jve.2016.17078
[research_huang_wang_2007]: https://doi.org/10.1109/robio.2007.4522326
[research_huang_wang_2015]: https://doi.org/10.1155/2015/672423
[research_huang_yang_2022]: https://doi.org/10.1016/j.ast.2021.107291
[research_huang_yao_2018]: https://doi.org/10.2514/1.a34093
[research_huang_yao_2019]: https://doi.org/10.2514/1.a34212
[research_huang_yao_2019_b]: https://doi.org/10.2514/1.a34363
[research_huang_yu_2024]: https://doi.org/10.1016/j.ast.2024.109636
[research_huang_zhang_2014]: https://doi.org/10.4028/www.scientific.net/amm.670-671.1410
[research_huang_zhang_2015]: https://doi.org/10.2991/icmmita-15.2015.257
[research_huayanayvillar_aldana_2024]: https://doi.org/10.1109/codit62066.2024.10708474
[research_hudson_2005]: https://doi.org/10.1063/1.1867137
[research_hudson_2006]: https://ntrs.nasa.gov/citations/20060056099
[research_hudson_2009]: https://ntrs.nasa.gov/citations/20090037113
[research_huebner_rock_2001]: https://doi.org/10.2514/2.3774
[research_huebner_rock_2001_b]: https://doi.org/10.2514/6.2001-1809
[research_huebner_smith_2009]: https://doi.org/10.1016/j.actaastro.2009.04.019
[research_hueschen_1984]: https://ntrs.nasa.gov/citations/19840012521
[research_hueschen_1985]: https://ntrs.nasa.gov/citations/19850053830
[research_hughes_chrispin_1988]: https://doi.org/10.1115/88-gt-104
[research_hugo_2016]: https://doi.org/10.1109/robomech.2016.7813184
[research_hugo_lago_2022]: https://doi.org/10.5772/intechopen.100328
[research_hui_yang_2013]: https://doi.org/10.4028/www.scientific.net/amm.275-277.567
[research_huili_xiying_2023]: https://doi.org/10.1109/fpm57590.2023.10565438
[research_hull_french_1981]: https://doi.org/10.2514/6.1981-1862
[research_humes_1978]: https://doi.org/10.2514/3.28010
[research_hummer_jurkovich_2018]: https://doi.org/10.2514/6.2018-3810
[research_humphrey_humphrey_1997]: https://doi.org/10.2514/6.1997-3567
[research_humphreys_1988]: https://ntrs.nasa.gov/citations/19880057789
[research_hundley_rowson_1993]: https://doi.org/10.1002/j.2161-4296.1993.tb02302.x
[research_hung_unger_2024]: https://doi.org/10.35534/dav.2024.10005
[research_hunt_1989]: https://doi.org/10.1007/978-1-4684-9187-6_5
[research_hunt_eiswirth_1996]: https://doi.org/10.2514/6.1996-4591
[research_hunter_1973]: https://doi.org/10.1017/s0373463300021561
[research_hunter_wilson_1976]: https://doi.org/10.2514/6.1976-930
[research_hutter_johnk_2004]: https://doi.org/10.1007/978-3-662-06402-3_10
[research_hutter_wang_2016]: https://doi.org/10.1007/978-3-319-33636-7_20
[research_huweijun_zhoujun_2009]: https://doi.org/10.1109/icicisys.2009.5358312
[research_huynh_kriz_2009]: https://doi.org/10.21236/ada640309
[research_hwang_oh_2005]: https://doi.org/10.1007/s10291-005-0135-9
[research_hyde_1993]: https://ntrs.nasa.gov/citations/19930068757
[research_hyde_2005]: https://doi.org/10.2514/6.2005-5897
[research_hynes_hardy_1987]: https://doi.org/10.4271/872316
[research_hyokawa_ueba_2023]: https://doi.org/10.3390/aerospace10040334
[research_hyslop_doherty_2021]: https://doi.org/10.2514/1.a34937
[research_hyslop_mcgilvray_2022]: https://doi.org/10.2514/6.2022-1324
[research_hyun_2005]: https://doi.org/10.2514/6.2005-7014
[research_ide_landman_2025]: https://doi.org/10.1108/ijius-11-2024-0335
[research_iden_1959]: https://doi.org/10.1109/tane3.1959.4201676
[research_iharasani_2015]: https://doi.org/10.5176/2382-5758_1.2.10
[research_iizuka_2024]: https://doi.org/10.53829/ntr202406ra1
[research_iliev_nachev_2022]: https://doi.org/10.3390/s22176451
[research_inatani_akiba_1992]: https://doi.org/10.2514/6.1992-5053
[research_indig_benasher_2017]: https://doi.org/10.2514/6.2017-1737
[research_inertial_navigation_1997]: https://doi.org/10.2514/5.9781600866463.0181.0209
[research_inertial_navigation_1999]: https://doi.org/10.2514/5.9781600861994.0039.0071
[research_inertial_navigation_2004]: https://doi.org/10.1049/pbra017e_ch10
[research_inertial_navigation_2007]: https://doi.org/10.2514/5.9781600861598.0215.0228
[research_inertial_navigation_2013]: https://doi.org/10.4324/9780080941523-105
[research_inertial_navigation_2013_b]: https://doi.org/10.1017/cbo9780511843860.005
[research_inertial_navigation_2018]: https://doi.org/10.1201/9781315217109-27
[research_inertially_augmented_1971]: https://doi.org/10.2514/6.1971-795
[research_influence_of_1963]: https://doi.org/10.1016/0043-1648(63)90021-8
[research_inger_2003]: https://doi.org/10.2514/6.2003-1136
[research_inger_2003_b]: https://doi.org/10.1063/1.1581589
[research_ingle_celi_1994]: https://doi.org/10.4050/jahs.39.12
[research_inokuchi_1996]: https://doi.org/10.1063/1.49968
[research_integrated_navigation_2004]: https://doi.org/10.1049/pbra017e_ch13
[research_integrated_vision_inertial_1999]: https://doi.org/10.1109/acc.1999.786185
[research_introduction_and_2022]: https://doi.org/10.1049/sbra550e_ch1
[research_ishida_nagai_2014]: https://doi.org/10.1299/jsmemecj.2014._s1910203-
[research_ishida_nagai_2015]: https://doi.org/10.2514/6.2015-0244
[research_ishikawa_ogasawara_2001]: https://doi.org/10.2514/6.2001-1879
[research_ishimoto_1995]: https://doi.org/10.2514/6.1995-3286
[research_ishimoto_fujii_2005]: https://doi.org/10.1016/j.actaastro.2005.03.045
[research_ishimoto_takizawa_1996]: https://doi.org/10.2514/6.1996-3403
[research_ishioka_uchiyama_2019]: https://doi.org/10.2514/6.2019-0358
[research_ismail_pashilkar_2015]: https://doi.org/10.1109/ccip.2015.7100733
[research_isro_releases_the_2018]: https://doi.org/10.18520/cs/v114/i08/1596-1596
[research_ito_akimoto_1990]: https://doi.org/10.2514/6.1990-5223
[research_ito_nomoto_1990]: https://doi.org/10.2322/jjsass1969.38.194
[research_ivanco_keller_2024]: https://doi.org/10.2514/1.a35930
[research_ivanov_bitzer_1993]: https://doi.org/10.1007/978-3-642-45720-3_14
[research_ivanov_huertas_2013]: https://doi.org/10.2514/6.2013-5019
[research_ivanov_vashchenkov_2007]: https://doi.org/10.2514/6.2007-4145
[research_ivanov_vashchenkov_2011]: https://doi.org/10.2514/6.2011-3309
[research_ivins_1978]: https://ntrs.nasa.gov/citations/19790045468
[research_iwabuchi_minesugi_2026]: https://doi.org/10.2514/6.2026-2326
[research_iwakawa_furukawa_2015]: https://doi.org/10.2514/6.2015-2584
[research_izraelevitz_pauken_2022]: https://doi.org/10.1109/aero53065.2022.9843453
[research_izzo_weiss_2011]: https://doi.org/10.2514/1.52553
[research_jacklin_2008]: https://doi.org/10.2514/6.2008-6988
[research_jackson_1961]: https://doi.org/10.2514/8.9246
[research_jackson_1991]: https://ntrs.nasa.gov/citations/19910062565
[research_jackson_1992]: https://ntrs.nasa.gov/citations/19920021931
[research_jackson_1992_b]: https://ntrs.nasa.gov/citations/19920021916
[research_jackson_1993]: https://ntrs.nasa.gov/citations/19930069741
[research_jackson_1994]: https://ntrs.nasa.gov/citations/19940030181
[research_jackson_2003]: https://ntrs.nasa.gov/citations/20030065638
[research_jackson_2004]: https://ntrs.nasa.gov/citations/20040086068
[research_jackson_2004_b]: https://ntrs.nasa.gov/citations/20040086484
[research_jackson_2004_c]: https://ntrs.nasa.gov/citations/20040191338
[research_jackson_2006]: https://ntrs.nasa.gov/citations/20060051445
[research_jackson_2016]: https://ntrs.nasa.gov/citations/20160010155
[research_jackson_2018]: https://ntrs.nasa.gov/citations/20180001967
[research_jackson_2018_b]: https://ntrs.nasa.gov/citations/20180006306
[research_jackson_coyle_1983]: https://doi.org/10.2514/6.1983-2724
[research_jackson_rivers_1993_b]: https://doi.org/10.2514/6.1993-3690
[research_jackson_rivers_1998]: https://doi.org/10.2514/6.1998-4254
[research_jacob_1991]: https://doi.org/10.1007/978-1-4612-3102-8_37
[research_jacobson_2004]: https://ntrs.nasa.gov/citations/20040041355
[research_jacobson_2004_b]: https://ntrs.nasa.gov/citations/20040041357
[research_jacobson_2005]: https://doi.org/10.2172/877779
[research_jaensch_markl_1991]: https://doi.org/10.2514/6.1991-2659
[research_jaffe_1972]: https://doi.org/10.2514/6.1972-983
[research_jaffe_1975]: https://ntrs.nasa.gov/citations/19750008472
[research_jalaja_manwatkar_2023]: https://doi.org/10.1016/j.engfailanal.2022.107042
[research_jamaleddine_2025]: https://doi.org/10.4236/aast.2025.102006
[research_james_1959]: https://ntrs.nasa.gov/citations/19980228370
[research_jameson_2001]: https://doi.org/10.21236/ada407255
[research_jamieson_white_2019]: https://doi.org/10.1061/9780784482476.024
[research_jamieson_white_2021]: https://doi.org/10.3390/ma14030502
[research_janicik_1999]: https://doi.org/10.2514/6.1999-4539
[research_jann_greinerperth_2009]: https://doi.org/10.2514/6.2009-2932
[research_janna_2020]: https://doi.org/10.1201/9780429324536-4
[research_janssens_2000]: https://doi.org/10.2514/6.2000-5500
[research_jaroslaw_robert_2026]: https://doi.org/10.3390/engproc2026133092
[research_jarvis_1989]: https://doi.org/10.1115/1.3240236
[research_jasra_valentino_2020]: https://doi.org/10.2514/6.2020-0674
[research_jategaonkar_behr_2006]: https://doi.org/10.2514/1.19602
[research_jathaveda_manokaran_2023]: https://doi.org/10.1007/978-981-19-7055-9_76
[research_javeed_1993]: https://ntrs.nasa.gov/citations/19930014046
[research_jayanthi_jain_2019]: https://doi.org/10.12783/ballistics2019/33142
[research_jayaraman_gaurav_2022]: https://doi.org/10.2514/6.2022-0751
[research_jayaraman_saini_2022]: https://doi.org/10.1016/j.ifacol.2023.03.032
[research_jeanross_edwards_1987]: https://doi.org/10.1017/s0001924000021631
[research_jebacek_horak_2016]: https://doi.org/10.4028/www.scientific.net/amm.821.325
[research_jee_brinda_2014]: https://doi.org/10.3182/20140313-3-in-3024.00100
[research_jee_yalagach_2014]: https://doi.org/10.3182/20140313-3-in-3024.00160
[research_jekeli_2015]: https://doi.org/10.1007/978-3-319-02370-0_10-1
[research_jenkins_1968]: https://ntrs.nasa.gov/citations/19710005528
[research_jenkins_donovan_1942]: https://doi.org/10.2514/8.10912
[research_jenkins_donovan_1942_b]: https://doi.org/10.2514/8.10919
[research_jensen_coy_2020]: https://doi.org/10.2514/6.2020-3833
[research_jeong_ryu_2013]: https://doi.org/10.5139/jksas.2013.41.6.458
[research_jetawatthana_khamvilai_2026]: https://doi.org/10.2514/6.2026-1176
[research_ji_hua_2023]: https://doi.org/10.1109/iws58240.2023.10222240
[research_ji_zhou_2018]: https://doi.org/10.1109/gncc42960.2018.9019124
[research_jia_2020]: https://doi.org/10.1109/aero47225.2020.9172562
[research_jia_fu_2020]: https://doi.org/10.1016/j.actaastro.2020.07.022
[research_jia_han_2011]: https://doi.org/10.4028/www.scientific.net/amm.105-107.470
[research_jia_jizhen_2019]: https://doi.org/10.1109/ccdc.2019.8833311
[research_jia_qi_2026]: https://doi.org/10.1016/j.ast.2025.111375
[research_jia_wang_2024]: https://doi.org/10.1109/icaace61206.2024.10548275
[research_jiang_2011]: https://doi.org/10.1016/j.proeng.2011.10.002
[research_jiang_chen_2018]: https://doi.org/10.1109/gncc42960.2018.9018655
[research_jiang_song_2017]: https://doi.org/10.2514/6.2017-2262
[research_jiang_wang_2017]: https://doi.org/10.1007/978-3-319-46213-4_29
[research_jiang_wang_2023]: https://doi.org/10.1016/j.triboint.2023.108501
[research_jiang_xie_2026]: https://doi.org/10.1007/978-981-95-3079-3_1
[research_jiang_yang_2014]: https://doi.org/10.1155/2014/929731
[research_jiang_ye_2014]: https://doi.org/10.2514/6.2014-0351
[research_jiang_yu_2019]: https://doi.org/10.1007/978-3-319-91020-8_1
[research_jiang_zhang_2017]: https://doi.org/10.1007/978-981-10-4591-2_30
[research_jiang_zhen_2018]: https://doi.org/10.23919/chicc.2018.8483965
[research_jianguo_guoqing_2016]: https://doi.org/10.1109/ccdc.2016.7532005
[research_jianguo_xiangyu_2017]: https://doi.org/10.1109/ccdc.2017.7978875
[research_jiao_liu_2017]: https://doi.org/10.2514/1.c033563
[research_jiawei_2024]: https://doi.org/10.52202/078373-0005
[research_jiaxing_dayi_2025]: https://doi.org/10.1007/978-981-96-2212-2_40
[research_jiayuan_peng_2018]: https://doi.org/10.1109/gncc42960.2018.9018894
[research_jieliangzhihuilixuguoliweiboshi_2020]: https://doi.org/10.4208/cicp.oa-2016-0213
[research_jin_huang_2025]: https://doi.org/10.1007/978-981-96-2204-7_31
[research_jin_zhu_2017]: https://doi.org/10.2514/6.2017-1522
[research_jindong_zhiqiang_2011]: https://doi.org/10.1109/isie.2011.20
[research_jing_qi_2020]: https://doi.org/10.1088/1757-899x/887/1/012042
[research_jiteng_shahneh_2018]: https://doi.org/10.1049/cp.2018.0227
[research_jits_wright_2005]: https://doi.org/10.2514/1.13428
[research_jmurnes_moomaw_1981]: https://doi.org/10.2514/3.56069
[research_jo_ahn_2021]: https://doi.org/10.1016/j.ast.2020.106431
[research_jo_ahn_2022]: https://doi.org/10.1016/j.ast.2022.107703
[research_jobmann_thielecke_2024]: https://doi.org/10.36001/phme.2024.v8i1.4104
[research_joelp_r_2014]: https://doi.org/10.9790/1684-11236774
[research_johannesen_vinh_1985]: https://doi.org/10.2514/6.1985-1817
[research_johannsen_pfendler_1976]: https://doi.org/10.1007/978-1-4684-2523-9_8
[research_johansen_fossen_2020]: https://doi.org/10.1007/978-3-642-41610-1_67-1
[research_johnis_2023]: https://doi.org/10.2514/6.2023-4614
[research_johnsen_runnels_2022]: https://doi.org/10.3390/app12167961
[research_johnson_1949]: https://ntrs.nasa.gov/citations/20090026465
[research_johnson_1951]: https://ntrs.nasa.gov/citations/20050030031
[research_johnson_1953]: https://ntrs.nasa.gov/citations/20050029408
[research_johnson_1962]: https://doi.org/10.21236/ad0295400
[research_johnson_1967]: https://doi.org/10.1016/b978-0-12-395737-5.50048-2
[research_johnson_2011]: https://ntrs.nasa.gov/citations/20150006935
[research_johnson_2019]: https://ntrs.nasa.gov/citations/20190027310
[research_johnson_calise_2008]: https://doi.org/10.2514/6.2008-6989
[research_johnson_cerimele_2018]: https://doi.org/10.2514/6.2018-0615
[research_johnson_lu_2020]: https://doi.org/10.2514/6.2020-1513
[research_johnson_shalaev_2006]: https://doi.org/10.21236/ada573636
[research_johnston_candler_2023]: https://doi.org/10.2514/6.2023-0084
[research_joint_conference_1960]: https://ntrs.nasa.gov/citations/19720063091
[research_jones_1970]: https://doi.org/10.1017/s0373463300032471
[research_jones_boiffier_2011]: https://doi.org/10.2514/6.2011-6674
[research_jones_diamant_1989]: https://doi.org/10.2514/6.1989-75
[research_jones_gruszczynski_1987]: https://doi.org/10.2514/6.1987-1505
[research_jones_laurence_2025]: https://doi.org/10.2514/6.2025-99832
[research_jones_nd]: https://doi.org/10.1109/smc-it.2006.15
[research_joo_alali_2008]: https://doi.org/10.3182/20080706-5-kr-1001.02316
[research_joo_ippolito_2008]: https://doi.org/10.1109/aero.2008.4526557
[research_joos_pfife_2012]: https://doi.org/10.2514/6.2012-4998
[research_joos_varga_1999]: https://doi.org/10.1524/auto.1999.47.6.239
[research_jordan_1980]: https://ntrs.nasa.gov/citations/19800015768
[research_jordan_1992]: https://ntrs.nasa.gov/citations/19920016033
[research_jordan_2004]: https://ntrs.nasa.gov/citations/20040085988
[research_jordan_bailey_2008]: https://doi.org/10.2514/6.2008-6660
[research_jordan_buffington_1987]: https://doi.org/10.2514/6.1987-2364
[research_jordan_langford_2005]: https://doi.org/10.2514/6.2005-6432
[research_jordanjr_1980]: https://doi.org/10.2514/6.1980-427
[research_joshi_compton_1985]: https://doi.org/10.2514/6.1985-3075
[research_joshi_jeon_2015]: https://doi.org/10.1061/(asce)as.1943-5525.0000395
[research_jouannet_2008]: https://doi.org/10.2514/6.2008-137
[research_jouannet_berry_2012]: https://doi.org/10.1108/00022661211222058
[research_jouannet_lundstrom_2017]: https://doi.org/10.2514/6.2017-4075
[research_jouhaud_1992]: https://doi.org/10.1016/0094-5765(92)90148-c
[research_jouhaud_ferreres_2007]: https://doi.org/10.3182/20070625-5-fr-2916.00054
[research_joyner_1969]: https://ntrs.nasa.gov/citations/19690057650
[research_joyner_1970]: https://ntrs.nasa.gov/citations/19700052398
[research_ju_jiang_2024]: https://doi.org/10.3390/math12193024
[research_ju_wei_2022]: https://doi.org/10.1016/j.actaastro.2021.11.015
[research_juang_chien_2008]: https://doi.org/10.1109/icicic.2008.178
[research_juang_chio_2005]: https://doi.org/10.1080/0020772042000325961
[research_juhasz_xin_2020]: https://doi.org/10.4050/f-0076-2020-16291
[research_jump_padfield_2006]: https://doi.org/10.1108/17488840610639618
[research_jumper_seward_1992]: https://doi.org/10.2514/6.1992-811
[research_junaidr_beebim_2015]: https://doi.org/10.70729/ijser15399
[research_jung_2024]: https://doi.org/10.3390/aerospace11040265
[research_jung_kim_2025]: https://doi.org/10.52202/083087-0113
[research_jung_lee_2015]: https://doi.org/10.1109/coase.2015.7294102
[research_kadam_sathish_2018]: https://doi.org/10.1007/978-981-10-8597-0_17
[research_kaertner_2006]: https://doi.org/10.21236/ada442348
[research_kageyama_hiraoka_2004]: https://doi.org/10.1299/jsmecmd.2004.17.681
[research_kahn_edwards_2015]: https://doi.org/10.21236/ada623280
[research_kahn_edwards_2019]: https://doi.org/10.2514/1.g004247
[research_kai_anglade_2018]: https://doi.org/10.1109/cdc.2018.8619827
[research_kai_ohtake_1996]: https://doi.org/10.2514/6.1996-4526
[research_kalden_2007]: https://doi.org/10.1109/rast.2007.4283979
[research_kalikhman_kalikhman_2018]: https://doi.org/10.23919/icins.2018.8405927
[research_kalman_filter_1999]: https://doi.org/10.2514/5.9781600861994.0095.0107
[research_kam_gage_2004]: https://doi.org/10.2514/1.6324
[research_kanda_ueda_2006]: https://doi.org/10.2514/1.18444
[research_kaneshige_bull_1999]: https://doi.org/10.2514/6.1999-3962
[research_kang_2008]: https://doi.org/10.1109/iccas.2008.4694527
[research_kang_choi_2024]: https://doi.org/10.1088/1361-665x/ad3e53
[research_kang_han_2025]: https://doi.org/10.1109/jsen.2025.3562935
[research_kang_li_2007]: https://doi.org/10.2514/6.2007-6468
[research_kannan_nd]: https://ntrs.nasa.gov/citations/20220018459
[research_kaplan_2002]: https://doi.org/10.1063/1.1449851
[research_kaplan_patil_2023]: https://doi.org/10.4050/f-0079-2023-18043
[research_karasopoulos_cervisi_1998]: https://doi.org/10.2514/6.1998-4149
[research_karel_1967]: https://doi.org/10.4271/670378
[research_kariya_tanaka_2020]: https://doi.org/10.1299/jsmermd.2020.2a1-b01
[research_karlgaard_deshmukh_2024]: https://doi.org/10.2514/6.2024-4326
[research_karmarker_1976]: https://ntrs.nasa.gov/citations/19760026090
[research_karpenko_sekhavat_2010]: https://doi.org/10.2514/6.2010-8051
[research_karpov_schmidt_1964]: https://doi.org/10.21236/ad0454925
[research_kashkovsky_2014]: https://doi.org/10.1063/1.4902593
[research_kashkovsky_vashchenkov_2014]: https://doi.org/10.1134/s0869864314060067
[research_kashkovsky_vashchenkov_2019]: https://doi.org/10.1063/1.5119609
[research_kato_1991]: https://doi.org/10.2322/jjsass1969.39.580
[research_katz_roglin_2000]: https://doi.org/10.2514/2.2658
[research_kaufmann_1995]: https://ntrs.nasa.gov/citations/19960002042
[research_kaufmann_1995_b]: https://ntrs.nasa.gov/citations/19950024367
[research_kaushik_anemaat_2012]: https://doi.org/10.2514/6.2012-3228
[research_kawaguchi_hashimoto_1997]: https://doi.org/10.2514/2.4148
[research_kawaguchi_suzuki_2017]: https://doi.org/10.2514/6.2017-0939
[research_kawamura_azimov_2022]: https://doi.org/10.1115/1.4054951
[research_kawamura_dolph_2023]: https://doi.org/10.2514/6.2023-2195
[research_kawamura_kannan_2022]: https://doi.org/10.2514/6.2022-0497
[research_kawamura_nd]: https://ntrs.nasa.gov/citations/20220007351
[research_kawamura_nd_b]: https://ntrs.nasa.gov/citations/20220017714
[research_kawato_watanabe_2002]: https://doi.org/10.2514/6.2002-5265
[research_kawato_watanabe_2003]: https://doi.org/10.2514/6.2003-7059
[research_kaynak_2010]: https://doi.org/10.3182/20100906-5-jp-2022.00012
[research_kayton_1968]: https://doi.org/10.1109/taes.1968.5409036
[research_ke_zhengzhong_2014]: https://doi.org/10.1109/cgncc.2014.7007248
[research_keidel_fasel_2019]: https://doi.org/10.2514/6.2019-0854
[research_keipour_2022]: https://doi.org/10.3390/s22176549
[research_keke_qing_2014]: https://doi.org/10.1109/cgncc.2014.7007393
[research_kellas_2017]: https://doi.org/10.1109/aero.2017.7943744
[research_keller_mckillipjr_2026]: https://doi.org/10.4050/f-0082-2026-0225
[research_kelly_1963]: https://ntrs.nasa.gov/citations/19630028727
[research_kelly_1977]: https://doi.org/10.1002/j.2161-4296.1977.tb01284.x
[research_kelly_1994]: https://doi.org/10.21236/ada282853
[research_kelly_davis_1994]: https://doi.org/10.1002/j.2161-4296.1994.tb02320.x
[research_kelly_laberge_1980]: https://doi.org/10.1002/j.2161-4296.1980.tb01395.x
[research_kelly_menich_2010]: https://doi.org/10.2514/6.2010-8872
[research_kempel_1970]: https://ntrs.nasa.gov/citations/19710000629
[research_kempel_1971]: https://ntrs.nasa.gov/citations/19710023831
[research_kempel_1971_b]: https://ntrs.nasa.gov/citations/19720004251
[research_kempel_1974]: https://ntrs.nasa.gov/citations/19740006422
[research_kempel_1975]: https://ntrs.nasa.gov/citations/19750018943
[research_kempel_1994]: https://ntrs.nasa.gov/citations/19940030197
[research_kempel_painter_1994]: https://doi.org/10.2514/6.1994-2180
[research_kendall_idris_2022]: https://doi.org/10.2514/6.2022-3759
[research_kendoul_2012]: https://doi.org/10.1002/rob.20414
[research_kendoul_2013]: https://doi.org/10.1177/0278364913509496
[research_kendoul_nonami_2009]: https://doi.org/10.1007/s10514-009-9135-x
[research_kendoul_yu_2009]: https://doi.org/10.1002/rob.20327
[research_kennell_neely_2016]: https://doi.org/10.2514/6.2016-1152
[research_keskin_2026]: https://doi.org/10.1108/aeat-04-2026-0122
[research_ketabdari_toraldo_2020]: https://doi.org/10.1007/978-3-030-58799-4_13
[research_ketterle_vuletic_2008]: https://doi.org/10.21236/ada499671
[research_keviczky_balas_2005]: https://doi.org/10.2514/6.2005-5863
[research_keviczky_balas_2006]: https://doi.org/10.2514/1.15562
[research_khalifa_hashim_2026]: https://doi.org/10.1016/j.measurement.2026.121964
[research_khalil_abdelgawad_2023]: https://doi.org/10.2514/1.a35441
[research_khamlak_2026]: https://doi.org/10.37547/tajet/book-26-01
[research_khan_chakraborty_2023]: https://doi.org/10.2514/1.j063120
[research_khan_chakraborty_2026]: https://doi.org/10.1007/978-981-96-9416-7_8
[research_khan_mehmood_2021]: https://doi.org/10.1109/icaem53552.2021.9547116
[research_khan_rajput_2019]: https://doi.org/10.1109/ibcast.2019.8666962
[research_khanapuri_rao_2017]: https://doi.org/10.1007/978-981-10-5146-3_7
[research_kharchenko_kryukov_2018]: https://doi.org/10.1088/1742-6596/1009/1/012004
[research_khattak_chan_2023]: https://doi.org/10.1038/s41598-023-36495-5
[research_khatwa_helmreich_1999]: https://doi.org/10.4271/1999-01-5587
[research_khurana_suzuki_2012]: https://doi.org/10.2514/6.2012-2659
[research_khurana_suzuki_2013]: https://doi.org/10.2514/6.2013-2513
[research_khurana_suzuki_2014]: https://doi.org/10.2514/6.2014-1247
[research_kiddy_1995]: https://ntrs.nasa.gov/citations/19970003084
[research_kiehn_2020]: https://doi.org/10.1007/s12567-020-00319-3
[research_kilgore_1982]: https://doi.org/10.1016/b978-0-408-01252-2.50096-0
[research_kilgore_adcock_1974]: https://doi.org/10.2514/3.60395
[research_kilgore_dress_1984]: https://doi.org/10.1016/0011-2275(84)90007-9
[research_kilgore_kilgore_1997]: https://doi.org/10.2514/6.1997-3928
[research_kim_2026]: https://doi.org/10.1002/asjc.70154
[research_kim_choi_2026]: https://doi.org/10.3390/ma19020303
[research_kim_han_2018]: https://doi.org/10.1117/12.2296757
[research_kim_jeong_2021]: https://doi.org/10.3390/aerospace8120380
[research_kim_kim_2009]: https://doi.org/10.5302/j.icros.2009.15.1.054
[research_kim_kim_2012]: https://doi.org/10.1061/(asce)as.1943-5525.0000172
[research_kim_kim_2014]: https://doi.org/10.1115/imece2014-36452
[research_kim_kim_2020]: https://doi.org/10.1080/09243046.2020.1790124
[research_kim_ko_2026]: https://doi.org/10.2514/6.2026-1707
[research_kim_langley_2003]: https://doi.org/10.1002/j.2161-4296.2003.tb00322.x
[research_kim_lee_2006]: https://doi.org/10.5081/jgps.5.1.82
[research_kim_lee_2021]: https://doi.org/10.3390/en14113210
[research_kim_shin_2015]: https://doi.org/10.1115/imece2015-52474
[research_kim_tahk_2019]: https://doi.org/10.1007/s42405-019-00192-3
[research_kim_um_2015]: https://doi.org/10.2514/1.g000093
[research_kim_woldeyohannis_2024]: https://doi.org/10.52202/078373-0082
[research_kim_woo_2017]: https://doi.org/10.1109/urai.2017.7992719
[research_kimhyunsu_jehyungjeon_2018]: https://doi.org/10.34163/jkits.2018.13.5.013
[research_kimmel_adamczak_2011]: https://doi.org/10.21236/ada548272
[research_kineyko_1982]: https://doi.org/10.21236/ada119003
[research_kirsten_1974]: https://ntrs.nasa.gov/citations/19740017460
[research_kish_rhoney_2017]: https://doi.org/10.1109/aero.2017.7943672
[research_klein_1992]: https://ntrs.nasa.gov/citations/19920072719
[research_kleinert_schleith_2010]: https://doi.org/10.1109/mfi.2010.5604453
[research_klevatt_gaubatz_1998]: https://doi.org/10.1063/1.54948
[research_kling_1989]: https://doi.org/10.1007/978-3-642-74585-0_39
[research_kling_hornung_2019]: https://doi.org/10.4271/2019-01-1890
[research_klingenberg_willems_2026]: https://doi.org/10.2514/6.2026-5043
[research_klochan_alammouri_2017]: https://doi.org/10.18372/1990-5548.54.12316
[research_kluever_2004]: https://doi.org/10.2514/1.7877
[research_kluever_2007]: https://doi.org/10.2514/1.24864
[research_kluever_2007_b]: https://doi.org/10.2514/1.28081
[research_kluever_2008]: https://doi.org/10.2514/1.36950
[research_kluever_2022]: https://doi.org/10.2514/1.g006338
[research_kluever_horneman_2005]: https://doi.org/10.2514/6.2005-6058
[research_kluever_horneman_2009]: https://doi.org/10.2514/6.2009-5766
[research_kluever_neal_2015]: https://doi.org/10.2514/1.g000909
[research_klumpp_1966]: https://doi.org/10.2514/6.1966-1863
[research_klyde_liang_2009]: https://doi.org/10.2514/1.43157
[research_knab_gogel_1995]: https://doi.org/10.2514/6.1995-623
[research_knapp_1999]: https://doi.org/10.2514/6.1999-4932
[research_knapp_ivler_2017]: https://doi.org/10.4050/f-0073-2017-12185
[research_ko_1983]: https://doi.org/10.2514/6.1983-2698
[research_ko_1984]: https://ntrs.nasa.gov/citations/19840007520
[research_ko_1987]: https://ntrs.nasa.gov/citations/19870055830
[research_kobald_fischer_2017]: https://doi.org/10.2514/6.2017-4902
[research_kobald_fischer_2018]: https://doi.org/10.2514/1.a34035
[research_kobayakawa_maeda_1978]: https://doi.org/10.2514/3.58403
[research_kobayashi_maita_1995]: https://doi.org/10.2514/6.1995-6002
[research_kobayashi_sato_2001]: https://doi.org/10.2514/6.2001-1912
[research_kobayashi_tanatsugu_2001]: https://doi.org/10.2514/6.2001-3965
[research_kocamer_uzun_2022]: https://doi.org/10.56753/asrel.2022.2.5
[research_koch_wilken_2025]: https://doi.org/10.1007/s12567-025-00597-9
[research_kock_1968]: https://ntrs.nasa.gov/citations/19710005529
[research_kock_1969]: https://ntrs.nasa.gov/citations/19710005051
[research_kock_1970]: https://ntrs.nasa.gov/citations/19710000635
[research_kock_1972]: https://ntrs.nasa.gov/citations/19720011372
[research_koelle_1993]: https://doi.org/10.1016/0094-5765(93)90132-g
[research_koelle_2000]: https://doi.org/10.1007/978-94-010-0894-5_19
[research_koelle_2000_b]: https://doi.org/10.1016/s0094-5765(00)00060-6
[research_koelle_2002]: https://doi.org/10.1016/s0094-5765(02)00090-5
[research_koenig_harris_2017]: https://doi.org/10.1109/aero.2017.7943694
[research_kohlman_schweikhard_1987]: https://doi.org/10.4271/871802
[research_kohrs_1982]: https://doi.org/10.2514/6.1982-1776
[research_koike_takahashi_2018]: https://doi.org/10.2514/6.2018-0289
[research_kokan_olds_2002]: https://doi.org/10.2514/6.2002-3905
[research_kolesnikov_2005]: https://doi.org/10.2514/6.2005-5977
[research_kolnick_1955]: https://ntrs.nasa.gov/citations/19930088817
[research_kolodziej_rasky_2003]: https://doi.org/10.2514/6.2003-3766
[research_komar_christenson_1996]: https://doi.org/10.2514/6.1996-4246
[research_komatsu_ohyagi_2001]: https://doi.org/10.1299/jsmesec.2001.9.83
[research_komatsu_suzuki_2005]: https://doi.org/10.1541/ieejias.125.590
[research_komatsuzaki_doi_2016]: https://doi.org/10.1109/icsens.2016.7808416
[research_kondrashev_lutsenko_2026]: https://doi.org/10.1007/978-3-032-30639-5_42
[research_kondrashov_2023]: https://doi.org/10.1134/s1995421223020120
[research_kong_lee_2009]: https://doi.org/10.1002/mawe.200900426
[research_kongkaew_ruchanurucks_2022]: https://doi.org/10.1115/1.4055081
[research_konstantinidis_forstner_2020]: https://doi.org/10.2514/1.g004760
[research_kontinos_palmer_1999]: https://doi.org/10.2514/2.3523
[research_koo_natali_2018]: https://doi.org/10.2514/1.a33925
[research_koo_sastry_2003]: https://doi.org/10.2514/6.2003-6541
[research_koratkar_chopra_2001]: https://doi.org/10.1088/0964-1726/10/1/301
[research_korn_doehler_2003]: https://doi.org/10.1109/dasc.2003.1245916
[research_korzun_tang_2020]: https://doi.org/10.2514/6.2020-1510
[research_kotfilia_painter_1969]: https://doi.org/10.2514/6.1969-887
[research_kozak_sharipov_2012]: https://doi.org/10.1007/s13538-012-0066-1
[research_kozak_yildiz_2013]: https://doi.org/10.1115/imece2013-63772
[research_kozina_1976]: https://doi.org/10.21236/ada029467
[research_kpca_kalman_filtering_2011]: https://doi.org/10.1115/1.859759.paper9
[research_krabacher_1993]: https://doi.org/10.4271/931400
[research_kramer_2000]: https://ntrs.nasa.gov/citations/20000062019
[research_kramer_2013]: https://ntrs.nasa.gov/citations/20140003882
[research_kramer_2014]: https://ntrs.nasa.gov/citations/20150000562
[research_krammer_holzapfel_2023]: https://doi.org/10.4050/f-0079-2023-18109
[research_krammer_rosenbauer_2022]: https://doi.org/10.1016/j.ifacol.2023.03.042
[research_krammer_scherer_2021]: https://doi.org/10.2514/6.2021-3217
[research_krasuski_wierzbicki_2018]: https://doi.org/10.5604/01.3001.0012.2504
[research_krempasky_1996]: https://doi.org/10.2514/6.1996-3816
[research_kreutz_1971]: https://doi.org/10.4050/jahs.16.17
[research_kriegsman_tao_1974]: https://doi.org/10.2514/6.1974-866
[research_krishnamoorthy_clarke_2016]: https://doi.org/10.1155/2016/8401249
[research_krishnan_sajikumar_2023]: https://doi.org/10.1063/5.0157175
[research_krishnan_thejus_2017]: https://doi.org/10.1109/i2ct.2017.8226156
[research_kroncke_1985]: https://doi.org/10.2514/3.25755
[research_kruger_besselink_1997]: https://doi.org/10.1080/00423119708969352
[research_kruggel_sigal_1999]: https://doi.org/10.2514/6.1999-435
[research_krumenacker_pellicano_1992]: https://doi.org/10.2514/6.1992-4108
[research_kryvoruka_ashurst_1973]: https://doi.org/10.2514/6.1973-183
[research_kubo_suzuki_2007]: https://doi.org/10.2514/6.2007-2752
[research_kubo_suzuki_2008]: https://doi.org/10.2514/1.30122
[research_kubota_hashimoto_2003]: https://doi.org/10.1016/s0094-5765(02)00147-9
[research_kubota_yoko_2020]: https://doi.org/10.2514/1.a34619
[research_kuchinka_1965]: https://doi.org/10.2514/6.1965-328
[research_kudo_kato_1991]: https://doi.org/10.2322/jjsass1969.39.662
[research_kugler_1996]: https://doi.org/10.1049/cp:19960396
[research_kugler_heller_2018]: https://doi.org/10.2514/6.2018-4275
[research_kugler_holzapfel_2017]: https://doi.org/10.23919/acc.2017.7963284
[research_kugler_holzapfel_2017_b]: https://doi.org/10.1109/ccta.2017.8062764
[research_kugler_rhein_2019]: https://doi.org/10.1007/s13272-019-00401-5
[research_kugler_rhein_2019_b]: https://doi.org/10.2514/6.2019-0505
[research_kugler_seiferth_2018]: https://doi.org/10.1109/iccar.2018.8384659
[research_kulik_ruth_2025]: https://doi.org/10.2514/1.g009054
[research_kulu_2025]: https://doi.org/10.52202/083093-0051
[research_kumar_2001]: https://doi.org/10.2514/2.3685
[research_kumar_2010]: https://doi.org/10.14741/ijcet/spl.2.2014.121
[research_kumar_deshpande_2022]: https://doi.org/10.1061/9780784415986.ch7
[research_kumar_dhanush_2024]: https://doi.org/10.55248/gengpi.5.0224.0622
[research_kumar_mahulikar_2016]: https://doi.org/10.1016/j.applthermaleng.2016.04.100
[research_kumar_mahulikar_2017]: https://doi.org/10.2514/1.a33688
[research_kumar_padhi_2024]: https://doi.org/10.1109/icarcv63323.2024.10821656
[research_kumar_rjustus_2023]: https://doi.org/10.61653/joast.v74i4.2022.45
[research_kumar_shanmugam_2007]: https://doi.org/10.2514/6.2007-2736
[research_kumarsulurloganathan_2023]: https://doi.org/10.5772/intechopen.107841
[research_kumtepe_pollack_2022]: https://doi.org/10.2514/6.2022-1597
[research_kundu_1990]: https://doi.org/10.1016/b978-0-12-428770-9.50014-8
[research_kundu_2013]: https://doi.org/10.21236/ada582581
[research_kunwar_chakraborty_2025]: https://doi.org/10.2514/6.2025-0739
[research_kunwar_putra_2026]: https://doi.org/10.2514/6.2026-2288
[research_kuppuswamy_kiran_1981]: https://doi.org/10.2514/6.1981-2381
[research_kurdel_gecejova_2024]: https://doi.org/10.3390/aerospace11010082
[research_kurniawan_stefanie_2022]: https://doi.org/10.30736/je-unisla.v7i1.755
[research_kutluay_mahmutyazicioglu_2009]: https://doi.org/10.2514/6.2009-5724
[research_kuzin_lozin_2009]: https://doi.org/10.2514/6.2009-6732
[research_kwon_park_2013]: https://doi.org/10.9766/kimst.2013.16.3.268
[research_la_shivananda_1993]: https://doi.org/10.2514/6.1993-3692
[research_lachman_ratliff_2025]: https://doi.org/10.52202/083075-0058
[research_laforte_wesley_2015]: https://doi.org/10.4271/2015-01-2076
[research_lagimoniere_avram_2024]: https://doi.org/10.1007/978-3-031-51928-4_51
[research_laguardia_airport_2020]: https://doi.org/10.14359/51724551
[research_laili_widayaka_2024]: https://doi.org/10.26740/jte.v13n2.p152-159
[research_lam_stollenwerk_1966]: https://doi.org/10.2514/6.1966-771
[research_lambregts_1981]: https://doi.org/10.2514/6.1981-1751
[research_lambregts_1982]: https://doi.org/10.2514/6.1982-1599
[research_lamp_luckner_2015]: https://doi.org/10.1007/978-3-319-17518-8_32
[research_lamy_1983]: https://doi.org/10.2514/6.1983-2736
[research_lan_tan_2021]: https://doi.org/10.3390/s21155062
[research_lan_xu_2020]: https://doi.org/10.1061/(asce)as.1943-5525.0001112
[research_lancaster_1977]: https://doi.org/10.2514/6.1977-1194
[research_landherr_klein_1987]: https://doi.org/10.21236/ada200604
[research_landherr_klein_1989]: https://doi.org/10.21236/ada219294
[research_landing_sites_2008]: https://doi.org/10.2307/jj.30346787.6
[research_landing_stripsierra_2020]: https://doi.org/10.2307/j.ctv14z1b9m.26
[research_langberg_tyler_2022]: https://doi.org/10.1109/aero53065.2022.9843527
[research_langelaan_grande_2013]: https://doi.org/10.4050/vfs-f69-0293
[research_langston_1967]: https://doi.org/10.21236/ad0813281
[research_langston_peterson_2021]: https://doi.org/10.2514/1.a34911
[research_lapygin_yakunina_2009]: https://doi.org/10.1016/j.jappmathmech.2009.11.004
[research_larsen_2000]: https://doi.org/10.2514/6.2000-5114
[research_larsen_2003]: https://doi.org/10.2514/6.2003-6407
[research_larsen_2005]: https://doi.org/10.2514/6.2005-6795
[research_larson_1967]: https://ntrs.nasa.gov/citations/19670018288
[research_larson_1972]: https://ntrs.nasa.gov/citations/19720011245
[research_larsson_2020]: https://doi.org/10.3390/aerospace7090135
[research_laub_white_2006]: https://doi.org/10.2514/1.19218
[research_lauer_2006]: https://doi.org/10.2514/6.iac-06-d2.4.08
[research_laumann_1966]: https://doi.org/10.2514/6.1966-772
[research_launius_2013]: https://doi.org/10.2514/5.9781624102172.0001.0024
[research_launius_2013_b]: https://doi.org/10.1111/1600-0498.12037
[research_lavender_1965]: https://doi.org/10.2514/6.1965-1124
[research_lavergne_villaume_2005]: https://doi.org/10.2514/6.2005-5848
[research_law_mcwhorter_1992]: https://doi.org/10.2514/6.1992-1273
[research_lawrance_sukkarieh_2009]: https://doi.org/10.2514/6.2009-6112
[research_lawrence_1952]: https://doi.org/10.21236/ad0021570
[research_lawrence_1993]: https://doi.org/10.1007/978-1-4684-0444-9_2
[research_lawrence_selmon_2001]: https://doi.org/10.2514/6.2001-4207
[research_layton_1969]: https://ntrs.nasa.gov/citations/19700039724
[research_layton_1970]: https://ntrs.nasa.gov/citations/19710000634
[research_le_2025]: https://doi.org/10.1109/comea66280.2025.11241669
[research_le_goo_2019]: https://doi.org/10.2514/1.a34400
[research_le_goo_2021]: https://doi.org/10.2514/1.a34908
[research_le_goo_2021_b]: https://doi.org/10.2514/6.2021-1405
[research_le_goo_2025]: https://doi.org/10.2514/1.a35955
[research_le_han_2023]: https://doi.org/10.2514/6.2023-1136
[research_lebacqz_1977]: https://doi.org/10.2514/6.1977-1143
[research_lee_1957]: https://ntrs.nasa.gov/citations/19750078088
[research_lee_1963]: https://doi.org/10.21236/ad0408930
[research_lee_1973]: https://doi.org/10.21236/ad0761621
[research_lee_1974]: https://doi.org/10.2514/6.1974-869
[research_lee_1976]: https://doi.org/10.2514/3.58677
[research_lee_2009]: https://doi.org/10.1109/dasc.2009.5347474
[research_lee_2011]: https://doi.org/10.2514/6.2011-6499
[research_lee_2023]: https://doi.org/10.1016/j.treng.2023.100204
[research_lee_benedict_2020]: https://doi.org/10.4050/f-0076-2020-16321
[research_lee_chang_1998]: https://doi.org/10.2514/6.1998-4410
[research_lee_cho_2023]: https://doi.org/10.5139/jksas.2023.51.3.149
[research_lee_chung_2019]: https://doi.org/10.3390/s19204468
[research_lee_han_2012]: https://doi.org/10.1088/0964-1726/21/9/094023
[research_lee_jo_2026]: https://doi.org/10.3390/aerospace13010079
[research_lee_kim_2026]: https://doi.org/10.2514/6.2026-5074
[research_lee_mesbahi_2017]: https://doi.org/10.2514/1.g001879
[research_lee_park_2011]: https://doi.org/10.5302/j.icros.2011.17.8.833
[research_lee_park_2021]: https://doi.org/10.3390/app11188555
[research_lee_park_2025]: https://doi.org/10.2514/1.g008809
[research_lee_payan_2022]: https://doi.org/10.1109/dasc55683.2022.9925756
[research_lee_ryu_2003]: https://doi.org/10.1088/0964-1726/12/1/317
[research_lee_soon_2008]: https://doi.org/10.1017/s037346330700464x
[research_lefevre_lock_2025]: https://doi.org/10.2514/1.a35636
[research_legoff_moreau_2013]: https://doi.org/10.1016/j.actaastro.2013.03.025
[research_lei_li_2012]: https://doi.org/10.3390/s121013212
[research_lei_liu_2026]: https://doi.org/10.1007/978-981-95-3031-1_10
[research_lei_xiaogang_2021]: https://doi.org/10.1007/978-981-15-8155-7_222
[research_lei_yan_2017]: https://doi.org/10.2514/6.2017-2256
[research_lei_zhong_2020]: https://doi.org/10.3901/jme.2020.23.107
[research_leisman_2000]: https://doi.org/10.2514/6.2000-5288
[research_leland_taylor_1964]: https://doi.org/10.2514/6.1964-346
[research_lemmens_2011]: https://doi.org/10.1007/978-94-007-1667-4_4
[research_leng_wang_2023]: https://doi.org/10.1017/aer.2022.111
[research_leo_fenza_2014]: https://doi.org/10.2478/meceng-2014-0017
[research_leparoux_herisse_2022]: https://doi.org/10.1109/cdc51059.2022.9992735
[research_lesonen_nazarenko_2020]: https://doi.org/10.1109/weconf48837.2020.9131459
[research_letchworth_2011]: https://doi.org/10.2514/6.2011-7314
[research_leuckert_domhardt_2008]: https://doi.org/10.2514/6.2008-842
[research_levesque_delafontaine_2006]: https://doi.org/10.2514/6.2006-6076
[research_leveugle_reinhard_1999]: https://doi.org/10.2514/6.1999-1705
[research_levin_1968]: https://doi.org/10.2514/6.1968-969
[research_levy_1964]: https://ntrs.nasa.gov/citations/19650019778
[research_lewerenz_1987]: https://doi.org/10.2514/6.1987-1732
[research_li_1989]: https://doi.org/10.2514/6.1989-886
[research_li_2008]: https://doi.org/10.1007/978-3-540-88518-4_119
[research_li_2017]: https://doi.org/10.4108/eai.28-2-2017.152290
[research_li_2020]: https://doi.org/10.1007/978-981-15-3707-3_62
[research_li_2025]: https://doi.org/10.1007/978-981-96-2216-0_14
[research_li_angelov_2024]: https://doi.org/10.1007/978-3-031-72347-6_11
[research_li_bando_2025]: https://doi.org/10.1109/access.2025.3609289
[research_li_chang_2024]: https://doi.org/10.1109/ccdc62350.2024.10587813
[research_li_chao_2016]: https://doi.org/10.1109/chicc.2016.7555065
[research_li_chao_2018]: https://doi.org/10.23919/chicc.2018.8482793
[research_li_chao_2018_b]: https://doi.org/10.1109/gncc42960.2018.9019175
[research_li_chao_2022]: https://doi.org/10.1016/j.ast.2022.107364
[research_li_cheng_2021]: https://doi.org/10.1049/rsn2.12092
[research_li_cui_2006]: https://doi.org/10.1016/j.ast.2005.12.003
[research_li_cui_2007]: https://doi.org/10.1016/j.ast.2007.04.006
[research_li_cui_2011]: https://doi.org/10.1109/icicip.2011.6008189
[research_li_cui_2013]: https://doi.org/10.1109/qr2mse.2013.6625699
[research_li_du_2026]: https://doi.org/10.1016/j.ceramint.2026.04.095
[research_li_duan_2015]: https://doi.org/10.1016/j.ast.2015.01.017
[research_li_hu_2018]: https://doi.org/10.1016/j.ast.2017.12.037
[research_li_hu_2023]: https://doi.org/10.1007/978-981-19-6613-2_627
[research_li_ji_2026]: https://doi.org/10.1109/access.2026.3667479
[research_li_jia_2020]: https://doi.org/10.1109/access.2020.2981015
[research_li_jiang_2017]: https://doi.org/10.2514/1.c034276
[research_li_jing_2008]: https://doi.org/10.1109/isscaa.2008.4776294
[research_li_li_2010]: https://doi.org/10.3724/sp.j.1087.2010.00971
[research_li_li_2018]: https://doi.org/10.1007/978-981-10-6334-3_5
[research_li_li_2018_b]: https://doi.org/10.1007/978-981-10-6334-3_6
[research_li_li_2018_c]: https://doi.org/10.1007/978-981-10-6334-3_4
[research_li_li_2022]: https://doi.org/10.1109/access.2021.3136612
[research_li_li_2023]: https://doi.org/10.1007/978-981-19-6613-2_211
[research_li_li_2025]: https://doi.org/10.52202/083088-0003
[research_li_luo_2022]: https://doi.org/10.1177/09544062211059736
[research_li_pan_2014]: https://doi.org/10.1017/s0373463314000575
[research_li_pei_2025]: https://doi.org/10.1109/cac67268.2025.11487618
[research_li_peng_2019]: https://doi.org/10.1109/icus48101.2019.8996088
[research_li_qi_2023]: https://doi.org/10.1109/itnec56291.2023.10082717
[research_li_qian_2014]: https://doi.org/10.3724/sp.j.1146.2012.01065
[research_li_shen_2010]: https://doi.org/10.1061/41096(366)178
[research_li_shi_2022]: https://doi.org/10.3934/jimo.2020180
[research_li_sun_2023]: https://doi.org/10.1016/j.ssci.2022.105992
[research_li_wang_2016]: https://doi.org/10.1017/s0373463315001083
[research_li_wang_2024]: https://doi.org/10.1142/s2737480724500250
[research_li_wang_2025]: https://doi.org/10.2514/1.a36377
[research_li_wu_2017]: https://doi.org/10.2514/6.2017-2344
[research_li_wu_2024]: https://doi.org/10.1117/12.3014827
[research_li_xia_2024]: https://doi.org/10.3390/drones8100571
[research_li_xiao_2018]: https://doi.org/10.1360/n092018-00034
[research_li_xiao_2021]: https://doi.org/10.1007/978-981-15-8155-7_185
[research_li_xiong_2025]: https://doi.org/10.1088/1742-6596/3044/1/012002
[research_li_xu_2024]: https://doi.org/10.3390/drones8100568
[research_li_xu_2025]: https://doi.org/10.3390/aerospace12040280
[research_li_yang_2012]: https://doi.org/10.4028/www.scientific.net/amr.452-453.548
[research_li_yavuz_2004]: https://doi.org/10.1115/ht-fed2004-56814
[research_li_zeng_2023]: https://doi.org/10.1007/978-981-19-6613-2_690
[research_li_zhai_2024]: https://doi.org/10.1007/978-981-97-5300-0_10
[research_li_zhai_2024_b]: https://doi.org/10.1007/978-981-97-5300-0_12
[research_li_zhang_2012]: https://doi.org/10.1016/s1000-9361(11)60384-1
[research_li_zhang_2021]: https://doi.org/10.1155/2021/9943370
[research_li_zhang_2021_b]: https://doi.org/10.1115/fedsm2021-61455
[research_li_zhang_2023]: https://doi.org/10.3390/app13179828
[research_li_zhao_2023]: https://doi.org/10.1016/j.ast.2023.108616
[research_li_zhao_2025]: https://doi.org/10.1016/j.ast.2025.110226
[research_lian_bang_2004]: https://doi.org/10.2514/6.2004-5328
[research_liang_chin_2021]: https://doi.org/10.3390/app11020509
[research_liang_li_2014]: https://doi.org/10.1109/cgncc.2014.7007320
[research_liang_ren_2018]: https://doi.org/10.2514/1.g003157
[research_liang_wang_2020]: https://doi.org/10.1016/j.ast.2020.106314
[research_liang_xu_2022]: https://doi.org/10.1016/j.ast.2022.107855
[research_liang_xu_2025]: https://doi.org/10.1109/taes.2024.3452051
[research_liano_castillo_2014]: https://doi.org/10.1016/j.ast.2014.10.001
[research_liao_chu_2023]: https://doi.org/10.1016/j.cja.2023.11.020
[research_liao_li_2021]: https://doi.org/10.1007/s10291-020-01056-0
[research_liao_song_2023]: https://doi.org/10.1061/jaeeez.aseng-4668
[research_liaoniwu_yiminhuang_2008]: https://doi.org/10.1109/isscaa.2008.4776287
[research_libo_zhangshengbing_2016]: https://doi.org/10.1109/cgncc.2016.7828846
[research_lieberman_1963]: https://doi.org/10.2514/6.1963-1813
[research_lieske_1966]: https://doi.org/10.21236/ad0809790
[research_lijewski_suhs_1994]: https://doi.org/10.2514/3.46575
[research_likhachev_sikharulidze_2014]: https://doi.org/10.1134/s0038094614070132
[research_lin_cui_2022]: https://doi.org/10.1088/1742-6596/2203/1/012020
[research_lin_meghdadhasheminasab_2020]: https://doi.org/10.1109/icuas48674.2020.9214049
[research_lin_qi_2020]: https://doi.org/10.23919/ccc50068.2020.9188609
[research_lin_tseng_2026]: https://doi.org/10.1177/00368504261448346
[research_lina_whitten_1968]: https://doi.org/10.2514/6.1968-191
[research_lindberg_schade_1997]: https://doi.org/10.2514/6.1997-5629
[research_ling_2017]: https://doi.org/10.2514/6.2017-4210
[research_linlin_jianqiao_2015]: https://doi.org/10.1109/chicc.2015.7260426
[research_liseitsev_2025]: https://doi.org/10.1007/978-981-96-4599-2_21
[research_littell_2007]: https://ntrs.nasa.gov/citations/20070021759
[research_littell_2015]: https://ntrs.nasa.gov/citations/20160005978
[research_littell_2018]: https://ntrs.nasa.gov/citations/20180001969
[research_littell_2019]: https://doi.org/10.2514/6.2019-4504
[research_litvintsev_molchanova_2019]: https://doi.org/10.1088/1742-6596/1404/1/012118
[research_liu_2012]: https://doi.org/10.1201/b12667-17
[research_liu_2025]: https://doi.org/10.1007/978-981-96-2440-9_2
[research_liu_2025_b]: https://doi.org/10.1109/comea66280.2025.11241751
[research_liu_chen_2002]: https://doi.org/10.21236/ada403577
[research_liu_chen_2017]: https://doi.org/10.2991/iccia-17.2017.155
[research_liu_dai_2017]: https://doi.org/10.2514/6.2017-2284
[research_liu_di_2023]: https://doi.org/10.3390/su151612477
[research_liu_ding_2014]: https://doi.org/10.1016/j.actaastro.2014.04.024
[research_liu_dong_2021]: https://doi.org/10.1016/j.cja.2020.04.026
[research_liu_hao_2023]: https://doi.org/10.1007/978-981-19-6613-2_432
[research_liu_he_2017]: https://doi.org/10.23919/chicc.2017.8028281
[research_liu_he_2023]: https://doi.org/10.1007/978-981-19-6613-2_584
[research_liu_hou_2020]: https://doi.org/10.32604/cmes.2020.08124
[research_liu_hu_2023]: https://doi.org/10.1007/978-981-19-6613-2_440
[research_liu_hu_2024]: https://doi.org/10.3390/act13070259
[research_liu_kuang_2025]: https://doi.org/10.1007/978-981-95-3010-6_40
[research_liu_lee_2022]: https://doi.org/10.1109/cacs55319.2022.9969843
[research_liu_li_2006]: https://doi.org/10.2514/6.2006-6547
[research_liu_li_2011]: https://doi.org/10.4028/www.scientific.net/amr.383-390.1452
[research_liu_liu_2015]: https://doi.org/10.1117/12.2205564
[research_liu_liu_2018]: https://doi.org/10.1080/00207179.2018.1426882
[research_liu_liu_2022]: https://doi.org/10.1080/00207179.2022.2106891
[research_liu_liu_2025]: https://doi.org/10.1088/1742-6596/3141/1/012039
[research_liu_liu_2025_b]: https://doi.org/10.1109/rcae66389.2025.11355191
[research_liu_liu_2025_c]: https://doi.org/10.1109/cac67268.2025.11487021
[research_liu_ren_2015]: https://doi.org/10.1108/ijicc-05-2015-0016
[research_liu_sun_2025]: https://doi.org/10.1016/j.conengprac.2025.106314
[research_liu_wang_2011]: https://doi.org/10.1109/icecc.2011.6066471
[research_liu_wang_2016]: https://doi.org/10.1109/chicc.2016.7555029
[research_liu_wang_2020]: https://doi.org/10.1017/s0373463320000582
[research_liu_wang_2023]: https://doi.org/10.3390/aerospace10110953
[research_liu_wang_2023_b]: https://doi.org/10.1145/3632971.3633003
[research_liu_xiao_2019]: https://doi.org/10.1007/978-981-13-6061-9_13
[research_liu_yan_2023]: https://doi.org/10.1109/itoec57671.2023.10291601
[research_liu_zhang_2017]: https://doi.org/10.1016/j.cja.2017.06.008
[research_liu_zhang_2024]: https://doi.org/10.1007/978-981-97-1107-9_37
[research_liu_zhang_2024_b]: https://doi.org/10.1016/j.jfranklin.2024.107218
[research_liu_zhang_2024_c]: https://doi.org/10.23919/ccc63176.2024.10662356
[research_liu_zheng_2021]: https://doi.org/10.23919/ccc52363.2021.9550644
[research_liu_zhou_2006]: https://doi.org/10.1109/chicc.2006.280702
[research_liuzhi_wangyong_2012]: https://doi.org/10.1109/aero.2012.6187321
[research_lobl_weiss_2018]: https://doi.org/10.2514/6.2018-1598
[research_lockman_1967]: https://ntrs.nasa.gov/citations/19670060153
[research_logan_1976]: https://doi.org/10.21236/ada029372
[research_logan_1978]: https://doi.org/10.21236/ada065298
[research_logsdon_williamson_1997]: https://doi.org/10.1016/s0265-9646(97)00010-6
[research_london_1999]: https://ntrs.nasa.gov/citations/19990116207
[research_long_1968]: https://doi.org/10.2514/6.1968-264
[research_longani_2000]: https://doi.org/10.1063/1.1302572
[research_looye_joos_2001]: https://doi.org/10.2514/6.2001-4206
[research_looye_joos_2002]: https://doi.org/10.2514/6.2002-4666
[research_looye_sancho_2002]: https://doi.org/10.2514/6.2002-4854
[research_looye_willemsen_2001]: https://doi.org/10.2514/6.2001-4208
[research_lopez_1993]: https://doi.org/10.1109/62.210639
[research_loureiro_soares_2019]: https://doi.org/10.1007/978-3-030-36150-1_11
[research_lovell_1956]: https://ntrs.nasa.gov/citations/19930084570
[research_lovtsov_karpov_2011]: https://doi.org/10.1134/s003809461107015x
[research_low_lift_to_drag_1985]: https://doi.org/10.2514/5.9781600865718.0378.0394
[research_lp_based_2013]: https://doi.org/10.21535/c6fhqe39
[research_lu_1996]: https://doi.org/10.2514/6.1996-1426
[research_lu_1997]: https://doi.org/10.2514/2.4008
[research_lu_1999]: https://ntrs.nasa.gov/citations/19990100665
[research_lu_2021]: https://doi.org/10.1007/978-981-16-1075-2_2
[research_lu_2021_b]: https://doi.org/10.1007/978-981-16-1075-2_3
[research_lu_antoun_2005]: https://doi.org/10.2514/1.9118
[research_lu_harris_2017]: https://doi.org/10.1109/icuas.2017.7991399
[research_lu_lei_2010]: https://doi.org/10.1108/00022661011028074
[research_lu_lei_2017]: https://doi.org/10.1038/s41598-017-04061-5
[research_lu_tao_2025]: https://doi.org/10.1007/978-981-97-9765-3_21
[research_lu_wang_2010]: https://doi.org/10.4028/www.scientific.net/amm.42.118
[research_lu_wang_2021]: https://doi.org/10.1109/icpics52425.2021.9524290
[research_lu_yang_2018]: https://doi.org/10.1063/1.5020226
[research_lu_yue_2024]: https://doi.org/10.1007/978-981-99-8048-2_270
[research_lu_zhang_2015]: https://doi.org/10.1016/j.ssci.2014.12.005
[research_lu_zhang_2016]: https://doi.org/10.1016/j.ssci.2016.06.018
[research_lu_zhang_2019]: https://doi.org/10.1016/j.cja.2019.09.010
[research_lucas_1978]: https://doi.org/10.21236/adb028240
[research_lugo_dwyercianciolo_2022]: https://doi.org/10.2514/6.2022-0607
[research_lugo_tolson_2014]: https://doi.org/10.2514/6.2014-0388
[research_lukeke_yujinyong_2016]: https://doi.org/10.1109/cgncc.2016.7829047
[research_lund_2004]: https://doi.org/10.2514/6.2004-6544
[research_lungu_2017]: https://doi.org/10.2316/p.2017.848-004
[research_lungu_lungu_2011]: https://doi.org/10.1109/lindi.2011.6031131
[research_lungu_lungu_2015]: https://doi.org/10.1002/asjc.1133
[research_lungu_lungu_2015_b]: https://doi.org/10.1115/1.4032028
[research_lungu_lungu_2018]: https://doi.org/10.1002/asjc.1810
[research_luo_guo_2021]: https://doi.org/10.1186/s43020-021-00061-z
[research_luo_li_2011]: https://doi.org/10.1007/s11432-011-4193-z
[research_luo_liu_2025]: https://doi.org/10.1007/978-981-96-2236-8_45
[research_luo_song_2025]: https://doi.org/10.1007/978-981-96-2264-1_30
[research_luo_tang_2026]: https://doi.org/10.1016/j.icheatmasstransfer.2026.111984
[research_luo_wu_2022]: https://doi.org/10.1016/j.asr.2022.02.049
[research_luong_le_2025]: https://doi.org/10.3390/mi16030355
[research_luria_guyton_1992]: https://doi.org/10.4271/922008
[research_lusty_miele_1966]: https://doi.org/10.2514/3.3866
[research_luyangliang_fengzhou_2016]: https://doi.org/10.1109/cgncc.2016.7828964
[research_lv_an_2021]: https://doi.org/10.1007/978-981-16-3142-9_41
[research_lv_fan_2024]: https://doi.org/10.3390/s24051645
[research_lv_wang_2023]: https://doi.org/10.1016/j.neucom.2022.11.057
[research_lv_zhou_2023]: https://doi.org/10.1142/s2737480723500115
[research_lykken_shah_1971]: https://doi.org/10.2514/6.1971-906
[research_lyons_1961]: https://doi.org/10.21236/ad0271681
[research_lyons_1977]: https://doi.org/10.1051/rphysap:01977001202038500
[research_lystad_1975]: https://doi.org/10.21236/ada024072
[research_m2_f2_1967]: https://ntrs.nasa.gov/citations/19670022976
[research_ma_chen_2018]: https://doi.org/10.1109/ccdc.2018.8407160
[research_ma_ding_2025]: https://doi.org/10.3390/aerospace12010063
[research_ma_guan_2018]: https://doi.org/10.23919/chicc.2018.8482717
[research_ma_liu_2024]: https://doi.org/10.23919/ccc63176.2024.10661212
[research_ma_sun_2013]: https://doi.org/10.4028/www.scientific.net/amr.753-755.1595
[research_ma_wu_2013]: https://doi.org/10.4028/www.scientific.net/amr.871.69
[research_ma_wu_2020]: https://doi.org/10.1109/icca51439.2020.9264516
[research_ma_zhao_2005]: https://doi.org/10.1007/978-3-540-27009-6_20
[research_maass_woicke_2020]: https://doi.org/10.2514/1.g004850
[research_macallister_1955]: https://doi.org/10.21236/ad0062045
[research_macconochie_2000]: https://ntrs.nasa.gov/citations/20000115607
[research_machin_daum_2026]: https://doi.org/10.2514/6.2026-3852
[research_machnik_decker_2022]: https://doi.org/10.5162/ettc2022/4.2
[research_mackay_ellingson_2016]: https://doi.org/10.2514/6.2016-1137
[research_mackinnon_madden_1971]: https://doi.org/10.2514/6.1971-957
[research_macklnnon_madden_1972]: https://doi.org/10.2514/3.59028
[research_macleod_2026]: https://doi.org/10.59332/jbis-079-01-0017
[research_macmillan_1981]: https://doi.org/10.2514/6.1981-2350
[research_macy_shea_1989]: https://doi.org/10.4271/892335
[research_madden_1958]: https://doi.org/10.21236/ad0160389
[research_madden_desai_1973]: https://doi.org/10.2514/6.1973-903
[research_maddock_minisci_2016]: https://doi.org/10.1109/ssci.2016.7850109
[research_madigan_1970]: https://doi.org/10.1002/j.2161-4296.1970.tb00025.x
[research_maeda_otsuki_2014]: https://doi.org/10.1299/jsmemovic.2014.12._3c22-1_
[research_maeda_otsuki_2016]: https://doi.org/10.2514/6.2016-5595
[research_maemori_tanigawa_2003]: https://doi.org/10.1115/detc2003/dac-48765
[research_maggin_1947]: https://ntrs.nasa.gov/citations/19930081903
[research_mahmood_2025]: https://doi.org/10.1007/s42496-025-00285-1
[research_mahmood_rehman_2022]: https://doi.org/10.3390/drones6110360
[research_mahmood_urrehman_2023]: https://doi.org/10.1016/j.rico.2023.100259
[research_mahmoud_maaruf_2021]: https://doi.org/10.1007/s40435-020-00738-4
[research_mahony_hamel_2001]: https://doi.org/10.1016/s0947-3580(01)70939-9
[research_mahoor_godzdanker_2010]: https://doi.org/10.1007/978-94-007-1110-5_17
[research_mahrous_khalil_2026]: https://doi.org/10.1088/1742-6596/3283/1/012028
[research_mahulikar_khurana_2008]: https://doi.org/10.1007/bf03256567
[research_maikapar_1993]: https://doi.org/10.1007/bf01050055
[research_maiorova_prosuntsov_2016]: https://doi.org/10.1007/s10891-016-1406-8
[research_maita_kobayashi_1996]: https://doi.org/10.2514/6.1996-6005
[research_maita_stockmans_1993]: https://doi.org/10.2514/6.1993-5010
[research_maiuzzo_1970]: https://doi.org/10.21236/ad0707129
[research_makarenko_makarov_2017]: https://doi.org/10.21778/2413-9599-2017-1-96-103
[research_malloy_chang_1998]: https://doi.org/10.1115/1.2802410
[research_mammarella_rodrigalvarez_2011]: https://doi.org/10.1007/978-3-642-19817-5_32
[research_mandal_gu_2016]: https://doi.org/10.2514/6.2016-0636
[research_manfred_ryno_2008]: https://doi.org/10.1109/icnsurv.2008.4559165
[research_mangum_1965]: https://doi.org/10.21236/ad0656438
[research_mani_2007]: https://doi.org/10.1109/dasc.2007.4391941
[research_manjarrez_davila_2018]: https://doi.org/10.23919/acc.2018.8430789
[research_manke_1970]: https://ntrs.nasa.gov/citations/19710000630
[research_manley_2000]: https://ntrs.nasa.gov/citations/20000040788
[research_mannai_1962]: https://doi.org/10.1016/0016-0032(62)91055-4
[research_manning_baum_1992]: https://doi.org/10.2514/6.1992-4115
[research_manning_gleason_1992]: https://doi.org/10.2514/6.1992-4425
[research_manokaran_vidya_2009]: https://doi.org/10.2514/1.39732
[research_mao_dou_2018]: https://doi.org/10.1002/rnc.4349
[research_mao_xue_2019]: https://doi.org/10.1007/978-981-13-3305-7_10
[research_marantos_karras_2017]: https://doi.org/10.1007/s10846-017-0702-7
[research_marcum_1998]: https://doi.org/10.1109/7.705891
[research_marcum_1998_b]: https://doi.org/10.1109/7.640264
[research_marcum_2000]: https://doi.org/10.1002/j.2161-4296.2000.tb00217.x
[research_margaria_dovis_2007]: https://doi.org/10.5081/jgps.6.1.89
[research_marinelli_green_1988]: https://doi.org/10.2514/6.1988-2667
[research_marioandrescordoba_2001]: https://doi.org/10.1016/s1474-6670(17)40758-0
[research_mark_2009]: https://ntrs.nasa.gov/citations/20090026521
[research_marley_driscoll_2017]: https://doi.org/10.2514/6.2017-0118
[research_marley_driscoll_2018]: https://doi.org/10.2514/6.2018-0280
[research_marlow_2003]: https://doi.org/10.2514/6.2003-5281
[research_marschall_2011]: https://doi.org/10.21236/ada553782
[research_marshall_1986_b]: https://doi.org/10.1126/science.231.4734.105
[research_marshall_cronin_2011]: https://doi.org/10.21236/ada547656
[research_marshall_sun_2021]: https://doi.org/10.1016/j.arcontrol.2021.10.013
[research_martin_2006]: https://doi.org/10.2514/6.2006-4960
[research_martin_boyd_2008]: https://doi.org/10.2514/6.2008-3805
[research_martin_hallam_2004]: https://doi.org/10.1177/1045389x04042797
[research_martin_panesi_2022]: https://doi.org/10.2514/1.a35029
[research_martin_stay_2024]: https://doi.org/10.1115/imece2024-142760
[research_martindale_2006]: https://doi.org/10.21236/ada457121
[research_martinezmoran_2018]: https://doi.org/10.5162/ettc2018/11.1
[research_martins_rassi_2025]: https://doi.org/10.3390/proceedings2025129019
[research_martorella_kelly_1981]: https://doi.org/10.2514/6.1981-1710
[research_marylin_christian_2007]: https://doi.org/10.1166/sl.2007.016
[research_masafumimorimoto_kenjiuchiyama_2007]: https://doi.org/10.1109/iccas.2007.4406858
[research_masaki_yakura_1968]: https://doi.org/10.2514/6.1968-1155
[research_masilamani_kumar_2018]: https://doi.org/10.18520/cs/v114/i01/84-100
[research_mason_zahn_2021]: https://doi.org/10.2514/6.2021-0569
[research_massa_1995]: https://doi.org/10.21236/ada299179
[research_mastromatteo_gaverina_2023]: https://doi.org/10.12783/shm2023/37054
[research_mastromatteo_gaverina_2026]: https://doi.org/10.58286/33864
[research_mathavaraj_halbe_2010]: https://doi.org/10.2514/6.2010-8312
[research_mathavaraj_padhi_2020]: https://doi.org/10.1142/s230138502050003x
[research_mathematical_model_2023]: https://doi.org/10.36652/0869-4931-2023-77-1-20-26
[research_mathew_dutta_2023]: https://doi.org/10.1007/978-981-19-6945-4_67
[research_matranga_1959a]: https://ntrs.nasa.gov/citations/19630004018
[research_matranga_1959b]: https://ntrs.nasa.gov/citations/19980235626
[research_matranga_1961]: https://ntrs.nasa.gov/citations/19980227282
[research_matsuda_kihara_2013]: https://doi.org/10.1016/j.proeng.2013.12.025
[research_matsumoto_kondoh_2015]: https://doi.org/10.2514/6.2015-1772
[research_matsunaga_takahashi_2017]: https://doi.org/10.2514/6.2017-0263
[research_matveev_2017]: https://doi.org/10.23919/icins.2017.7995628
[research_mauritz_1997]: https://ntrs.nasa.gov/citations/20210005070
[research_maurya_wang_2021]: https://doi.org/10.4050/jahs.66.042005
[research_maxwell_2017]: https://doi.org/10.2514/6.2017-4317
[research_mayanna_grimm_2006]: https://doi.org/10.2514/6.2006-6037
[research_mayhue_1962]: https://ntrs.nasa.gov/citations/19620003288
[research_mazaheri_bruce_2014]: https://doi.org/10.2514/1.a32721
[research_mazur_2020]: https://doi.org/10.1201/9780429070372-43
[research_mbagwu_dalle_2023]: https://doi.org/10.2514/1.c037186
[research_mcafee_alpert_2025]: https://doi.org/10.2514/6.2025-2704
[research_mcafee_rabin_2026]: https://doi.org/10.2514/1.a36673
[research_mcanally_engel_1979]: https://doi.org/10.2514/6.1979-508
[research_mccabe_brown_2017]: https://doi.org/10.2514/6.2017-1498
[research_mccabe_demars_2018]: https://doi.org/10.2514/6.2018-1332
[research_mccafferty_woodward_2014]: https://doi.org/10.2514/6.2014-0979
[research_mcclinton_voland_1998]: https://doi.org/10.2514/6.1998-2866
[research_mcclure_1998]: https://doi.org/10.2514/6.1998-5139
[research_mccown_mcclintick_2000]: https://doi.org/10.4050/vfs-f56-00026
[research_mcdowell_williamsonjr_1980]: https://doi.org/10.2514/6.1980-1605
[research_mcdowell_williamsonjr_1982]: https://doi.org/10.2514/6.1982-1376
[research_mcfarland_1981]: https://doi.org/10.1109/taes.1981.309154
[research_mcfarland_1991]: https://doi.org/10.1002/j.2161-4296.1991.tb01857.x
[research_mcfarland_1994]: https://doi.org/10.1109/7.303767
[research_mcgee_1977]: https://doi.org/10.2514/6.1977-603
[research_mcgee_foster_1981]: https://doi.org/10.2514/6.1981-1857
[research_mcgee_paulkjr_1981]: https://doi.org/10.2514/3.56096
[research_mcgehee_1959]: https://ntrs.nasa.gov/citations/19980228040
[research_mcguire_gage_2004]: https://doi.org/10.2514/6.2004-4490
[research_mckenzie_2003]: https://doi.org/10.2514/6.iac-03-v.3.02
[research_mckown_nd]: https://ntrs.nasa.gov/citations/20220008976
[research_mcnally_1988]: https://doi.org/10.2514/6.1988-2134
[research_mcnally_warner_1992]: https://doi.org/10.1002/j.2161-4296.1992.tb01872.x
[research_mcquellin_buttsworth_2024]: https://doi.org/10.2514/6.2024-2889
[research_mctigue_1970]: https://ntrs.nasa.gov/citations/19710000628
[research_mctigue_ryan_1968]: https://doi.org/10.1111/j.1749-6632.1968.tb15241.x
[research_mead_1998]: https://doi.org/10.21236/ada405839
[research_meckler_1965]: https://doi.org/10.21236/ad0620959
[research_mehmood_majeed_2021]: https://doi.org/10.1109/icase54940.2021.9904209
[research_mehra_1971]: https://doi.org/10.1109/tac.1971.1099744
[research_mehrotra_robinson_1982]: https://doi.org/10.2514/6.1982-602
[research_mehta_1989]: https://doi.org/10.2514/6.1989-1670
[research_mehta_bowles_2001]: https://doi.org/10.2514/2.5886
[research_mehta_bowles_2001_b]: https://doi.org/10.2514/6.2001-1795
[research_mehta_bowles_2012]: https://doi.org/10.2514/6.2012-5874
[research_mehta_bowles_2014]: https://doi.org/10.1017/s0001924000009970
[research_mejias_eng_2012]: https://doi.org/10.1007/s10846-012-9767-5
[research_melgaard_1986]: https://doi.org/10.2514/6.1986-9762
[research_melnyk_beattie_2021]: https://doi.org/10.1115/imece2021-66606
[research_mendes_langley_1999]: https://doi.org/10.1002/j.2161-4296.1999.tb02393.x
[research_mendham_2003]: https://doi.org/10.2514/6.iac-03-v.p.11
[research_menees_wilson_1987]: https://doi.org/10.2514/6.1987-2565
[research_meng_gao_2022]: https://doi.org/10.1117/12.2635153
[research_meng_he_2018]: https://doi.org/10.1109/gncc42960.2018.9018958
[research_meng_jiang_2016]: https://doi.org/10.1109/chicc.2016.7554371
[research_meng_wang_2019]: https://doi.org/10.1016/j.ast.2018.12.030
[research_meng_wu_2009]: https://doi.org/10.1007/s11432-009-0182-x
[research_menon_ck_2025]: https://doi.org/10.1007/s11038-025-09574-y
[research_menon_postlethwaite_2009]: https://doi.org/10.1016/j.conengprac.2008.12.002
[research_menon_vaddi_2010]: https://doi.org/10.2514/6.2010-7702
[research_menou_nd]: https://doi.org/10.70675/01a02ab5zdcb3z4b95zb05czfea1b906f3dc
[research_meriwether_1962]: https://doi.org/10.21236/ad0404420
[research_merlin_2006]: https://doi.org/10.2514/6.2006-7467
[research_merlin_2014]: https://ntrs.nasa.gov/citations/20140008618
[research_meseguer_perezgrande_2012]: https://doi.org/10.1533/9780857096081.305
[research_methodology_for_2022]: https://doi.org/10.36652/0869-4931-2022-76-12-551-554
[research_metzger_1970]: https://doi.org/10.21236/ad0714111
[research_meyer_1970]: https://doi.org/10.4271/700322
[research_meyerjr_jarvis_1981]: https://doi.org/10.2514/6.1981-2468
[research_meyers_tompkins_1968]: https://doi.org/10.21236/ad0675443
[research_meyers_weiderman_1988]: https://doi.org/10.21236/ada204850
[research_meyerson_1990]: https://ntrs.nasa.gov/citations/19900058866
[research_meyerson_1998]: https://doi.org/10.1061/40339(206)21
[research_meyerson_taylor_2001]: https://doi.org/10.2514/6.2001-2069
[research_mhenni_choley_2016]: https://doi.org/10.1016/j.ifacol.2016.07.076
[research_mi_lu_2018]: https://doi.org/10.23919/chicc.2018.8482701
[research_miao_wang_2026]: https://doi.org/10.1016/j.ast.2026.113155
[research_miccio_veneruso_2024]: https://doi.org/10.1109/dasc62030.2024.10749415
[research_michalski_johnson_2007]: https://doi.org/10.2514/6.2007-6273
[research_mickelson_carrico_1989]: https://doi.org/10.2514/6.1989-3498
[research_microwave_scanning_1977]: https://ntrs.nasa.gov/citations/19770018189
[research_midtfjord_huseby_2020]: https://doi.org/10.3850/978-981-14-8593-0_3717-cd
[research_miele_wang_1987]: https://doi.org/10.2514/6.1987-2341
[research_miele_wang_1988]: https://doi.org/10.1007/bf00939681
[research_miele_wang_1988_b]: https://doi.org/10.2514/6.1988-4069
[research_mikhailov_nedelko_2012]: https://doi.org/10.3103/s1068799812030130
[research_mikhailov_nedelko_2012_b]: https://doi.org/10.3103/s1068799812020067
[research_miki_fujii_2018]: https://doi.org/10.2514/6.2018-0382
[research_mikrin_orlovskii_2020]: https://doi.org/10.23919/icins43215.2020.9133923
[research_mikula_holthaus_2000]: https://doi.org/10.2514/6.2000-5073
[research_miller_1963]: https://doi.org/10.21236/ad0429015
[research_miller_kazemba_2023]: https://doi.org/10.2514/1.a35500
[research_miller_kazemba_2023_b]: https://doi.org/10.2514/1.a35595
[research_millerjr_1979]: https://doi.org/10.2514/6.1979-1678
[research_milner_2002]: https://doi.org/10.21236/ada408426
[research_milner_macabiau_2022]: https://doi.org/10.33012/2022.18422
[research_milos_chen_2013]: https://doi.org/10.2514/1.a32302
[research_milos_squire_1999]: https://doi.org/10.2514/2.3449
[research_minami_tsukamoto_2006]: https://doi.org/10.2514/6.2006-8120
[research_minghui_qiuying_2017]: https://doi.org/10.1109/cpgps.2017.8075089
[research_minisci_vasile_2013]: https://doi.org/10.2514/1.j051573
[research_minnema_mayersoares_2019]: https://doi.org/10.26678/abcm.cobem2019.cob2019-1726
[research_minor_2004]: https://doi.org/10.2514/6.2004-6836
[research_minwen_dayi_2014]: https://doi.org/10.1016/j.ast.2014.05.004
[research_miotto_lepome_2003]: https://doi.org/10.2514/6.2003-5360
[research_miotto_paduano_1995]: https://doi.org/10.2514/6.1995-3190
[research_miotto_paduano_1996]: https://doi.org/10.2514/3.21778
[research_miso_1999]: https://doi.org/10.1109/7.766929
[research_misra_bai_2019]: https://doi.org/10.2514/1.g004160
[research_misra_fraticellirivera_2022]: https://doi.org/10.58940/2374-6793.1754
[research_mitchell_2004]: https://ntrs.nasa.gov/citations/20040040180
[research_mitchell_hoh_1983]: https://doi.org/10.2514/6.1983-2106
[research_miyakawa_hirose_1985]: https://doi.org/10.2514/6.1985-5025
[research_miyashita_sugihara_2024]: https://doi.org/10.1088/1361-6463/ad4718
[research_miyazawa_ishikawa_1993]: https://doi.org/10.2514/6.1993-3818
[research_miyazawa_ishikawa_1996]: https://doi.org/10.2514/6.1996-3782
[research_miyazawa_motoda_1998]: https://doi.org/10.2514/6.1998-4428
[research_miyazawa_motoda_1999]: https://doi.org/10.2514/2.4480
[research_mo_jianhua_2018]: https://doi.org/10.1109/gncc42960.2018.9019152
[research_mo_li_2024]: https://doi.org/10.1007/s11071-023-09233-9
[research_mo_lu_2023]: https://doi.org/10.1007/978-981-99-0479-2_167
[research_mobile_autonomous_2024]: https://doi.org/10.3901/jme.2024.03.034
[research_mockenhaupt_wells_1981]: https://doi.org/10.2514/6.1981-1579
[research_modeling_of_design_2017]: https://doi.org/10.20535/0203-3771342017122918
[research_mohaghegh_2025]: https://doi.org/10.2139/ssrn.5772903
[research_mohamed_mamatas_2012]: https://doi.org/10.5772/31093
[research_mohamed_safwat_2022]: https://doi.org/10.1109/iceeng49683.2022.9782063
[research_mohammadkarimi_nobahari_2018]: https://doi.org/10.1002/navi.232
[research_mohan_s_2025]: https://doi.org/10.1016/j.jsse.2025.10.004
[research_mohiuddin_2025]: https://doi.org/10.52202/083076-0124
[research_moholkar_2024]: https://doi.org/10.1007/978-3-031-64836-6_1
[research_moholkar_2025]: https://doi.org/10.52783/anvi.v28.4126
[research_moiseev_poluboyarinov_2011]: https://doi.org/10.3103/s1068799811010016
[research_mokrane_benallegue_2022]: https://doi.org/10.3390/s22228865
[research_mokry_1974]: https://doi.org/10.2514/6.1974-83
[research_molchanova_kashkovsky_2016]: https://doi.org/10.1063/1.4964079
[research_molina_simeonides_1996]: https://doi.org/10.2514/6.1996-2468
[research_monteil_2024]: https://doi.org/10.5162/ettc2024/a1.4
[research_montella_vio_2024]: https://doi.org/10.52202/078369-0025
[research_monti_paterna_2001]: https://doi.org/10.1016/s1290-0729(01)01267-4
[research_moog_1979]: https://ntrs.nasa.gov/citations/19790042653
[research_mooij_2003]: https://doi.org/10.2514/6.2003-5322
[research_mooij_2024]: https://doi.org/10.1007/978-3-031-62174-1_8
[research_mooij_hanninen_2009]: https://doi.org/10.2514/6.2009-5770
[research_moore_1991]: https://ntrs.nasa.gov/citations/19920010688
[research_moore_2013]: https://doi.org/10.2514/6.2013-1380
[research_moorhouse_1990]: https://doi.org/10.2514/6.1990-3306
[research_moorhouse_1991]: https://doi.org/10.2514/6.1991-2641
[research_moorhouse_1994]: https://doi.org/10.2514/6.1994-2106
[research_moorhouse_fielding_1998]: https://doi.org/10.2514/6.1998-4568
[research_moran_mcquellin_2023]: https://doi.org/10.2514/6.2023-1385
[research_moreira_gripp_2022]: https://doi.org/10.2514/1.g006443
[research_morelli_1995]: https://doi.org/10.2514/6.1995-3499
[research_morelli_2009]: https://doi.org/10.2514/1.37092
[research_morello_1977]: https://ntrs.nasa.gov/citations/19780005111
[research_moreno_fugenschuh_2018]: https://doi.org/10.1007/978-3-319-89920-6_59
[research_morgado_garbacz_2022]: https://doi.org/10.2514/1.j061071
[research_morgan_williams_2025]: https://doi.org/10.2514/6.2025-1513
[research_morgenfeld_1992]: https://doi.org/10.2514/6.1992-1087
[research_mori_maita_1999]: https://doi.org/10.2514/6.1999-4801
[research_mori_maita_2001]: https://doi.org/10.2514/6.2001-1791
[research_morino_shimoda_2001]: https://doi.org/10.1163/156855101753415364
[research_morio_cazaurang_2009]: https://doi.org/10.1016/j.conengprac.2008.10.018
[research_morio_cazaurang_2010]: https://doi.org/10.1049/iet-cta.2008.0463
[research_morio_falcoz_2007]: https://doi.org/10.3182/20070625-5-fr-2916.00096
[research_moriwaki_2015]: https://doi.org/10.1016/j.ifacol.2015.05.056
[research_morrisjr_1995]: https://doi.org/10.2514/6.1995-6052
[research_morrison_chien_1982]: https://doi.org/10.2514/6.1982-1306
[research_morth_1972]: https://doi.org/10.2514/6.1972-833
[research_mosby_1965]: https://doi.org/10.2514/6.1965-711
[research_moses_1999]: https://ntrs.nasa.gov/citations/19990115467
[research_motaghedi_2003]: https://doi.org/10.1117/12.487303
[research_motoda_miyazawa_1999]: https://doi.org/10.2514/3.27199
[research_moura_borgesribeiro_2025]: https://doi.org/10.26678/abcm.cobem2025.cob2025-0360
[research_moura_borgesribeiro_2025_b]: https://doi.org/10.26678/abcm.cobem2025.cob2025-0300
[research_moura_borgesribeiro_2025_c]: https://doi.org/10.26678/abcm.cobem2025.cob2025-1507
[research_mourikis_trawny_2007]: https://doi.org/10.15607/rss.2007.iii.019
[research_mouritsen_1994]: https://doi.org/10.2514/6.1994-3488
[research_mowry_grasso_2020]: https://doi.org/10.1007/978-3-030-36308-6_92
[research_mu_yu_2016]: https://doi.org/10.1016/j.ifacol.2016.09.079
[research_mu_yu_2018]: https://doi.org/10.1016/j.actaastro.2017.10.027
[research_mu_yu_2019]: https://doi.org/10.1007/978-981-15-0474-7_106
[research_mu_zhang_2014]: https://doi.org/10.1155/2014/541627
[research_mu_zhang_2023]: https://doi.org/10.1007/978-981-19-6613-2_290
[research_muehter_1974]: https://doi.org/10.21236/ada043526
[research_mueller_landolt_2012]: https://doi.org/10.2514/6.2012-3317
[research_muhammadhadiwidanto_rizkifitriansyah_2025]: https://doi.org/10.35894/jtk.v10i1.230
[research_muhlsteinjr_petroff_1974]: https://doi.org/10.2514/6.1974-632
[research_mukhopadhyay_1969]: https://doi.org/10.2514/6.1969-128
[research_mukundan_maity_2022]: https://doi.org/10.1016/j.ifacol.2023.03.007
[research_mulcare_ness_1982]: https://doi.org/10.2514/6.1982-1626
[research_mullenix_povitsky_2016]: https://doi.org/10.2514/1.a33380
[research_multi_architecture_design_2025]: https://doi.org/10.3901/jme.2025.19.273
[research_multiple_inertial_1962]: https://doi.org/10.2514/5.9781600864827.0349.0366
[research_mumm_holzapfel_2017]: https://doi.org/10.1109/ccta.2017.8062608
[research_munguia_2014]: https://doi.org/10.1016/s1665-6423(14)70096-3
[research_munusamy_stephen_2022]: https://doi.org/10.13111/2066-8201.2022.14.3.3
[research_munzing_catris_2015]: https://doi.org/10.4271/2015-01-2129
[research_muraca_1975]: https://ntrs.nasa.gov/citations/19750012375
[research_murakami_kwak_2008]: https://doi.org/10.2514/6.2008-7488
[research_murali_moreno_2024]: https://doi.org/10.1109/icra57147.2024.10610780
[research_murch_cox_2009]: https://doi.org/10.2514/6.2009-2054
[research_murciapineros_vilhenademoraes_2022]: https://doi.org/10.1016/j.asr.2022.05.031
[research_murman_1982]: https://ntrs.nasa.gov/citations/19820017335
[research_murphy_1956]: https://doi.org/10.21236/ad0093521
[research_murphy_1963]: https://doi.org/10.21236/ad0442757
[research_murraysmith_1995]: https://doi.org/10.1007/978-1-4615-2504-2_11
[research_murri_1984]: https://ntrs.nasa.gov/citations/19840009116
[research_musal_hm_1964]: https://doi.org/10.21236/ad0449823
[research_mwenegoha_moore_2019]: https://doi.org/10.3390/s19112467
[research_nabi_najafi_2024]: https://doi.org/10.1115/ht2024-131509
[research_nadan_lee_2018]: https://doi.org/10.1115/imece2018-86615
[research_naeseth_1970]: https://ntrs.nasa.gov/citations/19700031351
[research_naftel_1986]: https://ntrs.nasa.gov/citations/19860035004
[research_naftel_1993]: https://ntrs.nasa.gov/citations/19930017827
[research_nag_senthil_2023]: https://doi.org/10.61653/joast.v65i2.2013.721
[research_nagarani_venkatakrishnan_2020]: https://doi.org/10.1016/j.comcom.2019.12.039
[research_nagarjuna_suresh_2015]: https://doi.org/10.1109/icscn.2015.7219864
[research_nagel_1983]: https://ntrs.nasa.gov/citations/19840002103
[research_najam_2014]: https://doi.org/10.1089/space.2013.0027
[research_najson_mease_2005]: https://doi.org/10.2514/6.2005-6289
[research_nakamura_kamimura_2014]: https://doi.org/10.1016/j.ast.2014.07.015
[research_nakasato_takahashi_2015]: https://doi.org/10.1115/ajkfluids2015-13593
[research_nakhod_2026]: https://doi.org/10.62717/3083-7057-2026-1-102
[research_nance_2013]: https://doi.org/10.21236/ada571259
[research_nanda_gopalakrishna_2025]: https://doi.org/10.1504/ijesms.2025.10072232
[research_narkiewicz_2002]: https://doi.org/10.4050/vfs-f58-00017
[research_nasa_ivhm_2000]: https://ntrs.nasa.gov/citations/20010071157
[research_nastasi_martorella_1983]: https://doi.org/10.2514/6.1983-2072
[research_nathan_2007]: https://doi.org/10.2514/6.2007-4540
[research_navigation_and_1964]: https://doi.org/10.2514/5.9781600864872.0391.0419
[research_navigation_grade_inertial_2022]: https://doi.org/10.1049/sbra550e_ch8
[research_nazar_gandhi_2020]: https://doi.org/10.1007/978-3-030-55115-5_21
[research_nazir_aziz_2018]: https://doi.org/10.1109/idap.2018.8620824
[research_neal_1970]: https://doi.org/10.4271/700237
[research_neal_1973]: https://doi.org/10.1002/j.2161-4296.1973.tb01176.x
[research_nebylov_nebylov_2011]: https://doi.org/10.3182/20110828-6-it-1002.02582
[research_nedelko_alimov_2018]: https://doi.org/10.3103/s1068799818020058
[research_negre_1991]: https://doi.org/10.1016/b978-0-08-036203-8.50016-x
[research_nelson_2003]: https://doi.org/10.2514/6.2003-7018
[research_nelson_arenajr_1993]: https://doi.org/10.2514/6.1993-93
[research_nelson_price_1997]: https://doi.org/10.2514/6.1997-195
[research_neri_macabiau_2010]: https://doi.org/10.1109/plans.2010.5507222
[research_neuhaus_2018]: https://ntrs.nasa.gov/citations/20180001968
[research_neumaier_kranemann_2022]: https://doi.org/10.3390/aerospace9030140
[research_neumannn_moore_2016]: https://doi.org/10.5162/etc2016/3.1
[research_neusypin_kupriyanov_2023]: https://doi.org/10.1007/s10291-023-01433-5
[research_newman_bailey_1987]: https://doi.org/10.21236/ada194602
[research_newman_fulcher_1992]: https://doi.org/10.2514/6.1992-2722
[research_newman_parham_2014]: https://doi.org/10.4050/f-0070-2014-9490
[research_newsom_1975]: https://ntrs.nasa.gov/citations/19750022036
[research_ngo_blake_2003]: https://doi.org/10.2514/6.2003-5738
[research_ngo_doman_2002]: https://doi.org/10.1109/acc.2002.1023917
[research_nguyen_2022]: https://doi.org/10.1109/vppc55846.2022.10003396
[research_nguyen_cao_2018]: https://doi.org/10.1109/icarcv.2018.8581117
[research_nguyen_jacklin_2010]: https://doi.org/10.1007/978-3-642-10690-3_5
[research_nguyen_kostiukov_2020]: https://doi.org/10.3846/aviation.2020.12424
[research_nho_agarwal_1998]: https://doi.org/10.2514/6.1998-4484
[research_ni_dai_2023]: https://doi.org/10.23919/icins51816.2023.10168471
[research_ni_wei_2026]: https://doi.org/10.1109/csis-iac70275.2026.11585053
[research_nial_1972]: https://doi.org/10.2514/6.1972-787
[research_nicolaides_1953]: https://doi.org/10.21236/ad0026405
[research_nicolaides_1969]: https://doi.org/10.21236/ad0867092
[research_nie_zhang_2023]: https://doi.org/10.1007/978-981-19-6613-2_250
[research_niebanck_1969]: https://doi.org/10.4050/vfs-f25-025
[research_niehaus_1962]: https://doi.org/10.4050/jahs.7.24
[research_nielson_swearingen_1986]: https://doi.org/10.1109/maes.1986.5005069
[research_niemela_1982]: https://doi.org/10.1002/j.2161-4296.1982.tb00813.x
[research_nietubicz_1975]: https://doi.org/10.21236/ada009704
[research_niewald_parker_1999]: https://doi.org/10.2514/6.1999-768
[research_ning_zhang_2007]: https://doi.org/10.1016/s1000-9361(07)60001-6
[research_ninomiya_suzuki_2005]: https://doi.org/10.2514/6.2005-3274
[research_ninomiya_suzuki_2006]: https://doi.org/10.2514/1.23265
[research_nippress_wilson_1992]: https://doi.org/10.2514/6.1992-1229
[research_niu_meng_2019]: https://doi.org/10.3390/rs11202404
[research_niu_wang_2025]: https://doi.org/10.1007/s10291-025-01967-w
[research_nizin_antony_2016]: https://doi.org/10.1109/iicpe.2016.8079437
[research_nobahari_mohammadkarimi_2017]: https://doi.org/10.1002/navi.195
[research_nogar_2020]: https://doi.org/10.1109/ssrr50563.2020.9292607
[research_noh_sharif_2024]: https://doi.org/10.1007/978-3-031-68751-8_5
[research_nomura_itabashi_2022]: https://doi.org/10.1007/978-981-19-2689-1_49
[research_nonami_kendoul_2010]: https://doi.org/10.1007/978-4-431-53856-1_13
[research_nonami_kendoul_2010_b]: https://doi.org/10.1007/978-4-431-53856-1_10
[research_nonlinear_flight_2004]: https://doi.org/10.2514/6.iac-04-a.4.07
[research_norton_1922]: https://ntrs.nasa.gov/citations/19930080929
[research_norwood_chichester_2015]: https://doi.org/10.2514/6.2015-0459
[research_noureldin_karamat_2012]: https://doi.org/10.1007/978-3-642-30466-8_4
[research_noureldin_karamat_2012_b]: https://doi.org/10.1007/978-3-642-30466-8_5
[research_novakovic_2014]: https://doi.org/10.4271/2014-01-2186
[research_nowak_kopecki_2022]: https://doi.org/10.3390/aerospace9060285
[research_nuhija_2021]: https://doi.org/10.47305/jlia2163090n
[research_numata_tsuchiya_2013]: https://doi.org/10.2514/6.2013-1023
[research_numerical_optimization_2016]: https://doi.org/10.21275/v5i6.nov164465
[research_nurse_prohaska_1978]: https://doi.org/10.21236/ada062810
[research_nurse_prohaska_1978_b]: https://doi.org/10.21236/ada062809
[research_nutt_martindale_1976]: https://doi.org/10.21236/ada025080
[research_o_kelly_1955]: https://ntrs.nasa.gov/citations/20090023313
[research_obermann_williamson_1998]: https://doi.org/10.1016/s0265-9646(97)00041-6
[research_obermark_2004]: https://doi.org/10.21236/ada422954
[research_obye_hakim_1984]: https://doi.org/10.2514/6.1984-1176
[research_ocallaghan_2016]: https://doi.org/10.2514/6.2016-4364
[research_ochi_2004]: https://doi.org/10.1111/j.1934-6093.2004.tb00211.x
[research_octavianie_ichsan_2020]: https://doi.org/10.46509/ajtk.v3i2.179
[research_oertel_1993]: https://doi.org/10.1007/978-3-642-45720-3_8
[research_oglesby_1975]: https://ntrs.nasa.gov/citations/19750056555
[research_ogneru_raileanu_2026]: https://doi.org/10.13111/2066-8201.2026.18.2.9
[research_ohara_2001]: https://doi.org/10.2514/6.2001-4038
[research_ohe_oyama_2014]: https://doi.org/10.2514/6.2014-3954
[research_ohkami_yamanaka_1991]: https://doi.org/10.2514/6.1991-5085
[research_ohno_yamaguchi_1998]: https://doi.org/10.1016/s1474-6670(17)41088-3
[research_ohno_yamaguchi_1999]: https://doi.org/10.1016/s0967-0661(99)00085-4
[research_ohya_kato_1985]: https://doi.org/10.2322/jjsass1969.33.540
[research_oishi_2002]: https://ntrs.nasa.gov/citations/20020091923
[research_okada_1994]: https://doi.org/10.4271/940001
[research_okafor_jemitola_2018]: https://doi.org/10.4314/njt.v37i3.9
[research_okojie_go_2023]: https://doi.org/10.1109/aero55745.2023.10115771
[research_olds_1998]: https://doi.org/10.21236/ada389224
[research_olds_bellini_1998]: https://doi.org/10.2514/6.1998-1557
[research_olds_bradford_1999]: https://doi.org/10.2514/6.1999-4944
[research_olejnik_kachel_2019]: https://doi.org/10.1051/matecconf/201930402010
[research_olejnik_kachel_2020]: https://doi.org/10.1177/0954410020934301
[research_olivaresmendez_mondragon_2013]: https://doi.org/10.3182/20131120-3-fr-4045.00011
[research_olson_2015]: https://doi.org/10.2514/6.2015-2397
[research_olson_sunkel_1983]: https://doi.org/10.2514/3.8519
[research_olynick_1996]: https://doi.org/10.2514/6.1996-1857
[research_olynick_1998]: https://doi.org/10.2514/2.3338
[research_olynick_henline_1996]: https://doi.org/10.2514/3.26842
[research_optimal_glide_1981]: https://doi.org/10.1016/b978-0-444-41961-3.50023-1
[research_orbital_aerodynamic_1981]: https://doi.org/10.1016/b978-0-444-41961-3.50024-3
[research_orbitec_orbital_1990]: https://doi.org/10.2514/5.9781600866005.0366.0373
[research_ortloff_1968]: https://doi.org/10.21236/ad0830727
[research_osder_1970]: https://ntrs.nasa.gov/citations/19700031646
[research_otsu_2016]: https://doi.org/10.2322/tastj.14.pe_7
[research_otsu_2018]: https://doi.org/10.2322/tastj.16.588
[research_otsu_abe_2006]: https://doi.org/10.2322/jjsass.54.181
[research_otsu_kanai_2001]: https://doi.org/10.2514/6.2001-2831
[research_otsu_katsurayama_2009]: https://doi.org/10.2514/6.2009-3729
[research_otsu_matsuda_2006]: https://doi.org/10.2514/6.2006-3566
[research_otsu_matsushita_2004]: https://doi.org/10.2514/6.2004-2167
[research_otsu_nakamura_2008]: https://doi.org/10.2514/6.2008-3897
[research_otsu_suzuki_1998]: https://doi.org/10.2514/6.1998-2447
[research_otsu_takama_2012]: https://doi.org/10.1007/978-3-642-25688-2_103
[research_otsu_yamada_2015]: https://doi.org/10.2514/6.2015-2808
[research_oudin_puyou_2013]: https://doi.org/10.2514/6.2013-5235
[research_ouellette_patil_2012]: https://doi.org/10.2514/6.2012-4640
[research_ouellette_patil_2014]: https://doi.org/10.2514/6.2014-0032
[research_ouyang_wu_2021]: https://doi.org/10.23919/icins43216.2021.9470873
[research_owens_cox_2006]: https://doi.org/10.2514/6.2006-3306
[research_oza_hu_2015]: https://doi.org/10.2514/6.2015-2288
[research_pace_maji_2008]: https://doi.org/10.1061/40988(323)37
[research_paciorri_assonitis_2026]: https://doi.org/10.2514/1.a36600
[research_packard_seiler_2009]: https://doi.org/10.21236/ada531629
[research_padhi_chawla_2016]: https://doi.org/10.1201/b12690-20
[research_padmanabhan_dowell_2015]: https://doi.org/10.2514/1.c033027
[research_painter_1972]: https://ntrs.nasa.gov/citations/19720018367
[research_painter_1974]: https://ntrs.nasa.gov/citations/19740006640
[research_palaninathan_bindu_2005]: https://doi.org/10.2514/1.10710
[research_paletta_belardo_2013]: https://doi.org/10.4271/2013-01-2188
[research_paletta_dmytriv_2015]: https://doi.org/10.1016/j.proeng.2015.08.030
[research_pallister_parker_1992]: https://doi.org/10.2514/6.1992-3985
[research_palmer_henline_1997]: https://doi.org/10.2514/2.3261
[research_palmer_pulsonetti_2009]: https://doi.org/10.2514/1.40478
[research_palomino_2022]: https://doi.org/10.5162/ettc2022/2.4
[research_palumbo_morani_2012]: https://doi.org/10.2514/6.2012-5857
[research_pan_ma_2025]: https://doi.org/10.1088/1742-6596/3126/1/012065
[research_panda_2022]: https://doi.org/10.2514/6.2022-2127
[research_panzieri_pascucci_2002]: https://doi.org/10.1109/tmech.2002.1011250
[research_paolozzi_2004]: https://doi.org/10.1299/jsmemecjsm.2004.8.0_303
[research_papadopoulos_subrahmanyam_2005]: https://doi.org/10.2514/6.2005-3206
[research_paquita_persadanta_2024]: https://doi.org/10.52989/jaet.v4i2.148
[research_paraforos_griepentrog_2015]: https://doi.org/10.3920/978-90-8686-814-8_33
[research_paranjape_2023]: https://doi.org/10.2514/6.2023-0983
[research_park_1980]: https://ntrs.nasa.gov/citations/19800018917
[research_park_2020]: https://doi.org/10.2514/1.g004058
[research_park_jung_2019]: https://doi.org/10.2514/1.g003400
[research_park_kim_2015]: https://doi.org/10.1109/iciev.2015.7334046
[research_park_lee_2012]: https://doi.org/10.1007/s11771-012-1106-2
[research_park_park_2017]: https://doi.org/10.1016/j.asr.2017.05.004
[research_park_yang_2025]: https://doi.org/10.5302/j.icros.2025.24.0218
[research_parker_2022]: https://doi.org/10.21236/ad1180064
[research_parker_templeman_1967]: https://doi.org/10.2514/6.1967-573
[research_parkinson_fitzgibbon_1989]: https://doi.org/10.1017/s0373463300015083
[research_parlett_1974]: https://ntrs.nasa.gov/citations/19740013536
[research_parlett_1974_b]: https://ntrs.nasa.gov/citations/19740012543
[research_parlini_1988]: https://doi.org/10.2514/6.1988-2076
[research_parracino_ceresoli_2024]: https://doi.org/10.52202/078368-0033
[research_parrish_1975]: https://ntrs.nasa.gov/citations/19750024959
[research_part_i_1997]: https://doi.org/10.2514/5.9781600866463.0013.0013
[research_part_ii_1997]: https://doi.org/10.2514/5.9781600866463.0179.0179
[research_pashilkar_haijun_2016]: https://doi.org/10.1201/b12690-28
[research_pasindu_2020]: https://doi.org/10.1016/j.trpro.2020.08.038
[research_pasindu_fwa_2015]: https://doi.org/10.1007/s40890-015-0001-6
[research_pastore_delfini_2021]: https://doi.org/10.2514/1.a34997
[research_patel_subbarao_2024]: https://doi.org/10.2514/1.g007549
[research_patel_venkatasubbaiah_2015]: https://doi.org/10.1061/(asce)as.1943-5525.0000397
[research_patera_2006]: https://doi.org/10.2514/6.2006-6500
[research_patrick_1972]: https://doi.org/10.1108/eb034932
[research_paul_suresh_2019]: https://doi.org/10.4271/01-12-02-0009
[research_paulson_1947]: https://ntrs.nasa.gov/citations/20050019336
[research_paulson_1947_b]: https://ntrs.nasa.gov/citations/20050029418
[research_paulson_1959]: https://ntrs.nasa.gov/citations/19980230602
[research_pausder_meyer_1983]: https://doi.org/10.2514/6.1983-2735
[research_pavanasam_anil_2024]: https://doi.org/10.4271/2024-26-0447
[research_pavlinsky_1993]: https://doi.org/10.2514/6.1993-2677
[research_pavlov_simakova_2021]: https://doi.org/10.33950/spacetech-2308-7625-2021-3-5-13
[research_payne_shoaf_1975]: https://doi.org/10.21236/adb008929
[research_peach_1980]: https://ntrs.nasa.gov/citations/19810055776
[research_peck_nd]: https://ntrs.nasa.gov/citations/20250010026
[research_peele_1968]: https://ntrs.nasa.gov/citations/19680022579
[research_pei_liu_2025]: https://doi.org/10.1109/rcae66389.2025.11355157
[research_peicheng_rong_2018]: https://doi.org/10.1109/icarcv.2018.8581289
[research_peipei_junbo_2017]: https://doi.org/10.2514/6.2017-2227
[research_pelt_1981]: https://doi.org/10.2514/6.1981-2375
[research_penagamboa_martineztorres_2026]: https://doi.org/10.1201/9781003643456-16
[research_peng_li_2025]: https://doi.org/10.1016/j.isatra.2025.10.052
[research_peng_qi_2019]: https://doi.org/10.1109/ccdc.2019.8832538
[research_peng_qi_2020]: https://doi.org/10.1016/j.jfranklin.2020.07.014
[research_pengxin_feng_2015]: https://doi.org/10.1109/ccdc.2015.7162512
[research_penland_romeo_1971]: https://doi.org/10.2514/3.59185
[research_penland_romeo_1971_b]: https://doi.org/10.2514/6.1971-132
[research_penn_lindley_1997]: https://doi.org/10.1063/1.52129
[research_perepelkina_fedotov_2023]: https://doi.org/10.23919/icins51816.2023.10168400
[research_perez_theodoulis_2022]: https://doi.org/10.1016/j.ifacol.2022.09.057
[research_perezrus_legal_2024]: https://doi.org/10.5162/ettc2024/b3.2
[research_performance_and_2018]: https://doi.org/10.33140/atcp.01.02.07
[research_perkasa_krisbudiman_2024]: https://doi.org/10.1063/5.0202288
[research_perkins_tannasjr_1967]: https://doi.org/10.2514/6.1967-597
[research_perminov_1969]: https://doi.org/10.1007/bf01015966
[research_perry_schneider_1984]: https://doi.org/10.2514/6.1984-2449
[research_peshekhonov_2020]: https://doi.org/10.1134/s2075108720040094
[research_pessanhasantos_lobo_2023]: https://doi.org/10.3390/drones7040243
[research_peter_umap_2021]: https://doi.org/10.32628/ijsrset2183196
[research_petersen_1981]: https://doi.org/10.2514/6.1981-2417
[research_petley_smith_1984]: https://doi.org/10.2514/3.57689
[research_petrishchev_2018]: https://doi.org/10.17587/mau.19.725-733
[research_petrovic_maneski_2018]: https://doi.org/10.1016/j.prostr.2018.12.076
[research_pettersson_rizzi_2006]: https://doi.org/10.2514/6.2006-3162
[research_pezzella_viviani_2024]: https://doi.org/10.1007/s42496-024-00211-x
[research_pfaff_1968]: https://doi.org/10.21236/ad0832104
[research_phatak_1985]: https://ntrs.nasa.gov/citations/19850018380
[research_phillips_1973]: https://doi.org/10.21236/ad0765489
[research_phillips_2008]: https://doi.org/10.2514/1.31327
[research_phillips_kryvoruka_1973]: https://doi.org/10.2514/6.1973-878
[research_phillips_wilson_1983]: https://doi.org/10.2514/3.56345
[research_pi_1988]: https://doi.org/10.2514/3.45700
[research_piacquadio_pridohl_2023]: https://doi.org/10.3390/aerospace10030319
[research_pienkowski_whitmore_2003]: https://doi.org/10.2514/6.2003-908
[research_pieper_perry_2018]: https://doi.org/10.2514/6.2018-4996
[research_pietlahanier_serre_2017]: https://doi.org/10.2514/6.2017-2197
[research_pilyugin_talipov_1994]: https://doi.org/10.1007/bf02324316
[research_pines_hueschen_1978]: https://doi.org/10.2514/6.1978-1296
[research_pipenberg_keennon_2019]: https://doi.org/10.2514/6.2019-0620
[research_pirooz_mirmahdi_2021]: https://doi.org/10.1007/s42452-021-04320-1
[research_pittman_dillon_1977]: https://doi.org/10.2514/3.44633
[research_pitts_kourtides_1989]: https://doi.org/10.2514/6.1989-1772
[research_platou_1968]: https://doi.org/10.2514/6.1968-388
[research_platus_1967]: https://doi.org/10.21236/ad0810587
[research_platus_1978]: https://doi.org/10.2514/6.1978-1367
[research_platus_1979]: https://doi.org/10.2514/6.1979-1670
[research_platus_1980]: https://doi.org/10.2514/6.1980-1574
[research_platus_1983]: https://doi.org/10.2514/6.1983-2111
[research_plinge_2003]: https://doi.org/10.1177/002029400303600603
[research_plumb_1971]: https://doi.org/10.1021/ed048p119
[research_podruzhin_zagidulin_2017]: https://doi.org/10.3103/s1068799817030047
[research_pogorelov_2008]: https://doi.org/10.1134/s0010952508030076
[research_pogorelov_2009]: https://doi.org/10.1134/s0010952509010067
[research_pogosyan_vereikin_2020]: https://doi.org/10.34759/vst-2020-3-7-22
[research_pohly_kang_2018]: https://doi.org/10.2514/6.2018-0020
[research_pollack_urch_1991]: https://doi.org/10.4271/911199
[research_polsgrove_2018]: https://ntrs.nasa.gov/citations/20180006829
[research_polsgrove_2018_b]: https://ntrs.nasa.gov/citations/20180006608
[research_ponton_warnes_2007]: https://doi.org/10.1115/gt2007-27408
[research_poritzky_1970]: https://doi.org/10.2514/6.1970-937
[research_post_dagli_2004]: https://doi.org/10.1002/j.2334-5837.2004.tb00591.x
[research_poteet_abukhajeel_2004]: https://doi.org/10.2514/1.9174
[research_poteet_blosser_2004]: https://doi.org/10.2514/1.9193
[research_pothjr_fisher_1993]: https://doi.org/10.2514/6.1993-3955
[research_pouly_lauffenburger_2009]: https://doi.org/10.3182/20090902-3-us-2007.0061
[research_pouya_saghafi_2009]: https://doi.org/10.1109/icas.2009.8
[research_powell_1959]: https://doi.org/10.1109/tane3.1959.4201679
[research_powell_1960]: https://doi.org/10.1002/j.2161-4296.1960.tb01992.x
[research_powell_1991]: https://ntrs.nasa.gov/citations/19910034496
[research_powers_1984]: https://ntrs.nasa.gov/citations/19850001764
[research_powers_1986]: https://ntrs.nasa.gov/citations/19870030482
[research_prachand_rakshith_2025]: https://doi.org/10.2514/6.2025-2347
[research_pragadheswaran_balguri_2015]: https://doi.org/10.1109/race.2015.7097261
[research_pragenau_1966]: https://ntrs.nasa.gov/citations/19660059586
[research_pragenau_1967]: https://ntrs.nasa.gov/citations/19670059067
[research_prahl_1968]: https://doi.org/10.1017/s0001924000083445
[research_prakash_zhong_2008]: https://doi.org/10.2514/6.2008-744
[research_prakash_zhong_2009]: https://doi.org/10.2514/6.2009-1542
[research_prasad_2022]: https://doi.org/10.13111/2066-8201.2022.14.1.10
[research_prasad_comandur_2018]: https://doi.org/10.4050/f-0074-2018-12780
[research_pravitra_johnson_2024]: https://doi.org/10.1142/s2301385025500220
[research_preliminary_subsystem_1990]: https://ntrs.nasa.gov/citations/19910008835
[research_preliminary_subsystem_1990_b]: https://ntrs.nasa.gov/citations/19900016723
[research_preliminary_subsystem_1990_c]: https://ntrs.nasa.gov/citations/19900014139
[research_prilliman_1966]: https://doi.org/10.2514/6.1966-14
[research_primich_1963]: https://doi.org/10.21236/ad0427050
[research_principles_of_2022]: https://doi.org/10.15394/eaglepub.2022.1066.n14
[research_prislin_1967]: https://ntrs.nasa.gov/citations/19670030344
[research_prislin_nd]: https://ntrs.nasa.gov/citations/19660017583
[research_pritchard_2001]: https://doi.org/10.2514/2.2744
[research_pruin_1970]: https://ntrs.nasa.gov/citations/19700028523
[research_pu_wang_2024]: https://doi.org/10.1007/978-981-99-8048-2_278
[research_pu_xiaodong_2021]: https://doi.org/10.1007/978-981-16-7423-5_96
[research_purcell_wicklund_2025]: https://doi.org/10.2514/6.2025-0202
[research_pusztai_lowenberg_2024]: https://doi.org/10.2514/6.2024-1497
[research_putman_1969]: https://doi.org/10.21236/ad0859807
[research_putnam_nd]: https://ntrs.nasa.gov/citations/20230006168
[research_putov_putov_2015]: https://doi.org/10.1109/scm.2015.7190429
[research_putov_putov_2016]: https://doi.org/10.1109/scm.2016.7519720
[research_pv_laxman_2023]: https://doi.org/10.1109/aero55745.2023.10115772
[research_pv_thomas_2017]: https://doi.org/10.2514/6.2017-1517
[research_pyle_1970]: https://ntrs.nasa.gov/citations/19710000631
[research_pyle_1971]: https://ntrs.nasa.gov/citations/19710009392
[research_pyle_1973]: https://ntrs.nasa.gov/citations/19740006622
[research_pytka_2023]: https://doi.org/10.1201/9781003312765-3
[research_qayyum_bhatti_2017]: https://doi.org/10.1109/ccdc.2017.7978809
[research_qi_li_2021]: https://doi.org/10.1186/s42774-021-00082-x
[research_qi_liu_2026]: https://doi.org/10.1016/j.jnlssr.2026.100290
[research_qi_zhao_2018]: https://doi.org/10.23919/acc.2018.8431539
[research_qi_zhao_2025]: https://doi.org/10.1109/ictis68762.2025.11215011
[research_qian_jiang_2012]: https://doi.org/10.3182/20120829-3-mx-2028.00014
[research_qian_qi_2014]: https://doi.org/10.1109/cgncc.2014.7007434
[research_qian_wang_2015]: https://doi.org/10.5623/cig2015-205
[research_qian_wang_2022]: https://doi.org/10.1080/10298436.2022.2101054
[research_qian_zhai_2012]: https://doi.org/10.4028/www.scientific.net/amr.466-467.1202
[research_qin_fu_2023]: https://doi.org/10.1007/978-981-99-0479-2_190
[research_qinchangmao_qinaiming_2010]: https://doi.org/10.1109/cmce.2010.5610285
[research_qiu_sang_2019]: https://doi.org/10.1007/978-981-13-3305-7_26
[research_qu_zhang_2023]: https://doi.org/10.1109/icma57826.2023.10215607
[research_quast_henke_1990]: https://doi.org/10.2514/6.1990-3045
[research_quinn_1963]: https://doi.org/10.21236/ad0431128
[research_r_sridhar_2022]: https://doi.org/10.1149/10701.1063ecst
[research_r_ss_2025]: https://doi.org/10.52202/080555-0012
[research_rabinskiy_tushavina_2019]: https://doi.org/10.52571/ptq.v16.n33.2019.672_periodico33_pgs_657_667.pdf
[research_radar_altimeter_2019]: https://doi.org/10.1109/icnsurv.2019.8735127
[research_radforth_1987]: https://doi.org/10.1017/s0373463300000357
[research_radhakrishnan_hari_2023]: https://doi.org/10.1007/s40435-023-01126-4
[research_radhakrishnan_hari_2024]: https://doi.org/10.1007/s40435-024-01477-6
[research_rafatnia_nourmohammadi_2019]: https://doi.org/10.1007/s10291-019-0845-z
[research_ragheb_dantsker_2013]: https://doi.org/10.2514/6.2013-2806
[research_rainey_1958]: https://ntrs.nasa.gov/citations/19930093826
[research_raja_2011]: https://doi.org/10.1109/aero.2011.5747518
[research_rajawana_smithmaitrie_2020]: https://doi.org/10.18178/ijmerr.9.7.1065-1071
[research_rajeshyadav_mohammadfaisal_2016]: https://doi.org/10.1007/978-81-322-2743-4_13
[research_rajukulkarni_larocca_2019]: https://doi.org/10.2514/6.2019-1208
[research_rajukulkarni_larocca_2022]: https://doi.org/10.1016/j.paerosci.2021.100798
[research_rajukulkarni_varriale_2019]: https://doi.org/10.2514/6.2019-3089
[research_rakow_waas_2005]: https://doi.org/10.2514/1.9741
[research_ralph_1999]: https://doi.org/10.4271/1999-01-5521
[research_raman_anderson_2000]: https://doi.org/10.2514/6.2000-534
[research_ramasamy_2015]: https://doi.org/10.2514/6.2015-0085
[research_ramirez_dux_2025]: https://doi.org/10.1109/robosoft63089.2025.11020912
[research_rammon_nirbito_2019]: https://doi.org/10.1088/1757-899x/685/1/012006
[research_rana_chudoba_2016]: https://doi.org/10.2514/6.2016-5319
[research_randolph_mullenax_2015]: https://doi.org/10.1109/aero.2015.7119212
[research_raney_1987]: https://doi.org/10.2514/6.1987-2625
[research_raney_1989]: https://ntrs.nasa.gov/citations/19890012431
[research_rang_gutmann_1979]: https://doi.org/10.21236/ada076021
[research_rao_sarma_2001]: https://doi.org/10.1017/s0373463301001333
[research_rao_uhlig_2012]: https://doi.org/10.2514/6.2012-2768
[research_rao_zhang_2022]: https://doi.org/10.1049/icp.2022.1772
[research_raquet_amt_2008]: https://doi.org/10.2514/6.2008-1618
[research_rashmikoushiketal_2020]: https://doi.org/10.24247/ijmperdjun2020726
[research_rasky_1995]: https://doi.org/10.4271/951618
[research_rasky_milos_2001]: https://doi.org/10.2514/2.3686
[research_rasky_pittman_2006]: https://doi.org/10.2514/6.2006-7208
[research_rasmussen_1979]: https://doi.org/10.2514/6.1979-1665
[research_rataczak_boyd_2024]: https://doi.org/10.2514/6.2024-0461
[research_ravichandran_ahmed_2023]: https://doi.org/10.2514/6.2023-3060
[research_raymer_2001]: https://doi.org/10.2514/6.2001-5246
[research_re_entry_thermal_1972]: https://doi.org/10.2514/5.9781600865039.0319.0331
[research_re_entry_vehicle_1981]: https://doi.org/10.2514/5.9781600865510.0287.0306
[research_recker_gribble_2018]: https://doi.org/10.1109/aipr.2018.8707418
[research_rector_hattendorf_1967]: https://doi.org/10.1002/j.2161-4296.1967.tb02553.x
[research_redd_1979]: https://ntrs.nasa.gov/citations/19800002782
[research_redding_jr_1984]: https://doi.org/10.21236/adb143755
[research_redesigned_aircraft_1987]: https://doi.org/10.1016/0308-9126(87)90458-5
[research_rediess_1994]: https://doi.org/10.2514/6.1994-2172
[research_redlich_1971]: https://doi.org/10.1109/taes.1971.310325
[research_redondogutierrez_seelbinder_2022]: https://doi.org/10.2514/6.2022-1842
[research_reed_1966]: https://ntrs.nasa.gov/citations/19710006451
[research_reed_1997]: https://ntrs.nasa.gov/citations/19980169231
[research_reedmohn_2000]: https://doi.org/10.1016/s1067-991x(00)90065-8
[research_reentry_control_2000]: https://doi.org/10.1201/9781482296914-23
[research_reentry_maneuvering_2025]: https://doi.org/10.37285/bsp.sacad2025.03
[research_reentry_vehicle_1977]: https://doi.org/10.2514/6.1977-428
[research_reich_willits_2015]: https://doi.org/10.4050/f-0071-2015-10101
[research_reiley_1991]: https://doi.org/10.1117/12.43736
[research_reimann_2016]: https://doi.org/10.2514/6.2016-3578
[research_reiser_villani_2024]: https://doi.org/10.1017/aer.2024.37
[research_ren_cai_2011]: https://doi.org/10.3724/sp.j.1218.2011.00502
[research_ren_fu_2017]: https://doi.org/10.1177/1687814017703900
[research_ren_ma_2025]: https://doi.org/10.1016/j.ast.2025.110080
[research_ren_wang_2018]: https://doi.org/10.23919/chicc.2018.8483181
[research_ren_wang_2023]: https://doi.org/10.1007/978-981-99-8861-7_47
[research_ren_wang_2025]: https://doi.org/10.3233/atde250081
[research_ren_zi_2020]: https://doi.org/10.23919/icins43215.2020.9133853
[research_research_on_2023]: https://doi.org/10.33140/jeee.02.03.06
[research_research_on_attitude_2012]: https://doi.org/10.4156/ijact.vol4.issue14.20
[research_response_analysis_2026]: https://doi.org/10.3901/jme.260010
[research_reusable_launch_2026]: https://doi.org/10.3901/jme.260002
[research_reusable_space_1999]: https://doi.org/10.2514/5.9781600862380.0275.0327
[research_rey_2000]: https://doi.org/10.1063/1.1290921
[research_reyhanoglu_alvarado_2013]: https://doi.org/10.1016/j.actaastro.2013.01.018
[research_reynerson_2006]: https://doi.org/10.2514/6.2006-6275
[research_reynolds_number_2000]: https://doi.org/10.1017/cbo9780511529535.007
[research_rezaifard_abbasi_2017]: https://doi.org/10.1109/iraniancee.2017.7985144
[research_ribarich_1967]: https://doi.org/10.2514/6.1967-544
[research_ricciardi_2016]: https://doi.org/10.2514/1.c033171
[research_ricciardi_maddock_2020]: https://doi.org/10.2514/6.2020-2403
[research_ricciardi_minwalla_2016]: https://doi.org/10.2514/6.2016-1435
[research_rice_1946]: https://doi.org/10.21236/adb803248
[research_rice_hazlwood_1994]: https://doi.org/10.2514/6.1994-2166
[research_rice_locksley_2000]: https://doi.org/10.21236/ada375749
[research_richards_erickson_2019]: https://doi.org/10.2514/6.2019-0759
[research_richards_tate_2023]: https://doi.org/10.2514/6.2023-3521
[research_richardson_1976]: https://doi.org/10.21236/adb012971
[research_richeson_pines_2007]: https://doi.org/10.2514/6.2007-6791
[research_richmond_2022]: https://doi.org/10.2514/6.2022-2608
[research_ridha_1968]: https://doi.org/10.2514/6.1968-328
[research_rigali_sterk_1980]: https://doi.org/10.2514/6.1980-1455
[research_rigatos_2012]: https://doi.org/10.1016/j.robot.2012.03.001
[research_rigatos_abbaszadeh_2023]: https://doi.org/10.1016/j.ifacsc.2023.100225
[research_rimani_viola_2022]: https://doi.org/10.3390/aerospace9120823
[research_rimer_sperling_1965]: https://doi.org/10.2514/6.1965-1437
[research_rimer_sperling_1966]: https://doi.org/10.2514/3.28507
[research_rimmer_1952]: https://doi.org/10.1108/eb032120
[research_ringel_panerai_2022]: https://doi.org/10.2514/6.2022-3947
[research_rithirun_sooraksa_2013]: https://doi.org/10.4028/www.scientific.net/amr.677.442
[research_ritter_neumann_2016]: https://doi.org/10.2514/1.j053384
[research_rivera_hein_2025]: https://doi.org/10.4050/f-0081-2025-0087
[research_rivers_1968]: https://doi.org/10.2514/3.29345
[research_rivers_1991]: https://ntrs.nasa.gov/citations/19920057409
[research_rizvi_he_2013]: https://doi.org/10.4028/www.scientific.net/amm.390.161
[research_robaglia_libine_2018]: https://doi.org/10.2514/6.2018-1461
[research_roberts_1988]: https://doi.org/10.2514/6.1988-2077
[research_roberts_1990]: https://doi.org/10.2514/6.1990-1265
[research_roberts_2024]: https://doi.org/10.33545/26648776.2024.v6.i1a.57
[research_roberts_bhanu_1992]: https://doi.org/10.1002/rob.4620090608
[research_robertson_1992]: https://doi.org/10.2514/6.1992-4076
[research_robertson_2017]: https://doi.org/10.2514/6.2017-1897
[research_robinson_nolen_1995]: https://doi.org/10.2514/6.1995-3606
[research_robinson_ouhabi_2025]: https://doi.org/10.2514/6.2025-3234
[research_robust_airspeed_2009]: https://doi.org/10.5302/j.icros.2009.15.8.859
[research_rocha_bauzermedeiros_2025]: https://doi.org/10.2514/6.2025-1821
[research_rochelle_roberts_1972]: https://doi.org/10.2514/6.1972-314
[research_rodi_bennett_2012]: https://doi.org/10.2514/6.2012-3221
[research_rodriguez_2005]: https://ntrs.nasa.gov/citations/20050204032
[research_roenneke_cornwell_1992]: https://doi.org/10.2514/6.1992-1146
[research_roenneke_well_1995]: https://doi.org/10.2514/6.1995-3370
[research_roenneke_well_1996]: https://doi.org/10.2514/6.1996-3698
[research_roepke_1972]: https://doi.org/10.2514/6.1972-1035
[research_roessler_1967]: https://doi.org/10.2514/3.29156
[research_rogers_1953]: https://doi.org/10.21236/ad0013358
[research_rogers_1973]: https://doi.org/10.21236/ad0771616
[research_rogers_dragone_1996]: https://doi.org/10.2514/6.1996-1228
[research_rogers_safie_2004]: https://doi.org/10.1007/978-0-85729-410-4_313
[research_rogers_schroeder_2022]: https://doi.org/10.2514/6.2022-3775
[research_rogers_walterk_1955]: https://doi.org/10.21236/ad0069214
[research_romano_cecchetti_2024]: https://doi.org/10.52202/078372-0079
[research_romanov_burke_2017]: https://doi.org/10.1063/1.4974676
[research_romere_eichblatt_1978]: https://doi.org/10.2514/6.1978-793
[research_romere_eichblatt_1979]: https://doi.org/10.2514/3.58510
[research_romero_bledsoe_2015]: https://doi.org/10.2514/6.2015-2178
[research_rona_soueid_2010]: https://doi.org/10.2514/6.2010-399
[research_rooney_2003]: https://doi.org/10.2514/6.2003-2953
[research_rooney_craig_1977]: https://doi.org/10.2514/6.1977-996
[research_rosenthal_1982]: https://doi.org/10.4271/821341
[research_roshanian_talebi_2008]: https://doi.org/10.1007/s10483-008-1103-z
[research_roshini_subbareddy_2023]: https://doi.org/10.61653/joast.v67i4.2015.407
[research_rosner_peszor_2018]: https://doi.org/10.1063/1.5043764
[research_rossman_braun_2017]: https://doi.org/10.2514/6.2017-0898
[research_rougeux_malomolina_2009]: https://doi.org/10.2514/6.2009-1580
[research_rouwhorst_2001]: https://doi.org/10.1016/s1290-0958(01)90090-5
[research_roux_mantini_2012]: https://doi.org/10.2514/6.2012-4996
[research_roxburgh_2015]: https://doi.org/10.1051/0004-6361/201527447
[research_rubenstein_carter_2000]: https://doi.org/10.2514/2.3556
[research_rudnik_germain_2009]: https://doi.org/10.2514/1.36487
[research_ruf_1996]: https://ntrs.nasa.gov/citations/19960029266
[research_rufolo_destefanofumo_2024]: https://doi.org/10.52202/078373-0036
[research_ruizgarcia_brown_2022]: https://doi.org/10.2514/6.2022-0713
[research_runkle_drobnik_1979]: https://doi.org/10.2514/6.1979-466
[research_ruping_xin_2021]: https://doi.org/10.1007/978-981-15-8155-7_262
[research_ruppe_1985]: https://doi.org/10.1016/0265-9646(85)90034-7
[research_rusbarsky_1990]: https://doi.org/10.2514/6.1990-1269
[research_russo_voto_2026]: https://doi.org/10.2514/6.2026-5140
[research_rutishauser_mendeck_2022]: https://doi.org/10.2514/6.2022-1832
[research_rutishauser_moore_2019]: https://doi.org/10.1109/aero.2019.8741888
[research_s_padhi_2017]: https://doi.org/10.2514/6.2017-1267
[research_sabatini_2014]: https://doi.org/10.1109/metroaerospace.2014.6865886
[research_sabatini_rodriguez_2013]: https://doi.org/10.2478/aon-2013-0008
[research_sabiron_chavent_2013]: https://doi.org/10.1007/978-3-642-38253-6_39
[research_sachan_padhi_2016]: https://doi.org/10.1109/indiancc.2016.7441139
[research_sachs_moeller_1995]: https://doi.org/10.2514/6.1995-3331
[research_sadovnitchii_ryabkov_1997]: https://doi.org/10.2514/6.1997-3792
[research_sadovnychiy_betin_1998]: https://doi.org/10.2514/6.1998-4166
[research_sadovnychiy_betin_1999]: https://doi.org/10.2514/6.1999-4195
[research_sadovnychiy_ryzhenko_2001]: https://doi.org/10.1016/s1474-6670(17)40706-3
[research_sadraey_2011]: https://doi.org/10.2514/6.2011-6627
[research_saff_rosenfeld_1982]: https://doi.org/10.1520/stp28862s
[research_saghafi_esmailifar_2009]: https://doi.org/10.1109/icas.2009.46
[research_sagirov_solovyov_2025]: https://doi.org/10.1109/rusautocon65989.2025.11177452
[research_sahasrabudhe_pritchard_2011]: https://doi.org/10.4050/vfs-f67-000377
[research_sahawneh_aljarrah_2010]: https://doi.org/10.1007/978-94-007-1110-5_31
[research_sahu_2005]: https://doi.org/10.21236/ada438422
[research_saiki_fukao_2009]: https://doi.org/10.3182/20090909-4-jp-2010.00008
[research_sainagabharghava_krishnatmali_2024]: https://doi.org/10.1016/j.ijheatfluidflow.2024.109413
[research_salgueirofilipe_deweerdt_2009]: https://doi.org/10.2514/6.2009-5768
[research_salt_1995]: https://doi.org/10.1117/12.212734
[research_salt_2015]: https://doi.org/10.2514/5.9781624101991.0185.0218
[research_saltzman_1999]: https://ntrs.nasa.gov/citations/19990052613
[research_saltzman_2002]: https://ntrs.nasa.gov/citations/20030003696
[research_saltzman_2007]: https://ntrs.nasa.gov/citations/20070017478
[research_samardzic_isakovic_2013]: https://doi.org/10.1016/j.measurement.2013.04.074
[research_samotokhin_2021]: https://doi.org/10.20948/prepr-2021-5
[research_sanders_1972]: https://doi.org/10.21236/ada036489
[research_sanderson_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50017-8
[research_sani_karimian_2017]: https://doi.org/10.1109/iconda.2017.8270408
[research_sankar_2012]: https://doi.org/10.2514/6.2012-4953
[research_sansica_hashimoto_2023]: https://doi.org/10.2514/6.2023-1989
[research_sanson_villedieu_2017]: https://doi.org/10.1016/j.expthermflusci.2016.11.013
[research_santongzhang_shiwuyang_2008]: https://doi.org/10.1109/indin.2008.4618076
[research_santos_2009]: https://doi.org/10.2514/1.41387
[research_santos_2011]: https://doi.org/10.2514/6.2011-2321
[research_santos_lobo_2019]: https://doi.org/10.23919/oceans40490.2019.8962869
[research_sanuki_1965]: https://doi.org/10.1299/jsmemag.68.552_99
[research_saputra_2017]: https://doi.org/10.25104/wa.v43i2.305.93-104
[research_sarigulklijn_sarigulklijn_2005]: https://doi.org/10.2514/6.2005-621
[research_sarigulklijn_sarigulklijn_2008]: https://doi.org/10.2514/6.2008-7835
[research_saripalli_2009]: https://doi.org/10.2514/6.2009-5660
[research_saripalli_montgomery_2003]: https://doi.org/10.1109/tra.2003.810239
[research_sarkar_amrr_2021]: https://doi.org/10.1109/med51440.2021.9480343
[research_sarrafian_1984]: https://doi.org/10.2514/6.1984-2095
[research_sasa_takizawa_1991]: https://doi.org/10.4271/911980
[research_satkunanathan_murphy_1998]: https://doi.org/10.1007/pl00000023
[research_sato_muraoka_2013]: https://doi.org/10.2514/6.2013-5100
[research_saunders_1996]: https://doi.org/10.2514/6.1996-227
[research_savino_viviani_2009]: https://doi.org/10.2514/6.2009-7307
[research_savkin_antonov_2021]: https://doi.org/10.23919/icins43216.2021.9470426
[research_sawyer_1984]: https://doi.org/10.2514/3.25646
[research_sawyer_bush_1997]: https://doi.org/10.1063/1.51910
[research_sawyer_bush_1998]: https://doi.org/10.1063/1.54711
[research_sawyer_hodge_1999]: https://doi.org/10.1063/1.57501
[research_sayadi_kosari_2018]: https://doi.org/10.1109/access.2018.2810204
[research_scaling_and_2017]: https://doi.org/10.7551/mitpress/11047.003.0028
[research_scanlon_1987]: https://ntrs.nasa.gov/citations/19880003098
[research_scarlatella_guadagnini_2024]: https://doi.org/10.2514/6.2024-2122
[research_schaeffer_1983]: https://doi.org/10.2514/6.1983-2192
[research_schang_2024]: https://doi.org/10.1061/9780784485736.014
[research_schanzer_1993]: https://doi.org/10.1007/978-3-642-45720-3_20
[research_scherberg_1927]: https://ntrs.nasa.gov/citations/19930081026
[research_schermerhorn_1969]: https://doi.org/10.21236/ad0860089
[research_schermerhorn_1969_b]: https://doi.org/10.21236/ad0863422
[research_scherzinger_blakereid_1989]: https://doi.org/10.1007/978-3-642-74585-0_42
[research_schiavazzi_juliano_2020]: https://doi.org/10.2514/6.2020-1652
[research_schiavone_2012]: https://doi.org/10.1088/1748-3182/7/2/025007
[research_schierman_gandhi_2004]: https://doi.org/10.2514/6.2004-4771
[research_schierman_ward_2001]: https://doi.org/10.21236/ada436263
[research_schierman_ward_2001_b]: https://doi.org/10.21236/ada436268
[research_schierman_ward_2004]: https://doi.org/10.2514/1.10344
[research_schifferle_deppe_1999]: https://doi.org/10.2514/6.1999-3963
[research_schmidt_1985]: https://doi.org/10.2514/6.1985-1851
[research_schmidt_2011]: https://doi.org/10.1109/maes.2011.5763346
[research_schmidt_mann_1996]: https://doi.org/10.2514/6.1996-1199
[research_schmitt_burchett_2004]: https://doi.org/10.2514/6.2004-6254
[research_schneider_larson_2012]: https://doi.org/10.2514/6.2012-3164
[research_schneider_searcy_2005]: https://doi.org/10.2514/6.2005-822
[research_scholz_theuser_2026]: https://doi.org/10.1007/s13272-026-00958-y
[research_schonberg_squire_2024]: https://doi.org/10.1016/j.jsse.2023.11.007
[research_schonberg_squire_2024_b]: https://doi.org/10.1115/hvis2024-007
[research_schonberg_squire_2025]: https://doi.org/10.1016/j.actaastro.2025.08.025
[research_schouler_prevereaud_2021]: https://doi.org/10.1080/10618562.2021.2016720
[research_schrader_2023]: https://doi.org/10.1007/978-3-662-63218-5_7
[research_schrauf_schroder_1999]: https://doi.org/10.1007/978-3-663-10901-3_51
[research_schroer_2003]: https://doi.org/10.1109/maes.2003.1226532
[research_schumann_liu_2009]: https://doi.org/10.2514/6.2009-1989
[research_schumann_mbaya_2011]: https://doi.org/10.36001/phmconf.2011.v3i1.2022
[research_schwabacher_2002]: https://ntrs.nasa.gov/citations/20020063487
[research_schwartz_1983]: https://doi.org/10.1002/j.2161-4296.1983.tb00851.x
[research_schwarz_1981]: https://doi.org/10.21236/ada113823
[research_schwelkart_hallion_1997]: https://doi.org/10.21236/ada441126
[research_sciegienny_nurse_1978]: https://doi.org/10.21236/ada062803
[research_scorsoglio_2022]: https://doi.org/10.2514/1.a35072
[research_scorsoglio_gaudet_2025]: https://doi.org/10.1007/s00521-025-11274-7
[research_scoville_rajula_2005]: https://doi.org/10.2514/6.2005-6722
[research_seanor_nd]: https://doi.org/10.33915/etd.2470
[research_sedlmair_theis_2019]: https://doi.org/10.1016/j.ifacol.2019.11.262
[research_sedlmair_theis_2022]: https://doi.org/10.2514/1.g005917
[research_sefic_cutler_1986]: https://doi.org/10.2514/6.1986-9727
[research_seiff_1952]: https://ntrs.nasa.gov/citations/19930086940
[research_seiff_1954]: https://ntrs.nasa.gov/citations/19930090989
[research_seiler_bastide_2012]: https://doi.org/10.1007/978-3-642-25688-2_70
[research_selezneva_neusypin_2022]: https://doi.org/10.23919/icins51784.2022.9815396
[research_sellers_2000]: https://doi.org/10.2514/6.2000-2528
[research_sen_1990]: https://doi.org/10.21236/ada227196
[research_sen_1990_b]: https://doi.org/10.21236/ada227197
[research_senkans_kish_2021]: https://doi.org/10.1109/aero50100.2021.9438277
[research_senpheng_ruchanurucks_2015]: https://doi.org/10.1109/ticst.2015.7369336
[research_sepka_samareh_2015]: https://doi.org/10.2514/6.2015-2507
[research_serrano_2006]: https://doi.org/10.1109/iros.2006.282603
[research_setterfield_hewitt_2021]: https://doi.org/10.1109/aero50100.2021.9438153
[research_setterfield_hewitt_2022]: https://doi.org/10.1109/aero53065.2022.9843356
[research_sevilla_nd]: https://doi.org/10.70675/f805cd5az289fz4a24zba4fzc6083ae4c260
[research_sexton_2003]: https://ntrs.nasa.gov/citations/20040031812
[research_sforza_2003]: https://doi.org/10.21236/ada415973
[research_sforza_2014]: https://doi.org/10.1016/b978-0-12-419953-8.00007-3
[research_sforza_2016]: https://doi.org/10.1016/b978-0-12-804425-4.00009-x
[research_sforza_2020]: https://doi.org/10.2514/6.2020-0281
[research_sha_li_2026]: https://doi.org/10.1109/ccdc69976.2026.11559926
[research_shafa_cunio_2011]: https://doi.org/10.2514/6.2011-7188
[research_shah_gevaert_1972]: https://doi.org/10.2514/6.1972-811
[research_shahrbabaki_bazazzadeh_2014]: https://doi.org/10.1109/aero.2014.6836242
[research_shahzad_weiduo_2019]: https://doi.org/10.1109/ibcast.2019.8667154
[research_shaiju_sreeja_2022]: https://doi.org/10.1016/j.ifacol.2023.03.035
[research_shakarian_1983]: https://doi.org/10.2514/6.1983-2193
[research_shakernia_ma_1999]: https://doi.org/10.1111/j.1934-6093.1999.tb00014.x
[research_shakoori_betin_2017]: https://doi.org/10.14716/ijtech.v8i3.2058
[research_shakoori_mortazavi_2012]: https://doi.org/10.4028/www.scientific.net/amm.225.323
[research_shalaby_2018]: https://doi.org/10.1201/9781315156637-11
[research_shamaghdari_nikravesh_2014]: https://doi.org/10.1002/rnc.3215
[research_shameed_gr_2021]: https://doi.org/10.1016/j.ast.2021.106777
[research_shan_huifeng_2015]: https://doi.org/10.1109/chicc.2015.7260273
[research_shang_li_2022]: https://doi.org/10.1007/978-3-031-20500-2_15
[research_shao_deyang_2016]: https://doi.org/10.2514/6.2016-3428
[research_shao_gu_2018]: https://doi.org/10.1017/s0373463318000358
[research_shao_wang_2015]: https://doi.org/10.1016/j.isatra.2014.06.010
[research_shao_wang_2015_b]: https://doi.org/10.1016/j.ast.2015.09.003
[research_shao_wang_2016]: https://doi.org/10.1016/j.jfranklin.2016.03.007
[research_shao_wu_2017]: https://doi.org/10.1016/j.solmat.2017.08.006
[research_shao_yang_2020]: https://doi.org/10.1109/access.2020.3035894
[research_shao_zhao_2025]: https://doi.org/10.1007/978-981-96-2232-0_36
[research_sharf_monterrubio_1999]: https://doi.org/10.2514/6.1999-4327
[research_sharma_giangaspero_2024]: https://doi.org/10.1063/5.0191101
[research_sharma_gogu_2008]: https://doi.org/10.2514/6.2008-2062
[research_sharma_hablani_2014]: https://doi.org/10.3182/20140313-3-in-3024.00224
[research_sharma_vidal_2011]: https://doi.org/10.2514/6.2011-7165
[research_shaw_richter_1985]: https://doi.org/10.2514/6.1985-338
[research_shaw_taylor_1997]: https://doi.org/10.1016/s0265-9646(97)00007-6
[research_shawyer_2023]: https://doi.org/10.1201/9781003456759-14
[research_shea_chan_2023]: https://doi.org/10.2514/6.2023-0426
[research_sheard_scaysbrook_2008]: https://doi.org/10.1109/plans.2008.4570001
[research_sheldon_1967]: https://doi.org/10.21236/ad0856658
[research_shen_2021]: https://doi.org/10.1007/978-981-33-4516-4_5
[research_shen_2021_b]: https://doi.org/10.1007/978-981-33-4516-4_6
[research_shen_chen_2025]: https://doi.org/10.3390/drones9090624
[research_shen_li_2019]: https://doi.org/10.1109/sdpc.2019.00169
[research_shen_sheng_2016]: https://doi.org/10.1109/cgncc.2016.7828761
[research_shen_xia_2023]: https://doi.org/10.1016/j.isatra.2022.06.023
[research_shen_zhang_2025]: https://doi.org/10.1007/978-981-96-2268-9_38
[research_sheng_geng_2015]: https://doi.org/10.1007/s12555-013-0181-y
[research_sheng_mian_2010]: https://doi.org/10.1016/j.conengprac.2010.05.009
[research_shengzechen_xuanzhang_2014]: https://doi.org/10.1109/wcica.2014.7052787
[research_shenming_tao_2017]: https://doi.org/10.1109/ascc.2017.8287226
[research_shenming_tao_2018]: https://doi.org/10.1109/gncc42960.2018.9019097
[research_shepheard_1965]: https://doi.org/10.21236/ad0630924
[research_shepperd_lentsch_2000]: https://doi.org/10.1007/978-94-010-0894-5_41
[research_shepperd_staugler_1999]: https://doi.org/10.2514/6.1999-4209
[research_sherman_1978]: https://doi.org/10.21236/ada056390
[research_sherry_shortle_2018]: https://doi.org/10.2514/6.2018-3983
[research_shi_li_2025]: https://doi.org/10.1007/978-981-96-2264-1_43
[research_shi_li_2025_b]: https://doi.org/10.1016/j.actaastro.2025.04.040
[research_shi_li_2026]: https://doi.org/10.1016/j.matdes.2026.115562
[research_shi_tang_2009]: https://doi.org/10.1109/ihmsc.2009.181
[research_shi_tanigawa_2016]: https://doi.org/10.1299/jamdsm.2016jamdsm0005
[research_shideler_webb_1985]: https://doi.org/10.2514/3.25070
[research_shields_1981]: https://doi.org/10.2514/6.1981-2351
[research_shields_mohseni_2011]: https://doi.org/10.2514/6.2011-873
[research_shiji_kulik_2026]: https://doi.org/10.1007/978-3-032-02717-7_13
[research_shilinan_lihuifeng_2014]: https://doi.org/10.1109/wcica.2014.7052790
[research_shim_park_2023]: https://doi.org/10.2514/6.2023-3623
[research_shimada_ohwada_2020]: https://doi.org/10.1186/s42774-020-00037-8
[research_shimizu_murata_2008]: https://doi.org/10.9746/jcmsi.1.362
[research_shin_kim_2013]: https://doi.org/10.12985/ksaa.2013.21.3.041
[research_shinbrot_2019]: https://doi.org/10.1093/oso/9780198812586.003.0007
[research_shinnick_1966]: https://doi.org/10.2514/6.1966-358
[research_shou_xu_2021]: https://doi.org/10.1016/j.ast.2021.106564
[research_shrotri_schrage_2009]: https://doi.org/10.4050/jahs.54.042005
[research_shrotri_schrage_2009_b]: https://doi.org/10.4050/jahs.54.042004
[research_shtessel_hall_2000]: https://doi.org/10.2514/2.4669
[research_shtessel_tournes_1997]: https://doi.org/10.2514/6.1997-3533
[research_shtessel_zhu_2002]: https://doi.org/10.2514/6.2002-4779
[research_shuai_daqian_2022]: https://doi.org/10.1109/docs55193.2022.9967480
[research_shuang_2008]: https://doi.org/10.1016/j.actaastro.2007.11.009
[research_shuang_hutao_2005]: https://doi.org/10.1108/00022660510606402
[research_shuang_liu_2009]: https://doi.org/10.1108/00022660910997810
[research_shuang_pingyuan_2006]: https://doi.org/10.2514/6.iac-06-a3.6.07
[research_shue_agarwal_1999]: https://doi.org/10.2514/2.4356
[research_shufeldt_1961]: https://doi.org/10.21236/ad0259559
[research_shuhuazhu_mingbotong_2008]: https://doi.org/10.1109/asc-icsc.2008.4675338
[research_shukla_2024]: https://doi.org/10.55041/isjem01527
[research_shulga_shcheglov_2021]: https://doi.org/10.18698/2308-6033-2021-9-2109
[research_shupingtan_zhibinli_2010]: https://doi.org/10.1109/ccdc.2010.5498526
[research_shuttle_autoland_1976]: https://ntrs.nasa.gov/citations/19760015180
[research_shweyk_hyde_2012]: https://doi.org/10.2514/6.2012-4579
[research_si_zhao_2024]: https://doi.org/10.25103/jestr.171.21
[research_siboro_zainul_2023]: https://doi.org/10.36277/identifikasi.v9i1.258
[research_sickle_2023]: https://doi.org/10.1201/9781003405238-8
[research_sillen_1993]: https://doi.org/10.2514/6.1993-5025
[research_silsby_1953]: https://ntrs.nasa.gov/citations/19930087581
[research_silsby_1955]: https://ntrs.nasa.gov/citations/19930088709
[research_silsby_1956]: https://ntrs.nasa.gov/citations/19930089352
[research_silva_augustoaparecidogomes_2021]: https://doi.org/10.26678/abcm.cobem2021.cob2021-1008
[research_silva_fontes_2019]: https://doi.org/10.1109/iscc47284.2019.8969571
[research_silva_gamarra_2009]: https://doi.org/10.5028/jatm.2009.01016977
[research_silva_mendonca_2014]: https://doi.org/10.1109/robio.2014.7090550
[research_silvestre_2013]: https://doi.org/10.1007/978-3-642-38253-6_37
[research_sim_1973]: https://ntrs.nasa.gov/citations/19740004421
[research_sim_1973_b]: https://ntrs.nasa.gov/citations/19740003701
[research_sim_murray_1994]: https://doi.org/10.2514/3.46617
[research_simeonides_2006]: https://doi.org/10.1007/s00193-006-0040-3
[research_similitude_and_1967]: https://doi.org/10.3138/9781487579890-102
[research_similitude_relationships_1992]: https://doi.org/10.1201/9781482286700-0
[research_simmons_ackerman_2025]: https://doi.org/10.4050/f-0081-2025-0161
[research_simmons_ackerman_2026]: https://doi.org/10.2514/6.2026-2088
[research_simmons_nd]: https://ntrs.nasa.gov/citations/20250003661
[research_simons_1975]: https://doi.org/10.21236/ada019517
[research_simons_1976]: https://doi.org/10.2514/3.7252
[research_simplicio_marcos_2020]: https://doi.org/10.2514/1.a34429
[research_simplicio_navarrotapia_2018]: https://doi.org/10.1016/j.ifacol.2018.11.095
[research_simpson_1972]: https://doi.org/10.2514/6.1972-785
[research_sims_carter_1981]: https://doi.org/10.2514/6.1981-2387
[research_sims_hahn_1964]: https://doi.org/10.21236/ad0603567
[research_simulation_support_1988]: https://doi.org/10.2514/6.1988-2130
[research_singh_2023]: https://doi.org/10.2514/6.2023-3006
[research_singh_chaudhary_2021]: https://doi.org/10.1007/978-981-16-0673-1_12
[research_singh_menghal_2022]: https://doi.org/10.1109/i2ct54291.2022.9824660
[research_singh_tiwari_1989]: https://doi.org/10.2514/6.1989-2184
[research_singleton_1998]: https://ntrs.nasa.gov/citations/20040090509
[research_sipe_hinde_2008]: https://doi.org/10.2514/6.2008-7801
[research_sippel_pohl_1996]: https://doi.org/10.2514/6.1996-4496
[research_sippel_sippel_1997]: https://doi.org/10.2514/6.1997-2646
[research_sithara_shenil_2022]: https://doi.org/10.1109/icccis56430.2022.10037641
[research_sivakumar_syedhaleem_2018]: https://doi.org/10.21595/mme.2018.19895
[research_sivalingam_hagen_2026]: https://doi.org/10.3390/engproc2026126003
[research_sivan_murmu_2017]: https://doi.org/10.1007/s40032-017-0426-2
[research_sivan_pandian_2018]: https://doi.org/10.18520/cs/v114/i01/38-47
[research_sivells_1969]: https://doi.org/10.2514/6.1969-337
[research_sivolella_2014]: https://doi.org/10.1007/978-1-4614-0983-0_8
[research_siwen_feng_2022]: https://doi.org/10.1109/itoec53115.2022.9734711
[research_skariya_sebastian_2014]: https://doi.org/10.3182/20140313-3-in-3024.00064
[research_skolnik_putnam_2020]: https://doi.org/10.2514/6.2020-0401
[research_slater_1956]: https://doi.org/10.21236/ada284483
[research_slayton_1977]: https://ntrs.nasa.gov/citations/19770052454
[research_slegers_beyer_2007]: https://doi.org/10.2514/6.2007-2526
[research_slender_lifting_1994]: https://doi.org/10.2514/5.9781600866326.0261.0275
[research_slivinsky_breitling_1995]: https://doi.org/10.2514/6.1995-3539
[research_smitchens_huber_1975]: https://doi.org/10.4271/751113
[research_smith_1965]: https://ntrs.nasa.gov/citations/19650024238
[research_smith_1974]: https://ntrs.nasa.gov/citations/19740023344
[research_smith_1981]: https://ntrs.nasa.gov/citations/19820005276
[research_smith_1996]: https://ntrs.nasa.gov/citations/20210003754
[research_smith_1996_b]: https://ntrs.nasa.gov/citations/19960038443
[research_smith_2003]: https://doi.org/10.2514/6.2003-6946
[research_smith_2011]: https://doi.org/10.2514/6.2011-6330
[research_smith_2017]: https://ntrs.nasa.gov/citations/20170009820
[research_smith_2018]: https://ntrs.nasa.gov/citations/20180007064
[research_smith_amitay_1998]: https://doi.org/10.2514/6.1998-209
[research_smith_meyer_1981]: https://doi.org/10.2514/6.1981-2238
[research_smith_nd]: https://doi.org/10.5204/thesis.eprints.246280
[research_smith_purvis_1994]: https://doi.org/10.1177/154193129403801503
[research_smithjr_biezad_1986]: https://doi.org/10.2514/6.1986-9817
[research_smotrova_2002]: https://doi.org/10.1177/0307174x0202901205
[research_snapp_rodriguez_2011]: https://doi.org/10.2514/6.2011-7308
[research_snyder_schipper_1992]: https://doi.org/10.1109/62.257086
[research_sobron_lundstrom_2021]: https://doi.org/10.3390/aerospace8030074
[research_soencksen_whyte_1999]: https://doi.org/10.2514/6.1999-4259
[research_sohier_farges_2014]: https://doi.org/10.3182/20140824-6-za-1003.01968
[research_sohier_farges_2014_b]: https://doi.org/10.1109/aero.2014.6836444
[research_sohier_pietlahanier_2015]: https://doi.org/10.1016/j.actaastro.2014.11.043
[research_soistmann_1993]: https://ntrs.nasa.gov/citations/19930049894
[research_sokolov_sukhanov_2022]: https://doi.org/10.1109/rusautocon54946.2022.9896308
[research_solntsev_2014]: https://doi.org/10.18577/2307-6046-2014-0-2-1-1
[research_soloviev_yang_2016]: https://doi.org/10.33012/2016.13464
[research_sommer_1960]: https://ntrs.nasa.gov/citations/19660024048
[research_son_oh_2023]: https://doi.org/10.5302/j.icros.2023.23.0010
[research_song_ai_2020]: https://doi.org/10.1016/j.ast.2020.106001
[research_song_cai_2013]: https://doi.org/10.4028/www.scientific.net/amm.448-453.3508
[research_song_liao_2005]: https://doi.org/10.1007/11427469_30
[research_song_liu_2020]: https://doi.org/10.1145/3440084.3441205
[research_song_shi_2026]: https://doi.org/10.1007/978-981-95-7342-4_35
[research_song_wang_2023]: https://doi.org/10.1007/978-981-99-0613-0_2
[research_song_wang_2023_b]: https://doi.org/10.1109/isas59543.2023.10164624
[research_song_wang_2025]: https://doi.org/10.1007/978-3-032-09862-7_2
[research_song_zhang_2019]: https://doi.org/10.1109/dasc43569.2019.9081785
[research_song_zhang_2023]: https://doi.org/10.23919/ccc58697.2023.10239989
[research_song_zhang_2024]: https://doi.org/10.1016/j.ast.2024.109261
[research_songhui_chufeng_2020]: https://doi.org/10.1109/cac51589.2020.9326754
[research_sonowal_pandey_2021]: https://doi.org/10.1016/j.matpr.2020.11.1032
[research_sorensen_1977]: https://ntrs.nasa.gov/citations/19770059946
[research_sostaric_cerimele_2017]: https://doi.org/10.2514/6.2017-1898
[research_sotirios_2008]: https://ntrs.nasa.gov/citations/20080017095
[research_space_shuttle_1977]: https://ntrs.nasa.gov/citations/19770010192
[research_spaceplane_coordinates_2016]: https://doi.org/10.1016/b978-0-12-804425-4.00024-6
[research_spaceplane_history_2002]: https://doi.org/10.1142/9781860949371_0002
[research_spaceplane_low_cost_2002]: https://doi.org/10.1142/9781860949371_0005
[research_spahr_1974]: https://doi.org/10.2514/6.1974-776
[research_spearman_1984]: https://doi.org/10.2514/6.1984-2146
[research_spearman_1985]: https://doi.org/10.2514/6.1985-497
[research_spearman_1994]: https://ntrs.nasa.gov/citations/19940022190
[research_spencer_1973]: https://ntrs.nasa.gov/citations/19730007258
[research_spidaliere_zipay_2004]: https://doi.org/10.2514/6.2004-6084
[research_sponable_morse_2004]: https://doi.org/10.2514/6.2004-4184
[research_spravka_jorris_2015]: https://doi.org/10.2514/6.2015-3224
[research_spravka_jorris_2015_b]: https://doi.org/10.21236/ada619521
[research_spreiter_steffen_1946]: https://doi.org/10.4271/460118
[research_springer_1996]: https://doi.org/10.2514/6.1996-196
[research_spurlin_lueck_1984]: https://doi.org/10.2514/6.1984-612
[research_squires_2004]: https://doi.org/10.21236/ada427305
[research_sreeletha_noble_2019]: https://doi.org/10.1063/1.5120188
[research_sruthis_sumathyr_2015]: https://doi.org/10.1109/iccc.2015.7432877
[research_staas_philipc_1963]: https://doi.org/10.21236/ad0406113
[research_stachiw_khouli_2020]: https://doi.org/10.2514/6.2020-1681
[research_stadler_1993]: https://doi.org/10.2514/6.1993-5102
[research_stadler_1998]: https://doi.org/10.2514/6.1998-1504
[research_stalnov_angland_2013]: https://doi.org/10.2514/6.2013-3153
[research_staniszewski_1999]: https://doi.org/10.2514/6.1999-4826
[research_stapleton_galati_1997]: https://doi.org/10.21236/ada397882
[research_starkey_argrow_2012]: https://doi.org/10.2514/6.2012-1048
[research_starkey_lewis_2000]: https://doi.org/10.2514/2.3618
[research_starkey_sequeira_2026]: https://doi.org/10.3390/engproc2025088079
[research_starr_1962]: https://doi.org/10.21236/ad0333228
[research_statistical_filtering_1964]: https://doi.org/10.2514/5.9781600864872.0775.0801
[research_staylor_1970]: https://ntrs.nasa.gov/citations/19700043608
[research_steer_2004]: https://doi.org/10.1017/s000192400000018x
[research_stein_2005]: https://ntrs.nasa.gov/citations/20060056201
[research_steinberg_1992]: https://doi.org/10.2514/6.1992-4392
[research_steiner_brady_2014]: https://doi.org/10.1109/aero.2014.6836216
[research_steinfeldt_grant_2008]: https://doi.org/10.2514/6.2008-6216
[research_stellar_techniques_1964]: https://doi.org/10.2514/5.9781600864872.0495.0550
[research_stephan_2025]: https://doi.org/10.1007/978-3-031-78487-3_6
[research_stephens_1959]: https://ntrs.nasa.gov/citations/19980232232
[research_stern_2004]: https://doi.org/10.21236/ada428861
[research_stern_2008]: https://doi.org/10.21236/ada491628
[research_stern_chu_1963]: https://doi.org/10.21236/ad0405109
[research_stetson_lewis_1977]: https://doi.org/10.2514/6.1977-1161
[research_stevens_1966]: https://ntrs.nasa.gov/citations/19670003792
[research_stevens_1985]: https://ntrs.nasa.gov/citations/19860063046
[research_stewart_leiser_1986]: https://doi.org/10.2514/3.25823
[research_stich_2012]: https://doi.org/10.1007/978-3-642-22627-4_21
[research_stickle_1960]: https://ntrs.nasa.gov/citations/20040020119
[research_stickle_1961]: https://ntrs.nasa.gov/citations/19980227994
[research_stiles_2022]: https://doi.org/10.2514/5.9781624106255.0275.0310
[research_stilley_1988]: https://doi.org/10.2514/6.1988-4350
[research_stolle_bolting_2015]: https://doi.org/10.1109/icuas.2015.7152281
[research_stollery_murthy_1978]: https://doi.org/10.2514/6.1978-766
[research_stottier_1995]: https://doi.org/10.21236/ada293962
[research_stout_1946]: https://doi.org/10.2514/8.11387
[research_stout_1971]: https://doi.org/10.2514/6.1971-788
[research_stower_2024]: https://doi.org/10.52202/078377-0011
[research_straub_1987]: https://ntrs.nasa.gov/citations/19870014163
[research_straub_johnston_1984]: https://doi.org/10.2514/6.1984-2532
[research_strauss_1967]: https://doi.org/10.2514/3.29076
[research_strebjr_1972]: https://doi.org/10.2514/6.1972-227
[research_strelets_tarasov_2023]: https://doi.org/10.18287/2541-7533-2023-22-3-89-98
[research_strouhal_curry_1966]: https://doi.org/10.2514/6.1966-1718
[research_structural_design_1972]: https://doi.org/10.2514/6.1972-372
[research_strutz_1972]: https://ntrs.nasa.gov/citations/19720023253
[research_study_influence_1967]: https://ntrs.nasa.gov/citations/19670020695
[research_study_of_2022]: https://doi.org/10.36652/0869-4931-2022-76-4-179-184
[research_stuessy_peeples_1997]: https://doi.org/10.2514/6.1997-663
[research_stumper_kraus_2015]: https://doi.org/10.14311/mad.2015.16.01
[research_stuper_1934]: https://ntrs.nasa.gov/citations/19930094666
[research_su_dai_2021]: https://doi.org/10.1016/j.ast.2021.107200
[research_su_dai_2021_b]: https://doi.org/10.1007/s00500-021-06039-y
[research_su_hong_2025]: https://doi.org/10.1080/23307706.2025.2556335
[research_su_kiang_2022]: https://doi.org/10.3390/rs14236092
[research_su_liu_2025]: https://doi.org/10.1016/j.ast.2024.109839
[research_su_liu_2025_b]: https://doi.org/10.1016/j.asoc.2024.112637
[research_su_wang_2015]: https://doi.org/10.1016/j.neucom.2015.03.063
[research_su_yu_2013]: https://doi.org/10.5139/ijass.2013.14.3.247
[research_subrahmanyam_1994]: https://doi.org/10.2514/3.21177
[research_subrahmanyam_1995]: https://doi.org/10.1007/978-1-4612-4272-7_6
[research_subrata_2017]: https://doi.org/10.26555/jiteki.v2i2.4896
[research_suit_1964]: https://doi.org/10.2514/6.1964-1304
[research_sukenik_2004]: https://doi.org/10.21236/ada421641
[research_sun_2026]: https://doi.org/10.1088/1742-6596/3207/1/012035
[research_sun_chang_2026]: https://doi.org/10.1016/j.ast.2026.112576
[research_sun_chen_2022]: https://doi.org/10.3390/rs14235932
[research_sun_huang_2025]: https://doi.org/10.1109/ccdc65474.2025.11090502
[research_sun_jia_2024]: https://doi.org/10.1007/978-981-97-3328-6_29
[research_sun_jing_2024]: https://doi.org/10.2514/1.g008075
[research_sun_qiu_2024]: https://doi.org/10.3390/en18010087
[research_sun_shi_2020]: https://doi.org/10.1016/j.ast.2020.106126
[research_sun_tang_2011]: https://doi.org/10.1109/icma.2011.5986361
[research_sun_wu_2023]: https://doi.org/10.1155/2023/9395447
[research_sun_xu_2025]: https://doi.org/10.1088/1742-6596/3026/1/012036
[research_sun_yang_2015]: https://doi.org/10.1360/n092014-00463
[research_sun_zhao_2024]: https://doi.org/10.1109/access.2024.3506597
[research_sun_zhu_2023]: https://doi.org/10.3390/aerospace10030310
[research_sunasawa_ohta_1997]: https://doi.org/10.2322/jjsass1969.45.52
[research_sunday_nd]: https://doi.org/10.70675/ce60d5a4za0bez468ez8ffbzbebc1b7093ce
[research_sunken_reentry_2013]: https://doi.org/10.2514/5.9781624102042.0231.0242
[research_suppes_2026]: https://doi.org/10.33774/coe-2026-7rzmb
[research_surzhikov_2015]: https://doi.org/10.2514/6.2015-1701
[research_surzhikov_2018]: https://doi.org/10.1134/s1028335818100038
[research_surzhikov_2018_b]: https://doi.org/10.31857/s086956520003101-4
[research_sushnigdha_2021]: https://doi.org/10.1007/978-981-16-2709-5_17
[research_suszynski_kowalski_2025]: https://doi.org/10.1108/aeat-01-2025-0003
[research_suzuki_2013]: https://doi.org/10.1007/978-4-431-54276-6_5
[research_suzuki_fujita_2014]: https://doi.org/10.2514/1.a32549
[research_suzuki_min_2016]: https://doi.org/10.1088/1742-6596/744/1/012219
[research_svyatushenko_yagodnikov_2021]: https://doi.org/10.1063/5.0035924
[research_swamy_zebenay_2021]: https://doi.org/10.17509/ajse.v1i3.37738
[research_swann_1960]: https://doi.org/10.1016/b978-1-4832-2885-3.50008-8
[research_swanson_1958]: https://ntrs.nasa.gov/citations/19630010650
[research_swanson_miller_2025]: https://doi.org/10.2514/1.a36287
[research_swathy_geetha_2018]: https://doi.org/10.1109/cetic4.2018.8530899
[research_szalai_chen_2005]: https://doi.org/10.2514/1.3637
[research_szmuk_eren_2017]: https://doi.org/10.2514/6.2017-1500
[research_szymanski_2025]: https://doi.org/10.2514/6.2025-2228
[research_tabatabaei_orlu_2021]: https://doi.org/10.3390/fluids6080265
[research_tablole_banavar_1998]: https://doi.org/10.14429/dsj.48.4043
[research_tadema_theunissen_2007]: https://doi.org/10.1109/dasc.2007.4391934
[research_tadema_theunissen_2008]: https://doi.org/10.1117/12.781845
[research_taghizadeh_nezhadshahbodaghi_2022]: https://doi.org/10.1007/s10291-022-01265-9
[research_taguchi_futamura_2001]: https://doi.org/10.2514/6.2001-1838
[research_taguchi_maita_1999]: https://doi.org/10.2514/6.1999-4811
[research_tahsini_mousavi_2014]: https://doi.org/10.4028/www.scientific.net/amm.598.298
[research_taihua_xianhong_2011]: https://doi.org/10.5772/13604
[research_takahashi_1993]: https://doi.org/10.2514/6.1993-3849
[research_takahashi_camberos_2024]: https://doi.org/10.2514/6.2024-3911
[research_takahashi_goerzen_2018]: https://doi.org/10.4050/jahs.63.042001
[research_takahashi_ha_2014]: https://doi.org/10.2514/6.2014-3283
[research_takahashi_mizobata_1997]: https://doi.org/10.2514/2.3280
[research_takahashi_nakasato_2016]: https://doi.org/10.3390/aerospace3010002
[research_takahashi_yamada_2013]: https://doi.org/10.2514/6.2013-1303
[research_takahashi_yamada_2015]: https://doi.org/10.2514/1.a33170
[research_takahashi_yamada_2018]: https://doi.org/10.1016/j.actaastro.2018.08.003
[research_talay_1991]: https://ntrs.nasa.gov/citations/19920029948
[research_tamer_2021]: https://doi.org/10.3390/machines9030061
[research_tan_nd]: https://doi.org/10.32657/10356/66721
[research_tan_yang_2025]: https://doi.org/10.1109/icccr65461.2025.11072631
[research_tanck_steadman_1998]: https://doi.org/10.1063/1.54716
[research_tancredi_accardo_2007]: https://doi.org/10.1016/j.actaastro.2006.06.003
[research_tancredi_grassi_2007]: https://doi.org/10.2514/1.22007
[research_tang_1970]: https://ntrs.nasa.gov/citations/19710000632
[research_tang_1971]: https://ntrs.nasa.gov/citations/19710029224
[research_tang_1971_b]: https://ntrs.nasa.gov/citations/19710015105
[research_tang_1973]: https://ntrs.nasa.gov/citations/19730016322
[research_tang_chen_2014]: https://doi.org/10.1109/cgncc.2014.7007529
[research_tang_long_2018]: https://doi.org/10.3103/s0146411618030100
[research_tang_zhai_2020]: https://doi.org/10.1016/j.ins.2019.08.012
[research_tangthong_aktimagool_2021]: https://doi.org/10.1109/ieecon51072.2021.9440230
[research_taniguchi_2000]: https://doi.org/10.1299/jsmemag.103.983_674
[research_tanno_komuro_2017]: https://doi.org/10.2514/6.2017-0772
[research_taoguo_daweiliu_2010]: https://doi.org/10.1109/icacte.2010.5578951
[research_tariq_wasim_2026]: https://doi.org/10.3390/pr14152458
[research_tartabini_2000]: https://ntrs.nasa.gov/citations/20000031364
[research_tate_1974]: https://ntrs.nasa.gov/citations/19760018248
[research_tate_1975]: https://ntrs.nasa.gov/citations/19760026273
[research_tatry_deneu_1997]: https://doi.org/10.1016/s0094-5765(97)00194-x
[research_tava_suzuki_2002]: https://doi.org/10.2322/tjsass.45.10
[research_taylor_1958]: https://doi.org/10.21236/ad0428384
[research_taylor_1983]: https://doi.org/10.2514/6.1983-2086
[research_taylor_2004]: https://ntrs.nasa.gov/citations/20040037790
[research_tazartes_mark_1988]: https://doi.org/10.1002/j.2161-4296.1988.tb00943.x
[research_technology_demonstrator_2023]: https://doi.org/10.2514/5.9781624106965.0259.0354
[research_teixeira_pascoa_2026]: https://doi.org/10.1061/jaeeez.aseng-6229
[research_tekinalp_kumbasar_2015]: https://doi.org/10.2514/6.2015-0601
[research_temple_2006]: https://doi.org/10.2514/6.iac-06-e4.3.01
[research_teng_chen_2021]: https://doi.org/10.1007/978-981-15-8155-7_295
[research_teng_han_2025]: https://doi.org/10.34133/space.0240
[research_tenhave_joiner_2026]: https://doi.org/10.3390/aerospace13010059
[research_tennstedt_rajagopalan_2023]: https://doi.org/10.33012/navi.604
[research_tennstedt_schon_2021]: https://doi.org/10.23919/icins43216.2021.9470809
[research_tennstedt_schon_2025]: https://doi.org/10.1109/inertial63280.2025.11037122
[research_teper_1981]: https://ntrs.nasa.gov/citations/19810018575
[research_terheyden_zickwolff_1986]: https://doi.org/10.1007/978-3-662-21924-9_4
[research_terminal_guidance_1962]: https://doi.org/10.2514/5.9781600864827.0217.0239
[research_tetlow_schoettle_2000]: https://doi.org/10.2514/6.2000-4180
[research_tewell_1984]: https://doi.org/10.2514/6.1984-781
[research_the_advance_1971]: https://doi.org/10.1108/eb034732
[research_the_algorithm_2020]: https://doi.org/10.36652/0869-4931-2020-74-2-78-84
[research_the_development_2004]: https://doi.org/10.2514/6.iac-04-i.6.02
[research_the_effect_1981]: https://doi.org/10.2514/5.9781600865510.0083.0108
[research_the_effect_1982]: https://doi.org/10.1016/0003-6870(82)90047-3
[research_the_graphic_2011]: https://doi.org/10.1049/et.2011.0620
[research_the_inertial_2007]: https://doi.org/10.1142/9789812708755_0006
[research_the_king_1962]: https://doi.org/10.2514/5.9781600864827.0397.0410
[research_the_spaceplane_2002]: https://doi.org/10.1142/9781860949371_0007
[research_the_traditional_2017]: https://doi.org/10.1002/9781119049272.ch1
[research_thermal_design_of_2018]: https://doi.org/10.18698/2308-6033-2017-12-1712
[research_thermal_performance_1972]: https://doi.org/10.2514/6.1972-388
[research_thermal_protection_1981]: https://doi.org/10.2514/5.9781600865510.0309.0334
[research_thermal_protection_2013]: https://doi.org/10.2514/5.9781624101717.0001.0030
[research_theunissen_1994]: https://doi.org/10.1016/0141-9382(94)90072-8
[research_thibodeaux_1977]: https://ntrs.nasa.gov/citations/19770020186
[research_thies_2022]: https://doi.org/10.1007/s12567-022-00456-x
[research_tho_wang_2009]: https://doi.org/10.4050/jahs.54.042003
[research_thomas_1998]: https://doi.org/10.2514/6.1998-3959
[research_thomas_2025]: https://doi.org/10.1007/s11668-025-02339-9
[research_thomas_perlbachs_1967]: https://doi.org/10.21236/ad0655383
[research_thompson_1964]: https://ntrs.nasa.gov/citations/19640012526
[research_thompson_1965]: https://doi.org/10.2514/6.1965-1209
[research_thompson_1966]: https://ntrs.nasa.gov/citations/19670035398
[research_thompson_1970]: https://ntrs.nasa.gov/citations/19710034122
[research_thompson_1970_b]: https://ntrs.nasa.gov/citations/19710008953
[research_thompson_1981]: https://ntrs.nasa.gov/citations/19820031406
[research_thompson_2024]: https://doi.org/10.1063/10.0024316
[research_thornton_1994]: https://doi.org/10.2514/6.1994-2163
[research_thornton_lamy_1992]: https://doi.org/10.2514/6.1992-4070
[research_threadgill_hader_2024]: https://doi.org/10.2514/6.2024-0498
[research_three_dimensional_location_2008]: https://doi.org/10.5302/j.icros.2008.14.6.608
[research_throckmorton_1981]: https://ntrs.nasa.gov/citations/19820030332
[research_throckmorton_1989]: https://doi.org/10.2514/6.1989-5009
[research_tian_1980]: https://doi.org/10.2514/6.1980-1534
[research_tian_dong_2025]: https://doi.org/10.1016/j.cej.2025.169346
[research_tian_fan_2015]: https://doi.org/10.1007/s11071-014-1877-0
[research_tian_luo_2025]: https://doi.org/10.1016/j.compositesa.2025.109107
[research_tian_sun_2014]: https://doi.org/10.1007/978-3-642-54233-6_61
[research_tian_yu_2018]: https://doi.org/10.1017/s0373463318000966
[research_tian_yu_2022]: https://doi.org/10.1109/robio55434.2022.10011723
[research_tian_yu_2024]: https://doi.org/10.1109/lra.2024.3380925
[research_tian_zong_2013]: https://doi.org/10.1016/j.ast.2012.10.015
[research_tie_cao_2018]: https://doi.org/10.3390/s18030906
[research_tieshan_zhiyao_2021]: https://doi.org/10.1109/ccdc52312.2021.9601884
[research_tile_gap_flow_1983]: https://doi.org/10.2514/5.9781600865626.0271.0299
[research_tire_overspeed_nd]: https://doi.org/10.4271/arp5257a
[research_tire_runway_braking_1958]: https://doi.org/10.1016/0043-1648(58)90128-5
[research_tirtey_paris_2005]: https://doi.org/10.2514/6.2005-3280
[research_tischler_2018]: https://doi.org/10.1201/9781315136820-2
[research_titan_ii_2002]: https://doi.org/10.2307/j.ctvvng4n.15
[research_titov_parnenkov_2025]: https://doi.org/10.26467/2079-0619-2025-28-4-67-83
[research_titov_serebryanskiy_2023]: https://doi.org/10.18698/2308-6033-2023-6-2283
[research_titov_serebryansky_2023]: https://doi.org/10.1051/e3sconf/202344603006
[research_titov_serebryansky_2023_b]: https://doi.org/10.1109/mlsd58227.2023.10303898
[research_titov_serebryansky_2026]: https://doi.org/10.1007/s42401-026-00486-x
[research_tkhorenko_karshakov_2023]: https://doi.org/10.23919/icins51816.2023.10168334
[research_tobin_dec_2015]: https://doi.org/10.2514/6.2015-1895
[research_toda_koike_2021]: https://doi.org/10.1109/inertial51137.2021.9430487
[research_tokluoglu_cavus_2019]: https://doi.org/10.1109/gpecom.2019.8778612
[research_tokugawa_ishida_2025]: https://doi.org/10.2514/6.2025-3289
[research_tomac_rizzi_2016]: https://doi.org/10.2514/6.2016-0803
[research_tomita_2022]: https://doi.org/10.2514/1.a35104
[research_tomita_2025]: https://doi.org/10.2514/1.a36253
[research_tomita_fujiwara_2021]: https://doi.org/10.1299/transjsme.20-00440
[research_tomita_ho_2025]: https://doi.org/10.2514/6.2025-1898
[research_tong_1991]: https://doi.org/10.2514/6.1991-865
[research_tooley_wyatt_2024]: https://doi.org/10.1201/9781003411932-15
[research_topcu_casoliva_2005]: https://doi.org/10.2514/6.2005-6286
[research_toraldo_ketabdari_2023]: https://doi.org/10.3390/designs7020041
[research_torresmartinez_heaps_2010]: https://doi.org/10.1109/igarss.2010.5649309
[research_toso_maddock_2017]: https://doi.org/10.2514/6.2017-2250
[research_tournes_johnson_1998]: https://doi.org/10.2514/6.1998-4151
[research_tournes_johnson_1998_b]: https://doi.org/10.2514/6.1998-4119
[research_tournes_johnson_2001]: https://doi.org/10.2514/2.4710
[research_tournes_landrum_1998]: https://doi.org/10.2514/2.4273
[research_tracy_1981]: https://doi.org/10.2514/6.1981-2464
[research_trajectory_shaping_2025]: https://doi.org/10.37285/bsp.sacad2025.24
[research_trawny_2015]: https://ntrs.nasa.gov/citations/20160009637
[research_trevino_schwartz_2012]: https://doi.org/10.2514/6.2012-797
[research_trifonov_shelkov_2024]: https://doi.org/10.1007/s42401-023-00253-2
[research_tripathi_kumarsinha_2024]: https://doi.org/10.1109/icarcv63323.2024.10854986
[research_tripathi_patel_2018]: https://doi.org/10.1109/icarcv.2018.8581208
[research_tripathi_patel_2024]: https://doi.org/10.1016/j.ifacol.2024.05.022
[research_tripropellant_engine_2004]: https://doi.org/10.2514/5.9781600866760.0649.0682
[research_trittler_rothermel_2016]: https://doi.org/10.2514/1.g000261
[research_trivailo_lentsch_2013]: https://doi.org/10.2514/6.2013-5521
[research_troya_mailloux_2018]: https://doi.org/10.1109/syseng.2018.8544459
[research_trujillo_meyerjr_1983]: https://doi.org/10.2514/6.1983-2704
[research_trusfus_abdullin_2021]: https://doi.org/10.34759/trd-2021-116-13
[research_trushlyakov_yudintsev_2019]: https://doi.org/10.1088/1742-6596/1210/1/012148
[research_truxtondavies_powell_1970]: https://doi.org/10.1109/sap.1970.269969
[research_tsai_2008]: https://doi.org/10.2514/6.2008-7240
[research_tsapparellas_jelev_2023]: https://doi.org/10.1109/icma57826.2023.10215523
[research_tseng_lou_2013]: https://doi.org/10.4028/www.scientific.net/amm.411-414.1815
[research_tsikalas_1982]: https://doi.org/10.2514/6.1982-1604
[research_tsikalas_1982_b]: https://ntrs.nasa.gov/citations/19820062072
[research_tsitses_zacharia_2024]: https://doi.org/10.3390/s24020680
[research_tsohas_heister_2010]: https://doi.org/10.2514/6.2010-6632
[research_tsoukalas_unlu_2026]: https://doi.org/10.1109/icuas69441.2026.11598570
[research_tsuchiya_suzuki_1998]: https://doi.org/10.1016/s1474-6670(17)41115-3
[research_tsuchiya_suzuki_2001]: https://doi.org/10.2514/6.2001-1847
[research_tsukahara_yamao_2001]: https://doi.org/10.2514/6.2001-1909
[research_tsukamoto_deturris_2003]: https://doi.org/10.2514/6.2003-911
[research_tsukamoto_suzuki_2004]: https://doi.org/10.2514/6.2004-4944
[research_tsukerman_weiss_2017]: https://doi.org/10.2514/6.2017-1025
[research_tsushima_saitoh_2024]: https://doi.org/10.2514/6.2024-2401
[research_tsuyuki_2005]: https://ntrs.nasa.gov/citations/20090026396
[research_tu_munir_1998]: https://doi.org/10.2514/6.1998-4573
[research_tuohy_1998]: https://doi.org/10.2514/6.1998-4177
[research_tuozzo_fox_2017]: https://doi.org/10.4050/f-0073-2017-12117
[research_tupitsin_stepanenko_2020]: https://doi.org/10.18372/1990-5548.64.14864
[research_turnbow_1961]: https://doi.org/10.21236/ad0261961
[research_turner_1950]: https://ntrs.nasa.gov/citations/19930086353
[research_turner_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50015-4
[research_turner_2000]: https://ntrs.nasa.gov/citations/20000112931
[research_turner_2003]: https://doi.org/10.2514/6.2003-2710
[research_turner_2003_b]: https://ntrs.nasa.gov/citations/20030111778
[research_turner_2005]: https://ntrs.nasa.gov/citations/20050217401
[research_tushavina_2025]: https://doi.org/10.1134/s1995080225608318
[research_tweedale_gonano_2014]: https://doi.org/10.1016/j.procs.2014.08.190
[research_udayakumar_ibrahim_2019]: https://doi.org/10.1109/iceca.2019.8821873
[research_ueno_yamaguchi_1999]: https://doi.org/10.2514/6.1999-3983
[research_uffelman_deffenbaugh_1979]: https://doi.org/10.2514/6.1979-1626
[research_ulukir_dursun_2025]: https://doi.org/10.1007/s11768-025-00275-5
[research_ulybyshev_2010]: https://doi.org/10.1134/s0010952510060067
[research_umadevi_navas_2017]: https://doi.org/10.1007/s40032-017-0404-8
[research_ungvichian_1986]: https://doi.org/10.1049/el:19860325
[research_uppoor_2026]: https://doi.org/10.2514/1.c039019
[research_uppoor_chopra_2026]: https://doi.org/10.4050/f-0082-2026-0148
[research_uppoor_zheng_2025]: https://doi.org/10.4050/f-0081-2025-0343
[research_urnes_hess_1979]: https://doi.org/10.2514/6.1979-1772
[research_urnes_hess_1983]: https://doi.org/10.2514/6.1983-2162
[research_urnes_hess_1985]: https://doi.org/10.2514/3.19978
[research_urschel_cox_2003]: https://doi.org/10.2514/6.2003-5544
[research_usry_1971]: https://ntrs.nasa.gov/citations/19720004249
[research_utterstrom_kestek_1965]: https://doi.org/10.2514/6.1965-1234
[research_uybarreta_grant_2025]: https://doi.org/10.2514/6.2025-3610
[research_vagliolaurin_finke_1965]: https://doi.org/10.4271/650801
[research_vaispacher_baranek_2025]: https://doi.org/10.3390/engproc2025088028
[research_valente_bartuli_2006]: https://doi.org/10.4028/3-908158-01-x.1505
[research_valentine_2004]: https://ntrs.nasa.gov/citations/20040086536
[research_vallot_snyder_1991]: https://doi.org/10.1002/j.2161-4296.1991.tb01719.x
[research_vanatta_inderhees_1988]: https://doi.org/10.2514/6.1988-2121
[research_vanbavel_2014]: https://doi.org/10.2514/6.2014-2059
[research_vandenabeelen_2016]: https://doi.org/10.1007/978-3-319-44472-7_1
[research_vandenabeelen_2016_b]: https://doi.org/10.1007/978-3-319-44472-7_20
[research_vandenbroek_hunns_2026]: https://doi.org/10.1016/j.ast.2025.111475
[research_vandenbroek_simpson_2025]: https://doi.org/10.2514/6.2025-1954
[research_vanes_2017]: https://doi.org/10.2514/6.2017-3651
[research_vangaasbeek_1980]: https://doi.org/10.21236/ada089008
[research_vangraas_diggle_1994]: https://doi.org/10.1002/j.2161-4296.1994.tb02322.x
[research_vanoort_chu_2007]: https://doi.org/10.3182/20070625-5-fr-2916.00056
[research_vanwyckhouse_1966]: https://doi.org/10.21236/ad0630927
[research_vaquero_kennedy_2022]: https://doi.org/10.2514/6.2022-2475
[research_vasconcelos_oliveira_2005]: https://doi.org/10.2514/6.2005-6057
[research_vassilakos_2011]: https://ntrs.nasa.gov/citations/20110007367
[research_veaux_1988]: https://doi.org/10.2514/3.45678
[research_vendemia_1965]: https://doi.org/10.21236/ad0630342
[research_veneruso_miccio_2024]: https://doi.org/10.1109/dasc62030.2024.10749214
[research_venkateswararao_go_2014]: https://doi.org/10.1016/j.ast.2013.10.001
[research_ventanas_nd]: https://doi.org/10.20868/upm.thesis.43277
[research_venugopalan_taher_2012]: https://doi.org/10.1109/oceans.2012.6404893
[research_vepa_zhahir_2010]: https://doi.org/10.1017/s0373463310000329
[research_verderame_phillips_1999]: https://doi.org/10.2514/6.1999-4608
[research_verhaegen_1988]: https://doi.org/10.2514/3.20272
[research_verkhovsky_gyazova_2023]: https://doi.org/10.52375/20728689_2023_2_150
[research_verma_1991]: https://doi.org/10.21236/ada237470
[research_verma_mettler_2017]: https://doi.org/10.2514/1.g001889
[research_verstraete_bizzarri_2009]: https://doi.org/10.1051/eucass/20091551
[research_vetter_1966]: https://doi.org/10.2514/6.1966-47
[research_vibration_of_1975]: https://doi.org/10.7551/mitpress/6449.003.0022
[research_vidal_1974]: https://ntrs.nasa.gov/citations/19750012378
[research_videmsek_dehaag_2020]: https://doi.org/10.23919/enc48637.2020.9317481
[research_vijayanandh_kiran_2020]: https://doi.org/10.1007/978-3-030-37393-1_15
[research_viladegut_2018]: https://doi.org/10.35294/phdt201804
[research_villanueva_2022]: https://doi.org/10.1109/eircon56026.2022.9934090
[research_vinh_medepalli_1994]: https://doi.org/10.1007/978-1-4615-2425-0_14
[research_vinod_geetha_2012]: https://doi.org/10.1007/s40032-011-0007-8
[research_violette_2024]: https://doi.org/10.2514/6.2024-0367
[research_violette_2026]: https://doi.org/10.2514/6.2026-2325
[research_viscardi_arena_2021]: https://doi.org/10.1016/j.matpr.2020.03.694
[research_viswanathan_sanyal_2017]: https://doi.org/10.2514/6.2017-1044
[research_viviand_1991]: https://doi.org/10.1007/978-3-642-84580-2_7
[research_viviani_pezzella_2006]: https://doi.org/10.2514/6.2006-8082
[research_viviani_pezzella_2007]: https://doi.org/10.2514/6.2007-4047
[research_viviani_pezzella_2007_b]: https://doi.org/10.2514/6.2007-1211
[research_viviani_pezzella_2008]: https://doi.org/10.2514/6.2008-2668
[research_viviani_pezzella_2009]: https://doi.org/10.1080/19942060.2009.11015290
[research_viviani_pezzella_2010]: https://doi.org/10.2514/1.40876
[research_vo_garrard_1993]: https://doi.org/10.2514/6.1993-1224
[research_vocke_nunez_2016]: https://doi.org/10.21236/ad1011994
[research_volkov_komar_2022]: https://doi.org/10.1007/s10559-023-00521-1
[research_voloshenyuk_2018]: https://doi.org/10.15407/usim.2017.06.065
[research_vorburger_mclay_1985]: https://doi.org/10.2514/6.1985-228
[research_vorobev_beliatskaya_2020]: https://doi.org/10.26467/2079-0619-2020-23-4-33-44
[research_vos_hodigeresiddaramaiah_2007]: https://doi.org/10.2514/6.2007-1706
[research_voss_tang_2026]: https://doi.org/10.2514/6.2026-1156
[research_w_p_2020]: https://doi.org/10.52453/t.v11i2.302
[research_wa_1963]: https://doi.org/10.21236/ad0414555
[research_wagner_valasek_2006]: https://doi.org/10.2514/6.2006-6599
[research_wagner_valasek_2007]: https://doi.org/10.2514/1.27761
[research_wahi_straub_1977]: https://doi.org/10.21236/ada039968
[research_waitman_marcos_2019]: https://doi.org/10.1109/systol.2019.8864789
[research_wakamatsu_ono_1999]: https://doi.org/10.2514/6.1999-4867
[research_waldmann_ehrle_2023]: https://doi.org/10.1007/s00348-023-03642-7
[research_walker_1960]: https://doi.org/10.1049/sqj.1960.0043
[research_walker_1981]: https://ntrs.nasa.gov/citations/19820002128
[research_walker_mueschke_2018]: https://doi.org/10.2514/6.2018-5382
[research_wallace_1963]: https://doi.org/10.2514/3.2128
[research_wallace_olds_2003]: https://doi.org/10.2514/6.2003-5269
[research_wallner_well_2002]: https://doi.org/10.2514/6.2002-4647
[research_wallskog_1954]: https://ntrs.nasa.gov/citations/20090023601
[research_walpot_noeding_2006]: https://doi.org/10.2514/6.2006-8077
[research_walton_2025]: https://doi.org/10.2139/ssrn.5329969
[research_wan_pan_2023]: https://doi.org/10.1007/978-981-19-6613-2_477
[research_wang_1963]: https://doi.org/10.21236/ad0402079
[research_wang_2016]: https://doi.org/10.1051/matecconf/20167701038
[research_wang_2021]: https://doi.org/10.1109/cacre52464.2021.9501289
[research_wang_2022]: https://doi.org/10.1155/2022/4627111
[research_wang_2022_b]: https://doi.org/10.1049/icp.2022.1550
[research_wang_2024]: https://doi.org/10.1117/12.3027186
[research_wang_ai_2025]: https://doi.org/10.2514/1.t7047
[research_wang_bi_2022]: https://doi.org/10.1007/978-981-16-9492-9_284
[research_wang_chen_2016]: https://doi.org/10.1155/2016/7345056
[research_wang_chen_2019]: https://doi.org/10.1109/iccasit48058.2019.8973184
[research_wang_chen_2020]: https://doi.org/10.3390/sym12091572
[research_wang_cui_2018]: https://doi.org/10.2514/6.2018-1871
[research_wang_demiroz_1986]: https://doi.org/10.2514/6.1986-9772
[research_wang_ding_2026]: https://doi.org/10.1109/ccdc69976.2026.11560758
[research_wang_dong_2018]: https://doi.org/10.1007/s10291-018-0718-x
[research_wang_feng_2017]: https://doi.org/10.23919/chicc.2017.8028295
[research_wang_feng_2024]: https://doi.org/10.3390/rs16122161
[research_wang_gan_2025]: https://doi.org/10.1109/comea66280.2025.11241251
[research_wang_gong_2022]: https://doi.org/10.3390/math11010066
[research_wang_holzapfel_2018]: https://doi.org/10.2514/6.2018-1166
[research_wang_hua_2015]: https://doi.org/10.1002/acs.2541
[research_wang_hua_2016]: https://doi.org/10.1109/chicc.2016.7555060
[research_wang_jau_2007]: https://doi.org/10.1109/icias.2007.4658394
[research_wang_jia_2018]: https://doi.org/10.1007/978-981-13-0005-9_59
[research_wang_jiang_2022]: https://doi.org/10.1016/j.isatra.2021.11.031
[research_wang_jiang_2023]: https://doi.org/10.1007/s12555-021-0901-7
[research_wang_li_2014]: https://doi.org/10.1109/cgncc.2014.7007445
[research_wang_li_2018]: https://doi.org/10.1007/s42401-018-0006-z
[research_wang_li_2018_b]: https://doi.org/10.1109/gncc42960.2018.9019210
[research_wang_li_2021]: https://doi.org/10.1049/rsn2.12199
[research_wang_li_2023]: https://doi.org/10.1016/j.engappai.2022.105497
[research_wang_li_2023_b]: https://doi.org/10.23919/ccc58697.2023.10240825
[research_wang_lin_2022]: https://doi.org/10.1177/01423312221104424
[research_wang_liu_2011]: https://doi.org/10.1109/rast.2011.5966829
[research_wang_liu_2012]: https://doi.org/10.4028/www.scientific.net/amm.232.194
[research_wang_liu_2019]: https://doi.org/10.1109/tps.2019.2926166
[research_wang_liu_2024]: https://doi.org/10.1007/978-981-97-3336-1_23
[research_wang_lu_2016]: https://doi.org/10.1109/chicc.2016.7555043
[research_wang_lu_2017]: https://doi.org/10.23919/acc.2017.7963614
[research_wang_ma_2023]: https://doi.org/10.3390/drones7120703
[research_wang_mou_2025]: https://doi.org/10.2514/1.i011487
[research_wang_mu_2025]: https://doi.org/10.1109/cac67268.2025.11487780
[research_wang_peng_2005]: https://doi.org/10.1117/12.654995
[research_wang_peng_2006]: https://doi.org/10.1142/s0218001406005216
[research_wang_shao_2025]: https://doi.org/10.3390/sym17010072
[research_wang_song_2018]: https://doi.org/10.1109/cac.2018.8623496
[research_wang_tang_2013]: https://doi.org/10.1109/cac.2013.6775751
[research_wang_tang_2023]: https://doi.org/10.1007/978-981-19-6613-2_287
[research_wang_wang_1997]: https://doi.org/10.2514/6.1997-2944
[research_wang_wang_2013]: https://doi.org/10.4028/www.scientific.net/amr.748.747
[research_wang_wang_2014]: https://doi.org/10.1117/1.oe.53.6.064103
[research_wang_wang_2016]: https://doi.org/10.1109/aus.2016.7748083
[research_wang_wang_2025]: https://doi.org/10.1007/978-981-96-2212-2_45
[research_wang_wang_2025_b]: https://doi.org/10.3390/s25113379
[research_wang_wei_2022]: https://doi.org/10.3390/app121910153
[research_wang_wu_2009]: https://doi.org/10.1007/s12555-009-0401-7
[research_wang_wu_2014]: https://doi.org/10.1142/s1793962314500147
[research_wang_wu_2019]: https://doi.org/10.1109/imcec46724.2019.8984061
[research_wang_xu_2014]: https://doi.org/10.4028/www.scientific.net/amr.945-949.662
[research_wang_xu_2020]: https://doi.org/10.1360/sst-2020-0211
[research_wang_xu_2024]: https://doi.org/10.1016/j.ijthermalsci.2023.108857
[research_wang_yang_2022]: https://doi.org/10.1007/s42405-022-00506-y
[research_wang_yang_2025]: https://doi.org/10.1007/978-981-96-2252-8_6
[research_wang_yang_2025_b]: https://doi.org/10.1016/j.jfranklin.2024.107426
[research_wang_yin_2020]: https://doi.org/10.1088/1757-899x/887/1/012035
[research_wang_yin_2024]: https://doi.org/10.1007/978-981-99-8045-1_14
[research_wang_yu_2016]: https://doi.org/10.1017/aer.2016.16
[research_wang_yuan_2023]: https://doi.org/10.1007/978-981-19-6613-2_59
[research_wang_zhai_2023]: https://doi.org/10.1007/s10291-023-01423-7
[research_wang_zhang_2013]: https://doi.org/10.4028/www.scientific.net/amr.823.62
[research_wang_zhang_2017]: https://doi.org/10.1177/0954410017746432
[research_wang_zhang_2019]: https://doi.org/10.1177/0959651819868039
[research_wang_zhang_2020]: https://doi.org/10.1016/j.ast.2020.106114
[research_wang_zhang_2026]: https://doi.org/10.1177/10775463251410847
[research_wang_zhao_2022]: https://doi.org/10.3390/aerospace9100615
[research_wang_zhao_2022_b]: https://doi.org/10.1117/12.2639180
[research_wang_zheng_2022]: https://doi.org/10.1016/j.heliyon.2022.e11249
[research_wang_zhou_2016]: https://doi.org/10.1109/cgncc.2016.7828813
[research_wang_zhou_2017]: https://doi.org/10.23919/icins.2017.7995607
[research_wang_zong_2015]: https://doi.org/10.1109/chicc.2015.7259721
[research_wang_zou_2017]: https://doi.org/10.1177/1687814017744077
[research_wang_zou_2021]: https://doi.org/10.1007/978-3-030-81007-8_108
[research_wanglu_yaoweili_2016]: https://doi.org/10.1109/cgncc.2016.7829029
[research_wangshihao_yanzilin_2018]: https://doi.org/10.1049/cp.2018.0231
[research_wangu_mouyos_1998]: https://doi.org/10.2514/6.1998-5239
[research_ward_collins_2026]: https://doi.org/10.2514/6.2026-4688
[research_ward_costello_2012]: https://doi.org/10.1109/acc.2012.6315600
[research_ward_costello_2013]: https://doi.org/10.2514/1.59260
[research_ward_costello_2015]: https://doi.org/10.2514/6.2015-2148
[research_ward_gavrilovski_2011]: https://doi.org/10.2514/6.2011-2572
[research_ward_gavrilovski_2011_b]: https://doi.org/10.2514/6.2011-2620
[research_ward_gavrilovski_2013]: https://doi.org/10.2514/1.c032029
[research_ward_ho_2025]: https://doi.org/10.2514/6.2025-3539
[research_ward_myers_1967]: https://doi.org/10.21236/ad0815090
[research_ward_smart_2026]: https://doi.org/10.2514/6.2026-5107
[research_wardana_pranoto_2021]: https://doi.org/10.1063/5.0060371
[research_ware_spencerjr_1991]: https://doi.org/10.2514/6.1991-3215
[research_warner_1981]: https://ntrs.nasa.gov/citations/19820006228
[research_warren_2024]: https://doi.org/10.2514/6.2024-0133
[research_warsop_crowther_2019]: https://doi.org/10.2514/6.2019-0282
[research_watanabe_ishimoto_1997]: https://doi.org/10.2514/2.3259
[research_watson_1981]: https://ntrs.nasa.gov/citations/19810010515
[research_watson_1983]: https://ntrs.nasa.gov/citations/19840005130
[research_watson_hardy_1986]: https://doi.org/10.2514/6.1986-2130
[research_watson_morgan_nd]: https://ntrs.nasa.gov/citations/20205004015
[research_watts_2005]: https://doi.org/10.2514/6.2005-6375
[research_way_desai_2003]: https://doi.org/10.2514/6.2003-2128
[research_way_sescu_2024]: https://doi.org/10.2514/6.2024-4107
[research_webb_bettinger_2024]: https://doi.org/10.2514/6.2024-1915
[research_webb_bettinger_2026]: https://doi.org/10.1016/j.ast.2026.112231
[research_wee_yechout_2004]: https://doi.org/10.2514/6.2004-722
[research_wei_2005]: https://doi.org/10.2514/1.6801
[research_wei_2024]: https://doi.org/10.1109/icra57147.2024.10611536
[research_wei_diaz_2026]: https://doi.org/10.2514/6.2026-114336
[research_wei_du_2018]: https://doi.org/10.1109/gncc42960.2018.9019216
[research_wei_gjestvang_2001]: https://doi.org/10.2514/6.2001-992
[research_wei_kang_2025]: https://doi.org/10.1007/978-981-96-2248-1_16
[research_wei_wang_2022]: https://doi.org/10.1016/j.cja.2021.03.017
[research_wei_wang_2025]: https://doi.org/10.1109/cac67268.2025.11487477
[research_wei_xu_2018]: https://doi.org/10.1109/gncc42960.2018.9019194
[research_weiland_2003]: https://doi.org/10.1016/b978-008044046-0/50293-1
[research_weinacht_2003]: https://doi.org/10.21236/ada417123
[research_weingarten_chalk_1982]: https://doi.org/10.2514/6.1982-1296
[research_weismuller_caballero_2007]: https://doi.org/10.2514/6.2007-6173
[research_weiwei_runde_2022]: https://doi.org/10.1109/cac57257.2022.10055554
[research_welberg_werner_2015]: https://doi.org/10.2514/6.2015-4123
[research_welch_1993]: https://ntrs.nasa.gov/citations/19930013950
[research_welge_2000]: https://ntrs.nasa.gov/citations/20010000880
[research_welker_huffman_2011]: https://doi.org/10.2514/6.2011-6643
[research_welker_pachter_2013]: https://doi.org/10.23919/ecc.2013.6669109
[research_wells_1987]: https://doi.org/10.2514/6.1987-2367
[research_welsh_1967]: https://doi.org/10.21236/ad0658433
[research_welton_1965]: https://ntrs.nasa.gov/citations/19650024803
[research_wen_huang_2021]: https://doi.org/10.1109/icetci53161.2021.9563541
[research_wendel_1991]: https://ntrs.nasa.gov/citations/19910064980
[research_weng_liu_2020]: https://doi.org/10.1007/s10291-020-00998-9
[research_wenming_zhi_2015]: https://doi.org/10.1109/chicc.2015.7259750
[research_wenzel_masselli_2010]: https://doi.org/10.1007/978-94-007-1110-5_15
[research_wernicke_1997]: https://doi.org/10.2514/6.1997-5603
[research_westbrook_1975]: https://doi.org/10.21236/ada004476
[research_westphal_wagner_2001]: https://doi.org/10.2514/6.2001-1319
[research_white_2010]: https://doi.org/10.2514/1.45222
[research_white_beck_2011]: https://doi.org/10.2514/6.2011-3491
[research_white_fonnegra_2024]: https://doi.org/10.2514/6.2024-85725
[research_white_gibson_2004]: https://doi.org/10.2514/6.2004-768
[research_white_jamesj_1967]: https://doi.org/10.21236/ad0648552
[research_whitfield_1963]: https://doi.org/10.21236/ad0298278
[research_whiting_neill_2024]: https://doi.org/10.2514/6.2024-1845
[research_whitmore_2004]: https://ntrs.nasa.gov/citations/20040013412
[research_whitmore_dunbar_2003]: https://doi.org/10.2514/6.2003-2718
[research_wibben_furfaro_2012]: https://doi.org/10.2514/6.2012-4919
[research_widnall_1974]: https://doi.org/10.21236/ada002879
[research_widnall_gobbini_1982]: https://doi.org/10.21236/ada116417
[research_widnall_morth_1972]: https://doi.org/10.1002/j.2161-4296.1972.tb01708.x
[research_wierzbanowski_ramasubramanian_2020]: https://doi.org/10.2514/6.2020-4205
[research_wijaya_nurrohmad_2020]: https://doi.org/10.30536/j.jtd.2020.v18.a3377
[research_wilcox_1963]: https://doi.org/10.21236/ad0400570
[research_wilder_2015]: https://ntrs.nasa.gov/citations/20150021846
[research_wilder_2019]: https://ntrs.nasa.gov/citations/20190028253
[research_wilhite_1977]: https://ntrs.nasa.gov/citations/19770018245
[research_williams_1947]: https://doi.org/10.1049/ji-3a-2.1947.0028
[research_williams_1994]: https://ntrs.nasa.gov/citations/19950007823
[research_williams_2017]: https://doi.org/10.4271/2017-01-2016
[research_williams_2021]: https://doi.org/10.1088/978-0-7503-3655-0ch6
[research_williams_alseyab_2026]: https://doi.org/10.1007/978-981-95-6445-3_28
[research_williams_curry_1995]: https://doi.org/10.2514/3.26637
[research_williams_davis_2000]: https://doi.org/10.21236/ada459739
[research_williams_hartford_1987]: https://doi.org/10.2514/6.1987-2924
[research_williamson_1980]: https://doi.org/10.2514/3.56024
[research_williamson_1992]: https://doi.org/10.2514/6.1992-3989
[research_williamson_bi_2025]: https://doi.org/10.2514/6.2025-3408
[research_williamson_speyer_2005]: https://doi.org/10.21236/ada433107
[research_williamsonjr_1978]: https://doi.org/10.2514/6.1978-1366
[research_wilson_1967]: https://ntrs.nasa.gov/citations/19670005606
[research_wilson_1980]: https://doi.org/10.21236/ada092788
[research_wilson_chou_1985]: https://doi.org/10.2514/6.1985-315
[research_wilson_goktogan_2015]: https://doi.org/10.1002/rob.21637
[research_wilson_riccardi_2022]: https://doi.org/10.1016/j.actaastro.2022.07.013
[research_wilz_johnson_1975]: https://doi.org/10.2514/6.1975-1021
[research_winchenbach_1997]: https://doi.org/10.21236/ada328536
[research_wind_tunnel_study_1981]: https://doi.org/10.2514/5.9781600865510.0260.0286
[research_windhorst_ardema_1997]: https://doi.org/10.2514/6.1997-3535
[research_winski_langston_2025]: https://doi.org/10.2514/6.2025-3461
[research_wisely_2002]: https://doi.org/10.1049/ic:20020015
[research_wiseman_lopez_2026]: https://doi.org/10.2514/6.2026-112080
[research_witte_roll_2016]: https://doi.org/10.1016/j.actaastro.2016.02.001
[research_wittliff_oconnor_1992]: https://doi.org/10.2514/6.1992-3906
[research_woestemeyer_1964]: https://doi.org/10.2514/6.1964-645
[research_woestemeyer_1967]: https://doi.org/10.2514/3.29041
[research_woicke_kruger_2023]: https://doi.org/10.2514/6.2023-0690
[research_woicke_mooij_2017]: https://doi.org/10.1007/978-3-319-65283-2_39
[research_wolf_1996]: https://doi.org/10.1017/s0001924000027299
[research_wolf_2011]: https://ntrs.nasa.gov/citations/20110020614
[research_wolf_bossert_2001]: https://doi.org/10.2514/6.2001-4313
[research_wolf_casoliva_2012]: https://doi.org/10.1109/aero.2012.6187005
[research_wolfe_1976]: https://doi.org/10.21236/ada034873
[research_woloshen_1974]: https://doi.org/10.21236/ada043527
[research_wong_ryan_2017]: https://doi.org/10.1007/s00158-017-1817-y
[research_wood_1968]: https://doi.org/10.1108/eb034334
[research_wood_1972]: https://doi.org/10.1017/s0373463300022554
[research_wood_2012]: https://doi.org/10.1016/j.matdes.2011.03.041
[research_wood_avadhanula_2007]: https://doi.org/10.1109/mra.2007.380656
[research_woodbury_1974]: https://ntrs.nasa.gov/citations/19740027145
[research_woodbury_gorman_1983]: https://doi.org/10.2514/6.1983-2729
[research_woodbury_valasek_2015]: https://doi.org/10.2514/6.2015-1073
[research_woodbury_valasek_2015_b]: https://doi.org/10.2514/6.2015-1481
[research_woodbury_valasek_2016]: https://doi.org/10.2514/1.g001758
[research_woods_2000]: https://ntrs.nasa.gov/citations/20000081743
[research_woods_2000_b]: https://ntrs.nasa.gov/citations/20000099722
[research_woollard_braun_2016]: https://doi.org/10.1109/aero.2016.7500556
[research_wortman_1969]: https://doi.org/10.2514/6.1969-866
[research_wright_1971]: https://ntrs.nasa.gov/citations/19770076296
[research_wright_1989]: https://doi.org/10.2514/6.1989-5003
[research_wright_1992]: https://doi.org/10.1080/00033799200200251
[research_wright_beck_2014]: https://doi.org/10.2514/1.a32579
[research_wright_milos_2006]: https://doi.org/10.2514/1.17703
[research_wu_2015]: https://doi.org/10.9734/bjast/2015/17376
[research_wu_2018]: https://doi.org/10.12783/dtetr/pmsms2018/24866
[research_wu_2023]: https://doi.org/10.1201/9781003343165-15
[research_wu_2024]: https://doi.org/10.62381/acs.sdit2024.44
[research_wu_2024_b]: https://doi.org/10.3390/drones9010003
[research_wu_cai_2014]: https://doi.org/10.1109/cgncc.2014.7007507
[research_wu_gu_2017]: https://doi.org/10.23919/icins.2017.7995603
[research_wu_guo_1994]: https://doi.org/10.2514/3.21196
[research_wu_johnson_2005]: https://doi.org/10.2514/6.2005-5998
[research_wu_lian_2017]: https://doi.org/10.2514/6.2017-2202
[research_wu_liu_2021]: https://doi.org/10.1145/3459104.3459109
[research_wu_luo_2019]: https://doi.org/10.1007/978-981-32-9682-4_10
[research_wu_luo_2023]: https://doi.org/10.1007/978-981-19-6613-2_581
[research_wu_lycans_1994]: https://doi.org/10.2514/6.1994-2023
[research_wu_shi_2018]: https://doi.org/10.23919/chicc.2018.8483338
[research_wu_shi_2022]: https://doi.org/10.1088/1742-6596/2403/1/012027
[research_wu_tang_2012]: https://doi.org/10.4028/www.scientific.net/amr.591-593.2624
[research_wu_tian_2020]: https://doi.org/10.23919/ccc50068.2020.9188640
[research_wu_wang_2018]: https://doi.org/10.1109/imccc.2018.00226
[research_wu_yuan_2025]: https://doi.org/10.3934/jimo.2025010
[research_wu_zhang_2018]: https://doi.org/10.1109/gncc42960.2018.9018887
[research_wu_zhang_2023]: https://doi.org/10.54254/2755-2721/11/20230209
[research_wu_zhu_2026]: https://doi.org/10.1108/aeat-08-2025-0295
[research_wurster_riley_1999]: https://doi.org/10.2514/2.3452
[research_wurster_stone_1993]: https://doi.org/10.2514/3.25565
[research_wuxing_chunwang_2015]: https://doi.org/10.1109/chicc.2015.7260440
[research_wuxing_pengxin_2015]: https://doi.org/10.1109/chicc.2015.7260512
[research_wyborny_requardt_1974]: https://doi.org/10.2514/6.1974-613
[research_wyborny_requardt_1975]: https://doi.org/10.2514/3.56956
[research_wygle_1965]: https://doi.org/10.4271/650848
[research_x_33_1999]: https://ntrs.nasa.gov/citations/20000033861
[research_x_37_flight_2004]: https://doi.org/10.2514/6.iac-04-v.6.05
[research_xargay_hovakimyan_2010]: https://doi.org/10.2514/6.2010-7773
[research_xi_li_2023]: https://doi.org/10.1109/iscsic60498.2023.00069
[research_xia_hu_2025]: https://doi.org/10.1007/978-981-96-2264-1_20
[research_xiang_du_2026]: https://doi.org/10.1061/jaeeez.aseng-6834
[research_xiang_guo_2024]: https://doi.org/10.1007/978-981-97-1099-7_22
[research_xiang_guo_2025]: https://doi.org/10.1007/s12555-024-0155-2
[research_xiang_zhou_2022]: https://doi.org/10.1007/978-981-16-7258-3_31
[research_xiangyu_hutao_2004]: https://doi.org/10.1016/j.actaastro.2003.09.001
[research_xiao_2022]: https://doi.org/10.1007/978-981-16-8052-6_141
[research_xiao_2026]: https://doi.org/10.1109/etai68332.2026.11485174
[research_xiaoqingchen_zhongxihou_2010]: https://doi.org/10.1109/isscaa.2010.5634043
[research_xie_2024]: https://doi.org/10.1117/12.3027188
[research_xie_li_2016]: https://doi.org/10.2991/msmi-16.2016.11
[research_xin_2021]: https://doi.org/10.1088/1742-6596/1750/1/012022
[research_xingling_honglun_2014]: https://doi.org/10.1016/j.isatra.2014.09.021
[research_xinguo_ting_2024]: https://doi.org/10.1109/ccdc62350.2024.10587450
[research_xiong_zhao_2018]: https://doi.org/10.1109/inertialsensors.2018.8577185
[research_xiuzhen_shaolei_2014]: https://doi.org/10.1109/cgncc.2014.7007256
[research_xu_2015]: https://doi.org/10.1007/s11071-015-1958-8
[research_xu_2025]: https://doi.org/10.1109/aipip66876.2025.11299229
[research_xu_dong_2022]: https://doi.org/10.1109/cac57257.2022.10055577
[research_xu_fu_2018]: https://doi.org/10.1016/j.ast.2018.07.007
[research_xu_guan_2022]: https://doi.org/10.3390/app12157436
[research_xu_guan_2023]: https://doi.org/10.1016/j.actaastro.2022.12.044
[research_xu_guo_2025]: https://doi.org/10.3390/act14110565
[research_xu_hu_2020]: https://doi.org/10.23919/ccc50068.2020.9188979
[research_xu_huang_2021]: https://doi.org/10.1016/j.ast.2021.107040
[research_xu_lan_2018]: https://doi.org/10.1109/icmic.2018.8529840
[research_xu_liu_2021]: https://doi.org/10.3390/rs13040772
[research_xu_mirmirani_2004]: https://doi.org/10.2514/1.12596
[research_xu_sun_2012]: https://doi.org/10.1049/iet-cta.2011.0026
[research_xu_tang_2010]: https://doi.org/10.1109/cmce.2010.5610293
[research_xu_wang_2016]: https://doi.org/10.1371/journal.pone.0167168
[research_xu_wang_2017]: https://doi.org/10.2514/1.g002105
[research_xu_wang_2017_b]: https://doi.org/10.23919/chicc.2017.8028301
[research_xu_xia_2012]: https://doi.org/10.4028/www.scientific.net/amr.562-564.1442
[research_xu_zhao_2017]: https://doi.org/10.23919/chicc.2017.8028367
[research_xue_qin_2019]: https://doi.org/10.1177/1687814019853062
[research_xuguo_ke_2018]: https://doi.org/10.1109/gncc42960.2018.9019176
[research_xuxibao_guojifeng_2016]: https://doi.org/10.1109/cgncc.2016.7829158
[research_y_2013]: https://doi.org/10.4172/2168-9792.1000107
[research_yadav_bodavula_2018]: https://doi.org/10.1017/aer.2018.109
[research_yadav_ramamoorthy_1991]: https://doi.org/10.1115/1.2896474
[research_yafei_jianqiao_2015]: https://doi.org/10.1109/chicc.2015.7260509
[research_yager_1983]: https://doi.org/10.2514/6.1983-274
[research_yager_1991]: https://doi.org/10.4271/912156
[research_yakimenko_altmann_2015]: https://doi.org/10.2514/5.9781624101960.0127.0198
[research_yamada_kawano_2014]: https://doi.org/10.2322/tastj.12.pk_83
[research_yamada_suzuki_2011]: https://doi.org/10.2322/tjsass.54.51
[research_yamada_suzuki_2016]: https://doi.org/10.2322/tastj.14.pe_77
[research_yamamoto_atsumi_1996]: https://doi.org/10.1163/156855196x00293
[research_yamanaka_1989]: https://doi.org/10.2514/6.1989-5008
[research_yamanaka_2003]: https://doi.org/10.2514/6.2003-6996
[research_yamanaka_maita_2001]: https://doi.org/10.2514/6.2001-1923
[research_yamasaki_matsumoto_2013]: https://doi.org/10.1109/aim.2013.6584309
[research_yan_chen_2025]: https://doi.org/10.1061/jaeeez.aseng-5871
[research_yan_he_2020]: https://doi.org/10.1016/j.ast.2020.105841
[research_yan_hexi_2025]: https://doi.org/10.1007/978-981-96-2232-0_23
[research_yan_luo_2015]: https://doi.org/10.2514/6.2015-2951
[research_yan_tan_2016]: https://doi.org/10.1109/chicc.2016.7555033
[research_yan_vonderdunk_1992]: https://doi.org/10.54648/aila1992004
[research_yan_wang_2015]: https://doi.org/10.1007/978-3-662-46632-2_68
[research_yan_xu_2013]: https://doi.org/10.4304/jcp.8.8.1973-1978
[research_yan_zhao_2023]: https://doi.org/10.1007/978-981-19-6613-2_491
[research_yanagihara_shigemi_1999]: https://doi.org/10.2514/2.2553
[research_yanagihara_suzuki_1991]: https://doi.org/10.4271/911979
[research_yang_2025]: https://doi.org/10.2514/1.g008911
[research_yang_chen_2023]: https://doi.org/10.1063/5.0170578
[research_yang_chen_2025]: https://doi.org/10.7717/peerj-cs.3040
[research_yang_gan_2024]: https://doi.org/10.3390/aerospace11070555
[research_yang_hao_2024]: https://doi.org/10.1088/1742-6596/2820/1/012032
[research_yang_hu_2006]: https://doi.org/10.2514/6.iac-06-d2.4.03
[research_yang_li_2008]: https://doi.org/10.2514/6.2008-374
[research_yang_liu_2021]: https://doi.org/10.1007/978-981-15-8155-7_286
[research_yang_men_2025]: https://doi.org/10.3390/drones9040239
[research_yang_meng_2012]: https://doi.org/10.1007/978-3-642-34390-2_26
[research_yang_qi_2016]: https://doi.org/10.1109/chicc.2016.7554207
[research_yang_qiu_2016]: https://doi.org/10.1109/cgncc.2016.7829103
[research_yang_shi_2018]: https://doi.org/10.1007/s10291-018-0766-2
[research_yang_tan_2014]: https://doi.org/10.1109/cgncc.2014.7007424
[research_yang_wang_2012]: https://doi.org/10.4028/www.scientific.net/amm.236-237.378
[research_yang_wang_2013]: https://doi.org/10.1109/icinfa.2013.6720343
[research_yang_wang_2017]: https://doi.org/10.1007/978-981-10-4591-2_18
[research_yang_wang_2022]: https://doi.org/10.3390/aerospace9040219
[research_yang_wu_2022]: https://doi.org/10.1088/1742-6596/2218/1/012080
[research_yang_yang_2026]: https://doi.org/10.1016/j.measurement.2025.118993
[research_yang_yanguang_2015]: https://doi.org/10.1109/icphm.2015.7245048
[research_yang_ye_2016]: https://doi.org/10.1016/j.actaastro.2016.07.029
[research_yang_ye_2021]: https://doi.org/10.1016/j.ast.2021.106915
[research_yang_zhang_2015]: https://doi.org/10.1360/n092014-00468
[research_yang_zhang_2025]: https://doi.org/10.1007/978-981-96-2268-9_40
[research_yankui_2005]: https://doi.org/10.2514/6.2005-6040
[research_yao_jia_2023]: https://doi.org/10.1109/cac59555.2023.10450574
[research_yao_kan_2025]: https://doi.org/10.1007/978-981-96-2212-2_5
[research_yao_li_2021]: https://doi.org/10.1088/1742-6596/1985/1/012007
[research_yao_li_2025]: https://doi.org/10.1142/s2737480725500062
[research_yao_li_2025_b]: https://doi.org/10.1016/j.cja.2024.08.033
[research_yao_ma_2022]: https://doi.org/10.1109/iaecst57965.2022.10062191
[research_yao_wang_2013]: https://doi.org/10.1007/978-3-319-01273-5_73
[research_yao_wu_2019]: https://doi.org/10.1109/access.2019.2905628
[research_yap_macias_2012]: https://doi.org/10.2514/1.a32156
[research_yarlett_adrezin_2000]: https://doi.org/10.2514/6.2000-1694
[research_yassirfadhilah_mubarok_2024]: https://doi.org/10.25104/mtm.v22i2.2387
[research_yates_1991]: https://ntrs.nasa.gov/citations/19910058938
[research_ye_2023]: https://doi.org/10.1038/d41586-023-01639-0
[research_ye_chaofang_2017]: https://doi.org/10.1109/ccdc.2017.7978401
[research_ye_li_2021]: https://doi.org/10.23919/ccc52363.2021.9549314
[research_ye_wang_2024]: https://doi.org/10.1007/978-981-97-3998-1_124
[research_yee_parkinson_2023]: https://doi.org/10.33599/nasampe/s.23.0039
[research_yelinzhang_yangzhuwang_2016]: https://doi.org/10.1109/cgncc.2016.7828920
[research_yeom_oh_2009]: https://doi.org/10.5139/jksas.2009.37.10.1010
[research_yerdon_cook_2015]: https://doi.org/10.1109/aero.2015.7118938
[research_yi_2011]: https://doi.org/10.1016/j.proeng.2011.10.020
[research_yifan_minghe_2024]: https://doi.org/10.1360/sspma-2024-0302
[research_yilmaz_warren_2019]: https://doi.org/10.2514/6.2019-3122
[research_yin_2024]: https://doi.org/10.2139/ssrn.4923521
[research_yin_li_2024]: https://doi.org/10.1109/meae62008.2024.11026322
[research_yingying_yanshun_2011]: https://doi.org/10.1109/icmtma.2011.634
[research_yip_1987]: https://ntrs.nasa.gov/citations/19870012422
[research_yip_1990]: https://doi.org/10.2514/6.1990-1261
[research_yntema_1952]: https://ntrs.nasa.gov/citations/19930083424
[research_yongjiang_jiecao_2006]: https://doi.org/10.1109/wcica.2006.1714021
[research_yongsheng_2021]: https://doi.org/10.1109/aemcse51986.2021.00271
[research_yongsheng_2021_b]: https://doi.org/10.1109/aemcse51986.2021.00193
[research_yoon_kim_2021]: https://doi.org/10.5139/jksas.2021.49.8.637
[research_yoshinaga_tate_1995]: https://doi.org/10.2514/6.1995-1901
[research_yoshinaga_tate_1996]: https://doi.org/10.2514/3.26813
[research_you_yasaee_2019]: https://doi.org/10.1016/j.compstruct.2019.111255
[research_young_1966]: https://doi.org/10.1038/2091163b0
[research_youssef_2001]: https://ntrs.nasa.gov/citations/20010067392
[research_yu_baek_2025]: https://doi.org/10.52202/083075-0025
[research_yu_cai_2017]: https://doi.org/10.1017/s0373463317000327
[research_yu_li_2018]: https://doi.org/10.1016/j.actaastro.2018.09.022
[research_yu_li_2019]: https://doi.org/10.1016/j.asr.2018.09.035
[research_yu_ni_2021]: https://doi.org/10.1155/2021/8885074
[research_yu_sun_2014]: https://doi.org/10.4028/www.scientific.net/amm.668-669.406
[research_yu_wang_2017]: https://doi.org/10.1016/j.ast.2017.06.026
[research_yu_wang_2026]: https://doi.org/10.1016/j.ast.2026.112132
[research_yu_xu_2015]: https://doi.org/10.2514/6.2015-1331
[research_yu_yang_2020]: https://doi.org/10.1007/s11071-020-05915-w
[research_yu_zhang_2024]: https://doi.org/10.1007/s40747-024-01579-w
[research_yuan_gong_2006]: https://doi.org/10.1155/2006/204289
[research_yuan_he_2025]: https://doi.org/10.1007/978-981-96-2212-2_15
[research_yuan_sun_2019]: https://doi.org/10.23919/chicc.2019.8866189
[research_yuan_xu_2022]: https://doi.org/10.1142/s2737480722500236
[research_yuan_zhu_2018]: https://doi.org/10.1109/aero.2018.8396462
[research_yue_lian_2017]: https://doi.org/10.1007/978-981-10-4591-2_32
[research_yue_lin_2022]: https://doi.org/10.1016/j.cja.2022.06.022
[research_yue_titurus_2019]: https://doi.org/10.1016/j.ymssp.2018.11.034
[research_yue_titurus_2022]: https://doi.org/10.1007/s11071-022-07944-z
[research_yue_yuan_2002]: https://doi.org/10.2514/6.2002-4827
[research_yue_zuo_2022]: https://doi.org/10.1109/taes.2022.3143481
[research_yun_seo_2019]: https://doi.org/10.2514/6.2019-4267
[research_yutaakai_kenjiuchiyama_2007]: https://doi.org/10.1109/iccas.2007.4406924
[research_zahn_nd]: https://ntrs.nasa.gov/citations/20240008754
[research_zakharin_ponomarenko_2023]: https://doi.org/10.1109/msnmc61017.2023.10329195
[research_zakrajsek_vogel_2017]: https://doi.org/10.2514/6.2017-0352
[research_zammitmangion_zammit_2006]: https://doi.org/10.2514/6.2006-6271
[research_zavalishin_zatuchny_2021]: https://doi.org/10.1007/978-981-16-0073-9_1
[research_zeiler_mcghee_1999]: https://doi.org/10.2514/2.3434
[research_zeng_wang_2026]: https://doi.org/10.1016/j.ast.2026.113306
[research_zeyuan_huahui_2021]: https://doi.org/10.1109/icetci53161.2021.9563537
[research_zhai_qi_2016]: https://doi.org/10.1109/chicc.2016.7554394
[research_zhai_qi_2019]: https://doi.org/10.1016/j.isatra.2019.01.005
[research_zhang_1992]: https://doi.org/10.21236/ada254307
[research_zhang_2008]: https://doi.org/10.1109/chicc.2008.4605457
[research_zhang_2011]: https://doi.org/10.3901/cjme.2011.02.277
[research_zhang_2015]: https://doi.org/10.2514/6.2015-3500
[research_zhang_2019]: https://doi.org/10.1109/access.2019.2911025
[research_zhang_2024]: https://doi.org/10.54097/rxvm3q06
[research_zhang_bai_2023]: https://doi.org/10.1007/978-981-19-6613-2_137
[research_zhang_cai_2007]: https://doi.org/10.2514/6.2007-6132
[research_zhang_cai_2024]: https://doi.org/10.1007/978-981-99-8048-2_269
[research_zhang_chang_2022]: https://doi.org/10.1007/978-981-16-9492-9_283
[research_zhang_chen_2011]: https://doi.org/10.2514/6.2011-2231
[research_zhang_chen_2023]: https://doi.org/10.1007/978-981-19-6613-2_436
[research_zhang_chen_2026]: https://doi.org/10.1016/j.ast.2026.112946
[research_zhang_ding_2023]: https://doi.org/10.1177/00202940231154856
[research_zhang_gao_2023]: https://doi.org/10.3390/en16041740
[research_zhang_gray_2005]: https://doi.org/10.2514/6.2005-6430
[research_zhang_guo_2017]: https://doi.org/10.2514/6.2017-2372
[research_zhang_han_2025]: https://doi.org/10.1007/978-981-96-7352-0_11
[research_zhang_han_2025_b]: https://doi.org/10.1002/asjc.3839
[research_zhang_hu_2021]: https://doi.org/10.1109/tnnls.2021.3080980
[research_zhang_hu_2025]: https://doi.org/10.1142/s021945542750088x
[research_zhang_jia_2013]: https://doi.org/10.1109/mic.2013.6758104
[research_zhang_jing_2021]: https://doi.org/10.1108/aeat-11-2020-0253
[research_zhang_li_2017]: https://doi.org/10.1109/icmsc.2017.7959475
[research_zhang_li_2019]: https://doi.org/10.1007/978-981-15-0474-7_107
[research_zhang_li_2019_d]: https://doi.org/10.3390/s19061426
[research_zhang_li_2021]: https://doi.org/10.1007/978-981-15-8155-7_298
[research_zhang_liao_2026]: https://doi.org/10.1016/j.ast.2026.111885
[research_zhang_lin_2014]: https://doi.org/10.1117/1.oe.53.7.074112
[research_zhang_lin_2021]: https://doi.org/10.1109/cac53003.2021.9728665
[research_zhang_liu_2016]: https://doi.org/10.1155/2016/4892376
[research_zhang_liu_2023]: https://doi.org/10.23919/ccc58697.2023.10240656
[research_zhang_ma_2025]: https://doi.org/10.3390/act14030114
[research_zhang_mu_2017]: https://doi.org/10.1109/icmic.2017.8321683
[research_zhang_mu_2021]: https://doi.org/10.1016/j.ast.2021.106825
[research_zhang_nie_2020]: https://doi.org/10.3390/app10144856
[research_zhang_selezneva_2022]: https://doi.org/10.1109/rusautocon54946.2022.9896327
[research_zhang_shi_2016]: https://doi.org/10.1117/1.oe.55.4.044102
[research_zhang_shou_2022]: https://doi.org/10.1016/j.neucom.2021.10.084
[research_zhang_sun_2013]: https://doi.org/10.1007/978-3-642-42057-3_81
[research_zhang_sun_2016]: https://doi.org/10.1109/icrms.2016.8050105
[research_zhang_tang_2017]: https://doi.org/10.1016/j.isatra.2017.08.012
[research_zhang_wan_2009]: https://doi.org/10.1109/iciecs.2009.5366427
[research_zhang_wang_2013]: https://doi.org/10.1109/icinfa.2013.6720345
[research_zhang_wang_2016]: https://doi.org/10.1016/j.ast.2016.08.020
[research_zhang_wang_2017]: https://doi.org/10.2322/tjsass.60.35
[research_zhang_wang_2022]: https://doi.org/10.1109/igarss46834.2022.9884023
[research_zhang_wang_2023]: https://doi.org/10.1109/iscsic60498.2023.00034
[research_zhang_wang_2023_b]: https://doi.org/10.1117/12.3007651
[research_zhang_wang_2024]: https://doi.org/10.1088/1742-6596/2791/1/012041
[research_zhang_wang_2025]: https://doi.org/10.1007/978-981-96-3552-8_23
[research_zhang_wang_2025_b]: https://doi.org/10.1063/5.0268125
[research_zhang_wang_2025_c]: https://doi.org/10.23919/cje.2023.00.339
[research_zhang_wang_2025_d]: https://doi.org/10.1109/ccdc65474.2025.11090906
[research_zhang_wei_2017]: https://doi.org/10.1109/icmae.2017.8038731
[research_zhang_wei_2018]: https://doi.org/10.1016/j.ast.2018.08.028
[research_zhang_wei_2019]: https://doi.org/10.1007/978-981-13-3305-7_204
[research_zhang_wei_2019_b]: https://doi.org/10.1016/j.actaastro.2019.03.078
[research_zhang_wu_2017]: https://doi.org/10.2514/6.2017-2320
[research_zhang_xu_2022]: https://doi.org/10.1016/j.actaastro.2022.05.021
[research_zhang_yang_2015]: https://doi.org/10.1080/13588265.2015.1033971
[research_zhang_yin_2025]: https://doi.org/10.1007/978-981-96-2228-3_25
[research_zhang_yu_2018]: https://doi.org/10.1109/gncc42960.2018.9018888
[research_zhang_yu_2024]: https://doi.org/10.1016/j.renene.2024.120541
[research_zhang_yuan_2026]: https://doi.org/10.1061/jaeeez.aseng-6418
[research_zhang_zhai_2019]: https://doi.org/10.3390/s19020408
[research_zhang_zhai_2019_b]: https://doi.org/10.1109/access.2019.2893062
[research_zhang_zhang_2011]: https://doi.org/10.1061/41184(419)500
[research_zhang_zhang_2020_b]: https://doi.org/10.1016/j.actaastro.2019.11.012
[research_zhang_zhang_2022]: https://doi.org/10.1016/j.isatra.2021.04.031
[research_zhang_zhang_2023]: https://doi.org/10.1007/978-981-19-6613-2_244
[research_zhang_zhou_2022]: https://doi.org/10.2514/1.g006504
[research_zhang_zong_2017]: https://doi.org/10.23919/chicc.2017.8027798
[research_zhangdayong_wuwenqi_2008]: https://doi.org/10.1109/chicc.2008.4605362
[research_zhao_2024]: https://doi.org/10.1007/978-981-97-7135-6_5
[research_zhao_blunt_2023]: https://doi.org/10.3390/s23052396
[research_zhao_chen_2014]: https://doi.org/10.3182/20140824-6-za-1003.01658
[research_zhao_cui_2011]: https://doi.org/10.1109/icqr2mse.2011.5976742
[research_zhao_he_2018]: https://doi.org/10.1109/gncc42960.2018.9019043
[research_zhao_he_2021]: https://doi.org/10.1016/j.actaastro.2021.02.036
[research_zhao_li_2013]: https://doi.org/10.4028/www.scientific.net/amm.462-463.809
[research_zhao_li_2020]: https://doi.org/10.1155/2020/4313758
[research_zhao_pei_2012]: https://doi.org/10.1016/j.phpro.2012.05.157
[research_zhao_pei_2013]: https://doi.org/10.4304/jmm.8.2.90-97
[research_zhao_sheng_2014]: https://doi.org/10.1109/cgncc.2014.7007465
[research_zhao_tang_2015]: https://doi.org/10.2991/icismme-15.2015.71
[research_zhao_wang_2016]: https://doi.org/10.1109/aus.2016.7748091
[research_zhao_yang_2013]: https://doi.org/10.1061/(asce)as.1943-5525.0000174
[research_zhao_zhao_2024]: https://doi.org/10.1177/16878132241300197
[research_zhao_zhou_2013]: https://doi.org/10.1016/j.cja.2013.10.009
[research_zhao_zhou_2019]: https://doi.org/10.23919/icins.2019.8769359
[research_zhen_jiang_2018]: https://doi.org/10.1016/j.ast.2018.07.039
[research_zhen_peng_2019]: https://doi.org/10.1109/access.2019.2957740
[research_zheng_2021]: https://doi.org/10.11648/j.ijmea.20210901.14
[research_zheng_jin_2017]: https://doi.org/10.1109/access.2017.2671440
[research_zheng_liang_2014]: https://doi.org/10.1109/cgncc.2014.7007564
[research_zheng_liu_2018]: https://doi.org/10.1109/gncc42960.2018.9019166
[research_zheng_selezneva_2022]: https://doi.org/10.1109/rusautocon54946.2022.9896297
[research_zheng_sergeevna_2022]: https://doi.org/10.1088/1742-6596/2235/1/012024
[research_zheng_wang_2019]: https://doi.org/10.1088/1757-899x/631/4/042055
[research_zheng_yin_2025]: https://doi.org/10.1007/978-981-97-7887-4_43
[research_zheng_zou_2025]: https://doi.org/10.3390/math13243911
[research_zhengchun_2018]: https://doi.org/10.1109/gncc42960.2018.9018936
[research_zhi_liu_2022]: https://doi.org/10.1016/j.measurement.2021.110516
[research_zhi_ran_2015]: https://doi.org/10.1016/j.proeng.2014.12.633
[research_zhicong_voronko_2023]: https://doi.org/10.36074/grail-of-science.17.02.2023.070
[research_zhihuizheng_haipingwei_2016]: https://doi.org/10.1109/cgncc.2016.7829098
[research_zhimin_guanxin_2008]: https://doi.org/10.2514/6.2008-6335
[research_zhiqiang_huiping_2015]: https://doi.org/10.1109/ccdc.2015.7162451
[research_zhishuai_di_2023]: https://doi.org/10.1007/978-981-19-6613-2_33
[research_zhixin_2022]: https://doi.org/10.1109/icmeas57305.2022.00056
[research_zhong_liu_2017]: https://doi.org/10.1017/s037346331600076x
[research_zhongping_2023]: https://doi.org/10.1007/978-981-99-8864-8_53
[research_zhou_2025]: https://doi.org/10.1109/aaac66612.2025.11427469
[research_zhou_2026]: https://doi.org/10.1088/1742-6596/3242/1/012057
[research_zhou_feng_2023]: https://doi.org/10.1007/978-981-19-6613-2_303
[research_zhou_jin_2023]: https://doi.org/10.3390/app13126951
[research_zhou_knedlik_2010]: https://doi.org/10.2514/6.2010-8190
[research_zhou_li_2023]: https://doi.org/10.1007/978-981-19-6613-2_64
[research_zhou_liang_2019]: https://doi.org/10.1115/gt2019-91112
[research_zhou_neusypin_2023]: https://doi.org/10.3390/engproc2023033066
[research_zhou_ohashi_2020]: https://doi.org/10.1109/tencon50793.2020.9293862
[research_zhou_takaba_2019]: https://doi.org/10.1109/icamechs.2019.8861664
[research_zhou_wan_2026]: https://doi.org/10.1016/j.cja.2025.103581
[research_zhou_wang_1987]: https://doi.org/10.1016/0094-5765(87)90016-6
[research_zhou_wang_2012]: https://doi.org/10.4028/www.scientific.net/amr.433-440.1519
[research_zhou_wang_2020]: https://doi.org/10.1016/j.ast.2019.105678
[research_zhou_xiao_2015]: https://doi.org/10.2514/6.2015-3536
[research_zhou_yang_2013]: https://doi.org/10.1007/978-3-642-37407-4_50
[research_zhou_yang_2024]: https://doi.org/10.3390/act13120523
[research_zhou_zheng_2020]: https://doi.org/10.1109/icarcv50220.2020.9305317
[research_zhou_zheng_2023]: https://doi.org/10.1007/978-981-19-6613-2_9
[research_zhou_zhong_2021]: https://doi.org/10.1007/978-981-15-4972-4_7
[research_zhou_zhong_2021_b]: https://doi.org/10.1007/978-981-15-4972-4_2
[research_zhou_zhou_2013]: https://doi.org/10.4028/www.scientific.net/amm.446-447.611
[research_zhou_zuo_2024]: https://doi.org/10.1109/meae62008.2024.11026451
[research_zhu_2024]: https://doi.org/10.1117/12.3039854
[research_zhu_bai_2021]: https://doi.org/10.1007/978-981-15-8155-7_194
[research_zhu_lee_2025]: https://doi.org/10.1109/icns65417.2025.10976907
[research_zhu_li_2016]: https://doi.org/10.1109/cgncc.2016.7828860
[research_zhu_liu_2015]: https://doi.org/10.1109/ccdc.2015.7162611
[research_zhu_liu_2021]: https://doi.org/10.1007/978-981-15-8155-7_96
[research_zhu_wang_2021]: https://doi.org/10.1007/978-981-16-7423-5_19
[research_zhu_wang_2025]: https://doi.org/10.1007/978-981-96-2200-9_8
[research_zhu_yang_2020]: https://doi.org/10.1016/j.compeleceng.2020.106637
[research_zhu_zhang_2024]: https://doi.org/10.1016/j.measurement.2024.114432
[research_zhuqidan_wangtong_2009]: https://doi.org/10.1109/ccdc.2009.5191918
[research_zhuqidan_wangtong_2009_b]: https://doi.org/10.1109/ccdc.2009.5194878
[research_zhuqidan_zhangwen_2009]: https://doi.org/10.1109/ccdc.2009.5192852
[research_zieja_kosinski_2015]: https://doi.org/10.5604/12314005.1137866
[research_zilong_zhaokui_2019]: https://doi.org/10.2514/1.a34265
[research_zimmerman_2002]: https://ntrs.nasa.gov/citations/20020065568
[research_zimmerman_dukeman_2003]: https://doi.org/10.2514/2.5096
[research_zimpfer_1999]: https://doi.org/10.2514/6.1999-4210
[research_zong_wang_2013]: https://doi.org/10.1177/0954410013482238
[research_zou_chen_2025]: https://doi.org/10.1177/09544100251350344
[research_zubrin_clapp_1996]: https://doi.org/10.2514/6.1996-4605
[research_zucker_1970]: https://doi.org/10.5957/jsr.1970.14.2.135
[research_zumwalt_cruz_2016]: https://doi.org/10.2514/6.2016-3882
[research_zuppardi_mongelluzzo_2023]: https://doi.org/10.2514/1.a35489
[research_zuppardi_mongelluzzo_2023_b]: https://doi.org/10.2514/1.a35665
[research_zwirglmaier_drees_2014]: https://doi.org/10.1201/b17399-279
